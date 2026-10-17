---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/evaluating-decision-models-for-document-categorization
source_type: blog-post
title: "Evaluating decision models for document categorization"
author: Pallavi Sinha
date_published: 2026-10-15
date_extracted: 2026-10-17
last_checked: 2026-10-17
status: current
confidence_overall: anecdotal
issue: "#4183"
---

# Evaluating decision models for document categorization

> A Thoughtworks Research practitioner runs the open-weights decision model Laya on document classification and reports the first small measured comparison against Claude Sonnet, plus concrete numbers on multi-question latency, long-document aggregation and sentence-based chunking.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, Generative AI)
- **Author credibility**: Pallavi Sinha, Thoughtworks Research team. Hands-on experiment, not a vendor post. The author states the work was "part of a two-day time-boxed exploration with a concrete use case."
- **Scope**: Decision-model question types, Laya setup (v0.3.22 via pip), a domain-choice experiment on ~5,000-word generated documents, latency for multi-question calls, long-document aggregation rules, sentence-based chunking, and a 6-document benchmark against Claude Sonnet. Does not cover cost, multiple runs, error bars, sample size for the chunking result, or Jev (the paid model) in measurements.

## Extracted Claims

### Claim 1: For fixed-label classification, an LLM's free-text output adds parsing, validation and token overhead that a constrained decision model avoids
- **Evidence**: Reasoning by the author; no measurement of parsing failures or token counts.
- **Confidence**: emerging
- **Quote**: "An LLM can do this, but it generates an answer as text. You then need to extract and validate the label, handle malformed responses and deal with answers outside your allowed set."
- **Our assessment**: Sound framing, but unmeasured here. Structured-output / constrained-decoding features on LLM APIs weaken the "malformed response" part of the argument, and the post does not compare against them.

### Claim 2: A decision model supports three question types (choice, score, yes/no), and every answer carries probabilities
- **Evidence**: Description of Laya's API with a JSON request and response example.
- **Confidence**: settled (as a description of the tool)
- **Quote**: "Each answer includes probabilities, which makes uncertainty explicit instead of forcing a guess."
- **Our assessment**: Consistent with the Jev descriptions in the corpus; Laya is an open-weights implementation of the same shape.

### Claim 3: Out-of-scope documents fall below a confidence threshold and become "uncategorized" rather than being forced into a label
- **Evidence**: Author added cooking recipes and a poem to the four-domain set. No counts or threshold value given for this test.
- **Confidence**: anecdotal
- **Quote**: "These fell below a predefined confidence threshold and were classified as uncategorized rather than being forced into one of the available domains."
- **Our assessment**: Useful pattern (threshold routing to an escape bucket), but only two kinds of out-of-domain input are reported. The benchmark in Claim 8 shows the flip side: a wrong answer at 0.106 is caught only if the threshold is applied.

### Claim 4: The probability gives a basis for deciding when to accept a classification and when to escalate it
- **Evidence**: Legal-document example returning 0.826 for "legal" with the remaining mass on finance, technology and medical.
- **Confidence**: emerging
- **Quote**: "the probability provides a basis for deciding when to accept a classification and when to escalate it."
- **Our assessment**: Matches the confidence-gate idea in other notes. No calibration data is presented, so whether 0.55 or 0.826 are well-calibrated is untested.

### Claim 5: Classification quality depends heavily on how criteria are written, because the model scores each option against its description
- **Evidence**: Author's experience; criteria example for four domains is in Concrete Artifacts. No ablation of criteria wording.
- **Confidence**: anecdotal
- **Quote**: "The quality of these decisions depends heavily on how the instructions and criteria are written."
- **Our assessment**: Plausible and consistent with prompt-sensitivity in LLMs. The post gives the lever but no evidence of effect size.

### Claim 6: Asking several questions in one call costs roughly 3-4x the latency of a single question
- **Evidence**: Table for three documents, domain-only vs four dimensions (domain, type, sensitivity, complexity): Legal 856 ms vs 3,461 ms (~4.0x), Medical 897 ms vs 3,854 ms (~4.3x), Finance 1,219 ms vs 4,126 ms (~3.4x).
- **Confidence**: anecdotal (three documents, single runs apparently, local hardware unspecified)
- **Quote**: "Classification of documents over four dimensions, domain, type, sensitivity and complexity took roughly 3–4x longer than domain categorizing alone."
- **Our assessment**: Notable because it contradicts the intuition that decision-model questions are cheap and parallel (Simon Willison's note describes questions "evaluated in parallel" on Jev's API). Here, on a local Laya run, cost scales near-linearly with question count. This is an implementation/hardware difference, not necessarily a contradiction with the hosted Jev API, so not filed as one.

