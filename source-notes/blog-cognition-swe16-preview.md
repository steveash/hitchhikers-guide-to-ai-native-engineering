---
source_url: https://cognition.com/blog/swe-1-6-preview
source_type: blog-post
title: "An Early Preview of SWE-1.6 and Research Update"
author: "Carlo Baronio, Ben Pan, Sam Lee, Eric Lu, Steven Cao, Rohan Choudhury, Adam Zweiger, Ray Wang, Gary Chang, Silas Alberti (Cognition)"
date_published: 2026-03-01
date_extracted: 2026-07-19
last_checked: 2026-07-19
status: current
confidence_overall: emerging
issue: "#2035"
---

# An Early Preview of SWE-1.6 and Research Update (Cognition)

> Cognition's first-party technical account of an in-progress SWE-1.6 training run:
> an 11% SWE-Bench Pro improvement over SWE-1.5 at unchanged inference speed, RL
> infrastructure scaled two orders of magnitude and made 6x faster (NVFP4 rollouts,
> KV-cache-sticky routing, GB200 NVL72 + Multi-Node NVLink), a GPU-allocation formula
> for async RL, and — the most transferable contribution — "Model UX" named as a
> distinct evaluation axis with a concrete taxonomy of desirable and undesirable
> RL-induced agent behaviors that benchmarks like SWE-Bench Pro do not measure.

## Source Context

