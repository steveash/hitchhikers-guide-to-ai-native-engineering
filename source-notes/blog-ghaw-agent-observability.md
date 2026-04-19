---
source_url: https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-metrics-analytics/
source_type: blog-post
title: "Meet the Workflows: Metrics & Analytics"
author: Don Syme, Peli de Halleux, Mara Kiefer (GitHub Agentic Workflows team)
date_published: 2026-01-13
date_extracted: 2026-04-19
last_checked: 2026-04-19
status: current
confidence_overall: emerging
issue: "#165"
---

# Meet the Workflows: Metrics & Analytics

> First-party production evidence from GitHub's own agent factory that
> observability is a first-class architectural concern for multi-agent systems —
> implemented as three dedicated agents (Metrics Collector, Portfolio Analyst,
> Audit Workflows) that monitor, cost-analyze, and audit every other agent in
> the factory, with the Audit Workflows agent demonstrating the fully-closed
> loop: meta-observation that autonomously triggers downstream corrective PRs.

## Source Context

- **Type**: blog-post (part 13 of a 19-part series on GitHub Agentic Workflows,
  `gh-aw`; the series documents GitHub's production multi-agent automation
  platform used by Peli de Halleux's "Agent Factory")
- **Author credibility**: First-party from GitHub: Don Syme (Distinguished
  Engineer, F# designer), Peli de Halleux (Principal Researcher, GitHub
  Copilot), and Mara Kiefer (GitHub Agentic Workflows team). These are not
  vendor-marketing authors — they are the engineers who built and operate the
  system they describe. Production metrics are from a live GitHub-hosted
  repository. High credibility for the claims they make about their own system;
  claims do not generalize to other platforms without caution.
- **Scope**: Covers three specific observability workflows in a single
  production agent factory. Does NOT cover: how to build observability from
  scratch without the `gh aw` CLI, observability for agent systems on other
  platforms, cost benchmarks across agent types, quality-outcome metrics (only
  performance and cost metrics are described), or failure modes of the
  observability workflows themselves. The post is relatively short (~600-800
  words) — depth comes from the specificity of the production numbers, not from
  breadth of coverage.

## Extracted Claims

### Claim 1: Observability is non-optional for multi-agent systems at scale

- **Evidence**: First-person production framing from the GitHub team operating
  dozens of AI agents in a live factory. The statement is backed by the system
  they built: three dedicated observability workflows that account for a large
  fraction of total agent activity (93 + 41 + 7 = 141 discussions created by
  monitoring agents alone).
- **Confidence**: emerging
- **Quote**: "Observability isn't optional when you're running dozens of AI
  agents — it's the difference between a well-oiled machine and an expensive
  black box."
- **Our assessment**: This is the thesis of the post and we buy it strongly.
  The production numbers lend it weight: the monitoring agents are among the
  most prolific agents in the factory. The alternative — shipping agents with
  no structured observation layer — is precisely what Osmani's "verification
  bottleneck" claim (blog-addyosmani-code-agent-orchestra, Claim 5) warns
  against. The GitHub team's production implementation is the concrete
  instantiation of the abstract principle. The framing "expensive black box"
  is pointed: without observability, cost and quality problems accumulate
  silently, which is what the Portfolio Analyst actually found.

### Claim 2: A three-tier observability architecture — performance tracking, cost optimization, meta-audit — maps to distinct monitoring concerns

- **Evidence**: The three workflows are purpose-differentiated: Metrics
  Collector (performance, daily), Portfolio Analyst (cost, weekly), Audit
  Workflows (logs/errors/success patterns, continuous). Each produces a
  different output type and has a different cadence.
- **Confidence**: emerging
- **Quote**: The post describes the observatory as "the nerve center of Peli's
  Agent Factory."
- **Our assessment**: The three-tier split (performance / cost / audit) is a
  useful architectural decomposition for any multi-agent system. It mirrors
  the observability best practice of separating metrics (what happened),
  profiling (what it cost), and auditing (why and whether it should have
  happened). The fact that GitHub's production system converged on these
  three tiers independently corroborates their naturalness as a partitioning
  scheme. For the guide: recommend this three-tier split as a starting
  framework rather than a monolithic "monitoring agent."

### Claim 3: The meta-agent pattern — agents dedicated to auditing other agents — is viable in production, and the Audit Workflows agent is the most prolific agent in the factory

- **Evidence**: Production metrics: Audit Workflows produced 93 audit report
  discussions and raised 9 issues. By volume it exceeds the Metrics Collector
  (41 discussions) and the Portfolio Analyst (7 discussions) combined.
- **Confidence**: emerging
- **Quote**: N/A (quantified in the production metrics section)
- **Our assessment**: The Audit Workflows being the most prolific agent is
  notable. It implies that auditing other agents' runs — reviewing logs, costs,
  errors, and success patterns — generates more structured output than the
  primary task-execution agents. This is a real and somewhat counterintuitive
  finding: monitoring can exceed the overhead it monitors in terms of artifact
  production. We cannot tell from this post whether that ratio (monitoring
  output > task output) is healthy or indicates over-instrumentation. But the
  fact that the GitHub team runs it in production at this volume suggests they
  find the output valuable.

### Claim 4: Cost optimization agents can identify unnecessarily expensive LLM calling patterns across an agent fleet

- **Evidence**: Portfolio Analyst finding: "some agents were way too chatty
  with their LLM calls" — a specific, actionable pattern discovered by a
  monitoring agent analyzing token consumption across the fleet.
- **Confidence**: anecdotal (one finding from one production system)
- **Quote**: "some agents were way too chatty with their LLM calls"
- **Our assessment**: This is the most practically valuable claim in the post.
  It demonstrates that cost inefficiency in multi-agent systems is often
  invisible without instrumentation — no individual agent knows it is
  over-calling LLMs relative to its peers. A Portfolio Analyst that can compare
  call patterns across agents and flag outliers is the only mechanism for
  surfacing this. The parallel to Bswen's MCP token audit (blog-bswen-mcp-
  token-cost) is strong: both sources find that cost problems in AI engineering
  are invisible without explicit measurement, and that measurement reveals
  patterns that are otherwise undetectable.

