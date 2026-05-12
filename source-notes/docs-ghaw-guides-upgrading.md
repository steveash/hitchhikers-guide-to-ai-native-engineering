---
source_url: https://github.github.com/gh-aw/guides/upgrading
source_type: docs
title: "GitHub Agentic Workflows: Upgrading (Guides)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#441"
---

# GitHub Agentic Workflows: Upgrading (Guides)

> The first-party step-by-step guide to upgrading gh-aw installations —
> documents `gh aw upgrade` as a single unified command covering extension
> update + automated codemod application + full recompilation, the specific
> deprecated-to-current field migrations codemods perform, the architectural
> change that workflow prompt files are now resolved from GitHub directly by
> the agent rather than managed by the CLI, and the troubleshooting paths for
> each failure mode.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `guides/upgrading` page —
  in the "Guides" section, which provides practitioner how-to guidance. Distinct
  from the "Reference" section's technical specification pages. This page is the
  canonical upgrade procedure reference, not a conceptual overview.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team that operates Peli de Halleux's agent factory. CLI commands,
  codemod behavior, and field migration patterns described here are authoritative
  for the `gh aw` platform.
- **Scope**: The full upgrade lifecycle — extension upgrade, automated codemod
  application, recompilation, review, commit, and troubleshooting. Does NOT
  cover: the internal compilation mechanics (see
  `docs-ghaw-compilation-process.md`), initial workflow creation (see
  `docs-ghaw-setup-creating-workflows.md`), or the editing lifecycle for
  day-to-day workflow changes (see `docs-ghaw-guides-editing-workflows.md`).

## Extracted Claims

### Claim 1: `gh aw upgrade` is a single unified command that handles the complete upgrade process — extension file updates, codemod application, and recompilation of all workflows

- **Evidence**: The page features a highlighted "Quick Upgrade" tip that states
  the entire upgrade process collapses to a single command. The body of the guide
  then breaks out three internal operations that this command performs.
- **Confidence**: settled (first-party documentation; the command and its scope
  are authoritative for the platform)
- **Quote**: "For most users, upgrading is a single command: `gh aw upgrade`. This
  updates agent files, applies codemods, and compiles all workflows."
- **Our assessment**: The single-command design is significant for operator
  workflow: practitioners managing many repositories do not need to coordinate
  three separate commands or worry about partial upgrades. The command is designed
  as an atomic upgrade operation. For Ch02 (Harness Engineering): document `gh aw
  upgrade` as the canonical upgrade entry point, not a sequence of individual
  compile/fix commands. The three sub-operations are still worth understanding for
  troubleshooting, but the primary recommendation is the single command.

### Claim 2: Workflow prompt files (`.github/aw/*.md`) are now resolved directly from GitHub by the agent and are no longer managed by the CLI — `gh aw upgrade` only updates the dispatcher agent file

- **Evidence**: Under the "2.1 Updates Dispatcher Agent File" section, the page
  explicitly scopes the CLI's responsibility: "Workflow prompt files
  (`.github/aw/*.md`) are resolved directly from GitHub by the agent — they're
  no longer managed by the CLI."
- **Confidence**: settled (first-party; this is a stated architectural boundary
  for what the upgrade command does and does not touch)
- **Quote**: "Workflow prompt files (`.github/aw/*.md`) are resolved directly from
  GitHub by the agent — they're no longer managed by the CLI."
- **Our assessment**: This is a significant architectural clarification. The CLI
  update step only manages `.github/agents/agentic-workflows.agent.md` (the
  dispatcher agent file). The prompt files in `.github/aw/*.md` are the workflow
  instruction bodies fetched at runtime — they are not tracked by `gh aw upgrade`
  because they are resolved dynamically at agent execution time. This means teams
  that have customized their dispatcher agent file should watch for updates to it,
  while their custom workflow prompts in `.github/aw/` remain untouched by the
  upgrade. For Ch02: clarify the distinction between the dispatcher agent file
  (managed by `gh aw upgrade`) and workflow prompt files (runtime-fetched,
  not CLI-managed).

### Claim 3: The upgrade automatically applies codemods to fix deprecated syntax in all workflow files — six specific field migrations are documented

- **Evidence**: Section 2.2 describes the automatic codemod application, and
  Step 3 ("Review the Changes") enumerates the specific migrations. The `git diff
  .github/workflows/` command is the recommended verification step.
- **Confidence**: settled (first-party; the codemod field migrations are explicitly
  listed with before/after transformations)
