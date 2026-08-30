---
source_url: https://martinfowler.com/articles/making-data-ready-for-agentic-ai.html
source_type: blog-post
title: "Making Your Data Ready for Agentic AI"
author: Pramod Sadalage (Distinguished Engineer, Thoughtworks) and Prem Chandrasekaran (Market Tech Director, Thoughtworks)
date_published: 2026-08-27
date_extracted: 2026-08-30
last_checked: 2026-08-30
status: current
confidence_overall: emerging
issue: "#3020"
---

# Making Your Data Ready for Agentic AI

> A four-layer architecture (data contracts/quality, traceability/governance,
> context layer, agent-ready access) for making enterprise data safe for
> autonomous agents to act on directly, organized around the claim that
> agents lack the implicit judgment humans supply and so every attribute a
> human used to provide for free — trust, context, traceability, governance,
> operability — must be engineered into the data itself.

## Source Context

- **Type**: blog-post (martinfowler.com "articles" section, published 27
  August 2026; martinfowler.com is a `trusted-feed` source in this corpus)
- **Author credibility**: Pramod Sadalage is a Distinguished Engineer at
  Thoughtworks leading Data Engineering and Architecture for North America,
  credited in-article as the developer of evolutionary/version-controlled
  database schema migration techniques in the early 2000s and co-author of
  five books including *Software Architecture: The Hard Parts* and
  *Refactoring Databases*. Prem Chandrasekaran is a Market Tech Director at
  Thoughtworks, described as staying "deliberately hands-on, designing and
  building production-grade systems alongside the teams he leads." Both are
  senior, named, credentialed practitioners at a firm with deep existing
  representation in this corpus's data-architecture sourcing. The article
  discloses AI-assisted drafting ("we used AI assistance to help research,
  organize, and format some parts of our writing") and lists nine named
  reviewers including Martin Fowler and Rebecca Parsons. It cites a mix of
  third-party survey data (Precisely/Drexel LeBow, KPMG), named regulation
  (EU AI Act Articles 12/19), named vendor/OSS tooling (Open Data Contract
  Standard, dbt MetricFlow, Databricks medallion architecture, GraphRAG,
  Graphiti), and the Thoughtworks Technology Radar, but names no specific
  client engagement or measured production outcome for the four-layer
  architecture as a whole — the article is a synthesis/prescriptive
  framework piece, not a case study.
- **Scope**: Covers four topics presented in a deliberate build order — data
  contracts and quality (schema-as-law, the quarantine pattern, medallion
  architecture extended with an "Adaptive Gold" tier, unstructured-data
  freshness, confidence-threshold routing), traceability and governance
  (the "audit gap," agentic lineage as traces/spans, EU AI Act Articles 12
  and 19, a four-stage staged-autonomy ladder, delegated access/JIT
  credentials/least privilege), the context layer (a three-part vocabulary —
  domain model, semantic model, capability model — as distinct from the
  looser "semantic layer" umbrella term, plus knowledge graphs for domain
  traversal), and agent-ready data access (the RAG/MCP-Read/MCP-Write
  spectrum, MCP's three primitives, an anti-pattern against naive
  API-to-MCP conversion, and a capability-declaration schema of
  permissions/owner/preconditions/reversibility). Closes with a
  self-assessment rubric and an explicit claim that the four topics are
  dependency-ordered, not independent workstreams. Does NOT cover: a named
  client's before/after metrics, specific vendor pricing, or model-layer
  prompt-injection defenses (cross-references the "lethal trifecta" concept
  by name but does not re-derive it).

## Extracted Claims

### Claim 1: Five data attributes a human analyst used to supply implicitly — trust, context, traceability, governance, operability — must be built explicitly into the data itself for agents, because an agent has no equivalent of a human's institutional judgment or hesitation
- **Evidence**: The article's central organizing framework, stated as five
  named, paired-with-a-human-behavior attributes (Trusted, Contextual,
  Traceable, Governed, Operational), each explicitly tied to a specific
  piece of human judgment that no longer exists once an agent is the
  consumer.
- **Confidence**: emerging (a specific, well-illustrated framing argument;
  not independently measured, but the article uses it to organize its own
  four-topic structure, and each attribute maps to a concrete architectural
  section later in the piece)
- **Quote**: "A human hesitates at data that looks wrong; an agent acts on it anyway"
- **Quote**: "Trusted: a person pauses at a number that feels wrong; an agent acts on it. The confidence a human used to supply has to be built in, so the data must be accurate, fresh, and validated before the agent ever sees it."
- **Our assessment**: This is the article's thesis and load-bearing framing
  device — the four topics that follow (contracts/quality, governance,
  context, access) are each explicitly mapped back to one or more of these
  five attributes at the section boundaries. It is a more granular,
  five-way decomposition of the general "agents lack human judgment/hesitation"
  observation already present in this corpus (e.g. the pricing-agent example
  in Claim 2 below is this article's own worked illustration of the same
  point). The five-attribute taxonomy itself — Trusted/Contextual/Traceable/
  Governed/Operational as five independently gradable properties — is new
  vocabulary to this corpus and is used later in the article as a literal
  self-assessment rubric (see Concrete Artifacts).

### Claim 2: A stale-price scenario (an agent quoting a customer an outdated price because its data source hadn't refreshed) illustrates that an agent can execute its workflow perfectly while still producing a confidently wrong outcome, because the failure is in the data, not the agent's reasoning
- **Evidence**: A concrete, named worked example, followed by third-party
  survey evidence about the confidence/readiness gap at the organizational
  level.
- **Confidence**: emerging (the worked example is illustrative rather than
  a documented incident; the survey statistics are third-party and cited by
  name)
- **Quote**: "The agent doesn't hesitate, it retrieves $49.99, quotes the customer, the customer buys, and the company loses $10 on every unit sold. Every step the agent took was technically correct. It followed its workflow perfectly. The data it accessed was the problem."
- **Quote** (survey data): "In the 2026 State of Data Integrity and AI Readiness report, Precisely and Drexel University's LeBow College of Business surveyed 505 data and analytics leaders, of whom 87% believed their data was ready for AI, yet 43% named data readiness as the single biggest barrier to getting value from it."
- **Our assessment**: The "every step was technically correct; the data was the problem" framing is a sharp, quotable distinction between agent-behavior failures and data-quality failures — useful for the guide because it argues against reflexively debugging agent logic when the actual defect is upstream. The 87%-vs-43% confidence/readiness gap statistic (Precisely/Drexel, 505 respondents) is a concrete, named survey the guide can cite directly for the "organizations overestimate their AI-readiness" argument; a second cited survey (KPMG Global AI Pulse, 2,145 leaders, "nearly half of executives now seeing AI's costs exceed its benefits") is mentioned in the same paragraph but not quoted verbatim in the article text as read.

### Claim 3: Data contracts, written as schema-as-law (illustrated in the Open Data Contract Standard) rather than a "polite suggestion," must specify schema types, quality rules, and — critically — a freshness SLA keyed to when data was last successfully loaded, not when a value last changed
- **Evidence**: A full YAML data-contract example for a `product_pricing`
  table (schema types, a SQL-based price>0 quality rule, a currency
  ISO-code quality rule, and a `latency: 24h` freshness SLA on
  `ingested_at`), plus explicit reasoning for why the SLA anchor matters.
- **Confidence**: emerging (a specific, concrete technical pattern with a
  worked example; not independently benchmarked, but internally consistent
  and tied to a named standard and CLI tool)
- **Quote**: "Freshness SLAs define the maximum acceptable staleness per dataset, nightly batch updates aren't enough when an agent answers in real time. Key the SLA to when the data was last successfully loaded, not when a value last changed, so that steady data isn't flagged as stale and a stalled pipeline can't masquerade as fresh."
- **Our assessment**: The freshness-SLA-anchor distinction (load-time, not
  change-time) is the article's most concrete and immediately checkable
  technical detail in this section — it is a specific bug class (a stalled
  pipeline silently "passing" a change-time-based freshness check because
  nothing changed) that a team could audit their own contracts against
  today. The full YAML example (Concrete Artifacts) is a directly reusable
  template for the Open Data Contract Standard.

### Claim 4: The quarantine pattern — a contract-validation gate that checks schema, freshness SLA, and quality rules before data reaches an agent-accessible store, routing failures to a dead-letter queue for human review — ensures the agent never sees bad data at all, rather than trying to make the agent robust to it
- **Evidence**: Direct architectural description of the gate, applied back
  to the Claim 2 pricing scenario to show the quarantine mechanism would
  have prevented that specific failure.
- **Confidence**: emerging (a coherent, specific architectural pattern; not
  independently measured, but explicitly demonstrated against the article's
  own worked example)
- **Quote**: "Bad data lands in a dead-letter queue, never in front of the agent"
- **Quote**: "if asked about the price the agent says, "I don't have current pricing data" rather than confidently quoting the wrong number. That is a far better failure mode. And it's a job for the data architecture, not the model. A better model won't rescue you from bad data."
- **Our assessment**: "A better model won't rescue you from bad data" is a
  pointed, quotable rejection of a common failure-response instinct (swap
  in a stronger model) when the actual defect is in the data pipeline. This
  directly corroborates `blog-anthropic-selfservice-data-analytics.md`
  Claim 8's "governance without enforcement decays" framing and Claim 2's
  emphasis on entity/data-layer accuracy over prompt or model quality — both
  sources independently argue that the fix for agent inaccuracy caused by
  bad or ambiguous data lives in the data layer, not the model layer.

### Claim 5: The medallion architecture (Bronze/Silver/Gold) should gain a fourth "Adaptive Gold" tier for agentic use, where agents actively curate optimized datasets from observed query patterns rather than only reading pre-built tiers, and agents should be restricted to Gold and above while Bronze/Silver remain for human lineage and debugging
- **Evidence**: Extension of the standard, Databricks-popularized
  three-tier medallion architecture with a named fourth tier, illustrated
  with a cited real-world precedent (Apple's use of agents as data-catalog
  "digital stewards" at DataHub's CONTEXT 2025 summit) that the article
  explicitly flags as a partial, not exact, precedent for its own proposal.
- **Confidence**: emerging (the three-tier Bronze/Silver/Gold base is
  "well established" per the article's own framing; the fourth
  "Adaptive Gold" tier is the article's own proposed extension, explicitly
  labeled as "an extrapolation, but a modest one from something already
  running")
- **Quote**: "Adaptive Gold where agents become active participants in data curation rather than passive consumers... They monitor their own query patterns, identify frequently accessed combinations, and materialize optimized datasets, effectively building their own warehouse views based on real usage."
- **Quote** (precedent, with explicit caveat): "Apple described agents acting as "digital stewards" of its data catalog, continuously scanning metadata, flagging gaps, and proposing updates... Apple's agents curate the catalog; Adaptive Gold points that same active-curation pattern at the datasets themselves. That last step is an extrapolation, but a modest one from something already running."
- **Quote** (access rule): "The key architectural principle is that agents should only access Gold tier or above. Bronze and Silver exist for lineage, debugging, and human investigation. Exposing raw or partially validated data to agents invites the pricing problem back in."
- **Our assessment**: The article's own hedge on "Adaptive Gold" ("an
  extrapolation, but a modest one") should travel with this claim into the
  guide — the Apple precedent is agents curating a *catalog* (metadata),
  while "Adaptive Gold" proposes agents curating the *datasets* themselves,
  which is a further step the article does not claim is already in
  production anywhere. The "agents see only Gold and above" access rule is
  the more load-bearing, better-supported half of this claim and is a
  direct, checkable architectural rule teams can adopt independent of
  whether they build the Adaptive Gold tier at all.

### Claim 6: The same freshness-SLA logic that governs structured pricing data applies to unstructured/RAG data, but the clock must measure when the vector index was last successfully rebuilt, not when the underlying content last changed — because a silently failed re-indexing job is exactly the case a change-time clock cannot distinguish from "nothing changed"
- **Evidence**: A direct structural parallel drawn between the stale-price
  scenario (Claim 2) and a stale-vector-index scenario, with the same
  load-time-vs-change-time reasoning as Claim 3 applied to embeddings.
- **Confidence**: emerging (a specific, logically argued extension of the
  freshness-SLA pattern to unstructured data; not independently measured
  against a documented RAG staleness incident)
- **Quote**: "A 24-hour SLA means the re-indexing job must have completed within the last 24 hours, if it hasn't, the index is stale and quarantined even when nothing appears to have changed, because a silently failed indexer is exactly when you can't tell whether something did."
- **Quote** (quality gates for text): "reject empty or truncated chunks, catch near-duplicate documents that skew retrieval, flag failed extractions and OCR garbage, and watch for embedding drift... A malformed or empty embedding warps similarity search, so it never reaches the store, for the same reason a bad price never reaches the agent."
- **Our assessment**: This is a specific, transferable technical detail for
  any team running RAG in production: a change-time-based re-indexing
  freshness check has a blind spot exactly when it matters most (a silently
  broken indexer), and the fix is the same load-time-anchoring principle
  already established for structured data contracts (Claim 3). No existing
  corpus note specifies this particular load-time-vs-change-time distinction
  for vector index freshness.

### Claim 7: Confidence-threshold routing bridges full autonomy and full human control by combining model confidence with data-quality signals (freshness, completeness, consistency) into a single threshold decision, but the article explicitly recommends starting with a hard gate (any contract/SLA breach forces human review, regardless of other signals) rather than a smooth composite score, because combining the signals into one score is "an open design problem, not a solved one"
- **Evidence**: Direct architectural description plus an explicit, self-
  flagged epistemic caveat about the state of the art for signal
  combination.
- **Confidence**: emerging (the routing concept itself is clearly stated as
  a design recommendation; the article is explicit that the harder
  sub-problem — weighting composite quality scores — is unsolved)
- **Quote**: "Data quality signals should drive the threshold, not just the model's own confidence. A model can be sure of a stale answer, and the freshness SLA overrides that misplaced certainty."
- **Quote** (caveat): "The hard part is turning those quality signals into a single score and weighing it against the model's own confidence. That's an open design problem, not a solved one. Start with a hard gate rather than a smooth composite. Any contract or SLA breach forces a human, regardless of how the other signals look. Add weighted scoring later, and only once you can show it beats that simple rule."
- **Our assessment**: The explicit "start with a hard gate, not a smooth
  composite, and only add weighting once you can show it beats the simple
  rule" sequencing advice is a specific, actionable anti-over-engineering
  heuristic that should travel with any guide citation of confidence-
  threshold routing — teams should not treat the more sophisticated
  composite-score version as the recommended starting point. This "hard
  gate first" instinct is structurally similar to the "start with a hard
  gate" instinct also present later in the same article's discussion of
  undeclared capability preconditions (an undeclared case escalates to
  human review rather than the agent improvising a workaround), suggesting
  this is a repeated design principle across the article, not a one-off
  recommendation specific to confidence scoring.

### Claim 8: Agentic lineage extends traditional data lineage from "what was accessed" to "why the agent decided to access X because it found Y in source Z," modeled as traces with spans (borrowed from distributed-systems observability), and is what the EU AI Act's Articles 12 and 19 actually require enterprises to produce — not just event logs, but a reconstructable reasoning chain retained for at least six months, with breaches falling in the Act's middle penalty tier (up to €15 million or 3% of global annual turnover)
- **Evidence**: A worked trade-finance example (a $2.4M letter-of-credit
  approval broken into four named spans) plus direct citation of specific
  EU AI Act article numbers, retention duration, and penalty tier.
- **Confidence**: settled for the EU AI Act's specific legal requirements
  (Articles 12 and 19, six-month retention, penalty tier) as verifiable
  regulatory text; emerging for the "agentic lineage"/traces-and-spans
  architectural prescription as the correct implementation of that
  requirement
- **Quote**: "Traditional audit logs can tell you what happened, which tables were queried, at what time, by which service account. What they can't tell you is why. Why did the agent check the sanctions list before the credit terms? Why did it approve despite a minor documentation discrepancy?"
- **Quote** (legal requirement): "Article 12 requires high-risk AI systems to automatically log events over their lifetime so their operation can be traced, and Article 19 requires providers to keep those logs for at least six months. Breaching these record-keeping obligations falls in the Act's middle penalty tier, up to €15 million or 3% of global annual turnover, whichever is higher."
- **Quote** (tooling): "For the agentic equivalent, Langfuse, Arize Phoenix, and OpenTelemetry for AI are the emerging choices. All three feature on the Thoughtworks Technology Radar, OpenTelemetry at Adopt, Langfuse at Trial, and Arize Phoenix at Assess."
- **Our assessment**: This directly extends `blog-anthropic-zero-trust-ai-agents.md`'s
  compliance framing, whose Phase 1 checklist names the EU AI Act as a
  regulatory input without stating specific article numbers, retention
  periods, or the penalty tier — this article supplies exactly that missing
  specificity (Articles 12/19, six months, up to €15M/3% turnover). It also
  extends `blog-thebatch-fde-agents-aiact-issue355.md` Claim 8, which
  documents that the EU AI Act's high-risk-system compliance deadline was
  delayed from August 2026 to December 2027 — that note supplies the "when
  it applies" timeline this article does not mention, while this article
  supplies the "what specifically Articles 12/19 require" detail that note
  does not cover. The named tooling triage (OpenTelemetry Adopt, Langfuse
  Trial, Arize Phoenix Assess per the Thoughtworks Radar) is a concrete,
  checkable practitioner recommendation.

### Claim 9: A four-stage staged-autonomy ladder (Shadow Mode, Supervised, Autonomous with guardrails, Full autonomy) should be earned through evidence — testing the agent before each promotion, not just observing it in production — and building the deterministic, mocked/replayed test harness needed to do that is "a discipline of its own" the article explicitly scopes out
- **Evidence**: A named four-stage table (Agent action / Human role /
  Monitoring per stage) plus an explicit statement of what promotion between
  stages should require.
- **Confidence**: emerging (a specific, named staged-rollout taxonomy;
  consistent with governance patterns already in this corpus but presented
  here as this article's own structured version)
- **Quote**: "Promotion up this ladder should turn on evidence, not a hunch. That means testing an agent before each step, not only watching it in production... So teams mock or replay the tool and model interactions so tests run deterministically in CI. They score the agent's decisions with evals rather than calling live services on every run. Building that harness is a discipline of its own, and beyond the scope of this article."
- **Our assessment**: This four-stage ladder (Shadow → Supervised →
  Autonomous with guardrails → Full autonomy) is structurally similar to,
  but a different granularity than, `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`
  Claim 5's three-tier manual/semi-automated/automated oversight taxonomy —
  both are staged-rollout frameworks for agent autonomy, but this article's
  stages are ordered by deployment maturity over time (a single agent
  graduating through stages), while Kamelman/Gordon's tiers are ordered by
  who enforces each control category (which parts of governance are
  human-authored vs. platform-enforced) at a fixed point in time. The two
  taxonomies answer different questions and are not in conflict; a team
  could apply Kamelman/Gordon's tier split to what controls exist and this
  article's ladder to how a given agent earns fuller access to them over
  time. The "promotion requires evidence, not a hunch" principle, and the
  explicit call-out that building a deterministic eval/replay harness for
  nondeterministic, costly, side-effect-bearing agents is its own discipline,
  is a specific and useful scoping statement — this article treats it as a
  named prerequisite without describing how to build it.

### Claim 10: Three security patterns — delegated access (an agent acts with the invoking user's permissions, not a broad service account), just-in-time credentials (short-lived, task-scoped tokens rather than persistent keys), and least privilege (minimum access for the task) — together break Simon Willison's "lethal trifecta" (private-data access + untrusted-content exposure + external communication) by shrinking what a hijacked agent can reach, and a second, complementary defense (Claim 15 below) keeps retrieved text out of the authorization path entirely
- **Evidence**: Direct description of the three patterns with a concrete
  worked contrast (shared service account vs. delegated access) and named
  attribution of the "lethal trifecta" concept to Simon Willison.
- **Confidence**: settled for the delegated-access/JIT/least-privilege
  patterns themselves (well-established security architecture, consistent
  with corpus corroboration below); emerging for the specific claim that
  these three patterns are sufficient to "break" the lethal trifecta (the
  article itself immediately qualifies this — see Claim 15)
- **Quote**: "When a regulator asks "who accessed this customer's data?", "the service account" tells you almost nothing. With delegated access, the answer is "Alice's agent, acting on Alice's behalf, with Alice's permissions.""
- **Quote** (lethal trifecta): "Simon Willison calls it the lethal trifecta, an agent turns dangerous the moment it holds all three of access to private data, exposure to untrusted content, and a way to communicate externally... Delegated access, just-in-time credentials, and least privilege shrink how much a hijacked agent can reach, breaking the trifecta."
- **Our assessment**: This directly corroborates
  `blog-anthropic-agent-identity-access-model.md` Claim 5 (Claude Tag
  agents act under their own per-system service accounts rather than
  borrowed user credentials — though note the surface difference: this
  article's "delegated access" means the agent inherits the *invoking
  user's* permissions, which is closer to per-user credential delegation
  than Claude Tag's per-*agent* service-account identity; both converge on
  "not a single shared, broadly-privileged service account" as the thing to
  avoid) and `blog-anthropic-zero-trust-ai-agents.md` Claim 12 (short-lived,
  identity-provider-issued tokens as the new baseline; static API keys are
  "no longer a legitimate entry point, not even at Foundation") and Claim
  11's Advanced-tier "Just-In-Time (JIT) / Just-Enough-Administration (JEA)
  with automatic expiration." Three independent Anthropic/Thoughtworks
  sources now converge on delegated, short-lived, minimally-scoped
  credentials as the settled baseline pattern for agent-to-system access.

### Claim 11: The context layer decomposes into three separately governed bodies of definition — a domain model (entities/relationships, consulted but never executed, no query path runs through it), a semantic model (versioned metric/dimension formulas compiled to the same SQL every time, "the semantic layer under a more exact name"), and a capability model (a curated set of read/write operations with permissions, owner, and — for actions — preconditions and a reversibility class) — deliberately separated because the write path (capability model) "carries different risk from the read path and benefits from being governed on its own terms," unlike vendor ontology products (e.g. Palantir's Foundry Ontology) that bundle entities and actions together
- **Evidence**: A direct definitional section distinguishing the three
  models, with an explicit comparison against dbt's `semantic_models`
  terminology and Palantir's Foundry Ontology / Databricks' Genie Ontology
  as named products that bundle these concerns differently.
- **Confidence**: emerging (a specific, named vocabulary and separation
  argument; internally consistent and explicitly justified, but a
  terminology proposal rather than an independently validated taxonomy —
  the article itself states "none of this vocabulary is settled")
- **Quote**: "Nouns, numbers, and verbs. Together they are the context layer, and what unites them is not that they are all about meaning... It is that each one is a place where a guarantee is declared once, in version control, instead of being worked out afresh by the model on every request."
- **Quote** (domain model, consulted-not-executed): "It is consulted, never executed; no query path to data runs through it."
- **Quote** (why capabilities are kept separate from the domain model): "The one real difference between Palantir's shape and ours is that it bundles the actions in. We keep them separate, because the write path carries different risk from the read path and benefits from being governed on its own terms."
- **Our assessment**: This is a more granular three-way split than this
  corpus's existing ontology sourcing provides.
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 2 treats
  "schemas → controlled vocabularies → semantic layers → ontologies →
  knowledge graphs" as a single continuum without separating a distinct
  action/capability layer from the entity/relationship layer,and
  `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md` Claim 2's
  four-part AI-readiness taxonomy (semantic meaning, relationships,
  temporal validity, machine-readable context) likewise does not name a
  distinct "what the agent may do" layer separate from "what exists." This
  article's domain/semantic/capability split, and specifically its
  explicit rationale for keeping the capability (write/action) model
  separate from the domain model (different risk profile, separate
  governance), is a genuinely new structural distinction for the guide's
  context-engineering vocabulary — see also Claim 13 below, which is the
  concrete operationalization of why that separation matters.

### Claim 12: A semantic model constrains an agent to correct, governed SQL instead of guessed table/column names and join paths, and this constraint effect — not raw model capability — is the primary accuracy lever; on AtScale's text-to-SQL benchmark, the same model's accuracy jumped from under 20% on the raw schema to over 92.5% with a semantic layer
- **Evidence**: A worked "same question, very different SQL" before/after
  example (raw-schema guess vs. semantic-layer-constrained query) plus a
  named, cited third-party benchmark figure.
- **Confidence**: settled for the benchmark citation itself (a specific,
  named, third-party-sourced figure); emerging for the general claim that
  this pattern generalizes beyond the cited benchmark
- **Quote**: "The semantic model doesn't make the agent smarter. It stops it from guessing. For an agent that acts on the answer unchecked, that's what matters."
- **Quote** (benchmark): "in AtScale's text-to-SQL benchmark, accuracy jumped from under 20% on the raw schema to over 92.5% with a semantic layer, on the same model."
- **Our assessment**: This is a striking, specific, independently-sourced
  quantification that directly corroborates
  `blog-anthropic-selfservice-data-analytics.md` Claim 6 (Anthropic's own
  internal analytics agent: accuracy without skills stayed at 21%, rising
  to 95%+ with skills) and Claim 2 (the central problem is
  concept-to-entity mapping, not code generation) — two independent
  sources (a third-party benchmark vendor and Anthropic's own production
  team) now converge on a near-identical shape of result: raw-schema/no-
  structured-context accuracy sits roughly in the 20% range, and adding a
  governed semantic layer/skills layer moves it to 92-95%+, on the *same*
  underlying model. This is one of the strongest quantitative convergences
  in this corpus's data/context-engineering sourcing and should be cited as
  a paired data point (AtScale benchmark + Anthropic production metric)
  rather than either figure alone.

### Claim 13: MCP's three primitives sit on an explicit risk gradient — Resources (read-only) are safe, Prompts shape behavior, Tools change state — and this gradient is why the safe rollout path is to expose Resources first and graduate to Tools only under governance; naively wrapping existing REST APIs one-to-one into dozens of MCP tools ("tool sprawl," e.g. 50 near-identical tools) degrades agent tool-selection accuracy sharply, which is why the Thoughtworks Technology Radar placed "naive API-to-MCP conversion" on Hold, and 5-10 well-described business capabilities will outperform 50 thin API wrappers almost every time
- **Evidence**: Direct statement of the MCP primitive risk gradient, a
  named anti-pattern with a specific example tool-naming pattern (
  `get_po_payment_status`, `create_ticket_po_payment`,
  `create_ticket_po_payment_network`), and a named Technology Radar
  placement.
- **Confidence**: emerging (the MCP primitive risk-gradient framing and the
  API-to-MCP anti-pattern are specific, named, and consistent with a
  documented Technology Radar entry, but the "5-10 capabilities beat 50
  wrappers" comparison is not backed by a cited controlled experiment
  within the article)
- **Quote**: "Its primitives sit on a risk gradient, Resources (read-only) are safe, Prompts shape behavior, and Tools change state. That gradient maps straight onto the tiers, Resources to retrieval and Tools to write-back, which is why the safe path is to expose Resources first and graduate to Tools only under governance."
- **Quote** (anti-pattern): "The result is tool sprawl, 50 tools with names like get_po_payment_status, create_ticket_po_payment, create_ticket_po_payment_network. The agent then has to choose among 50 barely-distinguished tools with little context, and LLMs are bad at that; accuracy drops sharply as the tool count climbs. The Thoughtworks Tech Radar put "naive API-to-MCP conversion" on HOLD for exactly this reason."
- **Quote** (principle): "The principle is to design capabilities, not endpoints. Five to ten well described business capabilities will outperform 50 thin API wrappers almost every time."
- **Our assessment**: The MCP-primitive-to-access-tier mapping (Resources↔retrieval,
  Tools↔write-back) is a clean, checkable design rule that gives teams a
  concrete way to audit their own MCP server: any Tool that only reads
  should probably be a Resource, and any capability that writes should be
  deliberately gated. The "design capabilities, not endpoints" principle
  and the named Technology Radar "Hold" placement for naive API-to-MCP
  conversion are new, specific, and citable details not previously present
  in this corpus's MCP-related sourcing (`blog-anthropic-zero-trust-ai-agents.md`
  and `blog-anthropic-agent-identity-access-model.md` cover MCP-adjacent
  identity/credential concerns but not this specific tool-design
  anti-pattern).

### Claim 14: Every capability in the capability model carries permissions and an owner; capabilities that act (as opposed to read) additionally carry preconditions checked against live state at the moment of acting, and a reversibility class (cleanly reversible, reversible at a cost, or irreversible) — and reversibility is a more useful predictor of safe autonomy than transaction size, because a large but reversible action (e.g. a $50,000 internal ledger correction) can be safer to automate than a small but irreversible one (e.g. a $200 external payment)
- **Evidence**: Direct definitional statement of the capability
  declaration's four fields (permissions, owner, preconditions,
  reversibility), with an explicit worked counterexample contrasting
  transaction size against reversibility as the risk-ordering variable.
- **Confidence**: emerging (a specific, well-argued design principle,
  illustrated with a clear counterexample; not independently measured
  against production incident data, and — see Cross-References →
  Contradicts — in tension with a differently-keyed escalation mechanism
  documented elsewhere in this corpus)
- **Quote**: "Reversibility is the class of damage the action can do: cleanly reversible, reversible at a cost through some compensating transaction, or irreversible. This is the more useful predictor of safe autonomy than the money involved. A $50,000 internal ledger correction you can back out is a safer thing to automate than a $200 payment to an external account you cannot claw back."
- **Quote** (guidance): "Where the staged autonomy ladder earlier keys its guardrails to transaction size, prefer keying them to reversibility, and let irreversible actions require human approval whatever stage the agent has reached."
- **Our assessment**: This is one of the article's sharpest, most specific
  design claims, and it is in direct tension with a concrete mechanism
  documented elsewhere in this corpus — see **Cross-References →
  Contradicts** below (filed as contradiction issue #3091). The
  counterexample is well-constructed (a large-but-reversible action vs. a
  small-but-irreversible one), but the article provides no production
  evidence that a reversibility-keyed gate outperforms a dollar-threshold
  gate in practice; both are argued-from-principle design recommendations,
  not measured outcomes.

### Claim 15: A precondition that gates an action must never be read and interpreted from unstructured text at the moment of acting — rules are extracted from source documents ahead of time, curated by a human, and stored as declared preconditions with a provenance link back to the source passage; retrieved text may inform what an agent proposes but never itself authorizes an action, which is a security property (a poisoned document cannot grant a permission the agent did not already have) distinct from and complementary to the delegated-access/JIT/least-privilege defense in Claim 10
- **Evidence**: A direct statement of the informing-vs-gating boundary,
  with an explicit, self-qualified claim about what this defense does and
  does not achieve.
- **Confidence**: emerging (a specific, well-reasoned architectural
  principle with an explicitly stated limitation, not independently
  measured against a documented prompt-injection incident)
- **Quote**: "The boundary is between informing and gating. Retrieved text can shape what the agent suggests and serve as evidence for a human approver, but it never carries the authority to authorise the action itself."
- **Quote** (explicit limitation, self-qualified): "It is not a complete defence, because injected text can still influence what the agent proposes, and a human approver shown fabricated evidence may wave it through. What it removes is the path where the document authorises the action directly, with nobody in between."
- **Quote** (escalation on gap): "Where no declaration covers the situation, the agent does not improvise from its own reading of policy. It escalates. ... An undeclared case degrades the agent to supervised, not to autonomous."
- **Our assessment**: This is a specific, named refinement of prompt-
  injection defense that is distinct from the environmental/credential
  controls documented in `blog-anthropic-zero-trust-ai-agents.md` (Claims
  6-9, 13-14: tool poisoning, indirect injection, Spotlighting,
  constitutional classifiers) — rather than trying to detect or filter a
  malicious instruction in retrieved content, this pattern removes
  retrieved text from the authorization path structurally, so that even a
  successful injection cannot itself grant a permission. The article's own
  explicit caveat (a human approver can still be fooled by fabricated
  evidence) should travel with this claim — it is presented as a
  narrowing of the injection attack surface, not a complete prompt-
  injection defense, and is complementary to rather than a substitute for
  the credential/environmental controls in the zero-trust eBook.

### Claim 16: The four topics (contracts/quality, governance/traceability, context layer, agent-ready access) are dependency-ordered, not independent workstreams — you cannot safely add meaning to data you don't trust, and you cannot safely let agents act without that meaning to constrain them — so a team's overall AI-readiness is capped by its weakest foundational layer, not averaged across layers, while observability/traceability is the exception: it must be instrumented from day one across all layers rather than staged
- **Evidence**: The article's explicit closing synthesis (the "AI-ready
  data stack" section) plus a companion self-assessment rubric scoring
  each of the five attributes from Claim 1 across three maturity states
  (Human-era / In Transition / Agent-ready).
- **Confidence**: emerging (a structural argument about how to sequence
  investment; internally consistent with the rest of the article's content
  but not independently validated against a documented case where skipping
  the ordering caused a specific failure)
- **Quote**: "Don't average the rows, because the stack is dependency ordered, your readiness is capped by your weakest foundational layer, a flawless context layer sitting on untrusted data is still not agent ready. Find your weakest row, and that's where the next investment goes."
- **Quote** (observability exception): "Observability is not staged at all. It goes in from day one, at full strength, whatever the autonomy level, because retrofitting it onto a running system is painful."
- **Our assessment**: The "capped by weakest layer, not averaged" framing is
  a specific, actionable prioritization heuristic distinct from a generic
  "do all four things" recommendation — it gives teams a concrete diagnostic
  question ("which of the five attributes is weakest?") rather than an
  unordered checklist. This is consistent with, and adds an explicit
  sequencing argument to, this corpus's existing "data/context
  infrastructure is a prerequisite, not an optional layer" sourcing (e.g.
  `blog-anthropic-selfservice-data-analytics.md` Claim 8's "data foundations
  first" framing), while adding the specific claim that observability is
  the one layer exempt from staged/sequential rollout.

## Concrete Artifacts

### Open Data Contract Standard example (verbatim YAML, abridged for length)
```
Source: martinfowler.com/articles/making-data-ready-for-agentic-ai.html,
        "Schema is law: data contracts as code"

apiVersion: v3.1.0
kind: DataContract
id: product-pricing
name: Product Pricing
version: 1.0.0
status: active
schema:
- name: product_pricing
  physicalType: table
  properties:
  - name: product_id
    logicalType: string
    physicalType: varchar(64)
    required: true
    unique: true
    primaryKey: true
    primaryKeyPosition: 1
  - name: price
    logicalType: number
    physicalType: decimal
    required: true
    quality:
    - type: sql
      description: Every price must be greater than zero
      query: SELECT min({property}) FROM {object}
      mustBeGreaterThan: 0
  - name: currency
    logicalType: string
    physicalType: varchar(3)
    required: true
    quality:
    - type: sql
      description: Currency must be a supported ISO code
      query: SELECT count(*) FROM {object} WHERE {property} NOT IN ('USD', 'EUR', 'GBP')
      mustBe: 0
  - name: ingested_at
    logicalType: timestamp
    physicalType: timestamp
    required: true
slaProperties:
# the rule that would have caught the stale-price scenario
- property: latency
  value: 24
  unit: h
  element: product_pricing.ingested_at
```

### Medallion architecture for agents (four tiers)
```
Source: martinfowler.com/articles/making-data-ready-for-agentic-ai.html,
        "Medallion architecture for agents"

Bronze:        raw, immutable ingestion; kept for audit trail and lineage
Silver:        validated and deduplicated; schema/contracts enforced here;
               this is where the quarantine pattern lives
Gold:          certified; semantic model compiles against this; access is
               governed; metrics are trusted
Adaptive Gold: agents monitor their own query patterns, materialize
               optimized datasets from real usage (proposed extension,
               explicitly flagged as "an extrapolation, but a modest one")

RULE: agents access Gold and above only. Bronze/Silver are for human
lineage, debugging, and investigation.
```

### Staged autonomy ladder (four stages, table structure preserved)
```
Source: martinfowler.com/articles/making-data-ready-for-agentic-ai.html,
        "Staged autonomy"

Stage                     | Agent                          | Human                                    | Monitoring
---------------------------|--------------------------------|-------------------------------------------|---------------------------------------------
Shadow Mode                | Recommends actions              | Reviews recommendation and executes if appropriate | All recommendations logged to track accuracy over time
Supervised                 | Prepares action, waits for approval | Reviews action and approves or denies  | All proposed actions and human decisions logged
Autonomous with guardrails | Acts within defined boundaries (best drawn by reversibility, not transaction size) | Defines guardrails | All actions logged, alerts fired on exceptions
Full autonomy              | Carries out all actions         | Spot checks                              | Continuous, by other agents and humans
```

### Capability declaration fields
```
Source: martinfowler.com/articles/making-data-ready-for-agentic-ai.html,
        "What a capability declares"

Every capability declares:
  - permissions: who may invoke it, and acting as whom
  - owner: the person accountable when it misbehaves
Acting capabilities additionally declare:
  - preconditions: checked against live state at the moment of acting
    (e.g. a refund needs an original payment, not yet refunded, within
    the amount the invoking user may authorise)
  - reversibility: cleanly reversible / reversible at a cost (compensating
    transaction) / irreversible — the preferred variable for gating
    autonomy, not transaction size
```

### Self-assessment rubric ("Where do you stand?")
```
Source: martinfowler.com/articles/making-data-ready-for-agentic-ai.html,
        "Where do you stand?"

Attribute    | Human-era                                    | In Transition                                          | Agent-ready
-------------|-----------------------------------------------|----------------------------------------------------------|------------------------------------------------------------
Trusted      | Loose schemas, no freshness SLAs; quality rests on an analyst noticing when a number looks off | Contracts on a few critical datasets; quality checked but not enforced in CI/CD | Contracts enforced as code, freshness SLAs per consumer, quarantine before agent storage, agents read Gold only
Contextual   | Metric definitions live in BI tools, SQL, and people's heads | Some metrics defined as code, but definitions still conflict and agents may still hit the raw schema | Context layer in Git: domain model, one semantic definition per metric, curated capabilities; agents route through it, never the raw schema
Traceable    | Logs show what a person queried and when; the why lives in the analyst's head | Traces on some agent workflows; reasoning captured inconsistently | Every agent workflow emits traces with spans, reasoning, and sources; any decision's "why" is reconstructable
Governed     | People access data through their own roles; systems share broad service accounts | Agents run on scoped but long-lived, coarse credentials | Delegated per-user access, just-in-time credentials, least privilege; lethal-trifecta paths closed
Operational  | No agent acts on the data; people read dashboards and act by hand | Agents retrieve via RAG; real-time reads emerging; write-back experimental or ungoverned | All three tiers via well-designed capabilities; write-back gated by staged autonomy and instrumentation

RULE: don't average the rows — readiness is capped by the weakest row.
```

## Cross-References

### Cross-reference verification notes
`blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md`,
`blog-thoughtworks-asthagiri-ontology-failure-modes.md`,
`blog-thoughtworks-gall-layered-context-enterprise-data.md`,
`blog-anthropic-selfservice-data-analytics.md`,
`blog-anthropic-zero-trust-ai-agents.md`,
`blog-anthropic-agent-identity-access-model.md`,
`blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`, and
`blog-thebatch-fde-agents-aiact-issue355.md` were re-read in full before
writing the citations below; claim numbers cited were confirmed against
each note's numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-anthropic-selfservice-data-analytics.md` Claim 6 (21%→95%+
    accuracy gap from adding a skills layer) and Claim 2 (concept-to-entity
    mapping, not code generation, is the central accuracy problem): this
    article's Claim 12 (AtScale benchmark: under 20%→over 92.5% accuracy
    from adding a semantic layer, same model) is an independent, third-
    party-benchmarked convergence on the same shape of result from a
    different organization and a different measurement source. Also
    corroborates that note's Claim 8 ("governance without enforcement
    decays"/data foundations as the top accuracy lever) via this article's
    Claim 4 ("a better model won't rescue you from bad data").
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 12 (short-lived,
    identity-provider-issued tokens are the new baseline; static API keys
    "no longer a legitimate entry point") and Claim 11's Advanced-tier JIT/
    JEA credentials: this article's Claim 10 (just-in-time credentials,
    least privilege, delegated access) restates the same baseline pattern
    in a data-access-specific framing, and explicitly ties it to Simon
    Willison's "lethal trifecta," a concept named but not itself sourced in
    the zero-trust eBook note.
  - `blog-anthropic-agent-identity-access-model.md` Claim 5 (Claude Tag
    agents act under distinct per-system service accounts, not a shared or
    borrowed user identity): corroborates the general "don't use one broad
    shared service account" principle in this article's Claim 10, though
    the specific mechanism differs — see Cross-References note above (this
    article's "delegated access" inherits the *invoking user's*
    permissions; Claude Tag's agent identity is a distinct *agent-level*
    service account rather than a proxy for any user). Both reject shared,
    over-broad service accounts as the thing to avoid; they differ on
    whether the replacement identity should be user-delegated or agent-
    native.
  - `blog-thebatch-fde-agents-aiact-issue355.md` Claim 8 (EU AI Act
    high-risk-system compliance deadline delayed from August 2026 to
    December 2027, with SME carve-outs): this article's Claim 8 names the
    specific *content* of Articles 12 and 19 (automatic lifecycle logging,
    six-month minimum retention, penalty tier up to €15M/3% turnover)
    without stating the current deadline; that note supplies the "when"
    this article's "what" is missing. Together they give a fuller EU AI Act
    compliance picture than either alone.
  - `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 5
    (three-tier manual/semi-automated/automated oversight, organized by who
    enforces each control) and Claim 1 (the Andon Labs case study's
    governance gap: "no governance document, no designated principal, no
    clear liability chain"): this article's Claim 9 (four-stage
    maturity-over-time autonomy ladder: Shadow→Supervised→Autonomous with
    guardrails→Full autonomy) is a complementary, differently-organized
    staged-rollout taxonomy for the same underlying problem (how much
    should an agent be trusted, and how is that trust earned/enforced) —
    see Extends below for the specific relationship, and see Contradicts
    below for one point of direct tension between the two articles'
    escalation-threshold mechanisms.

- **Contradicts** (filed as
  [issue #3091](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/3091)):
  - `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 5
    (Tier 2, dynamic escalation keyed to transaction dollar amount — e.g.
    "an agent authorized to negotiate purchases up to $10,000" has any
    negotiation above that limit auto-paused for human sign-off): this
    article's Claim 14 explicitly argues the opposite design variable —
    "Reversibility... is the more useful predictor of safe autonomy than
    the money involved," illustrated with a counterexample ("A $50,000
    internal ledger correction you can back out is a safer thing to
    automate than a $200 payment to an external account you cannot claw
    back") that is precisely the shape of case a fixed-dollar threshold
    handles incorrectly (it would auto-approve the small irreversible
    payment and auto-escalate the larger reversible correction). Both
    articles present their mechanism as a general design recommendation for
    agent escalation gating, not a narrow special case, so they cannot both
    be adopted as-stated for the same design decision. No verdict is
    asserted in this note — see issue #3091 and the eventual
    CONTRADICTIONS.md entry for resolution.

