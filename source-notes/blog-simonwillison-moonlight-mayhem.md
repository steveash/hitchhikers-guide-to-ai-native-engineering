---
source_url: https://simonwillison.net/2026/Aug/7/moonlight-mayhem/
source_type: blog-post
title: "Moonlight & Mayhem (Raccoon Heist by Codex + GPT-5.6 Sol Ultra)"
author: Simon Willison
date_published: 2026-08-07
date_extracted: 2026-08-17
last_checked: 2026-08-17
status: current
confidence_overall: anecdotal
issue: "#2744"
---

# Moonlight & Mayhem (Raccoon Heist by Codex + GPT-5.6 Sol Ultra)

> Simon Willison re-ran the exact same "raccoon heist" autonomy-granting
> prompt he'd previously given Claude Fable 5 (`blog-simonwillison-raccoon-heist.md`),
> this time against Codex Desktop running GPT-5.6 Sol Ultra in its
> aggressive-sub-agent mode, producing a game he judged substantially
> better-designed (a museum heist requiring raccoons to stack on each other
> to steal a golden sardine, vs. Fable 5's simple backyard coin/fish
> collection) — but one that shipped with a glaring visual bug (each
> raccoon's eye rendered as a sphere four times the size of its body) that
> Codex failed to notice despite reviewing its own screenshots during
> development, only fixing it after Willison explicitly flagged it.

## Source Context

- **Type**: blog-post (Simon Willison's weblog, August 7, 2026 — a
  first-person case-study/link-blog post, the direct follow-up to
  `blog-simonwillison-raccoon-heist.md` published two days earlier, pointing
  to a live demo, a public GitHub repo, a published session transcript, and
  a preserved "buggy" build of the game.
- **Author credibility**: Simon Willison is the creator of Django, Datasette,
  and the `llm` Python CLI, and a trusted-feed source already covered
  extensively in this corpus. No vendor affiliation with OpenAI or
  Anthropic. The claims here are first-person: he wrote the prompt (reused
  verbatim from the prior post), watched the session, and is the one
  characterizing both the design quality and the visual bug.
- **Scope**: Covers one single, non-repeated autonomous build of the same
  browser game concept using Codex Desktop and GPT-5.6 Sol Ultra (in its
  "aggressive use of sub-agents" mode), directly paired against the earlier
  Claude Fable 5 attempt at the identical prompt. Does not cover: a
  controlled/blinded comparison (Willison knew which model produced which
  game), repeated trials with either vendor, or any claim that this result
  generalizes beyond this one prompt and game concept.

## Extracted Claims

### Claim 1: Willison posed the identical prompt used for the Claude Fable 5 build to Codex Desktop running GPT-5.6 Sol Ultra, specifically in its aggressive sub-agent mode
- **Evidence**: Willison's own statement of intent and method, naming the specific tool, model, and mode used.
- **Confidence**: settled (author's direct, unambiguous statement of what he did)
- **Quote**: "I decided to pose the exact same prompt to Codex Desktop running GPT-5.6 Sol Ultra - the mode where Sol makes _aggressive_ use of sub-agents - to see how it would do."
- **Our assessment**: This is a genuine paired comparison — same task specification, same author, three days apart — which is stronger evidentiary footing than two independent anecdotes about different tasks. It is still a sample size of one build per vendor, run by one practitioner, so it supports "this happened once" rather than "this is the typical outcome," but the paired design is unusually clean for this corpus.

### Claim 2: The GPT-5.6 Sol Ultra build produced a game Willison judged design-superior to the Fable 5 build, with a heist mechanic closer to the original "raccoon heist" premise
- **Evidence**: Willison's direct comparison of the two games' mechanics — Fable 5's single raccoon collecting items in a backyard versus Sol's museum heist requiring cooperative raccoon-stacking to steal an object from a display case.
- **Confidence**: anecdotal (single practitioner's subjective design judgment)
- **Quote**: "It produced a much better game!"
- **Our assessment**: "Better" here is Willison's own aesthetic/design judgment, not a measured outcome — there's no rubric, no third-party rating, no blinded comparison. It is nonetheless a specific, checkable claim: readers can play both linked demos and form their own view. The paired-prompt design (Claim 1) makes this a meaningfully stronger single data point on cross-vendor game-design-quality variance than either source alone would be.

### Claim 3: The winning build's heist mechanic (rescuing crewmates, stacking raccoons to reach and steal a display-cased object) was substantively closer to the "heist" framing of the original prompt than the losing build's mechanic
- **Evidence**: Willison's own characterization of the gameplay, contrasting it explicitly with the earlier build.
- **Confidence**: anecdotal
- **Quote**: "GPT-5.6 Sol has you in a museum, rescuing your two other raccoon crewmates in order to stack on top of each other and bust the golden sardine out of its case." ... "Much more heisty!"
- **Our assessment**: This is a concrete illustration of what "better game design" meant in practice for Claim 2 — not just polish or bug count, but closer adherence to the thematic premise implied by the prompt's own reference material (the 2022 GPT-3/DALL-E "raccoon heist" concept text), which neither model was given as an explicit rubric to score against.

### Claim 4: The build shipped with a severe, glaring visual bug — an oversized sphere rendered over each raccoon's head at roughly four times body scale
- **Evidence**: Willison's direct description of the defect, with a preserved "eyeball edition" build of the game linked as a checkable artifact.
- **Confidence**: settled (independently verifiable via the preserved buggy build)
- **Quote**: "the version produced from the one-shot prompt had a bug where each raccoon had an eyeball that was enlarged to the size of a giant sphere floating over their head!"
- **Our assessment**: This is not a subtle spatial or physics defect (the kind Godogen's Lesson 4 discusses, e.g. z-fighting or floating objects) — it's a scale error large enough to dominate the character model, plausibly visible in any reasonably-composed screenshot. That's what makes Claim 5 (below) significant: it isn't a bug that a screenshot review would need to be especially attentive to catch.

### Claim 5: Despite reviewing its own screenshots during development, Codex/GPT-5.6 Sol Ultra did not notice or fix the oversized-eyeball bug on its own
- **Evidence**: Willison's direct statement that Codex reviewed screenshots as part of its development process and still failed to catch the defect.
- **Confidence**: anecdotal (single session, single practitioner's account of the agent's process)
- **Quote**: "Despite reviewing screenshots during development Codex failed to spot and correct this bug."
- **Our assessment**: This is the most guide-relevant claim in the source. It is a direct counter-example, on a comparably coarse bug class, to `blog-simonwillison-raccoon-heist.md` Claim 4, where Claude Fable 5's same-agent Playwright screenshot review *did* catch a coarse visual defect (objects not rendering on mobile) unprompted. We filed contradiction issue **#2752** over this — see Cross-References below — rather than silently picking a side. Note the asymmetry in verification rigor: the Fable 5 post describes an active, tool-driven Playwright testing loop across a specific viewport condition, while this post doesn't specify whether Codex's "reviewing screenshots" was similarly systematic or more incidental; that difference in QA process rigor, not just model capability, may be part of why the outcomes diverged.

### Claim 6: The bug was only fixed after Willison explicitly pointed it out in plain language, and the agent then corrected it in a single follow-up turn
- **Evidence**: Willison's account of the exact two-turn exchange that resolved the bug.
- **Confidence**: settled (author quotes the literal prompts he typed)
- **Quote**: "I fixed it by prompting: `Why do the raccoons have huge black spheres on them?` And then: `Fix it`"
- **Our assessment**: The bug was trivial for the agent to fix once identified by a human — this wasn't a case of the model being unable to solve the problem, only unable (or unmotivated) to notice it during its own unprompted review. That's a meaningful distinction for the guide's self-verification chapters: the gap here is one of autonomous QA attentiveness/thoroughness, not underlying capability to diagnose and repair the defect.

### Claim 7: The session's full API cost was $23.28, driven by 700.7K input tokens, 32.5M cached tokens, and 148K output tokens over 52 minutes, because Willison was paying full API prices rather than using his Codex subscription
- **Evidence**: Willison's own stated cost/token breakdown for the session, with an explicit note about billing method.
- **Confidence**: settled (author's direct, itemized accounting)
- **Quote**: "Total Cost: $23.28. Input Tokens: 700.7K, plus 32.5M cached tokens. Output Tokens: 148K" ... "I had been paying full API prices as opposed to using my monthly Codex subscription"
- **Our assessment**: This is the first source note in this corpus's raccoon-heist thread with hard cost/token numbers — the Fable 5 predecessor post did not state cost, token spend, or duration at all (flagged as a scope gap in that note's Source Context). The 32.5M cached-vs-700.7K-input ratio (roughly 46:1) is a striking data point on how much of an "aggressive sub-agent mode" session's token volume is cache reads rather than fresh input, though the post doesn't break down which sub-agent calls drove that ratio. The explicit "full API prices, not subscription" caveat matters for readers trying to estimate their own costs: a $23.28 API-metered figure is not representative of what a Codex subscriber would have paid out-of-pocket for the same session.

### Claim 8: The build took 52 minutes end-to-end
- **Evidence**: Willison's stated duration for the Codex session.
- **Confidence**: settled (author's direct statement)
- **Quote**: "Codex spent 52 minutes on the project."
- **Our assessment**: Unlike cost/tokens, the predecessor Fable 5 post also didn't state wall-clock duration, so this is not a comparison point against that source — but it's a useful absolute reference: a design-superior, multi-tool (3D rendering, sub-agents, self-testing) one-shot game build completed in under an hour, cost/attentiveness caveats aside.

### Claim 9: The build produced a public, verifiable artifact trail, including a preserved buggy build distinct from the fixed final version
- **Evidence**: Willison links the live fixed game, the GitHub repository (including an image-generation output subdirectory and the full commit history), a published transcript, and a separately-hosted "eyeball edition" snapshot of the pre-fix buggy build.
- **Confidence**: settled (the artifacts themselves are independently checkable, not just narrated claims)
- **Quote**: (no direct quote; see paraphrase above — the claim is evidenced by the linked artifacts themselves, not by a narrated sentence)
- **Our assessment**: The preserved "eyeball edition" is a notable auditability upgrade over the predecessor post: rather than asking readers to take the bug's severity on faith, Willison kept a live, playable copy of the buggy version alongside the fixed one, so Claim 4's severity is independently checkable by any reader, not just narrated.

## Concrete Artifacts

Comparison setup, as stated by the author (reusing the prior post's prompt verbatim):
```
I decided to pose the exact same prompt to Codex Desktop running GPT-5.6
Sol Ultra - the mode where Sol makes aggressive use of sub-agents - to
see how it would do.
```
*Source: Simon Willison, simonwillison.net/2026/Aug/7/moonlight-mayhem/*

Cost/token breakdown for the session:
```
Total Cost: $23.28
Input Tokens: 700.7K, plus 32.5M cached tokens
Output Tokens: 148K
Duration: 52 minutes
Billing: full API prices (not the monthly Codex subscription)
```
*Source: Simon Willison, simonwillison.net/2026/Aug/7/moonlight-mayhem/*

The bug-fix exchange (full text of both follow-up prompts):
```
Why do the raccoons have huge black spheres on them?

Fix it
```
*Source: Simon Willison, simonwillison.net/2026/Aug/7/moonlight-mayhem/*

Published artifact trail:
```
Live demo (fixed):     https://simonw.github.io/raccoon-heist-codex/
GitHub repository:     https://github.com/simonw/raccoon-heist-codex/
Image-gen outputs:     https://github.com/simonw/raccoon-heist-codex/tree/main/output/imagegen
Session transcript:    https://github.com/simonw/raccoon-heist-codex/blob/main/transcript.md
Buggy "eyeball edition": https://static.simonwillison.net/static/2026/raccoon-heist-eyeball-edition/
Bug-fix commit:        https://github.com/simonw/raccoon-heist-codex/commit/4e9a390dfbe80533324ee61a37aa661813c08446
Predecessor post:      https://simonwillison.net/2026/Aug/5/raccoon-heist/ (Claude Fable 5 build)
```
*Source: Simon Willison, simonwillison.net/2026/Aug/7/moonlight-mayhem/*

## Cross-References

- **Corroborates**:
  - `failure-htdt-godogen-game-generation.md` (Lesson 4: "A coding agent
    cannot reliably evaluate the visual/spatial correctness of its own
    output — external evaluator is required"): Claim 5 here is a direct,
    concrete instance of exactly that failure mode — an agent that both
    generated the visual defect and reviewed its own screenshots, and
    still missed a severe, non-subtle rendering error. This strengthens
    Godogen's general case with a second, independent vendor (Codex/OpenAI
    vs. Godogen's Claude-based pipeline).

- **Contradicts**: `blog-simonwillison-raccoon-heist.md` Claim 4 ("The
  agent used Playwright to take its own screenshots, detected a
  mobile-specific rendering bug from those screenshots, and fixed it
  without human intervention" — same-agent screenshot review *succeeded*
  at catching a coarse visual bug). This source's Claim 5 is the same
  setup (same coding agent both writes the rendering code and reviews its
  own screenshots) applied to a comparably or more coarse bug class, with
  the opposite outcome: the agent missed it. **Contradiction issue #2752
  filed** per MINER.md §4a — no verdict is picked in this note; see the
  issue for Side A/Side B framing and the filer's suggested (non-binding)
  reading that the more evidence-backed position is Godogen's general
  "external evaluator required" claim, with both raccoon-heist posts read
  as variance data points rather than competing rules.

- **Extends**: `blog-simonwillison-raccoon-heist.md` — this is the direct,
  same-author, same-prompt follow-up comparison the predecessor note
  explicitly lacked ("a comparison against other models attempting the
  same task" was listed there as out of scope). It also fills two gaps the
  predecessor note flagged as missing: cost/token figures (Claim 7) and
  wall-clock duration (Claim 8), neither of which the Fable 5 post stated.

- **Novel**:
  - First source note in this corpus with a genuinely paired,
    same-prompt, same-author cross-vendor comparison of one-shot
    autonomous game builds (Claude Fable 5 vs. Codex/GPT-5.6 Sol Ultra),
    rather than two independently-scoped case studies being compared after
    the fact.
  - First documented use of "aggressive sub-agent mode" as a named,
    selectable Codex/GPT-5.6 Sol Ultra operating mode in this corpus
    (Claim 1) — prior GPT-5.6 Sol coverage
    (`blog-simonwillison-pedalican-sprite-pipeline.md`,
    `blog-simonwillison-gpt56-sol-launch.md`) does not mention this mode.
  - First instance in this corpus of a practitioner preserving a live,
    playable "buggy edition" build specifically to make a described defect
    independently checkable rather than only narrated (Claim 9).

## Guide Impact

- **Chapter 03 (Verification)**: Do not cite `blog-simonwillison-raccoon-heist.md`
  Claim 4 alone as evidence that same-agent screenshot review is a
  sufficient gate for coarse visual bugs. This source's Claim 5 is a
  same-topic, comparably-coarse counter-example from a different vendor —
  see contradiction issue **#2752**. Until that issue resolves, the guide
  should either present both as a debated/unsettled point or lean on the
  independently-evidenced `failure-htdt-godogen-game-generation.md` Lesson
  4 position (external, code-blind evaluator required) rather than
  asserting same-agent review is reliable.

- **Chapter 04 (Context Engineering)**: Claim 6 (the bug was trivially
  fixed once a human named it, in a single follow-up turn) is a specific,
  actionable data point for any section discussing human-in-the-loop QA
  economics: the cost asymmetry between an agent's autonomous review
  missing an obvious defect versus a human's one-sentence flag resolving
  it in one turn argues for cheap, low-effort human spot-checks as a
  cost-effective backstop even when agent self-review is otherwise in
  place, rather than for either replacing the other.

- **Chapter 02 (Harness Engineering) / cost estimation guidance**: Claim 7's
  itemized cost/token breakdown (including the 46:1 cached-to-input token
  ratio under "aggressive sub-agent mode") is a concrete reference point
  for a section estimating agentic session costs, with the explicit
  caveat that it reflects full API pricing, not subscription pricing —
  any citation should preserve that distinction rather than presenting
  $23.28 as a typical per-session cost for subscribers.

## Extraction Notes

- WebFetch declined to reproduce the full article verbatim (correctly, to
  stay within fair-use bounds), so extraction was done via several
  narrower, targeted fetches, each requesting short (under ~30-word)
  verbatim quotes or structured factual summaries in the fetcher's own
  words. All quotes above were independently re-requested and returned
  consistent wording across separate fetch calls.
- One sub-page was followed: the anchor-linked "Fable 5 prompt" section of
  the predecessor post (`https://simonwillison.net/2026/Aug/5/raccoon-heist/#the-fable-5-prompt`),
  to confirm Claim 1's "exact same prompt" assertion against the actual
  prompt text (already fully captured in `blog-simonwillison-raccoon-heist.md`'s
  Concrete Artifacts section). The GitHub repo, transcript, and preserved
  buggy build were not separately fetched in full; their URLs are cited
  from the blog post's own links (Claim 9), consistent with MINER.md's "up
  to 5 linked pages" being a ceiling, not a requirement.
- The two Prospector triage comments on issue #2744 disagreed with each
  other in two ways worth flagging: (1) the first named the existing
  overlap correctly (`blog-simonwillison-raccoon-heist.md`, Fable 5's
  version of the same game) while the second claimed "no existing notes
  overlap" — this is incorrect, the overlap is substantial and is the
  spine of this note; (2) the second comment's claimed metrics (token
  counts, cost) were verified against the live source and are accurate,
  despite that comment's inaccurate overlap claim. Both were treated as
  untrusted, unverified leads per the task instructions, and every factual
  claim in this note was independently re-verified against the source
  rather than taken from either triage comment.
- The source does not state whether GPT-5.6 Sol Ultra used a Playwright-
  equivalent structured testing tool (as Fable 5 did in the predecessor
  post) or relied on more ad hoc screenshot review — flagged in Claim 5's
  assessment as a possible confound, and explicitly noted here as a scope
  gap rather than omitted by oversight.
- Contradiction issue **#2752** was filed per MINER.md §4a before this PR
  was opened, covering the Claim 5 vs. predecessor-note Claim 4 conflict.
  No verdict is asserted in this note.
