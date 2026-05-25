---
source_url: https://github.github.com/gh-aw/reference/repo-memory
source_type: docs
title: "GitHub Agentic Workflows: Repo Memory Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: emerging
issue: "#410"
---

# GitHub Agentic Workflows: Repo Memory Reference

> The authoritative API reference for `repo-memory` — covering minimal enablement,
> the full 11-parameter configuration surface (branch naming, file-glob, storage
> limits, target-repo, create-orphan, allowed-extensions), multiple-store `id:`
> syntax, auto-commit/auto-push trigger conditions, "your changes win" conflict
> resolution via the GraphQL `createCommitOnBranch` mutation (GPG-signed, enterprise
> ruleset-compatible), the signed-commit fallback limitation for symlinks and
> executables, a feature comparison with Cache Memory, and the security constraint
> against storing sensitive data. Complements `docs-ghaw-memory-ops.md` (patterns
> taxonomy) and `docs-ghaw-guides-memoryops.md` (how-to procedures) by providing
> the low-level implementation specification those pages omit.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/` section — the
  same tier as `reference/tools`, `reference/concurrency`, and
  `reference/frontmatter-full`. Reference pages document the complete parameter
  surface with types, defaults, and constraints. Distinct from the `patterns/`
  section (design patterns) and `guides/` section (how-to procedures), both of
  which address MemoryOps at the practitioner level without enumerating the
  implementation details this page covers.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's Agent Factory blog series and the `gh aw`
  CLI. Parameter names, defaults, path formats, and commit mechanism details are
  authoritative for the `gh aw` platform. Claims do not automatically generalize
  to non-gh-aw memory systems.
- **Scope**: Complete reference for the `repo-memory:` frontmatter tool — enablement,
  all configuration parameters, multiple-store syntax, behavioral mechanics
  (auto-commit trigger, merge conflict resolution, signed-commit guarantee),
  comparison with Cache Memory, security guidance, and troubleshooting stubs.
  Does NOT cover: the six MemoryOps design patterns (see `docs-ghaw-memory-ops.md`
  issue #855), the Pattern 1 JSON state schema or Pattern 6 multi-branch YAML
  (see `docs-ghaw-guides-memoryops.md` issue #438), cache-memory configuration
  (a separate tool), or the workflow examples ("Deep Report", "Daily Firewall
  Report") linked from the Examples section (practitioner examples, not reference
  content; not followed in this extraction).

## Extracted Claims

### Claim 1: `repo-memory: true` is the minimal syntax to enable persistent Git-branch storage, creating a `memory/default` branch with files accessible at a `/tmp/gh-aw/repo-memory-{id}/`-style mount path

- **Evidence**: "Enabling Repo Memory" section of the reference page, confirmed
  across multiple fetch passes.
- **Confidence**: settled (first-party documentation; the basic enablement syntax
  is explicit and unambiguous)
- **Quote**: "Creates branch `memory/default` at `/tmp/gh-aw/repo-memory-default/`."
- **Our assessment**: The one-line enablement (`tools: repo-memory: true`) is
  intentionally minimal — teams can adopt Repo Memory without configuring any
  parameters beyond the boolean. The branch name and access path are derived
  automatically: branch `memory/default` maps to mount path
  `/tmp/gh-aw/repo-memory-default/`. Note: the patterns/guides pages
  (`docs-ghaw-memory-ops.md`, `docs-ghaw-guides-memoryops.md`) consistently
  document the default path as `/tmp/gh-aw/repo-memory/default/` (slash-separated),
  while this reference page shows `/tmp/gh-aw/repo-memory-default/`
  (hyphen-separated). Both forms have appeared in multiple independent fetch
  passes; the Assayer should verify the exact path format against the live source.
  For Ch02 (Harness Engineering): document the one-line enablement pattern as
  the correct starting point for any stateful gh-aw workflow that needs cross-run
  persistence.

### Claim 2: Files are automatically committed and pushed after workflow completion — but only when changes are detected and threat detection passes

- **Evidence**: "Behavior" section of the reference page.
- **Confidence**: settled (first-party documentation; the trigger conditions are
  explicitly stated)
- **Quote**: "Files auto-commit/push after workflow completion." and "Changes
  auto-commit after validation (`file-glob`, `max-file-size`, `max-file-count`) and
  push when changes detected and threat detection passes."
- **Our assessment**: The auto-commit/push behavior has two gates: (1) validation
  against the configured file-glob, max-file-size, and max-file-count constraints
  — files that fail validation are not committed; (2) a "changes detected" check
  — no-op runs do not produce spurious commits. The threat detection gate is the
  gh-aw security layer; workflows that produce outputs flagged by threat detection
  do not persist memory. This explains the `always()` footgun (see Cross-References
  — `blog-ghaw-weekly-2026-04-13.md` Claim 7): `always()` as a step condition
  bypasses the skip propagation that should suppress `push_repo_memory` on
  bot-triggered no-ops. The correct conditional is `success()` or an explicit
  output-conditional check. For Ch02: document the "changes detected" gate as
  the reason `push_repo_memory` should not use `always()` — the platform already
  handles no-op suppression internally; adding `always()` overrides that protection.

### Claim 3: Merge conflicts are resolved via "your changes win" semantics — the GraphQL `createCommitOnBranch` mutation replays the file diff on top of the latest remote state when concurrent pushes collide

- **Evidence**: "Behavior" / merge conflict section of the reference page.
- **Confidence**: settled (first-party documentation; the specific resolution
  mechanism is stated)
- **Quote**: "if another run has pushed since the branch was checked out, the
  GraphQL mutation replays your file diff on top of the latest remote state
  (your changes win)"
- **Our assessment**: "Your changes win" is a last-writer-wins conflict resolution
  model. For append-only workloads (JSON Lines), this is safe: appending a new
  line is idempotent with respect to any concurrent appends. For mutating workloads
  (rewriting a JSON file), last-writer-wins means the earlier writer's changes are
  silently overwritten — which is why the MemoryOps pattern documentation
  (`docs-ghaw-memory-ops.md` Claim 10) recommends JSON Lines format to avoid
  this failure mode. The "replay" mechanism is architecturally elegant: the mutation
  doesn't reject concurrent writes, it merges them by replaying the diff on the
  latest state. This means the merge happens server-side via the GraphQL API, not
  as a local `git merge`. For Ch02: document last-writer-wins as the conflict
  model for Repo Memory, and cross-reference the JSON Lines recommendation as the
  design pattern that makes this safe for append-heavy workloads.

### Claim 4: Repo Memory commits use GitHub's GraphQL `createCommitOnBranch` mutation, producing GPG-signed commits that automatically satisfy enterprise signed-commit rulesets

- **Evidence**: Commit mechanism section (likely under "Behavior" or "Advanced
  Configuration") of the reference page.
- **Confidence**: settled (first-party documentation; the GraphQL mutation name
  and GPG signing are explicitly stated; GitHub's GraphQL API signing behavior
  is a platform guarantee)
- **Quote**: "signs each commit with GitHub's GPG key"
- **Our assessment**: GPG-signed commits via `createCommitOnBranch` satisfy the
  most common enterprise branch protection rule that would otherwise block Repo
  Memory from writing to protected branches: signed-commit rulesets. This means
  Repo Memory can write to branches in organizations that require signed commits
  (common in compliance-focused environments) without any additional configuration.
  The GraphQL path is the primary path; see Claim 5 for the fallback. For Ch05
  (Compliance and Governance): document the GraphQL-signed-commit guarantee as
  the reason Repo Memory is enterprise-ruleset-compatible by default.

### Claim 5: Files containing symlinks, executable bits (`chmod +x`), or submodule entries cause Repo Memory to fall back from the GraphQL mutation to plain `git push`, which fails signed-commit rulesets

- **Evidence**: Constraint note in the reference page (likely under "Advanced
  Configuration" or a dedicated limitation section).
- **Confidence**: settled (first-party documentation; the specific unsupported
  file types are enumerated)
- **Quote**: "The GraphQL mutation does not support symlinks, executable files
  (`chmod +x`), or submodule entries."
- **Our assessment**: The signed-commit guarantee (Claim 4) has a specific carve-out:
  any Repo Memory content that includes symlinks, executables, or submodules causes
  the system to fall back to `git push`, bypassing the GraphQL mutation. This breaks
  the GPG signing guarantee — the fallback push is unsigned and will fail
  signed-commit rulesets. The practical implication for harness engineers: Repo
  Memory content must be restricted to plain text/binary files without execute bits
  or symlinks. The `allowed-extensions` parameter (see Claim 6) is one mechanism
  to enforce this — restricting to `.json`, `.md`, `.txt` eliminates the risk of
  executable file content. For Ch02: document the symlink/executable fallback as a
  potential enterprise deployment blocker and recommend `allowed-extensions` as the
  mitigation.

### Claim 6: Repo Memory supports 11 configuration parameters — branch-name, branch-prefix, description, file-glob, max-file-size (100KB default), max-file-count (100 default), max-patch-size (10KB default, 1MB max), target-repo, create-orphan, and allowed-extensions — allowing precise control over storage scope, size limits, and security boundaries

- **Evidence**: Configuration parameter table from the reference page, confirmed
  across multiple fetch passes with consistent field names and defaults.
- **Confidence**: settled for the parameter names and defaults (first-party
  reference documentation; parameter table confirmed consistently). The
  interpretation of `target-repo`'s purpose is `emerging` (see note below).
- **Quote**: (no direct quote for the full table; see parameters table in
  Concrete Artifacts)
- **Our assessment**: The parameter surface is richer than most corpus sources
  have implied. Key parameters for harness engineers: `file-glob` controls what
  the agent can write (content scoping), `allowed-extensions` is a security
  boundary for the signed-commit fallback (Claim 5), `max-patch-size` (10KB
  default, 1MB max) caps individual push size to prevent runaway memory growth,
  and `target-repo` enables cross-repo isolation. The `max-file-count: 100`
  default is a hard ceiling — workflows that accumulate more than 100 files will
  need explicit configuration. For Ch02: document the default limits as operational
  guardrails that teams should consciously configure for production workflows;
  the defaults are conservative and suited for small-scale memory use, not for
  high-volume data accumulation.
  **Note on `target-repo` confidence**: The description "allows routing memory
  storage to a different repository" is inferred from the field name and the
  `owner/repository` value format in the example YAML. The reference page does
  not give a prose description of this field beyond the example. Confidence for
  the `target-repo` claim specifically is **emerging**, not settled. The Assayer
  should verify this interpretation against the live source.

### Claim 7: Multiple Repo Memory configurations can be declared using array syntax with distinct `id:` keys, with each instance mounting at `/tmp/gh-aw/repo-memory-{id}/`

- **Evidence**: "Multiple Configurations" section of the reference page, with a
  YAML example showing two configurations.
- **Confidence**: settled (first-party documentation; the array syntax and id-based
  mount path are explicitly shown)
- **Quote**: (no direct quote for the section heading; see YAML artifact in
  Concrete Artifacts)
- **Our assessment**: The `id:` syntax enables separation-of-concerns memory
  management within a single workflow — different data categories can have different
  branch names, file-glob filters, and size limits. This is the same architecture
  as MemoryOps Pattern 6 (Multiple Memory Stores), but the reference page provides
  the concrete YAML syntax that the patterns page describes conceptually. When
  multiple IDs are declared, the branch name defaults to `{branch-prefix}/{id}`,
  so `- id: insights` with `branch-prefix: daily` produces branch `daily/insights`
  at mount path `/tmp/gh-aw/repo-memory-insights/`. This is the mechanism that
  enables the `metrics/`, `config/`, and `archive/` branch taxonomy described in
  Pattern 6. Cross-reference `docs-ghaw-agentic-ops.md` Claims 6–7 for a
  production implementation of two workflows sharing a single named `repo-memory`
  branch (`branch-name: "memory/token-audit"`).

### Claim 8: `create-orphan: true` (default) creates Repo Memory branches as orphan branches — without history from the parent repository — as opposed to the alternative of a shallow clone via `--depth 1`

- **Evidence**: `create-orphan` parameter description from the reference page.
- **Confidence**: settled (first-party documentation; the default value and the
  alternative mechanism are explicitly stated)
- **Quote**: "Branches auto-create as orphans (default) or clone with `--depth 1`."
- **Our assessment**: Orphan branches (the default) share no history with the
  main repository — they start at a fresh commit with no parent. This has two
  implications: (1) memory branch history is completely decoupled from code history,
  making it easy to prune or delete memory branches without affecting the main
  branch; (2) the memory branch does not carry the full repository history, keeping
  its size minimal. The `--depth 1` clone alternative would create a shallow branch
  rooted in a recent commit of the target branch — appropriate when the memory
  needs to be initialized from existing data rather than from scratch. The orphan
  default is the correct starting point for most workflows. For Ch02: document
  the orphan default as the appropriate configuration for greenfield memory stores,
  and note that `create-orphan: false` should be considered only when pre-seeding
  from existing branch history.

### Claim 9: The `target-repo` parameter routes Repo Memory storage to a different repository, enabling cross-repo memory sharing or security isolation between the workflow repository and its memory store

- **Evidence**: `target-repo` parameter in the configuration table; the
  `owner/repository` value format in the advanced configuration YAML example.
- **Confidence**: emerging (the parameter name and value format strongly imply
  cross-repo routing, but the reference page does not provide a prose description
  of this field — the purpose is inferred from the field name and example value)
- **Quote**: (no direct quote; see advanced configuration YAML in Concrete Artifacts)
- **Our assessment**: `target-repo` is the mechanism for two distinct use cases:
  (1) **Security isolation** — if the workflow repository is public but memory
  contains derived statistics that should remain private, routing memory to a
  private repository maintains the security boundary. (2) **Cross-repo sharing** —
  multiple repositories' workflows can write to the same target memory repository,
  creating an organization-level aggregated knowledge store. Both interpretations
  are consistent with the `owner/repository` format, but neither is confirmed by
  explicit documentation text. For Ch05 (Orchestration): document `target-repo`
  as a potential mechanism for multi-repo memory aggregation, with the caveat that
  this is inferred behavior pending explicit documentation confirmation.

### Claim 10: Repo Memory and Cache Memory differ on three dimensions: retention (unlimited Git history vs. 7-day GitHub Actions cache), storage backend (Git branches vs. GitHub Actions cache), and performance profile (slower write path vs. faster)

- **Evidence**: "Comparison with Cache Memory" section of the reference page,
  confirmed consistently across multiple fetch passes.
- **Confidence**: settled (first-party comparison table; the retention period and
  storage backend differences are authoritative; the performance comparison is
  qualitative rather than quantitative)
- **Quote**: (no direct quote for the table; see comparison table in Concrete
  Artifacts)
- **Our assessment**: The comparison formalizes the selection rule that
  `docs-ghaw-memory-ops.md` and `docs-ghaw-guides-memoryops.md` describe in
  pattern terms: choose Cache Memory when data is useful within 7 days and
  acceptable to lose if evicted; choose Repo Memory when data must persist
  indefinitely, benefits from version history, or needs to be shared across
  workflows. The performance asymmetry (Cache Memory is faster) is the trade-off
  cost of Repo Memory's durability: each write is a git commit and push via the
  GraphQL API, not a cache key update. For high-frequency writes, Cache Memory's
  performance advantage is meaningful; for low-frequency persistent state (daily
  summaries, rolling metrics), Repo Memory's durability advantage outweighs the
  performance cost. For Ch02: document this three-dimension comparison as the
  decision framework for storage type selection in any stateful gh-aw workflow.

### Claim 11: The security guidance prohibits storing sensitive data and ties the security boundary explicitly to repository permissions — "Repo memory follows repository permissions"

- **Evidence**: "Security" section of the reference page, confirmed verbatim.
- **Confidence**: settled (first-party security requirement; stated as an
  explicit prohibition, not a recommendation)
- **Quote**: "Don't store sensitive data in repo memory. Repo memory follows
  repository permissions."
- **Our assessment**: This is the security constraint for Repo Memory at the
  reference level, complementing the more detailed prohibition in
  `docs-ghaw-memory-ops.md` Claim 11 ("Never store credentials, API tokens, PII,
  or secrets — only aggregate statistics and anonymized data"). The reference
  page's formulation is shorter but carries the same constraint: the security
  boundary for Repo Memory is identical to the repository's visibility and
  access controls. Public repository = public memory. This has a direct implication
  for the `target-repo` parameter (Claim 9): routing memory to a private repository
  is the correct mitigation when the workflow repo is public but derived statistics
  need to remain private. For Ch03 (Safety and Verification): document the
  repository-permission equivalence as the primary security mental model for Repo
  Memory, and the `target-repo` parameter as the isolation mechanism for sensitive
  derived data.

## Concrete Artifacts

### Minimal Enablement (from `reference/repo-memory` — "Enabling Repo Memory" section)

```yaml
---
tools:
  repo-memory: true
