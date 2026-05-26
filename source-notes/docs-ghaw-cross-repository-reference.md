---
source_url: https://github.github.com/gh-aw/reference/cross-repository
source_type: docs
title: "GitHub Agentic Workflows: Cross-Repository Operations Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-26
last_checked: 2026-05-26
status: current
confidence_overall: emerging
issue: "#376"
---

# GitHub Agentic Workflows: Cross-Repository Operations Reference

> A consolidated reference for all declarative cross-repo frontmatter in
> gh-aw — introduces the three-category taxonomy (Checkout / Reading / Safe
> Outputs), the `tools.github.allowed-repos` access control for toolset reads,
> the dynamic `target-repo: "*"` mode with its unsupported-operation list, and
> the `push-to-pull-request-branch` checkout constraint that earlier
> pattern-level notes left undocumented.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/cross-repository`
  page — in the same `reference/` section as `reference/checkout` covered by
  `docs-ghaw-checkout-reference.md`. This is a specification-level reference
  document, not a tutorial or pattern guide. It serves as the consolidated
  single-page overview for all declarative cross-repo configuration.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind Peli de Halleux's agent factory blog series and the
  `gh aw` platform. Claims about frontmatter schema, toolset access controls,
  and safe-output limitations are authoritative for this platform.
- **Scope**: All declarative cross-repo frontmatter features: checkout
  configuration for external repos, GitHub toolset read access controls
  (`tools.github.allowed-repos`), and cross-repo safe-output configuration
  (`target-repo`, `target-repo: "*"`, `allowed-repos`). Also documents
  practical patterns (Monorepo Development, Scheduled PR Branch Updates,
  Deterministic Multi-Repo Workflows). Does NOT cover: the MultiRepoOps
  topology archetypes in depth (hub-and-spoke, upstream-to-downstream,
  org-wide broadcast — see `docs-ghaw-multi-repo-ops.md`), the CentralRepoOps
  Orchestrator+Worker pattern (`docs-ghaw-central-repo-ops.md`), the full
  checkout field reference (`docs-ghaw-checkout-reference.md`), or the Safe
  Outputs MCP Gateway specification (`docs-ghaw-safe-outputs-specification.md`).

## Extracted Claims

### Claim 1: Cross-repository operations in gh-aw are classified into three mutually exclusive categories: Checkout, Reading, and Safe Outputs

- **Evidence**: The page's overview section opens with an explicit taxonomy:
  "Cross-repository features fall into three categories: 1. Cross-Repository
  Checkout — Check out code from other repositories 2. Cross-Repository
  Reading — Read issues, pull requests and other information from other
  repositories 3. Cross-Repository Safe Outputs — Create issues, PRs,
  comments, and other resources in external repositories using `target-repo`
  and `allowed-repos` in safe outputs." Each category has its own dedicated
  configuration path (checkout frontmatter, tools.github config, and
  safe-outputs frontmatter respectively).
- **Confidence**: settled (first-party documentation; the taxonomy is stated
  as the organizing principle of the page)
- **Quote**: "Cross-repository features fall into three categories: 1.
  Cross-Repository Checkout - Check out code from other repositories 2.
  Cross-Repository Reading - Read issues, pull requests and other information
  from other repositories 3. Cross-Repository Safe Outputs - Create issues,
  PRs, comments, and other resources in external repositories using
  `target-repo` and `allowed-repos` in safe outputs"
- **Our assessment**: This taxonomy clarifies that cross-repo capability is
  not a single switch but three distinct layers with separate configuration
  paths. A workflow may need all three (check out code, read issues from
  another repo, create a PR in a third repo) or only one. The categorization
  is a useful mental model for practitioners: when something doesn't work,
  which category's configuration needs attention? It also clarifies that
  `target-repo` (safe outputs) is separate from checkout — checking out a
  repo does not grant safe-output write permission, and vice versa. For Ch02
  (Harness Engineering): present cross-repo configuration through this
  three-category lens so practitioners can reason about each boundary
  independently.

### Claim 2: `tools.github.allowed-repos` restricts which repositories the agent can access through GitHub toolset calls, with five distinct value types

- **Evidence**: The page documents the field explicitly: "The setting
  `tools.github.allowed-repos` specifies which repositories the agent can
  access through GitHub tools: `"all"` — All repositories accessible by the
  configured token; `"public"` — Public repositories only; `"current"` — The
  repository where the workflow is running; `"${{ github.repository }}"` —
  Equivalent to `"current"`; Array of patterns — Specific repositories and
  wildcards: `"owner/repo"` (exact match), `"owner/*"` (all repos under an
  owner), `"owner/prefix*"` (repos with a name prefix under an owner)."
- **Confidence**: settled (first-party reference documentation; the value
  types are explicitly enumerated)
- **Quote**: "The setting `tools.github.allowed-repos` specifies which
  repositories the agent can access through GitHub tools"
- **Our assessment**: This is a defence-in-depth control for the GitHub
  toolset that operates independently of the PAT scope. An agent can be
  granted a broadly scoped PAT but still be restricted to reading only
  `current` or a specific list of repos via `tools.github.allowed-repos`.
  The wildcard patterns (`owner/*`, `owner/prefix*`) are significant: they
  allow org-wide read access scoped to one owner without listing every repo.
  The `${{ github.repository }}` form is useful for templates that need to
  be self-referential without hardcoding the repo name. For Ch03 (Safety and
  Verification): `tools.github.allowed-repos` should be documented as an
  explicit access control layer separate from PAT scoping — a cross-repo
  workflow should configure both a narrowly scoped PAT (what the token can
  access) and a narrowly scoped `allowed-repos` (what the agent is permitted
  to query).

### Claim 3: Setting `target-repo: "*"` enables dynamic runtime repository selection, where the agent supplies the target repository via a `repo` parameter in its tool call

- **Evidence**: The page states: "Set `target-repo: "*"` to allow the agent
  to dynamically target any repository at runtime. When configured, the agent
  receives a `repo` parameter in its tool call where it supplies the target
  repository in `owner/repo` format."
- **Confidence**: settled (first-party documentation; the mechanism is
  explicitly described)
- **Quote**: "Set `target-repo: "*"` to allow the agent to dynamically target
  any repository at runtime."
- **Our assessment**: `target-repo: "*"` shifts repository selection from
  compile-time (declared in frontmatter) to runtime (decided by the agent
  during execution). This is a significant capability for workflows that must
  determine the target programmatically — for example, an orchestrator that
  routes output to whichever repo owns a failing component. The trade-off is
  reduced static auditability: the frontmatter no longer declares the exact
  target, so automated tooling cannot determine in advance which repos the
  workflow can affect. This is why the dynamic mode is restricted to specific
  safe-output types (see Claim 4). For Ch02: `target-repo: "*"` is the correct
  choice when the target repo is determined by the agent's analysis, not
  pre-configured — but it should be paired with `allowed-repos` to limit the
  universe of possible targets.

### Claim 4: Five safe-output types do not support `target-repo: "*"` dynamic targeting: `create-pull-request-review-comment`, `reply-to-pull-request-review-comment`, `submit-pull-request-review`, `create-agent-session`, and `manage-project-items`

- **Evidence**: The page explicitly names the exclusions: "The following
  safe-output types do **not** support `target-repo: "*"`:
  `create-pull-request-review-comment`,
  `reply-to-pull-request-review-comment`, `submit-pull-request-review`,
  `create-agent-session`, and `manage-project-items`."
- **Confidence**: settled (first-party documentation; exclusions are
  explicitly enumerated)
- **Quote**: "The following safe-output types do not support
  `target-repo: \"*\"`: `create-pull-request-review-comment`,
  `reply-to-pull-request-review-comment`, `submit-pull-request-review`,
  `create-agent-session`, and `manage-project-items`."
- **Our assessment**: The excluded types share a common characteristic: they
  operate on existing resources that are tightly bound to a specific context
  (a PR review thread, an agent session, a project board). Dynamic targeting
  for these types would require resolving that context across an unknown repo
  at runtime, which is not safe. The exclusion of `create-agent-session` is
  particularly important: orchestrators that use dynamic targeting cannot
  spin up sub-agents in dynamically-selected repos — agent session creation
  must be statically targeted. For Ch04 (Multi-Agent Architecture): document
  this constraint when covering orchestrators that dispatch sub-agents
  dynamically. If the orchestrator needs to create agent sessions in
  different repos, it must enumerate those repos in static `target-repo`
  declarations, not use `target-repo: "*"`.

### Claim 5: `push-to-pull-request-branch` with `target-repo` requires the target repository to be locally checked out with a `path:` specified — unlike all other safe-output types with cross-repo targets

- **Evidence**: The page states: "Unlike other safe output types,
  `push-to-pull-request-branch` with `target-repo` requires the target
  repository to be **checked out into the workflow workspace** using the
  `checkout:` frontmatter field with a `path:` specified. Without a checkout,
  the agent has no local git history to create and push a patch from."
- **Confidence**: settled (first-party documentation; the requirement is
  explicitly stated with the technical reason)
- **Quote**: "Unlike other safe output types, `push-to-pull-request-branch`
  with `target-repo` requires the target repository to be checked out into
  the workflow workspace using the `checkout:` frontmatter field with a
  `path:` specified."
- **Our assessment**: This is the most important footgun in the
  cross-repository safe-outputs section. All other safe-output types with
  `target-repo` operate through the GitHub API (no local content needed);
  `push-to-pull-request-branch` is unique in requiring a local git clone
  because it operates on git history to create the patch. The Scheduled PR
  Branch Updates example (Concrete Artifacts) shows the correct paired
  configuration: `checkout:` with `fetch: ["refs/pulls/open/*"]` on the
  target repo, plus `push-to-pull-request-branch.target-repo` in
  `safe-outputs`. Omitting the checkout step causes runtime failure, not a
  configuration-time error. For Ch02: document this as a required pairing
  rule — if `push-to-pull-request-branch` is used with `target-repo`, the
  same target repo must appear in the `checkout:` array with a `path:`
  field.

### Claim 6: When `allowed-repos` is specified on a safe-output type, the agent can include a `repo` field to select the destination; the `target-repo` value is always implicitly allowed

- **Evidence**: The page states: "When `allowed-repos` is specified: The
  agentic step can include a `repo` field to select which repository. Target
  repository (from `target-repo` or current repo) is always implicitly
  allowed. Creates a union of allowed destinations."
- **Confidence**: settled (first-party documentation; the implicit inclusion
  rule is explicitly stated)
- **Quote**: "Target repository (from `target-repo` or current repo) is
  always implicitly allowed"
- **Our assessment**: The implicit inclusion of `target-repo` in the
  `allowed-repos` set is a safety design: it prevents a misconfiguration
  where the default target is not in the allowlist, which would break all
  same-target operations. The "union of allowed destinations" framing means
  `allowed-repos` always adds to — never replaces — the default target. For
  Ch03 (Safety and Verification): document `allowed-repos` on safe-outputs
  as a cumulative allowlist, not a whitelist that replaces `target-repo`. A
  workflow with `target-repo: "org/main-repo"` and `allowed-repos: ["org/alt-repo"]`
  permits output to both `org/main-repo` AND `org/alt-repo`.

### Claim 7: Cross-repo reading via GitHub tools requires explicit `github-token` configuration in `tools.github`; the same `allowed-repos` filter applies to all toolset reads using that token

- **Evidence**: The Cross-Repository Reading section documents the
  configuration pattern: a PAT or GitHub App token configured via
  `tools.github.github-token` enables reading from private repositories
  across repos, issues, PRs, commits, releases, workflow runs, and
  organization information. The `tools.github.allowed-repos` restriction
  applies to the configured token's access, scoping the agent's queries
  regardless of the token's intrinsic scope.
- **Confidence**: settled (corroborated by `docs-ghaw-multi-repo-ops.md`
  Claim 3 which confirms the GITHUB_TOKEN limitation; this page provides
  the complementary `allowed-repos` filter detail)
- **Quote**: (no direct quote capturing both points together; see paraphrase
  in Our assessment)
- **Our assessment**: The two-layer cross-repo read control — PAT scope (what
  the token CAN access) plus `allowed-repos` filter (what the agent is
  PERMITTED to query) — is important for defense in depth. A broadly scoped
  PAT can be narrowed by `allowed-repos` without changing the PAT itself.
  This complements `docs-ghaw-multi-repo-ops.md` Claim 3 (GITHUB_TOKEN is
  current-repo only, explicit auth required for cross-repo reads) by showing
  that even after adding cross-repo auth, the `allowed-repos` filter can
  restrict what the agent actually queries. For Ch03: both layers should
  appear in security guidance for cross-repo workflows.

### Claim 8: The Scheduled PR Branch Updates pattern combines cross-repo checkout with `fetch: ["refs/pulls/open/*"]` plus `push-to-pull-request-branch` safe output to automate maintenance across all open PRs in an external repository

- **Evidence**: The page provides a complete YAML example (reproduced in
  Concrete Artifacts) showing a scheduled workflow that checks out
  `org/target-repo` with `fetch: ["refs/pulls/open/*"]`, marks it
  `current: true`, and uses `push-to-pull-request-branch` in safe-outputs
  to push changes back to PR branches. This combines the cross-repo checkout
  and safe-output categories for a complete maintenance automation flow.
- **Confidence**: emerging (pattern is documented with complete YAML; the
  specific maintenance use case depends on the agent's instructions)
- **Quote**: (no direct prose quote; see Concrete Artifacts for verbatim YAML)
- **Our assessment**: This pattern is the most operationally novel example in
  the source. It shows that `fetch: ["refs/pulls/open/*"]` (fetching all open
  PR branches, documented in `docs-ghaw-checkout-reference.md` Claim 4) can
  be applied to a cross-repo checkout — enabling an agent to inspect and
  modify all open PR branches in an external repository on a schedule. This
  is a complete pattern for automation that doesn't fit neatly into the
  MultiRepoOps or CentralRepoOps paradigms: it's not about routing issues
  between repos, it's about maintaining the state of PR branches in an
  external repo as a scheduled operation. For Ch06 (Orchestration): add this
  as a concrete example of scheduled cross-repo maintenance that spans the
  Checkout + Safe Outputs categories.

## Concrete Artifacts

### Three-Category Cross-Repository Operations Summary

From the page's overview section.

```
Category                   | Frontmatter Config Location        | Operation Direction
───────────────────────── | ─────────────────────────────────── | ──────────────────
Cross-Repository Checkout  | checkout: [ {repository: ..., ...} ] | Read (local access to files)
Cross-Repository Reading   | tools.github.allowed-repos: [...]   | Read (API queries)
Cross-Repository Safe Outputs | safe-outputs: {target-repo: ..., allowed-repos: [...]} | Write (issues, PRs, comments)
```

### `tools.github` Cross-Repo Read Configuration

From the Cross-Repository Reading section.

```yaml
tools:
  github:
    toolsets: [repos, issues, pull_requests]
    github-token: ${{ secrets.CROSS_REPO_PAT }}
    allowed-repos:
      - "myorg/*"
      - "partner/shared-repo"
```

*Source: Cross-Repository Reference, "Cross-Repository Reading" section.*

### `tools.github.allowed-repos` Value Reference

From the page's "Restricting Repository Access" section.

```
Value                        | Effect
──────────────────────────── | ────────────────────────────────────────────
"all"                        | All repos accessible by the configured token
"public"                     | Public repositories only
"current"                    | The repo where the workflow runs
"${{ github.repository }}"   | Equivalent to "current"
"owner/repo"                 | Exact repository match
"owner/*"                    | All repos under an owner
"owner/prefix*"              | Repos with a name prefix under an owner
```

*Source: Cross-Repository Reference, "Restricting Repository Access" section.*

### Dynamic `target-repo: "*"` Configuration

From the "Dynamic Target Repository" section.

```yaml
safe-outputs:
  github-token: ${{ secrets.CROSS_REPO_PAT }}
  create-issue:
    target-repo: "*"
```

*Note: Not supported by: `create-pull-request-review-comment`,
`reply-to-pull-request-review-comment`, `submit-pull-request-review`,
`create-agent-session`, `manage-project-items`.*

*Source: Cross-Repository Reference, "Dynamic Target Repository" section.*

### Multiple Allowed Repos with Agent Selection

From the "Multiple Allowed Repositories" section.

```yaml
safe-outputs:
  github-token: ${{ secrets.CROSS_REPO_PAT }}
  create-issue:
    target-repo: "org/default-repo"
    allowed-repos: ["org/repo-a", "org/repo-b"]
```

*When `allowed-repos` is specified, the agent can include a `repo` field to
select the destination. `target-repo` is always implicitly allowed (union
semantics).*

*Source: Cross-Repository Reference, "Multiple Allowed Repositories" section.*

### Scheduled PR Branch Updates — Complete Workflow YAML

From the page's "Scheduled PR Branch Updates" example section.

```yaml
---
on:
  schedule: hourly

checkout:
  - repository: org/target-repo
    github-token: ${{ secrets.GH_AW_SIDE_REPO_PAT }}
    fetch: ["refs/pulls/open/*"]
    current: true

permissions:
  contents: read

safe-outputs:
  github-token: ${{ secrets.GH_AW_SIDE_REPO_PAT }}
  push-to-pull-request-branch:
    target-repo: "org/target-repo"
---
# Auto-Update PR Branches
Check open pull requests in org/target-repo and apply any pending automated
updates to each PR branch.
```

*Source: Cross-Repository Reference, "Scheduled PR Branch Updates" example.*

### Monorepo Development — Multiple Checkout with Sparse Checkout

From the page's "Monorepo Development" example section.

```yaml
checkout:
  - fetch-depth: 0
  - repository: org/shared-libs
    path: ./libs/shared
    ref: main
  - repository: org/config-repo
    path: ./config
    sparse-checkout: |
      defaults/
      overrides/
```

*Source: Cross-Repository Reference, "Monorepo Development" example.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-multi-repo-ops.md` Claim 1 ("`target-repo` parameter on safe
    outputs is the primary primitive for cross-repository coordination"):
    this page is the companion reference for `target-repo`, confirming its
    role and adding the dynamic `target-repo: "*"` variant and the
    `allowed-repos` union semantics.
  - `docs-ghaw-multi-repo-ops.md` Claim 3 ("default `GITHUB_TOKEN` only has
    access to the current repository — cross-repo reads silently fail without
    additional authentication"): this page corroborates the requirement for
    explicit `github-token` in `tools.github` and adds `allowed-repos` as a
    second access-control layer.
  - `docs-ghaw-sharing-workflows.md` Claim 7 ("Cross-repository operations
    require appropriate GitHub token permissions and explicit `allowed-repos`
    declarations"): this page corroborates the `allowed-repos` requirement
    and clarifies that `target-repo` is always implicitly included in the
    allowed set (union semantics not documented in the sharing-workflows note).
  - `docs-ghaw-checkout-reference.md` Claim 3 (multiple repos with array
    syntax): this page corroborates the array checkout form and shows its
    application in cross-repo scenarios.
  - `docs-ghaw-checkout-reference.md` Claim 4 (`fetch: "refs/pulls/open/*"`
    shorthand for all open PR head refs): the Scheduled PR Branch Updates
    example corroborates this pattern in the context of a cross-repo checkout
    workflow.

- **Extends**:
  - `docs-ghaw-multi-repo-ops.md`: that note covers static `target-repo`
    (declared in frontmatter, fixed at compile time). This page extends it
    with dynamic `target-repo: "*"` (selected by agent at runtime), the
    explicit list of types excluded from dynamic targeting, and the
    `allowed-repos` union semantics.
  - `docs-ghaw-checkout-reference.md`: that note covers the `checkout:`
    field in full including `fetch: refs/pulls/open/*`. This page extends
    it with the cross-repo application: `fetch: refs/pulls/open/*` on a
    non-default `repository:` entry, combined with
    `push-to-pull-request-branch`, as a complete pattern.
  - `docs-ghaw-sharing-workflows.md` Claim 7: that note documents
    `allowed-repos` as a required field for cross-repo execution but doesn't
    clarify the union semantics (target-repo is always implicitly allowed)
    or the agent `repo` field for dynamic destination selection.

- **Contradicts**: None identified. All claims in this source are consistent
  with existing source notes. The `target-repo: "*"` dynamic mode is new
  information, not a contradiction of static `target-repo` guidance. No
  contradiction issue filed.

- **Novel** (what this page adds that no prior source note covers):
  - **Three-category taxonomy** (Claim 1): Checkout / Reading / Safe Outputs
    as the organizing framework for cross-repo configuration is not articulated
    in any existing source note. Prior notes treat the categories separately
    without a unifying taxonomy.
  - **`tools.github.allowed-repos` with specific value types** (Claim 2):
    The five value forms ("all", "public", "current", expression,
    pattern array) for restricting GitHub toolset access are not documented
    in any existing note. Prior notes cover `github-token` in `tools.github`
    but not the access-restriction side.
  - **`target-repo: "*"` dynamic mode** (Claim 3): Not documented in any
    existing source note. Prior notes treat `target-repo` as a static
    frontmatter field.
  - **Operations excluded from dynamic targeting** (Claim 4): The explicit
    list of five excluded safe-output types is entirely new to the corpus.
  - **`push-to-pull-request-branch` checkout requirement** (Claim 5):
    The constraint that this safe-output type requires a local checkout with
    `path:` when used with `target-repo` is not mentioned in any existing note.
  - **`allowed-repos` union semantics and agent `repo` field** (Claim 6):
    The rule that `target-repo` is always implicitly included in `allowed-repos`
    (union, not override), and that the agent can supply a `repo` field at
    runtime, is not documented in any existing note.
  - **Scheduled PR Branch Updates pattern** (Claim 8): The combined
    cross-repo checkout + `fetch: refs/pulls/open/*` + `push-to-pull-request-branch`
    pattern for scheduled PR maintenance automation is new to the corpus.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add three-category cross-repo framework** (Claim 1): When documenting
  cross-repo configuration, structure guidance around the three categories
  (Checkout, Reading, Safe Outputs) with separate subsections. This clarifies
  that each category has its own configuration path and that they can be
  combined independently.

- **Add `tools.github.allowed-repos` as a toolset access control** (Claim 2):
  The guide currently documents `tools.github.github-token` for cross-repo
  read auth (via `docs-ghaw-multi-repo-ops.md` Claim 9). Add `allowed-repos`
  as the companion restriction field — practitioners should configure both:
  a narrowly scoped PAT (capacity) and `allowed-repos` (policy). Document
  the five value types with the wildcard pattern examples.

- **Add `target-repo: "*"` dynamic mode with excluded-operations list**
  (Claims 3 and 4): Document dynamic targeting as an advanced option for
  workflows where the target is determined at runtime. Always pair with
  `allowed-repos` to bound the universe of possible targets. Include the
  list of excluded safe-output types as a required callout — the five
  excluded types are not obvious from the `target-repo: "*"` syntax alone.

- **Add `push-to-pull-request-branch` pairing rule** (Claim 5): Add a
  prominent note that this safe-output type is unique in requiring a local
  checkout with `path:` specified. The Scheduled PR Branch Updates YAML
  (Concrete Artifacts) is the canonical reference configuration.

### Chapter 03: Safety and Verification

- **Add `tools.github.allowed-repos` to the cross-repo security checklist**
  (Claims 2 and 7): Extend the pre-flight security checklist for cross-repo
  workflows (currently: configure explicit PAT, avoid GITHUB_TOKEN) with a
  third requirement: set `tools.github.allowed-repos` to the minimum necessary
  scope. Document the two-layer model: PAT scope (token capability) +
  `allowed-repos` (agent permission) as complementary controls.

- **Clarify `allowed-repos` union semantics** (Claim 6): The guide currently
  describes `allowed-repos` as a whitelist without clarifying the union
  semantics. Add the note that `target-repo` is always implicitly included —
  this prevents confusing misconfiguration where practitioners think
  `allowed-repos` replaces rather than extends `target-repo`.

### Chapter 06: Orchestration

- **Add Scheduled PR Branch Updates as a cross-repo maintenance pattern**
  (Claim 8): The guide covers event-driven and schedule-driven orchestration.
  Add this pattern as the canonical example of scheduled cross-repo maintenance
  automation: check out an external repo with all open PR branches, let the
  agent analyze and update them, push changes back via `push-to-pull-request-branch`.
  This complements the MultiRepoOps (event-driven) and CentralRepoOps
  (dispatch-driven) patterns with a scheduled-read-and-modify pattern.

### Chapter 04: Multi-Agent Architecture

- **Add `create-agent-session` exclusion from dynamic targeting** (Claim 4):
  The guide may document orchestrators that use dynamic `target-repo` to route
  work. Add an explicit constraint: `create-agent-session` cannot use dynamic
  targeting, so multi-agent workflows that spin up sub-agents in
  dynamically-selected repos must use static `target-repo` declarations per
  repo. This is an architectural constraint for dynamic orchestrators.

## Extraction Notes

1. **Source is a reference/consolidation page**: Per the Prospector's triage,
   this page consolidates patterns already documented in detail in
   `docs-ghaw-multi-repo-ops.md` and `docs-ghaw-central-repo-ops.md`. The
   extraction focused on claims NOT already documented in those notes —
   particularly the three-category taxonomy, `tools.github.allowed-repos`,
   `target-repo: "*"`, the dynamic-targeting exclusion list, the
   push-to-PR-branch checkout constraint, and the `allowed-repos` union
   semantics. The MultiRepoOps topologies and authentication model were
   not re-extracted.

2. **WebFetch content verified for key quotes**: Key verbatim passages were
   verified with a second fetch that requested exact text. The YAML blocks
   in Concrete Artifacts are reproduced as returned by the fetch tool.
   Minor formatting differences (e.g., `on: schedule: hourly` vs. full cron
   syntax) reflect how the page represents shorthand schedule notation; verify
   against current gh-aw documentation before use in production.

3. **No explicit publication date**: The documentation page does not carry a
   publication date. `date_published` is null. Content is consistent with
   gh-aw documentation as of the 2026-05-26 extraction date.

4. **`docs-ghaw-multi-repo-ops.md` Extraction Note 4 specifically called out
   this page as un-fetched**: That note's Extraction Notes item 4 reads:
   "Sub-pages not followed: The page links to 'Feature Synchronization' and
   'Cross-Repo Issue Tracking' example pages, plus the Cross-Repository
   Operations reference and the GitHub App auth guide." This source note fills
   that explicitly identified gap.

5. **No contradictions filed**: Reviewed all existing corpus source notes. No
   claims in this source materially oppose existing source notes. `target-repo: "*"`
   is an extension of static `target-repo`, not a contradiction. No
   contradiction issue filed.
