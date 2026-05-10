---
source_url: https://github.github.com/gh-aw/guides/deterministic-agentic-patterns
source_type: docs
title: "GitHub Agentic Workflows: Deterministic & Agentic Patterns"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#434"
---

# GitHub Agentic Workflows: Deterministic & Agentic Patterns

> The canonical GHAW guide for combining deterministic CI/CD computation with
> AI agent reasoning — covers three named hybrid architectures (precomputation,
> multi-job pre/post processing, inline trigger filtering), four trigger-filtering
> approaches with decision guidance, and the `/tmp/gh-aw/agent/` data-exchange
> directory as the mechanism for passing preprocessed data to the AI agent job.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows guide page — in the `guides/`
  section alongside Agentic Authoring; practitioner how-to for building hybrid
  deterministic+agentic pipelines, not API reference or conceptual overview)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team that operates Peli de Halleux's agent factory and authors all
  `github.github.com/gh-aw` documentation. Claims about workflow patterns,
  configuration syntax, and the data exchange mechanism are authoritative for the
  `gh aw` platform. The decision guidance (which pattern to use when) is
  practitioner opinion from a team running 183+ production workflows; it does not
  automatically generalize beyond `gh aw`.
- **Scope**: Covers the pattern space for combining deterministic jobs with AI
  agent jobs — use cases, three named architectures, the `/tmp/gh-aw/agent/`
  data directory, four trigger-filtering approaches, post-processing via custom
  safe-outputs, and shared imports. Does NOT cover: the core compilation model
  (see `docs-ghaw-compilation-process.md`), the Safe Outputs permission model
  in depth (see `docs-ghaw-how-they-work.md`), orchestrator/worker fan-out at
  scale (see `docs-ghaw-orchestration-patterns.md`), or the pre-activation job
  internals beyond what filtering requires.

## Extracted Claims

### Claim 1: The three-stage hybrid pipeline (deterministic jobs → agent job → safe output jobs) is the named GHAW architecture for combining deterministic computation with AI reasoning

- **Evidence**: The page opens by describing this architecture as the model for
  combining deterministic and agentic steps: deterministic jobs perform data
  fetching and preprocessing, an agent job applies AI reasoning and decisions, and
  safe output jobs execute GitHub API calls after the agent has produced its output.
  The three-stage framing structures the entire guide page.
- **Confidence**: settled (first-party; this is the canonical reference for the
  pattern)
- **Quote**: "GitHub Agentic Workflows combine deterministic computation with AI
  reasoning, enabling data preprocessing, custom trigger filtering, and
  post-processing patterns."
- **Our assessment**: The three-stage model names what happens at each boundary:
  deterministic jobs are responsible for everything the AI should not have to
  compute itself (data fetching, compilation, search); the agent job is responsible
  for reasoning over that pre-gathered data; safe output jobs are responsible for
  writing results to GitHub APIs with appropriate permissions. This maps to the
  `docs-ghaw-how-they-work.md` Claim 2 framing ("combine deterministic GitHub
  Actions infrastructure with AI-driven decision-making") at the pattern level.
  For Ch03 (Orchestration & Workflows): this three-stage model should be named
  as the foundational pattern for hybrid pipeline design, positioned between
  purely deterministic Actions workflows and fully agentic runs.

### Claim 2: The applicable use cases for deterministic-agentic hybrids are five named scenarios: precomputing slow data, filtering triggers, preprocessing inputs, post-processing outputs, and building multi-stage reasoning pipelines

- **Evidence**: The "When to Use" section provides an explicit five-item taxonomy
  of when to reach for this pattern. Examples given include: a release-highlights
  workflow that fetches git logs and PR data before the agent summarizes them; a
  static-analysis workflow that compiles analysis results before the agent interprets
  them; a code-review workflow that uses safe-outputs jobs to format and post the
  agent's review.
- **Confidence**: settled (first-party; the five-item list is explicitly stated)
- **Quote**: "Combine deterministic steps with AI agents to precompute data, filter
  triggers, preprocess inputs, post-process outputs, or build multi-stage
  computation and reasoning pipelines."
- **Our assessment**: The five use cases map to distinct performance and correctness
  concerns. "Precompute data" addresses rate limits and latency (data that takes
  too long or too many API calls to gather during agent reasoning). "Filter triggers"
  addresses cost (don't run the agent when the event doesn't warrant it). "Preprocess
  inputs" addresses context quality (the agent gets structured, relevant data rather
  than raw API responses). "Post-process outputs" addresses format and delivery
  (the agent produces structured output; a deterministic job formats it for humans).
  "Multi-stage pipelines" addresses complex reasoning chains where intermediate
  computation informs later AI reasoning. For Ch05 (Agent Patterns): name these
  five as the canonical criteria for deciding when to add deterministic steps to
  an agentic workflow.

