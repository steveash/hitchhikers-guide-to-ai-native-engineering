---
source_url: https://github.github.com/gh-aw/guides/organization-practices/sharing-workflows
source_type: docs
title: "GitHub Agentic Workflows: Sharing Workflows (Organization Practices)"
author: GitHub Agentic Workflows team (official documentation)
date_published: null
date_extracted: 2026-05-02
last_checked: 2026-05-02
status: current
confidence_overall: emerging
issue: "#482"
---

# GitHub Agentic Workflows: Sharing Workflows (Organization Practices)

> The distribution and governance layer for gh-aw at enterprise scale — documents the four-tier
> versioning model, `private: true` access control, import caching + `.lock.yml` reproducibility
> contract, parameterized template imports, and the recommended central-repo enterprise pattern,
> all of which are absent from the orchestration-focused notes already in the corpus.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, "Organization Practices →
  Sharing Workflows" guide page; not a blog post or practitioner account — first-party reference
  for the design-time sharing and governance layer of gh-aw)
- **Author credibility**: GitHub Agentic Workflows team (the same team behind the Peli de
  Halleux / Don Syme agent factory series and the broader gh-aw documentation suite). First-party
  documentation for the `gh aw` platform. Claims about workflow installation mechanics, versioning
  semantics, `private:` frontmatter behavior, and lock file reproducibility are settled for this
  platform. The page includes a caveat that "recommended patterns, commands, and configuration
  options may change" — CLI flags and specific command syntax should be treated as `emerging`
  pending platform updates.
- **Scope**: The design-time sharing and governance layer — how workflows are installed, versioned,
  updated, access-controlled, and composed from shared modules. Covers six independent sharing
  layers (complete workflow installation, reusable component imports, parameterized templates,
  versioning strategies, privacy/access controls, import caching). Also covers the recommended
  enterprise implementation pattern and governance considerations. Does NOT cover: the
  orchestration-layer (Orchestrator+Worker, fan-out — that is `docs-ghaw-central-repo-ops.md`),
  the `imports:` subsystem in depth (covered by issue #298), or the compilation model conceptual
  overview (that is `docs-ghaw-how-they-work.md`).

## Extracted Claims

### Claim 1: `gh aw add <org>/<repo>/<workflow>@<version>` is the primary mechanism for platform teams distributing versioned workflows to consuming repositories

- **Evidence**: The page documents `gh aw add acme-org/agentic-workflows/ci-doctor@v1.2.0` as
  the installation command, noting it "automatically records origin and version information in
  the workflow's frontmatter via a `source:` field." The `gh aw add-wizard` variant provides
  interactive setup while `gh aw add` supports scripted deployments. The command is designed
  for the enterprise model where a platform team owns a central repository of versioned templates
  and consuming teams install copies into their own repositories.
- **Confidence**: emerging (first-party documentation; CLI behavior is documented but flagged
  as subject to change)
- **Quote**: "The installation automatically records origin and version information in the
  workflow's frontmatter via a `source:` field."
- **Our assessment**: The `source:` frontmatter tracking is a significant detail — it means
  every installed workflow carries a provenance record that `gh aw update` can later use to
  fetch the appropriate upstream version. The design intentionally links the installed artifact
  to its origin, making governance of "which version is installed where" tractable. This extends
  `docs-ghaw-agentic-authoring.md` Claim 3 (which names `gh aw add` as the synchronized reuse
  path but does not detail the versioning lifecycle) with the full install + track + update
  workflow. For Ch02 (Harness Engineering): `gh aw add` with a version pin is the correct
  pattern for distributing workflows across repositories — not `create-agentic-agent` (which
  is for one-time forks), not copy-paste.

### Claim 2: The platform supports four distinct reference types for versioning with different update and governance semantics

- **Evidence**: The page explicitly names and characterizes all four:
  - **Exact release tags** (`@v1.2.0`): immutable pins that never update automatically
  - **Moving major refs** (`@v1`): track latest compatible releases within a version stream;
    picked up automatically by `gh aw update`
  - **Branch references** (`@develop`): follow latest commits on specified branches
  - **SHA pins** (`@abc123def`): strict reproducibility guarantees
  Each type has a distinct governance trade-off. Moving refs accept compatible updates
  automatically; exact tags require explicit re-installation to advance; SHA pins freeze
  behavior regardless of upstream changes.
- **Confidence**: emerging (first-party documentation; the specific update semantics per
  ref type are documented but flagged as potentially subject to change)
- **Quote**: (no single direct quote covers all four; see Concrete Artifacts section for
  the tabular representation)
- **Our assessment**: The four-tier model is the most actionable novelty in this source.
  It gives platform teams a concrete vocabulary for expressing different stability-vs-currency
  trade-offs: production workflows should use exact tags or SHA pins; staging/preview
  workflows can use moving major refs; development integration can use branch refs. The key
  practical distinction is between `@v1.2.0` (never moves) and `@v1` (moves with compatible
  releases) — these look similar but have opposite update behaviors. For Ch02: document the
  four tiers with their governance implications as a decision framework for platform teams
  choosing version pins for their workflow templates.

### Claim 3: `gh aw update` retrieves upstream changes using 3-way merge by default, with `--no-merge` and `--major` as override flags for different update policies

- **Evidence**: The page documents the command and its flags: "`gh aw update ci-doctor` (single
  workflow) or `gh aw update` (all tracked workflows). Updates use 3-way merge by default to
  preserve local modifications. The `--no-merge` flag replaces local copies entirely. The
  `--major` flag allows moving beyond the currently tracked major version line."
