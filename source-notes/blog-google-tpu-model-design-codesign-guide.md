---
source_url: https://developers.googleblog.com/tpu-model-design-considerations-and-optimization-guide/
source_type: blog-post
title: "TPU Model Design Considerations and Optimization Guide"
author: "Gagik Amirkhanyan and Vaibhav Singh (Google)"
date_published: 2026-11-16
date_extracted: 2026-11-18
last_checked: 2026-11-18
status: current
confidence_overall: emerging
issue: "#4800"
---

# TPU Model Design Considerations and Optimization Guide

> A Google Developers Blog summary of the open `AI-Hypercomputer/tpu-codesign` guide: eight hardware-grounded model-design rules for TPU Ironwood, whose only transferable point for this guide is its methodology — measure wall-clock ablations on a tuned baseline instead of trusting paper FLOPs.

## Source Context

- **Type**: blog-post (vendor technical guide; auto-discovered via trusted feed `google-developers`).
- **Author credibility**: Two Google engineers (Staff SWE and SWE) writing about Google's own hardware and an in-house "Ironwood profiling program". Primary-source for TPU behavior; vendor-interested for the claim that TPUs reward these designs. Measured results are on open 20–30B MoEs (plus one 63B ablation) and are explicitly "config-specific".
- **Scope**: Model-architecture, shape, and parallelism rules for training/serving on TPU v7x (Ironwood), with notes on TPU 8t/8i. It is not about AI-assisted software engineering; the Prospector asked that TPU-specific numbers not be pushed into guide content. The companion repo and the linked references were not followed (the post body was read in full).

## Extracted Claims

### Claim 1: Architecture choices made before training set permanent ceilings on MFU, cost, and latency
- **Evidence**: Framing assertion for the whole guide; supported indirectly by the measured ablations below.
- **Confidence**: emerging
- **Quote**: "Architectural choices made before the first training step set permanent ceilings on MFU (Model FLOP Utilization), cost, and serving latency."
- **Our assessment**: Plausible for hardware-bound training, and an instance of "decisions upstream bound what tuning downstream can reach". Off-scope for day-to-day AI-native engineering.

### Claim 2: Reduction/output dimensions should be multiples of 256, especially `head_dim = 256`; 64 or 128 leaves the MXU at least half idle in flash attention
- **Evidence**: Hardware reasoning (256×256 MXU) plus a measured reshape of Qwen3-30B MoE attention from 32×128 to 16×256 heads at identical parameters and FLOPs, which sped up end-to-end training with gains widening at longer context. The result chart/table was not extractable as text, so no percentages are recorded here. A cited external ablation (Yang et al. 2025, Gated DeltaNet) reported par-or-better quality at head dim 256.
- **Confidence**: emerging
- **Quote**: "at 64 or 128, flash-attention QK products leave the MXU ≥ 50% idle."
- **Our assessment**: Credible and checkable (matches the 256×256 array). Corroborates the existing microbenchmark note's head_dim claim, now with an end-to-end measurement. TPU-specific.

### Claim 3: Static shapes: separate the shape of a buffer from the extent of the data inside it (bucketing, masking, scalar prefetch)
- **Evidence**: Mechanism description (XLA compiles per exact shape; Pallas `PrefetchScalarGridSpec`; MaxText `packing=True`). No numbers.
- **Confidence**: settled (for XLA/TPU)
- **Quote**: "Dynamic workloads fit this model: the trick is to separate the shape of a buffer from the extent of the data inside it."
- **Our assessment**: Well-known XLA constraint; a clear statement of it.

### Claim 4: LatentMoE (project routed tokens to a smaller latent width before dispatch) gave +14% tokens/s on a 30B/128-expert MoE
- **Evidence**: Measured: ℓ = 768 (2.67×) cut on-device permute time 2.8×, 322 vs 270 TFLOP/s/chip (+14% tokens/s, +19% in FLOP terms), freed ~25 GB/device of activation HBM. Idea is cited to Nemotron 3 and adopted by other large models.
- **Confidence**: emerging
- **Quote**: "Standard EP dispatches every routed token at full"
- **Our assessment**: The quote is a fragment because the source splits the sentence across inline formatting; figures are in the Evidence line. Single configuration, and the post tags principles 3–7 as quality-trading, so the throughput number is not a quality-neutral win. Treat the percentage as config-specific, as the post itself says.

