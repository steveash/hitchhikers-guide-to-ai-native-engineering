---
source_url: https://www.latent.space/p/chai-discovery
source_type: blog-post
title: "The BioAI Phase Shift - Matthew McPartlon & Neil Patil, Chai Discovery"
author: Latent Space (RJ Honicky), interviewing Matt McPartlon (cofounder) and Neil Patil (product lead), Chai Discovery
date_published: 2026-08-11
date_extracted: 2026-08-28
last_checked: 2026-08-28
status: current
confidence_overall: anecdotal
issue: "#3001"
---

# The BioAI Phase Shift - Matthew McPartlon & Neil Patil, Chai Discovery

> A Latent Space podcast episode page (written intro essay plus two short
> transcript excerpts; no full transcript published) arguing that
> structural-biology AI models crossed a "good enough to trust" threshold
> in January 2026, unlocking a wave of pharma licensing deals for Chai
> Discovery, and describing the company's product bet on a CAD-like
> molecule editor rather than a chatbot interface.

## Source Context

- **Type**: blog-post (podcast episode page, Latent Space Substack,
  published 2026-08-11). The written text totals 807 words per the page's
  own embedded metadata (`post.wordcount`): a framing essay on why pharma
  tools deals were historically rare and what changed in January 2026
  ("Pharma suddenly doing big AI tools deals"), a short two-line transcript
  excerpt (RJ Honicky and Matt McPartlon), a second section on Chai's
  product strategy ("Photoshop for molecules") containing one longer
  transcript excerpt from Neil Patil, a five-bullet "tune in to learn
  about" teaser list, and two footnotes (defining "biobucks" and
  caveating the Photoshop/SolidWorks analogy). Two embedded YouTube
  players point to the full episode video (ID `Qp5xklyJySI`); no rendered
  transcript text beyond the two excerpts above appears in the page's
  embedded JSON (`post.body_html`).
- **Author credibility**: Latent Space is a widely-read AI engineering
  podcast/newsletter that has hosted named founders and researchers from
  OpenAI, Anthropic, and elsewhere; this episode was sourced from the
  Prospector's `latent-space` trusted feed, the same publication already
  represented in this corpus by `blog-latentspace-xaira-causal-data-drug-discovery.md`
  and `blog-latentspace-lila-sciences-lab-data-center.md`. The interview
  subjects — Matt McPartlon (cofounder) and Neil Patil (product lead) of
  Chai Discovery — are named company officers describing their own
  company's product and commercial strategy; treat their claims as
  first-party positioning, not independently audited results. The
  framing essay (deal-structure explanation, "what changed" narrative,
  historical a16z reference) is the host's (RJ Honicky's) own written
  analysis, not a direct transcription of either guest.