### Claim 5: Observability can close the feedback loop autonomously — Audit Workflows raised 9 issues, 4 of which downstream agents converted to PRs

- **Evidence**: Production metrics: 93 audit reports → 9 issues raised → 4
  issues led to downstream PRs from other agents. This is the complete
  autonomous loop: observe → diagnose → flag → fix.
- **Confidence**: emerging
- **Quote**: N/A (quantified in the production metrics)
- **Our assessment**: This is the most architecturally novel claim in the post.
  The loop — Audit Workflows identifies a problem, raises a GitHub issue, and
  a downstream agent picks up the issue and opens a corrective PR — is a
  self-healing pattern that requires no human in the middle. The 4/9 conversion
  rate (44% of audit-raised issues became PRs) suggests the diagnostic quality
  is high enough for downstream agents to act on without clarification. For the
  guide: this is evidence that meta-observation, when it produces structured
  output (GitHub issues with sufficient context), can feed directly into
  autonomous remediation. The loop is only viable if the Audit Workflows agent
  writes issues that are actionable; the 44% PR-conversion rate is a proxy
  metric for that actionability.

### Claim 6: The `gh aw add-wizard` toolchain makes observability workflows declarative and repository-level, with wizard-driven setup and a compiled lock file

- **Evidence**: Three concrete `gh aw add-wizard` commands published in the
  post; post instructions: "edit and remix the workflow specifications to meet
  your needs, regenerate the lock file using `gh aw compile`, and push to
  your repository."
- **Confidence**: settled (these are the published CLI commands for the `gh aw`
  platform)
- **Quote**: "Then edit and remix the workflow specifications to meet your
  needs, regenerate the lock file using `gh aw compile`, and push to your
  repository."
- **Our assessment**: The declarative `gh aw compile` / lock-file model is
  important. It means observability workflows are not ad-hoc scripts run by
  hand — they are repository-checked artifacts with versioned specifications.
  The `v0.45.5` pinning in the wizard URLs suggests the platform takes
  reproducibility seriously. The "edit and remix" framing is also notable:
  these are not black-box vendor workflows but user-modifiable specifications.
  This is the operationally important claim for teams that want to adopt the
  pattern: it is accessible (wizard-driven) and customizable.

