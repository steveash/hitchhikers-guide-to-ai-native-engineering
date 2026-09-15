---
source_url: https://github.blog/changelog/2026-09-14-configure-cost-and-quality-in-copilot-auto-model-selection
source_type: docs
title: "Configure cost and quality in Copilot auto model selection"
author: GitHub (official changelog)
date_published: 2026-09-14
date_extracted: 2026-09-15
last_checked: 2026-09-15
status: current
confidence_overall: settled
issue: "#3447"
---

# Configure Cost and Quality in Copilot Auto Model Selection

> GitHub's September 14, 2026 changelog introduces three user-selectable "tiers"
> (Efficiency, Balance, Intelligence) that let users bias Copilot's auto model
> selection toward cost, a balance of cost/quality/latency, or quality — the
> first user-facing control over the cost/quality tradeoff in auto routing,
> layered on top of the existing task-complexity-aware routing already
> documented for VS Code, CLI, and Copilot Chat. Tiers are currently limited to
> VS Code, Copilot CLI, and the GitHub Copilot app; billing and the 10% paid-plan
> discount are unchanged.

## Source Context

- **Type**: docs (GitHub official product changelog, September 14, 2026, tagged
  "Release", ~150 words of primary announcement text, "1 minute read"). Cross-checked
  against the linked canonical documentation page,
  `docs.github.com/copilot/concepts/models/auto-model-selection`, which contains a
  substantially more detailed treatment of the same feature (a tier comparison table,
  worked per-tier routing examples, and scope caveats not present in the changelog
  post itself). Both pages were fetched directly (raw HTML) rather than through a
  rendering/summarization layer, so all quotes below are verbatim.
- **Author credibility**: GitHub engineering/docs team announcing and documenting a
  production feature. Authoritative for: the existence of the three tiers, their
  stated optimization targets, which surfaces support tiering, and the unchanged
  billing mechanics. Not a credible source for: the underlying routing algorithm's
  weighting logic between tiers, quantitative before/after cost or quality data,
  or how tier preference is actually surfaced/set in each product's UI (no
  screenshot or menu path is described in either page).
- **Scope**: Covers the three-tier configuration layer added on top of existing
  "auto with task optimization" routing across VS Code, Copilot CLI, and the
  GitHub Copilot app. Does NOT cover: Copilot Chat on github.com or Copilot cloud
  agent (the docs page explicitly excludes these from tiering), enterprise admin
  controls over which tiers are available to users, or any mechanism to set a
  default tier via `managed-settings.json` (unlike the `model: auto` policy lever
  documented for enterprises generally).

## Extracted Claims

### Claim 1: Auto model selection now offers three tiers — Efficiency, Balance, and Intelligence — that let users choose how auto weighs cost, quality, and response time per prompt
- **Evidence**: Direct feature description in both the changelog and the docs page's "Auto tier options" section, including a tier/priority/typical-use comparison table on the docs page.
- **Confidence**: settled
- **Quote**: "GitHub Copilot auto model selection now offers three tiers: efficiency, balance, and intelligence. Choose the tier that reflects how you want auto to weigh cost, quality, and response time for each prompt." (changelog body)
- **Our assessment**: This is a straightforward, unambiguous GA feature announcement from the primary vendor. We take the existence and naming of the three tiers at face value.

### Claim 2: Efficiency tier prioritizes cost and is suited to fast, straightforward tasks
- **Evidence**: Changelog per-tier description; corroborated by the docs page's tier table ("Priority: Cost") and worked example.
- **Confidence**: settled
- **Quote**: "Efficiency prioritizes keeping costs low and suits fast, straightforward tasks." (changelog body)
- **Our assessment**: Consistent with the general "small model for small tasks" framing GitHub has used across the entire auto-routing corpus (VS Code, CLI, Chat notes). Efficiency is essentially "auto, weighted harder toward the cheap end of the pool."

### Claim 3: Balance tier weighs cost, quality, and latency together and is the default fit for everyday work
- **Evidence**: Changelog per-tier description; docs page describes the same tier as "Balances cost, quality and latency" / "A good fit for everyday work."
- **Confidence**: settled
- **Quote**: "Balance weighs cost, quality, and latency together, and is a good fit for everyday work." (changelog body)
- **Our assessment**: Reads as the closest analog to auto's pre-tier behavior as documented in the VS Code/CLI/Chat notes already in the corpus — i.e., "Balance" is likely close to what auto did by default before tiers existed, with Efficiency and Intelligence as new bias knobs on either side.

