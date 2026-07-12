---
source_url: https://www.thoughtworks.com/insights/articles/how-to-build-transaction-foundation-models-in-banking-and-payments
source_type: blog-post
title: "How to build transaction foundation models in banking and payments"
author: Alla Gancz, Brian Blanchard, Artiom Troyanovsky, Dr. Jochen Papenbrock, Georgios Kolovos, Bilal Jaffery (Thoughtworks)
date_published: 2026-06-19
date_extracted: 2026-07-12
last_checked: 2026-07-12
status: current
confidence_overall: emerging
issue: "#1776"
---

# How to build transaction foundation models in banking and payments

> A six-author Thoughtworks technical guide describing transaction foundation
> models (TFMs) — decoder-only transformers trained on transaction sequences
> to produce reusable embeddings — as a shared intelligence layer for fraud,
> credit, operations, and personalization, with a concrete tokenization
> strategy, an NVIDIA/AWS reference tech stack, and a 3-day/3-week/3-month
> build timeline.

## Source Context

- **Type**: blog-post (Thoughtworks Insights technical guide, published
  June 19, 2026; auto-discovered via the trusted `thoughtworks` RSS feed)
- **Author credibility**: Six named co-authors, including Dr. Jochen
  Papenbrock, who is presented as the senior technical authority in the
  Prospector's triage assessment. No individual author bios, titles, or
  credentials are given in the article body itself — the byline is a flat
  list of six names with no role attribution. Thoughtworks is an established
  vendor-neutral consultancy already represented extensively in this corpus
  (16 prior `blog-thoughtworks-*` notes). This is a prescriptive technical
  guide, not a client case study: it contains no named client, no production
  deployment metrics, and no reported outcomes from a real institution. The
  one external metric cited (~88% data-processing cost saving) is attributed
  to a third-party NVIDIA publication, not to Thoughtworks' own work.
- **Scope**: Covers the concept and rationale for transaction foundation
  models, a five-step build process (business-problem selection, data
  preparation, tokenization, transformer training, embedding generation/
  serving), a nine-layer reference architecture (named but not itemized in
  the article text), a recommended NVIDIA/AWS technology stack, a hybrid
  decisioning architecture (TFM + graph models + rules + human review), and
  a 3-day/3-week/3-month phased build timeline. Does NOT cover: any named
  institution's actual production deployment, accuracy/precision/recall
  numbers for a working TFM, cost or infrastructure-spend figures beyond the
  single cited NVIDIA benchmark, model size or training-data-volume
  specifics, or a full enumeration of the nine architecture layers (the
  article names the "nine layers" framing but only describes functional
  groupings — data, tokenization, model training/serving, decisioning,
  governance — in prose).

## Extracted Claims

### Claim 1: A transaction foundation model replaces per-use-case feature pipelines with one shared, reusable representation of transaction behavior
- **Evidence**: The article's opening framing, contrasting the TFM approach
  against building "a separate feature pipeline and model for every problem."
- **Confidence**: emerging
- **Quote**: "Instead of building a separate feature pipeline and model for every problem (fraud, credit, authorization, reconciliation, customer engagement, liquidity forecasting), an institution can build one shared representation of transaction behavior and reuse it across many models and workflows."
- **Our assessment**: This is the article's central architectural thesis and
  the concept the rest of the note extends. It is a specific, testable claim
  about ROI structure (amortizing one representation-learning investment
  across N downstream use cases) rather than a general "AI helps banking"
  statement. The claim is plausible in principle — representation learning
  amortized across tasks is a well-established idea outside banking — but
  the article gives no evidence from an actual multi-use-case deployment
  that the amortization has been realized; it is presented as the
  motivating design goal, not a measured outcome.

### Claim 2: Point-in-time correctness — training and evaluating the model as if replaying real-world decision timing — is a required property for payments transaction data, not an optional refinement
- **Evidence**: Direct statement in the data-preparation step of the build
  process.
- **Confidence**: settled (this is a standard, well-established requirement
  in time-series/sequential financial modeling, not a novel claim specific
  to this article — but it is stated here as a concrete build-process step)
