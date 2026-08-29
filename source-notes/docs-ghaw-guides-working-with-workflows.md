---
source_url: https://github.github.com/gh-aw/guides/working-with-workflows
source_type: docs
title: "GitHub Agentic Workflows: Working with Workflows (Guides)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: emerging
issue: "#3006"
---

# GitHub Agentic Workflows: Working with Workflows (Guides)

> The umbrella practitioner guide that bundles the entire gh-aw workflow
> lifecycle — configure → create (five distinct methods) → add existing →
> edit → debug → upgrade — into one page with links out to the detailed
> task-specific guides; it also surfaces several small but concrete details
> (a renamed CLI flag, a new upgrade flag, a widened diff path) that are
> either absent from or inconsistent with existing corpus notes on the same
> commands.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `guides/working-with-workflows`
  page — the "Guides" section's top-level index/overview page for the workflow
  lifecycle. Structurally this page is a hub: each section is 1-4 sentences plus
  a command block, with an explicit "Learn More" list of links to the detailed
  pages that already exist as separate source notes.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind all other `docs-ghaw-*` notes in the corpus. CLI commands and
  flags are authoritative for the `gh aw` platform as of the extraction date.
- **Scope**: A single condensed walkthrough of the full workflow lifecycle:
  repository initialization, five creation methods (web interface, coding agent,
  wizard, remixing, dictation), adding existing workflows, editing, debugging,
  and upgrading. Each section is intentionally thin and defers to a linked
  detailed guide for depth. Does NOT itself provide the depth already captured in
  `docs-ghaw-setup-creating-workflows.md`, `docs-ghaw-guides-editing-workflows.md`,
  `docs-ghaw-guides-upgrading.md`, `docs-ghaw-guides-reusing-workflows.md`,
  `docs-ghaw-agentic-authoring.md`, or `docs-ghaw-wizard.md` — extraction here
  focused on what is either new or inconsistent relative to those six notes.

## Extracted Claims

### Claim 1: This page is a single-page lifecycle index that bundles configure → create → add → edit → debug → upgrade, with an explicit "Learn More" list pointing to five separate detailed guides

- **Evidence**: The page's structure runs, in order: "Configuring Your Repository
  for Agentic Authoring" → four "Creating Workflows..." sections plus a fifth
  "Creating Workflows by Dictation" section → "Adding Existing Workflows" →
  "Editing Workflows" → "Debugging Workflows" → "Upgrading Workflows" → a closing
  "Learn More" section listing: Create a New Workflow, Workflow Structure, CLI
  Commands, Imports, Debugging Workflows.
- **Confidence**: settled (directly observed page structure, two independent
  WebFetch passes agree on section order and the "Learn More" list)
- **Quote**: "This guide covers creating, editing, debugging, and maintaining
  GitHub Agentic Workflows using coding agents, the web interface, CLI tools,
  and various creation methods."
- **Our assessment**: No other source note in the corpus documents the full
  lifecycle as a single continuous practitioner journey — the existing notes
  (`docs-ghaw-setup-creating-workflows.md`, `docs-ghaw-guides-editing-workflows.md`,
  `docs-ghaw-guides-upgrading.md`, `docs-ghaw-guides-reusing-workflows.md`) each
  cover one phase in depth but were extracted independently, months apart, with no
  single source tying them together in sequence. This page is that connective
  tissue: it is the page a new practitioner would land on first, and its "Learn
  More" links are effectively a map of which detailed guide corresponds to which
  lifecycle stage. For Ch02 (Harness Engineering): use this page's section order
  as the recommended structure for a "workflow lifecycle" section that currently
  has no single entry point stitching the phase-specific notes together.

### Claim 2: Five distinct, named workflow creation methods are presented as parallel options — GitHub Web Interface, coding agent/VS Code, the Creation Wizard, Remixing an existing workflow, and Dictation — rather than a single recommended path