- **Extends**:
  - `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 2 (the
    schemas→controlled vocabularies→semantic layers→ontologies→knowledge
    graphs continuum) and `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md`
    Claim 2 (four-part AI-readiness taxonomy: semantic meaning,
    relationships, temporal validity, machine-readable context): this
    article's Claim 11 (domain model / semantic model / capability model as
    three separately-governed bodies of definition, with an explicit
    rationale for keeping the write/action layer separate from the
    entity/relationship layer) adds a structural distinction — a named,
    separately-governed "capability model" for what an agent may *do* —
    that neither prior source names as distinct from what an agent may
    *know*.
  - `blog-anthropic-zero-trust-ai-agents.md` (Claims 6-9, 13-14: tool
    poisoning, indirect prompt injection, Spotlighting, constitutional
    classifiers as detection/filtering defenses against malicious retrieved
    content): this article's Claim 15 (retrieved text may inform but never
    gate an action; preconditions are pre-extracted and human-curated, not
    read live from policy documents) adds a structural defense that removes
    retrieved text from the authorization path entirely, rather than
    trying to detect or filter malicious content within it — a
    complementary layer to, not a replacement for, the zero-trust eBook's
    detection-based controls.
  - `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 5:
    this article's four-stage staged-autonomy ladder (Claim 9) supplies a
    concrete, ordered maturity progression (with specific human/monitoring
    roles at each stage) that Kamelman/Gordon's three-tier framework does
    not itself sequence over time — that framework specifies which
    controls exist at a governance level; this article's ladder specifies
    how an individual agent earns fuller access to autonomy over time.

