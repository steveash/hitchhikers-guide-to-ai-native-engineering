---
source_url: https://www.thoughtworks.com/insights/articles/sovereign-ai--practical-approach-to-models-infrastructure-and-control
source_type: blog-post
title: "Sovereign AI: A practical approach to models, infrastructure and control"
author: Liu Shangqi (Thoughtworks)
date_published: 2026-11-17
date_extracted: 2026-11-18
last_checked: 2026-11-18
status: current
confidence_overall: anecdotal
issue: "#4801"
---

# Sovereign AI: A Practical Approach to Models, Infrastructure and Control

> Thoughtworks practitioner article proposing a per-workload "must control / should control / can rent" triage, applied across context, model and infrastructure layers, with a "map your dependencies, then test one fallback" procedure; evidence is the author's own experience, not measured data.

## Source Context

- **Type**: blog-post (Thoughtworks Insights article, topics: Technology strategy, Generative AI; from trusted feed `thoughtworks`).
- **Author credibility**: Liu Shangqi, Tech Principal of Thoughtworks APAC. Writes as a practitioner describing Thoughtworks' own internal setup.
- **Scope**: Enterprise decision framework for AI sovereignty. Does not give metrics, dates, or task definitions for its practitioner claims.

## Extracted Claims

### Claim 1: Sovereignty analysis should start from risk, and a concrete tool-switch showed that replacing a vendor costs more than a new subscription
- **Evidence**: Anecdote: a team using Cursor hit a pricing change; alternatives (GitHub Copilot, Claude Code) existed but switching was hard. No figures given.
- **Confidence**: anecdotal
- **Quote**: "We had alternatives, including GitHub Copilot and Claude Code, but switching took more than a new subscription."
- **Our assessment**: Plausible and consistent with the lock-in theme, but a single unquantified anecdote. The article does not (in what we could retrieve) spell out here which assets made switching hard; the later context-layer section implies skills, evals and integrations.

### Claim 2: The right level of control depends on the workload and the risk being protected, so portability is not the same as sovereignty
- **Evidence**: Reasoning plus a retailer example (cost concentration may be the main risk rather than physical control).
- **Confidence**: emerging
- **Quote**: "A system can be portable and still not sovereign enough for a particular workload."
- **Our assessment**: Useful distinction; it refines the "design for mobility" advice in existing notes by saying mobility alone does not satisfy every workload.

### Claim 3: Triage each workload into must control / should control / can rent, rather than writing one organization-wide policy
- **Evidence**: Described as the authors' own practice; no worked table of examples retrieved beyond general-purpose inference and cloud compute landing in "rent".
- **Confidence**: emerging
- **Quote**: "We look at each workload rather than write a single sovereignty policy for the whole organization."
- **Our assessment**: The central contribution. It parallels the per-workload rent-vs-own grid in the Nolan note but is simpler (three buckets, no scoring questions).

### Claim 4: Sovereignty should be mapped across three layers (context, model, infrastructure), starting with context; the harness assets are the portable layer
- **Evidence**: Framework assertion; the context layer covers proprietary knowledge, prompts, evaluations, and policies.
- **Confidence**: emerging
- **Quote**: "An enterprise harness brings together reusable agent skills, integrations, guardrails and evaluations."
- **Our assessment**: Directly relevant to Ch02/Ch04: keeping skills, evals, guardrails and connectors as shared assets independent of any one model is what makes model swaps feasible. Not independently validated.

### Claim 5: A practical multi-model setup routes most traffic to commercial frontier models and some to self-hosted open-weight models through an agentic gateway
- **Evidence**: Author's internal experience; GLM 5.3 is cited as capable of everyday coding tasks at lower inference cost, per internal evaluations, with no numbers, tasks or dates.
- **Confidence**: anecdotal
- **Quote**: "an agentic gateway that routes requests between commercial frontier models and self-hosted open-weight alternatives."
- **Our assessment**: Do not treat the GLM 5.3 cost/performance statement as a benchmark. The architecture (gateway plus tested fallback) is the transferable part and matches the Nolan and Gall notes. The article also says "Most traffic still goes to commercial providers", i.e. self-hosting is a fallback/option, not the default.

