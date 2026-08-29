---
source_url: https://developers.googleblog.com/enterprise-grade-precision-for-long-context-multimodal-embedding-inference-on-cloud-tpu/
source_type: blog-post
title: "Enterprise-Grade Precision for Long-Context Multimodal Embedding Inference on Cloud TPU"
author: "Anthony Su (Software Engineer, Google), Injae Kwak (Product Manager, Google)"
date_published: 2026-08-26
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: emerging
issue: "#3000"
---

# Enterprise-Grade Precision for Long-Context Multimodal Embedding Inference on Cloud TPU

> A first-party Google Developers Blog engineering report describing how Google ported the Qwen3 Embedding model series (text and multimodal pooling/embedding models, not autoregressive generation) to run on Cloud TPU via vLLM, covering three TPU-specific engineering fixes (vocabulary tensor-alignment padding, lazy-loading/pre-warming hardening, and a "StepPool" chunked-prefill architecture for long-context pooling), a numerical-parity verification methodology (cosine similarity against XPU golden references, ≥0.999/≥0.995 thresholds), and self-reported throughput figures — a low-level ML-serving infrastructure report, the corpus's sixth Google/TPU source and the first covering embedding/pooling inference specifically rather than generative LLM serving or training.

## Source Context

- **Type**: blog-post (Google Developers Blog, tagged AI/Cloud/Best
  Practices; published August 26, 2026). Discovered via the trusted
  `google-developers` RSS feed. No sub-pages were followed — the post is
  self-contained; it links out only to GitHub recipe repositories and the
  Cloud TPU product page, which are referenced as artifacts (see Concrete
  Artifacts) rather than fetched for additional claims.
- **Author credibility**: Two named Google authors — Anthony Su (Software
  Engineer) and Injae Kwak (Product Manager) — writing on the official
  Google Developers Blog, with a closing acknowledgment crediting "Google
  Cloud Product, Engineering and the vLLM community." This is a shorter,
  more announcement-oriented post than the corpus's densest Google/TPU
  report (`blog-google-qwen35-ironwood-moe-optimization.md`, 35+ named
  contributors, PR-referenced postmortem style) — closer in weight to
  `blog-google-ray-tpu-serve-data-train.md` (two named authors, how-to/
  announcement register).
- **Scope**: Covers what embedding models are and why enterprises use them,
  the case for elastic TPU+GPU serving via vLLM and GKE Custom Compute
  Classes, three named TPU-porting engineering challenges for the Qwen3
  Embedding model series, a minimal vLLM initialization code sample,
  a numerical-parity verification methodology and its pass thresholds, and
  one throughput benchmark table for Qwen3-Embedding-8B plus one
  (caption-only) table for the multimodal Qwen3-VL-Embedding-8B variant.
  Does **not** cover: the actual measured cosine-similarity scores achieved
  (only the pass thresholds are given, not the achieved values), a
  CPU-baseline throughput number to compare the 83,996 tokens/s figure
  against (despite the section heading naming "TPU vs. CPU Baseline"), cost/
  pricing, or any claim about AI-assisted software engineering workflows.

## Extracted Claims

### Claim 1: Embedding models convert text, image, and audio inputs into dense vectors that preserve semantic (not orthographic) similarity, illustrated by "cat" mapping close to "feline"/"dog" but far from the orthographically similar "hat"/"car"
- **Evidence**: Direct definitional framing in the opening section, with a
  worked example.
- **Confidence**: settled (a standard, well-established definition of
  embedding models, not a claim specific to this post or to TPU serving)
- **Quote**: "Simply put, embedding models translate inputs of various types of data — including text, images, and audio — into dense vector math."
- **Our assessment**: Uncontroversial background framing, included here
  only because it establishes the scope (pooling/embedding inference, not
  autoregressive generation) that distinguishes this post from every other
  TPU note in the corpus, all of which cover generative-LLM training or
  serving.

