---
source_url: https://martinfowler.com/articles/are-harnesses-worth-the-cost.html
source_type: blog-post
title: "Are Harnesses Worth the Cost?"
author: Naresh Jain (founder of Specmatic, Xnsio and ConfEngine)
date_published: 2026-10-13
date_extracted: 2026-10-14
last_checked: 2026-10-14
status: current
confidence_overall: emerging
issue: "#4099"
---

# Are Harnesses Worth the Cost?

> A paired-run experiment (10 runs per condition, two models, one task) suggests a behavioral harness (contract guides plus executable sensors) rescues a cost-optimized model's reliability (3/10 to 10/10) but adds ~7x cost with no measurable acceptance gain for a frontier model, leading to the hypothesis that model capability changes *when* sensors run, not *whether* an independent gate is needed.

## Source Context

- **Type**: blog-post (author-run controlled experiment, published on martinfowler.com in the "Exploring Gen AI" series)
- **Author credibility**: Naresh Jain, founder of Specmatic. The article is by Jain, not Böckeler, despite the feed-level attribution to her series. Jain has a commercial interest: the harness was built with Specmatic ("I implemented the behavioral harness using Specmatic, though equivalent contract-testing and service virtualization tools could provide the same capabilities"). Martin Fowler gave detailed review feedback per the acknowledgements. The author used generative AI to help build parts of the harness.
- **Scope**: One greenfield Java backend-for-frontend (product discovery: HTTP API, Order API downstream, Kafka publication), 178 external acceptance tests, GPT-6 Sol and GPT-6 Luna at low reasoning effort in Codex, 10 runs each with and without harness. Exploratory single runs of Claude Sonnet 4.6, Claude Opus 4.6 and Gemini 3.8 Flash. Costs are API-equivalent estimates. Does not cover legacy code, other languages, vague briefs, or authoring cost of the harness.

## Extracted Claims

### Claim 1: For the frontier model (GPT-6 Sol), the harness produced no observable acceptance improvement but cost roughly 7x more
- **Evidence**: 10 runs per condition. Harness: 11,331,970 tokens, 19m53s, ~$2.679, 10/10 accepted. No harness: 1,076,371 tokens, 6m51s, ~$0.406, 10/10 accepted. All runs passed all 178 tests.
- **Confidence**: emerging
- **Quote**: "For GPT-6 Sol, the harness used about 10.5 times as many tokens, took nearly 3 times as long, and cost about 7 times more, yet both conditions succeeded in all 10 runs."
- **Our assessment**: Credible as an observation, but a ceiling effect: with 10/10 baseline there was no room to show benefit, and the brief was unusually detailed (Claim 9). Shows harness overhead is real, not that harnesses are useless for frontier models.

### Claim 2: For the cost-optimized model (GPT-6 Luna), the harness turned a 3/10 acceptance rate into 10/10
- **Evidence**: Harness: 22,933,648 tokens, 35 min, ~$0.273, 10/10. No harness: 5,860,736 tokens, 15m56s, ~$0.086, 3/10.
- **Confidence**: emerging
- **Quote**: "Without a harness, it succeeded in 3 of 10 runs. With the harness, it succeeded in all 10."
- **Our assessment**: The strongest data point in the article. n=10 is small but 3/10 vs 10/10 is a large gap. Guides and sensors were added together, so the mechanism is not isolated (Claim 10).

### Claim 3: A harnessed cheap model beat an unharnessed frontier model on cost at equal reliability
- **Evidence**: Harnessed Luna ~$0.273/attempt vs unharnessed Sol ~$0.406/attempt, both 10/10. Harness added on average 17,072,912 tokens, 19m04s and ~$0.187 per Luna attempt (~3.9x tokens).
- **Confidence**: anecdotal
- **Quote**: "even with the harness overhead, a harnessed Luna attempt cost about 33% less than an unharnessed Sol attempt ($0.273 vs $0.406), and both conditions achieved the same 10-for-10 acceptance rate in this sample."
- **Our assessment**: True within the sample, but the comparison excludes harness authoring/maintenance cost and the cost of repairing failures (Claim 8), and Luna harnessed took 35 min vs Sol unharnessed ~7 min. The "33% cheaper" headline is cost-only, not time or total cost of ownership.

