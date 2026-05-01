---
source_url: https://github.github.com/gh-aw/patterns/dispatch-ops
source_type: docs
title: "GitHub Agentic Workflows: DispatchOps Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-01
last_checked: 2026-05-01
status: current
confidence_overall: emerging
issue: "#325"
---

# GitHub Agentic Workflows: DispatchOps Pattern

> The canonical pattern reference for human-triggered on-demand agentic automation —
> documents the full `workflow_dispatch` security model (role-based access control,
> fork protection, environment approval gates), typed input parameters with Handlebars
> conditionals for behavior branching, and the `gh aw run --wait` synchronous invocation
> pattern; the first source note in the corpus to treat `workflow_dispatch` as a
> first-class design pattern rather than a development-time testing escape hatch.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, Design Patterns >
  DispatchOps section — prescriptive pattern reference, not a blog post or conceptual
  overview. Patterns pages document proven interaction models rather than architectural
  principles.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same
  team behind the "Peli's Agent Factory" blog series and the `gh aw` platform. Claims
  about `workflow_dispatch` trigger schema, role enforcement, fork protection semantics,
  and input type behavior are authoritative for this platform. Claims about
  generalizability of the human-in-the-loop model beyond gh-aw require additional
  evidence.
- **Scope**: The DispatchOps pattern specifically — `workflow_dispatch` trigger syntax,
  `roles:` and `bots:` fields for access control, fork protection as an inherent
  security property, environment approval gates via `manual-approval:`, the four typed
  input parameter types (`string`, `boolean`, `choice`, `environment`), input
  interpolation via `${{ github.event.inputs.INPUT_NAME }}`, Handlebars conditionals for
  behavior branching, CLI invocation patterns (`gh aw run --wait`, `--ref`, `--repo`,
  `--verbose`), and the branch testing development workflow. Does NOT cover: the full
  five-layer security architecture (in `docs-ghaw-how-they-work.md`), compilation model
  (same), scheduled trigger patterns (in `docs-ghaw-dailyops.md`), MCP server integration
  (`docs-ghaw-mcps.md`), or the slash-command ChatOps pattern (`docs-ghaw-chatops.md`).

## Extracted Claims

### Claim 1: DispatchOps positions `workflow_dispatch` as the on-demand human-timing trigger — suited for tasks where humans decide *when* the agent acts, not just *whether* an event occurred

- **Evidence**: The page's opening framing: "DispatchOps enables manual workflow execution
  through the GitHub Actions UI or CLI for on-demand tasks. The `workflow_dispatch` trigger
  allows running workflows with custom inputs whenever needed, suited for research tasks,
  operational commands, testing, and debugging." The framing centers human judgment about
  timing and context, contrasting implicitly with event-driven triggers (which fire on
  repository events) and scheduled triggers (which fire on a clock).
- **Confidence**: anecdotal (design pattern framing from GitHub; no comparative data on
  when dispatch outperforms event-driven alternatives)
- **Quote**: "DispatchOps enables manual workflow execution through the GitHub Actions UI
  or CLI for on-demand tasks."
- **Our assessment**: This framing clarifies the triggering taxonomy. Three trigger classes
  emerge from the gh-aw documentation: (1) event-driven (fires on repository events such
  as push, PR, issue — automated, no human decision); (2) scheduled (fires on a clock —
  `docs-ghaw-dailyops.md`); (3) human-dispatch (fires when a human explicitly runs the
  workflow — this pattern). DispatchOps fills slot 3: the human decides *when* and *with
  what parameters* the agent runs. For Ch02 (Harness Engineering): the trigger taxonomy
  now has all three slots documented — event, schedule, dispatch. For Ch05 / HITL chapters:
  DispatchOps is the primary mechanism for pure human-initiated agentic workflows where
  the trigger itself is a human decision, not just human approval of an automated event.

### Claim 2: The `roles:` field restricts `workflow_dispatch` execution to specific GitHub roles — users must have write access or higher by default

- **Evidence**: The security model section states: "Users must have write access or higher."
  The `roles:` field restricts further:
  ```yaml
  on:
    workflow_dispatch:
      roles: [admin, maintainer]
  ```
  This provides runtime access control at the trigger level, analogous to the `roles:` field
  on `slash_command` triggers in ChatOps (documented in `docs-ghaw-chatops.md` Claim 3).
- **Confidence**: settled (first-party documentation; the `roles:` field and write-access
  default are explicitly documented with YAML examples)
- **Quote**: "Users must have write access or higher" and "Use `roles:` field to restrict
  execution permissions."
