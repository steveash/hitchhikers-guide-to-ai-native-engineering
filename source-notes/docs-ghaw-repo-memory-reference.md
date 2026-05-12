---
source_url: https://github.github.com/gh-aw/reference/repo-memory
source_type: docs
title: "GitHub Agentic Workflows: Repo Memory Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#410"
---

# GitHub Agentic Workflows: Repo Memory Reference

> The authoritative reference for `repo-memory:` — the gh-aw tool for unlimited
> Git-branch-backed persistent file storage — covering basic setup, the full
> advanced configuration surface (branch naming, file restrictions, size limits,
> multi-instance IDs, target repos), signed-commit behavior and its fallback
> limitations, concurrent-push conflict resolution, the contrast with 7-day
> cache-memory, and four documented troubleshooting failure modes.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/repo-memory` page —
  in the "Reference" section. Dedicated reference for the `repo-memory:` tool,
  distinct from the broader `docs-ghaw-tools-reference.md` which catalogues all
  twelve gh-aw tools including `repo-memory:` and `cache-memory:` at a
  higher level.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team operating the gh-aw platform. Configuration fields, defaults,
  behavioral claims (signed commits, conflict resolution, GraphQL mutation), and
  security guidance are authoritative for the `gh aw` platform. Defaults and
  limits cited here (10KB file size, 100KB max patch, 7-day cache-memory
  retention) are platform specifications, not general advice.
- **Scope**: Complete reference for the `repo-memory:` tool — enablement, advanced
  configuration, behavioral mechanics, comparison with `cache-memory:`,
  troubleshooting, and security. Does NOT cover: `cache-memory:` configuration
  in depth (separate reference), network controls, permissions for write
  operations, or the MCP server configuration that might interact with memory
  tools.

## Extracted Claims

### Claim 1: `repo-memory:` provides persistent file storage via Git branches with unlimited retention, contrasting with `cache-memory:`'s 7-day GitHub Actions Cache backend

- **Evidence**: The overview section states the unlimited-retention positioning
  directly. The comparison table distinguishes the two memory tools explicitly:
  Cache Memory → GitHub Actions Cache, 7 days; Repo Memory → Git Branches,
  Unlimited. This comparison is the primary framing device of the page.
- **Confidence**: settled (first-party documentation; the retention distinction
  is the defining characteristic of the tool)
- **Quote**: "Repo memory provides persistent file storage via Git branches with
  unlimited retention."
- **Our assessment**: The unlimited-retention property is the primary selection
  criterion between the two memory tools. Agent state that must survive longer
  than 7 days (long-running investigations, learned repository conventions, multi-
  week project context) must use `repo-memory:`. The Git-branch storage model also
  provides version history — each push is a signed commit — which `cache-memory:`
  does not. However, `cache-memory:` is described as "fast" (GitHub Actions Cache)
  while `repo-memory:` is "slower" (Git operations), making `cache-memory:` the
  better choice for frequently-updated temporary state within a sprint or session.
  See `docs-ghaw-tools-reference.md` Claim 5 for the higher-level two-scope
  distinction.

### Claim 2: Basic enablement requires a single `tools: repo-memory: true` declaration, which auto-creates a `memory/default` branch and mounts files at `/tmp/gh-aw/repo-memory-default/`

- **Evidence**: The "Enabling Repo Memory" section gives the minimal YAML
  configuration, branch name, and mount path explicitly.
- **Confidence**: settled (first-party documentation with explicit code example and
  path values)
- **Quote**: (no direct prose quote; the YAML and mount path appear in the code
  example and following text: `tools: repo-memory: true` → branch `memory/default`
  → mount at `/tmp/gh-aw/repo-memory-default/`)
- **Our assessment**: The single-line enablement hides significant infrastructure:
  branch creation, file checkout, commit signing, and push are all automated. The
  `/tmp/gh-aw/repo-memory-{id}/` path pattern means the agent writes to a
  conventional location, and the platform handles the git mechanics. For Ch02
  (Harness Engineering): document `tools: repo-memory: true` as the entry-level
  one-liner for agent state persistence; contrast with the advanced configuration
  (Claim 4) for workflows that need more control.

### Claim 3: The compiler auto-configures all Git operations — branch cloning/creation, file access, commit signing, and push — with conflict resolution that favors the current workflow's changes

- **Evidence**: The Behavior section describes the automated Git operations and
  names the conflict resolution semantics: "your changes win" when concurrent
  workflows have pushed to the branch since checkout.
- **Confidence**: settled (first-party documentation; the specific conflict resolution
  semantics are explicitly stated)
- **Quote**: "The compiler auto-configures branch cloning/creation, file access at
  `/tmp/gh-aw/repo-memory-{id}/`, commits/pushes, and merge conflict resolution
  (your changes win)."
- **Our assessment**: The "your changes win" conflict resolution is important for
  multi-workflow deployments where several concurrent runs write to the same memory
  branch. The GraphQL mutation's automatic replay mechanism (Claim 6) implements
  this: the current run's diff is replayed on top of the latest remote state after
  a concurrent push is detected. This is an automatic last-writer-wins-by-diff
  strategy — different from full last-writer-wins (which would discard the earlier
  writer's changes) because the replay applies the *diff*, not the final file state.
  If two concurrent runs modify different files, both changes survive.

### Claim 4: Advanced configuration supports custom branch naming, file type restrictions, per-file and per-patch size limits, target repository, orphan branch control, and a description field

- **Evidence**: The "Advanced Configuration" section enumerates the full set of
  configuration keys with a complete YAML example.
- **Confidence**: settled (first-party documentation with explicit YAML schema example)
- **Quote**: (no single prose quote; the fields are documented in the YAML example
  with descriptions for each key)
- **Our assessment**: The advanced configuration surface is broader than typical
  first impressions suggest. Of particular note: `target-repo` allows the memory
  branch to be hosted in a different repository than the workflow's repository,
  enabling cross-repository memory stores (an org-level agent memory pattern). The
  `file-glob` pattern restricts which files the tool monitors (not just what can
  be stored — `allowed-extensions` handles that), enabling selective tracking. The
  `create-orphan: true` field is required when the target branch does not already
  exist; workflows that fail with "Branch not created" errors likely need this flag.

### Claim 5: `max-file-size` defaults to 10KB and `max-file-count` to 100 files; `max-patch-size` defaults to 10KB with a hard ceiling of 100KB per push

- **Evidence**: The Advanced Configuration section documents these three limits
  with their defaults explicitly.
- **Confidence**: settled (first-party documentation; the defaults and maximum are
  stated)
- **Quote**: "Use `max-patch-size` to limit the total size of changes in a single
  push (default: 10KB, max: 100KB)."
- **Our assessment**: The 10KB default `max-file-size` is a conservative limit for
  text-based state files (JSON, Markdown). Workflows storing rich structured data
  (e.g., issue history, analysis results) may need to increase this. The 100KB
  `max-patch-size` ceiling is a hard platform limit — it cannot be configured
  higher. Workflows that accumulate large diffs (e.g., appending log entries or
  large JSON blobs per run) will hit this ceiling and need a compaction strategy
  (e.g., summarizing old entries, archiving to separate branches). The "Patch too
  large" troubleshooting entry confirms this is a known failure mode.

### Claim 6: Commits are pushed via GitHub's GraphQL `createCommitOnBranch` mutation, automatically signing each commit with GitHub's GPG key — satisfying enterprise rulesets that require verified signatures

- **Evidence**: The Behavior section names the GraphQL mutation and the automatic
  signing behavior explicitly.
- **Confidence**: settled (first-party documentation; the mutation name and signing
  mechanism are stated)
- **Quote**: "Commits are pushed via the GitHub GraphQL `createCommitOnBranch`
  mutation, which signs each commit with GitHub's GPG key."
- **Our assessment**: The automatic commit signing is operationally significant for
  organizations that enforce branch protection rules requiring verified commits.
  Memory updates to the `repo-memory` branch are verified by default without any
  additional GPG key configuration on the workflow side. This is a practical
  advantage over a naive `git push` approach, which would produce unverified commits
  unless the workflow's GitHub token had signing configured. The signing is a
  consequence of using the GitHub GraphQL API rather than native git — a design
  choice that provides enterprise compliance as a side effect.

### Claim 7: The GraphQL `createCommitOnBranch` mutation does not support symlinks, executable files, or submodule entries — these trigger a fallback to unsigned `git push`

- **Evidence**: The Behavior section states the fallback limitation explicitly,
  naming the three unsupported file types.
- **Confidence**: settled (first-party documentation; the three unsupported types
  are named and the fallback behavior is stated)
- **Quote**: "The GraphQL mutation does not support symlinks, executable files
  (`chmod +x`), or submodule entries."
- **Our assessment**: The fallback to unsigned `git push` is a silent security
  downgrade — workflows that store symlinks, executables, or submodule references
  lose the verified-signature guarantee (Claim 6) without an explicit warning to
  the practitioner. This matters for organizations with `required-signed-commits`
  branch protection on the memory branch. For Ch02: practitioners using repo-memory
  on repositories with verified-commit requirements should audit their memory files
  for symlinks and executable flags. The practical mitigation is to use
  `allowed-extensions` (Claim 4) to restrict stored file types to `.json`, `.md`,
  or `.txt` — types that cannot be executables or symlinks.

### Claim 8: Concurrent-push conflicts are resolved automatically by replaying the current workflow's file diff on top of the latest remote state ("your changes win")

- **Evidence**: The Troubleshooting section explicitly documents the concurrent-push
  resolution mechanism.
- **Confidence**: settled (first-party documentation; the resolution mechanism is
  described explicitly)
- **Quote**: "Concurrent pushes are handled: if another run has pushed since the
  branch was checked out, the GraphQL mutation replays your file diff on top of
  the latest remote state (your changes win)."
- **Our assessment**: The diff-replay strategy means "your changes win" is actually
  a merge, not a simple overwrite. Each concurrent run's diff (the specific file
  changes made during that run) is applied to the current remote HEAD rather than
  replacing it. If two runs modify different files, both changes survive. If two
  runs modify the same file, the later replay wins for those overlapping lines —
  consistent with the "your changes win" semantics. This is adequate for most
  agent state patterns (different agents writing to different files, or appending
  to log files). It is not adequate for shared counters or structured data where
  two concurrent agents modify the same field.

### Claim 9: `repo-memory:` supports multiple independent instances per workflow via unique `id` values, each creating its own branch and mount point

- **Evidence**: The "Multiple Configurations" section provides a YAML example with
  two repo-memory entries using `id: insights` and `id: state`, demonstrating that
  a single workflow can maintain multiple independent memory stores.
- **Confidence**: settled (first-party documentation with explicit YAML example)
- **Quote**: (no direct prose quote; the YAML example shows the multi-instance
  configuration with IDs `insights` and `state`)
- **Our assessment**: Multiple instances enable logical separation of memory
  concerns within a single workflow: e.g., one memory store for structured agent
  state (JSON files, fast-changing), another for long-form analysis artifacts
  (Markdown files, slow-changing, larger). Each instance gets its own branch
  (e.g., `daily/insights` and `memory/state` for the example above) and its own
  mount point at `/tmp/gh-aw/repo-memory-{id}/`. The `file-glob` and
  `allowed-extensions` configuration can be tailored per instance. For Ch05
  (State & Memory): document multi-instance repo-memory as the canonical pattern
  for workflows with heterogeneous state requirements.

### Claim 10: Security guidance: do not store sensitive data in repo-memory; it follows repository permissions; private repositories provide better isolation

- **Evidence**: The Security section gives explicit recommendations.
- **Confidence**: settled (first-party documentation; the security advice is stated
  as authoritative guidance)
- **Quote**: "Don't store sensitive data in repo memory. Repo memory follows
  repository permissions."
- **Our assessment**: "Follows repository permissions" means any user or system
  with read access to the repository (or the `target-repo`, if configured) can
  read the memory branch and all its history. This is a broader audience than
  the workflow's runtime permissions — repository collaborators with read access
  can inspect agent memory even if they cannot modify workflows. Practitioners
  should treat repo-memory as a semi-public artifact within their organization.
  For Ch02: when documenting repo-memory, include a security caveat that memory
  branches are readable by all repository collaborators — store conclusions and
  learned patterns, not credentials, tokens, API responses containing PII, or
  intermediate reasoning that includes sensitive business data.

### Claim 11: Four documented troubleshooting failure modes cover the primary error categories for repo-memory deployments

- **Evidence**: The Troubleshooting section names four failure modes with specific
  causes and fixes.
- **Confidence**: settled (first-party documentation; the failure modes are named
  with explicit causes)
- **Quote**: (no single direct quote covers all four; each failure mode appears
  as a labeled entry in the troubleshooting section)
- **Our assessment**: The four failure modes form a practical operational checklist:
  (1) "Branch not created" → add `create-orphan: true`; (2) "Validation failures"
  → mismatched file patterns or exceeded size constraints; (3) "Patch too large" →
  reduce diff size or raise `max-patch-size` (hard ceiling 100KB); (4) "Changes not
  persisting" → check directory path matches `/tmp/gh-aw/repo-memory-{id}/` and
  review workflow logs. The "Validation failures" entry implies the platform runs
  validation before committing, which means malformed or oversized files cause a
  runtime error rather than silent data loss — a useful property for debugging.

## Concrete Artifacts

### Minimal Enablement (Source: Enabling Repo Memory section)

```yaml
---
tools:
  repo-memory: true
