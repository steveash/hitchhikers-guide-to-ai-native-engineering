---
source_url: https://www.thoughtworks.com/insights/articles/How-data-agents-fail-and-why-its-a-context-problem
source_type: blog-post
title: "How data agents fail, and why it's a context problem"
author: Zichuan Xiong (Global Head of AIOps, Thoughtworks Managed Services)
date_published: 2026-08-03
date_extracted: 2026-08-19
last_checked: 2026-08-19
status: current
confidence_overall: emerging
issue: "#2782"
---

# How Data Agents Fail, and Why It's a Context Problem

> Thoughtworks essay arguing that data agents fail not from model weakness
> but from an uncontrolled step in their own pipeline — cross-system
> context resolution — illustrated with a healthcare example where a
> syntactically valid, successfully executed query silently blended two
> mutually-exclusive Medicare populations, and prescribing that enterprises
> codify tacit reconciliation knowledge into runtime services and
> domain-aware data products rather than leaving it as institutional
> knowledge.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, "Articles" category; published
  August 3, 2026; discovered via the trusted `thoughtworks` RSS feed). A
  practitioner essay structured around a single worked failure example
  ("A wrong readmission rate"), a root-cause section ("One concept, two
  systems"), a diagnostic framework ("The missing control in context" /
  "Can we control it?"), and a prescriptive closing section ("Closing the
  gap").
- **Author credibility**: Zichuan Xiong's Thoughtworks profile page states
  his title as **Global Head of AIOps**, with a bio reading: "Zichuan leads
  AI-powered Operations at Thoughtworks Managed Services, driving agentic
  AIOps and SRE modernization. With 18 years of experience, he pioneers
  pragmatic, scalable AI solutions across operations, platforms and
  enterprise systems." This corrects the Prospector's triage comments,
  which both stated his title as "Global Head of AI for Thoughtworks
  Managed Services" — the actual verified title is Global Head of AIOps.
  Xiong already has two other source notes in this corpus on adjacent
  ontology/data-modernization topics:
  `blog-thoughtworks-xiong-ontology-llm-data-modernization.md` (solo,
  2026-07-22) and `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md`
  (co-authored, 2026-07-23) — this is his third publication on this theme
  within a two-and-a-half week window. The article names no specific
  client, health system, or vendor; the healthcare example reads as an
  illustrative composite ("a data agent" computing "a 30-day readmission
  rate") rather than a documented, attributed case study.
- **Scope**: Covers one worked failure example (CHF readmission rate
  conflating Medicare Advantage and Original Medicare populations), a
  root-cause analysis of why two internally-correct source systems produced
  an ambiguous boundary, a six-step data-agent pipeline with an explicit
  "which steps have controls" diagnostic, and five prescriptive practices
  for closing the gap. Does NOT cover: a named client engagement, a
  measured before/after accuracy figure, an implementation of the proposed
  "runtime service" for context resolution, or a comparison against
  alternative architectures (e.g., the passive-harvesting approach in
  `blog-thoughtworks-gall-layered-context-enterprise-data.md`).

## Extracted Claims

### Claim 1: Data agent failures in enterprise workflows are usually not caused by the model itself, but by enterprise data carrying meaning that exists outside the data
- **Evidence**: Opening thesis statement of the article, framing the
  argument that follows.
- **Confidence**: emerging (a framing claim consistent with this corpus's
  existing ontology/semantic-layer sourcing, not itself an isolated
  empirical finding)
- **Quote**: "The reason isn't usually the model. It's that enterprise data carries meaning that exists outside the data itself."
- **Our assessment**: This is functionally the same diagnostic move as
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 1 ("A
  language model can read your documents, but it doesn't hold your
  operating logic") — both separate the model's linguistic competence from
  the enterprise's tacit operational/semantic knowledge, and both locate
  the failure surface in the latter, not the former. This article's
  distinct contribution is naming the specific pipeline step (context
  resolution, Claim 6) where that gap actually bites.

### Claim 2: A production data agent computing a CHF 30-day readmission rate silently blended two mutually-exclusive Medicare populations, producing a clinically invalid result
- **Evidence**: The article's central worked example, under "A wrong
  readmission rate."
- **Confidence**: anecdotal (a single, unnamed illustrative case — no
  health system, date, or independent audit is named)
- **Quote**: "The result had quietly folded Original Medicare members in with the Medicare Advantage ones."
- **Our assessment**: The specific failure mode — mixing two enrollment
  categories that are mutually exclusive under Medicare's actual
  regulatory structure — is a strong illustration precisely because the
  query "worked": it returned rows, in the right shape, without error. It
  demonstrates that syntactic/execution success is not evidence of
  semantic correctness (see Claim 4).

### Claim 3: The two source systems modeled the same real-world concept (Medicare enrollment category) at different levels of granularity — the Claims DB three levels deep down to HMO/PPO, the Enrollment DB only two levels — and each system was internally correct on its own terms
- **Evidence**: Direct comparison under "One concept, two systems,"
  naming each source system and its hierarchy depth explicitly.
- **Confidence**: anecdotal (specific to the single illustrative example;
  no second corroborating case given in the article)
- **Quote**: "Source 1, Claims DB. Three levels deep, down to HMO and PPO:"
- **Quote**: "Source 2, Enrollment. Two levels, and it stops there:"
- **Quote**: "Each system is internally correct."
- **Our assessment**: This is the article's most concrete, reusable
  diagnostic pattern: the failure was not a bug in either system, but an
  unreconciled difference in modeling depth between two systems that each
  pass their own internal validation. This is a specific, worked instance
  of the general "semantic-collision gap" pattern already named in
  `blog-thoughtworks-xiong-ontology-llm-data-modernization.md` Claim 8
  (a shared type name across systems does not imply shared meaning,
  illustrated there by `BillingStatus`/`TicketStatus` both typed `Status`
  with opposite implications) — here the collision is in hierarchy depth
  rather than a shared type name, but the underlying mechanism (two
  independently-correct systems disagreeing on how a concept decomposes)
  is the same category of gap.

### Claim 4: The failure occurred despite syntactically valid SQL and correct query execution — the fault sat one step earlier, in how the agent resolved the ambiguous category boundary before generating any query
- **Evidence**: Direct causal attribution in the article, tracing the
  failure back past SQL generation and execution to an earlier resolution
  step.
- **Confidence**: emerging (a specific causal claim about where in the
  pipeline the failure originated, tied to the one worked example, but
  consistent with the article's broader six-step diagnostic framework)
- **Quote**: "The fault sat one step earlier: when the agent resolved 'MA members' against the data, the boundary between Medicare Advantage and Original Medicare had already conflated."
- **Our assessment**: This is the article's key reframing for verification
  practice: a query that executes successfully and returns well-formed
  rows can still be wrong in a way that no SQL linter, type checker, or
  schema validator would catch, because those controls operate downstream
  of the step where the actual error was introduced. This directly extends
  `blog-anthropic-carta-healthcare-context-engineering.md` Claim 5 (a
  three-axis prompt/context/retrieval failure-attribution framework for
  extraction pipelines) by identifying a fourth, upstream failure axis
  specific to data agents: cross-system boundary resolution, which is
  distinct from context assembly (Carta's Claim 2) because it is about
  reconciling *conflicting category definitions* across sources rather
  than scoping *which* data enters a context window.

### Claim 5: Data agents operate through six steps — intent, cross-system context resolution, SQL generation, SQL execution, data retrieval, and presentation — and deterministic controls exist for five of the six, but not for context resolution
- **Evidence**: The article's named diagnostic table, under "Can we
  control it?", listing each step alongside its existing control mechanism
  or lack thereof.
- **Confidence**: emerging (a named process taxonomy proposed by the
  article, illustrated by the one worked example, not validated against
  multiple independent pipelines)
- **Quote**: "Intent | Cross-system context resolution | SQL generation | SQL execution | Data retrieval | Presentation"
- **Quote**: "Clarifying questions; intent confirmation" (Step 1 control)
- **Quote**: "Query review, SQL linting, dry-run plans" (Step 3 control)
- **Quote**: "Engine-enforced syntax, types, constraints" (Step 4 control)
- **Quote**: "Schema and type contracts; row-count checks" (Step 5 control)
- **Quote**: "Formatting rules, unit checks" (Step 6 control)
- **Our assessment**: This control-coverage matrix is the article's most
  guide-actionable contribution: it doesn't just assert "context matters,"
  it names five specific, already-common control mechanisms (clarifying
  questions, SQL linting, engine type enforcement, schema contracts,
  formatting rules) and shows that all five sit downstream of the one step
  that has none. This is a reusable diagnostic a team can apply to their
  own data-agent pipeline: enumerate the steps, ask "what control exists
  here," and expect the gap to appear at context/boundary resolution
  specifically, not distributed evenly across the pipeline.

### Claim 6: Context resolution — reconciling how independent source systems represent the same real-world concept before a query can be correctly scoped — is the critical, currently uncontrolled point where data agents fail
- **Evidence**: Direct statement under "The missing control in context,"
  naming the failure point identified by the six-step framework (Claim 5).
- **Confidence**: emerging (a specific claim about where failure
  concentrates, argued from the one worked example plus the control-matrix
  reasoning, not from a measured failure-rate distribution across many
  pipelines)
- **Quote**: "Context resolution is the critical and challenging point where data agents fail."
- **Our assessment**: This names, as a distinct pipeline step with its own
  failure profile, something this corpus's other context-engineering
  sources discuss in adjacent but not identical terms.
  `blog-anthropic-carta-healthcare-context-engineering.md` Claim 2 names
  per-query context *scoping* (what data enters the window and its
  temporal boundary) as the primary accuracy lever; this claim names
  cross-system *boundary reconciliation* (whether two systems' category
  definitions agree at all) as a distinct, prior problem. A context window
  can be perfectly scoped to the right systems and still be wrong if the
  systems disagree about what a category means.

### Claim 7: Closing the gap requires recognizing recurring reconciliation patterns and continuously discovering new semantic gaps, rather than treating each cross-system mismatch as a one-off incident
- **Evidence**: First two named practices under "Closing the gap."
- **Confidence**: anecdotal (prescriptive recommendations; no described
  implementation, tooling, or measured detection rate given)
- **Quote**: "Recognize recurring reconciliation patterns"
- **Quote**: "Continuously discover new semantic gaps"
- **Our assessment**: This treats semantic-gap discovery as an ongoing
  operational practice rather than a one-time audit — consistent with the
  "continuous maintenance" prescription already in this corpus (e.g.
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 6's
  observation that an unmaintained model goes stale within roughly two
  quarters), but applied here specifically to cross-system boundary
  reconciliation rather than ontology upkeep in general.

### Claim 8: Enterprises should turn tacit reconciliation knowledge — the kind currently held only in individual experts' heads — into codified, explicit rules
- **Evidence**: Named practice under "Closing the gap."
- **Confidence**: anecdotal (a prescriptive recommendation; no worked
  example of a codified rule or its format is given in the article)
- **Quote**: "Turn the tacit into the codified"
- **Our assessment**: This is a compact restatement of the translation-gap
  failure mode and fix already in this corpus —
  `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 7
  (ontology engineers know the formalism but not the business; SMEs know
  the business but not formal modeling) and Claim 9 ("curate, don't draft
  from scratch" — use LLM pipelines to pull draft taxonomies from existing
  schemas and documentation) — applied specifically to cross-system
  category reconciliation rather than ontology construction generally.

### Claim 9: Context resolution should be built as a runtime service, and enterprises should prefer domain-aware data products over ad hoc, per-query reconciliation
- **Evidence**: Final two named practices under "Closing the gap."
- **Confidence**: anecdotal (a prescriptive architectural recommendation;
  no described implementation, API shape, or deployed example is given)
- **Quote**: "Make context resolution a runtime service"
- **Quote**: "Prefer domain-aware data products"
- **Our assessment**: "Domain-aware data products" directly corroborates
  `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md` Claim 7
  (modular, self-describing "data products" packaging data, metadata,
  semantic meaning, and governance policies together, evaluated by an
  "agent-readability" test) — the same author naming the same
  architectural unit as the fix for a different, more specific failure
  (cross-system boundary conflation rather than AI-readiness generally).
  "Make context resolution a runtime service" also corroborates
  `blog-anthropic-carta-healthcare-context-engineering.md` Claim 1
  (Mazzanti: "the hardest problems we solved weren't about building a
  perfect prompt, they were about context construction") — both sources
  independently treat context assembly/resolution as infrastructure to be
  built and operated, not a one-time modeling exercise or a property of a
  good prompt.

### Claim 10: Making enterprise data AI-ready means making its meaning executable, not merely making the data accessible
- **Evidence**: Closing synthesis statement of the article.
- **Confidence**: emerging (a closing framing claim, consistent with and
  restating the article's overall argument)
- **Quote**: "It means making its meaning executable."
- **Our assessment**: This closing line is the article's most quotable
  synthesis and ties directly back to
  `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md`'s central
  thesis (the same author, one of its three co-authors) that AI-readiness
  requires a continuously-maintained semantic context layer, not just data
  accessibility. This article supplies the specific mechanism by which
  "accessible but not executable" meaning causes production failures
  (Claims 2-6), which the broader AI-ready-data essay argues for in more
  general terms.

## Concrete Artifacts

```
Source: Zichuan Xiong, "How data agents fail, and why it's a context
problem," Thoughtworks Insights, August 3, 2026

Six-step data agent pipeline and control coverage
(from "Can we control it?"):

Step 1: Intent                          -> Clarifying questions; intent confirmation
Step 2: Cross-system context resolution -> NO EXISTING CONTROL
Step 3: SQL generation                  -> Query review, SQL linting, dry-run plans
Step 4: SQL execution                   -> Engine-enforced syntax, types, constraints
Step 5: Data retrieval                  -> Schema and type contracts; row-count checks
Step 6: Presentation                    -> Formatting rules, unit checks

The wrong readmission rate originated at Step 2. Steps 3-6 all executed
correctly and passed their respective controls.
```

```
Worked example: hierarchy mismatch between two source systems
(from "One concept, two systems")

Source 1, Claims DB:  Medicare
                         |-- Medicare Advantage
                         |     |-- HMO
                         |     |-- PPO
                         |-- Original Medicare
                               |-- Part A
                               |-- Part B
                       (three levels deep, down to HMO and PPO)

Source 2, Enrollment: Medicare
                         |-- Advantage
                         |-- Traditional
                       (two levels, stops there)

Neither system is wrong internally; the systems disagree on how many
levels the "Medicare enrollment category" concept decomposes into, and
under what names ("MedicareAdvantage" in Claims vs. "Advantage" in
Enrollment).
```

```
Five prescribed practices for closing the gap (from "Closing the gap"):
1. Recognize recurring reconciliation patterns
2. Continuously discover new semantic gaps
3. Turn the tacit into the codified
4. Make context resolution a runtime service
5. Prefer domain-aware data products
```

## Cross-References

### Cross-reference verification notes
`blog-thoughtworks-xiong-ontology-llm-data-modernization.md`,
`blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md`,
`blog-thoughtworks-asthagiri-ontology-failure-modes.md`,
`blog-thoughtworks-gall-layered-context-enterprise-data.md`, and
`blog-anthropic-carta-healthcare-context-engineering.md` were re-read in
full before writing the citations above and below; claim numbers cited
were confirmed against each note's numbered `### Claim N:` headings in
document order.

- **Corroborates**:
  - `blog-thoughtworks-xiong-ontology-llm-data-modernization.md` Claim 8
    (a shared type name across systems does not imply shared meaning — a
    "semantic-collision gap," illustrated by `BillingStatus`/`TicketStatus`
    both typed `Status` with opposite implications): this article's
    Claim 3 (Claims DB vs. Enrollment DB modeling the same concept at
    different hierarchy depths) is a second, independent worked example of
    the same underlying gap category — same author, different illustrative
    domain (healthcare vs. billing/support), corroborating that this is a
    recurring pattern rather than a one-off illustration.
  - `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md` Claim 7
    (modular, self-describing "data products" packaging data, metadata,
    semantic meaning, and governance policies, evaluated by an
    "agent-readability" test): this article's Claim 9 ("prefer domain-aware
    data products") names the same architectural unit as a direct fix for
    the context-resolution failure documented here — same author, same
    prescription, applied to a more specific failure mode.
  - `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 7
    (translation gap: ontology engineers know the formalism, SMEs know the
    business, neither alone) and Claim 9 ("curate, don't draft from
    scratch"): this article's Claim 8 ("turn the tacit into the codified")
    is a compressed restatement of the same translation-gap diagnosis and
    fix, applied to cross-system boundary reconciliation specifically.
  - `blog-anthropic-carta-healthcare-context-engineering.md` Claim 1
    (Mazzanti: "the hardest problems we solved weren't about building a
    perfect prompt, they were about context construction") and Claim 5
    (a three-axis prompt/context/retrieval failure-attribution framework):
    this article's Claim 9 ("make context resolution a runtime service")
    corroborates treating context work as built infrastructure rather than
    prompt tuning, from a different vendor and genre (Thoughtworks
    conceptual essay vs. Anthropic-published production case study). This
    article's Claim 4 (fault traced past SQL generation/execution back to
    an earlier resolution step) also extends Carta's three-axis framework
    by naming a fourth, more upstream failure axis specific to
    multi-source data agents: cross-system boundary resolution, distinct
    from Carta's per-query context *scoping*.

- **Contradicts**: None filed as a new issue. This article's prescriptive
  stance — codify tacit reconciliation knowledge, build context resolution
  as durable runtime infrastructure, prefer curated domain-aware data
  products (Claims 7-9) — sits on the same side of the already-filed
  contradiction [#2458](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/2458)
  as `blog-thoughtworks-asthagiri-ontology-failure-modes.md` and
  `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md` (the
  "curate and codify" position), opposite
  `blog-thoughtworks-gall-layered-context-enterprise-data.md`'s Claim 6
  (any relationship-mapping process requiring human/SME confirmation "will
  unfortunately be dead on arrival" because enterprise data decay outpaces
  human curation). This is additional same-side evidence for an existing,
  already-filed contradiction, not a new disagreement — no new issue
  filed, per MINER.md §4a's guidance to check existing filed
  contradictions first.

- **Extends**:
  - `blog-thoughtworks-xiong-ontology-llm-data-modernization.md`: that
    article's six-step agentic loop (build ontological context per source,
    curate/reconcile, compare against design context, identify gaps, act,
    update and loop) describes *how to build and maintain* a landscape-level
    ontology. This article's six-step pipeline (intent, context resolution,
    SQL generation, execution, retrieval, presentation) is a *different,
    complementary* six-step process describing how a single data agent
    *answers a query at runtime* — the two are not the same taxonomy and
    should not be conflated. This article supplies the runtime-failure
    diagnostic (which pipeline steps have controls) that the ontology-loop
    article does not itself provide.
  - `blog-anthropic-carta-healthcare-context-engineering.md`: that note
    documents per-query context scoping with temporal anchors as a
    production accuracy lever for structured clinical extraction. This
    article extends the same domain (healthcare data) to a different task
    (SQL-generating data agents over relational sources) and identifies a
    failure mode — cross-system boundary conflation — that per-query
    scoping alone would not catch, since the ambiguity here is in what a
    category *means* across sources, not in which time window of data is
    relevant.

- **Novel**:
  - **The six-step data-agent pipeline with an explicit control-coverage
    matrix** (Claim 5, Concrete Artifacts) — naming five common, specific
    control mechanisms (clarifying questions, SQL linting, engine type
    enforcement, schema contracts, formatting rules) and showing all five
    sit downstream of the one uncontrolled step — is a new diagnostic
    framework in this corpus. No prior source note frames data-agent
    reliability as a step-by-step control-coverage audit.
  - **The specific Medicare Advantage / Original Medicare hierarchy-depth
    mismatch example** (Claims 2-3) is a new, concrete healthcare failure
    case distinct from `blog-anthropic-carta-healthcare-context-engineering.md`'s
    clinical-abstraction success story — this corpus now has both a
    documented healthcare context-engineering success and a described
    healthcare context-resolution failure, in the same domain but opposite
    outcomes.
  - **"Syntactically valid, successfully executed, semantically wrong" as
    an explicit named failure category** (Claim 4) — the article's framing
    that all five downstream controls can pass while the actual answer is
    still wrong is a sharper, more specific claim than this corpus's prior
    general observation that AI accuracy failures need root-cause
    attribution (Carta's three-axis framework); it names a failure that
    sits entirely outside that three-axis space.

## Guide Impact

- **Chapter 03 (Safety and Verification)**: Add the "syntactically valid,
  successfully executed, semantically wrong" failure category (Claim 4) as
  an explicit gap in query-based data-agent verification. Post-execution
  checks that validate SQL syntax, type contracts, and row counts (the
  article's Steps 3-5 controls) do not catch category-boundary conflation.
  Recommend teams add a semantic-boundary/domain-validity check as a
  distinct verification layer, alongside the existing three-axis
  (prompt/context/retrieval) attribution framework recommended from
  `blog-anthropic-carta-healthcare-context-engineering.md` — this source
  shows that framework needs a fourth axis (cross-system boundary
  resolution) for data agents specifically.
- **Chapter 04 (Context Engineering)**: Add the six-step control-coverage
  matrix (Claim 5, Concrete Artifacts) as a diagnostic exercise: teams
  building data agents should enumerate their own pipeline's steps and
  identify which have deterministic controls and which don't, expecting
  the gap to concentrate at cross-system context/boundary resolution
  rather than being evenly distributed. This is a concrete audit technique
  the guide currently lacks, distinct from per-query context scoping
  (already sourced from Carta) and from ontology-building workflows
  (already sourced from Xiong's earlier article) — cross-system boundary
  resolution is "do two systems agree on what this category means," which
  neither of those other patterns addresses directly.
- **Chapter 02 (Data & Infrastructure)**: Add "make context resolution a
  runtime service" and "prefer domain-aware data products" (Claim 9) as
  concrete architectural recommendations, cross-linked to the "data
  products" pattern already sourced from
  `blog-thoughtworks-xiong-asthagiri-kulkarni-ai-ready-data.md` Claim 7 —
  this article supplies a specific failure mode (Claims 2-4) that
  motivates why that pattern matters operationally, not just as an
  AI-readiness abstraction.

## Extraction Notes

- **Full verbatim article text was not obtainable via a single WebFetch
  pass**, consistent with other Thoughtworks pieces in this corpus (e.g.
  the companion Xiong and Asthagiri notes). An initial WebFetch request
  returned a paraphrased section-by-section summary. Three follow-up
  WebFetch calls were made requesting only short, verbatim, contiguous
  passages tied to named sections, with explicit instructions not to
  paraphrase or splice non-adjacent sentences into a single quote. One
  early candidate quote (returned with an internal ellipsis joining two
  possibly non-adjacent fragments) was discarded and re-fetched cleanly
  rather than used as-is, per MINER.md §2a(3). All quotes above are drawn
  from these verified short-passage fetches. The Assayer should spot-check
  quotes against the live URL.
- **Author title corrected against the primary source.** The Prospector's
  triage comments (both instances) stated Xiong's title as "Global Head of
  AI for Thoughtworks Managed Services." An independent WebFetch of his
  Thoughtworks profile page returned "Global Head of AIOps" as the actual
  listed title, with a bio describing his focus as "AI-powered Operations
  at Thoughtworks Managed Services, driving agentic AIOps and SRE
  modernization." The corrected title is used in this note's frontmatter
  and Source Context; the triage comments' title was not propagated.
- **No sub-pages followed.** The article is a single, self-contained essay
  with a single worked example; no in-article links to deeper technical
  posts or external studies were surfaced by any of the four WebFetch
  passes, consistent with the sibling Xiong/Asthagiri/Gall notes in this
  corpus, none of which found substantive sub-pages either.
- **No new contradiction filed.** This article's prescriptive stance
  (codify tacit knowledge, build durable context-resolution
  infrastructure, prefer curated data products) is additional same-side
  evidence for the existing, already-filed contradiction
  [#2458](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/2458)
  between the Asthagiri/Xiong "curate as a product" position and Gall's
  "curation is dead on arrival, harvest passively instead" position — see
  Cross-References → Contradicts. No new issue was filed per MINER.md
  §4a's guidance to check existing filed contradictions before filing.
- **Confidence rated `emerging` overall.** The article's core diagnostic
  framework (the six-step pipeline and its control-coverage matrix, Claims
  5-6) is specific and internally coherent, and is now corroborated by a
  second independent worked example of the same author's
  "semantic-collision gap" pattern (Claim 3, cross-referencing the earlier
  ontology-modernization article). However, the central evidence is a
  single, unnamed illustrative case (no health system, date, or
  independent audit named), and the five closing prescriptions (Claims
  7-9) are asserted without any described implementation or measured
  outcome — individually rated `anecdotal`. This mirrors the `emerging`
  rating given to Xiong's other two source notes in this corpus.
