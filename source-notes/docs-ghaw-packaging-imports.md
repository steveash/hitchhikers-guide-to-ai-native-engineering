---
source_url: https://github.github.com/gh-aw/guides/packaging-imports
source_type: docs
title: "GitHub Agentic Workflows: Reusing Workflows (Packaging and Imports)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-04-22
last_checked: 2026-04-22
status: current
confidence_overall: emerging
issue: "#298"
---

# GitHub Agentic Workflows: Reusing Workflows (Packaging and Imports)

> The definitive reference for gh-aw's workflow distribution system — documents
> the `imports:` frontmatter field for modular compile-time composition with
> offline-capable SHA-pinned caching, the `gh aw add` / `gh aw update` package
> management lifecycle with 3-way merge semantics, `private: true` as a
> distribution restriction primitive, and agent-assisted import prompts as the
> clearest example of a meta-agent pattern (an AI agent configuring another AI
> agent) in the corpus.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows guides page, "Guides >
  Reusing Workflows" — prescriptive how-to for workflow packaging, imports,
  and distribution. Distinct from the conceptual "How They Work" architecture
  page and the authoring lifecycle guide.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind the Peli de Halleux agent factory blog series and the
  full gh-aw documentation suite. Claims about the `imports:` field schema,
  versioning semantics, `gh aw add/update` CLI behavior, and `private: true`
  frontmatter are authoritative for this platform. Claims about generalizability
  of the modular composition or package-management patterns to other agentic
  systems require additional evidence and are assessed separately.
- **Scope**: Workflow distribution, packaging, and modular composition —
  installation via `gh aw add` / `gh aw add-wizard`, synchronization via
  `gh aw update`, modular import composition via the `imports:` field, version
  pinning strategies, `private:` distribution restriction, and agent-assisted
  import and adaptation prompt templates. Does NOT cover: the core compilation
  model (in `docs-ghaw-how-they-work.md`), the security architecture (same),
  external MCP server configuration (in `docs-ghaw-mcps.md`), or the authoring
  lifecycle beyond distribution (in `docs-ghaw-agentic-authoring.md`). This
  page is the "how to share and reuse workflows"; the authoring page is the
  "how to create and debug them."

## Extracted Claims

### Claim 1: The `imports:` frontmatter field enables modular workflow composition by merging referenced `.md` fragments into the compiled output at compile time

- **Evidence**: The page documents the `imports:` field as listing `.md` file
  paths (relative to workflow location) that are merged into the compiled
  workflow. The example shows a workflow importing three shared fragments:
  `shared/common-tools.md`, `shared/security-setup.md`, and
  `shared/mcp/tavily.md`. The compiler merges them before generating the
  `.lock.yml`, combining permissions (e.g., network permissions) automatically.
- **Confidence**: settled (first-party documentation; the schema and compile
  behavior are explicitly described)
- **Quote**: (from the documented example)
  ```yaml
  ---
  on: issues
  engine: copilot
  imports:
    - shared/common-tools.md
    - shared/security-setup.md
    - shared/mcp/tavily.md
  ---
  ```
- **Our assessment**: The `imports:` field is the structural answer to a problem
  that is otherwise solved by copy-paste: how do multiple workflows share a
  common MCP server configuration or a common permission block without
  duplicating it? `imports:` provides a compile-time include mechanism that
  keeps the editable `.md` source DRY while the compiled `.lock.yml` contains
  the full merged spec. This extends `docs-ghaw-how-they-work.md` Claim 7 (the
  `.md` → `.lock.yml` compilation model) with a dependency-graph dimension —
  the `.md` source can now compose from a tree of fragments, not just be a
  single flat file. For Ch02 (Harness Engineering): `imports:` is the modular
  composition primitive for gh-aw harnesses. Shared MCP configs, common
  permission blocks, and reusable tool definitions can be factored into library
  fragments and imported rather than duplicated.

### Claim 2: Remote imports are pinned to commit SHAs and cached in `.github/aw/imports/` — enabling offline compilation independent of network availability

- **Evidence**: The page states that during `gh aw add`, "import paths expand to
  include source repository tracking" — for example, `shared/common-tools.md`
  becomes `githubnext/agentics/shared/common-tools.md@abc123def`. Remote
  imports are then cached automatically in `.github/aw/imports/` by that
  commit SHA. The cache is shared across git refs pointing to the same commit.
  The documentation calls this "enabling offline compilation."
