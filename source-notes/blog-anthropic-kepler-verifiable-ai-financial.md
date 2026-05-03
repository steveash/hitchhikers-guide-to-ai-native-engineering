---
source_url: https://claude.com/blog/how-kepler-built-verifiable-ai-for-financial-services-with-claude
source_type: blog-post
title: "How Kepler Built Verifiable AI for Financial Services with Claude"
author: Anthropic (case study featuring Vinoo Ganesh, CEO and John McRaven, CTO, Kepler Finance)
date_published: 2026-04-30
date_extracted: 2026-05-03
last_checked: 2026-05-03
status: current
confidence_overall: emerging
issue: "#496"
---

# How Kepler Built Verifiable AI for Financial Services with Claude

> Production case study showing how Kepler Finance built an auditable AI system
> for regulated financial services by architecturally separating Claude's reasoning
> layer from deterministic computation, naming the "content engineering" vocabulary
> distinction, and treating provenance as an upfront architectural constraint rather
> than a retrofit.

## Source Context

- **Type**: blog-post (Anthropic/Claude blog, April 30, 2026; corporate case study with
  named founder quotes and production scale metrics)
- **Author credibility**: Anthropic-published case study featuring Vinoo Ganesh (CEO) and
  John McRaven (CTO) of Kepler Finance. Company founded in 2025 after discovery interviews
  with 147 financial firms. Marketing framing present — hosted on claude.com, positions
  Claude favorably — but technical substance comes from named engineers describing a
  production system. Scale metrics (26M+ SEC filings indexed in under three months,
  14,000+ companies, 27 markets) and compliance posture (SOC 2 Type II achieved) are
  independently verifiable in principle. The 94% taxonomy accuracy figure is self-reported.
  No code, no architecture diagrams, no ablation studies. Treat as a practitioner case
  study with medium depth: patterns are real, single-company evidence.
- **Scope**: Covers Kepler Finance's architecture for verifiable AI in financial services
  across five areas: (1) model selection and long-horizon task coherence, (2) the
  deterministic-layer / LLM-reasoning architectural separation, (3) the "content
  engineering" vocabulary distinction, (4) per-stage multi-model routing (Opus 4.7 /
  Sonnet 4.6), and (5) evaluation pipeline design and provenance architecture. Does NOT
  provide code, API details, architecture diagrams, or controlled comparisons between
  systems. Does NOT cover latency, cost structure, or deployment specifics.

## Extracted Claims

### Claim 1: For multi-step financial analysis, Claude maintained long-horizon plan coherence where competing frontier models silently dropped constraints mid-task

- **Evidence**: Ganesh's direct comparison during pre-founding competitive benchmarking
  across all frontier models on Kepler's specific workloads. The specific failure mode
  identified in other models: starting strong but dropping a constraint by step five
  without signaling the omission.
- **Confidence**: emerging (practitioner assertion from competitive benchmarking; no
  controlled study details or methodology provided; single-company workload; single
  practitioner source)
- **Quote**: "On our workloads, Claude was the model that consistently held the plan
  together. Other models would start strong and then quietly drop a constraint by
  step five." — Vinoo Ganesh, CEO
- **Our assessment**: The "quietly drop a constraint" failure mode is the specific
  downstream risk in multi-step financial analysis that Ganesh is flagging: not an
  outright error but a silent degradation where a binding constraint (e.g., fiscal
  period scope, segment boundary, exclusion criterion) is abandoned without announcement.
  This is harder to detect than an error because the output continues to look plausible.
  Ganesh's framing — plan coherence, not benchmark score — is an important calibration
  point for the guide: financial services require task-completion fidelity across many
  sequential steps, which is distinct from what typical single-turn benchmarks measure.
  The failure mode is generalizable to any long multi-step reasoning pipeline where
  early constraints must be honored throughout.

### Claim 2: Ambiguity escalation — stopping to ask analysts to clarify rather than silently assuming — matters more than benchmark scores in multi-step financial workflows

- **Evidence**: Ganesh's direct production observation of Claude's behavior on terms with
  multiple possible meanings in financial analysis. The mechanism: one wrong assumption
  at step one compounds through all downstream steps because subsequent computations are
  built on the initial interpretation.
