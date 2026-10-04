---
source_url: https://simonwillison.net/2026/Sep/27/hn-49871741/
source_type: blog-post
title: "S3 Is the Future, S3 Is the Past (Hacker News comment)"
author: Simon Willison
date_published: 2026-09-27
date_extracted: 2026-10-04
last_checked: 2026-10-04
status: current
confidence_overall: anecdotal
issue: "#3889"
---

# S3 Is the Future, S3 Is the Past (Hacker News comment)

> A Simon Willison "beat" reposting his HN comment: a seven-row table of AWS S3 standard storage price history showing no price cut since December 2016 — a thin but concrete data point that cloud storage unit costs no longer fall on their own.

## Source Context

- **Type**: blog-post (a "beat" — a short repost of a Hacker News comment on the thread "S3 Is the Future, S3 Is the Past"; ~50 words of prose plus a table)
- **Author credibility**: Simon Willison is creator of Datasette and the `llm` CLI and a widely cited LLM-tooling commentator. He has no special AWS authority here; the table is a factual price history he reproduces, not first-party measurement.
- **Scope**: Covers only S3 per-GB-month list pricing over time. Contains no analysis, no AI-specific content, no implications. It does not discuss egress, request pricing, tiers, or competitors.

## Extracted Claims

### Claim 1: S3 standard storage has had no list-price drop in a decade
- **Evidence**: A table of seven dated price points (2006–2016) and the statement that the price is unchanged today. No link to AWS pricing archives in the post itself.
- **Confidence**: emerging (concrete and checkable, but unsourced in the post)
- **Quote**: "One thing I find notable about S3 today is that, while it used to drop in price reasonably often, there hasn't been a price drop in a full decade"
- **Our assessment**: Plausible and easy to verify against the AWS price-history archive. Note "a full decade" is Willison's rounding of Dec 2016 → Sep 2026. Applies to the headline S3 Standard rate only.

### Claim 2: S3 prices fell steeply from 2006 to 2016, then flattened
- **Evidence**: The table: $0.150 (2006-03-14) → $0.140 → $0.125 → $0.095 → $0.085 → $0.030 (2014-04-01) → $0.023 (2016-12-01). That is roughly an 85% decline, with the biggest single cut (0.085 → 0.030) in April 2014.
- **Confidence**: emerging
- **Quote**: "2014-04-01  $0.030/GB-month"
- **Our assessment**: The decline percentage is our arithmetic, not the source's. The shape (steep then flat) matters for cost models that assume continued Moore's-law-style storage deflation.

### Claim 3: The current price is still $0.023/GB-month
- **Evidence**: Assertion by the author as of 2026-09-27.
- **Confidence**: emerging
- **Quote**: "Today it's still $0.023/GB-month."
- **Our assessment**: Time-sensitive; should be rechecked against AWS pricing before the guide cites it.

## Concrete Artifacts

```
S3 price history (Simon Willison, simonwillison.net/2026/Sep/27/hn-49871741/)
2006-03-14  $0.150/GB-month
2010-11-01  $0.140/GB-month
2012-02-01  $0.125/GB-month
2012-12-01  $0.095/GB-month
2014-02-01  $0.085/GB-month
2014-04-01  $0.030/GB-month
2016-12-01  $0.023/GB-month
```

## Cross-References

- **Corroborates**: None directly.
- **Contradicts**: None found.
- **Extends**: Loosely adjacent to `blog-simonwillison-agentsview-custom-model-price.md` (Claim 1 there treats cost observability for agent usage as a practitioner concern); this note concerns infrastructure unit cost, not token cost.
- **Novel**: No existing note covers cloud storage pricing. Nothing here is AI-native-specific.

## Guide Impact

- **Chapter 05 (Economics)**: At most a one-line footnote that storage unit prices should be modeled as flat, not deflating, when budgeting artifact/transcript/trace retention for agent systems. Not enough to justify a standalone section; the post gives no AI-specific evidence.

## Extraction Notes

- Fetched the page and verified the quote and table against the raw HTML. No sub-pages were followed except noting the post links to the HN thread (not read; the post is a repost of one comment).
- Source is very thin; the Prospector rated it low novelty/low priority. Confidence is capped at anecdotal overall. No contradictions filed.
