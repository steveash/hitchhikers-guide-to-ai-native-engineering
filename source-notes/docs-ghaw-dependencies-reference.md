---
source_url: https://github.github.com/gh-aw/reference/dependencies
source_type: docs
title: "GitHub Agentic Workflows: APM Dependencies Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: emerging
issue: "#380"
---

# GitHub Agentic Workflows: APM Dependencies Reference

> The authoritative reference for APM (Agent Package Manager) integration in
> gh-aw — documents how agent primitives (skills, prompts, instructions, agents,
> hooks, plugins) are packaged, versioned, and delivered to agent jobs via a
> dedicated `apm` workflow job, with `apm.lock` SHA pinning for reproducibility
> and a cascading token fallback for multi-org authentication.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/dependencies` page —
  in the "Reference" section alongside `reference/compilation-process`,
  `reference/integrity`, and others. Reference pages document platform mechanics and
  configuration authoritatively. Distinct from the compilation-process and
  sharing-workflows notes: this page covers the APM layer specifically, which
  manages agent-level primitives, not workflow-level imports or action-level
  dependencies.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team that operates Peli de Halleux's agent factory and maintains the `gh aw`
  CLI. The APM canonical source is maintained in `microsoft/apm` on GitHub. Claims
  about package reference formats, lock file behavior, job structure, and token
  fallback are authoritative for this platform integration.
- **Scope**: APM integration with gh-aw — what APM manages, how `shared/apm.md`
  integrates into compiled workflows, the three package reference formats, `apm.lock`
  reproducibility semantics, the token authentication chain, and the canonical
  `microsoft/apm-action@v1.5.0` version. Does NOT cover: the broader compilation
  pipeline (`docs-ghaw-compilation-process.md`), MCP server configuration
  (`docs-ghaw-mcps.md`), workflow-level import sharing (`docs-ghaw-sharing-workflows.md`),
  or runtime dependency monitoring (`docs-ghaw-dependabot.md`).

## Extracted Claims

### Claim 1: APM (Agent Package Manager) manages AI agent primitives — skills, prompts, instructions, agents, hooks, and plugins including the Claude plugin.json specification — as versioned packages with full dependency tree resolution

- **Evidence**: Opening description of APM on the page. Dependency resolution is
  described as working "across the full tree" — nested package dependencies are
  resolved, not just direct dependencies.
- **Confidence**: emerging (first-party documentation; APM itself is maintained by
  Microsoft, and the gh-aw integration is documented here, but broad adoption
  patterns are not yet benchmarked)
- **Quote**: "APM (Agent Package Manager) manages AI agent primitives such as skills,
  prompts, instructions, agents, hooks, and plugins"
- **Our assessment**: APM extends the gh-aw dependency model from the workflow level
  (action pins, import SHAs) to the agent capability level. The inclusion of Claude
  `plugin.json` format support is notable: plugins are a distinct primitive type
  that connects to the tool-use layer, not just instructions or prompts. Full
  dependency tree resolution means a package can itself declare dependencies on
  other packages, enabling composition of capability libraries. For Ch03 and Ch05:
  APM introduces a new dependency layer below MCP servers — agent primitives are
  above the prompt and below the workflow in the abstraction stack.

### Claim 2: APM integrates into gh-aw by importing `shared/apm.md`, which adds a dedicated `apm` job to the compiled workflow that runs `microsoft/apm-action`, packs packages into a bundle, and uploads it as a GitHub Actions artifact for agent jobs to consume

- **Evidence**: The "Usage" and "How it works" sections on the page describe the
  integration model. The `apm` job is a distinct job in the compiled workflow, not
  a step in the agent job.
- **Confidence**: settled (first-party documentation; the job structure and artifact
  upload mechanism are explicitly described)
- **Quote**: "APM is configured by importing the shared/apm.md workflow, which
  creates a dedicated apm job that packs packages and uploads the bundle as a
  GitHub Actions artifact."
- **Our assessment**: The dedicated `apm` job pattern is architecturally consistent
  with how gh-aw handles other pre-agent concerns — separate jobs for pre-activation,
  activation, and now package installation. The artifact upload → download pattern
  means agent jobs receive the package bundle as a filesystem restore, not via
  network calls at runtime. This keeps agent job execution deterministic: all
  capability dependencies are resolved and materialized before the AI engine starts.
  For Ch03 (Orchestration): the `apm` job runs before agent jobs as part of the
  compiled workflow's pre-execution phase, analogous to how activation prepares
  context before AI execution.

### Claim 3: The canonical `shared/apm.md` workflow is maintained by Microsoft in `microsoft/apm` on GitHub and is installed via `gh aw add microsoft/apm/.github/workflows/shared/apm.md --dir shared`

- **Evidence**: The "Where shared/apm.md comes from" section explicitly names the
  canonical source and the installation command.
- **Confidence**: settled (first-party documentation; the canonical repository and
  installation command are explicitly named)
- **Quote**: "The canonical source is maintained in microsoft/apm."
- **Our assessment**: This is a Microsoft-owned dependency in the gh-aw ecosystem —
  `shared/apm.md` is not bundled into the `gh aw` CLI but rather fetched from
  `microsoft/apm` and stored locally in `.github/workflows/shared/`. The
  `gh aw add` command installs it via the same mechanism used for other shared
  workflow components. This means the APM integration is updateable via
  `gh aw update` when new versions are released. For Ch02 (Harness Engineering):
  document APM setup as a one-time `gh aw add` operation that adds a shared
  workflow file; thereafter, any workflow using `imports: shared/apm.md` gets
  the APM job automatically.

### Claim 4: Three package reference formats are supported: full packages (`owner/repo`), individual primitives by path (`owner/repo/path/to/primitive`), and version-pinned references (`owner/repo#ref` for tag, branch, or commit SHA)