### Claim 3: `/tmp/gh-aw/agent/` is the designated data-exchange directory between deterministic pre-processing jobs and the AI agent — files written there are automatically uploaded as artifacts and accessible to the agent job

- **Evidence**: The page documents this directory as the data hand-off mechanism
  in two places: the precomputation example writes git and PR data to this directory
  before the agent runs; a dedicated "Agent Data Directory" section explains the
  automatic upload mechanism. Both passages are consistent across multiple WebFetch
  passes.
- **Confidence**: settled (first-party; the path and behavior are stated explicitly
  in both the examples and a dedicated section)
- **Quote**: "Files in `/tmp/gh-aw/agent/` are automatically uploaded as artifacts
  and available to the AI agent." / "Use `/tmp/gh-aw/agent/` to share data with
  AI agents. Files here are automatically uploaded as artifacts and accessible to
  the agent."
- **Our assessment**: This is the most directly actionable claim in the source for
  practitioners building hybrid workflows. The `/tmp/gh-aw/agent/` convention is
  the prescribed interface between deterministic jobs and the agent job — a
  known-location hand-off rather than requiring explicit artifact upload/download
  steps. It connects to `docs-ghaw-compilation-process.md` Claim 9 (the artifact
  inventory) — `agent_output.json` and `cache-memory/` flow the other direction
  (agent → safe outputs); `/tmp/gh-aw/agent/` files flow from deterministic jobs
  into the agent. Together they describe the complete data-flow contract for
  hybrid pipelines. For Ch03 (Orchestration & Workflows): name the `/tmp/gh-aw/agent/`
  directory as the prescribed data-hand-off convention, not just a filesystem path.

### Claim 4: Inline pre-activation steps (`on.steps:`) is the preferred, lightweight approach for trigger filtering — it saves one workflow job vs. the multi-job pattern and is recommended for simple conditions

- **Evidence**: The "Custom Trigger Filtering" section presents four approaches in
  priority order, placing inline steps first and marking it "Preferred." The
  savings and recommendation are stated explicitly. Steps run after built-in
  pre-activation checks and before AI execution. The example shows filtering on
  issue labels using a `grep` exit code.
- **Confidence**: settled (first-party; the preference and job-count savings are
  explicitly stated)
- **Quote**: "This saves one workflow job compared to the multi-job pattern and is
  the recommended approach for lightweight filtering."
- **Our assessment**: The job-count reduction matters for GitHub Actions billing
  and run-time — each job incurs startup overhead (container spinup, checkout,
  cache restoration). For filters that can be expressed as simple shell commands
  or `github-script` steps, using `on.steps:` avoids this overhead entirely. The
  preference guidance is actionable: use `on.steps:` by default; upgrade to
  multi-job only when the filter itself requires heavy tooling. For Ch03: make
  `on.steps:` the default recommendation for trigger filtering, with multi-job
  as the escalation path.

### Claim 5: Steps with IDs in `on.steps:` automatically wire a `<id>_result` output set to `${{ steps.<id>.outcome }}` — no manual output declaration needed for exit-code-based filtering

