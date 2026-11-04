---
source_url: https://developers.googleblog.com/cost-per-task-using-cheap-classifiers-to-route-across-gemini-models-and-thinking-levels/
source_type: blog-post
title: "Cost per task: Using cheap classifiers to route across Gemini models and thinking levels"
author: Sergio Villani (Google Cloud AI)
date_published: 2026-11-03
date_extracted: 2026-11-04
last_checked: 2026-11-04
status: current
confidence_overall: emerging
issue: "#4517"
---

# Cost per task: Using cheap classifiers to route across Gemini models and thinking levels

> A Google-authored 50-task benchmark showing that (a) low thinking level on a single Flash model beats most routing setups, (b) `maxOutputTokens` does not reduce thinking spend, (c) regex/length routers collapse on unseen tasks while an atomic-question classifier holds up, and (d) per-model prompt caching conflicts with per-turn routing.

## Source Context

- **Type**: blog-post (vendor, Google Developers Blog)
- **Author credibility**: Sergio Villani, Technical Solutions, Google Cloud AI. First-party access to Gemini APIs and Antigravity; however the article is vendor-authored and the benchmark code is not yet public ("The benchmark code will be published after open-source review.").
- **Scope**: One benchmark (50 hand-labelled coding-agent prompts, auto-graded) across Gemini 3.8 Flash, Flash-Lite, Pro, a regex heuristic router and a Jev classifier router. Covers routing accuracy, thinking-token behaviour, caching tradeoffs. Does not cover long-context agent turns, multi-turn loops, or non-Gemini models. The article's result tables were images/not extractable as text; numbers below are from the prose only.
- **Caveat**: The article states "Limits: one run per setup, 50 prompts with hand-assigned difficulty and simple automatic grading." It also discloses "Google has no partnership with TypeSafe, and this article is not an endorsement of TypeSafe or its products."

## Extracted Claims

### Claim 1: The governing production metric for coding agents is cost per successful task, not price per token
- **Evidence**: Definition given in the article's opening; no measurement, framing only. The benchmark is then judged on this metric.
- **Confidence**: emerging
- **Quote**: "The dominating metric is now cost per successful task: total spend across every loop iteration, tool call, retry and internal thinking pass divided by the number of tasks that pass verification."
- **Our assessment**: Useful, precise definition (denominator = verified successes). Matches the Anthropic framing but the definition here is more explicit. Note the article's own tests use short single-shot prompts, not full loops, so the metric is argued rather than demonstrated end to end.

### Claim 2: A single broad "simple or complex" Choice question fails as a router; one atomic Noul question works
- **Evidence**: On 16 dev tasks, the broad Choice routed nearly everything to simple (even LRU cache trace, modular exponentiation). Replacing it with one atomic Noul question gave 13/16 agreement with hand labels on the first run and 14/16 on the second pass.
- **Confidence**: anecdotal
- **Quote**: "If a question weighs multiple factors or requires a meta-judgment, decompose it into an atomic check."
- **Our assessment**: Plausible and consistent with general LLM-as-classifier practice; n=16 is small. The attribution of the guidance is to TypeSafe's documentation, not Google's own measurement.

### Claim 3: A frozen regex and prompt-length heuristic router overfits its dev set and collapses on unseen agent tasks
- **Evidence**: Heuristic scored 15/16 (93.8%) on the 16 dev questions used to write it; code frozen and tested on 34 held-out tasks across seven buckets: 70.6% (a drop of 23.2 points). Jev scored 34/34 on held-out; 48/50 (96.0%) overall.
- **Confidence**: emerging
- **Quote**: "On the 34 held-out questions, the frozen heuristic dropped 23.2 percentage points to 70.6%."
- **Our assessment**: A clean dev/held-out design, which is rare in vendor posts. Failure modes are instructive: long-but-simple prompts (extract a port from Kubernetes YAML) falsely escalate, short-but-multi-step traces (mutable default args, `{1: "a", True: "b", 1.0: "c"}`) falsely stay cheap. Caveat: the heuristic was written by the authors, who may not have tried hard; a Google-run test of a third-party classifier.

