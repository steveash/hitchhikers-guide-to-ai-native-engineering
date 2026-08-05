---
source_url: https://github.blog/changelog/2026-08-03-customize-the-reasoning-level-for-copilot-cloud-agent
source_type: docs
title: "Customize the reasoning level for Copilot cloud agent"
author: GitHub (official changelog)
date_published: 2026-08-03
date_extracted: 2026-08-05
last_checked: 2026-08-05
status: current
confidence_overall: settled
issue: "#2497"
---

# Customize the Reasoning Level for Copilot Cloud Agent

> GitHub's August 3, 2026 changelog announcing that Copilot cloud agent (CCA) users can
> now set a per-task reasoning level alongside model selection — extending the reasoning-level
> control first documented for VS Code, Copilot CLI, and the Copilot app on June 4, 2026 to
> the cloud agent surface, with the same "more tokens, more credits" cost framing but no
> surface-specific detail on which reasoning levels exist or which models support the control.

## Source Context

- **Type**: docs (GitHub official product changelog, August 3, 2026; a very short entry —
  "1 minute read" per the page's own label — of roughly 60-70 words of primary announcement
  text, plus a plan-availability sentence and a documentation link)
- **Author credibility**: GitHub engineering team announcing a production feature change to
  a named surface (Copilot cloud agent). Authoritative for: the existence of the reasoning-level
  control on CCA, the fact that it is selected per-task alongside the model, the qualitative
  cost/quality tradeoff, and plan-tier availability. Not a credible source for: which specific
  reasoning levels exist (names, count), which models "support" reasoning-level customization,
  the magnitude of the token/credit cost increase, or how this control interacts with CCA's
  existing auto model selection mode (`docs-github-copilot-cca-auto-model-selection.md`).
