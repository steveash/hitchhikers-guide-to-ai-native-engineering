---
source_url: https://simonwillison.net/2026/May/11/james-shore/
source_type: blog-post
title: "A quote from James Shore"
author: James Shore (quoted by Simon Willison)
date_published: 2026-05-11
date_extracted: 2026-05-19
last_checked: 2026-05-19
status: current
confidence_overall: emerging
issue: "#804"
---

# James Shore: You Need AI That Reduces Maintenance Costs

> James Shore articulates a precise economic framework: AI coding agents only produce
> genuine net productivity gains if they reduce maintenance costs by exactly the inverse
> of their productivity multiplier — 2× faster output requires ½ the maintenance cost,
> otherwise total maintenance burden increases; and stopping AI use does not remove the
> accumulated maintenance debt.

## Source Context

- **Type**: blog-post (Simon Willison link-blog quotation, May 11, 2026; relays two
  paragraphs from James Shore's article "You Need AI That Reduces Maintenance Costs" at
  https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs.
  The Willison page is the canonical source URL per the issue submission. The Shore article
  was fully accessible and read as a substantive linked page per extraction process §1;
  all extraction below draws from both sources, with the Shore article providing the
  detailed mathematical framework and worked examples.)
- **Author credibility**: James Shore is a software engineering consultant and author of
  *The Art of Agile Development*, with decades of practitioner experience specializing in
  late-stage startup engineering turnarounds. His framing of maintenance cost dynamics
  comes from direct consulting experience with teams whose productivity had collapsed after
  5–9 years of compounding technical debt. Simon Willison is the creator of Django and
  one of the highest-signal independent AI tooling commentators; his selection of this
  quotation for his curated feed is itself a relevance signal. Tags on the Willison post:
  ai, generative-ai, llms, ai-assisted-programming, coding-agents, agentic-engineering.
- **Scope**: Covers the economic relationship between AI coding productivity gains and
  maintenance cost changes, including a mathematical model for evaluating whether AI
  tools produce net positive or net negative long-term productivity outcomes, and a
  specific warning about maintenance debt lock-in when AI use is discontinued. Also
  covers Shore's synthesis of available evidence about current agent effects on
  maintenance costs. Does NOT cover: specific tools, team structures, harness
  configurations, measurement methodologies, or empirical data. The Shore article is
  analytical and argumentative, not empirical.

## Extracted Claims

### Claim 1: AI coding agents only produce a net productivity benefit if they reduce maintenance costs by exactly the inverse of their productivity gain ratio

- **Evidence**: Mathematical derivation from a maintenance cost model informed by
  crowdsourced practitioner estimates. Shore presents the inverse relationship as a
  mathematical necessity, not an empirical finding: if an AI doubles code output, it must
  halve per-unit maintenance costs to hold the overall maintenance burden constant.
- **Confidence**: emerging (the mathematical logic is sound; the maintenance cost model
  is built on crowdsourced estimates, not controlled data, but the model's qualitative
  dynamics are widely recognized)
