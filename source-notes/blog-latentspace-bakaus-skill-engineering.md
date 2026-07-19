---
source_url: https://www.latent.space/p/skill-engineering-design
source_type: blog-post
title: "Skill engineering and the case against one-shot AI design"
author: Richard MacManus (Latent Space), featuring Paul Bakaus (creator of Impeccable)
date_published: 2026-07-02
date_extracted: 2026-07-19
last_checked: 2026-07-19
status: current
confidence_overall: anecdotal
issue: "#2033"
---

# Skill engineering and the case against one-shot AI design

> A dedicated Latent Space profile of Paul Bakaus, creator of the open-source
> design skills system Impeccable, arguing that "skill engineering" is an
> emerging discipline in its own right — giving agents a precise, operational
> vocabulary for design terms — and that Impeccable will permanently have "no
> auto mode," with agents handling roughly the first 80% of design work and a
> human always retained for the final 20% where taste and authorship live.

## Source Context

- **Type**: blog-post — a same-day, dedicated journalistic profile (not a
  transcribed Q&A), published on Latent Space (Richard MacManus, byline
  confirmed via page metadata) on 2026-07-02.
- **Author credibility**: Richard MacManus is a named, recurring Latent Space
  byline already represented multiple times in this corpus (e.g.
  `blog-latentspace-aiewf-autoresearch-agency-dispatch.md`,
  `blog-latentspace-meurer-agent-engineer-fde.md`). Latent Space (swyx) is a
  `trusted-feed` source in this repo's scanning configuration. The
  substantive claims are MacManus's paraphrase of Bakaus's AI Engineer
  World's Fair (AIEWF) session and workshop, interleaved with direct quotes
  attributed to Bakaus — this is first-person conference/interview
  journalism about a single named practitioner's product and philosophy, not
  an independently verified transcript or a study.
- **Scope**: Covers Bakaus's rejection of one-shot AI design, the "skill
  engineering" discipline (skill/model creativity limits, cross-harness
  portability, routing inside skills), Impeccable's design-vocabulary
  translation layer, the convergence of design/engineering/PM roles,
  Impeccable's live mode, and Bakaus's explicit "no auto mode" principle
  including his rejection of "software factories" framing. Does NOT cover:
  Impeccable's pricing, user counts beyond the "at least half" designer
  estimate, technical implementation details of the skill system, or any
  data/benchmark evidence — this is a philosophy-and-product profile, not a
  technical deep-dive or a measured study.

## Extracted Claims