- **Evidence**: The documentation describes this auto-wiring behavior as a built-in
  platform feature: each step that has an `id` field gets its outcome (success,
  failure, cancelled) exposed as `<id>_result` without the author writing an
  `outputs:` block. The triggered sub-page (`reference/triggers`) confirms that
  explicit outputs in `jobs.pre-activation.outputs` take precedence, meaning the
  auto-wired outputs are a default, not an override.
- **Confidence**: settled (first-party; the auto-wiring is described as a platform
  behavior, not a convention)
- **Quote**: "Each step with an id gets an auto-wired output <id>_result set to
  ${{ steps.<id>.outcome }}"
- **Our assessment**: The auto-wiring removes boilerplate from the common case: if
  you just want to know whether a step succeeded or failed, you do not need to
  write output-declaration YAML. The override path (explicit `jobs.pre-activation.outputs`)
  exists for when the filtering condition is more nuanced (e.g., a step that
  checks a computed value, not just its own exit code). This aligns with
  `docs-ghaw-compilation-process.md` Claim 4 (the pre-activation job runs gating
  checks before AI execution, and failures set `activated=false`) — the `<id>_result`
  outputs are what downstream `if:` conditions read to determine whether to
  activate the agent. For Ch03: document the auto-wiring rule alongside any
  `on.steps:` examples so practitioners know they do not need to declare outputs
  manually for basic filtering.

### Claim 6: The multi-job filtering pattern (separate `jobs:` entry) is for filtering that requires checkouts, compiled tools, or multiple runner types — the compiler automatically adds the filter job as a dependency, resulting in skipped (not failed) workflow runs

- **Evidence**: The "Multi-Job Pattern" subsection is described as the escalation
  path from `on.steps:` for filters that need more than simple shell steps. The
  skipped-not-failed behavior is explicitly contrasted with a naive `if:` approach,
  which would show as failed rather than skipped when the filter does not pass.
- **Confidence**: settled (first-party; the when-to-use condition and skipped
  behavior are stated explicitly)
- **Quote**: "Use a separate jobs: entry when filtering requires heavy tooling
  (checkout, compiled tools, multiple runners)."
- **Our assessment**: The skipped-not-failed behavior is architecturally significant:
  a workflow run that is skipped (because the filter determined it should not run)
  does not pollute the PR status checks or branch protection rules with failure
  indicators. Teams relying on "all checks passed" branch protection need their
  filtering to produce skipped runs, not failed ones. The compiler-automatic
  dependency injection means the author does not need to manually wire the filter
  job into the agent job's `needs:` — the compilation model handles this. For Ch03:
  document the skipped-not-failed guarantee as a branch protection compatibility
  requirement, not just a cosmetic preference.

### Claim 7: Simple GitHub Actions context conditions can be expressed with `if:` directly — no custom job needed when the condition is available in the trigger's context object

- **Evidence**: The "Simple Context Conditions" subsection names this as a fourth,
  simpler alternative for filtering — applicable when the condition can be derived
  from `github.event.*` or other context objects without making additional API calls
  or running shell commands.
- **Confidence**: settled (first-party; stated as a named approach)
- **Quote**: "For conditions that can be expressed directly with GitHub Actions
  context, use if: without a custom job."
- **Our assessment**: This is the simplest filtering path — zero additional jobs,
  zero shell steps, just a YAML expression. The guidance is an important simplicity
  signal: before reaching for `on.steps:` or multi-job, ask whether the condition
  is already in the event context. Common cases: checking event type, checking
  actor login, checking label presence via the `contains()` function. The
  limitation is expressiveness: context conditions cannot make additional API
  calls or run CLI tools. For Ch03: present this as the first filter option to
  consider, before `on.steps:` and before multi-job.

### Claim 8: Query-based filtering with `skip-if-match:` / `skip-if-no-match:` accepts GitHub search query syntax and produces skipped (not failed) runs — the declarative approach for search-result-dependent conditions

- **Evidence**: The "Query-Based Filtering" subsection describes these as `on:`
  section directives that evaluate GitHub search queries before agent activation.
  The skipped-not-failed behavior is consistent with the multi-job pattern (Claim 6).
  The GitHub search query syntax acceptance means practitioners can use the same
  query language they use in GitHub's search bar.
