---
source_url: https://github.github.com/gh-aw/blog/2026-09-22-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – September 22, 2026: Sergo, the Serena Go Expert"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-09-22
date_extracted: 2026-09-23
last_checked: 2026-09-23
status: current
confidence_overall: settled
issue: "#3629"
---

# Agent of the Day – September 22, 2026: Sergo, the Serena Go Expert

> The first dedicated "Agent of the Day" profile of Sergo, previously known
> in the corpus only as the "challenge" role in
> `blog-ghaw-custom-linters-three-workflow-loop.md`'s three-workflow loop.
> This entry, filled in substantially by fetching the live workflow source
> (`sergo.md`), both filed issues (#62540, #62541), and the full daily
> discussion report (#62542), shows a same-week invent-then-audit handoff
> (a sibling workflow, Linter Miner, shipped the `uncheckedsliceindex`
> linter one day before Sergo found a systemic bug in it), a live
> re-verification of a previously auto-expired finding that surfaces a
> named, repeating failure mode of gh-aw's issue-expiry mechanism (7
> confirmed instances project-wide), and lifetime run statistics (74 runs,
> 473 findings, 129 tasks) that the blog's own "last three nights" framing
> does not surface.

## Source Context

- **Type**: blog-post (an "Agent of the Day" entry from the official GitHub
  Agentic Workflows blog, bylined "Copilot" — same recurring convention as
  the September profiles already in the corpus, e.g.
  `blog-ghaw-agent-of-the-day-2026-09-15.md`).
- **Author credibility**: Official gh-aw platform team blog, describing the
  team's own production repository (`github/gh-aw`). The post cites a
  specific Actions run (`github/gh-aw/actions/runs/35684470805`), two
  specific filed issues (#62540, #62541), a specific merged PR (#62408),
  and a specific linked discussion (#62542) — all four fetched directly and
  read in full by this note (see Concrete Artifacts), plus the live
  workflow source (`.github/workflows/sergo.md`).
- **Scope**: One short post (~500 words) describing Sergo's mission and one
  night's headline finding (the `uncheckedsliceindex` selector-base bug).
  Does NOT cover: the second finding filed the same run (the
  `bufioscannererunchecked` reverse-phantom refiling gets one paragraph but
  no code-level detail), the run's 50/50 strategy breakdown, the dedup
  check against 13 previously-open issues, the lifetime run totals (74 runs
  project-wide), or the "reverse-phantom-reconcile" naming convention —
  all of which exist in the linked issues/discussion/workflow source but
  are absent from the blog post's own text and were recovered by this note
  via direct fetches.

## Extracted Claims

### Claim 1: Sergo runs nightly against the gh-aw repository, using the Serena MCP language service for structural Go analysis, and follows a disciplined per-run loop — scan tools, load a bounded memory window, split effort 50/50 between reuse and exploration, generate up to three evidence-backed issues, then publish a discussion report

- **Evidence**: Blog post's "Agent of the Day: Sergo" section describes the
  loop narratively; the live workflow source (`.github/workflows/sergo.md`,
  "Execution Plan" section, steps 1–9) specifies the identical loop as
  explicit numbered instructions, confirming the blog's summary is not an
  editorial simplification.
- **Confidence**: settled (blog narrative directly corroborated by the live,
  first-party workflow definition fetched separately)
- **Quote**: "Sergo runs on a nightly schedule against the gh-aw repository,
  wired up to the Serena MCP language service for structural Go analysis
  rather than plain text search. Per its own execution plan, every run
  follows a disciplined loop: scan available Serena tools, load a bounded
  window of prior strategies from repo memory, split its effort 50/50
  between reusing a proven approach and exploring something new, then
  generate up to three non-duplicate, evidence-backed issues before
  publishing a full report as a GitHub Discussion." (blog post) / "3)
  Select strategy using a strict 50/50 split. - 50% cached reuse: prefer
  proven strategies with high success and stale recency. - 50% new
  exploration: use underused Serena tools, novel combinations, or new
  target areas." (`sergo.md`, Execution Plan step 3)
- **Our assessment**: This is the deployed-configuration confirmation that
  `blog-ghaw-custom-linters-three-workflow-loop.md` Claim 3 lacked — that
  note described Sergo's adversarial role from outcomes (issue-to-PR
  resolution chains) without ever seeing its workflow specification. This
  note supplies the missing execution-plan detail and confirms the
  50/50 reuse/explore split is a literal mission instruction, not an
  editorial description of emergent behavior.

### Claim 2: `uncheckedsliceindex` — a Go linter merged the day before this run via PR #62408 — has a systemic bug: its core safety-recognition function (`sameExpr`) only recognizes a slice/string base when it reduces to a bare `*ast.Ident`, so any struct-field-access base (`obj.Field[i]`) defeats every downstream bounds-check recognizer at once and gets falsely flagged as unchecked

- **Evidence**: Issue #62540 body, "Problem" and "Locations" sections, which
  name the exact function and line ranges
  (`pkg/linters/unchecked-slice-index/uncheckedsliceindex.go:366-371` for
  `sameExpr`; `:374-385` for `isLenOf`; `:171-195` for `isInRangeLoop`;
  `:213-241` for `isInBoundedForLoop`) and state the mechanism explicitly.
- **Confidence**: settled (directly read from the first-party issue body,
  which cites exact file:line locations for every affected function)
- **Quote**: "Its entire safety-recognition machinery (sameExpr, isLenOf,
  isInRangeLoop, isInBoundedForLoop, writesObjects, indexNonnegative)
  requires the slice/string base and the index to reduce to a bare
  *ast.Ident via astutil.UnwrapParenExpr(x).(*ast.Ident). Any base that is
  a selector expression (obj.Field, ptr.Field, nested.field.chain) fails
  every one of these checks at once, so a properly bounds-checked index
  into a struct-field slice or string is reported as unchecked" (issue
  #62540 body, "Problem")