### Claim 5: Fewer, wider routed experts plus a larger shared expert raised throughput +57% on a 63B LatentMoE
- **Evidence**: Measured on 512 TPU v7x chips at EP=128: halving (N, K) from (512,16) to (256,8) while doubling d_ff and shared expert; held lower loss across 120.8B tokens. Single ablation.
- **Confidence**: emerging
- **Quote**: "Ablate expert granularity and the shared-to-routed split at your target scale rather than copying GPU co-designed models, since the TPU optimum is more shared-heavy."
- **Our assessment**: The caution (do not copy another hardware's co-design) is the transferable part; +57% is one run.

### Claim 6: Decode is bound by weight reads, so size designs to real serving concurrency
- **Evidence**: Arithmetic example: Qwen3.5-397B in FP8 on 4 chips streams ~100 GB/chip, a ~13.5 ms floor before KV; expected union of experts touched is E × [1 - (1 - K/E)^B]. MTP heads and Boardfly (TPU 8i) are cited as levers, with acceptance rates drawn from other models' reports.
- **Confidence**: settled (the roofline reasoning); emerging (the specific levers)
- **Quote**: "If real concurrency will be small, design fewer active bytes (fewer active parameters or a smaller model) rather than planning around a batch size you will not have."
- **Our assessment**: Good, general sizing advice: plan for the load you actually have.

### Claim 7: Vector (VPU) work is free only while it fits inside the MXU window; block-scaled FP8 needs block size ≳340 on Ironwood
- **Evidence**: Worked derivation (fp8 peak 4,614 TFLOPS vs 19.2 TFLOPS vector peak); simulation on a DeepSeek-V3 expert shape (block 512 at per-tensor time, 256 at 1.2×, 128 at 2.4×). Post advises measuring rather than relying on the peak ratio.
- **Confidence**: emerging (simulation, not measurement)
- **Quote**: "This threshold is specific to Ironwood."
- **Our assessment**: The post itself flags it as non-portable; it explicitly says to re-measure on TPU 8t. Of note as an example of a rule that "carries forward" while its threshold doesn't.

### Claim 8: Multi-pass BF16 helps only when low-precision MXU throughput exceeds BF16 by more than the pass count; on Ironwood (2:1) it cannot beat native BF16
- **Evidence**: Stated hardware ratios; TPU 8t adds native FP4.
- **Confidence**: settled (arithmetic given the stated ratios)
- **Quote**: "On Ironwood the FP8 to BF16 ratio is exactly 2:1, so two or more passes cannot beat native BF16."
- **Our assessment**: Honest negative result: the principle is generic, but on the target hardware it does nothing today.

### Claim 9: Parallelism can be remapped onto physical links with no model changes; SparseCore offload cut step time 15–22%
- **Evidence**: Cites `tpu-recipes` benchmarks; rules such as TP=2 max for training, EP on one short torus axis, FSDP default, DP/PP over DCN. Post says to confirm with a short profile.
- **Confidence**: emerging
- **Quote**: "Enabling XLA SparseCore async collective and sparse-gather offload cuts step time by"
- **Our assessment**: Quote is a fragment (the figure sits in a separate formatted run; 15–22% is in Evidence). Consistent with the 21.2% step-time reduction in the microbenchmarks note.

### Claim 10: Evaluate architecture changes in wall-clock time on a tuned stack, not paper FLOPs; systems tuning alone moved an open 30B MoE from 12% to 23% MFU
- **Evidence**: Authors' Ironwood benchmarks; also compares published baselines of 256-aligned MoEs (DeepSeek-V3, Qwen3-235B at 608–630 BF16 TFLOP/s/chip) against unaligned GPT-OSS-120B (330 TFLOP/s/chip), a cross-model comparison with many confounders.
- **Confidence**: emerging
- **Quote**: "Always evaluate architectural changes in wall-clock time on a tuned software stack rather than paper FLOPs"
- **Our assessment**: The one point with a plausible link to the guide's verification theme: compare against a tuned baseline, or you attribute systems wins to the idea. The cross-model "2× throughput" comparison is weak evidence for alignment alone.

### Claim 11: Measured trends are transferable; exact percentages are config-specific
- **Evidence**: Authors' own scoping note on their measurement program (open 20–30B MoEs, single slice, BF16, training up to 32K sequence).
- **Confidence**: settled (as a caveat)
- **Quote**: "Treat the trends and rankings as transferable, the exact percentages as config-specific."
- **Our assessment**: Useful self-scoping; we adopt it and do not carry the percentages into the guide.

## Concrete Artifacts

```
Principle map (post's own grouping, Google Developers Blog, 2026-11-16):
  Shape rules (1-2): 256-aligned dims; static shapes         -> adopt always
  Architecture choices (3-7): LatentMoE; compute intensity;
     decode bandwidth wall; exposed VPU time; multi-pass BF16 -> validate with ablations
  Expressing parallelism (8): map axes to D2D/ICI/DCN         -> no model changes
Measured numbers (config-specific): head_dim 32x128 -> 16x256 (identical params/FLOPs);
  LatentMoE +14% tok/s (322 vs 270 TFLOP/s/chip); expert-granularity +57% tok/s (63B);
  SparseCore offload 15-22% step time; systems tuning 12% -> 23% MFU.
```

## Cross-References

- **Corroborates**: `blog-google-tpu-microbenchmarks-roofline.md` Claim 5 (MXU 256×256 constraint, head_dim 128 suboptimal) and Claim 9 (SparseCore offload reduced step time 21.2%; here 15–22%); `blog-google-torchtpu-torchtitan-tpu-optimization.md` Claim 4 (verify numerics/loss after compiler-flag sweeps) is thematically consistent with measure-first advice here.
- **Contradicts**: None found; no contradiction issue filed.
- **Extends**: `blog-google-qwen35-ironwood-moe-optimization.md` Claim 4 (TP=8 head-sharding problem) and Claim 7 (page-size/VPU stalls) — this post generalizes similar hardware-alignment reasoning into design-time rules and reuses the Qwen3.5-397B memory-floor example.
- **Novel**: Design-time (pre-training) hardware co-design rules; LatentMoE and expert-granularity ablations; the explicit "trends transfer, percentages don't" caveat.

## Guide Impact

- **Chapter 03 (verification)**: At most one optional supporting citation for "measure against a tuned baseline before crediting a change" (Claim 10). No new section recommended; the evidence is ML-systems-specific.
- **Other chapters**: No changes. TPU shape rules, LatentMoE, and Boardfly content are out of scope for the guide's audience.

## Extraction Notes

- Read the full post via raw HTML converted to text. Figures and tables did not convert to text, so the per-context-length gains in Claim 2 are not recorded.
- Where inline formatting split sentences, quotes are limited to contiguous fragments within a single line of the post text.
- Companion repo and references were not followed; priority was low per Prospector triage.
