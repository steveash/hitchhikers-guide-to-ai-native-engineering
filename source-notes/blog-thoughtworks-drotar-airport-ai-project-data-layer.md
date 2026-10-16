---
source_url: https://www.thoughtworks.com/insights/blog/technology-strategy/the-real-ai-project-at-your-airport-isnt-an-ai-project
source_type: blog-post
title: "The real AI project at your airport isn't an AI project"
author: Robert Drotar
date_published: 2026-10-14
date_extracted: 2026-10-16
last_checked: 2026-10-16
status: current
confidence_overall: anecdotal
issue: "#4160"
---

# The real AI project at your airport isn't an AI project

> A short Thoughtworks opinion piece that gives a concrete, domain-specific failure mode for agents on fragmented data (an agent acting on the first-queried of several disagreeing sources, with the error looking like a normal decision) and a budget-politics argument for why the unglamorous data-consolidation work must come before agentic AI.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, "Data strategy" blog, published October 14, 2026; discovered via trusted feed `thoughtworks`).
- **Author credibility**: Robert Drotar, Thoughtworks. The page includes the disclaimer that statements are the author's and not necessarily Thoughtworks' positions. No bio or credentials beyond the byline were visible on the page.
- **Scope**: Airport operations (AODB, A-CDM, operations plan). An argument piece with one hypothetical scenario and three vendor/airport announcements as illustration. No metrics, no measured agent deployments, no code. The Skytrax-ranking section is supporting colour and is not extracted as a claim.

## Extracted Claims

### Claim 1: Dashboards tolerate fragmented data because humans reconcile it; agents cannot, so the unification is an architectural prerequisite, not something a maturity curve delivers over time
- **Evidence**: Argument by analogy (a person checking three screens vs. an agent). No data.
- **Confidence**: anecdotal
- **Quote**: "The reason is architectural, not something you age into with a maturity curve."
- **Our assessment**: Plausible and consistent with our corpus, but asserted rather than demonstrated. The useful framing is that fragmentation which is harmless for human-read dashboards becomes a correctness problem once an agent acts on it.

### Claim 2: An agent will act confidently on whichever version of reality it queried first, and the resulting failure looks like a normal, well-reasoned decision
- **Evidence**: Hypothetical scenario: AODB shows a gate free while the fresher A-CDM feed shows the previous aircraft still there; the agent dispatches a ground crew to an occupied gate.
- **Confidence**: anecdotal
- **Quote**: "It will act, confidently and immediately, on whichever version of reality it queried first."
- **Our assessment**: A clear statement of a silent-failure mode: no error is raised, so nothing triggers review. The scenario is illustrative, not an observed incident; "first queried" is a simplification (an agent could be built to cross-check sources), which is exactly the mitigation the piece does not discuss.

### Claim 3: The sources disagree structurally because they are owned by different organizations with different incentives and cadences, so this is an ownership problem, not just a freshness problem
- **Evidence**: Description of AODB (airport IT estate), A-CDM (joint construct fed by airlines, ground handlers, ATC, owned by none), and the operations plan (assembled from whatever each side agreed to share).
- **Confidence**: anecdotal
- **Quote**: "these three systems aren't just out of sync, they're owned by different organizations with different incentives to keep them current."
- **Our assessment**: The most generalisable point: cross-organisational data without a single accountable owner cannot be fixed by a sync job. It maps to any multi-party enterprise integration.

### Claim 4: Agent errors on a bad base-layer read compound across multi-step actions instead of staying contained like one human's mistake
- **Evidence**: Hypothetical: one agent asked to act across ground handling, gate reassignment and passenger flow produces three bad calls from one bad read.
- **Confidence**: anecdotal
- **Quote**: "a bad read at the base layer produces three bad calls simultaneously, each built on top of the last, before anyone downstream has a chance to notice something's off."
- **Our assessment**: Reasonable, and an argument for scoping agent actions narrowly until the data is trustworthy. Unevidenced.