- **Our assessment**: This is a code-level root-cause citation (naming the
  exact gating function and its dependents), the same evidentiary standard
  documented as a general Sergo/audit-agent trait in
  `blog-ghaw-agent-of-the-day-2026-09-15.md` Claim 4 for a different
  workflow (ESLint Refiner) and a different language (TypeScript) — this is
  a second, independent instance of the same discipline in the Go/Sergo
  lineage, closing the gap `blog-ghaw-custom-linters-three-workflow-loop.md`
  left open (that note described Sergo's outcomes only, not a fully
  root-caused example).

### Claim 3: Sergo backed the finding with two real production call sites already in the codebase that would trip the exact blind spot, and separately confirmed the linter's own test fixtures never exercise a struct-field base, so the gap currently has zero test coverage

- **Evidence**: Issue #62540 body, "Evidence: 2 live production
  false-positive sites" and "Impact" sections.
- **Confidence**: settled (directly read from the first-party issue body,
  which quotes the exact guarded code at each site and separately checked
  the testdata file)
- **Quote**: "pkg/workflow/skills_ref_resolution.go:30-31: `if i <
  len(data.SkillReferences) { data.Skills[i] = data.SkillReferences[i].Skill
  }` -- data.SkillReferences[i] is directly guarded ... but
  data.SkillReferences is a SelectorExpr so isLenOf never matches ... The
  linters own testdata
  (pkg/linters/unchecked-slice-index/testdata/src/uncheckedsliceindex/uncheckedsliceindex.go)
  only ever indexes bare local variables such as arr and s, never a
  selector base, so this gap has zero test coverage." (issue #62540 body)
- **Our assessment**: Pairing a live production reproduction with an
  explicit check of the test suite's blind spot is a specific methodology
  step beyond simply finding the bug: it establishes *why* the bug shipped
  undetected (the tests structurally couldn't have caught it) rather than
  treating the absence of a caught regression as reassuring. For Ch03: a
  useful checklist item for audit-agent findings — "does the existing test
  suite structurally exercise this code path at all?" — distinct from
  "does a test currently fail?"

### Claim 4: The linter Sergo audited was itself created one day earlier by a different, separately-engined agentic workflow — "Linter Miner" (`engine: copilot`, model `mai-code-1-flash-picker`) — not by a human or by Sergo, giving a same-week, end-to-end invent-then-audit handoff between two autonomous workflows in the same repository

- **Evidence**: PR #62408 body and footer, fetched directly via `gh pr
  view`: authored and merged via the Linter Miner workflow (footer:
  "Generated by Linter Miner ... copilot · mai10"), opened around
  2026-09-21, immediately followed by Sergo's next scheduled run
  (2026-09-22, run 35684470805) auditing that exact linter as its
  "new exploration" 50% for the night.
- **Confidence**: settled (both PR #62408 and issue #62540 fetched directly
  as first-party GitHub artifacts; the day-after timing is derived from
  PR #62408's creation context and issue #62540's stated "merged just the
  day before" claim, corroborated by the PR's own generated-by footer
  naming a distinct workflow and engine)
- **Quote**: "This PR adds a new Go static-analysis linter:
  **unchecked-slice-index**." / "**Location**: `pkg/linters/unchecked-slice-index/`
  ... **Test coverage**: 18 test cases (5 bad patterns, 13 good patterns)"
  (PR #62408 body) / "Generated by [Linter Miner](https://github.com/github/gh-aw/actions/runs/35631985599)
  · copilot · mai10 · 105.5 AIC" (PR #62408 footer)
- **Our assessment**: This is the first corpus instance where the
  invent → challenge handoff documented abstractly in
  `blog-ghaw-custom-linters-three-workflow-loop.md` (Linter Miner invents,
  Sergo challenges) is traced end-to-end for one specific linter with dated
  artifacts on both sides: PR #62408 (invention, `engine: copilot`) and
  issue #62540 (challenge, `engine: claude`, per `sergo.md` frontmatter) —
  and the interval between them is one day, not the "multi-month PR range"
  framing that note's aggregate evidence implied. Also notable: PR #62408's
  own "Verification" section claims "✅ All linter tests pass" and "18 test
  cases (5 bad patterns, 13 good patterns)" — Sergo's finding shows that
  passing test coverage did not catch a foundational gap in what the test
  cases actually varied (Claim 3), a concrete illustration that "tests
  pass" and "tests exercise the failure mode" are different claims.

### Claim 5: Sergo re-verified a previously auto-expired issue (#60738, filed at an earlier run) and confirmed the underlying `bufioscannererunchecked` bug is still 100% present in source, then re-filed it with fresh evidence as issue #62541 rather than letting the finding stay lost — the 7th time this project has recorded this exact failure shape, which Sergo's own reports name "reverse-phantom-reconcile"

- **Evidence**: Issue #62541 body, "Problem" and "Impact" sections; blog
  post narrative; discussion #62542 body, "Historical context" section,
  which lists five prior named instances plus this one as the 7th.
- **Confidence**: settled (directly read from the first-party issue body
  and discussion report; the specific code-level re-verification —
  `analyzeBlockStatements` at `bufioscannererunchecked.go:72-98`, with a
  worked repro showing the check placed one block level up — is not
  present in the blog post's own text)
- **Quote**: "Issue 60738 (sg66a1, filed R66 for the block_scope_state_reset
  class in bufioscannererunchecked) was auto-closed not_planned on
  2026-09-21T04:49 by the issue-expiry workflow, with zero code changes.
  Re-reading the source confirms the underlying bug is still 100 percent
  present." / "This is the 7th confirmed reverse-phantom-reconcile instance
  in this project (an issue auto-expires and closes as not_planned while
  the underlying code defect is never touched), following the same pattern
  already seen for the nolint space-prefix gap (3 refilings), the 4-linter
  main-guard gap, the manualmutexunlock 2+-level selector collapse, the
  slicemakezerolength var-vs-make gap, and the bufferresetbeforereuse
  per-block-state gap" (issue #62541 body)
- **Our assessment**: This directly documents a repeated, named cost of
  the `expires:`-based safe-output auto-closure mechanism that
  `docs-ghaw-ephemerals.md` Claim 3 frames only as protective ("auto-expiry
  is a safety mechanism — stale agent-generated content that persists
  indefinitely can mislead future readers"). Here, seven times over, the
  mechanism has instead silently converted "unresolved bug, tracked" into
  "no record of an unresolved bug" with zero human decision involved — a
  materially different risk than content merely going stale. **Filed as
  contradiction issue #3639** rather than resolved here (see
  Cross-References → Contradicts).

### Claim 6: The blog's "three consecutive nights" framing describes only a recent window; the linked discussion report reveals Sergo is actually on its 74th run project-wide, with lifetime totals of 473 findings and 129 generated tasks and an average self-reported success score of 8.8/10

- **Evidence**: Discussion #62542 body, "Metrics" section.
- **Confidence**: settled (directly read from the first-party discussion
  report; not mentioned anywhere in the blog post, which frames the pattern
  only across "the last three nights")
- **Quote**: "Run R74. ... Totals to date: 74 runs, 473 findings, 129
  tasks, average success score 8.8." (discussion #62542 body, "Metrics")
- **Our assessment**: The blog post's "zoom out across the last three
  nights" framing is accurate as far as it goes but understates the
  workflow's actual maturity — this is not a young or experimental
  deployment but a 74-run production history with a stable, self-tracked
  quality metric. For Ch04 (Operations): a self-reported cumulative success
  score published in every run's own discussion report is a lightweight,
  low-effort way to make a long-running audit workflow's track record
  auditable by a human skimming the latest report, without requiring a
  separate dashboard.

### Claim 7: Before filing, Sergo reconciled all 13 previously-open `sergo`-labeled issues via a live `gh api` search, and both new issues this run were confirmed deduplicated against that list — the same "dedup check before filing" discipline previously documented only for the ESLint Refiner workflow

- **Evidence**: Discussion #62542 body, "Strategy: 50/50 split" and
  "Metrics" sections ("Issues created: 2, both deduplicated with zero prior
  coverage confirmed").
- **Confidence**: settled (directly read from the first-party discussion
  report; not mentioned in the blog post)
- **Quote**: "Cached (50%): Reconciled all 13 previously-open sergo issues
  via gh api. One (#60738) had auto-expired without any code fix;
  re-verified the underlying block_scope_state_reset bug in
  bufioscannererunchecked.go is unchanged and refiled it." (discussion
  #62542 body)
- **Our assessment**: This is a second, independent corpus instance of the
  live-dedup-before-filing pattern documented in
  `blog-ghaw-agent-of-the-day-2026-09-15.md` Claim 7 for ESLint Refiner —
  now confirmed in a structurally different workflow (Go/Serena vs.
  JS/TS-ESLint) and a different underlying engine relationship, which
  strengthens it as a generalizable audit-agent practice rather than a
  one-workflow habit. Notably, this run's dedup check is also what
  *produces* Claim 5's finding: reconciling the 13 open issues is precisely
  what surfaced that #60738 had silently disappeared from the open list.

### Claim 8: Sergo's memory tracks a named taxonomy of recurring bug-pattern *classes* across runs, not just individual findings — this run explicitly distinguishes the new "ident_only_equality_gap" class (Claim 2's bug) from a previously-catalogued "paren_unwrap_gap" class as a structurally different root cause

- **Evidence**: Discussion #62542 body, "Historical context" section.
- **Confidence**: settled (directly read from the first-party discussion
  report; not mentioned in the blog post, which describes only the
  individual finding, not the taxonomy Sergo maintains around it)
- **Quote**: "The new ident_only_equality_gap pattern class is distinct
  from the previously catalogued paren_unwrap_gap: that class is about
  missing ParenExpr unwrapping before an otherwise-adequate type assertion,
  while this one is about an equality helper refusing to handle anything
  but a bare identifier, even after full unwrapping." (discussion #62542
  body, "Historical context")
- **Our assessment**: This is a more sophisticated memory structure than
  "list of past findings" — Sergo's repo-memory apparently encodes an
  ontology of *why* linters fail (by root-cause shape), which lets a new
  finding be classified against prior root causes rather than only against
  prior specific bugs. For Ch06 (Memory & Context Management): naming and
  persisting root-cause *classes*, not just resolved/open finding IDs, is a
  concrete technique for helping a long-running audit agent generalize
  ("is this the same shape of bug as something I've seen before, even in a
  different function?") rather than only deduplicating on identical bugs.

### Claim 9: Sergo's workflow definition restricts it to read-only Go/repo inspection (`edit: null`, a fixed five-command `bash:` allowlist, GitHub access via `gh-proxy` scoped to `default`/`issues` toolsets) and explicitly excludes `api.anthropic.com` from `network.allowed`, which caused a firewall block on both filed issues from this run

- **Evidence**: Live workflow source (`.github/workflows/sergo.md`)
  frontmatter, `tools:` and `network:` blocks; both issue #62540 and
  issue #62541 carry an identical auto-appended firewall-warning box naming
  the same blocked domain.
- **Confidence**: settled (directly read from the live, first-party
  workflow file and corroborated by matching auto-generated warnings on
  both issues from the same run)
- **Quote**: "network: allowed: - defaults - github - go" / "tools: bash: -
  cat go.mod - cat go.sum - go list -m all - find . -name \"*.go\" -type f
  - grep -r \"func \" --include=\"*.go\" - grep -c '.Analyzer,' pkg/linters/registry.go
  - wc -l ... edit: null" (`sergo.md` frontmatter) / "The following domain
  was blocked by the firewall during workflow execution: - `api.anthropic.com`"
  (issue #62540 and #62541, identical auto-appended warning box)
- **Our assessment**: This is a second concrete, dated instance in the
  corpus of a firewall block on the model provider's own API host (the
  first being `blog-ghaw-agent-of-the-day-2026-09-15.md` Claim 9, for
  ESLint Refiner) — both workflows omit `api.anthropic.com` from
  `network.allowed` and both trip the same block on the same class of
  request, which is stronger evidence that this is a structural property
  of how `engine: claude` inference is routed in gh-aw workflows (through
  the AWF gateway, not a direct call — per
  `docs-ghaw-awf-reflect-reference.md` Claim 3) rather than a
  workflow-specific misconfiguration. Two independent workflows exhibiting
  the identical "blocked, but nothing else went wrong" pattern makes it
  less likely to be a fluke in either one.

## Concrete Artifacts

### Issue #62540 — `uncheckedsliceindex` Selector-Base Bug (filed 2026-09-22, open at extraction time)

```
Title:   uncheckedsliceindex: selector-based slice/string bases defeat all
         bounds-check and safe-loop recognition
