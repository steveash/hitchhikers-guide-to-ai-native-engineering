---
source_url: https://github.github.com/gh-aw/reference/cross-repository
source_type: docs
title: "GitHub Agentic Workflows: Cross-Repository Operations Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#376"
---

# GitHub Agentic Workflows: Cross-Repository Operations Reference

> A reference-layer consolidation of all cross-repository primitives in gh-aw —
> the primary novel contributions are the `target-repo: "*"` wildcard syntax,
> the five safe output types that explicitly do NOT support wildcard, and the
> `push-to-pull-request-branch` checkout requirement that distinguishes it from
> all other safe output types. The five concrete examples (monorepo, hub-and-spoke,
> cross-repo analysis, deterministic multi-repo, scheduled PR-branch update) add
> extractable YAML for patterns covered conceptually in the pattern notes.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, `reference/`
  section — a specification-level reference page, distinct from the
  pattern-focused `patterns/` pages such as `multi-repo-ops` and `central-repo-ops`.
  This page consolidates cross-repository behavior across three subsystems:
  `checkout:`, GitHub Tools authentication, and `safe-outputs`.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind Peli de Halleux's agent factory blog series and the
  `gh aw` platform. Claims about field semantics, wildcard support, and safe
  output type constraints are authoritative for this platform.
- **Scope**: The complete cross-repository operations surface for gh-aw —
  multi-repo `checkout:` (covered more fully in `docs-ghaw-checkout-reference.md`),
  GitHub Tools authentication for cross-repo reads, and `safe-outputs` with
  `target-repo` / `target-repo: "*"` / `allowed-repos`. Includes five concrete
  workflow examples. Does NOT cover: single-repo operations, MCP server
  configuration (`docs-ghaw-mcps.md`), the full Safe Outputs specification
  (`docs-ghaw-safe-outputs-specification.md`), or multi-repo orchestration
  patterns (`docs-ghaw-multi-repo-ops.md`, `docs-ghaw-central-repo-ops.md`).

## Extracted Claims

### Claim 1: `target-repo: "*"` wildcard enables agent-selected dynamic repository targeting at runtime, without requiring the destination to be known at workflow-authoring time

- **Evidence**: The page documents the wildcard form as a configuration option
  for safe outputs alongside the explicit `target-repo: "org/tracking-repo"`
  form and the `allowed-repos` list form. A concrete YAML example shows:
  ```yaml
  safe-outputs:
    github-token: ${{ secrets.CROSS_REPO_PAT }}
    create-issue:
      target-repo: "*"
      title-prefix: "[component] "
  ```
  The Prospector triage comment also identifies this as a scenario not yet
  documented in the pattern notes.
- **Confidence**: emerging (first-party documentation; wildcard semantics are
  described but the exact runtime mechanism for agent-specified target selection
  is not detailed on this page)
- **Quote**: (no direct quote for the wildcard mechanism; see YAML artifact and
  paraphrase in Our assessment)
- **Our assessment**: The wildcard `"*"` form is architecturally distinct from
  the explicit `target-repo` form. With an explicit value, the workflow author
  fixes the destination at authoring time. With `"*"`, the agent determines the
  destination at runtime (presumably via a structured field in its output). This
  enables agents that discover target repositories dynamically — for example, an
  analysis agent that finds the relevant repository from issue content and writes
  output there. For Ch02 (Harness Engineering): document both forms with explicit
  guidance on when to use each. `"*"` is more powerful but exposes a larger
  surface — it should be paired with `allowed-repos` to bound the set of eligible
  destinations.

### Claim 2: Five safe output types explicitly do NOT support `target-repo: "*"` wildcard — they require an explicit repository value or allowlist

- **Evidence**: The page contains a caution explicitly naming five types that
  do not support the wildcard: `create-pull-request-review-comment`,
  `reply-to-pull-request-review-comment`, `submit-pull-request-review`,
  `create-agent-session`, and `manage-project-items`. All other safe output
  types do support wildcard targeting.
- **Confidence**: settled (first-party documentation; the types are explicitly
  enumerated in a caution block)