- **Confidence**: emerging (first-party documentation; CLI flags subject to change per
  platform caveat)
- **Quote**: "Updates use 3-way merge by default to preserve local modifications."
- **Our assessment**: The 3-way merge default is a significant UX decision: it treats
  installed workflows as partially-owned artifacts where local customizations should be
  preserved through upstream updates. This is the same model used by `git rebase` — absorb
  upstream changes while keeping local modifications. The practical consequence is that
  consuming teams can customize an installed workflow and still receive upstream improvements
  without losing their customizations. The `--no-merge` flag is for cases where consuming
  teams want a clean overwrite (resetting to the upstream version); `--major` is for
  explicitly crossing semantic version boundaries. For Ch02: document the 3-way merge
  semantics as the default update contract — consuming teams should expect their local
  modifications to be preserved across updates unless they explicitly request `--no-merge`.

### Claim 4: `private: true` in workflow frontmatter is the access control primitive that blocks installation from external repositories, enabling org-internal catalogs

- **Evidence**: The page states that `private: true` in frontmatter "prevents installation into
  external repositories." Organization-internal catalogs are implemented "using private or
  internal repositories" to limit access to organization members. Attempting to install a
  private workflow from another repository returns an error. Private/internal repository
  visibility provides a second layer of access control; `private: true` is the workflow-level
  control.
- **Confidence**: emerging (first-party documentation; behavior is clearly described but
  subject to platform evolution)
- **Quote**: "`private: true` in frontmatter prevents installation into external repositories"
- **Our assessment**: `private: true` is the governance boundary between "internal-only"
  and "distributable" workflows. Without it, any workflow in a publicly accessible repository
  can be installed anywhere. The two-layer access model (repository visibility + `private:`
  frontmatter) is worth noting: repository visibility controls who can discover and read
  the workflow; `private: true` controls whether `gh aw add` can install it. An internal
  repository with `private: true` workflows provides an org-member-only catalog where
  consumption still requires explicit installation. For Ch05 (Team Adoption): document
  `private: true` as the mechanism for building curated internal catalogs that org members
  can install but external actors cannot — enabling a self-service model within the org
  boundary.

### Claim 5: Remote imports resolve to exact commit SHAs in `.lock.yml`, and the local `.github/aw/imports/` cache organized by SHA forms a reproducibility contract across compilations

- **Evidence**: "During compilation, remote imports resolve to exact commit SHAs recorded
  in `.lock.yml`. This lock file, combined with the local import cache organized by commit
  SHA, guarantees reproducibility across runs regardless of upstream branch changes.
  Cached imports persist for subsequent compilations until explicitly updated." The import
  cache is explicitly located under `.github/aw/imports/` and is organized by commit SHA,
  which prevents redundant downloads when multiple references target the same commit.
- **Confidence**: settled (first-party documentation; the SHA-pinning behavior is a
  deterministic platform mechanism, not a recommendation)
