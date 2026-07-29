---
source_url: https://www.thoughtworks.com/insights/articles/Path-to-production-for-enterprise-AI
source_type: blog-post
title: "Path to production for enterprise AI: Moving beyond the experimentation trap"
author: Lenara Aliyeva, Sebastian Werner, and Maximilian Lammel
date_published: 2026-07-16
date_extracted: 2026-07-29
last_checked: 2026-07-29
status: current
confidence_overall: emerging
issue: "#2299"
---

# Path to Production for Enterprise AI: Moving Beyond the Experimentation Trap

> Thoughtworks Insights article proposing a four-gate stage-gate model
> (Compliance & Feasibility, Secure Sandbox, Production Readiness,
> Operational Handover) as the sequencing structure for moving an AI
> initiative from idea to production, backed by three linked third-party
> statistics on PoC failure rates and paired with a catalog of six named
> frameworks (Lean Value Tree, Three Horizons, discovery/experimentation
> practices, secure MVP, and a continuous-optimization loop) mapped to each
> stage.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, "Articles" category; published
  July 16, 2026; from the trusted feed `thoughtworks`). A ~1,300-word
  prescriptive/process piece with 8 section headings, three linked
  third-party statistics, and a named four-gate framework — no case study or
  named client engagement is included (contrast with
  `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`,
  which anchors its framework in two named, quantified client engagements).
- **Author credibility**: Co-authored by three named Thoughtworks staff —
  Lenara Aliyeva, Sebastian Werner, and Maximilian Lammel. No bio, title, or
  "about the author" text is present anywhere on the fetched page (checked
  via a targeted follow-up fetch specifically requesting author bio text;
  none was found beyond the bylined names with profile links). Two of the
  three authors (Aliyeva, Werner) are also two of the three co-authors,
  alongside Danilo Sato, of an earlier Thoughtworks Insights piece, "How to
  build the organizational muscle needed to scale AI beyond PoCs" (published
  January 9, 2026), which this article links to inline and which introduces
  the same Lean Value Tree and Three Horizons frameworks this article
  references — see Extraction Notes for detail on that companion piece.
