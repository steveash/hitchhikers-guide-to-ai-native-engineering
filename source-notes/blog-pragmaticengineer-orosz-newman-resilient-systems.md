---
source_url: https://newsletter.pragmaticengineer.com/p/building-resilient-systems-with-sam
source_type: blog-post
title: "Building resilient systems with Sam Newman"
author: Gergely Orosz, featuring Sam Newman (The Pragmatic Engineer podcast)
date_published: 2026-10-07
date_extracted: 2026-10-08
last_checked: 2026-10-08
status: current
confidence_overall: anecdotal
issue: "#3985"
---

# Building resilient systems with Sam Newman

> Opinion-level podcast takeaways from Sam Newman on AI-era practice: resist "cognitive surrender", hedge across AI vendors/models and prefer deterministic code where possible, confine AI to human-designed module boundaries, and treat LLMs as non-world-models whose guardrails are not a long-term fix.

## Source Context

- **Type**: blog-post (podcast episode show notes with numbered takeaways, ~1:58 audio; Pragmatic Engineer, 2026-10-07)
- **Author credibility**: Gergely Orosz writes The Pragmatic Engineer. Sam Newman is the author of *Building Microservices* and *Building Resilient Distributed Systems* and a former Thoughtworks consultant. Strong distributed-systems credentials; the AI remarks are opinion, not measured research.
- **Scope**: The page contains intro, 12+ numbered takeaways, timestamps and links, not the full transcript. Most content is general distributed-systems/microservices/resilience material (out of scope per triage). This note covers only the AI-specific takeaways (9-12) plus the code-as-side-effect-of-collaboration takeaway (8). Timestamps list "AI and resilience" (1:32:42), "AI's limitations and where to use it" (1:36:26), "Cognitive debt and cognitive surrender" (1:40:06) and "Modular architecture and AI software factories" (1:45:02); these segments were not available as text, so claims rest on Orosz's written summary.

## Extracted Claims

### Claim 1: Heavy AI use is adding context switching and longer hours rather than freeing time for critical thinking ("cognitive surrender"), but Newman attributes this to how AI is used, not to AI itself
- **Evidence**: Newman's stated belief plus an unspecified reference to studies on working hours ("we've got studies that show this"); no study is cited on the page.
- **Confidence**: anecdotal
- **Quote**: "It’s just how we’re using it."
- **Our assessment**: Consistent with the cognitive-debt thread already in the corpus. Useful as an attributed framing, weak as evidence: the "studies" are uncited. Newman explicitly hedges ("or could we be using it wrong?"), so don't present it as a settled finding.

### Claim 2: Putting in manual verification effort often leads to better results than trusting AI output
- **Evidence**: One anecdote: while writing *Building Resilient Distributed Systems*, Newman used NotebookLM for research but manually clicked through every link it surfaced and checked whether it was information he wanted to reference.
- **Confidence**: anecdotal
- **Quote**: "Putting in the effort often leads to better results."
- **Our assessment**: A small, concrete, low-cost habit (verify each AI-surfaced citation) that is the stated remedy for cognitive surrender. Single-person anecdote with no measurement of the benefit.

### Claim 3: Systems integrating AI should hedge vendors: be multi-vendor and multi-model so the vendor/model layer is easy to change
- **Evidence**: Reasoning only: it is hard to tell which AI companies have sustainable business models. No data.
- **Confidence**: emerging
- **Quote**: "Aim to be multi-vendor, multi-model in your choices, so you can easily change the vendor or model layer."
- **Our assessment**: Plausible and aligned with several corpus notes, but the rationale here is business-model viability, whereas other notes emphasise sovereignty, cost and capability. Different motivation, same architecture advice.

### Claim 4: Consider replacing LLM-powered functionality with deterministic code that runs faster and cheaper
- **Evidence**: Assertion; no example or measurement.
- **Confidence**: anecdotal
- **Quote**: "Also, consider if you can swap out LLM-powered functionality for deterministic code that runs faster and cheaper."
- **Our assessment**: Sound engineering heuristic and a counterweight to LLM-everywhere designs. Note it is phrased as "consider", not as a rule.

### Claim 5: For AI-assisted work, design module boundaries first and let AI roam freely only inside that structure
- **Evidence**: Newman's answer to Orosz's question about how to get better at designing systems. No case study on the page; the related segment ("Modular architecture and AI software factories") is listed in timestamps only.
- **Confidence**: anecdotal
- **Quote**: "Start by thinking carefully about module boundaries and the connections between them"
- **Our assessment**: A clear, memorable statement of architecture-as-harness. Record as a design-first practice rather than a new pattern; it echoes existing harness advice without adding evidence.

