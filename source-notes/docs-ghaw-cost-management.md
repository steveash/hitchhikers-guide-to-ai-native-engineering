---
source_url: https://github.github.com/gh-aw/reference/cost-management
source_type: docs
title: "GitHub Agentic Workflows: Cost Management Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: emerging
issue: "#375"
---

# GitHub Agentic Workflows: Cost Management Reference

> The practitioner-facing cost reference for gh-aw: breaks down the two billing
> components (Actions minutes + inference), provides a trigger-type risk taxonomy
> with cost-reduction strategies for each, documents `gh aw logs` and `gh aw audit`
> as the monitoring commands, gives common scenario estimates, and introduces the
> Agentic Cost Optimization pattern — a meta-agent that uses the `agentic-workflows`
> MCP tool to automatically propose cost-reducing frontmatter changes for expensive
> workflows via pull request.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/cost-management` page
  — in the "Reference" section alongside `reference/rate-limiting-controls`,
  `reference/concurrency`, and `reference/permissions`. Reference pages document
  platform behavior precisely; this one is the practitioner guide to understanding
  and controlling gh-aw spending.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's "Agent Factory" blog series and the `gh aw`
  CLI. Cost component definitions, YAML field names, CLI command syntax, and
  scenario estimates are authoritative for the `gh aw` platform. Scenario cost
  estimates ("~1 Actions minute/month", "4–8 premium requests") are examples,
  not guarantees — actual costs vary by model, context size, and task complexity.
- **Scope**: Covers the two billing components, how to monitor costs with `gh aw
  logs` and `gh aw audit`, a trigger-type risk taxonomy, five cost-reduction
  strategies (with YAML examples), common scenario estimates, and the Agentic
  Cost Optimization meta-agent pattern. Does NOT cover: the Effective Tokens (ET)
  metric specification (see `docs-ghaw-effective-tokens-specification.md`), the
  full rate-limiting controls taxonomy (see `docs-ghaw-rate-limiting-controls.md`),
  or the reference implementation of the monitoring meta-agent
  (see `docs-ghaw-agentic-ops.md`).

## Extracted Claims

### Claim 1: The cost of running a gh-aw workflow is the sum of two components — GitHub Actions compute minutes and AI inference charges from the provider

- **Evidence**: Opening statement of the cost-components section, confirmed across
  multiple fetch passes.
- **Confidence**: settled (first-party documentation; the two-component breakdown
  is the foundational definition for the entire reference page)
- **Quote**: "The cost of running an agentic workflow is the sum of two components:
  **GitHub Actions minutes** consumed by the workflow jobs, and **inference costs**
  charged by the AI provider."
- **Our assessment**: The two-component framing is important for practitioners
  budgeting gh-aw deployments. Actions minutes and inference costs have separate
  pricing mechanisms and separate reduction strategies. A workflow that runs 1
  minute but makes many LLM calls is dominated by inference cost; a workflow that
  runs 10 minutes with a light LLM is dominated by compute cost. The guide should
  present the two components as independently manageable — not a single "cost"
  number. For Ch02 (Harness Engineering): establish the two-component cost model
  upfront so practitioners know which lever to pull.

### Claim 2: Every gh-aw workflow run incurs a predictable structural overhead of approximately 1.5 minutes of runner setup per job, in addition to execution time for a pre-activation job (10–30 seconds) and an agent job (1–15 minutes)

- **Evidence**: The "GitHub Actions Minutes" subsection documents typical job
  durations in a table and states the per-job overhead explicitly.
- **Confidence**: settled (first-party documentation; specific timing values are
  platform specifications)
- **Quote**: "Each job also incurs approximately 1.5 minutes of runner setup
  overhead on top of its execution time."
- **Our assessment**: The structural overhead has two implications. First, the
  minimum cost of any gh-aw run is approximately 3 minutes of Actions time even
  for the fastest possible task (two jobs × 1.5 min overhead each, with near-zero
  execution time). Second, the `skip-if-match` condition (Claim 5) that cancels
  the workflow before the agent job starts still incurs the pre-activation job
  cost (~1.5 min overhead + 10–30 seconds of execution) — it does not reduce cost
  to zero. For Ch02: practitioners sizing their monthly Actions budget must account
  for the per-job overhead, not just execution time.

### Claim 3: Inference billing model differs by AI engine — Copilot charges premium requests to the account owning the token; Claude and OpenAI charge based on token usage to their respective accounts

- **Evidence**: The "Inference Costs" subsection enumerates engine-specific billing
  models.
- **Confidence**: settled (first-party documentation; billing model per engine is
  a platform specification)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The engine-specific billing model has practical implications
  for account setup and cost attribution. Copilot-powered workflows bill against
  the GitHub Copilot subscription tied to the token, making costs invisible in
  standard AI billing dashboards (they appear in the GitHub organization billing
  page instead). Claude and OpenAI workflows bill against the Anthropic and OpenAI
  accounts respectively, giving practitioners standard token-based billing visibility.
  For Ch02: document the billing separation so teams know where to look for cost
  reports depending on which engine they use.

### Claim 4: `gh aw logs` is the primary cost-monitoring command — it shows per-run metrics including duration and estimated inference cost; `gh aw audit <run-id>` provides a detailed per-run breakdown of token usage and tool calls

- **Evidence**: The "Monitoring Costs with `gh aw logs`" section describes both
  commands and their scopes.
- **Confidence**: settled (first-party documentation; CLI command names and behavior
  are authoritative)
- **Quote**: (no direct prose quote; see CLI examples in Concrete Artifacts)
- **Our assessment**: The two-command monitoring pair creates a two-tier visibility
  model: `gh aw logs` for fleet-level trend monitoring (multiple workflows, multiple
  runs) and `gh aw audit <run-id>` for per-run forensic analysis. This maps to
  the two-tier observability model in the reference implementation documented in
  `docs-ghaw-agentic-ops.md` — where the `copilot-token-audit` workflow uses
  `gh aw logs --engine copilot --start-date -1d --json -c 100` to download the
  fleet-level daily snapshot. The `gh aw audit` command provides the deeper
  inspection path documented in `docs-ghaw-audit-with-agents.md`. For Ch02: present
  `gh aw logs` as the first-line cost check and `gh aw audit <run-id>` as the
  drill-down path.

### Claim 5: Using `skip-if-match` conditions to cancel the workflow before the agent job starts is the highest-leverage cost-reduction strategy — it avoids the inference cost entirely while incurring only the pre-activation job cost

- **Evidence**: The "Use Deterministic Checks to Skip the Agent" subsection describes
  this as the first and primary cost-reduction strategy.
- **Confidence**: settled (first-party documentation; the mechanism is a platform
  feature with documented behavior)
- **Quote**: (no direct prose quote; the mechanism is described via YAML example —
  see Concrete Artifacts)
- **Our assessment**: `skip-if-match` is categorically different from all other
  cost-reduction strategies because it eliminates the inference cost entirely for
  qualifying runs. Model selection (Claim 6), context limiting (Claim 7), and rate
  limiting (Claim 8) reduce cost per run; `skip-if-match` reduces cost to near-zero
  for the filtered run subset. The ordering of strategies in the source reflects
  this: deterministic filtering is presented before all other cost controls. For
  Ch02: when documenting cost controls, lead with `skip-if-match` as the highest-ROI
  mechanism — every condition that can be evaluated without an LLM call should be
  expressed as a `skip-if-match` condition. Cross-reference
  `docs-ghaw-deterministic-agentic-patterns.md` for the full taxonomy of deterministic
  pre-checks.

### Claim 6: Choosing a cheaper model for routine tasks is the second-highest-leverage cost reduction — the source explicitly names `gpt-4.1-mini` and `claude-haiku-4-5` as the lighter-model options

- **Evidence**: The "Choose a Cheaper Model" subsection names specific models with
  YAML configuration examples.
- **Confidence**: settled (first-party documentation; model names and YAML field
  syntax are authoritative)
- **Quote**: (no direct prose quote; model names appear in YAML configuration —
  see Concrete Artifacts)
- **Our assessment**: The explicit naming of `gpt-4.1-mini` and `claude-haiku-4-5`
  as cost-optimized options is the most concrete model-selection guidance in the
  corpus for gh-aw practitioners. The source positions model selection as a
  workflow-level decision (in the frontmatter `engine` block), not a per-run
  decision — meaning the cheaper model is a design-time choice for "routine"
  workflows, not a dynamic optimization. For Ch02: document the two named lighter
  models as the first candidates to evaluate when a workflow's task does not require
  frontier-model reasoning capability.

### Claim 7: Context limiting — writing focused prompts and restricting tool result counts — reduces inference cost by reducing the token volume processed per run

- **Evidence**: The "Limit Context Size" subsection describes this strategy.
- **Confidence**: settled (first-party documentation; the causal mechanism is
  well-understood: fewer tokens = lower inference cost)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Context limiting is the fine-grained complement to model
  selection. Where model selection changes the per-token cost, context limiting
  reduces the number of tokens processed. The source frames this as both a prompt
  discipline (focused prompts) and a configuration discipline (restrict tool result
  counts). This connects to the five token-efficiency anti-patterns in
  `docs-ghaw-agentic-ops.md` Claim 11 (batching independent reads, chaining bash
  commands, preferring typed tools) — all of which are specific techniques for
  limiting context growth. For Ch02: present context limiting as the day-two
  optimization once `skip-if-match` and model selection are applied.

### Claim 8: Per-user rate limiting via the `user-rate-limit` frontmatter field caps the number of workflow runs per user per time window, providing a cost control against high-frequency event-driven triggers

- **Evidence**: The "Rate Limiting and Concurrency" subsection documents the
  `user-rate-limit` field with a YAML example.
- **Confidence**: settled (first-party documentation; field name and syntax are
  authoritative)
- **Quote**: (no direct prose quote; see YAML example in Concrete Artifacts)
- **Our assessment**: The `user-rate-limit` field name in this page differs from
  the `rate-limit` field name documented in `docs-ghaw-rate-limiting-controls.md`
  Claim 8 — this may be an alias, an older field name, or a documentation
  inconsistency; both sources use `max-runs-per-window` and `window` as subfields
  with matching semantics. The cost-control framing here positions rate limiting
  as a budget tool alongside the security/anti-abuse framing in the rate-limiting
  reference. Both framings are valid. For Ch02: document rate limiting as both a
  cost control (this source) and an anti-abuse mechanism
  (`docs-ghaw-rate-limiting-controls.md`).

### Claim 9: Trigger types carry inherently different cost risk — push, check_run, and check_suite are High risk; issues and pull_request are Medium–High; schedule is Low–Predictable; workflow_dispatch is Low

- **Evidence**: A dedicated "Trigger Frequency and Cost Risk" section provides a
  complete table of trigger types with risk ratings and explanatory notes.
- **Confidence**: settled (first-party documentation; the risk taxonomy is an
  explicit product of the source)
- **Quote**: (table data extracted verbatim — see Concrete Artifacts)
- **Our assessment**: The trigger-type risk taxonomy is the most operationally
  useful cost-management guidance in this source because it lets practitioners
  assess the cost risk of a workflow at design time, before deploying. A workflow
  on `push` (High risk) in a busy repository with 100 commits/day fires 100×/day;
  the same workflow on `schedule` fires once/day. The risk table makes this
  explicit and actionable. For Ch02: include the trigger-type risk table in the
  "Cost planning" section so practitioners assess trigger selection as a cost
  decision, not just a behavior decision.

### Claim 10: Scheduled workflows offer predictable budgets because they fire at a fixed cadence, making monthly cost calculation straightforward

- **Evidence**: The "Use Schedules for Predictable Budgets" subsection describes
  this strategy.
- **Confidence**: settled (first-party documentation; the scheduling mechanism is
  deterministic)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The "schedule = predictable" principle is the positive
  complement to the trigger-type risk taxonomy (Claim 9). It explains why
  `schedule` receives a "Low–Predictable" risk rating: the run count per month is
  a deterministic function of the cron schedule, making monthly cost estimation
  a simple multiplication rather than a workload-dependent projection. The common
  scenario estimates (Claim 12) show this in practice: the weekly digest
  (4×/month) yields ~1 Actions minute and 4–8 Copilot requests/month — fully
  predictable from the schedule alone. For Ch05 (Team Adoption): scheduled
  workflows are the recommended entry point for cost-conscious teams adopting
  gh-aw, because the cost is calculable upfront.

### Claim 11: The Agentic Cost Optimization pattern enables a scheduled meta-agent to automatically optimize expensive workflows by using the `agentic-workflows` MCP tool to fetch cost data and propose frontmatter changes via pull request

- **Evidence**: The "Agentic Cost Optimization" section describes the pattern
  and its mechanism.
- **Confidence**: emerging (first-party documentation; the pattern is described
  but the reference implementation is separate — see `docs-ghaw-agentic-ops.md`)
- **Quote**: "The `agentic-workflows` MCP tool exposes the same operations as the
  CLI (`logs`, `audit`, `status`) to any workflow agent, so a scheduled meta-agent
  can inspect and optimize other agentic workflows automatically — fetching
  aggregate cost data, deep-diving into individual runs, and proposing frontmatter
  changes (cheaper model, tighter `skip-if-match`, lower `user-rate-limit`) via
  a pull request."
- **Our assessment**: This is the most novel claim in the source. The Agentic Cost
  Optimization pattern closes the loop between cost monitoring and cost reduction:
  instead of practitioners manually reading `gh aw logs` and editing workflow
  frontmatter, a meta-agent performs the full cycle automatically. The specific
  optimization proposals — cheaper model, tighter `skip-if-match`, lower
  `user-rate-limit` — map directly to the three configuration-level cost levers
  documented in Claims 5–8. The `agentic-workflows` MCP tool as the mechanism
  is significant: it gives any agent workflow the same cost-data access as the
  `gh aw` CLI, enabling self-optimization at scale. This is the conceptual
  description of the pattern the reference implementation in
  `docs-ghaw-agentic-ops.md` instantiates as `copilot-token-optimizer`. For Ch02:
  introduce the Agentic Cost Optimization pattern as the automated tier of cost
  management, above manual monitoring and below architectural redesign.

### Claim 12: Common scenario estimates provide concrete cost anchors: a weekly scheduled digest costs ~1 Actions minute/month plus 4–8 Copilot premium requests; issue triage on 20 events/month costs ~10 Actions minutes plus 20–40 premium requests; PR review on a busy repo (100 pushes/month) costs ~100 Actions minutes plus 100–200 premium requests

- **Evidence**: The "Common Scenario Estimates" section provides a table of four
  representative scenarios with Actions minutes and inference costs per month.
- **Confidence**: emerging (first-party documentation; these are example estimates,
  not billing guarantees — actual costs depend on model, context size, and task
  complexity)
- **Quote**: (table data extracted verbatim — see Concrete Artifacts)
- **Our assessment**: The scenario estimates are the first concrete cost anchors in
  the corpus for gh-aw deployments. They establish order-of-magnitude expectations
  for three common workflow types: background scheduled (low cost), event-driven
  at moderate volume (medium cost), and event-driven at high volume (high cost).
  The PR review scenario (100 pushes/month → ~100 Actions minutes) illustrates the
  Claim 9 risk rating: `push` is "High" risk because even moderate repository
  activity produces high aggregate cost. For Ch05 (Team Adoption): the scenario
  estimates are the starting point for a cost conversation with stakeholders — "a
  weekly digest costs about N/month in Copilot requests" is a concrete number that
  teams can validate against their Copilot subscription budget.

## Concrete Artifacts

### Cost Component Definition (from source)

```
"The cost of running an agentic workflow is the sum of two components:
GitHub Actions minutes consumed by the workflow jobs, and inference costs
charged by the AI provider."

