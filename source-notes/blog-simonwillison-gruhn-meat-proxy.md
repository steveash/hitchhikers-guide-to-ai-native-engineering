---
source_url: https://simonwillison.net/2026/Aug/3/dont-be-a-meat-proxy/
source_type: blog-post
title: "Don't be a meat proxy"
author: Niklas Gruhn (linked and quoted by Simon Willison)
date_published: 2026-08-03
date_extracted: 2026-08-10
last_checked: 2026-08-10
status: current
confidence_overall: anecdotal
issue: "#2603"
---

# Don't be a meat proxy

> Niklas Gruhn names "meat proxy" — a person who mechanically relays AI
> output to others (in Slack, code review, group chats) without reading,
> understanding, or validating it first — and prescribes a four-step
> discipline (read, understand, validate, rewrite in your own words) as the
> concrete, checkable alternative. Simon Willison amplifies the term to his
> own high-signal audience as "an excellent new term."

## Source Context

- **Type**: blog-post. Two linked layers: (1) Simon Willison's short "link
  post" on simonwillison.net (the submitted source URL) — a two-sentence
  introduction plus one verbatim blockquote from Gruhn's article; (2) Niklas
  Gruhn's original post at gruhn.me, which Willison links to and which
  contains the full argument. Both were fetched and read in full (Gruhn's
  post is a single page with no substantive sub-links; Willison's post links
  only to Gruhn's article and to Willison's own tag-archive pages, neither
  of which are substantive continuations).
