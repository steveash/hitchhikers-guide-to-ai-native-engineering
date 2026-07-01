---
source_url: https://martinfowler.com/articles/reliable-llm-bayer.html
source_type: blog-post
title: "Building Reliable Agentic AI Systems"
author: Sarang Sanjay Kulkarni (Principal Consultant, Thoughtworks), with Bayer AG engineering contributors
date_published: 2026-06-16
date_extracted: 2026-07-01
last_checked: 2026-07-01
status: current
confidence_overall: emerging
issue: "#1396"
---

# Building Reliable Agentic AI Systems

> A detailed practitioner case study of PRINCE, Bayer AG's production agentic RAG +
> Text-to-SQL platform for preclinical drug research, that retroactively frames its
> architecture using "context engineering" (what each specialized agent sees) and
> "harness engineering" (orchestration, retries, state persistence, and reflection
> loops built around the models) — with concrete pipeline parameters, a three-tier
> reflection architecture, and a documented decision to remove an LLM verifier step
> that was over-rejecting valid output.

## Source Context

- **Type**: blog-post (long-form technical case study published on martinfowler.com,
  16 June 2026)
- **Author credibility**: Sarang Sanjay Kulkarni is a Principal Consultant at
  Thoughtworks who "focuses on building production-grade GenAI systems, particularly
  Retrieval-Augmented Generation (RAG) and multi-agent workflows" and teaches an
  O'Reilly course on production-ready RAG applications. The article is published on
  martinfowler.com, a `trusted-feed` source in this repository, which applies editorial
  vetting distinct from a personal blog. The acknowledgments name five Bayer AG
  engineers (Adam Zalewski, Annika Kreuchwig, Carlos Henrique Vieira-Vieira, Jobst
  Löffler, Jonas Münch) and fourteen additional Thoughtworks contributors, indicating
  this reflects a real, jointly-built production system rather than a single
  consultant's account. The article states the author used AI assistance for
  "brainstorming ideas, creating outlines, and reviewing drafts" — disclosed
  explicitly, not hidden. The piece references a companion peer-reviewed paper in
  *Frontiers in Artificial Intelligence* covering product/business impact (not
  fetched for this note — the martinfowler.com article is scoped to technical
  architecture).
- **Scope**: Covers the end-to-end architecture of PRINCE — a Bayer AG platform that
  evolved through three phases (Search → Ask → Do) into a LangGraph-orchestrated
  multi-agent system combining Agentic RAG (for unstructured PDF study reports) and
  Text-to-SQL (for structured metadata in Amazon Athena). Covers: system architecture,
  the five-stage agentic workflow (Clarify Intent → Think & Plan → Research →
  Reflection → Writer), the RAG retrieval pipeline internals, the Text-to-SQL pipeline
  internals, evaluation and monitoring (RAGAS via Langfuse), error handling/recovery
  (Postgres/DynamoDB state, LLM fallbacks), and a data-quality NER pipeline. Does NOT
  cover: exact cost/latency figures, specific prompt text, model names/versions used
  per stage, or an independent/external audit of the reported outcomes. Business
  impact and adoption metrics are explicitly deferred to the companion paper and are
  not present in this article.

## Extracted Claims

### Claim 1: The authors retroactively frame PRINCE's engineering decisions using "context engineering" (what each agent sees) and "harness engineering" (the scaffolding around the models), though these terms did not exist when the system was designed

- **Evidence**: Direct authorial framing statement in the introduction, applied
  consistently as the organizing lens for the rest of the article.
- **Confidence**: settled (this is the article's own explicit stated framing, not an
  inferred pattern)
- **Quote**: "Many of the engineering decisions behind PRINCE can now be understood through the lens of context engineering and harness engineering, although when the system was first designed we did not use these terms. Context engineering shaped what information each model received, what it did not receive, and how context moved between specialized steps such as research, reflection, and writing. Harness engineering shaped the scaffolding around the models: orchestration, tool boundaries, state persistence, retries, fallbacks, validation, reflection loops, observability, and human review."
- **Our assessment**: This is a valuable retrospective validation of the guide's own
  vocabulary from a source with no incentive to use it — Thoughtworks/Bayer built the
  system years before framing it this way, then applied "context engineering" and
  "harness engineering" post hoc as the clearest available description of what they'd
  already built. This is stronger evidence for the terms' descriptive validity than a
  source coined to advocate for the terminology in advance.

### Claim 2: "Context discipline" — being selective about what each agent sees — remained necessary even as context windows grew larger, because over-stuffed context made the system harder to steer and evaluate

