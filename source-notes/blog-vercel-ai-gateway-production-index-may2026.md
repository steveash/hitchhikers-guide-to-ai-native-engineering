---
source_url: https://vercel.com/blog/ai-gateway-production-index-june-2026
source_type: blog-post
title: "DeepSeek enters the fight for token volume, Anthropic continues to dominate spend"
author: Jerilyn Zheng, Harpreet Arora, Eric Dodds (Vercel)
date_published: 2026-06-08
date_extracted: 2026-07-07
last_checked: 2026-07-07
status: current
confidence_overall: emerging
issue: "#1600"
---

# DeepSeek Enters the Fight for Token Volume, Anthropic Continues to Dominate Spend

> Vercel's monthly AI Gateway production index for May 2026: DeepSeek V4's launch
> took its token share from under 1% to 17% (third place, ahead of OpenAI) while
> its spend share stayed near 1%, illustrating a broader pattern in which
> low-cost models absorb high-volume work while Anthropic grew its spend share
> from 61% to 65% and held 70-80% of spend in every high-stakes use case
> (AI app generation, back-office agents, coding agents).

## Source Context

- **Type**: blog-post (Vercel Blog, "AI Gateway production index" recurring
  monthly series; this installment published June 8, 2026, reporting on May
  2026 gateway activity — the series names each report by publish month while
  covering the prior calendar month's data, per the post's own closing
  reference: "Read the April 2026 AI Gateway production index" as the prior
  installment). Includes seven charts/figures (with alt-text captions) and one
  data-methodology appendix; roughly 1,400 words of body text plus captions.
- **Author credibility**: Jerilyn Zheng, Harpreet Arora, and Eric Dodds,
  published under the Vercel Blog. Vercel operates the AI Gateway product
  itself, so this is first-party infrastructure-provider telemetry, not
  third-party survey or self-reported customer data — the numbers derive
  directly from requests routed through Vercel's own product. This gives high
  confidence in the *internal consistency* of the reported percentages (they
  are actual routing counts, not estimates or extrapolations), but the dataset
  reflects only traffic that flows through Vercel AI Gateway, not the AI
  market as a whole — a customer-base selection effect the post does not
  quantify or caveat explicitly.
