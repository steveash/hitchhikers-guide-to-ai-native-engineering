---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/is-ai-governance-the-right-conversation
source_type: blog-post
title: "Is AI governance even the right conversation?"
author: Matt Kamelman
date_published: 2026-06-04
date_extracted: 2026-07-03
last_checked: 2026-07-03
status: current
confidence_overall: anecdotal
issue: "#1462"
---

# Is AI Governance Even the Right Conversation?

> Thoughtworks essay arguing that AI governance debates are calibrated on a
> "category error" — they assume the thing being governed sits still while
> institutions catch up, when recursive self-improving AI development means
> the capability moves faster than any governance framework can form, and
> asks whether the more urgent unanswered question is not "how do we govern
> this" but "what are we building this for and what do we want to become
> alongside it."

## Source Context

- **Type**: blog-post (Thoughtworks Insights, published June 4, 2026; from the
  trusted feed `thoughtworks`. Authored by Matt Kamelman. Opinion/essay format,
  not a case study or empirical report — the piece is structured as a weekly
  news-synthesis argument, weaving together five contemporaneous signals
  (financial markets, enterprise AI spend, an Anthropic co-founder's public
  remarks, a papal encyclical, and Anthropic's self-improvement research team)
  into a single thesis about the inadequacy of current AI governance framing.)
- **Author credibility**: Matt Kamelman writes for Thoughtworks Insights, a
  vendor-neutral technology consultancy already established as a trusted feed
  source in this corpus (see `blog-thoughtworks-gall-supervisory-engineering.md`,
  `blog-thoughtworks-mugrage-claude-outage-infrastructure.md`,
  `blog-thoughtworks-jamieson-flow-game.md`). The article gives no further bio
  for Kamelman beyond the byline — no title or stated governance/policy
  credentials are cited in the piece itself. The article cites no primary
  data of its own; it synthesizes and interprets other people's data points
  (Shiller CAPE ratio, OpenAI's Q1 2026 results, Ramp's AI Index, Chris Olah's
  Vatican remarks, the papal encyclical) rather than presenting original
  research. This is an argumentative/philosophical essay, not a technical or
  empirical source — treat its interpretive claims as one informed
  practitioner's synthesis, not settled fact.
- **Scope**: Covers a macro argument about why AI governance debates may be
  built on a flawed premise (that the object of governance is static). Touches
  financial markets (Shiller CAPE, OpenAI margins, enterprise AI spend),
  public statements by AI lab leadership (Chris Olah, Dario Amodei), the
  Vatican's *Magnifica Humanitas* encyclical, and Anthropic's team using Claude
  to improve Claude (attributed to Andrej Karpathy joining Anthropic). Does
  NOT cover: specific governance mechanisms, technical controls, regulatory
  proposals, or any concrete organizational recommendation. No implementation
  guidance, no metrics of its own, no code or config artifacts — this is a
  think-piece, not a practitioner how-to.

## Extracted Claims

### Claim 1: Current AI governance debates are calibrated on an older category of problem — one where the thing being governed doesn't reshape itself while humans respond to it — and this frame may not fit AI
- **Evidence**: Stated as the article's opening thesis, then argued through the
  rest of the piece via historical analogy (industrialization, nuclear weapons,
  mass media) contrasted with recursive AI self-improvement.
- **Confidence**: anecdotal (single-author interpretive framing; a philosophical
  argument, not an empirical or measurable claim)
- **Quote**: "The debates unfolding around AI — who governs it, which
  institutions respond, how regulation catches up, whose values get encoded —
  are real debates. They're also debates that were calibrated on an older kind
  of problem, where the challenge, however large, reshapes the world around it
  but doesn't reshape itself: where the thing being governed is unchanged while
  humans struggle to catch up with its effects but where the window for change
  remains open."
- **Our assessment**: This is the article's central "category error" claim and
  the thesis everything else supports. It is a reframing argument, not a
  factual claim that can be verified or falsified in the usual sense — it asks
  the reader to accept a historical-analogy comparison (industrialization,
  nuclear weapons, mass media vs. recursively self-improving AI) as the right
  lens. The comparison is provocative but the article does not engage
  seriously with counterarguments (e.g., that governance frameworks have
  historically also evolved iteratively alongside fast-moving technology, or
  that "recursive self-improvement" claims about current AI systems are
  themselves contested). Useful as a counterpoint / framing device for
  discussions of AI governance, but should be presented as one essayist's
  argument, not as an established finding.

### Claim 2: Historical governance responses to civilizational shocks (industrialization, nuclear weapons, mass media) worked because the technology being governed was external to and did not improve itself
- **Evidence**: Historical analogy constructed by the author as the load-bearing
  contrast for Claim 1 — no citations to historians or a formal source, this is
  the author's own historical framing.
- **Confidence**: anecdotal (unsupported historical generalization presented as
  self-evident; no citation to historical scholarship)
- **Quote**: "Humanity has absorbed civilizational shocks before.
  Industrialization, nuclear weapons, mass media — the sequence was
  consistent. Deployment, suffering second, framework, institutional response
  (eventually). It always arrived late; people died in the gap, but it
  arrived. The reason it could arrive is that the thing being governed was
  external to the governing. Locomotives didn't design better locomotives.
  Nuclear weapons didn't improve their own yields."
- **Our assessment**: The "locomotives didn't design better locomotives"
  formulation is a memorable rhetorical device, but it is doing a lot of
  argumentative work without support. The claim conflates several distinct
  historical processes (industrial labor reform, nuclear non-proliferation,
  media regulation) into a single "sequence," and asserts causal sufficiency
  (technology being externally-fixed is *why* governance could eventually
  catch up) without evidence. Treat as rhetorical framing rather than a
  verified historical claim. Its function in the article is to set up the
  contrast with recursive self-improvement in Claim 3.

### Claim 3: AI development at frontier labs now includes teams whose explicit purpose is using the AI to improve the AI itself, which changes AI from a "governed-while-external" technology into a "governed-while-self-modifying" one
- **Evidence**: Author's description of Andrej Karpathy joining Anthropic
  specifically to build "a team that uses Claude to make Claude better,"
  presented without a direct citation or link to a primary source (no
  Anthropic announcement, interview, or Karpathy statement is quoted directly).
- **Confidence**: anecdotal (asserted as fact but the article provides no
  primary-source citation, quote, or link for the Karpathy/Anthropic claim —
  this should be independently verified before use)
- **Quote**: "It is a logical description of what several frontier labs are
  actively building — and what Andrej Karpathy joined Anthropic specifically
  to accelerate: a team that uses Claude to make Claude better."
- **Our assessment**: This is the article's most concrete, checkable factual
  claim, and it is also the one with the thinnest sourcing in the piece
  itself — no link, quote, or date is given for when or why Karpathy joined
  Anthropic or what team he leads. If used in the guide, this claim should be
  corroborated against a primary Anthropic source before being cited as fact;
  as extracted here it is Kamelman's unsourced assertion. The underlying idea
  (AI labs building AI-improves-AI research capability) is directionally
  consistent with publicly discussed frontier-lab research priorities, but the
  specific Karpathy attribution is unverified within this source.

### Claim 4: Elevated equity valuations (Shiller CAPE ratio crossing 40, a level reached only once before in 140 years) reflect capital pricing AI transformation as fast, large, and broadly distributed — a bet not yet borne out by underlying profitability
- **Evidence**: Cited market data point (Shiller CAPE ratio) combined with
  OpenAI's reported Q1 2026 financials and Ramp's AI Index adoption figures,
  presented as a composite argument rather than sourced individually with
  links.
- **Confidence**: anecdotal (specific numbers are cited — CAPE > 40, OpenAI
  losing "$1.22 for every dollar it earned in Q1 2026," "50%" enterprise
  adoption crossing this month — but none carry direct source links or
  citations within the article; treat as reported figures requiring
  independent verification, not primary data)
- **Quote**: "The S&P 500's Shiller CAPE ratio crossed 40 this week — a level
  reached only once before in 140 years of data, in 1999. What the number
  reveals isn't primarily crash risk, but instead the structure of the bet:
  capital is pricing AI transformation as if the economic benefits are large,
  fast, and broadly distributed. This is all while OpenAI — the company most
  directly positioned to capture that value — lost $1.22 for every dollar it
  earned in Q1 2026."
- **Our assessment**: This is a genuinely interesting economic observation —
  the disconnect between market valuation (pricing in fast, broad AI economic
  benefit) and the reported unit economics of the leading AI lab (losing more
  than a dollar for every dollar earned) is a real tension worth noting. But
  the article states these figures without citation, so they should be
  treated as claims to verify, not settled numbers, before use in the guide.
  If corroborated, this is a useful data point for any chapter discussing the
  economics of AI transformation and the gap between investment narrative and
  operational reality — a complement to `blog-simonwillison-anthropic-run-rate.md`
  and `blog-simonwillison-anthropic-47b-revenue.md` on Anthropic's own
  financials (not directly overlapping, since this article's data point is
  about OpenAI and the broader market, not Anthropic).

### Claim 5: AI deployment decisions — pace, systems, constraints — are being made by a small group of people operating inside incentive structures that cannot fully assess the consequences for everyone else
- **Evidence**: Author's structural argument, corroborated within the article
  by a paraphrased/summarized account of remarks Chris Olah (Anthropic
  co-founder) reportedly made standing beside Pope Leo XIV at the Vatican.
- **Confidence**: anecdotal (structural claim asserted by the author; the
  supporting anecdote about Olah's remarks is reported without a direct quote
  or link to the original source of those remarks)
- **Quote**: "the decisions about how AI gets deployed, at what pace, into
  which systems, with what constraints, are being made by the smallest
  possible group of people, inside incentive structures that cannot fully
  assess the consequences of those decisions for everyone else."
- **Our assessment**: This "concentrated decision-making" framing is a common
  critique in AI policy discourse, but the article treats it as self-evident
  rather than substantiating it with data (e.g., how many people, at how many
  labs, actually set deployment pace). The corroborating anecdote — Olah
  saying frontier labs operate inside incentives that can conflict with doing
  the right thing, and that outside critics are "enormously important" — is
  paraphrased rather than directly quoted in the article, and no link or date
  is given for the Vatican appearance. Useful as an illustration of an
  insider acknowledging the concentration-of-power critique, but the specific
  Olah remarks should be verified against a primary source before citing them
  as a direct quote in the guide.

### Claim 6: Anthropic co-founder Dario Amodei has said publicly that he is uncomfortable with AI deployment decisions being made by a small number of companies and people
- **Evidence**: Author's reference to a CBS appearance by Amodei, dated "last
  November" relative to the article's June 2026 publication (implying
  November 2025), reported without a direct quote or link.