- **Quote**: "In payments, time matters — the model must be trained and evaluated in a way that reflects how decisions would have been made in the real world (point-in-time correctness)."
- **Our assessment**: This is a well-known constraint in financial ML
  (avoiding label leakage from future information), restated here as a
  named checklist item for TFM builders specifically. Its inclusion signals
  that the guide is written for practitioners who may not come from a
  quantitative-finance background and need the constraint spelled out
  explicitly, rather than assuming it as background knowledge.

### Claim 3: Effective tokenization of transaction data requires domain-specific strategies per field type — log-spaced bucketing for amounts, granularity-matched time-delta tokens, and top-K/hashing/embedding-table approaches for high-cardinality fields
- **Evidence**: A three-part prescriptive rule set for the tokenization
  build step, one rule per field category.
- **Confidence**: emerging
- **Quote**: "Amount fields: Bucket using log-spaced or decile thresholds; never feed raw values. Time-delta tokens: Choose a granularity (minutes for fraud, days for credit) that matches the downstream task. High-cardinality fields (merchant ID, counterparty, device): Use top-K + UNK, hashing or learned embedding tables."
- **Our assessment**: This is the single most concrete, reusable technical
  artifact in the source — a practitioner could apply these three rules
  directly. The task-dependent granularity point (minutes for fraud vs.
  days for credit) is the most actionable detail: it explicitly ties
  tokenization design to the downstream use case rather than treating
  tokenization as a one-size-fits-all preprocessing step, which matters
  for the "one shared representation, many use cases" thesis in Claim 1 —
  if granularity must vary by use case, the "one shared representation"
  claim may need qualification (a single TFM might need per-use-case
  tokenization variants rather than being fully use-case-agnostic). The
  article does not address this tension directly.

### Claim 4: Frozen embeddings are simpler to govern than fine-tuned embeddings, but fine-tuned embeddings deliver more performance lift per downstream task
- **Evidence**: A direct governance/performance trade-off statement in the
  embedding-generation build step.
- **Confidence**: emerging
- **Quote**: "Frozen vs fine-tuned: Frozen embeddings are simpler to govern; fine-tuned embeddings give more lift per downstream task."
- **Our assessment**: This is a governance-vs-performance trade-off stated
  as a bare assertion with no supporting data (no lift magnitude, no
  governance-cost comparison). It is directionally plausible — a single
  frozen embedding space is easier to audit and version than N per-task
  fine-tuned variants — but the article gives practitioners no guidance on
  where the trade-off point lies (e.g., how much lift justifies the added
  governance burden of fine-tuning). Treat as a named consideration to
  weigh, not a resolved recommendation.

### Claim 5: The reference TFM training approach uses a decoder-only transformer trained with causal language modeling to predict what happens next in a transaction sequence
- **Evidence**: Direct description of the NVIDIA reference training
  methodology cited in the article.
- **Confidence**: emerging
- **Quote**: "The NVIDIA reference uses NeMo AutoModel to train a decoder-only transformer with causal language modeling — the model learns what tends to happen next in a transaction sequence."
- **Our assessment**: This positions TFM training as directly analogous to
  autoregressive next-token LLM pretraining, but applied to transaction
  events instead of text tokens. The claim is architecturally specific
  (decoder-only + causal LM, not e.g. a masked/bidirectional encoder or a
  contrastive/dual-encoder embedding approach) and attributed to a named
  vendor reference implementation (NVIDIA), not to Thoughtworks' own
  independent validation — the article does not report training this
  itself or compare it against alternative architectures.

### Claim 6: Generated transaction embeddings are stored in a vector database and served through a shared embedding service, letting fraud, credit, operations, and personalization teams consume the same intelligence layer
- **Evidence**: Direct description of the embedding-serving build step.
- **Confidence**: emerging
- **Quote**: "The embeddings are stored in a vector database and served through an embedding service. From this point on, fraud, credit, operations and personalization teams all consume the same intelligence layer."
- **Our assessment**: This is the concrete infrastructure instantiation of
  Claim 1's "one shared representation" thesis — a vector database plus an
  embedding service is the specific architectural mechanism, not just an
  abstract goal. As with Claim 1, the article presents this as the intended
  design rather than a validated production pattern with named consumer
  teams actually operating on shared embeddings.

