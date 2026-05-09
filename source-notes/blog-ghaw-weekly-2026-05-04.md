---
source_url: https://github.github.com/gh-aw/blog/2026-05-04-weekly-update/
source_type: blog-post
title: "Weekly Update – May 4, 2026 (GitHub Agentic Workflows)"
author: GitHub Agentic Workflows team (gh-aw)
date_published: 2026-05-04
date_extracted: 2026-05-09
last_checked: 2026-05-09
status: current
confidence_overall: emerging
issue: "#530"
---

# Weekly Update – May 4, 2026 (GitHub Agentic Workflows)

> Release v0.71.3 (April 30, 2026) delivers three architectural advances not
> present in prior weekly notes: (1) parameterized safe-outputs that let
> `workflow_call` callers configure threat-detection, booleans, and PR policy
> without forking; (2) a full A/B experiments framework with a hidden `experiments`
> CLI command and statistical significance analysis; and (3) the `ab-testing-advisor`
> meta-workflow — an agent that proposes experiment campaigns for other agents,
> consuming ~500k tokens per run.

## Source Context

- **Type**: blog-post (weekly changelog/release update from the GitHub Agentic
  Workflows blog; covers v0.71.3 released April 30, 2026, and associated notable
  PRs merged beyond the release; includes an "Agent of the Week" spotlight on the
  `ab-testing-advisor` meta-workflow)
- **Author credibility**: The gh-aw blog is the official publication of GitHub's
  Agentic Workflows platform team (Don Syme, Peli de Halleux, Mara Kiefer — see
  `blog-gh-aw-operations-release-workflows.md` for author background). Release
  notes cite specific PR numbers throughout. High credibility for claims about
  their own platform.
- **Scope**: Covers v0.71.3 and notable merged PRs. This release is three versions
  ahead of the last extracted weekly note (April 13: v0.68.1). Does NOT cover:
  intermediate releases v0.69.x–v0.71.2 (gap of approximately three versions);
  the full `experiments` CLI command vocabulary beyond what the changelog describes;
  the precise schema for parameterized safe-outputs fields; or per-run cost data
  beyond the ab-testing-advisor token estimate.

## Extracted Claims

### Claim 1: `workflow_call` inputs can now control safe-outputs configuration — threat-detection, boolean flags, PR policy fields, and list constraints — enabling reusable workflows that callers configure without forking

- **Evidence**: PR #29171, shipped in v0.71.3. The post enumerates four categories
  of configuration now exposed through `workflow_call` inputs: threat-detection,
  boolean flags, PR policy fields, and list constraints. The motivation is explicit:
  "callers can configure without forking."
- **Confidence**: emerging (feature shipped with specific PR number; the full
  parameter schema and which safe-outputs fields are addressable from `workflow_call`
  inputs are not enumerated in the changelog)
- **Quote**: "The workflow_call inputs can now control safe-outputs.threat-detection,
  boolean flags, PR policy fields, and list constraints. This enables reusable
  workflows that callers can configure without forking."
- **Our assessment**: This is the most practically significant change in the release
  for teams that share agentic workflows across repos. Previously, any team that
  needed custom safe-outputs behavior had to fork the workflow — a maintenance
  burden that fragments the corpus of shared workflows and makes security patches
  difficult to propagate. Parameterized safe-outputs decouple the *workflow logic*
  (shared) from the *safe-outputs policy* (caller-specific). For Ch02 (Harness
  Engineering): reusable workflow design should treat safe-outputs as a parameterized
  policy layer, not a hardcoded definition. Document the `workflow_call` input
  pattern alongside the existing safe-outputs guidance.

### Claim 2: `engine.mcp.session-timeout` frontmatter field lets operators control MCP gateway session lifetime, preventing premature session drops during long-running deep analysis workflows

- **Evidence**: Described in the v0.71.3 release notes. The feature is framed as
  solving a specific operational problem: premature timeouts during "deep analysis
  workflows."
- **Confidence**: emerging (feature described in changelog; the default timeout
  value and what constitutes a "long-running" session are not specified)
