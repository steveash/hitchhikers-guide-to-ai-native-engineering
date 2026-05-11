---
source_url: https://github.github.com/gh-aw/reference/dependencies
source_type: docs
title: "GitHub Agentic Workflows: APM Dependencies Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#380"
---

# GitHub Agentic Workflows: APM Dependencies Reference

> The authoritative reference for APM (Agent Package Manager) in gh-aw —
> documents the package manager for AI agent primitives (skills, prompts,
> instructions, agents, hooks, plugins), the `shared/apm.md` vendoring
> pattern, the `apm.lock` SHA-pinning governance contract, three package
> reference formats, cascading token fallback for authentication, and the
> explicit deprecation of the `dependencies:` frontmatter field in favor of
> the import-based approach.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/dependencies`
  page — in the "Reference" section, not the conceptual `introduction/` or
  `guides/` sections. This is the prescriptive configuration reference for
  APM, not a conceptual overview or blog post. Listed as "APM Dependencies"
  in the navigation; adjacent to "Imports" and "Imports - Copilot Agent
  Files" in the reference section.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind the Peli de Halleux agent factory blog series and the
  broader gh-aw documentation suite. APM itself is a Microsoft project
  (`microsoft/apm`, `microsoft/apm-action`). Claims about frontmatter fields,
  package formats, lock file behavior, and token authentication are
  authoritative for this platform. The page explicitly notes the platform
  "may change" — CLI flags and input names are `emerging`; SHA-pinning
  semantics and lock file governance are `settled`.
- **Scope**: APM configuration for gh-aw — what APM manages, how to configure
  it via `shared/apm.md`, package reference formats, lock file semantics,
  token authentication, and the `apm pack`/`apm unpack` local tooling.
  Also documents the explicit deprecation of the `dependencies:` frontmatter
  field and the `dependencies:` input on `microsoft/apm-action`. Does NOT
  cover: the full APM documentation at `microsoft.github.io/apm/` (a
  separate site), general workflow imports (see issue #298), or the
  compilation model conceptually (see `docs-ghaw-how-they-work.md` and
  `docs-ghaw-compilation-process.md`).

## Extracted Claims

### Claim 1: APM manages AI agent primitives — skills, prompts, instructions, agents, hooks, and plugins including the Claude `plugin.json` specification — as installable packages

- **Evidence**: The page opens with an explicit definition of APM's scope:
  "APM (Agent Package Manager) manages AI agent primitives such as skills,
  prompts, instructions, agents, hooks, and plugins (including the Claude
  `plugin.json` specification)." Packages handle dependency resolution
  through a complete dependency tree.
- **Confidence**: settled (first-party definition; the primitive types are
  explicitly enumerated)
- **Quote**: "APM (Agent Package Manager) manages AI agent primitives such as
  skills, prompts, instructions, agents, hooks, and plugins (including the
  Claude `plugin.json` specification)."
- **Our assessment**: The explicit inclusion of Claude `plugin.json` is
  significant — it means APM is model-aware at the package level, not
  just tool-aware. A package can bundle Claude-specific plugins alongside
  generic skills and prompts, enabling teams to distribute entire
  agent configurations (not just reusable code modules) as versioned APM
  packages. This is a higher-level abstraction than individual MCP tools
  (from `docs-ghaw-mcps.md`) — APM packages can contain multiple MCP tools,
  prompt templates, and agent configurations in a single installable unit.
  For Ch05 (Tool Integration): APM is the distribution layer above MCP
  configuration — teams that have built domain-specific skills should
  publish them as APM packages so other workflows can install them.

### Claim 2: The `dependencies:` frontmatter field is deprecated and no longer supported — teams must migrate to the import-based approach

- **Evidence**: The page contains an explicit deprecation notice:
  "The `dependencies:` frontmatter field is deprecated and no longer
  supported. Migrate to the import-based approach shown below." A second
  deprecation notice follows: "Note: The `dependencies:` input on the
  underlying `microsoft/apm-action` (used inside `shared/apm.md`) is also
  deprecated in favour of the `packages:` and `apps:` inputs."
- **Confidence**: settled (explicit deprecation notice; "no longer supported"
  is a hard statement, not a soft recommendation)
- **Quote**: "The `dependencies:` frontmatter field is deprecated and no longer
  supported. Migrate to the import-based approach shown below."
- **Our assessment**: This is an actionable breaking-change notice. Any
  existing gh-aw workflow using the `dependencies:` frontmatter field is
  broken or will break; the migration path is to replace it with the
  `shared/apm.md` import pattern documented in Claims 3-4. Similarly,
  any workflow calling `microsoft/apm-action` directly with a `dependencies:`
  input must migrate to `packages:` and `apps:` inputs. This deprecation
  has a direct guide impact: Ch02 (Harness Engineering) must not document
  `dependencies:` as a valid configuration option, and any existing guide
  content citing it should be updated. For practitioners maintaining existing
  gh-aw installations: audit workflows for `dependencies:` frontmatter
  fields and `apm-action` `dependencies:` inputs; migrate before they stop
  working.

### Claim 3: APM is configured by importing `shared/apm.md`, which adds a dedicated `apm` job to the compiled workflow that packs packages and uploads the bundle as a GitHub Actions artifact

- **Evidence**: The page states: "APM is configured by importing the
  `shared/apm.md` workflow, which creates a dedicated `apm` job that packs
  packages and uploads the bundle as a GitHub Actions artifact." The agent
  job downloads and restores the bundle as pre-steps, making all skills and
  tools available at runtime.
- **Confidence**: settled (first-party; the job architecture is explicitly
  described)
- **Quote**: (no single direct quote covers the full mechanism; see Concrete
  Artifacts for the usage example; paraphrase above is from source)
- **Our assessment**: The `apm` job as a separate dedicated job (not inline
  steps) means APM follows the same job-level isolation architecture as
  Safe Outputs and detection jobs documented in
  `docs-ghaw-compilation-process.md` Claim 3. The agent job depends on
  the `apm` job completing and uploading the artifact before it can
  restore the bundle and execute. This is the same artifact-based handoff
  pattern used throughout gh-aw: separate jobs communicate via GitHub
  Actions artifacts, not in-process IPC. For Ch02: when APM is configured,
  the compiled `.lock.yml` gains an `apm` job in its dependency graph —
  practitioners should account for this job's runtime in cost and execution
  time estimates.

### Claim 4: `shared/apm.md` is a local workflow file (not a remote import) that must be vendored into `.github/workflows/shared/` via `gh aw add`

- **Evidence**: The page states explicitly: "`shared/apm.md` is a **local
  workflow file** that gh-aw resolves at `.github/workflows/shared/apm.md`
  in your repository — it is not a remote import." Installation uses the
  command `gh aw add microsoft/apm/.github/workflows/shared/apm.md --dir
  shared`. The canonical source is at
  `github.com/microsoft/apm/blob/main/.github/workflows/shared/apm.md`.
- **Confidence**: settled (first-party; the vendoring requirement is stated
  explicitly as a design property)
- **Quote**: "`shared/apm.md` is a **local workflow file** that gh-aw resolves
  at `.github/workflows/shared/apm.md` in your repository — it is not a
  remote import."
- **Our assessment**: The local-not-remote distinction matters for several
  reasons: (1) it means the file must be explicitly committed to the
  repository — it does not benefit from gh-aw's remote import caching
  (`.github/aw/imports/` from `docs-ghaw-sharing-workflows.md` Claim 5);
  (2) the `--dir shared` flag places it under `shared/` as a vendored local
  convention consistent with the shared MCP configuration library pattern
  (`docs-ghaw-mcps.md` Claim 9); (3) it means the vendored copy must be
  kept up-to-date explicitly via `gh aw update`. The `redirect` mechanism
  (Claim 5) automates this update path. For Ch02: when setting up APM,
  `gh aw add microsoft/apm/.github/workflows/shared/apm.md --dir shared`
  is a mandatory setup step, not an optional optimization.

### Claim 5: The vendored `shared/apm.md` file declares a `redirect` to `microsoft/apm`, enabling `gh aw update` to automatically follow redirects and keep the vendored copy synchronized

- **Evidence**: The page states: "Running `gh aw update` keeps vendored
  copies synchronized. The file declares a `redirect` to the `microsoft/apm`
  library, automatically following redirects on updates."
- **Confidence**: settled (first-party; the redirect mechanism and `gh aw
  update` behavior are explicitly described)
- **Quote**: (no direct quote; see paraphrase above)
- **Our assessment**: The `redirect` declaration in `shared/apm.md` is the
  same tracking mechanism as the `source:` frontmatter field in
  `gh aw add`-installed workflows (from `docs-ghaw-sharing-workflows.md`
  Claim 1). The file knows where it came from, so `gh aw update` can
  retrieve the latest version without the practitioner specifying the origin
  URL again. This connects the APM vendoring pattern to the broader gh-aw
  update lifecycle: both shared workflow templates and APM's `shared/apm.md`
  are kept synchronized via the same `gh aw update` command and redirect/
  source tracking mechanism. For Ch02: `gh aw update` is the single command
  for keeping all vendored workflow components current — both shared workflow
  templates (via `source:`) and the APM shared workflow (via `redirect:`).

### Claim 6: The canonical `shared/apm.md` pins `microsoft/apm-action@v1.5.0` and supports multi-org GitHub App authentication and multi-bundle restore

- **Evidence**: The page states the canonical version "pins
  `microsoft/apm-action@v1.5.0` with support for multi-org GitHub App
  authentication and multi-bundle restore."
- **Confidence**: emerging (first-party; the specific version pin will become
  stale as the APM project evolves)
- **Quote**: (no direct quote; see paraphrase above)
- **Our assessment**: The version pin (`@v1.5.0`) at the time of extraction
  is relevant context but will change. The more durable architectural points
  are: (1) multi-org GitHub App authentication — meaning APM packages can
  span organizational boundaries with appropriate app credentials; (2) multi-
  bundle restore — meaning a single workflow can install packages from
  multiple APM bundles. Both features are relevant for enterprise gh-aw
  deployments where agent skills and plugins are maintained in separate
  organizational repositories. For Ch05: multi-org APM support means
  platform teams can distribute APM packages across org boundaries, not
  just within a single GitHub organization.

### Claim 7: Three package reference formats allow full packages, individual primitives, and version-pinned references within a single `packages:` block

- **Evidence**: The page documents a table with three reference formats and
  provides code examples demonstrating all three in a single `packages:`
  block: `microsoft/apm-sample-package` (full package), `github/awesome-
  copilot/skills/review-and-refactor` (individual primitive skill),
  `microsoft/apm-sample-package#v2.0` (version-pinned to tag),
  `microsoft/apm-sample-package#main` (version-pinned to branch).
