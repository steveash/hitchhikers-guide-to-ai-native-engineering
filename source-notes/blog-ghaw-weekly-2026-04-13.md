---
source_url: https://github.github.com/gh-aw/blog/2026-04-13-weekly-update/
source_type: blog-post
title: "Weekly Update – April 13, 2026 (GitHub Agentic Workflows)"
author: GitHub Agentic Workflows team (gh-aw)
date_published: 2026-04-13
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#237"
---

# Weekly Update – April 13, 2026 (GitHub Agentic Workflows)

> Five releases shipped between April 6–10, 2026 (v0.67.2–v0.68.1) deliver
> six high-signal patterns for AI-native engineering: (1) `engine.bare` as a
> clean-slate context-suppression primitive, enabling intentional no-context
> agent runs; (2) `pre-steps` for in-job token-minting without cross-job
> masking; (3) two security hardening patterns — log-file permission hardening
> for MCP bearer tokens and heredoc-injection-site validation; (4) cross-job
> OTel parent span propagation extending the April 6 OTLP release; (5) a
> Copilot CLI version-pinning regression with hotfix (first explicit engine-
> version pinning failure in corpus); and (6) the `always()` footgun for agent
> memory persistence, where `push_repo_memory` ran on bot-triggered no-ops
> because `always()` bypassed skip propagation.

## Source Context

- **Type**: blog-post (weekly changelog/release update from the GitHub Agentic
  Workflows blog; covers versions v0.67.2–v0.68.1 and in-flight PRs; includes
  an "Agent of the Week" spotlight on `auto-triage-issues`)
- **Author credibility**: The gh-aw blog is the official publication of GitHub's
  Agentic Workflows platform team (Don Syme, Peli de Halleux, Mara Kiefer — see
  `blog-gh-aw-operations-release-workflows.md` for author background). Weekly
  updates report on shipped releases with specific PR numbers. Security claims
  reference specific PRs and are independently verifiable. High credibility for
  claims about their own platform.
- **Scope**: Five releases across five days (April 6–10, 2026). Covers context
  control (`engine.bare`, `pre-steps`), security hardening (log permissions,
  heredoc validation, Markdown injection), OTel trace hierarchy, harness
  workflow templates (five new), and a Copilot CLI regression + hotfix. Does
  NOT cover: migration path for `add-comment.discussion` → `discussions:` in
  depth; exact heredoc insertion site names; root cause of the Copilot CLI
  v1.0.22 incompatibility; or whether `engine.bare` applies per-agent or
  per-workflow.

## Extracted Claims

### Claim 1: `engine.bare: true` suppresses automatic context loading — AGENTS.md, user instructions for Copilot, and CLAUDE.md memory files for Claude — enabling intentional clean-slate agent runs

- **Evidence**: PR #25661, shipped in v0.68.1. The frontmatter field disables
  automatic injection of all platform-provided context. The post distinguishes
  three context types suppressed: AGENTS.md (GitHub Copilot), user instructions
  (Copilot), and CLAUDE.md memory files (Claude).
- **Confidence**: emerging (feature shipped and documented; production adoption
  and operational semantics — whether it also suppresses workflow-level
  instructions — are not fully specified)
- **Quote**: (no direct quote; post describes `engine.bare: true` as suppressing
  automatic context loading of AGENTS.md/user instructions/CLAUDE.md)
- **Our assessment**: This is the most architecturally significant new primitive
  in the release cycle. Every prior gh-aw release assumed that platform context
  (AGENTS.md, CLAUDE.md, user instructions) was always injected. `engine.bare`
  breaks that assumption intentionally: operators can now run an agent with
  zero implicit context, receiving only the explicit inputs the harness provides.
  This has two important use cases: (a) reproducibility — a bare run is not
  influenced by context files that may have changed between runs; (b) security
  — suppressing memory context prevents accumulated CLAUDE.md instructions from
  influencing agent behavior when the operator wants a fresh execution. For Ch02
  (Harness Engineering): `engine.bare` is a new harness control surface that
  should be documented alongside `min-integrity` as a way to narrow the agent's
  implicit trust surface.

