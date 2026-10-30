---
source_url: https://newsletter.pragmaticengineer.com/p/software-engineering-at-google-and
source_type: blog-post
title: "Software engineering at Google & CS education with Titus Winters"
author: Gergely Orosz (The Pragmatic Engineer), interviewing Titus Winters
date_published: 2026-10-29
date_extracted: 2026-10-30
last_checked: 2026-10-30
status: current
confidence_overall: anecdotal
issue: "#4437"
---

# Software engineering at Google & CS education with Titus Winters

> A podcast companion post with 12 takeaways: Google's pre-LLM 250M-line refactor method, the 2007 mandatory-tests rule, the readability program, and Winters' anecdotal report that AI-era code output is up while outages rise ~30% and shipped features stay flat.

## Source Context

- **Type**: blog-post (written companion to a Pragmatic Engineer podcast episode; 12 takeaways written by Orosz, with a few direct Winters quotes)
- **Author credibility**: Orosz is the Pragmatic Engineer author and a former Uber engineering manager. Titus Winters led the Google readability program, built Abseil, is lead author of *Software Engineering at Google*, and is now Senior Principal Scientist at Adobe (developer experience and productivity).
- **Scope**: Large-scale refactoring, mandatory testing, readability reviews, AI productivity and outages, and CS curriculum. The post paraphrases most claims in Orosz's voice; only a few passages are direct quotes. The full transcript is linked from the page but was not captured in the page text I could fetch, so spoken-word wording of the outage and refactor claims is unchecked. Dates (2007, 2010) are Winters' recollection.

## Extracted Claims

### Claim 1: Google ran a ~250M-line C++ refactor in 2010 with a dozen people and no LLMs, using a parse/match/generate/coexist/shard/block/delete pipeline
- **Evidence**: Winters' first-hand recollection, relayed by Orosz. No metrics beyond the scale numbers.
- **Confidence**: anecdotal (first-hand, plausible)
- **Quote**: "A team of a dozen people was assembled. Google had close to 250M lines of code at the time, edited by 10,000 engineers."
- **Our assessment**: A useful pre-LLM template for automated migration: deterministic codemods with a coexistence period, sharded rollout, and a guard that blocks the old pattern. It maps directly onto how agent-driven migrations should be structured (see the Anthropic migration playbook note).

### Claim 2: Google made a test mandatory for every change after Search could no longer ship monthly (~2007), and cadence recovered
- **Evidence**: Winters' recollection of a specific org-level policy and its outcome. No numbers on the recovery.
- **Confidence**: anecdotal
- **Quote**: "Around 2007, Search, the flagship product, was unable to ship at a monthly cadence any more, and the best they could ship to production was quarterly."
- **Our assessment**: A concrete precedent for gating all changes (including AI-generated ones) on tests. It is causal-by-narrative: other changes could have contributed to the recovery. Still, it is a credible large-org example.

### Claim 3: A codebase is unsustainable if a valuable change cannot be made safely; safety nets are what remove fear
- **Evidence**: Winters' stated position; no data.
- **Confidence**: emerging (widely shared practitioner view)
- **Quote**: "Titus believes your codebase is unsustainable if it’s not possible to make a valuable change safely."
- **Our assessment**: Supports framing verification infrastructure as the precondition for agent-speed change. Conceptually close to the executable-specification argument in the Thoughtworks comprehensibility note.

### Claim 4: Outages at other companies are up ~30% year over year while features shipped are flat, despite much more code output
- **Evidence**: Anecdotal: Winters talks to engineers at other companies. Orosz relays it in his own words; there is no dataset, no named company and no definition of "outage".
- **Confidence**: anecdotal
- **Quote**: "Titus talks to engineers at other companies and it’s the same picture: code output is up hugely versus a year ago, and outages are also up about 30%, while the number of features shipped is static."
- **Our assessment**: Do not cite as a measured trend. It is consistent with the AI-linked outage evidence in other Pragmatic Engineer pieces, but those draw on overlapping networks and so this is not independent confirmation. Orosz himself hedges: "based on outages alone, the technology could be a negative."

### Claim 5: AI's main value is in projects too ambitious to have made sense before, which throughput-style metrics miss
- **Evidence**: Winters' opinion; no examples given in the post.
- **Confidence**: anecdotal
- **Quote**: "Instead, it’s about doing things you never thought of before: projects so ambitious that they didn’t used to make sense!"
- **Our assessment**: Plausible but unfalsifiable as stated. It sits in tension with Claim 4: both can't be settled by volume metrics, so teams need outcome measures. Not a clean contradiction with any note, so no contradiction issue filed.

