---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/jev-decision-models-what-need-know-why
source_type: blog-post
title: "Jev and the rise of decision models: what you need to know and why they matter"
author: Ken Mugrage (Thoughtworks), featuring Ben O'Mahony
date_published: 2026-10-12
date_extracted: 2026-10-14
last_checked: 2026-10-14
status: current
confidence_overall: anecdotal
issue: "#4108"
---

# Jev and the rise of decision models: what you need to know and why they matter

> A Thoughtworks explainer, built around one practitioner's demo, that proposes a decision model (Jev) as an "evaluative guardrail" or "confidence gate" in a coding-agent harness in place of LLM-as-judge. It reports no measurements.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, tagged Generative AI / Testing)
- **Author credibility**: Ken Mugrage is a Thoughtworks writer who interviews a colleague. The technical voice is Ben O'Mahony, Principal AI Engineer at Thoughtworks, described as an early Jev adopter and author of O'Reilly's forthcoming *Building AI Agent Platforms*. Neither is the model's vendor. It is a practitioner view, not a measurement.
- **Scope**: Covers how Jev's output modes work, why decision models matter now (cost, latency), one refactoring-candidate demo against Claude, the idea of Jev in a coding-agent harness, the "why now" story (Laya precedence, branding), the "system one" label, and a cost anecdote. It has no benchmarks, no code, no accuracy data, and the demo is described, not shown.

## Extracted Claims

### Claim 1: Jev is probabilistic rather than nondeterministic, because it has no injected randomness and returns a probability distribution over the options the user supplies
- **Evidence**: O'Mahony's explanation as relayed by the author. No tests.
- **Confidence**: anecdotal
- **Quote**: "Jev, though, isn’t nondeterministic: it’s"
- **Our assessment**: The article text continues "probabilistic" after a formatting break. We take the framing as the author's gloss. O'Mahony's own quote is "doesn’t have that injection of randomness." Compare [Latent Space interview](blog-latentspace-jev-system-one-for-prod.md) Claim 5, where the founder prefers robustness to bitwise determinism. The two sources do not claim identical things. Treat "no sampling randomness" as plausible and "deterministic output" as unverified.

### Claim 2: Jev's three modes are noul (true/false), ratings, and choices, and each returns confidence alongside the judgment
- **Evidence**: O'Mahony's description, from hands-on use.
- **Confidence**: emerging (matches other sources)
- **Quote**: "It has three modes of operation,” O’Mahony says. “The most simple is a ‘noul’, which is basically a true or false."
- **Our assessment**: Consistent with the API shape in [Willison](blog-simonwillison-jev-decision-models.md) Claim 4, which names the types Noul, Choice and Score. Here "ratings" is the numeric type. Nothing new on the mechanics.

### Claim 3: Jev suits tasks needing rapid evaluation where a rank or decision is more useful than prose, and its constrained capability is what makes it attractive
- **Evidence**: The refactoring demo, described in prose.
- **Confidence**: anecdotal
- **Quote**: "It’s well-suited to tasks that require rapid evaluation and analysis and where a rank or a decision is more helpful than strings of prose."
- **Our assessment**: Restates [Willison](blog-simonwillison-jev-decision-models.md) Claim 5, classification-shaped tasks. The "constrained is a feature" framing is reasonable but unsupported by data here.

### Claim 4: A refactoring-candidate pipeline, where Jev scans a codebase with a parsing tool against a list of code smells, was faster than Claude and consumed fewer tokens, while Claude gave broader output
- **Evidence**: One live demo observed by the author. No token counts, timings, or precision/recall are reported.
- **Confidence**: anecdotal
- **Quote**: "He shows me how Claude performs the same task, noting how many tokens it consumes compared to Jev."
- **Our assessment**: This was the triage key question, and the answer is that no numbers are reported. We do not know whether the two outputs were equal in quality. The comparison is also not like for like, because Jev scores candidates a tool has already extracted. O'Mahony's own caveat is useful: "which of these am I going to have more confidence in not breaking my code base? Because there's 10,000 things that [Claude] could do." This argues that a narrower action space gives lower risk, not that it gives better quality.

