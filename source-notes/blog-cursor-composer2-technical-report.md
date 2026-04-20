---
source_url: https://cursor.com/blog/composer-2-technical-report
source_type: blog-post
title: "A Technical Report on Composer 2"
author: Cursor Research (54 authors; Aaron Chan, Alexander Wettig et al.)
date_published: 2026-03-27
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#194"
---

# A Technical Report on Composer 2 (Cursor Research)

> Cursor's full technical account of how Composer 2 was built and evaluated:
> two-phase training (continued pretraining on Kimi K2.5 + large-scale async RL
> inside a production-identical harness), a custom Anyrun sandbox platform scaling
> to hundreds of thousands of concurrent environments, and CursorBench-3 — the
> clearest public benchmark design rationale showing why realistic multi-file,
> terse-prompt tasks are needed where SWE-bench has 7-10 median LOC changed vs.
> Composer's 181.

## Source Context

- **Type**: blog-post (front-end summary of arXiv:2603.24477; 54-author technical
  report from Cursor Research, March 2026)
- **Author credibility**: 54 Cursor Research engineers — this is a full technical report,
  not a marketing summary. The arXiv version includes training hyperparameters, ablation
  data, and infrastructure specifics. Cursor has production deployment and live traffic
  validation unavailable to external researchers. Claims about CursorBench, Anyrun, and
  training recipes are first-party and authoritative for their own system. Incentive to
  present Composer favorably is real but constrained by technical specificity — the paper
  includes unflattering details (NVFP4 training divergence, infrastructure failures, model
  limitations vs. GPT-5.4).
- **Scope**: Covers model selection, continued pretraining, RL training design, custom
  low-precision kernels, asynchronous RL infrastructure, Anyrun sandbox platform, CursorBench
  design rationale and quantitative characteristics, benchmark results vs. frontier models,
  and ablation findings. Does NOT cover: harness engineering patterns for practitioners
  (that is `blog-cursor-cursorbench.md` and `blog-cursor-composer-self-summarization.md`),
  pricing, context window limits, or CLAUDE.md-style configuration.

## Extracted Claims

### Claim 1: Kimi K2.5 was selected as base model over DeepSeek V3.2 and GLM-5 using internal benchmarks focused on coding fitness

- **Evidence**: Explicit model evaluation described: Kimi K2.5 was chosen by testing all
  three on FreshBench (measuring knowledge recency), state tracking tasks, and codebase
  perplexity. Kimi K2.5 is a 1.04 trillion parameter mixture-of-experts model with 32 billion
  active parameters.
- **Confidence**: emerging (first-party account; evaluation criteria are specific but the
  raw comparative numbers are not published)
- **Quote**: Evaluated "DeepSeek V3.2 and GLM-5 on internal benchmarks (FreshBench, state
  tracking, codebase perplexity)"
- **Our assessment**: The fact that Cursor evaluated three frontier MoE bases before
  selecting one is a transferable lesson for organizations building domain-specialized agents:
  base model selection should be driven by domain-specific fitness criteria (here: code
  knowledge, long-context state tracking, codebase familiarity), not general benchmark
  leaderboards. The 32B-of-1.04T active-parameter ratio is also relevant context for
  practitioners reasoning about inference cost on MoE models.

### Claim 2: Training inside a production-identical harness is the primary mechanism for closing train-test mismatch in specialized agents

- **Evidence**: Described as a core design principle: "RL training uses realistic Cursor
  sessions with the same tools and harness the deployed model uses." The problem distribution
  "reflects actual user workflows: debugging, refactoring, feature development, version control
  resolution, and long-running job monitoring — categories largely absent from public benchmarks."
