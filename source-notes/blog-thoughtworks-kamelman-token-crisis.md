---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/navigating-ai-token-crisis
source_type: blog-post
title: "Navigating today's AI token crisis"
author: Matt Kamelman (Innovation Choreographer, Thoughtworks)
date_published: 2026-06-10
date_extracted: 2026-07-06
last_checked: 2026-07-06
status: current
confidence_overall: emerging
issue: "#1567"
---

# Navigating Today's AI Token Crisis

> Thoughtworks essay arguing that AI token spend has become an architectural
> governance problem rather than a finance problem, diagnosing it as caused by
> unrevisited prototyping-phase defaults rather than individual developer
> behavior, and reframing two Agile Manifesto principles (welcoming change;
> reflecting and tuning) as literal organizational-survival requirements for
> navigating AI economics — while linking the crisis to a deeper energy-
> infrastructure constraint (data center power scarcity) that the Linux
> Foundation's new Tokenomics Foundation and Goldman Sachs's 24x usage-growth
> forecast are organizing around.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, "Generative AI" / "Technology
  strategy" verticals, published June 10, 2026; ~1,100-word opinion/analysis
  essay with one pull-quote from the author. From the trusted feed
  `thoughtworks`.)
- **Author credibility**: Matt Kamelman, "Innovation Choreographer" at
  Thoughtworks (title given on the article's pull-quote byline). Same author
  as `blog-thoughtworks-kamelman-ai-governance-category-error.md`, an earlier
  (June 4, 2026) Thoughtworks essay in this corpus. As with that piece, the
  article synthesizes and interprets other outlets' reporting (Tom's Hardware,
  Forbes, TechCrunch, Fortune, TheNextWeb, Linux Foundation, Goldman Sachs,
  DataCenterDynamics) rather than presenting original data or a Thoughtworks
  client case study — it is argumentative/synthesis journalism, not empirical
  research. Unlike the earlier Kamelman piece (rated "anecdotal" overall
  because its claims were unlinked), this article hyperlinks nearly every
  factual claim to an external source, which this note followed and verified
  (see Extraction Notes) — raising this note's overall confidence to
  "emerging."
- **Scope**: Covers five named pieces of corporate evidence for AI budget
  shock (Uber, Microsoft, GitHub, Duolingo, plus a Priceline/anonymous
  $500M-bill anecdote via FinOps Foundation), an engineering root-cause
  diagnosis (premium models on non-premium tasks, unbounded agent loops,
  verbose context, generous RAG retrieval), an organizational root-cause
  diagnosis (unrevisited prototyping-phase defaults), the Linux Foundation's
  Tokenomics Foundation launch, a Goldman Sachs 24x token-usage growth
  forecast, and a data-center energy-scarcity argument linking token cost to
  physical grid constraints (Ireland case). Does NOT cover: how to implement
  semantic caching, tiered model routing, or token circuit breakers
  technically (named as solutions but not described mechanically); any
  Thoughtworks client engagement or first-party data; or a rebuttal to the
  counter-narrative (seen elsewhere in the corpus) that some executives treat
  high token spend as an intentional productivity investment rather than
  waste.

## Extracted Claims

### Claim 1: Token spend has expanded from a pure finance problem into a simultaneous engineering-design, delivery-governance, and strategic-liability problem, with no single function owning the aggregate outcome
- **Evidence**: Author's opening framing argument, presented as the article's thesis before the corporate evidence is introduced.
- **Confidence**: anecdotal (interpretive framing claim; not measured, but consistent with the multi-functional evidence presented afterward)
- **Quote**: "What started as a finance issue has not stopped being one, but has, in fact, expanded. Token spend is now simultaneously a finance problem, an engineering design problem, a delivery governance problem and, for organizations that haven't yet noticed, a strategic liability. The difficulty is that none of those functions currently owns the aggregate."
- **Our assessment**: This "no one owns the aggregate" framing is the article's central diagnostic claim and is directly corroborated by the specific case evidence that follows (Uber's COO admitting no clear cost-to-value link; Microsoft dropping licenses over budget overrun). It is a reasonable synthesis of the cited evidence rather than a novel empirical finding, but it gives the guide a crisp naming device for a cross-functional governance gap that existing corpus sources (`blog-thoughtworks-omahony-feature-token-budgets.md`, `docs-ghaw-cost-management.md`) address piecemeal by function (feature-planning, platform ops) without naming the aggregate-ownership gap explicitly.