### Claim 7: For long documents, choice/score questions take the most confident section, while yes/no takes any sufficiently confident "yes", so document-wide checks must be phrased as violation searches
- **Evidence**: Description of Laya's section-scoring-then-aggregate behavior; reasoning example. No measured failure.
- **Confidence**: emerging
- **Quote**: "Reframing it as "Does this contain anything that violates policy X?" works better because a single violation is sufficient to answer yes."
- **Our assessment**: The most transferable point. Aggregation semantics determine correct question phrasing; the same trap (max-aggregation over chunks) applies to any chunked verification pipeline. Unmeasured, but follows from the stated rule.

### Claim 8: Sentence-based chunking in place of token-based chunking left classifications unchanged while cutting sections and latency by about 40%
- **Evidence**: Table: Laya's own chunking 235 sections / ~5 seconds; sentence-based 138 sections / ~3 seconds. No document count, document length or accuracy table given.
- **Confidence**: anecdotal
- **Quote**: "The classifications stayed the same, while the number of sections and latency both dropped by about 40%."
- **Our assessment**: Interesting and cheap to replicate, but the sample size is not stated and Laya's 512-token window makes chunking unusually consequential. Do not generalize to LLM RAG chunking without testing.

### Claim 9: On six technical documents, Laya (0.55 threshold) and Claude Sonnet each got 5 of 6 right, with different misses
- **Evidence**: Per-document table. Laya: 0.553, 0.664, 0.586, 0.600 correct; Doc 5 (insurance) wrong at 0.106; Doc 6 (retail) correct at 0.615. Sonnet wrong on Doc 6 (retail). Mean latency 1.72 s (Laya) vs 1.45 s (Sonnet).
- **Confidence**: anecdotal
- **Quote**: "Both models got 5 of 6 right. Mean latency was 1.72 s for Laya and 1.45 s for Claude Sonnet."
- **Our assessment**: n=6, single run, no error bars, prompt given to Sonnet not disclosed. Note that Doc 1 passed at 0.553, just above the 0.55 threshold, so the threshold choice is tight. "Comparable accuracy" is a fair reading only as a smoke test. The latency result also shows the local decision model was not faster than a hosted LLM here.

### Claim 10: The distinguishing advantage over the LLM is the explicit uncertainty signal, not accuracy
- **Evidence**: Same benchmark; Laya returned a distribution while the Sonnet comparison is a bare label.
- **Confidence**: emerging
- **Quote**: "Laya also returned a probability distribution over the allowed choices, giving an explicit uncertainty signal that can be used for thresholding or human review."
- **Our assessment**: Agrees with the confidence-gate theme in the corpus. Worth noting that the one Laya miss had very low confidence (0.106), the case where the signal would route to review, but the post does not test whether low confidence reliably predicts errors across more documents.

### Claim 11: The post's own stated caveat: this is an early signal from a small test
- **Evidence**: Author's framing.
- **Confidence**: settled (as a statement of limits)
- **Quote**: "This is an early signal, but it suggests that a decision model can be competitive with a generative LLM for this type of constrained classification task."
- **Our assessment**: We agree with the hedged conclusion and no stronger.

## Concrete Artifacts

Laya choice-question request (Sinha, "Exploring Laya"):

```json
{
  "domain": {
    "type": "choice",
    "instructions": "What subject-matter domain does the document belong to?",
    "criteria": {
      "legal": "contracts, litigation, statutes, court rulings, legal obligations",
      "medical": "diagnoses, symptoms, treatments, clinical or health guidance",
      "finance": "investments, markets, accounting, loans, currency, budgets",
      "technology": "software, hardware, programming, IT infrastructure, computing"
    }
  }
}
```

Response for a legal document (same source):

```json
{
  "answers": {
    "domain": {
      "type": "choice",
      "choice": "legal",
      "probabilities": {
        "legal": 0.826,
        "finance": 0.122,
        "technology": 0.032,
        "medical": 0.021
      },
      "answer_confidence": 0.826
    }
  }
}
```

Latency, one vs four questions (Sinha):