- **Quote**: "Users can set `engine.mcp.session-timeout` in workflow frontmatter to
  maintain long-running MCP sessions. This prevents premature timeouts during deep
  analysis workflows."
- **Our assessment**: MCP sessions have a lifecycle tied to the agentic workflow
  run. Without a configurable timeout, sessions that run longer than the default
  (presumably minutes) drop and require reconnection — potentially losing accumulated
  tool context. For deep analysis workflows (e.g., `ab-testing-advisor` analyzing
  a workflow corpus at ~500k tokens), the session timeout is a hard operational
  ceiling. For Ch02: workflows that involve multi-step deep analysis should
  explicitly configure `engine.mcp.session-timeout`; the default is likely tuned
  for interactive workflows, not extended analysis runs.

### Claim 3: Workflows without explicit safe-output configuration now automatically receive a `create_issue` safe output, reducing harness boilerplate for common agentic patterns

- **Evidence**: Described in the v0.71.3 release notes. The post frames this as
  "reducing boilerplate for common workflows."
- **Confidence**: emerging (feature shipped; what other default safe outputs exist
  alongside `create_issue`, and whether the auto-inject can be suppressed, are
  not specified)
- **Quote**: "Workflows without explicit safe-output configuration now automatically
  receive a `create_issue` safe output, reducing boilerplate for common workflows."
- **Our assessment**: Many agentic workflows need to surface findings as GitHub
  issues — this is close to a universal pattern. Auto-injecting `create_issue`
  as a default safe output means new workflows work for the common case without
  any explicit configuration. The risk is that teams relying on safe-outputs for
  security containment (restricting what outputs are allowed) may not realize
  `create_issue` is now implicitly present. For Ch02: document the auto-inject
  behavior alongside explicit safe-outputs configuration so teams know the default
  surface before adding restrictions. For Ch03: teams with strict safe-outputs
  policies should audit whether the auto-injected `create_issue` is appropriate
  for their threat model.

### Claim 4: A/B experiments framework adds a hidden `experiments` CLI command that reads experiment state from storage-repo branches for controlled testing of workflow behavior changes across runs

- **Evidence**: PR #30020. The post describes `experiments` as a "hidden" CLI
  command — likely behind a flag or not yet in stable CLI help output. Experiment
  state is stored in storage-repo branches, consistent with the gh-aw model of
  using git branches as typed storage (see `blog-ghaw-weekly-2026-03-30.md`
  Claim 1 on integrity-aware cache storage).
- **Confidence**: emerging (feature shipped with specific PR; "hidden" status
  suggests experimental or early-access; the full CLI vocabulary is not described)
- **Quote**: "A hidden `experiments` CLI command reads experiment state from storage
  repo branches for controlled A/B testing."
- **Our assessment**: This is the first documented infrastructure primitive for
  systematic A/B testing of agentic workflow behavior in the corpus. Prior workflow
  optimization relied on ad hoc comparison or the meta-monitoring patterns in
  `blog-ghaw-agent-observability.md`. The `experiments` framework gives teams a
  structured path to: (a) define variants (prompt changes, parameter changes),
  (b) distribute runs across variants, and (c) read accumulated results from
  storage branches for analysis. The storage-branch model for experiment state
  is elegant: it leverages the existing gh-aw storage infrastructure without
  requiring a new backend. For Ch02 (Harness Engineering): document `experiments`
  as a first-class harness control for teams doing systematic workflow optimization.
  For Ch05 (Team Adoption): this is the infrastructure that makes hypothesis-driven
  workflow improvement tractable at scale.

### Claim 5: `experiments analyze` computes statistical significance to determine whether observed differences between workflow variants represent real prompt-change improvements

- **Evidence**: PR #30029. The post names the specific command (`experiments analyze`)
  and its purpose: determining "whether prompt changes improved results."
- **Confidence**: emerging (feature shipped; what statistical test is used, what
  the significance threshold is, and what "results" means — token usage, success
  rate, output quality score — are not specified)
- **Quote**: "The `experiments analyze` command computes statistical significance
  to determine whether prompt changes improved results."
