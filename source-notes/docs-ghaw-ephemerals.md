---
source_url: https://github.github.com/gh-aw/guides/ephemerals
source_type: docs
title: "GitHub Agentic Workflows: Ephemerals"
author: GitHub Agentic Workflows team (official documentation)
date_published: null
date_extracted: 2026-04-22
last_checked: 2026-04-22
status: current
confidence_overall: emerging
issue: "#295"
---

# GitHub Agentic Workflows: Ephemerals

> The canonical reference for GH-AW's resource lifecycle management system —
> documents the `stop-after` deadline primitive for cost-controlled workflows,
> auto-expiring safe outputs (issues/discussions/PRs) with checkbox-based
> human override, cache-memory cleanup strategy, and the full maintenance
> operations suite — together constituting the first complete harness
> maintenance-lifecycle model in our corpus.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, "Ephemerals"
  guide page; not a blog post or practitioner account)
- **Author credibility**: First-party documentation from the GitHub Agentic
  Workflows team. Same team behind the Peli de Halleux / Don Syme agent factory
  series. Claims about platform behavior (deadlines, expiration mechanics,
  maintenance workflow generation) are settled for this platform; do not
  automatically generalize to other agentic systems.
- **Scope**: Platform lifecycle features — `stop-after` workflow deadline
  enforcement, safe output expiration (issues/discussions/PRs), cache-memory
  cleanup, manual maintenance operations, and maintenance workflow configuration.
  Does NOT cover: the full Safe Outputs permission model (see
  `docs-ghaw-how-they-work.md`), the five-layer security architecture, or
  specific workflow examples from the agent factory series.

## Extracted Claims

### Claim 1: `stop-after` is a first-class cost-control primitive that disables workflow triggering after an absolute or relative deadline

- **Evidence**: The page documents a `stop-after:` frontmatter field accepting
  absolute dates (YYYY-MM-DD, MM/DD/YYYY, DD/MM/YYYY, ISO 8601, natural language
  like "1st June 2025") and relative deltas (+7d, +25h, +1d12h30m calculated
  from compilation time). Minimum granularity is hours — minute-only units
  (e.g., +30m) are not allowed. Stated use cases: trial periods, experimental
  features, orchestrated initiatives, cost-controlled schedules.
- **Confidence**: settled (first-party documentation; the CLI mechanism is
  described precisely including the compile-time calculation basis)
- **Quote**: "Automatically disable workflow triggering after a deadline to
  control costs and prevent indefinite execution."
- **Our assessment**: `stop-after` addresses a real failure mode — workflows
  deployed for a bounded initiative (sprint, experiment, external initiative)
  that silently continue running and accumulating cost after the initiative
  ends. The deadline is baked in at compile time, which means it requires
  intentional recompilation to reset. This is the correct design: it makes
  cost extension a deliberate act, not an accidental default. The `+25h`
  relative format is particularly useful for workflows that are experimental
  from day one — compile with a short deadline, extend only if the experiment
  proves value. For Ch07 (Cost Management): recommend `stop-after` as a
  mandatory harness field for any workflow deployed for a bounded purpose.

### Claim 2: At the `stop-after` deadline, new runs are blocked while in-flight runs complete; the stop time persists through recompilation unless explicitly reset

- **Evidence**: The page states: "At the deadline, new runs are prevented while
  existing runs complete. The stop time persists through recompilation; use
  `gh aw compile --refresh-stop-time` to reset it." This implies that
  `gh aw compile` alone does NOT reset the stop time — you must pass
  `--refresh-stop-time` explicitly.
- **Confidence**: settled (first-party documentation; specific CLI flag documented)
- **Quote**: "The stop time persists through recompilation; use
  `gh aw compile --refresh-stop-time` to reset it."
- **Our assessment**: The "persists through recompilation" behavior is the
  important safety property: it prevents the stop-after deadline from being
  silently bypassed by a routine recompile (e.g., to update an unrelated
  frontmatter field). The explicit `--refresh-stop-time` flag makes deadline
  extension a conscious, observable action in git history. This is a good
  model for harness engineers designing other lifecycle gates: make extension
  intentional, not automatic.

### Claim 3: Safe output types (issues, discussions, PRs) support `expires:` config for automatic closure after a time window, accepting integer days or relative time strings

