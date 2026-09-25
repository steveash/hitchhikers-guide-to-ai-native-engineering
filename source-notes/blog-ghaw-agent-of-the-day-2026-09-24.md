---
source_url: https://github.github.com/gh-aw/blog/2026-09-24-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – September 24, 2026: Dependabot Burner"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-09-24
date_extracted: 2026-09-25
last_checked: 2026-09-25
status: current
confidence_overall: settled
issue: "#3694"
---

# Agent of the Day – September 24, 2026: Dependabot Burner

> An "Agent of the Day" profile of Dependabot Burner, a scheduled workflow
> that groups scattered Dependabot manifest-bump PRs into one source-first
> replacement PR — first coverage of this workflow in the corpus. The
> ~450-word blog post was substantially extended by fetching the live
> workflow source (`.github/workflows/dependabot-burner.md`), the PR that
> created its current architecture (`github/gh-aw#40396`), and the complete
> first-party GitHub Actions artifacts (run logs, `context.json`,
> `evals.jsonl`, `safe-output-items.jsonl`, `agent_output.json`) for the
> exact run the blog cites as its "successful" example
> (`github/gh-aw/actions/runs/33845039019`) — which together show the
> blog's central claim about that run (that it "walk[ed] through candidate
> PRs, grouping the applicable ones, and fir[ed] off its replacement pull
> request") is contradicted by the run's own first-party data: zero open
> Dependabot PRs existed for it to process, it emitted zero safe outputs,
> and it ended in an explicit "Blocked" no-op, not a merged PR.

## Source Context

- **Type**: blog-post (an "Agent of the Day" entry from the official GitHub
  Agentic Workflows blog, bylined "Copilot" — same recurring convention as
  the rest of this series, e.g. `blog-ghaw-agent-of-the-day-2026-09-23.md`
  and `blog-ghaw-agent-of-the-day-2026-09-15.md`).
- **Author credibility**: Official gh-aw platform team blog, auto-published
  by a scheduled `[blog] Agent of the Day` workflow (confirmed via
  `github/gh-aw` PR #63194, authored by `app/github-actions`, merged
  2026-09-24). The post cites two independently-checkable first-party
  artifacts — `github/gh-aw#40396` and Actions run `33845039019` — both
  fetched directly and read in full by this note (see Concrete Artifacts).
- **Scope**: One short post (~450 words) describing the workflow's mission,
  one cited "successful" run, and two cited failed runs. Does NOT cover:
  the workflow's five-subagent internal architecture, its retry-aware
  maintainer-feedback loop, its slash-command entrypoint, or (most
  importantly) the fact that its own cited "successful" run processed zero
  candidate PRs and produced no safe output at all — none of which appear
  in the blog post's own text and were recovered by this note via direct
  fetches of the live workflow source and the run's first-party artifacts.

## Extracted Claims

### Claim 1: Dependabot Burner's mission is to collapse scattered Dependabot PRs against generated workflow manifests into one source-first replacement PR, by tracing each PR back to the workflow markdown that generates the manifest, updating that source, recompiling, and opening a single PR
- **Evidence**: Blog post's second paragraph; independently confirmed by the
  live workflow source's `description` field
  (`.github/workflows/dependabot-burner.md`, fetched via `curl` from
  `raw.githubusercontent.com/github/gh-aw/main/`) and by the workflow's own
  `## Operating model` prompt section, which restates the same
  trace-source→update→recompile→one-PR sequence as agent instructions.
- **Confidence**: settled (blog narrative directly corroborated by the live
  workflow's frontmatter `description` and prompt body, both fetched fresh)
- **Quote**: "Dependabot Burner runs on a weekly schedule (with manual
  dispatch and a `/dependabot-burner` slash command as backups) and does one
  job: collect the grouped Dependabot PRs targeting generated workflow
  manifests, trace them back to their source workflow markdown, apply the
  equivalent update there, recompile, and open a single replacement pull
  request." (blog post) / "description: Runs one grouped Dependabot
  remediation wave from schedule, manual dispatch, or /dependabot-burner on
  pull requests" (live workflow source frontmatter)
- **Our assessment**: This is the same source-first update discipline
  documented for the `--dependabot` compiler flag in `docs-ghaw-dependabot.md`
  Claim 7/8 ("never merge Dependabot PRs that only modify manifest files";
  the four-step source-first response procedure) and for `./gh-aw compile
  --dependabot`'s all-workflows constraint (`docs-ghaw-dependabot.md` Claim
  5) — Dependabot Burner is the first corpus source describing an *agent*
  that automates that exact human procedure end-to-end, rather than
  documenting the procedure for a human to follow manually.

### Claim 2: The workflow's safety design constrains a wide-blast-radius task (touching many files across the repo) to a narrow set of writes: read-only default GitHub permissions plus exactly one safe-output type, `create-pull-request`, gated through a fixed bash-command allowlist rather than open shell access
- **Evidence**: Blog post states read-only default access and
  `create_pull_request`-only writes. The live workflow source's frontmatter
  confirms `permissions: {contents: read, issues: read, pull-requests:
  read}` and a `safe-outputs:` block importing `shared/daily-pr-base.md`
  (which itself only exposes `create-pull-request` and `noop`). The `tools:`
  block sets `edit:` (present, no value) but pairs it with a `bash:` field
  that is not `["*"]` — it is an exact list of seven fixed command strings
  (`make dependabot && make build`, `./gh-aw compile --dependabot`, `cd
  .github/workflows && npm install --package-lock-only`, `git status`, `git
  diff -- .github/workflows`, two `cat`/`rg` inspection commands).
- **Confidence**: settled (directly read from the first-party workflow
  source frontmatter, fetched fresh)
