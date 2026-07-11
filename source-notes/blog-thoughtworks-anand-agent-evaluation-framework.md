---
source_url: https://www.thoughtworks.com/insights/blog/machine-learning-and-ai/Evaluating-AI-agents-in-production
source_type: blog-post
title: "Evaluating AI agents in production: A practical framework"
author: Akshay Anand
date_published: 2026-06-18
date_extracted: 2026-07-11
last_checked: 2026-07-11
status: current
confidence_overall: emerging
issue: "#1744"
---

# Evaluating AI agents in production: A practical framework

> A Thoughtworks practitioner framework proposing a three-layer evaluation
> architecture (persona-based testing, functional unit evals, operational
> observability) for conversational AI agents, explicitly sequenced across
> the development → UAT → production lifecycle, with a named tool ecosystem
> for each layer.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, published June 18, 2026)
- **Author credibility**: Akshay Anand, writing on Thoughtworks' corporate
  insights blog. Thoughtworks is a consultancy with broad client-delivery
  exposure to enterprise AI projects, which is the implicit basis for the
  framework's claims — but the post cites no named client engagement, no
  outcome metrics from applying the framework, and no controlled study of
  its own. The one external statistic cited (95% AI project failure rate)
  is attributed secondhand to "a study by MIT," not independently verified
  in this post. The framework itself reads as a synthesis of established
  LLM-eval tooling and practice, organized into a proposed architecture,
  rather than a report of a single case's outcomes.
- **Scope**: Covers why traditional software testing fails for AI agents
  (non-determinism, multi-component systems, RAG vs. prompt-engineered
  evaluation needs, phase evolution), a three-layer evaluation architecture
  with a named tool per layer, a four-step implementation roadmap from
  development through continuous production improvement, and a metrics
  taxonomy (offline, online, RAG-specific). Does NOT cover: how to build or
  configure any of the named tools, cost/latency tradeoffs of running the
  three layers together, or a worked case study with before/after numbers.

## Extracted Claims

### Claim 1: Roughly 95% of AI projects fail, per an MIT study, which the article uses to motivate evaluation as the core unsolved problem
- **Evidence**: Secondhand citation of an MIT study, used as the article's
  opening motivation.
- **Confidence**: anecdotal (secondhand citation; the underlying MIT study is
  not named, linked, or examined for methodology in this post)
- **Quote**: "Based on a study by MIT last year, around 95% of AI projects fail."
- **Our assessment**: This is a widely-circulated but frequently contested
  statistic in AI industry commentary; the post does not name the specific
  MIT report or examine its methodology, so we treat the number itself as
  unverified color rather than a load-bearing data point. What is useful is
  the article's diagnosis of *why* projects fail — it attributes failure to
  measurement and evaluation gaps rather than model capability, which is the
  actual thesis the rest of the post supports with more specific claims.

### Claim 2: Traditional software testing assumes deterministic behavior, which breaks down for LLM-based systems
- **Evidence**: Stated as the article's core structural argument for why a
  new evaluation approach is needed, under the heading "Why traditional
  testing fails for AI."
- **Confidence**: settled (this is a well-established, broadly corroborated
  premise in the evaluation literature, not a novel claim by this author)
- **Quote**: "Traditional software testing assumes deterministic behavior:
  the same input produces the same output every time."
