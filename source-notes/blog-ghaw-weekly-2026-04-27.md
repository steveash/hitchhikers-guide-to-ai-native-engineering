---
source_url: https://github.github.com/gh-aw/blog/2026-04-27-weekly-update/
source_type: blog-post
title: "Weekly Update – April 27, 2026 (GitHub Agentic Workflows)"
author: GitHub Agentic Workflows team (gh-aw)
date_published: 2026-04-27
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#448"
---

# Weekly Update – April 27, 2026 (GitHub Agentic Workflows)

> Two releases (v0.71.0 and v0.71.1) shipped between April 23–24, 2026 deliver
> five high-signal patterns: (1) a `create_pull_request` infinite loop consumed
> "4.64M tokens per run" — the largest token runaway in the gh-aw corpus — and
> was resolved by adding single-PR-exit logic, establishing infinite-loop
> detection as a category of harness correctness; (2) Claude's deprecated
> `bypassPermissions` flag is replaced by `acceptEdits`, simultaneously closing
> a missing MCP server entry gap in `--allowed-tools`; (3) OTel tracing is
> extended to manually cancelled runs, filling the last major visibility gap in
> the distributed tracing story; (4) pre-agent skills installed by `pre-agent-steps`
> were silently erased by a subsequent "Restore agent config folders" step — a
> step-ordering correctness bug now fixed; and (5) `auto-triage-issues` continues
> its positive trajectory: 4–6 turns, 6 GitHub API calls, with per-day efficiency
> gains, while the team notes potential for deterministic conversion of the workflow.

## Source Context

- **Type**: blog-post (weekly changelog/release update from the GitHub Agentic
  Workflows blog; covers versions v0.71.0–v0.71.1, three additional merged PRs,
  and an "Agent of the Week" spotlight on `auto-triage-issues`)
- **Author credibility**: The gh-aw blog is the official publication of GitHub's
  Agentic Workflows platform team (Don Syme, Peli de Halleux, Mara Kiefer — see
  `blog-gh-aw-operations-release-workflows.md` for author background). Releases
  report on shipped PRs with specific numbers, independently verifiable. The
  token consumption figure (4.64M) and the Agent of the Week metrics (turns,
  API calls) are instrumentation data, not marketing. High credibility for
  first-party platform claims.
- **Scope**: Two releases across two days (April 23–24, 2026). Covers correctness
  fixes (four in v0.71.1), runtime and capability enhancements (three in v0.71.0),
  three additional merged PRs, and the weekly agent spotlight. Does NOT cover:
  whether the `acceptEdits` flag requires workflow migration steps; the full list
  of protected-file syntax forms now supported; the detection mechanism for the
  `create_pull_request` loop; or root-cause analysis of why afternoon runs of
  `auto-triage-issues` were shorter than morning runs.

## Extracted Claims

### Claim 1: A `create_pull_request` workflow loop consumed "4.64M tokens per run" — the largest single-run token figure in the gh-aw corpus — and is resolved by adding exit-after-single-creation logic

- **Evidence**: PR #28353, shipped in v0.71.1. The workflow was invoking
  `create_pull_request` in a loop; the fix exits after a single PR creation.
  Token figure ("4.64M tokens per run") is quoted in the post and represents
  an infinite-loop failure mode distinct from the over-agentic-reasoning runaways
  documented in prior weeks.
- **Confidence**: settled (specific PR, specific token count, clear fix described)
- **Quote**: "4.64M tokens per run"
- **Our assessment**: This is the largest token-runaway figure in the gh-aw weekly
  series by a wide margin. Prior runaways documented in the corpus were due to
  over-agentic reasoning: the contribution-check agent at 1.55M tokens / 50 turns
  (March 23, high workload) and `auto-triage-issues` at 817K tokens / 18 turns
  (March 30, over-contemplation). This case is structurally different: it is a
  loop bug — the agent or workflow kept invoking `create_pull_request` in a cycle
  until resources were exhausted, not because the agent was reasoning excessively
  but because the control flow lacked an exit condition. For Ch02 (Harness
  Engineering): workflows that invoke PR-creation tools must include idempotency
  guards (exit-if-PR-exists checks or single-creation gates). For Ch03 (Safety and
  Verification): hard token limits and turn limits are necessary but not sufficient
  for loop detection; specific tool-call idempotency checks are the correct
  mechanism. This is the first loop-bug token runaway (as distinct from
  over-reasoning runaway) documented in the corpus.