### Claim 7: Agent metrics data should feed upward to higher-level orchestrators, not just serve as human dashboards

- **Evidence**: Prospector triage note citing the Metrics Collector description:
  "treats the metrics feed as input to higher-level orchestrators." This
  distinguishes the Metrics Collector from a passive reporting tool — its
  output is meant to be consumed by other agents, not just by humans.
- **Confidence**: emerging
- **Quote**: N/A (triage note paraphrase; not a direct quote from the post)
- **Our assessment**: This claim is the most architecturally ambitious of the
  three: metrics are not terminal artifacts but inputs to a meta-orchestration
  layer. It implies a hierarchy where Metrics Collector → Portfolio Analyst or
  higher-level planning agents — the observatory feeds the factory's strategy
  layer. This is a step beyond typical "metrics dashboards for humans." If
  accurate, it makes the observability layer a functional component of the
  orchestration plane, not just a passive observer. We treat this as emerging
  because the post does not describe the mechanism in detail; the Prospector
  inferred it from the description.

### Claim 8: The observatory represents a named, first-class architectural component of an agent factory, not an afterthought

- **Evidence**: The post introduces the observability section as "the
  observatory — the nerve center of Peli's Agent Factory." The series places
  these workflows as part 13 of 19, after workflows for fault investigation and
  before operations/release workflows — a deliberate architectural position.
