---
source_url: https://developers.googleblog.com/reproducing-olmo-3-7b-pre-training-in-maxtext-case-study-of-large-scale-training-on-tpus/
source_type: blog-post
title: "Reproducing OLMo 3 7B Pre-training in MaxText: case study of large scale training on TPUs"
author: "Gagik Amirkhanyan, Ran Ran, Aireen Mei, Matt Davidow (Google TPU Inference Software Engineering Team), with the AI2 Team"
date_published: 2026-09-24
date_extracted: 2026-09-25
last_checked: 2026-09-25
status: current
confidence_overall: emerging
issue: "#3700"
---

# Reproducing OLMo 3 7B Pre-training in MaxText: case study of large scale training on TPUs

> A joint Google/AI2 engineering case study reproducing AI2's OLMo 3 7B
> pre-training recipe (originally PyTorch/GPU) in JAX/MaxText on TPUs,
> centered on a discovered data-loader bug that silently deflated training
> loss and the four-surface held-out verification discipline that caught
> it — plus infrastructure-portability results (mid-run device-count
> resize, bit-exact resume after host failure, cross-hardware-generation
> reuse) and a hardware/model-shape co-design speedup.

## Source Context

- **Type**: blog-post (Google Developers Blog, published Sept. 24, 2026;
  discovered one day later via the trusted `google-developers` RSS feed).
  Byline lists four named Google TPU Inference Software Engineering Team
  authors (Gagik Amirkhanyan, Ran Ran, Aireen Mei, Matt Davidow) jointly
  credited with "AI2 Team" — a genuine cross-organization collaboration
  reproducing AI2's own released model, not a single vendor's self-report
  about its own model.
