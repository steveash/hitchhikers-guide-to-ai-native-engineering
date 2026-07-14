---
source_url: https://claude.com/blog/working-at-the-frontier-how-hebbia-builds-ai-for-financial-diligence-that-cant-miss-a-detail
source_type: blog-post
title: "Working at the frontier: How Hebbia builds AI for financial diligence that can't miss a detail"
author: Anthropic (case study featuring Divya Mehta, Founding Product Manager, and Adithya Ramanathan, Applied AI Research Team Lead, Hebbia)
date_published: 2026-07-13
date_extracted: 2026-07-14
last_checked: 2026-07-14
status: current
confidence_overall: emerging
issue: "#1849"
---

# Working at the frontier: How Hebbia builds AI for financial diligence that can't miss a detail

> Production case study showing how Hebbia evaluates every new Claude model against a
> finance-specific benchmark before deployment, measures a ~20% relative accuracy gain
> from Claude Fable 5 on multi-document question-answering with citations, and is moving
> from single-model-run analysis toward Claude Agent SDK-composed, per-step-checked
> financial workflows (covenant extraction, credit analysis, pitch-deck generation).

## Source Context

- **Type**: blog-post (Anthropic/Claude blog, published July 13, 2026; corporate case
  study with two named practitioner sources and a specific benchmark metric)
