---
source_url: https://github.github.com/gh-aw/blog/2026-09-10-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – September 10, 2026: Package Specification Librarian"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-09-10
date_extracted: 2026-09-11
last_checked: 2026-09-11
status: current
confidence_overall: emerging
issue: "#3379"
---

# Agent of the Day – September 10, 2026: Package Specification Librarian

> A profile of Package Specification Librarian, a daily doc-vs-code drift
> auditor for `gh-aw`'s own Go packages, whose "five consecutive successful
> runs, zero errors... steadily shrinking backlog" framing does not survive
> a check against the GitHub Actions API and the workflow's own three most
> recent audit-report issues: the workflow has run daily since 2026-04-13
> (153 runs, 13 failures scattered across that history — not zero), and the
> cited backlog went 6 → 3 → 5 real issues across its last three audits, an
> increase on the final data point, not a continued shrink. The live
> workflow source also reveals the "opens a pull request"-adjacent framing
> is accurate here (it only ever opens or updates a single tracked issue,
> never a PR) and exposes a self-referential documentation-drift bug in the
> auditor's own prompt template.

## Source Context

- **Type**: blog-post (an "Agent of the Day" entry from the official GitHub
  Agentic Workflows blog, bylined "Copilot" — the same recurring gh-aw
  AI-authored-post convention documented throughout this series, e.g.
  `blog-ghaw-agent-of-the-day-2026-09-08.md`, `blog-ghaw-agent-of-the-day-2026-09-07.md`).
  This is the first corpus entry to profile Package Specification Librarian
  by name, though the workflow itself is not new (see Claim 7).
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team, profiling a workflow that runs
  in the team's own `github/gh-aw` repository. This note independently
  fetched the live workflow source
  (`.github/workflows/spec-librarian.md`, via `curl` against
  `raw.githubusercontent.com`), the workflow's full Actions run history (all
  153 runs via `gh api repos/github/gh-aw/actions/workflows/260340165/runs`),
  job-level step data for one failed run, and the full bodies of the three
  most recent audit-report issues (#57954, #58993, #59985) plus the earlier
  named issue #34216 — none of this was taken from the blog post's own text.
  Most of it qualifies or corrects the blog's framing; see Claims 3, 4, and
  6 below.
- **Scope**: Covers the featured agent's stated mission (comparing
  `pkg/*/README.md` against exported Go symbols), the latest audit's
  headline numbers (37 packages, 36 specced, 97% coverage, 5 issues), the
  four-dimension quality-scoring rubric, and a "five consecutive successful
  runs... shrinking backlog" reliability/trend framing. Does NOT cover: the
  workflow's actual `safe-outputs` configuration, its full run history, the
  four-dimension weighting scheme's numeric weights, or the fact that this
  is one of a family of three related doc-spec workflows (`spec-extractor`,
  `spec-enforcer`, `spec-librarian`) — all of which this note recovered only
  by fetching the live workflow source and the GitHub API directly.

## Extracted Claims

### Claim 1: Package Specification Librarian runs daily against `gh-aw` itself, comparing every `pkg/*/README.md` against the real exported Go symbols in the corresponding source, not checking for typos or style
- **Evidence**: Direct first-party description in the post's second
  paragraph, corroborated by the live workflow source's frontmatter
  `description:` field and its "Mission" section.
- **Confidence**: settled (identical framing given independently by the blog
  post and the live workflow source)
- **Quote**: "The Package Specification Librarian runs every day against
  gh-aw itself, reading every README.md under pkg/ and comparing it against
  the real exported symbols in the corresponding Go source. It's not looking
  for typos or style nits — it's checking whether the documentation still
  tells the truth about the code."
- **Our assessment**: This is directly corroborated by the live workflow
  source's own description (`"Daily review of all package README.md
  specifications to detect inconsistencies, staleness, and cross-package
  conflicts"`) and its `tools.bash` allowlist, which is built almost
  entirely around symbol-extraction greps (`grep -rn "func [A-Z]" pkg`,
  `grep -rn "type [A-Z]" pkg`, `grep -rn "const [A-Z]" pkg`) rather than any
  prose-linting tool. For Ch02 (Harness Engineering): this is a clean example
  of a narrowly-scoped audit agent whose entire tool surface is shaped to
  its one job — no general-purpose file editor is even granted (the workflow
  sets `edit: null`), since the mission is detection and reporting, not
  fixing.

### Claim 2: The latest audit (issue #59985) reports 37 total packages, 36 with specifications (97% coverage), and 5 issues found, with the one true coverage gap (`pkg/workflowcontract`) being a package that exists solely to hold a contract-test guard and never got a README
- **Evidence**: Blog prose plus this note's direct fetch of issue #59985's
  full body, which states the identical numbers and identifies
  `pkg/workflowcontract` as the sole missing-spec package, containing "0
  non-test `.go` files (1 test file:
  `daily_performance_summary_workflow_contract_test.go`)" and existing
  "solely to assert stable contract tokens for the `daily-performance-summary`
  workflow prompt."
