---
source_url: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
source_type: blog-post
title: "How Anthropic enables self-service data analytics with Claude"
author: Chen Chang, Clement Peng, Justin Leder, Johanne Jiao, and Josh Cherry (Data Science and Data Engineering team, Anthropic)
date_published: 2026-06-03
date_extracted: 2026-06-04
last_checked: 2026-06-04
status: current
confidence_overall: emerging
issue: "#1054"
---

# How Anthropic enables self-service data analytics with Claude

> Anthropic's internal experience report on building production analytics agents: five
> named co-authors from the Data Science and Data Engineering team document how they
> reached 95% automation at ~95% accuracy using a four-layer "agentic data stack," with
> the decisive finding that procedural skills (not SQL query retrieval) are the lever
> that moves accuracy from 21% to 95%+.

## Source Context

- **Type**: blog-post (claude.com/blog, June 3, 2026; co-authored by five named Anthropic
  employees on the Data Science and Data Engineering team)
- **Author credibility**: Five named practitioners on Anthropic's internal data science
  team writing about their own production system. The article describes first-party
  experience with concrete accuracy metrics, explicit failure mode taxonomies, and an
  appendix providing a reusable skill file skeleton template. No promotional gloss —
  the authors include tradeoffs (adversarial review costs 32% more tokens and 72%
  higher latency for 6% accuracy gain). Anthropic is the model vendor, so there is
  an implicit promotional incentive, but the candid tradeoff disclosure reduces the
  marketing-copy risk. The five-author byline is notable: this is a team product, not
  a thought-piece.
- **Scope**: Covers Anthropic's internal analytics agent architecture — from data
  foundations through sources of truth, skills, and validation — using Claude as the
  backbone. Includes specific accuracy measurements (21% baseline, 95%+ with skills),
  failure mode taxonomy, two skill type definitions (knowledge and unbook), two
  offline eval types, a correction harvesting pattern, and a getting-started
  recommendation. Does NOT cover: API details, cost/pricing, specific tooling beyond
  the described stack, integration with external BI tools, or the full contents of
  the skill file skeleton (structure only in appendix).

## Extracted Claims

### Claim 1: Self-service business analytics with LLMs is tractable — Anthropic automated 95% of internal analytics queries at ~95% aggregate accuracy

- **Evidence**: Concrete production metrics from Anthropic's internal analytics system,
  reported by five co-authors on the team that built it.
- **Confidence**: emerging (self-reported by the team that built the system; specific
  enough to be credible; no independent audit or methodology details)
- **Quote**: "At Anthropic, 95% of business analytics queries are automated via Claude,
  with ~95% accuracy in aggregate."
- **Our assessment**: This is the headline claim establishing that analytics agents at
  production accuracy thresholds are achievable today, not a future aspiration. The
  ~95% accuracy qualifier ("in aggregate") is important — certain domains reach ~99%,
  implying others pull the average down. The 95% automation rate (not all queries are
  automated — 5% still require manual handling) is also notable: some queries are
  presumably out of scope or too complex. For the guide: this is the first in-corpus
  production-scale analytics agent accuracy metric.

### Claim 2: The central problem is concept-to-entity mapping, not code generation — mapping a user's question to correct, up-to-date data model entities is what determines accuracy

- **Evidence**: Explicit author thesis, stated as the architectural organizing principle
  of the entire article.
- **Confidence**: emerging (author framing; consistent with the three failure modes all
  mapping to entity/knowledge retrieval failures rather than query-writing failures)
- **Quote**: "The central problem comes down to our ability to map a user's question to
  specific and up-to-date entities in our data model and know the correct way of working
  with them."
- **Our assessment**: This reframes the analytics agent problem from "can the model write
  SQL?" (largely solved) to "can the model identify the right table, column, and metric
  definition?" (the hard part). The implication is that engineering effort should
  concentrate on the entity resolution layer — data governance, canonical datasets,
  skills that encode which entities to use — rather than on prompt engineering for
  SQL quality. This is consistent with `blog-anthropic-carta-healthcare-context-engineering.md`
  Claim 1 (context construction is the primary accuracy lever, not prompt wording).

