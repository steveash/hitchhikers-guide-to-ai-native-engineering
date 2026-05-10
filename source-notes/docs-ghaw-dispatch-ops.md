---
source_url: https://github.github.com/gh-aw/patterns/dispatch-ops
source_type: docs
title: "GitHub Agentic Workflows: DispatchOps Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-03
last_checked: 2026-05-03
status: current
confidence_overall: emerging
issue: "#325"
---

# GitHub Agentic Workflows: DispatchOps Pattern

> The canonical reference for manual-trigger agentic workflows — documents
> `workflow_dispatch` as the human-in-the-loop trigger primitive (distinct from
> event-driven and scheduled patterns), typed input parameters with four types
> including `environment`, Handlebars conditionals for input-driven agent behavior
> branching, the full security model (`roles:`, `bots:`, fork protection,
> `manual-approval:` environment gates), `gh aw run --wait` for synchronous
> on-demand invocation, and the branch testing pattern using `gh aw trial` before
> merge.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, "Patterns"
  section, "DispatchOps" page — same `patterns/` section as `patterns/orchestration`
  and `patterns/monitoring`. Patterns pages are practitioner implementation
  references, distinct from the conceptual `introduction/` pages and the
  practitioner `guides/` section.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research (same
  team behind Peli de Halleux's agent factory series and all other gh-aw
  documentation in the corpus). YAML configurations, CLI behavior, and security
  model descriptions are authoritative for the `gh aw` platform. Claims about
  when to prefer dispatch over other trigger types are design opinions from
  practitioners running 183+ production workflows; they do not automatically
  generalize to non-gh-aw platforms.
- **Scope**: Covers the DispatchOps pattern in full — the `workflow_dispatch`
  trigger as a human-timing-judgment primitive, typed input parameters (all four
  types), input referencing syntax, Handlebars conditionals for behavior
  branching, the security model (access control, fork protection, approval gates),
  CLI invocation patterns including `--wait`, and the branch testing development
  workflow. Does NOT cover: the Safe Outputs permission model in general (see
  `docs-ghaw-how-they-work.md`), scheduled triggers (see `docs-ghaw-dailyops.md`),
  event-driven triggers (see other patterns pages), or the full five-layer security
  architecture (see `docs-ghaw-how-they-work.md`).

## Extracted Claims

### Claim 1: DispatchOps positions `workflow_dispatch` as the trigger for tasks requiring human judgment about timing — distinct from event-driven and scheduled alternatives

- **Evidence**: The page opens with this framing and provides an explicit use-case
  enumeration: "Use DispatchOps for research tasks, operational commands, testing
  workflows during development, debugging production issues, or any task that
  doesn't fit a schedule or event trigger." The framing distinguishes three trigger
  classes: event-driven (fires on a GitHub event — PR, issue, push), scheduled
  (fires on a cron), and manual dispatch (fires when a human decides to run it).
