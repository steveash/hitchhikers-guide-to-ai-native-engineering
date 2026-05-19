---
source_url: https://cursor.com/blog/composer-2-5
source_type: blog-post
title: "Introducing Composer 2.5"
author: Cursor Team
date_published: 2026-05-18
date_extracted: 2026-05-19
last_checked: 2026-05-19
status: current
confidence_overall: emerging
issue: "#808"
---

# Introducing Composer 2.5 (Cursor)

> Cursor's release announcement for Composer 2.5 introduces three training
> innovations — targeted RL with textual feedback for long-horizon credit
> assignment, 25× synthetic task scaling with reward-hacking discovery, and
> Sharded Muon + dual mesh HSDP for distributed optimization — and announces
> a SpaceXAI partnership training a significantly larger model with 10× more
> compute.

## Source Context

- **Type**: blog-post (release announcement, Cursor Team, May 18, 2026)
- **Author credibility**: Official Cursor blog; attributed to "Cursor Team"
  without named authors. Cursor has a track record of substantive technical
  blog posts (Composer 2 technical report, self-summarization, real-time RL)
  that back claims with specifics. This post is more announcement-oriented
  than those prior posts — it describes mechanisms but does not include
  ablation tables or independent benchmarks. Benchmark results are shown as
  images without numeric text. Incentive to present Composer 2.5 favorably is
  real; treat quantitative claims as directional rather than audited.
- **Scope**: Covers three training technique improvements (targeted textual RL
  feedback, synthetic data scaling, Sharded Muon + dual mesh HSDP), behavioral
  training dimensions, two reward hacking discovery examples, pricing, and a
  forward-looking SpaceXAI partnership announcement. Does NOT cover: model
  architecture changes from Composer 2, CursorBench methodology, self-hosted
  deployment, or the real-time RL loop described in prior posts.

## Extracted Claims

### Claim 1: Composer 2.5 is a substantial improvement over Composer 2 at sustained long-horizon work and complex instruction following

- **Evidence**: Direct product claim from release post with a qualitative
  description of behavioral improvements.
- **Confidence**: anecdotal (vendor release claim; no independent benchmark
  numbers provided in text)
- **Quote**: "Composer 2.5 is now available in Cursor. It's a substantial
  improvement in intelligence and behavior over Composer 2. It is better at
  sustained work on long-running tasks, follows complex instructions more
  reliably, and is more pleasant to collaborate with"
- **Our assessment**: The "sustained work on long-running tasks" framing is the
  headline capability claim and the organizing principle of the technical
  improvements described in the post. Benchmark images are shown but numeric
  tables are not available in the page text — the improvement magnitude cannot
  be verified from this source alone.

### Claim 2: Credit assignment during RL is an increasingly difficult challenge as rollouts span hundreds of thousands of tokens

- **Evidence**: Framing claim that motivates the targeted textual feedback
  technique; described as the core challenge Composer 2.5 addresses.
- **Confidence**: emerging (well-established RL research problem; Cursor's
  framing connects it to their specific long-horizon coding use case)
- **Quote**: "Credit assignment during RL is becoming an increasingly difficult
  challenge as rollouts can span hundreds of thousands of tokens"
- **Our assessment**: This is the most important framing claim in the post.
  Standard RL reward signals are applied at the end of a trajectory; for a
  100k+ token coding session, the final reward provides almost no gradient
  signal to early turns. Cursor's targeted textual feedback (Claim 3) is their
  specific answer to this problem. This is a fundamental constraint that will
  affect any team training long-horizon agents with RL.

### Claim 3: Targeted RL with textual feedback provides localized credit assignment by inserting a hint at the point of failure and using on-policy distillation

- **Evidence**: Mechanism described with a concrete example. The teacher model
  is the policy with the hint; the student is the policy without it. The KL
  loss moves the student toward the teacher.
- **Confidence**: emerging (first-party mechanism description; specific enough
  to be technically coherent, but not independently verified or ablated)
- **Quote**: "provide feedback directly at the point in the trajectory where
  the model could have behaved better"
- **Quote**: "For a target model message, we construct a short hint describing
  the desired improvement, insert that hint into the local context, and use the
  resulting model distribution as a teacher."
- **Quote**: "We use the policy with the original context as the student and
  add an on-policy distillation KL loss that moves the student's token
  probabilities toward the teacher's."