### Claim 2: Google Cloud added native TPU support to vLLM so teams can provision TPU nodes alongside GPU instances and use GKE Custom Compute Classes to auto-fallback to secondary GPU spot/on-demand pools if primary TPU reservations are fully utilized
- **Evidence**: Direct architectural description in "Seamless Elasticity
  with vLLM-TPU & GKE," paired with a named GKE feature.
- **Confidence**: emerging (a first-party description of a shipped
  capability; the fallback behavior is described mechanistically but not
  demonstrated with a specific incident or measured fallback-latency figure
  in this post)
- **Quote**: "By taking advantage of primitives like Custom Compute Classes in Google Kubernetes Engine (GKE), organizations can automate node autoscaling based on strict priority rules to scale up across different capacity types or accelerators if the previous one isn't available."
- **Our assessment**: This is the same TPU+GPU elastic-fallback pattern
  named generically ("primary reservation exhausted, fall back to a
  secondary pool") rather than shown with a concrete trigger threshold or
  observed fallback event — directionally useful as a capacity-planning
  pattern but not independently verified in this extraction.

### Claim 3: Serving next-generation embedding models in production requires processing "ultra-long sequence contexts" — 4K+ tokens for text, 15K+ tokens for multimodal text-and-image inputs — while maintaining strict mathematical parity with reference implementations across hardware backends
- **Evidence**: Direct scope statement opening "Engineering High-Precision
  Embedding Support on TPUs," framing the rest of the post's three
  challenges.
- **Confidence**: settled (a factual scope/requirements statement that the
  rest of the post's engineering work is built to satisfy — not a
  performance claim in itself)
- **Quote**: "Serving next-generation embedding models in production demands processing ultra-long sequence contexts - ranging from 4K+ tokens for text workloads up to 15K+ tokens for multimodal text-and-image inputs."
- **Our assessment**: This is the article's framing constraint: unlike
  chat/completion serving, where "long context" often means tens or
  hundreds of thousands of tokens, embedding/pooling workloads are
  considered "ultra-long" starting around 4K-15K tokens — useful context
  for calibrating expectations if the guide ever discusses embedding-model
  context limits for retrieval pipelines.

### Claim 4: TPU Matrix Execution Units (MXUs) impose strict divisibility constraints when sharding vocabulary matrices via Tensor Parallelism, which Google addressed with a "unified, hardware-safe vocabulary padding strategy" to guarantee exact tensor alignment during All-Gather execution
- **Evidence**: Direct technical description in "Challenge A: Hardware-Safe
  Tensor Alignment."
- **Confidence**: emerging (a specific, named engineering fix for a stated
  hardware constraint, but no before/after failure example or error message
  is given to show what happens without the padding — the constraint and
  the fix are both asserted, not demonstrated with a reproduction case)
- **Quote**: "TPU Matrix Execution Units (MXUs) impose strict divisibility constraints when sharding vocabulary matrices across topology meshes via Tensor Parallelism (TP). We implemented a unified, hardware-safe vocabulary padding strategy that guarantees exact tensor alignment during All-Gather execution."
- **Our assessment**: This is a narrower, embedding-specific instance of
  the same general "TPU hardware rewards specific tensor-shape alignment"
  theme already documented for generative-LLM serving in
  `blog-google-tpu-microbenchmarks-roofline.md` Claim 5 (head_dim=128 vs.
  256-aligned systolic-array shapes) and
  `blog-google-qwen35-ironwood-moe-optimization.md` Claim 7 (KV-cache block
  size 16→256 fixing VPU indexing stalls) — see Cross-References. Here the
  misaligned tensor is the vocabulary/embedding matrix rather than an
  attention dimension or cache page size, but the underlying pattern
  (TPU MXU/VPU hardware has specific divisibility/alignment requirements
  that naive sharding can violate) recurs across all three sources.

### Claim 5: vLLM's TPU lazy-loading (used to reduce cold-start latency and host memory usage) caused model initialization failures during lazy tensor transformations, which Google fixed via "attribute promotion within the unquantization pipeline"
- **Evidence**: Direct technical description in "Challenge B:
  Materialization Hardening, TPU Lazy-Loading & Compilation Pre-warming."
- **Confidence**: emerging (a specific named fix for a specific stated
  failure mode, but the failure mode itself — what error the initialization
  failures actually produced, how often they occurred — is not described
  beyond "model initialization failures during lazy tensor transformations")
- **Quote**: "To eliminate model initialization failures during lazy tensor transformations, we introduced attribute promotion within the unquantization pipeline, making weight loading fully compatible with vLLM's TPU lazy-loader for zero-failure initialization."
- **Our assessment**: A concrete engineering fix named specifically enough
  (attribute promotion in the unquantization pipeline) to be checkable
  against the linked open-source recipe/vLLM-TPU codebase, though the
  post itself gives no reproduction steps or error text for the failure it
  fixes.

### Claim 6: To avoid runtime JIT compilation latency and compilation traps in multi-process deployments, Google implemented "sharding-aware pre-warming" to lock JAX/XLA compilation caches before inference begins
- **Evidence**: Direct technical description immediately following Claim 5,
  same section.
- **Confidence**: emerging (a named technique with a stated purpose,
  presented as a shipped fix rather than a benchmarked improvement — no
  before/after compilation-latency number is given)
- **Quote**: "Furthermore, to eliminate runtime JIT compilation latencies and avoid compilation traps in multi-processes deployments, we implemented sharding-aware pre-warming to lock JAX/XLA compilation caches prior to inference and stabilize the production pipelines and rollouts."
- **Our assessment**: JAX/XLA pre-warming to avoid first-request JIT
  compilation stalls is a known pattern in JAX-based serving generally;
  this post's contribution is naming it as "sharding-aware" specifically —
  i.e., the pre-warming step accounts for the tensor-parallel sharding
  topology, not just the model graph in isolation. No independent
  verification of the claimed stabilization effect is given.

### Claim 7: Ultra-long-context embedding inference risks High Bandwidth Memory exhaustion during chunked prefill in the pooling layer, which Google addressed with a "hybrid StepPool" architecture that migrates metadata to `CachedRequestState` so pooling state accumulates correctly across steps and survives request preemptions
- **Evidence**: Direct technical description in "Challenge C: Long-Context
  StepPool Architecture," naming a specific internal data structure
  (`CachedRequestState`).
- **Confidence**: emerging (a specific, named architectural fix for a
  stated memory-exhaustion risk and a stated correctness risk — state loss
  across step boundaries and on preemption — but presented as a design
  description, not validated with a specific before/after failure case or
  a measured preemption-survival rate)
- **Quote**: "Ultra-long contexts require Chunked Prefill in the pooling layer to prevent High Bandwidth Memory (HBM) exhaustion, creating risk of state loss across step boundaries. We engineered a hybrid StepPool and migrated metadata to CachedRequestState, ensuring pooling states correctly accumulate across steps and survive request preemptions."
- **Our assessment**: This is the post's most embedding-specific
  engineering contribution — chunked prefill for autoregressive generation
  is well-established, but chunked prefill for a *pooling* (embedding)
  model has a different correctness requirement: partial pooling state must
  survive across chunks and across preemption/resumption, not just partial
  KV cache. This is a genuinely distinct problem from the generative-LLM
  serving challenges documented elsewhere in the corpus's TPU notes.

### Claim 8: To certify enterprise-grade precision, Google measures cosine similarity between TPU-generated embedding vectors and XPU golden-reference vectors, requiring ≥0.999 for text and ≥0.995 for multimodal inputs as the quality pass threshold
- **Evidence**: Direct methodology and threshold statement in
  "Golden-Reference Precision & Numerical Parity."
- **Confidence**: emerging (a specific, named verification methodology and
  explicit numeric pass thresholds — checkable in principle — but the post
  does not report the actual achieved cosine-similarity scores, only the
  thresholds used to judge pass/fail, so a reader cannot tell how close to
  the threshold the achieved parity actually was)
- **Quote**: "A cosine similarity score approaching 1.0 (with a target quality pass threshold of ≥0.999 for text and ≥0.995 for multimodal inputs) demonstrates near-perfect numerical parity across hardware backends. This confirms that optimizations implemented on the vLLM-TPU stack maintain golden-reference precision without sacrificing accuracy."
- **Our assessment**: This is a concrete, reusable verification pattern:
  define a numeric similarity threshold against a golden (reference-
  hardware) output and require every optimization to clear it, rather than
  relying on end-task benchmark scores alone. This directly corroborates
  the "golden implementation" fidelity philosophy documented in
  `blog-latentspace-baseten-inference-engineering-masterclass.md` Claim 9
  (Baseten: "quality... [is] how close are we getting to that, 100%
  fidelity of the model") and the FP8 kernel "Numerical Verification Layer"
  in `blog-google-qwen35-ironwood-moe-optimization.md` Claim 9 (zero
  deviation from a Float32 reference path) — three independent sources now
  document the same underlying practice (numerically verify optimized/
  ported inference against an unoptimized or cross-hardware reference,
  as a first-class deliverable) applied to three different optimization
  types: quantization (Baseten), FP8 kernel gating (Qwen 3.5/Ironwood), and
  cross-hardware porting (this post). See Cross-References.

### Claim 9: Serving Qwen3-Embedding-8B at 16K+ sequence length with tensor parallelism of 4 in bfloat16 on TPU Ironwood achieved 83,996 total tokens/second and 5.13 requests/second while maintaining strict numerical alignment
- **Evidence**: Table 1 caption in "Qwen3-Embedding-8B (7K+ Tokens, TPU vs.
  CPU Baseline)" section — the only quantified throughput figures in the
  post.
- **Confidence**: anecdotal (a single self-reported throughput/latency pair
  for one specific configuration; despite the section heading naming a
  "TPU vs. CPU Baseline" comparison, no CPU baseline number is actually
  given anywhere in the extracted text to compare against, and no table
  data beyond the caption sentence was rendered as extractable text)
- **Quote**: "While maintaining strict numerical alignment, serving qwen-3-embedding-8b (bf16, 16K+ sequence length, TP=4) on TPU Ironwood achieved an impressive throughput of 83,996 total token/s and 5.13 req/s."
- **Our assessment**: This figure is presented without any comparison
  baseline in the readable text (the "vs. CPU Baseline" framing in the
  section title is not substantiated by a stated CPU number), so it cannot
  be read as a speedup claim — only as an absolute throughput data point
  for this one specific configuration (TP=4, bf16, 16K+ tokens, Ironwood).
  Treated as the weakest-evidence claim in this note, consistent with how
  the corpus treats unbounded single-configuration vendor throughput
  numbers (compare `blog-google-tpu-microbenchmarks-roofline.md` Claim 8's
  treatment of an unnamed 110B MoE case study).

### Claim 10: For multimodal embedding models, vLLM-TPU's chunked prefill only chunks the text portion of the multimodal input — the image portion is handled differently
- **Evidence**: Table 2 caption in "Qwen3-VL-Embedding-8B (15K+ Tokens,
  TPU vs. XPU Baseline)" section — the only stated detail about multimodal
  prefill handling.
