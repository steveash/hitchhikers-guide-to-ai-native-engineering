---
source_url: https://cursor.com/blog/mixture-of-kittens
source_type: blog-post
title: "Mixture-of-Kittens: MoE Megakernel for NVL72s"
author: "Stuart Sul, Nash Brown, Henry Wildermuth, William Lin & Federico Cassano (Cursor Research)"
date_published: 2026-08-04
date_extracted: 2026-08-05
last_checked: 2026-08-05
status: current
confidence_overall: emerging
issue: "#2501"
---

# Mixture-of-Kittens: MoE Megakernel for NVL72s (Cursor Research)

> Cursor Research open-sources "Mixture-of-Kittens" (MoK), a deterministic MoE
> training megakernel for NVIDIA GB300 NVL72 GPUs that fuses expert dispatch/combine
> communication and expert computation into a single kernel — eliminating CPU-GPU
> synchronization points and delivering up to 2.37x forward throughput and 1.41x
> end-to-end training speedup over a DeepEP-based baseline at 512-GPU production scale.

## Source Context

- **Type**: blog-post (Cursor Research technical release, published August 4, 2026,
  accompanied by an open-source GitHub repository with benchmark code)
- **Author credibility**: Five named Cursor Research authors, including Federico Cassano,
  who also co-authored `blog-cursor-warp-decode.md` and contributed to
  `blog-cursor-composer2-technical-report.md` — giving him a consistent publication track
  record on Cursor's ML systems/kernel work. Unlike the warp-decode post (proprietary,
  undisclosed source) or the Composer 2 technical report's kernels (internal-only), this
  release ships as open-source code (`github.com/cursor/mixture-of-kittens`) with full
  benchmark code included, which raises the verifiability bar considerably — third parties
  can run the claimed benchmarks themselves rather than trusting first-party numbers alone.
  Commercial incentive to present favorably still exists (Cursor benefits from being seen
  as an infrastructure leader), but the open-source release constrains exaggeration more
  than a narrative-only blog post would.
- **Scope**: Covers one specific system: a GPU megakernel for MoE *training* on NVIDIA
  Blackwell GB300 NVL72 hardware, covering forward/backward dispatch-combine communication,
  computation-communication overlap tuning, ring buffer token handling, and MXFP8 mixed
  precision. Does NOT cover: inference/decode (contrast with `blog-cursor-warp-decode.md`,
  which covers the decode stage), model architecture or training recipe (contrast with
  `blog-cursor-composer2-technical-report.md`), Cursor's product, or any harness/agent
  patterns for practitioners.

## Extracted Claims

### Claim 1: MoK achieves up to 2.37x faster MoE forward throughput and 1.41x end-to-end training speedup versus existing public implementations

- **Evidence**: Headline result stated in the executive summary and confirmed by the
  README. End-to-end figure is measured from a 512-GPU production training run comparing
  against a DeepEP-based baseline.
- **Confidence**: emerging (first-party benchmark, but code and benchmark harness are
  open-sourced, allowing independent reproduction — stronger evidentiary footing than a
  purely narrative vendor claim)
- **Quote**: "achieving up to 2.37x faster forward throughput than existing public
  implementations and delivering 1.41x end-to-end training speedup"
- **Our assessment**: The 2.37x figure is a per-layer microbenchmark ceiling (see Claim 6);
  the 1.41x figure is the more practically meaningful number because it is measured at
  512-GPU production scale, where communication overhead, imbalance, and other bottlenecks
  typically erode microbenchmark gains. A 1.41x end-to-end speedup surviving from a 2.37x
  layer-level ceiling suggests the MoE communication/computation fusion is a genuine
  bottleneck in current training pipelines, not a narrow edge case.

### Claim 2: Pull-based forward dispatch delivers up to 29% higher NVLink bandwidth utilization than push-based dispatch under expert-imbalance conditions

- **Evidence**: Direct comparison of communication direction strategies: MoK uses
  pull-based dispatch for the forward pass and push-based combine for the backward/combine
  step, based on measured bandwidth utilization differences.
- **Confidence**: emerging (specific quantitative comparison; the imbalance condition
  under which the 29% figure holds is not further specified — e.g., what imbalance ratio)