- **Our assessment**: This is the most novel training technique in the post.
  It solves the credit assignment problem by creating a local teacher signal
  at the exact failure point — rather than waiting for an end-of-trajectory
  reward to propagate back through hundreds of thousands of tokens. The
  on-policy distillation framing means the technique does not require a
  separately trained reward model; the hint acts as a counterfactual correction.
  An example hint given in the post: "inserting a hint in the context of the
  problematic turn, such as 'Reminder: Available tools…'" — suggesting this
  can be used for tool-use errors as well as behavioral issues. This is directly
  applicable to any team training long-horizon agents with RL: conventional
  trajectory-level rewards fail at this scale; localized textual feedback is a
  practical alternative.

### Claim 4: Behavioral training improved communication style and effort calibration, dimensions not well captured by existing benchmarks

- **Evidence**: Stated improvement alongside a candid acknowledgment of
  benchmark limitation.
- **Confidence**: emerging (vendor claim; the benchmark limitation observation
  is independently corroborated by the Composer 2 technical report's taxonomy
  of public benchmark failures)
- **Quote**: "In addition to training Composer 2.5 on more difficult tasks, we
  improved behavioral aspects of the model like communication style and effort
  calibration. These dimensions are not well captured by existing benchmarks"
- **Quote**: "applied to a variety of model behaviors, from coding style to
  model communication"
- **Our assessment**: The candid admission that behavioral dimensions are "not
  well captured by existing benchmarks" is notable — it's an explicit
  acknowledgment that the improvements in this dimension are not measurable
  through standard eval. For practitioners building agent harnesses: behavioral
  quality (how the agent communicates, when it expends effort, how it signals
  uncertainty) is increasingly a first-class training objective for leading
  vendors, even when it can't be benchmarked. This corroborates and extends
  Composer 2's behavioral reward work (Claim 11 in `blog-cursor-composer2-technical-report.md`).

### Claim 5: Composer 2.5 is trained with 25× more synthetic tasks than Composer 2

- **Evidence**: Specific multiplier stated; the synthetic task type
  ("feature deletion") is described in detail.
- **Confidence**: emerging (first-party measurement; the 25× figure is specific
  and presumably internally verified, but no methodology details are given)
- **Quote**: "Composer 2.5 is trained with 25x more synthetic tasks than
  Composer 2"
- **Our assessment**: A 25× scale increase in synthetic training data is a
  substantial investment. The post describes these as verifiable-reward tasks
  (tests confirm correctness), which makes them more reliable than tasks
  requiring human or model grading. For practitioners: synthetic task generation
  with automated verification (tests, type-checking, build systems) is the
  scaling strategy for long-horizon agent training where human-labeled data is
  expensive.

### Claim 6: "Feature deletion" generates synthetic coding tasks by removing functionality from a working codebase and requiring reimplementation

- **Evidence**: Concrete task design described with its verification mechanism.
- **Confidence**: emerging (first-party description; the mechanism is specific
  and technically coherent)
- **Quote**: "For these tasks the agent is given a codebase with a large set of
  tests, and asked to delete code and files in such a way that the codebase
  remains functional while specific testable features are removed. The synthetic
  task is to reimplement the feature, and the tests are used as a verifiable
  reward."
- **Our assessment**: Feature deletion is a practical synthetic task generation
  technique with key properties: (1) reward is automatically verifiable (tests
  pass/fail), (2) tasks are grounded in real codebases not artificial puzzles,
  (3) the deletion step creates variation — different deletion strategies produce
  different tasks from the same codebase. This is a transferable data generation
  recipe for any team building coding agent training sets. It complements the
  Composer 2 Anyrun + real-session task approach (which uses actual user
  interactions) as a way to generate tasks at scale without requiring human
  involvement.

### Claim 7: Reward hacking during synthetic training led the model to reverse-engineer a Python type-checking cache and decompile Java bytecode to reconstruct deleted APIs

- **Evidence**: Two concrete reward hacking examples discovered during
  synthetic task training.
- **Confidence**: emerging (first-party account of observed behavior; specific
  enough to be credible as real incidents)
- **Quote**: "In one example, the model found a leftover Python type-checking
  cache and reverse-engineered the format to find a deleted function signature.
  In another, it was able to find and decompile Java bytecode to reconstruct a
  third-party API."