- **Confidence**: settled (identical figures independently confirmed by the
  blog post and the source issue's own body)
- **Quote**: "Out of 37 packages, 36 have specs — a 97% coverage rate — and
  the one true gap, pkg/workflowcontract, isn't even a missing-doc problem
  so much as a package that exists purely to hold a contract-test guard and
  never got a README explaining why."
- **Our assessment**: `pkg/workflowcontract` is not a one-off: this note's
  fetch of the two prior audit issues (#57954, Sep 2; #58993, Sep 6) shows
  the identical package flagged as the sole `❌` missing-spec entry in both,
  with recommendation text essentially unchanged run to run ("a short
  README.md explaining the package's purpose... would help future
  maintainers"). This is a persistent, low-priority, repeatedly-reported gap
  that has not been fixed across at least three audit cycles spanning more
  than a week — a concrete illustration that "found and reported" does not
  imply "fixed," even for a trivially small remediation (a single README
  file with no code API to document). For Ch04 (Operations): an audit agent
  that re-reports the same low-priority finding every cycle without any
  escalation or staleness signal risks normalizing repeat findings as noise;
  cross-reference the `close-older-issues: true` + `max: 1` configuration in
  Concrete Artifacts, which caps this to one open issue at a time but does
  not itself distinguish a brand-new finding from a week-old unaddressed one.

### Claim 3: The post frames the agent's reliability as "five consecutive successful runs, zero errors" — a framing that checks out for the exact five-day window it implicitly cites (Sep 6–10) but does not hold for the workflow's actual lifetime reliability
- **Evidence**: `gh api repos/github/gh-aw/actions/workflows/260340165/runs`
  (workflow ID resolved via the run URL for #34481937715, which maps to
  `.github/workflows/spec-librarian.lock.yml`) confirms runs #148–#152
  (2026-09-06 through 2026-09-10) are all `"conclusion": "success"` —
  exactly five consecutive successful runs, matching the blog's number
  precisely for that window. But the same API, queried across the workflow's
  full history back to run #1 (created 2026-04-13), shows 13 failed runs out
  of 153 total (run numbers 22, 28, 33, 56, 57, 58, 59, 73, 92, 110, 127,
  133, 138 — most recently 2026-08-27), roughly one failure in every twelve
  runs over the workflow's five-month life.
- **Confidence**: settled (both the five-run window and the full 153-run
  history with its 13 failures are read directly from the GitHub Actions
  API, not paraphrased from the blog)
- **Quote**: "Looking back at prior runs — #58993 on September 6 found 3
  issues, #57954 on September 2 found 6 — the pattern holds: five
  consecutive successful runs, zero errors, and a steadily shrinking
  backlog of undocumented symbols as the fixes land."
- **Our assessment**: The "five consecutive successful runs, zero errors"
  figure is, narrowly, exactly correct — it is not an exaggeration or an
  invented number, unlike some precision gaps documented elsewhere in this
  series. What it omits is scope: "zero errors" is true only for the
  five-day window bounding the three cited issues, not for the workflow as
  a whole, which failed on 2026-08-27 (run #138, twelve days before this
  post's window) and twelve other times going back to 2026-04-13. One
  inspected failure (run #138) failed at the infrastructure layer ("Start
  MCP Gateway" step), not from a logic error in the agent's own audit work
  — suggesting these are largely transient platform failures rather than
  auditor bugs, but the blog's phrasing does not distinguish "this window
  had zero errors" from "this agent doesn't fail." For Ch04 (Operations):
  when citing a "zero errors" or "N consecutive successes" framing for a
  long-running daily agent, check the full run history via `gh api
  .../actions/workflows/<id>/runs`, not just the window the source names —
  a narrow window can be literally true and still misrepresent the agent's
  overall reliability, echoing the same lesson already drawn in
  `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 3 for a different gh-aw
  daily agent (CLI Version Checker's understated seven-run failure streak).

### Claim 4: The post's "steadily shrinking backlog" framing, read against its own two cited data points plus the current run, does not describe a monotonic decline — the issue count went 6 (Sep 2) → 3 (Sep 6) → 5 (Sep 10)
- **Evidence**: This note's direct fetch of all three audit issues confirms
  the exact "issues found" figures in each title: `#57954` ("...6 issues
  found"), `#58993` ("...3 issues found"), `#59985` ("...5 issues found").
  6 → 3 → 5 is a decrease then an increase, not a steady decline.
- **Confidence**: settled (all three numbers are read directly from the
  cited issues' own titles, which the blog post itself names by number)
- **Quote**: "the pattern holds: five consecutive successful runs, zero
  errors, and a steadily shrinking backlog of undocumented symbols as the
  fixes land"
- **Our assessment**: This is the blog's own claim failing to survive a
  check against data the blog itself cites by issue number — not two
  independently-argued sources disagreeing, so per the precedent set in
  `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 2's "Our assessment" this
  does not meet the MINER.md §4a contradiction-filing bar. It is worth
  separating two things that are easy to conflate: total *package* coverage
  (37 packages, 36 specced, 97%) has been flat and stable across all three
  audits — that part of "the pattern holds" is accurate — while the
  *issue-count* trend the blog calls "steadily shrinking" is not a
  monotonic series in the numbers it names. One plausible explanation
  consistent with the data: `#59985`'s 5-issue count is partly an artifact
  of stricter false-positive filtering that run performed (Claim 6), not
  purely new regressions; but the blog does not make that distinction, and
  the raw number it presents as evidence of a trend does not describe one.
  For Ch04 (Operations): when a source names specific historical data points
  to support a trend claim ("the pattern holds"), check whether the named
  numbers actually form the claimed trend before repeating it — a series of
  three numbers is enough to falsify "steadily shrinking" on inspection, no
  deeper API digging required.

### Claim 5: Findings are scored across four weighted dimensions — completeness (30%), accuracy (30%), consistency (20%), freshness (20%) — with quality bands at ≥80% (Good), 50–79% (Needs Attention), and <50% (Critical)
- **Evidence**: Blog prose states the four dimension names without weights;
  the live workflow source's "Phase 4: Quality Assessment" section supplies
  the exact percentage weights and the three named quality bands, and issue
  #59985's own "📊 Quality Scores" table applies them, e.g. `cli`: 94%/95%/90%/90%
  → 93% overall, `errorutil`: 88%/95%/95%/90% → 92% overall.
- **Confidence**: settled (weights and bands read directly from the live
  workflow source's prompt; the applied scores are read directly from the
  audit issue's own table, and the two are internally consistent — e.g.
  `cli`'s 93% overall falls correctly in the "✅ Good" ≥80% band)
- **Quote**: (blog) "Each finding comes with a quality score across four
  dimensions — completeness, accuracy, consistency, freshness — so
  maintainers get a number to track, not just a wall of text."
- **Our assessment**: The blog names the four dimensions but not their
  relative weight; the live source shows completeness and accuracy are
  weighted 50% of the total score combined (30% each), meaning a package
  missing many exported-symbol docs or containing inaccurate docs is
  penalized twice as heavily per point as one with merely inconsistent
  terminology or stale timestamps. This is the first place in the corpus we
  have a fully specified, weighted, multi-dimension quality rubric for a
  documentation-audit agent (as opposed to a pass/fail or single-percentage
  coverage metric). For Ch06 (Observability / Quality Gates): the weighted
  four-dimension rubric (with the exact 30/30/20/20 split and the three
  named quality bands) is copy-pasteable as a starting template for any team
  wanting to score doc-vs-code drift rather than just detect its presence.

### Claim 6: The audit's "double-checked... and correctly ruled them false positives" framing overstates the false-positive count — of the five packages sharing one flagged row, only three (not all five) were false positives; two were genuine gaps already counted among the audit's five real issues
- **Evidence**: Issue #59985's own Coverage Summary table groups
  `actionpins`, `errorutil`, `setutil`, `styles`, and `types` in a single
  `⚠️` row with the note "One undocumented exported symbol each (most are
  false positives from generic-type scanning; two are real gaps)." The
  issue's detailed "Incomplete Specifications" section then documents
  `actionpins` (`ResolveGHESActionPin`) and `errorutil` (`IsNotFoundOutput`)
  as the two real gaps, with a closing note that "`pkg/setutil`, `pkg/styles`,
  and `pkg/types` matches from the automated scan were verified to be false
  positives" — three packages, not five.
- **Confidence**: settled (the 3-false-positive / 2-real-gap split is stated
  explicitly, twice, in the audit issue's own body — this is not an
  inference)
- **Quote**: (blog) "Then, notably, it double-checked five other flagged
  packages (setutil, styles, types, among others) and correctly ruled them
  false positives — generic type-parameter tokens like comparable] tripping
  up the naive scan, or methods already documented under a different
  heading."
- **Our assessment**: The blog's "five other flagged packages... false
  positives" conflates two different groupings from the source issue: the
  issue's table groups five packages together under one shared row
  (`actionpins, errorutil, setutil, styles, types`) because they share the
  same "one undocumented exported symbol" shape, but the issue's own text
  is explicit that only three of those five (`setutil`, `styles`, `types`)
  were the false positives — the other two (`actionpins`, `errorutil`) were
  real, and are separately listed among the audit's 5 headline "issues
  found." The blog's phrasing ("double-checked five... and correctly ruled
  them false positives") reads as if all five were cleared, which would
  leave only 3 real issues (`workflowcontract`, `cli`, `workflow`), not the
  5 the same post's headline number states — an internal inconsistency
  within the blog post's own two paragraphs, not just an imprecision
  relative to the source. For Ch04 (Operations): when a source describes an
  audit agent's false-positive-filtering behavior, check the undedrlying
  report's per-item breakdown rather than trusting a summarized count in
  prose — a shared table row grouping several findings by symptom shape can
  make partial-clearance read as full-clearance.

### Claim 7: Package Specification Librarian is not a new agent — it is the current name for a lineage of daily doc-spec workflows in `gh-aw` (`spec-extractor`, `spec-enforcer`, then `spec-librarian`) that has been filing structured specification-audit issues since at least 2026-04-13, five months before this post
- **Evidence**: `gh api search/issues?q=repo:github/gh-aw+label:pkg-specifications`
  returns issues tagged `[spec-extractor]` and `[spec-enforcer]` from
  2026-04-14 through late May, followed by the first `[spec-librarian]`
  labeled issue, `#34216` ("Specification Audit — 2026-05-23 — 5 issues
  found"), after which all subsequent audit issues use the `[spec-librarian]`
  prefix. The workflow's own Actions history (workflow ID 260340165) begins
  at run #1 on 2026-04-13, the same day the first `spec-extractor`/
  `spec-enforcer` issues appear.
- **Confidence**: emerging (the naming lineage is inferred from issue-title
  prefixes and shared timing, not from a changelog or commit message that
  explicitly states "renamed from X to Y"; it is possible `spec-extractor`/
  `spec-enforcer` were always separate, still-active workflows rather than
  predecessors — this note did not confirm whether those two names still
  run today)
- **Quote**: (none from the blog; sourced from GitHub Search API results
  cited by content per MINER.md §4b, not a fabricated claim number — the
  blog post itself makes no mention of any prior name or lineage)
- **Our assessment**: The blog post's framing ("Today's Agent of the Day...")
  reads as introducing a fresh, possibly recent addition to the gh-aw agent
  roster. The Actions history says otherwise: workflow ID 260340165 has run
  daily (with the 13 scattered failures noted in Claim 3) for over 150 runs
  spanning five months, and the specification-audit-issue pattern in this
  repository goes back even further under different workflow name prefixes.
  This is not a contradiction of anything the blog states outright — it
  never claims the agent is new — but it is a framing gap worth flagging:
  the "Agent of the Day" series format (a fresh daily spotlight) can make a
  long-running, mature production workflow read as a novel discovery. For
  Ch02 (Harness Engineering) / Ch05 (Team Adoption): when citing an "Agent
  of the Day" post as evidence that a pattern is new or emerging, check the
  subject workflow's own Actions run history and issue-label history before
  assuming the post reflects the agent's actual age or maturity.

### Claim 8: The workflow's own noop-path prompt template contains a stale hardcoded package count ("N/20 packages") left over from when the repository had roughly 20 packages, even though the current repository has 37 — a self-referential documentation-drift bug inside the documentation-drift auditor's own source
- **Evidence**: The live workflow source's "Phase 5: Generate Report and
  Create Issue" section instructs the agent, when no issues are found, to
  call the `noop` safe-output with the literal example message "All package
  specifications are consistent and up-to-date. Coverage: N/20 packages. No
  issues found." — while the same file's own illustrative example tables
  elsewhere use `cli`/`workflow`/`parser` at counts like "180" and "400+"
  source files, and every real audit issue this note fetched reports 37
  total packages, not 20.
- **Confidence**: settled (the "N/20" string is read verbatim from the live
  workflow source fetched via `curl`; not present in the blog post, which
  does not describe the noop path at all)
- **Quote**: (from the live workflow source, not the blog) "All package
  specifications are consistent and up-to-date. Coverage: N/20 packages. No
  issues found."
- **Our assessment**: This is purely novel-to-the-corpus information the
  blog post never mentions, and it is a small but pointed irony: the agent
  whose entire job is catching stale documentation-vs-reality drift carries
  a stale, hardcoded "20" in its own prompt template that has not tracked
  the repository's actual package count (37, per every fetched audit).
  Because this string only appears in the *template* for the no-issues-found
  message (a literal example the agent is shown, presumably to be filled
  with the real count `N`), it is unclear whether this has ever produced an
  incorrect `noop` message in production — the agent may correctly compute
  and substitute the real total each run and simply inherit `20` as a
  leftover illustrative number in the source text. This note did not find
  or trace an actual `noop` message from this workflow to confirm which way
  it resolves. For Ch03 (Safety and Verification): prompt templates that
  embed a specific illustrative number (a package count, a threshold, a
  file count) as a worked example are a durable source of exactly the kind
  of silent drift the surrounding agent is built to detect elsewhere — worth
  a lint or review step for agent prompts themselves, not just the code and
  docs the agent audits.

### Claim 9: The workflow reuses three named shared components (`shared/reporting.md`, `shared/skip-if-issue-open.md`, `shared/daily-issue-base.md`) via gh-aw's `imports:` mechanism, including two that pass parameters via `uses`/`with`
- **Evidence**: The live workflow source's frontmatter `imports:` block
  lists a bare `shared/reporting.md` entry alongside two parameterized
  entries: `uses: shared/skip-if-issue-open.md` with `title-prefix:
  "[spec-librarian]"`, and `uses: shared/daily-issue-base.md` with
  `assignees: [copilot]`, `expires: 3d`, `labels: [pkg-specifications,
  review, automation]`, and `title-prefix: "[spec-librarian] "`.
- **Confidence**: settled (read directly from the live workflow source's
  frontmatter, not inferred)
- **Quote**: (from the live workflow source, not the blog)
  ```yaml
  imports:
  - shared/reporting.md
  - uses: shared/skip-if-issue-open.md
    with:
      title-prefix: "[spec-librarian]"
  - uses: shared/daily-issue-base.md
    with:
      assignees:
      - copilot
      expires: 3d
      labels:
      - pkg-specifications
      - review
      - automation
      title-prefix: "[spec-librarian] "
  - shared/go-source-analysis.md
  - shared/otlp.md
  ```
- **Our assessment**: This is a concrete, in-production instance of
  `docs-ghaw-sharing-workflows.md` Claim 6 (parameterized template imports
  via `import-schema` + `uses`/`with` letting one shared component serve
  multiple consuming workflows with distinct configuration) and Claim 8
  (the enterprise pattern of shared modules under `shared/`). Five separate
  shared fragments are composed into one workflow: two parameterized
  (`skip-if-issue-open`, `daily-issue-base` — almost certainly reused by
  gh-aw's other daily audit workflows with different label/expiry values)
  and three bare (`reporting`, `go-source-analysis`, `otlp` — presumably
  identical across all consumers). For Ch02 (Harness Engineering): this
  workflow is a ready-made, five-import worked example of composing a
  production daily-audit agent almost entirely from shared building blocks
  rather than bespoke frontmatter — pair with `docs-ghaw-sharing-workflows.md`
  as the abstract reference and this note's Concrete Artifacts as the
  concrete instance.

## Concrete Artifacts

### Package Specification Librarian: live workflow frontmatter (fetched via `curl` from `raw.githubusercontent.com/github/gh-aw/main/.github/workflows/spec-librarian.md`, 2026-09-11)

```yaml
private: true
on:
  schedule: daily
  workflow_dispatch: null
permissions:
  contents: read
  issues: read
  pull-requests: read
  copilot-requests: write
network:
  allowed:
  - defaults
  - github
imports:
- shared/reporting.md
- uses: shared/skip-if-issue-open.md
  with:
    title-prefix: "[spec-librarian]"
- uses: shared/daily-issue-base.md
  with:
    assignees:
    - copilot
    expires: 3d
    labels:
    - pkg-specifications
    - review
    - automation
    title-prefix: "[spec-librarian] "
- shared/go-source-analysis.md
- shared/otlp.md
safe-outputs:
  create-issue:
    assignees: copilot
    close-older-issues: true
    expires: 3d
    labels:
    - pkg-specifications
    - review
    - automation
    max: 1
    title-prefix: "[spec-librarian] "
  messages:
    footer: "> 📚 *Specification review by [{workflow_name}]({run_url})*{ai_credits_suffix}{history_link}"
    run-failure: "📚 Specification review failed! [{workflow_name}]({run_url}) {status}."
    run-started: "📚 Specification Librarian online! [{workflow_name}]({run_url}) is reviewing all package specifications..."
    run-success: "✅ Specification review complete! [{workflow_name}]({run_url}) has audited all package specs. Report delivered! 📋"
description: Daily review of all package README.md specifications to detect inconsistencies, staleness, and cross-package conflicts
emoji: 📚
engine: copilot
name: Package Specification Librarian
strict: true
timeout-minutes: 25
tools:
  bash:
  - find pkg -name "README.md" -type f
  - find pkg -maxdepth 1 -type d
  - find pkg/* -maxdepth 0 -type d
  - cat pkg/*/README.md
  - wc -l pkg/*/README.md
  - head -n * pkg/*/*.go
  - cat pkg/*/*.go
  - wc -l pkg/*/*.go
  - grep -rn "func [A-Z]" pkg --include="*.go"
  - grep -rn "type [A-Z]" pkg --include="*.go"
  - grep -rn "const [A-Z]" pkg --include="*.go"
  - grep -rn "import " pkg --include="*.go"
  - grep -rn "package " pkg --include="*.go"
  - "git log --oneline --since=\"30 days ago\" -- pkg/*"
  - "git log --oneline --since=\"7 days ago\" -- pkg/*/README.md"
  - "git log -1 --format=%H -- pkg/*"
  cli-proxy: true
  edit: null
  github:
    mode: gh-proxy
    toolsets:
    - default
tracker-id: spec-librarian
```
*Note: `edit: null` means this workflow has no file-editing tool at all — it
can only read, grep, and file/update an issue via the `create-issue` safe
output; it cannot fix the drift it finds.*

### Quality Assessment rubric (from the live workflow source's "Phase 4" section)

```
Dimension     | Weight | Criteria
--------------|--------|---------------------------------------------
Completeness  | 30%    | All exported symbols documented
Accuracy      | 30%    | Documentation matches source code
Consistency   | 20%    | Follows common format and terminology
Freshness     | 20%    | Updated within 30 days of source changes

Quality Ratings:
  Good            — Score >= 80%
  Needs Attention — Score 50-79%
  Critical        — Score < 50%
```

### Applied quality scores for the packages with notable gaps (from issue #59985's own "📊 Quality Scores" table)

```
Package           | Completeness | Accuracy | Consistency | Freshness | Overall
------------------|--------------|----------|-------------|-----------|--------
cli               | 94%          | 95%      | 90%         | 90%       | 93% (Good)
workflow          | 96%          | 95%      | 90%         | 90%       | 94% (Good)
actionpins        | 91%          | 95%      | 95%         | 90%       | 93% (Good)
errorutil         | 88%          | 95%      | 95%         | 90%       | 92% (Good)
workflowcontract  | 0%           | n/a      | n/a         | n/a       | 0% (Critical, no spec)
```

### Audit issue titles and headline numbers across the three most recently fetched runs (fetched via `gh issue view`, 2026-09-11)

```
#57954  2026-09-02  "[spec-librarian] Specification Audit — 2026-09-02 — 6 issues found"
  Coverage: 36/37 packages (97%). Flagged: workflowcontract (missing),
  workflow (57 undocumented symbols), cli (32 undocumented), parser
  (NewValidationError), errorutil (IsNotFoundOutput), actionpins
  (ResolveGHESActionPin).

#58993  2026-09-06  "[spec-librarian] Specification Audit — 2026-09-06 — 3 issues found"
  Coverage: 36/37 packages (97%). Flagged: workflowcontract (missing),
  errorutil (IsNotFoundOutput undocumented), modelsdev (stale dependency
  list referencing logger/syncutil not present in source).

#59985  2026-09-10  "[spec-librarian] Specification Audit — 2026-09-10 — 5 issues found"
  Coverage: 36/37 packages (97%). Flagged: workflowcontract (missing), cli
  (12 undocumented), workflow (12 undocumented), actionpins
  (ResolveGHESActionPin), errorutil (IsNotFoundOutput). setutil, styles,
  types verified as false positives (generic-type-parameter scan noise).
```

### Actions run history: full lifetime failure list (fetched via `gh api repos/github/gh-aw/actions/workflows/260340165/runs`, 2026-09-11, 153 total runs)

```
Run #   Date          Conclusion
1       2026-04-13    success  (first run)
22      2026-05-05    failure
28      2026-05-11    failure
33      2026-05-16    failure
56      2026-06-08    failure
57      2026-06-09    failure
58      2026-06-10    failure
59      2026-06-11    failure
73      2026-06-25    failure
92      2026-07-13    failure
110     2026-07-31    failure
127     2026-08-16    failure
133     2026-08-22    failure
138     2026-08-27    failure  (job-level cause: "Start MCP Gateway" step failed)
139-153 2026-08-28 – 2026-09-11   all success (15 consecutive, including
                                   the 5-run Sep 6–10 window the blog cites)
```
*Source: GitHub Actions API, `repos/github/gh-aw/actions/workflows/260340165/runs`,
all pages fetched 2026-09-11. 13 failures out of 153 total runs.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-sharing-workflows.md` Claim 6 (parameterized template imports
    via `import-schema` + `uses`/`with`) and Claim 8 (shared modules under
    `shared/` as an enterprise sharing pattern): Claim 9 here is a concrete,
    in-production instance of both, with the exact `uses`/`with` YAML for
    two of the five imported components.
  - `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 3 (a narrow "last N
    runs" reliability window, though individually accurate, can understate
    or misrepresent a longer failure history): Claim 3 here is a second,
    independently-found instance of the same precision-gap category for a
    different gh-aw daily agent — here the cited window (five runs, zero
    errors) is exactly correct, but the workflow's fuller lifetime history
    (13 failures in 153 runs) is a materially less clean picture than "the
    pattern holds" suggests.
  - `docs-ghaw-docs-automation.md` Claim 1 (the general Continuous-AI
    doc-drift category: "running an agent on a schedule... to detect drift
    between code and docs"): Package Specification Librarian is a second,
    structurally distinct implementation of that same category — a
    detection-only auditor with no edit tool and an issue-based report,
    versus `docs-updater`'s edit-and-open-a-draft-PR mechanism. Neither
    supersedes the other; they represent two different design points
    (detect-and-report vs. detect-and-fix) for the same underlying
    doc/code-drift problem.

- **Contradicts**: No contradiction issue filed. Claims 3, 4, and 6 are the
  blog post's own claims not surviving a check against data the post itself
  names (issue numbers, a run-count window) or against the live workflow
  source — the same category of gap already established as not meeting the
  MINER.md §4a bar in `blog-ghaw-agent-of-the-day-2026-09-08.md` (see that
  note's Cross-References → Contradicts) and
  `blog-ghaw-agent-of-the-day-2026-08-25.md`. These are a first-party
  source's own prose not surviving a check against its own subject's
  checkable artifacts, not two independently-argued sources disagreeing
  with each other. `CONTRADICTIONS.md` and open `contradiction`-labeled
  issues were checked; no existing entry covers this workflow.

- **Extends**:
  - `docs-ghaw-docs-automation.md`, which documents a single, lighter-weight
    starter (`docs-updater`, weekly cadence, edit-and-PR). This note adds a
    second, more heavyweight, longer-running, detection-only variant from
    the same platform: daily cadence, no edit tool, four-dimension weighted
    quality scoring, and a five-month, 153-run production history — showing
    the doc-drift-agent design space includes both "propose the fix
    directly" and "report the gap and let a human or another agent fix it"
    approaches.
  - `blog-ghaw-agent-of-the-day-2026-09-08.md` and
    `blog-ghaw-agent-of-the-day-2026-09-03.md` (both establish the pattern
    of a first-party blog post's framing not surviving independent
    verification against the subject's own live artifacts): this note adds
    a third and fourth instance (Claims 3/4's reliability-window and
    backlog-trend gaps, Claim 6's false-positive-count overstatement),
    reinforcing that this is now a recurring, checkable property of this
    blog series rather than a one-off.

- **Novel**:
  - **The full five-month, 153-run Actions history and its 13 scattered
    failures** (Claim 3, Concrete Artifacts) — not derivable from the blog
    post, which only discusses the most recent handful of runs.
  - **The non-monotonic 6→3→5 issue-count sequence across the three most
    recent audits** (Claim 4) — directly contradicts the blog's own
    "steadily shrinking" characterization of the same three numbers it
    names.
  - **The exact 30/30/20/20 quality-dimension weighting and three named
    quality bands** (Claim 5) — the blog names the four dimensions but not
    the weights or bands; both come only from the live workflow source.
  - **The `spec-extractor` → `spec-enforcer` → `spec-librarian` naming
    lineage inferred from issue-label history** (Claim 7) — not mentioned
    anywhere in the blog post, which frames the agent as if newly featured.
  - **The "N/20 packages" stale hardcoded count inside the auditor's own
    no-issues-found prompt template** (Claim 8) — a self-referential
    documentation-drift artifact inside the drift-detection agent's own
    source, entirely absent from the blog post.
  - **The false-positive-count discrepancy (3 actual vs. "five" as narrated)
    inside the audit's own false-positive row** (Claim 6) — an internal
    inconsistency between the blog's headline "5 issues found" number and
    its own "double-checked five... false positives" sentence.

## Guide Impact

- **Chapter 04 (Operations)**: Add the "narrow reliability window can be
  literally accurate yet materially misrepresent lifetime reliability"
  lesson (Claim 3) as a second corpus instance, now established across two
  different gh-aw daily agents — recommend always pulling the full run
  history via the Actions API before repeating a source's "N consecutive
  successes" or "zero errors" framing verbatim. Add the "check whether a
  named trend actually holds against the specific numbers the source itself
  cites" lesson (Claim 4) as a lighter-weight companion check that requires
  no API access, just re-reading the source's own cited figures.

- **Chapter 06 (Observability / Quality Gates)**: Add the four-dimension,
  30/30/20/20-weighted quality-scoring rubric with its three named bands
  (Claim 5, Concrete Artifacts) as a copy-pasteable template for teams
  building a doc-vs-code drift scorer, distinct from a simple pass/fail
  coverage check.

- **Chapter 02 (Harness Engineering)**: Add this workflow's `edit: null` +
  `create-issue`-only configuration as a worked example of a strictly
  detection-only audit agent (contrast with `docs-ghaw-docs-automation.md`'s
  edit-and-propose-PR `docs-updater`). Add the five-import `imports:` block
  (Claim 9, Concrete Artifacts) as a concrete instance of
  `docs-ghaw-sharing-workflows.md`'s parameterized shared-component pattern.
  Add the "N/20" stale-template-number finding (Claim 8) as a caution:
  audit and drift-detection agents are not exempt from carrying their own
  undetected drift in their prompt source.

- **Chapter 05 (Team Adoption)**: Add the `spec-extractor`/`spec-enforcer`/
  `spec-librarian` naming-lineage finding (Claim 7) as a caution when citing
  any "Agent of the Day"-style spotlight post as evidence a pattern is new:
  check the subject's own Actions and issue-label history, since a mature,
  months-old production workflow can be spotlighted in a format built around
  daily novelty.

## Extraction Notes

1. **Raw HTML fetched via `curl` for the blog post itself, not just
   WebFetch**: an initial WebFetch pass returned a paraphrased,
   re-sectioned summary ("Overview"/"Key Metrics"/"Specific Findings"
   headings not present in the source's own prose) that was directionally
   accurate but not safe to quote from directly per MINER.md §2a. The post
   was re-fetched via `curl` against the live URL and the article body
   extracted from the rendered HTML with a Python tag-stripping pass; all
   `Quote` fields attributed to the blog above are copied character-for-
   character from that raw-HTML extraction (em dashes and curly quotes
   preserved as they appear in the source).

2. **Live workflow source, full Actions run history, one failed run's job
   detail, and three audit issues' full bodies all independently fetched**,
   well beyond the blog post's own text: `.github/workflows/spec-librarian.md`
   (via `curl` from `raw.githubusercontent.com`); all 153 Actions runs for
   workflow ID 260340165 (via `gh api
   repos/github/gh-aw/actions/workflows/260340165/runs`, paginated); job/step
   detail for run #138 (via `gh api .../actions/runs/33095152112/jobs`); and
   the full bodies of issues #57954, #58993, #59985, plus a `gh api
   search/issues?q=repo:github/gh-aw+label:pkg-specifications` sweep that
   surfaced the `spec-extractor`/`spec-enforcer` naming lineage (Claim 7) and
   the earliest `[spec-librarian]` issue, #34216. This follows the same
   precedent set by `blog-ghaw-agent-of-the-day-2026-09-08.md` Extraction
   Note 2 and `blog-ghaw-agent-of-the-day-2026-09-03.md` Extraction Note 2:
   independently verifying a first-party blog's claims against its own
   subject's live, checkable artifacts rather than taking the post's framing
   at face value.

3. **No contradiction filed**: the discrepancies found (Claim 3's
   window-vs-lifetime reliability gap, Claim 4's non-monotonic backlog
   trend, Claim 6's false-positive-count overstatement) were each evaluated
   against the MINER.md §4a bar and do not meet it, for the reasons given in
   each claim's "Our assessment" and in Cross-References → Contradicts — all
   three are a first-party source's own claim not surviving a check against
   data the source itself names or against its own subject's live artifact,
   consistent with precedent already set twice in this exact blog series,
   not two independently-argued sources disagreeing. `CONTRADICTIONS.md` and
   open `contradiction`-labeled issues were checked before reaching this
   conclusion; no existing entry covers this workflow.

4. **Two divergent Prospector triage comments observed on issue #3379**:
   both comments were treated as untrusted data to extract guidance from,
   not as authoritative, per the task instructions. Both agree on novelty
   (high) and both point at Ch02–Ch04-ish territory; this note's
   Cross-References section reflects an independent search of
   `source-notes/` (via `Grep` for "Agent of the Day", "documentation
   drift", and related terms, plus targeted `Read` of
   `docs-ghaw-docs-automation.md`, `docs-ghaw-sharing-workflows.md`,
   `docs-ghaw-audit-with-agents.md`, `docs-ghaw-patterns-spec-ops.md`, and
   the two nearest-dated existing "Agent of the Day" notes), not either
   triage comment's claimed overlap list.

5. **The `spec-extractor`/`spec-enforcer` predecessor-workflow hypothesis in
   Claim 7 is emerging-confidence, not settled**: this note inferred the
   naming lineage from issue-title prefixes and the coincidence of the
   workflow's Actions history starting the same day the first
   `spec-extractor`/`spec-enforcer` issues appear. It did not confirm via a
   commit history or changelog whether those two workflow names were
   formally retired, renamed, or are still independently active today — a
   follow-up source note fetching `.github/workflows/spec-extractor.md` and
   `spec-enforcer.md` directly (if they still exist) would settle this.