- **Confidence**: settled (first-party; the SHA-expansion behavior and cache
  location are explicitly documented)
- **Quote**: "Remote imports cache automatically in `.github/aw/imports/` by
  commit SHA, enabling offline compilation."
- **Our assessment**: The SHA-pinning of remote imports at install time is a
  reproducibility guarantee: the import path records exactly which commit was
  resolved, and the `.github/aw/imports/` cache commits those files alongside
  the workflow spec. This means `gh aw compile` does not need a live network
  connection — it can regenerate the `.lock.yml` from the local cache. The
  pattern is analogous to vendoring dependencies in other ecosystems (`vendor/`
  in Go, lockfiles in npm) but applied to natural-language workflow fragments
  rather than code libraries. For Ch02: the `.github/aw/imports/` directory
  should be committed alongside `.md` source and `.lock.yml` artifacts — it
  is part of the harness's reproducibility contract.

### Claim 3: `gh aw add` installs external workflows non-interactively with version pinning via semantic tags, branches, or commit SHAs

- **Evidence**: The documented `gh aw add <workflow-url>@version` syntax supports
  three version specifier formats: semantic tags (`@v1.0.0`), branches
  (`@develop`), and commit SHAs (for immutability). Flags documented include
  `--name` (custom workflow name), `--pr` (open a PR with the installed
  workflow), `--force` (overwrite existing), `--engine` (override engine), and
  `--verbose`. The non-interactive add command supports full short-form
  addressing (`owner/repo/workflow-name`) alongside full GitHub URLs.
- **Confidence**: settled (first-party; CLI syntax and flags are explicitly
  documented)
- **Quote**: `gh aw add <workflow-url>@version`
- **Our assessment**: `gh aw add` is the package-manager analogue for workflow
  distribution — it installs a versioned workflow dependency from a remote
  repository into the local `.github/workflows/` directory. The three-tier
  versioning strategy (semantic tag → branch → SHA) maps directly to the
  three-tier strategy recommended for other dependency managers: use tags for
  stable production installs, branches for development integration, and SHAs
  for auditable, immutable pinning. For Ch02: document the three-tier versioning
  strategy as the recommended discipline for workflow dependencies —
  `@v1.0.0` for stable, `@branch` for development, `@sha` for immutability.

### Claim 4: `gh aw add` auto-writes a `source:` field to the installed workflow's frontmatter, enabling origin tracking and future synchronized updates

- **Evidence**: The documentation states that during installation, the system
  "automatically fetches workflows referenced in the workflow's
  `dispatch-workflow` safe output and files declared in the workflow's
  `resources:` frontmatter field," and that a `source:` tracking entry is
  written to the installed workflow's frontmatter. This `source:` field is
  what enables `gh aw update` to later fetch updates from the correct upstream
  location and version.
- **Confidence**: settled (first-party; the `source:` field auto-write behavior
  is explicitly documented)
- **Quote**: "the system automatically fetches: Workflows referenced in the
  workflow's `dispatch-workflow` safe output; Files declared in the workflow's
  `resources:` frontmatter field"
- **Our assessment**: The `source:` field serves as a provenance chain embedded
  in the workflow file itself. Unlike many package managers where the version
  lock lives in a separate lockfile, gh-aw embeds the origin in the workflow's
  own frontmatter — the workflow knows where it came from and what version it
  is. This self-describing property is useful for audits: a reviewer can read
  the workflow file and immediately know its upstream origin and pin. For Ch03
  (Safety and Verification): the `source:` field is a lightweight provenance
  primitive — it does not prevent supply-chain attacks, but it creates an
  auditable record of origin that a review process can check.

### Claim 5: `gh aw update` synchronizes installed workflows with upstream using 3-way merge by default, preserving local customizations while incorporating upstream changes

- **Evidence**: The documented behavior: `gh aw update` (all workflows), `gh aw
  update ci-doctor` (specific workflow), `gh aw update ci-doctor issue-triage`
  (multiple). "Updates use 3-way merge by default to preserve local
  customizations; `--no-merge` replaces entirely." "Semantic versions update
  within the same major version."
- **Confidence**: settled (first-party; the merge strategy is explicitly
  documented with flag for override)
- **Quote**: "Updates use 3-way merge by default to preserve local
  customizations; `--no-merge` replaces entirely."
