---
source_url: https://claude.com/blog/carta-healthcare-clinical-abstractor
source_type: blog-post
title: "How Carta Healthcare Gets AI to Reason Like a Clinical Abstractor"
author: Anthropic (case study featuring Hannah Glaser and Matthew Mazzanti, Carta Healthcare)
date_published: 2026-04-08
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#206"
---

# How Carta Healthcare Gets AI to Reason Like a Clinical Abstractor

> Carta Healthcare's production case study demonstrating that per-data-point runtime
> context assembly — not prompt engineering — is the primary accuracy lever for
> structured clinical data extraction, achieving 98–99% inter-rater reliability at
> 22,000 surgical cases/year across 14 hospitals.

## Source Context

- **Type**: blog-post (Anthropic/Claude blog, April 2026; corporate case study with
  named practitioner quotes)
- **Author credibility**: Anthropic-published case study featuring Hannah Glaser
  (Applied AI Applications Manager, Carta Healthcare) and Matthew Mazzanti (Software
  Engineering Manager, Carta Healthcare). Marketing framing — hosted on claude.com,
  positions Claude favorably — but the technical substance comes from named engineers
  describing their production system. Metrics (98–99% inter-rater reliability,
  22,000 cases/year) are verifiable against known clinical registry standards.
  No code, no architecture diagrams, no ablation studies. Treat as a practitioner
  case study with medium depth: patterns are real, but claims require corroboration
  before strong guide recommendations.
- **Scope**: Covers Carta Healthcare's "Lighthouse" platform for clinical data
  abstraction, built on Claude via Amazon Bedrock. Addresses three areas: (1) why
  rules/NLP failed and LLMs succeeded, (2) the context-engineering architecture
  pattern, (3) the evaluation framework design, and (4) the human-in-the-loop and
  feedback-loop workflow. Does NOT provide code, API details, architecture diagrams,
  or ablation comparisons. Does NOT cover cost, latency, or specifics of the Bedrock
  integration.

## Extracted Claims

### Claim 1: Context construction at runtime is the primary production accuracy lever — not prompt wording

- **Evidence**: Direct practitioner assertion backed by 98–99% accuracy outcome.
  Matthew Mazzanti: "The hardest problems we solved weren't about building a perfect
  prompt, they were about context construction." The team's characterization of
  context as "the real work" aligns with their achieved metrics.
- **Confidence**: emerging (single company case study; practitioner assertion; no
  controlled ablation comparing context quality vs. prompt quality)
- **Quote**: "Integrating, organizing, and surfacing the right data at the right time
  is the real work. A perfectly written prompt with bad context gives bad answers.
  A straightforward prompt with the right context delivers the results you need."
  — Matthew Mazzanti, Software Engineering Manager, Carta Healthcare
- **Our assessment**: This is the load-bearing claim of the entire article. Mazzanti
  is describing a deliberate architectural finding from building a production system,
  not a theoretical preference. The implicit corollary is that time invested in
  prompt optimization is less valuable than time invested in context assembly.
  This directly challenges a common engineer instinct to iterate on prompt wording
  when accuracy plateaus. For the guide's Ch04, this is strong emerging evidence
  that context assembly deserves dedicated architectural treatment — not an
  afterthought to prompt design.

### Claim 2: Per-data-point runtime context scoping with temporal anchors is the concrete context engineering pattern for structured extraction

- **Evidence**: Concrete example from the article: for a question like "most recent
  glucose before procedure," the system injects the exact procedure start time into
  the per-question context window, scoping the extraction to readings before that
  timestamp and explicitly excluding post-procedure readings. Each extracted data
  point gets its own individually assembled context rather than a shared global one.
- **Confidence**: emerging (single implementation; no comparison to alternative
  context assembly strategies)
- **Quote**: Hannah Glaser: "If weight was assessed after the procedure, a skilled
  abstractor knows that doesn't count as a pre-procedure weight, and the system
  needs to know that too."
- **Our assessment**: This is the most architecturally specific claim in the article.
  The pattern — scope the context window to a single data point's requirements at
  query time, injecting the precise boundary condition (procedure start time) — is
  distinct from the common pattern of assembling one large context for the whole
  document. It is a pull-on-demand, query-scoped architecture rather than a
  load-everything-upfront architecture. This is high-value for Ch04 (context
  engineering) as a concrete named pattern: "per-query context scoping."

