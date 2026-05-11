---
source_url: https://github.github.com/gh-aw/reference/cost-management
source_type: docs
title: "GitHub Agentic Workflows: Cost Management Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#375"
---

# GitHub Agentic Workflows: Cost Management Reference

> The practitioner-facing reference for understanding, monitoring, and reducing
> costs in gh-aw deployments — covering the two-component billing model
> (Actions minutes + inference), trigger-frequency risk, model selection,
> skip-if-match guards, and the Agentic Cost Optimization meta-pattern for
> automated cross-workflow cost reduction.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/cost-management`
  page — in the `reference/` section alongside `reference/rate-limiting-controls`,
  `reference/concurrency`, and `reference/permissions`. Reference pages document
  platform behavior precisely; this one covers cost drivers and reduction strategies
  practitioners need for deploying workflows at scale.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team
  (GitHub Next / Microsoft Research — the same team behind Peli de Halleux's
  "Agent Factory" blog series, the `gh aw` CLI, and all other `reference/` pages
  in the corpus). Cost figures, CLI commands, model names, and configuration field
  names are authoritative for the `gh aw` platform. Budget estimates are
  representative calibration values, not contractual SLAs.
- **Scope**: Covers the two billing components (Actions minutes, inference costs),
  monitoring via `gh aw logs` and `gh aw audit`, trigger frequency risk table,
  five cost reduction strategies (skip-if-match guards, model selection, context
  limiting, rate limiting, scheduled triggers), budget calibration examples, and the
  Agentic Cost Optimization meta-pattern. Does NOT cover: the full `gh aw logs`
  field schema (see `docs-ghaw-monitoring-patterns.md`), the detailed rate-limit
  configuration (see `docs-ghaw-rate-limiting-controls.md`), the fleet-level cost
  anomaly detection thresholds (see `docs-ghaw-agentic-ops.md` Claim 9), or per-run
  audit schema (see `docs-ghaw-agentic-ops.md` Concrete Artifacts → Audit Workflow
  Run Data Schema section).

## Extracted Claims

### Claim 1: GH-AW costs split into two independent billing components — GitHub Actions compute minutes and AI inference charges billed separately to the AI provider account

- **Evidence**: "Cost Components" section of the page enumerates both billing
  streams with their charging mechanisms.
- **Confidence**: settled (first-party documentation; the billing separation is
  a platform architectural fact, not a recommendation)
- **Quote**: "Every workflow job consumes compute time billed at standard GitHub
  Actions rates."
- **Our assessment**: The billing split is practically important for teams managing
  separate budgets. Actions minutes are billed to the GitHub organization or account
  hosting the repository; inference costs are billed to the AI provider account
  (ANTHROPIC_API_KEY, OPENAI_API_KEY, or the account owning COPILOT_GITHUB_TOKEN).
  A cost spike can originate in either layer. For Ch02 (Harness Engineering): when
  documenting cost management, always name both billing streams — teams tracking
  only inference costs will miss Actions-minutes overruns from high-frequency
  triggers, and vice versa.

### Claim 2: A typical agentic workflow consumes three compute phases: a pre-activation/detection job (10–30 seconds), an agent job (1–15 minutes), and approximately 1.5 minutes of runner setup overhead per job

- **Evidence**: "Cost Components" section provides the breakdown of GitHub Actions
  minutes per phase for a representative workflow run.
- **Confidence**: settled (first-party documentation; the phase ranges are specific
  platform characterizations)
- **Quote**: (no single direct quote captures all three phases; see paraphrase and
  artifact below)
- **Our assessment**: The ~1.5-minute runner setup overhead is the often-missed
  cost item. It is paid even for very short agent runs — a 20-second pre-activation
  detection job that finds nothing still bills approximately 1.5 minutes for runner
  startup before that 20 seconds of work. For high-frequency triggers (every push,
  every check run), this overhead accumulates rapidly. The 1–15 minute agent job
  range reflects the wide variance between a focused classification task (~1 min)
  and a multi-step code review or research task (~15 min). For Ch02: document the
  per-job setup overhead as a constant cost floor for any trigger, independent of
  whether the agent does useful work.

### Claim 3: Trigger frequency is the primary driver of cost variance — scheduled triggers are low and predictable; push, pull request, and check-run triggers carry medium-to-high runaway risk

- **Evidence**: "Trigger Frequency Risk Assessment" section provides an explicit
  risk classification per trigger type, with Push and Check runs rated "High risk"
  and Schedule rated "Low and predictable."
- **Confidence**: settled (first-party; the risk classifications are explicit)
- **Quote**: "Push: High risk (every commit triggers)"
  / "Schedule: Low and predictable"
- **Our assessment**: Check-run triggers are the highest-risk trigger type in
  practice because a single push fires multiple check runs (one per CI job), meaning
  a workflow triggered by check runs can fire 5–20 times for one developer commit.
  This maps directly to the 5× cost runaway example from `blog-ghaw-weekly-mar2026.md`
  and the 1.55M token runaway in `blog-ghaw-weekly-2026-03-23.md` Claim 6. The
  risk table operationalizes those incident patterns into a pre-deployment checklist.
  For Ch02: this table belongs in the harness design section as a trigger-selection
  guide — teams should be required to justify any non-schedule trigger before
  deploying a new workflow.

### Claim 4: The recommended starting posture for new workflows is `schedule` or `workflow_dispatch` triggers while evaluating actual costs before enabling higher-frequency triggers

- **Evidence**: Explicit recommendation in the "Trigger Frequency Risk Assessment"
  section following the risk table.
- **Confidence**: settled (first-party; stated as a direct recommendation)
- **Quote**: "Recommendation: Begin with `schedule` or `workflow_dispatch` while
  evaluating costs."
- **Our assessment**: This is the gh-aw platform's cost-safety graduation model:
  start with low-risk triggers, measure actual token consumption and Actions minutes
  using `gh aw logs`, then promote to higher-frequency triggers only after the cost
  profile is understood. It mirrors the "start in report-only mode" principle from
  `docs-ghaw-safe-rollout.md` Claim 1 — conservative defaults, promote after
  validation. For Ch05 (Team Adoption): document this two-phase trigger adoption as
  the standard rollout sequence. Avoid giving teams push-triggered workflows as
  their first deployment — schedule first, push later.

### Claim 5: `skip-if-match`/`skip-if-no-match` pre-filters are the most effective cost reduction strategy because they prevent agent execution entirely — eliminating both Actions minutes and inference costs for filtered invocations

- **Evidence**: "Cost Reduction Strategies" section explicitly identifies this as
  "the most effective approach" among the five listed strategies.
- **Confidence**: settled (first-party; superlative effectiveness claim is explicit)
- **Quote**: "Skip the agent entirely using `skip-if-match`/`skip-if-no-match`
  conditions before the agent job starts—the most effective approach."
- **Our assessment**: The effectiveness claim is correct in principle: a skipped
  agent run avoids both inference cost AND the full agent job's Actions minutes.
  By contrast, model selection or context limiting only reduces per-run cost;
  skip-if-match can reduce run count to near zero for high-frequency triggers on
  low-signal events (e.g., a PR review workflow that skips draft PRs or PRs from
  bots). `skip-if-match` is documented in `docs-ghaw-compilation-process.md`
  Claim 4 as a deduplication mechanism in the pre-activation job; this source
  reframes it as the primary cost-control lever. For Ch02: position skip filters
  as a first-line cost-control tool, not just a deduplication mechanism — their
  cost-avoidance role is as important as their correctness role.

### Claim 6: Model selection for cost control — lighter models (gpt-4.1-mini, claude-haiku-4-5) are explicitly recommended for routine and structured-output tasks; premium models for complex reasoning

- **Evidence**: "Cost Reduction Strategies" section names specific model IDs
  with their recommended task categories.
- **Confidence**: settled (first-party; explicit model-to-task recommendations)
- **Quote**: "Use lighter models for routine tasks: `gpt-4.1-mini` instead of GPT-5"
  / "`claude-haiku-4-5` for structured outputs"
- **Our assessment**: This is the first-party model selection guidance tied
  specifically to task type in the gh-aw platform context. The structured
  outputs use case for `claude-haiku-4-5` is the most actionable: JSON extraction,
  classification, label assignment, and format-conversion tasks all qualify.
  The GPT-5 → gpt-4.1-mini substitution targets inference cost directly — gpt-4.1-mini
  is substantially cheaper per token than premium GPT-5 models. For Ch02: add a
  model selection decision rule — structured outputs and simple classifications
  → smallest capable model; analysis, code review, planning → premium model.

### Claim 7: Context limiting — writing focused prompts, avoiding full-file reads, and capping result counts — directly reduces inference cost by reducing token consumption per run

- **Evidence**: "Cost Reduction Strategies" section provides three specific
  context-limiting techniques.
- **Confidence**: settled (first-party; the specific techniques are named)
- **Quote**: "Write focused prompts, avoid full-file reads, cap result counts."
- **Our assessment**: Each of the three techniques targets a different source of
  excess token consumption. Focused prompts reduce the agent's system prompt and
  task context. Avoiding full-file reads prevents loading large files when only
  specific sections are needed (cross-reference: `docs-ghaw-agentic-ops.md` Claim 13
  recommends `awk`-based partial file reads for the same reason). Capping result
  counts limits the size of API response payloads loaded into agent context. These
  are the same five token-efficiency anti-patterns documented in
  `docs-ghaw-agentic-ops.md` Claim 11 from a different angle — this source names
  the harness-level design principles; that source names the run-level anti-patterns
  to detect. For Ch02: document context limiting as a harness design discipline,
  not just a runtime concern — it should be enforced at workflow authoring time
  through prompt review and result-cap configs.

### Claim 8: Rate limiting user-triggered runs per time window reduces inference cost for externally-triggered workflows subject to bursts or abuse

- **Evidence**: "Cost Reduction Strategies" section includes rate limiting as
  one of the five strategies.
- **Confidence**: settled (first-party; corroborated by the full `rate-limit`
  field documentation in `docs-ghaw-rate-limiting-controls.md`)
- **Quote**: "Cap user-triggered runs per time window."
- **Our assessment**: Rate limiting is documented in depth in
  `docs-ghaw-rate-limiting-controls.md` Claim 8 (the `rate-limit` frontmatter
  field with `max`, `window`, `events`, and `ignored-roles`). This source positions
  it explicitly as a cost control tool, adding the cost-management framing to the
  safety/anti-runaway framing from the rate-limiting reference. For Ch02: when
  presenting rate limiting, present both its safety rationale (preventing abuse)
  and its cost rationale (bounding inference spend from bursty triggers).

### Claim 9: Scheduled triggers provide predictable budget certainty because run counts are known in advance from the cron schedule

- **Evidence**: "Cost Reduction Strategies" section names scheduled triggers as a
  distinct cost-reduction strategy with the "budget certainty" rationale.
- **Confidence**: settled (first-party; the rationale is stated directly)
- **Quote**: "Use fixed cadences for budget certainty."
- **Our assessment**: The budget-predictability advantage of scheduled triggers goes
  beyond just risk classification (Claim 3). A scheduled workflow with a daily cron
  at noon has exactly 30 runs per month — its cost is bounded and predictable.
  A push-triggered workflow has unbounded run count tied to developer activity.
  For financial forecasting, the schedule-first posture (Claim 4) doubles as a
  budget-planning posture — scheduled workflows are line-item predictable in ways
  that event-triggered workflows are not. For Ch05 (Team Adoption): when teams
  evaluate gh-aw deployment costs, point to scheduled workflows as the baseline
  case for financial modeling.

### Claim 10: `gh aw logs [workflow-name]` shows per-run metrics including duration, token usage, and estimated inference cost; `gh aw logs --json` exports for programmatic trend analysis

- **Evidence**: "Monitoring Costs" section documents the `gh aw logs` command and
  its key output fields and flags.
- **Confidence**: settled (first-party CLI documentation; consistent with
  `docs-ghaw-monitoring-patterns.md` Claim 9 and `docs-ghaw-agentic-ops.md`
  Claim 8 which document the same CLI command)
- **Quote**: "View recent runs: `gh aw logs [workflow-name]`"
  / "Export JSON: `gh aw logs --json` for trend analysis"
- **Our assessment**: The `gh aw logs` command is the practitioner's primary
  cost-inspection tool — it surfaces the per-run cost data needed to make the
  trigger selection and model selection decisions from Claims 3–6. The `--json`
  flag is the bridge to automated analysis: the `docs-ghaw-agentic-ops.md` reference
  implementation uses `gh aw logs --engine copilot --start-date -1d --json -c 100`
  as the core data collection step for its fleet-level cost audit. For Ch02: document
  `gh aw logs` as the essential first tool for any cost investigation, before
  committing to architectural changes.

### Claim 11: `gh aw audit <run-id>` provides single-run token breakdown for deep-dive cost analysis

- **Evidence**: "Monitoring Costs" section documents the audit command as the
  per-run inspection tool.
- **Confidence**: settled (first-party; consistent with `docs-ghaw-monitoring-patterns.md`
  Claim 7 which documents the same command from the practitioner operator perspective)
- **Quote**: "Deep-dive: `gh aw audit <run-id>` for single-run token breakdown"
- **Our assessment**: `gh aw audit` complements `gh aw logs` — logs provide fleet-level
  trend data; audit provides the granular per-run breakdown needed to understand
  *why* a specific run was expensive. The two-tier monitoring (fleet trend + per-run
  drill-down) is the same pattern used by `docs-ghaw-agentic-ops.md` in its audit
  and optimizer workflows. For Ch02: document the two-tier approach: `gh aw logs`
  for trend detection, `gh aw audit <run-id>` for root-cause analysis.

### Claim 12: Episode-level analysis groups multiple workflow runs into logical task units, enabling cost attribution at the task level rather than the individual run level

- **Evidence**: "Monitoring Costs" section introduces episode-level analysis as a
  distinct monitoring capability.
- **Confidence**: emerging (first-party documentation; episode-level analysis is
  mentioned briefly and details are limited — no existing source note covers
  episode semantics in depth)
- **Quote**: "Episode-level analysis tracks logical executions across grouped runs"
- **Our assessment**: Episode-level tracking is architecturally important for
  workflows that span multiple runs (multi-step agents, fork-then-join patterns,
  research-then-implement sequences). Without episode attribution, cost data tells
  you per-run cost but not per-task cost — a task that splits across 5 runs shows
  5 cheap runs, obscuring its true total cost. The episode abstraction is not
  documented in any existing source note; this is the first corpus mention.
  For Ch02: document episode-level analysis as the correct cost accounting unit
  for multi-run workflows; recommend enabling it for any workflow that uses
  orchestration patterns documented in `docs-ghaw-orchestration-patterns.md`.

### Claim 13: Budget calibration examples: a weekly digest workflow costs ~4 premium inference requests/month; an issue-triage workflow (20 opens/month) costs ~20–40 requests; a PR review workflow (100 pushes/month) costs ~100–200 requests

- **Evidence**: "Budgeting Examples" section provides three representative scenarios
  with request-count estimates.
- **Confidence**: emerging (representative calibration values from first-party
  documentation; not contractual estimates — actual costs depend on model
  selection, prompt length, tool usage, and inference provider pricing)
- **Quote**: "Weekly digest: ~4 premium requests/month"
  / "Issue triage (20 opens/month): ~20-40 premium requests"
  / "PR review (100 pushes/month): ~100-200 premium requests"
- **Our assessment**: These three examples span a 50× range in inference cost
  (4 to 200 requests/month), driven primarily by trigger frequency. The PR review
  example is 1:1 with push count — each push → one premium inference request —
  which clarifies that "premium request" is roughly equivalent to one agent
  invocation at normal task complexity. The issue-triage range (20–40 for 20 events)
  reflects that some triage runs may require multiple inference calls or tool uses.
  For Ch05 (Team Adoption): use these three examples as a cost-modeling starter
  kit. Teams can extrapolate: a PR review workflow on a high-velocity repo
  (500 pushes/month) would consume ~500–1000 premium requests/month.

### Claim 14: The `agentic-workflows` MCP tool enables scheduled meta-agents to inspect cross-workflow cost data and propose optimizations via pull requests — the Agentic Cost Optimization meta-pattern

- **Evidence**: "Automated Cost Optimization" section documents the pattern and
  its mechanism.
- **Confidence**: emerging (first-party documentation; the specific MCP tool is
  named but the production usage metrics and PR acceptance rates are not given)
- **Quote**: "The `agentic-workflows` MCP tool allows scheduled meta-agents to
  inspect cost data across workflows and propose optimizations via pull requests."
- **Our assessment**: This is the self-referential cost optimization pattern —
  a scheduled agent workflow that monitors and rewrites other agent workflows for
  cost efficiency. The "propose via pull requests" mechanism ensures changes go
  through human review rather than auto-applying, preserving human oversight.
  This is the highest-level expression of the meta-agent pattern documented in
  `docs-ghaw-agentic-ops.md` (which covers audit + optimization as two separate
  workflows using `repo-memory`). The cost management reference names it as a
  distinct pattern. For Ch02: document this meta-optimization pattern as the
  long-term cost governance strategy for large gh-aw deployments — after initial
  manual optimization, a scheduled meta-agent can maintain cost efficiency
  continuously at scale.

## Concrete Artifacts

### Cost Components Breakdown (from source)

```
GitHub Actions Minutes — two job types per typical run:
  Pre-activation/detection job:  10–30 seconds
  Agent job:                     1–15 minutes
  Runner setup overhead:         ~1.5 minutes per job (constant cost floor)

