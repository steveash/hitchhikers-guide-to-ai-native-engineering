---
source_url: https://github.github.com/gh-aw/reference/triggers
source_type: docs
title: "GitHub Agentic Workflows: Triggers Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#418"
---

# GitHub Agentic Workflows: Triggers Reference

> The canonical reference for gh-aw trigger configuration — documents the complete
> trigger taxonomy (dispatch, schedule, event, slash_command, label_command, reaction),
> fuzzy schedule scattering, skip-if-match/skip-if-no-match conditional execution,
> stop-after cost controls, on.steps pre-activation YAML syntax, lock-for-agent
> concurrency protection, status-comment feedback, and compiler-injected security
> hardening for workflow_run and PR fork filtering; the first corpus source to cover
> several of these cross-cutting trigger features at the reference level.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/triggers` page — in
  the "Reference" section alongside `reference/concurrency`, `reference/permissions`,
  `reference/network`. Reference pages document platform behavior precisely; this one
  specifies the complete trigger configuration model across all trigger types.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same
  team behind Peli de Halleux's agent factory blog series and the `gh aw` platform.
  YAML field names, compiler behaviors, and trigger semantics are authoritative for the
  `gh aw` platform. Claims about trigger design choices and patterns do not automatically
  generalize to non-gh-aw agentic systems.
- **Scope**: The complete gh-aw trigger configuration — all supported trigger types
  (with full YAML schemas), shorthand syntax, skip conditions, cost controls, pre-
  activation configuration, status feedback mechanisms, and compiler security
  hardening for triggers. Does NOT cover: the Safe Outputs permission model in depth
  (see `docs-ghaw-how-they-work.md`), the full DispatchOps pattern including security
  model and Handlebars conditionals (see `docs-ghaw-dispatch-ops.md`), IssueOps
  sub-issue hierarchies (see `docs-ghaw-issueops.md`), LabelOps design principles
  (see `docs-ghaw-labelops.md`), ChatOps slash_command patterns (see
  `docs-ghaw-chatops.md`), or the DailyOps scheduling pattern in full (see
  `docs-ghaw-dailyops.md`).

## Extracted Claims

### Claim 1: GitHub Agentic Workflows supports all standard GitHub Actions triggers plus additional enhancements for reactions, cost control, and advanced filtering — all configured via the same `on:` section

- **Evidence**: The page opens with this scope statement, positioning gh-aw's trigger
  system as a superset of GitHub Actions triggers rather than a replacement. The `on:`
  section is explicitly identified as using "standard GitHub Actions syntax to define
  workflow triggers," with the six gh-aw-specific enhancements (reactions, cost control,
  filtering, pre-activation, status feedback, lock-for-agent) layered on top.
- **Confidence**: settled (first-party; scope statement is explicit)
- **Quote**: "GitHub Agentic Workflows supports all standard GitHub Actions triggers
  plus additional enhancements for reactions, cost control, and advanced filtering."
- **Our assessment**: The "superset" framing is significant for practitioners migrating
  from standard GitHub Actions: existing trigger configurations are valid gh-aw trigger
  configurations. The gh-aw value-add is the cross-cutting enhancements (skip conditions,
  cost controls, status feedback) that apply to any trigger type, not a replacement
  trigger model. For Ch03 (Workflow Orchestration): frame gh-aw triggers as "standard
  Actions triggers plus a safety and cost management layer" — this positions the
  enhancements correctly and reduces migration friction for teams adopting gh-aw.

### Claim 2: Fuzzy schedule triggers scatter execution times automatically — the compiler assigns each workflow a unique, deterministic execution time based on the file path to avoid load spikes

- **Evidence**: The page documents fuzzy schedule syntax as: `on: schedule: daily`,
  `on: schedule: daily around 14:00` (scatters within ±1 hour), `on: schedule: daily
  between 9:00 and 17:00` (uniform random within the window), and UTC-offset forms like
  `on: schedule: daily between 9am and 5pm utc-5`. The scattering mechanism: "the
  compiler assigns each workflow a unique, deterministic execution time based on the
  file path." Standard cron syntax is also supported alongside the fuzzy forms.
- **Confidence**: settled (first-party documentation; the scattering mechanism and syntax
  forms are explicitly described)
- **Quote**: "the compiler assigns each workflow a unique, deterministic execution time
  based on the file path"
- **Our assessment**: The "deterministic based on file path" property is novel — it
  means the same workflow file always compiles to the same execution time, making the
  schedule reproducible and auditable. A workflow that specifies `daily around 14:00`
  will always scatter to the same specific time each rebuild (e.g., 14:23), not a random
  time each day. This is different from traditional cron (fully deterministic) and from
  true random scattering (non-reproducible). The "avoid load spikes" motivation is
  practical: in an agent factory with 183+ workflows all set to `daily`, running all at
  midnight would saturate the AI engine. The compiler's file-path-based scattering
  distributes load automatically without manual cron planning. For Ch03 (Workflow
  Orchestration): recommend fuzzy schedules over precise cron for any agent factory with
  multiple daily workflows — the compiler handles load distribution, no manual schedule
  offset planning needed.

### Claim 3: skip-if-match conditionally skips workflow execution when a GitHub search query has matches — with optional `max:` threshold and cross-org `scope: none`

- **Evidence**: The page documents `skip-if-match` with two forms: string shorthand
  (`skip-if-match: 'is:issue is:open in:title "[daily-report]"'`) and object form
  (`query:` + optional `max: 3` threshold meaning "skip if 3 or more PRs match"). The
  `scope: none` option "disables the automatic `repo:owner/repo` qualifier" enabling
  org-wide search queries like `org:myorg label:ops:in-progress is:issue is:open`.
- **Confidence**: settled (first-party documentation; YAML fields and example queries
  are explicitly shown)
- **Quote**: "Conditionally skip workflow execution when a GitHub search query has
  matches."
- **Our assessment**: `skip-if-match` is a pre-execution guard that allows workflows
  to be self-limiting based on current GitHub state. A daily workflow that posts a
  `[daily-report]` issue can check if a report was already posted before creating a
  duplicate. A deployment workflow can skip if too many urgent PRs are open
  (avoiding noise during a crisis). The `scope: none` for org-wide queries enables
  cross-repository coordination without explicit inter-workflow communication — a
  workflow in repo A can skip if repo B has an in-progress operation. For Ch03:
  document `skip-if-match` as the idempotency guard for recurring workflows — always
  check if the intended artifact already exists before re-creating it. The `scope:
  none` pattern enables lightweight cross-repo state awareness without the full
  orchestrator/worker machinery.

### Claim 4: skip-if-no-match is the inverse — skip when a GitHub search query returns fewer than `min:` results — enabling workflows to only run when preconditions are met

- **Evidence**: Basic form: `skip-if-no-match: 'is:pr is:open label:ready-to-deploy'`
  (skip if no PRs match). Object form with threshold: `query: "is:issue is:open label:urgent"` + `min: 3` (only run if 3 or more issues match). Applicable to any trigger type
  including `workflow_dispatch`.
- **Confidence**: settled (first-party; syntax and examples are explicitly shown)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: `skip-if-no-match` is the precondition check for workflows that
  should only run when there is work to do. A weekly deployment review workflow should
  skip if there are no PRs labeled `ready-to-deploy`. A batch triage workflow should
  only run when enough urgent issues have accumulated (`min: 3`). Together, `skip-if-match`
  and `skip-if-no-match` form a bidirectional guard system: one prevents duplicate
  execution, the other prevents empty execution. Both query live GitHub state at trigger
  time, ensuring the guard reflects current repository reality. For Ch03: name this pair
  as "execution guards" — standard practice for all recurring and event-driven workflows
  in production agent factories.

### Claim 5: stop-after automatically disables workflow triggering after a deadline to control costs — supporting both relative (`"+25h"`) and absolute (`"2025-06-15"`) date formats

- **Evidence**: The page documents `stop-after` with two forms: `stop-after: "+25h"`
  (25 hours from compilation time) and `stop-after: "2025-06-15"` (absolute date). Also
  `"+7d"` is given as an example. The field applies to any trigger type.
- **Confidence**: settled (first-party; field name, formats, and behavior are explicitly
  described)
- **Quote**: "Automatically disable workflow triggering after a deadline to control costs"
- **Our assessment**: `stop-after` is a cost ceiling at the trigger configuration level —
  instead of remembering to manually disable a workflow after a sprint or deployment
  window closes, the harness author declares an expiry at compile time. The `+25h` form
  is especially useful for time-limited experiments or deployment windows: "this workflow
  should fire for the next day but not after that." The absolute date form suits
  known deadlines (sprint end, release date). Without `stop-after`, a misconfigured
  scheduled workflow left running after its purpose expires is a pure cost leak. For Ch03
  (Workflow Orchestration) and Ch04 (Automation Patterns): recommend `stop-after` as
  standard hygiene for any time-limited agentic workflow. Corroborates
  `docs-ghaw-how-they-work.md` Claim 10 ("Critical actions can require human approval")
  — `stop-after` is the counterpart: it disables the workflow automatically rather than
  requiring a human to remember to turn it off.

### Claim 6: on.steps injects custom deterministic steps directly into the pre-activation job — outcomes are auto-wired as `<id>_result` outputs that the agent job can condition on via `if:`

- **Evidence**: The page documents `on.steps` with a YAML example showing a step that
  checks issue labels via a shell command. The step's exit code is wired to an output
  named `<id>_result` (e.g., `label_check_result`). The activation condition
  `if: needs.pre_activation.outputs.label_check_result == 'success'` is shown as the
  downstream gate. For explicit outputs: steps can write `echo "has_bug_label=true" >>
  "$GITHUB_OUTPUT"` and the value is accessible in `pre-activation` job outputs.
- **Confidence**: settled (first-party documentation; YAML syntax and output wiring
  are explicitly shown)
- **Quote**: "Inject custom deterministic steps directly into the pre-activation job"
- **Our assessment**: `on.steps` is the YAML-frontmatter entry point for the
  "deterministic pre-computation → AI agent" hybrid pipeline described in
  `docs-ghaw-deterministic-agentic-patterns.md`. The key operational detail here
  (not in the deterministic-agentic-patterns guide): the `<id>_result` auto-wiring
  means any non-zero exit code from a shell step automatically sets the result to a
  non-success value, which the `if:` condition can gate on. Practitioners don't need
  to manually wire exit codes to outputs — the platform handles it. For Ch03: the
  `on.steps` + `if: needs.pre_activation.outputs.<id>_result` pattern is the canonical
  gh-aw mechanism for conditional agent activation. If a pre-activation check fails
  (e.g., label not present, precondition not met), the agent job is skipped, saving
  AI compute cost. Cross-reference with `docs-ghaw-deterministic-agentic-patterns.md`
  Claim 1 for the full hybrid pipeline pattern.

### Claim 7: on.needs and on.permissions allow pre-activation jobs to declare dependency jobs and additional token scopes — supporting complex multi-stage pre-activation pipelines

- **Evidence**: The page documents `on.needs` as adding "custom jobs that pre_activation
  and activation depend on" and `on.permissions` as granting "additional token scopes to
  pre-activation jobs for GitHub API calls."
- **Confidence**: settled (first-party; field names and semantics are explicitly described)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: `on.needs` enables pre-activation pipelines where multiple
  deterministic jobs must complete before the agent runs — for example, a compilation
  step and a linting step, both completing before the agent reviews the code. This is the
  `needs:` dependency mechanism from standard GitHub Actions, exposed at the trigger
  level. `on.permissions` allows pre-activation steps to make GitHub API calls (e.g.,
  fetching additional context, querying a GitHub Projects board) without elevating the
  agent job's permissions. Together with `on.steps`, these three fields give full
  control over pre-activation pipeline composition. For Ch02 (Harness Engineering):
  distinguish the three pre-activation configuration points: `on.steps` (inline shell
  commands), `on.needs` (external job dependencies), `on.permissions` (token scopes).
  A harness author needs all three to build sophisticated pre-agent data pipelines.

### Claim 8: workflow_run and deployment_status triggers enable cross-workflow and deployment-lifecycle automation — the compiler injects repository ID and fork checks for workflow_run to prevent cross-repository or fork exploitation

- **Evidence**: `workflow_run`: "Trigger workflows after another workflow completes"
  with `conclusion:` filtering for `success`, `failure`, `cancelled`. `deployment_status`:
  "Trigger workflows when a GitHub deployment status changes" with `state:` filtering
  for `error`, `failure`, `pending`, `success`. Compiler security for `workflow_run`:
  "The compiler injects repository ID and fork checks, rejecting cross-repository or
  fork-triggered runs."
- **Confidence**: settled (first-party; both trigger types and the compiler security
  injection are explicitly documented)
- **Quote**: "The compiler injects repository ID and fork checks, rejecting
  cross-repository or fork-triggered runs."
- **Our assessment**: `workflow_run` and `deployment_status` are the triggers for
  composing workflow chains and integrating with deployment pipelines — both absent from
  the existing corpus. The compiler's automatic injection of repository ID and fork checks
  for `workflow_run` is a concrete instance of `docs-ghaw-how-they-work.md` Claim 3
  (Layer 1: compilation-time validation), applied specifically to close the "fork trigger"
  attack vector on cross-workflow composition. Without this, a fork could submit a PR that
  triggers a `workflow_run` listener in the parent repository — a variant of the "pwn
  request" attack. The compiler closes this at compile time rather than requiring
  practitioners to add manual fork guards. For Ch03 (Safety and Verification): the compiler's
  fork-check injection for `workflow_run` is a named security property that practitioners
  should know is automatic — they do not need to add fork guards manually for this trigger
  type.

### Claim 9: Pull request triggers support a `forks:` filter field that enables practitioners to explicitly configure fork-PR filtering behavior at the trigger level

- **Evidence**: The page documents `on: pull_request:` as supporting a `forks:` field
  alongside the standard `types: [opened, synchronize, labeled]` and `names:` label
  filtering. This gives explicit declarative control over whether fork-originated PRs
  can activate the trigger.
- **Confidence**: settled (first-party; the `forks:` field is documented as a PR trigger
  option)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `forks:` field on PR triggers complements the fork protection
  described in `docs-ghaw-dispatch-ops.md` Claim 6 — that note establishes that
  `workflow_dispatch` is inherently fork-safe. This claim establishes that PR triggers
  provide explicit `forks:` configuration rather than inherent protection. The two
  together give practitioners the full fork protection picture: dispatch triggers are
  fork-safe by design; PR triggers require explicit `forks:` configuration to control
  fork behavior. For Ch03: add PR trigger fork configuration to the security discussion
  alongside the dispatch fork protection guarantee.

### Claim 10: lock-for-agent on issues and issue_comment triggers prevents concurrent modifications to the same item during agent execution

- **Evidence**: For `on: issues: types: [opened, edited]`, setting `lock-for-agent: true`
  prevents concurrent modifications. Same option is available for `on: issue_comment:
  types: [created, edited]`. The field appears in both issue and comment trigger contexts.
- **Confidence**: settled (first-party; field name and placement in YAML are explicitly shown)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: `lock-for-agent` is the trigger-level complement to the two-tier
  concurrency model in `docs-ghaw-concurrency-reference.md`. The concurrency reference
  covers group-based queueing at the workflow level; `lock-for-agent` provides an
  additional protection specifically against concurrent edits to the triggering item
  during agent execution (e.g., preventing a human from editing an issue while the agent
  is analyzing it). This is distinct from workflow concurrency — it's about the *item*
  being processed, not the *workflow run* being queued. For Ch03 (Safety and
  Verification): document `lock-for-agent: true` as the standard safety configuration
  for any issue or comment trigger where the agent's analysis depends on the item content
  being stable during processing.

### Claim 11: status-comment posts a started/completed comment on the triggering item — supports boolean form (true/false) and selective targeting by event type

- **Evidence**: Boolean form: `status-comment: true` posts on the triggering item when
  the workflow starts and completes. Object form enables per-type targeting:
  `issues: true`, `pull-requests: false`, `discussions: false` — enabling selective
  status feedback per event type in a multi-trigger workflow. The comment includes a
  link to the workflow run.
- **Confidence**: settled (first-party; both forms and targeting semantics are explicitly shown)
- **Quote**: "Post a started/completed comment on the triggering item with a link"
- **Our assessment**: `status-comment` closes a UX gap in agentic workflows — without
  it, a human who files an issue has no visible feedback that an agent is processing it.
  The started/completed comment pattern (with run link) gives participants in the issue
  or PR a direct link to the agent's work, enabling review and intervention if needed.
  The per-type targeting is important for multi-trigger workflows: a workflow triggered
  by both `issues:` and `pull_request:` events might want status comments on PRs
  (where collaborators are watching) but not on issues (to avoid comment noise). For
  Ch01 (Daily Workflows): recommend `status-comment: true` as a default for any
  IssueOps or ChatOps workflow — it makes agentic activity transparent and builds
  human trust in the automation.

### Claim 12: reaction adds emoji feedback to triggering items — a lightweight visual acknowledgment that the workflow has received the trigger

- **Evidence**: Available emoji values: `+1`, `-1`, `laugh`, `confused`, `heart`,
  `hooray`, `rocket`, `eyes`. Configured as `reaction: "eyes"` (or any other emoji) in
  the trigger block. Can be disabled with `none`.
- **Confidence**: settled (first-party; field name, values, and disable option are
  explicitly documented)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: `reaction` (typically `eyes` = "I'm looking at this") is the
  lowest-friction feedback mechanism in gh-aw — it does not add a comment, just an emoji
  reaction to the triggering item. In high-volume issue repositories, comment noise is
  a real friction point; a reaction emoji is a lighter touch that signals "the agent
  saw this" without adding content. Combined with `status-comment: true`, the typical
  pattern is: reaction on trigger receipt (immediate feedback) + status comment when
  the agent begins work (with run link) + completion comment when done. For Ch01:
  document `reaction: "eyes"` + `status-comment: true` as the standard feedback
  configuration for interactive trigger workflows.

### Claim 13: Shorthand syntax compiles natural-language trigger strings into standard GitHub Actions YAML and automatically includes workflow_dispatch — reducing boilerplate while maintaining security

- **Evidence**: "Instead of writing full YAML trigger configurations, you can use
  natural-language shorthand strings with `on:`. The compiler expands these into
  standard GitHub Actions trigger syntax and automatically includes `workflow_dispatch`."
  Examples: `on: push to main`, `on: pull_request merged`, `on: issue opened labeled bug`,
  `on: "deployment failed"`, `on: manual with input version`.
- **Confidence**: settled (first-party; mechanism and examples are explicitly described)
- **Quote**: "The compiler expands these into standard GitHub Actions trigger syntax
  and automatically includes `workflow_dispatch`."
- **Our assessment**: The automatic inclusion of `workflow_dispatch` in every compiled
  shorthand is a significant design choice — it means every workflow with a shorthand
  trigger is also manually invocable via the UI, API, or CLI at no additional
  configuration cost. This enables the branch testing pattern from
  `docs-ghaw-dispatch-ops.md` Claim 9 (`gh aw run --ref feature-branch`) for any
  workflow, not just those explicitly configured with `workflow_dispatch:`. For Ch02
  (Harness Engineering): recommend shorthand syntax for standard trigger configurations;
  it reduces YAML boilerplate and guarantees `workflow_dispatch` accessibility. The
  full YAML form remains appropriate when the practitioner needs fine-grained control
  over trigger configuration (custom `types:`, `forks:`, complex input schemas).

## Concrete Artifacts

### Fuzzy Schedule Trigger — All Supported Forms

```yaml
# Minimal — compiler assigns a unique scattered time per workflow (file-path-derived)
on: schedule: daily

