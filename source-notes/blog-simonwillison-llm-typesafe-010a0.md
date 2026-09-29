---
source_url: https://simonwillison.net/2026/Sep/22/llm-typesafe/
source_type: blog-post
title: "llm-typesafe 0.1a0"
author: Simon Willison
date_published: 2026-09-22
date_extracted: 2026-09-29
last_checked: 2026-09-29
status: current
confidence_overall: anecdotal
issue: "#3779"
---

# llm-typesafe 0.1a0

> Release note for an LLM CLI plugin exposing TypeSafe AI's Jev "decision model", which returns calibrated probabilities/scores for yes/no, multiple-choice and rating questions instead of free text — a concrete example of replacing a general chat-LLM call with a constrained classifier API.

## Source Context

- **Type**: blog-post (release announcement, ~150 words plus CLI examples)
- **Author credibility**: Simon Willison, creator of LLM and Datasette; prolific, hands-on tool builder. Here he is the plugin author, not an independent evaluator.
- **Scope**: Install/API-key setup and three usage modes of the plugin. Contains no benchmarks, latency/cost data, or discussion of Jev's internals. The README (github.com/simonw/llm-typesafe) adds the output shapes and option details used below.

## Extracted Claims

### Claim 1: Jev is exposed as a model that answers three typed question kinds (yes/no, choice, score) through the ordinary LLM CLI
- **Evidence**: Three worked CLI invocations with `-o answer_type` selecting the mode.
- **Confidence**: anecdotal
- **Quote**: "And now you can ask yes/no \"noul\" questions like this:"
- **Our assessment**: Shows a constrained-output model slotting into a general LLM harness with no special client. The typed answer is chosen via options rather than by prompting for JSON. Vendor-specific, alpha release.

### Claim 2: The yes/no mode returns a probability rather than a boolean
- **Evidence**: Example output `{"type": "noul", "noul": 0.99}`; README explains "Noul" as Bernoulli and that it "returns the probability of yes between 0 and 1".
- **Confidence**: anecdotal
- **Quote**: "{\"type\": \"noul\", \"noul\": 0.99}"
- **Our assessment**: Useful for thresholding in pipelines (route to human review below a cutoff). Whether the probability is actually calibrated is not shown in the source.

### Claim 3: Choice questions take per-category natural-language definitions and tie-break rules in the prompt
- **Evidence**: Example system prompt includes a tie-break ("If billing and technical issues both occur, choose billing.") plus a `criteria` JSON mapping category → description. README shows output with `confidence` and per-class `probabilities`.
- **Confidence**: anecdotal
- **Quote**: "Which team should handle this message? If billing and technical issues both occur, choose billing."
- **Our assessment**: The rubric is split into question (system prompt) and category definitions (options) — a clean pattern for ticket routing. Tie-break rule lives in prose, so it is only as reliable as the model's instruction-following.

### Claim 4: Scoring questions use a user-defined ordinal rubric
- **Evidence**: Example uses a three-level `criteria` list from "No reproduction instructions" to "Complete steps with expected and actual results"; README says the rating is a float on a scale the caller defines.
- **Confidence**: anecdotal
- **Quote**: "How reproducible is the problem described in this report?"
- **Our assessment**: Anchored rubric levels are the same technique used in LLM-as-judge prompts, here made a first-class parameter.

### Claim 5: Access is via a keyed hosted API with a waitlist
- **Evidence**: `llm keys set typesafe`; the post notes the waitlist "seems to move pretty fast".
- **Confidence**: anecdotal
- **Quote**: "get one here, the waitlist seems to move pretty fast"
- **Our assessment**: Adoption caveat: hosted, gated, alpha (0.1a0). Not something the guide can recommend as a default.

## Concrete Artifacts

```bash
# Source: simonwillison.net/2026/Sep/22/llm-typesafe/
llm install llm-typesafe
llm keys set typesafe

llm -m jev 'Please refund my last payment.' \
  -s 'Does this message explicitly request a refund?'
# {"type": "noul", "noul": 0.99}

cat message.txt | llm -m jev \
  -s 'Which team should handle this message? If billing and technical issues both occur, choose billing.' \
  -o answer_type choice \
  -o criteria '{
    "billing":"Charges, invoices, payments, or refunds",
    "technical":"Problems installing or using the product",
    "other":"Neither category fits"
  }'

cat report.txt | llm -m jev \
  -s 'How reproducible is the problem described in this report?' \
  -o answer_type score \
  -o criteria '[
    "No reproduction instructions",
    "Some instructions, but important steps are missing",
    "Complete steps with expected and actual results"
  ]'
```

README example choice output (github.com/simonw/llm-typesafe):

```json
{"type": "choice", "choice": "technical", "confidence": 0.97,
 "probabilities": {"technical": 0.98, "other": 0.02, "billing": 0.0}}
```

## Cross-References

- **Corroborates**: None found.
- **Contradicts**: None found.
- **Extends**: Other Willison LLM-plugin release notes in `source-notes/` (e.g. `blog-simonwillison-llm-anthropic-028.md`, `blog-simonwillison-llm-openrouter-07.md`) show the same plugin-per-provider pattern; this one is the first non-chat model type. The Prospector referenced a parent `blog-simonwillison-jev.md`, but that file does not exist in `source-notes/` at time of extraction.
- **Novel**: Dedicated "decision model" API returning probabilities for typed classification/scoring; not covered elsewhere in the corpus.

## Guide Impact

- **Chapter 04 / Chapter 06**: Candidate example (with heavy alpha/vendor caveat) of replacing a general LLM call with a constrained classifier that returns probabilities usable for thresholding. Do not add advice until there is independent evidence on accuracy, latency, or cost.

## Extraction Notes

- Source is very short; all claims are thin and product-descriptive. Fetched the post and the plugin README (one linked page). No independent evaluation exists in the source, hence `anecdotal`.
- No contradictions found, so no contradiction issue filed.