- **Confidence**: emerging (first-party design opinion; the three-class taxonomy is
  not formally codified, but the page's use-case enumeration implies it)
- **Quote**: "Use DispatchOps for research tasks, operational commands, testing
  workflows during development, debugging production issues, or any task that
  doesn't fit a schedule or event trigger."
- **Our assessment**: The "doesn't fit a schedule or event trigger" criterion is
  the clearest decision heuristic in the corpus for when to use manual dispatch.
  If a task has a natural event trigger (PR opened, issue labeled) → event-driven.
  If it should run on a regular cadence → schedule. If humans should decide when
  it runs based on context (research scope, operational need, timing judgment) →
  dispatch. For Ch05 (Human-in-the-Loop) and Ch06 (Orchestration): this taxonomy
  is worth naming explicitly. The four named use cases (research, operational
  commands, development testing, production debugging) are a useful taxonomy for
  teams choosing between trigger types.

### Claim 2: `workflow_dispatch` supports four typed input parameters — `string`, `boolean`, `choice`, and `environment` — enabling configurable, parameterized agent invocation

- **Evidence**: The page documents all four types with YAML examples. The
  `environment` type is given special treatment: it "auto-populates from
  repository Settings → Environments. No `options` list needed; specify a
  `default` matching an existing environment name." The `choice` type requires
  an explicit `options` list.
- **Confidence**: settled (first-party documentation; type names and YAML syntax
  are explicitly enumerated)
- **Quote**: "Supported input types: `string`, `boolean`, `choice`, and
  `environment`."
- **Our assessment**: The `environment` type is the most novel of the four —
  it integrates the input system with GitHub's environment management layer,
  so practitioners can parameterize agent invocation against existing deployment
  environments without maintaining a parallel `options` list. The `choice` type
  is the primary pattern for constrained agent behavior (pick from a predefined
  operation set). For Ch02 (Harness Engineering): document these four types as
  the input vocabulary for parameterized agent harnesses. The `environment` type
  is especially relevant for workflows that target different deployment stages
  (staging, production).

### Claim 3: Inputs are referenced in workflow markdown via `${{ github.event.inputs.INPUT_NAME }}` GitHub Actions expression syntax

- **Evidence**: The page documents the input reference syntax directly:
  "`${{ github.event.inputs.topic }}`" and "`${{ github.event.inputs.depth }}`"
  are given as examples of how to embed input values in the agent's instruction
  text.
- **Confidence**: settled (first-party documentation; syntax is specific and
  consistent with standard GitHub Actions expression syntax)
- **Quote**: "${{ github.event.inputs.topic }}"
- **Our assessment**: The input reference syntax is the same as standard GitHub
  Actions expression syntax — practitioners familiar with Actions will recognize
  it. For Ch02: the practical implication is that typed inputs can be interpolated
  directly into the workflow's natural language instruction section. This makes
  the agent's task description dynamic at invocation time (e.g., "Research the
  following topic: ${{ github.event.inputs.topic }}"), enabling one workflow
  spec to serve many different invocations.

### Claim 4: Handlebars conditionals enable input-driven agent behavior branching within workflow instructions — `{{#if (eq ...)}}` syntax conditions agent behavior on input values

- **Evidence**: The page documents Handlebars conditional syntax with two examples:
  branching on `include_code` (true/false) to include or omit code snippets, and
  branching on `priority` (value "high") to add urgency signaling. Both examples
  condition the agent's instruction text on the value of a `workflow_dispatch` input.
- **Confidence**: settled (first-party documentation; syntax is explicitly shown)
- **Quote**: (no single prose quote; see Concrete Artifacts for the verbatim code
  block)
- **Our assessment**: Handlebars conditionals are the gh-aw-specific mechanism for
  making agent instructions context-sensitive at invocation time without writing
  multiple workflow variants. A `choice` input (Claim 2) selects between discrete
  operation modes; Handlebars conditionals translate that selection into different
  instruction text for the agent. This is the input-driven behavior branching
  pattern: the human picks a mode via the dispatch UI, and the agent receives
  different instructions depending on that choice. For Ch02 (Harness Engineering):
  this pattern, combined with the four input types (Claim 2) and input reference
  syntax (Claim 3), gives a complete picture of configurable agent invocation via
  `workflow_dispatch`. The Handlebars layer is distinct from the YAML frontmatter
  — it lives in the markdown instruction body, not in the trigger configuration.

### Claim 5: `workflow_dispatch` security respects the same model as other triggers, with `roles:` and `bots:` fields for role-based and bot-identity access control

- **Evidence**: The page documents both access control mechanisms explicitly. For
  role-based access: `roles: [admin, maintainer]` in the frontmatter restricts
  trigger to named roles. For bot authorization: `bots: ["dependabot[bot]",
  "github-actions[bot]"]` explicitly authorizes named bot identities. The security
  model preamble states: "Manual workflow execution respects the same security
  model as other triggers: Repository permissions — User must have write access
  or higher to trigger workflows."
- **Confidence**: settled (first-party documentation; YAML fields are explicitly shown)
- **Quote**: "Manual workflow execution respects the same security model as other
  triggers: Repository permissions - User must have write access or higher to
  trigger workflows"
- **Our assessment**: The `roles:` field scopes trigger access below the
  "write access or higher" default — only users with the named roles can dispatch.
  The `bots:` field is the complement: it explicitly permits named bot identities
  that might otherwise be excluded by the role check. Together they give fine-grained
  access control at the trigger level. For Ch03 (Safety and Verification): the
  `roles:` field is the gh-aw mechanism for implementing least-privilege at the
  human-trigger layer — just as Safe Outputs (from `docs-ghaw-how-they-work.md`)
  is least-privilege at the write-operation layer. Corroborates
  `docs-ghaw-ephemerals.md` Claim 7, where the maintenance workflow's nine
  operations are also restricted to "admin and maintainer roles" via the same
  `roles:` mechanism.

### Claim 6: Fork protection is an inherent security property of `workflow_dispatch` — forks cannot trigger workflows in the parent repository, unlike issue/PR triggers

- **Evidence**: Explicitly stated as a design property: "Unlike issue/PR triggers,
  `workflow_dispatch` only executes in the repository where it's defined—forks
  cannot trigger workflows in the parent repository."
- **Confidence**: settled (first-party documentation; this is a structural property
  of the GitHub Actions platform, not a configuration option)
- **Quote**: "Unlike issue/PR triggers, `workflow_dispatch` only executes in the
  repository where it's defined—forks cannot trigger workflows in the parent
  repository."
- **Our assessment**: This is a materially different security posture from
  event-driven triggers. PR/issue triggers can fire from fork-submitted events —
  a security consideration for public repos (the "pwn request" attack vector where
  a malicious fork PR triggers a workflow with secrets access). `workflow_dispatch`
  is immune to this by design: the trigger is scoped to the defining repository
  and cannot be activated cross-repo. For Ch03: this fork-protection property
  should inform trigger selection for security-sensitive workflows. When a workflow
  handles sensitive secrets or has significant write permissions, prefer
  `workflow_dispatch` over PR/issue triggers if manual invocation is acceptable.
  This is a design choice, not a configuration toggle.

### Claim 7: The `manual-approval:` field implements environment approval gates as a human-in-the-loop primitive — requiring reviewer sign-off before workflow execution

- **Evidence**: The page documents the `manual-approval:` field: "Require manual
  approval before execution using GitHub environment protection rules" via
  `manual-approval: production`. Configuration of approval rules, required
  reviewers, and wait timers is done in repository Settings → Environments. The
  field value is the name of a GitHub environment with configured protection rules.
- **Confidence**: settled (first-party documentation; field name and integration
  with GitHub Environments is explicitly described)
- **Quote**: (no single prose quote captures the complete claim; the field name
  and mechanism are in the YAML example — see Concrete Artifacts)
- **Our assessment**: The `manual-approval:` field is the concrete implementation
  of the "human approval for critical actions" pattern from
  `docs-ghaw-how-they-work.md` Claim 10. It leverages GitHub's existing
  environment protection rules, so practitioners configure approval requirements
  in the familiar Environments UI rather than in a gh-aw-specific config. The
  combination of `roles:` (who can trigger) + `manual-approval:` (who must
  approve before execution) gives a two-layer human gate for sensitive dispatch
  workflows. For Ch05 (Human-in-the-Loop): this is the most concrete
  human-in-the-loop primitive in the gh-aw patterns corpus — a human explicitly
  approves each invocation before the agent runs.

### Claim 8: `gh aw run --wait` provides synchronous on-demand CLI invocation — monitors execution in real-time and exits with a success/failure code on completion

- **Evidence**: The page documents the `--wait` flag behavior: "`--wait` monitors
  progress in real-time and exits with a success/failure code on completion."
  Additional CLI options shown: `--raw-field` for passing input values,
  `--ref` for targeting a specific branch, `--repo` for cross-repo invocation,
  `--verbose` for detailed output.
- **Confidence**: settled (first-party documentation; flag name and behavior are
  explicitly described)
- **Quote**: "`--wait` monitors progress in real-time and exits with a
  success/failure code on completion."
- **Our assessment**: The `--wait` flag converts the default asynchronous dispatch
  into a blocking call that returns a machine-readable exit code. This enables
  shell scripting and CI composition: a pipeline can dispatch an agent task,
  block until it completes, and branch on success or failure. For Ch01 (Daily
  Workflows): document `gh aw run --wait` as the pattern for on-demand agent
  invocation that must complete before the calling process continues. This
  contrasts with the async default (fire and check separately) and enables
  integration of gh-aw agent tasks into scripts, makefiles, and non-gh-aw CI
  pipelines.

### Claim 9: Branch testing pattern — add `workflow_dispatch:` to feature branches and use `gh aw trial` for isolated testing before merge to the default branch

- **Evidence**: The page documents this as a development pattern: "Add
  `workflow_dispatch:` to feature branches for testing before merging" with two
  equivalent commands: `gh aw trial ./research.md --raw-field topic="test query"`
  (trial mode) and `gh aw run research --ref feature/improve-workflow` (run on
  branch). Both achieve isolated testing of workflow changes before they are
  promoted to the default branch.
- **Confidence**: settled (first-party documentation; both commands are explicitly
  shown)
- **Quote**: (no single prose quote; see Concrete Artifacts for command examples)
- **Our assessment**: This is the development lifecycle step between "authoring
  a workflow change" and "merging to the default branch." The dispatch-ops page
  establishes that `workflow_dispatch` is the mechanism that makes feature-branch
  testing possible — because `workflow_dispatch` can target `--ref feature-branch`,
  a practitioner can test workflow changes in isolation without merging. This
  extends `docs-ghaw-github-actions-primer.md` Claim 8 (which notes
  `workflow_dispatch` enables testing from any branch) with the concrete practice:
  add `workflow_dispatch:` to the feature branch trigger config, then use
  `gh aw trial` (safe, no-write-side-effects) or `gh aw run --ref` (production
  mechanics on the branch). For Ch02 (Harness Engineering): this is the final
  piece of the complete development lifecycle:
  `gh aw init` → compile → `gh aw trial` / `gh aw run --ref` (feature branch) →
  merge → production triggers.

## Concrete Artifacts

### Input Parameter YAML — Four Types

```yaml
# From DispatchOps documentation, "With Input Parameters" section
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

Note: `environment` type auto-populates from repository Settings → Environments;
no `options` list required. `boolean` type (not shown) is the fourth supported type.

### Security Model YAML — roles, bots, manual-approval

```yaml
# Role-based access (from "Security Model > Role-based access" section)
on:
  workflow_dispatch:
    roles: [admin, maintainer]

# Bot authorization (from "Security Model > Bot authorization" section)
on:
  workflow_dispatch:
    bots: ["dependabot[bot]", "github-actions[bot]"]

# Environment approval gate (from "Security Model > Environment Approval Gates" section)
on:
  workflow_dispatch:
    manual-approval: production
```

### Handlebars Conditionals — Input-Driven Behavior Branching

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

*Source: DispatchOps documentation, "Conditional Logic Based on Inputs" section*

### CLI Invocation Patterns

```bash
# Basic dispatch
gh aw run workflow

# With input parameters
gh aw run research --raw-field topic="quantum computing"
gh aw run scout \
  --raw-field topic="AI safety research" \
  --raw-field priority=high

# Synchronous: block until completion, exit with success/failure code
gh aw run research --raw-field topic="AI agents" --wait

# Branch targeting (for feature branch testing)
gh aw run research --ref feature-branch

# Cross-repo invocation
gh aw run workflow --repo owner/repository

# Verbose output
gh aw run research --raw-field topic="AI" --verbose
```

*Source: DispatchOps documentation, "Running Workflows with CLI" section*

### Branch Testing Pattern

```bash
# Option 1: Trial mode (no write side effects — safe for testing)
gh aw trial ./research.md --raw-field topic="test query"

# Option 2: Run on feature branch (production mechanics, on branch)
gh aw run research --ref feature/improve-workflow
```

Prerequisites: feature branch must include `workflow_dispatch:` in the `on:` section,
and the `.md` and `.lock.yml` must both be pushed to the branch.

*Source: DispatchOps documentation, "Development Pattern: Branch Testing" section*

### Trigger Type Decision Heuristic

```
When to use workflow_dispatch (DispatchOps):
  - Research tasks                       (scope varies by need)
  - Operational commands                 (human decides when to run)
  - Testing/debugging during development (pre-merge testing)
  - Debugging production issues          (on-demand diagnosis)
  - Any task that "doesn't fit a schedule or event trigger"

Use event-driven triggers when:
  - There is a natural GitHub event (PR opened, issue labeled, push)
  - The task should fire automatically in response to repository activity

Use scheduled triggers (DailyOps) when:
  - The task runs on a regular cadence regardless of events
  - Daily/weekly incremental automation (e.g., dependency updates, code quality)
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-github-actions-primer.md` Claim 8: documents `workflow_dispatch`
    as enabling "manual workflow execution from any branch for development and
    testing" — the dispatch-ops page is the dedicated canonical source that
    expands this incidental mention into a full design pattern with security model,
    typed inputs, Handlebars conditionals, and use-case taxonomy.
  - `docs-ghaw-how-they-work.md` Claim 10: "Critical actions can require human
    approval" — the `manual-approval:` field (Claim 7 here) is the concrete
    implementation of that pattern, using GitHub's environment protection rules
    as the approval gate mechanism.
  - `docs-ghaw-ephemerals.md` Claim 7: manual maintenance operations are
    "restricted to admin and maintainer roles" — the `roles:` field in dispatch-ops
    (Claim 5 here) is the same YAML mechanism used by the maintenance workflow.
    The two notes together confirm that `roles:` is a general-purpose access
    control primitive for any `workflow_dispatch`-triggered workflow.

- **Extends**:
  - `docs-ghaw-github-actions-primer.md` Claim 8 (`workflow_dispatch` as
    development-time escape hatch): the primer treats dispatch as an incidental
    capability for feature branch testing; this page is the dedicated reference
    that gives dispatch equal standing with event and schedule triggers, including
    a full security model, typed inputs, and use-case guidance. Together they give
    the complete picture: primer provides the architectural comparison context;
    this source provides the design pattern.
  - `docs-ghaw-agentic-authoring.md` Concrete Artifacts (branch testing with
    `gh aw trial`): the agentic-authoring note references `gh aw trial` in the
    debugging context; dispatch-ops establishes it as a standard step in the
    branch testing development pattern (Claim 9 here). The two together complete
    the `gh aw trial` usage picture: debugging failing runs (authoring guide) and
    testing workflow changes before merge (dispatch-ops).
  - `docs-ghaw-orchestration-patterns.md` Claim 2 (`dispatch-workflow` uses the
    `workflow_dispatch` API for async fan-out): the fork-protection property in
    Claim 6 here (dispatch is repository-scoped) is a security property that also
    applies to orchestration workers dispatched via `dispatch-workflow`. The
    dispatch-ops fork protection claim gives a security basis for why dispatching
    workers is safe in multi-repo setups.

- **Contradicts**: None identified. The security model described here
  (`roles:`, `bots:`, fork protection) does not contradict any existing source
  note — prior notes reference the mechanism in passing (`docs-ghaw-ephemerals.md`
  Claim 7) without detailing it. No contradiction issue filed.

- **Novel**:
  - **Typed input system** (Claim 2): The four-type vocabulary (`string`, `boolean`,
    `choice`, `environment`) for `workflow_dispatch` inputs, and especially the
    `environment` type auto-populating from Settings → Environments, is not
    documented in any existing source note.
  - **Handlebars conditionals for behavior branching** (Claim 4): The
    `{{#if (eq ...)}}` pattern for conditioning agent instruction text on input
    values is not described in any existing note.
  - **`roles:` and `bots:` access control fields** (Claim 5): While the
    maintenance operations note references role-gating in passing, the YAML fields
    (`roles:`, `bots:`) as explicit access control primitives for `workflow_dispatch`
    are new to the corpus.
  - **Fork protection as a design property** (Claim 6): The contrast between
    `workflow_dispatch` (repository-scoped, fork-safe) and issue/PR triggers
    (can fire from forks) is not stated in any existing source note.
  - **`manual-approval:` field and environment approval gates** (Claim 7): No
    existing source note documents the `manual-approval:` frontmatter field as
    a human-in-the-loop primitive.
  - **`gh aw run --wait` for synchronous invocation** (Claim 8): The `--wait`
    flag behavior (blocking, exits with success/failure code) is not described
    in any existing source note.
  - **Trigger type decision heuristic** (Claim 1): The explicit framing of
    dispatch for tasks that "don't fit a schedule or event trigger" as a
    decision rule is new to the corpus.

## Guide Impact

### Chapter 01: Daily Workflows

- **Add `gh aw run --wait` as the on-demand CLI pattern** (Claim 8): Document
  as the synchronous agent invocation idiom — dispatch an agent task, block until
  completion, branch on success/failure. This enables integrating gh-aw tasks
  into shell scripts and makefiles. The `--ref` flag (feature branch targeting)
  and `--repo` flag (cross-repo invocation) complete the on-demand CLI toolkit.

### Chapter 02: Harness Engineering

- **Complete the development lifecycle with branch testing** (Claim 9): The full
  gh-aw development lifecycle is now documented across several notes:
  `gh aw init` (from `docs-ghaw-agentic-authoring.md`) → compile → `gh aw trial`
  or `gh aw run --ref` (from this source, on feature branch) → merge → production
  triggers. Add this note as the reference for the feature-branch testing step.

- **Add parameterized agent invocation as a harness design pattern** (Claims 2–4):
  The combination of typed inputs, `${{ github.event.inputs.NAME }}` interpolation,
  and Handlebars conditionals gives a complete pattern for configurable, multi-mode
  agent harnesses. Practitioners designing an agent that must behave differently
  based on human-provided context (scope, target environment, urgency) should
  use this three-layer pattern.

### Chapter 03: Safety and Verification

- **Add fork protection as a trigger selection criterion** (Claim 6): For workflows
  handling sensitive secrets or with significant write permissions, `workflow_dispatch`
  is inherently safer than PR/issue triggers because forks cannot activate it.
  Add as a security-aware trigger selection principle alongside the five-layer
  defense-in-depth model from `docs-ghaw-how-they-work.md`.

- **Add `roles:` + `manual-approval:` as the two-layer human gate** (Claims 5, 7):
  The `roles:` field controls who can initiate a dispatch (access control);
  `manual-approval:` controls who must approve before execution (approval gate).
  Together they implement the "human approval for critical actions" principle from
  `docs-ghaw-how-they-work.md` Claim 10 at the trigger level. Recommend this
  two-layer pattern for any workflow with significant blast radius.

### Chapter 05: Human-in-the-Loop Patterns

- **Name `workflow_dispatch` as the canonical manual-trigger primitive** (Claim 1):
  The three trigger classes (event-driven, scheduled, manual) and the decision
  heuristic ("tasks that need human judgment about timing") belong in Ch05 as the
  introductory framing for human-in-the-loop automation. DispatchOps is the
  concrete implementation of "human decides when the agent runs."

- **Add `manual-approval:` as the human-in-the-loop approval primitive** (Claim 7):
  The `manual-approval:` field is the only pattern in the corpus that requires a
  named human reviewer to approve each agent invocation before execution begins.
  Add it as the highest-friction, highest-control point in the human-in-the-loop
  spectrum (compared to async review after the fact, or `roles:` access control
  before invocation).

### Chapter 06: Orchestration

- **Add trigger type selection framework** (Claim 1): The dispatch / schedule /
  event taxonomy provides a decision framework for orchestration designers choosing
  how to trigger each workflow in an agent factory. The "doesn't fit schedule or
  event" heuristic for dispatch is actionable and should be cited alongside the
  use-case list (research, operational commands, debugging, testing).

## Extraction Notes

1. **Source is compact but actionable**: The dispatch-ops page is shorter than most
   gh-aw documentation pages. It is structured around practical how-to sections
   rather than conceptual exposition. The highest-value content is the security
   model section (Claims 5–7), the input types and Handlebars pattern (Claims 2–4),
   and the `--wait` CLI flag (Claim 8) — all new to the corpus.

2. **No contradiction identified**: Reviewed all existing source notes.
   `docs-ghaw-github-actions-primer.md` Claim 8 mentions `workflow_dispatch`
   as a development testing escape hatch — this source does not oppose that claim,
   it extends it with a full design pattern. The security model claims (5–7) are
   novel to the corpus; no prior note makes opposing claims. No contradiction issue
   filed.

3. **YAML field placement**: The page shows `roles:`, `bots:`, and `manual-approval:`
   as sub-keys under the `workflow_dispatch:` block in the `on:` section, consistent
   with gh-aw's frontmatter extension of standard GitHub Actions syntax.

4. **No publication date**: The page does not carry an explicit publication date.
   `date_published` is left null. Content is consistent with current gh-aw platform
   behavior as of 2026-05-03.

5. **`gh aw trial` in branch testing**: The source shows `gh aw trial` used for
   branch testing. This command also appears in `docs-ghaw-agentic-authoring.md`
   in the debugging context. The two usages are complementary — trial mode (no write
   side effects) serves both pre-merge testing (dispatch-ops) and post-failure
   debugging (agentic-authoring).

6. **Prospector note on full patterns library**: The first triage comment flagged
   that the GH-AW site has 15+ patterns visible in nav (BatchOps, ChatOps, DailyOps,
   DataOps, IssueOps, LabelOps, MultiRepoOps, ProjectOps, ResearchPlanAssignOps,
   SideRepoOps, SpecOps, TaskOps, TrialOps, WorkQueueOps) not yet all captured.
   Several of these (ChatOps, IssueOps, LabelOps) already have dedicated source
   notes. Others (BatchOps, WorkQueueOps, TrialOps) may warrant future mining.