# Time-constrained — scatters within ±1 hour of target
on:
  schedule: daily around 14:00

# Window — uniform random within the specified range
on:
  schedule: daily between 9:00 and 17:00

# With UTC offset — window expressed in local timezone
on:
  schedule: daily between 9am and 5pm utc-5  # 9am-5pm EST → 2pm-10pm UTC

# Standard cron (still supported)
on:
  schedule:
    - cron: '0 14 * * *'
```

*Source: gh-aw Triggers Reference, "Scheduled Triggers" section*

### skip-if-match — All Supported Forms

```yaml
# String shorthand — skip if any issue has [daily-report] in title
on: daily
skip-if-match: 'is:issue is:open in:title "[daily-report]"'

# Object form with threshold — skip if 3 or more urgent PRs exist
on: weekly on monday
skip-if-match:
  query: "is:pr is:open label:urgent"
  max: 3  # Skip if 3 or more PRs match

# Cross-org query (scope: none disables auto repo:owner/repo qualifier)
on:
  schedule: every 15 minutes
skip-if-match:
  query: "org:myorg label:ops:in-progress is:issue is:open"
  scope: none
```

*Source: gh-aw Triggers Reference, "Skip Conditions — skip-if-match" section*

### skip-if-no-match — All Supported Forms

```yaml
# String shorthand — skip if no PRs are ready-to-deploy
on: weekly on monday
skip-if-no-match: 'is:pr is:open label:ready-to-deploy'