- **Quote**: "Typical migrations include `sandbox: false` → `sandbox.agent: false`,
  `app:` → `github-app:`, `safe-inputs:` → `mcp-scripts:`, `daily at` →
  `daily around`, and removal of deprecated `network.firewall` and
  `mcp-scripts.mode` fields."
- **Our assessment**: The codemod list reveals the evolution of gh-aw's frontmatter
  schema: sandbox configuration moved from a boolean to a nested object, app
  authentication was renamed for clarity, safe-inputs was renamed to mcp-scripts
  to better reflect its purpose, schedule syntax was softened from exact to fuzzy,
  and two fields were removed entirely. Teams with existing workflows will encounter
  exactly these changes. For Ch02: the codemod table should be documented as the
  authoritative migration reference for teams upgrading from older gh-aw versions.
  Practitioners can verify what was applied with `git diff .github/workflows/` after
  running `gh aw upgrade`.

### Claim 4: Both `.md` source files and their compiled `.lock.yml` counterparts must always be committed together — committing them separately or independently is incorrect

- **Evidence**: The "Step 4: Commit and Push" section states this as an explicit
  requirement: "Always commit both `.md` and `.lock.yml` files together." The
  commit command stages both directories: `git add .github/workflows/ .github/agents/`.
- **Confidence**: settled (first-party; the joint commit requirement is explicitly
  stated as a rule, not a recommendation)
- **Quote**: "Always commit both `.md` and `.lock.yml` files together."
- **Our assessment**: This is a correctness constraint, not just a convention: the
  `.lock.yml` is the compiled artifact that GitHub Actions executes, and it must
  match the `.md` source file it was compiled from. Committing them separately
  creates a window where the running lock file doesn't reflect the current source,
  or vice versa. This constraint extends `docs-ghaw-compilation-process.md`'s
  documentation of the `.md` → `.lock.yml` relationship to the version control
  workflow. For Ch02: add this as a required CI gate — a PR that modifies `.md`
  workflows without corresponding `.lock.yml` updates should be flagged.

### Claim 5: The `--no-fix` flag skips codemods and compilation, enabling extension-only upgrades when codemods are not needed

- **Evidence**: The "Command Options" section lists `gh aw upgrade --no-fix` with
  the description "skip codemods and compilation."
- **Confidence**: settled (first-party; CLI flag is documented)
- **Quote**: (no direct quote; see paraphrase in Our assessment — the command
  options table lists: `gh aw upgrade --no-fix # skip codemods and compilation`)
- **Our assessment**: The `--no-fix` flag is useful for practitioners who want to
  update the extension binary without touching their workflow files — for example,
  when testing a new extension version before applying migrations, or in CI
  pipelines that want to separate the extension update step from the codemod/compile
  step. It also enables a dry-run investigation: upgrade the extension, inspect
  what codemods would run, then decide whether to apply them. For Ch02: document
  `--no-fix` as the appropriate flag when decoupling the extension update from the
  workflow migration step, such as in staged rollout procedures.

### Claim 6: A backup branch must be created before upgrading — the restore path for breaking changes is `git checkout backup-before-upgrade`

- **Evidence**: The "Prerequisites" section explicitly recommends creating a backup
  branch before proceeding, providing the exact commands and the rationale.
  The "Troubleshooting" section confirms this as the recovery path for breaking
  changes.
- **Confidence**: settled (first-party; the procedure and rationale are explicitly
  documented)
- **Quote**: "Create a backup branch before upgrading so you can recover if
  something goes wrong"
- **Our assessment**: The backup branch recommendation reflects that `gh aw upgrade`
  modifies committed files (the dispatcher agent file and compiled lock files) in
  addition to workflow source files. Unlike a package manager upgrade that can be
  rolled back by reverting `package.json`, an upgrade that applies codemods to
  workflow source files and regenerates lock files may touch many files. A backup
  branch is the safe rollback mechanism. For Ch02: standardize the backup branch
  creation as the mandatory first step in any upgrade procedure, not an optional
  recommendation.

### Claim 7: Codemods can be manually applied with `gh aw fix --write -v` if the automated upgrade does not apply them

