---
source_url: https://github.github.com/gh-aw/blog/2026-08-26-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – August 26, 2026: The CLI Archivist"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-08-26
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: settled
issue: "#2996"
---

# Agent of the Day – August 26, 2026: The CLI Archivist

> Profiles the CLI Consistency Checker, a weekday-scheduled drift-detection
> agent that pre-collects `--help` output for 40+ `gh aw` CLI commands via a
> deterministic bash step, diffs it against a single documentation file, and
> files at most one consolidated issue per run — filed twice this week with
> zero false positives and same-day (or next-day) merged fixes. The live
> workflow source and its compiled lock file were fetched to fill in
> mechanism detail the blog post omits, surfacing a natural-language
> "friendly format" cron schedule string that appears to contradict an
> earlier corpus source's claim that no such short syntax exists for
> weekday-only schedules (see Cross-References → Contradicts).

## Source Context

- **Type**: blog-post (an "Agent of the Day" entry from the official GitHub
  Agentic Workflows blog, bylined "Copilot" — the same recurring gh-aw
  convention documented across this series, e.g.
  `blog-ghaw-agent-of-the-day-2026-08-25.md`. Distinct from the weekly
  changelog format; one agent profiled per post.)
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team. The post cites two specific,
  independently-checkable GitHub Actions run IDs (32924017960, 32974417489)
  and two specific issue numbers (#55788, #56047), both of which this note
  independently fetched and read in full (see Concrete Artifacts). This note
  additionally fetched the live workflow definition
  (`raw.githubusercontent.com/github/gh-aw/main/.github/workflows/cli-consistency-checker.md`)
  and its compiled companion lock file
  (`cli-consistency-checker.lock.yml`) — the blog post's own claims about
  cadence, deduplication, and reporting discipline are corroborated in detail
  by both, and the lock file additionally surfaces a scheduling mechanism not
  mentioned in the blog post at all (see Claim 3 and Cross-References →
  Contradicts).
- **Scope**: One short post (~350 words) describing the workflow's mission,
  daily audit method, and two specific runs' findings. Does NOT cover: the
  workflow's frontmatter configuration, permissions, safe-output
  deduplication settings, or issue labeling — all of which exist in the live
  workflow file but are unmentioned in the blog post's own text and were
  recovered by this note via direct source-file and issue/PR fetches.

## Extracted Claims

### Claim 1: The CLI Consistency Checker collects `--help` output for every one of the `gh aw` CLI's 40-plus top-level commands and subcommands each day and compares it against a single documentation file, hunting for typos, flag-naming inconsistencies, missing `--no-*` negation counterparts, undocumented commands, and stale examples

- **Evidence**: Direct description in the post's second section, "Agent of the
  Day: CLI Consistency Checker"; independently corroborated by the live
  workflow's own instructions and `pre-agent-steps` bash script, which
  programmatically walks every top-level command and subcommand via `--help`
  and writes each to a per-command file plus a combined `all-help.txt`.
- **Confidence**: settled (blog description directly confirmed by the fetched
  first-party workflow source)
- **Quote**: "Each day the workflow collects the full --help output for every
  one of the gh aw CLI's 40-plus top-level commands and subcommands, then
  lines it up against docs/src/content/docs/setup/cli.md looking for typos,
  flag-naming inconsistencies, missing --no-* negation counterparts,
  undocumented commands, and stale examples."
- **Our assessment**: This is a distinct agent archetype from the corpus's
  three prior audit/codemod examples: unlike Architecture Guardian's
  code-vs-code structural scan (`blog-ghaw-agent-of-the-day-2026-05-20.md`
  Claim 2) or the Dead Code Removal Agent's code-vs-tests verification
  (`blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 2), this agent's
  comparison target is CLI-behavior-vs-hand-written-prose — a genuinely
  different drift class (interface vs. documentation, not interface vs.
  interface). For Ch02 (Harness Engineering): add "CLI-vs-docs drift
  detection" as a named audit-agent subtype, distinct from code-quality
  audits and from the docs-drift starter covered in
  `docs-ghaw-docs-automation.md` (which reviews code *changes* against docs
  over a lookback window, not the full current CLI surface against docs on
  every run).

### Claim 2: Before the AI agent is invoked at all, a deterministic `pre-agent-steps` bash script builds the CLI from source and walks every top-level command's `--help` output, recursively discovering and capturing every subcommand's `--help` output too — failing the run outright if zero commands are parsed or the combined help file is empty

- **Evidence**: Live workflow source, `pre-agent-steps` block: builds the CLI
  (`make build`), runs `./gh-aw --help`, awk-parses the indented command list
  to discover top-level commands, then for each one runs `./gh-aw "$cmd"
  --help` and awk-parses *that* output for subcommands, running `--help`
  recursively for each. Two explicit `exit 1` guards fire if no top-level
  commands were parsed or if the concatenated `all-help.txt` ends up empty.
- **Confidence**: settled (directly read from the first-party workflow
  source's `pre-agent-steps` YAML block; not mentioned at all in the blog
  post's prose)
- **Quote**: (no direct quote from the blog post — the pre-agent data
  collection mechanism is not mentioned in the blog text at all; sourced from
  the live workflow file, cited by section name per MINER.md §4b:
  `pre-agent-steps` block, `.github/workflows/cli-consistency-checker.md`)
- **Our assessment**: This is a concrete, verifiable instance of the
  "deterministic data collection, then agent reasoning over authoritative
  pre-collected data" pattern — the workflow's own prompt reinforces this
  explicitly ("Use real CLI output as source of truth... treat this file as
  the authoritative source for CLI behavior"), which is a stronger and more
  specific instance of separating deterministic collection from agentic
  analysis than anything else currently in the corpus for an *audit* agent
  (the Dead Code Removal Agent's verification suite in
  `blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 6 runs *after* the agent
  edits, as a check; this workflow runs deterministic collection *before* the
  agent reasons at all, specifically to prevent the agent from hallucinating
  or paraphrasing CLI behavior it should instead read verbatim). For Ch02:
  name "pre-collect ground truth, then reason over it" as a harness pattern
  for any audit agent whose subject matter (CLI output, API responses, log
  data) is cheap to capture deterministically and expensive/unreliable for an
  LLM to reproduce from memory or partial tool calls.

### Claim 3: The workflow's schedule is written as a natural-language "friendly format" string, `cron: "daily around 13:00 on weekdays"`, which the gh-aw compiler resolves to the literal cron expression `5 13 * * 1-5` — not `0 13 * * 1-5` — indicating the compiler adds deliberate minute-level jitter ("scattered") rather than compiling to the naive on-the-hour equivalent

- **Evidence**: Live workflow source frontmatter: `cron: "daily around 13:00
  on weekdays"  # ~1 PM UTC, weekdays only (Mon-Fri)`. The compiled companion
  lock file (`cli-consistency-checker.lock.yml`, fetched from the same
  commit) resolves this to: `cron: "5 13 * * 1-5"  # Friendly format: daily
  around 13:00 on weekdays (scattered)`.
- **Confidence**: settled (both the uncompiled workflow source and its
  compiled lock-file output were fetched directly and read in full; the
  "(scattered)" annotation is the compiler's own generated comment, not an
  inference)
- **Quote**: (no direct quote from the blog post — the schedule syntax is not
  mentioned in the blog text at all; sourced from the live workflow file and
  its compiled lock file, cited by section name per MINER.md §4b: `on:` block
  of `.github/workflows/cli-consistency-checker.md`, and the `schedule:`
  block of the compiled `cli-consistency-checker.lock.yml`)
- **Our assessment**: This is the most consequential finding from
  cross-checking the live source against the rest of the corpus.
  `docs-ghaw-dailyops.md` Claim 2 documents the weekday-only cron pattern
  `0 2 * * 1-5` as "the standard DailyOps scheduling convention," with the
  source's own inline comment stating explicitly "(no short syntax
  available)" for weekday-only schedules. This workflow's frontmatter shows a
  natural-language alternative not only existing but running in gh-aw's own
  production repository, with the compiler demonstrably parsing it into a
  real cron expression — one that also applies undocumented (in
  `docs-ghaw-dailyops.md`) minute-level scattering, presumably to avoid many
  scheduled workflows firing on the exact same minute across a large fleet.
  This directly contradicts, however, `docs-ghaw-dailyops.md` Claim 2's "no
  short syntax available" statement. See Cross-References → Contradicts;
  filed as contradiction issue #3043. For Ch02: once #3043 is resolved,
  document the "friendly format" natural-language cron syntax (with its
  compiler-applied scattering) as the recommended default for weekday-cadence
  workflows in place of hand-written raw cron strings — but do not present
  this as settled guide content until the contradiction is resolved, since
  the two corpus sources currently disagree about whether this syntax exists
  at all.