- **Quote**: "The math only works if the LLM decreases your maintenance costs, and by
  exactly the inverse of the rate it adds code. If you double your output and your cost
  of maintaining that output, two times two means you've quadrupled your maintenance
  costs. If you double your output and hold your maintenance costs steady, two times one
  means you've still doubled your maintenance costs."
  — James Shore, as quoted on the Willison page (verbatim from
  https://simonwillison.net/2026/May/11/james-shore/)
- **Our assessment**: This is the central quantitative framework of the source. It
  converts vague questions about "AI ROI" into a specific testable criterion: measure
  whether maintenance costs per unit of code have decreased by at least the inverse of
  the productivity multiplier. Most team productivity measurements capture coding speed
  but not maintenance cost changes. Shore's framework implies that a team measuring only
  velocity is measuring the wrong thing.

### Claim 2: Maintenance costs compound over time until they consume most of a team's productive capacity — the dynamics are not linear

- **Evidence**: A maintenance cost model built on crowdsourced developer estimates
  (Shore describes a "Wisdom of the Crowd" survey of ~50 developers). Under the model,
  each month of code written generates ongoing maintenance costs for all subsequent years.
  Shore's hypothetical estimates: 10 days of maintenance in year 1, 5 days per year
  thereafter, per month of code written.
- **Confidence**: emerging (the model uses illustrative numbers; the qualitative dynamic
  is widely documented in the practitioner community)
- **Quote**: "According to our crowd's maintenance estimates, you'll spend more than half
  your time on maintenance after 2½ years. After ten years, you can hardly do anything
  else."
  — James Shore, https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs
- **Our assessment**: The specific numbers are illustrative, but Shore's key insight is
  that the relationship is nonlinear and cumulative. This framing explains why the
  question "how much does your AI tool increase maintenance costs?" is not a negligible
  engineering concern but a central business risk. Small changes in the per-unit
  maintenance cost multiplier have large long-term effects on team capacity. Shore
  further notes: "Halving the crowd's maintenance estimates gives you three more years
  before you hit the 50% mark. Doubling them sees you below 50% in less than a year."

### Claim 3: If an AI tool doubles code output but also doubles maintenance costs per unit, the productivity gain disappears within ~5 months and the team ends up worse off than if they never used the tool

- **Evidence**: Worked example in Shore's mathematical model, using "Rock Lobster"
  (fictional AI agent) that doubles output but doubles per-unit maintenance costs.
- **Confidence**: emerging (model-derived, not empirically measured; the mechanism is
  mathematically sound; the timeframe is sensitive to the model's initial assumptions)
- **Quote**: "About five months after you start using Rock Lobster, your productivity is
  back down to where you started, and a few months after that, it's worse than it would
  have been had you never touched Rock Lobster in the first place."
  — James Shore, https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs
- **Our assessment**: The ~5-month timeframe is model-dependent, but the directional
  result is consistent with the empirical finding in `paper-miller-speed-cost-quality.md`
  Claim 4 (velocity gains decay by months 3–6 post-Cursor-adoption). Shore's model
  provides a mechanistic explanation for that empirical pattern: the maintenance cost
  accumulated by the increased code volume eventually overwhelms the productivity gain
  from speed. Treat the specific timeframe as an illustration, not a prediction.

### Claim 4: Stopping AI agent use does not remove the accumulated maintenance debt — teams are "permanently indentured" to the higher maintenance burden

- **Evidence**: Logical consequence of the maintenance cost model: the maintenance debt
  is in the existing codebase, not in the AI tool itself. If the tool increases per-unit
  maintenance costs, that cost persists in the code even after the tool is discontinued.
- **Confidence**: emerging (the logical deduction is valid given the model's premises;
  the empirical question of whether AI-generated code has higher maintenance costs is
  addressed by Miller et al.)
- **Quote**: "When you stop using the agent, all the productivity benefit goes away...
  but the added maintenance costs don't! As long as that code's still around, you're
  stuck with lower productivity than if you had never touched the agent at all."
  — James Shore, https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs
- **Our assessment**: This is the "Hotel California" lock-in argument. It directly
  challenges the framing of AI coding as a low-risk experiment: if the tool increases
  maintenance costs, discontinuing the experiment does not reset the outcome. The
  implication for pilot programs is significant — a pilot that measures only velocity
  over 30–90 days will not detect the maintenance cost accumulation that persists after
  the pilot ends. The exit option is less clean than it appears.

### Claim 5: Shore's synthesis of available evidence suggests current coding agents increase maintenance costs rather than reduce them

- **Evidence**: Shore's own reading of published sources ("the finest news sources"),
  not a formal review or citation list. He acknowledges partial positive evidence
  ("Some people do say they help them understand large systems better") but concludes
  that the scale of reduction needed has not been demonstrated.
- **Confidence**: anecdotal (author synthesis; not a systematic review; consistent with
  the empirical data in `paper-miller-speed-cost-quality.md`)
- **Quote**: "All my reading of the finest news sources says that coding agents increase
  maintenance costs. Some people do say they help them understand large systems better.
  But big decreases in costs, of the size we need to see? No. Just the opposite."
  — James Shore, https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs
- **Our assessment**: Shore's conclusion aligns with what the Miller et al. study
  actually measures (41.6% persistent increase in cognitive complexity, 30.3% increase
  in static analysis warnings). His inference is not an outlier position — it is
  consistent with the best available peer-reviewed evidence on the question. The guide
  should present this claim not as one practitioner's view but as a position that the
  empirical literature currently supports.

### Claim 6: Teams must invest as much effort in reducing maintenance costs as in increasing coding speed — the two objectives are equally important for net productivity

- **Evidence**: Prescription derived from the model, stated as the operational conclusion.
- **Confidence**: anecdotal (prescription, not an empirical finding; but logically follows
  from Claims 1–5)
- **Quote**: "So, yeah, go ahead, chase improvements to your coding speed. But spend just
  as much time chasing improvements to your maintenance costs. Or you, too, will be
  trapped in Hotel California."
  — James Shore, https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs
- **Our assessment**: This is Shore's direct recommendation for teams adopting AI coding
  tools. It implies that team adoption strategies currently focused on maximizing
  velocity without equivalent attention to maintenance cost impact are economically
  miscalibrated. A team adoption framework should include explicit success criteria for
  maintenance cost metrics (e.g., cognitive complexity, static analysis warnings, PR
  review time per line) — not just for velocity metrics.

### Claim 7: Alternative AI levers exist that can improve net productivity without increasing code volume — AI tools that make maintenance work itself more efficient

- **Evidence**: Shore's own suggestion as an alternative to the failing pattern. He
  distinguishes between AI that makes coding faster (potentially harmful under the model)
  and AI that makes maintenance work faster (unambiguously beneficial under the model).
- **Confidence**: anecdotal (prescriptive suggestion; reasonable but not yet evidenced
  in the corpus)
- **Quote**: "There's other levers to pull, such as AI that makes maintenance itself more
  productive, even if it doesn't make the code more maintainable."
  — James Shore, https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs
- **Our assessment**: This reframes the AI tooling evaluation question usefully. Tools
  that automate dependency upgrades, suggest refactoring for complexity reduction,
  generate tests for existing code, or accelerate code review have maintenance-reducing
  effects that improve the model's outcome without the code-volume problem. The guide
  should distinguish these two categories of AI tooling: velocity-increasing tools
  (which require the inverse maintenance cost reduction to be beneficial) vs.
  maintenance-reducing tools (which are beneficial regardless of the velocity question).

### Claim 8: The problem Shore describes is not hypothetical — he observed exactly this productivity collapse pattern at late-stage startups across his career as a consultant

- **Evidence**: Shore's first-person account: "In my career as a consultant, I
  specialized in late-stage startups, and they all had the exact problem shown in the
  graph above. About 5-9 years in, they'd notice their teams were no longer getting
  shit done, and then they'd call me."
- **Confidence**: anecdotal (first-person consulting history; not independently
  verifiable; but consistent with widely documented "productivity death spiral" patterns
  in long-running codebases)
- **Quote**: "In my career as a consultant, I specialized in late-stage startups, and
  they all had the exact problem shown in the graph above. About 5-9 years in, they'd
  notice their teams were no longer getting shit done, and then they'd call me."
  — James Shore, https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs
- **Our assessment**: This claim grounds the mathematical model in documented real-world
  outcomes. Shore is not building a hypothetical model — he is building a model to
  describe a pattern he has repeatedly observed. The 5–9 year timeline matches the
  maintenance curve in the model (which shows >50% maintenance overhead appearing at
  2.5 years under his baseline estimates). His consulting experience suggests the model
  underestimates actual maintenance costs (teams paper over the problem with hiring or
  rewrites, so the visible crisis takes longer to appear). The AI scenario compresses
  the timeline: if AI doubles code output while doubling per-unit maintenance costs,
  the same collapse appears within months, not years.

## Concrete Artifacts

### The Willison Post (verbatim quotation, from https://simonwillison.net/2026/May/11/james-shore/)

```
Date: 11th May 2026

[Quoted block, paragraph 1:]
"Your AI coding agent, the one you use to write code, needs to reduce your maintenance
costs. Not by a little bit, either. You write code twice as quick now? Better hope
you've halved your maintenance costs. Three times as productive? One third the
maintenance costs. Otherwise, you're screwed. You're trading a temporary speed boost
for permanent indenture. [...]"

[Quoted block, paragraph 2:]
"The math only works if the LLM decreases your maintenance costs, and by exactly the
inverse of the rate it adds code. If you double your output and your cost of maintaining
that output, two times two means you've quadrupled your maintenance costs. If you double
your output and hold your maintenance costs steady, two times one means you've still
doubled your maintenance costs."

Attribution: — James Shore, You Need AI That Reduces Maintenance Costs
```

### Shore's Mathematical Framework (verbatim from the Shore article)

```
Source: James Shore, "You Need AI That Reduces Maintenance Costs"
        https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs

MAINTENANCE COST MODEL (crowdsourced estimates from ~50 developers):
  Per month of code written:
    - Year 1:           ~10 days of maintenance
    - Each year after:  ~5 days of maintenance, indefinitely

THRESHOLDS (from model):
  With baseline estimates:   >50% time on maintenance after 2.5 years
  With halved estimates:     >50% time on maintenance after ~5.5 years
  With doubled estimates:    >50% time on maintenance in <1 year

THE INVERSE REQUIREMENT:
  AI productivity multiplier   Required maintenance cost multiplier
  ─────────────────────────    ─────────────────────────────────────
  2× (double output)           0.5× (halve maintenance costs)
  3× (triple output)           0.33× (one-third maintenance costs)
  N× output                    1/N× maintenance costs

FAILURE CASE (AI doubles output AND doubles maintenance costs):
  Timeline to baseline productivity recovery:  ~5 months
  Timeline to net-negative outcome:            ~7–8 months
  Lock-in effect: stopping AI use removes velocity gain
                  but NOT accumulated maintenance burden
```

### Shore's Alternative Levers Framing

```
Source: James Shore, "You Need AI That Reduces Maintenance Costs"

Category 1 — Velocity-increasing AI tools (dangerous without maintenance reduction):
  - AI that generates more code faster
  - Risk: Increases maintenance burden unless per-unit cost drops proportionally
  - ROI test: Is maintenance cost per unit of code going down?

Category 2 — Maintenance-reducing AI tools (beneficial regardless of velocity):
  - AI that makes maintenance work itself more efficient
  - Dependency upgrade automation
  - Complexity reduction / refactoring assistance
  - Test generation for existing code
  - Code review acceleration
  - Risk: Lower (directly reduces the compounding maintenance burden)
```

## Cross-References

- **Corroborates**: `paper-miller-speed-cost-quality.md` Claim 2 — "Cognitive complexity
  increases by 41.6% post-adoption, persistently." The Miller et al. empirical finding
  directly supports Shore's Claim 5 assertion that current coding agents increase
  maintenance costs. Cognitive complexity is a direct proxy for Shore's "maintenance
  costs" — harder-to-read code takes more time to maintain, debug, and modify. The
  persistence of the increase (no decay) is exactly the "permanent indenture" pattern
  Shore describes in Claim 4.

- **Corroborates**: `paper-miller-speed-cost-quality.md` Claim 3 — "Static analysis
  warnings (reliability, maintainability, security) increase by 30.3% post-adoption,
  persistently." A second independent measurement of rising maintenance costs in
  AI-adopting codebases. Together, Claims 2 and 3 from Miller et al. constitute the
  empirical evidence base for Shore's model-derived claim that current coding agents
  increase rather than decrease maintenance costs.

- **Corroborates**: `paper-miller-speed-cost-quality.md` Claim 4 — "Velocity gains last
  only ~2 months, then disappear entirely." The empirical decay timeframe (months 3–6)
  is consistent with Shore's model-derived estimate (~5 months under the doubled-
  maintenance-cost scenario). Shore's model provides a mechanistic explanation for what
  Miller et al. measure empirically: the maintenance burden from increased code volume
  eventually overwhelms the velocity gain. The two sources arrive at the same qualitative
  result from independent directions (theoretical model vs. difference-in-differences
  study), strengthening the overall finding significantly.

- **Corroborates**: `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 2 —
  "Normalization of deviance is a real risk in agentic engineering — each successful
  unreviewed AI output increases false confidence for the next." Shore's scenario of
  teams that "kinda sorta don't actually read the code before smashing the approve button"
  is the exact behavioral mechanism Willison names as normalization of deviance. Shore
  provides the economic model showing why this behavior is catastrophic; Willison names
  the psychological mechanism that produces it. Together they establish both the cause
  and the consequence of inadequate AI code review.

- **Corroborates**: `blog-bvp-shopify-ai-playbook.md` Claim 4 — "Code review has
  become 'a big bottleneck' due to increased AI-generated code volume." Shopify's
  executive observation about review bottlenecks is the organizational symptom of the
  economic dynamic Shore models. The volume pressure that creates review shortcuts
  (described by Shopify as a "big bottleneck") is precisely the mechanism through which
  maintenance costs increase in Shore's worked example.

- **Extends**: `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 7 — "The
  SDLC was designed for ~200 LOC/day and does not scale to 2,000 LOC/day." Willison
  names the throughput disruption; Shore provides the economic model explaining why the
  throughput disruption matters so much in the long run. Shore's framework is the
  explanation for the downstream consequence of Willison's SDLC throughput finding:
  10× code output without proportional maintenance cost reduction means 10× the
  compounding maintenance burden. The two sources are complementary: Willison names
  the capacity disruption, Shore models its economic consequence.

- **Novel**:
  - **The precise mathematical ROI gate for AI coding tools**: No other corpus source
    provides a specific quantitative criterion for evaluating whether AI tool adoption
    is economically beneficial. The "inverse relationship" requirement (N× velocity
    gain must be matched by 1/N× maintenance cost) is a concrete, testable standard
    that teams can apply to their own metrics. Prior corpus coverage discusses
    maintenance and complexity concerns but does not quantify the relationship.
  - **The "permanent indenture" / Hotel California lock-in framing**: No prior corpus
    source identifies the asymmetric exit problem — that stopping AI use removes
    velocity benefits but not accumulated maintenance debt. This changes the risk
    calculus for "experimental" AI adoption: the experiment cannot be cleanly reversed.
  - **Velocity gain → maintenance cost compounding as a mechanism for productivity decay**:
    The Miller et al. paper (`paper-miller-speed-cost-quality.md`) measures the outcome
    (velocity decay, complexity increase); Shore provides the theoretical model that
    explains the mechanism. This combination of empirical finding + explanatory model
    is the most complete account in the corpus of why AI coding productivity gains are
    transient when not paired with maintenance cost controls.
  - **Categorical distinction between velocity-increasing AI tools and maintenance-reducing
    AI tools** (Claim 7): No other corpus source distinguishes these two categories
    explicitly or notes that they have different ROI profiles under Shore's framework.

- **Contradicts**: None filed. Shore's claim that current coding agents increase
  maintenance costs is consistent with the best available empirical evidence
  (`paper-miller-speed-cost-quality.md` Claims 2–4). The `blog-bvp-shopify-ai-playbook.md`
  Claim 6 ("reversion rate tracking shows no quality decline at Shopify") uses a
  different and less sensitive metric than cognitive complexity or static analysis
  warnings; this is not a contradiction but a metric-sensitivity difference, as noted
  in the BVP source note itself.

## Guide Impact

- **Chapter 05 (Team Adoption — ROI Evaluation Framework)**: This source provides the
  most concrete economic criterion in the corpus for evaluating AI adoption ROI. The
  guide currently does not have a quantitative ROI gate. Shore's framework should anchor
  a new section: teams should evaluate whether their maintenance cost metrics (cognitive
  complexity, static analysis warnings, PR review time per line) are improving at a rate
  that offsets their productivity multiplier. Without this measurement, teams cannot
  know whether their AI adoption is net positive. Pair with `paper-miller-speed-cost-quality.md`
  for the empirical evidence that current tools fail this test on average.

- **Chapter 05 (Team Adoption — Measuring Impact with Sufficient Time Horizon)**: Shore's
  model explains WHY the guide recommendation (via `paper-miller-speed-cost-quality.md`)
  to use a ≥6-month measurement window is correct. Short-window measurements capture the
  velocity gain before the maintenance burden accumulates to offset it. The guide should
  now explain the mechanism, not just prescribe the window length: "A 30-day productivity
  measurement is misleading because maintenance costs from AI-generated code accumulate
  over months and years; the true cost only becomes visible at the 6-month horizon."

- **Chapter 05 (Team Adoption — Pilot Design and Exit Strategy)**: The "permanent
  indenture" claim (Claim 4) directly challenges the assumption that AI tool pilots can
  be safely discontinued if they don't work. Teams designing pilots should account for
  the asymmetric exit: velocity benefits disappear on discontinuation, maintenance debt
  does not. This implies that pilot design should include maintenance cost measurement
  as a primary success criterion, not a secondary or optional one.

- **Chapter 02 (Harness Engineering — What to Measure)**: The guide's harness engineering
  chapter should add maintenance cost metrics as first-class harness outputs. The
  harness should track not just "how much code was generated" but "what happened to
  cognitive complexity, static analysis warnings, and PR review time per line." Shore's
  framework provides the rationale: these are the metrics that determine whether the
  AI adoption is economically beneficial, and they cannot be inferred from velocity
  metrics alone.

- **Chapter 01 (Daily Workflows — AI Tool Selection)**: Shore's categorical distinction
  between velocity-increasing and maintenance-reducing AI tools (Claim 7) is actionable
  at the daily-workflow level. The guide should help practitioners evaluate individual
  tools on both dimensions: not just "does this tool help me write code faster?" but
  "does this tool help me reduce the maintenance burden of existing code?" The two
  objectives are distinct and should be evaluated separately.

## Extraction Notes

1. **Source is a two-layer relay**: The issue URL (Willison's link-blog page) contains
   only two quoted paragraphs from Shore's article. The full analytical content required
   following the link to Shore's article as a substantive linked page per MINER.md §1.
   All claims beyond Claims 1 and 4 draw from the Shore article; Claims 1 and 4 are
   reproduced verbatim in the Willison post.

2. **Quote sourcing**: Quotes from the Willison page were confirmed verbatim via direct
   HTTP fetch of the page HTML (both quoted paragraphs, the attribution, and the page
   metadata). Quotes from the Shore article were confirmed verbatim via direct HTTP
   fetch of that page. All quotes in this note are marked with their actual source URL
   to distinguish Willison relay from Shore article.

3. **"Rock Lobster" is a fictional AI agent**: Shore uses this name in his worked
   example to make the scenario hypothetical. The analysis is not about a specific real
   tool; it is a general mathematical example of the consequences of doubled output with
   doubled maintenance costs.

4. **The spreadsheet model**: Shore links to a live spreadsheet for readers to explore
   the model with different assumptions. This spreadsheet was not fetched for this note
   as it is illustrative of the model already described in the text.

5. **Confidence calibration: emerging**: Rated "emerging" rather than "anecdotal"
   because the mathematical framework is internally valid and the directional claims
   about current AI tools are now corroborated by peer-reviewed empirical data
   (`paper-miller-speed-cost-quality.md`). The specific model numbers (10 days / 5 days
   maintenance estimates) are illustrative and should not be treated as empirical
   benchmarks. The qualitative framework and the inverse relationship requirement are
   robust to changes in the specific numbers.

6. **Cross-reference verification**: All cited claim numbers verified by re-reading the
   cited source notes at the line numbers found in this session:
   - `paper-miller-speed-cost-quality.md` Claim 2 (lines 51–55): "Cognitive complexity
     increases by 41.6% post-adoption, persistently" — verified.
   - `paper-miller-speed-cost-quality.md` Claim 3 (lines 57–61): "Static analysis
     warnings...increase by 30.3% post-adoption, persistently" — verified.
   - `paper-miller-speed-cost-quality.md` Claim 4 (lines 63–67): "Velocity gains last
     only ~2 months, then disappear entirely" — verified.
   - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 2 (lines 66–85):
     "Normalization of deviance is a real risk..." — verified.
   - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 7 (lines 162–181):
     "The SDLC was designed for ~200 LOC/day..." — verified.
   - `blog-bvp-shopify-ai-playbook.md` Claim 4 (lines 52–56): "Code review has become
     'a big bottleneck'..." — verified.
   - `blog-bvp-shopify-ai-playbook.md` Claim 6 (lines 64–68): "Shopify tracks reversion
     rate...reports no quality decline" — verified.
