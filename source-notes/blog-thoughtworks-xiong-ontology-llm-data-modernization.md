---
source_url: https://www.thoughtworks.com/insights/blog/legacy-modernization/an-ontology-LLM-approach-to-data-modernization
source_type: blog-post
title: "Closing the context gap: An ontology + LLM approach to data modernization"
author: Zichuan Xiong (Thoughtworks)
date_published: 2026-07-22
date_extracted: 2026-08-01
last_checked: 2026-08-01
status: current
confidence_overall: emerging
issue: "#2390"
---

# Closing the Context Gap: An Ontology + LLM Approach to Data Modernization

> Thoughtworks practitioner essay proposing a six-step agentic workflow —
> build ontological context per source, curate/reconcile across sources,
> compare against a use case's design context, classify the resulting gaps,
> act on them, then update and loop — that combines ontologies (explicit,
> verifiable semantic structure) with LLMs (fast but unverifiable inference)
> to accelerate enterprise data-modernization discovery, illustrated with a
> worked churn-forecasting example across billing and support systems.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, published July 22, 2026;
  from the trusted `thoughtworks` RSS feed. Six-section practitioner essay:
  intro, "The ontology + LLM approach," "What is an ontology?," "Why does
  combining ontology and LLMs matter?," "A step-by-step example" (with six
  numbered Step subsections), and "Summary.")
