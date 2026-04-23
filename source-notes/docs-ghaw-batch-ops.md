---
source_url: https://github.github.com/gh-aw/patterns/batch-ops
source_type: docs
title: "GitHub Agentic Workflows: BatchOps Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-04-23
last_checked: 2026-04-23
status: current
confidence_overall: emerging
issue: "#320"
---

# GitHub Agentic Workflows: BatchOps Pattern

> The canonical reference for processing large volumes of work items in gh-aw —
> documents four concrete strategies (chunked processing, matrix fan-out,
> rate-limit-aware batching, result aggregation) with full YAML workflow examples,
> a decision table for choosing between BatchOps and sequential processing, a
> dry-run safety convention, and a real-world label migration example across 100+
> issues — filling the gap in the existing gh-aw corpus, which covered the security
> model and observability but nothing on scaling work volume.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, "Design Patterns
  > BatchOps" page; not a blog post or practitioner account — this is the authoritative
  pattern reference for bulk processing in gh-aw)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's agent factory series and the gh-aw platform.
  The YAML schemas, decision table thresholds, and rate-limit behaviors are authoritative
  for this platform. Claims do not automatically generalize to non-gh-aw agentic systems,
  though the shard-assignment formula and retry-count tracking are transferable patterns.
- **Scope**: Bulk/batch work-item processing patterns within gh-aw — decision criteria,
  four concrete strategies with YAML, error handling and partial-failure isolation, and a
  label-migration worked example. Does NOT cover: the sequential queue patterns (those
  are WorkQueueOps), the research-plan-assign lifecycle (TaskOps), the overall security
  architecture (`docs-ghaw-how-they-work.md`), resource lifecycle and ephemeral cleanup
  (`docs-ghaw-ephemerals.md`), or MCP server integration (`docs-ghaw-mcps.md`). This
  page is specifically about parallelizing and scaling discrete work items; WorkQueueOps
  is the companion for order-dependent or dependency-aware sequential processing.

## Extracted Claims

### Claim 1: A concrete five-row decision table maps work-item volume and characteristics to the correct processing strategy

- **Evidence**: The page provides a named decision table "When to Use BatchOps vs
  Sequential Processing" with five rows:
  - `< 50 items, order matters` → Sequential (WorkQueueOps)
  - `50–500 items, order doesn't matter` → BatchOps with chunked processing
  - `> 500 items, high parallelism safe` → BatchOps with matrix fan-out
  - `Items have dependencies on each other` → Sequential (WorkQueueOps)
  - `Items are fully independent` → BatchOps (any strategy)
  - `Strict rate limits or quotas` → Rate-limit-aware batching
- **Confidence**: emerging (first-party documentation; the thresholds are stated
  prescriptively without published performance data behind the specific item counts)
- **Quote**: "< 50 items, order matters → Sequential (WorkQueueOps) / 50–500 items,
  order doesn't matter → BatchOps with chunked processing / > 500 items, high
  parallelism safe → BatchOps with matrix fan-out"
- **Our assessment**: The thresholds (50 and 500) appear to reflect practical experience
  with GitHub API rate limits and Actions billing granularity rather than benchmarked
  breakpoints, but they give practitioners a concrete starting point. The "items have
  dependencies" criterion is the most important selection gate — BatchOps assumes full
  item independence; any dependency between items must route to WorkQueueOps. For Ch02
  (Harness Engineering): this table is guide-facing material that practitioners can use
  directly to choose a processing pattern. The 50/500 thresholds are sensible defaults
  pending project-specific tuning.

### Claim 2: Chunked processing uses `GITHUB_RUN_NUMBER` modulo arithmetic for deterministic, zero-state pagination across scheduled runs

- **Evidence**: The chunked processing YAML shows:
  ```bash
  PAGE_SIZE=25
  PAGE=$(( (GITHUB_RUN_NUMBER % 1000) * PAGE_SIZE ))
  ```
  The page states: "Items must have a stable sort key (creation date, issue number)
  so pagination is deterministic." The formula cycles through pages on successive
  scheduled runs, resetting every 1000 runs (i.e., advancing 25 items per run,
  completing a full pass over 1000 × 25 = 25,000 items before resetting).