### Claim 4: Intelligence tier prioritizes quality and is built for complex tasks, but can still route simple prompts to a small model
- **Evidence**: Changelog body, plus an explicit worked example on both pages showing that tier preference doesn't override per-prompt task evaluation.
- **Confidence**: settled
- **Quote**: "Intelligence prioritizes quality and is built for complex tasks... a simple task like adding a docstring to an existing function may use a small, efficient model even when auto is optimizing for intelligence." (changelog body)
- **Our assessment**: This is the most important nuance in the source: tiers are a *bias*, not a *floor* or a *forced* model class. A user who sets Intelligence should not expect every prompt — including trivial ones — to hit the most expensive model in the pool. This directly limits any "set Intelligence to guarantee premium-model quality" advice we might otherwise be tempted to give.

### Claim 5: All three tiers draw from the same set of available models — tiering changes preferred routing weighting per prompt, not the model roster itself
- **Evidence**: Explicit statement on the docs page, absent from the changelog itself.
- **Confidence**: settled
- **Quote**: "The same models remain available in each tier, but tiered routing changes how preferred models are selected for each task." (docs page, "Auto tier options" section)
- **Our assessment**: Important scoping detail the changelog omits — tiers are not an access-control mechanism (they don't gate which models a user can reach), only a routing-preference mechanism. Anyone wanting to restrict which models are reachable at all still needs the separate "Configuring access to AI models" admin policy path documented elsewhere in the docs page (and referenced, but not detailed, in this source).

### Claim 6: Tiers are currently available only in VS Code, Copilot CLI, and the GitHub Copilot app — not in Copilot Chat on github.com or Copilot cloud agent
- **Evidence**: Stated in both pages; the docs page repeats it as a standalone "Note" callout distinct from the general "auto with task optimization" availability list (which does include github.com Chat and cloud agent for task-aware routing generally, just not tiers specifically).
- **Confidence**: settled
- **Quote**: "This feature is currently rolling out in Visual Studio Code, Copilot CLI, and GitHub Copilot app." (changelog body); "Auto tiers are only available on VS Code, Copilot CLI, and GitHub Copilot app." (docs page, standalone Note)
- **Our assessment**: This is a real, citable scope limit — worth flagging in the guide so readers don't assume tier configuration is available everywhere auto itself is available. It's a narrower rollout than baseline task-aware auto routing, which per the existing `docs-github-copilot-chat-auto-model-selection.md` note (Claim 1) is GA on github.com and mobile, and per `docs-github-copilot-cca-auto-model-selection.md` (Claim 1) is available in Copilot cloud agent — neither of which gets tiers in this announcement.

### Claim 7: Billing is unchanged by tier selection — usage is still charged based on the model auto actually selects, regardless of tier, with the existing 10% paid-plan discount preserved
- **Evidence**: Explicit statement in both pages.
- **Confidence**: settled
- **Quote**: "Usage is charged based on the model auto selects, regardless of tier. Paid subscribers continue to receive a 10% discount on usage billed through auto." (changelog body)
- **Our assessment**: Consistent with every other auto-routing note in the corpus (CLI, VS Code, Chat, CCA all cite the same 10% discount). Choosing Intelligence does not carry a surcharge beyond whatever model auto ends up selecting for a given prompt — the cost lever is indirect (via routing bias), not a direct tier price.

### Claim 8: GitHub frames tiers as the first step toward broader user customization of model selection, with more visibility into tradeoffs to come
- **Evidence**: Forward-looking statement in the changelog body, not present on the docs page.
- **Confidence**: emerging
- **Quote**: "This is the first step in our journey toward letting you customize how model selection works for you, with more visibility into the tradeoffs you're making." (changelog body)
- **Our assessment**: A roadmap signal, not a shipped capability — we should treat "more visibility into tradeoffs" as a thing to watch for in future changelog entries, not something to recommend today. Flagged as emerging/anecdotal-adjacent since it's a stated intent rather than a described mechanism.

## Concrete Artifacts

Tier comparison table, extracted verbatim from the docs page (`docs.github.com/copilot/concepts/models/auto-model-selection`, "Auto tier options" section — this table does not appear in the changelog post itself):

```
Tier          | Priority | Typical use
--------------|----------|--------------------------------
Efficiency    | Cost     | Well suited to fast, straightforward tasks.
Balance       | Balances cost, quality and latency | A good fit for everyday work.
Intelligence  | Quality  | Built for complex tasks.
```

Per-tier routing examples, verbatim from the docs page:

```
Efficiency: All prompts are routed to the most cost-efficient and
appropriately capable model for the task.

Balance: For each prompt, the model is selected by considering cost,
quality, and latency, to provide cost effective and efficient
performance appropriate to the complexity of each prompt.

Intelligence: Prompts are evaluated for which model would provide the
highest quality response. A simple prompt could still be routed to a
smaller model, while a complex prompt is routed to the most capable
model for that task.
```

Docs page availability note (verbatim):

```
Auto tiers are only available on VS Code, Copilot CLI, and GitHub
Copilot app.
```

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-vscode-auto-model-selection.md` (Claim 1, Claim 4) — task-complexity-aware
    routing and the 10% discount mechanic that tiers now sit on top of.
  - `docs-github-copilot-cli-auto-model-selection-task-based-routing.md` (Claim 2, Claim 7) —
    the four-dimension task evaluation and 10% discount preserved under the newer
    AI-credits billing model; this source doesn't contradict that billing shift, it's silent on
    billing units entirely and only reaffirms the discount percentage.
  - `docs-github-copilot-chat-auto-model-selection.md` (Claim 3, Claim 8) — same 10% discount
    figure and the same "task complexity + availability" routing framing, now with tiers added
    as a user-facing bias on top for the surfaces that support it.
- **Contradicts**: None identified. This source is additive (a new configuration layer) rather
  than revising prior routing-mechanism claims.
- **Extends**:
  - `docs-github-copilot-cca-auto-model-selection.md` and `docs-github-copilot-chat-auto-model-selection.md` —
    both describe surfaces that have baseline auto/task-aware routing but are explicitly
    excluded from the new tier control (Claim 6 above), so this source narrows the "which
    surfaces have which auto capability" picture the corpus has been building since April 2026.
  - `docs-github-copilot-enterprise-auto-model-default.md` — that note documents an admin-side
    `model: auto` lever in `managed-settings.json`; this source does not mention any equivalent
    admin-side default-tier policy, which is a gap worth watching for in a future changelog entry.
- **Novel**: The tier concept itself (Efficiency/Balance/Intelligence) is new to the corpus —
  no prior source note documents any user-settable bias on the cost/quality/latency tradeoff
  within auto; all prior notes document only the underlying routing heuristic (task complexity,
  availability, plan/policy constraints) as opaque to the user. `docs-ghaw-cost-management.md`
  covers cost management for GitHub Agentic Workflows (Actions-based CI workflows), a distinct
  product surface from Copilot's IDE/CLI/app auto routing — not a real overlap despite similar
  topic keywords.

## Guide Impact

- **Chapter 04 (Model Selection and Cost Management)**: Currently, guide material drawing on the
  CLI/VS Code/Chat auto notes should describe auto routing as a black box that balances task
  complexity against availability, with no user lever beyond turning auto on/off or pinning a
  specific model. This source justifies adding: "as of September 2026, VS Code, Copilot CLI, and
  the GitHub Copilot app expose a three-tier bias (Efficiency/Balance/Intelligence) for auto
  model selection — pick Efficiency for low-stakes/high-volume tasks to bias cost down, Intelligence
  for tasks where getting the best available model matters more than cost, understanding that tier
  choice biases routing rather than guaranteeing a model class." Should also caveat that tiers are
  not yet available for Copilot Chat on github.com or Copilot cloud agent, so guidance for those
  surfaces should not reference tiers.
- **Chapter 05 (team tooling configuration)**: No admin/team-level control over tiers is documented
  in this source (contrast with `docs-github-copilot-enterprise-auto-model-default.md`'s
  `managed-settings.json` lever for defaulting to auto generally). Guide should not claim teams
  can set an org-wide default tier — that capability is not shown to exist yet.

## Extraction Notes

- Followed the changelog's outbound link to the canonical docs page
  (`docs.github.com/copilot/concepts/models/auto-model-selection`) since it contained
  substantially more detail (the tier table, worked examples, and the VS Code/CLI/app-only
  scope note) than the ~150-word changelog post alone. Did not follow the second linked page
  ("updated selection of models available" / supported-models reference) or the "Upcoming
  deprecation of selected GitHub Copilot models" changelog entry it also links to, since neither
  is about tier configuration specifically and the Prospector's key question is scoped to the
  cost/quality configuration mechanism.
- Both pages were fetched as raw HTML and parsed directly (not through a summarizing fetch layer)
  specifically so that all quotes above are character-for-character from the source, per the
  Miner quote-verification requirement.
- No screenshot or exact UI menu path (e.g., a settings dropdown location) is described in
  either source page — this is a real documentation gap, not an extraction omission on our part.
