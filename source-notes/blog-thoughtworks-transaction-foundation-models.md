---
source_url: https://www.thoughtworks.com/insights/articles/power-of-transaction-foundation-models-building-the-unified-intelligence-layer-for-payments
source_type: blog-post
title: "The power of Transaction Foundation Models: Building the unified intelligence layer for payments"
author: Alla Gancz, Sid Sengupta, Artiom Troyanovsky, Nathan Hilt (Thoughtworks)
date_published: 2026-06-02
date_extracted: 2026-07-01
last_checked: 2026-07-01
status: current
confidence_overall: emerging
issue: "#1385"
---

# The power of Transaction Foundation Models: Building the unified intelligence layer for payments

> Thoughtworks vendor-neutral case for Transaction Foundation Models (TFMs) — domain-specific
> foundation models trained on payment/transaction event streams to replace many task-specific
> fraud, credit-risk, and personalization models with one shared, reusable representation layer —
> backed by named industry evidence (Mastercard LTM, Revolut PRAGMA, Stripe Radar, Adyen Uplift)
> and an explicit warning that the architecture only pays off with governance, business ownership,
> and disciplined delivery already in place.

## Source Context

- **Type**: blog-post (Thoughtworks Insights article; vendor-neutral consultancy, not tied to a
  single foundation-model vendor)
- **Author credibility**: Four named Thoughtworks contributors (Alla Gancz, Sid Sengupta, Artiom
  Troyanovsky, Nathan Hilt); no individual bios or titles are given in the article itself. The
  piece cites named, checkable industry evidence (Mastercard's GTC 2026 announcement with NVIDIA
  and Databricks; Revolut's published PRAGMA results; Stripe's and Adyen's public product claims)
  rather than relying solely on author authority, which raises credibility above an unsupported
  opinion piece. Thoughtworks has a commercial incentive to promote consulting engagements around
  this architecture pattern (the article ends with a "Get started" / contact-us call to action
  and a co-branded "Scaling transaction foundation models with NVIDIA and Thoughtworks" section).
- **Scope**: Covers the technical definition of a TFM, the fragmentation problem it addresses, a
  maturity map from fragmented models to a unified intelligence layer, five claimed benefits, a
  seven-layer implementation architecture, named production/industry examples, a recommended
  starting use case (fraud), and required organizational/governance preconditions. Does not cover
  training cost, infrastructure spend, model size, latency numbers, or a first-party account of
  Thoughtworks's own deployment (the named examples — Mastercard, Revolut, Stripe, Adyen — are
  reported second-hand, not Thoughtworks engagements). No sub-pages were followed; the "Related
  content" and NVIDIA-partnership sections point to Thoughtworks marketing pages, not additional
  substantive technical content.

## Extracted Claims

### Claim 1: A Transaction Foundation Model is defined as a model trained on large-scale transaction/event data to learn generalizable patterns in money movement, customer behavior, merchant operations, and risk
- **Evidence**: Direct definitional statement early in the article.
- **Confidence**: emerging (a named architectural category being actively marketed and adopted,
  not yet a settled industry standard)
- **Quote**: "A transaction foundation model is an AI model trained on large volumes of financial
  transaction and event data so it can learn patterns in how money moves, how customers behave,
  how merchants operate and how risk emerges across the ecosystem."
- **Our assessment**: This is the same "foundation model" pattern (pretrain broadly, adapt
  downstream) applied to a new modality — transaction event sequences instead of text or images.
  The definition is precise enough to be useful: it names four things the model must learn
  (money movement, customer behavior, merchant behavior, risk emergence), which gives a concrete
  bar for evaluating whether a given system actually qualifies as a TFM versus a rebranded
  task-specific classifier.

### Claim 2: The "unified intelligence layer" is a shared representation reused across many downstream use cases, replacing per-task feature pipelines
- **Evidence**: Direct definitional statement paired with the "gap they fill" framing.
- **Confidence**: emerging
- **Quote**: "It's a shared representation layer that can be reused across many use cases."
- **Quote**: "Data is fragmented across products and platforms" and "Models are often
  task-specific."
