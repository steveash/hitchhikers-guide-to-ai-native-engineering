---
source_url: https://github.github.com/gh-aw/blog/2026-08-25-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – August 25, 2026: The Cookie Monster of Issues"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-08-25
date_extracted: 2026-08-26
last_checked: 2026-08-26
status: current
confidence_overall: emerging
issue: "#2965"
---

# Agent of the Day – August 25, 2026: The Cookie Monster of Issues

> Profiles Issue Monster, a 30-minute-scheduled issue-triage-and-dispatch
> workflow that curates candidate issues (via a pre-applied "cookie" label
> and a points-based priority score, both undocumented in the blog post
> itself but recovered from the live workflow source) and routes up to
> three topically-separated issues per run to the Copilot coding agent via
> `assign-to-agent`, gated by capacity checks (open-draft-PR count, failing
> CI, and a live scan for rate-limit signals on the agent's own recent PRs).
> Establishes topic-separation, not strict serialization, as this
> workflow's current concurrency-safety mechanism — which conflicts with an
> earlier corpus source's description of the same named workflow as
> strictly one-at-a-time (see Cross-References → Contradicts).

## Source Context

- **Type**: blog-post (an "Agent of the Day" entry from the official GitHub
  Agentic Workflows blog, bylined "Copilot" — the same recurring gh-aw
  convention for AI-authored posts documented across this series, e.g.
  `blog-ghaw-agent-of-the-day-2026-08-20.md`. Distinct from the weekly
  changelog format; one agent profiled per post with concrete run data.)
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team. The post cites five specific,
  independently-checkable GitHub Actions run IDs (32853285457, 32856106356,
  32859101860, 32821436131, 32816269740) and five specific issue numbers
  (#55788, #55770, #55716, #55771, #55768). High credibility for first-party
  platform claims. This note additionally fetched and cross-checked the
  live workflow source file at
  `raw.githubusercontent.com/github/gh-aw/main/.github/workflows/issue-monster.md`
  (816 lines, fetched via `curl`, 2026-08-26) — the blog post's own claims
  about permissions and dispatch cardinality are narrower and in one
  respect materially inconsistent with what the live source file shows
  (see Claim 5 and Extraction Notes).
- **Scope**: One day's aggregate of five real runs ("the last day") plus a
  static description of the workflow's guardrails and its `assign_to_agent`
  / `issues: read` / `pull-requests: read` posture. Does NOT cover: the
  "cookie" label pre-filter, the points-based priority scoring system, the
  retry-blocked-topic exclusion logic, the parent/sub-issue sibling-PR
  gating, or the `copilot-requests: write` permission on the main agent
  job — all of which exist in the live workflow file but are not mentioned
  in the blog post's own text.

## Extracted Claims

### Claim 1: Issue Monster runs on a 30-minute schedule and, per run, reads the issue tracker, checks capacity, and routes at most a narrow set of issues to the Copilot coding agent — described as a curation job, not a code-editing job

- **Evidence**: Direct first-party description of the agent's mission and
  cadence in the post's opening and "Agent of the Day" sections.
- **Confidence**: settled (explicit, first-party mission and schedule
  description)
- **Quote**: "It wakes up every 30 minutes, peers into the open issue
  tracker, picks out the tastiest morsel it can find, and hands it straight
  to the Copilot coding agent." / "Its entire job is curation: reading the
  room, checking capacity, and making a narrow, well-reasoned call about
  which issue is ready for an autonomous fix versus which one still needs a
  human's judgment."
- **Our assessment**: "Curation, not code-editing" is a precise
  characterization: Issue Monster never touches source code itself — its
  only write action is routing (`assign_to_agent`) plus a courtesy comment.
  This is the same curator/dispatcher role already named for this workflow
  in `blog-ghaw-issue-pr-mgmt.md` Claim 2 ("the task dispatcher — it assigns
  issues to the GitHub platform's asynchronous [Copilot coding agent]"), now
  with a specific cadence (30 minutes, vs. the January post's unspecified
  schedule) and explicit curation framing not present in that earlier post.
  For Ch02 (Harness Engineering): "curation as a named agent archetype" —
  distinct from both scheduled read-only *audit* agents (Architecture
  Guardian, `blog-ghaw-agent-of-the-day-2026-05-20.md` Claim 6) and
  scheduled write-enabled *codemod* agents (Dead Code Removal Agent,
  `blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 1) — a curator reads,
  scores, and routes, but the actual work (code changes) is delegated
  entirely to a downstream agent it dispatches to, not performed itself.

### Claim 2: The workflow skips an entire run if 5+ open draft PRs already exist from the Copilot agent, if there are no open issues to consider, or if key CI checks are failing — implemented as declarative frontmatter conditions, not agent reasoning

- **Evidence**: Blog post's guardrail description, corroborated exactly by
  the live workflow file's `on:` block.
- **Confidence**: settled (blog description directly confirmed by the
  fetched first-party workflow source)
- **Quote**: "It skips a run entirely if there are already five or more open
  draft PRs from `app/copilot-swe-agent`, skips if there are no open issues
  to consider, and skips if key CI checks (`build`, `test`, `lint-go`,
  `lint-js`) are failing."
- **Our assessment**: This is a live, production instance of the
  config-level skip-gate system documented generically in
  `docs-ghaw-frontmatter-full-reference.md` Claim 3 (`on.skip-if-match`,
  `on.skip-if-no-match`, `on.skip-if-check-failing`). The fetched workflow
  file confirms the exact mapping: `skip-if-match: {query: "is:pr is:open
  is:draft author:app/copilot-swe-agent", max: 5}` for the draft-PR cap,
  `skip-if-no-match: "is:issue is:open"` for the no-issues case, and
  `skip-if-check-failing: {include: [build, test, lint-go, lint-js],
  allow-pending: true}` for the CI-health gate (see Concrete Artifacts).
  This is a capacity-aware precondition: the workflow checks the health and
  load of the *downstream* agent (Copilot) it is about to dispatch more
  work to, not just its own preconditions. For Ch04 (Operations): add
  "check downstream agent capacity/health before dispatching more work" as
  a named precondition-gate pattern, concretely instantiated here as a
  `skip-if-match` query against the assignee's own open draft PRs.

### Claim 3: Before selecting a new issue to dispatch, the workflow performs a live scan for rate-limiting signals in the last hour's Copilot-authored PR comments, and skips scheduling more work if any are found

- **Evidence**: Blog post's explicit statement, corroborated by the live
  workflow's pre-activation step, which searches PRs authored by
  `app/copilot-swe-agent` created in the last hour and greps their comment
  timelines for a regex matching rate-limit language.
- **Confidence**: settled (blog claim; live source code confirms mechanism
  in detail — a GraphQL timeline query per candidate PR, matched against
  `/rate limit|API rate limit|secondary rate limit|abuse detection|\b429\b|too
  many requests/i`)
- **Quote**: "Before picking a new target, it even checks for recent
  rate-limiting signals on Copilot-authored PRs from the last hour, so it
  doesn't pile more work onto an agent that's already struggling."
- **Our assessment**: This is a *dynamic*, content-inspecting capacity
  check, distinct from Claim 2's static, count-based `skip-if-match` gates.
  Rather than counting how many PRs exist (a cheap search-API query), this
  check reads recent PR comment text for rate-limit language — a check that
  can only be expressed as custom pre-activation script logic (a
  `github-script` step), not as a declarative frontmatter skip condition.
  This is new to the corpus: no prior source documents an agent inspecting
  a *sibling* agent's recent output for distress signals before adding to
  its queue. For Ch02/Ch04: name this "peer-health content scan" as a
  capacity-gating technique complementary to the static skip-if-match
  count-based gates — useful when the signal of overload is qualitative
  (error text in a comment) rather than quantitative (a PR count).

### Claim 4: Across five real runs in one day, the workflow consumed 350k tokens and made 125 GitHub API calls total, completed with zero errors and zero warnings, and produced write-capable safe outputs in two of the five runs while the other three stayed strictly read-only

- **Evidence**: Direct aggregate metrics statement in the blog post, plus
  five per-run summaries (durations, outcomes) immediately preceding it.
- **Confidence**: settled (specific aggregate figures tied to five
  individually described, named Actions runs)
- **Quote**: "Across all five runs, the workflow burned through 350k tokens
  and racked up 125 GitHub API calls — mostly reads, scanning issue bodies,
  checking recent PR activity, and verifying rate-limit safety before ever
  touching the `assign_to_agent` safe output. Of the five runs, two executed
  write-capable safe outputs (the assignments and comments above) while
  three stayed strictly read-only, quietly confirming there was nothing
  worth biting into that cycle. Zero errors, zero warnings, across the
  board."
- **Our assessment**: The 3-read/2-write split over five runs in one day is
  a concrete operational baseline for a high-frequency (30-minute cadence)
  curation agent — a materially higher run frequency than any prior
  "Agent of the Day" profile (Architecture Guardian: weekdays ~14:00 UTC;
  Dead Code Removal: daily; Issue Arborist: nightly). At 48 possible runs
  per day, a workflow that only writes 2 out of 5 sampled runs (~40%) is
  read-only the majority of the time by design, not by malfunction — the
  guardrails in Claims 2–3 are working as intended rather than the agent
  simply finding nothing. For Ch04 (Operations): record this as the first
  corpus baseline for a sub-hourly-cadence curation agent: ~70k
  tokens/run average (350k / 5) and ~25 API calls/run average (125 / 5),
  with a majority-read-only run mix as the expected steady state rather
  than an anomaly.

### Claim 5: The blog post states Issue Monster "only has `issues: read` and `pull-requests: read` permissions directly," but the live workflow's top-level `permissions:` block (governing the job that actually calls `assign_to_agent`) additionally grants `contents: read` and `copilot-requests: write`

- **Evidence**: Blog post's direct permissions claim, checked against two
  separate `permissions:` blocks in the fetched workflow source: a nested
  block under `on:` (lines 19–21, scoping the pre-activation search step to
  `issues: read` / `pull-requests: read` only) and a separate top-level
  block (lines 497–501, scoping the main agentic job) reading `contents:
  read`, `issues: read`, `pull-requests: read`, `copilot-requests: write`.
- **Confidence**: settled for the discrepancy itself (both permission
  blocks are read directly from the first-party workflow source, not
  inferred); emerging for whether this is best read as a blog imprecision
  or a legitimate simplification (the blog may be describing the
  pre-activation search step's scope, which does match its claim exactly,
  rather than the main job's scope)
- **Quote**: "Issue Monster only has `issues: read` and `pull-requests:
  read` permissions directly — it never edits code itself." (blog post)
- **Our assessment**: The blog's claim is accurate for the pre-activation
  search step but incomplete for the main agentic job, which needs
  `copilot-requests: write` to actually call the `assign_to_agent` safe
  output (assigning an issue to Copilot is itself a `copilot-requests`
  write, distinct from `contents`/`issues`/`pull-requests` writes) — and
  `contents: read` presumably to read repository files for context. This is
  not a contradiction rising to the MINER.md §4a bar (it is one blog post's
  own claim being narrower than its own linked artifact, not two
  independently-argued sources disagreeing), but it is a precision gap
  worth flagging: "never edits code itself" (true — no `contents: write`
  anywhere in the file) is a different and more defensible claim than "only
  has issues:read and pull-requests:read" (not true for the main job). For
  Ch03 (Safety and Verification): when citing an agent's permission
  footprint from a blog description, prefer the narrower, verifiable claim
  ("never has write access to repository contents") over a specific
  enumerated permission list, which this example shows can omit permissions
  that exist for a different purpose (here, `copilot-requests: write` for
  the dispatch action itself, not for code editing).

### Claim 6: The workflow's own written mission is to assign "up to three" topically-separated issues per run, and its `assign-to-agent` safe output is explicitly configured with `max: 3` — an override of the platform's documented `max: 1` default for that operation type — using topic separation, not serialization, as the concurrency-safety mechanism

- **Evidence**: Live workflow source: `safe-outputs: assign-to-agent: {max:
  3, target: "*", allowed: [copilot], ignore-if-error: true}`; prompt body:
  "Find up to three issues that need work... processing up to three
  separate issues at a time every hour, ensuring they are completely
  different in topic to avoid conflicts," with an explicit "Topic
  Separation Required" rule set (different codebase areas, no overlapping
  file changes, no shared parent task). The blog post's own Run
  32856106356 assigned three issues (#55788, #55770, #55716) in a single
  pass, consistent with this being real production behavior, not just
  aspirational prompt text.
- **Confidence**: settled (directly read from the first-party workflow
  source file's frontmatter and prompt body, and independently corroborated
  by the blog's own reported run data)
- **Quote**: (no direct quote from the blog post itself for the "up to
  three" / topic-separation mechanism — the blog post never states the
  per-run cap or the topic-separation rule explicitly; this claim is
  sourced from the live workflow file, cited by section name per MINER.md
  §4b: `.github/workflows/issue-monster.md`, "Your Mission" and "Select Up
  to Three Issues to Work On" sections)
- **Our assessment**: This is the most consequential finding from
  cross-checking the live source: `docs-ghaw-rate-limiting-controls.md`
  Claim 6 documents `assign-to-agent` defaulting to `max: 1` platform-wide,
  specifically "to prevent agent cascades," and `docs-ghaw-assign-to-
  copilot.md` Claim 5 documents the same default with the warning that
  "teams implementing bulk-assignment workflows... must explicitly raise
  `max`." Issue Monster is a concrete, production example of exactly that
  override, paired with a substitute safety mechanism (mandatory topic
  separation across the batch) rather than the `max:1` default's cascade
  prevention. This directly contradicts, however, `blog-ghaw-issue-pr-
  mgmt.md` Claim 2, which describes this same named workflow as
  dispatching "one at a time" specifically "to prevent... parallel
  execution chaos" — a strict-serialization design, not a
  topic-partitioned-batch design. See Cross-References → Contradicts;
  filed as contradiction issue #2979. For Ch02/Ch04: once #2979 is
  resolved, document `max:N` override + explicit non-overlap constraint (in
  this case, topic separation) as an alternative to strict `max:1`
  serialization for multi-agent dispatch — but do not present Issue Monster
  as an example of either pattern until the contradiction is resolved,
  since the two corpus sources currently disagree about which pattern this
  specific workflow uses.

### Claim 7: The candidate issue pool the workflow ever considers is pre-filtered to only issues carrying a "cookie" label — described in the live source as marking "approved work queue items from automated workflows" — a curation-of-a-curation step not mentioned anywhere in the blog post

- **Evidence**: Live workflow source, "Filtering Applied" section: "Only
  open issues **with 'cookie' label** (indicating approved work queue items
  from automated workflows)," alongside a longer exclusion list (wontfix,
  duplicate, invalid, question, discussion, needs-discussion, blocked,
  on-hold, waiting-for-feedback, needs-more-info, no-bot, no-campaign,
  copilot-retry-blocked labels; issues with campaign:* labels; issues with
  existing assignees; issues with sub-issues; issues with closed/merged or
  open Copilot PRs; stale duplicates of newer same-topic issues) and a
  points-based priority scoring system (community +60, good-first-issue
  +50, security +45, bug +40, documentation +35, enhancement/feature +30,
  performance +25, tech-debt/refactoring +20, any priority label +10, age
  bonus +0–20).
- **Confidence**: settled (directly read from the first-party workflow
  source's "Filtering Applied" and "Scoring System" sections; not
  mentioned, even in summary, anywhere in the blog post's own text)
- **Quote**: (no direct quote from the blog post — the blog post never
  mentions a label pre-filter or scoring system at all; sourced from the
  live workflow file, cited by section name per MINER.md §4b: "Filtering
  Applied" and "Scoring System" sections of `.github/workflows/issue-monster.md`)
- **Our assessment**: This significantly changes the mental model the blog
  post alone would produce. The blog's framing ("peers into the open issue
  tracker, picks out the tastiest morsel") implies Issue Monster does its
  own open-ended triage across the full issue tracker. In fact, its
  candidate pool has already been narrowed by an upstream, unnamed process
  that applies a "cookie" label to mark "approved work queue items" — Issue
  Monster's own job is closer to *ranking and dispatching within a
  pre-approved queue* than open-ended tracker-wide curation. This is a
  materially different (though not necessarily contradictory) description
  of the workflow's actual scope than the blog conveys, and it means the
  "curation" framing in Claim 1 undersells how much of the actual filtering
  work happens before Issue Monster ever runs. For Ch02 (Harness
  Engineering): when documenting a "curation agent" pattern from this
  workflow, note that its curation is a second-stage ranking/dispatch step
  over an already-labeled candidate pool, not first-stage open-ended
  triage — practitioners modeling a similar dispatcher should decide
  explicitly whether their agent does its own first-pass filtering or
  consumes a pre-filtered queue (as this one does via the "cookie" label).
  This is a novel labeling-as-queue-approval pattern not documented
  elsewhere in the corpus.

### Claim 8: Issues whose normalized title matches two or more Copilot PRs previously closed without merging are excluded from assignment and instead receive a comment requesting human review — a "retry-blocked" safeguard against repeatedly re-dispatching a topic the agent has already failed at

- **Evidence**: Live workflow source, step "4a. Handle Retry-Blocked
  Issues": "The pre-activation job lists issues whose topic already has two
  or more Copilot PRs closed without merging. Never assign these to
  Copilot," paired with a templated human-escalation comment.
- **Confidence**: settled (directly read from the first-party workflow
  source; not mentioned in the blog post)
- **Quote**: "This topic already has prior Copilot pull requests that were
  closed without merging. Automatic re-dispatch is disabled to avoid
  spending another agent session on a blocked topic." (comment template
  embedded in the workflow source, cited by section name: "4a. Handle
  Retry-Blocked Issues," `.github/workflows/issue-monster.md`)
- **Our assessment**: This is a distinct restraint mechanism from Claims 2–3
  (which gate on *system-wide* downstream capacity) — this one gates on a
  *per-topic* failure history, refusing to keep re-spending agent sessions
  on a specific issue the agent has already failed to resolve twice. It
  parallels the "agent restraint" principle named in
  `blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 4 (Dead Code Removal
  Agent declining to force a PR when it can't complete cleanly — "that
  restraint is a feature, not a gap"), but applied to a dispatcher deciding
  *whether to keep re-trying a downstream agent* rather than to a codemod
  agent deciding whether to submit its own PR. For Ch03 (Safety and
  Verification): add "per-topic retry-exhaustion tracking" (N failed
  attempts on the same normalized topic → stop auto-dispatching, escalate
  to human) as a named restraint pattern for any agent that repeatedly
  dispatches work to a downstream autonomous agent, distinct from
  system-wide capacity gating.

## Concrete Artifacts

### Issue Monster: Five-Run Daily Snapshot (as reported in the blog post)

```
Run 32853285457  — 8.9 min, 3 turns — evaluated tracker, no strong-enough
                   candidate this cycle (read-only)
Run 32856106356  — assigned 3 issues in one pass: #55788, #55770, #55716
                   (each HIGH-confidence, "clearly scoped, independent
                   candidates for automated resolution"); posted the
                   "Om nom nom!" comment on each
Run 32859101860  — assigned 2 issues: #55771, #55768
Run 32821436131  — 6-8 min, clean/error-free (read-only)
Run 32816269740  — 6-8 min, clean/error-free (read-only)

Aggregate: 350k tokens, 125 GitHub API calls (mostly reads), 2/5 runs
write-capable, 3/5 runs strictly read-only, 0 errors, 0 warnings.
```
*Source: GitHub Agentic Workflows blog, "Agent of the Day – August 25, 2026"*

### Issue Monster: Workflow Frontmatter (excerpted, live source)

```yaml
emoji: "👾"
name: Issue Monster
description: The Cookie Monster of issues - assigns issues to Copilot coding agent one at a time
on:
  workflow_dispatch:
  schedule: every 30m
  skip-if-match:
    query: "is:pr is:open is:draft author:app/copilot-swe-agent"
    max: 5
  skip-if-no-match: "is:issue is:open"
  skip-if-check-failing:
    include: [build, test, lint-go, lint-js]
    allow-pending: true
  permissions:                # scopes the pre-activation search step only
    issues: read
    pull-requests: read

permissions:                  # scopes the main agentic job
  contents: read
  issues: read
  pull-requests: read
  copilot-requests: write

features:
  gh-aw-detection: true

model: copilot/mai-code-1-flash-picker
engine: codex
imports:
  - shared/mcp-pagination.md
  - shared/github-guard-policy.md
  - shared/activation-app.md
  - shared/otlp.md
timeout-minutes: 30

tools:
  cli-proxy: true
  github:
    mode: gh-proxy
    min-integrity: approved
    toolsets: [issues]

safe-outputs:
  assign-to-agent:
    max: 3
    target: "*"           # requires explicit issue_number in agent output
    allowed: [copilot]
    ignore-if-error: true
  add-comment:
    max: 3
    target: "*"
  messages:
    footer: "> 🍪 *Om nom nom by [{workflow_name}]({run_url})*{ai_credits_suffix}{history_link}"
    run-started: "🍪 ISSUE! ISSUE! [{workflow_name}]({run_url}) hungry for issues on this {event_type}! Om nom nom..."
    run-success: "🍪 YUMMY! [{workflow_name}]({run_url}) ate the issues! That was DELICIOUS! Me want MORE! 😋"
    run-failure: "🍪 Aww... [{workflow_name}]({run_url}) {status}. No cookie for monster today... 😢"
evals:
  - id: issue_assigned
    question: Did the agent assign at least one issue to the Copilot coding agent, or correctly skip when no suitable issues were found?
  - id: single_issue_scoped
    question: Does the agent output show that at most one issue was assigned to Copilot per run?
```
*Source: `.github/workflows/issue-monster.md`, fetched via `curl` from
`raw.githubusercontent.com/github/gh-aw/main/`, 2026-08-26. Note the
description field's own text ("one at a time") and the `single_issue_scoped`
eval question ("at most one issue... per run") both still describe
strict single-issue dispatch, while the mission body and `max: 3`
configuration describe up-to-three-per-run batching — an internal
inconsistency in the source file itself, separate from the blog-vs-note
contradiction filed as issue #2979 (see Extraction Notes).*

### Issue Monster: Candidate Filtering and Scoring (live source, "Filtering Applied" / "Scoring System")

```
Required:      "cookie" label present
Excluded labels: wontfix, duplicate, invalid, question, discussion,
                needs-discussion, blocked, on-hold, waiting-for-feedback,
                needs-more-info, no-bot, no-campaign, copilot-retry-blocked
Excluded:      campaign:* labeled issues; issues with existing assignees;
                issues with sub-issues; issues with closed/merged PRs;
                issues with open Copilot PRs; stale duplicates of newer
                same-topic issues
Retry-blocked: issues whose normalized title matches >=2 Copilot PRs
                previously closed without merging (human review required)

Scoring (points, higher = dispatched first):
  Community                +60
  Good first issue         +50
  Security                 +45
  Bug                      +40
  Documentation             +35
  Enhancement/Feature       +30
  Performance                +25
  Tech-debt/Refactoring     +20
  Any priority label         +10
  Age bonus                 +0-20
```
*Source: `.github/workflows/issue-monster.md`, "Filtering Applied" and
"Scoring System" sections, fetched 2026-08-26. None of this appears in the
blog post.*

### Issue Monster: Comment Template on Assignment (live source, matches blog's quoted comment)

```
safeoutputs/add_comment(item_number=<issue_number>, body="🍪 **Issue Monster
selected this for Copilot**\n\nI've identified this issue as a good
candidate for automated resolution and requested assignment to the Copilot
coding agent.\n\nIf assignment succeeds, the Copilot coding agent will
analyze the issue and create a pull request with the fix.\n\nOm nom nom!
🍪")
```
*Source: `.github/workflows/issue-monster.md`, step "5. Add Comment to Each
Assigned Issue," fetched 2026-08-26.*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-issue-pr-mgmt.md` Claim 2 (Issue Monster named as "the task
    dispatcher" that assigns issues to the Copilot coding agent): Claim 1
    here corroborates the core curator/dispatcher role seven months later,
    adding a specific 30-minute cadence not stated in the January post — but
    see Contradicts below for where the two posts diverge on dispatch
    cardinality.
  - `docs-ghaw-frontmatter-full-reference.md` Claim 3 (six conditional
    skip options — `skip-if-match`, `skip-if-no-match`,
    `skip-if-check-failing`, etc. — forming a precondition-gate system that
    runs before the AI engine is invoked): Claim 2 here is a live,
    production instance of exactly this mechanism, with the fetched
    workflow file confirming the precise query/field mapping for all three
    gates the blog post describes in prose.
  - `docs-ghaw-assign-to-copilot.md` Claim 3 (`target: "*"` requires the
    agent to output explicit `issue_number`/`pull_number` values, described
    there as "the mechanism underlying Issue Monster-style workflows"):
    Claim 6 here confirms this prediction directly — the live Issue Monster
    workflow does use `target: "*"` in its `assign-to-agent` safe-output
    configuration.
  - `docs-ghaw-rate-limiting-controls.md` Claim 6 (`assign-to-agent`
    defaults to `max: 1` platform-wide "to prevent agent cascades") and
    `docs-ghaw-assign-to-copilot.md` Claim 5 (same default, with the note
    that bulk-assignment workflows "must explicitly raise `max`"): Claim 6
    here is a concrete, named production example of exactly that override
    (`max: 3`), paired with an explicit substitute safety mechanism (topic
    separation) rather than the default's blanket cascade prevention.
  - `blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 4 (Dead Code Removal
    Agent's "restraint is a feature, not a gap" — declining to force a PR
    when cleanup can't complete safely): Claim 8 here (retry-blocked-topic
    exclusion) extends the same restraint principle to a dispatcher
    context — declining to keep re-assigning a topic the downstream agent
    has already failed at twice.

- **Contradicts**:
  - `blog-ghaw-issue-pr-mgmt.md` Claim 2 (Issue Monster assigns issues to
    the Copilot coding agent "one at a time," explicitly to prevent "the
    chaos of parallel work on the same codebase" — a strict-serialization
    design). Claim 6 here shows the same named production workflow
    currently configured for `max: 3` with topic separation (not
    serialization) as the concurrency-safety mechanism, and the blog's own
    reported Run 32856106356 assigning three issues in a single pass. This
    is a genuine, unresolved contradiction about the same workflow's
    current dispatch cardinality and safety mechanism — **filed as
    contradiction issue #2979**
    (`steveash/hitchhikers-guide-to-ai-native-engineering#2979`). No
    verdict is asserted in this note; see that issue and its eventual
    CONTRADICTIONS.md entry for resolution.
  - No other contradictions filed. Reviewed `CONTRADICTIONS.md` (no
    existing entries on Issue Monster, issue-triage dispatch, or
    `assign-to-agent` cardinality prior to filing #2979) and the source
    notes cited throughout this note.

- **Extends**:
  - `docs-ghaw-frontmatter-full-reference.md` Claim 3: extends the abstract
    skip-gate taxonomy with a fully worked, three-gate production example
    (draft-PR count cap, no-open-issues check, CI-health check) plus a
    fourth gate (Claim 3 here, the peer-health content scan) that cannot be
    expressed as a declarative skip condition at all.
  - `docs-ghaw-assign-to-copilot.md` Claims 3 and 5: extends the abstract
    `target: "*"` and `max` override documentation with a live, named
    workflow using both.
  - `blog-ghaw-agent-of-the-day-2026-05-20.md` Claim 6 (Architecture
    Guardian's read-only analysis posture as a named agent category) and
    `blog-ghaw-agent-of-the-day-2026-05-28.md` Claim 1 (Dead Code Removal
    Agent as a scheduled write-enabled codemod archetype): Issue Monster
    extends the corpus's agent-archetype taxonomy with a third position —
    scheduled, technically write-enabled (it does call safe outputs) but
    never touches repository contents; its only write authority is
    dispatch (`copilot-requests: write`) and commenting, not code
    modification.

- **Novel**:
  - **Curation as a distinct agent archetype**, separate from read-only
    audit and write-enabled codemod agents (Claim 1): a scheduled agent
    whose entire authority is routing pre-vetted work to a different,
    downstream autonomous agent, never editing code itself.
  - **Peer-health content scan as a dynamic capacity-gating technique**
    (Claim 3): inspecting a sibling agent's recent PR comment text for
    distress-signal language before adding to its queue — not expressible
    as a static frontmatter skip condition, and not documented in any prior
    corpus source.
  - **Label-gated queue approval ("cookie" label) as a second-stage
    curation pattern** (Claim 7): the dispatcher only ever sees issues an
    upstream, unnamed process has already approved via a specific label —
    a queue-approval pattern not documented elsewhere in the corpus, and
    entirely absent from the blog post's own description of the workflow.
  - **Per-topic retry-exhaustion tracking** (Claim 8): refusing to
    re-dispatch a topic after two failed downstream attempts, with an
    explicit human-escalation comment — a restraint pattern distinct from
    system-wide capacity gating (Claims 2–3).
  - **A documented, named production override of the `assign-to-agent`
    `max: 1` default**, using topic separation as the substitute safety
    mechanism (Claim 6) — though this claim is currently in tension with
    an earlier corpus description of the same workflow; see Contradicts.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add "curation agent" as a named
  archetype distinct from read-only audit and write-enabled codemod agents
  (Claim 1) — a scheduled agent whose only authority is routing pre-vetted
  candidates to a separate downstream autonomous agent. Add "peer-health
  content scan" (Claim 3) as a capacity-gating technique for any dispatcher
  that feeds work to another agent, for use when the overload signal is
  qualitative (error text) rather than a simple count expressible as a
  `skip-if-match` query. Add "label-gated queue approval" (Claim 7) as a
  pattern for separating first-pass filtering (done by a separate,
  unnamed upstream process via a label) from second-pass ranking/dispatch
  (done by the curator agent itself) — flag that Issue Monster's own blog
  coverage did not mention this, so guide text citing it as a fully
  self-contained triage example would be incomplete without checking the
  live workflow source.

- **Chapter 03 (Safety and Verification)**: Add per-topic retry-exhaustion
  tracking (Claim 8) as a restraint pattern for dispatcher agents — after N
  failed downstream attempts on the same normalized topic, stop
  auto-dispatching and escalate to a human, rather than repeatedly spending
  downstream agent sessions on a topic that keeps failing. Note the
  permission-footprint precision issue in Claim 5: prefer verifiable
  negative claims ("never has write access to repository contents") over
  enumerated permission lists when summarizing an agent's authority from a
  blog post, since this example shows a blog's own enumerated list can omit
  permissions that exist for a non-obvious purpose (dispatch write, not
  code write).

- **Chapter 04 (Operations)**: Add the five-run daily snapshot (Claim 4) as
  the corpus's first baseline for a sub-hourly-cadence (30-minute) curation
  agent: ~70k tokens/run and ~25 API calls/run average, with a
  majority-read-only run mix (3 of 5) as the expected steady state rather
  than a sign of underuse. **Do not cite Issue Monster's dispatch
  cardinality (one-at-a-time vs. up-to-three-topic-separated) as settled
  guide content until contradiction issue #2979 is resolved** — the two
  corpus sources currently disagree about this workflow's core concurrency
  design.

## Extraction Notes

1. **WebFetch summary used only as a first pass, not for quotes**: An
   initial WebFetch call returned a structured summary of the post. Per
   MINER.md §2a, the page was then re-fetched directly via `curl` and
   parsed with BeautifulSoup (`div.sl-markdown-content`), and all quotes
   above are copied character-for-character from that raw-HTML extraction,
   not reconstructed from the WebFetch summary. The full post is
   short (well under 500 words) and was captured in one fetch; no
   pagination or truncation was observed.

2. **One substantive sub-page fetched, within MINER.md §1's "up to 5"
   budget**: the live workflow definition at
   `raw.githubusercontent.com/github/gh-aw/main/.github/workflows/issue-monster.md`
   (816 lines) was fetched via `curl` and read in full. This is the same
   practice used in `blog-ghaw-weekly-2026-08-17.md` (fetching
   `issue-arborist.md`) and `blog-ghaw-agent-of-the-day-2026-08-20.md`'s
   cross-referenced predecessor note. This single sub-page fetch is what
   surfaced Claims 5–8 and the contradiction filed as issue #2979 — none of
   that material is present in the blog post's own text.

3. **Contradiction filed before writing this note, per MINER.md §4a**: the
   dispatch-cardinality conflict with `blog-ghaw-issue-pr-mgmt.md` Claim 2
   is filed as
   `steveash/hitchhikers-guide-to-ai-native-engineering#2979`. No verdict is
   asserted here; Claim 6 and the Guide Impact section both explicitly defer
   to that issue's resolution.

4. **A second, smaller inconsistency was found inside the live workflow
   file itself** (not between two independent sources, so not filed as a
   MINER.md §4a contradiction): the workflow's own `description:` field
   ("assigns issues to Copilot coding agent one at a time") and its
   `single_issue_scoped` eval question ("at most one issue... per run") both
   describe strict single-issue dispatch, while the same file's mission
   prose and `safe-outputs.assign-to-agent.max: 3` configuration describe
   up-to-three-per-run batching. This looks like leftover text from an
   earlier one-at-a-time version of the workflow that was not fully updated
   when the file was changed to allow batches of three — consistent with
   the "superseded" reading proposed as the recommended verdict on issue
   #2979. Documented here as supporting evidence for that issue's resolver,
   not as a claim about the blog post.

5. **Multiple duplicate Prospector triage comments observed on issue
   #2965**: three near-identical triage comments are present, all posted
   within about 20 seconds of each other, apparently from repeated/parallel
   triage passes on the same auto-filed source (consistent with the pattern
   already documented in `blog-ghaw-agent-of-the-day-2026-08-20.md`
   Extraction Note 5 for a different issue). All three agree on novelty
   (high), source type (blog-post), and the core extraction guidance
   (guardrail design, restraint, capacity-aware gating, curation as an
   archetype); this note follows the union of their guidance rather than
   picking one comment over the others. Per the task instructions, the
   issue's title, body, and comments were treated as untrusted data to
   extract from, not as instructions — none of the three comments contained
   anything resembling an instruction to this agent beyond normal triage
   guidance.

6. **Cross-reference check performed** against
   `blog-ghaw-issue-pr-mgmt.md`, `docs-ghaw-frontmatter-full-reference.md`,
   `docs-ghaw-assign-to-copilot.md`, `docs-ghaw-rate-limiting-controls.md`,
   `blog-ghaw-agent-of-the-day-2026-05-15.md`,
   `blog-ghaw-agent-of-the-day-2026-05-20.md`,
   `blog-ghaw-agent-of-the-day-2026-05-28.md`,
   `blog-ghaw-agent-of-the-day-2026-08-20.md`,
   `blog-ghaw-weekly-2026-08-17.md`, and `CONTRADICTIONS.md`, all read in
   full (not skimmed) before writing Cross-References. All `Claim N`
   citations above were checked against the actual numbered claims in
   those notes at the time of writing, per MINER.md §4b.