- **Quote**: "pull-based communication delivers 'up to 29% higher NVLink bandwidth
  utilization' compared to push-based approaches under expert imbalance conditions"
- **Our assessment**: Expert imbalance (some experts receiving disproportionately more
  tokens than others) is an intrinsic property of MoE routing, not an edge case — so this
  result generalizes to any real MoE training workload rather than a synthetic best case.
  The choice to use *different* communication directions for dispatch vs. combine (pull
  for one, push for the other) rather than a single uniform strategy is the more
  transferable design insight: communication direction should be chosen per-operation
  based on its imbalance characteristics, not applied uniformly across a pipeline.

### Claim 3: Push-based dispatch signaling incurs roughly 5.8x higher latency than pull-based dispatch signaling (103µs vs. 18µs)

- **Evidence**: Direct latency measurement comparing signaling overhead between the two
  dispatch strategies.
- **Confidence**: emerging (specific first-party microbenchmark number; no hardware/config
  context given beyond the general NVL72 setting)
- **Quote**: "push-based dispatch signalling incurs roughly 5.8x higher latency than
  pull-based dispatch signalling, at 103 µs versus 18 µs"
- **Our assessment**: This is the quantitative backing for the dispatch-direction choice
  in Claim 2. A 5.8x signaling latency gap is large enough to dominate small-message
  communication patterns typical of MoE token dispatch, where many small transfers occur
  per training step. Combined with Claim 2, this establishes pull-based dispatch as the
  clearly superior choice specifically for the forward dispatch operation under MoE's
  characteristic small-message, imbalanced-load communication pattern.

### Claim 4: The optimal computation-communication overlap granularity for Kimi 2.5-scale MoE layers on Blackwell is T≥2368 tokens per minibatch, with measured performance peaking around 2,560 tokens at 3.425ms runtime

- **Evidence**: Microbenchmark sweep across minibatch token counts, targeting Kimi 2.5
  model specifications (hidden dim H=7168, intermediate dim I=2048).
- **Confidence**: emerging (specific, model-shape-dependent microbenchmark result — the
  threshold is derived for one model configuration and may not transfer directly to other
  hidden/intermediate dimension ratios)
- **Quote**: "they determined T≥2368 tokens per minibatch on Blackwell GPUs. Microbenchmarks
  showed performance peaked around 2,560 tokens, achieving 3.425ms runtime"
- **Our assessment**: This is a concrete instance of the general "neither fine-grained nor
  coarse-grained overlap is optimal — there's a sweet spot" principle. The specific token
  count is tied to Kimi 2.5's shape (H=7168, I=2048) and Blackwell hardware, so it is not
  directly portable to other model architectures, but the *methodology* — sweep minibatch
  granularity and measure the crossover point where compute fully hides communication
  latency — is the transferable pattern for teams tuning their own MoE training kernels.

### Claim 5: Ring token buffers (macrobatching) eliminate CPU-GPU synchronization by using fixed-size ring buffers that cycle at minibatch granularity, handling dynamic token counts without exact pre-allocation

- **Evidence**: Architectural description of the ring buffer mechanism; the backward pass
  uses reversed ring traversal specifically to minimize forward activation replay overhead.
- **Confidence**: emerging (first-party architectural description; the mechanism is
  technically coherent with known GPU kernel design patterns for dynamic-shape workloads)
- **Quote**: "MoK eliminates CPU-GPU synchronization by implementing fixed-size ring
  buffers cycling at minibatch granularity. This handles dynamic token counts without exact
  pre-allocation. The backward pass uses reversed ring traversal to minimize forward
  activation replay overhead."
- **Our assessment**: This directly addresses a known MoE-specific pain point: expert
  routing produces a dynamic, data-dependent number of tokens per expert per step, which
  conventionally forces a CPU-GPU synchronization point to read back token counts before
  allocating buffers. Fixed-size ring buffers sidestep this by never requiring an exact
  count — a design choice that trades a small amount of buffer over-provisioning for the
  removal of a synchronization stall on every step. This is architecturally analogous to
  `blog-cursor-warp-decode.md`'s buffer-elimination strategy for inference decode, but
  applied to the training-time token-routing problem instead of the inference-time
  expert-computation problem.

