---
source_url: https://cognition.com/blog/swe-check-10x-faster
source_type: blog-post
title: "Introducing SWE-Check: 10x Faster Bug Detection"
author: Raymond Feng (Applied Compute), Jeffrey Ling (Cognition AI), Rhythm Garg (Applied Compute), Moritz Stephan (Cognition AI)
date_published: 2026-04-14
date_extracted: 2026-07-17
last_checked: 2026-07-17
status: current
confidence_overall: emerging
issue: "#1970"
---

# Introducing SWE-Check: 10x Faster Bug Detection

> Cognition and Applied Compute's joint technical account of RL-training a
> small, specialized bug-detection model (SWE-check) that matches Opus 4.6 on
> in-distribution evals and closes most of the gap out-of-distribution, at an
> order-of-magnitude-faster wall-clock runtime — using reward linearization
> and two-phase post-training (capability first, then dogfooding-derived
> latency alignment) inside a Windsurf-harness-identical training sandbox.

## Source Context

- **Type**: blog-post (joint post from Cognition AI and Applied Compute,
  cognition.com/blog, published 04.14.26 per the page's own byline, i.e.
  2026-04-14)
- **Author credibility**: Four named individual authors, two from each
  partner company (Raymond Feng and Rhythm Garg, Applied Compute; Jeffrey
  Ling and Moritz Stephan, Cognition AI) — a joint technical post rather than
  an unattributed company-blog announcement, which is a step up in
  named-authorship specificity from several other Cognition posts already in
  this corpus (`blog-cognition-auto-triage.md`, `blog-cognition-devin-in-
  windsurf.md`, both bylined only "The Cognition Team"). This is nonetheless
  a first-party vendor account of a shipped, promoted feature (SWE-check
  ships inside Windsurf, a Cognition product) — the two companies have a
  direct commercial incentive to present the result favorably. The post
  discloses one unflattering-to-neutral detail against that incentive: the
  model is explicitly "behind the frontier on out-of-distribution evals in
  terms of pure capability," and the Conclusion states the model "is not
  categorically the most capable model on this task."
- **Scope**: Covers the case for model specialization (cost/latency vs.
  frontier capability trade-off), the SWE-check agent's product requirements
  (structured output for Windsurf rendering, near-real-time latency to avoid
  "The Semi-Async Valley of Death"), the training methodology (production-
  representative sandbox mirroring the Windsurf harness, a curated
  multi-language bug dataset), the reward-function design (reward
  linearization, two-phase post-training, a dogfooding-derived latency
  penalty), quantitative in-distribution and out-of-distribution delta-F1
  comparisons to Opus 4.6, and availability (Windsurf Next preview via
  cmd+U, general Windsurf release "soon"). Does NOT cover: SWE-check's
  parameter count or base model identity, absolute F1/accuracy numbers (only
  deltas to Opus 4.6 are given), independent/third-party benchmark
  validation, false-positive rate, pricing, or any named customer using
  SWE-check in production (unlike several other Cognition posts in this
  corpus that include a named-customer quote).

## Extracted Claims

### Claim 1: Smaller, specialized models can rival frontier generalist models on the specific tasks they are trained for, at a fraction of the cost and latency — and SWE-check is offered as the test case, via an RL-training partnership with Applied Compute
- **Evidence**: Opening thesis statement of the post, immediately followed by
  the specific delta-F1 comparison figures that back it (Claim 2).
- **Confidence**: emerging (a general thesis backed by one first-party,
  single-model case study with disclosed but unaudited metrics; no
  independent replication)
- **Quote**: "Smaller, specialized models can rival frontier generalists on
  the tasks they're trained for, at a fraction of the cost and latency. We've
  partnered with Applied Compute to put this to the test by collaborating to
  RL-train a bug detection model."
- **Our assessment**: This is a direct, named articulation of the
  specialization-vs-frontier-generalist trade-off already present in this
  corpus's Cursor Composer coverage (see Cross-References → Corroborates),
  but applied here to a narrower, single-purpose task (bug detection in a
  diff) rather than to a general-purpose coding agent. The claim should be
  read as a single case study offered as evidence for a broader thesis, not
  as a controlled comparison across multiple specialized-vs-frontier
  deployments.