---
```

Creates: branch `memory/default` — mount: `/tmp/gh-aw/repo-memory-default/`

### Full Advanced Configuration (Source: Advanced Configuration section)

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
    max-patch-size: 102400
    target-repo: "owner/repository"
    create-orphan: true
    allowed-extensions: [".json", ".txt", ".md"]
---
```

### Multiple Instances Configuration (Source: Multiple Configurations section)

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

Creates: branch `daily/insights` → mount `/tmp/gh-aw/repo-memory-insights/`
         branch `memory/state` → mount `/tmp/gh-aw/repo-memory-state/`

### Cache Memory vs. Repo Memory Comparison (Source: Comparison with Cache Memory section)

```
Feature          | Cache Memory          | Repo Memory
-----------------|-----------------------|---------------------------
Storage Backend  | GitHub Actions Cache  | Git Branches
Retention Period | 7 days                | Unlimited
Version Control  | No                    | Yes
Performance      | Fast                  | Slower
Best For         | Temporary/sessions    | Long-term/history
Size Limit       | 10GB/repo             | Repository limits
```

### Default Limits Summary (Source: Advanced Configuration and Behavior sections)

```
max-file-size:   10KB  (default) — configurable upward
max-file-count:  100   (default) — configurable
max-patch-size:  10KB  (default) — configurable up to hard ceiling of 100KB
Branch prefix:   memory (default) — customizable via branch-prefix
Orphan creation: true  (default behavior for new branches)
Clone depth:     --depth 1 (when cloning existing branch)
Commit signing:  GitHub GPG key via createCommitOnBranch mutation
```