- **Evidence**: The "Troubleshooting" section documents "Codemods not applied" as
  a failure mode with the explicit fix: "Manually apply with `gh aw fix --write
  -v`."
- **Confidence**: settled (first-party; the CLI command and its flags are
  authoritative)
- **Quote**: "Codemods not applied: Manually apply with `gh aw fix --write -v`."
- **Our assessment**: The `gh aw fix` command is a standalone codemod application
  tool separate from the full upgrade pipeline. The `--write` flag applies changes
  in place (rather than just reporting them) and `-v` enables verbose output showing
  each migration applied. This is useful in contexts where `gh aw upgrade`
  aborts partway through or where practitioners want to apply codemods incrementally.
  For Ch02: document `gh aw fix --write -v` as the manual codemod application
  command alongside the automated path.

### Claim 8: Post-upgrade workflow health can be validated with `gh aw status` and secrets configuration can be verified with `gh aw secrets bootstrap`

- **Evidence**: The "Troubleshooting" section under "Workflows not running"
  documents two diagnostic commands: "check status with `gh aw status`" and
  "confirm secrets are valid with `gh aw secrets bootstrap`."
- **Confidence**: settled (first-party; CLI commands are authoritative)
- **Quote**: "Verify `.lock.yml` files are committed, check status with
  `gh aw status`, and confirm secrets are valid with `gh aw secrets bootstrap`."
- **Our assessment**: `gh aw status` and `gh aw secrets bootstrap` are the
  post-upgrade health check tools. `gh aw status` likely reports whether workflows
  are active and their current state; `gh aw secrets bootstrap` verifies that
  required secrets are present and valid. Together they form a post-upgrade
  validation checklist. For Ch02: document these two commands as the standard
  post-upgrade health check, alongside verifying that `.lock.yml` files are
  committed.

### Claim 9: Compilation errors after upgrade can be reviewed and diagnosed with `gh aw compile my-workflow --validate`

- **Evidence**: The "Troubleshooting" section under "Compilation errors" documents:
  "Review errors with `gh aw compile my-workflow --validate` and fix YAML syntax
  in source files."
- **Confidence**: settled (first-party; the CLI command and flag are authoritative)
- **Quote**: "Review errors with `gh aw compile my-workflow --validate` and fix
  YAML syntax in source files."
- **Our assessment**: The `--validate` flag runs compilation validation without
  writing output — it is the diagnostic mode for understanding what went wrong
  before fixing. This is consistent with `docs-ghaw-compilation-process.md`'s
  documentation of `--no-emit` as the CI-safe validate-without-write mode. The
  per-workflow compilation (`gh aw compile my-workflow`) isolates errors to a
  specific workflow rather than aborting across all of them. For Ch02: document
  `--validate` as the first step when compilation fails during or after upgrade.

### Claim 10: Extension upgrade failures should be resolved with a clean reinstall sequence — remove then reinstall

- **Evidence**: The "Troubleshooting" section under "Extension upgrade fails"
  documents: "Try a clean reinstall with `gh extension remove gh-aw && gh extension
  install github/gh-aw`."
- **Confidence**: settled (first-party; the command is documented as the
  recommended recovery path)
- **Quote**: "Try a clean reinstall with `gh extension remove gh-aw && gh extension
  install github/gh-aw`."
- **Our assessment**: The clean reinstall pattern removes any partial upgrade state
  and starts fresh. This is the same recommendation documented in
  `docs-ghaw-troubleshooting-common-issues.md` Claim 5 for the Playwright EOF
  error fix, confirming the pattern generalizes beyond that specific failure. For
  Ch02: document the clean reinstall as the standard recovery for any extension
  upgrade failure, not just Playwright-specific issues.

### Claim 11: Multi-version upgrades require reviewing the changelog for cumulative changes — the guide explicitly scopes this as an advanced topic

- **Evidence**: The "Advanced Topics" section states: "Upgrading across versions:
  Review the changelog for cumulative changes when upgrading across multiple
  releases."
- **Confidence**: settled (first-party; the guidance is explicit)
- **Quote**: "Review the [changelog](https://github.com/github/gh-aw/blob/main/CHANGELOG.md)
  for cumulative changes when upgrading across multiple releases."
- **Our assessment**: Multi-version upgrades are treated as requiring explicit
  human review of the changelog — the codemods may not cover all breaking changes
  across multiple releases, and the cumulative effect of several migrations may
  require manual intervention. The page appropriately scopes this to "advanced
  topics" rather than the main procedure. For Ch02: document multi-version upgrades
  as a distinct procedure that requires changelog review, as distinct from
  single-version upgrades where `gh aw upgrade` alone is sufficient.

## Concrete Artifacts

### Quick Upgrade Command

```bash
# For most users, upgrading is a single command:
gh aw upgrade
# This updates agent files, applies codemods, and compiles all workflows.
```

*Source: guides/upgrading — "Quick Upgrade" tip*

### Full Upgrade Procedure

```bash
# Step 1: Create backup branch
git checkout -b backup-before-upgrade
git checkout -  # return to your previous branch