- **Quote**: (no single-sentence verbatim quote; the caution names the five
  types; see list in Our assessment)
- **Our assessment**: The five excluded types share a common characteristic:
  they are operations that modify or create content within an existing PR, review,
  session, or project — contexts where the repository identity is typically known
  from the event trigger, not discovered dynamically. The exclusion is architecturally
  coherent: wildcard makes sense for "create a new issue wherever the agent decides";
  it makes less sense for "add a review comment to a PR" where the PR's repository
  is already established. For Ch02: document the five exclusions explicitly — a
  workflow that uses `target-repo: "*"` on a `submit-pull-request-review` output
  will fail at runtime, not at compile time.

### Claim 3: `push-to-pull-request-branch` is the only safe output type that requires the target repository to be checked out into the workspace with `path:` specified

- **Evidence**: The page states: "Unlike other safe output types,
  push-to-pull-request-branch with target-repo requires the target repository
  to be checked out into the workflow workspace using the checkout: frontmatter
  field with a path: specified. Without a checkout, the agent has no local git
  history to create and push a patch from."
- **Confidence**: settled (first-party documentation; constraint is explicitly
  stated as unlike other safe output types)
- **Quote**: "Unlike other safe output types, push-to-pull-request-branch with
  target-repo requires the target repository to be checked out into the workflow
  workspace using the checkout: frontmatter field with a path: specified. Without
  a checkout, the agent has no local git history to create and push a patch from."
- **Our assessment**: This is the most actionable novel claim in this source.
  All other safe output types work with only token-level authentication — the
  Safe Output Processor calls the GitHub API to create issues, comments, PRs, etc.
  without needing a local workspace. `push-to-pull-request-branch` is fundamentally
  different: it pushes git commits, which requires local git history. Without the
  checkout, there is no local tree to diff against or push from. The complete
  example (Concrete Artifacts → Scheduled Push to PR Branch) shows the required
  configuration: `checkout:` with `fetch: ["refs/pulls/open/*"]` and `current: true`
  alongside `safe-outputs: push-to-pull-request-branch: target-repo:`. For Ch02:
  document `push-to-pull-request-branch` separately from other safe output types
  with the checkout requirement as a mandatory pre-condition.

### Claim 4: `allowed-repos` creates a union of allowed destinations that always implicitly includes the target-repo (or current repo if no target-repo is set)

- **Evidence**: The page documents the union semantics: "When allowed-repos is
  specified: Agent can include a repo field in output to select which repository;
  Target repository (from target-repo or current repo) is always implicitly
  allowed; Creates a union of allowed destinations."
- **Confidence**: emerging (first-party documentation; union semantics are
  described in a bulleted list format)
- **Quote**: "Target repository (from target-repo or current repo) is always
  implicitly allowed"
- **Our assessment**: The implicit inclusion of the target-repo in the allowed
  set is important — specifying `allowed-repos` does not replace the target-repo,
  it adds to it. A workflow with `target-repo: "org/primary-repo"` and
  `allowed-repos: ["org/repo-a", "org/repo-b"]` allows writes to three
  repositories: primary-repo, repo-a, and repo-b. The agent can choose any of the
  three via a `repo` field in its output. This is more flexible than a fixed
  target but narrower than the full wildcard. For Ch02: document `allowed-repos`
  as the "curated multi-target" pattern — more flexible than a fixed target, more
  bounded than `"*"`. The implicit inclusion of the default target means the
  existing target-repo behavior is preserved.

### Claim 5: Without `target-repo`, safe outputs operate on the workflow's own repository — the explicit parameter is required to write to any external repository

- **Evidence**: The page states: "Without target-repo, safe outputs operate on
  the repository where the workflow is running."
- **Confidence**: settled (consistent with `docs-ghaw-multi-repo-ops.md` Claim 2;
  first-party documentation)
- **Quote**: "Without target-repo, safe outputs operate on the repository where
  the workflow is running."
- **Our assessment**: Corroborates the same statement documented in
  `docs-ghaw-multi-repo-ops.md` Claim 2. The reference page repeats this as a
  default-behavior note at the beginning of the safe outputs section, reinforcing
  that cross-repo is always an explicit opt-in. No new information — included as
  a corroboration anchor.

