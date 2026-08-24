---
source_url: https://github.github.com/gh-aw/blog/2026-08-24-weekly-update/
source_type: blog-post
title: "Weekly Update – August 24, 2026 (GitHub Agentic Workflows)"
author: GitHub Agentic Workflows team (gh-aw); byline "Copilot"
date_published: 2026-08-24
date_extracted: 2026-08-24
last_checked: 2026-08-24
status: current
confidence_overall: emerging
issue: "#2909"
---

# Weekly Update – August 24, 2026 (GitHub Agentic Workflows)

> Three v0.87.x pre-releases (v0.87.1, v0.87.2, v0.87.4) ship pre-create
> pull-request "steering" — agents can read reviewer feedback left on a
> pre-created PR without silently gaining broader permissions — plus a new
> `gh aw models` CLI command, Copilot SDK startup-crash diagnostics, and
> automatic pull-request-review-dismissal ingestion. The Agent of the Week
> spotlight profiles PR Sous Chef, the workflow that shipped the steering
> feature and then used it on itself.

## Source Context

- **Type**: blog-post (weekly changelog/update from the official GitHub
  Agentic Workflows blog; a short intro, a "Release Highlights" section of
  four bullets, a "Notable Pull Requests" section of five bullets, an
  "Agent of the Week: PR Sous Chef" spotlight, and a "Try It Out" closer)
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team. The on-page byline names the
  author as "Copilot" — the same non-human byline pattern documented in
  prior weekly notes (e.g. `blog-ghaw-weekly-2026-08-17.md`). Fetched via
  `curl` and parsed with a Python HTML-stripping pass (not a WebFetch
  summary) to preserve exact wording — see Extraction Notes.
