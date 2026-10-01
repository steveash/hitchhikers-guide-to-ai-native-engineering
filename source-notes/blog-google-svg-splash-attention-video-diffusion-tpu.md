---
source_url: https://developers.googleblog.com/accelerating-spatio-temporal-attention-for-video-diffusion-on-tpus/
source_type: blog-post
title: "Accelerating Spatio-Temporal Attention for Video Diffusion on TPUs"
author: "Ravisri Valluri (PhD SWE Intern), Sagar Chapara (ML Engineer), Rishabh Manoj (Senior ML Engineer), Google"
date_published: 2026-09-30
date_extracted: 2026-10-01
last_checked: 2026-10-01
status: current
confidence_overall: emerging
issue: "#3836"
---

# Accelerating Spatio-Temporal Attention for Video Diffusion on TPUs

> A Google Developers Blog kernel-engineering case study showing how Sparse VideoGen (SVG) sparse attention only yields real TPU speedups (2.40× isolated kernel, 1.28×–1.69× end-to-end from 720p to 1440p) once empty tiles are skipped, full tiles bypass masking, the mask is tile-aligned, and token layouts are permuted on head-local devices — a low-level ML-serving report with little direct connection to this guide's AI-assisted-engineering scope.

## Source Context

- **Type**: blog-post (Google Developers Blog, published 2026-09-30; found via the trusted `google-developers` feed). Subtitle: "A case study in turning theoretical sparsity into an actual end-to-end speedup on TPUs." The post's figures/tables are images and were not readable as text; numbers below come from the body text only.
- **Author credibility**: Three Google engineers (an intern and two ML engineers; Manoj and Chapara also co-authored the HeyGen Avatar IV post already in the corpus). First-party, with specific benchmark configurations and PSNR quality measurements, but no independent reproduction and no code released in the post.
- **Scope**: Covers why attention dominates video-diffusion latency, SVG's spatial/temporal head routing, a four-stage progression of Splash Attention (JAX/Pallas) kernels on one TPU v6e, dynamic routing with fixed tensor shapes, token permutation placement in distributed inference, and end-to-end 720p/1080p/1440p results. Does NOT cover AI-assisted development practice, the SVG profiling algorithm itself (deferred to the SVG paper), or hardware other than TPU v6e.

## Extracted Claims

### Claim 1: Self-attention's share of per-layer latency grows steeply with resolution, making it the first optimization target
- **Evidence**: Table 1 (image, not extracted) plus figures in text: 55.5% at 720p, 72.5% at 1080p, 88.2% at 1440p on eight TPU v6e chips, 81 frames.
- **Confidence**: emerging
- **Quote**: "Because full attention scales quadratically with sequence length, its share of per-layer latency can grow from 55.5% to 88.2%."
- **Our assessment**: Plausible and consistent with quadratic scaling; the figures are for one model/hardware setup. Explains why end-to-end speedup grows with resolution.

### Claim 2: Attention heads in video diffusion are often classifiable as spatial or temporal, each with regular geometric sparsity, and SVG routes heads dynamically at inference time
- **Evidence**: Figure 2 (Step 6, Layer 32): 94.8% of attention mass for a spatial-head query lies in its own frame; temporal head concentrates along the same (y,x) across frames. SVG routing samples a few queries and picks the mask whose output deviates least from dense.
- **Confidence**: emerging
- **Quote**: "Within a spatial head, a patch attends mostly to other patches within the same or close-by frames; within a temporal head, a patch attends to a small spatial region across a large number of frames."
- **Our assessment**: The algorithm is from the external SVG paper, not this post; the post's contribution is implementation. Head-type specialization is the enabling observation.