### Claim 2: Claude engine flag `bypassPermissions` is deprecated and replaced by `acceptEdits`, with simultaneous fix for missing MCP server entries in `--allowed-tools`

- **Evidence**: PR #28047, shipped in v0.71.0. The PR transitions from
  `bypassPermissions` to `acceptEdits` and adds previously missing MCP server
  entries in the `--allowed-tools` argument. Both changes are shipped together,
  suggesting the migration touched the tool-invocation path.
- **Confidence**: settled (specific PR, named flags, described changes)
- **Quote**: (no direct quote; post describes the change as transitioning from
  deprecated `bypassPermissions` to `acceptEdits` while fixing missing MCP
  server entries in `--allowed-tools`)
- **Our assessment**: The flag name `bypassPermissions` is semantically significant:
  its name implies it suppressed permission-checking in the Claude integration.
  `acceptEdits` is a narrower semantic — it grants acceptance of file edits
  rather than bypassing a permission layer. This is a hardening change: the new
  flag is descriptively specific about what it allows, rather than broadly
  bypassing permission enforcement. The simultaneous fix for missing MCP server
  entries in `--allowed-tools` is notable: if MCP server entries were absent from
  `--allowed-tools`, those servers may have been operating outside the tool
  allowlist enforcement — a gap in the permission model. Both fixes together
  tighten the Claude invocation surface. For Ch02 (Harness Engineering): harness
  configurations invoking Claude should audit whether they use `bypassPermissions`
  and migrate to `acceptEdits`; the old flag may be removed in a future release.
  For Ch03 (Safety and Verification): the `--allowed-tools` gap is a reminder
  that MCP server registration and tool allowlisting are two independent steps,
  and a server can be registered but excluded from the allowlist unintentionally.

### Claim 3: OpenTelemetry spans are now emitted for manually cancelled workflow runs, delivering duration visibility for interrupted executions

- **Evidence**: PR #28172, shipped in v0.71.0. Manually terminated runs "now
  generate proper OTEL spans, providing complete duration visibility even when
  interrupted."
- **Confidence**: emerging (feature shipped and described; what "proper OTEL spans"
  means for partial runs — whether the spans are marked as cancelled or as errors
  — is not specified in the changelog)
- **Quote**: (no direct quote; post describes that manually terminated runs now
  generate proper OTEL spans with complete duration visibility even when interrupted)
- **Our assessment**: Before this fix, runs cancelled by operators produced no
  OTel spans, creating a gap in the distributed tracing picture: a cancelled run
  had no duration record, no tool-call trace, and no entry in the OTel backend.
  This matters operationally because cancellations are often investigative —
  an operator cancels a run because it looks stuck or is behaving unexpectedly.
  Without cancellation spans, the trace record for that run (which might contain
  the evidence of what went wrong) was lost. For Ch04 (Reliability and
  Observability): OTel instrumentation must cover the full run lifecycle including
  cancellations and interruptions; trace data from failed or cancelled runs is
  often the most operationally valuable. This extends the April 13 cross-job
  parent span work (which covered span hierarchy for multi-job runs) to cover
  runs that do not complete normally.

### Claim 4: Skills installed by `pre-agent-steps` were silently erased by a subsequent "Restore agent config folders" step — a step-ordering correctness bug now fixed

- **Evidence**: PR #28290, shipped in v0.71.1. The bug: skills installed
  through `pre-agent-steps` were eliminated because "Restore agent config folders"
  executed afterward and overwrote the config directory containing those skills.
  Resolution corrects the step sequence.
- **Confidence**: settled (specific PR, clear mechanism described — the "Restore"
  step running after `pre-agent-steps` installations is the ordering bug)
- **Quote**: (no direct quote; post describes skills installed through `pre-agent-steps`
  being eliminated because "Restore agent config folders" executed afterward)