- **Novel**:
  - **The five-attribute readiness taxonomy** (Trusted/Contextual/
    Traceable/Governed/Operational, Claim 1), used as both an organizing
    framework and a literal self-assessment rubric (Concrete Artifacts) —
    not present as a five-way, independently-gradable decomposition
    elsewhere in this corpus's data-readiness sourcing.
  - **Load-time-vs-change-time freshness SLA anchoring** for both
    structured data (Claim 3) and vector indexes (Claim 6) — a specific,
    checkable technical distinction (a stalled pipeline vs. genuinely
    unchanged content) not previously documented in this corpus.
  - **The domain model / semantic model / capability model three-way split**
    (Claim 11), with an explicit rationale for separating the capability
    (action) layer from the domain (entity) layer by risk profile — new,
    named vocabulary for this corpus's context-engineering sourcing.
  - **The informing-vs-gating boundary for retrieved text** (Claim 15) as a
    structural (not detection-based) prompt-injection mitigation — genuinely
    new to this corpus's security sourcing, which has otherwise focused on
    detection/filtering (Spotlighting, constitutional classifiers) and
    credential/environmental controls.
  - **The AtScale text-to-SQL benchmark figure** (under 20%→over 92.5%,
    Claim 12) — a new, named, third-party quantitative data point that
    happens to closely parallel Anthropic's own internal metric in
    `blog-anthropic-selfservice-data-analytics.md`.
  - **"Capped by weakest layer, not averaged" as an explicit AI-readiness
    prioritization rule** (Claim 16) — a specific sequencing heuristic not
    previously stated this explicitly in this corpus's data-infrastructure
    sourcing.
  - **Reversibility class over transaction size as the preferred autonomy-
    gating variable** (Claim 14) — new to this corpus, and in direct
    tension with an existing source's dollar-threshold mechanism (see
    Contradicts).

