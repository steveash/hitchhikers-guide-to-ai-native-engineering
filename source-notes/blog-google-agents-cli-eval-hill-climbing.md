---
source_url: https://developers.googleblog.com/hill-climbing-agent-quality-with-agents-cli-evaluation/
source_type: blog-post
title: "Hill-Climbing Agent Quality with Agents CLI Evaluation"
author: Pier Paolo Ippolito and Elia Secchi, Google
date_published: 2026-10-28
date_extracted: 2026-10-29
last_checked: 2026-10-29
status: current
confidence_overall: emerging
issue: "#4417"
---

# Hill-Climbing Agent Quality with Agents CLI Evaluation

> A command-level walkthrough of an eval loop (generate, grade, compare, scheduled regression with a threshold exit code) showing that a one-line prompt change can pass lint and unit tests yet drop an LLM-judge mean score, and that the mean alone hides the cause.

## Source Context

- **Type**: blog-post (vendor, Google Developers Blog)
- **Author credibility**: Google product manager and solutions specialist for Agents CLI (same authors as `blog-google-agents-cli-extension-system.md`). They know the tool, but the post promotes it; tool-specific claims (`eval optimize`, GEPA, ADK-only) are vendor claims.
- **Scope**: Covers a 4-case demo on a LangChain-template weather agent with one LLM-as-judge metric (1 to 5), a bad-prompt regression, a model swap, a nightly run, and an alert script. It does not give independent measurements, multiple judges, repeated runs, or larger datasets. Numbers illustrate the method and should not be generalized.

## Extracted Claims

### Claim 1: Eval work is a loop (write cases, run, grade, read failures, change, re-run), and that loop, not the demo, is what makes an agent reliable
- **Evidence**: Author framing; the post's CLI namespace is `eval generate` / `grade` / `compare` / `analyze` / `optimize`.
- **Confidence**: emerging
- **Quote**: "The first takes a weekend; the second takes a loop."
- **Our assessment**: Familiar framing and consistent with the corpus. Useful mostly as the structure of the walkthrough, not as new evidence.

### Claim 2: A one-line system-prompt change can pass lint, unit tests, and type checks while materially degrading behavior, and only an end-to-end LLM-judge eval catches it
- **Evidence**: Demo: pasting an unrelated chef-persona prompt moves the baseline mean from 4.0 (stdev 1.4142) to 2.75 (stdev 0.9574) on 4 cases.
- **Confidence**: anecdotal
- **Quote**: "a chef persona meant for a different codebase"
- **Our assessment**: The failure class (behavioral regression invisible to static checks) is real and plausible. The evidence is a deliberately staged regression on four cases, so it demonstrates detectability, not frequency.

### Claim 3: The regression mechanism was "tool registered but not called": the agent ignored its weather tool and fabricated values
- **Evidence**: Per-case table: `sf_weather` 4.0 → 2.0, `greeting` 5.0 → 4.0, `off_topic` 5.0 → 3.0, `rome_weather` 2.0 → 2.0 (unchanged).
- **Confidence**: anecdotal
- **Quote**: "ignored the weather tool, hallucinated conditions"
- **Our assessment**: A concrete symptom (silent skip of a tool followed by hallucinated output) that traces to a prompt change. Good illustration for verification chapters; the judge could only see the final response, so the diagnosis depends on the post's trace inspection.

### Claim 4: The mean hides the cause: a model swap and the bad prompt produce the same mean drop, but per-case results show different problems
- **Evidence**: Swapping 3.8-flash to 2.5-flash also lands at mean 2.75, but per-case: `greeting` 5.0 → 5.0, `sf_weather` 4.0 → 3.0, `rome_weather` 2.0 → 2.0, `off_topic` 5.0 → 1.0. The drop is concentrated in one out-of-scope case where the cheaper model refused with a hedge.
- **Confidence**: anecdotal
- **Quote**: "the cheaper model refused with a hedge about the event"
- **Our assessment**: This is the most useful point. It argues for per-case diffs (`eval compare`) as the default review view. Caveat: with n=4, one case moves the mean by 1.0, so "concentrated in one case" is nearly guaranteed, and the judge may penalize a refusal that is acceptable behavior.

### Claim 5: A nightly run against a stable regression dataset catches drift from vendor model updates and tool changes
- **Evidence**: Described pattern; no incident data.
- **Confidence**: anecdotal
- **Quote**: "A nightly run against a stable regression dataset catches drift from model updates."
- **Our assessment**: Sensible and matches the ambient-quality material in the corpus. No evidence on how often drift actually occurs.

### Claim 6: A small script can turn eval scores into an alert by exiting non-zero when the mean drop exceeds a threshold
- **Evidence**: `check_score.py` output shown for a regression (exit 1) and a self-compare (exit 0); see Concrete Artifacts.
- **Confidence**: emerging
- **Quote**: "exits non-zero when the drop exceeds a threshold"
- **Our assessment**: Simple, copyable verification practice. The example threshold of 0.1 on a mean over four cases is noise-sensitive; real use needs larger datasets and likely per-case guards (see vibe-check note, Claim 13).