### Claim 6: MXFP8 mixed-precision training keeps shared experts in BF16 for stability, with quantization fused directly into dispatch operations and expert GEMMs

- **Evidence**: Architectural description of the precision strategy: routed/regular
  experts train in MXFP8, shared experts remain BF16, and the quantization step is fused
  into the dispatch and GEMM kernels rather than run as a separate pass.
- **Confidence**: emerging (first-party design description; fusing quantization into
  existing kernel stages rather than adding a separate pass is a standard technique for
  minimizing memory traffic, consistent with prior Cursor kernel work)
- **Quote**: "Mixed-precision training operates in MXFP8 mode with shared experts remaining
  in BF16 for stability. Quantization is fused into dispatch operations and expert GEMMs."
- **Our assessment**: This selective-precision approach (some experts get low precision,
  a stability-critical subset stays higher precision) parallels the asymmetric precision
  choice in `blog-cursor-composer2-technical-report.md` Claim 9 (NVFP4 forward / MXFP8
  backward for RL training) — both sources show Cursor treating precision as a per-role
  design variable rather than a uniform setting across the whole model. Fusing
  quantization into existing GEMM/dispatch kernels (rather than a standalone conversion
  pass) avoids an extra read-modify-write round trip through GPU memory, which is the same
  class of optimization as buffer elimination in Claim 5.

### Claim 7: Per-layer MoE benchmarks on GB300 NVL72 (EP degree 64) show speedups ranging from 1.58x to 2.37x depending on precision mode and pass direction

- **Evidence**: Four measured configurations: MXFP8 forward 2.37x, MXFP8 backward 1.78x,
  BF16 forward 1.92x, BF16 backward 1.58x, all versus the fastest available baseline
  implementation at expert-parallelism degree 64.
- **Confidence**: emerging (specific first-party microbenchmark table; reproducible via
  the open-sourced benchmark code)
- **Quote**: "MXFP8 forward: up to 2.37x faster than fastest baseline; MXFP8 backward:
  1.78x faster; BF16 forward: 1.92x faster; BF16 backward: 1.58x faster"
- **Our assessment**: The consistent pattern — forward passes gain more than backward
  passes, and MXFP8 gains more than BF16 — suggests the megakernel fusion advantage is
  largest where communication-bound stages coincide with lower-precision compute (the
  MXFP8 forward case). The backward pass, doing more compute per byte transferred (gradient
  accumulation, activation replay), sees smaller relative gains because computation was
  already a larger share of the critical path there.

### Claim 8: In 512-GPU production training, MoK improved effective throughput from 760.9 to 1,070.2 tokens/second/GPU versus a DeepEP-based baseline (1.41x)

- **Evidence**: Direct production measurement at 512-GPU scale, the largest and most
  practically relevant data point in the source (vs. the per-layer microbenchmarks in
  Claim 7, which isolate the kernel from other pipeline effects).
- **Confidence**: emerging (first-party production measurement; DeepEP is a real,
  independently known open-source MoE communication library, making the baseline
  identifiable and the comparison checkable by anyone familiar with DeepEP's public
  benchmarks)
- **Quote**: "Previous DeepEP-based: 760.9 tokens/second/GPU; MoK: 1,070.2 tokens/second/GPU;
  Improvement: 1.41x speedup"
