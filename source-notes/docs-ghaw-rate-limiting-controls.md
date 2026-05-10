---
source_url: https://github.github.com/gh-aw/reference/rate-limiting-controls
source_type: docs
title: "GitHub Agentic Workflows: Rate Limiting Controls Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#409"
---

# GitHub Agentic Workflows: Rate Limiting Controls Reference

> The comprehensive defense-in-depth anti-runaway reference for gh-aw — the single
> page that enumerates all eight layered mechanisms (bot non-triggering, concurrency,
> timeouts, read-only tokens, safe output limits, built-in delays, per-user rate
> limiting, and manual review gates) in one taxonomy, with their configuration
> fields, default values, and the rationale for layering multiple controls.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/rate-limiting-controls`
  page — in the "Reference" section alongside `reference/concurrency`,
  `reference/permissions`, and `reference/network`. Reference pages document
  platform behavior precisely; this one specifies every control mechanism for
  preventing runaway agents and workflow explosions.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's "Agent Factory" blog series and the `gh aw`
  CLI. Configuration field names, default values, delay timings, and behavior
  descriptions are authoritative for the `gh aw` platform.
- **Scope**: All eight anti-runaway control mechanisms and how they compose.
  Does NOT cover: the full two-tier concurrency model detail (see
  `docs-ghaw-concurrency-reference.md`), the safe outputs permission model in
  depth (see `docs-ghaw-permissions-reference.md` and `docs-ghaw-how-they-work.md`),
  network egress controls (see `docs-ghaw-network-reference.md`), or the
  `stop-after` deadline lifecycle in full detail (see `docs-ghaw-ephemerals.md`).

## Extracted Claims

### Claim 1: GitHub Agentic Workflows uses defense-in-depth to prevent runaway workflows — eight distinct mechanisms layered together, not one primary control

- **Evidence**: The page's opening overview statement names all eight mechanisms
  in one sentence. The page structure then devotes a separate section to each
  mechanism, with configuration details. The "Multiple Protection Layers" example
  combines several mechanisms in one workflow spec to illustrate layering.
- **Confidence**: settled (first-party reference documentation; the taxonomy is
  explicitly stated and the page is organized around it)
- **Quote**: "GitHub Agentic Workflows uses defense-in-depth to prevent runaway
  workflows: bot non-triggering, concurrency controls, timeouts, rate limiting,
  read-only agents, safe output limits, built-in delays, and manual review gates."
- **Our assessment**: The defense-in-depth framing is the most important
  architectural insight on this page. No single mechanism is sufficient on its
  own: a timeout stops runaway duration but not runaway cascades; safe output
  limits stop runaway dispatch counts but not runaway per-run loops; per-user
  rate limits stop external triggers but not internally-dispatched workflows.
  The eight mechanisms address complementary failure modes. For Ch02 (Harness
  Engineering): present this taxonomy as the complete anti-runaway checklist —
  harness authors should consciously select which mechanisms to apply based on
  the risk profile of their workflow. For Ch04 (Safety and Verification): the
  taxonomy maps directly to a safety configuration review checklist.

### Claim 2: Bot non-triggering — the `github-actions[bot]` account cannot trigger workflow events, intrinsically preventing infinite loops when workflows create issues or post comments via safe outputs

- **Evidence**: The page documents this as the first mechanism. The behavior is
  platform-enforced (not configurable) — the bot account's actions simply do not
  fire workflow trigger events.
- **Confidence**: settled (first-party documentation; this is a platform constraint,
  not a configuration option)
- **Quote**: "The `github-actions[bot]` account does not trigger workflow events.
  When a workflow creates an issue or posts a comment via safe outputs, it won't
  trigger other workflows - preventing infinite loops."
- **Our assessment**: This is the most fundamental of the eight mechanisms because
  it requires zero configuration — it is the platform's baseline guarantee against
  the most common recursive loop pattern (workflow A creates a comment → comment
  triggers workflow A again). It is also the least visible: practitioners may not
  know the loop protection is there unless they read this reference. The constraint
  scope is important: it applies specifically to the `github-actions[bot]` account
  executing safe outputs — if a workflow uses a PAT (personal access token) instead
  of GITHUB_TOKEN for write operations, the bot non-triggering constraint does NOT
  apply, and infinite loops become possible. For Ch03 (Safety): document this as
  the zero-config baseline loop prevention, with the explicit caveat that PAT-based
  write operations bypass it.

### Claim 3: Concurrency controls use dual enforcement — per-workflow (based on trigger context) and per-engine (one agent job at a time per AI engine)

- **Evidence**: The page summarizes the concurrency mechanism with the standard
  `gh-aw-${{ github.workflow }}` group pattern example, calling out the two tiers.
- **Confidence**: settled (first-party documentation; consistent with the detailed
  treatment in `docs-ghaw-concurrency-reference.md`)
- **Quote**: "Workflows use dual concurrency control: per-workflow (based on
  context) and per-engine (one agent job at a time per AI engine)."
- **Our assessment**: This claim is the rate-limiting reference's summary of the
  full concurrency model. The per-engine singleton is the most impactful mechanism
  for preventing runaway parallel AI resource consumption: even if multiple workflow
  triggers fire simultaneously, at most one agent job runs per AI engine at any
  moment. Cross-reference `docs-ghaw-concurrency-reference.md` for the full two-tier
  architecture including custom overrides and the `job-discriminator` mechanism.
  For Ch02: when introducing the anti-runaway controls, the concurrency mechanism
  should be presented as the first active-dispatch guard.

### Claim 4: Timeouts enforce a default 20-minute agent execution limit and a 360-minute GitHub Actions platform default; `stop-after` provides a separate workflow-level deadline preventing execution beyond time limits (minimum unit: hours)

- **Evidence**: The page lists the default agent timeout (20 minutes) and the
  GitHub Actions platform default (360 minutes) explicitly. It documents
  `timeout-minutes` as the per-run configuration field and `stop-after` as the
  deadline field. Example custom values include `timeout-minutes: 120` and
  `stop-after: +48h`. Custom runners are noted as supporting extended timeouts.
- **Confidence**: settled (first-party documentation; timeout values and field names
  are authoritative for the platform)
- **Quote**: (no direct quote capturing both values; see paraphrase in Our assessment
  and YAML artifacts below)
- **Our assessment**: The two timeout mechanisms serve different functions. `timeout-minutes`
  is a per-run ceiling — it kills an individual workflow run that has been executing
  too long. `stop-after` is a scheduling deadline — it prevents new runs from being
  triggered after a point in time, allowing in-flight runs to complete. `stop-after`
  persists through recompilation (per `docs-ghaw-ephemerals.md` Claim 2); the
  `--refresh-stop-time` flag must be passed explicitly to extend the deadline. The
  20-minute default agent timeout is deliberately short — it assumes agents should
  complete their task in a single focused session. Workflows with inherently longer
  tasks (e.g., running a test suite or downloading large datasets) must explicitly
  set a higher `timeout-minutes`. For Ch02: document both fields together as the
  per-run and per-lifecycle timeout pair.

### Claim 5: Read-only tokens — agents operate with read-only GitHub permissions; write operations flow exclusively through the safe outputs system, providing validation and auditing

- **Evidence**: The page calls this out as a distinct mechanism in the anti-runaway
  taxonomy.
- **Confidence**: settled (consistent with the full treatment in
  `docs-ghaw-permissions-reference.md` and `docs-ghaw-how-they-work.md` Claim 4)
- **Quote**: (no direct quote; see paraphrase in Our assessment — the permissions
  model is fully documented in `docs-ghaw-permissions-reference.md`)
- **Our assessment**: In the context of runaway prevention, read-only tokens serve
  a different function than in the security model: they limit the *blast radius*
  of a runaway agent. An agent that loops indefinitely with read-only permissions
  consumes AI tokens and compute but cannot create unlimited GitHub state (issues,
  PRs, comments). Without this constraint, a runaway agent could create thousands
  of issues or comments before the timeout kills it. The safe-outputs system is
  both the write path and the enforcement boundary — safe output limits (Claim 6)
  apply specifically because all writes must go through this layer. For Ch03:
  present read-only tokens and safe output limits as a paired mechanism: read-only
  limits *damage*; safe output limits bound *count*.

### Claim 6: Safe output limits enforce per-operation maximums — `assign-to-agent`, `assign-to-bot`, and `dispatch-workflow` all default to `max: 1` — preventing exponential agent cascades and workflow explosions

- **Evidence**: The page provides an explicit table documenting three operations
  with their default max values and stated purposes. The rationale for the `max: 1`
  default is given directly: without limits, a workflow spawning multiple agents
  that each spawn more would create exponential growth.
- **Confidence**: settled (first-party documentation; the table and default values
  are authoritative for the platform)
- **Quote**: "Without limits, one workflow could spawn three agents, each spawning
  three more, creating exponential growth. The default max of 1 ensures linear
  progression."
- **Our assessment**: The three operations with `max: 1` defaults represent the
  three pathways for cascade growth: `assign-to-agent` (agent spawning another
  agent), `assign-to-bot` (agent delegating to a bot), and `dispatch-workflow`
  (agent triggering another workflow). All three default to 1 because the
  exponential risk is symmetric across all three channels. A team that needs more
  than 1 dispatch per run must explicitly override with `max: N` — this is the
  correct design: escalation requires intentional configuration, not the default.
  The `max:` annotation is the same per-safe-output rate-limiting mechanism
  documented in `docs-ghaw-chatops.md` Claim 8 (`max: 5` on
  `create-pull-request-review-comment`) — confirming that `max:` is the universal
  volume-limiting mechanism across all safe output types. For Ch02: document the
  three cascade-prevention defaults prominently — they are the most direct defense
  against multi-agent explosions in fan-out architectures.

### Claim 7: Built-in delays impose a 10-second pause between agent assignments and a 5-second pause between workflow dispatches — designed to prevent burst patterns and spread load over time

- **Evidence**: Both delay values are explicitly stated on the page. The timing
  rationale is given directly. A practical implication is noted: "five agents ≈
  40 seconds total" (five assignments with four 10-second gaps).
- **Confidence**: settled (first-party documentation; specific delay values are
  platform specifications)
- **Quote**: "These prevent burst patterns and spread load over time."
- **Our assessment**: The built-in delays are a passive rate-limiting mechanism —
  they require no configuration and cannot be disabled. Their primary effect is on
  fan-out scenarios: an orchestrator dispatching five parallel agent assignments
  will actually trigger them with 10-second gaps, meaning 40 seconds of serial
  delay before all five are queued. This is not a performance concern for most
  workflows (40 seconds is negligible for multi-minute agent tasks), but it is
  a troubleshooting point practitioners may not expect. The 5-second dispatch
  delay similarly serializes what appears to be parallel `dispatch-workflow` calls.
  The troubleshooting section of the page calls this out explicitly as a common
  confusion source ("Slow agent assignments → 10-second delays are intentional").
  For Ch02: document the delays as expected platform behavior, not a bug — include
  the timing calculation for practitioners sizing workflows with fan-out.

### Claim 8: The `rate-limit` frontmatter field provides per-user request throttling — `max` (1–10 runs per window) and `window` (up to 180 minutes) — with `ignored-roles` defaulting to `[admin, maintain]` and `events` to filter which trigger types count

- **Evidence**: The page provides the complete `rate-limit` YAML with four fields:
  `max` (valid range 1–10 runs per window), `window` (default 60 minutes, max 180
  minutes), `events` (list of trigger types to include in the count), and
  `ignored-roles` (roles exempt from rate limiting). The defaults for `ignored-roles`
  are `[admin, maintain]` but the page also notes `write` as part of the exempt set.
- **Confidence**: settled (first-party documentation; field names, valid ranges, and
  defaults are authoritative)
- **Quote**: "The `rate-limit` frontmatter field prevents users from triggering
  workflows too frequently."
- **Our assessment**: Per-user rate limiting is the only mechanism that addresses
  the external-attacker threat model directly: without it, any user with sufficient
  permissions (or, if using `roles: all` in ChatOps, any authenticated user) can
  trigger a workflow continuously. The 1–10 range for `max` is narrow — it prevents
  both trivial bypassing (minimum 1 means at least one request always succeeds)
  and excessive restriction (maximum 10 means legitimate power users aren't blocked).
  The 180-minute window ceiling prevents the sliding window from being so wide that
  the rate limit is effectively per-day rather than per-session. The `ignored-roles`
  default exempts admins and maintainers — who are presumed trusted — but the
  `ignored-roles: []` pattern applies rate limiting universally, including to
  organization owners. The `events` field enables scoping the rate limit to
  specific trigger types: a workflow triggered by both `workflow_dispatch` and
  `issue_comment` could rate-limit only the `issue_comment` path (more vulnerable
  to external abuse) while allowing unlimited `workflow_dispatch` (typically
  admin-only). For Ch03 (Safety): `rate-limit` with a narrow `max` and targeted
  `events` is the correct defense for workflows exposed to public comment threads.

### Claim 9: `ignored-roles: []` removes all role exemptions from rate limiting — applying the throttle to every user including admins, enabling universal rate enforcement

- **Evidence**: The page states this explicitly as part of the `rate-limit` field
  documentation.
- **Confidence**: settled (first-party; the pattern is explicitly documented as
  an option)
- **Quote**: "By default, users with `admin`, `maintain`, or `write` roles are
  exempt from rate limiting. To apply rate limiting to all users including admins,
  set `ignored-roles: []`."
- **Our assessment**: The `ignored-roles: []` pattern is notable for two reasons:
  (1) it is the configuration for maximum-strictness rate limiting — no user is
  exempt; (2) it reveals that the default exempt set includes not just `admin` and
  `maintain` but also `write`, which is a broader set than the ChatOps `roles:`
  default documented in `docs-ghaw-chatops.md` Claim 3. The full list
  (admin + maintain + write) means any contributor with push access is exempt from
  rate limiting by default. Teams deploying workflows in open-source repositories
  where many contributors have `write` access should evaluate whether the default
  exemption is appropriate. For Ch03: add `ignored-roles: []` as the pattern for
  high-security rate limiting scenarios where all users — including trusted
  contributors — should be subject to the same throttle.

### Claim 10: Manual review gates via GitHub Environments can be applied to specific safe outputs, requiring human approval before sensitive operations execute

- **Evidence**: The page shows the `environment: production` field in a
  `safe-outputs.dispatch-workflow` block as the mechanism for gating workflow
  dispatch on human approval. This integrates with GitHub's Environment protection
  rules (required reviewers, wait timers, etc.).
- **Confidence**: settled (first-party documentation; the YAML field is shown in
  the comprehensive protection example)
- **Quote**: (no direct prose quote; the `environment:` field appears in the YAML
  example — see Concrete Artifacts)
- **Our assessment**: Environment-based gates are the only mechanism on this page
  that requires active human intervention rather than automated enforcement.
  Where safe output limits (Claim 6) cap the *count* of dispatches and per-user
  rate limits (Claim 8) cap the *frequency*, environment gates stop execution
  entirely until a human approves. The scoping is important: the `environment:`
  field is per-safe-output (e.g., only `dispatch-workflow` requires approval, not
  `add-comment`), allowing fine-grained HITL control. This is the same mechanism
  described at the conceptual level in `docs-ghaw-how-they-work.md` Claim 10
  ("critical actions can require human approval"). For Ch08 (Human-in-the-Loop):
  the `environment:` field on `safe-outputs` is the concrete configuration for
  inserting human approval gates into agentic workflows.

### Claim 11: Layering multiple controls is the recommended pattern — the "Comprehensive Protection Example" combines `timeout-minutes`, `rate-limit`, `stop-after`, `safe-outputs.assign-to-agent.max`, and `environment` in a single workflow spec

- **Evidence**: The page provides a dedicated "Example: Multiple Protection Layers"
  section with a YAML spec that combines five mechanisms simultaneously. The best
  practices section reinforces: "Start conservatively and increase limits as needed.
  Layer multiple controls."
- **Confidence**: settled (first-party documentation; the example is prescriptive
  guidance, not descriptive)
- **Quote**: "Start conservatively and increase limits as needed. Layer multiple
  controls. Monitor workflow runs and adjust based on safe output logs."
- **Our assessment**: The "layer multiple controls" recommendation is operationally
  specific: different mechanisms protect against different failure modes, so they
  are complements, not alternatives. The comprehensive example demonstrates this
  composition: `timeout-minutes` bounds per-run duration; `rate-limit` bounds
  per-user trigger frequency; `stop-after` bounds workflow lifetime; `max: 1`
  bounds cascade count; `environment: production` requires human sign-off for
  the most consequential operation. A team that uses only one mechanism has a
  single point of failure in their anti-runaway design. For Ch02: use the
  comprehensive protection example as the reference template for any new workflow
  that has elevated risk (public-facing, fan-out capable, or long-running).

## Concrete Artifacts

### Page Overview Statement (from source)

```
"GitHub Agentic Workflows uses defense-in-depth to prevent runaway workflows:
bot non-triggering, concurrency controls, timeouts, rate limiting, read-only
agents, safe output limits, built-in delays, and manual review gates."
```

*Source: docs-ghaw-rate-limiting-controls, opening overview*

### Safe Output Limits — Default Max Table (from source)

| Operation | Default Max | Purpose |
|-----------|-------------|---------|
| `assign-to-agent` | 1 | Prevent agent cascades |
| `assign-to-bot` | 1 | Prevent bot loops |
| `dispatch-workflow` | 1 | Prevent workflow explosions |

*Source: docs-ghaw-rate-limiting-controls, "Safe Output Limits" section*

### Timeout and Stop-After Configuration

```yaml
timeout-minutes: 120     # Per-run wall-clock limit (default: 20 min for agents)
stop-after: +48h         # Workflow-level deadline (minimum unit: hours)
```

*Source: docs-ghaw-rate-limiting-controls, "Timeouts" section.
Default agent execution timeout: 20 minutes.
GitHub Actions platform default (other jobs): 360 minutes.*

### Per-User Rate Limiting — Full `rate-limit` Field

```yaml
rate-limit:
  max: 5              # Runs per window (valid range: 1–10)
  window: 60          # Window in minutes (default: 60, max: 180)
  events: [workflow_dispatch, issue_comment]  # Which trigger types count
  ignored-roles: [admin, maintain]            # Roles exempt from rate limiting