### Claim 3: Rules-based NLP fails on clinical data because the same finding appears in incompatible formats across hospitals

- **Evidence**: Hannah Glaser's explanation of the system's predecessor and why it
  failed: the same clinical finding appears as a structured field at one hospital and
  buried in free-text narrative at another. Pattern-matching systems cannot generalize
  across this structural inconsistency.
- **Confidence**: emerging (practitioner assertion; the cross-hospital inconsistency
  claim is plausible and consistent with known healthcare IT realities, but specific
  to Carta's deployment)
- **Quote**: "That's where Carta Healthcare started years ago with NLP, and it's
  exactly why we moved to LLMs." — Hannah Glaser
- **Our assessment**: This is the concrete failure mode that explains why LLMs
  replaced rules engines in this domain. The article doesn't just say "LLMs are
  better" — it names the specific failure surface: structural inconsistency across
  institutions. This generalizes beyond healthcare: any domain where the same
  semantic content appears in multiple incompatible formats is a candidate for the
  same LLM-over-NLP architectural shift. Useful for Ch02 (harness engineering) to
  motivate when LLMs are the right tool vs. simpler extractors.

### Claim 4: Clinical-grade structured extraction requires capabilities beyond pattern matching — temporal reasoning, conflicting evidence resolution, and ambiguity handling

- **Evidence**: Hannah Glaser's description of what a clinical abstractor does, used
  as the design spec for the AI system.
- **Confidence**: settled (description of well-understood domain requirements; the
  list of capabilities is not contested)
- **Quote**: "What an AI system needs to understand is what a trained clinical
  abstractor understands: how to read clinical language in context, weigh conflicting
  evidence across documents, apply temporal logic relative to specific procedure
  dates, and handle ambiguity." — Hannah Glaser
- **Our assessment**: This is a useful framing for the guide: use the domain expert's
  task description as the capability specification for the AI system. Glaser is not
  listing ML capabilities — she is listing what a skilled human does, and treating
  that as the design target. The implication for system design: before choosing a
  model or architecture, articulate the cognitive operations the domain task requires.
  If temporal reasoning and conflicting-evidence resolution appear in that list, a
  rules engine is a category mismatch.

### Claim 5: Granular evaluation that attributes failure to prompt, context, or retrieval is the correct architecture for debugging extraction pipelines

- **Evidence**: Matthew Mazzanti's description of their evaluation framework, cited
  as a specific design decision that enabled their velocity.
- **Confidence**: emerging (practitioner assertion backed by stated velocity outcomes;
  no controlled comparison against aggregate-only evaluation)
- **Quote**: "When something underperforms, you can trace it back to a specific
  prompt, a context issue, or a retrieval gap rather than staring at an aggregate
  score wondering what went wrong." — Matthew Mazzanti
- **Our assessment**: The three-axis attribution (prompt / context / retrieval) is
  the most actionable evaluation design insight in the article. It treats AI accuracy
  failures as having distinct root causes that require different fixes: a prompt
  failure requires prompt revision; a context failure requires context assembly
  changes; a retrieval failure requires retrieval pipeline changes. Aggregate accuracy
  scores conflate all three and cannot drive targeted remediation. This is
  independently useful for any structured extraction system, not just clinical data.

### Claim 6: Evaluation frameworks must be built early — retrofitting is more expensive than building forward

- **Evidence**: Matthew Mazzanti's direct recommendation, stated as a lesson from
  their build experience.
- **Confidence**: emerging (practitioner assertion; widely corroborated in principle
  by testing literature but not specifically measured here)
- **Quote**: "Build your evaluation framework early, make it granular, and design it
  to isolate variables. Skip this, and you'll spend more time debugging than
  building." — Matthew Mazzanti
- **Our assessment**: This is the evaluation design corollary to Claim 5. The warning
  ("skip this and you'll spend more time debugging than building") suggests Mazzanti
  is speaking from experience with teams that didn't do this. For the guide's Ch03,
  this is useful as a practitioner-level endorsement of evaluation-first development,
  specifically for AI extraction pipelines.

### Claim 7: Domain-expert feedback can replace data science translation in the prompt iteration loop — months → one week

- **Evidence**: Hannah Glaser's direct comparison of before/after iteration velocity,
  with a specific time-unit claim (months of engineering → one week).
- **Confidence**: emerging (single company claim; no external verification; the
  "months → one week" figure is plausible for moving from NLP retraining to prompt
  update, but the before/after comparison may not be fully controlled)
- **Quote**: "Our clinical abstractors regularly hand us long explanations of how a
  specific data point works in practice. Instead of spending weeks translating that
  into data science models and custom code, we use that feedback directly in the
  prompts. What used to take months of engineering and QA per registry now ships
  in a week." — Hannah Glaser
- **Our assessment**: This is the highest-value claim for Ch05 (team adoption). The
  mechanism — domain expert explains a rule in natural language, engineer translates
  directly into prompt text — eliminates the data science translation layer that was
  required for NLP retraining. The implications are structural: teams no longer need
  a data scientist to act as the intermediary between clinical judgment and system
  behavior. A product engineer who can write prompts can now implement domain expert
  feedback. This changes the team composition requirement for AI-based extraction
  systems. "Months → one week" should be treated as illustrative rather than exact,
  but the direction is clear and is consistent with the architectural shift described.

### Claim 8: Human-in-the-loop transparency — showing evidence and rationale per extracted data point — enables validation without blind acceptance

- **Evidence**: Product design description from the article; abstractor's direct
  characterization of the workflow.
- **Confidence**: emerging (design description; no metrics on validation accuracy or
  override rate)
- **Quote**: "Lighthouse doesn't replace my judgment. It enhances it."
  — Carta Healthcare clinical abstractor (unnamed)
- **Our assessment**: The article describes abstractors seeing supporting evidence
  and Claude's reasoning per extracted data point — not just the extracted value.
  This is a specific human-in-the-loop design choice: transparency per output rather
  than accuracy reporting in aggregate. It enables the abstractor to validate the
  reasoning, not just accept/reject the answer. For the guide's Ch09 (production AI
  systems) or Ch10 (human-AI collaboration), this is a concrete pattern: for
  high-stakes extraction, surface the evidence chain per decision, not just the
  decision. The abstractor quote frames this as augmentation ("enhances") rather
  than replacement — consistent with Anthropic's stated design philosophy but also
  with the practical reality that the system achieves 98-99% accuracy (not 100%),
  so human validation retains value.

