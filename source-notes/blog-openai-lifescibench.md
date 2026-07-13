---
source_url: https://openai.com/index/introducing-life-sci-bench
source_type: blog-post
title: "Introducing LifeSciBench"
author: OpenAI
date_published: 2026-06-17
date_extracted: 2026-07-13
last_checked: 2026-07-13
status: current
confidence_overall: emerging
issue: "#1815"
---

# Introducing LifeSciBench (OpenAI)

> OpenAI describes LifeSciBench, a 750-task, expert-authored and
> expert-reviewed benchmark for real-world life science research work,
> graded with granular partial-credit rubrics (19,020 criteria total)
> rather than binary pass/fail — and reports that its own newer model
> (GPT‑Rosalind vs. GPT‑5.5) improves most on synthesis/communication
> tasks but still degrades sharply on tasks requiring artifact
> interpretation (45.1% → 28.1% pass rate) or exact numeric/sequence
> output (14.8%–27.3% pass rate).

## Source Context

- **Type**: blog-post (OpenAI official blog, "Research / Publication"
  vertical, published June 17, 2026). Links to a companion research paper
  ("Read the paper") not fetched separately for this note — all claims
  below are drawn from the blog post text itself.
- **Author credibility**: First-party account from the lab that built the
  benchmark and also owns the model (GPT‑Rosalind) shown improving on it.
  The construction methodology (173 outside scientist-authors, 453
  independent reviewers not involved in writing tasks, ≥90% inter-reviewer
  agreement required for acceptance, ≥96% agreement in the independent
  validation survey) is a real check against pure self-grading of task
  quality, but the *results* section — which model performs better — is
  OpenAI grading its own model with no independent third party cited as
  having reproduced the pass-rate numbers.
- **Scope**: Covers why LifeSciBench was built (existing life-science evals
  are narrow/structured), the task taxonomy (seven workflows × seven
  biological domains), dataset construction and review process, rubric
  grading design, independent expert validation of task quality, and
  GPT‑5.5 vs. GPT‑Rosalind results broken down by workflow, artifact
  presence, and answer format. Does NOT cover: the full research paper's
  statistical methodology, the complete list of 750 tasks, or evaluation
  of any model besides GPT‑5.5 and GPT‑Rosalind.

## Extracted Claims

### Claim 1: Existing life-science benchmarks are structured, narrow, and clean-answer, and fail to test whether a model can do broader research-level work
- **Evidence**: Stated as the article's motivating gap, contrasted against
  a description of what real research work actually looks like
  (interpreting incomplete evidence, reconciling conflicting results,
  troubleshooting assays, evaluating translational risk).
- **Confidence**: emerging (first-party framing of the benchmark's own
  motivation; not an independently audited survey of the existing
  benchmark landscape)
- **Quote**: "Many life science evaluations focus on narrow domains or
  isolated skills, resulting in questions with structured question
  formats and clean reference answers."
- **Our assessment**: This is the standard "existing benchmarks test the
  wrong thing" framing every new benchmark opens with, but the specific
  diagnosis — narrow domain + clean reference answer — is the same
  underlying complaint as construct validity problems named elsewhere in
  the corpus for coding benchmarks (see Cross-References): a benchmark
  can be easy to grade precisely because it has stripped out the
  real-world ambiguity that makes the underlying skill hard.

### Claim 2: LifeSciBench comprises 750 expert-authored tasks spanning seven workflows and seven biological domains
- **Evidence**: Stated directly as the benchmark's headline composition,
  with supporting figures (1,062 task artifacts, 173 scientist
  contributors, 19,020 rubric criteria, 453 expert reviewers).
- **Confidence**: emerging (self-reported dataset statistics for a
  benchmark released by its own authors; internally consistent with the
  other reported figures)
- **Quote**: "LifeSciBench includes 750 expert-authored tasks spanning
  seven workflows and seven biological domains."
- **Our assessment**: The seven named workflows (Evidence Handling,
  Analysis, Design/Optimization/Prediction, Reasoning, Validation &
  Operations, Translation, Scientific Communication) function as a
  reusable taxonomy for "what does applied research work actually consist
  of," independent of whether the specific task content holds up.

### Claim 3: Most LifeSciBench tasks require multi-step reasoning and more than half require interpreting a supplied artifact, not just prompt text
- **Evidence**: Stated dataset-composition statistics: percentage of
  multi-step tasks, average steps per task, percentage requiring artifact
  interpretation, and the artifact-type inventory.