### Claim 3: Traditional self-service analytics approaches fail in two symmetric ways — denormalized tables create inconsistency, ringfenced environments miss the long tail

- **Evidence**: Opening problem framing with two named anti-patterns.
- **Confidence**: anecdotal (author characterization of industry-wide failure modes;
  consistent with common data engineering experience)
- **Quote**: "Making the data model more accessible to less technical coworkers via wide
  and denormalized tables often leads to overlapping views with inconsistent definitions
  as the business scales."
- **Quote**: "creating more ringfenced environments for users often misses the long tail
  of business questions and leads to metric and dashboard bloat as teams silo their work."
- **Our assessment**: The "slog" framing ("enabling self-service business analytics has
  traditionally been a slog") and the two anti-patterns provide the problem context
  that motivates the agentic approach. Wide denormalized tables optimize for query
  accessibility but degrade consistency; ringfenced curated environments optimize for
  consistency but leave most questions unanswered. Analytics agents solve both by
  providing a single governed data model (consistency) that agents can navigate
  flexibly (coverage). This positions agent analytics not as a replacement for BI
  tools but as an answer to the coverage/consistency tradeoff that BI tools cannot
  resolve.

### Claim 4: Three failure modes account for analytics agent inaccuracies — concept-entity ambiguity, data staleness, and retrieval failure

- **Evidence**: Explicit failure mode taxonomy from the authors, presented as the
  architectural problem statement for the four-layer stack.
- **Confidence**: emerging (first-party taxonomy from practitioners; reasonable and
  specific; covers the full problem space)
- **Quote** (ambiguity): "with hundreds of viable options in a data model (out of
  potentially millions of fields), the agent is unable to choose the correct fields"
- **Quote** (staleness): "data sources, business definitions, and schemas change
  constantly; assets and agent knowledge go stale"
- **Quote** (retrieval): "the right information may actually be in the data model and
  properly annotated, but given the vastness of the search space, the agent simply
  doesn't find it"
- **Our assessment**: The three failure modes are distinct enough to motivate separate
  architectural interventions: ambiguity → canonical datasets and governed semantic
  layer; staleness → correction harvesting and PR-based update cycle; retrieval →
  structured skills and knowledge routing (not raw retrieval). This taxonomy is the
  most specific failure-mode analysis of analytics agents in the corpus. It is also
  predictive: teams building analytics agents should expect these specific failures,
  and can design against them before deployment.

### Claim 5: LLMs are a double-edged sword for analytics — the generative capacity that enables creative problem-solving also enables hallucination

- **Evidence**: Opening framing of the "Data is not software" section.
- **Confidence**: settled (well-established observation; the authors use it to motivate
  the need for validation-first design in analytics)
- **Quote**: "LLMs' generative abilities are a double-edged sword: the mechanisms that
  enable creative solutions to complex problems can also hallucinate erroneous output."
- **Our assessment**: The "Data is not software" section title captures an important
  architectural constraint: software agents can tolerate creative approximation
  (a slightly wrong code solution can be debugged and iterated), but analytics answers
  that are confidently wrong cause decisions to be made on false data. The correctness
  bar for analytics is deterministic — "the same number every other surface in the
  company produces" — not probabilistic. This motivates the validation-first design
  philosophy that runs through the entire article.

### Claim 6: Skills are the decisive accuracy lever — without skills, accuracy stays at 21%; with skills, accuracy rises above 95% in aggregate and approaches 99% in certain domains

- **Evidence**: Direct ablation data from the team's own evaluation suite.
- **Confidence**: emerging (self-reported ablation result from the team; specific and
  quantified; no methodology details for the eval construction)
- **Quote**: "Without skills, Claude's ability to answer analytics questions accurately
  didn't exceed 21% on our evals."
- **Quote**: "Adding skills gets these numbers consistently above 95% in aggregate and
  regularly around 99% in certain domains."
- **Our assessment**: The 21% → 95%+ gap is the most striking quantitative claim in
  the article. It establishes that raw LLM ability against an unstructured data model
  is far below the threshold required for production use, but that the skills layer
  closes most of that gap. The "in certain domains" qualifier for 99% implies that
  domain coverage in skills correlates with accuracy — well-documented domains with
  mature skills reach near-perfect accuracy. This is a concrete argument for investing
  heavily in skills before deploying analytics agents in production.

