---
source_url: https://newsletter.pragmaticengineer.com/p/the-revised-rules-of-engineering
source_type: blog-post
title: "The revised rules of engineering management with Will Larson"
author: Gergely Orosz (The Pragmatic Engineer), guest Will Larson (CTO, Imprint)
date_published: 2026-10-21
date_extracted: 2026-10-22
last_checked: 2026-10-22
status: current
confidence_overall: anecdotal
issue: "#4278"
---

# The revised rules of engineering management with Will Larson

> Podcast write-up in which Will Larson (CTO of Imprint) offers opinion, not data, that AI is pulling technical decision-making back to engineering managers, widening spans of control and making the tech-lead-manager role in demand; AI-specific content is only a few passages.

## Source Context

- **Type**: blog-post (podcast-episode write-up with takeaways and transcript)
- **Author credibility**: Gergely Orosz is the author of The Pragmatic Engineer. Will Larson is CTO at Imprint, previously CTO at Carta and Calm and an engineering leader at Stripe and Uber, and author of a book on engineering leadership. Credibility rests on their experience; there is no study, metric, or code.
- **Scope**: Mostly management history (Digg v4 rewrite, ZIRP-era norms, career ladders, CTO path), out of scope here. This note extracts only the AI-adjacent claims, all opinion or speculation.

## Extracted Claims

### Claim 1: AI is bringing technical decision-making back to engineering leadership, reversing the 2010s advice that managers should not make technical decisions
- **Evidence**: Larson's personal recollection of the advice he was given; Orosz says he got the same advice and that the "tide is very much changing". No data on how many companies have shifted.
- **Confidence**: anecdotal
- **Quote**: "One of the worst parts of being an engineering manager in the 2010s was when you joined the ranks of engineering management, one of the first lessons you’d get was: ‘you need to never make a technical decision again.’ That’s literally what I was told.”
- **Our assessment**: Plausible and consistent with other corpus notes on leaders returning to hands-on work, but the AI causal link is asserted only in the intro ("bringing technical decision-making back to leadership"), not demonstrated.

### Claim 2: More tech companies now expect managers to be hands-on and in the details
- **Evidence**: Orosz's observation; Larson hires managers who want to write software at Imprint.
- **Confidence**: anecdotal
- **Quote**: "The tide is very much changing these days, with more tech companies expecting managers to be hands-on and in the details."
- **Our assessment**: Reasonable directional signal; unquantified and not attributed specifically to AI in this passage.

### Claim 3: EM spans of control are growing from 4-8 to 12-14 reports, with Directors managing more TLMs, and the tech lead manager role is in demand
- **Evidence**: Larson/Orosz assertion, no dataset.
- **Confidence**: anecdotal
- **Quote**: "EMs are starting to manage 12-14 people, instead of 4-8, as before, while Directors are managing more TLMs."
- **Our assessment**: Matches the flattening trend in the career-break note (Claim 16), which is also anecdotal. The source does not tie the change to AI explicitly.

### Claim 4: Line management and software-writing tools are now good enough that hands-on management is more engaging, while bureaucracy tooling remains poor
- **Evidence**: Larson's personal experience after stepping back from a 250-person org at Carta to a 25-person tech org at Imprint.
- **Confidence**: anecdotal
- **Quote**: "line management can be a lot more engaging for executives these days because the tools for line management and the tools for writing software are really good"
- **Our assessment**: The quote above is a fragment of the longer sentence; confirm wording against the page. Single-person experience.

### Claim 5: AI has made some engineers more productive but less happy, and one engineer retired because AI destroyed the ability to be "in the flow"
- **Evidence**: A single secondhand anecdote.
- **Confidence**: anecdotal
- **Quote**: "Will knows someone who decided to retire from tech because AI has destroyed the ability to be “in the flow.” Engineers are being more productive, but enjoy it less."
- **Our assessment**: Interesting counterpoint to productivity narratives, but n=1 and secondhand. Treat as a hypothesis for the guide's adoption/wellbeing discussion, not evidence.

### Claim 6 (speculation): Agent loops could automatically mitigate expected on-call incidents
- **Evidence**: None. Orosz's explicitly labelled side note.
- **Confidence**: anecdotal
- **Quote**: "Could we design loops that automatically mitigate incidents that we expect and are well-prepared for?"
- **Our assessment**: A question, not a claim. Related practitioner reports of alert-triage loops exist in the loop-engineering note (Claim 7).

### Claim 7: Engineers on call for software they build produce more reliable software (context for Claim 6)
- **Evidence**: Larson's argument about 2010s practice of keeping the highest-paid engineers off on-call.
- **Confidence**: anecdotal
- **Quote**: "But when engineers are oncall for the software they build, it leads to better, more reliable software."
- **Our assessment**: Common industry view; relevant only as the premise for automating pages with agents without removing ownership.

## Concrete Artifacts

None. The source has no code, configs, metrics, or transcripts of AI workflows. Imprint is hiring EMs "to use agents to rethink how software teams work" (no detail given).

## Cross-References

- **Corroborates**: `blog-pragmaticengineer-orosz-engineering-leader-career-break.md` Claim 16 (flattening organizations, more direct reports per manager) and Claims 8-9 (leaders returning to hands-on work for AI relevance).
- **Contradicts**: None found. No contradiction issue filed.
- **Extends**: `blog-pragmaticengineer-orosz-loop-engineering.md` Claim 7 (loops used for alert triage before on-call engages): this adds the speculative on-call automation idea from the leadership side.
- **Novel**: The "engineers more productive but enjoy it less" flow anecdote and the framing of AI as reversing the "never make a technical decision" manager norm.

## Guide Impact

- **Chapter 05**: At most a brief management-side note: some leaders report managers are expected to be hands-on technically and to run larger spans, citing this source and the career-break note as anecdotal. Do not state it as established.
- **Chapter 00**: No change recommended.

## Extraction Notes

- Read the full page text (takeaways 1-12 and transcript header) via the fetched HTML. The Prospector's triage said to extract only AI-adjacent claims, so Digg, ZIRP, career-ladder, and CTO-path material was skipped.
- The source is thin on AI evidence, as triage predicted. All claims are anecdotal opinion.