- **Confidence**: emerging (self-reported composition statistics)
- **Quote**: "Overall, 79% of tasks require multiple reasoning or
  decision-making steps, with an average of four steps per task." /
  "More than half of tasks (53%) require models to interpret or
  synthesize information from at least one artifact."
- **Our assessment**: This composition claim is what makes the later
  artifact-performance-gap result (Claim 9) meaningful rather than a
  footnote — artifacts aren't an edge case in this benchmark, they are
  present in a majority of tasks, so a model's artifact-handling weakness
  drags down more than half the benchmark's surface area.

### Claim 4: Tasks were authored by 173 Ph.D.-level scientists with industry experience and went through unlimited revision cycles plus at least two rounds of expert review requiring ≥90% reviewer agreement before acceptance
- **Evidence**: Described construction pipeline: task authorship
  population, revision-cycle policy, and acceptance bar.
- **Confidence**: emerging (first-party description of an internal
  editorial/QA process; the specific cycle counts and agreement threshold
  are stated as fact but not independently auditable from the blog post
  alone)
- **Quote**: "Tasks could undergo as many revision cycles as needed before
  acceptance, with no fixed cap on the number of rounds; accepted tasks
  averaged six self-directed automated review cycles and completed at
  least two rounds of expert reviews."
- **Our assessment**: An uncapped revision process with a hard acceptance
  bar (90% agreement in the relevant domain) is a stronger quality
  control than most benchmark-construction pipelines disclose, and is the
  structural reason the independent validation scores (Claim 6) come out
  as high as they do — the two are the same quality process measured from
  two different angles (production-side review vs. post-hoc audit).

### Claim 5: LifeSciBench is graded with granular, task-specific rubrics averaging 25 criteria per task, designed so a response can be scientifically correct yet still incomplete, or partially wrong yet still show valid reasoning
- **Evidence**: Described grading design and the rationale for granular
  rubrics over final-answer-only grading, with the total criteria count
  and per-task average.
- **Confidence**: emerging (first-party grading-design description; the
  design rationale is well-argued but the *quality* of any individual
  rubric — whether its point allocations are well-calibrated — is not
  independently audited in the post)
- **Quote**: "Across the benchmark, expert-developed rubrics include
  19,020 criteria—an average of 25 per task—to assess both scientific
  correctness and usefulness for research decisions." / "a partial
  response may contain high-quality reasoning even if it does not fully
  solve the task."
- **Our assessment**: This is the most transferable methodological claim
  in the source: decomposing a free-response scientific answer into dozens
  of independently gradable criteria (assay-specificity, surrogate-endpoint
  validity, statistical-comparator critique, etc., per the worked example
  in Concrete Artifacts) is a concrete instance of "expose what needs
  checking" applied to *benchmark grading* rather than product UI — the
  benchmark author had to answer exactly the four questions
  `blog-hamel-eval-smell.md` Claim 9 poses for product designers, just for
  a grading rubric instead of a user interface.

### Claim 6: An independent panel of 453 highly credentialed reviewers, uninvolved in task writing, rated LifeSciBench tasks on realism, domain-skill relevance, scientific grounding, and overall usefulness, with agreement exceeding 96% in every category
- **Evidence**: Described validation methodology (reviewer population,
  credentials, four rating dimensions) with per-dimension "strong agree"
  and "overall agree" percentages.
- **Confidence**: emerging (first-party validation study; reviewers were
  independent of task authorship, which is a real methodological control,
  but OpenAI selected and ran the validation study itself)
- **Quote**: "We validated LifeSciBench through an independent expert
  review. Feedback came from 453 reviewers who were not involved in
  writing the tasks." / "97% held a Ph.D. or equivalent doctorate, with an
  average of 12 years of field experience and 14 peer-reviewed
  publications; 88% reported receiving at least one award or fellowship."
  / "Agreement exceeded 96% in every category."
- **Our assessment**: Separating task-authorship from task-validation
  reviewers is a real control against the benchmark grading itself as
  good on the authors' own say-so. The reviewer credential bar (97% PhD,
  average 12 years experience) supports treating the "task quality"
  claims as reasonably credible, even though this does not bear on
  whether the model-comparison results (Claims 8–11) are equally
  trustworthy — those were not independently re-graded.

### Claim 7: LifeSciBench reports two complementary metrics per task — Pass rate (binary, 70% rubric-reward threshold) and Score (continuous average rubric reward) — because scientific responses can be partially correct or useful without being complete
- **Evidence**: Explicit metric definitions given before the results
  section.