- **Our assessment**: This is a subtle ordering hazard: `pre-agent-steps` is
  designed to inject tools and skills before the agent starts, but if a restoration
  step runs after the pre-steps and resets the config directory to a prior state,
  the injected skills are lost silently — the agent starts without the expected
  tools and no error is raised. Teams relying on `pre-agent-steps` to install
  custom skills would see the agent running without those skills and might
  attribute the failure to the agent's reasoning rather than the configuration.
  For Ch02 (Harness Engineering): step ordering in gh-aw workflows is a
  correctness concern independent of harness logic — restore/reset steps must
  be carefully positioned relative to installation steps. For teams using
  `pre-agent-steps` with custom skill injection, upgrading to v0.71.1 is
  necessary to restore correct behavior.

### Claim 5: Protected-files compilation now accepts both shorthand string syntax and the full `{policy, exclude}` object form — previously the object form was rejected

- **Evidence**: PR #28341, shipped in v0.71.1. The documentation-specified
  `{policy, exclude}` object syntax "was being rejected during compilation."
  The fix enables acceptance of "both shorthand string and complete object formats."
- **Confidence**: settled (specific PR, clear behavior change — a format the
  docs specified was previously rejected)
- **Quote**: (no direct quote; post describes the `{policy, exclude}` object syntax
  as previously rejected during compilation, now accepted alongside shorthand string form)
- **Our assessment**: This is a documentation-reality gap fix: the docs specified
  object syntax but the compiler rejected it. Teams who followed the documentation
  for protected-files configuration with complex policies (where the object form
  with `policy` and `exclude` fields is needed) would have encountered silent
  rejections or compilation failures with no clear error message pointing to the
  syntax mismatch. For Ch02 (Harness Engineering): when compiling gh-aw workflow
  specs that include protected-files configuration, verify against v0.71.1 or later
  if using the object form.

### Claim 6: Max patch size validation now measures only the incremental delta from the previous push, not the cumulative diff from the default branch — preventing false size-limit rejections on long-lived branches

- **Evidence**: PR #28198, shipped in v0.71.1. "Max patch size verification now
  measures only the incremental change from the previous push rather than total
  diff from the default branch."
- **Confidence**: settled (specific PR, clear behavior change described)
- **Quote**: (no direct quote; post describes max patch size now measuring only
  the incremental change from the previous push rather than total diff from the
  default branch)
- **Our assessment**: On long-lived feature branches, the cumulative diff from
  the default branch can be very large even if individual pushes are small and
  well-scoped. The old measurement strategy would reject patches from long-lived
  branches even when each individual commit was appropriately sized. This is a
  correctness fix that matters for multi-day or multi-sprint agentic work on
  feature branches. For Ch02 (Harness Engineering): max patch size as a safety
  control should always be interpreted relative to the incremental change, not
  the total branch divergence; otherwise it creates a perverse incentive to
  keep branches short-lived in order to avoid false rejections.

### Claim 7: Node.js environment setup was absent from Copilot threat-detection workflows, causing "node: command not found" failures before `copilot_driver.cjs` execution

- **Evidence**: PR #28160, shipped in v0.71.0. The fix adds Node.js setup
  before `copilot_driver.cjs` execution in threat-detection workflows, eliminating
  the "node: command not found" error.
- **Confidence**: settled (specific PR, specific error message, clear fix)
- **Quote**: "node: command not found"
- **Our assessment**: Missing runtime dependencies in threat-detection workflows
  are a reliability gap with a safety implication: if the threat-detection workflow
  fails to start, threats go undetected rather than raising an alert. A silent
  "node not found" failure in the threat-detection layer is potentially more
  dangerous than a noisy error, because the rest of the pipeline continues without
  safety verification. For Ch03 (Safety and Verification): safety-verification
  workflows (threat detection, policy enforcement) must have their runtime
  prerequisites verified as part of harness setup; a missing Node.js install
  should surface as an explicit, blocked-workflow failure, not a silent subprocess
  failure. This is a concrete example of the dependency-verification principle for
  safety-critical pipeline steps.

### Claim 8: `auto-triage-issues` runs at 4–6 turns and 6 GitHub API calls per execution, with intra-day efficiency gains, while maintaining potential for deterministic conversion

- **Evidence**: "Agent of the Week" spotlight for April 27. Three executions in
  one day: "4–6 turns per execution," "6 GitHub API calls per run." Efficiency
  improvement: morning run (6 turns) decreased to 4 turns by afternoon. Post
  notes "potential for 'deterministic automation' conversion," though the workflow
  "continued operating identically on subsequent runs."
