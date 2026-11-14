---
source_url: https://simonwillison.net/2026/Nov/11/gemini-decisions-api/
source_type: blog-post
title: "Gemini Decisions API"
author: Simon Willison
date_published: 2026-11-11
date_extracted: 2026-11-14
last_checked: 2026-11-14
status: current
confidence_overall: emerging
issue: "#4712"
---

# Gemini Decisions API

> Google becomes the third vendor (after Jev and OpenAI) to ship a decision-model API with the same yes/no, choice and rubric-score question shapes; it is the only one of the three that is natively multimodal, and in one small test it returns non-saturated probabilities.

## Source Context

- **Type**: blog-post (short link-blog item; primary announcement at https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/ was also read for verification)
- **Author credibility**: Simon Willison, creator of Datasette and the `llm` CLI; hands-on experimenter. Here he reports one informal test, not a benchmark.
- **Scope**: Vendor comparison (pricing, modalities, question types) and one four-question video test. Does not cover accuracy, latency, calibration measurement, or bias.

## Extracted Claims

### Claim 1: Google has joined Jev and OpenAI as a third vendor in the "decision model" category, with an almost identical API shape
- **Evidence**: Willison's comparison of API docs; Google's announcement confirms three question types (noul, choice, score) on model `gemini-decision-1`.
- **Confidence**: emerging
- **Quote**: "Google join Jev and OpenAI in the decision model category with \"Gemini Decision 1\"."
- **Our assessment**: Three independent vendors converging on one API shape is the strongest signal yet that this is a durable category rather than one startup's product. Note that the Jev-originated term "Noul" is reused verbatim.

### Claim 2: The three question types (yes/no, choice, rubric-scoring) match Jev, including the term "Noul"
- **Evidence**: Willison's observation; Google's post lists noul (yes/no), choice (2 to 255 options, normalized probabilities) and score (ordered rubric, weighted score plus per-level probabilities).
- **Confidence**: emerging
- **Quote**: "it supports the same three types of questions (yes/no, choice, and rubric-scoring) and even reuses Jev's term \"Noul\" for a yes/no question."
- **Our assessment**: Corroborated by the primary source. Interoperable shapes make vendor swapping and multi-vendor evals plausible.

### Claim 3: Gemini Decision 1 is priced the same as the GPT-6 Luna decision model ($0.10/M input, output free); Jev is cheapest at $0.042/M
- **Evidence**: Willison's price comparison; Google's post states $0.10 per 1M input and $0 output, with the shared input billed once per request.
- **Confidence**: emerging (point-in-time vendor pricing)
- **Quote**: "It's priced the same as the GPT-6 Luna decision model: 10 cents per million input tokens, and output is free."
- **Our assessment**: Gemini price verified against Google's announcement; the OpenAI and Jev prices are Willison's (Jev figure matches the earlier Jev note, Claim 3). Google also says there are no thinking-token, transcription or OCR charges, which is a structural difference from LLM pricing.

### Claim 4: Gemini Decision 1 is the only one of the three that is fully multimodal (text, images, audio, video, PDFs)
- **Evidence**: Willison's comparison; Google lists the same modalities with up to 256K tokens of shared input and up to 1,000 questions per request.
- **Confidence**: emerging
- **Quote**: "Jev is text (and JSON) only. OpenAI can handle text and images. Gemini Decision 1 is fully multi-model: it covers text, images, audio, video, and PDFs."
- **Our assessment**: Verified for Gemini against Google's post. The Jev and OpenAI limitations are Willison's claim and were not checked against those vendors' docs. (Source says "multi-model"; presumably a typo for multimodal.)

