---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/how-jev-can-help-improve-the-efficiency-of-rag-pipelines
source_type: blog-post
title: "How Jev can help improve the efficiency of RAG pipelines"
author: Jayanth Penumarthi
date_published: 2026-10-06
date_extracted: 2026-10-07
last_checked: 2026-10-07
status: current
confidence_overall: anecdotal
issue: "#3957"
---

# How Jev can help improve the efficiency of RAG pipelines

> A Thoughtworks practitioner maps four decision points in a RAG pipeline onto Jev's three answer types and proposes a 0.9/0.6 confidence-band cascade, but reports no metrics.

## Source Context

- **Type**: blog-post (Thoughtworks Insights)
- **Author credibility**: Jayanth Penumarthi, Thoughtworks; says they traced a user question through a RAG platform being built for a client. Thoughtworks carries a disclaimer that opinions are the author's own.
- **Scope**: Where model calls accumulate in RAG (ingestion, pre-retrieval, post-retrieval, post-generation), how Jev's choice/score/Noul answers fit each, a threshold framework, and cautions. No benchmarks, latency numbers, cost figures, or code. The author says they "implemented a simple framework" but does not report results from it.

## Extracted Claims

### Claim 1: Most model calls in a RAG pipeline are decisions, not text generation
- **Evidence**: Author's own trace of one user question through a client RAG platform; no counts given beyond "a huge number".
- **Confidence**: anecdotal
- **Quote**: "In fact, only one call wrote a sentence a person would actually read; the rest were decisions."
- **Our assessment**: Plausible and a useful framing for auditing any pipeline. It is one system, uncounted, so treat it as an audit prompt rather than a measured finding.

### Claim 2: Decisions accumulate at four RAG stages: ingestion, pre-retrieval, post-retrieval, post-generation
- **Evidence**: Enumerated by the author from the traced platform.
- **Confidence**: anecdotal
- **Quote**: "Only one step in that list needs to generate language: writing the final answer."
- **Our assessment**: A clean taxonomy (document classification/sensitivity, routing/rewrite/no-retrieval, rerank/sufficiency, claim grounding). Useful as a checklist; the stages themselves are not novel to RAG practice.

### Claim 3: Ingestion classification and sensitivity checks should be choice and yes/no questions written into metadata
- **Evidence**: Design recommendation; rationale is volume ("thousands a day").
- **Confidence**: anecdotal
- **Quote**: "The answers will go straight into the document's metadata, which means your retrieval filters can use them later."
- **Our assessment**: Sensible, since constrained labels avoid cleanup. The benefit is asserted, not measured.

### Claim 4: Pre-retrieval routing, including a "no retrieval needed" option, saves work when confidence is high
- **Evidence**: Design recommendation; routing options are vector store, knowledge graph, both, or none.
- **Confidence**: anecdotal
- **Quote**: "If Jev picks \"no retrieval needed\" with high confidence, you can send the query straight to the LLM."
- **Our assessment**: Routing sits in front of every query so latency matters. The article gives no accuracy data for routing mistakes (skipping retrieval wrongly produces ungrounded answers).

### Claim 5: Reranking and a sufficiency check can be done by parallel scoring of chunks plus a yes/no question
- **Evidence**: Worked example: score 20 chunks in parallel, keep top five, then ask whether the kept chunks are enough; no metrics.
- **Confidence**: anecdotal
- **Quote**: "Instead of asking an LLM to judge 20 chunks one by one, you score them all in parallel and keep the top ones."
- **Our assessment**: Extends the BM25 + Jev reranking idea (Willison Claim 7) to a second stage, but still without quality results. The sufficiency check ("retrieve again... or tell the user you don't know") is the more distinctive pattern, since the article notes "a question most pipelines skip".

### Claim 6: Post-generation grounding can be done by splitting the answer into claims and verifying each against retrieved chunks
- **Evidence**: Design recommendation; "A simple sentence splitter is usually enough."
- **Confidence**: anecdotal
- **Quote**: "Unsupported claims get flagged or removed before the user sees them."
- **Our assessment**: Matches the "verify everything" use-case family in the Latent Space interview. It needs per-claim calls on every answer, so only works if checks are cheap. Sentence splitting will miss multi-sentence or implicit claims; the article does not address this.

### Claim 7: Use probability bands: act above 0.9, fall back to an LLM between 0.6 and 0.9, escalate to human or safe default below 0.6
- **Evidence**: "I implemented a simple framework"; thresholds stated, no calibration data or distribution of cases per band.
- **Confidence**: anecdotal
- **Quote**: "Between 0.6 and 0.9, fall back to the LLM for a second opinion."
- **Our assessment**: The most concrete, transferable artifact: a three-band confidence cascade with a human escape hatch. The numbers are an example; they only mean something if the model is calibrated on your data, which the author concedes later (Claim 9).

