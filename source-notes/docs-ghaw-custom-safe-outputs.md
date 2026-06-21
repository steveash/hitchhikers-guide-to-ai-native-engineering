---
source_url: https://github.github.com/gh-aw/reference/custom-safe-outputs
source_type: docs
title: "GitHub Agentic Workflows: Custom Safe Outputs Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-06-21
last_checked: 2026-06-21
status: current
confidence_overall: emerging
issue: "#378"
---

# GitHub Agentic Workflows: Custom Safe Outputs Reference

> The practitioner reference guide for implementing Custom Safe Outputs in gh-aw —
> documents the three handler types (Scripts, Actions, Jobs), the complete Safe Job
> Reference (required/optional properties, input types, job ordering with `needs:`),
> how to access agent output via `GH_AW_AGENT_OUTPUT`, staged mode integration, and
> troubleshooting patterns; extends `docs-ghaw-safe-outputs-specification.md` from
> normative requirements to hands-on implementation.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows reference page, in the `reference/`
  section — the same section as `docs-ghaw-staged-mode-reference.md` and
  `docs-ghaw-permissions-reference.md`. Reference pages document platform feature syntax
  and behavior, not practitioner patterns or conceptual overviews. This page is the
  implementation counterpart to `docs-ghaw-safe-outputs-specification.md`, which
  establishes the normative security requirements; this page provides the hands-on
  configuration reference.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's agent factory blog series and the `gh aw`
  platform. Claims about job properties, handler type behavior, compilation mechanics,
  and environment variable contracts are authoritative for this platform. The page has
  the same provenance as the Safe Outputs MCP Gateway Specification.
- **Scope**: Creating Custom Safe Outputs (two-step procedure, three handler types),
  Safe Job Reference (required and optional job properties, input types, job ordering
  via `needs:`, accessing agent output via `GH_AW_AGENT_OUTPUT`), and Troubleshooting
  (duplicate names, tool visibility, silent failures, tool selection confusion). Does
  NOT cover: the normative security invariants (SP1-SP6) or conformance classes (C1/C2)
  — those are in `docs-ghaw-safe-outputs-specification.md`; built-in safe output type
  schemas (`create-issue`, `add-comment`, etc.); staged mode YAML syntax in full detail
  (`docs-ghaw-staged-mode-reference.md`); or the broader MCP server configuration for
  read operations (`docs-ghaw-mcps.md`).

## Extracted Claims

### Claim 1: Custom safe outputs extend built-in GitHub operations to integrate with third-party services requiring authentication that built-in safe outputs don't cover

- **Evidence**: The page's overview text names concrete integration targets: "Slack,
  Discord, Notion, Jira, databases, or any external API requiring authentication."
  The design principle is that built-in safe outputs cover GitHub-native write
  operations; custom safe outputs fill the gap for everything else.
- **Confidence**: settled (first-party reference documentation; the claim defines the
  scope of the feature)
- **Quote**: "Custom safe outputs extend built-in GitHub operations to integrate with
  third-party services — Slack, Discord, Notion, Jira, databases, or any external API
  requiring authentication. Use them for any write operation that built-in safe outputs
  don't cover."
- **Our assessment**: The definition is additive: custom safe outputs do not replace
  built-in safe outputs but extend them to the long tail of authenticated write
  integrations. The design principle is identical to the built-in mechanism — agents
  can only declare operations; a separate job executes with credentials. This makes
  custom safe outputs the escape hatch for any integration not already provided by
  the platform. For Ch02 (Harness Engineering): practitioners who need to write to
  Slack, Jira, Notion, or any other external service should reach for custom safe
  outputs rather than embedding credentials in MCP servers.

### Claim 2: The architecture cleanly separates the agent (read-only MCP tools with restricted tool lists) from write operations (custom jobs that execute with secret access after agent completion)

- **Evidence**: The page describes the architectural model explicitly: "The system
  separates concerns: agents use read-only Model Context Protocol (MCP) servers with
  restricted tool lists, while custom jobs handle write operations with secret access
  after agent completion." This mirrors the same separation principle as built-in
  safe outputs but applied to third-party integrations.
- **Confidence**: settled (first-party; this is the design rationale stated for the
  feature)
- **Quote**: (no single verbatim quote; the above is from WebFetch summarization.
  The dual-step procedure confirms: agents call tools from MCP servers; custom jobs
  run post-agent with full secret access — see Concrete Artifacts.)
