---
source_url: https://github.github.com/gh-aw/blog/2026-09-01-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – September 1, 2026: PR Sous Chef"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-09-01
date_extracted: 2026-09-02
last_checked: 2026-09-02
status: current
confidence_overall: settled
issue: "#3160"
---

# Agent of the Day – September 1, 2026: PR Sous Chef

> Twelfth entry in the "Agent of the Day" series — profiles PR Sous Chef, a
> hybrid schedule+slash-command `gh-aw` workflow that checks in on every
> open, non-draft `github/gh-aw` PR every 15 minutes and posts a targeted
> `@copilot` nudge only when a PR has genuinely stalled (merge conflict,
> zero-diff staleness, unresolved-but-answered review threads, or failed
> checks), rather than commenting on every PR every cycle. The blog post's
> ~350-word description was substantially extended by fetching the live
> workflow definition (`.github/workflows/pr-sous-chef.md`, 554 lines),
> which surfaces the exact prefilter/cooldown/priority mechanics, an inline
> `pr-processor` sub-agent, and an active A/B experiment not mentioned in
> the blog post at all.

## Source Context

- **Type**: blog-post (twelfth "Agent of the Day" entry from the official
  GitHub Agentic Workflows blog, bylined "Copilot" — the same recurring
  gh-aw convention documented across this series, e.g.
  `blog-ghaw-agent-of-the-day-2026-08-28.md`. One agent profiled per post,
  distinct from the weekly changelog format.)
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team. The post links two specific,
  independently-checkable GitHub Actions run IDs (33509763563, 33516358980).
  This note additionally fetched and read the live workflow definition in
  full (`raw.githubusercontent.com/github/gh-aw/main/.github/workflows/pr-sous-chef.md`,
  554 lines, via `curl`) and confirmed run 33516358980's basic metadata
  (event: `schedule`, conclusion: `success`, created `2026-09-01T13:55:45Z`,
  completed `2026-09-01T14:07:01Z`, ~11 minutes) directly against the GitHub
  REST API (`api.github.com/repos/github/gh-aw/actions/runs/33516358980`).
  The blog's qualitative description of the workflow's restraint and
  mechanics is corroborated in detail by the live source, which additionally
  surfaces mechanics (the exact prefilter logic, the inline `pr-processor`
  sub-agent, the active A/B experiment, and the full safe-outputs guardrail
  set) not mentioned in the blog post's own text at all.
- **Scope**: One short post (~350 words) describing the workflow's mission,
  its engine/trigger configuration, one day's aggregate metrics (five runs),
  a summary quality-grader result, and a one-paragraph "restraint" framing.
  Does NOT cover: the prefilter script's exact skip conditions, the
  `pr-processor` sub-agent, the safe-outputs configuration (comment/approve/
  resolve-thread/dismiss-review/update-PR/push/create-issue), the active
  `remove_redundant_context_v1` experiment, or the protected-file exclusion
  list — all of which exist in the live workflow file and were recovered by
  this note via a direct source-file fetch.

## Extracted Claims

### Claim 1: PR Sous Chef runs on the `pi` engine with `openai/gpt-5.4`, triggered on a 15-minute schedule plus an on-demand `/souschef` slash command, fetching all open PR branches and deciding whether a targeted nudge is warranted before posting a Copilot request

- **Evidence**: Direct first-party description in the post's second
  paragraph; corroborated exactly by the live workflow's frontmatter
  (`engine: {id: pi, model-provider: openai}`, `model: openai/gpt-5.4`,
  `on: {schedule: every 15m, slash_command: {name: souschef, events:
  [pull_request_comment]}}`, `checkout: {fetch: ["refs/pulls/open/*"]}`).
- **Confidence**: settled (blog claim directly confirmed by the fetched
  first-party workflow source)
- **Quote**: "PR Sous Chef runs on the `pi` engine with `openai/gpt-5.4`,
  triggered on a tight `every 15m` schedule plus an on-demand `/souschef`
  slash command for anyone who wants to pull it into a specific PR
  conversation. It fetches all open PR branches (`refs/pulls/open/*`), reads
  through PR state, checks, and comments, and decides whether a targeted
  nudge is warranted — then posts a Copilot request if so."
- **Our assessment**: This is the series' first entry to combine a
  sub-hourly (15-minute) schedule with a slash-command trigger on the same
  workflow — Issue Monster (`blog-ghaw-agent-of-the-day-2026-08-25.md` Claim
  1) runs a comparable 30-minute schedule but has no slash-command trigger,
  and Q (`blog-ghaw-agent-of-the-day-2026-08-24.md` Claim 1) is
  slash-command-only with no schedule at all. For Ch02 (Harness
  Engineering): "hybrid schedule + slash-command trigger" is a distinct
  trigger combination from either pure-scheduled or pure-on-demand agents
  documented elsewhere in this series — the schedule handles routine sweep
  coverage while the slash command lets a human pull the same agent into a
  specific PR outside its normal cadence.

### Claim 2: Across five runs in a single afternoon on September 1, the workflow completed successfully every time, generated 20 safe-output items combined with zero errors and zero warnings, ranging from a single-item quiet pass to busier sweeps of eight or nine actions

- **Evidence**: Direct aggregate metrics statement in the post, naming two
  specific linked Actions runs as examples; run 33516358980's basic metadata
  (event `schedule`, conclusion `success`, ~11-minute duration) was
  independently confirmed against the GitHub REST API by this note.