- **Author credibility**: Zichuan Xiong, byline on Thoughtworks' commercial
  insights blog; no further title, role, or track record is given in the
  article itself. The piece is a conceptual/methodological essay illustrated
  with a single constructed (not named-client) example — a two-system
  (billing + support) churn-forecasting scenario — rather than a documented
  production case study with before/after metrics. Thoughtworks is already
  an established trusted source in this corpus (see
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md`,
  `blog-thoughtworks-gall-supervisory-engineering.md`,
  `blog-thoughtworks-anand-agent-evaluation-framework.md`).
- **Scope**: Covers a definition of "ontology," a rationale for combining
  ontologies with LLMs, and a six-step agentic workflow walked through via
  one illustrative example (billing + support systems, churn forecasting).
  Does NOT cover: a named client engagement or outcome metrics, the specific
  prompting/tooling used to run the "AI agent" described in Step 1, how the
  ontology is stored or version-controlled in practice (beyond asserting it
  "can be kept under source control"), or a comparison against alternative
  approaches (e.g., schema-only inference without any ontology layer) beyond
  the one-paragraph "point an LLM straight at the problem" framing used to
  motivate the ontology layer.

## Extracted Claims

### Claim 1: An ontology is a schema of meaning — the entities, attributes, relationships, and rules of a domain, expressed as the schema layer of a knowledge graph before any instance data populates it
- **Evidence**: Direct definitional statement in the "What is an ontology?"
  section.
- **Confidence**: settled (standard semantic-web/data-architecture
  terminology, consistent with how the term is defined elsewhere in this
  corpus)
- **Quote**: "An ontology is a schema of meaning: it defines the entities that exist, their attributes, the relationships between them and the rules that govern them."
- **Our assessment**: This definition is materially identical to
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 3's
  distinction ("An ontology is a blueprint: the classes, the relationships
  and the rules"). Two independent Thoughtworks authors, writing five weeks
  apart, converge on the same "ontology = schema/blueprint, knowledge graph
  = populated instance" framing — this is corroborating consensus within
  the corpus, not a novel claim on its own, but it establishes this article
  is using the term consistently with prior-mined usage.

### Claim 2: Pointing an LLM directly at source systems without explicit semantic context is a reasonable starting point, but the LLM's inferences from schemas, column names, and sample values are difficult to verify consistently at enterprise scale
- **Evidence**: Author's framing argument in "The ontology + LLM approach"
  section, used to motivate why an ontology layer is needed at all.
- **Confidence**: emerging (a design-principle claim, illustrated but not
  measured against a controlled comparison in this article)
- **Quote**: "Without explicit semantic context, the LLM must infer relationships from schemas, column names and sample values. Those inferences can be useful, but they are difficult to verify consistently at enterprise scale."
- **Our assessment**: This is the article's stated justification for the
  entire methodology and directly corroborates
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 4's point
  that ontology's retrieval/verifiability benefit only exists once a
  populated, entity-resolved graph exists — both articles independently
  argue that LLM-only schema inference is a real capability but an
  unverifiable one at scale, which is exactly the gap an ontology is
  proposed to close.

### Claim 3: Ontologies and LLMs cover each other's weaknesses — the ontology grounds reasoning in explicit, verifiable semantics, while the LLM does the manual work (reading source systems, aligning synonyms, proposing reconciliations, spotting mismatches) that would otherwise make hand-built ontologies tedious
- **Evidence**: Direct statement in "Why does combining ontology and LLMs
  matter?" section.
- **Confidence**: emerging (a design-principle claim; plausible and
  internally consistent with Claim 1/2, but not independently measured)
- **Quote**: "Ontology and LLMs cover each other's weaknesses."
- **Quote**: "The LLM, in turn, does the work that would otherwise make ontologies are tedious to build by hand: reading source systems, aligning synonyms, proposing reconciliations, spotting mismatches."
- **Our assessment**: The second quote preserves an apparent copy-edit typo
  in the source ("make ontologies are tedious to build" — likely a leftover
  fragment from a sentence revision); quoted verbatim per MINER.md §2a
  rather than silently corrected. The underlying claim — LLMs substitute for
  the manual labor of hand-building an ontology, while the ontology supplies
  verifiability the LLM alone can't — is the article's central thesis and
  is a specific, agentic-AI-native instance of
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 9's "curate,
  don't draft from scratch" practice (using LLM pipelines to pull draft
  taxonomies from existing schemas, API definitions and wikis), applied here
  as a repeatable six-step loop rather than a one-time drafting step.

### Claim 4: The methodology operates as a repeatable six-step agentic loop — build ontological context per source, curate/reconcile context across sources, compare the design context against the curated context, identify gaps, take actions, then update the context and loop — rather than a one-off discovery exercise
- **Evidence**: Structural framing of "A step-by-step example" section,
  with each step given its own numbered subsection heading.
- **Confidence**: emerging (a novel process framing, illustrated with one
  worked example but not validated against multiple independent engagements
  in this article)
- **Quote**: "In practical terms, this method operates as an agentic loop consistingcomprised of six distinct steps"
- **Our assessment**: The quote preserves a visible copy-edit artifact
  ("consistingcomprised" — apparently two edited phrasings left merged in
  the published text) verbatim per MINER.md §2a. This six-step loop is the
  article's core, novel contribution to the corpus: no existing source note
  names this specific sequence (per-source ontology extraction → cross-
  source reconciliation → design-context comparison → gap classification →
  action → update-and-repeat) as a named, repeatable agentic workflow for
  data-modernization discovery specifically.

### Claim 5: In Step 1, an AI agent reads each source system's schema and data types, foreign keys and join patterns, sample values, and comments/documentation to infer a candidate ontology, flagging low-confidence guesses for an SME to confirm
- **Evidence**: Direct description of Step 1's mechanism, plus a worked
  example (two source systems: billing and support ticketing).
- **Confidence**: emerging (a specific technique description, illustrated
  with one example but not benchmarked against alternative extraction
  approaches or measured for extraction accuracy)
- **Quote**: "The agent reads across signals in each file:, schema and data types, foreign keys and join patterns, sample values and any comments or documentation, then infers a candidate ontology and flags low-confidence guesses for an SME to confirm."
- **Our assessment**: "Flags low-confidence guesses for an SME to confirm"
  is the article's specific confidence-scoring/human-verification mechanism
  — structurally similar to the general SME-validation pattern in
  `blog-thoughtworks-anand-agent-evaluation-framework.md` (persona-based and
  unit-eval layers requiring human/stakeholder validation before production)
  and to the "curate, don't draft from scratch" LLM-assisted extraction in
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 9, but
  applied specifically to per-source ontology inference rather than general
  taxonomy drafting or agent-output evaluation. The stray punctuation ("in
  each file:,") is preserved verbatim from the source per MINER.md §2a.

### Claim 6: Reconciling ontologies across multiple source systems surfaces use-case-agnostic gaps — duplicate identities, conflicting definitions, and overlapping concepts — that exist in the data landscape regardless of whether any specific use case cares about them, and require a human expert to recommend and resolve
- **Evidence**: Direct description of Step 2's outcome, with the worked
  example surfacing three specific gaps (shared EmailAddress, Account vs.
  Customer, shared Status type).
- **Confidence**: emerging
- **Quote**: "Reconciling multiple ontologies highlights inconsistencies such as duplicate identities, conflicting definitions and overlapping concepts that would otherwise remain hidden. These require a human expert to recommend and resolve."
- **Quote**: "These gaps are use-case agnostic. They exist in the landscape whether or not any use case cares about them, which is precisely why a human expert or an AI agent can be made aware of them up front."
- **Our assessment**: The "use-case agnostic" framing is a specific,
  useful distinction — it separates landscape-level semantic debt
  (inconsistencies that exist independent of any project) from the
  project-level question of which of those inconsistencies actually matter
  for a given use case (addressed next, in Claim 7/8). This two-stage
  separation (agnostic discovery, then use-case-specific triage) is not
  named this way in `blog-thoughtworks-asthagiri-ontology-failure-modes.md`,
  which discusses ontology scope/maintenance at a program level rather than
  as a per-use-case comparison step.

### Claim 7: Comparing a use case's own design context (its implicit required entities and relationships, expressed as an ontology) against the curated, cross-source context turns previously abstract, use-case-agnostic gaps into concrete, actionable ones
- **Evidence**: Direct description of Step 3, illustrated by the churn-
  forecasting use case requiring "a single, unambiguous Customer entity"
  unifying commercial and behavioral signals under one resolved identity.
- **Confidence**: emerging
- **Quote**: "By matching this design context against the curated, reconciled context from Step 2, the previously use-case-agnostic gaps become practical."
- **Our assessment**: This is the mechanism that operationalizes Claim 6 —
  it names the specific step where general semantic debt becomes a concrete,
  scoped decision for a specific project, rather than leaving "reconcile
  your ontologies" as an open-ended, never-finished exercise. This is a
  practical, structural counter to the scope-creep failure mode named in
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 7 (teams
  tempted to model all of reality before shipping): here, the design-context
  comparison step forces gap identification to be scoped to what a specific,
  funded use case actually needs, which is functionally similar in spirit to
  Asthagiri's "competency questions as a funding gate" (Claim 9) though this
  article does not use that vocabulary or frame it as a funding gate.

### Claim 8: A shared type name across systems does not imply shared meaning — the article names this a "semantic-collision gap," illustrated by BillingStatus and TicketStatus both being typed Status while `closed` means a healthy outcome for a ticket and a churn signal for billing
- **Evidence**: Direct description of "Gap 3" in Step 4, the article's most
  concrete illustration of a named gap type.
- **Confidence**: emerging (a single constructed illustrative example, not
  a documented case)
- **Quote**: "A shared type does not mean shared meaning."
- **Quote**: "This is a semantic-collision gap"
- **Our assessment**: "Semantic-collision gap" is a specific, quotable named
  failure mode not present elsewhere in this corpus in this form. It is a
  concrete worked instance of the more general point in
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 7 (a
  translation gap between formal modeling and business meaning) and Claim 5
  (ontologies make meaning explicit and verifiable) — this article supplies
  a specific, memorable example (`Status` meaning opposite things in two
  systems) of exactly the kind of tacit-meaning collision an ontology is
  meant to surface before it silently corrupts a downstream model label.

### Claim 9: The three gaps identified for the churn use case resolve into three genuinely different action plans — an internal reconciliation rule, an SME grain decision requiring human judgment before any code change, and a semantic disambiguation — each with different costs, owners, and a dependency order, all knowable before committing engineering time
- **Evidence**: Direct description of Step 5's outcome, synthesizing the
  three gaps identified in Step 4.
- **Confidence**: emerging
- **Quote**: "The \"three gaps\" resolve into three genuinely different plans: a reconciliation rule, an SME grain decision and a semantic disambiguation, with different costs, different owners and a dependency order between them. The strategist knows all of this before committing a quarter to the build."
- **Our assessment**: "Before committing a quarter to the build" is the
  article's clearest concrete claim about the value of the workflow: it
  argues the gap-classification step (Steps 3-4) front-loads
  scoping/costing decisions that would otherwise surface mid-build. No
  metric or named project is given to substantiate the "a quarter" figure —
  it reads as illustrative, not measured — but the underlying mechanism
  (different gap types require different owners and have a dependency
  order) is a specific, actionable planning heuristic distinct from a
  generic "do gap analysis first" recommendation.

### Claim 10: Even though AI can identify and classify potential gaps, governance remains essential — business owners and domain experts are responsible for validating entity definitions, resolving semantic conflicts, and approving changes that affect enterprise-wide data models
- **Evidence**: Direct statement immediately following Step 4's gap
  classification, functioning as an explicit governance caveat on the
  agentic workflow.
- **Confidence**: emerging
- **Quote**: "While AI can identify and classify potential gaps, governance remains essential. Business owners and domain experts are responsible for validating entity definitions, resolving semantic conflicts and approving changes that affect enterprise-wide data models."
- **Our assessment**: This is functionally the same human-in-the-loop
  governance principle as
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 5 (a rule
  only binds when a deterministic runtime/human process checks it) applied
  specifically to ontology gap-resolution decisions rather than to
  ontology-encoded agent guardrails generally — both sources independently
  insist that AI's role is limited to identification/classification, with
  binding decisions reserved for humans.

### Claim 11: Context must be managed as a continuously-updated, version-controlled semantic asset at the landscape level rather than a static, one-time design document — each resolved gap becomes the new baseline that the next use case and the next agent inherit rather than rediscover
- **Evidence**: Direct description of Step 6 ("Update the source context and
  loop").
- **Confidence**: emerging
- **Quote**: "This is why context must be managed as a service at the landscape level, not a document or one-time snapshot. Rather than documenting enterprise knowledge in static design documents, organizations can maintain it as a living, version-controlled semantic asset that every future project and AI agent can reuse."
- **Our assessment**: This directly corroborates
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 8 ("treat
  the ontology as a product, not a project") and Claim 6 (a shared ontology
  goes stale within roughly two quarters without a steward and reconciliation
  cadence) — this article supplies the specific mechanism by which that
  ongoing maintenance happens (each use case's resolved gaps become the new
  baseline, closing the loop rather than starting from scratch each time),
  which Asthagiri's article asserts as a prescription but does not itself
  describe procedurally.

## Concrete Artifacts

```
Six-step agentic workflow (as headed in the article's "A step-by-step
example" section)
Source: Zichuan Xiong, "Closing the context gap: An ontology + LLM approach
to data modernization," Thoughtworks Insights, July 22, 2026

Step 1: Build ontological context per source
Step 2: Curate context across sources, then reconcile
Step 3: Compare the design context against the curated (reconciled) context
Step 4: Identify the gaps
Step 5: Take actions
Step 6: Update the source context and loop
```

```
Worked example: churn-forecasting ontological context for two source
systems, as extracted by an AI agent (Step 1)
Source: same article, "Step 1: Build ontological context per source"

# --- Source System 1: Billing System ---
Account -Subscribes to-> Plan
Account -Billed by-> Invoice
Account -Has status-> BillingStatus
Account -Has email-> EmailAddress

# --- Source System 2: Support Ticketing System ---
Customer -Raises-> Ticket
Ticket -Assigned to-> Agent
Ticket -Has status-> TicketStatus
Customer -Has email-> EmailAddress
```

```
Three gaps surfaced by cross-source reconciliation (Step 2), and their
use-case-specific meaning once compared against the churn-forecasting
design context (Step 3-4)
Source: same article

Gap 1: EmailAddress shared by two ontologies
  -> For churn: the join key stitching billing and support histories to
     one customer. "It becomes an identity-resolution requirement."

Gap 2: Account and Customer may be the same real-world entity
  -> For churn: determines both the prediction target and the underlying
     data model. Requires an SME grain decision.

Gap 3: BillingStatus and TicketStatus share the type Status
  -> For churn: "the same type, opposite implications" (closed = healthy
     for a ticket, a churn signal for billing) -- a semantic-collision gap.

Resulting action plan (Step 5):
  Gap 1 -> internal reconciliation: define email as the resolved identity
           key and curate the join. "Fast and internal."
  Gap 2 -> SME decision on customer grain, then a modeling change to the
           curated Customer entity. "Low engineering cost, but it needs
           human judgment before code."
  Gap 3 -> disambiguate the shared type into distinct, context-qualified
           concepts (BillingStatus vs. TicketStatus as separate meanings).
```

## Cross-References

### Cross-reference verification notes
`blog-thoughtworks-asthagiri-ontology-failure-modes.md`,
`blog-thoughtworks-anand-agent-evaluation-framework.md`,
`blog-thoughtworks-gall-supervisory-engineering.md`, and
`blog-thoughtworks-kamelman-unbundling-expertise.md` were re-read in full
before writing the citations above and below; claim numbers cited were
confirmed against each note's numbered `### Claim N:` headings in document
order.

- **Corroborates**:
  - `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 3 (an
    ontology is a blueprint of classes/relationships/rules; a knowledge
    graph is that blueprint populated with real data): this article's
    Claim 1 states the same ontology/knowledge-graph distinction
    independently, five weeks later, from a different Thoughtworks author.
  - `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 4
    (ontology's retrieval benefit requires a populated, entity-resolved
    graph — the schema alone doesn't deliver it) and Claim 5 (a rule only
    binds when a deterministic runtime/process checks it): this article's
    Claim 2 (unverifiable LLM-only schema inference at scale) and Claim 10
    (AI classifies gaps, but governance/human approval is what actually
    binds enterprise-wide model changes) independently restate the same
    two principles — verifiability requires structure beyond raw LLM
    inference, and AI-generated proposals are not themselves the
    enforcement mechanism.
  - `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 8 (the
    ontology practice that survives contact with the real world treats the
    ontology as a product with an owner, not a one-time project) and
    Claim 6 (a shared ontology model goes stale within roughly two quarters
    without a steward and reconciliation cadence): this article's Claim 11
    (context managed as a continuously-updated, version-controlled
    semantic asset at the landscape level, not a static document) is the
    same prescription, with this article additionally supplying the
    specific mechanism (Step 6: each resolved gap becomes the next use
    case's inherited baseline) that operationalizes it.
  - `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 9
    ("curate, don't draft from scratch" — use LLM pipelines to pull draft
    taxonomies from existing schemas, API definitions, and wikis): this
    article's Claim 3 and Claim 5 (an AI agent reads schema, data types,
    foreign keys, sample values, and documentation to infer a candidate
    ontology, flagging low-confidence guesses for SME confirmation)
    describe a concrete, worked instance of exactly this practice, applied
    per-source-system as Step 1 of a repeatable loop rather than as a
    one-time drafting technique.
  - `blog-thoughtworks-anand-agent-evaluation-framework.md` Claim 5 and
    Claim 12 (evaluation strategy evolves from synthetic/dev-stage testing
    to stakeholder-validated business-user testing): the general pattern
    of "AI proposes, a human with domain authority validates before the
    result is trusted" recurs here as this article's Claim 5 (SME
    confirmation of low-confidence ontology guesses) and Claim 10
    (business owners/domain experts approve enterprise-wide model
    changes) — both sources independently place a human-validation gate
    between an AI-generated proposal and any production-affecting decision,
    though applied to different artifacts (evaluation personas vs.
    ontology gaps).