- **Confidence**: anecdotal (a one-sentence caption asserting a specific
  implementation behavior, with no explanation of why image tokens are
  excluded from chunking, no measured HBM-usage comparison, and no
  throughput number given for the multimodal variant despite the section
  heading)
- **Quote**: "vLLM-TPU only chunks the text portion of multimodal prefill."
- **Our assessment**: The thinnest claim in this post — it names a real
  implementation detail (text-only chunking for multimodal prefill) that a
  practitioner serving Qwen3-VL-Embedding-8B or a similar multimodal
  pooling model on TPU would need to know for memory planning, but gives
  no rationale, no measured consequence, and no accompanying throughput
  data for the multimodal configuration, unlike Claim 9's text-only figure.

### Claim 11: Google open-sourced setup and execution recipes for both Qwen3-Embedding-8B and Qwen3-VL-Embedding-8B on the AI-Hypercomputer public GitHub repository, alongside the underlying `vllm-project/tpu-inference` engine
- **Evidence**: Direct list of resources in "Public Recipes & Explore
  Resources," with named repository paths.
- **Confidence**: settled (specific, independently checkable public
  artifacts — named GitHub repository paths a reader can visit directly)
- **Quote**: "To help developers reproduce our numerical parity evaluations and rapidly deploy embedding workloads on Google Cloud TPUs, we have open-sourced official setup and execution recipes on the AI-Hypercomputer Public Repository."
- **Our assessment**: A concrete, reproducible artifact (unlike Claims 9-10,
  which give numbers/behavior without reproduction detail) — the linked
  `AI-Hypercomputer/tpu-recipes` paths for both the text and multimodal
  embedding models are the actual deployment code referenced throughout
  the post, making this the most independently verifiable claim in the
  note.