### Claim 2: SWE-check matches Opus 4.6 on internal in-distribution evals (delta F1 goes from 0.09 to 0) and closes most, but not all, of the gap on out-of-distribution evals (delta F1 goes from 0.49 to 0.29)
- **Evidence**: Quantitative delta-F1 figures stated directly in the opening
  paragraph, framed as the headline evidence for Claim 1.
- **Confidence**: emerging (specific, disclosed delta metrics against a
  named frontier model; but these are deltas only — no absolute F1 values,
  no disclosed eval set composition or size, and no independent audit)
- **Quote**: "The result is SWE-check, which matches frontier performance on
  internal in-distribution evals (delta F1 to Opus 4.6 goes from 0.09 to 0)
  and makes meaningful progress on out-of-distribution evals (delta F1 to
  Opus 4.6 goes from 0.49 to 0.29)."
- **Our assessment**: The in-distribution figure (0.09 to 0) supports a
  strong "matches frontier" claim; the OOD figure (0.49 to 0.29) supports a
  weaker "meaningful progress, not parity" claim — the post is careful to
  distinguish these two conditions rather than blending them into a single
  headline number. Because only deltas are disclosed (not absolute F1
  scores or eval set details), the guide should cite this as a directional,
  vendor-disclosed result rather than a fully specified, reproducible
  benchmark comparison.

### Claim 3: The SWE-check agent's product requirements were structured output (for rendering bug descriptions/fixes in Windsurf) and near-real-time latency, explicitly framed as avoiding "The Semi-Async Valley of Death"
- **Evidence**: Direct requirements statement from "The SWE-check Agent and
  its requirements" section, naming both the output-format constraint and
  the latency constraint with an internal Cognition term for the failure
  mode being avoided.
- **Confidence**: settled (first-party statement of the product requirements
  that shaped training, internally consistent with the reward-function
  design described later in the post)
- **Quote**: "The agent also needs to be near-real time and keep users _in
  flow_, avoiding at all costs what we call [The Semi-Async Valley of
  Death]"
- **Our assessment**: "The Semi-Async Valley of Death" is a named Cognition
  concept for a agent-response-time failure mode — a response too slow to
  feel synchronous but too fast to justify a context switch, so it disrupts
  user flow either way. This post does not itself define the term
  numerically (no latency threshold is given); it is used here, as in a
  companion Cognition/Windsurf post already in this corpus, as an
  unquantified mental-model heuristic rather than a specified threshold (see
  Cross-References → Extends).

### Claim 4: Training replicated the toolset available in the production Windsurf harness inside the training sandbox, and used a curated, multi-language, diverse-bug-type dataset iterated on jointly by both partner teams to match production distribution
- **Evidence**: Direct methodology statement from the "Training with
  production settings" section, naming both the harness-fidelity mechanism
  and the dataset curation process.
- **Confidence**: emerging (first-party description of training
  methodology; no dataset size, language list, or bug-type taxonomy is
  disclosed)
- **Quote**: "To that end, we replicated the toolset available in the
  Windsurf harness in the training sandbox. We also curated a dataset with
  diverse bug types over many programming languages, and we iterated on the
  dataset together to ensure that the distribution was representative of
  what was expected in production."
- **Our assessment**: "Replicated the toolset available in the Windsurf
  harness in the training sandbox" is a specific, named instance of
  train/deploy environment-fidelity — the same principle documented at
  larger scale and with more infrastructure detail in this corpus's Cursor
  Composer 2 coverage (see Cross-References → Corroborates). No detail is
  given here on how the joint dataset-iteration process worked operationally
  (e.g., how disagreements between the two teams' notions of "representative"
  were resolved), which limits how directly this specific claim can be
  operationalized by a reader.

### Claim 5: The reward design rested on two named techniques — reward linearization (a sample-level proxy for a population-level statistic) and two-phase post-training (maximize capability first, then align to product latency) — because training both objectives simultaneously converged on a fast-but-shallow local optimum
- **Evidence**: Direct technical description of both named techniques, plus
  an explicit statement of the failure mode observed when the two objectives
  were trained jointly instead of in sequence.
- **Confidence**: emerging (first-party description of a specific technical
  design choice with a named, concrete failure mode as justification; no
  ablation data comparing joint vs. two-phase training is disclosed
  numerically)
