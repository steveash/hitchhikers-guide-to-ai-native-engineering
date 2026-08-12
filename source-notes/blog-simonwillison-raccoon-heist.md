---
source_url: https://simonwillison.net/2026/Aug/5/raccoon-heist/
source_type: blog-post
title: "One-shotting a Raccoon Heist game using Claude Fable 5"
author: Simon Willison
date_published: 2026-08-05
date_extracted: 2026-08-12
last_checked: 2026-08-12
status: current
confidence_overall: anecdotal
issue: "#2634"
---

# One-shotting a Raccoon Heist game using Claude Fable 5

> Simon Willison gave Claude Fable 5 a single autonomy-granting prompt — build
> a playable 3D browser game from a 2022 GPT-3/DALL-E joke game concept, work
> independently, don't ask for further design decisions — and let it run
> end-to-end: vendoring Three.js, generating its own textures via OpenAI's
> `gpt-image-2` API, self-testing with Playwright to catch a mobile rendering
> bug, and adding an unrequested "dog AI" difficulty escalation, across seven
> commits pushed to a public GitHub repo with a live GitHub Pages demo and a
> published session transcript. The result was technically impressive but,
> by Willison's own assessment, gameplay-mediocre.

## Source Context

- **Type**: blog-post (Simon Willison's weblog, August 5, 2026 — a first-person
  case-study/link-blog post pointing to a live demo, a public GitHub repo
  (`simonw/raccoon-heist`), and a published Claude Code session transcript).
- **Author credibility**: Simon Willison is the creator of Django, Datasette,
  and the `llm` Python CLI, and a trusted-feed source already covered
  extensively in this corpus (e.g. `blog-simonwillison-claude-fable-5.md`,
  `blog-simonwillison-pedalican-sprite-pipeline.md`). No vendor affiliation
  with Anthropic or OpenAI. The claims here are first-person: he wrote the
  prompt, watched the session, and is the one characterizing the final
  gameplay quality.
- **Scope**: Covers one single, non-repeated autonomous build of one browser
  game using Claude Fable 5 (via Claude Code for web / mobile app), OpenAI's
  `gpt-image-2` for texture generation, Three.js for rendering, and
  Playwright for the agent's own testing. Does not cover: cost or token
  totals for the session (not stated in the post), wall-clock build duration
  (not stated), a comparison against other models attempting the same task,
  or any claim that this workflow generalizes beyond simple arcade-style
  games.

## Extracted Claims

### Claim 1: A single autonomy-granting prompt, explicitly forbidding follow-up design questions, was sufficient to drive an end-to-end game build with no further human design input
- **Evidence**: Willison's own account of the prompt he used to kick off the Claude Code session, contrasted with the fully-formed final game he describes.
- **Confidence**: anecdotal (single practitioner, single session, self-reported)
- **Quote**: "Work independently - do not ask me to make any further design decisions."
- **Our assessment**: This is a specific, reusable prompt-design pattern distinct from iterative back-and-forth vibe coding: explicitly revoking the model's ability to pause for clarification forces it to make and commit to design decisions autonomously rather than defer them. It only works because the rest of the prompt (see Claim 2) supplied enough concrete constraints that autonomous decisions had guardrails to work within.

### Claim 2: The autonomy-granting prompt paired "no further questions" with concrete, checkable technical constraints (static entry point, mobile support, vendored dependencies, external image API)
- **Evidence**: Willison's description of the specific directives given alongside the autonomy instruction: a static `index.html` entry point, mobile-friendly touch controls, Three.js vendored without a CDN dependency, and explicit permission/instruction to use OpenAI's image API for textures.
- **Confidence**: anecdotal
- **Quote**: "You have an OpenAI API key and access to their image generation model APIs, use that for textures to use with your 3D models."
- **Our assessment**: The "work independently" instruction (Claim 1) is not free-floating license — it's bounded by a handful of concrete, verifiable constraints (static HTML, mobile touch, vendored JS, a named external API to call). This suggests the generalizable pattern isn't "give total autonomy" but "give autonomy bounded by a short list of hard, checkable requirements the model can self-verify against," which is a more actionable guide recommendation than "let the agent decide."

