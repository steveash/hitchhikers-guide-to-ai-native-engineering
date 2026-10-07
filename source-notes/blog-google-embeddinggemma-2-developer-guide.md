---
source_url: https://developers.googleblog.com/embeddinggemma-2-the-developer-guide/
source_type: blog-post
title: "EmbeddingGemma 2: The Developer Guide"
author: "Maarten Grootendorst (Member of Technical Staff), Ian Ballantyne (Senior Developer Relations Engineer) (Google)"
date_published: 2026-10-06
date_extracted: 2026-10-07
last_checked: 2026-10-07
status: current
confidence_overall: emerging
issue: "#3954"
---

# EmbeddingGemma 2: The Developer Guide

> A first-party Google developer guide to EmbeddingGemma 2, a sub-1B Apache 2.0 multimodal embedding model (text, code, images, video, audio in one 768-d space) with modular encoder loading (270M/440M/570M/740M) and Matryoshka truncation (768d down to 128d, with stated quality-retention figures per dimension), giving concrete sizing and storage-tradeoff guidance for RAG and agentic code search.

## Source Context

- **Type**: blog-post (Google Developers Blog, Oct. 6, 2026; tutorial/developer guide with runnable `sentence-transformers` code).
- **Author credibility**: Vendor-authored by the model's team (a Member of Technical Staff and a Senior DevRel Engineer at Google). Authoritative on how the model works; the quality-retention numbers are vendor-reported and not accompanied by a benchmark table in the post. (The Prospector's triage comment attributes Grootendorst to Anthropic; the post itself lists the byline roles without that claim, and we do not repeat it.)
- **Scope**: Covers architecture at a high level, loading/encoding code, MRL truncation, configuration guidance (which encoders, which dimension, how much fits in an input), and one benchmark claim (MTEB Code). Does NOT provide full benchmark tables, latency numbers, or comparisons with non-Google embedding models. A companion post ("Bring multimodal semantic search to the edge with EmbeddingGemma 2") is listed under Related Posts but was not mined here.

## Extracted Claims

### Claim 1: A single compact open model can replace chained single-modality encoders by mapping text, code, images, video, and audio into one shared 768-d space
- **Evidence**: Architecture description; code showing a text query compared via `model.similarity` against image and audio embeddings. No cross-modal retrieval benchmark table is given.
- **Confidence**: emerging
- **Quote**: "EmbeddingGemma 2 replaces chained models with modular encoders that project into a shared 768-dimensional space"
- **Our assessment**: Plausible and practically useful: one index serves all modalities. Quality vs. best-of-breed per-modality models is unquantified in the post.

### Claim 2: Encoders can be loaded selectively, giving four footprints (270M text/code, 440M +vision, 570M +audio, 740M full), and disabled encoders are never loaded into memory
- **Evidence**: Parameter breakdown (text/code 270M base, vision +170M, audio +300M) and `config_kwargs` code setting `vision_config`/`audio_config` to `None`.
- **Confidence**: emerging
- **Quote**: "Disabled encoders are never loaded into memory, so the savings apply to both the weights and peak allocation"
- **Our assessment**: A concrete "pay only for the modalities you index" pattern. Vendor-stated; no measured RAM figures given beyond parameter counts.

### Claim 3: All four encoder setups share one vector space, so a query embedded with the small text-only setup can be matched against documents embedded by the full model, and adding modalities later does not require re-embedding
- **Evidence**: Stated design property of the single checkpoint in sentence-transformers.
- **Confidence**: emerging
- **Quote**: "a query embedded with the 270M text-only setup can be matched directly against documents embedded with the full model"
- **Our assessment**: Operationally significant (cheap query-side client, heavy indexing server; incremental modality rollout). Untested by us; worth validating for quality asymmetry.

### Claim 4: If you start with a text-only index and later add image or audio, existing embeddings do not need re-computation
- **Evidence**: Stated guidance in "Which Encoders to Load".
- **Confidence**: emerging
- **Quote**: "Embeddings you have already computed do not need to be re-computed."
- **Our assessment**: Removes a major migration cost of embedding-model switches, if it holds as claimed.