- **Confidence**: settled (YAML code example is specific; the stable-sort-key
  requirement is explicitly stated)
- **Quote**: "Items must have a stable sort key (creation date, issue number) so
  pagination is deterministic."
- **Our assessment**: The key insight is that this approach requires no persistent
  queue state — the pagination offset is derived entirely from the run number, making
  it zero-infrastructure. The tradeoff: items added between runs may be processed out
  of order relative to their creation date if the sort key drifts. The PAGE_SIZE=25 is
  a reasonable default for 2 AM scheduled runs that should complete well within the
  20-minute agent timeout. For Ch02: this is the simplest BatchOps entry point —
  no cache-memory required, deterministic behavior, suitable for maintenance workflows
  that run on a fixed schedule.

### Claim 3: Matrix fan-out with `fail-fast: false` enables shard-level partial-failure isolation — one shard's failure doesn't cancel the others

- **Evidence**: The fan-out YAML shows:
  ```yaml
  jobs:
    batch:
      strategy:
        matrix:
          shard: [0, 1, 2, 3]
        fail-fast: false
  ```
  The page states: "Use `fail-fast: false` so one shard failure doesn't cancel the others."
- **Confidence**: settled (first-party documentation; `fail-fast: false` is a standard
  GitHub Actions property — this is a documented behavioral guarantee of the platform)
- **Quote**: "Use fail-fast: false so one shard failure doesn't cancel the others. Each
  shard gets its own token and API rate limit quota."
- **Our assessment**: `fail-fast: false` is the single most important configuration
  property for production batch workflows. The default `fail-fast: true` behavior —
  where one shard failure cancels all other shards — is catastrophic for large batches
  (a transient API error in shard 0 wastes all work done in shards 1–3). The inverse
  (`false`) is almost always correct for independent work items. This pattern is
  transferable beyond gh-aw to any GitHub Actions matrix job processing independent
  items. For Ch02 and Ch09 (Agent Orchestration): make `fail-fast: false` the
  explicit recommended default for any matrix-based agent workflow.

### Claim 4: Each matrix shard gets its own GitHub token and API rate-limit quota, multiplying the effective throughput proportionally

- **Evidence**: The page states explicitly: "Each shard gets its own token and API rate
  limit quota." The shard assignment formula ensures non-overlap: agents process only
  issues where `(issue_number % total_shards) == shard`.
- **Confidence**: settled (first-party documentation; GitHub's per-token rate limit
  behavior is a platform guarantee)
- **Quote**: "Each shard gets its own token and API rate limit quota."
- **Our assessment**: This is the primary performance argument for matrix fan-out
  over chunked processing. With 4 shards, you get effectively 4× the API throughput.
  The non-overlapping shard assignment (`issue_number % total_shards`) guarantees
  exactly one shard processes each item — no double-processing, no missed items.
  The formula is O(1) to compute per item and requires no coordination between shards.
  For Ch09 (Agent Orchestration): the per-token rate-limit multiplication is the
  key concurrency argument for multi-agent patterns. It also sets the ceiling —
  rate limits scale with token count, not infinitely.

### Claim 5: Rate-limit-aware batching combines explicit sleep pauses with HTTP 429 retry logic (60-second backoff, single retry before permanent failure)

- **Evidence**: The rate-limit-aware batching instructions state:
  "On HTTP 429: pause 60 seconds and retry once before marking the item as failed."
  The workflow inputs include `pause_seconds` (default: 30) between sub-batches and
  `batch_size` (default: 10). The safe-outputs caps are `add-comment: max: 100` and
  `add-labels: max: 100`.
- **Confidence**: settled (specific retry behavior documented; the 60-second HTTP 429
  pause and single-retry policy are explicitly stated)
- **Quote**: "On HTTP 429: pause 60 seconds and retry once before marking the item as
  failed."
