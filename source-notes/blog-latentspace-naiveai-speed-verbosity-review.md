---
source_url: https://latent.space/p/naiveai/
source_type: blog-post
title: "NaiveAI Promises 2,100 Tokens per Second. How Well Does It Code?"
author: Gabriele Beltramo (Latent Space)
date_published: 2026-11-10
date_extracted: 2026-11-23
last_checked: 2026-11-23
status: current
confidence_overall: anecdotal
issue: "#4911"
---

# NaiveAI Promises 2,100 Tokens per Second. How Well Does It Code?

> A small hands-on review showing that a headline tokens-per-second figure can coexist with a very skewed completion-length distribution (median ~3.2K vs mean >51K tokens), so median latency, mean latency, and token budgets tell different stories for model selection and agent-loop timeouts.

## Source Context

- **Type**: blog-post (hands-on model review; first in a new Latent Space "trying new models and products" series)
- **Author credibility**: Gabriele Beltramo, byline on Latent Space; published code for the verbosity experiment (github.com/gbeltramo/llm-verbosity). Not a lab insider; the post includes a sponsor slot but is framed as an unbiased review.
- **Scope**: Naive-N0.5-Flash (open-weights model derived from Xiaomi MiMo-V2.5, run on the vendor's NaiveRT engine) vs DeepSeek V4.1 Flash 1017 and GLM 5.3 Flash. Covers a speed/verbosity test (30 questions per model) and three one-shot app-build prompts. Does NOT grade answer accuracy, does not test multi-turn agent harnesses, and has no independent benchmark scores for the new model.

## Extracted Claims

### Claim 1: Naive-N0.5-Flash's completion-length distribution is extremely skewed: median ~3,200 tokens vs mean >51,000 with thinking on
- **Evidence**: 30 questions (10 MATH-500, 10 GPQA-Diamond, 10 HLE-Diamond), 256K max completion tokens, same for all models.
- **Confidence**: anecdotal
- **Quote**: "Across all 30 questions, the median completion for Naive-N0.5-Flash with thinking on was about 3,200 tokens, far below its average of more than 51,000."
- **Our assessment**: Plausible and useful: a few runaway reasoning traces dominate token cost. Small sample, so the exact numbers should not be generalized, but the mean-vs-median lesson is sound for budgeting tokens and timeouts.

### Claim 2: The long tail is driven by a small number of very long reasoning traces, and the pattern appears in other models too
- **Evidence**: Same experiment; hard HLE questions averaged ~108,500 completion tokens for Naive (thinking), reported as roughly 9x GLM 5.3 Flash (high) and 11x DeepSeek V4.1 Flash 1017 (high).
- **Confidence**: anecdotal
- **Quote**: "A small number of requests produced exceptionally long reasoning traces and pulled the average up. The same pattern appears, less sharply, in the other models."
- **Our assessment**: Consistent with other reports of verbose reasoning models; see cross-reference to DeepSeek v4.1 verbosity claim.

### Claim 3: Median and mean end-to-end latency rank the models differently
- **Evidence**: Median 3.1s (Naive thinking) vs 5.3s (GLM 5.3 Flash high) vs 10.1s (DeepSeek V4.1 Flash high); means 45.3s, 86.9s (GLM), 45.0s (DeepSeek). On hard questions Naive averaged 89.8s vs DeepSeek's 79.7s.
- **Confidence**: anecdotal
- **Quote**: "The median question took 3.1 seconds with Naive-N0.5-Flash (thinking), against 5.3 seconds for GLM 5.3 Flash (high) and 10.1 seconds for DeepSeek V4.1 Flash 1017 (high)."
- **Our assessment**: The key point is that a "fastest" headline depends on the statistic chosen. The author's own conclusion ("Mean times were similar to DeepSeek V4.1 Flash 1017") undercuts a pure speed-win narrative; the author still concludes it is faster on easy/medium questions.

### Claim 4: Throughput numbers are not apples-to-apples, so no exact speed multiple is claimed
- **Evidence**: Naive's figures are server-side; DeepSeek/GLM figures come from OpenRouter.
- **Confidence**: settled (as a methodological caveat stated by the author)
- **Quote**: "Because its figures are server-side and the other models' figures come from OpenRouter, we do not claim an exact speed multiple over DeepSeek V4.1 Flash 1017 or GLM 5.3 Flash."
- **Our assessment**: Good practice by the author; a general caution for any comparison mixing vendor-measured and third-party-measured throughput.

### Claim 5: The headline 2,100 tokens/s is a one-second peak, achieved with speculative decoding on a custom engine, and sustained speed during thinking is about half that
- **Evidence**: Footnote 1: single eight-GPU Blackwell node, NaiveRT engine plus a FP8 draft model; acceptance rate 70.6% thinking-off vs 43.4% thinking-on; ~984 tok/s in thinking phase, 1,816 tok/s in answer phase; tuned for single-stream latency rather than batch throughput.
- **Confidence**: anecdotal (vendor-reported)
- **Quote**: "Peak rate: roughly 2,100 tokens/s over a single second. Treat this as an upper bound, not a typical rate."
- **Our assessment**: Vendor-reported figures relayed by the author, on hardware most users will not have. Important for discounting the title's number.

### Claim 6: Answer accuracy was not graded, so speed results say nothing about correctness
- **Evidence**: Author's explicit caveat.
- **Confidence**: settled
- **Quote**: "Short, fast replies are only useful if they are correct."
- **Our assessment**: The central limitation. The post's quality conclusion ("holds up against DeepSeek") rests only on three subjectively judged one-shot apps and vendor-reported benchmarks.

### Claim 7: Thinking mode materially affects coding usefulness: with thinking off, Naive failed the tree app entirely
- **Evidence**: One prompt per app per variant; six model/effort combinations.
- **Confidence**: anecdotal
- **Quote**: "The surprise was Naive-N0.5-Flash with thinking switched off, which did not produce a usable app at all."
- **Our assessment**: A single-sample result, but consistent with the idea that fast non-reasoning modes trade away reliability on complex generation.

### Claim 8: In one-shot app builds with thinking on, Naive was competitive with DeepSeek and more consistent than GLM, but not best on code efficiency
- **Evidence**: Three apps (3D solar system, procedural 3D tree, Ray Tracing in One Weekend port), compared qualitatively.
- **Confidence**: anecdotal
- **Quote**: "The Naive-N0.5-Flash (thinking) app is correct, but its JavaScript is less efficient."
- **Our assessment**: Qualitative, n=1 per cell, no rubric. Weak evidence.

### Claim 9: Published benchmarks place the model between the two comparison models, mixed across suites
- **Evidence**: Table from model cards/vendor blogs: NL2Repo-Bench 71.9 (Naive) vs 68.2 (DeepSeek) vs 56.3 (GLM); DeepSWE v1.1 67.8 vs 77.0 vs 63.4; Agent's Last Exam 32.4 vs 35.4 vs 26.3. No Artificial Analysis score yet for Naive.
- **Confidence**: anecdotal (vendor-reported, unverified)
- **Quote**: "They place its coding ability between the two comparison models, and ahead of both on NL2Repo-Bench."
- **Our assessment**: Vendor numbers; do not promote.

### Claim 10: Target pricing is $0.10/M input, $0.40/M output, $0.01/M cache read, but final cost depends on tokens used
- **Evidence**: Vendor-stated target prices; author observes the per-question cost ends up slightly higher due to verbosity.
- **Confidence**: anecdotal
- **Quote**: "The final bill will also depend on how many tokens the model uses."
- **Our assessment**: Reinforces that per-token price is not per-task cost; see the DeepSeek v4.1 note.

## Concrete Artifacts

```
Source: latent.space/p/naiveai, "Speed and verbosity experiments"
Design: 10 MATH-500 (easy) + 10 GPQA-Diamond (medium) + 10 HLE-Diamond (hard) = 30 questions/model
Max completion tokens: 256K (all models). Metrics: TPS, completion tokens, end-to-end time.
Code: https://github.com/gbeltramo/llm-verbosity

Median e2e: Naive (thinking) 3.1s | GLM 5.3 Flash (high) 5.3s | DeepSeek V4.1 Flash 1017 (high) 10.1s
Mean e2e:   Naive 45.3s | DeepSeek 45.0s | GLM 86.9s
Hard (HLE) mean e2e: Naive 89.8s vs DeepSeek 79.7s
Completion tokens (Naive thinking): median ~3.2K, mean >51K; HLE mean ~108.5K
Speculative decoding (footnote 1): acceptance 70.6% thinking-off vs 43.4% thinking-on; ~984 tok/s thinking, 1,816 tok/s answer; ~2,100 tok/s peak over 1s
Spec round time: 3.4 ms (NaiveRT) vs 12.3 ms (SGLang)
```

## Cross-References

- **Corroborates**: `blog-latentspace-ainews-deepseek-v41-flash-encoder-decoder.md` Claim 6 (Artificial Analysis finds DeepSeek v4.1-Flash very verbose, yet cheap per task thanks to low token prices) — both show that token verbosity, not unit price or speed alone, determines real cost/latency.
- **Contradicts**: None filed. The "fast overall" conclusion and the equal mean latency are in tension within the source itself, noted in Claim 3; this is not a cross-source contradiction.
- **Extends**: `blog-fowler-edwardsalexander-refactoring-token-economics.md` (Claim 8 and Claim 11 frame tokens as the economic unit) — this adds the point that reasoning-token variance matters on top of unit price.
- **Novel**: NaiveAI / Naive-N0.5-Flash is not covered elsewhere in the corpus; neither is the median-vs-mean framing for reasoning-token budgets nor the speculative-decoding acceptance-rate explanation for why peak TPS overstates typical TPS.

## Guide Impact

- **Chapter 02**: Optional caution in the model-selection discussion: don't pick models on headline tokens/sec; compare end-to-end latency by median and mean, and note whether throughput is vendor-measured or third-party. Evidence is weak (anecdotal), so frame as a caution rather than a recommendation.
- **Chapter 04**: Possible supporting example that reasoning-token distributions are heavy-tailed (median ~3.2K vs mean >51K), so agent loops should set timeouts/token caps around the tail and budget on means rather than medians. Pair with the DeepSeek v4.1 verbosity claim rather than citing this alone.
- No change recommended to Chapter 00/01 text.

## Extraction Notes

- Read the full article (fetched raw HTML, ~10 min read) including both footnotes; the app-gallery embeds and external NaiveAI blog/GitHub links were not followed, so vendor figures are unverified.
- Triage guidance followed: extracted as a general caution about speed claims, not an endorsement. Sample sizes are tiny (30 questions per model, one prompt per app), accuracy ungraded, and the post contains a sponsor slot.
- Cross-referenced claim numbers were checked against the headings of the cited notes.