### Claim 5: Matryoshka truncation cuts vector storage by up to 6x (1.5 GB → 250 MB per million vectors in bfloat16, 768d → 128d)
- **Evidence**: Arithmetic example given in the post; `truncate_dim` + `normalize_embeddings=True` code.
- **Confidence**: settled (storage arithmetic); emerging (quality retained)
- **Quote**: "in bfloat16 precision, storing a million 768-dimensional vectors takes roughly 1.5 GB of memory, while truncating them to 128 dimensions requires just 250 MB"
- **Our assessment**: Arithmetic is straightforward. Storage savings are real; the quality tradeoff is in Claim 6.

### Claim 6: Dimension choice is modality-dependent: 256d keeps most quality on text/code and ~95% on image/video/speech; 128d keeps ~90% on text/code but only ~75% on image/video/speech
- **Evidence**: Vendor-reported percentages in the configuration guide (no underlying table).
- **Confidence**: emerging
- **Quote**: "Text and code retains around 90% quality, but image, video, and speech retrieval quality drop to around 75%."
- **Our assessment**: Useful rule of thumb that multimodal embeddings degrade faster under truncation than text. Note an inconsistency with the triage summary: the post says 256d keeps "most of the full quality" on text/code, not a numeric figure. The post itself warns to validate before using 128d for multimodal.

### Claim 7: Use 128d for first-stage shortlisting before re-ranking, 768d/512d for multimodal and visual-document retrieval
- **Evidence**: Configuration guidance list.
- **Confidence**: emerging
- **Quote**: "Large text-only indexes and first-stage shortlisting (shortlisting before re-ranking)."
- **Our assessment**: Matches the standard two-stage retrieve-then-rerank pattern; low-dimension vectors as a cheap recall stage is a sound recommendation.