### Claim 3: The agent was directed to use a cross-vendor tool (OpenAI's image generation API) from inside an Anthropic coding agent session, and did so to generate all in-game textures and title art
- **Evidence**: Willison's account states the prompt explicitly authorized calling OpenAI's `gpt-image-2` model for texture generation, and that the agent used it for both gameplay textures and title-screen artwork.
- **Confidence**: anecdotal
- **Quote**: Model name and directive — "`gpt-image-2`" for texture generation, per the prompt: "use that for textures to use with your 3D models."
- **Our assessment**: This is a concrete example of cross-provider tool composition within a single agentic session — the coding model (Claude Fable 5) treats a competing vendor's generative API as just another tool call, no different in kind from any other API integration. Practitioners building agentic pipelines should not assume "use only same-vendor tools" is a meaningful constraint; the coding agent's tool-use loop is provider-agnostic if given credentials and a directive.

### Claim 4: The agent used Playwright to take its own screenshots, detected a mobile-specific rendering bug from those screenshots, and fixed it without human intervention
- **Evidence**: Willison's account of the agent self-testing across a mobile viewport and identifying that key game objects were not visible, then correcting the issue.
- **Confidence**: anecdotal
- **Quote**: "The raccoon, dumpster hideout, and both crew raccoons are now perfectly visible on mobile."
- **Our assessment**: This is a same-agent, self-administered visual QA loop (the agent that wrote the rendering code also screenshotted and judged it), which is a narrower case than `failure-htdt-godogen-game-generation.md`'s architecture of a *separate* vision-model evaluator with no code access. Godogen's Lesson 4 argues self-review "cannot reliably detect visual, spatial, or behavioral failures" and recommends an external evaluator; this single data point is a counter-example for at least one class of bug (object visibility on a viewport), where same-agent screenshot review did catch and fix a real problem. It does not contradict Godogen's broader claim (which concerns z-fighting, floating objects, physics explosions, and grid-like placement — subtler classes of spatial defect than "objects aren't rendering at all") but it's worth noting as a boundary case: self-administered screenshot testing works for coarse visibility bugs even without an independent evaluator.

### Claim 5: The agent added a difficulty-escalation feature (a patrolling guard dog appearing after a fixed number of in-game nights) that was not part of the original prompt
- **Evidence**: Willison's account of the agent's own design addition beyond the literal spec, describing it as his favorite unrequested change.
- **Confidence**: anecdotal
- **Quote**: "New escalation: from night 3 the yards get a patrolling guard dog — a low-poly brown hound."
- **Our assessment**: Under the "work independently, no further questions" directive (Claim 1), the model didn't just fill gaps mechanically — it invented and shipped a game-design feature (progressive difficulty via a new enemy type) that wasn't specified anywhere in the prompt. This is a concrete instance of autonomous creative elaboration beyond literal instruction-following, which is a distinct capability from "correctly implements what was asked."

### Claim 6: The prompt required the agent to maintain a running `notes.md` development log, updated as part of every commit
- **Evidence**: Willison's account of a specific documentation requirement baked into the initial instructions, intended to make the session's decisions traceable.
- **Confidence**: anecdotal
- **Quote**: "Append to a notes.md file as you work, including your changes to that as part of every commit."
- **Our assessment**: A specific, adoptable practice for autonomous/unsupervised agent sessions: require a persistent, append-only development log co-committed with every code change, so a human reviewing after the fact (or resuming a compacted session) can reconstruct the agent's own account of what it did and why — independent of the commit messages or diffs themselves. This parallels the "notebook as durable state" pattern already documented in `blog-simonwillison-pedalican-sprite-pipeline.md` (GPT-5.6 Sol's 1701-line `notes-on-creating-a-pet.md`), now corroborated cross-vendor (Claude Fable 5) and cross-domain (a 3D game rather than a sprite pipeline).