- **Quote**: "It's a `gpt-5.4-mini` Copilot CLI run with read-only GitHub
  access by default — it only writes through the `create_pull_request` safe
  output, keeping its blast radius small even though its job is to touch a
  lot of files." (blog post) / `tools: {edit:, cli-proxy: true, github:
  {mode: local, toolsets: [default, pull_requests]}, bash: ["make dependabot
  && make build", "./gh-aw compile --dependabot", "cd .github/workflows &&
  npm install --package-lock-only", "git status", "git diff --
  .github/workflows", "cat /tmp/gh-aw/agent/dependabot-burner/context.json",
  "cat .github/workflows/*.md", "cat .github/workflows/shared/*", "rg
  .github/workflows"]}` (live workflow source frontmatter)
- **Our assessment**: This is a stricter blast-radius design than the
  bare `bash: ["*"]` list-form seen in a different gh-aw workflow
  (`blog-ghaw-agent-of-the-day-2026-09-23.md` Cross-References → Extends
  bullet on ESLint Refiner — Daily Caveman Optimizer's `edit:` + unrestricted `bash: ["*"]`
  combination) — Dependabot Burner instead pins `bash:` to the exact
  literal command strings the remediation needs (compile, install, git
  status/diff, cat/rg for reading), so even with `edit:` enabled the agent
  cannot run arbitrary shell commands, only the named validation and
  inspection commands plus file edits via the `edit:` tool. For Ch02: name
  this "exact-string bash allowlist" as a narrower alternative to
  `bash: ["*"]`/`bash: {allow: [...]}` wildcard forms when a workflow's
  required shell operations are fully enumerable in advance.

### Claim 3: The workflow's remediation logic is decomposed into five named subagents (`pr-group-analyzer`, `retry-history-analyzer`, `dependency-batch-analyzer`, `retry-feedback-synthesizer`, `dependabot-remediator`) run in a fixed sequence by a top-level orchestrator prompt, with the actual file edits and PR creation confined to exactly one of them
- **Evidence**: Live workflow source's `## Required behavior` section lists
  the five subagent invocations in numbered order; each subagent is defined
  inline in the same file (`## agent: <name>` sections) with its own
  `description`, `model`, and scoped instructions. None of this
  subagent decomposition is mentioned in the blog post.
- **Confidence**: settled (directly read from the first-party workflow
  source, which defines all five subagents inline; not present in the blog
  post at all)
- **Quote**: "1. Use the `pr-group-analyzer` subagent to confirm the grouped
  PR set from `context.json`... 2. Use the `retry-history-analyzer`
  subagent... 5. Use the `dependency-batch-analyzer` subagent... 6. Use the
  `retry-feedback-synthesizer` subagent... 7. Use the `dependabot-remediator`
  subagent exactly once for the single remediation wave." (live workflow
  source, "Required behavior")
- **Our assessment**: The orchestrator/subagent split here is single-workflow
  and single-repo — distinct from the cross-repo orchestrator/worker
  CentralRepoOps pattern in `docs-ghaw-dependabot-rollout.md` (which
  dispatches separate `workflow_dispatch` worker runs via `dispatch-workflow`
  across up to 100 target repos). Dependabot Burner instead uses gh-aw's
  inline sub-agent mechanism to decompose *one* run into scoped reasoning
  stages (confirm grouping → derive retry strategy → summarize dependency
  batch → synthesize constraints → execute the one bounded edit), all within
  a single workflow invocation. This is a second, distinct multi-agent
  decomposition pattern gh-aw supports beyond CentralRepoOps: in-run
  subagent staging vs. cross-run worker dispatch. Cross-reference
  `docs-ghaw-inline-sub-agents.md` for the underlying mechanism (not
  separately verified by this note; flagged as an open cross-check).

### Claim 4: The `dependabot-remediator` subagent is required to write a deterministic result JSON file on every wave — including blocked or no-op waves — recording a `status` of `improved`, `unchanged`, or `blocked`, and the PR-creation rule requires `status: improved` plus a passing validation run before any PR may be opened
- **Evidence**: Live workflow source's `dependabot-remediator` agent
  definition, "Deterministic result" and "Pull request rule" sections.
- **Confidence**: settled (directly read from the first-party workflow
  source; not present in the blog post)
- **Quote**: "Always write one result JSON file for this wave, even if the
  work is blocked or no change is applied." / "Create a PR only if: the fix
  is real and bounded; validation passed; `git diff --stat` shows an actual
  code change; the result JSON would report `status: improved`." (live
  workflow source, `dependabot-remediator` agent definition)
- **Our assessment**: This is a concrete instance of the "always emit a
  structured self-report, even for the null case" discipline documented
  elsewhere in the corpus for `noop` safe outputs
  (`docs-ghaw-audit-with-agents.md` Claim 6) and no-op run reporting
  (`docs-ghaw-monitoring-patterns.md` Claim 6) — but applied one layer
  lower, to an *inline subagent's* own self-report file rather than to the
  workflow-level safe-output signal. The PR-gate condition (`status:
  improved` AND validation passed AND a real diff) is a three-part
  conjunctive guard against the single most likely failure mode for an
  agent whose job is "touch a lot of files": opening a PR that looks
  plausible but didn't actually validate. For Ch02/Ch03: document this
  three-part PR-creation gate as a transferable pattern for any
  remediation-style agent whose blast radius is "many files, one output PR."

### Claim 5: PR #40396 replaced two separate workflows (`dependabot-campaign`, `dependabot-worker`, together ~3,500 lines removed) with a single `dependabot-burner` workflow, adding a centralized `/dependabot-burner` slash command and a retry-aware feedback loop that reuses signal from prior failed burner PRs and maintainer-only review comments
- **Evidence**: `gh pr view 40396 --repo github/gh-aw --json
  title,body,additions,deletions,changedFiles` — the PR body explicitly
  states the old workflows "have been removed" and lists "Retry-aware burner
  orchestration" and "Maintainer-only feedback loop" as named features;
  `changedFiles: 8` with `dependabot-campaign.lock.yml` (-1730),
  `dependabot-campaign.md` (-249), `dependabot-worker.lock.yml` (-1776), and
  `dependabot-worker.md` (-179) all deleted (`changeType: DELETED`).
- **Confidence**: settled (directly read from the first-party PR's metadata
  and body via `gh pr view`)
- **Quote**: "The old `dependabot-campaign` and `dependabot-worker` workflows
  have been removed — `dependabot-burner` is now the single workflow
  handling all Dependabot remediation." / "Scans recent closed unmerged
  `[dependabot-burner]` PRs and passes that history into the next attempt."
  / "Explicitly scopes retry guidance to maintainer/admin/write feedback and
  ignores non-maintainer noise." (PR #40396 body)