- **Scope**: One "Release Highlights" section naming four PRs from the
  v0.87.4 pre-release line (#55171, #55148, #55149, #55180), one "Notable
  Pull Requests" section of five unlinked-in-prose merges (PR numbers
  recovered from the page's anchor hrefs — see Extraction Notes), and one
  Agent of the Week spotlight on PR Sous Chef. Does NOT cover: the full
  contents of v0.87.1/v0.87.2 individually (the post only names the
  combined "v0.87.4 line"); a changelog/release-notes page for v0.87.4 was
  not linked from this post the way prior weekly posts linked a GitHub
  Releases page, so no expanded "Internal & Security" section could be
  cross-checked this week (see Extraction Notes).

## Extracted Claims

### Claim 1: `safe-outputs.create-pull-request.pre-create.steer: true` lets an agent read user feedback left in PR comments and review comments on a pre-created pull request, without the compiler silently expanding the workflow's permissions (PR #55171)

- **Evidence**: "Release Highlights" section, first bullet; corroborated by
  the implementing PR's own description, fetched via `gh pr view
  55171 --repo github/gh-aw`.
- **Confidence**: settled (specific PR, specific config key, first-party PR
  description with concrete YAML and validation behavior)
- **Quote**: "Pre-create pull request steering (#55171): safe-outputs.create-pull-request.steer: true pre-creates a PR and lets agents read user feedback left in PR comments and review comments — without silently expanding workflow permissions. It requires explicit pull-requests: read and injects prompting so the agent knows to look for the steer keyword."
- **Our assessment**: This is the first corpus documentation of a "steer"
  mechanism for `create-pull-request` safe outputs. The PR body (fetched
  separately) shows the actual config path is nested under `pre-create` as
  an object — `pre-create: {steer: true}` — not a top-level
  `create-pull-request.steer` key as the blog prose's URL-like phrasing
  suggests; see Concrete Artifacts for the exact YAML and Extraction Notes
  for the discrepancy. The design pattern (explicit permission required,
  no silent escalation, compiler-enforced) matches gh-aw's established
  "external/explicit-permission-required for higher-impact capability"
  posture also seen in `blog-ghaw-weekly-2026-08-17.md` Claim 1
  (`approve-workflow-run` requiring an explicit external token). For Ch03
  (Workflows & Orchestration): add pre-create PR steering as a pattern for
  incorporating human review feedback into an agent's PR-editing loop
  without a full re-run; for Ch04 (Safety & Guardrails): note the
  compiler-enforced permission-gating design (fails to compile without
  `pull-requests: read`, not auto-added) as another instance of gh-aw's
  "require, don't silently grant" pattern for permission-adjacent safe
  outputs.

### Claim 2: The `pre-create.steer` compiler validator rejects a workflow at compile time if `steer: true` is configured without an effective `pull-requests: read` (or higher) permission, and does not auto-add the permission itself

- **Evidence**: PR #55171 description, "Validation" bullet list, fetched
  via `gh pr view 55171 --repo github/gh-aw`. Not stated in the blog post
  itself.
- **Confidence**: settled (first-party PR description, explicit validator
  behavior stated)
- **Quote**: "Reports a compiler error when `steer: true` is used without effective `pull-requests: read` or higher.\n  - Does not auto-add workflow permissions."
- **Our assessment**: This is a concrete, named compile-time guardrail
  (distinct from the runtime eligibility checks documented for
  `approve-workflow-run` in `blog-ghaw-weekly-2026-08-17.md` Claims 1–2) —
  gh-aw refuses to compile a workflow into an under-permissioned but
  behaviorally-broken state, rather than silently degrading or
  auto-granting. For Ch04: add this as a second, compile-time-class example
  (alongside `approve-workflow-run`'s runtime eligibility checks) of gh-aw
  refusing rather than silently working around a permission gap for a
  capability that reads reviewer-authored content.

### Claim 3: Steering also configures the GitHub MCP server to expose the pull-request read toolset, adding `pull_request_read` to an explicit GitHub MCP allowlist when one is configured, and updates the pre-created PR's body text to indicate whether steering is enabled

- **Evidence**: PR #55171 description, "Agent access" and "Prompting and PR
  body" bullets.
- **Confidence**: settled (first-party PR description, specific tool name
  and specific behavior)
- **Quote**: "Ensures the GitHub MCP server exposes the pull request toolset for steering.\n  - Adds `pull_request_read` when an explicit GitHub MCP allowlist is configured.\n  - Injects steering instructions telling the agent to query user-authored PR comments and review comments containing the `steer` keyword.\n  - Updates the pre-created PR body to indicate whether steering is enabled."
- **Our assessment**: The `steer` keyword requirement (the agent is
  instructed to look for comments containing that literal word) is a
  narrow, deliberate signal — it means ordinary PR discussion does not
  accidentally get treated as a steering instruction, only comments the
  reviewer explicitly flags. No existing corpus note documents a
  keyword-gated human-to-agent feedback channel of this shape. For Ch03:
  add the `steer`-keyword convention as a concrete pattern for
  disambiguating "feedback meant for the agent to act on" from general PR
  conversation.

### Claim 4: `gh aw models` is a new CLI command (registered under an "analysis" command group) that surfaces embedded catalog pricing (input/output/cache-read/cache-write/reasoning token prices), built-in model-alias resolution targets, and models actually observed in a repository's automation artifacts, in one place (PR #55148)

- **Evidence**: "Release Highlights" section, second bullet; corroborated by
  the implementing PR's own description, fetched via `gh pr view
  55148 --repo github/gh-aw`.
- **Confidence**: settled (specific PR, specific CLI surface, first-party PR
  description with flag list and example invocation)
- **Quote**: "gh aw models (#55148): a new CLI command surfaces catalog pricing, alias resolution, and observed automation models in one place."
- **Our assessment**: This is the first corpus mention of a dedicated
  model-inventory CLI command. It complements, rather than duplicates,
  the recurring "Model inventory refresh" changelog bullets seen in prior
  weekly notes (e.g. `blog-ghaw-weekly-2026-08-17.md` Claim 5, adding
  Gemini 3.7 Flash and Grok 4.6 to the supported list) and the
  `COPILOT_PROVIDER_WIRE_API` auto-configuration fix in
  `blog-ghaw-weekly-2026-07-20.md` Claim 2 — those are changelog-level
  facts about the catalog changing; `gh aw models` is a new tool for
  *querying* that catalog plus what a given repo's automation runs have
  actually used, aggregated from `summary.json` token-usage data, per-run
  token-usage artifacts, and `awf-reflect.json` endpoint model lists (per
  the PR body's "Observed-model intelligence from automation" section —
  see Concrete Artifacts). For Ch02 (Harness Engineering): add `gh aw
  models --json --refresh-count 50` as a concrete command for auditing
  which models a fleet of agentic workflows is actually running, versus
  what's configured/aliased, when writing guide material on model-cost
  governance.

### Claim 5: A pre-ready Copilot SDK headless-server crash now surfaces the SDK's own stderr tail (e.g. panic/assertion output) in the reported error, instead of only the exit signal (PR #55149)

- **Evidence**: "Release Highlights" section, third bullet; corroborated by
  the implementing PR's own description and example error shape, fetched
  via `gh pr view 55149 --repo github/gh-aw`.
- **Confidence**: settled (specific PR, first-party PR description with a
  concrete before/after failure-mode description and an example error
  string)
- **Quote**: "Copilot SDK startup diagnostics (#55149): pre-ready crashes now surface the Copilot SDK's startup stderr, making a previously opaque failure mode much easier to debug."
- **Our assessment**: The PR body states the prior behavior plainly:
  "Copilot SDK headless server crashes before readiness only reported the
  exit signal, hiding the SDK's own panic/assertion output" — i.e. a
  `SIGABRT` before the server was ready to accept connections previously
  surfaced as an opaque signal number with no further context. This is a
  narrow but concrete observability fix in the same family as other
  engine-diagnostics improvements in the corpus (e.g. the Aider
  silent-no-safe-outputs fix in `blog-ghaw-weekly-2026-08-17.md` Claim 9),
  though this one targets startup-time crashes specifically rather than a
  run that completes but produces nothing. For Ch06 (Agentic Operations):
  add this as a concrete example of gh-aw's incremental work hardening
  per-engine startup failure diagnostics — worth citing when the guide
  discusses debugging opaque agent-runtime crash signals.

### Claim 6: `dismiss_pull_request_review` safe-output ingestion previously rejected an omitted or `"auto"` `review_id`, even though the schema documented both as valid — this is now fixed so omitted and `"auto"` values are accepted while invalid explicit IDs are still rejected (PR #55180)

- **Evidence**: "Release Highlights" section, fourth bullet; corroborated
  by the implementing PR's own description, fetched via `gh pr view
  55180 --repo github/gh-aw`.
- **Confidence**: settled (specific PR, first-party PR description stating
  the bug and the fix explicitly, plus an example ingestion payload)
- **Quote**: "Automatic PR review dismissal ingestion (#55180): workflows can now ingest automatic pull request review dismissals as part of their safe-output processing."
- **Our assessment**: The PR body's own framing — "`dismiss_pull_request_review`
  documented omitted or `\"auto\"` `review_id` selection, but ingestion
  rejected both before the handler could resolve actor-authored reviews" —
  describes a validation/documentation mismatch bug: the schema promised a
  capability (auto-resolving which review to dismiss) that the validator
  actually blocked. This is the same class of "spec says X, validator does
  Y" bug already documented for `gh-aw-detection` in
  `blog-ghaw-weekly-2026-08-17.md` Claim 9 (misclassified unset/absent
  values) — a recurring failure mode in gh-aw's safe-output ingestion
  layer where schema and validator logic drift apart. For Ch04: note this
  as a second dated instance of that drift class; worth flagging in any
  guide discussion of safe-output schema validation as a place where
  first-party tooling itself has shipped mismatches between documented and
  enforced behavior.

### Claim 7: The Notable Pull Requests section reports five additional merges this week: standardizing daily-report workflow/merge-window metrics so fleet-size and Copilot success-rate numbers stop drifting apart (PR #55214); fixing a Lockfile Statistics report that was silently reporting zero discussion categories due to a key mismatch, plus a self-check to catch regressions (PR #55209); updating the detection-analysis report now that `gh-aw-detection` defaults on, so it classifies unset/absent values correctly instead of flagging them as misconfigured (PR #55236); migrating 30 Copilot workflows to the codex engine plus a `copilot/mai-code-1-flash-picker` (PR #55154); and rendering the agentic engine name in generated footers for traceability (PR #55192)

- **Evidence**: "Notable Pull Requests" section, all five bullets; PR
  numbers recovered from the page's anchor hrefs (not printed in the
  visible prose) via the raw HTML — see Extraction Notes.
