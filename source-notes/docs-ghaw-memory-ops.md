---
source_url: https://github.github.com/gh-aw/patterns/memory-ops
source_type: docs
title: "GitHub Agentic Workflows: MemoryOps Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-22
last_checked: 2026-05-22
status: current
confidence_overall: emerging
issue: "#855"
---

# GitHub Agentic Workflows: MemoryOps Pattern

> Canonical reference for the gh-aw MemoryOps pattern — documents six concrete
> design patterns for persisting state across workflow runs using Cache Memory
> (ephemeral, 7-day GitHub Actions cache at `/tmp/gh-aw/cache-memory/`) and
> Repo Memory (persistent, version-controlled Git branch at
> `/tmp/gh-aw/repo-memory/default/`), plus specific API caching TTLs, security
> requirements for memory content, and troubleshooting guidance for the four
> most common failure modes.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `patterns/memory-ops` page —
  in the same `patterns/` section as `patterns/orchestration`,
  `patterns/daily-ops`, `patterns/workqueue-ops`, and others. Patterns pages are
  practitioner implementation references, not conceptual overviews or API
  references.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's "Agent Factory" blog series and the `gh aw`
  CLI. YAML configurations, file paths, and memory type properties are
  authoritative for the `gh aw` platform. The six patterns represent established
  designs from production gh-aw deployments; they do not generalize to non-gh-aw
  memory systems without qualification.
- **Scope**: Covers the MemoryOps pattern in full — two memory types with their
  properties and access paths, six named design patterns with their use cases,
  best practices for time-series data storage, security requirements for memory
  content, and troubleshooting for four common failure modes. Does NOT cover:
  the GitHub Actions `cache:` directive for step-extracted data (see
  `docs-ghaw-dataops.md`), the full `cache-memory` cleanup lifecycle (see
  `docs-ghaw-ephemerals.md`), how `cache-memory: true` is configured in workflow
  frontmatter (see `docs-ghaw-dailyops.md`), or the `guides/memoryops` page
  (how-to procedures, distinct from patterns; subject of Issue #438).

## Extracted Claims

### Claim 1: MemoryOps is a named gh-aw pattern for persisting state across workflow runs, built on two storage primitives: Cache Memory (ephemeral) and Repo Memory (persistent)

- **Evidence**: Opening definition from the page, consistently extracted across
  all fetch passes.
- **Confidence**: settled (first-party documentation; formally named and listed in
  the `patterns/` section alongside IssueOps, ChatOps, DataOps, WorkQueueOps)
- **Quote**: "MemoryOps is a set of design patterns using Cache Memory and Repo
  Memory to persist state across workflow runs."
- **Our assessment**: The naming as "MemoryOps" places memory management in the
  same first-class-pattern taxonomy as other gh-aw operational patterns. This is
  not a passive capability — it is a deliberate design pattern that practitioners
  should select when their workflows need state that outlasts a single run. The
  two-storage-type architecture reflects a fundamental design choice: fast
  ephemeral state (cache-memory) for within-session and short-horizon needs vs.
  permanent versioned state (repo-memory) for long-horizon knowledge
  accumulation. For Ch03 (Long-Running Sessions & State): MemoryOps is the
  primary mechanism for state persistence in gh-aw production workflows; document
  it as a first-class architectural pattern.

### Claim 2: Cache Memory provides fast, ephemeral storage using GitHub Actions cache with 7-day retention, accessible at `/tmp/gh-aw/cache-memory/`

- **Evidence**: Two-type memory description from the page, consistent across
  multiple fetch passes. The 7-day retention is GitHub Actions' standard cache
  retention; the path is the gh-aw convention corroborated by
  `docs-ghaw-dailyops.md` Claim 6 and `docs-ghaw-workqueue-ops.md` Claim 5.
- **Confidence**: settled (first-party documentation; the `/tmp/gh-aw/cache-memory/`
  path is confirmed by multiple existing source notes)
- **Quote**: "gives fast, ephemeral storage using GitHub Actions cache (7 days
  retention)"