Inference Costs — billed to AI provider account:
  Copilot:  charged to account owning COPILOT_GITHUB_TOKEN
  Claude:   billed to Anthropic account via ANTHROPIC_API_KEY
  Codex:    billed to OpenAI account via OPENAI_API_KEY
```

*Source: docs-ghaw-cost-management, "Cost Components" section*

### Trigger Frequency Risk Table (from source)

| Trigger Type      | Risk Level    | Notes |
|-------------------|---------------|-------|
| Push              | High          | Every commit triggers |
| Pull requests     | Medium-High   | Each PR event triggers |
| Issues            | Medium-High   | Each issue event triggers |
| Check runs        | High          | Multiple fires per push |
| Schedule          | Low           | Predictable; budget-safe |
| workflow_dispatch | Low           | Human-initiated only |

*Source: docs-ghaw-cost-management, "Trigger Frequency Risk Assessment" section*

### Cost Reduction Strategies Summary (from source)

```
Strategy 1: Skip agent entirely (most effective)
  Mechanism: skip-if-match / skip-if-no-match pre-filters
  Benefit: eliminates both Actions minutes AND inference cost for filtered runs

Strategy 2: Choose cheaper models
  Examples: gpt-4.1-mini (instead of GPT-5); claude-haiku-4-5 (structured outputs)
  Benefit: reduces per-run inference cost

