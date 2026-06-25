---
source_url: https://github.blog/changelog/2026-06-24-changes-to-model-selection-for-free-and-student-plans
source_type: docs
title: "Changes to model selection for Free and Student plans"
author: GitHub (official changelog)
date_published: 2026-06-24
date_extracted: 2026-06-25
last_checked: 2026-06-25
status: current
confidence_overall: settled
issue: "#1305"
---

# Changes to Model Selection for Free and Student Plans

> GitHub's June 24, 2026 changelog establishing auto model selection as the
> default and ONLY model selection experience for Copilot Free and Student
> plans — completing the plan-tier differentiation of model selection mode
> that began with the April 2026 picker restrictions, and announcing the
> retirement of the "(Preview)" label from Microsoft-released Copilot models.

## Source Context

- **Type**: docs (GitHub official product changelog, June 24, 2026; approximately
  150–200 words of primary announcement text)
- **Author credibility**: GitHub engineering team announcing a production change
  to Copilot plan behavior. Authoritative for: the auto-only policy for Free and
  Student plans, the multi-model-family access description, and the rationale for
  retiring the "(Preview)" label. Not authoritative for: which specific models are
  in the Free/Student auto pool, whether Pro/Pro+ explicitly retain manual selection
  (implied but not stated in this changelog), or how the auto routing heuristic for
  Free/Student compares to the CLI or VS Code auto implementations.
