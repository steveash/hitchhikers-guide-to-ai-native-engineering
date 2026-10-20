---
source_url: https://hamel.dev/blog/posts/decision-model-evals/
source_type: blog-post
title: "How To Use Decision Models for Evals"
author: Hamel Husain, Antaripa Saha
date_published: 2026-10-20
date_extracted: 2026-10-20
last_checked: 2026-10-20
status: current
confidence_overall: emerging
issue: "#4230"
---

# How To Use Decision Models for Evals

> The first tracked source that measures, on labeled data, how tuning a decision model's threshold and calibrating its scores changes model selection and whether scores can serve as confidence estimates.

## Source Context

- **Type**: blog-post
- **Author credibility**: Hamel Husain is a well-known applied-AI/evals practitioner (trusted feed `hamel-husain`); co-author Antaripa Saha. The post publishes methodology, reusable prompts, and per-split audit details in its footnotes. The vendor numbers come from one small private dataset.
- **Scope**: Compares Jev 1.13, Perplexity Decider 1.1 27B, Liquid d1 / d1-ultra, Cloudflare Clef Flash and OpenAI Decisions (GPT-6 Luna) on one binary failure-detection task (98 scored traces from an apartment-leasing agent; 61 known failures, 37 without a labeled failure). Covers threshold tuning, precision/recall floors, cost vs. F1, and Platt-scaling calibration. Does not cover latency comparisons (footnote only), per-failure-mode judges, or other tasks. The original conversations are private, so results cannot be reproduced.

## Extracted Claims

### Claim 1: The default 0.50 decision threshold is often used unexamined and can leave performance on the table
- **Evidence**: Thought experiment (failures scored 0.40, passes 0.10: perfect at 0.30, catches nothing at 0.50) plus the measured gains from tuning in the experiment. The charts are not reproduced here, and the text gives no per-model default-vs-tuned F1 table.
- **Confidence**: emerging
- **Quote**: "We’ve also noticed people using the default decision threshold of 0.50 without checking whether it works well for their task. This can leave a lot of performance on the table."
- **Our assessment**: Standard classifier practice, but worth stating for decision models because the APIs hide the threshold behind a boolean. The authors' observation is anecdotal; the post gives no count of how many people do this.

### Claim 2: Set precision and recall minimums as a go/no-go gate before optimizing F1
- **Evidence**: Applied to the dataset: Perplexity, Liquid d1-ultra and OpenAI Decisions met 80%/80%; Liquid d1 and Clef Flash fell below the minimums even after tuning.
- **Confidence**: emerging
- **Quote**: "It’s also important not to blindly maximize F1 without thinking about your minimum requirements for the classifier to be useful."
- **Our assessment**: Sensible. The 80% floor is the author's choice for an alerting use case, not a general rule. The post itself says the minimums "do not guarantee the same performance on new examples" (footnote 9 paraphrase; see Concrete Artifacts for the fallback-split counts).

### Claim 3: Tune the threshold with cross-validation on saved scores, no new model calls needed
- **Evidence**: Stratified five-fold CV; thresholds chosen on training splits, metrics measured on held-out splits; same splits for all models. A reusable coding-agent prompt is given. In 36 of 100 training splits for Perplexity and 29 for Liquid d1-ultra no threshold satisfied both minimums, and the fallback was the unconstrained F1 optimum (never for OpenAI).
- **Confidence**: emerging
- **Quote**: "With labeled traces and saved model scores, you can ask a coding agent to tune the thresholds."
- **Our assessment**: Practical and cheap. The infeasible-split rates show that an 80%/80% floor is fragile with ~98 traces; the prompt wisely says to report infeasibility rather than relax the requirement, but the experiment itself fell back to unconstrained tuning for those splits.

### Claim 4: Tuning can change which model is viable, and weaker candidates gain more from tuning
- **Evidence**: Candidate models gained less from F1 tuning than Liquid d1 and Clef Flash, but the latter two still fell below minimums.
- **Confidence**: emerging
- **Quote**: "Our candidate models gained less from F1 tuning than Liquid d1 and Clef Flash, which fell below our minimums."
- **Our assessment**: Tuning rescues borderline models but did not rescue anyone past the floor here, so the triage framing "rescue or sink" is only half supported: it sank/kept them, no model was shown to be rescued above the floor. Treat as one benchmark.

### Claim 5: F1 weights precision and recall equally, which rarely matches business needs; choose the tradeoff deliberately
- **Evidence**: Reasoning plus examples (criminal trials favor precision; cancer screening favors recall); F-beta suggested as alternative.
- **Confidence**: settled
- **Quote**: "Be intentional, don’t just use F1 score because this post did!"
- **Our assessment**: Agree; textbook ML evaluation, and the authors acknowledge that.