### Claim 7: The entire project, from initial prompt through final polish, was conducted from a mobile phone rather than a desktop development environment
- **Evidence**: Willison's own statement about how he ran the session, and his description of the available surfaces for starting a Claude Code session.
- **Confidence**: anecdotal
- **Quote**: "This entire project was conducted on mobile"
- **Our assessment**: This is a concrete accessibility data point: a multi-hour, multi-commit, multi-tool (Three.js + OpenAI image API + Playwright + GitHub) autonomous coding session was initiated and steered entirely from a phone, with no desktop terminal involved. It corroborates the general trend (already present elsewhere in this corpus) toward Claude Code surfaces converging in capability — "Claude Code for web session, in the Claude iPhone or Desktop apps or in the browser" are presented as interchangeable entry points to the same underlying agentic capability.

### Claim 8: The build produced a public, verifiable artifact trail — seven commits, a live GitHub Pages demo, a public repo, and a published raw session transcript — rather than just a narrated summary
- **Evidence**: Willison links to the live game, the GitHub repository, and an HTML export of the full Claude Code session transcript.
- **Confidence**: settled (the artifacts themselves are independently checkable, not just narrated claims)
- **Quote**: "Raccoon Heist is built, tested, and pushed — 7 commits on `claude/3d-raccoon-heist-game-50n293`"
- **Our assessment**: Unlike many "I asked an AI to build X" case studies where readers must take the author's description on faith, this post is fully auditable: the live demo (https://simonw.github.io/raccoon-heist/), the source repo (https://github.com/simonw/raccoon-heist/), and the transcript (https://simonw.github.io/raccoon-heist/transcript/page-001.html) are all public. This raises the evidentiary bar above typical anecdotal blog-post claims, even though the underlying sample size is still one session by one practitioner.

### Claim 9: Despite being technically impressive as a one-shot build, the resulting game was gameplay-mediocre, reinforcing that AI-driven implementation speed does not translate into game design quality
- **Evidence**: Willison's own closing verdict on this build, plus a broader generalization he draws from his own prior vibe-coded game projects.
- **Confidence**: anecdotal
- **Quote**: On this build — "As a finished game project, it's mediocre. As a starting point from a single prompt I think it's very impressive." On the general pattern, from the same closing paragraph — "They've all been deeply disappointing from a gameplay perspective—it turns out designing games that are *fun* remains a uniquely human trait."
- **Our assessment**: The stronger of these two statements is the general one, and it is worth reading precisely: Willison is generalizing across *his own* repeated attempts ("I've vibe coded up quite a few games now"), which is a within-practitioner repeated observation rather than a cross-practitioner replication. That still exceeds the evidentiary weight of a one-session anecdote, but it is not independent corroboration. Taken at that weight, it's a blunt calibration point for guide readers: "one-shot, autonomous, well-tooled agentic build" is now demonstrably achievable end-to-end (working 3D game, generated art, mobile support, self-tested), but the bottleneck has moved to game/product design judgment, which the agent did not meaningfully supply even when explicitly given full creative latitude (Claim 1). Note that Willison scopes the limitation to himself as well as the model ("more skill and experience than either Claude or I can bring to bear"), so this is not a clean claim that models specifically cannot design fun games.

## Concrete Artifacts