### Claim 7: Automated prompt optimization (`eval optimize`, GEPA) can overfit the metric and needs human review
- **Evidence**: Author warning; ADK-only feature.
- **Confidence**: anecdotal
- **Quote**: "GEPA sometimes finds prompt variants that score higher on the specific metric by overfitting to its wording."
- **Our assessment**: A candid and valuable caveat (Goodhart on the judge). The post gives no example of it happening.

### Claim 8: Practical dataset and result hygiene: start small, snapshot full result files, separate datasets from expectations, distrust summary metrics
- **Evidence**: A list of five lessons at the end of the post.
- **Confidence**: anecdotal
- **Quote**: "Snapshot result files, not scores."
- **Our assessment**: Other lessons in the post are headed "Lead with a small, representative dataset, not a comprehensive one.", "Separate the dataset from its expectations.", "Treat summary metrics with suspicion.", and "More evals do not automatically lead to more fixes." Reasonable, uncontroversial practice advice without supporting data.

## Concrete Artifacts

Commands as shown in the post (Google Developers Blog, 2026-10-28):

```
agents-cli eval generate --dataset tests/eval/datasets/basic-dataset.json \
    -o tests/eval/output/
agents-cli eval grade --traces tests/eval/output/eval_dataset_*.json \
    --config tests/eval/eval_config.yaml

agents-cli eval compare \
    artifacts/grade_results/results_20261003_224516.json \
    artifacts/grade_results/results_20261003_225158.json

agents-cli eval optimize \
    --dataset tests/eval/datasets/regression.json \
    --target-metric final_response_quality \
    --config tests/eval/eval_config.yaml
```

Reported results (post's demo, 4 cases, LLM judge 1 to 5):

```
Baseline:            mean 4.0000, stdev 1.4142
Chef-prompt:         mean 2.7500, stdev 0.9574
  greeting 5.0->4.0, sf_weather 4.0->2.0, rome_weather 2.0->2.0, off_topic 5.0->3.0
Model swap 3.8-flash -> 2.5-flash: mean 4.00 -> 2.75
  greeting 5.0->5.0, sf_weather 4.0->3.0, rome_weather 2.0->2.0, off_topic 5.0->1.0
```

`check_score.py` output as reported:

```
FAIL: mean dropped 4.000 → 2.750 (drop 1.250 > threshold 0.1)
exit: 1

OK: mean 4.000 → 4.000 (drop 0.000 ≤ threshold 0.1)
exit: 0
```

## Cross-References

- **Corroborates**: `blog-google-developers-evaluating-agents-vibe-check.md` Claim 5 (a single top-line score cannot explain a failure) and Claim 13 (CI gate with global threshold plus zero regressions on previously passing metrics); this post's per-case view is a concrete example of that need. `blog-google-aqua-ambient-quality-agent.md` Claim 1 (quality regresses silently while health checks stay green) matches the nightly-drift rationale.
- **Contradicts**: None found. Note a tension in degree only: this post's gate is a mean-drop threshold, while vibe-check Claim 13 recommends also requiring zero per-metric regressions; not filed as a contradiction since the post does not argue against it.
- **Extends**: `blog-google-agents-cli-extension-system.md` (same tool and authors; that note covers the extension system, this one covers the eval namespace). `blog-google-developers-evaluating-agents-vibe-check.md` Claim 6 (change one variable at a time against a frozen dataset) gets a worked example here (prompt change, then model swap).
- **Novel**: A command-level worked example in which one-line prompt change and model swap give identical means (2.75) but different per-case causes; the exit-code threshold script with sample output; the explicit overfitting warning for automated prompt optimization. `blog-anthropic-claude-ai-3x-faster-hill-climbing.md` shares only the "hill-climbing" term (performance work, not eval-driven quality) and is not a close overlap.

## Guide Impact

- **Chapter 03 (verification)**: Add the chef-prompt regression as a worked example that lint, unit tests, and type checks pass while an end-to-end LLM-judge eval fails (mean 4.0 → 2.75), labeled vendor-run, 4 cases, illustrative. Add the same-mean-different-cause model-swap example to support "review per-case diffs, not just the mean."
- **Chapter 03**: Add the exit-code threshold script as a minimal scheduled-regression pattern, with a caution that a 4-case mean is too noisy for a real threshold.
- **Chapter 02 (harness engineering)**: Where prompt and model changes are treated as harness changes, cite this as evidence they should be regression-tested like code, and cite the GEPA caveat when discussing automated prompt optimization.

## Extraction Notes

- The page was read through a fetch tool that returns summaries and short excerpts rather than the full text, so I could not read every paragraph directly. All quoted fragments were returned as verbatim excerpts from the page; the Assayer should spot-check them against the URL. Code, command, and output blocks were transcribed from the same excerpts.
- No sub-pages followed. Cross-reference claim numbers were checked against the headings in the cited notes.
- Publication date 2026-10-28 is from the Prospector triage comment and the page byline.