### Claim 6: Cost vs. F1 shows a real tradeoff: the best model costs about 4.5x the cheapest viable one
- **Evidence**: Perplexity 0.82 cents per 100 eval runs at F1 0.79; OpenAI Decisions 3.72 cents at F1 0.87. Liquid d1-ultra is a lower-cost, lower-performance option. Costs are from token usage and provider prices (Liquid repriced as of October 17, 2026).
- **Confidence**: emerging
- **Quote**: "Perplexity was the cheapest of these candidates at 0.82 cents per 100 eval runs, with an F1 of 0.79. OpenAI Decisions reached an F1 of 0.87 at 3.72 cents per 100 eval runs, about 4.5 times the cost."
- **Our assessment**: Concrete numbers, but one 98-trace dataset and a deliberately broad task. The authors warn model performance "varies substantially across tasks and datasets". Do not present as a general ranking.

### Claim 7: Decision-model probabilities are not automatically calibrated; check before treating scores as confidence
- **Evidence**: Reliability plots in five bins of 19-20 traces. Perplexity, Liquid d1 and Clef Flash moved closer to the diagonal after Platt scaling; Jev and Liquid d1-ultra were already well calibrated. One Clef Flash bin averaged ~8% predicted failure probability but had 60% failures.
- **Confidence**: emerging
- **Quote**: "For example, one group of Clef Flash traces had an average predicted failure probability of about 8%, but 60% contained failures."
- **Our assessment**: Important for probability-band designs (act above 0.9, escalate below 0.6) that assume scores are literal probabilities. Caveat: bins of ~20 traces are a very noisy estimate; the authors say the chart "does not establish an exact failure rate for a future trace".

### Claim 8: Calibration must be measured, not assumed: Platt scaling made OpenAI's probabilities slightly worse
- **Evidence**: Brier scores (lower is better): Jev 0.187 to 0.188; Liquid d1-ultra 0.173 to 0.172; OpenAI 0.159 to 0.164. An exploratory refit directly on probabilities gave OpenAI 0.154, so the result is sensitive to the fitting method.
- **Confidence**: emerging
- **Quote**: "Platt scaling isn’t always the best fit. For example, OpenAI’s probabilities got slightly worse with the version of Platt scaling we used."
- **Our assessment**: The deltas for Jev and d1-ultra are within noise (0.001); only OpenAI's worsening is notable, and the footnote shows it is method-dependent. The takeaway "measure, don't assume" holds; "Platt scaling hurts OpenAI" does not generalize.

### Claim 9: Scope each judge to one failure mode; narrower tasks should shrink model gaps; start large then try smaller models
- **Evidence**: Author recommendation ("we expect"), not tested here: the eval task was kept broad deliberately. A small manual Jev experiment raised default-threshold F1 from 0.78 to 0.80 with a checklist of failure types; the authors say this does not establish how much systematic prompt optimization would help.
- **Confidence**: anecdotal
- **Quote**: "I like to start with a larger model that has acceptable performance on a task and then try smaller models to see if they can match the larger model’s performance for less cost."
- **Our assessment**: Consistent with the same author's earlier advice on single-error evaluators. The gap-shrinking expectation is untested in this post.

### Claim 10: Recommended workflow: fix the judge prompt, rule out by floors, tune thresholds, then weigh cost and latency; iterate
- **Evidence**: The post's four-step recap; the process is explicitly iterative since prompt changes require re-tuning and re-calibrating.
- **Confidence**: emerging
- **Quote**: "Tune each model’s decision threshold before comparing performance."
- **Our assessment**: Good ordering: comparing untuned models can mis-rank them. Missing: held-out test set sizing guidance beyond a footnote on GEPA suggesting a separate test set outside prompt development.

### Claim 11: Decision models match LLMs on classification/routing at lower cost, but harder eval tasks may justify an LLM
- **Evidence**: OpenAI Decisions (backed by GPT-6 Luna) had the highest F1 at the highest cost; the post cites Randy Olson's broader comparison (not verified by us).
- **Confidence**: anecdotal
- **Quote**: "OpenAI Decisions uses GPT-6 Luna, which delivered our highest F1 at the highest cost, suggesting that harder eval tasks may justify paying more for an LLM."
- **Our assessment**: Reasonable but the inference from one model is thin; OpenAI Decisions is itself an LLM-backed product.

### Claim 12: Threshold tuning and calibration are ordinary classifier evaluation; ML engineers already have the skills
- **Evidence**: Authority/framing; pointer to *Machine Learning with Python Cookbook*, 2nd ed.
- **Confidence**: settled
- **Quote**: "None of the ideas discussed in this post are new."
- **Our assessment**: Correct, and it is the useful framing for the guide: treat decision models as classifiers and apply classifier-evaluation discipline.

## Concrete Artifacts

Threshold-tuning prompt for a coding agent (verbatim, Hamel Husain & Saha, hamel.dev):

