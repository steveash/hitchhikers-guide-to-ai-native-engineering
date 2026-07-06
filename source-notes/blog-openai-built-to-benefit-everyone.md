---
source_url: https://openai.com/index/built-to-benefit-everyone-our-plan
source_type: blog-post
title: "Built to benefit everyone: our plan"
author: Sam Altman and Jakub Pachocki
date_published: 2026-06-08
date_extracted: 2026-07-06
last_checked: 2026-07-06
status: current
confidence_overall: anecdotal
issue: "#1580"
---

# Built to benefit everyone: our plan

> OpenAI's CEO and Chief Research Officer publish a strategic vision statement
> declaring OpenAI has entered a named "third phase" — after research (phase 1)
> and product deployment (phase 2) — defined by three goals (build an automated
> AI researcher, accelerate the economy, give everyone a "personal AGI"), with a
> specific internal target (a significant fraction of OpenAI's own research done
> by AI by March 2028) and a public call for international coordination among
> frontier labs. This is corporate mission/strategy language with almost no
> concrete engineering, governance, or organizational detail.

## Source Context

- **Type**: blog-post (`openai.com/index/`, Company vertical, June 8, 2026,
  ~1,100 words). Byline: Sam Altman (CEO) and Jakub Pachocki (Chief Research
  Officer). Auto-discovered via the `openai-news` trusted RSS feed. All three
  Prospector triage comments on the source issue independently flagged this as
  low-to-medium novelty, strategic/vision language rather than a practitioner
  how-to, and asked the Miner to verify whether concrete engineering or
  governance detail existed beyond mission rhetoric — it does not.
- **Author credibility**: First-party statement from OpenAI's two most senior
  leadership roles (CEO, Chief Research Officer) at the company most central to
  the corpus's coverage of frontier AI labs. This is the highest-authority tier
  of source (official company strategy, published under named executive
  bylines, not an anonymous "OpenAI" corporate voice) — but authority over
  *what OpenAI intends to say publicly* is not the same as authority over
  *what OpenAI is technically or organizationally doing*. The post contains
  zero citations, zero metrics beyond one internal date target, and zero
  named engineering practices — it reads as a mission/manifesto piece, closer
  in kind to a shareholder letter or founder blog post than to a product or
  research announcement.
- **Scope**: Covers OpenAI's stated mission framing (broad AI access and
  distributed power as the "safer future"), a historical analogy to rural
  electrification, three named strategic goals, a definition of "OpenAI's
  third phase," a call for international coordination among frontier labs,
  and a footnoted definition of "AI resilience" (analogized to automobile
  safety infrastructure). Does NOT cover: any specific product, any technical
  architecture, any governance mechanism beyond "an international
  organization... should ultimately" exist, any org-chart or team structure,
  any metric beyond the March 2028 internal research-automation target, or
  any acknowledgment of counter-evidence (e.g., export controls, access
  restrictions, or safety incidents at OpenAI or peer labs).

## Extracted Claims

### Claim 1: OpenAI names its current strategic period the "third phase" of the company, distinct from an initial research phase and a subsequent product-deployment phase
- **Evidence**: Direct three-part periodization stated in the article as the
  frame for the rest of the post's goals.
- **Confidence**: anecdotal (self-declared corporate narrative structure, not
  an externally verifiable claim)
- **Quote**: "The first phase of OpenAI was about doing research toward AGI.
  The second phase began when our research became relevant to the real world
  and we became a product company: deploying our systems, learning from how
  people used them, and making continued progress toward AGI that is safe and
  aligned with our mission. Now we are entering the third phase."