### Claim 4: On a finding, the workflow must consolidate every issue found into exactly one GitHub issue per run (not one issue per finding), with a required structure of severity breakdown, grouped findings by category, and per-finding affected commands/exact-quoted-output/expected-vs-actual/suggested-fix/priority — and the resulting issue is configured to auto-expire after 2 days and carries a "cookie" label alongside `automation`, `cli`, and `documentation`

- **Evidence**: Live workflow source, `safe-outputs.create-issue` block
  (`expires: 2d`, `title-prefix: "[cli-consistency] "`, `labels: [automation,
  cli, documentation, cookie]`, `max: 1`) and the "Step 3: Report Findings"
  prompt section, which explicitly instructs "Create one consolidated issue"
  with a mandated body structure.
- **Confidence**: settled (directly read from the first-party workflow
  source's `safe-outputs` frontmatter and prompt body; not mentioned in the
  blog post, which describes the reporting discipline qualitatively but not
  the specific `expires`/label/consolidation mechanics)
- **Quote**: (no direct quote from the blog post for the consolidation and
  expiration mechanics — the blog post never states `max: 1`, `expires: 2d`,
  or the `cookie` label; sourced from the live workflow file, cited by
  section name per MINER.md §4b: `safe-outputs` frontmatter block and "Step
  3: Report Findings" section of `.github/workflows/cli-consistency-checker.md`)
- **Our assessment**: The `expires: 2d` setting is a direct, concrete
  application of the `docs-ghaw-ephemerals.md` Claim 3 pattern (auto-closing
  safe outputs after a configured window) to an audit-agent's findings issue
  — a corroboration, not new ground, but a good worked example of
  auto-expiry applied specifically to audit findings rather than periodic
  reports. The `cookie` label is the more interesting finding: it is the
  *exact* label that `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 7
  documents as the required pre-filter for Issue Monster's candidate pool
  ("Only open issues with 'cookie' label (indicating approved work queue
  items from automated workflows)"). This means the CLI Consistency
  Checker's own issues are not merely informational — they are pre-approved,
  by construction, to enter Issue Monster's dispatch queue the moment they're
  created. This is a concrete, verifiable instance of one audit agent's
  output becoming another dispatcher agent's input via a shared label
  convention, without any explicit hand-off code connecting the two
  workflows. For Ch02/Ch09 (Multi-Agent Coordination): document
  "label-as-queue-contract" as a named pattern — independently-authored
  agents can compose into a pipeline purely by agreeing on a label's meaning,
  with no direct workflow-to-workflow dependency. Confirmed directly: issue
  #55788 (opened by this workflow) carries the `cookie` label alongside
  `documentation`, `automation`, and `cli`.

### Claim 5: One consolidated issue per run, with an explicit instruction not to create any issue when the audit finds nothing — the workflow's evals check for "issue created OR noop", treating a clean run as a valid, equally-monitored outcome

- **Evidence**: Live workflow source, "Step 4: End-of-Run Summary" ("If no
  issues are found, state that clearly but DO NOT create any issues. Only
  create an issue when actual problems are identified.") and the `evals`
  block's `issue_created_or_noop` question ("Was an issue created with
  specific CLI inconsistencies found, or was noop used when no issues were
  detected?").
- **Confidence**: settled (directly read from the first-party workflow
  source's prompt body and `evals` frontmatter; not mentioned in the blog
  post)
- **Quote**: "If no issues are found, state that clearly but DO NOT create
  any issues. Only create an issue when actual problems are identified."
  (workflow source, "Step 4: End-of-Run Summary")
- **Our assessment**: This is a restraint mechanism functionally identical in
  intent to Architecture Guardian's read-only skip-when-idle posture
  (`blog-ghaw-agent-of-the-day-2026-05-20.md` Claim 6), but implemented
  differently: Architecture Guardian calls an explicit `safeoutputs.noop`
  tool with a human-readable message (Claim 4 of that note); this workflow
  instead relies on a natural-language prompt instruction ("DO NOT create any
  issues") backed by an `evals` grading question that checks for the
  disjunction "issue created OR noop" as the success condition, without the
  post or the source confirming which specific mechanism (an explicit noop
  call vs. simply producing no safe-output) fires on a clean run. This is a
  real, if minor, gap in mechanism clarity relative to the Architecture
  Guardian note — worth flagging rather than assuming parity. For Ch03
  (Safety and Verification): note that "evals check the *outcome* (issue-or-noop),
  not the *mechanism*" is a looser but still auditable form of the restraint
  pattern; teams adopting this style should confirm whether their own
  `evals` framework can distinguish "no issue because nothing was wrong" from
  "no issue because the agent silently failed," since this source doesn't
  resolve that ambiguity for its own workflow.

### Claim 6: Two consecutive weekday runs (August 25 and 26, 2026) each surfaced exactly one confirmed, low-or-medium-severity finding — a completely undocumented `graders` command, and a cosmetic double-blank-line formatting bug affecting seven commands — and both were fixed and merged the same day or next day, with the reporting issue itself documenting explicit root-cause line numbers in the Go source

- **Evidence**: This note independently fetched and read issue #55788, PR
  #55794, issue #56047, and PR #56052 in full (not just the blog post's
  summary). Issue #55788 (created 2026-08-25T13:36:14Z, closed
  2026-08-25T16:16:02Z, ~2h40m) reports the `graders` command and its
  `operational-value` subcommand as completely absent from
  `docs/src/content/docs/setup/cli.md`, with a "severity breakdown: 1
  medium, 0 high, 0 low" and an explicit "Other areas checked (no issues
  found)" section listing every category scanned without incident. PR #55794
  fixed it by adding an 11-line documentation section and extending
  `pkg/cli/cli_consistency_help_test.go`. Issue #56047 (created
  2026-08-26T13:42:02Z, closed 2026-08-26T14:11:32Z, ~29 minutes) reports
  seven commands (`add`, `add-wizard`, `logs`, `trial`, `mcp add`, `mcp
  list`, `mcp inspect`) rendering two blank lines instead of one before their
  `Flags:` section, root-caused to a trailing newline before the closing
  backtick in each command's Go `Example:` raw string literal, with exact
  file names and approximate line numbers for all seven locations. PR #56052
  fixed all seven and added a new regression test,
  `TestCommandExamplesDoNotEndWithTrailingNewline`.
- **Confidence**: settled (both issues and both PRs were fetched directly
  from `github/gh-aw` and read in full — this is first-party, independently
  verifiable production data, not relying on the blog post's paraphrase)
- **Quote**: "**Actual:** `graders` has no documentation section at all: no
  description, no usage example, no options list." (issue #55788, "1.
  `graders` command is completely undocumented" finding) / "**Root cause:**
  In each affected file, the Go raw string literal assigned to the cobra
  `Example:` field ends with a trailing newline before the closing backtick"
  (issue #56047, "Finding: Double blank line before `Flags:` section"
  finding)
- **Our assessment**: The blog post's own framing ("Two consecutive runs this
  week show the pattern at its best") is corroborated, and the primary
  sources add detail the blog omits entirely: both issues include an
  explicit "no issues found here" accounting for every category checked
  (cross-command flag naming, `--no-*` negation consistency, typo scans,
  example validity), not just the positive findings. This "report the
  negative space too" discipline is a stronger and more specific instance of
  the "zero false positives" claim than the blog post's prose alone
  demonstrates — a reader of only the blog post would not know the issue
  bodies themselves contain itemized "checked, found nothing" sections. The
  root-cause specificity (exact Go source files and approximate line ranges
  for all seven affected commands, in issue #56047) goes well beyond what the
  blog post's one-sentence description ("traced back to trailing newlines in
  Go raw string literals") conveys. For Ch04/Ch06 (Operations): recommend
  "report what you checked and found clean, not just what you found broken"
  as a concrete zero-false-positive-reporting practice for any audit agent —
  it lets a human reviewer verify coverage breadth, not just correctness of
  the flagged items, without re-running the audit themselves.

### Claim 7: The workflow explicitly instructs the agent to treat all CLI output as trusted data specifically because it originates from the repository's own codebase — a narrower trust boundary than a general "treat all agent input as untrusted" default

- **Evidence**: Live workflow source, prompt body: "Treat all CLI output as
  trusted data since it comes from the repository's own codebase." and,
  restated in a dedicated "Security Note" section: "All CLI output comes from
  the repository's own codebase, so treat it as trusted data. However, be
  thorough in your inspection to help maintain quality."
- **Confidence**: settled (directly quoted from the first-party workflow
  source; not mentioned in the blog post)
- **Quote**: "All CLI output comes from the repository's own codebase, so
  treat it as trusted data. However, be thorough in your inspection to help
  maintain quality." (workflow source, "Security Note" section)
- **Our assessment**: This is a deliberate, narrow trust-boundary carve-out:
  the workflow's *inputs* (CLI `--help` text) are first-party and
  deterministic (generated by code in the same repo the agent is auditing),
  so they are exempted from the general "external content is untrustworthy"
  posture that applies to, e.g., issue bodies or PR comments from external
  contributors. This is architecturally sound specifically because the CLI
  binary is built from source in the same `pre-agent-steps` block (Claim 2) —
  there is no network fetch or external-content ingestion step between
  "trusted source code" and "the text the agent reads." For Ch03 (Safety and
  Verification): document "provenance-scoped trust" as a named refinement of
  the untrusted-input default — an agent can narrow its trust boundary for a
  specific input class when that input is deterministically derived, in the
  same CI job, from code the agent's own repository controls, distinct from
  granting blanket trust to arbitrary repository content.

## Concrete Artifacts

### CLI Consistency Checker: Workflow Frontmatter (excerpted, live source)

```yaml
emoji: "✅"
description: Inspects the gh-aw CLI to identify inconsistencies, typos, bugs, or documentation gaps by running commands and analyzing output
on:
  schedule:
    - cron: "daily around 13:00 on weekdays"  # ~1 PM UTC, weekdays only (Mon-Fri)
  workflow_dispatch:
max-daily-ai-credits: 10000
permissions:
  contents: read
  actions: read
  issues: read
  pull-requests: read
  copilot-requests: write
engine:
  id: copilot
  copilot-sdk: true
max-tool-denials: 3
strict: false
network:
  allowed: [defaults]
imports:
  - shared/otlp.md
  - shared/reporting.md
  - shared/graders.md
tools:
  bash:
    - "*"
safe-outputs:
  create-issue:
    expires: 2d
    title-prefix: "[cli-consistency] "
    labels: [automation, cli, documentation, cookie]
    max: 1
timeout-minutes: 20
features:
  gh-aw-detection: true
sandbox:
  agent:
    runtime: cloud-hypervisor
evals:
  - id: cli_inspected
    question: Did the agent inspect the gh-aw CLI commands and analyze their output for inconsistencies, typos, or documentation gaps?
  - id: issue_created_or_noop
    question: Was an issue created with specific CLI inconsistencies found, or was noop used when no issues were detected?
```

*Source: `.github/workflows/cli-consistency-checker.md`, fetched via `curl`
from `raw.githubusercontent.com/github/gh-aw/main/`, 2026-08-29.*

### CLI Consistency Checker: Compiled Schedule (lock file)

```yaml
schedule:
  - cron: "5 13 * * 1-5"  # Friendly format: daily around 13:00 on weekdays (scattered)
```

*Source: `.github/workflows/cli-consistency-checker.lock.yml`, fetched via
`curl` from `raw.githubusercontent.com/github/gh-aw/main/`, 2026-08-29 —
compiled output for the `cron: "daily around 13:00 on weekdays"` source
string above. See Claim 3 and Cross-References → Contradicts.*

### CLI Consistency Checker: Pre-Agent Data Collection Script (excerpted, live source)

```bash
# pre-agent-steps: "Build CLI and pre-collect help output"
cd /home/runner/work/gh-aw/gh-aw
make build

output_dir="/tmp/gh-aw/agent/help-output"
mkdir -p "${output_dir}"

./gh-aw --help > "${output_dir}/main.txt" 2>&1
mapfile -t top_commands < <(awk "${extract_commands}" "${output_dir}/main.txt" | sort -u)
if [ ${#top_commands[@]} -eq 0 ]; then
  echo "No top-level commands were parsed from ./gh-aw --help output" >&2
  exit 1
fi

for cmd in "${top_commands[@]}"; do
  if ! ./gh-aw "$cmd" --help > "${output_dir}/${cmd}.txt" 2>&1; then
    echo "warning: failed to collect help for '${cmd}'" >&2
    continue
  fi
  mapfile -t subcommands < <(awk "${extract_commands}" "${output_dir}/${cmd}.txt" | sort -u)
  for sub in "${subcommands[@]}"; do
    if ! ./gh-aw "$cmd" "$sub" --help > "${output_dir}/${cmd}-${sub}.txt" 2>&1; then
      echo "warning: failed to collect help for '${cmd} ${sub}'" >&2
    fi
  done
done

cat "${output_dir}"/*.txt > /tmp/gh-aw/agent/all-help.txt
if [ ! -s /tmp/gh-aw/agent/all-help.txt ]; then
  echo "Combined help output is empty" >&2
  exit 1
fi
```

*Source: `.github/workflows/cli-consistency-checker.md`, `pre-agent-steps`
block, fetched 2026-08-29. Abbreviated for length; full script includes an
awk extraction pattern for parsing indented command names from `--help`
output.*

### Run 32924017960 (Aug 25) — Issue #55788 Summary

```
Title:    [cli-consistency] CLI Consistency Issues - 2026-08-25
Opened:   2026-08-25T13:36:14Z
Closed:   2026-08-25T16:16:02Z  (~2h40m to merged fix)
Severity: 1 medium, 0 high, 0 low
Finding:  `gh aw graders` (and `graders operational-value` subcommand) is a
          real, functional command completely absent from
          docs/src/content/docs/setup/cli.md — grep for "graders" in that
          file returns 0 matches.
Coverage: Also checked and found clean — cross-command --repo/-r/--org/--repos
          flag naming; --no-* negation flags across 12 named commands; doc-vs-CLI
          flag lists for 13 named commands; typos/grammar/capitalization; example
          validity for 9 named commands.
Fix:      PR #55794, merged same day — added 11 lines to cli.md, extended
          pkg/cli/cli_consistency_help_test.go.
Labels:   documentation, automation, cli, cookie
```

*Source: github/gh-aw issue #55788 and PR #55794, fetched directly 2026-08-29.*

### Run 32974417489 (Aug 26) — Issue #56047 Summary

```
Title:    [cli-consistency] CLI Consistency Issues - 2026-08-26
Opened:   2026-08-26T13:42:02Z
Closed:   2026-08-26T14:11:32Z  (~29m to merged fix)
Severity: 1 low (affecting 7 commands/subcommands), 0 high, 0 medium
Finding:  7 commands (add, add-wizard, logs, trial, mcp add, mcp list,
          mcp inspect) render two blank lines before "Flags:" instead of one.
Root cause: trailing newline before the closing backtick in each command's
          Go `Example:` raw string literal (cobra usage template does not
          compensate for it).
Coverage: Also checked and found clean — all ~35 top-level/nested commands'
          documented **Options:** lists vs. actual Flags: sections; typo scan
          across full help text; --no-* negation naming across 6 named commands;
          specific flag cross-checks for forecast/checks/env get/env update.
Fix:      PR #56052, merged same day — removed trailing newlines in 6 Go files
          (logs_command.go needed no change), added
          TestCommandExamplesDoNotEndWithTrailingNewline regression test.
Labels:   documentation, automation, cli, cookie
```

*Source: github/gh-aw issue #56047 and PR #56052, fetched directly 2026-08-29.*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-agent-of-the-day-2026-05-20.md` Claim 6 (Architecture
    Guardian's read-only analysis posture — never auto-fixes, surfaces
    findings for human review) and `blog-ghaw-agent-of-the-day-2026-08-25.md`
    Claim 1 (curation as an archetype distinct from codemod agents): the CLI
    Consistency Checker is a third position in the read-only-audit family —
    like Architecture Guardian, it never edits code itself (`contents: read`
    only), but unlike Architecture Guardian's code-vs-code drift, its
    comparison target is CLI-behavior-vs-prose-documentation.
  - `docs-ghaw-ephemerals.md` Claim 3 (`expires:` config for auto-closing
    safe outputs): the `expires: 2d` setting on this workflow's
    `create-issue` safe output is a concrete, dated production example of
    that general pattern applied to audit findings specifically.
  - `blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 2 ("mechanical feedback
    loop" as an automation-fitness criterion — build/test give definitive
    pass/fail answers): CLI-help-output-vs-documentation-file comparison is
    another instance of an entirely mechanical, deterministically-checkable
    verification target, consistent with why this task is well-suited to
    unattended scheduled automation.
  - `docs-ghaw-docs-automation.md` Claim 1 (documentation automation defined
    as running an agent on a schedule to detect doc/code drift and propose a
    PR): this workflow shares the doc-drift detection goal but diverges
    sharply on remediation — `docs-updater` proposes fixes directly via
    `create-pull-request` (that note's Claim 5), while the CLI Consistency
    Checker only ever files a report issue (`create-issue`, no PR-creation
    permission or safe output configured at all) and leaves the fix to a
    separate human-or-agent PR. This is a conditioning-variable difference
    (docs-updater's target is prose it can safely rewrite; this workflow's
    target is a CLI/docs mismatch that may require either a docs fix or a
    CLI behavior fix, a judgment call better left to a human or a follow-up
    PR), not a contradiction.

- **Contradicts**:
  - `docs-ghaw-dailyops.md` Claim 2 (weekday-only cron scheduling requires
    hand-written raw cron syntax like `0 2 * * 1-5`, with the source's own
    inline comment stating "no short syntax available"). Claim 3 here shows
    a production gh-aw workflow using a natural-language "friendly format"
    schedule string (`"daily around 13:00 on weekdays"`) that the compiler
    resolves to a real, scattered cron expression. This is a genuine,
    unresolved contradiction about whether gh-aw's schedule syntax supports
    a non-raw-cron short form for weekday schedules — **filed as
    contradiction issue #3043**
    (`steveash/hitchhikers-guide-to-ai-native-engineering#3043`). No verdict
    is asserted in this note; see that issue and its eventual
    CONTRADICTIONS.md entry for resolution.
  - No other contradictions filed. Reviewed `CONTRADICTIONS.md` (no existing
    entries on gh-aw cron/schedule syntax prior to filing #3043) and the
    source notes cited throughout this note.

- **Extends**:
  - `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 7 (the "cookie" label as
    Issue Monster's required pre-filter for its candidate issue pool): Claim
    4 here shows the CLI Consistency Checker applying that exact label to
    its own findings issue at creation time, making it a concrete, verified
    producer into Issue Monster's consumption queue — the first time the
    corpus has traced a label-based hand-off between two independently
    profiled gh-aw agents end to end (confirmed on the live issue #55788,
    which carries the `cookie` label).
  - `docs-ghaw-ephemerals.md` Claim 3 (`expires:` on safe outputs): extends
    the abstract expiration-config documentation with a second dated,
    concrete production example (`expires: 2d` on an audit-findings issue),
    distinct from the discussion/PR examples already in that note.
  - `blog-ghaw-agent-of-the-day-2026-05-20.md` Claim 4 (`safeoutputs.noop`
    called with an explicit human-readable skip message as an auditability
    practice): Claim 5 here shows a related but less precisely specified
    restraint mechanism (a prompt instruction plus an `evals` question
    checking for "issue created OR noop"), without confirming whether an
    explicit noop call with a message is actually used on a clean run — a
    gap worth a follow-up source if one profiles a clean (no-finding) run of
    this specific workflow.

- **Novel**:
  - **Deterministic pre-agent CLI-surface capture as ground truth for an
    audit agent** (Claim 2): the `pre-agent-steps` bash script that builds
    the CLI from source and walks every command's `--help` output
    recursively, with explicit fail-fast guards, before the agent is invoked
    at all, is a level of pre-collection rigor not previously documented for
    an audit-class agent in the corpus.
  - **Natural-language "friendly format" cron scheduling with
    compiler-applied jitter** (Claim 3): first corpus documentation of this
    gh-aw scheduling syntax — currently in tension with an earlier corpus
    source describing no such syntax as available; see Contradicts.
  - **Label-as-queue-contract composition between two independently profiled
    agents** (Claim 4): the CLI Consistency Checker and Issue Monster
    connect purely through the shared `cookie` label, with no direct
    workflow dependency — a composition pattern not previously named in the
    corpus.
  - **"Report the negative space" as a concrete zero-false-positive
    reporting practice** (Claim 6): both fetched issues include itemized
    "checked, found nothing" sections alongside their positive findings — a
    specific reporting discipline beyond what "zero false positives" alone
    conveys, not previously documented with this level of concreteness.
  - **Provenance-scoped trust for deterministically-derived, same-job input**
    (Claim 7): the explicit "trust this specific input class because it's
    built from source in this same job" carve-out is a more precise
    trust-boundary articulation than the corpus's general
    untrusted-external-input guidance.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add "CLI-vs-docs drift detection" as
  a named audit-agent subtype (Claim 1), distinct from code-vs-code
  structural audits (Architecture Guardian) and from doc-vs-recent-code-change
  review (`docs-ghaw-docs-automation.md`'s `docs-updater`). Add "pre-collect
  ground truth, then reason over it" (Claim 2) as a harness pattern for any
  audit agent whose subject matter is cheap to capture deterministically —
  include the fail-fast guard pattern (`exit 1` if zero commands parsed or
  combined output is empty) as a concrete implementation detail worth citing.
  Once contradiction #3043 resolves, update the DailyOps scheduling section
  to reflect whether the "friendly format" cron syntax (Claim 3) is the
  current recommended default over raw cron strings.

- **Chapter 03 (Safety and Verification)**: Add "provenance-scoped trust"
  (Claim 7) as a named refinement of the untrusted-input default — an agent
  may narrow its trust boundary for a specific input class (here, CLI output
  built from source in the same job) without adopting blanket trust for all
  repository content. Flag the restraint-mechanism ambiguity in Claim 5
  (evals check outcome, not mechanism) as a caution for teams relying on
  `evals` alone to distinguish "clean run" from "silent failure."

- **Chapter 04 / Chapter 09 (Operations / Multi-Agent Coordination)**: Add
  "label-as-queue-contract" (Claim 4) as a named composition pattern —
  independently-authored scheduled agents can form a pipeline by agreeing on
  a shared label's meaning, with the producer (CLI Consistency Checker)
  never calling or even being aware of the consumer (Issue Monster). Add
  "report the negative space" (Claim 6) as a concrete zero-false-positive
  reporting practice: itemize what was checked and found clean, not just
  what was flagged, so a human reviewer can verify audit coverage without
  re-running it.

## Extraction Notes

1. **Blog post is short and thin; primary depth came from four fetched
   sub-pages**, within MINER.md §1's "up to 5" budget: the live workflow
   source (`cli-consistency-checker.md`), its compiled lock file
   (`cli-consistency-checker.lock.yml`), issue #55788 + PR #55794 (fetched as
   a pair via `gh issue view` / `gh pr view`), and issue #56047 + PR #56052
   (same). That is 5 distinct fetches (workflow source, lock file, and two
   issue/PR pairs each counted as reading one linked page's full content).
   All Claims 2–7 and all Concrete Artifacts beyond the two run summaries
   rely on this sub-page material — none of it is present in the blog post's
   own ~350 words. The blog post's text alone would have supported at most
   Claim 1 and a thin version of Claim 6.

2. **WebFetch summary used only as a first-pass orientation, not for
   quotes**: an initial WebFetch call against the blog URL returned a
   structured, paraphrased summary (it renamed the featured commands
   inaccurately in places, e.g. compressing the two distinct findings into
   generic descriptions). Per MINER.md §2a, the page was re-fetched directly
   via `curl` and parsed with a Python regex-based tag-stripping pass (same
   approach as `blog-ghaw-weekly-2026-08-24.md` Extraction Note 1;
   BeautifulSoup was not used). All blog-post quotes above are copied
   character-for-character from that raw-HTML extraction pass.

3. **Contradiction filed before writing this note, per MINER.md §4a**: the
   cron-syntax conflict with `docs-ghaw-dailyops.md` Claim 2 is filed as
   `steveash/hitchhikers-guide-to-ai-native-engineering#3043`. No verdict is
   asserted here; Claim 3 and the Guide Impact section both explicitly defer
   to that issue's resolution. The filer's recommended verdict on that issue
   is "superseded" (a later-added compiler feature), but this is a
   recommendation for the human resolver, not a claim in this note.

4. **Cross-reference check performed** against
   `blog-ghaw-agent-of-the-day-2026-05-20.md`,
   `blog-ghaw-agent-of-the-day-2026-05-28.md`,
   `blog-ghaw-agent-of-the-day-2026-08-25.md`, `blog-ghaw-issue-pr-mgmt.md`,
   `docs-ghaw-docs-automation.md`, `docs-ghaw-dailyops.md`,
   `docs-ghaw-ephemerals.md`, `docs-ghaw-frontmatter-full-reference.md`, and
   `CONTRADICTIONS.md`, all read in full (not skimmed) before writing
   Cross-References. All `Claim N` citations above were checked against the
   actual numbered claims in those notes at the time of writing, per MINER.md
   §4b.

5. **No engine-choice or cost data in this note**: unlike some prior
   "Agent of the Day" profiles, neither the blog post nor the fetched
   workflow source states token usage, runtime, or GitHub Actions minutes for
   either of the two profiled runs (`max-daily-ai-credits: 10000` is a cap,
   not an actual-usage figure). This is a gap relative to, e.g.,
   `blog-ghaw-agent-of-the-day-2026-05-28.md`'s Run #100 profile, which does
   report duration and token counts — flagged here rather than fabricated.