- **Evidence**: Three YAML patterns documented:
  - Issues: `safe-outputs.create-issue.expires: 7` (7 days)
  - Discussions: `safe-outputs.create-discussion.expires: 3` (3 days as "OUTDATED")
  - PRs: `safe-outputs.create-pull-request.expires: 14` (14 days, same-repo only)
  Supported formats: integer (days), or relative time string (2h, 7d, 2w, 1m, 1y).
  Hours less than 24 are treated as 1 day minimum.
- **Confidence**: settled (first-party documentation with specific YAML examples)
- **Quote**: "Auto-close issues, discussions, and pull requests after a specified
  time period."
- **Our assessment**: The `expires:` config is the concrete instantiation of
  ephemeral safe outputs. Prior source notes knew Safe Outputs existed as a
  permission pattern (`docs-ghaw-how-they-work.md` Claim 5) but had no
  visibility into the expiration dimension. The combination of Safe Outputs +
  expiration gives a complete pattern for time-bounded agentic announcements:
  the agent creates an artifact with write-separated permission AND the artifact
  self-cleans after a configured window. For Ch02 (Harness Engineering): the
  `create-discussion` + `expires: 14` + `close-older-discussions: true`
  combination is the canonical pattern for weekly reports and periodic analyses.
  For Ch03 (Safety): auto-expiry is a safety mechanism — stale agent-generated
  content that persists indefinitely can mislead future readers or downstream
  processes.

### Claim 4: The maintenance workflow frequency is algorithmically derived from the shortest `expires:` value across all workflows — not configured manually

- **Evidence**: A table maps shortest expiration to maintenance frequency:
  - ≤1 day → every 2 hours
  - 2 days → every 6 hours
  - 3–4 days → every 12 hours
  - 5+ days → daily
  The maintenance workflow (`agentics-maintenance.yml`) is auto-generated by
  the compiler at the minimum required frequency.
- **Confidence**: settled (first-party documentation; table is specific and
  algorithmic)
- **Quote**: "This generates a maintenance workflow that runs automatically at
  appropriate intervals."
- **Our assessment**: Auto-derived maintenance scheduling solves a real
  configuration problem: practitioners who forget to set maintenance frequency
  appropriately for their expiration windows end up with stale closures (too
  infrequent) or unnecessary CI cost (too frequent). The algorithm removes
  this as a decision point — the compiler owns it. This is a good harness
  design pattern: have the toolchain derive operational parameters from the
  same spec that declares intent, rather than requiring a separate operational
  config. For Ch02: this is an example of "config surface minimization" —
  fewer settings to misconfigure because the tool derives what it can.

### Claim 5: The expiration checkbox mechanism — a checked checkbox with an embedded XML timestamp comment — can be unchecked by users to prevent automatic closure

- **Evidence**: The expiration marker format is:
  ```
  - [x] expires <!-- gh-aw-expires: 2026-01-14T15:30:00.000Z --> on Jan 14, 2026, 3:30 PM UTC
  ```
  The maintenance workflow searches for items with this format (checked checkbox
  + XML comment) and closes them. Users can uncheck the checkbox to prevent
  automatic expiration.
- **Confidence**: settled (first-party documentation; format is specified exactly)
- **Quote**: "Users can uncheck the checkbox to prevent automatic expiration."
- **Our assessment**: This is a lightweight human-override mechanism embedded
  in the artifact itself. The checkbox doubles as an expiration display and an
  override toggle. The XML comment carries machine-readable state; the checkbox
  carries the human decision. The design is clever: it makes the expiration
  timestamp visible to users reading the issue/discussion, and it gives them
  a zero-friction override path (uncheck the box). For Ch03 (Safety): this
  pattern is worth naming as "in-artifact human override" — the override
  signal lives in the artifact rather than requiring a separate maintenance
  operation. Contrast with `stop-after`, where override requires recompilation.

### Claim 6: Cache-memory cleanup groups cache entries by workflow prefix, keeps the latest run per prefix, and deletes older entries — with rate-limit awareness built in

- **Evidence**: Cache keys follow the pattern `memory-{workflow}-{run-id}`.
  The cleanup job groups by workflow prefix, keeps the latest run ID per group,
  deletes older entries, and pauses early if the GitHub API rate limit is
  running low. Results are summarized in a job summary table (found, kept,
  deleted). Runs automatically on every maintenance workflow execution; also
  triggerable manually via `clean_cache_memories` operation.