- **Author credibility**: Anthropic-published case study featuring Divya Mehta (founding
  product manager, Hebbia) and Adithya Ramanathan (leads Hebbia's applied AI research).
  Hebbia is described as serving "more than a third of the top 50 asset managers along
  with tier-1 investment banks and law firms" — a verifiable customer-scale claim in
  principle, though not independently audited here. Marketing framing is present
  throughout (hosted on claude.com, positions Claude Fable 5 favorably), but the
  benchmarking methodology and named quotes come from practitioners describing a
  production evaluation process. The "20% relative gain" figure is self-reported by
  Hebbia and measured against Hebbia's own internal finance benchmark, not an
  independently reproducible public eval. Treat as a practitioner case study: real
  workflow and evaluation patterns, single-company metric.
- **Scope**: Covers Hebbia's model-evaluation process for new Claude releases, the
  specific capability gains attributed to Claude Fable 5 (multi-part query handling,
  citation grounding), two concrete production use cases (credit/covenant analysis and
  investment pitch-deck generation via Hebbia's "Matrix" product), and Hebbia's forward
  plan to adopt the Claude Agent SDK to decompose financial workflows into smaller,
  checked steps. Does NOT provide the benchmark's question set, scoring methodology,
  sample size, code, or architecture diagrams. Does NOT cover cost, latency, or
  deployment infrastructure.

## Extracted Claims

### Claim 1: Hebbia runs every new Claude model through a finance-specific internal benchmark, head-to-head against the model it would replace, before deploying it

- **Evidence**: Described as Hebbia's standing evaluation practice, framed as the
  mechanism by which new model releases are qualified for production use.
- **Confidence**: emerging (practitioner-described process; single company; no published
  benchmark question set or scoring methodology)
- **Quote**: "running every new model through Hebbia's finance-specific benchmark, head
  to head against the model it would replace"
- **Our assessment**: This is a concrete instantiation of pre-deployment model
  qualification for a regulated, high-stakes domain: a standing internal benchmark, run
  against every new release, compared directly to the incumbent model rather than to an
  absolute score. The head-to-head framing (new model vs. model it replaces) is a
  practical evaluation design choice — it directly answers "should we upgrade?" rather
  than "is this model good?" This corroborates the evaluation-first discipline documented
  in `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 8, from a different
  financial-services company.

### Claim 2: Claude Fable 5 posted approximately a 20% relative accuracy gain over financial documents on Hebbia's question-answering-and-citation test, the largest gain the team had seen from any new model

- **Evidence**: A specific benchmark result stated as a measured outcome of the internal
  finance benchmark, on a named test (question-answering and citation).
- **Confidence**: emerging (self-reported single metric; no confidence interval, sample
  size, or question set published; single company, single benchmark)
- **Quote**: "On the question-answering and citation test, it posted about a 20%
  relative gain in accuracy over financial documents, the best he had seen from any new
  model."
- **Our assessment**: This is the article's headline metric. "Relative gain" and
  "question-answering and citation test" narrow the claim's scope considerably: it is
  not a general capability claim but a specific measurement on one internal eval,
  reported by one practitioner as personally the best gain he'd observed. Useful as a
  directional data point for model-selection discussions in finance-document QA, but the
  guide should not present "20%" as a portable, domain-general number — it is tied to
  Hebbia's specific benchmark and document types.

### Claim 3: Claude Fable 5 improved on earlier models' tendency to drop parts of a multi-part query mid-analysis, instead answering and citing every sub-question

- **Evidence**: Direct comparison of Fable 5's behavior on multi-part requests against
  the failure mode of prior model versions (losing track of sub-questions partway
  through a complex query).
- **Confidence**: emerging (practitioner observation from production/benchmark use; no
  quantified drop-rate for prior models given)
- **Quote**: "it kept every part of a multi-part request at once, answering all of them
  and citing each answer back to its source"
- **Our assessment**: This describes the same class of failure Ganesh names in
  `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 1 — "quietly drop[ping] a
  constraint by step five" — but Hebbia's framing is about multi-part *queries* (losing
  a sub-question) rather than Kepler's multi-*step* constraint-dropping during a
  pipeline. Both are instances of the same underlying risk: long-horizon or
  multi-clause tasks where an LLM silently omits part of the request instead of
  flagging incompleteness. Two independent financial-services practitioners
  identifying variants of this failure mode as the thing that improved most in newer
  models is a meaningful corroboration point for the guide.

### Claim 4: Hebbia's "Matrix" product grounds each answer in its source document and displays each answer in its own cell on a grid, giving analysts transparency, traceability, and steerability over the analysis

- **Evidence**: Direct architectural/product description of how Matrix structures
  multi-document analysis output.
- **Confidence**: emerging (product description from a practitioner case study; no
  independent verification of the grounding mechanism's reliability)
- **Quote**: "Each answer lands in its own cell on a grid in Hebbia's Matrix, enabling
  full transparency, traceability, and steerability."
- **Quote**: "grounds each claim in the source rather than inferring it"
- **Our assessment**: The cell-per-answer grid structure is a UI-level implementation of
  citation grounding that makes verification a one-click action for the analyst (each
  cell can presumably be traced back to its source document) rather than a narrative
  claim buried in prose. This is a lighter-weight, UI-driven verifiability pattern
  compared to Kepler's architectural deterministic-execution-layer approach
  (`blog-anthropic-kepler-verifiable-ai-financial.md` Claim 3) — Hebbia keeps Claude in
  the answer-generation path but constrains and exposes its grounding at the UI level,
  rather than routing final numbers through a separate deterministic layer.

### Claim 5: Hebbia's meta-prompting layer turns analysts' plain-language requests into prompts that Claude then executes as analysis steps across hundreds of documents

- **Evidence**: Direct description of the request-to-analysis pipeline mechanism.
- **Confidence**: emerging (practitioner/product description; mechanism named but not
  detailed — no example prompts or meta-prompt templates shown)
- **Quote**: "Hebbia's meta-prompting turns plain-language requests into prompts, and
  then Claude runs each step of the analysis across hundreds of documents."
- **Our assessment**: "Meta-prompting" here names the layer that translates an analyst's
  natural-language ask into the structured prompt(s) Claude actually executes — a
  harness component sitting between user intent and model input. The article does not
  show the meta-prompt templates or explain how ambiguity in the analyst's request is
  resolved, so this claim documents that the layer exists and its stated purpose, not
  its internal design.

### Claim 6: With Claude Fable 5, Hebbia moved beyond covenant extraction to multi-step covenant analysis — comparing extracted covenants against live monitoring data and flagging risk — work previously requiring external specialist teams

- **Evidence**: Direct description of the credit-analysis use case, contrasting what
  the platform could do before (extraction) with what it can now do (multi-step analysis
  on top of the extraction).
- **Confidence**: emerging (practitioner description of a production capability
  expansion; no before/after accuracy or time metric given for this specific workflow)
- **Quote**: "With Claude Fable 5, Hebbia is reaching for the rest of the job: the
  multi-step analysis on top of those covenants, comparing them against live monitoring
  data, flagging risks"
- **Our assessment**: This is a capability-tier claim rather than a metric: the model
  upgrade is credited with expanding the scope of automatable work (from "extract the
  covenant" to "extract, monitor, and flag") rather than just making the existing
  extraction step faster or more accurate. The "previously required external specialist
  teams" framing (implied by the credit-analysis context) is the strongest economic
  claim in this section, but no cost or headcount figure is given, so it should be
  treated as directional.

### Claim 7: Hebbia's Matrix product compresses investment-pitch-deck production — previously 2-3 days of junior banker work — into a few minutes by running data-gathering, analysis, deck-building, and financial modeling as deterministic agentic steps

- **Evidence**: Direct before/after description of the pitch-deck workflow, naming the
  prior manual timeline and the new automated pipeline.
- **Confidence**: emerging (practitioner-reported time comparison; self-reported, no
  controlled measurement of the "2-3 days" baseline)
- **Quote**: "Hebbia has since codified the whole job into a Matrix that gathers the data
  across sources in a set of deterministic agentic steps, does the analysis, and builds
  the final deck, financial model, and internal research in a couple of minutes"
- **Our assessment**: "Deterministic agentic steps" is a notable phrase — Hebbia frames
  the pipeline as agentic (multi-step, tool-using) but deterministic in its step
  sequence, which is a middle ground between a single free-form model run and Kepler's
  strict reasoning/execution separation. The 2-3-days-to-minutes compression is the
  article's most dramatic time-savings claim; it should be read as a self-reported
  practitioner estimate of junior-banker task time, not a controlled study.

### Claim 8: Hebbia is adopting the Claude Agent SDK to compose financial workflows as smaller, repeatable, checked steps instead of running them as a single model call

- **Evidence**: Stated as Hebbia's forward-looking architectural direction, framed
  around firm control over which documents feed each step.
- **Confidence**: emerging (forward-looking statement of intent/early adoption; not yet
  demonstrated with production metrics in this article)
- **Quote**: "Hebbia is adopting the Claude Agent SDK to compose these jobs as smaller,
  repeatable, checked steps rather than a single model run."
- **Our assessment**: This is a direct architectural corroboration of the
  decompose-into-checked-steps pattern that Kepler independently arrived at
  (`blog-anthropic-kepler-verifiable-ai-financial.md` Claim 3, Claim 6): both companies,
  working in regulated financial analysis, converge on breaking a single large model
  task into smaller, individually verifiable/repeatable steps rather than trusting one
  long model run. Hebbia's version is Agent-SDK-based rather than Kepler's custom
  deterministic-layer architecture, so this is a second, differently-implemented data
  point for the same design principle — worth flagging to the guide as a
  cross-vendor-tooling convergence, not just a shared philosophy.

### Claim 9: The market's questions about AI in finance have shifted from defensive concerns about hallucination and correctness to workflow-automation questions

- **Evidence**: A before/after characterization of the tenor of customer conversations,
  attributed to the article's closing framing.
- **Confidence**: anecdotal (single practitioner/article characterization of customer
  sentiment shift over roughly two to three years; no survey data)
- **Quote**: "Two or three years ago the questions were defensive, about hallucinations
  and whether the math was right."
- **Our assessment**: This is a sentiment-shift claim, not a capability claim — it says
  customers' framing of the risk has changed, not that hallucination risk itself has
  been eliminated. It's useful context for why Hebbia's evaluation and grounding
  investments (Claims 1, 2, 4) matter commercially: the "is the math right" question
  had to be answered credibly before customers would engage with "how do I automate
  more of my workflow" questions. Should be read as narrative framing rather than
  independently verified market research.

### Claim 10: Adithya Ramanathan (leads Hebbia's applied AI research) frames the value of Claude's finance work as coming specifically from connecting it to the right data and ecosystem, not from the model alone

- **Evidence**: Named quote from Hebbia's applied AI research lead.
- **Confidence**: anecdotal (single named quote; practitioner opinion, not a measured
  claim)
- **Quote**: "When you're connecting it to the right data and putting it in the right
  ecosystem, that's when you get the alpha that finance professionals actually chase."
  — Adithya Ramanathan, who leads Hebbia's applied AI research
- **Our assessment**: This echoes the harness-over-model-alone framing common across the
  corpus's regulated-industry sources (e.g., Kepler's "the model can't be the whole
  system," `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 3) — Ramanathan's
  framing is data/ecosystem-centric rather than architecture-centric, but the underlying
  claim is the same: model quality alone does not produce the finance-specific value; the
  surrounding data connections and system design do. That this comes from the applied AI
  research lead — the person closest to the models themselves — makes the "it's not the
  model alone" framing more notable, not less.

### Claim 11: Divya Mehta (Hebbia's founding product manager) frames Hebbia's customer accuracy bar as extremely high and self-imposed by customer expectations in financial diligence

- **Evidence**: Named quote from Hebbia's founding product manager, in the context of
  describing the stakes customers hold Hebbia to.
- **Confidence**: anecdotal (single named quote; practitioner characterization)
- **Quote**: "The bar is extremely high, and our customers hold us to that extremely
  high bar—and rightfully so." — Divya Mehta, founding product manager, Hebbia
- **Our assessment**: This is framing/motivation context for Claim 1 (the standing
  finance benchmark) rather than a new technical claim — it explains *why* Hebbia
  maintains a head-to-head internal benchmark for every model release: the accuracy bar
  in financial diligence is customer-enforced, not just an internal engineering
  preference. Coming from the founding product manager, it frames the bar as a
  product/customer commitment rather than a purely engineering-internal standard.

## Concrete Artifacts

### Hebbia Model Evaluation & Deployment Process (from article)

```
Source: https://claude.com/blog/working-at-the-frontier-how-hebbia-builds-ai-for-financial-diligence-that-cant-miss-a-detail

EVALUATION PRACTICE:
  "running every new model through Hebbia's finance-specific benchmark, head
  to head against the model it would replace"

MEASURED RESULT (Claude Fable 5):
  Test: question-answering and citation test
  Result: "about a 20% relative gain in accuracy over financial documents,
           the best he had seen from any new model"

CAPABILITY IMPROVEMENT OBSERVED:
  Multi-part query handling: "it kept every part of a multi-part request at
  once, answering all of them and citing each answer back to its source"

FORWARD ARCHITECTURE PLAN:
  "Hebbia is adopting the Claude Agent SDK to compose these jobs as smaller,
  repeatable, checked steps rather than a single model run."
```

### Hebbia Production Use Cases (from article)

```
Source: https://claude.com/blog/working-at-the-frontier-how-hebbia-builds-ai-for-financial-diligence-that-cant-miss-a-detail

CREDIT / COVENANT ANALYSIS:
  Before: covenant extraction from unstructured legal documents
  Now (Claude Fable 5): "the multi-step analysis on top of those covenants,
    comparing them against live monitoring data, flagging risks"
  Previously required: external specialist teams (implied by article framing)

INVESTMENT PITCH DECK GENERATION (Hebbia "Matrix"):
  Before: 2-3 days of junior-banker work
  Now: "gathers the data across sources in a set of deterministic agentic
    steps, does the analysis, and builds the final deck, financial model,
    and internal research in a couple of minutes"

ANSWER GROUNDING (Matrix product UI):
  "Each answer lands in its own cell on a grid in Hebbia's Matrix, enabling
  full transparency, traceability, and steerability."
  "grounds each claim in the source rather than inferring it"

REQUEST PIPELINE:
  "Hebbia's meta-prompting turns plain-language requests into prompts, and
  then Claude runs each step of the analysis across hundreds of documents."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 8 (automated evaluation
    pipelines testing every model upgrade against known-correct answers, benchmarked
    within hours of release): Hebbia's practice of running every new Claude model
    through a finance-specific benchmark head-to-head against the incumbent model
    (Claim 1 here) is an independent second data point for the same evaluation-first
    discipline in financial services, from a different company.
  - `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 1 ("Other models would
    start strong and then quietly drop a constraint by step five"): Hebbia's
    observation that earlier models lost track of parts of multi-part queries while
    Claude Fable 5 "kept every part of a multi-part request at once" (Claim 3 here) is
    a variant of the same long-horizon-task failure mode — omission of part of a
    complex request — independently identified by a second financial-services
    practitioner.
  - `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 3 and Claim 6 (Claude
    restricted to interpretation/planning within a pipeline; idempotent, modular skill
    design): Hebbia's stated Agent SDK adoption to "compose these jobs as smaller,
    repeatable, checked steps rather than a single model run" (Claim 8 here) is a
    second, differently-implemented instance of the same decompose-into-checked-steps
    architectural principle in regulated financial AI.
  - `blog-anthropic-fong-finance-narrative.md` Claim 3 (Claude validating that
    numbers/claims reconcile to a single source of truth): Hebbia's Matrix grounding
    each answer "in the source rather than inferring it" (Claim 4 here) is the
    external-customer-facing-product version of the same grounding-to-source principle
    Fong describes for internal board-deck consistency checking — different products
    (customer SaaS vs. internal Cowork usage), same underlying verification discipline.

- **Contradicts**: None identified. No claim in this source materially opposes an
  existing source note.

- **Extends**:
  - `blog-anthropic-kepler-verifiable-ai-financial.md`: Kepler documents an
    architectural trust guarantee (deterministic execution layer structurally prevents
    Claude from producing final auditable numbers). Hebbia's Matrix instead keeps
    Claude in the answer-generation path but exposes grounding at the UI level
    (per-cell source citation) rather than routing final numbers through a separate
    deterministic layer (Claim 4 here). Together the two sources show two different
    verifiability architectures for the same regulated-finance problem: architectural
    separation (Kepler) vs. UI-exposed citation grounding (Hebbia).
  - `blog-anthropic-fong-finance-narrative.md`: Fong documents internal
    (Anthropic-employee) use of Claude for finance narrative work; this source
    documents a B2B SaaS vendor (Hebbia) building customer-facing financial-diligence
    tooling on Claude. Together they cover both the "Claude as employee tool" and
    "Claude embedded in a vertical SaaS product" ends of finance AI adoption.

- **Novel**:
  - **Head-to-head new-model-vs-incumbent-model benchmarking as a named deployment
    gate**: Not previously documented in this specific "new model vs. model it
    replaces" framing in the corpus's finance sources.
  - **"Deterministic agentic steps" as a stated pipeline design phrase**: Hebbia's own
    framing for the Matrix pitch-deck pipeline (agentic but with a deterministic step
    sequence) is a specific phrase not seen elsewhere in the corpus.
  - **Per-cell grounding in a spreadsheet-like grid UI as a verifiability pattern**:
    Distinct from Kepler's architectural deterministic layer — this is a UI-level
    verifiability implementation not previously documented.
  - **Customer sentiment shift from "is the math right" to "automate my workflow"
    framing (Claim 9)**: A narrative data point about how customer risk perception in
    finance AI has shifted over roughly two to three years, not previously documented
    in the corpus.

## Guide Impact

- **Chapter 03 (Safety and Verification)**: Add Hebbia's per-cell source-grounding
  pattern (Claim 4) as a second, lighter-weight verifiability architecture alongside
  Kepler's deterministic-execution-layer pattern (already recommended via
  `blog-anthropic-kepler-verifiable-ai-financial.md`). Frame as a spectrum: full
  architectural separation of reasoning from computation (Kepler) vs. keeping the model
  in the output path but exposing per-answer citations for one-click verification
  (Hebbia). Practitioners should choose based on how auditable the specific downstream
  number needs to be.

- **Chapter 02 (Harness Engineering)**: Add Hebbia's Agent SDK adoption for
  "smaller, repeatable, checked steps" (Claim 8) as a second, cross-vendor-tooling data
  point for the decompose-into-checked-steps principle already documented from Kepler's
  custom architecture. This strengthens the case that the principle (not just Kepler's
  specific implementation) generalizes across companies solving similar regulated-finance
  problems.

- **Chapter 06 (Evaluation & Model Selection)** (or wherever the guide covers
  pre-deployment model qualification): Add Hebbia's head-to-head internal
  finance-benchmark practice (Claim 1) — new model vs. incumbent model, not new model
  vs. absolute score — as a named evaluation-gate pattern. Cite the 20% relative-gain
  result (Claim 2) as an example metric, with the explicit caveat that it is
  self-reported, single-benchmark, and not a portable number.

- **Chapter 04 (Context Engineering)**: Add Hebbia's "meta-prompting" layer (Claim 5) —
  translating plain-language analyst requests into the structured prompts Claude
  executes — as a named example of a request-translation harness component, alongside
  Kepler's "content engineering" vocabulary (`blog-anthropic-kepler-verifiable-ai-financial.md`
  Claim 4). Note that the article does not expose the meta-prompt templates, so this
  should be cited as evidence the layer exists and its purpose, not as a design
  template.

## Extraction Notes

- Full-text reproduction of the article was not obtainable via WebFetch (the tool
  returned a synthesized summary rather than the raw page text on the first pass).
  All verbatim quotes in this note were obtained via targeted follow-up WebFetch passes
  asking specifically for short (sentence-or-less) verbatim fragments on named topics,
  and cross-checked for internal consistency across two separate passes (job titles,
  the 20% metric, and the "deterministic agentic steps" phrase were each confirmed in
  more than one pass).
- The article does not publish its finance-specific benchmark's question set, sample
  size, or scoring methodology — the 20% relative-gain figure (Claim 2) should be
  treated as a self-reported single metric, not an independently reproducible result.
- No specific document-count or page-count figures beyond "thousands of dense
  documents" and "hundreds of documents"/"hundreds of pages" (qualitative, not
  numeric) were found in the article.
- No sub-pages were linked from the article that required following; this is a
  self-contained case-study post.
- Confidence overall set to "emerging": a first-party Anthropic case study with two
  named practitioner sources and one specific (but self-reported, single-company,
  single-benchmark) accuracy metric — stronger than a pure anecdote, but not an
  independently verified or externally reproducible result.