- **Confidence**: anecdotal (one day's data, three runs; intra-day variation
  could be workload-driven; no accuracy metric reported)
- **Quote**: "4–6 turns per execution" and "6 GitHub API calls per run"
- **Our assessment**: This is the latest entry in a longitudinal `auto-triage-issues`
  performance record across the gh-aw weekly series. The arc: March 30 (18 turns,
  817K tokens, failure); April 13 (4 labels applied in single pass, 100% coverage);
  April 27 (4–6 turns, 6 API calls, three successful executions in one day). The
  agent has materially improved or its task scope has been reduced. The "potential
  for deterministic automation" observation directly echoes the `agentic_fraction`
  guidance from the March 30 note (Claim 6): turns that are pure data-gathering
  can be replaced with deterministic shell steps. That the team notes this
  potential but the workflow "continued operating identically" suggests the
  conversion has not been implemented despite the earlier analysis. For Ch02
  (Harness Engineering): the `agentic_fraction` metric identifies conversion
  candidates; the April 27 spotlight shows that identification and implementation
  are separate steps — recognition of the optimization opportunity does not
  automatically lead to conversion. For Ch04 (Reliability and Observability):
  6 API calls per run and 4–6 turns is a concrete baseline for a triage agent
  that processes a typical issue queue; teams designing similar agents can use
  this as a calibration reference.

### Claim 9: Spurious alerts in `daily-cache-strategy-analyzer` during empty-cache states were false positives — resolved by state-aware alert gating

- **Evidence**: PR #28617, one of three additional merged PRs noted in the
  post (outside the v0.71.x release sets). The fix addresses alerts firing
  during empty cache states.
- **Confidence**: settled (specific PR, clear symptom: alerts on empty-cache
  states that are normal operational conditions, not anomalies)
- **Quote**: (no direct quote; post describes spurious alerts in
  `daily-cache-strategy-analyzer` occurring during empty cache states as fixed)
- **Our assessment**: Spurious alerts in operational monitoring workflows are a
  signal-quality problem: alert fatigue causes operators to ignore or dismiss
  alerts, which degrades the reliability of real alerting. An empty cache state
  is a routine operational condition (e.g., on a fresh environment or after
  cache invalidation), not an anomaly. The fix requires distinguishing expected
  states (empty cache is normal at startup) from anomalous states (empty cache
  on a mature environment with recent activity). For Ch04 (Reliability and
  Observability): monitoring workflows must encode expected-state knowledge;
  alerting on conditions that are normal during legitimate lifecycle transitions
  creates noise that drowns out real signals. This is particularly acute for
  agentic monitoring workflows that run on schedules — they may encounter
  expected-empty states routinely.

## Concrete Artifacts

### Version Summary: v0.71.0–v0.71.1 (April 23–24, 2026)

```
v0.71.1 (April 24) — Four Correctness Fixes:
  - Fix: Protected-files compilation now accepts {policy, exclude} object syntax
         alongside shorthand string form (PR #28341)
  - Fix: Pre-agent skills preserved — step sequence corrected so "Restore agent
         config folders" no longer executes after pre-agent-steps (PR #28290)
  - Fix: Incremental patch size measurement — measures delta from previous push,
         not cumulative diff from default branch (PR #28198)
  - Fix: Infinite loop eliminated — create_pull_request workflow was consuming
         "4.64M tokens per run"; now exits after single PR creation (PR #28353)

v0.71.0 (April 23) — Runtime and Capability Enhancements:
  - Fix: Node.js setup added before copilot_driver.cjs in threat-detection
         workflows; eliminates "node: command not found" errors (PR #28160)
  - New: OTel spans for manually cancelled runs — complete duration visibility
         even when interrupted (PR #28172)
  - Change: Claude engine flag bypassPermissions → acceptEdits (deprecated);
            missing MCP server entries added to --allowed-tools (PR #28047)

Additional Merged PRs (outside release sets):
  - PR #28616: Enhanced documentation for gh aw run / local workflow execution
  - PR #28617: Spurious alerts fixed in daily-cache-strategy-analyzer (empty cache)
  - PR #28618: Accessibility — skip link anchor #_top → #main-content (WCAG 2.4.1)
```