Typical job structure per run:
  Pre-activation / detection:  10–30 seconds execution + ~1.5 min runner overhead
  Agent job:                   1–15 minutes execution  + ~1.5 min runner overhead
```

*Source: https://github.github.com/gh-aw/reference/cost-management, "Cost Components" section*

### Cost Monitoring Commands (from source)

```bash
# Overview table for all agentic workflows (last 10 runs)
gh aw logs

# Narrow to a single workflow
gh aw logs issue-triage-agent

# Aggregate cost by workflow over the last 30 days (JSON + jq)
gh aw logs --start-date -30d --json | \
  jq '[.runs[]] | group_by(.workflow_name) |
  map({workflow: .[0].workflow_name, runs: length, total_cost: (map(.estimated_cost) | add // 0)})'

# Per-run detailed breakdown
gh aw audit <run-id>
```

*Source: https://github.github.com/gh-aw/reference/cost-management, "Monitoring Costs with gh aw logs" section*

### skip-if-match Configuration Example (from source)

```yaml
on:
  issues:
    types: [opened]
  skip-if-match: 'label:duplicate OR label:wont-fix'
```

*Source: https://github.github.com/gh-aw/reference/cost-management, "Use Deterministic Checks to Skip the Agent" section*

### Model Selection for Cost Reduction (from source)

```yaml
# Copilot with lighter model
engine:
  id: copilot
  model: gpt-4.1-mini

# Claude with lighter model
engine:
  id: claude
  model: claude-haiku-4-5
```

*Source: https://github.github.com/gh-aw/reference/cost-management, "Choose a Cheaper Model" section*

### Per-User Rate Limiting for Cost Control (from source)

```yaml
user-rate-limit:
  max-runs-per-window: 3
  window: 60  # 3 runs per hour per user
```

*Source: https://github.github.com/gh-aw/reference/cost-management, "Rate Limiting and Concurrency" section*

### Trigger Type Risk Assessment Table (from source)

| Trigger type | Risk | Notes |
|---|---|---|
| `push` | High | Every commit to any matching branch fires the workflow |
| `pull_request` | Medium–High | Fires on open, sync, re-open, label, and other subtypes |
| `issues` | Medium–High | Fires on open, close, label, edit, and other subtypes |
| `check_run`, `check_suite` | High | Can fire many times per push in busy repositories |
| `issue_comment`, `pull_request_review_comment` | Medium | Scales with comment activity |
| `schedule` | Low–Predictable | Fires at a fixed cadence; easy to budget |
| `workflow_dispatch` | Low | Human-initiated; naturally rate-limited |

*Source: https://github.github.com/gh-aw/reference/cost-management, "Trigger Frequency and Cost Risk" section*

### Common Scenario Estimates Table (from source)

| Scenario | Frequency | Actions minutes/month | Inference/month |
|---|---|---|---|
| Weekly digest (schedule, 1 repo) | 4×/month | ~1 min | ~4–8 premium requests (Copilot) |
| Issue triage (issues opened, 20/month) | 20×/month | ~10 min | ~20–40 premium requests |
| PR review on every push (busy repo, 100 pushes/month) | 100×/month | ~100 min | ~100–200 premium requests |
| On-demand via slash command | User-controlled | Varies | Varies |

*Source: https://github.github.com/gh-aw/reference/cost-management, "Common Scenario Estimates" section*

### Agentic Cost Optimization — Pattern Description (from source)

```
"The `agentic-workflows` MCP tool exposes the same operations as the CLI
(`logs`, `audit`, `status`) to any workflow agent, so a scheduled meta-agent
can inspect and optimize other agentic workflows automatically — fetching
aggregate cost data, deep-diving into individual runs, and proposing frontmatter
changes (cheaper model, tighter `skip-if-match`, lower `user-rate-limit`) via
a pull request."
```

*Source: https://github.github.com/gh-aw/reference/cost-management, "Agentic Cost Optimization" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-agentic-ops.md` Claim 3 ("repeated failures, abnormal token
    consumption, or other unhealthy patterns" as the three detection classes for
    fleet monitoring): this source documents the cost-monitoring commands and
    scenario estimates that practitioners use to detect those same anomalies at
    the operational level. The agentic-ops pattern is the automated tier; this
    reference is the manual-monitoring tier.
  - `docs-ghaw-agentic-ops.md` Claim 8 (audit workflow using `gh aw logs
    --engine copilot --start-date -1d --json -c 100`): confirms that `gh aw logs`
    is the platform's canonical cost-monitoring command, consistent with what this
    reference documents for manual use. The same CLI is used for both human and
    automated monitoring.
  - `docs-ghaw-agentic-ops.md` Claim 9 (cost anomaly thresholds: >30% total
    tokens, high error rate, >100K avg tokens per run): those thresholds are the
    fleet-monitoring layer built on top of the per-run data this reference teaches
    practitioners to read with `gh aw logs` and `gh aw audit`.
  - `docs-ghaw-rate-limiting-controls.md` Claim 8 (the `rate-limit` frontmatter
    field for per-user throttling): that reference documents the same mechanism
    this source calls `user-rate-limit`. Both describe max-runs-per-window and
    window semantics. The naming difference may be an alias or a documentation
    version gap; practitioners should consult both pages when configuring this
    control. See also Extraction Notes §2.
  - `docs-ghaw-effective-tokens-specification.md` Claim 1 (ET normalizes token
    counts across token classes and models): the `estimated_cost` field in `gh aw
    logs --json` output is the billing-coupled complement to ET's billing-independent
    computational intensity metric. Together they provide both the cost-control view
    (this source) and the computational-intensity view (ET spec) of the same
    underlying run data.
  - `blog-bswen-mcp-token-cost.md` Claim 3 ("If you have a 200k context window
    and burn 100k on tool definitions, you've already lost half your capacity"):
    the context limiting strategy in this source (Claim 7) is the gh-aw
    implementation of the same principle — reducing tokens processed per run is
    the primary inference cost lever in both Claude Code and gh-aw contexts.

- **Extends**:
  - `docs-ghaw-agentic-ops.md`: The agentic-ops source covers the reference
    implementation of automated cost monitoring (the `copilot-token-audit` and
    `copilot-token-optimizer` workflows). This cost management reference is the
    human-facing documentation that teaches practitioners the underlying cost
    model, CLI tools, and configuration levers — the conceptual layer beneath
    the automation.
  - `docs-ghaw-rate-limiting-controls.md`: That source covers rate limiting as
    an anti-runaway safety mechanism. This source covers the same `user-rate-limit`
    field as a cost-control mechanism. Together they give practitioners both
    the safety framing and the cost framing for the same configuration.
  - `docs-ghaw-monitoring-patterns.md`: That source covers monitoring
    configuration primitives (safe-outputs for failure reporting, `gh aw audit`,
    `gh aw logs --format markdown`). This cost reference adds the billing context
    to the same CLI commands — `gh aw logs` is not just a log viewer but also the
    cost-reporting command.

- **Contradicts**: None identified. The `user-rate-limit` field name difference
  from `docs-ghaw-rate-limiting-controls.md`'s `rate-limit` is a potential
  documentation inconsistency but not a material contradiction — the underlying
  mechanism and semantics are the same. No contradiction issue filed.

- **Novel** (what this note adds that no prior source covers):
  - **Trigger-type cost risk taxonomy** (Claim 9): No existing source note provides
    a complete table of gh-aw trigger types rated by cost risk. The `push` and
    `check_run`/`check_suite` = High, `schedule` = Low–Predictable taxonomy is the
    first corpus entry giving practitioners a design-time cost-risk assessment
    framework for trigger selection.
  - **Common scenario cost estimates** (Claim 12): The four scenario estimates
    (weekly digest, issue triage, PR review, on-demand) are the first concrete
    cost anchors in the corpus. No existing source note provides specific
    Actions-minutes + inference-cost numbers for representative gh-aw workflows.
  - **Runner overhead accounting** (Claim 2): The ~1.5 minutes of runner setup
    overhead per job (in addition to execution time) is not documented in any
    existing source note. This overhead affects minimum-cost calculations for all
    gh-aw workflows.
  - **Engine-specific inference billing models** (Claim 3): The difference between
    Copilot (premium request billing) and Claude/OpenAI (token billing to respective
    accounts) is not documented in any existing source note.
  - **Agentic Cost Optimization pattern via `agentic-workflows` MCP** (Claim 11):
    The pattern of using the `agentic-workflows` MCP tool to build a meta-agent
    that automatically proposes cost-reduction frontmatter changes via PR is
    described here as the conceptual pattern. The reference implementation is in
    `docs-ghaw-agentic-ops.md`; this source provides the foundational description.
    The specific optimization proposals (cheaper model, tighter `skip-if-match`,
    lower `user-rate-limit`) are new to the corpus as named optimization targets.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add the two-component cost model (Actions minutes + inference) as the
    foundational framing for cost planning in gh-aw harness design. Practitioners
    need to know which component dominates their workflow type before choosing
    the right cost-reduction strategy.
  - Add the trigger-type risk taxonomy (Claim 9) as a design-time tool for
    cost risk assessment. `push` and `check_run`/`check_suite` triggers should
    carry explicit cost-risk warnings; `schedule` is the recommended starting
    point for cost-predictable deployments.
  - Add `skip-if-match` (Claim 5) as the highest-ROI cost control — before model
    selection, context limiting, or rate limiting. Any condition evaluable without
    an LLM call belongs in `skip-if-match`.
  - Add runner overhead accounting (~1.5 min/job) to the cost-estimation framework
    so practitioners can calculate minimum run costs accurately.
  - Document `gh aw logs` + `gh aw audit <run-id>` as the two-tier cost monitoring
    pair: fleet-level trend and per-run forensics respectively.
  - Add the Agentic Cost Optimization pattern (Claim 11) as the automated cost
    management tier: once manual monitoring is in place, a meta-agent using the
    `agentic-workflows` MCP can automate the review-and-optimize cycle. Reference
    `docs-ghaw-agentic-ops.md` for the reference implementation.

- **Chapter 03 (Safety and Verification)**:
  - Cross-reference the trigger-type risk table (Claim 9) when discussing workflow
    design principles — `push`/`check_run` triggers that bypass cost controls
    are also safety risks (runaway cost = runaway behavior).
  - Note that `skip-if-match` (Claim 5) is both a cost control and a safety
    mechanism: deterministic pre-checks that cancel the agent before it runs
    are the cheapest and most reliable safety gate.

- **Chapter 05 (Team Adoption)**:
  - Lead the cost section with the common scenario estimates (Claim 12): teams
    adopting gh-aw need concrete numbers to plan budgets. A weekly digest costs
    ~1 Actions minute + 4–8 Copilot premium requests/month — calculable from
    the schedule alone and easily within most Copilot subscription budgets.
  - Use the scenario estimates to motivate scheduled workflows as the recommended
    first deployment pattern for cost-predictability during adoption. Justify
    moving to event-driven triggers only after establishing a cost baseline with
    scheduled workflows.
  - Document the engine-specific billing model (Claim 3) so teams using different
    AI engines know which billing dashboard to monitor.

## Extraction Notes

1. **WebFetch content processed via AI model**: The gh-aw documentation is served
   as an Astro/Starlight SPA. The WebFetch tool processes HTML content through an
   AI model before returning results. Structured data (table values, YAML field
   names, CLI command syntax, numeric timing values) is likely accurate from
   multiple consistent fetch passes. The Agentic Cost Optimization description
   (Claim 11) returned in the same verbatim form across two independent fetch
   passes with different prompts — high confidence it is close to verbatim.
   Prose passages marked with "(no direct quote)" were not returned in a form
   I could verify as character-for-character matches; the assessment in those
   claims is based on consistent paraphrases.

2. **`user-rate-limit` vs. `rate-limit` field name discrepancy**: The cost
   management page uses `user-rate-limit` as the frontmatter field name in its
   YAML example (`max-runs-per-window: 3`, `window: 60`). The rate-limiting
   controls reference (`docs-ghaw-rate-limiting-controls.md`) uses `rate-limit`
   with `max:`, `window:`, `events:`, and `ignored-roles:` subfields. The
   subfield names differ (`max-runs-per-window` vs. `max`). This may reflect a
   platform naming evolution, an alias, or a documentation version difference.
   Both fields appear to control the same per-user throttling mechanism. The
   discrepancy is noted here for the Assayer; a detailed investigation of the
   platform's authoritative field name would require reading the frontmatter
   reference page (`docs-ghaw-frontmatter-full-reference.md`).

3. **"What to Optimize Automatically" subsection**: The source contains a subsection
   under "Agentic Cost Optimization" titled "What to Optimize Automatically." The
   content of this subsection (specific optimization targets beyond model, skip-if-match,
   and rate limiting) was not returned in detail by the WebFetch passes. The
   Claim 11 assessment is based on the opening description of the pattern
   (which was returned verbatim-quality) plus the three named optimization
   proposals from the same description.

4. **No contradictions filed**: Reviewed the potential `user-rate-limit` vs.
   `rate-limit` naming difference against MINER.md §4a criteria. The two names
   appear to describe the same mechanism with potentially different YAML syntax —
   not a material opposition that would lead to different guide advice. The
   Assayer may wish to verify the authoritative field name against the frontmatter
   reference page. No other claims oppose existing source notes; the cost estimates
   are additive to the corpus, not contradictory.

5. **Previous PR #679**: A prior Miner PR (branch `miner/issue-375-r25703781057`)
   was opened and subsequently closed for this issue. This extraction is
   independent; the current source note was written from scratch against the same
   source URL.
