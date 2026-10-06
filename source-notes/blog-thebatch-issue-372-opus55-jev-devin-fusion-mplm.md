---
source_url: https://www.deeplearning.ai/the-batch/issue-372
source_type: blog-post
title: "The Batch Issue 372: Opus Stalks the Frontier, Jev Classifies Everything, Running Two Models in One Agent"
author: Andrew Ng and The Batch editorial team (DeepLearning.AI)
date_published: 2026-09-25
date_extracted: 2026-10-06
last_checked: 2026-10-06
status: current
confidence_overall: emerging
issue: "#3925"
---

# The Batch Issue 372: Opus Stalks the Frontier, Jev Classifies Everything, Running Two Models in One Agent

> A weekly digest whose guide-relevant content is independent (Artificial Analysis, Vals AI) numbers for Cognition's lead/sidekick Devin Fusion harness, the Fusion-vs-Fugu split on a frontier model's role, Ng's "calibrate to project stage" letter, TypeSafe's Jev classifier, Claude Opus 5.5's launch numbers, and CMU's Message Passing Language Models.

## Source Context

- **Type**: blog-post (weekly newsletter issue; Ng letter + four news items). The live page returns HTTP 403 to WebFetch and curl; the full text was read from the Internet Archive snapshot of the same URL (web.archive.org, 2026-10-02). The sponsor message was ignored.
- **Author credibility**: Andrew Ng (DeepLearning.AI) and The Batch's reporting team. News items are secondary reporting of primary releases (Anthropic, TypeSafe, Cognition, Artificial Analysis, Vals AI, a CMU paper); the letter is opinion drawn from Ng's own project experience.
- **Scope**: Ng's letter on project-stage calibration; Opus 5.5 launch; Jev; Devin Fusion/SWE-2 with a Fugu comparison; MPLM. It does not give primary-source data; linked primary sources (Cognition, TypeSafe, MPLM paper) were not fetched in this pass.

## Extracted Claims

### Claim 1: The right tactic for AI engineering tasks (evals, architecture, product feedback) depends on project stage, and one-size-fits-all corporate policies can be counterproductive
- **Evidence**: Ng's experience; worked example of evaluating a customer-service email system from a dozen manually inspected examples, to hundreds with a rubric, to tens of thousands with downstream-effect measurement. No data.
- **Confidence**: anecdotal (expert opinion, though widely shared)
- **Quote**: "This is why corporate policies that mandate a one-size-fits-all approach, like requiring certain types of testing before anything can be shipped, can be counterproductive."
- **Our assessment**: Credible and consistent with practitioner experience. It is a conditioning variable for the guide's eval and verification advice rather than a contradiction of it: advice should be tagged by project maturity. Ng also names the failure in both directions (large-company engineers over-engineering startups; startup engineers hitting a "performance ceiling" at scale).

### Claim 2: Over- and under-design are both failure modes, and architecture rigor should rise as a project matures
- **Evidence**: Ng's argument, with early-stage versus mature examples (latency, availability, consistency, reliability, maintainability, simplicity, cost).
- **Confidence**: anecdotal
- **Quote**: "It is not helpful to over-design at the early stages, or under-design a mature product."
- **Our assessment**: Useful short statement of a principle; low novelty on its own, but it ties directly to the "when to ship a fast MVP versus slow down" skill Ng names in his skills map.

### Claim 3: Claude Opus 5.5 ranks first on both Artificial Analysis' Intelligence Index v4.3 (58) and Vals Index (69.69%), but cost per task stays high because it uses more tokens
- **Evidence**: Third-party indices cited by The Batch: Opus 5.5 at max reasoning with fallback scored 58, seven points above Opus 5 and five above Fable 5.1 and GPT-6 Astra; $5.98 per task versus $7.63 for Fable 5.1 and $3.26 for GPT-6 Astra.
- **Confidence**: emerging (independent evaluators, but reported secondhand and with the fallback caveat in Claim 4)
- **Quote**: "Artificial Analysis reports that while Claude Opus 5.5 costs less per token than its predecessor or Claude Fable 5.1, the model’s cost per benchmark task remains high because it uses more tokens than earlier Opus models."
- **Our assessment**: Another data point for price-per-task over price-per-token, from a third party rather than a vendor. Note the list price in this issue ($4/$0.25/$20 per million input/cached/output) differs slightly from the cache-read figure ($0.20/M) in `blog-simonwillison-opus55-gpt6-sol-luna-price-war.md` Claim 6; the Batch separately lists "cache reads/writes $0.20/$5", so the $0.25 is likely a cached-input/cache-read distinction in the Batch's own table. Flagged, not resolved.

