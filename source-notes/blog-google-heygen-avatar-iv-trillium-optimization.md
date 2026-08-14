---
source_url: https://developers.googleblog.com/heygen-x-google-cloud-bringing-avatar-iv-to-tpus/
source_type: blog-post
title: "HeyGen x Google Cloud: Bringing Avatar IV to TPUs"
author: "HeyGen team (Alireza Dolatabadi, Rui Zhang, Onee Yekeh, Rong Yan, Charly Hong) and Google Cloud AI team (Rishabh Manoj, Sagar Chapara, Prisha Jain, Hitesh Yadav, Shamik Ray), with Google Cloud Field & Customer Engineering (Travis Martin, Jennifer Liang)"
date_published: 2026-08-13
date_extracted: 2026-08-14
last_checked: 2026-08-14
status: current
confidence_overall: emerging
issue: "#2695"
---

# HeyGen x Google Cloud: Bringing Avatar IV to TPUs

> A first-party Google Developers Blog engineering case study describing how HeyGen and Google Cloud jointly ported and optimized Avatar IV (an 18B+ parameter diffusion video-generation model) onto eight-chip Trillium (TPU v6e) hosts, achieving a claimed 1.86× speedup and up to 25% better cost efficiency versus an 8×H100 baseline through collective pipelining, sparse-attention-mask elimination, a Cauchy-Schwarz softmax bound, and explicit compiler-layout contracts — a low-level ML-serving/kernel-engineering report with no direct connection to this guide's scope (AI-assisted software engineering practice), similar in kind to `blog-google-qwen35-ironwood-moe-optimization.md`.

## Source Context

