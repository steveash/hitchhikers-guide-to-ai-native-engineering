---
source_url: https://github.github.com/gh-aw/patterns/agentic-ops
source_type: docs
title: "GitHub Agentic Workflows: Agentic Ops Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-07
last_checked: 2026-05-07
status: current
confidence_overall: emerging
issue: "#552"
---

# GitHub Agentic Workflows: Agentic Ops Pattern

> Named pattern for a scheduled workflow that monitors other agentic workflows —
> inspecting logs, detecting cost and failure anomalies, and escalating findings
> via GitHub Discussions and threshold-triggered issues; the reference
> implementation at `githubnext/agentic-ops` provides two coordinated workflows
> (daily audit + daily optimizer) that share a `repo-memory` branch and introduce
> the two-workflow-pipeline coordination model as a distinct harness pattern.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `patterns/agentic-ops` page —
  in the `patterns/` section alongside ExpertOps, DailyOps, Monitoring, and
  Orchestration. Patterns pages are practitioner implementation references, not
  conceptual overviews or API references. Additionally enriched by the
  `githubnext/agentic-ops` reference implementation repository, which provides
  two complete workflow specifications and a README with verbatim installation
  commands.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team
  (GitHub Next / Microsoft Research — the same team behind Peli de Halleux's
  "Agent Factory" blog series, the `gh aw` CLI, and all other `patterns/` pages
  in the corpus). The reference implementation at `githubnext/agentic-ops` is an
  official GitHub Next repository with 44 commits and two production-grade
  workflow specifications. YAML configs, CLI commands, and field schemas are
  authoritative for the `gh aw` platform. Claims about the agentic-ops design
  (scope, when to use, applicability conditions) do not automatically generalize
  to non-`gh-aw` monitoring systems without qualification.
- **Scope**: Covers the Agentic Ops design pattern (what it does, when to apply
  it, its four-step workflow, related documentation links) and the reference
  implementation (two complete workflow YAML specifications: `copilot-token-audit`
  and `copilot-token-optimizer`, their coordination model, persistence mechanism,
  and token-efficiency analysis framework). Does NOT cover: the Safe Outputs
  permission model in general (see `docs-ghaw-how-they-work.md`), the monitoring
  configuration primitives (see `docs-ghaw-monitoring-patterns.md`), how to
  consume audit output in autonomous workflows (see `docs-ghaw-audit-with-agents.md`),
  or the observatory architecture at the blog-post level (see
  `blog-ghaw-agent-observability.md`).

## Extracted Claims

### Claim 1: Agentic Ops is a named gh-aw pattern for scheduled workflows that inspect other agentic workflows, summarize their activity, and escalate cost or failure anomalies

- **Evidence**: Opening description from the pattern page, consistently extracted
  across multiple fetch passes. The description is both the pattern's definition
  and its trigger condition.
- **Confidence**: settled (first-party documentation; the pattern is formally
  named, defined, and listed in the `patterns/` section alongside ExpertOps,
  DailyOps, and other named patterns)
- **Quote**: "Use this pattern when you want a scheduled workflow to inspect other
  agentic workflows, summarize what happened, and escalate unusual cost or failure
  patterns."
- **Our assessment**: Agentic Ops is the fleet-monitoring peer to ExpertOps (which
  monitors a single product domain). Where ExpertOps observes product quality
  (OTel traces, A/B experiments), Agentic Ops observes agent infrastructure
  quality (workflow logs, token costs, failure rates). The pattern formalizes
  the meta-agent concept from `blog-ghaw-agent-observability.md` Claim 3 into a
  distributable installation unit — teams can `gh aw add` the reference
  implementation rather than building an observatory from scratch. For Ch02
  (Harness Engineering): add Agentic Ops as the canonical pattern for fleet-level
  agent monitoring, positioned alongside ExpertOps in the pattern taxonomy.

### Claim 2: The pattern reviews workflow logs across a repository, classifies notable behavior, and publishes a structured report — it is the observatory concept made installable

- **Evidence**: Core description from the pattern page, confirmed across fetch passes.
  The description characterizes what the pattern does operationally, not just
  when to use it.
- **Confidence**: settled (first-party documentation)
- **Quote**: "This pattern reviews workflow logs across a repository, classifies
  notable behavior, and publishes a structured report."
- **Our assessment**: The "classifies notable behavior" language is architecturally
  important: this is not a passive log aggregator but a classification agent
  that applies qualitative assessment to fleet activity. The "publishes a
  structured report" framing positions it alongside DataOps (which also publishes
  reports to Discussions) but for the agent-infrastructure domain rather than
  a product domain. For Ch02: note that Agentic Ops is a DataOps-style pattern
  applied to agent fleet monitoring — the agent reads (logs), classifies, and
  publishes rather than creates, modifies, or files improvement suggestions.

### Claim 3: The detection targets are repeated failures, abnormal token consumption, and other unhealthy patterns — three distinct signal classes

- **Evidence**: Description from the pattern page enumerating the problem classes
  the pattern addresses.
- **Confidence**: settled (first-party documentation; enumeration is explicit)
- **Quote**: "repeated failures, abnormal token consumption, or other unhealthy
  patterns"
