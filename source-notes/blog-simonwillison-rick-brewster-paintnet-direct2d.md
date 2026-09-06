---
source_url: https://simonwillison.net/2026/Sep/2/rick-brewster/
source_type: blog-post
title: "Quoting Rick Brewster"
author: Simon Willison (link-blog curation); quoted subject Rick Brewster (creator/lead developer of Paint.NET)
date_published: 2026-09-02
date_extracted: 2026-09-06
last_checked: 2026-09-06
status: current
confidence_overall: anecdotal
issue: "#3268"
---

# Quoting Rick Brewster

> Simon Willison's link-blog "quotation" post relays a forum post from Rick Brewster, the
> 20+-year creator of Paint.NET, describing how he used Claude to write an unreviewed,
> ~180,000-line, clean-room reverse-engineered reimplementation of Direct2D so Paint.NET
> could run under WINE on Linux — explicitly framing the result as "vibe coded" / "trust me
> bro" because the volume made line-by-line review infeasible, while separately naming a
> specific resource-management bug (missing COM `AddRef()` calls) and unspecified "bad
> design or architecture decisions" that he had to catch and fix by hand, alongside praise
> for Claude's reverse-engineering of Direct2D's effects-library formulas.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog "quotation" post format — a single
  blockquote of the source text with a one-line title/citation and no original Willison
  commentary, the same format as `blog-simonwillison-akshat-bubna-quote.md` and
  `blog-simonwillison-linus-torvalds-ai-debug-session.md`). The post's entire substantive
  content is Brewster's own forum-post text; Willison contributes no analysis of his own.
  The primary source Willison quotes from — Brewster's forum post at
  `forums.paint.net/topic/134563-🍷-extremely-experimental-winelinux-support-how-to-get-started/`
  — returned HTTP 403 Forbidden to direct fetch (see Extraction Notes), so this note relies
  entirely on Willison's blockquote reproduction of that text, verified sentence-by-sentence
  via repeated fetches of Willison's own page.