### Claim 5: In a four-question video test, Gemini returns non-saturated probabilities where Jev and OpenAI return 1.0 or 0.0
- **Evidence**: A single run on one video (Willison's Yonkers stomping robot) with questions about dragon, robot, France and USA; results shown as JSON.
- **Confidence**: anecdotal
- **Quote**: "Jev and OpenAI both return 1.0 or 0.0 for yes/no questions, but Gemini insists on being a little less confident than that"
- **Our assessment**: Interesting but n=4 on one input, and the comparison to Jev/OpenAI on the same video is asserted, not shown. Less-extreme probabilities are not proof of better calibration; Hamel's note (Claim 7) warns calibration must be measured. Google claims lowest calibration error on its own benchmark suite, which is vendor-sourced and unverified.

### Claim 6 (from Google's primary post): Latency is nearly flat from 1 to 100 questions, and median end-to-end is 150-250 ms
- **Evidence**: Vendor-reported figures (cited for contexts up to 16K tokens); not independently verified.
- **Confidence**: anecdotal (vendor claim)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Corroborates the Jev claim that questions are evaluated in parallel (Jev note, Claim 4), though that note's version was hedged. Not mentioned by Willison; included because the triage asked for the primary announcement.

### Claim 7 (from Google's primary post): Intended uses are routing, tool selection, policy checks and safety layers, with confidence scores for fallback to a human or other model
- **Evidence**: Google lists Gemini Notebook using it as a model-tier router (up to 40% lower latency claimed) and Google Search using it as a safety layer for MCP tools.
- **Confidence**: anecdotal (first-party use cases)
- **Quote**: "scores your candidate options in a single forward pass."
- **Our assessment**: The quote is Google's description of the mechanism. The use cases align with the confidence-gate idea in the Thoughtworks note and the routing framing in the OpenAI DevDay note.

## Concrete Artifacts

Output from Willison's test (source: Gemini Decisions API post, Nov 11 2026), questions: dragon, robot, france, usa (yes_no):

```json
{
  "dragon": {"type": "yes_no", "probability": 0.04976021841520312},
  "robot": {"type": "yes_no", "probability": 0.9234055387792485},
  "france": {"type": "yes_no", "probability": 0.08329171353166241},
  "usa": {"type": "yes_no", "probability": 0.9230459995157706}
}
```

Vendor comparison table (compiled from the post and Google's announcement):

| | Jev | OpenAI (GPT-6 Luna decision model) | Gemini Decision 1 |
|---|---|---|---|
| Input $/M | 0.042 | 0.10 | 0.10 |
| Output | free | free | free |
| Modalities | text, JSON | text, images | text, images, audio, video, PDF |

Google's example uses the `google-genai` SDK (`v1beta`) and `client.decisions.create`.

## Cross-References

- **Corroborates:** `blog-simonwillison-jev-decision-models.md` (Claim 1: typed probabilistic decisions; Claim 3: $0.042/M input-only pricing; Claim 4: three question types, parallel evaluation). `blog-simonwillison-openai-devday-2026-live-blog.md` (Claim 7: the OpenAI Decisions API constrains a model to predefined options). `blog-thoughtworks-mugrage-jev-decision-models-what-to-know.md` (Claim 2: three modes with confidence; Claim 7: confidence gate for human-in-the-loop).
- **Contradicts:** None found. Hamel's note (Claim 7: probabilities are not automatically calibrated) is a caution rather than a contradiction of Google's calibration claim; Google's claim is unverified.
- **Extends:** `blog-hamel-decision-models-for-evals.md` (adds a third vendor to evaluate; Claim 6 cost-vs-F1 tradeoff now has a multimodal entrant). `blog-simonwillison-jev-decision-models.md` (adds multimodal inputs).
- **Novel:** Multimodal decision-model inputs (audio, video, PDF); non-saturated yes/no probabilities as an observed vendor difference; Google's first-party use cases and per-request billing of shared input.

## Guide Impact

- **Chapter 03**: If a section on decision models/classifier-style judges is added, cite this note as evidence that the category is multi-vendor with a shared API shape, and note that the probability-saturation difference means thresholds must be tuned per vendor (per Hamel Claims 1 and 7), not copied across.
- **Chapter 02**: Routing/guardrail components can now be sourced from three vendors; cite the Google use cases (model-tier router, MCP tool safety layer) as first-party examples, flagged as vendor claims.
- No change recommended to other chapters; evidence is a single informal test.

## Extraction Notes

- The post is a short link-blog item. Followed the "via" link to Google's announcement and used it to verify Gemini pricing, modalities and question types; the Google page was read via a summarizing fetch, so the one quote taken from it should be spot-checked.
- Jev and OpenAI pricing/modality claims are Willison's and were not verified against those vendors.
- Per triage guidance, the video test is treated as a single 4-question observation, not evidence of general calibration.
- Naming: the post says "GPT-6 Luna"; other notes in the corpus call it "GPT-5.6 Luna". Kept the source's wording; not reconciled.