### Claim 3: Logical sparsity does not equal physical speedup — a naive sparse kernel was 22% slower than dense despite skipping over half the tiles
- **Evidence**: B1 naive traversal: mask retains ~39% of pairs, kernel visits 44% of outer tiles, 96.37 ms vs 78.70 ms for dense Splash (75.6K tokens, 10 heads, head dim 128, single v6e).
- **Confidence**: emerging
- **Quote**: "This implementation takes 96.37 ms compared to 78.70 ms for dense Splash: 22% higher latency despite skipping more than half the tiles."
- **Our assessment**: A valuable negative result: a theoretically cheaper algorithm regressing latency. Specific, checkable numbers, though from synthetic BF16 inputs.

### Claim 4: Separating full tiles (mask-free fast path) from boundary tiles removes a VPU bottleneck that stalls the MXU
- **Evidence**: B2 drops latency from 96.37 ms to 54.12 ms (44% below naive sparse, 31% faster than dense) with the retained pairs unchanged.
- **Confidence**: emerging
- **Quote**: "On TPUs, performing this elementwise mask evaluation on every visited tile bottlenecks the Vector Processing Unit (VPU) and stalls the Matrix Multiply Unit (MXU), even when every pair in a tile is valid."
- **Our assessment**: Mechanism is stated but not profiled in the post beyond latency results; credible and an exact-output optimization (no quality change).

### Claim 5: Minimizing boundary-masking work does not minimize latency; tile size has an interior optimum
- **Evidence**: Varying BQ with BKV fixed at 1536: BQ=1024 → 16.95% masked tiles, 66.88 ms; BQ=3328 → 27.55%, 54.12 ms; BQ=4864 → 58.62 ms.
- **Confidence**: emerging
- **Quote**: "The plot shows this tradeoff: the configuration with the least masking work is not the fastest."
- **Our assessment**: Good example of a proxy metric (masked-tile fraction) misleading optimization; only three-to-four points sampled, on one shape.

### Claim 6: Aligning (rounding) the sparse mask to hardware tiles gives a further large gain, at the cost of slightly changing the mask
- **Evidence**: B3 reduces tiles needing masking from 27.55% to 2.22%; latency 32.76 ms, 2.40× over dense Splash. Rounding outward/inward is balanced to approximately preserve the pair budget.
- **Confidence**: emerging
- **Quote**: "Unlike the previous optimization, this changes which interactions contribute to the output."
- **Our assessment**: Unlike B2 this is lossy; the post reports end-to-end PSNR (Claim 9) rather than isolating the quality effect of rounding alone.

### Claim 7: Dynamic per-head routing should select between token layouts on static-shape tensors to avoid XLA recompilation
- **Evidence**: Design description: Boolean flags per head select original vs. permuted layout, tensor dimensions fixed; same flags restore order after attention.
- **Confidence**: anecdotal
- **Quote**: "Unlike dynamically splitting heads into variable-sized spatial and temporal subsets, changing a head’s assignment at runtime does not alter tensor shapes or trigger costly XLA recompilations."
- **Our assessment**: Sound compiler-aware design; no measurement of the recompilation cost avoided is given.

### Claim 8: Permuting tokens to temporal-major order, and doing it after the all-to-all on head-local devices, beats in-kernel temporal handling and earlier permutation
- **Evidence**: In-kernel handling raised latency from 44.40 to 74.14 ms on a temporal-head benchmark. Moving reordering into the head-local region cut attention latency from 75.64 ms to 46.81 ms (38%) on one captured step/layer, including routing, permutation, and communication.
- **Confidence**: emerging
- **Quote**: "We therefore apply the permutation after the input head exchange, execute sparse attention, and recover the original token order before the return exchange."
- **Our assessment**: Placement of data-layout transforms relative to collectives matters as much as the kernel. Authors admit they did not separately measure the in-kernel indexing cost.