Opened:  2026-09-22T03:59:20Z
State:   OPEN (checked 2026-09-23)
Labels:  cookie, sergo

Root function: sameExpr, pkg/linters/unchecked-slice-index/uncheckedsliceindex.go:366-371
  Requires both operands to be *ast.Ident. Downstream dependents that
  inherit the gap: isLenOf (:374-385), isInRangeLoop (:171-195),
  isInBoundedForLoop (:213-241).

Live false-positive sites:
  pkg/workflow/skills_ref_resolution.go:30-31
    if i < len(data.SkillReferences) { data.Skills[i] = data.SkillReferences[i].Skill }
  pkg/workflow/cache_memory.go:355-356
    for i := 1; i < len(config.Caches); i++ { if len(config.Caches[i].AllowedExtensions) != ... }

Test coverage gap: linter's own testdata
  (testdata/src/uncheckedsliceindex/uncheckedsliceindex.go) only indexes
  bare local variables (arr, s) — never a selector base.

Recommendation: generalize sameExpr to unwrap one level of SelectorExpr
  and compare Sel.Name + resolved base types.Object, instead of requiring
  a bare *ast.Ident.

Validation checklist:
  - Add testdata: struct-field slice guarded by if / bounded for / range
  - Re-run against the two named production sites, confirm FP disappears
  - Confirm no regression on badRangeDifferentSlice/badRangeOffset