- **Scope**: Covers month-over-month (April→May 2026) token volume and spend
  share by model/provider (DeepSeek, Anthropic, OpenAI, Google/Gemini),
  a per-use-case breakdown (AI coding agents, back-office agents, AI app
  generation), B2B vs. B2C cost differences, tool-use token/request density,
  and model-diversity-by-scale. Does NOT cover: absolute dollar or token
  figures (all data is presented as percentage shares); non-Gateway traffic
  (traffic outside Vercel's own product); customer identities or company-level
  breakdowns; or root-cause analysis of *why* teams choose particular models
  beyond the price/quality framing given.

## Extracted Claims

### Claim 1: DeepSeek's token share on AI Gateway jumped from under 1% to 17% in a single month (May 2026), making it the third-largest provider by volume, ahead of OpenAI — while its spend share stayed near 1%
- **Evidence**: Vercel's own first-party routing-volume and spend data, aggregated across all AI Gateway traffic; the post states April's DeepSeek share was "less than 1% of AI Gateway tokens and less than 0.2% of spend."
- **Confidence**: settled (directly measured routing/spend counts from the platform operator, not a survey or estimate)
- **Quote**: "DeepSeek's share of tokens jumped from under 1% to 17% in a single month, while its share of spend stayed near 1%."
- **Our assessment**: This is the report's headline finding and the most concrete confirmation yet in this corpus that DeepSeek V4's aggressive pricing (documented in `blog-simonwillison-deepseek-v4.md`) translated into actual production adoption rather than remaining a benchmarking curiosity. The volume/spend divergence (17% of tokens vs. ~1% of spend) is only possible at DeepSeek V4 Flash's price floor, which independently corroborates the magnitude of the price gap Willison reported in April.

### Claim 2: DeepSeek V4 Flash launched at $0.14 input / $0.28 output per million tokens — roughly 20-50x lower than comparable Anthropic models and 8-12x lower than other value-tier flagships like Qwen 3.6 Plus and Kimi K2.6
- **Evidence**: Stated directly in the post as the driver of DeepSeek's volume surge; Vercel frames this as the mechanism, not merely a coincidence, tying the pricing figure directly to the token-share jump in Claim 1.
- **Confidence**: settled (published list pricing, directly quoted figure matching the exact input/output numbers independently reported in `blog-simonwillison-deepseek-v4.md`)
- **Quote**: "DeepSeek V4 Flash launched at $0.14 input / $0.28 output per million tokens, roughly 20–50× lower than comparable Anthropic models and 8–12× lower than other value-tier flagships like Qwen 3.6 Plus and Kimi K2.6."
- **Our assessment**: The $0.14/$0.28 figures match `blog-simonwillison-deepseek-v4.md` Claim 2 exactly, giving independent, non-overlapping corroboration (Willison's post is an April 24 hands-on pricing-table comparison; this is June 8 aggregate production-routing data) that the pricing held steady into production billing. The new information here is the "8-12× lower than other value-tier flagships" comparison against Qwen 3.6 Plus and Kimi K2.6 — neither of those two models' pricing is yet documented anywhere in this corpus, so this is a new (if imprecise, given as a range rather than exact figures) data point about the broader low-cost model tier.

### Claim 3: Anthropic's spend share on AI Gateway grew from 61% to 65% in May 2026, while its token share grew from 26% to 32%
- **Evidence**: Vercel's own first-party spend and volume aggregation.
- **Confidence**: settled (directly measured share figures from the platform operator)
- **Quote**: "Anthropic’s token share grew from 26% to 32%, and its spend share from 61% to 65%."
- **Our assessment**: This is the first figure in this corpus quantifying Anthropic's actual production market share (as opposed to revenue run-rate methodology, covered by `blog-simonwillison-anthropic-run-rate.md`, which addresses how Anthropic reports revenue but not its share of any observed traffic). That Anthropic's *token* share grew even as DeepSeek's token share exploded (Claim 1) means Anthropic gained token share in absolute production terms simultaneously with DeepSeek's entry — the two are not a zero-sum swap; both grew, apparently at the expense of other providers (OpenAI's token share "held near 13%" per Claim 4, implying Google/Gemini and smaller providers likely absorbed most of the share loss, though the post does not break this out explicitly).

### Claim 4: OpenAI's token share held near 13% in May, but its spend share ticked up from 12% to 13% on a much larger total, meaning customers paid more per OpenAI token in May than in April
- **Evidence**: Vercel's own first-party spend and volume data.
- **Confidence**: settled (directly measured; the post's own interpretive gloss — "so customers were paying more per OpenAI token in May" — is a straightforward arithmetic inference from flat token share plus rising spend share, not a separate claim needing independent verification)
- **Quote**: "OpenAI’s token share held near 13%, but its spend share ticked up from 12% to 13% on a much larger total, so customers were paying more per OpenAI token in May."
- **Our assessment**: This is a subtler signal than the DeepSeek/Anthropic headline: it implies a shift in *which* OpenAI models or tiers customers used (toward pricier ones), or a list-price increase, rather than a change in OpenAI's usage volume. The post does not disambiguate between these two mechanisms, and no other source in this corpus documents an OpenAI price increase in this window — this should be treated as an open question rather than a settled explanation.

### Claim 5: In the AI coding agent use case specifically, DeepSeek drove 49% of the segment's token volume but only 4% of the cost, while Anthropic drove 28% of tokens and 70% of the cost
- **Evidence**: Vercel's own first-party per-use-case volume/spend breakdown, presented as the clearest illustration of the low-cost/frontier split.
- **Confidence**: settled (directly measured, use-case-segmented data)
- **Quote**: "DeepSeek drove 49% of the segment’s token volume, but only 4% of the cost. Anthropic drove 28% of tokens and 70% of the cost."
- **Our assessment**: This is the single most concrete, guide-relevant data point in the source: within one specific, named use case (coding agents), it quantifies exactly how volume and spend diverge between a low-cost and a frontier provider. It directly extends the qualitative "smart routing" and "circuit breaker" cost-governance patterns documented in `blog-thoughtworks-omahony-feature-token-budgets.md` and `blog-thoughtworks-kamelman-token-crisis.md` with an actual market-level outcome: teams are not choosing one model exclusively but splitting coding-agent workloads roughly 49/28 by volume between DeepSeek and Anthropic while spending roughly 4%/70% — i.e., using DeepSeek for high-volume, lower-stakes coding-agent calls and Anthropic for the smaller share of higher-stakes ones.

### Claim 6: The average cost per token across AI Gateway rose approximately 20% in May compared to April, even with DeepSeek pulling the average down, because demand for frontier-model work grew faster than demand for non-frontier work
- **Evidence**: Vercel's own first-party aggregate spend/volume ratio, with the post's own causal interpretation ("That increase happened because the work that demands frontier models grew faster than the work that doesn't").
- **Confidence**: emerging (the per-token cost increase itself is a directly measured ratio; the causal attribution — frontier-demand growth outpacing non-frontier growth — is Vercel's own interpretation of the aggregate pattern, not independently decomposed with supporting figures beyond the coding-agent use case in Claim 5)
- **Quote**: "Customers paid almost 20% more per token on average than in April... The average token got more expensive in May, even with DeepSeek pulling the average down. That increase happened because the work that demands frontier models grew faster than the work that doesn’t."
- **Our assessment**: This is a genuinely counterintuitive finding worth flagging for the guide: a massive influx of a 20-50x cheaper model (Claim 1-2) did not lower the *average* price customers paid per token — it rose. This directly challenges any assumption that cheap-model entry mechanically drives down blended AI costs; it can coincide with (and be outpaced by) even faster growth in frontier-model consumption. Practitioners reasoning about "will costs come down as cheaper models enter the market" should treat this as evidence that aggregate cost trends depend on the *mix shift* in demand, not just the price floor.

### Claim 7: Google's Gemini 3.5 Flash launched in May 2026 at a higher price point than Gemini 3.0 Flash, and migration did not happen at scale — by month-end, 3.5 held only 7% of the Flash family's tokens while 3.0 held 90%
- **Evidence**: Vercel's own first-party model-family token-share breakdown, contrasted explicitly against the faster adoption curve of Gemini 3.1 Pro in Feb-March 2026 ("it gained 30% adoption immediately, and by the next month was the dominant model in the family" — this figure appears only in the chart caption, not the body text).
- **Confidence**: settled (directly measured token-share-by-model data)
- **Quote**: "Gemini 3.5 Flash launched in May at a higher price point than Gemini 3.0 Flash, but migration didn’t happen at scale. By month-end, 3.5 held only 7% of the Flash family’s tokens while 3.0 held 90%."
- **Our assessment**: This is the clearest evidence in the source for genuine price sensitivity among Vercel's customer base, independent of the DeepSeek story: when a same-vendor, same-tier model gets more expensive with no accompanying capability leap large enough to justify it in customers' eyes, adoption stalls even without a cheaper competitor actively displacing it. This corroborates the broader "cost-consciousness" and "smarter routing" framing that runs through this entire report (Claims 1, 5, 6) and gives the guide a second, vendor-internal example (distinct from the cross-vendor DeepSeek/Anthropic split) of the same underlying behavior: teams evaluate price increases against demonstrated value before migrating, even within a single provider's own model family.

### Claim 8: B2B applications cost roughly 60% more per token than B2C applications in May 2026, because B2B workloads run fewer, more expensive calls while B2C runs many cheap ones
- **Evidence**: Vercel's own first-party token/spend classification by B2B vs. B2C application type, presented as an appendix finding.
- **Confidence**: settled (directly measured aggregate classification)
- **Quote**: "B2B applications run fewer, more expensive calls, while B2C applications run many cheap ones. On a per-token basis, B2B cost roughly 60% more than B2C in May."
- **Our assessment**: This is a new segmentation dimension for this corpus's cost-governance material — prior sources (`blog-thoughtworks-omahony-feature-token-budgets.md`, `blog-thoughtworks-kamelman-token-crisis.md`) discuss cost governance by use case (coding agent, back-office) or by organization (Uber, Meta, Shopify), not by B2B/B2C application classification. The post's own explanation ("higher consequence-of-error scenarios," per the WebFetch-derived summary — note this specific causal phrase does not appear verbatim in the parsed article text and should not be quoted; see Extraction Notes) is plausible but unconfirmed by any worked example in the post itself.

### Claim 9: Tool-use requests represent just under a quarter of all AI Gateway requests but carry over half of all tokens — agentic traffic runs roughly 2.5x denser per request than average
- **Evidence**: Vercel's own first-party request/token classification by whether a request ends in a tool call.
- **Confidence**: settled (directly measured aggregate classification)
- **Quote**: "Just under a quarter of requests end in a tool call, but those requests carry well over half of all tokens. Both metrics are roughly flat month-over-month."
- **Our assessment**: This quantifies something previously only qualitatively assumed in this corpus's agent/tool-use coverage: that agentic (tool-calling) requests are disproportionately token-heavy relative to their share of request volume. The "roughly flat month-over-month" note is also relevant — this ratio appears stable rather than rapidly changing, suggesting it reflects a structural property of tool-use requests (e.g., larger context from tool results, multi-turn tool-call chains) rather than a transient May-specific event.

### Claim 10: Model diversity within a production application rises with request scale — single-model setups dominate the lowest-volume tier, while at 1M+ monthly requests, most apps route across 11 or more distinct models
- **Evidence**: Vercel's own first-party model-count-per-app classification, segmented by request-volume tier.
- **Confidence**: settled (directly measured aggregate classification)
- **Quote**: "The more requests an app serves, the more models it runs in production. Single-model setups dominate the lowest-volume tier, while at 1M+ requests the majority of apps route across 11 or more models."
- **Our assessment**: This is a strong, previously undocumented-in-corpus data point supporting model-routing/multi-model architecture as a majority production pattern at scale, not a niche optimization. It gives a concrete number ("11 or more models") for what "smart routing" (Claims 5-7) looks like architecturally once an application is large enough — a useful anchor for any guide section arguing that mature AI-native applications should expect to maintain multiple model integrations rather than a single-model dependency.

### Claim 11: The prior month's news cycle included Uber "burning through its annual Claude Code budget shortly after Q1" and Amazon shutting down an internal system called "KiroRank" to curb what the post calls "unproductive tokenmaxxing," but the May data shows production spend on these use cases still increased despite that cost-overrun narrative
- **Evidence**: Vercel's own framing paragraph, contextualizing the report against contemporaneous press coverage, followed immediately by the post's own counter-framing that spend nonetheless rose.
- **Confidence**: anecdotal (the Uber and Amazon/KiroRank references are asserted in passing as context, not independently sourced or elaborated within this post; no link, date, or further detail is given for either)
- **Quote**: "Last month, headlines about blown token budgets dominated tech news: Uber burned through its annual Claude Code budget shortly after Q1 and Amazon shut down KiroRank to curb unproductive tokenmaxxing. While runaway cost is a real problem, this month’s report shows that spend on production use cases still increased."
- **Our assessment**: The Uber reference corroborates the Uber budget-exhaustion story already well-documented in this corpus (`blog-simonwillison-uber-caps-usage.md`, `blog-thoughtworks-omahony-feature-token-budgets.md`), though this post gives no new detail beyond what's already extracted there. The Amazon "KiroRank" reference is genuinely new to this corpus — no existing source note documents an Amazon-internal token-usage leaderboard or ranking system, nor its shutdown. This would be a fourth named-company instance of the "tokenmaxxing leaderboard" anti-pattern pattern (alongside Meta's "Claudeonomics" leaderboard in `blog-thoughtworks-omahony-feature-token-budgets.md` Claim 3/3a, Uber's spending-cap response, and Duolingo's performance-metric reversal in `blog-thoughtworks-kamelman-token-crisis.md` Claim 5) — but because this post gives only a single unsourced sentence with no link, date, or elaboration, it should be flagged as a lead to verify via a dedicated source (an Amazon/KiroRank-specific article), not treated as independently confirmed the way the Meta and Uber cases are.

## Concrete Artifacts

### Key month-over-month metrics (May 2026 vs. April 2026, verbatim from post body)

```
Total AI Gateway tokens: +20% MoM
Total AI Gateway spend: +43% MoM
Average cost per token: ~+20% MoM

DeepSeek:  token share  <1%  -> 17%   |  spend share  <0.2% -> ~1%
Anthropic: token share  26%  -> 32%   |  spend share  61%   -> 65%
OpenAI:    token share  ~13% (flat)   |  spend share  12%   -> 13%

Anthropic spend share within every high-stakes use case
(AI app generation, back-office agents, coding agents): 70-80%

Coding-agent use case specifically:
  DeepSeek:  49% of tokens,  4% of cost
  Anthropic: 28% of tokens, 70% of cost

Gemini Flash family, end of May:
  Gemini 3.0 Flash: 90% of family tokens
  Gemini 3.5 Flash (newer, pricier):  7% of family tokens

B2B vs B2C: B2B costs ~60% more per token than B2C
Tool-use requests: ~24% of requests, >50% of tokens (~2.5x denser per request)
Model diversity: at 1M+ monthly requests, most apps route across 11+ models

Source: Vercel Blog, "DeepSeek enters the fight for token volume,
Anthropic continues to dominate spend" (AI Gateway production index,
May 2026 data), published June 8, 2026,
https://vercel.com/blog/ai-gateway-production-index-june-2026
```

### Methodology note (verbatim)

```
"This analysis is based on anonymized, aggregate routing data from the
Vercel AI Gateway through May 2026.
A few notes on measurement:
Spend uses market-rate pricing (published list price) to provide a
normalized view across teams that bring their own API keys.
Volume counts tokens routed through AI Gateway.
B2C, B2B, and use-case classifications are aggregate. No individual team
or workload is identified."

Source: same as above, "About this data" appendix section.
```

### DeepSeek market-entry mechanism (verbatim)

```
"From February to April, volume distribution across labs on AI Gateway
changed slowly, but in May, DeepSeek V4's launch completely shifted token
share. The low-cost end of the market that barely existed in April became
AI Gateway's third-largest provider by volume in May, without a
significant impact on overall spend."
"Almost all of the volume comes from two models: deepseek/deepseek-v4-flash
and deepseek/deepseek-v4-pro, both released in May."
"Price alone wouldn't have shifted DeepSeek's volume that much in a month,
meaning teams testing DeepSeek V4 against their existing evals found the
output good enough to ship, not just low-cost enough to try."

Source: same as above, "Low-cost models saw significant production volume
for the first time" section.
```

## Cross-References

### Cross-reference verification notes
`blog-simonwillison-deepseek-v4.md`, `blog-simonwillison-anthropic-run-rate.md`,
`blog-thoughtworks-kamelman-token-crisis.md`, and
`blog-thoughtworks-omahony-feature-token-budgets.md` were re-read directly
(MINER.md §4b) and the claim numbers cited below were confirmed against
each note's numbered `### Claim N:` headings in document order before
writing this section.

- **Corroborates**:
  - `blog-simonwillison-deepseek-v4.md` Claim 2 (V4-Flash priced at
    $0.14/$0.28 per million input/output tokens, undercutting GPT-5.4 Nano):
    this source's Claim 2 independently confirms the identical price figures
    at the production-billing level, roughly six weeks after Willison's
    April 24 hands-on pricing-table observation. Willison established the
    price floor; this source shows the floor held into June production
    routing and quantifies its actual market effect (Claim 1: 17% token
    share at ~1% spend share).
  - `blog-simonwillison-uber-caps-usage.md` and
    `blog-thoughtworks-omahony-feature-token-budgets.md` Claim 1 (Uber
    exhausted its 2026 AI budget by April, driven by Claude Code adoption):
    this source's Claim 11 corroborates the Uber budget-exhaustion story in
    passing, as background context for its own May-2026 spend-increase
    finding, though it adds no new detail beyond what those two notes
    already document.
  - `blog-thoughtworks-omahony-feature-token-budgets.md` Claim 3/3a (Meta's
    employee-built "Claudeonomics" token leaderboard) and
    `blog-thoughtworks-kamelman-token-crisis.md` Claim 5 (Duolingo reversing
    an AI-activity performance metric): this source's Claim 11 (Amazon
    shutting down "KiroRank" to curb "unproductive tokenmaxxing") is a
    fourth named-company data point in the same "leaderboard/metric-gaming
    anti-pattern gets walked back" cluster — though unlike the Meta and
    Duolingo cases, this one is asserted here with no link or independent
    detail and should be treated as a lead, not a confirmed case, until a
    dedicated source is mined.

- **Contradicts**: None identified. This source's Claim 6 (average per-token
  cost rose ~20% even as a 20-50x cheaper model entered at scale) is in
  tension with a naive reading of `blog-simonwillison-deepseek-v4.md`'s
  framing (cheap models should pull blended costs down), but this is not a
  MINER.md §4a contradiction — Willison's post makes no claim about
  *aggregate market* cost trends, only about DeepSeek V4's own price
  position relative to other models. The two sources address different
  questions (per-model price floor vs. blended market average) and do not
  make opposing claims about the same fact.

- **Extends**:
  - `blog-simonwillison-anthropic-run-rate.md`: that note documents how
    Anthropic *calculates and reports* its own run-rate revenue (a
    methodology question) but contains no data on Anthropic's actual market
    or production share. This source's Claim 3 (Anthropic's spend share
    61%->65%, token share 26%->32% on Vercel's gateway) is the first figure
    in this corpus for Anthropic's observed production market share from an
    independent (non-Anthropic) infrastructure provider, giving practitioners
    a data point to weigh against Anthropic's self-reported revenue
    methodology.
  - `blog-thoughtworks-omahony-feature-token-budgets.md` and
    `blog-thoughtworks-kamelman-token-crisis.md`: both notes document
    organizational responses (budgets, circuit breakers, routing strategy)
    to token-cost pressure via named-company case studies (Uber, Meta,
    Shopify, Duolingo). This source extends that qualitative
    cost-governance narrative with market-level, quantified evidence
    (Claim 5's 49%/4% vs. 28%/70% coding-agent split) that the "smart
    routing between cheap and frontier models" pattern those notes describe
    is now visible in aggregate production data, not just individual
    company anecdotes.

- **Novel**:
  - **Quantified token-share vs. spend-share divergence for a single
    newly-launched model family** (Claim 1): no existing corpus source
    measures a model's production adoption curve in these terms (17% of
    volume at ~1% of spend, one month after launch).
  - **Per-use-case volume/spend split between a low-cost and frontier
    provider** (Claim 5): the coding-agent 49%/4% vs. 28%/70% breakdown is
    the first use-case-level quantification of the low-cost/frontier
    routing split in this corpus.
  - **Average per-token cost rising despite cheap-model entry** (Claim 6):
    a novel, somewhat counterintuitive market dynamic not addressed by any
    existing corpus source.
  - **Within-vendor price-increase adoption stall** (Claim 7, Gemini 3.5
    Flash vs. 3.0 Flash): the first documented case in this corpus of price
    sensitivity being demonstrated *within* a single vendor's own model
    family rather than via cross-vendor substitution.
  - **B2B/B2C per-token cost differential, tool-use token density, and
    model-diversity-by-scale** (Claims 8-10): three new segmentation
    dimensions for production AI cost/architecture data not previously
    present in this corpus.
  - **Amazon "KiroRank" reference** (Claim 11): a new, unconfirmed lead
    for a possible fourth tokenmaxxing-leaderboard case study.

## Guide Impact

- **Chapter 01 (Market Overview)**: Add Claims 1, 3, and 4 as the corpus's
  first independently-measured (non-vendor-self-reported) production market
  share figures: DeepSeek at 17% of tokens/~1% of spend, Anthropic at 32%
  tokens/65% spend, OpenAI at ~13% tokens/13% spend, all as of May 2026 on
  Vercel's AI Gateway. Flag clearly that this is Vercel-gateway-specific
  traffic, not total market share.

- **Chapter 03 (Model Selection Dynamics)**: Add Claim 5 (coding-agent
  49%/4% DeepSeek vs. 28%/70% Anthropic split) as a concrete illustration of
  price-tiered model routing in a specific, named use case — this is a
  stronger, quantified successor to the general "route cheap work to cheap
  models" advice already implied by `blog-thoughtworks-omahony-feature-token-budgets.md`.
  Add Claim 7 (Gemini 3.5 Flash's stalled adoption vs. 3.0 Flash) as a
  cautionary data point: a same-vendor price increase without a
  commensurate capability jump can stall adoption even without a
  competing cheaper vendor in the picture.

- **Chapter 04 (Cost Engineering at Scale)**: Add Claim 6 (average
  per-token cost still rose ~20% MoM despite a 20-50x cheaper model
  entering at 17% volume share) as a correction to any assumption that
  cheap-model market entry mechanically lowers blended AI spend — mix
  shift toward more frontier-model use can outpace and overwhelm the
  savings from cheap-model adoption. Add Claim 10 (11+ models per app at
  1M+ monthly requests) as a concrete target for what mature multi-model
  routing architecture looks like at scale, and Claim 9 (tool-use requests
  are ~2.5x denser per request) as a sizing input for teams estimating
  agentic-workload token budgets.

- **Chapter 06 (Governance and Cost Management)**: Note Claim 11's Amazon
  "KiroRank" reference as an unconfirmed lead — recommend the Prospector
  file a new source-submission issue to find a dedicated article on this,
  since if confirmed it would be a fourth named-company instance (after
  Meta, Uber, and Duolingo) of the token-usage-leaderboard anti-pattern
  cluster already documented via `blog-thoughtworks-omahony-feature-token-budgets.md`
  and `blog-thoughtworks-kamelman-token-crisis.md`.

## Extraction Notes

1. **Source fetched via direct HTTP, not WebFetch's AI-summarized output.**
   Per MINER.md §2a, an initial WebFetch pass returned "quotes" that varied
   slightly in wording across two separate fetches of the same URL (e.g.
   "jumped from under 1% to 17%" vs. "surged from under 1% to 17%"),
   indicating the tool was paraphrasing rather than returning verbatim
   text. This note instead retrieved the raw page HTML via a direct `curl`
   request, isolated the `<article>` element, stripped markup with a
   Python script, and read the resulting plain text in full (`/tmp/vercel_article.txt`,
   93 lines). Every `Quote` field in this note is taken from that
   locally-parsed verbatim text and cross-checked against the raw HTML
   directly (including `<figcaption>`/`alt` attributes for chart captions),
   not from the WebFetch summarization.
2. **No sub-pages followed.** The post links to a prior "April 2026 AI
   Gateway production index" report, but that report is out of scope for
   this issue (it is a separate monthly installment covering March 2026
   data) and was not fetched; MINER.md's "follow up to 5 linked pages"
   guidance applies to substantive supporting pages within scope of the
   current source, and the prior month's report is a distinct source in
   its own right, better mined separately if the Prospector queues it.
3. **One phrase flagged as unverifiable and excluded from quotes**: an
   initial WebFetch pass rendered a phrase resembling "reflecting higher
   consequence-of-error scenarios" for the B2B/B2C cost differential
   (Claim 8), but this exact wording does not appear in the verbatim parsed
   article text (the parsed text only states the B2B/B2C mechanism as
   quoted in Claim 8 and Concrete Artifacts, without that specific
   "consequence-of-error" phrasing). It is not presented as a quote in this
   note, and the Claim 8 "Our assessment" flags it explicitly as
   WebFetch-derived and unconfirmed rather than treating it as the source's
   own words.
4. **No contradiction issues filed.** Cross-referenced against all
   token-cost, DeepSeek-pricing, and Anthropic-revenue notes currently in
   the corpus; found no claim here that materially opposes an existing
   note's claim in a way that would drive different guide advice (see
   Cross-References → Contradicts for the one near-miss considered and
   ruled out).
5. **Confidence calibration: emerging.** Most individual claims are rated
   "settled" because they are direct, first-party measured routing/spend
   percentages from the platform operator (not estimates, surveys, or
   self-reports). The overall note is rated "emerging" rather than
   "settled" because: (a) the dataset is limited to Vercel AI Gateway
   traffic specifically, an unquantified and unrepresentative-by-definition
   slice of total AI market activity; (b) several interpretive/causal
   claims (Claim 4's price-increase explanation, Claim 6's demand-mix
   attribution, Claim 8's WebFetch-flagged causal phrase) are the authors'
   own inference rather than independently decomposed; and (c) Claim 11's
   Amazon "KiroRank" reference is a single unsourced sentence with no
   independent corroboration available in this extraction.