- **Evidence**: The "Package reference formats" table on the page lists all three
  formats with their descriptions. The examples section demonstrates all three in
  use, including version-pinned references to both tags (`#v2.0`) and branches
  (`#main`).
- **Confidence**: settled (first-party documentation; the format table is explicit)
- **Quote**: "Individual primitive (skill, instruction, plugin, etc.) from a
  repository"
- **Our assessment**: The individual-primitive path format (`owner/repo/path/to/primitive`)
  is the most powerful reference type — it allows pulling a single skill or plugin
  from any GitHub repository without requiring the repository to be structured as
  an APM package. The examples show `github/awesome-copilot/skills/review-and-refactor`
  and `github/awesome-copilot/plugins/context-engineering` — these are granular
  capability extractions from a public Microsoft repository. Version pinning via
  `#ref` supports all three standard Git reference types (tag, branch, SHA),
  giving teams the same version governance options available in other package
  managers. For Ch05 (Tool Integration): the path-based format is the low-friction
  entry point — teams can consume individual skills from community repositories
  without committing to full package adoption.

### Claim 5: `apm.lock` pins every package to an exact commit SHA, ensuring the same versions are installed on every run; lock file diffs appear in pull requests to provide an audit trail for dependency changes

- **Evidence**: The "Reproducibility and governance" section describes both the
  mechanical guarantee (SHA pinning → same versions) and the governance benefit
  (PR diffs → audit trail).
- **Confidence**: settled (first-party documentation; the lock file behavior is
  explicitly described)
- **Quote**: "APM lock files (apm.lock) pin every package to an exact commit SHA,
  so the same versions are installed on every run."
- **Our assessment**: The `apm.lock` file is the agent-primitive equivalent of a
  package manager lockfile (analogous to `yarn.lock`, `go.sum`, or gh-aw's own
  `actions-lock.json`). SHA pinning at this layer means that even if an upstream
  repository modifies a skill or plugin at a branch reference, the compiled workflow
  uses the pinned SHA until the lock is explicitly updated. The PR-diff visibility
  of lock file changes is a governance feature: security reviewers can inspect
  exactly which capability versions changed across workflow updates. For Ch03
  (Safety and Verification): `apm.lock` should be committed to version control
  (same recommendation as `actions-lock.json`) — it is the reproducibility and
  audit artifact for agent capability dependencies.

### Claim 6: Package authentication uses a cascading token fallback: `GH_AW_PLUGINS_TOKEN` → `GH_AW_GITHUB_TOKEN` → `GITHUB_TOKEN`, supporting multi-org GitHub App authentication configured via `apps:[]`

- **Evidence**: The "How it works" section describes the token fallback chain. The
  canonical `shared/apm.md` version description adds that it "supports multi-org
  GitHub App authentication (apps:[]) and multi-bundle restore."
- **Confidence**: settled (first-party documentation; the token fallback and
  GitHub App authentication support are explicitly stated)
- **Quote**: "Packages are fetched using the cascading token fallback:
  GH_AW_PLUGINS_TOKEN → GH_AW_GITHUB_TOKEN → GITHUB_TOKEN."
