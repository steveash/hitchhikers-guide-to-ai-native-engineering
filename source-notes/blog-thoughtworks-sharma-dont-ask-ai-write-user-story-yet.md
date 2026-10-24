---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/dont-ask-ai-to-write-the-user-story-yet
source_type: blog-post
title: "Don’t ask AI to write the user story yet"
author: Himanshu Sharma (Thoughtworks)
date_published: 2026-10-22
date_extracted: 2026-10-24
last_checked: 2026-10-24
status: current
confidence_overall: anecdotal
issue: "#4305"
---

# Don’t ask AI to write the user story yet

> A Thoughtworks practitioner proposes a pre-drafting protocol for AI-assisted requirements: have the model sort inputs into Confirmed / Assumed / Unknown piles (with a source quote for every Confirmed item), settle the open decisions with stakeholders, and only then draft acceptance criteria from the agreed decision record — naming the failure mode "confident gaps".

## Source Context

- **Type**: blog-post (Thoughtworks Insights, Generative AI / Product innovation)
- **Author credibility**: Himanshu Sharma, Thoughtworks. The article carries only a byline; no biography or experience claims appear on the page. Thoughtworks Insights is an editorially curated, vendor-neutral channel. The Thoughtworks disclaimer states the views are the author's own.
- **Scope**: How to prepare requirements (user stories, acceptance criteria) with an LLM assistant: the confident-gaps failure mode, the three-pile sort, a three-question gap triage, fitting into refinement / Three Amigos / Example Mapping, and two reusable prompts. Does NOT provide metrics or measured results; the only evidence is one illustrative CSV/filtered-export example (plus a brief retail-returns example). It is explicitly labelled illustrative ("The entries below are illustrative").

## Extracted Claims