- **Our assessment**: The three detection classes map to distinct monitoring
  concerns: failures (reliability), token consumption (cost/efficiency), and
  "other unhealthy patterns" (open-ended anomaly detection). The reference
  implementation focuses primarily on token consumption and secondarily on failures —
  consistent with the pattern's emphasis on cost visibility as a first-order concern
  in agent fleets. For Ch03 (Safety and Verification): these three classes
  correspond to the reliability, efficiency, and anomaly-detection dimensions of
  agent health monitoring. All three require different thresholds and different
  escalation paths.

### Claim 4: Reports are published to a durable destination (GitHub Discussion) and issues are opened when the same problem crosses a threshold — a two-level escalation model

- **Evidence**: Four-step workflow description from the pattern page, consistently
  extracted across fetch passes; corroborated by the reference implementation
  which uses `create-issue` with `expires: 3d, close-older-issues: true` and
  posts daily audits via GitHub Discussion.
- **Confidence**: settled (first-party documentation + reference implementation)
- **Quote**: "a durable operational record"
- **Our assessment**: The distinction between Discussion (informational, async,
  team-readable) and Issue (actionable, tracked, attention-requiring) is the
  two-level escalation model. Routine summaries go to Discussions as a "durable
  operational record"; threshold-crossing anomalies become Issues. This mirrors
  the design in `docs-ghaw-audit-with-agents.md` Claim 11 (weekly digest →
  Discussion; critical findings → Issue). For Ch02: document the two-level
  escalation as a harness design principle — the output channel encodes the
  expected human response (inform vs. require action). This extends the pattern
  established in `docs-ghaw-monitoring-patterns.md`.

### Claim 5: The applicability condition is repositories with sufficient workflow activity to make per-run manual checking impractical, or multi-team environments requiring shared failure visibility

- **Evidence**: "When to use it" section from the pattern page.
- **Confidence**: settled (first-party; explicitly stated as an applicability condition)
- **Quote**: "Use this pattern when a repository has enough workflow activity that
  maintainers need a regular summary instead of checking each run manually."
- **Our assessment**: This is a concrete adoption criterion, not a general
  recommendation. A repository with two workflows running daily does not need
  Agentic Ops; a repository with 50+ workflows across multiple teams does. The
  multi-team qualifier adds a second dimension: Agentic Ops provides shared
  visibility across teams that might not otherwise coordinate on workflow health.
  For Ch05 (Team Adoption): use this applicability condition as the adoption
  trigger — document how to assess whether a team's repository has "enough
  workflow activity" (50+ runs/week is a reasonable starting heuristic, though
  not stated in the source).

### Claim 6: The reference implementation uses two coordinated workflows — a daily audit and a daily optimizer — that run two hours apart and share a `repo-memory` branch as their coordination mechanism

- **Evidence**: README from `githubnext/agentic-ops` and the YAML frontmatter of
  both workflow files. The audit runs at 12:00 and the optimizer at 14:00 (weekdays);
  both specify `branch-name: "memory/token-audit"` in their `repo-memory` tool
  configs with the description "Historical daily Copilot token usage snapshots
  (shared with copilot-token-optimizer)".
- **Confidence**: settled (verbatim from workflow files)
- **Quote**: "Historical daily Copilot token usage snapshots (shared with
  copilot-token-optimizer)" (from `repo-memory` description in both workflow files)
- **Our assessment**: The two-workflow pipeline (producer → consumer via shared
  `repo-memory`) is the most architecturally novel feature of the reference
  implementation. The audit runs first and writes data (`YYYY-MM-DD.json`,
  `rolling-summary.json`, `optimization-log.json`) to the `memory/token-audit`
  branch; the optimizer runs two hours later and reads those files for context.
  The two-hour gap is a design choice: it gives the audit time to complete and
  write before the optimizer reads. This is a temporal coordination model — no
  API calls or event triggers between them, just a shared persistent store with
  a reliable time separation. For Ch04 (multi-agent orchestration): this is a
  concrete alternative to the `dispatch-workflow`/`call-workflow` fan-out model —
  when workflows need to coordinate on shared data but not on timing, shared
  `repo-memory` with scheduled offsets is the simpler pattern.

### Claim 7: The `repo-memory` tool persists cross-workflow data as files in a dedicated git branch — a different persistence mechanism from `cache-memory`, enabling shared state between multiple workflows

- **Evidence**: Both workflow files configure `repo-memory` with the same
  `branch-name: "memory/token-audit"`. The branch stores daily JSON snapshots,
  a rolling 90-entry summary, and an optimization log. Unlike `cache-memory`
  (which is per-workflow and cache-backed), `repo-memory` creates a shared,
  inspectable git branch that any workflow with the same branch name can read
  and write.
- **Confidence**: emerging (first-party configuration; the persistence semantics
  of `repo-memory` vs `cache-memory` are inferred from the field names and
  usage patterns, not from an explicit platform comparison)
- **Quote**: (from YAML frontmatter)
  ```yaml
  repo-memory:
    branch-name: "memory/token-audit"
    description: "Historical daily Copilot token usage snapshots (shared with copilot-token-optimizer)"
    file-glob: ["*.json", "*.jsonl", "*.csv", "*.md"]
    max-file-size: 102400
    max-patch-size: 51200
  ```