```
Document   Domain only   Four dimensions   Increase
Legal      856 ms        3,461 ms          ~4.0x
Medical    897 ms        3,854 ms          ~4.3x
Finance    1,219 ms      4,126 ms          ~3.4x
```

Chunking comparison (Sinha):

```
Approach                  Sections   Latency
Laya's own chunking       235        ~5 seconds
Sentence-based chunking   138        ~3 seconds
```

Benchmark vs Claude Sonnet, six documents, Laya threshold 0.55 (Sinha):

```
Doc   Label                          Laya            Claude Sonnet
1     transportation_and_logistics   correct (0.553) correct
2     pharma_and_healthcare          correct (0.664) correct
3     financial_services             correct (0.586) correct
4     retail                         correct (0.600) correct
5     insurance                      wrong   (0.106) correct
6     retail                         correct (0.615) wrong
Mean latency: Laya 1.72 s, Claude Sonnet 1.45 s
```

Tooling noted: Laya (Convai Innovations) is open weights, locally runnable, 512-token context window (English); Jev (TypeSafe AI) is a paid managed API with up to 64,000 tokens; experiment used laya v0.3.22 from pip with a Hugging Face checkpoint.

## Cross-References

- **Corroborates**: [blog-thoughtworks-mugrage-jev-decision-models-what-to-know](blog-thoughtworks-mugrage-jev-decision-models-what-to-know.md) Claim 7 (confidence scores make decision models an effective confidence gate easing human-in-the-loop); [blog-thoughtworks-penumarthi-jev-rag-pipelines](blog-thoughtworks-penumarthi-jev-rag-pipelines.md) Claim 7 (probability bands and escalation below a threshold) and Claim 3 (ingestion classification as choice questions); [blog-latentspace-jev-system-one-for-prod](blog-latentspace-jev-system-one-for-prod.md) Claim 9 (calibrated confidence for thresholds and escalation).
- **Contradicts**: None filed. Claim 6 (near-linear latency growth with question count on local Laya) sits in tension with the "evaluated in parallel" description in [blog-simonwillison-jev-decision-models](blog-simonwillison-jev-decision-models.md) Claim 4, but the systems differ (local open-weights vs hosted API), so we treat it as a conditioning variable rather than a contradiction.
- **Extends**: [blog-simonwillison-jev-decision-models](blog-simonwillison-jev-decision-models.md) Claim 10 (evals matter for decision models) by supplying a small example eval; [blog-latentspace-jev-system-one-for-prod](blog-latentspace-jev-system-one-for-prod.md) Claim 6 (decompose into small measurable questions) with the cost of doing so in latency; [blog-thoughtworks-penumarthi-jev-rag-pipelines](blog-thoughtworks-penumarthi-jev-rag-pipelines.md) Claim 9 (verify calibration on your own data) by showing a tight threshold (0.553 against 0.55).
- **Novel**: First measured decision-model vs LLM accuracy and latency comparison in the corpus (though n=6); max-aggregation semantics for chunked documents and the "contains a violation" question framing; sentence-based vs token-based chunking numbers; multi-question latency multiplier on Laya (an open-weights Jev analogue).

## Guide Impact

- **Chapter 03 (verification)**: Where the guide discusses confidence thresholds and human escalation for classification, add this as a small worked example (5/6 vs 5/6, miss at 0.106 confidence), explicitly labelled anecdotal (n=6). Add the rule that document-wide yes/no checks should be phrased as "does this contain a violation of X", citing Claim 7, as a general chunked-verification pitfall.
- **Chapter 04 (context engineering)**: Where chunking is discussed, note that boundary-aware (sentence) chunking cut section count about 40% with unchanged labels in one small-window-model experiment (Claim 8); caveat that this is not tested on large-context LLMs.
- **Chapter 02 (harness)**: At most a pointer that a constrained classifier step with a threshold can sit inside a pipeline; the evidence here is too thin to change recommendations, and the existing Jev notes already carry this theme.

## Extraction Notes

- Read the full article (fetched raw HTML and stripped to text); quotes were copied from that text. The page has no sub-pages beyond three "Related content" links, which correspond to existing notes (Mugrage, Penumarthi) or are off-topic (agentic payments).
- Claim numbers cited in Cross-References were checked against the headings of the cited notes.
- Limits to carry forward: n=6 documents, single runs, no error bars, no sample size for the chunking result, one open-weights model with a 512-token window, two-day time-boxed exploration, Sonnet prompt and version not disclosed.
