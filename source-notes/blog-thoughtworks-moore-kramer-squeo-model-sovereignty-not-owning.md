---
source_url: https://www.thoughtworks.com/insights/articles/model-sovereignty-is-not-about-owning-the-model
source_type: blog-post
title: "Model sovereignty is not about owning the model"
author: Alexander Moore, Chris Kramer, Thomas Squeo (Thoughtworks)
date_published: 2026-11-17
date_extracted: 2026-11-18
last_checked: 2026-11-18
status: current
confidence_overall: anecdotal
issue: "#4802"
---

# Model sovereignty is not about owning the model

> Thoughtworks framework article arguing that sovereignty is decided per workload on two axes (Control, Differentiation), is a property of the whole portfolio, and that the assets worth owning are evaluations, behavioral data/policies and the routing layer, while models, compute and serving can be rented.

## Source Context

- **Type**: blog-post (Thoughtworks Insights article, trusted feed `thoughtworks`, published 2026-11-17)
- **Author credibility**: Three Thoughtworks authors; vendor/consultancy perspective. Thomas Squeo also co-authored `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`. Cites survey figures without (in our read) primary-source detail.
- **Scope**: Decision model for placing AI workloads (API, rented regional frontier, owned weights, tuned small model, on-device, sovereign cloud) and for what to keep portable. No code or measurements of its own; survey stats are cited, not produced.

## Extracted Claims

### Claim 1: Sovereignty means control, not ownership or self-operation
- **Evidence**: Definitional argument.
- **Confidence**: emerging
- **Quote**: "Model sovereignty is that control, and it doesn't require owning or operating everything yourself."
- **Our assessment**: Useful reframing that dissolves the own-vs-rent binary. Consistent with the "rent the frontier" stance in existing notes.

### Claim 2: Each workload should be placed on two axes: Control and Differentiation
- **Evidence**: Framework; no empirical validation.
- **Confidence**: anecdotal
- **Quote**: "Who runs the computation and who can see it, stop it or change it?" (Control); "Whose knowledge is in the model, and how much of the result depends on it?" (Differentiation)
- **Our assessment**: Clean, actionable. Commodity/light-requirement workloads go to cheap APIs; differentiated/strict ones may justify fine-tuning and self-managed infrastructure (our paraphrase of the article's mapping).

### Claim 3: Options range from closed frontier API to on-device, sovereign cloud addresses infrastructure/residency only
- **Evidence**: Enumerated options: closed frontier APIs (bundle both questions under the vendor), rented frontier model served in-region, owned generic weights, tuned small model on own data, sovereign cloud (e.g. AWS European Sovereign Cloud). Contract terms on retention, residency and retirement still matter.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Sovereign cloud changes who controls infrastructure, not how differentiated the workload is. Reasonable; contract-term point is practical.

### Claim 4: Fine-tunes are tied to their base model's lifetime, so don't invest ownership there
- **Evidence**: Dated example: a provider gave 92 days' notice of shutting down two model families in January 2027, against a stated six-month minimum.
- **Confidence**: emerging (single dated example, provider unnamed in our extraction)
- **Quote**: "a fine-tune dies with the base model it was built on."
- **Our assessment**: Strong, concrete argument for investing in evals/data over weights. The 92-day vs six-month gap shows stated deprecation policies are not reliable.

### Claim 5: Multi-model use is already the norm (vendor research stat)
- **Evidence**: Cited survey: 3+ model families rose from 36% to 59% between July and October 2025.
- **Confidence**: anecdotal (self-reported, single-source; flag if cited)
- **Quote**: "puts 78% of companies on two or more model families"
- **Our assessment**: Directional support for portability/routing; do not cite the number without chasing the primary source.

### Claim 6: On-device inference is the most sovereign option but trades capability and cost model
- **Evidence**: Apple example: 20B-parameter model on a phone; capability capped by hardware, costs become fixed (utilization matters), fleet operations become the main work.
- **Confidence**: anecdotal
- **Quote**: "Apple fits a 20-billion-parameter model into a phone by keeping the weights in flash memory"
- **Our assessment**: Useful as a fixed-vs-variable cost illustration; vendor-specific and not generalizable to enterprise teams.

### Claim 7: Own evaluations, behavioral data/policies and routing; rent the rest
- **Evidence**: Argued from Claim 4; models, compute and serving are swappable, these three must be portable across platforms.
- **Confidence**: emerging
- **Quote**: "Evaluations, behavioral data and routing have to be owned"
- **Our assessment**: The most novel, guide-relevant claim: evals as the durable asset when models churn.

### Claim 8: Sovereignty is a portfolio property
- **Evidence**: Argument; includes knowing where each workload sits, why, and what moving it would take. Article also notes EU rules ending data-processing switching fees (Jan 2027).
- **Confidence**: emerging
- **Quote**: "Sovereignty is a property of the portfolio."
- **Our assessment**: Good framing for Ch05 portfolio/cost decisions.

## Concrete Artifacts

No code. Decision grid (from article, paraphrased): x = Control strictness, y = Differentiation; commodity+light → inexpensive API; differentiated+strict → fine-tune and self-run.

## Cross-References

- **Corroborates**: `blog-thoughtworks-nolan-renting-the-frontier.md` (rent the frontier, own the core); `blog-thoughtworks-vega-token-billing-lockin.md` (provider lock-in); `blog-thoughtworks-gall-kimi-k3-multi-model-era.md` (multi-model reality).
- **Contradicts**: none found.
- **Extends**: `blog-thoughtworks-kamelman-sovereign-ai-dependency.md` (sovereignty vs operational resilience) with a per-workload decision model and owned-assets list; `blog-thoughtworks-shangqi-sovereign-ai-practical-approach.md` (companion Thoughtworks sovereignty piece, #4801); `blog-thoughtworks-lovin-gall-local-inference-boundary.md` (local inference trade-offs).
- **Novel**: Two-axis Control/Differentiation placement; "own evals, behavioral data, routing" as sovereignty assets; the 92-day vs six-month deprecation example.

## Guide Impact

- **Chapter 05**: Where sovereignty is discussed, add the per-workload (not per-org) placement framing and the rule "own evals, behavioral data and routing; rent models and serving," citing this note.
- **Chapter 06**: Add contract-term checks (retention, residency, retirement notice) even when vendors don't train on paid-tier data; note stated deprecation minimums may not be honored.
- **Chapter 00**: Optionally cite the portfolio framing as a principle.

## Extraction Notes

- The page was read via a summarizing fetch tool that declined to reproduce the full text; quotes above are the short fragments it returned and were not independently re-verified character-by-character. The Assayer should spot-check them. Claims 3 and 6 carry paraphrase rather than quotes for that reason.
- Statistics are the article's cited figures; primary source not followed.
- Cross-references cite notes by name, not claim number.
