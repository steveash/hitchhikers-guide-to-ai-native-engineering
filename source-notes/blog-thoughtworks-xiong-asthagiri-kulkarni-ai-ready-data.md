---
source_url: https://www.thoughtworks.com/insights/articles/AI-ready-data-why-and-how
source_type: blog-post
title: "AI-ready data, why and how?"
author: Zichuan Xiong, Nimisha Asthagiri, and Shrinidhi Kulkarni (Thoughtworks)
date_published: 2026-07-23
date_extracted: 2026-08-02
last_checked: 2026-08-02
status: current
confidence_overall: emerging
issue: "#2416"
---

# AI-Ready Data, Why and How?

> Thoughtworks essay arguing that structured data has precision without
> meaning while unstructured data has meaning without precision, and that
> AI-readiness requires extending data modernization's scope to a
> continuously-maintained semantic context layer — recovered via agentic
> workflows, serialized in machine-readable form (MCP, vector databases,
> APIs), bound to self-describing "data product" units carrying their own
> governance policies, and refined through operational feedback loops.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, "Articles" category;
  published July 23, 2026; from the trusted `thoughtworks` RSS feed). A
  five-section conceptual/prescriptive essay: "Why the gap exists," "What
  AI actually needs from data," "A new scope for data modernization," "Our
  approach and how it scales," and "Summary." No named client engagement,
  tooling implementation, or quantified outcome is given anywhere in the
  piece.
- **Author credibility**: Co-authored by three named Thoughtworks
  practitioners — Zichuan Xiong, Nimisha Asthagiri, and Shrinidhi Kulkarni.
  Two of the three are independently established, single-authored voices
  already in this corpus on directly overlapping subject matter: Xiong
  authored `blog-thoughtworks-xiong-ontology-llm-data-modernization.md`
  (July 22, 2026, the day before this piece) proposing a six-step
  ontology+LLM agentic workflow for data-modernization discovery, and
  Asthagiri — Head of Advanced Analytics & AI, Thoughtworks North America —
  authored `blog-thoughtworks-asthagiri-ontology-failure-modes.md` (June
  17, 2026) diagnosing why ontology programs fail and prescribing "treat
  the ontology as a product, not a project." This article reads as a joint
  synthesis piece by (at least) two authors who had each already published
  solo essays on adjacent ontology/semantic-layer territory within the
  preceding five weeks, generalizing their individual arguments under an
  explicit "AI-readiness" framing. No bio or title is given for the third
  author, Shrinidhi Kulkarni, on the article page itself.
- **Scope**: Covers a diagnosis of why enterprise data isn't AI-ready
  (structured-vs-unstructured precision/meaning split), four things AI
  specifically needs from data (semantic meaning, relationships, temporal
  validity, machine-readable context), an argument that existing data
  modernization scope (accessibility, ownership, quality, lineage,
  governance) must extend to include a semantic context layer, and a
  three-part recommended approach (agentic reconstruction of meaning,
  binding context to data products, closing feedback loops through
  operations). Does NOT cover: a named client engagement, specific tooling
  benchmarks or implementation code, quantified before/after outcomes, or
  a comparison against alternative approaches (e.g., retrieval-only
  strategies without a semantic layer).

## Extracted Claims

### Claim 1: Enterprise data was built for two separate, AI-incompatible paradigms — structured data delivers precision without meaning, while unstructured data delivers meaning without precision — and the deployment gap for AI emerges specifically because these two properties are split across two different mechanisms
- **Evidence**: The article's opening diagnostic framing under "Why the gap
  exists," illustrated with a concrete example (a database column typed
  and constrained with perfect precision but whose business meaning is
  undocumented).
- **Confidence**: emerging (a specific, illustrated diagnostic framing
  consistent with the corpus's existing ontology/semantic-layer sourcing,
  but not independently measured against a failure-rate statistic)