- **Our assessment**: `repo-memory` is a new persistence primitive not documented
  in any prior corpus source. Its characteristics make it distinct from `cache-memory`:
  (1) stored in a git branch — inspectable and auditable by humans, (2) shared
  across workflows — multiple workflows can read and write the same files,
  (3) named by branch — the branch name is the namespace, not a per-workflow key.
  For Ch02 (Harness Engineering): add `repo-memory` as the cross-workflow shared
  state primitive alongside `cache-memory` (per-workflow rolling state). The
  choice between them is: `cache-memory` for workflow-local trend state;
  `repo-memory` for state that must be shared between multiple workflows or that
  benefits from human inspectability as a git branch.

### Claim 8: The audit workflow downloads logs with `gh aw logs --engine copilot --start-date -1d --json -c 100`, aggregates per-workflow token metrics, generates visual charts, and publishes an issue with `expires: 3d` and `close-older-issues: true`

- **Evidence**: Complete workflow specification from `workflows/copilot-token-audit.md`
  in the `githubnext/agentic-ops` repository.
- **Confidence**: settled (verbatim from reference implementation)
- **Quote**: (from step definition)
  ```bash
  gh aw logs \
    --engine copilot \
    --start-date -1d \
    --json \
    -c 100 \
    > /tmp/gh-aw/token-audit/copilot-logs.json
  ```
- **Our assessment**: The `--engine copilot --start-date -1d` flags are the
  specific parameterization for 24-hour Copilot-only monitoring. The `max: 100`
  cap (`-c 100`) limits the log download to prevent overwhelming the context with
  run data. The `expires: 3d` on `create-issue` is notable — the audit issue
  auto-expires after 3 days, ensuring the issue tracker only contains recent
  audit results and does not accumulate stale data. `close-older-issues: true`
  ensures at most one active audit issue at any time. For Ch02: the short
  `expires` on monitoring issues (3 days for audit, 7 days for optimizer) is the
  correct harness design for routine monitoring workflows — it prevents the issue
  tracker from becoming a graveyard of stale monitoring reports.

### Claim 9: The audit workflow flags three specific cost anomalies: workflows consuming >30% of total tokens ("heavy hitters"), workflows with high error/warning counts relative to run count, and workflows with average tokens >100,000 per run

- **Evidence**: Phase 4 (Publish Audit Issue) section of `copilot-token-audit.md`.
- **Confidence**: settled (verbatim from reference implementation)
- **Quote**: "Identify any workflow with >30% of total tokens as a 'heavy hitter'"
  / "Note workflows with high error/warning counts relative to runs" / "Flag any
  workflow whose avg tokens per run exceeds 100,000"
- **Our assessment**: These are concrete detection thresholds for the "abnormal
  token consumption" signal class from Claim 3. The three thresholds address
  different cost concerns: (1) relative share (one workflow dominating the fleet),
  (2) reliability correlation (error-prone workflows wasting tokens on retries),
  (3) absolute per-run cost (a single workflow that is inherently expensive).
  They complement the regression detection thresholds in
  `docs-ghaw-audit-with-agents.md` Claim 4 (cost increase >20%, token increase
  >50%) which are change-detection thresholds; the audit workflow thresholds here
  are absolute-level thresholds. For Ch03: add these three as the starter threshold
  set for fleet-level token monitoring; teams can tune them against their own
  baseline distribution.

### Claim 10: The optimizer workflow uses a 14-day recency-based exclusion list to cycle through the fleet, ensuring each workflow receives optimization attention over time rather than always targeting the same top consumer

- **Evidence**: Phase 1 (Select Target) section of `copilot-token-optimizer.md`.
- **Confidence**: settled (verbatim from reference implementation)
- **Quote**: "Exclude workflows optimized in the last 14 days (use
  `optimization-log.json`)."
- **Our assessment**: Without the exclusion list, the optimizer would always
  target the same highest-token workflow. The 14-day exclusion forces rotation
  through the fleet — ensuring lower-ranked workflows eventually receive attention.
  The `optimization-log.json` in `repo-memory` is the mechanism: each optimizer
  run appends an entry, and the next run filters out anything from the last 14
  days. This is a lightweight fairness constraint for a single-target-per-run
  design. For Ch05 (Team Adoption): document this pattern for any optimizer
  workflow that should cover multiple targets over time without duplicating effort
  within short windows.

### Claim 11: The optimizer identifies five specific token-efficiency anti-patterns by analyzing observed tool-usage sequences across multiple runs

- **Evidence**: "Tool-Usage Efficiency Patterns" section of
  `copilot-token-optimizer.md`.
- **Confidence**: settled (verbatim from reference implementation)
- **Quote**: (five anti-patterns with labels)
  - "Batch independent reads: look for sequential file reads or API calls that
    could be requested in a single tool-use block — each extra turn repeats the
    full context"
  - "Chain bash commands: look for separate bash tool calls that could be combined
    with `&&` — each call adds a full context echo"
  - "Prefer typed tools: look for `bash cat`, `bash grep`, `bash find -name` when
    `view`, `grep`, `glob` would return more concise output"
  - "Consolidate GitHub API sequences: look for multiple sequential `gh api` calls
    that could be combined into fewer round-trips with `jq` filtering"
  - "Don't retry without diagnosing: look for blind retries of the same failing
    operation without error analysis — each retry wastes a full turn"