- **Confidence**: emerging (practitioner assertion backed by production observation; no
  controlled comparison of escalation rate vs. downstream error rate provided)
- **Quote**: "That behavior matters more than any benchmark score. One wrong assumption
  early in a financial analysis breaks everything downstream." — Vinoo Ganesh, CEO
- **Our assessment**: This is the load-bearing behavioral requirement Ganesh identifies
  for financial AI. When a term has multiple possible meanings (e.g., "revenue" under
  different accounting standards, "EBITDA" under different definitional conventions),
  silent assumption is the wrong design choice because the propagation mechanism makes
  the cost high and the error invisible until late. Escalation has high expected value
  even when it adds friction. This generalizes: in any long multi-step reasoning
  pipeline where early ambiguity, if unresolved, compounds through downstream steps,
  escalation behavior is architecturally important and should be tested for explicitly
  during model selection — not assumed from benchmark scores.

### Claim 3: Claude is treated as one stage in a pipeline — the surrounding deterministic infrastructure is as load-bearing as the model itself

- **Evidence**: McRaven's explicit architectural framing. Claude handles interpretation,
  intent decomposition, and ambiguity resolution at its stage. Deterministic components
  handle all computation that must be provably correct: ratio calculations, fiscal period
  resolution, formula evaluation. The model's job is to hand the next stage exactly what
  it needs.
- **Confidence**: emerging (practitioner assertion; architectural design philosophy;
  single company; self-reported)
- **Quote**: "In finance, the model can't be the whole system. We treat it as one stage
  in a pipeline whose job is to hand the model exactly what it needs to succeed at
  exactly that stage." — John McRaven, CTO
- **Our assessment**: This is the architectural principle that makes Kepler's
  verifiability claim meaningful. By restricting Claude to interpretation and planning
  stages, every output that becomes a number in an audit trail originates from
  deterministic execution — not model generation. The model output can structurally
  never be the final number. This is a stronger trust guarantee than a prompt-level
  instruction to "only output verified numbers": the architecture enforces it, not a
  policy. The principle is transferable: any regulated domain that requires provably
  correct computation (not just plausible computation) should separate reasoning from
  execution architecturally.

### Claim 4: "Content engineering" — optimizing the system around a model call — is architecturally distinct from "prompt engineering" — optimizing an individual call

- **Evidence**: McRaven's direct definitional distinction. Content engineering addresses
  what information the model receives at each stage, the ontologies that constrain
  interpretation, the hard escalation boundaries. Prompt engineering addresses wording
  optimization within a single call. The two are complementary but operate at different
  scopes.
- **Confidence**: emerging (novel vocabulary from a single named practitioner; the
  distinction is real but not yet standardized; single-company origin)
- **Quote**: "Prompt engineering optimizes a call while content engineering optimizes
  the system around it." — John McRaven, CTO
- **Our assessment**: This is the most novel conceptual contribution in the article.
  McRaven is naming a distinction the corpus has previously described differently:
  "context engineering" (Carta Healthcare), "harness design" (Anthropic Engineering
  Blog), "system context design" (various sources). "Content engineering" specifically
  foregrounds what information is supplied to the model at each stage across the full
  system design — including ontologies, precise definitions, and hard escalation
  boundaries — rather than per-call prompt optimization. It is wider than call-level
  prompt optimization and narrower than full harness engineering. The vocabulary is
  practitioner-specific (McRaven's coinage, not a standard term), but the concept is
  load-bearing for Ch04. Note: this is a different but adjacent concept to "context
  engineering" as used in the Carta note — both describe disciplines of system-level
  information design, with slightly different emphasis. Not a contradiction; a
  terminological variation worth preserving in the guide.

### Claim 5: A proprietary financial ontology — mapping concepts to precise definitions — is a prerequisite content engineering artifact for production financial AI

- **Evidence**: McRaven's architectural description. The ontology maps financial concepts
  to precise definitions, ensuring consistent interpretation of terms across all model
  calls. It is part of the system context, not a per-call prompt element. It functions
  as a disambiguation artifact that reduces the need for real-time escalation on terms
  that have already been systematically defined.
- **Confidence**: emerging (architectural design claim; single company; no comparison
  to systems operating without curated ontologies)
- **Quote**: (no verbatim named quote; derived from article's architectural description
  section)
- **Our assessment**: The ontology is the content engineering artifact that operationalizes
  the ambiguity-escalation principle (Claim 2). By systematically pre-defining financial
  concepts, Kepler reduces the surface area of ambiguity that Claude must escalate on.
  The pattern generalizes: for any domain with high definitional precision requirements
  (finance, law, clinical medicine), a curated ontology is the structured knowledge
  artifact that bridges domain expert definitions and model interpretation — prerequisite
  to production-grade LLM deployment.

### Claim 6: Idempotent, modular skill design — same input always produces same output — enables pipeline stage improvement without ripple effects

- **Evidence**: McRaven's design description. Recurring workflow skills (enterprise value
  calculations, segment revenue waterfall reconciliation) are explicitly designed for
  idempotency. Improvements at one stage do not require pipeline-wide changes.
