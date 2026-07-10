---
source_url: https://www.thoughtworks.com/insights/blog/data-strategy/why-ontologies-matter-fail-build-anyway
source_type: blog-post
title: "Why ontologies matter, why they fail and how to build them anyway"
author: Nimisha Asthagiri (Head of Advanced Analytics & AI, Thoughtworks North America)
date_published: 2026-06-17
date_extracted: 2026-07-10
last_checked: 2026-07-10
status: current
confidence_overall: emerging
issue: "#1712"
---

# Why Ontologies Matter, Why They Fail and How to Build Them Anyway

> Thoughtworks essay arguing that ontologies matter for agentic AI because
> LLMs can read documents but do not hold an organization's operating logic,
> diagnosing three recurring failure modes in ontology programs (translation
> gap, scope creep, maintenance decay), and prescribing "treat the ontology
> as a product, not a project" as the practice that survives contact with
> production.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, published June 17, 2026)
- **Author credibility**: Nimisha Asthagiri, Head of Advanced Analytics & AI
  at Thoughtworks North America. Practitioner/consultant voice writing for a
  known enterprise-consulting outlet on a topic (semantic data architecture)
  central to her stated role. No named client case study, no metrics, no code
  — the piece is conceptual/prescriptive, generalized from unnamed engagement
  experience rather than a single documented deployment. Thoughtworks is
  already a trusted signal source in this corpus (multiple prior source notes
  from Thoughtworks Insights authors).
- **Scope**: Covers why the schemas → controlled vocabularies → semantic
  layers → ontologies → knowledge graphs continuum matters for agentic AI,
  three concrete benefits (retrieval, guardrails, shared language), three
  recurring failure modes of ontology programs, and five practices for
  building ontologies as a product. Does NOT cover a specific company's
  ontology, does NOT provide code/schema examples, does NOT provide metrics
  or a controlled before/after comparison, and does NOT discuss
  retrieval-augmented generation (RAG) as an alternative or complement.

## Extracted Claims

### Claim 1: LLMs can read an organization's documents but do not hold its operating logic (business rules, policies, conventions)
- **Evidence**: Framing assertion opening the article's argument for why
  ontologies matter to agentic systems specifically, as distinct from
  document-retrieval systems.
- **Confidence**: settled (this is the now-common industry framing that
  parametric/document knowledge and structured operational knowledge are
  distinct classes of information an LLM system needs)
- **Quote**: "A language model can read your documents, but it doesn't hold your operating logic."
- **Our assessment**: This is the article's thesis sentence and the
  justification for everything that follows. It correctly separates two
  different failure surfaces: hallucination from lacking facts (addressed by
  retrieval) versus incorrect action from lacking rules/constraints
  (addressed by structured operational knowledge like ontologies). This
  distinction is useful for the guide because teams often reach for more
  retrieval when the actual gap is missing operating logic.

### Claim 2: Schemas, controlled vocabularies, semantic layers, ontologies, and knowledge graphs sit on a single continuum rather than being competing choices
- **Evidence**: Structural framing of the article's middle section, used to
  argue teams should pick the minimum structure needed rather than defaulting
  to "ontology" as the answer to every semantic problem.
- **Confidence**: emerging (a framing/taxonomy claim, not an empirically
  tested one, but consistent with standard data-architecture literature)
- **Quote**: "Schemas, controlled vocabularies, semantic layers, ontologies and knowledge graphs all sit on one continuum."
- **Our assessment**: This reframes "should we build an ontology?" as "how
  far along this continuum does our use case actually require us to go?" —
  a more actionable question than a binary build/don't-build decision. It
  also implicitly argues against reflexively over-building (see Claim 8,
  scope creep).

### Claim 3: An ontology is the blueprint (classes, relationships, rules); a knowledge graph is that blueprint populated with real data and is what an agent actually queries
- **Evidence**: Direct definitional distinction given in the article.
- **Confidence**: settled (standard semantic-web/data-architecture
  terminology, not a novel claim)
- **Quote**: "An ontology is a blueprint: the classes, the relationships and the rules." / "A knowledge graph is that blueprint populated with your actual data; it's also the thing an agent actually queries."
- **Our assessment**: This distinction matters for the guide because it
  clarifies a common conflation: teams sometimes believe designing the
  ontology (the schema) is the deliverable, when the artifact an agent
  actually depends on operationally is the populated knowledge graph. This
  sets up Claim 4 (population, not schema design, is where the value and the
  difficulty live).