- **Quote**: "guarantees reproducibility across runs regardless of upstream branch changes"
- **Our assessment**: The lock file + import cache together form a two-part reproducibility
  guarantee. The `.lock.yml` is the declaration of intent (which SHA was used); the
  `.github/aw/imports/` cache is the materializable artifact (the actual content at that
  SHA). Together they enable offline compilation: once imports are cached, a workflow can
  be compiled without network access to the upstream repository. This extends
  `docs-ghaw-how-they-work.md` Claim 7 (the `.md` → `.lock.yml` compilation model) with
  the import caching semantics — the lock file is not just a compiled executable but also
  a dependency manifest that pins remote imports to exact SHAs. For Ch02: both `.lock.yml`
  and `.github/aw/imports/` should be committed to the repository as part of the
  reproducibility guarantee (analogous to committing `yarn.lock` or `go.sum`).

### Claim 6: Parameterized template imports via `import-schema` + `uses`/`with` allow a single shared component to serve multiple consuming workflows with distinct configurations

- **Evidence**: The page documents the syntax:
  ```yaml
  imports:
    - uses: acme-org/shared-workflows/shared/reviewer.md@v1
      with:
        languages: ["go", "typescript"]
        severity: "high"
  ```
  Shared workflows declare `import-schema` to define accepted parameters. The page states
  this "allows single shared components to serve multiple consuming workflows with distinct
  configurations without requiring separate copies."
- **Confidence**: emerging (first-party documentation with concrete syntax example)
- **Quote**: "allows single shared components to serve multiple consuming workflows with
  distinct configurations without requiring separate copies"
- **Our assessment**: This is the gh-aw equivalent of a parameterized function or
  configurable module. Without `import-schema`, shared components must be copied and
  modified per consumer (fork model). With `import-schema`, a single component handles
  multiple configuration profiles, and changes to the shared component propagate to all
  consumers on next update. The practical value is for shared building blocks like security
  policies (where severity level varies by consumer), tool configurations (where allowed
  languages vary), or prompt templates (where domain-specific context varies). For Ch02:
  `import-schema` + `uses`/`with` is the pattern for building a modular shared library of
  workflow components — avoid copy-paste proliferation of shared components, use
  parameterized imports instead.

### Claim 7: Cross-repository execution at runtime requires explicit `target-repo` and `allowed-repos` declarations in `safe-outputs` frontmatter plus appropriate GitHub token permissions

- **Evidence**: The page documents the runtime cross-repo execution pattern with a concrete
  example:
  ```yaml
  safe-outputs:
    create-issue:
      target-repo: "acme-org/target-repo"
      allowed-repos: ["acme-org/repo1", "acme-org/repo2"]
  ```
  Operations include "reading files and metadata from other repositories, checking out code
  from target repositories for analysis or modification, writing safe outputs to target
  repositories with authentication and allowlists." The explicit `allowed-repos` declaration
  is required; cross-repository operations "require appropriate GitHub token permissions
  and explicit `allowed-repos` declarations."
- **Confidence**: settled (first-party documentation; `allowed-repos` is a platform-enforced
  field, not a recommendation)
- **Quote**: "Cross-repository operations require appropriate GitHub token permissions and
  explicit `allowed-repos` declarations."
- **Our assessment**: The `allowed-repos` whitelist is a compile-time-enforced blast radius
  control — a workflow can only target repositories explicitly listed in its frontmatter. This
  extends `docs-ghaw-central-repo-ops.md` Claim 2 (the `max: 5` fan-out limit as a blast
  radius control) with the complementary per-repo allowlist mechanism: fan-out is bounded
  by count (`max`) AND by destination (`allowed-repos`). Together, they form a two-axis
  blast radius model. For Ch03 (Safety and Verification): `allowed-repos` should be treated
  as a security boundary, not an optional annotation — it limits which repositories a workflow
  can modify at the infrastructure level.

### Claim 8: The recommended enterprise pattern combines a central `agentic-workflows` repository, versioned templates, shared modules under `shared/`, `gh aw add` for installation, and `private: true` for internal-only workflows

- **Evidence**: The page describes a five-element enterprise pattern:
  1. Central repository (`agentic-workflows`) housing versioned templates under `workflows/`
     and shared modules under `shared/`
  2. Installation pattern using `gh aw add acme-org/agentic-workflows/<workflow>@<version>`
  3. Module strategy importing common components via `imports:` declarations
  4. Version anchoring through repository tags supporting production stability and
     development integration
  5. Privacy marking using `private: true` for internal-only workflows
  The page states this "enables platform teams to maintain centralized control while allowing
  consuming teams reproducibility through version pinning and local customization preservation
  via 3-way merge."
