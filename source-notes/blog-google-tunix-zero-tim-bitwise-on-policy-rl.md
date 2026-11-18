---
source_url: https://developers.googleblog.com/unlocking-stable-on-policy-rl-on-tpu-with-bitwise-zero-traininference-mismatch/
source_type: blog-post
title: "Unlocking Stable On-Policy RL on TPU with Bitwise-Zero Train–Inference Mismatch"
author: "Yuxuan Zhang, Lin Chai, Lance Wang, Tianshu Bao, Weiren Yu (Google)"
date_published: 2026-11-16
date_extracted: 2026-11-18
last_checked: 2026-11-18
status: current
confidence_overall: anecdotal
issue: "#4799"
---

# Unlocking Stable On-Policy RL on TPU with Bitwise-Zero Train–Inference Mismatch

> Google Developers Blog post describing "Zero-TIM" in Tunix: a four-part kernel/collective recipe plus a three-path bitwise logprob diagnostic (sampler decode vs. serving prefill vs. trainer forward) that makes sampler and trainer logprobs bit-identical on a 64-chip TPU v5p mesh. It is RL-training infrastructure, far outside the guide's core scope; the only transferable idea is the bitwise, tolerance-free, multi-checkpoint equality check as a verification pattern.

## Source Context

- **Type**: blog-post (Google Developers Blog, Nov 16, 2026; first-party vendor engineering report with an open-source prototype in Tunix)
- **Author credibility**: Google engineers on the Tunix team (software engineers through senior staff, plus a product manager). First-hand implementers; two authors (Lance Wang, Tianshu Bao, Weiren Yu) also appear on other Tunix posts already in the corpus.
- **Scope**: Numerical alignment between the sampling and training paths in synchronous on-policy LLM RL on JAX/XLA/Pallas. Does not cover coding agents, harness design, or agent-assisted engineering. Evidence is a single-seed, 200-step FrozenLake run on Qwen3-8B; no downstream benchmarks, no performance/throughput cost of batch-invariant kernels is reported, and MoE / linear-attention are listed as future work.

## Extracted Claims

### Claim 1: Even in a synchronous, nominally on-policy RL loop, separate sampler and trainer execution paths create a hidden off-policy gap
- **Evidence**: Conceptual argument; no measurement of the baseline gap's size is given in the text (Figure 4 plots it but the text only says "nonzero").
- **Confidence**: settled (widely recognized in RL-for-LLM community; the post itself cites vLLM/TorchTitan and RadixArk/LMSys Miles work)
- **Quote**: "The training schedule is on-policy, but the numerical execution has introduced a hidden off-policy gap that compounds over multi-turn trajectories."
- **Our assessment**: Plausible and consistent with the community. The "compounds over multi-turn trajectories" part is asserted, not demonstrated here.

### Claim 2: Reduction order alone (non-associative floating-point addition) is enough to change logprob bits; the weights and equations are not the cause
- **Evidence**: A bfloat16 toy example (Figure 1: near 2.0, each 0.0078125 input is half the distance to the next representable value, so adding separately rounds each away while grouping first reaches the next value). Extended to matmul accumulation, normalization statistics, and tensor-parallel shard combination.
- **Confidence**: settled
- **Quote**: "The weights and model equations were identical; the arithmetic was not."
- **Our assessment**: Correct as a general numerics fact. The post also names JAX shape specialization and the differentiated training program as sources of divergence, so "reduction order alone" is a slight over-simplification of the post's own account (intermediate precision is also named).

### Claim 3: A three-path bitwise contract (sampler decode, serving prefill, trainer forward) with zero tolerance is a systematic diagnostic that localizes where mismatch enters
- **Evidence**: Design rationale; Figure 2 shows the comparison points. The post argues a two-way comparison shows a gap exists but not where.
- **Confidence**: emerging
- **Quote**: "Introducing serving prefill as a middle checkpoint turns alignment into a systematic two-step diagnostic that any RL stack can adopt:"
- **Our assessment**: The strongest transferable idea: when two paths must agree, add an intermediate checkpoint so that disagreement is bisectable, and compare raw bytes rather than using tolerances. "Any RL stack" is an unvalidated generalization, as only Tunix is shown.