- **Our assessment**: Cache Memory is the right storage type when: (1) the data
  is useful within the current run or within the next week; (2) the data can be
  regenerated if lost; (3) access speed matters. The 7-day retention is a hard
  constraint — workflows that accumulate knowledge over weeks or months cannot
  rely on cache-memory alone. The `/tmp/gh-aw/cache-memory/` path is the
  standard cross-run state location confirmed across multiple corpus sources.
  Cross-reference with `docs-ghaw-dailyops.md` Claim 6 for `cache-memory: true`
  configuration and `docs-ghaw-workqueue-ops.md` Claim 5 for the queue state
  file structure at this path.

### Claim 3: Repo Memory provides persistent, version-controlled storage in a dedicated Git branch, accessible at `/tmp/gh-aw/repo-memory/default/`

- **Evidence**: Two-type memory description from the page, consistently extracted.
  The specific path `/tmp/gh-aw/repo-memory/default/` appeared consistently
  across multiple fetch passes.
- **Confidence**: settled (first-party documentation)
- **Quote**: "gives persistent, version-controlled storage in a dedicated Git
  branch"
- **Our assessment**: Repo Memory is the right storage type when: (1) data must
  outlast the 7-day GitHub Actions cache retention window; (2) data benefits from
  version history (rollback, audit trail); (3) data needs to be shared across
  workflows. The "dedicated Git branch" design means repo-memory data is part of
  the repository's version history — it is not siloed in a platform-specific
  opaque store. This has implications for auditability (all memory changes are
  commits) and for cross-workflow data sharing (any workflow with repository
  access can read it). For Ch03: document the two-type distinction as the primary
  architectural decision point in MemoryOps — the choice between cache-memory
  (ephemeral, fast) and repo-memory (persistent, versioned) should drive storage
  design for any stateful gh-aw workflow.

### Claim 4: Pattern 1 (Exhaustive Processing) tracks progress through large datasets using todo/done lists, enabling resumption after interruptions or timeouts

- **Evidence**: Pattern 1 description from the page, consistently extracted.
- **Confidence**: settled (first-party documentation; named pattern with specific
  use case)
- **Quote**: "Track progress through large datasets with todo/done lists to ensure
  complete coverage across multiple runs."
- **Our assessment**: The Exhaustive Processing pattern is the gh-aw answer to
  "how do you process a corpus that is too large for a single workflow run?" The
  todo/done list structure — maintained in cache-memory — creates a resumable
  cursor through the dataset. If the workflow times out or fails, the next run
  picks up at the last recorded position rather than restarting from the
  beginning. This is functionally similar to `docs-ghaw-workqueue-ops.md`'s
  Cache-Memory queue strategy (pending/in_progress/completed), but framed as a
  generic dataset processing pattern rather than a work-queue pattern. The key
  design constraint: the dataset must be enumerable in advance. For Ch03: this
  is the foundational pattern for any long-running agent task that processes a
  finite, enumerable corpus.

### Claim 5: Pattern 2 (State Persistence) saves workflow checkpoints to enable long-running tasks to resume across multiple runs

- **Evidence**: Pattern 2 description from the page, consistently extracted.
- **Confidence**: settled (first-party documentation)
- **Quote**: "Save workflow checkpoints to resume long-running tasks that may
  timeout."
- **Our assessment**: State Persistence is the generalized form of the Exhaustive
  Processing pattern — instead of tracking dataset coverage, it tracks arbitrary
  workflow progress (batch number, last processed ID, current phase). This is
  applicable to any long-running agent task that cannot complete in a single run:
  migrations, large-scale refactors, multi-step analysis pipelines. The checkpoint
  pattern maps directly to the WorkQueueOps `workqueue.json` `last_run` field
  (see `docs-ghaw-workqueue-ops.md` Claim 5). The key design constraint:
  checkpointing logic must be built into the workflow from the start; it cannot
  be retrofitted. For Ch03 (Long-Running Sessions): State Persistence is the
  generic resumability pattern; WorkQueueOps is its queue-specialized variant.