- **Our assessment**: The core architectural claim is a consolidation move: instead of N
  independent models each with their own feature engineering pipeline (one for fraud, one for
  credit risk, one for personalization), a single pretrained backbone produces embeddings that
  each downstream task adapts. This is the same "build once, adapt many times" argument used for
  general-purpose foundation models, applied at the level of a single institution's transaction
  data rather than the internet-scale text corpus.

### Claim 3: TFMs learn the "language of money movement" by analogy to how language models learn patterns in text
- **Evidence**: Explicit analogy drawn in the article to explain the TFM concept to a
  non-specialist audience.
- **Confidence**: emerging (illustrative analogy, not a technical equivalence claim)
- **Quote**: "In simple terms, a transaction foundation model learns the 'language of money
  movement'. Just as a language model learns patterns in words, grammar, context and meaning, a
  transaction foundation model learns patterns in payment events, account behavior, merchant
  categories, transaction amounts, timing, channels, devices, balances, customer journeys and
  network relationships."
- **Our assessment**: This is a marketing-friendly analogy rather than a technical claim about
  shared architecture, though the underlying mechanism (sequence modeling over discrete tokenized
  events, analogous to tokenized text) is a real and separately-verifiable technical similarity —
  the article's own seven-layer pipeline includes an explicit "transaction tokenisation" step
  that mirrors LLM tokenization.

### Claim 4: Five claimed benefits of the unified intelligence layer approach — better performance, faster reuse, improved data leverage, stronger scalability, and strategic differentiation
- **Evidence**: Structured list of five named benefits, each with a supporting sentence.
- **Confidence**: emerging (vendor-consultancy framing; benefits are asserted, not independently
  measured in this article — see Claim 6/7 for the separately-sourced production evidence)
- **Quote** (performance): "By learning from broader transaction and event histories, these
  models can identify signals that narrow models may miss."
- **Quote** (reuse): "A shared model backbone reduces duplication. Teams can adapt existing
  embeddings rather than build every model and feature set from scratch."
- **Quote** (data leverage): "Institutions can extract more value from transaction data, event
  streams and behavioral signals that already exist but are not fully used."
- **Quote** (scalability): "Instead of running disconnected AI pilots, banks can build a model
  platform that supports multiple use cases, governance patterns and delivery teams."
- **Quote** (differentiation): "Over time, the model becomes a proprietary intelligence asset. It
  reflects the institution's own transaction flows, customer relationships, operational patterns
  and risk experience."