- **Author credibility**: Rick Brewster is the original author and, per the post itself,
  20+-year continuous maintainer of Paint.NET, a widely used Windows image-editing
  application (he states the rest of the codebase is "about 700,000 lines of code and I've
  been working on it for over 20 years"). This is first-person, first-party testimony from
  the engineer who wrote the code and is asking his own forum's users to test it — not a
  secondhand report or marketing claim. Willison is a `trusted-feed` curator; for this
  quotation post he adds no editorial framing of his own beyond selecting and reproducing
  the quote.
- **Scope**: Covers one specific engineering effort — an AI-assisted, clean-room
  reimplementation of Direct2D to unblock "extremely experimental" WINE/Linux support for
  Paint.NET — and Brewster's own characterization of the review process (or lack of one),
  one named failure mode, and one named strength. Does NOT cover: which specific Claude
  model/version was used (the quote names only "Claude" generically), a timeline or
  cost/token accounting for the effort, whether the WINE support has since moved beyond
  "extremely experimental" status, or any test/QA process applied to the result beyond
  Brewster's own review comments quoted here.

## Extracted Claims

### Claim 1: Paint.NET now includes an internal, from-scratch, clean-room reverse-engineered reimplementation of Direct2D, built specifically because WINE's own Direct2D support was judged permanently insufficient for Paint.NET's needs
- **Evidence**: First-person statement from the application's own author, describing a
  shipped (if "extremely experimental") component and the specific WINE compatibility
  problem it was built to solve.
- **Confidence**: anecdotal (single first-party practitioner account of one project, though
  the underlying artifact — a component now bundled with an experimental release — is a
  concrete, checkable claim about what exists, not just an opinion)
- **Quote**: "Direct2D has always been the biggest hurdle for Paint.NET on WINE, and it's clear that it will never be completed enough for Paint.NET's use."
- **Our assessment**: This frames the *reason* for attempting a large reverse-engineering
  project at all: not a greenfield feature, but a compatibility gap (WINE's own Direct2D)
  that Brewster judged unfixable from the WINE side. It is the motivating constraint behind
  every claim that follows — the size and review burden described in Claims 2-4 exist
  because the alternative (waiting for or contributing to WINE's own Direct2D) was judged a
  dead end, not because Brewster chose the AI-reimplementation path over an easier one.

### Claim 2: Brewster credits Claude directly and explicitly as the author without whom the Direct2D reimplementation "would NOT have been possible"
- **Evidence**: Direct first-person statement of attribution, immediately following the
  description of the shipped component (`PaintDotNet.Windows.Direct2D1.Managed.dll`).
- **Confidence**: anecdotal
- **Quote**: "This was written by our good friend Claude, without whom this would NOT have been possible"
- **Our assessment**: This is a stronger and more specific attribution than a vague "AI
  helped with this" — Brewster is saying the project was not merely accelerated by Claude
  but was infeasible for him without it (implicitly: infeasible within a reasonable amount
  of his own unpaid/side-project time, for a 700,000-line codebase he already maintains
  alone). It sets up the tension that runs through the rest of the quote: the same tool that
  made an otherwise-infeasible project possible also produced a result he says he "cannot
  possibly review."

### Claim 3: Brewster explicitly labels most of the ~180,000-line Direct2D reimplementation as "vibe coded" — meaning not thoroughly reviewed, "trust me bro" style — and states plainly that reviewing that volume of code is not something he can do
- **Evidence**: Direct first-person statement, with an explicit definition of what he means
  by "vibe coded" in this context (not a vague aside — he defines the term for his own
  readers) and an explicit numeric comparison (180,000 new/AI-assisted lines against
  "the rest of Paint.NET," about 700,000 lines built over 20+ years).
- **Confidence**: anecdotal (single first-party account, but an unusually direct and
  self-implicating one — an experienced maintainer stating on his own project's forum that
  a shipped component has not been reviewed)
- **Quote**: "Most of this code is, as they say, \"vibe coded.\" By that I mean that it has not been thoroughly reviewed, it's more \"trust me bro\" style. I cannot possibly review 180,000 lines of code, it's just way way _way_ too much. For reference, the rest of Paint.NET is about 700,000 lines of code and I've been working on it for over 20 years."
- **Our assessment**: The 180,000-line figure is not stated with an explicit "of the
  Direct2D component" qualifier attached to the number itself, but the immediately preceding
  sentence's topic is exactly that component, and the very next sentence's contrast ("the
  rest of Paint.NET is about 700,000 lines") only makes sense read as "the new Direct2D code
  (180k) vs. everything else (700k)" — so we read this as Brewster stating the Direct2D
  reimplementation is roughly 180,000 lines, about a quarter the size of the rest of the
  application. The more important and more directly stated claim, independent of that
  reading, is the volume-makes-review-infeasible argument itself: at a scale in the
  hundreds-of-thousands of lines, "trust me bro" is presented not as a stylistic choice but
  as the only realistic option available to a solo, 20-year maintainer.

### Claim 4: Claude's Direct2D code initially had a concrete resource-management bug — it was not performing the COM equivalent of `AddRef()` for reference-counted objects — which Brewster had to catch and correct through active oversight
- **Evidence**: Direct first-person statement naming a specific, technically identifiable
  defect class (COM reference-counting) rather than a vague "there were some bugs."
- **Confidence**: anecdotal (one practitioner's account of one bug, but the description is
  specific and technically falsifiable — a missing `AddRef()` call on reference-counted COM
  objects is a well-understood, well-named category of resource-management defect, not an
  ambiguous complaint)
- **Quote**: "I had to babysit Claude quite a bit to make sure it did resource management correctly (for awhile it just wasn't doing the COM equivalent of AddRef() for reference counted objects, oops)."
- **Our assessment**: This is the single most concrete, technically specific failure mode in
  the quote, and it is exactly the class of bug that is easy to write, easy to miss in a
  quick read, and dangerous at scale: a missing reference-count increment produces
  use-after-free or premature-destruction bugs that may not surface until specific object
  lifetimes or GC/finalization timing are hit, which is consistent with Brewster describing
  it as something he had to actively "babysit" for rather than something caught immediately.
  This is a specific, named, citable instance of the general "AI-generated code can look
  correct while getting memory/resource-lifetime semantics wrong" pattern, in a domain (COM
  interop) where the failure is silent by default rather than a compiler or type error.

### Claim 5: Beyond the resource-management bug, Brewster separately had to intervene ("slap it") on multiple occasions when he found "really bad design or architecture decisions" in Claude's output
- **Evidence**: Direct first-person statement, presented as a second, distinct category of
  problem from the resource-management bug in Claim 4 (introduced with "I had to slap it a
  few times" as a separate sentence).
- **Confidence**: anecdotal (vague on specifics — no example of what the "bad design or
  architecture decisions" actually were is given)
- **Quote**: "I had to slap it a few times when I found some really bad design or architecture decisions."
- **Our assessment**: This is the weakest-evidenced claim in the source: unlike Claim 4, no
  concrete example is given, so it cannot be independently assessed for severity or
  frequency ("a few times" across 180,000 lines could mean almost anything). Its value is as
  a second, qualitatively distinct failure axis alongside Claim 4: not just a specific
  low-level correctness bug (reference counting) but higher-level architectural judgment
  calls that also required a human to catch. Treat as color establishing "more than one kind
  of problem occurred," not as a quantifiable defect-rate data point.

### Claim 6: Brewster was separately impressed by what he calls "clever and tireless reverse engineering work" Claude did to determine the mathematical formulas needed to implement Direct2D's built-in effects library
- **Evidence**: Direct first-person statement of praise, the closing sentence of the quoted
  text, describing a specific sub-task (deriving formulas for Direct2D's built-in effects)
  rather than praising the project generally.
- **Confidence**: anecdotal
- **Quote**: "And I was also impressed at some rather clever and tireless reverse engineering work it did to figure out all the formulas needed for implementing Direct2D's built-in effects library."
- **Our assessment**: This is the one clearly positive, capability-specific claim in the
  quote, and it names a task shape — reconstructing undocumented mathematical/algorithmic
  behavior of a closed system from its observable outputs — that is a plausible strength
  for an LLM-based agent (pattern-matching against a large corpus of graphics/shader math,
  combined with tireless trial-and-check iteration) distinct from the general "write correct
  production code" task where Claims 3-5 show it falling short. The word "tireless" here
  echoes (without any connection between the sources) the same word Linus Torvalds used and
  then explicitly declined to apply to an AI's debugging persistence in
  `blog-simonwillison-linus-torvalds-ai-debug-session.md` Claim 2 — see Cross-References.

## Concrete Artifacts

### Full quoted text, reconstructed verbatim from Willison's blockquote (sentence order confirmed via repeated direct fetches of the source page; see Extraction Notes)
```
Source: Rick Brewster, forum post at forums.paint.net/topic/134563 (undated in the
quote itself; titled "extremely experimental wine/linux support - how to get
started"), as quoted by Simon Willison, simonwillison.net/2026/Sep/2/rick-brewster/,
posted 2nd September 2026.

"Direct2D has always been the biggest hurdle for Paint.NET on WINE, and it's clear
that it will never be completed enough for Paint.NET's use.

Paint.NET now has an internal, from-scratch, clean-room reverse-engineered rewrite
of Direct2D that it uses on WINE (triggered by using --wine). It lives in
PaintDotNet.Windows.Direct2D1.Managed.dll.

This was written by our good friend Claude, without whom this would NOT have been
possible

Most of this code is, as they say, "vibe coded." By that I mean that it has not
been thoroughly reviewed, it's more "trust me bro" style. I cannot possibly review
180,000 lines of code, it's just way way _way_ too much. For reference, the rest
of Paint.NET is about 700,000 lines of code and I've been working on it for over
20 years.

I had to babysit Claude quite a bit to make sure it did resource management
correctly (for awhile it just wasn't doing the COM equivalent of AddRef() for
reference counted objects, oops). I had to slap it a few times when I found some
really bad design or architecture decisions.

And I was also impressed at some rather clever and tireless reverse engineering
work it did to figure out all the formulas needed for implementing Direct2D's
built-in effects library."

Post tags (Willison's site): dotnet, linux, reverse-engineering, ai,
generative-ai, llms, claude, vibe-coding, coding-agents
```

## Cross-References

- **Corroborates**: `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 4
  ("Traditional software quality markers — commit history, test suites, documentation — are
  no longer reliable signals because they can be generated in 30 minutes") and the same
  note's central "vibe coding and agentic engineering are blurring" thesis: Brewster's own
  self-description — a 20-year professional maintainer explicitly choosing "trust me bro"
  review (or non-review) for a 180,000-line shipped component, purely because of volume — is
  a concrete, named, first-party instance of exactly the practitioner-discipline erosion
  Willison describes abstractly in that source. Brewster does not merely fail to review by
  oversight; he states directly that reviewing 180,000 lines is not something a solo
  maintainer can do, which sharpens Willison's "normalization of deviance" framing (that
  note's Claim 2) into a concrete volume threshold beyond which even a disciplined engineer
  reports being unable to comply with his own review standard.
- **Corroborates**: `blog-simonwillison-cheap-reverse-engineering.md` Claim 3 ("Coding
  agents lower both the effort required to build a working automation and the cost of a
  failed attempt") and Claim 1 (secondhand anecdotes of coding agents used to
  reverse-engineer undocumented systems): this note supplies a first-party, named,
  large-scale, technically specific instance of exactly that pattern — clean-room
  reverse-engineering of an undocumented/closed API surface (Direct2D's behavior, as opposed
  to WINE's incomplete implementation of it) — where the earlier note had only anonymous
  "anecdotes from people" about home-device automation. This is a substantially
  higher-stakes and better-attested example of the same underlying claim (agents make
  previously-uneconomical reverse-engineering projects newly viable).
- **Corroborates**: `blog-simonwillison-linus-torvalds-ai-debug-session.md` Claim 1
  (Torvalds crediting an AI with "much of the grunt-work" on a hard debugging session while
  explicitly declining to call it "tireless" because of a separate failure mode) and Claim 6
  (a striking patches-to-final-fix ratio as evidence that AI assistance shows up as volume in
  a search/iteration phase, not as a shortcut to the final answer): both sources are
  first-party accounts from experienced, technically rigorous engineers describing AI
  assistance on hard, low-level systems work (kernel memory-mapping vs. closed-API graphics
  reverse-engineering) as genuinely valuable for exactly the kind of tireless, iterative
  exploration a human finds tedious, while each independently reporting a distinct, named
  failure mode (Torvalds: premature declarations of infeasibility; Brewster: resource-
  management and architecture defects) that required active human correction.
- **Extends**: `blog-simonwillison-vibe-coding-agentic-engineering.md` — that source
  documents Willison's own, more abstract and reflective account of the vibe-coding/agentic-
  engineering blur in his own (implicitly smaller-scale, tooling-focused) practice. This
  source extends that claim with a much larger, named, shipped-software instance: a
  20-year-maintained, widely used desktop application now bundling 180,000 lines of
  admittedly-unreviewed AI-generated code as part of an official (if experimental) release
  channel, which is a materially higher-stakes test of the same dynamic than Willison's own
  personal-tools examples.
- **Contradicts**: No contradiction issue filed. No existing source note in this corpus was
  found to make an opposing claim about the same specific situation (AI-assisted, unreviewed,
  large-scale reverse-engineering of a closed graphics API for a shipped application).
- **Novel**:
  - This is the first source in the corpus with a first-party account of an experienced,
    named, non-Anthropic-affiliated professional engineer explicitly and voluntarily
    disclosing that a specific, sizeable (~180,000-line), currently-shipped component of
    software he distributes to end users is "vibe coded" and has not been reviewed, together
    with an explicit statement that reviewing it at that scale is not something he can do.
  - The specific named defect — a missing COM `AddRef()` call causing incorrect
    reference-counting behavior — is a new, concrete example in this corpus of an
    AI-generated resource-management bug in unmanaged/COM-interop code, a domain not
    previously represented among this corpus's AI code-quality failure examples.
  - The pairing of one named correctness failure (Claim 4), one unspecified
    architecture/design failure (Claim 5), and one named strength (Claim 6) in a single
    first-party account, about a single project, is a useful compact "mixed report card" —
    most existing corpus sources document either capability wins or failure modes, not both
    in the same short first-party statement about the same codebase.

## Guide Impact

- **Chapter on Verification / Code Review Practices**: Add Brewster's account as a named,
  concrete counter-example to any guide framing that treats "review everything the agent
  writes" as a universally achievable practice. Brewster is not describing negligence or a
  process failure — he is an experienced, 20-year maintainer explicitly stating that at
  ~180,000 lines, line-by-line review is not something a solo practitioner can do, and
  choosing to ship anyway with "trust me bro" as the stated (not hidden) posture. The guide
  should distinguish this from an *endorsement* of skipping review: pair this claim with
  Claim 4 (the COM `AddRef()` bug that resulted) as the direct, named cost of that choice —
  a real, if apparently caught, resource-management defect in the unreviewed code. Recommend
  guidance on risk-tiering large AI-generated components (e.g., targeted review of
  lifetime/resource-management-sensitive code paths even when full-codebase review is
  infeasible) rather than an all-or-nothing review posture.

- **Chapter on Verification — resource-management-specific review**: Cite Claim 4 as a
  specific, named category of defect to prioritize when full review is infeasible: interop
  and unmanaged-memory boundaries (COM reference counting here; analogous risks exist for
  manual memory management, RAII violations, and FFI boundaries generally) are a
  higher-value, lower-volume target for targeted human review than attempting full-codebase
  coverage, precisely because these defects are silent (no compiler error) and were, in this
  account, not caught by whatever automated testing existed before Brewster personally
  noticed them.

- **Chapter on AI Capabilities / Reverse Engineering**: Add Claim 6 and the overall project
  (Claims 1-2) as a large-scale, named, real-world example supporting the guide's treatment
  of reverse-engineering and closed-API reimplementation as a strong AI-agent use case —
  pair with `blog-simonwillison-cheap-reverse-engineering.md` for the lower-stakes,
  anonymous-anecdote version of the same underlying claim, and note that this source
  provides the higher-stakes, named, technically-detailed corroboration that source lacked.

## Extraction Notes

1. **Primary source (Brewster's forum post) was inaccessible**: a direct fetch of
   `forums.paint.net/topic/134563-🍷-extremely-experimental-winelinux-support-how-to-get-started/`
   returned HTTP 403 Forbidden. This note's extraction is therefore based entirely on
   Willison's blockquote reproduction of that text, not on independent verification against
   the primary forum post itself — the same limitation `blog-simonwillison-akshat-bubna-quote.md`
   documented for its inaccessible Reuters primary source. No forum-post date was recoverable
   for this reason; only Willison's own publication date (2026-09-02) is known.
2. **Quote reconstructed from multiple targeted fetches, not a single full-page fetch**:
   Willison's page itself could not be reproduced in one verbatim pass — the fetch tool used
   for this extraction enforces a per-quote length ceiling and declined a full verbatim
   reproduction as excessive copying. The full quoted text in Concrete Artifacts above was
   assembled from a sequence of targeted fetches, each requesting a specific short fragment
   (a named sentence, or "the sentence before/after X"), and cross-checked for consistent
   ordering across separate fetches (e.g., the "vibe coded" → "trust me bro" → "180,000
   lines" → "700,000 lines" sequence was confirmed twice, from two different fetch prompts,
   with identical results both times). No fragment here was paraphrased or reconstructed from
   memory; each was returned by the fetch tool as an explicit verbatim quotation request.
3. **180,000-line attribution is this Miner's contextual reading, not an explicit
   statement**: as flagged in Claim 3's assessment, the source does not attach an explicit
   "of the Direct2D component" qualifier directly to the "180,000 lines" figure — that
   reading follows from sentence adjacency and the explicit "for reference, the rest of
   Paint.NET is..." contrast, not from a single self-contained sentence. Flagged here so a
   reviewer can independently judge whether that reading is safe to state as fact in the
   guide (this Miner believes it is, given the immediate context, but it is not a verbatim
   claim).
4. **No specific Claude model/version is named** anywhere in the quoted text — only
   "Claude" generically, per the post's own "claude" tag. Guide citations of this source
   should not attribute the account to a specific model version.
5. **Cross-reference verification (MINER.md §4b)**: all three cited source notes
   (`blog-simonwillison-vibe-coding-agentic-engineering.md`,
   `blog-simonwillison-cheap-reverse-engineering.md`,
   `blog-simonwillison-linus-torvalds-ai-debug-session.md`) were re-read in full immediately
   before writing Cross-References above, and every cited claim number was confirmed against
   those notes' numbered `### Claim N:` headings in document order before citing it.
6. **No contradiction issue filed**: see Cross-References — Contradicts.