### Claim 1: AI turns a vague request into a polished user story instantly, but the polish hides unmade product decisions
- **Evidence**: Worked example: "Users should be able to export a filtered report." The author lists unanswered questions (what "filtered" means, which date, hidden columns). Illustrative, not measured.
- **Confidence**: anecdotal
- **Quote**: "None of these are writing problems. They’re product decisions, and someone has to make them."
- **Our assessment**: Plausible and consistent with experience; the reframing (the model's first job is finding undecided questions, not writing) is the useful part. No data on how often it occurs.

### Claim 2: "Confident gaps" — output sounds certain because the model quietly filled a hole the team never examined
- **Evidence**: Example: notes confirm CSV download, a date filter and authorized-record access, say nothing about duplicates; the draft adds "remove duplicate records", which "invented a business rule". One illustrative case.
- **Confidence**: anecdotal
- **Quote**: "I think of these as confident gaps: places where the output sounds certain because the model quietly filled a hole the team never looked at."
- **Our assessment**: A useful named failure mode, adjacent to hallucination but specific to under-specified inputs: the invention is plausible and domain-sensible, so review does not catch it. The guide has no name for this. Worth adding as a vocabulary item.

### Claim 3: Specific language is not validated language
- **Evidence**: Argument by example (the duplicates rule); the author notes the ambiguity "will resurface later in development or testing, where it costs more to settle" — an assertion, not measured.
- **Confidence**: anecdotal
- **Quote**: "AI is good at turning a vague request into specific language. That’s the problem: specific doesn’t mean validated."
- **Our assessment**: Compact statement of a real risk. The cost-escalation claim is conventional wisdom (late defect cost), not evidenced here.

### Claim 4: Ask for three piles (Confirmed / Assumed / Unknown), not a draft, and require a source quote for every Confirmed item
- **Evidence**: Prescribed method; inputs are the user's task, desired outcome, already-confirmed rules and source notes. Includes a four-column decision record (status / rule / owner / source / still open). Illustrative table.
- **Confidence**: emerging
- **Quote**: "It may label an assumption as “confirmed”, so ask it to quote the source line for every confirmed item."
- **Our assessment**: The quote-the-source requirement is the load-bearing control: it turns the model's self-classification into something checkable by grep. It mirrors the Miner/Assayer verbatim-quote discipline in this repo. Caveat: the author does not report how reliably models comply, and quotes themselves can be paraphrased — verification is still human.

### Claim 5: An AI suggestion stays an assumption until a stakeholder with the right context confirms it; instruct the model not to fill gaps
- **Evidence**: Prescriptive; example table row "AI suggestion; no supporting source" classified as Assumed.
- **Confidence**: anecdotal
- **Quote**: "That one instruction changes the whole output, from “here’s your story” to “here’s what you still need to find out”."
- **Our assessment**: Claim about instruction efficacy is untested but cheap to try. Fits the "ask, don't assume" / escalation boundary pattern in agent specs.

### Claim 6: Triage gaps with three questions — scope, who may do what, what the data/outcome means
- **Evidence**: Prescribed heuristic, illustrated with a retail "cancel a return" feature (courier already collected parcel; refund under way) cutting across UX, logistics and payments.
- **Confidence**: anecdotal
- **Quote**: "Could the answer change the scope?"
- **Our assessment**: The full triad (scope / permissions / meaning) is the quotable rule; it is a tidy prioritization filter that prevents "40 open questions" overload. Single-author heuristic, untested. Related quote: "A list of 40 open questions helps about as much as a story with 40 hidden assumptions."

### Claim 7: Humans still run the discussion; AI's role is to shape it, and nice-to-haves go in a separate pile to prevent scope creep
- **Evidence**: Prescriptive; example: an export request "shouldn’t quietly grow into scheduled reports, notifications and a new dashboard."
- **Confidence**: anecdotal
- **Quote**: "Keep nice-to-haves in their own pile, too."
- **Our assessment**: Sound. Note that the quoted sentence about discussion in the source is garbled ("A discussion is still just as important, what AI should do is shape it."), so we do not rely on it verbatim.

### Claim 8: AI-generated gap lists plug into existing refinement practices (refinement, Three Amigos, Example Mapping); concrete examples test the answers
- **Evidence**: Example: "If there are 20,000 matches and only 50 on screen, what should the file contain?" The author suggests a trial on one upcoming requirement, noting which questions were useful, which noise, and review time.
- **Confidence**: anecdotal
- **Quote**: "An AI review can help prepare for those conversations."
- **Our assessment**: Good bridge between AI tooling and established agile technique; the proposed self-evaluation (useful vs noise, time cost) is a sensible lightweight experiment but yields no data in this article.

### Claim 9: Write the story last — record the agreed rule, owner, source and what's open, then draft acceptance criteria from that record, each linked to its decision
- **Evidence**: Prescriptive sequencing; example: reporting team confirms exports include all matching authorized records and only user-selected columns. Date boundaries and access rules "still need their own definitions".
- **Confidence**: emerging
- **Quote**: "Only then ask AI to draft acceptance criteria, and draft them from that record."
- **Our assessment**: This is spec-driven development with an explicit decision gate before generation. Complements, rather than competes with, Osmani's specify→plan→tasks flow by inserting a human-confirmation stage at the "specify" step.

### Claim 10: The decision record is often worth more than the story, since it lets teams revisit decisions when requirements change
- **Evidence**: Assertion; no case study.
- **Confidence**: anecdotal
- **Quote**: "That small decision record often ends up worth more than the story."
- **Our assessment**: Plausible (ADR-style rationale capture). Nice framing for durable context artifacts in Ch04.

### Claim 11: Accountability stays with the human analyst; use an approved AI environment and share only cleared data
- **Evidence**: Closing guidance.
- **Confidence**: settled (conventional governance advice)
- **Quote**: "The analyst still owns the result, questions and draft alike."
- **Our assessment**: Standard, but worth echoing alongside the data-handling caveat.

## Concrete Artifacts

Prompt 1 (pre-drafting review), verbatim from the source:

```
Review these notes using only the evidence supplied. Separate confirmed requirements, assumptions and unknowns. For each missing decision, explain its consequence and suggest a question for the relevant stakeholder. Keep optional enhancements separate. Do not invent business rules or write final acceptance criteria.
```

Prompt 2 (after decisions are confirmed), verbatim from the source:

```
Draft acceptance criteria from these confirmed decisions. Link each criterion to the decision behind it and list any unresolved dependencies.
```

Decision record table (source's illustrative example, reformatted; columns: Status | Rule or question | Decision owner | Source | Still open):

```
Confirmed | The export must be a CSV file.                                      | Product owner                 | Approved requirement notes | Nothing for file format.
Assumed   | The export includes all matching records, rather than just the visible page. | Product owner to confirm | AI suggestion; no supporting source | Which records should be included?
Unknown   | Should duplicate-looking rows be removed?                           | Business/data owner to confirm | Not covered in the notes | What counts as a duplicate, and could removing it lose information?
```

Three-question gap triage (paraphrased list of the source's three questions: could the answer change the scope; who is allowed to do what; what the data or outcome actually means).

## Cross-References

- **Corroborates**: `blog-osmani-good-spec.md` Claim 4 (agent files fail by being too vague) and Claim 7 (iterate on the spec interactively before implementation) — Sharma applies the same "resolve ambiguity before generation" idea to product requirements rather than agent instructions.
- **Contradicts**: None found. No filed contradiction.
- **Extends**: `blog-osmani-good-spec.md` Claim 6 (Specify → Plan → Tasks → Implement) by adding an explicit Confirmed/Assumed/Unknown gate inside the Specify phase. `blog-thoughtworks-shah-ai-makes-agile-alive.md` Claim 9 (backlog preparation and agile practices adapt, with customer collaboration/discovery staying important) with a concrete refinement technique. `blog-thoughtworks-malykhin-quantifying-ai-adoption.md` Claim 5 (heavy spec frameworks add overhead) is a related tension: Sharma's decision record is deliberately lightweight (a short table), consistent with preferring small specs.
- **Novel**: The "confident gaps" name; the three-pile sort with mandatory source quote; the scope/permission/meaning gap-triage test; the decision-record-first sequencing; the two reusable prompts. No existing note covers requirements elicitation with assumption marking.

## Guide Impact

- **Chapter 00** (Specification Quality Is the New Leverage Point, `guide/00-principles.md` ~L75): add "confident gaps" as a named failure mode — a plausible, specific, unvalidated rule invented by the model to fill an unexamined hole — citing this source (anecdotal grade; single illustrative example).
- **Chapter 04** (`guide/04-context-engineering.md` ~L260, "cheapest spec that conveys intent unambiguously"): add the Confirmed/Assumed/Unknown pattern with source-quote requirement as a technique for grounding requirement work, and the decision record as a compact durable context artifact.
- **Chapter 05** (team adoption): mention using AI-generated gap lists as input to Three Amigos / Example Mapping sessions, with the author's suggested one-requirement trial. Keep humans as decision owners.
- Present as a method from a practitioner, not as evidenced effect size.

## Extraction Notes

- Read the full article (fetched HTML directly; WebFetch only returned a summary, so quotes were copied from the raw page text). No sub-pages followed; the article has none beyond related-article teasers.
- No metrics, code, or measured results exist. All examples are explicitly illustrative; confidence_overall is therefore `anecdotal`.
- The source contains a garbled sentence ("A discussion is still just as important, what AI should do is shape it."); quoted nowhere as a key claim.
- Claim 6's Quote field shows only the first of the three questions; the others are listed in Concrete Artifacts and Our assessment.