- **Evidence**: Four consecutive `##`-level headings name each method: "Creating
  Workflows using the GitHub Web Interface," "Creating Workflows Using a Coding
  Agent," "Creating Workflows with the Creation Wizard," "Creating Workflows by
  Remixing," and "Creating Workflows by Dictation."
- **Confidence**: settled (headings are directly observed, verbatim)
- **Quote**: "This guide covers creating, editing, debugging, and maintaining
  GitHub Agentic Workflows using coding agents, the web interface, CLI tools,
  and various creation methods."
- **Our assessment**: Prior notes documented some of these methods individually
  (web interface and coding agent creation in `docs-ghaw-setup-creating-workflows.md`;
  the wizard in `docs-ghaw-wizard.md`) but no source established that the platform
  frames these as five co-equal, named entry points rather than a single
  recommended flow with fallbacks. Dictation, in particular, was previously
  documented only as an "auxiliary pattern" and "the thinnest and most specialized
  finding" in `docs-ghaw-agentic-authoring.md` (Claim 9) — here it is elevated to
  a first-class, equally-weighted heading alongside the other four. For Ch02: the
  five-method framing is worth using verbatim as the decision menu for "how do I
  create a workflow," rather than presenting the web interface or coding-agent
  path as the sole default.

### Claim 3: Remixing an existing workflow reuses the same `create.md` prompt used for fresh creation, with an added "use this existing workflow as the starting point" instruction — not a separately named tool

- **Evidence**: The "Creating Workflows by Remixing" section's prompt template is:
  "Create a workflow for GitHub Agentic Workflows using
  https://raw.githubusercontent.com/github/gh-aw/main/create.md. Use this existing
  workflow as the starting point: https://github.com/OWNER/REPO/blob/main/workflows/WORKFLOW.md.
  Preserve its purpose, but adapt its labels, assignees, branch names, permissions,
  triggers, tools, and outputs to this repository." The section closes with: "For
  unchanged or centrally managed workflows, use `gh aw add` instead."
- **Confidence**: emerging (verbatim prompt template from first-party docs; the
  relationship to the previously-documented `create-agentic-agent` tool name is
  our interpretation, not stated on the page — see Cross-References and
  Extraction Notes)
- **Quote**: "Create a workflow for GitHub Agentic Workflows using
  https://raw.githubusercontent.com/github/gh-aw/main/create.md. Use this existing
  workflow as the starting point: https://github.com/OWNER/REPO/blob/main/workflows/WORKFLOW.md."
- **Our assessment**: `docs-ghaw-agentic-authoring.md` Claim 3 (extracted 2026-04-21)
  names a distinct tool, `create-agentic-agent`, for this same one-time-fork-with-
  adaptation use case: "AI-assisted migration. The agent analyzes the source
  workflow, identifies dependencies, adapts configuration for your repository, and
  validates the result." This page (extracted 2026-08-29, ~4 months later) describes
  the identical use case — fork-and-adapt an existing workflow, contrasted with
  `gh aw add` for tracked reuse — but does so entirely through the generic
  `create.md` prompt plus an inline instruction, with no mention of a
  `create-agentic-agent` command or tool name anywhere on the page. This is either
  (a) a renaming/consolidation of the mechanism (the fork-and-adapt capability was
  folded into the general `create.md` prompt rather than kept as a separately named
  tool), or (b) two different documentation pages describing the same underlying
  mechanism with different levels of tooling specificity. We cannot determine which
  from the page content alone. For Ch02: if the guide currently names
  `create-agentic-agent` as the fork/migration tool (per the prior note's Guide
  Impact section), verify against current platform behavior before publishing —
  this page suggests the current first-party framing has moved to "remix via
  create.md," not a distinctly named command.

### Claim 4: `gh aw add-wizard`'s flag for skipping the API-key/secret prompt is `--no-secret`, not `--skip-secret` as documented three months earlier