# To apply rate limiting to ALL users including admins:
# ignored-roles: []
```

*Source: docs-ghaw-rate-limiting-controls, "Rate Limiting Per User" section.
Default ignored-roles includes admin, maintain, and write.*

### Comprehensive Protection Example (from source)

```yaml
---
name: Safe Agent Workflow
engine:
  id: copilot
timeout-minutes: 60
on:
  issues:
    types: [opened]
rate-limit:
  max: 5
  window: 60
stop-after: +2h
safe-outputs:
  assign-to-agent:
    max: 1
    environment: production
---
```

*Source: docs-ghaw-rate-limiting-controls, "Example: Multiple Protection Layers"
section — combines timeout, rate-limit, stop-after, safe-output max, and
environment gate in one workflow spec.*

### Built-In Delays Reference

```
Agent assignments:     10-second delay between each assignment
Workflow dispatches:    5-second delay between each dispatch

Timing implication: five agent assignments = ~40 seconds total
(four 10-second gaps between five sequential assignments)

Note: delays are platform-enforced, not configurable, and intentional.
Troubleshooting: "Slow agent assignments → 10-second delays are intentional"
```

*Source: docs-ghaw-rate-limiting-controls, "Built-In Delays" section*

### Manual Review Gate via GitHub Environment

```yaml
safe-outputs:
  dispatch-workflow:
    environment: production  # Requires human approval before dispatch executes
