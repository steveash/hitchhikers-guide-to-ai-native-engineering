---
source_url: https://github.github.com/gh-aw/guides/reusing-workflows
source_type: docs
title: "GitHub Agentic Workflows: Reusing Workflows (Guides)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-23
last_checked: 2026-05-23
status: current
confidence_overall: emerging
issue: "#878"
---

# GitHub Agentic Workflows: Reusing Workflows (Guides)

> The practitioner adoption guide for incorporating external workflows into a
> repository — documents the interactive wizard, the `--skip-secret` flag,
> automatic dependency handling, and the agent-assisted import-and-adapt pattern
> (Copilot web interface + coding agent procedure) that is absent from all existing
> corpus notes.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `guides/reusing-workflows` page —
  the "Guides" section, which provides practitioner how-to guidance for adopting
  existing workflows from external repositories. Complements the governance-focused
  `guides/organization-practices/sharing-workflows` page covered in
  `docs-ghaw-sharing-workflows.md` by addressing the consuming-team perspective
  rather than the distributing-team perspective.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's agent factory series and the full gh-aw
  documentation suite. Claims about CLI command behavior, flag semantics, and
  installation mechanics are first-party and authoritative for the `gh aw` platform.
  The page includes a standard caveat that command syntax and configuration options
  may change — CLI-specific claims are therefore treated as `emerging`.
- **Scope**: The practical adoption lifecycle from a consuming-team perspective —
  how to add a workflow from an external repository (wizard and non-interactive),
  how to use agents to import and adapt workflows to repository conventions, and
  how installed workflows stay synchronized via `gh aw update`. Does NOT cover:
  the governance/versioning model from the distributing-team perspective (that is
  `docs-ghaw-sharing-workflows.md`), the in-repo editing lifecycle for a workflow
  already installed (that is `docs-ghaw-guides-editing-workflows.md`), or the
  `create-agentic-agent` one-time fork path (that is `docs-ghaw-agentic-authoring.md`
  Claim 3).

## Extracted Claims

### Claim 1: `gh aw add-wizard` and `gh aw add` accept three reference formats — full GitHub URL, short owner/repo/workflow form, and explicit path with optional version pin

- **Evidence**: The page provides concrete examples for all three variants: full
  URL (`https://github.com/githubnext/agentics/blob/main/workflows/daily-repo-status.md`),
  short form (`githubnext/agentics/daily-repo-status`), and explicit path
  (`githubnext/agentics/workflows/ci-doctor.md`). Version pinning is shown as
  `githubnext/agentics/ci-doctor@v1.0.0`. Both the interactive wizard and the
  non-interactive `gh aw add` command accept the same reference formats.
- **Confidence**: emerging (first-party documentation; command syntax subject to
  platform change)
- **Quote**: "You can add any existing workflow you have access to from external
  repositories."
- **Our assessment**: The three-format flexibility lowers the friction of finding
  and installing workflows. The full URL path is useful for one-shot paste from a
  GitHub browser tab; the short form is ergonomic for scripted installs; the explicit
  path is useful when a repository organizes workflows in a non-default directory.
  The version-pinning syntax (`@v1.0.0`) confirms that non-interactive `gh aw add`
  supports the four-tier versioning model documented in `docs-ghaw-sharing-workflows.md`
  Claim 2. For Ch02 (Harness Engineering): document all three reference formats as
  valid inputs to both the wizard and the non-interactive command; the short form is
  the most readable for documentation examples.

### Claim 2: `--skip-secret` bypasses the interactive API key configuration prompt when the required secret is already configured at the organization or repository level

- **Evidence**: The page explicitly documents the flag and its use condition: the
  flag is specifically for cases where `COPILOT_GITHUB_TOKEN` (or equivalent) is
  already provisioned at the org or repo level, making the interactive prompt
  redundant.
- **Confidence**: emerging (first-party documentation; flag behavior subject to
  change)
- **Quote**: "The `--skip-secret` flag bypasses the interactive API key prompt. Use
  it when the required secret (e.g., `COPILOT_GITHUB_TOKEN`) is already configured
  at the organization or repository level."
- **Our assessment**: This flag is primarily relevant in CI/CD-style automated
  installs or in organizations where secrets are managed centrally and pre-provisioned
  before teams run `gh aw add-wizard`. Without this flag, the wizard would prompt
  for a secret that is already present, producing unnecessary interactive friction in
  scripted workflows. The flag name also reveals that the wizard's default behavior
  includes a secret-configuration step — useful to know when reasoning about what
  the wizard actually does. No existing source note documents this flag. For Ch02:
  document `--skip-secret` as the flag for scripted wizard invocations in org-managed
  secret environments.