### Claim 6: Google's readability program scaled mentoring-via-review to 10,000+ enrolled engineers, with an owner plus a language-certified readability reviewer on each change
- **Evidence**: Winters' account of Google's process, including enrollment size when he left.
- **Confidence**: anecdotal (first-hand, specific)
- **Quote**: "When Titus left Google three months ago, 10,000+ engineers were enrolled in readability at any given time."
- **Our assessment**: A model for institutionalised human review that teaches. Relevant to the question of what review should be for when AI writes most code; the post says nothing about AI interacting with the program.

### Claim 7: Testing and verification matter more for new engineers but are absent from the ACM/IEEE/AAAI curriculum; the middle tier of students is hurt most by AI
- **Evidence**: Winters served on the 2023 steering committee; the student-tier claim is professor hearsay, which Orosz says matches his own guest-lecture experience.
- **Confidence**: anecdotal
- **Quote**: "Testing and verification are cited as mattering a lot more for new joiners, but they are absent from the curriculum."
- **Our assessment**: Low priority for the guide, but it reinforces verification as a core skill. Education recommendations (grade prompts and tests, not code) are out of scope.

### Claim 8: Junior engineers should treat AI as a tool they wield ("Andrew's axe") rather than an anthropomorphised agent
- **Evidence**: Analogy from Winters.
- **Confidence**: anecdotal
- **Quote**: "Similarly with AI: it’s a tool for you to use, and anthropomorphizing this tool takes us out of that mindset."
- **Our assessment**: A principle-level framing (human accountability). Orosz's wording, not Winters' verbatim.

## Concrete Artifacts

Refactor pipeline as listed by Orosz (takeaway 2, summarising Winters):

```
Parse:         MapReduce over whole codebase; mapper parses every build target into an AST
Match:         match exact call patterns in the tree
Code generation: generate edits to be made by the machine
Coexist:       old API and new API work side-by-side
Shard:         split edits by directory, send out in batches
Block the old: make sure nobody copies the old pattern back
Delete:        remove the old API
```

Source also notes that the clang-format toolkit exists because this refactor needed it.

## Cross-References

- **Corroborates**: `blog-pragmaticengineer-orosz-slow-down-speed-up.md` (Claims 5 and 6 report sharply rising PR and code volume; Claim 1 covers an AI-linked outage). `blog-thoughtworks-mugrage-comprehensibility-liability.md` (Claim 3: AI-generated code volume outpacing trust and understanding; Claim 6: tests and specs as gates).
- **Contradicts**: None found.
- **Extends**: `blog-anthropic-code-migration-playbook.md` (this gives a deterministic, pre-LLM migration pattern with a "block the old" step). `blog-pragmaticengineer-orosz-state-of-tech-industry-2026.md` (it quotes Winters on hiring; this adds his testing and outage positions). `blog-pragmaticengineer-orosz-code-review-approaches.md` (the owner + readability two-reviewer model alongside risk-tiered review).
- **Novel**: The 2007 mandatory-test policy and its cadence recovery; the 250M-line refactor method; readability program scale; the ~30% outage anecdote (not independent of existing Pragmatic Engineer outage evidence).

## Guide Impact

- **Chapter 03**: Cite the 2007 Google mandatory-test rule as a precedent for gating all changes, with the caveat that it is a recalled anecdote. Cite the refactor pipeline (coexist, shard, block the old) next to migration material.
- **Chapter 05**: If outage trends are discussed, mention the ~30% figure only as an unmeasured anecdote with attribution. The readability program may be an example of scaled review-as-mentoring.
- **Chapter 00**: The point about volume metrics missing AI's value, together with "Andrew's axe", could support a principles note on tools versus agents. Evidence is thin.

## Extraction Notes

- Read the full post text (summary, 12 takeaways, and reference list). The transcript was linked but not available in the fetched content, so the outage and refactor claims are quoted from Orosz's prose, not Winters' spoken words.
- The triage comments described the outage claim as Winters' own; the post phrases it as Orosz's relay of Winters' conversations.
- Curriculum and student-grouping content was extracted only briefly (out of guide scope).
