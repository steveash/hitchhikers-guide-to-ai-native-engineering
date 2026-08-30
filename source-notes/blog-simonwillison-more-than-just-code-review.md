---
source_url: https://simonwillison.net/2026/Aug/22/more-than-just-code-review/
source_type: blog-post
title: "More than just code review"
author: Simon Willison
date_published: 2026-08-22
date_extracted: 2026-08-30
last_checked: 2026-08-30
status: current
confidence_overall: anecdotal
issue: "#3096"
---

# More than just code review

> A two-sentence "note" post arguing that the core skill for productive
> coding-agent use is confident instruction-giving paired with confident
> verification, and that line-by-line review — "eyeballing every line of
> code" — has never been the most effective way to validate a software
> change, agent-authored or otherwise.

## Source Context

- **Type**: blog-post (Willison's "note" format — a short-form post type
  distinct from his long-form linked/annotated posts, confirmed by the
  page's own metabox: "This is a note by Simon Willison").
- **Author credibility**: Simon Willison is an already-heavily-cited corpus
  source (150+ existing `blog-simonwillison-*.md` notes) — a widely-read,
  high-signal commentator on LLM tooling and agentic coding, and the
  original curator/publisher of many datasette/llm ecosystem tools. This
  particular post is a personal opinion/observation, not a report of
  original research, data, or a specific project — it carries his general
  authority as a trusted commentator but no independent evidence of its
  own.
- **Scope**: The entire post is two short paragraphs (three sentences
  total). It states a general principle (instruct confidently, verify
  confidently) and takes a position on one specific point (line-by-line
  review is not the most effective validation method) but does not name,
  describe, or give an example of any alternative verification method. It
  does not distinguish whether this claim is specific to AI-agent-authored
  code or is a general claim about software validation that predates
  agents (the wording suggests the latter — see Claim 2). It does not cite
  data, a project, or a specific incident.

## Extracted Claims

### Claim 1: The key skill for productive use of coding agents is confidently instructing them on changes and then confidently verifying those changes were applied correctly
- **Evidence**: Author's direct, unsupported assertion — stated as a
  general opinion, not tied to a specific project or dataset.
- **Confidence**: anecdotal
- **Quote**: "The key skill required to make productive use of coding
  agents is being able to confidently instruct them on how to make changes
  and then confidently verify that those changes have been applied in the
  correct way."
- **Our assessment**: This names instruction-giving and verification as a
  paired competency, not two separate skills — Willison frames the
  "confidently instruct" half as equally load-bearing as the "confidently
  verify" half, which is a subtly different emphasis from corpus sources
  that treat verification alone as the bottleneck (e.g.,
  `blog-addyosmani-code-agent-orchestra.md` Claim 5: "the bottleneck is no
  longer generation, it's verification"). Willison doesn't say instruction
  quality reduces verification burden explicitly — that connection is our
  inference, not stated in the text — but the pairing implies it. No
  mechanism or example is given for what "confidently verify" looks like
  in practice beyond Claim 2's narrow point about line-by-line review.

### Claim 2: Reviewing every line of code an agent wrote is one way to verify a change, but not the only way, and eyeballing every line has never been the most effective validation method for a software change generally
- **Evidence**: Author's direct, unsupported assertion.
- **Confidence**: anecdotal
- **Quote**: "Sometimes this involves reviewing every line of code they
  have written, but there are other ways to achieve that goal. Eyeballing
  every line of code has never been the most effective way to validate a
  change to a piece of software."
- **Our assessment**: The notable feature of this claim is its scope:
  Willison states it as a general truth about software validation
  ("has never been the most effective way to validate a change to a piece
  of software") rather than an AI-specific claim about agent-generated
  code. This is a different argument shape from
  `blog-addyosmani-agentic-code-review.md`, which argues review changed
  specifically *because of* agent-generated volume and diagnoses a
  mechanism for why (Claim 8 there: agents discard their reasoning once
  the diff is produced, forcing reviewers to reconstruct intent). Willison
  gives no mechanism, no example of an alternative validation method (no
  mention of tests, CI, reviewer agents, decision logs, or anything else),
  and no data. It reads as a pre-existing personal conviction restated in
  the agent-coding context, not a claim built from agent-specific
  evidence. This is the weakest-evidenced claim we have in the corpus on
  this topic — a bare assertion from a credible source, nothing more.

## Concrete Artifacts

None. The post contains no code, configuration, transcript, metric, or
step-by-step procedure — it is two sentences of prose opinion with no
supporting artifact of any kind.

## Cross-References

- **Corroborates**:
  - `blog-addyosmani-agentic-code-review.md` Claim 11 ("Effective review
    posture under agent-generated volume is 'human on the loop' (sampling,
    spot-checking, auditing) rather than 'human in the loop' (reading
    every diff)") — Willison's Claim 2 reaches the same conclusion (don't
    read every line) independently and from a different angle: Osmani
    argues it from volume/bottleneck economics with quantitative backing;
    Willison asserts it as a standing truth about software validation with
    no backing at all. The two sources agree on the recommendation, not on
    why it's true.
  - `blog-addyosmani-code-agent-orchestra.md` Claim 5 ("The bottleneck has
    shifted from code generation to verification") — Willison's Claim 1
    names the same two competencies (instruct, verify) as central to
    productive agent use, though without Osmani's "bottleneck" framing or
    any of the corroborating research Osmani cites (the Anthropic
    comprehension-debt study).
  - `blog-cognition-verifying-agentic-development.md` Claims 1 and 2 —
    this is the corpus's concrete answer to the question Willison's Claim 2
    raises but never answers ("there are other ways to achieve that goal").
    Claim 1 there corroborates Willison's Claim 1 framing from a production
    setting: Cognition reports that "For the first time, more Devins are
    being triggered asynchronously, via events, automations, schedules, and
    other Devins," which makes verified-without-a-human-watching results a
    structural requirement rather than a preference — the same instruct/
    verify pairing Willison names, but driven by a stated mechanism (trigger
    mode) rather than asserted as a general skill. Claim 2 there names one
    of the unnamed "other ways": Devin verifying its own work via
    computer-use tooling — "Devin will spin up the app, click through it,
    and confirm its changes actually work, the same way an engineer would."
    Worth flagging for the Smith: where Willison supplies a bare assertion
    that alternatives to line-by-line review exist, the Cognition note
    supplies a specific, shipped one plus the supporting techniques
    (source-grounded test plans, annotate-before-acting, deterministic setup
    skills). Any guide passage citing this source for "you don't have to
    read every line" should cite the Cognition note for what to do instead;
    this source cannot carry that half on its own.
- **Contradicts**: None filed. There is a directional tension worth noting
  rather than escalating: `blog-simonwillison-udell-human-agent-loop.md`
  Claim 3 documents Jon Udell (a different practitioner, in a different
  Willison-linked post) reporting that he "read[s] the Rust code that
  Claude Code and Codex write for me, as they write it" line-by-line. Per
  MINER.md §4a and consistent with that note's own assessment of the same
  tension against Osmani, this reads as a conditioning-variable difference
  (single-developer real-time engagement on one project vs. a general
  claim about validating software changes) rather than two claims about
  the same situation reaching opposite conclusions, so no contradiction
  issue is filed. Worth flagging for the Smith: this is now the second
  source in the corpus where Willison-published content sits on the "less
  than 100% line review" side of that same tension, without ever engaging
  Udell's counter-example directly (the two posts do not reference each
  other).
- **Extends**: None. This post is too thin (two sentences, no mechanism,
  no example) to extend any existing claim with new detail — it restates
  a conclusion the corpus already has more thoroughly evidenced elsewhere.
- **Novel**: Nothing here is new to the corpus. The recommendation
  (verification doesn't require reading every line) and the paired
  framing (instruct + verify as the core skill) are both already present,
  with substantially more evidence, in `blog-addyosmani-agentic-code-review.md`
  and `blog-addyosmani-code-agent-orchestra.md`. The only genuinely new
  data point this source contributes is that Willison — an independent,
  trusted voice not affiliated with Osmani — holds the same position,
  which has corroboration value but no evidentiary value of its own.

## Guide Impact

- No new guide content is warranted from this source on its own. It is too
  thin (a bare two-sentence assertion, no mechanism, no example, no data)
  to serve as a primary citation for any recommendation.
- **Chapter 05 (Team Adoption / human-agent collaboration)**: If the guide
  already cites `blog-addyosmani-agentic-code-review.md` Claim 11 ("human
  on the loop") for the recommendation that teams shouldn't read every
  agent-generated diff, this source can be added as a secondary,
  independent-voice citation alongside it — useful for signaling that the
  position isn't just one practitioner-synthesizer's framework but is
  shared by a second, differently-positioned commentator. It should not
  replace or be the sole citation for that recommendation, given how
  little evidence it supplies on its own.
- No other chapter changes are recommended. In particular, this source
  does not supply enough to justify adding "instruction-giving is a
  learnable skill" as its own guide section — Claim 1 asserts the pairing
  but gives no guidance on what confident instruction-giving actually
  looks like in practice.

## Extraction Notes

- The post is genuinely this short. This was independently verified three
  ways before concluding the extraction was complete rather than
  incomplete: (1) WebFetch's default summarizing pass, (2) two further
  targeted WebFetch passes asking specifically for a sentence-by-sentence
  breakdown with an exact count, and (3) a direct `curl` fetch of the raw
  page HTML (bypassing WebFetch's summarizing model entirely), which
  shows the full `<div class="note">` content as exactly two `<p>` tags
  totaling three sentences, matching the WebFetch output verbatim. No
  sub-pages, footnotes, or linked articles are referenced from within the
  post body itself (the "Recent articles" list and the Greptile sponsor
  banner are page furniture surrounding the post, not part of it, and were
  excluded from extraction accordingly).
- Both quotes above were checked against the raw HTML fetched via `curl`
  and are copied character-for-character from the `<div class="note">`
  block.
- Given the thinness of the source, this note has 2 extracted claims
  rather than the usual 5-15 — this reflects the source's actual length,
  not a shortfall in reading depth. A third "claim" would have required
  inventing content not present in the source.
- No contradiction issue was filed. The one tension identified (against
  `blog-simonwillison-udell-human-agent-loop.md` Claim 3) was assessed
  against MINER.md §4a's criteria and judged to be a conditioning-variable
  difference, not a material contradiction — see Cross-References above.
- Cross-references verified: `blog-addyosmani-agentic-code-review.md`
  Claim 11 and `blog-addyosmani-code-agent-orchestra.md` Claim 5 were each
  re-read in the cited note before this note was written, and
  `blog-simonwillison-udell-human-agent-loop.md` Claim 3 was likewise
  re-read; all quoted text above from those notes is copied verbatim from
  them rather than reconstructed from memory.
  `blog-cognition-verifying-agentic-development.md` Claims 1 and 2 were
  added on review and verified the same way — both numbered headings were
  located in that note and the two quoted passages copied verbatim from it.