- **Confidence**: anecdotal (paraphrased attribution without a direct quote or
  citation link; independently plausible given Amodei's publicly stated views
  on AI safety and industry concentration, but not independently verified
  within this source)
- **Quote**: "(no direct quote; see paraphrase in Our assessment)" — the
  article states: "Dario Amodei said on CBS last November that he is deeply
  uncomfortable with these decisions being made by a few companies and,
  indeed, a few people."
- **Our assessment**: This is a paraphrase, not a verbatim quote, and the
  article gives no link to the CBS segment. The underlying sentiment is
  consistent with Amodei's publicly documented concerns about AI safety and
  the concentration of frontier AI development among a handful of companies,
  but this specific attributed statement should be independently verified
  before being cited as a direct Amodei quote in the guide.

### Claim 7: Pope Leo XIV's encyclical *Magnifica Humanitas* was signed on May 15, 2026 — the 135th anniversary of *Rerum Novarum*, the document his namesake (Leo XIII) wrote in response to industrialization — and the date choice may signal urgency that the moral-framework response window for AI is much shorter than it was for industrialization
- **Evidence**: Author's dating and interpretation of the encyclical's
  signing date relative to *Rerum Novarum*'s anniversary; presented as the
  author's own inference about intent ("The date may not have been a
  coincidence").
