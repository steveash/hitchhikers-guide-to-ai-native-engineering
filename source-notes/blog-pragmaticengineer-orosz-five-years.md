---
source_url: https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-five-years
source_type: blog-post
title: "The Pragmatic Engineer: Five years"
author: Gergely Orosz (The Pragmatic Engineer)
date_published: 2026-09-01
date_extracted: 2026-09-02
last_checked: 2026-09-02
status: current
confidence_overall: anecdotal
issue: "#3164"
---

# The Pragmatic Engineer: Five years

> A fifth-anniversary retrospective and editorial-plans piece from Gergely Orosz that is
> mostly newsletter-business meta-commentary (subscriber growth, event/podcast plans, an
> essay contest), but contains a handful of substantive, single-author claims worth
> extracting: an explicit statement that the publication deliberately does not use AI to
> write its own content (only for research assistance and typo-checking, because AI
> "easily lead[s] you down the wrong track"), a short unsupported assertion that IDEs and
> code review are "falling out of style," and a claim that engineering fundamentals and
> "standout" pre-AI engineers remain in high demand.

## Source Context

- **Type**: blog-post (newsletter retrospective / editorial announcement, not a reported
  deepdive or interview piece)
- **Author credibility**: Gergely Orosz is an ex-Uber engineering manager who runs The
  Pragmatic Engineer, already a heavily corroborated corpus author (see
  `survey-pragmaticengineer-ai-tooling-2026.md`, `blog-pragmaticengineer-orosz-inside-anthropic.md`,
  `blog-pragmaticengineer-neetcode-interview.md`, `blog-pragmaticengineer-orosz-slow-down-speed-up.md`,
  among others). This specific piece states the newsletter now has "more than 1.1M
  readers, tens of thousands of paid subscribers, a podcast, and more than 500,000
  YouTube subscribers," and that it was, by the end of 2021, "the #1 paid technology
  newsletter on Substack (!!), with 2,700 paid subscribers and 30,000 free subscribers,"
  and is "the third most expensed newsletter at startups, globally, in 2026" per the Brex
  Benchmark. Unlike the corpus's other Pragmatic Engineer sources, this piece is not a
  reported deepdive with named interviewees — it is Orosz's own first-person editorial
  voice, reflecting on the publication itself.
- **Scope**: Covers newsletter history (2021–2026 timeline of features launched: The
  Pulse, direct company-access deepdive reporting, the podcast, the Pragmatic Summit,
  team expansion), the publication's editorial AI-usage policy, a short "What's next?"
  section touching on how software engineering is changing, and an essay-contest
  announcement. Does NOT cover any specific company, team, or measured engineering
  practice in depth — the "software engineering is changing" claims are brief, unsourced
  editorial assertions rather than reported findings, and the piece explicitly frames the
  essay contest as an attempt to source exactly that kind of first-hand evidence from
  readers, i.e., the publication is soliciting the deep material this piece itself does
  not contain.

## Extracted Claims

### Claim 1: The Pragmatic Engineer deliberately does not use AI to write its published content, using it only for research assistance and post-draft spelling/grammar checking, because the author judges AI to be unreliable for open-ended analysis and prone to inventing false connections
- **Evidence**: First-person statement of the publication's own editorial policy and its
  stated rationale, from the author who runs it.
- **Confidence**: anecdotal (a single publisher's stated policy and personal judgment, not
  a measured comparison or industry survey)
- **Quote**: "Needless to say, we've experimented with the analytical powers of AI tools in
  parts of the research process. The technology is good at gathering publicly-available
  sources and does a decent job of summarizing them, but that's been more or less the
  limits of AI's usefulness for our purposes to date – except as a spelling and grammar
  checking tool after a full draft is written by a person. If anything, AI can easily lead
  you down the wrong track by theorizing about non-existent connections and confidently
  espousing theories which some basic critical thinking could easily debunk! Aside from
  research and correcting (most) typos, we don't use AI in this publication. That's
  because we are writing for a readership of humans and believe in the value of human
  voices."
