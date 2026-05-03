---
source_url: https://github.github.com/gh-aw/patterns/expert-ops
source_type: docs
title: "GitHub Agentic Workflows: ExpertOps Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-03
last_checked: 2026-05-03
status: current
confidence_overall: emerging
issue: "#499"
---

# GitHub Agentic Workflows: ExpertOps Pattern

> The canonical reference for the ExpertOps pattern — a scheduled, single-domain
> focused agent that reads live runtime data, checks its own previously filed issues
> before proposing new ones, and caps output at two issues per run to preserve
> gradual improvement without creating backlog noise.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, "Patterns"
  section, "ExpertOps" page — prescriptive pattern reference, not API reference
  or conceptual overview)
- **Author credibility**: First-party from the GitHub Agentic Workflows team
  (GitHub Next / Microsoft Research — the same team behind Peli de Halleux's
  "Agent Factory" blog series and the `gh aw` platform). Claims about workflow
  configuration, safe-outputs, and the pattern design are authoritative for
  the `gh aw` platform. The "depth over breadth" design principle and the issue
  feedback loop are architectural opinions from practitioners with 183+
  production workflows.
- **Scope**: Covers the ExpertOps design pattern: single-domain focus as a
  first-class design constraint, live-data observation before suggesting
  improvements, self-deduplication via `gh issue list` before each run,
  `safe-outputs: create-issue: max: 2` as a noise-prevention mechanism,
  `cache-memory` for accumulating domain observations, `network: allowed:`
  for domain-specific backend access, and two complete YAML reference
  implementations (OpenTelemetry expert and A/B testing expert). Does NOT
  cover: the broader Safe Outputs permission model (see
  `docs-ghaw-how-they-work.md`), the DailyOps scheduling pattern for
  general improvement workflows (see `docs-ghaw-dailyops.md`), or the
  IssueOps pattern for event-triggered issue handling (see
  `docs-ghaw-issueops.md`).

## Extracted Claims

### Claim 1: ExpertOps is a scheduled workflow pattern that deploys a focused domain expert — scoped to a single concern like OTel instrumentation or A/B testing coverage — to continuously file targeted improvement suggestions

- **Evidence**: Opening definition from the documentation. Two concrete
  examples provided: an OpenTelemetry expert and an A/B Testing expert, each
  with complete YAML specifications. Both run on a schedule (daily/weekly),
  connect to a domain-specific backend, and file suggestions as GitHub issues.
- **Confidence**: settled (first-party documentation; the pattern is named,
  defined, and illustrated with two complete workflow specs)
- **Quote**: "ExpertOps uses a scheduled workflow as a focused domain expert — for example, an OpenTelemetry expert or an A/B testing expert — to continuously examine a product and file targeted improvement suggestions as GitHub issues."
- **Our assessment**: ExpertOps is architecturally distinct from DailyOps
  (`docs-ghaw-dailyops.md` Claim 1) which handles general incremental
  improvement across many concerns. ExpertOps narrows the scope to one domain
  and deepens the observation quality by connecting to live runtime data.
  The "continuously examine" framing signals that ExpertOps is expected to
  run indefinitely, not just until a backlog is cleared. For Ch01 (Daily
  Workflows): ExpertOps is the "specialist" complement to DailyOps's
  "generalist" model — useful when a domain (security, observability,
  experimentation) benefits from sustained focused attention beyond what a
  general improvement workflow provides.

### Claim 2: ExpertOps deliberately trades breadth for depth — covering a single, well-defined concern and ignoring everything else — as a first-class architectural design choice

- **Evidence**: Stated explicitly as the core operational principle in the
  documentation. Both reference implementations (OTel expert and A/B testing
  expert) exemplify this: each workflow is scoped to exactly one concern
  and uses domain-specific labels to keep its output separated from other
  workflows' output.
- **Confidence**: settled (first-party; stated as a defining design principle;
  both examples embody it)
- **Quote**: "An ExpertOps workflow covers a single, well-defined concern and ignores everything else. Breadth is traded for depth."
- **Our assessment**: The "breadth is traded for depth" principle distinguishes
  ExpertOps from omnibus improvement agents. An omnibus agent that handles
  security, performance, documentation, and observability in one workflow
  produces shallow suggestions in each domain. An ExpertOps agent that reads
  only OTel traces and knows only the instrumentation improvement space can
  develop more nuanced domain knowledge across runs via `cache-memory`. For
  Ch05/Ch06 (Agent Autonomy): this is a concrete design rule for scoping
  autonomous improvement agents — one domain per workflow, not many domains
  in one workflow. The `cache-memory` mechanism (Claim 6) is what makes
  sustained domain depth possible.

