---
source_url: https://github.github.com/gh-aw/reference/dependabot
source_type: docs
title: "GitHub Agentic Workflows: Dependabot Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: settled
issue: "#379"
---

# GitHub Agentic Workflows: Dependabot Reference

> Reference page for `gh aw compile --dependabot` — documents how the compiler
> automatically scans workflow files for runtime tool invocations (npm, pip, Go)
> and generates Dependabot-compatible dependency manifests, along with the
> critical rule that manifest-only Dependabot PRs must never be merged and the
> proper update workflow for runtime dependencies in gh-aw systems.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/dependabot` page —
  in the Reference section, alongside `reference/compilation-process` which covers
  the core compilation pipeline. This page is the dedicated reference for the
  `--dependabot` flag and gh-aw's Dependabot integration strategy.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team that operates Peli de Halleux's agent factory. CLI commands, flag
  behavior, manifest formats, and update workflows described here are authoritative
  for the `gh aw` platform.
- **Scope**: Covers the `--dependabot` compilation flag — how it scans for runtime
  tools, what manifests it generates, the all-workflows constraint, the proper PR
  handling workflow, MCP transitive dependency handling, and automatic ignore rule
  management. Does NOT cover: action pinning to SHAs (see
  `docs-ghaw-compilation-process.md` Claim 6 and Claim 12), the broader compilation
  pipeline (see `docs-ghaw-compilation-process.md`), or MCP server configuration
  (see `docs-ghaw-mcps.md`).

## Extracted Claims

### Claim 1: `gh aw compile --dependabot` automatically scans workflow files for runtime tool invocations and generates dependency manifests that Dependabot can monitor for security updates

- **Evidence**: The page opens with this as the primary description of the flag's
  function. The scanning and generation are automatic — practitioners do not specify
  which tools to track; the compiler discovers them by reading the workflow files.
- **Confidence**: settled (first-party documentation; the CLI flag and its behavior
  are authoritative for the platform)
- **Quote**: "The `gh aw compile --dependabot` command automatically scans workflows
  for runtime tools and generates dependency manifests that Dependabot can monitor
  for security updates."
- **Our assessment**: The integration pattern is significant: rather than manually
  maintaining dependency manifests for runtime tools used in workflows, the compiler
  generates them. This means the dependency surface is derived from the workflow
  source files, keeping Dependabot monitoring in sync with what the workflows
  actually use. The automation closes a gap common in CI systems where developers
  manually install tools (via `npx`, `pip install`, etc.) without declaring them as
  versioned dependencies, making security monitoring difficult. For Ch04 (system
  reliability & automation): this is a concrete pattern for extending automated
  security monitoring to runtime tool dependencies in agentic workflows.

### Claim 2: The compiler detects three runtime tool invocation patterns — `npx`, `pip install`, and `go install` — within workflow files and generates the corresponding ecosystem manifest for each detected pattern

- **Evidence**: The page explicitly names the three tool patterns detected and the
  manifest each produces. Detection is based on recognizing these specific command
  patterns in workflow content.
- **Confidence**: settled (first-party documentation; the detected patterns and
  resulting manifests are explicitly listed)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The three-pattern detection covers the three major runtime
  package ecosystems commonly used in automation workflows: Node.js tooling (npx),
  Python tooling (pip), and Go tooling (go install). The detection is pattern-based
  — it looks for specific invocation forms in the workflow markdown. This means
  workflows that install tools using alternative mechanisms (e.g., `npm exec` instead
  of `npx`, or `python -m pip`) may not be detected. For Ch04: teams should use the
  standard invocation forms (`npx`, `pip install`, `go install`) in their workflow
  markdown to ensure Dependabot monitoring coverage.

### Claim 3: Three ecosystem-specific manifest formats are generated — npm produces `package.json` + `package-lock.json`, pip produces `requirements.txt`, Go produces `go.mod` — all in standard formats Dependabot already understands

- **Evidence**: The page lists the three manifest outputs with their exact filenames:
  npm → `package.json` and `package-lock.json`; pip → `requirements.txt`;
  Go → `go.mod`. These are the standard manifest formats for their respective
  ecosystems.
- **Confidence**: settled (first-party; the exact output filenames are listed)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Using standard manifest formats means Dependabot needs no
  special gh-aw configuration — it reads these files the same way it reads any
  project's dependency manifests. The npm lock file (`package-lock.json`) is
  particularly valuable because it enables transitive dependency tracking, not
  just direct dependency pinning. This design choice (standard formats, not a
  custom gh-aw format) reduces onboarding cost for teams already using Dependabot
  on other manifests in the same repository. For Ch04: the generated manifests
  integrate with existing Dependabot configurations without any ecosystem-specific
  customization.

### Claim 4: All generated ecosystems receive weekly update schedules automatically added to `.github/dependabot.yml`

- **Evidence**: The page states that all ecosystems receive weekly update schedules
  in the project's Dependabot configuration file. This is applied uniformly across
  all generated manifests.
- **Confidence**: settled (first-party; the weekly schedule is described as the
  generated default)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Weekly is a reasonable default frequency for runtime tool
  dependencies in agentic workflows — frequent enough to catch security patches
  quickly, but not so frequent as to create excessive PR noise. Teams with stricter
  security requirements or more volatile dependencies may want to adjust the generated
  schedule. The fact that the schedule is generated (not hand-authored) means it stays
  in sync with detected dependencies across recompilations. For Ch04: document the
  weekly default and note that teams should review the generated schedule against
  their security posture.

### Claim 5: A hard usage constraint: `--dependabot` must compile all workflows simultaneously and cannot be used with specific workflow files or the `--dir` flag

- **Evidence**: The page names this as an "Important Usage Constraint" — the flag
  scope is always all-workflows; there is no partial compilation mode for Dependabot
  manifest generation.
- **Confidence**: settled (first-party; the constraint is explicitly documented as a
  usage limitation)
- **Quote**: "Must compile **all workflows** - cannot be used with specific files or
  `--dir` flag."
- **Our assessment**: The all-workflows constraint is a design consequence of how
  manifest generation works: the compiler needs to see all workflow files to build
  a complete dependency picture (a tool might be used in one workflow but not
  another). Partial compilation would produce incomplete manifests. In practice,
  this means `gh aw compile --dependabot` is a repository-level operation, not a
  per-workflow operation. Teams in large repositories with many workflows should
  expect a full compile run, not an incremental one. For Ch04: document this as an
  operational constraint — `--dependabot` is a periodic batch operation, not part
  of the per-workflow edit cycle.

### Claim 6: npm lock file generation requires Node.js and npm to be installed locally; pip and Go manifests generate without additional local tooling

- **Evidence**: The page distinguishes between ecosystems by their local tooling
  requirements: Node.js + npm are required for npm lock file generation (because
  `package-lock.json` requires running npm), while pip and Go manifests are generated
  without additional tooling.
- **Confidence**: settled (first-party; the tooling requirement is a stated constraint)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The asymmetry matters for CI environments that run the
  compiler. A CI pipeline running `gh aw compile --dependabot` needs Node.js and
  npm installed if any workflow uses `npx`; pip and Go workflows impose no such
  requirement. For Ch04: document the Node.js/npm prerequisite explicitly in
  any CI setup instructions for Dependabot manifest refresh pipelines.

### Claim 7: Dependabot PRs that only modify compiler-generated manifest files must never be merged — merging them creates files that will be overwritten on the next compilation

- **Evidence**: The page makes this a "Critical Workflow Rule" — the strongest
  advisory language on the page. The technical reason: generated manifest files are
  not source of truth; the workflow markdown files are. Accepting a manifest-only
  PR creates a state that the next compilation will silently overwrite.
- **Confidence**: settled (first-party; described as a Critical Workflow Rule)
- **Quote**: "Never merge Dependabot PRs that only modify manifest files, as they're
  automatically regenerated during compilation."
- **Our assessment**: This is the highest-priority operational rule on the page and
  one of the most counterintuitive — normally, accepting a Dependabot PR is the
  recommended security response. In gh-aw's model, the manifests are derived
  artifacts; accepting a Dependabot PR that only touches them "fixes" the manifest
  without fixing the underlying workflow source. The next compilation regenerates
  the old manifest, undoing Dependabot's update. The rule has a corollary: any
  Dependabot monitoring alert on a gh-aw project is a signal to update the workflow
  source, not to accept the Dependabot PR. For Ch04: this rule should be documented
  prominently in any guide section on Dependabot integration with agentic workflows.
  Teams familiar with standard Dependabot workflows will be confused by this inversion.

### Claim 8: The correct workflow for a Dependabot runtime dependency alert is a four-step source-first process: locate the workflow markdown → update the version → run `gh aw compile --dependabot` → commit (Dependabot auto-closes its PR)

- **Evidence**: The page provides this as the "proper approach" in the Critical
  Workflow Rules section. The four steps are listed sequentially with Dependabot's
  automatic PR closure as the final confirmation signal.
- **Confidence**: settled (first-party; the step sequence is explicitly documented)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The workflow inverts the standard Dependabot interaction: instead
  of reviewing and merging Dependabot's PR, practitioners dismiss it and update the
  source themselves, then let the compiler and Dependabot synchronize. The automatic
  PR closure by Dependabot is the feedback signal confirming the update was applied
  correctly. This is analogous to the `gh aw compile` discipline for action pins
  documented in `docs-ghaw-compilation-process.md` Claim 12 — in both cases, the
  compiler is the authoritative update mechanism, and Dependabot PRs are signals,
  not solutions. For Ch04: provide this four-step sequence as the canonical response
  procedure for Dependabot alerts on gh-aw projects. Teams without this guidance
  will try to merge Dependabot's PR, which is the wrong action.

### Claim 9: Transitive dependencies flagged by Dependabot from MCP server tooling should be resolved by updating the shared MCP configuration, not by editing manifest files directly

- **Evidence**: The page specifies this in a dedicated "Transitive Dependency
  Handling" section — the MCP server case is called out specifically because MCP
  configurations are shared resources, and editing manifests directly would be
  overwritten during recompilation.
- **Confidence**: emerging (stated as guidance but the diversity of MCP server
  configurations means edge cases may exist)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: MCP servers are a new vector for transitive dependencies in
  agentic workflows — the MCP server itself may depend on npm packages, pip packages,
  or Go modules that Dependabot flags. The guidance to update the shared MCP
  configuration (rather than editing the manifest) follows the same source-of-truth
  principle as Claim 7: manifests are derived, not authoritative. For teams using
  shared MCP configurations across multiple workflows, this has an amplifying effect
  — fixing the MCP configuration once updates the Dependabot manifests across all
  workflows that share it. For Ch04: document MCP server dependencies as a separate
  dependency category with their own update path (shared config, not manifest edit).

### Claim 10: The compiler automatically maintains an ignore rule for `github/gh-aw-actions/**` in `.github/dependabot.yml` whenever a `github-actions` update block already exists, while preserving any user-defined entries in that file

- **Evidence**: The "Automatic Ignore Rule Management" section documents this
  behavior. The specificity of the ignore target (`github/gh-aw-actions/**`) and
  the preservation guarantee for user-defined entries are both explicitly stated.
- **Confidence**: settled (first-party; the ignore rule behavior is explicitly
  documented)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This automatic ignore rule is the concrete mechanism described
  at a high level in `docs-ghaw-compilation-process.md` Claim 12 ("gh aw compile
  automatically inserts an ignore rule when a `github-actions` update block exists").
  This reference page provides the exact ignore target — `github/gh-aw-actions/**`
  specifically, not all GitHub Actions — and the conditional: the ignore rule only
  appears when a `github-actions` update block already exists (it does not create
  one from scratch). The preservation guarantee means user-authored Dependabot
  configuration is safe — the compiler is additive, not overwriting. For Ch04: this
  is an important safety property for teams that have existing Dependabot
  configurations — the compiler will not clobber their setup.

## Concrete Artifacts

### `--dependabot` Detection and Manifest Output Matrix

```
Detected Pattern   | Generated Manifests               | Local Tooling Required
-------------------|-----------------------------------|------------------------
npx <package>      | package.json + package-lock.json  | Node.js + npm
pip install <pkg>  | requirements.txt                  | None
go install <pkg>   | go.mod                            | None

All generated ecosystems:
  → Weekly update schedule added to .github/dependabot.yml
  → Standard manifest formats (Dependabot reads them as-is)
```

*Source: `reference/dependabot` — "Key Functionality" section*

### `--dependabot` Usage Constraint

```bash
# CORRECT: compile all workflows with Dependabot manifest generation
gh aw compile --dependabot

# INVALID: cannot target specific files or directories
# gh aw compile --dependabot my-workflow      # not supported
# gh aw compile --dependabot --dir .github    # not supported
```

*Source: `reference/dependabot` — "Important Usage Constraints" section*

### Correct Dependabot Alert Response Workflow

```
When Dependabot opens a PR on a gh-aw project:

1. DO NOT merge the PR if it only modifies generated manifests
   (package.json, package-lock.json, requirements.txt, go.mod)

2. Locate the workflow markdown file(s) that use the flagged tool:
   → Search for `npx <package>`, `pip install <package>`, or `go install <package>`

3. Update the dependency version in the workflow markdown source

4. Regenerate manifests:
   gh aw compile --dependabot

5. Commit the updated workflow markdown + regenerated manifests

→ Result: Dependabot automatically closes its original PR

For MCP server transitive dependencies:
  → Update the shared MCP configuration instead of step 2-3
  → Then run gh aw compile --dependabot to regenerate
```

*Source: `reference/dependabot` — "Critical Workflow Rules" and
"Transitive Dependency Handling" sections*

### Automatic Ignore Rule Behavior

```yaml
# What gh aw compile --dependabot adds to .github/dependabot.yml
# (only when a github-actions update block already exists):

updates:
  - package-ecosystem: "github-actions"
    # ... user-defined entries preserved ...
    ignore:
      - dependency-name: "github/gh-aw-actions/**"
        # managed ignore rule — prevents Dependabot from creating
        # conflicting PRs for gh-aw-managed action references
```

*Source: `reference/dependabot` — "Automatic Ignore Rule Management" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-compilation-process.md` Claim 12 ("Pin updates must come from
    `gh aw compile`, which coordinates pins across all compiled workflows from a
    single release. `gh aw compile` automatically inserts an ignore rule when a
    `github-actions` update block exists."): Claim 10 here provides the concrete
    target of that ignore rule (`github/gh-aw-actions/**`) and confirms the same
    conditional behavior (only when a `github-actions` block exists). Together
    they give the complete picture: Claim 12 covers why the ignore rule exists
    (prevent bypass of compiler-coordinated action pinning); this source gives the
    exact implementation (what the ignore rule targets and what it preserves).
  - `docs-ghaw-how-they-work.md` Claim 7 (the `.md` → `.lock.yml` compilation
    model): the `--dependabot` flag follows the same source-of-truth principle —
    markdown source files drive outputs, not the other way around. The "never merge
    manifest-only PRs" rule (Claim 7 here) is the Dependabot-specific expression
    of the same invariant: compiled/generated artifacts are not authoritative.

- **Extends**:
  - `docs-ghaw-compilation-process.md` Claim 12 (Dependabot + action pinning):
    that claim covers gh-aw's Dependabot strategy for action pins. This source
    reveals a second, distinct Dependabot integration mechanism: runtime tool
    dependency monitoring via manifest generation. Together they describe a
    two-track Dependabot strategy in gh-aw projects — (1) action pins managed by
    the compiler automatically (Claim 12 in compilation-process), (2) runtime tool
    dependencies tracked via generated manifests from `--dependabot` (this source).
    Neither source alone gives the complete picture of how gh-aw projects use
    Dependabot.
  - `docs-ghaw-compilation-process.md` Claim 7 (only frontmatter changes require
    recompilation; markdown body loaded at runtime): the `--dependabot` flag adds a
    third class of compilation trigger — Dependabot manifest refresh. Even if no
    frontmatter changed, manifest regeneration requires `gh aw compile --dependabot`.
    The runtime/compile-time boundary from Claim 7 does not address this periodic
    maintenance operation.
  - `docs-ghaw-how-they-work.md` Claim 11 (the compile → watch → run → review
    development workflow): the `--dependabot` compilation mode is a separate
    maintenance workflow outside the normal development loop — it is not part of
    the per-workflow edit cycle but a periodic repository-level operation.

- **Contradicts**: None. No existing source note makes claims that conflict with
  the `--dependabot` mechanism, the manifest formats, or the update workflow. The
  ignore rule behavior in `docs-ghaw-compilation-process.md` Claim 12 is consistent
  with Claim 10 here — this source adds specificity (the exact ignore target) without
  opposing the existing claim. No contradiction issue required.

- **Novel**:
  - **`gh aw compile --dependabot` as a distinct compilation mode** (Claims 1, 5):
    No existing source note documents this flag. `docs-ghaw-compilation-process.md`
    covers the core `gh aw compile` pipeline but does not mention the `--dependabot`
    flag or its manifest generation behavior.
  - **Runtime tool dependency monitoring via generated manifests** (Claims 1-4):
    The pattern of scanning workflow source for tool invocations and generating
    standard dependency manifests is entirely new to the corpus. This is distinct
    from action pinning (existing notes) — it covers the npm/pip/Go runtime tool
    dependency surface.
  - **"Never merge manifest-only Dependabot PRs" rule** (Claim 7): The specific
    operational rule and its technical rationale (manifests are generated artifacts;
    merging creates state that compilation will overwrite) are new. This is the most
    actionable operational guidance in the source for teams integrating Dependabot
    with gh-aw.
  - **Four-step source-first update workflow** (Claim 8): The canonical procedure
    for responding to Dependabot alerts on gh-aw projects — update source, compile,
    commit, let Dependabot close its PR — is new to the corpus.
  - **MCP server transitive dependency handling** (Claim 9): Identifying MCP server
    tooling as a distinct source of transitive dependencies with its own update path
    (shared config, not manifest edit) is new. No existing note covers MCP server
    dependency management.
  - **All-workflows constraint for `--dependabot`** (Claim 5): The limitation that
    the flag must compile all workflows and cannot be scoped to specific files or
    directories is new operational knowledge.

## Guide Impact

### Chapter 04: System Reliability & Automation / Ops Patterns

- **Add `gh aw compile --dependabot` as the standard mechanism for runtime tool
  dependency monitoring** (Claims 1-4): Teams running agentic workflows that install
  runtime tools via `npx`, `pip install`, or `go install` should run this flag
  periodically to keep Dependabot manifests current. Document the three manifest
  outputs and the standard format advantage (no Dependabot custom configuration).

- **Add the "never merge manifest-only Dependabot PRs" rule as a critical ops
  procedure** (Claim 7): This is high-priority because it inverts the standard
  Dependabot workflow that most teams follow by instinct. Teams without this guidance
  will merge manifest-only PRs, creating transient fixes that compilation reverts.
  Frame it as: "Dependabot PRs on gh-aw projects are signals, not solutions."

- **Document the four-step source-first update workflow** (Claim 8): Provide the
  canonical procedure for teams responding to Dependabot alerts. The automatic PR
  closure by Dependabot is an important feedback signal that confirms the update was
  applied correctly — include it in the procedure description.

- **Document the all-workflows constraint** (Claim 5): Practitioners designing CI
  pipelines for manifest refresh need to know that `--dependabot` is a repository-
  level batch operation. Flag the Node.js/npm prerequisite (Claim 6) for CI
  environments that run this command.

- **Add MCP server transitive dependency handling** (Claim 9): Teams using shared
  MCP configurations need the separate update path (update shared config, not
  manifest). Cross-reference the MCP server configuration guidance in `docs-ghaw-mcps.md`.

### Chapter 02: Harness Engineering

- **Extend the compilation model picture** (Claims 1, 5, 8): `docs-ghaw-compilation-process.md`
  Claim 7 documents the runtime/compile-time boundary for workflow development.
  Add `--dependabot` as a periodic maintenance compilation mode, distinct from
  the development loop. The complete picture of when to run `gh aw compile`:
  (a) frontmatter changes → `gh aw compile`; (b) Dependabot manifest refresh →
  `gh aw compile --dependabot`. These are separate triggers with different scopes.

### Chapter 03: Safety and Verification

- **Extend supply-chain security coverage** (Claims 1, 10): The existing
  `docs-ghaw-compilation-process.md` guidance on action pinning (Claim 6) and the
  ignore rule (Claim 12) covers the action supply-chain. This source adds the
  runtime tool supply-chain (npm packages called via `npx`, etc.). Complete
  supply-chain coverage in gh-aw projects requires both: SHA-pinned actions AND
  Dependabot-monitored runtime tool manifests.

## Extraction Notes

1. **Source is compact and reference-oriented**: The page is a focused reference,
   not a conceptual overview. It covers a single feature (`--dependabot`) with
   approximately five distinct sections. All sections were read fully; seven claims
   plus one operational rule (total ten) were extracted.

2. **WebFetch rendering note**: The gh-aw documentation is an Astro/Starlight SPA.
   WebFetch renders it to markdown. Most content on this page is prose and short
   lists; there do not appear to be complex diagrams or interactive elements that
   would be lost in rendering.

3. **Direct quotes**: The page provided two clear verbatim quotes (the opening
   description and the "must compile all workflows" constraint). All other claims
   are marked with "(no direct quote; see paraphrase in Our assessment)" per
   MINER.md §2a guidance. The WebFetch-rendered content may have paraphrased some
   prose, so extra caution was applied to limit verbatim attribution.

4. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   current gh-aw platform state as of 2026-05-11.

5. **No contradictions filed**: Reviewed all existing source notes, with particular
   attention to `docs-ghaw-compilation-process.md` (most related existing note).
   The ignore rule description here (Claim 10) is consistent with Claim 12 there;
   it adds specificity rather than opposing it. No claims in this source materially
   oppose any existing source note at the MINER.md §4a filing threshold.

6. **Cross-reference verification**: `docs-ghaw-compilation-process.md` Claim 12
   verified by reading the file — it is the 12th `### Claim:` heading in document
   order and its content ("Pin updates must come from `gh aw compile`...") matches
   the citation context. `docs-ghaw-how-they-work.md` Claims 7 and 11 verified
   similarly by position and content in that file.