- **Our assessment**: This is the most concrete, guide-relevant claim in the piece. It is
  a specific, named failure mode ("theorizing about non-existent connections and
  confidently espousing theories") stated by a high-profile, AI-adjacent tech writer who
  is otherwise enthusiastic about AI coding tools in his reporting — making the caveat
  more notable than a generic AI-skeptic take would be. It should be read as a scoped
  claim about a specific task category (open-ended research synthesis and long-form
  writing under a human byline) rather than a general claim that AI underperforms at
  writing tasks broadly.

### Claim 2: A "big theme" for the rest of 2026 for the publication's coverage is that IDEs are falling out of style and code review is becoming optional, with the biggest change being that engineers spend little to no time typing code
- **Evidence**: Editorial framing/assertion by the author, stated without citing a
  specific company, dataset, or interview in this piece.
- **Confidence**: anecdotal (unsupported assertion in this specific article — no data,
  example, or named source is given here; see Cross-References for where the corpus has
  independently-sourced, better-evidenced versions of the same claims)
- **Quote**: "A big theme for the rest of 2026 is how software engineering is changing:
  tools used for decades like IDEs are falling out of style, and processes long
  considered as best practices, like code reviews, are becoming optional. Of course, the
  biggest change is that we're spending little to no time on typing out the code, which
  has never been the case since computing existed. Even before computer keyboards,
  programmers were writing programs on punch cards!"
- **Our assessment**: Taken alone, this is a thin, unsupported assertion — exactly the
  kind of "meta-commentary" the first Prospector triage comment flagged. Its value to the
  guide is not as a standalone data point but as confirmation that Orosz's own editorial
  team judges "code review becoming optional" and "IDEs falling out of style" to be a
  significant enough trend to make it a named coverage priority for the rest of 2026 —
  which is corroborated with real data and named companies elsewhere in the corpus (see
  Cross-References). Do not cite this quote alone as evidence; cite it alongside the
  better-evidenced sources it points toward.

### Claim 3: Despite the above, "fundamentals still matter" — engineers who were considered standout developers before AI tooling remain, or are more, in demand, and picking up AI-assisted engineering is reported as easier than learning a new programming language
- **Evidence**: Editorial assertion by the author, immediately following Claim 2's "big
  theme" framing, presented as a counterbalancing observation rather than a contradiction.
- **Confidence**: anecdotal (unsupported assertion; no data, example, or named source
  given in this piece)
- **Quote**: "The good news is that we see that fundamentals still matter: many software
  engineers who were considered standout devs before seem to be even more in demand than
  ever, while picking up AI engineering appears to be easier than learning a new
  programming language."
- **Our assessment**: Directionally consistent with, but far less specific than, existing
  corpus claims about "effort"/judgment/taste remaining differentiators as AI commoditizes
  raw code output (see Cross-References). Treat as a thin corroborating data point, not a
  new finding — the corpus already has better-sourced, named-practitioner versions of this
  same argument.

### Claim 4: The author states the current AI-driven change to software engineering is "destabilizing" and "fast-paced," with no one having "figured out the 'right' way to build software with AI," while asserting that teams remain as important a structural unit at leading AI labs as they were pre-AI
- **Evidence**: Editorial assertion, with the "teams... just as important" clause
  hyperlinked in the original article to a specific section of a separate, earlier
  Pragmatic Engineer piece on team-level changes (not independently verified as part of
  this extraction — see Extraction Notes).
- **Confidence**: anecdotal (unsupported editorial assertion in this piece; the linked
  claim about team structure is sourced to a different article that would need its own
  extraction to verify)
- **Quote**: "Nonetheless, this change is destabilizing, fast-paced, and no one has
  figured out the "right" way to build software with AI. We'll keep reporting on cases of
  teams and individuals that adapt well, while also paying attention to those things that
  don't change, such as how teams, as a "core" unit of a business, seem to be just as
  important at leading AI labs as they were pre-AI."
- **Our assessment**: The "no one has figured out the right way" framing is a useful,
  quotable epistemic-humility marker from a well-sourced industry observer — worth citing
  in any guide section that risks overstating confidence in a single "correct" AI-adoption
  playbook. The "teams remain just as important" clause is asserted here, not
  demonstrated; the corpus's `blog-pragmaticengineer-orosz-inside-anthropic.md` (Claim 15)
  already flags that the corresponding "Team-level changes" section of a related Anthropic
  deepdive is paywalled and only available as a teaser, so this specific sub-claim remains
  thinly evidenced across the corpus, not just in this article.

### Claim 5: The author reports that AI has made context-switching between writing and building software easier for him personally, leading him to build more of the publication's own internal backend software (landing pages, API endpoints for subscriptions/refunds) in the past six months than in all previous years of running the newsletter combined
- **Evidence**: First-person anecdote about the author's own workflow and output over a
  stated six-month window, with no external verification or metrics beyond his own
  characterization ("probably built more").
- **Confidence**: anecdotal (single individual's self-reported, unquantified before/after
  comparison)
- **Quote**: "One thing that AI has made easier is context switching between writing and
  building software. In the past six months, I've found myself building more parts of The
  Pragmatic Engineer backend stack, such as landing pages, through to API endpoints used
  for group subscriptions, refunds, and more. This year, I've probably built more software
  scratching my own itch at the publication than in previous years combined!"
- **Our assessment**: A small but concrete, non-engineering-professional example of AI
  agents lowering the activation cost for a domain expert (a writer, not primarily a
  software engineer) to build internal tooling for their own business. It corroborates the
  broader corpus theme of AI compressing the cost of small, single-owner internal software
  projects, but as a single, self-reported, unquantified anecdote from a non-engineer, it
  should be cited only as an illustrative example, not as evidence of a measured
  productivity gain.

## Concrete Artifacts

```
Newsletter growth timeline (verbatim years/events, from the article body):
Source: https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-five-years

2021: Launched; crossed 1,000 paid subscribers six weeks after launch; by end of 2021,
  "the #1 paid technology newsletter on Substack (!!), with 2,700 paid subscribers and
  30,000 free subscribers." Growth attributed to word-of-mouth and the author's own
  social-media posts, "without spending on ads and marketing."
2022: Launched "The Scoop" (later renamed "The Pulse"), a weekly Thursday column.
2023: Shifted from indirect/"back door" reporting to going directly to companies for
  deepdives (named examples in the article: OpenAI, Meta/Threads, Stripe, Figma).
2024: Launched The Pragmatic Engineer Podcast (named guests: Grady Booch, Nicole
  Forsgren).
2025: First Pragmatic Summit, San Francisco, "500 attendees and 15 speakers."
2026: Team expanded (named additions: Jessica Salmon, Ivan Klaric) "to produce more
  ambitious deepdives."

Current reach (as stated in this article): "more than 1.1M readers, tens of thousands of
paid subscribers, a podcast, and more than 500,000 YouTube subscribers." Per the "Brex
Benchmark," described as "the third most expensed newsletter at startups, globally, in
2026."
```

```
"Recent deepdives" list named in this article (verbatim titles):
Source: https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-five-years

- "Why Ramp built its own in-house coding agent, Inspect"
  [Already extracted in full: blog-pragmaticengineer-orosz-ramp-inspect.md]
- "Software engineering at a proprietary trading company: Optiver"
  [Already extracted in full: blog-pragmaticengineer-optiver-trading-engineering.md]
- "How building software is changing at Anthropic"
  [Already extracted in full: blog-pragmaticengineer-orosz-inside-anthropic.md]
- "State of the software engineering job market in 2026"
  [Not yet confirmed as extracted under this exact title in source-notes/ as of this
  extraction — flagged for the Prospector as a possible future submission if not already
  queued; see Extraction Notes.]
```

```
Essay-challenge announcement (verbatim, from the "3. How software engineering is
changing: essay challenge" section):
Source: https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-five-years

"Send us an article no more than 10,000 words long on how you see things changing at
your startup or tech company. We'll award $10,000 for the best essay we read, and other
leading entries can win smaller prizes. Articles sent to us will be eligible for
publication in future editions of the Pragmatic Engineer."

"So, tell us what's new, different, better, or worse in your part of the tech industry
since AI has been in your workflow."

Deadline: "Submissions close 4 October at midnight (PST)."
```

## Cross-References

- **Corroborates**:
  - `blog-pragmaticengineer-orosz-slow-down-speed-up.md` Claim 7 (Cursor's own usage data
    shows a sharp rise in code changes accepted with no human review at all, beginning
    around February 2026): this article's Claim 2 ("processes long considered as best
    practices, like code reviews, are becoming optional") is the same author's later,
    unsourced restatement of a claim that source documents with named vendor data. Cite
    the Cursor-data source for the actual evidence; cite this article only as confirmation
    that the same author still judges the trend significant seven weeks later.
  - `blog-pragmaticengineer-neetcode-interview.md` Claim 4 ("Effort" — engagement, care,
    and the willingness to defend one's decisions — becoming the key differentiator
    between engineers as AI makes other skills cheap) and Claim 11 (learning hard things
    builds judgment that stays valuable regardless of how AI tools change): this article's
    Claim 3 ("fundamentals still matter... standout devs... more in demand than ever") is
    a thinner, unsourced restatement of the same argument from the same publication.
  - `failure-nyt-ai-fabricated-quote.md` (a New York Times reporter used an AI tool to
    obtain a quote, did not verify it against the original source, and published a
    fabricated quotation): this article's Claim 1 — Orosz's stated reason for keeping AI
    out of the publication's actual writing ("AI can easily lead you down the wrong track
    by theorizing about non-existent connections and confidently espousing theories") — is
    an independent, pre-emptive articulation of essentially the same failure mode that
    source documents as having actually occurred at a different publication. Together they
    make a stronger case that "AI hallucinating unverified claims/quotes in
    editorial/analytical writing" is a recognized, non-hypothetical risk in
    journalism-adjacent content work, not a one-off incident.
- **Extends**: `blog-pragmaticengineer-orosz-inside-anthropic.md` (that note's Claim 15
  documents a paywalled teaser, from a companion Anthropic deepdive by the same author, on
  "Team-level changes" and a "still the same" list including two-pizza teams): this
  article's Claim 4 ("teams, as a 'core' unit of a business, seem to be just as important
  at leading AI labs as they were pre-AI") is the same underlying claim, restated publicly
  and unpaywalled, but still without the supporting detail that remains locked behind that
  earlier article's paywall.
- **Novel**: The explicit statement of a specific media outlet's editorial policy on *not*
  using AI to write its own content, with a stated rationale (Claim 1). No existing source
  note documents a named publication's internal AI-usage policy for content creation
  itself — the corpus's other journalism/AI-adjacent source
  (`failure-nyt-ai-fabricated-quote.md`) documents a failure that occurred *because* AI was
  used for a writing/quoting task, not a stated policy of deliberately not using it.
- **Contradicts**: None found. This article's own "fundamentals still matter" claim
  (Claim 3) is presented by the author as a complement to, not a contradiction of, its
  "code review becoming optional" claim (Claim 2) — both describe different facets of the
  same transition rather than opposing positions, and neither rises to a filed-worthy
  contradiction against another corpus source per MINER.md §4a.

## Guide Impact

- **Chapter 00 (Principles) or a "Where not to use AI" section**: Claim 1 (Orosz's stated
  editorial policy and its rationale) is a concrete, quotable example — from a
  high-profile, generally AI-enthusiastic tech writer, not an AI skeptic — of deliberately
  scoping AI usage away from a specific task (open-ended analytical writing under a human
  byline) while still using it for a narrower, verifiable adjacent task (research
  gathering, typo-checking). Pair with `failure-nyt-ai-fabricated-quote.md` as the "what
  happens if you don't draw this line" companion case.
- **Chapter 01/05 (Daily Workflows / Team Adoption)**: Do NOT cite Claims 2–4 as
  standalone evidence for "code review is becoming optional" or "IDEs are falling out of
  style" — they are unsourced assertions in this specific piece. If the guide already
  cites `blog-pragmaticengineer-orosz-slow-down-speed-up.md`'s Cursor-data-backed version
  of the code-review claim, this article can be added as a one-line "and the same author
  still flagged this as a major 2026 theme seven weeks later" footnote, nothing more.
- **Chapter 05 (Team Adoption)**: Claim 5 (AI lowering the activation cost for a
  non-engineer to build internal tooling) is a small, illustrative, non-engineering
  example worth a passing mention if the guide discusses AI's effect broadly on
  "non-specialist building," but it is too thin (one person, six months, no metrics) to
  anchor a recommendation on its own.

## Extraction Notes

- **Verbatim quotes verified against raw HTML, not WebFetch summarization**: An initial
  WebFetch pass returned an AI-paraphrased summary (e.g., rendering the "IDEs falling out
  of style" passage with different wording each time it was re-fetched). All quotes in
  this note were instead copied character-for-character from the raw page HTML retrieved
  via `curl` with a browser user-agent (HTTP 200), after stripping markup — consistent
  with the verbatim-quote-verification approach already used in
  `blog-pragmaticengineer-ai-hiring-market-2026.md` and
  `blog-pragmaticengineer-orosz-inside-anthropic.md`.
- **No paywall encountered**: Unlike several other Pragmatic Engineer sources in this
  corpus, this specific article's full text (including the essay-contest section and the
  closing sign-off) was freely accessible without a paid-subscriber gate.
- **One internal hyperlink not followed**: The phrase "seem to be just as important" in
  Claim 4 is hyperlinked in the original article to a specific anchor
  (`#4-team-level-changes`) inside a different, earlier Pragmatic Engineer post. That
  linked post was not fetched or extracted as part of this pass — it is a separate article
  with its own publish date and would need its own source-note submission if not already
  in the corpus (it is plausibly the same "Team-level changes" material teased, and
  paywalled, in `blog-pragmaticengineer-orosz-inside-anthropic.md` Claim 15, but this was
  not independently confirmed).
- **"State of the software engineering job market in 2026" not independently confirmed as
  extracted**: this article names it as one of its own recent deepdives, but this
  extraction pass did not exhaustively search the full `source-notes/` directory (994
  files) for a matching note beyond a targeted check against the Prospector-flagged
  overlapping notes and a keyword search; flagging for the Prospector rather than
  asserting it is a gap.
- **Source is thin overall**: The bulk of the article (subscriber counts, event plans,
  team hires, podcast guest names, the essay-contest mechanics) is newsletter-business
  meta-commentary with no engineering-practice content, consistent with the first
  Prospector triage comment's assessment. The five claims extracted above represent the
  entirety of the article's substantive, guide-relevant content; this is a legitimately
  thin source, not an under-read one — the full article text (verified via raw HTML) was
  read in its entirety.