- **Our assessment**: The three-level fallback mirrors gh-aw's general token
  management approach (see `docs-ghaw-integrity-reference.md` Claim 10 for
  GitHub Variables for integrity config). The `GH_AW_PLUGINS_TOKEN` at the top
  of the chain allows organizations to use a dedicated credential for package
  access — decoupled from the workflow execution credential (`GITHUB_TOKEN`).
  Multi-org GitHub App authentication (`apps:[]`) is particularly important for
  enterprise scenarios where packages are distributed across GitHub organizations
  with different access control boundaries. For Ch05 (Tool Integration): teams
  consuming packages from private repositories or multiple organizations must
  configure `GH_AW_PLUGINS_TOKEN` or the `apps:[]` GitHub App configuration;
  the `GITHUB_TOKEN` fallback only works for packages in the same organization.

### Claim 7: The canonical `shared/apm.md` version pins `microsoft/apm-action@v1.5.0` and supports multi-bundle restore, enabling multiple APM package sets to be configured and consumed independently within a single workflow

- **Evidence**: The "Where shared/apm.md comes from" section states: "The canonical
  version pins microsoft/apm-action@v1.5.0 and supports multi-org GitHub App
  authentication (apps:[]) and multi-bundle restore."
- **Confidence**: settled (first-party documentation; the version pin and
  capabilities are explicitly named)
- **Quote**: "The canonical version pins microsoft/apm-action@v1.5.0 and supports
  multi-org GitHub App authentication (apps:[]) and multi-bundle restore."
- **Our assessment**: The explicit `@v1.5.0` pin in the canonical `shared/apm.md`
  means that when the file is installed via `gh aw add`, it references a specific
  version of the underlying action — consistent with gh-aw's general philosophy
  of compile-time SHA pinning for reproducibility. Multi-bundle restore extends
  the basic model: rather than a single package list producing a single bundle,
  teams can configure multiple named bundles and restore them selectively. This
  supports workflows with distinct capability profiles for different execution
  contexts (e.g., one bundle for triage tasks, another for code review). For
  Ch02: document the multi-bundle capability as an advanced pattern for workflows
  that serve multiple distinct task types with different capability requirements.

## Concrete Artifacts

### APM Package Import Syntax

```yaml
# Import shared/apm.md and declare package dependencies
imports:
  - uses: shared/apm.md
    with:
      packages:
        # Full APM package
        - microsoft/apm-sample-package
        # Individual primitive from any repository
        - github/awesome-copilot/skills/review-and-refactor
        # Plugin (Claude plugin.json format)
        - github/awesome-copilot/plugins/context-engineering
        # Version-pinned to a tag
        - microsoft/apm-sample-package#v2.0
        # Version-pinned to a branch
        - microsoft/apm-sample-package#main
```

*Source: `reference/dependencies` — "Usage" and "Examples" sections*

### Package Reference Format Table

```
Format                         | Description
-------------------------------|--------------------------------------------------
owner/repo                     | Full APM package
owner/repo/path/to/primitive   | Individual primitive (skill, instruction, plugin,
                               | etc.) from a repository
owner/repo#ref                 | Package pinned to a tag, branch, or commit SHA
```

*Source: `reference/dependencies` — "Package reference formats" section*

### APM Setup Command

```bash
# Install the canonical shared/apm.md from microsoft/apm
gh aw add microsoft/apm/.github/workflows/shared/apm.md --dir shared
```

*Source: `reference/dependencies` — "Where shared/apm.md comes from" section*

### How It Works (Operational Flow)

```
1. shared/apm.md is imported in the workflow
2. Compilation adds a dedicated `apm` job to the workflow
3. The apm job runs microsoft/apm-action@v1.5.0
4. apm-action fetches declared packages (using token fallback chain)
5. Packages are packed into a bundle archive
6. Bundle is uploaded as a GitHub Actions artifact
7. Agent jobs download and restore the bundle as pre-steps
8. Agent runtime has access to all declared skills, plugins, instructions
```

*Source: `reference/dependencies` — "How it works" section*

### Token Fallback Chain

```
GH_AW_PLUGINS_TOKEN     (preferred: dedicated package credential)
  ↓ (if absent)
GH_AW_GITHUB_TOKEN      (workflow execution credential)
  ↓ (if absent)
GITHUB_TOKEN            (default: same-org access only)

For multi-org packages: configure apps:[] with GitHub App credentials
in shared/apm.md for cross-organization authentication
```

*Source: `reference/dependencies` — "How it works" section*

### APM Reference Links (from the page)

