---
source_url: https://github.github.com/gh-aw/patterns/daily-ops
source_type: docs
title: "GitHub Agentic Workflows: DailyOps Pattern"
author: GitHub Agentic Workflows team (official documentation)
date_published: null
date_extracted: 2026-05-01
last_checked: 2026-05-01
status: current
confidence_overall: emerging
issue: "#323"
---

# GitHub Agentic Workflows: DailyOps Pattern

> The canonical pattern reference for scheduled incremental automation — documents
> the three-phase approach (Research → Configuration → Execution with maintainer
> approval between each phase), weekday-only scheduling convention, discussion-based
> cross-run progress tracking, and `cache-memory` as the persistent state primitive
> for long-horizon agentic workflows.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, "Patterns"
  section, "DailyOps" page; not a blog post or practitioner account)
- **Author credibility**: First-party documentation from the GitHub Agentic Workflows
  team (the same team behind Peli de Halleux / Don Syme's agent factory series).
  This is the authoritative pattern reference for scheduled autonomous improvement
  workflows on the `gh aw` platform. Claims about platform behavior and configuration
  are settled for this platform; design patterns (phased approach, scheduling
  convention) are architectural opinions from practitioners with 183+ production
  workflows.
- **Scope**: Covers the DailyOps scheduling pattern — cron configuration,
  `workflow_dispatch` for manual testing, the three-phase approach, discussion-based
  progress tracking (both `create-discussion` and `add-comment` with existing
  discussion targeting), `cache-memory` for persistent state, and seven named
  reference implementations. Does NOT cover: the full Safe Outputs permission model
  (see `docs-ghaw-how-they-work.md`), cache-memory cleanup lifecycle (see
  `docs-ghaw-ephemerals.md`), or the lifecycle of discussions created by these
  workflows (expiration, `close-older-discussions` — also in `docs-ghaw-ephemerals.md`).

## Extracted Claims

### Claim 1: DailyOps workflows automate incremental progress toward large goals via small, scheduled daily changes that are easy to review and integrate

- **Evidence**: Opening framing from the documentation: "DailyOps workflows automate
  incremental progress toward large goals through small, scheduled daily changes. Work
  happens automatically in manageable pieces that are easy to review and integrate."
  The "compound over time" framing is central — individually small changes accumulate
  into meaningful improvement over days and weeks.
- **Confidence**: anecdotal (architectural framing from GitHub; no measurement of
  compounding effect is provided)
- **Quote**: "DailyOps workflows automate incremental progress toward large goals
  through small, scheduled daily changes. Work happens automatically in manageable
  pieces that are easy to review and integrate."
- **Our assessment**: The "small, reviewable change" model is the same pattern that
  makes the Changeset Generator in `blog-gh-aw-operations-release-workflows.md`
  successful (78% merge rate). The architectural insight is that large goals are
  better decomposed into daily atomic units than pursued in large autonomous bursts.
  For Ch01 (Daily Workflows): the "compound over time" framing is a useful vocabulary
  entry for recommending always-on agentic automation to teams — the pitch is not
  "the agent will fix your code today" but "the agent will make 250 small improvements
  this year that a human would skip."

### Claim 2: The weekday-only cron schedule (`0 2 * * 1-5`) is the standard DailyOps scheduling convention, paired with `workflow_dispatch` for manual testing

- **Evidence**: YAML pattern documented directly on the page:
  ```yaml
  on:
    schedule:
      - cron: "0 2 * * 1-5"  # Weekdays only (no short syntax available)
    workflow_dispatch:
  ```
  The comment explicitly names this as the recommended schedule and notes the absence
  of a short-syntax alternative for weekday-only crons.
- **Confidence**: settled (first-party documentation; the YAML is specific and
  annotated with intent)
- **Quote**: `cron: "0 2 * * 1-5"  # Weekdays only (no short syntax available)`
- **Our assessment**: The weekday-only scheduling convention avoids weekend noise
  accumulation — a workflow that runs on weekends will produce changes that sit
  unreviewed until Monday, defeating the "easy to review and integrate" model.
  The 2 AM UTC time window targets off-peak hours for most US/EU teams. The
  `workflow_dispatch` pair is important for development: it lets practitioners
  trigger the workflow manually without waiting for the cron window, enabling
  iteration before deploying to a live schedule. For Ch02 (Harness Engineering):
  recommend this schedule pattern as the default for DailyOps workflows; the weekday
  constraint prevents unreviewed drift accumulation over weekends.

### Claim 3: The DailyOps phased approach structures work into three stages — Research, Configuration, Execution — with explicit maintainer approval between each

- **Evidence**: The documentation describes three numbered phases: "1. Research —
  Analyze state, create discussion with findings. 2. Configuration — Define steps,
  create config PR. 3. Execution — Make improvements, verify, create draft PRs."
  The phrase "with maintainer approval between each" is explicit — the workflow does
  not progress automatically from phase to phase.
- **Confidence**: emerging (first-party documentation of the design pattern; the
  approval gate mechanism is described but not the specific implementation details
  of how phase transitions are triggered)
- **Quote**: "Work proceeds through three phases with maintainer approval between each:
  1. Research - Analyze state, create discussion with findings; 2. Configuration -
  Define steps, create config PR; 3. Execution - Make improvements, verify, create
  draft PRs"
- **Our assessment**: This phased structure is the most complete human-in-the-loop
  design pattern for multi-step agentic automation in the corpus. Prior sources
  document approval gates at the PR level (`blog-gh-aw-operations-release-workflows.md`
  Claim 6 — 22% rejection rate on Changeset Generator PRs), but this is the first
  source to document approval gates *between* autonomous phases as a structural
  design choice. The Research phase produces a discussion (visible, inspectable);
  the Configuration phase produces a config PR (reviewable); the Execution phase
  produces draft PRs (reviewable before merge). Every consequential artifact is
  a human-reviewable gate. For Ch03 (Safety): this is the canonical pattern for
  "bounded autonomous work with human checkpoints" — the agent never proceeds past
  a phase gate without maintainer sign-off. For Ch09 (Agent Orchestration): the
  three-phase structure is a concrete orchestration model for long-horizon agentic
  tasks.

### Claim 4: GitHub Discussions are the progress-tracking primitive for DailyOps workflows, enabling continuity across scheduled runs

- **Evidence**: The documentation states: "Use GitHub discussions to maintain
  continuity across runs. The workflow creates a discussion (if none exists) and
  adds progress comments on subsequent runs." The `safe-outputs` config for this:
  ```yaml
  safe-outputs:
    create-discussion:
      title-prefix: "${{ github.workflow }}"
      category: "ideas"
  ```
  The discussion creation uses Safe Outputs (the permission-separated write mechanism
  from `docs-ghaw-how-they-work.md`), so the agent can create discussions without
  requiring direct write permissions.
- **Confidence**: settled (first-party documentation; YAML is specific; this aligns
  with the Safe Outputs model in `docs-ghaw-how-they-work.md` Claim 5)
- **Quote**: "Use GitHub discussions to maintain continuity across runs. The workflow
  creates a discussion (if none exists) and adds progress comments on subsequent runs."
- **Our assessment**: Using discussions as cross-run state solves the stateless-agent
  problem without requiring `cache-memory` for human-readable progress. The
  `title-prefix: "${{ github.workflow }}"` pattern allows the workflow to find its
  own discussion on subsequent runs (search by workflow name prefix). The `category:
  "ideas"` designation signals to human repository members that these are
  AI-generated analysis posts, not human-initiated discussions. For Ch02: document
  the `create-discussion` + `title-prefix` pattern as the mechanism for scheduled
  workflow progress tracking. For Ch09: discussions as a shared state layer between
  workflow phases enables the Research phase to write findings that the Configuration
  phase can read — this is a coordination primitive for multi-phase agentic work.

### Claim 5: Existing discussions can be targeted directly for comment posting via `add-comment` with a `target:` discussion number

- **Evidence**: Documentation provides a distinct YAML pattern for posting to an
  existing discussion:
  ```yaml
  safe-outputs:
    add-comment:
      target: "4750"
  ```
  The page notes: "Discussion targeting is automatic when the workflow runs in a
  discussion event context, or when the agent provides an `item_number`." The
  `daily-fact.md` workflow is given as the canonical example — it posts daily facts
  to a pinned discussion thread.
- **Confidence**: settled (first-party documentation; YAML is specific; two
  targeting mechanisms documented: event-context auto-targeting and explicit
  `target:` number)
- **Quote**: "For workflows that post updates to an existing discussion, use
  `add-comment` with a specific target discussion number."
- **Our assessment**: This is a distinct capability from `create-discussion` —
  it allows workflows to maintain a single persistent thread rather than creating
  a new discussion each run. The `daily-fact.md` pattern (pin a discussion once,
  post to it indefinitely) is appropriate for community-facing recurring content.
  The `create-discussion` pattern (create per-run, track by title prefix) is
  appropriate for analytical progress tracking. These two patterns serve different
  use cases: the fixed-thread pattern for community engagement, the per-run
  discussion for iterative analysis. For Ch02: document both `add-comment` targeting
  modes as they enable two distinct scheduling patterns with different human-facing
  experiences.

### Claim 6: `cache-memory: true` in the workflow tools block enables persistent state at `/tmp/gh-aw/cache-memory/` across scheduled runs

- **Evidence**: The frontmatter configuration documented on the page:
  ```yaml
  tools:
    cache-memory: true
  ```
  Description: "Enable `cache-memory` to maintain state at `/tmp/gh-aw/cache-memory/`
  across runs, useful for tracking progress, storing metrics, and building knowledge
  bases over time."
- **Confidence**: settled (first-party documentation; aligns with
  `docs-ghaw-audit-with-agents.md` Claim 5 which uses the same mechanism at the
  same path)
- **Quote**: "Enable `cache-memory` to maintain state at `/tmp/gh-aw/cache-memory/`
  across runs, useful for tracking progress, storing metrics, and building knowledge
  bases over time."
- **Our assessment**: `cache-memory` at `/tmp/gh-aw/cache-memory/` is confirmed as
  the standard platform mechanism for agent state persistence. The DailyOps use
  case (tracking progress, storing metrics, building knowledge bases) is broader
  than the audit use case in `docs-ghaw-audit-with-agents.md` (30-day rolling
  baselines for cost/token metrics). The two sources together establish `cache-memory`
  as a general-purpose cross-run state mechanism. The cleanup lifecycle (keep-latest
  per workflow, delete older) is documented in `docs-ghaw-ephemerals.md` Claim 6.
  For Ch02: `cache-memory: true` is a one-line configuration change that converts
  a stateless scheduled agent into a stateful one — recommend it for any DailyOps
  workflow that accumulates knowledge over time.

### Claim 7: Seven named reference implementations cover distinct DailyOps use cases from coverage to security observability

- **Evidence**: The page lists these canonical workflows:
  - `daily-fact.md` — posts daily facts about the repository to a discussion thread
  - `daily-test-improver.md` — systematically adds tests to improve coverage incrementally
  - `daily-perf-improver.md` — identifies and implements performance optimizations
  - `daily-doc-updater.md` — keeps documentation synchronized with merged code changes
  - `daily-team-status` (from agentics) — creates daily team status reports with activity summaries
  - `daily-repo-chronicle.md` — produces newspaper-style repository updates
  - `daily-security-observability.md` — unified security observability report combining firewall traffic analysis and DIFC integrity-filtered event analysis
  
  The page notes "All follow the phased approach with discussions for tracking and
  draft pull requests for review."
- **Confidence**: settled (first-party documentation; seven named workflows with
  specific descriptions; they exist in the GitHub Next production factory catalogued
  in `docs-ghaw-agent-factory-status.md`)
- **Quote**: "All follow the phased approach with discussions for tracking and draft
  pull requests for review."
- **Our assessment**: These seven workflows are the canonical reference implementations
  for the DailyOps pattern. They span both "informational" DailyOps (daily-fact,
  daily-team-status, daily-repo-chronicle — no PRs, just posts) and "improvement"
  DailyOps (daily-test-improver, daily-perf-improver, daily-doc-updater — produce
  draft PRs for review). The `daily-security-observability.md` workflow is notable
  because it combines firewall traffic analysis with DIFC integrity-filtered event
  analysis — a security-observability use case that extends beyond simple code
  improvement. For Ch09: these seven archetypes define the DailyOps use-case
  taxonomy; harness engineers should choose from these archetypes when designing
  new scheduled improvement workflows.

### Claim 8: DailyOps complements event-driven patterns (IssueOps, ChatOps, LabelOps) by providing scheduled automation that requires no manual trigger

- **Evidence**: The "Related Patterns" section names: "IssueOps — Trigger workflows
  from issue creation or comments; ChatOps — Trigger workflows from slash commands
  in comments; LabelOps — Trigger workflows when labels change on issues or pull
  requests; Planning Workflow — Use `/plan` command to split large discussions into
  actionable work items." DailyOps is positioned as the scheduled counterpart to
  these event-driven patterns.
- **Confidence**: anecdotal (architectural categorization from GitHub; the taxonomy
  is useful but reflects GitHub's design choices, not a universal framework)
- **Quote**: "DailyOps complements these patterns by providing scheduled automation
  that doesn't require manual triggers."
- **Our assessment**: The pattern taxonomy (DailyOps / IssueOps / ChatOps / LabelOps)
  is a complete model for "when does agentic automation fire?" — scheduled, issue-
  triggered, comment-triggered, and label-triggered. DailyOps fills the scheduled
  slot. This is valuable vocabulary for Ch09 (Agent Orchestration): teams designing
  an agent factory can use this taxonomy to map each workflow to a trigger type.
  DailyOps is appropriate when work should happen regardless of human activity in
  the repository (e.g., over weekends, during low-activity periods). For Ch01:
  the "no manual trigger required" property is the key operational difference from
  ChatOps/IssueOps — it removes the activation burden from humans entirely.

## Concrete Artifacts

### DailyOps Schedule Frontmatter

```yaml
# Standard DailyOps scheduling pattern from documentation
on:
  schedule:
    - cron: "0 2 * * 1-5"  # Weekdays only (no short syntax available)
  workflow_dispatch:        # Allow manual testing without waiting for cron
```
*Source: gh-aw DailyOps patterns documentation, "Scheduled Execution" section*

### Three-Phase Approach (from documentation)

```
Phase 1: Research
  → Analyze current state
  → Create discussion with findings
  → Wait for maintainer approval

Phase 2: Configuration
  → Define improvement steps based on Research findings
  → Create config PR for review
  → Wait for maintainer approval

Phase 3: Execution
  → Make improvements per approved config
  → Verify changes
  → Create draft PRs for human review

Each phase gate: explicit maintainer approval before proceeding
```
*Source: gh-aw DailyOps patterns documentation, "Phased Approach" section*

### Progress Tracking via Discussion Creation

```yaml
# Create a new discussion (or find existing by title prefix) for cross-run tracking
safe-outputs:
  create-discussion:
    title-prefix: "${{ github.workflow }}"
    category: "ideas"
```
*Source: gh-aw DailyOps patterns documentation, "Progress Tracking" section*

### Comment Posting to Pinned Discussion Thread

```yaml
# Post to a specific existing discussion (e.g., a pinned thread)
safe-outputs:
  add-comment:
    target: "4750"   # Item number of the pinned discussion
```
*Source: gh-aw DailyOps patterns documentation, "Discussion Comments" section*

### Persistent Memory Configuration

```yaml
# Enable cross-run state at /tmp/gh-aw/cache-memory/
tools:
  cache-memory: true
```
*Source: gh-aw DailyOps patterns documentation, "Persistent Memory" section*

### Reference Implementation Taxonomy

```
Informational DailyOps (posts to discussions, no PRs):
  daily-fact.md           → Daily repository facts to a pinned discussion thread
  daily-team-status       → Daily team activity summaries (from agentics)
  daily-repo-chronicle.md → Newspaper-style repository updates

Improvement DailyOps (creates draft PRs for review):
  daily-test-improver.md  → Incremental test coverage improvement
  daily-perf-improver.md  → Performance optimization identification and implementation
  daily-doc-updater.md    → Documentation synchronization with merged code changes

Observability DailyOps (produces reports):
  daily-security-observability.md → Unified security report: firewall traffic +
                                    DIFC integrity-filtered event analysis

All follow: phased approach + discussions for tracking + draft PRs for review
```
*Source: gh-aw DailyOps patterns documentation, "Common DailyOps Workflows" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 5 (Safe Outputs as permission-separated
    state mutation): the `create-discussion` and `add-comment` safe outputs used
    by DailyOps are direct applications of the base Safe Outputs model. This source
    provides concrete frontmatter patterns for the discussion-creation use case
    that `docs-ghaw-how-they-work.md` describes at the conceptual level.
  - `docs-ghaw-how-they-work.md` Claim 10 (critical actions can require human
    approval): the DailyOps three-phase approach with explicit approval gates between
    each phase is a concrete instantiation of this design principle. This is the
    most complete human-in-the-loop design in the corpus.
  - `docs-ghaw-audit-with-agents.md` Claim 5 (`cache-memory` at
    `/tmp/gh-aw/cache-memory/` for cross-run state): DailyOps uses the same
    `cache-memory` mechanism. The two sources together confirm `cache-memory` as
    the platform's general-purpose cross-run state primitive (not audit-specific).
  - `blog-gh-aw-operations-release-workflows.md` Claim 3 (routine maintenance as
    a viable always-on agentic task, "small, reviewable PR" model): DailyOps
    extends this pattern from a specific workflow (Daily Workflow Updater) to a
    named, structured pattern with phased approval gates. The "small, reviewable
    PR" insight in that note is operationalized by DailyOps's Execution phase.
  - `docs-ghaw-agent-factory-status.md` Claim 1 (183+ production workflows): the
    named DailyOps reference implementations (`daily-test-improver`,
    `daily-perf-improver`, etc.) correspond to workflows visible in the agent
    factory catalog, confirming these are live production patterns, not hypothetical
    examples.

- **Extends**:
  - `docs-ghaw-ephemerals.md`: that note documents `cache-memory` cleanup (Claim 6)
    and the discussion expiration config (Claim 3) — the maintenance layer for
    what DailyOps creates. DailyOps creates discussions and uses cache-memory;
    the Ephemerals page documents how both are managed over time. The two together
    give a complete picture: DailyOps produces persistent artifacts; Ephemerals
    governs their lifecycle.
  - `docs-ghaw-how-they-work.md` Claim 8 ("Continuous AI" as systematic automated
    AI application to software collaboration): the DailyOps pattern is the
    scheduled-automation implementation of "Continuous AI." The four canonical
    use cases named in that note (documentation currency, code quality, triage,
    code review) map directly to DailyOps reference implementations
    (`daily-doc-updater`, `daily-test-improver`).
  - `blog-gh-aw-operations-release-workflows.md`: that post covers the Daily
    Workflow Updater as a specific workflow from a "Meet the Workflows" blog
    perspective; this source documents the DailyOps design pattern that workflow
    exemplifies. The blog post is the practitioner story; this documentation is
    the architectural pattern behind it.

- **Contradicts**: None identified. The phased approach, scheduling convention,
  and `cache-memory` usage are consistent with all existing source notes. No
  existing note makes claims that conflict with these patterns.

- **Novel**:
  - **Three-phase approach (Research → Configuration → Execution) with approval
    gates between each phase** (Claim 3): No existing source documents phased
    progression with explicit maintainer approval between phases as a first-class
    design pattern. Prior sources show approval at the PR level (merge gate);
    this shows approval between autonomous workflow phases — a stronger human-in-
    the-loop model.
  - **Weekday-only scheduling convention with documented rationale** (Claim 2):
    The `0 2 * * 1-5` cron pattern with the explicit "no short syntax available"
    note is not in any existing source note.
  - **`add-comment` with `target:` for pinned discussion posting** (Claim 5):
    The fixed-thread discussion posting pattern (target a specific discussion
    number, post indefinitely) is distinct from `create-discussion` and not
    documented in any existing source note.
  - **Seven named reference implementations with use-case taxonomy** (Claim 7):
    While the agent factory status note lists workflow names, no existing source
    note groups them into the Informational / Improvement / Observability taxonomy
    or documents them as canonical DailyOps archetypes.
  - **"Compound over time" framing for scheduled automation** (Claim 1): The
    "small automated changes that compound over time" vocabulary is not in any
    existing source note. It is the strongest articulation of why scheduled
    incremental automation has value beyond one-shot agents.

## Guide Impact

### Chapter 01: Daily Workflows

- **Add the "compound over time" framing as the core pitch for DailyOps adoption**
  (Claim 1): Teams considering always-on automation need a vocabulary for its
  value. "250 small improvements over a year that a human would skip" is more
  actionable than "the agent will improve your codebase." Pair with the
  weekday-only scheduling convention (Claim 2) as the implementation default.

- **Add the DailyOps use-case taxonomy** (Claim 7): The Informational /
  Improvement / Observability taxonomy gives teams a starting menu for their
  first DailyOps workflows. `daily-test-improver` (incremental coverage) and
  `daily-doc-updater` (documentation currency) are the lowest-risk entry points;
  `daily-security-observability` is the highest-value once the team has built
  confidence in the pattern.

### Chapter 02: Harness Engineering

- **Add weekday-only cron + `workflow_dispatch` as the standard DailyOps harness
  pattern** (Claim 2): The `0 2 * * 1-5` + `workflow_dispatch` combination should
  be the default template for scheduled improvement workflows. Explain why: weekday-
  only prevents unreviewed weekend drift; `workflow_dispatch` enables development
  iteration without waiting for the cron window. This is currently absent from the
  guide's harness patterns.

- **Add `cache-memory: true` as the one-line stateful agent upgrade** (Claim 6):
  A stateless scheduled agent can track no history; with `cache-memory: true` it
  accumulates knowledge across runs. Recommend for any DailyOps workflow that
  benefits from multi-run context (essentially all improvement-type workflows).

- **Add `create-discussion` + `title-prefix` and `add-comment` + `target:` as the
  two discussion-posting patterns** (Claims 4–5): Each serves a different use case —
  per-run analytical tracking vs. persistent community thread. Document both with
  the YAML patterns as concrete harness artifacts.

### Chapter 03: Safety and Verification

- **Add the three-phase approval-gate model as the canonical pattern for multi-step
  autonomous improvement** (Claim 3): This is the most structured human-in-the-loop
  model in the corpus. The design principle: every autonomous phase produces a
  human-reviewable artifact (discussion → config PR → draft PRs) before the next
  phase begins. No consequence is irreversible without human approval. Recommend
  this model for any long-horizon agentic task where individual steps could compound
  errors if allowed to proceed autonomously.

### Chapter 09: Agent Orchestration

- **Add the DailyOps pattern taxonomy** (Claim 8): The four-pattern taxonomy
  (DailyOps / IssueOps / ChatOps / LabelOps) is a complete framework for
  "when does agentic automation fire?" Harness engineers designing an agent factory
  should map each workflow to a trigger type before building. DailyOps fills the
  scheduled slot; the other patterns fill event-driven slots.

- **Add the three-phase structure as a bounded-autonomy orchestration model**
  (Claim 3): For workflows that require multi-step autonomous work over days or
  weeks, the Research → Configuration → Execution structure with approval gates
  is the reference implementation. The key design insight: each phase gate is
  a GitHub artifact (discussion, PR) that doubles as both the approval mechanism
  and the communication artifact — no separate approval workflow needed.

## Extraction Notes

1. **Source rendered full content via Astro/Starlight static HTML**: The page
   content was fully extractable via WebFetch. Raw GitHub markdown sources (`.md`
   and `.mdx`) returned 404, likely because the repository is private. All content
   was extracted from the rendered static HTML.

2. **Phased approach approval gate mechanism not fully specified**: The documentation
   states "maintainer approval between each" phase but does not detail how that
   approval is signaled — whether via PR merge, a specific label, a comment, or
   another mechanism. The pattern is clear architecturally; the implementation
   detail may be in the individual workflow files referenced (not extracted here).

3. **Seven reference workflows listed but not deeply documented**: The page names
   seven canonical DailyOps workflows but does not provide their full YAML specs.
   Deeper extraction of individual workflow files (if accessible) would yield
   concrete harness templates. For now, the use-case descriptions are the extractable
   content.

4. **`daily-security-observability.md` references DIFC**: "DIFC integrity-filtered
   event analysis" appears in the description of `daily-security-observability.md`.
   DIFC (Decentralized Information Flow Control) is a security model; this suggests
   the workflow performs integrity-aware event filtering, not just firewall traffic
   analysis. This is a notable security-observability pattern that may warrant its
   own source note if the full workflow spec is accessible.

5. **No publication date**: The documentation page does not carry an explicit
   publication date. Content is consistent with gh-aw platform behavior as of the
   extraction date (May 2026).

6. **No contradictions filed**: Reviewed all existing source notes, including all
   gh-aw-related notes. No claims in this source materially oppose any existing
   source note. The phased approach, scheduling convention, and discussion-based
   progress tracking are entirely new patterns to the corpus.