- **Evidence**: Direct architectural principle statement, tied to concrete stage-by-
  stage context assignment (planning context, retrieval context, evidence context,
  synthesis context).
- **Confidence**: emerging (practitioner-reported architectural principle from a single
  production system; consistent with the guide's existing corpus but not independently
  measured here)
- **Quote**: "A design principle running through this architecture is context discipline. Larger context windows did not remove the need to be selective about what each agent sees. In early iterations, putting too much information into the context made the system harder to steer and harder to evaluate. PRINCE therefore avoids treating the prompt as one large container for all available information. Instead, different stages receive different context: planning context for Think & Plan, retrieval context for the Researcher Agent, evidence context for the Reflection Agent, and synthesis context for the Writer Agent."
- **Our assessment**: This directly corroborates the per-query/per-agent context
  scoping pattern documented in `blog-anthropic-carta-healthcare-context-engineering.md`
  (Claim 2), but from the opposite architectural angle: Carta scopes context per
  extracted data point within one workflow step, while PRINCE scopes context per
  *workflow stage* across a multi-agent pipeline. Both converge on the same underlying
  claim — a bigger context window is not a substitute for context curation — from
  different system shapes (single-agent extraction vs. multi-stage agent pipeline).

### Claim 3: A "Clarify User Intent" step that proactively asks clarifying questions functions as the first context-assembly decision, narrowing scope before retrieval begins and preventing wasted trial-and-error tool selection

- **Evidence**: Architectural description of the intent-clarification stage, framed
  explicitly as a "fail-fast" mechanism, with justification tied to tool-selection
  ambiguity as the system scaled to more domains.
- **Confidence**: emerging (practitioner design rationale; the described benefit —
  reduced wasted execution — is plausible but not quantified with a before/after metric)
- **Quote**: "This “fail-fast” mechanism prevents wasted execution on vague queries, while careful tuning ensures the system remains unobtrusive when the intent is already clear. From a context engineering perspective, this step is the first assembly decision in the workflow: it constrains which tools, domains, and data sources will be in scope before any retrieval begins, ensuring subsequent agents receive a focused rather than open-ended problem."
- **Our assessment**: This names intent clarification itself as a context engineering
  act, not merely a UX nicety — the decision of what NOT to retrieve is made before
  retrieval starts. This is a distinct, earlier point of context control than the
  per-stage routing in Claim 2 and is a reusable pattern for any agentic system
  choosing among many overlapping tools/domains.

### Claim 4: A dedicated "Think & Plan" reasoning step, modeled on Anthropic's Think tool, produced a "dramatic improvement" in tool-selection accuracy as the number of available tools grew and their domain boundaries began to overlap

- **Evidence**: Practitioner account of a specific problem (tool selection degrading as
  tool count grew, due to overlapping domains like structured vs. unstructured data
  covering similar concepts) and the fix (explicit reasoning step before tool
  invocation).
- **Confidence**: emerging (practitioner-reported outcome; "dramatic improvement" is not
  quantified with a specific accuracy delta)
- **Quote**: "By introducing a dedicated thinking step, the system can explicitly reason about which tool best matches the user's intent, evaluate the characteristics of each available tool, and make a more informed decision. This approach led to a dramatic improvement in the accuracy of tool selection."
- **Our assessment**: The failure mode described — tool selection degrading as tool
  count and domain overlap grow — is a concrete, generalizable warning for any harness
  design that keeps flatly adding tools to a single agent's toolbox. The fix (a
  dedicated pre-action reasoning step) is the same mechanism named "process reflection"
  later in the article (Claim 8), applied specifically to tool selection rather than
  general trajectory evaluation.

### Claim 5: PRINCE is actively evolving its single "Researcher Agent" into a hierarchy of domain-specific sub-agents, each owning its own toolset and prompt instructions, because a flat tool list became unmanageable as more scientific domains were onboarded

- **Evidence**: Architectural description of an in-progress redesign, explicitly framed
  as "actively evolving" and a "proposed architecture" rather than a completed
  migration, motivated by cross-domain tool/schema ambiguity (e.g., "the study" meaning
  different things in toxicology vs. pharmacology data).
- **Confidence**: emerging (this is a forward-looking, partially-implemented design
  decision — the article is explicit that this is in progress, not settled production
  behavior)