### Claim 9: AI-assisted clinical abstraction achieves 98–99% inter-rater reliability at production scale

- **Evidence**: Carta Healthcare's stated outcome for the Lighthouse platform:
  22,000+ surgical cases/year across 14 hospitals at a single large health system.
  98–99% inter-rater reliability is the clinical registry accuracy standard.
- **Confidence**: emerging (self-reported; marketing context; no independent audit
  cited; inter-rater reliability measures agreement between human abstractors, so
  the AI is meeting the human-human benchmark)
- **Quote**: (implied throughout; not a single verbatim quote — the 98–99% figure
  is stated as achieved performance)
- **Our assessment**: The 98–99% figure is specific and uses a clinical industry
  standard metric (inter-rater reliability), which is harder to game than arbitrary
  accuracy measures. Meeting the human-human agreement standard is the correct
  target for an AI that is replacing human abstractors — not exceeding human accuracy
  on a held-out test set, but matching the rate at which two trained humans agree on
  the same case. Treat as credible but unverified; cite as "self-reported" in the
  guide. The scale (22,000 cases/year, 14 hospitals) is production-level and not
  a pilot.

### Claim 10: Clinical data abstraction currently consumes 11,000+ skilled-labor hours per year per registry at large health systems

- **Evidence**: Article's quantification of the manual process that Lighthouse
  automates: individual cases take 60 minutes (routine) to 5–6 hours (complex).
- **Confidence**: emerging (Carta's claim; plausible given known clinical labor
  costs but not independently cited)
- **Quote**: (implied in article framing; not a single verbatim quote)
- **Our assessment**: Useful for the guide as a framing for the economic stakes
  of AI-assisted extraction in high-cost domains. Clinical abstraction is a
  low-volume, high-cognitive-load task — the exact class of task where per-query
  context assembly is worth the engineering cost. The 60-min to 5-6-hour range
  signals high variance in task complexity, which also explains why a static NLP
  system fails: the hard cases (5-6 hours) are hard precisely because they require
  the contextual reasoning and ambiguity handling that NLP cannot provide.