- **Confidence**: settled (specific aggregate figures tied to two
  individually linked, independently-checkable Actions runs, one of which
  was directly spot-checked by this note)
- **Quote**: "Recent runs on September 1 show the pattern clearly: five runs
  in a single afternoon, all completed successfully, ranging from quiet
  passes with a single safe item to busier sweeps producing eight or nine
  actions each — see run #33509763563 and run #33516358980. Across its last
  five runs combined, it generated 20 safe-output items with zero errors and
  zero warnings — a workflow that does its job and gets out of the way."
- **Our assessment**: 20 safe-output items across five runs (~4/run average)
  at a 15-minute cadence (up to 96 possible runs/day) is a materially lighter
  per-run output volume than Issue Monster's ~25 API calls/run at a
  30-minute cadence (`blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 4),
  though the two metrics are not directly comparable (safe-output items vs.
  API calls). The live workflow's own hard cap — "Process at most 4 nudges
  per run" (Concrete Artifacts → Workflow Prompt Body) — mechanically bounds
  the nudge-comment portion of this count regardless of queue size, which is
  a harness-level explanation for why per-run output stays low even at a
  15-minute cadence.

### Claim 3: The audit trail for the latest run showed all 13 automated quality graders passing clean, covering tool-success-rate (100%), loop detection (zero), and context-growth efficiency, with the sole flagged item being 5 of 53 outbound network calls blocked by firewall policy rather than a functional failure

- **Evidence**: Direct statement following the aggregate metrics, describing
  a specific run's grader results and one flagged network item; corroborated
  generically by `docs-ghaw-graders.md` Claim 3's documentation of ten
  reserved built-in grader IDs spanning tool-call quality and context-
  management health (this post's "13 out of 13" total exceeds the ten
  reserved built-ins, consistent with `docs-ghaw-graders.md` Claim 4's
  per-grader `enabled` overrides and Claim 9's shared preprocessing pass
  potentially producing additional sub-metrics not individually named here).
- **Confidence**: settled (specific grader-pass count and network-call ratio
  stated directly; the underlying grader taxonomy is independently
  documented in the corpus, though this post does not name which 13
  graders ran)
- **Quote**: "The audit trail on that latest run is worth a closer look: 13
  out of 13 automated quality graders passed clean, covering everything from
  tool-success-rate (100%) to loop detection (zero) to context-growth
  efficiency. The one flagged item was a handful of blocked outbound
  requests to `github.com:443` — five out of fifty-three total network
  calls — a firewall-policy nuance rather than a functional problem, since
  the run still completed successfully and produced its full set of nudges."
- **Our assessment**: This is a concrete, dated production instance of the
  grader system abstractly documented in `docs-ghaw-graders.md` (Claim 3's
  ten reserved built-in IDs) and corroborates that a workflow can pass all
  configured graders while still surfacing a secondary firewall/network
  signal worth noting in the report — the live workflow's own frontmatter
  confirms a `network: {allowed: ["defaults", "go"]}` allowlist (Concrete
  Artifacts → Workflow Frontmatter) that would plausibly account for
  blocked `github.com:443` calls made outside that allowlist (e.g., via
  `gh` CLI calls that bypass the declared network policy's expected path).
  The post does not confirm this mechanism explicitly, so this is offered as
  a plausible explanation, not a settled one. For Ch04 (Operations): "all
  graders pass, but network policy still flags a handful of blocked calls"
  is a useful example that grader-pass and network-policy-clean are
  separate signals — a fully green grader run does not imply zero
  firewall-policy friction.

### Claim 4: What the post frames as PR Sous Chef's defining property is restraint — most 15-minute cycles are pure read-only reconnaissance that finds nothing actionable, and the agent only steps in with a Copilot request when a PR has genuinely gone quiet, avoiding comment noise on PRs already progressing on their own

- **Evidence**: Direct editorial framing in the post's fourth paragraph,
  immediately following the grader/network discussion.
- **Confidence**: settled (explicit, first-party design-philosophy
  statement, though "restraint" itself is the author's characterization
  rather than a measured metric)
- **Quote**: "What makes PR Sous Chef worth watching is its restraint. It
  doesn’t comment on every PR every cycle; a 15-minute schedule paired with
  a handful of safe items per run means most cycles are pure read-only
  reconnaissance — checking state, finding nothing actionable, and moving
  on. Only when a PR has genuinely gone quiet does it step in with a
  Copilot request, keeping the review queue moving without adding comment
  noise to PRs that are already progressing fine on their own."
- **Our assessment**: This is the same "restraint is a feature, not a gap"
  principle already named for the Dead Code Removal Agent
  (`blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 4, declining to force a
  PR when cleanup can't complete cleanly) and echoed by Issue Monster's
  per-topic retry-exhaustion tracking (`blog-ghaw-agent-of-the-day-2026-08-25.md`
  Claim 8), now applied to a third distinct mechanism: a high-frequency
  (15-minute) scheduled monitor that is read-only the overwhelming majority
  of cycles by design, not by malfunction. The live workflow's own cooldown
  and duplicate-comment logic (Claim 5 below) is the concrete, mechanical
  implementation of this "restraint" the blog post only describes in prose.
  For Ch02 (Harness Engineering): "high-frequency scheduled monitor, mostly
  read-only by design" extends the corpus's restraint principle to the
  sub-hourly cadence range — a category not previously covered by this
  named principle, which so far has only been documented for daily-or-slower
  agents.

### Claim 5: The live workflow's prefilter step skips a candidate PR for any of three reasons — a check still pending and started less than 1 hour ago, the most recent comment already being an actionable sous-chef nudge, or a sous-chef nudge posted within the last 30 minutes (a cooldown) — with an explicit exception that a `CONFLICTING` merge state always overrides the duplicate-comment skip

- **Evidence**: Live workflow source, "Fetch open non-draft PR queue" step:
  `cooldown_seconds=1800`; the pending-checks filter ignores any check
  running longer than 1 hour (`$cutoff = now - 3600`); the "last comment is
  sous-chef" and cooldown checks both require the comment to contain both
  the `<!-- gh-aw-pr-sous-chef-nudge -->` marker AND `@copilot` to count
  (informational marker-only comments do not skip or trigger cooldown); and
  the explicit code comment/logic: `if [ "$last_comment_is_sous_chef" =
  "true" ] && [ "$merge_state_status" != "CONFLICTING" ]` — i.e., the skip
  is bypassed when the PR is in a `CONFLICTING` state.
- **Confidence**: settled (directly read from the first-party workflow
  source's prefilter shell script; not mentioned in the blog post at all)
- **Quote**: (no direct quote from the blog post — the blog post never
  describes the prefilter mechanics, cooldown duration, or the
  `CONFLICTING`-state exception; sourced from the live workflow file, cited
  by section name per MINER.md §4b: "Fetch open non-draft PR queue" step of
  `.github/workflows/pr-sous-chef.md`)
- **Our assessment**: This is the mechanical implementation underlying
  Claim 4's "restraint" framing, and it is entirely deterministic —
  implemented as bash/jq logic in a pre-agent step, not agent reasoning.
  This is a concrete production instance of the "deterministic
  pre-processing before the agent job" pattern documented generically in
  `docs-ghaw-deterministic-agentic-patterns.md` Claim 3 (`/tmp/gh-aw/agent/`
  as the designated data-exchange directory between deterministic
  pre-processing jobs and the AI agent) — the prefilter writes
  `pr-sous-chef-candidates-compact.json` to exactly that directory for the
  agent to read. The `CONFLICTING`-state override is a specific, notable
  design choice: the workflow's own duplicate-comment suppression (avoid
  nagging a PR twice in a row) is deliberately weaker than its
  merge-conflict-unblocking priority — a merge conflict is treated as
  urgent enough to warrant a repeat nudge even immediately after a prior
  one. For Ch02: document "cooldown/duplicate-suppression logic with an
  explicit override for higher-priority states" as a refinement of simple
  cooldown-gating — not all skip conditions should be equally weighted
  against every mutation trigger.

### Claim 6: Eligible PRs are prioritized in a fixed order — `CONFLICTING` merge state first, then PRs with zero file changes stalled for 24+ hours, then PRs with unresolved review threads that already have a follow-up response, then most-recently-updated — with ties broken by lower PR number for deterministic reruns, and the agent capped at 4 nudge comments per run

- **Evidence**: Live workflow source, "Token efficiency rules" section, item
  5: the four-tier priority list plus "If two PRs are still tied, prioritize
  the lower PR number first for deterministic behavior and stable reruns,"
  and item 4: "Process at most 4 nudges per run."
- **Confidence**: settled (directly read from the first-party workflow
  source's prompt body; not mentioned in the blog post, which does not
  describe any prioritization order or per-run cap)
- **Quote**: (no direct quote from the blog post — prioritization order and
  the 4-nudge cap are not mentioned in the blog text; sourced from the live
  workflow file, cited by section name per MINER.md §4b: "Token efficiency
  rules" section, item 5, of `.github/workflows/pr-sous-chef.md`)
- **Our assessment**: "Zero-diff stalled" (a PR open 24+ hours with no files
  changed) is a specific, checkable staleness signal not previously
  documented in the corpus's triage/monitoring agents — distinct from
  Issue Arborist's shared-run-ID linking signal
  (`blog-ghaw-agent-of-the-day-2026-08-20.md` Claim 3) or Issue Monster's
  peer-health content scan (`blog-ghaw-agent-of-the-day-2026-08-25.md`
  Claim 3), both of which detect different kinds of stalled/at-risk work.
  The deterministic lower-PR-number tiebreak is a small but concrete
  illustration of designing for stable, reproducible reruns — a scheduled
  agent that reruns every 15 minutes over a shifting PR queue needs a fully
  deterministic ordering or its behavior across consecutive runs becomes
  unpredictable to audit. For Ch02: add "zero-diff staleness" (opened, no
  files changed, N hours elapsed) as a named PR-health signal, alongside a
  fixed priority ladder (urgency class, then recency, then a deterministic
  tiebreak) as a reusable pattern for any agent processing a shared,
  frequently-rerun queue under a hard per-run action cap.

### Claim 7: The workflow delegates per-PR skip/nudge decisions to an inline `pr-processor` sub-agent running on `model: sonnet` — a different model and provider from the parent workflow's `openai/gpt-5.4` on the `pi` engine — capped at 8 tool calls per PR, returning compact JSON only

- **Evidence**: Live workflow source, `## agent: \`pr-processor\`` block:
  frontmatter `description: Processes one PR with minimal API calls and
  returns skip/nudge decisions`, `model: sonnet`; body: "Make at most 8 tool
  calls total. If 8 calls are insufficient to reach a confident decision,
  set all fields to `null` and set `skip_reason: "insufficient_context"`,"
  and "Keep output compact JSON only — a single object, no prose."
- **Confidence**: settled (directly read from the first-party workflow
  source's inline sub-agent block; not mentioned in the blog post at all)
- **Quote**: (no direct quote from the blog post — the `pr-processor`
  sub-agent is not mentioned in the blog text; sourced from the live
  workflow file, cited by section name per MINER.md §4b: `## agent:
  \`pr-processor\`` block of `.github/workflows/pr-sous-chef.md`)
- **Our assessment**: This is a concrete, named production instance of the
  inline sub-agent pattern documented in `docs-ghaw-inline-sub-agents.md`
  (Claim 1: `## agent: \`name\`` heading delimiters; Claim 4: `model`
  defaults to the parent's model but can be overridden as "the primary
  economic optimization lever for inline sub-agents"). Claim 4 of that
  reference note frames the pattern's canonical use case as same-provider
  cost tiering (its own example: parent on Claude Opus delegating to Claude
  Haiku); this workflow is the first corpus instance of a
  *cross-provider* override — an OpenAI-engine parent (`pi` /
  `openai/gpt-5.4`) delegating focused per-PR triage to an Anthropic model
  (`sonnet`) — extending that claim's documented lever to cross-provider
  model selection, not just cross-tier selection within one provider. The
  8-tool-call cap with an explicit `insufficient_context` bail-out is also a
  concrete, bounded-effort pattern: rather than letting a stuck sub-agent
  loop indefinitely on one PR, the harness caps its budget and requires it
  to report a specific failure reason rather than guessing. For Ch02: extend
  the inline-sub-agent "model as cost lever" guidance
  (`docs-ghaw-inline-sub-agents.md` Claim 4) with this cross-provider
  instance, and add "hard per-task tool-call cap with an explicit
  insufficient-context bail-out" as a reusable bounded-effort pattern for
  any sub-agent handling one item from a larger batch.

### Claim 8: The workflow's `safe-outputs` block composes seven distinct write-capable actions behind a shared `approval_allowlist` gate — `add-comment` (max 4), `approve-workflow-run` (max 8, restricted to three named CI workflow files and to PR numbers pre-approved by a separate deterministic job), `resolve-pull-request-review-thread` (max 40), `dismiss-pull-request-review` (max 20), `update-pull-request` (max 10, append-only body), `push-to-pull-request-branch` (max 10, with `README.md` and `.github/workflows/**` excluded), and `create-issue` (3-day expiry, grouped and deduplicated by day)

- **Evidence**: Live workflow source, `safe-outputs:` block in full
  (Concrete Artifacts), plus the `approval_allowlist` job that runs after
  the agent job and extracts `eligible_pull_request_numbers` from the
  prefilter's own compact JSON artifact, which `approve-workflow-run` then
  consumes via `allowed-pull-requests: ${{
  needs.approval_allowlist.outputs.eligible_pull_request_numbers }}`.
- **Confidence**: settled (directly read from the first-party workflow
  source's frontmatter; not mentioned in the blog post, which does not
  enumerate any of these seven action types or the two-stage approval gate)
- **Quote**: (no direct quote from the blog post — none of the seven
  safe-output types or the `approval_allowlist` gate are mentioned in the
  blog text; sourced from the live workflow file, cited by section name per
  MINER.md §4b: `safe-outputs:` block and `approval_allowlist:` job of
  `.github/workflows/pr-sous-chef.md`)
- **Our assessment**: This is by far the widest write-action surface
  documented for any single agent in this series to date — Issue Monster
  (`blog-ghaw-agent-of-the-day-2026-08-25.md`) uses two safe-output types
  (`assign-to-agent`, `add-comment`); Q (`blog-ghaw-agent-of-the-day-2026-08-24.md`
  Claim 7) uses one (`create-pull-request`) with three guardrails. PR Sous
  Chef combines seven, but layers two independent guardrail mechanisms not
  documented together elsewhere in the corpus: (1) the
  `approve-workflow-run` action is scoped twice — once by an
  `allowed-workflows` allowlist restricted to three specific CI files
  (`cjs.yml`, `cgo.yml`, `CWI.yml`), and again by an `allowed-pull-requests`
  list computed by a *separate, deterministic* job
  (`approval_allowlist`) that re-derives eligible PR numbers from the same
  prefilter artifact the agent read — meaning the agent cannot approve a
  workflow run for a PR it was never shown as eligible, even if it tried,
  because the safe-outputs processor enforces the allowlist independently
  of the agent's own output. This is a concrete, two-job instance of
  privilege separation beyond what a single `min-integrity`/`toolsets`
  scoping already provides (contrast with the single-job
  `min-integrity: approved` scoping documented for Issue Monster,
  `blog-ghaw-agent-of-the-day-2026-08-25.md` Concrete Artifacts). (2) the
  `push-to-pull-request-branch` action explicitly excludes
  `.github/workflows/**`, `README.md`, and
  `docs/src/content/docs/index.mdx` — corroborating, with a live named
  instance, the general protected-file category (CI/CD workflow files) in
  `docs-ghaw-threat-detection.md` Claim 10, and extending it with two
  specific non-CI files (top-level `README.md`, a docs index page) the
  workflow's own prompt separately explains are "primary project messaging
  that must only be changed by maintainers." For Ch03 (Safety and
  Verification): document "compute the write-scope allowlist in a separate
  deterministic job the agent cannot influence, then have the safe-outputs
  processor enforce it independently" as a stronger privilege-separation
  pattern than relying on the agent job's own tool/permission scoping
  alone — this is a second, cross-job layer on top of the
  agent-job-level restrictions the corpus has documented elsewhere.

### Claim 9: The workflow runs an active A/B experiment (`remove_redundant_context_v1`) testing whether removing a redundant "backup" skip-rules table from the main-agent prompt reduces execution duration without lowering eval pass rates, using a Mann-Whitney analysis with two named guardrail metrics and a minimum of 20 samples per variant

- **Evidence**: Live workflow source, `experiments:` block: `variants:
  [control, candidate]`, description explaining the redundant table is
  already "deterministically enforced by the fetch-prs prefilter step and
  re-verified by the pr-processor sub-agent," `hypothesis: "H0: No
  meaningful difference in execution-duration between control and
  candidate. H1: Removing the redundant backup skip-rules table decreases
  execution-duration without lowering the comment-added/pr-evaluated eval
  pass rate,"` `metric: "grader:execution-duration"`,
  `guardrail_metrics: [{name: "eval:comment-added", threshold: ">=0.90"},
  {name: "eval:pr-evaluated", threshold: ">=0.90"}]`, `min_samples: 20`,
  `analysis_type: mann_whitney`; the prompt body's
  `{{#if experiments.remove_redundant_context_v1 == 'control' }}...{{#endif}}`
  block conditionally includes a "Required skip rules per PR" backup table
  only in the `control` variant.
- **Confidence**: settled (directly read from the first-party workflow
  source's `experiments:` frontmatter and the conditional prompt block it
  gates; not mentioned in the blog post at all)
- **Quote**: (no direct quote from the blog post — the active experiment is
  not mentioned in the blog text; sourced from the live workflow file,
  cited by section name per MINER.md §4b: `experiments:` block and the
  `{{#if experiments.remove_redundant_context_v1 == 'control' }}` prompt
  section of `.github/workflows/pr-sous-chef.md`)
- **Our assessment**: This is a concrete, named production instance of the
  A/B testing mechanism documented in `docs-ghaw-practices-experiments.md`
  (Claim 1: named experiments with variant selection; Claim 3: `${{
  experiments.<name> }}` conditional syntax; Claim 9: `guardrail_metrics` as
  automated safeguards) and `docs-ghaw-graders.md` Claim 11 (experiment
  metrics referencing grader outputs via `grader:<id>`) — here
  `metric: "grader:execution-duration"` directly ties the experiment to one
  of the ten reserved built-in graders documented in `docs-ghaw-graders.md`
  Claim 3. The experiment's own stated rationale — the skip-rules table is
  "redundant context on every run" because the same three conditions are
  "already deterministically enforced by the fetch-prs prefilter step and
  re-verified by the pr-processor sub-agent" — is a specific, self-aware
  instance of a workflow author questioning whether a defensive
  belt-and-suspenders prompt section (documentation the agent doesn't
  strictly need, since the same logic already runs deterministically twice)
  is worth its token cost, tested empirically rather than removed on
  intuition alone. For Ch02/Ch04: this is a worked example of applying the
  `experiments` A/B-testing mechanism specifically to a context-trimming
  hypothesis (remove prompt content already enforced elsewhere in the
  pipeline) with dual eval-pass-rate guardrails preventing the optimization
  from silently degrading behavior — a concrete instance of "test whether
  defensive prompt redundancy is actually necessary" as an experiment
  design pattern.

## Concrete Artifacts

### PR Sous Chef: Workflow Frontmatter (excerpted, live source)

```yaml
name: PR Sous Chef
description: Keeps open non-draft PRs moving toward maintainer investigation by posting targeted Copilot nudges
on:
  schedule: every 15m
  workflow_dispatch:
  slash_command:
    strategy: centralized
    name: souschef
    events: [pull_request_comment]
  skip-if-no-match: "is:pr is:open -is:draft"
permissions:
  contents: read
  pull-requests: read
  issues: read
  actions: read
  copilot-requests: write
checkout:
  fetch: ["refs/pulls/open/*"]
  fetch-depth: 0
network:
  allowed: ["defaults", "go"]
model: openai/gpt-5.4
engine:
  id: pi
  model-provider: openai
strict: true
imports:
  - shared/mcp-pagination.md
  - shared/otlp.md
  - shared/graders.md
tools:
  cli-proxy: true
  github:
    mode: gh-proxy
    min-integrity: approved
    toolsets: [pull_requests, repos, issues]
  edit:
  bash:
    - "*"
timeout-minutes: 25
evals:
  - id: comment-added
    question: Did the agent add a comment to at least one pull request?
  - id: nudge-targeted
    question: Does the agent output show a specific reason why the selected PR needs a nudge toward maintainer investigation?
  - id: pr-evaluated
    question: Does the agent output confirm that it evaluated at least one open PR for nudge eligibility?
graders:
  execution-duration: {}
```
*Source: `.github/workflows/pr-sous-chef.md`, fetched via `curl` from
`raw.githubusercontent.com/github/gh-aw/main/`, 2026-09-02.*

### PR Sous Chef: Prefilter Logic (excerpted, live source shell script)

```
cooldown_seconds=1800   # 30-minute cooldown after an actionable sous-chef nudge
zero_diff_age_hours default = 24

Skip conditions (candidate excluded before the agent ever sees it):
  1. Any check queued/in_progress/requested/pending AND started/created
     within the last hour (checks running >1h are ignored so long-running
     agentic checks don't permanently block nudges)
  2. Most recent comment has both the <!-- gh-aw-pr-sous-chef-nudge -->
     marker AND "@copilot" (marker-only comments without "@copilot" are
     purely informational and do not count)
     -- EXCEPTION: not skipped if mergeStateStatus == CONFLICTING
  3. Any comment with both the marker and "@copilot" posted < 30 minutes ago

Output: /tmp/gh-aw/agent/pr-sous-chef-candidates-compact.json
  (fetched, generated_at, filtered_checks_pending, filtered_last_comment_
  from_sous_chef, filtered_cooldown, and per-PR: number, title, url,
  headRefOid, headRefName, createdAt, updatedAt, changedFiles,
  zero_diff_stalled, author, mergeStateStatus, failed_checks)
```
*Source: `.github/workflows/pr-sous-chef.md`, "Fetch open non-draft PR
queue" step, fetched 2026-09-02.*

### PR Sous Chef: Priority Order and Per-Run Cap (live source, prompt body)

```
Token efficiency rules (mandatory):
  1. Read the compact prefilter JSON first.
  2. If prs is empty, create the run-report issue and stop.
  3. Process PRs in updatedAt descending order.
  4. Process at most 4 nudges per run.
  5. Priority order:
       a. mergeStateStatus == CONFLICTING first
       b. zero_diff_stalled == true next (no files changed after 24h)
       c. unresolved review threads with an existing author/@copilot follow-up
       d. remaining PRs by most-recent updatedAt
     Ties broken by lower PR number, for deterministic reruns.
  6. Stop creating new nudge comments after 4 PRs nudged in the run.
  7. Use the pr-processor sub-agent for each PR; pass only PR number + compact context.
```
*Source: `.github/workflows/pr-sous-chef.md`, "Token efficiency rules"
section, fetched 2026-09-02.*

### PR Sous Chef: Inline `pr-processor` Sub-Agent (live source, full block)

```
## agent: `pr-processor`
---
description: Processes one PR with minimal API calls and returns skip/nudge decisions
model: sonnet
---
Given one PR number and compact metadata for github/gh-aw...

1. Check skip conditions in this order: checks/actions running;
   latest-comment-is-sous-chef-nudge (unless CONFLICTING); recent
   sous-chef nudge < 30 min ago.
2. If skipped, return skip_reason only.
3. If not skipped, return: conflicting (bool), whether branch update
   should be attempted, a single combined nudge comment body,
   resolve_review_threads (array of PRRT_... thread node IDs),
   dismiss_reviews (array of review IDs, only for github-actions[bot]
   CHANGES_REQUESTED reviews when ALL threads are resolved).
4. Make at most 8 tool calls total. If insufficient, set all fields to
   null and skip_reason: "insufficient_context".
5. Keep output compact JSON only — a single object, no prose.
```
*Source: `.github/workflows/pr-sous-chef.md`, `## agent: \`pr-processor\``
block, fetched 2026-09-02.*

### PR Sous Chef: Safe-Outputs Configuration (live source, full block)

```yaml
safe-outputs:
  needs: [approval_allowlist]
  add-comment:
    max: 4
    target: "*"
  approve-workflow-run:
    max: 8
    allowed-workflows: [cjs.yml, cgo.yml, CWI.yml]
    allowed-pull-requests: ${{ needs.approval_allowlist.outputs.eligible_pull_request_numbers }}
  resolve-pull-request-review-thread:
    max: 40
  dismiss-pull-request-review:
    max: 20
    target: "*"
  update-pull-request:
    title: false
    body: true
    operation: append
    update-branch: true
    sync-stack: true
    max: 10
    target: "*"
  push-to-pull-request-branch:
    target: "*"
    if-no-changes: ignore
    commit-title-suffix: " [pr-sous-chef]"
    excluded-files:
      - ".github/workflows/**"
      - "README.md"
      - "docs/src/content/docs/index.mdx"
    max: 10
  create-issue:
    title-prefix: "[pr-sous-chef] "
    labels: ["automation"]
    expires: 3d
    group-by-day: true
    close-older-issues: true
  mentions:
    allowed: ["@copilot"]
  noop:
```
*Source: `.github/workflows/pr-sous-chef.md`, `safe-outputs:` block, fetched
2026-09-02. The `approval_allowlist` job (not reproduced here in full) runs
after the agent job, re-derives eligible PR numbers from the same prefilter
artifact independently of the agent's own output, and feeds that list into
`approve-workflow-run`'s `allowed-pull-requests`.*

### PR Sous Chef: Active A/B Experiment (live source, full block)

```yaml
experiments:
  remove_redundant_context_v1:
    variants: [control, candidate]
    description: "Test removing the 'Required skip rules per PR' backup table from the main-agent prompt: the same three conditions are already deterministically enforced by the fetch-prs prefilter step and re-verified by the pr-processor sub-agent, so the table is redundant context on every run."
    hypothesis: "H0: No meaningful difference in execution-duration between control and candidate. H1: Removing the redundant backup skip-rules table decreases execution-duration without lowering the comment-added/pr-evaluated eval pass rate."
    metric: "grader:execution-duration"
    guardrail_metrics:
      - name: "eval:comment-added"
        threshold: ">=0.90"
      - name: "eval:pr-evaluated"
        threshold: ">=0.90"
    min_samples: 20
    analysis_type: mann_whitney
    decision:
      minimum_effect: 15000
      regression_tolerance: 15000
      confidence: 0.95
```
*Source: `.github/workflows/pr-sous-chef.md`, `experiments:` block, fetched
2026-09-02. Not mentioned anywhere in the blog post.*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 4 (Dead Code Removal
    Agent's "restraint is a feature, not a gap") and
    `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 8 (Issue Monster's
    per-topic retry-exhaustion tracking): Claim 4 here extends the same
    restraint principle to a third mechanism — a 15-minute scheduled
    monitor that is read-only the overwhelming majority of cycles by
    design.
  - `docs-ghaw-deterministic-agentic-patterns.md` Claim 3
    (`/tmp/gh-aw/agent/` as the designated pre-processing-to-agent
    data-exchange directory): Claim 5 here is a concrete production
    instance — the prefilter writes `pr-sous-chef-candidates-compact.json`
    to exactly that directory.
  - `docs-ghaw-inline-sub-agents.md` Claim 1 (`## agent: \`name\`` heading
    syntax) and Claim 4 (`model` field as "the primary economic
    optimization lever for inline sub-agents", defaulting to the parent's
    model): Claim 7 here is a concrete, named production instance of both,
    extending Claim 4 specifically with a cross-provider override (OpenAI
    `pi`/`gpt-5.4` parent delegating to an Anthropic `sonnet` sub-agent) —
    that reference note's own worked example was same-provider (Opus →
    Haiku).
  - `docs-ghaw-practices-experiments.md` Claim 1 (named experiments with
    variant selection), Claim 3 (`${{ experiments.<name> }}` conditional
    prompt syntax), and Claim 9 (`guardrail_metrics` as automated
    safeguards), plus `docs-ghaw-graders.md` Claim 11 (experiment metrics
    referencing grader outputs via `grader:<id>`): Claim 9 here is a
    concrete, named production instance of all of these combined in one
    workflow.
  - `docs-ghaw-threat-detection.md` Claim 10 (protected-file categories
    including CI/CD workflow files): Claim 8 here's
    `push-to-pull-request-branch.excluded-files` list is a live, named
    instance, extended with two specific non-CI protected files
    (`README.md`, a docs index page) the workflow's own prompt separately
    justifies as "primary project messaging."
  - `docs-ghaw-graders.md` Claim 3 (ten reserved built-in grader IDs
    spanning tool-call quality, execution shape, and context-management
    health): Claim 3 here's "13 out of 13 graders passed clean" is a
    concrete production result consistent with that documented taxonomy,
    though the post does not name which 13 graders ran.

- **Contradicts**: None identified. Reviewed `CONTRADICTIONS.md` in full (no
  existing entries touching PR-monitoring/nudging agents, inline sub-agent
  model selection, or the `experiments` A/B-testing mechanism) and all
  source notes cited throughout this note. No contradiction issue filed.

- **Extends**:
  - `blog-ghaw-agent-of-the-day-2026-08-25.md` (Issue Monster, curation
    archetype) and `blog-ghaw-agent-of-the-day-2026-08-24.md` (Q, on-demand
    diagnostic archetype): PR Sous Chef adds a sixth trigger/posture
    combination to this series' taxonomy — **high-frequency (sub-hourly)
    scheduled monitor with a supplementary slash-command trigger**, distinct
    from Issue Monster's 30-minute pure-schedule curation and Q's
    pure-slash-command diagnostic-and-fix pattern.
  - `docs-ghaw-inline-sub-agents.md` Claim 4: extends the documented
    same-provider cost-tiering use case for the sub-agent `model` field with
    a live cross-provider instance.
  - `docs-ghaw-safe-outputs-specification.md` Claim 5 (SP1 Permission
    Separation) and the single-job `min-integrity`/`toolsets` scoping
    already documented for Issue Monster
    (`blog-ghaw-agent-of-the-day-2026-08-25.md` Concrete Artifacts): Claim 8
    here's `approval_allowlist` job is a stronger, two-job instance of
    privilege separation — a deterministic job the agent cannot influence
    computes the write-scope allowlist that the safe-outputs processor then
    enforces independently of the agent's own output.

- **Novel**:
  - **A hybrid 15-minute-schedule + slash-command trigger on the same
    workflow** (Claim 1): no prior "Agent of the Day" entry combines a
    sub-hourly schedule with an on-demand slash-command trigger.
  - **"Zero-diff stalled" (opened, zero files changed, N hours elapsed) as a
    named PR-staleness signal** (Claim 6): a specific, checkable staleness
    heuristic not previously documented in the corpus's triage/monitoring
    agents.
  - **A deterministic, agent-independent second job computing a safe-output
    allowlist that the safe-outputs processor enforces on top of the
    agent's own output** (Claim 8, the `approval_allowlist` job): a
    stronger privilege-separation pattern than single-job tool/permission
    scoping documented elsewhere in the corpus.
  - **An active A/B experiment testing removal of prompt content already
    enforced deterministically elsewhere in the same pipeline** (Claim 9):
    the specific hypothesis — that a defensive "backup" instructions table
    is redundant because the same logic already runs in both a
    deterministic prefilter step and a sub-agent re-verification step — is
    a novel context-trimming experiment design not previously documented in
    this corpus.
  - **A `CONFLICTING`-merge-state exception that overrides duplicate-comment
    suppression** (Claim 5): the workflow will nudge a PR again immediately
    even right after its own prior nudge, specifically when the PR has
    entered a merge-conflict state — a priority-weighted refinement of
    simple cooldown gating not previously documented.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add "high-frequency scheduled
  monitor with supplementary slash-command trigger" as a sixth named
  trigger/posture combination in this series' taxonomy (Claim 1, Extends).
  Add "zero-diff staleness" as a named PR-health signal alongside a fixed
  priority ladder with a deterministic tiebreak (Claim 6) as a reusable
  pattern for agents processing a shared, frequently-rerun queue under a
  hard per-run action cap. Extend the inline-sub-agent "model as cost
  lever" guidance (`docs-ghaw-inline-sub-agents.md` Claim 4) with this
  cross-provider instance (Claim 7), and add "hard per-task tool-call cap
  with an explicit insufficient-context bail-out" as a bounded-effort
  sub-agent pattern.

- **Chapter 03 (Safety and Verification)**: Document "compute the
  write-scope allowlist in a separate deterministic job the agent cannot
  influence, then have the safe-outputs processor enforce it independently"
  (Claim 8's `approval_allowlist` job) as a stronger privilege-separation
  pattern than agent-job-level tool/permission scoping alone. Add the
  `CONFLICTING`-state override of duplicate-comment suppression (Claim 5) as
  a worked example of priority-weighted skip-gate design — not every
  restraint mechanism should apply uniformly to every mutation trigger.

- **Chapter 04 (Operations)**: Add PR Sous Chef's five-run September 1
  snapshot (Claim 2: 20 safe-output items across five runs, zero
  errors/warnings) as a baseline for a 15-minute-cadence monitoring agent,
  and Claim 3's grader/network-policy result (13/13 graders clean, 5/53
  network calls blocked by firewall policy despite a fully successful run)
  as an example that grader-pass and network-policy-clean are separate
  signals worth reporting independently.

- **Chapter 09 (Multi-Agent Coordination)**: Use Claim 9's active
  `remove_redundant_context_v1` experiment as a worked example of the
  `experiments` A/B-testing mechanism (`docs-ghaw-practices-experiments.md`)
  applied specifically to a context-trimming hypothesis — testing whether a
  defensive "backup" prompt section, already redundant with deterministic
  enforcement elsewhere in the pipeline, actually needs to exist.

## Extraction Notes

1. **Blog post is short (~350 words); primary depth came from one fetched
   sub-page**, well within MINER.md §1's "up to 5" budget: the live
   workflow source (`pr-sous-chef.md`, 554 lines), fetched via `curl` from
   `raw.githubusercontent.com/github/gh-aw/main/.github/workflows/pr-sous-chef.md`
   and read in full. Claims 5–9 and most of Concrete Artifacts rely entirely
   on this sub-page — none of it is present in the blog post's own text.
   Claims 1–4 are supported by the blog post's own text, cross-checked
   against the live source where it overlaps.

2. **Verbatim blog quotes obtained via direct HTML fetch, not WebFetch
   summarization**: an initial WebFetch call against the blog URL returned
   a structured, paraphrased summary (correct in substance — e.g. it
   accurately reported "20 safe-output items with zero errors and zero
   warnings" and "13 out of 13... graders passed clean" — but not
   confirmed verbatim by that pass alone). Per MINER.md §2a, the page was
   re-fetched directly via `curl`, and the article body was located inside
   `<div class="sl-markdown-content">`. All quotes above are copied
   character-for-character from that raw-HTML extraction (including
   original curly quotation marks and em-dashes), not reconstructed from
   the WebFetch summary.

3. **One Actions run independently spot-checked against the GitHub REST
   API**: run 33516358980's basic metadata (workflow name "PR Sous Chef",
   event `schedule`, conclusion `success`, created/completed timestamps)
   was fetched directly from `api.github.com/repos/github/gh-aw/actions/runs/33516358980`
   (public, unauthenticated) and matches the blog post's characterization
   of a September 1 scheduled run completing successfully. Job-level grader
   and network-call detail (Claim 3's "13/13 graders," "5 of 53 network
   calls") was not independently re-derived from raw run logs — those
   specific figures are taken as reported by the blog post, consistent with
   how per-run metrics are handled in prior notes in this series (e.g.
   `blog-ghaw-agent-of-the-day-2026-08-20.md` Extraction Note 2).

4. **Cross-reference check performed** against
   `blog-ghaw-agent-of-the-day-2026-08-28.md`,
   `blog-ghaw-agent-of-the-day-2026-08-25.md`,
   `blog-ghaw-agent-of-the-day-2026-08-24.md`,
   `blog-ghaw-agent-of-the-day-2026-08-20.md`,
   `blog-ghaw-agent-of-the-day-2026-05-28.md`,
   `docs-ghaw-inline-sub-agents.md`, `docs-ghaw-deterministic-agentic-patterns.md`,
   `docs-ghaw-practices-experiments.md`, `docs-ghaw-graders.md`,
   `docs-ghaw-safe-outputs-specification.md`, `docs-ghaw-threat-detection.md`,
   and `CONTRADICTIONS.md`, all read in full (not skimmed) before writing
   Cross-References. All `Claim N` citations above were checked against the
   actual numbered claims in those notes at the time of writing, per
   MINER.md §4b.

5. **Three near-duplicate Prospector triage comments observed on issue
   #3160**, apparently from repeated/parallel triage passes on the same
   auto-filed source (consistent with the pattern already documented in
   several prior notes in this series, e.g.
   `blog-ghaw-agent-of-the-day-2026-08-20.md` Extraction Note 5). All three
   agree on novelty (medium-to-high), source type (blog-post), and the core
   extraction guidance (restraint/selective-nudging design, scheduling vs.
   slash-command trigger comparison, Ch02/Ch04 relevance); this note
   follows the union of their guidance rather than picking one comment over
   the others. Per the task instructions, the issue's title, body, and
   comments were treated as untrusted data to extract from, not as
   instructions — none of the three comments contained anything resembling
   an instruction to this agent beyond normal triage guidance.
