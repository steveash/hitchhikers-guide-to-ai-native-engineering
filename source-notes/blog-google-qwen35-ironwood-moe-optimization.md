---
source_url: https://developers.googleblog.com/systems-engineering-playbook-optimizing-qwen-35-397b-moe-on-ironwood-tpu7x/
source_type: blog-post
title: "Systems Engineering Playbook: Optimizing Qwen 3.5-397B MoE on Ironwood (TPU7x)"
author: "Google for Developers (performance engineering team; named contributor list in Acknowledgements)"
date_published: 2026-07-14
date_extracted: 2026-07-15
last_checked: 2026-07-15
status: current
confidence_overall: emerging
issue: "#1886"
---

# Systems Engineering Playbook: Optimizing Qwen 3.5-397B MoE on Ironwood (TPU7x)

> A first-party Google Developers Blog systems-engineering deep-dive describing how a performance team optimized inference serving of the third-party, open-weights Qwen 3.5-397B Mixture-of-Experts model on Ironwood (TPU v7x) hardware, claiming ~3.1x (decode-heavy) and ~4.7x (prefill-heavy) throughput improvements via a hybrid Data-Parallel+Expert-Parallel sharding topology, custom JAX/Pallas kernels, and a "modular, model-agnostic" reusable-building-block optimization strategy — a low-level ML-serving infrastructure report with only a thin, indirect connection to this guide's actual scope (AI-assisted software engineering practice, not ML systems/kernel engineering).

## Source Context

- **Type**: blog-post (Google Developers Blog, "Optimization"/"Pallas"/"TPU"
  tagged technical report; published July 14, 2026). Discovered via the
  trusted `google-developers` RSS feed. No sub-pages were followed — the
  post is self-contained (it links out to a Hugging Face model repository
  and two third-party technical explainers on Qwen 3.5's hybrid attention
  design, but does not depend on them for its own claims).
- **Author credibility**: Bylined "Google for Developers" with an extensive
  named Acknowledgements section (35 named engineering-team contributors plus
  a 6-person program/product team), consistent with this corpus's other
  first-party Google technical deep-dives (compare
  `blog-google-litertjs-web-ai-inference.md`, four named authors;
  `blog-google-tunix-gemma-reasoning-hackathon.md`, five named authors).
  Unlike those two lighter announcement-style posts, this is a dense,
  PR-linked engineering report (12+ internal PR references by number) that
  reads as an internal performance-engineering postmortem published
  externally, not a product-launch announcement — the claims are far more
  granular (specific kernel designs, specific latency deltas) than typical
  vendor marketing copy.
- **Scope**: Covers Qwen 3.5-397B's architecture (hybrid Gated DeltaNet /
  GQA / sparse MoE layout), the benchmark methodology (prefill-heavy vs.
  decode-heavy workloads across four concurrency tiers on a single 4-chip
  Ironwood host), the sharding strategy (hybrid DP+EP replacing an
  infeasible tensor-parallel baseline), communication-fusion optimizations
  (All-Gather packing, Hierarchical Reduce-Scatter), custom Pallas kernels
  across three execution tracks (attention, MoE, GDN), a first-principles
  roofline analysis, and empirical throughput-vs-roofline results. Does
  NOT cover: cost/pricing of running this stack on Google Cloud, comparison
  against non-Google hardware (e.g., Nvidia GPUs) beyond a single one-line
  HBM-capacity aside, end-to-end request latency/quality trade-offs from a
  product perspective, or any claim about AI-assisted software engineering
  workflows — this is exclusively an ML-serving systems engineering report.

## Extracted Claims

### Claim 1: The team's strategic thesis is a "modular, model-agnostic optimization strategy" — decomposing models into reusable, hardware-aware building blocks (e.g., Batched RPA, Grouped GEMMs, SparseCore unpermutation) so that future model architectures can be optimized with "near-zero engineering friction" rather than months of per-model tuning
- **Evidence**: Stated directly as the motivating strategy in the Executive
  Summary, framed as a response to the growing complexity of the
  open-weights model landscape.
- **Confidence**: emerging (a stated engineering philosophy corroborated by
  the post's own detailed kernel-by-kernel breakdown, but "near-zero
  engineering friction" for *future* models is a forward-looking claim this
  single case study cannot itself prove)