### Claim 4: Unharnessed failures were not syntax errors or misunderstanding; they clustered at protocol boundaries, resiliency paths and integration seams
- **Evidence**: Failed unharnessed Java apps each passed at least 144 of 178 checks; unharnessed Luna averaged 94.8% of functional checks. Specific failures: deferred product creation at the timeout boundary returned 503 (4 apps), 400 (2), 429 (1) instead of 202 with a monitor link; in 7 runs the missing monitor URL caused secondary failures; Kafka publication reached the broker but violated the wire contract in 3 runs (Spring JSON serializer added a `__TypeId__` header in 2; `"categories": null` where an array was required in 1); 415 returned where the brief required 400; generic 500 handler on invalid requests; wrong representation for missing monitor; env var mismatch `ORDER_API_API_KEY` vs `ORDER_API_KEY` giving 503 instead of 201.
- **Confidence**: emerging
- **Quote**: "The observed gaps appeared at protocol boundaries, resiliency paths, and integration seams, where a convincing implementation could still fail as a system."
- **Our assessment**: A useful, concrete failure taxonomy for what "almost right" agent output looks like. The author is careful that the timeout-detection mechanism "is a likely explanation rather than a proven common cause."

### Claim 5: "Executable attention": explicit requirements can lose influence during implementation, and a red sensor pulls them back into focus
- **Evidence**: The deferred workflow, Kafka contract and exact error codes were all in the brief; Sol preserved them in all runs, Luna sometimes did not. The author's interpretation, explicitly not established as a cause.
- **Confidence**: anecdotal
- **Quote**: "A requirement can be explicit in the brief and still lose influence during implementation."
- **Our assessment**: A useful framing, but a hypothesis. The author states "this experiment did not establish the cause" of the lapses. Consistent with Böckeler's "monitor outcomes and give automated feedback" thread.

### Claim 6: Sensors should derive from human-supplied contracts and examples, not from tests the implementing agent writes, so expectations have an independent source
- **Evidence**: Design description: contract checks generated deterministically from OpenAPI/AsyncAPI; examples validated against specs before tests run ("examples validate" command); agent instructed to preserve inputs and not weaken expectations; reviewable evidence of dependency interactions required.
- **Confidence**: emerging
- **Quote**: "If an agent interprets requirements to write both the implementation and its tests, the same misreading or omission can appear in both."
- **Our assessment**: Strong design principle, matching the same-agent-writes-test-and-confirms-failure critique in the TDD note. Not tested in the experiment (no condition where the agent writes its own tests).

### Claim 7: The same sensors serve two roles: feedback during development and an independent acceptance gate at completion
- **Evidence**: Design argument; the outer-loop evaluation of 178 tests was hidden from the inner harness and applied to both conditions.
- **Confidence**: emerging
- **Quote**: "At completion: Sensor results become the basis for accepting the work: an independent check of the agent's interpretation against human expectations, which matters for every model."
- **Our assessment**: Clean separation of inner-loop feedback from outer-loop acceptance. Worth adopting as vocabulary.

### Claim 8: Recommended practice splits by model tier: continuous sensors for inconsistent cost-optimized models, a single final gate for frontier models (untested hypothesis)
- **Evidence**: Derived from Claims 1-2. The author states the "final gate only" condition was not measured and that failures at the gate could still require diagnosis and repair cycles. The author also notes the cost figures exclude harness authoring, maintenance and repair of unacceptable results.
- **Confidence**: anecdotal
- **Quote**: "Model capability changes when and how often sensors run, not whether an independent verification gate is needed."
- **Our assessment**: Plausible and actionable but explicitly a "revised, conditional hypothesis"; the next experiment is the final-gate-only condition. Do not present as established.

### Claim 9: The result may not generalize: one task, one language, n=10, low reasoning effort, and an unusually detailed brief
- **Evidence**: The author's own limitations section; also the harness could not isolate guides from sensors.
- **Confidence**: settled (as a statement of limitations)
- **Quote**: "This experiment covered 10 paired runs per model on 1 greenfield Java service, with both models at low reasoning effort."
- **Our assessment**: Must be carried into any guide text. A less detailed brief could hurt unaided runs more (favoring harness) or hurt the quality of contracts (hurting harness); the direction is unknown.

### Claim 10: Guides and sensors were added together so their individual contributions cannot be separated
- **Evidence**: Harness bundled OpenAPI/AsyncAPI specs, examples, an API-development skill, contract-driven mocks, API tests, CTRF and coverage reports. The feedback loop depended on the agent invoking tools; it did not run after every edit.
- **Confidence**: settled (as limitation)
- **Quote**: "Because the harness added guides and sensors together, this experiment also cannot isolate their individual contributions."
- **Our assessment**: Limits causal claims; "harness" here is a heavy, specific bundle, so cost conclusions do not transfer to lighter harnesses.

### Claim 11: Frontier models other than Sol also solved the task unassisted in exploratory runs
- **Evidence**: Single exploratory runs, all at low reasoning effort.
- **Confidence**: anecdotal
- **Quote**: "In exploratory runs with Claude Sonnet 4.6, Claude Opus 4.6, and Gemini 3.8 Flash (all at low reasoning effort), each also managed to complete the task unassisted on the first try."
- **Our assessment**: Single runs, so weak evidence; only suggests the task was "easy" for frontier models, supporting the ceiling-effect reading of Claim 1.

