---
source_url: https://simonwillison.net/2026/Aug/23/anthropics-best-ai-model-struggles-to-attract-users-as-cheaper-t/
source_type: blog-post
title: "Anthropic's best AI model struggles to attract users as cheaper tools thrive"
author: Simon Willison (relaying Financial Times reporting; quoting a Ramp AI index chart)
date_published: 2026-08-23
date_extracted: 2026-08-31
last_checked: 2026-08-31
status: current
confidence_overall: anecdotal
issue: "#3125"
---

# Anthropic's best AI model struggles to attract users as cheaper tools thrive

> Simon Willison relays Financial Times reporting on Anthropic's July 2026
> revenue ($65bn run-rate, up from $47bn in May) and introduces the Ramp AI
> index — billing data from 70,000 Ramp-card companies — showing that a
> full month after Opus 5's launch, the older Opus 4.8 still commands 28% of
> Anthropic model spend, more than triple Opus 5's 3.5% share, which
> Willison reads as support for "the idea that Fable's cost has made it a
> less popular model."

## Source Context

- **Type**: blog-post (Simon Willison's link-blog "linkblog" format — a
  short excerpt/summary plus his own framing and an embedded data table;
  published 23rd August 2026 at 8:24pm, filed under "Link Blog" per the
  page's own eyebrow label). The post's headline links out to a Financial
  Times article, "Anthropic's best AI model struggles to attract users as
  cheaper tools thrive" (ft.com/content/5ee49718-c258-4f01-aa32-7e5b76ae5245),
  reached "via" a Hacker News discussion (news.ycombinator.com/item?id=49411102).
  The FT article itself is paywalled and was not fetched directly; per
  MINER.md's "read the entire source" instruction, this note extracts from
  Willison's own page, which is the accessible, citable text — he explicitly
  quotes and paraphrases specific numbers "gathered from 'people with
  knowledge of the matter'" from the FT piece, and separately introduces and
  quotes the Ramp AI index data as his own addition, not sourced to the FT
  article. No other substantive linked sub-pages existed to follow: the FT
  link is paywalled, and the Ramp AI index link (ramp.com/data/ai-index) is
  a live/rolling dashboard, not a dated report — Willison's post itself
  states the specific July 2026 figures he read from it at time of writing,
  and this note treats his quoted November-derived figures, not the current
  state of the live dashboard, as the source text.
- **Author credibility**: Simon Willison is the creator of Django and the
  `llm` CLI, and is designated a `trusted-feed` source in this repo for
  independent, high-signal LLM-tooling commentary with no vendor
  affiliation. Here he functions partly as a curator (relaying FT's
  anonymously-sourced reporting) and partly as an independent analyst (he
  personally states the Ramp figures "look reasonable" and offers his own
  interpretation of what they imply about Fable's pricing). The underlying
  revenue figures are FT's own reporting, attributed only to "people with
  knowledge of the matter" — an anonymous-sourcing pattern, not a formal
  Anthropic disclosure. The Ramp AI index figures are first-party billing
  data from a corporate card/spend-management company (Ramp), aggregating
  actual customer spend across 70,000 companies, which is a stronger
  evidentiary basis than the anonymously-sourced revenue figures, though
  Willison's page is the only source for the specific number set quoted
  here — it was not independently cross-checked against Ramp's live
  dashboard by this Miner.
- **Scope**: Covers (1) Anthropic's July 2026 annualized revenue figure
  and its growth from May 2026, (2) Anthropic's claim of profitability
  expectations and a customer-count/spend-tier figure, (3) OpenAI's
  contemporaneous revenue growth and the GPT 5.6 launch's effect on it, and
  (4) a ten-model breakdown of Anthropic model spend share from the Ramp AI
  index for July 2026. Does NOT cover: any methodology detail for how Ramp
  computes "model adoption" from billing data (e.g., whether by
  request count, token count, or dollar spend), any absolute dollar figures
  for the Ramp breakdown (all ten figures are percentages), Anthropic's own
  response or comment on the FT story, or any comparison to non-Anthropic
  model vendors' adoption curves.

## Extracted Claims

### Claim 1: Anthropic's "annualized revenue" for July 2026 reached $65 billion, up from $47 billion in May 2026
- **Evidence**: Willison's own summary sentence of the FT story's reported
  figures, presented as one of "a few interesting numbers in this FT story
  gathered from 'people with knowledge of the matter.'"
- **Confidence**: anecdotal (FT's own reporting is attributed to anonymous
  sources — "people with knowledge of the matter" — not a formal Anthropic
  disclosure; Willison relays without independently verifying)
- **Quote**: "Anthropic's \"annualized revenue\" for July is up to $65bn - it
  was $47bn in May, and I collected more historic numbers here."
- **Our assessment**: This directly extends the revenue trajectory already
  in the corpus from `blog-simonwillison-anthropic-47b-revenue.md` Claim 1
  ($9B Dec 2025 → $14B Feb 2026 → $30B Apr 2026 → $47B May 2026, sourced
  from Anthropic's own Series H fundraising disclosures). The new $65B July
  figure continues that trajectory (+~38% in two months), but with a
  materially weaker evidentiary basis than the prior four data points: the
  May 2026 note's figures came from Anthropic's own fundraising
  announcement (with the associated securities-fraud-liability credibility
  argument Willison made in that post), while this $65B figure is FT's
  anonymously-sourced reporting, not a formal Anthropic disclosure quoted
  directly. Treat as directionally consistent with the established
  trajectory but lower-confidence than the four prior points on that same
  trajectory line.

### Claim 2: Anthropic expects Q3 2026 to be profitable under the same profitability model it used to declare Q2 2026 profitable, and told investors it has 6,000 customers spending $100,000 or more annually
- **Evidence**: Willison's summary of a second FT-reported figure, with one
  short direct quote embedded.
- **Confidence**: anecdotal (same anonymous-sourcing basis as Claim 1; the
  "same model they used to declare Q2 profitable" framing is Willison's own
  paraphrase of the FT reporting, not a quoted methodology description)
- **Quote**: "It also told investors that it had 6,000 customers that spend
  $100,000 annually or more."
- **Our assessment**: The 6,000-customer, $100K+-spend figure is a new,
  specific enterprise-adoption data point not previously in the corpus —
  prior corpus revenue sources (the $47B note) document aggregate run-rate
  revenue and one dramatic single-customer cost-overrun anecdote ($500M in
  one month), but no source before this one gives a customer-count
  breakdown at a defined spend threshold. Useful as a scale indicator for
  "how many enterprise customers is Anthropic's revenue actually spread
  across," though the article gives no context for what fraction of total
  revenue these 6,000 customers represent.

### Claim 3: OpenAI's annualized revenue jumped 35% quarter-to-date to over $40 billion, which Willison/FT attribute to the July launch of GPT 5.6 "jolting the company's performance after a sluggish start to the year"
- **Evidence**: Willison's direct quote of the FT reporting on OpenAI,
  presented as the third of the three FT-sourced figures in the post.
- **Confidence**: anecdotal (same "people with knowledge of the matter"
  anonymous-sourcing basis as Claims 1-2)
- **Quote**: "annualised revenue has jumped 35 per cent in the quarter to
  date and is now over $40bn, with the launch of GPT 5.6 in July jolting
  the company's performance after a sluggish start to the year"
- **Our assessment**: This is a comparative data point — Anthropic's ~$65B
  versus OpenAI's ~$40B+ annualized revenue in the same reporting window —
  giving the guide a same-source, same-moment comparison between the two
  largest US frontier labs' revenue trajectories, rather than figures
  reported independently at different times that would be harder to
  compare directly. The "sluggish start to the year" characterization of
  OpenAI's pre-GPT-5.6 performance is FT's own framing (via Willison), not
  independently corroborated elsewhere in this corpus.

### Claim 4: Ramp's AI index, built from billing data across 70,000 Ramp-card-using companies, estimates model adoption; for July 2026 it shows Opus 4.8 taking 28.0% of Anthropic model spend — more than three times Opus 5's 3.5% share, a full month after Opus 5's July 24th launch
- **Evidence**: Willison's own addition to the post (explicitly separate
  from the FT-sourced figures — "This article also introduced me to the
  Ramp AI index"), quoting the complete ten-model spend breakdown as an
  ordered list.
- **Confidence**: anecdotal overall for the interpretive framing (Willison's
  own reading that this "supports the idea that Fable's cost has made it a
  less popular model" is his interpretation, not Ramp's stated conclusion),
  though the underlying percentage figures themselves are first-party
  billing-data aggregates from Ramp, a stronger evidentiary basis than
  anonymously-sourced press reporting — see Concrete Artifacts for the full
  breakdown.
- **Quote**: "Here's Ramp's breakdown of Anthropic model spend for July
  2026, which looks reasonable given that Opus 5 was only released on July
  24th, and supports the idea that Fable's cost has made it a less popular
  model"
- **Our assessment**: This is the post's most novel and most guide-relevant
  contribution — a concrete, itemized model-adoption dataset at the
  individual-model level within Anthropic's own product line, rather than
  the vendor-level (Anthropic vs. OpenAI vs. Google) or category-level
  (open-weight vs. closed-weight) breakdowns already in the corpus from
  Vercel's AI Gateway index. Opus 4.8 at 28.0% of spend, more than triple
  Opus 5's 3.5% one month after Opus 5 shipped, is a striking practitioner
  data point: it shows a full model generation (Opus 4.8, from the prior
  Opus release) still dominating real spend well after a newer, presumably
  more capable successor is available — directly relevant to any guide
  claim that practitioners quickly migrate to newer/more-capable models.
  Willison's own caveat matters here too: Opus 5 having only 8 days of
  availability within the July reporting window (July 24-31) is a
  confound he flags himself ("looks reasonable given that Opus 5 was only
  released on July 24th") — this is a snapshot mid-migration, not
  necessarily Opus 5's steady-state adoption ceiling.

### Claim 5: Fable 5 (the highest-priced Claude model class) held 8.0% of Anthropic spend in July 2026, more than double Opus 5's 3.5% despite Fable 5 having been available far longer, which Willison reads as evidence that Fable's price, not its capability, is suppressing its adoption relative to what a newer top-tier model might otherwise command
- **Evidence**: Willison's direct interpretive claim, drawing on the same
  Ramp breakdown as Claim 4 (Fable 5's individual line item: 8.0%, third
  place in the ten-model ranking).
- **Confidence**: anecdotal (Willison's own inference from the spend
  percentages; no A/B or controlled comparison isolating price as the
  causal factor versus other explanations, e.g., organizational
  procurement inertia, access gating, or task-fit)
- **Quote**: "supports the idea that Fable's cost has made it a less popular
  model" (same sentence quoted in full under Claim 4; this claim isolates
  the Fable-specific reading of it)
- **Our assessment**: This is a **corroborating, independent data point**
  for the cost-driven-substitution argument already in the corpus from
  Drew Breunig's essay (`blog-simonwillison-fable-end-free-lunch.md` Claims
  1-2 and 6), which argues qualitatively, from a single practitioner's
  first-person account, that Fable's high price pushed him and others
  toward "good enough" alternatives (Opus, GLM, K3). This source supplies
  an independent, quantitative, multi-company data point (8.0% of spend
  across 70,000 billing companies) supporting the same directional claim
  from a completely different evidentiary basis (aggregate billing data
  vs. one practitioner's essay) — see Cross-References for detail on why
  this strengthens, without settling, the cost-adoption link.

### Claim 6: The full July 2026 Anthropic model spend ranking, in order, is Opus 4.8 (28.0%), Sonnet 4.6 (8.3%), Fable 5 (8.0%), Opus 4.6 (6.9%), Sonnet 5 (3.6%), Opus 5 (3.5%), Opus 4.7 (1.7%), Sonnet 4.5 (1.3%), Haiku 4.5 (1.0%), and Opus 4.5 (0.7%)
- **Evidence**: The complete verbatim ordered list from Willison's post,
  attributed to the Ramp AI index.
- **Confidence**: anecdotal overall confidence rating for this note (per
  the general sourcing caveats above), though this specific list is a
  directly quoted, itemized dataset rather than a summarized or
  interpreted figure.
- **Quote**: "Opus 4.8: 28.0%" / "Sonnet 4.6: 8.3%" / "Fable 5: 8.0%" /
  "Opus 4.6: 6.9%" / "Sonnet 5: 3.6%" / "Opus 5: 3.5%" / "Opus 4.7: 1.7%" /
  "Sonnet 4.5: 1.3%" / "Haiku 4.5: 1.0%" / "Opus 4.5: 0.7%" (each a
  separate list item in the source's ordered list; reproduced together
  here as the complete dataset — see Concrete Artifacts for the list in
  its original contiguous form)
- **Our assessment**: These ten figures sum to 63.0%, meaning roughly 37.0%
  of Anthropic model spend in this dataset falls outside the ten
  individually-listed models (presumably a long tail of smaller/older
  model versions, or non-Claude-model line items Ramp tracks separately) —
  the source does not explain this gap, and it is not addressed anywhere
  in Willison's post. Sonnet 4.6, not any Opus variant, is the
  second-highest line item (8.3%), narrowly ahead of Fable 5 (8.0%) —
  worth noting for a guide claim about "cheaper, mid-tier models capturing
  meaningful production share," since Sonnet 4.6 outspends every model
  except Opus 4.8 despite being a mid-tier, not flagship, class.

## Concrete Artifacts

### Ramp AI index: Anthropic model spend breakdown, July 2026 (verbatim ordered list)
```
Source: Ramp AI index (ramp.com/data/ai-index), as quoted in Simon
Willison's blog post, simonwillison.net/2026/Aug/23/anthropics-best-ai-model-struggles-to-attract-users-as-cheaper-t/,
23rd August 2026

"Here's Ramp's breakdown of Anthropic model spend for July 2026, which
looks reasonable given that Opus 5 was only released on July 24th, and
supports the idea that Fable's cost has made it a less popular model:"

1. Opus 4.8:   28.0%
2. Sonnet 4.6:  8.3%
3. Fable 5:     8.0%
4. Opus 4.6:    6.9%
5. Sonnet 5:    3.6%
6. Opus 5:      3.5%
7. Opus 4.7:    1.7%
8. Sonnet 4.5:  1.3%
9. Haiku 4.5:   1.0%
10. Opus 4.5:   0.7%

(Ten listed items sum to 63.0% of total Anthropic model spend; the
remaining ~37.0% is unaccounted for in the source text.)
```

### FT-reported revenue figures (verbatim, via Willison's summary and direct quotes)
```
Source: Financial Times, "Anthropic's best AI model struggles to attract
users as cheaper tools thrive" (ft.com/content/5ee49718-c258-4f01-aa32-7e5b76ae5245,
paywalled, not independently fetched), as relayed by Simon Willison,
same URL as above. Willison's own framing: "A few interesting numbers in
this FT story gathered from 'people with knowledge of the matter':"

- Anthropic: "annualized revenue" July 2026 = $65bn (up from $47bn in May 2026)
- Anthropic: expects Q3 2026 profitable, "using the same model they used
  to declare Q2 profitable"
- Anthropic: "It also told investors that it had 6,000 customers that
  spend $100,000 annually or more."
- OpenAI: "annualised revenue has jumped 35 per cent in the quarter to
  date and is now over $40bn, with the launch of GPT 5.6 in July jolting
  the company's performance after a sluggish start to the year"
```

## Cross-References

### Cross-reference verification notes
`blog-simonwillison-anthropic-47b-revenue.md`,
`blog-simonwillison-fable-end-free-lunch.md`,
`blog-vercel-ai-gateway-production-index-june2026.md`, and
`blog-thoughtworks-kamelman-ai-governance-category-error.md` were re-read
directly (MINER.md §4b) and every claim number cited below was confirmed
against those notes' numbered `### Claim N:` headings in document order
before writing this section.

- **Corroborates**:
  - `blog-simonwillison-fable-end-free-lunch.md` Claims 1, 2, and 6 (Drew
    Breunig's first-person practitioner account that Fable's high cost,
    relative to "good enough" alternatives, is causing deliberate
    model-routing away from Fable, and that this shift is not expected to
    reverse as prices generally fall): this source's Claims 4-5 (Fable 5
    at only 8.0% of Anthropic spend, versus Opus 4.8's 28.0%, more than a
    month after Opus 5 shipped) provide an independent, quantitative,
    multi-company data point for the same directional claim — aggregate
    billing data across 70,000 companies, rather than one practitioner's
    essay. This is a meaningfully different evidentiary basis (Ramp's
    billing aggregation vs. Breunig's self-reported workflow) converging
    on the same conclusion, which strengthens the case for citing the
    cost-driven-substitution pattern in the guide, though neither source
    isolates price as the sole causal factor (see Claim 5's "Our
    assessment" for the confound caveat).
  - `blog-thoughtworks-kamelman-ai-governance-category-error.md` Claim 4
    (that essay's composite argument cites "Ramp's AI Index shows >50%
    enterprise adoption this month" as one data point in an argument about
    AI capital allocation, without giving any model-level breakdown): this
    source corroborates that Ramp's AI index is an actively-cited,
    real-world adoption-tracking data source independently surfaced by two
    different authors in this corpus within the same reporting period
    (both articles reference the same underlying Ramp product), and
    extends Kamelman's aggregate "50% adoption" figure with the specific
    model-level detail Kamelman's essay does not include.
  - `blog-simonwillison-anthropic-47b-revenue.md` Claim 1 (the $9B→$14B→
    $30B→$47B run-rate trajectory through May 2026, sourced from
    Anthropic's own Series H disclosures): this source's Claim 1 extends
    that trajectory with a $65B July 2026 figure, though on a weaker
    evidentiary basis (anonymous FT sourcing vs. that note's formal
    fundraising-disclosure sourcing) — see Claim 1's "Our assessment" for
    the confidence distinction.

- **Contradicts**: None identified as a MINER.md §4a contradiction. At
  first glance, this source's Claim 4 (a full month after Opus 5's launch,
  the prior-generation Opus 4.8 still commands 8x Opus 5's spend share)
  could look like it undercuts `blog-anthropic-choosing-claude-model.md`
  Claim 1 (Anthropic's own stated default advice: "start with the most
  intelligent generally available model"). It is not a real contradiction:
  that note's Claim 1 is prescriptive vendor guidance about what
  practitioners *should* do when starting a new task, while this source's
  Ramp data is descriptive market behavior showing what a large population
  of companies is *actually* spending on in aggregate, likely reflecting
  procurement inertia, existing integrations, and the short (8-day)
  observation window for Opus 5 within the reporting month rather than a
  rejection of Anthropic's advice. A prescriptive claim about optimal
  practice and a descriptive claim about aggregate current behavior are
  different claim types, not opposing positions on the same question — no
  contradiction issue filed.

- **Extends**:
  - `blog-vercel-ai-gateway-production-index-june2026.md` Claim 9 (Vercel's
    AI-Gateway-routed data point: Fable 5 reached "22 requests for every
    100 sent to Opus 4.8" within four days of its June 9 launch, before a
    June 12 export-control suspension cut that adoption curve short): this
    source extends that single data point with a later, broader snapshot —
    two months on (July 2026, post-restoration), a different data source
    (Ramp billing aggregation vs. Vercel gateway routing), and a full
    ten-model ranking rather than a single two-model ratio. Note the two
    sources are not directly comparable as a before/after pair (different
    metrics — request-count ratio vs. spend-share percentage — and
    different underlying traffic populations), but both independently
    document Opus 4.8 retaining a dominant position relative to
    higher-tier/newer Claude models across two different measurement
    methodologies and two different months.
  - `blog-simonwillison-anthropic-47b-revenue.md`: extends the revenue
    trajectory documented there (through May 2026) with a July 2026 data
    point, and adds an OpenAI comparison figure not present in the earlier
    note.

- **Novel**:
  - **The complete ten-model Anthropic spend-share breakdown for a single
    month** (Claim 6) — no other corpus source gives an itemized,
    model-level (not just vendor-level or open/closed-weight-level)
    production spend ranking within a single vendor's product line.
  - **The 6,000-customers-at-$100K+-annual-spend figure** (Claim 2) — a
    new enterprise-scale data point not present in the prior revenue
    trajectory note.
  - **A same-source, same-moment Anthropic-vs-OpenAI revenue comparison**
    (Claim 3: ~$65B vs. ~$40B+ annualized, both reported by the same FT
    story) — prior corpus revenue figures for the two companies come from
    different sources at different times, making direct comparison harder.

## Guide Impact

- **Chapter 04 (Model Selection & Cost)**: Add Claim 4's spend breakdown
  (Opus 4.8 at 28.0% vs. Opus 5 at 3.5%, one month after Opus 5's launch)
  as a concrete, quantitative illustration that real-world model adoption
  lags well behind model release — useful as a caution against guide
  language that assumes practitioners migrate to the newest model quickly.
  Pair with Claim 5/Fable 5's 8.0% share and
  `blog-simonwillison-fable-end-free-lunch.md`'s qualitative argument to
  make the combined case (quantitative + qualitative) that price, not just
  recency or benchmark performance, is a primary driver of real-world
  Claude model selection.
- **Chapter 04 (Model Selection & Cost)**: Add Claim 6's full observation
  that Sonnet 4.6 (a mid-tier model, 8.3%) narrowly outspends Fable 5 (the
  flagship, 8.0%) as evidence that mid-tier models can capture more
  aggregate production spend than the flagship class — a data point for
  any guide section arguing that cost-effective mid-tier models, not just
  frontier models, deserve default consideration for production workloads.
- **Chapter 02 (LLM Landscape) / Chapter 01 (Foundations)**: Update the
  corpus's revenue-trajectory citation with Claim 1's $65B July 2026 figure
  as the latest point on the trajectory already documented in
  `blog-simonwillison-anthropic-47b-revenue.md`, explicitly flagging the
  weaker (anonymous-sourcing) evidentiary basis relative to the prior,
  fundraising-disclosure-sourced figures on the same trajectory line.

## Extraction Notes

- **Source fetched via direct HTTP, not WebFetch's summarized output.** An
  initial WebFetch pass returned only a loose paraphrase/summary of the
  page (e.g., collapsing the ten-item Ramp list into prose, restating
  quotes with altered wording). Per MINER.md §2a, the page was instead
  fetched directly via `curl` with a standard browser user-agent; the
  `<div class="entry entryPage">` content block was located and read
  directly from the raw HTML. All quotes in this note are copied
  character-for-character from that locally-fetched HTML, not from the
  WebFetch summary.
- **The FT article itself was not fetched.** It is paywalled
  (ft.com/content/5ee49718-c258-4f01-aa32-7e5b76ae5245); this note extracts
  entirely from Willison's own page, which quotes and paraphrases the FT
  figures directly and adds the Ramp AI index data independently. Per
  MINER.md §1, no other substantive linked sub-page existed to follow — the
  Hacker News "via" link is a discussion thread, not primary content, and
  was not followed as a source of additional claims.
  Ramp's AI index page (ramp.com/data/ai-index) is a live, continuously
  updating dashboard rather than a dated report; this note relies on the
  specific July 2026 figures as quoted verbatim in Willison's post, not on
  independently browsing the current state of Ramp's dashboard, since the
  latter would not reflect the July 2026 snapshot the source text
  describes.
- **This is a short link-blog entry** (the entire post body, tags, and
  ordered list reproduced above constitute the complete extractable
  content — roughly 200 words plus the ten-item list). Per MINER.md's
  "5-15 claims per source" guidance, six claims were extracted; a seventh
  candidate claim (Willison's own aside that he "collected more historic
  numbers here," linking to the May 2026 post already in this corpus as
  `blog-simonwillison-anthropic-47b-revenue.md`) was folded into Claim 1's
  cross-reference rather than treated as a separate claim, since it
  contributes no new information beyond pointing to an already-mined
  source.
- **Confidence rated `anecdotal` overall**: the FT-sourced revenue figures
  (Claims 1-3) are attributed only to anonymous "people with knowledge of
  the matter," a weaker sourcing basis than the formal fundraising
  disclosures behind the corpus's existing $47B figure. The Ramp AI index
  figures (Claims 4-6) rest on a stronger evidentiary basis (aggregated
  first-party billing data across 70,000 companies) but the interpretive
  claim that price specifically explains the adoption gap (Claim 5) is
  Willison's own inference, not a controlled analysis, and the underlying
  data itself was not independently verified against Ramp's own dashboard
  by this Miner. The overall rating reflects the weakest link across all
  six claims, per this corpus's established calibration convention (see
  e.g. `blog-simonwillison-anthropic-47b-revenue.md`'s Extraction Notes,
  where one anecdotal claim pulled an otherwise-emerging note's overall
  rating down).
- **No contradiction issues filed.** The one near-miss (this source's
  slow-Opus-5-adoption data vs. Anthropic's own "start with the most
  intelligent model" default advice) was evaluated and judged to be a
  prescriptive-vs-descriptive distinction, not a material contradiction —
  see Cross-References → Contradicts above for the full reasoning.