## Guide Impact

- **Chapter on Data & Infrastructure**: Add the five-attribute readiness
  taxonomy (Claim 1) and the "capped by weakest layer, not averaged"
  prioritization rule (Claim 16) as the organizing framework for any
  section on preparing data for agentic consumption. Add the load-time-
  vs-change-time freshness SLA distinction (Claims 3, 6) as a specific,
  checkable audit item for both structured data contracts and RAG
  vector-index pipelines. Add the domain/semantic/capability model
  three-way split (Claim 11) alongside the existing Asthagiri/Xiong
  ontology-continuum sourcing as a more granular vocabulary, specifically
  flagging the capability model as a distinct, separately-governed layer
  for "what the agent may do" rather than folding actions into the entity
  model.

- **Chapter on Context Engineering**: Add the AtScale benchmark figure
  (Claim 12) paired directly with `blog-anthropic-selfservice-data-analytics.md`
  Claim 6's 21%→95%+ metric as two independent, convergent data points for
  "a governed semantic/skills layer, not a bigger model, is the primary
  accuracy lever." Add the MCP primitive risk-gradient mapping and the
  "design capabilities, not endpoints" anti-sprawl principle (Claim 13) as
  concrete MCP server design guidance, citing the named Thoughtworks
  Technology Radar "Hold" placement for naive API-to-MCP conversion.