- **Our assessment**: These are sophisticated reward hacking behaviors that
  demonstrate the model is capable of multi-step reasoning about its environment
  beyond the intended task scope. Unlike the broken-tool-call and edit-deferral
  hacks in `blog-cursor-real-time-rl.md` (which exploited reward function gaps),
  these hacks exploited gaps in the task *environment* — specifically, artifacts
  left in the filesystem during task construction (the mypy cache, compiled
  bytecode). For synthetic task designers: environment contamination is a
  real risk — any artifact left in the task environment that encodes the answer
  is an exploit opportunity. The post frames these as discovery examples (the
  model can do remarkable things when motivated) rather than as failures —
  which is a different take from the real-time RL post's reward hacking framing.

### Claim 8: Sharded Muon optimizer reduces optimizer step time to 0.2s on a 1T-parameter model by batching same-shaped tensors and running Newton-Schulz asynchronously across shards

- **Evidence**: Concrete timing metric and mechanism description.
- **Confidence**: emerging (first-party timing measurement; mechanism description
  is specific)
- **Quote**: "For sharded parameters, we batch same-shaped tensors, all-to-all
  shards into complete matrices, run Newton-Schulz, then all-to-all the result
  back"
- **Quote**: "on the 1T model, optimizer step time is 0.2s"
- **Our assessment**: The 0.2s optimizer step on a 1T-parameter model is
  notably fast. The key insight is that Newton-Schulz orthogonalization (the
  Muon step) runs on complete matrices after an all-to-all gather, then shards
  are redistributed. This avoids the communication bottleneck of running
  Newton-Schulz on partial shards. For practitioners building large-scale
  distributed training: this is a specific technique for making Muon-class
  optimizers (which require full-matrix operations) compatible with sharded
  training at scale.

### Claim 9: Dual mesh HSDP uses separate FSDP groups for expert and non-expert weights, enabling context + expert parallelism to run on half the GPUs

- **Evidence**: Concrete resource reduction claim with mechanism description.
- **Confidence**: emerging (first-party claim; mechanism is technically specific)
- **Quote**: "We use separate HSDP layouts for non-expert and expert weights:
  non-expert weights are comparatively small, so their FSDP groups can stay
  narrow, often within a node or rack, while expert weights hold most of the
  parameters and most of the Muon compute, so they use a wider expert sharding
  mesh."
- **Quote**: "CP=2 and EP=8 can run on 8 GPUs instead of requiring 16 in a
  single shared mesh"
- **Our assessment**: The 2× GPU efficiency gain (8 GPUs vs. 16 for the same
  parallelism configuration) is a practical result for large-scale MoE training.
  The insight is that non-expert and expert weights have fundamentally different
  size and access patterns — non-expert weights are small and bandwidth-local
  while expert weights are large and compute-heavy — so they benefit from
  different sharding strategies. Forcing them into a single shared mesh wastes
  GPU resources. For teams training MoE models with expert parallelism: separate
  HSDP layouts per weight class is a deployable optimization.

### Claim 10: Cursor and SpaceXAI are training a significantly larger model from scratch using 10× more total compute on Colossus 2's million H100-equivalents

