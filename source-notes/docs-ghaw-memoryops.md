---
source_url: https://github.github.com/gh-aw/guides/memoryops
source_type: docs
title: "GitHub Agentic Workflows: MemoryOps Guide"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#438"
---

# GitHub Agentic Workflows: MemoryOps Guide

> General pattern library for stateful agent workflows — six named patterns covering
> exhaustive processing, state persistence, shared information, API caching, trend
> computation, and multiple memory stores, with concrete TTL recommendations, JSON
> Lines guidance, security constraints, and troubleshooting for the two gh-aw
> persistence primitives (cache-memory and repo-memory).

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `guides/memoryops` page — in the
  `guides/` section alongside other practitioner how-to guides. Guides pages are
  prescriptive implementation references, distinct from the conceptual `introduction/`
  pages and the named `patterns/` pages such as `patterns/agentic-ops` and
  `patterns/workqueue-ops`. This page is the cross-cutting reference for both
  `cache-memory` and `repo-memory` usage across all workflow types.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team
  (GitHub Next / Microsoft Research — the same team behind Peli de Halleux's "Agent
  Factory" blog series, the `gh aw` CLI, and all other `guides/` pages in the corpus).
  Tool configurations, file paths, and TTL recommendations are authoritative for the
  `gh aw` platform. The six patterns are practitioner-validated design guidance, not
  formally benchmarked experiments.
- **Scope**: Covers the two gh-aw persistence primitives (`cache-memory` and
  `repo-memory`) and six named usage patterns for stateful agent workflows. Provides
  best practice guidance (JSON Lines, data rotation, metadata, state validation),
  security constraints, and troubleshooting for both primitives. Does NOT cover: the
  Agentic Ops reference implementation (see `docs-ghaw-agentic-ops.md`), WorkQueueOps'
  four queue strategies (see `docs-ghaw-workqueue-ops.md`), how audit workflows consume
  cached state (see `docs-ghaw-audit-with-agents.md`), or the compilation process for
  workflow frontmatter (see `docs-ghaw-compilation-process.md`).

## Extracted Claims

### Claim 1: MemoryOps is the gh-aw pattern for stateful workflows — using `cache-memory` and `repo-memory` to persist progress, resume after interruptions, share data, and avoid API throttling

- **Evidence**: Opening paragraph of the page, confirmed consistently across multiple
  fetch passes.
- **Confidence**: settled (first-party documentation; the opening is the page's own
  scope definition, not a practitioner inference)
- **Quote**: "MemoryOps enables workflows to persist state across runs using
  `cache-memory` and `repo-memory`. Build workflows that remember their progress,
  resume after interruptions, share data between workflows, and avoid API throttling."
- **Our assessment**: The four goals — remember progress, resume after interruptions,
  share data, avoid throttling — map directly to the four patterns that use `repo-memory`
  (Patterns 1, 2, 3) and `cache-memory` (Pattern 4). This is the clearest statement of
  when stateful agent design is warranted. For Ch02 (Harness Engineering): use this
  four-goal framing as the adoption criteria for adding MemoryOps — if a workflow needs
  any of these four properties, it needs one of the two persistence primitives.

### Claim 2: `cache-memory` is fast ephemeral storage at `/tmp/gh-aw/cache-memory/` backed by GitHub Actions cache with 7-day retention — appropriate for temporary state and session data

- **Evidence**: Cache Memory section of the page, confirmed across multiple fetch passes
  with consistent path and retention period values.
- **Confidence**: settled (first-party documentation; path and retention values are
  authoritative configuration details)
- **Quote**: "Fast, ephemeral storage using GitHub Actions cache (7 days retention)"
- **Our assessment**: The 7-day retention window is the key design constraint for
  `cache-memory`. Workflows that run less than weekly may experience cache misses and
  must handle cold-start gracefully (the state validation pattern in Best Practices
  addresses this). The `/tmp/gh-aw/cache-memory/` path is the stable mount point for
  all cache-memory reads and writes — consistent with `docs-ghaw-audit-with-agents.md`
  Claim 5 and `docs-ghaw-workqueue-ops.md` Claim 5, which both use this same path.
  For Ch02: document `cache-memory` as the single-workflow, short-lived state primitive,
  with 7-day retention as the key constraint on usage patterns.

### Claim 3: `repo-memory` is persistent version-controlled storage at `/tmp/gh-aw/repo-memory/default/` in a dedicated git branch — appropriate for historical data, trend tracking, and permanent state shared between workflows

- **Evidence**: Repository Memory section of the page, confirmed across multiple fetch
  passes. The path and storage model are consistent with the YAML config shown in
  `docs-ghaw-agentic-ops.md` Claim 7.
- **Confidence**: settled (first-party documentation; path and storage model are
  authoritative; corroborated by agentic-ops reference implementation)
- **Quote**: "Persistent, version-controlled storage in a dedicated Git branch"
- **Our assessment**: The "version-controlled" characterization is the key differentiator
  from `cache-memory` — repo-memory commits are visible in git history, making the state
  human-inspectable and auditable. Unlike cache-memory's 7-day limit, repo-memory has no
  retention limit (permanent state). The path `/tmp/gh-aw/repo-memory/default/` is the
  default branch mount; workflows using a named branch (e.g., `memory/token-audit`) access
  state at that path rather than the default. For Ch02: document `repo-memory` as the
  cross-workflow, permanent-state primitive. Distinguish: use `repo-memory` when (1) state
  must outlive 7 days, (2) multiple workflows share the state, or (3) human inspectability
  of state history is required.

### Claim 4: Pattern 1 (Exhaustive Processing) — checkpoint files with todo/done/errors/last_run fields track progress through large datasets across multiple runs, ensuring complete coverage

- **Evidence**: Pattern 1 section with the JSON schema for the checkpoint file. The
  four-field structure (todo, done, errors, last_run) is documented in the code example.
- **Confidence**: settled (first-party documentation; JSON structure is verbatim from
  the pattern page)
- **Quote**: "Track progress through large datasets with todo/done lists to ensure
  complete coverage across multiple runs."
- **Our assessment**: The todo/done/errors/last_run schema is a minimal but complete
  checkpoint contract. The `errors` field distinguishes items that failed (should be
  retried or flagged) from items not yet processed (still in `todo`). The `last_run`
  Unix timestamp enables freshness detection. This pattern directly underlies
  `docs-ghaw-workqueue-ops.md` Claim 5, which describes the same JSON structure at
  `/tmp/gh-aw/cache-memory/workqueue.json` as the Cache-Memory queue strategy. For Ch02:
  the Exhaustive Processing pattern is the general case; WorkQueueOps' Cache-Memory
  strategy is the specific application to work queues.

### Claim 5: Pattern 2 (State Persistence) — JSON checkpoint with last_processed_id, batch_number, total_migrated, and status fields enables long-running workflow resumption after timeout

- **Evidence**: Pattern 2 section with the JSON checkpoint schema. The four fields are
  documented in the code example.
- **Confidence**: settled (first-party documentation; JSON structure is verbatim from
  the pattern page)
- **Quote**: "Save workflow checkpoints to resume long-running tasks that may timeout."
- **Our assessment**: State Persistence is the simpler linear-progress case (one
  sequential cursor: `last_processed_id`) versus Exhaustive Processing's set-based
  approach (todo/done lists). The `status: "in_progress"` field signals that resumption
  is expected, not that the workflow failed. The `batch_number` field enables batching
  without re-starting from scratch. For Ch02: document State Persistence as the correct
  pattern for workflows processing a numbered sequence (IDs, paginated APIs, ordered
  records) and Exhaustive Processing for unordered sets where any item may fail
  independently.

### Claim 6: Pattern 3 (Shared Information) — repo-memory with a named branch (e.g., `memory/shared-data`) is the coordination mechanism for producer-consumer multi-workflow architectures

- **Evidence**: Pattern 3 section with the YAML config showing `branch-name: memory/shared-data`.
  Consistent with `docs-ghaw-agentic-ops.md` Claim 6 (audit+optimizer sharing
  `memory/token-audit`) but generalized to any producer-consumer pair.
- **Confidence**: settled (first-party documentation; YAML config is verbatim; corroborated
  by the agentic-ops reference implementation)
- **Quote**: "Share data between workflows using repo-memory branches."
- **Our assessment**: The branch-name is the namespace for shared state — all workflows
  that reference the same `branch-name` read and write to the same git branch. This is
  the explicit documentation of the pattern that `docs-ghaw-agentic-ops.md` Claim 6
  uses implicitly (the audit and optimizer share `memory/token-audit`). This guide
  generalizes it: any workflow pair can coordinate via a shared `repo-memory` branch
  without synchronous communication, event dispatch, or API calls. For Ch04 (multi-agent
  orchestration): document Shared Information as the asynchronous coordination primitive —
  workflows share data through state, not through runtime communication.

### Claim 7: Pattern 4 (Data Caching) — specific TTLs by data type: repository metadata 24h, contributor lists 12h, issues/PRs 1h, workflow runs 30m

- **Evidence**: Pattern 4 section, confirmed across multiple fetch passes with consistent
  TTL values for all four data types.
- **Confidence**: emerging (first-party documentation; the TTL values are practitioner
  recommendations, not formally benchmarked against GitHub API rate limits or data
  freshness requirements — no methodology is cited)
- **Quote**: (no direct quote for the TTL table; see paraphrase in Our assessment)
- **Our assessment**: The four TTL tiers reflect data volatility: repository metadata
  changes infrequently (daily basis is fine), contributor lists change occasionally
  (12h is safe), issues and PRs change frequently (1h prevents stale decisions), workflow
  run data is the most volatile (30m reflects near-real-time monitoring needs). These
  TTLs are gh-aw team practitioner defaults, not API documentation values. Workflows
  using `cache-memory` for API response caching should use these as starting points and
  adjust based on observed data freshness requirements. For Ch02: these four TTL values
  are the only specific caching guidance in the corpus for gh-aw workflows — include them
  with the caveat that they are recommendations, not constraints.

### Claim 8: Pattern 5 (Trend Computation) — JSON Lines format with Python for moving averages and statistics is the recommended approach for time-series storage in agent workflows

- **Evidence**: Pattern 5 section description and the JSON Lines append example from the
  Best Practices section (use of `echo '...' >> data.jsonl` for append-only writes). The
  pattern instructs agents to compute 7-day and 30-day moving averages.
- **Confidence**: settled (first-party documentation; the JSON Lines recommendation is
  stated in both Pattern 5 and the Best Practices section; corroborated by the agentic-ops
  reference implementation)
- **Quote**: "Store time-series data and compute trends, moving averages, and statistics."
- **Our assessment**: JSON Lines (JSONL) is the correct format for append-only time-series
  data in agent workflows because: (1) each line is a valid JSON record, allowing
  incremental appends without rewriting the entire file, (2) `tail -n N` enables efficient
  rotation, (3) no merge conflicts — concurrent appends from separate branches remain
  line-independent. This recommendation appears in both Pattern 5 (the use case) and
  Best Practices (the implementation guidance). Cross-references: `docs-ghaw-agentic-ops.md`
  Claim 6 uses JSONL for the `rolling-summary.json` in the token-audit workflow;
  `docs-ghaw-audit-with-agents.md` Claim 5 uses `audit-trends.json` (JSON, not JSONL)
  for the rolling 30-day baseline — the MemoryOps guide's JSON Lines recommendation
  would prefer JSONL for that use case.

### Claim 9: Pattern 6 (Multiple Memory Stores) — cache-memory for session data, multiple repo-memory branches (metrics, config, archive) with different retention lifecycles, is the recommended pattern for complex stateful workflows

- **Evidence**: Pattern 6 section with the YAML config showing `cache-memory: key: session-data`
  plus `repo-memory` with three named branches (metrics, config, archive).
- **Confidence**: settled (first-party documentation; YAML config is verbatim from the page)
- **Quote**: "Use multiple memory instances for different lifecycles — cache-memory for
  temporary session data, separate repo-memory branches for metrics, configuration, and
  archives."
- **Our assessment**: The multi-store pattern is the explicit endorsement of mixing
  persistence types. The three repo-memory branches serve different purposes: metrics
  (append-only time-series), config (read-frequently, write-rarely), archive (long-term
  retention). The cache-memory handles the current session's working state. This is the
  most architecturally rich pattern in the guide, and it directly reflects what the
  agentic-ops reference implementation does (cache-memory for session data, repo-memory
  `memory/token-audit` branch for historical snapshots). For Ch02: document Multiple
  Memory Stores as the standard architecture for workflows needing both short-term
  session state and long-term historical state.

### Claim 10: Security constraint — memory stores are visible to all repository contributors; store only aggregate statistics and anonymized data, never credentials, tokens, PII, or secrets

- **Evidence**: Security Considerations section, confirmed verbatim across multiple fetch
  passes. This is the only security constraint stated on the page.
- **Confidence**: settled (first-party documentation; stated as an explicit prohibition,
  not a recommendation)
- **Quote**: "Memory stores are visible to anyone with repository access. Never store
  credentials, API tokens, PII, or secrets — only aggregate statistics and anonymized data."
- **Our assessment**: This constraint has concrete harness engineering implications:
  agent prompts must not instruct workflows to write environment-specific secrets, user
  identifiers, or raw API responses containing PII to either `cache-memory` or `repo-memory`.
  The "aggregate statistics and anonymized data" framing is the positive specification:
  counts, averages, timestamps, and aggregate rates are safe; usernames, email addresses,
  token values, and raw API payloads are not. The `docs-ghaw-agentic-ops.md` reference
  implementation follows this: it stores token counts and workflow names, not user data.
  For Ch03 (Safety and Verification): add this as a data classification requirement for
  any workflow that uses persistent memory — state written to memory must be classified
  before writing.

### Claim 11: Four troubleshooting patterns for memory failures — cache key consistency, file-glob matching, chunk processing for OOM errors, and JSON Lines/separate branches for merge conflicts

- **Evidence**: Troubleshooting section, confirmed verbatim across multiple fetch passes.
  All four items are listed with their specific causes and remedies.
- **Confidence**: settled (first-party documentation; each troubleshooting item maps to
  a specific configuration or usage failure mode)
- **Quote**: "**Merge conflicts**: Use JSON Lines format (append-only), separate branches
  per workflow, or add run ID to filenames"
- **Our assessment**: The four troubleshooting items reveal the most common failure modes
  for stateful workflows: (1) cache key drift (inconsistent keys across runs break
  persistence), (2) file-glob misconfiguration (repo-memory silently ignores files
  outside the glob), (3) OOM from loading full history (chunked processing + rotation
  prevents this), (4) merge conflicts in shared branches (JSON Lines prevents conflicts
  in shared time-series data). The merge conflict resolution guidance (JSON Lines, separate
  branches, run IDs in filenames) is the most operationally useful: teams sharing repo-memory
  branches between concurrent workflows should prefer JSON Lines for all time-series data.
  For Ch02: these four troubleshooting patterns should be in the harness engineer's
  diagnostic checklist for stateful workflow failures.

## Concrete Artifacts

### Cache Memory Configuration (from Cache Memory section)

```yaml
tools:
  cache-memory:
    key: my-workflow-state
```

Storage path: `/tmp/gh-aw/cache-memory/`
Retention: 7 days (GitHub Actions cache)

### Repository Memory Configuration (from Repository Memory section)

```yaml
tools:
  repo-memory:
    branch-name: memory/my-workflow
    file-glob: ["*.json", "*.jsonl"]
```

Storage path: `/tmp/gh-aw/repo-memory/default/`
Retention: permanent (git branch)

### Pattern 1 Checkpoint File Schema (Exhaustive Processing)

```json
{
  "todo": [123, 456, 789],
  "done": [101, 102],
  "errors": [],
  "last_run": 1705334400
}
```

### Pattern 2 Checkpoint File Schema (State Persistence)

```json
{
  "last_processed_id": 1250,
  "batch_number": 13,
  "total_migrated": 1250,
  "status": "in_progress"
}
```

### Pattern 3 Configuration (Shared Information)

```yaml
tools:
  repo-memory:
    branch-name: memory/shared-data
```

### Pattern 6 Multiple Memory Stores Configuration

```yaml
tools:
  cache-memory:
    key: session-data
  repo-memory:
    - id: metrics
      branch-name: memory/metrics
    - id: config
      branch-name: memory/config
    - id: archive
      branch-name: memory/archive
```

### Best Practice: JSON Lines Append (from Use JSON Lines section)

```bash
echo '{"date": "2024-01-15", "value": 42}' >> data.jsonl
```

### Best Practice: Metadata Document Structure

```json
{
  "dataset": "performance-metrics",
  "schema": {
    "date": "YYYY-MM-DD",
    "value": "integer"
  },
  "retention": "90 days"
}
```

### Best Practice: Data Rotation (from Implement Data Rotation section)

```bash
tail -n 90 history.jsonl > history-trimmed.jsonl
mv history-trimmed.jsonl history.jsonl
```

### Best Practice: State Validation Before Processing

```bash
if [ -f state.json ] && jq empty state.json 2>/dev/null; then
  echo "Valid state"
else
  echo "Corrupt state, reinitializing..."
  echo '{}' > state.json
fi
```

### Security: Good vs. Bad Memory Store Content

```bash
# ✅ Store aggregate statistics only
echo '{"open_issues": 42}' > metrics.json

# ❌ Never store PII or user-identifiable data
echo '{"user": "alice", "email": "alice@example.com"}' > users.json
```

### API Caching TTLs (Pattern 4 recommendations)

```
Data type              Recommended TTL
─────────────────────  ─────────────────
Repository metadata    24 hours
Contributor lists      12 hours
Issues / PRs           1 hour
Workflow runs          30 minutes
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-agentic-ops.md` Claim 7 (`repo-memory` as cross-workflow shared persistence
    primitive, branch-backed, human-inspectable): MemoryOps is the general documentation
    of what agentic-ops discovered as a specific implementation. Both confirm that
    `repo-memory` branches are the coordination mechanism for multi-workflow state sharing.
  - `docs-ghaw-agentic-ops.md` Claim 6 (the audit+optimizer pipeline shares `memory/token-audit`
    via `repo-memory` with a scheduled offset): MemoryOps Pattern 3 (Shared Information) is
    the named general pattern for exactly this architecture. The agentic-ops note documents one
    instantiation; MemoryOps names and generalizes it.
  - `docs-ghaw-audit-with-agents.md` Claim 5 (`cache-memory: key: audit-monitoring-trends`
    at `/tmp/gh-aw/cache-memory/` for 30-day rolling baselines): MemoryOps Pattern 5
    (Trend Computation) and Pattern 4 (Data Caching) describe the general patterns within
    which that specific usage sits. Both sources confirm the `/tmp/gh-aw/cache-memory/` path
    and the rolling-baseline use case.
  - `docs-ghaw-workqueue-ops.md` Claim 5 (Cache-Memory strategy stores queue state at
    `/tmp/gh-aw/cache-memory/workqueue.json` with todo/done/errors/last_run schema for
    large queues on multi-day horizons): MemoryOps Pattern 1 (Exhaustive Processing) is the
    general pattern; WorkQueueOps Strategy 3 is the specific application to work queues. The
    JSON schemas are the same four-field structure.

- **Contradicts**: None filed. The memory primitive paths, retention values, and usage
  patterns in this guide are consistent with all prior source notes. The `docs-ghaw-agentic-ops.md`
  note compared `cache-memory` (single-workflow, shorter-lived) vs `repo-memory` (cross-workflow,
  permanent); MemoryOps confirms this distinction explicitly. No material opposition to existing
  claims found.

- **Extends**:
  - `docs-ghaw-agentic-ops.md`: That note documents `repo-memory` as a novel primitive
    discovered in the agentic-ops reference implementation. MemoryOps is the authoritative
    general reference — it names both primitives, provides six named patterns, and gives
    the configuration guidance that agentic-ops uses but doesn't explain.
  - `docs-ghaw-audit-with-agents.md`: That note documents `cache-memory` for rolling
    audit baselines (Claim 5). MemoryOps provides the broader design context: Pattern 5
    (Trend Computation) is the named pattern for exactly that use case, and the Best
    Practices section provides the JSON Lines and data rotation guidance that audit-with-agents
    implements implicitly.
  - `docs-ghaw-workqueue-ops.md`: WorkQueueOps covers four queue strategies, one of which
    (Cache-Memory strategy) uses the primitives that MemoryOps documents. MemoryOps is the
    underlying reference; WorkQueueOps is the higher-level pattern that builds on it.

- **Novel**:
  - **Named six-pattern taxonomy for stateful agent workflows** (Claims 4–9): No existing
    source note provides a named taxonomy of memory usage patterns. This is the first corpus
    entry that names Exhaustive Processing, State Persistence, Shared Information, Data
    Caching, Trend Computation, and Multiple Memory Stores as distinct patterns with
    distinct schemas.
  - **Specific API caching TTLs by data type** (Claim 7): The four TTL tiers (24h for
    repo metadata, 12h for contributors, 1h for issues/PRs, 30m for workflow runs) are
    not documented in any other source note. These are the only specific caching-freshness
    recommendations in the corpus for gh-aw workflows.
  - **`/tmp/gh-aw/repo-memory/default/` as the default repo-memory mount path** (Claim 3):
    Prior notes reference `repo-memory` by configuration, not by file-system path. This is
    the first corpus entry that states the default mount path.
  - **Security constraint: aggregate statistics only, never PII or credentials** (Claim 10):
    The explicit prohibition on storing user-identifiable data in memory stores is not
    stated in any existing source note. This is a new data-classification constraint.
  - **Four troubleshooting patterns for memory failures** (Claim 11): The specific failure
    modes (cache key consistency, file-glob matching, OOM, merge conflicts) and their
    remedies are not documented in any existing source note.
  - **Multiple Memory Stores as a named pattern with YAML config for multiple repo-memory
    branches with IDs** (Claim 9): The multi-branch repo-memory config (with `id:` field
    per branch) is not documented in any existing source note. This is the first corpus
    entry showing that multiple `repo-memory` instances can be named and used simultaneously.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add the six-pattern taxonomy as the reference framework for stateful workflow design
    decisions. Engineers choosing between memory approaches should start here: Exhaustive
    Processing for large unordered datasets, State Persistence for sequential cursors,
    Shared Information for multi-workflow coordination, Data Caching for API throttle
    avoidance, Trend Computation for time-series analytics, Multiple Memory Stores for
    complex workflows needing both session and historical state.
  - Add `cache-memory` vs `repo-memory` decision guidance: `cache-memory` for single-workflow
    rolling state with 7-day retention; `repo-memory` when state must outlive 7 days, be
    shared between multiple workflows, or be human-inspectable as a git branch.
  - Add the `/tmp/gh-aw/cache-memory/` and `/tmp/gh-aw/repo-memory/default/` paths as
    the canonical file-system locations for state reads/writes in harness documentation.
  - Add the four API caching TTLs (repo metadata 24h, contributors 12h, issues/PRs 1h,
    workflow runs 30m) as the starter recommendations for Data Caching workflows.
  - Add the multiple repo-memory branch config (using `id:` per branch) as the pattern
    for workflows maintaining separate state namespaces for different data types.

- **Chapter 03 (Safety and Verification)**:
  - Add the security constraint (aggregate statistics only, never PII/credentials) as a
    data classification requirement for any stateful workflow — state written to memory
    must be reviewed before writing.
  - Add the four troubleshooting patterns as a diagnostic checklist for stateful workflow
    failures: cache key drift, file-glob misconfiguration, OOM from full-history loads,
    merge conflicts in shared branches.

- **Chapter 04 (Multi-agent Orchestration)**:
  - Add Pattern 3 (Shared Information via named repo-memory branch) as the asynchronous
    coordination primitive for multi-workflow architectures. Position it alongside the
    synchronous `dispatch-workflow`/`call-workflow` patterns from
    `docs-ghaw-orchestration-patterns.md`: use shared repo-memory when workflows share
    data but not timing; use dispatch/call when workflows need synchronous coordination.

## Extraction Notes

1. **WebFetch processes content through an AI model**: Quotes from the page were confirmed
   by issuing multiple targeted fetch requests for the same passages. Pattern descriptions,
   the opening paragraph, security section, and troubleshooting section were consistently
   returned in the same wording across independent fetches and are cited as direct quotes.
   The TTL values (24h/12h/1h/30m) were consistently returned but appeared in a paraphrase
   of the page rather than in a directly verified verbatim form — treated as emerging
   confidence accordingly. Code blocks (JSON, YAML, bash) were consistently returned
   verbatim.

2. **Source is in the `guides/` section, not `patterns/`**: MemoryOps is a cross-cutting
   reference guide, not a named pattern page. This distinguishes it from the WorkQueueOps
   and Agentic Ops pattern pages — those reference MemoryOps primitives but don't fully
   define them.

3. **No contradictions filed**: Reviewed `docs-ghaw-agentic-ops.md`, `docs-ghaw-audit-with-agents.md`,
   and `docs-ghaw-workqueue-ops.md` against MemoryOps claims. No material oppositions found.
   All sources use the same primitives and are consistent on paths, retention, and use cases.

4. **Pattern 4 TTL values**: The specific TTL values (24h/12h/1h/30m) were consistently
   returned across fetches. They are treated as practitioner recommendations from the guide,
   not formally derived values.