- **Confidence**: settled (first-party documentation; key pattern is specified)
- **Quote**: "The cleanup job groups caches by workflow prefix, keeps the latest
  run ID per group, and deletes older entries. This prevents cache storage from
  growing unboundedly as workflows run repeatedly."
- **Our assessment**: The "keep latest, delete older" strategy is the correct
  default for agent memory caches: you want the most recent state, and older
  states are obsolete. The rate-limit awareness is a production-quality detail
  — a cleanup job that burns through your GitHub API quota is worse than no
  cleanup. The key pattern (`memory-{workflow}-{run-id}`) is useful for
  practitioners implementing their own cache-memory patterns on similar platforms.
  For Ch07 (Cost Management): unbounded cache growth is a silent cost driver in
  long-running agentic systems; schedule regular cleanup as a hygiene practice.

### Claim 7: Manual maintenance operations are role-gated to admin and maintainer roles, with nine named operations covering the full harness lifecycle

- **Evidence**: The maintenance workflow exposes these operations via
  `workflow_dispatch`: `disable`, `enable`, `update`, `upgrade`, `safe_outputs`,
  `create_labels`, `clean_cache_memories`, `validate`, `activity_report`. All
  are "restricted to admin and maintainer roles and are not available on forks."
  Destructive operations (`disable`, `enable`, `upgrade`) are distinct from
  informational ones (`validate`, `activity_report`).
- **Confidence**: settled (first-party documentation; operations table is enumerated)
- **Quote**: "All operations are restricted to admin and maintainer roles and
  are not available on forks."
- **Our assessment**: The role-gating on destructive operations is the correct
  safety design for a shared harness maintenance workflow. The fork exclusion
  is important — it prevents contributors from triggering destructive operations
  on the main repo via fork-based PRs. The nine-operation taxonomy is a useful
  model for any agentic harness that has graduated beyond single-workflow setups:
  as the harness scales, you need dedicated tooling for bulk operations. For
  Ch09 (Agent Orchestration): `disable` / `enable` as emergency kill switches
  for the entire agent factory is a pattern worth documenting for incident
  response.

### Claim 8: The `update` and `upgrade` operations open PRs for review rather than making changes directly, preserving the human review gate

- **Evidence**: "Runs `gh aw update` or `gh aw upgrade`, stages changed files,
  and opens a pull request for review. After merging, recompile lock files with
  `gh aw compile`." The PR-for-review pattern means that even administrative
  updates go through human review before taking effect.
- **Confidence**: settled (first-party documentation)
- **Quote**: "opens a pull request for review"
- **Our assessment**: This is consistent with the broader gh-aw pattern of using
  PRs as the human oversight gate for consequential agent actions (see
  `blog-gh-aw-operations-release-workflows.md` Claim 6 — 22% PR rejection rate
  means humans are active participants, not rubber stamps). The `update` and
  `upgrade` operations apply the same gate to the harness itself — the tooling
  that manages agents is managed by the same review process as everything else.
  This prevents the maintenance workflow from becoming a backdoor for bypassing
  review. For Ch03 (Safety): the PR-for-review gate on maintenance operations
  is an example of the "human approval for critical actions" pattern (from
  `docs-ghaw-how-they-work.md` Claim 10) applied to the harness lifecycle itself.

### Claim 9: `action_failure_issue_expires` makes the harness self-healing — failure issues auto-expire after 168 hours (7 days) by default

- **Evidence**: The `aw.json` maintenance configuration includes
  `action_failure_issue_expires: 72` (configurable, in hours; default 168).
  Controls expiration for "failure issues opened by the conclusion job (including
  grouped parent issues when `group-reports: true`)."
- **Confidence**: settled (first-party documentation; specific config field and
  default value documented)
- **Quote**: "The `action_failure_issue_expires` field controls expiration (in
  hours) for failure issues opened by the conclusion job."
- **Our assessment**: Auto-expiring failure issues solves a real noise problem:
  a transient failure opens an issue; the failure clears; but the issue lingers
  indefinitely and creates false signal in repository health dashboards. The
  self-healing property (the harness resolves its own failure issues when they
  age out) is notable because it removes a manual triage task. The 168-hour
  default (7 days) is a reasonable window for human acknowledgment before
  auto-close. For Ch07: recommend `action_failure_issue_expires` as a
  standard config entry for any gh-aw deployment to prevent failure issue
  accumulation.