### Infinite Loop Pattern: `create_pull_request` Without Exit Guard

```
Failure Mode (pre-v0.71.1):
  A workflow invoked create_pull_request in a loop.
  Each iteration attempted PR creation even if a PR already existed.
  Token consumption: "4.64M tokens per run"
  Exit condition: none (ran until resource exhaustion)

Fix (v0.71.1, PR #28353):
  Workflow now exits after the first successful PR creation.
  Pattern: check-before-create or create-once guards required for any
           workflow tool that has persistent side effects (PR creation,
           issue filing, comment posting).

Design principle:
  Idempotent tool calls (read, search, inspect) can be called freely.
  Non-idempotent tool calls (create, post, push) require explicit
  exit conditions to prevent runaway loops.
```

### Claude Engine Flag Migration (v0.71.0, PR #28047)

```
Before (deprecated):
  Claude invoked with: --bypass-permissions / bypassPermissions flag
  Effect: bypasses permission enforcement layer

After:
  Claude invoked with: --accept-edits / acceptEdits flag
  Effect: accepts file edits (narrower, explicitly scoped permission)

Simultaneous fix:
  MCP server entries were missing from --allowed-tools argument.
  Servers could be registered but excluded from tool allowlist.
  Fix: all configured MCP servers now appear in --allowed-tools.

Migration requirement:
  Harness configurations using bypassPermissions should migrate to acceptEdits.
  The old flag is deprecated and may be removed in a future release.
```

### Agent of the Week: `auto-triage-issues` — April 27, 2026 Data

```
Agent:        auto-triage-issues
Function:     Reads open issues, applies classifications for team visibility
Period:       April 27, 2026 (single day)

Executions:   3 runs in one day
Turns/run:    "4–6 turns per execution"
API calls/run:"6 GitHub API calls per run"

Intra-day efficiency:
  Morning run:   6 turns
  Afternoon run: 4 turns  (33% turn reduction)

Team assessment: "potential for deterministic automation conversion"
  Note: Workflow "continued operating identically on subsequent runs"
  (conversion not yet implemented as of this report)

Longitudinal record:
  2026-03-30: 18 turns, 817K tokens, Monday sweep FAILED (blog-ghaw-weekly-2026-03-30)
  2026-04-13: 4 labels in single pass, 100% coverage (blog-ghaw-weekly-2026-04-13)
  2026-04-27: 4–6 turns, 6 API calls, 3 successful runs in one day (this note)
```

## Cross-References

- **Corroborates**:
  - `blog-ghaw-weekly-2026-03-23.md` Claim 6 (contribution-check 1.55M tokens /
    50 turns) and `blog-ghaw-weekly-2026-03-30.md` Claim 7 (auto-triage-issues
    817K tokens / 18 turns): The 4.64M token runaway (Claim 1 here) confirms
    token-limit enforcement and loop detection as a category of harness correctness
    concern. Prior runaways were reasoning-quality failures (agent contemplated
    too long); this is a loop-bug failure (no exit condition). The corpus now
    documents two distinct token-runaway root causes: over-agentic reasoning
    (March corpus) and loop-control bugs (April 27).
  - `blog-ghaw-weekly-2026-04-13.md` Claim 10 (auto-triage-issues 100% label
    coverage, 4 labels in single pass): The April 27 Agent of the Week data
    (Claim 8 here) continues the same positive trajectory — the agent is operating
    efficiently. The April 13 coverage metric (were labels applied?) pairs with the
    April 27 efficiency metric (turns per run, API calls per run) to provide a more
    complete performance picture of the same agent across consecutive weeks.
  - `blog-ghaw-weekly-2026-04-06.md` Claim 1 (OTLP distributed tracing via
    `observability.otlp` frontmatter): OTel spans for cancellations (Claim 3 here)
    extends the same tracing infrastructure to cover interrupted runs. April 6
    delivered the tracing framework; April 27 fills the cancellation-visibility gap.