### Claim 4: The retrieval benefit of ontologies comes from a populated, entity-resolved graph, not from the schema itself — population is the hard part
- **Evidence**: Description of how structured graphs improve retrieval by
  letting an agent traverse defined relationships instead of relying on
  embedding similarity, paired with an explicit caveat that this value
  requires entity resolution and relationship extraction against real data.
- **Confidence**: emerging (a design-principle claim; plausible and
  consistent with known limitations of pure vector retrieval, but not backed
  by a comparative metric in the article)
- **Quote**: "Pairing unstructured text with a structured graph lets an agent follow defined relationships instead of guessing from surface similarity."
- **Our assessment**: The important qualifier here is that traversal-based
  retrieval only works once entities are resolved and relationships are
  extracted against real data — the ontology schema alone doesn't deliver
  the benefit. This is a useful corrective for teams that treat schema design
  as "done" and skip the population/maintenance work, which directly sets up
  the article's Claim 7 (maintenance problem).

### Claim 5: Ontology-based guardrails only bind agent behavior when a deterministic runtime actually checks the rule and the check is demonstrable
- **Evidence**: Description of the "guardrails" benefit, qualified with a
  condition on enforcement mechanism rather than presence of the rule.
- **Confidence**: emerging (a design-principle claim without a cited
  incident or metric, but aligned with a broader pattern in this corpus of
  deterministic-enforcement-over-policy-instruction — see Cross-References)
- **Quote**: "A rule only binds when a deterministic runtime checks it and respects the answer and when you can show the check actually happened."
- **Our assessment**: This is functionally the same architectural claim as
  Kepler's deterministic-execution-layer pattern (see Cross-References,
  Corroborates), applied specifically to ontology-encoded rules rather than
  computation. An ontology stating "an agent may not do X" is not itself a
  guardrail; the guardrail is the runtime enforcement plus an auditable
  record that the check ran. This is an important calibration for Ch03: an
  ontology is necessary-but-not-sufficient for governance — it supplies the
  rule content, not the enforcement.

### Claim 6: A shared ontology maps different departments' terminology to a common reference, but the model goes stale within two quarters without an assigned steward and regular reconciliation
- **Evidence**: Description of the "shared language" benefit, immediately
  qualified with a specific staleness timeline tied to absence of ownership.
- **Confidence**: anecdotal (the "two quarters" figure reads as a
  practitioner rule-of-thumb from consulting engagements rather than a
  measured statistic; no methodology given)
- **Quote**: "Without a steward and a regular reconciliation, the model goes stale within two quarters."
- **Our assessment**: The specific timeframe is not independently verifiable
  and should be treated as an illustrative order-of-magnitude claim (a
  couple of quarters, not years) rather than a precise measurement. The
  underlying mechanism — that a semantic model decays without an assigned
  owner and a reconciliation cadence — is the more load-bearing and better
  supported part of the claim; it recurs as the article's core failure mode
  (Claim 7) and is corroborated elsewhere in this corpus (see
  Cross-References).

### Claim 7: Ontology programs fail for three recurring reasons: a translation gap between ontology engineers and subject-matter experts, scope creep from trying to model the whole enterprise, and a maintenance problem where the model can't keep pace with organizational change
- **Evidence**: The article's central diagnostic section, presented as three
  named, distinct failure modes rather than a single generic "ontologies are
  hard" claim.
- **Confidence**: emerging (practitioner-derived pattern from unnamed
  consulting experience; no case count or failure-rate statistic given, but
  each mode is described with a specific mechanism, not just asserted)
- **Quote**: "Ontology engineers know the formalism but not your business; subject matter experts know the business but not formal modeling." / "Because the model describes reality, teams are tempted to model all of it before shipping anything. Those projects tend to die after a year." / "Compliance shifts, teams reorganize, products evolve and all of it moves faster than a hand-maintained model can keep up with."
- **Our assessment**: This is the most guide-actionable content in the
  article: three distinct, independently-diagnosable failure modes, each
  with a different fix (translation gap → pair engineers with SMEs or use
  LLM-assisted drafting per Claim 9; scope creep → scope to one use case per
  Claim 8; maintenance problem → assign ownership and reconciliation cadence
  per Claim 6). Treating "ontology programs fail" as one undifferentiated
  risk would be less useful than this three-way split for diagnosing why a
  specific program is struggling.

