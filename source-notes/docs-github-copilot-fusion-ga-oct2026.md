---
source_url: https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion
source_type: docs
title: "Route and orchestrate models with GitHub Copilot Fusion"
author: GitHub (official changelog)
date_published: 2026-10-28
date_extracted: 2026-11-01
last_checked: 2026-11-01
status: current
confidence_overall: emerging
issue: "#4472"
---

# Route and orchestrate models with GitHub Copilot Fusion

> GitHub's Oct 28, 2026 changelog announces GA of Copilot Fusion (the renamed HydraFusion) with Standard/High/Max effort tiers, a per-prompt Single/Cascade/Critique workflow taxonomy, enterprise admin model-policy controls, and first vendor-asserted benchmark and cost figures with no methodology.

## Source Context

- **Type**: docs (GitHub official changelog)
- **Author credibility**: GitHub's own changelog. Authoritative for availability, naming, admin controls and billing terms. Not authoritative for performance: the benchmark figures are vendor-reported and no methodology, sample or task set is given on the page.
- **Scope**: GA, effort tiers, workflow taxonomy, benchmark/cost claims, one customer testimonial (AT&T), admin controls, billing, availability, migration of research-preview selections. Does not say how the router picks a workflow, which models play which role, or what baseline configuration the cost comparison used. Linked pages were not followed.

## Extracted Claims

### Claim 1: Copilot Fusion is GA; users pick "Copilot Fusion" plus an effort level instead of a specific model
- **Evidence**: Vendor announcement.
- **Confidence**: settled (as to the announced status)
- **Quote**: "GitHub Copilot Fusion is generally available."
- **Our assessment**: This ends the research-preview status described in `docs-github-copilot-hydrafusion-max-update-oct2026.md`. The model-picker UX is "select Copilot Fusion in the model picker, then choose the effort level" (source wording: "To use it, select Copilot Fusion in the model picker, then choose the effort level."). Guide text calling it "research preview" is now stale.

### Claim 2: Three user-facing effort tiers (Standard, High, Max) replace HydraFusion / HydraFusion Max and Auto
- **Evidence**: Vendor description of each tier. No data on what models each tier selects.
- **Confidence**: emerging
- **Quote**: "Prioritizes versatile models for everyday coding." (Standard); "Prioritizes capable models for challenging tasks and deeper reasoning." (High); "Prioritizes the most capable models for the most demanding tasks and complex reasoning." (Max)
- **Our assessment**: The user controls a cost/quality dial; the router controls the model and workflow. Tier definitions are qualitative only. The Oct 14 two-option table (HydraFusion / HydraFusion Max) has been expanded to three tiers.

### Claim 3: A router chooses among Single, Cascade and Critique workflows per task
- **Evidence**: Vendor description of each workflow; no description of the selection logic.
- **Confidence**: emerging
- **Quote**: "An efficient model drafts a response. A quality check determines whether to accept it or escalate to a stronger model." (Cascade); "One model drafts an initial response, another model reviews it, and the original model revises." (Critique); "One model solves the task directly." (Single)
- **Our assessment**: Consistent with Sept 7 Claim 3 (same three patterns). The GA text describes Cascade as accept-or-escalate (a quality gate) and does not mention the "judge and request repair" step from the Oct 14 note (Claim 3 there); it is unclear whether that is a simplification or a change. It also does not say whether Critique reviewers have workspace tools (Oct 14 Claim 4) or are tool-less (Sept 7 Claim 5). The GA page is silent, so it neither resolves nor deepens that open question. How the router picks a workflow is still undisclosed.

### Claim 4: Fusion Max scored 60 on the Artificial Analysis Coding Agent Index, within two points of Claude Code with Opus 5.5 Max, at about half the cost, tokens and ~40% less time (VENDOR-ASSERTED)
- **Evidence**: Vendor-reported numbers. No methodology, task set, sample size, run count, baseline configuration or link to the index run is given on the page.
- **Confidence**: anecdotal (unverified vendor claim; treated as such)
- **Quote**: "In the Artificial Analysis Coding Agent Index, Copilot Fusion Max scored 60" (the page continues that this is within two points of Claude Code with Opus 5.5 Max); "at about half the average API cost per task"; "using about half as many tokens and taking about 40% less time per task."
- **Our assessment**: Do not carry into the guide as measured fact. It is a "within two points" claim (i.e. slightly lower than the baseline) paired with cost savings; "average API cost" is not the same as what Copilot users are billed. Unlike Sept 7 Claim 4 (internal benchmarks vs. Opus 5, TerminalBench/DeepSWE/CheckpointBench) this cites a third-party index, but the page does not show that the index run is independently reproducible. The Sept 7 percentages describe an older model pool and a different baseline; the two sets of numbers are not comparable.

### Claim 5: Admins control which models Fusion can use and whether it is the default
- **Evidence**: Vendor description of policy behavior.
- **Confidence**: settled (as stated product behavior; not tested)
- **Quote**: "Copilot Fusion only uses the models that are enabled in your enterprise and organization model policies."
- **Our assessment**: Fusion inherits existing model governance rather than bypassing it, which matters for orgs that have restricted vendors. The page also says admins can disable models for Fusion only (without disabling them for everyone) and can see which models Fusion picks from. Exact quote for default-setting: "Administrators can set Copilot Fusion, at any effort level, as the default model" (page continues: via Enterprise managed settings). Useful for Ch05/Ch06 as a concrete governance lever.

