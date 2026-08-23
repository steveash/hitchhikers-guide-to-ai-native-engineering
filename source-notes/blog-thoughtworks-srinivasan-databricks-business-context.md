---
source_url: https://www.thoughtworks.com/insights/blog/technology-strategy/agents-on-databricks-the-platform-is-ready-your-business-context-is-not
source_type: blog-post
title: "Agents on Databricks: The platform is ready, your business context is not"
author: Arun Srinivasan (Thoughtworks)
date_published: 2026-08-21
date_extracted: 2026-08-23
last_checked: 2026-08-23
status: current
confidence_overall: emerging
issue: "#2887"
---

# Agents on Databricks: The Platform Is Ready, Your Business Context Is Not

> Thoughtworks essay arguing that Databricks (via Unity Catalog) has solved
> data *access* for agents, leaving business *meaning* — agreed metric
> definitions, business language, trusted sources, evidence, and versioned
> definitions — as the remaining gap; it names three named, composable
> Databricks(-Labs) paths for closing that gap (Genie Ontology, OntoBricks,
> Ontos), proposes a five-stage maturity model (Raw → Enriched → Defined →
> Curated → Verified), and recommends organizations start from one
> high-value business decision rather than a general chatbot.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, "Technology Strategy"
  category; published August 21, 2026; discovered via the trusted
  `thoughtworks` RSS feed). A practitioner essay built around a single
  named tension (platform readiness vs. business-context readiness),
  structured through a worked ambiguity example, three named
  Databricks(-Labs) tools framed as complementary paths, a five-discipline
  checklist, a five-stage maturity model, and a closing prescriptive
  recommendation.
- **Author credibility**: Arun Srinivasan (Thoughtworks). No job title or
  bio text was surfaced on the article page itself (WebFetch returned only
  the author name with a linked profile, no visible title/bio). Srinivasan
  has one other source note in this corpus,
  `blog-thoughtworks-srinivasan-xiong-agent-reliability-operating-model.md`
  (co-authored with Zichuan Xiong, published one week earlier, 2026-08-14),
  which proposes a "truth contract" governance framework for AI agent
  reliability with seven required fields per contract (requirement,
  measurement, tolerance, owner, enforcement, failure code, dependencies).
  This article's "five disciplines" checklist is thematically adjacent —
  both are Srinivasan-authored, checklist-style governance frameworks
  published within the same month — but is a distinct framework applied to
  a different problem (establishing shared business meaning vs. testing
  system reliability at each pipeline layer); see Cross-References →
  Extends.
- **Scope**: Covers the Databricks-specific access-vs-meaning gap, one
  worked example of metric-definition ambiguity (what "revenue" means),
  three named implementation paths (Genie Ontology, OntoBricks, Ontos) with
  their release status and intended use case, five prescribed governance
  disciplines, a five-stage maturity model, and a closing scoping
  recommendation. Does NOT cover: a named client engagement, measured
  before/after accuracy figures, an implementation walkthrough of any of
  the three named tools, or the healthcare/CHF example used in
  Srinivasan's companion reliability-operating-model article — confirmed
  absent via direct query (see Extraction Notes).

## Extracted Claims

### Claim 1: Databricks has solved data *access* for agents via Unity Catalog and its governance layers, but agents still cannot reliably understand an organization's business meaning — this gap, not access, is where agent programs stall
- **Evidence**: The article's core thesis statement, framing the argument
  that follows.
- **Confidence**: emerging (a framing claim specific to Databricks-based
  agent deployments, argued from the author's stated position rather than
  a measured failure-rate study)
- **Quote**: "Access is no longer the hard part. If you're building agents on Databricks, that was solved by Unity Catalog and the governance layers around it. Your agent can reach the data but it cannot reliably understand your business; that gap is where most agent programs stall between a convincing demo and something a business will trust with a decision."
- **Our assessment**: This is the same diagnostic move made across this
  corpus's other ontology/semantic-layer sources — separating the
  *access* problem (solved) from the *meaning* problem (unsolved) — but
  pinned specifically to Databricks' own stack (Unity Catalog) rather than
  argued in platform-agnostic terms. It directly corroborates
  `blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md` Claim 2
  (the technology for autonomous AI already exists; the harder problem is
  governance, data, architecture, accountability and operating model) —
  same "platform ready, organization not" shape, applied here narrowly to
  one platform vendor's data layer rather than autonomous AI generally.