Strategy 3: Limit context size
  Techniques: focused prompts, avoid full-file reads, cap result counts
  Benefit: reduces tokens per run → reduces inference cost

Strategy 4: Rate limiting
  Mechanism: cap user-triggered runs per time window (rate-limit frontmatter field)
  Benefit: bounds total run count for externally-triggered workflows

Strategy 5: Predictable schedules
  Mechanism: use fixed cron cadences instead of event triggers
  Benefit: budget certainty through bounded run count
```

*Source: docs-ghaw-cost-management, "Cost Reduction Strategies" section*

### Cost Monitoring CLI Commands (from source)

```bash
# Per-run metrics (duration, token usage, estimated inference cost)
gh aw logs [workflow-name]

# JSON export for programmatic trend analysis
gh aw logs --json

# Single-run token breakdown (deep-dive)
gh aw audit <run-id>
```

*Source: docs-ghaw-cost-management, "Monitoring Costs" section*

### Budget Calibration Examples (from source)

```
Workflow type                              Estimated cost
──────────────────────────────────────────────────────────
Weekly digest                              ~4 premium requests/month
Issue triage (20 opens/month)              ~20-40 premium requests/month
PR review (100 pushes/month)               ~100-200 premium requests/month
```

*Source: docs-ghaw-cost-management, "Budgeting Examples" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-agentic-ops.md` Claim 8 (audit workflow downloads logs with
    `gh aw logs --engine copilot --start-date -1d --json -c 100`): this source
    confirms `gh aw logs --json` as the standard cost-monitoring export format;
    the agentic-ops reference implementation operationalizes it in a fleet-level
    audit workflow.
  - `docs-ghaw-rate-limiting-controls.md` Claim 8 (the `rate-limit` frontmatter
    field for per-user request throttling): this source corroborates rate limiting
    as a cost-reduction strategy, adding the cost-management framing to the
    safety/anti-runaway framing of that reference page.
  - `docs-ghaw-compilation-process.md` Claim 4 (`skip-if-match` deduplication
    in the pre-activation job): this source confirms that `skip-if-match`/
    `skip-if-no-match` is the "most effective" cost reduction strategy; the
    compilation process note documents *how* it works at the platform level;
    this note explains *why* it matters for cost.
  - `docs-ghaw-monitoring-patterns.md` Claim 7 (`gh aw audit <run-id>` for
    per-run inspection): both sources document the same audit CLI command;
    this source presents it from the cost-management perspective; that source
    presents it from the practitioner-operator perspective.
  - `docs-ghaw-monitoring-patterns.md` Claim 9 (`gh aw logs --format markdown`
    for scheduled workflow trend monitoring): both reference `gh aw logs` as
    the core cost-visibility command; this source adds the `--json` export flag
    for programmatic analysis.