- **Confidence**: settled (first-party; the directives and syntax acceptance are
  stated)
- **Quote**: "For conditions based on GitHub search results, use skip-if-match: or
  skip-if-no-match: in the on: section"
- **Our assessment**: `skip-if-match:` / `skip-if-no-match:` is the declarative
  analog to the imperative `on.steps:` approach. It is the right tool when the
  filtering condition is "are there any open issues matching X?" rather than a
  condition about the triggering event itself. The `skip-if-match:` variant skips
  when the query returns results (i.e., the condition is already satisfied, no
  work to do); `skip-if-no-match:` skips when there are no results (i.e., nothing
  to process). This connects to `docs-ghaw-compilation-process.md` Claim 4, which
  names skip-if-match deduplication as one of the four pre-activation checks —
  `skip-if-match:` in the frontmatter is what generates that check in the compiled
  pre-activation job. For Ch03: document `skip-if-match:` / `skip-if-no-match:`
  as the search-query filtering path, distinct from and complementary to
  `on.steps:`.

### Claim 9: Post-processing is implemented via custom safe-outputs jobs that receive the agent's output and transform or deliver it — enabling formatting, routing, and multi-destination delivery after AI reasoning completes

- **Evidence**: The "Post-Processing Pattern" section shows a code-review workflow
  where custom safe-outputs jobs receive the agent's review output and format/post
  it to the appropriate GitHub destination. The pattern is presented as symmetric
  to precomputation: just as deterministic jobs can run before the agent job, custom
  safe-outputs jobs can run after it.
- **Confidence**: settled (first-party; the pattern is shown with a named example
  workflow)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The post-processing pattern closes the pipeline: deterministic
  work can happen before the agent (precomputation) and after it (post-processing).
  This is architecturally distinct from the agent writing directly via Safe Outputs —
  the agent produces a structured output artifact, and the post-processing job
  applies deterministic transformation before delivery. Use cases include: combining
  AI-generated content with statically computed metadata, routing different parts of
  the agent's output to different GitHub entities (issue + PR comment + Slack
  notification), or applying a deterministic quality gate before posting. For Ch03:
  present post-processing as a named pattern alongside precomputation, framing it
  as the "deterministic last mile" of a hybrid pipeline.

### Claim 10: Shared instruction imports (`imports:` field) enable reuse of common guidance blocks across multiple workflows — including bundling observability configuration with functional instructions in a single import file

- **Evidence**: The "Importing Shared Instructions" section documents the `imports:`
  field as a mechanism for including shared guidance files. The example cites a
  specific shared file (`shared/daily-audit-base.md`) that bundles multiple
  concerns — discussion publishing, reporting guidance, and OTLP observability
  configuration — into a single import. This extends `docs-ghaw-compilation-process.md`
  Claim 2 (BFS import resolution) with a practitioner recommendation for what to
  put in shared files.
- **Confidence**: settled (first-party; the `imports:` field and the shared-file
  recommendation are explicitly documented)
- **Quote**: "For daily discussion-based audit workflows, prefer shared/daily-audit-base.md
  to bundle discussion publishing, reporting guidance, and OTLP observability in a
  single import."
- **Our assessment**: The shared-import example reveals a design intent: shared
  files are not just reusable instruction snippets — they can bundle both behavioral
  instructions and infrastructure configuration (OTLP observability) so that authors
  of related workflows get a consistent operational baseline without copying config
  blocks. This is a harness engineering pattern worth naming: "operational baseline
  import" — a shared file that captures the team's standard observability setup,
  reporting conventions, and escalation instructions as a single composable unit.
  For Ch03 (Orchestration & Workflows): document the `imports:` field as the
  mechanism for team-level workflow standardization, with shared operational
  baseline files as the recommended pattern for consistent observability across
  related workflows.

## Concrete Artifacts

### Three-Stage Hybrid Pipeline Architecture

