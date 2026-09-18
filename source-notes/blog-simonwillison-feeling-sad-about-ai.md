---
source_url: https://simonwillison.net/2026/Sep/11/feeling-sad-about-ai/
source_type: blog-post
title: "Feeling sad about AI"
author: Simon Willison
date_published: 2026-09-11
date_extracted: 2026-09-18
last_checked: 2026-09-18
status: current
confidence_overall: anecdotal
issue: "#3525"
---

# Simon Willison: Feeling Sad About AI

> Willison republishes his own Hacker News comment reframing the "existential crisis"
> engineers feel when a coding agent does a week of work in an hour: the crisis is a
> common, survivable rite of passage, spec-to-code translation stops being a unique skill
> but a much larger set of problems remains where experience is still the differentiator,
> and radical tooling change has always been part of choosing software engineering as a
> career — this is just a faster iteration of it.

## Source Context

- **Type**: blog-post — specifically a "Comment" beat on Willison's link-blog: the page
  republishes, verbatim, a comment he posted to a Hacker News thread titled "Feeling sad
  about AI" (`news.ycombinator.com/item?id=49661506#49662090`). It is not an essay written
  for the blog; it is a five-paragraph HN comment cross-posted with no additional framing,
  intro, or edits beyond the "My comment on ... Feeling sad about AI — Hacker News" byline
  bar at the top of the page. The linked Hacker News thread itself returned HTTP 429 on
  fetch during this extraction (see Extraction Notes) and was not read; this note extracts
  only from Willison's own comment text, which is the full, self-contained content of the
  `source_url`.
- **Author credibility**: Simon Willison is the creator of Django, a 25-year software
  engineering practitioner, and one of the highest-signal independent AI-tooling
  commentators already extensively represented in this corpus (see, e.g.,
  `blog-simonwillison-why-ai-hasnt-replaced-engineers.md`,
  `blog-simonwillison-charity-majors-code-economics.md`). This piece is first-person
  testimony about his own past experience ("myself included, a few years ago now"), not
  third-party reporting or curation of someone else's argument.
- **Scope**: Covers exactly one thing — the emotional/professional arc of encountering a
  coding agent that outperforms a week of one's own work, and how Willison reframes that
  shock. Does NOT cover: any data, metrics, named companies, specific tools, or
  recommended practices. It is five paragraphs (roughly 200 words) of personal reflection,
  not an argument built on evidence.

## Extracted Claims

### Claim 1: The existential crisis engineers feel on encountering capable coding agents is common, and many people — Willison included — have already been through it and come out the other side

- **Evidence**: First-person testimony, offered as reassurance to the original Hacker News
  poster and other readers of the "Feeling sad about AI" thread.
- **Confidence**: anecdotal (a single practitioner's self-report, offered explicitly as
  possibly not useful: "I'm not sure how useful it is to say this")
- **Quote**: "I'm not sure how useful it is to say this, but I think a lot of people
  (myself included, a few years ago now) have been through this moment of existential
  crisis and come out the other side."
- **Our assessment**: This is a reassurance claim, not an evidenced one — "a lot of
  people" is unquantified and there is no data behind it. Its value is as a normalizing,
  quotable framing for a guide audience that may be experiencing the same reaction, from
  an author credible enough that the reassurance carries weight beyond a generic
  pep-talk.

### Claim 2: The initial reaction to watching a coding agent complete a week's worth of work in an hour, and do it well, is to feel very disheartened

- **Evidence**: Willison's own characterization of the typical first reaction, stated as
  a general pattern rather than a specific dated incident.
- **Confidence**: anecdotal
- **Quote**: "The initial reaction, when some coding agent does a piece of work that would
  have taken you a week in an hour and does it *well*, is to be very disheartened by it."
