---
source_url: https://github.github.com/gh-aw/patterns/monitoring
source_type: docs
title: "GitHub Agentic Workflows: Projects & Monitoring Patterns"
author: GitHub Agentic Workflows team (GitHub Next)
date_published: null
date_extracted: 2026-05-01
last_checked: 2026-05-01
status: current
confidence_overall: emerging
issue: "#328"
---

# GitHub Agentic Workflows: Projects & Monitoring Patterns

> Implementation-level complement to the observatory architecture in
> `blog-ghaw-agent-observability.md` — documents the config-layer primitives
> practitioners use to track what workflows did (`update-project`,
> `create-project-status-update`), aggregate failures at scale
> (`group-reports: true`), suppress no-op noise
> (`noop: report-as-issue: false`), and operationally inspect runs
> (`gh aw audit`, `gh aw logs --format markdown`).

## Source Context

- **Type**: docs (GitHub Agentic Workflows `patterns/monitoring` page — a
  practitioner implementation reference in the `patterns/` section, distinct
  from the `guides/` section and the blog series. Patterns pages describe
  configuration-layer patterns rather than conceptual architecture or
  end-to-end workflow specs.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team
  (same team behind Peli de Halleux's agent factory and the `gh aw` platform
  documentation). YAML configs and CLI commands are authoritative for the
  `gh aw` platform. High credibility for platform-specific claims; behavioral
  details (e.g., sub-issue caps, default behavior) do not automatically
  generalize to non-`gh-aw` systems.
- **Scope**: Covers five monitoring pattern areas: (1) GitHub Projects v2
  integration via `update-project` and `create-project-status-update` safe
  outputs; (2) failure issue creation and aggregation; (3) no-op run report
  control; (4) practitioner CLI monitoring commands. Does NOT cover: how to
  deploy audit-consuming agent workflows (see `docs-ghaw-audit-with-agents.md`),
  the JSON field schema for `gh aw audit` output, specific regression
  thresholds, or the underlying audit engine design.

## Extracted Claims

### Claim 1: `update-project` safe output integrates workflow runs with GitHub Projects v2, providing a durable structured audit trail of what each agent discovered, decided, and did

- **Evidence**: YAML config published on the page shows the `update-project`
  safe output with `project:` URL, `max:` cap, and `github-token:` fields.
  Description states it "adds issues/PRs to the board and updates custom
  fields" — not just appending items but updating structured project data per
  run.
- **Confidence**: emerging (first-party documentation; behavior described
  at a config level without production metrics on adoption)
- **Quote**: "adds issues/PRs to the board and updates custom fields"
- **Our assessment**: Projects v2 as a durable agent memory layer is
  architecturally distinct from ephemeral run logs or transient issues. The
  safe output model means this write is permission-separated — the workflow
  doesn't hold write access to the project board directly; it requests the
  `update-project` operation. The `max:` cap prevents unbounded board growth.
  For Ch02 (Harness Engineering): document `update-project` as the canonical
  safe output for workflows that should leave a persistent, queryable record
  of their decisions — particularly useful for orchestrator and investigator
  workflows where you want to see across runs "what did this agent find?"
  For Ch04 (Multi-agent orchestration): the Projects v2 board functions as
  the agent fleet's shared state store — a structured, human-readable surface
  where agents write their findings and humans (and other agents) read them.

### Claim 2: `create-project-status-update` safe output enables scheduled and orchestrator workflows to post run summaries as project status updates

- **Evidence**: YAML config shows `create-project-status-update` with the
  same `project:` URL and `github-token:` fields as `update-project`, but
  with `max: 1` — indicating it posts a single status update per run rather
  than updating multiple items.
- **Confidence**: emerging (first-party documentation; the use case for
  status-updates vs. item-updates is inferred from the `max: 1` default)
- **Quote**: (no direct description quote beyond config; implied: post
  run summaries to project status updates)
- **Our assessment**: The `max: 1` cap on `create-project-status-update`
  (vs. `max: 10` on `update-project`) signals it is designed for a single
  narrative summary per run rather than per-item updates. This is the
  "executive briefing" output for a workflow: not "I touched these 10 PRs"
  but "here is the run summary for the week." For scheduled orchestrator
  workflows that coordinate multiple sub-tasks, a status update is more
  readable than a pile of item updates. For Ch04: recommend
  `create-project-status-update` for orchestrator workflows that need to
  communicate overall run health; use `update-project` for worker workflows
  that produce per-artifact outputs.

### Claim 3: The `Tracker Id` custom field pattern correlates multiple workflow runs to a single tracking entity using run IDs, issue numbers, or initiative keys

- **Evidence**: The page documents adding custom text fields (e.g., "Tracker
  Id") to the Projects v2 board to correlate multiple runs using a common
  identifier such as run ID, issue number, or initiative key.
- **Confidence**: emerging (described as a pattern on the page; the specific
  field name "Tracker Id" appears to be an example rather than a required
  convention)
- **Quote**: "Add custom text fields (like 'Tracker Id') to correlate
  multiple runs using run IDs, issue numbers, or initiative keys."
- **Our assessment**: Run correlation is a non-trivial problem in agentic
  systems: when a workflow runs 50 times over a sprint, you need a way to
  group runs by the initiative they serve. The Tracker Id pattern solves
  this by adding a semantic link from the run's project board entry to the
  work item it belongs to. This makes the Projects v2 board a navigable
  audit trail rather than an unstructured list of runs. For Ch04: document
  Tracker Id (or equivalent) as a required field for any `update-project`
  safe output config on workflows that run repeatedly against bounded
  initiatives — it is the join key between run-level data and initiative-level
  reporting.

### Claim 4: `create-issue` with `title-prefix: "[failed]"` and `labels: [automation, failed]` makes workflow failures searchable and filterable at scale

- **Evidence**: YAML config from the page:
  ```yaml
  safe-outputs:
    create-issue:
      title-prefix: "[failed] "
      labels: [automation, failed]
  ```
  The `title-prefix` ensures failure issues are visually distinct and
  searchable by prefix; the labels enable label-filtered queries across all
  failure issues in the repository.
- **Confidence**: settled (first-party documented configuration; the
  mechanism — title prefix + labels — is straightforward and confirmed
  by the `docs-ghaw-ephemerals.md` reference to failure issues opened by
  the conclusion job)
- **Quote**: (from YAML config; not a prose quote)
- **Our assessment**: The label + prefix combination gives two independent
  filtering axes for failure triage: you can query `label:failed` to see
  all active failures across all workflows, or search `[failed]` in the
  title to find failures related to a specific workflow. For high-frequency
  polling workflows, this prevents failure issues from getting lost in the
  issue tracker noise. For Ch02: recommend the `title-prefix: "[failed] "`
  + `labels: [automation, failed]` pattern as a standard config for any
  workflow that creates failure issues — it makes the issue tracker
  self-organizing for failure triage.

### Claim 5: `group-reports: true` in `create-issue` aggregates multiple failure reports as sub-issues under a shared parent `[aw] Failed runs` issue, capping at 64 sub-issues per parent

- **Evidence**: The page documents that `group-reports: true` automatically
  creates a parent issue titled `[aw] Failed runs` when the first failure
  occurs, and links each subsequent failure as a sub-issue under that parent.
  Maximum of 64 sub-issues per parent is specified.
- **Confidence**: settled (first-party documentation; the parent issue title
  and sub-issue cap are explicit)
- **Quote**: "This automatically creates a parent '[aw] Failed runs' issue
  and tracks up to 64 sub-issues."
- **Our assessment**: Without grouping, a high-frequency workflow that runs
  hourly and hits a persistent failure generates 24+ individual failure issues
  per day — tracker scatter that obscures whether failures are related. With
  `group-reports: true`, all failures from the same workflow family aggregate
  under one parent, making it visually obvious that failures are clustered
  and reducing triage overhead. The 64-sub-issue cap prevents the parent
  issue from becoming unmanageable. This is an operational anti-chaos pattern
  for agent fleets at scale. For Ch02: recommend `group-reports: true` as
  the default config for any scheduled workflow with `create-issue` failure
  reporting — the signal-clarity benefit compounds as factory scale grows.
  Cross-reference `docs-ghaw-ephemerals.md` Claim 9 for the companion
  `action_failure_issue_expires` config that auto-expires these grouped
  failure issues after 168 hours (7 days).

### Claim 6: `noop: report-as-issue: false` suppresses "nothing to do" issue creation for workflows that frequently find no work, controlling signal-to-noise ratio in high-frequency polling workflows

- **Evidence**: The page documents two no-op control options:
  1. `noop: report-as-issue: false` — prevents issue creation when the
     workflow finds nothing to do, while preserving other run artifacts
  2. `noop: false` — disables no-op output entirely
- **Confidence**: settled (first-party documentation; config options are
  specific and documented)
- **Quote**: "Set `noop: false` to disable no-op output entirely."
- **Our assessment**: Default behavior is that workflows which find nothing
  to do still post a visible comment/issue signaling "no action needed." This
  is valuable for low-frequency or high-stakes workflows (proves the agent
  ran and found nothing). But for a workflow that polls hourly and typically
  finds nothing, posting 23 "nothing to do" issues per day per workflow
  creates severe tracker noise. `noop: report-as-issue: false` suppresses the
  issue while preserving other safe output artifacts (e.g., project board
  updates), giving fine-grained control over which no-op signals are visible.
  This is distinct from the `noop` *safe output tool* (from
  `docs-ghaw-audit-with-agents.md` Claim 6), which is an explicit success
  signal emitted by the agent from within a workflow; `noop: report-as-issue:
  false` is a config option that controls whether the platform creates a
  visible artifact for no-op runs. For Ch02: teams should set
  `noop: report-as-issue: false` for high-frequency polling workflows
  (hourly/daily triage agents) and leave the default (issue on no-op) for
  low-frequency or security-critical workflows where a "nothing found" record
  is valuable.

### Claim 7: `gh aw audit <run-id>` provides per-run operational inspection including tool usage, MCP failures, firewall activity, and cost metrics as a practitioner CLI command

- **Evidence**: CLI command from the page: `gh aw audit 12345678`.
  Listed alongside `gh aw status` and `gh aw logs` as operational monitoring
  commands for practitioner use.
- **Confidence**: settled (first-party documented CLI; consistent with the
  audit command schema documented in `docs-ghaw-audit-with-agents.md`)
- **Quote**: (CLI command from the page)
- **Our assessment**: The practitioner-operator framing of `gh aw audit` is
  distinct from the agent-workflow-consumption framing in
  `docs-ghaw-audit-with-agents.md`. That guide covers how *agent workflows*
  consume audit output via the `agentic-workflows` MCP tool; this page covers
  how *human operators* run the same audit from the CLI for ad-hoc inspection.
  Both paths exist; this page clarifies the practitioner's entry point. For
  Ch05 (Team Adoption): document `gh aw audit <run-id>` as the first tool to
  reach for when investigating an unexpected agent behavior — before writing
  a consumer workflow, run the audit CLI on the suspicious run.

### Claim 8: `gh aw audit <id1> <id2>` (two-run form) is the practitioner CLI command for detecting behavioral regressions between runs across cost, firewall, and MCP tool dimensions

- **Evidence**: CLI command from the page: `gh aw audit 12345678 12345679`.
  The two-run form is the CLI equivalent of the `audit diff` operation
  documented in `docs-ghaw-audit-with-agents.md` Claim 9, presented here
  as a practitioner inspection tool rather than a workflow-internal mechanism.
- **Confidence**: settled (first-party documented CLI; the two-argument form
  for diff is consistent with `docs-ghaw-audit-with-agents.md` which
  documents the same operation via the MCP tool `audit diff`)
- **Quote**: (CLI command from the page: `gh aw audit 12345678 12345679`)
- **Our assessment**: The CLI diff operation fills an important gap in the
  operational workflow: when an engineer notices a cost spike or unexpected
  firewall block in a recent run, they need to compare it to a known-good
  run without setting up a full regression detection workflow. The two-run
  CLI form enables one-off comparisons at the terminal. For Ch02: document
  this as the manual complement to the automated `audit diff` workflow in
  `docs-ghaw-audit-with-agents.md` — use the CLI for ad-hoc investigation,
  use the workflow for systematic regression gates.

### Claim 9: `gh aw logs --format markdown [workflow]` run inside a scheduled workflow agent automates trend monitoring, closing the monitoring loop without manual intervention

- **Evidence**: The page explicitly recommends running `gh aw logs --format
  markdown` inside a scheduled workflow agent for automated trend analysis.
  CLI command variants: `gh aw logs --format markdown [workflow]` and
  `gh aw logs my-workflow --format markdown --count 10`.
- **Confidence**: emerging (first-party recommendation; the pattern of
  running a CLI tool inside an agent is described but not with production
  metrics confirming its use)
- **Quote**: (recommendation from the page to run this inside a scheduled
  workflow agent for automated trend monitoring without manual intervention)
- **Our assessment**: The fully-closed loop — a scheduled agent runs
  `gh aw logs` against the fleet, formats the output as markdown, and posts
  a digest — is the implementation-level realization of the observatory
  architecture described in `blog-ghaw-agent-observability.md`. This page
  provides the single-command starting point for that loop; the full
  workflow spec (including cache-memory for rolling baselines) is documented
  in `docs-ghaw-audit-with-agents.md` Claim 11. For Ch04: this is the
  concrete recommendation for teams that want the observatory pattern without
  building custom infrastructure — one scheduled workflow, one CLI command,
  markdown output to a Discussion.

## Concrete Artifacts

### GitHub Projects v2 Safe Output Configs

```yaml
# update-project: add/update items on a Projects v2 board
safe-outputs:
  update-project:
    project: https://github.com/orgs/myorg/projects/123
    max: 10
    github-token: ${{ secrets.GH_AW_PROJECT_GITHUB_TOKEN }}

# create-project-status-update: post a run summary to project status
safe-outputs:
  create-project-status-update:
    project: https://github.com/orgs/myorg/projects/123
    max: 1
    github-token: ${{ secrets.GH_AW_PROJECT_GITHUB_TOKEN }}
```

*Source: gh-aw patterns/monitoring, "Project Board Tracking" section*

### Failure Reporting Safe Output Config

```yaml
# Title prefix + labels: searchable failure issues
safe-outputs:
  create-issue:
    title-prefix: "[failed] "
    labels: [automation, failed]

# group-reports: aggregate failures under a shared parent (max 64 sub-issues)
safe-outputs:
  create-issue:
    group-reports: true
```

When `group-reports: true`, the platform automatically creates a parent
issue titled `[aw] Failed runs` on first failure; subsequent failure issues
are linked as sub-issues. Companion config in `aw.json`:
`action_failure_issue_expires: 72` (hours) auto-expires the grouped parent
and its sub-issues (default 168h / 7 days — see `docs-ghaw-ephemerals.md`
Claim 9).

*Source: gh-aw patterns/monitoring, "Failure Reporting" section*

### No-Op Run Report Control

```yaml
# Suppress issue creation for no-op runs (preserve other artifacts)
safe-outputs:
  create-issue:
    noop:
      report-as-issue: false

# Disable no-op output entirely
safe-outputs:
  create-issue:
    noop: false
```

*Source: gh-aw patterns/monitoring, "No-Op Handling" section*

### Operational CLI Monitoring Commands

```bash
# Status of all workflows in the repository
gh aw status

# Per-run audit (tool usage, MCP failures, firewall activity, cost)
gh aw audit 12345678

# Two-run diff: detect behavioral regressions between runs
gh aw audit 12345678 12345679

# Cross-run log report in markdown (for human reading or agent consumption)
gh aw logs --format markdown [workflow]

# Filtered to last N runs of a specific workflow
gh aw logs my-workflow --format markdown --count 10
```

*Source: gh-aw patterns/monitoring, "Operational Monitoring" section*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-agent-observability.md` Claim 1 ("Observability isn't optional
    when you're running dozens of AI agents"): This page provides the
    configuration-level toolset that backs that architectural thesis — the
    Projects v2 audit trail, failure aggregation, and CLI inspection tools
    are the concrete mechanisms that make the observatory viable. The blog
    post names the observatory plane; this page provides the dials and levers.
  - `docs-ghaw-audit-with-agents.md` Claim 9 (`audit diff` for regression
    detection): The `gh aw audit <id1> <id2>` CLI command on this page is
    the practitioner-CLI form of the same operation that Claim 9 documents
    as a workflow-internal mechanism via the MCP tool. Both are valid; this
    page confirms the operation is accessible from the terminal as well.
  - `docs-ghaw-ephemerals.md` Claim 9 (`action_failure_issue_expires` auto-
    expires grouped failure issues): That note's mention of "grouped parent
    issues when `group-reports: true`" is the expiry-lifecycle counterpart
    to this page's creation-lifecycle description of `group-reports`. Together
    they give the full lifecycle of a grouped failure report: created here,
    expired there.

- **Extends**:
  - `blog-ghaw-agent-observability.md` — that note covers the *what* (three-
    tier observatory plane, production metrics) and the *why* (observability
    as first-class architecture). This page covers the *how to configure* —
    the YAML primitives that power the observatory. The two together give the
    complete picture: architectural motivation + implementation config.
  - `docs-ghaw-audit-with-agents.md` — that guide covers the *agent-workflow
    consumption* perspective: how autonomous workflows consume `gh aw audit`
    JSON output via the MCP tool, with full workflow specs and field schemas.
    This page covers the *practitioner-operator* perspective: CLI commands
    for ad-hoc inspection and config patterns for failure tracking and Projects
    v2 integration. The two perspectives are complementary — one is for
    workflow authors building audit consumers; the other is for operators
    doing live investigation.
  - `docs-ghaw-ephemerals.md` — ephemerals covers the expiry and lifecycle
    of safe outputs (when they close, how maintenance frequency is derived).
    This page extends the safe-output model with two new output types
    (`update-project`, `create-project-status-update`) and two behavioral
    configs (`group-reports`, `noop: report-as-issue`) not covered in the
    ephemerals doc.

- **Contradicts**: None. The `noop: report-as-issue: false` config (Claim 6)
  is distinct from — not in conflict with — the `noop` safe output tool
  documented in `docs-ghaw-audit-with-agents.md` Claim 6. One is a platform
  config that suppresses issue creation for no-op runs; the other is an
  explicit safe output the agent emits to signal completion with no action.
  They operate at different layers and can coexist.

- **Novel**:
  - **`update-project` and `create-project-status-update` safe outputs**
    (Claims 1–2): No existing source note documents these two safe output
    types. This is the first corpus entry describing GitHub Projects v2 as
    a durable agent-state store.
  - **`Tracker Id` correlation field** (Claim 3): The pattern of using a
    custom Projects v2 field to correlate multiple runs to an initiative key
    is not described anywhere in the corpus.
  - **`group-reports: true` as a failure aggregation pattern** (Claim 5):
    `docs-ghaw-ephemerals.md` mentions `group-reports` in a single line about
    expiry config; this is the first source that describes the feature itself —
    parent/sub-issue structure, 64-sub-issue cap, `[aw] Failed runs` naming.
  - **`noop: report-as-issue: false` config** (Claim 6): The distinction
    between suppressing no-op issue creation (this source) and calling the
    `noop` safe output tool (as documented in `docs-ghaw-audit-with-agents.md`)
    is new. This source adds the configuration path for operators who want
    high-frequency polling workflows without no-op tracker noise.
  - **Practitioner-operator framing of `gh aw audit` and `gh aw logs`**
    (Claims 7–9): Existing notes (`docs-ghaw-audit-with-agents.md`) document
    these commands from the perspective of agent-workflow authors building
    automated consumers. This is the first note framing them as CLI tools for
    human practitioners doing live investigation — a distinct and practical use
    case.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add `update-project` + `create-project-status-update` as the standard
    safe output pattern for workflows that need a durable, queryable audit
    trail. Distinguish from ephemeral issue/discussion outputs: Projects v2
    items persist and support custom fields for structured querying.
  - Add `title-prefix: "[failed]"` + `labels: [automation, failed]` as the
    required config pattern for any workflow using `create-issue` for failure
    reporting — these two fields are what make failure triage tractable at
    scale.
  - Add `group-reports: true` as the default for scheduled failure-reporting
    workflows; pair with `action_failure_issue_expires` (from
    `docs-ghaw-ephemerals.md`) for the full failure-lifecycle pattern.
  - Add `noop: report-as-issue: false` as the recommended config for
    high-frequency polling workflows where "nothing to do" is the expected
    outcome in most runs.
  - Document the Tracker Id pattern as a join key for runs that serve
    bounded initiatives.

- **Chapter 04 (Multi-agent orchestration patterns)**:
  - Add the `update-project` safe output as a shared-state mechanism for
    multi-agent systems: each worker agent writes its discoveries to the
    board; orchestrators and humans read the board to see fleet-wide activity.
    This is a concrete implementation of the "durable external state" pattern
    (see `discussion-hn-ttal-multiagent-factory.md` for the abstract version).
  - Add the `create-project-status-update` as the orchestrator's status
    communication channel — a structured way for orchestrator workflows to
    communicate overall run health to the board.

- **Chapter 05 (Team Adoption)**:
  - The `gh aw logs my-workflow --format markdown --count 10` command is the
    starting point for teams that want trend visibility before they invest in
    building full audit-consumer workflows. Recommend as a first step: run
    this weekly manually, then automate it in a scheduled workflow once the
    value is confirmed.
  - The `gh aw audit <run-id>` CLI command is the go-to investigation tool
    for teams debugging unexpected agent behavior. Document as part of the
    "day-2 operations" onboarding section.

## Extraction Notes

1. **Source is a patterns page, not a guide page**: The `patterns/` section
   of `github.github.com/gh-aw/` documents configuration patterns rather
   than end-to-end workflow implementations. This page focuses on the safe-
   output config options for monitoring-related outputs and the CLI commands
   available to practitioners. It is intentionally more concise than a
   guide page — the depth comes from the YAML configs and CLI commands, not
   from extended explanation.

2. **Overlap with `docs-ghaw-audit-with-agents.md` is real but additive**:
   Both sources reference `gh aw audit <run-id>` and `gh aw logs --format
   markdown`. The overlap is the same CLI commands viewed from different
   perspectives: this page frames them as practitioner tools; that guide
   frames them as agent-workflow inputs. Both perspectives are valid and
   document real use cases. They are marked as corroborating, not
   duplicative.

3. **`group-reports: true` cap of 64 sub-issues**: The 64-sub-issue cap is
   a platform limit. When a parent issue reaches 64 sub-issues, subsequent
   failures will either create a new parent or stop grouping (behavior at
   cap not specified on the page). Teams running very high failure-rate
   workflows should account for this limit.

4. **`noop: report-as-issue: false` vs. `noop` safe output tool**: These
   are two different mechanisms. The config suppresses issue creation at the
   platform level (before the agent runs); the safe output tool is an
   explicit agent-side signal (the agent calls it after determining there is
   nothing to do). Both may coexist: `noop: report-as-issue: false` prevents
   the platform from creating a no-op issue, while the agent still calls the
   `noop` safe output to confirm it completed successfully.

5. **No contradictions filed**: Reviewed `blog-ghaw-agent-observability.md`,
   `docs-ghaw-audit-with-agents.md`, `docs-ghaw-ephemerals.md`,
   `docs-ghaw-agent-factory-status.md`, and `docs-ghaw-how-they-work.md`.
   No claims in this source materially oppose existing source notes at the
   MINER.md §4a filing threshold.
