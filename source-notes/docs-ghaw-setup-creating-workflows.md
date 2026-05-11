---
source_url: https://github.github.com/gh-aw/setup/creating-workflows
source_type: docs
title: "GitHub Agentic Workflows: Creating Workflows (Setup Guide)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#420"
---

# GitHub Agentic Workflows: Creating Workflows (Setup Guide)

> The practical quickstart guide for creating gh-aw workflows, providing four
> verbatim example prompts for common workflow types, a manual editing procedure
> with exact commands, and documentation of `create.md` as a third
> URL-addressable self-contained prompt (alongside `install.md` and `debug.md`).

## Source Context

- **Type**: docs (official GitHub Agentic Workflows setup guide, "Setup >
  Creating Workflows" — practitioner quickstart for the creation phase, not
  the comprehensive authoring lifecycle covered in `docs-ghaw-agentic-authoring.md`)
- **Author credibility**: First-party from GitHub Next / Microsoft Research.
  This is the canonical setup guide for creating new workflows; it is the
  practical entry point rather than the deep-dive authoring guide. All CLI
  commands, prompt templates, and workflow procedures are production-verified
  first-party documentation.
- **Scope**: Three creation methods — (1) GitHub Web Interface with Copilot,
  (2) coding agent step-by-step, (3) manual editing — plus repository
  initialization via `gh aw init`. Estimated time: "5-15 minutes depending
  on complexity." Does NOT cover: debugging (see `docs-ghaw-agentic-authoring.md`
  Claim 5), workflow migration or reuse (see Claim 3 in that note), the
  compilation model in depth (see `docs-ghaw-compilation-process.md`), or
  the security architecture (see `docs-ghaw-how-they-work.md`).

## Extracted Claims

### Claim 1: `create.md` is a third URL-addressable self-contained prompt in the gh-aw ecosystem, extending the install.md/debug.md pattern to workflow creation itself

- **Evidence**: All four example prompts on this page reference
  `https://raw.githubusercontent.com/github/gh-aw/main/create.md` as the
  instruction source. The pattern is structurally identical to `install.md`
  (initialization) and `debug.md` (debugging) documented in
  `docs-ghaw-agentic-authoring.md` Claims 6 and 7: any AI assistant fetches
  the URL and follows self-contained instructions.
- **Confidence**: settled (first-party; the URL appears verbatim in all four
  example prompts; same AI-assistant-agnostic pattern as `install.md`)
- **Quote**: "Create a workflow for GitHub Agentic Workflows using https://raw.githubusercontent.com/github/gh-aw/main/create.md"
- **Our assessment**: This establishes `create.md` as the third member of
  the URL-addressable prompt trio: `install.md` bootstraps a repository,
  `create.md` creates a new workflow, `debug.md` diagnoses failures.
  The full lifecycle (init → create → debug) is now URL-addressable and
  AI-assistant-agnostic. `docs-ghaw-agentic-authoring.md` Claims 6 and 7
  identified `install.md` and `debug.md` as a deliberate architectural
  pattern; this source confirms the pattern is extended to the creation step.
  For Ch02 (Harness Engineering): update the URL-addressable prompt pattern
  description to name all three lifecycle operations and their corresponding
  prompt files.

### Claim 2: The web interface creation path provides four verbatim example prompts for high-value starting workflow types (issue triage, daily activity report, documentation updater, AGENTS.md maintainer)

- **Evidence**: The page provides complete prompt text for four specific workflow
  types under the GitHub Web Interface section. These are ready-to-use starting
  points, not descriptions — they are pasted directly into Copilot or a coding
  agent.
- **Confidence**: settled (first-party; prompts are reproduced verbatim on the
  page; they are designed to be copied)