## Concrete Artifacts

### Minimal vLLM initialization sample for Qwen3-Embedding-8B on TPU (verbatim from the post)

```python
from vllm import LLM

# Initialize Qwen3-Embedding-8B on Cloud TPU using vLLM's native pooling runner
llm = LLM(
    model="Qwen/Qwen3-Embedding-8B",
    runner="pooling",             # Enables dense pooling output
    tensor_parallel_size=2,       # Sharded across TPU topology mesh
    max_model_len=16384,
    max_num_batched_tokens=512,
    dtype="bfloat16",
    trust_remote_code=True
)

# Extract dense vector embeddings across inputs
prompts = ["Enterprise-grade semantic retrieval on TPUs with vLLM."]
results = llm.embed(prompts)
embedding_vector = results[0].outputs.embedding
```

Source: developers.googleblog.com/enterprise-grade-precision-for-long-context-multimodal-embedding-inference-on-cloud-tpu/, "vLLM Embedding Sample on TPU" section.

### Public recipe and resource links (verbatim list from the post)

```
- Qwen3-Embedding-8B TPU Recipe: AI-Hypercomputer/Qwen3-Embedding-8B
- Qwen3-VL-Embedding-8B TPU Recipe: AI-Hypercomputer/Qwen3-VL-Embedding-8B
- vLLM TPU Engine: vllm-project/tpu-inference
- Google Cloud TPU Portal: cloud.google.com/tpu
```

