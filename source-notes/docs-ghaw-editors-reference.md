---
source_url: https://github.github.com/gh-aw/reference/editors
source_type: docs
title: "GitHub Agentic Workflows: Workflow Editors Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research); community contributors
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#381"
---

# GitHub Agentic Workflows: Workflow Editors Reference

> Documents the editor ecosystem for authoring gh-aw workflows — one
> officially supported Compiler Playground (browser-based, WebAssembly-powered)
> and two community tools (a 5-step guided prompt generator with empirical
> anti-patterns data from 679 workflows, and a graphical visual editor) — with
> the most actionable finding being statistical evidence that `slash_command`
> and `workflow_run` triggers have critically low success rates in practice.

## Source Context

- **Type**: docs (official gh-aw `reference/editors` page listing both
  official and community tooling for workflow authoring. Part of the Reference
  section, not the Setup or Guides sections. The page links out to three
  external tools: one official and two community-built.)
- **Author credibility**: The reference page itself is first-party from GitHub
  Next / Microsoft Research. The Compiler Playground at
  `https://github.github.com/gh-aw/editor/` is official. The two community
  editors (Agentic Prompt Generator by Ashley Wolf, Graphical Workflow Editor
  by Mossaka) are independent contributions — explicitly disclaimed as not
  officially supported. The Agentic Prompt Generator's anti-patterns section
  is community-generated empirical analysis from the tool author, not official
  gh-aw documentation. Treat it as practitioner empirical data (anecdotal
  confidence), not platform guarantees.
- **Scope**: The three workflow authoring tools documented on the editors
  reference page, plus the substantive content from the Agentic Prompt
  Generator sub-page (followed per MINER.md §1 as a linked substantive page).
  Does NOT cover: the gh-aw compilation model (see `docs-ghaw-wasm-compilation.md`
  and `docs-ghaw-compilation-process.md`), the authoring lifecycle (`docs-ghaw-
  agentic-authoring.md`), official workflow creation procedures
  (`docs-ghaw-setup-creating-workflows.md`), or debugging tools
  (`docs-ghaw-troubleshooting-debugging.md`).

## Extracted Claims

### Claim 1: The editors reference page formally distinguishes official tools (the Compiler Playground) from community tools (Agentic Prompt Generator, Graphical Workflow Editor), explicitly disclaiming support for the latter

- **Evidence**: The page includes a stated disclaimer on community editors.
  The Compiler Playground links to `https://github.github.com/gh-aw/editor/`
  and is presented without disclaimer; the two community tools carry an
  explicit unsupported notice.
- **Confidence**: settled (first-party documentation of the official/community
  distinction)
- **Quote**: "Community editors are created and maintained by independent
  contributors. They are not officially supported by the gh-aw project."
- **Our assessment**: This disclaimer matters for practitioners: features,
  compatibility, and data reported by community tools are not gh-aw platform
  guarantees. The anti-patterns section of the Agentic Prompt Generator
  (Claims 5–10) should be read as practitioner empirical analysis, not as
  official platform guidance. For Ch02 (Harness Engineering): when documenting
  tooling choices, mark community tools with an "unsupported" caveat distinct
  from official gh-aw tooling.

### Claim 2: The Compiler Playground is an experimental browser-based tool that runs the gh-aw compiler in-browser via WebAssembly, enabling workflow authoring and live compilation without local CLI setup

- **Evidence**: The reference page and the Playground's own page confirm the
  WASM-based browser compilation. The Playground shows side-by-side editing:
  a "Workflow (.md)" input pane and a "Compiled Output (.lock.yml)" output
  pane. Loading text on the Playground page confirms the ~5 MB WASM module is
  downloaded on first load.
- **Confidence**: emerging (first-party; labeled "experimental")
- **Quote**: "runs the gh-aw compiler entirely in the browser using WebAssembly"
- **Our assessment**: The Compiler Playground is the consumer-facing application
  of the Wasm compilation capability documented technically in
  `docs-ghaw-wasm-compilation.md`. That note documents the build process and
  JavaScript API; this source adds that there is an actual live tool using it.
  For Ch02 (Harness Engineering): the Playground is a zero-install entry point
  for exploring gh-aw workflow syntax — no `gh` CLI, no local Go, no GitHub
  account required. It functions as both a learning resource and a quick
  prototyping tool.

### Claim 3: The Compiler Playground ships with five built-in sample workflows — Hello World, Issue Triage, CI Doctor, Contribution Guidelines Checker, and Daily Repo Status — accessible from a navigation menu

