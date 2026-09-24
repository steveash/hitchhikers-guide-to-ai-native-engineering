---
source_url: https://openai.com/index/fyxer
source_type: blog-post
title: "How Fyxer built an AI executive assistant people trust"
author: OpenAI (customer case study, featuring Archie Hollingsworth, Co-founder, Fyxer; Joey Dwonczyk, AI/ML Product Engineer, Fyxer; and Shantsila, Fyxer — no title given in source)
date_published: 2026-09-14
date_extracted: 2026-09-24
last_checked: 2026-09-24
status: current
confidence_overall: anecdotal
issue: "#3664"
---

# How Fyxer built an AI executive assistant people trust

> An OpenAI customer case study describing how Fyxer, an AI executive-assistant
> startup, decomposes email handling into 30–50 narrow specialized models,
> fine-tunes them with supervised fine-tuning and LoRA on a 500,000+ hour
> corpus of human executive-assistant workflows, and closes the loop with a
> Direct Preference Optimization pipeline that turns every user edit to a
> draft into training signal, gated by per-change A/B tests — reporting 53%
> of drafts accepted as written and 90%+ user retention at 90 days.

## Source Context

- **Type**: blog-post (OpenAI customer case study, `openai.com/index/fyxer`,
  published September 14, 2026; ~900 words — longer and more technically
  detailed than the shorter Codex-migration case studies in the corpus, e.g.
  `blog-openai-asana-codex-case-study.md`). Structured like other OpenAI
  customer-story posts: a company metadata block (Company size: Startup,
  Region: Europe & UK, Industry: Technology, Products: API), a two-stat
  headline block, three named-practitioner pull quotes, and a numbered
  "three lessons for founders" body structure with subheadings.
- **Author credibility**: Written and published by OpenAI as promotional
  customer-success content — OpenAI has a direct commercial incentive to
  present its API and fine-tuning offering favorably, and this piece
  specifically promotes OpenAI's managed fine-tuning support. Three Fyxer
  individuals are quoted: Archie Hollingsworth (Co-founder), Joey Dwonczyk
  (AI/ML Product Engineer), and a third person referred to only by surname,
  "Shantsila" (no first name or title given anywhere in the source). No
  independent party verifies the retention, acceptance-rate, or revenue
  figures; no methodology is disclosed for how the 53% draft-acceptance or
  90% retention figures were measured (e.g., cohort definition, or whether
  trivial whitespace-only edits still count as "accepted as written").
- **Scope**: Covers Fyxer's system architecture (specialized-model
  decomposition, memory/retrieval design), training methodology (SFT + LoRA,
  managed fine-tuning, DPO from user edits, A/B-gated shipping), and headline
  business metrics (retention, draft-acceptance rate, ARR growth). Does NOT
  cover: the actual training data format, model sizes, the classifier
  architecture beyond a narrative description, how memory conflicts are
  resolved, drop-out/error-rate figures for the other 47% of drafts, or any
  account of failures encountered along the way.

## Extracted Claims