### Claim 3: ExpertOps reads live state from its domain before proposing changes — the agent sees current runtime behavior, not just static code

- **Evidence**: Design principle stated explicitly. The OTel expert fetches
  traces from a live backend via `curl -s "https://otel.example.internal/api/traces?lookback=24h"`.
  The A/B testing expert fetches current experiment state from
  `https://experiments.example.internal/api/experiments`. The agent prompt
  instructs the agent to review the fetched data before filing issues.
- **Confidence**: settled (first-party; stated as a design principle and
  demonstrated in both YAML examples with concrete backend curl commands)
- **Quote**: "Static analysis catches obvious problems; live data reveals runtime surprises. The quality of ExpertOps suggestions is directly proportional to the richness of the observation step."
- **Our assessment**: This is the key differentiator between ExpertOps and
  a code-analysis DailyOps workflow. A static analysis agent reads source
  code; an ExpertOps agent reads what the code is doing at runtime. For OTel:
  missing spans only appear in traces, not in instrumentation code. For A/B
  testing: experiments running too long only appear in experiment metadata,
  not in feature flag code. Static analysis is necessary but insufficient for
  operational quality suggestions. For Ch08 (Observability): this principle
  extends to any improvement loop that targets runtime behavior — the agent's
  suggestions are only as good as the runtime signal it observes. Compare
  with `docs-ghaw-monitoring-patterns.md` Claim 7 which documents `gh aw audit`
  for the same "read before acting" pattern at the workflow-operations level.

### Claim 4: Before filing new issues, the ExpertOps agent reads its own previously filed issues to avoid duplicates and observe whether earlier suggestions were acted upon

- **Evidence**: Stated explicitly in the documentation as a key operational
  behavior. Both YAML examples implement this: the `steps:` block runs
  `gh issue list --label <domain-label> --state open --json number,title`
  and saves to `/tmp/gh-aw/open-issues.json` before the agent prompt. The
  agent prompt instructs the agent to "Check open issues at
  `/tmp/gh-aw/open-issues.json` to avoid duplicates."
- **Confidence**: settled (first-party; stated as a design behavior and
  implemented consistently in both YAML examples)
- **Quote**: "It also reads its own previously filed issues to avoid duplicates and observe whether earlier suggestions have been acted upon."
- **Our assessment**: This self-deduplication loop closes an important gap
  in scheduled improvement agents: without it, the same insight would be
  filed as a new issue on every run. With it, the agent knows what it has
  already suggested and can skip those, focus on what remains unaddressed,
  and observe which suggestions were merged or resolved. This is a concrete
  feedback signal about the team's responsiveness without requiring any
  special integration — the standard `gh issue list` command is sufficient.
  For Ch05/Ch06 (Agent Autonomy and Feedback Loops): this is the simplest
  implementation of a feedback loop for a scheduled improvement agent — no
  metrics API, no custom state store, just reading the issue list before
  each run. For Ch02: the `gh issue list --label <domain-label>` step is
  boilerplate that every ExpertOps workflow should include.

### Claim 5: Filing one or two issues per run is a principled design constraint — large batches create backlog noise and eliminate the gradual-improvement benefit

- **Evidence**: Stated as an explicit design constraint with reasoning. Both
  YAML examples enforce this mechanically via `safe-outputs: create-issue: max: 2`.
- **Confidence**: settled (first-party; stated as a design constraint with
  explicit rationale; mechanically enforced in both examples)
- **Quote**: "File one or two issues per run. If the expert creates ten issues at once, the team loses the gradual improvement benefit and the backlog becomes noise."
- **Our assessment**: The `max: 2` constraint is both a quality signal
  (if the agent can't prioritize to one or two issues, its suggestions are
  likely poorly discriminated) and a UX constraint (a team facing 10 new
  issues per day from a single workflow will disable or ignore it). The
  "gradual improvement benefit" framing echoes `docs-ghaw-dailyops.md`
  Claim 1's "compound over time" rationale: the value of ExpertOps is in
  sustained attention, not in flooding the backlog once. For Ch02 (Harness
  Engineering): `max: 2` is the recommended default for ExpertOps
  `create-issue` safe outputs. Document it as a quality constraint, not
  just a rate limit — teams that increase it are likely solving the wrong
  problem (agent scope is too broad, not max is too low).

