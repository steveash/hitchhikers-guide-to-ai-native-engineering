---
source_url: https://developers.googleblog.com/how-the-community-trained-gemma-to-think-with-tunix-and-tpus/
source_type: blog-post
title: "How the community trained Gemma to \"Think\" with Tunix and TPUs"
author: "Wei Wei, Weiren Yu, Tianshu Bao, Lance Wang, and Chris Achard (Google)"
date_published: 2026-05-28
date_extracted: 2026-07-05
last_checked: 2026-07-05
status: current
confidence_overall: anecdotal
issue: "#1532"
---

# How the community trained Gemma to "Think" with Tunix and TPUs

> Google Developers Blog recap of the Tunix Hackathon on Kaggle (11,000+
> entrants, 300+ submissions) documenting three winning post-training recipes
> — SFT+GRPO with a rubric-based judge, a three-stage SFT→SimPO→GRPO pipeline,
> and curriculum-guided GRPO with a TF-IDF reward — that converted
> non-reasoning Gemma-2-2B and Gemma-3-1B checkpoints into reasoning models on
> a single free Kaggle TPU v5e-8 in 9 hours. This is an ML post-training
> methodology report; it has only a thin, indirect connection to this guide's
> practitioner-harness-engineering scope.

## Source Context

- **Type**: blog-post (Google Developers Blog, published May 28, 2026;
  post-competition winner recap)
- **Author credibility**: Five named Google authors (Wei Wei, Weiren Yu,
  Tianshu Bao, Lance Wang, Chris Achard) writing on the official Google
  Developers Blog about a Google-run Kaggle competition. This is a first-party
  vendor/organizer account with a promotional angle (showcasing Tunix, an
  open-source Google JAX-based post-training library, and Gemma models), but
  the technical claims are attributed to named community teams' specific
  pipelines, reward functions, and code, not generic marketing copy.
- **Scope**: Covers the hackathon's top three winning submissions'
  post-training pipelines (architecture, reward design, training data
  volumes), a set of "Honorable Mentions" that includes both methodological
  submissions (a from-scratch on-policy distillation implementation;
  Gemma2-Deep's custom Deep-CoRGI dataset and "ThoughtTeacher" reward model)
  and domain applications (medical, chemistry, legal, robotics), and links to
  the Tunix GitHub repo and example notebooks. Does NOT cover: independent benchmark evaluation of the resulting
  models' reasoning quality, comparison against non-Tunix RL frameworks,
  the full leaderboard beyond the top three, or any discussion of deploying
  these models in an agentic coding/harness context.

## Extracted Claims

### Claim 1: The hackathon's goal was to convert non-reasoning Gemma-2-2B and Gemma-3-1B checkpoints into general reasoning models using only Tunix and Kaggle-provided TPUs
- **Evidence**: Stated directly as the competition's framing in the opening
  paragraph of the post.
- **Confidence**: settled (this is a factual description of the competition's
  rules/goal, not a claim requiring independent verification)
- **Quote**: "we challenged developers to transform non-reasoning base models
  (Gemma-2-2B and Gemma-3-1B) into general reasoning models, using Tunix and
  Kaggle TPUs."
- **Our assessment**: Straightforward framing claim. Establishes the
  competition's constraint set (specific small base models, specific
  open-source RL library, specific free-tier hardware) that all subsequent
  claims should be read against.

### Claim 2: Over 11,000 entrants and 300+ submissions demonstrated that reasoning post-training is achievable by the community, not just by large labs, under a limited compute budget
- **Evidence**: Aggregate participation numbers stated in the article's
  opening paragraph, offered as evidence for the "community can do this too"
  framing.
