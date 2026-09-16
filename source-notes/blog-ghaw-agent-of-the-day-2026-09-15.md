---
source_url: https://github.github.com/gh-aw/blog/2026-09-15-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – September 15, 2026: ESLint Refiner"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-09-15
date_extracted: 2026-09-16
last_checked: 2026-09-16
status: current
confidence_overall: settled
issue: "#3476"
---

# Agent of the Day – September 15, 2026: ESLint Refiner

> A second "Agent of the Day" profile of ESLint Refiner (first covered
> `blog-ghaw-agent-of-the-day-2026-08-28.md`), built around a new September 14
> run: a genuinely subtle false-positive catch in
> `prefer-actions-exec-over-child-process` (files that `require("./shim.cjs")`
> don't get `@actions/exec` polyfilled), filed with exact line numbers and a
> control-case contrast. The blog's two-paragraph description was filled in
> substantially by fetching the live filed issue (#61044), the daily
> discussion report (#61045), and the current workflow source, which together
> surface four additional "no defect found" investigations, a dedup check
> against nine open issues, an apparent resolution of the Aug 28 note's
> repo-memory staleness incident, and a self-reported resource-heavy flag with
> a blocked call to `api.anthropic.com`, none of which appear in the blog
> post's own text.

## Source Context

- **Type**: blog-post (an "Agent of the Day" entry from the official GitHub
  Agentic Workflows blog, bylined "Copilot" — same recurring convention as
  `blog-ghaw-agent-of-the-day-2026-08-28.md` and the rest of this series).
- **Author credibility**: Official gh-aw platform team blog. The post cites a
  specific, independently-checkable Actions run
  (`github/gh-aw/actions/runs/34932497227`), a specific filed issue (#61044),
  and a specific linked discussion (#61045) — all three fetched directly and
  read in full by this note (see Concrete Artifacts), plus the live workflow
  source (`.github/workflows/eslint-refiner.md`), fetched fresh rather than
  reused from the Aug 28 note to confirm it had not changed.
- **Scope**: One short post (~450 words) describing the workflow's mission and
  one day's headline finding (the `prefer-actions-exec-over-child-process`
  false positive). Does NOT cover: the four other rules investigated that same
  run with no issue filed, the dedup check against previously-open issues, the
  workflow's repo-memory continuity status, or the resource-consumption
  numbers beyond the one sentence about being "resource-heavy" — all of which
  exist in the linked issue/discussion/workflow source but are absent from the
  blog post's own text and were recovered by this note via direct fetches.

## Extracted Claims

### Claim 1: ESLint Refiner's mission and audit-only posture are unchanged from the August 28 profile — daily review of `eslint-factory`'s custom rules against `actions/setup/js/**`, filing up to three non-duplicate issues with acceptance criteria, and publishing a daily discussion report
- **Evidence**: Live workflow source (`.github/workflows/eslint-refiner.md`),
  "Mission" section, fetched fresh on 2026-09-16 and compared line-for-line
  against the version captured in `blog-ghaw-agent-of-the-day-2026-08-28.md`
  Concrete Artifacts — identical frontmatter and prose body except for one
  cosmetic whitespace difference (a blank line removed under `network:`).
- **Confidence**: settled (directly diffed against a prior fetch of the same
  first-party file)
- **Quote**: "Mission (daily): 1. Review recent diagnostics and issue feedback
  for ESLint factory rules. 2. Identify false positives, weak diagnostics, or
  missing edge cases. 3. Propose 1-3 high-impact refinement tasks for
  TypeScript ESLint rules." (live workflow source, "Mission" section)
- **Our assessment**: This confirms the workflow's deployed configuration —
  including the `edit: null` / four-command `bash:` allowlist / repo-memory
  scoping to `memory/eslint-refiner` documented in the Aug 28 note's Claims 7
  and 9 — has not drifted in the roughly three weeks between the two profiled
  runs (2026-08-27 and 2026-09-14/15). For Ch02: this is confirmation, not new
  evidence, that the audit-only harness configuration is a stable production
  setting rather than a one-off.

### Claim 2: The rule `prefer-actions-exec-over-child-process` assumes any file carrying the `/// <reference types="@actions/github-script" />` marker always runs inside a github-script step where `@actions/exec`'s `exec()` global is available — an assumption that breaks for files that also `require("./shim.cjs")`, because `shim.cjs` polyfills `core`/`context` but never `exec`
- **Evidence**: Blog post narrative; issue #61044 body, "Summary" and "Live
  evidence" sections, which additionally quote `shim.cjs`'s own docstring and
  enumerate exactly which globals it polyfills.
- **Confidence**: settled (blog's narrative directly corroborated by the
  first-party issue, which quotes the source file's docstring and lists the
  exact polyfilled property set)
- **Quote**: "The rule `prefer-actions-exec-over-child-process` flags any
  `child_process.exec`/`execSync`/`execFile` call inside a file that carries
  the `<reference types="@actions/github-script" />` marker, on the
  assumption that such files always run inside a GitHub Actions `github-script`
  step where the `@actions/exec` global is available." (blog post) / "`shim.cjs`
  ... only polyfills `core.{debug,info,notice,warning,error,setFailed,setOutput,setSecret}`
  and `context.{eventName,sha,ref,...}` — there is no `exec`/`io`/`github`/`getOctokit`
  shim at all." (issue #61044 body)
- **Our assessment**: This is a rule-logic false positive rooted in an
  incomplete execution-context model: the rule's marker check answers "is this
  a github-script-flavored file?" but not "does this specific invocation
  actually run inside a github-script step, or in one of the standalone
  fallback modes the codebase explicitly supports?" The two questions are
  conflated, and the fix (Claim 4/5) is exactly to separate them.

### Claim 3: The agent traced the false positive to two specific files with exact flagged line numbers — `merge_remote_agent_github_folder.cjs` (lines 194, 198, 207, 212, 215) and `build_checkout_manifest.cjs` (lines 52, 61) — and cited a third file, `get_current_branch.cjs`, as a contrasting true positive that must remain flagged because it lacks the `shim.cjs` fallback
- **Evidence**: Blog post narrative gives the line-number list; issue #61044
  body, "Live evidence" section, gives the same numbers plus the specific
  call shapes (`execFileSync("git", ...)`, `execFileSync("gh", ...)`) and the
  contrasting file.
- **Confidence**: settled (directly read from the first-party issue body,
  which cites exact line numbers and quotes the target file's own header
  docstring)
- **Quote**: "Flagged `execFileSync("git", [...])` calls at lines 194, 198,
  207, 212, 215 (all inside `sparseCheckoutGithubFolder`-style helpers) — 5
  call sites." / "Contrast with `actions/setup/js/get_current_branch.cjs`,
  which also carries the marker and calls `execSync` (line 21) but does
  **not** require `shim.cjs` — that file is correctly flagged as a true
  positive, since it has no standalone-execution fallback path." (issue
  #61044 body)
- **Our assessment**: Citing a specific control case that must *stay* flagged
  is the same "protect against over-correcting into a blanket suppression"
  discipline named in the blog post's own text (see Claim 5) — the agent
  doesn't just point at the bug, it identifies the boundary the fix must not
  cross. This is a transferable audit-agent practice: pair every "stop
  flagging X" finding with a "keep flagging Y" control case in the same
  report, so a fix implemented later can be tested against both.

### Claim 4: The root cause is that the rule's detection function gates entirely on a regex match against the triple-slash reference comment and never checks whether the file also requires `shim.cjs`
- **Evidence**: Issue #61044 body, "Root cause" section, which quotes the
  actual regex from `eslint-factory/src/rules/prefer-actions-exec-over-child-process.ts`.
- **Confidence**: settled (directly read from the first-party issue body,
  which quotes the rule's own source code; not mentioned in the blog post,
  which only names the rule and describes the failure narratively)
- **Quote**: "`eslint-factory/src/rules/prefer-actions-exec-over-child-process.ts`
  gates entirely on `isGitHubScriptModule(sourceCode)`, which only checks for
  the triple-slash reference comment: `const GITHUB_SCRIPT_REFERENCE_PATTERN
  = /<reference\\s+types=[\"']@actions\\/github-script[\"']\\s*\\/>/;` It
  never checks whether the file also `require(\"./shim.cjs\")`" (issue #61044
  body, "Root cause")
- **Our assessment**: The issue names the exact function and even quotes the
  regex literal — this is a code-level root-cause citation, not just a
  behavioral description, which is a stronger evidentiary standard than the
  blog post's own prose achieves alone. For Ch03: a rule-auditing agent that
  can point at the specific gating expression responsible for a false
  positive (rather than describing symptoms only) produces a fix request a
  human reviewer can verify without re-deriving the root cause themselves.

### Claim 5: The proposed fix is a `requiresShimCjs()` guard checked alongside the existing marker check, with acceptance criteria that explicitly require the two false-positive files to stop triggering while `get_current_branch.cjs` continues to be flagged, plus a dedicated regression test
- **Evidence**: Blog post narrative; issue #61044 body, "Suggested fix" and
  "Acceptance criteria" sections.
- **Confidence**: settled (blog's summary corroborated in full by the
  first-party issue's explicit, checkbox-formatted acceptance criteria)
- **Quote**: "Add a `requiresShimCjs(sourceCode)` check (grep the file's
  `require(...)` calls for a literal `\"./shim.cjs\"` argument) alongside
  `isGitHubScriptModule`." / "`get_current_branch.cjs:21` (marker present, no
  `shim.cjs` require) continues to be flagged — the fix must not blanket-
  suppress all marker-gated files." (issue #61044 body)
- **Our assessment**: The acceptance criteria are written as verifiable,
  file:line-level assertions (two specific files stop firing; one specific
  file keeps firing; one new test case added) rather than a vague "fix the
  false positive" directive — this is the same evidence-first reporting
  discipline documented for the Aug 27 run's issues (`blog-ghaw-agent-of-the-day-2026-08-28.md`
  Claims 2–4), now shown a second time on a structurally different defect
  (execution-context modeling rather than message-wording or literal
  classification).

### Claim 6: The same run investigated four additional rules and filed no issue for any of them, each with a specific, code-level reason recorded in the discussion report rather than a blanket "no issues found"
- **Evidence**: Discussion #61045 body, "Other rules reviewed, no issue
  filed" section (collapsible), covering `no-unsafe-promise-catch-error-property`,
  `prefer-get-error-message`, `prefer-get-error-message-over-string`, and
  `no-core-exportvariable-non-string`.
- **Confidence**: settled (directly read from the first-party discussion
  report; not mentioned anywhere in the blog post)
- **Quote**: "`no-unsafe-promise-catch-error-property` — has a real
  architectural gap: its `hasGuard` flag is set once per enclosing function
  and then blanket-suppresses *all* unsafe property accesses in that
  `.catch()` callback... Checked all 26 live `.catch((err|error) => {...})`
  call sites in `actions/setup/js`... Zero occurrences of the vulnerable
  shape... Not filed; flagged in memory as the first thing to re-check if new
  `.catch()` sites are added." (discussion #61045 body)
- **Our assessment**: This is the same "report the negative space" discipline
  documented in `blog-ghaw-agent-of-the-day-2026-08-26.md` Claim 6, now with a
  finer distinction worth naming explicitly: one of the four (`no-unsafe-promise-catch-error-property`)
  is not a clean pass — the agent identifies a genuine design gap in the
  rule's logic but declines to file because it found zero live occurrences of
  the vulnerable shape after checking all 26 call sites, and instead records
  it in memory as a standing watch item. That is a third category beyond
  "true negative, rule is fine" and "true positive, filed" — a "known latent
  rule weakness, not yet worth an issue" category, tracked for future
  re-evaluation rather than either filed or silently dropped.

### Claim 7: Before filing, the agent re-verified nine previously-open `eslint-factory` issues via a live `gh api` dedup check, confirming eight were still open and noting one (#59144) had dropped off the open list without being re-investigated
- **Evidence**: Discussion #61045 body, "Dedup check" section (collapsible).
- **Confidence**: settled (directly read from the first-party discussion
  report; not mentioned in the blog post)
- **Quote**: "60757, 60577, 60196, 59892, 59891, 59647, 59378, 59377 — all
  reconfirmed open. #59144 (`no-misplaced-error-code-definition`) has dropped
  off the open list since 2026-09-14 (fixed or expired via the auto-close TTL)
  and was not re-investigated this run." (discussion #61045 body)
- **Our assessment**: The agent explicitly declines to assert *why* #59144
  disappeared (fixed vs. expired) rather than guessing — a calibrated-uncertainty
  reporting habit consistent with Claim 6's "not filed, flagged as a watch
  item" pattern. This is a concrete, dated instance of live-dedup-before-filing
  as an anti-duplicate mechanism, distinct from (and complementary to) the
  short-lived-issue-replaces-stale-issue design documented in
  `blog-ghaw-conformance-eslint-feedback-loop.md` Claim 2 — that mechanism
  handles staleness *after* filing; this is a check performed *before* filing.

### Claim 8: The workflow's repo-memory now reports its rule count as current — "62 rules... unchanged since 2026-09-10" — appearing to have resolved the ~7-week silent staleness incident documented in the Aug 28 profile
- **Evidence**: Discussion #61045 body, opening paragraph: "Scope stayed
  within `eslint-factory/**` (62 rules, unchanged since 2026-09-10) targeting
  `actions/setup/js/**`." Compared against `blog-ghaw-agent-of-the-day-2026-08-28.md`
  Claim 5 (memory silently stale from 2026-07-08 until rediscovered and
  rebuilt around 2026-08-27) and that note's Concrete Artifacts (60 rules as
  of the Aug 27 run).
- **Confidence**: emerging (the September run's memory now cites a specific,
  recent last-changed date rather than a stale one, which is consistent with
  a successfully rebuilt and currently-tracking memory — but this note did
  not independently verify the accuracy of "unchanged since 2026-09-10"
  against `eslint-factory`'s actual git history, so "resolved" is an inference
  from the absence of a staleness symptom, not a confirmed fix)
- **Our assessment**: If accurate, this is a positive follow-up data point for
  Ch03's "operational success does not imply memory currency" caution
  (`blog-ghaw-agent-of-the-day-2026-08-28.md` Claim 5's Guide Impact): the
  same `repo-memory`-backed workflow, after its staleness was caught and
  manually reconciled once, is now citing a specific recent date rather than
  a stale one roughly seven weeks later — weak evidence that the one-time
  ground-truth reconciliation (Claim 5/6 in that note) produced a durable fix
  rather than a one-off patch. This is not proof of a systemic fix (a single
  data point can't establish that), but it is the first corpus evidence of a
  `repo-memory` incident being followed up on in a later run at all.

### Claim 9: gh-aw's own audit tooling flagged the run as resource-heavy for its task domain — 83 turns and 89,000 tokens against a 45-minute budget — and the run also had one network request blocked by the firewall, to `api.anthropic.com`, which is not in the workflow's `network.allowed` list
- **Evidence**: Blog post, closing narrative paragraph; issue #61044's
  auto-appended firewall warning box, which names the exact blocked domain.
- **Confidence**: settled (directly stated in both the blog post and the
  first-party issue's auto-generated firewall-block callout, which are
  independent artifacts of the same run)
- **Quote**: "The run wasn't flawless — gh-aw's own audit tooling flagged it
  as resource-heavy for its task domain, burning 83 turns and 89k tokens
  against a 45-minute budget, with one blocked network request to
  `api.anthropic.com`. That's useful signal in its own right: even a workflow
  that ships a precise, well-evidenced result can still be a candidate for
  tightening, and gh-aw's audit pipeline calls that out automatically rather
  than letting a "success" status hide the cost." (blog post) / "Firewall
  blocked 1 domain ... The following domain was blocked by the firewall
  during workflow execution: `api.anthropic.com`" (issue #61044, auto-appended
  warning box)
- **Our assessment**: The blocked domain is notable specifically because the
  workflow's `engine: claude` implies model inference for this very run goes
  somewhere — and `network.allowed` here is `[defaults, github, node]`, which
  does not include `api.anthropic.com`. This is consistent with (not
  contradicting) `docs-ghaw-awf-reflect-reference.md` Claim 3's documented
  prohibition on hardcoding direct upstream model API URLs in shared workflow
  logic ("all inference requests should go through the AWF gateway"): the
  firewall block is exactly the kind of enforcement that prohibition implies
  — something in the run's toolchain attempted a direct call to
  `api.anthropic.com` and was blocked rather than silently allowed, which
  keeps inference routed through the gateway. This note cannot identify what
  specifically attempted the direct call (a dependency, a stray default in
  the underlying SDK, etc.) — flagged as an open question, not resolved here.
  Separately, "resource-heavy for its task domain" as an automated
  self-flagging mechanism is consistent with the `agentic-observability-kit`
  behavior documented in `blog-ghaw-weekly-2026-04-06.md` Claim 9 ("it flags
  resource-heavy patterns and files issues when thresholds are crossed"),
  though this note did not confirm the two tools are the same system — the
  blog post says only "gh-aw's own audit tooling," which could equally refer
  to the `gh aw audit` CLI command documented in
  `docs-ghaw-troubleshooting-debugging.md` Claim 4 (token/cost metrics per
  run). Both are plausible; not disambiguated here.

### Claim 10: The workflow's `safe-outputs.create-issue` labels (`eslint`, `cookie`) place issue #61044 into Issue Monster's pre-approved dispatch queue, matching the Aug 28 note's documented `cookie`-label pattern
- **Evidence**: Issue #61044's labels, fetched via `gh issue view`:
  `cookie`, `eslint`, `eslint-factory`.
- **Confidence**: settled (directly observed on the first-party issue; the
  `cookie` label's role as a dispatch-queue contract is documented, not
  re-derived, by this note — see Cross-References)
- **Quote**: (no direct quote from the blog post — labels are not mentioned
  in the blog text; sourced from the live issue's label list, cited by field
  name per MINER.md §4b: `labels` field of issue #61044)
- **Our assessment**: A fourth confirmed producer (after the CLI Consistency
  Checker and the two Aug 25/26-profiled workflows, plus ESLint Refiner's own
  Aug 27 issues per the prior note) into the same `cookie`-labeled queue —
  reinforcing that this is a stable, multi-instance production convention
  rather than a one-off observation.

### Claim 11: The run left an explicit, prioritized backlog rather than declaring the sweep complete — one rule (`require-error-code-in-thrown-error`) deferred for a second consecutive run, and roughly 25 of the tracked 62 rules never yet reviewed by this workflow's memory
- **Evidence**: Discussion #61045 body, "Next actions" section.
- **Confidence**: settled (directly read from the first-party discussion
  report; not mentioned in the blog post)
- **Quote**: "`require-error-code-in-thrown-error` — deferred two runs in a
  row now; needs a targeted sampling pass (custom Error subclasses / unusual
  message-expression shapes across 100+ importing files) rather than
  exhaustive review. Top priority for next run." / "~25 of 62 rules remain
  never-reviewed by this memory (fs/exec/fetch try-catch family mostly)."
  (discussion #61045 body, "Next actions")
- **Our assessment**: Explicitly quantifying the unreviewed backlog (~25/62)
  and naming a specific rule as deferred twice, with a stated reason
  (requires targeted sampling, not exhaustive review, given 100+ importing
  files) rather than another blanket deferral, is a coverage-transparency
  practice: a reader of the discussion history can tell exactly how much of
  the rule surface this workflow has and hasn't gotten to, rather than
  inferring completeness from the absence of open issues.

## Concrete Artifacts

### Issue #61044 — `prefer-actions-exec-over-child-process` False Positive (filed 2026-09-15, open as of 2026-09-16)

```
Title:   prefer-actions-exec-over-child-process false positive on dual-mode
         standalone/github-script files
Opened:  2026-09-15T05:40:24Z
State:   OPEN (not yet closed as of this note's extraction, 2026-09-16 —
         unlike the Aug 27 pair of issues, which closed same-day)
Labels:  cookie, eslint, eslint-factory

Files affected, with exact flagged lines:
  merge_remote_agent_github_folder.cjs: 194, 198, 207, 212, 215
    (execFileSync("git", [...]) inside sparseCheckoutGithubFolder-style
    helpers; require("./shim.cjs") at line 26)
  build_checkout_manifest.cjs: 52, 61
    (execFileSync("git", ...) / execFileSync("gh", ...) inside
    resolveDefaultBranch(); require("./shim.cjs") at line 4)

Control case (must remain flagged):
  get_current_branch.cjs:21 — carries the marker, calls execSync, but has
  no shim.cjs require / standalone fallback path.

Root cause: isGitHubScriptModule() in
  eslint-factory/src/rules/prefer-actions-exec-over-child-process.ts gates
  only on the triple-slash reference regex; never checks for a shim.cjs
  require.

Suggested fix: add requiresShimCjs(sourceCode) — grep require(...) calls
  for a literal "./shim.cjs" argument — alongside isGitHubScriptModule().

Acceptance criteria:
  [ ] build_checkout_manifest.cjs (52, 61) and
      merge_remote_agent_github_folder.cjs (194, 198, 207, 212, 215) stop
      triggering, OR the diagnostic is adjusted to note the standalone-mode
      caveat.
  [ ] get_current_branch.cjs:21 continues to be flagged.
  [ ] New test case added: a github-script-marked file that also requires
      shim.cjs produces no false-positive diagnostic.

Footer: "claude · agent · 406 AIC · ⌖ 7.86 AIC · ⊞ 5.8K"; expires
  2026-09-22T05:40:23.926Z (7d from creation, matching
  safe-outputs.create-issue.expires: 7d)

Auto-appended firewall warning:
  "Firewall blocked 1 domain ... api.anthropic.com" — not in this
  workflow's network.allowed: [defaults, github, node].
```

*Source: github/gh-aw issue #61044, fetched directly via `gh issue view`,
2026-09-16.*

### Discussion #61045 — Daily Report, 2026-09-15 (linked from the blog post, not summarized in it)

```
Title: [eslint-refiner] ESLint Refiner daily report - 2026-09-15
Category: General
State: closed (state_reason: outdated, auto-expired), 1 comment

Scope: eslint-factory/** (62 rules, unchanged since 2026-09-10) targeting
  actions/setup/js/**

Filed: prefer-actions-exec-over-child-process false positive (see issue
  #61044 above).

Other rules reviewed, no issue filed (4):
  no-unsafe-promise-catch-error-property — real architectural gap
    (hasGuard flag suppresses per-function, not per-access, unlike sibling
    no-unsafe-catch-error-property); checked all 26 live .catch() sites;
    zero occurrences of the vulnerable shape; not filed, flagged in memory
    as a watch item for new .catch() sites.
  prefer-get-error-message — checks out correctly; no live gap.
  prefer-get-error-message-over-string — correctly scope-gated; ~15 files
    use String(err) but don't import getErrorMessage — a codebase-adoption
    gap, not a rule defect.
  no-core-exportvariable-non-string — mirrors no-core-setoutput-non-string
    (3 grounded gaps found 2026-07-01), but all 22 live call sites pass
    string-typed values; one site (checkout_pr_branch.cjs:86) already
    proactively wraps with String(). No live reproduction of the sibling's
    gaps.

Dedup check (before filing): 60757, 60577, 60196, 59892, 59891, 59647,
  59378, 59377 reconfirmed open via gh api. #59144 dropped off the open
  list since 2026-09-14 (fixed or expired), not re-investigated this run.

Next actions:
  - require-error-code-in-thrown-error: deferred 2 runs in a row; needs a
    targeted sampling pass across 100+ importing files. Top priority next.
  - no-unsafe-promise-catch-error-property: real gap, ungrounded; re-check
    only if new .catch() sites appear.
  - ~25 of 62 rules remain never-reviewed by this memory (fs/exec/fetch
    try-catch family mostly).

Footer: "claude · agent · 406 AIC · ⌖ 7.86 AIC · ⊞ 5.8K"; expires
  2026-09-16T05:40:24.724Z (1d from creation, matching
  shared/daily-audit-base.md with: {expires: 1d})
```

*Source: github/gh-aw discussion #61045, fetched directly via `gh api
repos/github/gh-aw/discussions/61045`, 2026-09-16.*

### ESLint Refiner: Workflow Frontmatter (fetched 2026-09-16, diffed against the Aug 28 note's capture)

```yaml
private: true
on:
  schedule: daily
  workflow_dispatch: null
permissions:
  contents: read
  discussions: read
  issues: read
  pull-requests: read
network:
  allowed:
  - defaults
  - github
  - node
imports:
- uses: shared/daily-audit-base.md
  with:
    expires: 1d
    title-prefix: "[eslint-refiner] "
- shared/otlp.md
- shared/reporting.md
safe-outputs:
  create-issue:
    expires: 7d
    labels:
    - eslint
    - cookie
    max: 3
description: Daily ESLint rule refinement using diagnostics trends from actions/setup/js
emoji: 🤖
engine: claude
name: ESLint Refiner
strict: true
timeout-minutes: 45
tools:
  bash:
  - cat eslint-factory/package.json
  - find actions/setup/js -name "*.cjs" -type f
  - find eslint-factory/src/rules -name "*.ts" -type f
  - wc -l
  cli-proxy: true
  edit: null
  github:
    mode: gh-proxy
    toolsets:
    - default
    - issues
  repo-memory:
    branch-name: memory/eslint-refiner
    description: Historical ESLint rule refinement runs and diagnostics snapshots
    file-glob:
    - "*.json"
    - "*.jsonl"
tracker-id: eslint-refiner
```

*Source: `.github/workflows/eslint-refiner.md`, fetched via `curl` from
`raw.githubusercontent.com/github/gh-aw/main/`, 2026-09-16. Byte-for-byte
identical (modulo one blank-line whitespace difference under `network:`) to
the version captured in `blog-ghaw-agent-of-the-day-2026-08-28.md` on
2026-08-29 — the `evals:` block present in that earlier capture was not
re-transcribed here since it is unchanged; see that note for its contents.*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-agent-of-the-day-2026-08-28.md` Claim 1 (rule-auditing vs.
    rule-inventing role split, `eslint-miner` invents / `eslint-refiner`
    audits) and Claims 7–9 (harness-enforced read-only posture, dual-expiry
    safe-outputs, scoped repo-memory): this run's unchanged workflow
    frontmatter (Claim 1, Concrete Artifacts) confirms all of these as stable
    production configuration, not a one-off snapshot.
  - `blog-ghaw-agent-of-the-day-2026-08-26.md` Claim 6 ("report the negative
    space" — itemizing true negatives and true positives, not just findings):
    Claim 6 here extends this with a third category (a real rule weakness,
    zero live occurrences, deliberately not filed but tracked) beyond simple
    true-negative/true-positive reporting.
  - `blog-ghaw-agent-of-the-day-2026-08-26.md` Claim 4 and
    `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 7 (the `cookie` label as
    Issue Monster's dispatch-queue contract): Claim 10 here is a fourth
    confirmed producer into that queue.
  - `docs-ghaw-awf-reflect-reference.md` Claim 3 (inference must route through
    the AWF gateway, not hardcoded upstream URLs): the firewall block on
    `api.anthropic.com` (Claim 9) is a concrete instance of that constraint
    being enforced at the network layer, though this note cannot identify
    what in the toolchain attempted the direct call.
  - `docs-ghaw-troubleshooting-debugging.md` Claim 8 and
    `docs-ghaw-troubleshooting-common-issues.md` Claim 18 (firewall blocks on
    domains outside `network.allowed`): a further concrete, dated instance —
    here the blocked domain is the model provider's own API host, not a
    package registry, which is a domain-class not previously illustrated with
    a concrete example in this corpus's `network.allowed` coverage.

- **Contradicts**: None identified. Reviewed `CONTRADICTIONS.md` (9 entries,
  none touching `repo-memory` continuity, ESLint-domain linting, or
  `network.allowed`/gateway routing) and all source notes cited throughout
  this note. No contradiction issue filed.

- **Extends**:
  - `blog-ghaw-agent-of-the-day-2026-08-28.md` Claim 5 (repo-memory silently
    stale for ~7 weeks, self-detected and manually reconciled around
    2026-08-27): Claim 8 here is the first follow-up data point in the corpus
    showing that same memory citing a specific, recent last-changed date
    roughly seven weeks later — weak evidence of a durable fix, explicitly
    not confirmed independently by this note.
  - `blog-ghaw-conformance-eslint-feedback-loop.md` Claim 2 (short-lived
    issues that get replaced by a newer run rather than accumulating): Claim 7
    here documents a complementary anti-duplicate mechanism — a live dedup
    check performed *before* filing, rather than staleness handled *after*
    filing.
  - `blog-ghaw-weekly-2026-04-06.md` Claim 9 (the `agentic-observability-kit`
    "flags resource-heavy patterns and files issues when thresholds are
    crossed"): Claim 9 here may be the same underlying mechanism applied to
    this specific run (83 turns / 89k tokens vs. a 45-minute budget), or may
    instead be the separately-documented `gh aw audit` CLI
    (`docs-ghaw-troubleshooting-debugging.md` Claim 4) — not disambiguated by
    either source.
  - `blog-ghaw-agent-of-the-day-2026-08-28.md` Claims 2–4 (evidence-first
    issue filing with file:line specificity and structural-guard requests):
    Claims 3 and 5 here show the same discipline applied to a different
    defect class (execution-context modeling vs. message-wording/literal
    classification), reinforcing it as a general workflow trait rather than
    specific to the wording-overclaim incident.

- **Novel**:
  - **A live dedup check against a named list of previously-open issues,
    performed immediately before filing, with an explicit non-claim about why
    one issue disappeared from that list** (Claim 7): not previously
    documented as a distinct step from the after-the-fact stale-issue-
    replacement pattern.
  - **A three-way finding taxonomy (true negative / true positive / "real
    weakness, zero live occurrences, tracked not filed")** (Claim 6): a finer
    distinction than the binary "finding filed or not" framing used elsewhere
    in the corpus.
  - **A concrete instance of a firewall block on the model provider's own API
    domain (`api.anthropic.com`) rather than a package registry or
    third-party service** (Claim 9): the corpus's existing `network.allowed`
    coverage is dominated by package-registry and third-party-API examples;
    this is the first example where the blocked domain is the inference
    provider itself, connecting directly to the AWF-gateway-routing
    prohibition documented elsewhere.
  - **A same-workflow, same-role follow-up data point on a previously-
    documented incident (repo-memory staleness) roughly seven weeks later**
    (Claim 8): the corpus has not previously had the opportunity to check
    whether a documented incident recurred or was durably fixed, since most
    "Agent of the Day" profiles are one-off snapshots of different workflows.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add "pair every 'stop flagging X'
  finding with a 'keep flagging Y' control case" (Claim 3) as a concrete
  audit-agent reporting practice. Add the three-way finding taxonomy (Claim 6)
  as a refinement of the existing "report negative space" guidance. Add
  live-dedup-before-filing (Claim 7) alongside the existing short-lived-issue-
  replacement pattern as a second, complementary anti-duplicate mechanism.

- **Chapter 03 (Safety and Verification)**: Note Claim 8 as a tentative
  positive follow-up to the "operational success does not imply memory
  currency" caution already recommended from the Aug 28 note — flag it as
  weak, single-data-point evidence rather than a confirmed resolution. Add
  Claim 4's code-level root-cause citation (naming the exact gating function
  and regex) as a stronger evidentiary bar for audit-agent fix requests than
  a purely behavioral description.

- **Chapter 04 (Operations)**: Add the concrete `api.anthropic.com` firewall-
  block instance (Claim 9) as a specific illustration of
  `docs-ghaw-awf-reflect-reference.md` Claim 3's gateway-routing constraint
  being enforced at the network layer — worth flagging to practitioners that
  a blocked-domain warning naming the model provider's own API host is
  expected/correct behavior under that architecture, not necessarily a
  misconfiguration to "fix" by adding the domain to `network.allowed`.

## Extraction Notes

1. **Blog post is short (~450 words); primary depth came from three fetched
   sub-pages**, within MINER.md §1's "up to 5" budget: issue #61044
   (`gh issue view`), discussion #61045 (`gh api
   repos/github/gh-aw/discussions/61045`), and the live workflow source
   (`curl` against `raw.githubusercontent.com`). Claims 4, 6, 7, 8, 10, and 11,
   and most of Concrete Artifacts, rely on this sub-page material — none of it
   is present in the blog post's own text.

2. **Verbatim blog quotes obtained via direct HTML fetch, not WebFetch
   summarization**: an initial WebFetch call against the blog URL returned a
   paraphrased summary consistent in substance but not quotable verbatim (it
   also named the wrong issue-tracker workflow detail in one place). Per
   MINER.md §2a, the page was re-fetched via `curl` and parsed with a Python
   regex pass converting `<code>`/`<a>`/heading tags to Markdown-equivalent
   text before stripping remaining tags, then hrefs for each inline link
   (`workflow definition`, `most recent run`, `issue #61044`, `daily
   discussion report`) were extracted separately to locate the sub-pages. All
   blog-post quotes above are copied character-for-character from that pass.

3. **Cross-reference check performed** against
   `blog-ghaw-agent-of-the-day-2026-08-28.md`,
   `blog-ghaw-conformance-eslint-feedback-loop.md`,
   `blog-ghaw-custom-linters-three-workflow-loop.md`,
   `blog-ghaw-agent-of-the-day-2026-08-25.md`,
   `blog-ghaw-agent-of-the-day-2026-08-26.md`,
   `blog-ghaw-weekly-2026-04-06.md`, `docs-ghaw-awf-reflect-reference.md`,
   `docs-ghaw-troubleshooting-debugging.md`,
   `docs-ghaw-troubleshooting-common-issues.md`,
   `docs-ghaw-repo-memory-reference.md`, and `CONTRADICTIONS.md`, all read (in
   full or by targeted claim-list grep against already-deeply-read notes)
   before writing Cross-References. All `Claim N` citations above were
   checked against the actual numbered claims in those notes at the time of
   writing, per MINER.md §4b.

4. **No contradiction filed**: nothing in this run's findings materially
   opposes an existing source note. Claim 8 (apparent repo-memory resolution)
   is framed as weak/unconfirmed evidence rather than an assertion that would
   need reconciling against the Aug 28 note's staleness finding — both notes
   agree the staleness happened; this note only adds that a later run's
   self-report is no longer showing the symptom.

5. **Issue #61044 still open at extraction time**: unlike the Aug 27 issue
   pair (`blog-ghaw-agent-of-the-day-2026-08-28.md`, closed same day, ~4-4.5h
   each), issue #61044 (filed 2026-09-15T05:40:24Z) was still open when
   checked on 2026-09-16 — roughly one day old, well within its 7-day expiry.
   This is noted as a data point in Concrete Artifacts but not treated as a
   finding in itself, since one day is not long enough to draw any conclusion
   about typical time-to-close for this workflow's issues.

6. **`api.anthropic.com` block not root-caused**: this note could not
   determine, from the fetched artifacts, what specifically attempted the
   blocked direct connection (Claim 9) — flagged as an open question rather
   than speculated on.