- **Evidence**: Two independent WebFetch passes of this page both returned
  `--no-secret` verbatim in the "Adding Existing Workflows" section's example:
  "Skip API key prompts when the secret is already configured: `gh aw add-wizard
  githubnext/agentics/daily-repo-status --no-secret`."
- **Confidence**: emerging (verbatim from two independent passes of the live page,
  but the platform explicitly caveats that "recommended patterns, commands, and
  configuration options may change," per `docs-ghaw-guides-reusing-workflows.md`
  Extraction Notes §2)
- **Quote**: "Skip API key prompts when the secret is already configured:"
  (followed by the code block `gh aw add-wizard githubnext/agentics/daily-repo-status --no-secret`)
- **Our assessment**: `docs-ghaw-guides-reusing-workflows.md` Claim 1 (extracted
  2026-05-25) documents the identical use case with the flag written as
  `--skip-secret`: "`gh aw add-wizard githubnext/agentics/daily-repo-status --skip-secret`."
  The two notes describe the same command for the same purpose with a different
  flag spelling, three months apart. This reads as CLI flag drift over time rather
  than a substantive disagreement — both sources agree the flag exists and does
  the same thing — but it is guide-actionable: any guide text that currently
  recommends `--skip-secret` verbatim would give practitioners a wrong flag today.
  Not filed as a formal contradiction (both sources agree on behavior, not
  outcome — this is a versioning/drift issue, not an opposing claim per MINER.md
  §4a's filing criteria), but flagged here so the Smith updates the flag spelling
  if it appears in the guide.

### Claim 5: `gh aw upgrade` documents a `--pre-releases` flag for opting into pre-release versions, not previously documented in the corpus's dedicated upgrading-guide note

- **Evidence**: The "Upgrading Workflows" section lists three flags in prose:
  "Use `--pre-releases` for pre-release versions, `--no-fix` to skip fixes and
  compilation, or `--dir` for custom workflow directories."
- **Confidence**: emerging (verbatim flag name from two independent WebFetch
  passes; flag behavior beyond the one-line description is not elaborated on this
  page)
- **Quote**: "Use `--pre-releases` for pre-release versions, `--no-fix` to skip
  fixes and compilation, or `--dir` for custom workflow directories."
- **Our assessment**: `docs-ghaw-guides-upgrading.md` (extracted 2026-05-12) documents
  `--no-fix` and `--dir`-equivalent (`--dir custom/workflows`) but has no `--pre-releases`
  flag in its "Command Options Reference" concrete artifact. Given the corpus already
  has extensive coverage of pre-release version churn (e.g.
  `blog-ghaw-weekly-2026-08-24.md` discusses v0.87.x pre-releases), a flag for
  explicitly opting into pre-release upgrades is a plausible and non-conflicting
  addition to the command surface, not a replacement of anything in the existing
  note. For Ch02: add `--pre-releases` to the upgrade command options reference
  alongside the previously documented `--no-fix` and `--dir`.

### Claim 6: The post-upgrade diff-review command now scopes to two directories, `.github/workflows/` and `.github/skills/`, rather than only `.github/workflows/`

- **Evidence**: The "Upgrading Workflows" section's review step is: "Review changes
  before committing: `git diff -- .github/workflows/ .github/skills/`."
- **Confidence**: emerging (verbatim command from two independent WebFetch passes)
- **Quote**: "Review changes before committing:" (followed by the code block
  `git diff -- .github/workflows/ .github/skills/`)
- **Our assessment**: `docs-ghaw-guides-upgrading.md` Claim 3's "Full Upgrade
  Procedure" concrete artifact shows only `git diff .github/workflows/` as Step 4.
  This page's inclusion of `.github/skills/` alongside workflows implies that
  `gh aw upgrade`'s codemods (or the underlying agentic-authoring file set) now
  also touch a `.github/skills/` directory not mentioned in the earlier note —
  consistent with `docs-ghaw-guides-serena.md` and other skills-related notes in
  the corpus documenting a `.github/skills/` convention that may have been
  introduced or formalized after the May extraction. For Ch02: widen the
  post-upgrade review checklist to include `.github/skills/`, not just
  `.github/workflows/`.

### Claim 7: The trust-review callout for adding external workflows enumerates seven specific things to review before adding — triggers, permissions, tools, network access, safe outputs, instructions, and lock files

- **Evidence**: The "Adding Existing Workflows" section's bolded callout reads, in
  full: "**Important:** Only add workflows from trusted sources. Review triggers,
  permissions, tools, network access, safe outputs, instructions, and lock files
  beforehand."
- **Confidence**: settled (verbatim callout, confirmed identically across two
  independent WebFetch passes)
- **Quote**: "Only add workflows from trusted sources. Review triggers,
  permissions, tools, network access, safe outputs, instructions, and lock files
  beforehand."
- **Our assessment**: `docs-ghaw-guides-reusing-workflows.md` Claim 5 documents a
  similar but less itemized callout: "Check carefully that the workflow comes from
  a trusted source and is appropriate for your use in your repository. Review the
  workflow's content and understand what it does before adding it to your
  repository." This page's version is the more actionable checklist form — it
  names the exact seven review targets rather than the generic "review the
  content" framing. The two are consistent (not contradictory), and this page
  gives the more citable, itemizable version. For Ch03 (Safety and Verification):
  use this page's seven-item list as the concrete pre-import review checklist,
  citing it as the more specific companion to Claim 5 in
  `docs-ghaw-guides-reusing-workflows.md`.

### Claim 8: The debug.md-driven debugging flow is described as ending in a "validates the workflow" step, distinct from the "opens a pull request" ending documented in the prior authoring-lifecycle note

- **Evidence**: The "Debugging Workflows" section states: "The agent installs the
  CLI, inspects logs, identifies causes, applies fixes, and validates the
  workflow." No mention of opening a pull request appears in this section.
- **Confidence**: emerging (verbatim sentence from two independent WebFetch passes;
  the omission of a PR-opening step relative to the prior note is an observation,
  not a confirmed behavior change)
- **Quote**: "The agent installs the CLI, inspects logs, identifies causes, applies
  fixes, and validates the workflow."
- **Our assessment**: `docs-ghaw-agentic-authoring.md` Claim 6 describes the same
  `debug.md` flow ending differently: "The agent fetches it and follows the
  instructions to install the `gh aw` CLI, analyze logs, apply fixes, and open a
  pull request with the changes." This page's ending step is "validates the
  workflow" instead of "open a pull request." This could be (a) a condensed
  description that omits the PR step without denying it happens, or (b) a genuine
  behavior refinement where validation was added as an explicit step. Given the
  brevity of this hub page relative to the dedicated authoring guide, we read this
  as most likely condensation rather than a behavior change, but it is worth noting
  since "validates the workflow" (e.g., a dry-run or compile check) and "opens a
  pull request" (a human-review checkpoint) have different safety implications if
  one is silently dropped. For Ch03: when documenting the debug flow, retain both
  the validation step and the PR-opening step from the more detailed prior note
  unless a dedicated debugging-page re-extraction confirms the PR step was removed.

### Claim 9: Dictation-assisted workflow creation is anchored to a specific, stable URL (`DICTATION.md`) applied before or after dictating, not just a conceptual "dictation instructions" feature

- **Evidence**: The "Creating Workflows by Dictation" section states: "When using
  speech-to-text for workflow creation, apply the dictation instructions from
  https://raw.githubusercontent.com/github/gh-aw/main/DICTATION.md to correct
  terminology and formatting before or after dictating."
- **Confidence**: settled (verbatim URL and sentence, confirmed across two
  independent WebFetch passes)
- **Quote**: "apply the dictation instructions from
  https://raw.githubusercontent.com/github/gh-aw/main/DICTATION.md to correct
  terminology and formatting before or after dictating"
- **Our assessment**: `docs-ghaw-agentic-authoring.md` Claim 9 describes the
  dictation feature's behavior (terminology correction, filler-word removal,
  casual-to-imperative transformation) but does not give a URL — that note states
  the prompt is loaded via a "Copy dictation instructions" button not accessible
  via static fetch. This page supplies the missing URL and confirms the pattern is
  the same URL-addressable self-contained prompt design documented for
  `install.md`, `create.md`, and `debug.md` in `docs-ghaw-agentic-authoring.md`
  Claims 6-7 — `DICTATION.md` is a fourth member of that family, not a
  UI-only feature. For Ch02: add `DICTATION.md` to the URL-addressable prompt
  inventory alongside `install.md`, `create.md`, and `debug.md`.

## Concrete Artifacts

### Full Page Structure (section order, verbatim headings)

```
## Overview
## Configuring Your Repository for Agentic Authoring
## Creating Workflows using the GitHub Web Interface
## Creating Workflows Using a Coding Agent
## Creating Workflows with the Creation Wizard
## Creating Workflows by Remixing
## Creating Workflows by Dictation
## Adding Existing Workflows
## Editing Workflows
## Debugging Workflows
## Upgrading Workflows
## Learn More
  - Create a New Workflow
  - Workflow Structure
  - CLI Commands
  - Imports
  - Debugging Workflows
