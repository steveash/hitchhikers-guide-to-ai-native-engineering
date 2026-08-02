---
source_url: https://cognition.com/blog/devin-fusion
source_type: blog-post
title: "Devin Fusion: Frontier Performance at 35% Lower Cost"
author: The Cognition Team
date_published: 2026-06-29
date_extracted: 2026-08-02
last_checked: 2026-08-02
status: current
confidence_overall: emerging
issue: "#2423"
---

# Devin Fusion: Frontier Performance at 35% Lower Cost

> Cognition introduces Devin Fusion, a "sidekick" multi-model harness that runs
> a frontier model and a cheaper model as two parallel, independently-cached
> agents — with the frontier model deciding what to delegate — plus a dynamic
> mid-session router that switches models for free at context-compaction
> boundaries. Reports a 35% cost reduction on FrontierCode (41% with Fable 5)
> at frontier-level quality, and that 88% of internally-merged PRs were driven
> entirely by the automated router.

## Source Context

- **Type**: blog-post (Cognition's own blog, cognition.com, anonymous
  corporate byline "By The Cognition Team," published "06.29.26" per the
  page's own byline format — the same MM.DD.YY convention used across this
  corpus's other Cognition posts). This is a product-launch/technical
  announcement post, not a named-author practitioner essay like
  `blog-cognition-multi-agents-working.md`.
- **Author credibility**: First-party vendor content from Cognition, the
  company that builds and sells Devin, announcing a new commercial feature
  ("Devin Fusion," in preview at app.devin.ai/signup). Cognition has a direct
  commercial interest in Fusion appearing cost-effective and high-quality. The
  post backs its claims with a named benchmark (FrontierCode, Cognition's own
  benchmark — see `blog-cognition-frontiercode.md`), five worked task-level
  case studies with before/after cost and score numbers (including one
  explicitly reported as a quality regression), and one internal usage
  statistic (88% of merged PRs router-driven). No named customer is quoted,
  no external/independent benchmark is cited, and the FrontierCode numbers
  reported here are Cognition grading its own product on its own benchmark.
- **Scope**: Covers the "sidekick" two-agent architecture, the rationale for
  it over simpler routing tools (including an explicit critique of Cognition's
  own prior "Smart Friend" pattern and Anthropic's "Advisor" tool), five
  representative FrontierCode task examples, dynamic mid-session routing tied
  to context compaction, aggregate cost/performance results, an internal
  "sanity check" usage statistic, and a broader argument for hybrid-model
  harnesses. Does **not** cover: the lightweight classifier's implementation,
  training, or accuracy; sample size or methodology for the 88% internal
  statistic; how models are selected for the main/sidekick roles at task
  start; or a customer-facing (as opposed to internal) validation of the
  reported cost savings.

## Extracted Claims

### Claim 1: Devin Fusion is a new multi-model harness that reportedly maintains frontier- and Fable-5-level performance at 35% lower cost on FrontierCode
- **Evidence**: Headline claim in the post's opening framing, backed by a
  benchmark chart (Concrete Artifacts) plotting score vs. average cost per
  task on FrontierCode Extended.
- **Confidence**: emerging (specific, quantified, first-party claim on the
  vendor's own benchmark; no independent replication)
- **Quote**: "Today, we're sharing our work on a new kind of multi-model harness, Devin Fusion, that is substantially better at mixing models while reducing costs and maintaining intelligence on real-world usage. We found it maintains frontier and Fable 5-level performance at 35% lower cost on FrontierCode, a new state-of-the-art coding benchmark that measures both code correctness and quality."
- **Our assessment**: This directly answers the third triage comment's key
  question (whether Fusion is a substantive technical advance over the
  "Smart Friend" pattern already documented in
  `blog-cognition-multi-agents-working.md`, or a marketing rebrand). It is
  more than a rebrand: the post explicitly frames Fusion as fixing specific,
  named problems with "existing tools for mixing models" — including
  Cognition's own prior Smart Friend design (see Claim 3) — with a concrete
  architectural change (persistent parallel context vs. per-call tool
  queries) and a quantified benchmark result Smart Friend's April post never
  reported. The FrontierCode score itself, however, is Cognition benchmarking
  its own product on its own benchmark, so "frontier-level performance" should
  be read as a vendor claim, not an independently verified one.

### Claim 2: The core architecture runs two parallel, fully independent agents — a frontier model and a cheaper "sidekick" model — where the frontier model decides what to delegate and defaults to delegating and monitoring rather than acting directly
- **Evidence**: Direct architectural description under "The Trick: Sidekick,"
  including a stated behavioral rule for the main agent.
- **Confidence**: emerging (first-party architecture description; no ablation
  isolating the effect of "the main agent should take minimal actions" from
  the rest of the system)
- **Quote**: "The key idea behind our architecture is to run two parallel agents: one with a frontier model, the other with a more cost-effective 'sidekick' model. Both are fully capable agents with their own toolsets and ability to gather & act on their own context." / "We've found that the main agent should take minimal actions, and only read what is absolutely necessary. By default it should delegate and monitor, while making the significant decisions: the plan, the interpretation of ambiguity, the final review."
- **Our assessment**: This is a specific, transferable design rule for any
  team building a similar delegator/executor pairing: the transferable
  finding here is not "use two models" but the behavioral split — the
  expensive model's job shrinks to planning, ambiguity resolution, and final
  review, while it deliberately avoids doing the read/verify legwork itself
  in order to preserve cost savings. This is a specific, actionable version
  of the general "orchestrator does less direct work" principle already
  present in this corpus's orchestrator-subagent coverage
  (`blog-anthropic-multi-agent-coordination-patterns.md`), narrowed
  specifically to the cost-optimization case rather than the
  context-window-management case.

### Claim 3: Sidekick is explicitly framed as fixing three named problems with prior model-routing approaches — including Cognition's own earlier "Smart Friend" tool and Anthropic's "Advisor" tool — the most concrete of which is that per-call consult tools incur an expensive cache miss on every query, whereas sidekick's two agents each maintain their own persistent, cached context
- **Evidence**: Three enumerated bullet points under "The Trick: Sidekick,"
  the third of which names the two specific prior tools it distinguishes
  itself from.
- **Confidence**: emerging (first-party architectural rationale; the
  magnitude of the cache-miss cost avoided is asserted, not quantified,
  in this post)
- **Quote**: "It retains real frontier intelligence rather than 'benchmark-score' intelligence. Routers often over-fit to specific benchmarks." / "It generalizes beyond single-prompt tasks and question-answering." / "It avoids costly cache misses when routing between models. We've previously explored a 'Smart Friend' tool, and Anthropic released a similar 'Advisor' tool. The core of both these ideas is to give one model a tool to query another model for helpful advice. The catch? Upon every call to the other model, the context for the task is not shared in a way that is cached, and you pay a very expensive price. In the sidekick setup, both the main model and sidekick model maintain their own persistent, cached contexts."
- **Our assessment**: This is the specific, load-bearing technical
  distinction between Fusion's "sidekick" pattern and the "Smart Friend"
  pattern this corpus already documents in detail
  (`blog-cognition-multi-agents-working.md` Claims 8-11): Smart Friend is a
  tool-call/consult pattern (primary model queries a larger model
  mid-task), which this post says pays a cache-miss cost on every query;
  sidekick instead runs two agents with independent, standing cached
  contexts and a delegation decision made by the frontier model rather than
  a query issued by a weaker one. This resolves the third triage comment's
  open question with a specific mechanism, not just a rebranding claim —
  though note the post does not quantify how large the avoided cache-miss
  cost actually is, so "costly" here is qualitative.

### Claim 4: The sidekick pattern is reported to scale better as the frontier model in the pair gets smarter — Fable 5 achieves a 41% cost reduction in the Fusion harness versus 35% for Opus- and GPT-5.5-class models, attributed to Fable 5 delegating and planning more effectively
- **Evidence**: Direct comparative statement plus an explicit caveat that the
  non-Fable numbers reflect more harness tuning than the Fable 5 numbers.
- **Confidence**: anecdotal (a first-party comparative percentage with an
  explicit, stated confound: unequal tuning effort between the two
  conditions being compared)
- **Quote**: "Recent models, and Fable 5 especially, perform unusually well in these multi-agent setups. Fable delegates work more intelligently, requests context more efficiently, and plans more precisely, all of which yield a larger cost improvement with minimal impact on intelligence." / "In our testing, Fusion with Fable 5 is 41% cheaper than a pure Fable 5 harness, versus 35% with Opus and GPT-5.5-level models. That gap may look modest, but we believe it understates the real difference. The non-Fable numbers reflect many rounds of tuning of the Devin Fusion harness; the Fable 5 numbers don't, since access was cut off before we could apply them."
- **Our assessment**: Cognition itself flags that the comparison is
  confounded (unequal tuning), which argues for treating the 41%-vs-35% gap
  as directional/suggestive rather than a clean apples-to-apples result. The
  underlying claim — that better frontier models make delegation-based
  routing patterns more valuable, not less — is a notable, falsifiable
  prediction: it argues against a "routing matters less as base models
  improve" intuition, and instead predicts routing/delegation architecture
  becomes a growing lever as frontier models improve their planning and
  self-assessment.

### Claim 5: Five worked FrontierCode task examples show sidekick delegation saves cost with no quality loss on test-running, mechanical removal, and reuse-heavy tasks, but a subtle-judgment-dependent feature task (a cross-team search selector) shows a quality regression (score 27 vs. a much higher baseline) when delegated
- **Evidence**: Five named task case studies, each with task description,
  difficulty/language tags, a qualitative explanation, and quantified
  cost-delta and score-delta figures.
- **Confidence**: emerging (specific, named, per-task quantified results;
  small sample of five hand-picked examples, explicitly described as
  illustrative "good and bad examples," not a systematic evaluation)
- **Quote**: "To better understand how the sidekick works, we inspected how using sidekick impacts cost and performance on a representative sample of FrontierCode tasks. Here we present both good and bad examples of sidekick usage."
- **Quote (bad example)**: "Add a team selector to the search bar (cross-team search), gated on a flag." / "Hard, multi-file React/Redux feature graded on its judgment calls." / "Devin delegated the coding, and the subtle intent was lost." / "When the judgment is the deliverable, delegating it backfires."
- **Our assessment**: The explicit inclusion of a negative example — cost
  dropped 28% ($6.84→$4.91) but score cratered to 27 (from an implied much
  higher baseline, given the pattern of the other four examples) — is a
  disclosed failure mode, not just a marketing highlight reel, which
  increases the credibility of the other four positive examples. The
  underlying rule stated ("when the judgment is the deliverable, delegating
  it backfires") is a concrete, transferable guardrail: delegate mechanical,
  verification-heavy, or reuse-heavy work to a cheaper sidekick, but keep
  judgment-dependent, taste-dependent, or ambiguous-intent work with the
  frontier model. This is a specific instance of the same principle named
  more abstractly in `blog-cognition-multi-agents-working.md` Claim 4
  ("real software requires a system that scales human taste and
  decision-making") — here applied specifically to a delegation-routing
  decision rather than to multi-agent architecture generally.

### Claim 6: Dynamic mid-session routing uses lightweight classifiers during task execution to switch models, timed specifically to context-compaction events so the model swap piggybacks on a cache miss that would happen anyway, effectively making model switching "free"
- **Evidence**: Direct mechanism description under "Dynamic Mid-Session
  Routing," including the explicit engineering rationale for the compaction
  timing choice.
- **Confidence**: emerging (specific, first-party mechanism description; no
  disclosure of the classifier's architecture, training, or accuracy)
- **Quote**: "It can be dangerous, however, to choose a model at the start and then realize later on that a different one would be better suited... To handle these cases, we use lightweight classifiers during task execution to signal when we need to switch to the main agent or use a different model entirely." / "We accomplish this by switching the model during context compaction, which would trigger a cache miss anyway. Each time we trigger compaction, we take it as an opportunity to evaluate the situation and switch the model that's in charge, effectively getting model switching 'for free'. Note that this means we can even 'upgrade' our sidekick model without going back to the main model, at no extra cache penalty."
- **Our assessment**: This is a specific, transferable cost-engineering
  technique: piggyback expensive state transitions (a model switch) onto an
  already-necessary expensive event (context compaction, which invalidates
  the prompt cache regardless) rather than treating them as separate cost
  centers. This is a concrete instance of context-rot-adjacent compaction
  engineering already documented in this corpus
  (`blog-anthropic-session-management-1m-context.md` Claim 8, "the model is
  at its least intelligent point when compacting") — here compaction timing
  is exploited as a free routing opportunity rather than treated only as a
  quality risk to manage.

### Claim 7: Aggregate results report a 35% cost improvement over frontier models (GPT-5.5, Opus 4.8) at matching performance without Fable 5, and a 41% cost reduction with Fable 5 at performance matching a traditional Fable-5-only harness
- **Evidence**: Direct results statement under "Results," restating and
  aggregating the headline claim (Claim 1) and the Fable-5-specific
  comparison (Claim 4) as the post's formal results summary.
- **Confidence**: emerging (first-party aggregate benchmark result; see
  Claim 4's confound caveat, which the post itself discloses, for the
  Fable-5-specific figure)
- **Quote**: "Without including Fable 5, our Devin Fusion multi-model harness gives a 35% cost improvement on FrontierCode relative to frontier models like GPT-5.5 and Opus 4.8, while maintaining performance matching the frontier." / "Fable 5 proved to be exceptionally performant in this multi-model harness, achieving a 41% cost reduction, while maintaining the same performance as Fable 5 in a traditional agent harness."
- **Our assessment**: This is the post's own formal restatement of Claims 1
  and 4 as headline results, not new evidence — recorded separately here
  because the Assayer's standard is to extract claims as they specifically
  appear, and this is the section a guide citation should point to for the
  "official" results figure rather than the looser opening framing.

### Claim 8: An internal "sanity check" — enabling Fusion for a set of Cognition employees — found that 88% of their merged PRs were driven entirely by the automated Fusion router (i.e., without a human manually overriding the router's model choice)
- **Evidence**: Direct statement under "The Sanity Check," framed as
  real-usage validation distinct from the benchmark results.
- **Confidence**: anecdotal (a single internal usage statistic; no disclosed
  sample size, user count, measurement window, or definition of what counts
  as "driven entirely by" the router, e.g., whether it excludes any session
  where a user ever manually pinned a model)
- **Quote**: "We set out to build a harness that not only performs well on benchmarks, but actually feels good in real use. We enabled Fusion for a set of users internally at Cognition, and we found that 88% of their merged PRs were driven entirely by the automated Fusion router." / "Of course, our end desire is to test this harness on a much wider set of tasks than what our internal usage covers."
- **Our assessment**: The post itself frames this as a preliminary check
  ("sanity check") on a narrow, internal-only population (Cognition's own
  employees, who are also the product's own builders) — the guide should
  cite this as a directional signal that the router's decisions were mostly
  accepted without override, not as evidence the router's model choices were
  optimal, since internal dogfooding populations are typically smaller,
  more forgiving, and more expert than a general customer base. The post
  explicitly acknowledges this limitation itself, which is a point in favor
  of the disclosure's honesty.

### Claim 9: Devin Fusion's benchmarking includes a Fable 5-inclusive comparison in which "Fusion + Fable 5" tops the FrontierCode Extended score/cost chart at 57.6 score / $3.00 average cost per task, ahead of a pure Fable 5 (medium) harness at 57.0 / $5.12 and Opus 4.8 (high) at 48.8 / $3.24
- **Evidence**: A labeled score-vs-cost chart with six named data points,
  reproduced in Concrete Artifacts.
- **Confidence**: emerging (specific, first-party benchmark chart data;
  point-in-time, and — per the post's own footnote — the Fable 5 data
  points were measured before a US government directive suspended Fable 5
  access, using an internal, pre-release version of the Fusion harness)
- **Quote**: (chart data, not prose — see Concrete Artifacts for the full
  extracted table)
- **Our assessment**: This chart gives FrontierCode Extended-subset absolute
  scores (57.6, 57.0, 48.8, etc.) in a different unit than the percentage
  scores reported in `blog-cognition-frontiercode.md` Claim 7's Extended
  results from the original FrontierCode 1.0 launch post (Opus 4.8: 51.8%
  on Extended). The two are not directly comparable as reported — this
  chart does not state whether its scores are a percentage, a raw rubric
  point total, or a different FrontierCode revision's scale, and the two
  Opus 4.8 Extended figures (48.8 here vs. 51.8% there) do not match on
  their face. A future source or the guide should not assume these are the
  same measurement; flag the unit ambiguity rather than treating 48.8 as
  "48.8%."

### Claim 10: A footnote discloses that Fable 5 access was suspended by a US government directive on June 12, 2026, and remained unrestored as of this post's June 29, 2026 publication date — Fable 5 results in this post were measured before the suspension, using an internal version of Devin Fusion current at that time
- **Evidence**: A dated, sourced footnote attached to the score/cost chart
  and the Results section.
- **Confidence**: settled (a specific, dated, externally-corroborated fact —
  see Cross-References; this corpus already documents the suspension
  independently via `blog-simonwillison-fable-mythos-access-directive.md`)
- **Quote**: "* On June 12, 2026, access to Fable 5 was suspended in accordance with a US government directive (anthropic.com/news/fable-mythos-access). As of this blogpost, access has not been restored. Results with Fable 5 are reported based on measurements from before this suspension and on the internal version of Devin Fusion at the time."
- **Our assessment**: This is not novel to the corpus — the suspension
  itself is independently documented in
  `blog-simonwillison-fable-mythos-access-directive.md` — but it is a
  useful, independently-dated corroboration from a second, unrelated
  vendor (Cognition, a Devin/coding-agent company, not an Anthropic
  competitor-commentary source) confirming both the June 12 suspension date
  and that access remained unrestored as of June 29. Cross-referenced
  against `blog-vercel-ai-gateway-fable-5-restored.md` (access restored,
  per Vercel, effective July 1, 2026), this places the suspension window
  Cognition is describing (June 12 – at least June 29) consistently inside
  the roughly three-week gap independently documented elsewhere in this
  corpus — no discrepancy found. This also caveats Claim 4 and Claim 9's
  Fable 5 figures: they are measurements against a since-superseded internal
  Fusion build, not the harness as tuned and shipped in this post.

### Claim 11: Cognition names one concrete unresolved engineering constraint without disclosing its solution — most prompt-cache entries expire after only 5 minutes, which the sidekick architecture's persistent, independently-cached parallel contexts must be engineered around
- **Evidence**: A single sentence flagged explicitly as an open engineering
  challenge, immediately followed by an invitation for readers to think
  about solutions.
- **Confidence**: anecdotal (a disclosed constraint with no stated solution
  or workaround described)
- **Quote**: "Of course, there are many implementation details we had to overcome to achieve the capabilities of Devin Fusion. For example, most cached inputs only have a 5-minute expiry. We encourage the reader to think about how to engineer around this. We'd love to trade notes!"
- **Our assessment**: This is a specific, concrete constraint (5-minute
  cache TTL) relevant to any team building a similarly long-running,
  multi-agent, cache-dependent harness — sessions or delegated sub-tasks
  that run longer than 5 minutes without a cache-touching request would, by
  this logic, fall out of cache and lose the persistent-context cost
  advantage Claim 3 attributes to the sidekick design. Cognition explicitly
  declines to disclose its mitigation, so the guide should flag this as a
  known open problem in this space rather than a solved one.

### Claim 12: Cognition frames hybrid-model harnesses as an industry-wide inflection point, driven by rising frontier model costs and a growing diversity of specialized, differently-priced models, arguing "the age of using one model for all of your work is coming to an end"
- **Evidence**: Closing section ("The rising importance of hybrid-model
  harnesses") with an explicit causal argument and analogy.
- **Confidence**: anecdotal (a stated industry prediction/framing, not a
  measured trend with supporting data beyond the post's own examples)
- **Quote**: "The age of using one model for all of your work is coming to an end. The rising costs of frontier intelligence are reaching prohibitive levels in engineering organizations small and large... You wouldn't drive a Lamborghini to the grocery store, so why should you take a model that can discover zero-day vulnerabilities in software and use it to round the corner of a button?" / "at Cognition, we find some models to be particularly good at UI testing, and different models to be good at identifying complicated bugs in PRs... as models emerge that excel at particular languages, tasks, or libraries, investing in multi-model capabilities only becomes more important."
- **Our assessment**: This closing argument bundles two distinct claims
  worth separating for guide purposes: (a) a cost-driven argument for
  delegating cheap/easy work to cheaper models (the sidekick pattern this
  post is about), and (b) a specialization-driven argument for routing by
  model strength regardless of cost tier (echoing
  `blog-cognition-multi-agents-working.md` Claim 11's frontier-to-frontier
  "capability router" distinction, and
  `blog-addyosmani-code-agent-orchestra.md` Claim 9's route-by-task-type
  recommendation). This post's own architecture (sidekick) only directly
  addresses (a); claim (b) is asserted as a motivation but not itself
  demonstrated by any evidence in this post.

## Concrete Artifacts

### FrontierCode Extended: score vs. average cost per task (headline chart)
```
Source: cognition.com/blog/devin-fusion, hero chart, "Score on FrontierCode
Extended Benchmark and average cost per task"

Configuration          Score   Avg. cost/task
Fusion + Fable 5*       57.6   $3.00
Fable 5 (medium)*       57.0   $5.12
Opus 4.8 (high)         48.8   $3.24
Fusion                  47.9   $2.38
GPT-5.5 (high)          44.8   $3.64
GLM-5.2                 43.0   $2.70

* Fable 5 access suspended June 12, 2026 per US government directive;
  Fable 5 figures measured before suspension, on an internal Devin Fusion
  build (see Claim 10).
```

### Five worked FrontierCode task examples (sidekick good/bad cases)
```
Source: cognition.com/blog/devin-fusion, "Examples of Sidekick in Action"

1. Modernize search.js (ES6, JS refactor, easy)
   "Small rewrite, but a slow, expensive test suite to verify it. Devin
   wrote the diff and handed off the slow test run."
   cost: -62% ($3.55 -> $1.37)   score: +2, 98 -> 100

2. Rip out OpenTracing integration (Mattermost server, Go, medium/deprecation)
   "Mechanical removal across many files. Few real judgment calls to make."
   cost: -32% ($3.80 -> $2.57)   score: -1, 98 -> 97

3. JSON-Schema oneOf-with-const handling (Python, medium/feature)
   "A medium feature Devin only partly solves. Devin reaches the same
   partial result either way, so the sidekick just makes it cheaper."
   cost: -38% ($5.08 -> $3.13)   score: -4, 54 -> 50

4. Team selector / cross-team search (TypeScript, hard/feature)
   "Hard, multi-file React/Redux feature graded on its judgment calls.
   Devin delegated the coding, and the subtle intent was lost. When the
   judgment is the deliverable, delegating it backfires."
   cost: -28% ($6.84 -> $4.91)   score: -27, [baseline] -> 27

5. LangChain4j WebSocket MCP transport into Quarkus (Java, hard/feature)
   "Hard task, but mostly mechanical: reuse what's upstream. The sidekick's
   changes needed no rework."
   cost: -25% ($5.25 -> $3.93)   score: +12, 69 -> 81
```

### Dynamic mid-session routing mechanism, verbatim
```
Source: cognition.com/blog/devin-fusion, "Dynamic Mid-Session Routing"

"We use lightweight classifiers during task execution to signal when we
need to switch to the main agent or use a different model entirely... We
accomplish this by switching the model during context compaction, which
would trigger a cache miss anyway. Each time we trigger compaction, we take
it as an opportunity to evaluate the situation and switch the model that's
in charge, effectively getting model switching 'for free'."
```

## Cross-References

- **Corroborates**:
  - `blog-cognition-multi-agents-working.md` Claims 8-11 (the "Smart
    Friend" small/large model pairing, its two named engineering
    sub-problems, and the escalation-vs-capability-routing distinction):
    this source's Claim 3 explicitly names Smart Friend as a direct
    predecessor and states the specific technical limitation (per-call
    cache misses) that sidekick's persistent parallel contexts are designed
    to fix. This directly answers the third triage comment's question about
    whether Fusion is novel beyond a rebrand — it is a distinct
    architecture (parallel independently-cached agents with
    frontier-decided delegation vs. a tool-call consult pattern), not the
    same pattern renamed.
  - `blog-cognition-frontiercode.md` (the FrontierCode benchmark's
    methodology, task-authoring process, and 1.1 revision): this source
    uses FrontierCode as its evaluation benchmark throughout and supplies a
    new Extended-subset data point (Claim 9) not present in that note's
    already-documented Main-leaderboard and 1.0-launch figures — though see
    Claim 9's "Our assessment" for a flagged unit-comparability caveat
    between this post's absolute scores and that note's percentage scores.
  - `blog-anthropic-session-management-1m-context.md` Claim 8 ("the model
    is at its least intelligent point when compacting"): this source's
    Claim 6 (routing model switches through context-compaction events)
    treats the same compaction moment this Anthropic source flags as a
    quality risk, instead as a free opportunity to change which model is in
    charge — a related but distinct engineering use of the same underlying
    fact (compaction already invalidates the cache and resets context).
  - `blog-addyosmani-code-agent-orchestra.md` Claim 9 (route planning to
    cheaper models, implementation to capable models, review to
    security-focused models) and `docs-github-copilot-cli-auto-model-selection-task-based-routing.md`
    (task-dimension-aware auto model routing, rolled out across GitHub
    Copilot surfaces): both corroborate the general industry direction
    toward task-aware, cost-conscious multi-model routing that this
    source's Claim 12 frames as an industry inflection point — though this
    source's sidekick pattern (persistent parallel agents, frontier-decided
    delegation) is architecturally distinct from static per-task-type
    routing (Osmani, GitHub Copilot auto).
  - `blog-simonwillison-fable-mythos-access-directive.md` (the June 12,
    2026 US government directive suspending Fable 5/Mythos 5 access) and
    `blog-vercel-ai-gateway-fable-5-restored.md` (access restored, per
    Vercel, effective July 1, 2026): this source's Claim 10 footnote is a
    second, independent (non-Anthropic-adjacent) vendor confirming both the
    suspension date and that access remained unrestored through this post's
    June 29, 2026 publication date — consistent with, and falling inside,
    the suspension window already documented by those two sources.

- **Contradicts**: None identified. One near-miss was evaluated: this
  source's Claim 9 chart reports Opus 4.8 at 48.8 on FrontierCode Extended,
  while `blog-cognition-frontiercode.md` Claim 7 reports Opus 4.8 at 51.8%
  on FrontierCode Extended from the original 1.0 launch post. This does not
  meet the `agents/MINER.md` §4a bar for a filed contradiction: the two
  figures use unstated and seemingly different units/scales (this post
  never states whether 48.8 is a percentage or a different point scale),
  and FrontierCode underwent a 1.1 methodology revision (documented in
  `blog-cognition-frontiercode.md` Claim 8-9) between the two posts, so a
  numeric mismatch is expected from a benchmark revision rather than a
  factual disagreement about the same measurement. Flagged as an
  unresolved unit-comparability caveat in Claim 9's "Our assessment"
  instead of filed as a contradiction.

- **Extends**:
  - `blog-cognition-multi-agents-working.md`: that source's Smart Friend
    pattern (Claims 8-11) is a reactive, tool-call-based escalation
    pattern with a disclosed negative result (SWE-1.5 as primary was "not
    good enough"); this source's sidekick pattern is architecturally
    distinct (parallel independent agents, not a query tool) and reports
    only positive/mixed results (Claim 5's one disclosed negative example
    is task-specific, not a wholesale pattern failure like Smart Friend's
    SWE-1.5 admission). Together the two posts trace an explicit lineage:
    Smart Friend (April 2026) named the escalation-routing cache-cost
    problem; Devin Fusion (June 2026) claims to solve it with a different
    architecture.
  - `blog-anthropic-multi-agent-coordination-patterns.md`: this source's
    Claim 2 (the frontier "main" agent should take minimal direct action,
    delegating and monitoring instead) is a cost-motivated instance of the
    general orchestrator-does-less-direct-work principle in that source's
    taxonomy, narrowed to a two-tier cost/capability pairing rather than a
    general coordination-overhead argument.

- **Novel**:
  - The specific claim that per-call consult/tool-based model-routing
    patterns (Smart Friend, Anthropic's Advisor) incur an "expensive"
    cache-miss cost on every query, and that running two agents with
    independent persistent caches instead avoids this — no prior corpus
    source names prompt-cache invalidation as the specific mechanism
    distinguishing a "consult tool" pattern from a "parallel agent" pattern.
  - Dynamic mid-session model switching deliberately timed to
    context-compaction events specifically to make the switch "free" by
    piggybacking on an unavoidable cache miss — new to this corpus.
  - Five named, quantified (cost delta + score delta) task-level case
    studies of delegation succeeding and failing on the same benchmark —
    more granular than any prior corpus source's model-routing evidence,
    which has generally been aggregate statistics or qualitative
    descriptions rather than per-task before/after numbers.
  - The disclosed, unresolved 5-minute prompt-cache-TTL engineering
    constraint (Claim 11) — a specific, concrete implementation detail not
    present in this corpus's other multi-model routing sources.

## Guide Impact

- **Chapter 04 (Cost & Reliability) / Chapter 06 (Model Selection &
  Routing)**: Add the sidekick architecture (Claim 2) as a named pattern
  distinct from "Smart Friend"/consult-tool routing: two parallel agents
  with independent persistent cached contexts, frontier model decides
  delegation and does minimal direct work. Cite the specific mechanism
  (Claim 3) — avoiding per-call cache misses — as the concrete reason to
  prefer this shape over a query-tool pattern for latency/cost-sensitive
  multi-model systems.

- **Chapter 04 (Cost & Reliability)**: Add Claim 5's guardrail as a
  decision rule for what to delegate to a cheaper sidekick model:
  mechanical, verification-heavy, or reuse-heavy work delegates well;
  ambiguous-intent or judgment-dependent work (UI/UX subtlety, "what did
  the user actually mean") does not and can silently regress quality even
  while reducing cost. Recommend guide readers watch for this specific
  failure mode (cost improves, judgment-dependent quality quietly drops)
  rather than assuming a cost win implies no quality risk.

- **Chapter 04 (Cost & Reliability)**: Add Claim 6's compaction-timed model
  switching as a specific cost-engineering technique: if a system already
  pays a cache-invalidation cost at compaction, treat that boundary as a
  natural, low-marginal-cost point to reconsider model choice, rather than
  switching models at arbitrary points mid-session.

- **Chapter 02 (Agentic Patterns)**: Note Claim 8 (88% of internally merged
  PRs router-driven) only as a directional, small-sample, vendor-internal
  signal — not as evidence the router's choices are optimal for external
  customers — consistent with how this corpus treats other self-reported,
  undisclosed-sample-size vendor usage statistics.

- **Chapter 06 (Model Selection & Routing)**: When citing FrontierCode
  scores from this post (Claim 9) alongside `blog-cognition-frontiercode.md`,
  flag the unit-comparability caveat explicitly (this post's absolute
  scores vs. that note's percentage scores) rather than treating them as
  directly comparable data points.

## Extraction Notes

- WebFetch's default summarizing pass on this URL returned a reasonably
  faithful but condensed, paraphrased summary (consistent with the pattern
  already recorded for other Cognition posts in this corpus, e.g.
  `blog-cognition-multi-agents-working.md` and `blog-cognition-devin-desktop.md`
  Extraction Notes). The full article was instead fetched via `curl` with a
  browser user-agent, the `<article>` element isolated from the raw HTML,
  and HTML tags stripped with a Python regex-based tag stripper (no
  `html2text` binary was available in this environment). All quotes above
  were taken from that raw-text extraction; each quote was located and
  verified character-for-character against the extracted plain text before
  being included in this note.
- The benchmark chart (Concrete Artifacts, "FrontierCode Extended: score vs.
  average cost per task") was reconstructed from the chart's underlying
  text labels as they appear in the page's raw HTML/text extraction (data
  point labels and axis values rendered as plain text alongside an SVG/canvas
  chart) — the numeric pairing of each named configuration to its score and
  cost was preserved as it appeared in source order in the extracted text,
  not re-derived from a visual reading of the chart image.
- One score figure (task 4, team selector) has an unclear baseline: the
  extracted text shows "score -2754 -> 27," which is presented in Concrete
  Artifacts as "score: -27, [baseline] -> 27" — the raw extracted text ran
  the delta and the "before" score together without a clear separator
  (likely "-27" delta immediately followed by "54 -> 27" or similar in the
  original visual layout, where the tag-stripping process merged two
  adjacent numeric labels). The "27" final score and the negative-percentage
  direction are unambiguous from context (a stated quality regression); the
  exact pre-delegation baseline score is not confidently recoverable from
  the extracted text and is left unstated rather than guessed. This
  ambiguity does not affect any claim above, none of which cites the exact
  baseline number.
- No sub-pages were followed. The post links only to app.devin.ai/signup
  (a product signup page, not a substantive content page) and to
  anthropic.com/news/fable-mythos-access (already independently documented
  in this corpus via `blog-simonwillison-fable-mythos-access-directive.md`,
  so not re-fetched separately here per `agents/MINER.md` §1's guidance to
  follow linked pages only when they would add information beyond a
  footnote-level mention).
- Cross-references verified before writing: re-read
  `blog-cognition-multi-agents-working.md` in full and confirmed Claims 4,
  8, 9, 10, 11 by number and content; re-read `blog-cognition-frontiercode.md`
  in full and confirmed Claims 7, 8, 9 by number and content; re-read
  `blog-anthropic-session-management-1m-context.md` and confirmed Claim 8 by
  number and content; re-read `blog-addyosmani-code-agent-orchestra.md` and
  confirmed Claim 9 by number and content; read
  `docs-github-copilot-cli-auto-model-selection-task-based-routing.md` in
  full; read `blog-simonwillison-fable-mythos-access-directive.md` and
  `blog-vercel-ai-gateway-fable-5-restored.md` frontmatter/summaries and
  confirmed the June 12 suspension / July 1 restoration dates against this
  source's June 29 publication date. No claim number was guessed or
  approximated.
- A candidate contradiction (this source's Opus 4.8 FrontierCode Extended
  score of 48.8 vs. `blog-cognition-frontiercode.md`'s 51.8% from the 1.0
  launch post) was evaluated against the `agents/MINER.md` §4a filing bar
  and did not meet it — see Cross-References → Contradicts for the full
  reasoning. No contradiction issue filed.
- Confidence is rated `emerging` overall: this is a first-party vendor
  product-launch post with several specific, quantified claims (cost/score
  deltas on five named tasks, a benchmark chart, a dated and
  externally-corroborated government-directive footnote) that exceed pure
  marketing framing, and it discloses at least one negative result (Claim
  5's judgment-task regression) and one unresolved constraint (Claim 11's
  cache-TTL problem) rather than reporting only successes. It does not
  reach `settled` because no figure is independently replicated, sample
  sizes and methodology are undisclosed throughout, and the central
  cost-savings claims (Claims 1, 4, 7) are all measured on Cognition's own
  benchmark by Cognition itself.