```
Hybrid Pipeline Model (GitHub Agentic Workflows):

Stage 1: Deterministic Jobs (before AI)
  - Data fetching and API calls (e.g., gh api, curl, gh aw logs)
  - Preprocessing / compilation (e.g., static analysis tools, data aggregation)
  - Trigger filtering (via on.steps:, jobs:, skip-if-match:, or if:)
  - Output: files in /tmp/gh-aw/agent/ (auto-uploaded as artifacts)
  - Output: job outputs / environment variables

Stage 2: Agent Job (AI reasoning)
  - Reads /tmp/gh-aw/agent/ files automatically
  - Applies reasoning over preprocessed data
  - Produces structured output (agent_output.json)

Stage 3: Safe Output Jobs (after AI)
  - Read agent_output.json
  - Execute GitHub API operations (create-issue, add-comment, etc.)
  - Optional: post-processing jobs (format, route, deliver)

Data sharing between jobs:
  Stage 1 → Stage 2: /tmp/gh-aw/agent/ directory (auto-artifact)
  Stage 2 → Stage 3: agent_output.json artifact
  Stage 1 → Stage 2 (metadata): job outputs, environment variables
```

*Source: `guides/deterministic-agentic-patterns` — "Architecture" and "Agent Data Directory" sections*

### Trigger Filtering Decision Guide (Four Approaches)

```
Approach                    When to Use                              Behavior on Skip
─────────────────────────────────────────────────────────────────────────────────────
if: <context-expr>          Condition is in github.event.* or        Skipped run
  (no custom job)           other trigger context; no API calls
                            or shell commands needed

on.steps: (inline)          Condition requires shell commands or      Skipped run
  PREFERRED for lightweight uses action steps; checkout not
  filters                   needed; no compiled tools

jobs: <filter-job>          Condition requires checkout, compiled     Skipped run
  (multi-job pattern)       tools, or a separate runner type         (compiler auto-adds
  For complex filters                                                  as dependency)

skip-if-match:/             Condition is based on GitHub search       Skipped run
skip-if-no-match:           query results (existing issues,
  (on: section)             PRs, etc.)
```

*Source: `guides/deterministic-agentic-patterns` — "Custom Trigger Filtering" section*

### Inline Steps (`on.steps:`) — Auto-Wired Output Pattern

```yaml
# Example: filter on bug label using inline pre-activation step
on:
  issues:
    types: [opened]
  steps:
    - name: Check issue has bug label
      id: label_check                     # <- id triggers auto-wiring
      env:
        LABELS: ${{ toJSON(github.event.issue.labels.*.name) }}
      run: echo "$LABELS" | grep -q '"bug"'
      # No outputs: block needed
      # Platform auto-wires: label_check_result = ${{ steps.label_check.outcome }}
      # Values: 'success' | 'failure' | 'cancelled'

# Use in downstream if: condition
if: needs.pre_activation.outputs.label_check_result == 'success'
```

*Source: `guides/deterministic-agentic-patterns` — "Inline Steps (on.steps:) — Preferred" section;
 output behavior confirmed via `reference/triggers` — "Pre-Activation Steps" section*

### Pre-Activation Step Output Rules (from `reference/triggers`)

```
Auto-wired output:
  Each step with an id gets: <id>_result = ${{ steps.<id>.outcome }}
  Values: 'success' | 'failure' | 'cancelled'

Override:
  Explicit outputs defined in jobs.pre-activation.outputs take precedence
  over auto-wired <id>_result outputs.

on.permissions (for on.steps: that need GitHub API access):
  - Merged on top of default pre-activation permissions
  - Scopes: actions, checks, contents, deployments, discussions, issues,
    packages, pages, pull-requests, repository-projects, security-events, statuses
```

*Source: `reference/triggers` — "Pre-Activation Steps" and "Pre-Activation Permissions" sections*

### Precomputation Example — Data Exchange via `/tmp/gh-aw/agent/`