- **Confidence**: emerging (first-party description; the architectural principle is clearly
  stated; causal attribution to train-test mismatch is the Cursor team's own analysis)
- **Quote**: "RL training happens in realistic Cursor sessions" with "equivalent tools,
  structures, and environments matching real problems"
- **Our assessment**: This is the practitioner-facing lesson from the entire training
  methodology. If you are building a specialized coding agent, training in a synthetic
  environment that differs from deployment is a structural source of performance degradation.
  The fix is environment fidelity. The Anyrun platform (Claim 6) is how Cursor operationalizes
  this at scale. For practitioners using Claude Code or other harnesses: this is why using the
  actual tool in eval matters more than using a cleaned-up synthetic version.

### Claim 3: CursorBench tasks have 181 median lines changed vs. 7-10 for SWE-bench, and 390-character descriptions vs. 1,185-3,055 for public benchmarks

- **Evidence**: Concrete quantitative characterization of CursorBench-3 vs. SWE-bench
  variants and Terminal-Bench. These are the first published numbers characterizing the scale
  and underspecification gap between real developer sessions and public benchmarks.
- **Confidence**: emerging (first-party measurement on their own benchmark; the SWE-bench
  comparison numbers are independently verifiable from the SWE-bench dataset)
- **Quote**: "Median 181 lines changed (vs. 7-10 for SWE-bench)" and "Median description
  length 390 characters (vs. 1,185-3,055 for public benchmarks)"
- **Our assessment**: These numbers are the quantitative anchor for the claim that public
  benchmarks do not measure real developer work. The ~18-26x LOC gap is stark: SWE-bench
  tasks are patch-fixing, not feature development. The description length inversion is equally
  striking: real developer requests are shorter AND the tasks are larger — the inverse of what
  public benchmarks assume. This is the strongest empirical support in our corpus for the
  claim that teams should build internal evals from real sessions rather than using public
  benchmarks.

### Claim 4: Composer 2 achieves 61.3% on CursorBench (37% relative improvement over Composer 1.5) at Pareto-optimal cost vs. comparable frontier models

- **Evidence**: Full comparison table: Composer 2 61.3%, Composer 1.5 44.2%, Composer 1
  38.0%, Kimi K2.5 base 36.0%. Against frontier models: GPT-5.4 63.9%, Opus 4.6 High 58.2%.
  On public benchmarks: SWE-bench Multilingual 73.7% (vs. Composer 1.5: 65.9%),
  Terminal-Bench 61.7% (vs. Composer 1.5: 47.9%). Cost is described as "similar to smaller
  or low-effort variants of models" while maintaining frontier accuracy.
- **Confidence**: emerging (first-party numbers on their own benchmark; public benchmark
  numbers are reproducible; cost claim is relative without absolute figures)
- **Quote**: "61.3% accuracy on CursorBench, representing a 37% relative improvement over
  Composer 1.5"; "superior Pareto frontier in cost while remaining highly competitive in
  token efficiency"
- **Our assessment**: The positioning is clear: Composer 2 is competitive with GPT-5.4 on
  CursorBench (61.3 vs 63.9) while beating Opus 4.6 High (58.2), at inference costs
  closer to smaller models. The 37% improvement over Composer 1.5 validates the combined
  pretraining + RL recipe. The Kimi K2.5 baseline of 36.0% vs Composer 2's 61.3% shows the
  net gain from specialization: 25.3 percentage points from continued pretraining + RL on top
  of a frontier base. For practitioners: a well-specialized domain model can approach or match
  frontier general models at substantially lower cost, which is actionable for model selection.

### Claim 5: RL training improves both average and best-of-K performance simultaneously, suggesting the model learns new solution paths rather than redistributing probability over known ones

- **Evidence**: Figure 5 in the paper: "both average and best-of-K metrics improve
  simultaneously." The team explicitly contrasts this with "recent literature suggesting RL
  concentrates probability on known trajectories at diversity cost."
- **Confidence**: emerging (vendor measurement on their own benchmark; the contrast with
  prior literature is their interpretation)
- **Quote**: "RL is not merely reweighting a fixed pool of reasoning paths, but is also
  improving the model's effective coverage of correct solutions"
- **Our assessment**: This is a significant finding for practitioners designing multi-attempt
  agent strategies. If RL improved only average performance, it would mean the model got
  better at its existing approach. Improving best-of-K means the model discovers new solution
  paths under sampling. This means that in a best-of-N architecture (run the agent N times,
  select the best result), a RL-trained model will improve more than a purely SFT model as
  N increases. This extends the context in `blog-cursor-cursorbench.md` about evaluation
  methodology: if you test Composer 2 with best-of-5, you capture a different capability
  profile than best-of-1.

### Claim 6: Anyrun is an internal platform supporting 500+ pods/second scheduling with Firecracker VMs, filesystem/memory forking, and transparent traffic control — enabling hundreds of thousands of concurrent sandboxed coding environments

- **Evidence**: Specific infrastructure description: "Scheduling throughput exceeding
  500 pods/second with awareness of live hardware pressure. Firecracker VMs supporting full
  development environments (browser, GUI). Forking/snapshotting at filesystem and memory
  levels. Anygress for transparent traffic control without proxy environment variables."
- **Confidence**: emerging (first-party description of proprietary infrastructure; numbers
  are specific and internally consistent with the claimed scale of RL training)
- **Quote**: "Anyrun platform: internal system running hundreds of thousands of sandboxed
  coding environments"
- **Our assessment**: Anyrun is the production-scale version of the "run the agent in a real
  environment" principle. Key innovations for the harness engineering field: (1)
  fork/snapshot at filesystem AND memory level means environments can be cheaply replicated
  and branched for parallel rollouts, (2) Firecracker supports GUI tools (not just CLI), (3)
  Anygress transparent traffic control means the model's tools don't need proxy awareness.
  For practitioners building their own agent evaluation environments: the fork/snapshot
  capability is the single most powerful feature — it enables rollback and branching without
  re-running expensive setup steps.

### Claim 7: Continued pretraining on Kimi K2.5 uses three stages: 32k sequences → 256k long-context extension → SFT on targeted coding tasks, on NVIDIA B300 GPUs with MXFP8 precision

- **Evidence**: Three-phase pretraining structure described explicitly. Hardware: B300 GPUs
  (next-generation Blackwell). Precision: MXFP8 with AdamW optimization. Multi-token
  prediction layers trained via self-distillation supporting speculative decoding at inference.
- **Confidence**: emerging (first-party description; technical specifics are verifiable in
  principle)
- **Quote**: "Extended training at 32k token sequences, long-context extension to 256k
  sequences, and supervised fine-tuning on targeted coding tasks"
- **Our assessment**: The 256k long-context extension is notable — it's a deliberate design
  decision for coding tasks that span large codebases. The multi-token prediction via
  self-distillation is both a training technique and an inference optimization (enables
  speculative decoding). For teams building domain-specialized models: the three-phase
  structure (general adaptation → long context → task-specific SFT) is a transferable recipe.

### Claim 8: RL training replaces the standard KL divergence estimator (k₃) with k₁ = −log r to prevent variance explosion at large divergence values

- **Evidence**: Technical description citing external research: "The team replaced standard
  k₃ estimator with k₁ = -log r due to variance explosion at large divergence values." This
  is a specific numerical stability fix applied during RL at scale.
- **Confidence**: emerging (cites prior research; specific numerical choice is described with
  a clear rationale)
- **Quote**: "k₃ produces unreliable estimates when distributions diverge significantly"
- **Our assessment**: For practitioners or researchers implementing RL for coding agents at
  scale, this is a specific, citable engineering decision. The k₃→k₁ switch is presented as
  necessary for stability, not a minor hyperparameter choice. The implication: large-scale
  RL on long coding trajectories pushes distributions far enough apart that standard KL
  estimators fail; practitioners should use the lower-variance estimator from the start.

### Claim 9: NVFP4 quantization during RL forward passes requires IEEE-compliant floating-point arithmetic — training diverges after ~100 RL steps with fast approximations

- **Evidence**: Specific failure mode documented: "IEEE-compliant floating-point arithmetic
  (e.g., __fdiv_rn) is critical for NVFP4; training diverges after ~100 RL steps with fast
  approximations." The forward pass uses a novel NVFP4 variant (FP8E4M3 per-block scales
  with FP32 per-token scales); backward uses standard MXFP8.