### Claim 6: Accountability for third-party AI does not require self-hosting
- **Evidence**: Argument; a managed service may give sufficient control for some workloads.
- **Confidence**: emerging
- **Quote**: "Accountability for third-party AI doesn't mean you have to self-host it."
- **Our assessment**: Sensible and relevant to Ch06 (third-party accountability); tempers the stronger self-host advice in the Vega note.

### Claim 7: Owning more costs more: self-hosting needs more than GPUs, and low utilization makes owned infrastructure more expensive than rented
- **Evidence**: Assertion, no cost model given.
- **Confidence**: emerging
- **Quote**: "Low utilization can make owned infrastructure considerably more expensive than rented capacity."
- **Our assessment**: Corroborated by Nolan Claim 8 (utilization determines whether dedicated capacity wins) and Gall Claim 6 (talent requirements). Here it is stated, not demonstrated.

### Claim 8: The recommended procedure is to map AI dependencies and who controls each, then test one fallback
- **Evidence**: Prescriptive conclusion.
- **Confidence**: emerging
- **Quote**: "Then test one fallback to confirm it works when circumstances change."
- **Our assessment**: Low-cost, actionable, and consistent with the guide's verification mindset: an untested fallback is not a fallback.

## Concrete Artifacts

```
Framework (Shangqi, Thoughtworks Insights, 2026-11-17), paraphrased structure:
Per workload: must control | should control | can rent
Layers: context (knowledge, prompts, evals, policies)
        model (proprietary vs open-weight, portability)
        infrastructure (owned vs rented compute)
Procedure: map AI dependencies and controllers -> test one fallback
Article section headings: "Start with the risk, not the architecture";
"Decide what you must control, what you should control and what you can rent";
"The cost of owning more"; "Making sovereignty a deliberate choice"
```

## Cross-References

- **Corroborates**: `blog-thoughtworks-nolan-renting-the-frontier.md` Claim 2 (decide per workload what to rent vs own) and Claim 8 (utilization drives owned-vs-rented economics); `blog-thoughtworks-gall-commodity-illusion-compute-geopolitics.md` Claim 10 (design for mobility) and Claim 6 (self-hosting needs scarce talent); `blog-thoughtworks-kamelman-sovereign-ai-dependency.md` Claim 1 (sovereignty differs from resilience).
- **Contradicts**: None found. The Vega note's Claim 8 pushes toward open-weight/local, whereas this article says most traffic stays commercial; this is a difference of emphasis and context, not a filed contradiction.
- **Extends**: `blog-thoughtworks-vega-token-billing-lockin.md` Claim 8 (countermeasures to lock-in) with a graded, per-workload alternative.
- **Novel**: The three-bucket must/should/rent triage and the context/model/infrastructure layer map; "test one fallback" as the minimum action.

## Guide Impact

- **Chapter 05**: In the vendor/model dependency discussion, add the "map dependencies, test one fallback" step as a minimal practice, cited alongside the Kamelman and Nolan notes.
- **Chapter 02**: Note that enterprise harness assets (skills, evals, guardrails, connectors) kept model-independent are what make a model swap or gateway routing practical (Claim 4); treat as emerging.
- **Chapter 06**: Third-party AI accountability does not imply self-hosting (Claim 6); pair with data-residency per workload.
- **Chapter 04**: Context-layer assets as the sovereignty-critical layer; low-confidence support only.

## Extraction Notes

- The fetch tool returned a summary and selected verbatim quotes rather than the full text; all quotes above were returned as exact sentences, but the full article was not read end to end. The Assayer should verify quotes against the URL.
- The GLM 5.3 and Cursor claims are anecdotal and carry no metrics; per triage they are not used as evidence.
- No contradiction issue was filed.
