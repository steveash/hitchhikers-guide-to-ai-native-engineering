---
source_url: https://github.github.com/gh-aw/guides/reusing-workflows
source_type: docs
title: "GitHub Agentic Workflows: Reusing Workflows (Guides)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: emerging
issue: "#878"
---

# GitHub Agentic Workflows: Reusing Workflows (Guides)

> The practitioner-facing guide for adopting workflows from other repositories — documents the
> three installation paths (interactive wizard, scriptable add, agent-assisted adapt), the
> complete `gh aw update` synchronization lifecycle, and ready-to-use coding-agent prompts
> for importing and customizing specific workflows.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `guides/reusing-workflows` page — the
  "Guides" section, practitioner how-to for adopting workflows from external repositories.
  Distinct from the "Organization Practices → Sharing Workflows" page, which documents the
  governance and versioning model from a platform team's perspective; this page documents
  the practitioner-consumer experience of finding, importing, adapting, and keeping
  workflows up to date.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research (the same team
  behind Peli de Halleux's agent factory series and all gh-aw documentation). Claims about
  CLI commands, flag behavior, and agent-assisted adaptation patterns are authoritative
  platform documentation. Platform explicitly notes "recommended patterns, commands, and
  configuration options may change" — CLI-specific claims are marked `emerging` accordingly.
- **Scope**: The consumer/adopter lifecycle for workflows from external repositories:
  interactive import via `gh aw add-wizard`, non-interactive import via `gh aw add`,
  agent-assisted import+adapt via Copilot or coding agents, and synchronization via
  `gh aw update`. Covers trust requirements for external workflows and the
  `private: true` installation restriction. Does NOT cover: the governance/versioning
  model from the platform team's perspective (see `docs-ghaw-sharing-workflows.md`),
  the editing lifecycle once a workflow is installed (see `docs-ghaw-guides-editing-workflows.md`),
  or the compilation model (see `docs-ghaw-compilation-process.md`).

## Extracted Claims

### Claim 1: `gh aw add-wizard` is the interactive command for importing an external workflow with guided prompts, accepting both full GitHub URLs and shorthand notation

- **Evidence**: The page documents the command with both URL forms and the `--skip-secret`
  flag:
  ```
  gh aw add-wizard https://github.com/githubnext/agentics/blob/main/workflows/daily-repo-status.md
  gh aw add-wizard githubnext/agentics/daily-repo-status
  gh aw add-wizard githubnext/agentics/daily-repo-status --skip-secret
  ```
  After adding, the user must "commit and push the changes to your repository."
- **Confidence**: settled (first-party documentation; command is explicitly documented)
- **Quote**: "Use the `gh aw add-wizard` command to add a workflow with interactive guidance"
- **Our assessment**: The shorthand `owner/repo/workflow-name` form is the more common
  usage. The `--skip-secret` flag handles the case where an organization has already
  configured the required secret (e.g., `COPILOT_GITHUB_TOKEN`) at the org level —
  avoiding a redundant interactive prompt. The "commit and push" reminder is intentional:
  installed workflows are written to disk but do not activate until pushed. For Ch02
  (Harness Engineering): `gh aw add-wizard` is the recommended interactive path for
  first-time adopters.

### Claim 2: `gh aw add` provides non-interactive, scriptable workflow installation with version pinning and a full flag set for automation

- **Evidence**: The page documents the command with version pinning and explicit path forms:
  ```
  gh aw add githubnext/agentics/ci-doctor              # short form
  gh aw add githubnext/agentics/ci-doctor@v1.0.0       # with version
  gh aw add githubnext/agentics/workflows/ci-doctor.md # explicit path
  ```
  Available flags: `--name`, `--pr`, `--force`, `--engine`, `--verbose`. "The `source`
  field is automatically added to workflow frontmatter for tracking origin and enabling
  updates."
- **Confidence**: settled (first-party documentation; command and flags explicitly named)
- **Quote**: "The `source` field is automatically added to workflow frontmatter for
  tracking origin and enabling updates."
- **Our assessment**: The automatic `source:` frontmatter insertion is the linchpin of
  the update lifecycle — `gh aw update` relies on this field to know where to fetch
  upstream changes. For automation-facing use cases (CI/CD pipelines, Makefiles,
  onboarding scripts), `gh aw add` is preferred over `gh aw add-wizard` because it
  requires no interactive prompts. The `--pr` flag likely creates a PR rather than
  committing directly, enabling review before activation. For Ch02: use `gh aw add`
  in documented setup scripts; `gh aw add-wizard` for developer-interactive adoption.

### Claim 3: Installing a workflow automatically fetches dependent workflows (via `dispatch-workflow` safe outputs) and companion files (via `resources:` frontmatter)

- **Evidence**: "When installing a workflow, `gh aw add` also automatically fetches:
  Workflows referenced in the workflow's `dispatch-workflow` safe output. Files declared
  in the workflow's `resources:` frontmatter field (companion workflows, custom actions)."
  The page links to both the safe-outputs reference and the frontmatter resources: reference.
- **Confidence**: emerging (first-party documentation; behavior is described but flagged
  as subject to change with platform caveat)
- **Quote**: "When installing a workflow, `gh aw add` also automatically fetches: Workflows
  referenced in the workflow's `dispatch-workflow` safe output. Files declared in the
  workflow's `resources:` frontmatter field (companion workflows, custom actions)."
- **Our assessment**: This is a non-obvious but important capability. A multi-workflow
  orchestration pattern (where a primary workflow dispatches sub-workflows) can be
  installed in a single `gh aw add` command because the installer follows the
  `dispatch-workflow` references transitively. Similarly, any supporting files declared
  in `resources:` (custom actions, companion config files) are pulled in automatically.
  For Ch04 (Orchestration): this means an orchestrator+worker workflow pair can be
  distributed as a unit — installing the orchestrator also installs its workers.

### Claim 4: `private: true` in workflow frontmatter prevents installation into other repositories; attempting to install such a workflow fails with an error

- **Evidence**: "Workflows marked with `private: true` in their frontmatter cannot be
  added to other repositories. Attempting to do so will fail with an error. See
  Private Workflows for details."
- **Confidence**: emerging (first-party documentation; platform-enforced at install
  time per the documentation)
- **Quote**: "Workflows marked with `private: true` in their frontmatter cannot be
  added to other repositories."
- **Our assessment**: This corroborates `docs-ghaw-sharing-workflows.md` Claim 4 with
  the consumer-side view: the failure is a hard error, not a silent skip. The enforcement
  is at install time (`gh aw add`), which means `private: true` is a platform-enforced
  boundary, not just a convention. For Ch05 (Team Adoption): platform teams should
  mark all internal-only workflows `private: true` — the enforcement is automatic and
  does not rely on consuming teams self-policing.

### Claim 5: Users must verify the trustworthiness and appropriateness of any external workflow before importing it

- **Evidence**: The page includes a Note callout: "Check carefully that the workflow
  comes from a trusted source and is appropriate for your use in your repository.
  Review the workflow's content and understand what it does before adding it to
  your repository."
- **Confidence**: settled (explicit recommendation in official documentation; this
  is a security guidance note, not an incidental observation)
- **Quote**: "Check carefully that the workflow comes from a trusted source and is
  appropriate for your use in your repository. Review the workflow's content and
  understand what it does before adding it to your repository."
- **Our assessment**: This is the supply chain security guidance for workflow adoption.
  Like reviewing a third-party GitHub Action before use, consuming an external agentic
  workflow requires understanding what agent actions it will take, what tools and
  permissions it requests, and whether those are appropriate for your repository. The
  explicit callout is significant — it signals the platform team considers this a
  meaningful risk, not a theoretical one. For Ch03 (Safety and Verification): recommend
  a workflow review checklist as a pre-import step, analogous to reviewing a GitHub
  Actions workflow for unexpected `curl | bash` patterns.

### Claim 6: Coding agents (Copilot, Claude, Codex, VSCode) can import AND adapt a workflow in a single step using a structured template prompt, also initializing the repository for GHAW if needed

- **Evidence**: The page documents a template prompt for the "Coding Agent" path:
  ```
  Initialize this repository for GitHub Agentic Workflows using
  https://raw.githubusercontent.com/github/gh-aw/main/install.md
  Then import and adapt the SOURCE_WORKFLOW workflow from OWNER/REPO. The source is at
  https://github.com/OWNER/REPO/blob/main/workflows/SOURCE_WORKFLOW.md.
  Adapt the workflow for this repository: update any labels, assignees, branch names,
  and permissions to match this project's structure. Keep the overall purpose and logic
  of the workflow intact.
  ```
  Step 1 is to start the coding agent in the repository context; step 3 is to set up
  required secrets.
- **Confidence**: emerging (first-party documentation; agent behavior depends on the
  specific coding agent used)
- **Quote**: "You can use a coding agent to import a workflow from another repository
  and adapt it for your own. The agent reads the source workflow, customizes
  repository-specific configuration (labels, assignees, branch names, permissions),
  and sets up the repository — including initialization if needed."
- **Our assessment**: This is a meaningful extension of the `gh aw add` + manual
  customization path. Instead of installing a workflow verbatim and then manually
  editing it, the agent reads the source workflow and produces an already-adapted
  version for the target repository's conventions. The embedded initialization step
  (`install.md` URL) means this works even in repositories not yet configured for
  GHAW — the agent bootstraps and adapts in one pass. The template's explicit scope
  — "Keep the overall purpose and logic of the workflow intact" — is important: it
  prevents the agent from over-customizing into a wholly different workflow. For Ch04
  (Orchestration & Workflow Patterns): document this as the recommended import path
  when customization is a priority over tracking upstream.

### Claim 7: Three ready-to-use Copilot prompts are provided for importing and adapting Daily Status Report, Issue Triage, and CI Doctor workflows from public repositories

- **Evidence**: The page includes three named prompts under "GitHub Web Interface" for
  users with GitHub Copilot access. Each prompt follows the same structure: initialize
  GHAW, then import+adapt a specific workflow from a specific source URL. The Daily
  Status Report prompt references `githubnext/agentics/repo-status.md`; Issue Triage
  references a suitable triage workflow in `github/gh-aw`; CI Doctor references
  `githubnext/agentics/ci-doctor.md`. Each prompt instructs the agent to "adapt
  any labels, team references, and output format to suit this repository."
- **Confidence**: emerging (first-party documentation; prompts depend on Copilot
  access and current availability of source workflows)
- **Quote**: "Initialize this repository for GitHub Agentic Workflows using
  https://raw.githubusercontent.com/github/gh-aw/main/install.md\nThen import and
  adapt the Daily Repo Status workflow from githubnext/agentics. The source is at
  https://github.com/githubnext/agentics/blob/main/workflows/repo-status.md. Adapt
  any labels, team references, and output format to suit this repository."
- **Our assessment**: These prompts are the lowest-friction entry point for adopting
  GHAW: a user with Copilot access pastes one prompt into GitHub.com and gets a
  fully initialized repository with a customized workflow. The choice of Daily Status
  Report, Issue Triage, and CI Doctor as the three canonical starter workflows
  reflects the platform team's view of the most broadly applicable patterns. For
  Ch05 (Team Adoption): these prompts are the "getting started" recommendation for
  Copilot-enabled teams — they bypass the CLI entirely.

### Claim 8: The agent-assisted import+adapt approach is explicitly positioned as the right choice when significant customization is needed, with `gh aw add`/`gh aw add-wizard` recommended for straightforward imports

- **Evidence**: The page states: "Use this approach when you want to significantly
  customize a workflow before using it. For straightforward imports without
  modification, use `gh aw add` or `gh aw add-wizard` instead."
- **Confidence**: settled (explicit decision guidance from the platform documentation)
- **Quote**: "Use this approach when you want to significantly customize a workflow
  before using it. For straightforward imports without modification, use `gh aw add`
  or `gh aw add-wizard` instead."
- **Our assessment**: This is the three-way decision framework for workflow adoption:
  (1) `gh aw add-wizard` for interactive verbatim import; (2) `gh aw add` for
  scriptable verbatim import with version pinning; (3) agent-assisted prompt for
  import+adapt in one step. The decision criterion is "how much customization do you
  need before first use?" The agent path is not a replacement for `gh aw add` — it
  trades upstream tracking (the `source:` field may not be set for agent-adapted
  workflows) for upfront customization fidelity. For Ch02: add the three-way decision
  as a workflow adoption decision tree.

### Claim 9: On first run in a new repository after agent-assisted setup, the workflow may fail because secrets are not yet configured; the workflow should detect this and open a setup issue

- **Evidence**: The page includes a Tip callout: "On the first run in a new repository,
  the workflow may fail because secrets are not yet configured. The agentic workflow
  should detect missing tokens and open an issue with setup instructions."
- **Confidence**: emerging (first-party documentation; behavior is "should detect,"
  not a guaranteed platform behavior)
- **Quote**: "On the first run in a new repository, the workflow may fail because
  secrets are not yet configured. The agentic workflow should detect missing tokens
  and open an issue with setup instructions."
- **Our assessment**: This corroborates `docs-ghaw-agentic-authoring.md` Claim 2,
  which documents the same graceful-failure-as-onboarding pattern from the authoring
  guide. The pattern — detect missing precondition → open a structured setup issue
  rather than silently failing — is independently documented in both the authoring
  guide and the reusing guide, suggesting it is an intentional design principle for
  GHAW workflows. For Ch02: this pattern is worth recommending for any agentic workflow
  that has first-run preconditions (secrets, repository settings, label configuration).

### Claim 10: `gh aw update` synchronizes installed workflows with their source repositories using the `source:` frontmatter field for tracking, and uses 3-way merge by default to preserve local modifications

- **Evidence**: "When you add a workflow, a tracking `source:` entry remembers where
  it came from. You can keep workflows synchronized with their source repositories."
  Commands: `gh aw update` (all), `gh aw update ci-doctor` (single), `gh aw update
  ci-doctor issue-triage` (multiple). "Updates use 3-way merge by default to preserve
  local changes; use `--no-merge` to replace with the upstream version."
- **Confidence**: emerging (first-party documentation; CLI behavior is documented but
  subject to platform caveat)
- **Quote**: "Updates use 3-way merge by default to preserve local changes; use
  `--no-merge` to replace with the upstream version."
- **Our assessment**: The 3-way merge default is the key UX guarantee for teams that
  customize installed workflows: upstream improvements are absorbed without wiping
  local changes. This corroborates `docs-ghaw-sharing-workflows.md` Claim 3, which
  documents the same 3-way merge semantics from the distribution side. Together the
  two notes establish that 3-way merge is the platform's intentional contract for
  the update lifecycle — not a default that might change. For Ch02: document `gh aw
  update` with the 3-way merge default as the recommended maintenance pattern for
  installed workflows; recommend running periodically (e.g., in a scheduled CI job).

### Claim 11: Semantic version references update within the same major version; branch references update to latest commit; SHA references update to the latest commit on the default branch

- **Evidence**: "Semantic versions (e.g., `v1.2.3`) update to latest compatible
  release within same major version. Branch references update to latest commit.
  SHA references update to the latest commit on the default branch."
  Flags for controlling update behavior: `--major` (cross major versions), `--force`,
  `--no-merge`, `--engine`, `--verbose`.
- **Confidence**: emerging (first-party documentation; update semantics subject to
  platform evolution)
- **Quote**: "Semantic versions (e.g., `v1.2.3`) update to latest compatible release
  within same major version. Branch references update to latest commit. SHA references
  update to the latest commit on the default branch."
- **Our assessment**: The semantic version behavior (stay within major, `--major` to
  cross) aligns with the four-tier versioning model in `docs-ghaw-sharing-workflows.md`
  Claim 2. Note a potential tension: `docs-ghaw-sharing-workflows.md` Claim 2 describes
  SHA pins as "Never moves (SHA-bound) — Absolute reproducibility; explicit re-install
  only." This note says SHA references update to latest on default branch. These may
  refer to different scenarios (explicit `@<sha>` pin vs. a `source:` field that records
  a SHA from a branch-based install), but the distinction is not clarified in either
  source. See Extraction Notes §3 for details. For Ch02: use `--major` explicitly when
  intentionally upgrading major versions; rely on default behavior for compatible updates.

### Claim 12: Merge conflicts from `gh aw update` require manual resolution of conflict markers followed by running `gh aw compile`

- **Evidence**: "When merge conflicts occur, manually resolve conflict markers and
  run `gh aw compile`."
- **Confidence**: settled (first-party documentation; the conflict resolution step is
  explicitly stated)
- **Quote**: "When merge conflicts occur, manually resolve conflict markers and run
  `gh aw compile`."
- **Our assessment**: The requirement to re-run `gh aw compile` after conflict resolution
  is consistent with the compilation model: any change to frontmatter (where most
  structurally significant customizations live) requires recompilation. If the merge
  conflict is in the markdown body only, recompilation may not be strictly necessary —
  but the guidance blanket-requires it, likely to ensure the lock file stays in sync
  with the resolved source. For Ch02: document the compile step as a required post-
  conflict-resolution action, not optional cleanup.

## Concrete Artifacts

### Three Workflow Import Paths (from page structure)

```
Path 1: Interactive installation (guided prompts)
  gh aw add-wizard <workflow-url>
  # e.g., gh aw add-wizard githubnext/agentics/daily-repo-status
  # e.g., gh aw add-wizard githubnext/agentics/daily-repo-status --skip-secret
  # After: commit and push the added files

Path 2: Non-interactive installation (scriptable, version-pinned)
  gh aw add githubnext/agentics/ci-doctor              # short form
  gh aw add githubnext/agentics/ci-doctor@v1.0.0       # with version
  gh aw add githubnext/agentics/workflows/ci-doctor.md # explicit path
  # Flags: --name, --pr, --force, --engine, --verbose

Path 3: Agent-assisted import + adapt (significant customization)
  # Use this prompt with Copilot (web) or any coding agent (terminal):
  Initialize this repository for GitHub Agentic Workflows using
  https://raw.githubusercontent.com/github/gh-aw/main/install.md
  Then import and adapt the SOURCE_WORKFLOW workflow from OWNER/REPO.
  The source is at https://github.com/OWNER/REPO/blob/main/workflows/SOURCE_WORKFLOW.md.
  Adapt the workflow for this repository: update any labels, assignees, branch names,
  and permissions to match this project's structure. Keep the overall purpose and
  logic of the workflow intact.

Decision rule (from documentation):
  Significant customization needed? → Path 3 (agent-assisted)
  Straightforward import, no modification? → Path 1 (wizard) or Path 2 (add)
```

*Source: `guides/reusing-workflows` — "Adding Existing Workflows" and "Using an Agent
to Import and Adapt a Workflow" sections.*

### Ready-to-Use Copilot Prompts (verbatim from page)

```
Daily Status Report:
  Initialize this repository for GitHub Agentic Workflows using
  https://raw.githubusercontent.com/github/gh-aw/main/install.md
  Then import and adapt the Daily Repo Status workflow from githubnext/agentics.
  The source is at https://github.com/githubnext/agentics/blob/main/workflows/repo-status.md.
  Adapt any labels, team references, and output format to suit this repository.

Issue Triage:
  Initialize this repository for GitHub Agentic Workflows using
  https://raw.githubusercontent.com/github/gh-aw/main/install.md
  Then import and adapt an issue triage workflow from github/gh-aw. Find a suitable issue
  triage workflow in that repository and adapt it: update the labels, assignee logic, and
  any repository-specific rules to match this project's conventions.

CI Doctor:
  Initialize this repository for GitHub Agentic Workflows using
  https://raw.githubusercontent.com/github/gh-aw/main/install.md
  Then import and adapt the CI Doctor workflow from githubnext/agentics.
  The source is at https://github.com/githubnext/agentics/blob/main/workflows/ci-doctor.md.
  Adapt the workflow to match this repository's CI setup, branch naming, and issue labeling
  conventions.
```

*Source: `guides/reusing-workflows` — "GitHub Web Interface" section (Copilot prompts).*

### `gh aw update` Command Reference (verbatim from page)

```bash
gh aw update                           # update all workflows
gh aw update ci-doctor                 # update specific workflow
gh aw update ci-doctor issue-triage    # update multiple

# Flags:
# --major    : allow crossing to a new major version
# --force    : force update (override local state)
# --no-merge : replace local copy entirely (no 3-way merge)
# --engine   : specify AI engine
# --verbose  : verbose output

# Conflict resolution:
# When merge conflicts occur, manually resolve conflict markers and run:
gh aw compile
```

*Source: `guides/reusing-workflows` — "Updating Workflows" section.*

### Automatic Dependency Fetching (verbatim from page)

```
When installing a workflow, gh aw add also automatically fetches:
  1. Workflows referenced in the workflow's dispatch-workflow safe output
  2. Files declared in the workflow's resources: frontmatter field
     (companion workflows, custom actions)
```

*Source: `guides/reusing-workflows` — "Adding Existing Workflows" section.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-sharing-workflows.md` Claim 4 (`private: true` prevents installation from
    external repositories): this source corroborates from the consumer side — the
    failure is a hard error at install time. The two notes together give both sides of
    the access control: platform teams set `private: true` (sharing-workflows), consumers
    get an error when they try to install (this note).
  - `docs-ghaw-sharing-workflows.md` Claim 3 (`gh aw update` uses 3-way merge by default
    to preserve local modifications; `--no-merge` for full replacement): this source
    independently corroborates the 3-way merge default from the consumer guide page.
    Quote verified from sharing-workflows Claim 3: "Updates use 3-way merge by default
    to preserve local modifications."
  - `docs-ghaw-sharing-workflows.md` Claim 10 (interactive `gh aw add-wizard` vs.
    scriptable `gh aw add`): this source corroborates the distinction and adds the full
    flag sets and version-pinning syntax documented from the consumer perspective.
  - `docs-ghaw-agentic-authoring.md` Claim 2 (first-run failure detecting missing tokens
    and opening a setup issue): this source independently corroborates the same graceful-
    failure-as-onboarding pattern in the Tip callout. Quote verified from agentic-authoring
    Claim 2: "The agentic workflow should detect the missing tokens and create an issue with
    instructions on how to configure them."

- **Extends**:
  - `docs-ghaw-sharing-workflows.md` Claims 1, 3, 10: that note covers the distribution
    governance model from the platform team perspective. This note adds the consumer-facing
    operational details: complete flag sets for `gh aw add`, shorthand notation examples,
    `--skip-secret` bypass, automatic dependency fetching behavior, and the update command's
    multi-workflow form. Together they give both the governance design (sharing-workflows) and
    the operational consumer experience (this note).
  - `docs-ghaw-agentic-authoring.md` Claim 3 (`create-agentic-agent` as one-time fork vs.
    `gh aw add` as synchronized reuse): the agentic-authoring note establishes the two-way
    choice (fork vs. sync). This note introduces a third option — agent-assisted import+adapt
    — that sits between the two: the agent customizes the workflow for the target repository's
    conventions, but the result may still have a `source:` field enabling future updates. The
    three-way decision (Claims 6, 8 in this note) extends Claim 3's two-way model.
  - `blog-gh-aw-operations-release-workflows.md` Claim 4 (`gh aw add-wizard` as the wizard-
    based installation mechanism): that source documents only the wizard command and version-
    pinned URL. This note adds the non-interactive `gh aw add` form, the full flag set
    (`--name`, `--pr`, `--force`, `--engine`, `--verbose`), the `--skip-secret` flag for
    `gh aw add-wizard`, and the agent-assisted adaptation path.

- **Contradicts**:
  - Potential tension with `docs-ghaw-sharing-workflows.md` Claim 2 on SHA reference update
    behavior: the sharing-workflows note's versioning table describes SHA pins (`@abc123def`)
    as "Never moves (SHA-bound) — Absolute reproducibility; explicit re-install only." This
    note states "SHA references update to the latest commit on the default branch" when
    `gh aw update` is run. These may refer to different scenarios (explicit `@<sha>` install
    pin vs. a `source:` field that stores a SHA from a branch-based install), but the distinction
    is not clarified in either source. Not filing a formal contradiction because the two notes
    address different contexts (install-time versioning vs. update-time behavior), but the
    potential conflict should be resolved with a platform clarification. See Extraction Notes §3.

- **Novel** (what this note adds that no prior source covers):
  - **Three-way adoption decision framework** (Claim 8): The explicit guidance "use agent-
    assisted when you want significant customization; use `gh aw add`/`gh aw add-wizard`
    for straightforward imports" is the first clear decision rule in the corpus for choosing
    between adoption paths.
  - **Ready-to-use coding-agent prompts for three canonical workflows** (Claim 7): The
    verbatim prompts for Daily Status Report, Issue Triage, and CI Doctor — the GHAW team's
    recommended starter set — are not documented in any existing source note.
  - **Automatic dependency fetching** (Claim 3): The behavior of `gh aw add` automatically
    fetching `dispatch-workflow`-referenced workflows and `resources:`-declared files is not
    documented in any existing source note.
  - **`--skip-secret` flag** (Claim 1): The `gh aw add-wizard` flag for bypassing the API
    key prompt when secrets are pre-configured is not mentioned in any existing source note.
  - **`--name`, `--pr`, `--force`, `--engine`, `--verbose` flags for `gh aw add`** (Claim 2):
    The full flag set for the non-interactive install command is not documented in any existing
    source note.
  - **Trust review callout as supply chain security guidance** (Claim 5): The explicit platform
    recommendation to review workflow content and verify source trustworthiness before importing
    is not documented in any existing source note.
  - **Post-conflict `gh aw compile` requirement** (Claim 12): The mandatory recompile after
    manually resolving `gh aw update` merge conflicts is not documented in any existing source
    note.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add the three-way workflow adoption decision** (Claims 6, 8): The guide currently
  covers `gh aw add-wizard` as the primary install path (via `blog-gh-aw-operations-release-workflows.md`
  Claim 4). Update to document all three paths — interactive wizard, scriptable add, agent-
  assisted adapt — with the explicit decision criterion from the documentation: "use agent-
  assisted when significant customization is needed; use add/add-wizard for straightforward
  imports." Add the `create-agentic-agent` option (from `docs-ghaw-agentic-authoring.md`
  Claim 3) to complete the four-option decision tree.

- **Document `gh aw update` as the recommended workflow maintenance pattern** (Claims 10, 11, 12):
  Add `gh aw update` (with 3-way merge default) as the scheduled maintenance operation for
  keeping installed workflows current. Document the conflict resolution path: resolve markers
  manually, then `gh aw compile`. Note that the `--major` flag is required to cross major
  version boundaries intentionally.

- **Add automatic dependency fetching to the installation model** (Claim 3): When documenting
  `gh aw add`, note that orchestrator workflows that reference sub-workflows via
  `dispatch-workflow` safe outputs are installed as a unit — the adopter does not need to
  separately install each sub-workflow. This is significant for multi-workflow orchestration
  patterns.

- **Add post-conflict compile step to the workflow update checklist** (Claim 12): Any
  maintenance runbook for GHAW should include: run `gh aw update`, check for merge conflicts,
  resolve conflicts, run `gh aw compile`. Ensure the compile step is documented as required,
  not optional.

### Chapter 04: Orchestration & Workflow Patterns

- **Add the agent-assisted import+adapt pattern as a distinct workflow adoption path**
  (Claims 6, 7): The agent-assisted pattern enables rapid adoption of complex workflows by
  automating repository-specific customization (labels, assignees, branch names, permissions).
  This is especially relevant for orchestration patterns where a source workflow needs
  adaptation to the target repo's issue taxonomy or permission model before it can run.

- **Add automatic dependency fetching for orchestrator+worker pairs** (Claim 3): In
  multi-workflow orchestration patterns, installing the orchestrator with `gh aw add` also
  installs all declared sub-workflows. Document this as the recommended installation pattern
  for orchestration chains.

### Chapter 03: Safety and Verification

- **Add workflow supply chain trust review as a required pre-import step** (Claim 5): The
  platform documentation explicitly requires reviewing external workflow content for trust
  and appropriateness. Add to Ch03 as a checklist item: before running `gh aw add` on an
  external workflow, review its frontmatter (permissions, tools, network, safe-outputs) and
  markdown body (what actions it will take). This is the agentic-workflow equivalent of
  reviewing a GitHub Actions workflow for unexpected shell commands.

### Chapter 05: Composability / Team Adoption

- **Add the ready-to-use Copilot prompts as the recommended getting-started path** (Claim 7):
  For Copilot-enabled teams, the three ready-to-use prompts (Daily Status Report, Issue Triage,
  CI Doctor) provide a zero-to-running workflow path without any CLI setup. Recommend as the
  entry point for teams exploring GHAW adoption. Follow up with `gh aw update` for ongoing
  maintenance.

## Extraction Notes

1. **Consumer/practitioner perspective**: This source is the consumer-side companion to
   `docs-ghaw-sharing-workflows.md` (platform/governance side). Extraction focused on
   operational command details and the agent-assisted adaptation pattern that are absent
   from the governance note.

2. **Platform caveat noted**: The page explicitly states "recommended patterns, commands,
   and configuration options may change." All CLI-flag claims are marked `emerging`.
   Platform-enforced behaviors (`private: true` blocking installation) are marked `emerging`
   per the global caveat but are structurally hard behaviors not mere recommendations.

3. **SHA reference update tension**: The reusing-workflows page states "SHA references
   update to the latest commit on the default branch" under `gh aw update` semantics.
   The sharing-workflows note's four-tier versioning table describes SHA pins as "Never
   moves (SHA-bound)." These may be consistent if they refer to different things: (a) a
   `source:` field that records a SHA because the workflow was installed from a branch
   (the SHA was the branch HEAD at install time) might legitimately update to the new
   branch HEAD; (b) a `source:` field that records a specific `@abc123def` explicit pin
   might never update. The documentation does not clarify. Not filed as a formal
   contradiction (the contexts differ enough that both could be correct) but worth
   tracking for a platform clarification ask.

4. **No publication date**: The documentation page does not carry an explicit publication
   date. `date_published` is left null. Content is consistent with current gh-aw platform
   state as of 2026-05-25.

5. **Previous PR context**: PR #886 was opened for this issue but closed without merging.
   This source note is a fresh extraction with a deeper read and more complete claim coverage.