### Claim 6: `cache-memory: true` enables ExpertOps agents to accumulate domain observations across runs, load history at the start of each run, and append new findings to persist them

- **Evidence**: The page documents `cache-memory: true` under `tools:` for
  ExpertOps. The agent prompt pattern instructs: "Load your observation history
  from `/tmp/gh-aw/cache-memory/` if it exists. After filing issues, append a
  brief summary of today's findings to the history."
- **Confidence**: settled (first-party; consistent with `docs-ghaw-dailyops.md`
  Claim 6 and `docs-ghaw-audit-with-agents.md` which document the same
  `cache-memory` mechanism at the same path)
- **Quote**: "Load your observation history from `/tmp/gh-aw/cache-memory/` if it exists. After filing issues, append a brief summary of today's findings to the history."
- **Our assessment**: `cache-memory` is what makes ExpertOps's "depth over
  breadth" principle operational over time. Without it, the agent starts
  fresh each run and cannot refine its domain model or track trends across
  runs. With it, the agent can observe: "I've seen this OTel cardinality
  pattern three times in the last week — it's a systemic issue, not a one-
  time anomaly." This cross-run knowledge accumulation is qualitatively
  different from what a stateless scheduled agent can produce. For Ch02
  (Harness Engineering): `cache-memory: true` should be the default for
  ExpertOps workflows, not an optional add-on. A stateless ExpertOps agent
  cannot develop the domain depth the pattern is designed for.

### Claim 7: `network: allowed:` must explicitly list domain-specific backend endpoints alongside `defaults` and `github` to enable live data access

- **Evidence**: Both YAML examples include a `network: allowed:` block with
  the domain-specific endpoint added alongside platform defaults. The OTel
  expert lists `otel.example.internal`; the A/B testing expert lists
  `experiments.example.internal`. Without these entries, the `curl` step
  in the `steps:` block would be blocked by the network firewall.
- **Confidence**: settled (first-party; demonstrated in both YAML examples;
  consistent with the gh-aw network configuration model documented in other
  notes)
- **Quote**: (no direct prose quote; evidence is in the YAML examples — see
  Concrete Artifacts)
- **Our assessment**: This is an important harness configuration detail for
  ExpertOps: the live-data-before-suggesting pattern (Claim 3) only works
  if the backend endpoint is in the network allowlist. Teams that copy the
  ExpertOps pattern but omit their internal backend from `network: allowed:`
  will get a silent failure (the curl step returns empty data) rather than
  a visible error. For Ch02: ExpertOps harness templates should include a
  note that `network: allowed:` must be updated with domain-specific backends
  before the workflow is deployed. Compare with `docs-ghaw-dataops.md`
  Claim 10 where `GH_TOKEN` is required for the `gh` CLI — both are
  boilerplate configuration requirements that are easy to miss.

### Claim 8: The ExpertOps improvement feedback loop closes when the agent tracks whether its earlier suggestions were acted upon before proposing the next one

- **Evidence**: Stated as a design behavior and goal. The agent reading
  previously filed issues (Claim 4) not only prevents duplicates but also
  reveals whether older suggestions are still open (not yet acted on) or
  closed (resolved). The documentation states this creates an improvement
  feedback loop that helps the expert refine its heuristics over time.
- **Confidence**: emerging (first-party; stated as a design behavior; the
  "refine its heuristics" outcome depends on the agent interpreting issue
  state as a signal, which requires prompt engineering beyond the basic
  pattern)
- **Quote**: "Track impact...This creates an improvement feedback loop and helps the expert refine its heuristics over time."
- **Our assessment**: The feedback loop is more subtle than it first appears.
  When the agent sees that an issue it filed three weeks ago is still open,
  it can infer the team has not prioritized that domain. When it sees many
  of its suggestions closed quickly, it can infer the suggestions are well-
  targeted. This is lightweight ML without any ML — the agent is using the
  issue tracker state as a reward signal for its own suggestions. For Ch05
  (Agent Autonomy): this is a concrete implementation of "learning from
  outcome" without requiring any special feedback infrastructure — the
  standard GitHub issue lifecycle is the feedback channel. For Ch08
  (Continuous Improvement): document ExpertOps as the pattern for "agents
  that get better over time through issue-state observation."