- **Our assessment**: The explicit retry protocol (60s pause → single retry → mark
  failed) is a production-quality design. The single-retry limit prevents a cascading
  rate-limit situation from blocking the batch indefinitely. The `max:` caps on safe
  outputs are a separate safety mechanism from the sleep pauses — they prevent the
  harness from exceeding safe output volumes independent of API rate limits. For Ch07
  (Cost Management): the explicit `pause_seconds` input and `batch_size` input allow
  operators to tune the throughput-reliability tradeoff per use case. For Ch09: the
  HTTP 429 + 60s + single retry is a specific, transferable retry policy for any
  GitHub API-heavy agent workflow.

### Claim 6: Result aggregation uses cache-memory JSON files with jq to accumulate results across multi-run batches and sub-issues for persistent failures

- **Evidence**: The result aggregation strategy shows:
  ```bash
  RESULTS_DIR="/tmp/gh-aw/cache-memory/batch-results"
  jq -s '{
    total_processed: (map(.processed) | add // 0),
    total_failed: (map(.failed) | add // 0),
    total_skipped: (map(.skipped) | add // 0),
    runs: length,
    errors: (map(.errors // []) | add // [])
  }' "$RESULTS_DIR"/*.json > /tmp/gh-aw/cache-memory/aggregate.json
  ```
  The aggregation instructions include: "For each failed item, create a sub-issue
  so it can be retried."
- **Confidence**: settled (YAML and bash examples are specific; the jq aggregation
  pattern is concrete and executable)
- **Quote**: "For each failed item, create a sub-issue so it can be retried."
- **Our assessment**: The sub-issue-per-failed-item pattern converts transient batch
  failures into persistent, reviewable work items — the failed item doesn't silently
  disappear. This creates a natural audit trail: humans can inspect, retry, or close
  sub-issues. The jq aggregation across JSON result files is a clean pattern for
  multi-run accumulation without a database. For Ch02: the `/tmp/gh-aw/cache-memory/`
  path is the standard cache-memory location for intermediate batch state. Cross-reference
  with `docs-ghaw-ephemerals.md` Claim 6 for the cache-memory cleanup lifecycle
  (memory-{workflow}-{run-id} keys, keep-latest-per-prefix cleanup).

### Claim 7: Error resilience requires tracking `retry_count` per failed item; permanent failure designation occurs after three failures

- **Evidence**: The error handling section states: "When using cache-memory queues,
  track `retry_count` per failed item. Retry items where `retry_count < 3`; after
  three failures move them to `permanently_failed` for human review."
- **Confidence**: emerging (stated as a recommended pattern; the specific threshold
  of 3 is prescriptive guidance without published justification)
- **Quote**: "Retry items where retry_count < 3; after three failures move them to
  permanently_failed for human review."
- **Our assessment**: The three-failure threshold is a reasonable default that prevents
  infinite retry loops while allowing for transient failures (network blips, temporary
  rate limits) to self-resolve. The `permanently_failed` designation as a human-review
  queue is the correct design — rather than silently dropping failed items, they are
  escalated. The pattern is analogous to dead-letter queues in message broker systems.
  For Ch02: recommend explicitly naming the retry state (`retry_count`), the threshold,
  and the permanent-failure destination in any batch workflow spec. This makes the
  failure handling auditable rather than implicit.

### Claim 8: The `dry_run` input pattern with default `true` is the canonical safety mechanism for destructive batch operations

- **Evidence**: The real-world label migration example includes:
  ```yaml
  on:
    workflow_dispatch:
      inputs:
        dry_run:
          description: "Preview changes without applying them"
          default: "true"
  ```
  The instructions state: "If `dry_run` is `true`: report how many issues would be
  updated and add a preview comment. Make no changes."
- **Confidence**: settled (YAML example is specific; the pattern is demonstrated in
  a concrete real-world example, not just described abstractly)
- **Quote**: "If dry_run is true: report how many issues would be updated and add a
  preview comment. Make no changes."