### Claim 7: Raw SQL query history barely improves accuracy — giving agents retrieval access to thousands of prior queries moved accuracy by less than a point

- **Evidence**: Direct ablation result from the team's experiments.
- **Confidence**: emerging (self-reported ablation; the specific finding counteracts
  an obvious hypothesis that "more historical examples = better performance")
- **Quote**: "In practice, we found that giving the agent raw retrieval access to
  thousands of prior queries moved accuracy by less than a point."
- **Our assessment**: This is a strongly counterintuitive finding with significant
  architectural implications. The obvious intuition is that showing the agent
  relevant past queries would help it learn the right patterns. The finding says
  structured procedural skills outperform raw retrieval of historical examples
  by a massive margin. The explanation is implicit: raw query history provides
  ambiguous precedents (many queries, some of which may be wrong or outdated),
  whereas skills provide curated, authoritative procedural guidance. This claim
  directly informs architecture choices: invest in skills authoring, not query
  corpus retrieval. For the guide: this is a named anti-pattern — "query retrieval
  augmentation" is the wrong investment for analytics accuracy.

### Claim 8: Data foundations — canonical datasets with enforced governance — are the most important accuracy enabler because they prevent ambiguity before agents query

- **Evidence**: First author claim about the "most important aspect" of accuracy,
  backed by the specific mechanism (reducing candidates from "forty plausible
  candidates" to "one governed dataset").
- **Confidence**: emerging (author characterization of relative importance; consistent
  with the failure mode analysis where concept-entity ambiguity is listed first)
- **Quote**: "The most important aspect of ensuring analytics agents are accurate is via
  strong data foundations, which include the data models, transforms, tests, and tables
  in a data warehouse, along with the metadata describing them."
- **Quote**: "if revenue, for example, resolves to one governed dataset instead of forty
  plausible candidates, the problem largely disappears"
- **Quote**: "Governance without enforcement otherwise quickly decays back to the
  multiple candidates problem."
- **Our assessment**: The "one governed dataset vs. forty plausible candidates" framing
  is the clearest statement of the data foundations value proposition. It is not about
  data quality per se — it is about cardinality reduction: eliminating ambiguity by
  making the mapping between concept and entity injective (one-to-one). The "governance
  without enforcement decays" claim is a strong warning against data governance
  initiatives that define standards without mechanisms to enforce them. For the guide:
  the data foundations layer is a prerequisite, not an optional optimization.

### Claim 9: The single-repo approach — all data code, semantic layer, reference docs, and dashboard definitions in one repo with CI checks — protects cross-layer integrity

- **Evidence**: Direct description of Anthropic's internal data architecture practice.
- **Confidence**: emerging (first-party practice description; specific and actionable;
  single organization evidence)
- **Quote**: "Nearly all data code (i.e., modeling, semantic layer, reference docs,
  canonical dashboard definitions) lives in a single repo, with CI checks that protect
  cross-layer integrity."
- **Our assessment**: Co-location in a single repo with CI checks is the enforcement
  mechanism that makes "governance without enforcement decays" not apply to Anthropic's
  own setup. The CI checks ensure that a change to the data model that would break the
  semantic layer is caught before merge — preventing the staleness failure mode
  proactively. This is a specific architectural practice, not a general principle, and
  teams on fragmented data stacks would need to adapt it.

### Claim 10: The semantic layer is the highest-reliability source of truth — it yields the same single metric value across all company surfaces

- **Evidence**: Description of the semantic layer's function and value proposition.
- **Confidence**: settled (the value proposition of a semantic layer is well-established
  in data engineering; the authors apply it to the agent context)
- **Quote**: "If a question maps cleanly to a defined metric, the agent calls a function
  and gets one number, the same number every other surface in the company produces."
- **Our assessment**: "The same number every other surface in the company produces" is
  the gold standard for analytics accuracy: the agent's answer matches what every other
  report, dashboard, and data product would show. The semantic layer achieves this by
  providing compiled metric and dimension definitions that all surfaces — including the
  agent — call as functions rather than querying raw tables independently. For the guide:
  teams with an existing semantic layer (dbt Metrics, Looker, Cube) should route agent
  queries through it as the first-line reference before falling back to raw table access.

