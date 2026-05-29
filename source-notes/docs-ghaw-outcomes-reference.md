---
source_url: https://github.github.com/gh-aw/reference/outcomes
source_type: docs
title: "GitHub Agentic Workflows: Outcomes Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-29
last_checked: 2026-05-29
status: current
confidence_overall: emerging
issue: "#991"
---

# GitHub Agentic Workflows: Outcomes Reference

> The definitive gh-aw framework for measuring workflow effectiveness after safe outputs land
> in repositories — defines six outcome states, the outcome efficiency metric (effective tokens ÷
> accepted outcomes), accepted outcomes as the base measurement unit, and a three-level rollup
> hierarchy (run → episode → workflow); fills the evaluation gap in the corpus by answering
> "did the workflow actually work?" with observable, repository-state-based metrics.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/outcomes` page — in the
  "Reference" section alongside `reference/cost-management`,
  `reference/effective-tokens-specification`, and `reference/safe-outputs-specification`.
  Reference pages document platform behavior precisely. This page completes the measurement
  picture: safe outputs define what workflows produce; outcomes measure what happened to those
  outputs in the repository.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same team
  behind Peli de Halleux's "Agent Factory" blog series and the `gh aw` CLI. Outcome state
  definitions, the efficiency formula, and telemetry integration details are authoritative for
  the `gh aw` platform.
- **Scope**: Covers the outcomes framework for gh-aw: the definition of outcomes and why they
  are needed alongside cost data, the six outcome states, accepted outcomes as the measurement
  unit, telemetry integration via OpenTelemetry spans, the three-level rollup hierarchy
  (run → episode → workflow), and the recommended dashboard metrics. Does NOT cover: the Safe
  Outputs mechanism (what workflows produce — see `docs-ghaw-safe-outputs-specification.md`),
  the Effective Tokens specification (the underlying cost metric — see
  `docs-ghaw-effective-tokens-specification.md`), or the cost management reference
  (see `docs-ghaw-cost-management.md`).

## Extracted Claims

### Claim 1: Outcomes measure repository state changes after safe outputs land — not workflow self-assessment

- **Evidence**: The opening definition frames outcomes as objective repository-state measurement,
  explicitly positioning them as the evaluation layer that follows safe outputs.
- **Confidence**: settled (first-party authoritative documentation; the definition is the
  foundational claim of the entire reference page)
- **Quote**: "Outcomes describe what happened after a safe output landed in a repository."
- **Our assessment**: This definition establishes outcomes as the measurement counterpart to
  safe outputs. Safe outputs are what workflows *produce* (via the MCP Gateway and Safe Output
  Processor); outcomes are what *happened* to those outputs in the repository (merged, rejected,
  pending, etc.). The measurement is objective — based on repository state — not the workflow's
  self-reported success. For Ch02 (Harness Engineering): practitioners should understand outcomes
  as the downstream evaluation layer of the Safe Outputs architecture, not a separate mechanism.
  For Ch03 (Safety): outcomes provide the post-execution observability that closes the loop on
  whether the workflow's actions were actually accepted.

### Claim 2: Outcome efficiency = effective tokens ÷ accepted outcomes (lower is better)

- **Evidence**: The Outcome Efficiency section defines the formula and its direction explicitly.
- **Confidence**: settled (first-party documentation; the formula is the page's central
  measurement primitive)
- **Quote**: "Outcome efficiency is measured as effective tokens divided by accepted outcomes.
  Lower is better: a lower value means the workflow spent less effective AI work per accepted result."
- **Our assessment**: This is a ratio metric, not an absolute metric. A workflow that produces
  2 accepted outcomes using 1000 ET (efficiency = 500) is more efficient than one that produces
  5 accepted outcomes using 6000 ET (efficiency = 1200). The formula connects the computational
  cost metric (ET, from `docs-ghaw-effective-tokens-specification.md`) to the quality metric
  (accepted outcomes) — giving practitioners a single number to optimize. For Ch04 (Scaling):
  outcome efficiency is the ROI primitive for agentic workflows. For Ch07 (Cost and Observability):
  this metric separates "cheaper because more efficient" from "cheaper because doing less useful
  work" — a critical distinction when evaluating cost-reduction interventions.

### Claim 3: Token and cost data alone are insufficient — outcomes reveal whether efficiency gains are real or just reduced activity

- **Evidence**: The page explicitly states why token data alone is insufficient, and what
  outcomes add.
- **Confidence**: settled (first-party documentation; the framing is the motivation for the
  entire outcomes framework)
- **Quote**: "A workflow can become cheaper because it became more efficient, or because it
  simply did less useful work. Outcomes make that difference visible by relating effective tokens
  to accepted results."
- **Our assessment**: Without outcome tracking, a cost decrease in `gh aw logs` is ambiguous:
  it could mean the workflow got smarter (good) or stopped doing useful work (bad). The outcome
  efficiency metric breaks this ambiguity. For Ch04 (Scaling) and Ch07 (Cost): when evaluating
  cost-reduction interventions — model downgrade, skip-if-match tuning, context limiting —
  practitioners must track outcome efficiency alongside token cost. A cheaper workflow that
  produces fewer accepted outcomes may represent a net loss.

### Claim 4: Six outcome states classify every safe output's final disposition

- **Evidence**: The Outcome States section defines six states with specific per-state definitions.
- **Confidence**: settled (first-party documentation; the state taxonomy is a formal platform
  definition)
- **Quote**: (no single verbatim quote covers all six; see states table in Concrete Artifacts)
- **Our assessment**: The six states form a complete classification scheme. `accepted` and
  `rejected` are terminal states with clear intent. `pending` is semi-terminal — the output
  exists but the evaluation window has not closed. `ignored` is a soft rejection — the output
  was not explicitly rejected but received no follow-up within the evaluation window. `lifecycle`
  and `lifecycle_close` distinguish workflow-initiated closes from lifecycle-bot-initiated closes.
  The distinction between `ignored` and `rejected` is operationally significant: a PR that is
  never reviewed accumulates in `pending` then eventually becomes `ignored`; a PR that is
  explicitly closed by a maintainer becomes `rejected`. For Ch02: practitioners should monitor
  `ignored` and `pending` rates to detect workflows producing outputs nobody acts on.

### Claim 5: Accepted outcomes are the "simplest useful unit" for measuring workflow value — intentionally unweighted

- **Evidence**: The Accepted Outcomes section defines the concept and names concrete examples.
- **Confidence**: settled (first-party documentation; the "simplest useful unit" framing is the
  explicit design rationale)
- **Quote**: "An accepted outcome is the simplest useful unit for measuring workflow effectiveness.
  Typical examples include merged pull requests, issues that remained relevant and were completed,
  and labels or comments that stuck and were acted on."
- **Our assessment**: The "simplest useful unit" framing is intentional — each accepted outcome
  counts equally, regardless of the size of the PR, complexity of the issue, or impact of the
  label. A merged 1-line fix counts the same as a merged 500-line feature. This flat-weight
  design avoids value-weighting that would require subjective judgment. For Ch04: the flat-weight
  design means teams should not use accepted outcome counts as a proxy for business value — they
  need separate domain-specific value measurement. Accepted outcomes measure *that* work was
  accepted, not *how much* value the accepted work delivered.

### Claim 6: Safe output types have varying acceptance evaluation coverage — some type-specific rules, some fallback rules, some with no rule yet

- **Evidence**: The Accepted Outcomes section describes categories of rule coverage across safe
  output types, distinguishing dedicated rules, limited checks, fallback rules, and types with
  no implemented rule yet.
- **Confidence**: settled (first-party documentation; the rule coverage taxonomy is explicit
  in the page)
- **Quote**: (no direct single-sentence quote; see Concrete Artifacts for the category
  descriptions)
- **Our assessment**: The uneven rule coverage has operational implications. Workflows that rely
  heavily on safe output types in the "no rule yet" category (such as certain discussion and
  review comment operations) will not have meaningful acceptance metrics — those outputs will
  not be classified as accepted or rejected. This affects interpretation of outcome efficiency
  numbers: a workflow whose primary output type has no outcome rule will appear to have zero
  accepted outcomes regardless of actual effectiveness. Practitioners should understand the
  coverage map before relying on outcome efficiency as a performance signal.

### Claim 7: Outcome data flows through OpenTelemetry spans at two granularities — per-item detailed fields and workflow-level rollup summaries

- **Evidence**: The Telemetry section describes the OTel integration and what data is available
  at each level.
- **Confidence**: settled (first-party documentation; specific span types and fields are
  described authoritatively)
- **Quote**: "Workflow-level rollups such as accepted counts and acceptance rate are emitted on
  outcome summary or conclusion spans, and per-item spans can carry more detailed fields such as
  object type, URL, comments, review activity, and zero-touch acceptance."
- **Our assessment**: The two-tier telemetry model (workflow rollup + per-item detail) is
  well-designed for observability. Workflow-level spans enable fleet monitoring (is this workflow
  still effective overall?); per-item spans enable debugging specific accepted/rejected outputs
  (why was this PR rejected? What was the review activity?). The "zero-touch acceptance" field
  in per-item spans is notable — it captures whether an output was accepted without any human
  interaction (e.g., auto-merged), which is relevant for autonomy level assessment. For Ch03
  (Safety): per-item span data is the audit trail for understanding exactly what happened to
  each safe output. For Ch07 (Observability): the OTel integration makes outcome data queryable
  from standard observability tooling alongside cost and trace data.

### Claim 8: Outcome information appears in OpenTelemetry spans and related artifacts

- **Evidence**: The Telemetry section's opening description.
- **Confidence**: settled (first-party documentation)
- **Quote**: "Outcome information appears in OpenTelemetry spans and related artifacts."
- **Our assessment**: The phrase "related artifacts" extends the telemetry integration beyond
  pure OTel to include other gh-aw artifacts (Safe Output NDJSON records, run summaries).
  Outcome data is queryable from both the OTel stack (fleet-level dashboards) and the gh-aw
  CLI (`gh aw logs`, `gh aw audit`) for per-run investigation.

### Claim 9: Three rollup levels handle both simple and orchestrated workflows — run, episode, and workflow totals

- **Evidence**: The Cost and Rollups section defines three levels and their use cases.
- **Confidence**: settled (first-party documentation; the three levels are explicitly defined
  with specific guidance on when each applies)
- **Quote** (on episodes): "For orchestrated workflows, multiple runs can belong to one logical
  execution. In that case, the more meaningful unit is the episode."
- **Quote** (on aggregation): "Outcome and cost totals can be rolled up from runs into episodes
  using simple sums, and then from episodes into workflow totals and repository totals."
- **Our assessment**: The episode concept is significant for multi-run orchestrated workflows
  (e.g., a workflow that spawns multiple worker runs via `dispatch-workflow`). Measuring each
  worker run independently misses the overall effectiveness of the orchestration — the episode
  aggregates all runs belonging to one logical execution. For Ch04 (Multi-Agent Orchestration):
  practitioners should track outcome efficiency at the episode level for orchestrated workflows,
  not per-run — otherwise the metric captures only a fraction of the total work and distorts
  the efficiency signal.

### Claim 10: The recommended basic dashboard requires five metrics — total effective tokens, total accepted outcomes, efficiency ratio, trend over time, and workflow ranking

- **Evidence**: The Cost and Rollups section specifies the recommended dashboard composition.
- **Confidence**: settled (first-party documentation; the five metrics are explicitly listed as
  the foundational measurement set)
- **Quote**: "total effective tokens, total accepted outcomes, effective tokens per accepted
  outcome, a trend over time, and a workflow ranking by effective tokens per accepted outcome."
- **Our assessment**: The five metrics form a coherent dashboard for multi-workflow deployments:
  total ET and accepted outcomes are the raw quantities; the efficiency ratio is the derived
  quality metric; trend over time enables regression detection; workflow ranking enables
  cross-workflow comparison. The workflow ranking dimension is particularly useful for
  organizations running many workflows — it surfaces which workflows are most and least
  efficient, guiding where to invest optimization effort. For Ch04 (Scaling): this five-metric
  dashboard is the implementation-ready starting point for any gh-aw observability deployment.

### Claim 11: The outcomes framework explicitly declines to estimate business value, replace human judgment, combine cost types, or solve duplicate-work analysis

- **Evidence**: The Cost and Rollups section explicitly lists what the framework does NOT do.
- **Confidence**: settled (first-party documentation; the scope limitations are explicitly
  enumerated)
- **Quote**: "does not try to estimate the full business value of a workflow, replace human
  judgment for nuanced quality questions, combine deterministic compute cost and inference cost
  into one synthetic score, or solve overlap and duplicate-work analysis."
- **Our assessment**: The explicit scope limitations are valuable guidance. Accepted outcomes
  count equally regardless of value, and business value estimation is deliberately out of scope.
  Teams needing value-weighted metrics must build them on top of the raw outcome data. The refusal
  to combine compute cost (Actions minutes) and inference cost (ET) into one synthetic score is
  architecturally consistent with the cost management reference (`docs-ghaw-cost-management.md`
  Claim 1), which documents the two cost components as independently manageable. For Ch04:
  practitioners must understand that outcome efficiency ≠ business ROI; the latter requires
  additional domain-specific instrumentation.

## Concrete Artifacts

### Six Outcome State Definitions (verbatim from source)

```
accepted:        "The result was kept, merged, completed, or otherwise accepted by the
                  repository state."
