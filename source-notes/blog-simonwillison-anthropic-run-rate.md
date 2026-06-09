---
source_url: https://simonwillison.net/2026/May/31/anthropic-run-rate/
source_type: blog-post
title: "Quoting Karen Kwok for Reuters Breakingviews"
author: Karen Kwok (Reuters Breakingviews), quoted by Simon Willison
date_published: 2026-05-31
date_extracted: 2026-06-09
last_checked: 2026-06-09
status: current
confidence_overall: anecdotal
issue: "#1121"
---

# Quoting Karen Kwok for Reuters Breakingviews: Anthropic's Run-Rate Revenue Formula

> Simon Willison surfaces a Reuters Breakingviews quote revealing Anthropic's
> method for calculating "run-rate revenue": 28-day consumption × 13 plus monthly
> subscription × 12 — a formula whose annualization approach attracted the Reuters
> headline "Anthropic gives lesson in AI revenue hallucination."

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, May 31, 2026; a minimal quotation
  post with no Willison commentary beyond the sourcing attribution. The underlying
  Reuters Breakingviews article was published March 10, 2026 — Willison is surfacing
  it approximately 2.7 months after publication. The post is tagged `ai` and
  `anthropic`; Willison provides no editorial framing of his own. Page description
  on the post: "This is a quotation collected by Simon Willison.")
- **Author credibility**: Karen Kwok is a Reuters Breakingviews analyst. Reuters
  Breakingviews is a financial commentary service with professional editorial
  standards. The specific revenue claim is attributed to "a person familiar with
  the matter" — an anonymous secondary source, not an official Anthropic disclosure
  or SEC filing. Simon Willison is the creator of Django and a high-signal
  independent AI tooling commentator; in this post, he functions as a curator
  without analysis, matching the format of his other quotation posts
  (cf. `blog-simonwillison-spacex-s1-anthropic.md`,
  `blog-simonwillison-mitchell-hashimoto-tdm-dynamics.md`).
- **Scope**: A single block-quote defining Anthropic's "run-rate revenue" calculation
  methodology. Does NOT cover: absolute revenue figures, comparison to competitors,
  investor valuation, or any Anthropic financial metrics beyond this formula.
  Does NOT include Willison's editorial commentary or analysis. The Reuters article
  URL slug ("anthropic-gives-lesson-ai-revenue-hallucination") signals an editorially
  skeptical stance toward this methodology — but the Reuters article body was not
  accessible for extraction; only the Willison post and its block-quote were read.

## Extracted Claims

### Claim 1: Anthropic calculates "run-rate revenue" using a two-part formula: 28-day consumption revenue × 13, plus monthly subscription revenue × 12

- **Evidence**: Reuters Breakingviews, citing "a person familiar with the matter."
  Single anonymous source; not an official Anthropic statement or SEC filing. The
  formula is internally coherent — 28 × 13 = 364 ≈ one year; subscriptions × 12
  = standard annual conversion — which is consistent with deliberate design rather
  than error or misquote.
- **Confidence**: anecdotal (single anonymous source; no corroborating official
  disclosure; not refuted but not confirmed by Anthropic)
- **Quote**: "Anthropic defines 'run-rate revenue' in two parts. Use the last 28 days
  of sales ⁠from customers charged on a consumption basis and multiply it by 13. Then,
  multiply the monthly subscription take by 12, ​and add the two together."
  — Karen Kwok for Reuters Breakingviews, citing "a person familiar with the matter"
- **Our assessment**: The formula is plausible and internally consistent. The 28-day
  basis (approximately 13 per year) is a common choice in SaaS-like revenue reporting:
  it avoids calendar-month length variation (28–31 days) and gives a clean periodicity.
  Using the *most recent* 28-day period and multiplying by 13 — rather than averaging
  trailing 12 months — is a bullish approach for a rapidly growing company: it projects
  a run rate based on current momentum, which may significantly exceed the actual
  revenue achieved over the prior year. This is the standard critique of "run-rate
  revenue" as a metric: it assumes the most recent period is representative of all
  future periods, which overstates likely annual revenue for a business experiencing
  deceleration or seasonality.

### Claim 2: Anthropic's revenue model has two structurally distinct streams — consumption-based (API usage) and subscription-based (Claude.ai plans) — which are annualized differently

- **Evidence**: The formula itself explicitly distinguishes "customers charged on a
  consumption basis" (API users) from "the monthly subscription take" (Claude.ai
  subscription plan users). The different annualization factors (× 13 vs. × 12)
  reflect this structural difference and are internally consistent with each stream's
  billing periodicity.
- **Confidence**: emerging (the formula implies this structure; no explicit Anthropic
  disclosure confirms it, but it is consistent with Anthropic's known product lines:
  the Claude API charges by token consumption, while Claude.ai Pro/Team plans are
  monthly subscriptions)