### Claim 6: LLMs are not world models and have no concept of causality, which explains failures such as an LLM deleting a database, and means guardrails are not the right long-term solution
- **Evidence**: Newman's argument from the nature of LLMs; Orosz adds a topical example (an Opus 5.5 run with `--dangerously-skip-permissions` reportedly formatting a developer's C: drive, sourced to an X screenshot, not independently verified).
- **Confidence**: anecdotal
- **Quote**: "LLMs are not world models."
- **Further quote**: "But the nature of LLMs is why all the guardrails around LLMs are really not going to be the right long-term solution."
- **Our assessment**: Principle-level opinion, not measured. The claim that guardrails are not a long-term fix is in tension with the guide's reliance on permissions/hooks/sandboxes as the practical answer; but Newman offers no alternative beyond the module-boundary and determinism advice, so treat it as a caution about over-trusting guardrails, not a reason to drop them.

### Claim 7: Typing code is an output, not an outcome; with LLMs removing typing as the main time sink, the next bottleneck may be delayed feedback cycles
- **Evidence**: Thoughtworks anecdote: clients refused pair programming because one person appeared idle; Fowler's dictum "programming is not typing" helped explain the value.
- **Confidence**: anecdotal
- **Quote**: "Could it be delayed feedback cycles?"
- **Our assessment**: Speculative (posed as a question). Interesting as a hypothesis for the next bottleneck; matches the corpus theme that verification and review, not generation, are now the constraint.

## Concrete Artifacts

```
Takeaway 9/10/11/12 headings (Pragmatic Engineer page, 2026-10-07):
9. Hedging the vendor options is sensible when integrating AI into systems.
10. We must resist “cognitive surrender” to AI.
11. Starting with modules encourages better software architecture. Also: production is truth.
12. Much of the tech world might still be naive about what an LLM is.
```

```
Newman's advice for getting better at designing systems (Takeaway 11):
- Start by thinking carefully about module boundaries and the connections between them
- When you use AI, allow it to roam freely, but only inside the module structure that you have designed!
```

No code, metrics or configs in the source.

## Cross-References

- **Corroborates**: `blog-thoughtworks-gall-kimi-k3-multi-model-era.md` (Claim 4, multi-model routing pattern; Claim 11, hybrid/multi-model systems) for vendor/model hedging. `blog-thoughtworks-gall-kimi-k3-multi-model-era.md` Claim 9 (defense-in-depth is foundational) is related to the guardrail discussion. `blog-addyosmani-human-judgment-relocates.md` (Claim 5, cognitive bandwidth does not scale with parallel agents; Claim 13, could not explain approved code) and `blog-simonwillison-litt-understand-to-participate.md` (Claim 1, understanding drifting from the code; Claim 2, understanding enough to participate) for the cognitive-surrender/debt theme. `blog-fowler-fragments-2026-10-04.md` (Claim 1, "nurturing" an inferential system rather than building a deterministic one) is adjacent to the determinism point.
- **Contradicts**: None filed. Claim 6's "guardrails ... not going to be the right long-term solution" sits in tension with guardrail-centric advice, but it is an unsupported opinion with no concrete opposing claim to file as a contradiction.
- **Extends**: `blog-simonwillison-not-locked-in.md` (Claim 5-6, switching cost/exit path as a decision factor) with a vendor-viability rationale. `blog-pragmaticengineer-orosz-osmani-career.md` as same-publisher adjacent coverage.
- **Novel**: The explicit "module boundaries first, AI roams only inside" formulation; "LLMs are not world models / no causality" as an explanation for destructive-action failures; "replace LLM calls with deterministic code" as a design heuristic; NotebookLM per-link manual verification as a concrete anti-surrender habit.

## Guide Impact

- **Chapter 00**: Could cite Newman as an attributed, opinion-level voice for "cognitive surrender" with the "how we use it, not AI itself" caveat; mark evidence level anecdotal (studies uncited).
- **Chapter 02**: Optional supporting citation for module boundaries as the unit of AI autonomy ("roam freely, but only inside the module structure"); and for preferring deterministic code over LLM calls where feasible. Do not use as evidence that guardrails should be dropped.
- **Chapter 05**: Vendor/model hedging could add vendor-viability as a motivation alongside sovereignty/cost, citing this note and the Kimi K3 note.

## Extraction Notes

- Fetched the page (HTML to text) and read the full takeaways, intro, timestamps and links. The page has no transcript, so segment-level quotes beyond Orosz's written takeaways were unavailable.
- Per triage, microservices history, the three distributed-systems rules, idempotency keys vs fingerprints, the resiliency concepts and the fail-open/closed discussion were deliberately not mined; fail-open/closed appears only in the intro and timestamps, with no detail to extract.
- The Opus 5.5 drive-format anecdote is Orosz's editorial addition citing an X post, not Newman's claim, and was not verified.
- Newman's recommended reading includes Margaret Storey's cognitive-debt post (margaretstorey.com/blog/2026/02/09/cognitive-debt) and the earlier Beyond Vibe Coding with Addy Osmani episode; neither was followed.