```

*Source: `guides/working-with-workflows` — full page, section headings in order*

### Remixing Prompt Template (verbatim)

```
Create a workflow for GitHub Agentic Workflows using
https://raw.githubusercontent.com/github/gh-aw/main/create.md. Use this
existing workflow as the starting point:
https://github.com/OWNER/REPO/blob/main/workflows/WORKFLOW.md. Preserve its
purpose, but adapt its labels, assignees, branch names, permissions,
triggers, tools, and outputs to this repository.
```

*Source: `guides/working-with-workflows` — "Creating Workflows by Remixing" section*

### Adding Existing Workflows — Command Reference (verbatim)

```bash
# Interactive, with guidance:
gh aw add-wizard githubnext/agentics/daily-repo-status

# Full GitHub URL form:
gh aw add-wizard https://github.com/githubnext/agentics/blob/main/workflows/daily-repo-status.md

# Skip the API key/secret prompt when already configured:
gh aw add-wizard githubnext/agentics/daily-repo-status --no-secret

# Non-interactive, with version pinning:
gh aw add githubnext/agentics/ci-doctor
gh aw add githubnext/agentics/ci-doctor@v1.0.0
gh aw add githubnext/agentics/workflows/ci-doctor.md
```

*Source: `guides/working-with-workflows` — "Adding Existing Workflows" section*

### Upgrading Workflows — Command Reference (verbatim)

```bash
gh aw upgrade
# Flags: --pre-releases (pre-release versions), --no-fix (skip fixes/compilation),
#        --dir (custom workflow directories)