### Claim 8: Logged probabilities provide an audit trail and drift signal for regulated settings
- **Evidence**: Author's experience claim: "Using Jev allowed us to log every probability, chart it and then alert us when it drifts."
- **Confidence**: anecdotal
- **Quote**: "\"The model was 94% confident this document is sensitive, and our threshold is 90%\" is an audit trail. \"The LLM said so\" is absolutely not."
- **Our assessment**: A reasonable argument, though a confidence number is a weaker audit artifact than it sounds given no explanation is returned (see Willison Claim 8). Drift alerting on probability distributions is a practical observability idea.

### Claim 9: Jev is only as good as the options you give it; verify calibration on your own data
- **Evidence**: Reasoned caution.
- **Confidence**: emerging
- **Quote**: "So, when Jev says 80%, check that it's right about 80% of the time on your own data."
- **Our assessment**: Correct and important; it is a calibration check that should accompany any threshold-based routing. Also: "a badly designed list of choices will still produce confident wrong answers".

### Claim 9a: Vendor risk: early access, vendor-published benchmarks, proprietary hosted model, no explanations
- **Evidence**: Author's caveats at time of writing (early October 2026).
- **Confidence**: emerging
- **Quote**: "published benchmarks come from TypeSafe itself and independent results are only starting to appear."
- **Our assessment**: Honest, and consistent with other notes. Also states that for decisions needing a written reason "an LLM is a more suitable option".

### Claim 10: Adopt incrementally: shadow one high-volume, low-risk decision (e.g., query routing) next to the existing LLM call for a few weeks
- **Evidence**: Recommendation only.
- **Confidence**: anecdotal
- **Quote**: "Instead, I’d recommend picking one high-volume, low-risk decision, such as query routing, and run Jev next to the current LLM call, comparing the results for a few weeks."
- **Our assessment**: Good adoption advice (shadow-mode comparison), applicable to any model swap, not Jev-specific.

### Claim 11: Right-sizing the model per decision is what "rewiring for agents" means
- **Evidence**: Author's framing.
- **Confidence**: anecdotal
- **Quote**: "Not bigger models everywhere, but the right model for each decision."
- **Our assessment**: A slogan consistent with model-routing material in the corpus; no evidence offered.

## Concrete Artifacts

```
Source: Penumarthi, "Use the probability, not just the answer"
Above 0.9, act on the decision automatically.
Between 0.6 and 0.9, fall back to the LLM for a second opinion.
Below 0.6, send it for human review or return a safe default.
```

```
Source: Penumarthi, stage-to-answer-type mapping (paraphrased table, not a quote)
Ingestion:       choice (document type) + yes/no (sensitive data?)
Before retrieval: choice (vector store / knowledge graph / both / none) + yes/no (rewrite needed?)
After retrieval:  score (each chunk; keep top 5 of 20) + yes/no (enough to answer?)
After generation: yes/no per claim (supported by retrieved chunks?)
```

## Cross-References

- **Corroborates**: `blog-latentspace-jev-system-one-for-prod.md` Claim 9 (confidence-based cascade), Claim 6 (decompose into small measurable questions) and Claim 8 (per-item verification questions); `blog-simonwillison-jev-decision-models.md` Claim 7 (cheap first stage plus Jev scoring), though with no quality data, so it remains weak corroboration; `blog-simonwillison-jev-decision-models.md` Claim 8 (no explanations).
- **Contradicts**: None found.
- **Extends**: `blog-simonwillison-jev-decision-models.md` Claim 7 by adding a sufficiency check, routing and claim-grounding stages; `blog-latentspace-ainews-jev-system-one-model.md` Claim 4 (replace LLMs as judges/classifiers/routers) with a RAG-specific stage map; `blog-fowler-bayer-prince-agentic-rag.md` and `blog-jetbrains-rag-semantic-code-search.md` (RAG architecture) as an alternative pipeline decomposition.
- **Novel**: The four-stage decision map for RAG; the explicit 0.9/0.6 band numbers with a human-review tier; the "log every probability, chart it, alert on drift" practice; shadow-mode adoption advice. Note: it provides no measured evidence, so the reranking pattern flagged "emerging" is still unproven.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Candidate pattern "classify the decision before choosing the model": audit a pipeline for calls that are decisions rather than generation. Cite as practitioner anecdote only.
- **Chapter 03 (Verification)**: Claim-level grounding check and sufficiency check ("tell the user 'I don't know'") as post-generation verification patterns; pair with calibration check from Claim 9 before relying on thresholds.
- **Chapter 04 (Context Engineering)**: Pre-retrieval routing including a "no retrieval" branch and a post-retrieval sufficiency gate as retrieval-efficiency tactics.
- **Do not upgrade**: This source does not supply the "corroborating evidence" the Willison note asked for; keep BM25 + Jev reranking marked as a candidate pattern.

## Extraction Notes

- Read the full article (fetched raw HTML and stripped markup); quotes were copied from that text. Curly apostrophes preserved where the source uses them.
- Single, short blog post; no sub-pages followed. No numbers or code in the source beyond the thresholds.
- Claim 9a is an extra numbered item; numbering follows document order of this note.