- **Confidence**: settled (first-party; schema is explicit in both a table
  and code examples)
- **Quote**: (no direct quote; see Concrete Artifacts section for the
  reference format table and code examples)
- **Our assessment**: The three-format system mirrors the versioning
  strategy documented in `docs-ghaw-sharing-workflows.md` Claim 2 for
  workflow distribution (`@v1.2.0`, `@v1`, `@develop`, `@sha`). APM uses
  a `#ref` suffix instead of `@ref`, but the semantic taxonomy is
  identical: full-package references (coarse-grained), individual primitive
  paths (fine-grained), and version pins (stability control). The
  individual-primitive format (`owner/repo/path/to/primitive`) is
  particularly valuable for consuming only the specific skills a workflow
  needs, without pulling in an entire package. For Ch05: recommend using
  individual primitive paths for production workflows (minimal surface area)
  and full packages only during initial exploration or when most of the
  package content is needed.

### Claim 8: `apm.lock` pins every installed package to an exact commit SHA, providing reproducible runs and a PR-reviewable governance audit trail

- **Evidence**: The page states: "APM lock files (`apm.lock`) pin every
  package to an exact commit SHA, so the same versions are installed on
  every run." Additionally: "Lock file diffs appear in pull requests for
  review before merge, providing audit trails and governance of agent
  context." The APM governance guide at
  `microsoft.github.io/apm/enterprise/governance/` covers policy
  enforcement and access controls.
