---
source_url: https://simonwillison.net/2026/Aug/3/devtools-must-be-open-source-exedev/
source_type: blog-post
title: "Comment: Devtools must be open source (exe.dev)"
author: Simon Willison
date_published: 2026-08-03
date_extracted: 2026-08-10
last_checked: 2026-08-10
status: current
confidence_overall: anecdotal
issue: "#2601"
---

# Comment: Devtools must be open source (exe.dev)

> Simon Willison, republishing his own Hacker News comment on the "Devtools
> must be open source" (exe.dev) discussion, argues in first person that
> LLMs have converted open source's traditional "freedom to examine and
> modify" from a mostly theoretical entitlement into one he now personally
> exercises multiple times a day — citing his own habitual prompt ("Clone
> x/y from GitHub and tell me how Z works") and reframing compilation setup
> as a "zero time investment challenge" he now delegates to Codex or Claude
> Code.

## Source Context

- **Type**: blog-post. This is Simon Willison's "Comment" beat format — a
  short first-person post (~180 words) that republishes a comment he posted
  directly on a Hacker News thread. The page's `comment-source-bar` links to
  "My comment" (`news.ycombinator.com/item?id=49156111#49156719`) on the HN
  thread titled "Devtools must be open source (exe.dev)"
  (`news.ycombinator.com/item?id=49156111`), which itself discusses David
  Crawshaw's exe.dev essay of the same title. Auto-discovered via the
  `simon-willison` trusted feed. This Miner attempted to fetch the HN thread
  directly (both via WebFetch and `curl`) to check for surrounding
  discussion context but received HTTP 429 (rate-limited) on both attempts;
  see Extraction Notes. The primary source — Willison's own weblog page,
  which is the exact URL filed in this issue — was fetched successfully via
  `curl` and read in full from raw HTML.
- **Author credibility**: Simon Willison is a designated `trusted-feed`
  source in this corpus (creator of Django, Datasette, `sqlite-utils`,
  `llm`) and one of the most closely tracked independent commentators on
  practical LLM tooling. Unlike most of his "quotation" posts, which curate
  someone else's words without added commentary (e.g.
  `blog-simonwillison-andrew-kelley.md`), this post is entirely
  Willison's own first-person account of his own daily workflow — he is the
  primary source here, not a curator.