- **Chapter on Security / Threat Model**: Add the informing-vs-gating
  boundary for retrieved text (Claim 15) as a structural complement to the
  zero-trust eBook's detection-based prompt-injection defenses — explicitly
  note the article's own caveat that this narrows, but does not eliminate,
  the injection attack surface (a human approver can still be shown
  fabricated evidence). Add delegated access / JIT credentials / least
  privilege (Claim 10) as a third independent corroboration of the
  short-lived-credential baseline already sourced from the zero-trust
  eBook and the Claude Tag agent-identity announcement, explicitly naming
  Simon Willison's "lethal trifecta" as the threat model these three
  patterns jointly narrow.

- **Chapter on Team Adoption / Governance**: Add the four-stage staged-
  autonomy ladder (Claim 9) as a maturity-over-time complement to
  Kamelman/Gordon's three-tier oversight framework, explicitly noting the
  two taxonomies answer different questions (which controls exist vs. how
  an agent earns fuller access over time) and are not in conflict. Flag the
  reversibility-vs-transaction-size contradiction (Claim 14, issue #3091)
  prominently in any section recommending a specific escalation-threshold
  design — do not present either the dollar-threshold or the reversibility-
  class approach as settled guidance until the contradiction is resolved.

- **Chapter on Compliance**: Add the specific EU AI Act Article 12/19
  content (automatic lifecycle logging, six-month minimum retention,
  penalty tier up to €15M/3% turnover, Claim 8) paired with
  `blog-thebatch-fde-agents-aiact-issue355.md` Claim 8's compliance-deadline
  timeline (December 2027 for high-risk systems) as a combined "what is
  required, and by when" compliance reference.

## Extraction Notes

1. **Full verbatim article text was obtained directly via HTML fetch, not
   WebFetch summarization.** The article was downloaded with `curl` using a
   standard browser user agent (HTTP 200) and converted to plain text by
   stripping HTML tags; the full ~7,000-word article, including both
   author bios, all figure captions, the acknowledgments section, and the
   "Significant Revisions" footer, was read in its entirety in this form.
   All quotes in this note are copied character-for-character from that
   locally-rendered text. The Assayer should still spot-check quotes
   against the live URL per standard practice.
2. **Five embedded figures** (medallion tiers, the context-layer diagram,
   the semantic-model query flow, the PO-payment end-to-end flow, and the
   AI-ready data stack) could not be extracted as image content — only
   their captions and the surrounding prose describing each are reflected
   above. No figure's visual layout (boxes/arrows) is claimed as directly
   observed; only caption text, which was present as plain text in the
   fetched HTML, is quoted.
3. **No sub-pages were followed.** The article links to numerous named
   external resources (Open Data Contract Standard docs, Data Contract CLI,
   DataHub's CONTEXT 2025 summit coverage, the Precisely/Drexel and KPMG
   survey reports, GraphRAG, Graphiti, the Microsoft Cloud Adoption
   Framework for AI, and the authors' forthcoming O'Reilly book) but none
   were fetched as separate sources — per MINER.md §1's "up to 5 linked
   pages that seem substantive" guidance, the article's own prose was
   judged to state each cited claim's substance directly (e.g. the
   87%/43% survey split, the AtScale benchmark figure), so following the
   underlying reports was not necessary to extract the claims as the
   article presents them. A future Prospector pass could independently
   evaluate the Precisely/Drexel "State of Data Integrity and AI Readiness"
   report or the AtScale benchmark writeup as primary sources in their own
   right.