---
```

Creates branch `memory/default`. Files accessible at `/tmp/gh-aw/repo-memory-default/`
(per reference page) or `/tmp/gh-aw/repo-memory/default/` (per patterns/guides pages —
path format discrepancy should be verified against live source).

### Full Configuration Parameter Reference (from `reference/repo-memory`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `id` | string | required (multi-config only) | Folder/mount name identifier |
| `branch-name` | string | `memory/default` or `{branch-prefix}/{id}` | Git branch name |
| `branch-prefix` | string | `memory` | Branch prefix (4–32 chars, alphanumeric, hyphens/underscores) |
| `description` | string | — | Descriptive label for the memory store |
| `file-glob` | array | — (all files) | File patterns to include in commit |
| `max-file-size` | number | 100KB | Individual file size limit |
| `max-file-count` | number | 100 | Maximum files allowed |
| `max-patch-size` | number | 10KB (max 1MB) | Total diff size limit per push |
| `target-repo` | string | current repo | Destination repository (`owner/repository` format) |
| `create-orphan` | boolean | true | Create orphan branch vs. shallow clone |
| `allowed-extensions` | array | empty (all types) | Restricted file type extensions |

### Advanced Configuration YAML (from `reference/repo-memory` — "Advanced Configuration" section)

```yaml
---
tools:
  repo-memory:
    branch-name: memory/custom-agent-for-aw
    branch-prefix: tracking
    description: "Long-term insights"
    file-glob: ["*.md", "*.json"]
    max-file-size: 1048576
    max-file-count: 50
    max-patch-size: 1048576
    target-repo: "owner/repository"
    create-orphan: true
    allowed-extensions: [".json", ".txt", ".md"]