- **Confidence**: settled (first-party; SHA-pinning is the stated design
  property, not a recommendation)
- **Quote**: "APM lock files (`apm.lock`) pin every package to an exact
  commit SHA, so the same versions are installed on every run."
- **Our assessment**: The `apm.lock` file is APM's equivalent of
  `yarn.lock`, `go.sum`, or the `.lock.yml` workflow import SHAs documented
  in `docs-ghaw-sharing-workflows.md` Claim 5. The PR-reviewable lock file
  diff is the governance mechanism — when a package is updated, the SHA
  change appears in a PR where humans can inspect what changed in the agent's
  context before the change takes effect in production. This is significant
  for teams that need to audit what instructions and capabilities their AI
  agents have access to. For Ch03 (Safety and Verification): `apm.lock`
  should be committed to the repository and treated as a security artifact.
  Package updates that change agent capabilities require explicit PR review
  of the lock file diff.

### Claim 9: Packages are fetched using a cascading token fallback: `GH_AW_PLUGINS_TOKEN` → `GH_AW_GITHUB_TOKEN` → `GITHUB_TOKEN`

- **Evidence**: The page states verbatim: "Packages are fetched using the
  cascading token fallback: `GH_AW_PLUGINS_TOKEN` → `GH_AW_GITHUB_TOKEN`
  → `GITHUB_TOKEN`."
