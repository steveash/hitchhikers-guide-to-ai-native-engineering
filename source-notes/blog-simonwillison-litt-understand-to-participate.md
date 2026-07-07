---
source_url: https://simonwillison.net/2026/Jul/2/understand-to-participate/
source_type: blog-post
title: "Understand to participate"
author: Geoffrey Litt (quoted by Simon Willison)
date_published: 2026-07-02
date_extracted: 2026-07-07
last_checked: 2026-07-07
status: current
confidence_overall: anecdotal
issue: "#1603"
---

# Understand to participate

> Willison relays Geoffrey Litt's framing from his AIE 2026 talk: as coding
> agents construct increasingly large and sophisticated changes, a developer
> needs to understand the code to a depth that enables active participation
> in directing it — not just observation — or their ability to move the
> work forward is "meaningfully limited." Litt names the risk of falling
> short of that depth as taking on cognitive debt.

## Source Context

- **Type**: blog-post (a short "note" — Willison's lighter-weight post format
  for a single observation, as opposed to his longer essays)
- **Author credibility**: The post is Simon Willison relaying a framing from
  Geoffrey Litt, whom he saw speak live at AIE (AI Engineer) 2026. Willison
  is an established, high-signal commentator on LLM tooling and is already a
  trusted feed in this corpus. Geoffrey Litt is credited elsewhere as a
  recognized agent-collaboration researcher/practitioner (he also builds at
  Notion per his account bio) and was speaking at a major industry
  conference — but the claim itself is relayed second-hand by Willison, not
  a direct quote Willison sourced against a transcript; treat the exact
  wording of the blockquote as Willison's best-effort capture of what Litt
  said, not a verified verbatim transcript.