- **Scope**: Covers Chai Discovery's 2026 pharma deal wave (four deals by
  summer 2026: Eli Lilly plus an expansion, Novartis, argenx), the
  historical reason AI-for-pharma companies default to building their own
  drug pipelines instead of licensing tools, the "biobucks" deal-structure
  mechanics, the claimed January 2026 inflection point ("tools got good
  enough for drug design teams to trust"), and Chai's product-design
  thesis (a CAD-like molecule editor, informed by partner needs rather
  than research done "in a vacuum"). Does NOT cover, in accessible text:
  Chai's underlying model architecture, training data, or benchmark
  numbers; the actual terms of any specific deal beyond "biobucks"
  structure in general; or the five teased discussion topics (protein
  token value, "portfolio optimization" framing, simplicity-driven
  scale) — these are named only as a bare bullet list with zero
  elaboration in the written page.

## Extracted Claims

### Claim 1: Chai Discovery, a two-year-old company backed by OpenAI, was at the center of four major AI×Pharma tools deals announced at the January 2026 JPM Pharma conference, and was valued at $4B in its Series C round

- **Evidence**: Stated as the article's opening framing claim, with inline
  links to a TechCrunch piece on the Eli Lilly deal and a LinkedIn post
  from Chai's co-founder announcing the $400M Series C.
- **Confidence**: anecdotal (a specific, checkable valuation and deal
  count, but sourced to the host's framing plus linked third-party
  reporting, not verified independently by this Miner beyond confirming
  the links exist in the source page)
- **Quote**: "This January, four big AI × Pharma tools deals were
  announced at the huge JPM Pharma conference that takes over San
  Francisco every year. OpenAI-backed Chai Discovery (now worth $4B) was
  somehow at the heart despite being all of 2 years old."
- **Our assessment**: The valuation and deal-count figures are specific
  and dated enough to be independently checkable (linked TechCrunch and
  LinkedIn sources), which raises this above a vague "AI is disrupting
  pharma" claim, but this Miner did not independently open those linked
  pages to verify the figures — treat as a plausible, well-sourced-looking
  claim, not confirmed.

### Claim 2: Pharma tools companies have historically defaulted to building their own drug pipelines rather than licensing to pharma, because proving a tool works (via good, validated targets) makes it easier to just keep that value yourself — either by raising money or by selling a proven target for biobucks — than to sell the tool itself across many companies' portfolios on a promise

- **Evidence**: Stated as the article's core explanation for why pharma
  tools deals were rare before 2026, framed as a structural incentive
  problem rather than a technology gap.
- **Confidence**: emerging (a specific, named causal mechanism for a
  market pattern, plausible on its face, but asserted by the host without
  citation to specific failed or redirected companies)
- **Quote**: "companies that start as AI for Pharma usually end up
  building their own drug pipelines instead, and the reason is something
  like this: convincing pharma to use your tool requires proof that your
  tool works. Proof means good targets, maybe with good clinical
  validation. If you have that, then it's easier to raise money (with a
  known, if long path to commercialization) or sell (e.g payment in
  biobucks) for a specific target than it is to sell to lots of companies
  on a promise that it will work across their portfolios."
- **Our assessment**: This is the source's sharpest guide-relevant claim
  about vertical-AI go-to-market economics: the same proof-of-value
  evidence that would let a startup sell its *tool* is, once obtained,
  more valuable kept in-house as a *proprietary asset* (a validated
  target) than sold as a service — a structural disincentive to
  horizontal tool-licensing in domains where the tool's own output is a
  monetizable asset. This generalizes beyond biotech to any domain where
  a tool's output (not just its usage) has direct resale value.

### Claim 3: "Biobucks" deals are structured so the headline value is almost entirely contingent — typically only 2-5% is paid upfront, with the rest paid out only if the drug clears each subsequent development milestone, and most drugs don't clear those gates

- **Evidence**: Footnote 1, defining the term used earlier in the article
  ("payment in biobucks").
- **Confidence**: settled (a factual description of a standard
  pharma-licensing deal structure, consistent with well-documented
  industry practice outside this source)