- **Confidence**: settled (a specific observed failure mode with a specific step count and
  specific fix)
- **Quote**: "IEEE-compliant floating-point arithmetic...is critical; training diverges
  after ~100 RL steps with fast approximations"
- **Our assessment**: This is a high-value engineering finding for teams implementing custom
  low-precision RL training. The failure mode (divergence at ~100 steps) is specific enough
  to be a diagnostic: if your RL training degrades after the first 100 steps, check your
  FP approximations. The asymmetric approach (NVFP4 forward, MXFP8 backward) is novel and
  the motivation is explained (numerical precision and gradient bias issues in RL context).

### Claim 10: A custom length penalty formula discourages verbosity on simple tasks while permitting extended reasoning on complex ones

- **Evidence**: Explicit mathematical formula:
  `C_length{k,q}(x) = [(1+kx)^(1-q)-1]/[k(1-q)]`
  This nonlinear penalty is described as letting the model recognize task complexity and
  respond proportionally.
- **Confidence**: emerging (design rationale is given; downstream effect on behavior is
  not quantified beyond the formula)
- **Quote**: "Encourages efficient responses on simple tasks while permitting extended
  reasoning on complex problems"
- **Our assessment**: This is a practical reward shaping technique for practitioners building
  RL-trained agents. The nonlinear form is key: a linear length penalty would uniformly
  discourage long responses; the power-law shape allows long responses when the task warrants
  it. For practitioners using RLHF or RLAIF: length penalties are easy to apply but should
  be nonlinear to preserve capability on genuinely complex tasks.

