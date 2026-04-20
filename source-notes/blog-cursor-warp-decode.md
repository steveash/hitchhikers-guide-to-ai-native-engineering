---
source_url: https://cursor.com/blog/warp-decode
source_type: blog-post
title: "Better MoE Model Inference with Warp Decode"
author: Less Wright, Federico Cassano & Zhiyuan Zhang (Cursor)
date_published: 2026-04-06
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#207"
---

# Better MoE Model Inference with Warp Decode (Cursor)

> Cursor's ML systems team documents a GPU kernel reorganization — "warp decode" — that
> achieves 1.84× throughput and 1.4× accuracy improvement over conventional MoE decode
> on NVIDIA Blackwell B200s by assigning each warp to one output scalar rather than one
> expert, eliminating five bookkeeping stages and two intermediate memory buffers. The
> primary practitioner relevance is understanding the inference cost model for MoE coding
> assistants at batch-size-1.

## Source Context

- **Type**: blog-post (ML systems engineering; published on Cursor's official blog April 6, 2026)
- **Author credibility**: Three named Cursor researchers — Less Wright, Federico Cassano,
  and Zhiyuan Zhang. Federico Cassano also co-authored the Composer self-summarization post
  (`blog-cursor-composer-self-summarization.md`) and the Composer 2 technical report
  (`blog-cursor-composer2-technical-report.md`), giving him a consistent publication track
  record on Cursor's internal ML systems work. The post includes specific kernel names, buffer
  size arithmetic, and hardware throughput numbers consistent with genuine engineering
  documentation. Commercial incentive to present favorably exists; the technical specificity
  constrains it.
- **Scope**: Covers one specific GPU kernel design (warp decode) for the MoE decode stage
  during autoregressive generation at small batch sizes on NVIDIA Blackwell B200 GPUs. Does
  NOT cover: prefill, large-batch inference, dense model inference, the broader Cursor product,
  model training, agent architecture, or any practitioner-facing workflow patterns. The
  connection to the Cursor product is one sentence at the end.

## Extracted Claims

### Claim 1: Conventional MoE decode is expert-centric, and 5 of 8 pipeline stages are pure bookkeeping overhead with no bearing on the actual computation

- **Evidence**: The post enumerates the eight stages of a conventional MoE decode pipeline
  and identifies which perform computation vs. which exist solely for data layout management
  (padding to power-of-2 boundaries, scatter/combine operations, separate reduction pass).
  Five of the eight stages fall into the overhead category.
- **Confidence**: emerging (first-party architectural analysis; the stage count and categorization
  are Cursor's own framing but technically coherent with published MoE literature)
- **Quote**: (paraphrased) Five of eight stages are bookkeeping overhead — padding, token
  dispatch, scatter/combine, and reduction passes that exist purely to manage data layout
  for the expert-centric kernel organization.
- **Our assessment**: This is the framing claim that motivates the redesign. The "5 of 8
  stages are overhead" framing is striking and plausible: expert-centric approaches were
  designed for large-batch scenarios where spreading tokens across experts amortizes setup
  cost. At batch-size-1 (a single user's coding request), there is no amortization — every
  overhead stage is paid in full for every token. This is the fundamental insight practitioners
  should take away: MoE models are not free at small batch sizes, and the overhead is
  architectural rather than incidental.

### Claim 2: At batch-size-1 (coding assistant regime), MoE overhead is non-amortizable — making MoE inherently more expensive per request than at large-batch serving

- **Evidence**: Implicit in the motivation section: the post explicitly identifies warp
  decode as targeting "small-batch decode" scenarios. The pipeline overhead from Claim 1
  is per-token, not per-batch, and cannot be spread across multiple concurrent requests.
- **Confidence**: emerging (inference from architectural description; not directly stated
  as a comparison claim)
- **Quote**: "Warp decode specifically targets small-batch decode scenarios."
- **Our assessment**: This is the most practically relevant insight for practitioners
  evaluating AI coding tools. An MoE model with 1T parameters / 32B active (like Kimi K2.5,
  Composer 2's base) pays the full expert dispatch and routing overhead for each token of
  a single user's request. This means the inference cost model for MoE coding assistants
  differs materially from the headline "only X% of parameters are active" framing. Vendors
  serving MoE models for coding tasks must solve this or accept higher latency than
  equivalent dense models at the same active parameter count.

### Claim 3: Warp decode reorganizes MoE parallelism from expert-axis to output-axis — each warp owns exactly one output scalar and streams all required weight rows through private registers

- **Evidence**: Named kernel functions described: `moe_gate_up_3d_batched` (each warp owns
  one intermediate neuron, loads expert routing, performs dot-product in private registers
  without shared-memory staging) and `moe_down_3d_batched` (each warp processes one output
  dimension, loops through routed experts, uses warp-level butterfly reduction via
  `__shfl_xor_sync` instruction).
- **Confidence**: emerging (first-party implementation description with named kernel functions
  and specific CUDA intrinsics — technically specific enough to be genuine)
- **Quote**: "Each warp owns exactly one output scalar, streams all required weight rows,
  and accumulates across all top-k experts in private registers with no shared-memory staging."
- **Our assessment**: The key architectural decision is the output-axis parallelism: instead
  of assigning warps to experts (requiring coordination when multiple experts contribute to
  the same output), each warp independently accumulates all expert contributions to a single
  output value. This makes every warp completely independent, enabling the GPU scheduler
  to issue them in any order. The `__shfl_xor_sync` butterfly reduction is the CUDA-specific
  mechanism for combining partial sums within a warp without shared memory.

### Claim 4: Warp decode achieves 1.84× throughput improvement on NVIDIA B200 GPUs

- **Evidence**: Direct measurement stated: "1.84x end-to-end decode throughput improvement
  on B200 GPUs." Hardware efficiency: sustains 3.95 TB/s at batch size 32, which is 58% of
  the B200's 6.8 TB/s peak bandwidth.
- **Confidence**: emerging (vendor measurement; specific numbers with hardware reference;
  not independently verified)
- **Quote**: "1.84× throughput improvement on B200 GPUs"; "Sustains 3.95 TB/s at batch
  size 32 (58% of B200's 6.8 TB/s peak)"
- **Our assessment**: 1.84× is a substantial throughput gain. The 58% memory bandwidth
  utilization is notably high for a decode kernel — decode is typically memory-bandwidth-
  bound, and 58% of B200 peak suggests the kernel is well-optimized for the memory hierarchy.
  The batch-32 context matters: this is not the batch-1 coding assistant scenario; batch-32
  is a controlled throughput measurement. Batch-1 latency improvements are implied but
  not separately quantified.

### Claim 5: Warp decode outputs are 1.4× closer to FP32 ground truth than the conventional pipeline

- **Evidence**: Cosine similarity measurement: "minimum cosine similarity > 0.999996 against
  reference FP32 implementation." The 1.4× accuracy figure is the ratio of output deviation
  from FP32 reference between the two implementations.
- **Confidence**: emerging (vendor measurement; cosine similarity threshold is specific and
  checkable in principle)
- **Quote**: "outputs 1.4x closer to FP32 ground truth"; "Minimum cosine similarity
  > 0.999996 against reference implementation"
- **Our assessment**: Simultaneous throughput AND accuracy improvement is rare in kernel
  optimization — typically there is a precision vs. speed tradeoff. The mechanism (Claim 6)
  explains why this is possible here: the conventional pipeline introduces unnecessary
  quantization round-trips that warp decode avoids. This is a design pattern worth
  noting: when a precision cost is unnecessary (introduced by data layout management
  rather than compute constraints), removing it gives accuracy for free.

### Claim 6: The accuracy improvement comes from eliminating unnecessary BF16→MXFP8→BF16 quantization round-trips that the conventional pipeline introduces for data layout reasons

- **Evidence**: Mechanism described: "Traditional path converts BF16 activations to MXFP8
  and back, introducing rounding errors that accumulate across layers. Warp decode maintains
  BF16 activations throughout and FP32 accumulators. Eliminating this intermediate
  quantization step directly improves output quality."
- **Confidence**: emerging (mechanistic explanation; technically coherent with known
  quantization error accumulation behavior)
- **Quote**: "BF16 activations throughout and FP32 accumulators... eliminating intermediate
  quantization step directly improves output quality"
- **Our assessment**: The key insight is that the conventional MoE kernel forced a
  BF16→MXFP8→BF16 round-trip not because MXFP8 was needed for the computation, but
  because the expert-centric data layout required it for staging. Warp decode avoids that
  layout entirely, so the quantization round-trip never happens. This is a concrete example
  of how a systems-level design decision (data layout) can have unexpected quality effects —
  the precision loss was never intentional, just a side effect of the architectural choice.

### Claim 7: Warp decode eliminates two intermediate memory buffers totaling 32+ KB per token at BF16

- **Evidence**: Specific buffer sizes named: "activation gather buffer (32+ KB per token)"
  and "per-expert output buffer (8 × 2048 × 2 bytes in BF16)." Both are eliminated because
  warp decode folds all expert contributions into register accumulators.
- **Confidence**: emerging (first-party buffer size arithmetic; specific formula given for
  one buffer)
- **Quote**: "Removes activation gather buffer (32+ KB per token). Removes per-expert output
  buffer (8 × 2048 × 2 bytes in BF16). Folds eight expert contributions into register
  accumulator."
- **Our assessment**: Buffer elimination reduces memory pressure, which at small batch sizes
  translates directly to lower latency. The 32+ KB per-token gather buffer at batch-1 is
  fully paid per forward pass. Eliminating it removes a memory allocation and write that
  contributed to the overhead identified in Claim 1.

### Claim 8: Complete warp independence enables linear scaling of warp decode — doubling the output dimension doubles independent work items with no synchronization cost

- **Evidence**: "Complete lack of shared mutable state between warps. Enables GPU scheduler
  to issue warps in any order without synchronization constraints. Linear scaling: doubling
  output dimension doubles independent work items."
- **Confidence**: emerging (follows from the architectural design described in Claim 3;
  linear scaling is a theoretical property, not a separate measurement)
- **Quote**: "every warp is completely independent of every other"
- **Our assessment**: Independence is the key property that makes the kernel scalable and
  GPU-scheduler-friendly. The conventional expert-centric kernel requires barrier synchronization
  after stages because multiple warps contribute to the same expert's output buffer —
  any warp assignment that assigns two warps to the same expert requires coordination.
  Warp decode eliminates this by design.

### Claim 9: Warp decode specifically targets small-batch decode and is not a universal replacement for expert-centric approaches

- **Evidence**: Explicit scope statement: "Warp decode is not a universal replacement —
  prefill and large-batch inference still benefit from expert-centric approaches because
  multiple tokens share experts, amortizing organizational overhead."
- **Confidence**: settled (standard ML inference trade-off; Cursor explicitly acknowledges
  the scope limitation)
- **Quote**: "Prefill and large-batch inference still benefit from expert-centric approaches
  because multiple tokens share experts, amortizing organizational overhead."
- **Our assessment**: This scoping is important for practitioners evaluating it. Warp decode
  solves a specific problem — single-request autoregressive decode in a coding assistant.
  For model serving at scale (many concurrent users, batch forming), the conventional
  expert-centric approach remains competitive. Cursor's coding assistant use case is
  precisely the small-batch regime where warp decode helps; a cloud inference provider
  serving many users simultaneously may see different tradeoffs.

### Claim 10: The warp decode optimization directly enables faster Composer research iteration — "improve the model faster and ship new versions more often"

- **Evidence**: Explicit connection made at the end of the post: "The optimization enables
  faster iteration on Cursor's Composer AI model by significantly reducing inference latency.
  This accelerates research cycles, allowing the team to 'improve the model faster and
  ship new versions more often.'"
- **Confidence**: anecdotal (stated as a product implication; the causal link from inference
  speed to research iteration speed is plausible but not quantified)
- **Quote**: "improve the model faster and ship new versions more often"
- **Our assessment**: This is the only practitioner-facing claim in the post. It connects
  inference-layer engineering to the product improvement cycle described in
  `blog-cursor-real-time-rl.md` (#193), which reported a ~5-hour real-time RL checkpoint
  cycle. Faster inference makes each research experiment cheaper and faster to evaluate,
  shortening the feedback loop for model training iterations. For practitioners: this is
  why Cursor's capabilities improve continuously — infrastructure investment at the inference
  layer accelerates the model improvement layer above it.

### Claim 11: The general principle of rethinking parallelism assumptions (rather than fusing existing stages) is the key to the throughput gains

- **Evidence**: The throughput improvement comes from eliminating stages, not from fusing or
  optimizing existing ones. The post frames this explicitly as a "parallelism flip" rather
  than an incremental optimization.
- **Confidence**: emerging (architectural framing from the authors; the stage elimination
  analysis supports it)
- **Quote**: (paraphrased) Warp decode "eliminates overhead by never forming per-expert
  batches" — it does not optimize the expert-batching step, it removes the need for it.
- **Our assessment**: This is the highest-abstraction principle in the post. The conventional
  MoE kernel was designed under the assumption that expert-centric parallelism is natural
  for MoE models. That assumption is correct for training and large-batch inference but wrong
  for small-batch decode. Rethinking the parallelism assumption from scratch — rather than
  optimizing within it — unlocked a 1.84× gain. This generalizes to other optimization
  problems: when incremental optimization yields diminishing returns, the right question
  may be "is the fundamental parallelism strategy correct for this regime?"

## Concrete Artifacts

### Warp Decode Architecture: Two-Kernel Design

```
# Warp Decode Kernel Design (Cursor, April 2026)
# Source: https://cursor.com/blog/warp-decode

KERNEL 1: moe_gate_up_3d_batched (gate + up projection)
  Warp assignment: each warp owns ONE intermediate neuron
  Load: expert routing information
  Compute: dot-product accumulation in PRIVATE REGISTERS
  Key property: NO shared-memory staging required

KERNEL 2: moe_down_3d_batched (down projection)
  Warp assignment: each warp processes ONE output dimension
  Loop: through all routed experts
  Reduction: warp-level butterfly via __shfl_xor_sync instruction
  Key property: no shared mutable state between warps

BUFFER ELIMINATIONS vs. conventional pipeline:
  Removed: activation gather buffer (~32+ KB per token at BF16)
  Removed: per-expert output buffer (8 × 2048 × 2 bytes at BF16)
  Replaced by: per-warp register accumulators (no memory writes)

PARALLELISM AXIS COMPARISON:
  Conventional: expert-axis → warps assigned to experts → requires coordination
  Warp decode:  output-axis → warps assigned to output scalars → fully independent
```

### Performance Results

```
# Warp Decode vs. Conventional MoE Decode (NVIDIA B200, April 2026)
# Source: https://cursor.com/blog/warp-decode

Metric                    Conventional    Warp Decode     Improvement
Decode throughput         baseline        1.84× baseline  +84%
Output accuracy           baseline        1.4× closer     FP32 reference
  (cosine sim deviation)
Min cosine similarity     <0.999996       >0.999996       —
Memory bandwidth          —               3.95 TB/s       58% of 6.8 TB/s peak
  (batch=32)
Intermediate buffers      2 buffers       0               eliminated
  per token

SCOPE: small-batch autoregressive decode (batch-size-1 to ~32)
NOT APPLICABLE TO: prefill, large-batch serving (expert-centric still optimal)
HARDWARE: NVIDIA Blackwell B200 GPUs
```

### Conventional vs. Warp Decode Pipeline Stages

```
# MoE Decode Pipeline Comparison (Cursor, April 2026)

CONVENTIONAL (expert-centric, 8 stages):
  1. Token dispatch to experts                  [overhead: routing]
  2. Padding tokens to power-of-2 boundaries   [overhead: layout]
  3. BF16 → MXFP8 activation conversion        [overhead: staging, loses precision]
  4. Expert computation                         [COMPUTATION]
  5. MXFP8 → BF16 output conversion            [overhead: staging, loses precision]
  6. Expert output buffering                    [overhead: memory write]
  7. Scatter/combine expert results             [overhead: layout]
  8. Reduction pass                             [overhead: aggregation]
  Overhead stages: 5 of 8

WARP DECODE (output-centric, 2 stages):
  1. Gate/Up projection (one warp per neuron, register accumulation)  [COMPUTATION]
  2. Down projection (one warp per output dim, butterfly reduction)   [COMPUTATION]
  Overhead stages: 0 — overhead eliminated by design
```

## Cross-References

- **Corroborates**: `blog-cursor-composer2-technical-report.md` (#194) — That report
  describes Kimi K2.5 (Composer 2's base model) as a 1.04T-parameter MoE with 32B active
  parameters, and documents custom NVFP4 kernels for RL training forward passes. Warp decode
  is the decode-stage counterpart: a custom kernel for inference (not training) on the same
  class of MoE architecture. Both sources show Cursor investing in custom GPU kernel work
  for MoE models. The technical report covers training-time kernels; this post covers
  inference-time kernels.

- **Corroborates**: `blog-cursor-real-time-rl.md` (#193) — That post reported an unexplained
  −10.3% latency improvement from the Composer 1.5 real-time RL training run. Warp decode is
  a plausible contributing mechanism: if the inference stack adopted warp decode during the
  same period, latency reductions at the kernel level would appear in A/B test latency metrics.
  The two posts converge on: Cursor is actively reducing Composer inference latency through
  both training-pipeline and kernel-level work. The latency connection is circumstantial —
  not stated — but instructive.

- **Extends**: `blog-cursor-composer2-technical-report.md` (#194) — The technical report
  establishes that Cursor builds custom low-precision kernels for Blackwell hardware (NVFP4
  forward pass for RL). This post extends that picture: warp decode is a separate custom
  kernel for the decode stage, not training. Together the two posts show Cursor's full custom
  kernel portfolio: training (NVFP4) + inference (warp decode), both targeting Blackwell
  and both delivering dual improvements (compute efficiency + numerical quality).

- **Extends**: `blog-cursor-real-time-rl.md` (#193) — That post's Claim 2 describes a ~5-hour
  RL checkpoint cycle. Warp decode (Claim 10 here) provides infrastructure context for how
  that cycle stays fast: faster inference reduces the cost of each model evaluation run, which
  compresses the training feedback loop. The real-time RL post explains the training cadence;
  warp decode explains some of the infrastructure investment that makes it sustainable.

- **Novel**: Compared to the existing corpus:
  - The batch-size-1 cost model for MoE inference in a coding assistant context: no existing
    note explains why MoE models have non-amortizable overhead at small batch sizes specifically.
  - The "output-axis vs. expert-axis parallelism" distinction in MoE kernels: no prior note
    covers MoE kernel design at this level.
  - The simultaneous accuracy + throughput improvement mechanism (eliminating unnecessary
    quantization round-trips): no prior note documents this pattern.
  - Specific Blackwell B200 performance characteristics (3.95 TB/s = 58% peak bandwidth):
    no other source note contains B200 memory bandwidth utilization data.

- **Contradicts**: None identified. No existing source note makes claims about MoE decode
  kernel design or batch-size inference cost models that this post would oppose.

## Guide Impact

- **Chapter 02 (Harness Engineering — model selection and inference cost)**: Add context on
  MoE inference cost at small batch sizes (Claims 1–2). Practitioners evaluating AI coding
  tools should understand that MoE models — despite advertising "X% of parameters active" —
  carry per-request overhead at batch-size-1 that dense models do not. Vendor-side
  kernel work (warp decode) can mitigate this, but only the vendor controls it. When comparing
  MoE vs. dense model backends for a coding tool, latency benchmarks at batch-1 are the
  relevant metric, not throughput benchmarks at large batch sizes.

- **Chapter 02 (Harness Engineering — capability improvement cadence)**: Cite Claim 10 as
  evidence that Cursor's model capability improves continuously through inference-layer work,
  not just training updates. Teams building harnesses on Cursor should expect both latency and
  quality to improve over time without configuration changes — but also acknowledge that
  behavior can change (cross-reference `blog-cursor-real-time-rl.md` Claim 2: ~5-hour
  checkpoint cycle). For reproducible harness evaluations, treat model behavior as non-static.

- **Chapter 00 (Principles — optimization requires rethinking assumptions)**: Claim 11 is
  a portable engineering principle: the largest throughput gains often come from questioning
  the parallelism strategy, not optimizing within it. This applies beyond GPU kernels —
  the same principle appears in agent workflow design (is the sequential tool-call pattern
  correct for this task?) and context engineering (is the "one context window" assumption
  correct for this task length?). Consider using as a framing example.

## Extraction Notes

- The post is a concise engineering write-up (~800-1000 words). Full content read. No
  paywalled sections. No linked sub-pages with substantive additional content beyond what
  is described.
- The primary audience of the post is ML systems engineers, not practitioners of AI-native
  engineering. The guide-relevant content is thin — one practitioner-facing claim (Claim 10)
  and two inference-economics insights (Claims 1–2, 9). The deeper technical content
  (Claims 3–8) is context, not prescription.
- Performance numbers (1.84×, 1.4×, 3.95 TB/s, >0.999996 cosine similarity) are first-party
  and not independently verified. They are technically specific and internally consistent;
  treat as directional with high confidence in the direction, lower confidence in exact
  magnitude.
- The Prospector triage produced three separate assessments with divergent novelty ratings
  (low / medium / low). The split reflects genuine ambiguity: the source is substantive
  ML systems work with thin guide relevance. The extraction above extracts what is
  extractable while being honest that most claims are infrastructure context rather than
  actionable guidance.
- No contradictions to file.