- **Scope**: Model selection mode changes for Copilot Free and Student plans, June
  24, 2026, plus a "(Preview)" label retirement for Microsoft-released models across
  Copilot. Does NOT cover: specific models in the Free/Student auto pool, Pro/Pro+
  model selection changes, business/enterprise plan impacts, numeric usage limits, or
  the GitHub Community discussion content (discussion #198751).

## Extracted Claims

### Claim 1: Copilot Free and Student plans now use auto model selection as the default and only model selection experience — manual model selection is fully removed

- **Evidence**: Official GitHub product changelog dated June 24, 2026. The announcement
  frames auto as "the default and only model selection experience," not merely a default
  with a manual override available.
- **Confidence**: settled (product fact stated in official changelog)
- **Quote**: "Copilot Free and Student plans will now use Copilot auto model selection
  as the default and only model selection experience."
- **Our assessment**: This is the most significant claim in the source. It establishes
  that Free and Student plan holders no longer have the ability to select models manually
  — auto routing is mandatory, not optional. This differs qualitatively from the pattern
  documented in `docs-github-copilot-student-gpt53codex-picker-removal.md` (April 27,
  2026), where one model (GPT-5.3-Codex) was removed from the Student picker while
  others remained selectable. That source introduced "picker-removed but auto-retained"
  as a third access state; this source eliminates the picker entirely for both Free and
  Student tiers. For Ch02: update any model selection guidance that assumes Free and
  Student users can exercise explicit model choice — as of June 24, 2026, they cannot.
  For Ch04: the model selection decision for Free and Student practitioners has been made
  for them; they should focus on understanding what the auto pool contains for their plan
  tier and whether to use the evaluation model opt-out documented in issue #1027.

### Claim 2: Auto selection for Free and Student plans provides access to models across multiple model families, subject to plan restrictions

- **Evidence**: Official changelog describes the auto pool in provider-agnostic terms
  without naming specific models. The phrase "subject to plan restrictions" indicates the
  Free/Student auto pool is not necessarily identical to auto pools on higher tiers.
- **Confidence**: settled (stated in official changelog; specific models undisclosed)
- **Quote**: "access to models across multiple model families, subject to plan restrictions"
- **Our assessment**: The "multiple model families" framing is consistent with the VS Code
  auto description (issue #844, Claim 9: "Auto leverages models from multiple model
  families, depending on subscription type and policies"). The "subject to plan
  restrictions" qualifier is important: the Free/Student auto pool may be more constrained
  than the Pro/Pro+ auto pool, even though both use auto routing. Prior CLI auto pool
  documentation (issue #203) listed GPT-5.4, GPT-5.3-Codex, Sonnet 4.6, and Haiku 4.5
  at 0x–1x multipliers; the Free/Student auto pool may be a subset. Specific pool
  composition for Free/Student is not confirmed in this source. For Ch04: practitioners
  on Free and Student plans should consult GitHub's supported models documentation to
  determine which models may be served by auto on their plan tier.

### Claim 3: GitHub is retiring the "(Preview)" designation from Microsoft-released models across Copilot, citing auto model selection as making the label unnecessary

- **Evidence**: Official changelog announces this as a concurrent change alongside the
  auto-only policy for Free/Student. The rationale explicitly invokes auto model selection
  as the reason labels are no longer needed.
- **Confidence**: settled (stated in official changelog)
- **Quote**: "Copilot auto model selection managing model routing and continuous
  improvements happening behind the scenes, these labels are no longer needed"
- **Our assessment**: The Preview label removal applies to Microsoft-released models across
  Copilot broadly, not only to Free/Student plans. The rationale reveals a key product
  philosophy: when model improvements are delivered automatically through auto routing,
  point-in-time quality signals like "Preview" labels lose usefulness as guides for user
  selection. For Free/Student users who have no picker at all, preview labels on models
  are irrelevant by definition; for higher tiers where manual selection remains available,
  GitHub is also retiring the label based on the auto-manages-it rationale. This signals
  GitHub's view that model quality is managed by the routing layer, not by user-visible
  version labels. For Ch02: remove any guide advice that recommends "avoid Preview
  models" as a Copilot selection heuristic for Microsoft-released models — this label no
  longer exists. For Ch04: the model selection framework for Copilot should no longer
  include "(Preview) status" as a variable for Microsoft-released models.

### Claim 4: Auto model selection is described as dynamically selecting the best model for each task, framed as removing the need for manual choice

- **Evidence**: Official changelog presents this as the rationale for why manual selection
  is no longer needed for Free/Student plans.
- **Confidence**: settled (framing stated in official changelog; "best model for each task"
  is vendor promotional language without independent verification in this source)
- **Quote**: "dynamically selects the best model for each task, removing the need for
  manual choice"
- **Our assessment**: This framing is consistent with VS Code auto marketing language
  (issue #844, Claim 1: "select the optimal model"). However, the CLI auto note (issue
  #203, Claim 2) documents that CLI auto routing is NOT task-aware — it routes on plan +
  policies + rate-limit pressure. If the Free/Student auto pool behaves like CLI auto, the
  "best model for each task" claim is promotional rather than technically accurate. If it
  behaves like VS Code auto (which does evaluate task dimensions, per issue #844 Claim 1),
  it may be more accurate. The source does not clarify which routing mechanism applies.
  For the guide: do not recommend auto on Free/Student as "task-optimal routing" without
  confirming which routing heuristic applies to this surface and plan tier.

### Claim 5: The change establishes a plan-tier boundary on model selection MODE — Free and Student tiers have auto-only; paid tiers implicitly retain manual selection capability

- **Evidence**: The announcement scopes the change to "Free and Student plans" specifically.
  By implication, Pro and Pro+ are not addressed, suggesting they retain manual selection.
  This is not explicitly stated for Pro/Pro+ in this changelog.
- **Confidence**: emerging (tier boundary strongly implied by scoping to Free and Student;
  explicit confirmation of Pro/Pro+ retention of manual selection not found in this changelog)
- **Quote**: (no direct quote confirming paid tier retention of manual selection; "Free and
  Student plans" scope implies the change is limited to these tiers)
- **Our assessment**: Prior plan-tier differences in the corpus focused on WHICH models
  are accessible (Opus from Pro per issue #289 Claim 5; GPT-5.3-Codex picker removal on
  Student per issue #447 Claim 1). This source adds differentiation on HOW models are
  selected: lower-tier (free/educational) plans have no manual picker; paid tiers appear to
  retain it. For Ch04: the model selection chapter should distinguish (a) model availability
  — which models are in scope per plan — from (b) model selection mode — can the user choose
  manually or is auto routing mandatory. This source establishes that the latter is also
  plan-gated as of June 24, 2026.

## Concrete Artifacts

### Model Selection Mode by Plan Tier (as of June 24, 2026)

```
GitHub Copilot — Model Selection Mode per Plan Tier

FREE:
  Model selection mode:  AUTO ONLY (manual selection removed)
  Auto pool:             Multiple model families, subject to plan restrictions
  Manual picker:         NOT available

STUDENT:
  Model selection mode:  AUTO ONLY (manual selection removed)
  Auto pool:             Multiple model families, subject to plan restrictions
  Manual picker:         NOT available

PRO ($10/month):
  Model selection mode:  Manual selection retained (implied; not explicitly
                         confirmed in this changelog)
  Auto option:           Available (documented in prior sources)

PRO+:
  Model selection mode:  Manual selection retained (implied; not explicitly
                         confirmed in this changelog)
  Auto option:           Available (documented in prior sources)

ENTERPRISE / BUSINESS:
  Not addressed in this changelog (scoped to individual Free and Student plans)
```

*Source: GitHub Copilot official changelog, June 24, 2026*

### "(Preview)" Label Retirement — Microsoft-Released Models

```
Change:    Removal of "(Preview)" designation from Microsoft-released Copilot models
Scope:     All Copilot users (not scoped to Free/Student specifically)
Rationale: "Copilot auto model selection managing model routing and continuous
            improvements happening behind the scenes, these labels are no longer needed"
Effect:    Microsoft-released models in Copilot no longer carry "(Preview)" suffixes
```

*Source: GitHub Copilot official changelog, June 24, 2026*

### Plan-Tier Model Selection Mode Evolution (2026 Timeline)

```
April 20, 2026 (issue #289):
  Opus removed from Pro plan (model availability restriction)
  New signups paused for Pro, Pro+, Student
  Pro+ at >5× Pro usage limit headroom

April 27, 2026 (issue #447):
  GPT-5.3-Codex removed from Student picker; retained in Student auto pool
  Pattern introduced: "picker-removed but auto-retained" as third access state

June 1, 2026 (issue #1027):
  Evaluation models added to auto for individual non-enterprise users (opt-out default)
  Free and Student users (as individual non-enterprise users) included in scope

June 24, 2026 (this source, issue #1305):
  Manual picker FULLY REMOVED from Free and Student plans
  Auto becomes the ONLY model selection mechanism for Free and Student
  "(Preview)" label retired from Microsoft-released models across Copilot
```

## Cross-References

- **Corroborates** `docs-github-copilot-individual-plan-changes.md` (issue #289,
  Claim 8): That source documented GitHub framing plan restrictions as "to ensure
  service reliability and a sustainable Copilot experience for all users." This June
  24 source continues the same restriction pattern, applying it to model selection MODE
  (auto-only) rather than just model availability. The April 20 and June 24 sources
  together show consistent application of Free/Student tier restrictions across two
  dimensions: which models are accessible (April 20) and how models are selected (June 24).

- **Extends** `docs-github-copilot-student-gpt53codex-picker-removal.md` (issue #447,
  Claims 1 and 6): That source documented the first picker-level restriction for the
  Student plan — GPT-5.3-Codex removed from picker while retained in auto — introducing
  "picker-removed but auto-retained" as a new access state. Claim 6 noted this was "the
  first documentation of product-tier model access differentiation specifically for the
  Student (educational free) tier." This June 24 source completes that trajectory: the
  entire picker is eliminated for Student (and now also Free), making auto the only
  mechanism. The access-state introduced in April (auto-retained) is now the only
  available state for both Free and Student.

- **Extends** `docs-github-copilot-evaluation-models-individual-plans.md` (issue #1027,
  Claims 1 and 2): That June 1 source documented evaluation models as opt-out defaults
  in auto for individual non-enterprise users. Free and Student plan holders are individual
  non-enterprise users. Since this June 24 source makes auto the ONLY experience for
  Free/Student, these users now get evaluation models by default AND have no fallback to
  manual model selection to avoid them. The only lever is the opt-out setting documented
  in issue #1027. The two sources together define the complete model access picture for
  Free/Student as of late June 2026: auto-only + evaluation models included by default
  (opt-out via GitHub Copilot settings). This is an emergent implication that neither
  source documents explicitly on its own.

- **Extends** `docs-github-copilot-vscode-auto-model-selection.md` (issue #844, Claim 7):
  That source documented that VS Code auto users can "switch between Auto and any specific
  model at any time." This June 24 source removes that option for Free and Student users
  entirely — they cannot switch to a specific model at all. Claim 7 of issue #844 applies
  only to subscribers on plans that retain manual model selection (Pro, Pro+); it is not
  a feature of the Free or Student Copilot experience as of June 24, 2026. Guide content
  referencing that claim should qualify it with the plan-tier constraint.

- **Contradicts**: None. The complete removal of the manual picker from Free/Student is a
  progression of restrictions documented in prior sources (issue #447 for picker-level
  removal; issue #289 for model availability restrictions). No existing source note claims
  that Free or Student plans have unrestricted manual model selection.

- **Novel**:
  - First source in corpus to document the COMPLETE removal of the manual model picker
    from a Copilot plan tier. Prior sources documented model-by-model picker removals
    (Student GPT-5.3-Codex, issue #447) and model availability restrictions (Opus from
    Pro, issue #289). This is the first source to establish that auto-only is an enforced
    selection MODE at the plan tier level — not just a default or a preference.
  - First documentation that both Free AND Student plans share the same auto-only model
    selection restriction, treating them as a single governance tier for model selection
    purposes (distinct from Pro and Pro+).
  - First source to document the retirement of the "(Preview)" label for Microsoft-
    released Copilot models, with an explicit rationale tied to auto model routing making
    point-in-time quality labels unnecessary.

## Guide Impact

### Chapter 02: Harness Engineering / Tooling Landscape

- **Free and Student plan practitioners cannot do manual model selection**: Update any
  harness engineering guidance that includes model pinning steps — these steps are
  inapplicable for Free/Student users as of June 24, 2026. Workflows requiring a specific
  model (for reproducibility, capability tier, or provider-specific compliance) cannot be
  supported on Free or Student plans. Practitioners who need explicit model selection must
  upgrade to Pro or higher.
- **"(Preview)" label removal**: Remove any guide heuristics that advise against using
  "(Preview)"-labeled Microsoft models in Copilot — this label no longer exists. Selection
  guidance that relied on GA vs. Preview status for Microsoft-released models in Copilot
  must be updated; the relevant signal is now the plan tier and auto pool composition.

### Chapter 04: Model Selection and Cost Management

- **Add model selection MODE to the plan-tier comparison table**: Not just WHICH models
  are available, but HOW selection works. Free and Student: auto-only (no manual picker).
  Pro, Pro+: manual selection + auto option available. This is a new dimension in any
  Copilot plan selection matrix.
- **Free/Student users + evaluation models**: Combine this source with
  `docs-github-copilot-evaluation-models-individual-plans.md` (issue #1027) to document
  the complete model access picture for Free/Student as of late June 2026: auto-only,
  with evaluation models included by default unless the user visits GitHub Copilot
  settings to opt out. The auto-only policy means these users have no fallback to manual
  selection to avoid evaluation models — opt-out is their only lever.
- **Auto routing framing for Free/Student**: Document that auto model selection for
  Free/Student is mandatory. Caution against citing the "best model for each task" vendor
  framing as a technical guarantee of task-optimal routing — the routing heuristic (task-
  aware vs. availability-driven) is not specified in this changelog for the Free/Student
  context.

## Extraction Notes

1. **Source is short (~150–200 words of primary text)**: All substantive claims are
   exhausted above. Nothing was skimmed.
2. **Quote verification risk**: Both WebFetch calls returned content processed through an
   AI model rather than raw HTML. Key quotes (Claims 1, 3, and 4) were consistent across
   both independent fetches. The Assayer should verify these quotes directly against the
   source URL to confirm character-for-character accuracy.
3. **Pro/Pro+ manual selection retention not explicitly confirmed**: Claim 5 notes that
   the change is scoped to Free and Student; the implication that Pro/Pro+ retain manual
   selection is strong but not explicitly stated in this changelog. Confirm against
   current Copilot documentation before citing as a settled claim.
4. **Auto pool composition for Free/Student not specified**: The source states "multiple
   model families, subject to plan restrictions" without listing specific models. Guide
   recommendations about Free/Student auto access should reference current GitHub
   documentation on supported models rather than citing this source for specific model names.
5. **No contradictions to file**: The complete removal of the manual picker from Free/Student
   is a progression of the restrictions documented in prior sources (issues #447 and #289).
   No existing source note claims that Free or Student plans have unrestricted manual model
   selection. No contradiction issue required.