- **Our assessment**: The "after agent completion" timing is architecturally important:
  custom jobs do not run in parallel with the agent, they run after the agent finishes.
  The agent declares what it wants (via `GH_AW_AGENT_OUTPUT`), then exits, then the
  custom job reads those declarations and executes with credentials. This preserves
  the same privilege separation as the built-in NDJSON pipeline described in
  `docs-ghaw-safe-outputs-specification.md` Claim 3 (AR2: agent-to-processor
  communication via artifact storage). For Ch03 (Safety and Verification): confirm
  that custom safe outputs share the same temporal isolation guarantee — write
  credentials are never present in the agent process's execution context.

### Claim 3: Three handler types exist with different performance and access tradeoffs — Scripts (in-process, no secret access), Actions (public GitHub Actions, SHA-pinned at compile time), Jobs (full GitHub Actions jobs with complete secret access)

- **Evidence**: The page names three distinct handler types under `safe-outputs`:
  `scripts`, `actions`, and `jobs`. Each has a distinct section with its own
  configuration syntax. Scripts: "in-process, in the consolidated safe-outputs job"
  with "fast startup and no extra job allocation overhead." Actions: "any public
  GitHub Action as a once-callable MCP tool." Jobs: "full-featured separate GitHub
  Actions jobs with complete secret access."
- **Confidence**: settled (first-party; the three types are defined with distinct
  configuration schemas and behavioral descriptions)
- **Quote**: "Use `safe-outputs.scripts` to define lightweight inline JavaScript
  handlers that execute inside the consolidated safe-outputs job handler loop."
- **Our assessment**: The three-way split provides a performance/capability tradeoff
  matrix. Scripts are fastest (no job scheduling, in-process execution) but cannot
  access secrets. Actions allow reusing public GitHub Actions ecosystem tooling
  (webhook senders, notification tools, etc.) with compile-time SHA pinning for
  supply chain safety. Jobs are the most flexible (full secret access, multi-step
  workflows, any runner) but incur GitHub Actions job scheduling overhead. For Ch02:
  practitioners should select handler type based on the tradeoff: lightweight
  processing with no secrets → Script; reuse of a published action → Action; complex
  multi-step workflow with secrets → Job. See Concrete Artifacts for configuration
  syntax for all three.

### Claim 4: The `inputs:` schema serves a dual purpose — it is both the MCP tool definition visible to the agent during execution and the validation schema for fields written to `GH_AW_AGENT_OUTPUT`

- **Evidence**: The documentation states this dual-purpose constraint explicitly as a
  key design point: "The inputs: schema serves as both the MCP tool definition visible
  to the agent and validation for the output fields written to GH_AW_AGENT_OUTPUT."
