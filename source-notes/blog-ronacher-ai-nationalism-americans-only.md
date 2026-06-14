---
source_url: https://lucumr.pocoo.org/2026/6/13/americans-only/
source_type: blog-post
title: "Dangerous Technology For Americans Only"
author: Armin Ronacher
date_published: 2026-06-13
date_extracted: 2026-06-14
last_checked: 2026-06-14
status: current
confidence_overall: anecdotal
issue: "#1176"
---

# Dangerous Technology For Americans Only

> Armin Ronacher argues that the US government's export control directive
> blocking Anthropic's Fable and Mythos models for foreign nationals represents
> AI nationalism masquerading as safety discourse — and identifies Europe's
> structural dependency on US AI infrastructure as a concrete engineering
> constraint, with open source as the primary path that avoids total
> concentration of frontier AI power.

## Source Context

- **Type**: blog-post (lucumr.pocoo.org personal blog; ~2,000 words; opinion/
  political essay published 2026-06-13; four named sections: "Safety and
  National Control", "Oh Europe", "The American Trap", "The Way Out Is
  Cooperation")
- **Author credibility**: Armin Ronacher is the creator of Flask, Jinja2,
  Click, and Sentry, and the author of the Pi coding agent. His blog is a
  designated `trusted-feed` source in this repo. This post is political and
  strategic commentary rather than technical practitioner analysis — it is
  Ronacher's first public piece on AI governance and export controls rather
  than on coding workflows. Claims are anecdotal/opinion; Ronacher discloses
  a personal stake ("I'm guilty of this myself as we have incorporated our
  holding in Delaware"). He is writing as a European founder who uses frontier
  AI models daily and is directly affected by the policy he describes.
- **Scope**: Covers the Anthropic export control directive (foreign national
  restriction on Fable and Mythos access), the shift from capability-based to
  nationality-based AI controls, European structural dependencies on US tech,
  self-inflicted European failures in market integration, the talent drain
  dynamic, the US model's limitations, and open source as a structural
  alternative to concentrated AI control. Does NOT cover: practitioner
  workflow patterns, harness engineering, specific coding agent techniques,
  or quantitative evidence of any kind. This is macro-level strategic and
  political analysis.

## Extracted Claims

### Claim 1: The US government's directive forced Anthropic to block AI model access for foreign nationals — including foreign national Anthropic employees — marking a shift from capability-based to nationality-based AI controls

- **Evidence**: Ronacher cites the Anthropic announcement directly (linked in
  the post to `https://www.anthropic.com/news/fable-mythos-access`). The
  scope of the directive — applying to foreign nationals "inside or outside
  the United States, including foreign national Anthropic employees" — is
  quoted from Anthropic's own description of the directive.
- **Confidence**: emerging (the policy event itself is a concrete, externally
  verifiable fact; Ronacher's characterization of its significance is anecdotal
  opinion)
- **Quote**: "The directive, as Anthropic describes it, applies to foreign
  nationals whether they are inside or outside the United States, including
  foreign national Anthropic employees. That is an astonishing boundary if you
  think about it. We moved from 'do not sell this model to hostile governments'
  to nationality itself being the defining boundary."
- **Our assessment**: This is a concrete, dated policy event — not a
  hypothetical. The specific scope (including Anthropic's own foreign national
  employees) makes it qualitatively different from prior export controls on
  commercial AI products, which targeted state actors. For practitioners outside
  the US: this is the first documented instance of a leading AI provider being
  forced to block model access by nationality rather than by use-case or
  destination-country classification. It changes the risk profile of depending
  on US frontier AI providers.

### Claim 2: AI safety discourse's universalist framing ("humanity, catastrophic risk, safeguards") has an embedded nationalist assumption that treats non-US actors as inherently untrustworthy

- **Evidence**: Ronacher's reading of US AI safety discourse as a practitioner
  who has engaged with it from a non-US perspective. No empirical study is
  cited — this is his direct observation and interpretation.
- **Confidence**: anecdotal
- **Quote**: "A lot of AI safety discourse presents itself as universal:
  humanity, catastrophic risk, safeguards, responsible deployment. Even
  Anthropic's own writings start out that way, but yet every time regulation
  is discussed there is an overtone of national security and that it cannot
  get into the wrong hands. It's not just Anthropic, it's the entire US based
  discourse on AI. The foundation is that the US has moral superiority and
  others are not to be trusted."
- **Our assessment**: This is an analytical claim about the structural logic of
  US AI safety discourse, not a factual claim about specific statements. For
  practitioners: the export control event gives this claim concrete grounding —
  safety language, if it maps to policy that restricts by nationality, operates
  as a national security instrument regardless of its framing. Teams making
  model selection decisions need to distinguish between a provider's stated
  values and the regulatory environment those values operate within.

### Claim 3: The export control situation cannot be addressed through regulation because it is a question of geopolitical power backed by military force, not a question of rules

- **Evidence**: Ronacher's political analysis of the negotiation dynamic between
  the EU and the US. He argues that the US's leverage comes from military
  capability, not from being normatively correct.
- **Confidence**: anecdotal
- **Quote**: "It is also a situation you cannot regulate yourself out of.
  European technology policy is entirely unprepared for this, because this is
  not a question of regulation but a question of might and power, something that
  Europe lacks."
- **Additional quote**: "Also let's not be naive in that this is a negotiation
  of money and force. The US is in that position because the US has a mighty
  military."
- **Our assessment**: The "regulation cannot fix this" claim is directly
  relevant to practitioners advising organizations on AI strategy. If AI access
  is a geopolitical variable — like energy, semiconductors, or satellite
  communications — it belongs in supply chain risk analysis, not just in
  compliance checklists. The existence of GDPR-level data regulation did not
  prevent this access restriction, consistent with Ronacher's claim.

### Claim 4: Europe has structural, layered dependency on US technology — cloud providers, operating systems, developer platforms, AI models, and satellite internet — with no comparable domestic alternatives

- **Evidence**: Ronacher's direct assessment as a European practitioner who
  builds on US infrastructure daily. The enumeration is specific.
- **Confidence**: anecdotal (widely observable dependency; no independent
  market data cited)
- **Quote**: "We depend on American cloud providers, operating systems,
  developer platforms and now AI models and internet from satellites. We also
  depend on global semiconductor supply chains we do not control. If access to
  frontier AI becomes a matter of American national security policy, Europe is
  not a peer in that conversation and might not even be a market."
- **Our assessment**: The specific enumeration is the most useful part of this
  claim for practitioners: cloud (AWS/GCP/Azure) → operating systems (Windows/
  macOS/iOS) → developer platforms (GitHub/npm/PyPI) → AI models (GPT/Claude/
  Gemini) → satellite internet (Starlink). Each layer is US-controlled. A team
  operating in the EU that depends on all five layers faces cascading exposure
  if US national security policy expands access controls beyond AI models. The
  phrase "might not even be a market" is the most extreme endpoint: a scenario
  where EU teams cannot access US AI providers at all, not just frontier models.

### Claim 5: European structural failure is primarily self-inflicted at the member-state level — fragmented internal markets, excessive regulatory burden, poor startup infrastructure, and brain drain — not primarily an EU-level failure

- **Evidence**: Ronacher's first-hand experience building companies across
  European jurisdictions, including incorporating a holding company in Delaware
  ("I'm guilty of this myself"). He identifies specific friction points by
  name.
- **Confidence**: anecdotal (single practitioner's direct experience; consistent
  with widely cited structural critiques of European startup ecosystems)
- **Quote**: "We built and maintained fragmented markets and then pretended we
  had a single one. We let company formation, hiring, equity compensation, tax,
  notaries, KYC, banking, and cross-border services remain much harder than
  they need to be and we are playing these rules against each other."
- **Additional quote**: "Too many entrepreneurs are blaming EU regulation for
  failures that are originating within the member states. EU regulation is the
  result of a democratic process between countries that are lobbying in favor
  of their local industries against others in the same economic bloc."
- **Our assessment**: The claim distinguishes EU-level policy (DMA, GDPR) from
  member-state level friction (notaries, KYC, cross-border banking, equity
  compensation). This is relevant for practitioners advising or working in
  European teams: the obstacle to hiring, equity structuring, and cross-border
  operations is often the local legal system of the member state, not the EU
  as a whole. Teams building engineering organizations across Europe face this
  layer of friction in ways that teams in the US do not.

### Claim 6: European talent drain creates a self-reinforcing death spiral — talent leaves because the ecosystem is weak; the ecosystem stays weak because talent leaves

- **Evidence**: Ronacher's structural observation, grounded in his own
  experience incorporating in Delaware. He presents the US infrastructure
  advantages (capital markets, startup infrastructure, employee equity) that
  make the migration individually rational.
- **Confidence**: anecdotal (widely recognized structural dynamic; not backed
  by longitudinal data here)
- **Quote**: "But this is why we are on a dangerous death spiral already.
  Talent leaves because the ecosystem is weak and the ecosystem stays weak
  because talent leaves. Infrastructure makes the world: build excellent
  swimming pools and you will grow a generation of great swimmers."
- **Our assessment**: This is the personnel-level mechanism that makes the
  structural dependency durable. For AI-native engineering teams: the same
  logic applies at the team level. A team that cannot access frontier AI models
  (due to export controls) or cannot build equity-driven compensation for
  AI-specialist talent faces compounding disadvantage relative to US teams.
  The "swimming pools" analogy is Ronacher's clearest statement that structural
  investment precedes talent development — not the reverse.

### Claim 7: Moving to the US is individually rational for European founders but collectively destructive — if every ambitious person treats Europe as a lost cause, it becomes one

- **Evidence**: Ronacher's normative argument, grounded in his own experience
  incorporating in Delaware. He explicitly frames his choice as individually
  rational but collectively harmful.
- **Confidence**: anecdotal
- **Quote**: "Moving to the US as a founder or tech employee is rational and
  individually it is often the right decision. But if every ambitious person
  treats Europe as a lost cause, then Europe becomes one. If everyone with
  agency leaves, the only people left to shape the system are the people most
  comfortable with the system as it is."
- **Our assessment**: This is the collective action problem at the ecosystem
  level. For teams: it suggests that individual-level decisions that seem
  optimal (incorporate in Delaware, use US AI providers exclusively, hire US
  talent) may be rational at the individual level while contributing to the
  structural dependency that makes export controls more damaging when they
  arrive.

### Claim 8: A stronger EU is, at best, a temporary defensive measure against a darker world — not a destination and not a substitute for international cooperation

- **Evidence**: Ronacher's normative argument about the limits of the "strengthen
  Europe" response. He explicitly rejects European nationalism as the answer to
  US nationalism.
- **Confidence**: anecdotal
- **Quote**: "This is why strengthening Europe cannot be the final goal. A
  stronger EU is, at best, a temporary defense against a darker world and not
  an excuse to replace American nationalism with European nationalism. The
  long-term answer cannot be bigger and bigger blocs fighting over who may use
  which model, which chip, which cloud or which trade route."
- **Our assessment**: This claim bounds the scope of the "build European AI"
  response. Ronacher is not arguing for European AI supremacy as the answer —
  he is arguing that the bloc-competition model itself is the failure mode.
  For AI strategy: this suggests the value of multi-provider strategies and
  open source adoption is not primarily "be in the right bloc" but rather
  "reduce dependence on any single bloc's political decisions."

### Claim 9: Open source is one of the few paths that does not naturally lead to total concentration of AI power

- **Evidence**: Ronacher's normative argument. He acknowledges open source is
  "not a magical answer to every problem" — the claim is comparative (relative
  to closed, centralized alternatives), not absolute.
- **Confidence**: anecdotal
- **Quote**: "I truly believe that Open Source matters and international
  cooperation matters. It is not a magical answer to every problem, but it is
  one of the few paths we have that does not naturally lead to total
  concentration of power."
- **Our assessment**: This is the direct prescriptive response to Claims 1–4.
  Open source models (weights publicly available) cannot be export-controlled
  in the same way that API-gated closed models can be blocked by nationality.
  Once weights are public, no subsequent government directive can un-publish
  them. The claim is not that open source models are better (capability is
  separate), but that they carry a structurally different access-risk profile.
  This is a novel framing for model selection criteria: not just cost/quality/
  latency, but access resilience.

### Claim 10: If frontier AI becomes accessible only through a small number of large corporations and governments, everyone else becomes dependent on their judgment

- **Evidence**: Ronacher's structural analysis of the current trajectory. He
  names both corporations and governments as concentration actors.
- **Confidence**: anecdotal (widely held concern; no empirical measure cited)
- **Quote**: "If frontier AI becomes something only large corporations and
  governments can control, then everyone else becomes dependent on their
  judgment. That is a bad place to be. Corporations will optimize for their
  incentives, as well structured as they might be, and governments will optimize
  for more and more power. Right now we're on a path in which access to
  general-purpose capability is mediated by a small number of actors with
  tremendous powers."
- **Our assessment**: This is the concentration-of-power argument for AI model
  diversity. The export control event is the concrete example: when one actor
  (US government) instructs another actor (Anthropic) to block access, the
  scope of that instruction is bounded by how many non-controlled alternatives
  exist. A team operating exclusively on closed US frontier models has no
  fallback when access is restricted. Multi-provider strategy and open-source
  hedges are not just cost optimization — they are access risk mitigation.

### Claim 11: The correct long-term direction is restoring international rule of law and broad access, not bloc supremacy — individual developers' success depends on a world where contracts, visas, trade routes, and payment systems function

- **Evidence**: Ronacher's normative concluding argument. He ties global
  stability concerns directly to individual engineering careers ("our basic
  needs cannot be considered met just because we have a great salaries or equity
  or investors that trust us").
- **Confidence**: anecdotal
- **Quote**: "If we believe this technology can be used for good, then broad
  access matters and our goal should be to restore the international rule of
  law, and not to further weaken it."
- **Additional quote**: "The way out is not American supremacy, Chinese supremacy
  or European supremacy. The way out is to climb back toward cooperation before
  the alternative becomes war."
- **Our assessment**: This is the macro-normative conclusion. For the guide's
  scope, the relevant implication is narrower: practitioners who believe AI can
  be used for good have a stake in broad access, not just in their own team's
  access. Advocacy for open source, for multi-provider strategies, and for
  international standards bodies is not just commercial pragmatism — it is
  aligned with restoring the kind of international cooperation on which
  engineering careers and projects depend.

## Concrete Artifacts

### The Anthropic Export Control Directive — Key Terms (as described in the post)

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/6/13/americans-only/
        citing Anthropic announcement at
        https://www.anthropic.com/news/fable-mythos-access (linked in post)

Scope as described:
  - Directive: US government export control
  - Models affected: Fable and Mythos (Anthropic)
  - Who is blocked: foreign nationals
  - Where: "whether they are inside or outside the United States"
  - Includes: "foreign national Anthropic employees"

Ronacher's framing of the boundary shift:
  "We moved from 'do not sell this model to hostile governments'
   to nationality itself being the defining boundary."
```

### European Structural Dependency Stack (as enumerated in the post)

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/6/13/americans-only/

Layers of EU dependency on US infrastructure (Ronacher's enumeration):
  1. Cloud providers
  2. Operating systems
  3. Developer platforms
  4. AI models
  5. Internet from satellites

Also named:
  - Global semiconductor supply chains

Ronacher's assessment:
  "If access to frontier AI becomes a matter of American national security
   policy, Europe is not a peer in that conversation and might not even
   be a market."
```

### European Member-State Friction Points Named in the Post

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/6/13/americans-only/

Specific friction points named (member-state level, not EU level):
  - Company formation
  - Hiring
  - Equity compensation
  - Tax
  - Notaries
  - KYC
  - Banking
  - Cross-border services

Illustrative example from post:
  "At one point I had to sign a four page contract for a 120 Euro lamp
   at an Austrian retailer, just to pick up from their store 15 minutes
   later."

Ronacher's framing: these are self-inflicted, not EU-mandated.
  "Too many entrepreneurs are blaming EU regulation for failures that are
   originating within the member states."
```

## Cross-References

- **Extends**: `blog-ronacher-local-models-focus-polish.md` Claim 14 — that
  note argues local/open-source models are preferable because "a hammer that's
  locked behind a subscription in a data center in another country does not
  qualify" as truly local, and that the goal is something "not limited by what
  the hyperscalers make available." The current post provides the concrete
  policy event that demonstrates WHY hyperscaler independence matters in
  practice: when the US government restricts a provider's API access by
  nationality, teams depending on that provider have no fallback. The current
  post supplies the geopolitical evidence; the local-models post supplies the
  technical path toward independence. Together they form a coherent argument:
  here is the risk (export controls by nationality), here is one mitigation
  (local/open-source inference).

- **Extends**: `blog-ronacher-communities-of-not.md` Claim 4 — that note
  documents that "LLMs show up in editors, issue trackers, hiring conversations,
  management pressure and code reviews whether we asked for them or not." The
  current post adds a policy dimension to that environmental fact: LLMs may
  show up in the work environment for US colleagues while being unavailable to
  non-US colleagues on the same team due to nationality-based access controls.
  The "whether we asked for them or not" dynamic has a new nationality-gating
  layer documented here.

- **Extends**: `blog-ronacher-pi-oss.md` (same author series) — the pi-oss
  note documents operational failure modes from dogfooding AI on Pi's codebase.
  The current post documents the macro-political context in which those
  operational decisions are made. The two posts represent different levels of
  Ronacher's analysis: pi-oss is micro (how AI affects individual engineering
  workflows), this post is macro (how geopolitics affects AI access). Both
  are relevant to the guide, at different levels of abstraction.

- **Corroborates**: `blog-ronacher-local-models-focus-polish.md` (overall
  argument for open-source local inference as independence from commercial
  control). That note emphasizes ergonomic and capability reasons; this note
  adds a geopolitical access-risk reason. The combination of the two
  strengthens the case for open-source hedging in model strategy.

- **Contradicts**: None identified. No existing corpus note makes claims that
  would lead to directly opposing guide advice about AI access controls or
  geopolitical risk in model selection. No contradiction issue filed.

- **Novel**:
  - **Nationality as the defining AI access boundary**: No other corpus source
    documents the shift from capability-based or destination-country-based AI
    export controls to nationality-based controls. The Anthropic directive is
    the first documented instance; Ronacher's framing of it as a structural
    departure from prior control models is new to the corpus.
  - **"Access risk" as a model selection criterion**: Existing corpus source
    notes discuss model selection in terms of cost, capability, latency, and
    context window. No prior note adds access resilience (what happens if the
    provider's API is cut off by government directive) as a selection criterion.
    This post introduces that criterion with a concrete example.
  - **Open source as geopolitical hedge (not just cost/ergonomic hedge)**: Prior
    corpus notes on open-source and local models frame the case in terms of
    privacy, cost, latency, and infrastructure independence. The current post
    adds a political dimension: open-source models cannot be export-controlled
    after publication in the same way API-gated models can be restricted.
  - **EU structural dependency stack fully enumerated**: No prior corpus note
    catalogues the specific layers of EU dependency on US infrastructure (cloud
    → OS → developer platforms → AI → satellite internet). This is useful as a
    concrete checklist for practitioners doing infrastructure risk assessment.
  - **Member-state vs. EU-level failure distinction**: No prior corpus note
    distinguishes between EU-level regulatory burden and member-state-level
    structural friction. Ronacher's argument that the primary obstacles (company
    formation, equity, banking, KYC, notaries) are national-level problems
    misattributed to the EU is a useful framing for practitioners advising on
    European engineering organization setup.

## Guide Impact

- **Chapter 02 (Working with LLMs — Model Selection)**: Add access resilience
  as a model selection criterion alongside cost, capability, latency, and
  privacy. Claim 1 documents that API-gated closed models are subject to
  nationality-based access restrictions by government directive. Teams building
  on US frontier AI providers should understand this risk dimension and consider
  multi-provider strategies or open-source hedges. This post supplies the
  concrete first evidence. `blog-ronacher-local-models-focus-polish.md` Claim 14
  provides the corresponding technical path (local open-source inference).

- **Chapter 04 (Safety and Governance)**: Claim 2 documents that "AI safety"
  language maps to national security policy in practice. Practitioners advising
  on AI governance should distinguish between provider safety framing (universal,
  humanity-focused) and regulatory outcomes (nationality-based access control).
  The gap between stated values and policy outcomes is a concrete governance
  risk. Current chapter coverage on safety and governance likely focuses on
  model behavior and incident response, not on provider access risk — this post
  adds the latter.

- **Chapter 05 (Team Adoption — Structural Context)**: Claims 4–7 document
  the structural context in which European teams make AI-native engineering
  decisions: multi-layer US infrastructure dependency, member-state-level hiring
  and equity friction, and the talent drain dynamic. Teams operating in European
  contexts face structural constraints that are not present for US teams. Current
  chapter coverage likely treats adoption decisions as primarily cultural or
  organizational; this source adds the structural/geopolitical layer.

- **Chapter 07 (Open Source Approaches)**: Claims 9–10 frame open source as
  one of the few paths that does not naturally lead to total concentration of
  AI power, and note that access to open-source models carries a different
  (lower) geopolitical risk profile than access to API-gated closed models.
  If such a chapter exists or is planned, Ronacher's argument grounds the
  case for open-source investment in access resilience rather than just
  capability or cost.

## Extraction Notes

- Full post HTML was fetched from `https://lucumr.pocoo.org/2026/6/13/americans-only/`
  via `curl` and stripped of HTML markup for verbatim extraction. All quotes
  verified character-for-character against the raw HTML output.
- The post links to Anthropic's announcement at
  `https://www.anthropic.com/news/fable-mythos-access` (the export control
  directive described in Claim 1) and to several prior Ronacher posts
  (`/2026/6/10/gaslighting/`, `/2025/10/21/eu-resigation/`,
  `/2026/4/23/equity-for-europeans/`, `/2025/12/9/fixing-europe/`). These
  linked posts were not fetched for this note as they are about EU policy and
  personal experience rather than AI engineering patterns.
- This post is primarily strategic/political commentary rather than practitioner
  workflow analysis. The guide impact is at the strategy and governance level
  (model selection risk, team structure context, open source rationale), not at
  the harness engineering or daily workflow level.
- Three Prospector triage comments were included in the issue, with slightly
  different emphasis: high novelty (Ch01/Ch02/Ch04/Ch07), medium novelty
  (Ch05), and low novelty (Ch03/Ch05 tangential). The extraction covers all
  three angles but reflects the medium-novelty assessment as most accurate for
  the guide's practitioner scope — the claims are substantive and novel but
  their direct workflow implications require inference from the strategic
  argument.
- Confidence rated anecdotal overall: all claims originate from one practitioner's
  political analysis with no empirical data. The export control event itself is
  verifiable (Anthropic published the announcement); Ronacher's interpretation
  of its significance and his structural claims about Europe are normative and
  anecdotal.
- No contradiction issues filed: no existing corpus note makes claims opposed
  to the core arguments here.