### Claim 6: Pattern 3 (Shared Information) enables cross-workflow data sharing via a producer/consumer model where both workflows reference the same repo-memory branch name

- **Evidence**: Pattern 3 description from the page.
- **Confidence**: settled (first-party documentation)
- **Quote**: "Share data between workflows using repo-memory branches. A producer
  workflow stores data; consumers read it using the same branch name."
- **Our assessment**: This is the gh-aw inter-workflow data sharing primitive.
  Repo Memory's Git branch structure enables one workflow to write data that
  another workflow can read without direct API coordination — the branch name is
  the shared key. This means workflows can be loosely coupled (the producer does
  not need to know about consumers) as long as they agree on the branch name. In
  contrast, Cache Memory is not shared across workflows by default because cache
  keys are typically scoped to the workflow run. The producer/consumer pattern
  via repo-memory branches is the gh-aw equivalent of a shared data store
  between microservices. For Ch05 (Orchestration): this is the data-sharing
  primitive for multi-workflow pipelines that do not use the orchestrator/worker
  dispatch model (`dispatch-workflow` / `call-workflow`).

### Claim 7: Pattern 4 (Data Caching) recommends specific TTLs for GitHub API responses: repository metadata (24h), contributors (12h), issues/PRs (1h), workflow runs (30m)

- **Evidence**: Pattern 4 description from the page. The four TTL values were
  extracted consistently across multiple fetch passes in the same numeric form.
- **Confidence**: emerging (first-party documentation; the TTL values are
  recommendations, not platform-enforced limits — their appropriateness depends
  on how quickly each resource type changes in practice)
- **Quote**: "Cache API responses to avoid rate limits and reduce workflow time."
  / "repository metadata (24h), contributor lists (12h), issues/PRs (1h),
  workflow runs (30m)"
- **Our assessment**: The TTL recommendations encode implicit assumptions about
  change frequency: repository metadata (name, description, settings) changes
  rarely; contributor lists change monthly; issues/PRs change frequently
  throughout the day; workflow run states change in real time. The 1h TTL for
  issues/PRs balances freshness against API rate limits — a workflow that checks
  issue state every minute would exhaust its rate limit budget. These four TTL
  values are the most specific operational caching guidance in the corpus: they
  give practitioners concrete starting defaults rather than leaving cache
  duration as an open question. For Ch02 (Harness Engineering): recommend these
  TTL values as defaults for any gh-aw workflow that caches GitHub API responses.

### Claim 8: Pattern 5 (Trend Computation) stores time-series data in JSON Lines format and computes moving averages and statistics over historical records

- **Evidence**: Pattern 5 description from the page; confirmed by the Best
  Practices section recommending JSON Lines for time-series data.
- **Confidence**: settled (first-party documentation; JSON Lines recommendation
  is corroborated by both the pattern description and the Best Practices section)
- **Quote**: "Store time-series data and compute trends, moving averages, and
  statistics."
- **Our assessment**: The Trend Computation pattern is the purpose-built
  application of repo-memory for historical data analysis. JSON Lines (`.jsonl`)
  format is critical: each line is an independent JSON object, so appending a
  new data point is a simple file append (no read-parse-modify-write cycle), and
  partial reads of large files remain valid JSON. The "compute moving averages
  and statistics" goal suggests Python-based analysis steps (consistent with
  the `docs-ghaw-dataops.md` pattern of shell steps for data processing before
  the agent). For Ch07 (State & Memory): Trend Computation is the pattern for
  building knowledge accumulation over time — it is the mechanism behind any
  gh-aw workflow that learns from historical data rather than just the current
  snapshot.

### Claim 9: Pattern 6 (Multiple Memory Stores) recommends separating concerns by using cache-memory for temporary session data and multiple repo-memory branches for metrics, configuration, and archives

- **Evidence**: Pattern 6 description from the page, consistently extracted.
- **Confidence**: settled (first-party documentation)
- **Quote**: "Use multiple memory instances for different lifecycles — cache-memory
  for temporary session data, separate repo-memory branches for metrics,
  configuration, and archives."
