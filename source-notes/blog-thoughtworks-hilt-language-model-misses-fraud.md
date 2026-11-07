---
source_url: https://www.thoughtworks.com/insights/blog/why-a-language-model-misses-fraud-in-your-transaction-data
source_type: blog-post
title: "Why a language model misses fraud in your transaction data"
author: Nathan Hilt (Thoughtworks)
date_published: 2026-11-06
date_extracted: 2026-11-07
last_checked: 2026-11-07
status: current
confidence_overall: anecdotal
issue: "#4578"
---

# Why a language model misses fraud in your transaction data

> A short Thoughtworks recap of a Sibos 2026 breakfast: a general LLM reads transaction data at the surface, TFMs (within-entity sequences) and GNNs (cross-entity graphs) are complementary, and fraud models need audit trails built into the pipeline; evidence is one unmeasured demo plus vendor-reported figures.

## Source Context

- **Type**: blog-post (Thoughtworks Insights blog, conference-breakfast recap; auto-discovered via trusted `thoughtworks` feed)
- **Author credibility**: Nathan Hilt, Thoughtworks; no bio in the article. Thoughtworks is a vendor-neutral consultancy, but the event was co-hosted with AWS and NVIDIA and the speakers quoted are from those vendors. The article carries Thoughtworks' standard disclaimer that opinions are the authors' own.
- **Scope**: Domain is payments/fraud ML. Covers the TFM vs. GNN distinction, market proof points, data readiness, and governance. Contains no code, no methodology, and no measured results from the demo. It is not about software engineering practice.

## Extracted Claims

### Claim 1: A general-purpose LLM can describe transaction patterns but cannot natively read transactions, so it returns surface-level flags
- **Evidence**: Assertion by the author; supported only by the Claim 4 demo (unmeasured).
- **Confidence**: anecdotal
- **Quote**: "However, it can't natively understand what a transaction is."
- **Our assessment**: Plausible and consistent with the grounding argument elsewhere in the corpus, but no benchmark is given. Treat as a framing, not a finding.

### Claim 2: A TFM captures within-entity temporal behaviour; a GNN captures cross-entity relational patterns; the fastest institutions combine them
- **Evidence**: Architectural explanation (sequence "grammar" of velocity, timing, merchant category, device history vs. message passing over nodes/edges). No performance comparison.
- **Confidence**: emerging
- **Quote**: "One reads a customer's story over time. The other reads the company that the customer keeps."
- **Our assessment**: A clean architect-level mnemonic. The "institutions moving fastest are combining both" claim is unsupported by named examples. It matches the hybrid-decisioning stance in the existing TFM note.

### Claim 3: Vendor-reported production proof points for transaction models (Revolut PRAGMA, Adyen Uplift, Mastercard LTM)
- **Evidence**: Figures stated without citation or methodology in the article; all vendor-reported.
- **Confidence**: anecdotal
- **Quote**: "Revolut's PRAGMA model, trained on 24 billion events and 207 billion tokens across 111 countries, improved external fraud recall by 64.7% and  lifted product recommendation by 40.5% from one pre-trained backbone."
- **Our assessment**: Attribute as vendor claims. No baseline, no precision/false-positive numbers, no independent validation. Adyen's "86% reduction in manual risk rules across 60 enterprise pilots" is similarly unqualified (fewer rules is not evidence of better detection). Do not cite as established performance.

### Claim 4: Grounding the same model (Claude) in transaction context turned a vague read into a structured, actionable risk breakdown
- **Evidence**: Live demo by Brian Blanchard at the breakfast; described in prose only, no metrics, dataset, prompt, or count disclosed.
- **Confidence**: anecdotal
- **Quote**: "The first pass produced a vague, pattern-level read. The second came back with a structured risk breakdown across the batch and a specific, actionable count of transactions warranting immediate review."
- **Our assessment**: The single most guide-relevant item: same model, different context, different output quality. But the demo is unmeasured and presented by the vendor-side host, so it illustrates rather than proves. Note the ambiguity: "grounded in transaction context" could mean a TFM, retrieval, or a semantic layer.

### Claim 5: The core enterprise gap is that proprietary context lives in warehouses inaccessible to public LLMs
- **Evidence**: Quote from Pahal Patangia (NVIDIA global payments industry leader); vendor perspective.
- **Confidence**: anecdotal
- **Quote**: "Your enterprise context is sitting in your proprietary warehouses, which is not available to the most popular large language models out there, and that's the key."
- **Our assessment**: Reasonable, but from an NVIDIA speaker with an interest in selling fine-tuning/training infrastructure. The article's follow-on, that fine-tuning on proprietary history teaches an institution its own fraud patterns, is asserted without evidence.