### Claim 3: Workflow installation automatically retrieves and installs companion dependencies — workflows referenced in `dispatch-workflow` safe outputs and files declared in the `resources:` frontmatter field

- **Evidence**: The page states that when a workflow is installed, the system
  automatically retrieves both "Workflows referenced in the workflow's
  `dispatch-workflow` safe output" and "Files declared in the workflow's `resources:`
  frontmatter field." This retrieval is automatic and does not require explicit
  follow-up commands.
- **Confidence**: settled (first-party; this is a platform-enforced installation
  behavior, not a recommendation)
- **Quote**: (no single verbatim quote confirmed for the dependency list; see
  paraphrase in Our assessment)
- **Our assessment**: This is a non-obvious installation behavior: installing a
  workflow that orchestrates sub-workflows via `dispatch-workflow` safe outputs
  will also pull those sub-workflows automatically. Similarly, companion resource
  files declared in `resources:` frontmatter are co-installed. The practical
  implication: a single `gh aw add` or `gh aw add-wizard` command can initialize
  a multi-workflow system in one step, provided the orchestrating workflow's
  dependencies are properly declared. For Ch02: document automatic dependency
  retrieval as a design implication — orchestrating workflows should declare their
  sub-workflow dependencies in `dispatch-workflow` safe outputs or `resources:`
  frontmatter to enable single-command installation.

### Claim 4: Installing a workflow requires an explicit trust decision — the platform warns practitioners to verify the source and suitability before adding

- **Evidence**: The page includes a direct warning statement requiring the installing
  practitioner to review the workflow's content, source trustworthiness, and
  appropriateness for their specific repository before proceeding.
- **Confidence**: settled (first-party guideline; the trust check is part of the
  documented installation process, not an optional suggestion)
- **Quote**: "Check carefully that the workflow comes from a trusted source and is
  appropriate for your use in your repository."
- **Our assessment**: This security warning parallels the `private: true` access
  control model in `docs-ghaw-sharing-workflows.md` Claim 4, but operates at the
  consuming-team level. `private: true` prevents untrusted installation at the
  platform level; this warning asks practitioners to apply judgment for publicly
  available workflows. The "appropriate for your use" clause is significant — a
  workflow from a trusted source may still be inappropriate if it has permissions
  or network access that exceed what the consuming repository should grant. For
  Ch03 (Safety and Verification): add the trust-and-appropriateness check as a
  required pre-installation step alongside the `private: true` governance
  documentation. The permission-scope review ("is this appropriate for my repo?")
  is the human-judgment layer that platform controls cannot automate.

### Claim 5: GitHub Copilot users can import and adapt existing workflows via the web interface using three canonical natural-language prompts for Daily Status Report, Issue Triage, and CI Doctor workflows

- **Evidence**: The page provides three ready-to-use Copilot prompts under the
  "GitHub Web Interface" subsection, each combining `gh aw` repository initialization
  with workflow import and adaptation in a single natural language instruction:
  - Daily Status Report: "Initialize this repository for GitHub Agentic Workflows
    using https://raw.githubusercontent.com/github/gh-aw/main/install.md Then import
    and adapt the Daily Repo Status workflow from githubnext/agentics."
  - Issue Triage: "Initialize this repository for GitHub Agentic Workflows using
    https://raw.githubusercontent.com/github/gh-aw/main/install.md Then import and
    adapt an issue triage workflow from github/gh-aw."
  - CI Doctor: "Initialize this repository for GitHub Agentic Workflows using
    https://raw.githubusercontent.com/github/gh-aw/main/install.md Then import and
    adapt the CI Doctor workflow from githubnext/agentics."
- **Confidence**: emerging (first-party documentation; prompts and behavior subject
  to Copilot and gh-aw platform evolution)
- **Quote**: "You can use a coding agent to import a workflow from another repository
  and adapt it for your own."
