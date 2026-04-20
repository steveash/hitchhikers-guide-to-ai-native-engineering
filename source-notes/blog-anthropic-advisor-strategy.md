---
source_url: https://claude.com/blog/the-advisor-strategy
source_type: blog-post
title: "The Advisor strategy: Give agents an intelligence boost"
author: Anthropic (claude.com blog)
date_published: 2026-04-09
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: settled
issue: "#241"
---

# The Advisor strategy: Give agents an intelligence boost

> Anthropic introduces the advisor strategy — a named, benchmarked multi-agent
> design pattern where a small executor model drives tasks end-to-end and
> escalates to a large advisor model only on demand, inverting the conventional
> orchestrator/worker hierarchy to achieve combined cost reductions and quality
> gains; now available as a first-class `advisor_20260301` tool in the Messages API.

## Source Context

- **Type**: blog-post (official claude.com blog, April 9 2026; product
  announcement with technical documentation and benchmark evidence)
- **Author credibility**: First-party Anthropic engineering post published on
  the official Claude blog. Benchmark figures (SWE-bench Multilingual,
  BrowseComp) are Anthropic-run with named model versions and specific
  percentage-point deltas. Practitioner quotes are from named executives at
  named companies (Bolt, Genspark, Eve Legal). The API primitive described
  (`advisor_20260301`) is a shipping feature, not a proposal — maximum
  authority on the technical design.
- **Scope**: Covers the advisor strategy as a design pattern, its API
  implementation in the Messages API, billing and cost-control mechanics,
  benchmark evidence across two benchmarks, and three practitioner testimonials.
  Does NOT cover: multi-agent coordination beyond the two-model advisor/executor
  dyad, evaluation methodology details for the benchmarks, or long-running
  session behavior. The advisor tool is in beta (`anthropic-beta:
  advisor-tool-2026-03-01`); GA timeline not stated.

## Extracted Claims

### Claim 1: The advisor strategy inverts the conventional orchestrator/worker pattern — a smaller executor model drives the task end-to-end and escalates to a larger advisor only when needed