- **Our assessment**: Defaulting `dry_run` to `true` is a production safety practice:
  a manual trigger (workflow_dispatch) cannot accidentally apply changes because the
  operator must explicitly pass `dry_run: false`. This is analogous to `--dry-run`
  flags in CLI tools. The value is especially high for destructive batch operations
  (label removal, comment deletion) where mistakes are hard to reverse at scale.
  For Ch03 (Safety and Verification): recommend the `dry_run: true` default as a
  standard pattern for any gh-aw workflow that modifies repository state in bulk.
  For Ch02: this convention should be present in the harness spec for any
  `workflow_dispatch`-triggered batch operation.

### Claim 9: The `concurrency` group with `cancel-in-progress: false` prevents overlapping batch runs from corrupting shared state

- **Evidence**: The label migration example shows:
  ```yaml
  concurrency:
    group: label-migration
    cancel-in-progress: false
  ```
  This causes a second trigger to wait rather than cancel the in-progress run.
- **Confidence**: settled (first-party; `cancel-in-progress: false` is a standard
  GitHub Actions concurrency behavior)
- **Quote**: (from YAML example: `cancel-in-progress: false`)
- **Our assessment**: `cancel-in-progress: false` (queue rather than cancel) is
  the correct concurrency behavior for batch workflows. The alternative — `true`
  (cancel the running job when a new trigger arrives) — risks orphaning in-progress
  items in a partially-updated state. For a label migration that processes items in
  sub-batches, a cancelled run might leave 30 of 100 issues with new labels and 70
  without, creating an inconsistent state that is hard to diagnose. The wait behavior
  ensures only one instance runs at a time and each run completes fully. For Ch02:
  recommend `cancel-in-progress: false` as the default concurrency policy for any
  stateful batch operation; distinguish from `cancel-in-progress: true` which is
  appropriate only for read-only or idempotent operations.

### Claim 10: The `safe-outputs` `max:` caps are independent rate-limit safety mechanisms separate from the sleep-based throttling

- **Evidence**: The rate-limit-aware batching workflow declares:
  ```yaml
  safe-outputs:
    add-comment: max: 100
    add-labels:
      allowed: [labeled-by-bot]
      max: 100
  ```
  The label migration example uses `add-labels: max: 200` and `remove-labels: max: 200`.
  These caps are configured in the workflow frontmatter, separate from the
  `pause_seconds` runtime parameter.
- **Confidence**: settled (first-party; the `max:` field is a documented Safe Outputs
  configuration property per `docs-ghaw-how-they-work.md`)
- **Quote**: (from YAML: `add-comment: max: 100`)
- **Our assessment**: The `max:` caps and the sleep-based throttling defend against
  different failure modes. The sleep pauses reduce instantaneous API call rate (preventing
  HTTP 429 from the GitHub API). The `max:` caps prevent the agent from issuing more
  safe output operations than the harness designer intended, regardless of what the AI
  decides to do. The two mechanisms are complementary: sleep manages throughput; `max:`
  manages total volume. For Ch03: the `max:` cap is a blast-radius limiter — even if
  the agent logic has a bug that would otherwise affect all 500 issues, the cap
  prevents the damage from exceeding the declared limit.

## Concrete Artifacts

### Decision Table: BatchOps vs Sequential Processing

```
Scenario                                 Recommendation
--------                                 --------------
< 50 items, order matters                Sequential (WorkQueueOps)
50–500 items, order doesn't matter       BatchOps with chunked processing
> 500 items, high parallelism safe       BatchOps with matrix fan-out
Items have dependencies on each other   Sequential (WorkQueueOps)
Items are fully independent              BatchOps (any strategy)
Strict rate limits or quotas             Rate-limit-aware batching
```

*Source: gh-aw BatchOps documentation, "When to Use BatchOps vs Sequential Processing"*

### Strategy 1: Chunked Processing (YAML + bash)