```
Resource                  | URL
--------------------------|--------------------------------------------------
APM documentation         | https://microsoft.github.io/apm/
APM governance guide      | https://microsoft.github.io/apm/enterprise/governance/
Pack and distribute guide | https://microsoft.github.io/apm/guides/pack-distribute/
gh-aw integration         | https://microsoft.github.io/apm/integrations/gh-aw/
apm-action (GitHub)       | https://github.com/microsoft/apm-action
microsoft/apm (GitHub)    | https://github.com/microsoft/apm
shared/apm.md (canonical) | https://github.com/microsoft/apm/blob/main/.github/workflows/shared/apm.md
```

*Source: `reference/dependencies` — "Reference" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-compilation-process.md` Claim 6 (action pins to SHA as supply-chain
    defense; "tags can be moved, SHAs cannot"): The `apm.lock` file applies the same
    SHA-pinning principle to agent primitives — the same supply-chain rationale that
    the compiler uses for action references applies here to skill and plugin packages.
    Both use commit SHAs as the immutable anchor. This source adds a third lockfile
    type to the gh-aw security model (alongside `actions-lock.json` and `.lock.yml`
    import pins).
  - `docs-ghaw-sharing-workflows.md` Claim 5 (remote imports resolve to exact commit
    SHAs in `.lock.yml` for reproducibility): Both the import-caching mechanism and
    `apm.lock` use SHA pinning for the same goal — deterministic, reproducible
    dependency resolution across environments. The patterns are architecturally
    consistent; this source extends the SHA-pinning approach to a different dependency
    class (agent primitives vs. workflow imports).
  - `docs-ghaw-dependabot.md` Claim 1 (`gh aw compile --dependabot` scans for
    runtime tool invocations and generates Dependabot manifests): Dependabot monitors
    npm/pip/Go runtime tools; `apm.lock` provides reproducibility for agent primitives.
    Together they describe two distinct dependency surfaces in gh-aw workflows, each
    with its own management mechanism.

- **Extends**:
  - `docs-ghaw-mcps.md` (four MCP server types covering tool integration at the
    infrastructure level): MCPs provide tools at the API/infrastructure layer;
    APM provides capabilities at the agent primitive layer (skills, prompts,
    instructions, plugins). These are complementary integration layers. An agent
    might consume MCP tools for API access while relying on APM primitives for
    pre-built task instructions and skill definitions. Neither note documents the
    interaction between these two layers.
  - `docs-ghaw-sharing-workflows.md` (distribution model for whole workflows): That
    note covers distributing complete workflows with `gh aw add`; APM extends the
    distribution model to sub-workflow components. An APM primitive (e.g., a skill
    or plugin) can be reused across multiple workflows without distributing the
    whole workflow. This is a finer-grained reuse model than workflow-level sharing.
  - `docs-ghaw-compilation-process.md` Claim 2 (import resolution via deterministic
    BFS traversal): The `shared/apm.md` import is resolved through the same BFS
    import mechanism — it is a workflow import like any other, and the APM job is
    generated by the compiler from that import. This source reveals that some imports
    contribute not just instructions/config to the workflow but entirely new job
    types (`apm`) to the compiled job graph.

- **Contradicts**: None identified. No existing source note makes claims that
  conflict with the APM model, the `apm.lock` pinning mechanism, or the dedicated
  `apm` job pattern. The job separation (APM job → artifact → agent job) is
  consistent with gh-aw's general principle of separating concerns into distinct
  jobs. No contradiction issue required.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **APM as a named package manager for agent primitives**: No existing source note
    documents APM or the concept of versioned agent primitive packages (skills,
    prompts, instructions, agents, hooks, plugins). Prior notes cover workflow-level
    imports and MCP servers; this is a third, distinct capability integration layer.
  - **`apm.lock` as an agent capability lockfile**: The SHA-pinned lockfile for
    agent primitives, with PR-diff audit visibility, is entirely new to the corpus.
    It extends gh-aw's lockfile pattern (already in `actions-lock.json` and
    `.lock.yml`) to the capability dependency surface.
  - **Individual primitive path references** (Claim 4): The `owner/repo/path/to/primitive`
    format for granular capability extraction from any GitHub repository is new.
    This allows consuming individual skills or plugins without adopting full APM
    packages.
  - **Claude `plugin.json` format support**: APM explicitly handles Claude plugin
    primitives as a first-class type. No existing source note documents a versioned
    distribution mechanism for Claude plugins in the gh-aw context.
  - **Multi-org GitHub App authentication (`apps:[]`)** (Claim 6): Cross-organization
    package authentication via GitHub Apps is new. The `GH_AW_PLUGINS_TOKEN`
    dedicated credential for package access is also new to the corpus.
  - **Multi-bundle restore** (Claim 7): Multiple named package bundles within a
    single workflow for different capability profiles is a new advanced pattern.
  - **Dedicated `apm` job in compiled workflow** (Claim 2): The addition of an
    entirely new job type to the compiled workflow via a `shared/apm.md` import is
    new. Prior notes document the fixed set of job types (pre-activation, activation,
    agent, detection, safe outputs, conclusion) — this shows that shared imports can
    extend the job graph with new roles.

## Guide Impact

### Chapter 03: Orchestration / Agent Composition

- **Add APM as a third capability integration layer** (Claims 1, 2): The guide
  currently covers tool integration via MCP servers (infrastructure layer) and
  prompt/instruction configuration (author layer). APM is a middle layer: pre-built,
  versioned agent primitives. Add APM to the capability composition model: MCPs for
  API access → APM for reusable skills/plugins → frontmatter for workflow-specific
  instructions. Clarify the boundaries: MCP is for dynamic tool calls; APM is for
  static capability distribution.

- **Document the `apm` job as a new compiled job type** (Claim 2): The compiled
  workflow job graph expands when `shared/apm.md` is imported. Practitioners who
  read compiled `.lock.yml` files should understand that the `apm` job is an APM
  artifact, not a custom workflow step. Update any Ch03 documentation of the
  compiled job structure to note that APM imports add an `apm` pre-execution job.

### Chapter 05: Tool Integration / Capability Distribution

- **Add individual primitive path references as the low-friction entry point**
  (Claim 4): The `owner/repo/path/to/primitive` format allows teams to consume
  individual skills from community repositories (e.g., `github/awesome-copilot/skills/`)
  without full APM package adoption. Document as the recommended starting pattern
  before committing to full APM package structure.

- **Document `apm.lock` as a required committed artifact** (Claim 5): Like
  `actions-lock.json` and `.lock.yml` import pins, `apm.lock` should be committed
  to version control. Teams relying on APM without committing the lockfile risk
  non-reproducible capability resolution across environments. Add to the harness
  reproducibility checklist alongside the other lockfiles.

- **Document the token fallback chain and multi-org authentication** (Claim 6):
  Teams consuming packages from private repositories or multiple organizations must
  configure `GH_AW_PLUGINS_TOKEN` or the `apps:[]` GitHub App mechanism. The
  `GITHUB_TOKEN` fallback silently fails to authenticate cross-org access — this
  is a silent failure mode that must be documented. Add to the Ch05 APM setup guide.

- **Add Claude plugin distribution via APM as a capability governance pattern**
  (Claim 1): For organizations distributing Claude plugins across multiple workflows,
  APM provides versioning, SHA pinning, and audit trails that ad-hoc plugin copying
  does not. Recommend APM as the distribution mechanism for org-wide plugin
  governance alongside the `private: true` workflow governance pattern in
  `docs-ghaw-sharing-workflows.md` Claim 4.

## Extraction Notes

1. **WebFetch content is AI-summarized**: The gh-aw documentation is an
   Astro/Starlight SPA. WebFetch converts the rendered page to markdown and
   then further processes it with an AI model. Three targeted fetches were made
   to maximize verbatim coverage. Direct quotes used in claims were verified by
   cross-checking across multiple fetch passes for consistency.

2. **Compact reference page**: The `reference/dependencies` page is focused and
   relatively short compared to `reference/compilation-process` or
   `reference/integrity`. Seven claims were extracted — fewer than the 5-15
   target range, but the page appears to cover a single focused topic (APM
   integration) without extensive subsections. Shallow extraction was not the
   reason; the source itself is compact.

3. **APM documentation not followed**: The reference section links to
   `https://microsoft.github.io/apm/` for full APM documentation, governance
   guides, and pack/distribute guides. These were not followed per the 5-page
   sub-page limit — the focus was on the gh-aw integration reference, not the
   full APM specification. The external APM documentation may warrant a separate
   source submission.

4. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   current gh-aw platform state as of 2026-05-25.

5. **Previous Miner PR closed without merge**: PR #643 (opened 2026-05-11,
   closed 2026-05-24) covered this same source. The closure without merge and
   re-queueing of the issue (`mining-queued` label remains) indicates the prior
   note required rework. This note is a fresh extraction following MINER.md
   guidelines, not a copy of the prior PR's content.

6. **No contradictions filed**: Reviewed all existing source notes in the
   ghaw-* series. No claims in this source materially oppose any existing note
   at the MINER.md §4a filing threshold. The APM model is additive to existing
   gh-aw documentation.
