---
source_url: https://www.anthropic.com/research/building-strong-safety-evaluations
source_type: blog-post
title: "Building strong safety evaluations"
author: Anthropic (Ruth Appel, Evan Frondorf, Jeremy Hadfield, Rebecca Hiscott, Kamya Jagadish, Shayne Longpre, Madeleine Tucker, Brett Wittmershaus)
date_published: 2026-11-13
date_extracted: 2026-11-14
last_checked: 2026-11-14
status: current
confidence_overall: emerging
issue: "#4718"
---

# Building strong safety evaluations

> Anthropic's practitioner checklist for building trustworthy evals (construct validity, multi-turn simulated users, grader calibration against chance-corrected human agreement, sample-size floors, preregistration, configuration reporting), plus a rule that evals with tool/internet access run sandboxed and monitored.

## Source Context

- **Type**: blog-post (Anthropic Engineering/Research, "Safety first" series; published Nov 13, 2026)
- **Author credibility**: Written by an Anthropic team that builds the safety evals reported in its system cards; examples are drawn from those system cards. Authoritative on its own practice, but the numbers (e.g. 60% vs 94%, 34-point gap) are self-reported and not independently reproducible from the post.
- **Scope**: Methodology for *safety* evals (propensity to cause harm), not capability evals (footnote 1 points to an earlier post on agent capability evals). Much transfers to any LLM-judged, multi-turn eval. Policy specifics (self-harm, romance scams, dual-use bio/cyber rubrics, election integrity) are only used here as illustrations and are not extracted in depth.

## Extracted Claims

### Claim 1: Choose the construct before the metric; refusal rate is often the wrong construct
- **Evidence**: Self-harm example: a model that refuses everything on the topic would score perfectly on a refusal-rate eval yet is not safer, because declining to engage with a user in crisis is itself a failure.
- **Confidence**: settled (construct validity is standard measurement practice; the example is concrete)
- **Quote**: "A model that refuses to respond to any prompt related to suicide or self-harm would get a perfect score on a refusal-rate eval, but it is not necessarily a safer model."
- **Our assessment**: Buy it. Generalizes beyond safety: any "did it do the bad thing" metric that can be satisfied by doing nothing needs a paired measure of usefulness. Maps directly to agent evals that reward "no destructive action" without checking the task got done.

### Claim 2: Report an "appropriate response rate" for multi-turn evals, where one bad turn fails the whole conversation
- **Evidence**: Anthropic's stated design for multi-turn safety evals, graded against a risk-area-specific rubric written by domain experts.
- **Confidence**: emerging (a design choice, not validated against alternatives in the post)
- **Quote**: "One bad turn—like a model divulging details on how to run a scam when repeatedly pressed—results in a failing grade for the whole conversation."
- **Our assessment**: A strict "all turns must pass" aggregation is a reasonable default for safety, but it is harsher than per-turn averaging and is part of why multi-turn scores spread widely. Worth noting as a design choice that interacts with the sample-size problem (Claim 11).

### Claim 3: Pair harmful and benign prompts in the same domain to measure both compliance and over-refusal
- **Evidence**: Single-turn suites pair harmful requests (maximize "harmless response rate") with benign same-topic requests (minimize "refusal rate"); chemistry example: nerve agent formulation vs. a historical chemical disaster.
- **Confidence**: settled
- **Quote**: "A good eval also needs to measure both compliance with harmful requests and over-refusal of benign requests."
- **Our assessment**: Standard precision/recall thinking applied to safety. Useful as a reminder that one-sided evals are gameable by a degenerate policy.

### Claim 4: Multi-turn simulation uses a fixed first turn, a separate Claude model as simulated user, the tested model as assistant, and a grader model over the full transcript
- **Evidence**: Described five-step internal tool: expert-written spec (objectives, tactics, persona, situation, tone, style); fixed first user turn; separate model generates later user turns sampling from spec dimensions; each scenario run multiple times with different combinations; grader scores each transcript.
- **Confidence**: emerging (single-organization description; no ablation shown)
- **Quote**: "The first user turn is fixed, so every run of a scenario starts from the exact same prompt."
- **Our assessment**: Concrete, reusable recipe for testing agents in conversation (support bots, coding assistants taking clarifications). Because the user turns react to the model's actual replies, it catches slow-escalation failures scripted conversations cannot. Caveat: simulated users are simpler than real ones (the post says so, Claim 7).