### Claim 6: Billing is per underlying model at standard rates, with a time-limited 30% discount on paid plans
- **Evidence**: Vendor billing statement. No end date given in the text we extracted.
- **Confidence**: settled (as to the stated terms); the discount is a dated promotion
- **Quote**: "For a limited time, users on paid Copilot plans will receive a 30% discount on model costs when using Copilot Fusion."
- **Our assessment**: Record the discount as a promotion, not standing pricing. Per-model billing matches Sept 7 Claim 7 (billing by underlying model tokens). Since a multi-leg workflow bills every leg, the "half the cost" claim (Claim 4) is relative to the benchmark baseline, not to a user's own prior bill.

### Claim 7: Availability is all Copilot plans, across VS Code, the Copilot app, Copilot CLI and JetBrains; research-preview selections migrate automatically
- **Evidence**: Vendor statement.
- **Confidence**: settled (as stated availability)
- **Quote**: "Copilot Fusion is available on all Copilot plans in Visual Studio Code" (page lists the Copilot app, Copilot CLI and JetBrains IDEs, with more clients planned); "if you previously enabled auto, HydraFusion, or HydraFusion Max, your selections will automatically transition"
- **Our assessment**: Broadens availability beyond the Oct 14 note (Claim 6: Pro through Enterprise with preview features, VS Code/app/CLI) to all plans and JetBrains. The migration statement indicates that Fusion subsumes single-model Auto as well as HydraFusion, i.e. the Auto routing in `docs-github-copilot-cca-auto-model-selection.md` is merged into Fusion's Standard tier at least in the picker.

### Claim 8: Customer testimonial (AT&T) credits Fusion Standard with improved token efficiency
- **Evidence**: Single customer quote from a named principal engineer; no metrics.
- **Confidence**: anecdotal
- **Quote**: "Copilot Fusion eliminates that friction, optimizing model selection without requiring developers to manage it themselves."
- **Our assessment**: Marketing testimonial; carries no data. Useful only as evidence that the pitch is "remove the model-choice burden from developers."

## Concrete Artifacts

```
Effort tiers (GitHub changelog, 2026-10-28):
Standard: "Prioritizes versatile models for everyday coding."
High:     "Prioritizes capable models for challenging tasks and deeper reasoning."
Max:      "Prioritizes the most capable models for the most demanding tasks and complex reasoning."

Workflows (same source):
Single:   "One model solves the task directly."
Cascade:  "An efficient model drafts a response. A quality check determines whether to accept it or escalate to a stronger model."
Critique: "One model drafts an initial response, another model reviews it, and the original model revises."
```

Vendor-asserted figures (summary of the source's claims; NOT independently verified): Fusion Max = 60 on Artificial Analysis Coding Agent Index; within 2 points of Claude Code + Opus 5.5 Max; ~1/2 average API cost per task; ~1/2 tokens; ~40% less time. 30% model-cost discount for a limited time on paid plans.

## Cross-References

- **Corroborates**: `docs-github-copilot-weekly-releases-sept7-2026.md` Claim 3 (Single/Cascade/Critique patterns) and Claim 7 (billing by underlying model tokens). `docs-github-copilot-hydrafusion-max-update-oct2026.md` Claim 6 (admin model-policy governance and multi-client availability).
- **Contradicts**: None filed. Cascade here is "accept or escalate" with no repair step, while `docs-github-copilot-hydrafusion-max-update-oct2026.md` Claim 3 describes an optional judge that requests repair; and the GA page says nothing on whether critics are tool-less (Sept 7 Claim 5) or workspace-inspecting (Oct 14 Claim 4). These are omissions in a short announcement rather than opposing assertions, so no contradiction issue was opened. The Sept 7 benchmark (Claim 4) and this page's benchmark use different baselines and pools and are not comparable.
- **Extends**: `docs-github-copilot-hydrafusion-max-update-oct2026.md` (GA, rename, Standard/High/Max tiers, benchmark, discount); `docs-github-copilot-cca-auto-model-selection.md` Claim 1 (Auto routing, now merged into Fusion); `docs-github-copilot-weekly-releases-sept7-2026.md` Claim 2 (semantic routing across models).
- **Novel**: The Artificial Analysis index score and cost/token/time claims; the "Fusion only uses policy-enabled models" admin design including Fusion-only model disables and default-setting via Enterprise managed settings; the 30% limited-time discount; automatic migration of Auto/HydraFusion selections.

## Guide Impact

- **Chapter 02 (model selection / routing)**: Where HydraFusion is described, rename to Copilot Fusion (GA) with Standard/High/Max tiers and describe it as a router over Single/Cascade/Critique. Any benchmark figures must be labeled vendor-asserted; do not present "within two points at half the cost" as measured.
- **Chapter 01 (daily workflows)**: Add that the developer-facing choice is now an effort tier in the model picker rather than a model name.
- **Chapter 05 (team adoption)**: Cite the admin controls (inherit enterprise/org model policy; Fusion-only model disable; default-model via managed settings) as a rollout lever. Mention the 30% discount as a dated promotion, not a budgeting assumption.
- **Chapter 06 (governance)**: Fusion respects per-model enterprise policy, so model allow-lists still govern what a routed workflow can call.
- **Chapter 03/04**: Cascade (quality gate) and Critique (draft/review/revise) remain usable examples of conditional and cross-model verification; cite as GitHub's design, not as evidence of effectiveness.

## Extraction Notes

- The page was fetched through a summarizing fetch tool that limits quote length to under ~125 characters, so quotes are contiguous fragments and some long sentences are partially quoted with the remainder marked as paraphrase. Quotes should be spot-checkable against the page.
- Linked docs and discussions were not followed.
- Claim numbers cited from other notes were checked against the headings in those notes (Sept 7: Claims 2, 3, 4, 5, 7; Oct 14: Claims 3, 4, 6; CCA auto: Claim 1).
- All numbers are vendor-asserted; the AT&T quote is a testimonial with no metrics.