# Review changes before committing:
git diff -- .github/workflows/ .github/skills/

# If upgrading reports errors:
gh aw fix --write -v
```

*Source: `guides/working-with-workflows` — "Upgrading Workflows" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-guides-editing-workflows.md` Claims 1-3 (two-part frontmatter/body
    architecture; frontmatter changes require recompilation): this page's
    "Editing Workflows" section restates the same boundary in condensed form —
    "The body loads at runtime, so changes to instructions, templates, context,
    conditions, and examples take effect immediately... Changes within frontmatter
    markers require recompilation, including triggers, permissions, tools, network
    settings, safe outputs, MCP scripts, runtimes, imports, custom jobs, engine
    selection, timeouts, and roles." The field list matches that note's 12-category
    enumeration.
  - `docs-ghaw-guides-reusing-workflows.md` Claim 3 (automatic dependency/resource
    fetching on `gh aw add`): this page's "The command adds workflow Markdown,
    generates its lock file, records the source for updates, and fetches declared
    resources" corroborates the same behavior in more compressed language.
  - `docs-ghaw-guides-reusing-workflows.md` Claim 4 (`private: true` blocks
    installation elsewhere): corroborated verbatim in compressed form — "Workflows
    marked `private: true` cannot be added elsewhere."
  - `docs-ghaw-agentic-authoring.md` Claim 1 (`gh aw init` / `install.md` as
    equivalent bootstrap paths): corroborated identically — "Initialize this
    repository for GitHub Agentic Workflows using
    https://raw.githubusercontent.com/github/gh-aw/main/install.md" alongside
    `gh aw init` as the CLI equivalent.
  - `docs-ghaw-wizard.md` Claim 11 (the wizard generates either a downloadable
    workflow file or a copy-pasteable prompt for coding agents): corroborated by
    "guides selection of triggers, tools, safe outputs, and permissions, then
    generates a prompt for coding agents like Claude Code or GitHub Copilot CLI."