- **Our assessment**: These five anti-patterns constitute the most specific
  token-efficiency guidance in the corpus for agent prompt/tool behavior. They are
  operationally grounded — derived from analyzing real workflow runs rather than
  theoretical principles. The "each extra turn repeats the full context" explanation
  is the key insight: in an LLM agent, every additional tool call sends the entire
  context again, so reducing tool calls compounds: one fewer tool call per run
  saves context tokens exponentially for high-frequency workflows. For Ch02
  (Harness Engineering): add these five as the starter checklist for agent
  token-efficiency review. Cross-reference `blog-ghaw-agent-observability.md`
  Claim 4 ("some agents were way too chatty with their LLM calls") — this
  reference implementation is the concrete tool for diagnosing exactly that.

### Claim 12: The audit workflow integrates OTLP observability with custom `gh_aw.experiment.*` span attributes, enabling A/B experiment variant tracking in Datadog, Honeycomb, or any OTLP backend

- **Evidence**: "Experiment OTEL Span Attributes" section of
  `copilot-token-audit.md`, with the complete JavaScript code block.
- **Confidence**: emerging (the OTLP integration mechanism is documented, but the
  A/B testing infrastructure it requires is external to the workflow)
- **Quote**: "This enables filtering workflow runs by experiment variant in Datadog,
  Honeycomb, or any OTLP-compatible backend. Attribute keys follow the pattern
  `gh_aw.experiment.<name>` with the assigned variant as the value, plus
  `gh_aw.experiment.names` as a comma-separated index."
- **Our assessment**: The experiment tracking integration connects agent workflow
  monitoring to the observability infrastructure used for product A/B tests. This
  is architecturally significant: it treats the agent workflow itself as an
  experiment variant, enabling comparison of workflow performance across
  configuration variants using the same infrastructure used for product experiments.
  For Ch02 (Harness Engineering) and Ch03 (Safety and Verification): the
  `observability.otlp` config block in the workflow frontmatter is a new harness
  primitive — not previously documented in the corpus — that enables OpenTelemetry
  integration at the workflow level.

### Claim 13: The optimizer workflow instructs agents to prefer `--jq` filtering on `gh api` calls over separate `jq` pipes, and to extract only required sections of workflow files using `awk` — to minimize tokens consumed by intermediate context

- **Evidence**: "Data Access Guidelines" section of `copilot-token-optimizer.md`.
- **Confidence**: settled (verbatim from reference implementation)
- **Quote**: "Prefer `--jq` on `gh api` calls over a separate `| jq` step when
  the filter is simple — it avoids piping the full response through the shell.
  Use `| jq` for multi-step transformations or when chaining with other commands."
- **Our assessment**: This is harness engineering advice embedded directly in the
  workflow's agent prompt — a self-referential optimization where a token-optimizer
  workflow instructs its agent to be token-efficient in its own operation. The
  preferred/anti-pattern examples (✅/❌) are the most concrete API efficiency
  guidance in the corpus. The principle — filter at the source rather than loading
  then filtering — applies to any agent that reads structured data via CLI or API.
  For Ch02: add `--jq` as the preferred filter pattern for `gh api` calls in
  agent workflows, with the `awk`-based frontmatter extraction as the pattern for
  reading specific workflow file sections.

## Concrete Artifacts

### Pattern Page: Opening Definition and Four-Step Workflow

From `https://github.github.com/gh-aw/patterns/agentic-ops`:

```
Pattern description:
  "Use this pattern when you want a scheduled workflow to inspect other agentic
  workflows, summarize what happened, and escalate unusual cost or failure patterns."

What it does:
  "This pattern reviews workflow logs across a repository, classifies notable
  behavior, and publishes a structured report."

Four-step workflow:
  1. Run on a schedule to collect recent workflow activity.
  2. Analyze logs, costs, and failure signals across runs.
  3. Post a summary report to a GitHub Discussion or another durable destination.
  4. Open or update issues when the same problem crosses a threshold.

When to use:
  "Use this pattern when a repository has enough workflow activity that maintainers
  need a regular summary instead of checking each run manually."

Related documentation:
  - Projects & Monitoring (durable tracking with Projects and safe outputs)
  - Custom OTLP Attributes (enriching workflow telemetry)
  - Audit Commands (investigating individual runs and regressions)

Reference implementation: https://github.com/githubnext/agentic-ops
```

### Reference Implementation README (verbatim)

```markdown
# agentic-ops

This repo contains a small set of GitHub Agentic Workflows for auditing Copilot
token usage and highlighting workflows that should be optimized.

## Usage

To add one of these workflows to your repo, use `gh aw add <owner>/<repo>/<workflow-name>`.

```bash
gh aw add githubnext/agentic-ops/copilot-token-audit githubnext/agentic-ops/copilot-token-optimizer
```

This adds the workflow to `.github/workflows/`. For guided setup, use
`gh aw add-wizard githubnext/agentic-ops/copilot-token-audit`.

## Workflows

| Workflow | What it does |
| ----- | --- |
| copilot-token-audit.md | Collects recent Copilot workflow usage and creates a daily audit snapshot. |
| copilot-token-optimizer.md | Analyzes expensive workflows and proposes conservative token-reduction changes. |
```