- **Confidence**: emerging (design guidance from the platform team; the pattern is well-motivated
  and internally coherent; real-world adoption at scale is not benchmarked in this documentation)
- **Quote**: "enables platform teams to maintain centralized control while allowing consuming
  teams reproducibility through version pinning and local customization preservation via
  3-way merge"
- **Our assessment**: This is a complete, opinionated enterprise architecture for distributing
  agentic workflows at organizational scale. The central repo is the platform team's
  responsibility; consuming teams get reproducibility (version pins) and flexibility
  (3-way merge preserves customizations). The `shared/` directory convention and `private: true`
  markings together create a catalog model: a curated set of org-internal building blocks
  available via `gh aw add` but not publicly distributable. Notably, this source covers the
  design-time distribution concern that `docs-ghaw-central-repo-ops.md` does not address —
  that note covers how orchestrators dispatch workers at runtime; this note covers how workflow
  definitions are packaged and governed before they run. For Ch05 (Team Adoption): recommend
  the central-repo pattern as the enterprise starting point and distinguish it from
  `docs-ghaw-central-repo-ops.md`'s runtime orchestration concerns.

### Claim 9: Governance decisions about workflow sharing are primarily operational rather than technical — ownership, update promotion, consumption authorization, and fork conditions matter more than file formats

- **Evidence**: The page frames governance as a set of operational questions: "workflow
  ownership and change review processes; testing, tagging, and promotion workflows for updates;
  repository consumption and dispatch authorization policies; standardization of secrets,
  permissions, and safe output configurations; conditions permitting teams to fork rather than
  remain on shared versions." The framing: "These operational decisions impact reliability more
  substantially than technical file formats."
- **Confidence**: anecdotal (the relative importance of operational vs. technical decisions
  is an editorial judgment from the platform team, not a measured finding)
- **Quote**: "These operational decisions impact reliability more substantially than technical
  file formats."
- **Our assessment**: This framing is consistent with the broader pattern in the corpus that
  the hardest problems in agentic adoption are organizational, not technical (see
  `blog-bvp-shopify-ai-playbook.md` and `blog-thebatch-ng-aiteam-structure.md` on
  organizational structure for AI). The specific question "when can a team fork rather than
  remain on shared versions?" is the hardest governance question in any shared-library model —
  it requires balancing standardization benefits against consuming-team autonomy. For Ch05:
  use the platform team's governance question list as a template for org-level policy
  discussions about agentic workflow adoption. The technical setup is the easy part; the
  ownership and fork-permission decisions are where adoption stalls.

### Claim 10: The `gh aw add-wizard` command provides interactive workflow installation, while `gh aw add` is the scriptable equivalent for CI/CD-style deployments

- **Evidence**: The page documents both variants: "`gh aw add-wizard` provides interactive
  setup, while `gh aw add` supports scripted deployments." Both commands trigger the
  installation of a remote workflow into the local repository with `source:` tracking.
- **Confidence**: settled (first-party documentation; both commands are explicitly named)
- **Quote**: "`gh aw add-wizard` provides interactive setup, while `gh aw add` supports
  scripted deployments"
- **Our assessment**: The two variants serve different adoption contexts. `gh aw add-wizard`
  is the human-facing path (developer runs it manually, answers prompts); `gh aw add` is
  the automation-facing path (CI/CD pipeline or Makefile runs it deterministically). The
  existence of a scriptable variant enables workflows-as-code patterns where repository
  configuration (including which agentic workflows are installed) is managed in version
  control and applied automatically. This refines `blog-gh-aw-operations-release-workflows.md`
  Claim 4, which only documents `gh aw add-wizard` and does not mention the scriptable
  `gh aw add` variant.

## Concrete Artifacts

### Complete Workflow Installation Command

```bash
# Install a versioned workflow from a central repository
gh aw add acme-org/agentic-workflows/ci-doctor@v1.2.0

# Interactive variant (prompts for configuration)
gh aw add-wizard <workflow-url>

# Update a single tracked workflow
gh aw update ci-doctor

# Update all tracked workflows
gh aw update

# Update without preserving local modifications (wholesale replace)
gh aw update --no-merge

# Cross major version boundary
gh aw update --major
```

*Source: Sharing Workflows guide, "Complete Workflow Installation" and "Versioning Strategies"
sections. CLI flags flagged as subject to change per platform caveat.*

### Four-Tier Versioning Reference