# Object form with minimum threshold — only run if 3+ urgent issues exist
on:
  workflow_dispatch:
skip-if-no-match:
  query: "is:issue is:open label:urgent"
  min: 3  # Only run if 3 or more issues match
```

*Source: gh-aw Triggers Reference, "Skip Conditions — skip-if-no-match" section*

### stop-after — Cost Control

```yaml
# Relative: disable 25 hours from compilation time
on: weekly on monday
stop-after: "+25h"

# Relative: disable after 7 days from compilation
on: daily
stop-after: "+7d"

# Absolute: disable after a specific date
on: daily
stop-after: "2025-06-15"
```

*Source: gh-aw Triggers Reference, "Cost Control — stop-after" section*

### Pre-Activation via on.steps — with Auto-Wired Exit Code Output

```yaml
on:
  issues:
    types: [opened]
  steps:
    - name: Check issue label
      id: label_check
      env:
        LABELS: ${{ toJSON(github.event.issue.labels.*.name) }}
      run: echo "$LABELS" | grep -q '"bug"'

# Agent job activation condition:
if: needs.pre_activation.outputs.label_check_result == 'success'
```

For explicit outputs from pre-activation steps:
```yaml
on:
  issues:
    types: [opened]
  steps:
    - name: Check issue label
      id: label_check
      run: |
        if echo "$LABELS" | grep -q '"bug"'; then
          echo "has_bug_label=true" >> "$GITHUB_OUTPUT"
        else
          echo "has_bug_label=false" >> "$GITHUB_OUTPUT"
        fi