- **Our assessment**: The write-access default is a sensible threshold for repositories
  where maintainers want to enable DispatchOps without configuring `roles:` explicitly —
  it excludes read-only contributors and anonymous viewers. The `roles:` field enables
  stricter control (e.g., `[admin, maintainer]` for destructive operational commands that
  even write-access contributors should not run). For Ch03 (Safety): document this as the
  first-line authorization check for DispatchOps workflows. Unlike event-driven triggers
  that fire on any qualifying repository event regardless of actor, DispatchOps applies
  an identity check at the trigger level. Cross-reference with ChatOps Claim 3 —
  identical roles mechanism, same default (write+), same `roles:` override field — the
  two human-trigger patterns share the same access-control model.

### Claim 3: The `bots:` field explicitly authorizes specific bot accounts to trigger `workflow_dispatch` — enabling automated chaining of agentic workflows

- **Evidence**: The security model section documents:
  ```yaml
  on:
    workflow_dispatch:
      bots: ["dependabot[bot]", "github-actions[bot]"]
  ```
  The purpose: "Use `bots:` field to authorize specific bot accounts."
- **Confidence**: settled (first-party documentation; field name and example are explicit)
- **Quote**: "Use `bots:` field to authorize specific bot accounts."
- **Our assessment**: The `bots:` field is novel — no prior source note documents a mechanism
  for explicitly authorizing bot identities to trigger a workflow. This has a significant
  design implication: it means DispatchOps workflows can be chained from other automated
  workflows (e.g., a Dependabot PR triggers a security audit DispatchOps workflow). The
  authorization is explicit and named — wildcards or ambient permissions are not supported
  from this documentation. For Ch09 (Agent Orchestration): the `bots:` field is the
  mechanism for composing dispatch-triggered workflows into multi-agent pipelines where
  an upstream workflow authorizes a downstream DispatchOps invocation. This enables
  patterns like: "when a bot merges a dependency update, dispatch a compatibility
  verification workflow."

### Claim 4: Fork protection is an inherent security property of `workflow_dispatch` — forks cannot trigger workflows in the defining repository, unlike event-driven triggers

- **Evidence**: The security model section states: "`workflow_dispatch` only executes in
  the defining repository—forks cannot trigger parent repository workflows, providing
  inherent attack protection."
- **Confidence**: settled (first-party documentation; this is a GitHub Actions platform
  property that gh-aw inherits, not a gh-aw-specific configuration)
- **Quote**: "`workflow_dispatch` only executes in the defining repository—forks cannot
  trigger parent repository workflows, providing inherent attack protection."
- **Our assessment**: This is a significant security contrast with event-driven triggers.
  Some GitHub Actions events (e.g., `pull_request_target`) can be triggered from forked
  repositories, creating a class of security vulnerabilities (fork-based secret exfiltration).
  `workflow_dispatch` does not have this vulnerability by design — the trigger can only be
  invoked in the workflow's defining repository. This makes DispatchOps inherently safer
  than equivalent event-driven patterns for workflows that access sensitive resources.
  For Ch03 (Safety and Verification): the fork protection property of `workflow_dispatch`
  is a design reason to prefer DispatchOps over event-driven triggers for workflows that
  handle sensitive context, credentials, or consequential operations. It is not a
  configuration — it is a platform-level guarantee.

### Claim 5: The `manual-approval: <environment>` field requires explicit reviewer sign-off before DispatchOps workflow execution — an environment-backed approval gate

- **Evidence**: The security model section documents:
  ```yaml
  on:
    workflow_dispatch:
      manual-approval: production
  ```
  Description: "Configure approval rules, required reviewers, and wait timers in
  Settings → Environments." The `manual-approval:` value names a GitHub environment;
  the environment's protection rules (required reviewers, wait timers) govern when the
  workflow proceeds.
- **Confidence**: settled (first-party documentation; YAML field and environment backing
  are documented explicitly)
- **Quote**: "Configure approval rules, required reviewers, and wait timers in
  Settings → Environments."
- **Our assessment**: This is the strongest human-in-the-loop gate in the DispatchOps
  pattern — a human must explicitly approve execution before the workflow runs, not just
  approve the result after. Combined with the `roles:` field (who can trigger) and
  environment reviewers (who must approve before execution), DispatchOps provides a
  two-factor authorization model: trigger-level identity check + execution-level approval
  gate. For Ch03 (Safety and Verification): the `manual-approval:` field is the canonical
  mechanism for workflows that require explicit human sign-off before agent execution —
  distinct from human approval of agent *outputs* (which is the PR review model in
  `docs-ghaw-how-they-work.md` Claim 10). This is pre-execution approval, not post-execution
  approval. For high-consequence operational workflows (e.g., production deployments,
  destructive cleanup operations), recommend pairing `manual-approval: production` with
  a configured environment that requires named reviewers.