```yaml
# Workflow: .github/workflows/release-highlights.md (frontmatter sketch)
on:
  push:
    tags: ["v*.*.*"]
safe-outputs:
  update-release:
# ...
steps:
  - name: Fetch release data
    run: |
      # Write data for the agent to /tmp/gh-aw/agent/
      git log ... > /tmp/gh-aw/agent/commits.txt
      gh api /repos/.../pulls ... > /tmp/gh-aw/agent/prs.json
      # Files auto-uploaded; agent job reads them without explicit download
```

```yaml
# Workflow: .github/workflows/static-analysis.md (multi-job pattern sketch)
on:
  schedule: daily
engine: claude
jobs:
  run-analysis:
    # Separate job: compiles analysis results
    steps:
      - uses: actions/checkout@...
      - run: ./tools/analyze.sh > /tmp/output.txt
    # Agent job downloads artifacts, creates discussion
```

*Source: `guides/deterministic-agentic-patterns` — "Precomputation Example" and "Multi-Job Pattern" sections*

### Query-Based Filter Examples

```yaml
# Skip if the issue was already processed (a matching issue exists)
on:
  issues:
    types: [opened]
  skip-if-match: "is:issue label:processed repo:owner/repo"

# Skip if there are no open PRs needing review
on:
  schedule: every hour
  skip-if-no-match: "is:pr is:open review-requested:my-bot"
```

*Source: `guides/deterministic-agentic-patterns` — "Query-Based Filtering" section*

### Shared Operational Baseline Import Pattern

```yaml
# In workflow frontmatter
imports:
  - shared/daily-audit-base.md  # bundles: discussion publishing + reporting
                                 # guidance + OTLP observability config
```

```
Operational baseline import (shared/daily-audit-base.md) bundles:
  - Discussion publishing instructions (create-discussion safe output config)
  - Reporting guidance (structure, tone, level of detail for audit reports)
  - OTLP observability (endpoint config, span attributes)

Effect: all daily audit workflows that import this file share a consistent
operational baseline without duplicating config blocks.
```