- **Quote**: "Create a workflow for GitHub Agentic Workflows using https://raw.githubusercontent.com/github/gh-aw/main/create.md The purpose of the workflow is to triage new issues: label them by type and priority, identify duplicates, ask clarifying questions when the description is unclear, and assign them to the right team members."
- **Our assessment**: These four prompts are a concrete practitioner-facing
  taxonomy of "starter workflows" — the kinds of workflows a team would build
  first when adopting gh-aw. The AGENTS.md Maintainer prompt is particularly
  notable: it establishes AGENTS.md as a first-class maintenance artifact that
  should be kept current via an automated weekly workflow. For Ch01 (Daily
  Workflows): these four prompts are a recommended starter set. For Ch02
  (Harness Engineering): they demonstrate the prompt-to-workflow authoring
  pattern in concrete terms.

### Claim 3: The manual editing path follows a precise 5-step sequence: create markdown → install extension → compile → git add specific files → configure secrets

- **Evidence**: The "Manual Editing" section gives step-by-step instructions
  with exact commands. Notably, the git add step specifies adding the `.md`
  source and the `.lock.yml` compiled file as separate named files — both
  must be committed together.
- **Confidence**: settled (first-party; commands are explicitly given)
- **Quote**: (no direct quote; see Concrete Artifacts section for the full
  command sequence extracted from the page)
- **Our assessment**: The manual editing path is important for practitioners
  who want to create workflows without a coding agent — for example, when
  migrating an existing workflow definition or making precise edits to YAML
  frontmatter. The fact that the git add step explicitly names both the `.md`
  and `.lock.yml` files reinforces `docs-ghaw-how-they-work.md` Claim 7 (both
  files belong in version control) and adds the specific command. For Ch02:
  add the manual editing procedure as the "when no coding agent is available"
  alternative to the coding-agent creation path.

### Claim 4: After `gh aw init`, teams can create and edit workflows via Copilot Chat on GitHub.com or the GitHub mobile app using the `/agent agentic-workflows` command — no local dev environment needed

- **Evidence**: The initialization section states: "After initialization, teams
  can create and edit workflows by opening Copilot Chat on github.com or the
  GitHub app and running: `/agent agentic-workflows Create a new workflow that...`"
  This is the Copilot-native path distinct from (1) the web interface creation
  path and (2) the local coding agent path.
- **Confidence**: settled (first-party; the command is explicitly documented;
  mobile app support is explicitly mentioned)
- **Quote**: (no direct quote for the command format; see Concrete Artifacts
  for the command pattern)
- **Our assessment**: This surfaces a third creation path not clearly named
  in existing notes: the `/agent agentic-workflows` Copilot command is available
  both on github.com and in the GitHub mobile app, making gh-aw accessible
  from mobile devices after `gh aw init` is run once. The mobile path is
  novel — no existing source note mentions creating or editing agentic workflows
  from the GitHub mobile app. For Ch05 (Team Adoption): the mobile-capable
  creation path lowers the barrier for product managers, designers, or other
  team members who don't run a local dev environment.

### Claim 5: The `engine:` frontmatter field must be explicitly set when using non-Copilot coding agents (Claude, Codex), and defaults to Copilot

- **Evidence**: The VSCode/Claude/Codex/Copilot section's Step 3 instructs:
  "adjust the `engine:` field in workflow frontmatter if not using Copilot."
  This makes clear that (a) Copilot is the default engine, and (b) switching
  engines requires explicit frontmatter configuration.
- **Confidence**: settled (first-party; explicit instruction in the setup guide)
- **Quote**: "adjust the `engine:` field in workflow frontmatter if not using Copilot"
- **Our assessment**: This adds a concrete operational detail to
  `docs-ghaw-how-they-work.md` Claim 9 (multi-engine support is first-class).
  That note established that switching engines is a frontmatter change, not a
  code change; this note names the specific field (`engine:`) that practitioners
  must adjust. For Ch02: add this as a concrete action item under the
  engine-selection pattern — "to use Claude or Codex instead of Copilot,
  set `engine: claude` or `engine: codex` in the workflow frontmatter."