- **Our assessment**: Statistical significance testing closes the most important
  gap in the A/B framework: distinguishing real improvement from noise. Without
  significance analysis, teams running small experiments might optimize on
  variance rather than signal. The existence of `experiments analyze` implies
  that experiment runs produce a quantifiable outcome metric. For Ch05: the
  `experiments analyze` command makes hypothesis-driven workflow optimization
  a quantitative discipline rather than an impressionistic one — teams should
  run experiments to completion before concluding a prompt change is better.

### Claim 6: The `ab-testing-advisor` meta-workflow identifies workflows lacking experiment infrastructure, then proposes detailed A/B test campaigns via GitHub issues, consuming ~500k tokens per run

- **Evidence**: "Agent of the Week" spotlight. The post describes the
  `ab-testing-advisor` as executing three times per week, each run consuming
  approximately 500,000 tokens. On May 2nd it generated two concrete issues:
  a prompt_style A/B test proposal for `daily-news` (#29660) and an experiment
  infrastructure improvement suggestion (#29661).
- **Confidence**: anecdotal (one agent, one week's operational data; token estimate
  is approximate; quality of proposed campaigns is not evaluated)
- **Quote**: "This meta-workflow identifies workflows lacking experiment infrastructure
  and proposes A/B testing campaigns through detailed GitHub issues. The
  `ab-testing-advisor` executed three times this week, consuming approximately
  500,000 tokens per run while analyzing workflow files and developing experiment
  specifications."
- **Our assessment**: The `ab-testing-advisor` is the clearest "agents improving
  agents" example in the corpus. Its operational pattern is: (1) enumerate all
  workflows in the repo, (2) classify each by whether it has experiment infrastructure,
  (3) for those without, generate a detailed A/B test proposal. The 500k token
  cost reflects the deep analysis required: each proposal involves reading the
  workflow file, understanding its intent, and designing a meaningful experiment.
  Compare this to the `agentic-observability-kit` in `blog-ghaw-weekly-2026-04-06.md`
  Claim 9, which hit token-limit errors at similar scale — the `ab-testing-advisor`
  appears to budget for this upfront. For Ch04 (Multi-agent orchestration): the
  meta-workflow pattern (agents that analyze and improve other agents) requires
  explicit token budgeting; 500k per run is a significant per-run cost that should
  be scheduled rather than triggered on every event. For Ch05: `ab-testing-advisor`
  is a concrete example of how teams can build continuous improvement infrastructure
  for their agentic systems without manual review of each workflow.

### Claim 7: The Codex engine now ships a default `codex_harness.cjs` file with built-in retry logic, reducing per-workflow boilerplate in harness definitions

- **Evidence**: PR #30035. The post describes the default harness as including
  "built-in retry logic for increased resilience."
- **Confidence**: emerging (feature shipped; what retry strategy is implemented —
  fixed backoff, exponential, max retries — is not specified)
- **Quote**: "The Codex engine includes a default `codex_harness.cjs` with built-in
  retry logic for increased resilience."
- **Our assessment**: Previously, Codex harness resilience required either custom
  `codex_harness.cjs` definitions with hand-rolled retry logic or accepting
  no-retry behavior. A default with retry logic changes the baseline: new Codex
  workflows are resilient by default, not by explicit configuration. For Ch02:
  update harness configuration guidance to note that the Codex engine's default
  harness now handles transient failures without custom retry code — operators
  only need to override if they want different retry semantics.

### Claim 8: The gh-aw compiler pre-flight detects single-quoted bash commands that crash the Copilot CLI, sanitizing them before the workflow reaches runtime

- **Evidence**: PR #30040. The compiler "catches and sanitizes single-quoted bash
  tool commands before reaching the Copilot CLI, preventing runtime crashes."
- **Confidence**: emerging (feature shipped; the mechanism — whether single-quoted
  commands are rejected, rewritten, or escaped — is described as "sanitization"
  without specifying the transformation)
- **Quote**: "The compiler catches and sanitizes single-quoted bash tool commands
  before reaching the Copilot CLI, preventing runtime crashes."
- **Our assessment**: This extends the compile-time safety story from the April 13
  note (`blog-ghaw-weekly-2026-04-13.md` Claim 4, `ValidateHeredocContent`) to
  a new crash class: single-quoted bash commands. Where the heredoc validation
  caught injection-site vulnerabilities, this catches a syntax incompatibility
  between the gh-aw command representation and Copilot CLI's command parser.
  The pattern is the same: use the compiler as a safety net that prevents a
  class of runtime failures from ever reaching the engine. For Ch02: the gh-aw
  compile step is load-bearing for safety — workflows should always run
  `gh aw compile` before deployment, not just before the initial push.
  For Ch03: document single-quoted bash commands as a known incompatibility
  class in Copilot CLI workflows.

### Claim 9: The OTLP `endpoint` field is now polymorphic, supporting multiple backends simultaneously and enabling multi-backend telemetry from a single workflow

- **Evidence**: PR #30021. The post states the `endpoint` field "supports multiple
  backends simultaneously for telemetry."
- **Confidence**: emerging (feature shipped; the exact syntax — array vs. named
  list — is not specified in the changelog)
- **Quote**: "The `endpoint` field in OTLP configuration supports multiple backends
  simultaneously for telemetry."
- **Our assessment**: The April 6 release (`blog-ghaw-weekly-2026-04-06.md` Claim 1)
  shipped single-endpoint OTLP tracing with a single `endpoint: https://...`
  field. This release removes that constraint. Teams can now send the same telemetry
  to Honeycomb (real-time query), Grafana Tempo (long-term retention), and Sentry
  (error alerting) from one workflow declaration without routing logic. For Ch02:
  update the `observability.otlp` documentation to reflect multiple-endpoint
  support. The recommended pattern for mature agentic deployments is multi-backend:
  one low-latency backend for live debugging, one retention backend for trend
  analysis.

### Claim 10: Round-robin workflow selection now starts at a random position when the cache is cold, preventing startup bottlenecks where all runners race to process the first item

- **Evidence**: PR #30005. The fix "randomly selects starting items when cache is
  cold, preventing startup bottlenecks."
- **Confidence**: emerging (bug fix described; the specific failure mode — all
  runners starting at item 0 on cache miss — is implied by the fix description)
- **Quote**: "Round-robin workflows randomly select starting items when cache is
  cold, preventing startup bottlenecks."
- **Our assessment**: The thundering-herd pattern on cold start is a classic
  distributed-systems bug: when all consumers initialize simultaneously without
  state, they all grab the first item. In a round-robin workflow, this means
  the first N items get processed N times while the remaining items are ignored
  until the cache warms. Randomizing the start position distributes initial load
  across the queue. For Ch04 (Multi-agent orchestration): any round-robin
  orchestration that initializes from cold state should randomize its starting
  cursor, not begin at position 0.

### Claim 11: The `repo-mind-light.md` shared workflow provides a pre-built reusable workflow for daily issue and PR agentic operations without per-repo customization

- **Evidence**: PR #29063. A shared `repo-mind-light.md` workflow is described as
  "available for reuse across daily issue/PR agentic workflows."
- **Confidence**: emerging (feature shipped; the workflow contents and which daily
  operations it covers are not enumerated in the changelog)
- **Quote**: "A shared `repo-mind-light.md` workflow is available for reuse across
  daily issue/PR agentic workflows (#29063)."
- **Our assessment**: This is an instance of the shared workflow library pattern
  described in `docs-ghaw-sharing-workflows.md`. A daily issue/PR workflow is
  one of the most frequently replicated patterns across repos — most projects
  want some form of daily triage, staleness detection, or PR review automation.
  `repo-mind-light.md` eliminates per-repo implementation for that common case.
  For Ch02: the availability of shared daily-ops workflows should shift the
  recommendation from "build your own daily-ops harness" to "import from the
  shared library and override only what differs."

### Claim 12: The `add_reviewer` MCP tool gains support for setting `team_reviewers` on pull requests, enabling workflows to assign review to GitHub teams rather than individual users

- **Evidence**: PR #29228. The post states the `add_reviewer` MCP tool "supports
  setting `team_reviewers` on pull requests."
- **Confidence**: settled (discrete tooling capability addition with specific PR
  number; the GitHub API distinction between individual and team reviewers is
  well-established)
- **Quote**: "The `add_reviewer` MCP tool supports setting `team_reviewers` on
  pull requests (#29228)."
- **Our assessment**: Previously, `add_reviewer` could only target individual
  users, requiring agentic workflows to maintain a mapping from "team" to
  "individuals." Team reviewer support enables more natural PR assignment that
  respects GitHub team ownership definitions. For Ch02: update `add_reviewer`
  usage guidance to document both individual and team reviewer modes. The team
  mode is preferable for production workflows because it respects org-level
  team membership changes without workflow updates.

## Concrete Artifacts

### Version Summary: v0.71.3 (April 30, 2026)

```
v0.71.3 (April 30, 2026) — Safe-Outputs Reusability + Experiments Infrastructure:
  New:
  - Parameterized safe-outputs for workflow_call callers (#29171)
    (threat-detection, booleans, PR policy fields, list constraints)
  - Configurable MCP gateway session timeout (engine.mcp.session-timeout)
  - Auto-inject create_issue safe output for workflows without explicit config
  - repo-mind-light.md shared workflow for daily issue/PR operations (#29063)
  - team_reviewers support in add_reviewer MCP tool (#29228)
  - Self-hosted runner support for non-default home directories (#27260)

Notable PRs merged (beyond v0.71.3):
  - Compiler detects/sanitizes single-quoted bash commands → Copilot CLI (#30040)
  - Default codex_harness.cjs with retry logic (#30035)
  - A/B experiments framework: experiments CLI command (#30020)
  - experiments analyze: statistical significance for prompt changes (#30029)
  - Multiple OTLP endpoints in endpoint field (#30021)
  - Round-robin: random start position on cache miss (#30005)
```

### Parameterized Safe-Outputs — `workflow_call` Pattern

```yaml
# Caller workflow (calls a shared reusable workflow):
jobs:
  agentic-run:
    uses: org/shared-workflows/.github/workflows/pr-assistant.md@main
    with:
      # Safe-outputs policy parameters (new in v0.71.3, PR #29171):
      threat_detection: true        # controls safe-outputs.threat-detection
      allow_create_issue: true      # boolean flag
      pr_policy_require_review: true  # PR policy field
      # Callers configure without forking the workflow

# Previously: each team forked the shared workflow to set their safe-outputs
# policy, making security patches hard to propagate. Now: one canonical workflow,
# per-caller policy via inputs.
```

### `engine.mcp.session-timeout` — Long-Running Session Configuration

```yaml
# In a gh-aw workflow spec (.md frontmatter):
engine:
  mcp:
    session-timeout: 3600  # seconds; value not confirmed by post, illustrative
# Use case: deep analysis workflows (e.g., ab-testing-advisor at ~500k tokens)
# where default session lifetime may expire mid-run.
```

### A/B Experiments Framework — CLI Usage Pattern

```
# Hidden experiments CLI (PR #30020 + #30029):
gh aw experiments                  # read experiment state from storage-repo branches
gh aw experiments analyze          # compute statistical significance for variants

# Design: experiment state stored in storage-repo branches
# (consistent with integrity-aware cache storage model)
# Use case: A/B testing prompt changes across workflow runs
```

### Agent of the Week: ab-testing-advisor — Operational Data

```
Agent:       ab-testing-advisor
Function:    Identifies workflows lacking experiment infrastructure;
             proposes A/B testing campaigns via GitHub issues
Period:      Week of May 4, 2026

Execution:   3 runs this week
Token cost:  ~500,000 tokens per run
             (deep workflow analysis + experiment specification generation)

May 2nd outputs:
  Issue #29660: prompt_style A/B test proposal for daily-news workflow
  Issue #29661: experiment infrastructure improvement suggestions

Pattern: meta-workflow (agent that improves other agents)
Budget note: token cost is significant; schedule rather than event-trigger
```

## Cross-References

- **Corroborates**:
  - `blog-ghaw-weekly-2026-04-06.md` Claim 1 (OTLP tracing via `observability.otlp`
    frontmatter): Claim 9 here (multiple OTLP endpoints) directly extends that
    capability. The April 6 release established single-endpoint OTLP; this release
    removes the one-backend constraint. Together, they document the complete OTLP
    maturation arc: single backend (April 6) → multi-backend (May 4).
  - `blog-ghaw-weekly-2026-04-13.md` Claim 4 (`ValidateHeredocContent` at five
    user-controlled insertion sites): Claim 8 here (compiler detection of
    single-quoted bash commands) is a further instance of the same compile-time
    safety pattern. April 13: compiler validates injection sites. May 4: compiler
    catches syntax-crash sites. Both extend the gh-aw compile step as the primary
    safety net for a class of runtime failures.
  - `blog-ghaw-weekly-2026-04-06.md` Claim 9 (`agentic-observability-kit`
    meta-monitoring failure, ~4 retries with progressively smaller `count` and
    `max_tokens`): The `ab-testing-advisor` at ~500k tokens per run (Claim 6 here)
    is the same cost scale as the observability kit. Both are meta-workflows that
    perform deep analysis of other workflows. The observability kit hit token-limit
    errors; the ab-testing-advisor appears to budget for this upfront. Together,
    these two cases establish the operational profile for meta-workflow agents:
    high token cost, schedule-driven execution, needs explicit resource budget.

- **Extends**:
  - `blog-ghaw-weekly-2026-04-13.md` (safe-outputs and `workflow_call`
    parameterization discussion): Claim 1 here (parameterized safe-outputs via
    `workflow_call` inputs) is the direct realization of the reusability gap
    that prior releases left open. The April 13 note documented the safe-outputs
    infrastructure; this release makes that infrastructure composable across repos.
  - `blog-ghaw-weekly-2026-03-30.md` (integrity-aware cache storage via git-branch
    isolation): Claim 4 here (A/B experiments framework storing state in
    storage-repo branches) uses the same storage model. March 30 established
    git branches as the typed storage primitive for gh-aw state; the experiments
    framework adopts that model for experiment state.
  - `docs-ghaw-sharing-workflows.md` (shared workflow library): Claim 11 here
    (`repo-mind-light.md`) is a concrete addition to the shared workflow library
    for the daily issue/PR operations category.

- **Contradicts**: None. Multiple OTLP endpoints (Claim 9) extends rather than
  contradicts the single-endpoint pattern from April 6 — callers still pass a
  single endpoint if they choose. No existing source note advocates against
  compile-time safety checks, parameterized safe-outputs, or A/B testing
  infrastructure.

- **Novel**:
  - **A/B experiments framework** (Claims 4–5): First documented infrastructure
    primitive for controlled A/B testing of agentic workflow behavior in the corpus.
    Prior notes describe observability and monitoring but not structured experiments
    with statistical significance analysis.
  - **ab-testing-advisor meta-workflow** (Claim 6): First "agents improving agents"
    example with operational data in the corpus. The pattern of an agent scanning
    a workflow corpus and proposing experiment campaigns is entirely new to the
    corpus. The ~500k token cost establishes the resource profile for this class
    of meta-workflow.
  - **Parameterized safe-outputs for workflow_call** (Claim 1): First coverage of
    safe-outputs as a parameterized layer in reusable workflow design. Prior notes
    treat safe-outputs as per-workflow configuration, not as a composable policy
    API.
  - **`engine.mcp.session-timeout`** (Claim 2): First documented frontmatter field
    for controlling MCP gateway session lifetime. Prior notes describe MCP tool
    capability but not session lifecycle management.
  - **Statistical significance for workflow evaluation** (Claim 5): First mention
    of quantitative significance testing for prompt change assessment in the corpus.
    Adds a principled evaluation layer absent from all prior workflow optimization
    discussion.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add parameterized safe-outputs (Claim 1) as the recommended pattern for any
    team publishing shared workflows. Frame as: safe-outputs policy should be
    separated from workflow logic. The caller configures policy via `workflow_call`
    inputs; the shared workflow enforces it. Reference PR #29171 / v0.71.3.
  - Add `engine.mcp.session-timeout` (Claim 2) as a required configuration item
    for deep analysis workflows. Document alongside the default harness configuration
    section. Any workflow expected to run for more than a few minutes should
    explicitly set this field.
  - Add the default Codex harness with retry logic (Claim 7) to harness
    configuration guidance: Codex workflows no longer need hand-rolled retry code;
    only override `codex_harness.cjs` when non-default retry semantics are needed.
  - Add multiple OTLP endpoints (Claim 9) to the observability frontmatter
    documentation as the recommended configuration for production deployments
    (multi-backend: one low-latency, one long-retention).
  - Add round-robin random-start-on-cache-miss (Claim 10) as a footnote in
    multi-agent orchestration: any workflow that distributes work via round-robin
    should randomize its start cursor, not assume position 0.
  - Note compiler single-quoted bash detection (Claim 8): `gh aw compile` is the
    correct gate before any deployment; this is another class of runtime failure
    it prevents.

- **Chapter 03 (Safety and Verification)**:
  - Add auto-injected `create_issue` safe output (Claim 3) to the safe-outputs
    documentation as a default surface teams must account for: workflows with
    strict containment policies should explicitly audit which safe outputs are
    present, including the implicit `create_issue`. The default reduces boilerplate
    for common cases but may be undesired in high-security contexts.
  - Update the compile-time safety net section to include single-quoted bash
    command detection (Claim 8) alongside heredoc validation from the April 13
    note. Together, these document the gh-aw compiler as a multi-class pre-flight
    safety check.

- **Chapter 04 (Multi-agent orchestration)**:
  - Add A/B experiments framework (Claims 4–5) as the infrastructure layer for
    hypothesis-driven workflow optimization. The `experiments` CLI + `experiments
    analyze` gives teams a complete test-and-measure loop for prompt engineering
    at workflow scale. Frame as the evaluation primitive that transforms workflow
    improvement from anecdotal ("this felt better") to quantified.
  - Add `ab-testing-advisor` (Claim 6) as the canonical example of a meta-workflow
    pattern: an agent that analyzes a corpus of other agents and proposes structured
    improvements. The ~500k token cost establishes the resource profile — meta-
    workflows in this category should be scheduled (e.g., weekly), not event-
    triggered. Budget explicitly and pair with `engine.mcp.session-timeout` to
    avoid mid-run session drops.

- **Chapter 05 (Team Adoption)**:
  - Add `ab-testing-advisor` (Claim 6) as infrastructure evidence for continuous
    agentic improvement at the team level. Teams with a mature workflow corpus can
    automate the identification of optimization opportunities rather than relying
    on human review. This is the logical endpoint of the "agents improve agents"
    progression started by the observability kit.
  - Add statistical significance testing via `experiments analyze` (Claim 5) as a
    recommended practice when evaluating prompt changes — prevents teams from
    shipping "improvements" that are within noise.

## Extraction Notes

1. **Source gap**: This note covers v0.71.3 (April 30). The last extracted weekly
   note (`blog-ghaw-weekly-2026-04-13.md`) covered v0.68.1 (April 10). Versions
   v0.69.x, v0.70.x, and v0.71.0–v0.71.2 are not covered by any existing source
   note. Features from those intermediate versions may have preceded or enabled
   changes described here.
2. **"Hidden" experiments CLI**: The post explicitly labels the `experiments`
   command as "hidden" — this likely means it is not yet surfaced in `gh aw --help`
   and may change before stable release. Claims 4 and 5 are marked emerging
   accordingly.
3. **Token estimate is approximate**: The ~500k token figure for `ab-testing-advisor`
   is described as "approximately" — treat as an order-of-magnitude estimate for
   the meta-workflow class, not a precise per-run budget.
4. **No contradictions filed**: No existing source note makes claims that materially
   conflict with this source. The multiple-endpoint OTLP change (Claim 9) extends
   rather than contradicts the single-endpoint feature from April 6. No contradiction
   issue was warranted.
5. **Registry JSON**: `registry/sources.json` contains pre-existing syntax issues
   (duplicate closing brace at line 38–39). The new registry entry was added at
   the end of the valid entries to avoid worsening the malformed structure.