### Claim 1: Bakaus designed Impeccable explicitly to give humans a way to steer AI-generated design output rather than to produce a finished design in one shot
- **Evidence**: Direct quotes from Bakaus's AIEWF session, captured by MacManus.
- **Confidence**: anecdotal (single founder's stated design intent for his own product, no user data)
- **Quote**: "The point is to give you a way to steer what you want to end up with," he said during a session at the AI Engineer World's Fair. "It's never going to be a tool for one-shot design. That's not the intent."
- **Our assessment**: This is the article's thesis statement and gives the guide a clean, named articulation of "steering, not one-shot generation" as a deliberate design-tool philosophy, distinct from a general "AI isn't good enough yet for one-shot design" capability claim — Bakaus frames it as an intentional, permanent design choice rather than a temporary limitation.

### Claim 2: Skill engineering is an emerging discipline in its own right, partly because most skills and models default toward homogeneous, convergent creative output
- **Evidence**: Bakaus's account of his AIEWF workshop, described as exploring the "dark arts" of building skills, plus a direct quote on model/skill creativity limits.
- **Confidence**: anecdotal (single practitioner's workshop framing and observation, no measurement of "convergence" across skills or models)
- **Quote**: "One of the interesting topics was that most skills — [and] most models — are not very creative," Bakaus told me. "They converge in one direction, and if everybody uses the same skill to do frontend design work or something like that, everything ends up looking the same."
- **Our assessment**: This names a specific, checkable risk of skill-based agent design — homogenization of output when many users share the same skill — that is new to this corpus's coverage of Claude Code Skills (`blog-anthropic-claude-code-skills-lessons.md`), which documents skills as a widely-used extension point (Claim 1) but does not address a homogenization risk. Worth flagging as a caution alongside any guide recommendation to adopt shared/public skills.

### Claim 3: Skill engineers must design for differences in how agent harnesses and models handle subagents and permissions — a skill built for one harness cannot assume identical capabilities in another
- **Evidence**: MacManus's paraphrase of Bakaus's account of cross-harness skill portability, naming Codex and Claude as an example pairing, and Claude Code, Cursor, GitHub Copilot, and Codex as the four target harnesses.
- **Confidence**: anecdotal (practitioner's stated design constraint, no specific failure example given)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This is a concrete, actionable engineering constraint for anyone authoring a skill intended for multi-harness distribution — it names the specific failure axis (subagent handling, permissions) rather than a generic "test on multiple tools" caution. New to the corpus's skills coverage, which so far treats Skills primarily from within a single harness (Claude Code).

### Claim 4: Bakaus has experimented with routing inside a skill — combining several capabilities and directing a task toward the relevant instructions — comparing the approach to a mixture-of-experts model used both to conserve tokens and improve effectiveness
- **Evidence**: MacManus's paraphrase of Bakaus's described technique.
- **Confidence**: anecdotal (single practitioner's experimental technique, no benchmark or before/after comparison given)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This is a concrete architectural pattern for skill design — routing sub-tasks to the relevant instruction subset within a single skill rather than loading the full skill context every time — offered as a token-conservation and effectiveness technique. It is new to the corpus and complements `blog-addyosmani-loop-engineering.md` Claim 6 (skills as externalized, one-time-written intent that stop an agent re-deriving context every session), by adding an internal-routing refinement that Osmani's post does not mention.

### Claim 5: Impeccable's core innovation is translating designer vocabulary (e.g. "bolder") into precise, operational concepts (hierarchy, scale, decisive typography) rather than leaving the model to interpret the adjective unassisted
- **Evidence**: MacManus's description of the translation mechanism, illustrated by contrasting an unassisted model's likely response ("gradients, neon effects or glass-like surfaces") against Impeccable's defined response, plus a direct quote.
- **Confidence**: anecdotal (single product's design mechanism as described by its creator, no comparison test between assisted and unassisted output shown)
- **Quote**: "An adjective with nothing behind it is just a nice apostrophe," Bakaus said. "You really have to tell the agent what you mean."
- **Our assessment**: This is the most quotable, concrete design-vocabulary mechanism in the piece — it operationalizes the general "give agents domain knowledge, not just instructions" principle already present elsewhere in the corpus's harness-engineering sources into a worked example specific to design output. Useful as a template for how any domain-specific skill might translate ambiguous adjectives into checkable properties.

### Claim 6: Bakaus observed large differences in output quality between a designer and an engineer using the same underlying model, attributable specifically to the designer's ability to articulate the desired result in precise vocabulary
- **Evidence**: MacManus's paraphrase of Bakaus's stated observation, followed by a direct quote on compressing that vocabulary into a system.
- **Confidence**: anecdotal (single practitioner's informal observation, no controlled comparison or sample size given)
- **Quote**: "I've been trying to put that language — basically compress it into a skill and into a system — to be able to express yourselves better," he said.
- **Our assessment**: This corroborates the "taste"/vocabulary-as-differentiator theme already present in this corpus (e.g. `blog-latentspace-meurer-agent-engineer-fde.md` Claim 5, where Meurer independently names "taste" — judgment about what feels human and high-quality — as the irreducible human skill in agent engineering). Bakaus's version is more specific: the differentiator isn't taste in the abstract but a learned, articulable vocabulary that Impeccable is explicitly trying to encode and distribute.

### Claim 7: Bakaus does not believe every part of design should be controlled through skill-level abstraction — some tasks (e.g. small spacing adjustments) are faster done directly, and open-ended prompting still has a role during initial exploration
- **Evidence**: MacManus's paraphrase of Bakaus's stated position, plus a direct partial quote on the goal of the system.
- **Confidence**: anecdotal (single practitioner's stated design philosophy, no usage data on when each mode is actually chosen)
- **Quote**: "the exact level of control"
- **Our assessment**: This is a nuance worth preserving for the guide: Bakaus is not arguing agents/skills should mediate all interaction with a design system, only that the *right* level of control should be deliberately chosen per task rather than defaulting either to raw prompting or to full skill-mediated abstraction. This tempers Claim 1's steering-not-one-shot framing with an explicit acknowledgment that direct manipulation remains appropriate for some tasks.

### Claim 8: Bakaus sees the boundaries between design, engineering, and product-management roles becoming less distinct, with designers now needing to think more about the "what" and product managers and designers converging
- **Evidence**: Direct quotes from Bakaus's session remarks.
- **Confidence**: anecdotal (single practitioner's observation of role convergence, no organizational data)
- **Quote**: "Designers are moving into code, engineers are moving into design, and vice versa," he said. "These worlds are all colliding." … "Designers all have to move one layer up the stack to think more about the what," he said. "I think the role of the product manager and designer is actually converging."
- **Our assessment**: This corroborates `blog-latentspace-meurer-agent-engineer-fde.md` Claims 7-9 (Natalie Meurer's prediction that product engineering and forward-deployed engineering are converging toward a more generalist, holistic role definition) from a different discipline (design rather than agent-engineering roles), and is consistent in direction though not identical in mechanism — Meurer's convergence is driven by cheap code authorship shortening the customer-insight-to-product distance, while Bakaus's is driven by agents absorbing the "how" and leaving humans the "what."

### Claim 9: Designers now make up at least half of Impeccable's user base, using it as a bridge between their own vocabulary and code implementation — a result Bakaus says he did not anticipate
- **Evidence**: MacManus's paraphrase of a stated usage estimate, plus a direct quote on why designers adopted it.
- **Confidence**: anecdotal (single founder's self-reported, unaudited usage estimate for his own product)
- **Quote**: "So rather than moving directly into code and, you know, having no help," Bakaus said about designers, "they use Impeccable as a bridge, because it communicates the way they communicate. And that was not obvious to me when I first built it."
- **Our assessment**: This is a concrete, checkable-in-principle product-adoption data point (though self-reported and unaudited) showing that a tool built with engineers as the assumed primary audience found substantial pull from designers instead — a useful corrective for any guide content that assumes agent-native tools are adopted along traditional role lines.

### Claim 10: Impeccable includes a "live mode" combining visual section selection with an underlying coding agent, operating within the project's existing code and design system rather than exporting an isolated mockup — which Bakaus describes as a potential "design harness"
- **Evidence**: MacManus's description of the live-mode feature and its workflow, plus a direct quote naming it.
- **Confidence**: anecdotal (feature description from the product's creator, no usage or adoption data for this specific mode)
- **Quote**: "design harness"
- **Our assessment**: The "design harness" framing is a novel extension of this corpus's harness vocabulary (previously scoped to coding/agent harnesses, e.g. `blog-addyosmani-loop-engineering.md`'s Linked Source 1, "Agent Harness Engineering") into design tooling specifically — a harness that sits at the intersection of chat-based instruction and direct visual manipulation, operating on real project code rather than an exported mockup. This is new to the corpus and worth flagging as a parallel-domain application of harness thinking.

### Claim 11: Bakaus rejects full automation ("loopmaxxing") as well as the traditional fully-manual Figma-centered workflow, landing on an 80/20 split where agents handle the first 80% of design work quickly and a human retains the final 20% for taste, context, and point of view
- **Evidence**: MacManus's framing of the two opposing camps Bakaus positions himself against, plus a direct quote on the resolution.
- **Confidence**: anecdotal (single founder's stated design philosophy for his own product)
- **Quote**: "The truth is somewhere in the middle," he said.
- **Our assessment**: This claim and its underlying 80/20 split are already documented in this corpus at `blog-latentspace-aiewf-autoresearch-agency-dispatch.md` Claim 7, sourced from the same AIEWF session and a follow-up interview by the same journalist (MacManus) — this article is that publication's dedicated, longer-form companion piece on the same event, published the same day. The specific term "loopmaxxing" for the full-automation camp does not appear in the dispatch note's extracted text and is new framing vocabulary this article adds. Treat this claim as corroborating and extending, not introducing, the dispatch note's Claim 7 — see Cross-References.

### Claim 12: Bakaus states Impeccable will permanently have no automatic mode, despite repeated user requests, because people need purpose and want to feel ownership over what they create
- **Evidence**: Direct quotes from Bakaus, one on the permanent design decision and one on the underlying motivation.
- **Confidence**: anecdotal (single founder's stated, non-negotiable product principle and personal rationale)
- **Quote**: "There is no auto," he said, "and there will be no auto." … "People need purpose, and they want to play a role in whatever they create," Bakaus said. "When you work with the agent, then you feel more ownership of the product."
- **Our assessment**: This is a near-verbatim duplicate of `blog-latentspace-aiewf-autoresearch-agency-dispatch.md` Claim 8, sourced from the same session/interview. Do not treat as an independently corroborating second source — it is the same underlying quotes reproduced in a second article by the same journalist. See Cross-References.

### Claim 13: Asked directly about "software factories" and visions that remove people from engineering altogether, Bakaus stated unambiguous opposition
- **Evidence**: MacManus's framing of the question and Bakaus's direct, one-line response.
- **Confidence**: anecdotal (single practitioner's stated position in response to a direct question, no elaboration given beyond the quote)
- **Quote**: "I'm squarely against that."
- **Our assessment**: This is new to the corpus's Bakaus coverage — the existing dispatch note (`blog-latentspace-aiewf-autoresearch-agency-dispatch.md`) does not cover Bakaus's position on "software factory" vocabulary at all. It extends this corpus's existing "software factory" contested-vocabulary thread (`blog-latentspace-aiewf-loops-software-factories-dispatch.md`; Geoffrey Litt's rejection of the metaphor in the autoresearch dispatch's Claim 4) with a second named practitioner explicitly rejecting the framing, from a design-tooling rather than a general-engineering perspective.

## Concrete Artifacts

```
Source: Latent Space, "Skill engineering and the case against one-shot AI
design" (Richard MacManus, 2026-07-02)

Section structure of the article, in order:
  1. (untitled intro) — Bakaus's steering-not-one-shot thesis
  2. "The emerging craft of skill engineering" — convergence risk,
     cross-harness portability, routing/mixture-of-experts
  3. "Giving agents a design vocabulary" — the "bolder" -> hierarchy/scale/
     typography translation, level-of-control framing
  4. "Designers and engineers move up the stack" — role convergence,
     designer adoption (at least half of audience), live mode / "design
     harness"
  5. "There will be no auto mode" — loopmaxxing vs. Figma-centered camps,
     the 80/20 split, "no auto" principle, rejection of "software factories"

Named products/tools mentioned: Impeccable (Bakaus's design skills system),
Anthropic's frontend design skill (Impeccable's origin point), Claude Code,
Cursor, GitHub Copilot, Codex.
```

## Cross-References

- **Corroborates**:
  - `blog-latentspace-aiewf-autoresearch-agency-dispatch.md` Claim 7 (the
    80/20 agent/human design split) and Claim 8 ("no auto, and there will
    be no auto," plus the purpose/ownership rationale): this article's
    Claims 11 and 12 reproduce the same underlying AIEWF session and
    follow-up interview quotes from the same journalist (MacManus),
    published the same day (2026-07-02). This is the deep, dedicated
    companion piece to that dispatch's brief two-claim treatment of
    Bakaus — not an independent second source. The guide should cite one
    canonical source for these two quotes, not both notes as separate
    corroboration.
  - `blog-latentspace-meurer-agent-engineer-fde.md` Claim 5 ("taste" as the
    irreducible human-judgment quality in agent engineering, illustrated via
    voice-agent design) and Claims 7-9 (role convergence toward generalist,
    holistic definitions): this article's Claim 6 (designer vocabulary as
    the differentiator between designer- and engineer-produced output) and
    Claim 8 (design/engineering/PM role convergence) independently name
    similar dynamics from a design-tooling perspective rather than an
    agent-engineering-role perspective.
  - `blog-addyosmani-loop-engineering.md` Claim 6 (skills as externalized,
    one-time-written intent that stop an agent re-deriving context every
    session): this article's Claim 4 (routing inside a skill, compared to a
    mixture-of-experts model) is a complementary, more advanced skill-design
    technique not mentioned in Osmani's post.

- **Contradicts**: None filed. This article's rejection of "loopmaxxing" and
  "software factories" (Claims 11, 13) sits in the same ongoing, already-
  documented automation-vs-human-agency tension covered by
  `blog-latentspace-aiewf-autoresearch-agency-dispatch.md` and
  `blog-latentspace-aiewf-loops-software-factories-dispatch.md` — this is a
  differing normative position on an open question (how much to automate
  design work), not a claim-vs-claim factual disagreement that would drive
  opposite guide advice, per MINER.md §4a's "when NOT to file" guidance.

- **Extends**:
  - `blog-latentspace-aiewf-autoresearch-agency-dispatch.md`: extends
    Claims 7-8's brief, conference-dispatch-level coverage of Bakaus with a
    full-length profile covering the "skill engineering" discipline,
    cross-harness portability, the design-vocabulary translation mechanism,
    role convergence, live mode, and — genuinely new — Bakaus's explicit
    rejection of "software factories" framing (Claim 13), which the dispatch
    note does not cover for Bakaus at all.
  - `blog-anthropic-claude-code-skills-lessons.md`: extends Claim 1 (skills
    as a widely-used Claude Code extension point) with a specific origin
    story — Impeccable "began as a relatively simple extension of
    Anthropic's frontend design skill" — and a homogenization risk (Claim 2
    here) not raised in that note.
  - `blog-latentspace-aiewf-loops-software-factories-dispatch.md`: extends
    the corpus's "software factory" contested-vocabulary coverage with a
    second named practitioner (Bakaus, design-tooling domain) explicitly
    rejecting the framing, alongside the existing Geoffrey Litt data point
    documented in `blog-latentspace-aiewf-autoresearch-agency-dispatch.md`
    Claim 4.

- **Novel**:
  - "Skill engineering" as a named discipline distinct from "loop
    engineering" (`blog-addyosmani-loop-engineering.md`) and "harness
    engineering" — this corpus now has three separate named "-engineering"
    disciplines coined by different practitioners in the same period; skill
    engineering is specifically about designing a domain vocabulary and
    portability layer for a single skill, not about scheduling/automation
    (loop engineering) or overall agent-scaffold architecture (harness
    engineering).
  - The convergence/homogenization risk of shared skills (Claim 2) — new to
    the corpus's skills coverage.
  - Cross-harness skill-portability constraints around subagent/permission
    handling (Claim 3) and routing-inside-a-skill as a mixture-of-experts-
    style technique (Claim 4) — both new, concrete skill-authoring
    considerations.
  - The design-vocabulary translation mechanism ("bolder" -> hierarchy,
    scale, decisive typography) and the "design harness" framing for
    Impeccable's live mode (Claims 5, 10) — new to the corpus.
  - Bakaus's explicit "I'm squarely against that" rejection of "software
    factories" (Claim 13) — new to the corpus's Bakaus coverage.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the design-vocabulary
  translation mechanism (Claim 5 — turning ambiguous adjectives like
  "bolder" into checkable properties such as hierarchy/scale/typography) as
  a worked, domain-specific example of the general "give agents precise,
  operational meaning rather than raw instructions" principle. Add the
  cross-harness skill-portability caution (Claim 3) to any guide content on
  authoring skills intended for distribution across multiple agent harnesses
  (Claude Code, Cursor, GitHub Copilot, Codex) — this is a concrete failure
  axis (subagent/permission handling) not currently named in the guide's
  skills coverage.

- **Chapter 01 (Daily Workflows) or Chapter 03 (Practitioner Patterns)**: If
  the guide cites Bakaus's 80/20 split and "no auto" principle (already
  recommended for Chapter 03 via `blog-latentspace-aiewf-autoresearch-
  agency-dispatch.md`'s Guide Impact), cite this article as the canonical,
  fuller-context source rather than the brief dispatch mention — it is the
  same underlying quotes with substantially more surrounding argument
  (Claims 1, 7, 11 here explain *why* Bakaus rejects one-shot design and
  full automation, not just *that* he does).

- **Chapter 05 (Team Adoption)**: Add Bakaus's explicit rejection of
  "software factories" (Claim 13) alongside Geoffrey Litt's tweeted
  objection (already recommended for Ch05 via the autoresearch dispatch
  note) as a second named practitioner pushing back on "factory" framing —
  strengthening the case that the guide should not present "factory"
  vocabulary as uncontested.

## Extraction Notes

- **Fetch method**: WebFetch's summarizing model initially returned a short,
  clearly-summarized digest ("Key Concepts" bullet format) rather than
  verbatim article text, and on a second attempt incorrectly characterized
  the piece as a Q&A transcript before self-correcting. Per MINER.md §2a,
  neither summarized pass was used as a quote source. The raw HTML was
  fetched directly via `curl` with a browser user agent and parsed to plain
  text; every quote in this note was copied character-for-character from
  that parsed raw-HTML text, not from either WebFetch summary. The full
  article body (title through the closing "I'm squarely against that" line)
  was captured this way and read in its entirety — there is no additional
  content beyond what is extracted here; the piece is a focused, single-page
  profile (~900 words) with no linked sub-pages substantive enough to follow.
- **Overlap with existing corpus content**: This article and
  `blog-latentspace-aiewf-autoresearch-agency-dispatch.md` cover the same
  underlying AIEWF session and follow-up interview with Bakaus, published
  the same day by the same journalist. Claims 11 and 12 here are
  substantially the same underlying quotes as that note's Claims 7-8. This
  note deliberately extracts them again (rather than omitting them) because
  this article provides materially more surrounding context and because the
  "loopmaxxing" term is genuinely new vocabulary not present in the
  dispatch's extracted text — but the Assayer and Smith should treat Claims
  11-12 here as the same underlying evidence as dispatch Claims 7-8, not as
  independent corroboration from a second source.
- Cross-references verified: `blog-latentspace-aiewf-autoresearch-agency-
  dispatch.md`, `blog-latentspace-meurer-agent-engineer-fde.md`,
  `blog-addyosmani-loop-engineering.md`, `blog-anthropic-claude-code-skills-
  lessons.md`, and `blog-latentspace-aiewf-loops-software-factories-
  dispatch.md` were each re-read in full before citing; no claim numbers
  were guessed.
- No contradiction issue filed — see Cross-References → Contradicts above.