- **Quote**: "Reward linearization to provide a sample-level reward which
  serves as a proxy for hill-climbing the population level statistic... Two-
  phase post-training to first maximize capability then align the model to
  product usage patterns by reducing latency."
- **Our assessment**: The stated reason for splitting into two phases is the
  more transferable and falsifiable part of this claim: joint optimization
  "tended to converge on local optima: for instance, learning to be
  extremely fast but producing shallow analysis that satisfied the latency
  target but missed real bugs" (per a separate quote captured in Extraction
  Notes). This is a specific, named risk for anyone jointly optimizing a
  correctness reward and a latency/efficiency reward in the same RL pass —
  the model can find a degenerate solution that satisfies the aggregate
  reward while failing the task's actual purpose.

### Claim 6: The latency penalty in the reward function was derived from real dogfooding data — the observed distribution of how long users take to disable SWE-check after invoking it, converted to a CDF used to define the penalty
- **Evidence**: Direct mechanism description: dogfooding data from an early
  internal version was used to build a time-to-disable distribution, whose
  CDF became the basis for a latency-scaled reward penalty.
- **Confidence**: emerging (specific, named mechanism grounded in real usage
  data rather than an arbitrary latency threshold; no numeric detail on the
  actual time-to-disable distribution or penalty formula is disclosed)
- **Quote**: "We then observed the statistical distribution for how long it
  takes users to switch off of SWE-check after invoking it using dogfooding
  data from an early internal version of the SWE-check agent." ... "The CDF
  at a given time tells us what fraction of users would have already moved
  on by then." ... "We then computed the CDF of this distribution and used
  it to define a penalty that scales with estimated latency."
- **Our assessment**: This is the most concrete, reusable technique in the
  post: rather than picking an arbitrary latency budget, the team measured
  actual user tolerance (via a real behavioral signal — disabling the
  feature) and converted that empirical distribution directly into a
  training reward penalty. This is a specific instance of grounding a
  product-quality reward in observed user behavior rather than an assumed
  or negotiated SLA, comparable in spirit to (but a distinct mechanism from)
  Cursor's behavioral-reward and length-penalty design already documented in
  this corpus (see Cross-References → Corroborates).

### Claim 7: SWE-check is explicitly behind frontier on out-of-distribution capability, but its speed and cost advantage still enables an "instant and free" bug-detection experience not possible with frontier models — and Cognition states it expects the OOD gap to shrink with data-pipeline improvements
- **Evidence**: Direct trade-off statement plus a forward-looking
  improvement commitment, both from the introduction/framing of the post.
- **Confidence**: emerging (first-party trade-off framing and forward-
  looking statement of intent; no committed timeline or numeric target is
  given for the promised OOD improvement)
- **Quote**: "While SWE-check is behind the frontier on out-of-distribution
  evals in terms of pure capability, its order of magnitude-faster wall-
  clock runtime and cheaper inference cost enable an instant and free bug
  detection experience not possible with frontier models." ... "We will
  continue to improve this model and expect that additional work on the
  data generation pipeline will allow us to reduce the gap to frontier
  performance on out of distribution evals as well."
- **Our assessment**: This is the source's clearest statement of the
  cost/latency-for-capability trade-off at the center of Claim 1 — SWE-check
  is not claimed to be as capable as Opus 4.6 out-of-distribution, but the
  post argues the speed/cost advantage changes what's economically viable
  (an "instant and free" check on every diff) rather than just making an
  equivalent check cheaper. The OOD-gap-closing commitment is a stated
  intention, not a delivered result, and should be cited as such.

### Claim 8: The post's conclusion frames model specialization as a way to approach frontier performance with a better latency/cost/UX profile aligned to a specific product feature, while explicitly conceding SWE-check "is not categorically the most capable model on this task" despite being "on the Pareto frontier"
- **Evidence**: Direct concluding synthesis statement, summarizing the
  post's five prior technical points (harness-native training, dogfooding-
  driven iteration, reward linearization, two-phase post-training) and then
  explicitly qualifying the result.
- **Confidence**: settled (first-party summary claim that includes a direct
  concession against the vendor's own promotional interest — naming the
  model as not the most capable, only Pareto-optimal)
- **Quote**: "To recap, model specialization is a powerful tool to approach
  frontier performance with a better latency, cost, and user experience
  profile that is deeply aligned with the product feature... There is still
  meaningful room for improvement in the final model – although it is on the
  Pareto frontier, it is not categorically the most capable model on this
  task."
