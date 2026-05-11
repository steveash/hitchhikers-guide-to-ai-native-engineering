---
source_url: https://github.github.com/gh-aw/reference/checkout
source_type: docs
title: "GitHub Agentic Workflows: Checkout Configuration Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: settled
issue: "#361"
---

# GitHub Agentic Workflows: Checkout Configuration Reference

> The authoritative configuration reference for the `checkout:` frontmatter
> field in gh-aw workflows — documents the five configuration categories
> (custom settings, multiple repos, additional ref fetching, disabling,
> primary marking), the merge rules when multiple checkout configs target
> the same path, and the critical distinction that `current: true` annotates
> the agent's default repository context but does not change the working
> directory.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/checkout` page —
  in the same `reference/` section as `reference/artifacts` covered by
  `docs-ghaw-artifacts-reference.md`. Reference pages are specification-level
  documents, distinct from the pattern-focused `patterns/` pages and the
  practitioner `guides/` section.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind Peli de Halleux's agent factory blog series and the
  `gh aw` platform. Claims about `checkout:` field schema, merge rules, and
  agent behavior are authoritative for this platform.
- **Scope**: The complete `checkout:` frontmatter configuration reference —
  all fields, their types and defaults, five configuration modes, authentication
  options (PAT and GitHub App), ref-fetching patterns, merge rules, and the
  `current: true` annotation for primary repository marking. Does NOT cover:
  Safe Outputs (see `docs-ghaw-safe-outputs-specification.md`), the MCP server
  configuration for cross-repo reads (see `docs-ghaw-mcps.md`), the permissions
  frontmatter field (see `docs-ghaw-permissions-reference.md`), or the full
  multi-repo orchestration pattern (see `docs-ghaw-central-repo-ops.md` and
  `docs-ghaw-multi-repo-ops.md`).

## Extracted Claims

### Claim 1: The `checkout:` frontmatter field is the single configuration point for all `actions/checkout` behavior in agent jobs — including repository selection, auth, depth, and ref patterns

- **Evidence**: The page opens: "The `checkout:` frontmatter field controls
  how `actions/checkout` is invoked in the agent job." The complete configuration
  table lists 11 fields (`repository`, `ref`, `path`, `github-token`,
  `github-app`, `fetch-depth`, `fetch`, `sparse-checkout`, `submodules`, `lfs`,
  `current`), all expressed as YAML under this single frontmatter key.
- **Confidence**: settled (first-party reference documentation; this is the
  authoritative field specification)
- **Quote**: "The `checkout:` frontmatter field controls how `actions/checkout`
  is invoked in the agent job."
- **Our assessment**: All checkout behavior is declared in one frontmatter
  field — there is no separate `actions/checkout` step to configure. This
  aligns with the two-component workflow structure in `docs-ghaw-how-they-work.md`
  Claim 1: frontmatter carries all capability and constraint declarations,
  including how the workspace is populated. For Ch02 (Harness Engineering): when
  documenting the frontmatter schema, `checkout:` should be presented as the
  complete checkout API — practitioners do not need to add a separate
  `actions/checkout@v4` step.

### Claim 2: The default behavior is a shallow fetch (fetch-depth: 1) of the triggering repository, plus automatic checkout of the PR head ref for pull request events

- **Evidence**: The page states: "By default, the workflow checks out the
  repository where it runs with shallow fetch (`fetch-depth: 1`), and for pull
  requests, it also checks out the PR head ref." No explicit `checkout:` block
  is needed to get this behavior.
- **Confidence**: settled (first-party documentation; default behavior is
  explicitly stated)
- **Quote**: "By default, the workflow checks out the repository where it runs
  with shallow fetch (`fetch-depth: 1`), and for pull requests, it also checks
  out the PR head ref."
- **Our assessment**: The PR head ref checkout-by-default is significant for
  code review and diff-aware workflows: agents acting on PRs automatically
  have the branch head available without configuration. Teams building review
  bots or PR analysis workflows do not need to specify `ref:` explicitly for
  standard cases. For Ch02: document this default to help practitioners
  distinguish when they need explicit `checkout:` configuration vs. when the
  default suffices.

### Claim 3: Multiple repositories can be checked out simultaneously using array syntax, each with independent configuration for auth, depth, path, and ref

- **Evidence**: The page provides a YAML example with array syntax:
  ```yaml
  checkout:
    - fetch-depth: 0
    - repository: owner/other-repo
      path: ./libs/other
      ref: main
      github-token: ${{ secrets.CROSS_REPO_PAT }}
  ```
  Each array element is an independent checkout configuration. The first entry
  modifies the primary repo checkout; additional entries add secondary repos.
- **Confidence**: settled (first-party documentation with YAML example)
- **Quote**: (no direct quote capturing the array semantics specifically; see
  YAML example in Concrete Artifacts)
- **Our assessment**: The array form is the foundation for deterministic
  multi-repo workflows — workflows that need to compare, synchronize, or
  analyze multiple repositories simultaneously. This is distinct from the
  `target-repo` safe-output approach in `docs-ghaw-multi-repo-ops.md` (which
  writes to external repos without local checkout). For Ch04 (Orchestration):
  when a workflow needs local access to multiple repos' file trees — not just
  the ability to post issues or PRs — the array checkout form is the correct
  mechanism. For Ch02: document both as complementary patterns with different
  purposes: array checkout for local-file-access scenarios, `target-repo` for
  safe-output write operations.

### Claim 4: The `fetch:` option retrieves additional Git refs post-checkout using named patterns, including a gh-aw shorthand for all open PR head refs

- **Evidence**: The page documents four ref-fetching patterns for the `fetch:`
  field:
  - `"*"` — all remote branches
  - `"refs/pulls/open/*"` — "GH-AW shorthand for all open PR head refs"
  - `"main"` — specific branch name
  - `"feature/*"` — glob pattern matching branch names
  All patterns are fetched after the initial checkout completes.
- **Confidence**: settled (first-party reference documentation; patterns are
  explicitly enumerated)
- **Quote**: "GH-AW shorthand for all open PR head refs"
- **Our assessment**: The `"refs/pulls/open/*"` shorthand is a gh-aw platform
  extension — not a standard Git ref pattern. It enables workflows that need
  to analyze or act on all open PRs without listing them individually. This is
  particularly useful for triage agents, code review orchestrators, or CI
  analysis workflows that need access to every open branch. For Ch03: document
  the `refs/pulls/open/*` shorthand as a platform-specific pattern that
  simplifies PR-scanning workflows but has no portable equivalent outside gh-aw.

### Claim 5: GitHub App credentials can be supplied directly in checkout configuration via a `github-app:` object field, supporting the `client-id`/`private-key` pair

- **Evidence**: The page provides a complete YAML example for GitHub App
  checkout authentication:
  ```yaml
  checkout:
    fetch-depth: 0
    github-app:
      client-id: ${{ vars.APP_ID }}
      private-key: ${{ secrets.APP_PRIVATE_KEY }}
  ```
  The configuration table notes that `app-id` is deprecated in favour of
  `client-id`. An optional `owner` and `repositories` field are also documented
  in the `github-app` object.
- **Confidence**: settled (first-party reference documentation; YAML example
  provided)
- **Quote**: "GitHub App credentials (`client-id` or `app-id` (deprecated),
  `private-key`, optional `owner`, `repositories`)"
- **Our assessment**: Supporting GitHub App auth at the checkout level means
  practitioners can use per-job minting and automatic revocation for workspace
  population — not just for safe outputs. This complements `docs-ghaw-multi-repo-ops.md`
  Claim 8's recommendation to prefer GitHub Apps over PATs: the recommendation
  now extends cleanly to checkout as well. For Ch03: the `github-app:` checkout
  field makes it straightforward to apply least-privilege GitHub App tokens to
  repo access, not just to safe-output delivery. Note the `app-id` deprecation
  — practitioners migrating from older configurations should update to `client-id`.

### Claim 6: Setting `checkout: false` suppresses automatic checkout entirely, for workflows that access repositories through MCP servers or other non-local mechanisms

- **Evidence**: The page states: "Set `checkout: false` to suppress default
  checkout entirely." The use case is explicit: "for workflows that access
  repositories through MCP servers or other mechanisms that do not require a
  local clone."
- **Confidence**: settled (first-party documentation; boolean field value
  explicitly documented)
- **Quote**: "for workflows that access repositories through MCP servers or
  other mechanisms that do not require a local clone."
- **Our assessment**: `checkout: false` is the correct configuration for
  workflows that operate entirely through remote API calls or MCP tools —
  for example, an agent that uses the GitHub MCP server to read and write
  repository state without ever needing the files locally. Suppressing checkout
  avoids an unnecessary workspace setup step that adds latency and consumes
  disk space. For Ch02: document `checkout: false` as the optimization for
  pure-API or pure-MCP workflows, with a note on when local checkout is
  actually required (e.g., when the agent needs to run tests, build artifacts,
  or diff file contents locally).

### Claim 7: `current: true` marks a non-default checkout as the primary working repository for agent GitHub operations — but does not change the working directory; explicit `cd` is still required

- **Evidence**: The page states: "The agent uses this as the default for all
  GitHub operations...When omitted, the agent defaults to the repository where
  the workflow is running." However, it explicitly warns: "`current: true` only
  annotates the system prompt—it does not automatically change the working
  directory." The required workaround is shown as a workflow step:
  ```yaml
  Navigate into the folder where the target repository has been checked out into: cd ${{ github.workspace }}/target
  ```
- **Confidence**: settled (first-party documentation; both the annotation
  behavior and the working-directory limitation are explicitly stated)
- **Quote**: "`current: true` only annotates the system prompt—it does not
  automatically change the working directory."
- **Our assessment**: This is the most important footgun in the checkout
  reference. Practitioners who check out a non-default repo with `current: true`
  and expect the agent's tools (shell commands, file operations) to automatically
  operate in that repo's directory will be surprised — the agent starts in the
  workflow's default working directory, not in the `current` repo's path. The
  fix is explicit `cd` navigation in the workflow instructions. This is
  confirmed by the CentralRepoOps worker YAML in `docs-ghaw-central-repo-ops.md`
  (Concrete Artifacts), which uses `current: true` alongside a `path:` field
  and requires the agent to navigate. For Ch02: document `current: true` with
  the explicit warning that shell-level working directory and agent GitHub
  context are separate — `current: true` only affects which repo is the default
  for GitHub API calls, not where the agent's file operations land.

### Claim 8: When multiple checkout configurations target the same path, they merge via deterministic rules — deepest fetch-depth wins, ref patterns union, LFS uses OR logic

- **Evidence**: The page documents merge rules explicitly:
  - Fetch depth: "Deepest value wins (0 = full history takes precedence)"
  - Fetch refs: "Union of all patterns; duplicates removed"
  - Sparse patterns: "Union of all patterns"
  - LFS: "OR-ed (enabled if any config enables it)"
  - Submodules: "First non-empty value wins"
  - Ref/Token/App: "First-seen wins"
- **Confidence**: settled (first-party reference documentation; rules are
  explicitly enumerated)
- **Quote**: "Multiple `checkout:` configurations can target the same path
  and repository."
- **Our assessment**: The merge rules matter for modular workflow composition
  where shared imports or base configurations define common checkout settings
  and individual workflow configs add specifics. The "deepest depth wins"
  rule means a base config with `fetch-depth: 0` will override a module that
  only needs `fetch-depth: 1` — which is safe (more history is always
  available) but may increase clone time. The "first-seen wins" rule for
  `ref`/token/app means the order of array entries matters for credential
  selection. For Ch02: document these merge rules when covering workflow
  composition patterns — they are invisible but critical for understanding
  the effective checkout configuration in composed workflows.

### Claim 9: `sparse-checkout` enables pattern-based partial workspaces using newline-separated path patterns

- **Evidence**: The configuration table documents `sparse-checkout` as:
  "Newline-separated patterns for sparse checkout (e.g., `.github/\nsrc/`)."
  The field type is `string`.
- **Confidence**: settled (first-party documentation; field is documented in
  the configuration table)
- **Quote**: "Newline-separated patterns for sparse checkout
  (e.g., `.github/\nsrc/`)."
- **Our assessment**: Sparse checkout is the optimization for workflows that
  only need a subset of repository files — a common case for agents operating
  on large monorepos that only care about `.github/` or `src/` subdirectories.
  Sparse checkout reduces disk usage and clone time significantly for large
  repositories. For Ch02: sparse checkout should be documented as a performance
  optimization for monorepo workflows, with the pattern string format
  (newline-separated, not comma-separated) made explicit to avoid configuration
  errors.

## Concrete Artifacts

### Custom Checkout with Full History (PAT Authentication)

From the checkout reference, "Custom Checkout Settings" section.

```yaml
checkout:
  fetch-depth: 0
  github-token: ${{ secrets.MY_TOKEN }}
```

*Source: GitHub Agentic Workflows checkout reference, "Custom Checkout Settings"*

### Custom Checkout with GitHub App Authentication

From the checkout reference, "Custom Checkout Settings" section.

```yaml
checkout:
  fetch-depth: 0
  github-app:
    client-id: ${{ vars.APP_ID }}
    private-key: ${{ secrets.APP_PRIVATE_KEY }}
```

*Source: GitHub Agentic Workflows checkout reference, "Custom Checkout Settings"*

### Multiple Repository Checkout (Array Syntax)

From the checkout reference, "Multiple Repositories" section.

```yaml
checkout:
  - fetch-depth: 0
  - repository: owner/other-repo
    path: ./libs/other
    ref: main
    github-token: ${{ secrets.CROSS_REPO_PAT }}
```

*Source: GitHub Agentic Workflows checkout reference, "Multiple Repositories"*

### Fetching Additional Refs — All Branches

From the checkout reference, "Fetching Additional Refs" section.

```yaml
checkout:
  - fetch: ["*"]
    fetch-depth: 0
```

*Source: GitHub Agentic Workflows checkout reference, "Fetching Additional Refs"*

### Fetching Additional Refs — All Open PR Head Refs (Cross-Repo)

From the checkout reference, "Fetching Additional Refs" section.

```yaml
checkout:
  - repository: githubnext/gh-aw-side-repo
    github-token: ${{ secrets.GH_AW_SIDE_REPO_PAT }}
    fetch: ["refs/pulls/open/*"]
    fetch-depth: 0
```

*Source: GitHub Agentic Workflows checkout reference, "Fetching Additional Refs"*

### Fetching Additional Refs — Specific Branches with Glob

From the checkout reference, "Fetching Additional Refs" section.

```yaml
checkout:
  - repository: org/target-repo
    github-token: ${{ secrets.CROSS_REPO_PAT }}
    fetch: ["main", "feature/*"]
    fetch-depth: 0
```

*Source: GitHub Agentic Workflows checkout reference, "Fetching Additional Refs"*

### Disabling Default Checkout

From the checkout reference, "Disabling Checkout" section.

```yaml
checkout: false
```

*Source: GitHub Agentic Workflows checkout reference, "Disabling Checkout"*

### Primary Repository Marking with Explicit Navigation

From the checkout reference, "Primary Repository Marking" section.

```yaml
checkout:
  - repository: org/target-repo
    path: ./target
    github-token: ${{ secrets.CROSS_REPO_PAT }}
    current: true
```

With corresponding workflow instruction:
```
Navigate into the folder where the target repository has been checked out into: cd ${{ github.workspace }}/target
```

*Source: GitHub Agentic Workflows checkout reference, "Primary Repository Marking"*

### Complete Configuration Field Reference Table

From the checkout reference, "Configuration Options" section.

```
Field           | Type         | Description
----------------|--------------|------------------------------------------------------
repository      | string       | Repository in `owner/repo` format. Defaults to current repo.
ref             | string       | Branch, tag, or SHA; defaults to triggering ref
path            | string       | Workspace location; defaults to root
github-token    | string       | Token using `${{ secrets.MY_TOKEN }}` syntax
github-app      | object       | GitHub App credentials (client-id or app-id [deprecated],
                |              | private-key, optional owner, repositories)
fetch-depth     | integer      | Commits to fetch. 0 = full history, 1 = shallow clone (default)
fetch           | string/array | Additional Git refs to fetch after checkout
sparse-checkout | string       | Newline-separated patterns for sparse checkout
submodules      | string/bool  | "recursive", "true", or "false"
lfs             | boolean      | Download Git LFS objects
current         | boolean      | Marks this checkout as the primary working repository
```

*Source: GitHub Agentic Workflows checkout reference, "Configuration Options"*

### Checkout Merge Rules

From the checkout reference, "Checkout Merging" section.

```
Property    | Merge Rule
------------|-----------------------------------------------------------
fetch-depth | Deepest value wins (0 = full history takes precedence)
fetch refs  | Union of all patterns; duplicates removed
sparse      | Union of all patterns
lfs         | OR-ed (enabled if any config enables it)
submodules  | First non-empty value wins
ref/token   | First-seen wins
```

*Source: GitHub Agentic Workflows checkout reference, "Checkout Merging"*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-central-repo-ops.md` Concrete Artifacts → "Complete Worker
    Workflow Frontmatter" section: the worker YAML uses `checkout: repository +
    github-token + current: true`, exactly matching the `current: true` pattern
    documented in this reference. The checkout reference now provides the formal
    specification for what that worker YAML means.
  - `docs-ghaw-how-they-work.md` Claim 1 (two-component workflow structure —
    YAML frontmatter carries constraints, markdown carries instructions):
    `checkout:` is one of the frontmatter fields that constrains the agent's
    execution environment. This reference fills in the complete specification
    for that field.
  - `docs-ghaw-multi-repo-ops.md` Claim 8 (GitHub Apps preferred over PATs for
    per-job minting and automatic revocation): the `github-app:` checkout field
    (Claim 5 here) extends that preference to the checkout step itself — not just
    safe outputs. Both notes now point to GitHub App auth as the default for
    production cross-repo workflows.

- **Extends**:
  - `docs-ghaw-central-repo-ops.md`: the CentralRepoOps worker YAML uses
    `checkout: current: true` but does not explain what `current: true` does or
    its working-directory limitation. This reference provides the full specification,
    including the critical footgun (Claim 7): `current: true` annotates the
    system prompt but does not change the shell working directory.
  - `docs-ghaw-multi-repo-ops.md` Concrete Artifacts → "Deterministic Multi-Repo
    Checkout" section: that section uses a legacy `actions/checkout@v6` explicit
    step approach. This reference documents the native `checkout:` frontmatter
    array syntax as the gh-aw-native equivalent, which is more concise and
    eliminates the need for a manual checkout step.
  - `docs-ghaw-how-they-work.md` Claim 4 (minimal permissions, no write access
    by default): `checkout: false` (Claim 6 here) is a further reduction —
    not just no write access but no local workspace at all for workflows operating
    purely via MCP or remote APIs.
  - `docs-ghaw-orchestration-patterns.md`: that note documents orchestrator/worker
    fan-out but does not cover how workers configure their workspace. This reference
    provides the checkout configuration that workers would use when receiving
    `target_repo` as a `workflow_dispatch` input and checking out the target
    repository with `current: true`.

- **Contradicts**: None identified. The `current: true` behavior (annotates
  agent context, not working directory) is consistent with the worker YAML
  patterns in `docs-ghaw-central-repo-ops.md` which show explicit `path:` fields
  alongside `current: true`. No existing source note makes a claim that `current:
  true` auto-changes the working directory. No contradiction issue filed.

- **Novel**:
  - **Complete `checkout:` field specification** (Claim 1): The full 11-field
    configuration table is not reproduced in any existing source note. Prior notes
    use checkout YAML examples but do not document the complete field inventory.
  - **Default behavior explicitness** (Claim 2): The PR head ref auto-checkout
    behavior is not mentioned in any existing source note. Practitioners building
    PR-triggered review workflows benefit from knowing this is default.
  - **`fetch:` ref patterns including the gh-aw `refs/pulls/open/*` shorthand**
    (Claim 4): This platform-specific shorthand is new to the corpus. It enables
    a class of PR-scanning workflows that would otherwise require listing all
    open PRs via API.
  - **`current: true` working-directory footgun** (Claim 7): The explicit
    warning that `current: true` is system-prompt annotation only, not
    working-directory change, is new to the corpus. The existing worker YAML
    examples imply but do not state this limitation.
  - **Checkout merge rules** (Claim 8): The deterministic merge rules for
    overlapping checkout configurations are completely absent from the corpus.
    The "first-seen wins" rule for credentials and "deepest depth wins" for
    fetch-depth are critical for composed workflow authors.
  - **`checkout: false` as an explicit configuration mode** (Claim 6): While
    MCP-based access patterns are documented, the explicit `checkout: false`
    field that suppresses workspace setup for such workflows is not documented
    in any prior source note.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add `checkout:` as a named frontmatter field alongside `permissions:` and
  `tools:`** (Claim 1): The guide's frontmatter coverage should include
  `checkout:` as a first-class field. Document the 11-field schema from Concrete
  Artifacts → Configuration Field Reference Table. The current guide likely
  describes permissions and tools but may underspecify the checkout configuration
  surface.

- **Document default behavior to help practitioners identify when explicit
  configuration is needed** (Claim 2): Most workflows do not need an explicit
  `checkout:` block — the default shallow-fetch with PR head ref covers the
  common case. Adding this to Ch02 helps practitioners make the right no-op choice
  (omit `checkout:`) and saves unnecessary configuration work.

- **Add `current: true` with the working-directory footgun warning** (Claim 7):
  Any workflow that checks out a non-default repository as the primary target
  must include this note: `current: true` sets the agent's GitHub API default,
  not the shell's working directory. Recommend pairing `current: true` with an
  explicit `path:` and a `cd` navigation step in the workflow instructions.

- **Document `checkout: false` for pure-MCP/pure-API workflows** (Claim 6):
  Workflows that access repositories only through MCP tools or GitHub API should
  suppress checkout. This reduces setup time and avoids unnecessary disk usage.

- **Document checkout merge rules for composed workflow authors** (Claim 8):
  Teams using imports or shared base configurations need to understand the
  merge semantics — especially "first-seen wins" for credentials and "deepest
  depth wins" for fetch-depth.

### Chapter 03: Safety and Verification

- **Add GitHub App auth at checkout level as a least-privilege recommendation**
  (Claim 5): Recommend `github-app:` in `checkout:` for production multi-repo
  workflows, complementing the `docs-ghaw-multi-repo-ops.md` recommendation to
  prefer Apps over PATs for safe outputs. The two recommendations together give
  App-based auth coverage at both the workspace-population stage and the
  write-output stage.

- **Document `sparse-checkout` as a privilege surface reduction** (Claim 9):
  Checking out only the paths the agent needs (e.g., `.github/` only for a
  configuration workflow) reduces the risk of the agent reading or leaking
  sensitive files that happen to be in the repository. Document as a security
  measure, not just a performance optimization.

### Chapter 04: Orchestration and Multi-Agent Systems

- **Add array checkout syntax as the workspace primitive for worker agents**
  (Claim 3): When documenting the orchestrator/worker pattern, specify how
  workers configure their workspace. The array checkout form — with a primary
  `current: true` repo and optionally additional repos — is the standard pattern
  for workers receiving a `target_repo` dispatch input.

- **Document `refs/pulls/open/*` shorthand for PR-scanning orchestrators**
  (Claim 4): Orchestrators that need to analyze or act on all open PRs can
  use this shorthand to pre-fetch all PR head refs without API enumeration.
  Flag it as a gh-aw platform extension with no portable equivalent.

## Extraction Notes

1. **Source is first-party official documentation**: This is the authoritative
   reference page for the `checkout:` field, not a blog post or practitioner
   account. All field names, types, defaults, and merge rules are platform
   specifications.

2. **`app-id` deprecation noted but not elaborated**: The docs note that
   `app-id` is deprecated in favour of `client-id` in the `github-app:` object.
   The migration path for existing configurations is not detailed on this page.
   Practitioners with older configurations should update `app-id` to `client-id`.

3. **No explicit publication date**: The documentation does not carry a
   publication date. Content is consistent with gh-aw v1.x era based on the
   `github-app: client-id` field (which replaced `app-id`).

4. **Relationship to `actions/checkout@v4`**: The `checkout:` frontmatter
   approach replaces manual `actions/checkout` steps. The existing
   `docs-ghaw-multi-repo-ops.md` Concrete Artifacts section shows a legacy
   approach using `actions/checkout@v6` explicit steps. The native `checkout:`
   frontmatter array form is the current canonical approach.

5. **No sub-pages followed**: The checkout reference page did not appear to
   link to substantive sub-pages beyond the main reference content. The page
   is self-contained as a field specification.

6. **No contradictions to file**: Reviewed all existing corpus source notes.
   No claims in this source materially oppose existing source notes. The
   `current: true` working-directory behavior is consistent with (and explains)
   the worker YAML patterns in `docs-ghaw-central-repo-ops.md`. No contradiction
   issue filed.
