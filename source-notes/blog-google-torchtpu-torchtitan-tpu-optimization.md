---
source_url: https://developers.googleblog.com/integrating-torchtpu-into-torchtitan-and-optimizing-models-for-tpu/
source_type: blog-post
title: "Integrating TorchTPU into TorchTitan and Optimizing Models for TPU"
author: "Aleksey Vlasenko, Rob Torres (Google); Will Constable (Meta)"
date_published: 2026-10-20
date_extracted: 2026-10-21
last_checked: 2026-10-21
status: current
confidence_overall: emerging
issue: "#4250"
---

# Integrating TorchTPU into TorchTitan and Optimizing Models for TPU

> A vendor co-authored (Google + Meta) ML-training-infrastructure post describing a staged TPU optimization playbook for PyTorch/TorchTitan, with vendor-reported MFU results; its only guide-relevant elements are the "ordered optimization ladder with a check after every change" method and a repository skill for agent-assisted model porting.

## Source Context

- **Type**: blog-post (Google Developers Blog, 2026-10-20), discovered via trusted feed `google-developers`.
- **Author credibility**: Two Google authors plus Will Constable of Meta's TorchTitan team. First-party engineering authors; all performance figures are vendor-reported with no independent reproduction.
- **Scope**: Native `torch.device("tpu")` backend (TorchTPU), the TorchTitan TPU fork, SimpleFSDP, Graph Trainer, Pallas kernels, a four-stage optimization playbook, case studies (FLUX.1, Muse Glimmer 30B, Qwen3-235B-A22B, plus Llama 3 405B and Qwen3-8B figures), a Hugging Face modeling backend, an agent-onboarding skill, and a roadmap. Does not cover AI-assisted software-engineering practice beyond the one skill mention.

## Extracted Claims