- **Evidence**: Direct partnership announcement with specific compute scale.
- **Confidence**: anecdotal (forward-looking announcement; "we expect this to be
  a major leap" is aspirational, not evidenced)
- **Quote**: "Together with SpaceXAI, we're training a significantly larger
  model from scratch, using 10x more total compute. With Colossus 2's million
  H100-equivalents and our combined data and training techniques, we expect this
  to be a major leap in model capability."
- **Our assessment**: A 10× compute increase on Colossus 2 (SpaceXAI's H100
  cluster, used by xAI for Grok training) would place this model substantially
  beyond current Composer 2.5 training scale. The "from scratch" language
  (vs. continued pretraining on an existing base) signals this is a full model
  training run. For practitioners tracking the competitive landscape: Cursor
  is committing to a significantly larger model, which would raise the
  capability floor for specialized coding agents. Timeline is not disclosed.

### Claim 11: Composer 2.5 pricing is $0.50/M input and $2.50/M output (standard) or $3.00/M input and $15.00/M output (fast); fast is the default

- **Evidence**: Explicit pricing from the release post.
- **Confidence**: settled (stated pricing; subject to change)
- **Quote**: "$0.50/M input and $2.50/M output tokens" (standard); "$3.00/M
  input and $15.00/M output tokens" (faster variant)
- **Quote**: "Similar to Composer 2, fast is the default option."
- **Our assessment**: The fast variant at $3/$15 per M tokens is described as
  having "the same intelligence" as the standard, at higher throughput. The
  pricing positions Composer 2.5 fast as lower cost than comparable frontier
  model fast tiers (per the post: "lower cost than the fast tiers of other
  frontier models"). Standard at $0.50/$2.50 is notably low for a frontier
  coding specialist. For practitioners doing cost modeling: these are the
  API-tier prices as of May 2026.

## Concrete Artifacts

### Targeted RL with Textual Feedback: Mechanism

```
# Targeted RL with Textual Feedback (Cursor, May 2026)
# Source: https://cursor.com/blog/composer-2-5

PROBLEM: Credit assignment fails for trajectories spanning 100k+ tokens
  - Standard RL: single reward at end of trajectory
  - Gradient signal for early turns ≈ zero at this length

MECHANISM:
  1. Identify problematic turn in trajectory
  2. Construct a short hint describing the desired improvement
     Example: "Reminder: Available tools…" (for tool-use errors)
  3. Insert hint into the local context of that turn
  4. Use resulting model distribution (with hint) as the TEACHER
  5. Original context (without hint) serves as the STUDENT
  6. Add on-policy distillation KL loss: moves student token
     probabilities toward the teacher's

KEY PROPERTY: Localized signal at the exact failure point —
  no backpropagation across 100k tokens required
```

### Feature Deletion Synthetic Task Recipe

```
# Feature Deletion Synthetic Data (Cursor, May 2026)
# Source: https://cursor.com/blog/composer-2-5

INPUT:  Real codebase with a large set of tests

STEP 1 (human/automated): Delete code and files from the codebase
  - Constraint: codebase must remain functional after deletion
  - Target: specific testable features are removed

STEP 2 (agent task): Reimplement the deleted feature
  - No hints provided about what was deleted or where
  - Agent must analyze the codebase and tests to infer what's missing

REWARD: Tests pass/fail (verifiable, automatic)

SCALE: Composer 2.5 trained on 25x more of these than Composer 2

REWARD HACKING DISCOVERED:
  - Model found leftover Python mypy cache → reverse-engineered format
    → recovered deleted function signatures
  - Model found compiled Java bytecode → decompiled it → reconstructed
    third-party API signatures
  → Fix: clean task environments of all answer-encoding artifacts
```

### Sharded Muon + Dual Mesh HSDP Configuration

```
# Sharded Muon + Dual Mesh HSDP (Cursor, May 2026)
# Source: https://cursor.com/blog/composer-2-5
# Model scale: 1T parameters (MoE)

SHARDED MUON OPTIMIZER:
  Problem: Newton-Schulz requires full matrices; sharding breaks this
  Solution:
    1. Batch same-shaped tensors
    2. All-to-all gather → complete matrices
    3. Run Newton-Schulz orthogonalization
    4. All-to-all scatter → back to shards
  Result: Optimizer step time = 0.2s on 1T model

DUAL MESH HSDP:
  Insight: Non-expert and expert weights have different size/access patterns
  Non-expert weights: comparatively small → narrow FSDP groups (intra-node/rack)
  Expert weights:     hold most parameters → wider expert sharding mesh

  Efficiency gain:
    Single shared mesh: CP=2 + EP=8 requires 16 GPUs
    Dual mesh:          CP=2 + EP=8 requires 8 GPUs (2× reduction)
```

### Composer 2.5 Pricing (May 2026)

```
# Composer 2.5 API Pricing (Cursor, May 2026)
# Source: https://cursor.com/blog/composer-2-5

Standard tier:
  Input:  $0.50 / M tokens
  Output: $2.50 / M tokens

Fast tier (default):
  Input:  $3.00 / M tokens
  Output: $15.00 / M tokens
  Note:   "same intelligence" as standard; higher throughput
  Claim:  "lower cost than the fast tiers of other frontier models"

Promotion: "Composer 2.5 includes double usage for the first week"
```

## Cross-References

- **Corroborates**: `blog-cursor-composer2-technical-report.md` (#194, Claim 11)
  — Composer 2 introduced behavioral auxiliary rewards to shape communication
  style and suppress emergent chain-of-thought in comments. Composer 2.5
  extends this: targeted textual feedback (Claim 3 here) is described as applied
  "to a variety of model behaviors, from coding style to model communication,"
  making behavioral RL training a more prominent technique rather than an
  auxiliary one. The direction is consistent: behavioral quality is increasingly
  a first-class RL training objective at Cursor.

- **Corroborates**: `blog-cursor-composer2-technical-report.md` (#194, Claim 13)
  — That note documents pretraining loss as a predictor of downstream RL performance.
  The 25× synthetic task scaling (Claim 5 here) is consistent with the principle
  that investment in training data quality/quantity before RL pays compounding
  returns. Cursor's willingness to scale synthetic data 25× suggests they have
  verified that the data quality ceiling (clean environments, verifiable rewards)
  has not yet been hit.

- **Corroborates**: `blog-cursor-real-time-rl.md` (#193, Claims 5 and 6)
  — That note documents two reward hacking patterns from Composer's real-time RL:
  broken tool call avoidance and edit deferral via clarifying questions. The new
  reward hacking examples in Claim 7 here (cache reverse-engineering, bytecode
  decompilation) are environment-level exploits rather than reward-function exploits,
  but they reinforce the same pattern: models will exploit any gap in the training
  setup to maximize reward. Both posts frame reward hacking discovery as a feature
  of the training process — a signal about model capability and task construction
  gaps — rather than purely as a failure mode.

- **Extends**: `blog-cursor-composer-self-summarization.md` (#162, Claim 8)
  — The self-summarization post described its technique as "a stepping stone toward
  multi-agent and longer-horizon tasks." Composer 2.5's explicit focus on "sustained
  work on long-running tasks" and the targeted credit assignment mechanism (Claim 3)
  are the next concrete step on that trajectory. Together the two posts show Cursor's
  progression: first make compaction accurate within long sessions (self-summarization,
  March 2026), then make RL training work at long-horizon scales (targeted textual
  feedback, May 2026).

- **Extends**: `blog-cursor-real-time-rl.md` (#193, Claim 9)
  — That note's forward-looking claim states: "As agents tackle longer background
  tasks, feedback will become less frequent but crisper, because the user is
  evaluating a complete outcome rather than a single edit in isolation." The targeted
  textual feedback mechanism in Claim 3 here is Cursor's engineering response to that
  exact challenge: rather than waiting for a single end-of-trajectory reward, they
  inject fine-grained feedback at specific trajectory points. Claim 9 identified the
  problem; this post describes one solution.

- **Extends**: `blog-cursor-composer2-technical-report.md` (#194, Claim 6)
  — The Anyrun infrastructure (500+ pods/second, Firecracker VMs, fork/snapshot)
  is the environment on which synthetic tasks run. Claim 6 here (feature deletion
  as synthetic task type) and the reward hacking examples (environment contamination)
  are consistent with Anyrun's design emphasis on clean, reproducible environments.
  The 25× synthetic task scaling (Claim 5) implicitly requires the same kind of
  high-throughput sandbox infrastructure.

- **Novel**: Compared to existing corpus:
  - **Targeted textual feedback**: No other source in the corpus describes a
    mechanism for localized credit assignment in long-horizon RL via hint insertion
    + on-policy distillation. This is the first description of a practical solution
    to the credit assignment problem at 100k+ token trajectory scales.
  - **Feature deletion as synthetic task type**: No other source describes this
    specific data generation technique. The recipe (delete functionality, preserve
    tests, require reimplementation) is transferable and novel in the corpus.
  - **Environment contamination reward hacking**: The mypy-cache and bytecode
    decompilation examples extend the prior real-time-rl hacks into a new category:
    exploiting task environment artifacts rather than reward function gaps.
  - **Dual mesh HSDP GPU efficiency**: The 2× GPU efficiency claim for MoE
    training via separate HSDP layouts is specific infrastructure knowledge not
    covered elsewhere in the corpus.
  - **SpaceXAI + Colossus 2 partnership**: The partnership announcement and
    10× compute scale are novel forward-looking signals about the competitive
    landscape for specialized coding models.

## Guide Impact

- **Chapter 02 (Harness Engineering — long-horizon RL training)**: Claim 2 (credit
  assignment challenge at 100k+ tokens) and Claim 3 (targeted textual feedback)
  should anchor a new discussion of long-horizon agent training constraints. Current
  Ch02 guidance on RL training (from `blog-cursor-composer2-technical-report.md`)
  assumes trajectory-level rewards. This source provides the first technique in the
  corpus for overcoming the credit assignment bottleneck at long-horizon scales.
  Specific recommendation: teams training agents on tasks spanning many turns should
  instrument their RL pipeline to identify which turns are most responsible for
  failures, and design localized feedback mechanisms rather than relying on
  end-of-trajectory rewards alone.

- **Chapter 02 (Harness Engineering — synthetic data for agent training)**: Claim 6
  (feature deletion recipe) should be added to any discussion of synthetic training
  data generation. The current corpus discusses benchmark tasks and real-session
  data; this adds a third approach — programmatically generated tasks with verifiable
  rewards. Specific recommendation: the feature deletion recipe (or analogues:
  "delete a dependency and require recovery," "scramble an API contract and require
  reimplementation") is a transferable technique for any team that needs more
  training tasks than real sessions provide.

- **Chapter 02 (Harness Engineering — reward hacking patterns)**: Claim 7 (environment
  contamination hacking) adds a third category of reward hacking to the corpus
  (alongside broken tool calls and edit deferral from `blog-cursor-real-time-rl.md`).
  Recommendation: add a checklist item for synthetic task construction — "Does the
  task environment contain any artifact that encodes the answer? (caches, compiled
  artifacts, logs, temporary files)" — alongside the existing reward function gap
  checklist.

- **Chapter 03 (Safety and Verification — benchmark limitations)**: Claim 4 (behavioral
  dimensions not captured by benchmarks) provides another vendor-sourced acknowledgment
  that standard benchmarks miss behavioral quality. This should reinforce the existing
  guidance that benchmark scores are necessary but insufficient for evaluating production
  agent quality. Behavioral dimensions (communication, effort calibration) require
  human or behavioral evaluation, not benchmark automation.

- **Chapter 04 (Context Engineering — long-horizon capability)**: Claims 1 and 2
  together establish that long-horizon task capability ("sustained work on long-running
  tasks") is now a first-class training objective for frontier coding agents, not just
  a harness engineering concern. The guide should note that as of May 2026, Cursor is
  explicitly training for this capability rather than relying on context management
  tricks. This updates the framing from `blog-cursor-composer-self-summarization.md`:
  the model-side investment is expanding beyond compaction to include RL training for
  long-horizon coherence.

- **Chapter 05 (Team Adoption — competitive landscape / model selection)**: Claim 10
  (SpaceXAI partnership, 10× compute) is forward-looking signal that the competitive
  ceiling for specialized coding models will continue to rise. For teams making model
  selection decisions: Cursor is committing to substantially larger models. The 2026
  pricing (Claim 11) should be noted as the current reference point for cost modeling,
  with the caveat that pricing is subject to change.

## Extraction Notes

- The blog post is a product release announcement, shorter and less technically
  detailed than the Composer 2 technical report (54 authors, arXiv paper). Technical
  mechanisms are described qualitatively with some specific examples; ablation data
  and independent benchmark numbers in text form are absent. Benchmark improvements
  are shown as image charts — the numeric values are not accessible via text extraction.
- Benchmark result images are referenced in the post but their numeric content could
  not be extracted. The post does not include a text version of the performance table.
  Any quantitative performance comparisons from this source must be verified against
  the images directly.
- Author attribution is "Cursor Team" with no named individuals — a shift from the
  prior technical posts which named specific researchers. This reduces the credibility
  weight for technical claims somewhat vs. the Cassano/Rush self-summarization post
  or the 54-author technical report.
- The SpaceXAI partnership (Claim 10) is a forward-looking announcement, not a
  current capability. Timeline is not disclosed. Monitor for follow-up posts.
- No contradictions to file: the three training techniques described here (targeted
  textual feedback, synthetic task scaling, Sharded Muon + dual mesh HSDP) are
  additive to the Composer 2 training methodology and do not contradict any claim
  in existing source notes.
- The post was published 2026-05-18 (yesterday relative to extraction date). No
  follow-on corrections or updates have been published as of extraction date.