- **Quote**: (no direct quote captures both streams as a pair; see the full formula
  quoted in Claim 1 above)
- **Our assessment**: The two-stream model is consistent with Anthropic's public
  product structure. API customers are billed per token (consumption), while
  consumer and team Claude.ai users pay fixed monthly subscriptions. The formula
  reveals that Anthropic internally tracks these streams separately — a meaningful
  signal about how the company monitors its own business health. For practitioners:
  the relative weight of consumption vs. subscription revenue affects how Anthropic
  will develop its products. An API-heavy revenue mix incentivizes continued
  investment in API capabilities, pricing, and reliability; a subscription-heavy mix
  incentivizes investment in consumer and team UI experience. Understanding which
  stream dominates helps practitioners anticipate which product investments Anthropic
  will prioritize.

### Claim 3: The Reuters Breakingviews article headline ("Anthropic gives lesson in AI revenue hallucination") signals editorial skepticism of the run-rate methodology

- **Evidence**: The Reuters article URL contains the slug
  `anthropic-gives-lesson-ai-revenue-hallucination`, which is the article title.
  "Hallucination" is deliberately chosen to invoke the AI terminology for producing
  plausible-sounding but false output — applied here to Anthropic's revenue figures.
  Reuters Breakingviews typically reserves such pointed headline framing for
  critiques of financial reporting practices.
- **Confidence**: anecdotal (only the title/slug is available; the article body
  was not read — claims about the article's substance are based solely on its title)
- **Quote**: (no direct quote; title inferred from URL slug:
  `anthropic-gives-lesson-ai-revenue-hallucination`)
- **Our assessment**: The title framing implies the Breakingviews analysis argues
  that Anthropic's run-rate revenue methodology inflates the reported figure. The
  "hallucination" metaphor is a strong editorial signal: it frames the revenue
  number as plausible-but-wrong in a way calculated to be legible to AI-literate
  financial readers. The technical critique implicit in the title is consistent with
  the formula's known property: using the most recent 28-day period × 13 rather
  than trailing twelve months' average is standard "current momentum" framing that
  can significantly overstate annual revenue for any fast-growing company. We cannot
  assess the full strength of the critique without reading the article, but the
  title alone constitutes editorial signal. Practitioners evaluating Anthropic
  vendor stability should understand that third-party "run-rate revenue" figures may
  use this formula, which could overstate annual revenue compared to TTM actuals.

### Claim 4: Willison surfaces the Reuters quote without personal editorial commentary — the post is a signal-amplification act, not an analysis

- **Evidence**: The Willison post structure: a single block-quote, a source
  attribution, and no additional Willison commentary. The page self-description:
  "This is a quotation collected by Simon Willison."
- **Confidence**: settled (directly observable from the post structure)
- **Quote**: (no direct quote captures this meta-observation; see paraphrase in
  Our assessment)
- **Our assessment**: Unlike Willison's substantial commentary posts (e.g.,
  `blog-simonwillison-xai-anthropic-datacenter.md`), this post is curation-only.
  Willison's decision to tag and post it is itself a weak relevance signal — he
  found it worth sharing — but he provides no interpretive frame. The evidentiary
  weight rests entirely on the Reuters Breakingviews article, not on Willison.
  The 2.7-month gap between the Reuters publication (March 10, 2026) and Willison's
  post (May 31, 2026) suggests he may have surfaced it in connection with other
  late-May Anthropic financial coverage (the SpaceX S-1 was filed May 20, 2026).

## Concrete Artifacts

### The Willison Block-Quote (verbatim from https://simonwillison.net/2026/May/31/anthropic-run-rate/)

```
Posted: 31st May 2026 at 1:48 am
Tags: ai (2,058), anthropic (290)
Source: Karen Kwok for Reuters Breakingviews,
        "Anthropic gives lesson in AI revenue hallucination" (2026-03-10),
        citing "a person familiar with the matter"
Reuters URL: https://www.reuters.com/commentary/breakingviews/anthropic-gives-lesson-ai-revenue-hallucination-2026-03-10/

[Block-quote, verbatim:]

"Anthropic defines 'run-rate revenue' in two parts. Use the last 28 days of sales ⁠from
customers charged on a consumption basis and multiply it by 13. Then, multiply the monthly
subscription take by 12, ​and add the two together."
```

### Anthropic Run-Rate Revenue Formula (derived from the block-quote)