### Claim 9: ExpertOps uses domain-specific labels on both the `gh issue list` query and the `create-issue` safe output to keep domain-expert issues organized and filterable

- **Evidence**: Both YAML examples use a domain-specific label: the OTel
  expert uses `otel-expert`; the A/B testing expert uses `ab-expert`. These
  labels appear in both the `safe-outputs: create-issue: labels:` field and
  in the `gh issue list --label <domain-label>` query in the step. The
  title-prefix (`[otel]`, `[ab]`) provides a second filtering axis.
- **Confidence**: settled (first-party; implemented in both examples; consistent
  with `docs-ghaw-monitoring-patterns.md` Claim 4's `[failed]` label pattern)
- **Quote**: (no direct prose quote; evidence is in both YAML examples — see
  Concrete Artifacts)
- **Our assessment**: The domain-specific label is the mechanism that makes the
  self-deduplication loop (Claim 4) work: the `gh issue list --label
  <domain-label>` query returns only *this expert's* previously filed issues,
  not all open issues in the repository. Without domain-specific labels, an
  OTel expert would need to filter all open issues by title prefix or author,
  which is less reliable. The `title-prefix:` in `create-issue` provides
  visual grouping in the issue list; the `labels:` provides queryable
  filtering. Both are needed for a well-organized ExpertOps deployment.
  For Ch02: recommend using both `title-prefix:` and `labels:` for ExpertOps
  safe-output configs; the label is the filter key for the self-deduplication
  step.

### Claim 10: ExpertOps is positioned in the GHAW pattern taxonomy as complementing DailyOps, DataOps, IssueOps, and Monitoring — it produces issues rather than consuming them

- **Evidence**: "Related Patterns" section on the page lists: DailyOps,
  DataOps, IssueOps, Monitoring as the related pattern family. ExpertOps
  produces GitHub issues as output (it is a producer); IssueOps reacts to
  incoming issues (it is a consumer). ExpertOps uses the DataOps
  deterministic-then-agentic split (shell step fetches data, agent analyzes).
  ExpertOps is a specialized DailyOps variant focused on a single domain.
- **Confidence**: settled (first-party; "Related Patterns" section explicitly
  names the four patterns)
- **Quote**: (no direct prose quote — the "Related Patterns" section lists the
  four patterns without a single summary sentence)
- **Our assessment**: The pattern taxonomy position is important for harness
  engineers designing agent factories. ExpertOps fills a specific niche:
  scheduled, proactive, single-domain, improvement-suggestion agent. It is
  distinguishable from: DailyOps (multi-concern general improvement),
  DataOps (reporting/analytics without improvement suggestions), IssueOps
  (event-triggered response to existing issues), and Monitoring (observing
  workflow health rather than product quality). For Ch09 (Agent Orchestration):
  when designing an agent factory, ExpertOps workflows should be created per
  domain rather than combined — one for OTel, one for A/B testing, one for
  security — each with its own label namespace and feedback loop.

## Concrete Artifacts

### OpenTelemetry Expert — Complete YAML Specification

```yaml
---
name: OpenTelemetry Expert

on:
  schedule: daily
  workflow_dispatch:

engine: copilot
strict: true

network:
  allowed:
    - defaults
    - github
    - otel.example.internal

safe-outputs:
  create-issue:
    title-prefix: "[otel] "
    labels: [otel-expert]
    max: 2

tools:
  bash: ["*"]

steps:
  - name: Fetch traces and open issues
    env:
      GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    run: |
      curl -s "https://otel.example.internal/api/traces?lookback=24h" \
        > /tmp/gh-aw/traces.json
      gh issue list --label otel-expert --state open --json number,title \
        > /tmp/gh-aw/open-issues.json
---

# OpenTelemetry Expert

Review the trace sample at `/tmp/gh-aw/traces.json` for instrumentation gaps
(missing spans, wrong cardinality, absent error attributes). Check open issues
at `/tmp/gh-aw/open-issues.json` to avoid duplicates. File one concise issue.
```

*Source: gh-aw ExpertOps patterns documentation, "OpenTelemetry Expert" example*

### A/B Testing Expert — Complete YAML Specification

```yaml
---
name: A/B Testing Expert

on:
  schedule: weekly
  workflow_dispatch:

engine: copilot
strict: true

network:
  allowed:
    - defaults
    - github
    - experiments.example.internal

safe-outputs:
  create-issue:
    title-prefix: "[ab] "
    labels: [ab-expert]
    max: 2

tools:
  bash: ["*"]

steps:
  - name: Fetch experiments and open issues
    env:
      GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    run: |
      curl -s "https://experiments.example.internal/api/experiments" \
        > /tmp/gh-aw/experiments.json
      gh issue list --label ab-expert --state open --json number,title \
        > /tmp/gh-aw/open-issues.json
---

# A/B Testing Expert

Review experiment coverage at `/tmp/gh-aw/experiments.json` (features shipped
without tests, experiments running too long, missing success metrics). Check
`/tmp/gh-aw/open-issues.json` to avoid duplicates. File one focused issue.
```

*Source: gh-aw ExpertOps patterns documentation, "A/B Testing Expert" example*

### Cache-Memory Pattern for Observation History

```yaml
# In the workflow frontmatter:
tools:
  cache-memory: true
```

```
# In the agent prompt (natural language body):
Load your observation history from `/tmp/gh-aw/cache-memory/` if it exists.
After filing issues, append a brief summary of today's findings to the history.
```

*Source: gh-aw ExpertOps patterns documentation, "Persistent Memory" section*

### ExpertOps Boilerplate Step Pattern

```bash
# Step: fetch live domain data + open issues for deduplication
# Add to the `steps:` block of every ExpertOps workflow
GH_TOKEN=${{ secrets.GITHUB_TOKEN }}

curl -s "https://<your-domain-backend>/api/<endpoint>" \
  > /tmp/gh-aw/<domain>-data.json

gh issue list \
  --label <domain-label> \
  --state open \
  --json number,title \
  > /tmp/gh-aw/open-issues.json
```

*Source: gh-aw ExpertOps patterns documentation, generalized from both examples*

### ExpertOps Pattern Summary (from documentation taxonomy)

```
ExpertOps:
  Trigger:        Scheduled (daily/weekly) + workflow_dispatch for manual testing
  Focus:          Single domain (OTel, A/B testing, security, etc.)
  Live data:      curl to domain backend → /tmp/gh-aw/<domain>-data.json
  Deduplication:  gh issue list --label <domain> → /tmp/gh-aw/open-issues.json
  Output:         create-issue with domain-specific title-prefix + labels + max: 2
  State:          cache-memory for observation history accumulation
  Network:        defaults + github + domain-specific backend endpoint

Related Patterns:
  DailyOps     — general scheduled improvement (broader scope)
  DataOps      — deterministic data collection + agentic analysis (structural basis)
  IssueOps     — event-triggered response to issues (consumer; ExpertOps is producer)
  Monitoring   — workflow health observation (input to ExpertOps, not output)
```

*Source: gh-aw ExpertOps patterns documentation, pattern description and "Related Patterns" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-dailyops.md` Claim 1 ("compound over time" framing for scheduled
    improvement automation): ExpertOps is the domain-specialist instantiation of
    the same principle. Both patterns rely on small, sustained improvements
    rather than large-batch automation. The "gradual improvement benefit" language
    in ExpertOps (Claim 5) directly echoes the DailyOps framing.
  - `docs-ghaw-dailyops.md` Claim 6 (`cache-memory: true` at
    `/tmp/gh-aw/cache-memory/` for cross-run state): ExpertOps uses the same
    `cache-memory` mechanism and path. This is the third corpus source
    confirming `cache-memory` as the standard cross-run state primitive for
    scheduled gh-aw workflows (after DailyOps and audit workflows).
  - `docs-ghaw-dataops.md` Claim 1 (deterministic data collection in `steps:`,
    agentic analysis in the agent prompt): ExpertOps follows the identical
    architectural split. The `curl` and `gh issue list` commands in ExpertOps
    `steps:` are the deterministic data-collection phase; the agent prompt is
    the agentic analysis phase. ExpertOps adds the self-deduplication feedback
    loop and the improvement-suggestion output on top of this structural basis.
  - `docs-ghaw-dataops.md` Claim 3 (`/tmp/gh-aw/` as the standard ephemeral
    data handoff location): Both ExpertOps examples use `/tmp/gh-aw/` for the
    step-to-agent data handoff (traces, experiments, open issues). This is
    consistent with all other gh-aw DataOps and DailyOps notes.
  - `docs-ghaw-monitoring-patterns.md` Claim 4 (domain-specific labels on
    failure issues for filterability): ExpertOps uses the same labeling
    discipline for its improvement suggestions — `otel-expert`, `ab-expert`
    — enabling label-filtered queries for deduplication and triage.

- **Extends**:
  - `docs-ghaw-dailyops.md`: DailyOps covers the general scheduled improvement
    pattern with a three-phase approach and multiple concerns per workflow.
    ExpertOps specializes this pattern by adding: (a) single-domain focus as
    a design constraint, (b) live runtime data as the observation source, (c)
    self-deduplication via issue list reading, and (d) the improvement feedback
    loop via issue-state observation. ExpertOps is to DailyOps what a specialist
    consultant is to a generalist engineer.
  - `docs-ghaw-dataops.md`: DataOps documents the deterministic-then-agentic
    architectural split for data analysis and reporting workflows. ExpertOps
    applies this split to a different output type (improvement suggestions as
    GitHub issues rather than reports as Discussions). ExpertOps also adds the
    self-deduplication step (`gh issue list`) as a required data-fetch step
    alongside the domain-data fetch.
  - `docs-ghaw-issueops.md` Claim 7 (sub-issues for task decomposition): ExpertOps
    produces the issues that IssueOps might subsequently react to. The two
    patterns are complementary in a full agent factory: ExpertOps files domain
    improvement suggestions; IssueOps might decompose high-priority ones into
    implementation sub-tasks. Neither pattern is aware of the other — they
    interact through the shared GitHub issue tracker state.

- **Contradicts**: None identified. The ExpertOps pattern is fully consistent
  with all existing source notes. Its use of `cache-memory`, `/tmp/gh-aw/`
  data handoffs, `safe-outputs: create-issue`, and `network: allowed:` is
  consistent with the corpus. No contradiction issue filed.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **Single-domain focus as a named design constraint** (Claim 2): No existing
    source note names "breadth is traded for depth" as a design principle for
    scheduled improvement agents. DailyOps covers general improvement;
    ExpertOps introduces the specialist model. This distinction is new to the
    corpus.
  - **Live-data-before-suggesting pattern** (Claim 3): While DataOps documents
    live data collection for analytics/reporting, no existing note documents
    live data as the *input quality differentiator* for improvement suggestions.
    "Static analysis catches obvious problems; live data reveals runtime
    surprises" is a new claim form in the corpus.
  - **Self-deduplication via `gh issue list` before each run** (Claim 4): The
    feedback loop where the agent reads its own previously filed open issues
    before proposing new ones is not documented in any existing source note.
    This is a practical technique for avoiding duplicate suggestions without
    any custom infrastructure.
  - **`max: 2` as a quality-not-rate-limit constraint** (Claim 5): Prior notes
    document `max:` as a volume-control mechanism. This source introduces the
    framing that a small `max:` is a *quality signal* — the agent should be
    discriminating enough to prioritize to 1-2 suggestions, not just technically
    limited from filing more.
  - **ExpertOps improvement feedback loop via issue-state observation** (Claim 8):
    The pattern of observing whether previously filed issues were acted on as
    a feedback signal — without any custom metrics or ML — is not documented
    in any existing source note. This is a novel lightweight feedback mechanism.
  - **Two complete YAML reference implementations with domain-specific network
    allowlist** (Claims 7, 9): The complete OTel and A/B testing expert YAML
    specs (including `network: allowed:` with domain-specific backends) are
    concrete harness templates not present in any existing source note.

## Guide Impact

### Chapter 01: Daily Workflows

- **Add ExpertOps as the "specialist" complement to DailyOps** (Claim 1):
  When a domain (observability, experimentation, security, accessibility) needs
  sustained focused attention beyond what a general improvement workflow provides,
  ExpertOps is the pattern. The recommendation: start with DailyOps for broad
  improvement; graduate domains that generate the most value into dedicated
  ExpertOps workflows. Cite the "breadth is traded for depth" principle (Claim 2)
  as the design rationale.

- **Add the live-data observation principle** (Claim 3): Scheduled improvement
  agents whose suggestions touch runtime behavior (not just code structure) should
  connect to live backend data. Static analysis has a ceiling; live data reveals
  what static analysis misses. This extends the DailyOps discussion in Ch01
  from code-quality improvement to operational quality improvement.

### Chapter 02: Harness Engineering

- **Add ExpertOps `steps:` boilerplate** (Claims 3, 4, 7): Every ExpertOps
  workflow needs two deterministic steps before the agent: (1) fetch live domain
  data from the backend, (2) fetch currently open domain-labeled issues for
  deduplication. The YAML examples provide the canonical template. Also requires
  `network: allowed:` to include the domain-specific backend endpoint.

- **Add `max: 2` as the ExpertOps issue-rate design constraint** (Claim 5):
  Distinguish this from `max:` as a safety rate limit in other safe outputs.
  For ExpertOps, `max: 2` is a quality gate — the agent should be discriminating
  enough to prioritize to the one or two most important suggestions.

- **Add `cache-memory: true` as the ExpertOps memory default** (Claim 6):
  A stateless ExpertOps agent produces shallow suggestions; a stateful one
  accumulates domain knowledge. `cache-memory: true` should be in every
  ExpertOps workflow frontmatter. Add the "load history at start, append at
  end" prompt pattern as the standard cache-memory usage template for ExpertOps.

- **Add domain-specific label pair** (Claim 9): ExpertOps workflows must use
  domain-specific labels on both `create-issue` output and `gh issue list`
  deduplication query. Without matching labels, the self-deduplication loop
  breaks.

### Chapter 05/06: Agent Autonomy and Feedback Loops

- **Add ExpertOps as the canonical pattern for lightweight agent feedback
  loops** (Claims 4, 8): The combination of reading previously filed issues
  + observing which were acted on is the simplest feedback mechanism in the
  corpus — no custom infrastructure, no metrics API, just `gh issue list`.
  This should be the first feedback mechanism teams implement when deploying
  scheduled improvement agents.

- **Add the "domain depth via cache-memory" pattern** (Claim 6): ExpertOps
  demonstrates how an agent can develop domain expertise over multiple runs
  by appending observations to `cache-memory`. This is a concrete implementation
  of the agent-memory concept that Ch05/Ch06 should document.

### Chapter 08/09: Observability and Agent Orchestration

- **Add ExpertOps taxonomy position** (Claim 10): When designing an agent
  factory, ExpertOps workflows should be created per domain rather than
  combined. The pattern produces issues for each domain; the issue tracker
  serves as the coordination surface between ExpertOps (producer) and the
  engineering team (consumer). For large agent factories, ExpertOps workflows
  should be deployed as a fleet: one per active domain, each with its own
  label namespace, feedback loop, and `cache-memory` state.

## Extraction Notes

1. **Source rendered via Astro/Starlight static HTML**: Page content was fully
   extractable via WebFetch. Two WebFetch calls were made: the first with a broad
   prompt for all major content, the second specifically requesting YAML examples
   and verbatim text. Both returned consistent results. The YAML specifications
   for the OTel and A/B testing experts appear complete in the second fetch.

2. **WebFetch uses an AI model to process page content**: All quotes in this note
   were cross-checked for consistency between the two fetch passes. Where a quote
   appeared in both passes in identical or near-identical form, it is presented as
   a direct quote. Where text appeared in only one pass, it is marked appropriately.
   Practitioners verifying specific wording should check the source URL directly.

3. **Cache-memory agent prompt pattern**: The "Load your observation history..."
   instruction was extracted from the second WebFetch pass. This appears in the
   agent prompt body (the natural language portion after the YAML frontmatter),
   not in the YAML frontmatter itself. The exact formatting of this section was
   not fully captured; the quoted text is from the model's output, presented
   as the documented pattern.

4. **No publication date**: The documentation page does not carry an explicit
   publication date. Content is consistent with gh-aw platform behavior as of
   the extraction date (May 2026).

5. **No contradictions filed**: Reviewed all existing gh-aw source notes
   (`docs-ghaw-dailyops.md`, `docs-ghaw-dataops.md`, `docs-ghaw-issueops.md`,
   `docs-ghaw-monitoring-patterns.md`, and others). No claims in this source
   materially oppose existing source notes at the MINER.md §4a filing threshold.
   The ExpertOps pattern extends and specializes existing patterns without
   contradicting them.

6. **`cache-memory` configuration in YAML vs. prose**: The `tools: cache-memory: true`
   configuration block appears consistent with `docs-ghaw-dailyops.md` Claim 6's
   documentation of the same mechanism. The complete YAML frontmatter for ExpertOps
   examples did not explicitly include `cache-memory: true` in the extracted YAML
   specs — the cache-memory section appears to be described separately in the
   documentation as an enhancement pattern rather than included in the base YAML
   examples. The configuration syntax is confirmed by cross-reference with
   `docs-ghaw-dailyops.md`.