- **Quote**: "\"Biobucks\" is deal-value for milestone-heavy licensing
  agreements — the headline number (e.g., \"$1.7B deal\") is almost
  entirely contingent on hitting targets. Typically only 2–5% of the
  total is upfront; the rest pays out only if the drug clears each gate,
  and most drugs don't."
- **Our assessment**: Important context for reading any headline pharma-AI
  deal-value number (including Chai's own Lilly/Novartis/argenx deals):
  the announced figure is not a revenue guarantee. A guide citing
  vertical-AI deal sizes in regulated/high-attrition industries should
  flag this same "headline vs. realized value" gap as a general pattern,
  not specific to Chai.

### Claim 4: What changed in January 2026 was not the deal structure but the tools crossing a trust threshold — they became "good enough" for drug design teams to actually rely on

- **Evidence**: Stated as the direct answer to the article's own question
  ("What changed?"), immediately following the deal-structure explanation.
- **Confidence**: anecdotal (host's own interpretive claim; no benchmark,
  metric, or named threshold is given for what "good enough to trust"
  means quantitatively)
- **Quote**: "The \"we'll just partner / build our own drug\" optionality
  proved to be the only good path up until January. What changed? In
  short, the tools got good enough for drug design teams to trust."
- **Our assessment**: This is an assertion of a trust inflection point
  with no supporting benchmark or metric — it should be read as the
  article's thesis framing, not as independently demonstrated. It is,
  however, a specific and falsifiable claim (a dated before/after) rather
  than a vague "AI is improving" statement.

### Claim 5: Trusted-enough tools unlock two distinct benefits — scaling existing discovery (more, better candidates reaching lab/animal trials faster, more toxicity/delivery screening, higher clinic success likelihood) and enabling mechanisms that were previously very hard or impossible via lab-based discovery alone, such as bi-specific antibodies that bind two different proteins

- **Evidence**: Stated directly in the framing essay, distinguishing an
  efficiency argument from a capability argument.
- **Confidence**: emerging (a specific, testable claim about a class of
  molecule — bi-specific antibodies — being unlocked, but no example
  antibody, target, or outcome is named)
- **Quote**: "Good-enough-to-trust unlocks the ability to scale discovery:
  get more, better candidates into the lab and animal trials faster. More
  screening for toxicity, better delivery, etc. This means that what you
  push to the clinic is more likely to succeed. Tools also unlock new
  capabilities: mechanisms that are very hard or impossible to develop
  using lab-based discovery. Designing an antibody that precisely
  triggers a very specific molecular cascade takes many years of trial
  and error. Designing bi-specific antibodies (that bind to two different
  proteins) is similarly difficult. Good design tools can unlock this."
- **Our assessment**: The scale/efficiency half of this claim is a
  familiar "AI speeds up the existing pipeline" argument seen broadly in
  this corpus's vertical-AI notes. The capability half (new molecule
  classes previously infeasible by trial-and-error) is the more novel and
  harder-to-verify claim — no named bi-specific antibody design or
  clinical outcome is cited as evidence, only the general design
  difficulty argument.

### Claim 6: Matt McPartlon frames Chai's ambition as a step change, not an efficiency gain — first matching what evolution (a mouse) can already do, then doing what mice cannot, then compounding further capability on top of that

- **Evidence**: Direct transcript excerpt, RJ Honicky's framing followed
  by McPartlon's response.
- **Confidence**: anecdotal (founder's own framing of ambition/thesis; not
  a measured capability claim)
- **Quote**: "RJ: The fact that the quality of the model has jumped means
  you're enabling things you just plain couldn't do. So it's a step
  change. It's not an efficiency argument at all, or not so much. Matt:
  Yeah, exactly. It's kind of interesting, even for us — it took me a
  while to believe in the thesis, actually. I talked to Josh for months
  before Chai started... It's like, can I beat a mouse, and then can I do
  what mice can't do? And then how many levels of interaction can you
  just keep building on top of that?"
- **Our assessment**: "Beat a mouse, then do what mice can't" is a
  concrete, memorable framing of a capability ladder (match a known
  biological baseline, then exceed it) applicable as a general pattern
  for arguing when a vertical AI tool has crossed from "efficiency" to
  "new capability" territory — but it is McPartlon's own rhetorical frame
  for his company's thesis, not an externally validated benchmark.

### Claim 7: Chai's differentiator is framed as getting good molecules right the first time (reducing the amount of downstream lab iteration needed), which "turns science into engineering" and lets teams "hill climb towards one-shotting molecules" through to the clinic

- **Evidence**: Stated directly in the framing essay as Chai's positioning
  relative to others in the "structural / binding space."
- **Confidence**: anecdotal (company positioning language; no named
  molecule, target, or measured iteration-count reduction is given)
- **Quote**: "Chai is pointing to a different unlock: getting good
  molecules right out of the gate (meaning they don't then need as much
  lab work) means that the iteration time is faster. This turns science
  into engineering: you can design your systems to reduce friction and
  hill climb towards one-shotting molecules all the way to the clinic."
- **Our assessment**: "Turns science into engineering" is a notable
  reframing pattern — treating a historically iterative, trial-and-error
  discipline as an optimizable engineering pipeline once a reliable
  design tool exists — but it's presented as a positioning thesis with no
  concrete before/after iteration-count example to substantiate the
  "one-shotting" claim.

### Claim 8: The technical unlock underlying the 2026 deal wave is that structural models (which predict protein structure) evolved into binding affinity models (which predict how well two molecules bind), and binding models are what make actual molecular design — not just structure prediction — possible

- **Evidence**: Stated directly, with an explicit historical anchor (a16z
  articulated a version of the "AI unlocks drug design" thesis in 2020)
  and a claim about what specifically changed since then.
- **Confidence**: emerging (a specific, technically named capability
  transition — structure prediction to binding-affinity prediction — but
  no benchmark, model name, or accuracy figure is given to substantiate
  "steadily improving")
- **Quote**: "This, per-se, is not a new thesis: a16z articulated a
  version of this in 2020. What has changed is that structural models
  became binding models (how well doesn't this molecule bind to this
  molecule, aka "binding affinity). Binding models unlock design, which
  has been steadily improving. Chai's observation is that for engineering
  problems the best product tends to win, and good technology is a
  necessary but not sufficient condition."
- **Our assessment**: "Good technology is necessary but not sufficient;
  for engineering problems the best product tends to win" is a specific,
  guide-relevant claim about vertical AI competition dynamics — it argues
  the deciding factor in a technically-converged field (many labs can
  build a good binding model) is product execution, not raw model
  quality. This is asserted as Chai's own strategic observation, not
  independently demonstrated against competitors.

### Claim 9: Chai's product bet is a CAD/graphics-design-like molecule editor rather than a chatbot interface — described by the author as "Photoshop for molecules" (with a footnote acknowledging SolidWorks may be the more accurate but less recognizable analogy)

- **Evidence**: Section heading and following sentence, plus footnote 2.
- **Confidence**: anecdotal (product-design framing from the author/host;
  no screenshot, workflow walkthrough, or user-facing detail of the
  editor is given in the written text)
- **Quote**: "This means better UX, such as a molecule editor that is more
  like a CAD or graphics design program than a chatbot." Footnote: "I
  actually think SolidWorks is a better analogy, but PhotoShop has better
  brand recognition ¯\\_(ツ)_/¯"
- **Our assessment**: This is a specific, checkable design claim (direct
  manipulation / CAD-style editing surface, explicitly positioned against
  a chat interface) for a domain-expert-facing vertical AI tool. It
  directly parallels the grid/cell-based, non-chat UI pattern documented
  for a different regulated vertical in
  `blog-anthropic-hebbia-financial-diligence.md` (Claim 4: Hebbia's
  Matrix product grounds and displays each answer in its own grid cell
  rather than a chat thread) — see Cross-References.

### Claim 10: Neil Patil frames Chai's research agenda as informed by what partners "organically" ask for help with, rather than research conducted "in a vacuum" based on what would hypothetically be useful

- **Evidence**: Direct transcript excerpt, attributed by name and role in
  the source's own blockquote formatting.
- **Confidence**: anecdotal (product lead's own characterization of the
  company's research process; no example of a specific partner request
  that shaped a specific feature is given)
- **Quote**: "What is kind of cool about working so closely and supporting
  so many of these partners is we get to really learn about what is the
  stuff that would be helpful in research. So rather than doing research
  in a vacuum, based on what would hypothetically be cool, we're able to
  do informed research based on what our partners have just been
  organically asking us for help with. — Neil Patil, (Chai product lead)"
- **Our assessment**: A specific, named claim about how partnership access
  shapes a vertical AI company's R&D prioritization (partner-need-driven
  rather than research-driven), consistent with the general
  "co-development with enterprise partners as a product-discovery
  mechanism" pattern already documented elsewhere in this corpus for
  other verticals (see Cross-References), but offered here with no
  concrete example of a feature or model change that resulted from a
  specific partner request.

### Claim 11: Since June 2026, Chai announced three more major deals — Lilly, Novartis, and argenx — plus an expansion of its existing Eli Lilly program

- **Evidence**: Stated directly in the framing essay as evidence the
  partnership approach "has paid off."
- **Confidence**: anecdotal (specific, named, dated deal list, but
  presented without deal values, terms, or independent confirmation
  beyond the host's own statement)
- **Quote**: "Their approach has paid off: since June, Chai has announced
  three more major deals: Lilly, Novartis, argenx, plus an expansion of
  their Eli Lily program." [sic — "Lily" appears misspelled in the source
  in this instance]
- **Our assessment**: Concrete, dated, named-counterparty deal list (four
  pharma names total across the article: Eli Lilly x2, Novartis, argenx)
  — the most independently checkable commercial claim in the source,
  though this Miner did not verify each deal against an independent
  announcement.

### Claim 12: The episode discusses five additional topics — protein tokens having the highest downstream value of any token type, climbing levels of abstraction as models improve, framing pharma/VC/research as portfolio optimization, better tech changing the whole portfolio, and relentless focus on simplicity enabling scale — but the written page gives no supporting detail for any of them

- **Evidence**: A bare five-bullet teaser list ("tune in to learn about"),
  immediately preceding a second embedded YouTube player.
- **Confidence**: anecdotal (bare topic labels, zero elaboration in
  accessible text)
- **Quote**: "Why protein tokens have the highest downstream value of any
  token / Climbing levels of abstraction as models improve / How Pharma,
  VC, and research are all just portfolio optimization / How better tech
  changes the whole portfolio / How relentless focus on simplicity leads
  to scale"
- **Our assessment**: Each of these is a genuinely guide-relevant-sounding
  claim (especially "protein tokens have the highest downstream value of
  any token type," which would bear on tokenization/data-value framing if
  elaborated), but none is substantiated anywhere in the written text —
  the actual argument exists only in the linked video, which this Miner
  did not watch (see Extraction Notes). Flagging as a gap for future
  re-mining if a transcript becomes available, consistent with how
  `blog-latentspace-xaira-causal-data-drug-discovery.md` (Claims 11-12)
  handled the same bare-teaser pattern from the same publication.

## Concrete Artifacts

### "Tune in to learn about" bullet list (verbatim, 5 bullets)

```
Why protein tokens have the highest downstream value of any token

Climbing levels of abstraction as models improve

How Pharma, VC, and research are all just portfolio optimization

How better tech changes the whole portfolio

How relentless focus on simplicity leads to scale

Source: latent.space, "The BioAI Phase Shift - Matthew McPartlon & Neil
Patil, Chai Discovery," August 11, 2026
```

### Footnote 1 — "biobucks" deal-structure definition (verbatim)

```
"Biobucks" is deal-value for milestone-heavy licensing agreements — the
headline number (e.g., "$1.7B deal") is almost entirely contingent on
hitting targets. Typically only 2–5% of the total is upfront; the rest
pays out only if the drug clears each gate, and most drugs don't.

Source: latent.space, "The BioAI Phase Shift," footnote 1
```

### Deal timeline (as stated in the article, assembled from body text)

```
January 2026 (JPM Pharma conference): 4 AI x Pharma tools deals announced
  industry-wide; Chai Discovery (OpenAI-backed, ~2 years old, $4B
  valuation per Series C) described as "at the heart" of this wave.
  - Eli Lilly deal (per linked TechCrunch coverage)

Since June 2026, per Chai's own account: 3 additional major deals
  - Lilly (expansion of existing program)
  - Novartis
  - argenx

Source: latent.space, "The BioAI Phase Shift," body text
```

## Cross-References

- **Corroborates** `blog-anthropic-hebbia-financial-diligence.md` Claim 4
  (Hebbia's Matrix product grounds each answer in a source document and
  displays it in its own grid cell, giving analysts transparency,
  traceability, and steerability, rather than a chat thread): Claim 9
  above (Chai's CAD-like molecule editor, explicitly positioned against a
  chatbot) makes the same underlying design argument — domain experts in
  a high-stakes vertical (pharma design, financial diligence) are better
  served by a direct-manipulation, artifact-grounded interface than a
  conversational one. Two independently named companies in two different
  regulated verticals converging on "not a chatbot" as the right UX for
  expert users is a useful cross-vertical pattern for the guide.
- **Extends** `blog-latentspace-xaira-causal-data-drug-discovery.md` and
  `blog-latentspace-lila-sciences-lab-data-center.md`: both existing
  BioAI notes in this corpus cover R&D/data-generation strategy (Xaira's
  causal-perturbation training data; Lila's automated-lab data platform)
  from named scientists/researchers. This source is the first in the
  corpus to cover the *commercialization* side of the same 2026 BioAI
  wave — deal structures (biobucks), a stated trust-threshold inflection
  point (January 2026), and product/GTM strategy (partner-informed
  research, CAD-style UX) — from a company's product and founding
  leadership rather than its scientists. Read together, the three notes
  span data strategy (Xaira), infrastructure/data-generation platform
  (Lila), and commercialization (Chai) for the same emerging vertical.
- **Novel**: No existing source note in this corpus documents: (1) the
  "biobucks" milestone-heavy licensing deal structure and its
  upfront/contingent split; (2) the structural incentive argument for why
  AI-for-pharma companies default to building proprietary pipelines
  instead of licensing tools (Claim 2); (3) a named, dated (January 2026)
  claimed trust-threshold inflection point for pharma AI-tool adoption;
  (4) the structural-model-to-binding-model technical narrative as the
  claimed unlock behind that inflection point; (5) a specific pharma
  deal list (Eli Lilly, Novartis, argenx) tied to a named vertical AI
  company's commercial traction.

## Guide Impact

- **Chapter 05 (Team Adoption / Enterprise Partnerships)**: If the guide
  documents vertical-AI enterprise sales patterns in regulated
  industries, add Claim 2 (the proof-of-value-becomes-a-proprietary-asset
  disincentive against licensing) and Claim 3 (the biobucks
  headline-vs.-realized-value gap) as a named pattern from biotech/pharma
  — both generalize beyond this domain to any vertical where a tool's
  *output*, not just its usage, has direct resale value. Cite alongside
  the existing Hebbia/Kepler financial-services notes as a second
  regulated-industry example of vertical AI commercialization, but flag
  all figures (deal count, valuation, deal names) as unverified beyond
  the host's own reporting and linked third-party articles this Miner did
  not independently open.
- **Chapter 02 (Harness/Product Design)**: If the guide discusses
  interface design for domain-expert users, add Claim 9 ("Photoshop for
  molecules" — CAD-style direct manipulation over chatbot) as a second,
  independently-sourced data point (alongside Hebbia's grid-cell UI)
  supporting a "domain experts in high-stakes verticals prefer
  direct-manipulation artifact interfaces over chat" pattern. Two data
  points is still thin for a general recommendation — flag as emerging,
  not settled.

## Extraction Notes

- Fetched via `curl` with a browser user agent, then parsed the page's
  embedded `window._preloads` JSON blob (`post.body_html`,
  `post.wordcount`) rather than relying on an initial WebFetch pass, per
  MINER.md §2a's requirement that quotes be verbatim rather than
  paraphrased — the same method used for
  `blog-latentspace-xaira-causal-data-drug-discovery.md`. The embedded
  JSON's `wordcount` field (807) is consistent with the length of the
  extracted written text (framing essay, two transcript excerpts, bullet
  list, two footnotes), confirming the full written page content was
  captured and nothing was paywall-truncated. All quotes in this note
  were copied character-for-character from the raw `body_html` (HTML
  tags stripped, HTML entities as rendered) rather than from a
  markdown-converted summary.
- As with the Xaira episode already in this corpus, the page exposes a
  "Transcript"/video UI but no full rendered transcript text in its
  embedded JSON — only the two blockquoted excerpts (RJ/Matt exchange;
  Neil Patil's quote) appear as direct transcription. The bulk of the
  interview (the five teased topics in Claim 12, and any further detail
  behind Claims 1, 4-8, 11) exists only in the linked YouTube video
  (ID `Qp5xklyJySI`), which this Miner did not watch. `confidence_overall`
  is rated `anecdotal` for the note as a whole on this basis, consistent
  with the same rating applied to the Xaira note for the identical
  structural limitation.
- No linked sub-pages were followed beyond confirming the TechCrunch and
  LinkedIn links referenced in Claim 1 exist in the source's HTML; their
  content was not independently fetched or verified by this Miner.
- Checked for contradictions against `blog-latentspace-xaira-causal-data-drug-discovery.md`,
  `blog-latentspace-lila-sciences-lab-data-center.md`, and this corpus's
  financial-services vertical-AI notes (`blog-anthropic-hebbia-financial-diligence.md`,
  `blog-anthropic-kepler-verifiable-ai-financial.md`) — found
  extension/corroboration relationships only (see Cross-References), no
  claim in this source directly opposes a claim in an existing note, so
  no contradiction issue was filed per MINER.md §4a.
- The issue's three Prospector triage comments gave inconsistent chapter
  guidance across passes (Ch05/Ch06/Ch07; Ch01/Ch05; Ch05/Ch02). This
  note's Guide Impact section reflects independent judgment from reading
  the source directly: Ch05 (enterprise/vertical adoption economics) and
  Ch02 (domain-expert interface design) are the two places this source
  gives specific, citable content; Ch06/Ch07/Ch01 were considered but not
  used because the source gives no accessible detail on Chai's
  deployment/ops architecture, scaling infrastructure, or day-to-day
  market-signal data beyond the deal list already captured in Claim 11.