- **Our assessment**: The "strategic differentiation" claim is the most interesting one for a
  harness-engineering audience by analogy: a well-curated, institution-specific corpus (whether
  transaction history or an organization's own codebase/docs) becomes a compounding proprietary
  asset once a model is built to exploit it — the same "compounding context" logic documented
  elsewhere in the corpus for project memory (see Cross-References), applied here to structured
  transaction data instead of conversational/document context.

### Claim 5: TFMs are built via a seven-layer pipeline — data inputs, data preparation/normalisation, transaction tokenisation, sequence modelling/training, embeddings/representation learning, downstream use-case adaptation, and production deployment/monitoring/governance
- **Evidence**: Numbered list of implementation layers presented as the recommended technical
  approach.
- **Confidence**: emerging (a prescriptive framework from a consultancy, not validated against a
  named production deployment in this article)
- **Quote**: The layers are named in sequence as "Data inputs," "Data preparation and
  normalisation," "Transaction tokenisation," "Sequence modelling and model training,"
  "Embeddings and representation learning," "Downstream use case adaptation," and "Production
  deployment, monitoring and governance."
- **Our assessment**: The pipeline is a direct structural transplant of the standard LLM
  pretrain-then-adapt pipeline (tokenize → sequence-model → embed → fine-tune/adapt →
  deploy-and-monitor) onto transaction data. The article does not elaborate each layer with
  supporting detail beyond the names themselves, so this claim is best read as an architectural
  checklist rather than a validated methodology.

### Claim 6: Named production deployments show large, but unevenly distributed, gains from transaction-model approaches — Mastercard LTM, Revolut PRAGMA, Stripe Radar, Adyen Uplift
- **Evidence**: Four named, checkable industry examples with specific metrics, cited as external
  evidence rather than Thoughtworks's own work.
- **Confidence**: emerging (each figure is a vendor's own reported metric, not independently
  audited by Thoughtworks or by us; still, these are named companies with publicly attributable
  claims, which is stronger evidence than an anonymized case study)
- **Quote**: "Mastercard's Large Transaction Model (LTM), announced at GTC 2026 in partnership
  with NVIDIA and Databricks, was trained on billions of anonymized transactions and is framed by
  Mastercard as an insights engine spanning payments, cybersecurity, personalization and
  commerce."
- **Quote**: "Revolut's PRAGMA model- trained on 26 million user records, 24 billion events and
  207 billion tokens across 111 countries- delivered a 130.2% improvement in credit scoring,
  64.7% improvement in external fraud recall and 40.5% improvement in product recommendation from
  a single pre-trained backbone."
- **Quote**: "Stripe Radar, trained on more than $1.9 trillion of annual payment volume, reduces
  fraud by 32% on average."
- **Quote**: "Adyen Uplift reported conversion uplift of up to 6%, cost reductions of up to 5% and
  an 86% reduction in manual risk rules across 60 enterprise pilots."
- **Our assessment**: Revolut's PRAGMA figures are the strongest evidence in the article because
  they name a single pretrained backbone driving three distinct downstream metrics simultaneously
  (credit scoring, fraud recall, recommendation) — direct empirical support for the "reuse across
  use cases" claim in Claim 2, rather than just an assertion. The 207-billion-token figure is also
  the most concrete scale indicator in the source. Stripe and Adyen figures describe narrower,
  task-specific products (fraud scoring, risk-rule automation) and don't by themselves establish
  that those products are built on a shared multi-task backbone the way PRAGMA is described.

### Claim 7: TFM benefits are uneven across tasks — anti-money-laundering performance was weaker than baseline in at least one case, and the article explicitly warns the benefits are not automatic
- **Evidence**: Direct caveat sentences distinguishing this article from unqualified vendor
  hype.
- **Confidence**: emerging
- **Quote**: "Some tasks showed very strong improvements, while anti-money laundering performance
  was weaker against the baseline."
- **Quote**: "The benefits are not automatic. Transaction foundation models require strong data
  foundations, thoughtful architecture, rigorous governance, clear business ownership and
  disciplined delivery."
- **Our assessment**: This is the single most important claim in the source for guide purposes —
  it directly qualifies every benefit claim above. The AML underperformance detail is notable
  because it's a specific negative result reported alongside the positive ones, which is unusual
  for vendor/consultancy content and increases the credibility of the piece as a whole. It implies
  TFMs are not a uniform upgrade: task domains with rarer, more adversarial, or more
  regulation-driven patterns (AML) may not benefit as much from a shared general-purpose
  representation as task domains with abundant, densely-labeled behavioral signal (fraud, credit
  scoring).

### Claim 8: Fraud detection is recommended as the ideal starting use case for a first TFM deployment because it is urgent, data-rich, and measurable
- **Evidence**: Explicit prescriptive recommendation with stated rationale.
- **Confidence**: emerging
- **Quote**: "For many institutions, fraud is the right starting point. It is urgent, data-rich
  and measurable."
- **Our assessment**: This is a concrete, transferable selection criterion for choosing a pilot
  use case when adopting any new AI architecture, not just TFMs specifically: pick the use case
  that is urgent (organizational pressure to act), data-rich (enough signal to train/validate
  against), and measurable (a clear before/after metric exists). This generalizes the same
  "start with a well-scoped, measurable pilot" logic seen elsewhere in the corpus for agentic
  coding tool adoption, applied here to domain-specific ML model adoption.

### Claim 9: Regulated financial deployment requires explainability, resilience, latency control, and auditability to matter as much as predictive accuracy
- **Evidence**: Direct statement on production constraints specific to regulated environments.
- **Confidence**: emerging
- **Quote**: Explainability, resilience, latency and control "matter as much as predictive
  accuracy" in regulated environments, per the article's discussion of production deployment
  requirements — full sentence not independently re-confirmed verbatim in a single extraction
  pass (see Extraction Notes).
- **Our assessment**: This is the standard "accuracy is necessary but not sufficient in regulated
  domains" argument, but stated specifically in terms that echo `blog-anthropic-kepler-verifiable-ai-financial.md`'s
  architectural provenance argument: a financial-services model needs a story for why a decision
  was made, not just what the decision was, and that story has to hold up under audit.

### Claim 10: Most institutions will adopt TFMs incrementally, moving toward hybrid systems that combine foundation-model embeddings with graph intelligence, rules, decision engines, and human oversight — not a single-step replacement of existing models
- **Evidence**: Direct statement from the "maturity map" section describing the expected adoption
  path.
- **Confidence**: emerging
- **Quote**: "Most institutions will not move to transaction foundation models in one step."
- **Quote**: The future state is described as combining "foundation model embeddings, graph
  intelligence, rules, decision engines and human oversight."
- **Our assessment**: This caveats the "unified intelligence layer replaces everything" framing
  implied by the article's title. The realistic end-state described is additive/hybrid, not a
  wholesale replacement of rules engines and human review — TFM embeddings become one more input
  layer feeding existing decision infrastructure, alongside graph models and rule systems, rather
  than a standalone replacement for them.

## Concrete Artifacts

### Seven-layer TFM implementation pipeline (from article, "How to get started" section)

```
Transaction Foundation Model — Implementation Layers
Source: Thoughtworks, "The power of Transaction Foundation Models" (June 2026)

1. Data inputs
2. Data preparation and normalisation
3. Transaction tokenisation
4. Sequence modelling and model training
5. Embeddings and representation learning
6. Downstream use case adaptation
7. Production deployment, monitoring and governance

Note: the article lists these as section/step headings without elaborating
each with a supporting sentence — treat as an architectural checklist, not
a validated step-by-step methodology.
```

### Named industry evidence table (from article)

```
Named TFM / transaction-model deployments cited in the article
Source: Thoughtworks, "The power of Transaction Foundation Models" (June 2026)

Mastercard LTM (Large Transaction Model):
  - Announced GTC 2026, partnership with NVIDIA and Databricks
  - Trained on billions of anonymized transactions
  - Framed as an insights engine spanning payments, cybersecurity,
    personalization, and commerce

Revolut PRAGMA:
  - 26 million user records, 24 billion events, 207 billion tokens,
    111 countries
  - Single pretrained backbone driving three downstream metrics:
    +130.2% credit scoring, +64.7% external fraud recall,
    +40.5% product recommendation

Stripe Radar:
  - Trained on >$1.9 trillion annual payment volume
  - Reduces fraud by 32% on average

Adyen Uplift:
  - Up to 6% conversion uplift, up to 5% cost reduction,
    86% reduction in manual risk rules
  - Across 60 enterprise pilots

Caveat stated in same article: "Some tasks showed very strong
improvements, while anti-money laundering performance was weaker
against the baseline."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-kepler-verifiable-ai-financial.md` — Both sources argue that regulated
    financial AI deployments require architectural attention to auditability/explainability
    beyond raw predictive accuracy (Claim 9 here vs. Kepler's provenance-by-architecture thesis).
    Kepler documents this for an LLM-reasoning system; this source documents the same requirement
    for a domain-specific transaction model, suggesting the "accuracy is not sufficient in
    regulated finance" constraint holds across both LLM-based and traditional-ML-based financial
    AI systems.
  - `blog-anthropic-fong-finance-narrative.md` — Not a direct methodological overlap (Fong
    describes a human practitioner using Claude for narrative work; this source describes
    training domain-specific models on transaction data), but both are finance-domain sources
    the corpus can pair to show two distinct classes of "AI in finance" claims: model-training
    pattern here vs. tool-usage pattern there.

- **Contradicts**: None found. No existing source note makes a competing claim about
  domain-specific transaction/foundation-model architecture that this source disagrees with.

- **Extends**: This is the first corpus source to document a domain-specific (non-LLM-agent)
  foundation model pattern — training a proprietary foundation model on an institution's own
  structured event data, rather than using a general-purpose LLM as an agent or assistant. It
  extends the corpus's general "foundation model" vocabulary (pretrain-then-adapt) into a new
  data modality (transaction event sequences) and a new deployment mode (an internally-trained,
  institution-owned model rather than a hosted LLM API).

- **Novel**:
  - The "Transaction Foundation Model" (TFM) category itself, and its definitional framing
    (learns "the language of money movement") — not present in any prior corpus source.
  - The seven-layer TFM implementation pipeline as a named architectural checklist.
  - The four named production benchmarks (Mastercard LTM, Revolut PRAGMA, Stripe Radar, Adyen
    Uplift) with specific metrics — first corpus appearance of any of these.
  - The explicit negative result (AML underperformance) reported alongside positive results —
    a rare "here's where this doesn't work" admission in a vendor/consultancy source, not seen
    in comparably promotional sources elsewhere in the corpus.
  - "Fraud is the right starting point: urgent, data-rich, measurable" as a named three-part
    pilot-use-case selection criterion — this specific triad framing (urgency + data richness +
    measurability) is new to the corpus, though the underlying "pick a well-scoped measurable
    pilot" idea is a common adoption pattern elsewhere.

## Guide Impact

- **Ch04 (Context Engineering)**: The "strategic differentiation" claim (Claim 4) — that a
  model trained on an institution's own proprietary data becomes a compounding intelligence asset
  — is a domain-specific instance of the general "compounding context" argument the guide already
  makes about project memory (`blog-anthropic-fong-finance-narrative.md` Claim 8: "project memory
  gets richer every pass"). Worth a cross-domain callout: the compounding-proprietary-context
  argument applies whether the substrate is conversational project memory or a purpose-trained
  transaction model.

- **Ch02 (Harness Engineering)**: The seven-layer implementation pipeline (Claim 5, Concrete
  Artifacts) is a useful analogy for readers building any domain-specific model/harness on top of
  structured internal data: tokenize the domain's events, sequence-model them, produce reusable
  embeddings, then adapt per downstream task. This is presented as an illustrative parallel, not
  as guidance to adopt TFMs specifically — the guide's scope is agentic coding harnesses, and this
  source is about a different model category (domain-specific transaction models, not
  general-purpose coding LLMs).

- **Ch05/Ch06 (Team Adoption / Security & Threat Model)**: Claim 8 ("fraud is the right starting
  point: urgent, data-rich, measurable") and Claim 10 (incremental, hybrid adoption rather than
  wholesale replacement) both reinforce existing guide advice on choosing measurable pilots and
  expecting AI systems to augment rather than replace existing decision infrastructure in
  regulated or high-stakes domains. Claim 7's explicit warning ("the benefits are not automatic";
  uneven task-level gains) supports guide language cautioning against assuming uniform ROI from
  a new model architecture without governance and delivery discipline already in place.

## Extraction Notes

- This source is outside the guide's core scope (agentic coding harnesses) — it concerns
  training domain-specific foundation models on transaction data for banking/payments, not LLM
  coding agents. Extraction treats it as a domain-specific parallel/analogy source per the
  Prospector's triage guidance, not as a direct harness-engineering case study. Guide Impact
  recommendations above are scoped accordingly (illustrative cross-domain parallels, not adoption
  guidance for TFMs themselves).
- All quotes were extracted via multiple targeted WebFetch passes against the live article, each
  scoped to a specific section (definition, benefits, pipeline, industry evidence, fraud
  starting-point, governance caveats, maturity map). Quotes in Claims 1–8 and 10, and the Concrete
  Artifacts section, were confirmed verbatim in their respective extraction pass.
- Claim 9's quote could not be independently re-confirmed as a single verbatim sentence across
  extraction passes (the fetching tool paraphrased it consistently as "matter as much as
  predictive accuracy" without reproducing full surrounding sentence structure); it is flagged
  as such in the claim and should be treated as a paraphrase-adjacent quote rather than a fully
  verified one.
- The article's full section structure (11 headings, ~2,500+ words) was identified via a
  dedicated structural pass; no sub-pages were followed because the "Related content" and
  NVIDIA-partnership links point to Thoughtworks marketing/contact pages rather than additional
  substantive technical content.
- No contradiction with existing source notes was found; none filed.
- Confidence overall set to "emerging": the TFM category is real and has named, checkable
  production evidence (Mastercard, Revolut, Stripe, Adyen), but the claims are vendor/consultancy-
  reported rather than independently benchmarked, and the article itself flags uneven results
  (AML) — not yet a settled pattern.