- **Our assessment**: The explicit "not categorically the most capable"
  concession is a stronger candor signal than a typical release-announcement
  conclusion — it directly qualifies the "matches frontier performance"
  framing used earlier in the post (Claim 2), clarifying that "matches" is
  scoped to in-distribution evals and to a Pareto (cost/latency-adjusted)
  comparison, not to an unconditional capability ranking against Opus 4.6.

### Claim 9: A preview of SWE-check is available today in Windsurf Next via the cmd+U shortcut, with general availability in mainstream Windsurf planned "soon" and no committed date
- **Evidence**: Direct availability statement in both the introduction and
  the closing section of the post.
- **Confidence**: settled (a specific, named, currently-live product access
  path — not a forecast or roadmap item)
- **Quote**: "A preview of SWE-check is available in Windsurf Next today and
  will be released in mainstream Windsurf soon." ... "You can try a preview
  of SWE-check today in Windsurf Next using the cmd+U shortcut. It will be
  available in Windsurf soon."
- **Our assessment**: This is a shipped-but-preview-stage feature (Windsurf
  Next, not mainstream Windsurf), consistent with the caveats elsewhere in
  the post (behind on OOD evals, room for improvement) — the guide should
  not treat SWE-check as a fully general-availability feature at the time of
  this post.

## Concrete Artifacts

### Delta-F1 comparison to Opus 4.6 (from the article, verbatim figures)

```
Source: cognition.com/blog/swe-check-10x-faster

In-distribution evals:  delta F1 to Opus 4.6 goes from 0.09 to 0   (matches)
Out-of-distribution evals: delta F1 to Opus 4.6 goes from 0.49 to 0.29
  (meaningful progress, not parity)
```

### Reward design and training pipeline (from the article, verbatim structure)

```
Source: cognition.com/blog/swe-check-10x-faster
Section headings, in order:
1. Introducing SWE-Check: 10x Faster Bug Detection
2. The SWE-check Agent and its requirements
3. Training with production settings
4. How we designed the reward function
   4a. Reward linearization
   4b. Two-phase post-training
5. Conclusion

Reward function design:
- Reward linearization: sample-level reward as a proxy for a
  population-level statistic (hill-climbing target)
- Two-phase post-training:
  Phase 1: maximize task capability
  Phase 2: align to product usage patterns by reducing latency
- Rationale for splitting phases: joint optimization "tended to converge
  on local optima: for instance, learning to be extremely fast but
  producing shallow analysis that satisfied the latency target but
  missed real bugs"
- Latency penalty construction:
  1. Observe dogfooding data: distribution of time-to-disable SWE-check
     after invocation, from an early internal version
  2. Compute the CDF of that distribution ("what fraction of users would
     have already moved on by [a given time]")
  3. Use the CDF to define a penalty that scales with estimated latency
```

### Authorship and byline (verbatim)

```
Source: cognition.com/blog/swe-check-10x-faster

"By Raymond Feng¹, Jeffrey Ling², Rhythm Garg¹, Moritz Stephan²
(¹ Applied Compute, ² Cognition AI) 04.14.26"
```

## Cross-References