- **Quote**: "A table defines types, keys and constraints, and every value is exact; yet a column named flg_3 holding 1, 2, 3 says nothing about what it represents."
- **Quote**: "The precision is real, but the meaning lives outside it: in someone's head, or a document no one really knows."
- **Quote**: "The meaning is there; the precision isn't."
- **Our assessment**: The "flg_3" example is a specific, memorable
  illustration of the same underlying gap that
  `blog-thoughtworks-xiong-ontology-llm-data-modernization.md` Claim 2
  describes more abstractly ("without explicit semantic context, the LLM
  must infer relationships from schemas, column names and sample values...
  difficult to verify consistently at enterprise scale") and that
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 1
  frames as "a language model can read your documents, but it doesn't
  hold your operating logic." This article's contribution is naming the
  precision/meaning split as the root mechanism common to both the
  structured and unstructured sides of the problem, rather than treating
  them as two unrelated data-quality issues.

### Claim 2: AI needs data with four specific properties — semantic meaning that travels embedded with the data, relationships reasoned over via ontologies, temporal validity (timestamps and validity periods, since past truths may not hold now or later), and a machine-readable format the agent can consume directly at the moment it acts
- **Evidence**: Direct enumeration under "What AI actually needs from
  data," the article's second major section.
- **Confidence**: emerging (a specific four-part requirements taxonomy,
  consistent with but more granular than prior corpus sourcing on what
  agentic systems need beyond raw retrieval)
- **Quote**: "AI needs data that explains itself, with precision, structure, an awareness of its own validity and a machine-readable format."
- **Our assessment**: This is a more granular requirements breakdown than
  this corpus's existing ontology sourcing provides — Asthagiri's article
  argues ontologies matter for agentic AI in general terms (retrieval,
  guardrails, shared language), while this claim decomposes "what AI
  needs from data" into four separately named, checkable properties. The
  temporal-validity requirement in particular is new to this corpus: no
  prior Thoughtworks ontology note names time-boundedness (data needing
  timestamps/validity periods because "past truths may not apply
  presently or futurely," per the WebFetch summary of this section) as a
  distinct AI-readiness dimension.

### Claim 3: Current enterprise data modernization programs — scoped to accessibility, ownership, quality, lineage, and governance — are necessary but insufficient for AI; the scope must extend to include a semantic context layer covering meaning, relationships, validity, and boundaries
- **Evidence**: Direct argument under "A new scope for data modernization,"
  reframing what "modernization" must cover once AI agents are the
  consumer of the data, not just human analysts or downstream systems.
- **Confidence**: emerging (a scoping/definitional argument, consistent
  with the article's overall thesis, not independently benchmarked against
  a specific modernization program's outcomes)
- **Quote**: "Semantic context isn't a one-off annotation exercise that ages out the moment a schema changes."
- **Our assessment**: This is the article's central definitional move — it
  does not argue existing data-modernization practice is wrong, only
  incomplete for AI consumption. This directly extends
  `blog-thoughtworks-aliyeva-werner-lammel-path-to-production.md` Claim 3,
  which names "data and infrastructure gaps" (fragmented, late-arriving
  data on unstable legacy foundations) as one of four causes of the "PoC
  graveyard" but does not itself define what closing that gap requires;
  this article supplies exactly that missing definition.

### Claim 4: The recommended approach recovers meaning through an agentic workflow — AI agents profile each data source, propose mappings to a unified ontology, draft the serialized machine-readable context, and infer candidate access policies, with humans reviewing and confirming rather than authoring from scratch
- **Evidence**: Direct description of "Agentic reconstruction of meaning,"
  the first of three named practices under "Our approach and how it
  scales."
- **Confidence**: emerging (a specific, named technique description,
  presented without a worked example or measured extraction-accuracy
  figure — contrast with the worked billing/support-ticketing example in
  the companion Xiong article, below)
- **Quote**: "agents profile each source, propose mappings to the ontology, draft the serialized context and infer candidate access policies, with humans reviewing and confirming rather than authoring from scratch."
- **Our assessment**: This is functionally identical to Step 1 of the
  six-step agentic loop in
  `blog-thoughtworks-xiong-ontology-llm-data-modernization.md` Claim 5 ("an
  AI agent reads each source system's schema and data types, foreign keys
  and join patterns, sample values, and comments/documentation to infer a
  candidate ontology, flagging low-confidence guesses for an SME to
  confirm") — the same author (Xiong) restates the same per-source
  ontology-extraction mechanism one day later in this joint piece, now
  folded into a broader three-part AI-readiness framework rather than
  presented as step one of a standalone six-step loop. This is
  corroboration from the same practitioner across two consecutive
  publications, not independent replication.

### Claim 5: Serialized semantic context must be delivered in a form an agent can consume directly and act on in the moment — via mechanisms like the Model Context Protocol (MCP), vector databases, or APIs — not through spreadsheets or static documentation
- **Evidence**: Direct statement under "Agentic reconstruction of meaning,"
  naming three specific serialization mechanisms.
- **Confidence**: emerging (a specific, named-technology recommendation;
  MCP and vector databases are named as examples of the delivery mechanism
  rather than benchmarked against each other)
- **Quote**: "Meaning has to travel with the data."
- **Our assessment**: This is the article's most concrete infrastructure
  recommendation and the first explicit naming of MCP as a semantic-context
  delivery mechanism in this corpus's ontology/data-modernization sourcing
  specifically (contrast with the Xiong and Asthagiri companion notes,
  neither of which names a specific protocol for how ontology context
  should be serialized for agent consumption — Xiong's note states context
  "can be kept under source control" but does not name a runtime delivery
  mechanism). This is a genuinely new, concrete detail for the guide's
  context-engineering infrastructure sourcing.

### Claim 6: AI-ready data must carry its own access policies, including row- and column-level security, so that agents can act safely and autonomously without a human manually gating each query
- **Evidence**: Direct statement under "Agentic reconstruction of
  meaning," the governance component of the three-part recommended
  approach.
- **Confidence**: emerging (a specific governance mechanism, consistent
  with but more granular than prior corpus governance sourcing)
- **Quote**: "AI-ready data must carry its own access policies and row- and column-level security, so agents can act safely and autonomously."
- **Our assessment**: This corroborates
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 5 ("a rule
  only binds when a deterministic runtime checks it and respects the
  answer and when you can show the check actually happened") by naming a
  specific enforcement granularity (row- and column-level security) for
  what "the runtime checks it" means in a data-access context — Asthagiri's
  claim is the general architectural principle; this claim supplies a
  concrete data-layer instance of it.

### Claim 7: The unit of AI-readiness should shift from monolithic data pipelines to modular, self-describing "data products" — composable units packaging data, metadata, semantic meaning, and governance policies together — evaluated against a new "agent-readability" test: can an agent, handed this product cold, understand what it is and what it may do with it?
- **Evidence**: Direct description of "Bind context to data products," the
  second of three named practices under "Our approach and how it scales."
- **Confidence**: emerging (a named design principle and a proposed
  evaluative question, not independently validated against a documented
  data-product catalog or agent-comprehension benchmark)
- **Quote**: "We shift from monolithic pipelines toward modular, self-describing data products: composable lego-blocks that package the data, metadata, semantic meaning and governance policies into a single node an agent can plug into."
- **Quote**: "Agent-readability.: Can an agent, handed this product cold, understand what it is and what it may do with it?"
- **Our assessment**: "Agent-readability" as a named, checkable design
  question is new to this corpus — the closest prior analogue is
  `blog-anthropic-selfservice-data-analytics.md` Claim 9 (a single repo
  containing data code, semantic layer, reference docs, and dashboard
  definitions together with CI checks protecting cross-layer integrity),
  which co-locates the same categories of artifact (data + semantic
  context + governance) but as a repo-level engineering practice at one
  company, not as a named, portable design principle for evaluating any
  individual data unit. This claim generalizes that pattern into an
  explicit test a team could apply to any data product.

### Claim 8: Operating semantic layers in live agent workflows surfaces concrete errors — misread fields, over-broad access policies — that feed back into the semantic layer for continuous refinement, closing the loop between design-time modeling and runtime behavior
- **Evidence**: Direct description of "Close feedback loops through
  operations," the third of three named practices.
- **Confidence**: emerging (a specific operational mechanism, presented
  without a named example of a specific error caught this way or a
  measured refinement cadence)
- **Quote**: "Operating is how modernization stays alive."
- **Our assessment**: This directly corroborates and gives an operational
  mechanism for
  `blog-thoughtworks-xiong-ontology-llm-data-modernization.md` Claim 11
  ("context must be managed as a continuously-updated, version-controlled
  semantic asset at the landscape level... each resolved gap becomes the
  new baseline that the next use case and the next agent inherit") and
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 6/7 (a
  shared ontology model goes stale within roughly two quarters without a
  steward and reconciliation cadence — the "maintenance problem" failure
  mode). This claim's specific contribution is naming the *source* of the
  feedback signal — live agent workflow errors (misread fields, over-broad
  policies) — rather than a general prescription to "keep the model
  current."

### Claim 9: The core enterprise-AI bottleneck in mid-2026 is data, not model or agentic capability
- **Evidence**: Opening statement of the "Summary" section, presented as
  the article's closing thesis restatement.
- **Confidence**: emerging (a framing/positioning claim consistent with
  the rest of the article's argument, not itself independently measured)
- **Quote**: "Enterprise AI is accelerating into production, and it's meeting a gap, not in model or agentic capability, but in data."
- **Our assessment**: This is a specific, checkable claim about where the
  bottleneck sits (data, not model/agent capability) that corroborates
  `blog-thoughtworks-aliyeva-werner-lammel-path-to-production.md` Claim 8
  ("technology is rarely the primary blocker... the bigger challenge is
  organizational") in spirit, though this article locates the specific
  blocker inside the data layer rather than the broader organizational
  operating model — the two claims are compatible (data-and-infrastructure
  gaps are one of the four named PoC-graveyard roadblocks in that same
  article's Claim 3) but this claim is more specific about which
  particular capability (data, not org process broadly) is lagging.

## Concrete Artifacts

```
Source: Zichuan Xiong, Nimisha Asthagiri, Shrinidhi Kulkarni, "AI-ready
data, why and how?", Thoughtworks Insights, July 23, 2026

Four things AI needs from data (as extracted from "What AI actually needs
from data"):
1. Semantic meaning — must travel embedded with the data (e.g. "flg_3
   represents customer tier" understandable without human explanation)
2. Relationships — reasoning across interconnected entities within
   ontologies representing real-world structure
3. Temporal validity — timestamps and validity periods, since past truths
   may not hold in the present or future
4. Machine-readable context — communicated in a form the agent can read
   directly, in the moment it acts (not spreadsheets or documentation)

Three-part recommended approach (as headed under "Our approach and how it
scales"):
1. Agentic reconstruction of meaning — agents profile sources, propose
   ontology mappings, draft serialized context (via MCP, vector
   databases, or APIs), infer access policies; humans review rather than
   author from scratch
2. Bind context to data products — modular, self-describing "composable
   lego-blocks" packaging data + metadata + semantic meaning + governance
   policies; evaluated by an "agent-readability" test
3. Close feedback loops through operations — live agent-workflow errors
   (misread fields, over-broad policies) feed back into continuous
   semantic-layer refinement
```

## Cross-References

### Cross-reference verification notes
`blog-thoughtworks-xiong-ontology-llm-data-modernization.md`,
`blog-thoughtworks-asthagiri-ontology-failure-modes.md`,
`blog-thoughtworks-aliyeva-werner-lammel-path-to-production.md`, and
`blog-anthropic-selfservice-data-analytics.md` were re-read in full before
writing the citations above and below; claim numbers cited were confirmed
against each note's numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-thoughtworks-xiong-ontology-llm-data-modernization.md` Claim 5
    (an AI agent reads schema, data types, foreign keys, sample values,
    and documentation to infer a candidate ontology, flagging
    low-confidence guesses for SME confirmation): this article's Claim 4
    restates the same mechanism in more compressed form, published one day
    after that article by the same author (Xiong) — same-author
    restatement, not independent replication, but confirms the mechanism
    is the author's settled position across two consecutive publications.
  - `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 5 (a rule
    only binds when a deterministic runtime checks it and the check is
    demonstrable): this article's Claim 6 (row- and column-level access
    policies carried by the data itself) supplies a concrete data-layer
    instance of that general enforcement principle.
  - `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 6/7 (a
    shared ontology model decays within roughly two quarters without a
    steward and reconciliation cadence — the "maintenance problem") and
    `blog-thoughtworks-xiong-ontology-llm-data-modernization.md` Claim 11
    (context managed as a continuously-updated, version-controlled
    semantic asset, with each resolved gap becoming the next use case's
    inherited baseline): this article's Claim 8 (operational feedback from
    live agent-workflow errors closes the loop) names the specific signal
    source for the continuous-maintenance mechanism both companion
    articles prescribe more abstractly.
  - `blog-thoughtworks-aliyeva-werner-lammel-path-to-production.md` Claim 3
    (data and infrastructure gaps — fragmented, late-arriving data on
    unstable legacy foundations — as one of four named PoC-graveyard
    causes): this article is the detailed "how to close this gap" piece
    the Prospector's triage comment specifically asked the Miner to look
    for; that article names the data/infrastructure gap as a blocker
    without explaining what AI-ready data requires or how to build it —
    this article supplies exactly that missing detail (Claims 1-8).
  - `blog-anthropic-selfservice-data-analytics.md` Claim 8 (data
    foundations — canonical datasets with enforced governance — are the
    most important accuracy enabler because they reduce ambiguity from
    "forty plausible candidates" to "one governed dataset") and Claim 10
    (the semantic layer is the highest-reliability source of truth,
    yielding the same metric value across all company surfaces): both
    describe, from a different vendor (Anthropic) and a different genre
    (documented internal case study with a 95%-accuracy figure, vs. this
    article's vendor-conceptual framing), the same underlying claim that
    semantic/governance infrastructure — not model or agent capability —
    is the accuracy-determining layer. This article's Claim 9 (the
    bottleneck is data, not model/agentic capability) is the general
    framing; the Anthropic note supplies the specific, measured instance.

- **Contradicts**: None identified and none filed. No claim in this
  article materially opposes a claim in the companion Xiong/Asthagiri
  ontology notes, the Thoughtworks path-to-production note, or the
  Anthropic self-service-analytics note — where topics overlap (agentic
  ontology extraction, deterministic enforcement, continuous maintenance,
  data as the enterprise-AI bottleneck), this article's claims are
  consistent extensions or same-author restatements, not disagreements.

- **Extends**:
  - `blog-thoughtworks-xiong-ontology-llm-data-modernization.md` and
    `blog-thoughtworks-asthagiri-ontology-failure-modes.md`: those two
    articles separately argue *why* ontologies matter for agentic AI and
    *how* to run a repeatable per-source ontology-extraction loop. This
    article synthesizes both under an explicit "AI-readiness" framing and
    adds two elements neither companion note contains: a named
    serialization mechanism for delivering context to agents (MCP, vector
    databases, or APIs — Claim 5) and the "data product" / "agent-
    readability" framing (Claim 7) for evaluating whether a given data
    unit is consumable by an agent independent of the surrounding
    pipeline.
  - `blog-anthropic-selfservice-data-analytics.md`: that note documents
    what a maintained semantic layer plus governed data foundations looks
    like in one company's production deployment (single-repo co-location,
    CI-enforced integrity, 95%-accuracy outcome). This article supplies
    the conceptual vocabulary (semantic meaning / relationships / temporal
    validity / machine-readable context, Claim 2; agent-readability,
    Claim 7) that the Anthropic note's practices satisfy but does not
    itself name in those terms.

- **Novel**:
  - **The precision-without-meaning / meaning-without-precision framing**
    (Claim 1) as the named root mechanism common to both structured and
    unstructured data's AI-readiness failure — not present as an explicit,
    two-sided diagnostic framing elsewhere in this corpus's ontology
    sourcing.
  - **Temporal validity as a named, distinct AI-readiness requirement**
    (Claim 2) — no prior corpus ontology/semantic-layer note names
    time-boundedness (data needing timestamps/validity periods because
    past truths may not hold now or later) as a separate dimension from
    semantic meaning or relationships.
  - **The Model Context Protocol (MCP) named as a semantic-context
    delivery mechanism** (Claim 5) — the first explicit naming of this
    specific protocol in this corpus's ontology/data-modernization
    sourcing.
  - **"Data products" as composable, self-describing units bound to
    semantic context and governance, evaluated by an "agent-readability"
    test** (Claim 7) — a new named design principle and evaluative
    question not present in the companion Xiong/Asthagiri notes or the
    Anthropic self-service-analytics note.

## Guide Impact

- **Chapter 02 (Data & Infrastructure)**: Add the structured/unstructured
  precision-vs-meaning framing (Claim 1) and the four-part AI-readiness
  requirements taxonomy (Claim 2: semantic meaning, relationships,
  temporal validity, machine-readable context) as a concrete definition of
  "AI-ready data" — filling the gap the Prospector identified in
  `blog-thoughtworks-aliyeva-werner-lammel-path-to-production.md`, which
  names "lack of AI-ready data" as a PoC-graveyard cause without defining
  what AI-readiness requires. Recommend citing this alongside that
  article's Gartner statistic (60% of AI projects abandoned through 2026
  due to lack of AI-ready data) as the problem-statement-plus-definition
  pairing.
- **Chapter 02 (Data & Infrastructure)**: Add the "data products as
  composable lego-blocks" pattern and the "agent-readability" test
  (Claim 7) as a concrete architectural unit and design checklist for
  teams building or auditing data infrastructure for agent consumption,
  paired with `blog-anthropic-selfservice-data-analytics.md`'s documented
  single-repo/CI-enforced implementation as a worked example of what
  satisfying that test looks like in practice.
- **Chapter 04 (Context Engineering)**: Add the named serialization
  mechanisms (MCP, vector databases, APIs — Claim 5) as the missing
  "how do agents actually consume this context at runtime" detail that
  neither `blog-thoughtworks-xiong-ontology-llm-data-modernization.md` nor
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md` specifies,
  positioned alongside those two notes' ontology-extraction and
  product-ownership guidance as the delivery-layer complement.
- **Chapter 04 (Context Engineering)**: Add the operational feedback-loop
  mechanism (Claim 8: live agent-workflow errors — misread fields,
  over-broad policies — feeding back into semantic-layer refinement) as a
  concrete instance of the "treat the ontology as a product" maintenance
  cadence already recommended from the Asthagiri note, specifically
  naming the signal source for when and why refinement should happen.

## Extraction Notes

1. **Full verbatim article text was not obtainable.** An initial WebFetch
   request for the complete article text was declined by the fetch tool
   citing copyright, consistent with the same limitation noted in
   `blog-thoughtworks-asthagiri-ontology-failure-modes.md`'s Extraction
   Notes. Three follow-up WebFetch calls were made instead: two requesting
   detailed section-by-section summaries (with short verbatim quotes under
   ~130 characters) covering all five of the article's sections, and a
   third requesting six specific short passages verbatim, each tied to a
   named section, to verify exact wording before quoting. All quotes above
   are drawn from these verified, individually-fetched short passages, not
   reconstructed from the summaries. The Assayer should spot-check quotes
   against the live URL, as with other WebFetch-sourced notes in this
   corpus (e.g. the Asthagiri and Xiong companion notes both note the same
   verbatim-fetch constraint).
2. **No sub-pages followed.** The article is a short, self-contained essay
   (five sections) with no inline links to deeper technical posts
   surfaced in the section-by-section summaries; unlike
   `blog-thoughtworks-aliyeva-werner-lammel-path-to-production.md`, which
   links to five external framework explainers, this article's summaries
   did not surface any comparable in-article citation links worth
   following per MINER.md §1.
3. **Two of three authors have existing, directly-overlapping solo source
   notes in this corpus** (Xiong: ontology+LLM workflow, published one day
   before this piece; Asthagiri: ontology failure modes, published five
   weeks before). This is unusually tight same-author/same-topic density
   for this corpus. Claims that closely restate those companion notes'
   content are flagged as same-author corroboration rather than
   independent replication throughout the Cross-References section above,
   to avoid overstating this article's evidentiary weight — the genuinely
   novel content is concentrated in Claims 1, 2, 5, 7, and 9 (see
   Cross-References → Novel), not in the restated ontology-extraction
   mechanics (Claim 4).
4. **No contradiction identified or filed.** Cross-referenced against all
   four notes named above plus a corpus check for any note arguing that
   semantic/ontology infrastructure is unnecessary for AI-readiness or
   that unstructured retrieval alone is sufficient; none found — see
   Cross-References → Contradicts.
5. **Confidence rated `emerging` overall**, consistent with the two
   companion solo notes by the same authors (both also rated `emerging`):
   the article is a coherent, specific, three-part conceptual/prescriptive
   framework from named practitioners, but names no client engagement,
   provides no before/after or accuracy metric, and is not benchmarked
   against an alternative approach. This is a step above `anecdotal`
   because each of the three practices is described with a specific
   mechanism (not just asserted as good practice), but below `settled`
   absent independent validation or a measured deployment outcome.