### Claim 2: The `pre-steps` frontmatter field injects steps before checkout and the agent within the same job, solving token-minting cross-job masking

- **Evidence**: Shipped in v0.67.3. The post states `pre-steps` enables steps to
  run before checkout in the same job, and specifically recommends this for
  `actions/create-github-app-token` and `octo-sts` because "tokens stay in-job
  and never get masked crossing job boundaries."
- **Confidence**: emerging (feature shipped with explicit recommended use case;
  the token-masking behavior across jobs is a documented GitHub Actions
  characteristic, making this claim structurally well-founded)
- **Quote**: (post describes `pre-steps` as recommended for token-minting actions
  "because tokens stay in-job and never get masked crossing job boundaries")
- **Our assessment**: The cross-job token masking problem is real: when a token is
  minted in Job A and passed as an output to Job B, GitHub Actions masks the
  value in Job B's logs as a security measure, which can cause unexpected
  authentication failures if the token value needs to appear in downstream tool
  invocations. `pre-steps` solves this by keeping the token mint and agent
  execution in a single job context. For Ch02 (Harness Engineering): token-minting
  patterns that require cross-job handoff should be refactored to `pre-steps`.
  For Ch03 (Safety and Verification): the fact that `pre-steps` bypasses masking
  is intentional — teams adopting this pattern should validate that their token
  scope is appropriately narrow, since the in-job tokens have reduced masking
  protection from the harness.

### Claim 3: `agent-stdio.log` is now pre-created with 0600 permissions before `tee` writes, preventing world-readable exposure of MCP gateway bearer tokens

- **Evidence**: Shipped in v0.68.1, associated with PR #25689 area. The post
  explicitly identifies the protected content: "MCP gateway bearer tokens." The
  protection mechanism is pre-creation with restrictive permissions rather than
  post-write chmod, eliminating the race window.
- **Confidence**: emerging (the mechanism and motivation are stated; the
  prior vulnerability window — between file creation and first write — is
  implicit but structurally sound)
- **Quote**: "Agent stdio log files now pre-created with 0600 permissions before
  writing, preventing world-readable exposure of MCP gateway bearer tokens"
- **Our assessment**: Shared runner environments are common in GitHub Actions.
  If `agent-stdio.log` were created world-readable and then received bearer
  token writes, any concurrent process on the runner (or a subsequent run with
  a dirty workspace) could read the credential. Pre-creation at 0600 is the
  correct pattern: it eliminates the race window between file creation and
  permission set. This is the first explicit log-file permission claim for MCP
  bearer token protection in the corpus. For Ch03 (Safety and Verification):
  any log pipeline that captures agent I/O should use pre-created restricted
  files, not post-write chmod. The MCP gateway token is a high-value credential;
  the protection must precede the write, not follow it.

### Claim 4: `ValidateHeredocContent` now validates five user-controlled heredoc insertion sites, closing a class of prompt- and command-injection vectors

- **Evidence**: PR #25510, shipped in v0.68.0. The claim is specific: five
  insertion sites are validated. The post frames this as closing "a class of
  prompt/command injection vectors" — not a single bug but a category.
- **Confidence**: emerging (shipped feature; the five specific insertion sites
  are not enumerated by name in the post, so the complete coverage cannot be
  independently verified from the changelog alone)
