---
source_url: https://simonwillison.net/2026/Aug/1/greg-brockman/
source_type: blog-post
title: "Quoting Greg Brockman"
author: Greg Brockman (quoted by Simon Willison)
date_published: 2026-08-01
date_extracted: 2026-08-08
last_checked: 2026-08-08
status: current
confidence_overall: anecdotal
issue: "#2562"
---

# Quoting Greg Brockman

> Greg Brockman (OpenAI President and Co-Founder) reports an internal OpenAI
> observation: employees who wire their ChatGPT up to Slack find that
> coworkers resent being contacted by someone else's AI agent on their
> behalf — even when they would have happily done the same work if asked
> directly by the human coworker — and reads this as evidence that people
> want AI to free up time for human relationships, not insert itself as a
> layer between people.

## Source Context

- **Type**: blog-post (Simon Willison's "Quoting" link-blog format — a
  single-paragraph excerpt with attribution and no added Willison
  commentary, published 2026-08-01). The quote originates from a post by
  Greg Brockman at https://twitter.com/gdb/status/2083435180392673714,
  which Willison links as the source. The original X/Twitter post could not
  be fetched directly (WebFetch returned an HTTP 402 on x.com), so this note
  relies on Willison's reproduction, which was confirmed verbatim across two
  independent WebFetch calls to the Willison page (see Extraction Notes).
- **Author credibility**: Greg Brockman is President and Co-Founder of
  OpenAI — a first-party, senior-leadership source describing an internal
  practice and behavioral observation at his own company. This is not
  vendor marketing copy; it is a spontaneous social-media observation about
  an internal friction point, which if anything cuts against OpenAI's
  commercial interest in frictionless agent-to-human contact. Simon
  Willison is a widely-read, independent AI-tooling commentator; his
  selection of this passage as a standalone quotation post is a relevance
  signal already established elsewhere in this corpus.
- **Scope**: Covers a single, brief, first-person anecdotal observation
  about employee behavior at OpenAI when ChatGPT agents are connected to
  Slack and act on a coworker's behalf. Does NOT cover: how widespread the
  "ChatGPT hooked up to Slack" practice is at OpenAI (no count or
  percentage given), what specific tasks these agents perform, whether this
  observation has been measured rather than anecdotally noticed by
  Brockman, or any prescription for how to design around the friction
  beyond the one-sentence framing quoted below. There is no linked essay or
  thread to follow — the quote is the entire source (see Extraction Notes).

## Extracted Claims

### Claim 1: At OpenAI, many employees connect their ChatGPT to Slack so it can act as an agent on their behalf
- **Evidence**: Brockman's own first-person statement about a practice at
  his company.
- **Confidence**: anecdotal (unquantified — "many people," no count, no
  measurement methodology; a senior leader's own characterization of an
  internal practice)
- **Quote**: "at openai, many people hook their chatgpt up to slack."
- **Our assessment**: This establishes the mechanism the rest of the quote
  depends on: the friction described in Claim 2 only arises because
  ChatGPT is acting as a Slack-integrated agent that can initiate contact
  with a coworker, not merely as a private chat tool the employee uses
  themselves. It is a lightweight but concrete data point that agent-to-
  Slack integration was, as of August 2026, common enough at OpenAI for
  Brockman to describe it as widespread ("many people") without further
  qualification.

### Claim 2: Coworkers dislike being contacted by a colleague's ChatGPT agent asking for help, even when they would be happy to do the identical work if the human colleague asked them directly
- **Evidence**: Brockman's direct observation, framed as a contrast between
  two conditions that differ only in *who* (or what) initiates the
  request — the same task, requested by an AI agent acting on a coworker's
  behalf versus requested by the coworker in person.
- **Confidence**: anecdotal (single leader's unquantified observation; no
  survey data, no measured refusal/friction rate, no description of how the
  observation was gathered)