- **Our assessment**: Naming DeepEP specifically (rather than an unnamed "existing
  baseline") is a credibility-strengthening detail — DeepEP is a well-known, publicly
  documented open-source MoE dispatch/combine library, so the comparison is falsifiable
  in principle by anyone who benchmarks DeepEP on comparable hardware. This is the single
  most load-bearing metric in the source for practitioners: it is measured at the scale
  (512 GPUs, full training pipeline) that matters for real MoE training cost, not an
  isolated kernel microbenchmark.

### Claim 9: MoK was validated against four different production-scale MoE architecture specifications spanning a wide range of expert counts and top-k routing

- **Evidence**: Four named model shapes tested: Kimi K2.7 Code (384 experts, H=7168,
  I=2048, top-k 8), GLM-5.2 (256 experts, H=6144, I=2048, top-k 8), Qwen3.5-397B-A17B
  (512 experts, H=4096, I=1024, top-k 10), DeepSeek-V4-Pro (384 experts, H=7168, I=3072,
  top-k 6), all benchmarked against DeepSeek-V3-style MoE layer baselines.
- **Confidence**: emerging (specific, named model shapes; testing against multiple
  production-representative architectures rather than a single synthetic configuration
  strengthens the generality claim)
- **Quote**: "The researchers evaluated against DeepSeek-V3-style MoE layers using: Kimi
  K2.7 Code (E: 384, H: 7168, I: 2048, top-k: 8), GLM-5.2 (E: 256, H: 6144, I: 2048,
  top-k: 8), Qwen3.5-397B-A17B (E: 512, H: 4096, I: 1024, top-k: 10), DeepSeek-V4-Pro
  (E: 384, H: 7168, I: 3072, top-k: 6)"
- **Our assessment**: Testing across four architecturally distinct MoE configurations
  (expert counts from 256 to 512, top-k from 6 to 10, differing hidden/intermediate
  dimensions) is meaningful evidence that the throughput gains are not an artifact of
  tuning to one specific model shape. This matters because MoE architectures vary widely
  across labs, and a kernel optimized narrowly for one shape would be far less valuable
  to the broader ecosystem than one shown to generalize across shapes.

### Claim 10: MoK's open-source release provides a two-layer API (low-level `ops` and higher-level `functional`) with five tunable hyperparameters and automatic workspace caching via PyTorch symmetric memory

- **Evidence**: GitHub README describes the API architecture: `mok/ops.py` (direct kernel
  access, minimal overhead, manual coordination) and `mok/functional.py` (workspace
  management and kernel coordination handled automatically, recommended for production).
  Tunable parameters: `fwd_num_comm_sms`/`bwd_num_comm_sms` (4-52 SMs recommended),
  `minibatch_size` (2048-16384 recommended), `macrobatch_size`, `schedule_capacity_multiplier`
  (default 0.5). Workspace management via `get_workspace()` (auto-caching) and
  `create_workspace()` (manual lifetime).
- **Confidence**: settled (directly observable from the public README/API surface, not a
  performance claim requiring independent verification)
- **Quote**: "Ops Layer (`mok/ops.py`): Low-level direct CUDA kernel access with minimal
  overhead... Functional Layer (`mok/functional.py`): Higher-level API handling workspace
  management and kernel coordination; recommended for production"
- **Our assessment**: This is the practitioner-actionable part of the release: unlike
  `blog-cursor-warp-decode.md` (described but never released) or the Composer 2 technical
  report's training kernels (internal-only infrastructure), MoK ships as installable,
  documented, open-source code with a tunable parameter surface. A team building their own
  MoE training pipeline on Blackwell hardware could adopt this directly rather than only
  learning from the design principles secondhand. This is the key practitioner-relevance
  differentiator versus Cursor's other kernel-engineering blog posts in our corpus.

## Concrete Artifacts

### Performance Summary Table

```
# Mixture-of-Kittens performance (Cursor Research, August 2026)
# Source: https://cursor.com/blog/mixture-of-kittens

Individual MoE Layer Benchmarks (GB300 NVL72, EP degree 64):
  MXFP8 forward:   up to 2.37x faster than fastest baseline
  MXFP8 backward:  1.78x faster
  BF16 forward:    1.92x faster
  BF16 backward:   1.58x faster

End-to-End Production Results (512 GPUs, vs. DeepEP baseline):
  Previous DeepEP-based:  760.9 tokens/second/GPU
  MoK:                   1,070.2 tokens/second/GPU
  Improvement:            1.41x speedup

Communication Direction Comparison:
  Pull-based dispatch:  up to 29% higher NVLink bandwidth utilization
                         vs. push-based, under expert imbalance
  Signaling latency:    pull-based 18 µs vs. push-based 103 µs (5.8x)

Overlap Tuning (Kimi 2.5 shape, H=7168, I=2048, Blackwell):
  Minimum viable minibatch: T >= 2368 tokens
  Measured peak:            ~2,560 tokens, 3.425ms runtime
```

### Model Architectures Tested

```
# MoE architecture specs used for MoK validation
# Source: https://cursor.com/blog/mixture-of-kittens

Model                    Experts   Hidden(H)   Intermediate(I)   Top-k
Kimi K2.7 Code             384       7168           2048            8
GLM-5.2                    256       6144           2048            8
Qwen3.5-397B-A17B          512       4096           1024           10
DeepSeek-V4-Pro             384       7168           3072            6

Baseline: DeepSeek-V3-style MoE layers
```

### API and Configuration Surface

```
# MoK open-source API architecture
# Source: https://github.com/cursor/mixture-of-kittens (README)

REQUIREMENTS
  Hardware: NVIDIA Blackwell SM100/SM103 (GB200/GB300 NVL72)
  Python 3.12+, PyTorch 2.10+, CUDA 13.0+

API LAYERS
  mok/ops.py         - low-level direct CUDA kernel access, manual coordination
  mok/functional.py  - higher-level, automatic workspace/kernel coordination
                        (recommended for production)

TUNABLE HYPERPARAMETERS
  fwd_num_comm_sms / bwd_num_comm_sms  - comm SMs (recommended 4-52)
  minibatch_size                       - overlap granularity (recommended 2048-16384)
  macrobatch_size                      - ring buffer size for token handling
  schedule_capacity_multiplier         - worst-case routing fraction (default 0.5)

WORKSPACE MANAGEMENT
  PyTorch symmetric memory for inter-GPU buffers
  get_workspace()    - automatic caching across identical configs
  create_workspace() - manual lifetime management

PRECISION
  mxfp8_quantize() - prepares prequantized MXFP8 weights separately from kernel
                      execution (integrates with FSDP-style sharding)
```

## Cross-References

- **Corroborates**: `blog-cursor-warp-decode.md` (#207) — Both sources describe Cursor
  investing in custom, hand-written GPU kernels for MoE models on NVIDIA hardware rather
  than relying on general-purpose libraries. Warp decode targets the inference decode
  stage on B200; MoK targets the training stage on GB300 NVL72. Together they show Cursor
  maintaining a full custom-kernel portfolio across both training and inference for MoE
  models — the same "eliminate architectural overhead by rethinking the parallelism/
  synchronization strategy, not optimizing within it" principle (warp-decode Claim 11)
  appears again here: MoK's megakernel fusion eliminates a CPU-GPU sync point rather than
  optimizing around it, exactly analogous to warp decode eliminating pipeline stages
  rather than speeding them up.

- **Corroborates**: `blog-cursor-composer2-technical-report.md` (#194) — That report's
  Claim 9 documents an asymmetric-precision RL training kernel (NVFP4 forward / MXFP8
  backward) with a specific numerical-stability failure mode (divergence at ~100 steps
  without IEEE-compliant arithmetic). MoK's asymmetric precision design (Claim 6 here:
  MXFP8 for routed experts, BF16 for shared experts) is the same design pattern —
  precision as a per-role, not per-model, variable — applied to MoE megakernel training
  rather than RL forward passes. Both sources are Cursor Research kernel work on Blackwell-
  class hardware from the same technical culture.

- **Extends**: `blog-cursor-composer2-technical-report.md` (#194) Claim 16 — That report
  describes Cursor's asynchronous multi-region RL training infrastructure (Anyrun, 3 GPU
  regions, 4 CPU regions) without detailing the MoE communication kernel used inside that
  pipeline. MoK is a plausible candidate for (or a direct predecessor of) the MoE
  dispatch/combine kernel underlying that infrastructure, though the source does not
  explicitly state this connection — Composer's base model (Kimi K2.5, a 1.04T-parameter
  MoE) is exactly the class of model MoK is designed to train.

- **Contradicts**: None identified. No existing source note makes claims about MoE
  training-time communication kernels that this post would oppose.

- **Novel**: Compared to the existing corpus:
  - **Open-source release of a production training kernel**: no other Cursor kernel post
    in our corpus (`blog-cursor-warp-decode.md`, `blog-cursor-composer2-technical-report.md`)
    ships as installable open-source code with public benchmark code. This is the first
    corpus source where practitioners could directly adopt the described kernel rather
    than only learning the design principles.
  - **Communication-direction asymmetry (pull vs. push) as a tunable design axis**: no
    prior source documents choosing different communication directions for dispatch vs.
    combine based on measured bandwidth/latency characteristics under expert imbalance.
  - **Deterministic megakernel design**: bitwise-identical output regardless of hardware
    scheduling order is a stronger correctness guarantee than any prior kernel-engineering
    source in the corpus discusses; most prior sources (warp decode) report near-bitwise
    accuracy (cosine similarity >0.999996) rather than exact determinism.
  - **Ring-buffer token handling for training-time dynamic routing**: no prior source
    documents the training-side equivalent of the dynamic-token-count problem; warp decode
    addresses a related but distinct inference-side buffer elimination.

## Guide Impact

- **Chapter 00 (Principles — rethinking synchronization rather than optimizing it)**:
  Claim 5 (ring buffers eliminate CPU-GPU sync entirely, rather than making the sync
  faster) and the megakernel fusion strategy overall are a second, independent instance
  of the principle already extracted from `blog-cursor-warp-decode.md` Claim 11: the
  largest performance gains come from removing a synchronization or coordination point
  by redesigning the data flow, not from speeding up the existing coordination step.
  Two independent Cursor kernel-engineering teams arriving at the same meta-strategy
  (for different problems — inference decode vs. training communication) strengthens this
  as a portable principle worth citing with two examples rather than one.

- **Chapter 02 (Harness Engineering — model cost and capability cadence)**: This is
  training-side infrastructure, not something most AI-native engineering teams will
  operate directly (it requires GB300 NVL72 clusters), so — similar to the assessment in
  `blog-cursor-warp-decode.md`'s Extraction Notes — practitioner actionability is
  indirect. The relevant takeaway is economic: a 1.41x end-to-end training throughput
  improvement (Claim 8) at 512-GPU scale materially reduces the compute cost of training
  frontier MoE models. This is one more concrete data point (alongside warp-decode's
  inference-side 1.84x) for why frontier model prices continue to fall and capability
  iteration cadence continues to increase — vendors are compounding gains across both the
  training and inference stacks, not just one.

- **Chapter 04 (Context Engineering / Infrastructure — precision-as-a-design-variable)**:
  Claim 6's selective precision strategy (low precision for routed experts, higher
  precision for shared/stability-critical experts) is a specific, reusable instance of a
  pattern already emerging in the corpus via `blog-cursor-composer2-technical-report.md`
  (NVFP4 forward / MXFP8 backward). For any team implementing custom low-precision
  training or inference kernels: treat precision as a per-component variable tied to that
  component's sensitivity to quantization error, not a single global setting.