- **Confidence**: emerging (architectural design claim; single system; idempotency claim
  is self-reported; no stress-test data)
- **Quote**: (no verbatim named quote; derived from article's architectural description)
- **Our assessment**: Idempotency in pipeline stages is a standard software engineering
  discipline applied deliberately to AI workflow design. In a multi-stage AI pipeline,
  non-idempotent stages introduce compounding variance: if stage A occasionally produces
  different outputs for the same input, stage B's reliability is a function of stage A's
  variance profile. Idempotent skills decouple stage reliability, allowing teams to
  improve one stage's accuracy or update one model independently of all others. For
  Kepler, this is critical because financial audit trails require that the same input
  always produce the same output — idempotency is both an engineering convenience and a
  regulatory necessity.

### Claim 7: Per-stage model routing (Opus 4.7 for complex reasoning stages, Sonnet 4.6 for constrained throughput stages) outperforms running everything on a single model for quality and cost

- **Evidence**: McRaven's stated design rationale. Opus 4.7 handles intent decomposition,
  ambiguity resolution, and structured execution planning — stages where complex reasoning
  is the primary requirement. Sonnet 4.6 handles constrained, high-throughput stages where
  volume matters more than reasoning depth.
- **Confidence**: emerging (practitioner design decision; single system; no ablation data
  comparing single-model vs. multi-model routing provided)
- **Quote**: (the routing rationale is described in the article; no verbatim named quote
  confirmed from source)
- **Our assessment**: The specific routing criterion — reasoning complexity and ambiguity
  of the stage — is more actionable than the generic advice to "use cheaper models for
  simpler tasks." The implied trade-off is: a single expensive model wastes cost on
  constrained stages; a single cheap model sacrifices quality on reasoning-intensive
  stages. The explicit per-stage model assignment (Opus 4.7 for decomposition/ambiguity,
  Sonnet 4.6 for constrained throughput) provides a concrete instantiation of the routing
  principle. This is the production-financial-services instantiation of the pattern;
  the specific model choices reflect the task profile, not a universal recommendation.

### Claim 8: Automated evaluation pipelines — testing every prompt change, model upgrade, and context modification against known-correct answers at every stage — are the development discipline for production financial AI

- **Evidence**: Description of Kepler's evaluation pipeline from the "Best practices"
  section. Tests run at every stage independently and end-to-end before any change goes
  to production. Failures are attributed to reasoning (model), context (content
  engineering), or downstream execution (deterministic layer). New Anthropic model
  versions are benchmarked within hours of release.
- **Confidence**: emerging (practitioner assertion; architectural design claim;
  self-reported; no external validation of the evaluation pipeline)
- **Quote**: (not a direct named quote; from article's "Best practices from the Kepler
  team" section)
- **Our assessment**: Kepler's three-axis evaluation attribution (reasoning / context /
  execution) is the same diagnostic structure Carta Healthcare's Mazzanti describes for
  clinical extraction (prompt / context / retrieval). Two different regulated domains
  independently converging on the same evaluation design principle strengthens the claim.
  The within-hours new model benchmarking cadence is notable: Kepler treats each Anthropic
  model release as a candidate requiring immediate evaluation rather than a deferred
  upgrade decision. This is the operational posture required when model selection
  (Claim 7) is a deliberate per-stage architectural choice.

### Claim 9: Provenance must be designed in from day one — full traceability to source SEC filings, page numbers, and line items is an architectural constraint, not a compliance feature added after the fact

- **Evidence**: McRaven's explicit design principle, stated as the foundational architectural
  requirement. Full audit logging, siloed customer environments, and end-to-end provenance
  were built from inception. SOC 2 Type II achieved; ISO 27001 underway.
- **Confidence**: emerging (practitioner design philosophy; self-reported outcomes; no
  independent audit of the provenance chain; single company)
- **Quote**: "Provenance has to shape the entire system, not get added at the end."
  (From article's "Design Principles" section; attributed to McRaven's architecture
  philosophy)
- **Our assessment**: The "not get added at the end" formulation is the most actionable
  insight in this category. Teams building regulated AI systems frequently defer audit
  trail design to late-stage development, treating it as infrastructure to add once the
  core pipeline works. Kepler's claim is that this creates architectural debt that cannot
  be cleanly repaid: provenance logging embedded from inception is structurally different
  from logging retrofitted to an existing pipeline. The traceability requirement (every
  number back to a specific SEC filing page and line item) is an extreme form, but the
  principle scales down to any regulated use case — the key insight is that provenance
  requirements constrain how the pipeline is designed, not merely what it logs.

### Claim 10: Specialized proprietary models alongside Claude achieve dramatically higher accuracy on narrow, well-defined domain tasks — 94% vs. 38–46% for competing models on financial taxonomy mapping

- **Evidence**: Kepler trained a proprietary model for mapping financial statement labels
  to standard taxonomy codes. On this narrowly scoped recall task, their specialized model
  achieves 94% accuracy vs. 38–46% from competing frontier models. The task is
  classification, not reasoning.
- **Confidence**: emerging (self-reported metric; no independent validation; task is
  well-defined and accuracy is a measurable property; single company)
- **Quote**: (from article metrics section; no direct verbatim named quote)
- **Our assessment**: The 94% vs. 38–46% gap is dramatic and plausible for a narrow,
  structured mapping task where training data can be precisely curated. This is not a
  claim about general Claude capability — it is a claim about the value of purpose-built
  fine-tuned models for well-defined, high-frequency classification tasks within a larger
  LLM system. The architecture insight is: Claude handles reasoning and interpretation;
  fine-tuned specialist models handle recall-intensive classification; deterministic
  systems handle computation. Three different execution contexts for three different
  capability profiles. This is the practical case for hybrid architectures over
  single-model-for-everything.

### Claim 11: Discovery with 147 financial firms before founding revealed that auditability is the irreducible trust requirement — not accuracy

- **Evidence**: Ganesh's description of the company's founding research. A managing
  director's question anchored the entire architecture's verifiability requirements.
  Auditability — being able to explain and trace every output — is framed as more
  fundamental than accuracy.
- **Confidence**: anecdotal (single quote; single discovery conversation reported;
  no systematic documentation of all 147 interviews)
- **Quote**: "How am I supposed to trust something I can't audit?" — Managing Director
  (unnamed financial firm)
- **Our assessment**: This is the practitioner-derived design requirement that explains
  why Kepler's architecture is structured the way it is. The question is not "can the
  AI produce accurate outputs?" but "can I verify the outputs before acting on them?"
  Accuracy without auditability is insufficient in regulated financial analysis, because
  the analyst cannot take accountability for outputs they cannot trace. Every architectural
  choice in Kepler's system (deterministic execution layer, full provenance logging,
  siloed environments) satisfies this requirement rather than optimizing for a
  benchmark-based accuracy metric. For the guide: regulated-industry AI requirements
  should be derived from the practitioners in those industries, not assumed from general
  compliance frameworks.