Source: developers.googleblog.com/enterprise-grade-precision-for-long-context-multimodal-embedding-inference-on-cloud-tpu/, "Public Recipes & Explore Resources" section. Full GitHub paths (confirmed by `curl`-fetching the raw page): `github.com/AI-Hypercomputer/tpu-recipes/tree/main/inference/ironwood/vLLM/Qwen3-Embedding-8B` and `github.com/AI-Hypercomputer/tpu-recipes/tree/main/inference/ironwood/vLLM/Qwen3-VL-Embedding-8B`. Neither repository was independently fetched in this extraction — see Extraction Notes.

## Cross-References

- **Corroborates**: `blog-google-qwen35-ironwood-moe-optimization.md`
  Claim 9 (a dedicated "Numerical Verification Layer" auditing FP8 gating
  kernels against a Float32 reference, reporting zero deviation) and
  `blog-latentspace-baseten-inference-engineering-masterclass.md` Claim 9
  ("quality" defined as fidelity to a "golden implementation" of the
  model) — this post's Claim 8 (cosine-similarity parity against XPU
  golden references, with explicit ≥0.999/≥0.995 pass thresholds) is a
  third independent instance of the same practice: numerically verify an
  optimized or hardware-ported inference path against a trusted reference,
  as a first-class production deliverable rather than an afterthought.
  Also corroborates `blog-google-tpu-microbenchmarks-roofline.md` Claim 5
  (head_dim=128 vs. 256-aligned systolic-array shapes causing suboptimal
  MXU utilization) and `blog-google-qwen35-ironwood-moe-optimization.md`
  Claim 7 (KV-cache block size 16→256 fixing VPU indexing stalls): this
  post's Claim 4 (hardware-safe vocabulary padding for MXU tensor
  alignment during All-Gather) is a third, embedding-specific instance of
  the recurring "TPU MXU/VPU hardware has strict tensor-shape/divisibility
  requirements that naive sharding or padding can violate" pattern.