- **Confidence**: settled (as a description of the benchmark's own
  reporting methodology, directly stated and internally consistent with
  the rest of the results)
- **Quote**: "Pass rate is the percentage of tasks on which a model meets
  the task-level success threshold of 70%. Score is the average rubric
  reward, giving partial credit for individual criteria even when the
  full task is not solved."
- **Our assessment**: Reporting both a binary threshold metric and a
  continuous partial-credit metric side by side, rather than collapsing to
  one number, is what makes Claim 11 (the 14%-of-tasks near-miss finding)
  visible at all — a pass/fail-only report would have hidden that
  substantial-but-incomplete responses exist in the data.

### Claim 8: GPT‑Rosalind improves overall exact pass rate over GPT‑5.5 from 25.7% to 36.1%, with the largest workflow-level gains in Scientific Communication and Translation
- **Evidence**: Headline aggregate pass-rate comparison plus two
  named-workflow breakdowns with before/after percentages.
- **Confidence**: emerging (first-party model comparison; OpenAI is
  grading its own two models on its own benchmark, with no independent
  reproduction cited)
- **Quote**: "GPT‑Rosalind shows meaningful progress over GPT‑5.5,
  improving overall exact pass rate from 25.7% to 36.1%." / "For example,
  the Scientific Communication pass rate increases from 56.3% for
  GPT‑5.5 to 71.1% for GPT‑Rosalind; this category is small (n=9), so it
  should be interpreted cautiously, but it suggests frontier models are
  improving rapidly in their ability to organize evidence and produce
  convincing expert-facing explanations."
- **Our assessment**: The post itself flags the small-n caveat (n=9) on
  its most dramatic single-workflow result, which is a reasonable
  self-disclosed limitation rather than a cherry-picked headline number —
  but it is still the number most likely to be quoted out of context, so
  any downstream citation of the Scientific Communication figure should
  carry the n=9 caveat forward.

### Claim 9: Model performance drops sharply on artifact-heavy tasks — GPT‑Rosalind's pass rate falls from 45.1% on text-only tasks to 28.1% on tasks requiring artifact or URL interpretation, and the same pattern holds for GPT‑5.5
- **Evidence**: Direct before/after pass-rate comparison for both models
  when tasks require interpreting a supplied artifact (figure, PDF,
  table, sequence file, structure/chemical file, web reference) versus
  text-only tasks, with a stated diagnosis of the failure mode.