```

*Source: gh-aw Triggers Reference, "Pre-Activation — on.steps" section*

### Status Feedback — reaction + status-comment

```yaml
# Minimal feedback: emoji reaction only
on:
  issues:
    types: [opened]
  reaction: "eyes"

# Full feedback: emoji + started/completed comment
on:
  issues:
    types: [opened]
  reaction: "eyes"
  status-comment: true

# Selective feedback: different behavior per event type
on:
  issues:
    types: [opened]
  pull_request:
    types: [opened]
  discussion:
    types: [created]
  status-comment:
    issues: true          # post on issue events
    pull-requests: false  # skip pull request events
    discussions: false    # skip discussion events
```

*Source: gh-aw Triggers Reference, "Status Feedback — reaction and status-comment" sections*

### lock-for-agent — Concurrent Modification Prevention

```yaml
# For issues — prevent concurrent edits during agent execution
on:
  issues:
    types: [opened, edited]
    lock-for-agent: true

# For issue comments
on:
  issue_comment:
    types: [created, edited]
    lock-for-agent: true
```

*Source: gh-aw Triggers Reference, "Event Triggers — lock-for-agent" section*

### workflow_run and deployment_status Triggers

```yaml
# workflow_run — trigger after another workflow completes
# Compiler automatically injects repository ID and fork checks
on:
  workflow_run:
    workflows: ["CI"]
    conclusion: success  # or: failure, cancelled