```

*Source: docs-ghaw-rate-limiting-controls, "Manual Review Gates" section.
Integrates with GitHub Environment protection rules (required reviewers,
wait timers, deployment branches).*

### Troubleshooting Reference (from source)

```
Immediate cancellation:
  → Check rate limit in pre-activation logs
  → Verify concurrency queue
  → Confirm stop-after timing

Slow agent assignments:
  → 10-second delays are intentional; five agents ≈ 40 seconds total

Dispatch not triggering:
  → Verify max dispatch limit (default: 1)
  → Check 5-second delay between dispatches
  → Confirm target workflow has `on: workflow_dispatch`
  → Check environment approvals if configured
```

*Source: docs-ghaw-rate-limiting-controls, "Troubleshooting" section*

### Best Practices (from source)

```
1. Start conservatively and increase limits as needed.
2. Layer multiple controls.
3. Monitor workflow runs and adjust based on safe output logs.
```

*Source: docs-ghaw-rate-limiting-controls, "Best Practices" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer defense-in-depth pipeline):
    this source expands the "defense-in-depth" framing from five layers (security
    architecture) to eight specific anti-runaway mechanisms. Both sources share the
    defense-in-depth principle; this reference makes it operational with specific
    configurations. The five security layers and the eight anti-runaway mechanisms
    are complementary taxonomies: the five-layer model organizes *what* the platform
    protects against (compilation bugs, runtime escapes, permission abuse, network
    exfiltration, output poisoning); the eight anti-runaway mechanisms organize
    *how* it prevents *cost explosion and cascade growth*.
  - `docs-ghaw-how-they-work.md` Claim 10 (critical actions can require human
    approval): Claim 10 here names GitHub Environments as the YAML mechanism for
    implementing that approval gate. The how-they-work note describes the capability;
    this reference shows the `environment: production` field in a concrete YAML
    example.
  - `docs-ghaw-chatops.md` Claim 8 (`max: 5` on `create-pull-request-review-comment`
    as a rate-limiting mechanism for agent output volume): this reference confirms
    that the `max:` annotation is the universal volume-limiting mechanism across all
    safe output types, not just `create-pull-request-review-comment`. The ChatOps
    note showed one application; this note provides the authoritative defaults table
    (assign-to-agent: 1, assign-to-bot: 1, dispatch-workflow: 1) and the cascade
    rationale. Together they give the complete picture of `max:` as a per-output
    rate-limiting control.
  - `docs-ghaw-ephemerals.md` Claim 1 (`stop-after` as cost-control primitive):
    both sources document `stop-after` with a minimum unit of hours and a relative
    delta format. This reference's `+48h` example is consistent with the ephemerals
    note's `+7d`, `+25h`, `+1d12h30m` examples. This reference positions `stop-after`
    as one of eight anti-runaway controls; the ephemerals note covers its full
    lifecycle semantics (recompilation persistence, `--refresh-stop-time` CLI flag).
    No contradiction — different depth of coverage of the same mechanism.
  - `blog-ghaw-weekly-2026-03-23.md` Claim 6 (contribution-check agent exhibited
    5× cost runaway — 1.55M tokens, 50 turns): the eight mechanisms documented
    here are precisely the controls that prevent or limit such runaways. The 1.55M
    token runaway (while correct) would have been contained by a `timeout-minutes`
    ceiling and the per-engine singleton (if concurrent workflows had competed for
    the AI engine). This source provides the "how to prevent the problem" complement
    to the weekly note's "here is the problem."
  - `docs-ghaw-concurrency-reference.md` Claim 3 (per-engine singleton enforcement —
    one agent job per engine across all workflows): this source names the per-engine
    singleton as one of its eight mechanisms, consistent with the deep treatment in
    the concurrency reference. No contradiction; the concurrency reference provides
    full detail on overrides and the `job-discriminator` mechanism.

- **Extends**:
  - `docs-ghaw-how-they-work.md` Claims 4–5 (read-only by default, Safe Outputs
    as permission-separated write path): this reference adds the runaway-prevention
    framing to the permission model — read-only tokens are not just a security
    mechanism but also a blast-radius limiter for runaway agents. The how-they-work
    note covers the security rationale; this reference adds the cost/damage-control
    rationale.
  - `docs-ghaw-permissions-reference.md` Claim 2 (four security rationales for
    read/safe-outputs separation): this reference adds a fifth implicit rationale —
    blast-radius containment for runaway agents. An agent that goes runaway with
    read-only permissions cannot create unbounded GitHub state; it only burns AI
    tokens and compute.
  - `docs-ghaw-safe-rollout.md` Claim 1 ("start in report-only mode" framing):
    the best practices here ("start conservatively and increase limits as needed")
    are the rate-limiting expression of the same trust-promotion principle. The
    safe-rollout note applies this to autonomy promotion; this note applies it to
    limit configuration.

- **Contradicts**: None identified. All eight mechanisms are consistent with their
  detailed treatments in existing source notes (concurrency, permissions, network,
  ephemerals, chatops, how-they-work). No contradiction issue required.

- **Novel** (what this note adds that no prior source covers):
  - **Eight-mechanism anti-runaway taxonomy in one reference** (Claim 1): No prior
    corpus note names all eight mechanisms together or frames them as a coordinated
    defense-in-depth anti-runaway system. The how-they-work five-layer model covers
    security; this is the operational cost/runaway-containment companion taxonomy.
  - **Bot non-triggering as a named, zero-config mechanism** (Claim 2): The
    `github-actions[bot]` loop prevention behavior is not documented in any existing
    source note, including `docs-ghaw-how-they-work.md`. It is the most invisible
    of the eight mechanisms but one of the most important for preventing recursive
    loops in comment-heavy workflows.
  - **Safe output defaults table: assign-to-agent=1, assign-to-bot=1,
    dispatch-workflow=1** (Claim 6): The specific default `max: 1` values for the
    three cascade-prevention output types are not documented in any existing source
    note. The chatops note documented `max: 5` on a different output type; this
    reference provides the cascade-specific defaults with their rationale.
  - **Built-in delay values: 10 seconds (agent assignments), 5 seconds
    (dispatches)** (Claim 7): No existing source note documents these specific
    delay values. The timing calculation (five agents ≈ 40 seconds) is particularly
    useful for practitioners designing fan-out workflows.
  - **`rate-limit` frontmatter field** (Claim 8): No existing source note
    documents this field. The complete syntax (max, window, events, ignored-roles)
    and valid ranges (max 1–10, window max 180 minutes) are new to the corpus.
  - **`ignored-roles: []` for universal rate limiting** (Claim 9): The pattern for
    applying rate limits to admins is not documented elsewhere.
  - **Comprehensive protection example combining five mechanisms** (Claim 11): No
    existing source note provides a multi-mechanism combined YAML example. The
    "Multiple Protection Layers" example is the first corpus artifact showing
    how the mechanisms compose in a single workflow spec.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add the eight-mechanism anti-runaway taxonomy as a harness design checklist**
  (Claim 1): Currently the corpus has individual notes on concurrency, permissions,
  network, and ephemerals, but no single reference synthesizes them as a runaway
  prevention system. Ch02 should present the eight mechanisms as a review checklist
  for every new workflow: which mechanisms are active by default (bot non-triggering,
  per-engine singleton, 20-min timeout, 10s/5s delays); which require explicit
  configuration (rate-limit, stop-after, safe output max overrides, environment
  gates).

- **Add bot non-triggering as a named zero-config safety baseline** (Claim 2):
  Practitioners designing comment-posting workflows should know the loop prevention
  is built in — and the caveat that PAT-based writes bypass it.

- **Add safe output default max values to the harness template** (Claim 6):
  When introducing safe outputs, document that `assign-to-agent`, `assign-to-bot`,
  and `dispatch-workflow` default to `max: 1`. Teams building fan-out architectures
  must explicitly raise these limits; the defaults are conservative by design.

- **Add built-in delay timing as expected behavior** (Claim 7): The 10-second and
  5-second delays affect fan-out workflow timing. Document the calculation
  (N agents = (N-1) × 10 seconds of sequential delay) so teams can size timeouts
  appropriately in fan-out scenarios.

- **Add `rate-limit` field documentation** (Claim 8): Document the complete field
  (max 1–10, window up to 180 min, events filter, ignored-roles). Include
  `ignored-roles: []` as the pattern for maximum-strictness enforcement.

- **Add the comprehensive protection example as the template for elevated-risk
  workflows** (Claim 11): Use the "Multiple Protection Layers" YAML as the
  recommended starting point for any workflow that is public-facing, fan-out
  capable, or long-running.

### Chapter 03 / Chapter 04: Safety and Verification / Agent Safety

- **Frame rate-limiting controls as the cost-containment complement to the
  five-layer security model** (Claim 1): The security model prevents unauthorized
  access and exploitation; the anti-runaway mechanisms prevent authorized
  workflows from becoming unintentionally expensive or self-amplifying. Both are
  required for a production-grade agentic harness.

- **Add `environment:` on safe outputs as the concrete HITL gate mechanism**
  (Claim 10): Cross-reference with `docs-ghaw-how-they-work.md` Claim 10. The
  `environment: production` pattern on `dispatch-workflow` is the YAML expression
  of human-in-the-loop for consequential automated actions.

- **Add per-user rate limiting as the defense against external-trigger abuse**
  (Claims 8–9): For workflows triggered from public comment threads (ChatOps or
  IssueOps), `rate-limit` is the required defense against volume abuse. Document
  the `events` filter pattern for scoping rate limits to the most-exposed trigger
  paths.

### Chapter 08: Human-in-the-Loop

- **Document `environment:` on `safe-outputs` as the approved HITL insertion
  point** (Claim 10): This is the gh-aw platform's built-in mechanism for
  requiring human approval before specific automated actions execute. It integrates
  with GitHub's Environment protection rules (required reviewers, deployment
  branch restrictions), giving teams standard GitHub workflow approval tooling for
  agentic workflows. Frame it alongside the ChatOps `slash_command` trigger
  (`docs-ghaw-chatops.md` Claim 1) as the two HITL modes: approval gate (passive
  wait) vs. human-initiated invocation (active command).

## Extraction Notes

1. **Source content via WebFetch AI model**: The gh-aw documentation is an
   Astro/Starlight SPA. The first WebFetch pass returned structured content
   including the eight mechanism overview, table data, YAML examples, numeric
   values, and troubleshooting guidance. A second pass requesting verbatim
   reproduction was declined citing copyright concerns. Technical strings (YAML
   field names, numeric values, table data) from the first pass are assessed as
   accurate platform specifications. Prose passages marked as quotes were returned
   in quoted form by the model on the first pass; they appear consistent with the
   page structure but should be verified by the Assayer against the source URL.

2. **Default `ignored-roles` set**: The first fetch result included `admin` and
   `maintain` in the `rate-limit` YAML example; a separate prose description
   mentioned `admin`, `maintain`, and `write` as the exempt default set. The
   source note uses the broader three-role set (admin + maintain + write) for
   the prose claim (Claim 9) and shows the two-role set in the YAML artifact
   as it appeared in the fetched example. The discrepancy may reflect the page
   showing a partial example in YAML vs. a complete list in prose.

3. **No contradictions filed**: Reviewed all existing corpus source notes.
   No claims in this source materially oppose existing notes. The `stop-after`
   coverage is consistent with `docs-ghaw-ephemerals.md` (different depths of
   the same mechanism). The concurrency summary is consistent with
   `docs-ghaw-concurrency-reference.md`. The safe-outputs defaults table adds
   new data not in prior notes — not a contradiction. No contradiction issue
   required.

4. **PAT bypass caveat**: The bot non-triggering claim includes an important
   caveat (PAT-based writes bypass the loop prevention) inferred from the platform
   design — not explicitly stated in the source. This is marked as Our assessment
   rather than a claim, because it is a logical inference from how GitHub's event
   system works, not a direct statement from this page.

5. **Related Documentation section not followed**: The page lists several related
   documentation links (likely to the concurrency reference, permissions reference,
   safe rollout guide, and ephemeral lifecycle guide). These are all already covered
   in the corpus by dedicated source notes. No new sub-pages were followed.