- **Confidence**: emerging (first-party measurement, but the underlying
  mechanism — that models struggle to extract and integrate information
  from complex figures or large sequence files — is stated as the
  authors' own diagnosis, not independently isolated per-artifact-type)
- **Quote**: "its pass rate still drops from 45.1% on text-only tasks to
  28.1% on tasks with artifacts or URLs." / "A more detailed analysis
  confirms that frontier models struggle at extracting information from
  complex figures or large sequence files and integrating that
  information into the final answer."
- **Our assessment**: This is the single most transferable result in the
  source outside the life-science domain: a ~17-point pass-rate collapse
  when a task requires grounding in a supplied artifact rather than prompt
  text alone, on a frontier model from mid-2026, in a benchmark where more
  than half the tasks require exactly that (Claim 3). It is direct
  quantitative evidence that "give the model the document/figure/file and
  it will correctly extract and use it" is still not a safe assumption,
  independent of whether the domain is life science or software.

### Claim 10: Exact-format outputs are the hardest response type for both models — GPT‑Rosalind reaches only 14.8% pass rate on numeric tasks, 24.0% on sequence/structure outputs, and 27.3% on construct-generation tasks
- **Evidence**: Answer-format breakdown of pass rates, with an explicit
  caveat about grading strictness for exact-answer tasks.
- **Confidence**: emerging (first-party breakdown; the post itself
  flags that some of the gap "may reflect a stricter grading surface for
  exact-answer tasks" rather than pure capability difference)
- **Quote**: "GPT‑Rosalind reaches only 14.8% on numeric tasks and 24.0%
  on sequence or structure outputs. Construct-generation tasks are also
  brittle, with GPT‑Rosalind at 27.3% and showing little improvement over
  GPT‑5.5."
- **Our assessment**: The post's own caveat (grading strictness may
  inflate the apparent gap) is an important qualifier the guide should
  preserve if this claim is cited — the 14.8% figure should not be read
  as "the model gets the science wrong 85% of the time" without also
  noting that small formatting/calculation deviations can zero out an
  otherwise-correct response under exact-match-style grading.

### Claim 11: In roughly 14% of tasks, models earned substantial partial credit despite failing the binary pass threshold, showing that pass/fail scoring alone hides real but incomplete capability
- **Evidence**: Cross-tabulation of Score (continuous) against Pass rate
  (binary) results, with a specific count for GPT‑Rosalind.
- **Confidence**: emerging (first-party statistical observation, directly
  computable from the two metrics defined in Claim 7; internally
  consistent with the rest of the results)
- **Quote**: "In roughly 14% of tasks, models earned substantial rubric
  credit despite failing the exact-pass threshold. For GPT‑Rosalind, 109
  tasks had pass rates below 20% while still earning at least 50% rubric
  reward."
- **Our assessment**: This is the strongest evidence in the source for why
  the granular-rubric grading design (Claim 5) is worth its construction
  cost: a pass/fail-only version of this benchmark would have reported 109
  of GPT‑Rosalind's task attempts as simple failures, when the rubric
  shows the model identified at least half of the graded content
  correctly. This directly corroborates the general "exact-match
  under-counts correct/near-correct behavior" point made elsewhere in the
  corpus (see Cross-References) with a specific, countable number.

### Claim 12: LifeSciBench measures task-level capability, not downstream research impact, and the authors explicitly frame strong benchmark performance as necessary but not sufficient evidence that a model accelerates real research
- **Evidence**: Stated directly in the "Limitations & what's next" section,
  contrasting self-contained benchmark tasks against the iterative,
  evidence-gathering, hypothesis-revising nature of real research.
- **Confidence**: settled (self-disclosed scope limitation, which
  strengthens rather than weakens the source's credibility — it is a
  specific, falsifiable boundary on the claim rather than a vague caveat)
- **Quote**: "Strong performance on LifeSciBench should therefore be
  interpreted as evidence of realistic task-level capability, not as a
  direct measure of downstream research impact." / "The next step is to
  connect benchmark performance to deployment studies in live research
  workflows."
- **Our assessment**: This is the authors correctly pre-empting the most
  likely misuse of their own benchmark (treating a pass-rate number as a
  claim about real-world research acceleration) and naming the actual gap
  that would need to be closed (live deployment studies over longer
  horizons) — the same benchmark-vs-deployment distinction the corpus
  already tracks for coding agents (see Cross-References).

## Concrete Artifacts

### Worked eval example and rubric (Evidence Handling workflow)

```
Source: https://openai.com/index/introducing-life-sci-bench,
"Eval Example" panel under "Grading and rubric breakdown"

Prompt (abridged): Pressure-test an FDA-meeting evidence package for an
AAV9-based micro-dystrophin gene therapy (AAV9-microDys-X) for Duchenne
muscular dystrophy, arguing whether micro-dystrophin expression supports
accelerated approval as a surrogate endpoint. Supplied artifacts: Western
blot quantification, immunofluorescence data, 48-week functional (NSAA)
comparison vs. an external natural-history cohort, safety data, AAV
biodistribution data, and eligibility criteria.

Rubric criteria and points (partial list, as shown):
  Identifies assay/measurement problems in micro-dystrophin
    quantification (MANEX1A epitope sharing, invalid standards,
    need for orthogonal transgene-specific measurement)        +24
  Explains why expression level is not automatically a valid
    surrogate for functional clinical benefit                  +22
  Flags biopsy-site, tissue-composition, and age-window
    confounding                                                 +19
  Critiques the NSAA comparator/statistics (external
    natural-history control, unpaired t-test)                   +12
  Addresses AAV durability, immune response, transaminitis,
    myocarditis, and follow-up needs                            +15
  Notes patient-selection/generalizability gaps                  +8
```

### Seven-workflow taxonomy

```
Source: https://openai.com/index/introducing-life-sci-bench,
"What LifeSciBench measures"

Evidence Handling — extracting, reconciling, and auditing scientific
  evidence from papers, figures, tables, and experimental records.
Analysis
Design, Optimization, & Prediction
Reasoning
Validation & Operations
Translation
Scientific Communication
```

### Dataset and validation statistics (as reported)

```
Source: https://openai.com/index/introducing-life-sci-bench

Tasks: 750
Task artifacts: 1,062
Scientist contributors (task authors): 173
Rubric criteria: 19,020 (avg. 25/task)
Independent expert reviewers (validation, not authorship): 453

Task composition:
  79% require multiple reasoning/decision-making steps (avg. 4 steps/task)
  53% require interpreting/synthesizing at least one artifact

Independent validation agreement (453 reviewers, "strong agree" / "overall agree"):
  Real-world relevance:            90.4% / 98.3%
  Scientific reasoning/domain skill: 86.4% / 98.1%
  Scientific grounding:             77.1% / 96.5%
  Overall usefulness:               79.1% / 96.6%

Results (Pass rate = % tasks meeting 70% rubric-reward threshold):
  Overall exact pass rate:        GPT-5.5 25.7%  -> GPT-Rosalind 36.1%
  Scientific Communication (n=9): GPT-5.5 56.3%  -> GPT-Rosalind 71.1%
  Translation:                    GPT-5.5 36.8%  -> GPT-Rosalind 57.7%
  Design, Optimization & Prediction:              GPT-Rosalind 30.7%
  Analysis:                                       GPT-Rosalind 30.3%
  Text-only tasks:   GPT-5.5 29.9% -> GPT-Rosalind 45.1%
  Artifact/URL tasks: GPT-5.5 21.9% -> GPT-Rosalind 28.1%
  Numeric-output tasks:            GPT-Rosalind 14.8%
  Sequence/structure-output tasks: GPT-Rosalind 24.0%
  Construct-generation tasks:      GPT-Rosalind 27.3%
  Rubric reward, expert-useful/actionable outputs: GPT-5.5 29.1% -> GPT-Rosalind 44.7%
  Rubric reward, uncertainty/caveat handling:       GPT-5.5 29.3% -> GPT-Rosalind 44.8%

Partial-credit near-misses: ~14% of tasks earned substantial rubric
  credit despite failing the pass threshold; 109 GPT-Rosalind tasks
  scored <20% pass rate while earning >=50% rubric reward.
```

## Cross-References

- **Corroborates** `blog-cursor-reward-hacking-benchmarks.md` Claim 11
  ("The goal of eval design is construct validity, not answer
  correctness: 'the benchmark measures what it claims to measure'"):
  LifeSciBench's stated design motivation (Claim 1 here — existing
  life-science evals use "structured question formats and clean reference
  answers" that fail to test broader research-level work) is an
  independently-arrived-at instance of the same construct-validity
  concern, in a different domain (life-science research vs. coding) and
  addressed with a different mechanism (free-response tasks with granular
  rubrics vs. environment isolation against retrieval).
- **Corroborates** `blog-cursor-cursorbench.md` Claims 6–7 (CursorBench
  grades across four dimensions and uses "agentic graders" for open-ended
  tasks that admit many valid solutions): LifeSciBench's granular,
  per-task rubric grading (Claim 5 here, 19,020 criteria across 750 tasks)
  is a second, independently-built example of the same design choice —
  replacing single-answer-correctness grading with multi-criterion rubric
  grading for open-ended, free-response tasks — at a larger scale of
  rubric granularity than CursorBench's four fixed dimensions.
- **Corroborates** `blog-thoughtworks-anand-agent-evaluation-framework.md`
  Claim 10 (offline metrics should distinguish exact-match accuracy from
  semantic correctness): LifeSciBench's two-metric design (Claim 7 here —
  binary Pass rate vs. continuous rubric Score) and its concrete finding
  that ~14% of tasks show substantial partial credit despite failing the
  pass threshold (Claim 11 here) is a large-scale, quantified
  demonstration of exactly the failure mode that source names in the
  abstract: exact-match-style scoring under-counts correct or
  near-correct model behavior.
- **Extends** `blog-hamel-eval-smell.md` Claim 9 (the four-question
  verification-design framework: what needs checking, what trusted
  reference to compare against, what expert heuristics exist, what
  smaller units can be accepted/edited/rejected): LifeSciBench's rubric
  construction (Claim 5 here) is that same framework applied to
  *benchmark grading* rather than *product UI design* — the worked eval
  example's six graded criteria (assay specificity, surrogate-endpoint
  validity, statistical-comparator critique, durability, safety,
  generalizability) are the benchmark-author's answer to "what does the
  user (a grader) actually need to check," decomposed into scorable units.