### Claim 1: SimpleFSDP replaces FSDP2 on TPU because expressing sharding as DTensor parametrizations makes collectives ordinary graph nodes that the compiler can see
- **Evidence**: Architecture explanation in the "Compile-Friendly FSDP Implementation" section; FSDP2's hooks and CUDA streams are described as invisible to compilers.
- **Confidence**: emerging (design rationale; benefit shown only through the post's aggregate results)
- **Quote**: "There are no hooks and no explicit collective calls, so both collectives are ordinary nodes in the traced graph"
- **Our assessment**: A plausible, specific mechanism. Whole-program compilers need all communication to be visible in the traced graph. The post does not isolate SimpleFSDP's contribution with an ablation outside the FLUX ladder.

### Claim 2: Graph Trainer captures the full training step as one XLA program, enabling whole-step compilation, scan over layers and a graph splitter with host activation offload for large models
- **Evidence**: Described in "Graph Trainer: Capturing the Entire Training Step"; Qwen3-235B (94 layers) reported feasible only via scan or the graph splitter; Qwen3-8B reaches 51–52% MFU with a functional AdamW traced into the step.
- **Confidence**: emerging (vendor-reported)
- **Quote**: "TorchTitan's Graph Trainer provides full training-step capture (forward, loss and backward)"
- **Our assessment**: Concrete and plausible, but MFU numbers are unreproduced vendor claims. Out of scope for the guide.

### Claim 3: A four-stage ordered optimization playbook (baseline → compute/kernels → memory/batch size → compiler/communication/profiling) is the recommended route to good TPU MFU
- **Evidence**: "TPU Model Optimization Playbook" section; stages detailed in the Concrete Artifacts below; applied across the case studies.
- **Confidence**: emerging
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The transferable pattern is a staged ladder, cheapest/most-general levers first, measuring after each rung and returning to the lever that addresses the observed bottleneck — a generic performance-engineering method also applicable to agent-harness tuning.

### Claim 4: Compiler/communication flags can silently change numerics, so loss and gradient norm must be checked after every flag sweep
- **Evidence**: Stated in playbook step 4 ("Tune Compiler, Communication and Profile").
- **Confidence**: emerging (practitioner guidance, no data given)
- **Quote**: "a flag that alters fusion or the order of a reduction, hierarchical reduce-scatter being one, shifts rounding."
- **Our assessment**: Good verification discipline: performance changes are not "free" and need a correctness check after each step. The follow-on sentence in the post, "So check the step-1 loss and gradient norm after every sweep.", is the actionable rule.

### Claim 5: FLUX.1 (12B DiT) on TPU v6e-8 went from 11.49 s to 2.78 s per step (~4.1x), reaching about 99% of JAX MaxDiffusion throughput
- **Evidence**: Stepwise ladder (deferred-and-fused eager, SimpleFSDP, splash attention, per-block compile, three small model-code rewrites), each step measured; scaled to 1,024 v7x chips at 19.4% MFU with 93% weak-scaling efficiency.
- **Confidence**: emerging (vendor-reported; per-step measurements give more rigor than a bare headline multiplier)
- **Quote**: "Together they brought the step to 2.78 s (8.6% improvement), 4.1x faster than the starting point"
- **Our assessment**: The per-rung measurement is the valuable element. The 99%-of-MaxDiffusion parity claim is a vendor self-comparison.

### Claim 6: Large-model MFU results: Qwen3-235B MoE 32.42% MFU on a single 1,024-chip slice; Llama 3 405B ~57%; Muse Glimmer 30B ~44% on 64 v7x chips
- **Evidence**: "Case Studies" section; Qwen3-235B per-chip throughput dropped 8% from 64 to 8,192 chips in a weak-scaling HSDP test.
- **Confidence**: anecdotal (vendor-reported, not reproduced)
- **Quote**: "Qwen3 235B (large MoE model) reaches 32.42% MFU on a single 1,024-chip slice"
- **Our assessment**: Note the triage comments disagree slightly on Qwen3-235B figures (29%+ vs 32.42%/30.51%); the article's own text gives 32.42% for the single slice. Cite as vendor-reported only.

### Claim 7: Hugging Face models can run through TorchTitan's trainer on TPU via a Transformers modeling backend, with limited optimization and a stated MoE gap
- **Evidence**: "HuggingFace Transformers modeling backend for TorchTitan TPU" section; first playbook optimizations applied but no hand tuning.
- **Confidence**: emerging
- **Quote**: "mixture-of-experts checkpoints run through the same path but without expert parallelism yet."
- **Our assessment**: An honest limitation statement; useful as an example of a vendor documenting what does not work yet.

### Claim 8: A repository skill guides engineers or coding agents through porting models to TorchTitan TPU using the same optimization ladder, with tests and acceptance criteria
- **Evidence**: "Agent-assisted Model Onboarding to TorchTitan TPU" section; the skill is said to encode how the case studies were done. The post gives no results on agent success rates.
- **Confidence**: anecdotal (assertion of existence, no outcome data)
- **Quote**: "for coding agents that captures how the case studies above were done"
- **Our assessment**: The only direct overlap with the guide's scope: encoding a hard-won human optimization playbook (ordered steps + tests + acceptance criteria) as a skill that agents follow. No evidence is offered that it works.

## Concrete Artifacts

Playbook structure (paraphrased from the "TPU Model Optimization Playbook" section; not verbatim):

```
1. Baseline: eager for bring-up -> per-block torch.compile or Graph Trainer;
   SimpleFSDP with bf16 params + fp32 gradient reduction; scan/graph splitter
   + activation host-offload for ~100B+ models.
2. Compute & kernels: Pallas kernels (Splash Attention, fused cross-entropy,
   MoE grouped matmul); tune tile sizes per model/TPU generation.
3. Memory & batch size: raise per-chip batch until HBM-bound.
4. Compiler, communication, profiling: tune XLA/libtpu flags, check step-1 loss
   and grad norm after every sweep; profile with xprof; revisit the bottleneck lever.
```

Reported results (vendor-reported): FLUX.1 11.49 s -> 2.78 s on v6e-8; Qwen3-8B 51–52% MFU (functional AdamW in graph); Llama 3 405B ~57% MFU on 128–1,024 chips; Muse Glimmer 30B ~44% MFU on 64 v7x chips; Qwen3-235B-A22B 32.42% MFU on 1,024 chips.

## Cross-References

- **Corroborates**: `blog-google-qwen35-ironwood-moe-optimization.md` — both are staged TPU performance playbooks with modular reusable building blocks (that note's Claim 1) and both treat correctness verification as part of optimization (that note's Claim 9, Numerical Verification Layer vs. this post's Claim 4).
- **Contradicts**: None found.
- **Extends**: `blog-google-svg-splash-attention-video-diffusion-tpu.md` and `blog-google-tpu-microbenchmarks-roofline.md` (Splash Attention and TPU performance methodology) by showing how those kernels plug into a PyTorch training stack.
- **Novel**: TorchTPU / `torch.device("tpu")`, TorchTitan TPU fork, SimpleFSDP, and Graph Trainer are new to the corpus (no existing note covers them); also the repository skill for agent-assisted model porting.

## Guide Impact

- **No chapter change recommended.** The content is ML-training infrastructure outside the guide's scope. Consistent with the prior TPU notes mined with no chapter impact.
- **Chapter 03 (verification), weak/optional**: Claim 4 ("check loss/grad norm after every flag sweep") is a minor illustration of verify-after-each-change, only if the Smith wants a non-coding-agent example.
- **Chapter 02 (harness engineering), weak/optional**: Claim 8 is a minimal example of packaging an optimization playbook as an agent skill; too thin (no outcome data) to cite as evidence.

## Extraction Notes

- Read via fetch tool, which returned a summary rather than full verbatim text; quotes were obtained by separately requesting short exact passages. The Assayer should spot-check them against the URL.
- No sub-pages followed. Playbook artifact is a paraphrase, labeled as such.
- Triage flagged the topic as low-fit; extraction kept to claims with possible transferable value.