### Claim 8: Validate truncated dimensions on your own data before deploying; queries and documents must use the same dimension
- **Evidence**: Explicit caveats in the post.
- **Confidence**: settled
- **Quote**: "Validate on your target data before deploying 128d for multimodal queries.."
- **Our assessment**: Good hygiene and consistent with eval-first practice. (Quote reproduces the source's double period.)

### Claim 9: Retrieval requires asymmetric task prompts for queries versus documents
- **Evidence**: Code using `prompt_name="SearchQuery"` vs `prompt_name="Document"`; media passed without a prompt.
- **Confidence**: settled (common for modern embedding models)
- **Quote**: "EmbeddingGemma 2 is trained with short task instructions to steer representations for specific tasks."
- **Our assessment**: A frequent silent-failure source (forgetting prompts degrades retrieval); worth a checklist item.

### Claim 10: Code retrieval improves 14% over EmbeddingGemma 1 on MTEB (Code), making it suited to local codebase indexing and agentic code search
- **Evidence**: One benchmark claim plus a demo: the 270M text-only setup embeds the Hugging Face transformers codebase, searched by an agent (Gemma 4 26B A4B with the Pi agent harness). No numbers beyond the 14%.
- **Confidence**: emerging
- **Quote**: "EmbeddingGemma 2 scores 14% higher than EmbeddingGemma 1 on MTEB (Code)"
- **Our assessment**: Relevant to agentic code search, but vendor self-comparison against its own predecessor only.

### Claim 11: Paired with Gemma 4 in an on-device RAG pipeline, the embedder and generator share the text tokenizer and audio encoder architecture, reducing total memory footprint
- **Evidence**: Stated architectural property; no measurement.
- **Confidence**: anecdotal
- **Quote**: "both models share the same text tokenizer and audio encoder architecture, reducing the total memory footprint"
- **Our assessment**: Plausible vendor-ecosystem advantage; savings unquantified.

### Claim 12: Context budget is shared across modalities at fixed rates (8,192 tokens), and media has input-handling defaults
- **Evidence**: A table of per-modality capacity exists on the page (not present in the extracted page text); the text states defaults.
- **Confidence**: settled
- **Quote**: "Video is sampled at 1 frame per second by default, and audio should be 16 kHz mono."
- **Our assessment**: Operational detail relevant to ingestion pipelines. The per-modality maxima table was not recoverable from the page text; the note does not cite specific maxima.

## Concrete Artifacts

```python
# Source: EmbeddingGemma 2: The Developer Guide, Step 1 (memory-optimized loading)
# Text only (270M parameters)
text_only_model = SentenceTransformer(
    MODEL_ID,
    config_kwargs={"vision_config": None, "audio_config": None},
)
```

```python
# Source: same post, Step 4 (Matryoshka truncation)
query_emb = model.encode(
    query,
    prompt_name="SearchQuery",
    truncate_dim=256,
    normalize_embeddings=True,
)
```

```
# Source: same post, "Which Dimension to Use" (vendor-reported)
768d / 512d : multimodal & visual-document retrieval
256d (3x storage reduction): ~95% quality image/video/speech; most quality on text/code
128d (6x storage reduction): ~90% text/code; ~75% image/video/speech
Storage: 1M x 768d bfloat16 ~= 1.5 GB; 1M x 128d ~= 250 MB
Install: pip install -U sentence-transformers[image,audio,video] transformers  (v6.1.0+)
```

## Cross-References

- **Corroborates**: `blog-jetbrains-rag-semantic-code-search.md` — both treat embedding-storage reduction as a first-order design concern for code search (JetBrains via binary quantization, Claim 7; here via MRL truncation, Claim 5). Also supports Claim 1 of that note (grep/keyword limits) only indirectly via the "agentic code search" framing.
- **Contradicts**: None found. (JetBrains' acceptance of recall loss for agent use, its Claim 8, is consistent with this post's shortlisting guidance, not opposed.)
- **Extends**: `blog-google-litert-raspberry-pi-gemma-edge.md` — Claim 2 lists EmbeddingGemma 300M as one edge-tuned Gemma size; this note covers its successor in depth. `blog-google-gemma-4-12b-developer-guide.md` — Claim 1 describes Gemma 4 12B's unified multimodal architecture; EmbeddingGemma 2 is the retrieval-side counterpart in the same family. `blog-google-qwen3-embedding-tpu-precision.md` — covers serving (Claim 3, long-context multimodal embedding), whereas this covers model selection/sizing.
- **Novel**: Modality-conditional MRL guidance (at 128d multimodal loses roughly 25% vs. roughly 10% for text/code); selective encoder loading from one checkpoint with compatible vector spaces; first embedding-model developer guide in the corpus.

## Guide Impact

- **Chapter 04 (Context Engineering)**: Add a short embedding-selection/sizing subsection: load only needed modality encoders, choose truncation dimension by modality and stage (128d shortlist → higher-dim rerank), and validate on own data. Cite this note (Claims 2, 6, 7, 8) with the caveat that figures are vendor-reported.
- **Chapter 02 (Foundational Patterns)**: Candidate checklist item for retrieval pipelines: use distinct query/document task prompts (Claim 9) and same-dimension queries and documents (Claim 8).
- **Chapter 05/08 (if retrieval/RAG content exists)**: Pair with the JetBrains quantization approach as alternative storage-reduction levers; compare MRL truncation vs. binary quantization.

## Extraction Notes

- Fetched raw HTML via `curl` and read the full text; all quotes were checked character-for-character against the stripped page text. The per-modality capacity table and some images/videos are not present in extracted text.
- The post links to the Gemma documentation and a companion edge-search post; neither was followed (the companion is a distinct submission candidate).
- No benchmark tables or third-party validation exist in the post; hence `confidence_overall: emerging`.
- Triage comment 1 expected "~95% on video/speech" for 256d and "down to 128d"; both are consistent with the post. Triage comment 3's Anthropic attribution for an author was not supported by the source.