```
Ref type             Example            Update behavior           Governance trade-off
──────────────────── ────────────────── ──────────────────────── ────────────────────────
Exact release tag    @v1.2.3            Never moves               Max reproducibility;
                                                                  must re-install to advance
Moving major ref     @v1                Follows latest compatible Automatic compatible
                                        releases in v1.x stream  updates; crossing to @v2
                                                                  requires --major
Branch reference     @develop           Follows HEAD on branch   Latest always; unstable
SHA pin              @abc123def         Never moves (SHA-bound)   Absolute reproducibility;
                                                                  explicit re-install only

Rule of thumb:
  Production workflows → @v1.2.3 or @abc123def (never surprise-update)
  Staging/preview      → @v1 (absorb compatible improvements automatically)
  Development          → @develop (track latest, accept instability)
```

*Source: Sharing Workflows guide, "Versioning Strategies" section.*

### Parameterized Import Syntax

```yaml
# Consuming workflow imports a shared component with configuration parameters
imports:
  - uses: acme-org/shared-workflows/shared/reviewer.md@v1
    with:
      languages: ["go", "typescript"]
      severity: "high"

  # Plain import (no parameters — shared component is not parameterized)
  - acme-org/shared-workflows/shared/security-setup.md@v2.1.0
  - acme-org/shared-workflows/shared/mcp/tavily.md@v1.0.0
```

*Source: Sharing Workflows guide, "Parameterized Template Configuration" section.*

### Privacy and Cross-Repository Safe Outputs Configuration

```yaml
---
# Workflow-level access control: blocks gh aw add from external repos
private: true

# Runtime cross-repository execution: explicit allowlist required
safe-outputs:
  create-issue:
    target-repo: "acme-org/target-repo"
    allowed-repos: ["acme-org/repo1", "acme-org/repo2"]
---
```

*Source: Sharing Workflows guide, "Privacy and Access Controls" and "Cross-Repository
Execution" sections.*

### Enterprise Implementation Pattern (Canonical Shape)

```
Central repository layout:
  agentic-workflows/
    workflows/
      ci-doctor.md          ← versioned templates (tagged @v1.2.0, @v2.0.0, etc.)
      release-manager.md
      security-scanner.md
    shared/
      security-setup.md     ← common modules imported by templates
      mcp/tavily.md
      prompt-templates/

Platform team responsibilities:
  - Tag releases on central repo (enables version pinning by consumers)
  - Mark internal-only templates with private: true
  - Maintain shared/ modules; version them separately
  - Define governance: ownership, update promotion, fork conditions

Consuming team workflow:
  gh aw add acme-org/agentic-workflows/ci-doctor@v1    # install
  # ... make local customizations if needed ...
  gh aw update ci-doctor                               # get upstream improvements
                                                       # (3-way merge preserves customizations)
```

*Source: Sharing Workflows guide, "Enterprise Implementation Pattern" section.*

### Import Caching and Lock File Reproducibility

```
Compilation pipeline (import resolution):

  workflow.md
    ↓ gh aw compile
    → resolves remote imports to exact commit SHAs
    → caches content under .github/aw/imports/<commit-sha>/
    → records SHA pins in workflow.lock.yml

  Result: .lock.yml is self-contained (import SHAs embedded)
          .github/aw/imports/ cache enables offline compilation
          both should be committed to the repository

Benefits:
  - Reproducible: same .lock.yml always compiles to the same executable
  - Offline-capable: cached imports survive upstream changes or outages
  - Dedup: multiple refs pointing to same SHA share one cached copy
  - Auditable: .lock.yml pinned SHAs form a dependency manifest
```

