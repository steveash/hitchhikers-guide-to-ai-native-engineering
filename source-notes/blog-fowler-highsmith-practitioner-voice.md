---
source_url: https://martinfowler.com/articles/practitioner-voice.html
source_type: blog-post
title: "Practitioner Voice: The Writing Category Nobody has Named Yet"
author: Jim Highsmith (Agile Manifesto co-author; published on martinfowler.com)
date_published: 2026-08-19
date_extracted: 2026-08-20
last_checked: 2026-08-20
status: current
confidence_overall: anecdotal
issue: "#2809"
---

# Practitioner Voice: The Writing Category Nobody has Named Yet

> Jim Highsmith proposes "Practitioner Voice" as a named writing category distinct from
> academic writing and thought leadership — authority from experience, tension left
> unresolved, the author's judgment kept visible, and a readership contract built on
> pattern recognition — and argues that its defining, un-automatable property is
> accountability: the willingness to put your name on a call and live with what happens
> next. He names the AI alternative "LLM Voice": fluent, correctly structured, and
> optimized to say nothing wrong, indistinguishable from Practitioner Voice until you
> notice nothing is at stake.

## Source Context

- **Type**: blog-post (martinfowler.com, published under Martin Fowler's "articles"
  section, dated 19 August 2026; single-page essay with an "Acknowledgments" and
  "Significant Revisions" footer, no sub-pages to follow)
- **Author credibility**: Jim Highsmith is a co-author of the Agile Manifesto, author of
  six books (including *Adaptive Software Development*, *Agile Project Management*,
  *Agile Software Development Ecosystems*, and *Wild West to Agile*), and sits on a PMI
  ("Project Management Institute") thought-leadership advisory group. The essay itself
  is framed as a first-person account of feedback he received "three times in my career —
  at Cutter Consortium, at Thoughtworks, and from Martin Fowler reviewing a manuscript" —
  each time being told to "let your voice out." Martin Fowler (co-author of the Agile
  Manifesto, martinfowler.com maintainer for twenty years) is credited within the piece
  as having given Highsmith direct editorial feedback on *Wild West to Agile* and is
  described as writing in the style the essay proposes naming. This is a credentialed,
  named practitioner's first-person reflective essay, not an empirical study — the
  claims are definitional/conceptual, not measured.