### Claim 5: Jev can sit in the harness around a coding agent as an evaluative guardrail for agent-produced code
- **Evidence**: A proposal from O'Mahony ("Ben mentions"). No implementation described.
- **Confidence**: anecdotal
- **Quote**: "Ben mentions Jev could be used in the"
- **Our assessment**: The article text continues after a formatting break: "harness around a coding agent, acting as a kind of evaluative guardrail for the code that the agent produces." It says "could", so this is a design idea and not a reported result. It fits the harness-as-verification-layer direction. The idea is untested in our corpus. Related: the claim in [Latent Space](blog-latentspace-jev-system-one-for-prod.md) Claim 8 that LLM calls can be verified by putting IDs on every message and asking one question per ID.

### Claim 6: LLM-as-judge is expensive, and its non-determinism makes it unreliable as a judge; Jev avoids this by judging probabilistically and exposing confidence scores
- **Evidence**: Assertion by the author. No citation, measurement or comparison.
- **Confidence**: anecdotal
- **Quote**: "Such an approach is not only expensive, its inherent non-determinism makes it unreliable as a judge."
- **Our assessment**: This is the claim the triage asked us to test, and it is unsupported. The article also describes LLM-as-judge as a technique "where an LLM is trained adversarially to evaluate the output of another, larger LLM", which is not how LLM-as-judge is usually defined (typically a prompted model, not an adversarially trained one). We would not reuse that definition. The cost point is plausible given [Willison](blog-simonwillison-jev-decision-models.md) Claim 3 on input-only pricing. Reliability is not shown, and [Willison](blog-simonwillison-jev-decision-models.md) Claims 6 and 10 (weak on numbers, dates and adversarial content; evals matter more) caution against assuming a decision model is a reliable judge without evaluation.

### Claim 7: Confidence scores make Jev an effective "confidence gate" that eases human-in-the-loop integration
- **Evidence**: Assertion only.
- **Confidence**: anecdotal
- **Quote**: "Jev makes it easier to think about and integrate the"
- **Our assessment**: The text continues "human-in-the-loop: it’s an effective ‘confidence gate’." Threshold-based escalation is concretely specified in [Penumarthi](blog-thoughtworks-penumarthi-jev-rag-pipelines.md) Claim 7 (act above 0.9, LLM fallback 0.6-0.9, escalate below 0.6) and [Latent Space](blog-latentspace-jev-system-one-for-prod.md) Claim 9. This article adds only the name. Whether the probabilities are calibrated is the unanswered question, per [Penumarthi](blog-thoughtworks-penumarthi-jev-rag-pipelines.md) Claim 9.

### Claim 8: The architecture is not new, and Jev cut through because of branding, positioning, and latency-focused use-case comparisons
- **Evidence**: O'Mahony's opinion plus the Laya author's published complaint (Nandakishor Mukkunnoth).
- **Confidence**: emerging
- **Quote**: "“There’s no major innovation here,” Ben notes."
- **Our assessment**: Corroborated by the clone coverage in [Latent Space six clones](blog-latentspace-ainews-six-jev-clones.md). Useful as a caution against treating Jev specifically as the unique technology. The category is what matters.

### Claim 9: "System one model" is a useful label even if partly marketing, because naming helps people find applications
- **Evidence**: Author's argument, with reference to Kahneman's *Thinking, Fast and Slow*.
- **Confidence**: anecdotal
- **Quote**: "While it’s easy to dismiss the use of terms like this as little more than marketing or branding, they nevertheless play an important role"
- **Our assessment**: Contrasts mildly with [Willison](blog-simonwillison-jev-decision-models.md) Claim 2, which prefers "decision models". The article uses both terms. This is a naming preference, not a conflict that affects advice, so we filed no contradiction issue.

### Claim 10: Running decision models rather than frontier models cuts spend from about $1,000 of tokens per person per day to about $1 per day
- **Evidence**: One quote from O'Mahony. No workload, usage volume or accounting basis is given.
- **Confidence**: anecdotal
- **Quote**: "now, with Jev, we're burning a dollar a day — that's a single Claude Code subscription."
- **Our assessment**: Treat as rhetorical. The two figures describe different workloads: an agentic organisation generating code, versus a scoring or gating step. The monthly arithmetic is "$30 at the end of the month", which only holds for the scoring workload. It is not a like-for-like saving. The same source site, [Xiong](blog-thoughtworks-xiong-decision-models-possibility-of-noops.md) Claim 3 and Claim 5, gives a more concrete account of token cost as the binding constraint, though also without figures in our note.

