---
source_url: https://github.blog/changelog/2026-06-01-evaluation-models-in-auto-for-individual-plans
source_type: docs
title: "Evaluation models in auto for individual plans"
author: GitHub (official changelog)
date_published: 2026-06-01
date_extracted: 2026-06-02
last_checked: 2026-06-02
status: current
confidence_overall: settled
issue: "#1027"
---

# Evaluation Models in Auto for Individual Plans

> GitHub's June 1, 2026 changelog announcing that experimental "evaluation
> models" are now accessible to individual non-enterprise Copilot users through
> auto model selection — opt-out by default, excluded from enterprise plans —
> expanding the effective auto pool beyond previously documented GA-only members
> and establishing a plan-differentiated model testing strategy.

## Source Context

- **Type**: docs (GitHub official product changelog, ~100–150 words of primary
  announcement text, June 1, 2026)
- **Author credibility**: GitHub engineering team announcing a production
  feature change for individual Copilot plans. Authoritative for: the existence
  of evaluation model access in auto, the opt-out nature of the feature, the
  user settings mechanism for disabling it, and the individual/non-enterprise
  scope. Not authoritative for: which specific evaluation models are in scope,
  their cost multipliers, their capability characteristics, technical differences
  between evaluation and GA models, or how long this program will run.
- **Scope**: The availability of evaluation (pre-GA/experimental) models in
  GitHub Copilot's auto model selection feature for individual non-enterprise
  users. Covers: the opt-out default, the user control mechanism (settings page),
  and the plan-tier boundary (individual only, not enterprise). Does NOT cover:
  which specific evaluation models are included, their multipliers, how
  evaluation models differ technically from GA models, whether enterprise users
  will eventually get access, or any performance/quality data from evaluation
  model usage.

## Extracted Claims

### Claim 1: GitHub is making evaluation (pre-GA/experimental) models available to individual non-enterprise Copilot users through auto model selection