- **Evidence**: First-party architectural description with explicit comparison
  to standard sub-agent orchestration ("standard sub-agent pattern has large
  orchestrator decompose work and delegate to small workers"). The inversion is
  the defining property: the *smaller* model is in the driver's seat;
  the *larger* model is on-call.
- **Confidence**: settled (first-party Anthropic description of a shipping API
  primitive)
- **Quote**: "Instead of a large orchestrator decomposing work and delegating
  to small workers, a small executor drives and escalates to a large advisor
  only when needed — frontier reasoning applied selectively, not universally."
- **Our assessment**: The architectural significance goes beyond cost. Standard
  orchestrator/worker patterns incur overhead at every sub-task boundary
  (decomposition, dispatch, result aggregation). The advisor pattern eliminates
  decomposition and worker-pool management entirely — the executor handles all
  of that, calling the advisor only when it encounters something it cannot
  resolve. For harness authors: this is a simpler control loop than orchestrated
  parallelism. For model selection: this pattern argues that "always use Opus"
  and "always use Sonnet" are both suboptimal — the right structure is
  task-conditional escalation.

### Claim 2: The advisor model never calls tools or produces user-facing output — it returns only a plan, correction, or stop signal (typically 400–700 tokens)

- **Evidence**: First-party technical specification. The advisor's output
  contract is explicitly constrained: plan / correction / stop signal. Token
  budget (400–700 tokens) is stated as typical.
- **Confidence**: settled (API design fact from first-party source)
- **Quote**: "Advisor returns short plan (typically 400–700 text tokens);
  executor resumes — all without extra round-trips."
- **Our assessment**: The constraint that the advisor never calls tools is
  architecturally significant. It means the advisor cannot take actions in the
  world, only provide guidance. This eliminates a class of bugs where the
  advisory model accidentally acts when it should only advise. The 400–700
  token output budget is also a cost-control property: a ceiling on how much
  Opus reasoning is purchased per advisor invocation. Harness authors can tune
  `max_uses` to cap total advisor spend per request.

### Claim 3: Sonnet 4.6 + Opus 4.6 advisor on SWE-bench Multilingual achieves +2.7 percentage points over Sonnet 4.6 alone, with 11.9% lower cost per agentic task

- **Evidence**: Named benchmark (SWE-bench Multilingual) with named model
  versions (claude-sonnet-4-6 executor, claude-opus-4-6 advisor). Both the
  quality improvement (+2.7pp) and the cost reduction (−11.9%) are reported
  for the same configuration.
- **Confidence**: settled (first-party benchmark with specific model versions
  and measured deltas; two metrics measured simultaneously)
- **Quote**: "Sonnet + Opus advisor on SWE-bench Multilingual: +2.7 percentage
  point improvement over Sonnet alone, −11.9% cost per agentic task."
- **Our assessment**: The simultaneous quality improvement and cost reduction
  on SWE-bench is the most significant benchmark result in this post. Standard
  model selection intuition predicts a quality/cost tradeoff — better quality
  costs more. The advisor strategy delivers a Pareto improvement on this
  benchmark: better AND cheaper than Sonnet solo. The mechanism is selective
  application of Opus reasoning: the executor handles routine tool calls and
  state management at Sonnet rates; Opus reasoning fires only on decisions where
  it adds value. The 11.9% cost reduction implies that the advisor invocations
  (billed at Opus rates) are more than offset by the executor handling more
  work that previously required an Opus baseline. This is the clearest
  quantified argument for the advisor pattern in the corpus.

### Claim 4: Haiku 4.5 + Opus 4.6 advisor on BrowseComp scores 41.2% vs. 19.7% for Haiku 4.5 solo — a >2× quality boost at 85% lower cost than Sonnet 4.6 solo

- **Evidence**: Named benchmark (BrowseComp) with named model versions. Three
  conditions compared: Haiku solo (19.7%), Haiku + Opus advisor (41.2%), and
  Sonnet solo (reference point for cost comparison). The 85% cost reduction is
  relative to Sonnet solo baseline.
- **Confidence**: settled (first-party benchmark with three named conditions
  and specific scores)
- **Quote**: "Haiku + Opus advisor: 41.2% score vs. Haiku solo 19.7% (>2×
  improvement), 85% cheaper than Sonnet solo."
- **Our assessment**: The Haiku + Opus advisor result is the more dramatic
  demonstration. Haiku alone achieves 19.7% — clearly insufficient for
  BrowseComp's research-style queries. Adding Opus as an on-demand advisor
  more than doubles the score to 41.2%. This shows the advisor pattern can
  unlock a task category that the executor model alone cannot handle, not
  just improve at the margin. The 85% cost reduction vs. Sonnet solo makes
  this relevant to cost-sensitive production deployments where Sonnet would
  otherwise be the floor choice. Contrast with the harnessing-claude-intelligence
  post (blog-anthropic-harnessing-claude-intelligence): that post showed Opus
  4.6 solo at 84% on BrowseComp; Haiku + Opus advisor at 41.2% is still well
  below that ceiling, meaning the advisor pattern has a quality ceiling of its
  own. The pattern is not a free substitute for using Opus throughout.

### Claim 5: The advisor_20260301 tool is a first-class Messages API primitive — a single /v1/messages request with no extra round trips or client-side orchestration required

- **Evidence**: API specification from the post. The tool type is
  `advisor_20260301`; the beta header is `anthropic-beta: advisor-tool-2026-03-01`.
  The "no extra round trips" claim is a specific engineering property: the
  advisor consultation happens server-side within the single API call.
- **Confidence**: settled (API design fact, shipping feature)
- **Quote**: "Curated context routes to advisor; advisor returns short plan;
  executor resumes — all within single /v1/messages request, no extra round
  trips."
- **Our assessment**: The single-request design is architecturally important.
  Previous multi-model patterns required client-side orchestration: the harness
  explicitly calls Model A, parses the result, calls Model B, parses the
  result, formats a combined response. The advisor primitive offloads this
  coordination to the API layer. The cost to harness authors is reduced
  orchestration code; the tradeoff is less control over exactly what context
  is routed to the advisor ("curated context" implies the API decides what to
  send, not the caller). For harness authors currently managing multi-model
  calls manually: this is a meaningful simplification if the advisor/executor
  pattern fits their use case.