- **Confidence**: settled for the existence and one-line description of
  each fix (specific, first-party changelog bullets, each independently
  linked to a PR number); emerging for mechanism detail on any of them
  (none is elaborated beyond one sentence in the blog post, and none of
  the five PRs was independently fetched — see Extraction Notes)
- **Quote**: "Align daily workflow and merged-PR metrics: standardized the daily reports' workflow population and merge-window comparisons so fleet-size and Copilot success-rate numbers stop drifting apart." / "Fix lockfile-stats discussion category extraction and add loud self-check: the Lockfile Statistics report was silently reporting zero discussion categories due to a key mismatch in compiled .lock.yml parsing — now fixed, with a self-check to keep it from regressing quietly again." / "Update detection analysis report to reflect gh-aw-detection default-on: now that gh-aw-detection defaults to enabled, the detection-analysis-report workflow correctly classifies unset/absent values instead of flagging them as misconfigured."
- **Our assessment**: The `gh-aw-detection` default-on item directly extends
  the rollout tracked across multiple prior weekly notes —
  `blog-ghaw-weekly-2026-06-22.md` Claim 3 (20% → 50%, ~107 of 214
  workflows) and `blog-ghaw-weekly-2026-08-17.md` Claim 9 (+30 more
  workflows, ~137 migrated, denominator unstated) — this week's item
  confirms the feature has now reached "default-on" status rather than
  being an opt-in percentage rollout, which is a meaningful status change
  worth updating the guide's account of that rollout to reflect. The
  Lockfile Statistics "silently reporting zero" bug is another instance of
  gh-aw's own internal reporting tooling shipping with a silent-failure
  mode later caught and fixed with an added self-check — consistent with
  the "self-check to prevent quiet regression" remediation pattern also
  implicit in the `dismiss_pull_request_review` fix (Claim 6). For Ch04:
  update the `gh-aw-detection` rollout status from "incremental percentage
  migration, denominator unstated" (as of `blog-ghaw-weekly-2026-08-17.md`)
  to "default-on" as of this release. For Ch06: add the Lockfile
  Statistics silent-zero bug as a further data point in the "internal
  reporting/metrics tooling shipping with silent failure modes" thread
  already touched by the daily-report metrics-drift fix (PR #55214) in
  this same week's notes.

### Claim 8: PR Sous Chef, a workflow that keeps open pull requests' descriptions, context, and footers current, ran three times in a single day (all successful, on the `pi` engine), used roughly 76K tokens total, produced 8 safe-output items across its runs, and — in its most recent run — produced 5 safe-output items in under 8 minutes; that same workflow shipped the new pre-create PR steering feature (#55171) about itself

- **Evidence**: "Agent of the Week: PR Sous Chef" section, two paragraphs
  plus a usage tip; corroborated by the actual PR #55171 description
  (fetched via `gh pr view`), whose footer identifies it as generated by
  "👨‍🍳 PR Sous Chef" on engine `pi`, model `copilot/gpt-5.4`.
- **Confidence**: settled for the specific run-data figures (three runs, 76K
  tokens, 8 safe-output items, most recent run: 5 items in under 8
  minutes) — first-party, specific, stated as a measured window;
  corroborated (not merely asserted) by the fact that PR #55171 itself
  carries a PR Sous Chef-generated footer naming the `pi` engine
- **Quote**: "This week pr-sous-chef ran three times in a single day (all successful, all on the pi engine), burning through roughly 76K tokens and racking up 8 safe-output items across its runs — including landing the new pre-create PR steering feature itself via #55171. Its most recent run alone produced 5 safe items in under 8 minutes, a tidy little burst of productivity right before this post went out." / "Somewhat fittingly, the workflow that teaches other PRs how to listen to reviewer feedback (steer) shipped that very feature about itself — a small bit of \"eating your own dog food\" that we appreciated."
- **Our assessment**: This is the corpus's first profile of PR Sous Chef by
  name and a concrete, verifiable instance of gh-aw's own PR pipeline
  producing a feature PR about itself — a dogfooding data point distinct
  from (but structurally similar to) the Issue Arborist and Dead Code
  Removal Agent profiles already in the corpus
  (`blog-ghaw-weekly-2026-08-17.md` Claims 10–11;
  `blog-ghaw-agent-of-the-day-2026-05-28.md`). The usage tip frames the
  workflow's ideal use case narrowly ("whenever your team's biggest
  bottleneck is PR descriptions and footers going stale between review
  rounds"), which is a useful scoping detail — it is explicitly not framed
  as a general PR-authoring or code-review agent. For Ch06 (Agentic
  Operations): add PR Sous Chef as a third scheduled/triggered
  maintenance-agent profile, and note it as a concrete real-world example
  of a workflow shipping a change to its own capabilities (the `steer`
  feature) and then presumably becoming a first user of that capability —
  worth citing when the guide discusses agents that modify their own
  automation surface.

## Concrete Artifacts

### `pre-create.steer` YAML configuration (from PR #55171 description, fetched via `gh pr view 55171 --repo github/gh-aw`)

```yaml
permissions:
  contents: read
  pull-requests: read

safe-outputs:
  create-pull-request:
    pre-create:
      steer: true
```

*Source: PR body, "Configuration" section. The PR body also states this
"Preserves existing boolean `pre-create: true` behavior" — i.e. `pre-create`
now accepts either a bare boolean or an object with a `steer` key.*

### `gh aw models` example invocation and data sources (from PR #55148 description, fetched via `gh pr view 55148 --repo github/gh-aw`)

```bash
gh aw models --json --refresh-count 50
```

```
Observed-model intelligence from automation — aggregates observed models from:
  - summary.json token usage (token_usage_summary.by_model)
  - per-run token usage artifacts
  - awf-reflect.json endpoint model lists
De-duplicates and merges provenance (summary, token-usage, awf-reflect),
tracks occurrence counts, and marks catalog presence.
```

*Source: PR body, "Command surface" and "Observed-model intelligence from
automation" sections.*

### Copilot SDK pre-ready crash error shape, before vs. after (from PR #55149 description, fetched via `gh pr view 55149 --repo github/gh-aw`)

```text
copilot-sdk headless server exited before ready (exitCode=unknown signal=SIGABRT)
stderr tail:
native assertion failed before listen
panic details
```

*Source: PR body, "Example reported error shape" — the `stderr tail:` block
is new; previously only the `exitCode=unknown signal=SIGABRT` portion was
reported, per the PR body's problem statement.*

### `dismiss_pull_request_review` ingestion payload accepted after the fix (from PR #55180 description, fetched via `gh pr view 55180 --repo github/gh-aw`)

```json
{
  "type": "dismiss_pull_request_review",
  "review_id": "auto",
  "justification": "This stale review no longer reflects the updated implementation."
}
```

*Source: PR body. The PR's "Fixes #55177" line confirms this was tracked as
a bug against previously-documented (but unenforced) validator behavior.*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-weekly-2026-08-17.md` Claim 1 (the `approve-workflow-run`
    safe output requiring an explicit external token rather than silently
    escalating permissions): Claim 1 here (`pre-create.steer` requiring
    explicit `pull-requests: read`, not auto-added) is a second, dated
    instance of gh-aw's "require explicit permission, never silently
    expand it" design posture applied to a different safe-output type.
  - `blog-ghaw-weekly-2026-08-17.md` Claim 9 (`gh-aw-detection` migrated to
    30 more workflows, ~137 total, denominator unstated) and
    `blog-ghaw-weekly-2026-06-22.md` Claim 3 (20% → 50% rollout, ~107 of
    214): Claim 7 here (the detection-analysis report now reflects
    `gh-aw-detection` defaulting on) is the next dated milestone in that
    same rollout thread, one week later, moving it from "incremental
    percentage migration" to "default-on."
  - `blog-ghaw-weekly-2026-07-20.md` Claim 2 (`COPILOT_PROVIDER_WIRE_API`
    auto-configured from the model catalog): Claim 4 here (`gh aw models`
    surfacing catalog pricing and alias resolution) corroborates that the
    model catalog continues to be a growing, actively-tooled configuration
    surface, now with a dedicated CLI query command rather than only
    auto-resolution behavior.

- **Contradicts**: None found at the MINER.md §4a threshold. No existing
  source note makes a claim this post's content materially opposes.

- **Extends**:
  - `blog-ghaw-weekly-2026-08-17.md` Claims 10–11 (Issue Arborist
    Agent-of-the-Week profile with multi-run metrics and an `experiments:`
    A/B block) and `blog-ghaw-agent-of-the-day-2026-05-28.md` (Dead Code
    Removal Agent profile): Claim 8 here adds PR Sous Chef as a third named,
    metrics-profiled maintenance agent, with a distinctive twist — it
    shipped a feature (steering) about itself and (per the post) is
    expected to be an early user of that same feature.
  - `blog-ghaw-weekly-2026-08-17.md` Claim 9 (Aider engine silently
    producing zero safe outputs) and the general "agent run completes
    without honestly reflecting what happened" failure class: Claim 5 here
    (Copilot SDK pre-ready crashes previously reporting only a bare exit
    signal) is an adjacent but distinct failure class — an opaque crash
    signal rather than a silently-empty successful run — now diagnosable
    via a captured stderr tail.
  - `blog-ghaw-weekly-2026-08-17.md` Claim 3 (`THREAT_WARNING_ABORT_TYPES`,
    the named non-reviewable-mutation safe-output category covering
    `approve-workflow-run`, `merge-pull-request`, `close-pull-request`):
    Claim 6 here's `dismiss_pull_request_review` ingestion fix is a
    related but distinct safe-output type not documented as belonging to
    that category; worth a follow-up check on which threat-detection
    category `dismiss_pull_request_review` itself falls under, since this
    post does not say.

- **Novel**:
  - **Pre-create pull-request steering** (Claims 1–3): first corpus
    documentation of a `pre-create.steer` config, its compile-time
    permission-gating validator, its GitHub MCP toolset wiring, and its
    `steer`-keyword-gated human-feedback channel.
  - **`gh aw models` CLI command** (Claim 4): first corpus mention of a
    dedicated model-inventory/pricing/alias-resolution query command,
    distinct from prior changelog-only "model added to catalog" bullets.
  - **Copilot SDK startup stderr diagnostics** (Claim 5) and
    **`dismiss_pull_request_review` `"auto"`/omitted `review_id` fix**
    (Claim 6): first corpus documentation of either specific bug/fix.
  - **PR Sous Chef** (Claim 8): first corpus profile of this named agent.

## Guide Impact

- **Chapter 03 (Workflows & Orchestration)**:
  - Add pre-create PR steering (Claims 1, 3) as a pattern for closing the
    loop between human review feedback and an agent's PR-editing behavior
    without a full workflow re-run, including the `steer`-keyword
    convention for disambiguating agent-directed feedback from ordinary PR
    discussion.

- **Chapter 04 (Safety & Guardrails)**:
  - Add the `pre-create.steer` compiler validator (Claim 2) — refuses to
    compile without explicit `pull-requests: read`, never auto-adds the
    permission — as a second, compile-time-class example of gh-aw's
    "require explicit permission, don't silently expand it" pattern,
    alongside the runtime-eligibility-check example already documented for
    `approve-workflow-run` in `blog-ghaw-weekly-2026-08-17.md`.
  - Update the `gh-aw-detection` rollout status (Claim 7) from "incremental
    percentage migration, ~137 workflows, denominator unstated" (as of
    2026-08-17) to "default-on" as of this release.
  - Note the `dismiss_pull_request_review` schema/validator mismatch fix
    (Claim 6) as a second dated instance (after the `gh-aw-detection`
    unset/absent-value misclassification in
    `blog-ghaw-weekly-2026-08-17.md` Claim 9) of gh-aw's own safe-output
    ingestion layer shipping mismatches between documented and enforced
    validation behavior.

- **Chapter 02 (Harness Engineering)**:
  - Add `gh aw models --json --refresh-count 50` (Claim 4) as a concrete
    command for auditing which models a fleet of agentic workflows
    actually uses (via `summary.json`, per-run token-usage artifacts, and
    `awf-reflect.json`) versus what's configured or aliased in the
    catalog — relevant to any guide material on model-cost governance or
    fleet-wide model auditing.

- **Chapter 06 (Agentic Operations)**:
  - Add PR Sous Chef (Claim 8) as a third scheduled/triggered
    maintenance-agent profile alongside Issue Arborist and the Dead Code
    Removal Agent, with the notable property that it shipped a new
    capability about itself.
  - Add the Copilot SDK pre-ready-crash stderr-diagnostics fix (Claim 5)
    and the Lockfile Statistics silent-zero-discussion-categories bug
    (Claim 7) as further data points in the corpus's running thread on
    gh-aw's own operational/reporting tooling shipping with, and later
    fixing, silent or opaque failure modes.

## Extraction Notes

1. **Raw HTML fetched via `curl` and parsed with a Python regex-based
   tag-stripping pass**, following the practice established in prior
   weekly notes (e.g. `blog-ghaw-weekly-2026-08-17.md` Extraction Note 1),
   though this pass used Python's built-in `re`/`html` modules rather than
   BeautifulSoup (not installed in this environment). Content was read
   from the full page body after script/style stripping, not from a
   WebFetch summary.

2. **Four linked pages were followed and fetched directly**, within the
   "up to 5" budget in MINER.md §1: the four PRs named in "Release
   Highlights" — #55171 (pre-create steering), #55148 (`gh aw models`),
   #55149 (Copilot SDK diagnostics), and #55180 (review-dismissal
   ingestion) — each fetched via `gh pr view <N> --repo github/gh-aw
   --json title,body,url`. These supplied all implementation-level detail
   in Claims 1–6 and all Concrete Artifacts; none of this detail is present
   in the blog post's one-sentence-per-item prose. The five "Notable Pull
   Requests" items (Claim 7) were NOT independently fetched — PR numbers
   for those were recovered from the raw HTML's anchor hrefs
   (`/pull/55214`, `/pull/55209`, `/pull/55236`, `/pull/55154`,
   `/pull/55192`), but their content in this note relies solely on the
   blog's own one-sentence descriptions.

3. **Unlike several prior weekly posts** (e.g.
   `blog-ghaw-weekly-2026-08-17.md`, which linked a GitHub Releases page
   with an expanded "🔧 Internal & Security" section), this post does not
   link a release-notes page separate from the individual PRs — "Release
   Highlights" links directly to PRs, and no expanded internal/security
   summary beyond what's in Claims 1–6 could be located or cross-checked.

4. **Discrepancy noted, not filed as a contradiction**: the blog prose's
   phrasing "`safe-outputs.create-pull-request.steer: true`" reads as a
   flat dotted key, but PR #55171's own "Configuration" section shows the
   actual schema nests `steer` one level deeper, under `pre-create` (see
   Concrete Artifacts: `create-pull-request.pre-create.steer`). This is a
   blog-prose imprecision against the first-party PR/schema source, not a
   disagreement between two independently-argued claims, so it does not
   meet the MINER.md §4a bar for a contradiction issue — flagged here so
   the guide cites the PR's schema, not the blog's shorthand, if it
   documents this config path.

5. **Cross-reference check performed** against `docs-ghaw-safe-outputs-specification.md`,
   `docs-ghaw-automated-pr-review.md`, `docs-ghaw-engines-reference.md`,
   `docs-ghaw-cost-management.md`, `blog-ghaw-weekly-2026-08-17.md`,
   `blog-ghaw-weekly-2026-07-20.md`, `blog-ghaw-weekly-2026-06-22.md`,
   `blog-ghaw-agent-of-the-day-2026-05-28.md`, and
   `blog-ghaw-custom-linters-three-workflow-loop.md`, plus `CONTRADICTIONS.md`
   for existing open entries. No contradiction rises to the MINER.md §4a
   filing bar.