- **Quote**: "To avoid one monolithic agent juggling overlapping tools and subtly different data contracts, we are actively evolving the Researcher capability into a hierarchy of domain‑specific sub‑agents. In this proposed architecture, each domain agent will own its own toolset (for example, toxicology RAG + tox metadata SQL, or pharmacology RAG + assay‑level SQL) along with tailored prompt instructions that encode how that domain’s data model works, which tables or indices are authoritative, and how to interpret key concepts."
- **Our assessment**: This is a concrete example of "context-centric decomposition" —
  the design principle from `blog-anthropic-multi-agent-coordination-patterns.md`
  (Claim 13: "Divide work by what context each agent needs rather than by what type of
  work it does") — arrived at independently by a production team facing the specific
  symptom of overlapping domain vocabulary ("studies," "findings," "assays" meaning
  different things per domain). Flag for the guide that this is a documented *in-
  progress* migration, not a completed and measured architecture; cite accordingly.

### Claim 6: The RAG retrieval pipeline uses a fixed 0.7/0.3 weighting between semantic vector search and keyword search, determined through experimentation, followed by a cross-encoder reranker that narrows ~20 candidate chunks to the top 7

- **Evidence**: Specific, named pipeline parameters for the hybrid retriever: keyword
  extraction, metadata filter generation, 5-way query expansion, weighted hybrid search
  (0.7 semantic / 0.3 keyword) retrieving k≈20 chunks, then `bge-reranker-large`
  reranking to k=7 chunks used as final context.
- **Confidence**: settled (concrete, specific implementation parameters presented as
  the production configuration, not illustrative)
- **Quote**: "A weight of 0.7 is given to the semantic search results and 0.3 to the keyword search results to balance contextual understanding and precise term matching. This weighting was determined through experimentation to optimize retrieval effectiveness for our data."
- **Our assessment**: This is a concrete, reusable artifact for the guide — an actual
  production weighting ratio and a named reranker model, not a generic "use hybrid
  search" recommendation. The explicit caveat ("for our data") is important: this
  ratio was tuned to Bayer's specific corpus and query distribution and should be
  presented as a starting point to tune from, not a universal constant.

### Claim 7: An earlier version of the Text-to-SQL pipeline included an LLM review step to catch invalid generated queries, but this step was removed because the reviewing LLM sometimes incorrectly flagged valid queries as erroneous, hurting efficiency without improving accuracy

- **Evidence**: Direct practitioner account of a design decision that was tried and
  then reverted, with the stated reason (false positives from the review step) and the
  stated outcome (efficiency loss without accuracy gain).
- **Confidence**: emerging (single-system practitioner account of a design reversal;
  no quantified false-positive rate given)
- **Quote**: "Notably, an earlier iteration of this process included an LLM review step for generated SQL queries; however, this step was later removed as it was found that the reviewing LLM sometimes incorrectly flagged valid queries as erroneous, hindering efficiency without a commensurate gain in accuracy."
- **Our assessment**: This is a first-class failure report embedded inside a broader
  success narrative and deserves separate attention in the guide. It is the mirror
  image of the "early victory problem" described in
  `blog-anthropic-multi-agent-coordination-patterns.md` (Claim 2: "The verifier is only
  as good as its criteria." — vague criteria cause a verifier to rubber-stamp bad
  output). Here, the failure runs the other direction: an LLM verifier without a
  crisp, formal correctness definition ("is this SQL valid?") over-rejected *good*
  output. PRINCE's actual solution for SQL correctness is not an LLM judge at all —
  it is a deterministic execution-based check (attempt the query against Athena, feed
  execution errors back to the same model for self-correction, retry up to 3 times;
  see Claim 12). The lesson for the guide: for tasks with an objective, mechanically-
  checkable correctness definition (does the query execute; does it return a result),
  prefer a deterministic verifier over an LLM verifier — reserve LLM-based verification
  for criteria that genuinely require judgment.

### Claim 8: The system implements three distinct, complementary reflection loops — process reflection (is the workflow on the right trajectory), data reflection (is the retrieved evidence sufficient), and draft reflection (is the generated output complete) — each catching a different failure category

- **Evidence**: Explicit architectural taxonomy given after describing all three
  mechanisms (Think & Plan, Reflection Agent, optional Writer review loop), naming
  what each one catches.
- **Confidence**: settled (this is the article's own explicit closing taxonomy for a
  set of mechanisms it has already described in full architectural detail)
- **Quote**: "This gives PRINCE three complementary reflection loops. Process reflection checks whether the workflow is on the right path and helps catch bad trajectory, wrong tool choice, or poor sequencing. Data reflection checks whether the gathered evidence is sufficient and helps catch thin evidence, missing context, or gaps in coverage. Draft reflection checks whether the generated output is complete and helps catch missing sections, incomplete tables, or synthesis gaps."
- **Our assessment**: This three-way taxonomy is more granular than the generic
  "generator/evaluator" split documented in `blog-anthropic-harness-long-running.md`
  and the "generator-verifier" pattern in
  `blog-anthropic-multi-agent-coordination-patterns.md`. Those sources treat reflection
  as a single evaluation checkpoint; PRINCE decomposes it into three checkpoints with
  different objects of evaluation (trajectory, evidence, output). This is a genuinely
  new and more precise vocabulary for the guide's treatment of reflection/verification
  patterns: not "add a verifier" but "identify which of trajectory, evidence, or
  output-completeness you are actually checking, and place a dedicated checkpoint for
  each."

### Claim 9: The Reflection Agent (data-sufficiency checkpoint) receives only the original user question and the collected evidence — not the full workflow history — and produces targeted follow-up questions when evidence is judged insufficient, which route back into Think & Plan for further retrieval

- **Evidence**: Description of the Reflection Agent's inputs and its output-driven
  feedback loop back to Think & Plan.
- **Confidence**: emerging (architectural description of a working production
  mechanism; no measurement of how often insufficiency is correctly detected)
- **Quote**: "If the gathered information is deemed insufficient to provide a complete response, the Reflection Agent generates specific follow-up questions designed to acquire the necessary missing information. These follow-up questions are then handed back to the Think & Plan step, which initiates further retrieval steps to obtain more comprehensive results."
- **Our assessment**: This is a concrete instance of narrow, purpose-scoped context
  assignment per agent — the article later summarizes this directly: "the Reflection
  Agent receives the original question alongside collected evidence to assess gaps,
  not the full workflow history." This directly extends the per-agent context-scoping
  principle in Claim 2. The feedback mechanism (generate follow-up questions, not a
  raw pass/fail) is notable: the reflection step doesn't just gate the workflow, it
  actively directs the next retrieval action.

### Claim 10: The Writer Agent must ground every claim in supplied context with citations back to source chunks and study IDs as a non-negotiable rule, because verifiability is critical in a regulated environment, and all regulatory drafting outputs are explicitly scoped for expert human review rather than autonomous submission

- **Evidence**: Direct statement of the Writer Agent's operating constraints and an
  explicit disclaimer about human review of regulatory outputs.
- **Confidence**: settled (explicit, stated design constraint and organizational
  policy, not an inferred behavior)
- **Quote**: "It must ground every claim in the supplied context and attach accurate citations back to the underlying chunks and study IDs, since verifiability is critical in a regulated environment."
- **Our assessment**: This is the regulated-industry-specific instantiation of
  citation-grounding as a hard constraint rather than a nice-to-have — the guide
  should distinguish citations as a trust-building UX benefit (seen in Claim 11) from
  citations as a compliance requirement (unverifiable output cannot be used in this
  domain at all). The article separately and explicitly scopes regulatory
  drafting outputs to human approval: "Importantly, all outputs from these regulatory
  drafting workflows are intended for expert review; final submissions are authored
  and approved by qualified personnel." That disclaimer is a governance pattern worth
  citing directly: the system is scoped to draft, not to submit.

### Claim 11: PRINCE's citation UI links every generated sentence to a specific source document, page number, and the exact supporting quote, which the article says enhances credibility and simplifies human review

- **Evidence**: Direct description of the citation UI mechanism.
- **Confidence**: settled (description of a shipped UI feature)
- **Quote**: "Users can hover over any sentence in the generated response to see the corresponding citation, which provides a link to the PRINCE and to the source document, including the page number and the exact quote from the report used to support that part of the answer. This granular level of citation significantly enhances the credibility and trustworthiness of the system's output and simplifies the human review process."
- **Our assessment**: The specificity here (page number plus exact quote, not just a
  document link) is the actionable detail for the guide — it sets a concrete bar for
  what a citation should mean in a high-stakes system: not a pointer to the source
  document, but the exact sentence that supports the exact claim being made. This
  sets a higher standard than typical RAG citation implementations that link only to
  a retrieved chunk or document ID.

### Claim 12: Error recovery separates two kinds of state — LangGraph agent state persisted to Postgres via checkpointing, and broader application state (logs, intermediate steps, citations) in DynamoDB — enabling user-initiated retries to resume from the exact point of failure rather than restarting the whole workflow

- **Evidence**: Architectural description of the state persistence split and its
  purpose, plus the specific mechanics of a user-initiated retry.
- **Confidence**: settled (concrete, specific architecture description of a shipped
  mechanism)
- **Quote**: "When a user initiates a retry, the system leverages the persisted state to continue the workflow directly from the point of failure, intelligently skipping the steps that were successfully completed in the previous attempt. This significantly improves user experience and saves computational resources."
- **Our assessment**: This is a concrete, reusable harness engineering pattern: split
  workflow-engine state (checkpointed via the orchestration framework, here LangGraph
  → Postgres) from application-level bookkeeping state (DynamoDB), so that recovery
  can be scoped precisely to resuming the graph without needing to reconstruct
  everything else. This is more specific than a generic recommendation to persist
  state for retries — it names which state goes where and why.

### Claim 13: The evaluation strategy combines two distinct evaluation types — Dataset Evaluations (run against SME-curated reference answers whenever the core workflow, prompts, or models change, using RAGAS-style metrics: Faithfulness, Answer Relevancy, Context Relevancy, Answer Accuracy, Semantic Similarity) and Live Traffic Evaluations (run daily on real production queries without reference answers)

- **Evidence**: Direct description of both evaluation types, their trigger conditions,
  and the specific named metrics for dataset evaluation.
- **Confidence**: settled (concrete, named production evaluation methodology)
- **Quote**: "Dataset Evaluations: conducted whenever significant changes are made to the core workflow, prompts, or underlying models, these evaluations utilize curated datasets with pre-defined reference answers, meticulously prepared by subject matter experts and stored in Langfuse."
- **Our assessment**: The two-evaluation-type split (change-triggered dataset eval vs.
  continuous live-traffic eval) is a concrete, adoptable evaluation cadence pattern.
  The article states the complementary Live Traffic side separately: "Live Traffic
  Evaluations: performed daily as a batch job on real user queries from the live
  environment (without pre-defined reference answers), these evaluations provide
  valuable insights into real-world performance." It also flags a specific
  evaluation-design principle worth extracting on its own: "applying appropriate
  evaluation metrics at different workflow stages, analogous to a testing pyramid,
  is crucial in addition to evaluating overall end-to-end performance" — i.e.,
  evaluate each agent stage individually (retrieval quality, reflection accuracy,
  writer faithfulness), not only the final answer.

### Claim 14: A confidence-scored NER pipeline auto-applies high-confidence extracted metadata annotations directly to the production database while quarantining low-confidence extractions for mandatory human review, rather than either fully automating or fully manualizing metadata correction

- **Evidence**: Description of the data-quality remediation system built to fix
  incomplete/incorrect structured metadata accumulated from historical system
  migrations.
- **Confidence**: emerging (described as an actively-developed system with "promising
  results" against curated evaluation datasets, not yet fully integrated into
  production pipelines per the article's own wording)
- **Quote**: "Fields with a high confidence score will be automatically used to update the corresponding entries in Amazon Athena. Fields with lower confidence scores will be quarantined and flagged for human review and intervention, ensuring data accuracy while leveraging automation."
- **Our assessment**: This confidence-threshold-gated automation pattern (auto-apply
  above a threshold, route below it to a human queue) is a generically reusable
  human-in-the-loop design for any AI system that writes back to a system of record,
  not specific to NER or pharma metadata. It is a more specific instantiation of
  "human-in-the-loop" than the Writer Agent review loop (Claim 10) — here the human
  reviews only the subset the system itself flags as uncertain, rather than reviewing
  every output.

### Claim 15: The authors conclude that as model capabilities improve, harness components may shrink or be absorbed into native model behavior, but explicit control over context, workflow state, recovery, reflection, and verification remains essential specifically in regulated, trust-and-traceability-sensitive domains

- **Evidence**: The article's closing thesis statement, generalizing beyond the PRINCE
  case study to a broader claim about the future trajectory of harness engineering.
- **Confidence**: emerging (forward-looking practitioner opinion/prediction, not an
  empirical finding — explicitly framed as "may become thinner," a hedge)
- **Quote**: "As model capabilities improve, some parts of today's harness may become thinner or move into native model capabilities. But in enterprise research systems, especially where trust, traceability, and reviewability matter, explicit control over context, workflow state, recovery, reflection, and verification remains essential."
- **Our assessment**: This is a notable, nuanced position for the guide's own
  editorial stance on whether harnesses become unnecessary as models improve — the
  authors do not claim harnesses are permanent in all domains, only in
  regulated/high-trust domains. This directly parallels the trajectory documented in
  `blog-anthropic-harness-long-running.md` Claim 3 and related claims (harness
  components were progressively removed from Opus 4.5 to 4.6 as the model internalized
  what the harness used to enforce) — but PRINCE's authors argue that trajectory has a
  floor in regulated environments, where the harness's job (traceability, auditability)
  isn't a capability gap to be closed, it's a compliance requirement that persists
  regardless of model quality.

## Concrete Artifacts

### Hybrid RAG Retrieval Pipeline (verbatim steps, from source)

```
Source: "Building Reliable Agentic AI Systems," martinfowler.com, 16 June 2026
        Section: "Retrieval-Augmented Generation (RAG) for Unstructured Data"

1. Keyword Extraction: LLM extracts keywords relevant for keyword search
   (e.g., "piloerection", "ataxia", "eyes partially closed", "loose faeces")
2. Metadata Filter Generation: LLM generates a structured filter, e.g.
   eq(study_id, T123456-2), via few-shot prompting
3. Query Expansion: a smaller, faster model generates n=5 semantically
   similar query rewrites
4. Hybrid Retriever (per expanded query, run in parallel against OpenSearch):
   - Metadata filtering applied first (narrows search space from millions
     of vectors to tens/hundreds)
   - Weighted hybrid search: semantic vector similarity (kNN) weighted 0.7
     + keyword search weighted 0.3
   - Aggregation across all 5 parallel searches, deduped by highest score,
     yielding ~20 candidate chunks
5. Reranking: cross-encoder model (bge-reranker-large) scores the ~20
   chunks against the original question, selects top k=7
6. Final LLM Prompt Generation: top-7 chunks + original question form the
   final prompt
7. Response Generation with Citation: reasoning model generates the answer
   with citations back to specific source chunks
8. Monitoring: entire pipeline traced in Langfuse
```

### Text-to-SQL Pipeline (verbatim steps, from source)

```
Source: "Building Reliable Agentic AI Systems," martinfowler.com, 16 June 2026
        Section: "Text-to-SQL for Structured Data"

1. Query Analysis and Intent Recognition
2. Schema Understanding and Relevant Schema Selection — only the schema
   components relevant to the query are dynamically injected, not the
   full database schema
3. Dynamic Few-Shot Prompting — hand-picked query→SQL (Athena dialect)
   examples retrieved via vector similarity from a separate "semantic
   layer" collection, continuously expanded as new challenges are found
4. SQL Query Generation and Validation — model generates SQL; validated
   to allow only SELECT (DELETE/INSERT/UPDATE explicitly blocked);
   essential columns (study ID, study title) always forced into SELECT
   [Note: an earlier LLM-review step for generated SQL was REMOVED —
    it incorrectly flagged valid queries as erroneous, hurting efficiency
    without improving accuracy]
5. Query Execution and Result Limiting — executed against Athena, capped
   at 50 records per query
6. Error Handling and Iteration — on failure, DB error message + query +
   context fed back to the same model for correction; retried up to 3
   times before the tool reports failure
```

### Reflection Loop Taxonomy (verbatim, from source)

```
Source: "Building Reliable Agentic AI Systems," martinfowler.com, 16 June 2026
        Section: "The Writer Agent: Answer Synthesis and Formatting"

Process reflection (Think & Plan)     → catches bad trajectory, wrong tool
                                          choice, poor sequencing
Data reflection (Reflection Agent)    → catches thin evidence, missing
                                          context, gaps in coverage
Draft reflection (Writer review loop) → catches missing sections,
                                          incomplete tables, synthesis gaps
```

### State Persistence and Recovery Architecture

```
Source: "Building Reliable Agentic AI Systems," martinfowler.com, 16 June 2026
        Section: "Engineering for Resilience: Error Handling and Recovery"

LangGraph Agent State  → persisted to Postgres via LangGraph checkpointer
                          (per-node, after each logical workflow step)
Application state       → persisted to DynamoDB
                          (logs, intermediate steps, citations)

Recovery mechanisms:
  - Built-in automatic retries at both the individual LLM-call level and
    the logical node level
  - User-initiated retry resumes from persisted checkpoint, skipping
    already-completed steps
  - LLM fallback: on repeated failure of primary provider/model, falls
    back automatically to an alternative LLM from a different provider
  - Agents are given the context of errors so they can "chart a different
    trajectory or alternative plan of action"
```

### Evaluation Metrics (Dataset Evaluation, verbatim list from source)

```
Source: "Building Reliable Agentic AI Systems," martinfowler.com, 16 June 2026
        Section: "Evaluation"

- Faithfulness (degree to which the answer is supported by context)
- Answer Relevancy (how well the answer addresses the query)
- Context Relevancy (relevance of retrieved chunks)
- Answer Accuracy (comparison to ground truth)
- Semantic Similarity with Reference (semantic similarity to reference answer)

Framework: RAGAS, orchestrated via Langfuse
Cadence: Dataset eval on significant workflow/prompt/model changes;
         Live traffic eval daily (no reference answers)
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-carta-healthcare-context-engineering.md` (Claim 1, Claim 2):
    Both sources independently converge on "context assembly/curation, not prompt
    wording, is the primary accuracy lever" and both scope context narrowly per
    unit of work rather than passing one global context. Carta scopes per extracted
    data point within a single extraction step; PRINCE scopes per pipeline *stage*
    across a multi-agent workflow (Claim 2 above). Two regulated-adjacent domains
    (healthcare data abstraction, pharma preclinical research) independently arrived
    at the same architectural principle.
  - `blog-anthropic-multi-agent-coordination-patterns.md` (Claim 13, "context-centric
    decomposition"): PRINCE's in-progress migration to domain-specific Researcher
    sub-agents (Claim 5 above) is a real-world instance of exactly this principle,
    arrived at independently and for a concrete, named reason (overlapping domain
    vocabulary across toxicology/pharmacology tools).
  - `blog-anthropic-harness-long-running.md` (Claim 1: models fail at self-evaluation
    and confidently praise mediocre work): PRINCE's decision to separate process
    reflection (Think & Plan), data reflection (Reflection Agent), and draft
    reflection (Writer review) into three distinct checkpoints (Claim 8 above) is
    consistent with harness-long-running's finding that self-critique inside a single
    agent is unreliable — PRINCE never asks one agent to both generate and judge its
    own trajectory, evidence, or output.

- **Extends**:
  - `blog-anthropic-multi-agent-coordination-patterns.md` (Claim 2, the "early victory
    problem" — vague verifier criteria cause false *acceptance*): PRINCE's removed
    SQL-review step (Claim 7 above) documents the inverse failure — an LLM verifier
    without a crisp formal definition of "valid SQL" produced false *rejections*
    instead. Together these two sources establish that LLM-based verification fails
    in both directions when criteria are not formal/explicit, and that PRINCE's fix
    (a deterministic execution-based check instead of an LLM judge) is a concrete
    alternative worth adding to the guide's verification-pattern guidance.
  - `blog-anthropic-harness-long-running.md` (the harness-shrinks-as-models-improve
    trajectory, e.g. Claim 3 and related): PRINCE's closing thesis (Claim 15 above)
    adds an explicit boundary condition to that trajectory — the authors argue harness
    thinning has a floor in regulated/high-trust domains, where traceability and
    auditability are compliance requirements rather than capability gaps.

- **Novel**:
  - The three-way reflection taxonomy (process / data / draft reflection, Claim 8) —
    no existing corpus note decomposes "reflection" or "verification" into three
    distinct objects of evaluation (trajectory vs. evidence vs. output). Existing
    corpus sources treat reflection/verification as a single generator↔evaluator
    checkpoint.
  - Concrete hybrid-retrieval tuning parameters (0.7/0.3 semantic/keyword weighting,
    k=20→k=7 rerank funnel, `bge-reranker-large`, Claim 6) — no existing corpus note
    provides a named, production-tuned hybrid search weighting.
  - The documented removal of an LLM SQL-review step due to false-positive rejections
    (Claim 7) — a genuinely new failure mode for the corpus (LLM verifier over-
    rejecting valid output), distinct from the more commonly documented failure mode
    of verifiers under-rejecting (rubber-stamping) bad output.
  - Confidence-threshold-gated write-back automation for data quality remediation
    (Claim 14) — a specific human-in-the-loop pattern (auto-apply above threshold,
    queue below threshold) not previously documented in the corpus in this form.
  - The explicit regulated-domain floor on harness thinning (Claim 15) — no existing
    corpus source argues that harness engineering's necessity is domain-conditional
    (shrinks with model capability in general use, persists in regulated/high-trust
    domains specifically) as directly as this closing thesis does.

## Guide Impact

- **Chapter on Context Engineering**: Add PRINCE's per-stage context assignment
  (Claim 2: distinct planning/retrieval/evidence/synthesis context per workflow stage)
  as a second concrete example alongside Carta Healthcare's per-query context scoping,
  to show the same principle applied at two different granularities (per-stage in a
  multi-agent pipeline vs. per-data-point in a single extraction step). Also add
  intent-clarification-as-context-assembly (Claim 3) as a named early-stage pattern:
  narrowing tool/domain scope before retrieval begins is itself a context engineering
  decision, not just a UX affordance.

- **Chapter on Harness Engineering / Verification Patterns**: Add the three-way
  reflection taxonomy (Claim 8: process / data / draft reflection) as a more precise
  replacement or complement for the generic "generator/evaluator" framing currently
  used. Recommend practitioners identify which of trajectory, evidence sufficiency,
  or output completeness they are checking, and place a dedicated checkpoint for each
  rather than one undifferentiated review step. Add the removed-SQL-review-step
  failure (Claim 7) as a concrete counterexample: for objectively checkable
  correctness (does the query execute), prefer a deterministic check over an LLM
  judge, and reserve LLM verification for genuinely judgment-based criteria.

- **Chapter on Production/Regulated-Industry Deployment**: Add the citation-as-
  compliance-requirement distinction (Claim 10, Claim 11): in regulated domains,
  citation grounding is a non-negotiable design constraint tied to verifiability
  requirements, not a trust-building UX feature — and cite PRINCE's citation
  granularity bar (page number + exact supporting quote per sentence) as a concrete
  standard. Add the explicit human-approval scoping for regulatory drafting outputs
  as a governance pattern: AI drafts, qualified humans approve and submit.

- **Chapter on Evaluation**: Add PRINCE's two-tier evaluation cadence (Claim 13:
  change-triggered dataset evaluation with RAGAS metrics vs. daily live-traffic
  evaluation without reference answers) as a concrete, adoptable pattern, along with
  the "testing pyramid" principle of evaluating each agent stage individually rather
  than only the end-to-end answer.

- **Chapter on the Future of Harness Engineering**: Add PRINCE's closing thesis
  (Claim 15) directly into any discussion of whether harnesses become unnecessary as
  models improve. This source provides an explicit counterpoint/refinement to the
  harness-shrinks-with-capability trajectory documented in
  `blog-anthropic-harness-long-running.md`: the shrinkage may have a floor in
  regulated, trust-and-traceability-sensitive domains.

## Extraction Notes

- The WebFetch tool returned only a lossy summary of this article on the first
  attempt (it compressed the whole piece into ~10 bullet points and did not preserve
  verbatim wording). To obtain quote-accurate text, the raw HTML was fetched directly
  via `curl` and converted to plain text locally, then read in full. All quotes in
  this note were copied from that locally-rendered full text, cross-checked against
  the surrounding paragraph structure of the original HTML.
- The article contains two embedded architecture diagrams (Figure 1: system context;
  Figure 2: research workflow; Figure 3: Text-to-SQL tool) whose visual content
  (boxes/arrows) could not be extracted as text — only their captions and the
  surrounding prose describing each component were available. The RAG pipeline
  diagram's step labels were recoverable from embedded CSS/layout text in the HTML
  and cross-checked against the prose walkthrough in the "Query-Time RAG Pipeline"
  section; both matched and are reflected in the Concrete Artifacts section above.
- The companion paper in *Frontiers in Artificial Intelligence* (referenced in the
  introduction as covering "product evolution and business impact") was explicitly
  out of scope for this article and was not fetched — a separate source submission
  for that paper may be warranted if it contains adoption/impact metrics not present
  here.
- No paywall or access restriction was encountered. The full article (~6,000 words)
  was read in its entirety, including the Acknowledgments and Disclaimer sections.
- Three separate Prospector triage comments were present on the issue with slightly
  different chapter mappings (all converging on context engineering and harness
  engineering as the core lenses, with varying chapter numbers). This note treats
  the underlying content claims as authoritative over any single comment's specific
  chapter numbering, per the guide's actual chapter structure at extraction time.
- Cross-reference claims were verified by re-reading the cited source notes directly
  before writing each citation: `blog-anthropic-carta-healthcare-context-engineering.md`
  (Claims 1, 2), `blog-anthropic-multi-agent-coordination-patterns.md` (Claims 2, 13),
  and `blog-anthropic-harness-long-running.md` (Claim 1 and the harness-thinning
  trajectory claims). No contradictions requiring a formal contradiction issue were
  found — the removed-SQL-review-step finding (Claim 7) extends rather than
  contradicts the "early victory problem" claim, since both describe the same root
  cause (verifier lacking formal criteria) producing opposite failure directions
  (false acceptance vs. false rejection), which is a complementary insight rather
  than a disagreement about what to recommend.