### Claim 1: Fyxer decomposes email handling into 30–50 specialized models, each responsible for a narrow part of the workflow, rather than using one model to write the whole reply
- **Evidence**: Narrative description of the system architecture, attributed to Co-founder Archie Hollingsworth, under the article's first numbered lesson ("Break email into smaller jobs").
- **Confidence**: anecdotal (single company's self-reported architecture; the 30-50 count is not further broken down)
- **Quote**: "Fyxer built its system around 30–50 specialized models, each responsible for a narrow part of the email workflow. Instead of treating email as a single text-generation task, Fyxer breaks the problem into a system of predictions, like deciding whether a message requires a reply or drafting responses that match a user's tone and context."
- **Our assessment**: This is a task-decomposition-into-many-narrow-models pattern, structurally similar to (but more extreme in model count than) the single learned routing classifier in `blog-cursor-router-model-classifier.md`, which routes a coding request to one of several cost-tier models rather than decomposing the task itself into dozens of narrow predictors. Fyxer's approach is decomposition of the *task* (reply-or-not, tone, intent, scheduling) into many small models, not routing a single task to different model sizes — a distinct but related strategy for the same underlying problem (a single frontier-model call producing inconsistent, context-blind output for a highly personal task).

### Claim 2: A reply-decision model classifies each incoming email as needing a response, a scheduling action, or being purely informational, before any downstream generation happens
- **Evidence**: Narrative description of the first stage of the pipeline.
- **Confidence**: anecdotal (single-company architecture description, no accuracy figures given for this classifier specifically)
- **Quote**: "When a new email arrives, a reply decision model classifies the message: is this something that needs a response, a scheduling action, or simply information the user should see?"
- **Our assessment**: A concrete first-stage triage/classification step ahead of generation — a predict-before-you-generate gating step that keeps a downstream generative model from being invoked (and potentially producing a wrong-tone or unnecessary draft) on messages that don't need one. Useful as a specific example of task decomposition applied to an agent-adjacent (not strictly coding) domain.

### Claim 3: Fyxer's memory system uses retrieval models to compare each new email against stored interactions and surface only the memories relevant to that specific person and thread, deciding case-by-case which details persist and which are discarded after a single exchange
- **Evidence**: Narrative description under the architecture section, described as "one of the most important parts of the system."
- **Confidence**: anecdotal (architecture description; no detail on the retrieval mechanism, embedding model, or persistence-decision logic)
- **Quote**: "Memory is one of the most important parts of the system. Fyxer needs to decide which details should persist across conversations and which should disappear after a single exchange. When a new email arrives, retrieval models compare it with stored interactions and surface the memories most relevant to that person and thread."
- **Our assessment**: This is a DIY, retrieval-model-based memory architecture built from OpenAI models, in contrast to the filesystem-based, platform-managed memory layer described in `blog-anthropic-claude-managed-agents-memory.md` (Claim 2). Fyxer's design is per-person, per-thread scoped rather than the org-wide/per-user scoped-store model in that note, and explicitly frames memory retention as a per-item selective-persistence decision (keep vs. discard after one exchange) rather than a bulk session-log or dreaming-style consolidation process. This is a useful, independently-arrived-at data point that a narrow relevance-filtered retrieval design is viable for a high-volume, highly personal production memory use case — corroborating the general principle that not everything should be remembered, without describing the same mechanism Anthropic uses.

### Claim 4: Fyxer uses supervised fine-tuning and LoRA across its system to create task-specific model variants while controlling training cost, starting with OpenAI's fine-tuning platform and later moving a new checkpoint into production with OpenAI's managed fine-tuning team
- **Evidence**: Narrative description of the training methodology, naming both techniques explicitly.
- **Confidence**: anecdotal (single-company methodology description; no figures on cost savings from LoRA specifically, no detail on which of the 30-50 models use LoRA vs. full fine-tuning)
- **Quote**: "Fyxer uses supervised fine-tuning and Low-Rank Adaptation (LoRA) across its broader system to create task-specific model variants while controlling training cost. Early in the product's development, the team used OpenAI's fine-tuning platform for tasks that needed high accuracy. More recently, Fyxer worked with OpenAI's managed fine-tuning team to put a new checkpoint into production."
- **Our assessment**: This is one of the few sources in the corpus to name LoRA explicitly as a cost-control mechanism for maintaining many task-specific model variants (consistent with the 30-50 specialized models of Claim 1) rather than fully fine-tuning each one. The progression described — self-serve fine-tuning platform early, then a vendor-assisted "managed fine-tuning team" engagement later — is a concrete data point on how a startup's fine-tuning operations matured alongside its scale, and is corroborated by the direct vendor-support quote in Claim 8.

### Claim 5: Fyxer converts user edits to AI-generated drafts into training data using Direct Preference Optimization, treating the original draft and the user-edited final version as a preference pair rather than manually labeling examples
- **Evidence**: Narrative description under the third numbered lesson ("Turn user feedback into a self-training loop").
- **Confidence**: anecdotal (single-company methodology description; no figures on pair volume, training frequency, or how quickly DPO updates propagate to production)
- **Quote**: "Fyxer converts those comparisons into training data using Direct Preference Optimization (DPO). Instead of manually labeling every example, the model learns from pairs of outputs: the original draft and the user-edited version."
- **Our assessment**: The source's preceding paragraph frames the underlying signal: "When someone edits a draft before sending it, the difference between the original and final email shows which output they preferred" — i.e., the edit-diff itself, not an explicit rating, is what generates the preference pair. This directly corroborates the production real-time preference-learning pattern documented in `blog-cursor-real-time-rl.md`, where Cursor treats live user interactions (accept/reject/edit signals on Composer suggestions) as reward signal for continuous RL-based checkpoint updates. Fyxer's version is narrower in scope (DPO on edit-diff pairs specifically, for email drafting rather than code generation) but the same core idea — implicit, passively-collected user correction as training signal, replacing manual labeling — appears independently in both a coding-agent context and an email-assistant context. This strengthens the general pattern's credibility: two different vendors, two different domains, converging on the same underlying idea — the user's own edit is the label.

### Claim 6: Every drafting model change goes through an A/B test and ships only when it produces a statistically significant improvement; Fyxer's user volume lets the team sometimes reach that significance threshold within a day
- **Evidence**: Narrative description immediately following the DPO explanation, same section.
- **Confidence**: anecdotal (single-company practice description; "statistically significant" is not defined — no p-value, sample size, or metric specified)
- **Quote**: "Every drafting change then goes through an A/B test. Fyxer ships the new version only when it produces a statistically significant improvement. Its user volume means the team can sometimes reach that threshold within a day."
- **Our assessment**: This is a concrete production-shipping gate for fine-tuned/DPO-trained checkpoints — a quantitative bar (statistical significance) rather than a qualitative looks-better judgment call, and notable for the claimed cadence (same-day significance at Fyxer's volume). This is the same ship-only-when-it-wins-a-live-A/B-test discipline documented for Cursor's Composer checkpoints in `blog-cursor-real-time-rl.md`, again independently arrived at in a different product domain — worth citing together as two vendors converging on live A/B gating as the release discipline for continuously-retrained models, rather than offline eval scores alone.

### Claim 7: Before deployment, every model is evaluated on validation sets built from Fyxer's own email tasks (drafting, classification, prioritization), weighing accuracy against response time and cost since the best model choice can vary by job
- **Evidence**: Narrative description closing the "Train on how great assistants actually work" section.
- **Confidence**: anecdotal (single-company evaluation practice; no specifics on validation set size or composition)
- **Quote**: "Before any model is deployed, Fyxer evaluates it on validation sets built around its own email tasks, including drafting, classification, and prioritization. The team weighs accuracy alongside response time and cost, since the best choice can vary by job."
- **Our assessment**: An explicit statement that model selection is per-task and cost/latency-aware, not simply defaulting to the biggest or best model for every job — consistent with the cost-tier routing logic in `blog-cursor-router-model-classifier.md`, though Fyxer's version is a pre-deployment evaluation step for choosing which fine-tuned variant to ship per task rather than Cursor's live per-request routing classifier. Both sources reflect the same underlying principle: production systems at scale pick models per-task on an accuracy/cost/latency trade-off curve, not a single fixed model choice.

### Claim 8: Fyxer selected OpenAI specifically because its models scored best on Fyxer's internal benchmarks, offered strong fine-tuning capability for subjective tasks like tone and intent, and because OpenAI provided hands-on engineering support including in-person whiteboarding sessions
- **Evidence**: Narrative vendor-selection rationale plus a direct quote from Co-founder Archie Hollingsworth.
- **Confidence**: anecdotal (single company's vendor-selection account, self-reported and published by the vendor being praised — high promotional-incentive source)
- **Quote**: "We chose OpenAI because they have the best models, and they've given us real access and a close working relationship. I can drop a question in Slack and get an answer quickly, and when we face a problem, the team comes to our office and works through it with us. They show up."
- **Our assessment**: The internal-benchmarks-plus-fine-tuning-capability-plus-hands-on-support rationale is a useful checklist for how a technically sophisticated startup evaluates a model vendor beyond raw leaderboard scores — vendor engineering support (in-person whiteboarding, fast Slack response) is treated as a differentiator on par with model quality. As with all vendor-published case studies, this should be read as OpenAI publishing a customer's praise of OpenAI; it is not independent evidence that OpenAI's support model outperforms competitors', only evidence that this specific customer experienced and valued that level of support.

### Claim 9: Fyxer's training data originates from a pre-AI, human-powered executive assistant service the company operated for years, which accumulated more than 500,000 hours of annotated executive-workflow data capturing real assistants' judgment calls
- **Evidence**: Narrative description of the company's origin and data provenance, under the second numbered lesson ("Train on how great assistants actually work").
- **Confidence**: anecdotal (single-company self-reported figure; "500,000 hours" and "annotated" are not further defined — annotated by whom, to what schema, over what calendar period)
- **Quote**: "Before launching its AI product, Fyxer spent years operating a human-powered executive assistant service. Over time, the team accumulated a dataset built from more than 500,000 hours of annotated executive workflows, capturing how real assistants manage professional communication."
- **Our assessment**: This is the most distinctive and defensible data point in the source: Fyxer's fine-tuning corpus is not scraped or synthetic but drawn from years of the company's own prior human-labor business, before it built an AI product at all. The source's next paragraph adds that these examples captured "the small judgments behind a good response: when to answer quickly, when to wait, which earlier conversation matters, and how the same request can call for a different response from one person to another" — i.e., the training signal is framed as capturing tacit, context-dependent judgment calls rather than factual knowledge. This strategy of operating the human version of the service first, then using its transaction logs as training data, is a concrete, reusable go-to-market/data-strategy pattern for founders building subjective, judgment-heavy AI products — distinct from generic fine-tuning advice, since it depends on having built (and staffed) a real human service first.

### Claim 10: 53% of Fyxer's AI-generated email drafts are accepted by users as written, without further editing
- **Evidence**: Headline stat, restated in body text as a claimed outcome of the DPO/A-B-testing loop.
- **Confidence**: anecdotal (single-company self-reported metric; no definition of "accepted as written" — e.g., whether trivial whitespace/signature edits still count as acceptance — and no baseline/comparison figure from before the feedback loop was introduced)
- **Quote**: "Today, 53% of Fyxer's AI-generated drafts are accepted as written. That means the system is correctly predicting intent and tone for a large share of real conversations."
- **Our assessment**: A concrete quality metric for a generative-drafting product, useful as a benchmark figure, but presented without a before-the-feedback-loop baseline acceptance-rate comparison, so it cannot be read as direct evidence that the DPO loop (Claim 5) specifically drove this number — only as a snapshot of current quality alongside the described training approach.

### Claim 11: Fyxer's user retention exceeds 90% at the 90-day mark, which the co-founder frames as a stronger trust signal than the company's revenue growth
- **Evidence**: Headline stat plus a direct quote from Co-founder Archie Hollingsworth explicitly de-emphasizing ARR in favor of retention.
- **Confidence**: anecdotal (single-company self-reported metric; no cohort definition, no churn-reason data, no comparison to industry-typical SaaS 90-day retention)
- **Quote**: "Everyone talks about ARR, but I think retention is the real flex. Over 90% of our users are still paying at the 90-day mark with us, and still using us every day."
- **Our assessment**: The explicit framing operationalizes trust as sustained daily usage and continued payment by a largely non-technical user base, rather than as a stated preference or satisfaction score — a concrete, if self-reported, definition of what the article's title ("an AI executive assistant people trust") means in practice for this product category. This gives Chapter 05 (team adoption/trust) material a behavioral, revealed-preference definition of trust to set alongside the more qualitative/survey-based trust framings elsewhere in the corpus.

### Claim 12: Fyxer grew from $1 million to $32 million in annual recurring revenue during 2025
- **Evidence**: Single sentence stated as fact in the retention-discussion paragraph, not part of the headline stat block.
- **Confidence**: anecdotal (single-company self-reported financial figure, unaudited, no source or filing cited)
- **Quote**: "In 2025 alone, Fyxer grew from $1 million to $32 million in annual recurring revenue."
- **Our assessment**: A 32x ARR growth figure for a single calendar year is an extreme outlier even among well-known fast-growing AI startups; treat as an unaudited, vendor-published self-report with no independent corroboration. Notably, the article itself immediately pivots away from this figure toward the retention statistic as "the real flex," which is worth preserving as framing: even the company being profiled treats its own ARR growth figure as less meaningful than its retention figure.

## Concrete Artifacts

### Case study metadata and stat block

```
Source: https://openai.com/index/fyxer (September 14, 2026)

Company size: Startup
Region:       Europe & UK
Industry:     Technology
Products:     API

Headline stats:
  90%   User retention after 90 days
  53%   Of AI-generated drafts accepted as written
```

### Three-lesson structure (article's own subheadings)

```
Source: https://openai.com/index/fyxer (September 14, 2026)

1. Break email into smaller jobs
2. Train on how great assistants actually work
3. Turn user feedback into a self-training loop

(closing section, unnumbered): "From drafts to a proactive assistant"
```

### Architecture description — verbatim

```
Source: https://openai.com/index/fyxer (September 14, 2026)

"Fyxer built its system around 30–50 specialized models, each responsible
for a narrow part of the email workflow. Instead of treating email as a
single text-generation task, Fyxer breaks the problem into a system of
predictions, like deciding whether a message requires a reply or drafting
responses that match a user's tone and context."

"When a new email arrives, a reply decision model classifies the message:
is this something that needs a response, a scheduling action, or simply
information the user should see?

If a response is needed, additional models analyze the intent of the email
and predict the likely outcome of the interaction. These models determine
patterns such as whether the conversation is moving toward scheduling a
meeting, resolving a request, or continuing a longer relationship thread.

Memory is one of the most important parts of the system. Fyxer needs to
decide which details should persist across conversations and which should
disappear after a single exchange. When a new email arrives, retrieval
models compare it with stored interactions and surface the memories most
relevant to that person and thread."
```

### Training/feedback-loop description — verbatim

```
Source: https://openai.com/index/fyxer (September 14, 2026)

"Fyxer uses supervised fine-tuning and Low-Rank Adaptation (LoRA) across
its broader system to create task-specific model variants while
controlling training cost. Early in the product's development, the team
used OpenAI's fine-tuning platform for tasks that needed high accuracy.
More recently, Fyxer worked with OpenAI's managed fine-tuning team to put
a new checkpoint into production."

"Once deployed, Fyxer's system continues improving through real user
feedback. When someone edits a draft before sending it, the difference
between the original and final email shows which output they preferred.
Fyxer converts those comparisons into training data using Direct
Preference Optimization (DPO). Instead of manually labeling every example,
the model learns from pairs of outputs: the original draft and the
user-edited version.

Every drafting change then goes through an A/B test. Fyxer ships the new
version only when it produces a statistically significant improvement.
Its user volume means the team can sometimes reach that threshold within
a day."
```

### Named quotes — verbatim

```
Source: https://openai.com/index/fyxer (September 14, 2026)

Attribution: Archie Hollingsworth, Co-founder, Fyxer
"There's something called Moravec's paradox. Things that humans find easy
are hard for computers, and things that computers find easy are hard for
humans."

Attribution: Archie Hollingsworth, Co-founder, Fyxer
"We chose OpenAI because they have the best models, and they've given us
real access and a close working relationship. I can drop a question in
Slack and get an answer quickly, and when we face a problem, the team
comes to our office and works through it with us. They show up."

Attribution: Joey Dwonczyk, AI/ML Product Engineer, Fyxer
"OpenAI has been pivotal for us in helping us transfer the learning that
we have about our customer and successfully incorporate it into how the
models work."

Attribution: Archie Hollingsworth, Co-founder, Fyxer
"Everyone talks about ARR, but I think retention is the real flex. Over
90% of our users are still paying at the 90-day mark with us, and still
using us every day."

Attribution: Archie Hollingsworth, Co-founder, Fyxer
"Our vision is to get our customers doing as much of the work they
absolutely love. We want to get them to a place where they never have to
open their computer and can trust Fyxer to manage all of that."
```

## Cross-References

- **Corroborates**:
  - `blog-cursor-real-time-rl.md`: Both sources describe production systems that
    convert passive, implicit user-correction signal (Fyxer: draft edits →
    DPO pairs; Cursor: accept/reject/edit interactions → RL reward) into
    continuous model improvement, gated by live evaluation before shipping
    (Fyxer: per-change A/B test requiring statistical significance, Claim 6;
    Cursor: checkpoints shipped roughly every ~5 hours based on live metrics).
    Two different vendors, two different task domains (email drafting vs. code
    editing), independently converge on the same idea: the user's own
    correction is the label, and shipping is gated by a live significance
    test rather than an offline eval score alone.
  - `blog-cursor-router-model-classifier.md`: Corroborates the general
    pattern of decomposing a monolithic model call into task-specific pieces
    chosen by a cost/accuracy trade-off (Claim 7), though Fyxer decomposes the
    *task* into 30-50 narrow predictive models (Claim 1) while Cursor routes a
    single coding request to one of several general-purpose models via a
    learned classifier — related but structurally distinct approaches to
    the same underlying problem that a single fixed model is the wrong
    default for every request.
  - `blog-anthropic-claude-managed-agents-memory.md`: Both sources treat
    selective memory persistence — deciding what to keep vs. discard — as
    architecturally central (this note's Claim 3 vs. that note's Claim 9,
    where Opus 4.7 is described as "more discerning about what to
    remember"). Fyxer's per-person, per-thread relevance scoping (Claim 3)
    is also comparable in kind, though not in mechanism, to that note's
    Claim 5 org-wide-read-only/per-user-read-write scoped-sharing model —
    both are examples of scoping memory access rather than treating a store
    as monolithic. Fyxer's design is a bespoke, retrieval-model-based system
    built directly on OpenAI's API rather than a managed platform memory
    layer, so this is independent corroboration of the general principle
    that not everything should persist and that relevance-scoped retrieval
    matters, from a different vendor stack and product category, not
    corroboration of the same implementation.

- **Contradicts**: None found. No existing source note makes a claim about
  email-assistant architecture, fine-tuning-cost-control via LoRA, or
  DPO-from-user-edits that this source disagrees with.

- **Extends**: `blog-openai-asana-codex-case-study.md`, and the broader set
  of OpenAI customer case studies in the corpus (e.g.
  `blog-openai-notion-codex-case-study.md`, `blog-openai-1password-codex-case-study.md`).
  Those case studies center on Codex-driven coding-agent migrations with
  time/cost-savings headline stats; this is the first OpenAI case study in
  the corpus centered on fine-tuning methodology (SFT + LoRA + DPO) and a
  production ML feedback-loop architecture for a non-coding product, rather
  than an agentic coding workflow.

- **Novel**:
  - A named, production DPO pipeline built directly from draft-vs-edited-draft
    pairs as the preference signal, for an email-drafting product specifically
    (Claim 5) — the corpus's clearest email-domain analogue to Cursor's
    code-domain real-time RL loop.
  - LoRA named explicitly as the mechanism for controlling training cost
    across dozens of task-specific fine-tuned model variants (Claim 4) — no
    prior corpus source names LoRA as a cost-control lever at this specific
    scale (30-50 models).
  - The go-to-market/data-strategy pattern of operating the human version of
    the service first, then mining its transaction logs as fine-tuning data
    (Claim 9) — a reusable strategic pattern for founders of subjective,
    judgment-heavy AI products, distinct from generic advice to simply gather
    more training data.
  - Retention (90%+ at 90 days), rather than ARR, offered explicitly by the
    founder as the primary trust metric for a consumer/prosumer-facing AI
    assistant (Claim 11) — a concrete, revealed-preference operationalization
    of the article's own title claim, "an AI executive assistant people trust."

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Cite Claim 1 (30-50 specialized
  models decomposing email handling) and Claim 7 (per-task, cost/latency-aware
  model selection at deployment) alongside `blog-cursor-router-model-classifier.md`
  as two independently-arrived-at examples of decomposing a task into narrow
  model calls chosen by a cost/accuracy trade-off, rather than one model call
  for everything — useful as a named pattern with two vendor examples from
  different product domains.

- **Chapter 04 (Context Engineering)**: Cite Claim 3 (retrieval-model-based,
  per-thread relevance-scoped memory that explicitly discards details judged
  not worth persisting) as a DIY memory-architecture data point to set
  alongside the managed-platform memory design in
  `blog-anthropic-claude-managed-agents-memory.md` — useful for readers
  building bespoke memory systems on a raw API rather than a managed agent
  platform.

- **Chapter 03 (Verification)**: Cite Claim 6 (every model change gated by a
  live A/B test requiring statistical significance before shipping) and
  Claim 5 (DPO from user-edit pairs as continuous training signal) alongside
  `blog-cursor-real-time-rl.md`'s live-metric-gated checkpoint shipping as a
  second, independent example of shipping model updates behind a live
  significance test rather than an offline eval score alone — worth adding
  as a named verification pattern for teams running continuously-retrained
  models in production, not just for coding agents.

- **Chapter 05 (Team Adoption)**: Cite Claim 11 (the founder's explicit
  retention-over-ARR trust framing, with 90%+ 90-day retention among a
  largely non-technical user base) as a concrete, behavioral definition of
  user trust in an AI product, to set alongside more qualitative trust
  material such as `blog-kentbeck-trust-factory.md` and
  `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`. Flag
  Claim 12 (32x ARR growth in one year) and Claim 10 (53% draft-acceptance)
  as unaudited, methodology-free self-reported figures that should be cited
  with that caveat rather than as validated benchmarks.

## Extraction Notes

- The live OpenAI URL (`https://openai.com/index/fyxer`) returned HTTP 403
  to both WebFetch and a direct `curl` request with a standard browser
  user-agent; the response headers show `cf-mitigated: challenge` and
  `server: cloudflare`, confirming this is a Cloudflare bot-challenge block,
  consistent with the same blocking behavior already documented for
  `openai.com` in other OpenAI-sourced notes' Extraction Notes (e.g.
  `blog-openai-asana-codex-case-study.md`). Retrieved instead via the
  Wayback Machine snapshot
  `http://web.archive.org/web/20260915155511/https://openai.com/index/fyxer`
  (crawled September 15, 2026, one day after the September 14 publication
  date), fetched with `curl` and parsed by stripping `<script>`/`<style>`
  blocks and remaining HTML tags rather than through an AI-summarization
  pass, specifically to keep every `Quote` field copied character-for-character
  rather than paraphrased, per MINER.md §2a.
- The article names a third Fyxer individual only by surname, "Shantsila,"
  with no first name or job title given anywhere in the source text. This
  quote (in the Architecture section, "We use OpenAI models for everything
  from digesting the email...") is used in Claim-adjacent context but not
  set up as a standalone numbered claim, since it duplicates the
  architectural content already covered by Claim 1-3 and adds no new
  information beyond confirming OpenAI models are used "across" the
  pipeline stages.
- The page's "Keep reading" footer links to three unrelated OpenAI customer
  posts (Legora, Playco, Replit case studies), none of which concern Fyxer;
  they were not followed as they are unrelated case studies, not
  sub-pages of this source.
- This is a single-source, single-company, vendor-published case study.
  Every quantitative claim (53% acceptance, 90%+ retention, $1M→$32M ARR,
  500,000+ hours of training data, 30-50 specialized models) is self-reported
  by Fyxer and/or OpenAI with no independent audit, methodology disclosure,
  or baseline comparison. Treat all confidence ratings above as anecdotal
  accordingly; none of the figures in this source should be cited in the
  guide as a validated benchmark without that caveat attached.
- No contradictions with existing source notes were identified during
  cross-referencing (see Cross-References → Contradicts); none filed.