## Concrete Artifacts

### Context Assembly Pattern (per-data-point with temporal anchor)

```
Per-question context assembly pattern (from Carta Healthcare's Lighthouse):

For extraction question: "Most recent glucose before procedure"
  → Context assembled AT QUERY TIME includes:
      - Patient's lab results (ordered by timestamp)
      - Exact procedure start time (injected as temporal anchor)
      - Instruction to scope to readings BEFORE procedure start time
      - Instruction to EXCLUDE readings after procedure start time

NOT: one global patient context passed to all extraction questions
BUT: individual context window assembled per data point, scoped to
     that question's temporal and clinical boundaries

Result: model applies correct boundary condition because the boundary
is explicitly part of the context, not inferred from general knowledge.
```
— Derived from Hannah Glaser's description; Mazzanti's "context construction" framing

### Evaluation Framework Structure (attributed to Mazzanti)

```
Root-cause attribution axes for extraction pipeline evaluation:
  1. PROMPT failure     → prompt revision required
  2. CONTEXT failure    → context assembly changes required
  3. RETRIEVAL failure  → retrieval pipeline changes required

Design requirement: each failure must be attributable to one axis.
Aggregate accuracy metrics cannot drive this attribution.

Build this early. "Skip this, and you'll spend more time debugging
than building." — Matthew Mazzanti
```

### Domain-Expert Feedback Loop (replacing data science translation)

```
Old workflow (NLP-based):
  Clinical abstractor identifies error
    → explains to data scientist
    → data scientist translates to labeled training data
    → model retraining (weeks to months)
    → QA cycle (weeks)
  Total: months per registry update

New workflow (LLM-based):
  Clinical abstractor explains data point rule in natural language
    → engineer translates explanation directly to prompt text
    → prompt updated in production
  Total: one week per registry update

Key structural change: data science translation layer is eliminated.
Domain expert language → prompt language (direct).
```
— Derived from Hannah Glaser quote; Carta Healthcare's stated experience

### Production Scale Metrics

```
Platform: Lighthouse (Carta Healthcare)
Model: Claude via Amazon Bedrock
Scale: 22,000+ surgical cases/year
Deployment: 14 hospitals (single large health system)
Accuracy: 98–99% inter-rater reliability (clinical registry standard)
Manual baseline: 11,000+ skilled-labor hours/year per registry
                 60 min/case (routine) to 5–6 hrs/case (complex)
Company: 125+ hospitals supported; 10x growth in 3 years (as of April 2026)
```

## Cross-References