```yaml
---
on:
  schedule:
    - cron: "0 2 * * 1-5"   # Weekdays at 2 AM
  workflow_dispatch:

tools:
  github:
    toolsets: [issues]
  bash:
    - "jq"
    - "date"

safe-outputs:
  add-labels:
    allowed: [stale, needs-triage, archived]
    max: 30
  add-comment:
    max: 30

steps:
  - name: compute-page
    id: compute-page
    run: |
      PAGE_SIZE=25
      # Use run number mod to cycle through pages; reset every 1000 runs
      PAGE=$(( (GITHUB_RUN_NUMBER % 1000) * PAGE_SIZE ))
      echo "page_offset=$PAGE" >> "$GITHUB_OUTPUT"
      echo "page_size=$PAGE_SIZE" >> "$GITHUB_OUTPUT"
---

# Chunked Issue Processor

This run covers offset ${{ steps.compute-page.outputs.page_offset }} with page
size ${{ steps.compute-page.outputs.page_size }}.

1. List issues sorted by creation date (oldest first), skipping the first
   ${{ steps.compute-page.outputs.page_offset }} and taking
   ${{ steps.compute-page.outputs.page_size }}.
2. For each issue: add `stale` if last updated > 90 days ago with no recent
   comments; add `needs-triage` if it has no labels; post a stale warning
   comment if applicable.
3. Summarize: issues labeled, comments posted, any errors.
```

*Source: gh-aw BatchOps documentation, "Batch Strategy 1: Chunked Processing"*

### Strategy 2: Fan-Out with Matrix (YAML)

```yaml
---
on:
  workflow_dispatch:
    inputs:
      total_shards:
        description: "Number of parallel workers"
        default: "4"
        required: false

jobs:
  batch:
    strategy:
      matrix:
        shard: [0, 1, 2, 3]
      fail-fast: false   # Continue other shards even if one fails

tools:
  github:
    toolsets: [issues, pull_requests]

safe-outputs:
  add-labels:
    allowed: [reviewed, duplicate, wontfix]
    max: 50
---

# Matrix Batch Worker — Shard ${{ matrix.shard }} of ${{ inputs.total_shards }}

Process only issues where `(issue_number % ${{ inputs.total_shards }}) ==
${{ matrix.shard }}` — this ensures no two shards process the same issue.

1. List all open issues (up to 500) and keep only those assigned to this shard.
2. For each issue: check for duplicates (similar title/content); add label
   `reviewed`; if a duplicate is found, add `duplicate` and reference the original.
3. Report: issues in this shard, how many labeled, any failures.
```

*Source: gh-aw BatchOps documentation, "Batch Strategy 2: Fan-Out with Matrix"*

### Strategy 3: Rate-Limit-Aware Batching (YAML)

```yaml
---
on:
  workflow_dispatch:
    inputs:
      batch_size:
        description: "Items per sub-batch"
        default: "10"
      pause_seconds:
        description: "Seconds to pause between sub-batches"
        default: "30"

tools:
  github:
    toolsets: [repos, issues]
  bash:
    - "sleep"
    - "jq"

safe-outputs:
  add-comment:
    max: 100
  add-labels:
    allowed: [labeled-by-bot]
    max: 100
---

# Rate-Limited Batch Processor

Process all open issues in sub-batches of ${{ inputs.batch_size }}, pausing
${{ inputs.pause_seconds }} seconds between batches.

1. Fetch all open issue numbers (paginate if needed).
2. For each sub-batch: read each issue body, determine the correct label, add
   the label, then pause before the next sub-batch.
3. On HTTP 429: pause 60 seconds and retry once before marking the item as failed.
4. Report: total processed, failed, skipped.
```

*Source: gh-aw BatchOps documentation, "Batch Strategy 3: Rate-Limit-Aware Batching"*

### Strategy 4: Result Aggregation (YAML + bash)