### Claim 6: The max_uses parameter caps advisor invocations per request; advisor tokens are billed separately at advisor model rates and reported in a separate usage block

- **Evidence**: API parameter documentation (`max_uses`) and billing model
  description (separate advisor token reporting in usage block).
- **Confidence**: settled (API specification from first-party source)
- **Quote**: "Advisor tokens billed at advisor model rates; executor tokens
  billed at executor rates; advisor tokens reported separately in usage block."
- **Our assessment**: `max_uses` is the primary cost-control lever for the
  advisor pattern. Without it, a runaway executor could escalate to Opus
  arbitrarily many times per request, making costs unpredictable. The separate
  usage-block reporting enables per-request observability: harness authors can
  track advisor vs. executor token consumption independently and set
  `max_uses` based on observed escalation frequency in their workloads. This
  is a well-designed cost-control primitive — compare with blog-bswen-mcp-token-cost,
  where MCP tool call costs are opaque and difficult to bound.

### Claim 7: Practitioner adoption from Bolt shows the advisor makes better architectural decisions on complex tasks with zero overhead on simple ones

- **Evidence**: Named practitioner (Eric Simmons, CEO and Founder, Bolt) with
  a specific functional claim: architectural decision quality improves on
  complex tasks; no overhead on simple tasks.
- **Confidence**: anecdotal (single named practitioner; no benchmark, no
  methodology)
- **Quote**: "It makes better architectural decisions on complex tasks while
  adding no overhead on simple ones." — Eric Simmons, CEO and Founder, Bolt
- **Our assessment**: The "zero overhead on simple tasks" claim is the key
  implication of the `max_uses` + conditional escalation design: if the
  executor can complete simple tasks without escalating, the advisor tokens
  are zero for those tasks. Bolt's CEO is describing the designed behavior
  working as intended in production. The "better architectural decisions"
  claim is qualitative — no before/after metric — but names the specific
  task category (architectural decisions) where Opus adds value.

### Claim 8: Genspark's CTO reports improvements in agent turns, tool calls, and overall score exceeding their internally-built planning tool

- **Evidence**: Named practitioner (Kay Zhu, Cofounder & CTO, Genspark) with
  a comparative claim: the advisor outperformed Genspark's own hand-built
  planning tool across multiple metrics.
- **Confidence**: anecdotal (named practitioner comparison, no metric values)
- **Quote**: "We saw clear improvements in agent turns, tool calls, and overall
  score — better than a planning tool we built ourselves." — Kay Zhu,
  Cofounder & CTO, Genspark
- **Our assessment**: The significance here is the comparison to a custom-built
  planning tool — Genspark had already tried to solve the same problem
  internally (a planning layer for their agent) and found the advisor primitive
  outperformed it. This is a build-vs-buy signal: an API-level advisor beats a
  hand-rolled planning tool at a company with the engineering resources to build
  one. The "agent turns" and "tool calls" metrics suggest the advisor is
  producing more efficient reasoning paths, not just better final output.

### Claim 9: Eve Legal reports 5× lower cost for their Haiku + Opus advisor configuration vs. a frontier-model baseline, matching frontier-model quality

- **Evidence**: Named practitioner (Anuraj Pandey, Machine Learning Engineer,
  Eve Legal) with a specific cost multiplier claim (5×) and a quality
  equivalence claim ("matching frontier-model quality").
- **Confidence**: anecdotal (named practitioner; no benchmark or methodology)
- **Quote**: "Haiku 4.5 dynamically scales intelligence by consulting Opus 4.6
  as complexity demands, matching frontier-model quality at 5× lower cost."
  — Anuraj Pandey, Machine Learning Engineer, Eve Legal
- **Our assessment**: "5× lower cost" is the largest cost-reduction claim in
  the post and the most practically relevant to teams evaluating the pattern.
  "Matching frontier-model quality" is a strong claim that is not independently
  benchmarked — it is Eve Legal's internal assessment on their document
  extraction tasks. The Eve Legal use case (legal document extraction) is a
  task type with clear success criteria and high value on accuracy, making it
  a meaningful validation of the pattern beyond coding benchmarks. The 5×
  figure should be read as Eve Legal's specific workload result, not a
  universal multiplier.