- **Scope**: Covers the "PoC graveyard" problem (three linked failure
  statistics and four named technical/non-technical roadblocks), a
  three-part "impact on transformation" argument, a four-gate stage-gate
  model for the path to production, and a catalog of six named frameworks
  mapped one-to-one onto six delivery stages (strategic alignment,
  prioritization, discovery, experimentation, secure MVP, scale &
  continuous optimization). Does NOT cover: a named client case study,
  quantitative outcome data for the four-gate model itself (the linked
  statistics describe the *problem*, not the effectiveness of this
  article's proposed *solution*), specific tooling/platform names, or a
  defined accountability/legal model (contrast with
  `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`).

## Extracted Claims

### Claim 1: A standardized "Path to Production" is a repeatable operating model spanning the full lifecycle of an AI initiative — idea generation, prioritization, funding, discovery, and continuous production at scale — not merely an engineering delivery pipeline
- **Evidence**: Opening framing statement, presented as the article's central thesis before any supporting data is introduced.
- **Confidence**: emerging (a scoping/definitional claim, but the rest of the article elaborates it into a concrete, named four-gate structure rather than leaving it abstract)
- **Quote**: "This is far more than an engineering pipeline; it is a repeatable operating model that takes an enterprise AI initiative from idea generation and prioritization through funding, discovery and continuous production at scale."
- **Our assessment**: This framing — that "path to production" is an end-to-end operating model, not just a CI/CD-style technical pipeline — is the article's organizing claim and distinguishes its scope from a narrower deployment-pipeline reading of the term. It sets up the article's actual contribution (the four-gate model in Claim 5) as the operationalization of this definition.

### Claim 2: Enterprise AI initiatives fail to reach production at a high, externally-measured rate — nearly two-thirds of organizations remain stuck in the piloting phase (per McKinsey), Gartner predicts organizations will abandon 60% of AI projects through 2026 due to lack of AI-ready data, and organizations lose an average of 2.4% of annual revenue on AI initiatives that fail to scale
- **Evidence**: Three distinct third-party statistics, each hyperlinked in the source article to an external report (McKinsey's "The state of AI," a Gartner press release, and a CIO Dive article citing underlying survey data) — a notably higher rate of linked, named external sourcing than most other Thoughtworks pieces in this corpus, which typically cite third-party research without a link (contrast with `blog-thoughtworks-singh-hayer-stranger-core.md`'s unattributed "70% of technology budgets" figure).
- **Confidence**: emerging (each figure is attributed to a named, external, linked source rather than asserted by the article's own authors; this Miner did not follow the external links to verify the underlying McKinsey/Gartner/CIO Dive reports themselves, so the figures should be treated as accurately-cited-but-independently-unverified by this note)
- **Quote**: "McKinsey highlights that nearly two-thirds of organizations remain stuck in the piloting phase, while Gartner predicts that through 2026, organizations will abandon 60% of AI projects unsupported by AI-ready data."
- **Quote** (revenue loss): "recent data shows that organizations lose an average of 2.4% of their annual revenue on AI initiatives that fail to scale."
- **Our assessment**: This is the strongest evidentiary anchor in the article — three separate, named, hyperlinked statistics rather than a single vendor-asserted figure. It gives the corpus its first linked quantification of the "PoC graveyard" problem already asserted qualitatively elsewhere (see Cross-References).

### Claim 3: The "PoC graveyard" results from a mix of four technical and non-technical roadblocks — organizational misalignment and process rigidity (the "last mile" problem), poor evaluation and governance (subjective human judgment instead of automated evaluation), data and infrastructure gaps (fragmented, late-arriving data on legacy foundations), and prohibitive operational costs (a demo costs a few hundred dollars, but scaling to production can jump to thousands weekly)
- **Evidence**: Four named subsections, each with a one-to-two sentence elaboration, directly following the statistics in Claim 2.
- **Confidence**: emerging (a structured, named taxonomy of causes, consistent with practitioner experience described elsewhere in the corpus, but not independently validated against incident or survey data specific to each of the four categories)
- **Quote** (PoC graveyard naming): "The roadblocks behind this \"PoC graveyard\" are a mix of technical and non-technical factors."
- **Quote** (cost roadblock): "While a simple demo costs a few hundred dollars to spin up, scaling to production can jump to thousands weekly. Without early cost modeling, projects quickly become financially unviable."
- **Quote** (last-mile roadblock): "Traditional innovation, funding and portfolio management frameworks are simply too rigid and slow to match the fast-moving, iterative nature of AI."
- **Our assessment**: The cost roadblock (few-hundred-dollar demo vs. thousand-dollar-weekly production) is a specific, quotable order-of-magnitude figure not present elsewhere in this corpus's cost-management sourcing (compare `blog-thoughtworks-omahony-feature-token-budgets.md` and `blog-thoughtworks-vega-token-billing-lockin.md`, which discuss token/billing cost structures but not this demo-to-production cost-jump framing specifically). Useful as a concrete number for a guide section on why cost modeling must start early, not after a PoC succeeds.

### Claim 4: Lack of a standardized path to production stalls transformation through three specific mechanisms — paralysis by uncertainty across ideation, funding and execution; reinventing the wheel across disparate tech stacks; and spinning up solutions from scratch without a repeatable plan
- **Evidence**: Three named, bulleted impacts, each with a one-to-three sentence elaboration, under "The impact on AI initiatives and transformation."
- **Confidence**: emerging (a structured taxonomy consistent with the article's overall argument; asserted rather than measured against specific organizational case data)
- **Quote** (paralysis): "The bottleneck begins at the whiteboard. Without a repeatable framework, organizations struggle to prioritize use cases, prove commercial viability or secure predictable funding."
- **Quote** (reinventing): "Without centralized standards, teams choose tooling in a vacuum, leading to architectural fragmentation. Breakthroughs cannot easily be shared, creating isolated silos of code, knowledge and infrastructure."
- **Quote** (spinning up from scratch): "Lacking reusable blueprints or shared pipelines, every project becomes a one-off endeavor. This unpredictability balloons delivery costs, worsened by unoptimized token usage, and makes scaling impossible."
- **Our assessment**: The "spinning up from scratch" mechanism explicitly names "unoptimized token usage" as a cost driver of unrepeatable, one-off AI projects — a specific, checkable claim linking process immaturity to a token-cost consequence, which corroborates this corpus's existing token-cost-management sourcing without itself giving a number (contrast with the demo/production cost jump in Claim 3, which does).

### Claim 5: AI solutions require four sequential, increasing-rigor decision gates before additional investment is made — Gate 1 (Compliance & Feasibility): ownership, baseline business case, automated Preliminary Risk Assessment against regulations like GDPR and the EU AI Act; Gate 2 (Secure Sandbox): threat modeling and data access controls with sanitized realistic datasets before building the MVP; Gate 3 (Production Readiness): penetration testing, bias/safety validation, and final CISO sign-off; Gate 4 (Operational Handover): transition to automated MLOps monitoring for performance degradation, model drift, and continuous compliance — built on traditional product-led thinking (desirability, feasibility, viability) plus enterprise AI guardrails
- **Evidence**: Named four-gate framework, presented as the article's central organizing structure under "The path to production and a need for stage-gates," with a one-sentence definition per gate.
- **Confidence**: emerging (a specific, named, sequential decision-gate structure — more operationally concrete than a general "governance must be built in" prescription — but presented without a named client engagement or outcome data showing this exact four-gate sequence was deployed and produced a measured result)
- **Quote**: "AI solutions cannot simply drift into production. They need clearly defined decision points that validate business value, technical readiness and governance before additional investment is made. Those stage gates should be streamlined, automated to large extent and form part of the platform. This approach builds on traditional product-led thinking (desirability, feasibility and viability) while adding enterprise AI guardrails."
- **Quote** (Gate 1): "Gate 1 (Compliance & feasibility): Establishes ownership, validates the baseline business case and runs automated Preliminary Risk Assessments (PRA) against regulations like GDPR and the EU AI Act."
- **Quote** (Gate 2): "Gate 2 (Secure sandbox): Focuses on threat modeling and data access controls to ensure the environment is fully isolated, utilizing sanitized, realistic datasets before building the MVP."
- **Quote** (Gate 3): "Gate 3 (Production readiness): Requires penetration testing, use-case-specific bias and safety validation and final CISO sign-off to harden the solution for live enterprise data."
- **Quote** (Gate 4): "Gate 4 (Operational handover): Transitions to automated MLOps monitoring to track performance degradation, model drift and continuous compliance."
- **Our assessment**: This is the article's core contribution and the answer to the Prospector's key question — a named, sequential, four-gate decision structure for the specific transition from experimentation to production, which is genuinely new sequencing content not present in the two overlapping Thoughtworks notes the Prospector flagged (see Cross-References → Novel). It is prescriptive and unvalidated by a case study, so it should be cited as a proposed structure, not a proven one.

### Claim 6: Each stage of the path to production is accelerated by a distinct named framework — Lean Value Tree (LVT) for strategic alignment (breaking boardroom mandates into measurable initiatives), the Three Horizons model for prioritization (balancing near-term wins with long-term ambition), phase mapping for discovery, hypothesis-driven prototyping for experimentation (finding the "good enough" point to move to product build), prescribed cloud-native runtimes and unified orchestration for secure MVP, and a continuous optimization loop for scale
- **Evidence**: Six named subsections under "Solid frameworks to accelerate the journey," each mapping one framework to one delivery stage.
- **Confidence**: emerging (a named catalog of established frameworks — LVT and Three Horizons are pre-existing methodologies the article did not originate, per the companion January 2026 Thoughtworks piece described in Extraction Notes — presented as a coherent stage-by-stage mapping)
- **Quote** (LVT): "The Lean Value Tree (LVT) framework breaks down boardroom mandates into actionable initiatives with measurable value, helping deploy strategy responsibly."
- **Quote** (Three Horizons): "The Three Horizons model identifies the most viable initiatives, helping leadership balance near-term quick wins with long-term transformative ambition."
- **Quote** (Experimentation): "Controlled prototyping and hypothesis-driven development find what resonates with users, determining the exact \"good enough\" point to move to product build."
- **Our assessment**: This catalog is useful as a map of *which* named methodology applies at *which* stage, but each framework is described in a single sentence with no further mechanical detail in this article — a reader would need to follow the article's own inline links (to separate Thoughtworks pieces on LVT, discovery, hypothesis-driven development, and pseudo-MVP pitfalls) to get operational detail. This note does not extract those linked pieces' content; see Extraction Notes.

### Claim 7: The "scale & continuous optimization" stage is not passive maintenance — it is an active optimization loop in which teams capture production traffic to continuously build new evaluation benchmarks (evals), iteratively tune AI agents, and safely test lower-cost models to maximize ROI
- **Evidence**: Direct statement under "Scale & continuous optimization," the final stage in the six-stage framework catalog.
- **Confidence**: emerging (a specific, actionable operational pattern — production-traffic-to-eval-to-model-swap — presented as a single-paragraph description without a named example or measured cost-reduction outcome)
- **Quote**: "Shifting from passive maintenance to an active optimization loop. By capturing production traffic, teams continuously build new evaluation benchmarks (evals) to iteratively tune AI agents, making the system more efficient and allowing organizations to safely test lower-cost models to maximize ROI."
- **Our assessment**: This is a specific, actionable pattern — production traffic becomes the raw material for new evals, and those evals become the safety net for testing cheaper models — that is more concrete than this corpus's existing evaluation-framework sourcing (`blog-thoughtworks-anand-agent-evaluation-framework.md`) on the specific question of *how* an eval suite should grow after launch. No prior corpus source states this production-traffic-to-eval-to-cost-optimization loop this explicitly.

### Claim 8: Technology is rarely the primary blocker to enterprise AI reaching production; the bigger challenge is organizational — connecting existing, often-mature engineering, governance, and delivery capabilities into a repeatable operating model, since most enterprises already have mature technology platforms, data governance, and MLOps practices but need these to work together with new AI-specific capabilities (evaluation, governance, operational cost management)
- **Evidence**: Direct statement under "The impact on AI initiatives and transformation," attributed to the authors' own client-engagement experience ("Through our work with clients, we find...").
- **Confidence**: emerging (a first-person practitioner assertion drawn from unspecified client engagements, not a survey or named case; consistent with, and now a fourth independent voice supporting, the same structural claim elsewhere in this corpus — see Cross-References)
- **Quote**: "Through our work with clients, we find that technology is rarely the primary blocker. The bigger challenge is organizational: enterprises struggle to connect existing engineering, governance and delivery capabilities into a repeatable operating model."
- **Quote** (foundations): "Many organizations already have mature technology platforms, data governance and MLOps practices. Enterprise AI builds on these foundations, but requires them to work together with new capabilities such as AI evaluation, governance and operational cost management."
- **Our assessment**: This directly corroborates the "not-a-technology-problem" thesis already documented twice in this corpus from other Thoughtworks-adjacent voices (see Cross-References) — this is now a third independent Thoughtworks-sourced statement of the same underlying claim, strengthening (without proving) the pattern that Thoughtworks' own practitioners consistently attribute enterprise AI's production gap to organizational rather than technical causes.

### Claim 9: Willingness and talent are not the primary bottleneck to enterprise AI adoption either — while specialized AI talent is scarce, many employees are genuinely eager to adopt tools that make their daily work faster and more efficient
- **Evidence**: Direct statement immediately following Claim 8, ruling out a second candidate root cause (employee resistance/talent shortage) before naming the actual bottleneck (lack of a standardized path to production).
- **Confidence**: anecdotal (an assertion with no survey data, adoption-rate figures, or named source given for either the "talent is scarce" or "employees are eager" halves of the claim)
- **Quote**: "Willingness is rarely the bottleneck either; while specialized AI talent is scarce, many employees are genuinely eager to adopt tools that make their daily tasks faster and more efficient."
- **Our assessment**: This is a minor supporting claim (ruling out a second candidate explanation) rather than a load-bearing one, and is the weakest-evidenced claim in the article — no data backs either half. Useful only as color for a guide section addressing "is resistance to AI tools the real problem?" with an appropriately anecdotal-confidence caveat.

### Claim 10: Standardization of the path to production is what enables faster, consistent value realization at scale; Thoughtworks recommends a "thin-slice" approach supported by client-tested templates to help organizations establish this path quickly while reducing delivery risk
- **Evidence**: Closing statement under "Conclusion: Faster value realisation through standardization," naming the authors' own firm's recommended methodology.
- **Confidence**: emerging (a vendor's own recommended approach, named but not elaborated mechanically within this article; the "thin-slice" term is also used, with more detail, in the companion January 2026 Thoughtworks piece by two of the same three authors — see Extraction Notes)
- **Quote**: "Standardization reduces unnecessary variation and uncertainty across AI delivery. By defining a clear path to production that integrates governance, funding and engineering practices, organizations can move beyond experimentation and deliver value consistently at scale."
- **Quote** (thin-slice): "At Thoughtworks, we use a thin-slice approach supported by client-tested templates to help organizations establish this path quickly while reducing delivery risk."
- **Our assessment**: This is the article's closing call to action and a vendor-positioning statement (Thoughtworks selling its own methodology and templates) rather than new evidentiary content — the "thin-slice" term is asserted without this article defining what specifically it means beyond "supported by client-tested templates." The companion January 2026 piece (Extraction Notes) defines "thin slice" more concretely as "focus[ing] on discrete elements needed for specific use cases rather than comprehensive transformation" — readers of this article alone would not get that fuller definition.

## Concrete Artifacts

### The four stage gates (verbatim, as published)

```
Source: Lenara Aliyeva, Sebastian Werner, Maximilian Lammel, "Path to
production for enterprise AI: Moving beyond the experimentation trap,"
Thoughtworks Insights, July 16, 2026

Gate 1 (Compliance & feasibility): Establishes ownership, validates the
baseline business case and runs automated Preliminary Risk Assessments
(PRA) against regulations like GDPR and the EU AI Act.

Gate 2 (Secure sandbox): Focuses on threat modeling and data access
controls to ensure the environment is fully isolated, utilizing sanitized,
realistic datasets before building the MVP.

Gate 3 (Production readiness): Requires penetration testing, use-case-
specific bias and safety validation and final CISO sign-off to harden the
solution for live enterprise data.

Gate 4 (Operational handover): Transitions to automated MLOps monitoring
to track performance degradation, model drift and continuous compliance.
```

### The four roadblocks behind the "PoC graveyard"

```
Source: as above

1. Organizational misalignment and process rigidity (the "last mile"
   problem) — traditional innovation, funding and portfolio management
   frameworks are too rigid and slow for AI's iterative pace.
2. Poor evaluation and governance — subjective human judgment during
   testing, rather than automated evaluations, leads to failures when
   models encounter real-world complexity.
3. Data and infrastructure gaps — data is fragmented, arrives late, and
   sits on unstable legacy foundations that cannot support real-time
   streaming or low-latency requirements.
4. Prohibitive operational costs — a demo costs a few hundred dollars to
   spin up; scaling to production can jump to thousands weekly.
```

### The six-stage framework catalog

```
Source: as above

Strategic alignment       -> Lean Value Tree (LVT)
Prioritization             -> Three Horizons model
Discovery                  -> Early phase mapping of technical/operational
                               problem spaces
Experimentation             -> Controlled prototyping, hypothesis-driven
                               development
Secure MVP                  -> Prescribed cloud-native runtimes, unified
                               orchestration layers
Scale & continuous
optimization                 -> Active optimization loop: capture
                               production traffic, build new evals,
                               iteratively tune agents, test lower-cost
                               models
```

### Three linked failure/cost statistics

```
Source: as above (each hyperlinked in the original article to an external
report)

- "nearly two-thirds of organizations remain stuck in the piloting phase"
  (cited to McKinsey)
- "organizations will abandon 60% of AI projects unsupported by AI-ready
  data" through 2026 (cited to Gartner)
- "organizations lose an average of 2.4% of their annual revenue on AI
  initiatives that fail to scale" (cited to a CIO Dive-linked data source)
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md`,
`blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`, and
`blog-thoughtworks-lad-platform-business-value.md` were re-read directly
(MINER.md §4b) and claim numbers below were confirmed against those notes'
numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md` Claim 2
    ("from a technical perspective, the technology already exists... the
    harder part is everything around it: governance, data, architecture,
    accountability and the operating model"): This article's Claim 8
    ("technology is rarely the primary blocker... the bigger challenge is
    organizational") is an independent, third convergence (after Mohanty,
    and Squeo/Kamelman below) on the same structural claim — enterprise
    AI's production gap is organizational, not technical.
  - `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`
    Claim 1 ("Most enterprise AI initiatives aren't failing because the
    model is weak; they're failing because the organization hasn't built
    the operating system required to govern, scale and learn from
    AI-enabled work"): This article's Claim 8 makes the same claim in
    different vocabulary ("connect existing engineering, governance and
    delivery capabilities into a repeatable operating model" vs. "build the
    operating system"), giving the corpus a fourth named Thoughtworks-
    adjacent voice (after Mohanty, Gordon/Kamelman's parallel argument, and
    Squeo/Kamelman) asserting the enabling technology is not the enterprise
    AI bottleneck.

- **Contradicts**: None found and none filed. No claim in this article
  materially opposes a claim in the two Prospector-flagged overlapping
  notes or in `blog-thoughtworks-lad-platform-business-value.md`; where
  topics overlap (the organizational-not-technical bottleneck; the value of
  standardized process; funding as a gating step), this article's claims
  are consistent extensions or restatements, not disagreements. This
  article's stage-gate model (governance rigor increases through four
  sequential gates before production) is also consistent with, not opposed
  to, the "governance must be built in from the start, not retrofitted"
  framing in `blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md`
  Claim 4 — the stage-gate model is one way of operationalizing "built in
  from the start" as a sequence of checkpoints rather than a single
  up-front decision.

- **Extends**:
  - `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`:
    That article's four-layer harness taxonomy (model / builder / user /
    organizational, Claim 2) and five organizational-harness capabilities
    (Claim 6) describe *what* an enterprise AI operating system must
    contain, but not *when*, in what sequence, or against what decision
    points it should be built and validated relative to funding and
    business-case development. This article's four-gate model (Claim 5)
    supplies exactly that missing temporal/process sequencing — Gate 1's
    automated Preliminary Risk Assessment and baseline business case
    roughly precede the builder-harness work; Gate 2's threat modeling and
    isolated sandbox correspond to early builder/user-harness construction;
    Gate 3's penetration testing and CISO sign-off harden the user harness
    for production; Gate 4's automated MLOps monitoring is the
    organizational harness's ongoing "steering loop" (that article's Claim
    6) in operation. This is the specific novel contribution the
    Prospector's triage comment asked the Miner to identify.
  - `blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md`: That
    article argues governance must be built into the operating
    environment's "original DNA" (Claim 4) as abstract advice, without
    naming a concrete mechanism for what "built in from the start" means
    procedurally. This article's Gate 1 (automated Preliminary Risk
    Assessment against GDPR/EU AI Act, run before an MVP is built) is a
    concrete instance of what "built in from the start" looks like as an
    actual, named, sequenced process step.
  - `blog-thoughtworks-lad-platform-business-value.md` Claim 9 ("Time-to-
    value (TTV)... platform engineering reduces the friction of development
    and allows development teams to reduce their time to value... the days
    / weeks / months saved in a path to production directly results in the
    business' ability to capture market opportunities"): That article
    argues platform teams should frame funding asks in TTV/market-share
    terms but does not itself define a path-to-production structure. This
    article's "value-driven portfolio management" and "lean funding
    process" (preceding the four gates) is a specific instantiation of the
    funding step Lad's article argues platform teams need better data to
    justify.

- **Novel**:
  - **The four-gate stage-gate model itself** (Gate 1: Compliance &
    Feasibility; Gate 2: Secure Sandbox; Gate 3: Production Readiness;
    Gate 4: Operational Handover, Claim 5): No prior corpus source
    describes a named, sequential set of decision gates for the specific
    transition from AI experimentation to production. This is the
    prescriptive "path/sequencing/phase" content the Prospector's triage
    comment explicitly asked the Miner to look for.
  - **Three linked, named third-party failure/cost statistics** (McKinsey
    two-thirds-stuck-in-piloting; Gartner 60%-abandoned-by-2026; 2.4%
    average revenue loss, Claim 2): A more rigorously (hyperlinked) sourced
    quantification of the "PoC graveyard" problem than this corpus's prior
    Thoughtworks sourcing typically provides.
  - **The demo-to-production cost jump figure** ("a simple demo costs a few
    hundred dollars to spin up, scaling to production can jump to thousands
    weekly," Claim 3): A specific order-of-magnitude number not present
    elsewhere in this corpus's cost-management sourcing.
  - **The production-traffic-to-eval-to-cost-optimization loop** (Claim 7):
    A specific, actionable pattern for how an evaluation suite should grow
    after launch and be used to justify testing cheaper models, more
    concrete than this corpus's existing evaluation-framework sourcing on
    this specific question.
  - **The six-stage framework catalog mapping named methodologies (LVT,
    Three Horizons, hypothesis-driven development, etc.) to specific
    delivery stages** (Claim 6): New as an explicit stage-by-stage map,
    though the individual frameworks themselves (LVT, Three Horizons) are
    not new to Thoughtworks' own published output — see Extraction Notes on
    the companion January 2026 piece.

## Guide Impact

- **Chapter 04 (Production Patterns)**: Add the four-gate stage-gate model
  (Claim 5) as a concrete, named sequencing structure for how organizations
  should move an AI initiative from experimentation to production. This
  fills a gap in the guide's existing enterprise-AI sourcing: prior notes
  (Marr/Mohanty, Squeo/Kamelman) describe governance layers and
  organizational structure but not the temporal/process sequence for
  getting there. Recommend citing this article's four gates alongside
  `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`'s
  four-layer harness taxonomy as a "what to build" (harness layers) plus
  "when to check it" (stage gates) pairing.

- **Chapter 05 (Team Adoption — Organizational Readiness)**: Add the three
  linked failure statistics (Claim 2) as a stronger-than-usual quantified
  problem statement for a chapter introduction on why standardized AI
  delivery process matters, and the four roadblocks (Claim 3) as a
  diagnostic checklist readers can use to classify why their own AI
  initiative may be stalled (organizational rigidity, evaluation/governance
  gaps, data/infrastructure gaps, or cost-modeling gaps).

- **Chapter 02 or wherever evaluation/eval-suite practices are discussed**:
  Add the "scale & continuous optimization" loop (Claim 7) — capturing
  production traffic to continuously build new evals, then using those
  evals to safely test lower-cost models — as a specific, actionable
  pattern for post-launch evaluation-driven cost optimization, alongside
  `blog-thoughtworks-anand-agent-evaluation-framework.md`.

## Extraction Notes

1. **Full article text obtained via WebFetch in two passes.** The first
   WebFetch call returned what reads as the article's complete body text
   (byline, all section headings, and body paragraphs matching the
   published section structure). A second, targeted follow-up call
   requested character-for-character verbatim quotes for seven specific
   passages (McKinsey/Gartner/revenue statistics, Gate 1, Gate 4, the
   thin-slice conclusion, and the byline/date) to cross-check against the
   first pass; all seven matched the first pass's wording exactly. A third
   targeted call verified Gate 2, Gate 3, the "PoC graveyard" naming
   sentence, the demo-cost sentence, and the scale/optimization sentence,
   again matching the first pass exactly. All quotes in this note are drawn
   from these consistent, cross-checked passages. The Assayer should
   spot-check quotes against the live URL, as with other WebFetch-sourced
   notes in this corpus.

2. **The article's three failure statistics are hyperlinked to external
   reports in the source markdown** (McKinsey's "The state of AI," a
   Gartner press release dated 2025-02-26, and a CIO Dive article). This
   Miner did not follow those three external (non-Thoughtworks) links to
   verify the underlying McKinsey/Gartner/CIO Dive claims themselves — per
   MINER.md §1, sub-page following is scoped to up to 5 *linked pages that
   seem substantive* to understanding this source's own claims; these three
   links point to independent third-party research reports outside
   Thoughtworks' site, which is a different kind of follow than the
   in-corpus convention of following a source's own linked sub-pages. The
   Claim 2 confidence rating (`emerging`, not `settled`) reflects this: the
   figures are attributed and linked, but independently unverified by this
   note.

3. **One inline-linked companion piece was followed and is significant for
   novelty assessment.** The article links inline to "How to build the
   organizational muscle needed to scale AI beyond PoCs" (Thoughtworks
   Insights, published January 9, 2026), co-authored by two of this
   article's three authors (Lenara Aliyeva, Sebastian Werner) plus Danilo
   Sato. A targeted WebFetch summary of that piece found it introduces the
   same Lean Value Tree and Three Horizons frameworks this article
   references (Claim 6), plus a five-building-block model (business
   alignment, technology foundations, repeatable production pathways,
   cross-functional product teams, sustained adoption) and the same
   "thin-slice" terminology used in this article's conclusion (Claim 10) —
   but that January piece does **not** contain the four-gate stage-gate
   structure (Gate 1–4) that is this article's central, novel contribution.
   This confirms the four-gate model is new content introduced between
   January and July 2026, not a restatement of the earlier piece. This
   January 2026 companion piece does not currently have a source note in
   this corpus (checked via grep for "organizational muscle," "Aliyeva,"
   and "Danilo Sato" across `source-notes/` — no matches); it is flagged
   here for the Prospector/Smith's awareness as a plausible future source,
   but filing a new source-submission issue for it is outside this Miner's
   scope for issue #2299.

4. **Five other inline-linked pages were not individually fetched.** The
   article links inline to five additional Thoughtworks explainer pieces
   corresponding to the framework catalog in Claim 6 ("How to run a
   successful discovery," "How to implement Hypothesis-Driven Development,"
   "How to avoid the pitfalls of the pseudo-MVP," "MLOps culture and
   automation are key to scalable machine learning," and "How to brew a
   perfect strategy, responsibly" for LVT). Given the budget for this
   extraction and that this article's own text already states each
   framework's one-sentence role at its corresponding stage (quoted in
   Claim 6), these five were not deep-read; a future Miner pass on any of
   them individually would extract framework mechanics this note does not
   cover.

5. **No contradiction found or filed.** This article's claims are
   consistent extensions of, not disagreements with, the two
   Prospector-flagged overlapping notes and `blog-thoughtworks-lad-platform-business-value.md`;
   see Cross-References → Contradicts for the specific reasoning.

6. **Overall confidence rated "emerging."** The article's linked, named
   third-party statistics (Claim 2) are stronger sourcing than this
   corpus's typical Thoughtworks think-piece (most cite third-party
   research without a link, or assert figures with no attribution at all).
   The four-gate stage-gate model and framework catalog are coherent,
   specific, and delivered by three named practitioners citing their own
   client-engagement experience, but — unlike
   `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`,
   which anchors its framework in two named, quantified client case studies
   — this article provides no case study or outcome data demonstrating the
   four-gate model itself has been deployed and produced a measured result.
   This caps the rating below `settled` while placing it above `anecdotal`
   given the quality of the problem-statement sourcing.