- **Quote**: "Heredoc content validation across five user-controlled insertion
  sites (PR #25510) — closes a class of prompt/command injection vectors"
- **Our assessment**: Heredoc blocks in shell scripts are a well-known injection
  surface: if user-controlled content (e.g., a PR title, issue body, or agent
  output) is interpolated into a heredoc that becomes a command, an attacker can
  break out of the heredoc and inject arbitrary shell commands. Validating at
  five sites suggests the gh-aw compiler's injection surface was non-trivial —
  this is not one use case but a category with multiple manifestations. For Ch03:
  any harness that constructs shell commands or heredoc blocks from agent outputs
  or user-controlled inputs should enumerate its injection surfaces explicitly.
  The gh-aw approach (compile-time validation at known sites) is the correct model
  over runtime sanitization.

### Claim 5: Cross-job OpenTelemetry parent span IDs now propagate through `aw_context`, enabling end-to-end distributed trace visibility for multi-job workflows

- **Evidence**: PR #25540, shipped in v0.68.0. Parent span IDs propagate through
  the `aw_context` mechanism across job boundaries. Named compatible backends:
  Tempo, Honeycomb, Datadog. The post describes this as enabling "end-to-end
  distributed trace visibility for multi-job workflows."
- **Confidence**: emerging (feature shipped and described; how `aw_context` passes
  span IDs across jobs — as environment variables, outputs, or a dedicated artifact
  — is not specified in the changelog)
- **Quote**: "Parent span IDs propagate through `aw_context` across jobs (v0.68.0,
  #25540) — delivers end-to-end distributed trace visibility for multi-job
  workflows in Tempo, Honeycomb, Datadog"
- **Our assessment**: The April 6 release (blog-ghaw-weekly-2026-04-06.md Claim 1)
  shipped OTLP tracing with cross-job correlation based on job-level spans. The
  missing piece was parent span propagation: without it, each job's trace was a
  root trace, producing disconnected telemetry that couldn't be unified into a
  single end-to-end view. This release closes that gap. Together, the two releases
  deliver a complete distributed tracing implementation for multi-job agentic
  workflows: structured spans (April 6) + hierarchical parent-child linking
  (April 13). For Ch04 (Multi-agent orchestration): cross-job trace hierarchy is
  the prerequisite for attributing latency and cost to specific pipeline stages in
  multi-job agent workflows.

### Claim 6: OTel exception span events now emit `exception.type` alongside `exception.message`, making individual error attributes queryable without parsing pipe-delimited strings

- **Evidence**: PR #25914 and PR #25972 (both in-flight/just merged). The posts
  describe `exception.type` added alongside `exception.message`, with "individual
  error attributes queryable."
- **Confidence**: emerging (PRs described as just-merged; the prior state — pipe-
  delimited strings requiring parsing — is the implicit before-picture)
- **Quote**: "OTel exception span events now emit `exception.type` alongside
  `exception.message`; individual error attributes queryable (#25914+#25972)"
- **Our assessment**: Structured exception data is a significant quality-of-life
  improvement for Grafana/Honeycomb dashboards. Before this change, error
  classification required parsing a combined string; after, `exception.type` is
  a first-class filterable attribute. For Ch04: when designing OTel instrumentation
  for agentic workflows, prefer typed attributes over concatenated strings for any
  field that will be used in dashboard filtering or alerting.

### Claim 7: The `push_repo_memory` step ran on every bot-triggered no-op because `always()` bypassed skip propagation — a confirmed footgun in GitHub Actions conditional logic for agent memory persistence

- **Evidence**: PR #25960. The bug is specific: the `always()` condition that was
  intended to ensure memory is always saved bypassed the skip propagation that
  would have suppressed the step on bot-triggered no-ops (events where no
  meaningful work was done). The post describes this as a bug that has been fixed.
- **Confidence**: settled (the bug is fixed in a named PR; the mechanism —
  `always()` bypassing skip propagation — is a documented GitHub Actions behavior)
- **Quote**: "Fixed bug where `push_repo_memory` would run on bot-triggered no-ops
  due to `always()` bypassing skip propagation (#25960)"
- **Our assessment**: `always()` in GitHub Actions evaluates to true regardless
  of prior step outcomes, including when a previous step has set its output to
  indicate the job should skip. This is correct behavior for teardown and cleanup
  steps (always clean up, even after failure), but a footgun for conditional steps
  like memory persistence (only save if meaningful work was done). The gh-aw team
  hit this bug in production: every bot-triggered run that produced no output still
  persisted memory. For Ch02 (Harness Engineering): `always()` should not be used
  for agent output persistence steps unless the intent is truly unconditional.
  Use `success()` or explicit output-conditional logic instead. This is the first
  `always()` footgun documented in the agentic CI corpus.

### Claim 8: `gh aw compile --validate` output is now sanitized before embedding in issue bodies, closing a Markdown injection vector

- **Evidence**: PR #25971. The compile tool's validation output was previously
  embedded directly into GitHub issue bodies, which allowed a maliciously crafted
  workflow file to inject Markdown (headings, links, formatted content) into the
  validation failure issue. The fix sanitizes the subprocess output before embedding.
- **Confidence**: emerging (the vulnerability class — injecting Markdown via
  tool output that surfaces in issue bodies — is well understood; the specific
  fix is described)
- **Quote**: "Raw subprocess output from `gh aw compile --validate` sanitized
  before embedding into issue bodies, closing Markdown injection vector"
- **Our assessment**: This is the second "agent output as untrusted input"
  security fix in this release cycle (after heredoc validation in Claim 4). The
  pattern: a component in the gh-aw toolchain produces output that is subsequently
  embedded in a user-visible context (an issue body, a comment, a heredoc) without
  sanitization — and that output can be influenced by an attacker who controls the
  input to the component (a workflow file, an issue title, a PR description). For
  Ch03: any harness pipeline that embeds tool or subprocess output into GitHub
  issue bodies, PR comments, or other user-visible contexts should sanitize that
  output for the target rendering format.

### Claim 9: Copilot CLI v1.0.22 caused workflows to hang indefinitely or produce zero-byte output; the fix was pinning back to v1.0.21 — the first explicit engine-version pinning regression in the corpus

- **Evidence**: PR #25689, shipped in v0.68.1 as a critical fix. The regression
  was introduced by a Copilot CLI version bump. The fix is a pin back to the
  last known-good version (v1.0.21).
- **Confidence**: settled (the regression, its symptoms, the fix, and the PR are
  all documented; the hang-or-zero-byte symptom is specific and unambiguous)
- **Quote**: "Workflows using the Copilot engine were hanging indefinitely or
  producing zero-byte output due to an incompatibility introduced in v1.0.22 of
  the Copilot CLI" (PR #25689)
- **Our assessment**: This is the clearest argument yet for pinning AI engine
  versions in harness configurations. The Copilot CLI v1.0.22 change produced a
  failure mode (hang or zero-byte output) that would be nearly impossible to
  diagnose without knowing that a version bump had occurred. Teams using
  auto-updated CLI versions would see all their agentic workflows fail silently
  with no indication that a tool version change was the cause. For Ch02: engine
  version pinning should be a mandatory harness configuration item, not an
  afterthought. The failure pattern (hang vs. error) makes this especially
  dangerous: a hanging workflow consumes runner time and quota while producing no
  signal.

### Claim 10: `auto-triage-issues` achieved 100% label coverage with near-real-time labeling and correctly applied four labels in a single pass

- **Evidence**: "Agent of the Week" spotlight. The April 13 scan reported "exactly
  zero unlabeled issues" (100% label coverage rate). The April 12 run applied four
  labels (`enhancement`, `mcp`, `compiler`, `security`) in a single pass. The post
  recommends pairing with label-based notification rules.
- **Confidence**: anecdotal (one agent, one week's data; no rejection analysis, no
  description of cases where labels were incorrect or disputed)
- **Quote**: "reporting a 100% label coverage rate" and "correctly applied four
  labels (enhancement, mcp, compiler, security) in a single pass on April 12"
- **Our assessment**: 100% label coverage is a meaningful operational metric for
  a triage agent: it confirms every new issue received at least one label, which
  is the precondition for label-based routing to work. The four-label single-pass
  result demonstrates multi-label classification is working. However, accuracy (are
  the labels correct?) is not reported — only coverage (did labels get applied?).
  For Ch04: triage agents should be evaluated on coverage AND accuracy; a 100%
  coverage rate with 20% incorrect labels is worse than 90% coverage with 95%
  accuracy. The recommendation to pair with label-based notifications is the correct
  activation pattern: labels are only valuable if they trigger action.

### Claim 11: Five new gh-aw workflow templates cover code quality and architectural governance agent patterns

- **Evidence**: Five templates shipped in v0.67.4: `approach-validator` (PR
  #25354), `test-quality-sentinel` (PR #25353), `refactoring-cadence` (PR #25352),
  `architecture-guardian` (PR #25334), `design-decision-gate` (PR #25323).
- **Confidence**: settled (templates are shipped with specific PR numbers)
- **Quote**: (no direct quote; templates listed by name and PR number)
- **Our assessment**: The five templates extend the gh-aw template library from
  release automation (changeset, daily-updater) and triage (auto-triage-issues,
  contribution-check) into a new category: architectural governance. An
  `architecture-guardian` and `design-decision-gate` agent presuppose that the
  codebase has documented architectural decisions (ADRs or similar) that an agent
  can validate new work against. For Ch02: these templates are evidence that
  agentic harnesses are maturing from automating routine tasks (triage, dependency
  updates) to enforcing design intent — which requires a higher-quality AGENTS.md /
  CLAUDE.md that encodes the architectural constraints the governance agents enforce.

### Claim 12: Stale lock file diagnostics now emit `[hash-debug]` log lines on hash mismatch, with actionable issue creation

- **Evidence**: PR #25571, shipped in v0.68.1. The log format is specific:
  `[hash-debug]` prefixed lines at the step level on hash mismatch. The post
  mentions "actionable issue creation" but does not describe the issue template.
- **Confidence**: emerging (feature shipped with specific log format described)
- **Quote**: "Improved stale lock file diagnostics with `[hash-debug]` log lines"
- **Our assessment**: Lock file staleness is a recurring operational issue in
  gh-aw deployments (the compile/push model means lock files can drift from spec
  files if a spec is edited without recompiling). `[hash-debug]` logging gives
  operators a specific log pattern to grep for when investigating compile mismatch
  failures. For Ch02: lock file diagnostic patterns should be documented in runbook
  templates alongside the `gh aw compile` workflow — operators should know to look
  for `[hash-debug]` lines when diagnosing unexpected compilation failures.

## Concrete Artifacts

### Version Summary: v0.67.2–v0.68.1 (April 6–10, 2026)

```
v0.68.1 (April 10) — Critical Hotfix + Context Control + Security:
  - CRITICAL FIX: Copilot CLI pinned back to v1.0.21 (v1.0.22 caused hangs /
    zero-byte output, PR #25689)
  - New: engine.bare frontmatter field — suppresses AGENTS.md, user instructions,
         CLAUDE.md memory files (PR #25661)
  - New: stale lock file diagnostics with [hash-debug] log lines (PR #25571)
  - New: actions/github-script v9 with built-in getOctokit (PR #25553)
  - New: squash-merge fallback in gh aw add (PR #25609)
  - Security: agent-stdio.log pre-created at 0600 before tee writes

v0.68.0 (April 10) — OTel Cross-Job Tracing + Security Validation:
  - New: parent span ID propagation through aw_context across jobs (PR #25540)
  - Breaking: add-comment.discussion boolean removed → discussions: true/false
              (migration: gh aw fix --write, PR #25532)
  - Security: ValidateHeredocContent at five user-controlled insertion sites
              (PR #25510)

v0.67.4 (April 9) — Governance Agent Templates:
  - New templates: approach-validator (#25354), test-quality-sentinel (#25353),
    refactoring-cadence (#25352), architecture-guardian (#25334),
    design-decision-gate (#25323)
  - New: Copilot driver retry logic; --runner-guard compilation flag

v0.67.3 (April 8) — Token-Minting Pattern:
  - New: pre-steps frontmatter field — inject steps before checkout in same job
    (prevents cross-job token masking for octo-sts / create-github-app-token)
  - New: ${{ github.aw.import-inputs.* }} expression in imports
  - New: assignees support on create-pull-request fallback issues

v0.67.2 (April 6) — Reliability:
  - Cross-repo workflow hash checks
  - Checkout tokens no longer silently dropped on newer runners
  - curl/wget flag-bearing invocations allowed in network.allowed workflows
  - timeout-minutes schema capped at 360 minutes
```

### `engine.bare` — Clean-Slate Context Suppression

```yaml
# In a gh-aw workflow spec (.md frontmatter):
engine:
  bare: true
  # Effect: suppresses ALL automatic context loading:
  #   - AGENTS.md (GitHub Copilot agent instructions)
  #   - User instructions (Copilot user-level config)
  #   - CLAUDE.md memory files (Claude engine)
  # Use case: reproducible / context-isolated agent runs
  # PR #25661, v0.68.1
```

### `pre-steps` — In-Job Token Minting

```yaml
# In a gh-aw workflow spec (.md frontmatter):
pre-steps:
  - name: Mint GitHub App token
    uses: actions/create-github-app-token@v1
    id: app-token
    with:
      app-id: ${{ vars.APP_ID }}
      private-key: ${{ secrets.PRIVATE_KEY }}
  # Steps run before checkout and agent, within the SAME job.
  # Token value never crosses a job boundary → no GitHub Actions masking issue.
  # Use for: octo-sts, create-github-app-token, any in-repo credential mint.
  # v0.67.3
```

### Log-File Permission Hardening Pattern

```bash
# gh-aw now does this before starting tee:
touch agent-stdio.log
chmod 0600 agent-stdio.log
# Then:
agent-process 2>&1 | tee agent-stdio.log

# Why: if agent-stdio.log is created by tee (default behavior), it
# inherits the process umask (often 0644 = world-readable). MCP gateway
# bearer tokens appear in stdio during agent initialization. Pre-creating
# at 0600 eliminates the race window between creation and permission set.
```

### `always()` Footgun — Conditional Memory Persistence

```yaml
# WRONG: always() bypasses skip propagation
- name: Push repo memory
  if: always()   # ← runs even on bot-triggered no-ops
  run: gh aw push-memory

# RIGHT: only save on successful meaningful work
- name: Push repo memory
  if: success() && steps.agent.outputs.did_work == 'true'
  run: gh aw push-memory

# Bug: PR #25960 — push_repo_memory ran on every bot-triggered event because
# always() does not respect the skip propagation that gh-aw sets when an
# event produces no meaningful agent work.
```

### `discussions:` Migration (Breaking Change v0.68.0)

```yaml
# Before (v0.67.x and earlier):
add-comment:
  discussion: true   # deprecated boolean

# After (v0.68.0+):
add-comment:
  discussions: true  # or false

# Migration command: gh aw fix --write
# PR #25532
```

### Agent of the Week: auto-triage-issues Performance Data

```
Agent:      auto-triage-issues
Function:   Applies labels to new issues
Period:     Week of April 13, 2026

April 13 scan:  0 unlabeled issues found → 100% label coverage
April 12 run:   4 labels applied in single pass:
                  - enhancement
                  - mcp
                  - compiler
                  - security

Note: coverage metric (were labels applied?) reported;
      accuracy metric (were labels correct?) not reported.
Recommendation: pair with label-based notification rules for team alerting.
```

## Cross-References

- **Corroborates**:
  - `blog-ghaw-weekly-2026-03-23.md` Claim 5 (GitHub App auth exemption gap on
    public repos closed by PR #21969): The `agent-stdio.log` 0600 hardening (Claim
    3 here) is a further instance of the same security posture — closing gaps where
    credential material was accessible beyond its intended audience. March 23 closed
    a policy-level gap; April 13 closes a log-file permission gap. Both reflect a
    pattern of tightening credential exposure surface in the gh-aw platform.
  - `blog-ghaw-weekly-2026-04-06.md` Claim 6 (422 `${{ secrets.* }}` migrations
    from `run:` to `env:`): The Markdown injection fix (PR #25971, Claim 8 here)
    is another instance of the same pattern: agent or tool output embedded in a
    user-visible context without sanitization. March 31–April 6: secrets as
    injection surface in `run:` blocks. April 6–10: subprocess output as injection
    surface in issue bodies. Together they document a systematic "agent output as
    untrusted input" hardening campaign across the gh-aw codebase.
  - `blog-ghaw-agent-observability.md` Claim 4 ("chatty LLM calling invisible
    without instrumentation"): The `auto-triage-issues` 100% coverage rate (Claim
    10) is a positive performance data point for a deployed triage agent, but the
    missing accuracy metric illustrates the same principle inversely: you cannot
    evaluate an agent's quality on coverage alone; instrumentation must capture
    the right metric.

- **Extends**:
  - `blog-ghaw-weekly-2026-04-06.md` Claim 1 (OTLP tracing via
    `observability.otlp` frontmatter, cross-job job-level spans): The parent span
    ID propagation through `aw_context` (Claim 5 here) is the missing link that
    completes the April 6 OTel implementation. April 6 delivered span structure
    within jobs; April 13 delivers span hierarchy across jobs. Together: complete
    distributed tracing for multi-job agentic pipelines.
  - `blog-ghaw-weekly-2026-04-06.md` Claim 9 (agentic-observability-kit meta-
    monitoring failure, token-limit errors): PR #25914 + #25972 OTel exception
    span improvements (Claim 6 here) directly improve the diagnostic quality
    available when monitoring agents hit errors like the token-limit failure in
    that Claim 9. Queryable `exception.type` replaces parsed pipe-delimited strings.
  - `blog-ghaw-weekly-2026-03-23.md` Claim 7 (lock file embed of agent ID/model
    in gh-aw-metadata v3): Stale lock file diagnostics with `[hash-debug]` (Claim
    12 here) extend the lock file model's operational story. March 23: what the
    lock file contains. April 13: how to diagnose when the lock file is stale.
  - `blog-gh-aw-operations-release-workflows.md` Claim 4 (`gh aw compile` lock
    file model): The `engine.bare` field (Claim 1) is a new harness control that
    sits alongside the compile model — it affects what the compiled harness
    injects at runtime, not the compilation step itself. Together: the compile
    model governs what executes; `engine.bare` governs what context it receives.

- **Contradicts**: None. No existing source note makes claims opposed by this
  release. The `always()` footgun (Claim 7) is a new operational finding with no
  prior source note recommending `always()` for agent memory persistence. The
  Copilot CLI version pinning failure (Claim 9) reinforces rather than contradicts
  existing harness engineering guidance favoring pinned dependencies.

- **Novel**:
  - **`engine.bare` clean-slate context control** (Claim 1): First documented
    primitive for explicitly suppressing all platform-provided context (AGENTS.md,
    CLAUDE.md, user instructions) in the corpus. No prior source covers intentional
    blank-slate agent execution.
  - **`pre-steps` in-job token-minting pattern** (Claim 2): First coverage in the
    corpus of a harness pattern specifically designed to avoid cross-job token
    masking. Prior notes cover token scoping and credential management in general;
    this is the first concrete GitHub Actions workaround for the masking behavior.
  - **Log-file permission hardening for MCP bearer tokens** (Claim 3): First
    explicit log-file permission claim for MCP credential protection in the corpus.
    No prior note covers pre-creation permission hardening as a credential
    protection technique.
  - **Heredoc injection-site enumeration** (Claim 4): First corpus source to
    document specific injection-site count (five) for a harness injection validation.
    Prior sources describe injection risk in general; this is the first with a
    concrete site count.
  - **`always()` footgun for agent memory persistence** (Claim 7): First corpus
    source to document `always()` as a conditional logic footgun in agentic CI.
    GitHub Actions `always()` semantics are documented elsewhere but their
    interaction with gh-aw skip propagation is new.
  - **Copilot CLI version pinning regression** (Claim 9): First explicit engine-
    version pinning failure + hotfix in the corpus. Prior notes recommend pinning
    in principle; this is the first concrete failure case demonstrating why.
  - **Architectural governance templates** (Claim 11): `architecture-guardian` and
    `design-decision-gate` are the first documented examples of governance-agent
    templates in the corpus, extending agentic automation from task execution to
    design intent enforcement.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add `engine.bare: true` as a named harness control for reproducible, context-
    isolated agent runs. Frame alongside `min-integrity` as a "narrowing" primitive:
    `min-integrity` controls what the agent can *do*; `engine.bare` controls what
    context it *receives*. Both are relevant for security-sensitive or reproducibility-
    critical workflows. Reference PR #25661 / v0.68.1.
  - Add `pre-steps` as the recommended pattern for in-job token minting when using
    `actions/create-github-app-token` or `octo-sts`. Document the cross-job token
    masking problem it solves. Reference v0.67.3.
  - Add explicit engine version pinning as a mandatory harness configuration rule,
    citing the Copilot CLI v1.0.22 regression (Claim 9) as the concrete failure
    case. The hang-or-zero-byte symptom makes unpinned engine versions a silent
    failure risk, not a detectable error.
  - Add `[hash-debug]` as the diagnostic log pattern for stale lock file
    investigation. Include in runbook guidance alongside `gh aw compile`.
  - Add `always()` as a conditional logic footgun for agent output persistence
    steps (Claim 7). Recommend `success()` or output-conditional logic instead.

- **Chapter 03 (Safety and Verification)**:
  - Add log-file pre-creation at 0600 as a required practice for any agent log
    pipeline that captures MCP gateway bearer tokens or other credentials. The
    race window between file creation and permission set is the vulnerability;
    pre-creation eliminates it. Reference the gh-aw `agent-stdio.log` pattern.
  - Add heredoc injection-site audit as a named security practice for harness
    engineers. Any harness that constructs heredoc blocks from user-controlled
    or agent-produced inputs should enumerate and validate each insertion site.
    Cite the five-site count from `ValidateHeredocContent` (PR #25510) as a
    concrete production example.
  - Add "agent/tool output as untrusted input" as a named security pattern, with
    two concrete gh-aw examples: (a) heredoc injection (PR #25510); (b) Markdown
    injection in issue bodies from compile validation output (PR #25971). Any
    harness that embeds tool output in user-visible contexts should sanitize for
    the target format.
  - Note the `pre-steps` credential scope consideration (Claim 2): in-job tokens
    have reduced masking protection; harness designs using `pre-steps` should
    validate that token scope is appropriately narrow.

- **Chapter 04 (Multi-agent orchestration)**:
  - Update OTel distributed tracing guidance: cross-job parent span propagation
    via `aw_context` (Claim 5) completes the trace hierarchy. The full picture
    (from blog-ghaw-weekly-2026-04-06.md + this note): `observability.otlp`
    frontmatter block (April 6) + cross-job parent span propagation (April 13) =
    complete end-to-end distributed tracing for multi-job agentic pipelines.
  - Add queryable exception attributes (`exception.type` as distinct from
    `exception.message`, Claim 6) as a recommended OTel instrumentation pattern.
    Prefer typed attributes over concatenated strings for any field used in
    dashboard filtering or alerting.
  - Add `auto-triage-issues` 100% coverage result as a concrete triage-agent
    data point (Claim 10). Pair with the missing accuracy metric as a reminder
    that coverage is a necessary but not sufficient quality signal for
    classification agents.

## Extraction Notes

1. **Source depth**: The weekly update is a changelog post covering five releases
   across ~700–900 words. The "Agent of the Week" section (auto-triage-issues) is
   brief; the release notes are structured bullet summaries. Twelve claims were
   extracted; no extractable content was skipped.
2. **Prospector triage cross-check**: Three concurrent Prospector triage comments
   on this issue — each independently identified the same six high-signal patterns
   (`engine.bare`, `pre-steps`, OTel cross-job, security hardening cluster,
   Copilot CLI regression, `always()` footgun). The convergence across three
   independent triage passes increases confidence in claim selection.
3. **In-flight PRs**: PR #25923 (image artifact Markdown embedding with
   `skip-archive: true`), PR #25908 (`cleanup-cache-memory` scheduled job), PR
   #25914 + #25972 (OTel exception span events) are listed as "notable merged PRs
   beyond releases" — they were merged but may not be in a tagged release as of
   April 13. Treated as emerging/in-progress; confidence marked accordingly.
4. **`engine.bare` operational scope**: The post does not clarify whether `bare: true`
   suppresses only the automatic platform context or also explicit context passed
   via the workflow frontmatter. Extraction is limited to the described behavior
   (AGENTS.md / user instructions / CLAUDE.md); any broader interpretation should
   be verified against gh-aw documentation.
5. **No contradictions filed**: Reviewed all existing source notes in the corpus.
   No existing claim materially opposes any claim in this source. The `always()`
   footgun (Claim 7) and the Copilot CLI regression (Claim 9) are additive
   findings with no corpus counterparts.