### Claim 4: The contract is defined as exact byte equality under identical rollout weights, token history, and sampling settings
- **Evidence**: Definition in "The alignment contract" section.
- **Confidence**: emerging
- **Quote**: "comparing raw floating-point bytes under the same rollout weights, token history, and sampling settings, with zero rounding or tolerance."
- **Our assessment**: Strict equality is a binary, cheap-to-evaluate oracle, which is the property that makes it a good verification check. It is only achievable because the authors control the kernels.

### Claim 5: Zero-TIM does not need a monolithic engine; a four-part recipe bridges separate serving and training pipelines
- **Evidence**: Recipe description with code for the accumulation kernel and custom VJP.
- **Confidence**: emerging
- **Quote**: "locking within-shard kernel accumulation, ordering cross-shard reductions, standardizing the logprob scoring tail, and wrapping serving kernels with custom differentiation rules."
- **Our assessment**: Specific and implementable for JAX/Pallas teams. Whether it generalizes to PyTorch/GPU stacks is not shown by this post (it cites other efforts as parallel work).

### Claim 6: Within-shard fix: batch-invariant Pallas kernels with fixed contraction order and float32 accumulation
- **Evidence**: Kernel snippet (see Concrete Artifacts); covers attention/MLP projections and the LM head, with dedicated kernels for RMSNorm and SwiGLU casts; the existing Pallas paged-attention forward is retained.
- **Confidence**: emerging
- **Quote**: "Projection kernels traverse fixed contraction blocks in order, keeping the reduction blocking independent of token-row count."
- **Our assessment**: Standard batch-invariance technique. No throughput penalty is reported; an unmeasured cost.

### Claim 7: Cross-shard fix: make reduction order explicit in the program using ppermute plus fixed-order addition
- **Evidence**: Description only, no code.
- **Confidence**: emerging
- **Quote**: "The reduction order is explicit in the program rather than selected by a collective implementation."
- **Our assessment**: Sound principle (don't let a collective's implementation choose the order); cost versus all-reduce not reported.

### Claim 8: The logprob tail (sampling transforms, log-softmax, action selection) and token IDs must also be shared, not just model logits
- **Evidence**: Description; uses a fixed Pallas log-softmax and preserves sampled token IDs across environment turns (token-in/token-out).
- **Confidence**: emerging
- **Quote**: "Alignment must extend beyond model logits to the probability of the sampled action."
- **Our assessment**: A useful reminder that equality must be checked at the output actually consumed downstream, not at an intermediate tensor.

### Claim 9: The trainer reuses the serving forward kernels via custom VJPs, and XLA excess-precision must be disabled
- **Evidence**: Code for `serving_matmul` custom_vjp; flag `--xla_allow_excess_precision=false`; chunked long-trajectory evaluation with KV-cache gradients.
- **Confidence**: emerging
- **Quote**: "The differentiable replica mirrors the kernel’s accumulation and casts, but is used only to construct the pullback. Forward values still come from the serving Pallas kernel."
- **Our assessment**: Concrete, reproducible detail. The backward pass is not bitwise-checked; the contract covers forward logprobs only.

### Claim 10: Zero-TIM yields exactly zero mean absolute sampler–trainer logprob difference at every logged step and higher observed solve rates than Standard or TIS
- **Evidence**: 200-step FrozenLake run (grids 2×2–9×9, up to five turns), Qwen3-8B, 64 TPU v5p (DP8×TP8), GSPO-token loss with leave-one-out advantages; single seed (Figure 4). Comparisons: Standard, token-level truncated importance sampling (TIS), Zero-TIM.
- **Confidence**: anecdotal
- **Quote**: "Zero-TIM records zero mean absolute sampler–trainer logprob difference at every logged step in this window, while its training solve rate increases."
- **Our assessment**: The bitwise-zero result is a deterministic property and credible for the tested config. The solve-rate advantage rests on one seed on a synthetic toy environment; it is not evidence of better real-world RL outcomes. The post also notes comparison runs "retain their existing tokenization paths", a confound (TiTO applied only to Zero-TIM).