### Claim 11: Two skill types encode different levels of procedural knowledge — knowledge skills route and load domain context on demand; unbook skills encode the full analyst workflow

- **Evidence**: Direct definition of both skill types with behavioral descriptions.
- **Confidence**: emerging (first-party practice description; specific and concrete;
  includes the adversarial review sub-agent pattern)
- **Quote** (knowledge skill): "a knowledge skill acts as a thin top-level router that
  allows additional domain details to load on demand. It says 'try the semantic layer
  first, but if there's no coverage, here are ~30 reference files for this domain.'"
- **Quote** (unbook skill): "The unbook skill encodes the process a senior analyst would
  follow: clarify the question, find sources (via the knowledge skill), run the query,
  and then loop the result through adversarial review sub-agents."
- **Our assessment**: The knowledge/unbook distinction maps to two different levels of
  procedural guidance: the knowledge skill is a routing layer (where to look) and the
  unbook skill is a workflow layer (how to work). The "~30 reference files" detail for
  knowledge skills is a concrete sizing signal: domain coverage is bounded and human-
  curated, not open-ended retrieval. The unbook skill's reference to "adversarial review
  sub-agents" is the clearest production application of the generator-verifier pattern
  in the corpus for a non-coding use case. Compare: `blog-anthropic-harness-long-running.md`
  Claim 2 (separating generation from evaluation is a strong lever) is the architectural
  principle; this skill encodes it as a procedural instruction.

### Claim 12: Adversarial review sub-agents increase accuracy by 6% but cost 32% more tokens and 72% more latency — the tradeoff must be explicit

- **Evidence**: Quantified tradeoff from the team's own eval suite.
- **Confidence**: emerging (self-reported tradeoff; specific; no methodology details)
- **Quote**: "We've found that employing a Claude skill to aggressively challenge all
  underlying assumptions on a potential final answer increased accuracy by 6% within
  our eval set, but at the cost of 32% more tokens and 72% higher latency."
- **Our assessment**: This is the most candid disclosure in the article. The adversarial
  review pattern is not free — it roughly doubles latency and adds a third more cost
  for a 6% accuracy improvement. Whether the tradeoff is worthwhile depends on the
  stakes of a wrong answer. For analytics queries that drive financial decisions,
  +6% accuracy may be worth it; for exploratory queries, it may not. For the guide:
  document the adversarial review pattern as a configurable option with explicit
  tradeoffs, not a universal recommendation. This corroborates `blog-anthropic-harness-long-running.md`
  Claim 11 which also discusses the cost-benefit of the evaluator component.

### Claim 13: Two offline eval types cover different coverage surfaces — dashboard-based evals for common questions, long-tail evals for broad domain coverage

- **Evidence**: Direct description of the two offline eval types used at Anthropic.
- **Confidence**: emerging (first-party practice description; specific and replicable)
- **Quote**: "Dashboard-based evals are auto-generated by Claude (then human validated),
  covering the most common stakeholder questions. Long tail evals are where we feed
  Claude business context (roadmaps, table docs) and have it generate plausible
  questions across the rest of the domain."
- **Our assessment**: The two-type eval design is elegant: use the most common real
  queries to anchor accuracy on the 80% case (dashboard-based), then use AI-generated
  plausible questions to cover the long tail. The "auto-generated by Claude (then human
  validated)" workflow for dashboard evals is a practical implementation pattern —
  the human validation step preserves eval quality while AI generation scales coverage.
  For the guide: this two-type eval framework should be presented as the minimum viable
  eval suite for analytics agents. The "every meaningful skill edit gets a before/after
  run on the relevant eval slice" norm (ablation testing) makes evals the gate for
  skill changes, not a periodic audit.

### Claim 14: Automated correction harvesting — a scheduled agent that scans stakeholder channels for corrections, drafts reference doc fixes, and opens PRs — closes the staleness failure mode

- **Evidence**: Specific description of a production pattern used at Anthropic.
- **Confidence**: emerging (first-party practice description; specific and replicable;
  no volume metrics reported)