# Step 2: Upgrade the extension
gh extension upgrade gh-aw
# Verify: gh aw version
# Clean reinstall if needed: gh extension remove gh-aw && gh extension install github/gh-aw

# Step 3: Run the upgrade command
gh aw upgrade
# Verbose output: gh aw upgrade -v
# Skip codemods/compilation: gh aw upgrade --no-fix
# Custom directory: gh aw upgrade --dir custom/workflows

# Step 4: Review the changes
git diff .github/workflows/

# Step 5: Commit and push (ALWAYS commit .md and .lock.yml together)
git add .github/workflows/ .github/agents/
git commit -m "Upgrade agentic workflows to latest version"
git push origin main
```

*Source: guides/upgrading — Steps 1–4*

### Codemod Migration Table

```
Deprecated field                  → Current field
-------------------------------------------------
sandbox: false                    → sandbox.agent: false
app:                              → github-app:
safe-inputs:                      → mcp-scripts:
daily at                          → daily around
network.firewall (field removed)
mcp-scripts.mode (field removed)
```

*Source: guides/upgrading — "Step 3: Review the Changes" section*

### Command Options Reference

```bash
gh aw upgrade                       # updates agent files + codemods + compiles
gh aw upgrade -v                    # verbose output
gh aw upgrade --no-fix              # skip codemods and compilation
gh aw upgrade --dir custom/workflows
```

*Source: guides/upgrading — "Command Options" section*

### Troubleshooting Reference

```
Failure Mode                | Diagnosis/Fix
----------------------------|--------------------------------------------------
Extension upgrade fails     | gh extension remove gh-aw && gh extension install github/gh-aw
Codemods not applied        | gh aw fix --write -v
Compilation errors          | gh aw compile my-workflow --validate (fix YAML syntax)
Workflows not running       | Check: .lock.yml committed, gh aw status, gh aw secrets bootstrap
Breaking changes            | git checkout backup-before-upgrade
```

*Source: guides/upgrading — "Troubleshooting" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-compilation-process.md` Claim 7 ("Only frontmatter changes require
    recompilation — the markdown body is loaded at runtime"): The upgrade process
    recompiles all workflows precisely because codemods change frontmatter fields
    (the six field migrations in Claim 3 all touch frontmatter YAML). The compilation
    step in `gh aw upgrade` is necessary and expected for any workflow that has
    deprecated fields. Both sources confirm that `.lock.yml` must be regenerated
    when frontmatter changes.
  - `docs-ghaw-guides-editing-workflows.md` Claim 1 ("two-part workflow
    architecture distinguishes YAML frontmatter from markdown body"): Claim 3 here
    documents exactly the type of frontmatter changes (codemod field migrations)
    that require recompilation per that architectural boundary. The upgrade guide
    is the lifecycle counterpart to the editing guide's compile-when-needed guidance.
  - `docs-ghaw-troubleshooting-common-issues.md` Claim 5 (Playwright EOF error
    resolved by `gh extension upgrade gh-aw`): The clean reinstall pattern in
    Claim 10 here (`gh extension remove gh-aw && gh extension install github/gh-aw`)
    is the same recovery sequence documented there for the Playwright failure.
    Both sources confirm this is the standard extension repair procedure.

- **Extends**:
  - `docs-ghaw-compilation-process.md` Claim 12 ("Dependabot pin updates must come
    from `gh aw compile`, which coordinates pins across all compiled workflows"):
    `gh aw upgrade` invokes `gh aw compile` internally as its third operation
    (Claim 1), so a full upgrade also triggers pin coordination across all
    workflows. Teams running regular upgrades may not need to run `gh aw compile`
    separately for Dependabot pin management.
  - `docs-ghaw-troubleshooting-common-issues.md` (general troubleshooting
    catalogue): The upgrade guide's troubleshooting section (Claim 10: clean
    reinstall) adds upgrade-specific recovery paths that complement the
    common-issues reference. Together they give a complete troubleshooting picture
    for extension and upgrade failures.
  - `docs-ghaw-setup-creating-workflows.md` (workflow creation): The upgrade guide
    completes the lifecycle that creation starts. The `gh aw secrets bootstrap`
    validation (Claim 8) is likely the same bootstrapping procedure used during
    initial setup.

- **Contradicts**: None identified. All claims are consistent with the existing
  source notes. No contradiction issue required.

- **Novel**:
  - **`gh aw upgrade` as a unified single-command upgrade** (Claim 1): No existing
    source note documents the `gh aw upgrade` command or its scope. The corpus has
    extensive coverage of `gh aw compile` but nothing on the upgrade workflow.
  - **Workflow prompt files resolved from GitHub at runtime, not CLI-managed**
    (Claim 2): The explicit scope restriction on what `gh aw upgrade` touches —
    only the dispatcher agent file, not `.github/aw/*.md` prompt files — is new
    to the corpus. This clarifies a potentially confusing architectural boundary.
  - **Specific codemod migration table** (Claim 3): The six named deprecated-to-current
    field migrations are new to the corpus. `docs-ghaw-compilation-process.md`
    documents the compilation process but does not enumerate which specific fields
    have been deprecated. `docs-ghaw-frontmatter-full-reference.md` describes
    current fields but not their deprecated predecessors.
  - **`gh aw fix --write -v` as manual codemod application** (Claim 7): The
    `gh aw fix` command is not documented in any existing source note.
  - **`gh aw secrets bootstrap` for post-upgrade secrets validation** (Claim 8):
    No existing note documents this command. The closest is the initial setup
    bootstrap in `docs-ghaw-setup-creating-workflows.md`, but `gh aw secrets
    bootstrap` as a post-upgrade health check is new.
  - **`gh aw status` for workflow health check** (Claim 8): Not documented in any
    existing source note.
  - **`gh aw compile my-workflow --validate` for compilation error diagnosis**
    (Claim 9): While `--no-emit` is documented in `docs-ghaw-compilation-process.md`
    Claim 11, `--validate` as a flag is separately documented here. These may be
    synonymous or distinct; the upgrade guide uses `--validate`.
  - **Backup branch as mandatory upgrade safety step** (Claim 6): No existing
    note documents the backup branch pattern for gh-aw upgrades specifically.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - **Add `gh aw upgrade` as the canonical upgrade procedure** (Claim 1): The
    current corpus has no chapter content on upgrading existing gh-aw installations.
    Add a dedicated upgrade section to Ch02 documenting `gh aw upgrade` as the
    entry point.
  - **Document the codemod migration table** (Claim 3): The six field migrations
    provide a versioning map for practitioners with existing workflows. Teams
    discovering that their `sandbox: false` or `app:` fields are silently ignored
    (per `docs-ghaw-troubleshooting-common-issues.md` Claim 2 on silent field
    ignoring) can cross-reference this table to understand why.
  - **Add mandatory `.md` + `.lock.yml` co-commit requirement** (Claim 4): This
    is an operational constraint that should appear in Ch02's version control
    guidance. A CI gate that checks for incomplete commits (`.md` changed without
    `.lock.yml` update, or vice versa) would catch this class of error.
  - **Add backup branch as upgrade safety practice** (Claim 6): The backup branch
    pattern generalizes to any multi-file automated migration. Document it in Ch02
    as the standard rollback preparation before running any automated upgrade or
    codemod tool.
  - **Add post-upgrade validation checklist** (Claim 8): `gh aw status` + `gh aw
    secrets bootstrap` + verify `.lock.yml` committed forms a three-step
    post-upgrade health check. Document this as a standard operational procedure.
  - **Clarify dispatcher agent file vs. workflow prompt file CLI ownership**
    (Claim 2): Add a note to the workflow authoring section clarifying that
    `gh aw upgrade` updates the dispatcher agent file but not workflow prompt
    files — teams should not expect their `.github/aw/*.md` customizations to be
    overwritten by upgrades.

## Extraction Notes

1. **WebFetch returns AI-processed content**: The gh-aw documentation is a
   rendered SPA (Astro/Starlight). WebFetch processes through an AI model.
   Two fetches were used: one full-content fetch that returned the complete
   rendered page text. Command strings, flag names, and file paths are treated
   as verbatim since they are specific technical strings. The page prose is
   marked with direct quotes where the fetched text was clearly verbatim.

2. **No publication date**: The documentation does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   current gh-aw platform state as of 2026-05-12.

3. **`--validate` vs. `--no-emit`**: The upgrade guide uses `--validate` as the
   compilation diagnostic flag (Claim 9), while `docs-ghaw-compilation-process.md`
   Claim 11 documents `--no-emit`. These may be synonymous or subtly different.
   No contradiction filed — both are documented as they appear in their respective
   sources.

4. **Advanced Topics sub-page not followed**: The "Advanced Topics" section links
   to the changelog for multi-version upgrade guidance. The changelog was not
   fetched — the main upgrading guide page was the scope of this extraction.