```
Source: Karen Kwok for Reuters Breakingviews (2026-03-10), via Willison (2026-05-31)

Run-rate revenue = (28-day consumption revenue × 13) + (monthly subscription revenue × 12)

Where:
  28-day consumption revenue = API/token revenue from last 28 days
  × 13 ≈ annualization factor (28 × 13 = 364 days ≈ 1 year)

  monthly subscription revenue = Claude.ai subscription take (most recent month)
  × 12 = standard annual conversion

Two revenue streams:
  1. Consumption-based (API customers):  rolling 28-day × 13
  2. Subscription-based (Claude.ai plans): most recent month × 12

Key property: uses MOST RECENT period (not trailing 12-month average)
— forward-looking momentum run rate, not historical average.

Critique implicit in Reuters title: most-recent-period × 13 can significantly
overstate annual revenue for a rapidly growing company where recent periods
are unrepresentative of the full prior year.
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-spacex-s1-anthropic.md` Claim 2: The SpaceX S-1 discloses
    Anthropic pays $1.25 billion per month for compute. Understanding that Anthropic's
    compute expenses run at this scale gives context for why run-rate revenue
    methodology matters — the company needs to demonstrate revenue momentum
    commensurate with infrastructure costs. A $1.25B/month compute bill requires
    a commensurate level of monthly API revenue for the business model to be viable,
    and how that revenue is measured and reported matters significantly.

- **Extends**:
  - `blog-simonwillison-xai-anthropic-datacenter.md` Claim 1 ("I get that Anthropic
    are severely compute-constrained"): This source adds the revenue side of the
    financial equation. The xAI note covers Anthropic's compute cost exposure;
    this note covers how Anthropic reports its revenue. Together they frame the
    financial position: high and growing compute costs ($1.25B/month per the
    SpaceX S-1), measured against a run-rate revenue figure that uses a
    forward-looking methodology which may overstate annual revenue. The gap between
    compute costs and revenue run rate is a practitioner-relevant indicator of
    vendor financial sustainability.

- **Contradicts**: None filed. No existing corpus note makes claims about Anthropic's
  revenue methodology that this source contradicts.

- **Novel**:
  - **The run-rate revenue formula itself**: No prior corpus source documents how
    Anthropic calculates or reports its revenue metric. The specific formula
    (28-day consumption × 13 + monthly subscription × 12) is new to the corpus and
    is the primary contribution of this source.
  - **Two-stream revenue structure (consumption vs. subscription)**: No prior corpus
    source explicitly delineates Anthropic's revenue into API consumption and
    subscription streams as structurally distinct categories with different
    annualization methodologies.
  - **Editorial skepticism of Anthropic's revenue reporting**: The Reuters
    "hallucination" headline framing is the first editorial critique of an
    Anthropic financial reporting methodology in the corpus.

## Guide Impact

- **Chapter 01 (Market Context — Vendor Financial Stability)**: Add a note that
  reported "run-rate revenue" figures for Anthropic use a forward-looking methodology
  (most recent 28-day consumption × 13) that may overstate projected annual revenue
  compared to TTM actuals, especially for a fast-growing company. Practitioners
  evaluating vendor stability should understand this methodology when interpreting
  AI vendor financial coverage.

- **Chapter 03 (Financial Infrastructure — Cost-Revenue Context)**: Combined with
  the SpaceX S-1 note ($1.25B/month compute cost), the run-rate formula provides
  context for practitioners reasoning about Anthropic's financial sustainability:
  the company measures its own momentum using a bullish forward-looking metric,
  which is appropriate for investor communications during growth phases but may
  obscure sustainability questions if consumption growth decelerates. Practitioners
  building AI-native systems should understand that their vendor's reported
  financial health is measured using vendor-defined metrics that may differ from
  GAAP accounting.

## Extraction Notes

- **Minimal source**: The Willison post is a single block-quote with a source
  attribution and no other text beyond standard page furniture. The full extractable
  content is in the one quoted passage. No sub-pages followed; none existed.
- **Reuters article not read**: Only the Willison block-quote was accessible.
  The Reuters Breakingviews article itself
  (https://www.reuters.com/commentary/breakingviews/anthropic-gives-lesson-ai-revenue-hallucination-2026-03-10/)
  was not fetched — Reuters Breakingviews is a subscription service and the article
  was not available via WebFetch. The article title ("Anthropic gives lesson in AI
  revenue hallucination") is inferred from the URL slug only and is treated
  cautiously in the extraction. Claim 3 is explicitly flagged as title-only evidence.
- **Anonymous source**: The formula's source is "a person familiar with the matter"
  — standard Reuters attribution for financially material but unconfirmed information.
  No Anthropic confirmation or denial is available in this source.
- **Timing gap**: The Reuters article was published March 10, 2026; Willison's post
  is May 31, 2026. The 2.7-month delay may reflect Willison surfacing the article
  in connection with the late-May Anthropic financial coverage environment
  (SpaceX S-1 filed May 20, 2026; other Anthropic revenue commentary in the period).
- **Confidence overall: anecdotal**: All substantive claims derive from a single
  anonymous secondary source via financial commentary. The formula is internally
  consistent and plausible but is not confirmed by Anthropic or any primary filing.