### Claim 6: GitHub Tools cross-repo reads require explicit additional authentication — either a PAT, GitHub App token, or `GH_AW_GITHUB_MCP_SERVER_TOKEN` — separate from the safe-outputs `github-token`

- **Evidence**: The page documents the tools configuration pattern for cross-repo
  reads:
  ```yaml
  tools:
    github:
      toolsets: [repos, issues, pull_requests]
      github-token: ${{ secrets.CROSS_REPO_PAT }}
  ```
  And references three authentication options for cross-repo reading: "Configure
  a PAT or GitHub App in your GitHub Tools configuration" and mentions the magic
  secret `GH_AW_GITHUB_MCP_SERVER_TOKEN` as an alternative.
- **Confidence**: settled (corroborates `docs-ghaw-multi-repo-ops.md` Claims 3
  and 9; first-party documentation)
- **Quote**: (no direct single-sentence quote beyond the YAML; see artifact and
  paraphrase in Our assessment)
- **Our assessment**: Corroborates the cross-repo read authentication pattern in
  `docs-ghaw-multi-repo-ops.md`. The key operational point: the `github-token`
  under `safe-outputs:` is for write operations; the `github-token` under `tools.github:`
  is for read operations. These are separate tokens with separate scopes. The
  `GH_AW_GITHUB_MCP_SERVER_TOKEN` magic secret (documented more fully in
  `docs-ghaw-multi-repo-ops.md` Claim 9) is the convenience path for cross-repo
  reads. For Ch02: document the two separate authentication points explicitly —
  teams frequently configure the safe-outputs token and forget the tools token.

### Claim 7: The monorepo development pattern uses the `checkout:` array to access shared libraries and config repos via sparse checkout alongside the primary repo

- **Evidence**: The monorepo example in the "Practical Applications" section
  shows a complete workflow YAML with two additional repository checkouts —
  `org/shared-libs` with `path: ./libs/shared` and `org/config-repo` with
  `sparse-checkout` for `defaults/` and `overrides/` paths. The pattern is
  described as "uses multiple checkout entries to access different repository
  components with varying fetch and sparse-checkout settings."
- **Confidence**: emerging (first-party documentation with YAML example)
- **Quote**: "uses multiple checkout entries to access different repository
  components with varying fetch and sparse-checkout settings"
- **Our assessment**: Sparse checkout in a cross-repo context is a performance
  optimization: for large monorepo-adjacent configs or library repos, checking
  out only the needed subdirectories avoids cloning gigabytes of irrelevant files.
  The combination of `path:` and `sparse-checkout:` within the same checkout
  array entry is the correct pattern. For Ch02: the monorepo development example
  is the reference pattern for workflows that need files from multiple repos
  simultaneously but don't need the full history of each.

### Claim 8: The scheduled push-to-PR-branch pattern — a scheduled workflow that fetches all open PR refs from a target repo and applies automated updates — requires a specific three-part configuration

- **Evidence**: The "Scheduled Push to Pull-Request Branch" example shows three
  required parts: (1) `checkout:` with `fetch: ["refs/pulls/open/*"]`, `current: true`,
  and the target repo's PAT; (2) `permissions: contents: read`; (3) `safe-outputs:
  push-to-pull-request-branch: target-repo: "org/target-repo"`. The description:
  "Fetches open PR branches and applies automated updates via scheduled triggers."
- **Confidence**: emerging (first-party documentation with YAML example)
- **Quote**: "Fetches open PR branches and applies automated updates via
  scheduled triggers."
- **Our assessment**: This is the only fully-specified example for the
  `push-to-pull-request-branch` safe output type in the gh-aw corpus. The pattern
  is useful for automated branch maintenance (e.g., rebasing open PRs onto main,
  applying dependency updates to branches, or running automated fixups across all
  open work). The three-part requirement (checkout with open-PR fetch, read
  permissions, safe output with matching target-repo) is specific enough to serve
  as a copy-paste starting point. For Ch06 (Orchestration): document this as the
  pattern for automated PR branch maintenance at scheduled intervals.

## Concrete Artifacts

### Wildcard Target Repository Configuration

From the cross-repository reference, "Safe Outputs" section.

```yaml
safe-outputs:
  github-token: ${{ secrets.CROSS_REPO_PAT }}
  create-issue:
    target-repo: "*"
    title-prefix: "[component] "