- **Confidence**: settled (first-party; the claim defines the contract between the
  agent-visible interface and the job's received data)
- **Quote**: "The inputs: schema serves as both the MCP tool definition visible to
  the agent and validation for the output fields written to GH_AW_AGENT_OUTPUT."
- **Our assessment**: This dual-purpose design is architecturally elegant and
  practically important. It means there is a single source of truth for what the agent
  can pass and what the job will receive — if the `inputs:` block defines a required
  field, the agent must provide it via MCP, and the job will find it in
  `GH_AW_AGENT_OUTPUT`. Practitioners cannot separately define the tool interface and
  the job input contract. For Ch02: document this constraint clearly. If a job
  property is needed by the custom job but not communicated to the agent, it should
  be an `env:` variable or a secret — it cannot be a "hidden" input not in `inputs:`.

### Claim 5: Agent output is accessed in custom jobs via `GH_AW_AGENT_OUTPUT` — an environment variable pointing to a JSON file with an `items` array where each item's `type` field uses underscores (job name dashes converted)

- **Evidence**: The page documents the `GH_AW_AGENT_OUTPUT` env var explicitly:
  "Custom jobs receive agent output via `GH_AW_AGENT_OUTPUT` environment variable
  pointing to a JSON file with structure containing `items` array where each item's
  `type` field matches the job name with dashes converted to underscores." The JSON
  schema is: `{"items": [{"type": "job_name_with_underscores", "field1": "value1"}]}`.
- **Confidence**: settled (first-party reference documentation; the env var name,
  JSON structure, and dash-to-underscore conversion are authoritative contracts)
- **Quote**: (no single verbatim sentence; the JSON structure and env var name are
  confirmed across multiple fetches — see Concrete Artifacts for the code example)
- **Our assessment**: The dash-to-underscore conversion is a silent naming convention
  that custom job implementors must know. A job named `slack-notify` in the YAML will
  appear as `type: "slack_notify"` in `GH_AW_AGENT_OUTPUT`. Missing this conversion
  causes the items filter to return no results silently. This is confirmed also in
  the Actions handler description: "Action names with dashes convert to underscores
  when registered as tools." For Ch02: always document the dash→underscore conversion
  as the first check when debugging a custom job that receives no agent output.

### Claim 6: `needs:` enables job sequencing relative to other workflow jobs, including built-in jobs; valid targets are validated at compile time with cycle rejection

- **Evidence**: The `needs:` optional property is defined as: "Jobs that must complete
  before this job runs." The page names valid targets: `agent`, `safe_outputs`,
  `detection`, `upload_assets`, `unlock`, and custom job names. The compiler validates
  entries at compile time and rejects self-dependencies or cycles. The documentation
  adds: "declaring `needs:` in the frontmatter persists across recompiles, unlike
  manual patches."
- **Confidence**: settled (first-party reference documentation; the valid target
  names and compile-time validation behavior are authoritative)
- **Quote**: (no single verbatim quote; the list of valid targets and the
  compile-time validation behavior are described in the Safe Job Reference section
  — see property descriptions in Concrete Artifacts)
- **Our assessment**: `needs:` is the mechanism for custom safe output jobs that must
  run after other jobs (e.g., run the Jira update only after the GitHub issue is
  created by the built-in safe output). The compile-time validation of cycle detection
  prevents configuration errors from reaching runtime. The "persists across recompiles"
  note is important for practitioners who edit workflow files: `needs:` in frontmatter
  is authoritative over manually patched `.lock.yml` values, which would be overwritten
  on next compile. For Ch02: document `needs:` as the ordering mechanism for custom
  safe output sequencing, and note the valid built-in job names.

### Claim 7: The `safe-outputs.actions` handler type pins public GitHub Actions to a specific SHA at compile time — `gh aw compile` fetches `action.yml` to resolve inputs

- **Evidence**: The Actions section states: "At compile time, `gh aw compile` fetches
  the action's `action.yml` to resolve its inputs and pins the action reference to a
  specific SHA."
- **Confidence**: settled (first-party; the compile-time behavior is described
  explicitly alongside the configuration syntax)
- **Quote**: "At compile time, `gh aw compile` fetches the action's `action.yml` to
  resolve its inputs and pins the action reference to a specific SHA."
- **Our assessment**: This compile-time SHA pinning is a supply chain defense — it
  prevents a malicious or accidental update to a public action from affecting running
  workflows. The same pinning behavior is documented in `docs-ghaw-compilation-process.md`
  Claim 1 for action pinning as Phase 4 of the compilation pipeline, confirming this
  is a platform-wide mechanism applied consistently to the Actions handler type. The
  description field must be provided manually (the `action.yml` provides inputs, not
  a human-readable description for the agent). For Ch03 (Safety and Verification):
  the compile-time SHA pinning of Actions handler types is an automatic supply chain
  defense that practitioners get without extra configuration — unlike manually pinning
  actions in `.lock.yml`.

### Claim 8: Scripts (`safe-outputs.scripts`) execute in-process without secret access, making them suitable for lightweight processing; Jobs (`safe-outputs.jobs`) run as separate GitHub Actions jobs with complete secret access

- **Evidence**: Scripts: "Scripts run 'in-process, in the consolidated safe-outputs
  job' with fast startup and no extra job allocation overhead. They lack direct secret
  access but are ideal for lightweight processing without scheduling delays." Jobs:
  the handler type description confirms "separate GitHub Actions job for each tool
  call" with "full secret access."
- **Confidence**: settled (first-party; the in-process vs. separate-job distinction
  and the secret access gap are stated for Scripts)
- **Quote**: (no single verbatim; the secret access constraint appears in the
  summary fetch as "They lack direct secret access" — treat as paraphrase. See
  Concrete Artifacts for the Scripts configuration syntax with code.)
- **Our assessment**: The secret access constraint on Scripts is the key decision
  factor: if the operation needs to authenticate to an external service, use Jobs
  (or Actions). Scripts are appropriate for transformations, logging, or interactions
  that do not require credentials. The "consolidated safe-outputs job" execution
  context means Scripts share the workflow's permission scope, not a custom
  `permissions:` block — practitioners cannot grant Scripts elevated permissions
  the way they can grant `permissions:` to a Job. For Ch02: make the secret access
  gap explicit in any decision tree for handler type selection.

### Claim 9: Custom jobs integrate with staged mode via the `GH_AW_SAFE_OUTPUTS_STAGED` environment variable — when `'true'`, jobs must skip real operations and display previews using `core.summary`

- **Evidence**: The page documents the staged mode integration contract for custom
  jobs: "When `GH_AW_SAFE_OUTPUTS_STAGED === 'true'`, skip actual operations and
  display previews using `core.summary` instead." The staged mode behavior for
  custom jobs is NOT automatic — implementors must check the env var and branch on it.
- **Confidence**: settled (first-party; the env var name and expected branching
  behavior are authoritative)
- **Quote**: "When `GH_AW_SAFE_OUTPUTS_STAGED === 'true'`, skip the real operation
  and display a preview using `core.summary`."
- **Our assessment**: This is a critical implementation responsibility. Built-in safe
  outputs handle staged mode automatically (per `docs-ghaw-staged-mode-reference.md`
  Claim 1: "runs the workflow completely while skipping every write operation"). Custom
  safe output jobs do NOT get this automatically — each implementor must add the
  `GH_AW_SAFE_OUTPUTS_STAGED` check. A custom job that ignores this env var will
  execute real write operations even when the workflow is in staged mode, silently
  violating the staged-mode guarantee. For Ch02: this is a mandatory implementation
  requirement for any custom safe output job intended for use in staged-mode
  workflows. The check should be one of the first steps in any custom job's script.
  For Ch03: staged mode coverage of custom jobs requires implementor discipline — the
  platform cannot enforce it for third-party service calls.

### Claim 10: Required job properties are `description`, `runs-on`, `inputs`, and `steps`; optional properties include `output`, `needs`, `permissions`, `env`, `if`, and `timeout-minutes`

- **Evidence**: The Safe Job Reference section provides a property table. Required:
  `description` ("Tool description shown to the agent"), `runs-on` ("GitHub Actions
  runner (e.g., `ubuntu-latest`)"), `inputs` ("Tool parameters (see Input Types)"),
  `steps` ("GitHub Actions steps to execute"). Optional: `output` ("Success message
  returned to the agent"), `needs` ("Jobs that must complete before this job runs"),
  `permissions` ("GitHub token permissions for the job"), `env` ("Environment
  variables for all steps"), `if` ("Conditional execution expression"),
  `timeout-minutes` ("Maximum job duration (GitHub Actions default: 360)").
- **Confidence**: settled (first-party reference documentation; the property table
  is the authoritative schema for the `safe-outputs.jobs` handler type)
- **Quote**: "Tool description shown to the agent"
- **Our assessment**: The `description` property is both a required field and the
  agent-visible tool documentation — the agent selects which custom safe output to
  call based on this description. A vague or duplicate description causes tool
  selection confusion (see Claim 11). The `output` property is the success message
  returned to the agent after job completion — without it, the agent receives no
  confirmation of the write operation. The `permissions:` block allows scoping the
  GitHub token to minimum necessary scope per-job, which is a good practice for
  security hygiene even when the job uses external API credentials (which use secrets,
  not the GitHub token). For Ch02: document all ten properties; emphasize `description`
  quality as the agent-facing interface.

### Claim 11: Three input types are supported — `string` (text), `boolean` (string values `"true"` or `"false"`), and `choice` (selection from predefined options array)

- **Evidence**: The Input Types section documents three types: "String inputs: Text
  input for general textual parameters. Boolean inputs: 'True/false (as strings:
  `"true"` or `"false"`.) for binary yes/no values. Choice inputs: Selection from
  predefined options allowing agents to pick from enumerated values." Each requires
  `description`, `required`, and `type` fields; boolean supports `default`; choice
  requires `options` array.
- **Confidence**: settled (first-party reference documentation; the three types and
  their constraints are authoritative)
- **Quote**: "True/false (as strings: `\"true\"` or `\"false\"`)"
- **Our assessment**: The boolean-as-string constraint is easy to miss and causes
  type errors if implementors try to compare against JS-native `true`/`false`. The
  agent passes `"true"` or `"false"` as string values, not JSON booleans. The
  choice type is the most constrained — the agent can only select from the
  `options` array, which prevents free-form injection into enumerated parameters.
  This makes choice inputs the preferred type wherever the set of valid values is
  known. For Ch02: document the boolean-as-string constraint explicitly and show
  a defensive comparison pattern (e.g., `item.notify === "true"` not `item.notify`).

### Claim 12: Four troubleshooting patterns address the most common custom safe output failures — duplicate names, tool visibility, silent failures, and tool selection confusion

- **Evidence**: The troubleshooting section names four failure patterns:
  "Duplicate names: Jobs with duplicate names cause compilation errors — rename to
  resolve conflicts." "Tool visibility issues: Ensure `inputs` and `description` are
  defined; verify import path; run `gh aw compile`." "Silent failures: Add
  `core.info()` logging and ensure `core.setFailed()` is called on errors."
  "Tool selection confusion: Make `description` specific and unique; explicitly
  mention job name in prompt."
- **Confidence**: settled (first-party; the four patterns and their resolutions are
  explicitly enumerated in the page's troubleshooting section)
- **Quote**: "Jobs with duplicate names cause compilation errors - rename to resolve
  conflicts."
- **Our assessment**: These four patterns cover the complete failure lifecycle:
  compilation failure (duplicate names), silent misconfiguration at build time (tool
  visibility — missing `inputs` or `description`), runtime failure with no signal
  (silent failures — missing `core.setFailed()`), and correct execution but wrong
  tool selected (tool selection confusion — vague `description`). The "tool selection
  confusion" pattern is particularly relevant for multi-tool workflows where the agent
  might call the wrong custom safe output if descriptions overlap. For Ch02: present
  these four troubleshooting patterns as the diagnostic checklist for any custom safe
  output that isn't working; they cover misconfiguration at every stage from
  compilation through agent-time tool selection. For Ch01: if a custom safe output
  appears available but never executes, check for silent failure (missing
  `core.setFailed()`) before concluding the tool isn't being called.

## Concrete Artifacts

### Custom Safe Output Creation Procedure (two-step)

```
Step 1: Define shared configuration in .github/workflows/shared/
  - Combine MCP server definition (optional) with custom job(s)
  - Job must declare: description, runs-on, inputs, steps

Step 2: Import into workflow via the imports: field
  imports:
    - shared/slack-notify.md
    - shared/jira-integration.md
```

*Source: custom-safe-outputs reference page — "Creating a Custom Safe Output" section*

### Handler Type: Scripts (`safe-outputs.scripts`)

```yaml
safe-outputs:
  scripts:
    post-slack-message:
      description: Post a message to a Slack channel
      inputs:
        channel:
          description: Slack channel name
          required: true
          type: string
        message:
          description: Message text
          required: true
          type: string
      script: |
        const targetChannel = item.channel || "#general";
        const text = item.message || "(no message)";
        core.info(`Posting to ${targetChannel}: ${text}`);
        return { success: true, channel: targetChannel };
```

*Source: custom-safe-outputs reference page — "Scripts" section*
Note: Scripts run in-process; `item` is the agent output record for this tool call.
No direct secret access — use Jobs for operations requiring credentials.

### Handler Type: Actions (`safe-outputs.actions`)

```yaml
safe-outputs:
  actions:
    add-smoked-label:
      uses: actions-ecosystem/action-add-labels@v1
      description: Add the 'smoked' label to the current pull request
      env:
        GITHUB_TOKEN: ${{ github.token }}
```

*Source: custom-safe-outputs reference page — "Actions" section*
Note: At compile time, `gh aw compile` pins the action reference to a specific SHA.
Action names with dashes convert to underscores when registered as tools.

### Handler Type: Jobs (`safe-outputs.jobs`) — Notion example

```yaml
safe-outputs:
  jobs:
    notion-add-comment:
      description: "Add a comment to a Notion page"
      runs-on: ubuntu-latest
      output: "Comment added to Notion successfully!"
      permissions:
        contents: read
      inputs:
        page_id:
          description: "The Notion page ID to add a comment to"
          required: true
          type: string
        comment:
          description: "The comment text to add"
          required: true
          type: string
      steps:
        - name: Add comment to Notion page
          uses: actions/github-script@v8
          env:
            NOTION_TOKEN: "${{ secrets.NOTION_TOKEN }}"
          with:
            script: |
              const fs = require('fs');
              const notionToken = process.env.NOTION_TOKEN;
              const outputFile = process.env.GH_AW_AGENT_OUTPUT;

              if (!notionToken) {
                core.setFailed('NOTION_TOKEN secret is not configured');
                return;
              }

              if (!outputFile) {
                core.info('No GH_AW_AGENT_OUTPUT environment variable found');
                return;
              }

              const fileContent = fs.readFileSync(outputFile, 'utf8');
              const agentOutput = JSON.parse(fileContent);

              const items = agentOutput.items.filter(item =>
                item.type === 'notion_add_comment'
              );

              for (const item of items) {
                const pageId = item.page_id;
                const comment = item.comment;
                core.info(`Adding comment to Notion page: ${pageId}`);
              }
```

*Source: custom-safe-outputs reference page — "Jobs" section (Notion example)*
Note: `item.type === 'notion_add_comment'` — dashes in job name converted to underscores.

### Handler Type: Jobs — Slack simple example

```yaml
safe-outputs:
  jobs:
    slack-notify:
      description: "Send a message to Slack"
      runs-on: ubuntu-latest
      output: "Message sent to Slack!"
      inputs:
        message:
          description: "The message to send"
          required: true
          type: string
      steps:
        - name: Send Slack message
          env:
            SLACK_WEBHOOK: "${{ secrets.SLACK_WEBHOOK }}"
          run: |
            PAYLOAD=$(jq -n --arg text "$MESSAGE" '{text: $text}')
            curl -X POST "$SLACK_WEBHOOK" -d "$PAYLOAD"
```

*Source: custom-safe-outputs reference page — "Jobs" section (Slack example)*

### `GH_AW_AGENT_OUTPUT` JSON Structure

```json
{
  "items": [
    {
      "type": "job_name_with_underscores",
      "field1": "value1",
      "field2": "value2"
    }
  ]
}
```

*Source: custom-safe-outputs reference page — "Accessing Agent Output" section*
Note: The `type` field converts dashes in job names to underscores.
Implementors must filter `items` by `type` to get their job's records.

### Input Types Reference

```yaml
inputs:
  message:
    description: "Message content"
    required: true
    type: string
  notify:
    description: "Send notification"
    required: false
    type: boolean
    default: "true"           # boolean default is a string, not JSON boolean
  environment:
    description: "Target environment"
    required: true
    type: choice
    options: ["staging", "production"]
```

*Source: custom-safe-outputs reference page — "Input Types" section*
Warning: boolean inputs are string values `"true"` / `"false"` — compare with
`=== "true"`, not with JS-native `=== true`.

### Staged Mode Integration Pattern for Custom Jobs

```javascript
// Required check at start of every custom job that should honor staged mode
if (process.env.GH_AW_SAFE_OUTPUTS_STAGED === 'true') {
  await core.summary
    .addHeading('Staged Mode Preview')
    .addRaw('Would have posted message: ' + item.message)
    .write();
  return;  // skip real operation
}
// ... real operation below
```

*Source: custom-safe-outputs reference page — "Staged Mode" section*
Note: Custom jobs must implement this check manually. Built-in safe outputs
handle staged mode automatically; custom jobs do NOT.

### Safe Job Properties Reference

```
Required properties:
  description     (string)   Tool description shown to the agent
  runs-on         (string)   GitHub Actions runner (e.g., ubuntu-latest)
  inputs          (object)   Tool parameters (string | boolean | choice)
  steps           (array)    GitHub Actions steps to execute

Optional properties:
  output          (string)   Success message returned to the agent
  needs           (string|array)  Jobs that must complete before this job runs
                             Valid built-in targets: agent, safe_outputs,
                             detection, upload_assets, unlock
  permissions     (object)   GitHub token scope restrictions
  env             (object)   Environment variables for all steps
  if              (string)   Conditional execution expression
  timeout-minutes (number)   Maximum job duration (default: 360)
```

*Source: custom-safe-outputs reference page — "Safe Job Reference" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-mcps.md` Claim 1 ("Custom MCP servers should be read-only. Write
    operations must go through safe outputs or Custom Safe Outputs."): this reference
    page implements that policy in practice — the two-step creation procedure (Claim 2)
    puts read queries in the MCP server config and write operations in custom jobs.
    The policy and the implementation are fully consistent.
  - `docs-ghaw-safe-outputs-specification.md` Claim 3 (AR2: agent-to-processor
    communication via GitHub Actions artifact storage): `GH_AW_AGENT_OUTPUT` is the
    concrete implementation of AR2 for custom safe outputs — the agent writes its
    output to artifact storage, and the custom job reads it via this env var.
  - `docs-ghaw-staged-mode-reference.md` Claim 1 (staged mode runs workflow
    completely while skipping write operations): the `GH_AW_SAFE_OUTPUTS_STAGED`
    contract (Claim 9) is the mechanism that extends staged mode coverage to custom
    jobs. The built-in behavior described in the staged-mode reference is automatic;
    the custom job integration requires implementor action.
  - `docs-ghaw-compilation-process.md` Claim 1 (five-phase compilation pipeline,
    Phase 4: action pinning): the `safe-outputs.actions` handler type's compile-time
    SHA pinning (Claim 7) uses the same action-pinning mechanism documented in the
    compilation process as Phase 4.

- **Extends**:
  - `docs-ghaw-safe-outputs-specification.md` Claim 11 (conformance classes C1/C2,
    Custom Safe Outputs builders targeting C2 minimum): this page provides the actual
    implementation patterns that practitioners use to build Custom Safe Outputs. The
    spec establishes the normative requirements (SP1-SP6); this reference page shows
    how to implement them — the two-step creation procedure, handler types, and
    property schemas are the practical realization of the spec's security invariants.
  - `docs-ghaw-safe-outputs-specification.md` Claim 9 (Staged Mode formally defined):
    the spec defines staged mode conceptually; this page provides the custom job
    integration contract (`GH_AW_SAFE_OUTPUTS_STAGED === 'true'`) that extends
    staged mode coverage beyond built-in outputs to custom implementations.
  - `docs-ghaw-how-they-work.md` Claim 5 (Safe Outputs as "pre-approved actions the
    AI can request without write permissions"): Custom Safe Outputs apply the same
    pattern to third-party write operations. The agent requests via MCP tool call
    (not write permissions), the output is declared in `GH_AW_AGENT_OUTPUT`, and
    the custom job executes with credentials post-agent. This page extends the
    concept from GitHub-native operations to any external service.

- **Contradicts**: None. The architectural principles (read-only MCPs, write through
  safe outputs, agent isolation, post-agent execution of write jobs) are fully
  consistent with `docs-ghaw-safe-outputs-specification.md`, `docs-ghaw-mcps.md`,
  and `docs-ghaw-how-they-work.md`. No contradiction issue filed.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **Three handler types (`scripts`, `actions`, `jobs`) with distinct
    performance/access tradeoffs** (Claim 3): No prior corpus note documents that
    custom safe outputs have three subtypes with different execution contexts and
    secret access properties. The spec covers the security architecture; this page
    reveals the implementation surface.
  - **`inputs:` dual-purpose schema** (Claim 4): No prior note states that the
    `inputs:` block serves as both the agent-visible MCP tool definition AND the
    validation schema for `GH_AW_AGENT_OUTPUT`. This is a key design constraint
    with practical implementation consequences.
  - **`GH_AW_AGENT_OUTPUT` env var and dash→underscore type conversion** (Claim 5):
    No prior note documents the exact mechanism by which custom jobs receive agent
    output, the JSON structure, or the dash-to-underscore naming convention for the
    `type` field. This conversion is a silent source of bugs.
  - **`needs:` job ordering with valid built-in targets** (Claim 6): The named valid
    targets (`agent`, `safe_outputs`, `detection`, `upload_assets`, `unlock`) and
    compile-time cycle detection for custom safe output sequencing are not documented
    in any existing corpus note.
  - **`GH_AW_SAFE_OUTPUTS_STAGED` implementor responsibility** (Claim 9): No prior
    note documents that custom jobs must implement staged mode manually — that
    built-in outputs get it automatically but custom jobs do not.
  - **Four troubleshooting patterns** (Claim 12): The diagnostic checklist for custom
    safe output failures (compilation: duplicate names; config: tool visibility;
    runtime: silent failures; agent: tool selection confusion) is not documented in
    any existing corpus note, though `docs-ghaw-troubleshooting-common-issues.md`
    and related notes may overlap. The specific actionable checks here (verify
    `inputs` + `description`, call `core.setFailed()`, make `description` specific)
    are new implementation guidance.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add Custom Safe Outputs as the escape hatch for third-party write integrations**
  (Claim 1): The guide should document Custom Safe Outputs as the recommended pattern
  for any write operation targeting Slack, Jira, Notion, databases, or external APIs.
  Contrast with MCP servers (read-only per `docs-ghaw-mcps.md` Claim 1) and built-in
  safe outputs (GitHub-native writes only). Three-way decision tree: read query →
  MCP server; GitHub write → built-in safe output; third-party write → custom safe
  output.

- **Document the three handler types and their selection criteria** (Claim 3): Guide
  practitioners to select the correct handler type based on: (1) needs secrets? →
  Job or Action; (2) reuses a public GitHub Action? → Action (gets SHA pinning for
  free); (3) lightweight transform, no secrets? → Script. Include the tradeoff table:
  Scripts (fastest, in-process, no secrets), Actions (reuse ecosystem, SHA-pinned),
  Jobs (maximum flexibility, full secret access, scheduling overhead).

- **Document the `inputs:` dual-purpose schema constraint** (Claim 4): The constraint
  that `inputs:` defines both the agent-visible MCP tool interface and the job's
  received data means practitioners cannot hide job configuration from the agent. This
  affects workflow design: if a job needs configuration that should not be agent-controlled
  (e.g., a fixed webhook URL), use `env:` or secrets, not `inputs:`.

- **Document `GH_AW_AGENT_OUTPUT` access pattern and dash→underscore conversion**
  (Claim 5): Include the standard job-start pattern: read `GH_AW_AGENT_OUTPUT`, parse
  JSON, filter items by `type` (with underscores). Warn explicitly about the
  dash→underscore conversion — a job named `jira-create-issue` filters on
  `type === "jira_create_issue"`.

- **Require staged mode integration in custom job implementations** (Claim 9): The
  guide should make `GH_AW_SAFE_OUTPUTS_STAGED` handling a mandatory implementation
  requirement, not an optional enhancement. Any custom job deployed in a workflow
  that may run in staged mode must implement the env var check. Provide the standard
  pattern (check at function start, use `core.summary` for preview, return early).

- **Present the four troubleshooting patterns as a diagnostic checklist** (Claim 12):
  Structure the troubleshooting section as a sequence: (1) compilation fails? →
  check for duplicate job names; (2) tool not visible to agent? → check `inputs` +
  `description` + import path + recompile; (3) tool called but no external effect? →
  check `core.setFailed()` + add `core.info()` logging; (4) wrong tool called? →
  make `description` more specific + mention job name in prompt.

### Chapter 03: Safety and Verification

- **Staged mode coverage gap for custom jobs** (Claim 9): Add an explicit warning
  that custom safe output jobs do not inherit staged mode behavior automatically —
  unlike built-in outputs. A workflow in staged mode that includes custom safe output
  jobs will execute real writes in those jobs unless implementors check
  `GH_AW_SAFE_OUTPUTS_STAGED`. Document this as a safety gap to address in code review.

- **SHA pinning for Actions handler type as automatic supply-chain defense** (Claim 7):
  The `safe-outputs.actions` type provides compile-time SHA pinning at no extra cost.
  Document this as the recommended way to integrate public GitHub Actions into safe
  output workflows — it closes the supply chain risk that comes from using a mutable
  version tag in production code.

## Extraction Notes

1. **WebFetch returns summarized content, not raw HTML**: The gh-aw documentation is
   an Astro/Starlight SPA. Multiple targeted WebFetch calls were made (five total)
   to maximize content fidelity across sections. Verbatim quotes are marked where
   the phrasing was consistent across fetches or sufficiently distinctive to be
   low-risk for summarization artifacts. Claims where specific wording could not be
   verified verbatim are marked "(no direct quote; see paraphrase in Our assessment)".

2. **Code examples are higher confidence than prose**: The JavaScript and YAML code
   blocks were returned consistently across fetches and are assessed as accurately
   captured. The exact naming of properties, the JSON structure of `GH_AW_AGENT_OUTPUT`,
   and the `GH_AW_SAFE_OUTPUTS_STAGED` env var name are all derived from code contexts
   where summarization artifacts are less likely.

3. **No publication date**: The gh-aw documentation does not carry explicit publication
   dates. `date_published` is left null. The content is consistent with the current
   gh-aw platform state as of 2026-06-21.

4. **Troubleshooting quotes are likely paraphrased**: The troubleshooting section
   content (Claim 12) was returned in a format suggesting WebFetch model summarization
   rather than verbatim reproduction. The four category names (duplicate names, tool
   visibility, silent failures, tool selection confusion) and their resolutions are
   confirmed consistent across two fetches. Specific wording should be verified
   against the source if used as direct quotes in the guide.

5. **Staged mode reference page should be read alongside this note**: The
   `docs-ghaw-staged-mode-reference.md` note covers the full staged mode syntax
   and built-in output type behavior; this note covers only the custom job integration
   contract (`GH_AW_SAFE_OUTPUTS_STAGED`). The two notes are complementary and should
   be cited together for complete staged mode guidance.

6. **No contradictions to file**: Reviewed all existing gh-aw source notes referenced
   in the triage comment and related corpus notes. No claims in this source materially
   oppose any existing note. The implementation patterns here are consistent with and
   extend the normative requirements in `docs-ghaw-safe-outputs-specification.md`.