### Claim 2: A seemingly simple agent query (e.g., "last quarter's revenue") requires resolving definitional ambiguity — whether "revenue" means booked, billed, or recognized — before the agent can answer correctly
- **Evidence**: The article's opening worked example, used to motivate the
  core thesis.
- **Confidence**: anecdotal (a single illustrative example, not a named
  production incident with a health system, client, or measured outcome)
- **Quote**: "Take a seemingly simple scenario, like asking an AI agent for last quarter's revenue. Before it can answer, it has to decide whether 'revenue' means booked, billed or recognized?"
- **Our assessment**: A generic (non-client-attributed) illustrative
  example, functionally similar in structure to the metric-ambiguity
  problem this corpus has already seen in healthcare terms (Medicare
  enrollment categories in
  `blog-thoughtworks-xiong-data-agents-context-resolution.md` Claim 3) —
  same underlying failure shape (a term means different things depending
  on which system or convention defines it), different domain (finance vs.
  healthcare).

### Claim 3: Genie Ontology is Databricks' bottom-up path to business meaning — it continuously scans an organization's existing catalog assets and injects extracted knowledge into agent queries automatically, and is now in Public Preview
- **Evidence**: Named description of the first of three paths.
- **Confidence**: emerging (a specific product description tied to a
  stated release status, not independently verified against Databricks'
  own product documentation)
- **Quote**: "Genie continuously scans your notebooks, dashboards, pipelines, files and catalog lineage, extracts knowledge snippets, scores each for authority and injects the relevant ones into the agent loop at query time under your existing permissions."
- **Quote**: "Genie Ontology is the bottom-up path, and the one now in Public Preview."
- **Our assessment**: The "continuously scans... under your existing
  permissions" mechanism is structurally close to
  `blog-thoughtworks-gall-layered-context-enterprise-data.md` Claim 7's
  proposal to build a "harness" that passively discovers relationships
  from employees' unintentional digital trails, rather than requiring
  upfront manual mapping — both treat automated, continuous discovery as
  preferable to a one-time curation exercise. See Cross-References for how
  this sits against the already-filed contradiction #2458 on this exact
  question.