- **Corroborates**:
  - `blog-cursor-composer2-technical-report.md` Claim 4 (Composer 2 achieves
    61.3% on CursorBench, competitive with GPT-5.4 (63.9%) and beating Opus
    4.6 High (58.2%), at "cost...similar to smaller or low-effort variants
    of models" — a 25.3-percentage-point net gain from specialization over
    the Kimi K2.5 base) — this source's Claim 1 and Claim 2 (a second,
    independent vendor pair specializing a model via RL to approach frontier
    performance at lower cost/latency, with a disclosed but partial gap on
    harder/OOD conditions) is a second, independent case study of the same
    "specialized model approaches frontier at a cost/latency advantage"
    pattern, for a narrower single-purpose task (bug detection in a diff)
    rather than general-purpose coding.
  - `blog-cursor-composer2-technical-report.md` Claim 2 ("RL training uses
    realistic Cursor sessions with the same tools and harness the deployed
    model uses" — training-environment fidelity as the primary mechanism for
    closing train-test mismatch) — this source's Claim 4 ("we replicated the
    toolset available in the Windsurf harness in the training sandbox") is
    the same environment-fidelity principle, independently named by a second
    vendor pair, applied to a narrower single-agent task rather than a
    general coding agent.
  - `blog-cursor-composer2-technical-report.md` Claim 11 (Composer 2's
    auxiliary behavioral rewards, including "dynamic reward introduction
    monitoring emergent behaviors," to suppress product-quality regressions
    like excessive chain-of-thought in comments) and `blog-cursor-composer-
    2-5.md` Claim 4 (Composer 2.5's behavioral training for communication
    style, explicitly "not well captured by existing benchmarks") — this
    source's Claim 6 (a latency penalty derived directly from observed
    dogfooding time-to-disable behavior) is a third, independent instance of
    a vendor building a reward signal from observed product-usage/behavioral
    data rather than from task-correctness metrics alone — though the
    specific mechanism differs (a CDF-derived latency penalty vs. Cursor's
    auxiliary style/communication rewards).
  - `docs-github-copilot-mai-code-1-flash-more-surfaces.md` Claim 4
    (Microsoft/GitHub's vendor claim that MAI-Code-1-Flash, a 5B-active-
    parameter model, "delivers best-in-class quality for its size,
    outperforming other small models in early testing," with no disclosed
    benchmark methodology) — both sources are vendor claims that a small,
    product-specific model can match or approach larger models on a defined
    task; this source's claim is more specific and falsifiable (named
    delta-F1 figures against a named frontier model, Opus 4.6) than the MAI-
    Code-1-Flash claim (an unquantified "best-in-class for its size" with no
    comparison model list), but both should be read with the same caution:
    vendor-disclosed, unaudited performance claims for a task-specific model.

- **Contradicts**: None identified. No claim in this source conflicts with
  an existing source note's claim under matching conditions.

- **Extends**:
  - `blog-cognition-devin-in-windsurf.md` Claim 2 (Devin "opens PRs, runs
    tests, QAs its own work using computer vision" as part of the cloud-
    agent product definition) — this source names the specific "Semi-Async
    Valley of Death" latency concept (Claim 3 here) that the Devin-in-
    Windsurf note's Extraction Notes flagged as referenced but "not formally
    defined" in a companion Cognition post (`cognition.com/blog/swe-grep`,
    which uses the closely related but not identical term "Semi-Async
    Valley of Death"). This source uses the identical bracketed term "[The
    Semi-Async Valley of Death]" without formally defining it either — the
    term remains an unquantified mental-model heuristic across all three
    Cognition-ecosystem posts that reference it in this corpus, not a
    specified latency threshold in any of them.
  - `blog-cognition-verifying-agentic-development.md` Claim 8 (Cognition
    "experimenting with routing the testing phase to different models" than
    the coding phase, because different task types reward different model
    strengths) — this source's overall thesis (Claim 1) is a more concrete,
    shipped instantiation of that same per-task model-specialization idea:
    rather than routing between existing models by task, Cognition and
    Applied Compute RL-trained a dedicated model for one specific task (bug
    detection) instead. The prior source hedges as an active experiment;
    this source describes a shipped (preview) result of pursuing that
    direction further.

- **Novel**: This is the first source in this corpus documenting a joint
  RL-training partnership between an agent-product company (Cognition) and
  a model-training company (Applied Compute) to produce a narrowly-scoped,
  single-task specialized model. The two named technical mechanisms — reward
  linearization (a sample-level proxy for a population-level hill-climbing
  target) and a dogfooding-derived CDF latency penalty (Claim 6) — are new
  to this corpus; no existing source note documents deriving an RL latency
  penalty directly from observed user disable-behavior data. The explicit,
  numeric delta-F1-to-a-named-frontier-model framing (0.09→0 in-distribution,
  0.49→0.29 out-of-distribution) is also a more quantified specialization
  case study than the qualitative "outperforming other small models" vendor
  language seen elsewhere in the corpus (see Cross-References →
  Corroborates).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claim 4 (training-sandbox
  fidelity to the production Windsurf harness) and Claim 6 (the dogfooding-
  derived CDF latency penalty) as a second, independently-sourced case study
  for the environment-fidelity and behavior-grounded-reward principles
  already anchored by `blog-cursor-composer2-technical-report.md`. The
  specific, reusable technique worth naming explicitly is Claim 6's
  mechanism: measure real user tolerance behavior (time-to-disable) and
  convert its empirical CDF directly into a reward penalty, rather than
  picking an arbitrary latency SLA.
