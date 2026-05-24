---
source_url: https://github.github.com/gh-aw/guides/memoryops
source_type: docs
title: "GitHub Agentic Workflows: MemoryOps Guide"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-24
last_checked: 2026-05-24
status: current
confidence_overall: emerging
issue: "#438"
---

# GitHub Agentic Workflows: MemoryOps Guide

> The `guides/memoryops` page (now redirecting to `patterns/memory-ops`) — covering
> two storage primitives (Cache Memory: ephemeral 7-day GitHub Actions cache; Repo
> Memory: persistent version-controlled Git branch), six named design patterns with
> concrete state schemas and YAML configurations, API caching TTL recommendations,
> JSON Lines as the required time-series format, a security constraint against
> storing credentials or PII, and a four-issue troubleshooting guide; substantively
> overlaps `docs-ghaw-memory-ops.md` (issue #855, patterns page) and adds the
> Pattern 1 JSON state schema and Pattern 6 multi-branch `id:`-keyed YAML as
> concrete artifacts.

## Source Context

- **Type**: docs (GitHub Agentic Workflows `guides/` section — now redirecting to
  `patterns/memory-ops`. Guides pages are how-to implementation references; the
  redirect appears to reflect a consolidation of the procedural guide into the
  patterns reference page. Content is authoritative for the `gh aw` platform.)
- **Author credibility**: First-party from the GitHub Next / Microsoft Research team
  behind Peli de Halleux's "Agent Factory" blog series and the `gh aw` CLI. YAML
  configurations, file paths, and state schemas are authoritative for this platform.
  Claims do not automatically generalize to non-gh-aw memory systems.
- **Scope**: Covers the two MemoryOps storage types (cache-memory and repo-memory)
  with properties and access paths; all six named patterns with state schemas and
  use-case examples; best practices for time-series format and data rotation;
  security constraints for memory content; and troubleshooting for the four most
  common failure modes. The page does NOT contain complete per-pattern workflow YAML
  specs (those are referenced to external examples) but DOES provide configuration
  YAML for the storage types and Pattern 6 multi-branch setup. Does not cover:
  `cache-memory: true` frontmatter configuration (see `docs-ghaw-dailyops.md`),
  the workqueue pattern (see `docs-ghaw-workqueue-ops.md`), or the full
  `patterns/memory-ops` treatment (see `docs-ghaw-memory-ops.md`, issue #855).

## Extracted Claims

### Claim 1: MemoryOps enables gh-aw workflows to maintain state across executions using two complementary storage primitives — Cache Memory (ephemeral) and Repo Memory (persistent)

- **Evidence**: Opening definition from the page, confirmed across multiple fetch
  passes.
- **Confidence**: settled (first-party documentation; MemoryOps is a formally named
  gh-aw guide/pattern with a dedicated page)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The two-primitive architecture is the foundational design decision
  for any stateful gh-aw workflow. Cache Memory (7-day retention, GitHub Actions
  cache backend) is the right choice when state can be regenerated if lost and is
  useful within the next week. Repo Memory (permanent, Git branch backend) is the
  right choice when state must outlast the 7-day cache window, benefits from version
  history, or needs to be shared across workflows. The selection rule — ephemeral vs.
  persistent — should be the first architectural decision in any stateful workflow
  design. Cross-reference `docs-ghaw-memory-ops.md` Claim 1 for the canonical patterns-
  page treatment of this same primitive.

### Claim 2: Cache Memory provides ephemeral storage via GitHub Actions cache (7-day retention) accessible at `/tmp/gh-aw/cache-memory/`, suitable for temporary state and session data

- **Evidence**: Storage type definition from the page; the 7-day retention is GitHub
  Actions' standard cache policy; the path is confirmed by multiple corpus sources.
- **Confidence**: settled (first-party documentation; path confirmed across
  `docs-ghaw-dailyops.md`, `docs-ghaw-workqueue-ops.md`, and `docs-ghaw-memory-ops.md`)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Cache Memory is the standard cross-run state mechanism for
  gh-aw workflows that need rolling history, session continuity, or resumption points
  within a 7-day window. The 7-day constraint is a hard limit — workflows that need
  to accumulate knowledge over weeks or months cannot use cache-memory as their
  primary store. The `/tmp/gh-aw/cache-memory/` path is confirmed across at least
  four corpus sources (dailyops, workqueue-ops, audit-with-agents, memory-ops).
  Cross-reference `docs-ghaw-memory-ops.md` Claim 2.

### Claim 3: Repo Memory provides persistent, version-controlled storage in a dedicated Git branch accessible at `/tmp/gh-aw/repo-memory/default/`, suitable for historical data and permanent state

- **Evidence**: Storage type definition from the page, consistent with
  `docs-ghaw-memory-ops.md` Claim 3 and `docs-ghaw-agentic-ops.md` Claim 7.
- **Confidence**: settled (first-party documentation)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Repo Memory is the appropriate store when: (1) data must
  outlast GitHub's 7-day cache retention; (2) data benefits from version history
  (rollback, audit trail of memory changes as commits); (3) data must be shared
  across multiple workflows (see Pattern 3 below). The "dedicated Git branch"
  architecture means memory data is auditable by anyone with repository access —
  a critical implication for the security constraint (Claim 10). Cross-reference
  `docs-ghaw-memory-ops.md` Claim 3.

### Claim 4: Pattern 1 (Exhaustive Processing) tracks progress through large datasets using todo/done lists with a four-field state schema: `todo`, `done`, `errors`, `last_run`

- **Evidence**: Pattern 1 description plus a JSON state example from the page.
  The four-field schema was obtained from a concrete JSON example on the page.
- **Confidence**: settled (first-party documentation; the JSON state example is
  internally consistent with the pattern's resumability goal)
- **Quote**: (no direct quote for the opening description; see JSON artifact below)
- **Our assessment**: Exhaustive Processing is the pattern for processing a
  finite, enumerable dataset that cannot complete in a single run. The four-field
  schema (`todo`: items remaining, `done`: completed items, `errors`: failed items,
  `last_run`: Unix timestamp) is a minimal resumability record — enough to pick up
  where a previous run stopped without reprocessing completed items or losing
  failed-item information. The `errors` field distinguishes this from the
  WorkQueueOps Strategy 3 schema (`pending`, `in_progress`, `completed`, `failed`,
  `last_run`) — five fields with different semantics: WorkQueueOps tracks in-progress
  state separately (supporting concurrent workers) while MemoryOps Pattern 1 is
  designed for single-worker sequential processing with a simple todo/done split.
  These are related but distinct designs for overlapping use cases. For Ch03
  (Long-Running Sessions): this is the canonical pattern for any agent that must
  process a corpus that exceeds a single run's capacity.

### Claim 5: Pattern 2 (State Persistence) saves checkpoint markers (e.g., `last_processed_id`, `batch_number`) to resume long-running tasks across multiple runs

- **Evidence**: Pattern 2 description from the page; the specific field names
  (`last_processed_id`, `batch_number`) appear as examples in the pattern description.
- **Confidence**: settled (first-party documentation)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: State Persistence is the generalized resumability pattern —
  where Pattern 1 tracks an enumerable todo list, Pattern 2 tracks arbitrary workflow
  progress as a position marker. Any long-running agent task that processes in batches
  (database migrations, large-scale refactors, multi-step analysis pipelines) should
  implement Pattern 2. The checkpoint must be written before the run ends; a workflow
  that writes the checkpoint only on success provides no benefit after a timeout.
  Cross-reference `docs-ghaw-workqueue-ops.md` Claim 5 — the `workqueue.json`
  `last_run` field is an instance of Pattern 2's checkpoint concept, applied within
  a queue management context.

### Claim 6: Pattern 3 (Shared Information) enables cross-workflow data sharing via a producer/consumer model where both workflows reference the same repo-memory branch name

- **Evidence**: Pattern 3 description from the page; confirmed by
  `docs-ghaw-agentic-ops.md` Claim 6 (the audit + optimizer pair sharing
  `memory/token-audit` branch).
- **Confidence**: settled (first-party documentation; corroborated by reference
  implementation in `docs-ghaw-agentic-ops.md`)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Shared Information is the gh-aw inter-workflow data sharing
  primitive. The shared branch name is the data contract — producer writes to a
  branch, consumers read from the same branch by name. This enables loose coupling:
  the producer does not need to invoke or notify consumers; they read when they run.
  The two-hour offset in the agentic-ops reference implementation (audit at 12:00,
  optimizer at 14:00) is a practical timing pattern for this coordination model.
  Cross-reference `docs-ghaw-agentic-ops.md` Claim 6 for a production implementation
  of this pattern.

### Claim 7: Pattern 4 (Data Caching) recommends specific TTLs for GitHub API responses: repository metadata (24h), contributor lists (12h), issues/PRs (1h), workflow runs (30m)

- **Evidence**: Pattern 4 description with four specific TTL values, consistent
  across multiple fetch passes.
- **Confidence**: emerging (first-party recommendations; the TTL values encode
  assumptions about change frequency that may not hold for all repositories)
- **Quote**: "repository metadata (24h), contributor lists (12h), issues/PRs (1h),
  workflow runs (30m)"
- **Our assessment**: These four TTL values are the most specific operational caching
  guidance in the corpus for GitHub API responses. The graduated TTLs reflect change
  frequency: repository metadata (name, settings) changes rarely; contributor lists
  change monthly; issues/PRs change throughout the day; workflow run state changes
  in real time. The 1h TTL for issues/PRs is the most consequential for monitoring
  workflows — it balances cache staleness against API rate limit consumption. For
  Ch02 (Harness Engineering): recommend these four TTL values as starting defaults
  for any gh-aw workflow that caches GitHub API responses.

### Claim 8: Pattern 5 (Trend Computation) stores time-series data points in JSON Lines format in repo-memory and computes moving averages and statistical trends over historical records

- **Evidence**: Pattern 5 description from the page; confirmed by the Best Practices
  section (JSON Lines recommendation) on the same page.
- **Confidence**: settled (first-party documentation; JSON Lines recommendation
  appears in both Pattern 5 and the Best Practices section)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Trend Computation is the pattern for building historical
  knowledge accumulation over time. The JSON Lines format is essential: each record
  is an independent JSON object appended as a new line, enabling streaming access
  to large files without parsing the whole file, and preventing merge conflicts
  (appending a line never conflicts with another line). The `docs-ghaw-agentic-ops.md`
  reference implementation uses `.json` files (not JSONL) for `rolling-summary.json`
  and `optimization-log.json` — the MemoryOps Best Practices guidance (JSON Lines
  for time-series) extends beyond what the agentic-ops reference implementation
  demonstrates, making it a gap worth noting for teams adopting the reference
  implementation. For Ch07 (State & Memory): Trend Computation with JSONL repo-memory
  is the gh-aw pattern for workflows that improve analysis based on accumulated
  historical data.

### Claim 9: Pattern 6 (Multiple Memory Stores) separates concerns by lifecycle — cache-memory for temporary session data, and multiple named repo-memory branches (metrics, config, archives) configured with `id:` keys

- **Evidence**: Pattern 6 description from the page; YAML configuration example
  recovered showing multi-branch repo-memory with `id:` keys.
- **Confidence**: settled (first-party documentation; YAML artifact is internally
  consistent and structurally novel)
- **Quote**: (no direct quote for the pattern description; see YAML artifact below)
- **Our assessment**: Multiple Memory Stores is the architectural organization
  pattern for complex stateful workflows with heterogeneous persistence needs.
  The `id:` key in the YAML (e.g., `- id: metrics`, `- id: config`, `- id: archive`)
  allows the workflow to reference each branch symbolically without hardcoding branch
  names in agent prompts. This separation-of-concerns design prevents lifecycle
  pollution: rotating session state (cache-memory, 7 days) does not touch long-term
  metrics (repo-memory, indefinite). For Ch05 (Orchestration): document this as the
  design best practice for workflows that accumulate different categories of knowledge
  with different lifetimes.

### Claim 10: Memory stores are visible to anyone with repository access — credentials, API tokens, PII, and secrets must never be stored; only aggregate statistics and anonymized data are appropriate

- **Evidence**: Security constraint section of the page, confirmed verbatim.
- **Confidence**: settled (first-party security requirement; stated as an explicit
  prohibition, not a recommendation)
- **Quote**: "Memory stores are visible to anyone with repository access. Never
  store credentials, API tokens, PII, or secrets — only aggregate statistics and
  anonymized data."
- **Our assessment**: This is the most important safety constraint in MemoryOps.
  Repo Memory is a Git branch — publicly readable in open-source repositories.
  Cache Memory has no access controls beyond repository permissions. Any agent that
  processes sensitive data (internal API responses, user data, infrastructure
  details) must derive and store only sanitized summaries. For Ch03 (Safety and
  Verification): this is a hard security requirement for any stateful gh-aw workflow
  deployed in open-source repositories. Cross-reference `docs-ghaw-chatops.md`
  Claim 7 ("treat user-provided content as untrusted") — memory content derived
  from user input must be sanitized before storage.

### Claim 11: The four most common MemoryOps failure modes each have specific symptoms and solutions: cache not persisting, repo memory not updating, out-of-memory errors, and merge conflicts

- **Evidence**: Troubleshooting section of the page with four named issues.
- **Confidence**: settled (first-party documentation; each issue is named with
  a specific symptom and remedy)
- **Quote**: (no direct quote for the section headings; see paraphrase below)
- **Our assessment**: The four troubleshooting entries map to four implementation
  errors: (1) **Cache not persisting** — the cache key is not stable across runs
  (includes run-specific values); fix: use a consistent, run-independent key.
  (2) **Repo memory not updating** — the `file-glob` pattern in workflow frontmatter
  does not match the actual file paths being written; fix: verify the glob matches
  the exact paths. (3) **Out of memory errors** — large JSON files loaded entirely
  into memory cause OOM; fix: process in chunks or use streaming JSONL parsing.
  (4) **Merge conflicts** — concurrent or sequential writes to the same JSON file
  in repo-memory conflict; fix: use JSON Lines (append-only) or separate branches
  per workflow. Issues 3 and 4 both motivate the Best Practices recommendation for
  JSON Lines format (Claim 8). For Ch03: document these four as the standard
  MemoryOps production debugging checklist.

## Concrete Artifacts

### Storage Type Configurations (from `guides/memoryops`)

```yaml
# Cache Memory — ephemeral, 7-day retention
tools:
  cache-memory:
    key: my-workflow-state

# Repo Memory — persistent, version-controlled Git branch
tools:
  repo-memory:
    branch-name: memory/my-workflow
    file-glob: ["*.json", "*.jsonl"]
```

### Pattern 1 State Schema (from `guides/memoryops`)

```json
{"todo": [123, 456, 789], "done": [101, 102], "errors": [], "last_run": 1705334400}
```

Four-field schema:
- `todo`: items remaining to process (e.g., issue/PR numbers, record IDs)
- `done`: completed items (for verification and deduplication)
- `errors`: items that failed processing (for retry or investigation)
- `last_run`: Unix timestamp of the last run (for time-based filtering)

Note: **different** from `docs-ghaw-workqueue-ops.md` Claim 5's five-field schema
(`pending`, `in_progress`, `completed`, `failed`, `last_run`) which supports
concurrent workers and in-progress tracking. These are related but distinct schemas.

### Pattern 6 Multi-Branch Repo Memory Configuration (from `guides/memoryops`)

```yaml
# Multiple Memory Stores — separate concerns by data lifecycle
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

The `id:` key allows symbolic reference to each branch in agent prompts without
hardcoding branch names. Three branch purposes:
- `metrics/`: time-series measurements (use JSON Lines; rotate to prevent unbounded growth)
- `config/`: agent settings and policies (relatively static; standard JSON)
- `archive/`: historical records aged out of active use (long-term retention)

### Troubleshooting Summary (from `guides/memoryops`)

```
Issue 1: Cache not persisting
  Symptom:     State does not carry over between workflow runs
  Root cause:  Cache key includes run-specific values; each run misses cache
  Fix:         Use a stable, run-independent key (not run_id or workflow_id)

Issue 2: Repo memory not updating
  Symptom:     Files not written to the repo-memory branch
  Root cause:  file-glob pattern in workflow frontmatter does not match written paths
  Fix:         Verify the glob expression matches the actual file paths exactly

Issue 3: Out of memory errors
  Symptom:     Workflow fails with OOM or memory-related errors
  Root cause:  Large JSON/JSONL files loaded entirely into memory
  Fix:         Process in chunks; use streaming JSON Lines parsing

Issue 4: Merge conflicts
  Symptom:     Repo-memory branch writes fail with conflict errors
  Root cause:  Multiple concurrent or sequential writes mutate the same JSON file
  Fix:         Use JSON Lines (append-only) or separate branches per workflow
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-memory-ops.md` Claims 1–12 (issue #855, `patterns/memory-ops`):
    The guides/memoryops URL now redirects to `patterns/memory-ops`. The patterns
    page note is a more complete extraction of the same content. This guides note
    adds the Pattern 1 JSON state schema (four-field: `todo`/`done`/`errors`/
    `last_run`) and the Pattern 6 multi-branch YAML with `id:` keys as concrete
    artifacts not recovered in the patterns-page extraction.
  - `docs-ghaw-agentic-ops.md` Claim 6 (audit + optimizer sharing the
    `memory/token-audit` repo-memory branch): This is a production implementation
    of Pattern 3 (Shared Information). The producer (audit, runs at 12:00) writes
    data; the consumer (optimizer, runs at 14:00) reads it via the same branch name.
    The two-hour offset is an implicit temporal coordination mechanism consistent
    with the Shared Information pattern's loose-coupling design.
  - `docs-ghaw-audit-with-agents.md` Claim 5 (`cache-memory` for rolling baselines
    at `/tmp/gh-aw/cache-memory/audit-trends.json`, 30-day retention): This is a
    production implementation of Pattern 2 (State Persistence) applied to audit
    monitoring. The weekly digest workflow reads the previous baseline, computes
    new rolling averages, and writes back — matching Pattern 2's checkpoint model.
  - `docs-ghaw-workqueue-ops.md` Claim 5 (Cache-Memory strategy with five-field
    `workqueue.json` schema): WorkQueueOps Strategy 3 addresses a similar use case
    to MemoryOps Pattern 1 (Exhaustive Processing) but with a different schema.
    WorkQueueOps uses `pending`/`in_progress`/`completed`/`failed`/`last_run`
    (five fields, supports concurrent workers and retry tracking); Pattern 1 uses
    `todo`/`done`/`errors`/`last_run` (four fields, designed for single-worker
    sequential processing). These are parallel designs for overlapping use cases —
    related, not identical. Teams choosing between them should prefer Pattern 1 for
    simple sequential processing and WorkQueueOps Strategy 3 when concurrency or
    retry budgets are needed.

- **Extends**:
  - `docs-ghaw-agentic-ops.md`: The agentic-ops note covers one specific two-workflow
    pipeline (audit + optimizer sharing repo-memory). This guides note provides the
    general six-pattern taxonomy — including TTL guidance, security constraints,
    troubleshooting, and multi-branch configuration — that explains WHY and HOW the
    agentic-ops design choices were made (Pattern 3 for shared information, Pattern 5
    for trend computation, Pattern 6 for separate-concern stores).
  - `docs-ghaw-audit-with-agents.md`: That guide documents cache-memory usage for
    rolling audit baselines (Pattern 2, State Persistence). This note provides the
    broader pattern context: cache-memory (not repo-memory) is correct for single-
    workflow rolling state; repo-memory is appropriate when state must outlast 7 days
    or be shared across workflows.

- **Contradicts**:
  - `docs-ghaw-agentic-ops.md` and `docs-ghaw-audit-with-agents.md` vs. Pattern 5
    (Trend Computation — JSON Lines recommended): The MemoryOps guide recommends
    JSON Lines for all time-series data in repo-memory. The agentic-ops reference
    implementation uses standard `.json` files for `rolling-summary.json` and
    `optimization-log.json` (the file-glob accepts `*.jsonl` but the actual artifacts
    are named `.json`). This is not a strict contradiction — both approaches work —
    but the MemoryOps guidance recommends JSONL specifically to prevent merge conflicts
    and enable streaming access, a benefit the agentic-ops `.json` files do not
    realize. Teams following the reference implementation exactly will not have the
    merge-conflict protection that Pattern 5 recommends. **No contradiction issue
    filed** because this is a conditioning variable (JSONL provides additional
    benefits that the reference implementation trades off against simplicity) rather
    than a material opposition.

- **Novel**:
  - **Pattern 1 four-field JSON state schema** (`todo`/`done`/`errors`/`last_run`):
    The explicit JSON state schema for Pattern 1 (Exhaustive Processing) is not
    documented in any other corpus source. It provides a concrete data structure
    for teams implementing resumable dataset processing.
  - **Pattern 6 multi-branch YAML with `id:` keys**: The `- id: metrics` /
    `- id: config` / `- id: archive` list syntax for multi-branch repo-memory
    configuration is not documented in any other corpus source. This syntax enables
    symbolic reference to branches in agent prompts.
  - **Guides-to-patterns redirect**: The `guides/memoryops` URL now redirects to
    `patterns/memory-ops`, indicating a consolidation of the procedural guide into
    the patterns reference. This structural change (guides content merged into
    patterns) is worth noting for corpus maintenance: the two issues (#438 and #855)
    were filed for what were originally separate pages that have since been merged.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - **Add Pattern 6 multi-branch YAML as the canonical config for complex stateful
    workflows** (Claim 9): The `id:`-keyed multi-branch repo-memory configuration
    is the design artifact for separation-of-concerns memory management. Include the
    YAML snippet as a copy-pasteable harness configuration starting point.
  - **Add API TTL recommendations as defaults for GitHub API caching** (Claim 7):
    Repository metadata (24h), contributor lists (12h), issues/PRs (1h), workflow
    runs (30m) — these four values should be the guide's concrete defaults for any
    gh-aw workflow caching API responses.
  - **Add Pattern 1 four-field schema as the data structure for resumable dataset
    processing** (Claim 4): The `todo`/`done`/`errors`/`last_run` JSON schema is the
    design artifact for Exhaustive Processing. Include it alongside the WorkQueueOps
    five-field schema as a simpler alternative for single-worker sequential processing.

- **Chapter 03 (Long-Running Sessions & State)**:
  - **Add the four troubleshooting failure modes as a production debugging checklist**
    (Claim 11): Cache not persisting (unstable key), repo memory not updating
    (mismatched file-glob), OOM errors (large file loaded whole), merge conflicts
    (mutating JSON vs. appending JSONL) — these four are the standard MemoryOps
    failure diagnosis steps.
  - **Add memory security constraint as a first-class safety rule** (Claim 10):
    Memory stores are visible to anyone with repository access. Credentials, tokens,
    PII, and secrets must never be stored — only aggregate statistics and anonymized
    data. This is a hard security requirement for all stateful gh-aw workflows,
    especially in open-source repositories.
  - **Note JSONL vs. .json gap in agentic-ops reference implementation**: The
    agentic-ops reference uses standard `.json` files where MemoryOps Pattern 5
    recommends JSON Lines. Teams adopting the reference implementation should convert
    time-series files to JSONL to gain merge-conflict protection and streaming access.

- **Chapter 07 (State & Memory)**:
  - **Add two-storage-type selection rule**: cache-memory for state useful within
    7 days and recoverable if lost; repo-memory for state that must persist longer,
    benefits from version history, or must be shared across workflows. This selection
    rule is the foundational architectural decision for any stateful gh-aw workflow.

## Extraction Notes

1. **URL redirect**: `https://github.github.com/gh-aw/guides/memoryops` returns
   HTTP 301 → `https://github.github.com/gh-aw/patterns/memory-ops/`. The guides
   and patterns pages for MemoryOps have been consolidated. This note covers the
   redirected content (patterns/memory-ops). The companion patterns-page note
   (`docs-ghaw-memory-ops.md`, issue #855) covers the same source URL; that note
   was extracted before this one (May 22, 2026) and provides a more thorough
   treatment of the content. This note focuses on the concrete YAML artifacts and
   the Pattern 1 JSON state schema that were not fully recovered in the prior
   extraction.

2. **WebFetch returns summaries, not verbatim text**: The `WebFetch` tool processes
   page content through an AI model. Quotes were extracted via multiple independent
   fetch passes. The Pattern 4 TTL values and the Claim 10 security text appeared
   verbatim across multiple passes and are cited as direct quotes. Other claims use
   `(no direct quote; see paraphrase in Our assessment)` where verbatim confirmation
   was not obtained. The Assayer should verify all quoted passages against the live
   source URL.

3. **YAML artifacts**: The cache-memory, repo-memory, and Pattern 6 multi-branch
   configurations were recovered from a targeted WebFetch pass. The Pattern 1 JSON
   state schema (`{"todo": [...], "done": [...], "errors": [], "last_run": ...}`) was
   recovered as a concrete JSON example. These are structurally internally consistent
   and match the pattern descriptions.

4. **Cross-reference corrections**: The prior mining PR (#629, closed 2026-05-24)
   received Assayer REQUEST CHANGES on two cross-reference errors: (a) an incorrect
   claim that MemoryOps Pattern 1 and WorkQueueOps Strategy 3 use "the same four-
   field structure" — they use different field names and counts; (b) an incorrect
   claim that `docs-ghaw-agentic-ops.md` Claim 6 uses JSONL for `rolling-summary.json`
   — it uses standard `.json`. Both errors are corrected in this note (see Claim 4
   and Claim 8, and the Cross-References section).

5. **No contradictions filed**: No claims in this source materially oppose existing
   source notes at the MINER.md §4a filing threshold. The JSONL-vs-.json difference
   with the agentic-ops reference implementation is a conditioning variable (different
   tradeoffs chosen), not a material opposition.