- **Our assessment**: Multiple Memory Stores is the architectural organization
  pattern for complex stateful workflows. The separation by lifecycle is the key
  insight: temporary session state (cache-memory, 7-day) has a fundamentally
  different lifecycle than permanent metrics (repo-memory, indefinite). Using a
  single memory store for both mixes concerns and creates data management
  problems (e.g., how do you rotate session state without touching metrics?).
  The "metrics / configuration / archives" taxonomy for repo-memory branches
  suggests three named branch purposes: a metrics branch for time-series trend
  data, a configuration branch for agent settings and policies, and an archive
  branch for historical records. For Ch05 (Orchestration): document this
  separation-of-concerns model as a design best practice for any gh-aw workflow
  with heterogeneous persistence needs.

### Claim 10: JSON Lines format (append-only) is the recommended format for time-series memory data, with data rotation required to prevent unbounded growth

- **Evidence**: Best Practices section of the page, consistently extracted across
  multiple passes.
- **Confidence**: settled (first-party documentation; stated as a named best
  practice; directly connects to merge-conflict troubleshooting in Claim 12)
- **Quote**: "Use append-only JSON Lines format for time-series data. Include
  metadata documenting data structures and retention policies. Implement data
  rotation to prevent unbounded growth."
- **Our assessment**: The JSON Lines recommendation has three distinct rationales:
  (1) append-only writes prevent merge conflicts (adding a line never conflicts
  with another line), directly addressing the merge-conflict troubleshooting
  issue; (2) each record is self-contained, so partial reads and crash recovery
  are safe; (3) tools like `jq` and Python can stream JSON Lines without loading
  the entire file, enabling chunked processing. The data rotation requirement is
  a production operational concern: without rotation, time-series files grow
  indefinitely, eventually causing the memory-error issue documented in
  Troubleshooting (Claim 12). Rotation policy (keep last N records, or records
  from last K days) must be designed into the workflow from the start. For Ch02:
  recommend JSON Lines as the default format for any time-series data in gh-aw
  memory stores; document data rotation as a required design step, not an
  optional optimization.

### Claim 11: Memory stores are visible to anyone with repository access — credentials, API tokens, PII, and secrets must never be stored; only aggregate statistics and anonymized data are appropriate

- **Evidence**: Security Considerations section of the page, consistently
  extracted. The visibility constraint follows from repo-memory being a Git
  branch, and cache-memory having no access controls beyond repository permissions.
- **Confidence**: settled (first-party security requirement; stated as an explicit
  prohibition, not a recommendation)
- **Quote**: "Memory stores are visible to anyone with repository access. Never
  store credentials, API tokens, PII, or secrets — only aggregate statistics and
  anonymized data."
- **Our assessment**: This is the most important security constraint in the
  MemoryOps pattern. The "visible to anyone with repository access" property
  means memory data has the same security boundary as the codebase itself —
  anyone who can read the repository can read all memory data. For open-source
  repositories, this means memory is effectively public. The practical constraint:
  if an agent accumulates knowledge from privileged data (internal API responses,
  user PII, infrastructure details), that knowledge cannot be stored verbatim —
  only derived statistics and anonymized summaries are safe. For Ch03 (Safety
  and Verification): add this as a first-class security constraint for any gh-aw
  stateful workflow. Cross-reference with `docs-ghaw-chatops.md` Claim 7
  ("treat user-provided content as untrusted") — memory content that comes from
  user input must be sanitized before storage.

### Claim 12: Four specific troubleshooting issues address the most common MemoryOps failure modes: inconsistent cache keys, mismatched file-glob patterns, memory errors from large datasets, and merge conflicts

- **Evidence**: Troubleshooting section of the page, consistently extracted.
  The four issues are named with both a symptom and a specific solution per issue.
- **Confidence**: settled (first-party documentation; specific symptom-solution
  pairs, not generic advice)
- **Quote (cache persistence)**: "Verify cache key is consistent across runs" /
  (repo memory): "Check `file-glob` patterns match your files" / (memory errors):
  "Process data in chunks instead of loading entirely" / (merge conflicts):
  "Use JSON Lines format (append-only), separate branches per workflow"
