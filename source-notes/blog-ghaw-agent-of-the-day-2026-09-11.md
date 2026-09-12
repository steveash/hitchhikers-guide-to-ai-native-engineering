---
source_url: https://github.github.com/gh-aw/blog/2026-09-11-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – September 11, 2026: jsweep, the JavaScript Unbloater"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-09-11
date_extracted: 2026-09-12
last_checked: 2026-09-12
status: current
confidence_overall: emerging
issue: "#3402"
---

# Agent of the Day – September 11, 2026: jsweep, the JavaScript Unbloater

> A profile of jsweep, gh-aw's daily one-file-per-day JavaScript cleanup agent
> for `actions/setup/js/`, whose "prioritizing files still marked with
> `@ts-nocheck`" framing and "merged output speaks for itself" example list do
> not survive independent verification: every one of the 433 non-test `.cjs`
> files in that directory was confirmed, by downloading and grepping each one
> live, to be free of `@ts-nocheck` already — meaning the Priority-1 selection
> criterion the blog describes can no longer fire — and one of the post's two
> named "merged output" examples (#52227) was never merged at all; it expired
> and auto-closed two days after five automated review bots had approved it.
> The workflow's own persisted cache-memory ledger (read directly from
> today's run log) shows only one real code change in its last seven
> tracked successful runs, and a repo-wide PR search shows jsweep has not
> landed a single merged PR in the 21 days before this post — a far deeper
> "coming up empty" streak than the post's single-day framing conveys.

## Source Context

- **Type**: blog-post (an "Agent of the Day" entry from the official GitHub
  Agentic Workflows blog, bylined "Copilot" — the same recurring gh-aw
  AI-authored-post convention documented throughout this series, e.g.
  `blog-ghaw-agent-of-the-day-2026-09-10.md`, `blog-ghaw-agent-of-the-day-2026-09-08.md`).
  This is the first corpus entry to profile jsweep by name.
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team, profiling a workflow that runs in
  the team's own `github/gh-aw` repository. This note independently fetched
  the live workflow source (`.github/workflows/jsweep.md`, 360 lines, via
  `curl` from `raw.githubusercontent.com`), the workflow's full Actions run
  history (336 runs since 2025-12-18, via `gh api
  repos/github/gh-aw/actions/workflows/217041300/runs`), job/step-level detail
  and full run logs for today's run plus four sampled failed runs, the
  workflow's own persisted `jsweep-state.json` cache-memory contents (as
  embedded in today's run log), a repo-wide search for every
  `[jsweep] `-titled PR (185 found), the full timelines of two named example
  PRs (#52227, #54427), and a direct download-and-grep of all 433 non-test
  `.cjs` files currently in `actions/setup/js/` — none of this was taken from
  the blog post's own text. Most of it qualifies or corrects the blog's
  framing; see Claims 4, 5, 7, and 8 below.
- **Scope**: Covers the featured agent's stated mission (clean one `.cjs`
  file per day, prioritizing `@ts-nocheck` files), its triage-then-cleanup
  process, today's specific run metrics, two named "merged output" PR
  examples, its `safe-outputs` configuration philosophy, and a closing "why
  this matters" framing about type-safety debt. Does NOT cover: the
  workflow's actual lifetime reliability, its real merge/expiry rate, the
  current state of its target `@ts-nocheck` backlog, the automated PR-review
  ecosystem its own PRs pass through, or the fact that one of its two named
  examples never merged — all of which this note recovered only by fetching
  the live workflow source, the GitHub Actions API, and the repo's PR/search
  history directly.

## Extracted Claims

### Claim 1: jsweep runs daily with a `copilot` engine plus a TypeScript language server (LSP), processes exactly one `.cjs` file per day from `actions/setup/js/`, and persists a round-robin ledger (`jsweep-state.json`) in cache-memory so it never repeats a file
- **Evidence**: Direct first-party description in the post, corroborated
  near-verbatim by the live workflow source's frontmatter (`engine: {id:
  copilot}`, an `lsp.typescript` block wired to `.js`/`.cjs`/`.mjs`/`.ts`/`.tsx`
  extensions, `cache-memory: true`, and a Step 1 instruction to load
  `/tmp/gh-aw/cache-memory/jsweep-state.json`).
- **Confidence**: settled (identical mechanism described independently by the
  blog post and the live workflow source)
- **Quote**: "jsweep (workflow source) is deliberately narrow in scope: clean
  exactly one .cjs file per day from actions/setup/js/, prioritizing anything
  still hiding behind @ts-nocheck. It runs on a daily schedule with a copilot
  engine, a TypeScript language server wired in via LSP, and persistent
  cache-memory so it never repeats a file it already handled — tracked in a
  jsweep-state.json round-robin ledger."
- **Our assessment**: This is a clean, narrowly-scoped maintenance-agent
  design consistent with the "one file/day, gated by triage" pattern this
  entire post is built around. The live source's `lsp.typescript` block
  (`command: typescript-language-server`, `args: ["--stdio"]`) is a concrete,
  fetchable instance of gh-aw's LSP integration feature, not otherwise
  documented in this corpus's existing "Agent of the Day" notes. For Ch02
  (Harness Engineering): document the LSP-wired-cleanup-agent pattern as a
  design point distinct from a plain grep/regex-based code-modernization
  agent — the language server gives the agent semantic (not just textual)
  understanding of the file it's touching.

### Claim 2: Before touching any code, jsweep dispatches a `file-triage` sub-agent that reads only the first 80 lines of the candidate file and returns a compact `cleanup`/`noop` verdict; today's run concretely exercised this path and returned `noop` on file `upload_artifact.cjs`
- **Evidence**: Blog prose describing the sub-agent's inputs (github-script vs.
  Node.js context, `@ts-nocheck` presence, test-file existence, cleanup
  worthiness) matches the live workflow source's embedded `## agent:
  \`file-triage\`` block (`model: small`, "Read only the first 80 lines of
  file_path", returns `{"decision":"cleanup|noop", ...}`). Independently,
  today's full run log (`gh run view --repo github/gh-aw 34559616639 --log`)
  shows the actual sub-agent invocation and its literal JSON-shaped verdict.
- **Confidence**: settled (the mechanism is corroborated by both the blog and
  the live source; today's concrete invocation is read directly from the raw
  run log, not paraphrased)
- **Quote**: "Before touching a single line, jsweep dispatches a file-triage
  sub-agent that reads only the first 80 lines of the candidate file and
  returns a compact verdict: is this github-script or plain Node.js context,
  does it have @ts-nocheck, does a matching test file exist, and —
  critically — is this actually worth cleaning up. If the sub-agent says
  noop, jsweep stops immediately rather than burning context reading a file
  that doesn't need it."
- **Our assessment**: Today's actual sub-agent output, read directly from the
  run log's `assistant.message` event, was: "execution_context: node ·
  has_ts_nocheck: false (has `@ts-check` instead) · test_file_exists: true ·
  decision: noop · reason: File uses `@ts-check`, JSDoc types, clean
  requires/module structure, well-documented functions with proper JSDoc
  annotations — no dead code, verbose try/catch, or non-idiomatic patterns
  visible in first 80 lines. · target_changes: []" — a verbatim, concrete
  instance of exactly the abstract mechanism the blog describes, not
  available from the blog post itself. This `file-triage` sub-agent is also
  a production instance of the inline sub-agent pattern documented in
  `docs-ghaw-inline-sub-agents.md` (see Cross-References). For Ch02: the
  bounded-read-then-verdict sub-agent pattern (read N lines, return a small
  structured decision, let the parent branch on it) is a reusable
  context-preservation technique for any agent that must triage many
  candidates before committing to expensive full-file work.

### Claim 3: Today's run (#34559616639) finished in under 8 minutes and produced no pull request, both of which check out against independently-fetched Actions API data
- **Evidence**: `gh api repos/github/gh-aw/actions/runs/34559616639` gives
  `created_at` → `updated_at` of exactly 465 seconds (7.75 minutes), and `gh
  api "search/issues?q=repo:github/gh-aw+%5Bjsweep%5D+in:title+created:2026-09-11"`
  returns 0 results.
- **Confidence**: settled for duration and PR-count (both read directly from
  the GitHub API); unverified for the specific "336K tokens" and "2 turns"
  figures — this note's own read of the run's raw JSONL agent-execution log
  found 14 distinct `assistant.message` events (a different unit than
  "turns" as gh-aw's own harness may define it) and did not locate a single
  aggregate token-count field matching "336K" in the portions of the log this
  note inspected
- **Quote**: "Today's run (Action run #34559616639) finished in under 8
  minutes, used 336K tokens, and completed the whole loop in just 2 turns —
  a sign the triage sub-agent did its job well and jsweep made a fast, clean
  decision rather than wandering through the file tree. Zero errors, zero
  warnings, and by design no pull request was opened this time."
- **Our assessment**: The checkable parts of this claim (duration, no PR)
  are precisely correct. The token/turn counts are plausible but this note
  could not independently reproduce them from the raw log in the time
  available — "turns" likely refers to a specific gh-aw-internal accounting
  unit (e.g., LLM round-trips excluding the file-triage sub-agent's own
  internal turns) that doesn't map 1:1 onto raw `assistant.message` event
  counts. Flagged here rather than asserted as verified, per MINER.md's
  distinction between what was independently confirmed and what was merely
  not contradicted. For Ch04 (Operations): when citing per-run token/turn
  metrics from a source, note whether the figure was independently
  reproduced from the run's own artifacts or only taken on the source's word.

### Claim 4: Every one of the 433 non-test `.cjs` files currently in `actions/setup/js/` is free of `@ts-nocheck` — meaning the blog's "prioritizing files still marked with `@ts-nocheck`" framing describes a selection criterion that can no longer actually fire
- **Evidence**: This note downloaded all 433 non-test `.cjs` files in
  `actions/setup/js/` directly from `raw.githubusercontent.com/github/gh-aw/main/`
  and grepped each for the literal string `ts-nocheck`: zero matches.
  Independently, `gh api "search/code?q=ts-nocheck+repo:github/gh-aw"` (GitHub's
  code-search index, a second, differently-implemented check) returns exactly
  4 matches repo-wide, none under `actions/setup/js/` — only the blog post
  itself, the workflow source/lock files, and jsweep's own Go test file (all
  of which *mention* `ts-nocheck` as text, not carry it as a live pragma).
- **Confidence**: settled for the current state (two independent methods —
  direct download-and-grep of every candidate file, and GitHub's separate
  code-search index — agree); the blog's own framing is the one thing this
  contradicts, and per established precedent (see Cross-References →
  Contradicts) a first-party source's own prose not surviving a check against
  its own subject's live state does not meet the MINER.md §4a
  contradiction-filing bar
- **Quote**: "jsweep (workflow source) is deliberately narrow in scope: clean
  exactly one .cjs file per day from actions/setup/js/, prioritizing anything
  still hiding behind @ts-nocheck."
- **Our assessment**: The live workflow source itself still states this
  priority order ("PRIORITIZE files with `@ts-nocheck`" is listed as an
  "Important Constraint"), so the blog is accurately describing the
  *workflow's own instructions*, not fabricating anything — but those
  instructions describe a Priority-1 selection path that, as of this post,
  has no remaining candidates to select. Every run from here forward must
  fall through to the workflow's documented Priority-2 fallback ("pick one
  file at random from the top 10 most recently modified candidates"), which
  is a materially different task: instead of retiring known technical debt,
  the agent is now re-reviewing files it already (or previously) considered
  clean, hunting for marginal cleanups. This is a plausible root cause for
  Claim 5's noop streak: the backlog jsweep exists to clear appears to be
  cleared. For Ch02 (Harness Engineering) / Ch04 (Operations): a
  narrowly-scoped daily maintenance agent built against a finite backlog
  should have an explicit "backlog exhausted, consider retiring or
  repurposing" signal — without one, the agent silently keeps running,
  consuming its daily budget on low-value re-review, and a blog-style status
  post can still describe its original priority criterion as active
  indefinitely after it stops being reachable.

### Claim 5: The workflow's own persisted cache-memory state shows only one real code-cleanup entry across its seven most recent tracked successful runs, with six consecutive `noop` verdicts immediately preceding today's post
- **Evidence**: Today's run log (`gh run view --repo github/gh-aw
  34559616639 --log`) contains the literal contents of
  `/tmp/gh-aw/cache-memory/jsweep-state.json` as loaded at Step 1:
  `cleaned_files` lists `working_set_metrics.cjs` (2026-08-26, no note = a
  real cleanup) followed by `validate_memory_step.cjs` (09-03),
  `validate_secrets.cjs` (09-07), `write_daily_aic_usage_cache.cjs` (09-08),
  `workflow_metadata_helpers.cjs` (09-09), `upload_code_coverage.cjs`
  (09-10), each annotated "already clean, no changes needed (noop)"; today's
  run (Claim 2) appended `upload_artifact.cjs` with the same noop note.
- **Confidence**: settled (the cache-memory JSON is read verbatim from the
  run's own log output, not paraphrased or inferred)
- **Quote**: (from the run's own logged cache-memory state, not the blog)
  `{"file":"working_set_metrics.cjs","cleaned_at":"2026-08-26"}` followed by
  five consecutive entries each carrying the note `"already clean, no changes
  needed (noop)"` — see Concrete Artifacts for the full JSON.
- **Our assessment**: This is a far more specific and striking "coming up
  empty" data point than the blog's single-day framing conveys: not just
  today's run, but six of the workflow's last seven *successful, cache-writing*
  runs produced no code change at all. The `cache_hit_history` array (capped
  at the last 14 entries by the workflow's own `.slice(-14)` logic) only shows
  7 entries total despite ~139 lifetime merged PRs (Claim 7), which is
  consistent with the workflow's own documented behavior of periodically
  resetting `cleaned_files` to a single entry once "no uncleaned files
  remain" — i.e., the round-robin ledger appears to have already cycled
  through its full candidate pool and restarted multiple times over jsweep's
  nine-month history, and the current cycle has mostly been striking out.
  For Ch04 (Operations): a daily maintenance agent's own persisted
  state — not just its latest run's headline metrics — is a cheap, directly
  fetchable signal for "is this agent still finding real work," and can
  reveal a multi-week dry spell a single-run blog post has no reason to
  surface.

### Claim 6: jsweep's lifetime Actions run history (336 runs since 2025-12-18) shows a 24.1% failure rate (81 failures), a noticeably higher rate than other daily gh-aw agents already documented in this corpus, with at least some failures traced to an infrastructure-level sandbox/firewall fault unrelated to the agent's own JS-cleanup logic
- **Evidence**: `gh api repos/github/gh-aw/actions/workflows/217041300/runs`
  (workflow ID resolved via a full-workflow-list scan for `jsweep` in the
  path) returns 336 total runs, 255 `success` / 81 `failure`. Job/step
  detail for four sampled failed runs (2026-08-30, 09-02, 09-04, 09-05) shows
  all four failing in the `agent` job's "Execute GitHub Copilot CLI"
  equivalent step; full run logs for two of the four (09-04, 09-05) show the
  identical fatal error `Docker sbx direct egress bypassed Squid; ensure the
  sbx daemon was started with DOCKER_SANDBOXES_PROXY pointing to AWF Squid`
  (a sandbox network-isolation self-check failing before the agent ever
  starts working), while the other two (08-30, 09-02) show a bare `Agent
  execution exited with code 1` with all logged model API calls returning
  HTTP 200 and no visible tool-level error in this note's inspection window.
- **Confidence**: settled for the aggregate failure count (81/336, read
  directly from the Actions API); anecdotal for the specific failure-cause
  breakdown (n=4 sampled runs, 2 confirmed infra-cause, 2 unresolved)
- **Quote**: (no direct blog quote — the blog does not discuss jsweep's
  historical reliability at all, only today's specific "zero errors, zero
  warnings" run; sourced from the Actions API and raw run logs per MINER.md
  §4b)
- **Our assessment**: 81/336 = 24.1% is markedly worse than the two other
  daily gh-aw agents with fully-audited lifetime run histories in this
  corpus: CLI Version Checker's ~1-in-12 (`blog-ghaw-agent-of-the-day-2026-09-08.md`
  Claim 3) and Package Specification Librarian's 13/153 ≈ 8.5%
  (`blog-ghaw-agent-of-the-day-2026-09-10.md` Claim 3). The confirmed
  sandbox-egress fatal error is the same general category as those two
  notes' own findings — a platform/infrastructure fault rather than a bug in
  the agent's own domain logic — but this note could not confirm that
  category for all 81 failures, only 2 of the 4 sampled. For Ch04
  (Operations): when a source omits an agent's historical reliability
  entirely (as this post does), pulling the full run history via `gh api
  .../actions/workflows/<id>/runs` before treating a single clean run as
  representative is the same check already established for sources that
  *do* make an explicit reliability claim — the absence of a claim is not
  evidence of a clean history.

### Claim 7: Across its roughly nine-month lifetime, jsweep has opened 185 `[jsweep] `-titled pull requests, of which 139 (75%) merged and 46 (25%) closed without merging — and, as of this post, none has merged in the 21 days since #54427 on 2026-08-21
- **Evidence**: `gh api "search/issues?q=repo:github/gh-aw+%5Bjsweep%5D+in:title+type:pr"`
  returned 214 raw matches (GitHub's search API also loosely matches titles
  containing "jsweep" without the literal bracket prefix, e.g. maintainer
  commits like "Add jsweep daily workflow"); filtering to titles literally
  starting with `"[jsweep] "` narrows this to 185 real jsweep-produced PRs,
  of which this note counted 139 with a non-null `merged_at` and 46 `closed`
  with no `merged_at`. The most recent PR by `created_at` in this filtered
  set is #54427 (2026-08-21).
- **Confidence**: settled (both the filtered PR count and the merge/close
  split are computed directly from the GitHub search API's own per-item
  `merged_at`/`state` fields, not estimated)
- **Quote**: (no direct blog quote — the blog states only that "its merged
  output speaks for itself" without any aggregate count; sourced from the
  repo's own PR history per MINER.md §4b)
- **Our assessment**: The 21-day PR-less gap directly corroborates Claim 5's
  cache-memory-derived noop streak from a second, independent data source
  (repo-wide PR search vs. the workflow's own persisted state) — both point
  to the same conclusion: jsweep has been unusually unproductive in the
  weeks immediately preceding this "Agent of the Day" post, which is exactly
  when the post frames its behavior as a virtue ("comfortable coming up
  empty") rather than flagging it as a state worth investigating (is the
  backlog gone, per Claim 4, or is something else suppressing cleanup
  decisions?). The 25% unmerged rate is itself notable and is explored
  further in Claim 8. For Ch04 (Operations): a "restraint is a virtue"
  framing for a low-output agent should be checked against how long the
  agent has actually been producing nothing — restraint framed as by-design
  discipline (Claim 4/5) reads differently from restraint that turns out to
  be a symptom of an exhausted backlog with no repurposing plan.

### Claim 8: The blog's claim that jsweep's "merged output speaks for itself," illustrated by two named examples (#54427 and #52227), is inaccurate for one of those two examples — #52227 was never merged; it was reviewed favorably by five automated bots within about 16 hours and then auto-closed unmerged when its 2-day `expires` window elapsed
- **Evidence**: `gh pr view 52227 --repo github/gh-aw --json state,mergedAt,closedAt`
  shows `state: CLOSED`, `mergedAt: null`. The PR's own timeline
  (`gh api repos/github/gh-aw/issues/52227/timeline`) shows: opened
  2026-08-12 05:25 as a draft; `ready_for_review` at 21:34 the same day by
  maintainer `pelikhan`; five automated review-bot comments between 21:35
  and 21:36 (see Concrete Artifacts), including "✅ Great work! This PR looks
  ready for review" and "Lean already. Ship."; a `gh-aw-bot` comment at
  2026-08-13 00:44 asking `@copilot` to fix two failing checks and offering
  a branch update; then closed 2026-08-14 05:13 with the automated message
  "This pull request was automatically closed because it expired on
  2026-08-14T04:31:57.986Z" — a gap of essentially exactly 2 days from
  creation, matching the workflow's configured `safe-outputs.create-pull-request.expires:
  2d`.
- **Confidence**: settled (every step of this timeline — draft creation,
  ready-for-review conversion, all bot comments, the expiry closure and its
  exact timestamp — is read directly from the PR's own GitHub-recorded
  timeline and comment history, not paraphrased)
- **Quote**: "Looking back over jsweep's history, its merged output speaks
  for itself — recent examples include #54427: Clean
  run_validate_workflows.cjs, which extracted duplicated “truncate then
  sanitize” logic into a single reusable helper, and #52227: Clean
  validate_memory_files.cjs."
- **Our assessment**: This is a first-party source's own specific, checkable,
  by-number claim not surviving a direct check against its own subject's
  GitHub history — the same category of gap already established repeatedly
  in this series (see Cross-References → Contradicts) and so, per that
  precedent, not filed as a CONTRADICTIONS.md entry. What makes this
  instance sharper than most prior examples in the corpus is that it is not
  a matter of a narrow window or an omitted nuance — "merged output" is
  simply false for the specific PR named as an example of it. More
  interesting than the error itself is the mechanism it surfaces: #52227 was
  not rejected on quality grounds (five separate review bots approved it,
  one calling it "lean already. ship") and not abandoned by its author (a
  `gh-aw-bot` actively tried to route it back to Copilot for a fix) — it
  died purely because the fix-and-resubmit loop didn't complete inside a
  fixed 2-day window. This is a second, independently-found instance of the
  "expiry race" failure mode already documented for a different gh-aw agent
  in `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 2 (there, a
  cross-agent issue→PR handoff; here, a single agent's own PR dying inside
  its own review-and-fix cycle). For Ch04 (Operations): a 2-day `expires`
  window on a `create-pull-request` safe output is short enough that a PR
  which needs even one round of "bot flags an issue → agent must
  re-address it" can die from time pressure alone, independent of code
  quality — recommend either a longer expiry for PRs that enter an active
  review/fix cycle, or explicitly exempting PRs with recent bot activity
  from the expiry countdown.

### Claim 9: Both of the blog's two named example PRs were in fact created as drafts (matching the workflow's `draft: true` configuration) and later manually converted to ready-for-review by the same human maintainer, `pelikhan` — the draft-by-default mechanism itself worked exactly as designed
- **Evidence**: `gh api repos/github/gh-aw/issues/52227/timeline` and the
  equivalent call for issue 54427 both show a `ready_for_review` event
  (2026-08-12T21:34:25Z and 2026-08-21T05:26:51Z respectively) with actor
  `pelikhan`, immediately followed by `review_requested`; #54427 was then
  merged the same day (2026-08-21T10:30:46Z) also by `pelikhan`.
- **Confidence**: settled (both events are read directly from each PR's own
  GitHub timeline)
- **Quote**: (no direct quote; sourced from each PR's `issues/<n>/timeline`
  API response per MINER.md §4b, not from the blog, which does not discuss
  draft status)
- **Our assessment**: A naive `gh pr view --json isDraft` check on either PR
  today returns `false`, which could be misread as "the `draft: true`
  config isn't actually applied" — but the full timeline shows both PRs
  *were* created as drafts and only lost that status hours later via an
  explicit human action. This confirms the draft-by-default safety mechanism
  functioned correctly in both traced cases; the eventual outcomes diverged
  for unrelated reasons (#54427 was promptly merged same-day by the same
  maintainer who un-drafted it; #52227 was un-drafted, bot-reviewed, flagged
  for a fix, and then still expired — see Claim 8). For Ch03 (Safety and
  Verification): when auditing whether a `draft: true` safe-output
  configuration is actually honored, check the PR's *creation-time* state via
  its timeline API, not its current `isDraft` field, which only reflects the
  most recent state and can silently mask a working draft-then-promote
  workflow.

### Claim 10: jsweep's `file-triage` block is a concrete production instance of gh-aw's documented inline sub-agent feature, configured with the named model alias `small`
- **Evidence**: The live workflow source's `## agent: \`file-triage\`` block
  sets `model: small` in its frontmatter — the only field set besides
  `description`. Independently, a failed run's own API-proxy startup log
  (captured in this note's investigation of Claim 6) lists `small` as one of
  exactly 60 named model aliases the proxy resolves (`"aliases":["agent",
  "antigravity","any","auto",...,"small","small-agent",...]`), confirming
  `small` is a real, currently-resolvable alias rather than a stale or
  invalid reference.
- **Confidence**: settled (the sub-agent's `model` field is read directly
  from the live workflow source; the alias's validity is independently
  confirmed via a live proxy log, not merely assumed from the field's
  presence)
- **Quote**: (from the live workflow source's embedded sub-agent block, not
  the blog)
  ```yaml
  ## agent: `file-triage`
  ---
  description: Reads only the first 80 lines of the selected .cjs file and returns a compact cleanup decision.
  model: small
  ---
  ```
- **Our assessment**: This is a direct, in-production instance of
  `docs-ghaw-inline-sub-agents.md` Claim 4 (the `model` field as "the
  primary economic optimization lever for inline sub-agents," letting a
  parent workflow on a heavier model delegate bounded, cheap sub-tasks to a
  lighter one). jsweep's parent runs on the `copilot` engine's default model
  routing (Claim 6 showed at least one run resolving to `claude-sonnet-5` via
  `model: auto`-style routing), while the `file-triage` sub-agent is pinned
  to the explicitly lighter `small` alias for its 80-line-read, single-verdict
  task — exactly the cost/capability split that reference note's Claim 4
  predicts as the mechanism's intended use. For Ch02 (Harness Engineering):
  add this as a second, independently-verified worked example (alongside
  whatever the inline-sub-agent reference note's own examples are) of
  matching sub-agent model weight to task simplicity.

### Claim 11: jsweep's PRs pass through a repo-wide gauntlet of at least five distinct automated review-bot workflows (Design Decision Gate, Ponytail Reviewer, Matt Pocock Skills Reviewer, Test Quality Sentinel, PR Code Quality Reviewer) plus a `gh-aw-bot` dispatcher that can request `@copilot` fix a PR's failing checks — several of which reported a distinct "Threat Detection Engine Failure" tooling fault, not a security finding
- **Evidence**: PR #52227's own comment history (fetched via `gh pr view
  52227 --json comments`) shows five separate bot-authored review comments
  within about 90 seconds of each other on 2026-08-12, three of which
  (Matt Pocock Skills Reviewer, Test Quality Sentinel, PR Code Quality
  Reviewer) carry the identical boilerplate: "**Threat Detection Engine
  Failure** — The analysis engine could not complete. This is a tooling
  failure, not a security finding," followed by a link to that bot's own
  Actions run. A sixth, non-bot-review comment from `gh-aw-bot` then asks
  `@copilot` to "inspect the latest branch state, refresh the branch if
  needed, address the failed checks below, and run the `pr-finisher` skill."
- **Confidence**: settled for the fact of five distinct bot comments and
  the shared failure-boilerplate text (read directly from the PR's own
  comment history); anecdotal for how frequently the "Threat Detection
  Engine Failure" fires across the wider repo (n=1 PR traced)
- **Quote**: (from PR #52227's own comment thread, not the blog) "🧠 [Matt
  Pocock Skills Reviewer](...) has completed the skills-based review. ✅ >
  [!WARNING] > **Threat Detection Engine Failure** — The analysis engine
  could not complete. This is a tooling failure, not a security finding."
- **Our assessment**: This is entirely novel-to-the-corpus information the
  blog post never touches — it profiles jsweep in isolation and gives no
  indication that its output lands inside a multi-bot review pipeline at
  all. None of these five bot names, nor `gh-aw-bot`'s `@copilot`-dispatch
  behavior, appear in any existing source note in this corpus (a `grep`
  across `source-notes/` for each name returned no matches). That three of
  five bots hit the identical "Threat Detection Engine Failure" boilerplate
  on the same PR at nearly the same timestamp suggests a shared
  threat-detection dependency failing once and being independently reported
  by every consumer, rather than three unrelated bot-specific faults — the
  same "check whether a fault is platform-wide before treating it as
  workflow-specific" lesson already drawn in
  `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 8 for a blocked firewall
  domain, now observed for a shared analysis-engine dependency instead of a
  shared network egress path. For Ch02 (Harness Engineering) / Ch05 (Team
  Adoption): a repo that layers many independent review-bot workflows onto
  every PR should expect correlated, simultaneous tooling failures across
  that whole layer when a shared dependency (here, whatever "threat
  detection engine" all three consumed) goes down, and should design each
  bot's failure message to make that shared-cause hypothesis checkable (as
  these three did, by explicitly distinguishing "tooling failure" from "no
  finding").

## Concrete Artifacts

### jsweep: live workflow frontmatter (abridged, fetched via `curl` from `raw.githubusercontent.com/github/gh-aw/main/.github/workflows/jsweep.md`, 2026-09-12)

```yaml
private: true
emoji: "🧹"
description: Daily JavaScript unbloater that cleans one .cjs file per day, prioritizing files with @ts-nocheck to enable type checking
on:
  schedule: daily
  workflow_dispatch:
tracker-id: jsweep-daily
engine:
  id: copilot
  copilot-sdk: true
max-tool-denials: 3
imports:
  - shared/otlp.md
  - shared/reporting.md
tools:
  cli-proxy: true
  github:
    mode: local
    toolsets: [repos]
  edit:
  bash: ["*"]
  cache-memory: true
lsp:
  typescript:
    command: typescript-language-server
    args: ["--stdio"]
    fileExtensions:
      ".js": javascript
      ".cjs": javascript
      ".mjs": javascript
      ".ts": typescript
      ".tsx": typescriptreact
safe-outputs:
  create-pull-request:
    expires: 2d
    title-prefix: "[jsweep] "
    branch-prefix: "signed/"
    labels: [unbloat, automation]
    draft: true
    if-no-changes: "ignore"
network:
  allowed:
    - go
timeout-minutes: 20
strict: true
```

### `file-triage` inline sub-agent block (from the same live source)

```yaml
## agent: `file-triage`
---
description: Reads only the first 80 lines of the selected .cjs file and returns a compact cleanup decision.
model: small
---

You are a bounded JavaScript file triage sub-agent.
...
Rules:
- Read **only** the first 80 lines of `file_path`.
- If the file already looks well-maintained from the first 80 lines and you cannot justify 1–3 concrete cleanup targets, choose `noop`.
- If `@ts-nocheck` is present, always choose `cleanup`.
- Do not read past line 80.
```

### Today's actual triage decision (from run #34559616639's own log, fetched via `gh run view --repo github/gh-aw 34559616639 --log`, 2026-09-12)

```
- execution_context: node
- has_ts_nocheck: false (has `@ts-check` instead)
- test_file_exists: true
- decision: noop
- reason: File uses `@ts-check`, JSDoc types, clean requires/module structure,
  well-documented functions with proper JSDoc annotations — no dead code,
  verbose try/catch, or non-idiomatic patterns visible in first 80 lines.
- target_changes: []
```

### jsweep-state.json as loaded at the start of today's run (from the same run log)

```json
{
  "cleaned_files": [
    {"file": "working_set_metrics.cjs", "cleaned_at": "2026-08-26"},
    {"file": "validate_memory_step.cjs", "cleaned_at": "2026-09-03", "note": "already clean, no changes needed"},
    {"file": "validate_secrets.cjs", "cleaned_at": "2026-09-07", "note": "already clean, no changes needed"},
    {"file": "write_daily_aic_usage_cache.cjs", "cleaned_at": "2026-09-08", "note": "already clean, no changes needed (noop)"},
    {"file": "workflow_metadata_helpers.cjs", "cleaned_at": "2026-09-09", "note": "already clean, no changes needed (noop)"},
    {"file": "upload_code_coverage.cjs", "cleaned_at": "2026-09-10", "note": "already clean, no changes needed (noop)"}
  ],
  "last_run": "2026-09-10",
  "last_file": "upload_code_coverage.cjs",
  "cache_hit_history": [
    {"run_id": "32928386991", "date": "2026-08-26", "status": "hit"},
    {"run_id": "33717423487", "date": "2026-09-03", "status": "hit"},
    {"run_id": "34080822691", "date": "2026-09-07", "status": "hit"},
    {"run_id": "34184584747", "date": "2026-09-08", "status": "hit"},
    {"run_id": "34308317625", "date": "2026-09-09", "status": "hit"},
    {"run_id": "34434500061", "date": "2026-09-10", "status": "hit"}
  ]
}
```
*After today's run appended `upload_artifact.cjs` with an identical noop note.
Source: run #34559616639's own bash-tool output at Step 1, fetched via `gh run
view --repo github/gh-aw 34559616639 --log`, 2026-09-12.*

### Actions run history summary (fetched via `gh api repos/github/gh-aw/actions/workflows/217041300/runs`, paginated, 2026-09-12, 336 total runs)

```
Workflow ID: 217041300 (path: .github/workflows/jsweep.lock.yml)
First run:  #1  2025-12-18  success
Latest run: #336 2026-09-12  success
Total: 336 runs — 255 success / 81 failure (24.1% failure rate)

Sampled failed-run causes (job: agent, step: Execute GitHub Copilot CLI-equivalent):
  2026-08-30 (run #33290921299): exit code 1, no distinct tool-level error found in inspected window
  2026-09-02 (run #33588225184): exit code 1, no distinct tool-level error found in inspected window
  2026-09-04 (run #33834305456): "Fatal error: Error: Docker sbx direct egress bypassed Squid"
  2026-09-05 (run #33942634754): "Fatal error: Error: Docker sbx direct egress bypassed Squid"
```
*Source: GitHub Actions API plus `gh run view --log` for the four sampled
runs, fetched 2026-09-12.*

### PR #52227's full lifecycle (fetched via `gh pr view`/`gh api issues/52227/timeline`, 2026-09-12)

```
2026-08-12 05:25  jsweep opens #52227 as a DRAFT
                  "[jsweep] Clean validate_memory_files.cjs"
2026-08-12 21:34  ready_for_review (actor: pelikhan)
2026-08-12 21:35  5 automated review-bot comments within ~90s, incl.:
                  - "✅ Great work! This PR looks ready for review."
                  - "Lean already. Ship." (Ponytail Reviewer)
                  - 3× "Threat Detection Engine Failure — ... tooling
                    failure, not a security finding" (Matt Pocock Skills
                    Reviewer, Test Quality Sentinel, PR Code Quality Reviewer)
2026-08-13 00:44  gh-aw-bot: "@copilot Please inspect the latest branch
                  state ... address the failed checks below, and run the
                  pr-finisher skill ..."
2026-08-14 05:13  CLOSED — "automatically closed because it expired on
                  2026-08-14T04:31:57.986Z" (≈2 days after creation, matching
                  safe-outputs.create-pull-request.expires: 2d)
Never merged.
```

### jsweep lifetime PR yield (computed from `gh api "search/issues?q=repo:github/gh-aw+%5Bjsweep%5D+in:title+type:pr"`, filtered to titles starting with `"[jsweep] "`, 2026-09-12)

```
Total [jsweep]-titled PRs: 185
  Merged:          139 (75.1%)
  Closed unmerged:  46 (24.9%)
  Open:              0
Earliest: 2025-12-18   Latest: 2026-08-21 (#54427)
→ 21 days with zero merged jsweep PRs as of this post (2026-09-11/12)
```

### `@ts-nocheck` backlog check (this note's own direct download-and-grep of every file, 2026-09-12)

```
Files checked: all 433 non-test .cjs files in actions/setup/js/ (via
  raw.githubusercontent.com/github/gh-aw/main/actions/setup/js/<name>)
Files containing "ts-nocheck": 0

Cross-check via GitHub code search (gh api "search/code?q=ts-nocheck+repo:github/gh-aw"):
  4 total repo-wide matches, none under actions/setup/js/:
    docs/src/content/docs/blog/2026-09-11-agent-of-the-day.md  (mentions it as text)
    pkg/workflow/jsweep_workflow_test.go                        (mentions it as text)
    .github/workflows/jsweep.md                                 (the instruction itself)
    .github/workflows/jsweep.lock.yml                           (compiled instruction)
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-inline-sub-agents.md` Claim 4 (the sub-agent `model` field as
    the primary cost-optimization lever, letting a parent delegate a bounded
    task to a cheaper model): Claim 10 here is a concrete, in-production
    instance, with the exact `model: small` value cross-checked against a
    live API-proxy alias list.
  - `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 8 and
    `blog-ghaw-agent-of-the-day-2026-09-10.md` Claim 3 (a source's "N
    consecutive runs" or reliability framing checks out narrowly but omits a
    less-clean fuller history): Claim 6 here is a third instance of the same
    category, this time for a source that does not even attempt a lifetime
    reliability claim — the blog simply never raises the subject, and the
    fuller history (24.1% failure rate, worse than either prior example)
    still had to be independently pulled.
  - `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 2 (the "expiry race"
    failure mode, where a time-boxed safe output silently dies before a
    downstream fix/handoff completes): Claim 8 here is a second, structurally
    different instance — not a cross-agent issue→PR handoff, but a single
    agent's own PR dying inside its own bot-review-and-fix cycle.

- **Contradicts**: No contradiction issue filed. Claims 4 and 8 are the
  blog's own claims (an active `@ts-nocheck` priority criterion; two named
  PRs as examples of "merged output") not surviving a check against the
  post's own subject's live, checkable state — the same category of gap
  already established as not meeting the MINER.md §4a contradiction-filing
  bar in `blog-ghaw-agent-of-the-day-2026-09-08.md`,
  `blog-ghaw-agent-of-the-day-2026-09-10.md`, and
  `blog-ghaw-agent-of-the-day-2026-08-25.md` (see each note's own
  Cross-References → Contradicts). These are a first-party source's own
  prose not surviving a check against its own subject's checkable artifacts,
  not two independently-argued sources disagreeing with each other.
  `CONTRADICTIONS.md` and open `contradiction`-labeled issues were checked;
  no existing entry covers this workflow.

- **Extends**:
  - `docs-ghaw-inline-sub-agents.md`: adds a fifth-or-so concrete
    production instance of the inline sub-agent feature (the `file-triage`
    block), with a real traced invocation and output (Claim 2), extending
    that reference note's abstract field-by-field documentation with a
    worked example.
  - `docs-ghaw-cache-memory-reference.md` (not re-read in full for this
    note, but the general cache-memory mechanism it documents): jsweep's
    `jsweep-state.json` round-robin ledger is a concrete consumer of
    cache-memory for a use-case (avoid-repeat scheduling state) distinct
    from the token-usage-caching consumers already documented elsewhere in
    this corpus.
  - `blog-ghaw-agent-of-the-day-2026-09-08.md` and
    `blog-ghaw-agent-of-the-day-2026-09-10.md` (both establish that this
    blog series' first-party framing does not always survive independent
    verification against the subject's own live artifacts): this note adds
    two further, more consequential instances — an entire selection
    criterion that can no longer fire (Claim 4), and a named "merged"
    example that was never merged (Claim 8) — reinforcing that this is a
    recurring, checkable property of the series rather than a one-off.

- **Novel**:
  - **The complete exhaustion of the `@ts-nocheck` backlog in
    `actions/setup/js/`** (Claim 4, Concrete Artifacts) — independently
    verified via direct download-and-grep of all 433 candidate files plus a
    second GitHub code-search cross-check; not discoverable from the blog
    post, which describes the priority criterion as if still live.
  - **The persisted cache-memory ledger showing a 6-in-a-row noop streak**
    (Claim 5, Concrete Artifacts) — recovered only by reading the run's own
    logged tool output, not mentioned in the blog.
  - **The 185-PR lifetime yield with its 75%/25% merge/expire split and the
    21-day gap since the last merge** (Claim 7, Concrete Artifacts) — the
    first aggregate PR-outcome accounting for jsweep in the corpus.
  - **PR #52227's full traced lifecycle showing a positively-reviewed PR
    dying to a 2-day expiry** (Claim 8, Concrete Artifacts) — a second,
    independently-found instance of the expiry-race failure mode, and a
    direct refutation of the blog's own naming of that PR as an example of
    "merged output."
  - **The five-bot automated PR-review gauntlet and the shared "Threat
    Detection Engine Failure" tooling fault** (Claim 11) — an entirely new
    piece of the gh-aw repo's own development infrastructure, absent from
    every existing source note in this corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the bounded-read (first-80-lines)
  triage-sub-agent pattern (Claim 2) as a reusable context-preservation
  technique, now with a concrete real invocation and verdict to cite. Add the
  `model: small`-pinned inline sub-agent (Claim 10) as a second worked
  example of `docs-ghaw-inline-sub-agents.md`'s cost-optimization field. Add
  a caution: a narrowly-scoped daily maintenance agent built against a finite
  backlog (Claim 4) needs an explicit "backlog exhausted" signal, or it will
  silently keep running against an empty queue while a status post can still
  describe its original selection criterion as active.

- **Chapter 04 (Operations)**: Add the "check an agent's own persisted
  cache-memory state and its full PR/issue history, not just the latest
  run's headline metrics" lesson (Claims 5, 7) as a lightweight,
  API-only technique for detecting a multi-week productivity dry spell a
  single-run status post has no reason to surface. Add the 2-day
  `create-pull-request` expiry racing an active bot-review-and-fix cycle
  (Claim 8) as a second, independently-verified instance of the expiry-race
  failure mode — recommend a longer expiry, or an expiry-pause, for any PR
  that has received recent automated review/fix activity. Add the
  "correlated tooling failure across independent review bots sharing one
  dependency" observation (Claim 11) alongside the existing
  cross-workflow-blocked-domain lesson from
  `blog-ghaw-agent-of-the-day-2026-09-08.md` Claim 8.

- **Chapter 03 (Safety and Verification)**: Add the draft-by-default
  verification method (Claim 9) — check a PR's creation-time state via its
  own timeline API, not its current `isDraft` field, before concluding a
  `draft: true` safe-output configuration isn't being honored.

- **Chapter 05 (Team Adoption)**: When citing an "Agent of the Day"-style
  spotlight post's named example artifacts (specific PR numbers, specific
  file counts), check them against the artifact's own current state before
  repeating them — this post's own two named "merged" examples included one
  that never merged (Claim 8), and its central selection criterion had
  already stopped being reachable (Claim 4) at the time it was published.

## Extraction Notes

1. **Raw HTML fetched via `curl` for the blog post itself, not just
   WebFetch**: an initial WebFetch pass returned a paraphrased, re-sectioned
   summary ("Core Purpose"/"Key Operational Details"/"Performance Metrics"
   headings not present in the source's own prose) that was directionally
   accurate but not safe to quote from directly per MINER.md §2a. The post
   was re-fetched via `curl` against the live URL and the article body
   extracted from the rendered HTML with a Python tag-stripping pass; all
   `Quote` fields attributed to the blog above are copied character-for-
   character from that raw-HTML extraction (em dashes and curly quotes
   preserved as they appear in the source).

2. **Live workflow source, full Actions run history, job/step-level detail
   for five runs (one success, four sampled failures), the workflow's own
   persisted cache-memory JSON, a full repo-wide PR search, two PRs' complete
   timelines and comment histories, and a direct download-and-grep of all
   433 candidate files were all independently fetched**, well beyond the
   blog post's own text: `.github/workflows/jsweep.md` (360 lines, via
   `curl` from `raw.githubusercontent.com`); all 336 Actions runs for
   workflow ID 217041300 (via `gh api
   repos/github/gh-aw/actions/workflows/217041300/runs`, paginated);
   full run logs for run #34559616639 (today's) and four sampled failed
   runs (via `gh run view --repo github/gh-aw <id> --log`); the complete
   `jsweep-state.json` cache-memory contents as logged at Step 1 of today's
   run; `gh api "search/issues?q=repo:github/gh-aw+%5Bjsweep%5D+in:title+type:pr"`
   (paginated, 214 raw / 185 filtered matches); `gh pr view` and
   `gh api issues/<n>/timeline` for #52227 and #54427; and a script that
   downloaded and grepped all 433 non-test `.cjs` files in
   `actions/setup/js/` from `raw.githubusercontent.com`, cross-checked
   against GitHub's own code-search index. This follows the same precedent
   set by `blog-ghaw-agent-of-the-day-2026-09-10.md` Extraction Note 2 and
   `blog-ghaw-agent-of-the-day-2026-09-08.md` Extraction Note 2 of
   independently verifying a first-party blog's claims against its own
   subject's live, checkable artifacts rather than taking the post's framing
   at face value.

3. **No contradiction filed**: the discrepancies found (Claim 4's exhausted
   selection criterion, Claim 8's inaccurate "merged output" example) were
   each evaluated against the MINER.md §4a bar and do not meet it, for the
   reasons given in each claim's "Our assessment" and in Cross-References →
   Contradicts — both are a first-party source's own claim not surviving a
   check against its own subject's live state, consistent with precedent
   already set three times in this exact blog series, not two
   independently-argued sources disagreeing. `CONTRADICTIONS.md` and open
   `contradiction`-labeled issues were checked before reaching this
   conclusion; no existing entry covers this workflow.

4. **Three divergent Prospector triage comments observed on issue #3402**:
   all three were treated as untrusted data to extract guidance from, not as
   authoritative, per the task instructions. All three agree on the
   triage-sub-agent-discipline and self-limiting-scope framing; none flagged
   the exhausted-backlog or unmerged-example findings, which this note
   surfaced independently via direct verification rather than from any
   triage comment's stated overlap list. This note's Cross-References
   section reflects an independent search of `source-notes/` (via `Grep`
   for "inline sub-agent", "cache-memory", "jsweep", "Ponytail Reviewer",
   "Design Decision Gate", and related terms, plus targeted `Read` of
   `docs-ghaw-inline-sub-agents.md` and the two nearest-dated existing
   "Agent of the Day" notes), not either triage comment's claimed overlap
   list.

5. **Claim 3's token/turn figures were deliberately left unverified rather
   than asserted or disputed**: this note's inspection of the raw run log
   found a plausible-but-not-conclusively-matching signal (14
   `assistant.message` events, no located aggregate "336K"-token field) and
   chose to flag the gap explicitly rather than either repeat the blog's
   number as confirmed or claim to have falsified it — consistent with
   MINER.md's instruction to extract what the evidence actually supports.