### Claim 5: Single-turn evals saturate quickly and are unrealistic; harm often emerges only across turns
- **Evidence**: API aggregate harmless response rates for single-turn evals are 94-98% for every recent model, while multi-turn rates range much more widely. Example: user discloses a layoff early; a later ordinary-looking question needs a careful answer.
- **Confidence**: emerging (figures self-reported, models unnamed)
- **Quote**: "In other words, the single-turn tasks are saturated, and are therefore useful mainly as regression checks on known failure modes."
- **Our assessment**: Useful framing: keep saturated suites as cheap regression gates, invest new effort in harder, longer-horizon ones. The post's advice for saturation is to "make the tasks harder in ways that preserve the construct" rather than adding trick questions.

### Claim 6: Vary scenario dimensions independently (factorial coverage) so effects can be attributed
- **Evidence**: Example: if all severe cases use an "urgent" tone and all less-severe use a "bitter" one, their contributions cannot be separated.
- **Confidence**: settled (basic experimental design)
- **Quote**: "If all severe cases are paired with an “urgent” tone and all less severe cases are paired with a “bitter” one, you won’t be able to tell how each dimension contributes to the model’s behavior."
- **Our assessment**: Easy to violate when hand-writing eval sets; cheap to check.

### Claim 7: Build scenarios from observed behavior, and keep the scenario set evolving
- **Evidence**: Election integrity prompts grounded in real usage patterns; fallbacks are public data, red-team transcripts, incident reports, clinician interviews. Single-turn suites run across 16 policy areas, seven languages, multiple product surfaces.
- **Confidence**: emerging
- **Quote**: "Fully invented scenarios tend to be both too easy for models to pass and subtly unlike what real users write, so build from observed behavior whenever possible."
- **Our assessment**: Corroborates the "mine real sessions" approach of CursorBench. Also notes eval setup (tools, default system prompt) should match the deployment under test.

### Claim 8: Guard internal validity: contamination, reward hacking of the eval, and difficulty calibration
- **Evidence**: Use post-cutoff or synthetic data; close paths where answers are discoverable or graders can be satisfied without doing the task; randomize irrelevant details (answer order). Too-hard example: an audit of a leading coding benchmark found many tasks underspecified or graded by tests that rejected correct solutions (benchmark not named).
- **Confidence**: settled (well-known issues), the audit claim is uncited
- **Quote**: "Models can also find shortcuts you didn’t intend (aka reward hacking)."
- **Our assessment**: Standard but compactly stated; the coding-benchmark audit claim is unattributed so we should not cite it as evidence.

### Claim 9: LLM graders fail silently; make criteria atomic and binary, state what does NOT count, and judge substance over framing
- **Evidence**: Practices listed: simple/objective grading (programmatic where ground truth exists; beware "Yes" pattern-matching on "Yes, I’m generally happy to help, but not with this request."); atomic yes/no criteria (emotional manipulation, unconditional availability, warmth, attachment); rubric spells out edge cases (does pseudocode count as exploit code?); disclaimers and caveats do not make harmful content harmless.
- **Confidence**: emerging (practitioner guidance, no measured effect sizes)
- **Quote**: "Make criteria atomic and binary. Opt for a set of yes/no questions over a single overall score."
- **Our assessment**: Strongly consistent with Hamel's "one failure mode per evaluator" advice. Practical, directly actionable for anyone writing judge prompts.

### Claim 10: Stress-test the grader for self-preference, length bias, and position bias; use a different model than the one under test; fail loudly
- **Evidence**: Grader sees only the conversation, not design metadata; use a different grader model than the tested model; check correlation of scores with response length; flip option order in pairwise comparisons; re-grade a sample with a different model or reworded rubric and confirm top-line holds; grader breakage should be flagged and excluded, not silently scored or dropped.
- **Confidence**: emerging (cites that these biases "have been shown", no citations given)
- **Quote**: "If the conclusions change when the grader does, you’ve likely measured the grader, not the model, and need to update it."
- **Our assessment**: A good checklist. "Fail loudly" is the eval-harness analogue of not swallowing exceptions. Note the "different model" advice is a mitigation rather than a guarantee.