- **Confidence**: anecdotal (one team's architectural labeling decision)
- **Quote**: "Now it's time to plunge into the _observatory_ — the nerve center
  of Peli's Agent Factory!"
- **Our assessment**: The naming ("observatory" as "nerve center") is
  intentional. The GitHub team treats these three monitoring workflows as
  structural rather than incidental. For the guide: recommend that teams
  explicitly name and plan their observability layer as a first-class component,
  not as "monitoring we'll add later." The observatory metaphor is useful: just
  as an astronomical observatory is built before the observation campaign, the
  agent observatory should be deployed before the factory scales.

## Concrete Artifacts

### Production Metrics (from the post)

```
Peli's Agent Factory — Observability Workflow Output (as of Jan 13, 2026):

Metrics Collector:
  Output: 41 daily metrics discussions
  Example: Discussion #6986 (daily code metrics report)
  Cadence: Daily

Portfolio Analyst:
  Output: 7 portfolio analysis discussions
  Example: Discussion #6499 (weekly portfolio analysis)
  Cadence: Weekly
  Finding: identified agents making "unnecessarily expensive LLM calls"
           ("some agents were way too chatty with their LLM calls")

Audit Workflows:
  Output: 93 audit report discussions, 9 issues raised
  Conversion: 4 of 9 issues led to downstream PRs from other agents
  Cadence: Continuous
  Status: Most prolific agent in the factory
```

### CLI Commands to Add the Three Workflows

```bash
# Add Metrics Collector
gh aw add-wizard https://github.com/github/gh-aw/blob/v0.45.5/.github/workflows/metrics-collector.md

# Add Portfolio Analyst
gh aw add-wizard https://github.com/github/gh-aw/blob/v0.45.5/.github/workflows/portfolio-analyst.md

# Add Audit Workflows
gh aw add-wizard https://github.com/github/gh-aw/blob/v0.45.5/.github/workflows/audit-workflows.md

# After adding/editing: compile and deploy
gh aw compile
git push
```

### Autonomous Remediation Loop (inferred from production metrics)

```
Audit Workflows agent observes:
  → analyzes logs, costs, errors, success patterns across all agents
  → produces: audit report discussion (93 total)

If problem detected:
  → raises GitHub issue (9 raised from 93 audit reports = ~10% rate)

Downstream agent picks up issue:
  → opens corrective PR (4 of 9 issues → PRs = 44% conversion rate)

Full loop: no human required between observation and fix attempt.
```

## Cross-References

- **Corroborates**:
  - **blog-addyosmani-code-agent-orchestra** (Claim 5 — "The bottleneck has
    shifted from code generation to verification"): The observatory pattern is
    the production implementation of this principle applied to agent systems.
    Osmani argues human engineers must shift to verification; this source shows
    GitHub built *dedicated agents* to perform that verification role for other
    agents. The GitHub team's solution to the verification bottleneck is
    automated meta-observation, not more human review hours.
  - **blog-bswen-mcp-token-cost** (Claim 1/2 — invisible MCP token costs):
    Both sources converge on the same meta-principle: cost problems in AI
    systems are invisible without explicit instrumentation. Bswen's MCP
    over-loading was invisible until `/context` was run; the "chatty" agents
    in the GitHub factory were invisible until the Portfolio Analyst profiled
    them. Neither problem self-announces; both required purpose-built
    measurement.
  - **blog-faros-claude-code-roi** (Claim 4 — three-layer measurement
    framework): Faros recommends measuring adoption, code trust, and team
    performance. The GitHub factory's observatory maps roughly to these layers:
    Metrics Collector (team performance), Portfolio Analyst (cost/efficiency as
    a proxy for adoption quality), Audit Workflows (quality/correctness). The
    two frameworks were developed independently for different scopes (org-level
    vs. agent-fleet) and converge on similar decompositions.
  - **discussion-hn-ttal-multiagent-factory** (Claim 8 — "stuck-vs-slow" as an
    open problem): TTal's HN thread flagged detecting stuck agents as unsolved.
    The GitHub Audit Workflows agent is one production approach: a dedicated
    agent that analyzes all runs for errors and anomalies. It does not
    specifically solve the stuck-vs-slow heuristic problem, but it demonstrates
    that systematic audit-based detection is viable at scale.

- **Extends**:
  - **discussion-hn-ttal-multiagent-factory**: TTal established the Manager/
    Worker plane architecture with external state. This source extends the
    corpus's multi-agent architecture picture with a third layer: an
    *observatory* plane that sits above the manager/worker planes and observes
    both. The GitHub architecture implies at least three layers — task execution
    (workers), coordination (manager), and observation (observatory) — where
    TTal's architecture explicitly covers only the first two.
  - **docs-github-copilot-pr-review-metrics**: The Copilot PR metrics note
    covers GitHub-native measurement for AI-assisted code review at the
    organization level. This source covers GitHub-internal measurement for
    AI agents at the agent-fleet level. Together they show GitHub instrumenting
    AI assistance at two different granularities: org-level metrics for human
    tooling, fleet-level observability for autonomous agent systems. The latter
    is more novel to the corpus.

- **Contradicts**: None filed. No existing source note makes a claim that
  observability is optional or that monitoring agents is unnecessary overhead.
  The nearest tensions are around cost (instrumentation has token overhead),
  but neither TTal nor Osmani addresses this specifically enough to constitute
  a contradiction. The GitHub team's Audit Workflows being the "most prolific
  agent" (by output volume) is potentially noteworthy — it implies monitoring
  overhead can exceed task execution overhead — but no source in the corpus
  claims this is undesirable.

- **Novel**:
  - **The autonomous remediation loop** (Claim 5): No other source in the
    corpus documents the fully-closed observability loop: meta-agent observes →
    raises issue → downstream agent fixes without human intervention. Osmani
    describes two-agent verification (Agent A implements, Agent B reviews) but
    does not describe the self-healing loop at the factory level. This is new.
  - **The observatory as a named architectural layer** (Claim 8): Treating the
    observability layer as a first-class "nerve center" component — not a
    monitoring script but a named architectural plane — is not described in
    TTal, Osmani, Kiln, or any other multi-agent source in the corpus.
  - **Three-tier observability decomposition** (Claim 2): The specific split
    of performance / cost / meta-audit into three separate agents with different
    cadences and output formats is not described elsewhere. Prior sources
    discuss observability in general terms; this is the first concrete
    production implementation.
  - **"Chatty" LLM calling as a detectable pattern** (Claim 4): The finding
    that some agents make "unnecessarily expensive LLM calls" and that this
    is discoverable via a Portfolio Analyst agent is novel. Bswen identifies
    over-loaded MCP servers as a cost problem; this source identifies
    over-calling LLMs as a separate, agent-level cost problem. The two patterns
    together give a more complete picture of where AI system costs hide.

## Guide Impact

- **Chapter 04 (Multi-agent orchestration patterns, planned)**: Add the
  "observatory plane" as a named third layer in multi-agent architecture,
  alongside the execution and coordination planes. The three-tier observability
  decomposition (performance / cost / audit) should be the recommended starting
  framework, with the GitHub production metrics as concrete evidence that all
  three tiers generate valuable signal. Cite Claim 1 ("Observability isn't
  optional") as the design principle; the production numbers as evidence.

- **Chapter 04 (Multi-agent orchestration patterns, planned)**: Add the
  autonomous remediation loop (Claim 5) as an advanced pattern: observatory
  → structured issues → downstream agent fixes. Frame it as requiring two
  preconditions: (a) audit agents that write actionable issue descriptions,
  and (b) downstream agents that can pick up issues autonomously. The 44%
  PR-conversion rate is the quality signal to track. Without it, the loop
  breaks: issues that are too vague will not be picked up.

- **Chapter 04 (Multi-agent orchestration patterns, planned)**: Add "chatty
  LLM calling" as a detectable anti-pattern for agent fleets, with the
  Portfolio Analyst approach as the remedy. Pair with Bswen's MCP token audit
  as the context-layer equivalent: both are invisible costs requiring
  purpose-built instrumentation.

- **Chapter 05 (Team adoption, planned)**: The `gh aw compile` / lock-file
  model (Claim 6) is relevant to teams adopting the `gh aw` platform — it
  shows observability workflows are versioned repository artifacts, not manual
  setups. Cross-reference with Faros's measurement framework: the GitHub
  observatory is the agent-fleet equivalent of Faros's team-level cohort
  measurement. For teams on the `gh aw` platform, the wizard-driven setup
  removes the implementation barrier to observability.

- **Chapter 04 (Multi-agent orchestration, planned) OR Chapter 02 (Harness
  Engineering)**: The metrics-as-orchestration-input claim (Claim 7) has
  architectural implications beyond observation: if metrics flow upward into
  higher-level orchestrators, the observatory is not just a monitoring layer
  but a coordination input. This should be noted as an advanced pattern —
  "closed-loop agent governance" — with the caveat that the mechanism is not
  fully described in the source.

## Extraction Notes

1. **Source is intentionally compact**: This is entry 13 in a 19-part blog
   series; each entry is designed to cover one topic area succinctly. The
   source is ~600-800 words. The depth comes from the production metrics, not
   from long-form explanation. Claims were fully exhausted in 8 extractions.

2. **One web fetch**: The source was fetched once with two passes (summary
   pass + verbatim pass). The full text was obtained. No sub-pages were linked
   or followed; the post does not link to the workflow specification files (only
   the `gh aw add-wizard` URLs, which point to GitHub file URLs rather than
   rendered documentation pages).

3. **Series context matters**: The post is positioned after "Fault
   Investigation Workflows" and before "Operations & Release Workflows" in the
   19-part series, suggesting the GitHub team views observability as a middle
   layer in the factory architecture (after task execution is established,
   before operations/release automation). This positioning corroborates Claim 8
   (observatory as a named architectural layer).

4. **Production numbers are live repository data**: The discussion counts (41,
   7, 93) and issue counts (9) and PR counts (4) are from a live GitHub
   repository that hosts Peli's Agent Factory. These numbers may have changed
   since publication (Jan 13, 2026); they represent a snapshot. The pattern
   they demonstrate (audit > performance > cost by output volume) is more
   durable than the specific counts.

5. **Claim 7 is partially inferred**: The "metrics as input to higher-level
   orchestrators" claim was surfaced by the Prospector's triage note, not
   directly from a quote in the post. The post describes the Metrics Collector
   as the "central nervous system" for performance data, which implies it feeds
   something; the specific mechanism is not described. Confidence is marked
   emerging rather than settled for this reason.

6. **No contradictions found**: Reviewed all existing source notes for
   claims that disagree with this source. No contradictions found that meet
   the MINER.md §4a filing threshold. The nearest tension (monitoring overhead
   vs. production efficiency) is a conditioning variable, not a contradiction.
