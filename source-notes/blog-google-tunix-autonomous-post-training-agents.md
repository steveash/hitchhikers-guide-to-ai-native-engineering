---
source_url: https://developers.googleblog.com/autonomous-llm-post-training-with-tunix-on-tpus/
source_type: blog-post
title: "Autonomous LLM post-training with Tunix on TPUs"
author: "Wei Wei, Developer Advocate (Google)"
date_published: 2026-09-11
date_extracted: 2026-09-12
last_checked: 2026-09-12
status: current
confidence_overall: anecdotal
issue: "#3405"
---

# Autonomous LLM post-training with Tunix on TPUs

> Google Developers Blog post describing `autofinetune`, a pattern for letting
> an LLM agent (Gemini Flash 3.7, via Antigravity CLI) autonomously run
> dozens of Tunix fine-tuning experiments unattended overnight, governed by
> a single `program.md` specification that declares an allowed/disallowed
> hyperparameter boundary and an objective metric, with the agent editing
> `run.py`, launching jobs, and retaining winning commits or reverting
> regressions based on that metric. Two case studies (SFT on a 270M
> function-calling model; GRPO on Gemma 3 1B for math reasoning) are given
> as evidence, both first-party and unbenchmarked against a human-tuned
> baseline.

## Source Context

- **Type**: blog-post (Google Developers Blog, published September 11, 2026)
- **Author credibility**: Wei Wei, a Google Developer Advocate, writing a
  single-author post on the official Google Developers Blog about Tunix (a
  Google-built open-source JAX-native post-training library) and
  `autofinetune`, a companion repository the author says "we created." This
  is a first-party, promotional account of the author's own project — there
  is no named external reviewer, third-party replication, or independent
  benchmark comparing the autonomous loop's results against a human expert
  tuning the same models.
- **Scope**: Covers the *workflow design* for an autonomous LLM
  post-training loop (a spec file declaring boundaries and an evaluation
  metric, a single fine-tuning script the agent edits, an agent that
  iterates and gates on the metric) and two worked case studies. Does NOT
  cover: the internal training-time infrastructure Tunix uses to run each
  experiment (that is the subject of the two other Tunix source notes in
  this corpus — see Cross-References), independent verification that the
  agent-found configurations beat a skilled human's manual tuning, or
  guidance for practitioners operating an already-deployed *coding* agent
  (this is about agents that tune *other* models, not about coding
  assistants).

## Extracted Claims

### Claim 1: The article frames "autonomous loops" as a paradigm shift from manual, human-driven hyperparameter tuning to unattended overnight agent-run experimentation
- **Evidence**: Framing statement in the subtitle/opening, contrasted
  directly against a description of the traditional manual cycle.
- **Confidence**: anecdotal (framing/marketing language from the author
  introducing their own project, not an evaluated claim)
- **Quote**: "Imagine going to sleep after writing a single Markdown
  specification and waking up to find that an AI agent ran dozens of LLM
  fine-tuning experiments overnight on your behalf" ... "Traditional
  post-training involves a repetitive, manual cycle: formulate a
  hypothesis, edit training scripts, launch a job, monitor loss curves, and
  manually record results."
- **Our assessment**: The contrast is the article's thesis, not a measured
  result — there is no reported comparison of how long the manual cycle
  actually takes versus the autonomous one, only the qualitative "repetitive
  manual cycle" vs. "ran dozens of experiments overnight" framing.

### Claim 2: The autonomous loop is structured as three components: a spec file (`program.md`) defining the loop/boundaries/evaluation criteria, a single clean execution script (`run.py`), and an agent that iterates over both
- **Evidence**: Direct description of the workflow's three-part structure.
- **Confidence**: emerging (first-party architectural description of a
  workflow the author built and is publishing code for)
- **Quote**: "An agent follows instructions in `program.md`: it modifies
  `run.py`, runs the training job, measures the target metric, retains
  winning commits or reverts regressions, and logs results in
  `results.tsv`."