- **Corroborates (different domain)** the general
  benchmark-vs-real-deployment distinction already present in the corpus:
  Claim 12 here (task-level capability is not a proxy for downstream
  research impact) mirrors the same self-scoping move made in
  `blog-openai-deployment-simulation.md`'s framing of pre-deployment
  forecasting as incomplete without post-release validation — both
  sources, independently, caution against over-reading a pre-deployment
  or benchmark number as a guarantee of real-world outcome.
- **Novel**: The specific, quantified artifact-grounding performance gap
  (Claim 9 — pass rate falling from 45.1% to 28.1% when a task requires
  interpreting a supplied figure, PDF, table, sequence file, or URL,
  rather than reasoning from prompt text alone) is not documented
  anywhere else in the corpus. No existing source note reports a
  controlled before/after pass-rate comparison isolating "artifact
  present vs. absent" as the sole variable on a frontier model.
- **Contradicts**: None found. No existing source note stakes out a
  position on life-science-specific evaluation, and the general
  evaluation-methodology claims here (rubric grading, partial credit,
  construct validity) are consistent with, not opposed to, existing
  corpus claims.

## Guide Impact

- **Chapter 03 (Verification)**: The existing "Benchmark Scores Can
  Measure Retrieval, Not Coding" section already establishes construct
  validity as the goal for coding-agent evals (citing
  `blog-cursor-reward-hacking-benchmarks`) and cites CursorBench's
  multi-dimension agentic grading as one alternative to binary pass/fail.
  This source adds a second, independently-built example at much larger
  rubric granularity (19,020 criteria across 750 tasks) plus a concrete,
  countable demonstration of *why* binary pass/fail alone is
  insufficient: ~14% of tasks (Claim 11) would be reported as simple
  failures under pass/fail-only scoring despite the model earning ≥50%
  rubric credit on over 100 of them. Recommend citing this alongside the
  CursorBench material as evidence that granular partial-credit rubric
  grading is converging practice across at least two independently-built
  eval systems in different domains (coding, life sciences), not a
  one-off choice.