Effort: Medium.

Footer: "claude · agent · 232.6 AIC · ⌖ 8.31 AIC · ⊞ 7K"; expires
  2026-09-29T03:59:20.338Z (7d from creation).
Auto-appended firewall warning: blocked domain api.anthropic.com.
```
*Source: github/gh-aw issue #62540, fetched via `gh issue view`, 2026-09-23.*

### Issue #62541 — `bufioscannererunchecked` Reverse-Phantom Refiling (filed 2026-09-22, open at extraction time)

```
Title:   bufioscannererunchecked: block-scope Err() check gap still
         unfixed (issue 60738 auto-expired, 7th reverse-phantom)
Opened:  2026-09-22T03:59:21Z
State:   OPEN (checked 2026-09-23)
Labels:  cookie, sergo

Prior issue: #60738 (filed run R66), auto-closed not_planned
  2026-09-21T04:49 by the issue-expiry workflow, zero code change.

Root cause (re-verified unchanged): hasScannerErrCheck,
  pkg/linters/bufioscannererunchecked/bufioscannererunchecked.go:72-98 —
  only searches for a trailing scanner.Err() call within the SAME
  []ast.Stmt slice as the scan loop; an Err() check in an enclosing block
  (after an if/for/switch wrapping the loop) is invisible to the search.

