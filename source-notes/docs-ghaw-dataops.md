---
source_url: https://github.github.com/gh-aw/patterns/data-ops/
source_type: docs
title: "GitHub Agentic Workflows: DataOps Pattern"
author: GitHub Agentic Workflows team (official documentation)
date_published: null
date_extracted: 2026-05-01
last_checked: 2026-05-01
status: current
confidence_overall: emerging
issue: "#324"
---

# GitHub Agentic Workflows: DataOps Pattern

> The canonical reference for the DataOps pattern — documents the deterministic-
> then-agentic architectural split (shell `steps:` own data collection; the AI
> agent owns analysis), a complete Weekly PR Summary YAML workflow, the GitHub
> Actions `cache:` directive for data persistence between runs, multi-source
> aggregation via `jq -s`, and the five DataOps best practices — establishing
> the named "collect deterministically, analyze agentically" design pattern for
> gh-aw data workflows.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, "Patterns"
  section, "DataOps" page; not a blog post or practitioner account)
- **Author credibility**: First-party documentation from the GitHub Agentic
  Workflows team — the same team behind Peli de Halleux / Don Syme's agent
  factory series and the authoritative `gh aw` platform documentation. Claims
  about the DataOps pattern, step structure, and caching configuration are
  settled for this platform; the architectural principle (deterministic data
  collection + agentic analysis) is a design pattern that generalizes beyond
  gh-aw but is documented here only in that platform's context.
- **Scope**: Covers the DataOps design pattern: the two-phase architecture
  (deterministic steps + agent analysis phase), the `/tmp/gh-aw/` data handoff
  convention, GitHub Actions `cache:` directive for workflow-level data
  persistence, multi-source data aggregation via `jq -s`, explicit data
  location documentation in the agent prompt, and `safe-outputs:
  create-discussion` for report surfacing. Includes a complete Weekly PR
  Summary workflow spec. Does NOT cover: `cache-memory:` agent state persistence
  (see `docs-ghaw-audit-with-agents.md` and `docs-ghaw-dailyops.md`), the Safe
  Outputs permission model (see `docs-ghaw-how-they-work.md`), or the
  DailyOps scheduling/phased-approval pattern (see `docs-ghaw-dailyops.md`).

## Extracted Claims

### Claim 1: DataOps is a named gh-aw pattern that splits workflow execution into a deterministic data-collection phase (shell `steps:`) and an agentic analysis phase

- **Evidence**: The page defines DataOps as a pattern that "merges deterministic
  data collection with AI-powered analysis." The architectural summary:
  "Shell commands in `steps:` reliably collect and prepare data (fast, cacheable,
  reproducible), then the AI agent reads the results and generates insights."
  The full Weekly PR Summary workflow spec implements this split with two named
  steps (data collection via `gh pr list`, statistics via `jq`) before the agent
  prompt.
- **Confidence**: settled (first-party documentation; the pattern is named,
  defined, and illustrated with a complete workflow spec)
- **Quote**: "Shell commands in `steps:` reliably collect and prepare data
  (fast, cacheable, reproducible), then the AI agent reads the results and
  generates insights."