### Claim 6: Data readiness is staged — a raw layer, then a semantic layer giving each field one shared definition
- **Evidence**: Prescriptive description; no example schema.
- **Confidence**: emerging
- **Quote**: "A second layer gives every field, including \"risk score\" and \"merchant category,\" one consistent, semantic definition that every downstream model shares."
- **Our assessment**: A semantic-layer pattern familiar from data engineering; applying it to model inputs is sensible but thinly described.

### Claim 7: About 25 months of history is enough to start
- **Evidence**: Single quote from Paul Chang (AWS head of payment networks); no basis given.
- **Confidence**: anecdotal
- **Quote**: "typically, we recommend twenty-five months of data; that's all you need to get started."
- **Our assessment**: A vendor rule of thumb. Likely driven by seasonality (two full annual cycles plus a month), but the source does not say so; that is our inference.

### Claim 8: Build the audit trail into the pipeline from the start — log every question and answer, restrict model data access, and be able to reconstruct decisions
- **Evidence**: Author's assertion about regulator expectations; no regulation cited.
- **Confidence**: emerging
- **Quote**: "That means a record of every question a model was asked and every answer it gave, clear limits on what data each model can access and the ability to reconstruct how a decision was made."
- **Our assessment**: A generalizable pattern for any AI decision system. The article logs prompts and answers; the Kamelman note (Claim 4) argues model-generated explanations are not faithful causal records, so logging Q&A alone may be insufficient. Related tension, not a direct contradiction; not filed.

### Claim 9: A model that cannot explain itself is unlikely to clear production review regardless of accuracy
- **Evidence**: Assertion only.
- **Confidence**: anecdotal
- **Quote**: "A fraud model that can't explain itself is unlikely to clear production review, however accurate it looks in a demo."
- **Our assessment**: True for regulated finance as a practical matter; unevidenced here.

## Concrete Artifacts

No code or configs. Figures reported (all vendor-reported, as stated in the article):

```
Revolut PRAGMA: 24B events, 207B tokens, 111 countries;
  +64.7% external fraud recall; +40.5% product recommendation (one backbone)
Adyen Uplift: -86% manual risk rules across 60 enterprise pilots
Mastercard Large Transaction Model: built with NVIDIA and Databricks (no metrics)
AWS guidance: ~25 months of history to start
(Source: Hilt, Thoughtworks, 2026-11-06)
```

## Cross-References

- **Corroborates**: `blog-thoughtworks-gancz-transaction-foundation-models.md` — Claim 8 there (hybrid decisioning combining TFM embeddings, graph models, rules and human review) matches this article's "combining both into one shared context layer"; Claim 9 there (explainability and governance as operational requirements) matches Claim 8 here.
- **Contradicts**: None found. (Mild tension with Claim 4 of `blog-thoughtworks-kamelman-agentic-payments-executable-authority.md` on whether logged model output is adequate evidence; see Claim 8 above. Not a material contradiction, so no issue filed.)
- **Extends**: `blog-thoughtworks-gancz-transaction-foundation-models.md` — adds the TFM-vs-GNN framing, market proof points, and the 25-month data bar, none of which are in that note's 12 claims.
- **Novel**: The Sibos demo anecdote (same model, grounded vs. ungrounded), and the named vendor figures (Revolut, Adyen, Mastercard).

## Guide Impact

- **Chapter 04 (context engineering)**: At most, an optional one-line illustration that the same model gives vague vs. actionable output depending on grounding context, explicitly labeled an unmeasured vendor-event demo. Do not use as evidence for a recommendation.
- **Chapter 06 (security/governance)**: Optional corroboration, alongside the Kamelman note, for logging every model question/answer and restricting per-model data access in regulated decision systems.
- No other change recommended. The domain is outside the guide's core scope, and the vendor figures should not be cited.

## Extraction Notes

- Read the full article (single page, ~700 words) via direct fetch of the HTML. Did not follow the linked Thoughtworks GNN/TFM articles, the NVIDIA blueprint, or the AWS eBook; the TFM article is already covered by the existing note.
- Overall confidence is `anecdotal`: one unmeasured demo and vendor-reported statistics, no independent validation. Per triage, this note is kept short rather than duplicating the existing TFM note.