### Claim 4: `maxOutputTokens` is a ceiling, not a thinking budget; capping it does not make easy tasks cheaper and breaks hard ones
- **Evidence**: gemini-3.8-flash with cap 300 vs 4096 (default thinkingConfig): almost identical thinking tokens on the 27 tasks labelled SIMPLE; capped version cost slightly more. Cap broke 7 of 25 hard tasks (6 ran out of room mid-reasoning, 1 squeezed reasoning and answered wrong).
- **Confidence**: emerging
- **Quote**: "Capping the model's output at 300 tokens didn't save any money on easy tasks."
- **Our assessment**: Concrete, actionable, and counterintuitive. Single run, Gemini-specific; the general lesson (control reasoning via the dedicated thinking parameter, not the output cap) likely transfers to other reasoning-model APIs but is not shown here.

### Claim 5: If the cheap option does not reduce thinking, no router can save money
- **Evidence**: The Jev router sending easy tasks to the capped Flash and hard ones to normal Flash solved all 50 but cost slightly more than plain Flash everywhere and was slower.
- **Confidence**: emerging
- **Quote**: "If your cheap option doesn't actually make the model think less on easy tasks, no router can save you money."
- **Our assessment**: Good design principle: validate that the cheap arm is actually cheaper before building routing.

### Claim 6: The strongest no-router baseline (Flash with thinking level LOW) solved all 50 tasks and should be tried before building a router
- **Evidence**: Gemini 3.8 Flash at `thinkingLevel: "LOW"` solved 50/50 and "cost considerably less than the default setting" (per the closing rules).
- **Confidence**: emerging
- **Quote**: "Start with Flash on low thinking before you build a router."
- **Our assessment**: Strong practical advice and the article's most transferable point: tune the thinking-level knob first. Limited by short prompts and easy-ish tasks; low thinking may fail on harder real workloads.

### Claim 7: A Flash-Lite-first router that escalates only classifier-flagged tasks to Flash-LOW matches 100% accuracy with lower latency and modestly lower cost
- **Evidence**: Flash-Lite alone answered simple tasks in half a second but missed 6 of 25 hard ones; Jev flagged all 6 as complex and escalated. Router solved 50/50. Keyword heuristic router was cheaper "only because it got things wrong": 5 hard tasks to Flash-Lite, 2 failed, 48/50.
- **Confidence**: emerging
- **Quote**: "On prompts this short the cost difference per task is small, so for an interactive agent the shorter wait is the bigger benefit."
- **Our assessment**: The honest framing matters: the router's benefit over the Flash-LOW baseline is mostly latency, with small cost savings. Exact dollar figures live in image tables not reproduced here.

### Claim 8: Escalating to a heavier target (default-thinking Flash) did not pay off on this benchmark
- **Evidence**: Routing hard tasks to default-thinking Flash was cheaper than default thinking everywhere but costlier than low thinking everywhere, which already solved all 50.
- **Confidence**: emerging
- **Quote**: "A heavier escalation target only makes sense when the low setting starts failing."
- **Our assessment**: Sensible; the escalation tier should be chosen from observed failures of the cheaper tier.

### Claim 9: Prompt caching is bound to one model, so per-turn model routing conflicts with caching; route short standalone tasks, keep context-heavy turns on one model
- **Evidence**: Argued from product behaviour (Agent Platform Context Caching, 75% to 90% cheaper resend), not measured in the benchmark, whose prompts were short.
- **Confidence**: emerging
- **Quote**: "The catch is that a cache belongs to one model."
- **Our assessment**: Important and under-discussed constraint for harness designers. Untested here; the real tradeoff depends on cache hit rates and context size.

### Claim 10: Model configurations can differ in safety behaviour; the Pro configuration declined two short code-security review prompts that Flash answered
- **Evidence**: Observation from the run; count of two prompts.
- **Confidence**: anecdotal
- **Quote**: "In our run, the Pro configuration declined two short code-security review prompts that Flash answered."
- **Our assessment**: Small but practically relevant for routing: routing across models also routes across refusal behaviours. Test security-review prompts on the intended configuration.

### Claim 11: Instrument traces and thinking-token counts to see what drives spend and catch truncation/retries
- **Evidence**: Recommendation only (Cloud Logging and BigQuery).
- **Confidence**: emerging
- **Quote**: "Measure what your agent actually spends."
- **Our assessment**: Consistent with the truncation finding in Claim 4, since truncation silently inflates retries. Vendor-stack-specific implementation.

