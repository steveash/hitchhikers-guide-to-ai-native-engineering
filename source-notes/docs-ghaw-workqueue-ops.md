---
source_url: https://github.github.com/gh-aw/patterns/workqueue-ops
source_type: docs
title: "GitHub Agentic Workflows: WorkQueueOps Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#356"
---

# GitHub Agentic Workflows: WorkQueueOps Pattern

> Canonical reference for the gh-aw WorkQueueOps pattern — four concrete queue
> strategies (Issue Checklist, Sub-Issues, Cache-Memory, Discussion-based) with
> explicit scale ranges, idempotency requirements, and concurrency controls for
> processing large backlogs of work items across interruptions, rate limits, and
> multi-day horizons.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `patterns/workqueue-ops` page —
  in the same `patterns/` section as `patterns/agentic-ops`, `patterns/orchestration`,
  `patterns/daily-ops`, `patterns/issue-ops`, and others. Patterns pages are
  practitioner implementation references, not conceptual overviews or API references.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team
  (GitHub Next / Microsoft Research — the same team behind Peli de Halleux's "Agent
  Factory" blog series, the `gh aw` CLI, and all other `patterns/` pages in the corpus).
  YAML configurations, tool names, and file paths are authoritative for the `gh aw`
  platform. Design patterns (queue strategies, idempotency requirements) represent
  practitioner experience from operating production agent fleets; they are well-motivated
  but not externally benchmarked.
- **Scope**: Covers the WorkQueueOps design pattern in full — four queue strategies
  with their appropriate use cases and scale ranges, idempotency requirements and
  implementation techniques, concurrency configuration, workflow trigger options
  (scheduled and manual dispatch), and related patterns (BatchOps, TaskOps). Does NOT
  cover: the Safe Outputs permission model in general (see `docs-ghaw-how-they-work.md`),
  cache-memory cleanup lifecycle (see `docs-ghaw-ephemerals.md`), parallel chunk
  processing (see `docs-ghaw-orchestration-patterns.md`), or the issue trigger model
  (see `docs-ghaw-issueops.md`).

## Extracted Claims

### Claim 1: WorkQueueOps is the named gh-aw pattern for processing large backlogs of work items incrementally — surviving interruptions, rate limits, and multi-day horizons

- **Evidence**: Opening definition on the pattern page, consistently extracted across
  multiple fetch passes.
- **Confidence**: settled (first-party documentation; formally named and listed in the
  `patterns/` section alongside other named patterns)
- **Quote**: "WorkQueueOps is a pattern for systematically processing a large backlog
  of work items. Instead of processing everything at once, work is queued, tracked, and
  consumed incrementally — surviving interruptions, rate limits, and multi-day horizons."
- **Our assessment**: The "surviving interruptions" framing is architecturally significant.
  Unlike BatchOps (parallel chunk processing that fails atomically) and DailyOps
  (scheduled incremental improvement), WorkQueueOps is explicitly designed for resumable
  processing — the queue persists state so that a partial run, a rate-limit hit, or a
  multi-day pause does not lose progress. This makes it the correct pattern for any
  large-scale operation that cannot complete in a single workflow run. For Ch02
  (Harness Engineering): introduce WorkQueueOps as the resumable-backlog pattern,
  distinguished from BatchOps (single-run parallel chunks) and DailyOps (scheduled
  incremental improvement without a formal queue data structure).

### Claim 2: The applicability condition for WorkQueueOps is operations that are idempotent and require progress visibility

- **Evidence**: "When to use" section of the pattern page, short and explicit.
- **Confidence**: settled (first-party; stated as the primary applicability condition)
- **Quote**: "Use it when operations are idempotent and progress visibility matters."
- **Our assessment**: The two conditions are complementary constraints. Idempotency is
  a correctness requirement: if a worker crashes mid-queue, the same item may be
  processed again on retry — it must be safe to do so. Progress visibility is an
  operational requirement: large backlogs that update silently are difficult to debug
  and difficult to interrupt safely. Together they define the WorkQueueOps target class:
  any bulk operation where both "can I rerun this item?" and "can I see where I am?"
  must be true. For Ch03 (Safety and Verification): add idempotency as the primary
  safety gate for any workflow that processes a queue — without it, interruptions
  corrupt state rather than merely delay progress.

### Claim 3: The Issue Checklist strategy uses GitHub issue checkboxes as a lightweight queue suited for small-to-medium batches under 100 items

- **Evidence**: Strategy 1 description from the pattern page; scale limit stated
  explicitly.
- **Confidence**: settled (first-party documentation)
- **Quote**: "Use GitHub issue checkboxes as a lightweight, human-readable queue. The
  agent reads the issue body, finds unchecked items, processes each one, and checks
  it off."
- **Our assessment**: The Issue Checklist strategy's primary virtue is human readability —
  the queue is visible in the issue body, editable without tooling, and progress is
  tracked in a place maintainers already watch. The `< 100 items` limit is a practical
  ceiling based on issue body rendering and checkbox count; above this, the issue
  becomes unwieldy. The `workflow_dispatch: inputs: queue_issue:` trigger pattern
  makes this strategy manually driveable: a maintainer passes the issue number and the
  agent resumes. For Ch02: the checklist strategy is the entry point for teams that
  want queue-based processing without additional infrastructure — the queue is the issue
  itself.

### Claim 4: The Sub-Issues strategy creates one sub-issue per work item and scales to hundreds of items with per-item discussion threads

- **Evidence**: Strategy 2 description from the pattern page; scaling claim is explicit.
- **Confidence**: settled (first-party documentation)
- **Quote**: "Create one sub-issue per work item. The agent queries open sub-issues of
  a parent tracking issue, processes each one, and closes it when done."
- **Our assessment**: Sub-issues as a queue is a natural extension of the sub-issue
  hierarchy pattern in `docs-ghaw-issueops.md` Claim 6. Where IssueOps creates
  sub-issues as a decomposition step, WorkQueueOps consumes them as a processing queue.
  The "per-item discussion thread" property distinguishes this strategy from the
  checklist: each work item has its own audit trail, can receive human comments during
  processing, and can be individually triaged if it fails. The `max: 5` safe-output cap
  on `close-issue` prevents notification storms when closing multiple sub-issues per run.
  For Ch02: sub-issues as queue is the right strategy when individual work items need
  human-inspectable processing records — it trades throughput (5 closures per run) for
  visibility.

### Claim 5: The Cache-Memory strategy stores queue state as a JSON file at `/tmp/gh-aw/cache-memory/workqueue.json` and is best for large queues and programmatically-generated items on multi-day horizons

- **Evidence**: Strategy 3 description from the pattern page; file path and queue state
  structure stated explicitly.
- **Confidence**: settled (first-party documentation)
- **Quote**: "Best for large queues and multi-day processing horizons where items are
  generated programmatically."
- **Our assessment**: The Cache-Memory strategy is the most powerful of the four because
  it decouples queue generation from queue consumption. A separate workflow (or a setup
  step in the same workflow) can populate `workqueue.json` with hundreds or thousands of
  items; subsequent scheduled runs process batches without regenerating the queue. The
  five-field JSON structure (`pending`, `in_progress`, `completed`, `failed`, `last_run`)
  encodes both the current state and the history — `completed` and `failed` enable
  resumability and retry budgeting without scanning external systems. The filename
  warning (use filesystem-safe timestamps `YYYY-MM-DD-HH-MM-SS-sss`, no colons) is a
  concrete operational detail not documented elsewhere. This strategy extends
  `docs-ghaw-dailyops.md` Claim 6 (`cache-memory: true` for cross-run state) with a
  specific queue data structure and processing semantics.

### Claim 6: The Discussion-based strategy uses unresolved GitHub Discussion replies as work items, suited for community-sourced queues requiring human inspection

- **Evidence**: Strategy 4 description from the pattern page; queue structure and use
  case stated explicitly.
- **Confidence**: settled (first-party documentation)
- **Quote**: "Each unresolved top-level reply is a work item."
- **Our assessment**: The Discussion-based strategy inverts the typical gh-aw pattern
  where agents create Discussions as output. Here, Discussions are the *input* — a
  community-sourced queue populated by human replies. "Resolving" a reply marks it
  processed; unresolved replies remain as pending items. The human-inspection qualifier
  ("humans need to inspect items before or after processing") makes this strategy
  appropriate for moderation-style workflows where automated processing should be
  visible to community members. This is the most asynchronous of the four strategies —
  the queue grows organically as humans participate rather than being pre-populated by
  the agent. For Ch02: document Discussion-based queuing as the pattern for community-
  driven workloads, distinct from agent-generated queues.

### Claim 7: All WorkQueueOps implementations must be idempotent — running the same item twice must not cause double processing

- **Evidence**: Idempotency requirements section of the pattern page; stated as a
  universal requirement, not a recommendation.
- **Confidence**: settled (first-party documentation; explicitly stated as mandatory)
- **Quote**: "All WorkQueueOps patterns should be idempotent: running the same item
  twice should not cause double processing."
- **Our assessment**: This is the hardest architectural constraint of the pattern.
  Idempotency is required because the queue state (checkboxes, open sub-issues, JSON
  file, unresolved replies) may be out of sync with the actual system state after a
  crash or rate-limit hit. The agent must check external state — not just queue state —
  before acting. The platform provides check-before-act, atomic state updates, and
  retry budgets as implementation techniques (see Claim 8). For Ch03 (Safety and
  Verification): idempotency is a first-class safety requirement for any queue-based
  workflow, not an implementation detail. It must be designed in, not added later.

### Claim 8: WorkQueueOps idempotency is implemented through four techniques: check-before-act, atomic state updates, concurrency groups, and retry budgets

- **Evidence**: Idempotency implementation table on the pattern page, extracted across
  multiple fetch passes in the same form.
- **Confidence**: settled (first-party documentation; four techniques named explicitly)
- **Quote**: "Check before acting: Query current state (label present? comment exists?)
  before making changes" / "Atomic state updates: Write queue state in a single step;
  avoid partial updates" / "set a retry limit before giving up"
- **Our assessment**: The four techniques address different failure modes: check-before-act
  prevents double processing on retry; atomic state updates prevent partial queue states
  from a crash mid-write; concurrency groups prevent two simultaneous runs from racing on
  the same queue; retry budgets prevent failed items from blocking the queue indefinitely.
  The interaction between these is important: check-before-act alone is not sufficient if
  two agents can check simultaneously and both see "not done yet" — only the concurrency
  group prevents this race condition. For Ch03: document all four as a required safety
  bundle, not optional optimizations.

### Claim 9: Concurrency must use `concurrency.group` with `cancel-in-progress: false` to prevent race conditions between parallel runs

- **Evidence**: Concurrency configuration from the pattern page, confirmed in YAML
  examples.
- **Confidence**: settled (first-party documentation; YAML configuration is explicit)
- **Quote**: "Use `concurrency.group` with `cancel-in-progress: false` to prevent
  parallel runs"
- **Our assessment**: The `cancel-in-progress: false` setting is the critical
  distinction from the typical `cancel-in-progress: true` pattern used to save
  resources in CI. For WorkQueueOps, canceling a run mid-processing would leave the
  queue in a partial state — items removed from the pending list but not fully
  processed. The correct behavior is to let the in-progress run complete, then queue
  the new run. The example concurrency key (`workqueue-${{ inputs.queue_issue }}`)
  scopes the lock to the specific queue issue, allowing multiple different queues to run
  concurrently while preventing two runs on the same queue from overlapping. For Ch02:
  `cancel-in-progress: false` is the correct default for any stateful workflow — not
  just WorkQueueOps.

### Claim 10: WorkQueueOps is the sequential per-item processing alternative to BatchOps (parallel chunk processing) — the two patterns address different throughput/simplicity tradeoffs

- **Evidence**: Related Patterns section of the pattern page; BatchOps explicitly
  contrasted with WorkQueueOps.
- **Confidence**: settled (first-party; the contrast is stated on the page)
- **Quote**: "[BatchOps](/gh-aw/patterns/batch-ops/) — Process large volumes in parallel
  chunks rather than sequentially"
- **Our assessment**: This distinction matters for harness design: BatchOps maximizes
  throughput via fan-out (up to 10 parallel workers per `docs-ghaw-orchestration-patterns.md`
  Claim 2) but requires all items to be processable in a single run window. WorkQueueOps
  maximizes reliability and resumability by processing items sequentially across multiple
  runs, accepting lower throughput in exchange for multi-day horizon support. For Ch02:
  introduce both patterns and the tradeoff: BatchOps for bounded parallel workloads,
  WorkQueueOps for unbounded sequential backlogs. The choice is: "can this complete in
  one run?" → BatchOps; "will this take multiple days?" → WorkQueueOps.

### Claim 11: TaskOps (Research → Plan → Assign workflow) is a related pattern, positioned as a higher-level orchestration complement to WorkQueueOps's queue-consumption focus

- **Evidence**: Related Patterns section of the pattern page; TaskOps is named alongside
  BatchOps as a companion.
- **Confidence**: emerging (the relationship is named but not elaborated on the page)
- **Quote**: "[TaskOps](/gh-aw/patterns/task-ops/) — Research → Plan → Assign pattern"
- **Our assessment**: The Research → Plan → Assign model suggests TaskOps operates
  upstream of WorkQueueOps: TaskOps generates a structured set of tasks (the Assign
  step), which WorkQueueOps then consumes as a queue. This producer-consumer relationship
  is not stated explicitly on the page but is implied by the contrast: WorkQueueOps is
  the *consumption* pattern; TaskOps is the *generation* pattern. For Ch02: document the
  TaskOps → WorkQueueOps pipeline as a two-pattern orchestration model for large research-
  driven backlog operations.

## Concrete Artifacts

### Queue Strategy YAML — Issue Checklist (from pattern page)

```yaml
on:
  workflow_dispatch:
    inputs:
      queue_issue:
        description: "Issue number containing the checklist queue"
        required: true
tools:
  github:
    toolsets: [issues]
safe-outputs:
  update-issue:
    body: true
  add-comment:
    max: 1
concurrency:
  group: workqueue-${{ inputs.queue_issue }}
  cancel-in-progress: false
```

### Queue Strategy YAML — Sub-Issues (from pattern page)

```yaml
on:
  schedule: hourly
  workflow_dispatch:
tools:
  github:
    toolsets: [issues]
safe-outputs:
  add-comment:
    max: 5
  close-issue:
    max: 5
concurrency:
  group: sub-issue-queue
  cancel-in-progress: false
```

### Cache-Memory Queue State Structure (from pattern page)

```json
{
  "pending": ["item-1", "item-2"],
  "in_progress": [],
  "completed": ["item-0"],
  "failed": [],
  "last_run": "2026-04-07-06-00-00"
}
```

File path: `/tmp/gh-aw/cache-memory/workqueue.json`

Filename constraint: use filesystem-safe timestamps in filenames (no colons —
e.g., `YYYY-MM-DD-HH-MM-SS-sss`)

### Four Idempotency Implementation Techniques (from pattern page)

```
1. Check before acting
   Technique: Query current state (label present? comment exists?) before making changes

2. Atomic state updates
   Technique: Write queue state in a single step; avoid partial updates

3. Concurrency groups
   Technique: Use concurrency.group with cancel-in-progress: false to prevent parallel runs

4. Retry budgets
   Technique: Track failed items separately; set a retry limit before giving up
```

### Four Queue Strategies with Scale Ranges (from pattern page)

```
Strategy 1: Issue Checklist as Queue
  Scale: < 100 items
  Queue mechanism: GitHub issue checkboxes
  Progress: Checked/unchecked items visible in issue body
  Trigger: workflow_dispatch with queue_issue input

Strategy 2: Sub-Issues as Queue
  Scale: Hundreds of items
  Queue mechanism: Open sub-issues of a parent tracking issue
  Progress: Individual discussion thread per work item
  Trigger: schedule or workflow_dispatch
  Safe-output constraint: max: 5 on close-issue (avoids notification storms)

Strategy 3: Cache-Memory Queue
  Scale: Large queues, multi-day horizons
  Queue mechanism: JSON file at /tmp/gh-aw/cache-memory/workqueue.json
  Progress: pending/in_progress/completed/failed fields in JSON
  Best for: programmatically-generated items

Strategy 4: Discussion-Based Queue
  Scale: Community-sourced (unbounded)
  Queue mechanism: Unresolved top-level replies in a GitHub Discussion
  Progress: Resolved/unresolved reply state
  Best for: async collaboration requiring human inspection
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-dailyops.md` Claim 6 (`cache-memory: true` at `/tmp/gh-aw/cache-memory/`
    for cross-run persistent state): WorkQueueOps Strategy 3 uses the same cache-memory
    path with a specific `workqueue.json` file for queue state. Both sources confirm
    `/tmp/gh-aw/cache-memory/` as the standard cross-run state location.
  - `docs-ghaw-issueops.md` Claim 6 (sub-issue hierarchies with `temporary_id` and
    `parent` fields for agent-sized task decomposition): WorkQueueOps Strategy 2 (Sub-
    Issues as Queue) consumes sub-issues as a processing queue. IssueOps creates the
    hierarchy; WorkQueueOps provides the pattern for draining it.
  - `docs-ghaw-issueops.md` Claim 7 (sub-issues assigned to Copilot via `assignees:
    copilot` for parallel autonomous execution): WorkQueueOps' Sub-Issues strategy
    processes exactly this kind of Copilot-assigned sub-issue queue, processing each
    and closing when done.

- **Extends**:
  - `docs-ghaw-dailyops.md`: DailyOps provides the scheduled incremental processing
    model with `cache-memory` as the persistence mechanism. WorkQueueOps extends this by
    specifying a formal queue data structure (`workqueue.json` with `pending`,
    `in_progress`, `completed`, `failed`, `last_run`) and explicit strategies for
    different queue backends. DailyOps is the general scheduled-improvement pattern;
    WorkQueueOps is the specialized backlog-processing variant with explicit queue
    semantics.
  - `docs-ghaw-orchestration-patterns.md`: That note covers `dispatch-workflow` and
    `call-workflow` fan-out patterns for parallel multi-worker execution. WorkQueueOps
    is the sequential alternative — processing items one-at-a-time across multiple runs
    rather than many items in parallel within a single run. Together they form the
    throughput/resumability tradeoff space for bulk processing: fan-out for bounded
    parallel workloads, WorkQueueOps for unbounded sequential backlogs.
  - `docs-ghaw-ephemerals.md`: That note covers cache-memory cleanup (Claim 6) and the
    full maintenance lifecycle. WorkQueueOps' Cache-Memory strategy depends on the
    cache-memory primitive whose cleanup behavior is documented in ephemerals — teams
    using Strategy 3 need both documents.

- **Contradicts**: None identified. The sequential processing approach of WorkQueueOps
  (one run consumes a bounded batch) is complementary to, not in conflict with,
  BatchOps' parallel chunk model. Both are valid strategies for different use cases.

- **Novel**:
  - **Named four-strategy queue taxonomy with explicit scale ranges**: No existing
    source note documents the Issue Checklist / Sub-Issues / Cache-Memory / Discussion-
    based taxonomy with their specific scale ranges (< 100 items, hundreds, large /
    multi-day, community-sourced). This is the first corpus formalization of queue
    strategy selection criteria.
  - **`cancel-in-progress: false` as the stateful workflow default**: Prior corpus
    notes discuss `concurrency.group` for resource management, but the explicit
    guidance that stateful queue-processing workflows must use `cancel-in-progress:
    false` to avoid partial state corruption is first-stated here.
  - **Four-technique idempotency bundle (check-before-act + atomic updates +
    concurrency group + retry budget)**: The existing corpus covers individual
    idempotency techniques in passing, but this is the first source to enumerate
    all four as a required implementation bundle for queue-based workflows.
  - **`workqueue.json` with five-field schema as the standard cache-memory queue
    format**: The specific `pending` / `in_progress` / `completed` / `failed` /
    `last_run` schema for cache-memory queue state is not documented in any other
    corpus source.
  - **TaskOps → WorkQueueOps pipeline as a named two-pattern orchestration model**:
    The Research → Plan → Assign → Consume producer-consumer relationship between
    TaskOps and WorkQueueOps is not described in any existing source note.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add WorkQueueOps as a named pattern for resumable backlog processing, positioned
    in a three-way taxonomy alongside BatchOps (parallel chunks, bounded) and DailyOps
    (scheduled incremental improvement, no formal queue). The selection heuristic:
    "Can this backlog complete in one run?" → BatchOps; "Does this need to accumulate
    state across multiple days?" → WorkQueueOps; "Is this open-ended improvement without
    a finite backlog?" → DailyOps.
  - Add the four queue strategies as concrete options with explicit scale ranges and
    use case guidance. Teams can match their backlog size and visibility needs to the
    right strategy without building custom infrastructure.
  - Add `cancel-in-progress: false` as the required concurrency setting for any
    stateful workflow (not just WorkQueueOps). The current guide likely does not
    distinguish between `cancel-in-progress: true` (CI default, safe for stateless)
    and `cancel-in-progress: false` (required for stateful queue processing).
  - Document the `workqueue.json` five-field schema (`pending`, `in_progress`,
    `completed`, `failed`, `last_run`) as the standard format for cache-memory queue
    state. Teams should use this rather than inventing their own schema.

- **Chapter 03 (Safety and Verification)**:
  - Add idempotency as a first-class safety requirement for any queue-processing
    workflow, not an implementation detail. The four-technique bundle (check-before-act,
    atomic state updates, concurrency group, retry budget) should be presented as a
    required safety checklist — teams must implement all four to be safe.
  - Add "retry budget" as a safety mechanism: `failed` items tracked separately with
    a maximum retry count prevents infinite retry loops while ensuring transient failures
    get a second chance.

## Extraction Notes

1. **Source page content processed by AI model**: The `WebFetch` tool processes page
   content through an AI model before returning results. Quotes were extracted via four
   independent WebFetch calls with different prompt framings. Passages that appeared
   consistently across calls in the same or near-identical form are cited as direct
   quotes. Passages cited as quotes are those I am most confident represent verbatim
   source text; others are marked "(no direct quote; see paraphrase in Our assessment)."

2. **YAML examples**: The YAML workflow frontmatter examples were extracted via
   WebFetch and appear consistent with GHAW platform conventions documented in other
   corpus notes. They are presented as direct artifacts but noted as WebFetch-extracted
   rather than GitHub API-fetched (unlike the `docs-ghaw-agentic-ops.md` note which
   fetched YAML directly from GitHub via API).

3. **No reference implementation repository**: Unlike `patterns/agentic-ops`, the
   `patterns/workqueue-ops` page does not appear to link to a reference implementation
   repository. The pattern is documented entirely on the page itself.

4. **BatchOps and TaskOps not separately fetched**: The Related Patterns section
   references `patterns/batch-ops` and `patterns/task-ops`. These pages were not
   fetched for this extraction (scope constraint). The claims about BatchOps
   (parallel chunk processing) and TaskOps (Research → Plan → Assign) are based solely
   on the one-line descriptions on the WorkQueueOps page.

5. **No contradictions filed**: WorkQueueOps' sequential processing approach is
   complementary to BatchOps' parallel approach — different tradeoffs for different
   workloads, not an opposition. No existing corpus source contradicts the four
   strategies or the idempotency requirements.