### Claim 4: Opus 5.5 falls back to Opus 4.8 on queries Anthropic deems sensitive (cyber, bio), so benchmark scores understate or blur true capability, and legitimate work may be refused
- **Evidence**: Launch description; The Batch's own editorial comment. Vals reports that counting fallbacks as failures did not meaningfully change its score.
- **Confidence**: emerging
- **Quote**: "It’s also important that legitimate safety, biomedical, and AI engineering work may be refused out of fears that users will use the models in ways Anthropic doesn’t want them to."
- **Our assessment**: Practical operational caveat: a model ID may silently serve a different (older) model for some prompts, which matters for evals, reproducibility and routing policy. Editorial speculation, not measured here.

### Claim 5: Opus 5.5 exposes five reasoning levels (low to max, default high) and a fast mode at 2.5x speed for 2x cost
- **Evidence**: Launch specs as reported by The Batch.
- **Confidence**: emerging (vendor-published specs relayed secondhand)
- **Quote**: "Reasoning always on, five levels (low, medium, high, xhigh, and max, defaults to high), statistical watermarking of generated text, fast mode (2.5x speed at 2x cost)"
- **Our assessment**: Useful reference for effort-level guidance. The Batch's benchmarks use max; `blog-simonwillison-opus55-gpt6-sol-luna-price-war.md` Claim 9 reports max hitting the 128k output cap with no answer, so leaderboard settings may not be practical defaults.

### Claim 6: Devin Fusion pairs a frontier lead with a cheaper sidekick, each with its own context and tools, and matched Claude Code running Fable 5.1 alone at 36% lower cost per task on an independent index
- **Evidence**: Artificial Analysis Coding Agent Index v1.5: Fusion (Fable 5.1 xhigh lead + SWE-2 medium sidekick) scored 62 at $7.90 and 35.8 min per task versus Claude Code with Fable 5.1 max (62, $12.40, 34.8 min). With GPT-6 Astra: 59 at $4.54 and 24.7 min versus Codex Astra max (62, $7.47, 29.4 min).
- **Confidence**: emerging (independent evaluator, but vendor-supplied harness, a single index, and lead/sidekick configured at lower reasoning levels than baselines)
- **Quote**: "Instead of handing a task from one model to another in sequence, Devin Fusion runs two agents at once."
- **Our assessment**: This is the first independent replication of Cognition's own numbers (`blog-cognition-devin-fusion.md` Claim 1: 35%; `blog-cognition-devin-local-fusion.md` Claim 1: up to 39%). The result is not uniform: Fusion lost three points with Astra, and on Vals Code Migration Fusion won with Fable (57.3% at $42.00 vs 54.6% at $70.97) but lost with Astra (61.3% vs 67.7%).

### Claim 7: Agents exchange briefs, results and feedback rather than full conversations, which preserves each agent's prompt cache; this is why ordinary mid-session model routing fails
- **Evidence**: The Batch's summary of Cognition's argument; the lead hands the sidekick a brief with constraints and success criteria and "reclaims" the task when the sidekick stumbles.
- **Confidence**: emerging (restated vendor rationale; mechanism not independently measured)
- **Quote**: "Moving a task to another model mid-session empties the cache, and refilling it at frontier prices reduces savings that routing would otherwise give."
- **Our assessment**: Corroborates `blog-cognition-devin-local-fusion.md` Claim 4 and Claim 5 and `blog-anthropic-prompt-caching-everything.md` Claim 6 (switching Opus to Haiku mid-session costs more than staying), now with an independent reporter repeating it. Still Cognition's argument, not an independent test.

