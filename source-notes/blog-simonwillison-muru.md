---
source_url: https://simonwillison.net/2026/Nov/21/muru/
source_type: blog-post
title: "Muru"
author: Simon Willison (linking to Graham Dumpleton)
date_published: 2026-11-21
date_extracted: 2026-11-22
last_checked: 2026-11-22
status: current
confidence_overall: anecdotal
issue: "#4894"
---

# Muru

> A link post pointing to Graham Dumpleton's day-by-day build log of Muru, an AI-assisted Rust ASGI/WSGI server, whose practitioner claim is that AI does the surface work while judging what "isn't good enough yet" stays with the human.

## Source Context

- **Type**: blog-post (link-blog entry, with primary-source follow-up of two Dumpleton posts: "AI as a lifestyle choice" and "A first look at Muru")
- **Author credibility**: Simon Willison is a widely read LLM-tooling commentator. Graham Dumpleton is the creator of mod_wsgi with ~20 years of Python web-hosting experience. Both claims are practitioner self-report.
- **Scope**: The Willison page contains one substantive quote and a list of Dumpleton posts (17 posts, 4-21 Nov 2026). The two primary posts were read for this note. The other 15 were not mined (out of scope per triage). Muru's design posts say nothing about AI; the AI-workflow content is concentrated in "AI as a lifestyle choice".

## Extracted Claims

### Claim 1: The human keeps the judgment about when output is not yet good enough, even when AI does most of the visible work
- **Evidence**: Single-practitioner statement; Dumpleton is building Muru with AI and publishing the process.
- **Confidence**: anecdotal
- **Quote**: "The AI may be doing a lot of the work on the surface, but deciding what isn't good enough yet is still down to me" (Dumpleton, "AI as a lifestyle choice", as quoted on the Willison page)
- **Our assessment**: Useful concise framing of where human judgment sits. Note the wording is "isn't good enough yet" (iterative rejection), not "what is good enough". Matches Willison's own position but offers no verification method.

### Claim 2: AI removes the grunt work, leaving the author the ideas and satisfaction of making
- **Evidence**: Personal experience; he is on sabbatical building software most days.
- **Confidence**: anecdotal
- **Quote**: "The making of things was always the point though, not the typing."
- **Our assessment**: Motivational/experiential claim; supports a "delegate typing, keep design" division of labour but is not testable.

### Claim 3: AI-generated output starts rough and is refined iteratively (dorodango analogy)
- **Evidence**: Analogy to his own early mod_wsgi code; no artefacts shown in this post.
- **Confidence**: anecdotal
- **Quote**: "It starts out as a crude lump of mud."
- **Our assessment**: Consistent with iterate-and-review workflows; dismissing output as "slop" without reading is, per the post, a critic's failure. Our view: plausible, but the post gives no review criteria.

### Claim 4: Owning AI-generated code means taking responsibility and not pushing it onto maintainers
- **Evidence**: Stated policy for the project, including asking users to describe problems rather than send patches.
- **Confidence**: anecdotal
- **Quote**: "If Muru has problems, they are my problems."
- **Our assessment**: Accountability stance. Related quote: "So don't send me a patch, just describe the problem." Interesting policy for AI-era open source maintenance: issue descriptions are the input, the maintainer's own agent loop produces fixes.

### Claim 5: Async delegation fits AI around daily life (start a task, walk away, return to review)
- **Evidence**: Personal workflow description.
- **Confidence**: anecdotal
- **Quote**: "set something going, then head out for a walk, do some gardening, or deal with whatever else needs"
- **Our assessment**: Corroborates the background-agent working pattern; no data on failure rate or review cost.

### Claim 6: Planning came first, and explaining features publicly acts as a design test
- **Evidence**: Per the post, a few days of thinking before code, then near-daily development; posts and workshops used to check a feature can be explained simply.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The build log as a review artefact (if you can't explain it simply, the design is likely flawed) is a novel verification-adjacent practice, but it's the author's description, not demonstrated.

### Claim 7: Muru's design makes worker crashes and bad releases non-fatal (reloads start a whole new host and workers beside the old ones)
- **Evidence**: Walkthrough of dev-mode behaviour in "A first look at Muru"; no AI content.
- **Confidence**: anecdotal (alpha software; demonstrated by author's own run, not independently verified)
- **Quote**: "An exception raised by your code results in a failed request, but never a dead process."
- **Our assessment**: Concrete product claims, only tangential to the guide. Supporting quote: "Muru is still in alpha, with only pre-releases available" - treat all as unproven. Shows AI-built infrastructure with explicit design invariants (fork-safety check at import: "Muru checks for this when it does the import, before any workers are forked").

## Concrete Artifacts

```
# From "A first look at Muru" (Dumpleton, 2026-11), process steps as described:
uv tool install muructl
muructl run app:application
```

No code, config, metrics or failure data appear on the Willison page itself.

## Cross-References

- **Corroborates**: `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 9 (experienced engineers remain the value driver because AI amplifies expertise); `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` Claim 4 (decide-execute-deliver sandwich: AI compresses the middle, human keeps outer layers) and Claim 7 (verifying and being accountable resists automation).
- **Contradicts**: None found.
- **Extends**: `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` with a named practitioner on a production-infrastructure project.
- **Novel**: Build-log/public-explanation as a design-validation practice; "describe the problem, not a patch" contribution policy for an AI-built project; the Dumpleton/Muru series itself (no prior note).

## Guide Impact

- **Chapter 00 (principles)**: Could cite Claim 1 as a practitioner formulation that humans keep the "not good enough yet" judgment. Weak evidence (anecdotal); use as illustration only.
- **Chapter 01 (daily workflows)**: Claims 5 and 6 are minor examples of async delegation and plan-first-then-build; no new guidance.
- **Chapter 03 (verification)**: Nothing concrete; publishing an explanation as a design check (Claim 6) is a candidate idea if corroborated elsewhere.
- Recommend mining "AI as a lifestyle choice" as its own source only if more evidence is wanted.

## Extraction Notes

- The Willison page is a thin link post. I fetched and read two primary posts ("AI as a lifestyle choice", "A first look at Muru") and checked every quote above against the raw HTML of those pages; not followed: the 15 other posts.
- The triage comment paraphrased the quote as "what is good enough"; the actual text is "what isn't good enough yet".
- "A first look at Muru" contains no mention of AI.
- Triage comments' suggestion of "Muru: import once, fork many" and "releases, not restarts" posts were not read in full.
