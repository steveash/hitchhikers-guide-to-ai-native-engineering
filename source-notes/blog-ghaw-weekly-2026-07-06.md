---
source_url: https://github.github.com/gh-aw/blog/2026-07-06-weekly-update/
source_type: blog-post
title: "Weekly Update – July 6, 2026 (GitHub Agentic Workflows)"
author: GitHub Agentic Workflows team (gh-aw)
date_published: 2026-07-06
date_extracted: 2026-07-07
last_checked: 2026-07-07
status: current
confidence_overall: emerging
issue: "#1606"
---

# Weekly Update – July 6, 2026 (GitHub Agentic Workflows)

> The July 6 week ships five merged PRs: a compiler fix that auto-wires a
> missing `pre_activation` job dependency in generated lock files (PR #43570);
> consolidation of duplicated AST/context linter helpers into a shared
> `internal/astutil` package (PR #43649); a ~28% reduction (27,299 → 11,876
> characters) in the `copilot-agent-analysis` ambient-context first-request
> payload via cold-start gating (PR #43619); a shared prompt quality rubric
> introduced after agent-review effectiveness scores plateaued at 61–62 for
> several weeks (PR #43527); and a 23-file JavaScript correctness sweep in
> `actions/setup/js` (PR #43637). The `weekly-issue-summary` Agent of the Week
> is a scheduled reporting agent that compiles 30 days of issue activity into
> trend charts and resolution statistics at ~59 AI Credits and 13 GitHub API
> calls per run, extending — not originating — the reporting-agent pattern
> already documented for `api-consumption-report`.

## Source Context

- **Type**: blog-post (weekly changelog/update from the official GitHub
  Agentic Workflows blog; covers the week ending July 6, 2026; five named PRs
  across the compiler, linter infrastructure, ambient-context cost, prompt
  quality process, and JavaScript setup scripts, plus an Agent of the Week
  spotlight on `weekly-issue-summary`)
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team; this post's byline is "Copilot"
  (per the page's on-page byline and its `schema.org/BlogPosting` JSON-LD,
  which names the author as `copilot`), distinct from the human-bylined posts
  in this corpus (Don Syme, Peli de Halleux, Mara Kiefer — see
  `blog-ghaw-agent-observability.md`). Unlike the June 22 and June 29 weekly
  posts, whose PR numbers are printed as visible inline text in the article
  body, this post's PR numbers are present only as the `href` targets of each
  section heading link (e.g., the "fix(compiler)…" heading links to
  `https://github.com/github/gh-aw/pull/43570`) and are not shown as visible
  `#NNNNN` text anywhere in the rendered page. This is a first-party account
  of the team's own production system, and the PR numbers are independently
  resolvable (confirmed by inspecting the page's raw HTML), but the shift from
  inline-visible citations to link-only citations is a presentation change
  worth flagging — see Extraction Notes.
- **Scope**: Covers five merged PRs (compiler fix #43570, linter refactor
  #43649, ambient-context reduction #43619, prompt quality gate #43527,
  setup/js sweep #43637) and the `weekly-issue-summary` Agent of the Week.
  Does NOT cover: the exact diff or line-level implementation of any PR; the
  full text of the new shared prompt quality rubric; the specific 23 file
  names touched in the setup/js sweep; the internal structure of the
  `internal/astutil` package beyond the three named helpers; or a
  root-cause writeup for the `weekly-issue-summary` timeout mentioned in the
  Agent of the Week section.

## Extracted Claims

### Claim 1: A compiler bug generated `skillet.lock.yml` files with broken actionlint expressions because `safe_outputs` and `conclusion` jobs referenced `${{ needs.pre_activation.outputs.skill_name }}` without declaring `pre_activation` as an explicit job dependency; the fix (PR #43570) auto-wires the dependency whenever a message template references `pre_activation` outputs

- **Evidence**: PR #43570 (linked from the section heading). The post names the
  broken expression pattern, the two job types affected (`safe_outputs` and
  `conclusion`), and the fix mechanism (auto-wiring the dependency on template
  reference).
- **Confidence**: emerging (single PR, first-party changelog description; the
  exact template-detection mechanism used to trigger auto-wiring is not
  described)
- **Quote**: "A sneaky compiler bug was generating skillet.lock.yml files with
  broken actionlint expressions: safe_outputs and conclusion jobs referenced
  ${{ needs.pre_activation.outputs.skill_name }} without actually declaring
  pre_activation as a dependency. This fix auto-wires the dependency whenever
  a message template references pre_activation outputs — no more cryptic
  expression errors in generated lock files."
- **Our assessment**: This is a concrete instance of a class of compiler bug
  familiar from GitHub Actions workflow generation generally: a generated
  workflow references `needs.<job>.outputs.<field>` in an `if:` or templated
  expression without the job appearing in that job's `needs:` array, which
  GitHub Actions (and actionlint, statically) flags as invalid — the
  referenced output is simply unavailable at evaluation time because the
  dependency edge doesn't exist in the job graph. `docs-ghaw-compilation-process.md`
  documents `pre_activation` as the job that "Always (runs first)" and performs
  "Role checks, deadlines, skip-if-match dedup, command position validation" —
  exactly the kind of job whose outputs (like a computed `skill_name`) other
  jobs would want to consume in downstream messaging. That same note documents
  `gh aw compile --actionlint --zizmor --poutine` as the recommended
  security-scanner-integrated compile command (Claim 11 there); actionlint is
  the specific tool this bug's symptom ("broken actionlint expressions") would
  have been caught by, which raises the question of why this shipped
  undetected — the fix is reactive (a bug report or internal test caught it),
  not the result of running the documented `--actionlint` flag proactively in
  CI for this code path. For Ch02 (Harness Engineering): this is a concrete
  argument for treating compiler-generated job dependency graphs as a class of
  correctness bug to test explicitly — the fix pattern (auto-wire the
  dependency edge whenever a template references a job's outputs) generalizes
  to any code generator that stitches together templated expressions across a
  declared job graph.

### Claim 2: Duplicated AST/context helper functions (`enclosingFuncType`, context-type resolution, OS-call detection) scattered across individual linter analyzers were consolidated into a single `internal/astutil` package (PR #43649)

- **Evidence**: PR #43649 (linked from the section heading). The post names
  three specific duplicated helper categories and the new consolidated
  package path.
- **Confidence**: emerging (single PR, first-party changelog description; the
  number of analyzers affected and the resulting line-count reduction are not
  quantified)
- **Quote**: "The linter suite had quietly grown several copies of the same
  helper functions — enclosingFuncType, context-type resolution, OS-call
  detection — scattered across individual analyzers. This PR gathers them all
  into a single pkg/linters/internal/astutil package and rewires the affected
  analyzers, eliminating drift risk and making future linter work easier to
  reason about."
- **Our assessment**: This is a maintainability refactor of the gh-aw custom
  Go linter infrastructure itself, distinct from the addition of new analyzer
  rules (the pattern documented in `blog-ghaw-custom-linters-three-workflow-loop.md`).
  That note's Claim 1 describes a "three interconnected workflows" system
  (Linter Miner invents, Sergo challenges, LintMonster applies) that has grown
  the analyzer registry in `cmd/linters/main.go` to 35+ entries; as that
  registry grows via Linter Miner's continuous rule invention, duplicated
  helper logic across independently-authored analyzers is exactly the drift
  risk that a shared `astutil` package addresses. Neither this post nor the
  three-workflow-loop note states whether this consolidation PR was itself
  produced by one of the three named workflows (Linter Miner, Sergo, or
  LintMonster) or by a human/other-agent contributor — the "quietly grown"
  framing suggests organic accumulation across many small PRs rather than a
  single origin. For Ch02 (Harness Engineering): shared-helper consolidation
  for a growing family of independently-generated static analyzers is a
  concrete maintenance pattern worth naming alongside the invent/challenge/apply
  loop — as an analyzer registry scales via automated rule invention, periodic
  helper consolidation is the counterpart hygiene practice that keeps
  per-analyzer code from drifting.

### Claim 3: The `copilot-agent-analysis` ambient-context payload — the largest such payload in gh-aw at 27,299 characters — was reduced to 11,876 characters (~28%) for the first request by gating cold-start rebuild content behind an optional import (PR #43619)

- **Evidence**: PR #43619 (linked from the section heading). The post gives
  exact before/after character counts (27,299 → 11,876) and names the
  optimization mechanism (gating cold-start rebuild content behind an optional
  import).
- **Confidence**: settled (specific PR, exact before/after character counts
  quoted verbatim, specific optimization mechanism named)
- **Quote**: "copilot-agent-analysis was the largest ambient-context payload
  at 27,299 characters — most of it content that's rarely needed at runtime.
  By gating cold-start rebuild content behind an optional import, this PR
  trims the first-request size to 11,876 characters, cutting token costs on
  every agent activation that uses this analysis path."
- **Our assessment**: 11,876 / 27,299 ≈ 43.5% of the original size, i.e. a
  reduction of ≈56.5% in absolute character count — the post's own "~28%"
  framing does not match a straightforward before/after percentage-of-original
  or percentage-reduction calculation from the two numbers it quotes, unless
  "~28%" refers to something else (e.g. reduction as a fraction of some other
  baseline, or an approximation using a different pair of numbers than the
  ones printed in this passage). We flag this arithmetic discrepancy rather
  than silently recomputing a different percentage in its place; see
  Extraction Notes. Independent of the exact percentage, this is the same
  ambient-context-payload-reduction pattern documented twice already in this
  corpus: `blog-ghaw-weekly-2026-06-15.md` Claim 12 (PR #39157, ambient-context
  payload reduced across daily and PR workflows) and `blog-ghaw-weekly-2026-06-22.md`
  Claim 5 (PR #40695, initial system-prompt compression in high-traffic
  workflows). `docs-ghaw-audit-reference.md` Claim 4 documents the `ambient_context`
  metrics object exposed by `gh aw audit` — "first LLM inference footprint"
  with input/cached/effective token sub-fields — as the measurement mechanism
  that would surface exactly this kind of payload-size regression. Gating
  "cold-start rebuild content" behind an optional import is a new
  *mechanism* for this recurring optimization category: the June 15 and June
  22 passes are described only as trims/compressions without naming a
  code-level technique, whereas this PR describes conditional/lazy imports as
  the implementation. For Ch02 (Harness Engineering) / cost optimization:
  gating rarely-needed ambient-context content behind optional imports is a
  concrete, reusable technique — not just "trim the prompt" but "defer loading
  content that isn't needed on the common (warm) path" — that should be added
  to the ambient-context reduction playbook alongside the June 15/June 22
  entries, and cross-referenced to the `ambient_context` audit metric as the
  way to detect when a payload has grown large enough to warrant this
  treatment.

### Claim 4: A shared prompt quality rubric was introduced for agent-review workflows (PR #43527) after agent effectiveness scores had been stuck around 61–62 for several weeks, signaling that prompt design rather than runtime bugs was the limiting factor

- **Evidence**: PR #43527 (linked from the section heading). The post states
  the plateau range (61–62), its duration ("several weeks"), the diagnosis
  (prompt design, not runtime bugs), and the fix (a reusable quality rubric
  shared across analyzer and reviewer workflows).
- **Confidence**: emerging (single PR, first-party changelog description; the
  effectiveness-score metric's definition, the specific rubric criteria, and
  which analyzer/reviewer workflows adopted it are not detailed in this post)
- **Quote**: "Agent effectiveness scores had been stuck around 61–62 for
  several weeks — a signal that prompt design, not runtime bugs, was the
  limiting factor. This PR introduces a reusable quality rubric shared across
  analyzer and reviewer workflows, giving those workflows a concrete target
  for what "good" looks like and a path out of the plateau."
- **Our assessment**: This is the first source in the corpus to document a
  named "effectiveness score" metric plateauing over a multi-week period as
  the trigger for a deliberate prompt-design intervention, and to frame the
  fix as a *shared* rubric applied across multiple workflow categories
  (analyzer and reviewer) rather than a per-workflow prompt rewrite. The
  diagnostic move — distinguishing "prompt design problem" from "runtime bug"
  when a quality metric stalls rather than crashes — is a useful evaluation
  pattern: a stable-but-mediocre score, unlike an error rate or crash rate,
  doesn't surface as an incident and can go unaddressed without an explicit
  plateau-detection habit. The post does not say what "effectiveness score"
  measures or how it's computed, so we cannot verify whether 61-62 is
  measured on the same scale as any other quality metric already in the
  corpus (e.g., `agent-persona-explorer`'s five-dimension scoring in
  `blog-ghaw-weekly-2026-06-29.md` Claim 9). For Ch03 (Agent Orchestration):
  add "plateaued effectiveness score → shared prompt quality rubric" as a
  named remediation pattern for teams running families of related evaluation/
  review workflows — when several workflows share a quality ceiling, a
  cross-workflow rubric can be a more leveraged fix than tuning each prompt
  independently.

### Claim 5: A sweep across 23 files in `actions/setup/js` replaced global `isNaN` with `Number.isNaN`, fixed `core.setOutput` value types, and cleaned up unhandled async rejections (PR #43637)

- **Evidence**: PR #43637 (linked from the section heading). The post names
  the exact file count (23), the specific anti-pattern fixed (`isNaN` →
  `Number.isNaN`), the second fix category (`core.setOutput` value types), and
  the third (unhandled async rejections).
- **Confidence**: settled (specific PR, exact file count, named specific
  functions and fix categories)
- **Quote**: "A sweep across 23 files in actions/setup/js replaced global
  isNaN (which silently coerces inputs) with Number.isNaN, fixed core.setOutput
  value types, and cleaned up unhandled async rejections. Small correctness
  improvements that prevent subtle runtime surprises in CI steps."
- **Our assessment**: Global `isNaN` coerces its argument to a number before
  testing (so `isNaN("foo")` is `true` but so is `isNaN(undefined)`,
  and non-numeric strings and other falsy-ish values can produce
  surprising results), while `Number.isNaN` only returns `true` for the
  actual `NaN` value — a well-known JavaScript correctness footgun, and this
  fix is a straightforward hardening pass rather than a novel pattern. This is
  the same "23-file correctness sweep" category as the linter-driven Go fixes
  documented elsewhere in the corpus (`blog-ghaw-custom-linters-three-workflow-loop.md`),
  but for the platform's JavaScript setup scripts rather than Go, and the post
  does not state whether this sweep was linter-driven (i.e., produced by an
  automated JS-equivalent of the Go linter registry) or a manual audit. For
  Ch02 (Harness Engineering): global `isNaN` vs. `Number.isNaN` is a concrete,
  generalizable JavaScript linting rule worth adding to any Node.js-based
  agent-harness tooling, independent of the gh-aw context.

### Claim 6: The `weekly-issue-summary` Agent of the Week runs every Monday around 3 PM UTC, pulls 30 days of issue data, generates CSV trend files, and renders two charts (issue open/close velocity and resolution-time distribution), consuming roughly 59 AI Credits and 13 GitHub API calls per run across its last three runs

- **Evidence**: "Agent of the Week" spotlight section. The post states the
  schedule (Monday, ~3 PM UTC), the data window (30 days), the two output
  artifact types (CSV trend files, two named chart types), and per-run cost
  (13 API calls, ~59 AI Credits) averaged/typical across "its last three
  runs." A link to the workflow definition
  (`https://github.com/github/gh-aw/blob/main/.github/workflows/weekly-issue-summary.md`)
  is provided.
- **Confidence**: emerging (single-agent spotlight, small sample of three
  runs, first-party changelog description; no baseline comparison to a prior
  period, and the workflow's underlying prompt/frontmatter is not shown)
- **Quote**: "weekly-issue-summary has been running quietly every Monday
  around 3 PM UTC, pulling 30 days of issue data, generating CSV trend files,
  and rendering two charts: one for issue open/close velocity and one for
  resolution time distributions. In its last three runs it made 13 GitHub API
  calls each time and burned through roughly 59 AI credits — efficient for a
  workflow that touches every open and closed issue in the repo."
- **Our assessment**: Per `blog-ghaw-ai-credits-migration.md` Claim 1, 1 AIC =
  $0.01 USD, so ~59 AIC ≈ $0.59 per run for a workflow that (per the post)
  "touches every open and closed issue in the repo" over a 30-day window —
  the post's own framing ("efficient") is a value judgment we can't
  independently verify without knowing the repo's issue volume, but the ratio
  of 13 API calls to a 30-day, full-repo issue sweep is notably low, which is
  consistent with using GitHub's search/list APIs (paginated queries) rather
  than per-issue calls. This is NOT the first reporting/dashboard-style Agent
  of the Week in the corpus: `blog-ghaw-weekly-2026-06-01.md` Claim 12
  documents `api-consumption-report`, which already "processed 95 runs (58
  successful, 37 failed) and tracked 10,619 GitHub API calls in a single day,
  generating trend charts published as GitHub Discussions" — an
  "observability-as-agent" pattern per that note's own assessment. `weekly-issue-summary`
  extends that pattern (issue-activity trends rather than API-consumption
  trends, a weekly 30-day rolling window rather than a daily snapshot, and CSV
  trend files as a named additional artifact type) rather than introducing a
  new agent category. For Ch06 (Agentic Operations): add `weekly-issue-summary`
  to the existing "reporting/data-journalism agent" category alongside
  `api-consumption-report`, and position the cost (~59 AIC per 30-day,
  full-repo sweep) as a second data point in that category's cost profile.

### Claim 7: One of `weekly-issue-summary`'s last three runs hit a timeout during the data-preparation phase and "bailed cleanly," and a separate observability report on a June 15th run flagged that the run "consumed a heavy execution profile for its task shape" and suggested swapping in a smaller model, after which the workflow "came back the following Monday working perfectly"

- **Evidence**: "Agent of the Week" spotlight section, two adjacent sentences:
  one describing the timeout/bail outcome as part of the "last three runs"
  summary, the next describing "the June 15th failure" and an observability
  report's model-sizing suggestion.
- **Confidence**: anecdotal (single narrative account of one workflow's
  failure/recovery across two consecutive Monday runs; no data on how many
  total runs preceded this, and no confirmation the "one run hit a timeout"
  sentence and "the June 15th failure" sentence describe the same incident)
- **Quote**: "Two of the three runs succeeded without any write-side effects,
  posting the full digest to a tracking issue, while one run hit a timeout on
  the data preparation phase and bailed cleanly." … "The June 15th failure is
  the fun part: the observability report flagged it with the note "this run
  consumed a heavy execution profile for its task shape" and gently suggested
  the team might want to swap in a smaller model. The workflow took the
  feedback in stride and came back the following Monday working perfectly."
- **Our assessment**: We flag, rather than silently resolve, an apparent
  looseness in the source's own narrative: the "last three runs" sentence
  describes a *timeout during data preparation* as the failure mode, while the
  very next sentence attributes "the June 15th failure" to an observability
  report about *execution-profile weight* (implicitly, a cost/resource
  concern, not a timeout) recommending a smaller model — these read as two
  different characterizations of what may or may not be the same single
  failed run. If they are the same run, the post is describing one failure
  from two angles (symptom: timeout; diagnosis: oversized execution profile
  for the task); if they are different runs, the post has only partially
  enumerated its failure history. Either reading is plausible from the text
  alone. Independent of that ambiguity, the underlying pattern —an automated
  observability report recommending a smaller model based on a run's
  "execution profile," and the team/workflow accepting that feedback for the
  next scheduled run — is a genuinely new angle in the corpus on model
  right-sizing: `blog-ghaw-agent-of-the-day-2026-05-29.md` Claim 8 documents
  model right-sizing as a *design-time* decision ("choosing a smaller, faster
  model when the task is textual classification with a fixed label set");
  this post describes right-sizing triggered *reactively* by a post-run
  observability signal rather than decided upfront at workflow design time.
  For Ch06 (Agentic Operations): add "observability-triggered model
  right-sizing" as a distinct sub-pattern alongside design-time right-sizing
  (`blog-ghaw-agent-of-the-day-2026-05-29.md` Claim 8) — a scheduled agent's
  execution profile, once measured in production, can itself be the signal
  that prompts a model downgrade for subsequent runs.

### Claim 8: The post recommends pairing `weekly-issue-summary` with a consistent issue-labeling strategy, because its resolution-time-distribution chart breakdowns become more useful when issues can be split by category

- **Evidence**: "Usage tip" callout at the end of the Agent of the Week
  section.
- **Confidence**: anecdotal (a single usage recommendation from the workflow's
  own authors, not independently tested or measured in this post)
- **Quote**: "Usage tip: Pair weekly-issue-summary with a label strategy — the
  chart breakdowns are most useful when issues are consistently labeled, since
  resolution-time distributions get interesting when you can split them by
  category."
- **Our assessment**: This is a straightforward but concrete operational
  dependency: an analytics/reporting agent's output value scales with the
  quality of the input metadata (issue labels) it can slice on, not just the
  raw event data (issue open/close timestamps) it ingests. For Ch06 (Agentic
  Operations): when documenting `weekly-issue-summary` (or any reporting
  agent that segments metrics by category), note that a prerequisite for
  getting full value from the tool is a maintained, consistent labeling
  taxonomy on the underlying data — the reporting agent doesn't create that
  taxonomy, it only reveals value already present in consistently-applied
  labels.

## Concrete Artifacts

### PR Summary: Week Ending July 6, 2026

```
Compiler:
  Fix: pre_activation dependency auto-wiring (PR #43570)
       Bug: safe_outputs / conclusion jobs referenced
            ${{ needs.pre_activation.outputs.skill_name }} without declaring
            pre_activation as a dependency -> broken actionlint expressions
            in generated skillet.lock.yml files
       Fix: auto-wire the dependency whenever a message template references
            pre_activation outputs

Linters:
  Refactor: consolidate AST/context helpers into internal/astutil (PR #43649)
       Duplicated helpers: enclosingFuncType, context-type resolution,
       OS-call detection
       New package: pkg/linters/internal/astutil

Cost / Ambient Context:
  Optimization: copilot-agent-analysis first-request size (PR #43619)
       Before: 27,299 characters (largest ambient-context payload in gh-aw)
       After:  11,876 characters
       Mechanism: gate cold-start rebuild content behind an optional import
       Stated reduction: "~28%" (see Claim 3 Our assessment re: arithmetic)

Process / Quality:
  Addition: shared prompt quality gate for agent-review workflows (PR #43527)
       Trigger: agent effectiveness scores plateaued at 61-62 for
                "several weeks"
       Fix: reusable quality rubric shared across analyzer and reviewer
            workflows

JavaScript:
  Fix: setup/js correctness sweep (PR #43637)
       Scope: 23 files in actions/setup/js
       Changes: global isNaN -> Number.isNaN
                core.setOutput value type fixes
                unhandled async rejection cleanup
```

### Agent of the Week: `weekly-issue-summary` — July 6, 2026

```
Agent:          weekly-issue-summary
Function:       "Your Monday morning data journalist" — scans all issue
                activity from the past week and compiles trends, charts,
                and resolution statistics into a single digest comment
Schedule:       Every Monday, ~3 PM UTC
Data window:    30 days of issue data (full repo — every open and closed
                issue)
Outputs:        CSV trend files
                Chart 1: issue open/close velocity
                Chart 2: resolution-time distributions
                Digest posted as a comment on a tracking issue

Cost (last three runs, per run):
  GitHub API calls: 13
  AI Credits:       ~59 (~$0.59 at 1 AIC = $0.01 USD, per
                     blog-ghaw-ai-credits-migration.md Claim 1)

Run outcomes (last three runs):
  2/3: succeeded, posted digest, no unexpected write-side effects
  1/3: timeout during data-preparation phase, "bailed cleanly"

June 15th incident:
  Observability report note: "this run consumed a heavy execution profile
  for its task shape"
  Suggestion: swap in a smaller model
  Outcome: workflow ran successfully the following Monday

Usage tip (from source): pair with a consistent issue-label strategy —
  resolution-time breakdowns are more useful when issues can be split by
  category

Workflow definition:
  https://github.com/github/gh-aw/blob/main/.github/workflows/weekly-issue-summary.md
```

*Source: this week's blog post, all sections (fetched 2026-07-07)*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-weekly-2026-06-15.md` Claim 12 (ambient-context payload
    reduced across daily and PR workflows, PR #39157) and
    `blog-ghaw-weekly-2026-06-22.md` Claim 5 (initial system-prompt
    compression in high-traffic workflows, PR #40695): Claim 3 here
    (`copilot-agent-analysis` first-request size cut from 27,299 to 11,876
    characters, PR #43619) is a third instance of the same recurring
    ambient-context-reduction optimization category, now with a named
    mechanism (gating cold-start content behind an optional import) that the
    two prior instances did not specify.
  - `docs-ghaw-audit-reference.md` Claim 4 (the `ambient_context` metrics
    object in `gh aw audit` output captures "first LLM inference footprint"
    with input/cached/effective token sub-fields): the payload-size
    measurement described in Claim 3 here is exactly the quantity that metric
    is designed to surface, though this post does not state whether the
    27,299/11,876 character counts were measured via `gh aw audit` or by some
    other means.
  - `blog-ghaw-ai-credits-migration.md` Claim 1 (AI Credits, AIC, replaced
    Effective Tokens as the primary spend metric; 1 AIC = $0.01 USD): the
    ~59 AIC figure in Claim 6 here uses the post-migration unit, consistent
    with all gh-aw cost reporting in the corpus since that migration.
  - `docs-ghaw-compilation-process.md` (job types table: `pre_activation` runs
    always/first for role checks, deadlines, dedup, and command-position
    validation; `conclusion` runs `always()` when safe outputs exist to
    aggregate results): Claim 1 here describes a concrete bug in exactly the
    dependency edge between `pre_activation` and the `safe_outputs`/
    `conclusion` jobs that table documents as consumers of `pre_activation`'s
    outputs.

- **Extends**:
  - `blog-ghaw-custom-linters-three-workflow-loop.md` (Linter Miner / Sergo /
    LintMonster manage 35+ custom Go analyzers registered in
    `cmd/linters/main.go`): Claim 2 here (consolidating duplicated
    `enclosingFuncType`/context-resolution/OS-call-detection helpers into
    `internal/astutil`, PR #43649) is a maintenance action on that same
    analyzer suite's shared infrastructure, but the source does not state
    whether this consolidation PR was produced by Linter Miner, Sergo,
    LintMonster, or an unrelated contributor — unlike that note's six
    explicitly-attributed Linter Miner PRs (fprintlnsprintf through
    stringreplaceminusone).
  - `blog-ghaw-weekly-2026-06-01.md` Claim 12 (`api-consumption-report`:
    reporting/dashboard-style Agent of the Week that processed 95 runs and
    10,619 API calls in a single day, generating trend charts published as
    GitHub Discussions): Claim 6 here (`weekly-issue-summary`) is a second
    named instance of this reporting-agent category — issue-activity trends
    on a weekly 30-day rolling window, versus API-consumption trends on a
    daily snapshot. Together the two notes establish "scheduled
    trend-reporting agent that generates charts from repository activity
    data" as a recurring Agent-of-the-Week category, not a one-off.
  - `blog-ghaw-agent-of-the-day-2026-05-29.md` Claim 8 (model right-sizing —
    choosing a smaller/faster model for bounded classification tasks — framed
    as a design-time decision): Claim 7 here describes model right-sizing
    triggered reactively by a post-run observability report's note about
    "execution profile," rather than decided at workflow design time. This is
    a new instance of the right-sizing principle applied at a different point
    in the workflow lifecycle (post-hoc, feedback-driven vs. upfront,
    design-driven).
  - `blog-ghaw-weekly-2026-06-15.md` Claim 13 (`aw-failure-investigator`
    filed an issue after detecting the Daily Model Inventory Checker broken
    for six days due to 60-second timeout exhaustion): both that note and
    Claim 7 here describe an observability/monitoring layer surfacing a
    scheduled workflow's operational problem (a timeout, an oversized
    execution profile) as actionable feedback; `aw-failure-investigator`
    files an issue, while the mechanism that flagged `weekly-issue-summary`'s
    June 15th run is only described as "the observability report," not
    attributed to a named investigator agent.

- **Contradicts**: None identified at the MINER.md §4a filing threshold. The
  "~28%" figure in Claim 3 does not arithmetically match a straightforward
  computation from the two character counts printed alongside it (27,299 →
  11,876 is a ~56.5% reduction in absolute terms, or the result is ~43.5% of
  the original), but this is an internal inconsistency in a single passage of
  one source — not a claim that opposes an existing source note or a chapter
  position — so no contradiction issue was filed. See Claim 3 and Extraction
  Notes.

- **Novel**:
  - **Plateaued "agent effectiveness score" as a named, multi-week metric
    triggering a shared prompt-quality-rubric intervention** (Claim 4): No
    existing corpus note documents a numeric effectiveness-score plateau
    (61–62, "several weeks") as the diagnostic trigger for introducing a
    prompt quality rubric shared across a *category* of workflows
    (analyzer + reviewer) rather than a single workflow.
  - **Ambient-context reduction via gating cold-start rebuild content behind
    an optional import** (Claim 3): the first time this corpus names a
    specific code-level mechanism (conditional/lazy import) for an
    ambient-context payload reduction, rather than describing the reduction
    only as an outcome.
  - **Observability-triggered (post-hoc) model right-sizing recommendation**
    (Claim 7): the first corpus source describing an automated observability
    report recommending a smaller model based on a completed run's measured
    "execution profile," as distinct from the design-time right-sizing
    decision documented in `blog-ghaw-agent-of-the-day-2026-05-29.md`.
  - **`internal/astutil` as a shared AST/context-helper package for the
    custom Go linter suite** (Claim 2): not previously named in the corpus;
    extends but is distinct from the analyzer-registry growth pattern in
    `blog-ghaw-custom-linters-three-workflow-loop.md`.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add "gate rarely-needed ambient-context content behind an optional/lazy
    import" (Claim 3, PR #43619) as a concrete, named technique in the
    ambient-context cost-reduction playbook, alongside the June 15
    (`blog-ghaw-weekly-2026-06-15.md` Claim 12) and June 22
    (`blog-ghaw-weekly-2026-06-22.md` Claim 5) entries which describe outcomes
    without naming a mechanism. Cross-reference `docs-ghaw-audit-reference.md`
    Claim 4's `ambient_context` metric as the detection signal.
  - Add "auto-wire job dependencies when a template references another job's
    outputs" (Claim 1, PR #43570) as a concrete correctness pattern for any
    workflow/code compiler that assembles job graphs from templated
    expressions — the class of bug (referencing `needs.<job>.outputs.<x>`
    without declaring `<job>` as a dependency) generalizes beyond gh-aw to any
    GitHub Actions code generator.
  - Add shared-helper consolidation for growing static-analyzer suites
    (Claim 2, `internal/astutil`) as the maintenance counterpart to the
    invent/challenge/apply linter-registry-growth loop already documented in
    `blog-ghaw-custom-linters-three-workflow-loop.md`.

- **Chapter 03 (Agent Orchestration)**:
  - Add "plateaued effectiveness score → shared prompt quality rubric" (Claim
    4) as a named remediation pattern: when a family of related evaluation/
    review workflows shares a quality ceiling that persists over multiple
    weeks without crashing or erroring, a cross-workflow rubric is a more
    leveraged fix than independently tuning each workflow's prompt.

- **Chapter 06 (Agentic Operations)**:
  - Add `weekly-issue-summary` to the existing reporting/data-journalism
    agent category established by `api-consumption-report`
    (`blog-ghaw-weekly-2026-06-01.md` Claim 12) — do NOT present it as a new
    category; present it as the category's second documented instance, with
    a distinct cadence (weekly, 30-day rolling window vs. daily snapshot) and
    a cost data point (~59 AIC, 13 API calls per run) for teams estimating
    similar reporting-agent budgets.
  - Add "observability-triggered model right-sizing" (Claim 7) as a distinct
    sub-pattern of the design-time right-sizing principle in
    `blog-ghaw-agent-of-the-day-2026-05-29.md` Claim 8 — note that this
    post's account of the triggering incident is internally ambiguous (the
    "timeout" sentence and the "heavy execution profile" sentence may or may
    not describe the same run) and should be presented with that caveat
    rather than as a fully resolved case study.
  - Add the labeling-strategy usage tip (Claim 8) as a prerequisite note for
    any team deploying a category-segmented reporting agent: the value of
    category breakdowns depends on the consistency of the underlying labels,
    which the reporting agent itself does not create or enforce.

## Extraction Notes

1. **WebFetch output vs. raw HTML**: An initial WebFetch pass against the
   source URL returned a heavily condensed six-paragraph summary that
   dropped all PR numbers, exact character counts, and several direct
   quotes present in the actual page. All quotes, PR numbers, and figures in
   this note were instead verified against the page's raw HTML (fetched via
   `curl`), from which the article's full text was extracted and PR links
   were resolved by mapping each `<h3>` section heading to its nearest
   embedded PR link. The Miner recommends the Assayer spot-check the raw
   page directly rather than relying on a WebFetch summary for this source,
   since the WebFetch summary alone would have produced a substantially
   thinner and less verifiable note.

2. **PR numbers are link targets, not visible inline text**: Unlike the June
   22 and June 29 weekly updates (which print PR numbers as visible `#NNNNN`
   text in prose, e.g., "PR #42119 is a satisfying milestone"), this post's
   PR numbers (#43570, #43649, #43619, #43527, #43637) appear only as the
   `href` attribute of each section's heading anchor link, not as visible
   text anywhere on the rendered page. They were recovered by parsing the
   raw HTML and are independently resolvable GitHub PR URLs
   (`https://github.com/github/gh-aw/pull/<number>`), but a reader relying on
   the rendered page's visible text alone (or on a naive text-extraction
   WebFetch pass) would not see them. This is a real presentation difference
   from prior weeks' posts, not an extraction artifact on our part — flagging
   it in case the Assayer's spot-check of this source note's quotes
   initially "can't find" the PR numbers when skimming the rendered page.

3. **"~28%" figure does not match the printed character counts**: The
   source states the `copilot-agent-analysis` payload was "the largest
   ambient-context payload at 27,299 characters" and that the fix "trims the
   first-request size to 11,876 characters," describing this as a "~28%"
   change. 11,876 / 27,299 ≈ 0.435 (the new size is ~43.5% of the old size),
   and (27,299 − 11,876) / 27,299 ≈ 0.565 (a ~56.5% reduction) — neither
   reading produces "~28%." We did not attempt to guess which number the
   post intended or silently substitute a "corrected" percentage; Claim 3
   quotes the source's own "~28%" framing verbatim and flags the
   discrepancy in "Our assessment" and under Cross-References →
   Contradicts. This does not rise to a MINER.md §4a contradiction (it is
   not a claim disagreeing with another source or a chapter position — it is
   an apparent internal arithmetic inconsistency in a single blog post
   passage), so no contradiction issue was filed.

4. **Claim 7's "last three runs" vs. "June 15th failure" may or may not be
   the same incident**: We deliberately preserved this as flagged ambiguity
   rather than resolving it, per the instruction to quote verbatim and put
   only genuine synthesis in "Our assessment." See Claim 7.

5. **No sub-pages followed**: This is a single blog post page. It links to
   the five PRs and the `weekly-issue-summary` workflow definition file on
   GitHub; per MINER.md §1 we may follow up to 5 substantive linked pages,
   but PR pages and a single workflow markdown file on the gh-aw GitHub repo
   are primary-source artifacts referenced by, rather than sub-pages of, the
   blog post itself, and were not independently fetched and read in full for
   this note (their existence and URLs were confirmed via the raw HTML
   only). If deeper verification of PR-level implementation detail is
   needed, a follow-up source note against `weekly-issue-summary.md` itself
   (the workflow definition) could be filed separately.

6. **No contradictions filed**: Reviewed all cross-referenced source notes
   (`blog-ghaw-weekly-2026-06-01.md`, `blog-ghaw-weekly-2026-06-15.md`,
   `blog-ghaw-weekly-2026-06-22.md`, `blog-ghaw-weekly-2026-06-29.md`,
   `blog-ghaw-custom-linters-three-workflow-loop.md`,
   `blog-ghaw-agent-of-the-day-2026-05-29.md`, `docs-ghaw-compilation-process.md`,
   `docs-ghaw-audit-reference.md`, `blog-ghaw-ai-credits-migration.md`). No
   claim in this source materially opposes an existing source note's claim
   at the MINER.md §4a filing threshold. The one internal numeric
   inconsistency found (Claim 3's "~28%") is within this single source, not
   between sources, and does not meet the "disagrees with itself" bar in a
   way that would change guide advice either way — both readings (43.5% of
   original or 56.5% reduction) support the same qualitative claim (a
   substantial size reduction) — so no contradiction issue was filed; it is
   flagged here and in Claim 3 for transparency instead.