- **Our assessment**: The italicized "well" is load-bearing — Willison is explicit that
  the dread response is triggered specifically by quality, not just speed; a fast-but-bad
  output would not produce the same reaction. This is a personal-experience instance of
  the same supply-side economics shift Charity Majors names structurally (code generation
  went from "very hard, time-consuming, and expensive" to "effectively free and instant" —
  see Cross-References): Willison's "a week in an hour" is the felt, individual-scale
  version of Majors' economic claim.

### Claim 3: Once spec-to-code translation is accepted as no longer a unique skill, a much larger set of engineering problems remains, and existing skill and experience let a practitioner master new tools and outperform newcomers who lack that depth

- **Evidence**: Willison's own reasoning, presented as the resolution to the crisis named
  in Claim 1 — the mechanism by which he says people "come out the other side."
- **Confidence**: anecdotal
- **Quote**: "Once you come to terms with the idea that translating an exact specification
  into decent code isn't a unique skill any more, you can start looking at the larger set
  of problems that you face as a software engineer and realize that there is *so much
  left*, and your existing skill and experience mean you can master these new tools,
  provide value, and execute at a level far greater than anyone who is just getting
  started building software using agents without any of your depth."
- **Our assessment**: This is the essay's central claim and the one with the most
  existing corpus support (see Cross-References) — it is a compact, quotable restatement
  of the "job split" thesis found elsewhere in more structured or empirical form. Its
  specific contribution is naming *depth/experience* as the mechanism of continued
  advantage over "anyone who is just getting started building software using agents" —
  a direct claim that experienced engineers outperform AI-native newcomers specifically
  because of pre-AI depth, not despite it.

### Claim 4: Software engineering has never had more than roughly five years of stability in its tools and languages, so wanting the profession not to change at all was never a realistic expectation

- **Evidence**: Willison's own rhetorical framing, posed as a question rather than a
  sourced claim.
- **Confidence**: anecdotal (a rhetorical assertion with no supporting data; presented as
  a question, not a measured finding)
- **Quote**: "If you don't want your profession to change at all then you're going to
  have a tough time with this - but that's surely been true for the history of software
  engineering? Has there ever been any stability to the tools and language we use beyond
  about a five year time horizon?"
- **Our assessment**: The "five year" figure is asserted, not measured — no specific
  tooling history is cited to support it. Treat this as a rhetorical device rather than
  an empirical claim. It is nonetheless a distinct claim from Claim 3: Claim 3 argues
  *what remains valuable*, while Claim 4 argues the *premise of stability itself* was
  always false, independent of AI.

### Claim 5: Current AI-driven changes are happening faster than prior technology shifts, but choosing software development as a career has always meant opting into frequent radical change, so the pace difference is quantitative, not categorical

- **Evidence**: Willison's closing statement, generalizing from Claim 4's premise.
- **Confidence**: anecdotal
- **Quote**: "These changes are happening a bit faster, but if you chose software
  development as a passion you've opted into pretty frequent radical change from the
  start."
- **Our assessment**: This is a deliberate concession — Willison does not claim the
  current AI shift is the same magnitude as past shifts, only that it is the same *kind*
  of shift, accelerated. This is a more measured framing than either "this changes
  nothing" or "this changes everything," and is useful specifically because it
  acknowledges the pace difference rather than dismissing it.

## Concrete Artifacts

### Full text of the post (verbatim, all five paragraphs)

```
Source: https://simonwillison.net/2026/Sep/11/feeling-sad-about-ai/
Posted: 11th September 2026 at 5:28 pm
Byline: "My comment on Feeling sad about AI — Hacker News"
        (linking to news.ycombinator.com/item?id=49661506#49662090,
         thread news.ycombinator.com/item?id=49661506)
Tags: ai, generative-ai, llms, deep-blue

I'm not sure how useful it is to say this, but I think a lot of people (myself
included, a few years ago now) have been through this moment of existential crisis
and come out the other side.

The initial reaction, when some coding agent does a piece of work that would have
taken you a week in an hour and does it well, is to be very disheartened by it.

Once you come to terms with the idea that translating an exact specification into
decent code isn't a unique skill any more, you can start looking at the larger set
of problems that you face as a software engineer and realize that there is so much
left, and your existing skill and experience mean you can master these new tools,
provide value, and execute at a level far greater than anyone who is just getting
started building software using agents without any of your depth.

If you don't want your profession to change at all then you're going to have a
tough time with this - but that's surely been true for the history of software
engineering? Has there ever been any stability to the tools and language we use
beyond about a five year time horizon?

These changes are happening a bit faster, but if you chose software development as
a passion you've opted into pretty frequent radical change from the start.
```