- **Our assessment**: This is an important architectural naming in the gh-aw
  corpus. The deterministic-then-agentic split is implied by the step/agent
  structure across multiple other gh-aw notes, but here it is named explicitly
  as "DataOps" and described as a design pattern. The key distinction: the
  step phase is deterministic (same inputs → same outputs), fast (shell
  commands, no token usage), and cacheable (can be skipped on cache hit);
  the agent phase is non-deterministic (AI interpretation), slower (LLM
  inference), and context-dependent. Separating them maximizes the value of
  each. For Ch05 (agent orchestration): the DataOps pattern operationalizes
  the broader `docs-ghaw-how-they-work.md` Claim 2 ("combine deterministic
  GitHub Actions infrastructure with AI-driven decision-making") into a
  concrete workflow structure.

### Claim 2: Pre-computing aggregations in deterministic `steps:` reduces agent token consumption

- **Evidence**: Explicitly stated as a best practice: "Pre-compute aggregations
  to reduce token usage." The Weekly PR Summary example demonstrates this: a
  `jq` step computes summary statistics (merged/open/closed counts,
  additions, deletions, top authors) and saves to `stats.json` — the agent
  then reads the pre-computed summary rather than receiving 100 raw PR records.
- **Confidence**: emerging (stated as a best practice in first-party
  documentation; the mechanism is logically sound — fewer tokens in the prompt
  means lower cost and less context noise — but no quantification is provided)
- **Quote**: "Pre-compute aggregations to reduce agent token consumption."
- **Our assessment**: This is the most actionable cost-optimization claim in
  the DataOps pattern. If the agent receives 100 raw JSON PR objects, it
  processes each during reasoning; if it receives pre-computed counts and top-5
  lists, it can focus on insight generation rather than arithmetic. The
  `jq` aggregation in the example produces a stats.json with total, merged,
  open, closed counts plus top-5 authors — the agent never sees the
  raw PR array. This is a transferable pattern beyond gh-aw: any
  context-window-aware system should pre-compute aggregations in a deterministic
  layer before passing data to the LLM. For Ch04 (context engineering): this
  is a concrete data-preparation technique for reducing context size without
  losing analytical value.

### Claim 3: `/tmp/gh-aw/` is the standard ephemeral data handoff location between deterministic steps and the agent prompt

- **Evidence**: The Weekly PR Summary workflow saves data to
  `/tmp/gh-aw/pr-data/recent-prs.json` (raw API data) and
  `/tmp/gh-aw/pr-data/stats.json` (aggregated statistics). The agent prompt
  then references these exact paths: "Analyze the prepared data:
  `/tmp/gh-aw/pr-data/recent-prs.json` - Last 100 PRs with full metadata /
  `/tmp/gh-aw/pr-data/stats.json` - Pre-computed statistics." The multi-source
  example similarly uses `/tmp/gh-aw/prs.json`, `/tmp/gh-aw/issues.json`,
  `/tmp/gh-aw/runs.json`, and `/tmp/gh-aw/combined.json`.
- **Confidence**: settled (consistent across all examples on the page;
  corroborated by `docs-ghaw-ephemerals.md` which confirms `/tmp/gh-aw/` as
  the platform's ephemeral storage root)
- **Quote**: (path pattern used consistently in all code examples)
- **Our assessment**: The `/tmp/gh-aw/` path convention is the glue between
  the deterministic steps phase and the agent phase. Steps write to
  `/tmp/gh-aw/<workflow-specific-subdir>/`; the agent prompt documents
  what files are there and what they contain. This creates a clean interface:
  the steps own data production, the agent owns data consumption. The
  convention matches `docs-ghaw-ephemerals.md`'s documentation of
  `/tmp/gh-aw/` as the platform-standard ephemeral storage root, and
  `docs-ghaw-audit-with-agents.md`'s use of `/tmp/gh-aw/cache-memory/`
  for agent state persistence. For Ch02 (harness engineering): the
  `steps:` → `/tmp/gh-aw/` → agent prompt data handoff is the canonical
  DataOps integration point; document it as the standard file-passing
  convention for gh-aw data workflows.

### Claim 4: The GitHub Actions `cache:` directive persists step-extracted data between workflow runs, preventing redundant API calls

- **Evidence**: The page documents a `cache:` frontmatter block:
  ```yaml
  cache:
    - key: pr-data-${{ github.run_id }}
      path: /tmp/gh-aw/pr-data
      restore-keys: |
        pr-data-
  ```
  The accompanying step uses a cache-hit check:
  ```bash
  if [ -f /tmp/gh-aw/pr-data/recent-prs.json ]; then
    echo "Using cached data"
  else
    gh pr list --limit 100 --json ... > /tmp/gh-aw/pr-data/recent-prs.json
  fi
  ```
  The pattern is described for "frequently-running workflows processing large
  datasets" to "prevent redundant API calls on frequent runs."
- **Confidence**: emerging (first-party documentation with working YAML;
  the standard GitHub Actions cache mechanism is well-established, but the
  gh-aw `cache:` frontmatter integration is platform-specific)
- **Quote**: "prevents redundant API calls on frequent runs"
- **Our assessment**: This `cache:` directive is the standard GitHub Actions
  data cache, distinct from `cache-memory:` (the GHAW-specific agent state
  persistence from `docs-ghaw-audit-with-agents.md` and
  `docs-ghaw-dailyops.md`). The difference is important: `cache:` stores
  step-extracted raw/aggregated data from GitHub APIs (cost of collection:
  API rate limit); `cache-memory:` stores agent-generated JSON state
  (cost of regeneration: LLM inference). DataOps uses `cache:` for the
  deterministic-phase output; DailyOps and audit workflows use `cache-memory:`
  for agent-phase state. Teams should use both when appropriate: `cache:` to
  avoid re-fetching the same API data within a day; `cache-memory:` to carry
  agent-computed baselines across weeks. For Ch02: add this two-cache model
  as a concrete harness optimization pattern.

### Claim 5: Multi-source data (PRs, issues, CI runs) should be aggregated via `jq -s` into a unified JSON object before the agent receives it

- **Evidence**: The "Advanced: Multi-Source Data" section provides a four-step
  pattern: three separate `gh` API calls writing to individual files, then a
  `jq -s` combine step:
  ```bash
  jq -s '{prs: .[0], issues: .[1], runs: .[2]}' \
    /tmp/gh-aw/prs.json \
    /tmp/gh-aw/issues.json \
    /tmp/gh-aw/runs.json \
    > /tmp/gh-aw/combined.json
  ```
  The agent then receives a single `combined.json` with named keys.
- **Confidence**: emerging (first-party pattern with code example; the
  architectural reasoning — unified object reduces prompt complexity — is
  sound, but no comparison with alternative approaches is provided)
- **Quote**: (from the multi-source example YAML — combine step)
- **Our assessment**: The `jq -s` combine pattern is important for two
  reasons. First, it gives the agent a single file to reason about rather
  than multiple coordination points. Second, it enforces named structure —
  `{prs: [...], issues: [...], runs: [...]}` makes the data source explicit
  within the combined object, preventing the agent from confusing record
  types. The Repository Health Report example uses cross-domain analysis:
  "Pull request velocity and review times / Issue response rates and
  resolution times / CI/CD success rates and flaky tests" — queries that
  require correlating across all three data sources. For Ch04 (context
  engineering): the `jq -s` combine step is the canonical multi-source
  data normalization technique for DataOps workflows.

### Claim 6: The agent prompt must explicitly document data file locations and formats to enable effective analysis

- **Evidence**: The Weekly PR Summary agent prompt demonstrates this:
  ```
  # Weekly Pull Request Summary
  Analyze the prepared data:
  - `/tmp/gh-aw/pr-data/recent-prs.json` - Last 100 PRs with full metadata
  - `/tmp/gh-aw/pr-data/stats.json` - Pre-computed statistics
  Create a discussion summarizing: total PRs, merge rate, code changes
  (+/- lines), top contributors, and any notable trends.
  ```
  Stated as an explicit best practice: "Document data locations — Inform the
  agent where data resides and expected format."
- **Confidence**: settled (stated explicitly as a best practice and demonstrated
  in the workflow example)
- **Quote**: "Document data locations — Inform the agent where data resides
  and expected format."
- **Our assessment**: This is a context-engineering principle specific to
  DataOps: the agent needs a map of the data it is being asked to analyze.
  Without explicit paths and format descriptions, the agent may hallucinate
  data structure or fail to locate files. The prompt in the example is a
  "data manifest" — it tells the agent where each file lives, how many
  records it contains, and what keys are present. This is the DataOps
  equivalent of the "show your work" principle: the step phase produces the
  data; the prompt manifests it; the agent interprets it. For Ch04:
  recommend the data-manifest pattern as a standard agent prompt section
  for any DataOps workflow — one bullet per file, with path, description,
  and format.

### Claim 7: `safe-outputs: create-discussion` with `close-older-discussions: true` is the standard report surfacing pattern for DataOps workflows

- **Evidence**: The Weekly PR Summary workflow uses:
  ```yaml
  safe-outputs:
    create-discussion:
      title-prefix: "[weekly-summary] "
      category: "announcements"
      max: 1
      close-older-discussions: true
  ```
  The pattern creates one discussion per run, closes older ones, and enforces
  a single active report via `max: 1`. Presented in the documentation as the
  standard mechanism for "surfacing agent-generated reports."
- **Confidence**: emerging (one detailed example shown; the pattern is
  consistent with `docs-ghaw-dailyops.md` Claim 4's discussion-based progress
  tracking, and `docs-ghaw-audit-with-agents.md` Claim 11's weekly digest
  using Discussions)
- **Quote**: "Use safe outputs — Discussions work well for reports, supporting
  threading and reactions."
- **Our assessment**: The combination of `close-older-discussions: true`,
  `max: 1`, and `title-prefix:` gives a "living report" pattern: each run
  replaces the previous report with a fresh one, while the title-prefix allows
  the workflow to find its own prior report. Discussions are preferred over
  Issues for this use case because Discussions support threading (readers can
  ask follow-up questions) and reactions (team members can signal engagement)
  without creating tracker noise. The `category: "announcements"` designation
  makes DataOps reports a formal communication channel rather than a side
  discussion. For Ch02: this four-field `safe-outputs: create-discussion`
  block is the canonical DataOps report output pattern; document it with
  its full semantics.

### Claim 8: `strict: true` is used in DataOps workflows to enforce stricter agent compliance with the workflow specification

- **Evidence**: The Weekly PR Summary frontmatter includes `strict: true`
  alongside `engine: copilot`. The page does not fully explain the semantics
  of this flag in this context, but it appears as part of the recommended
  DataOps workflow configuration.
- **Confidence**: anecdotal (present in the example; semantics not explained
  in full on this page; a single data point)
- **Quote**: `strict: true` (from the Weekly PR Summary frontmatter)
- **Our assessment**: The `strict: true` field appears in this DataOps example
  but is not defined on this page. Based on context (DataOps workflows
  interact with real GitHub data and post to Discussions), this likely
  enforces that the agent follows the safe-outputs configuration precisely
  and does not attempt unauthorized actions. The flag may be relevant to
  the five-layer security model described in `docs-ghaw-how-they-work.md`
  (compile-time validation). For Ch02: note `strict: true` as present
  in the reference DataOps workflow; wait for authoritative documentation
  of its semantics before prescribing it.

### Claim 9: `jq` is the prescribed statistical aggregation tool for DataOps steps, providing a complete example pipeline for PR activity metrics

- **Evidence**: The Weekly PR Summary compute-statistics step provides a
  full `jq` pipeline:
  ```bash
  jq '{
    total: length,
    merged: [.[] | select(.state == "MERGED")] | length,
    open: [.[] | select(.state == "OPEN")] | length,
    closed: [.[] | select(.state == "CLOSED")] | length,
    total_additions: [.[].additions] | add,
    total_deletions: [.[].deletions] | add,
    total_files_changed: [.[].changedFiles] | add,
    authors: [.[].author.login] | unique | length,
    top_authors: ([.[].author.login] | group_by(.) | map({author: .[0], count: length}) | sort_by(-.count) | .[0:5])
  }' recent-prs.json > stats.json
  ```
  `awk` and Python are also mentioned alongside `jq` as acceptable tools in
  the best practices section.
- **Confidence**: settled (first-party documentation; a complete, working `jq`
  pipeline is provided verbatim)
- **Quote**: "Pre-compute aggregations with `jq`, `awk`, or Python"
- **Our assessment**: The `jq` pipeline is the highest-value concrete artifact
  on the page — it is directly reusable. The pipeline demonstrates how to
  reduce 100 JSON objects to a structured summary with counts, totals, unique
  authors, and a ranked top-5 list. Each `jq` expression is a pattern:
  `[.[] | select(.state == "MERGED")] | length` for filtered counts;
  `[.[].additions] | add` for field totals; `group_by(.) | map({...}) |
  sort_by(-.count)` for frequency ranking. These patterns apply to any
  GitHub API response, not just PR data. For Ch04 (context engineering):
  the `jq` aggregation pipeline is a concrete pre-processing template for
  reducing GitHub API responses to agent-consumable summaries.

### Claim 10: DataOps steps require `GH_TOKEN` via environment variable for GitHub CLI access

- **Evidence**: The data-collection step in the Weekly PR Summary spec uses:
  ```yaml
  env:
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  ```
  This is required for the `gh pr list` command to authenticate against the
  GitHub API.
- **Confidence**: settled (standard GitHub CLI authentication pattern;
  consistent with other gh-aw workflow specs in the corpus)
- **Quote**: `env:\n  GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}`
- **Our assessment**: Boilerplate but worth noting: in DataOps workflows,
  the deterministic step phase requires explicit `GITHUB_TOKEN` injection
  via the `env:` block for the `gh` CLI. The agent phase (natural language
  prompt) does not need this because it uses the MCP tool layer for GitHub
  API access. This means the two phases use different authentication paths:
  shell steps use `GH_TOKEN` env var; agent tools use the MCP tool
  permission model. For Ch02: note this as a configuration requirement for
  DataOps step definitions.

## Concrete Artifacts

### DataOps — Two-Phase Structure (from documentation)

```
Phase 1: Steps (Deterministic)
  → Extract data using shell commands (gh, curl, etc.)
  → Pre-compute aggregations with jq, awk, or Python
  → Save structured output to /tmp/gh-aw/<subdir>/
  Properties: fast, cacheable, reproducible, no token usage

Phase 2: Agent (Agentic)
  → Read prepared data files from /tmp/gh-aw/
  → Generate insights and analysis
  → Create reports via safe outputs (discussions, etc.)
  Properties: context-dependent, token-consuming, non-deterministic
```
*Source: gh-aw DataOps pattern documentation, "Core Pattern" section*

### Weekly PR Summary — Complete Workflow Spec

```yaml
---
name: Weekly PR Summary
description: Summarizes pull request activity from the last week

on:
  schedule: weekly
  workflow_dispatch:

permissions:
  contents: read
  pull-requests: read

engine: copilot
strict: true

network:
  allowed:
    - defaults
    - github

safe-outputs:
  create-discussion:
    title-prefix: "[weekly-summary] "
    category: "announcements"
    max: 1
    close-older-discussions: true

tools:
  bash: ["*"]

steps:
  - name: Fetch recent pull requests
    env:
      GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    run: |
      mkdir -p /tmp/gh-aw/pr-data
      gh pr list \
        --repo "${{ github.repository }}" \
        --state all \
        --limit 100 \
        --json number,title,state,author,createdAt,mergedAt,closedAt,additions,deletions,changedFiles,labels \
        > /tmp/gh-aw/pr-data/recent-prs.json
      echo "Fetched $(jq 'length' /tmp/gh-aw/pr-data/recent-prs.json) PRs"

  - name: Compute summary statistics
    run: |
      cd /tmp/gh-aw/pr-data
      jq '{
        total: length,
        merged: [.[] | select(.state == "MERGED")] | length,
        open: [.[] | select(.state == "OPEN")] | length,
        closed: [.[] | select(.state == "CLOSED")] | length,
        total_additions: [.[].additions] | add,
        total_deletions: [.[].deletions] | add,
        total_files_changed: [.[].changedFiles] | add,
        authors: [.[].author.login] | unique | length,
        top_authors: ([.[].author.login] | group_by(.) | map({author: .[0], count: length}) | sort_by(-.count) | .[0:5])
      }' recent-prs.json > stats.json
      echo "Statistics computed:"
      cat stats.json

    timeout-minutes: 10
---
# Weekly Pull Request Summary
Analyze the prepared data:
- `/tmp/gh-aw/pr-data/recent-prs.json` - Last 100 PRs with full metadata
- `/tmp/gh-aw/pr-data/stats.json` - Pre-computed statistics

Create a discussion summarizing: total PRs, merge rate, code changes (+/- lines),
top contributors, and any notable trends. Keep it concise and factual.
```
*Source: gh-aw DataOps pattern documentation, "Practical Example: Weekly PR Summary"*

### Data Caching — Workflow-Level Cache Directive

```yaml
---
cache:
  - key: pr-data-${{ github.run_id }}
    path: /tmp/gh-aw/pr-data
    restore-keys: |
      pr-data-

steps:
  - name: Check cache and fetch only new data
    run: |
      if [ -f /tmp/gh-aw/pr-data/recent-prs.json ]; then
        echo "Using cached data"
      else
        gh pr list --limit 100 --json ... > /tmp/gh-aw/pr-data/recent-prs.json
      fi
---
```
*Source: gh-aw DataOps pattern documentation, "Data Caching" section*

### Multi-Source Data Aggregation — jq -s Pattern

```yaml
---
steps:
  - name: Fetch PR data
    run: gh pr list --json ... > /tmp/gh-aw/prs.json

  - name: Fetch issue data
    run: gh issue list --json ... > /tmp/gh-aw/issues.json

  - name: Fetch workflow runs
    run: gh run list --json ... > /tmp/gh-aw/runs.json

  - name: Combine into unified dataset
    run: |
      jq -s '{prs: .[0], issues: .[1], runs: .[2]}' \
        /tmp/gh-aw/prs.json \
        /tmp/gh-aw/issues.json \
        /tmp/gh-aw/runs.json \
        > /tmp/gh-aw/combined.json
---
# Repository Health Report
Analyze the combined data at `/tmp/gh-aw/combined.json` covering:
- Pull request velocity and review times
- Issue response rates and resolution times
- CI/CD success rates and flaky tests
```
*Source: gh-aw DataOps pattern documentation, "Advanced: Multi-Source Data" section*

### DataOps Best Practices (from documentation)

```
1. Keep steps deterministic  — identical inputs produce identical outputs;
                               eliminate randomness or time-dependent logic
2. Pre-compute aggregations  — use jq, awk, or Python to calculate statistics
                               upfront, reducing agent token consumption
3. Structure data clearly    — output JSON with explicit field names; include
                               summary files alongside raw data
4. Document data locations   — inform the agent where data resides and expected
                               format
5. Use safe outputs          — Discussions work well for reports, supporting
                               threading and reactions
```
*Source: gh-aw DataOps pattern documentation, "Best Practices" section*

### jq Statistical Aggregation Pipeline

```bash
# From the Weekly PR Summary compute step — reusable pattern for any PR dataset
jq '{
  total: length,
  merged: [.[] | select(.state == "MERGED")] | length,
  open:   [.[] | select(.state == "OPEN")]   | length,
  closed: [.[] | select(.state == "CLOSED")] | length,
  total_additions:    [.[].additions]    | add,
  total_deletions:    [.[].deletions]    | add,
  total_files_changed:[.[].changedFiles] | add,
  authors:     [.[].author.login] | unique | length,
  top_authors: ([.[].author.login]
    | group_by(.)
    | map({author: .[0], count: length})
    | sort_by(-.count)
    | .[0:5])
}' recent-prs.json > stats.json
```
*Source: gh-aw DataOps pattern documentation, "Compute summary statistics" step*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 2 (deterministic GitHub Actions
    infrastructure + AI-driven decision-making): DataOps is the concrete
    implementation of this architectural principle as a named workflow pattern.
    That note states the design principle; this note provides the playbook.
  - `docs-ghaw-ephemerals.md` Claims 1–6 (`/tmp/gh-aw/` as ephemeral storage
    root; cache-memory cleanup): the `/tmp/gh-aw/` data handoff path in
    DataOps is the same ephemeral root that the Ephemerals page documents.
    DataOps uses this path for step-to-agent data transfer; Ephemerals
    documents its lifecycle and cleanup.
  - `docs-ghaw-dailyops.md` Claim 6 (`cache-memory: true` at
    `/tmp/gh-aw/cache-memory/`): both DataOps and DailyOps use `/tmp/gh-aw/`
    for data, but via different mechanisms. DataOps uses the GitHub Actions
    `cache:` directive (for step-extracted API data); DailyOps uses
    `cache-memory: true` (for agent-generated state). Together they establish
    the two-cache model for GHAW workflows.
  - `docs-ghaw-audit-with-agents.md` Claim 11 (weekly digest via GitHub
    Discussions): DataOps uses `safe-outputs: create-discussion` with
    `close-older-discussions: true` for weekly summaries. The audit digest
    uses the same pattern. Both confirm Discussions as the standard async
    team reporting channel for scheduled gh-aw workflows.

- **Extends**:
  - `docs-ghaw-audit-with-agents.md` — audit workflows follow the DataOps
    pattern (shell steps extract audit JSON → agent analyzes and posts a
    discussion) without naming it as such. DataOps is the named generalization
    of the pattern that audit workflows exemplify.
  - `docs-ghaw-dailyops.md` — DailyOps covers the scheduling, phased approval,
    and discussion-tracking patterns for scheduled improvement workflows.
    DataOps is the data-architecture complement: it describes how data flows
    from steps to the agent, which DailyOps workflows also implement but do
    not document as a named pattern.
  - `docs-ghaw-how-they-work.md` Claim 11 (development workflow: compile →
    watch → run → review): DataOps adds the data-preparation layer before
    `run` — steps must be validated for correctness before the agent can
    analyze anything. The `timeout-minutes: 10` on the compute step is a
    concrete example of step-level safeguards.

- **Contradicts**: None identified. The DataOps pattern is consistent with
  all existing source notes on gh-aw. The `/tmp/gh-aw/` path, `safe-outputs`,
  and GitHub CLI usage all align with prior corpus entries. The `cache:`
  directive (GitHub Actions cache) is distinct from but not contradictory
  to `cache-memory:` (GHAW agent state) — they are complementary mechanisms
  for different caching needs.

- **Novel**:
  - **DataOps as a named pattern** (Claim 1): No existing source note names
    or defines the "DataOps" pattern. Prior notes document the step/agent
    structure as part of specific workflows (audit, release), but this is the
    first explicit architectural naming and definition in the corpus.
  - **Pre-computing aggregations as a token-reduction technique** (Claim 2):
    While `docs-ghaw-how-they-work.md` implies the step/agent split, no
    existing note states explicitly that shell-side aggregation reduces agent
    token consumption. This is the first claim of that form.
  - **GitHub Actions `cache:` directive for DataOps** (Claim 4): The workflow-
    level data cache (distinct from `cache-memory:`) has not been documented
    in any existing source note. This is the first appearance of the `cache:`
    frontmatter block and the associated `restore-keys:` pattern.
  - **Multi-source `jq -s` aggregation pattern** (Claim 5): The `jq -s` named-
    key combine pattern for unified multi-source datasets is new to the corpus.
    Prior notes use `jq` for filtering and counting but not for multi-file
    dataset unification.
  - **Data-manifest agent prompt structure** (Claim 6): The practice of
    explicitly listing data file paths, record counts, and format descriptions
    in the agent prompt as a "data manifest" is stated as a best practice
    here for the first time in the corpus.
  - **`close-older-discussions: true` + `max: 1` as a "living report" pattern**
    (Claim 7): While `docs-ghaw-dailyops.md` documents discussion creation,
    the specific combination of `close-older-discussions: true` and `max: 1`
    for maintaining a single rolling report is new.
  - **Full jq statistical pipeline for PR data** (Claim 9): The complete `jq`
    pipeline (filtered counts, totals, unique counts, top-N ranking) is a
    directly reusable artifact not present in any existing source note.

## Guide Impact

- **Chapter 05 (agent orchestration / workflow patterns)**:
  - **Add DataOps as a named architectural pattern**: The guide should name
    and define the DataOps split — deterministic shell steps for data collection,
    agent for analysis. This is the concrete design pattern behind vague
    advice like "give the agent good context." The naming lets practitioners
    ask: "Is this a DataOps workflow? If so, what belongs in `steps:` and what
    belongs in the agent prompt?" Cite `docs-ghaw-how-they-work.md` Claim 2
    as the conceptual basis; cite this source for the concrete implementation.
  - **Add the five DataOps best practices**: "Keep steps deterministic /
    Pre-compute aggregations / Structure data clearly / Document data locations
    / Use safe outputs" — these are directly actionable design rules for any
    workflow that collects data before analysis, not just gh-aw workflows.

- **Chapter 06 (agentic pipeline design)**:
  - **Add the `jq -s` multi-source aggregation pattern**: When a workflow
    must analyze data from multiple GitHub API sources (PRs, issues, CI),
    aggregate them into a single structured object before the agent receives
    them. The `jq -s '{prs: .[0], issues: .[1], runs: .[2]}'` idiom is the
    concrete technique.
  - **Add the data-manifest agent prompt structure**: Agent prompts for
    DataOps workflows should include an explicit list of data files, their
    paths, and their formats. This is a context-engineering best practice
    that reduces agent hallucination about data structure.
  - **Add the two-cache model**: `cache:` (GitHub Actions cache) for step-
    extracted API data; `cache-memory:` for agent-generated state. Both
    serve different caching needs; neither substitutes for the other.
    Cross-reference `docs-ghaw-audit-with-agents.md` and
    `docs-ghaw-dailyops.md` for `cache-memory:` usage.

- **Chapter 04 (context engineering)**:
  - **Add pre-aggregation as a token-reduction technique** (Claim 2): In
    any pipeline that passes structured data to an LLM, pre-computing
    aggregations in a deterministic layer (shell, Python, jq) reduces
    token count and improves signal quality in the agent's context. The
    `jq` pipeline reducing 100 PR objects to a 9-field summary is the
    canonical example.

## Extraction Notes

1. **Source content extracted via WebFetch on the rendered Astro/Starlight
   page**: Full content including all YAML examples and prose was returned.
   The page structure matches the other gh-aw documentation pages in the
   corpus; no interactive content or diagrams were missed (the page is
   primarily textual with YAML code blocks).

2. **`strict: true` semantics not fully explained**: The Weekly PR Summary
   example uses `strict: true` in the frontmatter but the page does not
   define what this flag does. Marked as anecdotal; practitioners should
   refer to the gh-aw configuration reference for authoritative semantics.

3. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   gh-aw platform behavior as of the extraction date (May 2026).

4. **`cache:` vs `cache-memory:` distinction is implicit**: The page documents
   the `cache:` directive without explicitly distinguishing it from the GHAW-
   specific `cache-memory:` tool. This distinction was derived from cross-
   referencing with `docs-ghaw-audit-with-agents.md` and `docs-ghaw-dailyops.md`.

5. **No contradictions filed**: Reviewed all GHAW-related source notes and
   the broader corpus. No claims in this source materially oppose any existing
   source note. The DataOps pattern is a net-new named construct that extends
   and operationalizes patterns already implicit in the corpus.