# deployment_status — trigger on GitHub deployment lifecycle events
on:
  deployment_status:
    state: success  # or: error, failure, pending
```

*Source: gh-aw Triggers Reference, "Event Triggers — workflow_run and deployment_status" sections*

### Trigger Shorthand Syntax — Natural Language to YAML

```yaml
# These shorthand strings:
on: push to main
on: pull_request merged
on: issue opened labeled bug
on: "deployment failed"
on: manual with input version

# Are compiled into equivalent full YAML and automatically include workflow_dispatch.
# Example expansion (conceptual):
#   on: issue opened labeled bug
#   → on:
#       issues:
#         types: [opened]
#         names: [bug]
#       workflow_dispatch:  ← automatically added
```

*Source: gh-aw Triggers Reference, "Shorthand Syntax" section*

### Complete Trigger Type Reference Summary

```
Trigger category         | gh-aw syntax            | Notes
-------------------------|-------------------------|-----------------------------
Manual dispatch          | workflow_dispatch:       | See docs-ghaw-dispatch-ops.md
Fuzzy schedule           | schedule: daily around X | File-path-based scatter
Event: issues            | issues: types: [...]    | lock-for-agent available
Event: pull_request      | pull_request: types:... | forks: filter field
Event: issue_comment     | issue_comment:          | lock-for-agent available
Event: PR review comment | pull_request_review_comment: |
Event: discussion_comment| discussion_comment:     |
Event: workflow_run      | workflow_run:           | Compiler injects fork check
Event: deployment_status | deployment_status:      | state: filter
Command: slash_command   | slash_command:          | See docs-ghaw-chatops.md
Command: label_command   | label_command:          | See docs-ghaw-labelops.md
Reaction                 | reaction: "eyes"        | Emoji feedback
─────────────────────────────────────────────────────────────────────────────
Cross-cutting features (apply to any trigger type):
  skip-if-match          | Idempotency guard — skip if artifact already exists
  skip-if-no-match       | Precondition guard — skip if no work to do
  stop-after             | Cost ceiling — disable after deadline
  on.steps               | Pre-activation deterministic steps
  on.needs               | Pre-activation job dependencies
  on.permissions         | Pre-activation token scopes
  status-comment         | Started/completed feedback comment
  lock-for-agent         | Concurrent edit prevention
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer defense-in-depth: Layer 1 =
    compilation-time validation): Claim 8 here provides a concrete instance — the
    compiler's automatic injection of repository ID and fork checks for `workflow_run`
    triggers is a named compile-time security hardening step. Together these two sources
    establish that compiler security injection is both a general principle (how-they-work)
    and a specific implementation (triggers reference for workflow_run).
  - `docs-ghaw-dispatch-ops.md` Claim 6 (fork protection is inherent to
    `workflow_dispatch` — forks cannot trigger the parent): Claim 9 here extends the
    fork protection picture to PR triggers, which require explicit `forks:` configuration
    rather than inherent protection. The two sources together give the complete fork
    protection model: dispatch = inherently safe; PR triggers = explicit configuration
    required; workflow_run = compiler injects fork check automatically.
  - `docs-ghaw-concurrency-reference.md` (two-tier concurrency model): Claim 10
    (`lock-for-agent`) is a trigger-level concurrency primitive that complements the
    workflow-level concurrency groups in the concurrency reference. Both sources address
    concurrent execution safety; this note's claim is scoped to item-level modification
    safety rather than run-level queuing.
  - `docs-ghaw-deterministic-agentic-patterns.md` Claim 1 (three-stage hybrid pipeline —
    deterministic jobs → agent → safe outputs): Claim 6 here (`on.steps`) is the
    frontmatter YAML entry point to the pre-activation stage of that three-stage pipeline.
    Both sources describe the same feature; this note gives the reference-level YAML
    syntax; the deterministic-agentic-patterns guide gives the pattern rationale and
    use cases.
  - `docs-ghaw-how-they-work.md` Claim 10 ("Critical actions can require human approval"):
    Claim 5 here (`stop-after`) is the temporal complement — `manual-approval:` gates
    individual invocations; `stop-after` disables the entire workflow trigger after a
    deadline. Together they give the full human control surface: per-invocation gates
    and lifecycle expiry.

