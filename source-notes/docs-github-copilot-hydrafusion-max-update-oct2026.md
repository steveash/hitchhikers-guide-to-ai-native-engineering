---
source_url: https://github.blog/changelog/2026-10-14-hydrafusion-updates-and-new-max-option
source_type: docs
title: "HydraFusion updates and new Max option"
author: GitHub (official changelog)
date_published: 2026-10-14
date_extracted: 2026-10-15
last_checked: 2026-10-15
status: current
confidence_overall: emerging
issue: "#4126"
---

# HydraFusion updates and new Max option

> GitHub's October 14, 2026 changelog updates the HydraFusion multi-model orchestrator (new model pool, per-stage reasoning effort, a Cascade judging step, a tool-using Critique with parallel critics) and adds a "Max" tier. It is vendor-asserted, with no benchmarks, costs, or routing details.

## Source Context

- **Type**: docs (GitHub official changelog, 2-minute read)
- **Author credibility**: GitHub's own changelog. It is authoritative for what changed and for availability. It is not authoritative for performance, because the page gives no measurements.
- **Scope**: Covers the model pool, per-step reasoning effort, Cascade and Critique workflow changes, the HydraFusion Max tier, and plan availability. It does not cover benchmarks, cost or token numbers, how the router picks a workflow, or what tools the critics get. The page links to HydraFusion documentation and a community discussion; neither was followed.

## Extracted Claims

### Claim 1: The HydraFusion model pool now includes Claude Opus 5.5, GPT-6 Astra, GPT-6.1 Sol, and GPT-6 Luna, and which model runs depends on the workflow
- **Evidence**: Vendor statement only. No pool-composition or per-model role detail.
- **Confidence**: emerging
- **Quote**: "HydraFusion and HydraFusion Max draw from a pool that now includes Claude Opus 5.5, GPT-6 Astra, GPT-6.1 Sol, and GPT-6 Luna. The models used for each task vary based on the orchestration workflow."
- **Our assessment**: The pool changed, so the September benchmark comparison against an Opus 5 baseline (`docs-github-copilot-weekly-releases-sept7-2026.md` Claim 4) describes an older configuration. Do not carry those percentages over to the current system. It is unstated which model plays drafter, judge or critic.

### Claim 2: Reasoning effort is now set per stage (medium for drafts, high for review), replacing each model's default effort
- **Evidence**: Vendor statement with a one-sentence rationale. No data on its effect.
- **Confidence**: emerging
- **Quote**: "With this update, it explicitly tailors effort to each stage, using medium effort for initial drafts and high effort for review."
- **Our assessment**: This is a concrete, reusable harness pattern: spend cheap reasoning on generation and expensive reasoning on verification. It matches the intuition that checking is where extra thinking pays off, but GitHub shows no ablation. Treat it as a design choice, not a measured result.

### Claim 3: Cascade can now include a judging step that inspects the initial work and requests a repair only when needed
- **Evidence**: Vendor description of a before/after change.
- **Confidence**: emerging
- **Quote**: "It can now include a judging step that inspects the initial work and requests a repair only when needed."
- **Our assessment**: Sept 7 Claim 3 described Cascade as a quality gate that accepts or escalates to a stronger model. The new wording adds "repair" as an alternative to escalating. It is unclear whether the repair is done by the original model or by a stronger one. Note the hedge "can now include": the judge is optional.

### Claim 4: Critique now relies more on tools that inspect the actual workspace rather than text summaries, and uses parallel critic models
- **Evidence**: Vendor description of a before/after change.
- **Confidence**: emerging
- **Quote**: "It now relies more on tools to inspect the actual workspace directly. Critique now also uses parallel critic models to inspect work."
- **Our assessment**: This is the item the triage flagged. Sept 7 Claim 5 quoted an "Isolated review" principle: review steps run "in isolated, tool-less contexts." The new text says critics use tools on the actual workspace. The two cannot both hold literally for the same critic. Plausible reconciliations: the isolation principle was relaxed; the tools are read-only inspection tools; or the Sept 7 principle was imprecise. The changelog does not say. The old Critique was described as relying "heavily on text summaries," which suggests the move from summary-fed critics to inspecting the workspace directly is a response to critics missing real state. Whether write protection is retained is unknown, so do not assume it. See the Contradicts note below.