rejected:        "The result was explicitly undone, closed, removed, or not accepted."
pending:         "The result exists, but has not reached a terminal state yet."
ignored:         "The result received no meaningful follow-up within the evaluation window."
lifecycle:       "Closed or removed by the workflow itself as part of its normal operation"
lifecycle_close: "A `close_issue` or `close_pull_request` output where the close actor
                  was a lifecycle bot"
```

*Source: https://github.github.com/gh-aw/reference/outcomes, "Outcome States" section*

### Outcome Efficiency Formula (verbatim from source)

```
Outcome efficiency = effective_tokens ÷ accepted_outcomes

"Outcome efficiency is measured as effective tokens divided by accepted outcomes.
Lower is better: a lower value means the workflow spent less effective AI work
per accepted result."
```

*Source: https://github.github.com/gh-aw/reference/outcomes, "Outcome Efficiency" section*

### Basic Measurement Dashboard (verbatim from source)

```
Recommended five-metric dashboard:
  1. total effective tokens
  2. total accepted outcomes
  3. effective tokens per accepted outcome
  4. a trend over time
  5. a workflow ranking by effective tokens per accepted outcome
```

*Source: https://github.github.com/gh-aw/reference/outcomes, "Cost and Rollups" section*

### Rollup Hierarchy (verbatim from source)

```
Run:      "For simple workflows, a single run is usually the right unit for
           outcome measurement."