- **Extends**:
  - `docs-ghaw-dispatch-ops.md` (DispatchOps pattern — full `workflow_dispatch` reference):
    Claim 13 here establishes that the compiler automatically includes `workflow_dispatch`
    in any shorthand-syntax trigger. This means DispatchOps capabilities (CLI invocation,
    `--wait`, `--ref` branch targeting) are available to any workflow using shorthand
    syntax, not just those explicitly adding `workflow_dispatch:`. The triggers reference
    extends the scope of DispatchOps to "all shorthand workflows."
  - `docs-ghaw-dailyops.md` (scheduled triggers): Claim 2 here provides the reference-
    level documentation for fuzzy schedule syntax with all supported forms (daily around,
    daily between, UTC offsets) and the compiler's file-path-based scattering mechanism.
    DailyOps covers the operational pattern; this note covers the complete syntax
    reference. Together they give both the "when to use" (DailyOps) and the "how to
    configure" (triggers reference) for scheduled workflows.
  - `docs-ghaw-issueops.md` Claim 1 (`on: issues: types: [opened]` trigger): this note
    adds `lock-for-agent: true` as an option on the same trigger that IssueOps documents.
    IssueOps covers the permission and safe-output model for issues; this note adds the
    concurrent-edit guard. For any IssueOps workflow where the agent's analysis depends
    on stable issue content, both sources should be applied together.
  - `docs-ghaw-chatops.md` (`slash_command` trigger): the reaction and status-comment
    features (Claims 11, 12) apply to slash_command triggers just as they do to other
    event triggers. The ChatOps note does not document these feedback mechanisms; this
    reference fills that gap.