### Claim 11: Importance-sampling correction (TIS) reweights the update but does not remove the mismatch
- **Evidence**: Figure 4 shows nonzero differences for Standard and TIS.
- **Confidence**: emerging
- **Quote**: "TIS adjusts their contribution to the update without removing the underlying mismatch."
- **Our assessment**: Fair framing (fix the cause vs. compensate for the symptom), but the post does not show whether TIS runs are meaningfully worse in practice beyond the single-seed solve rates.

### Claim 12: Support is limited so far; the work is a prototype
- **Evidence**: Stated future work.
- **Confidence**: settled
- **Quote**: "we are actively extending support to linear-attention and Mixture-of-Experts (MoE) architectures."
- **Our assessment**: Dense-transformer only for now; MoE routing nondeterminism is a known harder case.

## Concrete Artifacts

Within-shard accumulation core (Google Developers Blog, "Fix within-shard arithmetic"):

```python
input_tile = x_ref[...]
weight_tile = y_ref[...]
partial = jnp.dot(
    input_tile,
    weight_tile,
    preferred_element_type=jnp.float32,
)
acc_ref[...] = acc_ref[...] + partial
out_ref[...] = acc_ref[...].astype(out_ref.dtype)
```

Custom VJP keeping serving kernel forward (same section "Differentiate the serving forward"):

```python
@jax.custom_vjp
def serving_matmul(inputs, weights):
    return pallas_matmul(inputs, weights)
def matmul_forward(inputs, weights):
    output = pallas_matmul(inputs, weights)
    return output, (inputs, weights)
def matmul_backward(saved, output_gradient):
    inputs, weights = saved
    _, pullback = jax.vjp(
        differentiable_matmul,
        inputs,
        weights,
    )
    return pullback(output_gradient)
serving_matmul.defvjp(matmul_forward, matmul_backward)
```

Compiler flag: `--xla_allow_excess_precision=false` passed via `XLA_FLAGS`.

Evaluation setup: 200 steps, FrozenLake (2×2 to 9×9, ≤5 turns), public Qwen3-8B, 64 TPU v5p chips, DP8×TP8 mesh, GSPO-token loss with leave-one-out advantages; arms = Standard (trainer-old logprobs), token-level TIS, Zero-TIM (+TiTO); single seed.

## Cross-References

- **Corroborates**: none directly. `blog-google-qwen3-embedding-tpu-precision.md` also treats TPU numerical parity as a first-class requirement (it uses cosine-similarity thresholds, whereas this post uses zero-tolerance bitwise equality, a different contract for a different problem).
- **Contradicts**: none found.
- **Extends**: `blog-google-tunix-agentic-rl-throughput.md` (same Tunix library; that note covers rollout/trainer pipeline throughput, this one covers numerical alignment between those paths). Also adjacent to `blog-google-tunix-autonomous-post-training-agents.md` and `blog-google-tunix-gemma-reasoning-hackathon.md` (Tunix usage, no numerics content).
- **Novel**: First note in the corpus on train–inference logprob mismatch, batch-invariant kernels, and bitwise-equality verification. Loosely related in spirit to determinism-focused notes such as `blog-fowler-joshi-deterministic-simulation-testing.md`, but those address software testing, not floating-point numerics.

## Guide Impact

- **Chapter 03 (verification)**: At most a one-line optional illustration: when two implementations must agree, use a zero-tolerance equality oracle with an intermediate checkpoint to localize disagreement. Not worth a section; the guide does not cover RL training. No other chapter changes recommended.
- Otherwise: no guide impact; retain as RL-infrastructure background for the Tunix note cluster.

## Extraction Notes

- Read the full article (fetched raw HTML and converted to text; all quotes copied from that text). Figures (1–4) are images; their captions were used, the plotted values were not extractable, so the magnitude of the baseline Standard/TIS logprob differences and the solve-rate numbers are not captured.
- The "Preview the current implementation" link target was not followed; the repository code was not inspected.
- No performance/overhead numbers were in the post. Evidence is single-seed on a synthetic environment, hence `anecdotal` overall.