### Claim 6: The web interface creation path is characterized as "slow and non-interactive but it is incredibly useful to turn an idea to reality in a couple minutes"

- **Evidence**: The page frames the web interface explicitly as a speed-over-
  interactivity trade-off, recommending coding agents for "more interactive
  experience" but validating the web interface for rapid prototyping.
- **Confidence**: settled (first-party characterization; consistent with
  `docs-ghaw-agentic-authoring.md` Claim 4's framing of the web interface)
- **Quote**: "slow and non-interactive but it is incredibly useful to turn an
  idea to reality in a couple minutes"
- **Our assessment**: The framing is slightly more candid than
  `docs-ghaw-agentic-authoring.md` Claim 4 ("While non-interactive, it's
  useful for quickly turning an idea into a working workflow"). Both sources
  agree on the trade-off — the creating-workflows page uses stronger language
  ("slow") while the agentic-authoring guide uses more neutral language.
  This is not a contradiction — both acknowledge the non-interactivity limitation
  and value the speed of the initial creation. The choosing criterion is clear:
  use the web interface for speed and simplicity; use a coding agent for
  iterative refinement.

### Claim 7: First-run failure on unconfigured repositories is expected; the workflow detects missing tokens and creates a setup-guidance issue

- **Evidence**: A tip callout on the page states this explicitly.
- **Confidence**: emerging (consistent with `docs-ghaw-agentic-authoring.md`
  Claim 2, which documents the same behavior from the same documentation tier)
- **Quote**: "On the first run in a new repository, the workflow will surely
  fail because the secrets are not configured. The agentic workflow should
  detect the missing tokens and create an issue with instructions on how to
  configure them."
- **Our assessment**: This is a direct corroboration of `docs-ghaw-agentic-authoring.md`
  Claim 2. The quote is identical, confirming that this "graceful
  failure-as-onboarding" behavior is documented consistently across the setup
  guide and the authoring lifecycle guide. The pattern is worth naming in Ch02:
  design first-run failures as onboarding flows by having the agent detect
  missing preconditions and escalate via issue creation rather than failing
  silently.

### Claim 8: Completed workflows can be triggered in two ways: from the GitHub Actions tab or via `gh aw run` from the terminal

- **Evidence**: Both the coding agent path and the manual editing path mention
  these two run methods. The Actions tab path requires no CLI; the `gh aw run`
  path is for terminal-first practitioners.
- **Confidence**: settled (first-party; consistent with `docs-ghaw-how-they-work.md`
  Claim 11)
- **Quote**: "Workflows can be triggered from the Actions tab or using `gh aw run` command."
- **Our assessment**: This confirms `docs-ghaw-how-they-work.md` Claim 11's
  `gh aw run` as a trigger mechanism and adds the Actions tab as an equally
  valid alternative for practitioners who prefer the GitHub web UI. No novel
  content here; primarily a corroboration. The two-path trigger model is
  worth noting in Ch01 as a "works for CLI and browser" pattern.

## Concrete Artifacts

### Four Verbatim Example Prompts for Starting Workflows

*Source: creating-workflows page, "GitHub Web Interface" section*

```
# Prompt 1: Issue Triage
Create a workflow for GitHub Agentic Workflows using https://raw.githubusercontent.com/github/gh-aw/main/create.md
The purpose of the workflow is to triage new issues: label them by type and priority,
identify duplicates, ask clarifying questions when the description is unclear, and
assign them to the right team members.

# Prompt 2: Daily Activity Report
Create a workflow for GitHub Agentic Workflows using https://raw.githubusercontent.com/github/gh-aw/main/create.md
The purpose of the workflow is a daily report on recent activity in the repository,
delivered as an issue. The report should summarize new issues, pull requests merged,
and any open blockers.

# Prompt 3: Documentation Updater
Create a workflow for GitHub Agentic Workflows using https://raw.githubusercontent.com/github/gh-aw/main/create.md
The purpose of the workflow is to run daily and keep the repository documentation
up to date: identify doc files that are out of sync with recent code changes and
open a pull request with the necessary updates.

# Prompt 4: AGENTS.md Maintainer
Create a workflow for GitHub Agentic Workflows using https://raw.githubusercontent.com/github/gh-aw/main/create.md
The purpose of the workflow is to run weekly and maintain the AGENTS.md file:
review merged pull requests and updated source files since the last run, then
open a pull request that keeps AGENTS.md accurate and current.
```

### URL-Addressable Prompt Trio (Complete Picture)

*Source: creating-workflows page + docs-ghaw-agentic-authoring.md (Claims 6, 7)*

```
gh-aw URL-addressable self-contained prompts:

1. install.md — Repository initialization
   URL:     https://raw.githubusercontent.com/github/gh-aw/main/install.md
   CLI:     gh aw init
   Purpose: Bootstrap a repository for agentic authoring

2. create.md — Workflow creation
   URL:     https://raw.githubusercontent.com/github/gh-aw/main/create.md
   CLI:     (no direct CLI; used via the prompt pattern)
   Purpose: Create a new agentic workflow from a natural-language description

3. debug.md — Workflow debugging
   URL:     https://raw.githubusercontent.com/github/gh-aw/main/debug.md
   CLI:     /agent agentic-workflows debug <run-url>
   Purpose: Diagnose and fix a failing workflow run

All three work with any AI assistant (Copilot, Claude, Codex, local models).
CLI equivalents exist for install.md and debug.md; create.md is accessed
directly via the prompt pattern with the URL reference.
```

### Manual Editing Procedure (Exact Commands)

*Source: creating-workflows page, "Manual Editing" section*

```bash
# Step 1: Create the workflow file
# (create .github/workflows/<workflow-name>.md with your workflow spec)

# Step 2: Install the GitHub CLI and gh-aw extension
gh extension install github/gh-aw

# Step 3: Compile markdown to YAML lock file
gh aw compile
# Generates: .github/workflows/<workflow-name>.lock.yml

# Step 4: Add, commit, and push both source and compiled files
git add .github/workflows/<workflow-name>.md
git add .github/workflows/<workflow-name>.lock.yml
git commit -m "Add <workflow-name> workflow"
git push

# Step 5: Set up repository secrets for the coding agent (if not already done)

# After push: trigger via Actions tab on GitHub.com or:
gh aw run
```

### Copilot Chat Workflow Creation Command (Post-Init)

*Source: creating-workflows page, "Initialize the Repository" section*

```
# After gh aw init is run once in the repository,
# create/edit workflows from Copilot Chat (github.com or GitHub mobile app):

/agent agentic-workflows Create a new workflow that...

# The dispatcher agent registered at .github/agents/agentic-workflows.agent.md
# handles this command and has access to gh-aw MCP tools.
```

### Three-Step Coding Agent Workflow Creation

*Source: creating-workflows page, "VSCode/Claude/Codex/Copilot" section*

```
Step 1: Start your preferred coding agent in the repository context
  Options: VSCode Agent Mode | Claude CLI | Codex | Copilot

Step 2: Enter the creation prompt:
  "Create a workflow for GitHub Agentic Workflows using
   https://raw.githubusercontent.com/github/gh-aw/main/create.md
   The purpose of the workflow is <your description here>."
  
  → The agent creates .github/workflows/<name>.md (and may open a PR)

Step 3: Set up repository secrets for the chosen engine
  → Adjust `engine:` in workflow frontmatter if not using Copilot (default)
  → Merge the PR → trigger via Actions tab or `gh aw run`
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-agentic-authoring.md` Claim 1 (`gh aw init` bootstraps a
    repository): this page confirms `gh aw init` is required for the Copilot
    Chat creation path and explicitly states "Running `gh aw init` is required
    to enable the authoring experience in the GitHub code agent."
  - `docs-ghaw-agentic-authoring.md` Claim 2 (first-run secret detection and
    issue creation): Claim 7 in this note uses the identical quote, confirming
    the graceful failure-as-onboarding pattern across both pages.
  - `docs-ghaw-agentic-authoring.md` Claim 4 (web interface for non-interactive
    creation): Claim 6 here corroborates the same trade-off framing with
    slightly different (more candid) language — "slow and non-interactive" vs.
    "while non-interactive." Both agree on the trade-off.
  - `docs-ghaw-how-they-work.md` Claim 7 (`.md` → `.lock.yml` compilation):
    the manual editing procedure (Claim 3) confirms that both `.md` and `.lock.yml`
    must be committed together, consistent with that note.
  - `docs-ghaw-how-they-work.md` Claim 9 (multi-engine support is first-class):
    Claim 5 here corroborates multi-engine support and adds the concrete action
    of adjusting the `engine:` frontmatter field.
  - `docs-ghaw-how-they-work.md` Claim 11 (`gh aw run` as a trigger): Claim 8
    here corroborates `gh aw run` and adds the Actions tab as a UI alternative.

- **Extends**:
  - `docs-ghaw-agentic-authoring.md` Claims 6 and 7 (URL-addressable
    self-contained prompt pattern documented for `install.md` and `debug.md`):
    Claim 1 here extends the pattern by documenting `create.md` as the third
    URL-addressable prompt, completing the lifecycle trio (init → create →
    debug). That note identified the pattern as generalizable; this note
    confirms the extension.
  - `docs-ghaw-how-they-work.md` Claim 11 (compile → watch → run → review
    development loop): the manual editing procedure (Claim 3) adds the git
    commit step (`git add <name>.md && git add <name>.lock.yml && git commit
    && git push`) as the bridge between compile and run — a step that is
    missing from the development loop in that note but present here explicitly.

- **Contradicts**: None identified. The slightly different language between
  this page ("slow and non-interactive but it is incredibly useful to turn
  an idea to reality in a couple minutes") and `docs-ghaw-agentic-authoring.md`
  Claim 4 ("While non-interactive, it's useful for quickly turning an idea
  into a working workflow") is a difference in phrasing emphasis, not a
  contradiction — both acknowledge the non-interactivity limitation and
  value the speed. No guidance change would result from this difference.

- **Novel**:
  - **`create.md` as the third URL-addressable prompt** (Claim 1): No existing
    source note documents `create.md` or establishes the full trio of
    URL-addressable prompts (`install.md`, `create.md`, `debug.md`).
    `docs-ghaw-agentic-authoring.md` Claims 6 and 7 documented `install.md`
    and `debug.md` but left a gap for the creation step.
  - **Four verbatim example prompts** (Claim 2, Concrete Artifacts): The four
    complete prompt templates (issue triage, daily report, documentation
    updater, AGENTS.md maintainer) are not reproduced in any existing source
    note. These are ready-to-use starting points for teams building their first
    gh-aw workflows.
  - **AGENTS.md Maintainer as a starter workflow** (Claim 2): The explicit
    recommendation of an AGENTS.md maintenance workflow (running weekly to
    review merged PRs and update AGENTS.md) establishes AGENTS.md as a
    first-class maintenance artifact deserving automated upkeep. No existing
    note recommends automating AGENTS.md maintenance specifically.
  - **Mobile app as a workflow creation surface** (Claim 4): No existing source
    note mentions the GitHub mobile app as a surface for creating or editing
    agentic workflows. The `/agent agentic-workflows` command is available on
    the GitHub mobile app after `gh aw init` is run.
  - **Manual editing procedure with exact commands** (Claim 3, Concrete
    Artifacts): The precise 5-step manual editing procedure — with exact git
    add commands for both `.md` and `.lock.yml` files — is not present in any
    existing note. It complements the coding-agent path as an alternative for
    practitioners who want direct control.

## Guide Impact

### Chapter 01: Daily Workflows

- **Add four starter workflow prompts as a practitioner starting kit**: The
  four verbatim prompts (issue triage, daily report, documentation updater,
  AGENTS.md maintainer) are a concrete recommended starting set for teams
  adopting gh-aw. Currently Ch01 describes *what* agentic workflows can do but
  doesn't give teams ready-to-paste prompt starting points. These four prompts
  close that gap. Cite this note alongside `docs-ghaw-how-they-work.md` Claim
  8 ("Continuous AI" four-pattern taxonomy) — the four starter prompts map
  directly to that taxonomy.

- **Document AGENTS.md maintenance as an automated workflow**: The AGENTS.md
  Maintainer prompt (weekly run to review PRs and update AGENTS.md) establishes
  a concrete practice not currently named in the guide. If AGENTS.md is the
  team's agent context document (per the Ch02 AGENTS.md pattern), keeping it
  current via automation is a natural step.

### Chapter 02: Harness Engineering

- **Complete the URL-addressable prompt pattern with `create.md`**: Update
  the URL-addressable prompt section (currently citing only `install.md` and
  `debug.md` from `docs-ghaw-agentic-authoring.md`) to name all three lifecycle
  prompts: init → create → debug. The full trio makes the pattern concrete
  and actionable.

- **Add `engine:` field as the engine-selection configuration point**: Claim 5
  adds the concrete frontmatter action missing from the multi-engine discussion.
  Ch02 should state: "To switch from Copilot (default) to Claude or Codex,
  set `engine: claude` or `engine: codex` in the workflow frontmatter."

- **Include the manual editing procedure as an alternative creation path**:
  For practitioners who prefer direct file editing over a coding agent (e.g.,
  for precise frontmatter control or workflow migration), add the 5-step manual
  procedure from Claim 3 and the Concrete Artifacts section.

- **Note mobile app as a creation surface for team adoption**: After `gh aw
  init`, the `/agent agentic-workflows` command is available on the GitHub
  mobile app, enabling non-developer team members to create workflows without
  a local dev environment. This lowers the adoption barrier for full teams.

## Extraction Notes

1. **Page is the setup quickstart, not the comprehensive lifecycle guide**:
   Per Prospector guidance, this page overlaps significantly with
   `docs-ghaw-agentic-authoring.md`. Extraction focused on novel material:
   the `create.md` URL, the four example prompts, the manual editing procedure,
   and the mobile app creation path. Content already fully documented in
   existing notes (debugging, `create-agentic-agent` migration, the Planner)
   was not re-extracted.

2. **Quotes rely on WebFetch AI extraction**: The WebFetch tool processes the
   page through an AI model. Quotes marked as verbatim were cross-checked where
   possible (e.g., the first-run tip quote matches exactly with
   `docs-ghaw-agentic-authoring.md` Claim 2, confirming accuracy). Quotes
   that could not be independently verified are marked `(no direct quote)` per
   MINER.md §2a.

3. **"Adding an Existing Workflow" section was minimal**: Per Prospector
   recommendation to examine this section specifically — it contains only a
   redirect to the "Reusing Workflows" guide. No extractable content beyond
   the pointer to `gh aw add` (already documented in `docs-ghaw-agentic-authoring.md`
   Claim 3).

4. **Video content not extracted**: The web interface section references an
   embedded video. WebFetch cannot extract video content. The surrounding text
   was fully captured.

5. **No contradictions filed**: Reviewed all existing source notes. The
   slight wording difference between this page ("slow and non-interactive")
   and `docs-ghaw-agentic-authoring.md` Claim 4 ("while non-interactive")
   does not meet the contradiction threshold — both lead to identical guide
   advice. No contradiction issue needed.