### Claim 7: Fraud detection is recommended as the first TFM use case because its value case is directly quantifiable through standard operational metrics
- **Evidence**: Direct rationale statement for use-case selection.
- **Confidence**: emerging
- **Quote**: "Fraud detection is often a strong starting point because the value case can be quantified through fraud loss, recall, precision, false positives, manual review volumes and decision latency."
- **Our assessment**: This is a specific, checkable selection criterion
  (quantifiability of value via six named metrics) rather than a vague
  "fraud is important" claim. It implies a general prioritization heuristic
  for TFM rollout — pick the first use case where success is measurable
  along multiple pre-existing operational dimensions — that is transferable
  beyond fraud to any first-use-case-selection decision for a new
  intelligence layer.

### Claim 8: TFM-based decisioning should be hybrid — combining TFM embeddings, graph models, gradient-boosted models, hard rules, and human case-team review — because a TFM augments rather than replaces existing controls
- **Evidence**: Direct architectural recommendation, with an explanation of
  what each component in the hybrid stack contributes.
- **Confidence**: emerging
- **Quote**: "The best architecture is therefore hybrid. A TFM does not replace every existing rule, model or decision engine; it augments them. The strongest pattern combines TFM embeddings, graph intelligence, gradient-boosted models, hard rules, case-team feedback and human review."
- **Quote**: "The combination matters most for fraud and scams: TFMs capture behavioral and temporal patterns, graph models capture relationships across accounts, devices, beneficiaries and merchants, rules enforce hard controls and case teams provide the feedback that keeps the model honest over time."
- **Our assessment**: This is the article's clearest regulated-domain
  design principle, and it names a specific division of labor across five
  distinct component types rather than a generic "keep a human in the
  loop" caveat. It corroborates a pattern already established in this
  corpus for regulated financial AI (see Cross-References) that a single
  model — however capable — should not be the sole decision-maker; the
  novel contribution here is the specific combination for fraud/scams
  (TFM for behavior/timing, graph models for relationships, rules for hard
  limits, case teams for the feedback loop).

### Claim 9: Production TFM systems in banking/payments must satisfy five non-negotiable operational requirements — explainability, resilience, latency discipline, continuous monitoring, and governance
- **Evidence**: A direct enumerated list of requirements tied to specific
  regulatory/operational rationales for each.
- **Confidence**: emerging
- **Quote**: "They need explainability because decisions affect customers, merchants and financial outcomes. They need resilience because payments operate 24/7. They need latency discipline because fraud and authorization decisions happen in milliseconds. They need monitoring because fraud patterns, customer behavior and payment flows change continuously. They need governance because data privacy, fairness, security and auditability are non-negotiable."
- **Our assessment**: Each requirement is paired with a specific rationale
  rather than left as an unexplained checklist item, which makes this more
  actionable than a generic "AI systems need governance" statement. The
  latency-discipline item (milliseconds, tied explicitly to fraud/
  authorization decisions) is the most concrete and domain-specific of the
  five; the others (explainability, resilience, monitoring, governance) are
  general regulated-AI requirements already well-represented elsewhere in
  this corpus.

### Claim 10: A TFM build should proceed in three phases of escalating scope and duration — a 3-day concept phase, a 3-week prototype phase, and a 3-month production/pathfinder phase
- **Evidence**: Direct description of the phased implementation timeline,
  with specific activities named for each phase.
- **Confidence**: emerging
- **Quote**: "In a 3-day concept phase, identify the priority use case, define the scope, assess data readiness and shape the value case. In a 3-week prototype phase, build a working pipeline using real or representative data. Tokenize transactions, train or adapt a model, generate embeddings and compare performance against the current baseline. In a 3-month MLP phase, harden the capability for production or controlled pathfinder deployment."
- **Our assessment**: This is a specific, named timeline (using "MLP" —
  minimum lovable/loveable product, a Thoughtworks house term — for the
  final phase) that gives practitioners a concrete planning scaffold. As
  with the rest of the article, no evidence is given that any institution
  has actually completed this timeline in practice; it reads as a
  recommended planning template rather than a reported delivery outcome.
  The "3-week prototype includes training or adapting a model AND
  comparing against baseline" scope is notably aggressive relative to
  typical ML project timelines and is not defended with an example.