*Source: `guides/deterministic-agentic-patterns` — "Importing Shared Instructions" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 2 ("combine deterministic GitHub Actions
    infrastructure with AI-driven decision-making"): This guide is the practitioner
    pattern reference for exactly that framing — it names and illustrates the three
    stages where deterministic infrastructure (pre-jobs, safe-output jobs) wraps
    AI decision-making (the agent job). The conceptual claim and the pattern
    implementation now have matching documentation.
  - `docs-ghaw-compilation-process.md` Claim 4 (pre-activation job runs gating
    checks including skip-if-match deduplication before AI execution, failures
    set `activated=false`): Claim 8 here (query-based filtering via `skip-if-match:`
    / `skip-if-no-match:`) is the author-facing interface that generates those
    pre-activation checks. The two sources together give the complete picture:
    `compilation-process` documents what the pre-activation job does; this source
    documents how authors declare what those checks should be.
  - `docs-ghaw-compilation-process.md` Claim 9 (agent job produces artifacts
    including `agent_output.json` and `cache-memory/`): Claim 3 here documents the
    incoming data path (`/tmp/gh-aw/agent/` → agent job); Claim 9 in
    `compilation-process` documents the outgoing path (agent job → `agent_output.json`
    → safe output jobs). Together they define the complete data-flow contract for
    hybrid pipelines.
  - `docs-ghaw-compilation-process.md` Claim 2 (import resolution via BFS
    traversal): Claim 10 here (shared instruction imports bundling operational
    baseline config) is a practitioner recommendation for what to put in those
    import files. The compilation mechanism (BFS traversal, cycle detection) is
    the implementation; this source adds the design guidance for import contents.

- **Extends**:
  - `docs-ghaw-orchestration-patterns.md` Claim 1 (orchestrator/worker fan-out
    as the canonical multi-agent pattern): The multi-job filtering pattern in this
    source (Claim 6) is a simpler, single-agent variant — a deterministic filter job
    running before the agent job, not a full orchestrator dispatching multiple workers.
    Together the two sources cover the pattern space: simple pre-processing (this
    source) → full fan-out orchestration (orchestration-patterns). The decision
    between them is: do you need parallel workers or sequential pre/post steps?
  - `docs-ghaw-agentic-ops.md` Claim 6 (two-workflow pipeline via shared
    `repo-memory` with scheduled offset): The precomputation pattern here (Claim 2,
    Claim 3) is a same-workflow variant of that coordination model — deterministic
    steps run as jobs within the same workflow run, not as a separate scheduled
    workflow. Together they give two coordination styles: inline pre-processing
    within a single run vs. pipeline coordination between distinct scheduled runs.
  - `docs-ghaw-agentic-authoring.md` Claim 8 ("what, not how" principle for workflow
    instruction sections): The shared operational baseline import pattern (Claim 10)
    is a complement — it allows the "what" instructions to remain in the workflow
    markdown while the "how" for common concerns (OTLP config, reporting structure)
    lives in a shared import file. The two together give a complete picture of the
    instruction composition model.

- **Contradicts**: None identified. No existing source note makes claims that
  conflict with the three-stage pipeline model, the `/tmp/gh-aw/agent/` directory
  convention, the trigger-filtering hierarchy, or the import-based instruction
  reuse pattern. The pre-activation job description in `docs-ghaw-compilation-process.md`
  Claim 4 is fully consistent with the filtering approaches documented here. No
  contradiction issue required.

- **Novel**:
  - **Three-stage hybrid pipeline as a named architecture** (Claim 1): No existing
    source note names the deterministic → agent → safe-outputs pipeline as a
    three-stage model. `docs-ghaw-how-they-work.md` Claim 2 states the conceptual
    framing; this is the first source that names it as a pattern with three
    distinct stages.
  - **`/tmp/gh-aw/agent/` as the designated data-exchange directory** (Claim 3):
    No existing source note documents this directory or its auto-upload behavior.
    This is the first corpus description of the data-hand-off convention between
    deterministic and agent jobs.
  - **Four-approach trigger-filtering taxonomy with priority order** (Claims 4–8):
    `docs-ghaw-compilation-process.md` Claim 4 names the pre-activation checks
    at the compilation level; no existing source note provides the author-facing
    decision guide for which filtering approach to use when.
  - **`<id>_result` auto-wiring behavior** (Claim 5): The auto-wired output
    convention for pre-activation steps — no `outputs:` block needed for exit-code
    filters — is not documented in any existing corpus note.
  - **Query-based filtering with GitHub search syntax** (Claim 8): `skip-if-match:`
    / `skip-if-no-match:` accepting GitHub search query syntax as `on:` section
    directives is not documented in any existing corpus note beyond the brief
    reference in `docs-ghaw-compilation-process.md` Claim 4 (which names
    "skip-if-match deduplication" as one check type without documenting the
    author-facing directive).
  - **Post-processing as a named pipeline stage** (Claim 9): The idea that custom
    safe-outputs jobs can act as a "deterministic last mile" — transforming or
    routing agent output before delivery — is not named as a distinct pattern in
    any existing source note.
  - **Shared operational baseline import file as a pattern** (Claim 10): The
    concept of a shared import file that bundles observability config + behavioral
    instructions as a team-level operational baseline is not described in any
    existing corpus note. `docs-ghaw-compilation-process.md` Claim 2 documents
    the import mechanism; this is the first corpus entry recommending what to put
    in shared import files.

## Guide Impact

### Chapter 03: Orchestration & Workflows

- **Name the three-stage hybrid pipeline as the foundational GHAW composition
  model** (Claim 1): Add the deterministic → agent → safe-outputs architecture
  as the named model for hybrid pipelines, alongside the purely deterministic
  Actions workflow and the purely agentic workflow. The three stages are the
  practitioner's mental model for decomposing work into "what should be
  deterministic" vs. "what requires AI reasoning."

- **Document `/tmp/gh-aw/agent/` as the data-hand-off convention** (Claim 3):
  When deterministic pre-processing jobs gather data for the agent, the prescribed
  convention is to write it to `/tmp/gh-aw/agent/`. This eliminates the need for
  explicit artifact upload/download steps in the workflow spec. The guide should
  name this directory and explain its auto-upload behavior.

- **Add the four-approach trigger filtering decision guide** (Claims 4–8): Present
  as a decision table: start with `if:` (context-only conditions), escalate to
  `on.steps:` (shell commands, lightweight filtering), escalate to multi-job (heavy
  tooling), and use `skip-if-match:` / `skip-if-no-match:` for search-query
  conditions. All four produce skipped-not-failed runs when the condition is not met.

- **Name post-processing as the "deterministic last mile"** (Claim 9): Custom
  safe-outputs jobs that transform agent output before delivery are the post-processing
  pattern. Document alongside precomputation as the symmetric bookend: deterministic
  first (precompute) and deterministic last (post-process) wrap AI reasoning.

### Chapter 05: Agent Patterns

- **Add the five-category use-case taxonomy for deterministic-agentic hybrids**
  (Claim 2): When should practitioners add deterministic steps to an agentic
  workflow? The five categories — precompute data, filter triggers, preprocess
  inputs, post-process outputs, build multi-stage pipelines — are the decision
  criteria. Each maps to a distinct concern (cost, performance, context quality,
  formatting, reasoning complexity).

- **Document the `<id>_result` auto-wiring pattern** (Claim 5): Practitioners
  writing `on.steps:` filters do not need to declare `outputs:` blocks for
  exit-code-based filtering. The platform auto-wires `<id>_result = success|failure`.
  This reduces boilerplate and the friction of adopting inline filtering.

### Chapter 06: Production Readiness

- **Add shared operational baseline imports as a team standardization pattern**
  (Claim 10): Teams running multiple related workflows should define a shared
  operational baseline import file that bundles: observability config (OTLP
  endpoint/headers), reporting guidance (structure, tone, level of detail), and
  output routing (discussion publishing config). Referencing by import rather
  than copy-paste ensures consistent observability across the fleet.

## Extraction Notes

1. **WebFetch returns AI-processed content**: The `gh aw` documentation site
   is an Astro/Starlight SPA; WebFetch renders content through an AI model before
   returning it. Three independent fetches were made (two to the main
   `guides/deterministic-agentic-patterns` page and one to the linked
   `reference/triggers` sub-page). Quotes were validated by cross-checking
   consistency across the two main-page fetches. Claims where quote text was
   inconsistent across fetches are marked "(no direct quote; see paraphrase in
   Our assessment)" per MINER.md §2a.