- **Contradicts**: None identified. No existing source note argues that
  ontology-building should be fully automated without human/SME validation,
  that LLM schema inference alone is sufficient for enterprise-scale
  semantic reconciliation, or that gap classification should bypass
  business-owner approval — so there is no direct conflict to file as a
  contradiction issue.

- **Extends**:
  - `blog-thoughtworks-asthagiri-ontology-failure-modes.md`: that article
    diagnoses *why* ontology programs fail (translation gap, scope creep,
    maintenance decay) and prescribes treating the ontology as a product.
    This article supplies a specific, repeatable *procedure* — the
    six-step agentic loop — that operationalizes that prescription: Step 2
    directly addresses the translation-gap failure mode (reconciling
    formal ontology structure against business meaning, with human
    resolution), Step 3's design-context comparison scopes work to one
    funded use case (a structural counter to scope creep), and Step 6's
    continuous update-and-loop is the maintenance mechanism Asthagiri's
    article argues is necessary but does not itself describe procedurally.

- **Novel**:
  - The six-step agentic loop itself (build per-source context, curate/
    reconcile, compare against design context, identify gaps, act, update
    and loop) as a named, repeatable methodology for data-modernization
    discovery is new to this corpus — no prior note describes this specific
    sequence.
  - "Semantic-collision gap" (Claim 8) as a named gap type — a shared type
    name masking opposite business meanings across systems — is a new,
    specific term not present elsewhere in the corpus.
  - The three-way gap taxonomy (identity-resolution requirement / business-
    grain decision / semantic-collision gap), each mapped to a distinct
    action, owner, and cost (Claim 9), is a new, concrete classification
    scheme not present in the more program-level Asthagiri note.
  - The worked billing + support-ticketing ontology example (Concrete
    Artifacts) is a new, specific illustration of enterprise ontology
    reconciliation not present elsewhere in the corpus.