### Claim 5: Data consolidation loses internal budget fights to agentic demos, even though it is the real prerequisite
- **Evidence**: Author's observation of internal pitch dynamics; no survey or case data.
- **Confidence**: anecdotal
- **Quote**: "This is the least fundable-sounding project in the building."
- **Our assessment**: Believable and a useful organisational-politics framing, but it is opinion. Note the author's firm sells this kind of consulting.

### Claim 6: Skipping the data layer yields a result that looks identical in the demo but fails when the agent is given something that matters
- **Evidence**: Assertion.
- **Confidence**: anecdotal
- **Quote**: "they're choosing a destination that looks identical in the demo and falls apart the first time the agent is handed something that actually matters."
- **Our assessment**: A good one-line statement of the demo-vs-production gap. No evidence beyond the argument.

### Claim 7: Industry leaders are consolidating operational data onto single platforms first, and announcements led with the shared picture rather than AI
- **Evidence**: Three announcements cited: Heathrow (multi-year deal, March, to replace its operational database and run A-CDM and operations plan on one platform), Melbourne Airport (platform live, February), GMR Hyderabad (single platform, December 2024). We did not verify these.
- **Confidence**: anecdotal
- **Quote**: "The early movers have decided. The open question is everyone else."
- **Our assessment**: Illustrative only; per triage, not a claim we verify. Announcements show direction, not outcomes.

## Concrete Artifacts

No code or configs. The one concrete artifact is the failure scenario, quoted from the source:

```
If the AODB shows a gate as free while A-CDM's fresher feed shows the previous aircraft still on the ground, it won't hesitate ...
(Drotar, Thoughtworks Insights, 2026-10-14)
```

Closing diagnostic question from the source: whether anyone can give "a straight, confident answer to what your airport's own operational picture actually is, right now, without three people checking three different screens first."

## Cross-References

- **Corroborates**: `blog-fowler-sadalage-chandrasekaran-ai-ready-data.md` Claim 2 (stale-price scenario: agent executes perfectly yet gives a confidently wrong outcome because the failure is in the data) and Claim 16 (the layers are dependency-ordered, with readiness capped by the weakest foundation). `blog-thoughtworks-patole-context-real-bottleneck-ai-agents.md` Claim 6 (data silos create competing versions of truth) and Claim 2 (plausible-looking wrong outputs defeat review). `blog-thoughtworks-kantrod-data-modernization-guide.md` Claim 14 (agentic automation is safe only after quality and governance work, a prerequisite chain).
- **Contradicts**: None found.
- **Extends**: Fowler et al. Claim 2 by adding a multi-source variant: two live sources that disagree (rather than one stale source), with the agent choosing by query order, and a cross-organisational ownership cause. Also extends the same notes with the budget-politics framing.
- **Novel**: (a) the "first-queried source wins" silent-failure mode with multiple disagreeing systems of record; (b) the ownership-and-incentive explanation for why feeds are out of sync; (c) compounding errors across chained actions from one bad read; (d) the demo-vs-consolidation funding dynamic.

## Guide Impact

- **Chapter 02 / data-readiness material**: could add the multi-source-conflict failure mode as a second example next to the stale-price scenario cited from the Fowler et al. note, flagged as a single-author, unmeasured illustration.
- **Chapter 04 (context engineering)**: supporting example that when several systems of record disagree, the context layer needs an explicit source-precedence/ownership rule, not agent discretion. This is our inference; the source does not propose a mechanism.
- **Low priority overall**: no new pattern or evidence. Treat as a cite-able illustration only.

## Extraction Notes

- Full article read (about 900 words; no sub-pages). WebFetch only returned a summary, so the text was read from the raw HTML and quotes copied from it.
- Quotes verified against the page text. Skytrax ranking section deliberately not extracted per triage.
- Cross-referenced claim numbers were checked against the headings in each cited note.