Repro (from issue body):
  func readLines(r io.Reader) {
      scanner := bufio.NewScanner(r)
      if true {
          for scanner.Scan() { _ = scanner.Text() }
      }
      if err := scanner.Err(); err != nil { log.Println(err) }
  }

Impact: not yet CI-enforced (diagnostic-only); ~20 real
  scanner.Scan()/Err() sites in pkg/ all place loop+check as top-level
  siblings today, so no live production FP currently — the bug has simply
  never been fixed since first filed.

Historical pattern named "reverse-phantom-reconcile" — 7th instance in
  this project: nolint space-prefix gap (3 refilings), 4-linter main-guard
  gap, manualmutexunlock selector collapse, slicemakezerolength
  var-vs-make gap, bufferresetbeforereuse per-block-state gap (direct
  sibling, same pattern class), and now this one.

Effort: Small (same fix shape as the still-open bufferresetbeforereuse
  companion issue).

Footer: identical firewall-block warning (api.anthropic.com) and expiry
  format to issue #62540.
```
*Source: github/gh-aw issue #62541, fetched via `gh issue view`, 2026-09-23.*

### Discussion #62542 — Sergo Report, Run R74, 2026-09-22

```
Title: [sergo] Sergo Report: DELTA-72to73-newlinter-audit(uncheckedsliceindex)
       +reverse-phantom-refile(bufioscannererunchecked) - 2026-09-22
Category: Audits
State: closed (state_reason: outdated, auto-expired), 1 comment