---
```

### Multiple Configurations YAML (from `reference/repo-memory` — "Multiple Configurations" section)

```yaml
---
tools:
  repo-memory:
    - id: insights
      branch-prefix: daily
      file-glob: ["*.md"]
    - id: state
      file-glob: ["*.json"]
      max-file-size: 524288
---
```

Each id mounts at `/tmp/gh-aw/repo-memory-{id}/`. Branch name defaults to
`{branch-prefix}/{id}` (e.g., `daily/insights` for `id: insights` with
`branch-prefix: daily`).

### Repo Memory vs. Cache Memory Comparison (from `reference/repo-memory` — "Comparison with Cache Memory" section)

```
                    Cache Memory              Repo Memory
Storage backend:    GitHub Actions cache      Git branches
Retention:          7 days                    Unlimited
Version control:    No                        Yes (full commit history)
Performance:        Faster                    Slower (GraphQL commit/push per write)
Sharing:            Per-workflow (by key)     Cross-workflow (by branch name)
Best for:           Temporary session state,  Long-term historical data,
                    short-term caching,       trend tracking, cross-workflow
                    rate limit avoidance      coordination, audit trails
```

### `always()` Footgun — Correct Conditional for Memory Persistence Steps

```yaml
# WRONG: always() bypasses skip propagation — runs even on bot-triggered no-ops
- name: Push repo memory
  if: always()
  run: gh aw push-memory