### Claim 12: Harness cost accounting omits human setup and repair costs, so "cheaper" is only autonomous generation cost
- **Evidence**: Author's economics section.
- **Confidence**: settled (as limitation)
- **Quote**: "They exclude the upfront effort of authoring, reviewing, and maintaining the contracts, examples, assertions, and harness."
- **Our assessment**: Important for Ch05; the real total cost depends on how reusable contracts are, which the author says he did not measure.

## Concrete Artifacts

```
GPT-6 Sol (10-run averages) — Jain, "Are Harnesses Worth the Cost?"
Harness  Tokens       Time          Est. cost  Accepted
Yes      11,331,970   19m 53s       ~$2.679    10/10
No        1,076,371    6m 51s       ~$0.406    10/10

GPT-6 Luna (10-run averages)
Harness  Tokens       Time          Est. cost  Accepted
Yes      22,933,648   35 min        ~$0.273    10/10
No        5,860,736   15m 56s       ~$0.086     3/10
```

Experiment design (paraphrased from article, not a quote): inner loop = brief + OpenAPI/AsyncAPI contracts + request/response examples + API-development skill + contract-driven mocks (Specmatic) + test/CTRF/coverage reports, invoked via the project's test command; outer loop = 178 hidden acceptance tests run in isolated Docker containers with fresh Codex home per attempt. Acceptance = starts successfully AND passes all 178 tests.

Failure symptoms (from "Where unharnessed runs slipped up"): `__TypeId__` header added by Spring JSON serializer; `"categories": null` where array required; 415 instead of required 400; env var `ORDER_API_API_KEY` read vs `ORDER_API_KEY` supplied.

## Cross-References

- **Corroborates**: `blog-fowler-boeckeler-tdd-in-the-agent-loop.md` Claim 6 (red/green loses meaning when the same agent writes and verifies tests; here, independent human-supplied contracts address that) and Claim 12 (monitor outcomes and give automated feedback rather than dictating how). `blog-humanlayer-skill-issue-harness-engineering.md` Claim 8 (success correlates with the agent's ability to verify its own work).
- **Contradicts**: None filed. Note a tension, not a contradiction: `blog-humanlayer-skill-issue-harness-engineering.md` Claim 1 attributes most failures to harness configuration, whereas here harness benefit is strongly model-tier dependent and zero for Sol. The claims differ by context (task, model tier), so no contradiction issue was filed per MINER.md §4a.
- **Extends**: `blog-fowler-edwardsalexander-refactoring-token-economics.md` (the article cites it as influencing how token use was measured; this adds a harness-overhead measurement of tokens/time/cost). `blog-fowler-boeckeler-local-models-viability.md` Claim 9 (task choice dominates small-model viability) and Claim 10 (pairing a stronger planner with a weaker executor): here a harness compensates for weaker-model drift on a well-specified task.
- **Novel**: Paired-run data on harness overhead vs reliability by model tier; the "executable attention" framing; the dual role of sensors (inner feedback vs outer acceptance gate); a concrete taxonomy of integration-seam failures; the continuous-vs-final-gate hypothesis by model tier.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add a scoped qualifier that harness benefit depends on model tier and task specification quality: in this one experiment it fixed a cheap model (3/10 to 10/10) and added ~7x cost with no acceptance gain for a frontier model. Introduce "executable attention" with caveats (single author, n=10, one task, hypothesis rather than established cause). Likely a `**Debated:**`-style note rather than a contradiction.
- **Chapter 03 (Verification)**: Add the dual-role distinction (inner-loop sensors vs independent outer acceptance gate) and the principle that sensors should come from human-supplied contracts rather than agent-authored tests (cite Claim 6 here with TDD note Claim 6).
- **Chapter 05 (Cost/Economics)**: Add the harnessed-cheap-model vs unharnessed-frontier-model cost comparison ($0.273 vs $0.406) with the caveats that costs are API-equivalent estimates and exclude harness authoring and repair costs, and that wall-clock time was higher (35 min vs ~7 min).

## Extraction Notes

- Fetched the full article HTML directly and read the whole text; quotes were copied from the extracted page text. Figures (1-6) are images and were not inspected. The article's own citations (Böckeler's "Harness engineering for coding agent users", Edwards-Alexander's refactoring article) were not followed; the latter exists in the corpus.
- The auto-filed issue attributed the piece to Böckeler's series; the byline is Naresh Jain.
- Model names (GPT-6 Sol/Luna, Gemini 3.8 Flash) are as used in the article; pricing context may be in `blog-simonwillison-opus55-gpt6-sol-luna-price-war.md` but was not verified against this article's cost estimates.
- Triage comments differed slightly on figures; all numbers here come from the article tables.