Episode:  "For orchestrated workflows, multiple runs can belong to one logical
           execution. In that case, the more meaningful unit is the episode."
Rollup:   "Outcome and cost totals can be rolled up from runs into episodes
           using simple sums, and then from episodes into workflow totals and
           repository totals."
```

*Source: https://github.github.com/gh-aw/reference/outcomes, "Cost and Rollups" section*

### Accepted Outcomes Definition (verbatim from source)

```
"An accepted outcome is the simplest useful unit for measuring workflow effectiveness.
Typical examples include merged pull requests, issues that remained relevant and were
completed, and labels or comments that stuck and were acted on."
```

*Source: https://github.github.com/gh-aw/reference/outcomes, "Accepted Outcomes" section*

### Safe Output Type Outcome Rule Coverage Categories

```
Categories of acceptance evaluation coverage (from source):
  - Dedicated rules (type-specific): PR merges, issue completion, comment engagement,
    reviewer actions — type-specific acceptance logic
  - Limited checks: label retention evaluation
  - Fallback rules (generic existence): discussion updates, project modifications —
    generic existence-based acceptance
  - No rules yet: certain discussion and review comment operations

Note: Types with no implemented rule produce outputs that cannot be classified as
accepted or rejected, affecting outcome efficiency calculations for those workflows.
```

*Source: https://github.github.com/gh-aw/reference/outcomes, "Accepted Outcomes" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-effective-tokens-specification.md` Claim 1 (ET normalizes token counts
    across token classes and models as a computational intensity metric, distinct from
    billing): Outcome efficiency (this source Claim 2) uses ET as its numerator — the two
    specs are designed as complementary metrics. ET measures computational intensity;
    accepted outcomes measure useful work; the ratio is efficiency. Both specs are from
    the same team using the same ET definition.
  - `docs-ghaw-cost-management.md` Claim 1 (cost of running a gh-aw workflow = Actions
    minutes + inference costs, as two independently manageable components): This source's
    Claim 11 explicitly declines to combine the two cost components into one synthetic score —
    consistent with the cost management reference keeping Actions minutes and inference
    separate. Both sources treat the two-component cost model as a deliberate design decision.
  - `docs-ghaw-safe-rollout.md` Claim 7 (persist what the workflow predicted at decision
    time — prediction snapshots must be explicit, not reconstructed from logs): The outcomes
    rollup hierarchy (Claim 9) and per-item OTel spans (Claim 7) are the persistent records
    of accepted vs. rejected outputs across runs and episodes — the data structures that make
    safe rollout's before/after comparison possible. The rollout guide's design rule about not
    reconstructing predictions from logs aligns with the outcomes framework's explicit per-item
    span data.