- **Author credibility**: Niklas Gruhn is the primary author; no independent
  corroboration of his professional background was found in either fetched
  page — the claims stand on the strength of his argument and concrete
  examples, not on an established public track record in this corpus (this
  is his first appearance). Simon Willison is an established, high-signal
  commentator on LLM tooling already extensively represented in this corpus
  (see the `blog-simonwillison-*` notes); his role here is curation and
  amplification, not original argument — he adds one sentence of framing
  ("Niklas Gruhn coins an excellent new term - meat proxy - for people who
  blindly copy and paste the output of AI systems to their peers") and then
  quotes Gruhn's own paragraph verbatim.
- **Scope**: Gruhn's post is short — seven brief paragraphs. It covers: the
  specific behavioral pattern being named (verbatim-relay of AI chat output
  into human conversations), why reading AI output is costly (verbosity,
  plausible nonsense, jargon density, with one concrete jargon example), the
  prescribed remedy (read/understand/validate/rewrite-in-own-words), and a
  single extended example applying the same pattern to code review (copy the
  ticket in, don't read the code, copy reviewer feedback back in, iterate).
  It does NOT provide data, a study, or multiple examples beyond the one
  Slack/PR/WhatsApp framing and the one code-review framing — this is a
  single practitioner's named-pattern essay, not a research piece.

## Extracted Claims

### Claim 1: Verbatim-relaying an AI system's response into a human conversation (Slack, PR feedback, group chat) is a distinct, nameable failure mode — a "meat proxy" — because it adds no value the recipient couldn't get by querying the AI directly
- **Evidence**: Author's own repeated first-person experience being on the receiving end of this pattern across three different communication channels.
- **Confidence**: anecdotal
- **Quote**: "I can talk to Claude myself. It's going to be faster and I get to control the context. I don't need a meat proxy in between."
- **Our assessment**: This is the post's core claim and the source of its guide-usable vocabulary. The reasoning is sound as a communication-norm argument (a relayed, unedited AI response is strictly worse for the recipient than direct access to the AI), independent of whether "meat proxy" catches on as a term. Its actionability for the guide is in the negative case it defines: any AI-mediated communication artifact a human passes along unread should specifically fail this test.

### Claim 2: The specific behavioral signature of the failure mode is pasting the model's full, unedited response and attributing it only by name, with no synthesis
- **Evidence**: The author's own quoted example of the exact message format he receives.
- **Confidence**: anecdotal
- **Quote**: "I ask a question in Slack or leave feedback under a merge/pull request or argue with friends in a WhatsApp group and get back: Claude said: [giant response verbatim]"
- **Our assessment**: Useful because it's checkable — "Claude said: [pasted output]" with zero added framing is a concrete pattern a team could actually flag in a Slack norms doc or PR review guideline, rather than a vague "don't overuse AI" instruction.

### Claim 3: Reading AI output imposes real extra cognitive cost on the recipient specifically because it tends to be verbose, contains plausible-sounding falsehoods, and is increasingly dense with jargon — illustrated by a real sentence the author had to look up almost word-for-word
- **Evidence**: Author's own example of a jargon-dense sentence received from Claude, plus his stated reaction.
- **Confidence**: anecdotal
- **Quote**: "Reading AI output is extra effort. It's verbose, frequently contains all too plausible nonsense, and is increasingly jargon dense."
- **Quote (example sentence)**: "NATS control-plane events: stream leader election / R3 quorum re-form during pod churn."
- **Quote (reaction)**: "Jesus. I had to lookup almost every word to make sense of this."
- **Our assessment**: This is the claim's mechanism, not just its symptom — it explains *why* relaying AI output shifts cost onto the recipient rather than removing it: jargon density means the recipient can't skim, they have to actively decode. This is a specific, concrete example (unlike a generic "AI output can be verbose" claim) and is novel in this corpus for naming jargon density specifically, rather than length alone, as a comprehension tax.

### Claim 4: The prescribed remedy is a four-step discipline — read, understand, validate, then rewrite the response in your own words — and the act of rewriting functions as a self-check that the first three steps actually happened
- **Evidence**: Author's own prescriptive statement, presented as the post's thesis/resolution.
- **Confidence**: anecdotal
- **Quote**: "By all means, prompt AI. But don't just relay the output. Read it, understand it, validate it, and then write a response in your own words (a decent certificate that you've done the prior steps). Making that effort is value you can add."
- **Our assessment**: The "certificate" framing is the most guide-actionable phrase in the post — it converts a vague exhortation ("understand before you share") into an operational test: if you cannot rewrite the AI's output in your own words, you have not actually understood it, and you should not be relaying it as your own contribution. This is a lightweight, self-administered check that requires no tooling, unlike verification mechanisms elsewhere in this corpus that rely on rubric-based evals or decision logs (see Cross-References).

### Claim 5: The same failure mode appears in code review as a specific, low-effort workflow — copy the ticket into Claude Code, don't read the generated code, copy reviewer feedback back in, iterate — which "works" mechanically but means the reviewers, not the nominal author, actually did the implementation
- **Evidence**: Author's own worked example of a minimal-effort shipping workflow, followed by his own rhetorical question and answer.
- **Confidence**: anecdotal
- **Quote**: "Shipping some code can be done with close to zero effort now: Copy/paste the ticket description into Claude Code. Don't look at the code or read what Claude has written. If there's any feedback from reviewers, copy/paste that into Claude Code as well. If necessary, iterate."
- **Quote (conclusion)**: "That works. But who has done the implementation? The reviewers did, using Claude Code, and you as a meat proxy."
- **Our assessment**: This is the post's sharpest and most guide-relevant extension of the core claim, because it relocates the "meat proxy" failure from communication into engineering process specifically: if the nominal PR author never reads the diff, the actual verification and understanding work is done entirely by whoever reviews it, and the author contributes nothing but a relay function between the ticket and the reviewer's feedback. This directly names a code-review anti-pattern this corpus has evidence for from the review-capacity side (see Cross-References) but not previously from the author-side motivation for why it happens.

### Claim 6: The author explicitly implicates himself as having done the same thing he's criticizing, framing the post as self-aware correction rather than one-sided accusation
- **Evidence**: Author's own admission, placed immediately after describing the pattern.
- **Confidence**: anecdotal
- **Quote**: "I mean, I've done this. But I've been on the receiving end too many times now."
- **Our assessment**: Low evidentiary weight on its own, but relevant context for how to cite this source: the author is not describing a hypothetical junior-engineer failure mode from a distance, he is naming a pattern he catches himself doing. This matters for guide tone — the recommended framing is "a habit to catch yourself in," not "a fault to police in others."

### Claim 7: Simon Willison, an independent high-signal commentator on LLM tooling, judged "meat proxy" specifically worth naming and amplifying to his own audience, describing it as coining "an excellent new term"
- **Evidence**: Willison's own editorial framing in his link post, which quotes Gruhn's remedy paragraph in full and adds no further argument of his own.
- **Confidence**: anecdotal
- **Quote**: "Niklas Gruhn coins an excellent new term - meat proxy - for people who blindly copy and paste the output of AI systems to their peers."
- **Our assessment**: This is curation-as-signal rather than independent evidence for the underlying claim — Willison did not test or extend Gruhn's argument, he judged it citation-worthy. Given Willison's extensive, already-cited footprint in this corpus as someone who tracks a very high volume of LLM-tooling writing, his choice to link-post this specific short essay (rather than the many other candidate posts he reads and skips) is a mild signal that the term is likely to propagate in practitioner discourse, which is itself a reason a guide naming failure modes might want to use the same term rather than inventing a competing one.

## Concrete Artifacts

```
Source: Niklas Gruhn, "Don't be a meat proxy", gruhn.me, 2026-08-03
Full post text (verbatim, minus HTML markup):

Too often I ask a question in Slack or leave feedback under a merge/pull
request or argue with friends in a WhatsApp group and get back:

  Claude said: [giant response verbatim]

Please don't do this. I mean, I've done this. But I've been on the
receiving end too many times now. This is not adding value. I can talk to
Claude myself. It's going to be faster and I get to control the context. I
don't need a meat proxy in between.

Reading AI output is extra effort. It's verbose, frequently contains all
too plausible nonsense, and is increasingly jargon dense. I recently got
this sentence from Claude:

  NATS control-plane events: stream leader election / R3 quorum re-form
  during pod churn.

Jesus. I had to lookup almost every word to make sense of this.

By all means, prompt AI. But don't just relay the output. Read it,
understand it, validate it, and then write a response in your own words (a
decent certificate that you've done the prior steps). Making that effort is
value you can add.

Take code review in particular. Shipping some code can be done with close
to zero effort now: Copy/paste the ticket description into Claude Code.
Don't look at the code or read what Claude has written. If there's any
feedback from reviewers, copy/paste that into Claude Code as well. If
necessary, iterate.

That works. But who has done the implementation? The reviewers did, using
Claude Code, and you as a meat proxy.
```

```
Source: Simon Willison, "Don't be a meat proxy" (link post),
simonwillison.net, 2026-08-03T23:45:00Z

Niklas Gruhn coins an excellent new term - meat proxy - for people who
blindly copy and paste the output of AI systems to their peers.

  By all means, prompt AI. But don't just relay the output. Read it,
  understand it, validate it, and then write a response in your own words
  (a decent certificate that you've done the prior steps). Making that
  effort is value you can add.

Tags: definitions, ai, generative-ai, llms, ai-misuse
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-litt-understand-to-participate.md` (Claim 2, Claim
    3): Litt's framing — that a developer needs a "rich set of concepts" to
    "participate" in agent-assisted work, and that insufficient fluency
    "meaningfully limits" that participation — is the same underlying
    requirement (genuine comprehension, not surface-level following) that
    this source's Claim 4 states as an operational test ("write a response
    in your own words"). Litt's post argues *why* understanding matters for
    directing agent work; this source supplies a concrete, self-administered
    check for whether that understanding is actually present.
  - `blog-addyosmani-earning-taste-judgment.md` (Claim 7, the Shaw & Nave
    "cognitive surrender" study: ~80% acceptance of incorrect AI output,
    confidence rising while accuracy falls) and `blog-addyosmani-own-the-outer-loop.md`
    (which names "cognitive surrender" as one of three "hidden costs of
    delegation"): both describe the same underlying failure at the level of
    an individual's judgment about AI output; this source names the
    *interpersonal* consequence of the same underlying failure — surrendered
    judgment doesn't stay contained to the individual, it gets relayed
    outward to other people ("meat proxy") who then have to redo the
    verification work themselves.
  - `blog-addyosmani-agentic-code-review.md` (Claim 8: agents discard their
    reasoning once a diff is produced, forcing reviewers to reconstruct
    intent; Claim 2: Faros AI's finding of a 31.3% rise in PRs merging with
    zero review): this source's Claim 5 (copy ticket in, don't read the
    code, copy feedback back) is a first-person, motive-level account of
    exactly the author-side behavior that produces the review-capacity
    crisis those quantitative findings describe from the reviewer-side. The
    two sources corroborate the same phenomenon from opposite ends of the
    same PR.
- **Contradicts**: None identified. No claim in this source was found to
  directly oppose an existing corpus source note on the same topic.
- **Extends**:
  - `blog-addyosmani-agentic-code-review.md`: that note documents review
    *capacity* being overwhelmed (churn, defect rate, review duration all
    up) without fully explaining the author-side incentive that produces
    additional low-effort submissions; this source's Claim 5 supplies that
    missing author-side account — a PR author can now ship without reading
    their own diff, which is a distinct contributing cause to review load
    beyond raw volume increase.
  - `blog-simonwillison-litt-understand-to-participate.md`: extends Litt's
    abstract "understand to participate" framing with a concrete,
    low-tooling operational test (can you rewrite it in your own words?)
    that a team could adopt immediately, where Litt's post states the need
    for understanding but does not supply a check for whether it's present.
- **Novel**:
  - The "meat proxy" term itself and its specific definition (a person who
    relays AI output unread/unvalidated to other people, as distinct from a
    person who merely over-trusts AI output for their own decisions) is new
    to this corpus — existing related notes describe over-trust in AI output
    as a private judgment failure (cognitive surrender, cognitive debt); this
    source is the first to name the version of that failure that is
    specifically interpersonal (relaying unread/unvalidated output to a
    second human).
  - The "write it in your own words" test as an operational check for
    whether understanding actually occurred is new to the corpus as a named,
    self-administered practice — related sources recommend reading code,
    keeping a wrong log, or building rubric-based evals, but none propose
    the low-cost "can you restate this without the source in front of you"
    check.
  - The jargon-density mechanism specifically (as distinct from mere
    verbosity) as a reason AI output requires deliberate decoding effort
    before being safe to relay is new to the corpus.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add "meat proxy" as a named anti-pattern
  for day-to-day AI-mediated communication (Slack answers, PR comments,
  chat threads) — the concrete signal to flag is a message that opens with
  "[Model] said:" followed by unedited pasted output and no synthesis
  (Claim 2). Pair with the "write it in your own words" self-check (Claim 4)
  as a lightweight norm teams can adopt without new tooling.
- **Chapter 03 (Verification)**: Cite Claim 5 (the ticket-in/don't-read/
  feedback-back-in workflow) as a first-person account of the specific
  author-side behavior that produces the review-capacity problems already
  documented via Faros AI/CodeRabbit/GitClear data in
  `blog-addyosmani-agentic-code-review.md`. Recommend the guide explicitly
  distinguish "the AI wrote code that was reviewed" from "the AI wrote code
  that nobody but the reviewer ever read" — this source shows the latter is
  an easy, low-effort default absent an explicit norm against it.
- **Chapter 05 (Team/Hiring)**: The jargon-density observation (Claim 3)
  is a concrete, quotable justification for a team communication norm: raw
  AI output should not be treated as a finished, shareable artifact by
  default, because its jargon density imposes a real, uneven decoding cost
  on recipients who did not generate it.

## Extraction Notes

- Both linked pages were fetched and their raw HTML parsed directly (not
  relied on WebFetch's summarizing pass) to guarantee verbatim quotes per
  MINER.md §2a: `gruhn.me/blog/2026-08-03/` and
  `simonwillison.net/2026/Aug/3/dont-be-a-meat-proxy/`. A first WebFetch pass
  on the Willison URL returned an accurate paraphrase that matched the raw
  HTML closely, but all quotes in this note were verified against the raw
  HTML extraction, not taken from that paraphrase.
- Gruhn's article is a single page with no sub-links worth following (no
  footnotes, no linked studies, no embedded code repository). Willison's
  post links only to Gruhn's article itself and to Willison's own
  tag-archive pages (`ai`, `generative-ai`, `llms`, `ai-misuse`,
  `definitions`), which are not substantive continuations of this specific
  piece.
- The source is genuinely short (Gruhn's post is seven short paragraphs;
  Willison's is two sentences plus a blockquote) — this caps the achievable
  claim count below the higher end of the 5-15 target range. Seven claims
  were extracted without padding or inventing content not present in either
  fetched page; a longer claim list would have required treating minor
  rephrasings of the same two or three ideas as distinct claims.
- No independent biographical information on Niklas Gruhn was found via the
  fetched pages themselves (no author bio, no "about" page followed, per the
  5-linked-page budget being better spent on verifying quotes than on
  background that doesn't change how the claims should be weighted).
- No contradiction with existing corpus notes was identified — see
  Cross-References/Contradicts above.