### Claim 4: OntoBricks is Databricks' top-down path — a Databricks Labs (exploration-grade, not SLA-backed) tool for designing formal ontologies or importing industry standards such as FIBO, FHIR, and CDISC, and reasoning over them on the lakehouse
- **Evidence**: Named description of the second of three paths.
- **Confidence**: emerging (specific product description; explicitly
  flagged by the source itself as "exploration-grade rather than
  SLA-backed," i.e., not production-hardened)
- **Quote**: "OntoBricks is the top-down path, a Databricks Labs project and so exploration-grade rather than SLA-backed. You design formal ontologies or import industry standards such as FIBO, FHIR and CDISC, then materialize and reason over them on the lakehouse."
- **Our assessment**: This directly extends the formal-ontology-import
  concept named generically in
  `blog-thoughtworks-xiong-ontology-llm-data-modernization.md` Claim 1
  (an ontology as "the schema layer of a knowledge graph") by naming a
  concrete Databricks-native tool and naming specific regulated-domain
  standards (FIBO for finance, FHIR for healthcare, CDISC for clinical
  trials) as import targets — a level of implementation specificity absent
  from the earlier, platform-agnostic ontology sources in this corpus.

### Claim 5: Ontos is Databricks' curated path — a Databricks Labs business-catalog layer over Unity Catalog built around data products, data contracts, and ownership, aimed at organizations whose gap is ownership and agreements rather than technology
- **Evidence**: Named description of the third of three paths.
- **Confidence**: emerging (specific product description; also explicitly
  flagged as a Labs/exploration-grade project)
- **Quote**: "Ontos is the curated path, also Labs. It puts a business catalog over Unity Catalog with data products, data contracts and compliance rules, built for organizations whose gap is ownership and agreements rather than technology."
- **Our assessment**: "Data products, data contracts" directly corroborates
  the "domain-aware data products" architectural unit already in this
  corpus (`blog-thoughtworks-xiong-data-agents-context-resolution.md`
  Claim 9's "prefer domain-aware data products,"
  `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md` Claim 7's
  self-describing data-product packaging) — this article supplies a named,
  Databricks-specific product (Ontos) implementing that same
  architectural pattern.

### Claim 6: The three paths (Genie Ontology, OntoBricks, Ontos) are complementary rather than competing, and organizations should select among them by the type of question being answered — fast natural-language analytics, formal/regulated reasoning, or ownership and contracts
- **Evidence**: The article's explicit synthesis of the three paths, under
  a "three paths, three questions" framing.
- **Confidence**: emerging (a prescriptive framing claim from the author,
  not validated against an organization that has actually combined all
  three)
- **Quote**: "Pick by the question you are answering. Trustworthy natural-language analytics, quickly and with little configuration, points to Genie Ontology. Formal semantics, inference and regulated standards point to OntoBricks. Ownership, contracts and data products point to Ontos."
- **Quote**: "They compose. They do not compete."
- **Our assessment**: This "pick by the question" framing is consistent
  with `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 2
  (schemas, controlled vocabularies, semantic layers, ontologies, and
  knowledge graphs sit on a single continuum rather than being competing
  choices) — both sources reject a single "correct" semantic-tooling
  choice in favor of matching tool formality to the specific question or
  gap at hand.

### Claim 7: Organizations must fix metric definitions first — for each core metric, settling the formula, owner, allowed dimensions, system of record, temporal rule, and permitted exceptions
- **Evidence**: First of the article's five prescribed disciplines.
- **Confidence**: emerging (a specific, actionable prescription, not tied
  to a measured before/after outcome)
- **Quote**: "Settle revenue, margin, churn, active customer and service level first. For each, fix the formula, the owner, the allowed dimensions, the system of record, the temporal rule for when the definition applies and the exceptions you permit."
- **Our assessment**: This six-field metric-definition checklist
  (formula, owner, dimensions, system of record, temporal rule,
  exceptions) is structurally similar to the seven-field "truth contract"
  in Srinivasan's own companion note
  (`blog-thoughtworks-srinivasan-xiong-agent-reliability-operating-model.md`
  Claim 5: requirement, measurement, tolerance, owner, enforcement,
  failure code, dependencies) — same author, same instinct to replace a
  vague definition with an explicit, ownable, multi-field contract, applied
  here to metric semantics rather than to system reliability testing.

### Claim 8: Business language must be explicitly reconciled across teams — the same term (customer, account, household, product, supplier) means different things to different teams, and the relationships between these entities carry meaning too
- **Evidence**: Second of the article's five prescribed disciplines.
- **Confidence**: emerging (a specific, named prescription)
- **Quote**: "Customer, account, household, product and supplier mean different things to different teams, and the relationships between them carry meaning too."
- **Our assessment**: This directly corroborates the "semantic-collision
  gap" already named in
  `blog-thoughtworks-xiong-ontology-llm-data-modernization.md` Claim 8 (a
  shared type name across systems does not imply shared meaning,
  illustrated there by `BillingStatus`/`TicketStatus` both typed `Status`
  with opposite implications) — this article names the same failure
  category using business-entity examples (customer, account, household)
  rather than a code-level type-system example.

### Claim 9: Trusted sources should be identified by letting the platform compute authority and surface candidates, with human owners then confirming the actual source of record for the metrics that matter
- **Evidence**: Third of the article's five prescribed disciplines.
- **Confidence**: emerging
- **Quote**: "Let the platform compute authority and do the discovery, then have owners confirm the source of record for the metrics that matter."
- **Our assessment**: This is a hybrid stance in the automated-discovery
  vs. human-curation tension this corpus already tracks under contradiction
  #2458 — the platform (i.e., Genie Ontology-style continuous scanning, per
  Claim 3) does the discovery work, but a human owner still performs a
  confirmation step before the source is trusted. It sits closer to Side A
  of #2458 (human-confirmed curation) than to Gall's fully passive,
  harvest-only Side B, despite using automated discovery as an input.

### Claim 10: Agents should be required to cite evidence for every assertion — pointing back to a document passage, a table row, a policy, or a recorded decision
- **Evidence**: Fourth of the article's five prescribed disciplines.
- **Confidence**: emerging
- **Quote**: "If an agent asserts something, it should point back to a document passage, a table row, a policy or a recorded decision."
- **Our assessment**: A standard evidence-citation prescription, consistent
  with (though less developed than) the "truth contract" testability
  requirement in Srinivasan's companion note, and with this corpus's
  broader theme that agent trustworthiness requires traceable evidence
  rather than an unverifiable natural-language answer.

### Claim 11: For high-risk decisions, organizations should keep a versioned layer of approved definitions separate from the live/learned one, pin agents to a named release, and test against that release rather than against shifting current records
- **Evidence**: Fifth of the article's five prescribed disciplines.
- **Confidence**: emerging
- **Quote**: "Keep a versioned layer of approved definitions alongside the learned one, pin your agents to a named release, and test against that release rather than against shifting current records."
- **Our assessment**: This "pin to a named release, test against it"
  practice is a specific, testable instantiation of the same instinct
  behind Srinivasan's own "truth contract" testability requirement
  (companion note, Claim 6: "a truth contract is only meaningful if it is
  executable") — treating a business definition itself as a versioned,
  pinned artifact rather than a live, silently-drifting one.

### Claim 12: Organizational semantic-layer maturity progresses through five stages — Raw (no extraction), Enriched (tags/descriptions accumulating), Defined (glossary + steward workflows), Curated (metric views driving dashboards/agents, domain organization), and Verified (certified assets, consistently rated agent answers)
- **Evidence**: The article's named maturity model, given as five stage
  descriptions.
- **Confidence**: emerging (a named self-assessment framework proposed by
  the author, not validated against multiple organizations placed on the
  scale)
- **Quote**: "Catalog objects carry no descriptions or tags. No knowledge is being extracted." (Raw)
- **Quote**: "Governed tags and rich descriptions on the tables that matter. Knowledge accumulating from your sources." (Enriched)
- **Quote**: "Glossary pages drafted, steward approval workflows running, extracted knowledge feeding your glossary and metric definitions." (Defined)
- **Quote**: "Metric views driving dashboards and agents. Domains organizing the catalog. Domain-specific agents in real use." (Curated)
- **Quote**: "Assets certified, deprecated and classified. Agent answers consistently rated to produce high-quality signal." (Verified)
- **Our assessment**: This is a new, named framework in this corpus — no
  existing source note proposes a comparable staged maturity scale for
  organizational semantic-layer readiness specifically (as distinct from
  general AI-adoption maturity models). Its explicit inclusion of a
  "steward approval workflow" at the Defined stage reinforces that even
  the Genie Ontology automated-scanning path (Claim 3) still routes
  through human stewardship before an organization can be considered
  past the earliest maturity stages — tempering a reading of Claim 3 as
  fully automation-only.

### Claim 13: Organizations should start their business-context work from a single high-value business decision where meaning is currently expensive, rather than building a general-purpose chatbot
- **Evidence**: The article's closing recommendation.
- **Confidence**: anecdotal (a prescriptive recommendation, no described
  before/after case of an organization following this advice)
- **Quote**: "Pick a business process where the decisions carry weight, then find the decision where meaning is expensive"
- **Quote**: "'Which customer contracts are at risk, why, and what evidence supports that view?' is a far better test of readiness than a general chat interface."
- **Our assessment**: This directly corroborates
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 9
  (scope ontology work to one funded use case, using "competency
  questions" as a funding gate) and Claim 10 (build the smallest semantic
  structure that answers a funded question) — same "scope to one concrete
  decision, not a general capability" prescription, independently arrived
  at by a different Thoughtworks author on a different platform.

## Concrete Artifacts

```
Source: Arun Srinivasan, "Agents on Databricks: The platform is ready,
your business context is not," Thoughtworks Insights, August 21, 2026

Three paths to business meaning:

| Path            | Orientation | Status                          | Best for                                  |
|------------------|-------------|----------------------------------|--------------------------------------------|
| Genie Ontology   | Bottom-up   | Public Preview                   | Trustworthy natural-language analytics,   |
|                  |             |                                   | quickly, with little configuration        |
| OntoBricks       | Top-down    | Databricks Labs (exploration-grade,| Formal semantics, inference, regulated  |
|                  |             | not SLA-backed)                  | standards (FIBO, FHIR, CDISC)              |
| Ontos            | Curated     | Databricks Labs                  | Ownership, contracts, data products       |

"They compose. They do not compete." — all three read from the same
underlying agreed definitions, so "the quality of what you put in sets
the ceiling on what you get out."
```

```
Five disciplines for establishing business context
(paraphrased headings; quotes captured per-claim above):

1. Metrics — fix formula, owner, dimensions, system of record, temporal
   rule, and exceptions for each core metric.
2. Business language — reconcile what shared terms (customer, account,
   household, product, supplier) mean across teams, including
   relationships between entities.
3. Trusted sources — platform computes authority/discovery; owners
   confirm the source of record.
4. Evidence — every agent assertion should cite a document passage,
   table row, policy, or recorded decision.
5. Versioned definitions — keep a versioned, pinned layer of approved
   definitions for high-risk decisions; test against the pinned release.
```

```
Five-stage maturity model (measured across "what the catalog knows" and
"what agents can use"):

Raw       -> No descriptions/tags; no knowledge extraction
Enriched  -> Governed tags/descriptions on key tables; knowledge accumulating
Defined   -> Glossary drafted; steward approval workflows running
Curated   -> Metric views driving dashboards/agents; domains organized;
             domain-specific agents in real use
Verified  -> Assets certified/deprecated/classified; agent answers
             consistently rated for quality
```

## Cross-References

### Cross-reference verification notes
`blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md`,
`blog-thoughtworks-asthagiri-ontology-failure-modes.md`,
`blog-thoughtworks-xiong-ontology-llm-data-modernization.md`,
`blog-thoughtworks-xiong-data-agents-context-resolution.md`,
`blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md`,
`blog-thoughtworks-gall-layered-context-enterprise-data.md`,
`blog-latentspace-databricks-agent-clouds.md`, and
`blog-thoughtworks-srinivasan-xiong-agent-reliability-operating-model.md`
were re-read in full (or, for the two already re-read while drafting
`blog-thoughtworks-xiong-data-agents-context-resolution.md` in this same
session, re-checked against their numbered `### Claim N:` headings) before
writing the citations below; all claim numbers cited were confirmed
against each note's headings in document order.

- **Corroborates**:
  - `blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md` Claim 2
    (the technology for autonomous AI already exists; the harder enterprise
    problem is governance, data, architecture, accountability and
    operating model): this article's Claim 1 (Unity Catalog solved access;
    business meaning is the unsolved gap) is the same "platform ready,
    organization not" shape, narrowed to one vendor's data-access layer.
  - `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 2
    (schemas, controlled vocabularies, semantic layers, ontologies, and
    knowledge graphs sit on a single continuum rather than competing
    choices) and Claim 9 (scope to one funded use case via "competency
    questions" as a funding gate): this article's Claim 6 ("pick by the
    question you are answering... they compose, they do not compete") and
    Claim 13 (start from one high-value decision, not a general chatbot)
    independently arrive at the same two prescriptions from a different
    author and a Databricks-specific angle.
  - `blog-thoughtworks-xiong-ontology-llm-data-modernization.md` Claim 1
    (an ontology as the schema layer of a knowledge graph) and Claim 8 (a
    shared type name across systems does not imply shared meaning — the
    "semantic-collision gap"): this article's Claim 4 (OntoBricks: formal
    ontologies, FIBO/FHIR/CDISC) names a concrete tool implementing the
    first, and Claim 8 (customer/account/household mean different things
    to different teams) restates the second using business-entity rather
    than code-type examples.
  - `blog-thoughtworks-xiong-data-agents-context-resolution.md` Claim 9
    (prefer domain-aware data products) and
    `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md` Claim 7
    (self-describing "data products" packaging data, metadata, meaning,
    and governance): this article's Claim 5 (Ontos: data products, data
    contracts, ownership) names a specific Databricks-native tool
    implementing the same architectural pattern both of those notes
    prescribe in platform-agnostic terms.

- **Extends**:
  - `blog-latentspace-databricks-agent-clouds.md` Claim 11 (the concrete
    motivating case for Databricks' LTAP was agents needing live
    operational database state — "who's placing those orders, what is
    happening" — because product telemetry alone was insufficient
    context): that note documents Databricks solving live-data *access*
    for agents; this article, on the same platform, extends the argument
    one layer up — showing that solved access still leaves the *meaning*
    of that data (what "revenue" or "customer" refers to) unresolved. Read
    together, they cover Databricks' agent story end-to-end: access
    (LTAP/Unity Catalog) then meaning (Genie Ontology/OntoBricks/Ontos).
  - `blog-thoughtworks-xiong-data-agents-context-resolution.md` Claim 6
    (context resolution — reconciling how independent source systems
    represent the same concept — is the critical, currently uncontrolled
    point where data agents fail): this article extends that diagnosis by
    naming three concrete, named Databricks(-Labs) tools as candidate
    implementations for closing exactly that control gap, though it does
    not itself claim any of the three has been validated as a fix for a
    documented failure (no worked failure case appears in this article;
    see Extraction Notes on the absent healthcare/CHF crossover).
  - `blog-thoughtworks-srinivasan-xiong-agent-reliability-operating-model.md`
    Claim 5 (a "truth contract" requires seven fields: requirement,
    measurement, tolerance, owner, enforcement, failure code,
    dependencies) and Claim 6 (a truth contract is only meaningful if it
    is executable/testable): this article's five disciplines (Claims
    7-11), especially the metrics discipline's six-field checklist and the
    versioned-definitions discipline's "pin to a named release, test
    against it," extend the same author's contract-based governance
    instinct from system-reliability testing (the companion note) to
    business-meaning establishment (this article) — a second, adjacent
    application of the same "make it an explicit, ownable, testable
    contract" pattern within a single week of Thoughtworks publications by
    the same author.

- **Contradicts**: None filed as a new issue. This article's overall
  stance — build and maintain named semantic-layer tooling (Genie
  Ontology, OntoBricks, Ontos) with owners, stewards, and versioned
  definitions (Claims 3-5, 7-12) — sits on the same side of the
  already-filed contradiction
  [#2458](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/2458)
  as `blog-thoughtworks-asthagiri-ontology-failure-modes.md` and
  `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md` (the
  "curate and codify as core infrastructure" position), rather than
  `blog-thoughtworks-gall-layered-context-enterprise-data.md`'s "curation
  is dead on arrival, harvest passively instead" position. One nuance
  worth flagging for the Assayer/Smith: this article's Genie Ontology path
  (Claim 3, "continuously scans... and injects... under your existing
  permissions") uses automated, continuous, non-manual discovery as an
  *input* mechanism — structurally closer to Gall's passive-harvesting
  proposal than to Asthagiri's SME-driven curation — but the article still
  routes that discovery through human owner confirmation (Claim 9) and a
  named "steward approval workflow" at its Defined maturity stage
  (Claim 12), which keeps its overall position on the Side A side of
  #2458. This is additional same-side evidence with one internal nuance,
  not a new disagreement — no new issue filed, per MINER.md §4a's guidance
  to check existing filed contradictions first.

- **Novel**:
  - **Three named, complementary Databricks(-Labs) implementation paths**
    (Claims 3-6, Concrete Artifacts) — Genie Ontology, OntoBricks, and
    Ontos, each with a stated release status (Public Preview vs. Labs
    exploration-grade) and a "pick by the question" selection criterion —
    is the first source note in this corpus to name specific,
    vendor-shipped tooling options for the semantic/business-context layer,
    as opposed to platform-agnostic prescriptions.
  - **The five-stage maturity model** (Raw → Enriched → Defined → Curated
    → Verified, Claim 12) is a new named self-assessment framework not
    present elsewhere in this corpus's ontology/context-engineering
    sources.
  - **The five-discipline checklist framed as a governance contract**
    (Claims 7-11) is new in its specific field-level detail (e.g., the
    six-field metric-definition checklist), though thematically it is the
    same author's second contract-style governance framework published
    within a week (see Extends, above).

## Guide Impact

- **Chapter 04 (Context Engineering)**: Add the "three named paths, pick
  by the question" framework (Claim 6, Concrete Artifacts) as a concrete
  decision aid for teams choosing semantic-layer tooling on Databricks —
  distinct from this corpus's existing platform-agnostic ontology guidance
  (Asthagiri, Xiong) by naming actual product options and their maturity
  status. Add the five-discipline checklist (Claims 7-11) as a concrete
  audit checklist teams can apply directly, cross-linked to the existing
  "ontology as a product" guidance already sourced from
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md`.
- **Chapter 02 (Harness Engineering)**: Add the five-stage maturity model
  (Raw → Enriched → Defined → Curated → Verified, Claim 12) as a
  self-assessment scale teams can use to locate where their own catalog
  and agent-context work currently sits — the guide currently has no
  comparable staged maturity scale specific to organizational
  semantic-layer readiness.