*Source: Sharing Workflows guide, "Import Caching and Lock Files" section.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-agentic-authoring.md` Claim 3 ("create-agentic-agent performs AI-assisted
    one-time cross-repo workflow migration, distinct from gh aw add which provides ongoing
    synchronized reuse"): this source corroborates the `gh aw add` synchronized-reuse
    characterization and adds the full versioning lifecycle (four tiers, update semantics,
    3-way merge) that Claim 3 alludes to but does not detail.
  - `docs-ghaw-how-they-work.md` Claim 7 ("The compilation model separates the editable
    workflow source (.md) from the hardened executable (.lock.yml)"): this source
    corroborates the `.md` → `.lock.yml` model and extends it with the import caching
    layer — `.lock.yml` also pins remote import SHAs, and `.github/aw/imports/` is a
    companion reproducibility artifact that the how-they-work note does not describe.
  - `docs-ghaw-central-repo-ops.md` Claim 7 ("`inlined-imports: true` for cross-org
    deployments … embeds all imported content into the .lock.yml at compile time"):
    this source corroborates the import caching mechanisms and explains why the lock file
    can be made self-contained — the SHA pinning in `.lock.yml` is the base mechanism
    that `inlined-imports` extends.

- **Extends**:
  - `docs-ghaw-agentic-authoring.md` Claim 3: that note introduces the `gh aw add`
    vs. `create-agentic-agent` distinction. This note adds the full versioning lifecycle:
    four reference types, `gh aw update` with 3-way merge, `--no-merge`, `--major`.
    Together they give the complete workflow reuse picture: installation model
    (agentic-authoring) + versioning semantics (this note).
  - `blog-gh-aw-operations-release-workflows.md` Claim 4 ("`gh aw add-wizard` provides
    a wizard-based mechanism for installing pre-built agentic workflows"): that source
    only documents `gh aw add-wizard`. This source adds the scriptable `gh aw add` variant,
    the full four-tier versioning model, and the `gh aw update` lifecycle — converting a
    snapshot of the install command into a complete workflow distribution model.
  - `docs-ghaw-how-they-work.md` Claim 7 (compilation model): that note documents the
    `.md` → `.lock.yml` compilation step. This note adds the import caching semantics
    that are part of the same compilation pipeline: remote imports are resolved to SHAs
    and cached under `.github/aw/imports/`. Together they give the complete picture of
    what compilation produces and commits.

- **Contradicts**: None identified. Reviewed all corpus source notes. No existing claim
  materially opposes the four-tier versioning model, `private: true` access control,
  import caching semantics, or the enterprise central-repo pattern described here. The
  design-time distribution layer documented in this note is the complement to, not a
  contradiction of, the runtime orchestration layer documented in
  `docs-ghaw-central-repo-ops.md`. No contradiction issue needs to be filed.

- **Novel** (what this note adds that no prior source covers):
  - **Four-tier versioning model with `gh aw update` semantics**: No prior corpus source
    documents the exact-tag / moving-major-ref / branch-ref / SHA-pin distinction or
    explains how `gh aw update` behaves differently across these four types. This is the
    most actionable novelty in the source for practitioners managing shared workflow
    versions.
  - **`private: true` as an org governance boundary**: The frontmatter field that blocks
    external installation and enables org-internal catalogs is not documented in any
    existing source note. Prior notes treat workflows as either public or implicitly
    internal; this note introduces the explicit access-control primitive.
  - **Import caching under `.github/aw/imports/`**: The local cache organized by commit
    SHA — enabling offline compilation and deduplication — is not described in any
    existing source note. The `.lock.yml` is covered, but not the companion cache
    directory.
  - **Parameterized shared components via `import-schema` + `uses`/`with`**: The runtime
    parameter injection mechanism for shared imports is entirely new to the corpus. Prior
    notes treat imports as static inclusions.
  - **Scriptable `gh aw add` vs. interactive `gh aw add-wizard`**: The distinction
    between the two installation variants (and the automation-facing use case for `gh aw
    add`) is not documented in prior notes.
  - **`allowed-repos` as a compile-time blast radius control**: The explicit repository
    allowlist in `safe-outputs` configuration for cross-repo execution is documented in
    `docs-ghaw-central-repo-ops.md` only for the runtime case; this note documents it
    as a required field in the sharing/governance layer.
  - **Governance question framing**: The operational governance questions (ownership, fork
    conditions, update promotion, consumption authorization) as the reliability-critical
    layer are articulated here for the first time in the corpus.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add the four-tier versioning model as a workflow distribution decision framework**
  (Claim 2): The guide currently covers how to write workflows but not how to version and
  distribute them at scale. Add the four-tier model with the governance table from Concrete
  Artifacts as a decision aid. Rule of thumb: exact tags or SHA pins for production;
  moving major refs for staging; branch refs for development integration only.

- **Document `gh aw add` + `gh aw update` + 3-way merge as the workflow distribution
  lifecycle** (Claims 1, 3, 10): The complete lifecycle — install with version pin, customize
  locally, update while preserving customizations — is the enterprise pattern for adopting
  shared workflows without losing team-specific adjustments. Add as a pattern alongside
  `create-agentic-agent` (fork model) with explicit decision criteria: use `gh aw add`
  when the team wants to track upstream; use `create-agentic-agent` when substantial local
  customization will diverge from upstream.

- **Add import caching commitment to the reproducibility checklist** (Claim 5): Both
  `.lock.yml` and `.github/aw/imports/` should be committed to the repository. The guide
  currently references the `.lock.yml` commit requirement (via `docs-ghaw-how-they-work.md`
  Claim 7); add the import cache as the companion artifact. Frame this as analogous to
  committing `yarn.lock` — the cache makes builds reproducible and offline-capable.

- **Add parameterized imports (`import-schema` + `uses`/`with`) as the shared-library
  pattern** (Claim 6): Without this pattern, shared components must be forked and
  customized per consumer. With `import-schema`, a single shared component handles
  multiple configuration profiles. Add to the harness composability section as the
  preferred pattern for building modular workflow libraries.

### Chapter 05: Team Adoption / Organizational Patterns

- **Add `private: true` and the org-internal catalog model** (Claim 4): For organizations
  building curated internal catalogs, `private: true` on internal-only workflows (combined
  with private/internal repository visibility) is the access control primitive. Document
  the two-layer model: repository visibility (who can see) + `private:` frontmatter (who
  can install). Recommend that platform teams mark all internal-only workflows `private: true`
  by default and explicitly remove it only when distributing externally.

- **Add the enterprise central-repo pattern as the recommended starting architecture**
  (Claim 8): The five-element pattern (central repo, versioned templates, shared modules,
  `gh aw add` installation, `private: true` governance) is the concrete enterprise
  recommendation. Frame it explicitly alongside the runtime CentralRepoOps pattern from
  `docs-ghaw-central-repo-ops.md` to distinguish design-time distribution concerns from
  runtime orchestration concerns — teams frequently conflate the two.

- **Use the governance question list as an adoption policy template** (Claim 9): The six
  operational governance questions (ownership, change review, testing/tagging/promotion,
  consumption authorization, secret/permission standardization, fork conditions) are a
  practical policy template. Add to Ch05 as a checklist for organizations standing up a
  shared agentic workflow program. Emphasize the platform team's finding that these
  decisions "impact reliability more substantially than technical file formats."

### Chapter 03: Safety and Verification

- **Add `allowed-repos` as a required blast radius control for cross-repository workflows**
  (Claim 7): The explicit repository allowlist in `safe-outputs` is a compile-time-enforced
  boundary on which repositories a workflow can modify. Extend the Ch03 discussion of blast
  radius control (currently centered on `max` in `dispatch-workflow` from
  `docs-ghaw-central-repo-ops.md` Claim 2) with the complementary allowlist dimension:
  fan-out is bounded by count (`max`) AND by destination (`allowed-repos`). Both fields
  should be treated as security requirements.

## Extraction Notes

1. **Source is the distribution/governance layer, not the orchestration layer**: Per
   Prospector guidance, this source was extracted with explicit scope focus on the
   design-time concerns (versioning, packaging, governance, access control) rather than
   runtime orchestration (that is `docs-ghaw-central-repo-ops.md`). The `imports:`
   subsystem is present on this page but was not extracted in depth — that is covered
   by issue #298.

2. **Platform caveat noted**: The page explicitly states "recommended patterns, commands,
   and configuration options may change." All CLI-specific claims (flags, command syntax)
   are marked `emerging` for this reason. Platform-enforced fields (`allowed-repos`,
   `private:`) are marked `settled`.

3. **No publication date**: The documentation page does not carry an explicit publication
   date. `date_published` is left null. Content is consistent with gh-aw documentation
   as of the 2026-05-02 extraction date.

4. **Cross-repository execution section scope**: Claim 7 extracts the `safe-outputs`
   `allowed-repos` pattern from the "Cross-Repository Execution" section. This section
   also covers reading files and metadata from other repos and checking out code from
   target repos — these are consistent with `docs-ghaw-central-repo-ops.md`'s
   Orchestrator+Worker checkout patterns and were not separately extracted to avoid
   duplication.

5. **No contradictions filed**: Reviewed all existing source notes. No claims in this
   source materially oppose existing source notes. The design-time distribution layer
   (this note) and the runtime orchestration layer (`docs-ghaw-central-repo-ops.md`) are
   complementary, not contradictory. No contradiction issue filed.