## Concrete Artifacts

### Architectural Separation Pattern (Kepler Production System)

```
Kepler Financial AI Architecture — Separation of Concerns
Source: McRaven description, April 2026 case study

WHAT CLAUDE HANDLES (reasoning layer):
  - Intent decomposition (understanding the analyst's question)
  - Ambiguity resolution (escalating when terms have multiple meanings)
  - Structured execution planning (determining what data and formulas are needed)
  - Interpretation of results (translating computational outputs to analyst language)

WHAT DETERMINISTIC INFRASTRUCTURE HANDLES (execution layer):
  - Ratio calculations (e.g., EV/EBITDA, P/E, debt-to-equity)
  - Fiscal period resolution (matching analyst questions to correct reporting periods)
  - Formula evaluation (applying financial formulas to extracted data)
  - Idempotent skill execution (EV calculations, segment revenue waterfall reconciliation)

WHAT PROPRIETARY SPECIALIZED MODELS HANDLE (recall layer):
  - Financial taxonomy mapping (statement labels → standard taxonomy codes)
    Accuracy: 94% (vs. 38–46% for competing models)

PROVENANCE CHAIN:
  - Every final number → deterministic execution (not model output)
  - Every deterministic computation → source data
  - Every source data point → specific SEC filing, page number, line item

COMPLIANCE POSTURE:
  - SOC 2 Type II certified
  - ISO 27001 underway
  - Siloed customer environments
  - Full audit logging from day one
```