- **Extends**:
  - `docs-ghaw-agentic-ops.md`: that note covers fleet-level cost *anomaly
    detection* (Claim 9: thresholds for heavy-hitter workflows, high error rates,
    >100K avg tokens per run) and automated optimization (Claim 10–11: the
    copilot-token-optimizer workflow). This source adds the *harness-level* cost
    reduction strategies that practitioners apply at workflow authoring time
    (trigger selection, model selection, skip filters, context limits). Together
    they form a two-tier cost governance framework: author-time controls (this
    source) + runtime monitoring and automated optimization (agentic-ops).
  - `docs-ghaw-rate-limiting-controls.md`: that reference provides the full
    `rate-limit` field specification (max 1–10, window up to 180 min, events,
    ignored-roles). This source adds the cost-reduction framing for why rate
    limiting matters beyond anti-runaway safety.
  - `docs-ghaw-deterministic-agentic-patterns.md`: that guide covers the four
    trigger-filtering approaches and the three hybrid architectures. This source
    positions `skip-if-match`/`skip-if-no-match` from those patterns as the
    primary cost-control mechanism — the deterministic-patterns guide motivates
    filtering on correctness grounds; this reference motivates it on cost grounds.
  - `blog-bswen-mcp-token-cost.md`: that source covers context token cost in
    Claude Code (MCP server overhead, CLAUDE.md sizing). This source covers
    inference cost in gh-aw workflows. Both address "how do I manage AI cost?"
    but at different layers: bswen addresses the local development context budget;
    this source addresses the fleet deployment inference bill.