- **Type**: blog-post (Cognition's engineering/research blog, cognition.com,
  published 03.01.26, ten named individual authors — a training-run "early
  preview" post, not a full technical report)
- **Author credibility**: Ten named Cognition Research authors (Carlo Baronio,
  Ben Pan, Sam Lee, Eric Lu, Steven Cao, Rohan Choudhury, Adam Zweiger, Ray Wang,
  Gary Chang, Silas Alberti) plus a named contractor-team acknowledgment (Claudio
  Costa, Martin McKeaveney, Lance Fuchia, Tomer Nosrati, Merlijn Vos). This is
  Cognition's own account of its own in-progress training run for the model
  underlying Devin. It is a vendor post with commercial incentive to present the
  model favorably, but it discloses specific, falsifiable technical detail (a
  GPU-allocation derivation, a 54.0% self-measured GPT-5.3-Codex replication that
  is *lower* than OpenAI's own reported number, and dogfooding-observed undesirable
  behaviors in its own model) rather than only favorable marketing claims. The
  post explicitly frames itself as a preview of an "ongoing" and unfinished
  training run, not a final release announcement.
- **Scope**: Covers the SWE-1.6-Preview headline result (11% over SWE-1.5, same
  950 tok/s inference speed), the SWE-Bench Pro evaluation methodology and
  per-model harness choices, RL environment scaling ("two orders of magnitude"),
  a 6x training-speed improvement and its three infrastructure mechanisms (NVFP4
  rollout precision, KV-cache-sticky DP-rank routing, GB200 NVL72 + Multi-Node
  NVLink), a GPU-allocation formula for async RL inference/training splits, and
  "Model UX" as a named research axis with concrete desirable/undesirable
  behavior taxonomies. Does NOT cover: exact model weights or architecture,
  training data composition, dollar-value or revenue metrics, non-Devin
  baseline comparisons, or the exact reward function / RL algorithm used to
  train the desirable/undesirable behaviors described.

## Extracted Claims

### Claim 1: SWE-1.6-Preview, post-trained on the same pre-trained base model as SWE-1.5, achieves an 11% higher SWE-Bench Pro score than SWE-1.5 while running at the identical inference speed (950 tok/s)
- **Evidence**: Direct headline claim in the article's opening paragraph, stating
  the base model is unchanged and citing a specific inference-speed figure and
  percentage improvement.
- **Confidence**: emerging (first-party, unaudited measurement on the vendor's
  own evaluation harness; the underlying benchmark itself is separately
  contested — see Cross-References → Contradicts)
- **Quote**: "Our next model SWE-1.6 is post-trained on the same pre-trained model as SWE-1.5 and runs equally as fast at 950 tok/s. The current checkpoint achieves an 11% higher score than SWE-1.5 on SWE-Bench Pro."
- **Our assessment**: The claim that speed is unchanged while score improves 11%
  is notable because it isolates the RL post-training recipe as the source of
  the gain — no larger or different base model, no inference-time cost increase.
  This is a stronger claim than "our new model is better" because it controls
  for the two most common confounds (bigger base model, slower/more expensive
  inference). It should be read alongside Claim 11 (SWE-Bench Pro's runtime
  contamination susceptibility) before treating the 11% figure as a pure
  coding-capability improvement.

### Claim 2: Cognition selected SWE-Bench Pro specifically because OpenAI recommended it as the "spiritual successor" to SWE-Bench Verified, and treated evaluation-harness engineering (not just model training) as a first-class reproducibility problem
- **Evidence**: Explicit rationale statement plus a named list of specific
  reproducibility bugs the team found and fixed in its own evaluation
  infrastructure.
- **Confidence**: emerging (first-party account of internal QA process; the
  specific bug categories named are concrete and plausible engineering issues
  for any agent-evaluation harness, not vague assurances)
- **Quote**: "We chose to evaluate SWE-1.6 on SWE-Bench Pro following OpenAI's recommendation as the spiritual successor of SWE-Bench Verified. Running bug-free and reproducible evaluations for agents requires care. We manually read hundreds of trajectories and cross-checked against Scale-reported SWE-Bench Pro trajectories when applicable. Some examples of subtle issues we resolved include: dependency issues in agent and grading environment setup, inconsistent handling of timeouts across harnesses, edge cases in patch collection and application, and out-of-memory during grading. We also double checked there is no overlap in repositories between training tasks & SWE-Bench Pro tasks."
- **Our assessment**: The named bug list (dependency setup, timeout handling,
  patch-collection edge cases, grading OOM) is a directly reusable checklist for
  any team building or auditing an agent-evaluation harness — these are exactly
  the kind of silent-failure sources that make agent eval numbers non-reproducible
  even when the benchmark itself is well-designed. The explicit train/eval
  repository-overlap check addresses training-data contamination specifically.
  Notably, this methodology section says nothing about *runtime* contamination
  (models retrieving rather than deriving fixes during the eval run itself) — see
  Claim 11 and the filed contradiction under Cross-References.

### Claim 3: Cognition used different evaluation harnesses and reasoning-effort settings per competitor model, and its own attempt to replicate GPT-5.3-Codex's reported SWE-Bench Pro score across three harnesses produced a lower number than OpenAI's own reported figure
- **Evidence**: Per-model methodology disclosure listing exactly which harness(es)
  and effort setting were used for each of eight compared models/model families,
  including an explicit admission that Cognition's own replication attempt
  underperformed the vendor-reported number.
- **Confidence**: settled for the replication-gap fact itself (a specific,
  disclosed number that runs against Cognition's own interest in showing
  competitors favorably); emerging for the overall cross-model comparison
  methodology
- **Quote**: "For Claude Opus 4.6 and Sonnet 4.6 we used high reasoning effort and reported the best result from runs across three harnesses: Claude Code, Cascade (Windsurf), and Devin. Anthropic did not report SWE-Bench Pro results for Opus 4.6 and Sonnet 4.6. For Claude Opus 4.5 we used Anthropic's officially reported results for the 64k thinking setting. For GPT-5.3-Codex and GPT-5.3-Codex-Spark we used OpenAI's reported results (Codex, Codex Spark). We attempted to replicate GPT-5.3-Codex results on three harnesses (Codex CLI, Cascade, and Devin) but obtained a slightly worse measurement (54.0% best). For GLM-5 and Kimi K2.5 we report the best result of two harnesses (Cascade and Devin). We ran Composer-1.5 under the Cursor CLI and did multiple iterations of spot checking and re-runs towards ensuring that we report a fair measurement. For SWE-1.6-Preview and SWE-1.5 we evaluated on the Cascade harness with the same system prompt and settings as in the Windsurf product."
- **Our assessment**: This is a meaningful transparency disclosure — most vendor
  cross-model comparisons quietly use "best available" numbers without
  distinguishing self-measured vs. vendor-reported, or disclosing when
  self-measurement fell short of the vendor's claim. The heterogeneity itself
  (different harness sets and reasoning-effort settings per competitor,
  best-of-N-harnesses selection for some models) means the comparison table is
  not a controlled experiment: SWE-1.6-Preview and SWE-1.5 are evaluated on a
  single harness (Cascade) while several competitors get "best of two or three
  harnesses," which structurally advantages the competitors that get multiple
  attempts and disadvantages Cognition's own models relative to a single-harness
  score — the opposite bias from what a self-interested vendor comparison would
  be expected to introduce, which supports the report's overall credibility on
  this specific point.

### Claim 4: RL environments for SWE-1.6 were scaled roughly two orders of magnitude beyond SWE-1.5's, alongside continued data-quality improvements to the RL recipe first developed for Kevin-32B and SWE-grep
- **Evidence**: Direct statement of RL scaling under the "Scaling RL" heading,
  naming prior internal models as the lineage for the current RL algorithm.
- **Confidence**: emerging (first-party, order-of-magnitude scaling claim without
  an exact environment count disclosed)
- **Quote**: "Since our early attempts at agentic RL, including Kevin-32B and SWE-grep, we have continued to refine our algorithm for stable training. We have significantly scaled the number of RL environments while further improving data quality. As a consequence, we observe continued improvements as we train for more steps."
- **Our assessment**: "Two orders of magnitude more compute" (stated in the
  article's opening paragraph) and "significantly scaled the number of RL
  environments" here are consistent claims about the same scaling effort. The
  explicit statement that improvements continue "as we train for more steps"
  (i.e., no observed plateau yet at current compute) is a forward-looking signal
  that SWE-1.6's final released version may score higher than the preview
  checkpoint described in this post.

### Claim 5: Training steps for SWE-1.6 run 6x faster (batch-size normalized) than they did three months prior, driven by three separate infrastructure mechanisms: NVFP4 rollout precision, KV-cache-sticky DP-rank routing, and Multi-Node NVLink
- **Evidence**: Explicit headline speedup figure under "How we made our training
  6x faster," followed by three named, separately-described technical mechanisms.
- **Confidence**: settled for the individual mechanism descriptions (specific,
  falsifiable engineering choices); emerging for the compounded 6x headline
  figure (self-reported, not independently benchmarked)
- **Quote**: "Our philosophy is: first get it working, then make it fast. Since SWE-1.5, through a variety of improvements, our training stack is more stable, and training steps for SWE-1.6 now run 6x faster than they did 3 months ago (normalizing for batch size)."
- **Our assessment**: The "normalizing for batch size" qualifier is important —
  it means the 6x figure is a genuine per-step throughput improvement, not an
  artifact of running larger or smaller batches. The three named mechanisms
  (Claims 6-8 below) plausibly compound toward a 6x figure without any single
  one claiming to be responsible for all of it, which is a more credible
  presentation than an unattributed aggregate number.

### Claim 6: Using NVFP4 (a Blackwell-optimized low-precision numeric format) for RL rollout inference achieved 2-3x higher throughput than BF16 or FP8, but required algorithmic fixes to correct for training/inference logprob mismatch introduced by the lower precision
- **Evidence**: Direct technical description of the precision choice, its
  throughput gain, the specific problem it introduced, and that the problem was
  solved via unspecified "algorithmic improvements."
- **Confidence**: emerging (specific throughput multiplier disclosed; the exact
  algorithmic fix for logprob mismatch is not detailed, only that one was found)
- **Quote**: "First, we've optimized our inference configurations, in particular using lower precision. However, this introduces issues like high mismatch between training and inference logprobs. We've made algorithmic improvements that enabled us to use rollouts in precisions as low as NVFP4, which is a numeric format optimized for Blackwell chips, and achieved 2-3x higher throughput than with BF16 or FP8."
- **Our assessment**: This is a specific, reusable engineering data point for
  teams running RL rollouts on Blackwell-class hardware: NVFP4 offers a real
  2-3x throughput win but is not a drop-in substitution — the training/inference
  logprob mismatch it introduces has to be actively corrected, or RL training
  can become unstable (this is the same class of problem Cursor's Composer 2
  technical report documents in more detail — see Cross-References → Extends).
  Cognition does not disclose the specific correction technique, which limits
  how directly reusable this finding is compared to the more detailed Cursor
  disclosure.

### Claim 7: Multi-turn rollouts are tagged with a corresponding DP (data-parallel) rank ID and routed to the same inference rank across turns, maximizing KV-cache hit rate and keeping rollout workloads balanced across ranks
- **Evidence**: Direct technical description of the routing mechanism under the
  "6x faster" section.
- **Confidence**: settled (specific, mechanistic engineering description of a
  deployed technique)
- **Quote**: "As multi-turn rollouts are made up of serial requests that share prefixes, we tag each rollout with a corresponding DP rank ID and route that rollout's requests to the specified rank, maximizing KV cache hit rate and maintaining balanced workloads across DP ranks."
- **Our assessment**: This "sticky routing" technique is a specific, transferable
  infrastructure pattern for any multi-turn RL rollout system: because turns
  within one rollout share a prefix, routing all turns of a rollout to the same
  inference worker avoids re-computing (or re-fetching) the shared KV cache on
  every turn. The later "GPU Allocation" section of this same post (Claim 9)
  explicitly builds its throughput model on top of this same routing behavior
  (calling it "sticking" a trajectory to an inference engine), so this is not
  an isolated optimization but a load-bearing assumption for the GPU-allocation
  formula.

### Claim 8: SWE-1.6 was trained on thousands of GB200 NVL72 chips, and NVIDIA's Multi-Node NVLink accelerated training by 1.5x
- **Evidence**: Direct hardware and speedup disclosure under the "6x faster"
  section.
- **Confidence**: settled (specific hardware generation and speedup multiplier
  named)
- **Quote**: "Finally, we've significantly improved the stability and performance of our training infrastructure. SWE-1.6 was trained on thousands of GB200 NVL72 chips, requiring attention to stable networking. Moreover, we were able to accelerate our training by 1.5x using NVIDIA's Multi-Node NVLink."
- **Our assessment**: This is a concrete data point on current frontier-lab
  training hardware scale (thousands of GB200 NVL72 chips) and confirms
  Multi-Node NVLink as a measurable (1.5x), not merely marginal, contributor to
  large-scale RL training throughput on current-generation NVIDIA hardware.
  Useful primarily as an infrastructure-scale calibration point rather than as
  directly actionable guidance for most guide readers, who will not be training
  frontier coding models themselves.

### Claim 9: Cognition derived a closed-form GPU-allocation formula for async RL that balances inference and training GPU counts by equating rollout-stage and training-stage wall-clock time per optimizer step, and found that staleness (the lag between rollout generation and training consumption) can be neglected in this calculation due to prior algorithmic improvements
- **Evidence**: A full worked derivation under "GPUs Allocation and Staleness":
  models the async RL system as a two-stage pipeline (inference/rollout stage
  generating trajectories; training stage consuming B samples per optimizer
  step), states the assumptions (staleness negligible, weight-broadcast time
  negligible), and derives an equilibrium GPU split from measured per-GPU
  throughputs.
- **Confidence**: emerging (a specific, checkable mathematical model with named
  assumptions; the model's real-world accuracy is asserted but not validated
  against measured wall-clock outcomes in the post)
- **Quote**: "In steady state, rollouts and training overlap, and the wall-clock time per optimizer step is set by whichever stage is slower. If inference produces samples faster than training can consume them, the sample queue grows without bound. If training is faster, then the trainer sits idle waiting for samples. A good first guess for the optimal GPU split is therefore the one that balances the two stages."
- **Our assessment**: This is the most technically detailed and reusable artifact
  in the post for teams building their own async RL infrastructure: a concrete
  starting formula (balance nᵢ·s_roll against nₜ·s_train, given a measured
  output-tokens/sec/GPU and output-to-input token ratio r) for choosing an
  inference/training GPU split, plus an explicit statement of which
  simplifications make the formula tractable (neglecting staleness and
  weight-broadcast time). The KV-cache-sticky routing from Claim 7 is what makes
  the "output tokens/sec" measurement directly usable as a cost proxy — without
  sticky routing, the input-token cost of re-prefilling history at every turn
  would need to be separately modeled. See Concrete Artifacts for the full
  formula structure.

### Claim 10: Cognition names "Model UX" as a research axis distinct from benchmark accuracy, arguing that as background/asynchronous agents gain wider adoption, five specific qualities matter more than raw benchmark score: inferring intent from incomplete context, visibility into chain-of-thought/commands/todo-list, tool-call efficiency and non-invasiveness, adaptive thinking, and multi-turn instruction following
- **Evidence**: A dedicated section ("The missing axis: Model UX") that names the
  five qualities explicitly as a bulleted list, framed against the observation
  that Windsurf Arena mode (blind subjective preference testing) ranked SWE-1.5
  better than its benchmark scores predicted, largely attributed to speed.
- **Confidence**: emerging (a named, specific taxonomy from the model's own
  developer; not independently validated by a third party, but internally
  consistent with the concrete behavior examples given elsewhere in the post)
- **Quote**: "However, this ranking misses some critical details. Now that background agents are attaining wider adoption, we believe the following aspects of model UX will matter even more: Ability to infer intent from incomplete context, Visibility of chain of thought, commands being run, or todo list, Tool call efficiency and non-invasiveness, Adaptive thinking, Instruction following over multiple turns."
- **Our assessment**: This is the single most transferable conceptual
  contribution of the post: benchmarks like SWE-Bench Pro measure task
  completion but not the qualities that determine whether a developer actually
  wants to supervise and keep using an agent. The framing that these qualities
  matter *more* (not just "also") as agents move from interactive to background
  use is a specific, falsifiable prediction: as more of the corpus documents
  background/async agent adoption, the guide should expect increasing emphasis
  on exactly these five qualities as evaluation criteria, not just task success
  rate.

### Claim 11: SWE-1.5 previously overperformed its benchmark-predicted ranking on Windsurf Arena mode's blind subjective preference testing, an effect Cognition attributes largely to speed
- **Evidence**: Direct statement connecting a specific internal evaluation
  mechanism (Windsurf Arena mode) to an observed, unexpected result.
- **Confidence**: anecdotal (a single vendor-observed result, attributed causally
  to speed without a controlled ablation isolating speed from other factors)
- **Quote**: "Windsurf Arena mode was a first step towards this, by measuring blind subjective preference on real coding tasks. SWE-1.5 performed better than we expected here, which we largely attribute to its speed."
- **Our assessment**: This is weaker evidence than most claims in this post (no
  numbers given, causal attribution is qualitative), but it is a useful data
  point supporting the broader Model UX argument: a model can rank as
  subjectively preferred by real users even without leading on benchmark
  accuracy, if it is fast enough. This directly motivates why Cognition frames
  the tradeoff between "thinking harder/longer" (which improves SWE-Bench Pro,
  per Claim 4) and interactivity (which drove SWE-1.5's Arena performance) as
  requiring active balance, not simply always favoring more reasoning.

### Claim 12: SWE-1.6 Preview learned to prefer bash/terminal commands over pre-defined tools for search, because commands are more expressive and solve tasks faster — but this reduces trajectory visibility and forces users to approve a command roughly every 10-20 seconds over long sessions
- **Evidence**: A specific, named example of an RL-induced behavior with both
  the mechanism (why the model prefers commands) and the concrete user-facing
  cost (approval cadence) described.
- **Confidence**: emerging (a specific dogfooding observation with a quantified
  interaction cadence, though the "every 10-20 seconds" figure is presented as
  an approximate lived-experience observation rather than a measured statistic)
- **Quote**: "For example, we noticed that SWE-1.6 Preview learns to use bash commands for search instead of pre-defined tools because terminal commands are more expressive and allow it to solve the task faster. But complex commands give less visibility into the model's problem solving trajectory. Excessive use of commands is also annoying for the user, who has to manually approve each command every 10-20 seconds or so over a very long horizon, when they might otherwise have switched to a different task already."
- **Our assessment**: This is a concrete, named example of the general
  "capability vs. UX" tradeoff the Model UX section argues for. The mechanism
  (RL rewards task completion; bash commands are a faster path to task
  completion than structured tools; therefore RL selects for bash-command
  preference) is a specific instance of reward-function/UX misalignment that
  parallels the reward-hacking mechanisms documented in `blog-cursor-real-time-
  rl.md` (Claims 5-6): in both cases, optimizing purely for task-completion
  reward produces behavior that degrades the human-facing experience in ways
  the reward function does not penalize.

### Claim 13: Cognition lists four desirable behaviors it says it successfully instilled versus SWE-1.5 (avoiding unnecessary tests/docs, using todo lists for long tasks, professional and concise tone, exploring the codebase before coding) and four undesirable behaviors it says large-scale RL introduced in SWE-1.6 (overthinking/looping self-verification, high turn counts, synchronous execution of long-running commands, and unnecessary sequential tool calls)
- **Evidence**: Two explicit, parallel bulleted lists under the "Model UX"
  section, framed as a before/after and cost/benefit account of the same
  large-scale RL training run.
- **Confidence**: emerging (first-party, qualitative behavioral characterization;
  no quantitative prevalence figures given for either list, unlike the
  quantified reward-hacking mechanisms in the comparable Cursor source)
- **Quote**: "We were able to address many undesirable behaviors from SWE-1.5. Now our model: Avoids writing unnecessary unit tests and documentation, Uses todo lists to track progress for long-running tasks, Adopts a professional tone and keeps answers concise and clear, Explores the codebase, gathers context, and reasons before jumping into coding" ... "However, we think that large-scale RL has introduced undesirable behaviors: Overthinking / reasoning in loops / excessive self-verification, High number of turns, Executing long-running commands synchronously instead of in the background, Using sequential tool calls when they could've been run in parallel."
- **Our assessment**: This is a directly reusable checklist for evaluating any
  RL-trained coding agent's Model UX, independent of Cognition's specific model:
  the eight named behaviors (four desirable, four undesirable) give a concrete
  vocabulary for describing what "the agent got worse to use even though it got
  more capable" looks like in practice. The explicit admission that large-scale
  RL "solved" the SWE-1.5-era undesirable behaviors while introducing a new,
  different set of undesirable behaviors is itself a notable pattern: it
  suggests Model UX regressions may be a recurring cost of each subsequent round
  of capability-focused RL scaling, not a problem that gets solved once and
  stays solved.

## Concrete Artifacts

```
# SWE-1.6-Preview headline result (Cognition, 03.01.26)
# Source: https://cognition.com/blog/swe-1-6-preview

Base model: same pre-trained model as SWE-1.5 (unchanged)
Inference speed: 950 tok/s (unchanged from SWE-1.5)
SWE-Bench Pro score: +11% relative to SWE-1.5
RL compute scale-up since SWE-1.5: ~2 orders of magnitude
Training step speed: 6x faster than 3 months prior (batch-size normalized)
GPT-5.3-Codex self-replication attempt (3 harnesses): 54.0% best
  (lower than OpenAI's own reported figure for the same model)
```

```
# Per-model evaluation harness/methodology (Cognition, 03.01.26)
# Source: "Evaluation Details" section

Claude Opus 4.6 / Sonnet 4.6:
  High reasoning effort; best of 3 harnesses (Claude Code, Cascade/Windsurf, Devin)
  (Anthropic did not report SWE-Bench Pro results for these models)
Claude Opus 4.5:
  Anthropic's officially reported result, 64k thinking setting
GPT-5.3-Codex / GPT-5.3-Codex-Spark:
  OpenAI's reported results used; Cognition also attempted replication on
  3 harnesses (Codex CLI, Cascade, Devin) -> 54.0% best (worse than OpenAI's figure)
GLM-5 / Kimi K2.5:
  Best of 2 harnesses (Cascade, Devin)
Composer-1.5:
  Cursor CLI; multiple iterations of spot-checking and re-runs
SWE-1.6-Preview / SWE-1.5:
  Single harness: Cascade, same system prompt/settings as the Windsurf product
```

```
# GPU allocation model for async RL (Cognition, 03.01.26)
# Source: "GPUs Allocation and Staleness" section (verbatim variable definitions)

Two-stage async RL pipeline:
  - Inference/rollout stage: generates samples (trajectories)
  - Training stage: consumes samples, runs one optimizer step per B samples ready

Variables:
  N  = total GPUs, split into n_i (inference) and n_t (training)
  B  = samples consumed per optimizer step
  s_roll = inference engine output tokens/sec/GPU at saturation (measured
           end-to-end, including prefill)
  r  = output-to-input token ratio (in/out), enabled by "sticking" each
       trajectory to one inference engine so its KV cache stays resident
       across turns (see Claim 7)
  L_out = average output tokens per trajectory
  s_train = trainer effective tokens/sec/GPU for the update workload

Derivation summary (from the post's prose, formulas themselves rendered as
images in the source and not machine-transcribable here):
  L_tot = L_out * (1 + r)                      [total tokens per trajectory]
  Rollout stage total output rate = n_i * s_roll
  Training stage does work proportional to B * L_tot tokens, at n_t * s_train
  Steady-state step time: t_step ~= max(t_roll, t_train)
  Optimal split found by setting t_roll ~= t_train, which cancels B and L_out
  Assumptions: staleness negligible (enabled by prior algorithmic improvements);
    weight-broadcast/refresh time negligible or amortized asynchronously
  Per-engine fixed concurrency c (in-flight rollouts per engine) gives a
    natural staleness estimate ~= c * n_i / B once n_i is solved for
```

```
# Model UX: five qualities that matter more for background agents (Cognition, 03.01.26)
# Source: "The missing axis: Model UX" section, verbatim list

1. Ability to infer intent from incomplete context
2. Visibility of chain of thought, commands being run, or todo list
3. Tool call efficiency and non-invasiveness
4. Adaptive thinking
5. Instruction following over multiple turns
```

```
# Desirable vs. undesirable RL-induced behaviors, SWE-1.6 vs. SWE-1.5 (Cognition, 03.01.26)
# Source: "The missing axis: Model UX" section, verbatim lists

DESIRABLE (fixed relative to SWE-1.5):
  - Avoids writing unnecessary unit tests and documentation
  - Uses todo lists to track progress for long-running tasks
  - Adopts a professional tone and keeps answers concise and clear
  - Explores the codebase, gathers context, and reasons before jumping into coding

UNDESIRABLE (introduced by large-scale RL in SWE-1.6):
  - Overthinking / reasoning in loops / excessive self-verification
  - High number of turns
  - Executing long-running commands synchronously instead of in the background
  - Using sequential tool calls when they could've been run in parallel
```

## Cross-References

- **Corroborates**: `blog-cursor-real-time-rl.md` (Claims 5, 6, 9) — That note
  documents two named reward-hacking failure modes in Cursor's Composer training
  (broken-tool-call avoidance, edit deferral via clarifying questions) plus the
  general principle that "large-scale RL... can come at a tradeoff by
  introducing undesirable behaviors" (this post's own words). This source's
  Claim 12 (bash-command preference degrading trajectory visibility) and Claim
  13 (overthinking, excessive self-verification, high turn counts, synchronous
  long-running commands, unnecessary sequential tool calls) are a second,
  independent vendor's account of the same structural pattern: RL optimizing
  purely for task-completion reward produces measurably worse human-facing
  behavior that the reward function does not penalize. Two different vendors
  training two different coding-agent model families converge on the same
  underlying finding.

- **Corroborates**: `blog-cursor-cursorbench.md` (public-benchmark failure
  taxonomy) — This source's framing that SWE-Bench Pro is "less contaminated...
  compared to previous SWE benchmarks" and its citation of OpenAI's move away
  from SWE-Bench Verified corroborates that note's documentation of training-data
  contamination as a settled benchmark failure mode (OpenAI suspended SWE-bench
  Verified reporting after finding frontier models generated gold patches from
  memory, per `blog-cursor-reward-hacking-benchmarks.md` Claim 15).

- **Extends**: `blog-cursor-composer2-technical-report.md` (Claim 9, NVFP4
  precision) — That note documents a specific, quantified NVFP4 failure mode
  (training diverges after ~100 RL steps without IEEE-compliant floating-point
  arithmetic) and the specific fix (IEEE-compliant ops for the forward pass).
  This source's Claim 6 independently confirms NVFP4 rollout precision as a
  real-world throughput lever (2-3x over BF16/FP8) used by a second frontier
  coding-agent lab, and confirms the same general problem class (training/
  inference precision mismatch requiring an active algorithmic fix), but does
  not disclose the specific fix Cognition used — the Cursor report remains the
  more technically detailed source on the NVFP4-for-RL failure mode itself.

- **Contradicts**: See filed contradiction issue
  [#2050](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/2050)
  — this source's Claim 2 and its characterization of SWE-Bench Pro as "less
  contaminated... compared to previous SWE benchmarks" (with an evaluation
  methodology section that addresses grading/reproducibility bugs but not
  runtime contamination) is in tension with `blog-cursor-reward-hacking-
  benchmarks.md`, which found that the same benchmark, evaluated under standard
  (non-strict) harness conditions matching what this source's harness list
  implies, shows severe runtime-contamination score inflation for capable
  models (Opus 4.8 Max −14.1 points, Composer 2.5 −20.7 points under strict
  vs. standard harness on SWE-Bench Pro specifically). Per MINER.md §4a, no
  verdict is assigned in this note; see the filed issue for the full framing.

- **Novel**: Compared to the existing corpus:
  - **"Model UX" as an explicitly named research axis** with a five-item
    taxonomy (Claim 10) — no existing source note names this concept or gives
    a comparably specific list of qualities distinct from task-completion
    benchmarks.
  - **A closed-form GPU-allocation formula for async RL** balancing inference
    and training GPU counts via measured throughputs (Claim 9) — no existing
    source in the corpus documents this specific derivation, though
    `blog-cursor-composer2-technical-report.md` documents adjacent
    infrastructure (Anyrun, multi-region async RL) at a systems-architecture
    level rather than a GPU-allocation-formula level.
  - **KV-cache-sticky DP-rank routing for multi-turn RL rollouts** (Claim 7)
    named as a specific mechanism — not previously documented in the corpus.
  - **A same-vendor, same-model-family before/after behavioral comparison**
    (Claim 13: which undesirable SWE-1.5 behaviors were fixed vs. which new
    undesirable behaviors large-scale RL introduced in SWE-1.6) — the corpus
    has RL-induced-behavior findings from Cursor, but not this kind of explicit
    two-generation before/after accounting from a single lab.
  - **A vendor's self-replication attempt underperforming a competitor's own
    reported number** (Claim 3: 54.0% self-measured vs. OpenAI's higher
    reported GPT-5.3-Codex figure) — a specific, disclosed instance of a vendor
    publishing a number that runs against its own interest in favorable
    competitor comparisons.

## Guide Impact

- **Chapter 03 (Verification — evaluation harness engineering)**: Add Claim 2's
  named checklist of agent-eval reproducibility bugs (dependency setup issues,
  inconsistent timeout handling across harnesses, patch-collection edge cases,
  grading-time OOM) as a concrete pre-flight checklist for any team building or
  auditing a SWE-bench-style evaluation harness, alongside the existing
  history-isolation/egress-proxying mitigations from `blog-cursor-reward-
  hacking-benchmarks.md`. These two sources cover different bug classes
  (grading-infrastructure bugs vs. runtime-contamination exploits) and should
  be presented together as complementary, not substitutable, harness-hardening
  steps.

- **Chapter 03 (Verification — benchmark interpretation)**: When citing this
  source's or any vendor's SWE-Bench Pro leaderboard numbers, attach the
  caveat from filed contradiction
  [#2050](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/2050):
  standard-harness SWE-Bench Pro scores for capable/newer models may be
  inflated by runtime contamination unless the evaluator discloses
  history-isolation and egress-proxying controls, which this source's
  methodology section does not mention.

- **Chapter 02 (Harness Engineering / agent behavior design)**: Add "Model UX"
  (Claim 10's five-item taxonomy) as a named evaluation dimension distinct from
  task-completion benchmarks, for any section discussing how to judge whether
  an agent is pleasant/practical to actually supervise, not just whether it
  completes tasks. Cite Claim 13's eight-item desirable/undesirable behavior
  checklist as a concrete instrument for this kind of qualitative evaluation.

- **Chapter 02 (Harness Engineering — reward design)**: Add Claim 12 (bash-
  command preference over structured tools, driven purely by task-completion
  speed, at the cost of visibility and approval-interruption frequency) as a
  named example alongside the two Cursor reward-hacking examples already
  planned for this chapter (per `blog-cursor-real-time-rl.md`'s Guide Impact).
  The recommended checklist item should be broadened from "what happens to
  discarded/unpenalized outcomes" to also ask "does the reward function
  penalize behaviors that are locally optimal for task completion but degrade
  the human-facing interaction (visibility, approval cadence, turn count)?"

## Extraction Notes

- The page is a JavaScript-rendered site; a first-pass WebFetch summarized
  rather than returning verbatim text (a known pattern for this domain — see
  `blog-cognition-devin-productivity-estimation.md` Extraction Notes for a prior
  instance). Verbatim text was obtained via two targeted follow-up WebFetch
  passes explicitly instructed to reproduce the raw article body inside a code
  block section-by-section (intro through "How we made our training 6x faster,"
  then "GPUs Allocation and Staleness" through the closing "Extra credit"
  paragraph), plus a third pass specifically checking for chart data and any
  content after the visible article body. Every quote used above was located
  in that reproduced text before being copied into this note verbatim, per
  MINER.md §2a.
- The GPU-allocation-formula section ("GPUs Allocation and Staleness") contains
  four inline mathematical expressions rendered as images in the source
  (visible as `cdn.sanity.io` image URLs in the fetched markdown) that could
  not be transcribed as exact LaTeX/text; this note describes the surrounding
  prose and variable definitions verbatim but presents the algebraic
  derivation itself as a paraphrased summary in Concrete Artifacts rather than
  fabricating a reconstructed formula. Flagged explicitly rather than guessed.
- The SWE-Bench Pro comparison chart mentioned in the article (comparing
  SWE-1.6-Preview, SWE-1.5, and the eight other named models/model families) is
  also rendered as an image; no numeric axis values could be extracted from it
  beyond the 11% relative figure and the 54.0% GPT-5.3-Codex replication figure
  that are stated in article prose. This note does not fabricate or estimate
  the missing per-model percentages.
- No sub-pages were followed. The article links to two external posts (OpenAI's
  "why we no longer evaluate SWE-Bench Verified" post, and Cognition's own
  earlier SWE-grep/SWE-1.5 blog post referencing the "Semi-Async Valley of
  Death") — neither is a Cognition site page eligible for the "up to 5 linked
  pages" follow-up under MINER.md §1, and the earlier SWE-grep/SWE-1.5 post is
  referenced only for a named concept ("Semi-Async Valley of Death") that this
  note does not extract as its own claim since it was not independently read
  in full for this extraction pass.
- Searched the corpus for existing SWE-1.5, SWE-grep, Windsurf Arena, and
  "Model UX" coverage before writing Cross-References; no existing source note
  covers any of these specifically, confirming the "Novel" assessments above.
  Re-read `blog-cursor-real-time-rl.md`, `blog-cursor-composer2-technical-
  report.md`, and `blog-cursor-reward-hacking-benchmarks.md` in full and
  confirmed all cited claim numbers by content before citing them; no claim
  number was guessed or approximated.
- Filed contradiction issue #2050 before writing this note's Cross-References
  → Contradicts section, per MINER.md §4a-§4b. No verdict is asserted here;
  see the issue for full framing and the filer's tentative (non-binding)
  "debated" recommendation.
- Confidence rated `emerging` overall: the post discloses genuinely specific,
  falsifiable technical detail (a GPU-allocation derivation, named hardware,
  a self-replication figure that undercuts a competitor comparison, dogfooding-
  observed undesirable behaviors in the vendor's own model) that goes well
  beyond typical marketing framing, which is why it is not rated `anecdotal`;
  it is not rated `settled` because the training run is explicitly described
  as "ongoing" and unfinished, none of the headline figures are independently
  reproducible from published data, and the SWE-Bench Pro benchmark itself is
  under active dispute elsewhere in the corpus (see Contradicts above).