### Per-Stage Model Routing (Kepler)

```
Stage Type                        | Model       | Rationale
----------------------------------|-------------|-------------------------------
Intent decomposition              | Opus 4.7    | Complex reasoning required
Ambiguity resolution              | Opus 4.7    | Nuanced interpretation needed
Structured execution planning     | Opus 4.7    | Multi-constraint planning
Constrained high-throughput tasks | Sonnet 4.6  | Volume matters more than depth

McRaven design rationale: running everything on one model leaves
either quality or cost on the table.
```

### Design Principles (Kepler — "Best practices from the Kepler team")

```
Source: Kepler case study, April 2026

1. RIGHT-JOB ASSIGNMENT
   Retrieval → query engines
   Computation → formula engines
   Interpretation, planning → Claude

2. MODEL SPECIALIZATION
   Complex reasoning stages:      Opus 4.7
   Constrained throughput stages: Sonnet 4.6
   Narrow recall classification:  proprietary fine-tuned model

3. EVALUATION-FIRST
   - Automated pipelines test every prompt change, model upgrade,
     and context modification before production
   - Test each stage independently AND end-to-end
   - Benchmark new Anthropic model versions within hours of release
   - Attribute failures: reasoning (model) vs. context vs. execution

4. PROVENANCE ARCHITECTURE
   "Provenance has to shape the entire system, not get added at the end."
   - Build audit logging and traceability from inception
   - Every output traceable to source documents
```

### Production Scale Metrics

```
Platform:    Kepler Finance
Founded:     2025 (Vinoo Ganesh, CEO; John McRaven, CTO)
Research:    147 financial firms interviewed before founding
Data scale:  26M+ SEC filings (indexed in <3 months)
             50M+ public documents
             1M+ private documents
Coverage:    14,000+ companies, 27 global markets
Tech stack:  AWS, Rust, Python, containers
Taxonomy:    94% accuracy (proprietary model) vs. 38–46% (competing models)
Compliance:  SOC 2 Type II certified; ISO 27001 underway
Model use:   Claude (Opus 4.7 for reasoning stages, Sonnet 4.6 for throughput)
```

## Cross-References

- **Corroborates** `blog-anthropic-carta-healthcare-context-engineering.md` Claim 5
  (granular evaluation attributing failures to prompt, context, or retrieval is the
  correct architecture for debugging extraction pipelines): Kepler's evaluation pipeline
  uses the same three-axis attribution — failures attributed to Claude's reasoning,
  the provided context, or downstream execution. Both Carta and Kepler independently
  arrived at the same evaluation design principle from different regulated domains
  (healthcare and financial services). The convergence across domains and case-study
  formats strengthens the claim that stage-attributable evaluation is a general
  requirement for production AI in regulated industries.

- **Corroborates** `blog-anthropic-multi-agent-coordination-patterns.md` Claim 7
  (orchestrator-subagent is the recommended default multi-agent coordination pattern):
  Kepler's pipeline — intent decomposition → execution planning → deterministic execution
  — is a production instantiation of the orchestrator-subagent pattern in financial
  services. Kepler's per-stage model routing (Claim 7 here) adds a layer of specificity
  the coordination patterns note does not include: the reasoning-stage model selection
  (Opus 4.7) differs from the constrained-stage selection (Sonnet 4.6) and the choice
  is explicit and rationale-backed, not a default.