- **Author credibility**: First-party engineering account from the team
  that did the reproduction work, co-signed by the original model's
  creator (AI2). AI2's OLMo models are a well-known, independently
  released open-weight/open-recipe model family, so the reference the
  reproduction is checked against is external and publicly verifiable
  (AI2's own published OLMo 3 7B checkpoints/evals), not an internal-only
  baseline.
- **Scope**: Covers the engineering work of porting a PyTorch/GPU
  pre-training recipe (OLMo-core) to JAX/MaxText on TPU: model
  architecture conversion, optimizer/loss-masking parity, a data-pipeline
  bug and its detection, four-surface convergence verification at six
  step landmarks across a ~5.93T-token stage-1 run plus a stage-2
  mid-training anneal, infrastructure resilience (mid-run resize, host-
  failure resume), and one hardware/model-shape co-design speedup. Does
  **not** cover: downstream fine-tuning/RLHF, inference-serving
  performance, cost/pricing, or anything about how a practitioner
  operates an AI coding agent or harness — this is ML pre-training
  infrastructure and reproducibility methodology, not coding-assistant
  usage.

## Extracted Claims

### Claim 1: A PyTorch-on-GPU pre-training recipe can be reproduced faithfully in JAX-on-TPU, but "faithfully" must be measured by generalization (held-out metrics), not training loss alone
- **Evidence**: Stated as the article's own closing thesis, after walking
  through the full reproduction including the loss-deflation bug (Claim
  3) that would have looked like a win on training loss alone.
- **Confidence**: emerging (a single, first-party cross-framework
  reproduction instance — not an independently replicated methodological
  finding — but backed by the four-surface verification data reported
  in Claim 2 and the concrete counterexample in Claim 3)
- **Quote**: "The bottom line: a PyTorch-on-GPU pre-training recipe reproduces faithfully in JAX-on-TPU, but only "faithfully" if you measure generalization, not just training loss."
- **Our assessment**: This is the article's organizing claim and its most
  transferable lesson outside the TPU-specific context: the proxy metric
  you optimize against during a long run (training loss) can diverge from
  the property you actually care about (generalization/held-out
  performance) without any visible signal in the proxy itself. See Claim
  3 for the concrete mechanism that made this non-hypothetical here.

### Claim 2: The team verified convergence on four independent surfaces at six step landmarks spanning 915k steps, rather than relying on any single metric
- **Evidence**: Direct methodology statement under a "Does it converge?"
  section, enumerating the four surfaces used.
- **Confidence**: settled (a specific, checkable description of the
  verification protocol actually used, not an aspirational claim)
- **Quote**: "We verified convergence on four independent surfaces at six step landmarks spanning 915k steps: (1) Held-out C4 lm_loss, (2) 8-task lm-eval-harness suite, (3) Multi-domain held-out perplexity, (4) Token-level KL."
- **Our assessment**: Notable for combining a loss-based surface (held-out
  C4), a downstream-task surface (lm-eval-harness), a generalization
  surface across additional domains (multi-domain perplexity), and a
  distributional-similarity surface (token-level KL) — four different
  failure modes would each need to independently slip through for a
  divergence to go undetected. This is a stronger verification design
  than "held-out loss alone," which is itself already stronger than the
  "training loss alone" baseline Claim 3 shows was insufficient.

### Claim 3: A double-sharding bug in the Grain data loader caused repeated training examples, which artificially deflated training loss without affecting held-out performance — and would have shipped as a false "MaxText beats the reference" result if held-out eval hadn't already been a committed practice
- **Evidence**: Root-cause description plus the team's own account of why
  the bug was caught rather than shipped.
- **Confidence**: emerging (a specific, mechanistically explained,
  single-incident bug report — plausible and detailed, but not
  independently reproduced outside this one run)
- **Quote**: "MaxText's OLMo loader passed ShardOptions(shard_index, shard_count) to the Grain DataLoader while the index sampler was already sharding internally. Grain's shard_options doesn't just record metadata; it re-strides the sampler's index stream." ... "Training loss is not a convergence proof. The only reason we didn't ship a false "MaxText beats the reference" claim is that we'd committed to held-out eval at every landmark."
- **Our assessment**: This is the article's single most concrete, high-value
  finding: a specific double-sharding interaction (two independent layers
  each re-striding the same index stream) silently produced repeated data
  instances, which drove training loss down by up to -0.25 (per the
  Prospector's triage summary of the post) while held-out loss stayed
  flat — the exact failure mode Claim 1's thesis warns about, caught only
  because held-out evaluation was already a pre-committed practice rather
  than a reactive check added after a surprising result.

### Claim 4: The downstream-accuracy gap between the MaxText/TPU reproduction and AI2's PyTorch/GPU reference never exceeded ±0.005 macro accuracy across six evaluation landmarks, with the sign of the gap flipping direction four times
- **Evidence**: Direct quantitative comparison against the reference
  model's published evals.
- **Confidence**: emerging (a specific, quantified cross-framework parity
  result, but a single reproduction instance without independent
  third-party replication)
- **Quote**: "And the downstream-accuracy gap never exceeds ±0.005 macro across all six landmarks, with the sign flipping four times, exactly the random walk you'd expect from two faithful runs differing only in RNG and numerics"
- **Our assessment**: The sign-flipping detail is the load-bearing part of
  this claim — a gap that stayed on one side consistently would suggest a
  systematic bias (e.g., a persistent under- or over-estimate from a
  subtle implementation difference), whereas a gap that flips sign is
  consistent with pure numerical/RNG noise around true equivalence. This
  is a more rigorous framing than just reporting a small average gap.

### Claim 5: Storing Adam's optimizer moments (m/v) in bfloat16 instead of float32 silently degraded convergence — adding +0.93 to the loss over 1000 steps — because bfloat16's ~3-digit mantissa drops small early-warmup updates
- **Evidence**: A specific ablation-style finding described as "a gotcha
  worth its own paragraph," with a named mechanism (mantissa precision
  loss compounding over updates).
- **Confidence**: emerging (quantified and mechanistically explained, but
  a single-run finding rather than a swept ablation with multiple seeds)
- **Quote**: "Setting weight_dtype=bfloat16 silently demoted Adam's m/v moments via mu_dtype inheritance, adding +0.93 to the loss over 1000 steps: bf16's ~3-digit mantissa drops a fraction of every tiny early-warmup update, and it compounds."
- **Our assessment**: A concrete, actionable gotcha for anyone porting a
  training recipe between frameworks: a dtype setting intended for
  *weights* (`weight_dtype=bfloat16`) silently inherited into optimizer
  *state* via a `mu_dtype` default, a configuration-inheritance bug class
  distinct from Claim 3's data-pipeline bug but the same underlying
  lesson — silent precision/sharding defaults compound invisibly unless
  specifically checked for.

### Claim 6: After a host failure killed the training job at step 19,627, the run resumed from the step-19,500 checkpoint and re-trained the 127 lost steps with an exact bit-level match to the original run's loss and perplexity (Δ = 0.000), versus the ~0.01–0.4 scatter a broken resume produces
- **Evidence**: A real production incident (not a planned test) that
  produced a natural paired comparison, since the 127 steps had already
  been logged before the crash.
- **Confidence**: anecdotal (a single, unplanned incident — strong
  evidence for this one case, but an n=1 natural experiment, not a
  repeated or independently verified test)
- **Quote**: "Sixteen hours in, a host failure killed the jobset at step 19,627 (loss smooth right up to it: an infra blip, not a divergence). The run resumed from the step-19,500 checkpoint and re-trained the 127 lost steps, about six minutes of recompute on a 47,684-step run. Because those steps were already in the logs before the crash, the preemption handed us a free paired diff, and the re-trained loss matched the original exactly: Δ = 0.000 in both loss and perplexity at all 127 steps, against the ~0.01–0.4 scatter a broken resume produces."
- **Our assessment**: The framing of the ~0.01–0.4 scatter as the
  signature of "a broken resume" implies the team has independent
  experience with resume bugs that don't reproduce bit-exactly — making
  this incident a positive control confirming their resume mechanism
  (Claim 8's atomic weights+optimizer+iterator-state restore) actually
  works, discovered opportunistically rather than by design.

### Claim 7: The training run survived a mid-run capacity loss — from a 512-device slice down to a 128-device slice (losing three-quarters of capacity) — with no recipe change and fully preserved per-device throughput, only wall-clock-per-step changing
- **Evidence**: Direct incident description with before/after throughput
  numbers.
- **Confidence**: anecdotal (a single infrastructure event, not a planned
  systematic test of resize behavior)
- **Quote**: "at step ~1.05M we lost three quarters of our capacity, and the run resumed on a 128-device slice (one quarter the size) at the same global batch, with no recipe change. Per-device throughput was preserved (~510–513 TFLOP/s/device on both); only wall-clock per step changed (0.76 s → 3.05 s, the expected 4×)."
- **Our assessment**: "No recipe change" is the specific, checkable claim
  here — the same hyperparameters/sharding config ran correctly at both
  512 and 128 devices without manual retuning, and per-device efficiency
  didn't degrade at the smaller scale. This is a portability claim about
  the training infrastructure, distinct from Claim 9's planned strong-
  scaling test.

### Claim 8: Checkpointing was extended to carry the exact data-iterator position alongside model and optimizer state, so a resume atomically restores weights, optimizer state, and iterator position together
- **Evidence**: Direct architectural description of the checkpoint format
  change that enabled Claim 6's bit-exact resume.
- **Confidence**: settled (a specific, checkable description of what the
  team built, directly substantiated by the Claim 6 outcome)
- **Quote**: "The checkpoint now carries an iter item alongside the model items, and a resume restores weights, optimizer state, and the exact data-iterator position together, atomically."
- **Our assessment**: This is the mechanism behind Claim 6's result, not
  just an assertion — without atomic iterator-position restore, a resume
  could replay the wrong data shard or skip/repeat examples even with
  correct weight and optimizer restoration, which is exactly the kind of
  off-by-one error the team elsewhere warns "remain[s] invisible in loss
  curves" (per the Prospector's triage summary of the post's "Practical
  Lessons").

### Claim 9: Going from a 128-device slice to a 512-device slice (4x) at the same global batch size produced a 3.99x aggregate-throughput increase — approximately 100% strong scaling — in a 1000-step test
- **Evidence**: A dedicated, planned scaling test with a specific
  measured multiplier.
- **Confidence**: emerging (a specific, quantified benchmark result from
  a single 1000-step test; not repeated across multiple scale points or
  independently reproduced)
- **Quote**: "going from a 128-device slice to a 512-device slice (4×) at the same global batch gave a 3.99× aggregate-throughput increase, ≈100% strong scaling, in a 1000-step test."
- **Our assessment**: A near-linear scaling result this close to the
  theoretical 4x ceiling is a strong infrastructure claim — most large
  distributed-training scaling curves show meaningfully more falloff at
  this device-count multiplier due to communication overhead. Combined
  with Claim 7's resize result, both point to communication/sharding
  overhead not being the bottleneck for this recipe at these scales.

### Claim 10: Reshaping the attention head dimension from 32x128 to 16x256 aligned the tensor dimension to the TPU hardware and yielded a +12.4% throughput increase (571 vs. 508 TFLOP/s/device, or 49.6% vs. 44.2% MFU) with identical parameter count and FLOPs
- **Evidence**: A direct before/after architecture-shape ablation with
  matched FLOPs, isolating the effect to hardware alignment rather than
  a capability change.
- **Confidence**: emerging (a specific, quantified, matched-FLOPs
  ablation from a single measurement; consistent with — and adds a
  precise measured percentage to — the general TPU head-dim-alignment
  pattern described qualitatively elsewhere in this corpus, see
  Cross-References)
- **Quote**: "Reshaping to a head-dim of 256 perfectly aligns the tensor dimension to 256 with the hardware, entirely preventing idle compute cycles. This yields a +12.4% throughput increase (571 vs 508 TFLOP/s/device, or 49.6% vs 44.2% MFU) while keeping parameters and FLOPs completely identical."
- **Our assessment**: The "parameters and FLOPs completely identical"
  framing is what makes this a clean causal claim rather than a confound
  — the speedup is attributed specifically to hardware-shape alignment,
  not to a smaller or cheaper model. This is a directly actionable,
  quantified instance of the general head_dim-alignment pattern.

### Claim 11: The stage-2 mid-training anneal phase, run on TPU v5p (a different hardware generation than stage 1's Ironwood), achieved 57.4% MFU with zero v5p-specific tuning
- **Evidence**: Direct cross-generation portability result.
- **Confidence**: emerging (a specific quantified result from a single
  run; "zero v5p-specific tuning" is the team's own characterization of
  their process, not independently audited)
- **Quote**: "With no v5p-specific tuning it landed at 57.4% MFU (263 TFLOP/s/chip median, of v5p's 459 peak)"
- **Our assessment**: This is a portability claim distinct from Claims 7
  and 9 (which are about device *count*, not hardware *generation*) — the
  recipe and its tuning carried over from Ironwood to v5p without
  per-generation retuning and still achieved a majority-of-peak MFU,
  suggesting the recipe's efficiency gains (e.g., Claim 10's head-dim
  alignment) are not narrowly overfit to one chip generation.

### Claim 12: Reproducing the model required converting several OLMo-core-specific architecture and training details into MaxText: reordered-norm transformer blocks, QK-norm, a 3:1 sliding/global attention pattern, a skip-step optimizer matching OLMo-core's Bessel-corrected 6-sigma/128-step-window skip semantics, z-loss, and per-parameter weight-decay masking (to exclude embeddings)
- **Evidence**: Direct enumeration of implementation work, each item
  cross-referenced to a specific tracked issue/PR number in the source.
- **Confidence**: settled (a specific, itemized description of concrete
  engineering work performed, each traceable to a named tracking number
  in the source rather than a vague summary)
- **Quote**: "The model itself: the reordered-norm block, QK-norm, and the 3:1 sliding/global attention pattern (#3004, #3112)." ... "A skip-step optimizer matching OLMo-core's semantics down to the Bessel-corrected running std (skip at 6σ over a 128-step window) (#3490)." ... "z-loss (#3211) and per-parameter weight-decay masking so embeddings can be excluded (#3280)."
- **Our assessment**: The level of specificity here (exact sigma threshold,
  exact window size, named issue numbers) signals this was matched to
  OLMo-core's actual implementation rather than approximated — relevant
  context for Claim 4's tight accuracy-gap result, since architecture and
  optimizer fidelity at this level of detail is a precondition for a
  faithful reproduction, not incidental to it.

## Concrete Artifacts

### Double-sharding bug root cause (verbatim from the post, "The bug that looked like a win" section)

```
MaxText's OLMo loader passed ShardOptions(shard_index, shard_count) to the
Grain DataLoader while the index sampler was already sharding internally.
Grain's shard_options doesn't just record metadata; it re-strides the
sampler's index stream.
```

### Four-surface verification protocol (verbatim from the post, "Does it converge?" section)

```
We verified convergence on four independent surfaces at six step
landmarks spanning 915k steps:
(1) Held-out C4 lm_loss
(2) 8-task lm-eval-harness suite
(3) Multi-domain held-out perplexity
(4) Token-level KL
```

### Architecture/optimizer conversion checklist (verbatim from the post, with source-tracked issue numbers)

```
The model itself: the reordered-norm block, QK-norm, and the 3:1
sliding/global attention pattern (#3004, #3112).
A skip-step optimizer matching OLMo-core's semantics down to the
Bessel-corrected running std (skip at 6σ over a 128-step window) (#3490).
z-loss (#3211) and per-parameter weight-decay masking so embeddings can
be excluded (#3280).
```

### Byline (verbatim from the post)

```
SEPT. 24, 2026 | Gagik Amirkhanyan, Ran Ran, Aireen Mei, Matt Davidow,
TPU Inference Software Engineering Team, AI2 Team
```

Source for all four artifacts above: developers.googleblog.com/reproducing-olmo-3-7b-pre-training-in-maxtext-case-study-of-large-scale-training-on-tpus/.

## Cross-References

- **Corroborates**: `blog-google-tpu-microbenchmarks-roofline.md` Claim 5
  (Ironwood/TPU7x's 256x256 systolic array makes `head_dim=128` — common
  in older Llama variants — less optimal than 256-aligned shapes; stated
  qualitatively with no throughput delta given) — this note's Claim 10
  supplies an independent, precisely quantified instance of the same
  underlying hardware-alignment pattern (32x128 → 16x256 reshaping, exact
  +12.4%/571-vs-508-TFLOP/s-per-device delta with matched FLOPs), for a
  different model family (OLMo vs. Llama-shaped attention) and a
  different mechanism description (data-pipeline/optimizer-conversion
  case study vs. general microbenchmarking methodology post).
- **Contradicts**: None identified. No existing source note takes a
  position on TPU data-loader sharding semantics, cross-framework
  pre-training reproduction, or checkpoint/resume atomicity that this
  post's claims oppose.
- **Extends**: `blog-google-tpu-microbenchmarks-roofline.md` and
  `blog-google-tunix-agentic-rl-throughput.md` as the corpus's third
  Google/TPU large-scale-training infrastructure source, but the first to
  document a full end-to-end cross-framework (PyTorch→JAX) *pre-training
  reproduction* rather than a benchmarking methodology or an RL-training
  infrastructure design. It extends the microbenchmarks note's Roofline/
  MFU framing with concrete measured MFU values (44.2%/49.6% stage 1,
  57.4% stage 2) from an actual production-scale training run rather than
  a diagnostic tool description.
- **Novel**: This is the corpus's first source documenting: (1) a
  cross-organization (Google + AI2), cross-framework (PyTorch/GPU →
  JAX/TPU) full pre-training reproduction of a named, externally released
  open model; (2) the specific double-sharding data-loader bug class
  (`ShardOptions` re-striding an already-sharded index sampler) and the
  "training loss is not a convergence proof" lesson it produced; (3) the
  bfloat16-optimizer-moment-demotion gotcha (`weight_dtype` silently
  inheriting into `mu_dtype`) with a quantified +0.93 loss cost; (4) a
  bit-exact (Δ=0.000) checkpoint-resume verification from an actual
  unplanned host failure, rather than a planned resume test; (5) a
  mid-run device-count resize (512→128) surviving with no recipe change;
  (6) cross-hardware-generation (Ironwood→TPU v5p) recipe portability
  without generation-specific retuning.

## Guide Impact

Following the same independent assessment reached by this corpus's two
prior Google/TPU source notes (`blog-google-tpu-microbenchmarks-roofline.md`,
`blog-google-tunix-agentic-rl-throughput.md`): this article documents ML
*pre-training* infrastructure and reproducibility engineering — porting a
model-training recipe across frameworks and hardware, verifying training
convergence, and surviving training-cluster infrastructure events — not
guidance about how a practitioner builds, configures, or operates an AI
coding agent or harness. The guide's actual chapters (confirmed by reading
`guide/*.md` headers directly: 00-principles, 01-daily-workflows,
02-harness-engineering, 03-verification, 04-context-engineering,
05-team-adoption, 06-security-threat-model) address working *with*
deployed AI coding agents in a software-engineering context — none covers
model pre-training, ML training-cluster infrastructure, or accelerator
performance tuning.

