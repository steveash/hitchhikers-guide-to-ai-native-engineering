---
source_url: https://github.github.com/gh-aw/blog/2026-09-23-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – September 23, 2026: Daily Caveman Optimizer"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-09-23
date_extracted: 2026-09-24
last_checked: 2026-09-24
status: current
confidence_overall: settled
issue: "#3662"
---

# Agent of the Day – September 23, 2026: Daily Caveman Optimizer

> An "Agent of the Day" profile of Daily Caveman Optimizer, a scheduled workflow
> that trims redundant prose from gh-aw's own `.github/aw`/`.github/agents`
> instruction files without losing schema signal — first coverage of this
> workflow in the corpus. The blog's ~500-word narrative was substantially
> extended by fetching the live workflow source
> (`.github/workflows/daily-caveman-optimizer.md`), the merged PR (#62470) and
> its underlying commit diff, and two weeks of prior scheduled-run history
> (including full failure logs for a six-day outage window), which
> together surface the workflow's full "preserve schema signal / cut filler"
> rule set, an in-flight Sonnet-vs-Haiku A/B cost experiment, one factual
> inaccuracy in the blog's own text about how the workflow stays quiet on
> already-tight files, and an undisclosed six-day platform sandbox outage
> immediately preceding the profiled run — none of which appear in the blog
> post itself.

## Source Context

- **Type**: blog-post (an "Agent of the Day" entry from the official GitHub
  Agentic Workflows blog, bylined "Copilot" — same recurring convention as
  the rest of this series, e.g. `blog-ghaw-agent-of-the-day-2026-09-15.md`).
- **Author credibility**: Official gh-aw platform team blog. The post cites a
  specific, independently-checkable Actions run
  (`github/gh-aw/actions/runs/35652743170`) and a specific merged PR
  (`github/gh-aw/pull/62470`) — both fetched directly and read in full by this
  note (see Concrete Artifacts), plus the live workflow source
  (`.github/workflows/daily-caveman-optimizer.md`) and the run history of the
  workflow's prior six scheduled executions.
- **Scope**: One short post (~500 words) describing the workflow's mission and
  one day's headline result (the `loop.md` trim). Does NOT cover: the full
  file-selection/exclusion rules, the "preserve schema signal" editing
  criteria, the in-flight Sonnet-vs-Haiku cost experiment this exact run was
  randomized into, or the six consecutive scheduled-run failures immediately
  preceding the profiled run — all of which exist in the fetched workflow
  source and run history but are absent from the blog post's own text and
  were recovered by this note via direct fetches.

## Extracted Claims

### Claim 1: Daily Caveman Optimizer round-robins daily through gh-aw's own instruction directories and only opens a PR when it finds "real redundancy worth removing," using the "caveman optimization" joke/principle from a named third-party repo
- **Evidence**: Blog post opening paragraphs; corroborated by the live workflow
  source's `description` field and system prompt, both of which cite the same
  external repo (`github.com/JuliusBrussee/caveman`, confirmed via `gh api
  repos/JuliusBrussee/caveman` to be a real, 107,648-star public repository
  described as a "Viral skill + proxy for coding agents that cuts 65% of
  tokens by talking like a caveman").
- **Confidence**: settled (blog narrative directly corroborated by the live
  workflow's frontmatter `description` field and system-prompt text, both
  fetched fresh)
- **Quote**: "The workflow runs daily on a schedule, round-robins through the
  `.github/aw` and `.github/agents` instruction directories, and only opens a
  pull request when it finds real redundancy worth removing." (blog post) /
  "You are the Caveman Optimizer — an expert at applying the [caveman
  optimization](https://github.com/JuliusBrussee/caveman) principle to AI
  instruction and agent files." (live workflow source, opening line of system
  prompt)
- **Our assessment**: This is the first corpus coverage of a workflow whose
  entire mission is editing an agentic-workflow repo's own instruction files
  for token economy, as distinct from editing application code (the
  ESLint-domain agents) or filing operational issues. See Cross-References →
  Novel for how this differs from the corpus's other "caveman" source,
  `blog-jetbrains-caveman-token-savings-test.md`.

### Claim 2: The profiled run found that `.github/aw/loop.md`'s "Shared architecture" section restated six concepts the immediately-following "Pattern inventory" section already covered in more depth, and the agent migrated unique details (branch-naming templates, repo-memory branch names, the status-comment sentinel, and the "discard but record" rule) into the pattern entries before deleting the duplicate section
- **Evidence**: Blog post narrative; independently confirmed by fetching the
  actual commit diff (`github/gh-aw` commit `4832a6ff`, via `gh api
  repos/github/gh-aw/commits/.../` with the diff media type) and the merged
  PR body (#62470), which both describe the same six concepts by name.
- **Confidence**: settled (blog narrative corroborated line-for-line by the
  first-party commit diff, which shows the exact prose removed and where each
  surviving detail was folded into Patterns A, B, C, D, E, F, and J)
- **Quote**: "The agent noticed that a `## Shared architecture` section near
  the top of the file was restating — almost line for line — six concepts
  that a `## Pattern inventory` section immediately below already covered in
  more depth: the single-item scheduler, canonical branch and single-PR
  conventions, ratcheting acceptance, durable repo-memory state, the human
  control-plane issue, and pause semantics." (blog post)
- **Our assessment**: The commit diff (see Concrete Artifacts) shows this was
  not a blind deletion — e.g. Pattern B's text is rewritten from "Branch names
  must be deterministic and suffix-free" to "Each item owns one stable,
  deterministic, suffix-free branch (`autoloop/<program>`, `goal/<issue>-<slug>`,
  `crane/<migration>`)", explicitly re-absorbing the naming templates that
  only existed in the deleted section. This is a stronger editing discipline
  than simple redundancy deletion: verify no unique fact lives only in the
  passage being cut, and if it does, relocate it before deleting.

### Claim 3: The resulting PR #62470 was 8 lines added, 32 removed (net 17% shorter), touched exactly one file, and was merged by a human maintainer (@pelikhan) approximately 27 minutes after it was opened
- **Evidence**: Blog post narrative; independently confirmed via `gh pr view
  62470 --repo github/gh-aw --json additions,deletions,changedFiles,createdAt,mergedAt`,
  which returns `additions: 8, deletions: 32, changedFiles: 1, createdAt:
  "2026-09-21T20:53:15Z", mergedAt: "2026-09-21T21:20:15Z"` — a gap of 26
  minutes 60 seconds.
- **Confidence**: settled (blog's stated numbers match the PR API response
  exactly, including the derived ~27-minute merge time)
- **Quote**: "The result, opened as PR #62470, was refreshingly small: 8 lines
  added, 32 removed, net 17% shorter, one file touched. ... Maintainer
  @pelikhan merged it about 27 minutes after it was opened." (blog post)
- **Our assessment**: Every quantitative claim in this sentence checks out
  against the live PR API response — a clean, independently-verifiable
  first-party metric, not a rounded or narrativized approximation.

### Claim 4: The PR body included a table of files reviewed but not touched, each with a one-line, file-specific reason rather than a generic "already fine"
- **Evidence**: PR #62470 body, "Files Reviewed — No Change Needed" table,
  fetched via `gh pr view 62470 --repo github/gh-aw --json body`.
- **Confidence**: settled (directly read from the first-party PR body, quoted
  in full)
- **Quote**: "`.github/aw/intent.md` | Prose-dense but non-redundant; each
  paragraph carries distinct design guidance" / "`.github/aw/jobs.md` |
  Almost entirely reference tables and YAML" / "`.github/aw/linter-workflows.md`
  | Already imperative bullets with no filler" / "`.github/aw/llms.md` |
  Mostly code blocks and a port/credential table" (PR #62470 body, "Files
  Reviewed — No Change Needed" table)
- **Our assessment**: This is the same "report the negative space" discipline
  documented for a different gh-aw workflow in
  `blog-ghaw-agent-of-the-day-2026-09-15.md` Claim 6 (ESLint Refiner
  itemizing why each non-filed rule was a true negative) — now shown in a
  documentation-editing agent rather than a code-linting agent, reinforcing it
  as a cross-domain reporting convention on this platform rather than a
  linting-specific habit.

### Claim 5: The blog post attributes the workflow's silence on already-tight files to an `if-no-changes: "ignore"` setting — but the live workflow source contains no `if-no-changes` field at all; the actual mechanism is an explicit `noop:` safe-output combined with a prompt instruction to call it when no files need changes
- **Evidence**: Blog post narrative claims the setting by name. The live
  workflow source's full `safe-outputs:` block (fetched via `curl` against
  `raw.githubusercontent.com/github/gh-aw/main/.github/workflows/daily-caveman-optimizer.md`)
  reads `safe-outputs: { steer: true, create-pull-request: {expires: 3d,
  title-prefix: "[caveman] ", labels: [...], draft: false, protected-files:
  allowed, allowed-files: [...]}, noop: }` — no `if-no-changes` key is
  present anywhere in the frontmatter. The prompt body's own "Step 5: Output"
  section instructs: "If no files needed changes, call `noop`" with a
  structured JSON example. Separately, `gh api search/code -q '"if-no-changes"
  repo:github/gh-aw'` confirms `if-no-changes` is a real gh-aw
  `create-pull-request` field (default `"warn"`, per
  `docs/src/content/docs/reference/safe-outputs-pull-requests.md`) used by
  *other* gh-aw workflows (e.g. `.github/workflows/eslint-miner.md`,
  `linter-miner.md`) — so the field exists on the platform, just not in this
  workflow's configuration.
- **Confidence**: settled (directly diffed the blog's specific claim against
  the live workflow source's full frontmatter, which is freely inspectable
  and contains no such key)
- **Quote**: "Not every run finds something to fix — the agent's
  `if-no-changes: \"ignore\"` setting means it stays quiet when a file is
  already tight, and one recent run did close without a PR, exactly as
  designed." (blog post) / "**If no files needed changes**, call `noop`:
  ```json
  {\"noop\": {\"message\": \"No changes needed. Files in this batch are
  already concise. Processed: <file1>, <file2>. Queue position: N/Z.\"}}
  ```" (live workflow source, "Step 5: Output")
- **Our assessment**: This is a factual inaccuracy in the blog's own text,
  not a matter of interpretation — the specific field name and value it names
  do not exist in this workflow's configuration. The *behavior* the blog
  describes (staying quiet on tight files) is real and independently
  confirmed (Claim 6 below), but the mechanism is misattributed: it is an
  explicit LLM-executed `noop` safe-output call per the system prompt, not a
  harness-level `if-no-changes` gate. This matters for Ch02/Ch03 guide
  accuracy: a reader citing this blog post's field name to configure their
  own workflow would be reaching for a real gh-aw field that happens to be
  wrong for this use case (it governs `create-pull-request`'s behavior when
  a *branch push* produces no diff, not whether the agent decides there's
  nothing to fix). Consistent with the blog-inaccuracy pattern already
  documented in `blog-ghaw-agent-of-the-day-2026-09-15.md` Extraction Note 2
  (an initial WebFetch pass over a different blog post in this series
  returned a paraphrase that also got a technical detail wrong) — this is a
  second, independent instance of this series' blog prose containing a
  plausible-sounding but unverified technical claim.

### Claim 6: A prior scheduled run genuinely closed with no PR via the `noop` path, consistent with the "quiet on tight files" behavior the blog describes (even though its stated mechanism, Claim 5, is wrong)
- **Evidence**: Blog post narrative asserts this happened. This note did not
  independently locate the specific noop'd run in the fetched run history
  (the six runs immediately preceding the profiled one, 2026-09-15 through
  2026-09-20, all failed at the infrastructure level before the agent could
  execute — see Claim 9 — so the noop run the blog references, if real, is
  not among those six and was not otherwise located).
- **Confidence**: anecdotal (the blog's own assertion; this note could not
  independently confirm which specific run it refers to, and the six most
  recent prior runs are ruled out as candidates by Claim 9)
- **Quote**: "Not every run finds something to fix ... one recent run did
  close without a PR, exactly as designed." (blog post)
- **Our assessment**: Flagged as unconfirmed rather than verified — this note
  checked run history back to 2026-09-09 (15 runs) and found successes (with
  PRs, per the merged-PR pattern in Claim 7's queue-progress numbers) and the
  six-day failure streak in Claim 9, but did not fetch every individual run's
  full agent output to locate a specific noop. Included here because the
  underlying behavior (staying quiet when appropriate) is corroborated by the
  workflow's explicit design (Claim 5's `noop` path and the "Prefer no
  change" guideline in Concrete Artifacts), even though this specific
  instance is not independently verified.

### Claim 7: The workflow processes files in fixed batches of 5 per run via a persisted round-robin cursor, and the profiled run's PR states it had processed "files 31–35 of 71 in the queue" — of which only file 31 (`loop.md`) needed an edit
- **Evidence**: Live workflow source, "Step 2: Load Round-Robin State" and
  "Guidelines" sections ("Small batches: Processing 5 files per run keeps
  each run focused and reviewable"); PR #62470 body, "Round-Robin Progress"
  section.
- **Confidence**: settled (directly read from the first-party workflow source
  and PR body; the batch-of-5 mechanism is not mentioned in the blog post,
  which instead compresses this to "landed on file 31 of a 71-file queue")
- **Quote**: "Pick the **next 5 files** starting from `last_processed_index +
  1` (wrapping around if needed). This is your **batch** for this run." (live
  workflow source, Step 2) / "Processed files 31–35 of 71 total files in the
  queue." (PR #62470 body, "Round-Robin Progress")
- **Our assessment**: The blog's "landed on file 31" phrasing is a
  simplification, not an inaccuracy: file 31 (`loop.md`) is the one file in a
  5-file batch (31–35) that needed an edit — the other four are the "Files
  Reviewed — No Change Needed" table (Claim 4). A reader of the blog post
  alone would not know the run reviewed four other files in the same pass, or
  that the workflow's queue-persistence mechanism uses a cache-memory JSON
  state file (`/tmp/gh-aw/cache-memory/caveman-optimizer/state.json`) with a
  documented cold-start behavior (random starting index via `$(( RANDOM %
  TOTAL ))` when no prior state exists, to avoid always processing the same
  files first).

### Claim 8: The workflow's editing criteria explicitly separate "signal that helps agents write valid AW source" (must preserve) from "prose that does NOT help agents generate AW" (cut freely), with a stated default-to-caution rule when the classification is ambiguous
- **Evidence**: Live workflow source, "Critical Context: These Files Are
  Agentic Instructions" and "Caveman Optimization Rules" sections.
- **Confidence**: settled (directly read from the first-party workflow
  system prompt; not mentioned in the blog post at all, which only describes
  the outcome, not the editing policy)
- **Quote**: "**Preserve signal that helps agents write valid AW source:**
  YAML frontmatter examples showing field names and valid values... Trigger/
  permission/tool patterns that agents will copy directly... \"Do this, not
  that\" patterns... Any hint that narrows the space of valid AW
  configurations... Constraints the compiler enforces" / "**Golden rule**: If
  removing a sentence would make an agent more likely to write invalid AW
  frontmatter, keep it. If in doubt, keep it." (live workflow source)
- **Our assessment**: This is a concrete, transferable pattern for any agent
  tasked with trimming instruction files that are themselves consumed by
  other agents: the classification criterion is not "is this sentence
  wordy" but "does removing this sentence change what a downstream agent
  would generate." The `10%` minimum-reduction threshold documented alongside
  this (Concrete Artifacts) — "Only edit if you can reduce the file by at
  least 10% in characters or lines... without removing any AW schema hints"
  — is a further guardrail against marginal, low-value edits triggering a PR.
  For Ch02: this is a specific, quotable instance of "optimize for the
  downstream consumer of the instructions, not for line count" as a design
  principle for any self-referential documentation-maintenance agent.

### Claim 9: The six scheduled runs immediately preceding the profiled 2026-09-21 run (2026-09-15 through 2026-09-20) all failed identically at workflow startup, before the Claude agent began executing, with a sandbox permission error on the `cloud-hypervisor` runtime binary — an outage not mentioned anywhere in the blog post
- **Evidence**: `gh run list --repo github/gh-aw --workflow=daily-caveman-optimizer.lock.yml --limit 15 --json databaseId,conclusion,createdAt,event,status`, which lists `conclusion: "failure"` for the six runs dated 2026-09-15 through 2026-09-20 and `conclusion: "success"` immediately before and after that window. Full logs for all six failed runs (`gh run view <id> --repo github/gh-aw --log`) were fetched; each shows an identical failure signature at the `agent` job's "Execute Claude Code CLI" step.
- **Confidence**: settled (directly observed in six independent, first-party
  GitHub Actions run logs, all showing the same error class; the blog post
  does not mention this outage at all)
- **Quote**: "[ERROR] Fatal error: Error: Unable to execute
  \"/run/awf-cloud-hypervisor/trusted-artifacts/run-Y5aDue/cloud-hypervisor
  --version\"; verify the trusted Cloud Hypervisor artifact exists, is
  executable, and is complete: code=EACCES; Command failed with EACCES:
  /run/awf-cloud-hypervisor/trusted-artifacts/run-Y5aDue/cloud-hypervisor
  --version" (run 35392917245 log, 2026-09-18; the same `EACCES` signature —
  with a different random `trusted-artifacts/run-*` path each time — appears
  in the 2026-09-17, -18, -19, and -20 runs; the 2026-09-15 and -16 runs show
  a shorter variant of the same underlying failure: "exited with code
  undefined" instead of an explicit `EACCES`) / "[claude-awf-retry] AWF failed
  before the claude harness started; recorded agent execution evidence as
  not_started" (same log)
- **Our assessment**: This is a six-consecutive-day outage of the sandboxed
  execution layer for a production scheduled workflow, self-resolving by the
  2026-09-21 run with no corresponding commit to this workflow's own source
  in that window (the only commit touching this workflow's file in the run's
  vicinity is the loop.md content commit itself, which is the agent's
  *output*, not an infra fix). `blog-ghaw-cloud-hypervisor-consolidation.md`
  Claim 1 documents `cloud-hypervisor` as being in **preview** as of
  2026-09-05, gated to GitHub-hosted Ubuntu x86_64 runners with `/dev/kvm` —
  this outage is concrete evidence that a preview-status sandbox runtime
  reached a fully broken state (100% failure rate) for six consecutive daily
  runs on a real production workflow, not a synthetic test. For Ch03/Ch04:
  practitioners adopting preview-status sandbox runtimes should expect (and
  monitor for) multi-day silent failure windows, since this workflow's own
  `noop`/PR reporting path never fires when the agent doesn't start at all —
  a human watching only the workflow's *outputs* (PRs, discussions) would see
  a six-day gap and have no first-party signal explaining it short of
  checking Actions run conclusions directly.

### Claim 10: The profiled run's firewall blocked one outbound request to `api.anthropic.com`, which is absent from the workflow's `network.allowed` list (`[defaults, github]`)
- **Evidence**: PR #62470's auto-appended firewall warning box, fetched via
  `gh pr view 62470 --json body`; live workflow source's `network:` block.
- **Confidence**: settled (directly observed in the first-party PR body's
  auto-generated firewall-block callout and the live workflow frontmatter)
- **Quote**: "The following domain was blocked by the firewall during
  workflow execution: - `api.anthropic.com`" (PR #62470 body, auto-appended
  warning) / `network: { allowed: [defaults, github] }` (live workflow
  source frontmatter)
- **Our assessment**: This is the same blocked-domain signature documented
  for a different workflow (ESLint Refiner) in
  `blog-ghaw-agent-of-the-day-2026-09-15.md` Claim 9, and is consistent with
  `docs-ghaw-awf-reflect-reference.md` Claim 3's documented prohibition on
  hardcoding direct upstream model API URLs — inference is expected to route
  through the AWF gateway, so a blocked direct call to `api.anthropic.com` is
  expected enforcement behavior, not a misconfiguration needing a
  `network.allowed` fix. This is now a second independent gh-aw workflow (of
  two profiled in this corpus with visible firewall-block data) showing the
  identical blocked domain, strengthening the case that whatever in the
  toolchain attempts this direct call is common across `engine: claude`
  workflows rather than workflow-specific — still not root-caused by either
  note.

### Claim 11: This run was one arm of a live, first-party A/B experiment (`model_size`) comparing `claude-sonnet-5` against `claude-haiku-4.5` on this exact optimization task, using a `continual` ramped-rollout schedule not documented in the corpus's existing gh-aw experiments coverage
- **Evidence**: Live workflow source frontmatter, `experiments:` block; blog
  post's closing paragraphs confirm the run drew the Haiku variant.
- **Confidence**: settled for the experiment's existence and this run's
  variant assignment (directly read from first-party workflow frontmatter and
  corroborated by the blog's own text); emerging for how `continual`/`ramp`
  specifically alters the balancing algorithm, since this note did not find
  that field in `docs-ghaw-practices-experiments.md` or
  `docs-ghaw-practices-experiments-specification.md` (searched both for
  `continual` and `ramp:` — no matches) and so cannot corroborate its
  behavior against existing platform documentation.
- **Quote**: "experiments: model_size: variants: [claude-sonnet-5,
  claude-haiku-4.5] ... hypothesis: \"H0: no change in PR creation rate or
  run success rate. H1: Claude Haiku reduces AI credit usage >=30% with
  equivalent run success rate (>=0.90).\" ... guardrail_metrics: - name:
  run_success_rate threshold: \">=0.90\" - name: empty_output_rate threshold:
  \"<=0.10\" min_samples: 20 continual: seed: daily-caveman-model-size-v1
  ramp: [10, 25, 50] start_date: \"2026-06-04\"" (live workflow source
  frontmatter) / "This run was also part of a live A/B experiment comparing
  `claude-sonnet-5` against `claude-haiku-4.5` on this exact task — testing
  whether the cheaper model produces equivalent documentation trims at lower
  token cost. This run drew the Haiku variant and still shipped a clean,
  mergeable PR." (blog post)
- **Our assessment**: The experiment has been running since 2026-06-04 (per
  `start_date`) — roughly 15 weeks before this profiled run — meaning the
  09-21 run is one data point in a long-lived rollout, not a one-off test.
  The `continual`/`ramp: [10, 25, 50]` fields read as a staged rollout
  percentage schedule (consistent with typical progressive-rollout naming),
  but since neither existing corpus note on gh-aw's experiments feature
  documents this field, this note cannot confirm the exact semantics —
  flagged as an open question for a future dedicated `docs-ghaw-*` mining
  pass on the experiments reference pages, not resolved here.

## Concrete Artifacts

### Commit `4832a6ff` — `.github/aw/loop.md` diff (PR #62470, merged 2026-09-21T21:20:15Z)

```
--- a/.github/aw/loop.md
+++ b/.github/aw/loop.md
@@ -12,41 +12,17 @@ A loop workflow repeatedly: 1) selects one work item, 2) makes one bounded impro

 Design for reliability across repeated runs, merges, CI failures, and human steering.

-## Shared architecture across Autoloop, Goal, and Crane
-
-### 1) Single-item scheduler
-
-Select one item per run (Autoloop: one program, Goal: one goal issue, Crane: one migration). Bounds run cost, preserves round-robin fairness.
-
-### 2) Canonical long-running branch + single PR
-
-Each item owns one stable branch and one draft PR (`autoloop/<program>`, `goal/<issue>-<slug>`, `crane/<migration>`). Accumulate accepted commits on that same PR over time.
-
-### 3) Ratcheting acceptance
-
-Accept a change only when it improves the tracked metric (or advances the contract) and passes CI/verification gates. On failure, discard the change but still record the run.
-
-### 4) Durable state in repo-memory
-
-Persist state as markdown in a dedicated memory branch (`memory/autoloop`, `memory/goal`, `memory/crane`). Keep it machine-readable and human-editable.
-
-### 5) Human control-plane issue
-
-Each item has one canonical issue with: a durable status comment sentinel (`<!-- ...:STATUS -->`), one per-run log comment, human steering directives.
-
-### 6) Explicit no-progress and pause semantics
-
-When blocked or stuck, pause with a concrete reason. Do not retry forever.
-
 ## Pattern inventory

 ### Pattern A — Item selection and fairness

+Select one item per run (Autoloop: one program, Goal: one goal issue, Crane: one migration). Bounds run cost, preserves round-robin fairness.
+
 Use a deterministic pre-step scheduler that writes a compact selection artifact...

 ### Pattern B — Canonical branch invariants

-Branch names must be deterministic and suffix-free. Always use ahead/behind logic against default branch:
+Each item owns one stable, deterministic, suffix-free branch (`autoloop/<program>`, `goal/<issue>-<slug>`, `crane/<migration>`). Always use ahead/behind logic against default branch:
 [... unchanged bullet list ...]

 ### Pattern C — One PR per item

-Never create multiple active PRs for the same item. Resolve in order: ...
+Each item owns one draft PR; accumulate accepted commits on it over time. Never create multiple active PRs for the same item. Resolve in order: ...

 ### Pattern D — Improve → push → gate → accept

-Three-phase accept path: ... Avoids sandbox-only false positives.
+Three-phase accept path: ... Avoids sandbox-only false positives. On failure, discard the change but still record the run.

 ### Pattern E — CI fix loop with circuit breakers

-... pause with structured reason (`ci-fix-exhausted`, `stuck`, `ci-timeout`).
+... pause with structured reason (`ci-fix-exhausted`, `stuck`, `ci-timeout`). Do not retry forever.

 ### Pattern F — Structured state file

-Keep a stable state layout with: machine-state table...
+Persist state as markdown in a dedicated repo-memory branch (`memory/autoloop`, `memory/goal`, `memory/crane`), machine-readable and human-editable. Keep a stable layout with: machine-state table...

 ### Pattern J — Unified run reporting

-On every run (accepted/rejected/error/blocked): update durable status comment, append per-run summary comment...
+Each item has one canonical control-plane issue carrying a durable status comment sentinel (`<!-- ...:STATUS -->`), per-run log comments, and human steering directives. On every run (accepted/rejected/error/blocked): update the status comment, append a per-run summary comment...
```

*Source: `github/gh-aw` commit `4832a6ffe9638081eff5bc6de58879ab29f54391`, fetched via `gh api repos/github/gh-aw/commits/4832a6ff... -H "Accept: application/vnd.github.v3.diff"`, 2026-09-24. Elided marks (`...`) mark unchanged bullet/list content omitted for length; all added/removed lines are reproduced verbatim.*

### PR #62470 — Files Reviewed table and firewall warning (fetched 2026-09-24)

```
Title:      [caveman] Optimize instruction verbosity — loop.md (2026-09-21)
Created:    2026-09-21T20:53:15Z
Merged:     2026-09-21T21:20:15Z  (by @pelikhan)
Additions:  8   Deletions: 32   Files changed: 1
Labels:     documentation, automation, prompt-quality

Files Optimized:
| .github/aw/loop.md | 144 lines | 120 lines | "Shared architecture" section
  that restated the Pattern inventory below it |

Files Reviewed — No Change Needed:
| .github/aw/intent.md          | Prose-dense but non-redundant; each
                                   paragraph carries distinct design guidance |
| .github/aw/jobs.md            | Almost entirely reference tables and YAML |
| .github/aw/linter-workflows.md| Already imperative bullets with no filler |
| .github/aw/llms.md            | Mostly code blocks and a port/credential
                                   table |

Round-Robin Progress: Processed files 31-35 of 71 total files in the queue.

Footer: "claude · agent · 141.1 AIC · ⌖ 53.2 AIC · ⊞ 8.7K"; model: haiku45;
  expires 2026-09-24T20:53:09.579Z (3d, matching safe-outputs.create-pull-
  request.expires: 3d)

Auto-appended firewall warning: "Firewall blocked 1 domain ... api.anthropic.com"
  — not in this workflow's network.allowed: [defaults, github].
```

*Source: `github/gh-aw` PR #62470, fetched via `gh pr view 62470 --json
title,body,additions,deletions,changedFiles,files,mergedAt,createdAt,labels,commits`, 2026-09-24.*

### Daily Caveman Optimizer: Workflow Frontmatter (fetched 2026-09-24)

```yaml
private: true
emoji: "⚡"
name: Daily Caveman Optimizer
description: Applies caveman optimization to instruction files in .github/aw
  and .github/agents — making them more concise without losing technical
  accuracy. Round-robins through files daily and creates a PR when
  improvements are found.
on:
  schedule:
    - cron: daily
  workflow_dispatch:
max-daily-ai-credits: 10000
permissions:
  contents: read
  pull-requests: read
  issues: read
tracker-id: daily-caveman-optimizer
model: "${{ needs.activation.outputs.model_size }}"
engine:
  id: claude
strict: true
experiments:
  model_size:
    variants: [claude-sonnet-5, claude-haiku-4.5]
    description: "Tests whether Claude Haiku produces equivalent instruction
      conciseness improvements at lower token cost versus Claude Sonnet."
    hypothesis: "H0: no change in PR creation rate or run success rate. H1:
      Claude Haiku reduces AI credit usage >=30% with equivalent run success
      rate (>=0.90)."
    metric: ai_credits_total
    secondary_metrics: [run_success_rate, run_duration_ms]
    guardrail_metrics:
      - name: run_success_rate
        threshold: ">=0.90"
      - name: empty_output_rate
        threshold: "<=0.10"
    min_samples: 20
    continual:
      seed: daily-caveman-model-size-v1
      ramp: [10, 25, 50]
    start_date: "2026-06-04"
network:
  allowed:
    - defaults
    - github
safe-outputs:
  steer: true
  create-pull-request:
    expires: 3d
    title-prefix: "[caveman] "
    labels: [documentation, automation, prompt-quality]
    draft: false
    protected-files: allowed
    allowed-files:
      - .github/aw/**
      - .github/agents/**
  noop:
sandbox:
  agent:
    id: awf
tools:
  cli-proxy: true
  cache-memory: true
  github:
    mode: local
    toolsets: [default]
  edit:
  bash:
    - "*"
timeout-minutes: 30
imports:
  - shared/otlp.md
features:
  gh-aw-detection: true
evals:
  - id: instruction_file_optimized
    question: Did the agent apply caveman optimization to an instruction
      file in .github/aw or .github/agents?
  - id: pr_created_or_noop
    question: Was a PR created with concise improvements, or was noop used
      when no improvements were needed?
```

*Source: `.github/workflows/daily-caveman-optimizer.md`, fetched via `curl`
from `raw.githubusercontent.com/github/gh-aw/main/`, 2026-09-24.*

### Daily Caveman Optimizer: File Queue Exclusions and Optimization Threshold (system prompt, fetched 2026-09-24)

```
Excluded from processing (never modify these):
- github-agentic-workflows.md — canonical schema reference, maintained by
  instructions-janitor
- Any file whose name ends in -agentic-workflow.md or matches *-workflow.md
  inside .github/aw/ (dispatcher/template prompts such as create, update,
  debug, upgrade variants)
- Any file that contains disable-model-invocation: true in its first 10
  lines (template files)
- Any file under 20 lines (already concise)

Optimization threshold: Only edit if you can reduce the file by at least 10%
in characters or lines — counting only removed prose, not whitespace
changes — without removing any AW schema hints, field examples, or compiler
constraints. When uncertain whether a cut loses agentic signal, keep the
original text.
```

*Source: `.github/workflows/daily-caveman-optimizer.md`, "Step 1: Build the
File Queue" and "Step 3b: Assess optimization potential" sections, fetched
2026-09-24.*

### Run history, `daily-caveman-optimizer.lock.yml`, 2026-09-09 through 2026-09-23 (fetched 2026-09-24)

```
2026-09-09  success
2026-09-10  success
2026-09-11  success
2026-09-12  success
2026-09-13  success
2026-09-14  success
2026-09-15  failure  — EACCES on cloud-hypervisor trusted-artifacts binary
2026-09-16  failure  — same signature
2026-09-17  failure  — same signature
2026-09-18  failure  — same signature
2026-09-19  failure  — same signature
2026-09-20  failure  — same signature
2026-09-21  success  — profiled run; PR #62470
2026-09-22  success
2026-09-23  success  — blog published same day
```

*Source: `gh run list --repo github/gh-aw --workflow=daily-caveman-optimizer.lock.yml --limit 15 --json databaseId,conclusion,createdAt,event,status`, fetched 2026-09-24; failure detail from `gh run view <id> --repo github/gh-aw --log` on each of the six failed run IDs (35021356986, 35148320109, 35272495249, 35392917245, 35468186716, 35536381816).*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-agent-of-the-day-2026-09-15.md` Claim 6 ("report the negative
    space" — itemizing true negatives with specific reasons, not a blanket
    "no issues found"): Claim 4 here is the same discipline in a
    documentation-editing workflow rather than a linting workflow.
  - `blog-ghaw-agent-of-the-day-2026-09-15.md` Claim 9 and
    `docs-ghaw-awf-reflect-reference.md` Claim 3 (firewall blocks on direct
    calls to `api.anthropic.com`, consistent with the AWF-gateway-routing
    requirement): Claim 10 here is a second, independent gh-aw workflow
    showing the identical blocked domain.
  - `blog-ghaw-cloud-hypervisor-consolidation.md` Claim 1 (`cloud-hypervisor`
    is a preview-status sandbox runtime as of 2026-09-05): Claim 9 here is
    concrete evidence of that preview runtime failing completely for six
    consecutive production runs roughly two to three weeks later.

- **Contradicts**: None requiring a filed contradiction issue. Claim 5
  documents a factual inaccuracy *within this source itself* (the blog
  misnames the mechanism behind a real, correctly-described behavior), not a
  disagreement between two source notes or two independently-argued
  positions — per MINER.md §4a this does not meet the bar for a
  CONTRADICTIONS.md entry. Reviewed `CONTRADICTIONS.md` (9 entries, none
  touching gh-aw documentation-maintenance workflows, sandbox runtime
  reliability, or `safe-outputs.create-pull-request` semantics) and all
  source notes cited throughout this note. No contradiction issue filed.

- **Extends**:
  - `blog-jetbrains-caveman-token-savings-test.md` (the "Caveman" skill's
    marketed 65% token-saving claim measures at ~8.5% in real agentic
    workloads once code/diffs/tool calls dominate the token budget): that
    note benchmarks a *runtime prompt-compression* skill built from the same
    `JuliusBrussee/caveman` repo this workflow cites by name and quotes for
    its "why use many token when few do trick" tagline. This is a different
    mechanism (editing static instruction files ahead of time, not
    compressing live conversational output) applying the same named
    principle — see Novel below for why this is not treated as a
    contradiction.
  - `blog-ghaw-agent-of-the-day-2026-08-28.md` Claim 7 (ESLint Refiner grants
    no code-editing capability at all — `edit: null` plus a four-command
    read-only `bash:` allowlist — because it can only file issues, never fix
    code): Daily Caveman Optimizer's tools config is a structural *contrast*,
    not a match, worth naming explicitly rather than assumed. Its frontmatter
    also sets `edit:` with no value (syntactically identical to ESLint
    Refiner's `edit: null`) but pairs it with `bash: ["*"]` — a single-item
    list, not the `bash: {allow: [...]}` object form
    `docs-ghaw-tools-reference.md` Claim 2 documents for expanding bash access
    (that page's documented expansion tokens are `git:*` for a command family
    and `:*` for unrestricted access; `["*"]` as a bare list item matches
    neither string exactly). This note cannot confirm from the tools reference
    alone whether `bash: ["*"]` grants the same unrestricted shell access as
    `:*`, but functionally the workflow *does* edit and commit file content
    (Claim 2, Concrete Artifacts), which only make sense if some tool grants
    write access to the working tree — most plausibly broad `bash:` access
    used to rewrite file contents directly, with `create-pull-request` then
    diffing the working tree, rather than a dedicated `edit:` tool call. The
    file-scoping in this workflow instead comes from a different mechanism,
    `safe-outputs.create-pull-request.allowed-files: [.github/aw/**,
    .github/agents/**]` (Concrete Artifacts) — a safe-output-level allowlist
    on which files a PR may touch, not a tools-level restriction. Both
    workflows constrain an autonomous agent's blast radius, but via different
    layers of the same platform (tool grants vs. safe-output allowlists) —
    flagged as an open question for a future `docs-ghaw-tools-reference.md`
    or `bash:` field deep-dive, not resolved here.

- **Novel**:
  - **A workflow whose entire mission is trimming an agentic-workflow
    platform's own instruction files for token economy, with an explicit
    "does this sentence change what a downstream agent generates" edit
    criterion** (Claim 8): distinct from the corpus's existing
    documentation-maintenance coverage, which so far concerns code
    comments/READMEs or third-party docs, not first-party AI-instruction
    files consumed at runtime by other agents on the same platform.
  - **A specific instance of a gh-aw blog post's own prose being factually
    wrong about a named configuration field** (Claim 5): the corpus has
    previously documented a WebFetch-paraphrase inaccuracy
    (`blog-ghaw-agent-of-the-day-2026-09-15.md` Extraction Note 2), but this
    is the first instance where the blog's own published text — not a
    summarization artifact — misattributes a real, differently-scoped
    platform field to explain a behavior it otherwise describes correctly.
  - **A first-party A/B experiment comparing model size (Sonnet vs. Haiku) on
    a documentation-editing task, using a `continual`/`ramp` field not found
    in the corpus's existing `docs-ghaw-practices-experiments*` coverage**
    (Claim 11): the corpus has prior coverage of the `experiments:` schema's
    bare/rich forms and `min_samples`/`guardrail_metrics` fields, but not
    this staged-rollout mechanism.
  - **A six-consecutive-day total outage of a preview-status sandbox runtime
    on a real production scheduled workflow, invisible to anyone monitoring
    only the workflow's PR/discussion outputs** (Claim 9): the corpus's
    existing sandbox-reliability coverage is architectural/reference
    material (`docs-ghaw-sandbox-reference.md`) and a single deprecation
    announcement (`blog-ghaw-cloud-hypervisor-consolidation.md`); this is the
    first concrete, dated, multi-run failure incident tied to that specific
    preview runtime.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the "preserve signal that helps a
  downstream agent write valid output, cut everything else" criterion (Claim
  8) as a specific, transferable pattern for any agent maintaining
  instruction files that are themselves consumed by other agents at runtime —
  distinguish this from generic prose-trimming, which has no such downstream
  correctness constraint. Add the "verify no unique fact lives only in the
  passage being cut, relocate before deleting" discipline (Claim 2) as a
  concrete technique, not just a stated goal.

- **Chapter 03 (Safety and Verification)**: Flag Claim 5 as a caution about
  trusting even first-party platform blog prose for exact configuration field
  names/values without checking the live source — this source note's own
  quality bar (MINER.md §2a/§4b) exists for the same reason. Add Claim 9 (the
  six-day `cloud-hypervisor` outage) as a concrete illustration that
  preview-status sandbox runtimes can fail totally and silently on scheduled
  workflows; recommend monitoring Actions run conclusions directly rather
  than relying on a workflow's own PR/discussion output cadence as an
  implicit health signal.

- **Chapter 04 (Operations)**: Add the `experiments.continual`/`ramp` field
  (Claim 11) as an open item for a dedicated docs-mining pass on gh-aw's
  experiments reference pages — the corpus's existing experiments coverage
  does not yet explain staged-rollout percentage semantics. Note the second
  independent `api.anthropic.com` firewall-block instance (Claim 10) as
  further evidence this is expected, platform-wide `engine: claude` behavior
  under the AWF-gateway-routing model, not workflow-specific.

## Extraction Notes

1. **Blog post is short (~500 words); primary depth came from four fetched
   sub-pages**, within MINER.md §1's "up to 5" budget: the merged PR #62470
   (`gh pr view`), the underlying commit diff (`gh api .../commits/... -H
   "Accept: application/vnd.github.v3.diff"`), the live workflow source
   (`curl` against `raw.githubusercontent.com`), and the run history plus six
   individual failed-run logs (`gh run list` / `gh run view --log`). Claims
   5, 6 (partially), 7 (partially), 8, 9, and 11, and all of Concrete
   Artifacts except the PR summary table, rely on this sub-page material —
   none of it is present in the blog post's own text.

2. **Verbatim blog quotes obtained via direct HTML fetch, not WebFetch
   summarization**, per the same MINER.md §2a discipline documented in
   `blog-ghaw-agent-of-the-day-2026-09-15.md` Extraction Note 2: the page was
   fetched via `curl`, the `sl-markdown-content` div isolated, and converted
   with a Python regex pass (links preserved as `text [LINK:href]`, `<code>`
   tags converted to backticks, headings/paragraphs converted to newlines)
   before stripping remaining tags and unescaping HTML entities. All blog-post
   quotes above are copied character-for-character from that pass.

3. **Cross-reference check performed** against
   `blog-ghaw-agent-of-the-day-2026-09-15.md`,
   `blog-ghaw-cloud-hypervisor-consolidation.md`,
   `blog-jetbrains-caveman-token-savings-test.md`,
   `docs-ghaw-awf-reflect-reference.md`, `docs-ghaw-sandbox-reference.md`,
   `docs-ghaw-practices-experiments.md`,
   `docs-ghaw-practices-experiments-specification.md`, and
   `CONTRADICTIONS.md`, all read (in full or by targeted claim-list grep
   against already-deeply-read notes) before writing Cross-References. All
   `Claim N` citations above were checked against the actual numbered claims
   in those notes at the time of writing, per MINER.md §4b.

4. **No contradiction filed**: the JetBrains "Caveman" skill benchmark
   (`blog-jetbrains-caveman-token-savings-test.md`) and this workflow apply
   the same named principle to different mechanisms (runtime prompt
   compression vs. ahead-of-time static-file editing) and different metrics
   (measured conversational output tokens vs. a file's own line/character
   count) — per MINER.md §4a this is a conditioning-variable difference, not
   a material disagreement that would lead to different guide advice on the
   same question. Both are cited under Extends rather than Contradicts.

5. **`api.anthropic.com` block not root-caused**, same open question as
   `blog-ghaw-agent-of-the-day-2026-09-15.md` Claim 9 — this note also could
   not determine what specifically attempted the blocked direct connection.

6. **The blog's noop'd run (Claim 6) was not independently located.** This
   note checked run history back to 2026-09-09 and confirmed the six runs
   immediately prior to the profiled one all failed at the infrastructure
   level (Claim 9), ruling those out as the noop run the blog references, but
   did not fetch full agent transcripts for the remaining successful runs to
   find the specific noop instance. Flagged as anecdotal rather than
   verified.

7. **`continual`/`ramp` experiment semantics not resolved.** Searched both
   existing gh-aw experiments-practices notes for `continual` and `ramp:` —
   no matches in either. This note does not know what `ramp: [10, 25, 50]`
   controls (percentages, sample counts, or something else) and did not
   guess; flagged as an open question in Claim 11 and Guide Impact rather
   than resolved with an assumption.