## Concrete Artifacts

### API Implementation (Python)

```python
# Source: "The Advisor strategy," Anthropic, claude.com/blog, April 9, 2026
# Beta feature — requires anthropic-beta: advisor-tool-2026-03-01 header

response = client.messages.create(
    model="claude-sonnet-4-6",          # executor model drives the task
    tools=[
        {
            "type": "advisor_20260301",
            "name": "advisor",
            "model": "claude-opus-4-6", # advisor model — Opus recommended
            "max_uses": 3,              # cap advisor calls per request
        },
        # ... your other tools (bash, read, write, etc.)
    ],
    messages=[...],
    extra_headers={"anthropic-beta": "advisor-tool-2026-03-01"},
)

# Usage block reports executor and advisor tokens separately:
# response.usage.input_tokens          → executor input tokens (Sonnet rates)
# response.usage.advisor_input_tokens  → advisor input tokens (Opus rates)
```

### Benchmark Results Summary

```
# Advisor Strategy Benchmarks
# Source: "The Advisor strategy," Anthropic, claude.com/blog, April 9, 2026
# Advisor model: claude-opus-4-6 in all configurations

SWE-bench Multilingual (code-repair tasks):
  claude-sonnet-4-6 solo:                 baseline
  claude-sonnet-4-6 + Opus advisor:       +2.7pp    cost: -11.9% vs. baseline

BrowseComp (web research tasks):
  claude-haiku-4-5 solo:                  19.7%
  claude-haiku-4-5 + Opus advisor:        41.2%     cost: 85% cheaper than Sonnet solo
  claude-sonnet-4-6 solo:                 (reference) cost: 100%
  claude-opus-4-6 solo:                   84%        (from blog-anthropic-harnessing-claude-intelligence)
```

### Pattern Comparison: Orchestrator/Worker vs. Advisor/Executor

```
STANDARD ORCHESTRATOR/WORKER PATTERN
  Large orchestrator (Opus):
    → decomposes task
    → dispatches to small workers (Sonnet/Haiku)
    → aggregates results
  Overhead: decomposition, dispatch, aggregation on every task
  Model: Opus reasoning applied to orchestration, not execution

ADVISOR/EXECUTOR PATTERN (advisor_20260301)
  Small executor (Sonnet/Haiku):
    → drives task end-to-end
    → calls advisor tool when blocked or uncertain
  Large advisor (Opus):
    → receives curated context from executor
    → returns plan/correction/stop signal (400-700 tokens, no tool calls)
    → does NOT produce user-facing output
  Overhead: advisor tokens only when executor escalates (capped by max_uses)
  Model: Opus reasoning applied selectively to decisions that need it
```

### Practitioner Evidence Summary

```
Company    | Role                       | Model Pair         | Reported Outcome
-----------|----------------------------|--------------------|---------------------------
Bolt       | CEO (Eric Simmons)         | unspecified        | Better architectural decisions
           |                            |                    | on complex tasks; zero overhead
           |                            |                    | on simple ones
Genspark   | CTO (Kay Zhu)              | unspecified        | Improved agent turns, tool
           |                            |                    | calls, overall score; beat their
           |                            |                    | own planning tool
Eve Legal  | ML Engineer (Anuraj Pandey)| Haiku 4.5 + Opus  | 5× lower cost vs. frontier
           |                            |                    | baseline; matching quality
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-harnessing-claude-intelligence.md` — That post's BrowseComp
    benchmarks (Opus 4.6 solo: 84%; subagents: +2.8%) establish the same benchmark
    as the baseline this post measures against. The Haiku + Opus advisor result
    (41.2%) fits clearly in that benchmark's range: above Haiku-solo capability,
    well below full-Opus solo. Both posts use BrowseComp as the evaluation vehicle
    for architecture decisions — the advisor pattern is a new architecture choice
    in the same measurement space.
  - `docs-github-copilot-agent-model-selection.md` — That source documents model
    tier selection (Sonnet vs. Opus) as a per-task operator choice in GitHub's
    hosted agent UI. The advisor strategy is a complementary mechanism: rather than
    statically selecting Sonnet or Opus for a task, the advisor pattern lets the
    executor dynamically upgrade to Opus reasoning on the specific decisions that
    need it. Together these two patterns — static tier selection and dynamic advisor
    escalation — form a richer model selection toolkit than either alone.
  - `blog-anthropic-harness-long-running.md` — That post documents the
    generator/evaluator architecture (two models in sequence: generator produces,
    evaluator critiques). The advisor pattern is related but architecturally
    distinct: the advisor is not a fixed second pass — it is an on-demand
    consultation invoked by the executor when needed. The generator/evaluator
    applies evaluation universally; the advisor applies intelligence selectively.