- **Our assessment**: This is a rhetorical device more than a factual claim —
  OpenAI is retroactively narrating its own history into three acts to justify
  the goals that follow. It is useful to the guide only as a citable framing
  of how the company describes its own trajectory (research → product →
  "advanced AI abundant, affordable, safe, useful, and easy enough for every
  person and organization to benefit from it"), not as evidence that anything
  concrete changed on June 8, 2026.

### Claim 2: OpenAI states an internal target that by March 2028, "a significant fraction" of its own research may be conducted by AI systems working alongside human researchers
- **Evidence**: A specific, dated, internal forward-looking projection — the
  single most concrete and falsifiable claim in the entire post.
- **Confidence**: anecdotal (unaudited, self-reported internal belief about a
  future state; no baseline, no definition of "significant fraction," no
  measurement methodology disclosed)
- **Quote**: "Our internal belief is that by March of 2028 we may have a
  significant fraction of our research being done by AI systems in tandem
  with our own researchers."
- **Our assessment**: This is the only claim in the source with a concrete
  date and a (vague but falsifiable-in-principle) magnitude — everything else
  in the post is unfalsifiable mission language. "Significant fraction" is
  left undefined (10%? 50%?), and "may have" hedges the projection as belief
  rather than commitment. Directionally consistent with the industry-wide
  narrative that frontier labs are racing to automate their own research
  pipelines (see Cross-References), but should be cited in the guide only as
  "OpenAI's stated internal belief," never as an achieved or measured outcome.

### Claim 3: OpenAI states three "main goals": build an automated AI researcher, accelerate the economy while working to keep the gains widely shared, and give everyone on Earth a "personal AGI"
- **Evidence**: Explicit three-item list under the heading "Currently at
  OpenAI we have three main goals."
- **Confidence**: anecdotal (self-declared strategic priorities; no
  operationalization, budget, team, or metric attached to any of the three)
- **Quote**: "Build an automated AI researcher... Accelerate the economy...
  Give everyone on Earth a personal AGI, empowering them to benefit from one
  of humanity's most transformative technologies in whatever way they choose."
- **Our assessment**: The three goals are stated at the highest possible level
  of abstraction — no named products, timelines (beyond Claim 2's research
  target), or success metrics accompany any of them. "Give everyone on Earth
  a personal AGI" is a slogan-level claim; the post gives no indication of
  how OpenAI intends to reach populations without internet access, without
  disposable income for API/subscription costs, or under national export
  restrictions (see Cross-References — Contradicts). Useful to the guide only
  as a citable statement of stated corporate intent, not as evidence of a plan.

### Claim 4: OpenAI frames alignment as "itself a hard research problem" and states its researchers will need AI systems to "test ideas, find mistakes, explore alternatives, and iterate alongside" them to make fast progress
- **Evidence**: Direct statement connecting the "automated AI researcher" goal
  (Claim 3) to alignment work specifically, not just capability research.
- **Confidence**: anecdotal (aspirational framing of a research methodology;
  no description of what "iterate alongside us" means mechanically — no
  tooling, workflow, or evaluation method is named)
- **Quote**: "We believe that AI doing AI research will become the determining
  factor of the pace of progress within the next few years. That matters
  because alignment is itself a hard research problem. To make fast and deep
  progress, our researchers will need AI systems that can help test ideas,
  find mistakes, explore alternatives, and iterate alongside us."
- **Our assessment**: This is the closest the post comes to describing an
  actual research practice, but it stops at the level of intent — there is no
  concrete workflow, harness, or evaluation methodology described (contrast
  with `blog-anthropic-agent-identity-access-model.md`, which documents a
  shipped product architecture with named mechanisms). The claim that "AI
  doing AI research will become the determining factor of the pace of
  progress within the next few years" is a strong, unqualified prediction
  stated as settled belief, not evidence.

### Claim 5: OpenAI states it has "long believed there should ultimately be an international organization that helps coordinate leading AI efforts to reduce catastrophic risk," including the capacity to coordinate "slowing frontier development when needed"
- **Evidence**: Direct policy position stated in the post's discussion of
  national/global coordination.
- **Confidence**: anecdotal (an advocacy position, not a description of any
  organization that exists or that OpenAI has taken concrete steps to create)
- **Quote**: "We have long believed there should ultimately be an
  international organization that helps coordinate leading AI efforts to
  reduce catastrophic risk... One goal of such an organization should be to
  make it possible for the world to take coordinated action, including
  slowing frontier development when needed, so societal resilience, safety,
  and alignment can keep pace."
- **Our assessment**: This is a governance advocacy statement with no
  accompanying detail: no named proposal, no partner organizations, no
  timeline, and no acknowledgment of the practical difficulty of getting
  competing frontier labs and nation-states to cede any control over
  development pace to a coordinating body. It is directionally consistent
  with `blog-thoughtworks-kamelman-ai-governance-category-error.md`'s
  observation that "there should ultimately be" international coordination
  responses to fast-moving technology, but that source is skeptical
  governance can keep pace with self-improving AI at all — this post asserts
  the opposite (that such coordination is achievable) without engaging the
  skepticism.

### Claim 6: OpenAI explicitly states that "entirely automating everything is not the future we want," framing full automation as both "unfulfilling" and "dangerous," and describes the human role as becoming more important, not less, as AI capability grows
- **Evidence**: Direct normative statement distinguishing OpenAI's stated goal
  from full automation.
- **Confidence**: anecdotal (values statement, not a technical or operational
  commitment)
- **Quote**: "Entirely automating everything is not the future we want. It
  would be unfulfilling, and it would be dangerous. AI should help people
  pursue their goals, not become untethered from them. As AI systems become
  more capable, the human role becomes more important: setting direction,
  making tradeoffs, applying judgment, and bringing values, taste, care, and
  responsibility to the work."
- **Our assessment**: This directly echoes existing corpus framing that
  supervisory/judgment roles for humans become more important as agent
  capability increases, but here it is asserted as OpenAI's belief about
  society broadly, not stated as an operational engineering practice (contrast
  with `blog-thoughtworks-gall-supervisory-engineering.md`'s concrete
  "supervisory engineering" workflow prescription). Useful as an aligned,
  corroborating executive-level statement of a pattern the corpus already
  documents at the practitioner level, but adds no new mechanism.

### Claim 7: OpenAI states its "first commitment is to build AI in service of humanity," framed explicitly as avoiding power concentration among "a few companies, governments, or individuals," and asserts "the safer future is one where power is broadly distributed"
- **Evidence**: Direct mission statement, positioned early in the post as the
  foundational commitment underlying the rest of the strategy.
- **Confidence**: anecdotal (aspirational mission statement; no mechanism,
  metric, or governance commitment attached to "broadly distributed")
- **Quote**: "Our first commitment is to build AI in service of humanity. That
  means we want to empower people broadly, not see power concentrated among a
  few companies, governments, or individuals. We believe the safer future is
  one where power is broadly distributed, so more of the world can participate
  in building a resilience ecosystem."
- **Our assessment**: This is the post's central thesis, and it is the claim
  most directly in tension with existing corpus evidence — see
  Cross-References (Contradicts). OpenAI itself is one of the "few companies"
  whose decisions concentrate development pace and deployment terms for
  frontier AI; the statement gives no indication of any structural change
  (equity distribution, governance seat, or veto power for outside parties)
  that would make "broadly distributed" more than rhetorical.

### Claim 8: The post coins "AI resilience" via footnote, defined as the collective organizations, systems, and individuals society builds to anticipate, withstand, adapt to, and recover from AI-driven disruption — explicitly analogized to automobile safety infrastructure (seatbelts, traffic laws, licenses, crash testing, road infrastructure)
- **Evidence**: Footnoted definition attached to the mission statement in
  Claim 7.
- **Confidence**: anecdotal (a novel framing term introduced by the company;
  not an empirical or measured concept)
- **Quote**: "AI resilience refers to the collective organizations, systems,
  and individuals that society could put in place to anticipate, withstand,
  adapt to, and rapidly recover from AI-driven disruptions. For instance, the
  automobile transformed society, but they only became broadly beneficial
  because societies built systems around them: seatbelts, traffic laws,
  drivers' licenses, crash testing, and road infrastructure. The goal wasn't
  to stop people from driving—it was to make a powerful technology resilient
  enough for widespread use."
- **Our assessment**: This is the most concrete and portable idea in the
  source — a named concept ("AI resilience") with a specific historical
  analogy that gives it content: the automobile analogy names five concrete
  categories of societal scaffolding (safety equipment, law, licensing,
  testing standards, infrastructure). It is still an analogy, not a plan —
  the post does not map any of the five automobile-safety categories onto a
  concrete AI equivalent (what is AI's "seatbelt"? its "driver's license"?).
  Novel to the corpus as a named term; useful primarily as vocabulary rather
  than as evidence of implemented practice.

### Claim 9: The post opens with an extended historical analogy to rural electrification in 1920s America, arguing that a transformative technology's value comes from what people do with it rather than the technology itself, and that access diffuses unevenly and over time
- **Evidence**: The article's rhetorical framing device, occupying roughly the
  first third of the post.
- **Confidence**: anecdotal (historical analogy constructed for rhetorical
  effect, not a sourced historical claim — no citation for the "median
  inflation-adjusted income tripled" or "average lifespan had increased by
  over 20 years" figures)
- **Quote**: "Imagine electricity reaching a rural American town in the 1920s.
  Before power lines arrived, daily life was shaped by physical limits...
  Electricity did not transform every household overnight, and many of its
  benefits reached people unevenly. But as access spread, ordinary life
  changed."
- **Our assessment**: The analogy is doing persuasive work (transformative
  technologies take time to diffuse but are ultimately broadly beneficial) to
  set up the "give everyone a personal AGI" goal (Claim 3), but the specific
  historical statistics cited ("the average lifespan had increased by over 20
  years and the median inflation-adjusted income tripled or so" over the 20th
  century) are presented without citation and are not specific to
  electrification's causal contribution versus other 20th-century factors
  (sanitation, medicine, engineering — which the post itself lists as
  co-contributors). Not usable as an evidentiary claim; only as rhetorical
  context for how OpenAI wants readers to interpret its access mission.

## Concrete Artifacts

```
"Built to benefit everyone: our plan" — Sam Altman & Jakub Pachocki, OpenAI,
June 8, 2026

STATED THREE-PHASE COMPANY NARRATIVE:
  Phase 1: Research toward AGI
  Phase 2: Product company (deploy, learn from usage, iterate toward safe/
           aligned AGI)
  Phase 3 (current): Make advanced AI "abundant, affordable, safe, useful,
           and easy enough for every person and organization to benefit
           from it"

STATED THREE GOALS ("Currently at OpenAI we have three main goals"):
  1. Build an automated AI researcher (internal target: "by March of 2028
     we may have a significant fraction of our research being done by AI
     systems in tandem with our own researchers")
  2. Accelerate the economy (scientific progress, productivity, economic
     growth) "while working to ensure the gains are widely shared"
  3. Give everyone on Earth a personal AGI

FOOTNOTE — "AI resilience" (coined term):
  Defined as: "the collective organizations, systems, and individuals that
  society could put in place to anticipate, withstand, adapt to, and
  rapidly recover from AI-driven disruptions"
  Analogy: automobile safety ecosystem — seatbelts, traffic laws, drivers'
  licenses, crash testing, road infrastructure — "The goal wasn't to stop
  people from driving—it was to make a powerful technology resilient enough
  for widespread use."

GOVERNANCE POSITION:
  "We have long believed there should ultimately be an international
  organization that helps coordinate leading AI efforts to reduce
  catastrophic risk... including slowing frontier development when needed"
```

## Cross-References

- **Corroborates**:
  - `blog-thoughtworks-kamelman-ai-governance-category-error.md` Claim 3
    (frontier labs building explicit AI-improves-AI research capability,
    illustrated there by Anthropic's reported Karpathy-led team): This post's
    Claim 2 and Claim 4 (OpenAI's own stated internal target of a "significant
    fraction" of research being AI-conducted by March 2028, framed as
    necessary for making fast progress on alignment) is a second, first-party,
    named-executive confirmation of the same industry-wide trend the Kamelman
    piece describes secondhand for Anthropic. Where Kamelman's Claim 3 was
    rated anecdotal/unsourced within that note (no primary Anthropic citation
    given), this post is itself a primary source for the equivalent OpenAI
    claim — it strengthens the general pattern ("frontier labs are racing to
    automate their own research") even though it says nothing about
    Anthropic specifically.
  - `blog-thoughtworks-kamelman-ai-governance-category-error.md` Claim 1 (AI
    governance debates may be miscalibrated because the object being governed
    changes faster than institutions can respond) and Claim 9 ("alignment to
    what, decided by whom" as a harder question than technical alignment):
    This post's Claim 5 (call for an international coordination body) is the
    kind of governance response Kamelman's essay is skeptical can keep pace —
    the two sources corroborate that the coordination gap is real and
    discussed at the highest levels (an OpenAI executive statement and an
    independent essayist both treat "can governance move fast enough"
    as the live question), while disagreeing on how optimistic to be that an
    international body can close it.

- **Contradicts**:
  - **See filed contradiction issue #1597** (not resolved in this note per
    MINER.md §4a — no verdict is assigned here). This post's Claim 7 ("we
    believe the safer future is one where power is broadly distributed" /
    "give everyone on Earth a personal AGI," Claim 3) is in tension with
    `blog-ronacher-ai-nationalism-americans-only.md` Claim 1 and Claim 2,
    which document a concrete June 2026 policy event (Anthropic's Fable/Mythos
    export-control directive blocking foreign nationals, "including foreign
    national Anthropic employees") and argue that "universal" AI-safety
    framing from US frontier labs — Ronacher names Anthropic specifically but
    argues the pattern is industry-wide — coexists with, and arguably
    obscures, a real-world trend toward nationality-gated access. Both
    sources are about the same axis (how broadly frontier AI access actually
    is/will be distributed) and would lead to different guide advice about
    how much weight to give lab mission statements on universal access.
    Contradiction filed for human resolution; see CONTRADICTIONS.md once
    resolved.

- **Extends**:
  - `blog-simonwillison-encyclical-on-ai.md` Claim 7 (the encyclical's §108:
    "AI tends to amplify the power of those who already possess economic
    resources, expertise and access to data"): This post's Claim 7 states the
    opposite intent (power should be "broadly distributed") without engaging
    the encyclical's structural claim that concentration is the default
    tendency requiring active countermeasures. The two sources are not a
    direct contradiction (one is a structural/descriptive claim about
    tendency, the other is an aspirational commitment about intent), but a
    guide section citing OpenAI's access mission should pair it with the
    encyclical's skepticism that stated intent alone counteracts structural
    concentration.
  - `blog-openai-codex-knowledge-work.md`: That source note already flags
    OpenAI's "Global Affairs" vertical as producing policy-advocacy documents
    that use usage telemetry to support a favorable-regulation narrative
    (that note's Claim 12 — "Policy for the Agentic Era" recommendations to
    governments). This post is a second instance of OpenAI publishing
    company-mission/policy-advocacy content rather than technical or product
    disclosure, reinforcing that pattern: this is the second corpus source
    where OpenAI content should be read as strategic communication first,
    technical evidence second.

- **Novel**:
  - **Named three-phase company narrative** ("research phase" → "product
    company phase" → current phase of "making advanced AI abundant,
    affordable, safe, useful, and easy enough for every person and
    organization"): no prior corpus source documents OpenAI periodizing its
    own history this way.
  - **A dated, quantified (if vague) internal research-automation target**:
    "by March of 2028... a significant fraction of our research being done by
    AI systems" is the first OpenAI-sourced claim in the corpus with a
    specific future date attached to AI-conducted research, distinct from
    Kamelman's unsourced Anthropic/Karpathy claim.
  - **"AI resilience" as a named, defined term with the automobile-safety
    analogy**: not present elsewhere in the corpus.
  - **Explicit public call for an international AI-coordination body with
    power to slow frontier development**: no other corpus source documents a
    frontier lab publicly endorsing an external body with authority to slow
    its own development pace (contrast with the encyclical and Kamelman
    pieces, which discuss governance and coordination but not a specific lab
    endorsing an external slowing mechanism for itself).

## Guide Impact

- **Chapter 00 (Principles)**: If the guide discusses how frontier labs
  publicly frame their mission and how much weight practitioners should give
  such statements, cite Claim 7 and Claim 3 as an example of maximally
  aspirational, non-operationalized mission language — paired with the filed
  contradiction (issue #1597) as a concrete counter-example of the gap
  between stated mission and observed access-restriction practice. Recommend
  explicitly flagging this as "corporate strategy language, not an
  engineering or governance commitment" if cited at all.

- **Chapter 05 (Team Adoption)**: Claim 6 (human role becomes more important,
  not less, as AI capability grows: "setting direction, making tradeoffs,
  applying judgment") is a citable, executive-level corroboration of the
  supervisory-engineering pattern the guide likely already documents from
  practitioner sources (e.g., `blog-thoughtworks-gall-supervisory-engineering.md`).
  Add as a secondary, higher-authority-but-lower-specificity citation
  alongside the existing practitioner-level sourcing — do not let it replace
  the more concrete practitioner sources, since this post names no mechanism.

- **Chapter 06 (Security/Threat Model or Governance, if such a section
  exists)**: Claim 5 (call for an international coordinating body with power
  to slow frontier development) is worth a single-sentence mention as
  evidence that frontier labs themselves acknowledge the need for external
  coordination — but flag clearly that no such body exists yet and OpenAI
  names no concrete steps toward creating one. Should be presented alongside
  `blog-thoughtworks-kamelman-ai-governance-category-error.md`'s skepticism
  that governance can keep pace with self-modifying AI at all, not in
  isolation.

- **No chapter should cite this source's headline claims (Claims 3, 7, 9) as
  evidence of what OpenAI is actually doing** — they are unoperationalized
  mission statements. The only claim in this source with enough specificity
  to be treated as a real (if unverifiable) commitment is Claim 2 (the March
  2028 internal research-automation target), and even that should be flagged
  as self-reported belief, not a measured outcome.

## Extraction Notes

1. **Live URL returns Cloudflare/JS-challenge redirect**: `curl` and WebFetch
   against `https://openai.com/index/built-to-benefit-everyone-our-plan`
   both returned HTTP 403 / a client-side redirect challenge page, consistent
   with the second Prospector triage comment's note that "Article is behind
   Cloudflare challenge and full content could not be verified directly."
   Retrieved instead via the Wayback Machine snapshot
   `http://web.archive.org/web/20260611151801/https://openai.com/index/built-to-benefit-everyone-our-plan/`
   (crawled 2026-06-11, three days after publication), fetched with `curl`
   since the WebFetch tool itself refuses `web.archive.org` URLs directly
   (consistent with the pattern already documented in
   `blog-openai-codex-knowledge-work.md`'s Extraction Notes). The archived
   HTML was converted to text with `html2text` and reads as a complete,
   internally consistent article (byline, dateline, full body text, footnote,
   and standard site footer/nav boilerplate) — no truncation or summarization
   artifacts were observed.
2. **No sub-pages followed**: The article contains no substantive inline
   links to further primary content (only site navigation and "keep reading"
   links to unrelated OpenAI posts). Per MINER.md §1 guidance to follow up to
   5 substantive linked pages, none were followed because none existed.
3. **Source is thin on concrete, checkable content**: All three Prospector
   triage comments anticipated this and asked the Miner to verify whether the
   post contained concrete engineering, governance, or organizational detail
   beyond mission rhetoric. It does not — of nine extracted claims, only
   Claim 2 (the March 2028 date) has any specificity; the rest are
   unoperationalized mission and values statements. This note's overall
   confidence is rated `anecdotal` for that reason: the source is a
   first-party strategy statement with no metrics, no citations, and no
   independently verifiable claims beyond the bare fact that OpenAI published
   this statement on this date.
4. **Contradiction filed**: Per MINER.md §4a, filed issue #1597 (
   "Universal AI-for-everyone mission rhetoric vs. nationality-gated frontier
   AI access in practice") before writing this note, contrasting this
   source's Claim 3/Claim 7 against
   `blog-ronacher-ai-nationalism-americans-only.md` Claims 1–2. No verdict is
   assigned in this note; see the issue and (once resolved) CONTRADICTIONS.md.
5. **Cross-reference verification**: Before writing citations above,
   `blog-thoughtworks-kamelman-ai-governance-category-error.md`,
   `blog-ronacher-ai-nationalism-americans-only.md`,
   `blog-simonwillison-encyclical-on-ai.md`, and
   `blog-openai-codex-knowledge-work.md` were re-read directly (MINER.md §4b)
   and all claim numbers above were confirmed against those notes' numbered
   `### Claim N:` headings in document order.