### Claim 11: The recommended TFM technology stack is built on a specific NVIDIA GPU-acceleration toolchain — CUDA-X for data/graph operations, NeMo/Megatron-Core/TransformerEngine for training, and NIM/Dynamo-Triton/TensorRT-LLM/NeMo Retriever for production embedding serving — with a cited ~88% data-processing cost saving over CPU
- **Evidence**: A named list of specific NVIDIA products mapped to pipeline
  stages, with one externally-sourced cost metric.
- **Confidence**: emerging (the technology mapping is a vendor-stack
  recommendation; the one quantified metric is attributed to a third-party
  NVIDIA publication, not independently measured by Thoughtworks)
- **Quote**: "NVIDIA CUDA-X (cuDF, cuML, cuGraph, CuPy): GPU-accelerated dataframes, classical ML, graph operations and tokenization." "NeMo AutoModel, Megatron-Core, TransformerEngine: Scalable training of transformer architectures" "NIM microservices, Dynamo-Triton, TensorRT-LLM, NeMo Retriever: Production embedding service"
- **Quote**: "~88% data-processing cost saving vs CPU per the published NVIDIA AI Blueprint for Financial Fraud Detection."
- **Our assessment**: This is the most vendor-specific portion of the
  article — it reads as an NVIDIA-aligned reference stack rather than a
  vendor-neutral recommendation, despite Thoughtworks' general
  vendor-neutral positioning in this corpus. The 88% cost-saving figure is
  explicitly sourced to an NVIDIA-published blueprint (not to Thoughtworks'
  own measurement or to any named bank), so it should be treated as a
  vendor benchmark claim, not an independently verified production result.

### Claim 12: For training transaction foundation models at scale, AWS SageMaker HyperPod provides distributed training infrastructure with resilient, self-healing node management and checkpoint recovery across thousands of accelerators
- **Evidence**: Direct description of the recommended distributed-training
  infrastructure for large TFMs.
- **Confidence**: emerging
- **Quote**: "For training large transaction models at scale, Amazon SageMaker HyperPod provides distributed training across thousands of accelerators with resilient, self-healing infrastructure, node management, checkpoint recovery, and long-running job support."
- **Our assessment**: This is an infrastructure-layer recommendation
  parallel to Claim 11's NVIDIA software stack, but from a different vendor
  (AWS) for a different concern (distributed training orchestration rather
  than GPU-accelerated data/model operations). Like Claim 11, this is a
  vendor-capability description rather than a reported outcome from a named
  TFM training run — the article gives no accelerator count, training
  duration, or checkpoint-recovery incident that was actually handled by
  HyperPod in this context.

## Concrete Artifacts

```
Source: Thoughtworks, "How to build transaction foundation models in
banking and payments," June 19, 2026

MINIMUM VIABLE TRANSACTION DATASET (data-preparation step):
"The minimum dataset includes transaction amount, timestamp, merchant or
counterparty, transaction type, channel, currency, customer or account
identifier and outcome labels."

TOKENIZATION RULES (per field type):
  Amount fields       -> log-spaced or decile bucket thresholds (never raw values)
  Time-delta tokens    -> granularity matched to task (minutes: fraud, days: credit)
  High-cardinality     -> top-K + UNK, hashing, or learned embedding tables
                          (merchant ID, counterparty, device)
  Tokenizer principle: "A good tokenizer balances domain meaning, privacy,
                        scale and model efficiency."

NVIDIA REFERENCE STACK (by pipeline stage):
  Data/graph ops   -> CUDA-X: cuDF, cuML, cuGraph, CuPy
  Model training   -> NeMo AutoModel, Megatron-Core, TransformerEngine
  Embedding serving -> NIM microservices, Dynamo-Triton, TensorRT-LLM, NeMo Retriever
  Cited benchmark  -> ~88% data-processing cost saving vs. CPU
                      (source: NVIDIA AI Blueprint for Financial Fraud Detection)

AWS DISTRIBUTED TRAINING:
  Amazon SageMaker HyperPod — distributed training across thousands of
  accelerators; resilient/self-healing infrastructure, node management,
  checkpoint recovery, long-running job support.

HYBRID DECISIONING STACK (fraud/scams):
  TFM embeddings        -> behavioral and temporal patterns
  Graph models           -> relationships across accounts, devices, beneficiaries, merchants
  Gradient-boosted models + hard rules -> enforce hard controls
  Case teams / human review -> ongoing feedback that "keeps the model honest over time"

BUILD TIMELINE:
  3-day concept phase   -> identify priority use case, define scope, assess data
                           readiness, shape value case
  3-week prototype phase -> build working pipeline; tokenize, train/adapt model,
                            generate embeddings, compare vs. current baseline
  3-month MLP phase      -> harden for production or controlled pathfinder deployment

PRODUCTION REQUIREMENTS (5 items, each with stated rationale):
  Explainability  -> decisions affect customers, merchants, financial outcomes
  Resilience      -> payments operate 24/7
  Latency discipline -> fraud/authorization decisions happen in milliseconds
  Monitoring      -> fraud patterns, customer behavior, payment flows change continuously
  Governance      -> data privacy, fairness, security, auditability are non-negotiable
```