- **Confidence**: settled (first-party; the token fallback order is
  explicitly specified)
- **Quote**: "Packages are fetched using the cascading token fallback:
  `GH_AW_PLUGINS_TOKEN` → `GH_AW_GITHUB_TOKEN` → `GITHUB_TOKEN`."
- **Our assessment**: The cascading fallback enables graduated authentication
  for packages from different access levels: `GH_AW_PLUGINS_TOKEN` is a
  dedicated token for plugin fetching (highest specificity, can be
  scoped narrowly); `GH_AW_GITHUB_TOKEN` is the general gh-aw GitHub token;
  `GITHUB_TOKEN` is the repository's standard Actions token (most general,
  fewest permissions). Practitioners distributing packages from private or
  internal repositories must ensure the appropriate token is configured —
  `GITHUB_TOKEN` alone will not suffice for cross-org or private-repo
  packages. For Ch02: document the three-token hierarchy when configuring
  APM in enterprise environments. Private package repositories require
  `GH_AW_PLUGINS_TOKEN` to be set as a secret with appropriate cross-org
  read permissions.

### Claim 10: Local reproduction of APM operations uses `apm pack` and `apm unpack` directly, enabling offline debugging without running a full workflow

- **Evidence**: The page notes: "To reproduce or debug locally, run `apm
  pack` and `apm unpack` directly." The page links to the pack and distribute
  guide at `microsoft.github.io/apm/guides/pack-distribute/` for
  instructions.
- **Confidence**: settled (first-party; commands are explicitly named)
- **Quote**: (no direct quote; paraphrase above)
- **Our assessment**: The `apm pack` / `apm unpack` commands close the
  local development loop for APM-based workflows. Without these commands,
  debugging APM configuration issues would require running the full
  GitHub Actions workflow — slow and expensive. With them, practitioners
  can test package installation, inspect bundle contents, and validate that
  the correct primitive versions are being pulled before committing to a
  PR. This is analogous to the `gh aw compile --no-emit` flag from
  `docs-ghaw-compilation-process.md` Claim 11 — a local validation step
  that catches configuration errors without producing side effects.

## Concrete Artifacts

### APM Usage — Import and Package Declaration

```yaml
# Import the shared/apm.md workflow to enable APM
imports:
  - uses: shared/apm.md
    with:
      packages:
        # Full APM package
        - microsoft/apm-sample-package
        # Individual primitive (skill) from any repository
        - github/awesome-copilot/skills/review-and-refactor
        # Claude plugin.json from a specific repo
        - github/awesome-copilot/plugins/context-engineering
        # Version-pinned to a tag
        - microsoft/apm-sample-package#v2.0
        # Version-pinned to a branch
        - microsoft/apm-sample-package#main
        # Anthropic skills package
        - anthropics/skills/skills/frontend-design