### Claim 8: The ontology practice that survives production is one where the ontology is treated as a product with an owner, not a one-time modeling project
- **Evidence**: The article's stated central thesis, presented as the
  synthesis of the three failure modes in Claim 7.
- **Confidence**: emerging (a prescriptive framing claim, not independently
  measured, but it is the article's core argument and is consistent with
  general "data-as-a-product" thinking applied to semantic models)
- **Quote**: "The ontology that survives contact with the real world is one where an ontology is treated as a product rather than a project."
- **Our assessment**: This is the article's title thesis and functions as
  the organizing principle for its five concrete practices (Claim 9). It is
  a reframing rather than a new mechanism — "treat X as a product" is a
  familiar pattern from data-mesh/data-product literature — but applying it
  specifically to ontologies, with the three named failure modes as the
  motivating evidence, is the article's contribution.

### Claim 9: Building ontologies as a product means scoping to one funded use case, using "competency questions" as a funding gate, drafting taxonomies from existing schemas via LLM pipelines rather than from scratch, assigning clear ownership with versioning/reconciliation cycles, and making deliberate build-vs-buy decisions
- **Evidence**: The article's prescriptive practices section, listed as
  concrete steps rather than general advice.
- **Confidence**: emerging (practitioner recommendations; plausible and
  specific, but not validated against a documented before/after outcome in
  this article)
- **Quote**: "Make competency questions a funding gate. Before anyone models a single class, ask the business to name the precise questions the system cannot answer today, and tie each one to a decision or a dollar." / "Curate, don't draft from scratch. Use LLM pipelines to pull draft taxonomies from your existing schemas, API definitions and wikis."
- **Our assessment**: The "competency questions as a funding gate" practice
  is the most directly actionable item: it forces the business to name the
  specific unanswerable question and its dollar/decision stake *before* any
  modeling work starts, which is a concrete countermeasure to the scope-creep
  failure mode (Claim 7). The "curate, don't draft from scratch" practice —
  using LLM pipelines to extract draft taxonomies from existing schemas, API
  definitions, and wikis — is notable as a specific agentic-AI-native
  technique for addressing the translation-gap failure mode: it substitutes
  LLM-assisted extraction for the slow manual hand-off between engineers and
  SMEs. This is the article's most concrete "AI helping build the AI's own
  operating logic" pattern.

### Claim 10: The effective stance on ontologies is a narrow middle ground: build the smallest semantic structure that answers a funded question, own it as a product, and expand only when the next funded question requires it
- **Evidence**: The article's concluding synthesis, explicitly rejecting both
  the "model all of reality" extreme and the "retrieval over documents is
  good enough" extreme.
- **Confidence**: emerging (prescriptive synthesis claim; the article's own
  conclusion, not independently validated)
- **Quote**: "The most effective stance sits between two extremes. It's not the academic hunt for a complete model of the enterprise and it's not the assumption that retrieval over a pile of documents is good enough. It's something narrower and more practical: build the smallest semantic structure that answers a funded question, own it as a product and expand it only when the next funded question asks you to."
- **Our assessment**: This closing framing directly connects Claim 2 (the
  stack-not-a-switch continuum) with Claim 9 (competency-question funding
  gate): the "smallest semantic structure that answers a funded question" is
  the operational rule for how far up the continuum a team should go for any
  given use case, rather than defaulting to "ontology" or "knowledge graph"
  as the assumed target. This is a useful anti-over-engineering heuristic for
  Ch04 guidance on semantic/context infrastructure investment.

## Concrete Artifacts