- **Confidence**: anecdotal (the anniversary date is a checkable fact; the
  interpretation of intent behind the date choice is explicitly speculative,
  flagged by the author's own hedging language "may not have been a
  coincidence" and "may suggest")
- **Quote**: "Pope Leo XIV published Magnifica Humanitas on May 25, but was
  signed on the 15th, the 135th anniversary of Rerum Novarum, the document his
  namesake wrote in response to industrialization... The choice of date may
  suggest the current Pope is saying that sequence cannot run again. The
  window for the moral framework to arrive before the damage accumulates
  isn't 35 years; it may not even be 35 months."
- **Our assessment**: This directly extends `blog-simonwillison-encyclical-on-ai.md`,
  the corpus's existing note on the same encyclical. That note extracts eight
  substantive sections (§83, §98, §100–102, §105, §108, §213) on
  interpretability, cultural bias, environmental cost, accountability, power
  concentration, and data governance, but does not discuss the significance
  of the encyclical's signing date or its relationship to *Rerum Novarum*.
  This is a genuinely novel framing not present in the existing encyclical
  note — the "35 years vs. 35 months" compressed-timeline argument is a
  distinct interpretive contribution. It should be flagged as the author's
  own speculative reading of the date's significance, not a claim the
  encyclical itself makes explicitly (the article does not quote the
  encyclical stating this timeline compression).

### Claim 8: The AI governance conversation currently proceeds as if the systems being deployed remain "tools" that humans direct toward pre-defined ends, without seriously asking what happens if that assumption is false
- **Evidence**: Author's central philosophical argument in the article's back
  half, framed as the "not being asked" question underlying the governance
  debate.
- **Confidence**: anecdotal (philosophical/interpretive claim, not an
  empirical one)
- **Quote**: "These are real questions. But they share an assumption that is
  worth examining: that the thing being built remains, in some meaningful
  sense, a tool. Powerful, fast, consequential — but a tool. Something humans
  deploy toward ends they have already defined. What's not being asked is
  what happens if that assumption is wrong."
- **Our assessment**: This is the article's most philosophically substantive
  claim and its clearest link to Ch00-level foundational discussions in the
  guide. It reframes governance debates (who's in the room, which values,
  faster institutions) as downstream of an unexamined premise (that AI is
  instrumentally a tool). This connects to but goes further than
  `blog-simonwillison-encyclical-on-ai.md` Claim 1 (the "cultivated not built"
  interpretability framing) — where the encyclical note focuses on the
  technical opacity of how AI systems are trained, this article's claim is
  about the philosophical status of what is being built (tool vs. something
  else) and what that implies for governance framing. Both point toward the
  same underlying discomfort (AI may not fit familiar categories) from
  different angles (technical opacity vs. purpose/agency).

### Claim 9: Technical alignment is necessary but not sufficient — the harder unresolved question is "alignment to what, decided by whom, toward which definition of what humanity is and wants"
- **Evidence**: Author's direct argumentative claim, presented as the
  article's synthesis of the alignment-vs-governance distinction.
- **Confidence**: anecdotal (philosophical claim; a distinction that is
  intuitively meaningful but not empirically testable)
- **Quote**: "Technical alignment is a necessary condition. It is not a
  sufficient one. Alignment to what, decided by whom, toward which definition
  of what humanity is and wants — that is the question the current
  conversation keeps approaching and stepping back from."
- **Our assessment**: This is a useful conceptual distinction for any guide
  section that discusses AI alignment or safety: technical alignment
  (does the system do what it's told) is separable from and does not resolve
  normative alignment (who decides what it should be told to want). The
  article's claim that current discourse "keeps approaching and stepping back
  from" this question is an assertion about the state of public discourse
  that isn't substantiated with examples of specific governance proposals
  that avoid the question — it's presented as the author's read of the field,
  not demonstrated case by case.

### Claim 10: The article closes by naming the unasked question directly — whether we are building a form of intelligence capable of outperforming humans in every domain, and what that means for humanity's purpose, not just how to govern its deployment
- **Evidence**: The article's closing paragraphs, stated as the direct
  restatement of the thesis after the historical, financial, and
  institutional evidence has been presented.
- **Confidence**: anecdotal (restatement of Claim 1/8's thesis; rhetorical
  closing, not new evidence)
- **Quote**: "That question is not yet being asked seriously enough to produce
  an answer. And it needs to be named plainly: we may be building a form of
  intelligence capable of outperforming us in every domain, and we have not
  yet seriously asked what that means for humanity — not how to govern it,
  but what we want to become alongside it, and whether we have thought
  carefully enough about why we are building it at all."
- **Our assessment**: This is the article's rhetorical conclusion rather than
  a new claim — it restates Claim 1 and Claim 8 in more direct language. Its
  guide value is as a citable framing statement (useful for chapter epigraphs
  or introductions to governance/ethics sections) rather than as evidence of
  anything specific. Treat as a strong, quotable articulation of an
  unresolved question in the AI governance discourse, not as a finding.

## Concrete Artifacts

### The article's five converging "signals" (as structured by the author)

```
Is AI Governance Even the Right Conversation? — Matt Kamelman, Thoughtworks, June 4, 2026

1. FINANCIAL: Shiller CAPE ratio > 40 (only prior instance: 1999) while
   OpenAI lost $1.22 per $1 earned in Q1 2026; Ramp's AI Index shows >50%
   enterprise adoption this month; Uber has "already blown its 2026 AI budget."

2. ENTERPRISE OPERATIONS: fastest-growing vendors on enterprise spend
   platforms are inference providers offering cheap open-source model access.

3. FRONTIER LAB LEADERSHIP: Chris Olah (Anthropic co-founder), speaking
   beside Pope Leo XIV at the Vatican, said every frontier AI lab operates
   inside incentives that can conflict with doing the right thing, and that
   outside earnest critics are "enormously important." Dario Amodei
   (reported, CBS, November 2025) said he is "deeply uncomfortable" with
   deployment decisions resting with "a few companies and, indeed, a few
   people."

4. VATICAN: Magnifica Humanitas, signed May 15, 2026 — the 135th anniversary
   of Rerum Novarum (Leo XIII's 1891 response to industrialization).

5. RECURSIVE CAPABILITY: Andrej Karpathy joined Anthropic to build "a team
   that uses Claude to make Claude better" (unsourced within the article).

Thesis: these five signals point to the same underlying condition — AI
governance debates assume the object of governance holds still while
institutions respond, but recursive self-improvement means the capability
does not wait for the governance conversation to catch up.
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-simonwillison-encyclical-on-ai.md` and
`blog-thoughtworks-gall-supervisory-engineering.md` were re-read directly
(MINER.md §4b) and claim numbers below were confirmed against those notes'
numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-simonwillison-encyclical-on-ai.md` Claim 6 ("responsibility must be
    clearly defined at every stage: from those who design and develop these
    systems to those who use them and rely on them for concrete decisions" —
    the encyclical's §105 distributed accountability framing): This article's
    Claim 5 (deployment decisions concentrated among "the smallest possible
    group of people") describes the same power-concentration problem the
    encyclical's distributed-accountability framing is a response to — both
    sources treat concentrated, unaccountable decision-making as the
    structural problem AI governance must solve.
  - `blog-simonwillison-encyclical-on-ai.md` Claim 7 ("AI tends to amplify the
    power of those who already possess economic resources, expertise and
    access to data" — encyclical §108): Directly corroborates this article's
    Claim 5 and the broader "smallest possible group of people" framing —
    two independent sources (the Vatican encyclical and this Thoughtworks
    essay) converge on concentrated power as a central AI governance concern.

- **Contradicts**: None identified. This source does not make claims that
  materially oppose any existing corpus note. No contradiction issue filed.

- **Extends**:
  - `blog-simonwillison-encyclical-on-ai.md`: That note extracts the
    encyclical's substantive ethical content (interpretability, bias,
    environment, accountability, power, data governance) but does not discuss
    the significance of the encyclical's signing date. This article's Claim 7
    (the *Rerum Novarum* anniversary date and the "35 years vs. 35 months"
    compressed-timeline argument) is a novel interpretive layer on the same
    primary document — a reading of *when* the encyclical was signed, not
    *what* it says. Guide sections citing the encyclical should treat these
    two notes as complementary: the Willison note for section-by-section
    content, this note for the dating argument and the broader "is governance
    even the right frame" critique.
  - `blog-thoughtworks-gall-supervisory-engineering.md`: Both are Thoughtworks
    Insights essays from the same trusted feed, addressing different scales
    of the same underlying shift (AI systems changing faster than human
    processes can adapt to them). Gall's piece addresses this at the
    engineering-workflow level (the "middle loop" requiring supervisory
    engineering because agents move faster than traditional review
    processes); Kamelman's piece addresses the same underlying dynamic at
    the civilizational/governance level (institutions cannot govern
    something that improves itself faster than governance frameworks can
    form). Both essays share an implicit thesis: human oversight processes
    calibrated for a slower-moving object no longer fit an object that
    changes faster than the process can adapt.

- **Novel**:
  - **"Category error" framing of AI governance debates**: No prior corpus
    source explicitly argues that AI governance debates are miscalibrated
    because they assume a static object of governance. This is a distinct
    contribution — a critique of the *framing* of governance discourse, not
    a governance pattern or technical control (contrast with
    `blog-jetbrains-agentic-ai-governance.md`, which provides concrete
    governance patterns without questioning whether "governance" is the
    right frame at all).
  - **Recursive self-improvement as the reason historical governance analogies
    break down**: The "locomotives didn't design better locomotives" argument
    (Claim 2/3) — that prior technologies were externally fixed while AI
    modifies itself — is a novel argument in the corpus for why AI governance
    may need fundamentally different institutional responses than
    industrialization, nuclear weapons, or mass media required.
  - **Market valuation vs. reported unit economics as a governance-relevant
    tension**: The Shiller CAPE ratio / OpenAI Q1 2026 loss juxtaposition
    (Claim 4) is a novel economic framing not present elsewhere in the
    corpus — it uses financial market data as evidence for a governance
    argument (the gap between what capital is pricing and what
    organizations are experiencing), rather than as a standalone economics
    claim.
  - **"Alignment to what, decided by whom" as a distinct question from
    technical alignment** (Claim 9): While the corpus discusses technical
    alignment and safety extensively, this is the first source to explicitly
    separate "does the system do what it's told" from "who decides what it
    should be told to want" as two different unresolved problems.

## Guide Impact

- **Chapter 00 (Principles/Fundamentals)**: The article's central reframing —
  that governance debates assume AI is a fixed "tool" and that this
  assumption itself deserves scrutiny (Claim 8) — is a useful counterpoint
  for any foundational discussion of what AI-native engineering practices are
  ultimately in service of. Recommend citing as an example of a credible
  practitioner voice questioning the default frame, to be presented alongside
  (not replacing) the guide's existing operational governance content. This
  is philosophical framing, not actionable guidance — flag it as such if
  incorporated.

- **Chapter 05 (Team Adoption)**: Claim 5 and Claim 6 (deployment decisions
  concentrated among a small group operating inside conflicted incentives)
  are relevant context for any section discussing why organizations should
  build internal governance capacity rather than relying solely on vendor
  assurances — reinforces, from an industry-critique angle, the same
  incremental-autonomy and accountability arguments already sourced from
  `blog-jetbrains-agentic-ai-governance.md`.

- **Chapter 06 (Security/Threat Model)**: Limited direct applicability — this
  source is philosophical/argumentative rather than technical. If Chapter 06
  discusses the *limits* of governance frameworks (e.g., why technical
  controls alone are insufficient), Claim 9 ("alignment to what, decided by
  whom") is a useful framing for explaining why access controls and audit
  trails (already well-covered via `blog-anthropic-zero-trust-ai-agents.md`
  and `blog-jetbrains-agentic-ai-governance.md`) address the "how" of
  governance but not the deeper "toward what end" question this article
  raises.

- **Any chapter citing `blog-simonwillison-encyclical-on-ai.md`**: Add Claim 7
  (the *Rerum Novarum* anniversary and the compressed-timeline argument) as a
  complementary interpretive note when referencing the encyclical — it adds
  context about the deliberateness and urgency the Vatican may have intended,
  beyond the encyclical's textual content already extracted in the existing
  note.

## Extraction Notes

1. **Source fetched via WebFetch with a verbatim-text-return prompt**: A single
   fetch using an explicit "return the FULL text verbatim, do not summarize"
   prompt returned what appears to be the complete article (author byline,
   publish date, all body paragraphs, section headings, and the closing
   disclaimer). The returned text reads as internally consistent prose with
   no obvious summarization artifacts (no bullet-point compression, no
   truncation mid-sentence), and the closing "Disclaimer" boilerplate matches
   the standard Thoughtworks Insights article footer, which is a signal the
   full page was rendered. As with all WebFetch-sourced notes in this corpus,
   quotes should be spot-checked against the live URL by the Assayer before
   being cited verbatim in the guide.

2. **Article is an opinion/synthesis essay, not a reported or empirical
   source**: Nearly every specific factual claim in the article (the Karpathy
   attribution, the Olah Vatican remarks, the Amodei CBS quote, the OpenAI
   Q1 2026 loss figure) is stated without a citation link within the article
   itself. This note's confidence ratings reflect that: all claims are rated
   "anecdotal" because the article functions as a single author's synthesis
   and interpretation of other people's data points and statements, not as a
   primary report of original research or first-party data. The overall
   source confidence is rated "anecdotal" for the same reason — this is a
   think-piece drawing on unlinked secondary reports, not a source
   establishing new facts.

3. **The Karpathy/Anthropic claim (Claim 3) and the Amodei CBS claim (Claim 6)
   in particular should be independently verified** before being cited in the
   guide as factual — the article provides no link, date beyond "last
   November," or direct quote for either.

4. **No sub-pages followed**: The article is self-contained prose with no
   inline links to the underlying sources it references (the CBS interview,
   the Vatican appearance, the Ramp AI Index, the OpenAI financials). Per
   MINER.md guidance to follow up to 5 substantive linked pages, none were
   followed because the fetched article text contained no linked URLs to
   follow — this appears to be a limitation of the WebFetch markdown
   conversion (links may have been stripped) rather than the article having
   no sources. The Assayer or a future miner revisiting this source with
   direct HTML access may find inline links worth following.

5. **No contradictions filed**: Cross-referenced against
   `blog-simonwillison-encyclical-on-ai.md` (the only existing note discussing
   the same encyclical) and `blog-jetbrains-agentic-ai-governance.md` (the
   only existing note on AI governance patterns generally) — found no
   material contradictions. This article's critique targets the *framing* of
   governance conversations, not any specific governance pattern the
   JetBrains note recommends; the two are complementary rather than opposed.