### Claim 6: DispatchOps supports four typed input parameters — `string`, `boolean`, `choice`, `environment` — each with distinct semantics and validation behavior

- **Evidence**: The page documents four types with concrete YAML examples:
  - `string`: free-text input (e.g., `topic: description: 'Research topic', type: string`)
  - `boolean`: true/false toggle
  - `choice`: predefined option list with a default (e.g., `priority: options: [low, medium,
    high], default: medium`)
  - `environment`: auto-populates from Settings → Environments, returns the selected
    environment name as a string without requiring an `options:` list
  The `required:` flag applies to all types.
- **Confidence**: settled (first-party documentation; all four types are shown with explicit
  YAML and behavioral notes)
- **Quote**: "Supported Input Types: `string`, `boolean`, `choice`, `environment`" and
  "The `environment` type auto-populates from Settings → Environments, returning the
  selected name as a string without requiring an `options` list."
- **Our assessment**: The typed input system converts DispatchOps from a simple trigger
  into a parameterized agent invocation interface. The `environment` type is the most
  distinctive: it connects workflow inputs directly to GitHub's environment model, enabling
  workflows like "deploy to [staging | production]" where the option list is derived from
  the repository's configured environments rather than a hardcoded list. This matters for
  security: the environment type integrates with environment protection rules, so a
  `deploy_target: environment` input can trigger environment-specific approval gates.
  For Ch02 (Harness Engineering): the four input types define the parameter vocabulary
  for DispatchOps harnesses. `choice` is the right type for operational modes (e.g.,
  cleanup scope: `[repo | org | all]`); `environment` is the right type for deployment
  target selection; `string` is the right type for free-form research queries; `boolean`
  is the right type for feature flags or verbosity toggles.

### Claim 7: Inputs are interpolated into the workflow's natural language instruction body via `${{ github.event.inputs.INPUT_NAME }}` — enabling parameterized agent instructions

- **Evidence**: The page shows a complete example:
  ```markdown
  Research the following topic: "${{ github.event.inputs.topic }}"
  Analysis depth requested: ${{ github.event.inputs.depth }}
  Provide a ${{ github.event.inputs.depth }} analysis with key findings and recommendations.
  ```
  The interpolation syntax is the standard GitHub Actions expression syntax applied
  directly inside the markdown instruction body of the agentic workflow.
- **Confidence**: settled (first-party documentation; the interpolation pattern is shown
  with a complete working example)
- **Quote**: (from the Research Assistant example)
  `Research the following topic: "${{ github.event.inputs.topic }}"`
- **Our assessment**: The interpolation model means DispatchOps workflows are
  parameterized prompt templates. The human chooses parameter values (topic, depth,
  priority) at invocation time; the platform interpolates those values into the agent's
  instruction body before execution. This is analogous to parameterized SQL queries —
  values are injected at defined binding points rather than concatenated freely. However,
  unlike the ChatOps `steps.sanitized.outputs.text` mechanism (which sanitizes user
  content before injection), `${{ github.event.inputs.INPUT_NAME }}` does not appear to
  pass through a sanitization layer. The input comes from the person invoking the
  workflow (who must have write access or higher per Claim 2), so the injection threat
  model is lower than ChatOps (where any authenticated user can post a comment). For
  Ch02: the `${{ github.event.inputs.INPUT_NAME }}` pattern is the standard input
  interpolation mechanism for DispatchOps instruction bodies. For Ch03: note the
  contrast with ChatOps — dispatch inputs are authorized-user inputs (lower injection
  risk), not open comment-field inputs (higher injection risk).

### Claim 8: Handlebars conditionals enable input-driven behavior branching directly in the workflow's instruction body

- **Evidence**: The page documents two concrete conditional examples:
  ```handlebars
  {{#if (eq github.event.inputs.include_code "true")}}
  Include actual code snippets in your analysis.
  {{else}}
  Describe code patterns without including actual code.
  {{/if}}

  {{#if (eq github.event.inputs.priority "high")}}
  URGENT: Prioritize speed over completeness.
  {{/if}}
  ```
  Both use the `eq` helper to compare input values. The conditionals are processed during
  compilation, before the agent executes.
- **Confidence**: settled (first-party documentation; syntax is shown with explicit
  examples; Handlebars is the documented templating system for gh-aw)