- **Our assessment**: These three prompts combine the `gh aw init` initialization
  step (documented in `docs-ghaw-agentic-authoring.md` Claim 1) with an
  import-and-adapt step in a single instruction. This is distinct from the web
  interface workflow creation covered in `docs-ghaw-agentic-authoring.md` Claim 4
  (which creates a new workflow from scratch) — here, the agent imports an existing
  workflow from a named source repository. The three workflows (Daily Status, Issue
  Triage, CI Doctor) serve as gh-aw's canonical adoption examples, mirroring the
  three example workflows documented elsewhere in the corpus. For Ch05 (Team
  Adoption): document these three prompts as the recommended entry points for
  practitioners first adopting gh-aw — they provide a zero-to-running workflow
  experience within the GitHub web interface.

### Claim 6: The coding agent adoption procedure is a 3-step workflow: start the agent in repository context, submit a structured prompt with workflow/owner/repo variables replaced, then configure required secrets

- **Evidence**: The page's "Coding Agent" subsection enumerates three steps
  explicitly, with step 2 providing a prompt template containing three named
  placeholders (`SOURCE_WORKFLOW`, `OWNER`, `REPO`) to be replaced by the
  practitioner. The full prompt template combines initialization, import, and
  adaptation in a single instruction with an explicit constraint to preserve the
  workflow's core logic.
- **Confidence**: emerging (first-party documentation; prompt template and step
  sequence subject to change)
- **Quote**: "Start your coding agent in the context of your repository." and "Set
  up required secrets if you haven't done so already."
- **Our assessment**: The 3-step procedure makes the coding agent path procedurally
  explicit and replicable. The inclusion of repository initialization (step 2's
  `install.md` URL) makes this a self-contained workflow for repositories that
  have not yet run `gh aw init` — the agent performs initialization AND import in
  one pass. The final secrets-configuration step (step 3) is consistent with
  `docs-ghaw-agentic-authoring.md` Claim 2 (first-run secret detection). For Ch02
  (Harness Engineering): document this 3-step procedure as the coding-agent path
  for practitioners who prefer terminal-based tools over the GitHub web interface.
  The procedure works with any coding agent that can execute shell commands — not
  just Copilot.

### Claim 7: The agent-assisted import prompt template instructs agents to adapt repository-specific configuration (labels, assignees, branch names, permissions) while explicitly preserving the workflow's overall purpose and logic

- **Evidence**: The coding agent prompt template states: "Adapt the workflow for
  this repository: update any labels, assignees, branch names, and permissions to
  match this project's structure. Keep the overall purpose and logic of the workflow
  intact." Per-workflow customization guidance specifies: Daily Status → labels,
  team references, output format; Issue Triage → labels, assignee logic,
  repository-specific rules; CI Doctor → CI setup, branch naming, issue labeling
  conventions.
- **Confidence**: emerging (first-party; prompt template and customization scope
  subject to platform evolution)
- **Quote**: "Adapt the workflow for this repository: update any labels, assignees,
  branch names, and permissions to match this project's structure. Keep the overall
  purpose and logic of the workflow intact."
- **Our assessment**: The explicit constraint "keep the overall purpose and logic
  intact" is significant — it tells the agent which parts of the workflow are
  invariant (core logic, workflow purpose) and which are expected to vary per
  repository (organizational conventions). This is the agent-assisted equivalent
  of the 3-way merge in `docs-ghaw-sharing-workflows.md` Claim 3: local
  customizations (labels, assignees, branches, permissions) are layered on top of
  an upstream workflow while preserving its fundamental behavior. The four-item
  customization list (labels, assignees, branch names, permissions) aligns
  precisely with the organizational-convention layer — these are the things that
  vary across repos in the same organization, not the things that define what the
  workflow does. For Ch05 (Team Adoption) and Ch02 (Harness Engineering): document
  this four-item customization scope as the expected adaptation surface for
  importing workflows — teams should expect to configure exactly these four areas
  and nothing more for a standard adoption.

### Claim 8: The agent-assisted "import and adapt" workflow results in a `source:`-tracked installation that remains synchronized via `gh aw update`, distinct from the `create-agentic-agent` one-time fork path

- **Evidence**: The page frames agent-assisted import in the context of the
  reusing/synchronization lifecycle, immediately followed by the update section
  documenting `source:` tracking. The platform tracks origin via a `source:` entry
  added automatically at install time, enabling later synchronization.
- **Confidence**: emerging (inference from page structure and context; the
  distinction from `create-agentic-agent` is stated explicitly in
  `docs-ghaw-agentic-authoring.md` Claim 3, which directs one-time migrations
  to `create-agentic-agent` and synchronized updates to this guide)