## Extraction Notes

- Primary source (cursor.com/blog/mixture-of-kittens) was fetched and read in full; it is
  a concise technical release post (~600-800 words equivalent) rather than a full paper.
  The linked GitHub repository (github.com/cursor/mixture-of-kittens) README was also
  fetched to extract the API/configuration surface (Claim 10, Concrete Artifacts), since
  the blog post itself does not describe the installable API in detail. No other linked
  sub-pages were followed; the source code itself (kernel implementation files) was not
  read line-by-line — this extraction covers the documented architecture and benchmarks,
  not a code-level audit of the CUDA implementation.
- All performance numbers are first-party but the accompanying open-source release with
  public benchmark code is a meaningfully stronger evidentiary position than a narrative-
  only vendor blog post — treat direction of claims with higher confidence than typical
  vendor posts in this corpus, while still flagging exact magnitudes as unverified by any
  third party at extraction time (source is one day old as of extraction).
- Guide relevance is similar in shape to `blog-cursor-warp-decode.md`: deep, credible GPU
  systems engineering with thin *direct* practitioner applicability for teams building
  agent harnesses, but real value as (a) a second data point for the "eliminate
  synchronization rather than optimize it" principle, and (b) economic context for why
  frontier MoE model training/serving costs continue to fall. The open-source release is
  the one aspect that is directly and immediately actionable, and only for the narrow
  audience of teams operating their own Blackwell-class MoE training infrastructure.
- No contradictions to file.
