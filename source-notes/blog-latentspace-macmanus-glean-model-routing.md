---
source_url: https://www.latent.space/p/glean-model-routing
source_type: blog-post
title: "Frontier Model Cost and Open-Weights Popularity is Driving Demand for Model Routing"
author: Richard MacManus (Latent Space), interviewing Arvind Jain (Glean co-founder/CEO)
date_published: 2026-08-18
date_extracted: 2026-09-03
last_checked: 2026-09-03
status: current
confidence_overall: anecdotal
issue: "#3199"
---

# Frontier Model Cost and Open-Weights Popularity is Driving Demand for Model Routing

> A narrative Latent Space interview with Glean CEO Arvind Jain describing
> Glean's three-level model-routing architecture, a pre-routing filtering
> layer ("Waldo"), and a shadow-testing-plus-AI-judge continuous-evaluation
> loop — all framed as responses to frontier-model cost spikes (10-20x
> per-user YoY, per Jain) and a sudden enterprise pivot toward open-weight
> models in the three months before publication. Nearly every quantitative
> claim is single-source, self-reported by Glean executives, and undisclosed
> in methodology.

## Source Context

- **Type**: blog-post (Latent Space, narrative article built around an
  interview; not a Q&A transcript — the author paraphrases throughout and
  weaves in direct quotes from Arvind Jain, one direct quote from co-founder
  Tony Gentilcore, and a secondhand reference to a 2023 interview with
  founding engineer Deedy Das)
- **Author credibility**: Richard MacManus, writing for Latent Space (Shawn
  "swyx" Wang's publication), already established in this corpus as a
  `trusted-feed` source per the repo's scanning configuration — the feed
  itself is pre-screened for "is this author worth listening to," not for
  whether individual claims within an article are independently verified.
  The interview subject, Arvind Jain, is Glean's co-founder/CEO and an
  ex-Google Distinguished Engineer with a direct commercial incentive to
  present Glean's routing architecture and cost-effectiveness favorably —
  this is a vendor executive being profiled, not an independent audit.
  Nearly every number in the piece (cost multipliers, Waldo's latency/token
  savings, the $0.45-vs-$1.84 cost-per-task figure, adoption percentages) is
  self-reported by Glean with no disclosed methodology, sample size, or
  measurement window.
- **Scope**: Covers Glean's three-level model-selection architecture
  (manual/admin/automatic), the cost pressures driving customers toward
  automatic routing, the Waldo pre-filtering layer, Glean's shadow-testing
  and AI-judge evaluation loop for its router, the recent (Jain says
  "last three months") enterprise shift toward open-weight models, and
  Glean's own company narrative (founded 2019 for enterprise search, now
  "$300M ARR," valued at "$7.2B"). Does NOT cover: Waldo's or the router's
  underlying model architecture or training method; any per-customer case
  study beyond the two adoption-percentage mentions (Zillow, Booking.com);
  the AA-Omniscience-style benchmark methodology behind any of Glean's
  numbers; or any comparison of Glean's routing accuracy against a named
  competitor's routing accuracy (only cost, not correctness, is compared to
  Claude Cowork).

## Extracted Claims

### Claim 1: The article frames model routing as having "become a key part of AI deployment" across the industry, citing Stripe's ~$7B acquisition of OpenRouter as evidence of the trend at the infrastructure-market level, before turning to enterprise-specific reporting on Glean
- **Evidence**: Author's own opening framing, referencing a deal already
  independently documented elsewhere in this corpus.
- **Confidence**: anecdotal (editorial framing by the article's author; the
  underlying OpenRouter deal facts are corroborated at "emerging" confidence
  by a dedicated corpus source — see Cross-References)
- **Quote**: "With the intense competition among frontier model companies, together with ever-increasing power of open-weight models like Kimi K3 and Qwen3.8-Max, model routing has become a key part of AI deployment. We've just seen Stripe buy OpenRouter for over $7B, but the trend is equally hot in enterprises."
- **Our assessment**: A reasonable framing device, not independent evidence
  on its own — but it correctly signals that this article should be read as
  one enterprise-scale data point within a broader routing-market trend
  already documented in this corpus (`blog-latentspace-ainews-stripe-buys-openrouter.md`),
  not as an isolated anecdote.

