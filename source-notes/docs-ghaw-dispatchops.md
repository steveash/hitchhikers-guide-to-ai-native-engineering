---
source_url: https://github.github.com/gh-aw/patterns/dispatch-ops
source_type: docs
title: "GitHub Agentic Workflows: DispatchOps Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-02
last_checked: 2026-05-02
status: current
confidence_overall: emerging
issue: "#325"
---

# GitHub Agentic Workflows: DispatchOps Pattern

> The authoritative reference for `workflow_dispatch` as a human-in-the-loop
> trigger pattern in gh-aw — documents parameterized agent invocation (four
> input types, Handlebars conditionals), the security model specific to manual
> dispatch (role-based access, bot authorization, fork protection, environment
> approval gates), and synchronous/branch-scoped CLI execution flags; the first
> source note in the corpus to document `manual-approval:` as a concrete
> human-approval primitive.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, "Design
  Patterns > DispatchOps" section — prescriptive pattern reference for
  on-demand manual workflow execution, not API reference or changelog)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind Peli de Halleux's "Agent Factory" blog series and the
  `gh aw` platform. Claims about `workflow_dispatch` schema, role enforcement,
  fork protection semantics, and `manual-approval:` behavior are authoritative
  for this platform.
- **Scope**: The DispatchOps pattern specifically — `workflow_dispatch` trigger
  syntax, four input parameter types, input interpolation and Handlebars
  conditionals, `roles:` and `bots:` access control, fork protection, environment
  approval gates (`manual-approval:`), CLI execution flags (`--wait`, `--ref`,
  `--repo`, `--raw-field`, `--verbose`), and use-case framing. Does NOT cover:
  the five-layer security architecture (in `docs-ghaw-how-they-work.md`),
  ChatOps slash-command patterns (`docs-ghaw-chatops.md`), IssueOps or DailyOps
  patterns, the compilation model or `gh aw compile`.

## Extracted Claims

### Claim 1: DispatchOps enables on-demand manual workflow execution from the GitHub UI or CLI — the human decides when the agent runs, rather than automation deciding on a schedule or event

- **Evidence**: "DispatchOps enables manual workflow execution through the
  GitHub Actions UI or CLI for on-demand tasks. The `workflow_dispatch` trigger
  allows running workflows with custom inputs whenever needed, rather than waiting
  for scheduled events." Use cases listed: on-demand research, manual operations,
  testing/debugging, and combining with scheduled triggers for immediate testing.
- **Confidence**: settled (first-party documentation; `workflow_dispatch` is a
  live feature on the gh-aw platform)
- **Quote**: "DispatchOps enables manual workflow execution through the GitHub
  Actions UI or CLI for on-demand tasks. The `workflow_dispatch` trigger allows
  running workflows with custom inputs whenever needed, rather than waiting for
  scheduled events."
- **Our assessment**: DispatchOps fills the human-initiated trigger slot in the
  gh-aw pattern taxonomy. Where DailyOps fires on a schedule and IssueOps/ChatOps
  fire on repository events, DispatchOps fires when a human explicitly decides
  the moment is right. This is the correct pattern when the agent needs human
  context to know when to run — for example, "analyze this incident now" vs.
  "analyze incidents every Tuesday." For Ch02 (Harness Engineering): `workflow_dispatch`
  should be positioned as the third trigger category alongside schedule and
  event-based triggers. For Ch05/Ch06 (Human-in-the-Loop / Orchestration): the
  human timing judgment model is a first-class design choice, not a fallback.

### Claim 2: DispatchOps supports four parameterized input types — `string`, `boolean`, `choice`, and `environment` — defined in a YAML `inputs:` block with per-field `description:`, `required:`, and `default:` metadata

- **Evidence**: The page documents the full `inputs:` schema with examples:
  `topic` (string, required), `priority` (choice with options `low`/`medium`/`high`,
  default `medium`), `deploy_target` (environment type, default `staging`). The
  page states explicitly: "**Supported types:** `string`, `boolean`, `choice`,
  and `environment`."
- **Confidence**: settled (first-party; the four types and their YAML schema are
  explicitly documented with working examples)
- **Quote**: "Supported types: `string`, `boolean`, `choice`, and `environment`."
- **Our assessment**: The `environment` input type is the most architecturally
  significant: it links workflow input to a named GitHub environment (and its
  associated secrets, protection rules, and approval gates), not just a string
  value. A workflow with `type: environment` can be parameterized to run against
  `staging` vs. `production` at invocation time, with the protection rules for
  each environment automatically applied. For Ch02: document all four input types
  as the complete DispatchOps parameterization vocabulary, with special attention
  to `environment` as the gate for production-impacting operations.