### Claim 11: Behavioral auxiliary rewards shaped agent communication style, including dynamic introduction of penalties to suppress emergent excessive chain-of-thought in comments

- **Evidence**: "Auxiliary rewards shaped agent behavior including coding style and
  communication rewards, product-specific penalties for incomplete operations, and dynamic
  reward introduction monitoring emergent behaviors (e.g., preventing excessive
  chain-of-thought in comments)."
- **Confidence**: emerging (described as a design choice; the "dynamic introduction" detail
  suggests this was reactive to observed behavior, not pre-planned)
- **Quote**: "dynamic reward introduction monitoring emergent behaviors (e.g., preventing
  excessive chain-of-thought in comments)"
- **Our assessment**: The emergent excessive-CoT-in-comments behavior is notable: RL training
  apparently caused the model to start writing extended internal reasoning inside code comments
  — presumably because it improved task performance but degraded product quality. The response
  (add a new penalty reward when you observe an unwanted behavior) is a reusable RL discipline.
  For practitioners: behavioral rewards are not just "nice to have" — they are the mechanism
  for suppressing emergent RL behaviors that optimize for reward but degrade product experience.

### Claim 12: Delta compression reduces 1T-parameter model weight updates to "a handful of gigabytes" for distribution across a multi-region training cluster

- **Evidence**: "Sharded weight uploads using delta compression to S3. Diffs compress to
  a handful of gigabytes for the 1T-parameter model." Used in conjunction with fast weight
  synchronization enabling mid-rollout inference updates.
- **Confidence**: emerging (described with a specific size claim; mechanism is plausible for
  the parameter update sparsity typical in RL fine-tuning)
- **Quote**: "delta compression...diffs compress to a handful of gigabytes for the
  1T-parameter model"
- **Our assessment**: This is a non-obvious infrastructure finding. A 1T-parameter model in
  FP16 is ~2TB. "A handful of gigabytes" per update means ~0.1-0.3% of parameters are
  non-zero in each delta — a remarkable sparsity that enables practical multi-region RL
  training on a model this size. For teams building multi-region RL infrastructure: delta
  compression is the key to making weight synchronization tractable at this scale.

### Claim 13: Pretraining loss correlates with downstream RL performance — less pretraining loss predicts better RL fine-tuning outcomes