- **Chapter 04 (Context Engineering)**: The guide does not currently cite
  a controlled measurement of model performance when a task requires
  grounding in a supplied artifact (figure, large file, document) versus
  prompt text alone. This source's Claim 9 — pass rate dropping from
  45.1% to 28.1% (GPT‑Rosalind) and 29.9% to 21.9% (GPT‑5.5) specifically
  when a task requires interpreting an attached artifact — is a citable,
  quantified data point for a "don't assume the model faithfully extracts
  from supplied context" caution, applicable beyond life sciences to any
  workflow that hands an agent a large file, spec document, or image and
  expects correct extraction without verification. Recommend flagging
  this as evidence for structuring/pre-processing artifacts (e.g.
  extracting key figures/tables into text before handoff) rather than
  relying on raw-artifact grounding.
- Given the domain (life sciences) is narrow relative to the guide's
  general audience, recommend citing this source primarily for its
  evaluation-methodology claims (rubric design, partial credit, construct
  validity) and the artifact-grounding gap — not for any life-science
  domain-specific claim, per the Prospector's triage note that "actionability
  is lower for general practitioners."

## Extraction Notes

- The live page at `https://openai.com/index/introducing-life-sci-bench`
  returned HTTP 403 to both the WebFetch tool and a direct `curl` request
  (served an anti-bot interstitial page, not the article). The full
  article text was recovered from a Wayback Machine snapshot
  (`web.archive.org/web/20260624061916/https://openai.com/index/introducing-life-sci-bench/`,
  captured 2026-06-24, HTTP 200) fetched directly via `curl` and
  HTML-stripped for full-text extraction. All quotes in this note were
  verified against that archived text (cross-checked against the raw HTML
  source for entity-decoding accuracy, e.g. `&quot;` → `"`).
- The post links to a companion research paper ("Read the paper") that
  was not fetched separately for this note; it is noted as likely
  containing the full 750-task list, the complete rubric set, and more
  detailed statistical methodology than the blog post summarizes. A
  future extraction pass could mine the full paper if deeper
  life-science-specific detail becomes relevant.
- The reviewer-comment carousel ("Reviewer comments reinforced the
  quantitative ratings") contains three rotating testimonial quotes; only
  the visible first one plus two others captured in the same DOM extract
  were recovered ("Overall it is a strong task...", "This is an excellent
  prompt...", "It does not simply test whether a model can recall
  information..."). These are illustrative reviewer color, not
  independently load-bearing claims, so they were not extracted as
  separate numbered claims.
- No contradictions with existing source notes were identified; none
  filed.