- **Contradicts**: None identified. The cost-reduction strategies and monitoring
  approaches described here are consistent with their detailed treatments in
  existing source notes. No contradiction issue required.

- **Novel** (what this source adds that no prior source covers):
  - **Episode-level analysis as a cost attribution unit** (Claim 12): No existing
    source note documents the episode abstraction or positions it as the correct
    cost accounting unit for multi-run workflows. This is the first corpus
    description of episode-level cost attribution.
  - **Two-component billing model with provider-specific account routing** (Claim 1):
    No existing source note explicitly separates Actions minutes billing from
    inference billing or names the specific environment variables (ANTHROPIC_API_KEY,
    OPENAI_API_KEY, COPILOT_GITHUB_TOKEN) as the billing account routing keys.
  - **Trigger frequency risk classification table** (Claim 3): No existing source
    note provides a per-trigger-type cost risk classification. The weekly-update
    blog notes describe specific cost incidents (e.g., the 5× runaway), but none
    provides a structured risk table for all trigger types.
  - **Budget calibration examples tied to workflow type and event frequency**
    (Claim 13): No existing source note provides per-workflow-type cost estimates
    in premium-request units. These are the first concrete cost-modeling anchors
    in the corpus for gh-aw deployment planning.
  - **Agentic Cost Optimization as a named pattern** (Claim 14): While
    `docs-ghaw-agentic-ops.md` documents the copilot-token-optimizer reference
    implementation, this source names "Agentic Cost Optimization" as a distinct
    meta-pattern and positions the `agentic-workflows` MCP tool as its mechanism.
    This is the first corpus description of cost optimization as a named
    first-class pattern rather than an implementation detail.
  - **`skip-if-match` ranked as most effective cost strategy** (Claim 5): No
    existing source provides a ranked ordering of cost reduction strategies.
    This source explicitly names skip filters as the highest-impact approach.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add trigger selection as a cost-engineering decision, not just a functional
    decision. Use the risk table (Claim 3) to present a cost-aware trigger
    selection guide: schedule-first for new deployments, promote to event-triggered
    only after validating cost profile with `gh aw logs`.
  - Add `skip-if-match`/`skip-if-no-match` pre-filters as the recommended
    first-line cost control mechanism (Claim 5). Currently the deterministic
    patterns guide positions these primarily as correctness filters; Ch02 should
    add the cost-avoidance framing.
  - Add the two-component billing model (Actions minutes + inference) as a
    required mental model for workflow authors (Claim 1). Teams need to track
    both billing streams independently.
  - Add model selection decision rule (Claim 6): structured outputs and simple
    classification → claude-haiku-4-5 / gpt-4.1-mini; complex analysis and
    reasoning → premium model.
  - Add context limiting discipline (Claim 7): focused prompts, no full-file
    reads, capped result counts as authoring-time requirements.
  - Add the two-tier monitoring sequence (Claim 10–11): `gh aw logs` for trend
    detection, `gh aw audit <run-id>` for root-cause analysis.