- **Our assessment**: The blog names PR #40396 as the workflow's origin but
  describes it only as adding "centralized grouping and retry-aware
  remediation" — it omits that this PR was a consolidation (two workflows
  → one) and omits the maintainer-only feedback filter entirely. The
  maintainer-only filter is itself a specific, transferable safety pattern:
  an autonomous retry loop that could otherwise be steered by any commenter
  (including other bots, or a compromised low-privilege account) is
  explicitly restricted to `admin`/`maintainer`/`write`-role feedback only —
  the same role list used by the workflow's own `on.roles:` gate
  (Concrete Artifacts). For Ch03 (Safety and Verification): document
  "scope autonomous retry guidance to the same role list that gates
  triggering the workflow at all" as a concrete anti-steering pattern for
  any agent that reads PR/issue comments to adjust its own retry behavior.

### Claim 6 (central finding): The blog's claim that run `#33845039019` (September 4) "completed successfully... walking through candidate PRs, grouping the applicable ones, and firing off its replacement pull request" is contradicted by that run's own first-party GitHub Actions artifacts: the run found zero open Dependabot PRs, produced zero safe outputs, and ended in an explicit blocked no-op — not a created PR
- **Evidence**: Four independent first-party artifacts fetched directly from
  `github/gh-aw`'s Actions API for run `33845039019`, all internally
  consistent with each other: (1) the agent's own precomputed context file
  `agent/dependabot-burner/context.json` (from the `agent` artifact,
  `gh api repos/github/gh-aw/actions/artifacts/9926324783/zip`) reads
  `"open_pr_count": 0, "selected_batch_pr_numbers": [], "selected_batch_dependencies": []`
  — there were no candidate Dependabot PRs for the run to process at all;
  (2) `evals.jsonl` (from the `evals` artifact) records both of the
  workflow's own evals as failed: `{"id":"dependabot_batch_analyzed",...,"answer":"NO"}`
  and `{"id":"remediation_reported",...,"answer":"NO"}`; (3)
  `safe-output-items.jsonl` (from the `safe-outputs-items` artifact) is an
  empty file — zero safe outputs of any kind were emitted, not even a
  `noop`; (4) `agent_output.json` reads `{"items":[],"errors":[]}`; and the
  agent's own final conversation turn, read from `gh run view 33845039019
  --repo github/gh-aw --log`'s "Copilot Execution Summary" section, states
  outright that nothing was remediated. The GitHub Actions run-level
  `conclusion` field is `"success"` (confirmed via `gh run view --json
  conclusion`) — the run did not error, it simply had nothing to do and
  correctly reported that, but the blog describes this exact run as if it
  had found and processed a batch of dependency PRs.
- **Confidence**: settled (four independently-fetched first-party artifacts
  for the exact run ID the blog names, all mutually consistent, directly
  contradicting the blog's narrative for that same run ID)
- **Quote**: "Digging into [run #33845039019 from September 4], the agent
  completed successfully in 27 turns and ~10 minutes, walking through
  candidate PRs, grouping the applicable ones, and firing off its
  replacement pull request." (blog post, verbatim from
  `docs/src/content/docs/blog/2026-09-24-agent-of-the-day.md`, fetched via
  `curl` from `raw.githubusercontent.com`) / "[4] ◆ No in-scope Dependabot
  PRs are selected, so I'm recording a no-op result and finishing without
  changes. ... [11] ◆ **Blocked:** no in-scope Dependabot PRs were selected,
  so there was nothing to remediate. ... Statistics: Turns: 11 Tools: 7/7
  succeeded Tokens: 170,925 total (170,397 in / 528 out)" (run 33845039019
  agent-job log, "Copilot Execution Summary" section, fetched via `gh run
  view --log`) / `{"objective":"Close grouped Dependabot PRs for generated
  workflow manifests by updating source workflow markdown and recompiling in
  one replacement PR.","trigger_event":"schedule","open_pr_count":0,"selected_batch_pr_numbers":[],"selected_batch_dependencies":[]}`
  (run 33845039019, `agent/dependabot-burner/context.json` artifact)
- **Our assessment**: This is a more severe instance of the "blog prose
  factually wrong about a specific, checkable detail" pattern already
  established twice in this corpus for this exact blog series
  (`blog-ghaw-agent-of-the-day-2026-09-23.md` Claim 5, a misattributed
  config field name, and that note's Extraction Note 2 citing a prior
  WebFetch-paraphrase error in `blog-ghaw-agent-of-the-day-2026-09-15.md`).
  Those two prior instances were narrow misattributions of a mechanism
  behind an otherwise-correctly-described behavior. Here, the blog's
  narrative substance for its single cited "successful" run — that
  candidate PRs existed, were grouped, and a replacement PR was fired off —
  is the opposite of what that run's own artifacts record: no candidates
  existed, nothing was grouped, and no PR (or any safe output at all) was
  produced. The turn count is also wrong in the same direction: the log's
  own "Statistics" line reports `Turns: 11`, not the 27 the blog states.
  Combined with Claim 7 below (no agent-authored Dependabot Burner output
  PR is findable anywhere in the repository's history), this raises a
  real possibility that the blog post's "27 turns... firing off its
  replacement pull request" sentence describes a hypothetical/typical run
  rather than the specific run ID it links to and names — but as written,
  the post presents it as a factual account of that exact, linked run.
  For Ch03 (Safety and Verification): this is a concrete argument for
  independently verifying any blog-cited "successful run" against the
  run's own first-party artifacts before using it as evidence in the guide
  — a first-party platform blog citing a real, linked run ID is not
  sufficient corroboration on its own.

### Claim 7: No PR carrying the labels the workflow's own safe-output configuration would apply to a real replacement PR (`automation`, `dependencies`, `dependabot` — from the `shared/daily-pr-base.md` import parameters) exists anywhere in `github/gh-aw`'s history, and no PR titled with the `[dependabot-burner] ` prefix appears in a full-history title search
- **Evidence**: `gh api search/issues -f q='repo:github/gh-aw is:pr
  label:dependabot label:automation label:dependencies'` returns
  `"total_count": 0`. A broader `gh pr list --search "dependabot-burner"
  --state all` (50-result page, plus a `search/issues` count of 375 total
  matches across all PRs that merely *mention* "dependabot-burner" anywhere)
  surfaces only human/`app/copilot-swe-agent` development PRs that modify
  the workflow's own source files (e.g., "Migrate agentic workflows to
  Cloud Hypervisor," "Enable evals on 20 more agentic workflows") — none is
  an agent-authored `[dependabot-burner] `-prefixed dependency-remediation
  output PR.
- **Confidence**: emerging (a search-based absence check — it is possible an
  output PR exists but is excluded from GitHub's search index, was deleted,
  or used a title/label combination other than the one configured in the
  live workflow source at the time of this check; the workflow's config has
  also likely changed over its ~8-month run history, so an older output PR
  could have used different labels)
- **Quote**: (search result, not prose from any source — see Evidence)
- **Our assessment**: This is corroborating, not conclusive, evidence for
  Claim 6's implication that this specific "Agent of the Day" workflow may
  rarely or never fire its core capability in production. Combined with
  Claim 6's direct verification that the one run the blog cites by name and
  link produced zero output, and with the run-history sample in Concrete
  Artifacts (Sept 4 and Sept 25 both "success" with — per this same
  no-op signature — likely nothing to do, Sept 11 and Sept 18 both
  driver-layer failures), this note did not find a single run in its
  sampled window with independent evidence of the workflow's headline
  capability (grouping N PRs into one replacement PR) actually firing. For
  Ch03: recommend that any "boring but valuable" scheduled remediation
  workflow publish its own historical success-rate (PRs actually created
  vs. runs executed) rather than relying on a single cited run as
  representative — this is exactly the kind of claim a reader cannot check
  without doing the archival work this note did.

### Claim 8: `driver_exit` (zero-turn failure) is a real, documented gh-aw platform classification — a failed run with `Turns == 0` — distinct from `agent_logic` failures (`Turns > 0`), and the two runs the blog cites as `driver_exit` failures (Sept 11, Sept 18) show harness-level retry exhaustion consistent with that classification
- **Evidence**: `docs/adr/47250-classify-driver-exit-vs-agent-logic-failures.md`
  (fetched via `curl` from `raw.githubusercontent.com/github/gh-aw/main/`)
  documents the exact classification rule and its implementation location
  (`isDriverExitFailure(run WorkflowRun) bool` in `pkg/cli/logs_models.go`).
  Independently, the full Actions logs for both cited runs (`34570607704`,
  Sept 11; `35315588170`, Sept 18; fetched via `gh run view --log`) show
  four consecutive `[copilot-harness] attempt N failed: exitCode=1
  failureClass=partial_execution` retries each, ending in "all 3 retries
  exhausted — giving up," with no "Statistics: Turns: N" line ever printed
  for either run (contrast with the Sept 4 run's `Turns: 11` line) —
  consistent with the harness never completing a countable turn before
  giving up.
- **Confidence**: settled for the classification rule's existence and exact
  definition (directly read from the first-party ADR); settled for the two
  cited runs matching the zero-turn signature (directly observed in both
  runs' full logs, which show no printed turn count and repeated harness-
  level `400 Bad Request` retry failures)
- **Quote**: "The classification rule is: a failed run with `Turns == 0` is
  a `driver_exit` failure; a failed run with `Turns > 0` is an `agent_logic`
  failure." (ADR-47250) / "[copilot-harness] attempt 4 failed: exitCode=1
  failureClass=partial_execution ... [copilot-harness] all 3 retries
  exhausted — giving up (exitCode=1)" (run 34570607704 agent-job log,
  2026-09-11)
- **Our assessment**: Unlike Claim 6, this part of the blog's narrative
  checks out against ground truth: the two failures really do show the
  signature the classification rule requires (no completed turn, harness-
  level exit). This makes the blog internally inconsistent in an
  instructive way — its account of a *failure* is verifiable and accurate,
  while its account of the cited *success* is not. The ADR's own
  "Consequences → Negative" section flags the same caveat this note
  observed independently: "a run that fails at the agent's very first
  action (before completing a turn) would still report `Turns == 0` and be
  misclassified as `driver_exit` even if the agent did begin executing" —
  the raw log's `failureClass=partial_execution` (not a bespoke
  `driver_exit` string) confirms the classification is a derived label
  applied post hoc from the turn count, not a distinct error type the
  harness itself emits. For Ch03/Ch04: document the `Turns == 0` heuristic
  and its known false-classification edge case (agent starts but fails
  before its first turn completes) as a caveat when citing `driver_exit`
  counts as a fleet-health signal.

### Claim 9: `threat_detection_job_failed` and `agentic_resource_heavy_for_domain` are real, stable, machine-readable audit finding codes defined in the `gh aw` CLI's audit engine, and `gh aw`'s audit comparison engine implements a real "baseline-cohort" run-matching mechanism (matching candidate baseline runs on `task_domain`, `execution_style`, `resource_profile`, or `actuation_style` before falling back to "latest successful run")
- **Evidence**: `pkg/cli/audit_finding_codes.go` (fetched via `curl` from
  `raw.githubusercontent.com/github/gh-aw/main/`) defines
  `AuditFindingDetectionJobFailed AuditFindingCode = "threat_detection_job_failed"`
  and `AuditFindingAgenticResourceHeavy AuditFindingCode =
  "agentic_resource_heavy_for_domain"` in a stable enum alongside
  `workflow_failed`, `many_iterations`, `mcp_server_failures`, and eight
  other named codes. `pkg/cli/audit_comparison.go` (same fetch method)
  implements a `Selection` field set to `"cohort_match"` when a candidate
  baseline run matches the current run on any of the four named dimensions,
  falling back to `"latest_success"` otherwise.
- **Confidence**: settled (both files are first-party Go source defining the
  exact code paths that would produce the terminology the blog uses;
  fetched directly)
- **Quote**: `AuditFindingDetectionJobFailed AuditFindingCode =
  "threat_detection_job_failed"` / `AuditFindingAgenticResourceHeavy
  AuditFindingCode = "agentic_resource_heavy_for_domain"` (both from
  `pkg/cli/audit_finding_codes.go`) / `candidate.Selection = "cohort_match"`
  ... `candidate.Selection = "latest_success"` (`pkg/cli/audit_comparison.go`)
- **Our assessment**: This corroborates that the blog is drawing on real
  platform terminology and real audit-engine mechanisms for its
  `threat_detection_job_failed` and "baseline-cohort matching" claims — the
  vocabulary is not invented. It does not, on its own, confirm that these
  specific finding codes actually fired for the specific runs the blog
  names: this note observed the raw GitHub Actions `detection` job
  conclusion as `"success"` for both the Sept 11 and Sept 18 runs (not a
  `failure` job conclusion), so the `threat_detection_job_failed` *audit
  finding* the blog describes is evidently a higher-level interpretation
  by `gh aw audit` (e.g., "the security job produced no meaningful output
  because the upstream agent job never ran") rather than a raw Actions job
  failure — consistent with the finding code's name but not independently
  reproduced by this note without running `gh aw audit` itself. For Ch04
  (Operations): document the full audit finding-code enum
  (`pkg/cli/audit_finding_codes.go`, 18 codes total) as a reference the
  guide can point to — no existing source note enumerates gh-aw's audit
  finding vocabulary; `docs-ghaw-audit-with-agents.md` and
  `docs-ghaw-monitoring-patterns.md` cover the JSON field *schema* for
  audit output but not the closed set of finding-code values that can
  populate it.

### Claim 10: The workflow's `cache:` block writes the deterministic pre-fetch step's output to `/tmp/gh-aw/agent/dependabot-burner/`, matching the platform-documented `/tmp/gh-aw/agent/` data-exchange convention exactly, and the pre-fetch itself (an `actions/github-script` step gathering open Dependabot PRs, prior failed burner PRs, and manifest-family classification) runs entirely before the agent job starts
- **Evidence**: Live workflow source frontmatter: `cache: [{key:
  dependabot-burner-selection-${{ github.run_id }}, path:
  /tmp/gh-aw/agent/dependabot-burner}]`, paired with a `steps:` entry
  ("Prefetch dependabot burner context") that runs `actions/github-script`
  to enumerate `listOpenDependabotPRs()` and `listRecentClosedBurnerPRs()`
  and writes the combined result to
  `/tmp/gh-aw/agent/dependabot-burner/context.json` before the agent's
  system prompt instructs it to `Read
  /tmp/gh-aw/agent/dependabot-burner/context.json` as its first step.
- **Confidence**: settled (directly read from the first-party workflow
  source; the fetched `context.json` artifact for run 33845039019, shown in
  Claim 6, confirms this is exactly the file the agent reads)
- **Quote**: `cache: - key: dependabot-burner-selection-${{ github.run_id }}
  ... path: /tmp/gh-aw/agent/dependabot-burner` (live workflow source
  frontmatter) / "1. Read `/tmp/gh-aw/agent/dependabot-burner/context.json`."
  (live workflow source, "## Read first")
- **Our assessment**: This is a concrete production instance of the
  precomputation pattern named in `docs-ghaw-deterministic-agentic-patterns.md`
  Claim 1 (three-stage hybrid pipeline) and Claim 3 (`/tmp/gh-aw/agent/` as
  the designated deterministic→agent data-exchange directory) — that note's
  examples were reconstructed/schema-illustrative (its Extraction Note 4
  says the YAML "is not character-for-character from the source"); this
  note supplies a real, verbatim, production workflow using the exact same
  directory convention end-to-end (deterministic GitHub-API enumeration →
  `/tmp/gh-aw/agent/<name>/context.json` → agent's own first instruction is
  to read that file). For Ch03: cite Dependabot Burner as the concrete
  worked example for `docs-ghaw-deterministic-agentic-patterns.md`'s
  precomputation pattern — a real workflow, not a documentation sketch.

## Concrete Artifacts

### Dependabot Burner: Workflow Frontmatter (fetched 2026-09-25)

```yaml
private: true
emoji: "🔥"
name: Dependabot Burner
description: Runs one grouped Dependabot remediation wave from schedule, manual dispatch, or /dependabot-burner on pull requests
on:
  roles: [admin, maintainer, write]
  schedule: weekly
  workflow_dispatch:
    inputs:
      objective: { type: string, required: false, default: "Close grouped Dependabot PRs for generated workflow manifests by updating source workflow markdown and recompiling in one replacement PR." }
  slash_command:
    strategy: centralized
    name: dependabot-burner
    events: [pull_request_comment, pull_request_review_comment]
permissions:
  contents: read
  issues: read
  pull-requests: read
concurrency:
  group: dependabot-burner
  cancel-in-progress: false
model: gpt-5.4-mini
engine:
  id: copilot
strict: true
network:
  allowed: [defaults, node, python, go]
cache:
  - key: dependabot-burner-selection-${{ github.run_id }}
    path: /tmp/gh-aw/agent/dependabot-burner
safe-outputs:
  allowed-domains: [default-safe-outputs]
  add-comment:
    max: 1
timeout-minutes: 20
imports:
  - shared/mcp-pagination.md
  - uses: shared/daily-pr-base.md
    with:
      title-prefix: "[dependabot-burner] "
      expires: "3d"
      labels: [automation, dependencies, dependabot]
      reviewers: [copilot]
  - shared/otlp.md
  - shared/reporting.md
tools:
  edit:
  cli-proxy: true
  github: { mode: local, toolsets: [default, pull_requests] }
  bash:
    - "make dependabot && make build"
    - "./gh-aw compile --dependabot"
    - "cd .github/workflows && npm install --package-lock-only"
    - "git status"
    - "git diff -- .github/workflows"
    - "cat /tmp/gh-aw/agent/dependabot-burner/context.json"
    - "cat .github/workflows/*.md"
    - "cat .github/workflows/shared/*"
    - "rg .github/workflows"
evals:
  - id: dependabot_batch_analyzed
    question: Did the agent analyze the selected grouped Dependabot remediation batch?
  - id: remediation_reported
    question: Was a remediation pull request created or clearly reported as not needed?
features:
  gh-aw-detection: true
```

*Source: `.github/workflows/dependabot-burner.md`, fetched via `curl` from
`raw.githubusercontent.com/github/gh-aw/main/`, 2026-09-25. `network.allowed`
including `node`/`python`/`go` (not just `defaults`) matches the
Node.js/npm requirement for npm lock-file generation documented in
`docs-ghaw-dependabot.md` Claim 6.*

### Five-Subagent Required Behavior Sequence (from live workflow source)

```
1. pr-group-analyzer        — confirm grouped PR set, flag exclusions
2. retry-history-analyzer   — derive retry strategy from failed burner PRs
                               + maintainer-only feedback
3. [if empty batch: noop with explanation, stop]
4. [if /dependabot-burner triggered: post grouping comment on triggering PR]
5. dependency-batch-analyzer — summarize dependency batch + likely source files
6. retry-feedback-synthesizer — condense retry history + feedback into constraints
7. dependabot-remediator     — EXACTLY ONCE: execute the single remediation wave
8. [do not split into multiple attempts or multiple PRs]
```

*Source: `.github/workflows/dependabot-burner.md`, "## Required behavior"
section, fetched 2026-09-25.*

### `dependabot-remediator` Subagent: Result Contract and PR Gate

```
Always write (even if blocked/no-op):
  /tmp/gh-aw/agent/dependabot-burner/results/${{ github.run_id }}-result.json
  Fields: pr_numbers, dependencies_processed, source_files_updated,
          fix_applied, replacement_pr_created, retry_strategy,
          maintainer_feedback_used, status (improved|unchanged|blocked),
          validation_commands, notes

PR creation gate — ALL must hold:
  1. the fix is real and bounded
  2. validation passed (make dependabot && make build; npm install
     --package-lock-only if npm manifest changed)
  3. git diff --stat shows an actual code change
  4. status would report "improved"
```

*Source: `.github/workflows/dependabot-burner.md`, `## agent:
dependabot-remediator` section ("Deterministic result", "Required
validation", "Pull request rule"), fetched 2026-09-25.*

### Run `33845039019` (Sept 4) — First-Party Artifacts vs. Blog Narrative

```
BLOG CLAIM: "completed successfully in 27 turns and ~10 minutes, walking
through candidate PRs, grouping the applicable ones, and firing off its
replacement pull request."

ACTUAL FIRST-PARTY DATA (all fetched 2026-09-25):

  gh run view 33845039019 --json conclusion  → "success"

  agent/dependabot-burner/context.json (agent artifact):
    { "open_pr_count": 0,
      "selected_batch_pr_numbers": [],
      "selected_batch_dependencies": [],
      "recent_failed_burns": [] }

  evals.jsonl (evals artifact):
    {"id":"dependabot_batch_analyzed", "answer":"NO"}
    {"id":"remediation_reported",      "answer":"NO"}

  safe-output-items.jsonl (safe-outputs-items artifact):
    <empty file — zero safe outputs of any kind emitted>

  agent_output.json (agent artifact):
    {"items":[],"errors":[]}

  Agent-job log, "Copilot Execution Summary":
    [4]  "No in-scope Dependabot PRs are selected, so I'm recording a
          no-op result and finishing without changes."
    [11] "Blocked: no in-scope Dependabot PRs were selected, so there
          was nothing to remediate."
    Statistics: Turns: 11   Tools: 7/7 succeeded
                Tokens: 170,925 total (170,397 in / 528 out)

  Repo-wide PR search (gh api search/issues):
    q='repo:github/gh-aw is:pr label:dependabot label:automation
        label:dependencies'  →  total_count: 0
    (zero PRs anywhere in github/gh-aw carry the label set this
    workflow's own safe-outputs config would apply to a real output PR)
```

*Sources: `gh run view 33845039019 --repo github/gh-aw --log`; `gh api
repos/github/gh-aw/actions/artifacts/{9926324783,9926384948,9926364122}/zip`
(agent, evals, safe-outputs-items artifacts respectively); `gh api
search/issues`. All fetched 2026-09-25.*

### `driver_exit` Classification Rule (from ADR-47250)

```
Rule: failed run with Turns == 0  → "driver_exit"   (infra/harness layer)
      failed run with Turns  > 0  → "agent_logic"   (agent reasoning layer)

Implemented in: pkg/cli/logs_models.go, isDriverExitFailure(run) bool
Propagated to: WorkflowHealth.DriverExitCount, .AgentLogicFailureCount,
               LogsSummary.Total{DriverExit,AgentLogic}Failures,
               RunData.FailureKind

Known false-classification edge case (ADR's own "Negative" consequence):
  a run that fails at the agent's very first action, before completing
  one full turn, still reports Turns==0 and is misclassified as
  driver_exit even though the agent did begin executing.
```

*Source: `docs/adr/47250-classify-driver-exit-vs-agent-logic-failures.md`,
fetched via `curl` from `raw.githubusercontent.com/github/gh-aw/main/`,
2026-09-25.*

### Audit Finding Codes (from `pkg/cli/audit_finding_codes.go`)

```go
AuditFindingWorkflowFailed         = "workflow_failed"
AuditFindingWorkflowTimeout        = "workflow_timeout"
AuditFindingHighTokenUsage         = "high_token_usage"
AuditFindingManyIterations         = "many_iterations"
AuditFindingMultipleErrors         = "multiple_errors"
AuditFindingMCPServerFailures      = "mcp_server_failures"
AuditFindingToolsNotAvailable      = "tools_not_available"
AuditFindingBlockedNetworkRequests = "blocked_network_requests"
AuditFindingWorkflowSucceeded      = "workflow_succeeded"
AuditFindingDetectionJobFailed     = "threat_detection_job_failed"
AuditFindingThreatDetected         = "threat_detected"
AuditFindingAgenticResourceHeavy      = "agentic_resource_heavy_for_domain"
AuditFindingAgenticOverkill           = "agentic_overkill_for_agentic"
AuditFindingAgenticPoorControl        = "agentic_poor_agentic_control"
AuditFindingAgenticPartiallyReducible = "agentic_partially_reducible"
AuditFindingAgenticModelDowngrade     = "agentic_model_downgrade_available"
AuditFindingAgenticDelegatedContext   = "agentic_delegated_context_present"
```

*Source: `pkg/cli/audit_finding_codes.go`, fetched via `curl` from
`raw.githubusercontent.com/github/gh-aw/main/`, 2026-09-25. Comment in
source: "AuditFindingCode is a stable machine-readable identifier for an
audit finding type... must not be repurposed."*

### PR #40396 Summary (workflow's cited origin)

```
Title: Add centralized /dependabot-burner grouping and retry-aware
       single-workflow remediation
Merged: 2026-06-20T02:56:41Z (created 2026-06-19T22:05:47Z)
Changed files: 8  (+807 / -4022)
  MODIFIED: .github/workflows/agentic_commands.yml
  MODIFIED: .github/workflows/dependabot-burner.{md,lock.yml}
  DELETED:  .github/workflows/dependabot-campaign.{md,lock.yml}  (-249/-1730)
  DELETED:  .github/workflows/dependabot-worker.{md,lock.yml}    (-179/-1776)
  MODIFIED: .github/workflows/skillet.lock.yml
```

*Source: `gh pr view 40396 --repo github/gh-aw --json
title,body,additions,deletions,changedFiles,files,mergedAt,createdAt`,
fetched 2026-09-25.*

### `dependabot-burner.lock.yml` Run History Sample, 2026-04-14 through 2026-09-25 (fetched 2026-09-25)

```
2026-09-25  success   (latest run at extraction time)
2026-09-18  failure   — driver_exit signature (4x copilot-harness retries
                         exhausted, exitCode=1, no Turns: line printed)
2026-09-11  failure   — same driver_exit signature
2026-09-04  success   — BLOG'S CITED "SUCCESS": Turns:11, open_pr_count:0,
                         zero safe outputs, ended in explicit "Blocked" noop
2026-08-28  success
2026-07-31  failure   (push-triggered run, not sampled in detail)
2026-07-13  failure   (push-triggered run, not sampled in detail)
[...16 additional "success"-conclusion scheduled runs back to 2026-04-14,
 none independently verified for actual PR output by this note]
```

*Source: `gh run list --repo github/gh-aw
--workflow=dependabot-burner.lock.yml --limit 30 --json
databaseId,conclusion,createdAt,event,status`, fetched 2026-09-25. Only the
four runs named in bold above were opened and read in full; the remaining
"success" runs are conclusion-only and were not individually checked for
whether they actually produced output, per Claim 7's caveat.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-dependabot.md` Claims 5, 6, 7, 8 (`--dependabot` all-workflows
    constraint, Node.js/npm prerequisite, "never merge manifest-only PRs,"
    four-step source-first update procedure): Dependabot Burner is a
    production agent that automates exactly this documented human
    procedure — its bash allowlist runs the literal `./gh-aw compile
    --dependabot` command, and its `network.allowed` includes `node`,
    `python`, `go` matching Claim 6's tooling prerequisite for npm lock-file
    generation.
  - `docs-ghaw-deterministic-agentic-patterns.md` Claims 1 and 3 (three-stage
    hybrid pipeline; `/tmp/gh-aw/agent/` as the deterministic→agent data
    directory): Claim 10 here is a verbatim production instance of both —
    a `github-script` pre-step writes to
    `/tmp/gh-aw/agent/dependabot-burner/context.json`, and the agent's
    first instruction is to read exactly that file.
  - `docs-ghaw-audit-with-agents.md` Claim 6 and
    `docs-ghaw-monitoring-patterns.md` Claim 6 (`noop` as an explicit
    completion signal; no-op run report suppression): Claim 4 here shows
    the same "always emit a structured result, even for nothing-to-do"
    discipline applied one layer down, inside an individual subagent's own
    result-JSON contract rather than at the workflow's safe-output layer.
  - `blog-ghaw-agent-of-the-day-2026-09-23.md` Claim 5 and its Extraction
    Note 4 (a gh-aw blog's own prose misattributing a real platform
    mechanism to a behavior it otherwise describes correctly) and
    `blog-ghaw-agent-of-the-day-2026-09-15.md` Extraction Note 2 (a
    WebFetch-paraphrase inaccuracy in an earlier post in the same series):
    Claim 6 here is a third, more severe instance of this series' prose
    being unreliable about specific checkable facts — this time about the
    *substance* of a cited run's outcome, not just a config field name.

- **Contradicts**: None requiring a filed contradiction issue. Claim 6
  documents a factual inaccuracy *within this source itself* — the blog
  misdescribes what its own cited, linked run actually did — not a
  disagreement between two source notes or two independently-argued
  positions. Per MINER.md §4a this does not meet the bar for a
  CONTRADICTIONS.md entry, consistent with the identical judgment made for
  the same class of finding in `blog-ghaw-agent-of-the-day-2026-09-23.md`
  Extraction Note 4 and `blog-ghaw-agent-of-the-day-2026-09-15.md`.
  Reviewed `CONTRADICTIONS.md` (8 entries: C-001 through C-008, none
  touching gh-aw dependency-remediation workflows, driver_exit
  classification, or audit finding-code semantics) and all source notes
  cited throughout this note. No contradiction issue filed.

- **Extends**:
  - `docs-ghaw-dependabot-rollout.md` (CentralRepoOps orchestrator/worker
    pattern for org-scale Dependabot configuration rollout across up to 100
    repos via `dispatch-workflow`): Dependabot Burner's five-subagent
    decomposition (Claim 3) is a structurally different multi-agent pattern
    — in-run inline subagent staging within one repo and one workflow
    invocation, not cross-repo worker dispatch. The two sources together
    show gh-aw supports at least two distinct "split the work across
    multiple agent contexts" patterns for different problem shapes:
    org-scale fan-out (CentralRepoOps) vs. single-run reasoning-stage
    decomposition (Dependabot Burner's inline subagents).
  - `docs-ghaw-threat-detection.md` Claim 1 (three-stage pipeline: agentic
    job → threat detection job → safe output processor): this note's
    observed job list for both cited runs (`pre_activation → activation →
    agent → detection → safe_outputs → evals → push_evals_state →
    conclusion`) is a real production instance of that architecture, and
    Claim 9 here adds the previously-undocumented finding-code vocabulary
    (`pkg/cli/audit_finding_codes.go`) that the detection/audit layer
    reports through.

- **Novel**:
  - **A verified, run-level factual inaccuracy in a first-party gh-aw
    blog post's central narrative claim** (Claim 6): more severe than the
    two prior instances of this pattern already in the corpus (misattributed
    config field, WebFetch paraphrase error) — here the blog's account of
    what its own cited, linked, "successful" run actually accomplished is
    directly contradicted by that run's complete first-party artifact set
    (context, evals, safe-outputs, agent output, and the agent's own final
    message).
  - **The `driver_exit`/`agent_logic` failure classification rule and its
    documented false-classification edge case** (Claim 8): not described in
    any existing corpus note; sourced from a first-party ADR
    (`docs/adr/47250-...md`) not previously fetched by this corpus.
  - **The closed-set audit finding-code enum** (Claim 9, 18 codes total):
    no existing source note enumerates gh-aw's audit finding vocabulary;
    prior notes (`docs-ghaw-audit-with-agents.md`,
    `docs-ghaw-monitoring-patterns.md`) document the JSON *schema* audit
    output uses but not the closed set of finding-code values.
  - **"Baseline-cohort matching" as a real, implemented run-comparison
    mechanism** (Claim 9): `pkg/cli/audit_comparison.go`'s `cohort_match`
    vs. `latest_success` baseline-selection logic is new to the corpus.
  - **An exact-string `bash:` allowlist as a narrower alternative to
    `bash: ["*"]`** (Claim 2): contrasted explicitly with the wildcard
    `bash: ["*"]` pattern already documented in
    `blog-ghaw-agent-of-the-day-2026-09-23.md` Cross-References → Extends
    (the ESLint Refiner bullet describing Daily Caveman Optimizer's tools
    config).
  - **A single-workflow, five-subagent inline decomposition for a
    remediation task** (Claim 3), distinct from the cross-repo
    orchestrator/worker pattern already covered by
    `docs-ghaw-dependabot-rollout.md` and `docs-ghaw-central-repo-ops.md`.
  - **A three-part conjunctive PR-creation gate inside a subagent's own
    instructions** (`status: improved` AND validation passed AND a real
    diff) (Claim 4): not documented in any existing source note as a
    named pattern.

## Guide Impact

- **Chapter 03 (Safety and Verification)**: Add Claim 6 as the corpus's
  strongest concrete case study for "verify a vendor's own blog-cited
  evidence before repeating it" — a first-party platform blog, citing a
  real and linked run ID as its main proof point, turns out to describe a
  run that did the opposite of what the post claims (zero candidates, zero
  output, explicit "Blocked" no-op) once the run's own artifacts are
  checked. Pair with the three-part PR-creation gate (Claim 4) and the
  maintainer-only retry-feedback scoping (Claim 5) as concrete, positive
  safety patterns from the same workflow, so the chapter isn't only "don't
  trust the blog" but also "here is what a well-designed low-trust
  remediation agent's own internal gates look like."

- **Chapter 02 (Harness Engineering)**: Add the exact-string `bash:`
  allowlist (Claim 2) as an alternative to wildcard `bash: ["*"]"` when a
  workflow's shell needs are fully enumerable ahead of time. Add the
  single-workflow inline-subagent decomposition (Claim 3) as a second
  multi-agent pattern alongside CentralRepoOps, for problems that need
  staged reasoning within one run rather than fan-out across repos. Cite
  Dependabot Burner as the first real (non-schema-illustrative) production
  example for `docs-ghaw-deterministic-agentic-patterns.md`'s
  precomputation pattern (Claim 10).

- **Chapter 04 (Operations)**: Add the full audit finding-code enum
  (Claim 9, Concrete Artifacts) as a reference table — this fills a gap
  in the existing audit-tooling coverage, which documents the JSON schema
  but not the closed set of finding values. Add the `driver_exit`/
  `agent_logic` classification rule and its known false-classification
  edge case (Claim 8) as a caveat for any fleet-health dashboard built on
  `WorkflowHealth.DriverExitCount`.

## Extraction Notes

1. **Blog post is short (~450 words); nearly all depth came from six fetched
   sub-artifacts**, within MINER.md §1's "up to 5 linked pages" guidance
   (extended here because the artifacts are API/log fetches rather than
   linked documentation pages, and because verifying the blog's central
   claim required following the run ID it linked): the live workflow source
   (`curl` from `raw.githubusercontent.com`), PR #40396 (`gh pr view`), the
   full Actions log for run 33845039019 (`gh run view --log`), that run's
   `agent`/`evals`/`safe-outputs-items` artifacts (`gh api .../artifacts/*/zip`
   + `unzip`), the two cited failed runs' full logs (`gh run view --log`),
   ADR-47250 (`curl`), and `pkg/cli/audit_finding_codes.go` +
   `pkg/cli/audit_comparison.go` (`curl`). None of this is present in the
   blog post's own text.

2. **Blog quotes obtained from the raw markdown source, not WebFetch or HTML
   scraping**: `docs/src/content/docs/blog/2026-09-24-agent-of-the-day.md`
   was located via `gh api search/code -f q='threat_detection_job_failed
   repo:github/gh-aw'` and fetched directly via `curl` from
   `raw.githubusercontent.com` — this is the actual Markdown source file
   for the post, not a rendered/summarized version, so quotes above are
   copied character-for-character from the source `.md`, cross-checked
   against an independent HTML-scrape pass (`curl` + regex tag-stripping)
   of the live page, which matched exactly.

3. **Cross-reference check performed** against `docs-ghaw-dependabot.md`,
   `docs-ghaw-dependabot-rollout.md`, `docs-ghaw-deterministic-agentic-patterns.md`,
   `docs-ghaw-threat-detection.md`, `docs-ghaw-audit-with-agents.md`,
   `docs-ghaw-monitoring-patterns.md`, `blog-gh-aw-operations-release-workflows.md`,
   `blog-ghaw-agent-of-the-day-2026-09-23.md`,
   `blog-ghaw-agent-of-the-day-2026-09-15.md`, and `CONTRADICTIONS.md`, all
   read in full before writing Cross-References. All `Claim N` citations
   above were checked against the actual numbered claims in those notes at
   the time of writing, per MINER.md §4b.

4. **`docs-ghaw-inline-sub-agents.md` cited but not independently verified**
   in Claim 3 — flagged explicitly in that claim's assessment as an open
   cross-check rather than treated as confirmed, since this note did not
   fetch that source note's contents.

5. **Claim 7's search-based absence check has known limitations** (stated
   in that claim's Confidence line): GitHub search-index completeness,
   possible label/title-prefix drift over the workflow's ~8-month history,
   and deleted PRs are all confounds this note could not rule out. Graded
   `emerging`, not `settled`, for that reason.

6. **Run-history sample is partial**: of the ~24 runs listed in the
   `gh run list` output for this workflow (2026-04-14 through 2026-09-25),
   only the four runs the blog itself references (plus the latest run at
   extraction time) were opened and read in full. The remaining
   "success"-conclusion runs were not individually checked for whether they
   produced real output — Claim 7's conclusion is therefore a corroborating
   signal from the sampled runs plus the label-based repo-wide search, not
   an exhaustive audit of the workflow's full run history.

7. **No contradiction filed**, per the reasoning in Cross-References →
   Contradicts: this is a source's own text being factually wrong about a
   run it names and links, not a disagreement between two independently-
   argued positions in the corpus.
