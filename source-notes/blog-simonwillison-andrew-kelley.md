---
source_url: https://simonwillison.net/2026/Apr/30/andrew-kelley/
source_type: blog-post
title: "A quote from Andrew Kelley"
author: Simon Willison (quoting Andrew Kelley, Creator of Zig)
date_published: 2026-04-30
date_extracted: 2026-05-09
last_checked: 2026-05-09
status: current
confidence_overall: anecdotal
issue: "#571"
---

# A Quote from Andrew Kelley: "Digital Smell" and LLM Detection in Code Review

> Andrew Kelley (Zig creator) asserts that experienced maintainers can
> detect LLM-assisted contributions through qualitatively different error
> patterns, and that agentic coding practitioners emit a "digital smell"
> perceptible to non-users but invisible to the practitioners themselves.

## Source Context

- **Type**: blog-post (Simon Willison "quotation" format — a single collected quote
  from a Lobsters comment, no independent analysis by Willison; the full thread is
  at https://lobste.rs/s/ifcyr1/contributor_poker_zig_s_ai_ban#c_cbtxub, a discussion
  of Loris Cro's "Contributor Poker and Zig's AI Ban" essay).
- **Author credibility**: Andrew Kelley is the creator of the Zig programming language
  and the primary maintainer of the Zig project. He is writing from direct first-person
  experience reviewing pull requests to a major, actively maintained programming language
  project. He is not making a general empirical claim — he is reporting what he and his
  team have observed. His authority is high for this specific context (Zig PR review)
  and appropriately narrower as a generalization.
- **Scope**: One Lobsters comment, collected by Simon Willison without additional
  commentary. The full quote covers: (1) a direct rebuttal of the "you can't tell"
  misconception, (2) the claim that LLM error types differ qualitatively from human
  error types, (3) the "digital smell" metaphor for perceivable agentic coding signatures,
  (4) the asymmetric perceptibility of that smell, and (5) a policy statement about
  Zig contributions. Does NOT cover: what specific patterns constitute the "smell,"
  detection methodology, false positive rate, or how these observations apply to
  projects with different review processes.

## Extracted Claims

### Claim 1: The belief that maintainers cannot distinguish LLM-assisted PRs from human PRs is a common misconception

- **Evidence**: Andrew Kelley's direct first-person rebuttal from experience reviewing
  Zig contributions over "the past few months" — the period after Zig's AI contribution
  ban was formalized. Kelley's framing ("It's a common misconception") implies this
  belief was specifically asserted to him or the Zig team.
- **Confidence**: anecdotal (one project's experience; no methodology, no count, no
  cross-project validation)
- **Quote**: "It's a common misconception that we can't tell who is using LLM and who is not."
- **Our assessment**: This is a credible rebuttal from someone with the specific context
  to make it (active maintainer enforcing an AI ban). The hedge embedded in the same
  comment — "I'm sure we didn't catch 100% of LLM-assisted PRs" — is important: Kelley
  is claiming detectable signal, not perfect detection. The claim invites the follow-up
  question "which patterns trigger detection?" but Kelley does not answer it here. The
  value for the guide is the claim that the perception is possible, not the method.

### Claim 2: LLM hallucinations produce a qualitatively different error signature than human mistakes, enabling experienced maintainers to identify them

- **Evidence**: Kelley's direct observational claim from reviewing Zig contributions.
  Stated as a mechanism explaining *how* detection works ("making them easy to spot").
- **Confidence**: anecdotal (single maintainer's qualitative judgment; no specific error
  patterns enumerated; no count of reviewed PRs or detection rate)
- **Quote**: "the kind of mistakes humans make are fundamentally different than LLM hallucinations, making them easy to spot"
- **Our assessment**: The word "fundamentally" is load-bearing — Kelley is claiming a
  difference in kind, not just degree. This is plausible: LLM hallucinations tend toward
  confident invocations of nonexistent APIs, argument transpositions in standard-library
  calls, or plausible-looking but semantically wrong logic synthesis. Human mistakes tend
  toward off-by-one errors, missed edge cases, and logic errors that follow the developer's
  existing mental model. But Kelley does not enumerate these — this is an assertion, not
  a taxonomy. The `discussion-hn-autofix-hybrid-review.md` source (Claim 1) documents a
  four-mode failure taxonomy for LLM code review tools (non-determinism, low recall,
  cost, distraction) — that is about automated detection; Kelley is describing human
  perception of code authorship, which is a different phenomenon but may share a root cause.

### Claim 3: Practitioners immersed in agentic coding emit a "digital smell" that is perceptible to those who abstain from AI tools

- **Evidence**: Kelley's metaphorical framing of his observation; the smoking/smell analogy
  is used to convey both the immediacy and the qualitative character of the perception.
- **Confidence**: anecdotal (evocative metaphor; no specific behaviors or code patterns
  constituting the "smell" are enumerated; the observation is from a single project)
- **Quote**: "people who come from the world of agentic coding have a certain _digital smell_ that is not obvious to them but is obvious to those who abstain. It's like when a smoker walks into the room, everybody who doesn't smoke instantly knows it."
- **Our assessment**: The "digital smell" metaphor is memorable but deliberately non-specific.
  The Lobsters thread context (126 comments) surfaces some candidate components: perfect
  surface style with semantic errors; unusually large first-time PRs; over-engineered
  solutions to narrow problems; PR descriptions that are verbose and well-formatted but miss
  the actual design question. Kelley does not cite these specifically — the claim is that
  the gestalt is detectable, not that any specific signal is diagnostic. For the guide, this
  is useful as a named concept even without a definitive pattern list: it licenses teams to
  acknowledge that AI-assisted code is perceptible to reviewers, not invisible.

### Claim 4: The "digital smell" of agentic coding is asymmetrically perceptible — practitioners cannot perceive it in their own work, but non-practitioners can

- **Evidence**: Embedded within the same quote as Claim 3; the asymmetry is explicit in
  the "not obvious to them but is obvious to those who abstain" clause.
- **Confidence**: anecdotal (asserted without methodology; the smoker analogy implies
  olfactory adaptation, but this is metaphorical)
- **Quote**: "not obvious to them but is obvious to those who abstain" (contained within the Claim 3 quote; see the full passage above)
- **Our assessment**: This is the most consequential sub-claim for the guide. If agentic
  coding practitioners genuinely have a perceptual blind spot about their own work's
  detectability, then teams making AI-adoption decisions are operating on an incorrect
  self-model. Engineers who believe "no one can tell" when reviewers believe "I can
  always tell" are making different assumptions about the social stakes of AI adoption.
  This asymmetry also implies that the "digital smell" cannot be self-corrected by
  practitioners — they need external feedback to know whether and how their AI-assisted
  work is perceived. No existing source in our corpus addresses this asymmetric
  perceptibility directly.

### Claim 5: Kelley's position is permissive about LLM use in general but draws a hard contextual boundary at contributions to his project

- **Evidence**: Kelley's direct statement closing the quote; the smoking/house metaphor
  makes the policy structure explicit.
- **Confidence**: settled (direct policy statement with no ambiguity)
- **Quote**: "I'm not telling you not to smoke, but I am telling you not to smoke in my house."
- **Our assessment**: This is not a moral condemnation of AI tool use — it is a contextual
  boundary. Kelley's objection is specific to the shared space he controls (Zig contributions),
  not to LLM use in general. The framing matters for the guide: practitioners working on
  OSS projects, contributing to shared codebases, or submitting work for external review
  need to understand that project maintainers can and do set AI-contribution policies, and
  that these policies operate independently of the practitioner's own judgment about LLM use.
  This is consistent with Zig's explicit code-of-conduct ban (corroborated in
  `blog-simonwillison-zig-anti-ai.md`, Claim 1 — pending review in PR #579, issue #569).

## Concrete Artifacts

### Full verbatim quote from Andrew Kelley (Creator of Zig)

```
Source: https://lobste.rs/s/ifcyr1/contributor_poker_zig_s_ai_ban#c_cbtxub
Collected by Simon Willison: https://simonwillison.net/2026/Apr/30/andrew-kelley/
Posted: 30th April 2026

"It's a common misconception that we can't tell who is using LLM and who is
not. I'm sure we didn't catch 100% of LLM-assisted PRs over the past few
months, but the kind of mistakes humans make are fundamentally different than
LLM hallucinations, making them easy to spot. Furthermore, people who come
from the world of agentic coding have a certain _digital smell_ that is not
obvious to them but is obvious to those who abstain. It's like when a smoker
walks into the room, everybody who doesn't smoke instantly knows it.

I'm not telling you not to smoke, but I am telling you not to smoke in my house."

— Andrew Kelley, Creator of Zig
```

## Cross-References

- **Corroborates**: `blog-simonwillison-zig-anti-ai.md` (pending review in PR #579,
  issue #569) — Claim 1 of that note establishes Zig's explicit code-of-conduct ban
  on LLM contributions; Claims 1–5 here provide the *detection rationale* that makes
  enforcement credible. The ban is not purely philosophical or unenforceable — Kelley
  asserts detectable signal exists. Claim 4 of that note documents the low quality of
  observed AI contributions; this note adds the *mechanism* by which qualitative
  differences are perceived (error type, not just error rate).

- **Extends**: `discussion-hn-autofix-hybrid-review.md` — That note (Claim 1) documents
  a four-mode failure taxonomy for LLM-only automated code review (non-determinism, low
  recall, cost, distraction). This source describes a parallel but distinct phenomenon:
  *human* perceptual detection of AI-authored code, not algorithmic detection. Together
  they establish that LLM contribution signatures are detectable both by automated tools
  and by experienced human reviewers — two complementary detection surfaces with
  different false-positive/negative profiles.

- **Novel**: The following claims are new to our corpus:
  1. The "digital smell" concept as a named phenomenon for the gestalt perceptual
     signature of agentic coding practitioners.
  2. The asymmetric perceptibility claim (Claim 4): practitioners cannot self-perceive
     the signal they emit; only non-practitioners can detect it. No other source in
     the corpus addresses this specific asymmetry.
  3. The distinction between *error type* (qualitative difference in hallucination vs.
     human-mistake character) vs. *error rate* as the detection mechanism.

- **Contradicts**: none identified in current corpus.

## Guide Impact

- **Chapter on Code Review / Safety**: Kelley's Claim 2 (error type as detection signal)
  motivates a guide recommendation: when reviewing AI-assisted code contributions from
  external collaborators or team members, reviewers should be aware that LLM-style errors
  (confident wrong API invocations, plausible but semantically broken logic) differ from
  human-style errors and may require different review heuristics. The guide currently
  lacks coverage of *how* code reviewers should calibrate for AI-assisted contributions
  — this source opens that gap.

- **Chapter on Team Adoption / OSS Contribution**: Claim 4 (asymmetric perceptibility)
  is directly actionable: AI-native engineers contributing to OSS projects or external
  codebases should not assume their work is imperceptible. The guide should advise that
  transparency about AI tool use — and awareness of how AI-assisted code reads to
  non-users — is part of responsible agentic engineering practice.

- **Chapter on AI Contribution Policy**: Claims 1 and 5 together establish that at
  least some prominent OSS project leaders (1) believe they can enforce an AI-contribution
  ban through perceptual detection and (2) frame the policy as a contextual boundary
  rather than a moral prohibition. Teams setting internal AI-use policies should note
  the Kelley model: permissive about personal use, restrictive about contributions to
  shared artifacts.

## Extraction Notes

1. **Source thinness**: This is a single Lobsters comment (≈100 words), collected
   by Simon Willison without additional commentary. The claims are asserted rather than
   argued. The guide impact is real, but the evidentiary weight is low — treat all
   claims as anecdotal, and flag to the Smith that this source needs corroboration
   before driving guide guidance.

2. **Companion source**: Issue #569 covers the companion source from the same day
   (Simon Willison's summary of Loris Cro's "Contributor Poker and Zig's AI Ban"
   essay). The two sources together form a richer picture: issue #569 covers *why*
   the ban exists (contributor poker, investment philosophy); issue #571 covers *how*
   detection works. Both should be cited together wherever the guide addresses
   AI contribution policy or code review for AI-assisted work.

3. **Lobsters thread context**: The source quote was posted in a Lobsters thread with
   126 comments and 212 upvotes. The thread itself contains more concrete discussion
   of detection patterns (e.g., PR description style, code structure characteristics).
   This Miner extraction covers only the Simon Willison-collected quotation per the
   issue scope; the fuller Lobsters thread is a candidate for a separate source note
   if warranted.

4. **Detection completeness caveat**: Kelley hedges: "I'm sure we didn't catch 100%
   of LLM-assisted PRs." The claim is detectable-signal-exists, not perfect-recall.
   This hedge is important for any guide claim about LLM-contribution detection.