- **Contradicts**: None identified. No existing source note takes a
  position on embedding-model TPU serving, vLLM pooling-runner behavior,
  or cosine-similarity parity testing that this post's claims oppose.
- **Extends**: `blog-google-ray-tpu-serve-data-train.md` (vLLM-on-TPU
  serving via GKE, covered there for generative LLM serving via Ray Serve;
  this post covers the same vLLM-TPU serving stack but for pooling/
  embedding models specifically, and without Ray in the picture — it uses
  vLLM's native TPU integration and GKE Custom Compute Classes directly).
  Also extends the corpus's existing TPU/Ironwood cluster
  (`blog-google-qwen35-ironwood-moe-optimization.md`,
  `blog-google-tpu-microbenchmarks-roofline.md`,
  `blog-google-tunix-gemma-reasoning-hackathon.md`,
  `blog-google-tunix-agentic-rl-throughput.md`) as a sixth Google/TPU
  source note, the first to cover embedding/pooling inference rather than
  generative-LLM training or serving.
- **Novel**: This is the corpus's first source documenting: (1) TPU
  serving of embedding/pooling models (as opposed to autoregressive
  generation) at all; (2) the "StepPool"/`CachedRequestState` chunked-
  prefill architecture for pooling-layer state across preemptible steps;
  (3) explicit numeric cosine-similarity pass thresholds (≥0.999 text,
  ≥0.995 multimodal) as a stated production acceptance criterion for
  cross-hardware numerical parity; (4) any TPU-serving detail for a
  multimodal (text-and-image) embedding model specifically.

## Guide Impact

Following the same assessment reached independently by all five prior
Google/TPU source notes in this corpus
(`blog-google-tunix-gemma-reasoning-hackathon.md`,
`blog-google-tunix-agentic-rl-throughput.md`,
`blog-google-qwen35-ironwood-moe-optimization.md`,
`blog-google-ray-tpu-serve-data-train.md`,
`blog-google-tpu-microbenchmarks-roofline.md`): this article is ML-serving
infrastructure engineering — how to port and scale an embedding-model
inference stack onto TPU hardware — not guidance about how a practitioner
builds, configures, or operates an AI coding agent/harness. The guide's
actual chapters (confirmed by reading `guide/*.md` headers directly:
Principles, Daily Workflows, Harness Engineering, Verification, Context
Engineering, Team Adoption, Security and Threat Model) address working
*with* deployed AI coding agents in a software-engineering context — none
covers accelerator-hardware serving infrastructure, TPU-specific kernel
engineering, or embedding-model production deployment.

- **No direct chapter impact recommended.** None of Claims 1-11 describes
  a harness-configuration practice, a verification technique for
  AI-generated *code*, a context-management pattern for a coding agent, a
  team-adoption process, or a security consideration for coding-agent
  usage. The Prospector's three triage comments proposed Ch02 (Harness
  Engineering) and Ch04 (Context Engineering) relevance, but on reading the
  full article its subject is entirely TPU-serving infrastructure for a
  generic embedding-model workload — a different audience (ML infra
  engineers deploying embedding services) and a different layer of the
  stack (the compute substrate an embedding/retrieval *product* runs on,
  not the harness a developer uses to write code with AI assistance) — the
  same discrepancy already flagged in each of the five prior TPU notes'
  Guide Impact sections for their own respective triage comments.
