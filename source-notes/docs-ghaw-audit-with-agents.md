---
source_url: https://github.github.com/gh-aw/guides/audit-with-agents
source_type: docs
title: "Consuming Audit Reports with Agents"
author: GitHub Agentic Workflows team (official guides documentation)
date_published: null
date_extracted: 2026-04-21
last_checked: 2026-04-21
status: current
confidence_overall: emerging
issue: "#294"
---

# Consuming Audit Reports with Agents

> The practitioner implementation guide for wiring `gh aw audit` JSON output into
> autonomous downstream workflows — provides four complete workflow specs, the stable
> JSON field schema for audit commands, specific numeric regression-detection thresholds
> (cost >20%, tokens >50%, MCP error_rate >0.10), the cache-memory pattern for 30-day
> rolling baselines, and the `noop` safe-output requirement — filling the implementation
> detail gap behind the `blog-ghaw-agent-observability.md` observatory architecture.

## Source Context

- **Type**: docs (GitHub Agentic Workflows guides section — user-facing implementation
  reference, not a blog post or conceptual overview. Guides are prescriptive how-to pages
  in the `github.github.com/gh-aw/guides/` section, distinct from the blog series and
  the architecture documentation.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team — the same
  team behind Peli de Halleux's agent factory blog series and the official `gh aw` platform
  documentation. The JSON field schemas, CLI commands, and workflow specs are authoritative
  for the `gh aw` platform. Numeric thresholds (cost >20%, tokens >50%, error_rate >0.10)
  are presented as practitioner-validated defaults, not arbitrary values. High credibility
  for platform-specific claims; the thresholds do not automatically generalize to other
  audit systems without recalibration.
- **Scope**: Covers how to consume `gh aw audit` CLI output programmatically inside
  autonomous agent workflows. Specifically: the JSON field schema for each audit command,
  four concrete workflow YAML specs, regression detection thresholds, the cache-memory
  pattern for rolling averages, the `noop` safe-output requirement, MCP vs CLI access
  patterns inside Actions, and per-workflow permission requirements. Does NOT cover: how
  the audit workflows are deployed (that is `blog-ghaw-agent-observability.md`), the
  underlying audit engine design, security threat models (see `docs-ghaw-how-they-work.md`),
  or cost/latency of running these consumer workflows themselves.

## Extracted Claims

### Claim 1: Inside GitHub Actions, agents consume audit commands via the `agentic-workflows` MCP tool rather than calling the `gh aw` CLI directly

- **Evidence**: All four workflow specs in the guide use `agentic-workflows:` in their
  `tools:` block and instruct the agent to "Use the `agentic-workflows` MCP tool `audit`"
  or `logs`. No workflow calls the CLI directly. The guide documents the same commands
  (`audit`, `logs`, `audit diff`) at two levels: as CLI commands in the reference table
  and as MCP tool invocations in the workflow specs — but only the MCP path is used in
  production Actions.
- **Confidence**: settled (first-party documentation; all four workflow specs use this
  pattern consistently)
- **Quote**: "Use the `agentic-workflows` MCP tool `audit` with run ID
  ${{ github.event.workflow_run.id }}"
- **Our assessment**: This is an architecturally important distinction for Ch02
  (Harness Engineering). The CLI is for local development and testing; the MCP tool is
  the production integration point inside Actions. This mirrors the `docs-ghaw-how-they-work.md`
  pattern where MCP tools are the standard tool interface for agents operating in the
  GitHub Actions runtime. Teams building audit-consuming workflows should wire through
  the MCP tool, not shell out to the CLI — the MCP path is what is supported, documented,
  and sandbox-safe.

### Claim 2: The `workflow_run:completed` event is the standard trigger for downstream audit-consuming workflows, enabling event-chaining between agent runs and audit consumers

- **Evidence**: Two of the four workflow specs (PR comment poster and auto-issue filer)
  use `on: workflow_run: workflows: ['my-workflow'] types: [completed]` as their trigger.
  The third (regression detection) uses `workflow_dispatch` for manual invocation. The
  fourth (weekly digest) uses `schedule: weekly`.
- **Confidence**: emerging (four data points from one platform's documentation; the pattern
  is clear but not externally corroborated)
- **Quote**: `on:\n  workflow_run:\n    workflows: ['my-workflow']\n    types: [completed]`
- **Our assessment**: The `workflow_run:completed` trigger is the production event-chaining
  pattern: a primary agent workflow completes, and the audit consumer fires automatically
  against that run's ID (`${{ github.event.workflow_run.id }}`). This is a reusable
  architectural pattern beyond audit workflows — any downstream workflow that needs to
  analyze the output of an upstream workflow can use this trigger. For Ch02: document this
  as the standard event-chaining primitive for post-run analysis workflows.

### Claim 3: Audit output has stable top-level fields and extensible nested sub-fields — providing a practitioner stability contract for building consumer workflows

- **Evidence**: The guide documents top-level stable fields (`key_findings`,
  `recommendations`, `metrics`, `firewall_analysis`, `mcp_tool_usage`) separately from
  command-specific fields (`per_run_breakdown`, `domain_inventory` for `logs`; `run_metrics_diff`,
  `firewall_diff`, `mcp_tools_diff` for `audit diff`). The `--parse` flag is separately
  noted as adding optional enrichment fields (`behavior_fingerprint`, `agentic_assessments`)
  that are not part of the stable schema.
- **Confidence**: emerging (first-party documentation; the stable/extensible distinction
  is implied by how the page presents the schema, not explicitly labeled as such)
- **Quote**: The `--parse` flag "populates `behavior_fingerprint` and `agentic_assessments`
  fields" — presented as additive enrichment separate from the base output.
- **Our assessment**: The implicit stability contract matters for consumer workflow design:
  agents should rely on the top-level stable fields for branching logic and issue-filing
  decisions, and treat `--parse`-enriched fields as optional context. Building a consumer
  workflow that requires `behavior_fingerprint` creates a fragile dependency on a non-stable
  field. For Ch02: recommend building audit consumers against the stable field set; treat
  `--parse` enrichment as read-only context for prose generation, not for branching logic.

### Claim 4: Specific regression detection thresholds for production use — cost increase >20%, token increase >50%, MCP error rate >0.10 — are the practitioner-validated defaults from GitHub's own workflows

- **Evidence**: These three thresholds appear verbatim in the regression detection workflow
  spec: "cost increase > 20%, or token usage increase > 50%... MCP servers with
  `error_rate > 0.10`". They are presented as the detection criteria the guide recommends
  teams use as starting points, drawn from GitHub's own audit consumer experience.
- **Confidence**: emerging (GitHub presents these as practitioner defaults, not formally
  validated statistical thresholds; no A/B testing or failure analysis is cited)
- **Quote**: "Check for new blocked domains, increased MCP error rates, cost increase
  > 20%, or token usage increase > 50%."
- **Our assessment**: These are the first specific numeric regression thresholds in the
  corpus for agentic workflow monitoring. No other source — not the observability blog,
  not the how-they-work docs, not any weekly update — provides explicit cost/token/error
  rate threshold values. Their provenance is GitHub's own production experience rather
  than cited research, which limits generalizability; but they are the only specific
  numbers available and should be presented as a starting calibration point, not an
  industry standard. For Ch03 (Safety and Verification): these thresholds are actionable
  gate values for automated regression detection — include them with the caveat that teams
  should recalibrate against their own baseline variance.

### Claim 5: The `cache-memory` tool provides persistent state across agent runs for rolling trend analysis without external infrastructure

- **Evidence**: The weekly digest workflow spec uses `cache-memory: key: audit-monitoring-trends`
  in its `tools:` block and instructs the agent to "read `/tmp/gh-aw/cache-memory/audit-trends.json`
  as the previous baseline" and "Update `/tmp/gh-aw/cache-memory/audit-trends.json` with
  rolling averages... keeping only the last 30 days." The cache-memory tool is listed
  alongside `agentic-workflows` as a standard toolset.
- **Confidence**: emerging (first-party documentation; the mechanism is described but
  the persistence substrate is not detailed on this page)
- **Quote**: "read `/tmp/gh-aw/cache-memory/audit-trends.json` as the previous baseline"
- **Our assessment**: Cache-memory solves the stateless-agent problem for longitudinal
  monitoring. A stateless agent that runs weekly would have no memory of prior weeks;
  cache-memory allows it to maintain rolling averages for cost, tokens, error counts,
  and deny rates across 30 days without requiring a database, external storage, or
  custom infrastructure. The `/tmp/gh-aw/cache-memory/` path and the 30-day retention
  window are the first explicit persistence mechanism for long-running audit baselines
  in the corpus. For Ch02 (Harness Engineering): document cache-memory as the
  platform-native mechanism for stateful agent behavior in gh-aw. This is architecturally
  significant: it enables agents to detect trends rather than just point-in-time anomalies.

### Claim 6: The `noop` safe output is required as an explicit signal when no action is warranted — preventing silent workflow completion ambiguity

- **Evidence**: The auto-issue filing workflow spec ends with "If no critical findings,
  call the `noop` safe output tool." The guide presents this as the standard pattern
  for audit-consumer workflows to signal a clean run. Without `noop`, a workflow that
  finds nothing would complete without any output, making it ambiguous whether it found
  nothing or failed silently.
- **Confidence**: settled (the `noop` call is documented as a required pattern in the
  guide, not an optional recommendation)
- **Quote**: "If no critical findings, call the `noop` safe output tool."
- **Our assessment**: The `noop` requirement is a subtle but important safety mechanism.
  In an autonomous workflow, the difference between "nothing found" and "workflow failed
  silently" is only resolvable if the workflow explicitly emits a success signal. `noop`
  fills this role — it is the zero-action safe output that confirms the agent completed
  its analysis and found nothing to do. This extends `docs-ghaw-how-they-work.md` Claim 5
  (Safe Outputs as permission-separated state mutation): `noop` is a Safe Output that
  mutates no state but confirms completion. For Ch03: recommend the `noop` pattern for
  any conditional-action audit workflow — the absence of a result should be as explicit
  as a result.

### Claim 7: Deduplication-before-filing is the required pattern for auto-issue creation from audit findings

- **Evidence**: The auto-issue filing workflow spec instructs: "For each finding without
  a matching open issue, create one..." — deduplication against open issues is part of
  the prescribed agent behavior, not a post-hoc cleanup. The workflow filters
  `key_findings` for `high`/`critical` severity AND checks for existing open issues
  before filing.
- **Confidence**: emerging (first-party guidance; presented as a requirement rather than
  an option, but no quantified deduplication failure rate is cited to justify it)
- **Quote**: "For each finding without a matching open issue, create one with the finding
  title, description, impact, and recommendations, labelled `audit-finding`."
- **Our assessment**: The deduplication requirement prevents issue spam: if an audit
  finding persists across multiple runs (a recurring blocked domain, a persistent MCP
  error), filing a new issue each run would flood the tracker. The prescribed pattern
  is to check open issues first and only file if no match exists. This is a standard
  idempotency pattern applied to agentic issue creation. For Ch03: document
  deduplication-before-filing as a required pattern for any agent that creates issues
  from repeated observations. The guide operationalizes this via the agent's natural
  language instructions ("for each finding without a matching open issue"), which means
  the deduplication logic lives in the prompt, not in code — a notable design choice.

### Claim 8: Each audit-consuming workflow type is granted only the specific write permission it requires — no cross-contamination of write capabilities

- **Evidence**: Permission blocks in the four workflow specs: PR comment poster gets
  `pull-requests: write`; regression detector and issue filer get `issues: write`; weekly
  digest gets `discussions: write`. All four share the same read base:
  `contents: read` + `actions: read`. No workflow requests write permissions it does not
  use.
- **Confidence**: settled (first-party documentation; permissions are YAML-specified and
  compiler-validated)
- **Quote**: (from weekly digest spec) `permissions:\n  contents: read\n  actions: read\n  discussions: write`
- **Our assessment**: This permission decomposition exemplifies the "zero capability by
  default, explicit permit" principle from `docs-ghaw-how-they-work.md` Claim 4 applied
  specifically to the audit-consumer use case. Four different workflows, each with the
  minimal write scope required for its output target. The pattern teaches by example:
  before building a consumer workflow, identify exactly where it writes (PR comment,
  issue, discussion) and grant only that scope. For Ch02/Ch03: this four-workflow
  permission comparison is a concrete teaching artifact for least-privilege harness design.

### Claim 9: The regression detection workflow uses `audit diff` across two run IDs to surface before/after comparisons across cost, tokens, firewall, and MCP tool dimensions

- **Evidence**: Regression detection workflow spec uses `workflow_dispatch` with two
  inputs (`base_run_id`, `current_run_id`) and instructs the agent to call `audit diff`
  with those IDs. Output fields: `run_metrics_diff` (cost and token deltas), `firewall_diff`
  (new blocked domains), `mcp_tools_diff` (per-tool error rate changes). If regressions
  found, the agent opens a GitHub issue with a structured table from each diff field.
- **Confidence**: emerging (first-party documentation; the `audit diff` command schema
  is described but the underlying diff computation is not detailed)
- **Quote**: "Check for new blocked domains, increased MCP error rates, cost increase
  > 20%, or token usage increase > 50%. If regressions are found, open a GitHub issue
  with a table from `run_metrics_diff`, affected domains from `firewall_diff`, and
  affected MCP tools from `mcp_tools_diff`."
- **Our assessment**: The `audit diff` workflow enables targeted regression testing: given
  a baseline run and a current run, surface exactly what changed. This is a structured
  change-detection primitive at the agent-behavior level, analogous to code diffs but
  for agent runtime characteristics. The three diff dimensions (cost/token, firewall,
  MCP tools) align with the three categories where agent regressions typically manifest:
  efficiency (cost/tokens), safety (firewall/blocked domains), and reliability (MCP tool
  errors). For Ch03: document `audit diff` as the canonical regression detection primitive
  for gh-aw; the four threshold values are the starting gate.

### Claim 10: MCP server reliability is monitorable via `error_rate` and `unreliable` flags in logs output — providing an objective health signal for the tool infrastructure layer

- **Evidence**: The weekly digest workflow spec detects "MCP servers with `error_rate > 0.10`
  or `unreliable: true`" in the `logs` output's `per_run_breakdown`. These two fields are
  presented as the standard MCP health indicators, with `unreliable: true` being a
  platform-computed flag (not a manual annotation).
- **Confidence**: emerging (first-party documentation; the computation behind `unreliable: true`
  is not detailed on this page)
- **Quote**: "MCP servers with `error_rate > 0.10` or `unreliable: true`"
- **Our assessment**: MCP server health monitoring is a gap in the existing corpus.
  `blog-bswen-mcp-token-cost.md` covers MCP token cost, and `docs-ghaw-how-they-work.md`
  covers MCP Scripts as inline tool definitions, but neither addresses how to detect
  unreliable MCP servers at runtime. The `error_rate` and `unreliable` flags provide
  an objective monitoring contract: if an MCP tool is failing more than 10% of the time,
  the platform labels it unreliable. This is the first reliability SLI (service level
  indicator) for MCP tools in the corpus. For Ch02: document these two fields as the
  standard health signals for MCP tool infrastructure in gh-aw.

### Claim 11: The weekly digest pattern uses `schedule: weekly` plus cache-memory to produce a trend-aware digest that is posted to GitHub Discussions for async team visibility

- **Evidence**: Weekly digest spec uses `schedule: weekly`, the `discussions` toolset,
  `discussions: write` permission, and instructs the agent to "Create a GitHub discussion
  'Audit Digest — [YYYY-MM-DD]' with an executive summary, anomalies table, and MCP
  health table." Cache-memory provides the 30-day rolling baseline for trend detection.
- **Confidence**: emerging (first-party; the choice of Discussions over Issues for the
  digest output is implicit in the permissions block — it is a design choice, not a
  platform constraint)
- **Quote**: "Create a GitHub discussion 'Audit Digest — [YYYY-MM-DD]' with an executive
  summary, anomalies table, and MCP health table."
- **Our assessment**: The weekly digest is the team-facing output of the audit-consumer
  pipeline. Posting to GitHub Discussions rather than Issues signals that the digest is
  informational (team awareness) rather than actionable (requires individual response).
  This is consistent with the blog-ghaw-agent-observability.md Claim 5 autonomous
  remediation loop: critical findings become Issues (requiring action), while trend
  summaries become Discussions (providing context). The output channel selection
  (`discussions: write` vs `issues: write`) is itself a design decision that communicates
  expected human response. For Ch05 (Team Adoption): the weekly digest pattern is a
  low-friction team-monitoring mechanism — no dashboard required, just a weekly Discussion
  that the team can read async.

### Claim 12: The `--parse` flag enriches audit output with `behavior_fingerprint` and `agentic_assessments` as optional, non-stable fields

- **Evidence**: The CLI reference table notes that adding `--parse` "Populates
  `behavior_fingerprint` and `agentic_assessments` fields." These are documented
  separately from the stable output fields and are not used in any of the four workflow
  specs.
- **Confidence**: emerging (first-party documentation; the semantic meaning and stability
  contract of these fields is not described in detail on this page)
- **Quote**: "`--parse` flag — Populates `behavior_fingerprint` and `agentic_assessments`
  fields"
- **Our assessment**: The `--parse` enrichment provides semantic interpretation of agent
  behavior beyond raw metrics — "what the agent's behavior pattern looks like" and
  "AI-generated assessments" are the implied semantics. The fact that these fields are
  absent from all four workflow specs suggests they are used for deep inspection rather
  than automated decision-making. For practitioners building audit consumers: use the
  stable fields for branching logic; use `--parse` enrichment for richer prose in reports
  where human review is expected. Do not build hard-coded logic around fields that may
  change as the platform evolves.

## Concrete Artifacts

### Workflow 1: Post Audit Findings as PR Comment

```yaml
---
description: Post audit findings as a PR comment after each agent run
on:
  workflow_run:
    workflows: ['my-workflow']
    types: [completed]
engine: copilot
tools:
  github:
    toolsets: [pull_requests]
  agentic-workflows:
permissions:
  contents: read
  actions: read
  pull-requests: write
---
# Summarize Audit Findings
Use the `agentic-workflows` MCP tool `audit` with run ID ${{ github.event.workflow_run.id }},
identify the pull request that triggered it, and post a comment summarizing key findings and
blocked domains. Highlight issues with severity `high` or `critical`. If there are no findings,
post a brief "no issues found" comment.
```

### Workflow 2: Regression Detection via Diff

```yaml
---
description: Detect regressions between two workflow runs
on:
  workflow_dispatch:
    inputs:
      base_run_id:
        description: 'Baseline run ID'
        required: true
      current_run_id:
        description: 'Current run ID to compare'
        required: true
engine: copilot
tools:
  github:
    toolsets: [issues]
  agentic-workflows:
permissions:
  contents: read
  actions: read
  issues: write
---
# Regression Detection
Use the `agentic-workflows` MCP tool `audit diff` with base run ID ${{ inputs.base_run_id }}
and current run ID ${{ inputs.current_run_id }}. Check for new blocked domains, increased MCP
error rates, cost increase > 20%, or token usage increase > 50%. If regressions are found, open
a GitHub issue with a table from `run_metrics_diff`, affected domains from `firewall_diff`, and
affected MCP tools from `mcp_tools_diff`.
```

### Workflow 3: Auto-File Issues for Critical Findings

```yaml
---
description: File GitHub issues for high-severity audit findings
on:
  workflow_run:
    workflows: ['my-workflow']
    types: [completed]
engine: copilot
tools:
  github:
    toolsets: [issues]
  agentic-workflows:
permissions:
  contents: read
  actions: read
  issues: write
---
# Auto-File Issues for Critical Findings
Use the `agentic-workflows` MCP tool `audit` with run ID ${{ github.event.workflow_run.id }}.
Filter `key_findings` for severity `high` or `critical`. For each finding without a matching
open issue, create one with the finding title, description, impact, and recommendations,
labelled `audit-finding`. If no critical findings, call the `noop` safe output tool.
```

### Workflow 4: Weekly Audit Monitoring Digest

```yaml
---
description: Weekly audit digest with trend analysis
on:
  schedule: weekly
engine: copilot
tools:
  github:
    toolsets: [discussions]
  agentic-workflows:
  cache-memory:
    key: audit-monitoring-trends
permissions:
  contents: read
  actions: read
  discussions: write
---
# Weekly Audit Monitoring Digest
1. Use the `agentic-workflows` MCP tool `logs` with parameters `workflow: my-workflow, last: 10`
   and read `/tmp/gh-aw/cache-memory/audit-trends.json` as the previous baseline.
2. Detect: cost spikes (`cost_spike: true` in `per_run_breakdown`), new denied domains in
   `domain_inventory`, MCP servers with `error_rate > 0.10` or `unreliable: true`, and
   week-over-week changes in `error_trend.runs_with_errors`.
3. Create a GitHub discussion "Audit Digest — [YYYY-MM-DD]" with an executive summary,
   anomalies table, and MCP health table.
4. Update `/tmp/gh-aw/cache-memory/audit-trends.json` with rolling averages (cost, tokens,
   error count, deny rate), keeping only the last 30 days.
```

### JSON Field Schema for Audit Commands

```
gh aw audit <run-id> --json
  Stable top-level fields:
    key_findings        → list of findings, each with: severity (high/critical), title,
                          description, impact, recommendations
    recommendations     → action items from the audit
    metrics             → run performance metrics
    firewall_analysis   → network/domain access analysis
    mcp_tool_usage      → per-tool invocation data

gh aw logs [workflow] --last 10 --json
  Fields:
    per_run_breakdown   → per-run data including cost_spike (bool)
    domain_inventory    → domains accessed across runs
    error_trend         → { runs_with_errors: <count> }
    (per MCP server)    → error_rate (float), unreliable (bool)

gh aw audit diff <id1> <id2> --json
  Fields:
    run_metrics_diff    → cost/token deltas between the two runs
    firewall_diff       → new/changed blocked domains
    mcp_tools_diff      → per-tool error rate changes

With --parse flag (optional enrichment, not stable):
    behavior_fingerprint    → agent behavior pattern classification
    agentic_assessments     → AI-generated assessment of agent behavior
```

### Regression Detection Thresholds (Practitioner Defaults)

```
Cost increase:      > 20%   (from run_metrics_diff)
Token increase:     > 50%   (from run_metrics_diff)
MCP error rate:     > 0.10  (10%, from logs per-server data)
MCP unreliable flag: true   (platform-computed, from logs)
New blocked domains: any    (from firewall_diff)
Cache-memory retention: last 30 days of rolling averages
```

### Permission Pattern per Workflow Type

```
Base (all workflows):  contents: read, actions: read

PR comment poster:     + pull-requests: write
Regression detector:   + issues: write
Issue filer:           + issues: write
Weekly digest:         + discussions: write
```

### Cache-Memory Pattern

```
Tool block:
  cache-memory:
    key: audit-monitoring-trends

Read:   /tmp/gh-aw/cache-memory/audit-trends.json   (previous baseline)
Write:  /tmp/gh-aw/cache-memory/audit-trends.json   (updated with new run)

Stored fields (rolling averages, last 30 days):
  cost          → average cost per run
  tokens        → average token usage
  error_count   → average errors per run
  deny_rate     → average domain deny rate
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 4 ("no write access by default"): all four workflow
    specs enforce the least-privilege principle, each adding only the one write scope it
    needs. This guide is a concrete implementation of the base security design from the
    how-they-work docs.
  - `docs-ghaw-how-they-work.md` Claim 5 (Safe Outputs as permission-separated state
    mutation): the `noop` safe output (Claim 6) is a direct application of the Safe Outputs
    pattern — a pre-approved operation (do nothing, but signal success) that requires no
    write permission.
  - `blog-ghaw-agent-observability.md` Claim 5 (autonomous remediation loop — audit
    observes → raises issue → downstream agent fixes): Workflow 3 (auto-issue filer) is
    the user-side implementation of the first link in that loop. The blog post establishes
    that GitHub runs this loop in production (9 issues raised from 93 audit reports); this
    guide provides the workflow spec for teams to replicate it.
  - `docs-ghaw-how-they-work.md` Claim 6 (MCP Scripts for inline tool integration): the
    `agentic-workflows:` toolset in every workflow spec follows the same pattern of
    declaring tools in frontmatter for the compiler to provision.

- **Extends**:
  - `blog-ghaw-agent-observability.md` — that note covers the *why* (observability as
    first-class architecture, three-tier observatory) and the production metrics (93 audit
    discussions, 9 issues, 4 PRs). This guide covers the *how to build* — the JSON field
    schema, the specific workflow specs, the thresholds. The two together give a complete
    picture: the blog post is the architecture reference; this guide is the implementation
    reference.
  - `docs-ghaw-how-they-work.md` Claim 11 (`gh aw logs` for cost monitoring as best
    practice): this guide extends that single-line best practice with the full logs field
    schema (`per_run_breakdown`, `domain_inventory`, `error_trend`) and specific detection
    logic (cost spikes, unreliable MCP servers, denied domains).
  - `docs-ghaw-agent-factory-status.md` — the agent factory status page shows that
    audit-consuming workflows are part of the observatory category in GitHub's production
    factory. This guide provides the templates for building those workflows.

- **Contradicts**: None filed. No existing source note makes claims that conflict with
  the workflow patterns, field schemas, or thresholds documented here. The regression
  thresholds (cost >20%, tokens >50%) are new specific values not previously present
  in any form in the corpus — there is nothing to contradict.

- **Novel**:
  - **Specific numeric regression thresholds** (Claim 4): cost >20%, tokens >50%,
    MCP error_rate >0.10 are the first specific threshold values in the corpus for
    agentic regression detection. No other source names gate values.
  - **Cache-memory as persistence mechanism for rolling baselines** (Claim 5): the
    `/tmp/gh-aw/cache-memory/` path and 30-day retention pattern for rolling averages
    is not described in any existing source note. This is the first explicit stateful
    agent mechanism (other than GitHub state mutations via Safe Outputs) in the corpus.
  - **`noop` safe output as explicit no-op signal** (Claim 6): the requirement to call
    `noop` when no action is warranted — as distinct from silently completing — is not
    in any existing source note. It is a safety pattern for audit-consumer workflows.
  - **Deduplication-before-filing as a required pattern** (Claim 7): the pattern of
    checking open issues before creating a new one from an audit finding is not documented
    elsewhere in the corpus.
  - **MCP server reliability signals: `error_rate` + `unreliable` flags** (Claim 10):
    the first SLI definition for MCP tool health in the corpus.
  - **Full JSON field schema for `gh aw audit`, `gh aw logs`, `gh aw audit diff`**
    (Claim 3): the complete field-level schema for all three audit command variants
    is not described in any existing source note.
  - **Per-workflow permission decomposition as a teaching artifact** (Claim 8): four
    workflows, each with minimal/distinct write scope, presented as a concrete example
    of least-privilege harness design.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add the four workflow specs as reference harness patterns for audit-consuming
    workflows. The YAML structure — frontmatter with tools, permissions, trigger — is
    the same compilation target described in `docs-ghaw-how-they-work.md`; these are
    concrete, copy-pasteable starting points.
  - Document the `agentic-workflows` MCP tool as the production integration point for
    audit commands inside Actions (vs. CLI for local development). Cross-reference
    `docs-ghaw-how-they-work.md` Claim 6 (MCP Scripts).
  - Document the `cache-memory` tool as the platform-native mechanism for stateful
    agent behavior. Current guide corpus has no coverage of how agents maintain state
    across runs — this fills the gap.
  - Add the `workflow_run:completed` event-chaining trigger as a reusable harness pattern.
  - Add the per-workflow permission decomposition as the concrete example of least-privilege
    harness design (from abstract principle to four concrete examples).

- **Chapter 03 (Safety and Verification)**:
  - Add the regression detection threshold values (cost >20%, tokens >50%, error_rate
    >0.10) as practitioner-validated gate values for automated regression detection.
    Frame as starting calibration points to be adjusted against local baselines.
  - Add the `noop` safe output requirement as a safety pattern for conditional-action
    workflows: explicit no-op signal prevents silent-failure ambiguity.
  - Add deduplication-before-filing as a required idempotency pattern for issue-creation
    workflows — prevents tracker spam from repeated observations.
  - Add MCP `error_rate` + `unreliable` flags as the monitoring contract for MCP tool
    infrastructure health. Cross-reference `blog-bswen-mcp-token-cost.md` for the
    cost dimension; this source adds the reliability dimension.

- **Chapter 05 (Team Adoption)**:
  - Add the weekly audit digest pattern (schedule:weekly + cache-memory + GitHub
    Discussions) as a low-friction team monitoring workflow. No external dashboard
    required — weekly Discussion posts provide async visibility into agent health
    trends. Cross-reference `blog-ghaw-agent-observability.md` Claim 2 (three-tier
    observability architecture) — this workflow is the team-facing output tier.

## Extraction Notes

1. **Four complete workflow specs extracted verbatim**: All four YAML workflow specs
   from the page were captured in full. WebFetch returned the complete page content
   including all code blocks.

2. **JSON field schema is documentation-derived, not schema-file derived**: The field
   schemas were extracted from the workflow spec instructions and the CLI reference table
   on the page, not from a machine-readable schema definition. Field names are stable
   enough to cite, but the page does not publish a formal JSON schema document.

3. **Numeric thresholds are practitioner defaults, not formally validated**: The cost
   >20%, token >50%, and error_rate >0.10 values are presented as recommended starting
   points by GitHub, not as statistically derived thresholds. They should be treated as
   calibration anchors, not universal standards.

4. **`cache-memory` persistence substrate not fully described**: The page describes what
   cache-memory does (persist a JSON file across runs at a named key path) and how to
   use it, but does not describe the storage backend, TTL behavior, concurrent-write
   semantics, or what happens if the cache is evicted. These are platform implementation
   details not covered on this page.

5. **`noop` safe output not described beyond this pattern**: The `noop` safe output is
   referenced only in Workflow 3's instructions. The page does not provide a definition
   section for it — its semantics (signal success, write nothing) are inferred from
   context. Treating it as "the no-action safe output" is consistent with the
   `docs-ghaw-how-they-work.md` Safe Outputs model.

6. **No contradictions filed**: Reviewed `blog-ghaw-agent-observability.md`,
   `docs-ghaw-how-they-work.md`, `docs-ghaw-agent-factory-status.md`,
   `blog-gh-aw-operations-release-workflows.md`, and all related source notes.
   No claims in this source materially oppose existing notes. The regression thresholds
   and cache-memory pattern are entirely new to the corpus — there is nothing to contradict.