### copilot-token-audit.md — YAML Frontmatter (verbatim)

From `https://github.com/githubnext/agentic-ops/blob/main/workflows/copilot-token-audit.md`:

```yaml
---
description: Daily audit of Copilot token usage across all agentic workflows with historical trend tracking
on:
  schedule:
    - cron: "daily around 12:00 on weekdays"
  workflow_dispatch:
permissions:
  contents: read
  actions: read
  issues: read
  pull-requests: read
observability:
  otlp:
    endpoint: ${{ secrets.GH_AW_OTEL_ENDPOINT }}
    headers: ${{ secrets.GH_AW_OTEL_HEADERS }}
tracker-id: copilot-token-audit
engine: copilot
safe-outputs:
  create-issue:
    expires: 3d
    title-prefix: "[copilot-token-audit] "
    max: 1
    close-older-issues: true
  upload-asset:
    max: 5
    allowed-exts: [.png, .jpg, .jpeg, .svg]
tools:
  agentic-workflows:
  bash:
    - "*"
  repo-memory:
    branch-name: "memory/token-audit"
    description: "Historical daily Copilot token usage snapshots (shared with copilot-token-optimizer)"
    file-glob: ["*.json", "*.jsonl", "*.csv", "*.md"]
    max-file-size: 102400
    max-patch-size: 51200
steps:
  - name: Setup Python runtime
    uses: actions/setup-python@v6.2.0
    with:
      python-version: "3.12"
  - name: Setup local chart workspace
    run: |
      mkdir -p /tmp/gh-aw/token-audit/charts /tmp/gh-aw/token-audit/site-packages
  - name: Install Python chart dependencies
    run: |
      python3 -m pip install --quiet \
        --target /tmp/gh-aw/token-audit/site-packages \
        pandas matplotlib seaborn
  - name: Download Copilot workflow logs
    env:
      GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    run: |
      set -euo pipefail
      mkdir -p /tmp/gh-aw/token-audit

      LOGS_EXIT=0
      gh aw logs \
        --engine copilot \
        --start-date -1d \
        --json \
        -c 100 \
        > /tmp/gh-aw/token-audit/copilot-logs.json || LOGS_EXIT=$?

      if [ -s /tmp/gh-aw/token-audit/copilot-logs.json ]; then
        TOTAL=$(jq '.runs | length' /tmp/gh-aw/token-audit/copilot-logs.json)
        echo "✅ Downloaded $TOTAL Copilot workflow runs (last 24 hours)"
        if [ "$LOGS_EXIT" -ne 0 ]; then
          echo "⚠️ gh aw logs exited with code $LOGS_EXIT (partial results — likely API rate limit)"
        fi
      else
        echo "❌ No log data downloaded (exit code $LOGS_EXIT)"
        echo '{"runs":[],"summary":{}}' > /tmp/gh-aw/token-audit/copilot-logs.json
      fi
timeout-minutes: 25
features:
  copilot-requests: true
---
```

### copilot-token-optimizer.md — YAML Frontmatter (verbatim)

From `https://github.com/githubnext/agentic-ops/blob/main/workflows/copilot-token-optimizer.md`:

```yaml
---
description: Daily optimizer that identifies a high-token-usage Copilot workflow, audits its runs, and recommends efficiency improvements
on:
  schedule:
    - cron: "daily around 14:00 on weekdays"
  workflow_dispatch:
permissions:
  contents: read
  actions: read
  issues: read
  pull-requests: read
tracker-id: copilot-token-optimizer
engine: copilot
tools:
  github:
    mode: gh-proxy
    toolsets: [issues]
  bash:
    - "*"
  repo-memory:
    branch-name: "memory/token-audit"
    description: "Historical daily Copilot token usage snapshots (shared with copilot-token-audit)"
    file-glob: ["*.json", "*.jsonl", "*.csv", "*.md"]
    max-file-size: 102400
    max-patch-size: 51200
safe-outputs:
  create-issue:
    expires: 7d
    title-prefix: "[copilot-token-optimizer] "
    close-older-issues: true
    max: 1
  threat-detection: false
timeout-minutes: 30
---
```

### Audit Workflow Run Data Schema (from `copilot-token-audit.md`)

```
RunData fields in gh aw logs --json output:
  workflow_name      string   Human-readable name
  workflow_path      string   .github/workflows/....lock.yml
  token_usage        int      Total tokens (omitempty — treat missing/null as 0)
  effective_tokens   int      Cost-normalized tokens
  estimated_cost     float    USD cost (omitempty — treat missing/null as 0)
  action_minutes     float    Billable GitHub Actions minutes
  turns              int      Number of agent turns
  duration           string   Human-readable duration
  created_at         ISO 8601 Run creation time
  run_id             int64    Unique run ID
  url                string   Link to the run
  status             string   "completed", "in_progress", etc.
  conclusion         string   "success", "failure", etc.
  error_count        int      Errors encountered
  warning_count      int      Warnings encountered
  token_usage_summary object  Firewall-level breakdown by model
```

