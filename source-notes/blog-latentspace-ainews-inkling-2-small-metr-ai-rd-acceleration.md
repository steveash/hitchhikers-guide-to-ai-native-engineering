---
source_url: https://latent.space/p/ainews-inkling-2-small-17a-594b-trained-in-68-hours-on-12t-tokens-beating-muse-spark/
source_type: blog-post
title: "[AINews] Inkling 2 Small: 17A-594B trained in 68 hours on 12T tokens, beating Muse Spark"
author: swyx / smol.ai (AINews aggregation, published under Latent Space)
date_published: 2026-11-06
date_extracted: 2026-11-19
last_checked: 2026-11-19
status: current
confidence_overall: emerging
issue: "#4836"
---

# [AINews] Inkling 2 Small (METR AI-R&D acceleration item)

> A daily AINews roundup whose one substantive item is METR's external review of Anthropic's August 2026 Risk Report, which estimates a ~1.9x acceleration in Anthropic's AECI capability trend; METR's primary post differs in detail from the roundup's secondhand summary.

## Source Context

- **Type**: blog-post (aggregation digest of tweets and Reddit threads)
- **Author credibility**: swyx / AINews is a high-volume curator; items are secondhand links to primary tweets. Per triage, only the METR item was extraction-worthy; Inkling 2 Small training/benchmark claims are vendor-side and deliberately not mined.
- **Scope**: Mined the "METR: Is AI Accelerating AI R&D?" section; verified against METR's primary post (https://metr.org/blog/2026-11-05-rd-section-anthropic-risk-report-august-2026-review/). Skipped model specs, benchmark tables, open-weights recap.

## Extracted Claims

### Claim 1: METR reports Anthropic-model AECI scores have grown ~1.9x faster since Oct 2025
- **Evidence**: METR tweet relayed by AINews; METR's primary review says Anthropic added benchmarks, giving an acceleration estimate of 1.9x on the same models (vs ~1.5x on the Risk Report's original data).
- **Confidence**: emerging
- **Quote**: "Since October 2025, AECI scores for Anthropic models have grown 1.9x faster than before, with a 95% interval of 1.5–2.8x" (AINews, attributed to METR tweet)
- **Our assessment**: Real, but note the discrepancy: the primary review we fetched gives "1.9x" and "1.5x" for different data sets and reports "between 1.3 and 2.8" for leading indicators; it does not present a 95% interval of 1.5–2.8x. The roundup's interval is likely a conflation, so cite the primary post, not the digest, for numbers.

### Claim 2: METR cannot distinguish a one-time capability jump from continued acceleration
- **Evidence**: METR's primary review (caveats section).
- **Confidence**: emerging
- **Quote**: "we cannot confidently distinguish between a one-time jump in capabilities and a continued acceleration" (METR primary post)
- **Our assessment**: Key caveat; any guide use must carry it. The roundup states the weaker "METR says the estimate depends on analysis choices."

### Claim 3: METR thinks the public Risk Report understates acceleration
- **Evidence**: METR's primary review conclusions.
- **Confidence**: anecdotal (one reviewer's judgment, partially redacted)
- **Quote**: "the public report overall understates the level of acceleration that was occurring."
- **Our assessment**: Externally sourced, and notable as a rare third-party check on a lab's self-report; still unreplicable by us since underlying data is internal.

### Claim 4: Anthropic's Sam McCandlish endorses "AI is speeding up research, but cannot yet make the most important training contributions alone"
- **Evidence**: Tweet relayed by AINews (secondhand; not fetched directly).
- **Confidence**: anecdotal
- **Quote**: "AI is speeding up research, but it cannot yet make the most important training contributions alone." (AINews, attributed to McCandlish)
- **Our assessment**: Vendor-side framing; consistent with the OpenAI view that agents still need human steering.

### Claim 5: METR's report redactions are disputed
- **Evidence**: AINews relays Barnes (METR): "the report takes no position on whether the redactions were justified"; METR's primary post says redacted material important to conclusions is described.
- **Confidence**: anecdotal
- **Quote**: "the report takes no position on whether the redactions were justified" (AINews, attributed to Beth Barnes)
- **Our assessment**: Limits how much weight the figures carry.

### Claim 6: Commenters on Claude Code context management prefer manual handoff over autocompact
- **Evidence**: Reddit r/ClaudeCode thread excerpts relayed by AINews; author not shown.
- **Confidence**: anecdotal
- **Quote**: "Handoff > autocompact"
- **Our assessment**: Weak, one-line anecdote; no mechanism or data. Only mildly relevant to context-management guidance.

### Claim 7: CMU ServerBench: coding agents built complete serving stacks, 22 of 33 runs verified
- **Evidence**: Secondhand tweet summary; not verified against the paper.
- **Confidence**: anecdotal
- **Quote**: "22 of 33 runs produced verified systems and 13 beat the strongest baseline."
- **Our assessment**: Interesting but unverified; would need the primary paper before use.

## Concrete Artifacts

```
Metrics as relayed (METR primary review, 2026-11-05):
- AECI acceleration: ~1.5x (Risk Report data) -> 1.9x (added benchmarks, same models)
- Leading-indicator rates: "between 1.3 and 2.8, depending on the definition and time period"
- AINews-only claim (not in METR primary): 95% interval 1.5–2.8x
```

## Cross-References

- **Corroborates**: `blog-simonwillison-research-acceleration-view-inside-openai.md` (Claims 4, 5, 9) — an independent lab-side picture of AI accelerating research with human steering still needed.
- **Contradicts**: none filed. Minor internal discrepancy between the digest's 95% interval and METR's primary post (see Claim 1).
- **Extends**: `blog-anthropic-ai-accelerated-offense.md` (same lab, capability-acceleration theme); prior AINews notes such as `blog-latentspace-ainews-muse-spark-13-frontier-lab.md`.
- **Novel**: METR's external review of Anthropic's Risk Report and the AECI acceleration estimate; not previously in the corpus.

## Guide Impact

- **Chapter 00**: If the guide discusses AI-accelerated AI R&D, add METR's review as an externally sourced, caveated data point (1.9x, cannot separate jump from acceleration), cited to the METR primary post rather than this digest.
- No change to Ch01–Ch06.

## Extraction Notes

- Read the digest's METR section via fetch and the primary METR post; did not read the full 32-minute digest line by line, by triage direction. Tweets were not fetched directly (X); tweet quotes are as relayed by AINews.
- Priority low; recommend not citing the digest's 95% interval.