Executive summary: Run R74. Linter registry grew 72->73 (new:
  uncheckedsliceindex, PR #62408). First-ever audit found the
  Ident-only-equality bug (2 live FP sites). Separately, 7th
  reverse-phantom instance caught and refiled. 2 new issues, both
  deduplicated via gh api before filing.

Tool updates: Serena — 24 tools, stable, activate_project OK for
  go/typescript/bash, no approval prompts. Linter registry: 72 -> 73
  analyzers (grep -c '.Analyzer,' pkg/linters/registry.go).

Strategy (50/50 split):
  Cached (50%): reconciled all 13 previously-open sergo issues via gh api;
    #60738 found auto-expired with zero fix, re-verified and refiled.
  New exploration (50%): first-ever full audit of the 73rd (newest)
    linter, uncheckedsliceindex.

Findings this run: 5 total (2 filed as issues; 3 recorded in memory as
  audited-clean or structurally-immune paths, not filed).

Generated tasks (2):
  1. Generalize sameExpr to handle SelectorExpr bases. Medium effort.
  2. Thread enclosing-block statements into hasScannerErrCheck. Small
     effort — same shape as the open bufferresetbeforereuse companion.

Metrics: Findings 5 (2 filed, 3 clean/immune). Issues created: 2, both
  deduplicated, zero prior coverage. Success score: 9/10. Totals to date:
  74 runs, 473 findings, 129 tasks, average success score 8.8.

Historical context: 6 prior reverse-phantom instances named explicitly
  (nolint space-prefix x3, 4-linter main-guard gap, manualmutexunlock
  selector-collapse, slicemakezerolength var-vs-make, bufferresetbeforereuse
  per-block-state). New pattern class this run: ident_only_equality_gap,
  explicitly distinguished from the previously-catalogued paren_unwrap_gap
  class.

Next-run focus: verify both new issues land as filed; re-tally all 14 open
  sergo issues at start of next run; if the registry grows again, audit
  the newest linter first; otherwise extend the uncheckedsliceindex audit
  to hasTerminatingGuardBefore/invalidBounds for the same Ident-only
  limitation.

References: run 35684470805,
  https://github.com/github/gh-aw/actions/runs/35684470805

Footer: identical firewall-block warning (api.anthropic.com); expires 1d
  from creation (matching shared/daily-audit-base.md with: {expires: 1d}).
```
*Source: github/gh-aw discussion #62542, fetched via `gh api
repos/github/gh-aw/discussions/62542`, 2026-09-23.*

### Sergo: Workflow Frontmatter and Execution Plan (fetched 2026-09-23)

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
  - go
imports:
- uses: shared/daily-audit-base.md
  with:
    expires: 1d
    title-prefix: "[sergo] "
- shared/mcp/serena-go.md
- shared/otlp.md
- shared/reporting.md
safe-outputs:
  create-issue:
    expires: 7d
    labels:
    - sergo
    - cookie
    max: 3
description: Daily Go code quality analysis using Serena MCP language
  service protocol expert
emoji: 🤖
engine: claude
name: "Sergo - Serena Go Expert"
strict: true
timeout-minutes: 45
tools:
  bash:
  - cat go.mod
  - cat go.sum
  - go list -m all
  - find . -name "*.go" -type f
  - grep -r "func " --include="*.go"
  - grep -c '.Analyzer,' pkg/linters/registry.go
  - wc -l
  cli-proxy: true
  edit: null
  github:
    mode: gh-proxy
    toolsets:
    - default
    - issues
  repo-memory:
    branch-name: memory/sergo
    description: Historical Sergo Go analysis results, strategies, and tool
      snapshots
    file-glob:
    - "*.json"
    - "*.jsonl"
tracker-id: sergo-daily
```

Execution Plan (9 steps, abbreviated to novel content not already in
Concrete Artifacts above): step 1 initializes the Serena tool cache and
treats a missing cache as expected first-run behavior; step 2 reads only
the 3 most recent strategy entries from `sergo-strategies.jsonl` (a bounded
memory window, matching the blog's "bounded window of prior strategies"
language); step 8 computes a 0–10 success score and appends it to that same
JSONL file after every run — the mechanism behind Claim 6's cumulative 8.8
average.

*Source: `.github/workflows/sergo.md`, fetched via `curl` from
`raw.githubusercontent.com/github/gh-aw/main/`, 2026-09-23.*

### PR #62408 — `uncheckedsliceindex` Linter Introduced (merged, authored by a different workflow)

```
Title: adds unchecked-slice-index linter
Author workflow: Linter Miner (engine: copilot, model mai-code-1-flash-picker)
Related run: #140 — Linter Miner daily task

What it does: reports direct slice/string indexing without a bounds check
  that can panic at runtime. Recognizes as safe: len()-based guards,
  range-loop variables, constant indices on statically-sized arrays.
  Supports // nolint:uncheckedsliceindex suppression.

Evidence & origin (per PR body): derived from code-pattern mining of
  pkg/cli/ and cmd/; differentiated from slicemakezerolength/deferinloop;
  cites MISRA C / CWE-129 bounds-checking philosophy.

Verification claimed in PR body: "All linter tests pass"; "go build
  ./cmd/linters succeeds"; 18 test cases (5 bad patterns, 13 good
  patterns).

Footer: "copilot · mai10 · 105.5 AIC · ⊞ 6.6K"; expires
  2026-09-28T17:41:40.994Z (7d, pull-request type).
Auto-appended firewall warning on THIS PR: blocked domain
  api.github.com (different domain than Sergo's block — Linter Miner's
  network.allowed evidently omits api.github.com specifically, with an
  auto-generated tip recommending tools.github.mode: gh-proxy instead of
  allowlisting it).
```
*Source: github/gh-aw PR #62408, fetched via `gh pr view`, 2026-09-23.*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-custom-linters-three-workflow-loop.md` Claims 1, 3, 6 (the
    invent/Linter-Miner → challenge/Sergo two-role split; Sergo as
    "adversarial testing layer... targeting precision gaps"): Claim 4 here
    traces that abstract split to one concrete, dated pair of artifacts
    (PR #62408 → issue #62540) with a one-day invent-to-audit interval, and
    Claim 1 supplies the execution-plan detail that note lacked.
  - `docs-ghaw-agent-factory-status.md` Claim 7 (Sergo listed as one of six
    Claude-only Go-specialization workflows): this note confirms
    `engine: claude` directly from the live workflow frontmatter, and PR
    #62408's `engine: copilot` footer confirms Linter Miner sits outside
    that Claude-only Go cluster — the two sibling workflows in the same
    lifecycle use different engines.
  - `blog-ghaw-agent-of-the-day-2026-09-15.md` Claim 7 (live dedup check
    against open issues performed before filing, documented for ESLint
    Refiner): Claim 7 here is a second, independent instance in a
    different workflow and language ecosystem.
  - `blog-ghaw-agent-of-the-day-2026-09-15.md` Claim 9 and
    `docs-ghaw-awf-reflect-reference.md` Claim 3 (firewall blocks on
    `api.anthropic.com` specifically, consistent with inference routed
    through the AWF gateway rather than a direct upstream call): Claim 9
    here is a second, independent workflow tripping the identical block.

- **Contradicts**: `docs-ghaw-ephemerals.md` Claim 3 ("auto-expiry is a
  safety mechanism" for safe-output issues, with no downside documented for
  finding-type issues specifically) vs. Claim 5 here (7 confirmed instances
  of the same auto-expiry mechanism silently erasing an unresolved code
  defect's tracking record, project-wide, in this one repo). **Filed as
  contradiction issue #3639** — see that issue and, once resolved,
  `CONTRADICTIONS.md` for the verdict. Not resolved in this note per
  MINER.md §4a.

- **Extends**:
  - `docs-ghaw-guides-serena.md` Claim 2 (Serena exposes "11 specific
    tools," documented 2026-05-11): discussion #62542 self-reports "Serena:
    24 tools, stable" as of 2026-09-22, roughly 4.5 months later. Not
    treated as a contradiction — a growing MCP tool surface over time is
    the expected trajectory for an actively developed language server
    integration, and no guide recommendation turns on the exact count — but
    flagged here as a numeric staleness note: any future citation of "11
    tools" for Serena should be re-verified against the current tool list
    rather than treated as still-current.
  - `blog-ghaw-agent-of-the-day-2026-09-15.md` Claims 6–7 (multi-category
    finding taxonomy; live dedup): Claim 8 here extends the taxonomy idea
    one level further — not just categorizing a single run's findings, but
    persisting named root-cause *classes* across the workflow's entire run
    history so a new finding can be classified against prior root causes.

- **Novel**:
  - **A same-week, end-to-end invent → audit handoff between two
    separately-engined agentic workflows, traced through dated first-party
    artifacts on both sides** (Claim 4): the three-workflow-loop note
    established the pattern abstractly with month-scale PR ranges; this is
    the first single-linter case study with a one-day interval.
  - **A named, self-tracked taxonomy of recurring auto-expiry failures
    ("reverse-phantom-reconcile") with a running count (7 instances) and
    five prior instances named by pattern** (Claim 5): not documented
    anywhere else in the corpus as a systemic mechanism-level risk of
    `expires:`-based safe-output closure, as opposed to an isolated
    incident.
  - **A named taxonomy of bug root-cause *classes* (not just individual
    findings) persisted in repo-memory across runs** (Claim 8): a finer
    memory structure than the finding-level dedup lists documented
    elsewhere.
  - **Lifetime run statistics (74 runs, 473 findings, 129 tasks, 8.8 avg
    success score) self-published inside a routine daily report** (Claim
    6): the corpus has prior examples of per-run findings and per-run
    success framing, but not a workflow casually exposing its own
    multi-month cumulative track record as a standing section of every
    report.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the traced invent → audit
  handoff (Claim 4) as a concrete, dated case study for the "separate
  invention and validation into independent agentic roles" pattern already
  recommended from `blog-ghaw-custom-linters-three-workflow-loop.md`. Add
  the live-dedup-before-filing practice (Claim 7) as now corroborated
  across two independent workflows and language ecosystems, strengthening
  it from "one workflow's habit" to "a generalizable practice worth
  recommending directly."

- **Chapter 03 (Safety & Verification)**: Cite Claim 5 as evidence that
  `expires:`-based auto-closure of *finding-type* issues (as opposed to
  periodic report/announcement issues) needs an explicit caveat or a
  verification gate before the guide recommends short expiry windows
  uncritically — reference contradiction issue #3639 and its eventual
  CONTRADICTIONS.md resolution before finalizing this recommendation. Add
  Claim 3's "does the test suite structurally exercise this path at all"
  check as a concrete audit-agent methodology item, distinct from "does a
  test currently fail."

- **Chapter 06 (Memory & Context Management)**: Add the root-cause-class
  taxonomy (Claim 8) as a technique for long-running audit agents: persist
  named categories of *why* a class of tool fails, not only a list of
  resolved/open finding IDs, so new findings can be matched against prior
  root causes even when the specific bug or file differs.

## Extraction Notes

1. **Blog post is short (~500 words); primary depth came from five fetched
   sub-pages**, within MINER.md §1's "up to 5" budget: issue #62540 (`gh
   issue view`), issue #62541 (`gh issue view`), discussion #62542 (`gh api
   repos/github/gh-aw/discussions/62542`), the live workflow source
   (`curl` against `raw.githubusercontent.com`), and PR #62408 (`gh pr
   view`). Claims 3–9 and most of Concrete Artifacts rely on this sub-page
   material — none of it is present in the blog post's own text.

2. **Verbatim blog quotes obtained via direct HTML fetch, not WebFetch
   summarization**: per MINER.md §2a, the page was fetched via `curl` and
   parsed with a Python regex pass stripping script/style/nav boilerplate
   and converting the article body to plain text, then cross-checked
   against the raw HTML's anchor tags to recover the five inline links
   (workflow source, most recent run, PR #62408, issue #62540, issue
   #62541, discussion #62542) used to locate every sub-page fetched above.
   All blog-post quotes are copied character-for-character from that pass.

3. **Contradiction filed**: issue #3639, `docs-ghaw-ephemerals.md` Claim 3
   ("auto-expiry is a safety mechanism") vs. this note's Claim 5 (7 named
   instances of the same mechanism silently masking unresolved code
   defects). See Cross-References → Contradicts. Recommended verdict in the
   filed issue is `debated` (the mechanism likely needs a conditioning
   variable — finding-type issues vs. report-type issues — rather than one
   side being simply wrong), but the actual verdict is left to the human
   resolver per MINER.md §4a. Note for that resolver: #3639 already
   received a contradiction assessment returning `unresolved` on the
   grounds that Side B "does not yet exist in the corpus" — that
   assessment was run before this note was written, so it should be
   re-run once this note merges and Side B's citation target exists.

4. **Cross-reference check performed** against
   `blog-ghaw-custom-linters-three-workflow-loop.md`,
   `blog-ghaw-agent-of-the-day-2026-09-15.md`,
   `blog-ghaw-agent-of-the-day-2026-08-28.md`,
   `docs-ghaw-agent-factory-status.md`, `docs-ghaw-guides-serena.md`,
   `docs-ghaw-ephemerals.md`, `docs-ghaw-awf-reflect-reference.md`, and
   `CONTRADICTIONS.md` (44 open contradiction issues reviewed by title;
   none pre-existing on the auto-expiry/defect-masking topic before this
   note's filing), plus a corpus-wide grep for "sergo" and "phantom" to
   confirm no prior note already profiled Sergo directly. That grep hits
   eight other notes, none of them an independent Sergo profile:
   `blog-ghaw-custom-linters-three-workflow-loop.md` is the only
   substantive treatment, and it covers Sergo as one of three workflows
   in the invent/challenge/apply loop rather than as a dedicated profile;
   `docs-ghaw-agent-factory-status.md` lists Sergo in a catalog table
   (name, schedule, engine) only; `blog-ghaw-agent-of-the-day-2026-09-02.md`'s
   hits are all the branch name `copilot/sergo-fix-linters-silent-delete`,
   not Sergo the workflow; and the remaining five
   (`blog-ghaw-weekly-2026-07-06.md`, `blog-ghaw-weekly-2026-07-20.md`,
   `blog-ghaw-weekly-2026-08-17.md`, `blog-ghaw-agent-of-the-day-2026-08-28.md`,
   `blog-ghuntley-engineer-away-slop.md`) are comparison or cross-reference
   mentions that each cite
   `blog-ghaw-custom-linters-three-workflow-loop.md` by name.
   All `Claim N` citations above were checked against the
   actual numbered claims in those notes at the time of writing, per
   MINER.md §4b.

5. **Five of the seven named reverse-phantom instances not independently
   re-verified**: discussion #62542's "Historical context" section names
   five prior instances (nolint space-prefix, 4-linter main-guard gap,
   manualmutexunlock selector-collapse, slicemakezerolength var-vs-make,
   bufferresetbeforereuse per-block-state) by pattern name only, without
   issue numbers in the fetched text. This note did not independently
   fetch those five to confirm the specifics — only the 7th instance
   (#60738 → #62541) was independently verified end-to-end via direct
   issue fetch. The "7 instances" count itself is taken as Sergo's own
   self-report, not independently re-derived by this note.

6. **PR #62408's firewall block (api.github.com) is a different domain
   than Sergo's (api.anthropic.com)** and is included in Concrete Artifacts
   for completeness, but is not treated as corroborating Claim 9 — it
   reflects a different, GitHub-API-specific network gap with its own
   documented remedy (`tools.github.mode: gh-proxy`), not the
   inference-gateway-routing pattern Claim 9 is about.