## Cross-References

- **Corroborates**: `blog-kentbeck-jessicakerr-learning-system.md` Claim 1 ("AI didn't
  eliminate the programmer's job, it split it in two — hand-crafted code-writing is
  commoditized... while understanding what to build, proving it works, and stewarding
  the... system is the harder, more human remainder") and Claim 2 (Kerr: the
  code-crafting part "has been commoditized... But that's not all of our job"): this
  note's Claim 3 (spec-to-code translation is "not a unique skill any more" but "the
  larger set of problems" remains) restates the identical job-split thesis independently,
  from a different practitioner, in a different venue, using a different register
  (personal crisis narrative rather than podcast conversation). Three independent
  practitioners now converge on this framing.
- **Corroborates**: `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` Claim 12
  ("Give me all of the AI assistance in the world and the value I produce will still be
  reliant on how deeply I understand both the problems and the solutions that the agents
  are building for them" — Willison's own commentary, June 14, 2026): this note's Claim 3
  is the same author restating the same underlying position roughly three months later,
  in a different register (a Hacker News comment about a colleague's emotional crisis
  rather than commentary on a research essay). This strengthens confidence that the
  position is Willison's settled view rather than a one-off framing choice, consistent
  with the "recurring position across venues" pattern already noted for Kent Beck in
  `blog-pragmaticengineer-orosz-kentbeck-career.md` Claim 2.
- **Corroborates**: `blog-simonwillison-charity-majors-code-economics.md` Claim 1 ("In
  2025, the economics of code production were turned upside down — generation shifted
  from expensive and time-consuming to effectively free and instant"): this note's
  Claim 2 ("a coding agent does a piece of work that would have taken you a week in an
  hour") is the felt, individual-scale experience of exactly the economic inversion
  Majors names structurally. Majors describes the supply-side economics; Willison
  describes what that economics feels like to the engineer on the receiving end of it.
- **Extends**: `blog-pragmaticengineer-orosz-five-years.md` Claim 4 (Orosz: the current
  AI-driven change is "destabilizing, fast-paced, and no one has figured out the 'right'
  way to build software with AI"): both sources agree the current period is unusually
  fast-moving, but this note's Claim 5 adds a historical-continuity argument Orosz's
  piece does not make — Willison frames the instability as a faster iteration of a
  pattern that has always existed in software engineering ("opted into pretty frequent
  radical change from the start"), rather than as a novel, unprecedented condition. This
  is a difference in framing/emphasis, not a factual disagreement — both would agree the
  pace has increased — so it does not meet the MINER.md §4a bar for a contradiction issue.
- **Novel**: This is the first source note in the corpus built specifically around the
  *subjective, emotional arc* of an individual engineer's adaptation to AI coding
  capability — naming "existential crisis" directly and describing its resolution as a
  first-person process ("come out the other side"), rather than addressing labor
  economics, productivity data, or career-structure changes in the abstract. The corpus
  has extensive coverage of *why* engineering skill remains valuable (Narayanan/Kapoor,
  Beck, Majors) but this is the first source addressing the felt experience of getting
  from dread to that conclusion.
- **Contradicts**: None found. No claim in this source materially opposes an existing
  corpus source in a way that would change guide advice; it restates and personalizes a
  thesis the corpus already documents from other angles.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Claims 1–2 (existential crisis is common; the trigger is
  specifically an agent doing a week of work well, not just fast) give the guide a
  concrete, named emotional pattern to acknowledge when discussing engineer reactions to
  agentic tooling rollout. Currently the guide's adoption material (per the corpus's
  economics- and productivity-focused sources) argues *why* engineers remain valuable but
  does not name the dread reaction itself as a normal, expected, first stage. Recommend
  adding this as explicit framing: acknowledge the "week of work in an hour" shock as a
  common trigger before presenting the reframing argument, rather than jumping straight
  to the reassurance.
- **Chapter 00 (Principles)**: Claim 3's specific phrasing — that depth and experience let
  a practitioner "execute at a level far greater than anyone who is just getting started
  building software using agents without any of your depth" — is a compact, quotable
  restatement of the corpus's job-split thesis (see Cross-References) that is more
  accessible/personal than the Narayanan-Kapoor "decide-execute-deliver sandwich" framing
  already cited for Chapter 00. Recommend using this as a shorter, emotionally resonant
  companion quote alongside the more structural framings already in the guide.

## Extraction Notes

- **Source is a republished HN comment, not an essay**: The entire content of the
  `source_url` is five short paragraphs (~200 words) — Willison's own Hacker News comment,
  cross-posted with no additional blog-native commentary. This is legitimately thin
  source material, not an under-read source; the full text is reproduced verbatim in
  Concrete Artifacts and every sentence of it is covered by one of the five claims above.
- **Linked Hacker News thread not read**: The byline links to the originating HN thread
  (`news.ycombinator.com/item?id=49661506`, titled "Feeling sad about AI"). A fetch
  attempt during this extraction returned HTTP 429 (rate limited). Per MINER.md §1's "up
  to 5 linked pages" guidance, this was the only substantive linked page, and it was not
  accessible; this note extracts solely from Willison's own comment text at the canonical
  `source_url`, which is fully self-contained and was verified against raw HTML fetched
  via `curl` (not WebFetch's summarizing pass, which paraphrased rather than quoted
  verbatim on first attempt — consistent with the precedent in
  `blog-pragmaticengineer-orosz-five-years.md` and
  `blog-simonwillison-florian-herrengt-middle-class-engineering.md`).
- **Conflicting Prospector triage comments**: The issue carries three separate triage
  comments with differing novelty assessments (high / low / medium) and differing
  relevant-chapter suggestions (Ch02+Ch03 / Ch01+Ch05 / Ch05+Ch00). This extraction
  follows the highest-detail comment's framing (the emotional/professional-arc angle,
  Ch05 relevance) since it most specifically engages with the source's actual content;
  the "low novelty" comment's assessment that the post "lacks concrete patterns, code
  examples, metrics, or failure reports" is accurate as a description of the source's
  evidentiary weight (hence `confidence_overall: anecdotal`), but this note treats the
  psychological-framing angle itself as novel to the corpus per the Cross-References
  section above, rather than treating thin evidence and thin novelty as the same thing.
- **No contradiction issue filed**: The one framing difference identified (this source's
  "radical change was always the norm" vs. Orosz's "destabilizing" framing in
  `blog-pragmaticengineer-orosz-five-years.md`) is a difference in emphasis, not a factual
  disagreement, and does not meet the MINER.md §4a bar.
- **Cross-reference verification**: All claim numbers cited from other source notes were
  verified by re-reading those notes' actual headings before writing this note:
  `blog-kentbeck-jessicakerr-learning-system.md` Claim 1 (line 64) and Claim 2 (line 84);
  `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` Claim 12 (line 268);
  `blog-simonwillison-charity-majors-code-economics.md` Claim 1 (line 47);
  `blog-pragmaticengineer-orosz-five-years.md` Claim 4 (line 114);
  `blog-pragmaticengineer-orosz-kentbeck-career.md` Claim 2 (line 59).