- **Confidence**: emerging (the participation count is a real, checkable
  number; the inference that scale of participation proves feasibility "for
  the community" is the organizers' own framing, not independently audited)
- **Quote**: "over 11,000 entrants and 300+ high-quality submissions proved
  that decent reasoning training can be done by the community even with a
  very limited compute budget."
- **Our assessment**: This is the article's central democratization claim.
  It is plausible directionally (300+ working submissions is a large sample),
  but "high-quality" is the organizers' own qualitative judgment with no
  stated rubric in the extracted text, and there's no comparison to a
  non-democratized baseline (e.g., what fraction of entrants failed to
  produce a working reasoning model). Treat as promotional-but-plausible,
  not as a rigorously measured feasibility rate.

### Claim 3: The compute budget for training was a single free Kaggle TPU v5e-8 for 9 hours
- **Evidence**: Stated as the compute constraint in the opening paragraph.
- **Confidence**: settled (this is the competition's stated hardware rule)
- **Quote**: "limited compute budget (Kaggle TPU v5e-8 for 9 hours)"
- **Our assessment**: This is the most concrete, reusable data point in the
  source: a specific, free, publicly-accessible hardware/time budget under
  which multiple teams produced working reasoning-post-trained small models.
  It gives practitioners a calibration point for "how much compute does
  small-model reasoning post-training plausibly require," even though it
  says nothing about quality relative to larger-budget training runs.

### Claim 4: The 1st-place submission (G-RaR, "Rubrics as Rewards") combines SFT with GRPO driven by a rubric-based LLM-as-judge reward system
- **Evidence**: Direct description of the winning architecture under the
  "1st Place: G-RaR" heading.
- **Confidence**: emerging (first-party description of a competition winner;
  no independent replication or benchmark score is given in the extracted
  text)
- **Quote**: "G-RaR trains Gemma models to produce structured reasoning by
  combining Supervised Fine-Tuning (SFT) with GRPO, driven by a novel
  rubric-based LLM-as-judge reward system."
- **Our assessment**: The two-stage SFT-then-GRPO pattern, with a rubric-based
  judge standing in for a hand-written verifier, is the pipeline shape most
  directly generalizable outside Gemma/Tunix: it's a recipe for teaching
  structured reasoning on tasks that don't have an automatically-checkable
  answer (contrast with math/code RL, which typically uses exact-match or
  execution-based rewards).

### Claim 5: G-RaR's technical implementation used a split-mesh TPU architecture, ~33k SFT samples, and a composite reward combining format, exact-answer, and rubric-judge scores
- **Evidence**: Technical Solution subsection under the G-RaR heading.
- **Confidence**: emerging (first-party technical description; specific
  numbers given but not independently verified)
- **Quote**: "split-mesh architecture on a single Kaggle TPU v5e-8, placing
  the policy/reference models on one mesh and the judge model on the other"
  ... "fine-tuned via LoRA on a ~33k sample dataset to establish a baseline"
  ... "composite reward function (Format Reward + Exact Answer Reward +
  G-RaR Score)"
- **Our assessment**: The split-mesh detail is the most operationally useful
  piece: running the policy/reference model and the LLM-judge model on
  separate TPU meshes within a single 8-chip pod is a concrete pattern for
  fitting an LLM-as-judge RL loop into a constrained single-host budget,
  which is otherwise a memory/compute problem (you need at least two models
  resident simultaneously). The composite reward (format + exact-match +
  rubric score) is a reusable reward-shaping template: layer a
  cheap/deterministic check (format, exact match) under a more expensive
  qualitative judge score.

### Claim 6: The 2nd-place submission (Pinocchio-1B) uses a three-stage pipeline — SFT (distillation), then SimPO (alignment), then GRPO (refinement)
- **Evidence**: Direct description under the "2nd Place: Pinocchio-1B"
  heading.
- **Confidence**: emerging (first-party description of a competition winner)
- **Quote**: "pipeline consists of three stages: SFT (Distillation)...SimPO
  (Alignment)...GRPO (Refinement)"
- **Our assessment**: This is a distinct pipeline shape from G-RaR's two-stage
  approach — it inserts a preference-optimization stage (SimPO) between
  distillation and RL refinement. The naming ("distillation → alignment →
  refinement") reads as marketing framing more than a technical taxonomy, but
  the underlying sequencing (imitation learning, then preference tuning, then
  RL) is a recognizable staged post-training pattern that shows up elsewhere
  in the corpus for pretraining continuation (see Cross-References).

### Claim 7: Pinocchio-1B was trained on 70k prompts using an OSS-120B teacher model and a Gemini task-router, and its authors extended Tunix with a custom SimPO loss function and an asynchronous evaluation engine
- **Evidence**: Technical Solution and "Customizing Tunix" subsections under
  the Pinocchio-1B heading.
- **Confidence**: emerging (first-party technical description; the
  task-router's function is asserted but not explained in the extracted
  text)
- **Quote**: "Trained on 70k prompts using an OSS-120B teacher model and a
  Gemini task-router." ... "Injecting a custom SimPO loss function (with
  length normalization) into the DPOTrainer" ... "Creating a high-throughput,
  asynchronous evaluation engine to process GRPO reward signals on the fly"
- **Our assessment**: Two reusable engineering details here: (1) injecting a
  custom loss function into an existing trainer class (Tunix's `DPOTrainer`)
  rather than forking the library, which is a lower-friction way to
  contribute novel loss variants to an open-source RL framework; (2) building
  an asynchronous reward-evaluation engine specifically to avoid the GRPO
  training loop stalling on judge-model latency — this is the same
  throughput problem that any LLM-as-judge RL setup faces, and async
  evaluation is the generic fix. The "Gemini task-router" detail is
  under-specified in the source (what routes to what is not explained) and
  should not be treated as a verified mechanism.

### Claim 8: The 3rd-place submission (IDEA-E Distillation) uses a two-stage SFT-then-GRPO pipeline where the GRPO stage uses curriculum guidance and a TF-IDF-based reward instead of an LLM judge
- **Evidence**: Direct description under the "3rd Place: IDEA-E Distillation"
  Technical Solution heading.
- **Confidence**: emerging (first-party description of a competition winner)
- **Quote**: "The pipeline features two stages: SFT: Fine-tuning on teacher
  data to establish the IDEA-E format. GRPO: Reinforcement learning using
  curriculum guidance and a TF-IDF reward"
- **Our assessment**: This is the cheapest of the three reward designs —
  TF-IDF is a classical, non-learned scoring method, avoiding the cost and
  latency of an LLM-as-judge entirely. It trades reward sophistication for
  speed and determinism. Combined with curriculum guidance (presumably
  ordering training examples by difficulty, though the mechanism for
  determining difficulty is not detailed in the extracted text), this is the
  most compute-frugal of the three winning recipes — notable given all three
  operated under the same 9-hour TPU budget.

### Claim 9: The IDEA-E framework's structured-reasoning format is designed to force step-by-step deduction and prevent premature guessing
- **Evidence**: Stated under the "Why it Improves Reasoning" subsection for
  IDEA-E Distillation.
- **Confidence**: anecdotal (a design-intent claim about why the format
  works, not a measured outcome — no benchmark comparing IDEA-E-formatted
  output against a baseline is given in the extracted text)
- **Quote**: "IDEA-E scaffold forces the model through step-by-step logical
  deduction before answering, preventing premature guessing"
- **Our assessment**: This is a design rationale, not an evidenced result —
  the article asserts the scaffold prevents premature guessing but doesn't
  show a metric (e.g., accuracy with vs. without the scaffold) to support it.
  Consistent with other structured chain-of-thought scaffolding claims
  elsewhere in the ML literature, but this source alone doesn't establish it
  quantitatively.

### Claim 10: Hackathon submissions beyond the top three demonstrated reasoning post-training applied to medical, chemistry, legal, and robotics domains
- **Evidence**: "Honorable Mentions" section listing domain-specific
  submissions.
- **Confidence**: anecdotal (each domain application is a single described
  submission, not an evaluated or benchmarked result)
- **Quote**: Chemistry — "step-by-step reasoning traces benefited the
  chemistry use case by enabling a small language model to solve complex
  chemistry reasoning tasks"; Legal — "GRPO reinforces structured, step-by-
  step reasoning, enabling the Gemma 3 1B model to accurately analyze complex
  legal data"; Robotics — "step-by-step reasoning generation allows the model
  to solve multi-step robotics planning and decision-making tasks"
- **Our assessment**: These are one-line summaries of individual
  hackathon submissions with no supporting metrics in the extracted text —
  each reads as a description of what the team attempted, not a validated
  outcome. Useful only as evidence that the SFT/GRPO reasoning-post-training
  pattern was applied by different teams across several verticals, not as
  evidence that it works well in any of them.

### Claim 11: Two Honorable Mentions were methodological rather than domain-specific — a from-scratch on-policy distillation implementation in Tunix, and Gemma2-Deep's custom Deep-CoRGI dataset paired with a custom "ThoughtTeacher" reward model
- **Evidence**: Two "Honorable Mentions" entries ("Eliciting Reasoning via
  On-Policy Distillation" and "Gemma2-Deep: Incentivizing Gemma to Reason
  before Answering") describing novel *training methods*, not vertical
  applications like the medical/chemistry/legal/robotics entries in Claim 10.
- **Confidence**: emerging (first-party descriptions of individual
  submissions; specific methods named, but no benchmark or replication given
  in the extracted text)
- **Quote**: On-policy distillation — "on-policy distillation method from
  scratch within the Tunix framework" ... "a larger, highly capable teacher
  model (trained in 3 phases) to generate reasoning traces dynamically in
  response to the student model's generations during training, creating a
  tighter feedback loop"; Gemma2-Deep — "curated the Deep-CoRGI (Cognitive
  Reasoning Guided Interface) dataset, specifically designed to teach Chain
  of Thought" ... "trained a custom ThoughtTeacher reward model to evaluate
  not just the correctness of the final answer, but the logical flow of the
  reasoning steps themselves"
- **Our assessment**: These two entries carry more reusable-methodology
  content than the four domain applications in Claim 10, which is why they
  warrant a dedicated claim. (1) On-policy distillation — generating teacher
  reasoning traces *dynamically in response to the student's own current
  outputs*, rather than distilling from a fixed pre-generated dataset — is a
  recognizable technique for tightening the imitation-learning feedback loop;
  implementing it "from scratch within Tunix" is another instance of the
  extend-the-trainer pattern seen in Claim 7 (custom SimPO loss injected into
  `DPOTrainer`). (2) Gemma2-Deep's ThoughtTeacher reward model targets
  *reasoning-process* quality — "the logical flow of the reasoning steps
  themselves" — rather than only final-answer correctness, which is a
  reward-shaping idea distinct from the format/exact-match/rubric composite in
  Claim 5 and the TF-IDF reward in Claim 8: it rewards the trajectory, not
  just the endpoint. Both are single-submission, unbenchmarked descriptions,
  but they are exactly the reusable-pattern content the rest of this note
  prioritizes.

### Claim 12: Google is positioning Tunix as an extensible open-source library that hackathon teams modified directly (custom loss functions, custom reward functions, custom evaluation engines) rather than treating as a fixed black box
- **Evidence**: Multiple submissions' "Customizing Tunix" subsections
  describe direct modifications to Tunix internals (Pinocchio-1B's custom
  SimPO loss injected into `DPOTrainer`; the closing call-to-action pointing
  at the GitHub repo).
- **Confidence**: emerging (demonstrated by at least the Pinocchio-1B case
  in the extracted text; presented as a general pattern by the organizers)
- **Quote**: "Check out the official Tunix repository to access the code,
  documentation, and community examples."
- **Our assessment**: The concrete evidence for "extensibility" is really
  just the one Pinocchio-1B example (custom SimPO loss in DPOTrainer); the
  organizers generalize this into a broader claim about the library's
  design philosophy. Reasonable given JAX-based RL libraries commonly expose
  trainer classes for subclassing, but this source alone only substantiates
  one instance of it.

### Claim 13: The hackathon organizers frame the event's outcome as democratizing access to structured-reasoning training recipes by making the winning approaches and code publicly available
- **Evidence**: Closing section of the post.
- **Confidence**: anecdotal (organizer framing/marketing conclusion, not an
  independently measured claim)
- **Quote**: "Tunix Hackathon democratizes training highly capable,
  structured reasoning models by producing so many impressive reasoning
  training recipes that are now all publicly available."
- **Our assessment**: This is the article's closing thesis and should be read
  as promotional framing from the event organizers (Google, who also built
  and maintains Tunix and Gemma). The underlying facts it rests on — free
  TPU access, open-source code, public recipes — are real and independently
  checkable, but "democratizes" is a value-laden characterization the
  authors apply to their own event.

### Claim 14: Winning teams' code is publicly available via the Tunix GitHub repository, including a specific GRPO example notebook and general RL documentation
- **Evidence**: Links provided in the article to `github.com/google/tunix`,
  the `examples/grpo_gemma.ipynb` notebook, and `tunix.readthedocs.io`'s RL
  design docs.
- **Confidence**: settled (these are direct, checkable links; whether they
  remain live/current at any later date is a separate question)
- **Quote**: (no direct quote; see paraphrase — the article links to
  `https://github.com/google/tunix/blob/main/examples/grpo_gemma.ipynb`,
  `https://github.com/google/tunix`, `https://github.com/google/tunix/tree/main/examples`,
  and `https://tunix.readthedocs.io/en/latest/design.html#rl`)
- **Our assessment**: These are reproducibility artifacts, not claims to
  assess — a practitioner wanting to try the recipes described in Claims 4-9
  can start from the linked GRPO example notebook rather than reimplementing
  from the prose description.

## Concrete Artifacts

### Winning pipeline shapes (from the article's per-submission headings)

```
1st: G-RaR ("Rubrics as Rewards")
  Stage 1: SFT via LoRA on ~33k samples (baseline)
  Stage 2: GRPO with composite reward:
             Format Reward + Exact Answer Reward + G-RaR Score (rubric-based
             LLM-as-judge)
  Infra:   split-mesh TPU v5e-8 — policy/reference model on one mesh,
             judge model on the other mesh

2nd: Pinocchio-1B ("Creating a Reasoning Model in 3 Acts")
  Stage 1: SFT (distillation) — from OSS-120B teacher, 70k prompts,
             Gemini task-router
  Stage 2: SimPO (alignment) — custom SimPO loss (length-normalized)
             injected into Tunix's DPOTrainer
  Stage 3: GRPO (refinement) — fed by a custom async evaluation engine
             built to process GRPO reward signals without stalling on
             judge latency

3rd: IDEA-E Distillation
  Stage 1: SFT — fine-tune on teacher data to establish the IDEA-E
             structured-reasoning format
  Stage 2: GRPO — curriculum-guided, reward = TF-IDF score (no LLM judge)
```

*Source: developers.googleblog.com/how-the-community-trained-gemma-to-think-with-tunix-and-tpus/,
per-submission "Technical Solution" and "Customizing Tunix" subsections.*

### Links referenced in the article

```
https://github.com/google/tunix
https://github.com/google/tunix/tree/main/examples
https://github.com/google/tunix/blob/main/examples/grpo_gemma.ipynb
https://tunix.readthedocs.io/en/latest/design.html#rl
https://www.kaggle.com/competitions/google-tunix-hackathon
```

## Cross-References

- **Corroborates**:
  - **blog-cursor-composer2-technical-report.md** (Claim 7 — Kimi K2.5
    continued pretraining uses a staged pipeline: 32k-sequence pretraining →
    256k long-context extension → SFT on targeted coding tasks): That note's
    assessment that "structure (general adaptation → long context →
    task-specific SFT) is a transferable recipe" is corroborated by this
    source's staged pipelines (G-RaR's SFT→GRPO, Pinocchio-1B's
    SFT→SimPO→GRPO, IDEA-E's SFT→curriculum-GRPO). Both sources independently
    show that multi-stage post-training (imitation/distillation stage
    followed by one or more RL/preference stages) is the dominant pattern
    for both large-lab (Kimi K2.5) and hackathon-scale (Gemma-2-2B,
    Gemma-3-1B) model adaptation.

- **Contradicts**: None found. No existing source note makes a claim about
  post-training pipeline design, reward shaping, or reasoning-model training
  cost that this source opposes.

- **Extends**:
  - **blog-simonwillison-diffusiongemma.md** (Gemma model-family currency):
    That note tracks DiffusionGemma's open-weight release under the Gemma
    family. This source extends the corpus's Gemma-family coverage with a
    training-methodology angle (post-training small Gemma checkpoints into
    reasoning models) rather than an architecture/release angle.
  - **blog-google-io-2026-developer-keynote.md** (Claim 6 — Gemma 4 added to
    Android Bench, Google's domain-specific leaderboard): That note
    documents Gemma models entering Google's own agentic-coding evaluation
    tooling. This source provides background on how small Gemma checkpoints
    can be made to reason at all (via the recipes described in Claims 4-9),
    which is a prerequisite capability for a small open-weight model to be
    competitive on any reasoning-dependent leaderboard.

- **Novel**: No existing source note in the corpus documents:
  - Concrete, named post-training recipes (SFT+GRPO with rubric-based
    reward; SFT+SimPO+GRPO; curriculum-guided GRPO with TF-IDF reward) for
    turning a non-reasoning small open-weight model into a reasoning model.
  - A specific, free, reproducible compute budget (Kaggle TPU v5e-8, 9
    hours) for reasoning post-training at the 1B-2B parameter scale.
  - Split-mesh TPU architecture as a pattern for co-locating a policy model
    and an LLM-judge model within a single small TPU pod for RL training.
  - Reward-shaping alternatives to LLM-as-judge for non-verifiable reasoning
    tasks (TF-IDF-based rewards, composite format+exact-match+judge rewards).
  - This is a genuinely new topic area (open-weight small-model post-training
    methodology) rather than an extension of an existing corpus thread.

## Guide Impact

The Prospector's three triage comments on this issue assessed this source as
directly relevant to Ch02/Ch03/Ch04/Ch05 of the guide. Having read the
source in full, that assessment does not hold up: this article is an ML
post-training methodology report (how to fine-tune and RL-train small
open-weight language models), and the guide's current chapters
(00-principles, 01-daily-workflows, 02-harness-engineering, 03-verification,
04-context-engineering, 05-team-adoption, 06-security-threat-model) are
about how practitioners work *with* existing AI coding agents and harnesses
— none of them addresses training or post-training LLMs. There is no
chapter section this source should update, add to, or contradict.

- **No direct chapter impact recommended.** None of Claims 1-14 describes
  a harness-engineering practice, a verification technique, a context-
  management pattern, a team-adoption process, or a security consideration
  — the guide's actual subject matter. Forcing a citation into, e.g.,
  Ch02's CLAUDE.md or permission-model sections would be a non-sequitur;
  this source says nothing about how to configure or operate an agentic
  coding harness.
- **Weak, indirect relevance only**: if the guide ever adds content about
  the broader model landscape (e.g., "which open-weight models are viable
  for local/cheap agentic tasks and why"), this source would be one data
  point that small Gemma checkpoints can be made to produce structured
  reasoning traces cheaply — but that is speculative scope the guide does
  not currently have, not a recommendation to add a section now.

## Extraction Notes

- Full article text could not be retrieved verbatim in bulk (copyright
  restriction on bulk reproduction); all quotes above were obtained via
  multiple targeted fetches asking for short (1-3 sentence), attributed,
  verbatim passages under specific section headings, then cross-checked
  against each other for consistency. Every `Quote` field above is a
  character-for-character fragment returned by those targeted fetches, not
  a reconstruction.
- No sub-pages were followed: the article links to the Tunix GitHub repo,
  a specific example notebook, Tunix's RL docs, and the Kaggle competition
  page. These are reproducibility/reference destinations (code you'd run,
  not additional editorial content) rather than substantive additional
  argument, consistent with MINER.md's "follow up to 5 linked pages that
  seem substantive" guidance — none of these four links contains
  substantive prose beyond what the blog post itself summarizes.
- The Prospector filed three separate triage comments on this issue (likely
  three independent triage passes), each proposing different chapter
  mappings (Ch02/03/04/05 in various combinations) and none matching the
  guide's actual current chapter list precisely. I've treated all three as
  input but based the Guide Impact assessment on the actual content of
  `guide/*.md` as it exists today, not on the triage comments' chapter
  numbering.
- No contradictions were found requiring a contradiction issue: this source
  does not oppose any existing source note's claims, and its content
  (ML training methodology) doesn't overlap in subject matter closely
  enough with any existing note to produce a direct claim-vs-claim conflict.
- Confidence overall set to **anecdotal**: while some individual facts
  (participation counts, compute budget, links) are settled/checkable, the
  substantive claims about *why* each recipe works (reward design quality,
  "democratization," domain-application success) rest on a single
  first-party, promotional blog post describing a one-time competition,
  with no independent benchmark or replication in the extracted text.
