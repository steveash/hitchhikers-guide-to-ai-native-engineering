---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/importance-layered-context-enterprise-data-architecture
source_type: blog-post
title: "The importance of layered context in enterprise data architecture"
author: Richard Gall (Thoughtworks)
date_published: 2026-07-29
date_extracted: 2026-08-03
last_checked: 2026-08-03
status: current
confidence_overall: emerging
issue: "#2450"
---

# The Importance of Layered Context in Enterprise Data Architecture

> Thoughtworks essay arguing that a manually-curated, unified enterprise
> semantic layer or monolithic knowledge graph is "ultimately illusory"
> because data decay outpaces human curation, and proposing instead a
> three-layer, pull-based architecture (thin metadata map, small
> common-reference layer, direct access to unstructured/transactional
> data) with federated, domain-owned sub-graphs discovered via passive
> signal harvesting rather than upfront relationship-mapping — a direct
> architectural challenge to the ontology/semantic-layer curation model
> this corpus's other Thoughtworks data-architecture notes advocate (see
> **Contradicts**, filed as [#2458](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/2458)).

## Source Context

- **Type**: blog-post (Thoughtworks Insights, "Generative AI" category;
  published July 29, 2026; discovered via the trusted `thoughtworks` RSS
  feed). A conceptual/argumentative essay structured around named H2/H3
  sections including an introduction, "The layered context model," "The
  key decision point: Push vs. pull autonomy," "The fallacy of the
  monolithic graph," "Don't build the map; build the harness," "Storing
  reason[ing]" (traces as data), "Semantic pollution," "The risk of
  hallucinatory drift," and "Replicating tasks vs. seeking goals."
- **Author credibility**: Richard Gall, published under Thoughtworks
  Insights. Gall already has three other solo-authored source notes in
  this corpus on adjacent enterprise-AI-architecture topics
  (`blog-thoughtworks-gall-primitive-paradox.md`,
  `blog-thoughtworks-gall-commodity-illusion-compute-geopolitics.md`,
  `blog-thoughtworks-gall-supervisory-engineering.md`), all rated
  `emerging` — a recurring conceptual/framework-essay voice at
  Thoughtworks, not a first-person practitioner reporting a named
  deployment. This article names no client engagement, no product, no
  metric, and contains no code — it is argumentative/prescriptive, not
  a case study. Thoughtworks is an established trusted-feed source in
  this corpus.
- **Scope**: Covers a critique of centralized/curated semantic-layer
  architectures, a proposed three-layer context model, a push-vs-pull
  framing for context delivery, an argument against monolithic knowledge
  graphs in favor of federated sub-graphs, a "harness" (passive signal
  harvesting) alternative to manual relationship-mapping, treating
  agentic reasoning traces as storable/optimizable data, and temporal
  decay/provenance scoring as a defense against "hallucinatory drift."
  Does NOT cover: a named client engagement, a worked example with real
  entities/schemas, any quantified before/after outcome, or a
  head-to-head comparison against a documented semantic-layer
  deployment (e.g., the corpus's own
  `blog-anthropic-selfservice-data-analytics.md`).

## Extracted Claims

### Claim 1: Enterprises building AI-ready data infrastructure are effectively replicating the failed 1990s web-portal model — a manually curated, hierarchical taxonomy — which does not scale to how information actually grows
- **Evidence**: Opening framing analogy of the article, used to set up the
  critique of centralized semantic-layer curation.
- **Confidence**: emerging (an analogy/framing claim, not independently
  measured, but used to motivate the rest of the article's argument)
- **Quote**: "Organizations are effectively trying to build a 1994 Yahoo! for the enterprise"
- **Our assessment**: This is a rhetorical framing device, not itself
  evidence, but it previews the article's central objection: hierarchical,
  human-curated taxonomies (Yahoo!'s original web directory) lost to
  link-based, algorithmically-discovered structure (search engines/PageRank)
  because manual curation cannot keep pace with content growth. The
  article's later "hallucinatory drift" section (Claim 8) explicitly invokes
  PageRank-style ranking as the mechanism it wants enterprises to adopt and
  guard against, so this opening analogy is load-bearing for the rest of
  the piece, not decorative.

### Claim 2: A perfectly constructed, complete semantic layer for the enterprise is "ultimately illusory" — a "beautiful illusion" — because it can never be fully or permanently achieved
- **Evidence**: Direct critique statement in the article's introduction,
  responding to the premise that a single, complete semantic layer is an
  achievable target.
- **Confidence**: emerging (a critique/framing claim, not benchmarked
  against a specific failed semantic-layer deployment named in the
  article itself)
- **Quote**: "This is a nice idea in theory but really a beautiful illusion."
- **Our assessment**: This is the article's central point of disagreement
  with this corpus's other Thoughtworks data-architecture notes. See
  **Contradicts** below — this claim directly opposes the "treat the
  ontology as a product" and "agentic reconstruction of meaning" framings
  in `blog-thoughtworks-asthagiri-ontology-failure-modes.md` and
  `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md`, which
  both prescribe building and maintaining a curated semantic layer rather
  than treating the goal itself as illusory.

### Claim 3: The layered context model separates enterprise data into three distinct tiers — a lightweight metadata map, a common-reference layer of universal primitives, and a much larger unstructured/transactional layer accessed on demand
- **Evidence**: Direct definitional section ("The layered context model")
  naming and describing each of the three layers in turn.
- **Confidence**: emerging (a named architectural taxonomy, prescriptive
  rather than benchmarked)
- **Quote**: "This is the lightweight map. It defines data products, system boundaries, schemas and API locations."
- **Quote**: "These are your universal primitives; they include things like currency codes, country codes, system records and core entities."
- **Quote**: "These are petabytes of data that capture operational reality."
- **Our assessment**: This three-layer split is the article's core proposed
  architecture. It reframes "how much of the enterprise do we need to
  model?" as "which of these three layers does each piece of information
  belong in?" — the metadata/map layer stays deliberately thin (locations
  and boundaries, not full semantics), the common-reference layer holds
  only genuinely universal primitives (not domain-specific business
  logic), and everything else is left in its native, unstructured form and
  accessed directly rather than pre-modeled. This is a materially
  different design target than the corpus's existing ontology sourcing,
  which aims to make domain-specific business meaning explicit and
  machine-readable up front (see Cross-References).

### Claim 4: Pushing large amounts of reference data into an agent's context window upfront wastes tokens and primes the model with irrelevant noise; agents should instead be given a map and the tools to pull exactly what they need, when they need it
- **Evidence**: Direct statement under "The key decision point: Push vs.
  pull autonomy," contrasting the two delivery strategies.
- **Confidence**: emerging (a design-principle claim, plausible and
  consistent with known context-window-management concerns, not
  benchmarked against a push-based alternative in this article)
- **Quote**: "Pushing massive amounts of reference data into an agent's context window upfront wastes tokens and primes the model with noise."
- **Quote**: "equipped with a map and the API tools to traverse it dynamically"
- **Our assessment**: This "pull, don't push" prescription for reference
  data corroborates the pull/dynamic-context pattern already in this
  corpus from a different source and vendor context (see Cross-References
  → Corroborates,
  `blog-anthropic-carta-healthcare-context-engineering.md` Claim 2's
  per-query, assembled-at-query-time context scoping). The mechanism is
  the same underlying principle — scope what enters the context window to
  the specific task at hand rather than loading everything upfront — but
  applied here to enterprise reference/metadata delivery generally, not to
  a single structured-extraction pipeline.

### Claim 5: A single, monolithic, enterprise-wide knowledge graph is the wrong target; agentic context should instead be carved along domain boundaries so individual domains govern their own schemas, freshness, and credibility, with agents navigating between federated sub-graphs
- **Evidence**: Direct argument under "The fallacy of the monolithic
  graph," applying a domain-driven-design framing to agent context
  ownership.
- **Confidence**: emerging (an architectural-principle claim, argued by
  analogy to domain-driven design rather than demonstrated against a
  named monolithic-graph failure)
- **Quote**: "agentic context must be carved along clear boundaries"
- **Quote**: "individual domains can govern their own schemas, freshness and credibility"
- **Quote**: "The agent should then navigate between these distinct sub-graphs using a decentralized, web-like architecture."
- **Our assessment**: This is a specific, named architectural alternative —
  federated, domain-owned sub-graphs with decentralized navigation — to
  the single-knowledge-graph target implicit in this corpus's other
  ontology sourcing (e.g., `blog-thoughtworks-asthagiri-ontology-failure-modes.md`
  Claim 3's "a knowledge graph is that blueprint populated with your
  actual data; it's also the thing an agent actually queries," which does
  not itself specify one graph vs. many). This claim's contribution is
  naming domain ownership and decentralized navigation as the specific
  countermeasure to the monolithic-graph failure mode, applying
  domain-driven design vocabulary to agent context architecture
  specifically.

### Claim 6: Requiring subject matter experts to manually map every relationship in a knowledge graph produces a graph that is "dead on arrival," because the rate of enterprise data decay far outpaces human curation
- **Evidence**: Direct statement under "Don't build the map; build the
  harness," used to motivate the article's proposed alternative to manual
  relationship-mapping.
- **Confidence**: emerging (a critique of manual-curation feasibility,
  argued rather than measured against a specific named failed mapping
  project)
- **Quote**: "If subject matter experts are required to manually map every link and relationship within a knowledge graph, the graph will unfortunately be dead on arrival."
- **Quote**: "The rate of data decay inside an enterprise far outpaces human curation; documentation is almost always an inaccurate reflection of operational reality."
- **Our assessment**: This is the article's sharpest, most specific
  disagreement with the "agentic reconstruction of meaning" practice in
  `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md` (Claim 4)
  and the SME-confirmation step in
  `blog-thoughtworks-xiong-ontology-llm-data-modernization.md` (Claim 5) —
  both of those articles still route relationship/mapping proposals
  through human/SME review as the trust mechanism, whereas this claim
  argues that *any* mapping process requiring humans to manually confirm
  relationships (whether drafted by an LLM or not) will lag behind the
  actual rate of enterprise change and arrive already stale. This is the
  claim most directly underlying the contradiction filed as
  [#2458](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/2458).

### Claim 7: Instead of manually mapping relationships, enterprises should build a "harness" that passively discovers relationships from the unintentional digital trails employees already leave — emails, Slack threads, document references
- **Evidence**: Direct description of the proposed alternative mechanism
  under "Don't build the map; build the harness."
- **Confidence**: anecdotal (a proposed mechanism illustrated with
  generic, non-named examples — no described implementation, tooling, or
  measured discovery accuracy is given in the article)
- **Quote**: "Every day, humans leave a digital trail of relationships: an email links to a sales opportunity; a Slack thread references a specific GitHub commit."
- **Our assessment**: This is a genuinely novel mechanism to this corpus —
  discovering the knowledge-graph edges from ambient, unintentional
  digital exhaust rather than either manual SME mapping or LLM-drafted
  proposals subject to human confirmation. The article gives no detail on
  how such a harness would be built, what privacy/access-control
  implications passively mining email and chat content would raise, or
  how discovery accuracy would be evaluated — this is the least concretely
  specified claim in the article and is rated `anecdotal` accordingly (an
  illustrative idea, not a described or measured system).

### Claim 8: Reasoning traces from agentic workflows should be stored as first-class, graph-shaped or skill-shaped historical data, enabling network/graph algorithms to optimize future workflows
- **Evidence**: Direct statement under "Storing reason[ing]," describing
  agentic decision logs as a new category of enterprise data to be
  retained and analyzed.
- **Confidence**: anecdotal (a proposed practice, no described
  implementation, storage format, or measured optimization outcome given)
- **Quote**: "By storing agentic traces as graph-shaped or skill-shaped historical projections, network algorithms can be run to optimize workflows."
- **Our assessment**: This is a novel, concrete idea for this corpus — that
  an agent's own reasoning/decision history is itself enterprise data
  worth retaining as a queryable graph, not just transient execution
  state. No detail is given on retention policy, format, or what "network
  algorithms to optimize workflows" concretely means or measures, so this
  should be treated as a suggestive direction rather than an
  implementation-ready pattern.

### Claim 9: Without safeguards, errors and stale assumptions get amplified across an enterprise knowledge graph the same way link-based ranking algorithms amplify popular but incorrect pages — a "hallucinatory drift" risk analogous to enterprise SEO
- **Evidence**: Direct argument under "The risk of hallucinatory drift" /
  "Semantic pollution," describing the mechanism by which repeated stale
  or incorrect data gets ranked as credible.
- **Confidence**: emerging (a specific failure-mechanism argument, drawn
  by analogy to search-ranking algorithms rather than a documented
  incident of this occurring in an enterprise knowledge graph)
- **Quote**: "if incorrect assumptions, a stale design document or a hallucinated metric is cross-referenced or repeated multiple times across disparate systems...graph ranking algorithms will naturally weight that node as highly credible"
- **Our assessment**: This names a specific, mechanism-level risk that is
  new to this corpus's data-architecture sourcing: repetition itself
  (rather than source authority) becoming a false credibility signal
  inside a knowledge graph, mirroring known SEO-gaming dynamics in web
  search. This is a concrete argument for why graph-based context
  retrieval needs its own integrity safeguards (Claim 10), not just
  population coverage.

### Claim 10: To defend against this drift, a node's authority in the graph must be penalized by its age and validated against hard transactional boundaries, rather than weighted by how often it is cited or repeated
- **Evidence**: Direct prescription under "Semantic pollution," proposed
  as the countermeasure to Claim 9's drift mechanism.
- **Confidence**: anecdotal (a proposed scoring principle; no described
  implementation, weighting formula, or measured effect on drift given)
- **Quote**: "A node's authority must be heavily penalized by its age and validated against hard transactional boundaries, rather than just its citation count"
- **Our assessment**: This is a specific, named design principle —
  temporal decay plus grounding against transactional ("hard") data as the
  trust mechanism, explicitly rejecting citation-count/repetition as a
  valid credibility signal. It is prescriptive rather than demonstrated:
  the article gives no worked example of how "penalized by age" or
  "validated against hard transactional boundaries" would be computed or
  tuned in practice.

### Claim 11: Enterprise AI agents should be built and evaluated as goal-seeking entities pursuing a measurable target, not as systems that replicate a fixed human workflow step-by-step
- **Evidence**: Direct argument in the closing section, "Replicating
  tasks vs. seeking goals," contrasting workflow-mimicry with goal-directed
  autonomy.
- **Confidence**: emerging (a design-philosophy claim, argued rather than
  benchmarked against a specific workflow-mimicry failure)
- **Quote**: "Agents, however, need to be understood as goal-seeking entities."
- **Quote**: "If we provide them with a high-fidelity map of our metadata, a clear set of operational boundaries and a measurable target, they will find paths toward that goal that a human process would never have conceived"
- **Our assessment**: This claim explicitly ties back to the article's
  layered-context architecture (Claim 3): the metadata map and operational
  boundaries are framed as the necessary and sufficient inputs for a
  goal-seeking agent to find novel paths, rather than context being used
  to make the agent faithfully replicate an existing human process. This
  reframes the purpose of the metadata/reference layers described earlier
  — not as documentation for a human-equivalent process-follower, but as
  boundary conditions for an optimizer.

### Claim 12: The ultimate goal of enterprise AI is not to automate existing processes but to make them obsolete
- **Evidence**: Closing thesis statement of the article, presented as the
  logical conclusion of treating agents as goal-seeking (Claim 11) rather
  than task-replicating.
- **Confidence**: anecdotal (a closing rhetorical/aspirational claim, not
  itself argued with a specific mechanism or example beyond the
  goal-seeking framing that precedes it)
- **Quote**: "The ultimate goal of enterprise AI isn't to automate existing processes; it's to make them obsolete"
- **Our assessment**: This is a strong, quotable framing claim but the
  article does not substantiate it with a worked example of a process
  being made obsolete (as opposed to automated) as a result of the
  layered-context architecture it proposes. Treat as an aspirational
  closing thesis rather than a demonstrated outcome — it is the article's
  rhetorical high point, not its evidentiary center of gravity (which is
  Claims 3-7, the layered-context architecture itself).

## Concrete Artifacts

```
Source: Richard Gall, "The importance of layered context in enterprise
data architecture," Thoughtworks Insights, July 29, 2026

Three-layer context model (as headed under "The layered context model"):
1. Metadata / map layer — lightweight map of data products, system
   boundaries, schemas, and API locations
2. Common reference layer — universal primitives (currency codes,
   country codes, system records, core entities)
3. Unstructured / transactional layer — petabytes of data capturing
   operational reality, accessed via targeted pull queries rather than
   pre-modeled

Design principles named:
- Push vs. pull: don't push large reference datasets into the context
  window upfront; give agents a map + API tools to pull what they need
  ("The key decision point: Push vs. pull autonomy")
- Federated, not monolithic: carve agentic context along domain
  boundaries (domain-driven design applied to context); each domain
  governs its own schema, freshness, and credibility; agents navigate
  federated sub-graphs via a "decentralized, web-like architecture"
  ("The fallacy of the monolithic graph")
- Harness, not manual map: discover relationships passively from
  existing digital trails (emails, Slack threads, doc references) rather
  than requiring SMEs to manually map every link ("Don't build the map;
  build the harness")
- Reasoning traces as data: store agentic decision logs as graph-shaped
  or skill-shaped historical projections; run network algorithms over
  them to optimize future workflows ("Storing reason[ing]")
- Anti-drift scoring: penalize a graph node's authority by its age and
  validate against hard transactional boundaries, not citation/repetition
  count, to prevent "hallucinatory drift" / "semantic pollution"
  analogous to enterprise SEO ("Semantic pollution",
  "The risk of hallucinatory drift")
- Goal-seeking framing: agents should be given a metadata map, boundaries,
  and a measurable target, then evaluated on paths found toward the goal
  rather than fidelity to an existing human workflow
  ("Replicating tasks vs. seeking goals")
```

## Cross-References

### Cross-reference verification notes
`blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md`,
`blog-thoughtworks-asthagiri-ontology-failure-modes.md`,
`blog-thoughtworks-xiong-ontology-llm-data-modernization.md`, and
`blog-anthropic-carta-healthcare-context-engineering.md` were re-read in
full before writing the citations below; claim numbers cited were
confirmed against each note's numbered `### Claim N:` headings in
document order.

- **Corroborates**:
  - `blog-anthropic-carta-healthcare-context-engineering.md` Claim 2
    (per-data-point runtime context assembly with temporal anchors —
    assembling a distinct context window per query, scoped to that
    query's specific boundary conditions, rather than one global context
    for every question): this article's Claim 4 (pull, don't push;
    "equipped with a map and the API tools to traverse it dynamically")
    is the same underlying principle — scope what enters the context
    window to the specific task at hand — applied to enterprise
    reference-data delivery generally rather than to a single clinical
    extraction pipeline. Independent corroboration from a different
    vendor (Anthropic/Carta Healthcare) and a different genre (a
    documented, metriced production case study vs. this article's
    vendor-conceptual framing).

- **Contradicts** (filed as
  [#2458](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/2458)):
  - `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 8
    ("the ontology that survives contact with the real world is one
    where an ontology is treated as a product rather than a project")
    and Claim 9 (five product-building practices, including agentic
    LLM-assisted drafting with SME confirmation): this article's Claim 2
    ("a perfectly constructed semantic layer... is really a beautiful
    illusion") and Claim 6 (any process requiring humans to manually
    confirm mapped relationships "will unfortunately be dead on arrival"
    because "the rate of data decay inside an enterprise far outpaces
    human curation") directly oppose the premise that a curated,
    product-managed ontology/semantic layer is an achievable, worthwhile
    target — even one scoped to a single funded use case and maintained
    with an owner and reconciliation cadence, per Asthagiri's Claim 9.
  - `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md` Claim 4
    ("agents profile each source, propose mappings to the ontology, draft
    the serialized context and infer candidate access policies, with
    humans reviewing and confirming rather than authoring from scratch")
    and Claim 7 ("data products" as composable units binding data +
    metadata + semantic meaning + governance): this article's Claim 5
    (a single monolithic knowledge graph is a "fallacy"; context should
    be federated along domain boundaries) and Claim 7 (discover
    relationships by passively harvesting existing digital trails,
    rather than through any human-confirmed mapping process, LLM-drafted
    or otherwise) propose a structurally different mechanism for how the
    semantic layer itself comes into being — passive harvesting instead
    of agentic-proposal-plus-human-review.
  - This is filed as a contradiction issue rather than resolved here per
    MINER.md §4a; no verdict is asserted in this note. See the issue for
    the full Side A / Side B statement and a noted possible reconciling
    reading (Asthagiri's own "scope creep" warning is partially in the
    spirit of Gall's critique of monolithic graphs, but Gall's critique is
    more totalizing and targets the curation *mechanism* itself, not just
    over-ambitious scope).

- **Extends**:
  - `blog-anthropic-carta-healthcare-context-engineering.md`: that note
    documents pull-based, per-query context scoping within a single
    structured-extraction pipeline (clinical data abstraction). This
    article generalizes the same push-vs-pull principle (Claim 4) to
    enterprise-wide reference-data architecture and adds two elements the
    Carta note does not contain: a named three-layer model for what
    belongs in "pushed" vs. "pulled" data (Claim 3), and a federated,
    domain-owned sub-graph structure for the pulled portion (Claim 5).

- **Novel**:
  - **The three-layer context model** (metadata/map, common reference,
    unstructured/transactional — Claim 3) as a named architecture for
    what to model upfront vs. leave in native form and pull on demand —
    not present as an explicit three-way split elsewhere in this corpus's
    data-architecture sourcing.
  - **Domain-driven design applied to agent context ownership** (Claim 5:
    federated sub-graphs, each domain governing its own schema, freshness,
    and credibility, navigated via a "decentralized, web-like
    architecture") — a new named architectural alternative to a single
    enterprise-wide knowledge graph.
  - **Passive signal harvesting from digital exhaust** (Claim 7: emails,
    Slack threads, document references) as a relationship-discovery
    mechanism replacing manual or human-confirmed mapping — genuinely new
    to this corpus, though the article leaves the implementation
    (including privacy/access-control implications of mining
    communications) entirely unspecified.
  - **Reasoning traces stored as first-class graph data** (Claim 8) for
    workflow optimization via network algorithms — a new proposed data
    category not discussed in the corpus's other context-engineering
    sourcing.
  - **"Enterprise SEO" / hallucinatory-drift risk and age-based
    provenance scoring** (Claims 9-10) as a named failure mode and
    countermeasure for graph-based enterprise context — new to this
    corpus's data-architecture and hallucination-risk sourcing.

## Guide Impact

- **Chapter 02 (Data & Infrastructure)**: Flag the contradiction
  ([#2458](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/2458))
  between this article and the "AI-ready data" / "treat the ontology as
  a product" guidance already sourced from
  `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md` and
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md`. Do not add
  either side's prescription as settled guidance until the contradiction
  is resolved; once resolved, cite per the CONTRADICTIONS.md entry's
  "Citation in the guide" instructions.
- **Chapter 02 (Data & Infrastructure)**: Independent of the
  contradiction's resolution, add the three-layer context model
  (Claim 3: metadata/map, common reference, unstructured/transactional)
  as a candidate framework for deciding what enterprise data needs to be
  pre-modeled at all versus left in native form and pulled on demand —
  this is a more granular scoping question than "should we build an
  ontology," and is compatible with either side of the filed
  contradiction (a team could apply Side A's product discipline to the
  common-reference layer specifically, while applying Side B's pull
  model to the transactional layer).
- **Chapter 04 (Context Engineering)**: Add the push-vs-pull framing
  (Claim 4) and its corroboration by
  `blog-anthropic-carta-healthcare-context-engineering.md` Claim 2 as
  reinforced guidance: scope context delivered to an agent to the
  specific task/query at hand rather than loading broad reference data
  upfront. This recommendation stands independent of the semantic-layer
  contradiction — both sides of that disagreement could adopt a pull
  model for the transactional layer.
- **Chapter 04 (Context Engineering)**: Add the "hallucinatory drift" /
  "enterprise SEO" risk mechanism (Claims 9-10) as a named risk for any
  team building graph-based or repetition-weighted enterprise context
  retrieval, regardless of how that graph is populated (manually curated
  per Side A or passively harvested per Side B) — the age-penalty /
  transactional-grounding countermeasure is a candidate mitigation to
  document, though it is prescriptive rather than demonstrated in this
  article and should be flagged as such (confidence: anecdotal).

## Extraction Notes

1. **Full verbatim article text was not obtainable via a single
   WebFetch pass.** As with other Thoughtworks pieces in this corpus
   (e.g. `blog-thoughtworks-asthagiri-ontology-failure-modes.md`,
   `blog-thoughtworks-xiong-ontology-llm-data-modernization.md`), an
   initial WebFetch request returned a paraphrased section-by-section
   summary rather than the raw article body. Two additional, targeted
   WebFetch calls were made requesting only short (under ~250 character),
   verbatim, contiguous passages tied to named sections, with explicit
   instructions not to paraphrase or splice non-adjacent sentences. All
   quotes above are drawn from these verified short-passage fetches, not
   reconstructed from the initial paraphrased summary. As with the
   companion notes, the Assayer should spot-check quotes against the
   live URL.
2. **No sub-pages followed.** The article is a single, self-contained
   essay with no in-article links to deeper technical posts or external
   studies surfaced in the section-by-section fetches; per MINER.md §1,
   no sub-pages were identified as substantive enough to follow.
3. **Contradiction filed before this note was opened, per MINER.md §4a.**
   Claim 2 and Claim 6 of this article materially oppose Claim 8/9 of
   `blog-thoughtworks-asthagiri-ontology-failure-modes.md` and Claim 4/7
   of `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md` on
   whether building/maintaining a curated semantic layer is a worthwhile,
   achievable target. Filed as
   [#2458](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/2458)
   with a `debated` filer-recommended verdict (both sides are
   argumentative Thoughtworks essays without a named production
   deployment or head-to-head benchmark). No verdict is asserted in this
   source note — see Cross-References → Contradicts.
4. **Confidence rated `emerging` overall.** The article's core
   architectural claims (Claims 3-7: the three-layer model, push/pull,
   federated sub-graphs, passive harvesting) are specific and internally
   coherent, consistent with the `emerging` rating given to Gall's other
   three source notes in this corpus. Several individual claims are
   rated `anecdotal` (Claims 7, 8, 10, 12) where the article proposes a
   mechanism without any description of an implementation, tooling, or
   measured outcome — these are ideas the article puts forward, not
   demonstrated practices. No claim in the article is rated `settled`;
   nothing here is corroborated by an independent, named production
   deployment within this corpus.