### Claim 2: Glean offers three levels of model selection — employees can explicitly choose a model, administrators can restrict models or impose usage limits, and Glean's automatic mode selects a model dynamically per task
- **Evidence**: Direct paraphrase of Glean's product architecture, attributed
  to the reporting rather than a Jain quote for this specific sentence.
- **Confidence**: settled (a factual description of a shipped product's
  configuration surface, not a performance or effectiveness claim)
- **Quote**: "Employees can explicitly choose a model. Administrators can restrict models or impose usage limits. Glean's automatic mode selects a model dynamically for each task."
- **Our assessment**: This is architecturally identical in shape to the
  admin-governance layers already documented for other vendors in this
  corpus — see Cross-References — confirming that manual/admin/automatic
  tiering is converging into a standard product pattern for enterprise model
  routing, not a Glean-specific innovation.

### Claim 3: Glean's customers mostly choose automatic routing mode for economic reasons, not quality reasons, according to Jain
- **Evidence**: Direct Jain quote, unquantified (no percentage of customers
  choosing each mode is given).
- **Confidence**: anecdotal (single-executive assertion, no supporting usage
  data)
- **Quote**: "Why are people talking about model routing? Why are they excited about it? It's mostly because of cost,"
- **Our assessment**: Plausible and consistent with the cost-driven framing
  of the rest of the article, but it is Jain's own characterization of his
  customers' motivations with no independent usage breakdown to check it
  against.

### Claim 4: Frontier model per-token prices have risen 2-4x on recent flagship releases, and combined with longer task runs this compounds into roughly 10-20x higher per-user AI spend year-over-year, according to Jain
- **Evidence**: Direct Jain quote combining a per-token pricing observation
  with a usage-growth observation into a compounded spend estimate.
- **Confidence**: anecdotal (a single executive's rounded, unsourced
  estimate — no vendor pricing table, no customer billing data, no time
  window more specific than "last year")