- **Evidence**: Ablation using Qwen3-Coder-30B-A3B at three logarithmically-spaced compute
  levels. Cross-entropy loss "correlates with downstream RL performance" and "decreases
  log-linearly over the course of the training run."
- **Confidence**: emerging (single model family ablation; three compute points; directional
  but not a strong causal claim)
- **Quote**: "Cross-entropy loss correlates with downstream RL performance"
- **Our assessment**: This finding has significant implications for the "when to stop
  pretraining and start RL" design question. If pretraining loss predicts RL performance,
  then under-training the base model before RL is a structural performance ceiling. For
  practitioners fine-tuning with RL: invest in the base model quality (or choose a stronger
  base) before expecting RL to solve the gap. The log-linear relationship also means
  returns on pretraining compute are diminishing but consistently positive.

### Claim 14: CursorBench-3 doubles the median task size from the initial version and adds multi-workspace environments, monorepos, and production log investigation tasks

- **Evidence**: Explicit version comparison: "CursorBench-3 doubles the median task size
  from the initial version." New task types named: multi-workspace environments, monorepos,
  production log investigation.
- **Confidence**: emerging (first-party version comparison; specific task types are listed)
- **Quote**: "CursorBench-3 doubles the median task size from the initial version, measured
  by lines of code and mean number of files"
- **Our assessment**: This extends `blog-cursor-cursorbench.md`'s description of CursorBench
  evolution. The new task types map to real senior-engineer work: production log investigation
  (diagnosing live system behavior), monorepos (multi-package dependency management), and
  multi-workspace environments (operating across separate but related codebases). These are
  the task types where AI coding tools have the highest potential leverage and where current
  public benchmarks are completely absent.

### Claim 15: Four failure modes of public benchmarks: domain mismatch, prompt over-specification, training data contamination, and narrow evaluation scope (correctness only)

- **Evidence**: Explicit taxonomy: (1) SWE-bench focuses on isolated bug-fixing; Terminal-Bench
  includes non-engineering puzzles. (2) Public benchmarks assume narrow solution sets; real
  requests admit "multiple valid architectural approaches." (3) "OpenAI suspended SWE-bench
  Verified reporting after finding frontier models generated gold patches from memory." (4)
  Practitioners weight code quality, readability, latency, cost, and interaction behavior
  alongside correctness.