- **Quote**: "Rather than tackling models as monolithic systems, we decompose them into self-contained, independent building blocks (such as Batched RPA, Grouped GEMMs, and SparseCore unpermutation) accompanied by hardware-aware cost models. When a new architecture arrives, these pre-optimized modules are ported with near-zero engineering friction."
- **Our assessment**: This is the report's organizing idea and the reason it
  reads as a "playbook" rather than a one-off case study — the kernel
  library (RPA, GMM, SparseCore gather/reduce) is explicitly designed to be
  reused across model families rather than rebuilt per model. The claim is
  plausible given the level of modularity shown in the kernel descriptions,
  but the post provides no second model as evidence that the reuse actually
  worked in practice — it is asserted as strategy, not demonstrated twice.

### Claim 2: The optimizations improved inference performance by approximately 3.1x for decode-heavy workloads and approximately 4.7x for prefill-heavy workloads (512-concurrency tier), measured between April and June 2026
- **Evidence**: Headline performance figures stated in the Executive Summary,
  with an explicit measurement window and concurrency tier specified.
- **Confidence**: anecdotal (vendor-self-reported improvement multiplier;
  the post does not state what the "before" baseline configuration was
  beyond implying a naive tensor-parallel starting point, and no
  independent party has reproduced these numbers)
- **Quote**: "The optimizations discussed below allowed us to improve inference performance by approximately 3.1x for Decode-heavy and by approximately 4.7x for Prefill-heavy workloads (512 Concurrency tier) between April and June 2026."
- **Our assessment**: The specificity of the measurement window (April-June
  2026) and concurrency tier (512) lends some rigor beyond a bare marketing
  multiplier, but this is still a self-reported before/after comparison with
  an unstated exact baseline. Should be cited as a vendor-reported directional
  figure, consistent with how this corpus treats other first-party Google
  performance claims (see `blog-google-litertjs-web-ai-inference.md` Claim 2).

### Claim 3: Qwen 3.5-397B activates only 17 billion of its 397 billion total parameters per token (a 4.3% activation ratio), via a hybrid layout of 75% Gated DeltaNet (linear attention) layers and 25% Grouped Query Attention layers, each paired with routed sparse MoE (512 experts, top-10 routing, plus one always-on shared expert)
- **Evidence**: Direct architectural description in Section 1, with layer
  counts, head counts, and expert-routing parameters specified.
- **Confidence**: settled (a factual architecture description, independently
  checkable against the model's own Hugging Face repository, which the post
  links directly)
- **Quote**: "The model consists of 397 billion total parameters, but leverages a highly sparse routing scheme that activates exactly 17 billion parameters per token per forward pass. This sparse configuration represents a 4.3% routing activation ratio, enabling the model to deliver the expressive capacity and intelligence of a 400B-class model while maintaining the inference footprint and execution speed of a much smaller 20B-class system."
- **Our assessment**: This is a concrete, checkable architecture fact (not a
  performance claim), and the 3:1 GDN:GQA layer ratio plus 512-expert/top-10
  MoE routing gives a specific reference point for how far MoE sparsity has
  progressed at the 400B-parameter scale — useful context for any future
  guide discussion of MoE-style sparse-activation architectures, distinct
  from the on-device sparse-activation technique (instruction-following
  pruning) documented in `blog-thoughtworks-lovin-gall-local-inference-boundary.md`
  Claim 1.

### Claim 4: Naive tensor-parallel sharding (TP=8) of the GQA layers is physically impossible because it requires fractional head sharding (2 KV heads / 8 devices = 0.25 heads per device); replicating heads instead duplicates the KV cache memory footprint across all devices, which capped real-world concurrency at roughly 200 requests instead of the planned 512
- **Evidence**: Direct technical explanation of the sharding constraint and
  its measured concurrency consequence, in Section 3.
- **Confidence**: settled (a concrete hardware/memory-arithmetic constraint,
  independently verifiable: 2 KV heads cannot be evenly divided across 8
  devices; the ~200-vs-512 concurrency gap is stated as an observed,
  specific result of this constraint, not a projection)