- **Contradicts**: None. The trigger taxonomy and cross-cutting features described here
  are fully consistent with the patterns documented in the existing source notes. No
  claim here materially opposes any claim in any existing source note. The fuzzy schedule
  scattering mechanism is new but does not contradict DailyOps scheduling claims. The
  compiler's fork-check injection for `workflow_run` extends (rather than opposes) the
  compile-time validation claims in `docs-ghaw-how-they-work.md`. No contradiction issue
  filed.

- **Novel** (what this note adds to the corpus):
  - **skip-if-match and skip-if-no-match as execution guards** (Claims 3, 4): No prior
    corpus source documents these conditional skip primitives, their query syntax, `max:`
    and `min:` thresholds, or the `scope: none` cross-org query option. These are the
    primary idempotency and precondition mechanisms for production gh-aw workflows.
  - **stop-after as a trigger-level cost ceiling** (Claim 5): No prior source documents
    the `stop-after` field or its relative/absolute date formats. The "automatic disable
    after deadline" pattern is new to the corpus.
  - **on.steps YAML syntax with auto-wired `<id>_result` outputs** (Claim 6): The
    deterministic-agentic-patterns guide covers pre-activation at the pattern level;
    this note adds the specific frontmatter YAML fields (`on.steps`, step ID, GITHUB_OUTPUT
    wiring) needed to implement the pattern.
  - **on.needs and on.permissions for pre-activation pipeline composition** (Claim 7):
    Not documented in any existing source note. Enables multi-job pre-activation
    pipelines with explicit dependency ordering.
  - **workflow_run and deployment_status triggers** (Claim 8): No prior corpus source
    documents either trigger type, their filtering fields (`conclusion:`, `state:`), or
    the compiler's automatic fork-check injection for `workflow_run`.
  - **lock-for-agent concurrent modification prevention** (Claim 10): Not documented
    in any existing source note, including the concurrency reference. Item-level locking
    (vs. workflow-level queuing) is a distinct concurrency safety primitive.
  - **status-comment started/completed feedback with per-type targeting** (Claim 11):
    No prior source documents this mechanism. The selective targeting option (`issues:
    true`, `pull-requests: false`) for multi-trigger workflows is particularly novel.
  - **reaction as a lightweight acknowledgment mechanism** (Claim 12): ChatOps mentions
    reactions in passing; this note provides the reference-level documentation of all
    eight supported emoji values and the `none` disable option.
  - **Shorthand syntax auto-including workflow_dispatch** (Claim 13): The automatic
    inclusion of `workflow_dispatch` in all compiled shorthand triggers is documented
    here for the first time. This has material implications for branch testing
    accessibility (all shorthand workflows are also manually invocable).
  - **Fuzzy schedule compiler scattering mechanism** (Claim 2): DailyOps covers
    scheduling at the pattern level. The specific mechanism — file-path-based deterministic
    time assignment — is documented here for the first time. The reproducibility
    property (same file → same time) is a new and actionable detail.

## Guide Impact

### Chapter 03: Workflow Orchestration