# RIGHT: only persist when meaningful work was done
- name: Push repo memory
  if: success() && steps.agent.outputs.did_work == 'true'
  run: gh aw push-memory

# Why: Repo Memory's auto-commit/push is gated on "changes detected". When
# always() is used, the step runs even when gh-aw skip propagation would
# suppress it (e.g., bot-triggered events with no agent work). The platform
# already handles no-op suppression; always() overrides that protection.
# Source: blog-ghaw-weekly-2026-04-13.md Claim 7, PR #25960.
```

### Signed-Commit Guarantee and Fallback Limitation

```
Normal path (GPG-signed, enterprise-compatible):
  → GraphQL createCommitOnBranch mutation
  → Signed with GitHub's GPG key
  → Satisfies signed-commit rulesets automatically

Fallback path (UNSIGNED, fails signed-commit rulesets):
  → Triggered when content includes: symlinks, executable files (chmod +x),
    or submodule entries
  → Falls back to plain git push
  → Rejected by signed-commit rulesets

Mitigation: use allowed-extensions: [".json", ".txt", ".md"] to restrict
content to plain text/binary files without execute bits or symlinks.
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-memory-ops.md` Claims 1–3 (MemoryOps pattern page's treatment
    of Cache Memory vs. Repo Memory as two complementary storage primitives):
    The reference page's Comparison section (Claim 10) provides the formal
    specification that confirms what the patterns page describes functionally.
    The unlimited-vs-7-day retention distinction is stated identically in both.
  - `docs-ghaw-guides-memoryops.md` Claim 3 (Repo Memory provides persistent,
    version-controlled storage in a dedicated Git branch): The reference page
    confirms this characterization with the additional technical detail that
    commits use the GraphQL `createCommitOnBranch` mutation (Claim 4).
  - `docs-ghaw-agentic-ops.md` Claims 6–7: The reference implementation uses
    two coordinated workflows (daily audit + daily optimizer) that share a
    single `repo-memory` branch (`branch-name: "memory/token-audit"`,
    `max-file-size: 102400`, `max-patch-size: 51200`). This is a production
    implementation of the multi-instance pattern described in Claim 7, applied
    to a cross-workflow coordination use case rather than a single workflow with
    multiple stores. The shared branch name is the data contract between the two
    workflows — no API calls or event triggers required, just a reliable time
    separation (audit at 12:00, optimizer at 14:00).
  - `docs-ghaw-tools-reference.md` Claim 5 (two built-in memory tools as distinct
    persistence scopes — `cache-memory:` for cross-run trend data and `repo-memory:`
    for repository-specific context): The reference page's comparison table (Claim
    10) formalizes the performance and retention trade-offs that the tools reference
    describes qualitatively.
  - `blog-ghaw-weekly-2026-04-13.md` Claim 7 (`push_repo_memory` ran on every
    bot-triggered no-op because `always()` bypassed skip propagation, PR #25960):
    This is a fifth "changes not persisting" failure mode beyond the four documented
    in the MemoryOps troubleshooting sections. Claim 2's auto-commit/push trigger
    conditions explain WHY `always()` is a footgun: the platform already implements
    a "changes detected" gate; `always()` overrides that gate, causing spurious
    pushes on no-op runs. Practitioners reading Claim 2 should cross-reference this
    settled (PR-fixed) production bug as the canonical `always()` warning. For Ch02:
    add the `always()` footgun as a named anti-pattern for Repo Memory persistence
    steps, recommending `success()` or explicit output-conditional logic instead.

- **Extends**:
  - `docs-ghaw-memory-ops.md` (patterns page, issue #855) and
    `docs-ghaw-guides-memoryops.md` (guides page, issue #438): Both existing notes
    document MemoryOps at the pattern and procedure level. This reference note adds
    the technical implementation layer: the complete parameter table (11 fields with
    types and defaults), the GraphQL commit mechanism (Claims 3–4), the fallback
    limitation (Claim 5), the orphan-vs-clone branch creation modes (Claim 8), and
    the auto-commit trigger conditions (Claim 2). Together the three notes form a
    complete picture: patterns (why) → guides (how) → reference (what exactly).
  - `docs-ghaw-tools-reference.md` (issue #416): The tools reference documents
    `repo-memory:` as one of twelve tool categories. This note provides the full
    parameter reference that the tools overview intentionally omits.

- **Contradicts**:
  - **Path format discrepancy** (Claim 1 note): This reference page reports the
    default access path as `/tmp/gh-aw/repo-memory-default/` (hyphen-separated),
    while `docs-ghaw-memory-ops.md` Claim 3 and `docs-ghaw-guides-memoryops.md`
    Claim 3 both document `/tmp/gh-aw/repo-memory/default/` (slash-separated).
    All three are first-party sources. This may be an AI-summarization artifact
    from WebFetch processing, or a genuine documentation inconsistency. No
    contradiction issue filed because the discrepancy is uncertain; the Assayer
    should verify the exact path format against the live source URL. If confirmed
    as a genuine discrepancy, this would warrant a contradiction issue against
    `docs-ghaw-memory-ops.md` Claim 3 and `docs-ghaw-guides-memoryops.md` Claim 3.

- **Novel**:
  - **Complete 11-parameter configuration reference** (Claim 6 + Concrete
    Artifacts): No existing corpus note documents the full parameter surface with
    types and defaults. Prior notes reference `branch-name`, `file-glob`, and
    storage limits in isolation without a complete reference table.
  - **GraphQL `createCommitOnBranch` commit mechanism** (Claim 4): The specific
    mutation name and GPG-signing guarantee are new to the corpus. Prior notes
    describe repo-memory as "version-controlled" without explaining the commit
    mechanism or its enterprise compliance implications.
  - **Signed-commit fallback limitation** (Claim 5): The symlink/executable/
    submodule fallback to plain `git push` (and its signed-commit ruleset failure
    mode) is entirely new to the corpus. This is a production-blocking edge case
    for enterprise deployments with signed-commit rulesets.
  - **`create-orphan` parameter semantics** (Claim 8): The orphan-vs-shallow-clone
    tradeoff is not documented in any existing corpus note.
  - **Auto-commit trigger conditions** (Claim 2): The explicit gate conditions
    (file-glob validation + max-file-size + max-file-count + changes detection +
    threat detection) are new. Prior notes describe auto-commit as a simple "after
    workflow completion" behavior without the validation and detection gates.
  - **`target-repo` parameter** (Claim 9): The ability to route memory storage
    to a different repository is not documented in any existing corpus note. This
    is a significant capability for multi-repo orchestration and security isolation.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - **Add the complete parameter reference as a configuration starting point**
    (Claim 6): Teams designing Repo Memory configurations should see the full
    parameter surface (11 fields) with defaults, not just the subset referenced
    in pattern examples. The `file-glob` + `allowed-extensions` combination for
    type-safe, signed-commit-compatible memory is the recommended starting
    configuration for any workflow deployed in an enterprise environment.
  - **Add the `always()` footgun as a named anti-pattern** (Claim 2,
    `blog-ghaw-weekly-2026-04-13.md` Claim 7): Memory persistence steps must
    use `success()` or output-conditional logic, not `always()`. The platform's
    "changes detected" gate already handles no-op suppression; `always()` overrides
    it. Document the PR #25960 fix as the canonical production example.
  - **Add the signed-commit guarantee and fallback limitation** (Claims 4–5):
    Repo Memory is enterprise-signed-commit-compatible by default, but only for
    plain text/binary files without execute bits or symlinks. Document
    `allowed-extensions: [".json", ".txt", ".md"]` as the recommended mitigation.
  - **Add auto-commit trigger conditions** (Claim 2): The validation gates
    (file-glob, max-file-size, max-file-count) determine what gets committed.
    Misconfigured file-globs are the most common "files not persisting" failure
    mode (corroborated by the MemoryOps troubleshooting guides).

- **Chapter 05 (Multi-Agent Orchestration)**:
  - **Add `target-repo` as a cross-repo memory sharing mechanism** (Claim 9):
    Multiple workflows across different repositories can share a single Repo
    Memory store by pointing `target-repo` to a shared destination. This enables
    organization-level knowledge aggregation without API-based orchestration.
    Document with the caveat that this is inferred behavior pending explicit
    documentation confirmation.
  - **Corroborate cross-workflow Repo Memory sharing with production example**
    (Claim 7, `docs-ghaw-agentic-ops.md` Claims 6–7): The daily audit + daily
    optimizer pattern (two workflows sharing `memory/token-audit` with a 2-hour
    time offset) is the concrete production template for loose-coupled cross-
    workflow coordination via shared Repo Memory. Include the `branch-name:
    "memory/token-audit"` sharing pattern alongside the `target-repo` mechanism.

- **Chapter 08 (Enterprise and Compliance)**:
  - **Add GraphQL signed-commit guarantee as enterprise enabler** (Claim 4):
    Repo Memory writes are automatically GPG-signed via the GraphQL
    `createCommitOnBranch` mutation — no additional configuration required to
    satisfy signed-commit rulesets. Document alongside other enterprise-compatible
    gh-aw defaults.
  - **Add the symlink/executable fallback as a compliance risk** (Claim 5):
    Any Repo Memory content that includes symlinks or executable files bypasses
    the signed-commit path. Document `allowed-extensions` as the recommended
    mitigation for compliance-sensitive deployments.
  - **Add `target-repo` as a security isolation mechanism** (Claim 9): When the
    workflow repository is public (or semi-public) but memory stores derived
    statistics that should remain private, routing via `target-repo` to a private
    repository maintains the appropriate security boundary.

## Extraction Notes

1. **WebFetch processes through an AI model, not raw HTML**: The
   `reference/repo-memory` page is a single-page application. `WebFetch` returns
   AI-summarized markdown rather than the raw source. Quotes that appeared
   consistently in the same or near-identical form across multiple independent
   fetch passes are cited as direct quotes. All other claims use `(no direct quote;
   see paraphrase in Our assessment)`. The Assayer should verify quoted passages
   against the live source URL. This limitation applies equally to all
   `docs-ghaw-*` source notes using WebFetch.

2. **Path format discrepancy — verify against live source**: The reference page
   returns `/tmp/gh-aw/repo-memory-default/` (hyphen) while the patterns and
   guides pages show `/tmp/gh-aw/repo-memory/default/` (slash). This discrepancy
   appeared across all fetch passes of the reference page. It may be an AI
   summarization artifact, or it may reflect a genuine documentation inconsistency.
   The correct path format is important for practitioners — document only after
   live-source verification.

3. **`target-repo` prose description absent**: The reference page does not appear
   to provide a prose description of the `target-repo` parameter beyond the
   `owner/repository` value format in the example YAML. Claim 9 is marked
   `emerging` and should be verified. A prose description in the live source
   would upgrade this to `settled`.

4. **Example sub-pages not followed**: The reference page links to workflow
   examples ("Deep Report", "Daily Firewall Report") from the Examples section.
   These are practitioner workflow examples, not configuration documentation.
   Not followed in this extraction; they would be appropriate for a separate
   blog-post source issue, not a reference note.

5. **Confidence_overall `emerging` reconciliation**: Individual claims are graded
   `settled` where the parameter names, defaults, and behavioral mechanics are
   explicitly documented (e.g., the commit mutation name, the GPG signing guarantee,
   the orphan default). The overall `emerging` grade reflects that: (a) the path
   format discrepancy is unresolved (Claim 1); (b) `target-repo` purpose is inferred
   (Claim 9); (c) guide application patterns (e.g., how teams should compose
   `allowed-extensions` with enterprise rulesets) are unvalidated in the wild.
   Claims that are individually settled as platform specs may collectively form
   emerging guide patterns when combined.

6. **Prior PR #684 closed without merge**: The previous Miner attempt (PR #684,
   May 12, 2026) received Assayer REQUEST CHANGES for: (a) missing
   `blog-ghaw-weekly-2026-04-13.md` Claim 7 cross-reference (the `always()`
   footgun); (b) missing `docs-ghaw-agentic-ops.md` Claims 6–7 cross-reference
   (production shared repo-memory implementation); (c) Claim 4 `target-repo`
   confidence graded `settled` when it should be `emerging`. All three issues are
   addressed in this note. PR #684 was subsequently closed by the maintainer as
   part of a pipeline dispatch-rate-limit cleanup (not due to Assayer failure);
   this note is the fresh attempt on a new branch.
