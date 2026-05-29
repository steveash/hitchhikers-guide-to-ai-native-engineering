---
source_url: https://github.github.com/gh-aw/reference/measuring-impact
source_type: docs
title: "GitHub Agentic Workflows: Measuring Impact"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-29
last_checked: 2026-05-29
status: current
confidence_overall: emerging
issue: "#990"
---

# GitHub Agentic Workflows: Measuring Impact

> First-party reference documentation introducing a practical measurement
> framework for agentic workflows — a four-layer metric model (operational,
> cost-efficiency, outcome, long-term impact), explicit guidance on the
> timing gap between cost signals (early) and outcome signals (delayed), a
> concrete waste taxonomy, and the principle of not collapsing metrics into
> a single synthetic score.

## Source Context

- **Type**: docs (GitHub Agentic Workflows `reference/measuring-impact` page —
  in the "Reference" section, alongside `reference/cost-management` and
  `reference/rate-limiting-controls`. Reference pages document platform
  practices precisely; this one covers measurement strategy and impact
  evaluation rather than billing mechanics or rate controls.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind the `gh aw` CLI and Peli de Halleux's "Agent Factory"
  blog series. Authoritative for the `gh aw` platform. Measurement model and
  metric definitions reflect the team's production experience operating
  agent fleets at scale. Claims generalize to non-`gh-aw` systems at the
  strategic level; specific tool references (`gh aw logs`, Outcomes model)
  are platform-specific.
- **Scope**: Covers the measurement philosophy (cost vs. outcome timing,
  multi-layer vs. single-score), the recommended starting metric set, the
  four-layer taxonomy with descriptions, the three recommended measurement
  tools, waste identification and remediation, and trend-based monitoring
  guidance. Does NOT cover: billing mechanics (see `docs-ghaw-cost-management.md`),
  monitoring configuration primitives (see `docs-ghaw-monitoring-patterns.md`),
  the three-tier observability architecture (see `blog-ghaw-agent-observability.md`),
  or implementation of automated monitoring workflows.

## Extracted Claims

### Claim 1: Measuring agentic workflow impact requires using early cost signals alongside later outcome signals, and explicitly not collapsing them into a single score

- **Evidence**: Opening framing of the measurement approach — the core
  prescriptive principle from which all other guidance in the source derives.
  The emphasis on not collapsing into a single score is explicit and repeated.
- **Confidence**: emerging (first-party documentation; the principle is stated
  as design guidance, not backed by production A/B evidence)
- **Quote**: "Measure impact by using **early cost signals** alongside **later
  outcome signals**. Do not try to collapse them into a single score."
- **Our assessment**: The anti-collapse principle addresses a real practitioner
  failure mode: computing a single "value score" by combining cost and outcome
  data obscures the timing mismatch and produces a misleading composite. A
  workflow can show low cost (immediately visible) but poor outcomes (visible
  only weeks later) — or vice versa. Keeping them separate forces practitioners
  to reason explicitly about each dimension. The "do not collapse" instruction
  is uncommon in metrics guidance, which typically pushes toward composite
  KPIs. For Ch05 (Team Adoption): when teaching teams to measure ROI, lead
  with this principle — present cost and outcome metrics as separate dashboards
  with separate interpretation cadences, not a combined score.

### Claim 2: Cost signals arrive early and are usually immediately available, while outcome signals are delayed and downstream

- **Evidence**: The source articulates the timing asymmetry explicitly, giving
  it as the reason to track cost and outcomes in separate metric layers.
- **Confidence**: settled (first-party documentation; the timing gap is a
  structural property of how agentic systems work — cost is metered
  immediately by the platform; outcomes require humans to accept, merge,
  or otherwise act on agent output)
- **Quote**: "Cost estimates are usually available early, while accurate cost
  measurement often arrives later." and "Outcomes are often delayed and
  downstream."
- **Our assessment**: The timing asymmetry is the strategic insight that
  justifies the entire framework. Comments may take days to receive
  responses, code changes only matter once merged, issues only create
  value upon resolution. In the early deployment phase, practitioners
  only have cost data to act on — which is why understanding its relationship
  to eventual outcomes matters. For Ch05: the timing gap argument is the
  principal reason teams should not make early "kill or keep" decisions about
  agentic workflows based purely on cost signals — outcomes may not yet be
  visible. Frame cost-only monitoring as an early-warning system, not a
  verdict mechanism.

### Claim 3: The foundational dashboard for most teams should include run volume, execution success, Actions minutes, inference cost, useful output rate, and acceptance over time

- **Evidence**: Described as "the best starting point" for most teams — a
  concrete metric set teams can implement immediately before building more
  sophisticated instrumentation.
- **Confidence**: emerging (first-party recommendation; framed as a practical
  starting point rather than an empirically validated minimum set)
- **Quote**: "For most teams, the best starting point is a small set of direct
  metrics: run volume, execution success, Actions minutes, inference cost,
  useful output rate, and acceptance over time."
- **Our assessment**: The six-metric starter kit gives practitioners a concrete
  implementation target rather than a vague instruction to "measure things."
  Notably it spans both cost-side (Actions minutes, inference cost) and
  outcome-side (useful output rate, acceptance over time) dimensions, reflecting
  the core timing-separation principle. For Ch02 (Harness Engineering): recommend
  this six-metric set as the minimum observable surface any agentic workflow
  deployment should instrument before launch.

### Claim 4: A more complete metric set for ongoing monitoring includes run count, completion rate, retries, duration, cost per successful run, useful output rate, acceptance rate, and time to adoption

- **Evidence**: Described alongside the foundational starter set as a fuller
  metric list for teams moving beyond initial instrumentation.
- **Confidence**: emerging (first-party recommendation; the fuller list extends
  the starter set with operational depth metrics like retries, duration, and
  time to adoption)
- **Quote**: "run count, completion rate, retries, duration, cost per
  successful run, useful output rate, acceptance rate, and time to adoption."
- **Our assessment**: The expanded metric list adds two important dimensions
  absent from the starter set: operational health signals (retries, completion
  rate) and adoption velocity (time to adoption). "Time to adoption" is
  particularly interesting — it measures how quickly users engage with agent
  output, which is a proxy for both output quality and workflow integration
  into team practice. For Ch05: "time to adoption" as a metric is novel to the
  corpus and should be highlighted; a low acceptance rate with a long time to
  adoption signals friction in the human-agent handoff, not just output quality.

### Claim 5: Four metric layers — operational, cost-efficiency, outcome, and long-term impact — provide better diagnostic clarity than any single metric or composite score

- **Evidence**: The source explicitly defines and names four distinct layers,
  each addressing a different measurement question about the workflow's
  performance.
- **Confidence**: emerging (first-party documentation; the four-layer framework
  is prescriptive design guidance from the team that operates the platform)
- **Quote**: "Use a small set of metric layers instead of one synthetic impact
  formula."
- **Our assessment**: The four-layer structure is the operationalization of
  the anti-collapse principle from Claim 1. Rather than a formula, practitioners
  maintain four distinct views, each answering a different question. This is
  architecturally cleaner than composite KPIs and allows teams to improve one
  layer without obscuring regressions in others. For Ch05: the four-layer
  taxonomy should be the organizing framework for the measurement section —
  each layer deserves its own dashboard/cadence discussion.

### Claim 6: Operational metrics tell you whether the workflow runs reliably

- **Evidence**: First of the four layers described in the source, defined as
  addressing reliability as the foundational question.
- **Confidence**: emerging (first-party definition within the four-layer framework)
- **Quote**: "tell you whether the workflow runs reliably"
- **Our assessment**: Reliability is the prerequisite layer — if the workflow
  does not run reliably (high failure rates, frequent retries, inconsistent
  completion), the other layers are noise. This maps to traditional software
  SLO/SLA thinking but applied to agentic runs rather than HTTP requests.
  Relevant metrics: run count, completion rate, retry rate, duration. For Ch02:
  operational metrics are the "is it working?" layer and should be the first
  dashboard teams set up.

### Claim 7: Cost-efficiency metrics tell you what useful execution costs

- **Evidence**: Second of the four layers, defined as addressing the cost
  side of the measurement problem.
- **Confidence**: emerging (first-party definition within the four-layer framework)
- **Quote**: "tell you what useful execution costs"
- **Our assessment**: The phrasing "what useful execution costs" (not just
  "what execution costs") is precise: cost efficiency is measured against
  useful output, not total output. A workflow that runs 100 times but only
  20 times produce accepted output has a 5× cost inefficiency on the useful-
  execution basis. The "cost per successful run" metric from Claim 4 directly
  operationalizes this. For Ch03 (Safety and Verification): cost efficiency
  is a safety signal — sustained cost inefficiency (high spend per useful
  output) may indicate the workflow is failing silently, producing output
  that looks complete but is rejected downstream.

### Claim 8: Outcome metrics tell you whether the workflow produced something that mattered

- **Evidence**: Third of the four layers, defined as addressing actual impact
  on the work being done.
- **Confidence**: emerging (first-party definition within the four-layer framework)
- **Quote**: "tell you whether the workflow produced something that mattered"
- **Our assessment**: "Mattered" is the key word — it distinguishes output
  (something was produced) from impact (the output changed something in the
  world). Acceptance rate is the primary operationalization: was the PR
  merged? Was the comment acted on? Was the issue resolved using the
  suggested approach? The timing gap from Claim 2 applies most directly
  here: outcome metrics take the longest to materialize. For Ch05: outcome
  metrics are the lagging indicators teams must wait for; warn practitioners
  against abandoning workflows that have good operational and cost-efficiency
  metrics but whose outcome metrics have not yet accumulated enough data.

### Claim 9: Long-term impact metrics tell you whether the workflow improved the broader system

- **Evidence**: Fourth of the four layers, explicitly framed as the
  system-level question beyond individual workflow runs.
- **Confidence**: emerging (first-party definition; this is the hardest layer
  to instrument and the source provides the least implementation detail for it)
- **Quote**: "tell you whether the workflow improved the broader system"
- **Our assessment**: Long-term impact is the hardest layer to measure and
  the most strategically important. "Improved the broader system" might mean:
  did code quality metrics improve after the review agent was deployed? Did
  time-to-merge decrease after the triage agent was deployed? These require
  comparing system state before and after at a granularity that requires
  dedicated measurement infrastructure. The source names OpenTelemetry and
  the Outcomes model as tools for this layer. For Ch05: position long-term
  impact as the "mature phase" metrics — teams should begin tracking them
  early but expect meaningful signal only after months of operation.

### Claim 10: `gh aw logs` covers the run and cost side of measurement; the Outcomes model covers the downstream acceptance side; OpenTelemetry covers repository-wide or organization-wide trends

- **Evidence**: Described as the three recommended instrumentation paths
  for the measurement framework — each serves a different layer of the
  four-layer taxonomy.
- **Confidence**: emerging (first-party documentation; these are the platform's
  built-in instrumentation tools)
- **Quote**: "gives you the run and cost side" (for `gh aw logs`);
  "downstream acceptance side" (for Outcomes model); referenced alongside
  OpenTelemetry "for repository-wide or organization-wide trends."
- **Our assessment**: The three-tool instrumentation stack maps naturally
  to the measurement layers: `gh aw logs` → operational + cost-efficiency
  layers; Outcomes model → outcome layer; OpenTelemetry → long-term impact
  layer. Notably, `gh aw logs` appears here as a measurement tool with
  a different framing than in `docs-ghaw-cost-management.md` (where it is
  framed as cost monitoring) and `docs-ghaw-monitoring-patterns.md` (where
  it is framed as operational inspection). All three framings are consistent —
  `gh aw logs` is a multi-purpose tool that serves different measurement
  questions depending on context. For Ch02: document all three framings
  together so practitioners know which question each invocation is answering.

### Claim 11: System waste is any cost, time, or reviewer attention that does not produce proportional value; common sources include redundant runs, duplicate outputs, repeated context collection, expensive model calls for deterministic work, and outputs with consistently low usage

- **Evidence**: Explicit waste definition and taxonomy from the source,
  framed as a system-level concern that individual workflow metrics can miss.
- **Confidence**: emerging (first-party definition; framed as design guidance)
- **Quote**: "Waste is any cost, time, or reviewer attention that does not
  produce proportional value. Common sources include redundant runs, duplicate
  outputs, repeated context collection, expensive model calls for deterministic
  work, and outputs with consistently low usage or acceptance."
- **Our assessment**: The waste taxonomy is the most operationally specific
  content in the source. "Reviewer attention" as a waste category is
  particularly important — it acknowledges that human review time is a
  real cost even when not captured in billing. A workflow that produces
  outputs that humans ignore or reject wastes not just compute but human
  attention. The five waste sources map to specific remediation strategies
  (Claim 12). For Ch02: the waste taxonomy should inform workflow design
  review — each waste source corresponds to a design smell worth checking
  at deployment review time.

### Claim 12: The standard remediation for waste is consolidating overlapping workflows, sharing intermediate artifacts, caching stable context, and moving deterministic work out of the agent path

- **Evidence**: Listed as the "typical fixes" for the waste sources identified
  in Claim 11 — a concrete remediation map matching each waste class.
- **Confidence**: emerging (first-party recommendations; framed as typical
  approaches rather than proven interventions with measured results)
- **Quote**: "consolidating overlapping workflows, sharing intermediate
  artifacts, caching stable context, and moving deterministic work out of
  the agent path"
- **Our assessment**: The "moving deterministic work out of the agent path"
  fix is the strongest of the four — it corresponds to the `skip-if-match`
  pattern from `docs-ghaw-cost-management.md` Claim 5 and the broader
  deterministic pre-check patterns in `docs-ghaw-deterministic-agentic-patterns.md`.
  "Caching stable context" maps to the memory/context management patterns
  elsewhere in the corpus. "Consolidating overlapping workflows" requires
  the system-level visibility from Claim 9 (long-term impact layer) to
  detect in the first place — an individual workflow looks fine; only a
  fleet-level view reveals the overlap. For Ch02: pair this remediation list
  with the waste taxonomy as a diagnostic → fix table.

### Claim 13: Trend data is more useful than single numbers; the target trends are cost per successful run decreasing, useful output rate and acceptance increasing, retries dropping, and system overlap decreasing

- **Evidence**: Explicit monitoring guidance, framed as an anti-pattern
  (reacting to single numbers) and a positive target state (directional
  trends).
- **Confidence**: emerging (first-party guidance; the directional targets
  are logical derivations from the metric definitions rather than empirically
  calibrated thresholds)
- **Quote**: "Do not overreact to single numbers. Trend data is usually more
  useful. Look for cost per successful run moving down, useful output rate and
  acceptance moving up, retries dropping, and system overlap decreasing."
- **Our assessment**: The explicit anti-pattern ("do not overreact to single
  numbers") is operationally important. A single expensive run or a single
  low-acceptance run carries little signal; a persistent trend in either
  direction is actionable. The four target trends map directly to the four
  metric layers: cost per successful run (cost-efficiency), useful output
  rate/acceptance (outcome), retries (operational), system overlap (long-term
  impact). For Ch05: this trend framing is the right mindset for teams
  reviewing agentic workflow health — present it as a monthly trend review
  discipline rather than a per-run alert discipline.

## Concrete Artifacts

### Core Measurement Principle (verbatim from source)

```
"Measure impact by using early cost signals alongside later outcome signals.
Do not try to collapse them into a single score."
```

*Source: https://github.github.com/gh-aw/reference/measuring-impact, opening measurement principle*

### Foundational Metric Dashboard (verbatim from source)

```
Starting metrics for most teams:
  run volume, execution success, Actions minutes, inference cost,
  useful output rate, and acceptance over time

Expanded metric set:
  run count, completion rate, retries, duration, cost per successful run,
  useful output rate, acceptance rate, and time to adoption
```

*Source: https://github.github.com/gh-aw/reference/measuring-impact, "Starting Metrics" section*

### Four Metric Layers (verbatim descriptions from source)

```
Layer 1 — Operational metrics:
  "tell you whether the workflow runs reliably"

Layer 2 — Cost-efficiency metrics:
  "tell you what useful execution costs"

Layer 3 — Outcome metrics:
  "tell you whether the workflow produced something that mattered"

Layer 4 — Long-term impact metrics:
  "tell you whether the workflow improved the broader system"
```

*Source: https://github.github.com/gh-aw/reference/measuring-impact, "Metric Layers" section*

### System Waste Taxonomy (verbatim from source)

```
Definition:
  "Waste is any cost, time, or reviewer attention that does not produce
  proportional value."

Common waste sources:
  "redundant runs, duplicate outputs, repeated context collection,
  expensive model calls for deterministic work, and outputs with
  consistently low usage or acceptance"

Typical fixes:
  "consolidating overlapping workflows, sharing intermediate artifacts,
  caching stable context, and moving deterministic work out of the
  agent path"
```

*Source: https://github.github.com/gh-aw/reference/measuring-impact, "System Waste" section*

### Trend Monitoring Guidance (verbatim from source)

```
"Do not overreact to single numbers. Trend data is usually more useful.
Look for cost per successful run moving down, useful output rate and
acceptance moving up, retries dropping, and system overlap decreasing."
```

*Source: https://github.github.com/gh-aw/reference/measuring-impact, "Monitoring Trends" section*

### Recommended Instrumentation Stack

```
Tool: gh aw logs
Purpose: "gives you the run and cost side"
Covers: operational metrics + cost-efficiency metrics

Tool: Outcomes model
Purpose: "downstream acceptance side"
Covers: outcome metrics

Tool: OpenTelemetry
Purpose: repository-wide or organization-wide trends
Covers: long-term impact metrics
```

*Source: https://github.github.com/gh-aw/reference/measuring-impact, "Measurement Tools" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-cost-management.md` Claim 4 (`gh aw logs` is the primary
    cost-monitoring command): this source confirms `gh aw logs` as the
    run-and-cost measurement tool, consistent with the cost management
    reference. Both framings co-exist: cost management frames it as spend
    control; measuring impact frames it as the cost side of the measurement
    framework. The two uses are complementary.
  - `docs-ghaw-cost-management.md` Claim 5 (`skip-if-match` as the highest-
    leverage cost control): Claim 12 of this source names "moving deterministic
    work out of the agent path" as the primary waste remediation — the
    conceptual equivalent of `skip-if-match`. Both sources converge on the
    same design principle from different angles: cost management as a budget
    mechanism, measuring impact as a waste identification mechanism.
  - `blog-ghaw-agent-observability.md` Claim 1 ("Observability isn't optional
    when you're running dozens of AI agents"): this source's measurement
    framework is the strategic complement to that architectural thesis. The
    observability architecture provides the infrastructure; this source defines
    what to measure and how to interpret it. Both are necessary.
  - `docs-ghaw-monitoring-patterns.md` Claim 7 (`gh aw audit` for per-run
    operational inspection): that note covers the practitioner CLI tools for
    investigation; this source provides the higher-level question those tools
    should answer. The monitoring patterns are the toolbox; the measuring
    impact framework is the checklist for how to use it.

- **Extends**:
  - `blog-ghaw-agent-observability.md`: that note documents the three-tier
    observability *architecture* (performance, cost, audit) and its production
    implementation metrics. This source adds the *measurement strategy* layer —
    when to expect which signals, how to layer metrics, and what trends to
    target. The two together give the complete picture: build the observatory
    (blog), then know what to measure with it (this source).
  - `docs-ghaw-cost-management.md`: that source covers cost billing mechanics,
    trigger-type risk, and cost-reduction strategies. This source adds the
    strategic framing: cost metrics are early signals that must be interpreted
    alongside later outcome signals. The cost management reference answers "how
    do I reduce cost?"; this source answers "how do I know if cost is worth the
    outcome?"
  - `docs-ghaw-monitoring-patterns.md`: that source covers configuration
    primitives for failure reporting, Projects v2 integration, and CLI inspection.
    This source adds the strategic question layer: what are we monitoring *for*,
    and what do the trends mean? The monitoring patterns provide the config;
    this source provides the framework for interpreting what that config collects.

- **Contradicts**: None identified. The four-layer taxonomy in this source does
  not contradict the three-tier observability architecture in
  `blog-ghaw-agent-observability.md` — they are orthogonal decompositions.
  The blog post decomposes *who monitors* (Metrics Collector, Portfolio Analyst,
  Audit Workflows); this source decomposes *what questions metrics answer*
  (reliability, cost-efficiency, outcomes, system impact). Both frameworks
  coexist without conflict.

- **Novel** (what this note adds that no prior source covers):
  - **Timing gap principle** (Claims 1–2): The explicit articulation that cost
    signals are early and outcome signals are delayed — and that this timing
    difference requires keeping them in separate metric layers — is not
    documented in any existing source note. Prior corpus sources describe *what*
    to measure; this is the first to address *when* different signals become
    available and how to reason about the gap.
  - **Anti-collapse principle** (Claim 1): The explicit guidance "do not try
    to collapse them into a single score" is new. No existing source note
    warns against composite KPIs for agentic workflows.
  - **Four metric layer taxonomy with definitions** (Claims 5–9): The named
    four-layer framework (operational / cost-efficiency / outcome / long-term
    impact) with verbatim descriptions of each layer's question is not described
    anywhere in the existing corpus. Prior sources describe metrics at a
    feature level; this is the first source to provide a named organizing
    taxonomy.
  - **"Reviewer attention" as a waste category** (Claim 11): Including human
    review time as a waste dimension alongside compute cost and time is novel.
    No existing source treats human attention as an explicit measurable cost
    in the waste taxonomy.
  - **Time to adoption as a metric** (Claim 4): The "time to adoption" metric —
    measuring how quickly users engage with agent output — is not described
    in any existing source note. It is a proxy for human-agent handoff friction
    distinct from acceptance rate.
  - **System overlap as a monitoring target** (Claim 13): "System overlap
    decreasing" as a trend to watch is new. Prior sources address individual
    workflow efficiency; this is the first to name fleet-level overlap reduction
    as an explicit measurement target.

## Guide Impact

- **Chapter 05 (Team Adoption — measurement and rollout)**:
  - Add the cost-vs-outcome timing gap (Claims 1–2) as the foundational
    principle for agentic workflow measurement: teams must track cost and
    outcome signals on separate dashboards with separate interpretation
    cadences. Warn against "kill or keep" decisions based on cost-only
    data before outcome signals have materialized.
  - Add the four-layer taxonomy (Claims 5–9) as the organizing framework
    for the measurement section. Each layer (operational / cost-efficiency /
    outcome / long-term impact) answers a different question and has a
    different data availability timeline.
  - Add the six-metric starter kit (Claim 3) as the "minimum observable
    surface" for any workflow deployment — teams should be able to answer
    all six questions before going to production.
  - Add "time to adoption" (Claim 4) as an underused metric for diagnosing
    human-agent handoff friction — distinct from acceptance rate, it
    measures latency to engagement.
  - Add the trend-monitoring principle (Claim 13) as the operating cadence:
    review trends monthly, not per-run; the four target trends (cost per
    successful run down, acceptance up, retries down, overlap down) are the
    directional health check.

- **Chapter 02 (Harness Engineering)**:
  - Add the waste taxonomy (Claim 11) to workflow design review: each of
    the five waste sources (redundant runs, duplicate outputs, repeated context
    collection, deterministic work in agent path, low-adoption outputs) is a
    design smell worth checking before deployment.
  - Add the remediation map (Claim 12) paired with the waste taxonomy:
    consolidation, artifact sharing, context caching, and deterministic
    pre-checks are the standard fixes. Cross-reference `docs-ghaw-cost-management.md`
    Claim 5 for the `skip-if-match` implementation of "move deterministic
    work out of agent path."
  - Add the three-tool instrumentation stack (Claim 10): `gh aw logs`
    (operational + cost), Outcomes model (acceptance), OpenTelemetry
    (system trends). Document all three framings of `gh aw logs` together:
    cost monitoring, operational inspection, and measurement framework input.

- **Chapter 03 (Safety and Verification)**:
  - Cost-efficiency as a safety signal (Claim 7 Our assessment): sustained
    cost inefficiency (high spend per useful output) may indicate silent
    failure — the workflow is completing runs but producing rejected output.
    This warrants a safety framing, not just a cost framing.

## Extraction Notes

1. **WebFetch content processed via AI model**: The gh-aw documentation is
   served as an Astro/Starlight SPA. Multiple independent WebFetch passes
   with different prompts were used to capture verbatim content. Quotes marked
   with verbatim attribution are consistent across multiple passes and are
   treated as high-confidence; quotes from single-pass returns are marked
   accordingly. The core measurement principle ("Measure impact by using early
   cost signals alongside later outcome signals. Do not try to collapse them
   into a single score.") returned verbatim-consistent across all passes.

2. **Relationship to `reference/cost-management`**: The two reference pages are
   intentionally complementary. Cost management answers "how do I control and
   reduce cost?" Measuring impact answers "how do I evaluate whether cost is
   generating proportional value?" Teams need both; they address different
   questions. The cross-reference relationship is additive, not duplicative.

3. **Four-layer taxonomy vs. three-tier observability architecture**: The four-
   layer measurement framework (this source) and the three-tier observability
   architecture (`blog-ghaw-agent-observability.md`) are orthogonal. The blog
   decomposes monitoring by *agent role* (Metrics Collector, Portfolio Analyst,
   Audit Workflows); this source decomposes by *measurement question* (operational,
   cost-efficiency, outcome, long-term impact). Both are valid and non-contradictory.

4. **Outcomes model**: The source references "the Outcomes model" for downstream
   acceptance tracking without defining it in detail. This appears to be a
   platform-level construct in `gh aw` for tracking whether agent-produced
   content was accepted (PRs merged, comments acted on, issues resolved). The
   specifics of the Outcomes model are not documented in detail by this source.

5. **No contradictions filed**: Reviewed `docs-ghaw-cost-management.md`,
   `blog-ghaw-agent-observability.md`, `docs-ghaw-monitoring-patterns.md`, and
   `docs-ghaw-monitor-ops.md`. No claims in this source materially oppose
   existing source notes at the MINER.md §4a filing threshold.