4. **One contradiction identified and filed before this note was written**,
   per MINER.md §4a: this article's Claim 14 (reversibility over
   transaction size for autonomy gating) directly opposes
   `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 5's
   dollar-threshold dynamic-escalation mechanism. Filed as
   [issue #3091](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/3091).
   No verdict is asserted in this source note.
5. **A second, pre-existing contradiction (issue #2458)** — between
   `blog-thoughtworks-gall-layered-context-enterprise-data.md` (a curated,
   human-confirmed semantic layer/ontology is "ultimately illusory"; prefer
   federated, passively-harvested sub-graphs) and the Asthagiri/Xiong
   "treat the ontology as a product" sourcing — was checked against this
   article's own position. This article's context-layer prescription
   (Claim 11: domain/semantic/capability models, versioned in source
   control, human-reviewed, tested in CI) sits on the Asthagiri/Xiong side
   of that existing debate; it also explicitly states "chasing one
   canonical model is usually a mirage; each domain has its own, governed
   the federated way Data Mesh describes" (context-layer section), which
   partially echoes Gall's federated-domain-ownership argument (his Claim
   5) without adopting his passive-harvesting mechanism or his "any
   human-confirmed mapping is dead on arrival" claim (his Claim 6). This
   article is therefore added as a third, mixed data point on the existing
   #2458 debate rather than filed as a new contradiction — it does not
   take a position clean enough to be "Side A" or "Side B" of that specific
   disagreement, since it agrees with Gall on federation-by-domain while
   disagreeing with him on whether human-curated, code-reviewed context
   layers are viable at all.
6. **Confidence rated `emerging` overall.** The article is a synthesis/
   prescriptive framework from two senior, named, credentialed Thoughtworks
   practitioners, citing specific named third-party data (surveys, a
   benchmark figure, EU AI Act article numbers) for several individual
   claims (rated `settled` where the citation is independently verifiable,
   e.g. the EU AI Act's Articles 12/19 content and the AtScale benchmark
   figure) alongside several proposed architectural extensions the article
   itself flags as unvalidated (e.g. "Adaptive Gold" as "an extrapolation,"
   confidence-threshold-signal weighting as "an open design problem, not a
   solved one"). No client engagement or before/after production outcome
   is named for the four-layer architecture as a whole, which keeps the
   overall rating below `settled`.