- **Quote**: "people really don't like when a coworker's chatgpt contacts them asking for help with a task, even when they'd be perfectly happy doing that same work if asked by that coworker."
- **Our assessment**: This is the core empirical claim and the reason the
  source was triaged as high-novelty. The controlled contrast Brockman
  draws — same task, same requester-relationship, only the delivery
  mechanism (human vs. that human's AI proxy) differs — isolates the
  variable cleanly, at least rhetorically. It is worth being precise about
  what this claim does and doesn't establish: it is Brockman's
  characterization of a pattern he's observed, not a measured comparison
  with a control group or a cited internal study. The guide should treat it
  as a plausible, well-articulated anecdote from a highly-positioned
  observer (OpenAI's own Slack culture), not as settled research.

### Claim 3: Brockman interprets the resentment toward AI-mediated requests as evidence that people place high value on human relationships and on helping each other directly
- **Evidence**: Brockman's own stated interpretation, offered immediately
  after describing the observed friction in Claim 2.
- **Confidence**: anecdotal (an interpretive gloss on an already-anecdotal
  observation, not independently tested)
- **Quote**: "reinforces how much people care about human relationships and helping each other"
- **Our assessment**: This is an inference, not a new data point — Brockman
  is naming *why* he thinks people react the way Claim 2 describes. It is a
  plausible read (a request routed through a bot removes the social
  transaction of being asked and thanked by a person) but it's one
  interpretation among several a reader might draw from the same
  observation (e.g., it could equally be read as distrust of whether the
  bot accurately represents the coworker's actual need, rather than a pure
  preference for human connection). The guide should attribute this
  reading to Brockman explicitly rather than presenting it as an
  established finding.

### Claim 4: Brockman states a normative design goal for AI — it should give people time back or enhance time spent together, rather than become a layer that separates people from each other
- **Evidence**: Brockman's own closing statement, presented as the
  conclusion drawn from Claims 1-3.
- **Confidence**: anecdotal (a stated design preference/value judgment from
  an OpenAI leader, not a tested design principle or product commitment)
- **Quote**: "want AI to give time back — or enhance time together — rather than become a layer separating people."
- **Our assessment**: This is the most guide-relevant sentence in the
  source: a named, if brief, design principle — "AI should not mediate
  human-to-human requests it wasn't asked to mediate." For agent-design
  purposes, the actionable distinction is between an agent that acts
  *for* a human toward a shared goal the human directed (e.g., drafting a
  message the human then sends themselves) versus an agent that acts *as*
  the human, initiating contact with a third party autonomously. Brockman's
  quote describes the second pattern as the one that generates friction,
  but does not by itself provide a design rule for where the line falls —
  it names the value ("don't become a layer separating people") without
  specifying the mechanism.

<!-- Only 4 claims: the source is a single un-elaborated paragraph with no
     linked essay or thread to extend it (see Extraction Notes). Each claim
     above anchors to a distinct, non-overlapping clause of that paragraph
     rather than restating the same sentence four ways. -->

## Concrete Artifacts

No code, config, transcripts, or metrics are present in this source — it is
a single prose paragraph with no embedded artifacts.

```
Full quote (simonwillison.net/2026/Aug/1/greg-brockman/, 2026-08-01):

"at openai, many people hook their chatgpt up to slack. people really
don't like when a coworker's chatgpt contacts them asking for help with a
task, even when they'd be perfectly happy doing that same work if asked
by that coworker. reinforces how much people care about human
relationships and helping each other, and want AI to give time back — or
enhance time together — rather than become a layer separating people."

Attribution: Greg Brockman, President and Co-Founder, OpenAI
Original source linked by Willison: https://twitter.com/gdb/status/2083435180392673714
Tags on the Willison post: ai, openai, generative-ai, llms, ai-ethics, ai-misuse
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-udell-human-agent-loop.md` Claim 9 ("I dislike the
    phrase 'human in the loop' because it cedes authority to the machines.
    Let's flip the narrative. It's our loop, we work the same way we always
    have, now we recruit agents to join the team. An agent-assisted process
    need not be a black box that takes in prompts and emits features.") and
    Claim 11 ("Let's do agentic software development like that. Not as a
    loop we've been excluded from, instead as one we invite agents into.").
    Both sources converge on the same underlying value — human agency and
    human relationships should remain the organizing center, with AI
    joining an existing human process rather than substituting for or
    routing around direct human-to-human interaction. Udell's claims are
    about a single practitioner's authorship/authority framing for
    human-agent collaboration on a coding project; Brockman's claim is
    about a specific, narrower social friction point (an agent contacting
    a *third person* on a user's behalf) inside a large organization. The
    two are independently-arrived-at articulations of a related principle
    from very different vantage points (a solo tool-builder vs. an OpenAI
    executive observing company-wide Slack behavior), which strengthens
    the case for treating "keep AI from displacing direct human contact"
    as a recurring value in the corpus rather than a one-off opinion.

- **Contradicts**: None identified. No existing corpus note argues that
  people prefer or are indifferent to being contacted by a colleague's AI
  agent rather than the colleague directly. No contradiction issue
  required.

- **Extends**: None identified with sufficient specificity to cite by
  claim number. `blog-simonwillison-datasette-agent-askuser.md` (the
  Prospector's suggested overlap, documenting the `ask_user()` mid-execution
  prompting pattern) was reviewed directly for this note but is not a close
  enough match to cite as an extension: `ask_user()` is a mechanism for an
  agent to ask questions of *its own user* mid-task, not for one person's
  agent to initiate contact with a *different* person on that user's
  behalf. The friction Brockman describes is specifically about
  third-party mediation (agent-to-coworker), which `ask_user()`'s
  first-party mechanism (agent-to-its-own-operator) does not address one
  way or the other. Flagging this explicitly since the Prospector's triage
  comment proposed the connection and a future Smith pass may want to
  revisit whether a genuine extension relationship exists once more sources
  on agent-initiated third-party contact are mined.

- **Novel**:
  - **First corpus documentation of resentment toward AI-mediated
    coworker-to-coworker requests, specifically**: no existing source note
    documents the finding that people react negatively to an AI agent
    contacting them on a *coworker's* behalf, as distinct from general
    skepticism about AI agent output quality or trustworthiness. This is a
    social/interpersonal friction claim, not a capability or safety claim.
  - **"Layer separating people" as a named anti-pattern for agent design**:
    no existing corpus source names this specific framing — AI risking
    becoming an intermediation layer between people who would otherwise
    interact directly — as a thing to avoid. This is a values-level framing
    that could inform how the guide discusses agent-to-human (as opposed
    to agent-to-task) design choices.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Add Claim 2 and Claim 4 as a named
  organizational-friction pattern for teams building or deploying
  Slack-integrated (or similarly network-facing) agents that can initiate
  contact with other employees on a user's behalf: employees may resist
  a request routed through a colleague's AI agent even when they would
  accept the identical request from the colleague directly. Recommend the
  guide draw the design distinction implicit in Claim 4 explicitly: agents
  that act *for* a user toward a goal the user directs (e.g., drafting
  a message for the user to send) are different in kind from agents that
  act *as* the user, autonomously initiating contact with a third
  colleague — the friction Brockman describes is specific to the latter.
  Flag as anecdotal, single-company, unquantified evidence (Confidence:
  anecdotal throughout) rather than a measured finding.

- **Chapter 00 (Principles)**: Consider Claim 4's framing ("AI should give
  time back or enhance time together, rather than become a layer
  separating people") as a candidate principle-level statement about
  agent-to-human design, to be paired with
  `blog-simonwillison-udell-human-agent-loop.md` Claim 9's "our loop, agents
  invited in" framing (see Cross-References — Corroborates). Both sources
  argue, from different contexts, that agent design should preserve rather
  than substitute for direct human involvement in a process; the guide
  could state this as a shared principle citing both sources together
  rather than treating either as a standalone anecdote.

## Extraction Notes

- **Thin, single-paragraph source with no linked essay to follow**: unlike
  several other "Quoting" posts in this corpus (e.g.,
  `blog-simonwillison-udell-human-agent-loop.md`,
  `blog-simonwillison-kyle-kingsbury.md`), the link Willison provides for
  this quote goes directly to the original X/Twitter post
  (https://twitter.com/gdb/status/2083435180392673714), not to a longer
  essay or blog post with additional context. Per MINER.md §1's
  instruction to follow substantive linked pages, this link was attempted:
  WebFetch on the twitter.com URL returned a same-host redirect to
  x.com, and the subsequent x.com fetch returned an HTTP 402 Payment
  Required error. No archived or alternate copy of the original post was
  located. The quote as reproduced on Willison's page is therefore the
  entirety of the extractable source text; this note's 4 claims each
  anchor to a distinct clause of that one paragraph rather than restating
  it, and no 5th–15th claim was manufactured to hit the "5-15 claims"
  guidance in MINER.md §2 — the source genuinely does not contain more
  than four non-redundant claims.
  - As a general convention for future short-quote Miner notes: 3-4 claims is
    the right target for a single-paragraph, no-linked-essay "Quoting"
    source, since MINER §2's 5-15 claim guidance assumes there is enough
    distinct source material to support it.
- **Verbatim quote confirmed via two independent WebFetch calls**: the full
  paragraph quote was returned identically (down to lowercase sentence-initial
  letters, em-dash usage, and punctuation) across two separate WebFetch
  requests to https://simonwillison.net/2026/Aug/1/greg-brockman/ made
  moments apart, one asking for the raw page content and one asking
  specifically for the exact blockquote text character-for-character. Both
  returned the identical string used throughout this note's Quote fields.
  This matches the verification pattern used in
  `blog-simonwillison-kyle-kingsbury.md` ("confirmed via two separate
  fetches").
- **Fragment URL**: the issue body's Source URL includes `#atom-everything`.
  The `source_url` field above uses the canonical URL without the
  fragment, consistent with prior Willison source notes in this corpus
  (e.g., `blog-simonwillison-datasette-agent-askuser.md`'s Extraction Notes
  on the same convention).
- **Cross-references verified**: `blog-simonwillison-udell-human-agent-loop.md`
  Claims 9 and 11 were re-read in full in that note before citing them
  here; the quoted text above is copied verbatim from that note rather than
  reconstructed from memory. `blog-simonwillison-datasette-agent-askuser.md`
  was re-read in full to evaluate the Prospector's suggested overlap; the
  assessment above (not a close enough match to cite as Extends) reflects
  that direct re-reading, not the Prospector's characterization alone.
- **No contradiction filed**: no existing corpus note makes a claim in
  tension with the observation that people resent AI-mediated third-party
  contact; see Cross-References — Contradicts.