- **Extends**:
  - `blog-ghaw-weekly-2026-04-13.md` Claim 5 (cross-job OTel parent span
    propagation through `aw_context`): The OTel-for-cancellations feature (Claim 3
    here) is the next incremental completion of the distributed tracing story.
    April 6: OTLP framework. April 13: cross-job span hierarchy. April 27:
    cancellation spans. Together, the three releases deliver a complete trace
    record for all run outcomes — normal completion, cross-job pipelines, and
    manual cancellation.
  - `blog-ghaw-weekly-2026-03-30.md` Claim 6 (`agentic_fraction` metric
    identifying deterministic-conversion candidates): The "potential for
    deterministic automation conversion" observation in the April 27 Agent of
    the Week (Claim 8 here) is the applied use of `agentic_fraction` thinking.
    The March 30 note named the metric and the concept; the April 27 note shows
    the team explicitly making the assessment ("potential for deterministic
    conversion") for the same workflow — without yet implementing it. This
    extends the March 30 finding: identification of over-agentic turns and
    the decision to convert them are separate organizational steps.
  - `blog-ghaw-weekly-2026-04-13.md` Claim 3 (agent-stdio.log pre-created at
    0600 before tee writes) and `blog-ghaw-weekly-2026-04-06.md` Claim 6
    (422 `${{ secrets.* }}` migrations): The `bypassPermissions` → `acceptEdits`
    migration (Claim 2 here) is the latest in the gh-aw security hardening
    campaign. Permission-bypass suppression (April 27) joins log-file permission
    hardening (April 13) and secrets interpolation migration (April 6) as the
    third named permission/credential hardening fix in a six-week window.

- **Contradicts**: None. No existing source note recommends `bypassPermissions`
  as a preferred Claude integration flag, recommends measuring patch size against
  the full branch divergence, or documents `pre-agent-steps` skills as persistent
  across the "Restore agent config folders" step. No contradiction issue is
  warranted.

- **Novel**:
  - **Loop-bug token runaway as a distinct failure category** (Claim 1): The
    4.64M token runaway from a `create_pull_request` loop is the first corpus
    example of a token exhaustion event caused by a missing exit condition in
    tool-calling logic, as distinct from over-agentic reasoning. The corpus now
    has both categories documented: reasoning-quantity failures (March) and
    control-flow failures (April 27).
  - **`bypassPermissions` → `acceptEdits` migration** (Claim 2): First corpus
    source to document the deprecation of `bypassPermissions` in the Claude
    engine integration and its replacement with the narrower `acceptEdits` flag.
    Also the first source to document the `--allowed-tools` MCP server omission
    gap.
  - **OTel tracing for manual cancellations** (Claim 3): First corpus source to
    describe instrumentation coverage for manually interrupted workflow runs.
    Prior OTel sources cover normal completions and cross-job hierarchies; this
    is the first cancellation-trace coverage.
  - **Tool idempotency as a loop-prevention design pattern** (Claim 1, Concrete
    Artifacts): The `create_pull_request` infinite loop makes explicit that
    non-idempotent tools require exit-condition guards. No prior corpus source
    names tool idempotency as a loop-prevention design requirement; prior sources
    address over-agentic reasoning but not tool-call loop control.
  - **`pre-agent-steps` skills erasure pattern** (Claim 4): First corpus source
    to document that step ordering between `pre-agent-steps` and harness restore
    steps can silently erase injected skills. This is a new class of harness
    correctness hazard specific to skill injection via pre-steps.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add tool idempotency guards as a named harness design requirement for any
    workflow that invokes non-idempotent tools (create, post, push). Cite the
    `create_pull_request` 4.64M token loop (Claim 1, PR #28353) as the canonical
    failure case. Recommend: any tool call with persistent side effects must
    include a check-before-create or create-once exit condition in the workflow
    control flow.
  - Add `bypassPermissions` → `acceptEdits` migration as a mandatory upgrade
    item for harness configurations invoking Claude (Claim 2, PR #28047). Note
    the simultaneous `--allowed-tools` gap: MCP server registration and tool
    allowlisting are independent; verify that all configured MCP servers appear
    in `--allowed-tools`.
  - Update protected-files configuration guidance to document both shorthand
    string and `{policy, exclude}` object forms as valid syntax (Claim 5,
    PR #28341). Teams using the object form prior to v0.71.1 should verify
    their compilation behavior.
  - Add incremental patch size measurement as the recommended semantics for
    patch-size safety controls (Claim 6, PR #28198). Cumulative diff from the
    default branch is the wrong measure; it penalizes long-lived branches
    regardless of per-push scope.
  - Add `pre-agent-steps` skill preservation as a correctness concern: "Restore
    agent config folders" steps must not execute after skill-injection steps
    (Claim 4, PR #28290). Teams who observed missing custom skills in pre-step-
    configured agents should upgrade to v0.71.1.
  - Cite the `agentic_fraction` observation in the April 27 Agent of the Week
    (Claim 8) as evidence that identifying deterministic-conversion candidates
    and implementing the conversion are separate organizational steps. The
    March 30 note named the metric; the April 27 note shows the gap between
    recognition and action.

- **Chapter 03 (Safety and Verification)**:
  - Add safety-verification workflow dependency checking as a prerequisite for
    threat-detection reliability (Claim 7, PR #28160). If the threat-detection
    workflow cannot start (missing Node.js), threats are not detected — this is
    a worse outcome than a noisy failure. Safety-critical steps must have their
    runtime prerequisites explicitly verified at harness setup.
  - Extend the "agent output as untrusted input" security hardening pattern
    (from April 6 and April 13 notes) with the `bypassPermissions` → `acceptEdits`
    migration (Claim 2) as the third named permission-surface fix in the six-week
    hardening campaign. The pattern of tightening implicit permission grants is
    consistent: log file permissions (April 13), secrets interpolation (April 6),
    permission flag scope (April 27).
  - Add tool loop detection as a safety verification concern alongside token limits
    and turn limits (Claim 1). A workflow that hits neither a token limit nor a
    turn limit before exhausting resources through a tool-call loop is a gap in
    the safety envelope; tool-specific idempotency checks are needed.

- **Chapter 04 (Reliability and Observability)**:
  - Update OTel distributed tracing guidance: cancellation spans (Claim 3,
    PR #28172) complete the trace lifecycle coverage. The full gh-aw distributed
    tracing story (from April 6 + April 13 + April 27): `observability.otlp`
    frontmatter (April 6) + cross-job parent span propagation (April 13) +
    cancellation spans (April 27) = complete trace record for all run outcomes.
  - Add state-aware alert gating as a monitoring design requirement (Claim 9,
    PR #28617). Monitoring workflows must encode expected-state knowledge for
    lifecycle transitions (e.g., empty cache at startup is not anomalous) to
    avoid alert fatigue from false positives.
  - Add `auto-triage-issues` April 27 metrics (4–6 turns, 6 API calls per run)
    as a calibration reference for triage agent design (Claim 8). Pair with the
    March 30 failure (18 turns, 817K tokens) to illustrate the scale of
    improvement when over-agentic behavior is corrected.

## Extraction Notes

1. **Source depth**: The weekly update is a changelog post covering two releases
   and additional merged PRs across ~400–500 words. Nine claims were extracted;
   the token runaway (Claim 1) and the Claude flag migration (Claim 2) are the
   highest-signal items.
2. **WebFetch extraction**: The source content was obtained via a WebFetch model
   that converts HTML to markdown before processing. Quoted strings from the post
   ("4.64M tokens per run," "4–6 turns per execution," "6 GitHub API calls per
   run," "node: command not found") appear verbatim in the extracted content;
   other descriptions are summarized by the fetch model. Claims marked "(no direct
   quote; see paraphrase in Our assessment)" reflect descriptions that could not
   be verified character-for-character from the fetch output.
3. **`bypassPermissions` semantic interpretation**: The security assessment of
   `bypassPermissions` as a broader permission bypass vs. `acceptEdits` as a
   narrower scoped permission is inferred from the flag names. The post confirms
   the migration and the `--allowed-tools` gap fix but does not describe the
   prior security impact of `bypassPermissions` explicitly.
4. **Longitudinal `auto-triage-issues` tracking**: The April 27 Agent of the Week
   data is the fourth appearance of this agent in the weekly series (March 18,
   March 30, April 13, April 27). The four data points together form a meaningful
   longitudinal performance record that no single note captures alone.
5. **No contradictions filed**: Reviewed all existing source notes. No existing
   claim in the corpus is materially opposed by any claim in this source. The
   `bypassPermissions` deprecation and the incremental patch measurement change
   are additive corrections with no corpus counterparts. No contradiction issue
   is warranted.