```
Using my saved model scores and binary labels (1 means failure), tune a decision threshold to maximize F1 while requiring at least 80% precision and 80% recall. Use stratified five-fold cross-validation, choosing thresholds on the training examples and measuring performance on the remaining examples. If comparing models, use the same splits for each. Only select thresholds that meet both minimums on the training examples. If none qualifies, report that rather than relaxing either requirement. Report validation precision, recall, and F1, along with any splits where no threshold qualified or validation performance fell below my minimums. Compare with the default threshold of 0.50. Reuse the saved scores without making new model calls.
```

Calibration prompt (verbatim):

```
Using my saved failure probabilities and binary labels (1 means failure), test whether Platt scaling improves each model’s probabilities. Use stratified five-fold cross-validation with the same splits for every model. Fit the calibration mapping on each training split and apply it to the remaining traces. Fit on log-odds, clipping probabilities away from 0 and 1 first. Plot predicted probabilities against observed failure rates before and after calibration. Report Brier scores (lower is better), and explain which models improved or got worse. Reuse the saved scores without making new model calls.
```

Metrics reported (hamel.dev post, text and footnotes):

```
Dataset: 98 scored traces (100 minus 2 internal QA); 61 known failures, 37 without labeled failure
Cost per 100 eval runs / tuned F1: Perplexity 0.82 cents / 0.79; OpenAI Decisions 3.72 cents / 0.87
Mean latency (s), separate runs: Jev 4.33, Perplexity 7.85, Liquid d1 7.38, d1-ultra 1.56, Clef Flash 2.09, OpenAI 2.77
Infeasible 80/80 training splits (of 100): Perplexity 36, Liquid d1-ultra 29, OpenAI 0
Brier before/after Platt: Jev 0.187/0.188; d1-ultra 0.173/0.172; OpenAI 0.159/0.164 (0.154 with direct-probability refit)
```

The appendix also contains the apartment-leasing "any substantive issue" judge prompt and its structured Jev version (`"version": "nurtureboss-any-issue-v1"`, `"type": "noul"`); not reproduced here.

## Cross-References

- **Corroborates**: `blog-simonwillison-jev-decision-models.md` Claim 10 (evals matter more for decision models and are cheap to run): this post supplies a concrete method. `blog-hamel-claude-auto-evals.md` Claim 6 (prefer evaluators scoped to one error at a time) aligns with this post's per-failure-mode judge recommendation; the dataset and broad failure-finding task are shared with Hamel's earlier automated-evals post.
- **Contradicts**: None filed. Tension, not contradiction: `blog-thoughtworks-penumarthi-jev-rag-pipelines.md` Claim 7 proposes fixed probability bands (0.9 / 0.6), which implicitly treat scores as literal probabilities; this post shows scores can be miscalibrated (Clef Flash), though it found Jev well calibrated on its dataset. Context differs (RAG decisions vs. failure detection), so no issue was opened.
- **Extends**: `blog-thoughtworks-penumarthi-jev-rag-pipelines.md` Claim 9 (verify calibration on your own data) with a method and measurements. `blog-latentspace-jev-system-one-for-prod.md` Claim 9 (use calibrated confidence for thresholds and escalation) with evidence on when calibration holds. `blog-thoughtworks-xiong-decision-models-possibility-of-noops.md` Claim 9 (deciding when to involve a human) with a concrete approach to setting the gate threshold.
- **Novel**: Labeled-data measurements of default vs. tuned thresholds, precision/recall floors as a model-selection gate, a cost-vs-F1 comparison across five decision models, Brier-score evidence that Platt scaling can hurt, and reusable coding-agent prompts for both procedures.

## Guide Impact

- **Chapter 03**: In the verification/evals material, add a short subsection on using decision models as automated judges: set precision/recall minimums first, tune threshold with stratified CV on saved scores, and do not use the default 0.50. Cite this note's Claims 1-3 and 10 with the prompt in Concrete Artifacts. Present the cost/F1 numbers as a single illustrative 98-trace benchmark.
- **Chapter 03**: Where the guide discusses confidence thresholds or escalation for classifiers, add the caveat that scores must be checked for calibration (Claims 7-8) before banding; cite the Clef Flash bucket (8% predicted vs. 60% observed) as the example.
- **Chapter 02**: Optional sidebar: decision models as cheap in-loop gates still need threshold tuning against labeled traces (Claim 3); no change to the main recommendation.

## Extraction Notes

- Read the full post text (main body, appendix, and all 14 footnotes) from the raw HTML. Charts are interactive/image-based and could not be read, so figures such as per-model default-vs-tuned F1 are not extracted; only numbers in the text/footnotes are used.
- Did not follow external links (Randy Olson comparison, scikit-learn guides, TypeSafe docs). The Randy Olson claim is reported as the authors' citation only.
- Triage suggested "rescue or sink" framing for tuning; the text only shows Liquid d1 and Clef Flash staying below minimums, so Claim 4 is worded accordingly.
- All quotes were copied verbatim from the fetched page. Cross-reference claim numbers were checked against the headings in the cited notes.