- **Our assessment**: The four troubleshooting entries reveal the four most common
  implementation errors in MemoryOps: (1) **Inconsistent cache keys** — the cache
  misses every run, so state never persists; use a stable key (not run-specific)
  for cross-run persistence. (2) **Mismatched file-glob patterns** — repo-memory
  writes fail because the `file-glob` pattern in the workflow frontmatter doesn't
  match the actual file paths; verify the glob matches the exact paths written.
  (3) **Memory errors from large datasets** — loading large JSON files entirely
  into memory causes OOM errors; process in chunks (streaming JSON Lines parsing).
  (4) **Merge conflicts** — concurrent or sequential writes to the same repo-memory
  branch conflict on JSON file writes; JSON Lines (append-only) avoids conflicts,
  or separate branches per workflow prevent them entirely. The merge conflict
  solution (JSON Lines) directly motivates the Best Practices recommendation
  (Claim 10). For Ch03: document these four failure modes as the standard
  MemoryOps production debugging checklist.

## Concrete Artifacts

### Memory Type Properties (from `patterns/memory-ops`)

```
Cache Memory
  Access path:   /tmp/gh-aw/cache-memory/
  Storage:       GitHub Actions cache
  Retention:     7 days
  Best for:      Temporary state, session data, short-term caching
  Properties:    Fast access; data lost if cache expires or is evicted
  Enable with:   tools: { cache-memory: true }

Repo Memory
  Access path:   /tmp/gh-aw/repo-memory/default/
  Storage:       Dedicated Git branch
  Retention:     Permanent (version-controlled)
  Best for:      Historical data, trend tracking, permanent state
  Properties:    Version history; readable by any workflow with repo access
  Enable with:   tools: { repo-memory: true } (or equivalent config)
```

*Source: `patterns/memory-ops` — "Memory Types" section*

### Six MemoryOps Patterns with Use Cases (from `patterns/memory-ops`)

```
Pattern 1: Exhaustive Processing
  Use case:    Process large datasets that cannot complete in a single run
  Mechanism:   Todo/done lists in cache-memory
  Key feature: Resumable across interrupted runs; no items skipped or doubled

Pattern 2: State Persistence
  Use case:    Resume long-running tasks that may timeout
  Mechanism:   Checkpoint markers (e.g., last_processed_id, batch_number)
  Key feature: Multi-run continuation for tasks exceeding single-run limits

Pattern 3: Shared Information
  Use case:    Share data between producer and consumer workflows
  Mechanism:   Producer writes to repo-memory branch; consumers read same branch
  Key feature: Loose coupling via shared branch name convention

Pattern 4: Data Caching
  Use case:    Cache API responses to avoid rate limits and reduce workflow time
  Mechanism:   Cache-memory with TTL-based refresh
  Recommended TTLs:
    - repository metadata:  24h
    - contributor lists:    12h
    - issues/PRs:           1h
    - workflow runs:        30m

Pattern 5: Trend Computation
  Use case:    Compute moving averages and statistics over historical data
  Mechanism:   Append time-series entries to JSON Lines files in repo-memory
  Key feature: Enables multi-week/month trend analysis and learning over time

Pattern 6: Multiple Memory Stores
  Use case:    Separate concerns by data lifecycle in complex workflows
  Mechanism:   cache-memory for temporary data + multiple repo-memory branches
  Typical branches:
    - metrics/       — time-series measurements
    - configuration/ — agent settings and policies
    - archives/      — historical records aged out of active use
```

*Source: `patterns/memory-ops` — six-pattern section*

### Best Practices (from `patterns/memory-ops`)

```
1. JSON Lines format (append-only)
   Use for all time-series data; prevents merge conflicts (appending a line
   never conflicts with another line); enables streaming access to large files

2. Include metadata
   Document data structures and retention policies in a README or metadata
   file alongside memory data

3. Implement data rotation
   Prevent unbounded growth; define retention window (last N records or last
   K days) at design time — not as an afterthought
```