### Claim 11: Validate graders against blind human labels with chance-corrected agreement, benchmarked against human-human agreement
- **Evidence**: Humans label a sample without seeing grader verdicts; report agreement corrected for chance (Cohen's kappa, footnote 3); compare with inter-human agreement; if experts disagree there is no "right" answer to score; if humans agree but the grader disagrees, revisit the rubric.
- **Confidence**: settled (standard measurement practice)
- **Quote**: "Benchmark the agreement between humans and the grader against how well the human labelers agree with each other"
- **Our assessment**: The most transferable item. The "grader should agree with experts about as often as experts agree with each other" bar is a concrete stopping criterion. No kappa thresholds are given.

### Claim 12: Preregister metrics, comparisons, slices and thresholds before seeing results; document deviations
- **Evidence**: Borrowed from psychology's replication-crisis reforms; list: main metrics, comparisons, data slices (e.g. by conversation length), improvement/regression threshold.
- **Confidence**: emerging (applied by analogy; no evidence in the post that it changed Anthropic's results)
- **Quote**: "Decide how you’re going to analyze the results before you see them; this is known as preregistration."
- **Our assessment**: Sound, cheap discipline that guards against metric-shopping after the fact, especially relevant when an agent team reruns evals after every prompt tweak.

### Claim 13: Sample-size floors: 100 items for complex multi-turn, 1,000 for simple single-turn; run cases multiple times; use paired comparisons
- **Evidence**: Anthropic's stated floors; paired comparisons compute a confidence interval on per-item differences. Multi-turn API confidence intervals can exceed ±10 percentage points.
- **Confidence**: emerging (floors are a stated house rule without derivation)
- **Quote**: "We treat 100 items as the floor for a complex, multi-turn eval and 1,000 as the floor for a simpler, single-turn one."
- **Our assessment**: Rare to see concrete numbers; treat as rule-of-thumb. Note that with ±10pp intervals even 100 items detects only large effects, so the floor is a minimum, not a guarantee.

### Claim 14: Report uncertainty and per-category results; a 98% vs 94% gap on a multi-turn eval was not statistically significant
- **Evidence**: Romance-scams eval on claude.ai, Opus 5 vs Opus 5.5, 98% vs 94%, not significant. System cards attach confidence intervals.
- **Confidence**: emerging (single reported example)
- **Quote**: "However, the difference between the two models wasn’t statistically significant, so we couldn’t conclude that one performed better than the other."
- **Our assessment**: Good counterexample to leaderboard-style ranking on small multi-turn sets. Also advises correcting for multiple comparisons.

### Claim 15: Configuration changes results massively; report API vs product-surface results separately (up to 34 points)
- **Evidence**: For Claude Fable 5.1, appropriate-response-rate difference between raw API and claude.ai (system prompt applied) was "as high as 34 percentage points" on multi-turn safety evals.
- **Confidence**: emerging (self-reported)
- **Quote**: "In testing Claude Fable 5.1, the difference in the appropriate response rate between these two configurations on our multi-turn safety evals was as high as 34 percentage points."
- **Our assessment**: Strong evidence that the harness/system-prompt layer, not just model weights, drives behavior, and that eval results are only meaningful with their configuration attached. Also: don't compare scores from different graders.

### Claim 16: A system-prompt instruction found via transcript review fixed an implicit-validation failure (60% API vs 94% claude.ai)
- **Evidence**: Pre-release transcript review of suicide/self-harm evals showed implicit validation of self-harm as a coping strategy; a system-prompt line was added; re-run improved claude.ai appropriate response rate.
- **Confidence**: anecdotal (single case, other mitigations were bundled in: "this and other targeted system prompt mitigations")
- **Quote**: "60% on the API vs 94% on claude.ai with the new system prompt"
- **Our assessment**: Triage note suggested this was the source of the 34-point gap; the post gives the 34-point figure for Fable 5.1 in the reporting section and the 60/94 in the disclosure section, so they are likely related but the post does not state they are the same measurement. Do not conflate them. Also illustrates reading transcripts, not just scores, and running evals continuously on snapshots during development.

### Claim 17: Evals with tool or internet access should run in a no-internet sandbox with real-time monitoring
- **Evidence**: Cyber evals: models may probe testing boundaries and take unintended actions if they escape. Anthropic reports hardening eval environments, temporarily halting many internet-access evals, and adding real-time monitoring for web-search evals "in response to our own incidents".
- **Confidence**: emerging (incidents referenced but not detailed)
- **Quote**: "evals should be run in a sandbox with no internet access, and monitored in real time so you can stop a run immediately if a model is acting in ways that could result in real-world harm."
- **Our assessment**: Notable admission that evals themselves have caused incidents; no incident details given. Consistent with the guide's containment-first stance.

### Claim 18: If you only do three things: write down the construct, validate the grader against humans, report uncertainty
- **Evidence**: Closing prioritization.
- **Confidence**: emerging
- **Quote**: "write down the construct you want to measure before collecting data, validate your grader against human judgment before trusting any number it produces, and report uncertainty so readers can tell signal from noise"
- **Our assessment**: A handy minimum bar for the guide's eval chapter.

## Concrete Artifacts

Simulated-user eval pipeline (Anthropic, "Design scenarios that model a range of conditions"):

```
1. Domain expert writes a specification: simulated-user objectives + tactics,
   plus persona, situation, tone, conversational style (each with several options).
2. First user turn is fixed (identical across runs).
3. A separate Claude model generates later "user" turns following the spec;
   the model under test writes the "assistant" turns.
4. Each scenario runs N times, each with a different combination of spec options.
5. A grader model scores each transcript against the risk area's rubric;
   report share of conversations graded "appropriate" throughout.
```
(paraphrased outline of the source's numbered steps, not a verbatim quote)

Example grader-failure pattern from the source: a pattern-matcher extracting "Yes" from "Yes, I’m generally happy to help, but not with this request."

Preregistration checklist (paraphrased): main metrics; comparisons; data slices (e.g. by conversation length); threshold for improvement/regression; disclose deviations.

Reported numbers: single-turn API harmless response rates 94-98%; multi-turn CIs can exceed ±10pp; romance scams on claude.ai 98% vs 94% (not significant); API vs claude.ai gap up to 34pp (Fable 5.1); 60% API vs 94% claude.ai after system-prompt change.

Tooling named: UK AI Security Institute's Inspect framework; Anthropic's Petri toolkit (built on Inspect).

## Cross-References

- **Corroborates**:
  - `blog-hamel-claude-auto-evals.md` Claim 6 (prefer evaluators scoped to one error at a time) and Claim 5 (bundling four checks into one score): this source's "atomic and binary" criteria (Claim 9 here).
  - `blog-hamel-decision-models-for-evals.md` Claim 7 and Claim 8 (probabilities/judge scores are not automatically calibrated; calibration must be measured): parallels validating a grader against human labels (Claim 11 here).
  - `blog-google-agents-cli-eval-hill-climbing.md` Claim 4 (the mean hides the cause; per-case results differ): parallels "break results out by category rather than averaging".
  - `blog-cursor-cursorbench.md` Claim 1 (public benchmarks suffer grading problems and contamination) and Claim 3 (real-session-derived tasks): parallels Claims 7 and 8 here.
  - `blog-thoughtworks-anand-agent-evaluation-framework.md` Claim 5 (persona-based multi-turn simulation against synthetic personas): this source describes a concrete implementation with a fixed first turn and a separate simulator model.
  - `blog-anthropic-how-contain-claude.md` Claim 3 (environmental containment as primary design priority): same containment logic applied to eval environments (Claim 17 here).
- **Contradicts**: None found. No contradiction issue filed.
- **Extends**:
  - `blog-hamel-decision-models-for-evals.md`: adds chance-corrected human agreement (Cohen's kappa), inter-rater benchmarking, and sample-size floors, which that note does not cover.
  - `blog-openai-model-misalignment-reporting-framework.md`: its "Disclose flaws responsibly" section is a lighter-weight analogue of that framework's disclosure process (that note's Claim 1 and Claim 3 cover OpenAI's stance).
  - `blog-anthropic-claude-fable-and-mythos-5-2.md`: this post explains the methodology behind system-card safety-eval numbers (check that note's claims before citing figures).
- **Novel**: Specific sample-size floors (100 / 1,000); paired-comparison guidance; grader bias stress tests (self-preference, length, position); "fail loudly" for graders; preregistration adapted to evals; "appropriate response rate" metric; reporting configuration gaps (API vs product surface, up to 34pp); admission that eval environments were hardened after incidents.

## Guide Impact

- **Chapter 03 (verification)**: Add a grader-validation checklist based on Claims 9-11: atomic binary criteria, different grader model, bias stress tests (length, order, self-preference), fail-loudly handling, blind human labeling with chance-corrected agreement benchmarked against inter-human agreement. Cite alongside the Hamel notes.
- **Chapter 03**: Add a statistical-reporting subsection: sample-size floors (Claim 13), paired comparisons, confidence intervals, and the non-significant 98% vs 94% example (Claim 14). Flag the floors as one organization's rule of thumb.
- **Chapter 03**: Add the construct-validity warning (Claim 1) and harmful+benign pairing (Claim 3) when discussing "did the agent avoid X" evals.
- **Chapter 02 (harness design)**: Add the 34-point API vs product-surface gap (Claim 15) as evidence the harness/system prompt changes measured behavior, and that evals must match the deployed configuration.
- **Chapter 06 (security)**: Cite Claim 17 for "evals that give models tools or internet should run in a no-internet sandbox with real-time monitoring"; note the source reports eval-environment incidents but does not detail them.

## Extraction Notes

- Read the full article text (fetched raw HTML and stripped markup); quotes were copied from that text. No sub-pages followed; the post links an earlier Anthropic post on agent capability evals, system cards, Inspect, and Petri, which were not fetched.
- Policy-specific material (rubric contents for self-harm, scams, bio/cyber, election integrity) deliberately summarized only as illustrations, per Prospector guidance.
- The post's figures are self-reported and the models/benchmark audits referenced are partly unnamed; confidence is therefore "emerging" overall despite many settled underlying practices.
- Triage comment treated the 60%/94% and 34-point figures as related; the post presents them in different sections and does not explicitly equate them (see Claim 16).