- **Extends**:
  - `docs-ghaw-safe-outputs-specification.md`: Safe outputs define the *production* side
    (what workflows write, with the seven-stage validation pipeline); outcomes define the
    *evaluation* side (what happened to those writes in the repository). The two references
    together form the complete Safe Outputs lifecycle. Notably, the provenance metadata
    requirement SP5 from the spec ("All created GitHub resources MUST include provenance
    metadata identifying workflow source and run") is what enables outcome attribution to
    specific workflow runs — without provenance, the outcome measurement system cannot
    identify which run produced which accepted or rejected output.
  - `docs-ghaw-cost-management.md`: The cost management reference covers `gh aw logs` and
    `gh aw audit` for cost monitoring. The outcomes framework adds the acceptance dimension.
    Practitioners should combine cost monitoring (is this expensive?) with outcome monitoring
    (is this effective?) to get a complete picture of workflow health. Outcome efficiency is
    the ratio that connects the two monitoring surfaces.
  - `docs-ghaw-agentic-ops.md` Claim 1 (Agentic Ops pattern monitors workflow cost and
    failure anomalies via scheduled meta-agent): The Agentic Ops pattern monitors cost and
    failures; the outcomes framework extends the monitoring surface to acceptance rates. A
    workflow that generates many safe outputs but has a high `rejected` or `ignored` rate
    needs attention even if its cost metrics look healthy. Acceptance rate (available via
    workflow-level OTel spans, Claim 7) should be a first-class Agentic Ops monitoring
    target alongside cost and failure rate.

- **Contradicts**: None identified. The outcomes framework is additive to the corpus. No
  existing note claims that token/cost data alone is sufficient for workflow evaluation,
  and no existing note defines outcome states or efficiency in any conflicting way. The
  cost management reference's two-component cost model is fully consistent with this
  source's refusal to combine cost types.

- **Novel** (what this note adds that no prior source covers):
  - **Six-state outcome taxonomy** (Claim 4): No existing corpus note defines outcome states.
    The `ignored`, `lifecycle`, and `lifecycle_close` distinctions are entirely new.
  - **Outcome efficiency as a formal metric** (Claim 2): No existing note defines outcome
    efficiency as effective tokens ÷ accepted outcomes. `docs-ghaw-effective-tokens-specification.md`
    defines ET; this page defines how to use ET in a ratio with accepted outcomes.
  - **The efficiency/activity ambiguity** (Claim 3): The framing that a cost decrease could
    mean "more efficient" or "less useful work" is the key insight motivating the outcomes
    framework. No existing note articulates this ambiguity or offers a metric to resolve it.
  - **Accepted outcomes as the "simplest useful unit" with intentional flat weighting** (Claim 5):
    The design choice to count all accepted outcomes equally, rejecting business value weighting,
    is new to the corpus.
  - **Episode as the measurement unit for orchestrated workflows** (Claim 9): The episode
    concept — grouping multiple runs into a logical execution unit — is new to the corpus and
    important for multi-agent orchestration cost attribution.
  - **Five-metric basic dashboard specification** (Claim 10): The specific five-metric
    dashboard recommendation is new to the corpus.
  - **Explicit outcome framework scope limitations** (Claim 11): The named exclusions
    (business value estimation, human judgment replacement, unified cost score, duplicate
    analysis) are new to the corpus and help practitioners understand what they must build
    themselves vs. what the platform provides.
  - **Zero-touch acceptance as a per-item telemetry field** (Claim 7): The existence of a
    `zero-touch acceptance` field in per-item OTel spans — capturing whether an output was
    accepted without human interaction — is new to the corpus and relevant for autonomy
    level assessment.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add outcome monitoring as a first-class component of gh-aw harness design, alongside
    cost monitoring. Practitioners who only monitor `gh aw logs` cost data miss the
    effectiveness dimension. The five-metric dashboard (Claim 10) is the implementation
    starting point.
  - Document the `ignored` and `pending` outcome states as monitoring targets — high
    `ignored` rates indicate the workflow is producing outputs nobody acts on; persistent
    `pending` accumulation indicates evaluation windows are not closing.
  - Note safe output type rule coverage: workflows relying on types with no outcome rule
    will not get meaningful acceptance metrics. This affects harness design decisions about
    which safe output types to prioritize.

- **Chapter 03 (Safety and Verification)**:
  - Add outcome states (Claim 4) as the post-execution observability primitive that closes
    the Safe Outputs lifecycle: safe output produced → validated by seven-stage pipeline →
    outcome classified in repository state. The per-item OTel span data (Claim 7) is the
    audit trail for this lifecycle.
  - The `zero-touch acceptance` field in per-item spans (Claim 7) warrants attention — workflows
    with consistently high zero-touch acceptance rates are being trusted without human review,
    which may warrant additional scrutiny as part of safe rollout evaluation.

- **Chapter 04 (Scaling / Multi-Agent Orchestration)**:
  - Add outcome efficiency (Claim 2) as the primary ROI metric for scaled gh-aw deployments.
    When evaluating whether to scale up a workflow or retire it, outcome efficiency is the key
    number — not token cost alone.
  - Add the episode concept (Claim 9) as the measurement unit for orchestrated multi-run
    workflows. Track outcome efficiency at episode level for orchestrated workflows, not per-run.
  - Add the scope limitation caveat (Claim 11): outcome efficiency ≠ business ROI.
    The platform measures accepted outcomes; business value requires domain-specific
    instrumentation on top of the platform metrics.

- **Chapter 07 (Cost and Observability)**:
  - Ch07 currently covers cost monitoring (via `docs-ghaw-cost-management.md`) and ET
    measurement (via `docs-ghaw-effective-tokens-specification.md`). Add outcome efficiency
    as the third leg of the observability triad: cost (what did it spend?) → ET (how much
    compute per run?) → outcome efficiency (how much compute per accepted result?).
  - The five-metric dashboard (Claim 10) provides the implementation-ready starting point.
  - The OTel integration (Claims 7-8) makes outcome data queryable from the same tooling
    as trace and cost data — the existing OTel infrastructure in the harness already
    collects it.

## Extraction Notes

1. **WebFetch content via AI model**: The gh-aw documentation is served as an Astro/Starlight
   SPA. The WebFetch tool processes HTML through an AI model before returning results. Four
   fetch passes were made with different prompts to triangulate verbatim wording. Quotes are
   drawn from passes that returned specific verbatim text consistently. The outcome state
   definitions, outcome efficiency formula, accepted outcomes definition, rollup hierarchy,
   and telemetry integration description were returned consistently across passes.

2. **Safe output type counts**: The first and third fetch passes returned different counts
   for the number of safe output types covered by outcome rules (27 vs. 23). This inconsistency
   likely reflects variation in how the AI model summarized the table. Specific type counts
   were not cited in this source note to avoid propagating an inaccurate number. The category
   structure (dedicated, limited, fallback, no rules) was consistent across passes and is the
   more reliable information.

3. **No contradictions filed**: Reviewed all gh-aw source notes. No claims in this source
   materially oppose any existing note. The two-component cost non-combination (Claim 11) is
   consistent with the cost management reference. The ET usage in the efficiency formula is
   consistent with the ET specification. No contradiction issue required.

4. **Related page links not followed**: The source's "Related Documentation" section links to
   safe outputs, effective tokens, cost management, and telemetry reference pages. The safe
   outputs and effective tokens references are already covered by corpus notes. The telemetry
   reference was not followed — it likely covers OTel configuration in detail that would
   warrant a separate source note if the guide's observability chapters need that level of
   instrumentation detail.