```
Semantic structure continuum (Thoughtworks, Asthagiri, June 2026)
Source: "Why ontologies matter, why they fail and how to build them anyway"

Schemas → Controlled vocabularies → Semantic layers → Ontologies → Knowledge graphs
  (paraphrase of the article's continuum framing; the article states these
   "all sit on one continuum" running, per the article, from how data is
   stored to what it means to what a machine can reason and act on)

Three named benefits:
  1. Better retrieval (via graph traversal vs. surface/embedding similarity;
     requires entity resolution + relationship extraction against real data)
  2. Guardrails for agents (a model of permissible actions; only binds when
     a deterministic runtime checks it and the check is demonstrable)
  3. Shared language across teams (maps departmental dialects to a common
     reference; decays without a steward and reconciliation cadence)

Three named failure modes:
  1. Translation gap (ontology engineers know formalism, not the business;
     SMEs know the business, not formal modeling)
  2. Scope creep (modeling all of reality before shipping anything; these
     projects "tend to die after a year")
  3. Maintenance problem (compliance/org/product change outpaces a
     hand-maintained model)

Five product-building practices:
  1. Scope to a single high-return use case, not the enterprise
  2. Competency questions as a funding gate (before modeling starts, name
     the precise unanswerable question and tie it to a decision/dollar)
  3. Curate, don't draft from scratch — use LLM pipelines to pull draft
     taxonomies from existing schemas, API definitions, and wikis
  4. Assign clear ownership with versioning and reconciliation cycles
  5. Make deliberate build-vs-buy decisions
```

## Cross-References

- **Corroborates** `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 5
  (a proprietary financial ontology mapping concepts to precise definitions
  is a prerequisite content-engineering artifact for production financial
  AI): Kepler's case study is a positive instance of exactly what this
  article warns is fragile — a curated ontology as load-bearing
  infrastructure. This article supplies the failure modes (translation gap,
  scope creep, maintenance decay) and product practices that the Kepler note
  does not discuss; the Kepler note does not describe how its ontology is
  governed, staffed, or kept current, which is precisely the gap this
  article's "treat it as a product" prescription (Claim 8) addresses.
- **Corroborates** `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 3
  (Claude is treated as one stage in a pipeline — the surrounding
  deterministic infrastructure is as load-bearing as the model itself, so
  "the model output can structurally never be the final number... the
  architecture enforces it, not a policy"): this article's Claim 5 (a rule
  only binds when a deterministic runtime checks it) is the same
  architectural principle — a model or ontology stating a rule is not itself
  enforcement — applied to ontology-encoded guardrails specifically rather
  than to financial computation.
- **Corroborates** `blog-anthropic-selfservice-data-analytics.md` Claim 10
  (the semantic layer is the highest-reliability source of truth, yielding
  the same single metric value across all company surfaces): both sources
  independently identify the semantic layer / ontology tier as the
  authoritative reference an agent should query rather than re-deriving
  answers ad hoc. The self-service-analytics note documents a working
  implementation (a company knowledge graph plus semantic layer feeding a
  "knowledge skill" router); this article supplies the governance failure
  modes that implementation would need to avoid to stay authoritative over
  time (Claim 6, Claim 7's maintenance problem).
- **Corroborates** `blog-kentbeck-randy-shoup-create-anything.md` Claim 9
  (Thrive Market's "genome" knowledge graph exists specifically because a
  12-year-old legacy codebase's actual behavior is not known even to its
  nominal owners): this is a concrete, named instance of the shared-language
  failure this article warns against — tribal knowledge fragmenting across
  teams until no one holds the authoritative picture. Shoup's account
  describes building the knowledge graph as an ongoing, actively-maintained
  effort rather than a one-time modeling exercise, which is consistent with
  this article's "product not project" prescription (Claim 8), though Shoup
  does not use that framing explicitly.
- **Extends** `blog-anthropic-selfservice-data-analytics.md`: that note
  documents what a maintained semantic layer plus knowledge graph looks like
  in production (skill routing, CI checks protecting cross-layer integrity,
  automated staleness-resolution PRs). This article supplies the
  organizational/process reasoning for *why* that maintenance investment is
  necessary — the maintenance-problem failure mode (Claim 7) is exactly what
  Anthropic's CI-enforced single-repo practice (selfservice-data-analytics
  Claim 9) is a countermeasure against, even though that note doesn't frame
  it that way.
- **Contradicts**: None identified. No existing source note stakes out a
  position that ontologies are unnecessary, that retrieval-over-documents is
  sufficient on its own, or that enterprise-wide ontology modeling (the
  scope-creep pattern this article warns against) is advisable — so there is
  no direct conflict to file as a contradiction issue.