### Claim 8: Cloud Fusion can swap models mid-session at compaction boundaries, where the cache is discarded anyway, driven by lightweight classifiers
- **Evidence**: Description of the cloud variant.
- **Confidence**: emerging
- **Quote**: "These model swaps happen during compaction, when an agent summarizes earlier turns to shrink context. Compaction discards the cache, so the switch adds no cost."
- **Our assessment**: Matches `blog-cognition-devin-fusion.md` Claim 6. Actionable design rule for any router: schedule model switches at compaction or other forced cache resets.

### Claim 9: Token count is no longer a proxy for cost in a two-model harness: Fusion used 70% more tokens and nearly 3x the turns of Claude Code yet cost less per task
- **Evidence**: Artificial Analysis measurement for Fusion with Fable 5.1 lead versus Claude Code with Fable 5.1 alone.
- **Confidence**: emerging (independent measurement, single configuration)
- **Quote**: "Fusion muddies these estimates because it burns lower-cost tokens at a higher rate."
- **Our assessment**: Strong practical caution for cost dashboards: track dollars per task and per-model token mix, not total tokens. Pairs with `blog-cognition-devin-local-fusion.md` Claim 7 ("price per task rather than price per token").

### Claim 10: A pricier, smarter sidekick can be cheaper overall; SWE-2 was the most efficient sidekick, beating a cheaper-per-token option on both quality and cost
- **Evidence**: The Batch's "Why it matters" comparison against GPT-5.6 Luna. No numbers given in this piece.
- **Confidence**: emerging
- **Quote**: "SWE-2 appears to be the most efficient option for a sidekick model, both outperforming and costing less than models (for example, GPT-5.6 Luna) that are head-to-head more intelligent and cost less per token."
- **Our assessment**: Consistent with `blog-cognition-devin-local-fusion.md` Claim 8. The sentence is awkwardly worded in the source (it says Luna is "more intelligent" head-to-head, which seems to contradict the sentence's own point); read as "Luna is cheaper per token". Treat the direction as supported, the wording as unreliable.

### Claim 11: SWE-2 is trained with an RL reward that subtracts cost (money and time) from success, so all reasoning levels come out of one run
- **Evidence**: Training description: fine-tuned from Kimi K3 (2.8T-parameter MoE); Kimi K3's makers instead trained a separate expert per reasoning level and merged.
- **Confidence**: emerging (secondhand description of the vendor's method, no ablation reported)
- **Quote**: "The reward subtracts what an attempt costs, in money and time, from whether it succeeded."
- **Our assessment**: Novel to the corpus as a concrete cost-aware reward design for a worker model. Cognition-only claim; evidence is the benchmark above.

### Claim 12: Two competing multi-model designs disagree about a frontier model's role: Fusion keeps one in charge, while Sakana's Fugu uses a cheap trained dispatcher over a pool
- **Evidence**: The Batch's comparison; Fugu v2 models (Fugu Max, Fugu Ultra v2) released the same day.
- **Confidence**: emerging
- **Quote**: "The two designs disagree about a frontier model’s role."
- **Our assessment**: Extends `blog-thoughtworks-omahony-fugu-model-routing-critique.md` (Claim 1 on Fugu's coordinator, Claim 10 on owning your orchestration layer): the Batch frames Fusion versus Fugu as lead-plus-worker versus dispatcher-plus-pool. No head-to-head exists in this source; Ng's team concludes only that specialised companion models work.

### Claim 13: Jev is a non-autoregressive classifier, not an LLM, that returns calibrated probabilities, and is built to be asked many short questions in parallel
- **Evidence**: TypeSafe's own four internal datasets (answers determined by GPT-6 Astra and Claude Fable 5): 67% accuracy, similar to GPT-5.6 Terra and Claude Sonnet 5; about $0.0007 per example versus about $0.06 (Terra) and $0.12 (Sonnet); claimed 193.6x faster than unspecified LLMs. Calibration via "reinforcement learning for calibrated decisions" (RLCD). No public benchmark.
- **Confidence**: anecdotal (vendor-only internal evals with LLM-derived labels; architecture and training data undisclosed)
- **Quote**: "Jev’s structure and pricing encourage users to ask many short, straightforward questions at once."
- **Our assessment**: Interesting pattern (decompose a classification into several criteria, such as domain mismatch or credential requests for spam, and let software combine the probabilities), but labels come from other LLMs and the datasets are private, so the cost/speed claims are unverified. The Batch notes Vercel and Cloudflare added Jev support for uses like tool selection; no data on outcomes.

### Claim 14: Small specialised classifiers are already being used to replace LLM calls for control decisions (tool selection, jailbreak detection, satisfaction judging)
- **Evidence**: The Batch's observation of platform adoption plus copycats (Laya, Bespoke Nimble, Kev on Qwen 3.5 bases); no public benchmark to compare them.
- **Confidence**: anecdotal
- **Quote**: "Instead, it can detect jailbreaks, flag missing details, judge user satisfaction, and more — all situations where turning unstructured input into structured responses can be tremendously valuable for software engineers."
- **Our assessment**: Parallels the first-stage classifier in `blog-cursor-router-compass-taxonomy-mechanics.md` Claim 1 (Compass decides whether a frontier model is needed at all). Worth watching as a harness building block; no evidence yet of end-to-end gains.

### Claim 15: MPLM lets sub-agent threads message each other directly instead of through a coordinator, improving speed and per-thread token growth on structured puzzles
- **Evidence**: CMU paper (Liu, Arora et al.); a Qwen3-0.6B-Base model trained on program-generated traces. 9x9 Sudoku: 100% in ~15 s versus 93% in ~60 s for the coordinator-based parallel method; 25x25: 72% solved while both baselines hit authors' limits; 3-SAT: ~92% vs ~91%, up to 2.5x faster on some examples.
- **Confidence**: emerging (a research prototype on toy, fixed-topology tasks)
- **Quote**: "Enabling threads to communicate directly makes the coordinator unnecessary and limits the total load on any one thread."
- **Our assessment**: Only applies where the communication pattern is known in advance; the source itself warns "MPLM's efficiency depends on knowing in advance which threads must communicate with which." Not evidence for open-ended coding agents. The Batch's closing note that two larger Qwen models gained ~2x lower latency on LongBench-v2 is a weak generalisation signal.

## Concrete Artifacts

```
Artificial Analysis Coding Agent Index v1.5 (as reported in The Batch issue 372)
Devin Fusion, Fable 5.1 xhigh lead + SWE-2 medium sidekick: 62, $7.90/task, 35.8 min/task
Claude Code, Fable 5.1 max with fallback:                  62, $12.40/task, 34.8 min/task
Devin Fusion, GPT-6 Astra xhigh lead + SWE-2 medium:       59, $4.54/task, 24.7 min/task
Codex, GPT-6 Astra max:                                    62, $7.47/task, 29.4 min/task

Vals AI Code Migration
Fusion (Fable 5.1 + SWE-2): 57.3% at $42.00/task   Claude Code (Fable 5.1): 54.6% at $70.97/task
Fusion (Astra + SWE-2):     61.3% at $35.51/task   Codex (Astra):           67.7% at $44.36/task
```

```
Fusion roles (paraphrased from The Batch's "How it works"; not a source quote)
lead:     resolves ambiguity, writes plan, briefs sidekick (constraints + success criteria), reviews, reclaims task if sidekick stumbles
sidekick: reads, edits, tests code; reports back
transport: briefs, results, feedback (not whole conversations) -> each agent keeps its own context and prompt cache
```

```
Opus 5.5 spec lines (The Batch issue 372)
Input/output: text and images in (up to 1M tokens), text out (up to 128,000 tokens)
Price: $4/$0.25/$20 per million input/cached/output; batch $2/$10
Intelligence Index v4.3: 58 (max + fallback); $5.98/task
```

## Cross-References

- **Corroborates**: `blog-cognition-devin-fusion.md` Claim 1 and `blog-cognition-devin-local-fusion.md` Claim 1 (Fusion cost reductions, now independently measured by Artificial Analysis); `blog-cognition-devin-local-fusion.md` Claim 4 and `blog-anthropic-prompt-caching-everything.md` Claim 6 (mid-session model switches break the cache); `blog-cognition-devin-fusion.md` Claim 6 (swap at compaction); `blog-cognition-devin-local-fusion.md` Claim 8 (a stronger sidekick can be cheaper overall).
- **Contradicts**: None identified. Ng's "calibrate to project stage" (Claim 1) tempers, but does not oppose, any existing note; the guide-relevant tension is that Fusion's gain is mixed across lead models (Claim 6), which is a context difference rather than a contradiction, so no contradiction issue was filed.
- **Extends**: `blog-thoughtworks-omahony-fugu-model-routing-critique.md` Claim 1 and Claim 10 (Fugu versus Fusion framing); `blog-simonwillison-opus55-gpt6-sol-luna-price-war.md` Claim 6 and Claim 9 (Opus 5.5 price and max-effort behaviour, now with benchmark and per-task cost numbers); `blog-latentspace-ainews-andrew-ng-ai-engineering.md` Claim 5 (Ng's "when to quickly build an MVP... and when to slow down" skill, now expanded in his letter); `blog-cursor-router-compass-taxonomy-mechanics.md` Claim 1 (classifier-first routing; Jev as a general-purpose version).
- **Novel**: Independent third-party cost/accuracy numbers for a lead/sidekick harness including a loss case with GPT-6 Astra; token count as a misleading cost proxy in multi-model harnesses (70% more tokens, ~3x turns, lower cost); SWE-2's cost-subtracting RL reward; the Jev classifier-as-harness-component pattern with calibrated probabilities; MPLM peer-to-peer sub-agent messaging; Opus 5.5 fallback-to-Opus-4.8 as an evaluation caveat.

## Guide Impact

- **Chapter 05 (Agentic Patterns)**: Where the guide describes lead/sidekick or architect/worker patterns (currently citing `blog-cognition-devin-fusion.md` and `blog-cognition-devin-local-fusion.md`), add this issue's Artificial Analysis and Vals results as independent evidence, including the GPT-6 Astra case that lost three points, and the Fusion-versus-Fugu split from Claim 12.
- **Chapter 05 / cost guidance**: Add the warning that in multi-model harnesses total tokens misreport spend (Claim 9); recommend tracking cost per task and model-mix per task.
- **Chapter 05 (peer sub-agents)**: Optionally note MPLM (Claim 15) as research-stage evidence that coordinator-less messaging helps only when the communication topology is known in advance.
- **Chapter 02 (Foundation Models)**: Add Opus 5.5 data points (Claims 3-5): fallback to Opus 4.8 on sensitive queries, five effort levels, per-task cost still high despite lower list price.
- **Ch02 / Ch05 (small models as components)**: Mention Jev-style classifiers as a cheaper control-plane component, labelled anecdotal pending a public benchmark (Claims 13-14).
- **Verification/eval chapter**: Ng's stage-calibration principle (Claims 1-2) can frame eval-rigor advice as stage-dependent rather than universal.

## Extraction Notes

- The live URL returned 403 to WebFetch and curl; text was read from the Internet Archive snapshot (20261002204133), which required gzip decompression. The full issue (letter and all four news items) was read.
- Linked primary sources (Cognition Fusion/SWE-2 posts, TypeSafe's Jev post, the MPLM paper, Artificial Analysis, Vals AI) were not fetched; figures are The Batch's secondary reporting.
- Confidence is `emerging`: reputable reporting with independent-evaluator numbers for Fusion and Opus 5.5, but vendor-only evidence for Jev and a toy-task paper for MPLM.
- All quotes were copied from the archived text; cross-referenced claim numbers were checked against headings in the cited notes. Cross-references to Cognition's notes were based on their claim headings and the two Claim 4/7/8 passages read in full.
- The Batch says the Opus 5.5 cached-input price is $0.25 in one line and $0.20 in the cache-read line; both are reproduced as published.