- **Corroborates** `blog-anthropic-compliance-api.md` Claim 4 (inference activities are
  not logged by the Compliance API — regulated-industry teams must implement
  application-layer logging themselves): Kepler's provenance architecture (full audit
  logging from inception, end-to-end traceability to SEC filings) is the application-layer
  logging implementation that the compliance-api note identifies as a gap requiring
  team-built solutions. Kepler fills that gap by design — as a first-class architectural
  constraint, not an afterthought. This confirms the compliance-api note's prescription
  with a production example in a named regulated-industry context.

- **Corroborates** `blog-anthropic-harness-long-running.md` Claim 9 (every harness
  component encodes an assumption about what the model cannot do — those assumptions
  should be stress-tested at each model upgrade): Kepler's explicit stage assignment —
  Claude handles interpretation, deterministic systems handle computation — is the
  positive formulation of this principle. Where the harness-long-running note focuses
  on pruning components as model capability improves, Kepler shows how the same principle
  guides initial design: components are added specifically for what the architecture
  requires Claude NOT to do (produce final numbers), not merely for what it cannot do
  today. The architecture deliberately confines Claude to its comparative advantage within
  the pipeline.

- **Extends** `blog-anthropic-carta-healthcare-context-engineering.md`: Carta documented
  runtime context assembly (per-query context scoping) as the primary accuracy lever for
  structured extraction in healthcare. Kepler adds a complementary pattern for regulated
  industries: the deterministic execution layer as the architectural provenance guarantee.
  Carta's insight addresses what the model receives; Kepler's deterministic-layer insight
  addresses what happens downstream of the model's output. Together they describe both
  upstream (context engineering) and downstream (execution separation) pipeline design
  for regulated AI.

- **Extends** `blog-anthropic-compliance-api.md`: The compliance-api note established
  the platform-level inference logging gap and the prescription that teams must build
  application-layer logging themselves. This source shows how a production financial
  services team fills that gap architecturally: by designing provenance into the execution
  pipeline from day one, with every number traceable through deterministic paths to SEC
  source documents. The compliance-api note documented the gap; this source documents a
  reference architecture for filling it.

- **Novel**:
  - **"Content engineering" as a named, distinct vocabulary from "prompt engineering"**:
    McRaven's formulation ("content engineering optimizes the system around it") is a new
    term in this corpus. Existing notes use "context engineering" (Carta), "harness design"
    (harness-long-running), and "system design" generically. "Content engineering"
    specifically names the discipline of optimizing what information reaches the model at
    each stage across the full system — including ontologies and escalation boundaries —
    as distinct from per-call prompt optimization. Whether this becomes standardized
    vocabulary is unknown, but the concept is worth preserving.
  - **Deterministic execution layer as an architectural trust guarantee for regulated AI**:
    The pattern of separating Claude's reasoning from computation such that model output
    is structurally unable to become a final auditable number is not described in any
    prior corpus note. This is the most architecturally specific verifiability pattern
    in the corpus for regulated industries.
  - **Provenance-first as an upfront architectural constraint, not a compliance feature**:
    "Provenance has to shape the entire system, not get added at the end" as an explicit
    design principle for regulated AI is new. Prior corpus sources discuss provenance as a
    compliance concern; this source positions it as a foundational architectural decision
    that constrains all other design choices.
  - **"Silent constraint dropping" as a named failure mode in long multi-step tasks**:
    Ganesh's description of competing models "quietly dropping a constraint by step five"
    names a specific failure mode — silent mid-plan constraint abandonment — that is
    harder to detect than an outright error because the output remains plausible. This is
    new vocabulary for a previously unnamed failure class.
  - **Proprietary financial ontology as a prerequisite content engineering artifact**:
    The use of a curated domain ontology (mapping concepts to precise definitions) as a
    mandatory system component for financial AI — not as a prompt element but as a shared
    definitional layer — is not described in other corpus notes.

## Guide Impact

- **Chapter 03 (Safety and Verification)**: Add "deterministic trust layer" as a named
  pattern for regulated-industry AI. Pattern: restrict the LLM to interpretation,
  decomposition, and planning; route all computation that must be provably correct through
  deterministic execution environments. Cite McRaven: "The model can't be the whole
  system." This is the architectural answer to "how do you make AI outputs auditable in
  regulated domains?" — structurally enforced, not policy-based. Pair with the Carta note
  as two complementary regulated-industry case studies that together cover context
  engineering (upstream) and execution separation (downstream).