- **Chapter 03 (Safety and Verification)**:
  - Cross-reference the Agentic Cost Optimization meta-pattern (Claim 14) with
    the fleet monitoring patterns from `docs-ghaw-agentic-ops.md`. The meta-agent
    that proposes cost-optimization PRs is an automated safety gate for cost
    compliance — it surfaces expensive workflows before they generate unmanageable
    bills.

- **Chapter 05 (Team Adoption)**:
  - Add the schedule-first deployment posture (Claim 4) as the standard rollout
    sequence. Document the concrete trigger promotion path: schedule → workflow_dispatch
    → issue/PR triggers → push (never check-run without careful analysis).
  - Add the budget calibration examples (Claim 13) as the financial modeling
    starter kit for teams evaluating deployment. The 4 / 20–40 / 100–200
    premium-requests-per-month anchors span the range from low-intensity
    (digest-style) to high-intensity (push-triggered review) deployments.

## Extraction Notes

1. **Source content via WebFetch AI model**: The gh-aw documentation is an
   Astro/Starlight SPA. The first WebFetch pass returned structured content
   including cost components, risk table, strategies, budgeting examples, and
   monitoring commands. A second-pass request for verbatim reproduction was
   declined citing copyright concerns. Prose passages marked as quotes were
   returned in quoted form by the model on the first pass and appear consistent
   with the page structure; they should be verified by the Assayer against the
   source URL. Technical strings (command syntax, model names, field names, numeric
   ranges) from the first pass are assessed as accurate platform specifications.