### Claim 5: HydraFusion Max uses the same architecture and workflows but is tuned for frontier capability, applying higher reasoning effort while still considering token efficiency
- **Evidence**: Vendor description plus a two-row comparison table.
- **Confidence**: emerging
- **Quote**: "It applies higher reasoning efforts where depth and thoroughness matter most, while still using orchestration to consider token efficiency."
- **Our assessment**: This is a cost/quality dial on top of a router, similar to effort tiers elsewhere in the corpus. The table calls standard HydraFusion "Balanced approach with moderate token savings." The savings are relative to something unspecified (presumably running a single frontier model). "Frontier capability" is marketing language with no supporting numbers.

### Claim 6: Availability is research preview on Pro, Pro+, Business and Enterprise with preview features enabled, in VS Code, the Copilot app and Copilot CLI, subject to model policy
- **Evidence**: Vendor statement.
- **Confidence**: settled (as to availability as stated)
- **Quote**: "HydraFusion and HydraFusion Max are available on Copilot Pro, Pro+, Business, and Enterprise plans with experimental or preview features enabled, subject to your organization's model policies."
- **Our assessment**: Sept 7 described HydraFusion as CLI-only (`/experimental`) and the Sept VS Code note covers a picker entry. It is now stated as available across all three clients. Organization admins control it through the normal model policy.

## Concrete Artifacts

Comparison table from the changelog (reproduced from source):

```
Option          | Description                                                       | Typical use case
HydraFusion     | Balanced approach with moderate token savings.                    | Agentic tasks that require a balance of speed, cost, and performance.
HydraFusion Max | Frontier capability for more demanding tasks, with token          | Tasks requiring the deepest possible reasoning and most thorough analysis.
                | efficiency considered through orchestration.                      |
```

Workflow before/after (GitHub changelog, paraphrased from "Optimized Cascade and Critique workflows"): Cascade went from initial model plus escalation to adding an optional judge that triggers repair. Critique went from text-summary-based review to tool-based workspace inspection with parallel critics.

## Cross-References

- **Corroborates**: `docs-github-copilot-opus55-availability.md` (Claude Opus 5.5 is in Copilot; the pool includes it).
- **Contradicts**: `docs-github-copilot-weekly-releases-sept7-2026.md` Claim 5 ("Isolated review ... tool-less contexts") versus Claim 4 here (critic "relies more on tools to inspect the actual workspace"). This is a time-ordered change in the same product, so it may be an update rather than a true conflict. No contradiction issue was filed because the new source does not say the isolation guarantee was dropped; the Smith should treat the isolation claim as unverified for the current version.
- **Extends**: `docs-github-copilot-weekly-releases-sept7-2026.md` Claim 3 (Single/Cascade/Critique patterns) and Claim 4 (benchmarks, now tied to an older pool); `docs-github-copilot-vscode-september-2026.md` Claim 1 (HydraFusion picker entry); `docs-github-copilot-vscode-auto-model-selection.md` (single-model routing, which HydraFusion generalizes).
- **Novel**: Per-stage reasoning-effort tailoring; the optional Cascade judge with repair; parallel critics; the Max tier.

## Guide Impact

- **Chapter 02 (model selection / routing)**: Where HydraFusion is described, update it to the October state: the new pool, per-stage effort, and the Max tier as a cost/quality selector. Label all of it vendor-asserted and unmeasured.
- **Chapter 04 (agentic workflows / multi-model review)**: Use the per-stage effort split (medium to draft, high to review) and the parallel-critic pattern as a documented example. Do not repeat the "tool-less isolated critic" claim without noting that GitHub's later description has critics using workspace tools.
- **Chapter 03 (verification)**: The Cascade judge-then-repair-only-if-needed design is an example of conditional verification. Cite it as GitHub's design, not as evidence of effectiveness.
- **Chapter 06**: Keep HydraFusion listed as a research-preview router; there is still no independent evidence.

## Extraction Notes

- The page was fetched and read in full (short changelog). The linked HydraFusion docs and community discussion were not followed. Quotes were checked against the raw page text.
- The source has no metrics. All behavioral claims are GitHub's self-description.
- Prior issue #3829 was closed as a duplicate of the Sept 7 coverage; this entry has new content (Max, the new pool, workflow changes), so it is not a duplicate.