```

*Source: APM Dependencies reference page, "Usage" section*

### Package Reference Format Table

```
Format                          | Description
--------------------------------|------------------------------------------
owner/repo                      | Full APM package (all primitives in repo)
owner/repo/path/to/primitive    | Individual primitive (skill, instruction,
                                | plugin, etc.) from any repository
owner/repo#ref                  | Package pinned to tag, branch, or commit SHA
```

*Source: APM Dependencies reference page, "Package Reference Formats" section*

### Vendoring `shared/apm.md` from the Canonical Source

```bash
# Add the canonical shared/apm.md from microsoft/apm to your repository
gh aw add microsoft/apm/.github/workflows/shared/apm.md --dir shared

# Keep the vendored copy synchronized with upstream
gh aw update

# Local debugging of APM package installation
apm pack
apm unpack
```

*Source: APM Dependencies reference page, "Where shared/apm.md Comes From" section*

### Token Fallback and Deprecation Notices

```
Token fallback order for package fetching:
  GH_AW_PLUGINS_TOKEN → GH_AW_GITHUB_TOKEN → GITHUB_TOKEN

Deprecated fields (do NOT use in new workflows):
  - dependencies: (frontmatter field) — "deprecated and no longer supported;
    migrate to the import-based approach"
  - dependencies: (microsoft/apm-action input) — "deprecated in favour of
    the packages: and apps: inputs"
```

*Source: APM Dependencies reference page — deprecation notices and
"How It Works" section*

### External References

```
Resource                    | URL
----------------------------|------------------------------------------
APM documentation           | https://microsoft.github.io/apm/
APM governance guide        | https://microsoft.github.io/apm/enterprise/governance/
Pack and distribute guide   | https://microsoft.github.io/apm/guides/pack-distribute/
gh-aw integration (APM)     | https://microsoft.github.io/apm/integrations/gh-aw/
apm-action (GitHub)         | https://github.com/microsoft/apm-action
microsoft/apm (GitHub)      | https://github.com/microsoft/apm
shared/apm.md (canonical)   | https://github.com/microsoft/apm/blob/main/.github/workflows/shared/apm.md
```

*Source: APM Dependencies reference page, "Reference" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-sharing-workflows.md` Claim 5 (SHA pinning for reproducibility
    across runs): the `apm.lock` file (Claim 8 here) uses the same SHA-pinning
    principle as `.lock.yml` import resolution. Both guarantee that the same
    source content is installed on every run — `.lock.yml` for workflow import
    SHAs, `apm.lock` for APM package SHAs. The two lock files are the
    repository's complete dependency manifest at different layers of the
    dependency graph (workflow structure vs. agent primitives).
  - `docs-ghaw-compilation-process.md` Claim 9 (artifact-based handoff
    between agent job and safe output jobs): the `apm` job (Claim 3 here)
    follows the same artifact-based handoff pattern — the `apm` job packs
    packages and uploads a bundle artifact, which the agent job downloads as
    pre-steps. Both patterns use GitHub Actions artifacts as the inter-job
    communication mechanism.
  - `docs-ghaw-sharing-workflows.md` Claim 1 (the `source:` frontmatter
    field enables `gh aw update` to track and resynchronize installed
    workflows): the `redirect` declaration in `shared/apm.md` (Claim 5 here)
    is the same tracking mechanism applied to a vendored component rather
    than a top-level workflow. Both enable `gh aw update` to retrieve
    upstream changes without re-specifying the origin URL.