- **Scope**: The post is very short — three short paragraphs plus a two-
  sentence blockquote. It introduces a single framing ("understand to
  participate") and its stakes (cognitive debt, limited participation), and
  points to two follow-up sources: Litt's recorded AIE talk (not yet
  published on YouTube at time of writing — "should be trickling out over
  the next three weeks") and a Twitter/X thread version of the talk. It does
  NOT provide implementation mechanics, a case study, data, or a definition
  of how much understanding is "enough" — it is a framing/thesis statement,
  not a how-to.

## Extracted Claims

### Claim 1: Collaborating with coding agents as they construct increasingly large and sophisticated changes creates a specific risk: a developer's understanding of the code can drift from how it actually works
- **Evidence**: Willison's framing of the problem Litt was addressing in his talk.
- **Confidence**: emerging
- **Quote**: "Geoffrey was talking about the challenge of collaborating with coding agents as they construct increasingly large and sophisticated changes, and the need to avoid taking on cognitive debt as your understanding drifts from how the code actually works."
- **Our assessment**: This names the mechanism (agent-authored change size/sophistication growing faster than the human's tracking of it) rather than just labeling the outcome "cognitive debt." It's consistent with — and adds a growth-rate framing to — the corpus's existing cognitive/comprehension-debt claims (see Cross-References).

### Claim 2: The depth of understanding required is not just enough to follow along, but enough to actively participate in directing the work
- **Evidence**: Willison's direct statement of Litt's argument, immediately preceding the blockquote.
- **Confidence**: emerging
- **Quote**: "His argument is that you need to understand the code to a depth that enables you to participate further with the model"
- **Our assessment**: This is the load-bearing distinction of the post: it separates a lower bar ("I can review/follow this diff") from a higher one ("I can direct where this goes next"). Most existing corpus material on comprehension/cognitive debt discusses risk to reviewability or correctness; this frames the risk instead as loss of the human's creative/directive agency in the collaboration.

### Claim 3: A developer needs a rich set of concepts in mind to think creatively and fluently about how to move a project forward, and lacking that fluency meaningfully limits their ability to participate
- **Evidence**: Direct quote attributed to Geoffrey Litt (relayed by Willison, presented as blockquote).
- **Confidence**: emerging
- **Quote**: "You need a rich set of concepts in your mind to think creatively and fluently about how to move something forward. If you're lacking that fluency, your ability to participate in the project is meaningfully limited."
- **Our assessment**: This is the post's single most citable line. It reframes "understanding the code" as a precondition for creative fluency rather than an end in itself — the claim is that insufficient conceptual grounding doesn't just risk bugs slipping through, it actively degrades the human's capacity to contribute ideas and direction. This is a narrower, more specific mechanism than general "cognitive debt" framings elsewhere in the corpus.

### Claim 4: The same quote frames active participation in the agent's process as something the human can learn to do, not something inherently foreclosed by using an agent
- **Evidence**: The first sentence of the blockquote, which precedes and sets up Claim 3.
- **Confidence**: emerging
- **Quote**: "You can learn what the agent is doing to make sure you can be an active participant in the creative process. [...]"
- **Our assessment**: This positions "active participant" as an achievable, learnable state rather than a fixed trait — implying the practice being recommended is deliberately tracking/learning what the agent is doing as work progresses, rather than reviewing only the final diff. The post does not elaborate on *how* to do this (no concrete practice is given), which limits its actionability compared to, e.g., Udell's "read the code as it's written" practice (see Cross-References).

### Claim 5: Litt's own framing of the same idea, published independently as a Twitter/X thread, opens with a "hot take" framing — implying the position that understanding agent-written code still matters is a contrarian one worth arguing for, not a settled consensus
- **Evidence**: The first tweet of the thread Willison links to, fetched directly (full thread not accessible — see Extraction Notes).
- **Confidence**: anecdotal
- **Quote**: "Hot take: I think it's still important to understand the code that our agents write!"
- **Our assessment**: The "hot take" framing is notable independent evidence about the state of practitioner opinion: Litt himself signals he expects pushback or at least surprise at the claim that understanding agent-written code still matters, suggesting a competing/prevailing view in his audience that it's fine to stop understanding code an agent writes. This is a useful data point for the guide when motivating *why* this chapter's advice needs saying at all — it's not obviously true to the intended audience.

### Claim 6: Willison, an experienced LLM-tooling practitioner and prolific agent user in his own right, found this specific framing distinctly resonant among everything he heard at the conference
- **Evidence**: Willison's own editorial framing at the top of the post.
- **Confidence**: anecdotal
- **Quote**: "I saw Geoffrey Litt speak at AIE yesterday, and one framing he used particularly resonated with me:"
- **Our assessment**: This is a single practitioner's endorsement, not independent evidence for the underlying claim — but Willison's own corpus footprint (dozens of notes in this repo) shows him building and shipping heavily agent-assisted projects, so his stated resonance with a "you must still understand the code" framing is a meaningful signal from someone who is not simply skeptical of agents in general.

## Concrete Artifacts

```
Source: https://simonwillison.net/2026/Jul/2/understand-to-participate/
Full post text (verbatim, minus HTML markup):

I saw Geoffrey Litt speak at AIE yesterday, and one framing he used
particularly resonated with me:

Understand to participate

Geoffrey was talking about the challenge of collaborating with coding
agents as they construct increasingly large and sophisticated changes,
and the need to avoid taking on cognitive debt as your understanding
drifts from how the code actually works.

His argument is that you need to understand the code to a depth that
enables you to participate further with the model:

  You can learn what the agent is doing to make sure you can be an
  active participant in the creative process. [...]

  You need a rich set of concepts in your mind to think creatively and
  fluently about how to move something forward. If you're lacking that
  fluency, your ability to participate in the project is meaningfully
  limited.

The AIE talks are all recorded - all 300+ of them! - and should be
trickling out over the next three weeks. Geoffrey's is one that I
recommend catching on YouTube.

Geoffrey also published a thread version of his talk on Twitter.

Tags: ai, generative-ai, llms, geoffrey-litt, coding-agents, cognitive-debt
```

```
Source: https://twitter.com/geoffreylitt/status/2072522251300409556
(first tweet of thread only — full thread behind X's login wall, see
Extraction Notes)

Hot take: I think it's still important to understand the code that our
agents write!

In this mega thread (based on my AIE talk today), I will explain why
that's the case, and show some ideas for how to efficiently understand
code. Alright, let's dive in. 1/
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-udell-human-agent-loop.md` (Claims 2-3): Udell's
    "fully engaged" claim while building Bram, and his Claim 3 (reading and
    understanding Rust he never wrote, "as they write it" rather than after
    the fact) is a concrete practitioner instance of exactly the depth of
    engagement Litt's framing argues is necessary — Udell demonstrates the
    "active participant" state Litt's Claim 2-4 describes in the abstract.
  - `blog-addyosmani-intent-debt.md` and `blog-fowler-fragments-2026-06-02.md`
    (Pavel Voronin's "generative debt"): both describe cognitive/comprehension
    decay as agent-generated volume grows, matching this post's Claim 1
    mechanism (understanding drifting from actual code as agent changes grow
    larger/more sophisticated).
- **Contradicts**: None identified.
- **Extends**:
  - `blog-simonwillison-udell-human-agent-loop.md`: Udell's post supplies a
    concrete *mechanism* (small testable chunks, shared worklist/repo
    context, reading code as it's written) for staying engaged; this post
    supplies the *cognitive prerequisite* Udell's mechanism is presumably
    meant to sustain — understanding deep enough to direct, not just review.
    Neither post cites the other; they were independently triaged as
    related by the Prospector.
  - `blog-addyosmani-intent-debt.md` (Claim 9, "software's scarce resource
    shifted... to intent, the one input that must still originate with a
    human"): this post narrows that general claim to a specific mechanism —
    a human can't originate intent/direction for work they no longer have
    the conceptual fluency to reason about, which is what happens when
    understanding drifts (Claim 1) below the threshold Claim 3 describes.
- **Novel**:
  - The "understand to participate" framing itself, and the specific
    argument that insufficient understanding degrades creative/directive
    *fluency* (not just review accuracy), is new to the corpus — no existing
    note frames the risk this way.
  - The "hot take" framing from Litt's own Twitter thread (Claim 5) — that
    even asserting "you should still understand agent-written code" is
    perceived as a contrarian position worth arguing for — is a new data
    point about practitioner sentiment not previously captured in the corpus.

## Guide Impact

- **Chapter 03 (Verification)**: Add Claim 2/Claim 3 as the cognitive
  precondition for the chapter's existing verification practices — reviewing
  or spot-checking agent output requires the reviewer to already have (or be
  actively building) the "rich set of concepts" Litt describes; a verifier
  who has let their understanding drift cannot meaningfully verify, only
  rubber-stamp. Cite this source directly alongside the existing cognitive/
  comprehension-debt material.
- **Chapter 05 (Team Adoption / Cognitive Load)**: Use Claim 1 and Claim 5
  together to motivate why this needs to be said explicitly to teams: the
  risk (understanding drift) grows with agent capability/change size, and
  practitioner sentiment (Litt's own "hot take" framing) suggests teams may
  not currently treat "stay fluent enough to direct the work" as an
  established norm. Pair with `blog-simonwillison-udell-human-agent-loop.md`
  for a concrete practice (small testable chunks, real-time reading of
  agent-authored code) that operationalizes the "understand to participate"
  goal this source only states abstractly.
- **Chapter 01 (Daily Workflows)**: Note as a caution alongside any workflow
  guidance that encourages reviewing only final diffs or batching large
  agent-authored changes — this source's Claim 1 argues that exactly this
  pattern (large, infrequent review of increasingly sophisticated changes)
  is what allows understanding to drift below the participation threshold.

## Extraction Notes

- Fetched the primary source twice: once via WebFetch (which returned a
  paraphrased summary, not verbatim text) and once via direct `curl` against
  the raw HTML, parsing the actual `<div class="note">` content by hand. All
  quotes above are checked against the raw HTML extraction, not the WebFetch
  summary — this matters because the post is short enough that a paraphrase
  could easily read as more comprehensive than it is.
- Followed the linked Twitter/X thread
  (https://twitter.com/geoffreylitt/status/2072522251300409556). X requires
  login to render replies/subsequent tweets in the thread; both a direct
  page fetch and the `syndication.twimg.com` embed API returned only the
  first tweet of the thread. Claim 5 is therefore sourced from that first
  tweet only — the remainder of the "mega thread" (which per its own text
  promises an explanation and "ideas for how to efficiently understand
  code") was not accessible and is not represented in this note. This is a
  real gap: the thread likely contains Litt's concrete practices, which
  would be the most guide-actionable material referenced by this source.
  A future miner pass should retry this thread if X access becomes
  available, or look for the AIE 2026 YouTube recording once published
  (the source post states talks would "trickle out over the next three
  weeks" from 2026-07-02).
- Did not follow the AIE conference homepage link
  (https://www.ai.engineer/worldsfair/2026) — it is a conference marketing
  page, not a substantive source for this talk's content.
- The source itself is unusually short (a "note," not an essay) — this
  limited the claim count achievable from the primary source alone; claims
  5-6 draw on the linked Twitter thread and the primary post's own framing
  respectively to reach a defensible claim count without padding or
  inventing claims not supported by the text.
- No contradiction with existing corpus notes was identified.