```yaml
---
on:
  workflow_dispatch:
    inputs:
      report_issue:
        description: "Issue number to aggregate results into"
        required: true

tools:
  cache-memory: true
  github:
    toolsets: [issues, repos]
  bash:
    - "jq"

safe-outputs:
  add-comment:
    max: 1
  update-issue:
    body: true

steps:
  - name: collect-results
    run: |
      RESULTS_DIR="/tmp/gh-aw/cache-memory/batch-results"
      if [ -d "$RESULTS_DIR" ]; then
        jq -s '{
          total_processed: (map(.processed) | add // 0),
          total_failed: (map(.failed) | add // 0),
          total_skipped: (map(.skipped) | add // 0),
          runs: length,
          errors: (map(.errors // []) | add // [])
        }' "$RESULTS_DIR"/*.json > /tmp/gh-aw/cache-memory/aggregate.json
        cat /tmp/gh-aw/cache-memory/aggregate.json
      else
        echo '{"total_processed":0,"total_failed":0,"total_skipped":0,"runs":0,"errors":[]}' \
          > /tmp/gh-aw/cache-memory/aggregate.json
      fi
---

# Batch Result Aggregator

Aggregate results from previous batch runs stored in
`/tmp/gh-aw/cache-memory/batch-results/` into issue #${{ inputs.report_issue }}.

1. Read `/tmp/gh-aw/cache-memory/aggregate.json` for totals and each individual
   result file for per-run breakdowns.
2. Update issue #${{ inputs.report_issue }} body with a Markdown table: summary
   row (processed/failed/skipped) plus per-run breakdown. List errors requiring
   manual intervention.
3. Add a comment: "Batch complete ✓" if no failures, or "Batch complete with
   failures !" with a list of failed items.
4. For each failed item, create a sub-issue so it can be retried.
```

*Source: gh-aw BatchOps documentation, "Batch Strategy 4: Result Aggregation"*

### Error Handling Summary

```
Retry pattern:
  - Track retry_count per failed item in cache-memory queue JSON
  - Retry if retry_count < 3
  - After 3 failures: move to permanently_failed for human review
  - Increment count and save queue after each attempt

Failure isolation:
  - fail-fast: false in matrix jobs (one shard failure ≠ cancel others)
  - Write per-item results BEFORE moving to the next item
  - Store errors with enough context to diagnose and retry
```

*Source: gh-aw BatchOps documentation, "Error Handling and Partial Failures"*

### Real-World Example: Label Migration (dry_run + concurrency)

```yaml
---
on:
  workflow_dispatch:
    inputs:
      dry_run:
        description: "Preview changes without applying them"
        default: "true"

tools:
  github:
    toolsets: [issues]
  bash:
    - "jq"

safe-outputs:
  add-labels:
    allowed: [type:bug]
    max: 200
  remove-labels:
    allowed: [bug]
    max: 200
  add-comment:
    max: 1

concurrency:
  group: label-migration
  cancel-in-progress: false
---

# Label Migration: `bug` → `type:bug`

Migrate all issues with label `bug` to use `type:bug`. List all issues (open
and closed) with label `bug`, paginating to retrieve all of them.

- If `${{ inputs.dry_run }}` is `true`: report how many issues would be updated
  and add a preview comment. Make no changes.
- If `${{ inputs.dry_run }}` is `false`: for each issue add `type:bug` then
  remove `bug`. Process in sub-batches of 20 with 15-second pauses. Track
  successes and failures.

Add a final comment with totals and a search link to verify no `bug` labels remain.
```