- **Scope**: A single-surface (Copilot cloud agent) feature announcement covering: what the
  control does, how it is invoked (picked alongside the model at task start), the cost/quality
  tradeoff, and plan eligibility. Does NOT cover: enumerated reasoning-level options, the list
  of "models that support it," admin-policy gating for Business/Enterprise, whether the setting
  is exposed via the CCA REST API (`docs-github-copilot-cca-rest-api-tasks.md`), or any
  quantitative token/credit cost data. The linked documentation page ("choosing the right AI
  model for your task") was checked directly and does not contain reasoning-level content —
  see Extraction Notes.

## Extracted Claims

### Claim 1: Copilot cloud agent users can now set the reasoning level for models that support it when delegating a task

- **Evidence**: Official GitHub product changelog stating the capability as a shipped feature
  ("you can now set").
- **Confidence**: settled (product fact — stated in official changelog as a released feature)
- **Quote**: "When you delegate a task to GitHub Copilot cloud agent, you can now set the reasoning level for models that support it."
- **Our assessment**: This is the core claim of the source. The "models that support it"
  qualifier is the same access-gating pattern used in the June 4, 2026 announcement for VS
  Code/CLI/app (`docs-github-copilot-1m-context-reasoning-levels.md` Claim 6: "accessed by
  selecting supported models"), and, as with that source, the specific supported-model list is
  not named here either. This is the first corpus documentation of reasoning-level customization
  as a feature specifically on the Copilot cloud agent surface — CCA was not among the three
  surfaces (VS Code, Copilot CLI, GitHub Copilot app) named in the June 4 announcement.

### Claim 2: Reasoning level controls how much the model reasons before responding, trading answer quality on complex problems against token (and therefore credit) consumption

- **Evidence**: Official changelog stating both the mechanism (amount of reasoning before
  responding) and the explicit cost consequence in the same sentence.
- **Confidence**: settled (mechanism and cost tradeoff stated directly in official changelog)
- **Quote**: "This allows you to control how much the model reasons before it responds. A higher level can improve answers to complex problems, but it consumes more tokens, and therefore more credits."
- **Our assessment**: This restates, on the CCA surface, the same qualitative cost framing
  GitHub used for VS Code/CLI/app reasoning levels on June 4: "Choosing a larger context window
  or higher reasoning level will consume more AI credits per interaction"
  (`docs-github-copilot-1m-context-reasoning-levels.md` Claim 5). Both sources agree that higher
  reasoning is a credits lever, not a free quality upgrade — but neither source quantifies the
  multiplier. For CCA specifically, this now adds a fourth independently-selectable cost/quality
  axis alongside the three already documented for CCA: model tier (0.33x/1x/>1x per
  `docs-github-copilot-cca-cost-efficient-models.md`), auto vs. explicit model routing (10%
  discount per `docs-github-copilot-cca-auto-model-selection.md` Claim 3), and now reasoning
  level.

### Claim 3: Reasoning level is selected alongside the model at task start and applies for that run

- **Evidence**: Official changelog describing the UX/invocation mechanism directly.
- **Confidence**: settled (invocation mechanism stated in official changelog)
- **Quote**: "Pick a reasoning level alongside the model when you start a task, and Copilot cloud agent will use it for the run."
- **Our assessment**: This establishes reasoning level as a per-task setting, not a session-,
  account-, or org-wide default — consistent with how CCA's existing model picker already works
  (pick model → "Auto" or explicit tier — at task submission time, per
  `docs-github-copilot-cca-auto-model-selection.md` Claim 5). "For the run" implies the chosen
  level is fixed for the full lifetime of that delegated task and cannot be changed mid-task.
  Whether this per-task setting is exposed as a parameter on the CCA REST API
  (`docs-github-copilot-cca-rest-api-tasks.md`) is not addressed by this source — a documentation
  gap for teams that script CCA task submission rather than using the picker UI.

### Claim 4: The feature is available on all paid Copilot plans that include Copilot cloud agent — Pro, Pro+, Business, Enterprise, and Max

- **Evidence**: Official changelog states the plan-eligibility list explicitly and frames it
  as coextensive with CCA access generally ("all paid Copilot plans that include Copilot cloud
  agent").
- **Confidence**: settled (plan eligibility stated in official changelog)
- **Quote**: "This is available on all paid Copilot plans that include Copilot cloud agent (i.e., Copilot Pro, Pro+, Business, Enterprise, and Max)."
- **Our assessment**: Notably, this eligibility list includes standard Copilot Pro — a contrast
  with the Claude Opus 4.8 fast-mode rollout, where "Pro and Pro+ subscription tiers are NOT
  listed — the eligible tiers are Pro+, Max, Business, and Enterprise" and "Practitioners on the
  standard Pro plan ($10/month) cannot access fast mode" (`docs-github-copilot-opus48-fast-mode-preview.md`
  Claim 5). Reasoning-level customization on CCA is gated only by whether the plan includes CCA
  at all, not by a higher premium tier the way fast mode is. Free and Student plans are not
  listed, consistent with Free/Student plans already lacking manual model-selection UI on other
  surfaces (`docs-github-copilot-free-student-auto-only-model-selection.md` Claim 1) — though
  this source does not state whether Free/Student even have CCA access to begin with, so the
  exclusion may simply follow from CCA plan eligibility rather than a reasoning-level-specific
  restriction.

### Claim 5: GitHub points to its general "choosing the right AI model for your task" documentation as the reference for this feature, but that page does not itself document reasoning-level configuration

- **Evidence**: The changelog entry links to
  `https://docs.github.com/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task`.
  We fetched that linked page directly to check for reasoning-level detail (level names,
  model list, cost specifics) per the MINER.md instruction to follow substantive linked pages.
- **Confidence**: settled (the changelog does link to this page; the page's lack of
  reasoning-level content is a direct observation, not an inference)
- **Quote**: (no direct quote; see paraphrase in Our assessment — the linked doc page itself
  was fetched and summarized, not quoted, since the task here was to check for the presence
  of specific content, not extract prose from that page)
- **Our assessment**: The linked documentation page covers model selection by task type
  (general-purpose vs. fast-help vs. deep-reasoning) and a general credit-consumption note
  ("Different models consume AI credits at different rates based on their token pricing"), but
  contains no reasoning-level-specific configuration guidance, no enumeration of reasoning
  levels, and no CCA-specific detail. This confirms the documentation gap already flagged for
  the June 4 announcement: `docs-github-copilot-1m-context-reasoning-levels.md` Extraction Note
  3 states "Neither WebFetch pass surfaced specific level names... The announcement describes
  the capability conceptually... without naming the specific options." As of August 3, 2026,
  that gap still has not been closed by GitHub's own linked documentation — practitioners must
  discover the actual reasoning-level options and supported-model list from the product UI
  itself, not from published docs.

## Concrete Artifacts

### Announcement Verbatim (August 3, 2026)

```
Title:   Customize the reasoning level for Copilot cloud agent
Date:    August 3, 2026 (1 minute read)
Source:  https://github.blog/changelog/2026-08-03-customize-the-reasoning-level-for-copilot-cloud-agent

Primary text:
"When you delegate a task to GitHub Copilot cloud agent, you can now set the
reasoning level for models that support it. This allows you to control how
much the model reasons before it responds. A higher level can improve answers
to complex problems, but it consumes more tokens, and therefore more credits.
Pick a reasoning level alongside the model when you start a task, and Copilot
cloud agent will use it for the run."

Plan availability:
"This is available on all paid Copilot plans that include Copilot cloud agent
(i.e., Copilot Pro, Pro+, Business, Enterprise, and Max)."

Documentation link:
"choosing the right AI model for your task"
-> https://docs.github.com/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task

Tag: copilot (https://github.blog/changelog/2026/?label=copilot)
```

### Reasoning-Level-by-Surface Coverage (synthesized across corpus, as of August 3, 2026)

```
Surface                 Reasoning level control    First documented
──────────────────────────────────────────────────────────────────────
VS Code                 Yes                         2026-06-04 (#1101)
Copilot CLI              Yes                         2026-06-04 (#1101)
GitHub Copilot app       Yes                         2026-06-04 (#1101)
Copilot cloud agent      Yes                         2026-08-03 (this source, #2497)
Eclipse (thinking effort — possibly related capability)  2026-06-02 (docs-github-copilot-eclipse-byok-skills-chat.md)
JetBrains, Visual Studio, github.com web, GitHub Mobile   Not documented in corpus as of 2026-08-05

Note: Level names/count and the specific "models that support it" list are
undocumented on every surface above — this is a standing gap across the
entire corpus, not something unique to the CCA announcement.
```

## Cross-References

- **Extends** `docs-github-copilot-1m-context-reasoning-levels.md` (issue #1101) Claim 6 and
  Claim 7: Claim 6 named the reasoning-level surfaces as of June 4, 2026 as "VS Code, Copilot
  CLI, and GitHub Copilot app" and explicitly noted "these features were not yet available in
  JetBrains, Eclipse, Visual Studio, or the GitHub web interface." Copilot cloud agent was not
  named at all — neither as available nor as explicitly excluded. Claim 7 of that note stated
  "Expansion of these features to additional surfaces is planned" (confidence: settled, though
  no exact expansion-language quote was confirmed) and recommended "practitioners on other
  surfaces should check the changelog for updates." This August 3 source is the concrete
  fulfillment of that predicted expansion for the CCA surface specifically.

- **Corroborates** `docs-github-copilot-1m-context-reasoning-levels.md` Claim 5: That claim
  quoted "Choosing a larger context window or higher reasoning level will consume more AI
  credits per interaction" as the cost framing for VS Code/CLI/app reasoning levels. This
  source's Claim 2 quote ("it consumes more tokens, and therefore more credits") restates the
  identical cost-quality tradeoff for the CCA surface. The two sources together confirm GitHub
  applies a consistent, but non-quantified, "more reasoning = more credits" cost narrative
  across every surface where reasoning levels ship.

- **Extends** `docs-github-copilot-cca-auto-model-selection.md` (issue #745) Claim 5: That
  source documented CCA's model-picker UX ("CCA auto is accessed by selecting 'Auto' in the
  model picker"). This source adds reasoning level as a second parameter selected at the same
  task-start moment ("Pick a reasoning level alongside the model when you start a task"). CCA
  task submission now involves at minimum two independently configurable dimensions: model
  (auto or explicit tier) and reasoning level (for supporting models).

- **Extends** `docs-github-copilot-cca-cost-efficient-models.md` (issue #818) Claim 4: That
  source described CCA's model selection as at least a three-tier cost structure (budget/
  standard/premium, by model). This source adds reasoning level as an orthogonal cost axis on
  top of model tier — a CCA task's total cost is now a function of both which model is chosen
  and what reasoning level is set for it, not model choice alone.

- **Contradicts**: None found. No existing source note makes a claim this source refutes; it
  is a straightforward surface-scope extension of an existing, settled feature.

- **Novel**:
  - **First corpus documentation of reasoning-level customization as a Copilot cloud agent
    (CCA) feature.** Prior reasoning-level documentation (issue #1101) covered VS Code, CLI,
    and the Copilot app only; CCA was not named in that announcement.
  - **First corpus documentation of plan-tier eligibility specifically for reasoning-level
    customization.** The June 4 source did not state plan-tier restrictions for reasoning
    levels at all; this source is the first to confirm the feature (on CCA) is tied to CCA
    plan access generally (Pro/Pro+/Business/Enterprise/Max) rather than a higher premium tier.
  - **First direct confirmation that GitHub's own linked documentation does not describe
    reasoning-level options**, obtained by fetching the linked "choosing the right AI model"
    page directly rather than inferring the gap from changelog silence alone.

## Guide Impact

- **Chapter 04 (Model Selection and Cost Management)**: Update the CCA model-selection cost
  framework (currently: model tier [Ch04, per `docs-github-copilot-cca-cost-efficient-models.md`]
  plus auto-vs-explicit routing [Ch04, per `docs-github-copilot-cca-auto-model-selection.md`])
  to add reasoning level as a third independently selectable cost/quality lever on CCA,
  specifically. Recommend documenting the same "default for everyday tasks, escalate for
  complex/architectural work" heuristic already given for VS Code/CLI/app
  (`docs-github-copilot-1m-context-reasoning-levels.md` Claim 4) as the provisional guidance for
  CCA reasoning level, since GitHub has not published CCA-specific reasoning-level guidance
  and the general heuristic is the closest available official signal.
- **Chapter 02 (Harness Engineering / Tooling Landscape)**: Teams that script CCA task
  submission via the REST API (`docs-github-copilot-cca-rest-api-tasks.md`) should verify
  whether reasoning level is exposed as an API parameter before assuming programmatic control
  — this source only confirms the picker-UI path ("Pick a reasoning level alongside the
  model when you start a task"). If the API does not yet expose it, automated CCA harnesses
  are currently limited to whatever reasoning level is the un-set default for their chosen
  model.
- **Chapter 03 (Evaluation and Quality)**: Note the practitioner-facing quality/cost tradeoff
  for CCA specifically: for complex or architecturally significant delegated tasks, a higher
  reasoning level is now an available lever (on supporting models) to improve output quality,
  at a credit cost. Teams doing quality postmortems on failed or low-quality CCA task results
  should check what reasoning level (if any) was selected before concluding the model itself
  was insufficient.

## Extraction Notes

1. **Source is extremely short**: The changelog page self-labels as a "1 minute read." Two
   independent WebFetch passes (one summarized, one requesting raw/verbatim text) returned
   fully consistent content — the same four sentences of primary text, the plan-availability
   sentence, and the documentation link. All substantive content is captured across the five
   claims above; nothing was skimmed or left unexamined.
2. **Followed the linked documentation page per MINER.md §1**: Fetched
   `https://docs.github.com/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task`
   directly to check for reasoning-level-specific content, since it was the only substantive
   link in the source. It contains general model-selection-by-task-type guidance but no
   reasoning-level detail — documented as Claim 5 rather than treated as a silent gap.
3. **No enumerated reasoning levels, no named supported-model list**: Consistent with the June
   4, 2026 announcement's same gap (`docs-github-copilot-1m-context-reasoning-levels.md`
   Extraction Notes 3 and 4), this source does not name the reasoning-level options or which
   models support the control. This is now a two-for-two pattern across both reasoning-level
   announcements in the corpus — flagged prominently rather than guessed at.
4. **No contradictions to file**: This source extends rather than conflicts with any existing
   corpus claim. No contradiction issue was filed.
5. **Relationship to Eclipse "thinking effort" is not clarified by this source**: The
   `docs-github-copilot-eclipse-byok-skills-chat.md` note documented a separate "thinking
   effort" selector for Eclipse; whether that is the same underlying capability as "reasoning
   level" on CCA is not addressed by either source. Left as an open question rather than
   asserted as either same or different.