- **Novel**:
  - The three-way failure-mode taxonomy for ontology programs (translation
    gap / scope creep / maintenance problem) as named, independently
    diagnosable categories is new to this corpus — prior notes touching
    ontologies or knowledge graphs (Kepler, self-service-analytics, Shoup)
    describe successful or in-progress implementations, not a structured
    account of why such programs fail.
  - "Competency questions as a funding gate" — requiring the business to
    name a specific unanswerable question and its dollar/decision stake
    before any ontology modeling begins — is a new prescriptive practice not
    described elsewhere in the corpus.
  - "Curate, don't draft from scratch" — using LLM pipelines to extract
    draft taxonomies from existing schemas, API definitions, and wikis as a
    countermeasure to the translation gap — is a specific agentic-AI-native
    technique for ontology construction not previously captured.
  - The explicit "stack, not a switch" framing (schemas → controlled
    vocabularies → semantic layers → ontologies → knowledge graphs as one
    continuum, choose the minimum structure needed) is a new organizing
    taxonomy for this corpus's semantic-infrastructure discussions.

## Guide Impact

- **Chapter 04 (Context Engineering)**: Add the three-mode ontology-program
  failure taxonomy (translation gap, scope creep, maintenance problem) as a
  named diagnostic checklist alongside the existing content-engineering /
  semantic-layer guidance from the Kepler and self-service-analytics notes.
  Currently the guide (via those notes) shows ontologies and semantic layers
  as things that work when implemented; this source adds the missing "here
  is specifically how these programs fail, and which of the three modes your
  stalled program is stuck in" diagnostic, which those notes don't provide.
- **Chapter 04 (Context Engineering)**: Add "treat the ontology as a
  product, not a project" plus its five concrete practices (Claim 9) as a
  named build-it-right pattern, specifically the "competency questions as a
  funding gate" practice as a concrete anti-scope-creep gate teams can apply
  before starting ontology work — the guide currently has no scoping
  mechanism for when to invest in ontology/semantic-layer infrastructure.
- **Chapter 04 (Context Engineering)**: Add the "stack, not a switch"
  continuum (schemas → controlled vocabularies → semantic layers →
  ontologies → knowledge graphs) as framing for a "choose the minimum
  semantic structure your use case requires" recommendation, to counter a
  reflexive "we need an ontology" or "we need a knowledge graph" default.
- **Chapter 03 (Safety and Verification)**: Add Claim 5 (a rule only binds
  when a deterministic runtime checks it and the check is demonstrable) as
  a second, independent source for the deterministic-enforcement-over-policy
  principle already suggested by the Kepler note, specifically applied to
  ontology-encoded guardrails: an ontology stating a permission rule is not
  itself a guardrail without runtime enforcement and an auditable record.

## Extraction Notes

- The source page declined full-text verbatim reproduction when requested
  (citing copyright), which is consistent with this project's own quoting
  discipline (MINER.md §2a): every `Quote` field above was independently
  fetched and verified as a short (under ~125-character), verbatim,
  contiguous excerpt tied to a specific claim, not reconstructed from a
  paraphrased summary. No quote in this note splices non-adjacent sentences.
- The article's "Related Content" sidebar links to three other Thoughtworks
  pieces ("Is a codeless future an illusion?", "Semantic drift and semantic
  integrity: Stewarding meaning in the age of AI", "The future of data is
  semantic"). These read as generic related-reading suggestions rather than
  substantive in-article citations the piece builds its argument on, so they
  were not followed as sub-pages per MINER.md §1. A future Prospector pass
  could independently evaluate the "semantic drift" piece, which sounds
  topically adjacent.
- The article names no specific company, client engagement, product, or
  vendor, and cites no metrics — it is a conceptual/prescriptive essay
  generalized from the author's stated role (Head of Advanced Analytics & AI
  at Thoughtworks), not a documented case study. This is reflected in the
  `emerging` confidence ratings throughout: the mechanisms described are
  plausible and specific, but none are independently measured or tied to a
  named, verifiable deployment.
- Checked existing source-notes for a direct contradiction (e.g., a note
  arguing ontologies are unnecessary, or that unstructured retrieval alone
  is sufficient) and found none — see Cross-References → Contradicts. No
  contradiction issue was filed.