*Source: gh-aw BatchOps documentation, "Real-World Example: Updating Labels Across 100+ Issues"*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-ephemerals.md` Claim 6 (cache-memory cleanup strategy, key pattern
    `memory-{workflow}-{run-id}`, keep-latest-per-prefix): this source uses the same
    `/tmp/gh-aw/cache-memory/` path for inter-run state accumulation. Both sources
    agree that cache-memory is the standard mechanism for persistent batch state in
    gh-aw. The Ephemerals note covers the lifecycle (cleanup, GC); this note covers
    the write side (JSON accumulation, aggregation).
  - `docs-ghaw-how-they-work.md` Claim 5 (Safe Outputs as pre-approved operations
    the AI can request without write permissions): BatchOps relies entirely on Safe
    Outputs for all GitHub state mutations — `add-labels`, `remove-labels`,
    `add-comment`, `update-issue`, `create-issue`. The `max:` caps in BatchOps
    workflows are the Safe Outputs configuration that enforces blast-radius limits.
    Both sources are required to understand how write operations work in gh-aw
    batch workflows.
  - `docs-ghaw-how-they-work.md` Claim 10 (critical actions can require human
    approval): the `dry_run: true` default (Claim 8) is a workflow-level instantiation
    of this principle — operators must explicitly opt into applying changes, which
    is a manual approval gate for destructive batch operations.

- **Extends**:
  - `docs-ghaw-ephemerals.md` Claim 6 (cache-memory cleanup): this note adds
    the production write patterns (JSON result files, jq aggregation, per-item
    result accumulation) to the picture the Ephemerals note gives for cleanup.
    Together: Ephemerals covers how cache-memory is cleaned up; this note covers
    how batch workflows write to it.
  - `docs-ghaw-how-they-work.md` (overall architecture): that note covers the
    conceptual model (Safe Outputs, compilation, security pipeline). This note is
    the first in the corpus to show how those primitives are assembled into a
    bulk-processing pattern. It extends the architecture note with a specific
    operational pattern for scaling work volume.
  - `blog-gh-aw-operations-release-workflows.md` (Daily Workflow Updater): that
    blog post mentions routine dependency updates as an always-on task. BatchOps
    provides the concrete pattern for how such updates would scale beyond a single
    sequential pass — chunked processing or matrix fan-out would be appropriate
    depending on repository size.

- **Contradicts**: None identified. No existing source note makes claims that
  contradict the decision table thresholds, the `fail-fast: false` recommendation,
  the retry-count pattern, or the dry-run safety convention. The cache-memory usage
  is consistent with `docs-ghaw-ephemerals.md`; the Safe Outputs usage is consistent
  with `docs-ghaw-how-they-work.md`.

- **Novel**:
  - **Decision table with item-count thresholds** (Claim 1): No other source in the
    corpus provides a decision table for choosing between sequential and parallel
    processing strategies with specific item-count thresholds (50 and 500). This is
    the first guide-facing decision aid for batch strategy selection.
  - **GITHUB_RUN_NUMBER modulo pagination** (Claim 2): The zero-state pagination
    approach — deriving the page offset from the run number without any external
    queue — is not documented in any existing source note. It is a novel pattern
    for maintenance workflows that need to cycle through large item sets without
    infrastructure overhead.
  - **Per-shard rate-limit quota multiplication** (Claim 4): The explicit statement
    that each matrix shard receives its own token and therefore its own rate-limit
    quota is new to the corpus. No existing note makes this throughput argument for
    matrix-based parallel agents.
  - **HTTP 429 retry policy (60s + single retry)** (Claim 5): The specific retry
    protocol is new. Prior notes reference rate-limit awareness (e.g.,
    `docs-ghaw-ephemerals.md` Claim 6 pauses when rate-limited) but do not specify
    the 60-second pause or the single-retry-then-fail policy.
  - **`dry_run: true` as a default-safe input pattern** (Claim 8): No existing source
    names or recommends this convention. The specific default-to-preview design —
    where the operator must actively opt into applying changes — is new to the corpus.
  - **`cancel-in-progress: false` for stateful batch operations** (Claim 9): The
    specific recommendation to use queue-not-cancel concurrency for workflows with
    shared state is new. Prior corpus notes do not distinguish between appropriate
    uses of `cancel-in-progress: true` vs. `false`.
  - **Four-strategy taxonomy with YAML examples** (overall): The existing gh-aw corpus
    has no source that covers bulk work-item processing. This note fills the entire
    gap identified in the triage comments — the security model, resource lifecycle,
    observability, and MCP tooling were covered; how to scale work volume was not.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add BatchOps as a named harness pattern** (Claims 1–4): The guide currently
  lacks a discussion of how to process large volumes of work items. Add the four-strategy
  taxonomy with the decision table as a practitioner reference. Specific recommendations:
  use chunked processing (GITHUB_RUN_NUMBER modulo) for 50–500 item scheduled batches
  with no state infrastructure; use matrix fan-out for >500 items where parallelism is
  safe; use rate-limit-aware batching when quotas are strict.

- **`dry_run: true` as a default-safe convention** (Claim 8): Add to the harness
  engineering section on `workflow_dispatch` inputs: any batch operation that modifies
  repository state should carry a `dry_run` input defaulting to `true`. This makes
  accidental execution impossible — the operator must explicitly pass `false`.

- **`cancel-in-progress: false` for stateful batches** (Claim 9): Add a note
  distinguishing the two concurrency behaviors in the context of batch workflows:
  `cancel-in-progress: true` (cancel + restart, appropriate for read-only or idempotent
  operations) vs. `false` (queue + complete, required for stateful batch operations
  to prevent partial-update states).

- **Safe Outputs `max:` as blast-radius limiter** (Claim 10): Add the `max:` cap
  to the harness engineering section on Safe Outputs. Frame it as a volume ceiling that
  caps total output regardless of agent behavior — a second line of defense after the
  `allowed:` list.

### Chapter 07: Cost Management and Observability

- **Per-shard rate-limit quota as throughput lever** (Claim 4): When practitioners
  need higher API throughput for large batches, matrix fan-out is the gh-aw mechanism
  to achieve it. Each shard gets a separate token and quota. Document as a cost-vs-speed
  tradeoff: more shards = higher throughput but also higher Actions billing.

- **Rate-limit sleep pauses as explicit operational parameter** (Claim 5): The
  `pause_seconds` workflow input is a tunable throughput parameter. Document the tradeoff:
  longer pauses = lower rate-limit error rate but slower batch completion. The 60-second
  HTTP 429 retry pause is a fixed protocol constant, not a tunable parameter.

### Chapter 09: Agent Orchestration Patterns

- **`fail-fast: false` as the default for multi-agent parallel work** (Claim 3): This
  is the single most important configuration property for any parallel agent workflow
  where items are independent. Add it as a named recommendation in Ch09 alongside the
  shard-assignment formula (`item_id % total_shards == shard`) as the standard pattern
  for non-overlapping parallel agent work.

- **Retry-count tracking as a dead-letter-queue pattern** (Claim 7): The `retry_count`
  + `permanently_failed` pattern is a lightweight dead-letter queue for agentic batch
  workflows. Document alongside result aggregation (Claim 6) as the complete failure
  management pattern: track retries, cap at 3, escalate permanently failed items to
  sub-issues for human review.

## Extraction Notes

1. **Full page content retrieved**: The BatchOps page was fetched via `curl -sL` which
   returned the full Astro/Starlight HTML. Python-based HTML stripping extracted all
   text content including the YAML workflow examples. The YAML is verified consistent
   across the raw extraction and the agent-summarized description.

2. **Four related pages followed**: Per MINER.md instructions to follow up to 5 linked
   pages, the following were fetched and reviewed: WorkQueueOps (for cross-reference
   and decision table context), TaskOps (confirms orthogonality — BatchOps and TaskOps
   serve different use cases), and Rate Limiting Controls (confirms the `max:` cap
   behavior and built-in throttling mechanisms). These informed the cross-references
   but were not separately sourced.

3. **No publication date**: The documentation does not carry an explicit publication
   date. `date_published` is left null. Content is consistent with the gh-aw platform
   as of 2026-04-23.

4. **Prospector triage corroboration**: All three Prospector triage comments agreed on
   the four strategies and their key properties. The first comment identified the most
   specific extraction targets (the three strategies, the decision table, and the
   WorkQueueOps comparison). This note extracts all four strategies with full YAML
   plus the dry_run and concurrency patterns that the triage comments flagged as
   particularly extractable.

5. **No contradictions to file**: Reviewed all existing source notes. No claims in this
   source materially oppose existing notes. The cache-memory usage is consistent with
   `docs-ghaw-ephemerals.md`; the Safe Outputs usage is consistent with
   `docs-ghaw-how-they-work.md`. The decision table thresholds (50/500) are novel
   prescriptive guidance without contradicting prior notes (no prior note addresses
   batch size thresholds).