*Source: `patterns/memory-ops` — "Best Practices" section*

### Troubleshooting Guide (from `patterns/memory-ops`)

```
Issue 1: Cache persistence problems
  Symptom:     State does not persist between workflow runs
  Solution:    "Verify cache key is consistent across runs"
  Root cause:  Cache key includes run-specific values (e.g., run_id);
               each run misses the cache and starts fresh

Issue 2: Repo memory update failures
  Symptom:     Files not written to repo-memory branch
  Solution:    "Check `file-glob` patterns match your files"
  Root cause:  The workflow frontmatter file-glob does not match the actual
               file paths being written by the agent

Issue 3: Memory errors from large datasets
  Symptom:     Workflow fails with OOM or memory-related errors
  Solution:    "Process data in chunks instead of loading entirely"
  Root cause:  Loading a large JSON or JSONL file fully into memory instead
               of streaming / chunking it

Issue 4: Merge conflicts
  Symptom:     Repo-memory branch writes fail with conflict errors
  Solution:    "Use JSON Lines format (append-only), separate branches
               per workflow"
  Root cause:  Multiple concurrent or sequential writes mutate the same JSON
               file (mutating vs. appending)
```

*Source: `patterns/memory-ops` — "Troubleshooting" section*

### Security Constraint (from `patterns/memory-ops`)

```
Memory visibility:  All memory stores are visible to anyone with repository
                    access (public repos = public memory)

Prohibited content: credentials / API tokens / PII / secrets

Permitted content:  aggregate statistics / anonymized data only

Rationale: repo-memory is a Git branch (readable by anyone with repository
           access); cache-memory has no access controls beyond repository
           permissions — neither provides isolation from collaborators.
```