- **Extends**:
  - `docs-ghaw-mcps.md` Claim 9 (shared MCP configuration library in
    `.github/workflows/shared/mcp/`): this note adds the APM-specific shared
    component at `.github/workflows/shared/apm.md`. Together they complete
    the picture of what lives in `.github/workflows/shared/` — shared MCP
    configurations AND the APM workflow. Both are vendored via `gh aw add`
    and kept current via `gh aw update`.
  - `docs-ghaw-compilation-process.md` Claim 5 (agent job step sequence
    starts with "cache restoration"): the APM bundle restoration described
    in Claim 3 here clarifies that "pre-steps" in the agent job include
    downloading and restoring the APM artifact produced by the `apm` job.
    The agent job step sequence gains a concrete preceding dependency that
    the compilation process note does not describe.
  - `docs-ghaw-sharing-workflows.md` Claim 2 (four-tier versioning model
    for workflow distribution): APM's `#ref` format (Claim 7 here) mirrors
    the same four-tier pattern — `#v2.0` (exact tag), `#main` (branch
    reference), and `#<sha>` (SHA pin). Both systems express the same
    stability-vs-currency trade-offs for different artifact types (workflow
    templates vs. agent primitive packages).

- **Contradicts**: None identified. Reviewed all existing corpus source
  notes. No existing note makes claims about APM, agent primitive packaging,
  or the `dependencies:` frontmatter field that contradict the content here.
  The SHA-pinning principle documented in `docs-ghaw-sharing-workflows.md`
  is consistent with (and analogous to) the `apm.lock` mechanism described
  here — they are parallel, not opposing. No contradiction issue required.

- **Novel** (what this note adds that no prior source covers):
  - **APM as a package manager for agent primitives** (Claim 1): No existing
    corpus source documents APM or a package management abstraction for agent
    skills, prompts, and plugins. MCP servers (from `docs-ghaw-mcps.md`) are
    the tool integration layer; APM is the distribution layer for pre-built
    agent content. The two are complementary and operate at different levels
    of abstraction.
  - **Explicit `dependencies:` deprecation** (Claim 2): No existing source
    note mentions the `dependencies:` frontmatter field or its deprecation.
    This is an actionable breaking-change notice for any team with existing
    gh-aw workflows. The migration path (import-based `shared/apm.md`) is
    also documented here for the first time.
  - **`shared/apm.md` vendoring pattern** (Claim 4): The distinction between
    remote imports and local vendored workflow files — and the `gh aw add`
    installation command for APM specifically — is not documented in any
    existing note. `docs-ghaw-sharing-workflows.md` covers the general
    sharing/installation model but does not cover APM's `shared/apm.md`
    specifically.
  - **`apm.lock` as a PR-reviewable governance artifact** (Claim 8): No
    existing source describes a lock file whose diffs appear in PRs for
    explicit review of changes to agent context. `docs-ghaw-sharing-workflows.md`
    Claim 5 covers `.lock.yml` import pinning, but not a distinct `apm.lock`
    file for package-level governance. The framing of lock file review as a
    governance gate on agent capability changes is new.
  - **Cascading token fallback for package authentication** (Claim 9): The
    three-token hierarchy (`GH_AW_PLUGINS_TOKEN` → `GH_AW_GITHUB_TOKEN` →
    `GITHUB_TOKEN`) for APM package fetching is not documented in any existing
    note. No existing note covers APM-specific authentication requirements
    for cross-org or private-repo package distribution.
  - **`apm pack` / `apm unpack` for local reproduction** (Claim 10): The
    local APM debugging toolchain is entirely new to the corpus.

## Guide Impact

### Chapter 05: Tool Integration / Orchestration