- **Add skip-if-match as the standard idempotency guard for recurring workflows**
  (Claims 3, 4): Any daily or weekly workflow that produces a GitHub artifact (issue,
  comment, PR) should include a `skip-if-match` guard to prevent duplicates when the
  workflow fires on a day where the artifact already exists. Document the string shorthand
  form for simple cases and the object form with `max:` for threshold-based skipping.
  Also add `skip-if-no-match` as the precondition guard for workflows that should only
  run when work is available.

- **Add stop-after as standard hygiene for time-limited workflows** (Claim 5): Any
  workflow with a finite useful lifetime (sprint experiments, deployment windows,
  feature-flagged automation) should include a `stop-after` deadline. Recommend the
  relative `+Nd`/`+Nh` form for development and the absolute date form for planned
  release cutoffs.

- **Add lock-for-agent as the standard configuration for issue/comment triggers**
  (Claim 10): Any IssueOps or ChatOps workflow whose analysis depends on the item
  content being stable should include `lock-for-agent: true`. Document this alongside
  the concurrency reference's workflow-level queue settings as a complementary
  item-level safety mechanism.

- **Add workflow_run and deployment_status to the trigger taxonomy** (Claim 8): These
  two triggers enable CI/CD pipeline composition with agentic workflows — an agent can
  fire when a build succeeds or a deployment fails. Add them to the trigger decision
  guide alongside event-driven and schedule triggers. Note the automatic fork-check
  injection as a security property practitioners get without configuration.

### Chapter 04: Automation Patterns

- **Add skip-if-match with scope: none as a cross-repo state awareness pattern**
  (Claim 3): The `scope: none` option enables workflows in one repository to check
  the state of issues/PRs across the organization before executing. This is a
  lightweight alternative to full orchestrator/worker coordination for simple
  mutual-exclusion scenarios.

- **Add fuzzy schedule scattering as the recommended scheduling approach for agent
  factories** (Claim 2): In a multi-workflow factory, precise cron scheduling causes
  load spikes; fuzzy schedules scatter load automatically via file-path-based deterministic
  time assignment. Recommend `daily around HH:MM` over precise cron for any workflow
  where exact execution time is not critical.

### Chapter 02: Harness Engineering

- **Complete the trigger taxonomy** (Claims 1, 13): Add the full trigger reference
  (all types + cross-cutting features) to Ch02. Specifically document the shorthand
  syntax's automatic `workflow_dispatch` inclusion — it means all shorthand workflows
  support `gh aw run`, `gh aw trial`, and `--ref` branch targeting without additional
  configuration.

- **Add on.steps + on.needs + on.permissions as the three pre-activation configuration
  points** (Claims 6, 7): Extend the harness engineering trigger section with the
  complete YAML reference for pre-activation pipeline composition. Cross-reference with
  `docs-ghaw-deterministic-agentic-patterns.md` for the pattern rationale.

- **Add reaction + status-comment as the standard feedback configuration** (Claims 11,
  12): Recommend `reaction: "eyes"` + `status-comment: true` as the default for any
  interactive trigger. Document the per-type targeting syntax for multi-trigger workflows.

## Extraction Notes

1. **Reference page vs. patterns pages**: This page is in the `reference/` section
   (alongside `reference/concurrency`, `reference/permissions`, `reference/network`)
   rather than the `patterns/` section. Reference pages document complete platform
   behavior; patterns pages document specific workflow designs. Many trigger types
   (workflow_dispatch, schedule, issues, slash_command, label_command) have dedicated
   patterns pages in the corpus. This note focuses on what the reference page adds
   beyond the patterns pages — primarily the cross-cutting features (skip conditions,
   stop-after, pre-activation YAML, status feedback) and the complete taxonomy.

2. **WebFetch returned summaries, not full verbatim text**: The page is an Astro/
   Starlight-rendered SPA. Three WebFetch calls were made to extract content at
   progressively more granular levels. The YAML examples and quotes in this note
   are verbatim from the WebFetch responses; however, the WebFetch model occasionally
   summarizes surrounding prose. Section intros and non-YAML prose may not be fully
   captured. The Assayer should treat all quotes in this note as sourced from WebFetch
   output rather than direct page HTML.

3. **No publication date**: The page does not carry an explicit publication date.
   `date_published` is left null. Content is consistent with current gh-aw platform
   behavior as of 2026-05-11.

4. **scope: none confirmed**: The cross-org `scope: none` option for skip conditions
   was explicitly documented in the WebFetch response with a quoted description. This
   is the trigger-level complement to the multi-repo patterns described in
   `docs-ghaw-multi-repo-ops.md`.

5. **No contradictions filed**: Reviewed all relevant existing source notes.
   No claim in this source materially opposes any existing source note. The fuzzy
   schedule scattering extends `docs-ghaw-dailyops.md`; the compiler fork-check
   injection extends `docs-ghaw-how-they-work.md` Claim 3; `lock-for-agent` extends
   `docs-ghaw-concurrency-reference.md`. All extensions, no oppositions.