- **Chapter 02 (Harness Engineering) / Chapter 05 (Team Adoption — model
  selection)**: Add Claim 1 and Claim 2 as a concrete instance of the "when
  to specialize a small model vs. use a frontier generalist" decision,
  specifically for narrow, well-scoped tasks (bug detection on a diff) — but
  flag Claim 8's own concession (not categorically the most capable model,
  only Pareto-optimal) and Claim 7 (explicit OOD capability gap) so the
  guide does not overstate parity with frontier models.
- **Chapter 03 (Verification)**: If the guide discusses bug-detection or
  diff-review tooling, add this source as a case study of a dedicated,
  fast, low-cost bug-detection pass distinct from a full frontier-model code
  review — citing the "instant and free" framing (Claim 7) as the intended
  use case (a cheap, always-on check) rather than a replacement for deeper,
  slower frontier-model review.
- **Chapter 04 (Context Engineering)**: Add Claim 5 (two-phase post-training
  to avoid a joint-optimization local optimum where the model learned to be
  "extremely fast but produc[e] shallow analysis") as a specific, named risk
  for any team jointly training a correctness reward and a latency/
  efficiency reward in a single RL pass — the fix demonstrated here is
  sequencing (capability first, then latency alignment) rather than a single
  combined objective.

## Extraction Notes

- The article was fetched via WebFetch, which — consistent with the
  verbatim-extraction difficulty already documented in several other
  Cognition/Cursor source notes in this corpus (e.g. `blog-cognition-
  verifying-agentic-development.md`, `blog-cognition-devin-in-windsurf.md`)
  — initially refused a "reproduce the entire article verbatim" request,
  citing an internal ~125-character quote-length constraint and a copyright
  concern. All quotes above were obtained through five subsequent, narrowly-
  scoped follow-up fetches, each requesting exact, character-for-character
  sentences for a specific topic or section (opening thesis/delta-F1
  figures; section headings and the reward-function-design paragraph;
  training-sandbox/dataset paragraph; dogfooding time-to-disable and OOD-gap
  paragraphs; agent-requirements and conclusion paragraphs; pricing/
  authorship/availability). Section headings were independently confirmed
  via a dedicated fetch listing them in order, and each quote was
  cross-checked against the section it was attributed to. No sub-pages were
  followed — the article does not link out to other substantive Cognition
  or Applied Compute posts beyond site navigation.
- The post does not disclose SWE-check's parameter count, base model
  identity, absolute F1/accuracy scores (only deltas to Opus 4.6), eval set
  size or composition, false-positive rate, or pricing — these gaps are
  reflected in the `confidence_overall: emerging` rating and flagged
  throughout the Extracted Claims and Source Context above.
- No contradiction meeting the MINER.md §4a filing bar was identified. This
  source corroborates and extends existing claims in this corpus about
  model specialization, environment-fidelity training, and behavior-grounded
  reward design, but does not oppose any existing source note's claim under
  matching conditions. No contradiction issue filed.
- Cross-references verified before writing: re-read `blog-cursor-
  composer2-technical-report.md` in full and confirmed Claims 2, 4, and 11
  by number and content; re-read `blog-cursor-composer-2-5.md` in full and
  confirmed Claim 4 by number and content; re-read `docs-github-copilot-
  mai-code-1-flash-more-surfaces.md` in full and confirmed Claim 4 by number
  and content; re-read `blog-cognition-devin-in-windsurf.md` in full and
  confirmed Claim 2 and its Extraction Notes' "Semi-Async Valley of Death"
  discussion by content; re-read `blog-cognition-verifying-agentic-
  development.md` in full and confirmed Claim 8 by number and content. No
  claim number was guessed or approximated.
- The three Prospector triage comments on the source issue (#1970) appear to
  be from repeated/duplicate triage runs and use inconsistent chapter-
  numbering language; this note's Guide Impact section cites the guide's
  actual chapter file names as read directly from the `guide/` directory
  (`02-harness-engineering.md`, `03-verification.md`,
  `04-context-engineering.md`, `05-team-adoption.md`), not the numbering
  used in any of the three triage comments.