- **Quote**: "On a per token basis, they're more expensive — sometimes double or quadruple the rates of the previous models... So you're spending, like, 10 times, 20 times, more, on a per user basis, than what you were doing last year."
- **Our assessment**: The direction (costs rising) is broadly consistent
  with other cost-pressure narratives elsewhere in this corpus, but the
  specific 10-20x figure is a loose verbal estimate ("like, 10 times, 20
  times") rather than a measured figure, and should be cited as such — not
  as a benchmarked cost-growth statistic.

### Claim 5: Glean co-founder and engineering lead Tony Gentilcore claimed Glean is "4x more cost-effective" than a named competitor, averaging $0.45 per task versus $1.84, attributing the gap to Glean's "harness and routing capabilities"
- **Evidence**: The article relays a claim originally made by a different
  Glean executive (not Jain, and not made in this interview) — the article's
  own phrasing ("recently claimed") indicates this is a secondhand citation
  of a separate public statement, likely social media, not verified firsthand
  by MacManus.
- **Confidence**: anecdotal (a vendor's own head-to-head cost claim, relayed
  third-hand by the article, with no task definition, sample size, or
  measurement methodology disclosed)
- **Quote**: "Glean 'is 4x more cost-effective' than Claude Code, 'averaging $0.45 per task versus $1.84 for Claude Cowork.'"
- **Our assessment**: This is the single most guide-citable number in the
  article, but it is also the weakest-sourced: the article itself names two
  different products ("Claude Code" in one clause, "Claude Cowork" in the
  next) as if interchangeable within the same sentence, which this
  extraction cannot resolve without reading the original Gentilcore
  statement (not linked in the article). Treat the $0.45/$1.84 figures as
  an unverified vendor marketing claim, not a benchmarked comparison, until
  a primary source names a specific task set and methodology.

### Claim 6: Glean's "Waldo" agentic search model sits ahead of frontier-model routing, deciding how to decompose a query, which tools to use, and when enough evidence has been gathered to hand off to a frontier model — and is claimed to reduce latency by 50% and token usage by 25%
- **Evidence**: A named product ("Waldo," introduced in April per the
  article) described partly via a Jain quote and partly via a quote from an
  unnamed "technical blog post," plus a headline metric claim attributed to
  Glean.
- **Confidence**: anecdotal (vendor-claimed percentages with no baseline
  definition, no benchmark task set, and no independent measurement)
- **Quote**: "Glean claims that Waldo, its agentic search model, 'reduces latency by 50% and tokens by 25%, reserving advanced models for work that needs them.'" The filtering role: "decides how to break down the question, which tools to use, what to read next, and when it has enough evidence to hand off to a frontier model for a high-quality answer."
- **Our assessment**: This is architecturally novel for the corpus — a named
  pre-routing context-assembly/filtering stage, distinct from the routing
  decision itself (see Cross-References → Novel). The 50%/25% figures should
  be treated the same way as the $0.45/$1.84 figure in Claim 5: a specific,
  citable, but entirely vendor-self-reported number with no disclosed
  baseline or measurement method.

### Claim 7: Enterprise-scale deployment (Zillow reports 80% adoption across 7,000 employees; Booking.com adopted Glean company-wide as its first AI platform) gives Glean visibility into which model users manually switch to when dissatisfied with the router's first choice, which Jain frames as a feedback signal for improving routing
- **Evidence**: Two named-customer adoption statistics plus a Jain quote
  describing what Glean observes across its user base.
- **Confidence**: anecdotal (self-reported adoption percentages with no
  independent verification; the "feedback loop" mechanism itself is
  described only qualitatively, with no data on how often users switch
  models or how that switching data is actually incorporated into routing
  decisions)
- **Quote**: "Zillow reports 80% adoption across 7,000 employees, while at Booking.com, 'Glean became the first AI platform adopted company-wide.'" On the feedback mechanism: "We are getting to see when they're on different types of tasks with AI, what models do they select first, and when they are not satisfied, when they actually upgrade to some other model [that] actually gives them the right results."
- **Our assessment**: The underlying mechanism described here — treating a
  user's manual model override as an implicit dissatisfaction/feedback
  signal — is directionally similar to Cursor Router's "user satisfaction"
  proxy (see Cross-References), but Glean's version is described only in
  the abstract, with no named metric, no reported accuracy, and no
  disclosure of how large a role this signal plays relative to other
  training inputs.

### Claim 8: Glean evaluates its router by running "internal testing systems" that complete the same task in parallel with alternative (cheaper and pricier) models, then scores the router's choice using "AI-based judges," applied continuously to "a small fraction" of real-world traffic
- **Evidence**: Direct Jain description of an internal shadow-testing and
  automated-judging methodology, in response to a direct question about
  evals.
- **Confidence**: emerging (a specific, named mechanism — parallel shadow
  execution plus LLM-judge scoring — described with enough structural detail
  to be a checkable methodology, though no accuracy figures, judge-agreement
  rates, or sample sizes are disclosed)
- **Quote**: "There's this continuous learning that gets updated with new real-world traffic, where basically what is happening is that you let the model router do the work for the user, but behind the scenes you run the same task," alongside "AI-based judges" used to determine "how spot-on the model router was."
- **Our assessment**: This is the article's most concrete, structurally
  specific claim — shadow-testing a router's choice against alternative
  models and scoring the outcome with an LLM judge is a describable,
  reproducible pattern, unlike the article's percentage claims. It directly
  answers the kind of "how do you validate routing decisions" question the
  Prospector's triage comment raised, and it operationalizes, at Glean's
  production scale, the exact prescription `blog-thoughtworks-omahony-fugu-model-routing-critique.md`
  Claim 5 makes in the abstract (see Cross-References).

### Claim 9: Enterprise interest in open-weight models shifted sharply in roughly the three months before publication (i.e., since around May 2026), driven by cost pressure, after a prior "stigma" around models developed outside the US had suppressed adoption
- **Evidence**: Direct Jain quotes contrasting "last year" (minuscule usage)
  against "the last three months" (open source now "a key part of their AI
  strategy" for "most enterprises").
- **Confidence**: anecdotal (a single executive's characterization of a
  market-wide shift, with no adoption-rate data, customer count, or
  usage-share figures given for either period)
- **Quote**: "Last year, the usage [of open source LLMs] was minuscule and nobody was really seriously considering open source... So in the last three months, because AI got so expensive, businesses have started to find it untenable to maintain these AI investments. Given that open source is an order of magnitude cheaper to do tasks, it has created a lot of interest. Today, I can say that in most enterprises, they are considering open source models to be a key part of their AI strategy."
- **Our assessment**: Directionally consistent with the article's own
  opening reference to Kimi K3 and Qwen3.8-Max as competitive open-weight
  models, but "most enterprises" and "a lot of interest" are unquantified.
  Useful as a dated (as of Aug 2026) practitioner-adjacent signal of
  sentiment shift, not as adoption-rate evidence.

### Claim 10: Enterprises are no longer willing to depend on a single model provider or two, and see open-source models as necessary for provider-independence — not just for cost
- **Evidence**: Direct Jain quote.
- **Confidence**: anecdotal (rhetorical generalization, no named companies
  or count of "how many" enterprises hold this view)
- **Quote**: "Nobody is willing anymore to rely on only one model provider, or two, and nobody thinks that they can survive without open source,"
- **Our assessment**: This reframes multi-model routing as a resilience/
  dependency-risk strategy, not purely a cost-optimization one — a distinct
  angle from the cost-only framing that dominates the rest of the article
  (Claims 3, 4, 6), worth preserving as a separate motivation in any guide
  synthesis of "why route between models."

### Claim 11: Part of Glean's stated mission is avoiding LLM calls entirely for tasks that do not need one — Jain gives arithmetic queries handled with a calculator instead of an LLM as an example
- **Evidence**: Direct Jain quote given early in the interview, framing
  "no model" as itself a routing outcome.
- **Confidence**: anecdotal (a single illustrative example, not a
  quantification of how often this "no-LLM" path is actually taken)
- **Quote**: "A big goal of Glean is to avoid using LLMs for tasks where we don't need them," ... "Sometimes you'll see queries in Glean where people are adding two numbers or multiplying two numbers. They could have used a calculator to do that."
- **Our assessment**: A useful, concrete framing for a guide discussion of
  model routing: the cheapest and fastest "model" for a task can be no model
  at all, routed to a deterministic tool instead. No other claim in this
  article, or in the routing-focused notes cross-referenced below, states
  this as explicitly as a named design goal.

### Claim 12: Glean frames its own history — founded in 2019 for enterprise search, now describing itself as an "end-to-end AI platform" that is "used very heavily" by enterprise customers — as the source of the usage data it says it needs to route models effectively
- **Evidence**: Author's narrative framing plus a closing Jain quote tying
  Glean's scale of usage directly to its routing capability.
- **Confidence**: anecdotal (a self-serving competitive-moat narrative,
  asserted without any metric connecting "amount of usage data" to
  "routing accuracy")
- **Quote**: Jain calls Glean an "end-to-end AI platform" that is "used very heavily" by its enterprise customers, which he says allows Glean to "have that data that is required to do effective model routing."
- **Our assessment**: This is a data-moat argument common to vendor
  narratives generally — more usage produces better routing, which produces
  more usage — presented with no supporting measurement of routing accuracy
  over time. Worth flagging as an unverified claim of competitive advantage
  rather than a demonstrated one.

## Concrete Artifacts

### Company and product figures (as stated in the article, unverified by this Miner)
```
Source: latent.space/p/glean-model-routing, Aug 18, 2026

Company:
  Founded: 2019 (enterprise search)
  Valuation: $7.2B (after $150M Series F, "last June")
  ARR: $300M (a "three-fold increase over 15 months")

Cost-effectiveness claim (Tony Gentilcore, co-founder/eng lead, relayed
third-hand — not independently verified, and the article names two
different comparison products, "Claude Code" and "Claude Cowork," within
the same sentence):
  Glean: $0.45 per task
  Comparison product: $1.84 per task
  Stated multiplier: "4x more cost-effective"

Waldo (Glean's "agentic search model," introduced April 2026):
  Claimed latency reduction: 50%
  Claimed token reduction: 25%

Customer adoption (self-reported):
  Zillow: 80% adoption across 7,000 employees
  Booking.com: "first AI platform adopted company-wide"

Cost trend (Jain's estimate, unsourced beyond his own statement):
  Per-token pricing: "double or quadruple" prior-model rates
  Compounded per-user annual spend growth: "10 times, 20 times" YoY

Model-selection architecture: three tiers
  1. Employee-selected (manual)
  2. Admin-restricted / usage-limited
  3. Automatic (dynamic per-task selection)

Evals mechanism: shadow-test a task against alternative (cheaper/pricier)
models in parallel with the router's live choice; score with "AI-based
judges"; applied continuously to "a small fraction" of real-world traffic.
```

## Cross-References

### Cross-reference verification notes
`blog-thoughtworks-omahony-fugu-model-routing-critique.md`,
`blog-cursor-router-model-classifier.md`, `blog-google-api-gateway-model-routing.md`,
and `blog-latentspace-ainews-stripe-buys-openrouter.md` were each read in full
before drafting this section; `blog-thebatch-gpt55-hallucination-kimi-k26.md`'s
claim was verified against its `### Claim 4:` heading text (the corpus
convention states the full one-sentence claim in the heading itself). All
claim numbers below were confirmed against each note's numbered
`### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-thoughtworks-omahony-fugu-model-routing-critique.md` Claim 5
    ("the only claim that would mean anything is 'routing significantly
    improves performance on tasks like yours,' and nobody can make that
    claim except you, with your evals, on your tasks"): this note's Claim 8
    (Glean's shadow-testing + AI-judge evaluation loop, run continuously
    against live production traffic) is a concrete, production-scale
    instance of exactly the practice that article argues is the only way to
    validate a routing product's claims — one Thoughtworks author's
    prescriptive argument, corroborated here by a routing vendor actually
    building that evaluation infrastructure.
  - `blog-cursor-router-model-classifier.md` Claim 6 (Cursor chose online
    A/B testing over offline evals because offline evals are small, distant
    from real usage, and hard to reduce to a rubric) and Claim 7 (Cursor's
    "user satisfaction" behavioral-proxy metric, inferred from whether users
    move on or correct the agent): this note's Claim 7 (Glean observing
    when users manually switch away from the router's first model choice as
    an implicit dissatisfaction signal) and Claim 8 (continuous shadow-
    testing against live traffic rather than static offline evals)
    independently corroborate, from a second named vendor, that production
    routing systems in this corpus are converging on live-traffic behavioral
    signals over offline benchmark evals as the trusted measurement source.
  - `blog-latentspace-ainews-stripe-buys-openrouter.md` Claims 1-3 (Stripe's
    reported ~$7B acquisition of OpenRouter, ~70% gross margin, 250T
    tokens/month): this note's Claim 1 references the same acquisition as
    framing context; that note's fuller financial detail (deal multiple,
    margin, token volume, developer count) is the more rigorous, dedicated
    corpus source for that specific claim, and should be cited in preference
    to this note's brief mention if the guide needs those figures.

- **Contradicts**: None identified. No existing source note stakes out a
  claim about Glean, Waldo, or this specific evaluation methodology that
  this article's claims materially oppose. One point of scope difference
  worth flagging without filing a contradiction (per MINER.md §4a): this
  note's Claim 7 describes Glean as having fine-grained visibility into
  which model a user manually switches to per task, while
  `blog-google-api-gateway-model-routing.md` Claim 6 documents a different
  vendor's routing product (Google Cloud API Gateway) as currently *unable*
  to attribute usage to a specific target model during Public Preview. These
  are different products at different maturity levels, not opposing claims
  about the same fact — Glean's is a mature, in-house application-layer
  router with full visibility into its own routing decisions by
  construction, while Google's is a stateless infrastructure-layer gateway
  with a disclosed observability gap. Not filed as a contradiction.

- **Extends**:
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 4 ("architecting
    software stacks to swap models as easily as bumping a dependency
    version, given four flagship model launches in approximately three
    months"): this note's Claim 2 (Glean's three-tier manual/admin/automatic
    model-selection architecture) and Claim 8 (continuously shadow-testing
    the live router against alternative models) are a concrete, enterprise-
    scale implementation of that editorial's abstract recommendation — an
    architecture explicitly designed so both the routing decision and the
    pool of candidate models can change without redesigning the system.
  - `blog-cursor-router-model-classifier.md`: extends the corpus's coverage
    of production model-routing evaluation from a single-vendor (Cursor)
    online-A/B-test methodology to a second, structurally different
    methodology (Glean's shadow-execution-plus-LLM-judge approach) —
    together the two notes give the corpus two independently-arrived-at,
    non-offline-eval approaches to validating routing decisions in
    production.

- **Novel**:
  - **Waldo as a named pre-routing context-assembly/filtering layer**
    (Claim 6): no other source in this corpus documents a distinct
    architectural stage, positioned before the model-routing decision
    itself, whose job is decomposing the query and assembling "raw
    materials" without spending LLM tokens — corroborating and extending the
    corpus's existing routing-mechanism coverage (Cursor Router, Fugu,
    Google API Gateway) with a stage those sources do not describe.
  - **Shadow-execution-plus-AI-judge continuous evaluation** (Claim 8): a
    specific evaluation architecture — running the router's live choice
    against alternative models on the same task in parallel, then scoring
    with an LLM judge — distinct from Cursor Router's online-A/B-test
    methodology and not previously documented in this corpus's routing
    coverage.
  - **"No model" as an explicit routing outcome** (Claim 11): the most
    direct statement in this corpus's routing coverage that avoiding an LLM
    call entirely (routing to a deterministic tool instead) is itself a
    named design goal, not merely an implicit possibility.
  - **Multi-provider dependency-risk framing distinct from cost framing**
    (Claim 10): while cost-driven multi-model routing is well-covered
    elsewhere in this corpus, framing open-weight/multi-provider adoption
    explicitly as insurance against single-provider dependency (rather than
    pure cost optimization) is a distinct angle this note adds.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claim 6 (Waldo as a named
  pre-routing filtering/context-assembly stage) as a concrete example of
  separating "figure out what's needed" from "pick which model handles it"
  as two distinct architectural stages, rather than a single routing
  decision — worth citing alongside the existing Cursor Router and Fugu
  coverage as a third named production pattern. Add Claim 11 ("no model" as
  a routing outcome, illustrated by routing arithmetic to a calculator
  instead of an LLM) as a specific, quotable example for any section on
  routing granularity.

- **Chapter 03 (Verification)**: Add Claim 8 (shadow-test the router's live
  choice against alternative models in parallel, score with an LLM judge,
  applied continuously to a sample of real traffic) as a second named,
  production-scale pattern for validating routing decisions without relying
  on static offline evals — directly answering
  `blog-thoughtworks-omahony-fugu-model-routing-critique.md` Claim 5's
  challenge ("nobody can make that claim except you, with your evals, on
  your tasks") with a concrete example of a team building exactly that
  evaluation capability in-house.

- **Chapter 04 (Model Selection & Cost)**: Add Claim 4 (Jain's rounded
  10-20x YoY per-user cost estimate) and Claim 9 (a stated three-month-old
  shift toward open-weight adoption for cost reasons) as additional,
  clearly-labeled-as-anecdotal data points in the corpus's existing
  cost-pressure narrative. Do NOT cite Claim 5's $0.45-vs-$1.84 cost-per-task
  figure as a benchmarked comparison — flag it explicitly as an unverified,
  third-hand vendor marketing claim with an internal product-naming
  inconsistency in the source itself (see Extraction Notes), citable only as
  "Glean has publicly claimed a 4x cost advantage over a Claude coding
  product, unverified."

- **Chapter 05 (Team Adoption)**: Add Claim 10 (enterprises no longer
  willing to depend on one or two model providers) as a distinct,
  citable motivation for multi-model strategies — separate from the
  cost-optimization motivation that dominates most of this corpus's routing
  coverage — for any guide section on why teams adopt multi-vendor model
  strategies.

## Extraction Notes

- **Fetch method**: WebFetch's AI-summarization pass against this URL
  returned only a condensed, paraphrased summary on first request and
  reconstructed (not verbatim) sentences on a follow-up targeted request,
  consistent with the limitation already documented in several other source
  notes in this corpus (e.g. `blog-google-api-gateway-model-routing.md`,
  `blog-cursor-router-model-classifier.md`). The article's raw HTML was
  instead fetched directly via `curl` with a browser user agent (HTTP 200),
  script/style blocks were stripped, remaining HTML tags were removed with a
  Python regex pass, and HTML entities were decoded, yielding a 78-line
  plain-text rendering of the full article. This is a short article (~1,500
  words); all `Quote` fields above were copied character-for-character from
  that extracted plain text, keeping individual quotes short per this
  repo's copyright-conscious extraction practice.
- **No sub-pages followed.** The article references a "technical blog post"
  about Waldo and a prior Latent Space interview with Deedy Das (April 2023)
  without linking either with a resolvable URL in the extracted text, so
  neither was fetched. Both are flagged above as unverified secondary
  references rather than followed.
- **Internal inconsistency in the source, not resolved by this extraction**:
  the article names "Claude Code" and "Claude Cowork" as if referring to the
  same comparison product within a single sentence relaying Tony
  Gentilcore's cost claim (Claim 5). This extraction preserves the
  inconsistency verbatim rather than silently resolving it, since resolving
  it would require reading Gentilcore's original (unlinked) statement.
- **No contradiction issues filed.** Cross-referenced against all
  model-routing, model-selection, and cost-governance source notes
  identified in the corpus (see Cross-References); found no claim here that
  materially opposes an existing note's settled claim on the same fact in a
  way that would drive different guide advice — see Cross-References →
  Contradicts for the one scope-difference near-miss considered and ruled
  out.
- **Confidence calibration: anecdotal.** Nearly every quantitative claim in
  this article (Claims 3, 4, 5, 6, 7, 9, 10, 12) is a single Glean
  executive's rounded, unsourced estimate or a vendor-self-reported
  percentage/dollar figure with no disclosed methodology, baseline, sample
  size, or measurement window — and one of the two headline cost figures
  (Claim 5) is relayed third-hand from a different executive's separate,
  unlinked public statement and contains an internal product-naming
  inconsistency. Only the product-feature description (Claim 2, the
  three-tier selection architecture) and the evaluation-methodology
  description (Claim 8, shadow-testing plus AI judges) are rated above
  "anecdotal," because both are structural/mechanistic descriptions
  checkable in principle rather than unverifiable performance percentages.
  The overall note is rated "anecdotal" rather than "emerging" because the
  bulk of its evidentiary weight — and its most guide-tempting numbers
  (10-20x cost growth, 50%/25% Waldo savings, $0.45-vs-$1.84 cost-per-task,
  80% Zillow adoption) — are unaudited, single-source vendor claims, a lower
  evidentiary bar than the "emerging"-rated Cursor Router and Google API
  Gateway posts in this corpus, both of which disclose at least partial
  methodology (training-set size, A/B test scale, or documented API
  behavior) for their headline figures.