- **Extends**:
  - `discussion-hn-ttal-multiagent-factory.md` — TTal's seven multi-agent
    patterns include Executor-Reviewer (sequential), Router, Orchestrator,
    Pipeline, Debate, Supervisor, and Swarm. The advisor/executor pattern does
    not fit neatly into any of these — it is neither sequential evaluation nor
    orchestrated dispatch. It is closest to a Supervisor (monitor-correct) pattern
    but differs because the advisor only acts when the executor escalates, not
    on a polling schedule. The advisor pattern adds a new first-class pattern to
    TTal's taxonomy: conditional on-demand escalation.
  - `blog-anthropic-harnessing-claude-intelligence.md` — That post's Claim 12
    ("switching models mid-session breaks cache; use subagents for cheaper
    models instead") is directly relevant to the advisor pattern. The
    `advisor_20260301` tool handles this at the API layer: the executor session
    stays on Sonnet (preserving the cache); advisor calls are API-internal and
    do not bust the prefix cache. The advisor primitive solves the cache-
    invalidation problem for in-flight model switching that the earlier post
    flagged.
  - `blog-anthropic-claude-managed-agents.md` — That post's multi-agent
    coordination feature (agents spawn sub-agents to parallelize work) is a
    different dimension of multi-model use. The advisor pattern is not about
    parallelism — it is about selective escalation within a single task. Together
    these two Anthropic announcements (April 8 and April 9, 2026) represent
    complementary multi-model patterns: Managed Agents for parallel work
    distribution, advisor strategy for sequential quality escalation.

- **Contradicts**: None filed. The advisor pattern's BrowseComp result
  (Haiku + Opus advisor: 41.2%) is well below Opus solo (84% from
  `blog-anthropic-harnessing-claude-intelligence.md`), which might appear to
  contradict Eve Legal's claim of "matching frontier-model quality" — but this
  is a conditioning variable: Eve Legal's tasks (legal document extraction)
  may not be BrowseComp-style web research. The two measurements are not
  comparable, so no contradiction issue is required.

- **Novel**:
  - **The `advisor_20260301` API primitive as a first-class Messages API tool**:
    No other source in the corpus documents a vendor-provided multi-model
    escalation primitive. Prior multi-model patterns required client-side
    orchestration; this is the first API-native solution.
  - **Simultaneous quality improvement and cost reduction on SWE-bench**:
    The +2.7pp quality gain AND −11.9% cost reduction on the same benchmark
    are a Pareto improvement with no quality/cost tradeoff. No other architecture
    pattern in our corpus has documented this combination on a named benchmark.
  - **`max_uses` as a first-class cost-control parameter for model escalation**:
    No other source documents a bounded per-request cap on advisory model
    invocations. This is a new cost-control primitive for multi-model harnesses.
  - **The inversion principle as an architectural heuristic**: The explicit
    claim that "smaller models should drive, larger models should advise on
    demand" inverts the conventional "Opus orchestrates, Haiku executes"
    framing that practitioners have assumed. This is a named design principle
    with benchmarks attached — the first such principle for the executor-drives,
    advisor-advises pattern in our corpus.
  - **Genspark comparison to hand-built planning tool**: No other source
    documents a practitioner's explicit comparison of an API primitive to a
    custom-built equivalent with a preference for the API primitive. This is
    a concrete build-vs-buy signal for the advisor pattern.

## Guide Impact

- **Chapter 05 (Multi-Agent Systems / Orchestration Patterns)**: Add the
  advisor/executor pattern as a distinct named design pattern alongside
  orchestrator/worker and generator/evaluator. The key differentiator to
  document: orchestrator/worker applies Opus universally at decomposition;
  generator/evaluator applies it universally at evaluation; advisor/executor
  applies it conditionally at escalation. Cite the SWE-bench Multilingual
  result (+2.7pp, −11.9% cost) and the BrowseComp Haiku result (19.7% →
  41.2%) as the quantified evidence. The pattern comparison artifact above
  is the concrete illustration.

- **Chapter 05 (Multi-Agent Systems / Orchestration Patterns)**: Document the
  `advisor_20260301` API primitive with the Python code example. Note the
  `max_uses` cost-control parameter, the separate usage-block reporting for
  observability, and the beta header requirement. This is actionable today
  for practitioners building with the Messages API.

- **Chapter 06 (Model Selection & Cost Optimization)**: Update any Sonnet vs.
  Opus selection guidance to include the advisor pattern as a third option.
  Current framing: "use Sonnet for most tasks, upgrade to Opus when you need
  more capability." New framing: "use Sonnet-drives-Opus-advises for tasks
  where selective escalation delivers Pareto improvements — the SWE-bench
  Multilingual result shows this can beat both single-model options
  simultaneously." The Eve Legal 5× cost reduction is the reference point
  for practitioners with document-intelligence or extraction tasks.

- **Chapter 06 (Model Selection & Cost Optimization)**: Add the BrowseComp
  data point (Haiku + Opus advisor: 41.2% vs. Haiku solo: 19.7%, vs. Sonnet
  solo at ~100% cost) to the cost/quality tradeoff table. This is the first
  benchmark in the corpus that directly quantifies the advisor pattern on the
  BrowseComp benchmark used consistently across Anthropic's harness engineering
  posts. Cross-reference with `blog-anthropic-harnessing-claude-intelligence.md`
  Claim 7 (Opus 4.6 solo: 84% on BrowseComp) to give practitioners the full
  performance ladder: Haiku solo → Haiku + Opus advisor → Sonnet → Opus.

- **Chapter 02 (Harness Engineering)**: Note that `advisor_20260301` solves
  the cache-invalidation problem for in-flight model switching documented in
  `blog-anthropic-harnessing-claude-intelligence.md` Claim 12. Practitioners
  who previously had to spawn subagents to switch models without busting cache
  now have an API-native alternative for the advisor use case.

## Extraction Notes

- The source was retrieved via WebFetch (Webflow JS rendering). The content was
  fully extractable. No sub-pages were followed — the blog post is self-contained
  with all technical specifics on the single page.
- The `advisor_20260301` tool is in beta at time of extraction. The beta header
  (`anthropic-beta: advisor-tool-2026-03-01`) must be included in all API calls;
  GA availability is not stated. Practitioners should consult current API
  documentation before deploying.
- BrowseComp scores are used in multiple Anthropic posts as a consistent
  benchmark: `blog-anthropic-harnessing-claude-intelligence.md` documents
  Opus 4.6 solo at 84%, Sonnet 4.5 at 43%; this post adds Haiku 4.5 solo
  at 19.7% and Haiku + Opus advisor at 41.2%. These are now comparable data
  points in the same measurement space.
- Practitioner quotes (Bolt, Genspark, Eve Legal) are from named individuals
  with full titles. They are testimonial-quality evidence — credible as
  real-world validation, but not benchmarked or independently replicated.
  Confidence on claims derived solely from these quotes is rated anecdotal.
- Confidence overall is set to `settled` because: (a) the API primitive is
  a shipping feature with published specifications, (b) the benchmark results
  are first-party Anthropic numbers on named benchmarks with named model
  versions, and (c) three named enterprise practitioners corroborate the
  pattern in production. Individual practitioner claims are rated anecdotal
  within their respective claim sections.