```

*Source: GitHub Agentic Workflows cross-repository reference, "Safe Outputs" section*

### Allowed Repositories with Default Target

From the cross-repository reference, "Safe Outputs" section.

```yaml
safe-outputs:
  github-token: ${{ secrets.CROSS_REPO_PAT }}
  create-issue:
    target-repo: "org/default-repo"
    allowed-repos: ["org/repo-a", "org/repo-b", "org/repo-c"]
    title-prefix: "[cross-repo] "
```

*Source: GitHub Agentic Workflows cross-repository reference, "Safe Outputs" section*

### GitHub Tools Authentication for Cross-Repo Reads

From the cross-repository reference, "Reading Access" section.

```yaml
tools:
  github:
    toolsets: [repos, issues, pull_requests]
    github-token: ${{ secrets.CROSS_REPO_PAT }}
```

*Source: GitHub Agentic Workflows cross-repository reference, "Reading Access" section*

### Monorepo Development Pattern — Sparse Cross-Repo Checkout

From the cross-repository reference, "Monorepo Development" example.

```yaml
---
on:
  pull_request:
    types: [opened, synchronize]

checkout:
  - fetch-depth: 0
  - repository: org/shared-libs
    path: ./libs/shared
    ref: main
    github-token: ${{ secrets.LIBS_PAT }}
  - repository: org/config-repo
    path: ./config
    sparse-checkout: |
      defaults/
      overrides/

permissions:
  contents: read
  pull-requests: read
---
# Cross-Repo PR Analysis
```

*Source: GitHub Agentic Workflows cross-repository reference, "Monorepo Development" example*

### Hub-and-Spoke Issue Tracking Pattern

From the cross-repository reference, "Hub-and-Spoke Tracking" example.

```yaml
---
on:
  issues:
    types: [opened, labeled]

permissions:
  contents: read
  issues: read

safe-outputs:
  github-token: ${{ secrets.CROSS_REPO_PAT }}
  create-issue:
    target-repo: "org/central-tracker"
    title-prefix: "[component-a] "
    labels: [tracking, multi-repo]
    max: 1
---
# Cross-Repository Issue Tracker
```

*Source: GitHub Agentic Workflows cross-repository reference, "Hub-and-Spoke Tracking" example*

### Scheduled Push to Pull-Request Branch

From the cross-repository reference, "Scheduled Push to Pull-Request Branch" example.

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
```

*Source: GitHub Agentic Workflows cross-repository reference, "Scheduled Push to Pull-Request Branch" example*

### Wildcard Non-Support Matrix — Safe Output Types Excluded from `target-repo: "*"`

From the cross-repository reference, caution block in "Safe Outputs" section.

```
Safe output type                        | Wildcard support
----------------------------------------|------------------
create-pull-request-review-comment      | NOT supported
reply-to-pull-request-review-comment    | NOT supported
submit-pull-request-review              | NOT supported
create-agent-session                    | NOT supported
manage-project-items                    | NOT supported
All other safe output types             | Supported
```

*Source: GitHub Agentic Workflows cross-repository reference, caution block in "Safe Outputs" section*

### `push-to-pull-request-branch` Checkout Requirement (Verbatim)

From the cross-repository reference, constraint note in "Safe Outputs" section.

```
"Unlike other safe output types, push-to-pull-request-branch with target-repo
requires the target repository to be checked out into the workflow workspace
using the checkout: frontmatter field with a path: specified. Without a checkout,
the agent has no local git history to create and push a patch from."
```

*Source: GitHub Agentic Workflows cross-repository reference, "Safe Outputs" section*

### `allowed-repos` Union Semantics

From the cross-repository reference, "Safe Outputs" section.