## Cross-References

- **Corroborates** `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 3
  (Claude is treated as one stage in a pipeline; the surrounding
  deterministic infrastructure is as load-bearing as the model itself —
  quoted as "In finance, the model can't be the whole system"): this
  article's Claim 8 (hybrid decisioning — "A TFM does not replace every
  existing rule, model or decision engine; it augments them") is the same
  architectural principle applied to a transaction-embedding model instead
  of an LLM-reasoning layer. Both sources, from different technical domains
  within financial services (LLM-based analysis pipelines vs.
  transformer-based transaction embeddings), independently converge on
  "the model is one component in a larger deterministic/rule-based system,
  not the whole decision-maker."
- **Corroborates** `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 10
  (specialized proprietary models alongside a general-purpose LLM achieve
  much higher accuracy on narrow, well-defined domain tasks — 94% vs.
  38-46% for Kepler's financial-taxonomy-mapping classifier): this
  article's recommended architecture — a domain-specific foundation model
  trained purely on transaction sequences, distinct from any general-purpose
  LLM — is a broader instantiation of the same "narrow, purpose-built model
  for a narrow, well-defined task" principle Kepler applies at classifier
  scale. Neither source provides a head-to-head accuracy comparison for
  TFMs specifically, so this is a conceptual, not quantitative,
  corroboration.
- **Extends** `blog-openai-bbva-banking-transformation.md`: BBVA's Credit
  Analysis Pro GPT (that note's Claim 7) is an application-layer LLM tool
  that extracts and analyzes unstructured data for credit-risk analysts,
  with — per that note's assessment — "no architectural detail, no mention
  of how outputs are verified before entering a credit decision, and no
  auditability claim at all." This article operates one layer below that:
  it describes how to build the underlying domain-specific representation
  (transaction embeddings) that a credit-risk or fraud application could
  consume, rather than an application built directly on a general-purpose
  LLM. The two sources describe different, complementary layers of a
  banking AI stack (embedding/representation layer here vs.
  application/tool layer in BBVA) — this article does not resolve the
  auditability gap the BBVA note identifies, since it likewise stops short
  of describing how a specific institution verified TFM-driven decisions in
  production.
- **Novel**:
  - Transaction foundation models as a named category — a decoder-only
    transformer pretrained with causal language modeling on transaction
    sequences (not text) to produce reusable embeddings — is not described
    in any prior corpus source. All prior financial-services notes in this
    corpus (Kepler, BBVA, Fong) concern general-purpose LLM (Claude/GPT)
    application patterns, not domain-specific pretraining of a new model
    architecture on proprietary transaction data.
  - The field-specific tokenization rule set (log-spaced amount buckets,
    task-matched time-delta granularity, top-K/hashing/embedding-table
    handling for high-cardinality fields) is a concrete technical artifact
    with no analog elsewhere in the corpus — prior corpus tokenization
    discussion (e.g., `blog-thoughtworks-kamelman-token-crisis.md`,
    `blog-thoughtworks-omahony-feature-token-budgets.md`) concerns LLM
    context/prompt token consumption and billing, a materially different
    concept from transformer input tokenization of structured transaction
    fields. These should not be conflated in the guide.
  - The NVIDIA (CUDA-X/NeMo/NIM/TensorRT-LLM) and AWS SageMaker HyperPod
    reference technology stack for training a domain-specific transformer
    at scale is new infrastructure detail not present in any prior corpus
    note, all of which describe consuming hosted general-purpose LLM APIs
    rather than training a custom model.
  - The 3-day/3-week/3-month phased build timeline for a from-scratch model
    build is a different kind of timeline than the adoption/rollout
    timelines documented elsewhere in the corpus (e.g., BBVA's multi-year
    pilot-to-100,000-employee rollout) — this timeline is about building
    infrastructure, not about organizational tool adoption.

## Guide Impact

- **Limited direct applicability**: The guide's current chapters (Harness
  Engineering, Verification, Context Engineering, Team Adoption, Security)
  are scoped to AI-native *software engineering* — configuring and working
  with coding agents (Claude Code and similar tools) — not to training
  domain-specific foundation models from scratch on proprietary structured
  data. This article describes an ML/data-science model-building workflow
  (pretraining a transformer on transaction sequences) that sits outside
  that scope. Most of its content (tokenization rules, NVIDIA/AWS training
  stack, embedding-serving architecture) has no direct home in the current
  guide structure and should not be forced into a chapter it does not fit.
- **Chapter 03 (Verification)**: The one transferable structural principle
  is Claim 8/9's hybrid-architecture stance — a model (any model, not just
  a coding agent) should be one layer in a system with deterministic rules,
  monitoring, and human review, not the sole decision-maker, and each
  requirement (explainability, resilience, latency discipline, monitoring,
  governance) should have a stated rationale rather than being an
  unexplained checklist item. This generalizes the guide's existing
  layered-verification thesis (Ch03's "verification stack, cheapest to
  most expensive" framing) to a non-coding-agent domain: the same
  "layers, not a single point of trust" logic applies to production ML
  decisioning systems, reinforcing that the principle is domain-general
  rather than specific to reviewing AI-generated code.
- **No recommended change to Ch02 or Ch04**: despite the Prospector's
  triage comments suggesting Ch02 relevance, Ch02 (Harness Engineering) is
  specifically about CLAUDE.md/agent-harness configuration for coding
  agents, which this article does not address at all. Ch04's tokenization
  content concerns LLM context/prompt token budgets, a different concept
  from this article's transformer-input tokenization of transaction
  fields (see Cross-References → Novel); adding this article's tokenization
  claims to Ch04 would conflate two unrelated meanings of "tokenization"
  and should be avoided.

## Extraction Notes

- The article was read via five targeted WebFetch passes (full-content
  synthesis, then four passes each targeting specific sections for verbatim
  quotes: introduction/authors/nine-layers framing; tokenization/embedding-
  governance/metrics/timeline; fraud-use-case/transformer-training/
  point-in-time/NVIDIA-AWS-stack; hybrid-architecture/regulatory-
  requirements/conclusion/nine-layers detail; data-preparation/embedding-
  reuse/tokenization-tradeoffs/title-date). All quotes in this note were
  confirmed verbatim in at least one targeted pass.
- The article states "A practical TFM reference architecture can be
  structured across nine layers" but the fetched text only describes
  functional groupings (data, tokenization, model training/serving,
  decisioning, governance) in prose — the nine layers appear to be named
  only in an accompanying diagram/graphic that was not extractable as text
  through WebFetch. This is flagged as a limitation: the "nine layers"
  claim is real (the article explicitly makes it) but the specific
  itemization could not be verified and is therefore NOT presented as a
  claim with a full enumerated list in this note.
- No author bios, titles, or individual role attributions were found in the
  fetched article text beyond the flat six-name byline — despite the
  Prospector's triage comment characterizing Dr. Jochen Papenbrock as "a
  senior technical authority," this note does not independently confirm
  that characterization from the article itself (it may derive from
  Papenbrock's external profile, not article content).
- No contradiction with any existing source note was identified. The
  hybrid-architecture stance (Claim 8) and production-requirements list
  (Claim 9) corroborate rather than conflict with the Kepler note's
  deterministic-execution-layer principle — both argue against a model
  being the sole decision-maker in regulated financial contexts.
- All cross-referenced claim numbers (from `blog-anthropic-kepler-
  verifiable-ai-financial.md` and `blog-openai-bbva-banking-
  transformation.md`) were verified by re-reading each cited note in full
  before writing this note's Cross-References section; none were guessed.
- No sub-pages were linked from the article requiring follow-up; the
  source is a single self-contained technical guide page.