- **Corroborates** `failure-thailandjohn-schema-refactor-context-collapse.md`: That
  source's central failure — context collapse leading to hallucination — is the
  mirror image of this source's central success. ThailandJohn's diagnosis: "the AI
  couldn't keep enough files in its context window to understand the full scope."
  Carta's architecture is the systematic solution: scope each query's context window
  to exactly what that query needs, not the full document. The shared underlying
  principle (from Mazzanti's formulation): "An AI agent's performance isn't
  determined solely by the model. It's determined by what the model is given to
  work with." Both sources converge on context quality as the primary accuracy
  variable from opposite sides — failure and success.

- **Corroborates** `blog-anthropic-harnessing-claude-intelligence.md` Claim 3
  (code-execution filtering lifted BrowseComp from 45.3% to 61.6%): That source
  demonstrates that letting Claude filter what enters its own context window improves
  accuracy by 16.3pp. Carta's per-data-point context scoping is the domain-specific
  instantiation of the same principle: don't route all available data through the
  context window; scope to what the specific query requires. Both validate
  "targeted context assembly for specific queries outperforms loading everything."

- **Extends** `research-wasnotwas-context-compaction.md`: Wasnotwas documents how
  harnesses manage context overflow after it happens (compaction mechanics and costs).
  This source describes the complementary upstream approach: proactively scope context
  per query so the full context ceiling is never approached. Per-data-point assembly
  means each query runs in a narrow, purpose-built context window, not an accumulating
  session window. These are complementary strategies: compaction manages overflow in
  long sessions; per-query scoping prevents overflow in extraction architectures.

- **Novel**:
  - **Per-data-point runtime context scoping with temporal anchors** as a named
    extraction architecture pattern. No other source in this corpus describes this
    specific approach: assembling a distinct context window per extracted data point,
    scoped to that point's temporal and clinical boundaries, rather than passing a
    global context to all extraction questions. This is the most reusable pattern
    in the article.
  - **Three-axis evaluation attribution** (prompt / context / retrieval) for AI
    extraction pipelines. The diagnostic framework — attributing each failure to one
    of three root causes — is a concrete design requirement not present in other
    corpus notes on evaluation.
  - **Domain-expert-to-prompt direct feedback loop**: eliminating the data science
    translation layer and allowing domain expert natural language explanations to
    flow directly into prompt text. Other sources describe prompt iteration but not
    this specific organizational pattern of who performs the iteration and how it
    bypasses traditional ML development cycles.
  - **LLM-over-NLP shift motivated by cross-institution structural inconsistency**:
    the specific failure mode (same finding = structured at hospital A, free-text at
    hospital B) is a concrete and generalizable reason for choosing LLMs over
    rules/NLP beyond the generic "LLMs are smarter." This is applicable to any
    multi-source extraction domain.

## Guide Impact

- **Chapter 04 (Context Engineering)**: Add "per-query context scoping" as a named
  pattern for structured extraction tasks. The pattern: for each extracted data
  point, assemble a distinct context window scoped to that point's specific
  requirements (temporal boundaries, relevant documents, applicable rules). Do NOT
  pass a global context to all queries. Cite Mazzanti's formulation as the canonical
  statement of the principle: "A perfectly written prompt with bad context gives
  bad answers. A straightforward prompt with the right context delivers the results
  you need." This source provides the clearest production evidence in the corpus
  for context engineering as a distinct, primary engineering discipline.

- **Chapter 02 (Harness Engineering)**: Add a decision criterion for LLM-vs-NLP
  selection: if the same semantic content appears in structurally incompatible formats
  across source documents (structured at source A, free-text at source B), rules/NLP
  is a category mismatch. LLMs are the correct choice for cross-institution or
  cross-format extraction. The runtime context assembly pipeline — injecting
  query-specific boundary conditions at extraction time — is a harness architecture
  pattern to document here.

- **Chapter 03 (Safety and Verification / Evaluation Frameworks)**: Add the three-axis
  evaluation design: build evaluation to attribute failures to prompt, context, or
  retrieval — not just aggregate accuracy. Cite Mazzanti's warning ("skip this and
  you'll spend more time debugging than building") as the motivating case. The
  attribute-to-root-cause pattern generalizes beyond clinical extraction to any AI
  pipeline with multiple contributing components.

- **Chapter 05 (Team Adoption / Human-AI Collaboration)**: Add the domain-expert
  feedback loop pattern: for domains where expertise is in natural language (clinical
  knowledge, legal reasoning, compliance rules), the feedback loop can bypass the
  data science layer entirely. Domain experts explain rules in prose; engineers
  translate directly to prompts. Cite the months-to-one-week velocity claim as the
  motivation. Also add the human-in-the-loop transparency pattern: for high-stakes
  extraction, surface the evidence chain per decision (not just aggregate accuracy)
  so validators can apply their judgment to the reasoning, not just the output.

## Extraction Notes

- Source is Anthropic-published marketing content (claude.com/blog). Marketing
  framing is present throughout — Claude is positioned as uniquely capable. Extract
  the structural patterns; do not cite capability claims as independent evidence.
- The article has no code, no architecture diagrams, and no ablation comparisons.
  Claims rest on practitioner authority and production metrics, not controlled
  experiments. All confidence ratings are "emerging" accordingly.
- The 98–99% inter-rater reliability figure uses a clinical domain standard (agreement
  between two trained human abstractors), which is the correct benchmark for this
  task. It is self-reported and unaudited; cite accordingly.
- Amazon Bedrock is mentioned as the integration layer but with no technical detail
  on API usage, latency, cost, or configuration.
- Three Prospector triage comments were present on this issue, with slightly differing
  chapter assignments. The most specific and detailed triage comment (third comment,
  2026-04-19) was used as the primary extraction guide. All three converge on Ch04
  (context engineering) as the primary chapter.
- The article was read in full via WebFetch. No sub-pages were linked from the article
  that required following. The article is a single-page case study.