2. **Episode-level analysis detail is limited**: The source page mentions
   "episode-level analysis" in a single sentence. The corpus has no other
   description of this feature. The Assayer may wish to investigate whether the
   source page has a linked reference page for episode semantics. Claim 12 is
   marked `emerging` to reflect this uncertainty.

3. **"Premium requests" as the cost unit**: The budget calibration examples use
   "premium requests" as the billing unit. This likely corresponds to Copilot
   premium request billing (GitHub's per-request billing tier for AI-intensive
   operations). The exact mapping between one gh-aw workflow invocation and
   premium request count may vary by model and task complexity. The Assayer should
   verify whether the source page defines "premium requests" more precisely.

4. **No contradictions filed**: Reviewed all related source notes (docs-ghaw-agentic-ops,
   docs-ghaw-rate-limiting-controls, docs-ghaw-compilation-process,
   docs-ghaw-deterministic-agentic-patterns, docs-ghaw-monitoring-patterns,
   blog-bswen-mcp-token-cost, paper-miller-speed-cost-quality). No claim in this
   source materially opposes existing notes at the MINER.md §4a filing threshold.
   The agentic-ops and cost-management coverage is additive (fleet-level monitoring
   vs. harness-level design controls), not contradictory.

5. **Relationship to docs-ghaw-agentic-ops.md**: There is intentional design
   continuity between the cost-management reference page and the agentic-ops
   pattern. The cost-management page defines the problem and the author-time
   controls; the agentic-ops pattern provides the runtime automation for monitoring
   and optimizing. This source note covers the former; docs-ghaw-agentic-ops.md
   covers the latter. Both are required for a complete Ch02 treatment of cost
   management.