- **Scope**: Covers: (1) a personal narrative of being pushed toward a distinct writing
  style across three points in Highsmith's career; (2) a critique of "thought
  leadership" and academic writing as two ways consequential judgment gets edited out of
  prose; (3) a four-part definition of "Practitioner Voice"; (4) the naming of "LLM
  Voice" as a third, AI-native failure mode; (5) the claim that accountability is the
  property that cannot be automated. Does NOT cover: a "how-to" craft guide for writing
  in Practitioner Voice (explicitly deferred — "my next contribution, which I will add
  to this article when it's ready"), quantitative measurement of writing quality, or any
  software-engineering-specific practice.

## Extracted Claims

### Claim 1: Thought leadership and academic writing both degrade practitioner judgment out of the finished text, for different structural reasons
- **Evidence**: Highsmith's own narrative account of thought leadership's evolution
  ("ideas worth following" → "content category" → "marketing function" → "a LinkedIn
  post with a hook, three lessons, and a call to follow for more") and of academic
  writing's convention of citations, caveats, and literature reviews that "buried the
  lead."
- **Confidence**: anecdotal (a named, credentialed practitioner's reflective argument;
  not measured, but internally coherent and specific about mechanism)
- **Quote**: "The problem isn't academic writing or thought leadership individually. At
  their worst, both do the same thing: they edit consequential human judgment out of the
  prose. The practitioner disappears behind the rigor or the polish, and what remains is
  correct but weightless."
- **Our assessment**: The phrase "correct but weightless" is the load-bearing diagnostic
  — Highsmith isn't arguing either mode produces false content, but content stripped of
  the stakes and judgment that would let a reader calibrate how much to trust it. This
  sets up the essay's central move: proposing a third category defined by the presence
  of exactly what the other two remove.

### Claim 2: A third failure mode — "LLM Voice" — has now arrived, and it is more insidious than academic hiding or thought-leadership polish because there is no author present to hide at all
- **Evidence**: Highsmith's own argument, stated as the pivot point of the essay
  ("Now a third option has arrived...").
- **Confidence**: anecdotal (a named practitioner's conceptual coinage; no measurement,
  but a sharp and specific claim)
- **Quote**: "Now a third option has arrived — _LLM Voice_ — that doesn't require hiding
  at all, because there's no one there. That was a problem worth solving before AI
  arrived. Now it's urgent."
- **Our assessment**: This reframes AI-generated writing not as a new problem but as the
  logical endpoint of a pre-existing one (judgment-erasure), which is a more useful frame
  for the guide than "AI content is bad" — it gives a lineage and a mechanism. Highsmith
  later sharpens this further in Claim 6 below: LLM Voice's danger isn't detectability,
  it's that it is *indistinguishable* from the real thing until scrutinized for stakes.

### Claim 3: Practitioner Voice starts with the claim and trusts the reader to close the gap, rather than building up to it (academic) or explaining it (thought leadership)
- **Evidence**: Highsmith's structural comparison of the three writing modes, illustrated
  with Martin Fowler's own writing practice as the worked example.
- **Confidence**: anecdotal (definitional/structural claim, illustrated by one named
  example — Fowler's own articles)
- **Quote**: "Academic writing builds to the claim. Thought leadership makes the claim
  and explains it. Practitioner Voice starts with the claim and trusts the reader to
  close the gap."
- **Our assessment**: This is a specific, falsifiable structural claim (a reader could
  check Fowler's articles against it) rather than a vague style preference. Paired with
  the next quote — "His best pieces don't build to the conclusion, they open with it.
  The rest is a practitioner showing his reasoning, not constructing a case for a jury.
  The reader either recognizes the pattern from their own experience or doesn't. He
  doesn't write for the ones who don't." — it doubles as an implicit statement about
  this guide's own target audience: practitioners who can pattern-match against their
  own experience, not readers who need to be persuaded from first principles.

### Claim 4: Practitioner Voice is defined by four properties: authority from experience (not credentials), tension named but left unresolved, the author staying visibly present, and a readership contract built on pattern recognition rather than universality
- **Evidence**: Highsmith's own four-part enumerated definition, the structural core of
  the essay.
- **Confidence**: anecdotal (a named practitioner's proposed taxonomy; not validated
  against a corpus of writing samples, but each of the four properties is given its own
  specific, quotable justification)
- **Quote**: "Four things separate Practitioner Voice from the alternatives... Authority
  from experience, not credentials... Tension without resolution... The author stays
  in... The readership contract."
- **Our assessment**: Each of the four properties is independently checkable and maps to
  something the guide's own sourcing practice already implicitly does (see Guide Impact
  below): the guide already favors named practitioners with direct experience over
  credentialed-but-unaccountable commentary, and its `confidence_overall` field already
  tracks something like "does this claim's tension get resolved or left live." Highsmith
  gives that existing editorial instinct a name and an argument.

### Claim 5: Practitioner authority, unlike academic or thought-leadership authority, cannot be acquired through credentials — it requires having been personally responsible for an outcome, though consultants earn a weaker but still real version through repeated proximity to consequence
- **Evidence**: Highsmith's own argument, distinguishing direct accountability from
  consultant-style repeated exposure.
- **Confidence**: anecdotal
- **Quote**: "Practitioner authority comes from having been in the situation, not as a
  researcher studying it, but as a person responsible for the outcome. That difference
  shows in every sentence. You can't fake it and you can't credential your way into it.
  For consultants the authority takes a slightly different form. We rarely carry direct
  accountability for outcomes. But if we do our work well, we've been close enough to
  consequence, across enough contexts and enough years, that the pattern recognition is
  real. Earned differently. Still earned."
- **Our assessment**: This is a notably self-aware qualification — Highsmith, writing as
  a consultant/author rather than a hands-on line engineer, explicitly carves out that
  his own authority is "earned differently" from a practitioner who directly shipped and
  owned the outcome. This nuance matters for the guide's own source-evaluation practice:
  it distinguishes "was accountable for the outcome" from "was close to enough outcomes
  to recognize the pattern," both of which the guide's `confidence_overall` field
  currently collapses into a single scale.

### Claim 6: The property that distinguishes Practitioner Voice from AI-mimicked "LLM Voice" is not style, compression, or rhythm — it is accountability, and that specifically cannot be automated
- **Evidence**: Highsmith's own closing argument, the essay's central thesis stated most
  explicitly.
- **Confidence**: anecdotal (a strong, unhedged claim by a named practitioner; not
  empirically tested — no method is proposed in this essay for detecting LLM Voice, only
  for defining what it lacks)
- **Quote**: "AI can mimic the sound of Practitioner Voice. It cannot own the consequences
  behind it. That's the distinction that holds: not style, not compression, not even the
  rhythm of earned judgment. Accountability. The willingness to put your name on a call
  and live with what happens next. That can't be automated."
- **Our assessment**: This is the single most guide-relevant sentence in the source. It
  gives the guide's editorial practice (favoring named, accountable practitioners as
  sources, and flagging anonymous or unaccountable AI-generated claims as lower
  confidence) an explicit, citable rationale rather than an implicit house style. Note
  the claim is asserted, not demonstrated — Highsmith offers no test a reader could apply
  to distinguish accountability-bearing prose from a well-mimicked imitation in practice,
  which is a real limitation (see Guide Impact and Extraction Notes).

### Claim 7: Practitioner Voice is not a new phenomenon created by AI — it has existed unnamed for roughly a decade, and lacking a name prevented it from being taught or recognized deliberately
- **Evidence**: Highsmith's own claim, framed as an observation about the pre-AI writing
  landscape.
- **Confidence**: anecdotal
- **Quote**: "This isn't new behavior. Scroll LinkedIn or Substack and you'll find it:
  practitioners writing from earned judgment, starting with the claim, keeping the
  tension live. It's been building for a decade. Nobody called it anything. Without the
  category, there was no way to teach it, no way to recognize it, no way to say: that's
  the thing, do more of that."
- **Our assessment**: This claim does the work of positioning the essay's contribution as
  naming/taxonomy rather than discovery — Highsmith is explicit that the practice
  predates the essay and predates AI; what's new is only the label and the urgency
  created by LLM Voice's arrival. This is a modest, checkable framing (it doesn't claim
  Practitioner Voice is rare or that Highsmith invented the practice).

### Claim 8: The essay itself was written with AI editing assistance, disclosed in an acknowledgment, with the author retaining sole responsibility for content
- **Evidence**: The article's own "Acknowledgments" section, a factual statement about
  its own production.
- **Confidence**: settled (this is a direct, verifiable statement about the artifact
  itself, not an argued claim)
- **Quote**: "Parts of this essay were edited with assistance from an AI language model
  (Claude Sonnet 4.6). I reviewed and approved the final text and am solely responsible
  for its content."
- **Our assessment**: This is a striking, almost load-bearing detail: an essay arguing
  that accountability (not style) is what separates Practitioner Voice from LLM Voice was
  itself partly AI-edited, and the author's response is exactly the countermeasure the
  essay prescribes — disclosure plus an explicit claim of sole responsibility, not a
  denial of AI involvement. This is a concrete, in-the-wild demonstration of Claim 6's
  argument: the accountability statement, not the absence of AI touch, is what the essay
  claims makes the difference.

## Concrete Artifacts

### The four-part definition of Practitioner Voice (verbatim, "What makes it different" section)

```
Source: Jim Highsmith, https://martinfowler.com/articles/practitioner-voice.html
Published: 19 August 2026

1. Authority from experience, not credentials.
   "Academic authority comes from credentials and methods. Thought leadership
   authority comes from platform and reputation. Practitioner authority comes
   from having been in the situation, not as a researcher studying it, but as
   a person responsible for the outcome... For consultants the authority takes
   a slightly different form. We rarely carry direct accountability for
   outcomes. But if we do our work well, we've been close enough to
   consequence, across enough contexts and enough years, that the pattern
   recognition is real. Earned differently. Still earned."

2. Tension without resolution.
   "Academic writing resolves tension — that's what conclusions are for.
   Thought leadership resolves it in the three takeaways. Practitioner Voice
   names the tension and leaves it live. The practitioner knows the tension
   is real and the reader has to navigate it themselves. Resolving it for
   them would be lying."

3. The author stays in.
   "Academic writing never allows this. Thought leadership allows it only as
   personal brand. In Practitioner Voice the author's judgment is the point.
   Not the data. Not the framework. The accumulated perspective of someone
   making consequential decisions for a long time, with something to say
   about what that's actually like."

4. The readership contract.
   "Academics write for peer reviewers. Thought leadership writes for
   eyeballs. Practitioner Voice writes for people who recognize the pattern
   from their own experience. It's comfortable with limited context — this
   worked here, under these conditions, judge for yourself whether it fits
   yours. It doesn't chase universality. It trusts specificity."
```

### The three-category writing taxonomy (Practitioner Voice / Academic / Thought Leadership / LLM Voice)

```
Source: Jim Highsmith, https://martinfowler.com/articles/practitioner-voice.html

Academic writing:      builds to the claim; resolves tension in conclusions;
                        author absent; writes for peer reviewers; "hides
                        behind rigor"
Thought leadership:    makes the claim and explains it; resolves tension in
                        "three takeaways"; author present only as brand;
                        writes for eyeballs; "hides behind polish"
Practitioner Voice:    starts with the claim; leaves tension live; author's
                        judgment is the point; writes for readers who
                        recognize the pattern from experience
LLM Voice:             "fluent, well-organized, correctly structured,
                        optimized to say nothing wrong" — mimics the sound
                        of Practitioner Voice without the accountability
                        behind it; "the most insidious failure mode of the
                        three because it's indistinguishable from the real
                        thing until you notice nothing is at stake"
```

### Article self-disclosure footer (verbatim)

```
Source: Jim Highsmith, https://martinfowler.com/articles/practitioner-voice.html

## Acknowledgments
Parts of this essay were edited with assistance from an AI language model
(Claude Sonnet 4.6). I reviewed and approved the final text and am solely
responsible for its content.

## Significant Revisions
19 August 2026: published
```

## Cross-References

- **Corroborates**: `blog-simonwillison-tom-macwright-accidental-anonymity.md` Claim 2
  ("LLM-generated application materials create 'accidental anonymity' — the hiring
  manager cannot know anything about the applicant as a person") and Claim 6 ("Authentic
  self-presentation requires bravery... LLM generation allows avoidance of this act at
  the cost of being unknowable"). MacWright's hiring-context observation and Highsmith's
  writing-taxonomy argument independently converge on the same mechanism from different
  domains: MacWright names the *consequence* of removing the human from professional
  materials ("I don't know anything about these people... They haven't said anything
  true"); Highsmith names the *property being removed* (accountability — "the
  willingness to put your name on a call and live with what happens next"). Both frame
  the defining gap as not style or polish but stakes/consequence. This is a strong,
  independent two-author convergence worth citing together.

- **Corroborates**: `blog-ronacher-content-for-contents-sake.md` Claim 4 ("Low-effort
  AI-generated content outperforms quality human content algorithmically, creating an
  unfair arms race") and Claim 9 ("Engagement metrics are the wrong KPI for healthy
  long-term platforms in a world of AI-generated content"). Ronacher documents the
  platform-scale, empirical version of the same phenomenon Highsmith diagnoses at the
  level of a single essay's authorial stance: "thought leadership" degrading into "a
  LinkedIn post with a hook, three lessons, and a call to follow for more" (Highsmith)
  is the individual-writing-style precursor to the content-flooding dynamic Ronacher
  measures at platform scale ("a clanker-made post 3 minutes later"). Ronacher's
  practitioner-side countermeasure (disclose AI assistance when there is ambiguity) is
  the same move Highsmith's own essay makes in its Acknowledgments section (Claim 8
  above) — this is a concrete instance of Ronacher's Claim 8 recommendation
  ("Transparency in either direction, when there is ambiguity, can help great lengths")
  being practiced by Highsmith's own article.

- **Extends**: `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` Claim 7 ("human
  teams need to be accountable for what they deliver" — the structural, not merely
  capability-based, argument for why AI cannot take over the "deliver" layer of
  software engineering work). Narayanan and Kapoor make the accountability argument
  about software delivery; Highsmith makes the structurally identical argument about
  writing and publishing. Both name accountability (not current capability) as the
  durable, non-automatable property. This source extends the corpus's accountability
  argument from code delivery into a second domain (professional writing), strengthening
  the case that "accountability resists automation structurally" is a pattern that
  recurs across at least two independent domains and four independent authors
  (Narayanan, Kapoor, Willison, Highsmith), not a claim specific to software engineering.

- **Novel** (not present in any existing corpus note):
  - **A named, four-part taxonomy of practitioner writing** (authority from experience,
    tension without resolution, author presence, readership contract): No existing
    corpus source proposes a structural definition for what makes practitioner writing
    itself credible, as distinct from claims about AI capability or labor markets. This
    is a meta-source about how to evaluate *any* text-based source, including other
    entries in this corpus.
  - **"LLM Voice" as a named category**, explicitly defined as fluent, structurally
    correct, and "optimized to say nothing wrong" — distinct from "AI slop" (Ronacher's
    framing, which centers on low-effort volume) in that Highsmith's LLM Voice can be
    highly polished and is dangerous *because* of its polish, not despite it.
  - **The "correct but weightless" diagnostic**: a specific, reusable phrase for content
    that contains no factual errors but also carries no accountable judgment — applicable
    to evaluating both external sources and, self-referentially, entries in this guide.
  - **An author explicitly disclosing AI-editing assistance within an essay arguing that
    accountability (not authorial purity) is what matters**: no other corpus source
    combines a theoretical argument about AI/authenticity with a live, verifiable
    self-example of the recommended disclosure practice in the same document.

- **Contradicts**: None found requiring a filed contradiction issue. Every existing
  corpus note this source overlaps with (MacWright/Willison on authenticity, Ronacher on
  content flooding, Narayanan/Kapoor on accountability) is corroborated or extended, not
  contradicted.

## Guide Impact

- **Chapter 00 (Principles — Source Evaluation / Practitioner Authority)**: This is the
  most directly applicable claim for the guide's own editorial practice. Claim 6
  ("accountability... can't be automated") and Claim 4 (the four-part definition) give
  an explicit, citable rationale for why this guide already prioritizes named,
  accountable practitioners over anonymous or AI-generated commentary, and for why
  `confidence_overall: anecdotal/emerging/settled` in every source note's frontmatter is
  doing real epistemic work rather than being a formality. Recommend the guide's
  principles section explicitly name "LLM Voice" (Claim 2) as the failure mode its
  sourcing discipline is designed to filter out, and cite this source alongside
  MacWright/Willison and Ronacher.

- **Chapter 00 (Principles) or a new "How this guide evaluates sources" section**:
  Claim 5's distinction between direct-accountability authority (a practitioner who
  personally owned an outcome) and consultant-style pattern-recognition authority
  (repeated proximity to consequence without direct accountability) is a finer-grained
  model than the guide's current `author_credibility` free-text field appears to use.
  Consider whether source notes should distinguish these two authority types explicitly,
  since the guide's own corpus contains both kinds (e.g., first-person engineers
  reporting their own incidents vs. consultants/analysts synthesizing patterns across
  clients).

- **Chapter 06 (Human-AI Collaboration) or wherever the guide discusses AI-assisted
  writing/communication**: Claim 8 (Highsmith's own AI-editing disclosure) is a concrete,
  reusable example of the disclosure norm Ronacher separately recommends
  (`blog-ronacher-content-for-contents-sake.md` Claim 8). The guide could cite this
  article itself as a worked example: AI-assisted editing is compatible with
  Practitioner Voice as long as the author retains and states sole responsibility for
  content — the presence of AI assistance is not disqualifying; the absence of a
  named, accountable owner is.

- **Limitation to flag wherever this source is cited**: Highsmith proposes no test a
  reader can apply in practice to distinguish well-mimicked LLM Voice from genuine
  Practitioner Voice before consequences arrive — the essay's own framing acknowledges
  this ("indistinguishable from the real thing until you notice nothing is at stake").
  The guide should not present this source as offering a detection method, only a
  vocabulary and a diagnostic principle (accountability, not style) for after-the-fact
  evaluation.

## Extraction Notes

- **Single-page source, fully read**: The article is a self-contained essay with no
  sub-pages; the "Acknowledgments" and "Significant Revisions" footer were read as part
  of the source and yielded a substantive claim (Claim 8). No linked pages needed
  following per MINER.md §1 — the essay does not link out to other substantive articles
  as part of its argument (it references Martin Fowler's site generally and social media
  feeds for future-update notifications, not additional source material).
- **Craft guide not yet published**: The essay explicitly defers its practical "how to
  write in Practitioner Voice" guidance to a future installment ("The craft — a guide to
  writing in Practitioner Voice — is my next contribution, which I will add to this
  article when it's ready"). This source note covers only the definitional/taxonomic
  content that exists as of 2026-08-19; a future source-submission should be filed if
  and when that craft guide is published, since it would likely contain new,
  independently extractable claims (practical writing techniques) not present in this
  version.
- **Confidence rated anecdotal overall**: Every substantive claim in this essay
  (Claims 1–7) is Highsmith's own conceptual/definitional argument, illustrated by
  personal anecdote and one named example (Fowler's writing), not measured or tested
  against a corpus of writing samples. Claim 8 (the AI-disclosure acknowledgment) is
  independently verifiable as a factual statement about the document itself and would
  merit `settled` in isolation, but the overall confidence rating reflects the
  predominant claim type in the source.
- **Cross-reference verification**: All claim numbers cited from other source notes were
  verified by re-reading those notes in this session before citing them:
  - `blog-simonwillison-tom-macwright-accidental-anonymity.md` Claim 2 (lines 67–87) and
    Claim 6 (lines 156–178) — verified.
  - `blog-ronacher-content-for-contents-sake.md` Claim 4 (lines 97–112) and Claim 9
    (lines 183–197) — verified. Claim 8 (lines 168–181), cited in the "Guide Impact"
    section for the disclosure-norm parallel, also verified.
  - `blog-simonwillison-why-ai-hasnt-replaced-engineers.md` Claim 7 (lines 163–185) —
    verified.
- **Triage comments were partially inaccurate**: One of the three duplicate Prospector
  triage comments on the source issue claimed this article "is the foundational
  definition for the concept of 'practitioner voice' that's referenced throughout
  multiple existing source notes (e.g., blog-pragmaticengineer-neetcode-interview.md,
  blog-simonwillison-why-ai-hasnt-replaced-engineers.md)." This was checked directly:
  both notes use the lowercase, generic phrase "practitioner voice" in passing (e.g.,
  "Willison's May 6 post makes the same core argument in his own practitioner voice")
  and neither references Highsmith's essay or its specific four-part taxonomy — the
  phrase is coincidental, not a citation of this article's defined term. No corpus note
  predates or references this essay's specific "Practitioner Voice" / "LLM Voice"
  taxonomy; the cross-references above are independently identified thematic
  convergences, not pre-existing citations of this article.