- **Evidence**: The Playground page's navigation menu lists these five sample
  workflows by name. These provide immediate interactive examples without
  requiring users to write their own workflow markdown first.
- **Confidence**: settled (menu items are directly visible on the Playground
  page)
- **Quote**: (no direct quote; from Playground page menu items: "Hello World,
  Issue Triage, CI Doctor, Contribution Guidelines Checker, Daily Repo Status")
- **Our assessment**: The five sample names map directly to the "Continuous AI"
  workflow taxonomy in `docs-ghaw-how-they-work.md` Claim 8 — Issue Triage and
  CI Doctor are operational patterns; Daily Repo Status is a reporting pattern.
  The Playground samples serve as an on-ramp: practitioners can select a
  sample, modify the markdown, and observe compilation output live. For Ch02:
  cite the Playground as an interactive first step before local CLI setup.

### Claim 4: The Agentic Prompt Generator (community) uses a 5-step guided UI — Archetype, Triggers, Outputs, Customize, Preview — to scaffold workflow prompts, offering nine predefined workflow archetypes

- **Evidence**: The tool's page describes the five-step process and lists nine
  archetypes: Issue Triage, Code Improvement, Status Report, Upstream Monitor,
  Dependency Monitor, PR Review, Documentation Updater, Content Moderation,
  and a Custom option. The tool's tagline is "Create GitHub Copilot agentic
  workflow prompts in minutes."
- **Confidence**: settled (directly observed from the tool page; the archetypes
  are named and described)
- **Quote**: "Create GitHub Copilot agentic workflow prompts in minutes"
- **Our assessment**: The nine-archetype taxonomy is a practitioner-derived
  classification of what gh-aw workflows are commonly built for. It is more
  granular than the four-pattern "Continuous AI" taxonomy in `docs-ghaw-how-
  they-work.md` Claim 8 — expanding "automated tasks" into distinct categories
  (issue triage, code improvement, PR review, documentation, dependency
  monitoring, content moderation). For Ch01 (Daily Workflows): this taxonomy
  is useful for helping teams identify which workflows to build first. The five
  trigger options (new issue, pull request, schedule, manual dispatch, slash
  command, push) and the output permissions step (commenting, labeling, creating
  issues, opening PRs, committing) also give a practical vocabulary for the
  authoring UX.

### Claim 5: Based on analysis of 679 workflows, the `slash_command` trigger has near-zero success rate across all configurations and should be replaced with `issues + workflow_dispatch` for user-initiated workflows

- **Evidence**: The Agentic Prompt Generator's anti-patterns section states a
  near-zero success rate with n=204 workflows using the slash_command trigger.
  The recommendation is to use `issues + workflow_dispatch` instead. See
  contradiction issue against `docs-ghaw-chatops.md` Claim 1 (filed separately
  per MINER.md §4a).
- **Confidence**: anecdotal (community tool's empirical analysis; dataset not
  independently verified; sample may be biased toward poorly-configured community
  workflows)
- **Quote**: "The `slash_command` trigger has a near-zero success rate across
  all combos (n=204)."
- **Our assessment**: This is the most striking finding in the source. The
  official ChatOps documentation (`docs-ghaw-chatops.md`) presents `slash_command`
  as a recommended, first-class trigger for HITL interactions. This community
  empirical analysis says the opposite: near-zero success rate. The tension
  between documented feature and empirical outcome could reflect: (a) the trigger
  works when configured correctly but is often misconfigured; (b) the sample is
  biased toward unsophisticated community workflows; or (c) a genuine platform
  reliability issue. The guide should surface both sides without picking a winner
  until the contradiction is resolved. **See contradiction issue (filed separately).**

### Claim 6: `workflow_run` as the sole trigger has a 13% success rate (n=76); the recommended fix is `schedule + workflow_dispatch` combined with preliminary data-gathering steps

- **Evidence**: From the anti-patterns section: explicit success rate (13%) and
  sample size (n=76) with a concrete alternative trigger combination.
- **Confidence**: anecdotal (same community dataset as Claim 5)
- **Quote**: "Using `workflow_run` as the sole trigger results in 13% success
  (n=76)."
- **Our assessment**: `workflow_run` as a trigger means "run this workflow after
  another workflow completes." The low success rate may reflect the challenge of
  correctly chaining workflows — context, outputs, and state from the upstream
  workflow must be passed correctly. The recommended fix (`schedule +
  workflow_dispatch`) side-steps the chaining problem by decoupling execution
  from upstream events. For Ch02: document `workflow_run` chaining as a
  high-risk pattern requiring careful validation; prefer explicit scheduling or
  manual dispatch for workflows that aggregate data from other workflows.

### Claim 7: The Codex model has a 47% success rate vs. 67% for the default model in gh-aw workflows; for complex tasks, Claude Opus is recommended over Codex

- **Evidence**: From the anti-patterns section: specific success rates by model
  with a named recommendation for complex tasks.
- **Confidence**: anecdotal (community dataset; "success" definition not specified;
  may reflect workflow type distribution rather than pure model capability)
- **Quote**: "The `codex` model has a 47% success rate vs 67% for the default
  model."
- **Our assessment**: The 20-point gap between Codex (47%) and the default
  model (67%) is large enough to suggest a meaningful difference. However, the
  "success" metric is undefined — it may aggregate across workflow types where
  Codex is more or less appropriate. The recommendation to use Claude Opus for
  complex tasks aligns with the multi-engine support documented in
  `docs-ghaw-how-they-work.md` Claim 9 and the `engine:` frontmatter field in
  `docs-ghaw-setup-creating-workflows.md` Claim 5. For Ch02: add model selection
  guidance — the default engine outperforms Codex across a broad workflow sample;
  Codex should only be chosen when there's a specific reason.

### Claim 8: Workflows without `workflow_dispatch` as an additional trigger have a 21 percentage point lower success rate (n=3,476 vs. n=1,412), making `workflow_dispatch` a recommended standard inclusion

- **Evidence**: Explicit percentage point difference with sample sizes from the
  anti-patterns section.
- **Confidence**: anecdotal (community dataset; largest sample in the anti-patterns
  section: n=4,888 total)
- **Quote**: "Workflows without `workflow_dispatch` have 21 percentage points
  lower success (n=3,476 vs n=1,412)."
- **Our assessment**: The mechanism behind this correlation is likely that
  `workflow_dispatch` enables manual re-runs for debugging and recovery, and
  that workflows designed with manual dispatch support are generally better
  engineered. The causality is unclear — including `workflow_dispatch` may not
  directly cause higher success, but workflows that include it tend to be better
  configured overall. For Ch02: recommend `workflow_dispatch` as a standard
  addition to all workflows as a debugging escape hatch — even if the primary
  trigger is `schedule` or `push`, manual dispatch is cheap to add and
  significantly reduces the friction of diagnosing failures.

### Claim 9: 32% of all analyzed workflows are unmodified template copies, and these underperform because permissions, context, and timeout settings are not adapted to the specific repository

- **Evidence**: Percentage from the anti-patterns section.
- **Confidence**: anecdotal (community dataset)
- **Quote**: "32% of all workflows are unmodified template copies."
- **Our assessment**: Template non-adaptation is the most avoidable anti-pattern.
  The five-step guided UI of the Agentic Prompt Generator is specifically
  designed to surface configuration decisions (permissions in the Outputs step,
  context in the Customize step) that template-cloners skip. This reinforces
  the guidance implicit in `docs-ghaw-setup-creating-workflows.md` Claim 2 — the
  example prompts and the `create.md` URL-addressable prompt are starting points
  requiring repository-specific adaptation, not copy-paste solutions. For Ch02:
  add an explicit caution against unmodified template use; the guide should
  emphasize that at minimum, permissions and context configuration must be
  reviewed for the specific repository.

### Claim 10: Optimal workflow prompt size is 3–8 KB; prompts exceeding 30 KB on the default model risk context limits and degraded performance

- **Evidence**: Specific size ranges from the anti-patterns section.
- **Confidence**: anecdotal (community dataset; size thresholds may vary by
  model and task type)
- **Quote**: "Prompts exceeding 30KB on the default model risk context limits
  and degraded performance."
- **Our assessment**: The 3–8 KB guidance is the most actionable sizing
  recommendation in our corpus for gh-aw workflow prompt sections. The 30 KB
  ceiling aligns with general context window stewardship principles. The
  recommendation to upgrade to a larger model or split the workflow at 30 KB
  is consistent with multi-agent decomposition patterns in other sources (e.g.,
  `blog-anthropic-multi-agent-coordination-patterns.md`). For Ch02: add prompt
  sizing as a workflow engineering consideration — keep instruction sections
  concise (3–8 KB target), split oversized workflows, upgrade the engine for
  genuinely complex single-workflow tasks.

### Claim 11: The Graphical Workflow Editor (community) provides a visual, interactive editing experience for agentic workflows as an alternative to direct markdown/YAML editing

- **Evidence**: Reference page description and editor page title ("Agentic
  Workflow Builder"). Minimal content was available from the editor page itself.
- **Confidence**: anecdotal (community tool; limited content extractable from
  page; no feature list, no usage documentation visible)
- **Quote**: "focuses on a more interactive and visual editing experience"
- **Our assessment**: The Graphical Workflow Editor represents the visual
  editing vector of the community ecosystem — complementing the Agentic Prompt
  Generator's guided text-based approach. Little content is available to
  evaluate its capabilities. For Ch02: acknowledge as a community alternative
  for teams that prefer visual workflow authoring, with the caveat that it is
  unsupported by the gh-aw project.

## Concrete Artifacts

### Editor Ecosystem Overview

```
GitHub Agentic Workflows — Editor Ecosystem
────────────────────────────────────────────────────────────────────────
Tool                         Type       URL
────────────────────────────────────────────────────────────────────────
Compiler Playground          official   https://github.github.com/gh-aw/editor/
Agentic Prompt Generator     community  https://ashleywolf.github.io/agentic-prompt-generator/
Graphical Workflow Editor    community  https://mossaka.github.io/gh-aw-editor-visualizer/
────────────────────────────────────────────────────────────────────────
Note: Community editors "are not officially supported by the gh-aw project."
```

*Source: `reference/editors` page — Editor listing and community disclaimer*

### Compiler Playground — Built-In Sample Workflows

```
Compiler Playground (https://github.github.com/gh-aw/editor/)
Navigation menu samples:
  1. Hello World
  2. Issue Triage
  3. CI Doctor
  4. Contribution Guidelines Checker
  5. Daily Repo Status

Interface: side-by-side panes
  Left:  Workflow (.md)          — editable workflow markdown source
  Right: Compiled Output (.lock.yml) — live compilation result

WASM module: ~5 MB (compressed) loaded in browser
```

*Source: Compiler Playground page — menu items and UI description*

### Agentic Prompt Generator — 5-Step Workflow and Archetype Taxonomy

```
GitHub Agentic Workflow Generator
Tagline: "Create GitHub Copilot agentic workflow prompts in minutes"
URL: https://ashleywolf.github.io/agentic-prompt-generator/

5-Step guided creation process:
  Step 1: Archetype  — choose a predefined workflow pattern
  Step 2: Triggers   — choose what events activate the workflow
  Step 3: Outputs    — choose what the workflow is permitted to write
  Step 4: Customize  — add repository-specific context
  Step 5: Preview    — review and copy the generated prompt

Archetypes (9 options):
  Issue Triage            — classify and label new issues
  Code Improvement        — daily code quality improvements
  Status Report           — periodic status/activity reports
  Upstream Monitor        — track upstream dependencies and sync changes
  Dependency Monitor      — track and update project dependencies
  PR Review               — review PRs for quality and issues
  Documentation Updater   — keep docs accurate and up-to-date
  Content Moderation      — check PRs/issues for spam or policy violations
  Custom                  — describe your own workflow from scratch

Trigger options:
  New issue opened
  Pull request opened
  On a schedule (daily/weekly)
  Manual dispatch
  Slash command (/command in comments)
  Push to branch

Output permissions:
  Commenting on issues/PRs
  Applying labels
  Creating issues
  Opening pull requests
  Committing changes
```

*Source: Agentic Prompt Generator page — observed UI and feature descriptions*

### Anti-Patterns from 679 Workflows (Agentic Prompt Generator)

```
ANTI-PATTERNS — from analysis of 679 gh-aw workflows
(Source: Agentic Prompt Generator, Anti-Patterns section; community data)

Trigger reliability (empirical success rates):
  slash_command trigger:       near-zero success rate (n=204)
    → Replace with: issues + workflow_dispatch
  workflow_run (sole trigger): 13% success (n=76)
    → Replace with: schedule + workflow_dispatch + preliminary data-gathering

Model selection:
  codex model:                 47% success rate
  default model:               67% success rate
  Complex tasks:               use claude-opus-4.5 over codex

Missing workflow_dispatch:
  Workflows WITHOUT dispatch:  21 percentage points lower success (n=3,476)
  Workflows WITH dispatch:     baseline (n=1,412)
  → Add workflow_dispatch to all workflows as debugging escape hatch

Template non-adaptation:
  32% of all workflows are unmodified template copies
  → Always adapt: permissions, context, timeout for your specific repository

Prompt sizing:
  Optimal range:   3–8 KB
  Risk threshold:  > 30 KB (context limits, degraded performance on default model)
  > 30 KB options: upgrade model (claude-opus-4.5) or split into multiple workflows
```

*Source: Agentic Prompt Generator page — Anti-Patterns section; community analysis*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-wasm-compilation.md` Claim 1 (gh-aw compiler packaged as WebAssembly
    for browser-based compilation): the Compiler Playground is the live consumer
    application of that capability. The wasm-compilation note covers the technical
    build; this source adds the user-facing interactive tool.
  - `docs-ghaw-how-they-work.md` Claim 8 ("Continuous AI" workflow taxonomy): the
    nine Agentic Prompt Generator archetypes provide a more granular practitioner
    taxonomy that corroborates and extends the four-pattern "Continuous AI" framing.
    "Issue Triage," "CI Doctor," and "Daily Repo Status" in the Playground samples
    also align with this taxonomy.
  - `docs-ghaw-setup-creating-workflows.md` Claim 2 (four verbatim starter workflow
    prompts for issue triage, daily activity report, documentation updater, AGENTS.md
    maintainer): the Agentic Prompt Generator's archetypes overlap significantly —
    Issue Triage, Documentation Updater, and Status Report archetypes correspond to
    three of the four starter prompts, confirming these as high-value starting points.
  - `docs-ghaw-how-they-work.md` Claim 9 (multi-engine support via `engine:`
    frontmatter): the Agentic Prompt Generator's model selection anti-patterns
    (Claim 7 here) corroborate that engine selection meaningfully affects outcomes.
  - `docs-ghaw-setup-creating-workflows.md` Claim 5 (`engine:` frontmatter for
    non-Copilot models): the recommendation to prefer the default model over Codex
    corroborates the importance of the `engine:` field documented there.

- **Contradicts**:
  - `docs-ghaw-chatops.md` Claim 1 (the `slash_command` trigger is a documented,
    first-class trigger for human-initiated HITL interactions, recommended for
    ChatOps use cases): Claim 5 in this source presents empirical data showing
    near-zero success rate for the slash_command trigger (n=204). The official docs
    recommend it; the community empirical data says avoid it. **See contradiction
    issue filed separately per MINER.md §4a.**

- **Extends**:
  - `docs-ghaw-agentic-authoring.md` Claim 4 (GitHub Web Interface as a non-interactive
    browser-based creation path): this source adds two community browser-based editing
    tools (Agentic Prompt Generator and Graphical Workflow Editor) as alternatives that
    run outside the official GitHub web interface.
  - `docs-ghaw-wasm-compilation.md` (technical Wasm build reference): this note adds
    the user-facing dimension — the Compiler Playground is what the Wasm build produces
    for practitioners, not just a build target.
  - `docs-ghaw-setup-creating-workflows.md` Claim 2 and 6 (starter workflow prompts
    and web interface trade-off): the Agentic Prompt Generator archetypes and the
    anti-patterns data extend the workflow creation guidance with empirical data on
    what actually works in the wild.

- **Novel**:
  - **Community editor ecosystem** (Claim 1): No existing source note documents the
    community tooling layer for gh-aw — the fact that independent contributors have
    built a guided prompt generator and a graphical editor is new to the corpus.
  - **Statistical anti-patterns from 679 workflows** (Claims 5–10): This is the first
    empirical data in the corpus on gh-aw workflow success rates by trigger type,
    model, and prompt size. No other source provides quantitative failure analysis
    at this scale.
  - **slash_command near-zero success rate** (Claim 5): First empirical evidence
    challenging the official recommendation to use `slash_command` for HITL
    interactions. Directly contradicts `docs-ghaw-chatops.md`.
  - **Workflow prompt sizing guidance** (Claim 10): The 3–8 KB optimal range and
    30 KB ceiling are the first concrete sizing recommendations for workflow
    instruction sections in the corpus.
  - **workflow_dispatch as a success factor** (Claim 8): The 21-percentage-point
    improvement from adding `workflow_dispatch` as an additional trigger is a
    specific, actionable finding with no parallel in existing notes.
  - **Template non-adaptation prevalence** (Claim 9): The 32% rate of unmodified
    template copies provides quantitative context for how often practitioners skip
    repository-specific adaptation.
  - **Compiler Playground sample workflow catalog** (Claim 3): The five named
    sample workflows (Hello World, Issue Triage, CI Doctor, Contribution Guidelines
    Checker, Daily Repo Status) are not enumerated in any existing note.

## Guide Impact

### Chapter 01: Daily Workflows

- **Add Compiler Playground as a zero-install exploration tool** (Claim 2 and 3):
  Before committing to CLI setup, practitioners can explore gh-aw workflow syntax
  interactively at `https://github.github.com/gh-aw/editor/`. The five sample
  workflows (Hello World, Issue Triage, CI Doctor, Contribution Guidelines Checker,
  Daily Repo Status) provide starting points. Cite alongside the web interface path
  from `docs-ghaw-agentic-authoring.md` Claim 4.
- **Add workflow archetype taxonomy** (Claim 4): The nine archetypes from the Agentic
  Prompt Generator complement the four "Continuous AI" patterns from
  `docs-ghaw-how-they-work.md` Claim 8 as a more granular vocabulary for team planning
  conversations about what to automate first.

### Chapter 02: Harness Engineering

- **Add anti-pattern guidance with empirical backing** (Claims 5–10): This is the
  most specific, evidence-backed authoring guidance in the corpus. Recommend adding
  a "common workflow anti-patterns" section citing this source:
  - Avoid `slash_command` as a trigger (near-zero success, n=204) — but note
    the contradiction with `docs-ghaw-chatops.md` and await resolution.
  - Avoid `workflow_run` as the sole trigger (13% success, n=76); prefer
    `schedule + workflow_dispatch`.
  - Always add `workflow_dispatch` (+21 pp success, n=4,888 total).
  - Always adapt templates — 32% of unmodified copies underperform.
  - Keep prompts in the 3–8 KB range; treat 30 KB as a hard ceiling.
- **Add model selection guidance** (Claim 7): The default model (67%) outperforms
  Codex (47%) across a broad workflow sample; use Codex only when justified. Update
  the `engine:` frontmatter guidance in `docs-ghaw-setup-creating-workflows.md`
  Claim 5 to add this empirical context.
- **Mark community tools as unsupported** (Claim 1): When documenting the editor
  ecosystem, clearly distinguish the official Compiler Playground from community
  tools. The Agentic Prompt Generator and Graphical Workflow Editor are useful but
  carry no platform support guarantee.
- **Note Compiler Playground limitations for multi-file workflows** (Claim 2):
  The Compiler Playground uses the Wasm compiler, which cannot compile workflows
  with `imports:` (per `docs-ghaw-wasm-compilation.md` Claim 8). Teams with
  multi-file workflows should use the native CLI rather than the Playground.

## Extraction Notes

1. **Reference page content was thin; followed linked pages per MINER.md §1**:
   The `reference/editors` page itself describes the three tools in brief (a
   paragraph each with a disclaimer on community tools). Per MINER.md §1, the
   Miner followed up to five linked pages. The Compiler Playground and the
   Agentic Prompt Generator yielded substantive content. The Graphical Workflow
   Editor page had minimal content (just the title "Agentic Workflow Builder")
   and yielded Claim 11 only.

2. **Anti-patterns data confidence qualification**: The Agentic Prompt Generator's
   anti-patterns section is community-generated empirical analysis. The dataset
   of 679 workflows is not independently verified — its composition (which
   repositories, which time range, what "success" means) is not disclosed. Claims
   5–10 are therefore marked `anecdotal` confidence. The directional signals (near-
   zero vs. 67% vs. 13%) are strong enough to note, but practitioners should not
   treat these as platform-guaranteed benchmarks.

3. **Contradiction filed for slash_command**: The near-zero success rate for
   `slash_command` (n=204) from the Agentic Prompt Generator directly contradicts
   the official `docs-ghaw-chatops.md` recommendation of `slash_command` as the
   primary HITL trigger. A contradiction issue was filed before opening this PR
   per MINER.md §4a. The guide should present both sides until the contradiction
   is resolved.

4. **WebFetch processes content through an AI model**: Quotes marked as verbatim
   were cross-checked across multiple fetch passes. The anti-patterns statistics
   (n=204, n=76, 47%, 67%, 21 pp, 32%, 30 KB) were consistent across both fetch
   passes of the Agentic Prompt Generator page and are treated as verbatim.

5. **No publication date on any of the three tools**: None of the three editor
   pages carry explicit publication dates. `date_published` is left null.

6. **Graphical Workflow Editor content was minimal**: Only the title "Agentic
   Workflow Builder" was extractable from the page. The reference page description
   ("focuses on a more interactive and visual editing experience") provided the
   main claim about its positioning.