- **Quote**: "A scheduled agent scans stakeholder channels every few hours for similar
  correction language, drafts a one-line fix to the relevant reference doc, and opens
  a PR tagged to the domain owner."
- **Our assessment**: This is the most novel pattern in the article from a systems
  architecture standpoint. Rather than waiting for human operators to notice and fix
  stale reference docs, the system monitors for correction signal from actual users,
  automatically proposes fixes, and routes them to the right owner. The PR-tagging-
  to-domain-owner workflow preserves human oversight while automating the detection
  and drafting steps. This is a production implementation of the "feedback loop for
  continuous improvement" pattern that other corpus sources recommend conceptually
  but rarely describe mechanically.

### Claim 15: Getting started is feasible with minimal initial investment — a handful of canonical datasets, a few dozen offline evals, and a thin knowledge skill capture most of the upside

- **Evidence**: Explicit author recommendation in the "Getting started" section.
- **Confidence**: anecdotal (author's practical recommendation; consistent with the
  accuracy claims that skills are the decisive lever)
- **Quote**: "If you're starting from zero, a handful of canonical datasets, a few dozen
  offline evals, and a thin knowledge skill will capture most of the upside."
- **Our assessment**: The "handful / few dozen / thin" sizing is the most actionable
  guidance in the article for teams evaluating whether to invest. The implication is
  that the 21% → 95%+ improvement is achievable without building a comprehensive
  enterprise data catalog first — a focused, well-governed subset with matching skills
  is sufficient to prove value. This is consistent with the "data foundations first"
  principle: get one domain right before scaling to many.

## Concrete Artifacts

### Four-Layer Agentic Analytics Stack (from article)

```
"Our agentic analytics stack"
Source: "How Anthropic enables self-service data analytics with Claude"
Authors: Chen Chang, Clement Peng, Justin Leder, Johanne Jiao, Josh Cherry
Anthropic Data Science and Data Engineering team, June 2026

LAYER 1: DATA FOUNDATIONS
  Definition: "the data models, transforms, tests, and tables in a data warehouse,
               along with the metadata describing them"
  Key practice: Canonical datasets with enforced governance; single repo;
                CI checks protecting cross-layer integrity
  Why: "if revenue, for example, resolves to one governed dataset instead of
        forty plausible candidates, the problem largely disappears"

LAYER 2: SOURCES OF TRUTH
  Definition: "the reference surfaces the agent consults to navigate it"
  Purpose: "reduces concept <> entity ambiguity and turns 'weekly active users'
            in a stakeholder's question into a specific, governed entity"
  Included surfaces:
    - Semantic layer: "the compiled metric and dimension definitions"
    - Lineage and transformation graphs: help "reason about which upstream models
      feed a concept, which are deprecated, and which share grain"
    - Historical SQL from dashboards and notebooks (for reference, NOT retrieval)
    - Company knowledge graph: "indexed docs, roadmaps, decision logs, and our
      organizational structure so the agent can resolve ambient references and
      ask better clarifying questions"

LAYER 3: SKILLS
  Definition: "a folder of markdown the agent reads on demand"
  Purpose: procedural knowledge — "which sources to consult in what order, how to
           navigate ambiguous data, and what a finished analysis looks like"
  Two types:
    - Knowledge skill: "a thin top-level router that allows additional domain
      details to load on demand... try the semantic layer first, but if there's
      no coverage, here are ~30 reference files for this domain"
    - Unbook skill: "encodes the process a senior analyst would follow: clarify
      the question, find sources (via the knowledge skill), run the query, and
      then loop the result through adversarial review sub-agents"

LAYER 4: VALIDATION
  Purpose: "how you find out which of the three failure modes is still leaking through"
  Included methods:
    - Dashboard-based evals: auto-generated by Claude (then human validated),
      covering most common stakeholder questions
    - Long tail evals: Claude-generated plausible questions from business context
      (roadmaps, table docs), covering broader domain
    - Ablation testing: "Every meaningful skill edit gets a before / after run on
      the relevant eval slice, with the delta in the PR description"
    - Adversarial review: "employing a Claude skill to aggressively challenge all
      underlying assumptions on a potential final answer increased accuracy by 6%
      within our eval set, but at the cost of 32% more tokens and 72% higher latency"
    - Correction harvesting: "A scheduled agent scans stakeholder channels every
      few hours for similar correction language, drafts a one-line fix to the
      relevant reference doc, and opens a PR tagged to the domain owner."
```