- **Quote**: (from the conditional examples) `{{#if (eq github.event.inputs.priority "high")}} URGENT: Prioritize speed over completeness. {{/if}}`
- **Our assessment**: Handlebars conditionals give DispatchOps workflows a branching
  capability that `${{ }}` interpolation alone cannot provide. The `include_code`
  boolean example demonstrates the pattern for behavioral toggles — the workflow's
  instruction body adapts to the input value. The `priority` example demonstrates
  urgency injection — a "high priority" flag changes the agent's optimization criteria.
  These conditionals are resolved at compile time or invocation time (before the agent
  sees the instructions), keeping the agent's instruction context clean. For Ch02
  (Harness Engineering): Handlebars conditionals are the mechanism for multi-mode
  DispatchOps workflows where the same workflow file covers multiple behavioral variants
  controlled by a `choice` input. This avoids duplicating workflow files for variants
  that differ only in instruction emphasis.

### Claim 9: `gh aw run --wait` enables synchronous on-demand invocation — the caller blocks until the workflow completes

- **Evidence**: The page documents:
  ```bash
  gh aw run research --raw-field topic="AI agents" --wait
  ```
  Additional CLI options documented: `--raw-field KEY=VALUE` for input parameters,
  `--ref branch-name` for branch targeting, `--repo owner/repository` for cross-repo
  targeting, `--verbose` for detailed output.
- **Confidence**: settled (first-party documentation; CLI flags are explicit and named)
- **Quote**: (from the CLI invocation section) `gh aw run research --raw-field topic="AI agents" --wait`
- **Our assessment**: The `--wait` flag converts the async default (fire-and-forget,
  check the Actions UI for results) into a synchronous call that blocks until completion.
  This matters for two use cases: (1) scripted automation that needs workflow output
  before proceeding; (2) developers testing workflows interactively and wanting immediate
  feedback. The `--raw-field` flag for input injection means complex multi-input
  workflows can be fully scripted:
  `gh aw run scout --raw-field topic="AI safety" --raw-field priority=high --wait`.
  For Ch01 (Daily Workflows): `--wait` is the CLI primitive for blocking workflow
  invocation — relevant for scripted DispatchOps that feed into downstream processing.
  For Ch02: the full CLI flag set (`--wait`, `--ref`, `--repo`, `--verbose`) is the
  standard invocation vocabulary for DispatchOps; document these in the harness
  operations section.

### Claim 10: Branch testing combines `--ref` (live repository against a feature branch) and `gh aw trial` (isolated local testing without production side effects)

- **Evidence**: The page documents two testing approaches as complementary:
  ```bash
  gh aw trial ./research.md --raw-field topic="test query"  # isolated, no side effects
  gh aw run research --ref feature/improve-workflow         # live, against the repo
  ```
  Description: "Trial mode provides isolated testing without affecting production;
  branch execution runs against the live repository."
- **Confidence**: settled (first-party documentation; both commands are explicitly
  documented with the distinction between them)
- **Quote**: "Trial mode provides isolated testing without affecting production;
  branch execution runs against the live repository."
- **Our assessment**: The trial-vs-branch distinction is critical for DispatchOps
  development: `gh aw trial` is the safe sandbox (no writes to the repository, no
  production side effects); `gh aw run --ref` is the live-but-branched test (executes
  against the live repository's state, but from the feature branch's workflow definition).
  This extends `docs-ghaw-agentic-authoring.md` Claim 3 (which documents `gh aw trial`
  as a development tool) with a specific two-stage testing workflow: trial first for
  basic correctness, then `--ref` for live integration testing before merging to main.
  For Ch02 (Harness Engineering): recommend the two-stage pattern as the standard
  DispatchOps development loop: `gh aw trial` (local, isolated) → `gh aw run --ref`
  (live, feature branch) → merge.

### Claim 11: DispatchOps is positioned for four use cases — on-demand research, manual operations, testing/debugging, and scheduled workflow testing

- **Evidence**: The page names four documented use cases:
  1. "On-demand research: String input triggered via CLI"
  2. "Manual operations: Choice inputs with predefined operations (cleanup, sync, audit)"
  3. "Testing and debugging: Add to event-triggered workflows with optional test URL inputs"
  4. "Scheduled workflow testing: Combine `schedule` with `workflow_dispatch` for immediate
     testing"
- **Confidence**: anecdotal (use cases are listed without comparison data against
  alternative patterns; no metrics on adoption or effectiveness)
- **Quote**: "DispatchOps enables manual workflow execution... suited for research tasks,
  operational commands, testing, and debugging."
- **Our assessment**: The four use cases reveal an implicit decision heuristic: use
  DispatchOps when (a) the trigger is a human decision about timing and context, not a
  repository event; (b) the task is episodic, not always-on; or (c) the task needs
  specific input parameters that cannot be inferred from repository context alone. The
  "scheduled workflow testing" use case (pairing `schedule` with `workflow_dispatch`) is
  particularly practical — it matches the DailyOps pattern in `docs-ghaw-dailyops.md`
  Claim 2, confirming that the `workflow_dispatch` escape hatch for scheduled workflows
  is a cross-pattern convention. For Ch09 (Agent Orchestration): the four use cases
  define the DispatchOps niche in the trigger taxonomy; teams should evaluate whether
  a proposed workflow fits one of these archetypes before choosing a trigger type.