- **Chapter 05 (Team Adoption)**: Reinforce the existing "scope to one
  funded/high-value decision, not a general chatbot" guidance (already
  sourced from Asthagiri's Claims 9-10) with this article's independently
  arrived-at Claim 13 and its concrete example question ("which customer
  contracts are at risk, why, and what evidence supports that view?") as
  an additional, Databricks-specific illustration for the guide.

## Extraction Notes

- **Full verbatim article text was not obtainable via a single WebFetch
  pass**, consistent with other Thoughtworks pieces already in this
  corpus. An initial WebFetch request returned a paraphrased
  section-by-section summary. Five follow-up WebFetch calls were made,
  each requesting only short (under-40/50-word), verbatim, contiguous
  passages tied to specific named claims, with explicit instructions not
  to paraphrase or splice non-adjacent sentences into a single quote. All
  quotes above are drawn from these verified short-passage fetches.
  Because this source could not be retrieved as a single clean document,
  the Assayer should spot-check quotes against the live URL, particularly
  the maturity-model stage descriptions and the five-discipline quotes,
  which were retrieved together in batches.
- **Checked for, and confirmed absent, a healthcare/CHF crossover with
  Srinivasan's companion article.** Given that the same author's
  `blog-thoughtworks-srinivasan-xiong-agent-reliability-operating-model.md`
  (published one week earlier) centers on a CHF readmission-rate healthcare
  example, a targeted WebFetch call explicitly checked whether this
  article reuses that example or mentions healthcare, CHF, readmission
  rates, or Medicare. It does not — this article's only worked example is
  the "revenue: booked, billed, or recognized?" ambiguity (Claim 2), and
  its metrics discipline example uses revenue, margin, churn, active
  customer, and service level (Claim 7), not healthcare metrics.
- **No author title/bio found on the article page.** Unlike some other
  Thoughtworks source notes in this corpus where a distinct profile-page
  WebFetch surfaced a stated title, this article's byline area returned
  only "Arun Srinivasan" with a linked profile and no visible title or bio
  text. The frontmatter author field is left as "Arun Srinivasan
  (Thoughtworks)" without a title, matching the format used in the
  companion `blog-thoughtworks-srinivasan-xiong-agent-reliability-operating-model.md`
  note's author line.
- **Prospector triage discrepancy.** This issue carries three separate
  triage comments with differing novelty assessments (medium, medium,
  high) and differing "relevant chapters" and "existing notes that
  overlap" lists — the first two comments' reasoning reads as speculative
  about likely article content (one guesses at "organizational
  readiness/governance" themes not actually present in the article; e.g.
  neither mentions Genie Ontology, OntoBricks, or Ontos by name), while
  the third comment's specifics (the three named paths, the five
  disciplines) match the actual article content closely, suggesting only
  the third triage pass actually read the source. This note follows the
  third comment's framing and chapter recommendations (Ch02, Ch04) and
  adds Ch05 based on this note's own reading of the closing
  recommendation (Claim 13), rather than the first two comments'
  Ch05-as-"organizational readiness" framing, since the article's actual
  content is about scoping semantic-layer work to one decision, not about
  broader organizational-readiness factors (funding, stakeholder
  engagement) as such.
- **No new contradiction filed.** This article's overall stance is
  additional same-side evidence for the existing, already-filed
  contradiction [#2458](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/2458),
  with one internal nuance noted under Cross-References → Contradicts. Per
  MINER.md §4a, no new issue was filed since the disagreement is already
  tracked.
- **Confidence rated `emerging` overall.** The article's central framework
  (three named paths + five disciplines + maturity model) is specific,
  internally coherent, and corroborated piece-by-piece by several
  independent, differently-authored sources already in this corpus.
  However, it rests on the author's own prescriptive framing rather than a
  named client engagement or measured outcome, two of the three named
  tools (OntoBricks, Ontos) are explicitly self-described as
  Labs/exploration-grade rather than production-hardened, and the worked
  example (revenue definition ambiguity) is generic and unattributed. This
  matches the `emerging` rating given to Srinivasan's companion note and
  to the other Thoughtworks ontology/context sources in this corpus.
