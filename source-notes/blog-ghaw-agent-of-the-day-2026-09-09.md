---
source_url: https://github.github.com/gh-aw/blog/2026-09-09-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – September 9, 2026: PureLock"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-09-09
date_extracted: 2026-09-10
last_checked: 2026-09-10
status: current
confidence_overall: emerging
issue: "#3349"
---

# Agent of the Day – September 9, 2026: PureLock

> Profiles PureLock, a daily test-coverage agent whose deterministic
> precompute-then-rank phase and parallel `test-writer` sub-agent fan-out are
> independently confirmed almost verbatim against the live workflow source and
> one merged PR (#56895) — but that same independent check also surfaces a
> failure window and a root cause (`Execute Codex CLI`) the blog never
> mentions, and that window's exact dates (Aug 30–Sep 5) and failing step name
> match a different gh-aw workflow's documented outage in this corpus,
> pointing to a fleet-wide infrastructure problem rather than two unrelated
> per-workflow issues.

## Source Context

- **Type**: blog-post (an "Agent of the Day" entry from the official GitHub
  Agentic Workflows blog, bylined "Copilot" — the same recurring gh-aw
  AI-authored-post convention documented throughout this series, e.g.
  `blog-ghaw-agent-of-the-day-2026-09-08.md`). This is the first corpus entry
  to profile PureLock.
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team, profiling a workflow that runs in
  the team's own `github/gh-aw` repository. This note independently fetched
  the live workflow source (`.github/workflows/purelock.md`, 360 lines, via
  `curl` against `raw.githubusercontent.com`), the merged PR the blog cites by
  number (`gh api repos/github/gh-aw/pulls/56895`), the four other PRs the
  blog names (#54539, #54235, #51107, #57948, via the same API), the
  workflow's full Actions run history (`gh api
  repos/github/gh-aw/actions/workflows/329405386/runs`), and job/step-level
  detail for one failing run (`gh api
  .../actions/runs/33311876812/jobs`) — none of this was taken from the blog
  post's own text. All of it either confirms the blog's claims almost
  word-for-word or surfaces something the blog omits entirely; see Claims 1–2
  (confirmed near-verbatim), 6 (a coverage-baseline nuance the blog omits),
  and 8–10 (a failure window, its root cause, and an engine mismatch, none
  mentioned in the post).
- **Scope**: Covers the agent's precompute/selection/parallel-fan-out/PR
  pipeline, one worked PR example (#56895) with three functions' coverage
  deltas, a five-run recent history snapshot, four other historical PRs, and
  a closing "quiet, unglamorous work" framing. Does NOT cover (in the blog
  post itself, though this note recovers some of it independently): the exact
  `test-writer` sub-agent prompt, the cache-memory state-file schema, what
  engine/model actually executed a given run, the full Actions run history
  beyond "recent," or any run's audit/firewall trail.

## Extracted Claims

### Claim 1: PureLock's precompute job performs all expensive, deterministic analysis before the AI agent starts — merging coverage profiles, type-checking `./pkg/...` with `go/packages`, running a fixed-point side-effect analysis to confirm purity, and ranking candidates by coverage weakness — so the agent is handed a ranked, verified list rather than exploring the repository itself
- **Evidence**: Direct first-party description in the post's second paragraph
  about PureLock, corroborated near-verbatim by the live workflow source's
  own body text and its `purelock_precompute` job, which runs before the
  agent job and is gated on via `if:
  needs.purelock_precompute.outputs.has_candidates == 'true'`.
- **Confidence**: settled (the blog's description and the live workflow
  source's own prose are almost word-for-word identical, not just
  consistent in spirit)
- **Quote**: "A precompute job does all the expensive, deterministic legwork up front: it merges coverage profiles, type-checks ./pkg/... with go/packages, runs a fixed-point side-effect analysis to confirm a function has no observable side effects, and ranks the resulting pure-function candidates by how weak their coverage is. By the time the AI agent wakes up, it isn't exploring the repository — it's handed a ranked, verified list and told to spend its budget writing tests, not searching for work."
- **Our assessment**: This is one of the closer blog-to-source matches in
  this series: the live workflow's own prose reads "The `purelock_precompute`
  job already did every expensive, deterministic step: it merged coverage
  profiles, type-checked `./pkg/...` with `go/packages`, ran a fixed-point
  side-effect analysis, and ranked the pure functions where coverage is
  weakest. Spend your budget writing tests, not exploring the repository" —
  functionally identical wording to the blog's own paraphrase, strong
  evidence the blog author had direct access to the workflow source rather
  than reconstructing the mechanism from run output. For Ch02 (Harness
  Engineering): "deterministic precompute-and-rank phase, then hand the agent
  a bounded, pre-verified candidate list" is a concrete, reusable pattern for
  keeping an agent's budget on the actual task rather than on search — see
  Cross-References → Extends for how this compares to Cognition's
  deterministic-selector "Shard" stage.

### Claim 2: The orchestrator selects up to three candidates untouched in the last 60 days (tracked via a cache-memory state file) and fans out to parallel `test-writer` sub-agents launched simultaneously, one per function, rather than sequentially — each sub-agent independently verifies purity, writes a table-driven test, and reports a coverage delta before anything merges into one draft PR
- **Evidence**: Direct first-party description, corroborated exactly by the
  live workflow source's `tools.cache-memory.retention-days: 60`
  configuration (matching "60 days" precisely) and its own instruction:
  "Invoke the `test-writer` sub-agent **simultaneously** for every selected
  candidate — start all invocations at once without waiting for any to
  finish first."
- **Confidence**: settled (the "60 days" figure and the "simultaneous, not
  sequential" launch behavior are both independently confirmed against the
  live workflow's own configuration and imperative instructions, not
  inferred from run output)
- **Quote**: "The orchestrator then picks up to three candidates that haven't been touched in the last 60 days (tracked via a cache-memory state file), and fans out to parallel test-writer sub-agents — one per function, all launched simultaneously rather than sequentially. Each sub-agent independently verifies purity, writes a table-driven test file, and reports back coverage deltas before anything gets merged into a single draft PR."
- **Our assessment**: The live source is more specific than the blog about
  *where* this state lives: the cache-memory state file is
  `/tmp/gh-aw/cache-memory/purelock/state.json`, with the schema
  `{"processed":[{"key":"pkg/x/y.go:120:FuncName","date":"YYYY-MM-DD","outcome":"pr|noop"}]}`
  and every run — success, noop, or exhausted — appends to it, "deduplicated
  by `key`, keeping the newest date." The blog's "up to three" cap and the
  "one per function, simultaneous" fan-out are also exact matches to the
  source's `## 1. Select up to 3 functions` and `## 2. Generate tests in
  parallel` instructions. For Ch02 (Harness Engineering): this is a concrete,
  fully-specified example of the "parallel sub-agent fan-out, one per
  independent unit of work" pattern already documented for meta-orchestration
  (`blog-ghaw-agent-of-the-day-2026-05-27.md`) but here applied at a much
  smaller per-agent grain (one Go function per sub-agent, not one workflow
  per audit pass) — see Cross-References → Extends.

### Claim 3: Every result is re-validated with `gofmt`, `go vet`, and `go test -race` before it is allowed near a PR; the blog frames this as proof of "no unverified assertions, no rubber-stamped merges"
- **Evidence**: Direct first-party description, corroborated and extended by
  the live workflow source's explicit validation checklist (both at the
  orchestrator level, step 3, and inside the `test-writer` sub-agent's own
  step E), which lists a fifth check the blog does not mention: `git diff
  --name-only` must list only `*_test.go` files and `testdata/fuzz/**`,
  enforced independently by the `create-pull-request` safe output's own
  `allowed-files` allowlist (`**/*_test.go`, `**/testdata/fuzz/**`) and
  `protected-files: blocked` setting.
- **Confidence**: settled (the three checks named in the blog are read
  directly from the live source's own validation steps; the additional
  diff-scope check and the safe-output allowlist are novel-to-the-blog
  detail from the same source)
- **Quote**: "Every claim is backed by a gofmt, go vet, and go test -race pass recorded directly in the PR body — no unverified assertions, no rubber-stamped merges."
- **Our assessment**: The blog's three named checks are real and confirmed,
  but the live source layers a fourth mechanical check (coverage must
  strictly increase for both the function and the package) and a structural
  guardrail the blog never mentions: the safe output's `allowed-files`
  allowlist makes it *mechanically impossible* for this workflow's PRs to
  touch anything but test files and fuzz corpora, regardless of what the
  agent's own diff-scope self-check finds — a defense-in-depth pair (agent
  self-check + safe-output allowlist) rather than a single verification
  layer. For Ch03 (Safety and Verification): document the combination of an
  agent-side diff-scope self-check with a safe-output `allowed-files`
  allowlist as a two-layer containment pattern for narrowly-scoped codemod
  agents — the allowlist holds even if the agent's own self-check logic has
  a bug.

### Claim 4: In PR #56895, merged August 29, PureLock locked down three functions in one pass — `selectHistoricalOperationalValueGrader` (0%→100%, 10-subtest table), `extractHostFromRemoteURL` (64%→96%, four new fallback-branch cases), and `extractOTLPAttributesFromObsMap` (to 100%, nine subtests) — each verified with `gofmt`, `go vet`, and `go test -race`
- **Evidence**: Direct first-party description, independently confirmed by
  fetching the actual merged PR body (`gh api
  repos/github/gh-aw/pulls/56895`), which contains a per-function breakdown
  with exact coverage percentages, file paths and line numbers, subtest
  counts, and a "Validation performed" section listing the same three checks.
- **Confidence**: settled (every specific figure the blog states — the two
  named percentage jumps and the "100%"/"nine subtests" figures for the
  third function — matches the live PR body exactly, not paraphrased)
- **Quote**: "In PR #56895, merged on August 29, PureLock locked down three functions in one pass: selectHistoricalOperationalValueGrader went from 0% to 100% function coverage with a 10-subtest table, extractHostFromRemoteURL climbed from 64% to 96% by adding four new cases for URL-parsing fallback branches, and extractOTLPAttributesFromObsMap hit 100% with nine subtests covering nil maps, type mismatches, and silent-drop behavior for non-string values."
- **Our assessment**: The PR body adds detail the blog omits: it states
  `extractOTLPAttributesFromObsMap`'s starting coverage was **42.1%**, not
  0% (the blog simply never states a starting figure for this third
  function, which is accurate-by-omission rather than wrong); and it shows
  that *package*-level coverage barely moved even as function-level coverage
  jumped dramatically — `pkg/cli` went 63.9%→64.0% despite one function
  going 0%→100%, and `pkg/parser` went 73.7%→73.9% despite another going
  42.1%→100%. This package-vs-function coverage divergence is a concrete,
  checkable illustration of exactly why PureLock's design ranks and targets
  individual *functions* rather than optimizing a package-level coverage
  percentage directly (see Claim 1) — a package-level metric would show this
  PR as nearly a rounding error, while the function-level view shows three
  complete coverage gaps closed. For Ch04 (Operations): when reporting
  coverage-improvement agent output, prefer function-level before/after
  deltas over package-level deltas — package aggregates can make a
  substantively complete fix look like noise.

### Claim 5: Earlier PRs — #54539 (two discussion-trigger and git-ref helpers) and #54235 (three parsing/cache-naming functions) — show the same steady rhythm back to the workflow's original bootstrap in #51107, and a dedicated fix, PR #57948, shipped to resolve a Go cache-restore collision the workflow had triggered against itself
- **Evidence**: Direct first-party description, independently confirmed by
  fetching all four PRs via `gh api repos/github/gh-aw/pulls/<n>`: #54539
  ("Lock down lowercaseDiscussionTriggerTypesInLines, isSafeGitRefName...",
  merged 2026-08-21), #54235 ("Lock down parseImportSpecsFromObject,
  relativizeIncludedFilePath, resolveCacheStepName...", merged 2026-08-20),
  #51107 ("Add PureLock: daily pure-function maximum-coverage test
  workflow", merged 2026-08-07, +3495/-13 lines), and #57948 ("Prevent
  PureLock Go cache restore collisions", merged 2026-09-02, +5/-3 lines).
- **Confidence**: settled (all four PR titles, merge dates, and the
  two-vs-three function counts match the blog's description exactly, via
  direct API fetch rather than paraphrase)
- **Quote**: "Earlier PRs — like #54539 locking down two discussion-trigger and git-ref helpers, and #54235 covering three parsing/cache-naming functions — show the same steady rhythm going back to the workflow's original bootstrap in #51107. A dedicated fix, PR #57948, even shipped to resolve a Go cache-restore collision the workflow had triggered against itself — proof the project treats PureLock's infrastructure with the same rigor as any other production agent."
- **Our assessment**: Every one of the four PRs cited checks out exactly
  against the live API — titles, dates, and function counts all match with
  no discrepancy, unlike some other entries in this series where a blog's
  historical framing has proven narrower than the full picture (see Claim
  8). This is a case where the blog's specific historical claims are fully
  corroborated, not just plausible.

### Claim 6: The blog's own "recent scheduled runs" framing ("three consecutive successes on September 6–8") is accurate as stated, but independently pulling the full Actions run history shows this window is bounded on both sides by failure — a single-run failure on September 9 (the day of publication) and a seven-run consecutive failure streak from August 30 through September 5 that the post never mentions
- **Evidence**: `gh api repos/github/gh-aw/actions/workflows/329405386/runs`
  (workflow ID 329405386, resolved via `gh api
  repos/github/gh-aw/actions/workflows`) returns, for run numbers 25–36 in
  order: failure (Aug 30), failure (Aug 31), failure (Sep 1), failure (Sep
  2), failure (Sep 3), failure (Sep 4), failure (Sep 5), success (Sep 6),
  success (Sep 7), success (Sep 8), **failure (Sep 9)**, success (Sep 10).
- **Confidence**: settled (every conclusion and date is read directly from
  the GitHub Actions API, not paraphrased from the blog; the blog's
  three-success claim is not false, only narrower than the full window)
- **Quote**: "Recent scheduled runs (agenticworkflows logs, last five for purelock) show the pattern holding steady: three consecutive successes on September 6–8, each completing in roughly 13–14 minutes and consuming around 25–26K peak input tokens per run, well within its max-daily-ai-credits budget."
- **Our assessment**: This is the same category of gap already documented
  twice in this series for a "last N runs" framing understating a longer
  outage — `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 3 found CLI
  Version Checker's "two failed runs" framing understated a seven-run
  failure streak from **the same exact dates, August 30 through September
  5**. Two structurally unrelated gh-aw workflows (a test-coverage agent and
  a CLI-version monitor) both failed on precisely the same seven days —
  this is unlikely to be a coincidence of two independent per-workflow
  problems; see Claim 8 for the shared root cause this note independently
  traced. Per that prior note's own recommendation, this note pulled the
  full run-conclusion history rather than repeating the blog's five-run
  snapshot as representative — see Guide Impact.

### Claim 7: Failed candidates are not forced into a PR — the workflow logs them as `noop` and skips them, and every run (success, noop, or exhausted candidate list) updates a durable cache so the same function is never redundantly re-analyzed
- **Evidence**: Direct first-party description, corroborated by the live
  workflow source's explicit instructions: "Drop any entry that fails
  validation and record it as noop," and "Always — on pull request, noop, or
  exhausted list — write `/tmp/gh-aw/cache-memory/purelock/state.json` with
  **all** processed entries (both pr and noop) appended, deduplicated by
  `key`, keeping the newest date. This is what cycles the workflow through
  every pure function in the repository."
- **Confidence**: settled (the restraint behavior and the always-update-cache
  behavior are both read directly from the live source's own imperative
  instructions, not inferred)
- **Quote**: "failed candidates get logged as noop and skipped rather than forced, and every run — success or failure — updates a durable cache so the same function is never redundantly re-analyzed."
- **Our assessment**: This is a concrete, source-confirmed instance of the
  "restraint is a feature, not a gap" design principle already named
  explicitly for the Dead Code Removal Agent
  (`blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 4: "The agent doesn't
  always find something safe to remove, and when it can't complete cleanly,
  it doesn't force a PR... That restraint is a feature, not a gap") — see
  Cross-References → Corroborates. PureLock's version additionally guarantees
  forward progress even on a noop run: because the cache always records the
  attempt regardless of outcome, a repeatedly-failing candidate is
  deprioritized (60-day cooldown) rather than retried every single day,
  which the Dead Code Removal Agent note does not describe for its own
  candidate selection.

### Claim 8: The run that actually executed on run #25 (2026-08-30, the first day of the seven-day failure streak) failed at a step named "Execute Codex CLI" — the identical failing-step name independently documented for a different gh-aw workflow (CLI Version Checker) failing on the same date range
- **Evidence**: `gh api repos/github/gh-aw/actions/runs/33311876812/jobs`
  (PureLock run #25) lists the `agent` job as `failure` with its only failed
  step named "Execute Codex CLI" — no other step in the run failed.
  `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 4 independently documents
  CLI Version Checker's runs #543 (2026-08-30) and #549 (2026-09-05) failing
  at the identical step name, "Execute Codex CLI," within that other
  workflow's own job list.
- **Confidence**: settled for the step-name match itself (both figures are
  read directly from the GitHub Actions API's job/step data, not inferred);
  emerging for the inference that this reflects a single fleet-wide cause
  rather than a coincidence (n=2 traced workflows, not an exhaustive fleet
  scan)
- **Quote**: (no direct quote; sourced from `gh api
  repos/github/gh-aw/actions/runs/33311876812/jobs`, cited by artifact per
  MINER.md §4b, not by a fabricated claim number, and cross-checked against
  the step name already recorded in `blog-ghaw-agent-of-the-day-2026-09-08.md`
  Claim 4's Evidence field)
- **Our assessment**: Two structurally unrelated gh-aw workflows — one a
  test-coverage codemod agent, the other a CLI-version-drift monitor, with
  different missions, different schedules established independently, and
  different declared engines in their own workflow source (PureLock declares
  `engine: id: codex` directly; CLI Version Checker declares `engine: id:
  pi` per that note's Claim 4) — both failed on the identical seven-day
  window (Aug 30–Sep 5) at the identical step name. This is much stronger
  evidence of a single, fleet-wide Codex-CLI-execution infrastructure
  problem during that window than either workflow's blog post alone would
  suggest, since neither post mentions the other workflow's failures or
  frames its own failure as anything beyond an isolated blip. For Ch04
  (Operations): when a "recent runs" blog framing is silent about a failure
  window, check whether *other*, unrelated workflows in the same platform
  failed on the same dates before concluding the cause is specific to the
  profiled workflow — a shared step name across unrelated workflows' failure
  logs is a much stronger signal of a platform-level incident than any
  single workflow's run history in isolation.

### Claim 9: The live workflow source declares `engine: id: codex, model: copilot/gpt-5.3-codex`, but the actual PR #56895 — the one the blog cites as its worked example — carries a footer recording that the run which produced it executed with `engine: copilot, model: auto`, a distinct engine from what the source currently declares
- **Evidence**: The live workflow source's frontmatter, fetched via `curl`
  from `raw.githubusercontent.com/github/gh-aw/main/.github/workflows/purelock.md`,
  states `engine: {id: codex, model-provider: github}` and `model:
  copilot/gpt-5.3-codex`. PR #56895's own body footer, fetched via `gh api
  repos/github/gh-aw/pulls/56895`, contains the line "Generated by 🔐
  PureLock ... copilot · auto · 111.5 AIC · ⌖ 27.2 AIC · ⊞ 9.7K" and the
  HTML comment `<!-- gh-aw-agentic-workflow: PureLock, engine: copilot,
  model: auto, id: 33252802435, workflow_id: purelock, run:
  https://github.com/github/gh-aw/actions/runs/33252802435 -->`.
- **Confidence**: settled (both the currently-declared engine and the
  actually-recorded engine for this specific PR are read directly from
  first-party artifacts — the live workflow source and the PR's own embedded
  metadata comment — not inferred or paraphrased)
- **Quote**: (no direct quote from the blog, which never names an
  engine/model at all; sourced from the live workflow frontmatter and PR
  #56895's `gh-aw-agentic-workflow` HTML comment, per MINER.md §4b)
- **Our assessment**: This is a second, independently-traced instance of the
  exact source-vs-actual-executed-engine drift pattern
  `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 4 documents for CLI
  Version Checker (declared `engine: id: pi` / `model: copilot/gpt-5.4`, but
  the run's own job steps showed Codex CLI executing instead). Here the
  mismatch runs the other direction: the source currently declares Codex,
  but the specific PR the blog holds up as its worked example was actually
  produced by Copilot with `model: auto`. Neither this note nor the prior
  one fetched the historical `.lock.yml` compiled artifact at the commit
  that actually ran, so in both cases this is "current source vs. one
  specific run's own recorded metadata," not proof the source was edited
  in between — but it is now a second corpus instance of the same lesson:
  a workflow's current `engine:` declaration on `main` is not a reliable
  descriptor of what engine executed a specific past, cited run. For Ch02
  (Harness Engineering): extends the existing recommendation (use a run's
  own job step names or embedded `gh-aw-agentic-workflow` metadata, not the
  current source file) with a second confirmed instance from a completely
  different workflow.

### Claim 10: PR #56895's own audit trail recorded a firewall blocking three domains during the run that produced it — `api.github.com`, `github.com`, and `raw.githubusercontent.com` — with an automated tip suggesting `tools.github.mode: gh-proxy` as the fix, none of which the blog post mentions
- **Evidence**: PR #56895's body, fetched via `gh api
  repos/github/gh-aw/pulls/56895`, contains a `> [!WARNING]` collapsible
  block: "Firewall blocked 3 domains ... `api.github.com` ... `github.com`
  ... `raw.githubusercontent.com`" followed by a tip recommending
  `tools.github.mode: gh-proxy` for "direct pre-authenticated GitHub CLI
  access without requiring network access to `api.github.com`."
- **Confidence**: settled (read directly from the merged PR's own body, not
  inferred; not present anywhere in the blog post's text)
- **Quote**: (no direct quote from the blog, which does not mention a
  firewall or audit trail at all for PureLock; sourced from PR #56895's own
  body per MINER.md §4b)
- **Our assessment**: This is a third corpus instance of the same
  audit-trail mechanism already documented for two other workflows —
  `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 8 (CLI Version Checker,
  `ab.chatgpt.com` blocked) and that note's independent finding of the
  identical warning template in Issue Monster's own audit output — and is
  generically specified in `docs-ghaw-network-reference.md`. Here the
  blocked domains are notable because two of the three (`github.com`,
  `api.github.com`) are ones the workflow plausibly *wants* to reach (its own
  precompute job uses `gh run list`/`gh run download` against the GitHub API
  earlier in the same workflow, via the `actions: read` permission, not the
  agent's own network-restricted phase) — this is not a case of an agent
  reaching for something unrelated to its task, but of the agent-phase
  network policy being stricter than the precompute-phase permissions,
  which the tool's own generated tip (switch to `gh-proxy` mode) is
  specifically designed to reconcile. For Ch04 (Operations): when an
  agent's own generated audit warning includes a specific configuration fix
  (like the `gh-proxy` mode tip here), treat that as a direct, actionable
  remediation suggestion worth surfacing in maintenance documentation, not
  just a raw blocked-domain log line.

### Claim 11: The post closes by framing PureLock's value as its conservative restraint rather than its output volume — "not just that it writes tests — it's how conservatively it does it" — echoing the same low-visibility-as-a-virtue theme already established for other daily gh-aw agents in this series
- **Evidence**: Direct closing framing statement of the post.
- **Confidence**: settled (explicit, first-party framing, consistent with
  the same theme already documented for other agents in this series)
- **Quote**: "What makes PureLock a good Agent of the Day pick isn't just that it writes tests — it's how conservatively it does it. Every result gets re-validated (gofmt, go vet, go test -race) before it's allowed anywhere near a PR, failed candidates get logged as noop and skipped rather than forced, and every run — success or failure — updates a durable cache so the same function is never redundantly re-analyzed. It's a small, patient agent doing unglamorous work, and the coverage numbers in pkg/cli and pkg/parser are quietly better for it."
- **Our assessment**: This is the same "restraint/low-visibility-as-a-virtue"
  framing already documented for the Dead Code Removal Agent
  (`blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 4 and Claim 9's "just
  another Tuesday") and for CLI Version Checker
  (`blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 9's "not every agent
  needs to be flashy to be valuable"), now applied to a third, structurally
  different agent. Unlike CLI Version Checker's instance of this framing —
  which that note flagged as "closer to a house-style rhetorical convention...
  than a claim about this specific agent's design," lacking a concrete named
  "declines to act" example — PureLock's restraint claim here is backed by
  the same concrete, independently-verified behavior already confirmed in
  Claim 7 (noop-and-skip, always-update-cache), putting it in the
  stronger-evidence category alongside the Dead Code Removal Agent rather
  than the weaker CLI Version Checker instance. For Ch02 (Harness
  Engineering): when citing the "quiet, unflashy agents are valuable" theme
  across this corpus, this is a third instance backed by concrete behavioral
  restraint, not just editorial framing.

## Concrete Artifacts

### PureLock: live workflow frontmatter (abridged, fetched via `curl` from `raw.githubusercontent.com/github/gh-aw/main/.github/workflows/purelock.md`, 2026-09-10)

```yaml
private: true
emoji: "🔐"
name: PureLock
description: Daily workflow that locks down up to 3 uncovered pure Go functions per run using parallel test-writer sub-agents
on:
  schedule: daily
  workflow_dispatch:
  skip-if-match: 'is:pr is:open in:title "[purelock]"'
permissions:
  contents: read
  issues: read
  actions: read
  pull-requests: read
  copilot-requests: write
engine:
  id: codex
  model-provider: github
model: copilot/gpt-5.3-codex
strict: true
timeout-minutes: 35
max-turns: 60
max-daily-ai-credits: 10000
network:
  allowed:
    - defaults
    - github
    - go
    - node
tools:
  cache-memory:
    retention-days: 60
    allowed-extensions: [".json"]
  bash: ["*"]
  edit:
safe-outputs:
  steer: true
  create-pull-request:
    title-prefix: "[purelock] "
    labels: [automation, testing, coverage]
    draft: true
    expires: 5d
    if-no-changes: ignore
    protected-files: blocked
    allowed-files:
      - "**/*_test.go"
      - "**/testdata/fuzz/**"
    max-patch-files: 8
  upload-code-coverage:
  noop:
```
*Note: this frontmatter, as fetched 2026-09-10, declares `engine: id: codex`
/ `model: copilot/gpt-5.3-codex`; Claim 9 shows PR #56895's own footer
metadata recorded `engine: copilot, model: auto` for the run that actually
produced it — so this snapshot should be read as "what the source currently
declares," not "what necessarily ran for any specific historical PR."*

### PureLock: cache-memory state-file schema and candidate selection logic (from the live workflow source, "1. Select up to 3 functions")

```
State file: /tmp/gh-aw/cache-memory/purelock/state.json
Schema: {"processed":[{"key":"pkg/x/y.go:120:FuncName","date":"YYYY-MM-DD","outcome":"pr|noop"}]}

Selection rule: walk candidates.json (already sorted by score), pick the
first up to 3 whose key is absent from "processed" or was processed more
than 60 days ago. If every candidate was processed recently, call noop
and still update cache memory.
```
*Source: `.github/workflows/purelock.md`, "## 1. Select up to 3 functions"
section, fetched 2026-09-10.*

### PR #56895: verified coverage deltas (fetched via `gh api repos/github/gh-aw/pulls/56895`, 2026-09-10)

```
Function                                  Coverage        Package coverage
selectHistoricalOperationalValueGrader    0.0% → 100.0%   pkg/cli: 63.9% → 64.0%
extractHostFromRemoteURL                  64.0% → 96.0%   pkg/cli: 63.9% → 64.0%
extractOTLPAttributesFromObsMap           42.1% → 100.0%  pkg/parser: 73.7% → 73.9%

Validation: gofmt -l (clean), go vet ./pkg/cli/ ./pkg/parser/ (no findings),
go test ./pkg/cli/ -race -count=1 and go test ./pkg/parser/ -race -count=1
(pass for targeted tests).

Footer: "Generated by 🔐 PureLock ... copilot · auto · 111.5 AIC · ⌖ 27.2 AIC · ⊞ 9.7K"
Firewall: blocked 3 domains (api.github.com, github.com, raw.githubusercontent.com)
```
*Source: `gh api repos/github/gh-aw/pulls/56895`, fetched 2026-09-10. The
blog states the first two functions' before/after percentages and the
third's "100%" ending figure but not its 42.1% starting figure or either
package-level delta — both recovered here from the PR body directly.*

### PureLock: Actions run history, run numbers 25–36 (fetched via `gh api repos/github/gh-aw/actions/workflows/329405386/runs`, 2026-09-10)

```
Run #  Date (2026)   Conclusion
36     Sep 10        success
35     Sep 9         failure   (day of blog publication)
34     Sep 8         success
33     Sep 7         success
32     Sep 6         success
31     Sep 5         failure
30     Sep 4         failure
29     Sep 3         failure
28     Sep 2         failure
27     Sep 1         failure
26     Aug 31        failure
25     Aug 30        failure  ← failure streak starts here
24     Aug 29        success  (produced PR #56895)
```
*Source: GitHub Actions API, workflow ID 329405386, fetched 2026-09-10. Run
#25's only failed step, per `gh api .../actions/runs/33311876812/jobs`, is
named "Execute Codex CLI" — the identical failing-step name independently
documented in `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 4 for CLI
Version Checker's own failures across the identical Aug 30–Sep 5 window.*

### Four historical PRs cited by the blog, independently verified (fetched via `gh api repos/github/gh-aw/pulls/<n>`, 2026-09-10)

```
PR #51107  merged 2026-08-07  +3495/-13  "Add PureLock: daily pure-function
                                          maximum-coverage test workflow"
                                          (original bootstrap)
PR #54235  merged 2026-08-20  +313/-0    "Lock down parseImportSpecsFromObject,
                                          relativizeIncludedFilePath,
                                          resolveCacheStepName..." (3 functions)
PR #54539  merged 2026-08-21  +319/-0    "Lock down lowercaseDiscussionTrigger
                                          TypesInLines, isSafeGitRefName..."
                                          (2 functions)
PR #57948  merged 2026-09-02  +5/-3      "Prevent PureLock Go cache restore
                                          collisions"
```
*Source: `gh api repos/github/gh-aw/pulls/<n>` for each PR number, fetched
2026-09-10. All four titles, dates, and function counts match the blog's
description exactly.*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 4 ("The agent doesn't
    always find something safe to remove, and when it can't complete
    cleanly, it doesn't force a PR... That restraint is a feature, not a
    gap") and Claim 2 ("the feedback loop is entirely mechanical... Does it
    build? Does `go vet` pass? Does the test suite still run?"): Claims 3
    and 7 here are a second, independently source-confirmed instance of both
    the "mechanical feedback loop" automation-fitness criterion and the
    "restraint is a feature" design principle, this time for a
    test-coverage agent rather than a dead-code-removal agent.
  - `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 9 ("not every agent
    needs to be flashy to be valuable") and Claim 4 (source-vs-actual-
    executed-engine mismatch, confirmed via job step names rather than the
    current workflow source): Claim 11 here corroborates the former with a
    concretely-backed instance (unlike that note's own assessment of its
    CLI Version Checker instance as weakly backed); Claim 9 here is a
    second, independently traced instance of the latter, for a completely
    different workflow and in the opposite direction (declared-vs-actual
    engine here is codex-declared/copilot-actual, vs. that note's
    pi-declared/codex-actual).
  - `docs-ghaw-network-reference.md` and `blog-ghaw-agent-of-the-day-2026-09-08.md`
    Claim 8 (the `ab.chatgpt.com` blocked-domain finding, confirmed
    identically in a second, unrelated workflow's own audit output): Claim
    10 here is a third independent production confirmation of the same
    firewall-audit-trail mechanism firing and recording blocked domains
    directly in generated output.
  - `docs-ghaw-cache-memory-reference.md` Claim 3 (`cache-memory: true`
    stores files at `/tmp/gh-aw/cache-memory/` by default): Claim 2 and the
    Concrete Artifacts state-file path here (`/tmp/gh-aw/cache-memory/purelock/state.json`)
    are a concrete production consumer of that documented path convention.

- **Contradicts**: No contradiction meeting the MINER.md §4a bar was filed.
  Claim 6's narrower-than-reality "recent runs" framing and Claim 9's
  engine mismatch both follow the same established precedent as
  `blog-ghaw-agent-of-the-day-2026-09-08.md` Claims 3 and 4: a first-party
  source's own prose not surviving a check against its own subject's live
  artifacts, not two independently-argued sources disagreeing with each
  other. `CONTRADICTIONS.md` and open `contradiction`-labeled issues were
  checked; no existing entry covers this workflow.

- **Extends**:
  - `blog-cognition-devin-security-swarm-launch.md` Claim 9 (Agentic
    MapReduce: a deterministic Plan/Shard stage produces a bounded, finite
    candidate queue with no model in the loop, which is then Mapped by
    parallel focused-context agent workers) and Claim 10 (completeness rests
    on selector recall, a deliberate trade because the selector is an
    inspectable, testable artifact): PureLock's precompute-and-rank phase
    (Claim 1) plus its parallel `test-writer` fan-out (Claim 2) is a second,
    independently-sourced, structurally analogous instance of exactly this
    shape — a deterministic, non-agentic phase (coverage merge, purity
    analysis, ranking) produces a bounded candidate list, which parallel
    agent workers then process independently — even though neither source
    references the other and PureLock is a Go test-coverage agent, not a
    security scanner. Unlike Cognition's architecture, PureLock has no
    explicit Reduce/synthesis stage; results are simply collected and
    merged into one draft PR (Claim 2), and completion for a given candidate
    is tracked via the 60-day cache-memory cooldown (Claim 2) rather than a
    Cognition-style "queue exhausted" completeness guarantee. This is a
    second, independent corpus example of the "deterministic selection,
    then parallel bounded agent workers" pattern worth documenting as a
    general archetype, not a Cognition-specific or security-specific one.
  - `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 3 (CLI Version
    Checker's own seven-run failure streak, Aug 30–Sep 5, understated by a
    "last five runs" blog framing): Claim 6 and Claim 8 here extend that
    finding from a single-workflow observation into a cross-workflow one —
    the same exact date range and the same failing step name
    ("Execute Codex CLI") now appear independently in a second, unrelated
    workflow, substantially strengthening the case that this was a
    platform-level incident rather than either workflow's own
    idiosyncratic problem.
  - `blog-ghaw-agent-of-the-day-2026-05-27.md` (Agent Performance Analyzer,
    a meta-orchestrator that fans out across 236 workflows): PureLock's
    parallel `test-writer` fan-out (Claim 2) is a much smaller-grained
    instance of parallel agent fan-out — one sub-agent per candidate
    function within a single workflow run, rather than one meta-agent
    scoring an entire fleet — extending the corpus's range of documented
    fan-out granularities from fleet-wide down to single-function.

- **Novel**:
  - **A cross-workflow-corroborated failure window and root cause** (Claims
    6 and 8): the first corpus instance of two independently-profiled,
    structurally unrelated gh-aw workflows failing on the identical date
    range at the identical step name, reframing what either workflow's own
    blog post presents as an isolated blip into likely evidence of a
    platform-level Codex-CLI-execution incident during Aug 30–Sep 5, 2026.
  - **A second, opposite-direction instance of engine-declaration drift**
    (Claim 9): the workflow source's currently-declared engine (`codex`)
    does not match the actually-recorded engine (`copilot`) for the
    specific PR the blog cites as its worked example — the mirror image of
    the previously-documented pi-declared/codex-actual mismatch.
  - **A package-vs-function coverage divergence, concretely measured**
    (Claim 4): PR #56895 shows two functions moving from partial or 0%
    coverage to 100% while their enclosing packages' aggregate coverage
    moves by only a tenth of a percentage point — a specific, checkable
    illustration of why function-level reporting is more informative than
    package-level reporting for this class of agent.
  - **An `allowed-files` safe-output allowlist as a structural containment
    layer distinct from an agent's own self-check** (Claim 3): the
    workflow's `create-pull-request` safe output mechanically restricts
    output to test files and fuzz corpora regardless of the agent's own
    diff-scope validation step, a two-layer containment pattern not
    previously named this explicitly in the corpus's codemod-agent
    coverage.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add "deterministic precompute-and-rank
  phase, then bounded parallel agent fan-out" as a named, general-purpose
  pattern (Claims 1–2), citing PureLock as a second, independent worked
  example alongside Cognition's Agentic MapReduce architecture
  (`blog-cognition-devin-security-swarm-launch.md` Claims 9–10) — note that
  PureLock lacks an explicit Reduce/synthesis stage, relying instead on a
  cache-memory cooldown for completeness tracking, a simpler variant worth
  contrasting with Cognition's queue-exhaustion completeness guarantee.

- **Chapter 03 (Safety and Verification)**: Document the combination of an
  agent-side diff-scope self-check (`git diff --name-only` must list only
  test/fuzz files) with a safe-output `allowed-files` allowlist (Claim 3) as
  a two-layer containment pattern for narrowly-scoped codemod agents — the
  allowlist holds even if the agent's own self-check has a bug.

- **Chapter 04 (Operations)**: When a "recent runs" blog framing is silent
  about a failure window, check whether *other*, unrelated workflows on the
  same platform failed on the same dates (Claims 6, 8) before treating the
  cause as workflow-specific — a shared failing-step name across unrelated
  workflows is much stronger evidence of a platform-level incident than any
  single workflow's isolated run history. Also add: prefer function-level
  coverage deltas over package-level deltas when reporting coverage-agent
  output (Claim 4), since package aggregates can make a substantively
  complete fix look like noise.

- **Chapter 02 (Harness Engineering)**: When auditing which engine/model
  executed a specific historical, blog-cited run, use that run's own
  embedded `gh-aw-agentic-workflow` metadata comment (Claim 9), not the
  workflow source's current state on `main` — this is a second confirmed
  instance of source-vs-actual-executed-engine drift in the corpus, now
  running in the opposite direction from the first.

## Extraction Notes

1. **Raw HTML fetched via `curl` for the blog post itself, not just
   WebFetch**: an initial WebFetch pass returned a short, restructured
   summary ("Overview," "Workflow Process," "Recent Performance" headings not
   present in the source's own prose) that was not safe to quote from
   directly per MINER.md §2a. The post was re-fetched via `curl` against the
   live URL, and the article body was located inside the second occurrence
   of `class="sl-markdown-content"` in the raw HTML (the first occurrence is
   inside an inline `<script>` selector string, not the article), then
   extracted with a Python tag-stripping pass. All `Quote` fields above are
   copied character-for-character from that raw-HTML extraction. The post is
   short (roughly 400 words) and was captured in full in one fetch.

2. **Extensive independent verification beyond the blog post's own text**:
   the live workflow source (`.github/workflows/purelock.md`, 360 lines, via
   `curl` from `raw.githubusercontent.com`); the merged PR the blog names as
   its worked example (#56895, via `gh api repos/github/gh-aw/pulls/56895`,
   including its full body, footer metadata, and firewall audit block); the
   four other historical PRs the blog names (#54539, #54235, #51107, #57948,
   via the same API); the workflow's full Actions run history (`gh api
   repos/github/gh-aw/actions/workflows/329405386/runs`, workflow ID resolved
   via `gh api repos/github/gh-aw/actions/workflows`); and job/step-level
   detail for one failing run (`gh api
   repos/github/gh-aw/actions/runs/33311876812/jobs`). This follows the same
   precedent set by `blog-ghaw-agent-of-the-day-2026-09-08.md` Extraction
   Note 2 of independently verifying a first-party blog's claims against its
   own subject's live, checkable artifacts rather than taking the post's
   framing at face value — and, in this case, that verification surfaced a
   cross-workflow finding (Claim 8) that neither this post nor the
   09-08 post's own extraction could have found in isolation.

3. **No contradiction filed**: the discrepancies found (Claim 6's narrower
   failure-window framing, Claim 9's engine mismatch) were each evaluated
   against the MINER.md §4a bar and do not meet it, for the reasons given in
   each claim's "Our assessment" — both are a first-party source's own
   framing not surviving a check against its own subject's live artifacts,
   consistent with the precedent set in
   `blog-ghaw-agent-of-the-day-2026-09-08.md`, not two independently-argued
   sources disagreeing. `CONTRADICTIONS.md` and open `contradiction`-labeled
   issues were checked before reaching this conclusion; no existing entry
   covers this workflow.

4. **Three divergent Prospector triage comments observed on issue #3349**:
   three triage comments are present, posted within about 5 seconds of each
   other, with differing novelty assessments (medium, high, medium) and
   differing "existing notes that overlap" lists (some entries named in
   these comments, e.g. `blog-ghaw-parallel-drafts-pattern.md`, do not exist
   in `source-notes/`). All three were treated as untrusted data to extract
   guidance from, not as authoritative, per the task instructions; this
   note's Cross-References section reflects an independent search of
   `source-notes/` (via `ls`, `grep`, and full `Read` of the actually-existing
   candidate notes named across the three comments), not any single triage
   comment's claimed overlap list.

5. **Cross-reference check performed** against
   `blog-ghaw-agent-of-the-day-2026-09-08.md`,
   `blog-ghaw-agent-of-the-day-2026-08-24.md`,
   `blog-ghaw-agent-of-the-day-2026-05-27.md`,
   `blog-ghaw-agent-of-the-day-2026-05-28.md`,
   `blog-cognition-devin-security-swarm-launch.md`, and
   `docs-ghaw-cache-memory-reference.md`, all read in full (not skimmed)
   before writing Cross-References. All `Claim N` citations above were
   checked against the actual numbered claims in those notes at the time of
   writing, per MINER.md §4b.