### Troubleshooting Reference (Source: Troubleshooting section)

```
Symptom                | Cause                              | Fix
-----------------------|------------------------------------|-------------------------------
Branch not created     | Branch doesn't exist and           | Add create-orphan: true
                       | create-orphan not set              |
Validation failures    | File types or sizes exceed limits  | Match allowed-extensions and
                       |                                    | max-file-size constraints
Patch too large        | Diff exceeds max-patch-size        | Reduce changes or increase
                       |                                    | max-patch-size (hard max 100KB)
Changes not persisting | Wrong directory path or log error  | Verify /tmp/gh-aw/repo-memory-
                       |                                    | {id}/ path; check workflow logs
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-tools-reference.md` Claim 5 ("Two built-in memory tools serve
    distinct persistence scopes — `cache-memory:` for cross-run trend data and
    `repo-memory:` for repository-specific context"): this source's comparison
    table confirms the two-scope distinction. The high-level characterization in
    that note is accurate; this source adds the full technical detail behind it.
  - `blog-ghaw-weekly-2026-03-30.md` Claim 1 (integrity-aware cache-memory via
    git branches for trust-level isolation in v0.64.3): that note documents a
    git-branch-based integrity isolation layer applied *to* cache-memory, not
    that cache-memory's primary storage is git branches. Consistent with this
    source's table showing cache-memory uses GitHub Actions Cache as its primary
    backend — the two notes address different layers of the cache-memory design.

- **Extends**:
  - `docs-ghaw-tools-reference.md` Claim 5: That note describes the two memory
    tools at a single-paragraph level ("Repository-specific memory storage for
    maintaining context across executions"). This source is the dedicated reference
    page providing the full configuration schema, behavioral mechanics, conflict
    resolution, signed-commit design, and troubleshooting.
  - `blog-anthropic-claude-managed-agents-memory.md` (Anthropic Managed Agents
    memory via filesystem mount): Both sources describe agent state that persists
    across sessions and is accessible to agents via familiar I/O primitives.
    However, they are architecturally distinct platforms: Anthropic's approach
    mounts memory onto a filesystem so agents use bash/code execution; gh-aw's
    `repo-memory:` uses Git branches with automatic commit management. Neither
    contradicts the other — they are competing design approaches to the same
    underlying problem. Relevant for Ch05: include both as reference implementations
    with different trade-off profiles (Git audit trail + unlimited retention vs.
    filesystem simplicity + enterprise governance layer).

- **Contradicts**: None found. The retention and storage characterizations here are
  consistent with every existing corpus note that references these tools.

- **Novel**:
  - **Full configuration schema for `repo-memory:`** (Claim 4): No prior corpus
    note documents the complete advanced configuration surface —
    `branch-name`, `branch-prefix`, `description`, `file-glob`, `max-file-size`,
    `max-file-count`, `max-patch-size`, `target-repo`, `create-orphan`,
    `allowed-extensions`. `docs-ghaw-tools-reference.md` mentions the tool but
    not the configuration.
  - **Signed-commit mechanism and fallback limitation** (Claims 6, 7): The
    `createCommitOnBranch` GraphQL mutation, the automatic GitHub GPG signing,
    and the fallback to unsigned `git push` for unsupported file types are not
    documented in any existing corpus note. The security implication (silent
    downgrade when storing symlinks/executables) is new.
  - **Diff-replay conflict resolution** (Claim 8): The specific "replay your
    file diff on top of the latest remote state" mechanism is new to the corpus.
    Prior notes acknowledge concurrent access as a concern; this is the first
    documented resolution strategy.
  - **Multi-instance configuration via IDs** (Claim 9): The ability to run
    multiple independent repo-memory instances within one workflow, each with
    its own branch and mount point, is not documented elsewhere.
  - **Default limits as a compaction signal** (Claim 5): The 100KB hard ceiling
    on `max-patch-size` implies a compaction requirement for workflows that
    accumulate large diffs over time — not previously identified as a design
    constraint in any corpus note.
  - **`target-repo` enabling cross-repository memory stores** (Claim 4): The
    ability to host memory branches in a different repository opens an org-level
    shared memory pattern not documented anywhere in the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add `tools: repo-memory: true` as the
  canonical one-liner for agent state persistence. Document the `allowed-extensions`
  + file type constraint as the best-practice mitigation for the signed-commit
  fallback (Claim 7). Contrast with `cache-memory:` using the comparison table:
  choose `repo-memory:` for state that must outlive 7 days or where audit history
  is valuable; choose `cache-memory:` for high-frequency ephemeral state.

- **Chapter 05 (State & Memory)**: This source should be the primary reference for
  the `repo-memory:` implementation pattern. The multi-instance configuration
  (Claim 9) should be documented as the canonical pattern for workflows with
  heterogeneous state (structured JSON state in one store, analysis artifacts in
  another). The `target-repo` option (Claim 4) enables an org-level shared memory
  pattern worth calling out explicitly — a team of agents sharing a central memory
  repository. The 100KB patch ceiling (Claim 5) should be called out as a compaction
  forcing function: long-lived agents need a strategy for keeping per-commit diffs
  under the hard ceiling.

- **Chapter 02 or Ch08 (Security / Governance)**: The signed-commit fallback
  (Claim 7) should be documented as a security consideration alongside
  `allowed-extensions` as the primary mitigation. The "follows repository
  permissions" scoping (Claim 10) means practitioners must treat memory branch
  contents as semi-public within their organization. Add this to any security
  checklist for gh-aw deployments.

- **Chapter 05 (State & Memory) — comparative section**: Include `repo-memory:`
  alongside `blog-anthropic-claude-managed-agents-memory.md`'s filesystem approach
  as two reference implementations of persistent agent memory, differing in
  platform, governance model, and storage mechanism.

## Extraction Notes

1. **WebFetch returns summarized content**: The gh-aw documentation pages are
   rendered SPAs; WebFetch processes HTML into AI-summarized markdown rather than
   returning raw page source. Three fetches were performed to maximize content
   fidelity. Quotes marked as direct quotes appeared consistently across at least
   two fetches with the same wording. Configuration values (defaults, maximums, the
   GraphQL mutation name, the mount path pattern) appeared consistently. Claims
   where the specific wording varied between fetches are marked
   "(no direct quote; see paraphrase in Our assessment)."

2. **No publication date**: gh-aw documentation pages do not carry explicit
   publication dates. `date_published` is left null. Content reflects the platform
   state as of 2026-05-12.

3. **Examples section — limited detail**: The final sections of the page reference
   "Deep Report" and "Daily Firewall Report" as example workflows using repo-memory.
   These were not followed as sub-pages; they are described as reference examples,
   not configuration documentation.

4. **No contradictions filed**: Reviewed all existing corpus notes for conflicting
   claims about repo-memory, cache-memory retention, Git branch storage, or commit
   signing. No material contradictions found. The `blog-ghaw-weekly-2026-03-30.md`
   reference to "integrity-aware cache-memory via git branches" describes a
   trust-segmentation *layer on top of* cache-memory's GitHub Actions Cache backend,
   not a claim that cache-memory uses git branches as its primary storage.

5. **`target-repo` interpretation**: The presence of a `target-repo` field in
   the advanced configuration example implies memory can be stored in a different
   repository. This interpretation is consistent with the field name and the
   `owner/repository` value format shown in the example. The source does not
   give a prose description of this field beyond the example YAML.