### Claim 10: The `validate` operation runs all linters (`--zizmor`, `--actionlint`, `--poutine`) and files or updates an issue with findings — making validation a persistent signal rather than a transient CI output

- **Evidence**: "Runs `gh aw compile --validate --no-emit --zizmor --actionlint
  --poutine --verbose`. If errors or warnings are found, creates or updates a
  GitHub issue titled `[aw] workflow validation findings` with the full output."
  The "creates or updates" phrasing means the issue is maintained as a living
  record of validation state, not re-created on each run.
- **Confidence**: settled (first-party documentation; CLI flags and issue title
  are specific)
- **Quote**: "creates or updates a GitHub issue titled `[aw] workflow validation
  findings` with the full output"
- **Our assessment**: Surfacing validation findings as a persistent issue (rather
  than only in CI logs) is an observability design pattern: it makes workflow
  health visible to anyone watching the repository, not just engineers who read
  CI output. The "create or update" behavior means the issue reflects current
  state — it is updated when findings change, rather than accumulating stale
  findings across runs. For Ch07 (Observability): this pattern is transferable
  to any agent factory — surface health findings as repository artifacts, not
  just log lines.

### Claim 11: The `activity_report` operation generates a 24h/7d/30d run summary with collapsible sections, and skips the 30-day query when rate-limited

- **Evidence**: "Runs `gh aw logs --format markdown` for the last 24 hours,
  7 days, and 30 days (up to 1000 runs each), then creates an issue titled
  `[aw] agentic status report` with all three time-range sections as collapsible
  `<details>` blocks. Downloaded logs are cached under `./.cache/gh-aw/activity-report-logs`.
  The job has a 2-hour timeout and skips the 30-day query when the GitHub API
  is rate-limited."
- **Confidence**: settled (first-party documentation; time ranges, issue title,
  caching path, and timeout are specific)
- **Quote**: "creates an issue titled `[aw] agentic status report`"
- **Our assessment**: The three-horizon report (24h, 7d, 30d) is a useful
  pattern for distinguishing noise (24h) from trend (30d). The rate-limit
  fallback (skip 30-day rather than fail) is a graceful degradation that
  preserves partial value when the API is constrained. The 2-hour job timeout
  is a cost bound on the operation itself. For Ch07 (Observability): the
  collapsible `<details>` blocks within a GitHub issue is a UX pattern for
  surfacing structured data in a low-noise format — worth noting as a UI
  pattern for agent-generated reports.

### Claim 12: The SideRepoOps pattern isolates automation from the main repository by running workflows in a dedicated side repo targeting the main repo via PAT

- **Evidence**: The page references SideRepoOps as an isolation pattern without
  fully documenting it; additional documentation from sub-pages establishes:
  the side repo runs workflows with `mode: remote` in the tools config, uses
  a PAT with specific scopes (Contents: Read, Issues: Read+Write, Pull Requests:
  Read+Write, Metadata: Read), and targets the main repo via `safe-outputs.github-token`
  and `target-repo` fields.
- **Confidence**: emerging (referenced on this page; full documentation on a
  linked sub-page; the pattern itself is settled for the platform)
- **Quote**: "SideRepoOps pattern referenced for isolation"
- **Our assessment**: SideRepoOps is a significant isolation technique for
  high-volume or high-noise agentic automation. By running workflows from a
  dedicated repo, the main repository's Actions tab, workflow history, and
  billing surface stay clean — all automation overhead appears in the side
  repo. The PAT scope list (Contents: Read, Issues/PRs: Read+Write) is the
  minimal viable permission set for a side repo writing issues and PRs to the
  main repo. For Ch09 (Agent Orchestration): recommend SideRepoOps when
  agentic automation volume would otherwise pollute the main repo's timeline
  or confuse human contributors.

## Concrete Artifacts

### `stop-after` — Workflow Deadline Frontmatter

```yaml
# Example from documentation: weekly workflow with 25-hour deadline
on: weekly on monday
stop-after: "+25h"  # 25 hours from compilation time