- **Contradicts**: None filed as formal contradiction issues. Two discrepancies
  were identified and are documented above rather than filed, per MINER.md §4a's
  guidance that documentation drift/versioning differences without opposing guide
  advice do not meet the filing threshold:
  - **`--no-secret` (this page) vs. `--skip-secret`** (`docs-ghaw-guides-reusing-workflows.md`
    Claim 1, extracted 2026-05-25): same command, same purpose, different flag
    spelling three months apart. See Claim 4 above and Extraction Notes §2.
  - **Remixing via generic `create.md` prompt (this page) vs. a distinct
    `create-agentic-agent` tool** (`docs-ghaw-agentic-authoring.md` Claim 3,
    extracted 2026-04-21): same use case (fork-and-adapt an existing workflow),
    described with different tooling specificity four months apart. See Claim 3
    above and Extraction Notes §3. Neither discrepancy changes the guide's
    recommended *behavior* (skip the secret prompt; fork-and-adapt an existing
    workflow) — only the exact command surface used to achieve it — which is why
    these are flagged as drift rather than filed as contradictions.

- **Extends**:
  - `docs-ghaw-agentic-authoring.md` Claims 6-7 (URL-addressable self-contained
    prompt pattern: `install.md`, `create.md`, `debug.md`): Claim 9 above extends
    this family with `DICTATION.md` as a fourth confirmed URL-addressable prompt.
  - `docs-ghaw-guides-upgrading.md` Claim 3/5 (codemod migrations; `--no-fix` flag):
    Claim 5 above extends the command options reference with `--pre-releases`.
  - `docs-ghaw-guides-upgrading.md`'s "Full Upgrade Procedure" concrete artifact
    (Step 4, `git diff .github/workflows/`): Claim 6 above extends the reviewed
    path set to include `.github/skills/`.
  - `docs-ghaw-guides-reusing-workflows.md` Claim 5 (general trust-review callout):
    Claim 7 above extends it into a concrete seven-item checklist.

- **Novel**:
  - **The five-method creation menu as a single, co-equal decision point**
    (Claim 2): no prior source presents web interface, coding agent, wizard,
    remixing, and dictation as five parallel named options in one place.
  - **The full lifecycle-as-one-page structure** (Claim 1): no prior source ties
    init → create → add → edit → debug → upgrade into a single continuous
    narrative with a "Learn More" map to the deeper pages.
  - **`--pre-releases` flag** (Claim 5) and **`.github/skills/` in the post-upgrade
    diff scope** (Claim 6): neither appears in any existing source note.
  - **`DICTATION.md` URL** (Claim 9): the concrete URL for the dictation prompt is
    new; prior coverage was UI-only.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add a single "workflow lifecycle" section using this page's structure**
  (Claim 1): configure → create (5 methods) → add existing → edit → debug →
  upgrade, with pointers to the deeper existing notes for each phase.
- **Present the five creation methods as a decision menu, not a single default**
  (Claim 2): web interface (fastest, non-interactive), coding agent (most
  interactive), wizard (empirically-informed archetype selection, per
  `docs-ghaw-wizard.md`), remixing (adapt an existing workflow), dictation
  (voice-first authoring).
- **Verify and correct the `create-agentic-agent` vs. "remix via `create.md`"
  terminology before publishing** (Claim 3): if the guide currently names
  `create-agentic-agent` as a distinct tool (per `docs-ghaw-agentic-authoring.md`
  Claim 3's Guide Impact and `docs-ghaw-sharing-workflows.md`'s references to it),
  cross-check against current platform behavior — this page's most recent framing
  uses the generic `create.md` prompt with an inline "use this as the starting
  point" instruction instead.