### Claim 3: Input values are accessed in the workflow instruction body via `${{ github.event.inputs.INPUT_NAME }}` expression syntax — the same GitHub Actions expression model

- **Evidence**: "Access inputs using expression syntax: `Research the following
  topic: "${{ github.event.inputs.topic }}"`. `Analysis depth: ${{ github.event.inputs.depth }}`"
- **Confidence**: settled (first-party; the expression syntax is documented with
  a concrete example in the instruction body)
- **Quote**: "Access inputs using expression syntax"
- **Our assessment**: The `${{ github.event.inputs.* }}` pattern is identical to
  standard GitHub Actions input access — gh-aw does not introduce a different
  interpolation syntax for dispatched inputs. Harness authors familiar with Actions
  can use the pattern directly. For Ch02: the interpolation example
  (`"Research the following topic: ${{ github.event.inputs.topic }}"`) is the
  canonical pattern for injecting human-provided values into the agent's natural
  language instruction body.

### Claim 4: Handlebars conditional syntax enables input-driven behavior branching within the workflow instruction body — without requiring YAML condition logic outside the instruction text

- **Evidence**: The page documents the Handlebars conditional pattern:
  ```
  {{#if (eq github.event.inputs.include_code "true")}}
  Include actual code snippets in analysis.
  {{else}}
  Describe patterns without code.
  {{/if}}
  ```
  This is conditional logic embedded in the natural language instruction section,
  not in the YAML frontmatter.
- **Confidence**: settled (first-party; the Handlebars syntax with `eq` helper and
  if/else structure is shown with a concrete example)
- **Quote**: (code block above, extracted verbatim from the page)
- **Our assessment**: Handlebars conditionals in the instruction body allow a
  single workflow to express branching behavior parameterized by dispatch inputs,
  without splitting into multiple separate workflow files. The `eq` helper performs
  string equality comparison; additional Handlebars helpers may exist (not
  enumerated on this page). For Ch02: this is the pattern for "configurable agent
  behavior at invocation time" — a human triggering the workflow chooses the
  execution mode via an input; the Handlebars block translates that choice into
  different instruction text for the agent.

### Claim 5: The `roles:` field on `workflow_dispatch` restricts which GitHub repository roles can manually trigger the workflow — providing caller-identity access control for DispatchOps

- **Evidence**: YAML example on the page:
  ```yaml
  on:
    workflow_dispatch:
      roles: [admin, maintainer]
  ```
  This restricts manual triggering to users with admin or maintainer roles.
- **Confidence**: settled (first-party; the `roles:` field is explicitly shown in
  YAML context with named role values)
- **Quote**: (YAML block above, extracted verbatim)
- **Our assessment**: The `roles:` field on `workflow_dispatch` is the DispatchOps
  counterpart to the `roles:` field on `slash_command` documented in
  `docs-ghaw-chatops.md` Claim 3. Both patterns share the same access control
  mechanism: restrict who can invoke the agent by specifying required repository
  roles. For `workflow_dispatch`, this means only users with the listed roles can
  trigger the workflow from the GitHub UI or CLI — anonymous or low-privilege
  users cannot invoke DispatchOps workflows. For Ch03 (Safety and Verification):
  the `roles:` field is the access control primitive for DispatchOps, and its
  default behavior (if not specified) should be confirmed before recommending
  open-trigger designs for sensitive operations.

### Claim 6: The `bots:` field authorizes specific bot identities to trigger DispatchOps workflows programmatically — enabling automation tools to invoke manual-trigger workflows without human interaction

- **Evidence**: YAML example on the page:
  ```yaml
  on:
    workflow_dispatch:
      bots: ["dependabot[bot]", "github-actions[bot]"]
  ```
  The `bots:` field accepts a list of bot identity strings in the `name[bot]`
  format used by GitHub.
- **Confidence**: settled (first-party; the `bots:` field and example bot names
  are explicitly documented)
- **Quote**: (YAML block above, extracted verbatim)
- **Our assessment**: The `bots:` field is new to the corpus — no existing source
  note documents a mechanism for explicitly authorizing bot actors to trigger
  `workflow_dispatch` workflows. This enables hybrid automation where a bot
  (Dependabot, a CI workflow) can programmatically invoke an on-demand agentic
  workflow without a human in the loop at trigger time. The human-in-the-loop
  element shifts from "who triggers?" to "what parameters?" and "approval gates."
  For Ch02: this is a pattern for wiring agentic on-demand workflows into automated
  pipelines — for example, Dependabot opens a PR and the `bots:` field authorizes
  it to also trigger an analysis workflow.

### Claim 7: Fork protection is an inherent security property of `workflow_dispatch` — forks of a repository cannot trigger the parent repository's `workflow_dispatch` workflows

- **Evidence**: "Fork Protection: DispatchOps executes only in the repository where
  defined; forks cannot trigger parent repository workflows, providing inherent
  attack protection."
- **Confidence**: settled (first-party; the property is named and the security
  implication is stated explicitly)
- **Quote**: "forks cannot trigger parent repository workflows, providing inherent
  attack protection."
- **Our assessment**: Fork protection is meaningful for open-source repositories
  where external contributors can fork the project. Because `workflow_dispatch`
  can only be triggered in the defining repository, a malicious fork cannot invoke
  the parent repo's DispatchOps workflows to abuse resources or access secrets.
  This is architecturally distinct from push/PR triggers, which can fire from
  forks and require explicit `pull_request_target` workarounds to safely access
  secrets. DispatchOps provides this protection without any additional
  configuration. For Ch03: document fork protection as a built-in security
  property of `workflow_dispatch` — relevant to any DispatchOps workflow that
  accesses secrets or performs sensitive operations.

### Claim 8: The `manual-approval:` field gates workflow execution on human sign-off via a named GitHub environment — the concrete mechanism for human-in-the-loop approval before DispatchOps execution

- **Evidence**: YAML example:
  ```yaml
  on:
    workflow_dispatch:
      manual-approval: production
  ```
  "Approval rules are configured in repository Settings → Environments with
  required reviewers and wait timers."
- **Confidence**: settled (first-party; YAML field is explicitly documented with
  configuration location)
- **Quote**: "Approval rules are configured in repository Settings → Environments
  with required reviewers and wait timers."
- **Our assessment**: `manual-approval:` is the most complete implementation of
  the human-approval-gate primitive in the corpus. The field names a GitHub
  environment (`production` in the example); the environment's "required reviewers"
  and "wait timers" configured in Settings must be satisfied before the workflow
  runs. This means: a human triggers DispatchOps (Claim 1), the platform pauses
  execution, a designated reviewer approves in the GitHub environment UI, then
  the workflow proceeds. The two-layer human involvement (human decides to run +
  reviewer approves before execution) is a stronger HITL model than simple role
  restriction. For Ch05 (Human-in-the-Loop): `manual-approval:` + named environment
  is the canonical approval-gate pattern for gh-aw. For Ch03: document as the
  high-assurance variant for DispatchOps workflows that touch production systems.

### Claim 9: `gh aw run --wait` provides synchronous CLI execution — the command blocks until the workflow completes, enabling scripts and programmatic callers to block on the result

- **Evidence**: CLI example: `gh aw run research --raw-field topic="AI agents" --wait`.
  Additional flags: `--raw-field KEY=VALUE` for input parameters, `--repo owner/repository`
  for cross-repo invocation, `--verbose` for extended output.
- **Confidence**: settled (first-party; CLI flags are explicitly documented with
  examples)
- **Quote**: (CLI example above, extracted verbatim)
- **Our assessment**: Synchronous CLI execution (`--wait`) is a pattern for
  scripted or CI-driven workflows that need to wait for the agentic workflow to
  finish before proceeding. Without `--wait`, `gh aw run` returns immediately and
  the workflow runs asynchronously. For Ch02: document `--wait` as the flag for
  pipeline-integration of DispatchOps — when the caller needs the result before
  taking the next step. The `--raw-field KEY=VALUE` flag is the CLI equivalent
  of UI input fields.

### Claim 10: `gh aw run --ref BRANCH` executes a DispatchOps workflow from a specific branch, enabling pre-merge testing of workflow changes on feature branches before promotion to the default branch

- **Evidence**: CLI example: `gh aw run research --ref feature-branch`. The page
  also documents: "Specify branch with `--ref branch-name`" as a troubleshooting
  step for "wrong branch" errors.
- **Confidence**: settled (first-party; the `--ref` flag is explicitly documented
  in both the CLI commands section and troubleshooting)
- **Quote**: "Specify branch with `--ref branch-name`"
- **Our assessment**: The `--ref` flag makes DispatchOps the primary development
  testing path for workflow changes in progress. A practitioner authoring a new
  or modified workflow on a feature branch can invoke it via `gh aw run --ref
  feature-branch` without merging to the default branch first. This is the
  DispatchOps-specific implementation of the pre-merge testing escape hatch
  described at a conceptual level in `docs-ghaw-github-actions-primer.md` Claim 8.
  For Ch02: document `gh aw run --ref` as the recommended pattern for validating
  dispatch-triggered workflows during development — the complete development loop
  for DispatchOps is: author on feature branch → `gh aw compile` → `gh aw run
  --ref BRANCH` → verify → merge to default.

### Claim 11: DispatchOps workflows require both the `.md` source and the compiled `.lock.yml` to be pushed to the branch before they appear as available workflows in the GitHub Actions UI

- **Evidence**: Troubleshooting entry: "Workflow not listed: Verify
  `workflow_dispatch:` exists in `on:` section, compile, and push both `.md`
  and `.lock.yml`."
- **Confidence**: settled (first-party; this is a troubleshooting note that
  documents a required deployment step)
- **Quote**: "Verify `workflow_dispatch:` exists in `on:` section, compile, and
  push both `.md` and `.lock.yml`."
- **Our assessment**: The requirement to push both files is a practitioner gotcha
  specific to the gh-aw compilation model — the GitHub Actions UI reads from the
  `.lock.yml`, not the `.md` source. If only the `.md` is pushed, the workflow
  will not appear as available for dispatch. This is consistent with the
  `.md` → `.lock.yml` compilation model in `docs-ghaw-how-they-work.md` Claim 7,
  but the DispatchOps troubleshooting note makes explicit what the how-they-work
  documentation leaves implicit: the UI reads the compiled artifact, not the source.

## Concrete Artifacts

### DispatchOps Trigger — Basic Syntax

```yaml
on:
  workflow_dispatch:
```

*Source: DispatchOps pattern documentation, "Basic Syntax" section*

### Parameterized Input Block — Full YAML Example

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

*Source: DispatchOps pattern documentation, "Input Parameters" section*

### Input Interpolation — Expression Syntax

```yaml
# In the workflow instruction body:
Research the following topic: "${{ github.event.inputs.topic }}"
Analysis depth: ${{ github.event.inputs.depth }}
```

*Source: DispatchOps pattern documentation, "Input Referencing" section*

### Handlebars Conditional — Input-Driven Behavior Branching

```
{{#if (eq github.event.inputs.include_code "true")}}
Include actual code snippets in analysis.
{{else}}
Describe patterns without code.
{{/if}}
```

*Source: DispatchOps pattern documentation, "Input Referencing" → Conditional logic section*

### Security Model — Roles, Bots, and Approval Gates

```yaml
# Role-based access control: restrict to admin and maintainer only
on:
  workflow_dispatch:
    roles: [admin, maintainer]

# Bot authorization: allow specific bots to trigger programmatically
on:
  workflow_dispatch:
    bots: ["dependabot[bot]", "github-actions[bot]"]

# Environment approval gate: require human review before execution
on:
  workflow_dispatch:
    manual-approval: production
# (Approval rules configured in: Settings → Environments → required reviewers)
```

*Source: DispatchOps pattern documentation, "Security Model" section*

### CLI Execution Commands — Full Reference

```bash
# Basic execution
gh aw run workflow

# With input parameters
gh aw run research --raw-field topic="quantum computing"
gh aw run scout \
  --raw-field topic="AI safety" \
  --raw-field priority=high

# Synchronous execution (blocks until complete)
gh aw run research --raw-field topic="AI agents" --wait

# Branch-specific execution (pre-merge testing on feature branch)
gh aw run research --ref feature-branch

# Cross-repo execution
gh aw run workflow --repo owner/repository

# With verbose output
gh aw run research --raw-field topic="AI" --verbose
```

*Source: DispatchOps pattern documentation, "CLI Commands" section*

### Trigger Taxonomy — DispatchOps in Context

```
Trigger type       When it fires                         Pattern
─────────────────────────────────────────────────────────────────
schedule           On a cron schedule (automated)        DailyOps
event-driven       On repository events (push, PR, etc.) IssueOps, LabelOps
slash_command      When a human types a command          ChatOps
workflow_dispatch  When a human manually triggers it     DispatchOps
```

*Source: DispatchOps related patterns + existing corpus synthesis*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-chatops.md` Claim 3 (by default, the `slash_command` trigger
    restricts execution to users with admin, maintainer, or write permissions):
    both ChatOps and DispatchOps share the `roles:` field as the runtime access
    control mechanism for human-triggered workflows. Claim 3 in the ChatOps note
    documents the default role set for `slash_command`; DispatchOps Claim 5 here
    documents the equivalent for `workflow_dispatch`. The two patterns use the
    same access control primitive applied to different trigger types.
  - `docs-ghaw-how-they-work.md` Claim 10 (critical actions can require human
    approval as a configurable escalation point): the DispatchOps `manual-approval:`
    field (Claim 8 here) is the concrete implementation of this design principle.
    Where Claim 10 in that note states the capability abstractly ("critical actions
    can require human approval"), DispatchOps provides the specific YAML field
    (`manual-approval: production`) and the configuration location (Settings →
    Environments with required reviewers and wait timers).
  - `docs-ghaw-dailyops.md` Claim 2 (weekday cron + `workflow_dispatch` for manual
    testing): DailyOps documents `workflow_dispatch` paired with `schedule` as the
    development-time testing companion. DispatchOps explains the underlying
    capability that makes this pairing work — `workflow_dispatch` allows execution
    "whenever needed, rather than waiting for scheduled events." The two notes
    together establish `workflow_dispatch` as both a standalone trigger type
    (DispatchOps) and a development-time supplement to scheduled workflows (DailyOps).
  - `docs-ghaw-github-actions-primer.md` Claim 8 (`workflow_dispatch` enables manual
    execution from any branch for development and testing): the primer documents the
    conceptual capability; DispatchOps provides the specific CLI implementation via
    `gh aw run --ref BRANCH` (Claim 10 here). The primer identifies the escape
    hatch; DispatchOps documents how to use it.

- **Contradicts**: None identified. DispatchOps is fully consistent with the security
  architecture in `docs-ghaw-how-they-work.md`, the access control model in
  `docs-ghaw-chatops.md`, and the `workflow_dispatch` testing pattern in
  `docs-ghaw-github-actions-primer.md`. No existing source note makes claims that
  conflict with the DispatchOps security model, input parameter syntax, or CLI flags.

- **Extends**:
  - `docs-ghaw-how-they-work.md` — that note introduces human approval conceptually
    (Claim 10). DispatchOps extends it with the specific YAML primitive (`manual-approval:`),
    the named environment configuration mechanism, and the two-layer HITL model
    (trigger decision + reviewer approval before execution).
  - `docs-ghaw-github-actions-primer.md` Claim 8 (the `workflow_dispatch` branch
    testing escape hatch): the primer identifies the capability; DispatchOps documents
    the named CLI flag (`--ref`), the trigger input parameter schema, and the
    full development workflow for dispatch-triggered agents.

- **Novel**:
  - **`bots:` field for bot authorization** (Claim 6): No existing source note
    documents an explicit bot-authorization field on any gh-aw trigger type. The
    `bots:` field enables programmatic invocation of `workflow_dispatch` workflows
    by named bot actors without human interaction at trigger time.
  - **Fork protection as a named security property of `workflow_dispatch`** (Claim 7):
    Prior notes document the default-branch trust boundary and the five-layer security
    model, but none name fork protection as a specific security property of
    `workflow_dispatch` triggers. The property (forks cannot trigger parent repo
    workflows) is distinct from the trust-boundary framing in
    `docs-ghaw-github-actions-primer.md` Claim 7.
  - **`manual-approval:` field with environment-based reviewer configuration** (Claim 8):
    The specific YAML field name, its mapping to a named GitHub environment, and the
    two-layer approval model (trigger + environment reviewer) are documented only here.
    Prior notes establish the principle; this is the implementation.
  - **Pre-merge feature branch testing via `gh aw run --ref`** (Claim 10): The specific
    CLI pattern of running `gh aw run --ref feature-branch` as a named development
    workflow for DispatchOps is not structured as a named pattern in any existing
    source note. The primer identifies `workflow_dispatch` as an escape hatch; no
    prior note documents the `--ref` flag or the branch-targeted development loop.
  - **Handlebars conditional syntax for input-driven behavior branching** (Claim 4):
    The `{{#if (eq ...)}}` Handlebars pattern in workflow instruction bodies is not
    documented in any existing source note. This is a new instruction-body pattern
    for parameterized behavior branching.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add `workflow_dispatch` to the trigger taxonomy as the human-initiated type**
  (Claim 1): The guide's trigger taxonomy should explicitly include manual dispatch
  alongside schedule and event-driven triggers. Use the four-row taxonomy table
  (Concrete Artifacts → Trigger Taxonomy) as a reference. The design decision:
  use `workflow_dispatch` when the agent needs human judgment to know when to run,
  not just what to run.
- **Document all four input types and their use-case roles** (Claim 2): Teach
  `string` for free-form inputs, `choice` for predefined menus, `boolean` for
  flags, and `environment` for production-gate operations. The `environment` type
  is the highest-value teaching point — it wires input choice to secrets and
  protection rules automatically.
- **Name Handlebars conditionals as the input-driven branching pattern** (Claim 4):
  The `{{#if (eq github.event.inputs.KEY "VALUE")}}` idiom belongs in Ch02 as the
  canonical pattern for parameterized agent behavior. It keeps the conditional
  logic in the instruction body where the agent interprets it, rather than in YAML
  where it would require a separate workflow branch.
- **Document the DispatchOps development loop** (Claims 10, 11): Author on feature
  branch → `gh aw compile` → `gh aw run --ref BRANCH` → verify → merge to default.
  Push both `.md` and `.lock.yml` for the workflow to appear in the Actions UI.
  This is the complete development loop for dispatch-triggered workflows.

### Chapter 03: Safety and Verification

- **Document the DispatchOps three-level security model** (Claims 5, 6, 7, 8):
  (1) `roles:` restricts who can trigger manually; (2) `bots:` explicitly authorizes
  bot actors; (3) fork protection prevents trigger from forks by default; (4)
  `manual-approval:` gates execution on environment reviewer sign-off. Present
  these as a layered access control model specific to `workflow_dispatch`.
- **Add fork protection as a built-in security property** (Claim 7): For any
  DispatchOps workflow accessing secrets or performing sensitive operations, document
  that fork protection is inherent — no additional configuration required.

### Chapter 05 / Human-in-the-Loop

- **`manual-approval:` + named environment as the canonical approval-gate primitive**
  (Claim 8): This is the most complete HITL approval pattern in the corpus. The
  two-layer model — human decides to trigger (Claim 1) + reviewer approves before
  execution (Claim 8) — is the reference design for high-assurance on-demand agent
  tasks. Pair with `docs-ghaw-how-they-work.md` Claim 10 for the conceptual
  framing.

### Chapter 06 / Orchestration

- **Trigger selection heuristic** (Claim 1 + trigger taxonomy): Add a decision
  guide for when to use DispatchOps vs. DailyOps vs. ChatOps vs. IssueOps. Core
  distinction: DispatchOps = human controls timing AND inputs; ChatOps = human
  controls timing but inputs come from comment context; DailyOps = system controls
  timing, human reviews output; IssueOps = event controls timing. The taxonomy
  table (Concrete Artifacts) provides the reference frame.

## Extraction Notes

1. **Source is a pattern reference page, not a full CLI reference**: The DispatchOps
   page documents the pattern and common CLI usage, but does not enumerate every
   possible `gh aw run` flag. The `--repo`, `--verbose`, and `--wait` flags shown
   are documented from the examples on the page; additional flags may exist in the
   full CLI reference (`/gh-aw/setup/cli/`).

2. **Handlebars helper vocabulary is incomplete**: The page demonstrates the `eq`
   helper for string equality. Additional Handlebars helpers (e.g., for numeric
   comparison, string operations) may be supported but are not documented on this
   page. The vocabulary shown (`{{#if (eq ...)}}...{{else}}...{{/if}}`) is treated
   as settled; the broader helper set is not enumerated.

3. **`bots:` field default behavior not documented**: The page shows how to authorize
   bots via `bots:` but does not state whether `workflow_dispatch` is blocked to bots
   by default (requiring explicit `bots:` authorization) or open to bots by default
   (with `bots:` as an allowlist addition). The security implications of the default
   differ materially; this should be confirmed against the full trigger reference.

4. **Related patterns not extracted**: The page links to DataOps, ExpertOps, TrialOps,
   Triggers Reference, and CLI Commands. These are not extracted here. TrialOps in
   particular may be relevant to the pre-merge testing pattern (Claim 10) — a
   separate source note for TrialOps would add context on how `gh aw trial` relates
   to the `--ref` branch testing pattern.

5. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with the
   current gh-aw platform as of 2026-05-02.

6. **No contradictions filed**: Reviewed all existing source notes, including all
   gh-aw-related notes. No claims in this source materially oppose any existing
   source note. The `roles:` field usage in DispatchOps extends rather than
   contradicts the ChatOps documentation of the same field.