# Accepted absolute formats:
# YYYY-MM-DD, MM/DD/YYYY, DD/MM/YYYY
# January 2 2006, 1st June 2025
# ISO 8601

# Accepted relative formats:
# +7d, +25h, +1d12h30m  (minimum unit: hours; +30m alone is NOT valid)

# To reset the stop time on recompile:
# gh aw compile --refresh-stop-time
```
*Source: gh-aw Ephemerals documentation, "Workflow Stop-After" section*

### Safe Output Expiration — YAML Patterns

```yaml
# Issue expiration (7 days)
safe-outputs:
  create-issue:
    expires: 7
    labels: [automation, agentic]

# Discussion expiration (3 days, closes as "OUTDATED")
safe-outputs:
  create-discussion:
    expires: 3
    category: "general"

# Pull request expiration (14 days, same-repo only)
safe-outputs:
  create-pull-request:
    expires: 14
    draft: true

# Supported formats for `expires`:
# Integer: number of days (e.g., 7 = 7 days)
# Relative: 2h, 7d, 2w, 1m, 1y
# Note: hours < 24 are treated as 1 day minimum
```
*Source: gh-aw Ephemerals documentation, "Safe Output Expiration" section*

### Expiration Marker Format (as embedded in issue/discussion body)

```markdown
- [x] expires <!-- gh-aw-expires: 2026-01-14T15:30:00.000Z --> on Jan 14, 2026, 3:30 PM UTC
```

Maintenance workflow closes items where this checkbox is checked AND the
timestamp is in the past. Uncheck the checkbox to prevent automatic expiration.

*Source: gh-aw Ephemerals documentation, "Expiration markers" section*

### Maintenance Frequency Algorithm

```
Shortest expiration across all workflows → generated maintenance schedule:

≤ 1 day    → Every 2 hours
2 days     → Every 6 hours
3–4 days   → Every 12 hours
5+ days    → Daily

The agentics-maintenance.yml workflow is auto-generated by the compiler.
```
*Source: gh-aw Ephemerals documentation, maintenance frequency table*

### Cache-Memory Key Pattern and Cleanup Strategy

```
Cache key format:  memory-{workflow}-{run-id}
Cleanup strategy:
  1. List all caches with "memory-" prefix
  2. Group by {workflow} prefix
  3. Keep the latest {run-id} per group
  4. Delete all older entries
  5. Pause if GitHub API rate limit is running low
  6. Emit job summary: found / kept / deleted counts

Manual trigger:    clean_cache_memories (workflow_dispatch)
Automatic:         Every maintenance workflow run
```
*Source: gh-aw Ephemerals documentation, "Cache-Memory Cleanup" section*

### Manual Maintenance Operations Table

```
Operation             Description
---------             -----------
disable               Disable ALL agentic workflows in the repository
enable                Re-enable all agentic workflows
update                Recompile and open PR if files changed
upgrade               Upgrade to latest version and open PR if changed
safe_outputs          Replay safe outputs from a specific run (run URL or ID)
create_labels         Create missing repository labels from safe-outputs config
clean_cache_memories  Clean up outdated cache-memory entries
validate              Run all linters; file/update issue with findings
activity_report       Generate 24h/7d/30d report and create issue

Access: admin and maintainer roles only. Not available on forks.
```
*Source: gh-aw Ephemerals documentation, "Manual Maintenance Operations" section*

### Maintenance Configuration (aw.json)

```json
{
  "maintenance": {
    "runs_on": "ubuntu-latest",
    "action_failure_issue_expires": 72
  }
}
```

- `runs_on`: String or array for multi-label runners (default: `ubuntu-slim`)
- `action_failure_issue_expires`: Hours until failure issues auto-close
  (default: 168 hours / 7 days)
- File location: `.github/workflows/aw.json`

*Source: gh-aw Ephemerals documentation, "Maintenance Configuration" section*

### SideRepoOps Workflow Config Pattern

```yaml
# In side repository's workflow frontmatter:
tools:
  github:
    mode: remote
    toolsets: [repos, issues, pull_requests]

safe-outputs:
  github-token: ${{ secrets.GH_AW_MAIN_REPO_TOKEN }}
  create-issue:
    target-repo: "my-org/main-repo"