- **Correct `--skip-secret` to `--no-secret` if it appears in drafted guide text**
  (Claim 4), and **add `--pre-releases` to the upgrade flag reference** (Claim 5).
- **Widen the post-upgrade review command to include `.github/skills/`** (Claim 6).
- **Add `DICTATION.md` to the URL-addressable prompt inventory** (Claim 9),
  alongside `install.md`, `create.md`, and `debug.md`.

### Chapter 03: Safety and Verification

- **Use the seven-item trust-review checklist verbatim** (Claim 7): triggers,
  permissions, tools, network access, safe outputs, instructions, and lock files —
  as the concrete pre-import review checklist for adopting external workflows.
- **Confirm whether the debug flow still opens a pull request** (Claim 8) before
  asserting a human-review checkpoint exists in the debugging flow; if a future
  re-extraction of the dedicated debugging guide confirms the PR step was dropped,
  that would be a meaningful safety-relevant change worth its own note.

## Extraction Notes

1. **This is a hub/index page, not a deep-dive**: Each section is 1-4 sentences.
   Per the nature of the page, extraction focused on claims that are either novel
   relative to the six existing detailed notes it links to/overlaps with, or that
   disagree with those notes in some verifiable, verbatim way. Content fully and
   identically covered elsewhere (e.g., the wizard's internals, already exhaustively
   covered in `docs-ghaw-wizard.md`) was not re-extracted.

2. **`--no-secret` vs. `--skip-secret` verified across two independent WebFetch
   passes of this same page** (both returned `--no-secret` verbatim); it was not
   cross-checked against the live gh-aw CLI or GitHub source repository itself
   (out of scope for this extraction), so we cannot rule out that one of the two
   source notes (this one or `docs-ghaw-guides-reusing-workflows.md`) reflects a
   stale or in-between platform state. Flagged for the Smith/Assayer's attention
   rather than resolved here.

3. **`create-agentic-agent` vs. "remix via `create.md`" is an interpretation, not
   a stated equivalence**: the page never mentions `create-agentic-agent` by name,
   and we have no way to confirm from this page alone whether that tool still
   exists, was renamed, or was folded into the generic `create.md` prompt pattern.
   This is flagged as a discrepancy requiring verification rather than resolved.

4. **No sub-pages followed**: The "Learn More" section links to five pages
   (Create a New Workflow, Workflow Structure, CLI Commands, Imports, Debugging
   Workflows) that substantially overlap with `docs-ghaw-setup-creating-workflows.md`,
   `docs-ghaw-workflow-structure-reference.md`, and other existing corpus notes.
   Per MINER.md §1's "up to 5 linked pages" guidance and the Prospector's framing
   of this source as primarily valuable for its *umbrella* perspective rather than
   new depth, sub-pages were not separately fetched; this note relies on the hub
   page's own content plus cross-referencing already-extracted detail notes.

5. **No publication date**: The documentation page carries no explicit
   `date_published`. Content is consistent with current gh-aw platform state as of
   2026-08-29.

6. **Two independent WebFetch passes used for verbatim accuracy**: The gh-aw
   documentation is an Astro/Starlight SPA processed through an AI summarization
   model on fetch. A first general-extraction pass and a second pass specifically
   re-requesting verbatim quotes for flags, URLs, and callout text were used;
   all quotes in this note were confirmed identical across both passes.

7. **No contradiction issues filed**: The two discrepancies found (Claims 3 and 4)
   were assessed against MINER.md §4a's filing criteria and judged to be
   version/terminology drift rather than opposing claims that would produce
   different guide advice — both are documented prominently in Cross-References
   and Guide Impact instead, consistent with how prior notes in this corpus
   (e.g., `docs-ghaw-guides-reusing-workflows.md`'s SHA-reference tension,
   `docs-ghaw-guides-upgrading.md`'s `--validate`/`--no-emit` note) have handled
   similar low-stakes command-surface ambiguity without opening a formal issue.