## Concrete Artifacts

Atomic Noul routing question (verbatim from the article; request body, Python):

```python
def call_jev(question_text):
    body = {
        "state": question_text,
        "model": "jev-latest",
        "questions": {
            "multi_step": {
                "type": "noul",
                "instructions": (
                    "Answering this requires performing more than one "
                    "sequential calculation, simulation step, or logical "
                    "deduction, rather than a single direct lookup, format "
                    "check, or one-step classification."
                ),
            }
        },
    }
    # Send the request above to the classifier's API.
    # response.answers["multi_step"].noul is the probability used to route.
```

Key measurements (from article prose; single run each):

```
Heuristic router: dev 15/16 (93.8%) -> held-out 24/34 (70.6%)   [34 x 0.706 = 24]
Jev router:       held-out 34/34 (100%); overall 48/50 (96.0%) classification agreement
Flash maxOutputTokens=300 vs 4096: ~equal thinking tokens on 27 SIMPLE tasks; 300 cap broke 7/25 hard tasks
Flash thinkingLevel LOW: 50/50
Router Flash-Lite -> Flash LOW (Jev-flagged): 50/50
Keyword-heuristic router: 48/50 (2 of 5 hard tasks sent to Flash-Lite failed)
Flash-Lite alone: missed 6/25 hard tasks
```

## Cross-References

- **Corroborates**: `blog-anthropic-choosing-claude-model.md` Claim 7 (effort level as an axis independent of model class; lower effort on a bigger model can beat a smaller model) is the Anthropic-side analogue of this article's "tune thinking level before routing." Claim 2 of that note shares the cost-per-task framing.
- **Contradicts**: None found. (Mild tension: `blog-anthropic-choosing-claude-model.md` Claim 2 favours starting with the most capable model; this article favours starting with a fast model on a light setting. These are different recommendations but conditioned on different workloads, so not filed as a contradiction.)
- **Extends**: `blog-simonwillison-jev-decision-models.md` Claim 4 (Jev API takes one state and many questions of Noul/Choice/Score types): this article provides a benchmarked usage pattern and the "atomic Noul over broad Choice" guidance. `blog-latentspace-macmanus-glean-model-routing.md` Claim 8 (Glean evaluates routers by running parallel tasks with alternative models and judging): this article gives an offline, auto-graded evaluation design (dev/held-out split) for the same problem.
- **Related**: `blog-google-api-gateway-model-routing.md` Claim 1 (gateway-level routing across models): infrastructure layer versus this article's per-task classifier layer.
- **Novel**: Held-out evidence that regex/length heuristic routers overfit; the `maxOutputTokens` vs thinking-token finding; the per-model cache vs routing tension; routing-induced differences in safety refusals.

## Guide Impact

- **Chapter 02 (harness/model configuration)**: Add guidance that thinking level is the primary cost knob and `maxOutputTokens` is not a substitute; recommend evaluating "strongest single model at low thinking" before building any router (Claims 4, 6).
- **Chapter 02 (routing layer)**: When describing classifier routing, recommend atomic yes/no checks over a broad simple/complex label, and a dev/held-out evaluation split for heuristic routers (Claims 2, 3).
- **Chapter 04 (context)**: Note that context caches are per-model, so mid-session model switching forfeits the cache discount; route only short standalone sub-tasks (Claim 9).
- **Chapter 05 (metrics)**: Use "cost per successful task" with an explicit definition (spend across loops, tool calls, retries, thinking passes over verified successes) (Claim 1).
- **Ch03 (verification)**: Optional example of an auto-graded 50-prompt benchmark as the routing-validation method; treat numbers as single-run vendor results.

## Extraction Notes

- Read the full article text (fetched HTML, stripped). Result tables/charts are images and were not extractable; all numbers come from prose. Exact per-task dollar costs and latencies were therefore not captured.
- Did not follow linked pages (codelab, Jeff Nelson's BigQuery cascade post).
- Model names (Gemini 3.8 Flash, 3.5 Flash-Lite, 3.1 Pro) are as written in the article.
- The "24/34" figure in Concrete Artifacts is derived arithmetic from 70.6% of 34, not stated in the article.