### Accuracy Benchmarks (from article)

```
Accuracy benchmarks — Anthropic analytics agent
Source: ibid., June 2026

Baseline (no skills): ≤21% on evals
With skills (aggregate): consistently above 95%
With skills (best domains): regularly around ~99%

SQL query retrieval augmentation: moved accuracy by less than a point
  (finding: structured skills >> raw query history retrieval)

Adversarial review sub-agents: +6% accuracy; +32% tokens; +72% latency
  (finding: high cost for incremental gain — use selectively based on stakes)
```

### Skill File Skeleton (Appendix structure from article)

```
Appendix: Skill File Skeleton
Source: ibid., June 2026

Front matter: name, version, description

Sections:
  "Warehouse Skill Instructions"
    - Description
    - Executing queries

  "Semantic Layer (REQUIRED first step)"
    - Required workflow
    - Date windows guidance

  "PART 1: MUST KNOW"
    - Quick Start Workflow
    - Business Context
    - Entity Disambiguation
    - Business Terminology
    - Data Integrity Requirements

  "PART 2: HOW TO DO"
    - Technical Execution Guide
    - Analysis Best Practices Guide

  "PART 3: DATA REFERENCES & RESOURCES"
    - Knowledge Base Navigation
    - Troubleshooting Guide
```

### Getting Started Decision Framework (from article)