## Guide Impact

- **Chapter 04 (Context Engineering)**: Add the six-step agentic loop
  (Claim 4, Concrete Artifacts) as a named, repeatable procedure for
  semantic-gap discovery, positioned as the operational complement to
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md`'s "treat the
  ontology as a product" prescription. Currently the guide (via the
  Asthagiri note) states *that* ontologies must be continuously maintained
  and scoped to funded use cases, but has no step-by-step procedure for
  *how* a team actually runs a discovery cycle; this article supplies that
  procedure, including where in the loop human/SME judgment is required
  (Steps 2, 4, 5) versus where an AI agent can act with review (Step 1).
- **Chapter 04 (Context Engineering)**: Add the "semantic-collision gap"
  concept (Claim 8) and the three-way gap taxonomy (Claim 9: identity-
  resolution requirement / business-grain decision / semantic-collision
  gap) as a named diagnostic checklist for classifying cross-system
  semantic gaps once they're found — the guide currently has no vocabulary
  for distinguishing these gap types, which this article shows map to
  different owners, costs, and dependency orders.
- **Chapter 04 (Context Engineering)**: Add Claim 11 (context managed as a
  living, version-controlled semantic asset at the landscape level, with
  each resolved gap becoming the next use case's inherited baseline) as a
  concrete mechanism for the "ontology as a product, not a project"
  guidance already recommended from the Asthagiri note — this article is
  the second, independent Thoughtworks source converging on the same
  prescription and adds the specific "update and loop" step that makes it
  procedural rather than aspirational.

## Extraction Notes

- **Raw HTML was fetched directly via `curl` rather than relying solely on
  WebFetch.** An initial WebFetch pass returned a paraphrased, restructured
  summary of the article (headers and framing not matching the source's
  actual section order/wording) rather than verbatim text, consistent with
  prior extractions in this corpus (e.g.
  `blog-thoughtworks-gall-supervisory-engineering.md`,
  `blog-thoughtworks-kamelman-unbundling-expertise.md`). To satisfy the
  verbatim-quote requirement in MINER.md §2a, the live URL was fetched
  directly with `curl`, HTML tags were stripped, and entities were
  unescaped to recover the actual rendered body text, which was then read
  in full. All quotes above were verified against this raw-HTML extraction,
  not against the WebFetch-generated summary.
- **Two visible copy-editing artifacts in the source were preserved
  verbatim rather than silently corrected**: "consisting**comprised**" (Step
  overview paragraph, quoted in Claim 4) and "ontologies **are** tedious to
  build" (quoted in Claim 3) both read as leftover fragments from a sentence
  revision that was not fully cleaned up before publication. A third
  artifact — "Collapsing them into a **flatteninto flatten** concept would
  corrupt the label. This is a semantic-collision gap**:** — the same type,
  opposite implications" (Gap 3 description) — was judged too garbled to
  quote as a single contiguous passage per MINER.md §2a(3); only the clean
  surrounding sentences ("A shared type does not mean shared meaning."/
  "This is a semantic-collision gap") were quoted directly for Claim 8, and
  the garbled middle portion is paraphrased in that claim's summary instead
  of quoted.
- **No sub-pages followed.** The article is short (essay-length,
  self-contained) and does not link out to deeper technical posts or
  external studies the way some other Thoughtworks pieces in this corpus do
  (e.g. `blog-thoughtworks-kamelman-unbundling-expertise.md`'s link to an
  Anthropic study). The "More insights" sidebar links three unrelated
  Thoughtworks articles (a technical-debt piece and two AI-adoption
  pieces) that read as generic related-reading suggestions rather than
  in-article citations the piece builds its argument on, so they were not
  followed as sub-pages per MINER.md §1.
- **No contradiction identified or filed.** Cross-referenced against all
  four overlapping notes named in the two Prospector triage comments
  (Asthagiri, Anand, Gall, Kamelman) plus a corpus-wide review for any note
  arguing against SME-validated, ontology-grounded semantic reconciliation.
  Found strong corroboration (see Cross-References) but no material
  disagreement — see Cross-References → Contradicts above.
- **Confidence rated `emerging` overall**: the six-step methodology and its
  worked example are internally coherent and consistent with prior-mined
  Thoughtworks ontology guidance, but the article names no client
  engagement, provides no before/after metric, and the worked example
  (billing + support churn forecasting) is explicitly constructed for
  illustration ("let's assume") rather than a documented deployment. The
  one `settled`-rated claim (Claim 1) is a definitional statement
  consistent with established semantic-web/data-architecture terminology
  already used elsewhere in this corpus, not an empirical finding specific
  to this article.