2. **Sub-pages followed**: The guide links to `reference/triggers` (pre-activation
   steps and permissions), `reference/compilation-process`, `reference/imports`,
   and `reference/templating`. The `reference/triggers` sub-page was fetched and
   contributed the `<id>_result` auto-wiring behavior (Claim 5) and the
   `on.permissions` merging behavior. The other linked pages were not followed —
   they are covered by existing corpus notes (`docs-ghaw-compilation-process.md`)
   or are API-reference style pages outside this guide's scope.

3. **Workflow filenames extracted**: The page references three named workflow
   examples: `.github/workflows/release-highlights.md` (precomputation),
   `.github/workflows/static-analysis.md` (multi-job pattern), and
   `.github/workflows/code-review.md` (post-processing). These are example
   filenames from the documentation, not from a reference implementation
   repository.

4. **No YAML frontmatter blocks available verbatim**: The guide page documents
   patterns with workflow filename references and prose descriptions, not full
   YAML blocks. The YAML in the Concrete Artifacts section is reconstructed from
   the documented behavior and examples; it is schema-illustrative, not
   character-for-character from the source. Practitioners should consult the
   full workflow references for authoritative YAML.

5. **No contradictions to file**: Reviewed all existing source notes against
   all claims. No claims here materially oppose any existing source note at the
   MINER.md §4a threshold. The three-stage pipeline model and the `/tmp/gh-aw/agent/`
   convention are additive to the existing corpus; the filtering approaches extend
   `docs-ghaw-compilation-process.md` Claim 4 without opposing it.

6. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   the current `gh aw` platform as of 2026-05-10.