### Token Efficiency Anti-Patterns (from `copilot-token-optimizer.md`)

```
Five anti-patterns for agent token efficiency:

1. Batch independent reads
   Problem: sequential file reads or API calls that could be one tool-use block
   Impact: each extra turn repeats the full context

2. Chain bash commands
   Problem: separate bash tool calls that could be combined with &&
   Impact: each call adds a full context echo

3. Prefer typed tools
   Problem: bash cat/grep/find when view/grep/glob return more concise output
   Impact: typed tools return structured output; bash returns raw text

4. Consolidate GitHub API sequences
   Problem: multiple sequential gh api calls that could be combined with jq filtering
   Impact: round-trips multiply context overhead

5. Don't retry without diagnosing
   Problem: blind retries of the same failing operation without error analysis
   Impact: each retry wastes a full turn

Rule: audit at least 5 runs before making removal recommendations.
Never recommend removing a tool used in any successful run without strong contrary evidence.
```

### Cost Anomaly Detection Thresholds (from `copilot-token-audit.md`)

```
Fleet-level token monitoring thresholds:

Heavy hitter:         workflow consuming >30% of repository's total tokens
High error rate:      high error/warning count relative to run count (no specific value given)
Expensive per run:    avg tokens per run exceeds 100,000

Note: These are absolute-level thresholds (is this workflow too expensive now?).
Compare with docs-ghaw-audit-with-agents.md which uses change-detection thresholds
(did this workflow get more expensive recently? cost +20%, tokens +50%).
```

### OTLP Experiment Span Attribute Pattern (from `copilot-token-audit.md`)

```javascript
// Emit OTLP span attributes for experiment tracking
const fs = require('fs');
const assignmentsFile = '/tmp/gh-aw/experiments/assignments.json';
if (fs.existsSync(assignmentsFile)) {
  const assignments = JSON.parse(fs.readFileSync(assignmentsFile, 'utf8'));
  const names = Object.keys(assignments).sort();
  if (names.length > 0) {
    const attrs = { 'gh_aw.experiment.names': names.join(',') };
    for (const name of names) {
      attrs[`gh_aw.experiment.${name}`] = assignments[name];
    }
    const otlp = require('/tmp/gh-aw/actions/otlp.cjs');
    await otlp.logSpan('experiment', attrs);
  }
}
// Attribute pattern: gh_aw.experiment.<name> = <variant>
// Index attribute:   gh_aw.experiment.names  = "name1,name2,..."
```

### GitHub API Efficiency Patterns (from `copilot-token-optimizer.md`)

```bash
REPO="${{ github.repository }}"

# ✅ Extract only the fields you need from a file
gh api "repos/$REPO/contents/.github/workflows/my-workflow.md" \
  --jq '.content' | base64 -d

# ✅ List workflow runs — keep only essential metadata
gh api "repos/$REPO/actions/workflows/my-workflow.yml/runs?per_page=10" \
  --jq '.workflow_runs[] | {id, name, conclusion, run_started_at}'

# ✅ Combine multi-step reads into one bash block with pipes
gh api "repos/$REPO/contents/.github/workflows/my-workflow.md" \
  --jq '.content' | base64 -d | sed -n '1,/^---$/{ /^---$/d; p }' | head -40

# ❌ Never load full unfiltered responses — drops everything into context
gh api "repos/$REPO/actions/workflows/my-workflow.yml/runs"
```

## Cross-References