- **Our assessment**: This is the uncontroversial premise the rest of the
  framework builds on. It corroborates the general corpus consensus (e.g.,
  `blog-langchain-better-harness.md` Claim 6, "agents are famous cheaters,"
  and `blog-langchain-human-judgment-improvement-loop.md` Claim 7, "it's
  impossible to know what an AI agent will do until it runs") that agent
  behavior cannot be fully characterized by static code inspection or
  single-run tests.

### Claim 3: Enterprise AI systems combine deterministic and non-deterministic components in the same pipeline, and each requires a different evaluation approach
- **Evidence**: Named as "Driver 2" for specialized evaluation, with explicit
  examples of each component type.
- **Confidence**: emerging (structural observation, no quantification of how
  common mixed pipelines are)
- **Quote**: "Deterministic agent: e.g. intent identification agent or a
  guardrail agent. Non-deterministic agent: e.g. summarization agent,
  rewriting agent."
- **Our assessment**: This corroborates `blog-langchain-human-judgment-improvement-loop.md`
  Claim 3 (deterministic code checkpoints alongside LLM reasoning reduce
  latency, guarantee critical-step execution, and may be a hard regulatory
  requirement). Both sources converge on treating "deterministic vs.
  non-deterministic" as a design axis that should also be an *evaluation*
  axis — you cannot apply the same eval methodology uniformly across a
  pipeline that mixes both component types.

### Claim 4: RAG systems and prompt-engineered systems require distinct evaluation metric sets
- **Evidence**: Named as "Driver 3," with two explicit metric lists.
- **Confidence**: emerging (taxonomy is plausible and internally consistent,
  but the post does not justify why these specific four-and-four metric
  sets are the right split, or whether hybrid RAG+prompt systems need both)
- **Quote**: "RAG systems are typically evaluated on: Retrieval relevance,
  Context coverage, Faithfulness, Hallucination rates. Prompt-based systems
  are typically evaluated on: Instruction adherence, Task completion,
  Reasoning quality, Output consistency."
- **Our assessment**: This is directly corroborated by `blog-fowler-bayer-prince-agentic-rag.md`
  Claim 13, which documents a concrete production implementation of
  RAG-specific evaluation (RAGAS metrics: Faithfulness, Answer Relevancy,
  Context Relevancy, Answer Accuracy, Semantic Similarity) via Langfuse.
  The Thoughtworks post generalizes what PRINCE implements: PRINCE is the
  worked example of the RAG side of this driver; this post is the first
  source in the corpus to state the RAG-vs-prompt evaluation split as an
  explicit, named taxonomy rather than an implementation detail of one
  system.

### Claim 5: Persona-based testing is the layer for validating agent logic via high-fidelity, multi-turn conversation simulations against synthetic "human personas"
- **Evidence**: Described as the first of three layers in the "Three-layer
  evaluation architecture" section, with named supporting tools.
- **Confidence**: emerging (named as a distinct evaluation layer with a
  supporting tool ecosystem; no metrics on its effectiveness relative to
  the other two layers are given)
- **Quote**: "High-fidelity, multi-turn simulations. We test against 'human
  personas' to validate the agent's logic."
- **Our assessment**: This is genuinely novel to the corpus — no existing
  source note names persona-based multi-turn simulation as a distinct
  evaluation layer with dedicated tooling (Snowglobe, Collinear, Rhesis are
  named; none appear elsewhere in the corpus). It is conceptually adjacent
  to `blog-langchain-human-judgment-improvement-loop.md`'s "Phase 1
  Development" ground-truth datasets, but that source describes
  single-turn question→answer pairs, not persona-driven multi-turn
  conversation simulation across project phases (synthetic personas in dev,
  business-user personas in UAT).

### Claim 6: Functional unit evals are automated, assertion-based checks — the "Pytest for LLMs" — that can be scoped to either individual agents or whole conversations
- **Evidence**: Described as the second layer, with an explicit sub-split
  between agent-level and conversation-level units of evaluation.
- **Confidence**: emerging (the analogy to Pytest is a framing device, not
  a technical equivalence claim; the agent-vs-conversation unit split is
  stated without guidance on when to prefer one over the other)
- **Quote**: "The 'Pytest' for LLMs. These are automated, assertion-based
  checks that catch regressions." ... "Agents as a unit: Here, individual
  agents are unit tested to verify that they produce intended outcomes.
  Conversation as a unit: Conversation-level evaluations treat a complete
  interaction as the unit under test."
- **Our assessment**: The "catch regressions" framing directly corroborates
  `blog-langchain-better-harness.md` Claim 12 ("Once our agent handles a
  case correctly, we don't want to lose that gain. The eval becomes a
  regression test.") — both sources converge on evals-as-regression-tests
  as the load-bearing role of the unit-eval layer once an agent is working.
  The agent-level vs. conversation-level distinction is new to the corpus:
  neither the LangChain posts nor `blog-hamel-eval-smell.md` name this as
  an explicit choice of evaluation unit granularity.

### Claim 7: Operational observability is the production safety net — real-time tracing and monitoring that bridges the gap between pre-deployment testing and real user behavior
- **Evidence**: Described as the third layer, framed against the
  "it works on my machine" problem.
- **Confidence**: emerging (framing device; the specific mechanics of
  what "bridging the gap" requires operationally are not detailed beyond
  the tool names and the roadmap's Step 3 description)
- **Quote**: "The production safety net. Real-time tracing and monitoring
  to bridge the gap between 'it works on my machine' and 'it works for
  the user.'"
- **Our assessment**: This corroborates `blog-langchain-human-judgment-improvement-loop.md`'s
  "Phase 2 — Post-Deployment" (online evaluations, alerts, annotation
  queues) almost one-for-one in function, though the Thoughtworks post
  frames it as a named architectural *layer* rather than a lifecycle
  *phase*. Read together, the two sources describe the same operational
  practice from different organizing angles: LangChain organizes by time
  (development → post-deployment → refinement), Thoughtworks organizes by
  evaluation type (persona / unit / observability) that maps onto phases
  secondarily via the roadmap in Claim 9 below.

### Claim 8: The three evaluation layers map to a named vendor tool ecosystem — persona-based (Snowglobe, Collinear, Rhesis), unit evals (DeepEval, ragas, TruLens), observability (LangSmith, Langfuse, Helicone)
- **Evidence**: Presented as a table under the "Three-layer evaluation
  architecture" section, one tool triad per layer.
- **Confidence**: anecdotal (tool selection presented without comparison
  criteria, pricing, or rationale for why these three per category and not
  others)
- **Quote**: (no direct quote; see Concrete Artifacts for the extracted
  table — the tool names themselves are the citable artifact, not a
  quotable sentence)
- **Our assessment**: Five of these nine tool names (Snowglobe, Collinear,
  Rhesis, DeepEval, TruLens, Helicone) are new to the corpus. Two
  (ragas, Langfuse) already appear in `blog-fowler-bayer-prince-agentic-rag.md`
  as PRINCE's actual production stack (RAGAS via Langfuse), which gives
  independent corroboration that at least this pairing is a real,
  load-bearing production choice rather than a hypothetical listing.
  LangSmith appears extensively elsewhere in the corpus
  (`blog-langchain-human-judgment-improvement-loop.md`,
  `blog-langchain-better-harness.md`) as LangChain's own observability
  platform. The unverified two-thirds of this tool list (Snowglobe,
  Collinear, Rhesis, DeepEval, TruLens, Helicone) should be treated as a
  landscape pointer for further evaluation, not an endorsement — the post
  gives no comparative evidence for choosing among them.

### Claim 9: The recommended implementation roadmap has four sequential steps: start with unit testing (~20% automated), refine through business-user (UAT) testing, introduce production observability, then continuously improve from production feedback
- **Evidence**: Explicit four-step roadmap with a section heading per step.
- **Confidence**: emerging (sequencing is logical and consistent with
  software testing maturity models generally, but the specific 20%
  automation figure is asserted without a study or survey behind it)
- **Quote**: "At this stage, you'll likely have around 20% of your scenarios
  automated, with the remaining 80% still requiring manual validation."
  ... "Capture traces, user feedback, latency, costs, retrieval quality and
  failure patterns." ... "Review production conversations regularly,
  identify failure modes, update test datasets and recalibrate LLM judges."
- **Our assessment**: The ~20%-automated starting point is a useful
  expectation-setting number for teams new to agent evaluation — it
  pushes back against the assumption that a mature eval suite exists (or
  should exist) from day one. This directly corroborates the sequencing
  logic in `blog-langchain-human-judgment-improvement-loop.md`'s three-phase
  flywheel (development → post-deployment → continuous refinement) and
  "recalibrate LLM judges" corroborates that source's Claim 6 (LLM-as-a-judge
  evaluators require ongoing calibration against subject matter expert
  examples, not a one-time setup).

### Claim 10: Offline metrics distinguish exact-match accuracy from semantic correctness, and RAG-specific evaluation includes hallucination rate as the frequency of unsupported claims
- **Evidence**: Named and defined in the metrics taxonomy sections
  ("Offline evals (pre-deployment)" and "RAG evaluation metrics").
- **Confidence**: settled (these are standard, widely-used metric
  definitions in the LLM evaluation field, not novel to this post)
- **Quote**: "Accuracy/exact match: How often the output matches expected
  answers." ... "Semantic correctness: Meaningfully correct even if wording
  differs." ... "Hallucination rate. Frequency of unsupported claims."
- **Our assessment**: These definitions are useful as precise, reusable
  glossary entries rather than novel claims — the value is in having crisp,
  quotable one-line definitions to cite in the guide rather than in any
  new empirical finding. The accuracy/semantic-correctness split is a
  concrete reminder that exact-match scoring under-counts correct agent
  behavior when wording legitimately varies.

### Claim 11: Organizations that treat evaluation as a continuous discipline rather than a one-time testing activity will be better positioned to build trustworthy AI systems at scale
- **Evidence**: Stated as the article's closing synthesis.
- **Confidence**: emerging (thesis-level claim, consistent with but not
  independently proven by the rest of the post's content)
- **Quote**: "Organizations that treat evaluation as a continuous
  discipline, rather than a one-time testing activity, will be far better
  positioned to build trustworthy AI systems at scale."
- **Our assessment**: This closing claim is the framework's thesis in one
  sentence and is consistent with the entire LangChain "agent improvement
  flywheel" corpus (`blog-langchain-human-judgment-improvement-loop.md`,
  `blog-langchain-better-harness.md`), both of which treat evaluation as
  an ongoing, never-finished system rather than a pre-launch gate. No
  source in the corpus disputes this framing; it functions as corroborating
  consensus rather than a novel or contested position.

### Claim 12: Project phase determines evaluation strategy — development-stage testing should be rapid and synthetic, while UAT-stage testing should use stakeholder-validated personas
- **Evidence**: Named as "Driver 4" and elaborated under "What should be
  tested?"
- **Confidence**: emerging (structural claim about how evaluation should
  evolve; no comparative data on outcomes from following vs. not following
  this sequencing)
- **Quote**: "The evaluation framework must be architected to evolve
  seamlessly from dev to production...from rapid, synthetic testing in
  development to stakeholder-validated personas in UAT."
- **Our assessment**: This is the connective claim that ties the
  persona-based testing layer (Claim 5) to the implementation roadmap
  (Claim 9): personas themselves are not static — they start as
  engineer-authored synthetic proxies and are replaced or refined with
  business-user-validated personas as the project moves toward production.
  This lifecycle-awareness for the *persona* artifact itself (not just the
  eval process generally) is new to the corpus.

## Concrete Artifacts

```
Four drivers requiring specialized AI agent evaluation
Source: "Evaluating AI agents in production," Akshay Anand, Thoughtworks (2026-06-18)

Driver 1: Non-deterministic behavior
  LLMs generate probabilistic responses; traditional testing assumes
  deterministic input->output mapping.

Driver 2: Multiple specialized components/agents in one system
  Deterministic agent example: intent identification, guardrail agent
  Non-deterministic agent example: summarization agent, rewriting agent

Driver 3: RAG vs. prompt-engineered systems need different metrics
  RAG metrics: Retrieval relevance, Context coverage, Faithfulness,
    Hallucination rates
  Prompt-based metrics: Instruction adherence, Task completion,
    Reasoning quality, Output consistency

Driver 4: Evaluation strategy must evolve across project phases
  Dev: rapid, synthetic testing
  UAT: stakeholder-validated personas
  Production: operational observability
```

```
Three-layer evaluation architecture and tool ecosystem
Source: "Evaluating AI agents in production," Akshay Anand, Thoughtworks (2026-06-18)

Layer 1 — Persona-based testing
  Definition: High-fidelity, multi-turn simulations against "human personas"
    to validate agent logic.
  Tools named: Snowglobe, Collinear, Rhesis

Layer 2 — Functional unit evals
  Definition: The "Pytest for LLMs" -- automated, assertion-based checks
    that catch regressions.
  Units: Agents as a unit (individual agent tested for intended outcomes)
         Conversation as a unit (complete interaction as unit under test)
  Tools named: DeepEval, ragas, TruLens

Layer 3 — Operational observability
  Definition: The production safety net -- real-time tracing and
    monitoring bridging "it works on my machine" and "it works for the user."
  Tools named: LangSmith, Langfuse, Helicone
```

```
Four-step implementation roadmap
Source: "Evaluating AI agents in production," Akshay Anand, Thoughtworks (2026-06-18)

Step 1 — Start with unit testing and early persona-based testing setup
  ~20% of scenarios automated; remaining 80% still requires manual validation

Step 2 — Refine personas, judges and tests during business user testing
  Add conversational scenarios surfaced during UAT to the test suite
  Refine personas to reflect the actual personas of users testing the system

Step 3 — Introduce production observability
  Capture traces, user feedback, latency, costs, retrieval quality,
  failure patterns

Step 4 — Continuously improve using production feedback
  Review production conversations regularly
  Identify failure modes
  Update test datasets
  Recalibrate LLM judges
```

```
Metrics taxonomy (partial, as extracted)
Source: "Evaluating AI agents in production," Akshay Anand, Thoughtworks (2026-06-18)

Offline evals (pre-deployment):
  Accuracy/exact match -- how often output matches expected answers
  Semantic correctness -- meaningfully correct even if wording differs

RAG evaluation metrics:
  Hallucination rate -- frequency of unsupported claims
```

## Cross-References

- **Corroborates** `blog-fowler-bayer-prince-agentic-rag.md` Claim 13 (PRINCE's
  two-tier evaluation: SME-curated Dataset Evaluations using RAGAS metrics vs.
  daily Live Traffic Evaluations, both via Langfuse): this Thoughtworks source's
  Driver 3 (RAG vs. prompt-engineered evaluation metrics, Claim 4 here) and its
  Layer 3 tool list (Claim 8 here, which names both `ragas` and Langfuse)
  generalize what PRINCE implements as one concrete production system. PRINCE
  is evidence that this part of the framework is not merely theoretical — a
  real production RAG pipeline uses exactly this tool pairing for exactly this
  purpose.
- **Corroborates** `blog-langchain-better-harness.md` Claim 12 (evals become
  regression tests once an agent handles a case correctly): this source's
  Layer 2 definition of functional unit evals as automated checks "that catch
  regressions" (Claim 6 here) states the same role for the unit-eval layer
  independently, from a different vendor's framing.
- **Corroborates** `blog-langchain-human-judgment-improvement-loop.md` Claim 6
  (LLM-as-a-judge evaluators require ongoing calibration against subject
  matter expert examples) and Claim 11 (production data is the best source of
  test cases after launch): this source's Step 4 ("recalibrate LLM judges")
  and Step 3/4 roadmap (Claim 9 here) state the same operational practice —
  evaluators are not "set and forget," and production traffic is the
  post-launch source of new test cases.
- **Extends** `blog-langchain-human-judgment-improvement-loop.md`: that
  source's "Phase 1 — Development" step describes ground-truth
  question→answer datasets built by engineers/PMs/SMEs, but does not name
  multi-turn persona simulation as a distinct evaluation layer with its own
  tool ecosystem. This source's persona-based testing layer (Claim 5) and its
  lifecycle treatment of personas themselves — synthetic in dev, stakeholder-
  validated in UAT (Claim 12) — is a more granular treatment of that same
  development-phase testing step.
- **Contradicts**: None found. No existing source note stakes out a
  conflicting position on evaluation architecture, layering, or sequencing.
- **Novel**:
  - **Persona-based testing named as a distinct evaluation layer** with its
    own tool ecosystem (Snowglobe, Collinear, Rhesis) — no existing source
    treats multi-turn persona simulation as a first-class evaluation
    category separate from unit evals and observability.
  - **Five tool names new to the corpus**: Snowglobe, Collinear, Rhesis,
    DeepEval, TruLens, Helicone (ragas and Langfuse were already present via
    the PRINCE note; LangSmith was already present via the LangChain notes).
  - **Agent-level vs. conversation-level as an explicit choice of evaluation
    unit granularity** within functional unit evals — not named as a duality
    anywhere else in the corpus.
  - **RAG-vs-prompt-engineered evaluation metrics stated as an explicit,
    general taxonomy** (rather than as an implementation detail of a single
    system, as in the PRINCE note).
  - **Persona lifecycle**: the specific claim that the *personas themselves*
    should evolve from synthetic (dev) to stakeholder-validated (UAT) is new;
    prior sources discuss evaluation strategy evolving by phase but not the
    persona artifact itself evolving.

## Guide Impact

- **Chapter 05 (Evaluation & Continuous Improvement)**: Add the three-layer
  evaluation architecture (persona-based testing / functional unit evals /
  operational observability) as a named organizing framework, positioned
  alongside the existing LangChain agent-improvement-flywheel content. The
  guide currently has strong coverage of the unit-eval and observability
  layers (via the LangChain and PRINCE notes) but no dedicated treatment of
  persona-based multi-turn simulation as its own category — add this as a
  new subsection with the Snowglobe/Collinear/Rhesis tool pointers flagged
  as unverified landscape references (per Claim 8's confidence caveat), not
  as vetted recommendations.
- **Chapter 05**: Add the four-step implementation roadmap (Claim 9) as
  concrete "how much should I have automated by which stage" guidance —
  the ~20%-automated-at-launch figure is a useful expectation-setter for
  teams intimidated by the idea of needing a complete eval suite before
  shipping.
- **Chapter 05**: Add the RAG-vs-prompt-engineered evaluation metric split
  (Claim 4) as explicit guidance for choosing which metrics apply to which
  system architecture, cross-referenced against PRINCE's concrete RAGAS
  implementation as the worked example.
- **Chapter 06 (Observability)**: Cross-reference the operational
  observability tool list (LangSmith, Langfuse, Helicone) alongside the
  existing PRINCE case study's Langfuse-based tracing implementation, to
  give readers a broader (if unverified beyond ragas/Langfuse) sense of the
  vendor landscape for production agent tracing.

## Extraction Notes

- The source is a short, framework-style consultancy blog post. The default
  WebFetch pass returned a paraphrased summary rather than verbatim text
  (consistent with prior extractions in this corpus, e.g.
  `blog-hamel-eval-smell.md` and `blog-langchain-better-harness.md`); two
  follow-up passes explicitly requesting short (<40 word), verbatim,
  quotation-marked sentences per named topic were used to obtain the quotes
  above. Quotes were cross-checked for consistency across the two passes.
- No sub-pages or linked posts were followed — the article is short
  (framework-overview length) and self-contained; it does not link out to
  deeper technical posts the way the Osmani or LangChain series posts do.
- The author's professional bio/title was not surfaced in the fetched
  content beyond the byline ("By Akshay Anand"); Source Context above
  reflects only what could be verified from the fetched article and general
  knowledge of Thoughtworks as a firm, not an independently verified author
  bio.
- Two Prospector triage comments were filed on the issue with substantially
  overlapping guidance (three-layer architecture, lifecycle evolution,
  RAG vs. prompt distinction, tool ecosystem); both are addressed above.
  The second comment's suggested overlap candidates
  (`blog-addyosmani-code-agent-orchestra.md`,
  `blog-anthropic-agent-view-claude-code.md`) were checked directly — neither
  covers evaluation methodology (the orchestra post covers orchestration and
  verification-as-bottleneck generally; the agent-view post covers a CLI
  session-management UI) — so no cross-reference to either was included
  above; the closer, more substantively overlapping matches turned out to be
  the LangChain evaluation-flywheel posts and the PRINCE RAG case study,
  found via a corpus-wide search for evaluation-related terms rather than
  from the triage comments' suggestions.
- No contradiction with any existing source note was identified; none filed.