- **Weak, indirect analogy only, flagged rather than forced**: Claim 8's
  numerical-parity-against-a-golden-reference verification methodology
  (cosine similarity ≥0.999/≥0.995 as an explicit pass threshold) is
  conceptually the same discipline as `blog-latentspace-baseten-inference-
  engineering-masterclass.md` Claim 9's "fidelity to a golden
  implementation" framing, which that note's own Guide Impact section
  already flags as a transferable verification philosophy. If the guide
  ever adds content on embedding-based retrieval/RAG pipelines as part of
  Ch04 (Context Engineering), this post's explicit-threshold parity-testing
  pattern would be a relevant citation for "how to verify a retrieval
  component wasn't silently degraded by an infrastructure change" — but
  the guide does not currently have such a section, and this source alone
  does not justify adding one.

## Extraction Notes

- **Verified the source is real and live before extraction.** The first
  `WebFetch` pass returned a paraphrased summary (it wrapped several
  sentences in quotation marks that did not match the source's actual
  wording character-for-character). Fetched the raw article HTML directly
  via `curl` (HTTP 200, ~49KB response) and stripped markup with a Python
  script to obtain the full, close-to-verbatim article text before
  extracting any quotes. Every `Quote` field above was checked against that
  `curl`-fetched, tag-stripped text, not against the WebFetch summarizer's
  paraphrase.
- **No sub-pages followed.** The post links only to GitHub recipe
  repositories and the Cloud TPU product page, all treated as artifacts
  (Concrete Artifacts, Claim 11) rather than fetched for additional
  substantive claims — consistent with how prior TPU notes in this corpus
  treat linked recipe repositories as large, actively-changing code
  samples rather than short substantive pages worth an independent fetch.
- **Tables rendered as caption-only text.** The post contains two data
  tables (Qwen3-Embedding-8B benchmark, Qwen3-VL-Embedding-8B benchmark)
  whose actual cell contents did not survive HTML-tag stripping as
  readable text — only their captions (Claims 9 and 10) were extractable.
  This is flagged explicitly rather than silently omitted: the post's
  headline throughput claim (83,996 tokens/s, Claim 9) and its multimodal
  chunking claim (Claim 10) are both weaker than they would be with the
  underlying table data, and both section headings promise a "vs. CPU
  Baseline" / "vs. XPU Baseline" comparison that the extractable text does
  not substantiate with an actual baseline number.
- **Existing overlap checked before writing.** Searched all
  `source-notes/*.md` for "embedding model", "Qwen3-Embedding",
  "cosine similarity", "numerical parity", "golden reference", "vLLM-TPU",
  "StepPool", and "pooling runner" before drafting. Found no existing note
  covering embedding/pooling-model TPU serving specifically; found the five
  prior Google/TPU notes (Qwen 3.5/Ironwood MoE, Ray-on-TPU, TPU
  microbenchmarks/Roofline, and the two Tunix notes) as the relevant
  infrastructure-layer cluster, and the Baseten inference masterclass note
  as the relevant cross-vendor corroboration for the "golden-reference
  fidelity" verification pattern (Claim 8) — both addressed in
  Cross-References.
- **Confidence rationale**: Set to `emerging` overall. The definitional
  framing (Claim 1) and the open-source recipe links (Claim 11) are
  concrete, independently checkable facts (rated `settled` individually).
  The three named engineering fixes (Claims 4-7), the elasticity
  architecture (Claim 2), the ultra-long-context scope statement (Claim 3),
  and the numerical-parity methodology (Claim 8) are specific, named
  first-party engineering descriptions not independently verified against
  the linked vLLM-TPU codebase in this extraction (rated `emerging`
  individually). The throughput and multimodal-chunking claims (Claims 9,
  10) are single-configuration, caption-only figures presented without the
  baseline comparison their own section headings promise (rated
  `anecdotal` individually — the weakest evidence in this note). The
  overall `emerging` rating reflects that mix: the architecture/methodology
  claims are specific and plausible, the headline performance numbers are
  thin and incompletely substantiated.