- **Evidence**: Official GitHub product changelog announcing the feature. The
  term "evaluation models" is used by GitHub without explicit definition in this
  source — the referenced documentation anchor (supported-models#evaluation-models)
  establishes them as a distinct model category separate from GA and public
  preview models.
- **Confidence**: settled (product fact stated in official changelog)
- **Quote**: "GitHub Copilot offers access to evaluation models for individual
  non-enterprise users, and these models may be served in Copilot auto model
  selection."
- **Our assessment**: This is the core new capability. "Evaluation models" are
  distinct from GA models — the GitHub documentation reference indicates a
  separate category for models not yet fully released. Making them available via
  auto routing to individual users (rather than requiring explicit opt-in
  selection) means practitioners using auto mode may encounter these models
  without actively choosing them. For Ch04: note that "auto model selection"
  does not mean "GA models only" for individual users as of June 1, 2026 — the
  effective pool now includes experimental models unless disabled. This is a
  meaningful expansion of what "auto" means for individual Copilot subscribers.

### Claim 2: Evaluation models in auto are opt-out, not opt-in — individual users receive them by default unless they actively disable them

- **Evidence**: The announcement's instructions frame disabling as an action the
  user must take, confirming that evaluation models are included in auto routing
  by default for eligible users.
- **Confidence**: settled (opt-out framing stated in official changelog)
- **Quote**: "To disable use of evaluation models through Copilot auto model
  selection, visit your GitHub Copilot settings."
- **Our assessment**: The opt-out default is the highest-impact aspect of this
  change for practitioners. Auto mode in GitHub Copilot is already recommended
  as the default for most workflows (per CLI auto: #203, CCA auto: #745, VS Code
  auto: #844). Practitioners who adopted auto as a "GA models only" routing mode
  will now be receiving evaluation models unless they explicitly visit settings
  to disable them. For Ch04: add a note to auto model selection guidance that
  individual users should evaluate whether evaluation model access is appropriate
  for their workflows. Production workflows with stability requirements should
  consider disabling evaluation models via settings; exploratory or development
  workflows might benefit from earlier access to experimental model versions.

### Claim 3: This feature is scoped to individual non-enterprise users — enterprise Copilot users are explicitly excluded

- **Evidence**: The announcement's "individual non-enterprise users" qualifier
  establishes the plan-tier boundary. Enterprise users are not mentioned as
  eligible for this feature.
- **Confidence**: settled (stated explicitly in official changelog)
- **Quote**: "GitHub Copilot offers access to evaluation models for individual
  non-enterprise users"
- **Our assessment**: The enterprise exclusion is significant for two reasons.
  First, enterprise teams have tighter governance requirements around model
  stability — routing enterprise users to evaluation models without change-control
  review could introduce compliance risks. Second, the exclusion creates a
  plan-differentiated testing strategy: individual users serve as a testing
  population for evaluation models before any potential enterprise rollout. This
  partially inverts the typical pattern in GitHub Copilot plan changes: prior
  individual plan changes (#289) documented restrictions (Opus removed from Pro,
  signup pauses) where enterprise retained capabilities individual users lost.
  Here, individual users gain access to something enterprise users explicitly
  don't have — experimental model routing through auto.

### Claim 4: GitHub is using individual users as a distributed evaluation population for pre-GA models, consistent with a plan-differentiated model testing strategy

- **Evidence**: Emerging inference from the combination of: (a) the "evaluation
  models" nomenclature, (b) the individual-only scope excluding enterprise, and
  (c) the opt-out default ensuring broad coverage across individual users. No
  explicit statement in the source says "we are using individual users to evaluate
  models" — the structural design (experimental models, routed to non-enterprise
  individuals by default) describes this pattern.
- **Confidence**: emerging (structural inference — strongly implied by design
  choices, not stated explicitly)
- **Quote**: (no direct quote; see Our assessment)
- **Our assessment**: The design is consistent with how software products use
  broader user populations to gather usage data on pre-release features: a wider
  population receives early access, their usage provides signal, more restricted
  (e.g., enterprise) deployments later benefit from that validation. If this
  framing is correct, individual Copilot subscribers who haven't read the
  changelog are quietly participating in GitHub's model evaluation pipeline. The
  opt-out mechanism acknowledges this by giving users a choice, but the opt-out
  default means most individual users receive evaluation models without explicitly
  consenting to the evaluator role. For Ch03: this is a notable example of using
  production user traffic for model evaluation — a methodology consideration for
  practitioners who depend on agentic tools with opaque model routing.

### Claim 5: Evaluation model access expands the effective auto model pool beyond the previously documented GA-only members, with specific model names and multipliers undisclosed

- **Evidence**: Prior auto pool documentation (CLI #203: GPT-5.4, GPT-5.3-Codex,
  Sonnet 4.6, Haiku 4.5; VS Code #844: "multiple model families at 0x–1x")
  described the pool in terms of GA model versions. This source adds a new
  category of eligible candidates — evaluation models — without naming specific
  models or their multipliers.
- **Confidence**: settled (pool expansion is stated; specific new members are not)
- **Quote**: "these models may be served in Copilot auto model selection"
- **Our assessment**: The phrase "may be served" introduces probabilistic routing
  — evaluation models are eligible for auto selection but not guaranteed to be
  selected on any given request. This is consistent with how the auto router
  works (selecting from a pool rather than deterministically selecting a specific
  model). For Ch04: the practical implication is that individual users' auto-
  routed requests may now be handled by models not previously in the documented
  pool. Teams that built observability into their CLI auto usage (per #203
  Claim 5: logging the surfaced model name) will be able to detect when evaluation
  models are selected. Teams without this logging will have no visibility into
  whether evaluation models are handling their requests.

## Concrete Artifacts

### Announcement Summary (June 1, 2026)

```
Title:     Evaluation models in auto for individual plans
Published: June 1, 2026
Source:    https://github.blog/changelog/2026-06-01-evaluation-models-in-auto-for-individual-plans

Core fact:  "GitHub Copilot offers access to evaluation models for individual
            non-enterprise users, and these models may be served in Copilot
            auto model selection."

Opt-out:    "To disable use of evaluation models through Copilot auto model
            selection, visit your GitHub Copilot settings."

Scope:      Individual non-enterprise users ONLY.
            Enterprise users: NOT affected by this announcement.

Docs ref:   https://docs.github.com/copilot/reference/ai-models/supported-models#evaluation-models
```

### Evaluation Model Access by Plan Tier (as of June 1, 2026)

```
GitHub Copilot — Evaluation Models in Auto

INDIVIDUAL (FREE):
  Evaluation models in auto:  YES (opt-out default)
  Disable via:                GitHub Copilot settings

INDIVIDUAL (PRO):
  Evaluation models in auto:  YES (opt-out default)
  Disable via:                GitHub Copilot settings

INDIVIDUAL (PRO+):
  Evaluation models in auto:  YES (opt-out default)
  Disable via:                GitHub Copilot settings

ENTERPRISE / BUSINESS:
  Evaluation models in auto:  NOT in scope per this announcement

Note: Specific evaluation model names and multipliers NOT disclosed
      in this changelog. See referenced documentation for current list:
      https://docs.github.com/copilot/reference/ai-models/supported-models#evaluation-models
```

### Auto Model Pool — Individual Users (before and after June 1, 2026)

```
Prior auto pool (April 17 – May 20, 2026, per #203 and #844):
  GA models: GPT-5.4, GPT-5.3-Codex, Sonnet 4.6, Haiku 4.5
  (VS Code: "multiple model families at 0x–1x")
  Constraint: 0x–1x multiplier models, GA status only

Updated pool (as of June 1, 2026, for individual non-enterprise users):
  GA models (as above) + evaluation models (names and multipliers not disclosed)

Key change: evaluation model eligibility applies only to individual users.
Enterprise users' auto pool: unchanged per this announcement.
```

## Cross-References

- **Corroborates** `docs-github-copilot-cli-auto-model-selection.md` (issue #203,
  Claim 1): CLI auto was documented as "available across all Copilot plans." This
  source confirms that feature but adds a new dimension within individual plans:
  the auto pool now includes evaluation models for non-enterprise users. The April
  17 note itself anticipated evolution: "the available models will evolve over time."
  This source is that documented evolution for the evaluation model category.

- **Extends** `docs-github-copilot-cli-auto-model-selection.md` (issue #203,
  Claim 3): That source established the auto pool as "currently limited to models
  with 0x to 1x multipliers" listing GPT-5.4, GPT-5.3-Codex, Sonnet 4.6, and
  Haiku 4.5. This source adds evaluation models to the eligible pool for individual
  users. Whether evaluation models fall within the 0x–1x constraint is not stated
  — the constraint may apply, may be suspended for evaluation models, or may be
  irrelevant (e.g., evaluation models may have 0x multipliers during testing). The
  prior pool statement remains accurate as a GA model floor; this source adds an
  additional category above or alongside it.

- **Extends** `docs-github-copilot-vscode-auto-model-selection.md` (issue #844,
  Claim 3): That source documented VS Code auto as "currently limited to models
  with 0x to 1x multipliers." This source's evaluation model expansion applies to
  auto model selection generally; whether it affects the VS Code auto pool
  specifically (as well as the CLI pool) is not stated in this changelog but is
  plausible by consistency. The 0x–1x constraint in #844 may now have a new
  qualification for individual users: evaluation models may be served regardless
  of how they relate to the 0x–1x pool constraint.

- **Extends** `docs-github-copilot-individual-plan-changes.md` (issue #289):
  That source (April 20, 2026) documented individual plan restrictions — Opus
  removed from Pro, signup pauses, Pro+ as the Opus ceiling. This source
  introduces an asymmetry the April 20 source did not capture: individual users
  now gain access to evaluation models that enterprise users do not. The two
  sources together show GitHub applying plan differentiation in both directions:
  individual users lose access to high-capability GA models (Opus from Pro) while
  gaining access to experimental pre-GA models (evaluation models via auto). The
  net capability for individual users is being restructured, not simply narrowed.

- **Complements** `docs-github-copilot-cca-auto-model-selection.md` (issue #745,
  Claim 2): That source documented CCA auto routing as based on "system health and
  model performance" with the auto pool unspecified. This source provides a new
  data point applicable to auto model selection across surfaces: evaluation models
  are now eligible for individual users. Whether the evaluation model expansion
  applies to CCA auto specifically (not just CLI/VS Code auto) is not confirmed in
  either source, but the consistent auto-routing policy framework across surfaces
  (per CLI #203, CCA #745, VS Code #844) suggests consistency is likely.

- **Novel**:
  - First corpus source to document "evaluation models" as a distinct GitHub
    Copilot auto pool category accessible to individual users. All prior auto pool
    documentation described GA-only model membership; this is the first source to
    introduce a non-GA experimental tier into the documented pool.
  - First corpus source to document an opt-out-default experimental feature for
    individual Copilot users — prior plan changes were restrictions (Opus removed,
    signups paused); this is an expansion of auto pool scope that users must
    actively disable to avoid.
  - First corpus source to document a plan-differentiated difference where
    individual users explicitly get something enterprise users do not: evaluation
    model routing through auto. All prior plan-tier differences in this corpus
    consistently gave enterprise more (model access, governance controls, agent
    features); this inverts that pattern for the experimental model category.
  - First source to introduce the concept that GitHub may use individual user
    populations as a model evaluation pool before broader rollout — a production
    evaluation methodology claim with no prior corpus parallel.

## Guide Impact

### Chapter 03: Agentic Practices / Workflow Methodology

- **Production traffic as model evaluation signal**: This announcement documents
  GitHub routing individual users to evaluation (pre-GA) models by default via
  auto model selection. For Ch03: note that AI-native development tools may use
  production user traffic as evaluation data for new model versions. Practitioners
  who rely on "auto" mode may be participating in model evaluation without explicit
  consent — their workflow is part of the vendor's quality signal pipeline. This is
  a relevant consideration when designing agentic workflows: "auto" mode is not a
  black box with fixed behavior; it is a dynamic routing policy that may include
  experimental models.
- **Opt-out as a workflow design decision**: The existence of a settings-based
  opt-out implies that evaluation models are not universally desirable. For
  production agentic workflows with stability or reproducibility requirements,
  guide advice should be: inspect auto model selection settings in GitHub Copilot
  and consider disabling evaluation models for production pipelines where model
  consistency matters. Development and exploratory workflows may benefit from
  evaluation model access as a way to try newer model versions earlier.

### Chapter 04: Model Selection and Cost Management

- **Auto mode no longer guarantees GA-only routing for individual users**: Prior
  guidance recommending auto mode for individual users implicitly assumed the auto
  pool contained only GA models. This source changes that assumption as of June 1,
  2026. Update any Ch04 guidance that frames auto as "routing to the best
  available GA model" — for individual non-enterprise users, auto now includes
  evaluation models unless explicitly disabled.
- **Evaluation model multipliers unknown**: Unlike the documented 0x–1x GA pool,
  the multipliers for evaluation models are not stated. Teams monitoring premium
  request consumption may see unexpected changes if evaluation models carry
  non-standard multipliers. Individual users running cost-sensitive automated
  workflows on auto mode should monitor their premium request consumption after
  this change.
- **Settings audit recommendation**: Add a recommendation for individual Copilot
  users running automated or agentic workflows on auto mode: visit GitHub Copilot
  settings and verify the evaluation model preference matches their workflow
  requirements. This is a new configuration variable that did not exist before
  June 1, 2026.

## Extraction Notes

1. **Source is very short (~100–150 words of primary text)**: All substantive
   claims are exhausted in the five claims above. Nothing was skimmed.
2. **Quote verification note**: The two key quotes were obtained through multiple
   independent WebFetch calls to the source URL and appeared consistently across
   responses. However, since WebFetch processes content through an AI model rather
   than returning raw HTML, there is a residual risk that these are very close
   paraphrases rather than character-for-character copies. The Assayer should
   verify these quotes directly against the source URL.
3. **"Evaluation models" definition not in source**: The source does not define
   what "evaluation models" are; it relies on the referenced documentation
   (supported-models#evaluation-models) for definition. A WebFetch of that
   documentation page did not surface an explicit "evaluation models" section in
   the returned summary, suggesting either the section exists but wasn't captured
   in the summary, or the documentation was recently updated. The interpretation
   in this note (pre-GA, experimental category) is based on the terminology and
   the referenced anchor — verify against current docs before citing.
4. **No specific evaluation model names disclosed**: The announcement does not
   name any specific evaluation models. Any source note citing a specific model
   as an "evaluation model" would require a separate authoritative source.
5. **Related concurrent updates not extracted**: The changelog page references
   concurrent updates (Claude Opus 4.8 GA, billing changes, usage metrics API
   enhancements, VS Code model selection improvements) as related items. These are
   separate changelog entries, not part of this specific announcement, and are not
   extracted as primary claims here.
6. **No contradictions to file**: The auto pool expansion for individual users with
   evaluation models does not contradict existing source note claims — prior notes
   documented the pool as of their dates and the CLI auto note explicitly flagged
   that "available models will evolve over time." This is documented evolution, not
   contradiction. No contradiction issue required.
