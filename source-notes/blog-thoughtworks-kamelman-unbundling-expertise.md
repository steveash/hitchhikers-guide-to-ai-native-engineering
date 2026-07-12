---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/unbundling-expertise
source_type: blog-post
title: "Is AI unbundling expertise?"
author: Matt Kamelman
date_published: 2026-06-19
date_extracted: 2026-07-12
last_checked: 2026-07-12
status: current
confidence_overall: emerging
issue: "#1777"
---

# Is AI Unbundling Expertise?

> Thoughtworks essay arguing that expertise has always bundled three separable
> functions — knowing, reasoning, and transmitting — and that an Anthropic
> study of ~400,000 Claude Code sessions shows the bundle coming apart:
> success with AI correlates with the ability to externalize a coherent
> mental model (transmissibility), not with domain knowledge itself, which
> means organizations that reward execution over explicability may be
> underinvesting in the capability AI actually rewards.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, published June 19, 2026;
  subtitle "Articulating and transmitting knowledge in an AI era"; from the
  trusted feed `thoughtworks`). The piece has no H2/H3 section markup in the
  rendered page's semantic headings beyond the four in-body section titles
  ("Externalizing mental models", "The transmission of knowledge",
  "Pre-structuring context", "Can we cultivate the ability to transmit?"),
  bookended by an unheaded intro and closing paragraph.