- **Quote**: "However, attempting to shard the GQA layers with a tensor parallelism size of 8 (TP=8) forces fractional head sharding (2/8 = 0.25 heads per device), which is physically impossible on hardware. Replicating the heads locally across 8 cores duplicates the physical KV cache memory footprint on every device, neutralizing the memory-saving benefits of GQA. This memory redundancy severely restricts the HBM headroom available for active KV caches under high-load workloads. This capacity limitation forces the server engine to cap the actual achieved concurrency far below expected targets—limiting the system to roughly ~200 concurrent requests instead of the planned 512."
- **Our assessment**: This is the report's clearest concrete failure-to-fix
  narrative: a specific, named baseline approach (TP=8) is shown to be
  mathematically infeasible for this specific model's GQA head count, with
  a measured concurrency shortfall as the symptom, motivating the hybrid
  DP+EP redesign described in Claim 5. The arithmetic (2/8=0.25) is
  independently checkable and not just an assertion.

### Claim 5: The team replaced tensor parallelism with a hybrid sharding scheme — 8-way "Attention Batch Sharding" (Data Parallelism, DP=8) for attention layers combined with 8-way Expert Parallelism (EP=8, 64 of 512 experts per device) for the MoE feed-forward layers — which eliminates the KV-cache duplication problem while avoiding replicating the full 400GB parameter footprint across all devices
- **Evidence**: Direct description of the co-designed sharding scheme,
  referencing an internal PR by number.
- **Confidence**: settled (a specific, named architectural solution with a
  stated mechanism for why it resolves the Claim 4 constraint)
- **Quote**: "To eliminate this bottleneck, we co-designed a hybrid sharding scheme (PR #2577): 8-way Attention Batch Sharding (Data Parallelism, DP=8) combined with 8-way Expert Parallelism (EP=8) in the MoE layers. Replicating GQA and GDN weights across all 8 devices allows each core to process attention locally with the full 2 KV heads, preserving local KV cache consistency and eliminating intra-attention sharding communication. In the feed-forward MoE layers, we switch to Expert Parallelism (EP=8). The 512 routed experts are distributed evenly (64 experts per device)."
- **Our assessment**: This is a genuinely reusable pattern for anyone serving
  MoE models with a small, non-power-of-two-friendly KV head count: shard
  attention and MoE layers along *different* axes (DP for attention,
  EP for experts) rather than forcing one uniform parallelism scheme across
  the whole model. This is the report's single most transferable systems-
  engineering insight, independent of the specific model or hardware.

### Claim 6: The team chose a "Full Token Replication" MoE routing pipeline (All-Gather → local MoE → Reduce-Scatter) over an "All-to-All Shuffling" pipeline, explicitly trading higher local memory consumption for deterministic latency, because unpredictable All-to-All network routing overhead under variable workloads was judged unacceptable for production serving
- **Evidence**: Direct comparison of the two design options considered, with
  the stated rationale for the choice, in Section 3.
- **Confidence**: settled (a specific, named design decision with an
  explicitly stated trade-off rationale, not merely an outcome)
- **Quote**: "Option A (All-to-All Shuffling): ...this incurs massive, unpredictable network routing overhead due to global All-to-All steps under variable workloads. Option B (Full Token Replication): ...This completely bypasses the unpredictable All-to-All routing penalties at the cost of higher local memory consumption. Because deterministic latency is critical for real-world serving, we opted for Option B."
- **Our assessment**: This is a clean, explicit example of prioritizing
  latency predictability over raw efficiency for a production serving
  system — a design trade-off documented with its rejected alternative
  named and reasoned through, rather than presented as an obviously-correct
  choice. Worth noting as a general principle (deterministic latency over
  minimal compute) even outside the TPU/MoE-specific context.

### Claim 7: Coarsening the KV cache page/block size from 16 tokens to 256 tokens reduced decode-step latency under 512 concurrency from 428µs to 283µs — a 33.8% kernel-level speedup — because smaller block sizes caused Vector Processing Unit indexing-stall overhead on TPU hardware
- **Evidence**: A specific before/after latency measurement tied to a single,
  named configuration change (`--block-size=256`), in Section "Attention
  Track: Ragged Page Attention."
- **Confidence**: settled (a specific, reproducible measurement with an
  exact before/after latency figure and the exact server flag that produced
  it)