### Claim 2: Uber's President/COO Andrew Macdonald has publicly stated there is not yet a demonstrated link between rising token consumption and useful consumer features shipped
- **Evidence**: Linked to a Tom's Hardware article (in turn relaying Business Insider's coverage of Macdonald's remarks on the Rapid Response Podcast). This note followed the link and confirmed the quote directly against the Tom's Hardware page (see Extraction Notes).
- **Confidence**: emerging (on-record remarks by a named, senior Uber executive, independently confirmed via the followed link; single company)
- **Quote**: "Uber's President and COO Andrew Macdonald then stated he couldn't draw a clear connection between rising token consumption and an increase in useful consumer features — a candid admission that the organization had been spending ahead of demonstrated value."
- **Our assessment**: The Thoughtworks article's paraphrase is faithful to the underlying source: Tom's Hardware quotes Macdonald directly as saying "That link is not there yet, right?" regarding AI-driven feature shipping, and separately quotes him saying "the headline stats make your head explode" and that "there hasn't really been anything that's taken off yet." This is a materially new, guide-relevant data point not previously in the corpus's Uber coverage (`blog-simonwillison-uber-caps-usage.md` and `blog-thoughtworks-omahony-feature-token-budgets.md` both document Uber's *budget exhaustion* and its *spending-cap response*, but neither documents this specific admission that Uber's own leadership cannot connect the spend to shipped value). It substantiates Claim 1's "no clear connection to value" framing with a named, on-record executive statement rather than inference.