- **Author credibility**: Matt Kamelman, "Innovation Choreographer,
  Thoughtworks" (byline given in the article's pull-quote attribution). He is
  already a corpus source via `blog-thoughtworks-kamelman-ai-governance-category-error.md`
  (published 2026-06-04, two weeks before this piece) and
  `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`. No further
  bio, credentials, or track record in organizational psychology, labor
  economics, or AI research is given in this piece itself — Kamelman's basis
  for the central claim is interpretation of a third-party study (Anthropic's),
  not original research or data he collected. The article also references his
  own earlier post ("a piece about teaching AI to skip stones", linked to
  `https://www.thoughtworks.com/insights/blog/generative-ai/why-context-engineering-is-like-teaching-AI-to-skip-stones`,
  published 2025-10-15) as prior work he is extending.
- **Scope**: Covers a conceptual reframing of what "expertise" is composed of
  and how AI-assisted work performance data (from an Anthropic study) can be
  reinterpreted as evidence for that reframing. Does NOT cover: the Anthropic
  study's actual methodology, sample composition, or statistical detail
  beyond the session count (400,000) — the study itself is linked
  ("a study" is a hyperlink in the source HTML) but its content is not quoted
  or summarized beyond what Kamelman characterizes it as showing. Does NOT
  give any concrete organizational recommendations, tools, or measurement
  approach for how to "cultivate transmissibility" — the piece ends on an
  open question, not a prescription. No code, config, or metrics artifacts
  beyond the "400,000" session count are present.

## Extracted Claims

### Claim 1: Expertise has historically bundled three distinct functions — knowing, reasoning, and transmitting — into a single person, because no tool could perform any of them independently
- **Evidence**: Author's structural framework, stated as a three-item list.
- **Confidence**: emerging (a novel decomposition/naming claim, not empirically tested, but internally coherent and the load-bearing premise for the rest of the article)
- **Quote**: "For most of human history, expertise bundled three distinct functions in a single person: You had to know something — accumulating domain knowledge through experience, training and pattern recognition. You had to reason through problems — applying that knowledge to produce judgments, plans and solutions. You had to transmit your model — making your understanding legible to other minds well enough to coordinate with them, teach them or direct their work."
- **Our assessment**: This is the article's central taxonomy and its main contribution to our corpus — no existing source note names a three-way split of "expertise" into know/reason/transmit. It is a framing claim (vocabulary), not a measured one; its value is as a decomposition tool, similar in kind to (but distinct in content from) the Triple Debt Model in `blog-addyosmani-intent-debt.md` Claim 1 (technical/cognitive/intent debt) — see Cross-References.

### Claim 2: An Anthropic study of ~400,000 Claude Code sessions rated "expertise" not by measuring knowledge depth or credentials, but by measuring precision of instruction, verification behavior, error detection, and the ability to redirect the agent when it had misunderstood
- **Evidence**: Author's characterization of the study's measurement approach; the study itself is hyperlinked in the source but not quoted directly, and no author, publisher, or exact title of the Anthropic study is given in this article's text.
- **Confidence**: anecdotal (this is Kamelman's secondhand characterization of what the study measured, not a direct quote from the study itself; independently verifying what the Anthropic study actually measured would require reading it directly, which was outside the scope of this extraction — the link target was not part of the triaged source)
- **Quote**: "When they rated \"expertise\" across 400,000 sessions, the researchers weren't measuring knowledge depth or professional credentials, but were instead measuring precision of instruction, verification behavior, error detection and the ability to redirect the agent when it had misunderstood."
- **Our assessment**: This is the empirical anchor for the rest of the article's argument, but it is one step removed from the primary source — a future miner or the Assayer should consider mining the underlying Anthropic study directly if it hasn't already been triaged, since this article's entire thesis rests on that study's methodology being accurately characterized here.

### Claim 3: Success in AI-assisted work is primarily a measure of a person's capacity to externalize a coherent internal model so another intelligence can act on it rather than approximate it
- **Evidence**: Author's direct interpretive claim, following from Claim 2.
- **Confidence**: emerging
- **Quote**: "These are primarily measures of a person's capacity to externalize a coherent internal model — to make the structure of their understanding available to another intelligence, so that intelligence can act on it rather than approximate it."
- **Our assessment**: This is the article's core reframing: expertise is not the predictor, externalization capacity is. It directly parallels the mechanism named in `blog-addyosmani-intent-debt.md` Claim 2 — that an agent given insufficient externalized rationale will "infer and approximate" (Kamelman's words) or "invent a confident-sounding reason" (Osmani's words) rather than act correctly. Both sources independently converge on the same failure mode (agent fills gaps left by unexternalized human understanding) from different angles.

### Claim 4: A domain novice (an accountant with no coding background) can outperform a junior developer at directing an AI coding agent because she can transmit a precise model of the problem, not because she has more domain knowledge
- **Evidence**: Author's illustrative example, not a documented case study or named individual.
- **Confidence**: anecdotal (an illustrative example constructed by the author, not a reported or verified case)
- **Quote**: "The accountant with no coding background who knows exactly which reconciliation rules the script must enforce — and catches the edge case at month-end close — succeeds not because she possesses more domain knowledge than the junior developer, but because she can transmit a precise model of what the problem actually is."
- **Our assessment**: Illustrative, not evidentiary — no data ties this specific scenario to the Anthropic study's actual findings. Treat as a plausible narrative gloss on Claim 2/3, not as independent proof. Useful as a concrete, quotable example if the guide wants to illustrate the abstract "transmissibility" concept.

### Claim 5: The capacity to transmit a coherent model to another mind has always existed as a professional skill (teaching, consulting, filmmaking, public speaking, tribal-elder-style community coordination), but was never priced separately from knowledge because the two were always bundled in the same person
- **Evidence**: Author's historical/analogical argument, including the tribal-elder analogy as an extended illustration.
- **Confidence**: anecdotal (historical generalization and analogy, not sourced to any historical or anthropological scholarship)
- **Quote**: "It's what the tribal elder who maintained collective coherence across generations was actually exercising: not superior knowledge of hunting technique, but the highest-bandwidth transmission of the community's operating model — its history, norms, exceptions, relationships and causal chains. Those roles were never primarily defined by possessing knowledge; they were defined by making knowledge transmissible. The bundled nature of expertise meant we never needed to price this capacity separately."
- **Our assessment**: This is a rhetorical/historical analogy, not a verifiable claim — similar in kind to the unsupported historical generalizations flagged in `blog-thoughtworks-kamelman-ai-governance-category-error.md` Claim 2 ("locomotives didn't design better locomotives"), which is the same author using the same rhetorical move (a compressed historical analogy asserted as self-evident, without citation to supporting scholarship) in a different essay. Should be cited as illustrative framing, not as historical fact.

### Claim 6: Expertise is not the multiplier for AI-assisted work outcomes — transmissibility is; experts who have never had to make their reasoning explicit may find AI tools disappointing, and the resulting gap shows up as a productivity ceiling rather than a knowledge deficit
- **Evidence**: Author's direct argumentative claim, extending Claim 3.
- **Confidence**: emerging
- **Quote**: "Expertise helps because deep familiarity with a domain usually produces better internal models. But expertise isn't the multiplier; transmissibility is. The expert who has never been asked to make their reasoning explicit, who has accumulated knowledge through experience but not through articulation, may find the tool unexpectedly disappointing. The gap between what they know and what they can make usable will not show up as a knowledge deficit. It will show up as a productivity ceiling."
- **Our assessment**: This is a specific, falsifiable-sounding prediction (experts with high tacit-but-inarticulate knowledge underperform with AI tools) that would benefit from independent verification against practitioner reports in the corpus. It corroborates the general direction of `blog-thoughtworks-gall-supervisory-engineering.md` Claim 11 (the industry now values "strong mental models of system architecture" and "an intuitive grasp of real-world software behavior" over syntax mastery) — both sources converge on articulated/legible mental models mattering more than raw accumulated knowledge, though Gall's piece frames this as favoring experienced engineers specifically, while Kamelman's piece frames it as orthogonal to seniority (a novice who can articulate beats an expert who can't).

### Claim 7: Organizations that have systematically rewarded execution over explicability may find they have underinvested in the layer AI actually rewards
- **Evidence**: Author's direct claim, presented in the article both in-line and as a styled pull-quote (see Extraction Notes on duplication).
- **Confidence**: anecdotal (a values/prediction claim about organizational behavior, not measured against any named organization's outcomes)
- **Quote**: "An organization that has systematically rewarded execution over explicability, where people have been valued for producing outputs rather than for making their reasoning legible, may find it has underinvested in the layer AI actually rewards."
- **Our assessment**: This is the article's clearest organizational-stakes claim and the one most directly actionable for a guide chapter on team adoption — but it is asserted, not demonstrated with a named organization's before/after experience. Should be cited as a hypothesis worth testing against a team's own hiring/promotion criteria, not as an established finding.

### Claim 8: The gap between what people know and what they can transmit has always existed, but it never had a direct economic cost attached to it until AI-assisted work made transmission legible and consequential
- **Evidence**: Author's closing claim of the "Pre-structuring context" section.
- **Confidence**: anecdotal (economic claim asserted without measurement of "cost")
- **Quote**: "The bottleneck in those organizations will be the gap between what people know and what they can transmit. That gap has always existed. It has never, until now, had a direct economic cost attached to it."
- **Our assessment**: This restates Claim 7 in economic terms. Notably, this is nearly the identical structural argument Osmani makes about intent debt in `blog-addyosmani-intent-debt.md` Claim 5 ("Un-externalized intent used to cost you once in a while, at onboarding or after someone left. Now you pay it every session, multiplied by every agent you run") — both authors independently argue that AI adoption converts a previously-latent, unpriced organizational gap (unexternalized knowledge/intent) into a recurring, directly-priced cost. This is a strong corroboration across two independent authors and publications within the same ~2-week window (Osmani: 2026-06-05; Kamelman: 2026-06-19).

### Claim 9: The ability to pre-structure context into a form another intelligence can act on is separable from expertise itself — it is "its own thing," distinct from the domain knowledge it is often bundled with
- **Evidence**: Author's own reflection on his earlier piece ("teaching AI to skip stones", 2025-10-15), explicitly revising/sharpening that earlier argument.
- **Confidence**: emerging
- **Quote**: "What I didn't name clearly enough then is that this capacity — the ability to pre-structure context into a form another intelligence can act on — is separable from expertise itself. It is its own thing."
- **Our assessment**: Read against the earlier "skip stones" piece (fetched for context during this extraction; not itself triaged or source-noted in this corpus), that 2025 article argued for context engineering as a technical/architectural discipline (chunking, vector search, knowledge graphs, RAG, for BFSI compliance use cases) — a systems-level concern. This article reframes the same underlying idea at the level of individual human capability rather than system architecture: not "how do we architect context pipelines" but "who among us can construct good context in the first place." This is a genuine shift in framing across the same author's two pieces, worth noting if the guide cites both.

### Claim 10: Transmissibility can potentially be cultivated deliberately — teaching, writing, scientific training, and leadership are cited as developmental experiences that produce it
- **Evidence**: Author's assertion, no supporting research or citation for why these four specific activities produce transmissibility.
- **Confidence**: anecdotal (asserted without evidence; the author raises this as an open question rather than a settled claim)
- **Quote**: "Teaching produces it. Writing produces it. Scientific training, which requires making reasoning independently reproducible, produces it. Leadership, at its best, produces it."
- **Our assessment**: This is speculative and unsupported — no study or citation backs the claim that these four activities specifically build "transmissibility" as opposed to correlating with people who already had it. Should be flagged as an open, unverified hypothesis if used in the guide, not as an established developmental pathway.

### Claim 11: AI may be the first technology in history that makes transmission quality directly observable
- **Evidence**: Author's closing argument of the "Can we cultivate the ability to transmit?" section.
- **Confidence**: anecdotal (a sweeping historical claim — "first technology in history" — asserted without comparison to other candidate technologies, e.g., writing itself, the printing press, or standardized testing, that might also have made aspects of transmission quality observable)
- **Quote**: "AI may be the first technology in history that makes transmission quality directly observable."
- **Our assessment**: This is a strong claim that the article does not defend against obvious counterexamples (e.g., written exams, teaching evaluations, or peer review already made some aspects of transmission quality observable before AI). Treat as rhetorical emphasis rather than a defensible historical claim.

### Claim 12: Expertise isn't disappearing, but it may be getting "repriced" — and the components that get priced separately may not be the ones most organizations have been investing in
- **Evidence**: Author's closing thesis statement, synthesizing the whole article.
- **Confidence**: emerging (this is the article's summary framing claim rather than new evidence, but it accurately compresses the argument built across Claims 1-11)
- **Quote**: "Expertise isn't disappearing, but it may be getting repriced. And the components that get priced separately may not be the ones most organizations have been investing in."
- **Our assessment**: This is the single most citable sentence in the piece for a guide section on how AI reshapes what organizations should value and hire for — a compact restatement of the whole thesis, useful as a section epigraph.

## Concrete Artifacts

```
Source: Matt Kamelman, "Is AI unbundling expertise?", Thoughtworks Insights,
published June 19, 2026. Subtitle: "Articulating and transmitting knowledge
in an AI era."

The three-function bundle (Claim 1), as listed in the source:
  1. Know something    — accumulate domain knowledge (experience, training,
                          pattern recognition)
  2. Reason through it — apply knowledge to produce judgments, plans,
                          solutions
  3. Transmit the model — make understanding legible to other minds well
                           enough to coordinate, teach, or direct their work

In-article section headings (in order, no numbered H2/H3 markup in source,
these are the article's own bolded section titles):
  (unheaded intro)
  Externalizing mental models
  The transmission of knowledge
  Pre-structuring context
  Can we cultivate the ability to transmit?
  (unheaded closing paragraph)

Referenced (not quoted in depth) external study:
  Anthropic study, ~400,000 Claude Code sessions, hyperlinked in source as
  "a study" — not independently verified by this extraction; the study
  itself was not the triaged source for issue #1777 and was not separately
  mined here.

Referenced prior post by the same author:
  "Why context engineering is like teaching AI to skip stones", Thoughtworks
  Insights, published October 15, 2025 — a technical piece on RAG/knowledge-
  graph/vector-search context engineering for BFSI compliance use cases, cited
  by this article as prior work on "the architectural dimension of this
  problem." Not itself source-noted in this corpus as of this extraction.
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-addyosmani-intent-debt.md`,
`blog-thoughtworks-gall-supervisory-engineering.md`,
`blog-thoughtworks-kamelman-ai-governance-category-error.md`, and
`blog-anthropic-ai-native-engineering-org.md` were re-read directly
(MINER.md §4b) and claim numbers below were confirmed against those notes'
numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-addyosmani-intent-debt.md` Claim 2 (an agent cannot generate
    intent, only infer a plausible-sounding rationale) and Claim 9 (the
    scarce resource shifted from implementation to intent, "the one input
    that still has to originate with a human"): both directly corroborate
    this article's Claims 3 and 6 — Osmani and Kamelman independently
    describe the same mechanism (agents fill gaps left by unexternalized
    human understanding with fabricated/approximated substitutes) using
    different vocabulary ("intent" vs. "transmissibility"/"externalized
    mental model") from different starting points (Osmani: what must be
    written into repo artifacts; Kamelman: what must be communicated in
    real time to direct an agent).
  - `blog-addyosmani-intent-debt.md` Claim 5 (un-externalized intent used
    to cost a team once per onboarding/departure event; now it is paid
    every agent session): near-identical structural claim to this article's
    Claim 8 (the knowledge/transmission gap "has never, until now, had a
    direct economic cost attached to it") — two independent authors,
    publishing two weeks apart (Osmani 2026-06-05, Kamelman 2026-06-19),
    converge on AI adoption converting a previously-latent organizational
    gap into a recurring, directly-priced cost.
  - `blog-thoughtworks-gall-supervisory-engineering.md` Claim 11 (the
    industry no longer requires syntax mastery; it now values "strong
    mental models of system architecture" and "an intuitive grasp of
    real-world software behavior"): corroborates this article's Claim 6
    that articulated/legible mental models, not raw accumulated knowledge,
    are now the valued capability — though Gall's piece speculates this
    favors *experienced* engineers specifically (an open question the
    article itself hedges), while Kamelman's Claim 4 explicitly argues
    articulation ability is orthogonal to domain seniority (a non-expert
    who can articulate outperforms an expert who can't). This is a
    conditioning-variable difference (whose articulation ability is being
    predicted), not a contradiction — see MINER.md §4a criteria.
  - `blog-anthropic-ai-native-engineering-org.md` Claim 4 (context-gathering
    shifted from "find the code author" to "ask Claude what you actually
    need to know" — the question changed, not just the tool): a concrete,
    first-party practitioner instance of the same underlying shift this
    article argues for abstractly — institutional/tacit knowledge no longer
    accumulates in a queryable human head, so what can be explicitly
    transmitted (to a human questioner or to an agent) becomes the operative
    resource.

- **Contradicts**: No contradiction issue filed. This article's claims are
  interpretive/philosophical rather than empirical, and no existing corpus
  note was found that argues the opposite of its central thesis (that
  articulation/transmission capacity, not raw domain knowledge, drives
  AI-assisted work outcomes). The Prospector's second triage comment flagged
  a possible relation to contradiction issue #1764 (role convergence into
  generalists vs. specialization into sub-roles); on review, that
  contradiction is about the future *structure of job titles/roles*, while
  this article is about what capability within any role becomes valuable —
  the two are addressing different questions (role boundaries vs. skill
  composition) and this article does not take a position on role
  convergence/specialization, so it is not added as a party to that
  contradiction.

- **Extends**:
  - `blog-thoughtworks-kamelman-ai-governance-category-error.md`: same
    author, published two weeks earlier (2026-06-04). That piece argues
    governance debates are miscalibrated because they assume AI holds still
    while institutions respond, when AI is recursively self-improving. This
    piece applies a structurally similar move — arguing that a familiar
    category (expertise) is being decomposed by AI in a way conventional
    thinking hasn't caught up with — to a different object (individual
    skill/expertise rather than institutional governance). Both essays share
    Kamelman's recurring rhetorical pattern: take a settled-seeming category,
    argue AI is decomposing or outpacing it, and end on an open question
    rather than a prescription (see also Claim 5's note on the shared
    "unsupported historical analogy" rhetorical device across both pieces).
  - The author's own earlier piece "Why context engineering is like teaching
    AI to skip stones" (2025-10-15, not separately source-noted in this
    corpus): this article's Claim 9 explicitly revises that piece's
    architectural framing of "context selection" into a claim about
    individual human capability separable from expertise.

- **Novel**:
  - **The know/reason/transmit three-function decomposition of "expertise"**
    (Claim 1): no existing corpus source names this specific three-way
    split. It is a distinct decomposition from Storey's Triple Debt Model
    (technical/cognitive/intent) used in `blog-addyosmani-intent-debt.md`
    Claim 1 — that model splits *system* health categories, whereas this
    article splits *individual expertise* into functional components. The
    two frameworks operate at different units of analysis (system vs.
    person) even though both converge on "the un-externalized part is the
    one that costs you" (see Corroborates above).
  - **"Transmissibility" as a named, independently-priceable capability**:
    while other corpus sources (Osmani, Gall) gesture at the value of
    articulated/legible knowledge, this is the first source to name the
    capacity itself ("transmissibility") as a candidate independent economic
    variable, historically bundled with and mispriced as "expertise."
  - **The tribal-elder / teacher / consultant / filmmaker analogy** (Claim 5)
    as a historical framing for transmission-as-a-profession is not present
    elsewhere in the corpus.

## Guide Impact

- **Chapter 00 (Principles)**: The guide's foundational discussion of what
  AI-native engineering values could add this article's core distinction
  (Claim 1, Claim 6) — that raw domain knowledge and the capacity to
  externalize/transmit a mental model are separable, and that AI-assisted
  work rewards the latter specifically. This is a framing addition, not a
  practice change: it explains *why* practices like writing clear specs
  (`blog-osmani-good-spec.md`) and intent-focused documentation
  (`blog-addyosmani-intent-debt.md`) matter at the level of individual
  capability, not just team process.
- **Chapter 02 (Harness Engineering)**: Cite Claim 3 and Claim 6 alongside
  the existing AGENTS.md/intent-debt guidance to explain the *mechanism*
  (agents "infer and approximate" absent a clear model to act on) behind
  why precise, externalized instructions outperform vague ones — this
  corroborates rather than replaces the existing `blog-addyosmani-intent-debt.md`-
  sourced guidance.
- **Chapter 05 (Team Adoption)**: Claim 7 and Claim 8 (organizations that
  reward execution over explicability may be underinvesting in the
  capability AI rewards; the knowledge-transmission gap now has a direct
  economic cost) are relevant for any section on hiring, promotion, or
  onboarding criteria in AI-native teams — recommend citing as a hypothesis
  organizations should test against their own criteria (flag as anecdotal/
  unverified, not settled), alongside the concrete hiring-profile evidence
  already sourced from `blog-anthropic-ai-native-engineering-org.md` Claim 9
  ("creative builders with product sense" and "engineers with deep systems
  expertise" over "raw throughput").

## Extraction Notes

- **WebFetch declined verbatim reproduction; raw HTML was fetched directly
  instead.** As with `blog-thoughtworks-gall-supervisory-engineering.md` and
  `blog-addyosmani-intent-debt.md`, WebFetch's underlying model refused a
  full verbatim reproduction of the article, citing copyright concerns, and
  offered only a summary. To satisfy the verbatim-quote requirement in
  MINER.md §2a, the article was fetched a second way: `curl` against the
  live URL, followed by stripping HTML tags and unescaping entities to
  recover the raw text. All quotes in this note were verified against that
  raw-HTML extraction (saved locally during extraction), not against any
  WebFetch-generated summary or paraphrase.
- **Pull-quote duplication is a page-rendering artifact, not two separate
  statements.** The sentence "An organization that has systematically
  rewarded execution over explicability..." (Claim 7) appears twice in the
  raw extracted text, back-to-back with the "Matt Kamelman / Innovation
  Choreographer, Thoughtworks" byline repeated between them. This is the
  page's pull-quote/callout styling duplicating a body sentence for visual
  emphasis, not two independent instances of the claim in the source article.
  Recorded here as a single claim.
- **One linked page was followed for context, not separately source-noted.**
  The article links to Kamelman's own October 2025 piece ("teaching AI to
  skip stones") as prior work. That piece was fetched (via `curl`, same
  method) and read in full to accurately characterize Claim 9's relationship
  to it. It was not itself formally source-noted in this PR — it addresses
  a different topic (RAG/knowledge-graph context engineering for BFSI
  compliance) than what was triaged for issue #1777, and a full extraction
  of it would be better scoped as its own mining issue if the Prospector
  judges it independently novel. The Anthropic study this article's central
  claim rests on (Claim 2) was hyperlinked in the source but not followed or
  independently verified — it was not the triaged source for this issue,
  and this article does not quote the study directly, only characterizes it.
- **No contradiction issue filed.** See Cross-References → Contradicts above
  for the reasoning on why this article's relationship to contradiction
  issue #1764 does not rise to a material contradiction warranting a new
  filing.
- **Two Prospector triage comments were present on the issue** (apparently
  from repeated auto-triage runs, as also observed on issue #1422 in
  `blog-thoughtworks-gall-supervisory-engineering.md`'s extraction notes).
  Both converged on high/medium-high novelty and Ch00/Ch05 relevance; the
  first additionally named Ch02/Ch03, which this note follows since the
  harness-engineering and verification angles (Claim 3, Claim 6) are
  directly applicable.