### Claim 11: Model choice is shifting toward routing, open-weight and local models as cost, performance and control frustrate users of the frontier status quo
- **Evidence**: Author's observation of "the last six months".
- **Confidence**: emerging
- **Quote**: "We’ve seen this already over the last six months with the rise of open-weight and local models and growing interest in model routing techniques and platforms"
- **Our assessment**: Consistent with [Xiong](blog-thoughtworks-xiong-decision-models-possibility-of-noops.md) Claim 6 on open-weight cost structure. Context rather than evidence.

## Concrete Artifacts

No code, configuration, or measurements are in the source. The quoted demo flow is the closest thing to a procedure:

```
Refactoring-candidate demo (described by Ken Mugrage, Thoughtworks, 2026-10-12):
  1. Jev crawls a codebase, using a parsing tool.
  2. It finds candidates to refactor, "based on a list of refactoring code smells".
  3. The same task is run with Claude; the author is shown token consumption and breadth of output.
No token counts, timings or accuracy figures are reported.
```

## Cross-References

- **Corroborates**: [Willison](blog-simonwillison-jev-decision-models.md) Claims 1, 4 and 5 (typed probabilistic decisions, question types, classification fit); [Latent Space](blog-latentspace-jev-system-one-for-prod.md) Claim 9 (confidence-based thresholds); [Penumarthi](blog-thoughtworks-penumarthi-jev-rag-pipelines.md) Claim 7 (probability bands); [Latent Space six clones](blog-latentspace-ainews-six-jev-clones.md) (Jev is part of a wider category, Laya among others).
- **Contradicts**: None filed. The "probabilistic, not nondeterministic" framing differs in emphasis from [Latent Space](blog-latentspace-jev-system-one-for-prod.md) Claim 5 (robustness, not bitwise determinism), but the two do not lead to different guide advice.
- **Extends**: [Xiong](blog-thoughtworks-xiong-decision-models-possibility-of-noops.md) Claim 5 (decision models fit triage) with a coding-agent use case. [Penumarthi](blog-thoughtworks-penumarthi-jev-rag-pipelines.md) Claim 1 (most model calls are decisions) with a developer-tooling example.
- **Novel**: (a) the specific proposal of a decision model as an evaluative guardrail in a coding-agent harness, replacing LLM-as-judge; (b) the refactoring-candidate demo against Claude (without numbers); (c) the $1,000 vs $1 a day cost framing.

## Guide Impact

- **Chapter 03 (verification)**: Could mention, as an unproven option, a decision model as a cheap gate before or instead of LLM-as-judge, attributed to a practitioner and labelled anecdotal. Do not repeat "LLM-as-judge is unreliable because non-deterministic" as established. This source offers no evidence, and the source's definition of LLM-as-judge is nonstandard.
- **Chapter 02 (harness engineering)**: A one-line example of a confidence gate in a harness, linking to the [Penumarthi](blog-thoughtworks-penumarthi-jev-rag-pipelines.md) thresholds for the concrete numbers. This source adds the coding-agent framing only.
- **Chapter 01 (model routing / cost)**: The $1/day versus $1,000/day figure should not be cited as a measured saving. At most, use it as an illustration that decision-shaped sub-tasks are priced differently from agentic generation.

## Extraction Notes

- Read the full article (single page, no sub-pages). The related Thoughtworks Jev RAG post was already mined as [Penumarthi](blog-thoughtworks-penumarthi-jev-rag-pipelines.md).
- Several quotes are split mid-sentence in the page markup because inline links break the text. Where a quote stops short, the continuation is given in the assessment.
- Source is thin on evidence by design: it is an interview-style explainer. The Assayer should expect the confidence to be anecdotal throughout.
- Cross-referenced claim numbers were checked against the headings of the cited notes.