```
When allowed-repos is specified:
  - Agent can include a repo field in output to select which repository
  - Target repository (from target-repo or current repo) is always implicitly allowed
  - Creates a union of allowed destinations
```

*Source: GitHub Agentic Workflows cross-repository reference, "Safe Outputs" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-multi-repo-ops.md` Claim 1 (`target-repo` as the primary cross-repo
    safe-output parameter): this page corroborates the explicit `target-repo` form
    and the eight supported output types. The cross-repository reference adds the
    wildcard form and the `allowed-repos` union semantics that the patterns page does
    not describe in detail.
  - `docs-ghaw-multi-repo-ops.md` Claim 2 ("Without `target-repo`, these safe outputs
    operate on the repository where the workflow is running."): the cross-repo reference
    makes the same statement, confirming the default behavior across both the patterns
    and reference pages.
  - `docs-ghaw-multi-repo-ops.md` Claim 9 (`GH_AW_GITHUB_MCP_SERVER_TOKEN` as a
    cross-repo read authentication option): the cross-repo reference names the same
    three options (PAT, GitHub App, magic secret) for GitHub Tools cross-repo reads.
  - `docs-ghaw-sharing-workflows.md` Claim 7 (`target-repo` and `allowed-repos` for
    cross-repository execution — "Cross-repository operations require appropriate
    GitHub token permissions and explicit `allowed-repos` declarations."): the
    reference page corroborates `allowed-repos` as a required field for multi-target
    cross-repo operations and extends it with the union semantics (implicit inclusion
    of the default target repo).
  - `docs-ghaw-checkout-reference.md` Claim 3 (multiple repository checkout using
    array syntax): the monorepo example and deterministic multi-repo example here use
    the same array checkout syntax documented in the checkout reference.
  - `docs-ghaw-checkout-reference.md` Claim 4 (`refs/pulls/open/*` as a gh-aw shorthand
    for all open PR head refs): the scheduled push-to-PR-branch example uses exactly
    this fetch pattern in its checkout configuration.
  - `docs-ghaw-safe-outputs-specification.md` Claim 5 (SP6: Cross-Repository Containment
    — "For all cross-repository operations: target must be in type-specific allowlist OR
    global allowlist when defined."): the `allowed-repos` mechanism documented here is the
    runtime implementation of the SP6 security invariant.

- **Contradicts**: None identified. All claims are consistent with existing source notes.
  The wildcard and `push-to-pull-request-branch` constraints are additive detail, not
  contradictions of existing coverage. No contradiction issue filed.

- **Extends**:
  - `docs-ghaw-multi-repo-ops.md`: the patterns page documents `target-repo` with an
    explicit value. This reference page adds two additional forms: wildcard (`"*"`) and
    agent-selectable via `allowed-repos`. Together they give the complete three-form
    cross-repo targeting model.
  - `docs-ghaw-checkout-reference.md` Claim 3 (array checkout syntax): the cross-repo
    reference's monorepo example adds the sparse-checkout dimension to multi-repo
    array checkout, making it the reference for "check out multiple repos but only the
    parts you need." The checkout reference documents the field; this page shows the
    cross-repo sparse-checkout use case.
  - `docs-ghaw-safe-outputs-specification.md`: the spec documents the abstract Safe
    Outputs architecture and security invariants. This page provides the concrete
    operational guidance for one specific advanced case (`push-to-pull-request-branch`)
    that the spec abstracts over. Together they give the complete picture.

- **Novel**:
  - **`target-repo: "*"` wildcard syntax** (Claim 1): No prior corpus source documents
    the wildcard form of `target-repo`. The pattern notes cover explicit targets only.
    This is the primary novel contribution.
  - **Five safe output types excluded from wildcard** (Claim 2): The explicit list of
    PR-review and project-management types that require explicit targeting is not
    documented anywhere in the corpus. Practitioners using wildcard on any of these
    five types will encounter a runtime failure.
  - **`push-to-pull-request-branch` checkout requirement** (Claim 3): No prior source
    documents that this safe output type requires a workspace checkout with `path:`.
    The constraint distinguishes it from all other safe output types. A complete working
    example (Concrete Artifacts → Scheduled Push to PR Branch) is the first such example
    in the corpus.
  - **`allowed-repos` implicit-inclusion union semantics** (Claim 4): Prior notes describe
    `allowed-repos` as an allowlist but do not document that the `target-repo` value is
    always implicitly included. The union semantics are new.
  - **Scheduled push-to-PR-branch example** (Claim 8): The complete three-part YAML
    for a scheduled PR branch update workflow is not in any prior source note.

## Guide Impact

### Chapter 02: Harness Engineering

- **Document `target-repo` in three forms with selection guidance** (Claims 1, 4, 5):
  The guide should present `target-repo: "org/repo"` (explicit, single destination),
  `target-repo: "*"` (agent-selected at runtime), and `allowed-repos` list (curated
  multi-target) as three distinct configuration modes. Selection guidance: explicit
  for known single destinations; `allowed-repos` for workflows that need a bounded
  choice set; `"*"` only when the full set of potential destinations is unknown at
  authoring time (and always paired with authentication scoping).

- **Add `push-to-pull-request-branch` as a separate safe output type with its checkout
  pre-condition** (Claims 3, 8): The guide's safe-outputs coverage should document
  this type separately from all others, noting the mandatory `checkout:` with `path:`
  and `fetch: ["refs/pulls/open/*"]` configuration. Use the Concrete Artifacts →
  Scheduled Push to PR Branch YAML as the reference example.

- **Add wildcard exclusion table for `target-repo: "*"`** (Claim 2): When documenting
  wildcard targeting, include the five excluded safe output types with an explanation
  of why they require explicit targets (they operate within an existing PR/project
  context where the repo is already known from the event trigger).

### Chapter 03: Safety and Verification

- **Add `allowed-repos` as a required blast radius control for multi-target wildcard
  workflows** (Claims 1, 4): Workflows using `target-repo: "*"` should always pair
  it with `allowed-repos` to bound the set of eligible destinations. Without
  `allowed-repos`, the wildcard has no destination constraint beyond what the agent
  reasons at runtime. Frame this as the compile-time complement to the runtime
  wildcard: `"*"` enables flexibility; `allowed-repos` enforces the boundary.

### Chapter 06: Orchestration and Multi-Agent Coordination

- **Add scheduled PR branch maintenance as a gh-aw orchestration pattern** (Claim 8):
  The scheduled push-to-PR-branch pattern is distinct from the multi-repo issue
  tracking patterns documented via `docs-ghaw-multi-repo-ops.md`. Document it as
  the pattern for automated PR branch maintenance (rebasing, dependency updates,
  automated fixups) with the specific three-part configuration pre-conditions.

## Extraction Notes

1. **WebFetch returns model-summarized content, not raw HTML**: The page is an
   Astro/Starlight SPA. Multiple targeted WebFetch requests extracted different
   sections. Verbatim quotes were requested and returned by the processing model;
   they are assessed as accurately captured for short, specific constraint statements
   (especially Claim 3's push-to-pull-request-branch quote and Claim 5's default
   behavior quote). The YAML code blocks are treated as authoritative extracts from
   the page. If any quote fails Assayer spot-check, the constraint it describes is
   still documented in the Concrete Artifacts section and Our assessment.

2. **Source is a consolidation reference, not a patterns page**: The Prospector
   assessed novelty as low because the core patterns are already documented. This
   note focuses extraction on the three genuinely novel elements (wildcard targeting,
   wildcard exclusions, push-to-PR-branch checkout requirement) and provides five
   YAML examples not all present in prior notes.

3. **Prospector guidance followed**: Mined specifically for novel examples and edge
   cases as directed: the wildcard form, the five excluded types, the checkout
   constraint, and the scheduled push-to-PR-branch pattern.

4. **No explicit publication date**: The documentation does not carry a publication
   date. `date_published` is left null.

5. **No contradictions filed**: Reviewed all existing corpus source notes. All claims
   in this source are consistent with existing notes or extend them. No contradiction
   issue filed.
