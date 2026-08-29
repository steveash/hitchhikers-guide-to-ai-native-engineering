---
source_url: https://github.github.com/gh-aw/blog/2026-08-28-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – August 28, 2026: ESLint Refiner"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-08-28
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: settled
issue: "#3055"
---

# Agent of the Day – August 28, 2026: ESLint Refiner

> Profiles ESLint Refiner, a daily workflow that audits `gh-aw`'s own custom
> ESLint rule library (`eslint-factory`) for correctness rather than using
> those rules to check other code — the JS/TS-domain counterpart to Sergo's
> Go-linter-validation role in the existing three-workflow loop
> (`blog-ghaw-custom-linters-three-workflow-loop.md`). The blog post's
> two-paragraph description of the August 27 run was filled in substantially
> by fetching the live workflow source and the two filed issues and the
> discussion report it links to, which surface a self-detected memory-drift
> incident (repo-memory silently stale for ~7 weeks while the workflow kept
> running) not mentioned in the blog post at all.

## Source Context

- **Type**: blog-post (an "Agent of the Day" entry from the official GitHub
  Agentic Workflows blog, bylined "Copilot" — the same recurring gh-aw
  convention documented across this series, e.g.
  `blog-ghaw-agent-of-the-day-2026-08-26.md`. One agent profiled per post,
  distinct from the weekly changelog format.)
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team. The post cites two specific,
  independently-checkable GitHub Actions run IDs (33050923118, 33152652663)
  and two specific issue numbers (#56288, #56289), plus a linked discussion
  post (#56290) — all four fetched directly and read in full by this note
  (see Concrete Artifacts). This note additionally fetched the live workflow
  definition (`raw.githubusercontent.com/github/gh-aw/main/.github/workflows/eslint-refiner.md`)
  — the blog post's qualitative description of the workflow's discipline is
  corroborated in detail by all of these, and the fetched material surfaces
  several mechanics (tool restrictions, repo-memory scoping, a self-reported
  memory-staleness incident) not mentioned in the blog post's own text at all.
- **Scope**: One short post (~450 words) describing the workflow's mission
  and one day's findings (August 27), plus a one-sentence mention of the
  following day's clean run (August 28). Does NOT cover: the workflow's
  frontmatter configuration, its `tools:` restrictions, its `repo-memory`
  scoping, or the discussion report's own metrics and continuity note — all
  of which exist in the live workflow file and the linked discussion post but
  are unmentioned in the blog post's own text and were recovered by this note
  via direct source-file and issue/discussion fetches.

## Extracted Claims

### Claim 1: ESLint Refiner audits `eslint-factory`'s own custom lint rules for correctness against real call sites, in explicit contrast to a sibling workflow (`eslint-miner`) that invents roughly one new rule a day — and only files a finding when it is grounded in an actual bug, not a hypothetical one

- **Evidence**: Direct description in the post's opening and "Agent of the
  Day: ESLint Refiner" section.
- **Confidence**: settled (blog description directly corroborated by the
  fetched live workflow's own mission statement, which lists "Identify false
  positives, weak diagnostics, or missing edge cases" as mission step 2)
- **Quote**: "ESLint Refiner picks two of the least-scrutinized rules each
  run, checks their logic against real call sites in the codebase, and only
  files an issue when it finds something grounded in an actual bug — not a
  hypothetical."
- **Our assessment**: This is a distinct role from `eslint-miner` (invention)
  in the same rule-lifecycle sense that Sergo is distinct from Linter Miner
  in the Go three-workflow loop (`blog-ghaw-custom-linters-three-workflow-loop.md`
  Claim 3 — "Sergo acts as an adversarial testing layer for linters,
  specifically targeting precision gaps and suppression shortcomings"). This
  is the first corpus evidence that the invent/challenge pattern GitHub uses
  for its Go analyzer library (`eslint-factory`'s Go-side sibling, per that
  note) is replicated, by name, for the JS/TS `eslint-factory` rule set too
  — `eslint-miner` invents, `ESLint Refiner` challenges. For Ch02: document
  "rule-auditing agent" as a role distinct from "rule-inventing agent" that
  generalizes across at least two language ecosystems in the same codebase.

### Claim 2: The August 27 run reviewed exactly two rules (`require-mkdtempsync-try-catch`, `require-decodeuricomponent-try-catch`) and additionally ran a cross-cutting sweep that found the same wording defect — a "will crash the action if unhandled" overclaim — recurring across 11 rule files, despite having already been fixed once for a different rule and never propagated to siblings

- **Evidence**: Blog post narrative, corroborated and substantially extended
  by the filed issue #56288, which lists all 11 affected files with exact
  line numbers and states the prior fix location (#52644, for
  `require-fetch-response-body-try-catch`).
- **Confidence**: settled (both the blog's narrative and the underlying
  first-party issue, which lists concrete file:line locations, were read in
  full)
- **Quote**: "Eleven rules — including both reviewed that day — say a call
  “will crash the action if unhandled.” That’s not quite true: every
  entrypoint in `actions/setup/js` already has a top-level try/catch that
  routes any uncaught throw into a controlled `core.setFailed`, so nothing
  actually crashes silently. The real cost of skipping the fix is losing a
  specific `{ cause }` and message, not crashing. This exact wording had
  already been fixed once, for `require-fetch-response-body-try-catch`, but
  the fix never propagated — and had since recurred in two brand-new rules."
  (blog post) / "This exact defect was already identified and fixed for
  `require-fetch-response-body-try-catch` in #52644 (closed) — the wording
  there was reworded to describe the actual benefit (preserved cause /
  specific message) rather than claiming a crash. That fix was scoped
  narrowly to one rule and never propagated to its many siblings, so the
  same overclaim persists verbatim elsewhere... meaning the defect has
  already recurred once since the "fix."" (issue #56288 body)
- **Our assessment**: This is a concrete instance of a fix-propagation
  failure mode distinct from anything else currently in the corpus: a
  correction applied to one instance of a duplicated pattern (rather than to
  a shared abstraction) silently fails to reach its siblings, and — worse —
  new siblings created *after* the fix reintroduce the same defect, because
  nothing enforces the corrected wording at creation time. The agent's own
  fix request (see Claim 3) explicitly asks for a structural guard, not just
  a one-time reword, which is the mature response to this failure mode. For
  Ch03 (Safety and Verification): document "point fixes to duplicated
  patterns don't propagate on their own" as a caution, with this recurrence
  (fixed once, recurred twice since) as a concrete illustration of why a
  guard (shared constant, meta-test) is worth the extra effort over a single
  find-and-replace.

### Claim 3: Rather than only requesting the wording fix, the agent's issue #56288 explicitly asks for a structural guard — either a shared message-string constant/template all affected rules import, or a meta-test that scans all rule metadata for the offending phrase and fails the build if it recurs without an explicit allowlist entry

- **Evidence**: Issue #56288 body, "Ask" section, item 2.
- **Confidence**: settled (directly read from the first-party issue body;
  not mentioned in the blog post, which only describes the reword request in
  general terms)
- **Quote**: "To stop this recurring a third time (it already recurred once
  via two new eslint-miner-authored rules after the first fix), add a small
  guard: either a shared message-string constant/template that all these
  rules import, or a meta-test that scans `meta.messages`/`docs.description`
  across all rules for the phrase "will crash the action" and fails if it's
  reintroduced without an explicit allowlist entry."
- **Our assessment**: This is a specific, transferable engineering
  discipline: when an agent identifies a defect that has already recurred
  once despite a prior fix, the correct remediation request is not "fix it
  again" but "fix it and add a mechanical guard that makes the defect class
  structurally harder to reintroduce." The agent is reasoning about the
  fix-propagation failure mode itself (Claim 2), not just the current
  instances of it — a level of self-aware process correction not documented
  elsewhere in the corpus for an audit-class agent. For Ch02/Ch03: document
  "ask for a guard against recurrence, not just a fix for the current
  instances" as a concrete audit-agent reporting practice, especially
  valuable when the audit agent has direct evidence (via issue-tracker
  search) that the same defect class has already slipped through a prior
  fix once.

### Claim 4: The second finding — `require-decodeuricomponent-try-catch` misclassifying numeric, boolean, and `null` literal arguments as unsafe because it only special-cases string literals — was filed with zero live occurrences in the codebase, explicitly framed as a latent defect worth closing before any call site actually hits it, and explicitly cited as mirroring an already-fixed defect class in an unrelated rule (`prefer-number-isnan`)

- **Evidence**: Blog post narrative; issue #56289 body, "Grounding" and
  "Summary" sections.
- **Confidence**: settled (blog's narrative directly corroborated by the
  first-party issue, which additionally names the precedent rule and states
  the exact live call-site count)
- **Quote**: "`require-decodeuricomponent-try-catch` only recognized string
  literals as provably safe arguments, so calls like `decodeURIComponent(42)`
  or `decodeURIComponent(null)` got flagged even though a number, boolean, or
  `null` can never produce a decoding error. Zero live call sites hit this
  today, but it’s a cheap, well-scoped fix worth closing before one does —
  filed as issue #56289." (blog post) / "This mirrors a defect class the
  codebase has already fixed once for `prefer-number-isnan` (#43515 /
  #45064 — "autofix for provably-numeric args, drop misleading caveat"): a
  brand-new rule not yet special-casing an argument shape that is provably
  safe rather than actually dynamic." (issue #56289 body)
- **Our assessment**: The explicit "0 live occurrences today... but this is
  the rule's first review, so a design gap now is easiest to close before
  more callers accumulate" framing (issue #56289, "Grounding" section) is a
  proactive-fix rationale distinct from a strict "only fix grounded, live
  bugs" policy — the agent draws a line between filing a *hypothetical*
  finding (which its own mission statement forbids, per Claim 1) and filing
  a *provably-latent* one (a defect confirmed by code inspection to be real,
  just not yet triggered by any current call site). This is a useful,
  transferable distinction for audit-agent design: "zero live occurrences"
  is not the same bar as "hypothetical," and conflating them would either
  suppress real latent bugs or flood the tracker with speculation — the
  agent's own reasoning here threads that needle by requiring the defect
  itself (not just its trigger condition) to be proven.

### Claim 5: The workflow's discussion report for the August 27 run (a separate, linked artifact not summarized in the blog post) discloses that the workflow's own `repo-memory` had silently gone stale since 2026-07-08 — roughly seven weeks — even while the workflow continued running and filing issues daily throughout that period, and it rebuilt continuity by searching GitHub directly for its own prior issues rather than trusting its stored memory

- **Evidence**: Discussion #56290 body, "Grounding notes" collapsible
  section, "Continuity note."
- **Confidence**: settled (directly read from the first-party discussion
  report; not mentioned anywhere in the blog post)
- **Quote**: "this workflow's local repo-memory had gone stale since
  2026-07-08 even though the workflow kept running and filing issues daily
  (verified via GitHub issue search on the `eslint-refiner` tracker ID, 100
  issues found through 2026-08-26). Memory has been rebuilt from that ground
  truth and now records the gap explicitly so future runs don't need to
  re-derive it." (discussion #56290)
- **Our assessment**: This is the single most consequential finding in this
  source, and it is completely absent from the blog post's own framing
  (which only says the agent "kept" a discussion post noting "its own
  repo-memory had gone stale for weeks" — a soft paraphrase that undersells
  the mechanism and duration). The workflow ran, and successfully filed
  issues, for roughly seven weeks while its own persistence layer was
  silently disconnected from reality — the workflow's outputs (issue
  filings) were apparently still correct during this window (nothing in the
  discussion suggests filed issues were wrong), meaning the staleness was a
  *silent* failure of the continuity/self-awareness mechanism specifically,
  not of the audit function itself. This is a concrete, dated counter-example
  to any assumption that a `repo-memory`-backed workflow's memory reliably
  tracks its own operational history just because the workflow keeps
  running successfully — the two can diverge for extended periods without
  any error signal, and the divergence was only caught because the agent
  happened to cross-check against a ground-truth source (GitHub issue
  search) rather than because the platform surfaced a staleness warning.
  For Ch03 (Safety and Verification): document "operational success does
  not imply memory currency" as a named risk for any `repo-memory`-based
  continuity mechanism, and recommend periodic ground-truth reconciliation
  (as this workflow did, after the fact) as a mitigation — ideally on a
  schedule, not only when an agent happens to notice the gap.

### Claim 6: The ground-truth reconciliation search itself hit an unhandled scaling limit — it returned exactly 100 issues, the GitHub search API's page cap — and the agent's own "next actions" flagged this as unresolved, since it could not confirm whether more than 100 matching issues actually exist

- **Evidence**: Discussion #56290 body, "Continuity note" and "Next actions"
  sections.
- **Confidence**: settled (directly read from the first-party discussion
  report; not mentioned in the blog post)
- **Quote**: "Re-check for a second page of tracker-id search results next
  run (count hit exactly 100 today, the API page cap)." (discussion #56290,
  "Next actions")
- **Our assessment**: This is a small but concrete illustration of a
  self-correcting agent still leaving a known gap explicitly open rather than
  silently assuming completeness — the agent used a search result capped at
  exactly 100 as its ground truth for Claim 5's reconciliation, noticed the
  round number was suspicious, and explicitly deferred verification to a
  future run instead of asserting the memory rebuild was complete. This
  pairs with Claim 5 as a second layer of the same lesson: even the
  *recovery* mechanism from a memory-staleness incident can itself be
  silently truncated by an unrelated platform limit (API pagination), and
  disciplined reporting means flagging that residual uncertainty rather than
  treating the recovery as a clean resolution.

### Claim 7: The live workflow's `tools:` configuration grants no code-editing capability at all (`edit: null`) and restricts `bash` to four specific read-only commands, meaning the agent is structurally incapable of fixing the rules it audits — it can only file issues describing what should change

- **Evidence**: Live workflow source (`eslint-refiner.md`), `tools:` block:
  `bash: [cat eslint-factory/package.json, find actions/setup/js -name
  "*.cjs" -type f, find eslint-factory/src/rules -name "*.ts" -type f, wc
  -l]`, `edit: null`, `github: {mode: gh-proxy, toolsets: [default,
  issues]}`.
- **Confidence**: settled (directly read from the first-party workflow
  source's `tools:` frontmatter; not mentioned in the blog post at all)
- **Quote**: (no direct quote from the blog post — the tool restrictions are
  not mentioned in the blog text; sourced from the live workflow file, cited
  by section name per MINER.md §4b: `tools:` block of
  `.github/workflows/eslint-refiner.md`)
- **Our assessment**: This is an architectural enforcement of the
  audit-only posture the blog post describes narratively ("checks their
  logic against real call sites... only files an issue") — rather than
  relying on the agent's prompt instructions alone to avoid making direct
  rule edits, the harness removes the capability outright (`edit: null`) and
  narrows `bash` to four specific, non-mutating discovery commands. This is
  a stronger, harness-enforced version of the read-only-audit posture already
  documented for Architecture Guardian (`blog-ghaw-agent-of-the-day-2026-05-20.md`
  Claim 6, `contents: read` only) and the CLI Consistency Checker
  (`blog-ghaw-agent-of-the-day-2026-08-26.md` Claim 7's provenance-scoped
  trust discussion) — this workflow goes further by also removing generic
  bash and edit access, not just restricting GitHub API permissions. For
  Ch02: document "capability removal over prompt discipline" as the stronger
  form of the read-only-audit pattern — an explicit `bash:` allowlist plus
  `edit: null` is a harness-level guarantee that survives even if the
  agent's reasoning goes wrong, unlike a prompt instruction alone.

### Claim 8: The workflow composes a shared operational baseline (`shared/daily-audit-base.md`, parameterized with a 1-day issue expiry and a title prefix) with its own separately configured `safe-outputs.create-issue` block, which sets a longer 7-day expiry, a `max: 3` cap, and `[eslint, cookie]` labels — meaning the same workflow run produces two categories of safe output with two different expiration windows

- **Evidence**: Live workflow source, frontmatter: `imports: [{uses:
  shared/daily-audit-base.md, with: {expires: 1d, title-prefix:
  "[eslint-refiner] "}}, shared/otlp.md, shared/reporting.md]` and
  `safe-outputs: {create-issue: {expires: 7d, labels: [eslint, cookie], max:
  3}}`.
- **Confidence**: settled (directly read from the first-party workflow
  source's frontmatter; not mentioned in the blog post, which does not
  discuss issue expiration or the `cookie` label at all)
- **Quote**: (no direct quote from the blog post — the dual-expiry
  configuration is not mentioned in the blog text; sourced from the live
  workflow file, cited by section name per MINER.md §4b: top-level
  frontmatter of `.github/workflows/eslint-refiner.md`)
- **Our assessment**: This is a concrete, dated production example extending
  `docs-ghaw-deterministic-agentic-patterns.md` Claim 10's "operational
  baseline import" pattern (`shared/daily-audit-base.md` bundling discussion
  publishing, reporting, and observability config): here the shared import
  is *parameterized* per-workflow (`with: {expires: 1d, title-prefix:
  ...}`) rather than used with defaults, and the importing workflow layers
  its own distinct `safe-outputs` configuration on top with a different
  expiry (7d, for the substantive rule-defect issues) than whatever the
  shared base's own 1-day-expiry artifact covers (presumably a lower-stakes
  daily status object). The `cookie` label additionally makes this
  workflow's findings issues eligible for Issue Monster's pre-approved
  dispatch queue, per the label-as-queue-contract pattern documented in
  `blog-ghaw-agent-of-the-day-2026-08-26.md` Claim 4 and
  `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 7 — confirmed directly:
  both issue #56288 and #56289 carry the `cookie` label. For Ch02: extend
  the "operational baseline import" pattern with the concrete detail that
  shared imports can be parameterized per-consuming-workflow via `with:`,
  and that a single workflow can layer multiple expiry windows for different
  output categories rather than using one blanket TTL.

### Claim 9: The workflow's `repo-memory` tool is narrowly scoped to a dedicated branch (`memory/eslint-refiner`) and a restricted file-glob (`*.json`, `*.jsonl` only), explicitly described as storing "historical ESLint rule refinement runs and diagnostics snapshots"

- **Evidence**: Live workflow source, `tools.repo-memory` block:
  `branch-name: memory/eslint-refiner`, `description: "Historical ESLint
  rule refinement runs and diagnostics snapshots"`, `file-glob: ["*.json",
  "*.jsonl"]`.
- **Confidence**: settled (directly read from the first-party workflow
  source's `tools:` frontmatter; not mentioned in the blog post)
- **Quote**: (no direct quote from the blog post — the repo-memory scoping
  is not mentioned in the blog text; sourced from the live workflow file,
  cited by section name per MINER.md §4b: `tools.repo-memory` block of
  `.github/workflows/eslint-refiner.md`)
- **Our assessment**: This is the exact configuration whose contents went
  stale for seven weeks per Claim 5 — a per-workflow, dedicated memory
  branch restricted to structured data files (not free-form notes), which
  makes the staleness incident more notable rather than less: even a
  narrowly-scoped, structured-data-only memory store can silently drift out
  of sync with the workflow's actual operational history. This is a concrete
  production instance to pair with `docs-ghaw-repo-memory-reference.md`'s
  abstract documentation of the `repo-memory` tool's configuration surface
  — a specific, named branch and glob restriction, now with a documented
  failure mode (Claim 5) attached to a real deployment of it.

## Concrete Artifacts

### ESLint Refiner: Workflow Frontmatter (full, live source)

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
evals:
  - id: eslint_trends_analyzed
    question: Did the agent analyze ESLint diagnostics trends to identify rule refinement opportunities?
  - id: refinements_reported
    question: Did the agent report actionable ESLint rule refinements or explain why no refinement was needed?
```

*Source: `.github/workflows/eslint-refiner.md`, fetched via `curl` from
`raw.githubusercontent.com/github/gh-aw/main/`, 2026-08-29. Note the bare
`schedule: daily` (no time constraint) — a plain instance of the fuzzy
daily-schedule family documented in
`docs-ghaw-fuzzy-schedule-specification.md`'s grammar (`daily-schedule =
"daily" [time-constraint]`, time-constraint optional), corroborating that
note rather than contradicting anything in the corpus.*

### ESLint Refiner: Mission and Scope (live source, prose body)

```
Mission (daily):
1. Review recent diagnostics and issue feedback for ESLint factory rules.
2. Identify false positives, weak diagnostics, or missing edge cases.
3. Propose 1-3 high-impact refinement tasks for TypeScript ESLint rules.
4. Create up to 3 non-duplicate issues with concrete acceptance criteria.
5. Persist strategy and findings in repo-memory for future runs.
6. Publish a daily discussion report with summary metrics.

Scope:
  In scope:    eslint-factory/**; JS/TS files in actions/setup/js/** as rule targets
  Out of scope: Go analysis rules; JavaScript outside actions/setup/js
```

*Source: `.github/workflows/eslint-refiner.md`, "Mission" and "Scope"
sections, fetched 2026-08-29.*

### Issue #56288 — Wording Overclaim (filed 2026-08-27, closed same day)

```
Title:   eslint-factory: 11 try/catch rules overclaim will-crash-the-action
         wording; precedent fix propagated incompletely
Opened:  2026-08-27T07:56:30Z
Closed:  2026-08-27T12:26:10Z  (~4h30m)
Labels:  cookie, eslint, eslint-factory
Affected files (11), with line numbers:
  require-fs-io-try-catch.ts:23        require-mkdtempsync-try-catch.ts:21
  require-fs-sync-try-catch.ts:25      require-rmsync-try-catch.ts:21
  require-mkdirsync-try-catch.ts:21    require-decodeuricomponent-try-catch.ts:22
  require-new-url-try-catch.ts:19      require-execsync-try-catch.ts:90
  require-execfilesync-try-catch.ts:90 require-fetch-try-catch.ts:87,91
Prior fix (never propagated): #52644, for require-fetch-response-body-try-catch
Ask: (1) reword all 11 to describe actual benefit (preserved `{ cause }` /
     specific message) instead of claiming a crash; (2) add a guard (shared
     message constant, or a meta-test scanning meta.messages/docs.description
     for the phrase) so it cannot recur a third time; (3) no detection-logic
     changes needed — wording/docs only.
Footer: "claude · agent · 223.2 AIC · 5.8K" tokens; expires 2026-09-03
        (7d from creation, matching safe-outputs.create-issue.expires: 7d)
```

*Source: github/gh-aw issue #56288, fetched directly via `gh issue view`,
2026-08-29.*

### Issue #56289 — Misclassified Literal (filed 2026-08-27, closed same day)

```
Title:   eslint-factory: require-decodeuricomponent-try-catch misclassifies
         safe numeric/boolean/null literal args as dynamic
Opened:  2026-08-27T07:56:31Z
Closed:  2026-08-27T12:17:28Z  (~4h20m)
Labels:  cookie, eslint, eslint-factory
Root cause: isStaticStringExpression / isDynamicArg
  (require-decodeuricomponent-try-catch.ts:44-57) only recognizes string
  Literal / no-expression TemplateLiteral / "+"-concatenation of statics as
  provably safe; numeric, boolean, and null Literal nodes fall through to
  isDynamicArg === true and get flagged, even though decodeURIComponent(42),
  decodeURIComponent(true), decodeURIComponent(null) can never throw
  (each coerces to a fixed, %-free string).
Grounding: 0 live occurrences in actions/setup/js today; all 5 non-test
  call sites pass genuinely dynamic string values.
Precedent: mirrors an already-fixed defect class in prefer-number-isnan
  (#43515 / #45064 — "autofix for provably-numeric args, drop misleading
  caveat").
Ask: extend isStaticStringExpression (or add a sibling check) to treat
  number/boolean/null Literal nodes as provably safe; add valid test cases
  for decodeURIComponent(42)/decodeURIComponent(true)/decodeURIComponent(null);
  explicitly scoped OUT: identifier-resolution (e.g. const SAFE = "abc")
  deferred as a separate, ungrounded project.
```

*Source: github/gh-aw issue #56289, fetched directly via `gh issue view`,
2026-08-29.*

### Discussion #56290 — Daily Report, 2026-08-27 (linked from the blog post, not summarized in it)

```
Title: [eslint-refiner] ESLint Refiner — Daily Report (2026-08-27)
Category: Audits
State: closed (state_reason: outdated), 1 comment

Key metrics:
  Rules in index.ts: 60 (up from 12 tracked in this workflow's last local
    memory sync — most growth from sibling eslint-miner, ~1 new rule/day)
  Issues filed today: 2
  Live call sites checked: 5 (decodeURIComponent/decodeURI) + 9 (fs.mkdtempSync)
  True negatives confirmed: 1 decode call + 6 mkdtemp calls (already
    correctly wrapped)
  Live true positives (real unwrapped call sites correctly flagged by the
    rules — app bugs, not rule bugs, out of this workflow's scope): 3
    decodeURIComponent sites, 3 mkdtempSync sites

Continuity note: "this workflow's local repo-memory had gone stale since
  2026-07-08 even though the workflow kept running and filing issues daily
  (verified via GitHub issue search on the eslint-refiner tracker ID, 100
  issues found through 2026-08-26). Memory has been rebuilt from that
  ground truth and now records the gap explicitly so future runs don't
  need to re-derive it."

Next actions:
  - Re-check for a second page of tracker-id search results next run
    (count hit exactly 100 today, the API page cap).
  - Candidates for next review (lowest historical issue-search hit counts):
    no-throw-plain-object, no-json-stringify-equality,
    no-unsafe-promise-catch-error-property,
    prefer-get-error-message-over-string, require-fs-close-sync,
    require-execfilesync-try-catch, require-fs-io-try-catch,
    require-fetch-timeout, require-error-code-for-github-api-throw.
  - Verify the "will crash the action" reword lands across all 11 files.

Footer: "claude · agent · 223.2 AIC · 5.8K" tokens; expires 2026-08-28
        (1d from creation, matching the shared/daily-audit-base.md
        with: {expires: 1d} parameterization)
```

*Source: github/gh-aw discussion #56290, fetched directly via `gh api
repos/github/gh-aw/discussions/56290`, 2026-08-29.*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-custom-linters-three-workflow-loop.md` Claim 3 (Sergo as an
    adversarial testing layer for Go linters, targeting precision gaps and
    suppression shortcomings): ESLint Refiner is the same role — rule
    correctness auditing, not rule application — replicated for the JS/TS
    `eslint-factory` rule set, with `eslint-miner` playing the Linter Miner
    "invent" role (Claim 1 here).
  - `blog-ghaw-agent-of-the-day-2026-08-26.md` Claim 5 (evals check outcome —
    "issue created OR noop" — not the underlying mechanism) and Claim 6
    ("report the negative space" as a zero-false-positive-reporting
    discipline): ESLint Refiner's discussion report (Claim 6 here) itemizes
    true negatives and true positives alongside its two filed issues,
    another concrete instance of reporting full coverage, not just findings.
  - `docs-ghaw-fuzzy-schedule-specification.md` Claim 1 (four fuzzy schedule
    families, including a bare `"daily"` form with optional time-constraint):
    this workflow's `schedule: daily` (Concrete Artifacts) is a plain
    production instance of that documented grammar — corroboration, not the
    contradiction that a different cron pattern raised in
    `blog-ghaw-agent-of-the-day-2026-08-26.md` Claim 3 / contradiction issue
    #3043 (that contradiction concerned weekday-only raw-cron patterns, a
    different schedule family; it is unaffected by this note).
  - `docs-ghaw-deterministic-agentic-patterns.md` Claim 10 (`shared/daily-audit-base.md`
    as an "operational baseline import" bundling discussion publishing,
    reporting, and OTLP observability): this workflow's `imports:` block
    (Claim 8 here) is a concrete, parameterized production use of exactly
    that shared file.
  - `blog-ghaw-agent-of-the-day-2026-08-26.md` Claim 4 and
    `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 7 (the `cookie` label
    as Issue Monster's required pre-filter): both issues filed by this
    workflow (#56288, #56289) carry the `cookie` label, a third confirmed
    producer into that same dispatch queue.

- **Contradicts**: None identified. Reviewed `CONTRADICTIONS.md` (no
  existing entries touching `repo-memory` staleness, ESLint-domain linting,
  or the `daily` fuzzy-schedule form) and the source notes cited throughout
  this note. No contradiction issue filed.

- **Extends**:
  - `blog-ghaw-conformance-eslint-feedback-loop.md` Claim 7 ("ESLint Miner"
    mines issues/discussions, scans one target directory, selects one
    low-false-positive rule, opens at most one draft PR per run): that note
    documents the JS/TS rule-*inventing* half of this ecosystem in detail
    (naming it "ESLint Miner"); this note documents the rule-*auditing* half
    by the closely related name `eslint-miner`'s sibling, `eslint-refiner`
    — read together, the two notes now cover both halves of a JS/TS-domain
    invent/challenge pair structurally parallel to the Go-domain Linter
    Miner/Sergo pair in `blog-ghaw-custom-linters-three-workflow-loop.md`.
    (Note: this note did not independently verify that "ESLint Miner" in
    that note and "eslint-miner" mentioned here are the exact same workflow
    file, only that both names describe a rule-inventing workflow for the
    same `actions/setup/js` / `eslint-factory` domain — worth confirming in
    a future source pass if either workflow is profiled directly.)
  - `docs-ghaw-repo-memory-reference.md` (abstract documentation of the
    `repo-memory` tool's configuration surface, branch naming, and file-glob
    scoping): Claim 9 here is a concrete, named production instance
    (`memory/eslint-refiner` branch, `*.json`/`*.jsonl` glob), and Claim 5
    adds a documented failure mode (silent multi-week staleness despite
    continuous successful operation) not present in that reference note.
  - `blog-ghaw-agent-of-the-day-2026-05-20.md` Claim 6 (Architecture
    Guardian's read-only posture via `contents: read` permissions only):
    Claim 7 here shows a stronger, harness-level version of the same
    restraint — `edit: null` plus a four-command `bash:` allowlist, removing
    edit capability outright rather than relying on permission scoping alone.

- **Novel**:
  - **A documented, dated instance of `repo-memory` silently going stale for
    ~7 weeks during continuous successful operation, self-detected via a
    ground-truth reconciliation search** (Claim 5): no existing corpus note
    documents a memory-continuity mechanism failing silently while the
    workflow's primary function (filing issues) continued to succeed. This
    is the first evidence in the corpus that "the workflow keeps running
    without errors" does not imply "the workflow's memory of its own history
    is current."
  - **The reconciliation search itself hitting an unhandled API page cap
    (100 results), explicitly flagged as unresolved rather than assumed
    complete** (Claim 6): a second-order caution about recovery mechanisms
    themselves being subject to silent truncation, not previously documented.
  - **"Ask for a guard against recurrence, not just a fix for current
    instances" as an audit-agent remediation-request pattern** (Claim 3):
    the agent's explicit reasoning that a defect which already recurred once
    despite a prior fix warrants a structural guard (shared constant or
    meta-test), not a second one-off fix, is a specific process-maturity
    marker not previously named in the corpus for an audit-class agent.
  - **The "provably latent, not hypothetical" distinction for zero-live-
    occurrence findings** (Claim 4): a specific line an audit agent draws
    between filing a speculative concern (forbidden by its own mission) and
    filing a real defect confirmed by code inspection but not yet triggered
    by any current call site — not previously articulated this precisely in
    the corpus.
  - **`edit: null` plus a narrow, explicit `bash:` command allowlist as
    harness-enforced (not just permission-scoped) read-only audit posture**
    (Claim 7): the corpus has documented `contents: read`-only permission
    scoping for read-only agents before, but not the combination of removing
    the generic `edit` tool entirely and restricting `bash` to four literal,
    non-mutating commands.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add "rule-auditing agent" (Claim 1)
  as a named role in the rule-lifecycle pattern already documented for Go
  (`blog-ghaw-custom-linters-three-workflow-loop.md`), now confirmed
  replicated for JS/TS by name (`eslint-miner` invents, `eslint-refiner`
  audits). Extend the "operational baseline import" pattern
  (`docs-ghaw-deterministic-agentic-patterns.md` Claim 10) with the concrete
  detail that shared imports can be parameterized per-consumer via `with:`
  and that a single workflow can carry multiple `expires:` windows for
  different safe-output categories (Claim 8). Add "capability removal over
  prompt discipline" (Claim 7) as the stronger form of the read-only-audit
  pattern — `edit: null` plus an explicit `bash:` allowlist as a
  harness-level guarantee.

- **Chapter 03 (Safety and Verification)**: Add "operational success does
  not imply memory currency" (Claim 5) as a named risk for any
  `repo-memory`-based continuity mechanism, with a recommendation for
  scheduled ground-truth reconciliation rather than relying on an agent to
  notice the gap unprompted. Pair with Claim 6's caution that even the
  reconciliation mechanism itself can be silently truncated by an unrelated
  platform limit (search API pagination) — recommend logging and re-checking
  capped result counts rather than treating them as complete. Add "ask for a
  guard against recurrence, not just a fix" (Claim 3) and the
  "provably-latent vs. hypothetical" distinction (Claim 4) as concrete
  audit-agent remediation-request and filing-threshold practices.

- **Chapter 04/Ch09 (Operations / Multi-Agent Coordination)**: Note the
  third confirmed producer (alongside the CLI Consistency Checker and the
  workflows in the Aug 25/26 notes) into Issue Monster's `cookie`-labeled
  dispatch queue (Claim 8), reinforcing label-as-queue-contract as a
  recurring, multi-instance composition pattern across independently
  profiled gh-aw agents.

## Extraction Notes

1. **Blog post is short (~450 words); primary depth came from four fetched
   sub-pages**, within MINER.md §1's "up to 5" budget: the live workflow
   source (`eslint-refiner.md`), issue #56288, issue #56289, and discussion
   #56290 (fetched via `gh issue view` / `gh api repos/.../discussions/56290`
   against `github/gh-aw`, a different repository than this guide's own).
   Claims 3, 5, 6, 7, 8, and 9, and most of Concrete Artifacts, rely on this
   sub-page material — none of it is present in the blog post's own text.
   The blog post's text alone would have supported Claims 1, 2 (partially —
   the file list and line numbers came from the issue), and 4 (partially).

2. **Verbatim blog quotes obtained via direct HTML fetch with inline `<code>`
   spans converted to backticks, not WebFetch summarization**: an initial
   WebFetch call against the blog URL returned a structured, paraphrased
   summary (correct in substance but not quotable verbatim — e.g. it
   compressed "Eleven rules... say a call 'will crash the action if
   unhandled'" into "Eleven rules claimed violations 'will crash the action
   if unhandled'," which changes the wording). Per MINER.md §2a, the page
   was re-fetched directly via `curl` and parsed with a Python regex pass
   that converts `<code>` tags to backticks (rather than stripping them,
   which would have visually fragmented inline-code sentences and risked
   sentence-splicing) before stripping remaining tags. All blog-post quotes
   above are copied character-for-character from that pass, including
   original curly quotation marks and em-dashes.

3. **Cross-reference check performed** against
   `blog-ghaw-custom-linters-three-workflow-loop.md`,
   `blog-ghaw-conformance-eslint-feedback-loop.md`,
   `blog-ghaw-agent-of-the-day-2026-08-25.md`,
   `blog-ghaw-agent-of-the-day-2026-08-26.md`,
   `docs-ghaw-deterministic-agentic-patterns.md`,
   `docs-ghaw-fuzzy-schedule-specification.md`,
   `docs-ghaw-repo-memory-reference.md`, `docs-ghaw-dailyops.md`, and
   `CONTRADICTIONS.md`, all read in full (not skimmed) before writing
   Cross-References. All `Claim N` citations above were checked against the
   actual numbered claims in those notes at the time of writing, per
   MINER.md §4b.

4. **No contradiction filed**: The bare `schedule: daily` form corroborates
   `docs-ghaw-fuzzy-schedule-specification.md`'s documented grammar rather
   than conflicting with it, and is a different schedule family than the
   weekday-only raw-cron pattern at issue in contradiction #3043 — that
   existing contradiction is unaffected by anything in this note.

5. **`eslint-miner` vs. "ESLint Miner" naming not independently resolved**:
   this blog post names the sibling rule-inventing workflow `eslint-miner`
   (lowercase, hyphenated, as a code-formatted workflow name); the
   Aug 23 conformance post names a rule-inventing workflow "ESLint Miner"
   (title case, prose). Both describe a workflow that mines
   issues/discussions and proposes new lint rules for the same
   `actions/setup/js` domain, and this note treats them as very likely the
   same workflow (see Cross-References → Extends), but did not fetch
   `eslint-miner.md` directly to confirm the file-level identity — flagged
   rather than asserted as settled.

6. **No live occurrences double-checked**: this note did not independently
   re-run the grep/search described in issue #56289's "Grounding" section
   against the current state of `actions/setup/js` — the "0 live
   occurrences" and "5 live call sites" figures are taken as reported by the
   first-party issue, consistent with how call-site counts are handled in
   `blog-ghaw-agent-of-the-day-2026-08-26.md`.