- **Our assessment**: The 3-way merge default is the key design choice that
  distinguishes `gh aw update` from a simple file replacement. A 3-way merge
  treats the installed workflow as a fork: it has a common ancestor (the version
  that was installed), a local version (with the team's customizations), and the
  upstream version (the new release). Git-style merge semantics resolve non-
  conflicting changes automatically and flag conflicts for manual resolution —
  the same model used for code merges. This is the correct default for a package
  that is expected to be customized: it updates without clobbering local work.
  `--no-merge` (full replacement) is the right choice when local customizations
  should be discarded — e.g., when upgrading to a major version with breaking
  changes. For Ch02: document the 3-way merge as the recommended update path;
  flag `--no-merge` as appropriate only for major-version upgrades or when
  local customizations are intentionally abandoned.

### Claim 6: Semantic version pinning for workflow dependencies follows the same update semantics as npm/Go modules — major version boundary is a breaking-change contract

- **Evidence**: The documentation states: "Semantic versions update within the
  same major version" during `gh aw update`. This means a workflow installed at
  `@v1.0.0` will receive `v1.1.x` updates via `gh aw update`, but NOT `v2.x.x`
  updates. Breaking changes require an explicit re-install with the new major
  version. Branch refs update to the latest commit on that branch; commit SHA
  pins are immutable and never auto-update.
- **Confidence**: settled (first-party; the major-version boundary semantics are
  explicitly stated)
- **Quote**: "Semantic versions update within the same major version."
- **Our assessment**: The major-version-boundary contract is the semantic
  versioning guarantee that makes `gh aw update` safe to run as a routine
  maintenance operation. Teams can run `gh aw update` on a schedule without
  fear of silent breaking changes — the update will only pick up compatible
  minor and patch releases. This mirrors the npm `^` range semantics (accept
  compatible updates, reject breaking). The practical implication for harness
  engineers: adopt semantic versioning for any workflow intended for distribution
  (`@v1.0.0`, `@v2.0.0` for breaking changes), so consumers can use `gh aw
  update` safely. For Ch02: workflow version authors should treat major version
  increments as a breaking-change signal requiring coordinated consumer updates.

### Claim 7: `private: true` frontmatter prevents a workflow from being installed into other repositories — a distribution-restriction primitive for enterprise governance

- **Evidence**: Directly stated: "Workflows marked with `private: true` in
  their frontmatter cannot be added to other repositories." Attempting `gh aw
  add` on a private workflow fails with an error. The restriction is declared
  at the source (the workflow file's frontmatter) rather than at the repository
  level.
- **Confidence**: settled (first-party; the behavior is explicitly documented)
- **Quote**: "Workflows marked with `private: true` in their frontmatter cannot
  be added to other repositories."
- **Our assessment**: `private: true` is a lightweight access-control primitive
  at the workflow level. It answers a practical governance question: how does
  an organization prevent internal automation workflows (which may encode
  business-sensitive logic or depend on private infrastructure) from being
  copied into external or unauthorized repositories? The frontmatter-level
  restriction keeps the control co-located with the workflow definition rather
  than requiring repository-level permissions. Note the limitation: `private:
  true` prevents `gh aw add`-based distribution but does not prevent manual
  copying of the file content. For Ch05 (Team Adoption): `private: true` is
  the recommended setting for any workflow encoding proprietary business logic,
  internal API credentials via `resources:`, or organizational-specific
  procedures. For Ch03: document as a governance mechanism, not a security
  boundary — it prevents convenient distribution, not determined exfiltration.

### Claim 8: `gh aw add` auto-fetches companion workflows declared in `dispatch-workflow` safe outputs and files listed in `resources:` frontmatter — dependency resolution at install time

- **Evidence**: The page documents that during `gh aw add`, the installer
  automatically fetches: (1) workflows referenced in the installed workflow's
  `dispatch-workflow` safe output, and (2) files declared in the workflow's
  `resources:` frontmatter field. These companion assets are fetched and
  installed alongside the main workflow — the installer resolves the dependency
  tree, not just the single file.
- **Confidence**: settled (first-party; both dependency auto-fetch behaviors are
  explicitly documented)
- **Quote**: (paraphrased from page) "automatically fetches: Workflows
  referenced in the workflow's `dispatch-workflow` safe output; Files declared
  in the workflow's `resources:` frontmatter field"
- **Our assessment**: Auto-fetching companion workflows and `resources:` files
  solves a coordination problem: a workflow author can declare its dependencies
  in the workflow spec, and consumers get a complete installation in one `gh aw
  add` command rather than having to manually identify and install each component.
  This is the `gh aw` equivalent of transitive dependency resolution in a package
  manager. The `dispatch-workflow` and `resources:` auto-fetch are distinct from
  `imports:` (Claim 1): `imports:` are compile-time fragment merges;
  `dispatch-workflow` and `resources:` auto-fetches are install-time file
  retrieval. For Ch02: workflow authors distributing multi-component automation
  suites should declare their companion workflows via `dispatch-workflow` safe
  output and shared files via `resources:` so consumers get the full suite on
  `gh aw add`.

### Claim 9: Agent-assisted import and adaptation is a meta-agent pattern — a coding agent bootstraps a repository, imports a workflow, and adapts it to local conventions in one prompt sequence

- **Evidence**: The page documents templated prompt sequences for GitHub
  Copilot, Claude, Codex, and other coding agents to perform import-and-adapt
  workflows. The documented prompt template:
  ```
  Initialize this repository for GitHub Agentic Workflows using [install URL]
  Then import and adapt the [WORKFLOW_NAME] from [OWNER/REPO]
  Adapt the workflow for this repository: update any labels, assignees,
  branch names, and permissions to match this project's structure.
  ```
  Named example workflows: daily status reports, issue triage, CI doctor.
  Two invocation paths: via GitHub's web UI (non-interactive) or via local
  coding agents (terminal-based, interactive).
- **Confidence**: settled (first-party documentation; prompt templates are
  explicitly provided for production use)
- **Quote**: "Adapt the workflow for this repository: update any labels,
  assignees, branch names, and permissions to match this project's structure."
- **Our assessment**: This is the clearest example of a meta-agent pattern in
  the corpus: a coding agent (Claude, Copilot, Codex) is performing the task
  of configuring another AI agent (the imported gh-aw workflow). The human
  describes the intent; the coding agent fetches the source workflow, reads
  its structure, adapts repository-specific configuration values (labels,
  assignees, branch names, permissions), and commits the result. What is novel
  here is not the agent-assisted configuration itself (which `docs-ghaw-
  agentic-authoring.md` Claim 3 touches) but the specific three-step pattern:
  (1) initialize repo for agentic authoring, (2) import a named workflow from
  upstream, (3) adapt it to the repository's conventions. The coding agent
  acts as an installation and configuration wizard. For Ch01 (Daily Workflows):
  document this as a repeatable workflow for adding agentic automation to a
  new repository — one prompt sequence handles the entire init-import-adapt
  lifecycle. For Ch02: this is an example of harness composition via AI
  assistance — the "harness builder" is itself an AI agent.

### Claim 10: The `imports:` field enables shared MCP configuration fragments to be factored out of individual workflows and reused across the workflow library

- **Evidence**: The Tavily MCP configuration is documented as a canonical
  example of a shared `imports:` fragment. The file
  `.github/workflows/shared/mcp/tavily.md` contains only a frontmatter block:
  ```yaml
  ---
  mcp-servers:
    tavily:
      url: "https://mcp.tavily.com/mcp/?tavilyApiKey=${{ secrets.TAVILY_API_KEY }}"
      allowed: ["*"]
  network:
    allowed:
      - mcp.tavily.com
  ---
  ```
  Workflows that need Tavily include `shared/mcp/tavily.md` in their `imports:`
  list. The compiler merges the MCP server declaration and network permission
  automatically.
- **Confidence**: settled (first-party; the Tavily example is explicitly
  documented as the canonical shared config pattern)
- **Quote**: (from Tavily example in documentation — see Concrete Artifacts)
- **Our assessment**: The `imports:` mechanism combined with shared MCP
  fragments creates a two-level factoring: (1) `imports:` for compile-time
  fragment composition within a workflow; (2) the shared MCP library (in
  `.github/workflows/shared/mcp/`) as the library of pre-built fragments.
  This directly connects to `docs-ghaw-mcps.md` Claim 9, which documents the
  17 pre-built shared MCP configurations in that library — `imports:` is the
  mechanism by which those configs are consumed. Together, the two sources give
  a complete picture: the shared library provides the building blocks; `imports:`
  is how you assemble them into a workflow. For Ch02: the pattern of factoring
  MCP configurations into `.md` fragments and including them via `imports:`
  reduces duplication and keeps the per-workflow spec focused on task logic.
  This is analogous to importing a library in code rather than copy-pasting its
  implementation.

### Claim 11: Three remote import specification formats are supported — short-form, explicit-path, and URL-based — all pinnable to a semantic tag, branch, or commit SHA

- **Evidence**: The page documents the specification formats:
  - Short-form: `owner/repo/workflow-name` (auto-adds `workflows/` prefix,
    for top-level `.github/workflows/` files)
  - Explicit path: `owner/repo/path/to/file.md` (requires explicit `.md`
    suffix for non-top-level paths)
  - URL-based: full `https://github.com/...` or `https://raw.githubusercontent.com/...`
  - Version suffix: `@v1.0.0`, `@branch-name`, or `@commitsha` appended to any format
  - Agent file imports: `owner/repo/.github/agents/agent-name.md[@version]`
    for agent instruction files
- **Confidence**: settled (first-party; path format rules are explicitly specified)
- **Quote**: "Remote import path: `owner/repo/path.md[@version]`. Explicit
  `.md` suffix required for non-top-level paths."
- **Our assessment**: The three-format specification with consistent version
  suffix semantics provides a uniform addressing scheme for any importable
  gh-aw artifact regardless of host or path structure. The agent file import
  format (`.github/agents/`) is worth noting separately: it enables workflows
  to import not just tool configurations but agent instruction files — the
  instructions that define a companion agent's behavior. This opens a
  composition pattern: a workflow can import both an MCP config fragment
  (Claim 10) AND the agent instruction file that knows how to use it. For
  Ch02: document the explicit `.md` suffix requirement for non-top-level paths
  as a common source of configuration errors.

## Concrete Artifacts

### `imports:` Frontmatter Field — Basic Usage

```yaml
---
on: issues
engine: copilot
imports:
  - shared/common-tools.md
  - shared/security-setup.md
  - shared/mcp/tavily.md
---

## Task
When a new issue is opened, analyze and triage it...
```

*Source: docs-ghaw-packaging-imports, "Imports Field" section — illustrative
example showing three shared fragments imported before the workflow body.*

### Shared MCP Configuration Fragment — Tavily Example

```yaml
# .github/workflows/shared/mcp/tavily.md
---
mcp-servers:
  tavily:
    url: "https://mcp.tavily.com/mcp/?tavilyApiKey=${{ secrets.TAVILY_API_KEY }}"
    allowed: ["*"]
network:
  allowed:
    - mcp.tavily.com
---
```

*Source: docs-ghaw-packaging-imports, "Imports Field" section — canonical
example of a shared MCP config fragment reused via `imports:`.*

### `gh aw add` and `gh aw update` CLI Lifecycle

```bash
# Install a workflow — non-interactive, version-pinned
gh aw add owner/repo/workflow-name@v1.0.0
gh aw add owner/repo/workflow-name@develop        # track branch
gh aw add owner/repo/workflow-name@abc123def      # pin to commit SHA

# Install with customizations
gh aw add owner/repo/workflow-name@v1.0.0 --name my-custom-name
gh aw add owner/repo/workflow-name@v1.0.0 --pr    # open PR with install
gh aw add owner/repo/workflow-name@v1.0.0 --engine claude

# Interactive wizard (prompts for configuration)
gh aw add-wizard owner/repo/workflow-name@v1.0.0
gh aw add-wizard owner/repo/workflow-name --skip-secret  # skip org-level secrets

# Update installed workflows
gh aw update                          # update all workflows
gh aw update ci-doctor                # update specific workflow
gh aw update ci-doctor issue-triage   # update multiple
gh aw update ci-doctor --no-merge     # replace entirely (no 3-way merge)
```

*Source: docs-ghaw-packaging-imports, "Adding Workflows" and "Updating
Workflows" sections.*

### Remote Import Specification Formats

```
Short-form (top-level workflow):
  owner/repo/workflow-name               # auto-adds workflows/ prefix

Explicit path (any location, .md suffix required):
  owner/repo/path/to/file.md

URL formats (both supported):
  https://github.com/owner/repo/blob/main/path/file.md
  https://raw.githubusercontent.com/owner/repo/main/path/file.md

Agent file imports:
  owner/repo/.github/agents/agent-name.md

Version suffix (appended to any format):
  @v1.0.0     — semantic tag (stable)
  @develop    — branch ref (tracks latest)
  @abc123def  — commit SHA (immutable)

After gh aw add, local import path expands to fully-qualified form:
  shared/mcp/tavily.md  →  githubnext/agentics/shared/mcp/tavily.md@abc123def

Cache location: .github/aw/imports/<sha>/
  Committed to repository; enables offline compilation
  Shared across refs pointing to same commit
```

*Source: docs-ghaw-packaging-imports, "Specification Formats" section.*

### Agent-Assisted Import and Adaptation — Prompt Template

```
Initialize this repository for GitHub Agentic Workflows using [install URL]
Then import and adapt the [WORKFLOW_NAME] from [OWNER/REPO]
Adapt the workflow for this repository: update any labels, assignees,
branch names, and permissions to match this project's structure.
```

Named example workflows for this pattern:
- Daily Status Reports
- Issue Triage
- CI Doctor

Invocation paths:
- GitHub Web UI (non-interactive, via GitHub Copilot)
- Local coding agent (terminal-based: VSCode, Claude Code, Codex, Copilot)

*Source: docs-ghaw-packaging-imports, "Using Agents to Import and Adapt" section.*

### Version Pinning Strategy (3-tier)

```
Tier 1: Semantic tag — @v1.0.0
  Use for: stable production installs
  Update behavior: gh aw update picks up compatible minor/patch within major
  Breaking changes: require explicit re-install at @v2.0.0

Tier 2: Branch ref — @develop / @main
  Use for: development integration, tracking fast-moving upstream
  Update behavior: gh aw update fetches latest commit on branch

Tier 3: Commit SHA — @abc123def
  Use for: immutable, auditable pins (security-sensitive workflows)
  Update behavior: never auto-updates; manual re-install required

Best practice recommendation (from docs):
  - Stable workflows → semantic versioning (@v1.0.0)
  - Development → branches (@develop)
  - Immutability required → commit SHA
```

*Source: docs-ghaw-packaging-imports, "Best Practices" section.*

## Cross-References

- **Corroborates**:
  - `blog-gh-aw-operations-release-workflows.md` Claim 4 (`gh aw add-wizard` +
    `gh aw compile` as a workflow delivery mechanism): that source documents
    `gh aw add-wizard` as an installation step from a practitioner blog post;
    this source is the canonical documentation for the full distribution system
    (`gh aw add`, `gh aw add-wizard`, `gh aw update`). Both establish the
    same package-manager-style workflow distribution model; this page is the
    primary reference.
  - `docs-ghaw-agentic-authoring.md` Claim 3 (fork via `create-agentic-agent`
    vs. synchronization via `gh aw add`): that note documents the high-level
    distinction; this page provides the full mechanics of the synchronization
    path (`gh aw add` + `gh aw update` + `source:` tracking + 3-way merge).
    Together they give the complete workflow reuse picture: fork (one-time
    migration, diverges from upstream) vs. sync (ongoing dependency, tracks
    upstream within major version).
  - `docs-ghaw-mcps.md` Claim 9 (17 pre-built shared MCP configurations in
    `.github/workflows/shared/mcp/`): that note documents the existence of the
    shared MCP library; this page documents the mechanism — `imports:` — by
    which those configs are included in workflows. Together they give the full
    shared-MCP-config picture: the library is in `shared/mcp/`; `imports:`
    is how you use it.

- **Extends**:
  - `docs-ghaw-how-they-work.md` Claim 7 (`.md` → `.lock.yml` compilation
    model): this page adds a dependency-graph dimension to the compilation model.
    Previously, the compilation model was single-file (one `.md` compiles to one
    `.lock.yml`). With `imports:`, the compilation model is a tree: the root
    `.md` imports one or more fragment `.md` files, and the compiler merges them
    before generating the lock file. The `imports:` expansion + SHA-pinning step
    (Claim 2) is a new stage in the compilation pipeline not documented in
    `docs-ghaw-how-they-work.md`.
  - `docs-ghaw-how-they-work.md` Claim 6 (MCP Scripts as inline custom tools):
    that note covers inline MCP tool definitions within a single workflow's
    frontmatter. This note adds the complementary distribution mechanism:
    factoring MCP configs into shared `.md` fragments and importing them via
    `imports:`. The two together give the three-tier MCP integration spectrum
    for gh-aw: (a) inline MCP Script (single workflow, no sharing), (b) shared
    `imports:` fragment (multiple workflows in same repo), (c) external MCP
    server (`docs-ghaw-mcps.md` — persistent service, shared across all
    workflows and repos).
  - `docs-ghaw-agentic-authoring.md` Claim 9 (agent-assisted debugging as a
    meta-agent pattern): this note adds agent-assisted import-and-adapt (Claim
    9) as a parallel meta-agent pattern for workflow distribution. Both are
    examples of a coding agent performing lifecycle management tasks for another
    AI agent: debugging (agentic-authoring) and configuration onboarding
    (packaging-imports).
  - `docs-ghaw-agentic-authoring.md` Claims 6 and 7 (URL-addressable
    self-contained prompt pattern): the agent-assisted import prompts (Claim 9)
    follow the same pattern. The install URL in the template
    ("Initialize this repository using [install URL]") is the `install.md`
    URL-addressable prompt. `imports:` fragments are themselves URL-addressable
    at the short-form `owner/repo/path.md@version` address.

- **Contradicts**: None identified. No existing source note makes claims that
  contradict the `imports:` modular composition model, `gh aw add/update`
  versioning semantics, `private: true` restriction, or 3-way merge default.
  The version-pinning strategy here is consistent with the version-pinned
  `add-wizard` URL documented in `blog-gh-aw-operations-release-workflows.md`
  Claim 4 (`@v0.45.5`). The fork vs. sync distinction here is consistent with
  `docs-ghaw-agentic-authoring.md` Claim 3.

- **Novel**:
  - **`imports:` as a modular composition mechanism** (Claim 1): No existing
    source note documents the `imports:` frontmatter field or compile-time
    fragment merging. This is the first coverage of modular workflow composition
    in the corpus.
  - **Remote import SHA-pinning and `.github/aw/imports/` caching** (Claim 2):
    The offline compilation guarantee via SHA-pinned, committed import cache
    is new to the corpus. No existing note documents this caching mechanism.
  - **3-way merge semantics for `gh aw update`** (Claim 5): The specific merge
    strategy (3-way by default, `--no-merge` for full replacement) is not
    documented in any existing source note. `docs-ghaw-agentic-authoring.md`
    Claim 3 mentions `gh aw add` for synchronized reuse but does not describe
    the update merge semantics.
  - **`source:` field auto-tracking** (Claim 4): The auto-written `source:`
    frontmatter field as a provenance primitive is new to the corpus.
  - **`private: true` as a distribution restriction primitive** (Claim 7):
    No existing source note documents `private: true` or workflow-level
    distribution governance. This is the first coverage of workflow access
    control in the corpus.
  - **Meta-agent import-and-adapt pattern with prompt templates** (Claim 9):
    While `docs-ghaw-agentic-authoring.md` Claim 3 mentions the general
    distinction between fork (`create-agentic-agent`) and sync (`gh aw add`),
    it does not document the specific three-step init-import-adapt prompt
    template. These templates are the most concrete "agents configuring agents"
    artifact in the corpus.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add `imports:` as the modular composition primitive for gh-aw harnesses**
  (Claim 1): Currently the guide covers the single-file `.md` → `.lock.yml`
  compilation model. Add the `imports:` dimension: multiple `.md` fragments can
  be composed into one compiled workflow. Introduce the pattern of factoring
  shared MCP configs, permission blocks, and tool definitions into library
  fragments under `shared/`. Cross-reference with `docs-ghaw-mcps.md` Claim 9
  for the pre-built shared MCP library.

- **Document the `.github/aw/imports/` cache as part of the harness reproducibility
  contract** (Claim 2): Practitioners committing gh-aw workflows should commit
  the `imports/` cache alongside `.md` source and `.lock.yml` artifacts. Explain
  why: it is the offline compilation guarantee and the SHA-pinning record for
  all imported fragments.

- **Add the `gh aw add` → `gh aw update` package management lifecycle** (Claims
  3–6): The guide currently documents `gh aw compile` and the basic CLI but does
  not cover workflow dependencies as a package-management concern. Add: (a) how
  to install a versioned workflow dependency via `gh aw add @version`; (b) the
  three-tier versioning strategy (tag → branch → SHA); (c) `gh aw update` with
  3-way merge semantics for routine maintenance; (d) `source:` field as provenance.
  This closes the lifecycle gap between "install a workflow once" and "maintain it
  as a dependency."

- **Name the meta-agent import-and-adapt pattern** (Claim 9): The three-step
  prompt sequence (init → import → adapt) is a reusable onboarding workflow for
  adding agentic automation to a new repository. Document it as a pattern: a
  coding agent performs the entire harness installation and local customization in
  one session. This is the fastest path from "empty repository" to "configured
  agentic workflow."

### Chapter 03: Safety and Verification

- **Add `private: true` as a governance mechanism** (Claim 7): Workflows
  encoding proprietary business logic, internal API credentials, or
  organizational-specific procedures should use `private: true` to prevent
  convenient distribution. Document as a governance mechanism (not a security
  boundary — it prevents `gh aw add` distribution but not manual copying). Pair
  with the `source:` field (Claim 4) for provenance and the OIDC auth pattern
  from `docs-ghaw-mcps.md` Claim 4 for credential management.

- **Add `source:` field to the provenance audit checklist** (Claim 4): When
  reviewing an installed workflow, the `source:` field in the frontmatter
  provides the upstream origin and version. Add this to any harness security
  review checklist — a workflow without a `source:` field is either authored
  locally (expected for custom workflows) or was manually installed without
  version tracking (flag for review).

### Chapter 05: Team Adoption

- **Add `private: true` to enterprise workflow distribution governance** (Claim
  7): Organizations deploying shared workflow libraries should establish a policy
  for which workflows are distributable (`private: false` or absent) vs.
  internal-only (`private: true`). The `private:` frontmatter field is the
  enforcement mechanism.

- **Document the meta-agent import pattern as a team onboarding tool** (Claim
  9): When a team wants to add agentic automation to a repository, the
  agent-assisted import prompts provide a low-friction, conversational onboarding
  path. No gh-aw expertise required: the coding agent handles initialization,
  import, and local adaptation. This reduces the barrier to adoption for teams
  that are not yet comfortable with the gh-aw CLI.

### Chapter 01: Daily Workflows

- **Add the three-step init-import-adapt prompt sequence as a daily workflow for
  agentic automation onboarding** (Claim 9): When adding a new workflow to a
  repository, the standard sequence is: (1) prompt a coding agent to initialize
  the repository for gh-aw; (2) instruct it to import the named workflow from
  the source repository; (3) instruct it to adapt the workflow to local
  conventions (labels, assignees, branch names, permissions). This is a
  repeatable, low-overhead workflow for growing an agent factory incrementally.

## Extraction Notes

1. **Source rendered via Astro/Starlight SPA**: WebFetch returns the rendered
   text. Some interactive content (tabs, expandable sections) may not have been
   fully captured. The `imports:` examples, CLI syntax, and specification format
   table were extracted from the rendered text and are assessed as accurate based
   on consistency with documented patterns in adjacent gh-aw notes. Minor YAML
   formatting variations are possible.

2. **Three Prospector triage comments for this issue**: Issue #298 has three
   `claude`-authored triage comments, each offering slightly different extraction
   guidance. The third comment (most detailed) identifies the `imports:` modular
   composition pattern, `gh aw add/update` package lifecycle, 3-way merge
   semantics, and agent-assisted bootstrap prompts as the key extraction targets.
   All three comments converge on these themes. This note prioritizes those four
   themes while also capturing `private: true`, `source:` tracking, and companion
   workflow auto-fetch as secondary findings.

3. **Agent-assisted adaptation overlaps with `docs-ghaw-agentic-authoring.md`**:
   The agentic authoring guide (issue #293, Claim 3) documents the conceptual
   distinction between `create-agentic-agent` (fork/migrate) and `gh aw add`
   (sync). This note focuses on the `gh aw add` path's mechanics and the specific
   import-and-adapt prompt templates, which are not covered in that note. No
   duplication; the two are complementary.

4. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   the current gh-aw platform state as of 2026-04-22.

5. **No contradictions to file**: Reviewed all existing source notes, open
   `contradiction`-labeled issues, and CONTRADICTIONS.md. No claims in this
   source materially oppose existing source notes. The `imports:` field, `source:`
   field, `private: true`, and 3-way merge semantics are all new additions to the
   corpus without opposing claims.

6. **Registry/sources.json**: The `registry/sources.json` file contains an
   empty/minimal schema (`{"sources": {}, "last_updated": null}`). Per extraction
   guidelines, no entry was added to avoid inventing a schema.