- **Quote**: "When you add a workflow, a tracking `source:` entry remembers where
  it came from."
- **Our assessment**: The architectural distinction matters for workflow lifecycle
  decisions: agent-assisted import (via this guide's procedure) uses `gh aw add`
  or equivalent and produces a tracked installation — local customizations made
  by the agent are preserved across `gh aw update` calls via 3-way merge
  (`docs-ghaw-sharing-workflows.md` Claim 3). `create-agentic-agent`
  (`docs-ghaw-agentic-authoring.md` Claim 3) produces an untracked fork — the
  result is owned entirely by the consuming repo with no upstream linkage. The
  decision heuristic: use agent-assisted import when the team wants periodic
  upstream improvements absorbed automatically; use `create-agentic-agent` when
  the customization is so substantial it will diverge from upstream permanently.
  For Ch02: add this as an explicit decision criterion in the workflow adoption
  section: "Will you track upstream improvements? Use `gh aw add` (with or without
  an agent). Forking permanently? Use `create-agentic-agent`."

## Concrete Artifacts

### Reference Formats for `gh aw add-wizard` and `gh aw add`

```bash
# Interactive wizard — three supported reference formats:
gh aw add-wizard https://github.com/githubnext/agentics/blob/main/workflows/daily-repo-status.md
gh aw add-wizard githubnext/agentics/daily-repo-status
gh aw add-wizard githubnext/agentics/daily-repo-status --skip-secret

# Non-interactive installation:
gh aw add githubnext/agentics/ci-doctor
gh aw add githubnext/agentics/ci-doctor@v1.0.0
gh aw add githubnext/agentics/workflows/ci-doctor.md

# Update all tracked workflows:
gh aw update

# Update specific workflow(s):
gh aw update ci-doctor
gh aw update ci-doctor issue-triage
```

*Source: `guides/reusing-workflows` — "Adding Existing Workflows" section. CLI flags
subject to change per platform caveat.*

### Canonical Copilot Web Interface Prompts (Three Workflows)

```
Daily Status Report:
  Initialize this repository for GitHub Agentic Workflows using
  https://raw.githubusercontent.com/github/gh-aw/main/install.md
  Then import and adapt the Daily Repo Status workflow from githubnext/agentics.
  Adapt any labels, team references, and output format to suit this repository.

Issue Triage:
  Initialize this repository for GitHub Agentic Workflows using
  https://raw.githubusercontent.com/github/gh-aw/main/install.md
  Then import and adapt an issue triage workflow from github/gh-aw.
  Update the labels, assignee logic, and any repository-specific rules to
  match this project's conventions.

CI Doctor:
  Initialize this repository for GitHub Agentic Workflows using
  https://raw.githubusercontent.com/github/gh-aw/main/install.md
  Then import and adapt the CI Doctor workflow from githubnext/agentics.
  Adapt the workflow to match this repository's CI setup, branch naming, and
  issue labeling conventions.
```

*Source: `guides/reusing-workflows` — "Using an Agent to Import and Adapt a
Workflow → GitHub Web Interface" section.*

### Coding Agent Prompt Template (General)

```
Initialize this repository for GitHub Agentic Workflows using
https://raw.githubusercontent.com/github/gh-aw/main/install.md

Then import and adapt the SOURCE_WORKFLOW workflow from OWNER/REPO.
The source is at https://github.com/OWNER/REPO/blob/main/workflows/SOURCE_WORKFLOW.md.

Adapt the workflow for this repository: update any labels, assignees, branch
names, and permissions to match this project's structure. Keep the overall
purpose and logic of the workflow intact.
```

*Source: `guides/reusing-workflows` — "Using an Agent → Coding Agent" section.
Replace `SOURCE_WORKFLOW`, `OWNER`, and `REPO` with the target workflow details.*

### 3-Step Coding Agent Adoption Procedure

```
Step 1: Start your coding agent in the context of your repository.

Step 2: Enter the prompt template above, replacing SOURCE_WORKFLOW, OWNER,
        and REPO with the workflow you want to import.

Step 3: Set up required secrets if you haven't done so already.

Tip: On the first run in a new repository, the workflow may fail because
     secrets are not yet configured. The workflow should detect missing tokens
     and open an issue with setup instructions.
```