```
Getting started questions — Anthropic analytics agent
Source: ibid., June 2026

Before building, align on:
  - "How important is a correct answer today vs. in the future?"
  - "How do you anticipate the complexity of your business to change over time?"
  - "How technical is the intended audience of the output?"
  - "How much are you willing to spend for improved accuracy?"
  - "What is your comfort around access controls and internal data privacy?"

Minimum viable starting point:
  "a handful of canonical datasets, a few dozen offline evals, and a thin
  knowledge skill will capture most of the upside."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-carta-healthcare-context-engineering.md` Claim 1 ("Integrating,
    organizing, and surfacing the right data at the right time is the real work. A
    perfectly written prompt with bad context gives bad answers."): Carta's finding that
    context construction — not prompt optimization — is the primary accuracy lever is the
    cross-domain equivalent of this article's central thesis. Here the "context" is the
    skills layer; in Carta, it is per-case runtime context assembly. Both sources converge
    on the same architectural conclusion: invest in what the agent knows (context/skills),
    not in how it is asked (prompt wording).
  - `blog-anthropic-mcp-production-agents.md` Claim 12 ("Skills and MCP are complementary.
    MCP gives an agent access to tools and data from external systems, while skills teach
    an agent the procedural knowledge of how to use those tools to accomplish real work."):
    This article provides extensive first-hand evidence for exactly why skills are so
    critical — the 21% → 95%+ accuracy gap is the quantified form of the "skills teach
    procedural knowledge" claim. The article also validates the two-layer architecture:
    the data foundations and sources of truth are the "tool access" layer; skills are
    the "procedural knowledge" layer on top.
  - `blog-anthropic-harness-long-running.md` Claim 2 ("Separating the agent doing the
    work from the agent judging it proves to be a strong lever"): The unbook skill's
    adversarial review sub-agents are a production implementation of the generator-verifier
    separation in an analytics context. The +6% accuracy finding here quantifies what
    harness-long-running describes structurally. Both sources agree on the mechanism;
    this article adds the cost side of the tradeoff.
  - `blog-anthropic-fong-finance-narrative.md` Claim 10 (Finance & Strategy archetype:
    "Interactive forecasting and cohort dashboards built from a prompt by analysts
    themselves: no SQL or engineering involvement needed."): Fong describes self-service
    analytics for the Finance & Strategy function as an archetype. This article is the
    technical account of how Anthropic built the underlying capability that makes that
    archetype possible. The architecture here (four layers, skills) is the infrastructure
    behind Fong's "no SQL or engineering involvement needed" outcome.

- **Extends**:
  - `blog-anthropic-mcp-production-agents.md` — That post establishes the skills + MCP
    architecture conceptually (Claim 12). This article documents in detail what skills
    look like in production: two skill types (knowledge and unbook), the skill file
    skeleton template, the connection to adversarial review sub-agents, and the specific
    accuracy impact of skills vs. no skills. Together the two posts form a complete
    picture: the two-layer architecture in principle (MCP post) and the skills layer
    in practice (this article).
  - `blog-anthropic-harness-long-running.md` — That post documents the generator/evaluator
    split for coding applications. This article extends the same pattern to analytics:
    the unbook skill instructs the agent to "loop the result through adversarial review
    sub-agents" as a standard workflow step. The quantified tradeoff (+6% accuracy,
    +32% tokens, +72% latency) extends the harness post's cost-benefit analysis with
    analytics-domain numbers.

- **Contradicts**: None filed. The SQL query retrieval finding (Claim 7) is counterintuitive
  but does not contradict any existing corpus claim — no prior source recommended raw
  SQL retrieval augmentation as an analytics agent accuracy lever. The finding is novel,
  not contradictory.

- **Novel**:
  - **21% → 95%+ accuracy gap from skills**: No prior corpus source quantifies the
    accuracy impact of the skills layer with this specificity. This is the first numeric
    ablation of a skills-vs-no-skills comparison in the corpus.
  - **Three failure modes taxonomy for analytics agents**: concept-entity ambiguity,
    data staleness, retrieval failure — as a named, structured taxonomy. No prior
    corpus source provides a failure mode taxonomy specific to analytics agent use cases.
  - **SQL query retrieval anti-pattern**: "less than a point" accuracy improvement from
    thousands of prior queries is a concrete counter-evidence against a common architectural
    intuition. No prior source documents this finding.
  - **Adversarial review quantified tradeoff**: +6% accuracy at +32% tokens and +72%
    latency is the first quantified cost-benefit disclosure for the adversarial review
    pattern in the corpus. Prior sources recommend the pattern; this article documents
    the specific cost.
  - **Knowledge skill vs. unbook skill distinction**: The two-type taxonomy of skills —
    thin router (knowledge) vs. procedural workflow encoder (unbook) — is a new named
    distinction not documented in any prior corpus source.
  - **Correction harvesting pattern**: Scheduled agent scanning stakeholder channels,
    drafting one-line reference doc fixes, opening tagged PRs — this automated staleness
    resolution pattern is completely new to the corpus.
  - **Skill file skeleton template**: A standardized template structure for warehouse
    skills (including the REQUIRED semantic layer section and the three PARTS structure)
    is the first reusable skill authoring artifact in the corpus.
  - **Five getting-started alignment questions**: The specific five questions for scoping
    an analytics agent deployment (correct answer stakes, business complexity trajectory,
    audience technical level, accuracy spend, access controls) are a novel pre-build
    decision framework not documented elsewhere.
  - **Production accuracy benchmarks for analytics agents**: The 95% automation rate
    and ~95% aggregate accuracy at Anthropic's scale is the first production-scale
    analytics agent metric in the corpus.

## Guide Impact

- **Chapter 03 or 04 (Agent Accuracy / Context Engineering)**: Add the three failure
  mode taxonomy (Claim 4) as the named diagnostic framework for analytics agent
  inaccuracies. Currently the corpus covers failure modes for coding agents and
  multi-agent systems; analytics-specific failure modes are absent. The three modes —
  concept-entity ambiguity, staleness, retrieval failure — are actionable design targets
  that map to specific architectural interventions in the four-layer stack.

- **Chapter 03 or 04 (Evaluation / Validation)**: Add the two-type offline eval framework
  (dashboard-based + long-tail, Claim 13) as the minimum viable eval suite for analytics
  agents. The "auto-generated by Claude, then human validated" workflow for dashboard
  evals is a concrete, replicable implementation pattern. The ablation testing norm
  ("every meaningful skill edit gets a before/after run") should be presented as the
  gate for skills development work.

- **Chapter 03 or 04 (Evaluation — Adversarial Review)**: The adversarial review
  tradeoff (Claim 12: +6% accuracy, +32% tokens, +72% latency) should be documented
  alongside `blog-anthropic-harness-long-running.md`'s evaluator cost-benefit analysis
  as the definitive cross-domain evidence that generator-verifier patterns are real
  costs, not free quality improvements. The guide should recommend adversarial review
  as a configurable option (use for high-stakes queries; skip for exploratory work) not
  a universal default.

- **Chapter 04 (Context Engineering / Skills)**: Add the knowledge skill vs. unbook
  skill distinction (Claim 11) as the two-tier skills architecture. The knowledge skill
  as a thin domain router (load ~30 reference files on demand) is the right first skills
  investment; unbook skills that encode the full analyst workflow are the advanced tier
  for high-value domains. The skill file skeleton (Concrete Artifacts) provides the
  reusable template.

- **Chapter 04 (Context Engineering)**: Add the SQL query retrieval anti-pattern
  (Claim 7) as named guidance: "raw retrieval of prior SQL queries does not
  substantially improve analytics agent accuracy — invest in structured skills instead."
  This is a direct architectural recommendation that prevents teams from building
  expensive vector-search-over-query-history infrastructure that the evidence says
  barely moves the needle.

- **Chapter 05 or 06 (Use Cases / Self-Service Analytics)**: Add the four-layer agentic
  analytics stack (Claims 8–11) as the production architecture reference for analytics
  agent deployments. The 95% automation / 95% accuracy metric (Claim 1) is the
  production target; the "handful of canonical datasets, few dozen offline evals, thin
  knowledge skill" recommendation (Claim 15) is the minimum viable starting point.

- **Chapter 06 (Continuous Improvement / Feedback Loops)**: Add the correction
  harvesting pattern (Claim 14) as the production implementation of automated staleness
  detection and resolution. The scheduled-agent-to-PR pattern is a concrete, reusable
  design that no prior corpus source documents mechanically.

- **Chapter 05 (Use Cases)**: This article corroborates and technically grounds Fong's
  finance analytics archetype (`blog-anthropic-fong-finance-narrative.md` Claim 10).
  The guide's treatment of self-service analytics for non-technical users (no SQL
  required) should cite both sources: Fong as the practitioner demand signal, this
  article as the technical architecture that delivers it.

## Extraction Notes

- The article was fetched from claude.com/blog using multiple targeted WebFetch calls
  with verbatim-extraction prompts (the claude.com blog is a JavaScript-rendered SPA
  that WebFetch AI-processes rather than reproducing verbatim). Quotes were extracted
  across 8 separate WebFetch passes with targeted prompts for specific sections and
  metrics. All verbatim quotes in this note appeared consistently across multiple
  passes.
- The article has five named co-authors (Chen Chang, Clement Peng, Justin Leder,
  Johanne Jiao, Josh Cherry), all from Anthropic's Data Science and Data Engineering
  team. The byline appears at the article footer: "This article was written by Chen
  Chang, Clement Peng, Justin Leder, Johanne Jiao, and Josh Cherry, members of the
  Data Science and Data Engineering team." No individual seniority or title is given.
- The article has 8 main sections plus an appendix: "Data is not software," "Our
  agentic analytics stack," "Data foundations," "Sources of truth," "Skills,"
  "Validation," "Getting started," and "Appendix" (Skill File Skeleton).
- The "unbook skill" name is unusual — "unbook" likely refers to "runbook" (a documented
  standard operating procedure) but the article consistently uses "unbook." Extracted
  verbatim; Assayers should verify spelling against source.
- The Appendix provides a skill file skeleton structure but not the content of a real
  deployed skill. The structure is extracted in Concrete Artifacts; actual skill content
  would be high-value for any practitioner building analytics skills.
- No linked sub-pages were followed. The article appears to be self-contained.
- No contradictions with existing corpus notes were identified. The SQL query retrieval
  finding (Claim 7) is counterintuitive but not contradicted by any existing note.
- Confidence is set to `emerging`: five named practitioners from Anthropic's data team
  writing about their own production system with specific metrics and concrete practices.
  The claims are specific and actionable. Confidence is not `settled` because: metrics
  are self-reported, no independent validation, and no methodology is disclosed for the
  eval suite. Confidence is not `anecdotal` because: five authors, production scale,
  specific quantified ablation results.