- **Our assessment**: This is the single most reusable pattern in the
  source: a declarative spec (what's allowed to change, what metric wins)
  paired with one imperative script the agent is free to mutate, plus a
  persistent results log. It is structurally the same shape as a
  spec-driven autonomous coding loop — declare boundaries and a success
  metric once, then let the agent iterate against that fixed target — just
  applied to ML hyperparameter search rather than code changes.

### Claim 3: The `program.md` spec for the SFT case study explicitly enumerates an "Allowed" list of tunable hyperparameters and a separate "Disallowed" list of fixed elements the agent may not touch
- **Evidence**: Direct quote of both lists under Case Study 1's "The Setup."
- **Confidence**: emerging (first-party description of the actual spec
  content used in the reported experiment)
- **Quote**: "Allowed: LoRA rank/alpha, target projection layers, learning
  rates, warmup/decay schedules, optimizers (e.g., AdamW/Muon, gradient
  clipping), batch size, and seeds." ... "Disallowed: Changing the dataset,
  number of epochs, or model architecture."
- **Our assessment**: This is a concrete instance of an explicit
  allow/disallow boundary list gating an autonomous agent's action space —
  the same shape as this guide's two-tier MUST NEVER/MUST ALWAYS and
  three-tier Always/Ask First/Never Do boundary patterns (see Guide
  Impact), just written for an ML hyperparameter search agent instead of a
  coding agent. Notably there is no third "ask first" tier here — the
  boundary is a hard binary split, closer to the two-tier pattern than the
  three-tier one.

### Claim 4: The agent gates every experiment on a single quantitative objective metric, keeping the change ("winning commit") if the metric improves and reverting it if the metric regresses
- **Evidence**: Direct description of the accept/reject mechanism, repeated
  for both case studies.
- **Confidence**: emerging (first-party description; the article does not
  specify the exact implementation mechanism — e.g., whether "commit" means
  a literal git commit — beyond the phrase "retains winning commits or
  reverts regressions")
- **Quote**: "retains winning commits or reverts regressions, and logs
  results in `results.tsv`."
- **Our assessment**: This is a hillclimbing/greedy-search accept-reject
  loop with the objective metric as the sole oracle — no held-out
  cross-validation or statistical-significance check on the metric
  improvement is mentioned. It's a specific instance of the general
  "verify against an outcome metric, not by trusting the agent's own
  narration" principle already in this guide's verification chapter,
  applied to a training-metric objective rather than a test suite. The word
  "commits" and the presence of a persistent `results.tsv` log implies some
  form of version control or checkpointing, but the exact mechanism is not
  specified in the extracted text.

### Claim 5: Case Study 1 (SFT on FunctionGemma-270M for function-calling) ran 20 automated experiments in a couple of hours on a single Cloud TPU v5e-1, with each run taking a few minutes
- **Evidence**: Direct statement of the experiment count, hardware, and
  timing under "The Setup."
- **Confidence**: emerging (first-party reported timing/hardware; not
  independently verified against the linked repo in this extraction)
- **Quote**: "20 automated experiments in a couple of hours" ... Setup:
  "Model: google/functiongemma-270m-it, Dataset: google/mobile-actions,
  Hardware: Cloud TPU v5e-1" ... "A few minutes per run"
- **Our assessment**: The concrete, checkable numbers here (20 experiments,
  a couple of hours wall-clock, minutes per run, one small TPU chip) give a
  practitioner a real calibration point for how much compute an autonomous
  hyperparameter search over a 270M-parameter model plausibly costs — much
  cheaper than the GRPO case study (Claim 7), consistent with SFT being a
  cheaper training regime than RL.

### Claim 6: For Case Study 1, the agent is reported to have automatically adjusted LoRA rank/alpha, optimizer, and learning rate across the 20 experiments to keep improving function-call generation accuracy, but no numeric before/after accuracy figures are given in the article text
- **Evidence**: Direct claim of improvement under "Sample Trajectory,"
  referencing a results table image and a `sample_runs/SFT_results.tsv`
  file not reproduced in the article body.
- **Confidence**: anecdotal (the improvement claim is asserted in prose and
  illustrated by an image; the article text itself gives no accuracy
  percentages, so the actual magnitude of improvement cannot be checked
  from the text alone)
- **Quote**: "As you can see, the agent is able to automatically adjust LoRA
  rank/alpha, optimizer, learning rate, etc. to keep improving the model's
  accuracy in terms of generating correct function calls."
- **Our assessment**: This is the weakest-evidenced claim in the source —
  "kept improving" over 20 runs is consistent with the accept-on-improvement
  gating in Claim 4 almost by construction (a hillclimb that only keeps
  wins will show a monotonically non-decreasing best-so-far curve), but
  says nothing about how close the result is to a skilled human's manual
  tuning, or whether 20 runs was enough to reach a plateau.

### Claim 7: Case Study 2 (GRPO on Gemma 3 1B for math reasoning on GSM8K) ran 40 experiments over 2-3 days on a single Cloud TPU v6e-1, with each run taking a couple of hours, improving total reward by approximately 10%
- **Evidence**: Direct statement of setup and quantitative result under
  "The Arena Setup."
- **Confidence**: emerging (the ~10% figure is a specific, stated number,
  but it is a first-party report with no independent replication, no error
  bars, and no comparison against a human-tuned GRPO baseline on the same
  task)
- **Quote**: "Model: Gemma 3 1B, Dataset: GSM8K, Iteration Speed: A couple
  of hours per run" ... "The agent was able to identify better LoRA
  configurations, rollout temperature, KL penalty, system prompt, etc. to
  improve the total reward by ~10%."
- **Our assessment**: This is the single most concrete quantitative result
  in the source (a specific percentage tied to a specific benchmark,
  model, and experiment count) and the most useful data point for
  practitioners: an autonomous loop searching LoRA config, rollout
  temperature, KL penalty, *and* system prompt simultaneously found a ~10%
  reward improvement over 40 runs / 2-3 days on a single TPU chip. Whether
  10% is a large or small improvement depends entirely on the unstated
  baseline (what reward did the untuned starting config get?), which the
  article does not report.

### Claim 8: Unlike Case Study 1, the article does not report an explicit "Allowed"/"Disallowed" boundary list for Case Study 2's GRPO experiment
- **Evidence**: Absence noted directly against the presence of such lists
  in Case Study 1.
- **Confidence**: settled (a factual observation about what the article
  does and does not state — confirmed via a targeted re-fetch specifically
  checking for this)
- **Quote**: (no direct quote; see paraphrase — Case Study 2's "The Arena
  Setup" describes hardware, model, dataset, iteration speed, and the
  objective metric, but does not restate an Allowed/Disallowed list the way
  Case Study 1's "The Setup" does)
- **Our assessment**: This may just be an editorial choice (assuming the
  reader infers the same boundary-list pattern from Case Study 1) rather
  than evidence the GRPO run had no boundaries at all — the "LoRA
  configurations, rollout temperature, KL penalty, system prompt, etc." list
  in Claim 7 reads like an implicit "allowed" list. But taken at face value,
  the article is inconsistent in how explicitly it documents agent
  boundaries across its two case studies, which matters if a practitioner
  is trying to replicate the exact spec used.

### Claim 9: The autonomous loop uses Gemini Flash 3.7 as the acting agent, orchestrated via the Antigravity CLI, running Tunix as the underlying fine-tuning library on Cloud TPUs, and was inspired by Andrej Karpathy's `autoresearch` project
- **Evidence**: Direct naming of each component and its role, plus an
  explicit attribution of inspiration.
- **Confidence**: settled (specific, named, checkable tools and a named
  inspiration source)
- **Quote**: "the [autoresearch](https://github.com/karpathy/autoresearch)
  project showcased" ... "we created
  [autofinetune](https://github.com/windmaple/autofinetune)" ... "using
  Google's full AI stack—[Tunix](https://github.com/google/tunix)"
- **Our assessment**: Naming the exact agent model (Gemini Flash 3.7, not
  just "an LLM"), the orchestration surface (Antigravity CLI), and the
  explicit lineage from Karpathy's `autoresearch` project gives this a
  checkable provenance chain: this is presented as an application of a
  general "agent-runs-autonomous-research-loop" pattern (already
  demonstrated outside ML post-training by `autoresearch`) to the specific
  domain of LLM fine-tuning, not a novel loop-design invention by the
  Tunix team.

### Claim 10: The article does not describe any human review or approval checkpoint occurring within the autonomous loop itself between the initial spec-writing and the final results
- **Evidence**: Absence noted against the described mechanics of the loop
  (agent modifies script, runs job, measures metric, retains/reverts, logs
  results) which contains no mention of a human being consulted mid-loop.
- **Confidence**: settled (confirmed via a targeted re-fetch specifically
  checking for any described human-in-the-loop checkpoint; the described
  mechanics contain no such step)
- **Quote**: (no direct quote; see paraphrase — the described loop is
  "it modifies `run.py`, runs the training job, measures the target metric,
  retains winning commits or reverts regressions, and logs results in
  `results.tsv`," with no step in that sequence involving a human)
- **Our assessment**: This matches the article's own "go to sleep... wake up"
  framing (Claim 1) — the entire pitch is that no human attention is needed
  once the spec is written. This is the fully-autonomous end of the
  spectrum discussed elsewhere in this guide's verification chapter
  (Böckeler's fully-autonomous TDD experiment, `blog-fowler-boeckeler-tdd-in-the-agent-loop`)
  — the human's judgment is front-loaded entirely into writing the spec
  (the allowed/disallowed boundaries and the objective metric) rather than
  exercised at any point during execution.

### Claim 11: The article's closing call to action directs readers to the `autofinetune` GitHub repository and the Tunix library to build their own autonomous post-training loops
- **Evidence**: Direct closing statement under "What's Next?"
- **Confidence**: settled (direct, checkable links)
- **Quote**: "Please check out the code, sample runs, and `program.md`
  templates in the **autofinetune GitHub repository**, explore the **Tunix
  library**, and start building your own autonomous post-training lab
  today!"
- **Our assessment**: Reproducibility artifact, not a claim to assess — the
  linked repo reportedly contains the actual `program.md` templates and
  `sample_runs/*.tsv` result logs referenced but not reproduced in the
  article body (see Claim 6), so a practitioner wanting the exact spec
  text or the full 20-row/40-row results tables would need to go to the
  repository rather than the article.

## Concrete Artifacts

### Three-part autonomous loop structure (paraphrased from the article's workflow description)

```
1. Design the Arena (program.md):
   - Define the loop, boundaries (Allowed / Disallowed), evaluation
     criteria, and constraints.
2. Provide Execution Code (run.py):
   - A single, clean fine-tuning script the agent is free to edit.
3. Let the Agent Iterate:
   - Agent modifies run.py, runs the training job, measures the target
     metric, retains winning commits or reverts regressions, logs results
     to results.tsv.
```
*Source: developers.googleblog.com/autonomous-llm-post-training-with-tunix-on-tpus/,
"The Paradigm Shift: From Manual Tuning to Autonomous Loops" section.*

### Case Study 1 spec boundary (SFT on FunctionGemma-270M)

```
Model:    google/functiongemma-270m-it
Dataset:  google/mobile-actions
Hardware: Cloud TPU v5e-1
Runs:     20 automated experiments, a couple of hours total, minutes/run

Allowed:    LoRA rank/alpha, target projection layers, learning rates,
            warmup/decay schedules, optimizers (e.g., AdamW/Muon, gradient
            clipping), batch size, and seeds.
Disallowed: Changing the dataset, number of epochs, or model architecture.

Objective:  function call generation accuracy
```
*Source: developers.googleblog.com/autonomous-llm-post-training-with-tunix-on-tpus/,
Case Study 1, "The Setup."*

### Case Study 2 spec boundary (GRPO on Gemma 3 1B, math reasoning)

```
Model:    google/gemma-3-1b-it
Dataset:  GSM8K
Hardware: Cloud TPU v6e-1
Runs:     40 experiments over 2-3 days, a couple of hours/run

Tunable (not labeled "Allowed" in the article, but described as what the
agent varied): LoRA configurations, rollout temperature, KL penalty,
system prompt, etc.

Result:   total reward improved by ~10%
```
*Source: developers.googleblog.com/autonomous-llm-post-training-with-tunix-on-tpus/,
Case Study 2, "The Arena Setup."*

### Links referenced in the article

```
https://github.com/karpathy/autoresearch          (inspiration project)
https://github.com/windmaple/autofinetune         (this project's repo)
https://github.com/google/tunix                   (underlying training library)
https://huggingface.co/google/functiongemma-270m-it
https://huggingface.co/datasets/google/mobile-actions
https://huggingface.co/google/gemma-3-1b-it
```

## Cross-References

- **Extends**: `blog-google-tunix-agentic-rl-throughput.md` (issue #2135)
  and `blog-google-tunix-gemma-reasoning-hackathon.md` (issue #1532) — both
  prior Tunix notes concluded "no direct chapter impact" because they cover
  ML training infrastructure and human-driven post-training recipes, a
  different layer/audience than this guide's harness-engineering scope.
  This source describes a third, distinct layer built on the same
  underlying library: an *agent* (not a human, not the training
  infrastructure itself) driving the post-training *process* — writing a
  spec, iterating on a script, gating on a metric. It is the first Tunix
  source note where the subject is agent behavior/orchestration rather
  than ML infrastructure or ML methodology, which is why (unlike its two
  predecessors) it has a plausible Guide Impact case below.
- **Corroborates**: This guide's existing boundary-system material
  (`guide/02-harness-engineering.md`, "The Three-Tier Boundary System" and
  "Agent Boundaries," sourced from `blog-addyosmani-code-agent-orchestra`
  and `practitioner-frankray78-netpace`) already documents Always
  Do/Ask First/Never Do and MUST NEVER/MUST ALWAYS boundary lists gating
  coding-agent actions. This source's `program.md` Allowed/Disallowed list
  (Claim 3) is the same boundary-declaration pattern independently applied
  to an ML-hyperparameter-search agent — corroborating evidence that
  explicit allow/disallow action-space declarations are a general pattern
  for constraining autonomous agents, not something specific to coding
  harnesses.
- **Contradicts**: None found. No existing source note takes a position
  this source opposes.
- **Novel**: No existing source note documents (a) a spec-file-driven
  autonomous *research* loop (as opposed to a coding-task loop) where the
  human's only involvement is writing the spec and the agent runs fully
  unattended for hours/days; (b) an explicit lineage from Karpathy's
  `autoresearch` project to a domain-specific application (LLM
  post-training); or (c) a hillclimbing accept/revert-on-regression
  mechanism gated on a single training metric as the sole verification
  oracle for an autonomous agent loop.

## Guide Impact

Unlike the two prior Tunix source notes (which found no direct chapter
impact because they cover ML training infrastructure and methodology, not
harness engineering), this source's *subject* — an agent operating inside
declared boundaries and self-gating on an objective metric — is squarely
the same pattern this guide already documents for coding agents. The
specific domain (LLM fine-tuning, not software changes) is out of scope,
but the workflow shape is a relevant data point.

- **Chapter 02 (harness-engineering.md), "The Three-Tier Boundary System" /
  "Agent Boundaries"**: Could add this source as a cross-domain data point
  showing the same Allowed/Disallowed (here, effectively two-tier, not
  three-tier — see Claim 3's assessment) boundary-declaration pattern
  applied outside coding harnesses, in an ML hyperparameter-search agent.
  Worth a one-line mention as evidence the pattern generalizes beyond
  coding agents, not a new subsection.
- **Chapter 03 (verification.md)**: The retain-winning-commit /
  revert-on-regression mechanism (Claim 4) gated on a single objective
  metric is a minimal-verification-oracle pattern worth contrasting with
  this guide's existing discussion of Böckeler's fully-autonomous mode
  (`blog-fowler-boeckeler-tdd-in-the-agent-loop`) and the general theme that
  "verify against an outcome metric, not the agent's narration" — this
  source is a case where the outcome metric is a training-loss/reward
  number rather than a test suite, and the loop runs fully unattended for
  hours to days with *no* human checkpoint (Claim 10), a more extreme
  autonomy point than anything currently cited in that chapter. Given the
  single-source, unbenchmarked, first-party nature of the evidence
  (Claims 6-7 have no baseline comparison), any citation should be framed
  as an illustrative data point, not as validated guidance to adopt
  unattended multi-day autonomous loops.
- **No change recommended to Chapters 00, 01, 04, 05, 06**: none of the
  extracted claims speak to daily-workflow practices, context engineering,
  team adoption, or security/threat-model concerns.

## Extraction Notes

- The article could not be retrieved verbatim in one bulk pass (the first
  broad-quote request was refused as exceeding a per-quote length limit
  imposed by the fetch tool); all quotes above were obtained via multiple
  targeted, short (under-40-word) fetch requests scoped to individual
  sections/subheadings, then cross-checked against each other for
  consistency. Every `Quote` field is a fragment returned verbatim by those
  targeted fetches, not a reconstruction.
- One early broad-structure fetch mis-rendered the `autoresearch` repo
  link as `github.com/karplászló/autoresearch`; a follow-up targeted fetch
  corrected this to the actual link text in the article,
  `github.com/karpathy/autoresearch` (Andrej Karpathy's project). The
  corrected URL is what's used throughout this note and in Claim 9/Concrete
  Artifacts.
- No sub-pages were followed. The article links to three GitHub
  repositories (`karpathy/autoresearch`, `windmaple/autofinetune`,
  `google/tunix`) and two HuggingFace model/dataset pages — all
  reproducibility destinations (code/models to run) rather than additional
  substantive editorial content, consistent with MINER.md's guidance to
  follow only links that "seem substantive." None of these five links was
  independently fetched to verify the article's description of their
  contents against the live repos.
- Confirmed by explicit targeted re-fetches (not just absence-by-omission
  in a summary): Case Study 2 has no stated Allowed/Disallowed list
  (Claim 8), and no human review/checkpoint step is described anywhere in
  the loop mechanics (Claim 10).
- No numeric baseline (pre-tuning accuracy or reward) is given for either
  case study, so the magnitude of improvement in Claims 6 and 7 cannot be
  independently assessed from the article text — confirmed via a targeted
  fetch asking specifically for such numbers.
- No contradiction issue was filed: this source does not oppose any claim
  in the two existing Tunix notes or any other source note in the corpus —
  it corroborates the existing boundary-system material (see
  Cross-References) rather than conflicting with it.
- Confidence overall set to **anecdotal**: the workflow description and
  named tools are checkable facts, but the substantive performance claims
  (Case Study 1's "kept improving," Case Study 2's ~10% reward lift) rest
  entirely on a single first-party author's two unreplicated case studies,
  with no baseline, no independent benchmark, and no comparison against a
  human expert performing the same tuning task.