*Source: `guides/reusing-workflows` — "Using an Agent → Coding Agent" section.
Steps 1 and 3 are verbatim. Tip content paraphrased from the callout box.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-sharing-workflows.md` Claim 1 ("`gh aw add <org>/<repo>/<workflow>@<version>`
    is the primary mechanism for platform teams distributing versioned workflows"): the
    new source corroborates `gh aw add` with version pinning syntax (`@v1.0.0`) as the
    non-interactive installation command, and adds the full URL and short-form reference
    variants not enumerated in that claim.
  - `docs-ghaw-sharing-workflows.md` Claim 3 ("`gh aw update` with 3-way merge default"):
    corroborated by the update section of this source, which documents the same 3-way
    merge default and `--no-merge` flag behavior. This source adds the multi-workflow
    update variant (`gh aw update ci-doctor issue-triage`).
  - `docs-ghaw-sharing-workflows.md` Claim 10 ("`gh aw add-wizard` provides interactive
    setup, while `gh aw add` supports scripted deployments"): corroborated and extended
    with specific format variants and the `--skip-secret` flag.
  - `docs-ghaw-agentic-authoring.md` Claim 1 (`gh aw init` and the `install.md` URL
    as the initialization path): the agent prompts in this source use the same
    `install.md` URL (`https://raw.githubusercontent.com/github/gh-aw/main/install.md`),
    confirming that the reusing-workflows agent path extends rather than replaces the
    initialization step.
  - `docs-ghaw-agentic-authoring.md` Claim 2 (first-run secret detection and setup
    issue creation): the Tip callout in this source ("On the first run in a new
    repository, the workflow may fail because secrets are not yet configured")
    corroborates the same first-run behavior for imported workflows.

- **Extends**:
  - `docs-ghaw-sharing-workflows.md` Claim 10 (`gh aw add-wizard` interactive setup):
    this source adds the three reference formats, the `--skip-secret` flag, and the
    automatic dependency retrieval behavior — converting a one-sentence claim into
    a complete operational picture.
  - `docs-ghaw-agentic-authoring.md` Claim 3 (`create-agentic-agent` vs. `gh aw add`
    distinction): that claim contrasts one-time fork vs. synchronized reuse at the
    mechanism level. This source extends it with the agent-assisted tracked-adoption
    path — a middle path where an agent performs the import-and-adapt operation but
    the result remains tracked for `gh aw update` synchronization.
  - `docs-ghaw-agentic-authoring.md` Claim 4 (GitHub web interface for workflow
    creation): that claim covers using Copilot to create new workflows. This source
    extends the web interface use case to importing and adapting existing workflows
    from named source repositories.

- **Contradicts**: None identified. Reviewed all existing source notes in the corpus.
  No claim in this source materially opposes any existing source note. The three
  reference format variants (full URL, short form, explicit path) are additive
  specificity to existing documentation of `gh aw add-wizard`. The `--skip-secret`
  flag and automatic dependency retrieval are new details not mentioned in existing
  notes, not contradictions of them. No contradiction issue filed.

- **Novel** (what this note adds that no prior source covers):
  - **`--skip-secret` flag** (Claim 2): Not documented in any existing corpus note.
    The flag and its use condition (pre-configured org/repo secrets) are entirely new.
  - **Automatic dependency retrieval** (Claim 3): The behavior of automatically
    pulling `dispatch-workflow`-referenced sub-workflows and `resources:` companion
    files at install time is not documented in any existing corpus note.
  - **Copilot web interface import prompts** (Claim 5): `docs-ghaw-agentic-authoring.md`
    Claim 4 covers the Copilot web interface for creating new workflows; no existing
    note documents using the web interface to import and adapt existing workflows
    with the three canonical prompts.
  - **Coding agent adoption procedure** (Claim 6): The 3-step procedure with a
    prompt template for coding agent adoption is entirely new to the corpus. Prior
    notes cover `create-agentic-agent` (one-time migration) and `gh aw add`
    (direct CLI install), but not the agent-mediated import-and-adapt workflow.
  - **Four-item customization surface** (Claim 7): The explicit delineation of what
    agents should and should not change during workflow adaptation (labels, assignees,
    branch names, permissions — but not core logic) is novel to the corpus.
  - **Tracked vs. forked import decision heuristic** (Claim 8): While
    `docs-ghaw-agentic-authoring.md` Claim 3 documents the fork/track distinction
    at the mechanism level, this source provides the decision criterion from the
    consuming team's perspective: "keep the overall purpose and logic intact" =
    tracked import; "substantial customization that will diverge permanently" =
    `create-agentic-agent` fork.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add `--skip-secret` to the workflow installation reference** (Claim 2): The
  existing corpus documents `gh aw add-wizard` and `gh aw add` without mentioning
  their flag variants. Add `--skip-secret` as the flag for CI/CD-style scripted
  wizard invocations in environments with centrally managed secrets. Place alongside
  the four-tier versioning flags from `docs-ghaw-sharing-workflows.md`.

- **Add automatic dependency retrieval as a design implication for orchestrating
  workflows** (Claim 3): Practitioners designing orchestrating workflows should know
  that sub-workflows declared in `dispatch-workflow` safe outputs and `resources:`
  frontmatter are auto-installed when the parent is installed. This should appear in
  the chapter's workflow composition guidance — it changes the question from "how do
  I install all the pieces?" to "how do I declare the pieces correctly?"

- **Add the coding agent adoption procedure as a named path** (Claims 6, 7): The
  guide currently documents `gh aw add` (direct CLI) and `create-agentic-agent`
  (one-time fork). Add the coding agent import-and-adapt procedure as the third
  path: agent-mediated tracked installation. Decision criterion: tracked path
  (`gh aw add` or agent import) when the team wants upstream improvements; fork path
  (`create-agentic-agent`) when customization will permanently diverge.

### Chapter 04/05: Orchestration & Composition / Team Adoption

- **Add the Copilot web interface import prompts as onboarding entry points**
  (Claim 5): The three canonical Copilot prompts (Daily Status, Issue Triage,
  CI Doctor) are the lowest-friction path to adopting a gh-aw workflow — no CLI,
  no local dev environment, one paste into GitHub Copilot. Document these as the
  recommended starting point for teams evaluating gh-aw without committing to full
  CLI setup.

- **Add the four-item customization surface as a team adoption checklist** (Claim 7):
  When a team adopts a workflow via agent-assisted import, the expected configuration
  work is: (1) labels, (2) assignee logic, (3) branch names, (4) permissions. Document
  this as a scoped adoption checklist so teams can plan the adaptation effort
  accurately — typically one agent-assisted pass is sufficient.

### Chapter 03: Safety and Verification

- **Add the trust-and-appropriateness check as a pre-installation step** (Claim 4):
  The explicit warning ("Check carefully that the workflow comes from a trusted
  source and is appropriate for your use in your repository.") should appear in
  the guide's discussion of workflow governance. This is the human-judgment layer
  that complements `private: true` platform controls — `private:` prevents
  unauthorized external installation; the trust check asks practitioners to verify
  that a publicly available workflow has appropriate permissions scope for their
  repository.

## Extraction Notes

1. **Source is the practitioner adoption guide, not the governance guide**: The
   Prospector's triage correctly identifies this as the consuming-team perspective.
   The governance/versioning layer (four-tier versioning, `private: true`, enterprise
   central-repo pattern) was deliberately not re-extracted — it is fully covered in
   `docs-ghaw-sharing-workflows.md`. This note focuses on what that note does not
   cover: the adoption UX (wizard variants, agent-assisted import, coding agent
   procedure).

2. **Multiple WebFetch passes for verbatim accuracy**: Six separate WebFetch passes
   were used to extract content from this page, including targeted passes for
   verbatim quotes. All quotes marked verbatim were confirmed consistent across at
   least two passes. Quotes for the three Copilot prompts and the coding agent prompt
   template were confirmed across two targeted passes. The dependency retrieval claim
   (Claim 3) was extracted from two passes where the wording appeared in quotation
   marks in both; treated as likely verbatim but the Quote field is set to
   "(no direct quote; see paraphrase in Our assessment)" to be conservative.

3. **`create-agentic-agent` distinction**: This source's agent import approach is
   intentionally scoped to the tracked-adoption path. The `create-agentic-agent`
   mechanism (one-time fork with no update tracking) is covered in
   `docs-ghaw-agentic-authoring.md` Claim 3 and was not re-extracted here. The
   Claim 8 cross-reference to that mechanism is analytical context, not extraction
   from this source.

4. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   the gh-aw platform state as of the 2026-05-23 extraction date.

5. **No contradictions to file**: Reviewed all existing source notes and the
   CONTRADICTIONS.md ledger. No claims in this source materially oppose any
   existing source note at the MINER.md §4a filing threshold. All claims are
   either novel or additive specificity to existing documentation.