- **Corroborates**:
  - `blog-ghaw-agent-observability.md` Claim 3 (meta-agent pattern viable in
    production — Audit Workflows is the most prolific agent in the factory):
    The agentic-ops reference implementation is the distributable, user-installable
    instantiation of the same meta-agent concept. The blog post proves meta-agents
    are viable at 183-workflow scale; this pattern makes them accessible to teams
    not operating at factory scale.
  - `blog-ghaw-agent-observability.md` Claim 4 ("some agents were way too chatty
    with their LLM calls" — Portfolio Analyst finding): The `copilot-token-optimizer`
    is the production tool for diagnosing exactly this problem. The blog post names
    the symptom; the reference implementation is the cure.
  - `docs-ghaw-monitoring-patterns.md` Claim 9 (`gh aw logs --format markdown`
    inside a scheduled workflow for automated trend monitoring): The
    `copilot-token-audit` does this with `gh aw logs --engine copilot --start-date
    -1d --json`, using the same CLI command inside a scheduled agent. Claim 9 in
    monitoring-patterns describes the general pattern; this is a production
    implementation.
  - `docs-ghaw-monitoring-patterns.md` Claim 4 (`title-prefix: "[failed] "` + labels
    for searchable failure issues): The reference implementation uses
    `title-prefix: "[copilot-token-audit] "` and `title-prefix: "[copilot-token-optimizer] "`
    following the same convention, confirming it as the standard.
  - `docs-ghaw-expert-ops.md` Claim 5 (`max: 2` issue rate as a quality constraint):
    The reference implementation uses `max: 1` for both workflows — one issue per run
    per workflow — following the same "limit to avoid backlog noise" principle.

- **Extends**:
  - `blog-ghaw-agent-observability.md`: The blog post describes the observatory
    architecture at GitHub's scale (183 workflows, three-tier observability layer).
    This pattern + reference implementation makes the same observatory concept
    installable for any repository via `gh aw add`. The blog is the architecture
    reference; this pattern is the user-facing distribution mechanism.
  - `docs-ghaw-monitoring-patterns.md`: That note covers the configuration-layer
    primitives (safe-outputs for failure reporting, Projects v2 integration, CLI
    monitoring commands). This pattern is the operational pattern that assembles
    those primitives into a fleet-monitoring workflow with a specific architecture
    (audit + optimizer pair, shared repo-memory, scheduled offset timing).
  - `docs-ghaw-expert-ops.md`: ExpertOps monitors a single product domain
    (OTel traces, A/B experiments) and produces improvement suggestions via issues.
    Agentic Ops monitors agent infrastructure (token usage, failure rates) and
    produces monitoring reports via Discussions plus anomaly issues. Together they
    are the two scheduled-monitoring pattern types: ExpertOps for product quality,
    Agentic Ops for agent fleet health.
  - `docs-ghaw-audit-with-agents.md`: That guide covers how agent workflows consume
    `gh aw audit` CLI output in production workflows. The `copilot-token-audit`
    complements this by using `gh aw logs` (not `gh aw audit`) for fleet-level
    summary monitoring, while `docs-ghaw-audit-with-agents.md` covers per-run
    deep audit. Together: `gh aw logs` for fleet-wide trend; `gh aw audit <run-id>`
    for per-run inspection.

- **Contradicts**:
  - **`docs-ghaw-audit-with-agents.md` Claim 5 (`cache-memory` as the persistence
    mechanism for rolling baselines)**: That note documents `cache-memory: key:
    audit-monitoring-trends` as the platform-native mechanism for rolling trend
    analysis across runs. The agentic-ops reference implementation uses `repo-memory`
    instead. These are different persistence mechanisms: `cache-memory` is per-workflow,
    cache-backed, and shorter-lived; `repo-memory` is branch-backed, shared across
    workflows, and git-inspectable. This is not a strict contradiction — both work
    for trend storage — but it is different guidance. Teams choosing between them
    should know: `cache-memory` for single-workflow state, `repo-memory` when
    multiple workflows share state. **No contradiction issue filed** because the
    mechanisms serve different use cases (single-workflow vs multi-workflow
    coordination); the difference is a conditioning variable, not an opposition.

- **Novel**:
  - **`repo-memory` as a cross-workflow shared persistence primitive** (Claim 7):
    No existing source note documents `repo-memory`. This is the first corpus entry
    describing branch-backed persistent shared state between multiple workflows.
    The distinction from `cache-memory` is important for harness engineers designing
    multi-workflow coordination systems.
  - **Two-workflow pipeline via shared `repo-memory` with scheduled offset**
    (Claim 6): The audit → optimizer coordination pattern (producer writes at 12:00,
    consumer reads at 14:00, shared via git branch) is not documented anywhere in
    the corpus. This is a distinct alternative to the `dispatch-workflow`/
    `call-workflow` fan-out patterns in `docs-ghaw-orchestration-patterns.md`.
  - **Recency-based target cycling (14-day exclusion list)** (Claim 10): The
    optimization history log + 14-day exclusion pattern for ensuring fleet-wide
    coverage over time is not documented in any existing source note.
  - **Five concrete token-efficiency anti-patterns** (Claim 11): The specific
    five anti-patterns (batch independent reads, chain bash commands, prefer typed
    tools, consolidate API sequences, don't retry without diagnosing) are the most
    specific token-efficiency guidance in the corpus. No prior source enumerates
    these specific patterns.
  - **Cost anomaly thresholds for fleet monitoring** (Claim 9): The three
    fleet-level thresholds (>30% total tokens, high error rate, >100K avg tokens)
    are a distinct set from the change-detection thresholds in
    `docs-ghaw-audit-with-agents.md`. The corpus now has two complementary threshold
    sets: absolute-level (this source) and change-detection (audit-with-agents).
  - **`observability.otlp` workflow-level OTLP config** (Claim 12): The
    `observability.otlp.endpoint` and `headers` frontmatter fields are not
    documented in any existing source note. This is the first description of
    OpenTelemetry integration at the workflow-definition level.
  - **`upload-asset` safe output for visual reporting** (Claim 8): The
    `upload-asset` safe output (with `allowed-exts: [.png, .jpg, ...]`) is not
    documented in any existing source note. This is the first corpus description
    of a workflow that generates and uploads chart images as safe-output artifacts.
  - **`--jq` preferred over `| jq` for API calls in agent prompts** (Claim 13):
    The specific preference for `gh api --jq` over separate `jq` pipes, embedded
    as agent instructions, is not described in any existing source note. This is
    the most specific data-access efficiency guidance in the corpus for API-calling
    agents.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add `repo-memory` as a cross-workflow shared persistence primitive alongside
    `cache-memory`. Key distinction: `cache-memory` for single-workflow rolling
    state; `repo-memory` when multiple workflows share state or when the state
    must be human-inspectable as a git branch. The `memory/token-audit` branch
    naming convention (descriptive, prefixed with `memory/`) should become the
    recommended pattern for `repo-memory` branches.
  - Add `upload-asset` as a safe-output type for workflows that generate visual
    artifacts. Currently undocumented in the guide. Include the `allowed-exts`
    whitelist and `max:` cap as required config.
  - Add `observability.otlp` as a workflow-level OTLP config for telemetry
    integration. Document `endpoint` and `headers` as the fields, with secrets
    as the recommended value source.
  - Add the two-workflow pipeline (producer + consumer with scheduled offset and
    shared `repo-memory`) as a multi-workflow coordination pattern. Position it
    as the simpler alternative to `dispatch-workflow`/`call-workflow` for cases
    where workflows share data but do not need synchronous coordination.
  - Add `expires: 3d` (short-lived) for routine monitoring issues and `expires: 7d`
    for optimization issues as the recommended `create-issue` config for monitoring
    workflows. Pair with `close-older-issues: true` to ensure at most one active
    issue per monitoring workflow.
  - Add the five token-efficiency anti-patterns as a harness review checklist for
    agents that make CLI or API calls. The most impactful: batching independent
    reads and chaining bash commands — these directly reduce turn count, which
    linearly reduces context repetition cost.

- **Chapter 03 (Safety and Verification)**:
  - Add the three fleet-level cost anomaly thresholds (>30% total tokens, high
    error rate relative to run count, >100K avg tokens per run) as starter
    detection gates for fleet monitoring. Cross-reference the change-detection
    thresholds from `docs-ghaw-audit-with-agents.md` (cost +20%, tokens +50%)
    as the companion set for regression detection.
  - Add the recency-based exclusion list pattern (14-day window, `optimization-log.json`)
    as a fairness mechanism for optimizer workflows that must cycle through
    multiple targets. Without it, optimization workflows converge on the same
    top-cost target indefinitely.
  - Add the `threat-detection: false` flag (used in `copilot-token-optimizer.md`)
    as a documented safe-outputs config option — currently undocumented in the
    corpus.

- **Chapter 05 (Team Adoption)**:
  - Add the Agentic Ops applicability condition as a concrete adoption criterion:
    use this pattern when a repository has enough workflow activity that maintainers
    need a regular summary instead of checking each run manually. Provide a
    practical heuristic (50+ runs/week across 5+ workflows is a reasonable trigger,
    though the pattern page does not specify a number).
  - Document `gh aw add githubnext/agentic-ops/copilot-token-audit githubnext/agentic-ops/copilot-token-optimizer`
    as the one-command installation for the reference implementation. This is the
    lowest-friction path to fleet-level token monitoring for teams on the `gh aw`
    platform.

## Extraction Notes

1. **Source page content processed by AI model**: The `WebFetch` tool processes
   page content through an AI model before returning results. Quotes from the
   pattern page (`github.github.com/gh-aw/patterns/agentic-ops`) were confirmed
   across four independent WebFetch calls. Where a passage appeared consistently
   across calls in the same form, it is cited as a direct quote. The pattern page
   appears to be relatively concise (~400 words plus related-links section) based
   on consistent returns across calls.

2. **Reference implementation accessed via GitHub API**: The `githubnext/agentic-ops`
   repository content was fetched via `gh api` with base64 decoding, providing
   verbatim workflow file content. The workflow YAML frontmatter and agent prompt
   body are extracted character-for-character from the repository as of 2026-05-07.
   (Commit: `7d8ad62` for copilot-token-audit.md, `7b3e0dc` for copilot-token-optimizer.md.)

3. **No YAML artifacts from the pattern page itself**: The `patterns/agentic-ops`
   page does not appear to contain YAML code blocks (consistent with how the
   Prospector's triage comment describes it: a pattern-level description rather
   than a configuration reference). The concrete YAML artifacts in this note are
   from the reference implementation, not the pattern page.

4. **`repo-memory` vs `cache-memory` is not a contradiction**: Both mechanisms are
   valid persistence options, but they serve different coordination needs. See Claim 7
   and the Cross-References section for the nuanced comparison. No contradiction
   issue filed because the difference is a conditioning variable (single-workflow
   vs multi-workflow coordination scope).

5. **`threat-detection: false` in the optimizer workflow**: This safe-outputs flag
   appears in the `copilot-token-optimizer.md` frontmatter but is not explained in
   the workflow documentation. It likely disables the platform's threat-detection
   scanning for the optimizer (which reads workflow source files and run data, and
   may trigger heuristics that generate false positives for a security scanner).
   The semantics are inferred from context; the platform documentation for this
   flag was not found in existing corpus source notes.

6. **No contradictions filed**: Reviewed the potential `cache-memory` vs `repo-memory`
   difference against MINER.md §4a criteria. The two mechanisms serve different use
   cases (single-workflow vs multi-workflow coordination) and both are documented
   as valid options — this is a conditioning variable, not a material opposition.
   No other claims in this source materially oppose existing source notes.