# Required PAT scopes:
# Contents: Read
# Issues: Read + Write
# Pull Requests: Read + Write
# Metadata: Read
```
*Source: gh-aw SideRepoOps documentation (sub-page from Ephemerals)*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 5 (Safe Outputs as pre-approved GitHub
    operations the AI can request without write permissions): this page provides
    the concrete `expires:` configuration that makes Safe Outputs time-bounded.
    The base permission-separation model in `docs-ghaw-how-they-work.md` is
    extended here with expiration semantics.
  - `docs-ghaw-how-they-work.md` Claim 10 (critical actions can require human
    approval): this page's `update`/`upgrade` operations opening PRs for review
    before applying changes is a concrete instance of that pattern applied to
    harness maintenance operations.
  - `blog-gh-aw-operations-release-workflows.md` Claim 6 (22% PR rejection rate
    — humans actively review agent PRs): the PR-for-review gate on `update` and
    `upgrade` operations is the same human oversight mechanism applied to the
    maintenance workflow itself.
  - `blog-ghaw-weekly-2026-03-30.md` (integrity-aware cache-memory via git
    branches): that note documents the v0.64.3 storage backend for cache-memory;
    this page documents the cleanup lifecycle. Together they give the full
    cache-memory picture: git branches as storage, maintenance workflow as GC.

- **Extends**:
  - `docs-ghaw-how-they-work.md`: this page is the resource lifecycle companion
    to the conceptual architecture page. That page covers the security model
    and Safe Outputs permission design; this page covers the time dimension —
    how resources expire, how costs are bounded, how the harness self-maintains.
  - `blog-ghaw-weekly-2026-03-23.md` (safe-outputs.actions for exposing GitHub
    Actions as MCP tools): this page adds the `expires:` config to the safe
    outputs model; those two dimensions — tool extensibility and time-bounding —
    combine for complete safe output specification.
  - `docs-ghaw-agent-factory-status.md` and `docs-ghaw-audit-with-agents.md`
    (observability patterns): this page's `activity_report` and `validate`
    operations extend the observability model with maintenance-layer visibility.

- **Contradicts**: None identified. The expiration and cost-control patterns
  here do not conflict with any existing source note claims.

- **Novel**:
  - **`stop-after` deadline enforcement** (Claims 1–2): No other source in the
    corpus documents this cost-control primitive. Completely new to the corpus.
  - **Safe output expiration with `expires:` config** (Claim 3): Prior notes
    knew Safe Outputs existed as a permission pattern, but had zero visibility
    into the expiration dimension. The specific YAML patterns are new.
  - **Maintenance frequency derivation algorithm** (Claim 4): The compiler-derived
    schedule based on shortest expiration is a novel harness design pattern.
  - **Checkbox uncheck-to-prevent-expiry UX** (Claim 5): In-artifact human
    override mechanism is new to the corpus.
  - **Cache-memory cleanup strategy and key pattern** (Claim 6): The
    memory-{workflow}-{run-id} key format and keep-latest-per-prefix cleanup
    are new (the storage backend was covered in weekly notes, not the lifecycle).
  - **Nine-operation maintenance suite with role-gating** (Claim 7): Complete
    maintenance operations taxonomy is new to the corpus.
  - **`action_failure_issue_expires` self-healing config** (Claim 9): No prior
    source documents this pattern.
  - **SideRepoOps isolation pattern** (Claim 12): Referenced in triage as novel;
    not covered in any existing source note.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add `stop-after` as a mandatory harness field for bounded workflows** (Claims
  1–2): Any workflow deployed for a trial, experiment, or time-bounded initiative
  should carry a `stop-after:` declaration in its frontmatter. Recommend the
  `+Nd` relative format for experiments (deploy with a short deadline, extend
  only on validation). Note that `--refresh-stop-time` must be explicit — the
  stop time does not reset on routine recompile. This is a cost-safety property.

- **Add `expires:` as the standard config for periodic safe outputs** (Claim 3):
  The `create-discussion` + `expires: 14` + `close-older-discussions: true`
  combination is the canonical harness pattern for weekly/periodic agent
  announcements. It gives the agent a write-separated output channel that
  self-cleans, preventing stale content accumulation. Cite this source for the
  YAML schema.

- **Config surface minimization via compiler-derived maintenance frequency**
  (Claim 4): Use this as an example of the principle "the toolchain should
  derive operational parameters from the spec, not require a separate
  operational config." The maintenance schedule is a function of the expiration
  config, so it should not be a separate setting.

- **SideRepoOps for high-volume automation** (Claim 12): Add as a recommended
  isolation pattern when agentic automation volume would pollute the main
  repo's timeline. Document the PAT scope list as the minimal viable permission
  set.

### Chapter 03: Safety and Verification

- **Auto-expiry as a safety mechanism** (Claim 3): Add to Ch03's discussion of
  output safety: ephemeral safe outputs that auto-close reduce the risk of
  stale agent-generated content persisting and misleading future readers or
  downstream processes. The `expires:` config is the mechanism; the checkbox
  override (Claim 5) is the human gate.

- **In-artifact human override pattern** (Claim 5): Name and document the
  checkbox-based override mechanism as "in-artifact human override" — the
  override signal lives in the artifact itself, making it visible and
  zero-friction. Contrast with `stop-after` (which requires recompilation)
  as two different granularities of human override: per-artifact (checkbox)
  vs. per-workflow (recompile).

- **Role-gating on destructive maintenance operations** (Claim 7): Add the
  admin/maintainer-only gate on `disable`, `enable`, and `upgrade` as a
  model for harness access control. The fork exclusion is a specific security
  property worth naming: contributors cannot trigger destructive operations
  via fork-based PRs.

### Chapter 07: Cost Management and Observability

- **`stop-after` for cost control** (Claims 1–2): The primary cost-control
  recommendation for bounded workflows. Pair with `gh aw logs` (from
  `docs-ghaw-how-they-work.md` Claim 11) as the monitoring companion.

- **Cache-memory cleanup as mandatory hygiene** (Claim 6): Unbounded cache
  growth is a silent cost driver. The memory-{workflow}-{run-id} key pattern
  and keep-latest-per-prefix cleanup strategy are transferable to any
  platform with similar caching patterns.

- **`action_failure_issue_expires` to prevent failure issue accumulation**
  (Claim 9): Recommend as a standard `aw.json` entry. The self-healing
  property (harness resolves its own stale failure issues) removes a manual
  triage burden.

- **`validate` and `activity_report` as observability primitives** (Claims
  10–11): Surface workflow health as persistent GitHub issues rather than
  transient CI logs. The 24h/7d/30d activity report is a pattern for
  distinguishing noise from trend in agent observability.

### Chapter 09: Agent Orchestration Patterns

- **`disable` / `enable` as emergency kill switches** (Claim 7): Document as
  an incident-response pattern — a single `workflow_dispatch` can halt the
  entire agent factory without editing code. Pairs with the role-gating to
  ensure only authorized operators can trigger it.

- **SideRepoOps as an isolation pattern** (Claim 12): When orchestrating a
  multi-repo agentic factory, the SideRepoOps pattern separates the automation
  infrastructure from the product codebase. Document alongside the `mode: remote`
  + PAT setup.

## Extraction Notes

1. **Source is the lifecycle companion to the conceptual overview**: This page
   and `docs-ghaw-how-they-work.md` together form the conceptual documentation
   layer. That page covers architecture and security; this page covers resource
   lifecycle and maintenance. Recommend cross-referencing both in any guide
   section on gh-aw harness design.

2. **SideRepoOps is referenced but not fully documented on the main page**: Full
   SideRepoOps documentation is on a linked sub-page. The details extracted here
   (PAT scopes, `mode: remote`, `target-repo`) came from that sub-page. If a
   dedicated source note for SideRepoOps is warranted, the sub-page URL should
   be the primary source.

3. **No publication date**: The documentation page does not carry an explicit
   publication date. Content is consistent with gh-aw platform behavior as of
   the extraction date (April 2026).

4. **No contradictions filed**: Reviewed all existing source notes. No claims
   in this source materially oppose existing notes. The expiration and lifecycle
   content is entirely new to the corpus.

5. **`close-older-discussions` config**: The triage comments reference this field
   specifically. It appears in the discussion expiration pattern — when set to
   `true`, the maintenance workflow closes older discussion instances when a new
   one is created (keeping the latest). The source page documents `expires: 3`
   for discussions but the specific `close-older-discussions: true` field
   appeared in the second triage comment's description of the pattern rather
   than directly quoted from the page; marked as emerging pending verification
   on a future check.