- **No direct chapter impact recommended.** None of Claims 1-12 describes
  a harness-configuration practice, an AI-generated-*code* verification
  technique, a context-management pattern, a team-adoption process, or a
  security consideration for coding-agent usage. The Prospector's two
  triage comments proposed Ch01/Ch04/Ch05/Ch06 relevance (infrastructure
  portability, production validation, platform-engineering resilience),
  but on reading the full article its subject is model pre-training
  infrastructure for a different audience (ML infra/training engineers
  reproducing a base model) and a different lifecycle stage (training a
  model from scratch, not using an already-trained coding assistant) than
  any existing chapter addresses. Note also that this guide currently has
  no chapter numbered 01/04/05/06 matching the Prospector's proposed
  topics as stated — the actual chapter list is 00-principles through
  06-security-threat-model as enumerated above; the closest matches by
  content are 03-verification (not 04/06) and 05-team-adoption, and
  neither covers ML training infrastructure.
- **Weak, indirect analogy only, flagged rather than forced**: Claim 1's
  thesis — the metric you're directly optimizing (training loss) can look
  fine while the property you actually care about (generalization)
  silently degrades, unless you deliberately verify against a held-out,
  independent surface — is the same *shape* of discipline
  `03-verification.md`'s opening thesis argues for (do not trust that
  "the diff looks reasonable" is equivalent to correctness; build layered
  verification because a single signal will miss failures). But the
  specific mechanism (data-loader index-sharding bugs, optimizer dtype
  inheritance, checkpoint iterator-state atomicity) has no transferable
  detail for a coding-harness context — an AI coding agent's "training
  loss equivalent" (e.g., a green CI run, an agent's own self-report of
  success) is a structurally different kind of proxy metric than a
  numerical training loss. If the guide ever adds content on the
  economics/mechanics of self-hosting, fine-tuning, or reproducing models
  for agentic-coding workloads, this post (together with the other two
  TPU notes) would be background reading for that new scope, not a
  citation for any existing section.