- **Scope**: Covers Willison's personal argument that LLMs have made the
  "freedom to examine and modify" open-source value proposition practically
  exercisable rather than theoretical, two specific habitual prompts he uses
  (a "clone and explain" prompt to "regular Claude chat," and a "checkout
  and build" delegation to "Codex or Claude Code"), and an explicit
  admission that he has not yet extended this to habitually *modifying* the
  software he uses. Does NOT cover: the underlying exe.dev essay's own
  content (that is covered separately by
  `blog-simonwillison-crawshaw-devtools-open-source.md`, mined from a
  different Willison post, `/2026/Aug/3/david-crawshaw/`, about the same
  underlying essay — see Cross-References), the Hacker News thread's other
  commenters, any measurement of time saved, or any specific worked example
  (unlike the Crawshaw note's meat.dev/Slinky examples, this post gives no
  named repo or concrete before/after outcome).

## Extracted Claims

### Claim 1: A core traditional argument for open source has been the user's freedom to examine and modify how software works
- **Evidence**: Opening framing statement, establishing the premise the rest
  of the post argues against/updates.
- **Confidence**: settled (a widely-recognized, uncontroversial
  characterization of the open-source freedoms argument, not a claim
  original to Willison)
- **Quote**: "One of the arguments for open source software for end-users has always been the freedom to examine and modify how that software works."
- **Our assessment**: This is scene-setting rather than a novel claim — it
  restates a decades-old open-source rationale so Willison can argue the
  practical *exercise* of that freedom has changed, not the freedom's
  existence.

### Claim 2: For most people, including expert programmers, the freedom to examine and modify source code has practically meant relying on other people to do it, because the time investment required is rarely justifiable
- **Evidence**: Willison's own characterization of the pre-LLM status quo,
  explicitly including "even expert programmers" in the group that could not
  exercise the freedom directly.
- **Confidence**: anecdotal (a single practitioner's characterization of a
  general pattern, not measured)
- **Quote**: "The reality for most people - even expert programmers - has been that the freedom is more about being able to lean on other people to do that. Most people can't justify the time commitment needed to read and then modify the code for tools they use very often."
- **Our assessment**: This is the essay's key premise: that "freedom to
  examine and modify" was, for nearly everyone, a *delegated* freedom
  (exercised by other people on your behalf — maintainers, forum experts)
  rather than a *personally exercised* one. The claim that this applied even
  to expert programmers is notable — it locates the friction in raw time
  cost, not in skill gap, which is what makes an LLM (a time-cost reducer)
  a plausible fix rather than a training intervention.

### Claim 3: LLMs have changed the time-cost equation enough to make the original "examine and modify your own software" vision of open source more practically achievable
- **Evidence**: Willison's direct thesis statement, connecting Claim 2's
  diagnosis (time cost as the barrier) to LLMs as the specific mechanism
  that lowers it.
- **Confidence**: anecdotal (a single practitioner's assessment, though
  consistent with the corpus's broader "LLMs reduce time-to-understanding"
  theme — see Cross-References → Corroborates)
- **Quote**: "I think LLMs have changed that equation in a way that makes the original dream much more feasible."
- **Our assessment**: This is the post's central claim and the reason the
  Prospector flagged it as high-novelty: it is not "LLMs make coding
  faster" in general, but a specific claim about open source's *founding
  freedoms* argument becoming practically real for the first time at scale,
  attributable to a time-cost mechanism rather than a licensing or tooling
  change.

### Claim 4: Willison personally prompts a general-purpose chat LLM multiple times a day to clone and explain unfamiliar repositories
- **Evidence**: A specific, named, self-reported habitual workflow with an
  exact prompt template, distinguishing this from a one-off anecdote.
- **Confidence**: anecdotal (single practitioner's self-reported frequency
  and habit; not independently verified or logged)
- **Quote**: "Several times a day I'll prompt regular Claude chat to "Clone x/y from GitHub and tell me how Z works"."
- **Our assessment**: The "several times a day" frequency claim is what
  elevates this from a one-time example to a described habit — Willison is
  asserting this is now a routine part of his workflow, not a novelty he
  tried once. The specificity of the prompt template ("Clone x/y ... tell
  me how Z works") makes this directly reusable as a concrete prompt pattern
  for the guide, in the same spirit as the two named prompts already
  extracted from the companion Crawshaw essay (see Cross-References →
  Extends).

### Claim 5: Compilation/build friction, which previously stopped Willison from exploring a codebase at all, is now something he delegates entirely to a coding agent and treats as costing zero of his own time
- **Evidence**: Direct before/after comparison in Willison's own words,
  naming both Codex and Claude Code as the delegation targets.
- **Confidence**: anecdotal (single practitioner's self-reported behavior
  change; no measurement of actual wall-clock time or success rate across
  repositories)
- **Quote**: "Getting software to compile in order to start hacking on it used to be enough friction that I often wouldn't bother. Now I treat that as a zero time investment challenge: tell Codex or Claude Code to checkout and build X and then come back ten minutes later and see how it got on."
- **Our assessment**: The "zero time investment challenge" framing and the
  specific "come back ten minutes later" pattern is the most concrete,
  actionable detail in the post — it describes a fire-and-forget delegation
  workflow (issue an instruction, walk away, check back) rather than
  active supervision. This is consistent with the corpus's async/routine
  agent-delegation pattern (see Cross-References → Corroborates) but applied
  specifically to the narrow task of "getting a foreign codebase to build,"
  which is not a use case already documented elsewhere in this corpus.

### Claim 6: Willison has not yet extended this workflow to habitually modifying the software he uses, but sees a newly-opened path to doing so that did not exist about a year earlier
- **Evidence**: Explicit self-report and hedge, closing the post.
- **Confidence**: anecdotal (a single practitioner's self-assessed
  trajectory, not a completed outcome)
- **Quote**: "I'm not habitually modifying the software I use yet, but I can see a path to that which didn't exist a year or so ago."
- **Our assessment**: This hedge is important for calibrating the claim's
  strength: Willison is explicitly not claiming the full "freedom to modify"
  half of the open-source argument is realized yet, only the "freedom to
  examine" half (Claims 3-5). The guide should preserve this distinction —
  reading-and-understanding friction reduction (well-evidenced here, daily
  habitual use) is a materially different, more mature claim than
  modification-friction reduction (self-reported as not yet habitual, only
  "a path" that "didn't exist a year or so ago").

## Concrete Artifacts

```
Source: Simon Willison's Weblog, "Comment: Devtools must be open source (exe.dev)"
https://simonwillison.net/2026/Aug/3/devtools-must-be-open-source-exedev/
Posted 3rd August 2026 at 3:30pm. Full post text, verbatim (~180 words):

"One of the arguments for open source software for end-users has always been
the freedom to examine and modify how that software works.

The reality for most people - even expert programmers - has been that the
freedom is more about being able to lean on other people to do that. Most
people can't justify the time commitment needed to read and then modify the
code for tools they use very often.

I think LLMs have changed that equation in a way that makes the original
dream much more feasible.

Several times a day I'll prompt regular Claude chat to "Clone x/y from
GitHub and tell me how Z works".

Getting software to compile in order to start hacking on it used to be
enough friction that I often wouldn't bother. Now I treat that as a zero
time investment challenge: tell Codex or Claude Code to checkout and build X
and then come back ten minutes later and see how it got on.

I'm not habitually modifying the software I use yet, but I can see a path to
that which didn't exist a year or so ago."

Cross-reference line on the page: "My comment on Devtools must be open
source (exe.dev) — Hacker News" (links to
news.ycombinator.com/item?id=49156111#49156719, the specific comment, and
news.ycombinator.com/item?id=49156111, the HN thread itself).
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-crawshaw-devtools-open-source.md` (mined from a
    different Willison post about the same underlying HN thread/exe.dev
    essay) — that note's Claim 5 argues the *economic* case for plugin
    systems is undermined because "the expense of learning the code and
    making a change has dropped dramatically" via agents. This post is
    independent, first-person corroboration of exactly that mechanism from
    Willison's own daily practice: he reports the "time commitment needed to
    read and then modify code" (this note's Claim 2) as the specific
    barrier that LLMs lowered (Claim 3), which is the same underlying
    economic argument the Crawshaw essay makes about plugin/config systems,
    applied here to open-source engagement generally rather than to a
    specific product's extensibility model.
  - `blog-anthropic-code-w-claude-2026.md` Claim 3 ("Executives and managers
    are returning to hands-on coding because AI reduces the time investment
    required to contribute meaningfully") — a structurally identical
    mechanism (LLMs lowering the time-cost of engaging with code) applied to
    a different population (executives re-engaging with their own
    codebases) and a different behavior (contributing code vs. reading
    open-source code). Both sources independently locate the causal
    mechanism in time-investment reduction rather than a skill or tooling
    change.
  - `blog-anthropic-maccoss-developer-onboarding.md` Claim 1 (treating
    Claude "like a new trainee" to build understanding of a large,
    unfamiliar codebase) — corroborates the general pattern of using an LLM
    as an intermediary to build understanding of code the user did not
    write, though that source documents a structured, sustained onboarding
    process for one large internal codebase, while this post describes an
    ad hoc, several-times-a-day habit applied to many different external
    repositories.

- **Contradicts**: None identified. No existing source note asserts that
  LLM-assisted codebase comprehension remains high-friction or that
  compilation/build friction has not been meaningfully reduced by coding
  agents, so no contradiction issue was filed per MINER.md §4a.

- **Extends**: `blog-simonwillison-crawshaw-devtools-open-source.md` —
  that note's Claims 1-2 document two specific, structured *prompts* for
  personalizing software once you have engaged with its source (a one-time
  fork-and-modify prompt and a nightly rebase-and-verify prompt). This post
  documents the *upstream* step that makes those prompts reachable in the
  first place: Willison's own habitual "clone and explain" prompt (Claim 4)
  and his build-delegation pattern (Claim 5) are what get a practitioner
  from "I don't understand this codebase" to "I could now try Crawshaw's
  personalization prompts on it." Read together, the two Willison posts
  (both published 2026-08-03, both surfacing the same underlying exe.dev
  HN discussion) describe a full pipeline: examine (this post) → understand
  and build (this post) → personalize and maintain (the Crawshaw note).

- **Novel**:
  - The explicit reframing of open source's "freedom to examine and modify"
    argument as having been, for most people including experts, a
    *delegated* freedom (exercised via other people, not personally) rather
    than a directly exercised one, with LLMs specifically closing that
    delegation gap — this framing (freedom-in-practice vs.
    freedom-in-principle, tied to a named time-cost mechanism) is new to
    this corpus. `blog-simonwillison-open-source-ai-gap-map.md` covers
    open-source AI ecosystem measurement (product counts, openness scoring)
    but not this friction-reduction argument.
  - The specific, reusable "Clone x/y from GitHub and tell me how Z works"
    prompt template as a named, habitual (multiple-times-a-day) practice by
    a highly-credible practitioner is new to this corpus — no existing
    source documents a comparably concrete "understand an unfamiliar repo"
    prompt used at this reported frequency.
  - The "zero time investment challenge" framing for delegated build/compile
    setup, with an explicit "come back ten minutes later" fire-and-forget
    pattern, is a new concrete instance of async agent delegation applied
    specifically to build-environment setup — a narrower and more specific
    task than the general async/routines patterns already in the corpus
    (`blog-anthropic-claude-code-routines.md`,
    `blog-addyosmani-loop-engineering.md`).

## Guide Impact

- **Chapter 02 (Harness Engineering) or Chapter 03 (Adoption/Productivity
  Patterns)**: Add Claim 4's "Clone x/y from GitHub and tell me how Z
  works" as a named, reusable prompt template for rapid codebase
  comprehension, alongside the existing developer-onboarding material from
  `blog-anthropic-maccoss-developer-onboarding.md` — presenting it as a
  lightweight, ad hoc counterpart to that source's more structured,
  sustained onboarding process. The two differ in scale (single ad hoc
  query vs. maintained project context) and should be presented as
  complementary rather than competing techniques.

- **Chapter 02 (Harness Engineering) — build/setup delegation**: Add Claim
  5's "zero time investment challenge" framing and its specific
  fire-and-forget pattern (issue a checkout-and-build instruction, return
  ten minutes later) as a concrete example of appropriate async delegation
  scope: a bounded, verifiable task (does it build?) well-suited to
  unsupervised agent execution, distinct from the higher-stakes async
  delegation examples already in the corpus (e.g., autonomous PR-opening
  routines).

- **Any section discussing open-source engagement/contribution as an
  AI-native practice**: Use Claims 1-3 (the freedom-in-practice vs.
  freedom-in-principle framing) as the motivating narrative, paired with
  Claim 6's explicit hedge — the guide should be precise that the
  well-evidenced claim here is about *reading/understanding* friction, not
  yet about a demonstrated increase in habitual *modification* of
  third-party software, per Willison's own qualification.

## Extraction Notes

1. **This is a distinct source from the already-mined Crawshaw essay note**,
   despite both being filed from issues discovered the same day
   (2026-08-03) about the same underlying Hacker News thread/exe.dev essay
   title ("Devtools must be open source"). This issue's source URL
   (`simonwillison.net/2026/Aug/3/devtools-must-be-open-source-exedev/`) is
   Willison's own first-person "Comment" beat (a republished HN comment,
   ~180 words, no reference to David Crawshaw by name anywhere in the text).
   The already-merged `blog-simonwillison-crawshaw-devtools-open-source.md`
   was mined from a different URL
   (`simonwillison.net/2026/Aug/3/david-crawshaw/`), Willison's "quotation"
   beat that excerpts a prompt from Crawshaw's linked essay. This Miner
   verified the two pages are structurally different post types (`beat`
   class `note`/comment-source-bar vs. a `blockquote` quotation) with
   entirely non-overlapping body text before proceeding, to avoid filing a
   duplicate note for the same content under a different issue number.
2. **HN thread itself was not readable**: both `WebFetch` and a direct
   `curl` (with a browser user-agent) against
   `news.ycombinator.com/item?id=49156111` returned HTTP 429 (rate-limited)
   on every attempt. The primary filed source — Willison's own weblog page,
   which fully reproduces his comment text — was fetched successfully and
   is a complete, self-contained record of the claims extracted here; no
   claim in this note depends on content that was only visible on the
   unreachable HN page (e.g., other commenters' replies).
3. **All quotes verified against raw HTML**: the page was fetched via
   `curl` and the `<div class="entry entryPage">` / `<div class="note">`
   content block was read directly from the raw response (see line ranges
   57-86 of the fetched HTML), not from a summarizer's paraphrase. Every
   `Quote` field above is a verbatim substring of that raw block, checked
   against the reproduction in Concrete Artifacts.
4. **Cross-reference verification**: before writing citations,
   `blog-simonwillison-crawshaw-devtools-open-source.md`,
   `blog-anthropic-code-w-claude-2026.md`, and
   `blog-anthropic-maccoss-developer-onboarding.md` were each re-read
   directly and all cited claim numbers were confirmed against those notes'
   numbered `### Claim N:` headings in document order.
5. **Confidence rated `anecdotal` overall**: every substantive claim (2-6)
   traces to a single practitioner's self-report of his own habits and
   impressions, with no measurement, no named repository example, and no
   third-party corroboration of frequency or outcome. Claim 1 alone would
   independently rate `settled` (an uncontroversial restatement of the
   open-source freedoms argument), but it is not the source's substantive
   contribution — the overall rating reflects the evidentiary tier of
   Claims 2-6, which is where this source's guide-relevant content lives.
6. **Source is short**: the entire post is approximately 180 words. Six
   claims were extracted by treating each of the post's six paragraphs as a
   distinct claim, which is fewer than MINER.md's suggested 5-15 range;
   this reflects the source's genuine brevity (a single HN comment) rather
   than shallow reading — there is no additional substantive content on the
   page beyond what is reproduced verbatim in Concrete Artifacts, and the
   one linked page (the HN thread) was unreachable per Note 2.