Initial autonomy-granting prompt (partial, as quoted by Willison):
```
Build this 3D game, for the browser.
[...concept + reference images from a 2022 GPT-3/DALL-E-generated
"raccoon heist" product description...]

Work independently - do not ask me to make any further design decisions.
```
*Source: Simon Willison, simonwillison.net/2026/Aug/5/raccoon-heist/*

Documentation requirement embedded in the initial prompt:
```
Append to a notes.md file as you work, including your changes to that
as part of every commit.
```
*Source: Simon Willison, simonwillison.net/2026/Aug/5/raccoon-heist/*

Texture-generation directive embedded in the initial prompt:
```
You have an OpenAI API key and access to their image generation model
APIs, use that for textures to use with your 3D models.
```
*Source: Simon Willison, simonwillison.net/2026/Aug/5/raccoon-heist/*

Session/build surfaces described as interchangeable entry points:
```
Start a Claude Code for web session, in the Claude iPhone or Desktop
apps or in the browser
```
*Source: Simon Willison, simonwillison.net/2026/Aug/5/raccoon-heist/*

Published artifact trail:
```
Live demo:            https://simonw.github.io/raccoon-heist/
GitHub repository:     https://github.com/simonw/raccoon-heist/
Session transcript:    https://simonw.github.io/raccoon-heist/transcript/page-001.html
Commits:               7, on branch claude/3d-raccoon-heist-game-50n293
Rendering:             Three.js (vendored, no CDN)
Textures/art:          OpenAI gpt-image-2
Testing:               Playwright (agent-driven screenshot QA)
Audio:                 procedurally generated via WebAudio
```
*Source: Simon Willison, simonwillison.net/2026/Aug/5/raccoon-heist/*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-pedalican-sprite-pipeline.md` (Source Context — the
    1701-line `notes-on-creating-a-pet.md` notebook file that Willison states
    was written by the model itself, not by him): this source's
    `notes.md`-per-commit requirement (Claim 6) produces the same artifact
    class — a durable external log of an autonomous agent's own decisions,
    written by the agent — applied to a different vendor (Claude Fable 5 vs.
    GPT-5.6 Sol) and domain (full game vs. sprite atlas). The difference
    worth noting for the guide: in pedalican the notebook is an emergent
    output of the skill, whereas here it is an explicit prompt directive
    with a commit-coupling requirement, which is the more reproducible form.
  - `blog-simonwillison-claude-fable-5.md` (Claim 9, Fable 5 producing
    publishable-quality API design/tests/code/docs in a single session):
    this source extends that claim from library code to a full creative,
    multi-tool application build (3D rendering, external image API,
    browser testing, deployment), reinforcing that Fable 5's single-session
    end-to-end capability is not limited to conventional software
    engineering tasks.

- **Related but NOT corroborating** (recorded explicitly to prevent a future
  synthesis from over-reading it):
  - `failure-htdt-godogen-game-generation.md` does **not** contain an author
    claim that AI-generated games disappoint on gameplay. Its Root Cause
    section names three *engineering* bottlenecks (GDScript training-data
    scarcity, build-time vs. runtime state confusion, agent self-bias in
    evaluation), and its eight numbered Lessons are all engineering/pipeline
    lessons. The only gameplay-quality material in that note is in Source
    Context → Community response, which records HN commenters' skepticism
    about "output polish and gameplay depth" — third-party commenters, not
    the author's finding. Claim 9 here therefore stands on Willison's own
    repeated experience alone; it is **not** a second independent source
    replicating a Godogen conclusion, because Godogen makes no such
    conclusion.

- **Contradicts**: None identified against an existing source note. Claim 4's
  "self-administered screenshot QA caught a real bug" is a nuance against,
  not a contradiction of, `failure-htdt-godogen-game-generation.md`'s
  self-bias warning — see the "Our assessment" under Claim 4 for why this is
  a boundary case (coarse visibility bug vs. Godogen's subtler spatial/physics
  defect classes) rather than a genuine claims conflict; no contradiction
  issue filed per MINER.md §4a.

- **Extends**: `blog-simonwillison-claude-fable-5.md` — moves from a
  library/tooling case study to a full autonomous creative-application build,
  the first in this corpus to combine 3D rendering, cross-vendor generative
  image APIs, agent-driven browser testing, and unsupervised multi-day-scope
  design elaboration in one session.

- **Novel**:
  - First source note in this corpus documenting an explicit "work
    independently — do not ask me to make any further design decisions"
    prompt pattern as a deliberate technique for one-shot autonomous builds,
    paired with a short list of hard, checkable constraints (Claims 1–2).
  - First documented instance of a Claude coding agent calling a competing
    vendor's (OpenAI) generative image API as a routine tool call within an
    otherwise Anthropic-only session (Claim 3).
  - First fully-public, independently-auditable artifact trail (live demo +
    repo + raw session transcript) for a one-shot creative build in this
    corpus (Claim 8) — most prior case studies rely on the author's narrated
    description alone.
  - First documentation of a whole multi-tool, multi-hour agentic coding
    session run entirely from a mobile phone, with no desktop terminal
    involved (Claim 7).

## Guide Impact

- **Chapter on prompt/task design for autonomous agent sessions**: Add the
  "work independently — do not ask me to make any further design decisions"
  pattern (Claim 1) as a specific, reusable technique for one-shot builds,
  with the caveat from Claim 2 that it should be paired with a short list of
  concrete, checkable constraints (static entry point, target platform
  support, dependency vendoring rules, named external tools/credentials the
  agent is authorized to use) rather than issued as unconstrained license.

- **Chapter on multi-tool / cross-vendor agent workflows**: Cite Claim 3 as a
  concrete example that a coding agent's tool-use loop is provider-agnostic —
  a Claude Code session calling OpenAI's `gpt-image-2` for texture generation
  with no special integration work beyond an API key and a directive.

- **Chapter on agent self-verification / QA loops**: Cite Claim 4 alongside
  `failure-htdt-godogen-game-generation.md`'s self-bias warning as a paired
  example: same-agent screenshot review can catch coarse visual bugs (objects
  simply not rendering) but the Godogen source's stronger claim — that
  subtler spatial/physics defects need an independent, code-blind evaluator —
  is not undermined by this single counter-data-point. Recommend: use
  same-agent screenshot checks for cheap "is this basically working" gates,
  but keep an independent evaluator for launch-quality visual QA.

- **Chapter on AI-generated game/creative-application quality**: Add Claim 9
  as the corpus's first substantive data point on this specific question:
  autonomous, well-tooled agentic builds now clear the "does it technically
  work" bar for small interactive applications, but game/product design
  judgment remains the bottleneck and was not supplied even under an
  explicit full-autonomy directive. Attribute it carefully — this is one
  practitioner generalizing across his own repeated attempts ("I've vibe
  coded up quite a few games now"), not a replication across practitioners,
  and Willison scopes the limitation to himself as well as the model. Do
  **not** cite `failure-htdt-godogen-game-generation.md` as corroboration
  here; that note's author makes engineering claims, not gameplay-quality
  claims (see Cross-References → "Related but NOT corroborating"). If the
  chapter wants a second data point, it needs a genuinely new source.

## Extraction Notes

- The WebFetch tool declined to reproduce the article's full text verbatim
  (correctly, as that would exceed fair-use bounds for a copyrighted blog
  post), so extraction was done via several narrower, targeted fetches each
  asking for specific short quotes (under 25 words) or structured
  summarization in the fetcher's own words. All quotes above were obtained
  this way and cross-checked for consistency across separate fetch calls
  that independently returned the same wording.
- No sub-pages were followed beyond the blog post itself. The linked GitHub
  repo, live demo, and raw session transcript were not separately fetched in
  full — their existence and URLs are cited from the blog post's own links,
  consistent with MINER.md's "up to 5 linked pages" guidance being a ceiling,
  not a requirement, and the post itself supplying enough substantive,
  quotable content on its own.
- The post does not state total session cost, token spend, or wall-clock
  build duration — flagged in Source Context as an explicit scope gap rather
  than omitted by oversight.
- Three separate (near-duplicate) Prospector triage comments were present on
  the source issue, apparently from repeated triage runs; all three agreed
  on high novelty and blog-post type, so no ambiguity in triage guidance.
- **Post-review correction (2026-08-12)**: the first draft of this note
  attributed the "vibe coded games consistently disappoint from a gameplay
  perspective" framing to `failure-htdt-godogen-game-generation.md` (at a
  non-existent "Lesson 9") and treated Claim 9 as independent replication of
  it. That was wrong twice over: the phrasing is Willison's own, in *this*
  post's closing paragraph, and the Godogen note contains no author claim
  about gameplay quality at all. Both the Cross-References and Guide Impact
  entries were rewritten, and the actual Willison sentence was re-fetched
  and added to Claim 9's Quote field where it belonged in the first place.
  The `blog-simonwillison-pedalican-sprite-pipeline.md` corroboration was
  also re-pointed from "Claim 8" (which is about `hatch-pet`-to-`imagegen`
  skill delegation) to that note's Source Context, where the 1701-line
  notebook is actually described.
- No contradiction with an existing source note was found; the one nuance
  worth flagging (Claim 4 vs. Godogen's self-bias warning) is a boundary
  case explained inline, not a genuine conflict, so no contradiction issue
  was filed.