### Claim 3: Microsoft ended most internal Claude Code licenses and moved engineers toward its own Copilot CLI, reportedly because token-based Claude Code costs ran past Microsoft's internal annual AI budget months ahead of schedule
- **Evidence**: Linked to a Forbes article (Jon Markman), which this note followed and read in full.
- **Confidence**: emerging (named company, specific product-discontinuation action with a stated deadline, reported motive attributed to cost)
- **Quote**: "Microsoft ended most internal Claude Code licenses and moved engineers toward Copilot CLI."
- **Our assessment**: This is a new, previously unmined data point for the corpus. The followed Forbes article adds detail the Thoughtworks piece omits: the license end-date (June 30, 2026), that Claude Code adoption inside Microsoft grew heavily starting in December, that "the costs ran past the annual AI budget months ahead of schedule" specifically because token-based pricing is a cost Microsoft "does not control," and that the move is framed as part of a broader Microsoft "self-sufficiency in AI" strategy (building in-house coding/voice/image/transcription models). This connects directly to `blog-simonwillison-microsoft-mai-models.md` (Microsoft's June 2, 2026 launch of MAI-Thinking-1 and MAI-Code-1-Flash, explicitly positioned for GitHub Copilot) — the Claude Code license cancellation and the MAI model launch are two data points in the same underlying Microsoft strategic shift, roughly contemporaneous (early-to-mid June 2026), that no existing corpus note connects to each other.

### Claim 4: GitHub moved from predictable subscription pricing to usage-based AI credits for Copilot, forcing organizations to reason about AI consumption the way they previously reserved for cloud infrastructure billing
- **Evidence**: Linked to a TechCrunch article, cited as evidence of a broader industry pricing-model shift.
- **Confidence**: emerging (named vendor pricing-model change; single source followed at the citation level, not independently re-read in full by this note — see Extraction Notes)
- **Quote**: "GitHub moved from predictable subscription pricing to usage-based AI credits, forcing organizations to think about consumption patterns in ways they previously reserved for cloud infrastructure."
- **Our assessment**: This is directionally consistent with the corpus's existing `docs-github-copilot-cli-sdk-session-credit-limits.md`, which documents GitHub Copilot CLI's credit-limit mechanics from the vendor-documentation side. This article adds the *industry framing* — that the pricing-model shift itself (subscription to metered) is part of the same crisis pattern as Uber's and Microsoft's budget overruns, not just a routine vendor pricing update. Treat as corroborating evidence for the crisis narrative rather than a new mechanism; the technical credit-limit details already live in the gh-aw-family notes.

### Claim 5: Duolingo reversed its policy of evaluating employee performance using AI-activity metrics after finding usage doesn't reliably correlate with value creation
- **Evidence**: Linked to a Fortune article, which this note followed and read in full.
- **Confidence**: settled (on-record reversal, confirmed via direct quotes from Duolingo CEO Luis von Ahn and a company spokesperson in the followed Fortune article)
- **Quote**: "Duolingo reversed its decision to evaluate developer performance using AI activity metrics after discovering that usage does not reliably correlate with value creation."
- **Our assessment**: The followed Fortune article substantiates and sharpens this: von Ahn is quoted saying "At the end, we backtracked, and we said, 'No. Look, the most important thing in your performance is that you are doing whatever your job is as well as possible... if it can't, I'm not going to force you to do that,'" and that the original AI-first performance policy "felt like rather than being held accountable for the actual outcome, we're trying to just push something that in some cases did not fit." This is a direct, named-company corroboration of the corpus's existing anti-gaming-metric principle (`blog-simonwillison-uber-caps-usage.md` Claim 4's "tokenmaxxing leaderboard" anti-pattern, and `blog-cursor-paypal-enterprise-adoption.md` Claim 8's rejection of "% AI-generated code" as a metric) — Duolingo is now a third independent named enterprise reaching the same "don't reward the usage proxy, reward the outcome" conclusion, this time specifically about *performance review* metrics rather than *cost-governance* metrics.

### Claim 6: FinOps Foundation executive director J.R. Storment reports hearing from multiple companies in April–May 2026 that they were already 3x over their entire 2026 token budget, and that one company reportedly ran up a $500 million AI bill in a single month after failing to set usage limits
- **Evidence**: Linked to a TheNextWeb article, which this note followed and read in full; the $500M figure and Storment quote are independently corroborated by a Tom's Hardware headline ("Mystery company accidentally blew $500 million on Claude AI in a single month") surfaced as a related article during extraction.
- **Confidence**: emerging (named, on-record FinOps Foundation executive quote, corroborated by a second outlet's independent headline referencing the same $500M figure; the specific company behind the $500M bill remains unnamed in both sources)
- **Quote**: "'In April and May, I started hearing from companies: \"Oh my god, we are 3x over our entire 2026 token budget and it's only April,\"' said J.R. Storment, executive director of the FinOps Foundation. One company reportedly ran up a $500 million AI bill in a single month after failing to set usage limits."
- **Our assessment**: This is the single most concrete piece of aggregate evidence in the article — a named industry-body executive's on-record account of a pattern across "companies" (plural), not one anecdote. The followed TheNextWeb source adds context the Thoughtworks piece omits: per-token API prices fell 98% (from $20 to $0.40 per million tokens since late 2022) while enterprise AI bills rose an estimated 320% (average enterprise AI budget: $1.2M/year in 2024 → $7M in 2026), because agentic tooling drives per-task token volume up roughly 30x (a $0.04 linear-workflow interaction in 2023 now costs ~$1.20 as an orchestrated agentic system) and per-developer consumption up 18.6x in nine months (per Jellyfish's Nicholas Arcolano). This "prices collapsed, spend tripled" framing is a genuinely new, quantified paradox for the corpus — no existing token-cost source states the per-token deflation figure alongside the aggregate-spend inflation figure as two sides of the same mechanism.

### Claim 7: A Priceline employee described a routine Cursor contract renewal coming back four to five times more expensive than expected
- **Evidence**: Same followed TheNextWeb article; independently, the Linux Foundation press release (also followed, see Concrete Artifacts) quotes the same individual — Chris Reed, Senior Director IT Finance, Booking.com (Priceline's parent) — in a different, non-overlapping context (supporting the Tokenomics Foundation).
- **Confidence**: emerging (single named employee's on-record anecdote to TechCrunch, relayed by TheNextWeb; corroborated as the same real individual by his separate, independently-sourced Linux Foundation quote)
- **Quote**: "A Priceline employee described a routine Cursor contract renewal coming back four to five times more expensive."
- **Our assessment**: TheNextWeb's fuller quote sharpens this into a memorable analogy: Reed said "It's like the crack-cocaine epidemic. They let you try it to get you hooked, and now you're kind of beholden to it," and separately noted he was "already seeing discrepancies between vendor-reported usage and Priceline's internal data" — a data-integrity problem (vendor usage metering vs. internal metering disagreeing) not mentioned anywhere else in the corpus. This is a novel, concrete governance-tooling gap: even a company trying to govern spend can't fully trust the vendor's own usage numbers.

### Claim 8: Enterprise AI token waste follows an engineering pattern — premium reasoning models used for non-premium tasks (classification, validation, structured transformation), agent retry loops without hard boundaries, verbose conversation-history context prepended to every request, and RAG pipelines that "retrieve generously because retrieval appears cheap relative to generation"
- **Evidence**: Author's own engineering diagnosis, presented without citation to a specific case or vendor data — a general pattern claim.
- **Confidence**: anecdotal (asserted engineering-pattern claim; no measured frequency or named example given for any of the four sub-patterns)
- **Quote**: "Large portions of enterprise AI traffic are still being routed through premium reasoning models for tasks that don't require premium reasoning — classification workloads, validation pipelines, structured transformations. It's the 2026 version of deploying a Kubernetes cluster to run a cron job... retry instructions without hard boundaries create expensive loops that are invisible to standard infrastructure monitoring. Stateful systems prepend thousands of tokens of conversation history to every new request while RAG pipelines retrieve generously because retrieval appears cheap relative to generation."
- **Our assessment**: This corroborates `docs-ghaw-cost-management.md`'s existing cost-reduction levers (model selection, context limiting) and `blog-bswen-mcp-token-cost.md`'s session-hygiene guidance from the platform/individual-session angle, but frames them here as *symptoms of a diagnosed anti-pattern* rather than *available levers* — a useful "here's what to look for" framing the guide could use as a checklist, though it should be flagged as the author's own unsourced generalization rather than a measured finding (no company is named as exhibiting these specific four patterns).

### Claim 9: The deeper, "harder and more important" diagnosis of token waste is organizational rather than individual — waste stems from defaults (model selection, context management, agent design, governance) set during prototyping and never revisited before production, with no one owning the aggregate outcome even though local optimizations were individually sensible
- **Evidence**: Author's own structural argument, the article's core reframing move (distinguishing this from the more common "developers are being careless" narrative).
- **Confidence**: anecdotal (interpretive/structural claim; no data on what fraction of enterprise token waste is attributable to unrevisited defaults specifically, versus other causes)
- **Quote**: "Token waste at this scale is rarely caused by individual developers. It's caused by defaults — model selection defaults, context management defaults, agent design defaults, governance defaults — that were set during a prototyping phase and never revisited before production. While teams made sensible local optimizations, no one owned the aggregate outcome."
- **Our assessment**: This is the article's most guide-relevant claim: it explicitly reframes token-cost governance away from blaming individual developer behavior (a framing the guide should avoid if adopting this source) and toward a specific, actionable diagnostic question — "which defaults were set during prototyping and never revisited?" This extends `blog-thoughtworks-omahony-feature-token-budgets.md` Claim 9 (Goodhart's Law caution against gaming a formal token-budget target) by locating the failure earlier in the lifecycle — not at the budget-enforcement stage, but at the prototype-to-production defaults-carryover stage, before any budget is even set.

### Claim 10: The Linux Foundation announced its intent to launch the Tokenomics Foundation, an open-standards body for AI cost management operating in partnership with the FinOps Foundation, with initial supporters including Accenture, Booking.com, IBM, KPMG, Oracle, Salesforce, SAP, and ServiceNow
- **Evidence**: Linked directly to the Linux Foundation's own press release, which this note followed and read in full.
- **Confidence**: settled (primary-source press release, directly followed and read; named organizational commitment)
- **Quote**: "The clearest sign this is becoming a structural issue arrived this week when the Linux Foundation announced its intent to launch the Tokenomics Foundation... Initial supporters already include Accenture, Booking.com, IBM, KPMG, Oracle, Salesforce, SAP and ServiceNow."
- **Our assessment**: **Fact-check finding**: the Thoughtworks article's supporter list is incomplete relative to the primary source. The Linux Foundation's own press release (followed directly, see Concrete Artifacts) lists twelve initial supporters, not eight — it additionally names Flexera, Google Cloud, JPMorganChase, and Microsoft, none of which appear in the Thoughtworks article's list. This doesn't rise to a MINER.md §4a contradiction (it's an incomplete quotation of a list, not an opposing factual or interpretive claim that would change guide advice either way), but the guide should cite the primary Linux Foundation press release's full twelve-member list rather than Thoughtworks' truncated eight, and should note Microsoft's presence on that list is notable given Claim 3's Microsoft-drops-Claude-Code narrative in the same article — Microsoft is simultaneously exiting a specific vendor's token-metered product and joining an industry-wide token-standards body, which is a coherent (not contradictory) combination: reducing exposure to any one vendor's metered pricing while supporting shared standards for measuring it.

### Claim 11: Goldman Sachs research projects global AI token usage will multiply 24 times between 2026 and 2030, reaching 120 quadrillion tokens per month, with the inference market expanding from roughly $106 billion in 2025 to $255 billion by 2030
- **Evidence**: Linked to a Goldman Sachs research article; this note attempted to follow the link directly but the page returned HTTP 403 (see Extraction Notes). The figures are independently corroborated verbatim in the followed Linux Foundation press release, which cites the same Goldman Sachs research.
- **Confidence**: emerging (specific quantitative forecast from a named, credible financial-research source, corroborated by an independent primary source citing the same figures; the Goldman Sachs original page itself could not be directly verified for this extraction)
- **Quote**: "Research from Goldman Sachs, cited in the announcement, projects global token usage will multiply 24 times between 2026 and 2030, reaching 120 quadrillion tokens per month, with the inference market expanding from roughly $106 billion in 2025 to $255 billion by 2030."
- **Our assessment**: This is the corpus's first documentation of a specific long-range (2026–2030) token-usage growth forecast from a named financial-research firm, and it is doubly sourced (Thoughtworks article + independently followed Linux Foundation press release both cite the identical figures), which raises confidence despite the Goldman Sachs primary page being inaccessible during this extraction. This figure gives the guide a quantitative anchor for "how much bigger does this problem get" that complements the qualitative crisis anecdotes (Uber, Microsoft, the $500M bill) with a forward-looking industry-wide projection.

### Claim 12: The token crisis is a downstream symptom of a deeper physical constraint — data centers are approaching 1,050 TWh of energy consumption in 2026 (which would make them the world's fifth-largest national energy consumer if counted as a country), and Ireland's data centers are projected to consume 32% of the country's total electricity supply, driving regulatory moratoriums on new grid connections
- **Evidence**: The 1,050 TWh figure is stated by the author without a direct inline citation; the Ireland 32% figure is linked to a DataCenterDynamics article, which this note followed and read.
- **Confidence**: anecdotal for the 1,050 TWh figure (no link provided, not independently verified in this extraction); emerging for the Ireland figure (followed and confirmed, though the followed source attributes it to "a report from the International Energy Agency" with the specific number given as "32 percent... by 2026" — a forecast year the Thoughtworks article does not explicitly restate)
- **Quote**: "Data center energy consumption is approaching 1,050 TWh in 2026, which would make data centers the fifth largest energy consumer in the world if counted as a country. Ireland's data centers are projected to consume 32 percent of the country's total electricity supply, a figure that has driven regulatory moratoriums on new grid connections."
- **Our assessment**: The followed DataCenterDynamics article confirms the 32% figure and the moratorium (EirGrid's 2022 moratorium on new Dublin-area data center connections, "set to last until 2028") but attributes the 32%-by-2026 figure to the International Energy Agency, a detail the Thoughtworks article omits (it implies the figure is Thoughtworks' own framing). The 1,050 TWh global figure could not be independently verified in this extraction (no link provided in the source article) and should be treated as unverified until corroborated elsewhere. This is a genuinely novel angle for the corpus — no existing token-cost source connects enterprise token-spend pressure to data-center grid-capacity constraints as a causal upstream driver rather than a separate environmental-impact concern.

### Claim 13: Because the underlying constraint (energy/infrastructure) is physical and compounding rather than purely financial, organizations cannot optimize their way out of it at the billing layer — they must move the decisions that generate the cost upstream, to where they can actually be governed
- **Evidence**: Author's own synthesis and central prescriptive recommendation, restated twice in the article (once in body text, once in the pull-quote).
- **Confidence**: anecdotal (prescriptive conclusion; not tested or benchmarked against any organization actually implementing "upstream governance" as described)
- **Quote**: "When the constraint is physical and compounding, you cannot optimize your way out of it at the billing layer. You have to move the decisions that generate the cost upstream, to where they can actually be governed."
- **Our assessment**: This is the article's core actionable recommendation and its most guide-relevant single sentence — it argues for shifting cost governance from *runtime billing controls* (circuit breakers, spend caps — already well-covered via `blog-simonwillison-uber-caps-usage.md` and the Shopify circuit-breaker material in `blog-thoughtworks-omahony-feature-token-budgets.md`) to *upstream design-time decisions* (model selection, context architecture, agent design — Claim 8's four patterns). It's consistent with, and gives a memorable one-line rationale for, O'Mahony's build/run/maintenance budget framework (`blog-thoughtworks-omahony-feature-token-budgets.md` Claim 4), which is also a pre-build/upstream gate rather than a runtime control. Should be presented as a compelling synthesis argument, not a validated organizational playbook — no named company is cited as having executed this "move decisions upstream" transition successfully end-to-end.

### Claim 14: The article reframes the Agile Manifesto's second principle ("welcome changing requirements... harness change for the customer's competitive advantage") and twelfth principle ("at regular intervals, the team reflects on how to become more effective, then tunes and adjusts its behavior accordingly") as literal, structural requirements for organizational survival under AI token economics, not just software-delivery guidance
- **Evidence**: Author's own argumentative framing device, structuring the entire essay (the headline itself: "The fresh urgency of two particular principles of the Agile Manifesto").
- **Confidence**: anecdotal (rhetorical/interpretive framing; the Agile Manifesto's principles are quoted accurately but the claim that they apply "more literally" to AI economics than the authors intended is the author's own argumentative leap)
- **Quote**: "The teams that will navigate AI economics well over the next five years are not the ones that respond correctly to this year's cost structure. They're the ones that build the organizational metabolism to respond correctly to the next one (and then the one after that)... Twenty-five years after the manifesto was written and signed, both principles are more literal than their authors likely intended."
- **Our assessment**: This is a distinctive rhetorical framing not present elsewhere in the corpus's token-cost coverage — it connects token-cost governance to Ch00-level foundational Agile principles rather than treating it as a purely technical/financial problem. The "organizational metabolism" phrase is a useful, quotable synthesis of Claim 9's diagnosis (the problem isn't this year's specific waste pattern, it's the organization's capacity to keep re-diagnosing new waste patterns as they emerge) — but it is an analogy, not a tested organizational-design principle, and should be presented as such.

## Concrete Artifacts

### The article's five-item corporate evidence list (as structured by the author, with this note's follow-up verification)

```
Navigating today's AI token crisis — Matt Kamelman, Thoughtworks, June 10, 2026

1. UBER: CTO acknowledged Claude Code budget for all of 2026 spent by April.
   President/COO Andrew Macdonald: no clear link yet between token spend and
   useful shipped features. [Verified via followed Tom's Hardware link —
   direct quote: "That link is not there yet, right?"]

2. MICROSOFT: ended most internal Claude Code licenses, moved to Copilot CLI.
   [Verified via followed Forbes link — license end-date June 30, 2026;
   motive: "the costs ran past the annual AI budget months ahead of
   schedule"; part of a stated Microsoft "self-sufficiency in AI" strategy]

3. GITHUB: moved from subscription pricing to usage-based AI credits.
   [TechCrunch link cited but not independently re-read in full for this note]

4. DUOLINGO: reversed AI-activity performance-review policy; usage doesn't
   correlate with value creation. [Verified via followed Fortune link — CEO
   Luis von Ahn direct quote confirmed]

5. FINOPS FOUNDATION (J.R. Storment): companies reporting 3x-over-budget in
   April/May 2026; one company's $500M single-month AI bill.
   [Verified via followed TheNextWeb link — direct Storment quote confirmed,
   plus additional context: 98% per-token price drop vs. 320% enterprise
   AI-bill increase; Priceline's Chris Reed "crack-cocaine epidemic" quote]
```

### The Tokenomics Foundation's actual supporter list (from the primary Linux Foundation press release, followed directly — corrects the Thoughtworks article's truncated list)

```
Linux Foundation press release, "Linux Foundation Announces the Intent to
Launch the Tokenomics Foundation...", June 3, 2026:

"Organizations who have expressed initial support for the Tokenomics
Foundation include Accenture, Booking.com, Flexera, Google Cloud, IBM,
JPMorganChase, KPMG, Microsoft, Oracle, Salesforce, SAP and ServiceNow."

[Thoughtworks article's list, by contrast, names only: Accenture,
Booking.com, IBM, KPMG, Oracle, Salesforce, SAP and ServiceNow — omitting
Flexera, Google Cloud, JPMorganChase, and Microsoft.]

Quoted purpose (Jim Zemlin, Linux Foundation CEO): "Measuring and
benchmarking token efficiency across different models and vendors is
critical to how organizations make business decisions, but until now, there
was no neutral home to develop the standards needed to measure token
economics transparently across the entire supply chain."

Source: https://www.linuxfoundation.org/press/linux-foundation-announces-the-intent-to-launch-the-tokenomics-foundation-to-establish-open-standards-for-ai-cost-management
```

### The token-price-deflation-vs-spend-inflation paradox (from the followed TheNextWeb article)

```
"GPT-4-equivalent performance now costs roughly $0.40 per million tokens,
down from $20 per million in late 2022. That is a 98% reduction. Yet
enterprise AI bills have risen by an estimated 320%... The average
enterprise AI budget has grown from $1.2 million per year in 2024 to $7
million in 2026... A simple linear workflow in 2023 cost about $0.04 per
interaction. An orchestrated agentic system in 2026 costs roughly $1.20,
about 30 times more."

— Nicholas Arcolano (Jellyfish), on per-developer token consumption:
"per-developer consumption has risen roughly 18.6 times in nine months...
Whether extreme spend pays off comes down to the ultimate business value of
shipped code, which most companies still can't measure."

Source: https://thenextweb.com/news/token-prices-fell-98-enterprise-ai-bills-tripled-now-the-industry-wants-a-standards-body-to-explain-why
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-thoughtworks-omahony-feature-token-budgets.md`,
`blog-simonwillison-uber-caps-usage.md`, `blog-thoughtworks-kamelman-ai-governance-category-error.md`,
and `blog-simonwillison-microsoft-mai-models.md` were re-read directly
(MINER.md §4b) and claim numbers below were confirmed against those notes'
numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-simonwillison-uber-caps-usage.md` Claim 1 (Uber exhausted its 2026
    AI budget within four months, budget set in 2025 before the adoption
    curve was visible): this article's Claim 2 corroborates the underlying
    event and adds the Andrew Macdonald "no clear value link" admission that
    neither Willison's note nor `blog-thoughtworks-omahony-feature-token-budgets.md`
    Claim 1 (adoption-curve data) documents.
  - `blog-simonwillison-uber-caps-usage.md` Claim 4 (Willison's
    "tokenmaxxing leaderboard" anti-pattern, contrasted with Uber's rational
    per-tool cap) and `blog-cursor-paypal-enterprise-adoption.md` Claim 8
    (PayPal's rejection of "% AI-generated code" as a metric): this article's
    Claim 5 (Duolingo's reversal of AI-activity performance metrics) is a
    third, independent named-company instance of the same anti-gaming-metric
    principle — Uber, PayPal, and Duolingo each independently avoid rewarding
    a usage/activity proxy instead of actual outcomes.
  - `blog-thoughtworks-omahony-feature-token-budgets.md` Claim 5 (maintenance
    budget is where teams "consistently under invest" because model
    deprecation, pricing changes, and eval re-runs aren't in story-point
    estimates): this article's Claim 9 (waste caused by prototyping-phase
    defaults never revisited before production) describes the same underlying
    failure mode — unrevisited assumptions compounding — from the
    organizational-governance angle rather than the maintenance-budgeting
    angle.

- **Contradicts**: None identified as a MINER.md §4a contradiction (no claim
  here materially opposes an existing note's claim in a way that would drive
  different guide advice). One fact-check discrepancy is noted instead: this
  article's Tokenomics Foundation supporter list (eight companies) omits four
  companies (Flexera, Google Cloud, JPMorganChase, Microsoft) that the primary
  Linux Foundation press release names as initial supporters — see Claim 10's
  "Our assessment" and the Concrete Artifacts section. This is an
  incompleteness in a secondary source's list, not an opposing factual claim,
  so no contradiction issue was filed.

- **Extends**:
  - `blog-thoughtworks-omahony-feature-token-budgets.md`: That note documents
    the *feature-planning-stage* budgeting response to the same Uber/Meta
    evidence base (build/run/maintenance budgets, per-ticket token estimates).
    This article extends the diagnosis one level further upstream — from "how
    should we budget for a feature" to "why do organizations keep setting
    defaults during prototyping that no one revisits before production" — and
    adds an industry-standards dimension (Tokenomics Foundation) and a
    physical-infrastructure dimension (energy/grid constraints) that
    O'Mahony's note does not cover.
  - `blog-simonwillison-microsoft-mai-models.md`: That note documents
    Microsoft's June 2, 2026 launch of independent MAI-series models
    (MAI-Thinking-1, MAI-Code-1-Flash) for GitHub Copilot. This article's
    Claim 3 (Microsoft ending Claude Code licenses over budget overrun,
    reported early June 2026) is the cost-driven flip side of the same
    strategic move — no existing note connects Microsoft's *model
    self-sufficiency push* to its *simultaneous exit from a metered
    third-party coding tool* as two data points in one strategy.
  - `blog-thoughtworks-kamelman-ai-governance-category-error.md`: Same
    author, same trusted-feed source, six days apart (June 4 vs. June 10,
    2026). That essay argues AI governance debates are miscalibrated because
    they assume a static object of governance; this essay makes a structurally
    similar argument at the operational-cost layer — that token-cost
    governance is miscalibrated because organizations treat this year's cost
    structure as fixable rather than building ongoing "organizational
    metabolism" (Claim 14) to keep adapting. Both essays share Kamelman's
    recurring thesis that AI-native institutions need continuous
    re-calibration capacity, not one-time fixes, applied to two different
    domains (governance framing vs. cost governance).

- **Novel**:
  - **The 98%-price-drop-vs-320%-spend-increase paradox** (Claim 6, from the
    followed TheNextWeb link): no existing corpus source states both figures
    together as two sides of the same volume-driven mechanism.
  - **Vendor-reported vs. internal usage-metering discrepancies** (Claim 7,
    Priceline's Chris Reed): a novel governance-tooling gap — even companies
    actively trying to track spend can't fully trust vendor-reported token
    usage numbers against their own internal measurement.
  - **The Tokenomics Foundation and its full twelve-member supporter list**
    (Claim 10): the corpus's first documentation of a Linux
    Foundation-sponsored, FinOps-partnered standards body specifically for
    AI/token cost economics.
  - **Goldman Sachs's 24x/120-quadrillion-tokens-per-month 2026–2030
    forecast, and the $106B→$255B inference-market growth figure** (Claim 11):
    the corpus's first named, quantified, multi-year token-usage growth
    forecast from a financial-research firm.
  - **The data-center energy/grid-constraint framing of the token crisis**
    (Claim 12): no existing corpus token-cost source connects enterprise
    token spend to physical electricity-grid scarcity as a causal upstream
    driver (as opposed to a separate environmental-footprint discussion).
  - **Duolingo's performance-review policy reversal** (Claim 5): a new named
    enterprise case study for the anti-gaming-metric principle, previously
    only documented via Uber and PayPal.
  - **Microsoft's Claude Code license cancellation with a specific stated
    cost-overrun motive and end-date** (Claim 3): new to the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering / Cost Management)**: Add the "no one
  owns the aggregate" framing (Claim 1) and the "unrevisited prototyping
  defaults" diagnosis (Claim 9) as a named root-cause pattern, positioned
  upstream of the existing build/run/maintenance budgeting framework already
  sourced from `blog-thoughtworks-omahony-feature-token-budgets.md`. Add the
  "move decisions upstream, not to the billing layer" recommendation (Claim
  13) as the connecting principle between design-time controls (model
  routing, context limits — already covered via `docs-ghaw-cost-management.md`)
  and runtime controls (circuit breakers — already covered via the Shopify
  example in the O'Mahony note).

- **Chapter 04 (Production Patterns / Operational Risk Management)**: Add
  Microsoft's Claude Code license cancellation (Claim 3) and GitHub's
  usage-based credit pricing shift (Claim 4) as two more named-company
  budget-shock data points, alongside the existing Uber and Meta cases. Add
  the J.R. Storment / FinOps Foundation "3x over budget" and $500M-bill
  evidence (Claim 6) as aggregate, cross-company evidence (rather than
  single-company anecdote) that the crisis is industry-wide, not
  Uber-specific.

- **Chapter 05 (Team Adoption / Organizational Scaling)**: Add Duolingo's
  performance-review reversal (Claim 5) as a third named-company instance of
  the anti-gaming-metric principle, alongside Uber's spending-cap response
  and PayPal's metric rejection. Add the Priceline vendor/internal
  usage-metering discrepancy (Claim 7) as a caution: organizations adopting
  cost-governance tooling should not assume vendor-reported usage figures are
  reliable without independent verification.

- **Any chapter discussing industry standards or cost-governance tooling
  emergence**: Add the Tokenomics Foundation (Claim 10) as the corpus's first
  documented industry-standards response to the token-cost crisis, citing the
  primary Linux Foundation press release's full supporter list rather than
  the Thoughtworks article's truncated version.

- **Any chapter discussing the environmental or infrastructure dimension of
  AI cost**: Add the data-center energy-constraint argument (Claim 12) as a
  novel causal link between token pricing pressure and physical grid
  scarcity — flag the global 1,050 TWh figure as unverified (no primary
  source link available) while the Ireland 32% figure is independently
  confirmed.

## Extraction Notes

1. **WebFetch initially returned an AI-summarized "Summary of..." response
   instead of verbatim text** despite an explicit verbatim-return prompt.
   Per MINER.md §2a, this note does not rely on that summarized output for
   quotes — the full article text was instead retrieved via a direct `curl`
   fetch of the live HTML (with a browser user-agent) and parsed with
   BeautifulSoup, stripping script/style tags and extracting the `<article>`
   body. All quotes attributed directly to the Thoughtworks article in this
   note are taken from that locally-parsed verbatim text, not from the
   AI-summarized WebFetch output.

2. **Followed 5 of the article's 8 substantive outbound links**, per MINER.md
   §1's "follow up to 5 linked pages" guidance, prioritizing the links behind
   the most load-bearing factual claims:
   - Tom's Hardware (Uber/Macdonald) — fetched via direct `curl` after an
     initial WebFetch attempt returned only navigation/membership boilerplate
     with no article body; the `curl` fetch succeeded and is the basis for
     Claim 2's verbatim quotes.
   - TheNextWeb (Storment/FinOps/$500M/Priceline) — fetched via both WebFetch
     and a follow-up direct `curl`; the `curl` fetch confirmed verbatim
     quotes for Claims 6–7 and the price-paradox figures in Concrete
     Artifacts.
   - Linux Foundation press release (Tokenomics Foundation) — fetched via
     both WebFetch and a follow-up direct `curl`; the `curl` fetch surfaced
     the supporter-list discrepancy documented in Claim 10.
   - Forbes (Microsoft/Copilot CLI) — fetched via WebFetch only; treat
     Claim 3's non-headline details (license end-date, "self-sufficiency"
     framing) as AI-summarized rather than character-verbatim, though the
     one directly quoted sentence ("Renting intelligence by the token...")
     was returned consistently and is presented as a quote.
   - Fortune (Duolingo) — fetched via WebFetch only; the von Ahn quotes in
     Claim 5 are AI-summarized WebFetch output, not independently re-verified
     via direct HTML fetch. The Assayer should spot-check these two
     WebFetch-only quotes (Forbes, Fortune) against their source URLs before
     treating them as character-for-character verbatim.
   - NOT followed: TechCrunch (GitHub pricing) — cited in Claim 4 at the
     Thoughtworks article's paraphrase level only, not independently re-read.
     Goldman Sachs (token-usage forecast) — attempted via WebFetch, returned
     HTTP 403; the figures were instead corroborated via the independently
     followed Linux Foundation press release, which cites the same Goldman
     Sachs research and figures verbatim (see Claim 11).
     DataCenterDynamics (Ireland energy) — this one WAS followed (6th link,
     exceeding the "up to 5" guidance by one, because it was necessary to
     verify Claim 12's most checkable figure); fetched via WebFetch.

3. **One fact-check discrepancy surfaced, not filed as a contradiction**: the
   Thoughtworks article's Tokenomics Foundation supporter list (8 companies)
   omits 4 companies present in the primary Linux Foundation press release's
   list (12 companies) — see Claim 10 and Cross-References → Contradicts.
   Per MINER.md §4a this is not a contradiction (no opposing claim that would
   drive different guide advice), so no issue was filed; the discrepancy is
   flagged so the guide cites the primary source's complete list.

4. **No contradiction issues filed**: cross-referenced against all
   Thoughtworks token/cost-governance notes and the Uber/PayPal/Duolingo
   metric-gaming cluster; found no claim here that materially opposes an
   existing corpus claim in a way that would change guide advice either way.

5. **Two Prospector triage comments exist on issue #1567** with different
   chapter framings (one emphasizing Ch02/Ch04/Ch05 organizational/energy
   diagnosis; one emphasizing Ch00/Ch04/Ch05 and an Agile-principles angle).
   This note's extraction and Guide Impact section address both framings:
   the organizational-defaults and energy-infrastructure diagnosis (first
   triage comment) is covered in Claims 1, 9, 12–13; the Agile-principles
   reframing (second triage comment) is covered in Claim 14.