### Claim 9: End-to-end speedups are real but smaller than kernel speedups and grow with resolution, with quality loss measured by PSNR
- **Evidence**: 720p aggressive schedule 153.50 s → 119.86 s (1.28×); 1080p 683 s → 457 s (1.49×, 24.66 dB); 1440p 2,471 s → 1,461 s (1.69×, 24.05 dB); 720p video example 24.80 dB. Medians of three warm runs, 40 steps, eight v6e chips.
- **Confidence**: emerging
- **Quote**: "Gains are smaller than the isolated kernel speedups because denoising also includes work outside sparse attention."
- **Our assessment**: Credible method (dense control, same prompt/seed, warm medians). PSNR ~24 dB vs dense is only a similarity proxy, and the aggressive schedule is explicitly lossy; no human or benchmark quality evaluation is reported.

### Claim 10: Takeaway — efficiency depends on hardware work avoided, not attention pairs removed
- **Evidence**: Summary of the preceding progression.
- **Confidence**: emerging
- **Quote**: "Efficient sparse attention on TPUs depends on how much work the hardware can avoid, not just how many attention pairs the mask removes."
- **Our assessment**: A transferable principle for any sparse/approximate optimization: measure on hardware, not by algorithmic operation counts.

## Concrete Artifacts

```
Source: Table-less summary of kernel progression (Google Developers Blog; single TPU v6e,
75,600 tokens, 10 heads, head dim 128, BQ=3328, BKV=1536)
B0 Dense Splash                        78.70 ms
B1 Naive sparse traversal              96.37 ms
B2 Full/boundary tile specialization   54.12 ms
B3 Tile-aligned sparse traversal       32.76 ms  (2.40x vs dense)

Tile-size sweep (BKV=1536): BQ=1024 66.88 ms; BQ=3328 54.12 ms; BQ=4864 58.62 ms

End-to-end (aggressive SVG schedule, eight TPU v6e):
720p  153.50 s -> 119.86 s  1.28x
1080p   683 s  ->   457 s   1.49x  24.66 dB
1440p 2,471 s  -> 1,461 s   1.69x  24.05 dB
```

(Numbers transcribed from the post body text; no code was published.)

## Cross-References

- **Corroborates**: `blog-google-heygen-avatar-iv-trillium-optimization.md` Claim 6 — both find that aligning sparse-attention blocks to hardware tiling to eliminate mask/padding work is a major lever on TPU v6e.
- **Contradicts**: None found. (The HeyGen note's Claim 6 prefers finer, frame-aligned blocks, while this post finds an interior optimum at BQ=3328 over smaller 1024 — different kernels and models, so a conditioning difference, not a contradiction.)
- **Extends**: `blog-google-heygen-avatar-iv-trillium-optimization.md` (same authors' group, same hardware; complementary techniques — tile specialization, layout permutation — versus its collective pipelining in Claim 5) and `blog-google-tpu-microbenchmarks-roofline.md` (hardware-measurement context). Also adjacent to `blog-google-qwen35-ironwood-moe-optimization.md` as TPU kernel work.
- **Novel**: Dynamic sparse-attention head routing (SVG) on TPU; the "logical vs. physical sparsity" negative result; token-permutation placement after head all-to-all; fixed-shape routing flags to avoid XLA recompilation; resolution-scaling of end-to-end speedup.

## Guide Impact

- **Chapter 05 (inference optimization)**: Marginal. If the guide discusses inference-time optimization, this could be a one-line example that algorithmic sparsity must be validated against hardware execution (Claim 3, Claim 10). Otherwise out of scope — pure kernel/infrastructure engineering; recommend reference-only treatment consistent with the HeyGen and Qwen3.5/Ironwood notes.
- No change recommended to chapters on AI-assisted engineering workflow.

## Extraction Notes

- Read the full post body from the raw HTML (converted to text). Figures and Tables 1–4 are images, so table contents were not extracted; the body text restates the key numbers used here.
- No linked sub-pages followed; the SVG paper is referenced for the routing algorithm but not read.
- Published date taken from the page ("SEPT. 30, 2026").
- Cross-reference claim numbers (HeyGen Claims 5 and 6) were verified against that note's text.
- Triage flagged scope uncertainty; the note is kept short on guide impact accordingly.