- **Quote**: "Historically, a block size of 16 tokens was used to minimize memory fragmentation. However, on TPU, smaller block sizes result in massive indexing overhead, causing the Vector Processing Unit (VPU) to stall during the decode phase. We resolved this by coarse-graining the indexing to a KV page size of 256 (enabled via the server command --block-size=256). This coarse-grained indexing reduced the decode step latency under Concurrency-512 from 428µs to 283µs, achieving a 33.8% kernel-level speedup."
- **Our assessment**: This is the single most concrete, reproducible
  micro-optimization in the report — a one-flag configuration change with
  an exact latency delta, in contrast to most of the other claims which
  describe custom kernel engineering that isn't a simple flag flip. It's
  also a specific counter-example to a general "smaller block size is
  always better for fragmentation" intuition carried over from GPU/CPU
  memory-management practice — the TPU's VPU indexing overhead inverts that
  intuition at this hardware layer.

### Claim 8: Empirically, the optimized stack achieved 3,707 tokens/s/chip for prefill-heavy workloads (82.4% of the estimated 4,500 tokens/s/chip discounted roofline limit) and 677 tokens/s/chip for decode-heavy workloads (79.6% of the estimated 850 tokens/s/chip discounted roofline limit), at the baseline 64-concurrency tier
- **Evidence**: Empirical throughput results compared directly against the
  paper's own first-principles roofline model, in Section 6.
- **Confidence**: emerging (the roofline *ceiling* figures are the authors'
  own theoretical model, not an independently derived hardware spec — so the
  "82.4%/79.6% of roofline" framing depends on trusting the authors' roofline
  math as well as their measured throughput; both halves of the ratio come
  from the same first-party source)
- **Quote**: "Under the 8K/1K prefill-heavy workload, our JAX serving stack delivers an actual throughput of 3,707 tokens/s/chip. Compared to our estimated prefill roofline limit of 4,500 tokens/s/chip (discounted), our custom SparseCore and TensorCore co-designed GEMMs successfully extract 82.4% of the absolute compute capacity of the TPU v7 TensorCores... Under the 1K/8K decode-heavy workload, our stack delivers an actual throughput of 677 tokens/s/chip. Compared to our memory-bound decode roofline limit of 850 tokens/s/chip (discounted), our Ragged Page Attention (RPA) and Gated DeltaNet (GDN) fusions successfully achieve 79.6% of the theoretical HBM bandwidth limit."
- **Our assessment**: Reporting measured throughput as a percentage of a
  self-derived roofline (rather than only as a raw tokens/s number, or only
  as a multiplier over an undisclosed baseline) is methodologically more
  transparent than Claim 2's bare "3.1x/4.7x" framing, since it at least
  shows the ceiling being measured against. Still self-reported and
  unverified by any third party, so treated as emerging rather than settled.