- **Type**: blog-post (Google Developers Blog, engineering deep-dive; published August 13, 2026). Discovered via the trusted `google-developers` RSS feed. The post is self-contained — no sub-pages were followed since it does not link out to external explainers or repositories that its own claims depend on; it embeds its own figures (attribution noted where used) rather than deferring to linked material.
- **Author credibility**: Ten named individual contributors across HeyGen (5) and Google Cloud (5, split between an AI team and a Field & Customer Engineering team), listed in an "Acknowledgements" section. This is a joint vendor-customer engineering report, structurally similar to `blog-google-qwen35-ironwood-moe-optimization.md` (Google's own performance team optimizing a third-party model) but distinct in that here the *customer* (HeyGen) is the model owner and co-author, not just the subject of an internal Google optimization exercise. The post reads as a genuine postmortem-style engineering narrative (named PR-level detail on kernel and compiler-flag changes) rather than pure marketing copy, though it is still a vendor-published joint case study with no independent reproduction.
- **Scope**: Covers the memory/parallelism setup (FSDP weight sharding + Ulysses sequence sharding across an eight-chip Trillium mesh), the torchax (PyTorch-on-JAX) port path, three named optimization "walls" (collective pipelining, sparse-attention-mask elimination, softmax dependency removal via a Cauchy-Schwarz bound), a cross-cutting "layout is the ABI" compiler-contracts theme, a two-tier output-quality verification gate, and a six-milestone cumulative-speedup breakdown. Does NOT cover: training (this is inference-serving optimization only), any AI-assisted coding/development workflow used by the engineers who wrote this optimization work, comparison to TPU generations other than Trillium (v6e), or public benchmarking beyond the single 8×H100-vs-Trillium cost/performance comparison stated once.

## Extracted Claims

### Claim 1: The optimized pipeline is 1.86× faster than HeyGen's first working Trillium port, and reaches performance comparable to their 8×H100 production setup while being up to 25% more cost-efficient per minute of generated video
- **Evidence**: Headline result stated directly, with the specific hardware baseline (8×H100) named.
- **Confidence**: anecdotal (vendor/customer joint self-report; no independent reproduction, and "first working version" as the baseline is not itself quantified in absolute terms)
- **Quote**: "we brought Avatar IV to an eight-chip Trillium (v6e) host and made it 1.86× faster than our first working version." / "The result is a pipeline that streams at performance comparable to what we see from our 8×H100 production setup while being up to 25% more cost efficient per minute of generated video."
- **Our assessment**: Consistent with how this corpus treats other first-party Google/vendor performance multipliers (see `blog-google-qwen35-ironwood-moe-optimization.md` Claim 2) — directionally credible given the amount of concrete, checkable mechanism detail surrounding it, but an unverified self-reported number with an unspecified exact baseline.

### Claim 2: Avatar IV's real-time streaming requirement (chunk-by-chunk video delivery, where a late chunk stalls playback) is the framing constraint that makes latency, not just throughput, the primary optimization target
- **Evidence**: Stated as the opening framing of the entire post.
- **Confidence**: settled (a factual description of the product's delivery model, not a performance claim)
- **Quote**: "A stream doesn't wait. Avatar IV renders talking-head video chunk by chunk, and if a chunk is late, the video stalls."
- **Our assessment**: This framing matters for interpreting every downstream optimization in the post — the target metric is time-per-chunk (latency), not aggregate throughput, which is a different optimization regime than the batch-inference framing common in most of this corpus's other TPU/LLM-serving posts (e.g., `blog-google-qwen35-ironwood-moe-optimization.md`, which optimizes concurrency and tokens/s).

### Claim 3: Avatar IV's two transformers require more than 36GB of bf16 weights against 32GB of HBM per Trillium chip, forcing FSDP weight-sharding and Ulysses sequence-sharding across the same eight-chip mesh
- **Evidence**: Direct memory-arithmetic statement (36GB required vs. 32GB available per chip) paired with the two named parallelism strategies used to resolve it.
- **Confidence**: settled (a concrete, checkable hardware-capacity constraint with a stated resolution mechanism)
- **Quote**: "The two transformers total more than 36 GB of bf16 weights against 32 GB of HBM per Trillium chip, so the weights are FSDP-sharded across the eight chips." / "Weights are FSDP-sharded and sequences Ulysses-sharded across the same eight-chip mesh."
- **Our assessment**: A specific, independently sensible constraint (36GB doesn't fit in 32GB, so it must be sharded) that motivates the whole eight-chip topology choice. Combining FSDP (parameter sharding) and Ulysses (sequence sharding) on the *same* mesh — rather than assigning each dimension to a disjoint set of devices — is the one architectural decision stated but not deeply justified in the post; it's presented as a given rather than a design trade-off like the DP+EP split in `blog-google-qwen35-ironwood-moe-optimization.md` Claim 5.

### Claim 4: The port to TPU ran through torchax, a PyTorch frontend on JAX, allowing HeyGen's production PyTorch model code to run unmodified while being dispatched to JAX arrays and compiled by XLA
- **Evidence**: Direct statement of the porting mechanism.
- **Confidence**: settled (a factual description of the tooling used, independently checkable as a known open-source project)
- **Quote**: "The port ran through torchax, a PyTorch frontend on JAX: the production model code runs unmodified, dispatched onto JAX arrays and compiled by the XLA compiler."
- **Our assessment**: This is the corpus's first documented instance of torchax as a migration path for moving an existing PyTorch production model to TPU/JAX without a rewrite — a potentially reusable data point for any future guide discussion of GPU-to-TPU migration costs, distinct from a from-scratch JAX/Pallas implementation.

### Claim 5: Splitting the attention heads into independent groups, each running its own all-to-all/attention/all-to-all sequence, let the XLA compiler pipeline communication transfers behind sibling groups' compute, collapsing the collective's footprint on the compute stream roughly 5× with attention time itself unchanged
- **Evidence**: Named optimization ("Hiding the Collective") with a specific before/after trace-derived metric.
- **Confidence**: settled (a specific, named technique with a stated quantitative trace measurement)
- **Quote**: "The attention heads split into a few independent groups, each running its own all-to-all, attention, all-to-all pattern" / "In the traces, the collective's footprint on the compute stream collapsed roughly 5×, with attention time itself unchanged."
- **Our assessment**: A generalizable pattern independent of this specific model: a monolithic collective operation that blocks the compiler from overlapping communication with compute can sometimes be decomposed into independent groups purely to create pipelining opportunities, without changing what is computed. Structurally similar in spirit to the collective-fusion techniques in `blog-google-qwen35-ironwood-moe-optimization.md` Claim 11 (bitcast-packing two collectives into one), though the mechanism here (splitting into groups to enable overlap) is the inverse move — decomposing rather than fusing — aimed at hiding latency rather than reducing call count.

### Claim 6: Relaxing the sparse-attention kernel's block-size constraint from multiples of 128 down to multiples of 16 (the finest bf16 tiling the hardware supports) enabled frame-aligned blocks that eliminated mask predicates and padding, lifting the super-resolution kernel's efficiency from about half of the hardware ceiling to nearly three-quarters, and a subsequent kernel rebuild closed that to about 86%
- **Evidence**: Named optimization ("Deleting the Mask") with a two-step before/after efficiency progression (50% → ~75% → ~86% of ceiling).
- **Confidence**: settled (a specific, named technique with a stated two-stage quantitative efficiency progression)
- **Quote**: "We relaxed the kernel's block-size constraint from multiples of 128 down to multiples of 16, the finest bf16 tiling the hardware supports along the sequence dimension" / "The alignment round lifted the kernel from about half of the ceiling this attention shape can reach on the hardware to nearly three-quarters of it, and the rebuilt body closed to about 86%."
- **Our assessment**: A concrete counter-example to an intuition that coarser block sizes are safer for hardware efficiency — here the opposite (finer, frame-aligned block sizes) removed padding/masking overhead entirely rather than just shrinking it. Note the two-step framing (block-size relaxation gets to ~75%, then a *separate* kernel rebuild gets to ~86%) — the post attributes only part of the final 86% figure to the block-size change itself, which matters for anyone trying to isolate the block-size lever's standalone contribution.

### Claim 7: A Cauchy-Schwarz-derived upper bound on attention logits, precomputed and fed to the kernel via scalar prefetch, removes the need for flash-attention's per-block running-maximum rescaling; on HeyGen's production data 98-99% of attention heads qualify for this optimization
- **Evidence**: Named optimization ("Unchaining the Softmax") with the specific mathematical justification and a stated production-data qualification rate.
- **Confidence**: settled (a specific, named numerical technique with a mathematically stated bound and a concrete measured qualification rate on stated data)
- **Quote**: "By the Cauchy–Schwarz inequality, a query's largest possible logit is bounded by its norm times the largest key norm." / "A tiny array of precomputed norms, fed to the kernel through scalar prefetch, lets each row derive its bound as it starts, and the online max is no longer needed." / "On our production data, 98–99% of heads qualify."
- **Our assessment**: This is the single most reusable numerical-kernel-engineering insight in the post: replacing flash attention's *data-dependent* running-max rescaling (which serializes the innermost loop, since each block's max depends on the previous block) with a *data-independent, precomputable* bound derived analytically from vector norms removes a serialization point without changing the attention math's correctness — a generalizable technique for anyone hand-optimizing flash-attention-style kernels, not specific to video diffusion models. The corpus's first documented instance of this specific technique.

### Claim 8: Fusing the chain of small operations preceding attention (normalization, rotary embeddings, projections, head packing) into a single Pallas kernel that writes output directly in the physical layout the subsequent all-to-all collective expects eliminated a five-stage repack chain outright in one case
- **Evidence**: Named cross-cutting theme ("Layout Is the ABI") with a specific worked example.
- **Confidence**: settled (a specific, named technique with a concrete before/after example — a five-stage repack chain disappearing)
- **Quote**: "The compiler assigns a specific physical layout to the operand of the all-to-all that follows, and any mismatch gets patched with copies. We fused that chain into a single Pallas kernel that writes its output in exactly the layout the collective wants. The kernel's output buffer is the collective's input buffer. In one case, a five-stage repack chain between the projections and the collective disappeared outright."
- **Our assessment**: This generalizes past just this one optimization: treating physical memory layout as an explicit contract between kernel author and compiler, rather than letting the compiler silently patch mismatches with copy operations, is the connecting principle across several of the post's individual wins (see Claim 9 for the same theme applied to compiler scheduling and cost-estimation flags).

### Claim 9: The team explicitly requests a non-default XLA instruction scheduler (`XLA_TPU_FORCE_LP_LLO_SCHEDULER`) by name for their heavy self-attention kernels, and attaches honest cost estimates (FLOPs/bytes) to their custom Pallas kernels — since XLA otherwise prices a custom kernel at zero FLOPs and zero bytes, mispricing the scheduler's latency-hiding decisions around it — recovering scheduling time with no kernel or graph change
- **Evidence**: Two named "compiler contract" techniques stated directly, with the specific XLA flag name given.
- **Confidence**: settled (specific, named compiler-flag and cost-model techniques with a stated causal mechanism for why each works)
- **Quote**: "The heavy self-attention kernels only hit their tuned speed under an alternative instruction scheduler that better overlaps the softmax's vector work with the matrix unit. So each kernel requests it by name (`XLA_TPU_FORCE_LP_LLO_SCHEDULER`) rather than trusting the defaults." / "XLA prices a custom kernel at zero FLOPs and zero bytes, since it can't see inside, so its latency-hiding scheduler misprices everything around it. Attaching honest cost estimates to our in-house kernels bought back time with no kernel or graph change at all: the scheduler simply repriced what it could hide."
- **Our assessment**: A specific, transferable insight for anyone writing custom kernels under XLA (or any compiler with a cost-based scheduler): an opaque custom kernel with no declared cost model can silently degrade scheduling decisions for *surrounding* code, even though the kernel itself is correct and fast — the fix (declaring an honest cost estimate) requires zero changes to the kernel's actual computation.

### Claim 10: Output correctness is enforced through a two-tier verification gate — Tier 1 requires byte-identical (frame-for-frame hash-equal) output versus baseline; Tier 2, for changes that alter the compiled program's floating-point reduction order, is held to an independently-measured bf16-reassociation tolerance band, with anything outside that band routed to a blind, frame-by-frame human review by the model's owners before shipping
- **Evidence**: Named verification section ("Proving the Pixels Didn't Change") describing both tiers and their respective pass/escalation criteria.
- **Confidence**: settled (a specific, named two-tier verification process with stated criteria for each tier and an explicit escalation path)
- **Quote**: "Tier one is byte-identical. The delivered video must hash equal to baseline, frame for frame." / "Tier two covers changes that alter the compiled program's reduction order. Those are held to the narrow similarity band that bf16 reassociation itself produces, a band we measured independently. Anything below that band goes to the model's owners for a blind, frame-by-frame review before it ships."
- **Our assessment**: This is the post's clearest process-engineering claim (versus its many kernel/numerical claims): every optimization in the post, however aggressive, was gated behind an explicit, tiered output-quality check before shipping, with human review as the fallback for anything that couldn't be verified programmatically. This is a directly transferable quality-gate pattern for any team optimizing a generative model's inference stack where "faster" and "bit-identical" are in tension — independent of the TPU/video-diffusion specifics.

### Claim 11: Across six cumulative optimization milestones plotted on the same model and quality gates throughout, time-per-chunk fell to just over half its starting value (the 1.86× headline speedup), with the first milestone — a "known playbook" of custom attention kernels, locked-in sequence-parallel layout, workload-tuned XLA flags, and shape-matched kernel tile sizes — producing the single largest drop
- **Evidence**: Stated directly in the "Six Milestones" section describing the cumulative-speedup chart.
- **Confidence**: settled (a specific claim about the *relative ordering* of gains across a stated six-step campaign, though the exact per-milestone numeric breakdown beyond "largest drop" for milestone one is not given in the extracted text)
- **Quote**: "Moving from left to right across the graph, time per chunk falls to just over half its starting value—a 1.86× speedup—with the same model and quality gates throughout. The first milestone is the largest drop, representing the known playbook executed in full: custom attention kernels in place of stock ones, the sequence-parallel layout locked in, the XLA flag set tuned against this workload rather than left at defaults, and kernel tile sizes matched to its shapes."
- **Our assessment**: Notable as an explicit statement that the "known playbook" (standard, already-understood optimizations) captured the majority of the gain, with the three novel techniques detailed later in the post (collective pipelining, mask deletion, softmax bound) contributing the remaining, harder-won increment. This is a useful calibration point: most of the value came from applying known best practices correctly before any of the bespoke kernel engineering began.

## Concrete Artifacts

### "Layout Is the ABI" section (verbatim from the post)

```
"The walls shared a quieter lever: explicit contracts with the compiler.

The clearest example is layout. Attention's inputs are produced by a chain
of small operations: normalization, rotary embeddings, projections, head
packing. The compiler assigns a specific physical layout to the operand of
the all-to-all that follows, and any mismatch gets patched with copies. We
fused that chain into a single Pallas kernel that writes its output in
exactly the layout the collective wants. The kernel's output buffer is the
collective's input buffer. In one case, a five-stage repack chain between
the projections and the collective disappeared outright.

Flags are contracts too. The heavy self-attention kernels only hit their
tuned speed under an alternative instruction scheduler that better overlaps
the softmax's vector work with the matrix unit. So each kernel requests it
by name (XLA_TPU_FORCE_LP_LLO_SCHEDULER) rather than trusting the defaults.

Two more contracts paid off the same way. XLA prices a custom kernel at
zero FLOPs and zero bytes, since it can't see inside, so its
latency-hiding scheduler misprices everything around it. Attaching honest
cost estimates to our in-house kernels bought back time with no kernel or
graph change at all: the scheduler simply repriced what it could hide.

And because the unit of shipment on TPU is a compiled program, our
executables are release artifacts: cached, versioned, and promoted between
environments like model weights, gated on zero recompiles and bit-exact
output."

Source: developers.googleblog.com/heygen-x-google-cloud-bringing-avatar-iv-to-tpus/,
section "Layout Is the ABI"
```

### Team composition (verbatim from the post's Acknowledgements)

```
HeyGen Team: Alireza Dolatabadi, Rui Zhang, Onee Yekeh, Rong Yan, Charly Hong
Google Cloud AI Team: Rishabh Manoj, Sagar Chapara, Prisha Jain, Hitesh Yadav, Shamik Ray
Google Cloud Field & Customer Engineering Teams: Travis Martin, Jennifer Liang

Source: developers.googleblog.com/heygen-x-google-cloud-bringing-avatar-iv-to-tpus/,
"Acknowledgements" section
```

### Section structure (post outline, for reference)

```
1. The Workload, and the Port
2. Six Milestones
3. Hiding the Collective
4. Deleting the Mask
5. Unchaining the Softmax
6. Layout Is the ABI
7. Proving the Pixels Didn't Change
8. Acknowledgements
```

## Cross-References

- **Corroborates**: `blog-google-qwen35-ironwood-moe-optimization.md` — both are first-party/joint Google Developers Blog posts pairing a headline vendor-reported performance multiplier (this post's 1.86×; that post's 3.1×/4.7×) with genuinely concrete, independently checkable supporting technical detail (named kernel techniques, specific before/after measurements, named compiler flags), consistent with this corpus's general pattern of treating such headline multipliers as `anecdotal`/`emerging` while treating the surrounding named mechanism descriptions as `settled` where independently checkable.
- **Contradicts**: None identified. No existing source note makes a claim about TPU-based diffusion-model inference, flash-attention softmax bounding, or torchax that this post's claims oppose.
- **Extends**: `blog-google-qwen35-ironwood-moe-optimization.md` (TPU v7/Ironwood inference-serving of a text LLM) and `blog-google-tunix-agentic-rl-throughput.md` (TPU v5e training) — together with this post (TPU v6e/Trillium inference-serving of a diffusion video-generation model), the corpus now has three distinct TPU-generation/workload-type data points (v5e training, v7 LLM inference, v6e diffusion-video inference). `blog-google-tpu-microbenchmarks-roofline.md`'s Ragged-Paged-Attention microbenchmark and roofline methodology is topically adjacent (both concern TPU attention-kernel performance measurement) but that note's roofline framework is not applied or referenced in this post. `blog-cursor-multi-agent-kernels.md` documents a superficially similar activity (kernel-level performance optimization, 38% GPU kernel speedup) but via an autonomous multi-agent AI system doing the optimization work itself — a meaningful contrast worth flagging: this HeyGen/Google post is entirely human-engineered optimization (no AI coding agents used in the optimization process itself, per the post's text), whereas the Cursor+NVIDIA post is specifically about AI agents performing the optimization, which is the actual within-scope pattern for this guide.
- **Novel**: This is the corpus's first source documenting: (1) TPU v6e (Trillium) inference-serving optimization of any workload; (2) diffusion-model-based video generation as an inference workload on TPU; (3) torchax as a PyTorch-to-JAX/TPU migration path; (4) a Cauchy-Schwarz-derived analytical bound replacing flash attention's running-maximum rescaling; (5) an explicit two-tier (byte-identical / bf16-reassociation-tolerance-plus-human-review) output-quality gate for a generative-model kernel-optimization campaign.

## Guide Impact

- **No direct chapter impact identified.** This guide (per `guide/*.md` chapter headers: 00-principles, 01-daily-workflows, 02-harness-engineering, 03-verification, 04-context-engineering, 05-team-adoption, 06-security-threat-model) is about the practice of AI-assisted software engineering. This source is an ML-serving/kernel-engineering case study about humans manually optimizing inference infrastructure for a video-generation model on specialized TPU hardware. It contains no claims about coding agents, AI-assisted development workflows, or engineering practices for building *with* AI models — the optimization work described (Pallas kernel authoring, XLA flag tuning, sharding-strategy design) is traditional systems engineering, not agent-assisted engineering. This mirrors the Prospector's third triage comment, which explicitly flagged this source as topically off-scope and drew the same parallel to `blog-google-qwen35-ironwood-moe-optimization.md` that this note's Cross-References section confirms.
- **Weakest possible connection, flagged rather than forced**: Claim 10's two-tier output-quality gate (byte-identical hash check, then bounded-tolerance-plus-human-review for anything with a changed reduction order) is a generically reusable verification pattern — "define a tight automated check for the common case, and a human-in-the-loop fallback with an explicit, measured tolerance band for the rest" — that echoes the guide's Ch03 (Verification) themes of layered automated/human checks, but this guide's Ch03 content is about verifying AI-*generated code*, not verifying floating-point-reduction-order changes in a video-generation model's output. The parallel is structural, not substantive, and does not by itself justify a guide citation.

## Extraction Notes

- **Read the full post directly**, not just a WebFetch summary — used targeted follow-up fetches against the live URL to obtain verbatim quotes for each of the eleven claims (memory constraints, torchax, collective pipelining, mask deletion, softmax bound, layout/compiler-contracts section, quality-gate tiers, six-milestones summary, author/acknowledgements list, and section headings) rather than relying on a single paraphrased summary pass.
- **No sub-pages followed.** The post is self-contained and does not link out to external material its own claims depend on (unlike, e.g., `blog-google-qwen35-ironwood-moe-optimization.md`, which links to a Hugging Face model repo and third-party explainers for background).
- **One figure (Figure 5, "Layout is the ABI") is referenced but not itself analyzed** — its content is fully covered by the surrounding verbatim prose quoted in Claim 8 and the Concrete Artifacts section, so no information was lost by not visually inspecting the image.
- **Existing overlap checked before writing.** Searched `source-notes/*.md` for "TPU", "Trillium", "torchax", "Cauchy", "diffusion", "video generation", and "Pallas" before drafting. Found two topically-adjacent Google/TPU notes (`blog-google-qwen35-ironwood-moe-optimization.md`, `blog-google-tunix-agentic-rl-throughput.md`) and one roofline-methodology note (`blog-google-tpu-microbenchmarks-roofline.md`), none of which cover diffusion/video-generation inference, torchax, or the Cauchy-Schwarz softmax technique — confirmed net-new coverage, addressed in Cross-References. No contradiction with any existing note was found, so no contradiction issue was filed per MINER.md §4a.
- **Confidence rationale**: Set to `emerging` overall. The mechanism-level claims (Claims 3-10: memory constraints, torchax port, collective pipelining, mask elimination, softmax bound, layout fusion, compiler-flag contracts, quality-gate structure) are concrete, specific, and internally consistent, and rated `settled` individually. The headline performance claim (Claim 1, 1.86×/25% cost efficiency) and the milestone-ordering claim (Claim 11) remain self-reported, unverified-by-a-third-party vendor/customer joint claims (rated `anecdotal`/`settled-but-unreproduced` individually) — consistent with how this corpus treats other first-party Google performance-benchmark posts (see `blog-google-qwen35-ironwood-moe-optimization.md`'s same `emerging` overall rating with the same settled-mechanism/anecdotal-headline split).
- **Off-topic relative to this guide's scope, flagged explicitly rather than force-fit.** Per MINER.md's instruction to be specific about guide impact rather than vaguely gesture at relevance, this note states plainly in Guide Impact that the source has no direct chapter mapping, rather than inventing a connection to justify the extraction effort. The extraction itself remains thorough per MINER.md's requirement to read deeply regardless of eventual guide relevance.