## Extraction Notes

- The article could not be retrieved as clean raw text in one pass — the
  WebFetch tool returned a summarized/paraphrased version on a broad
  "reproduce the full article" request, and one intermediate request
  returned a spurious clarifying question about a character-limit
  constraint that was never actually specified in this extraction (an
  apparent tool-side artifact, disregarded). All `Quote` fields above were
  obtained through several follow-up requests, each scoped to a specific
  named claim/section, and cross-checked against each other for internal
  consistency (e.g., the double-sharding root cause and the bfloat16
  finding were independently re-requested and returned identical wording
  across separate fetches) before being used as direct quotes.
- Numeric figures mentioned only in the Prospector's triage comments and
  not independently re-verified as exact source quotes in this extraction
  (the -0.25 training-loss deflation magnitude, the 57.4% MFU headline
  figure as a standalone summary claim) are attributed to "the Prospector's
  triage summary of the post" rather than presented as `Quote` fields,
  per MINER.md's rule against fabricating quotes — the 57.4% MFU figure
  *was* independently confirmed as a verbatim quote (Claim 11) with its
  own TFLOP/s-per-chip detail, but the -0.25 figure was not re-confirmed
  verbatim and is flagged as such in Claim 3's assessment rather than
  quoted directly.
- No sub-pages were followed. The article did not surface links to
  additional substantive pages (e.g., a separate design doc, GitHub PR,
  or the referenced issue-tracker numbers themselves) through the
  targeted fetches performed; the cited issue/PR numbers (#3004, #3112,
  #3490, #3211, #3280) are reproduced as they appear in the source text
  but were not independently opened or verified against a live tracker.
- **Existing overlap checked before writing.** Searched `source-notes/`
  for Google/TPU-related notes and read the two most relevant in full
  (`blog-google-tpu-microbenchmarks-roofline.md`,
  `blog-google-tunix-agentic-rl-throughput.md`, both named by the
  Prospector) plus scanned the full source-notes directory listing for
  other MaxText/TPU/checkpoint/data-loader coverage — found no other
  overlapping notes. No contradiction issue was filed: this source does
  not oppose any claim in either related note or any other existing
  source note.
- **Confidence rationale**: Set to `emerging` overall. The architectural/
  methodological description of what was built (Claims 2, 8, 12) is
  specific and checkable, rated `settled` individually. The core bug-
  discovery narrative and its quantified outcomes (Claims 1, 3, 4, 5, 9,
  10, 11) are precisely described and mechanistically explained but rest
  on a single reproduction run with no independent third-party
  replication, rated `emerging` individually. The two unplanned
  infrastructure incidents (Claims 6, 7) are strong evidence for their
  specific instance but are n=1 natural experiments rather than
  systematic tests, rated `anecdotal` individually. The overall `emerging`
  rating reflects that the methodology and architecture-conversion work
  is solidly documented while the standout numeric results are single-run,
  first-party figures without independent reproduction.
- **Off-topic relative to this guide's scope, flagged explicitly rather
  than force-fit.** Per MINER.md's instruction to be specific about guide
  impact rather than vaguely gesture at relevance, this note states
  plainly in Guide Impact that the source has no direct chapter mapping,
  consistent with the two prior Google/TPU notes' independent conclusions
  reaching the same result, and explicitly flags that the Prospector's
  proposed chapter numbers (01/04/05/06 for infrastructure/production-
  validation/platform-engineering topics) do not match this guide's
  actual seven-chapter structure as read directly from `guide/*.md`.