## Concrete Artifacts

### Basic `workflow_dispatch` Trigger (No Inputs)

```yaml
on:
  workflow_dispatch:
```

*Source: gh-aw DispatchOps patterns documentation, "Basic Syntax" section*

### Parameterized `workflow_dispatch` with All Four Input Types

```yaml
on:
  workflow_dispatch:
    inputs:
      topic:
        description: 'Research topic'
        required: true
        type: string
      priority:
        description: 'Task priority'
        required: false
        type: choice
        options:
          - low
          - medium
          - high
        default: medium
      deploy_target:
        description: 'Deployment environment'
        required: false
        type: environment
        default: staging
```

*Source: gh-aw DispatchOps patterns documentation, "With Input Parameters" section*

### Security Model Configuration

```yaml
# Role restriction — only admin and maintainer can trigger
on:
  workflow_dispatch:
    roles: [admin, maintainer]

# Bot authorization — specific bots can trigger
on:
  workflow_dispatch:
    bots: ["dependabot[bot]", "github-actions[bot]"]

# Environment approval gate — requires reviewer sign-off before execution
on:
  workflow_dispatch:
    manual-approval: production
```

*Source: gh-aw DispatchOps patterns documentation, "Security Model" section*

### Research Assistant — Full Parameterized Workflow Example

```yaml
---
on:
  workflow_dispatch:
    inputs:
      topic:
        description: 'Research topic'
        required: true
        type: string
      depth:
        description: 'Analysis depth'
        type: choice
        options:
          - brief
          - detailed
        default: brief
permissions:
  contents: read
safe-outputs:
  create-discussion:
---
# Research Assistant
Research the following topic: "${{ github.event.inputs.topic }}"
Analysis depth requested: ${{ github.event.inputs.depth }}
Provide a ${{ github.event.inputs.depth }} analysis with key findings and recommendations.
```

*Source: gh-aw DispatchOps patterns documentation, "Declaring and Referencing Inputs"
section — Research Assistant example*

### Handlebars Conditionals for Behavior Branching

```handlebars
{{#if (eq github.event.inputs.include_code "true")}}
Include actual code snippets in your analysis.
{{else}}
Describe code patterns without including actual code.
{{/if}}

{{#if (eq github.event.inputs.priority "high")}}
URGENT: Prioritize speed over completeness.
{{/if}}
```

*Source: gh-aw DispatchOps patterns documentation, "Conditional Logic Based on Inputs"
section*

### CLI Invocation Patterns

```bash
# Basic invocation
gh aw run workflow

# With input parameters
gh aw run research --raw-field topic="quantum computing"
gh aw run scout \
  --raw-field topic="AI safety research" \
  --raw-field priority=high

# Synchronous (blocks until completion)
gh aw run research --raw-field topic="AI agents" --wait

# Target a specific branch (live repository, feature branch workflow)
gh aw run research --ref feature-branch

# Cross-repository invocation
gh aw run workflow --repo owner/repository

# Verbose output
gh aw run research --raw-field topic="AI" --verbose
```

*Source: gh-aw DispatchOps patterns documentation, "Running Workflows with CLI" section*

### Two-Stage Development Testing Pattern

```bash
# Stage 1: Isolated trial (no production side effects)
gh aw trial ./research.md --raw-field topic="test query"

# Stage 2: Live branch testing (runs against repository, from feature branch)
gh aw run research --ref feature/improve-workflow
```

*Source: gh-aw DispatchOps patterns documentation, "Development Pattern: Branch Testing"
section*

### Troubleshooting Reference

```
Issue                       | Solution
----------------------------|--------------------------------------------------
Workflow not listed in UI   | Verify workflow_dispatch: exists; compile; push
                            | both .md and .lock.yml files
"Workflow not found" error  | Use filename without .md extension; verify file
                            | in .github/workflows/
"Cannot be run" error       | Add workflow_dispatch: to on: section; recompile;
                            | verify .lock.yml
Permission denied           | Verify write access; check roles: field
Inputs not appearing        | Check YAML indentation (2 spaces); validate input
                            | types; recompile and push
Wrong branch context        | Specify branch with --ref branch-name in CLI
```