*Source: `patterns/memory-ops` — "Security Considerations" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-dailyops.md` Claim 6 (`cache-memory: true` at
    `/tmp/gh-aw/cache-memory/` for cross-run state persistence): MemoryOps
    confirms the same path and use case. DailyOps documents the
    `cache-memory: true` configuration flag; MemoryOps provides the full design
    pattern taxonomy built on that same storage primitive. Both agree that
    `/tmp/gh-aw/cache-memory/` is the standard cross-run state location for
    agent-generated state.
  - `docs-ghaw-workqueue-ops.md` Claim 5 (Cache-Memory strategy for queue state
    at `/tmp/gh-aw/cache-memory/workqueue.json`): WorkQueueOps' Strategy 3 is
    a specific application of MemoryOps Pattern 2 (State Persistence) — the
    `workqueue.json` with `pending/in_progress/completed/failed/last_run` fields
    is an instance of the checkpoint structure MemoryOps Pattern 2 prescribes.
    Both sources confirm cache-memory as the right store for this use case.
  - `docs-ghaw-chatops.md` Claim 9 (Grumpy Code Reviewer uses cache memory to
    track previous reviews and avoid duplicate feedback): this is MemoryOps
    Pattern 2 (State Persistence) applied to a ChatOps use case — the cache
    stores review history as cross-invocation state. MemoryOps provides the
    formal named pattern that the Grumpy Code Reviewer implicitly follows.
  - `docs-ghaw-dataops.md` Claim 4 (GitHub Actions `cache:` directive for
    step-extracted data): both DataOps (`cache:`) and MemoryOps (`cache-memory:`)
    are caching mechanisms, but for different purposes. DataOps caches
    step-extracted API data (cost of collection: API rate limit); MemoryOps
    caches agent-generated state (cost of regeneration: LLM inference).
    Together they establish the two-cache model for gh-aw workflows.

- **Extends**:
  - `docs-ghaw-dailyops.md`: DailyOps introduces `cache-memory: true` but treats
    it as a configuration option, not a design pattern with named strategies.
    MemoryOps provides the six named patterns and best practices that explain
    *how* to use cache-memory and repo-memory effectively — it is the
    pattern-level documentation above DailyOps' mechanism-level documentation.
  - `docs-ghaw-workqueue-ops.md`: WorkQueueOps covers one specific application
    of cache-memory (queue state management). MemoryOps covers the full design
    pattern space — WorkQueueOps' `workqueue.json` structure is a specialization
    of MemoryOps Pattern 2 (State Persistence) and Pattern 1 (Exhaustive
    Processing) for queue use cases. Teams reading both notes have a complete
    picture of cache-memory use cases.
  - `docs-ghaw-dataops.md`: DataOps establishes the step-extracted-data half of
    the two-cache model (`cache:` for API data). MemoryOps fills in the
    agent-state half (`cache-memory:` and `repo-memory:` for agent-generated
    knowledge). Together they define the complete data persistence landscape for
    gh-aw workflows: deterministic step data (DataOps) + agentic state data
    (MemoryOps).

- **Contradicts**: None identified. MemoryOps is fully consistent with the
  cache-memory and repo-memory references in existing corpus sources. The security
  constraint (Claim 11) extends, rather than contradicts, the general
  "treat user-provided content as untrusted" principle from
  `docs-ghaw-chatops.md` Claim 7 — both apply to different points in the same
  data flow (input sanitization vs. output storage). No contradiction issue
  required.

- **Novel**:
  - **Six-pattern MemoryOps taxonomy** (Claims 4–9): No existing source note
    names or defines the six MemoryOps patterns. Prior notes (DailyOps,
    WorkQueueOps, ChatOps) use cache-memory or repo-memory incidentally for
    their specific use cases; none provides a comprehensive design pattern
    taxonomy.
  - **Repo Memory as a distinct storage type** (Claim 3): No existing corpus
    source documents repo-memory as a named storage type at
    `/tmp/gh-aw/repo-memory/default/`. Prior notes focus exclusively on
    cache-memory. The producer/consumer Shared Information pattern (Claim 6)
    is entirely new to the corpus.
  - **Specific API TTL recommendations** (Claim 7): The four TTL values (24h /
    12h / 1h / 30m) for different GitHub API resource types are the most
    concrete operational caching guidance in the corpus — no prior note provides
    this level of specificity.
  - **JSON Lines as the memory format recommendation with rationale** (Claim 10):
    While DataOps uses JSON and WorkQueueOps uses JSON for queue state, this is
    the first source to explicitly recommend JSON Lines (append-only) as the
    preferred format for time-series data in memory stores, with the rationale
    (merge-conflict prevention, streaming access).
  - **Memory security boundary** (Claim 11): The explicit statement that memory
    stores are visible to anyone with repository access, with the prohibition on
    credentials/PII, is new to the corpus. No prior note documents the security
    boundary of gh-aw memory stores.
  - **Four-issue troubleshooting guide with root causes and solutions** (Claim 12):
    The specific mapping of symptoms to root causes and solutions for the four
    most common MemoryOps failures is entirely new.

## Guide Impact

- **Chapter 03 (Long-Running Sessions & State)**:
  - **Add MemoryOps as the canonical gh-aw state persistence pattern** (Claims
    1–3): The guide should document the Cache Memory / Repo Memory two-type
    architecture as the foundational design decision for any stateful gh-aw
    workflow. The selection rule: time-limited ephemeral state (≤7 days) →
    cache-memory; permanent versioned state → repo-memory.
  - **Add State Persistence pattern as the canonical resumability design**
    (Claim 5): For any long-running task that may timeout, checkpoint markers
    (last processed ID, batch number) in cache-memory are the gh-aw resumability
    primitive. Cross-reference WorkQueueOps (`workqueue.json`) as the
    queue-specialized variant.
  - **Add the four troubleshooting issues as a production debugging checklist**
    (Claim 12): Include the four failure modes (inconsistent cache keys,
    mismatched file-globs, memory errors, merge conflicts) with their solutions.
  - **Add memory security constraint as a first-class safety rule** (Claim 11):
    gh-aw memory stores are visible to anyone with repository access. The
    prohibition on storing credentials, tokens, PII, or secrets is a hard
    security requirement for any stateful gh-aw workflow, especially those
    deployed in open-source repositories.

- **Chapter 05 (Multi-Agent Orchestration)**:
  - **Add Shared Information pattern as the inter-workflow data sharing primitive**
    (Claim 6): When multiple gh-aw workflows need to share data without direct
    API coordination, repo-memory branches are the sharing primitive. The
    producer/consumer model (same branch name = shared data contract) is a
    loosely coupled inter-workflow communication pattern complementary to
    orchestration dispatch (`dispatch-workflow`, `call-workflow`). Document as
    the appropriate choice when workflows need to share data without a formal
    orchestrator/worker relationship.

- **Chapter 07 (State & Memory)**:
  - **Add Trend Computation as the pattern for historical knowledge accumulation**
    (Claim 8): JSON Lines + repo-memory is the design for any workflow that needs
    to compute trends across weeks or months. This enables the "agent that learns
    over time" pattern — workflows that improve their analysis based on accumulated
    historical data rather than just the current snapshot.
  - **Add Multiple Memory Stores as a separation-of-concerns design principle**
    (Claim 9): Different lifecycle data (session state, metrics, configuration,
    archives) should live in separate memory stores. The mixed-lifecycle
    anti-pattern creates data management problems; the separated-lifecycle design
    makes rotation, audit, and access control tractable.

- **Chapter 02 (Harness Engineering)**:
  - **Add API TTL recommendations as concrete defaults for Data Caching pattern**
    (Claim 7): Practitioners designing caching workflows should use the four TTL
    values (repository metadata: 24h, contributors: 12h, issues/PRs: 1h,
    workflow runs: 30m) as starting defaults rather than choosing arbitrary
    values.
  - **Add JSON Lines format + data rotation as mandatory best practices for
    time-series memory** (Claim 10): Any workflow that writes time-series data
    to memory should use append-only JSON Lines (to prevent merge conflicts) and
    implement data rotation (to prevent unbounded growth). These are operational
    requirements, not optional optimizations.

## Extraction Notes

1. **Source page content processed by AI model**: The `WebFetch` tool processes
   page content through an AI model before returning results. Quotes were
   extracted via four independent `WebFetch` calls with different prompt
   framings. Passages that appeared consistently across calls in the same or
   near-identical form are cited as direct quotes. The Assayer should verify
   quoted passages against the live source URL.

2. **YAML configuration examples not fully recovered**: The page likely contains
   YAML workflow configuration examples for each of the six patterns. `WebFetch`
   did not return these code blocks verbatim across any fetch pass — the
   structured text for each pattern was returned, but the YAML was summarized.
   The pattern descriptions, TTL values, and best practices are considered
   well-extracted; concrete YAML artifacts may be incomplete.

3. **No publication date**: Like other gh-aw documentation pages, this page does
   not carry an explicit publication date. `date_published` is left null. Content
   is consistent with gh-aw platform state as of the extraction date (May 2026).

4. **Distinct from `guides/memoryops` (Issue #438)**: The Prospector notes that
   Issue #438 covers the related `guides/memoryops` source. This note covers
   `patterns/memory-ops` — the patterns section documents proven design patterns;
   the guides section documents how-to procedures. These are complementary, not
   duplicates. Cross-referencing the Issue #438 extracted note (if available)
   would strengthen the patterns/guides pairing for the Smith.

5. **Relationship to Anthropic Managed Agents Memory**: The Prospector identified
   `blog-anthropic-claude-managed-agents-memory.md` as an overlapping note.
   These are on different platforms: gh-aw uses GitHub Actions cache + Git
   branches (no access controls beyond repo permissions); Anthropic Managed
   Agents uses a filesystem-based, enterprise-managed memory layer with scoped
   permissions, audit logs, and version rollback. The gh-aw memory model is
   simpler and more accessible; the Managed Agents model provides stronger
   governance. No contradiction — different platforms, different security
   postures.

6. **No contradictions filed**: Reviewed all GHAW-related source notes and the
   broader corpus. No claims in this source materially oppose any existing source
   note at the MINER.md §4a filing threshold. The two-memory-type architecture
   (cache-memory vs. repo-memory) extends and clarifies existing corpus coverage
   without opposing any claim.