- **Chapter 04 (Context Engineering)**: Add "content engineering" as a vocabulary entry
  — the discipline of optimizing what information the model receives at each stage across
  the full system design, including ontologies, precise definitions, and escalation
  boundaries. Distinguish from "context engineering" (per-query context assembly, per
  Carta) and "prompt engineering" (per-call optimization). Cite McRaven's formulation
  as the practitioner origin. Note this vocabulary is not yet standardized.

- **Chapter 02 (Harness Engineering)**: Add "per-stage model routing" as a named pattern
  with concrete routing criteria. Criterion from Kepler: Opus-class models for stages
  requiring complex reasoning (intent decomposition, ambiguity resolution, multi-constraint
  planning); Sonnet-class models for constrained high-throughput stages. Pair with the
  multi-agent coordination patterns note (orchestrator-subagent topology) and this source
  (model-routing layer within that topology) as complementary guidance.

- **Chapter 02 (Harness Engineering)**: Add idempotent modular skill design as a named
  design requirement for regulated-domain multi-stage pipelines. Idempotency is both an
  engineering convenience (per-stage independent improvement) and a regulatory necessity
  (reproducible outputs). Cite Kepler's EV calculation and segment revenue reconciliation
  skills as concrete examples.

- **Chapter 03 (Safety and Verification)**: Add provenance-first as a named design
  principle: "Provenance has to shape the entire system, not get added at the end." Use
  Kepler's traceability chain (number → deterministic computation → source data → SEC
  filing page and line item) as the production exemplar for what full-provenance AI looks
  like in a regulated domain. Pair with the compliance-api note's platform-level logging
  gap as the problem context.

- **Chapter 03 (Safety and Verification)**: The three-axis evaluation attribution
  (reasoning / context / execution) corroborates the same pattern from Carta Healthcare
  (prompt / context / retrieval). Cite both as converging evidence for stage-attributable
  evaluation design. The within-hours model benchmarking cadence is worth including as
  the operational posture for teams building on a rapidly evolving platform.

## Extraction Notes

- Source is Anthropic-published marketing content (claude.com/blog). Marketing framing
  is present throughout — Claude is positioned as uniquely capable. Structural patterns
  are extracted; model capability claims are not cited as independent evidence.
- No code, no architecture diagrams, no ablation comparisons. All claims rest on
  practitioner authority and production scale metrics. Confidence ratings are "emerging"
  throughout accordingly.
- The article's section headings were: "Handling long, multi-step tasks and flagging
  ambiguity," "Engineering the context around Claude," "Scaling with Claude," "Best
  practices from the Kepler team." These guided claim extraction by section.
- Three Prospector triage comments were filed on the issue, all convergent on the same
  extraction targets (deterministic trust layer, content engineering vocabulary, ambiguity
  escalation, idempotent skills, multi-model routing, evaluation-first, provenance).
  Convergence across three independent triage runs increases confidence that the correct
  extraction targets were identified.
- The article was read in full via two WebFetch passes: the first for full content
  synthesis; the second specifically for direct named quotes and section headings. Named
  quotes that appeared in the Prospector's triage comments but were not confirmed by
  WebFetch passes are NOT presented as verbatim quotes in this note. The confirmed named
  quotes are attributed by name as extracted.
- "Content engineering" (McRaven) is a different term from "context engineering" (Carta
  Healthcare / broader corpus). Both describe system-level information design disciplines;
  they overlap but differ in emphasis. Not a contradiction — preserved both terms in this
  note to allow the guide to compare vocabulary origins.
- Kepler was founded in 2025, making this a very recent post-cutoff company. Production
  metrics (26M+ SEC filings, SOC 2 Type II) indicate a mature-enough system to have real
  architecture lessons despite the company's youth.
- The Prospector cited "Running everything on one model leaves either quality or cost on
  the table" as a quote from the source. This phrase was NOT confirmed in verbatim form
  by the Miner's WebFetch passes and is presented as a paraphrase of McRaven's routing
  rationale, not a direct quote.
- No sub-pages were linked from the article that required following.