### Claim 9: The team implemented a dedicated "Numerical Verification Layer" to audit FP8-quantized gating/routing kernels against a high-precision Float32 reference path, and reports zero deviation between the two — treating correctness verification as a first-class deliverable alongside throughput
- **Evidence**: Dedicated subsection ("Rigorous Numerical Verification &
  Correctness") describing the verification methodology and its result,
  referencing two internal PRs by number.
- **Confidence**: emerging (a specific, named verification practice with a
  stated "zero deviation" result, but the precise statistical definition of
  "zero deviation" — e.g., what tolerance, over what token/expert-load
  distribution — is not given in the extracted text)
- **Quote**: "In designing our custom JAX/Pallas gating kernels, the systems engineering team incorporated a dedicated Numerical Verification Layer to audit accumulation precision across our FP8 scaling blocks. By continuously monitoring the softmax distribution ranges and expert load balances, we verified that our Pallas-lowered gating weights maintain zero deviation from the high-precision Float32 reference path (see PR #2328 and PR #2674), guaranteeing high throughput alongside strict output quality."
- **Our assessment**: This is a notable process claim distinct from the
  performance claims elsewhere in the post: it demonstrates that the team
  treated low-precision kernel correctness as something to actively verify
  and monitor (via a continuous check against a reference path), not merely
  assume works because throughput improved. This is a transferable
  verification pattern for anyone building custom low-precision kernels —
  test output distribution against a known-correct high-precision reference,
  continuously, not just once at kernel-authoring time.

### Claim 10: TPU v7 (Ironwood) provides 192GB of HBM per chip, versus 288GB on Nvidia's Blackwell GB300 GPUs — a roughly 50% capacity difference the team names as a "severe systems constraint" motivating a custom hybrid memory layout for GDN recurrent state and GQA KV cache
- **Evidence**: Direct hardware comparison statement in Section "Memory
  Track: Hybrid Attention KV Layout Optimization," with a named competing
  hardware platform and specific capacity figures for both.
- **Confidence**: settled (a specific, named, independently checkable
  hardware specification comparison between two publicly documented
  accelerator platforms)
- **Quote**: "Because the TPU v7 features 192GB of HBM capacity per chip (e.g. compared to the 288GB available on Blackwell GB300 GPUs - a ~50% capacity difference), HBM footprint optimization under high concurrency is a severe systems constraint. In PR #2416, we introduced a custom memory layout designed to align and store these hybrid attention states together in HBM."
- **Our assessment**: This is the single instance in the post where Google
  explicitly names and quantifies a hardware disadvantage relative to a
  competitor platform (Nvidia), rather than presenting TPU v7 purely as a
  strength — a notably candid disclosure for a first-party vendor post, and
  the direct motivation for the custom memory-layout optimization it then
  describes.

### Claim 11: The team consolidated three separate All-Gather collective operations (token hidden-state vectors, expert routing indices, and gating weights) down to two, by bitcasting and packing the integer routing indices and float gating weights — which share identical tensor shapes — into a single dense 32-bit blob transmitted in one collective call
- **Evidence**: Named technique ("The 3-to-2 All-Gather Optimization") with
  the specific tensor shapes and packing mechanism described, referencing an
  internal PR by number.
- **Confidence**: settled (a concrete, specific bit-packing technique with
  named tensor shapes, independently understandable and checkable as a
  general communication-fusion pattern regardless of this model/hardware)
- **Quote**: "Because the expert indices (integers) and the topk weights (floats) share identical tensor shapes ([1024,10]), we stack, bitcast, and pack them together along a new dimension into a single dense 32-bit integer array (blob). This allows us to run a single All-Gather across the data dimension ... for both routing metadata blocks, unpacking them locally and halving the routing metadata collective latency."
- **Our assessment**: This is a generalizable distributed-systems trick
  independent of ML specifics: when two same-shaped tensors of different
  logical types must be broadcast together, bitcast-and-pack them into one
  buffer to halve the number of collective calls (each of which carries
  fixed launch/sync latency). Reusable well beyond MoE routing.

## Concrete Artifacts

### Hierarchical Reduce-Scatter design (verbatim from the post)

```
"After expert execution, token outputs must return to their data-parallel
ranks. A standard All-Reduce over the 8-device mesh is highly inefficient.
We replaced this with a custom, TPU-native Hierarchical Reduce-Scatter
written in Pallas/Mosaic (see PR #2679). The collective runs in two
pipelined phases:

Intra-chip Reduce-Scatter: Logical chiplets on the same physical chip
exchange and sum their data using fast, local shared-memory transfers
(which are 6x faster than chip-to-chip ICI bandwidth).

Inter-chip Reduce-Scatter: Partially reduced data is exchanged across
physical chips using a recursive-doubling hypercube algorithm over the
TPU's physical ICI links.

To prevent VMEM Out-of-Memory (OOM) errors, the data is sliced into 2 to 4
micro-batches. The kernel pipelines remote DMA transfers of micro-batch i
while the TensorCore is performing vector additions for micro-batch i-1,
hiding the communication latency behind the compute."

Source: developers.googleblog.com/systems-engineering-playbook-optimizing-qwen-35-397b-moe-on-ironwood-tpu7x/,
Section 3, "2. Hierarchical Reduce-Scatter"
```

### Ironwood (TPU v7) hardware specifications and roofline inputs (verbatim from the post)

```
"Tensor Core (TC) Frequency: 2.2 GHz
Tensor Cores per chip: 2
MXUs (Matrix Execution Units) per TC: 2 (total 4 MXUs per chip)
Peak BF16 performance: 2,307 TFLOPS/chip ((262,144 FLOP/cycle/MXU x 2.2 GHz
x 4 MXUs = 2,307 TFLOPS))
Peak FP8 performance: 4,614 TFLOPS/chip"

Source: developers.googleblog.com/systems-engineering-playbook-optimizing-qwen-35-397b-moe-on-ironwood-tpu7x/,
Section 4, "Ironwood Hardware Specifications"
```

### Custom Pallas kernel inventory by execution track (verbatim from the post)

```
"Attention Track: PR #1820 (RPA v3) and PR #1961 (Batched RPA)
MoE Track: PR #1688 (GMM v2) and PR #2137 (SparseCore Ragged Gather)
GDN Track: PR #2149 (Chunked GDN) and PR #3016 (Fully-Fused Conv1D and
Recurrent / Chunked GDN)"

Source: developers.googleblog.com/systems-engineering-playbook-optimizing-qwen-35-397b-moe-on-ironwood-tpu7x/,
"Kernel Optimizations" section
```

### Benchmark topology and serving-engine configuration (verbatim from the post)

```
"Accelerator Topology: A single physical host housing 4 physical Ironwood
chips. Each physical chip is composed of 2 logical chiplets, exposing a
logical topology of 8 distinct execution cores (devices) interconnected via
a high-speed, sub-microsecond Inter-Chip Interconnect (ICI) plane.

Inference Server Engine: Engineered using vllm-project/tpu-inference. For
the final optimized runs utilizing Attention DP, the server execution loop
was configured with --max-num-batched-tokens=1024 and --max-num-seqs=64 per
core (compared to --max-num-batched-tokens=8192 and --max-num-seqs=512
utilized in early tensor-parallel baselines)."

Source: developers.googleblog.com/systems-engineering-playbook-optimizing-qwen-35-397b-moe-on-ironwood-tpu7x/,
Section 2, "Mixed-Engine Orchestration & Topology"
```

## Cross-References

- **Corroborates**: `blog-google-litertjs-web-ai-inference.md` and
  `blog-google-tunix-gemma-reasoning-hackathon.md` in the general pattern
  that Google's first-party technical blog posts pair specific vendor-
  reported performance multipliers (this post's 3.1x/4.7x, LiteRT.js's 3x
  and 5-60x figures) with genuinely concrete, independently checkable
  supporting technical detail (named PRs, exact latency deltas, exact
  hardware specs) — consistent with this corpus's general treatment of
  first-party vendor performance claims as directionally credible but
  unverified (`emerging`/`anecdotal`), while treating the surrounding
  architecture/mechanism descriptions as `settled` where independently
  checkable.
- **Contradicts**: None identified. No existing source note makes a claim
  about Qwen 3.5's architecture, TPU v7/Ironwood inference performance, or
  DP+EP MoE sharding strategy that this post's claims oppose.
- **Extends**: `blog-google-tunix-gemma-reasoning-hackathon.md` (the
  corpus's only other TPU-focused Google Developers Blog post): that note
  covers TPU v5e used for *training* (RL post-training of small Gemma
  models on a single free Kaggle pod), while this post covers TPU v7
  (Ironwood) used for *inference serving* of a much larger (397B) MoE
  model. Together the two notes give the corpus one data point each on
  TPU-based training and TPU-based inference-serving optimization, though
  neither maps directly onto this guide's actual scope (see Guide Impact).
  `blog-thoughtworks-lovin-gall-local-inference-boundary.md` Claim 1
  documents "instruction-following pruning" as a sparse-activation
  technique for on-device serving (activating 1-4B of 20B parameters
  per task); this post's Claim 3 (17B of 397B parameters activated per
  token via MoE routing) is architecturally distinct — MoE routing
  activates different experts per token from a fixed, trained sparsity
  pattern, whereas IFP dynamically swaps parameter subsets from flash based
  on task type — but both are instances of the same broader "activate only
  a task-relevant subset of a larger parameter set" family of techniques,
  worth noting together if the guide ever covers sparse-activation
  architectures as a category.
- **Novel**: This is the corpus's first source documenting: (1) Qwen 3.5's
  architecture in any detail (hybrid GDN/GQA layout, 512-expert MoE, native
  1M+-token context via YaRN scaling); (2) TPU v7 ("Ironwood") inference-
  serving hardware specifications and roofline methodology; (3) the
  hybrid Data-Parallelism + Expert-Parallelism sharding pattern for MoE
  models with small, non-power-of-two-friendly KV head counts; (4) any
  named Pallas/Mosaic custom-kernel engineering detail; (5) a first-party
  vendor's numerical-verification-layer practice for low-precision (FP8)
  kernel correctness auditing.

## Guide Impact

- **No direct chapter impact identified.** This guide (per `guide/*.md`
  chapter headers: 00-principles, 01-daily-workflows, 02-harness-engineering,
  03-verification, 04-context-engineering, 05-team-adoption,
  06-security-threat-model) is about the practice of AI-assisted software
  engineering — CLAUDE.md/harness design, multi-agent workflows,
  verification of AI-generated code, context management, team adoption, and
  security. This source is an ML-serving systems/kernel engineering report
  about optimizing raw inference throughput for a large MoE model on
  specialized accelerator hardware. It contains no claims about coding
  agents, AI-assisted development workflows, or engineering practices for
  building *with* AI models — only practices for optimizing the *serving
  infrastructure underneath* a model. The Prospector's three triage
  comments proposed several chapter mappings (Ch07 Infrastructure & Platforms,
  Ch03 inference patterns, Ch04 scaling distributed systems, Ch02 Harness
  Engineering) that do not correspond to this guide's actual chapter
  structure (confirmed by reading `guide/*.md` headers directly) — same
  discrepancy already flagged in `blog-google-litertjs-web-ai-inference.md`'s
  Extraction Notes for a different issue's triage comments.
- **Weakest possible connection, flagged rather than forced**: If the guide
  ever adds content on the economics/performance characteristics of
  self-hosting or fine-tuning open-weights models for agentic-coding
  workloads (a topic currently touched only tangentially via
  `blog-fowler-boeckeler-local-models-viability.md`'s RAM-constraint
  discussion), this post's DP+EP sharding pattern (Claim 5) and KV-cache
  block-size tuning result (Claim 7) would be relevant background for
  understanding why large MoE models are expensive/complex to serve at
  scale — but this guide does not currently have such a section, and this
  source alone does not justify adding one.

## Extraction Notes

- **Verified the source is real and live before extraction.** The article's
  subject matter (Google publicly detailing systems-engineering work to
  optimize a competitor's — Alibaba's Qwen — open-weights model on Google's
  own TPU hardware) initially read as suspicious enough to warrant
  independent verification, especially since the first WebFetch pass
  returned only a paraphrased summary rather than source text. Fetched the
  raw page HTML directly via `curl` (HTTP 200, ~71KB response, matching
  `<title>`/`<h1>`/JSON-LD `Article` schema metadata all internally
  consistent with the claimed headline, author, and July 14, 2026 publish
  date) and stripped markup with a Python script to obtain the full
  character-for-character article text before extracting any quotes. All
  quotes in this note are taken from that raw-HTML text, not from the
  WebFetch summarizer's paraphrase.
- **No sub-pages followed.** The post links to a Hugging Face model
  repository and two third-party explainer articles (a Hugging Face blog
  post and a Sebastian Raschka post on Gated DeltaNet), but these support
  only the architecture background in Claim 3, which the post itself
  states in sufficient, checkable detail without needing the linked
  explainers.
- **Existing overlap checked before writing.** Searched all
  `source-notes/*.md` for "TPU", "Ironwood", "MoE", "Mixture-of-Experts",
  "JAX", "Pallas", "vLLM", "SGLang", "roofline", and "Qwen" before drafting.
  Found one topically-adjacent Google/TPU note
  (`blog-google-tunix-gemma-reasoning-hackathon.md`, TPU v5e *training*,
  not inference) and no note covering Qwen's architecture, MoE sharding, or
  TPU v7/Ironwood specifically — confirmed net-new coverage, addressed in
  Cross-References.
- **Confidence rationale**: Set to `emerging` overall. The architecture
  description (Claim 3), the sharding-infeasibility arithmetic (Claim 4),
  the sharding redesign (Claim 5), the design-trade-off rationale (Claim 6),
  the specific reproducible latency measurement (Claim 7), the hardware
  comparison (Claim 10), and the bit-packing technique (Claim 11) are all
  concrete, specific, and independently checkable claims (rated `settled`
  individually). The headline performance multipliers (Claim 2) and the
  roofline-percentage framing (Claim 8) remain self-reported, unverified-by-
  a-third-party vendor benchmarks (rated `anecdotal`/`emerging`
  individually) — consistent with how this corpus treats other first-party
  Google performance-benchmark posts. The overall `emerging` rating reflects
  that mix: mechanism claims are strong, headline performance claims are not
  independently verified.
- **Off-topic relative to this guide's scope, flagged explicitly rather than
  force-fit.** Per MINER.md's instruction to be specific about guide impact
  rather than vaguely gesture at relevance, this note states plainly in
  Guide Impact that the source has no direct chapter mapping, rather than
  inventing a connection to justify the extraction effort. The extraction
  itself remains thorough per MINER.md's requirement to read deeply
  regardless of eventual guide relevance.