*Source: gh-aw DispatchOps patterns documentation, "Troubleshooting" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-github-actions-primer.md` Claim 8 (`workflow_dispatch` as the development-
    time testing escape hatch for feature branches): DispatchOps Claim 10 is the
    same pattern — `gh aw run --ref feature-branch` for pre-merge live testing. The
    primer treats it as a development ergonomic; DispatchOps elevates it to a formal
    two-stage testing pattern (trial → live branch). Both sources agree that
    `workflow_dispatch` is the mechanism for testing on feature branches before
    merging to the default branch.
  - `docs-ghaw-chatops.md` Claim 3 (default `roles:` restricts slash commands to
    admin/maintainer/write users): DispatchOps Claim 2 documents the identical
    access-control model for `workflow_dispatch` — write access or higher by default,
    `roles:` field for stricter restriction. Both human-trigger patterns share the
    same roles-based authorization model. The two sources together confirm this as
    the platform-wide convention for human-initiated agentic workflows.
  - `docs-ghaw-how-they-work.md` Claim 10 (critical actions can require human approval):
    DispatchOps Claim 5 (`manual-approval: <environment>`) is the concrete mechanism
    for pre-execution human approval. The how-they-work note documents this as a
    principle; DispatchOps documents the implementation — the `manual-approval:` field
    backed by GitHub's environment protection rules.
  - `docs-ghaw-dailyops.md` Claim 2 (weekday-only cron paired with `workflow_dispatch`
    for manual testing): DispatchOps Claim 11 ("Scheduled workflow testing: Combine
    `schedule` with `workflow_dispatch` for immediate testing") is the same convention.
    Both sources confirm that pairing `schedule` with `workflow_dispatch` is a
    cross-pattern best practice for scheduled workflows — not DailyOps-specific.
  - `docs-ghaw-ephemerals.md` (mentions `workflow_dispatch` for manual cache clearing
    as an operational pattern): DispatchOps Claim 11 frames "Manual operations:
    Choice inputs with predefined operations (cleanup, sync, audit)" as a primary
    DispatchOps use case. The ephemerals pattern of using `workflow_dispatch` for
    maintenance operations is consistent with and subsumed by the DispatchOps
    operational use case.
  - `docs-ghaw-agentic-authoring.md` Claim 3 (`gh aw trial` for isolated pre-merge
    testing): DispatchOps Claim 10 extends this with the two-stage testing pattern —
    trial (isolated) followed by `gh aw run --ref` (live). The authoring note
    documents `trial` as a development tool; DispatchOps completes the workflow with
    the live-branch testing step that follows.

- **Extends**:
  - `docs-ghaw-how-they-work.md` — that note covers the two-component YAML+markdown
    structure, the five-layer security architecture, and the general trigger model.
    DispatchOps extends it with `workflow_dispatch`-specific security semantics (fork
    protection, `roles:`, `bots:`, `manual-approval:`) that are not covered in the
    general security architecture documentation.
  - `docs-ghaw-github-actions-primer.md` Claim 8 (`workflow_dispatch` as development
    testing): the primer treats `workflow_dispatch` incidentally — as a development-time
    escape hatch. DispatchOps is the dedicated canonical source that treats it as a
    first-class production trigger with a full security model, typed inputs, and
    named use cases.
  - `docs-ghaw-chatops.md` — ChatOps documents the slash-command human trigger pattern
    in comment contexts; DispatchOps documents the UI/CLI dispatch human trigger pattern.
    Together they define the two human-initiated trigger types in the gh-aw platform:
    comment-based (ChatOps) and dispatch-based (DispatchOps). DispatchOps adds the
    `bots:` field (not in ChatOps), environment-backed approval gates, and typed
    input parameters.

- **Contradicts**: None identified. The security model (write access default, `roles:`
  field) is consistent with the ChatOps pattern. The `workflow_dispatch` behavior
  (fork protection, branch execution) is consistent with the GitHub Actions Primer.
  The two-stage testing workflow (trial → live branch) is consistent with the
  Agentic Authoring guide. No existing source note makes claims that DispatchOps
  contradicts.

- **Novel**:
  - **`bots:` field for bot account authorization** (Claim 3): No prior source note
    documents a mechanism for explicitly authorizing specific bot accounts to trigger
    a workflow. This is entirely new to the corpus and has significant implications
    for multi-agent pipeline composition.
  - **Fork protection as a design reason to prefer `workflow_dispatch`** (Claim 4):
    While GitHub's fork protection behavior is a platform property, no prior source
    note names it as a deliberate security reason to choose DispatchOps over
    event-driven triggers for sensitive workflows. The explicit framing ("providing
    inherent attack protection") is new to the corpus.
  - **`manual-approval: <environment>` as a pre-execution approval gate** (Claim 5):
    Prior notes document human approval of agent *outputs* (PR review model in
    `docs-ghaw-how-they-work.md` Claim 10). The `manual-approval:` field is the first
    documented mechanism for pre-execution human approval — the agent does not start
    until a reviewer approves. This is a stronger HITL constraint than post-execution
    review.
  - **`environment` input type auto-populated from Settings → Environments** (Claim 6):
    The `environment` type and its automatic integration with GitHub's environment
    protection rules is not documented in any existing source note. This connects
    workflow inputs directly to repository environment management.
  - **Handlebars conditionals for behavior branching on input values** (Claim 8):
    The `{{#if (eq github.event.inputs.X "value")}}` pattern for input-driven
    instruction branching is not documented in any existing source note. Prior notes
    cover Handlebars interpolation; this source documents the conditional logic layer.
  - **`gh aw run --wait` synchronous blocking invocation** (Claim 9): The `--wait`
    flag and its use for scripted synchronous dispatch are new to the corpus. Prior
    notes document `gh aw run` but not its blocking invocation mode.
  - **Two-stage testing pattern: `gh aw trial` → `gh aw run --ref`** (Claim 10):
    While both commands are individually documented elsewhere, the explicit two-stage
    development workflow (trial for isolation, `--ref` for live integration) is not
    structured as a named pattern in any existing source note.

## Guide Impact

### Chapter 02: Harness Engineering

- **Complete the trigger taxonomy with `workflow_dispatch` as the third trigger type**
  (Claim 1): The guide's trigger taxonomy currently covers schedule-based
  (`docs-ghaw-dailyops.md`) and event-based triggers (`docs-ghaw-how-they-work.md`).
  Add `workflow_dispatch` / DispatchOps as the human-dispatch trigger type — fires when
  a human explicitly runs the workflow via UI or CLI. The decision heuristic: use
  DispatchOps when the task is episodic, needs input parameters the harness cannot infer
  from repository context, and the human decides both *when* and *with what parameters*
  the agent acts.
- **Document the four typed input parameter types** (Claim 6): The `string`, `boolean`,
  `choice`, and `environment` types are the parameterization vocabulary for DispatchOps
  harnesses. Add concrete guidance: `choice` for operational modes, `environment` for
  deployment target selection (with automatic environment protection integration),
  `string` for free-form queries, `boolean` for feature/verbosity toggles.
- **Document the `${{ github.event.inputs.INPUT_NAME }}` interpolation pattern** (Claim 7):
  This is the standard mechanism for injecting DispatchOps input values into the
  agent's instruction body. Contrast with ChatOps's `steps.sanitized.outputs.text`
  (which sanitizes; dispatch inputs come from authorized users so the sanitization
  need is lower).
- **Add Handlebars conditional branching as a multi-mode workflow pattern** (Claim 8):
  The `{{#if (eq ...)}}` pattern enables a single workflow file to cover multiple
  behavioral variants controlled by a `choice` input. Document as the mechanism for
  avoiding workflow file duplication for variants that differ only in instruction
  emphasis.
- **Document the full CLI invocation vocabulary** (Claim 9): The `gh aw run` flags
  (`--raw-field`, `--wait`, `--ref`, `--repo`, `--verbose`) are the standard operational
  interface for DispatchOps. Add these to the harness operations reference.
- **Add the two-stage development testing pattern** (Claim 10): For DispatchOps
  harnesses, recommend: `gh aw trial` (local, isolated, no side effects) → `gh aw run
  --ref feature-branch` (live, integration test) → merge. This is the development loop
  for DispatchOps workflows.

### Chapter 03: Safety and Verification

- **Add `workflow_dispatch` fork protection as a deliberate security design choice**
  (Claim 4): For workflows that handle sensitive resources or consequential operations,
  `workflow_dispatch` provides inherent fork protection that event-driven triggers do not.
  Name this as a design reason to prefer DispatchOps for sensitive operational workflows
  in public repositories — it eliminates an entire class of fork-based attack vectors
  without additional configuration.
- **Add `roles:` field as the first-line authorization check for DispatchOps** (Claim 2):
  Mirror the Ch03 guidance for ChatOps (`docs-ghaw-chatops.md` Claim 3 and 4). The
  write-access default is appropriate for most workflows; restrict to `[admin, maintainer]`
  for destructive or high-consequence operations.
- **Add `manual-approval: <environment>` as the pre-execution approval gate** (Claim 5):
  For production-targeting workflows or workflows with irreversible side effects, pair
  DispatchOps with `manual-approval: production` and configured environment reviewers.
  This is the only mechanism in the gh-aw corpus for requiring explicit human approval
  *before* the agent executes — stronger than the PR review model.
- **Document `bots:` field for bot authorization with multi-agent security implications**
  (Claim 3): When authorizing bots to trigger dispatch workflows, the `bots:` list must
  be explicitly maintained — it should not use wildcard patterns. Document as a security
  consideration for multi-agent pipeline design.

### Chapter 05 / Human-in-the-Loop

- **Frame DispatchOps and ChatOps as the two human-initiated trigger types, with distinct
  invocation contexts** (Claim 1): ChatOps (`slash_command`) fires when a human types
  a command in a GitHub comment — the interaction context is a conversation thread.
  DispatchOps (`workflow_dispatch`) fires when a human runs a workflow via UI or CLI —
  the interaction context is the Actions panel or terminal. Together they cover all
  human-initiated trigger scenarios. Choose ChatOps when the request is naturally made
  in a comment context (e.g., a PR review requesting agent analysis); choose DispatchOps
  when the request is a standalone task invocation (e.g., initiating a research workflow,
  running a deployment).
- **Add `manual-approval:` as the pre-execution HITL gate** (Claim 5): The HITL
  chapter should distinguish between human approval of agent *outputs* (post-execution
  PR review) and human approval before agent *execution* (`manual-approval:` gate).
  Both are HITL mechanisms; they apply at different points in the agent lifecycle.

### Chapter 09: Agent Orchestration

- **Document `bots:` field as the mechanism for chaining dispatch-triggered workflows
  from upstream automation** (Claim 3): The `bots:` field enables multi-agent pipelines
  where an upstream workflow (e.g., Dependabot) triggers a downstream DispatchOps
  workflow. This is the composition primitive for event-driven → dispatch-triggered
  agent chains.
- **Add DispatchOps to the trigger taxonomy alongside DailyOps, ChatOps, IssueOps,
  LabelOps** (Claim 11): The four-pattern taxonomy (`docs-ghaw-dailyops.md` Claim 8)
  should now include DispatchOps explicitly — it fills the "human-dispatch" slot that
  the DailyOps note does not fully document. The complete taxonomy: DailyOps (scheduled),
  IssueOps (issue event), ChatOps (slash command in comment), LabelOps (label change),
  DispatchOps (human UI/CLI dispatch).

## Extraction Notes

1. **Source rendered full content via Astro/Starlight static HTML**: The page content
   was fully extractable via WebFetch. All YAML examples, CLI commands, and security
   model details were captured from the rendered output. No content appears to have been
   truncated.

2. **`environment` input type integration with GitHub Environments**: The `environment`
   type auto-populates from Settings → Environments without requiring a hardcoded
   `options:` list. The full interaction between the `environment` input type and
   environment protection rules (required reviewers, wait timers) is partially documented
   — the page notes that `manual-approval: <environment>` uses environment protection rules
   but does not detail the full environment configuration workflow. Practitioners should
   consult the GitHub Environments documentation for the complete approval rule setup.

3. **No named production workflow examples**: Unlike ChatOps (which documents the Grumpy
   Code Reviewer as a named production example), the DispatchOps page does not name
   specific production DispatchOps workflows from the agent factory. The Research
   Assistant example appears to be illustrative rather than a live production workflow.
   Deeper extraction of specific DispatchOps workflow files (e.g., the "Manual Workflows
   Example" linked in the Related Documentation section) would yield concrete harness
   templates but those URLs were not accessible from this page.

4. **Handlebars is the templating system for gh-aw**: The Handlebars conditionals
   (`{{#if (eq ...)}}`, `{{else}}`, `{{/if}}`) are part of the gh-aw Handlebars
   templating system. The full Handlebars helper vocabulary (beyond `eq`) is not
   documented on this page; the "Templating" link in Related Documentation may contain
   additional helper documentation not extracted here.

5. **No publication date**: The documentation page does not carry an explicit publication
   date. `date_published` is left null. Content is consistent with gh-aw platform state
   as of 2026-05-01.

6. **No contradictions filed**: Reviewed all existing source notes. No claims in this
   source materially oppose any existing source note at the MINER.md §4a threshold.
   The DispatchOps security model is fully consistent with the ChatOps pattern and the
   five-layer security architecture in `docs-ghaw-how-they-work.md`.

7. **Prospector note on full patterns library**: The first Prospector triage comment
   noted that the GH-AW site has a full patterns library (15+ patterns: BatchOps,
   DataOps, IssueOps, LabelOps, MultiRepoOps, ProjectOps, ResearchPlanAssignOps,
   SideRepoOps, SpecOps, TaskOps, TrialOps, WorkQueueOps, and others not yet captured).
   A systematic sweep of the full patterns section would yield substantial new content
   for the corpus. This is flagged here for the Prospector/scheduling team rather than
   actioned in this note.