- **Confidence**: settled for contamination (OpenAI's public behavior corroborates), emerging
  for the other three (Cursor's analytical claim; plausible and consistent with other evidence)
- **Quote**: "OpenAI suspended SWE-bench Verified reporting after finding frontier models
  generated gold patches from memory"
- **Our assessment**: This taxonomy is a tighter and more specific version of the benchmark
  failure argument in `blog-cursor-cursorbench.md`. The contamination claim is effectively
  settled; the narrow-scope claim is now backed by quantitative specifics (Claim 3: 181 vs.
  7-10 LOC). The prompt over-specification point is the inverse of Claim 3: public benchmarks
  are verbose (1,185-3,055 chars) precisely because they need to constrain solutions to make
  grading tractable — but that means they measure agents that perform well on constrained,
  fully-specified tasks, not on real underspecified ones.

### Claim 16: Asynchronous RL across 3 GPU regions and 4 CPU regions with centralized reconciler and warm-standby fault recovery enables stable training at this scale

- **Evidence**: Infrastructure description: "Centralized reconciler managing slot-based
  sample lifecycle. Passive and active health checks enabling warm standby recovery. Distributed
  training across 3 regions for GPU compute, 4 for CPU compute. Policy-aware checkpointing
  at rollout and group levels."
- **Confidence**: emerging (first-party description; the specific fault-tolerance mechanisms
  described are coherent with the claimed scale)
- **Quote**: "fully asynchronous RL pipeline spanning multiple regions"
- **Our assessment**: The multi-region architecture is the production-scale version of what
  most RL implementations don't need to solve. Key design insight: the "slot-based sample
  lifecycle" managed by a centralized reconciler is the mechanism that makes asynchronous
  multi-region RL tractable — it decouples training speed from the slowest worker. For teams
  building agent training infrastructure at scale: this is the reference architecture for
  fault-tolerant async RL.

## Concrete Artifacts

### Benchmark Comparison Table

```
# Composer 2 vs. frontier models (Cursor Research, March 2026)
# Source: arXiv:2603.24477

                  CursorBench-3   SWE-bench Multi   Terminal-Bench
Composer 2            61.3%            73.7%             61.7%
Composer 1.5          44.2%            65.9%             47.9%
Composer 1            38.0%             —                 —
Kimi K2.5 base        36.0%             —                 —
GPT-5.4               63.9%            76.8%             66.5%
Opus 4.6 High         58.2%            75.8%             58.0%

Net gain from specialization (Kimi K2.5 base → Composer 2):
  CursorBench: 36.0% → 61.3% = +25.3 pp
  Shows value of continued pretraining + RL on domain-specific tasks
```

### CursorBench-3 Design Characteristics

```
# CursorBench-3 vs. public benchmarks (quantitative)
# Source: Cursor Research technical report, March 2026

Metric                CursorBench-3    SWE-bench       Terminal-Bench
Median LOC changed        181           7-10 (est.)          n/a
Median description        390 chars     1,185-3,055 chars    n/a
  length
Task scope trend      2x from v1        stable               n/a
  (CursorBench-3 vs v1)

CursorBench task categories:
  - Real Cursor engineering team sessions (via Cursor Blame technique)
  - Multi-workspace environments
  - Monorepos
  - Production log investigation (e.g., diagnosing transpilation failures)
  - Pattern detection across hundreds of heterogeneous files

Task examples:
  - "Diagnose esbuild 0.20.2 downleveling bugs from transpilation failures"
  - "Detect subtle streaming prefix regression across 954 heterogeneous
     response files through heuristic algorithm design"
```

### Training Architecture Summary

```
# Composer 2 training pipeline (Cursor Research, March 2026)

BASE MODEL
  Name: Kimi K2.5
  Scale: 1.04T parameters, 32B active (mixture-of-experts)
  Selection criteria: FreshBench, state tracking, codebase perplexity
  Alternatives evaluated: DeepSeek V3.2, GLM-5

CONTINUED PRETRAINING
  Phase 1: Extended training at 32k token sequences (MXFP8, AdamW, B300 GPUs)
  Phase 2: Long-context extension to 256k sequences
  Phase 3: SFT on targeted coding tasks
  Extras: Multi-token prediction via self-distillation (supports speculative decoding)

RL TRAINING
  Algorithm: Multiple-sample policy gradients, fixed group size, single-epoch
  KL estimator: k₁ = -log r (not k₃ — variance issues at large divergence)
  Length penalty: C_length{k,q}(x) = [(1+kx)^(1-q)-1]/[k(1-q)]
  Self-summarization: In-loop (trained via RL, not prompted)
  Behavioral rewards: Coding style, communication, product-specific penalties
  Dynamic penalties: Added reactively for emergent behaviors (e.g., excessive CoT in comments)

INFRASTRUCTURE
  Anyrun: 500+ pods/second, Firecracker VMs (GUI-capable), fork/snapshot
  Compute: 3 regions GPU, 4 regions CPU; async RL via Ray + PyTorch
  Quantization (forward): NVFP4 (FP8E4M3 per-block + FP32 per-token scales)
  Quantization (backward): MXFP8
  Weight sync: Delta compression (~handful of GBs for 1T-param model)
  Inference partner: Fireworks AI
  Critical finding: IEEE-compliant FP arithmetic required for NVFP4 (diverges at ~100 RL steps otherwise)
```

### Length Penalty Formula

```
# Nonlinear length penalty (Cursor Research, March 2026)
# Purpose: allow long responses on complex tasks, penalize verbosity on simple ones

C_length{k,q}(x) = [(1+kx)^(1-q)-1] / [k(1-q)]

  k: scaling constant (controls penalty steepness)
  q: power parameter (q > 1 → sublinear penalty growth = allows longer complex responses)
  x: response length in tokens
```

## Cross-References

- **Corroborates**: `blog-cursor-cursorbench.md` (#160) — This technical report provides
  the quantitative backbone for the CursorBench design claims in that note. The 181 vs. 7-10
  LOC comparison and 390 vs. 1,185-3,055 char descriptions quantify what that note describes
  qualitatively. The four-part public benchmark failure taxonomy here (domain mismatch,
  over-specification, contamination, narrow scope) extends the three-part taxonomy in that
  note (misalignment, grading problems, contamination) — adding "narrow evaluation scope"
  as a distinct failure mode. The contamination finding (OpenAI suspended SWE-bench Verified
  reporting) is cited identically in both sources.

- **Corroborates**: `blog-cursor-composer-self-summarization.md` (#162) — Both sources
  describe self-summarization as trained via RL for Composer. The self-summarization post
  (March 17) is a standalone research result; this technical report (March 27) includes
  self-summarization as one component of the overall training recipe. Consistent: both
  treat in-loop trained summarization as superior to prompt-based compaction.

- **Corroborates**: `blog-anthropic-harness-long-running.md` (#173) — The environment
  fidelity principle here ("train in production-identical harness") directly corroborates
  that post's finding that harness fidelity drives agent capability. Both posts converge
  on: the gap between training/eval environment and deployment environment is a primary
  performance ceiling. The Anyrun platform is Cursor's production-scale implementation of
  the same principle Anthropic labs documents at smaller scale.

- **Extends**: `blog-cursor-cursorbench.md` (#160) — This source adds the specific
  quantitative CursorBench characteristics (Claim 3), the full frontier comparison table
  (Claim 4), the best-of-K RL finding (Claim 5), and the Anyrun infrastructure (Claim 6)
  that the CursorBench post does not cover. The CursorBench post covers eval methodology;
  this covers training methodology, model selection, and infrastructure.

- **Extends**: `blog-cursor-composer-self-summarization.md` (#162) — This report places
  self-summarization within the broader training recipe and provides the behavioral rewards
  context (Claim 11) that explains how product-quality behaviors are instilled alongside
  task performance. The earlier post covers self-summarization in depth; this covers
  everything else around it.

- **Extends**: `blog-french-owen-coding-agents-feb-2026.md` — French-Owen's best-of-K
  discussion is anecdotal. Claim 5 here provides the first empirical support in the corpus
  for the proposition that RL-trained models genuinely improve under sampling (best-of-K
  improves alongside average), not just concentrate on known paths. This means multi-attempt
  strategies have compounding returns with RL-trained models.

- **Contradicts**: None identified. The CursorBench numbers here (61.3% for Composer 2)
  are consistent with the CursorBench post's framing that the benchmark continues to
  stratify models. The self-summarization findings are consistent.

- **Novel**: Compared to existing corpus:
  - **Anyrun platform architecture** — 500+ pods/second, Firecracker VM fork/snapshot, Anygress
    traffic control: no other source covers agent-training sandbox infrastructure at this scale
  - **Base model selection methodology** — explicit evaluation of 3 frontier MoE models on
    domain-specific criteria before selecting Kimi K2.5: no other source describes this selection process
  - **RL-specific numerical stability findings** — k₁ over k₃ KL estimator, NVFP4 IEEE
    requirement, training divergence at ~100 steps: no other source in corpus covers RL
    training numerics at this specificity
  - **CursorBench quantitative characteristics** — 181 vs. 7-10 LOC, 390 vs. 1,185+ char
    descriptions: first time these specific numbers appear in the corpus
  - **Best-of-K RL improvement finding** — RL improves both average and best-of-K: first
    empirical backing in corpus for the "RL trains new solution paths" claim
  - **Delta compression at 1T-param scale** — handful of GBs for model updates: unique
    infrastructure finding

## Guide Impact

- **Chapter 02 (Harness Engineering — environment fidelity)**: Add a section on training
  and evaluation environment fidelity as a first-class design principle. Cite Claim 2: the
  gap between training environment and deployment environment is a primary performance ceiling
  for specialized agents. Anyrun (Claim 6) is the production-scale implementation reference.
  For practitioners: test your harness in a realistic environment (real tools, real repos,
  real prompts) not a synthetic cleanup.

- **Chapter 02 (Harness Engineering — base model selection)**: Cite Claim 1 as the model
  for domain-specific base model selection: evaluate on FreshBench-equivalent (recency),
  state tracking, and domain perplexity — not general leaderboard rank. The 25.3pp net gain
  from specialization (36.0% base → 61.3% Composer 2) quantifies the value of the selection +
  specialization pipeline.

- **Chapter 02 (Harness Engineering — RL for specialized agents)**: Add Claims 8, 10, 11
  as specific RL design decisions practitioners can adopt: k₁ KL estimator for stability
  at large divergence, nonlinear length penalty to preserve complex-task capability, and
  dynamic behavioral rewards to suppress emergent unwanted behaviors.

- **Chapter 03 (Safety and Verification — eval design)**: Claims 3 and 15 should anchor
  the benchmark selection guidance. The specific numbers (181 vs. 7-10 LOC; 390 vs. 1,185+
  chars) provide the clearest quantitative case for building internal evals from real sessions.
  Recommendation: cite the four-part failure taxonomy as the checklist before trusting any
  public benchmark number. Update contamination caveat to include "OpenAI suspended SWE-bench
  Verified reporting" as the settled evidence.

- **Chapter 03 (Safety and Verification — multi-attempt strategies)**: Claim 5 (RL improves
  both average and best-of-K) supports designing best-of-N agent pipelines when using RL-trained
  models. For practitioners using Composer 2 specifically: running multiple attempts and
  selecting the best result captures capability the single-pass average doesn't reveal.

- **Chapter 04 (Context Engineering — long-horizon training)**: Claim 7 (256k long-context
  pretraining) and the self-summarization integration (from this report and #162) together
  argue that long-context capability is increasingly trained in, not just a harness-side
  concern. Update the compaction guidance: model-trained context management is becoming the
  production direction; harness-side workarounds are temporary mitigations.

- **Chapter 05 (Team Adoption — model selection for cost/quality tradeoff)**: Claim 4
  provides the clearest Pareto-optimal model cost/performance data in the corpus. For teams
  evaluating model cost: a well-specialized domain model (Composer 2) approaches frontier
  general models (GPT-5.4, Opus 4.6) at substantially lower inference cost. This is direct
  evidence for the "specialized beats general for well-defined workloads" thesis.

## Extraction Notes

- Blog post is a summary of arXiv:2603.24477. The arXiv HTML version (accessed April 2026)
  provided substantially more detail than the blog post itself — ablation data, formula
  specifics, quantitative CursorBench characteristics, and infrastructure architecture.
  The arXiv version was the primary extraction source; the blog post provided framing.
- 54 named authors on the arXiv paper; this is a full research paper, not a blog post with
  a technical appendix. Authority weight is accordingly high for technical claims.
- The paper notes Composer 2 is "likely smaller than other proprietary models of comparable
  ability" — the team acknowledges headroom. This is a relevant calibration for the cost
  efficiency claims: Composer 2 achieves near-frontier quality despite likely being smaller
  than the models it competes with; more training compute would likely improve it further.
- The NVFP4 finding (Claim 9 — training diverges at ~100 RL steps with fast FP approximations)
  is one of the few unflattering details published. Its inclusion strengthens the credibility
  of the technical report overall; the team is reporting a real failure mode they hit and solved.
- No contradictions to file: no existing source note makes claims opposed by this source.
- The Anyrun platform is internal to Cursor and not available externally. Its architecture is
  instructive for teams building their own agent training infrastructure, but practitioners
  cannot adopt Anyrun directly.
- Future-looking statement: "considerable room for development both architecturally and
  algorithmically" — the team does not claim Composer 2 is a ceiling. Track arXiv updates
  to 2603.24477 for subsequent versions.