- **Add APM as the package-distribution layer above MCP** (Claim 1): The
  guide's tool integration discussion currently covers MCP servers
  (`docs-ghaw-mcps.md`) but not APM. Add a description of APM as the
  mechanism for distributing pre-built agent primitives (skills, prompts,
  plugins) across workflows and repositories. Frame the relationship: MCP
  servers provide tool capabilities at runtime; APM packages distribute
  those tools (and instructions, plugins, and other primitives) as versioned,
  shareable artifacts. Teams building reusable agent components should publish
  them as APM packages.

- **Document the `shared/apm.md` setup pattern** (Claims 3-4): `gh aw add
  microsoft/apm/.github/workflows/shared/apm.md --dir shared` is a
  prerequisite step for any workflow using APM packages. Add to the harness
  setup checklist alongside `gh aw init`.

### Chapter 02: Harness Engineering

- **Flag `dependencies:` as a deprecated field** (Claim 2): If any existing
  guide content references the `dependencies:` frontmatter field, update it.
  The field is "deprecated and no longer supported." The correct pattern is
  importing `shared/apm.md` with a `packages:` input. Guide examples must
  not use the deprecated field.

- **Add `apm.lock` to the reproducibility checklist** (Claim 8): Alongside
  `.lock.yml` and `.github/aw/imports/` (from `docs-ghaw-sharing-workflows.md`
  Claim 5 and `docs-ghaw-compilation-process.md` Claim 6), `apm.lock` is a
  third reproducibility artifact that must be committed to the repository.
  Frame the three together: `.lock.yml` (compiled workflow + import SHAs),
  `actions-lock.json` (pinned action SHAs), and `apm.lock` (pinned package
  SHAs) constitute the complete reproducibility contract for a gh-aw
  repository.

- **Document the three-token hierarchy for APM in enterprise** (Claim 9):
  For teams distributing APM packages across organizational boundaries or
  from private repositories, the `GH_AW_PLUGINS_TOKEN` must be configured.
  Add to the enterprise setup section as a prerequisite for cross-org APM
  package consumption.

### Chapter 03: Safety and Verification

- **Add `apm.lock` PR-review as a governance gate** (Claim 8): The ability
  to review lock file diffs before merging a package update is a governance
  pattern worth naming explicitly. Teams can require PR approval on
  `apm.lock` changes to enforce human review of any change to the agent
  context (new primitives, version bumps). Frame this as the agent-primitive
  analogue of reviewing `yarn.lock` changes for supply chain security.

## Extraction Notes

1. **WebFetch returns AI-summarized content**: The gh-aw documentation is an
   Astro/Starlight SPA. WebFetch returns rendered text with AI processing.
   Three targeted fetches were used to maximize verbatim quote coverage.
   The deprecation notices and token fallback text were confirmed verbatim
   in a second targeted fetch. YAML examples match the source consistently
   across fetches.

2. **`dependencies:` deprecation is the highest-priority finding**: The
   explicit "deprecated and no longer supported" notice is the most
   actionable content on this page and appears before any configuration
   guidance. It is the first thing a practitioner consulting this page will
   encounter.

3. **APM documentation lives on a separate site**: The authoritative APM
   documentation is at `microsoft.github.io/apm/`, not within the gh-aw
   documentation. This page is the gh-aw integration reference; for
   full APM governance, enterprise policy, and `apm pack`/`apm unpack`
   details, the external APM site must be consulted. The External References
   table in Concrete Artifacts captures the relevant entry points.

4. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent
   with gh-aw documentation as of 2026-05-11.

5. **No contradictions to file**: Reviewed all existing source notes. No
   claims in this source materially oppose any existing source note at the
   MINER.md §4a filing threshold. APM is a new concept in the corpus with
   no prior opposing positions to resolve.

6. **`apps:` input not detailed**: The deprecation notice references both
   `packages:` and `apps:` as the replacement inputs for the deprecated
   `dependencies:` on `microsoft/apm-action`. The `apps:` input is not
   further detailed in the fetched content. It likely handles a distinct
   class of installable content (application-level vs. primitive-level).
   The full APM documentation at `microsoft.github.io/apm/` would clarify
   the distinction.
