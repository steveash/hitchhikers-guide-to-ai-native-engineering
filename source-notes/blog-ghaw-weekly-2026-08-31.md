---
source_url: https://github.github.com/gh-aw/blog/2026-08-31-weekly-update/
source_type: blog-post
title: "Weekly Update – August 31, 2026 (GitHub Agentic Workflows)"
author: GitHub Agentic Workflows team (gh-aw); byline "Copilot"
date_published: 2026-08-31
date_extracted: 2026-08-31
last_checked: 2026-08-31
status: current
confidence_overall: settled
issue: "#3127"
---

# Weekly Update – August 31, 2026 (GitHub Agentic Workflows)

> Three v0.87.x pre-releases (v0.87.5, v0.87.8, v0.87.9) ship `on.cooldown`
> workflow-trigger gating, a typed `on.stop-after` field that now accepts
> GitHub Actions expressions, Codex tool-schema failure diagnostics, and
> intent-driven workflow design guidance, plus five new entries in a
> 25-grader "trajectory graders" catalog. The Agent of the Week is AI
> Moderator, a read-only spam/AI-content moderation workflow running
> `threat-detection: false` at high trigger volume. The post's own prose
> calls PR #56614 the "Feature Farmer workflow pattern," but the PR itself
> shipped the pattern under the name **Feature Grower** — already documented
> in this corpus as `docs-ghaw-feature-grower.md` — a naming discrepancy
> worth flagging for anyone citing this post.

## Source Context

- **Type**: blog-post (weekly changelog/update from the official GitHub
  Agentic Workflows blog; a short intro, a "Release Highlights" section of
  four bullets, a "Notable Pull Requests" section of five items plus a
  trajectory-grader-library summary sentence, an "Agent of the Week: AI
  Moderator" spotlight, and a "Try It Out" closer)
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team (GitHub Next / Microsoft
  Research). The on-page byline names the author as "Copilot" — the same
  non-human byline pattern documented in prior weekly notes (e.g.
  `blog-ghaw-weekly-2026-08-24.md`). Fetched via `curl` and parsed with a
  Python regex-based tag-stripping pass (not a WebFetch summary) to preserve
  exact wording — see Extraction Notes.
- **Scope**: One "Release Highlights" section naming four items from the
  v0.87.9 pre-release line (`on.cooldown` #56998, typed `on.stop-after`
  #56983, Codex tool-schema diagnostics #57256, two dependency bumps
  #57188/#56914), one "Notable Pull Requests" section of five prose items
  (PR numbers recovered from the page's anchor hrefs) plus a one-sentence
  summary of five trajectory-grader implementations, and one Agent of the
  Week spotlight on AI Moderator. Does NOT cover: the internals of the
  trajectory-grader Trajectory IR data model beyond what individual grader
  PRs describe (fetched separately, below); a changelog/release-notes page
  distinct from the individual linked PRs (this post links directly to PRs
  and GitHub Releases tags, not to an expanded internal/security summary
  page).

## Extracted Claims

### Claim 1: `on.cooldown` lets a workflow declare a minimum interval (a literal Go duration of at least five minutes) since the most recently completed run of its `agent` job, enforced by a pre-activation run-history check that fails open when history is unavailable and rejects GitHub Actions expressions

- **Evidence**: "Release Highlights" section, first bullet; corroborated by
  the implementing PR's own description and diff, fetched via `gh pr view
  56998 --repo github/gh-aw`. The PR adds `pkg/workflow/cooldown.go`,
  `actions/setup/js/check_cooldown.cjs`, an ADR
  (`docs/adr/56998-add-workflow-cooldown-gating.md`), and a new
  pre-activation `actions: read` check.
- **Confidence**: settled (specific PR, specific config key, first-party PR
  description with concrete YAML, validation constraints, and runtime
  behavior)
- **Quote**: "`on.cooldown` workflow gating (#56998): workflows can now
  declare a cooldown window to prevent consecutive triggers from
  accumulating"
- **Quote**: "Adds a configurable cooldown between agent executions based on
  the latest completed workflow run that executed the `agent` job. -
  **Frontmatter** - Accepts literal Go durations of at least five minutes. -
  Rejects GitHub Actions expressions and invalid durations. - **Execution
  gating** - Adds a pre-activation run-history check with `actions: read`. -
  Ignores runs where the agent job was skipped. - Counts successful and
  failed agent executions. - Fails open when run history is unavailable."
  (PR #56998 body)
- **Our assessment**: This is a distinct cost/noise-control primitive from
  the existing `skip-if-match` open-item gate and `stop-after` deadline
  mechanism documented in `docs-ghaw-triggers-reference.md` (Claims 6 and
  9) and the "All You Can Eat" open-output gate documented in
  `docs-ghaw-feature-grower.md` (Concrete Artifacts). Those gates ask "is
  there still an open item from last time?" or "has the deadline passed?";
  `on.cooldown` asks a purely time-based question — "has enough wall-clock
  time elapsed since the last run?" — independent of whether that run
  produced an open, unconsumed item. The explicit rejection of GitHub
  Actions expressions (literal durations only) is notable given Claim 2
  below shows the *sibling* `stop-after` field moved the opposite direction
  this same release line, toward accepting expressions — the two fields
  diverge on this design axis for different reasons (see Claim 2's
  assessment). The "fails open when run history is unavailable" behavior
  is a deliberate availability-over-strictness choice: if the run-history
  API call itself fails, the workflow activates rather than silently never
  running. For Ch03 (Workflows & Orchestration): add `on.cooldown` as a
  third scheduling-gate primitive alongside `skip-if-match` and
  `stop-after`, useful specifically for suppressing back-to-back triggers
  on a hot event stream (e.g., a workflow triggered by `issue_comment` on
  a fast-moving thread) regardless of whether prior runs left open output.

### Claim 2: The `on.stop-after` field gained a typed `OnStopAfter string` struct field (replacing a dynamic `map[string]any` lookup) and now accepts a GitHub Actions expression like `${{ inputs.stop-after }}`, which is passed through verbatim at compile time and resolved only at runtime, whereas static values are still parsed as relative deltas or absolute timestamps at compile time

- **Evidence**: "Release Highlights" section, second bullet; corroborated by
  the implementing PR's own description, fetched via `gh pr view 56983
  --repo github/gh-aw`.
- **Confidence**: settled (specific PR, first-party PR description with
  exact mechanism, a worked YAML example, and the motivating bug reference)
- **Quote**: "Typed `on.stop-after` field (#56983): `stop-after` now accepts
  GitHub Actions expressions in addition to static values" (blog post)
- **Quote**: "`on.stop-after` was documented and actively parsed at
  runtime, but had no typed struct field — it was only readable via a
  dynamic `map[string]any` lookup, creating a schema/parser/docs drift
  risk. Additionally, `stop-after` couldn't reference a GitHub Actions
  expression, since compile-time parsing would reject anything that wasn't
  a valid relative delta or absolute timestamp. ... `stop-after` now
  accepts an expression such as `${{ inputs.stop-after }}`. When detected
  via `isExpression()`, the value is passed through verbatim instead of
  being parsed as a relative delta or absolute timestamp at compile time —
  resolution happens at workflow runtime." (PR #56983 body)
- **Our assessment**: This directly extends and updates
  `docs-ghaw-triggers-reference.md` Claim 9, which documented `stop-after:`
  (as of 2026-05-11) as accepting only static forms — `'+25h'`, `'+7d'`,
  `'2025-12-31'` — calculated from compilation time, with no mention of
  expression support. This is not a contradiction between two sources
  disagreeing about the current state; it is the platform shipping a
  capability the earlier reference page's snapshot did not have. The
  practical unlock is workflow_dispatch-parameterized expiry —
  `stop-after: ${{ inputs.stop-after }}` lets a human dispatching the
  workflow choose the deadline at trigger time rather than it being fixed
  at the last compile. Contrast with `on.cooldown` (Claim 1), which
  explicitly *rejects* expressions for the opposite reason: cooldown
  gating is a pre-activation, no-agent-run correctness check that must be
  cheap and side-effect-free to evaluate before any GitHub Actions context
  is fully resolved, whereas `stop-after` is evaluated per-trigger and can
  safely defer to runtime expression resolution. For Ch03: update any
  guide coverage of `stop-after:` to note expression support was added in
  this release (v0.87.9-line) and is the newer of the two mechanisms;
  cite `docs-ghaw-triggers-reference.md` Claim 9 for the pre-existing
  static-only behavior and this claim for the current expanded behavior.

### Claim 3: A Codex-engine tool-schema failure — where the configured model doesn't support the `custom` tool type Codex CLI requires for its `apply_patch` schema — previously surfaced only as a cryptic nested JSON provider error (`"Invalid value: 'custom'"` / `unknown_parameter`), and the harness now detects this specific signature and logs an actionable message instead

- **Evidence**: "Release Highlights" section, third bullet; corroborated by
  the implementing PR's own description, fetched via `gh pr view 57256
  --repo github/gh-aw`.
- **Confidence**: settled (specific PR, first-party PR description with
  the exact failing error JSON, the detection function names, and the
  before/after log message text)
- **Quote**: "Codex harness tool-schema diagnostics (#57256): unsupported-
  model failures now display dedicated error messages" (blog post)
- **Quote**: "The Daily Go Test Parallelizer workflow crashed with the
  Codex engine failing on a cryptic provider error: `{\"error\": {\"message\":
  \"Invalid value: 'custom'\", \"type\": \"invalid_request_error\", \"param\":
  \"tools\", \"code\": \"unknown_parameter\"}}` The configured model doesn't
  support the `custom` tool type Codex CLI requires for its
  `apply_patch`/freeform tool schema — a model-capability mismatch, not a
  transient failure. ... Added `extractNestedProviderErrorDetails()` to
  unwrap Codex's `turn.failed` event, whose provider error is
  JSON-string-encoded (sometimes doubly nested), to reach the structured
  `param`/`code` fields. Added `isUnsupportedModelToolsError()` as a
  dedicated detector for the `\"tools\"` / `\"unknown_parameter\"`
  signature" (PR #57256 body)
- **Our assessment**: This is a concrete, dated instance of the same
  "opaque engine failure → captured diagnostic" remediation pattern
  documented for the Copilot SDK pre-ready crash fix in
  `blog-ghaw-weekly-2026-08-24.md` Claim 5 (surfacing stderr tail instead
  of a bare exit signal), applied here to the Codex engine's provider-error
  layer instead of process-crash layer. The fix explicitly does not change
  retry behavior — it was already correctly non-retried as a generic
  `invalid_request_error` — it only makes the *reason* legible: "pick a
  model documented as compatible with Codex CLI, or remove the `model:`
  override in workflow frontmatter to use the engine default." This is a
  narrow but real debuggability win for teams pinning specific models on
  Codex-engine workflows. For Ch06 (Agentic Operations): add this as a
  further data point in the corpus's running thread on gh-aw hardening
  per-engine failure diagnostics — specifically, a model/tool-schema
  capability mismatch is now a self-diagnosing failure mode on Codex,
  distinct from the Copilot SDK startup-crash case already documented.

### Claim 4: Intent-driven workflow design guidance defines "intent" as an implementation-independent statement of a repository outcome, introduces a transient `IntentSpec` for design-time decisions, documents PromptPex-derived positive and inverse eval scenarios as distinct from operational-value measurement, and is now linked from the workflow creation, update, and designer agent instructions

- **Evidence**: "Notable Pull Requests" section, first item; corroborated by
  the implementing PR's own description, fetched via `gh pr view 57005
  --repo github/gh-aw`.
- **Confidence**: settled (specific PR, first-party PR description
  enumerating the four documentation additions)
- **Quote**: "Document intent-driven workflow design: new guidance explains
  how to write workflow prompts around clear intent rather than rigid
  step-by-step instructions, complementing the earlier intent-driven
  workflow design guidance and the optional `intent` frontmatter field
  (#56599)." (blog post)
- **Quote**: "Adds intent guidance for designing and evaluating agentic
  workflows. - **Intent definition** - Defines intent as an
  implementation-independent repository outcome. - Introduces a transient
  `IntentSpec` for design decisions. - **Evaluation** - Documents PromptPex
  derivation of positive and inverse eval scenarios. - Separates
  behavioral evals from operational-value measurement. - **Operational
  value** - Maps intent conditions to opportunities, evidence, attainment
  metrics, and maturity rules. - **Integration** - Links the guidance from
  workflow creation, update, and designer instructions." (PR #57005 body)
- **Our assessment**: This is the first corpus documentation of an
  `intent`/`IntentSpec` design vocabulary for gh-aw workflow authoring,
  distinct from (but directly wired into) the `operational-value` grader
  mechanism documented in `docs-ghaw-graders.md` Claim 6 — that note
  documents *how* an operational-value evaluator is frozen, digested, and
  scored, but not what determines its scoring criteria in the first place.
  PR #57005's "maps intent conditions to opportunities, evidence,
  attainment metrics, and maturity rules" is the missing upstream link: an
  `IntentSpec` written at design time appears to be the source that an
  `operational-value` evaluator's attainment scoring is meant to
  implement. This PR's own body references "the earlier intent-driven
  workflow design guidance and the optional `intent` frontmatter field
  (#56599)" as a prior, separate PR — meaning `#56599` (not independently
  fetched in this note) shipped an initial `intent:` frontmatter field
  before this PR added the fuller design/evaluation guidance. For Ch02
  (Harness Engineering) and Ch04 (Agent Patterns): document `intent`/
  `IntentSpec` as the design-time vocabulary that upstream-feeds
  `operational-value` grader criteria (`docs-ghaw-graders.md` Claim 6),
  and flag PR #56599 as a candidate follow-up fetch for the `intent:`
  frontmatter field's exact schema, which this note did not independently
  verify.

### Claim 5: PR #56614, titled "Add the Feature Farmer workflow pattern" in both its own PR title and this week's blog prose, is the exact PR that created `.github/workflows/feature-grower.md` and `docs/src/content/docs/patterns/feature-grower.md` — i.e., the pattern shipped under the name "Feature Grower," not "Feature Farmer"

- **Evidence**: `gh pr view 56614 --repo github/gh-aw --json title,body,
  files,createdAt,mergedAt` — file list includes
  `.github/workflows/feature-grower.lock.yml`,
  `.github/workflows/feature-grower.md`, and
  `docs/src/content/docs/patterns/feature-grower.md`. Merged 2026-08-28,
  three days before this post. Corroborated independently: this corpus
  already has `docs-ghaw-feature-grower.md` (extracted 2026-08-30, from
  the shipped `patterns/feature-grower` docs page), documenting the
  identical `crop`/`cookie` label mechanism, the identical open-child
  backpressure gate, and the identical avoiding-waterfall-planning
  rationale that PR #56614's own body describes.
- **Confidence**: settled (direct verification against the PR's own file
  list, not an inference)
- **Quote**: "Feature Farmer advances long-lived features incrementally: a
  scheduled agent assesses current implementation state and creates the
  next reviewable unit of work instead of planning the entire feature
  upfront. ## Changes - **Workflow** - Scan open issues labeled `crop`. -
  Skip crops with an open `cookie` sub-issue. - Assess the plan against
  repository files, completed children, and workflow memory. - Create one
  implementation-ready `cookie` sub-issue per eligible crop." (PR #56614
  body)
- **Our assessment**: This is a naming discrepancy between the PR's own
  title/description and the artifact it actually shipped, not a
  contradiction between two independently-argued claims — the PR body and
  the shipped file names are produced by the same change, and the file
  names (which the docs site and workflow directory expose to users) are
  authoritative over the PR title (an internal, pre-merge label). Per
  MINER.md §4a this does not meet the bar for a contradiction issue: there
  is no disagreement about what the pattern *is* or *does*, only about
  which of two names is user-facing. Practically, this means a reader
  encountering "Feature Farmer" only in this blog post's prose (as the
  Prospector's triage comment for this issue did, listing "Feature Farmer
  workflow pattern" as a claim to extract) should be pointed to the
  existing `docs-ghaw-feature-grower.md` note rather than treated as
  encountering a new, second pattern. For Ch02: when citing this pattern,
  use "Feature Grower" (the shipped name) and note "Feature Farmer" only
  as the PR's internal working title, to avoid the guide accidentally
  implying two distinct patterns exist.

### Claim 6: The gh-aw team's own Trajectory Grader Implementer workflow was itself converted to run as a Feature Grower under the "All You Can Eat" cadence — schedule changed from daily to every 30 minutes, with `skip-if-match` normalized to match on open PR title rather than an issue-body marker

- **Evidence**: Blog prose links "converting the trajectory grader workflow
  to the 'all-you-can-eat' pattern" to PR #56988, fetched via `gh pr view
  56988 --repo github/gh-aw --json title,body,createdAt,mergedAt`. Not
  listed as a separate bullet in the blog's "Notable Pull Requests"
  section — it appears only as an inline link inside the Feature
  Farmer/Feature Grower bullet's prose.
- **Confidence**: settled (specific PR, first-party PR description with
  before/after schedule and skip-query values, merged 2026-08-29)
- **Quote**: "Updates the Trajectory Grader Implementer workflow to run as
  a Feature Grower using the All-You-Can-Eat pattern, increasing schedule
  frequency to every 30 minutes while maintaining open PR backpressure
  gating. ... Changed `on.schedule` from `daily` to `every 30 minutes` and
  normalized `skip-if-match` to `'is:pr is:open in:title
  \"[trajectory-grader]\"'`." (PR #56988 body)
- **Our assessment**: This is a concrete, dated, real-world worked example
  of exactly the cadence-selection guidance
  `docs-ghaw-feature-grower.md` Claim 10 documents in the abstract ("Use
  the All You Can Eat pattern with a frequent schedule, typically every 30
  minutes, when the next chunk should appear soon after the previous issue
  closes or pull request merges") — here applied to a PR-based backpressure
  gate (`is:pr is:open in:title ...`) rather than the issue-body-marker
  gate shown in that note's reference frontmatter. It also confirms the PR
  title itself uses "feature grower," not "Feature Farmer" ("Convert
  trajectory grader workflow to feature grower (all-you-can-eat)
  pattern"), independently corroborating Claim 5's naming finding. For
  Ch02: add this as a second worked `skip-if-match` example alongside the
  issue-body-marker form already in `docs-ghaw-feature-grower.md` — an
  open-PR-title match is the natural gate when the "cookie" unit of work
  is a pull request rather than a sub-issue.

### Claim 7: The trajectory grader library is a ranked, 25-entry catalog of self-contained importable grader components (distinct from the `graders:` built-in/custom-inline-JS system) computed over a shared "Trajectory IR" of canonical `events[]` and `objectives[]`, including entropy/complexity measures (event-entropy-rate, lempel-ziv-trajectory-complexity) and objective-attribution measures (policy-near-miss, exploration-error, exploitation-error) that distinguish "failed despite enough evidence" from "failed from insufficient search"

- **Evidence**: Blog post's one-sentence summary ("the team also kept
  implementing new entries in the trajectory grader library"); each of the
  five named graders independently fetched via `gh pr view <N> --repo
  github/gh-aw` (PRs #56464, #56972, #56996, #57087, #57152).
- **Confidence**: settled for the catalog's existence, ranking, and the
  five graders' individual purposes (first-party PR bodies, each stating
  tier/rank and a precise metric definition); emerging for the full
  25-grader catalog contents and the Trajectory IR schema beyond
  `events[]`/`objectives[]` (not independently fetched — the catalog
  README and IR schema live outside this post's linked PRs)
- **Quote**: "The team also implemented trajectory grader entries:
  event-entropy-rate, lempel-ziv-trajectory-complexity, policy-near-miss,
  exploration-error, and exploitation-error." (blog post)
- **Quote**: "Implements `event-entropy-rate` (Tier 1, rank 10) from the
  trajectory graders catalog: the normalized first-order (bigram) Shannon
  entropy rate of the event process, projected purely from the Trajectory
  IR's `events[]`. This is 6 of 25 catalog graders now implemented." (PR
  #56464 body)
- **Quote**: "`policy-near-miss` detects \"successful\" traces (those that
  emitted a `safe_output` event) that nonetheless left one or more
  guard/policy-shaped objectives unsatisfied — i.e. runs that reached the
  correct outcome without performing a required check." (PR #56996 body)
- **Quote**: "Adds the `exploration-error` grader (Tier 2, rank 3 in the
  trajectory graders catalog), which attributes objective failure to
  insufficient search density, as opposed to failing despite having enough
  evidence. ... Where `exploration-error` attributes objective failure to
  insufficient search, `exploitation-error` isolates the opposite case: the
  run gathered enough evidence but still missed objectives, scoring how
  much of that evidence no later action ever consumed." (PR #57087 and PR
  #57152 bodies)
- **Our assessment**: This is a distinct grader delivery mechanism from
  the two documented in `docs-ghaw-graders.md` — that note's Claims 3–5
  cover ten reserved *built-in* grader IDs (recognized by the compiler,
  cannot accept a custom script) and 4096-character *inline* JS
  expressions configured directly in a workflow's `graders:` block. These
  trajectory graders are neither: each ships as its own importable
  workflow fragment file (e.g.
  `.github/workflows/shared/graders/policy-near-miss.md`, per PR #56996),
  suggesting a third grader-authoring path — full workflow-fragment
  graders, presumably composed via the `imports:` mechanism already
  documented for `shared/graders.md` in `docs-ghaw-graders.md`'s Concrete
  Artifacts (the CLI Consistency Checker's import list). `policy-near-miss`
  vs. `exploration-error` vs. `exploitation-error` is a genuinely novel
  three-way taxonomy for grading *why* an agent trajectory failed to meet
  its objectives (insufficient search vs. sufficient-but-unused evidence
  vs. reached the outcome without the required guard check) — none of this
  failure-attribution vocabulary appears in `docs-ghaw-graders.md`'s
  built-in metric set (which measures execution shape: success rate,
  loops, context growth) or in `docs-ghaw-measuring-impact.md`'s four-layer
  taxonomy. For Ch02/Ch06 (Harness Engineering / Observability): document
  the trajectory-grader catalog as a third, higher-effort grader-authoring
  path beyond built-ins and inline JS — full workflow-fragment graders
  computed over a canonical Trajectory IR — and flag the catalog README
  (`.github/workflows/shared/graders/README.md`, referenced across all
  five PRs but not independently fetched here) as a follow-up source for
  the complete 25-grader list and Trajectory IR schema.

### Claim 8: AI Moderator is a read-only, `engine: codex` workflow that classifies issues, PR openings, and comments as spam / link-spam / ai-generated / ai-inspected using an explicit "probe detection" priority pass, is rate-limited to 5 runs per 60-second window per user and 10,000 daily AI credits, and runs with `threat-detection: false`

- **Evidence**: Blog post's "Agent of the Week" section; corroborated by
  the workflow's own source file, fetched via `curl` at
  `raw.githubusercontent.com/github/gh-aw/main/.github/workflows/ai-moderator.md`
  (frontmatter and full prompt body, reproduced in Concrete Artifacts
  below).
- **Confidence**: settled (first-party workflow source file, not just blog
  prose — every configuration detail below is drawn from the actual
  compiled workflow's frontmatter)
- **Quote**: "AI Moderator is the quiet gatekeeper that watches newly
  opened issues, comments, and pull requests for spam, AI-generated noise,
  and link spam, then quietly labels or hides what it finds. ... It runs
  read-only by design (no write-capable safe outputs get exercised unless
  it actually flags something) ... Because it runs read-only with
  `threat-detection: false` and tight per-window rate limits, ai-moderator
  is a solid template for any workflow that needs to watch high-volume
  public triggers (like `issues: opened` or `pull_request: opened` from
  forks) without risking runaway write actions." (blog post)
- **Quote (workflow frontmatter, verbatim)**: "max-daily-ai-credits: 10000
  \nuser-rate-limit:\n  max-runs-per-window: 5\n  window: 60" and
  "safe-outputs:\n  add-labels:\n    allowed: [spam, ai-generated,
  link-spam, ai-inspected]\n    target: \"*\"\n  hide-comment:\n    max: 5\n
  allowed-reasons: [spam]\n  noop:\n  threat-detection: false" (from
  `.github/workflows/ai-moderator.md`)
- **Our assessment**: The `threat-detection: false` choice here is a
  concrete, named, real-world instance of the opt-out
  `docs-ghaw-threat-detection.md` Claim 4 documents in the abstract —
  that note already speculated (via `docs-ghaw-agentic-ops.md`) about one
  workflow (`copilot-token-optimizer`) using this flag to avoid false
  positives when reading workflow source as data. AI Moderator is a second,
  independently-confirmed instance, and its rationale is different: AI
  Moderator's own job *is* adversarial content triage (deliberately reading
  attacker-controlled issue/PR/comment bodies for spam and injection-like
  patterns), so its safe-output surface is already maximally constrained
  by other means — read-only GitHub access, a 5-choice `add-labels`
  allowlist, a 5-per-run `hide-comment` cap, and tight per-user rate
  limiting — rather than by the AI threat-detection job. This is exactly
  the "high-volume public trigger without risking runaway write actions"
  design point `docs-ghaw-threat-detection.md`'s Guide Impact section
  anticipated needing a documented example of. Separately,
  `docs-ghaw-agent-factory-status.md` already lists "AI Moderator" among
  nine Codex-engine workflows (5% of a fleet) — this post's `engine: codex`
  frontmatter directly corroborates that prior fleet-inventory snapshot by
  name. For Ch03 (Safety and Verification): add AI Moderator as the
  reference example when documenting `threat-detection: false` as a
  deliberate, justified opt-out (not a blanket anti-pattern) — the
  justification here is "safe-output surface is already narrow and
  read-mostly by other guardrails," not "detection produces false
  positives" (the `copilot-token-optimizer` rationale).

### Claim 9: AI Moderator's spam-triage prompt defines a mandatory, priority-ordered "Probe Detection" check that must run before any other spam/link-spam/AI-content analysis, classifying near-empty or placeholder submissions as spam outright, and separately tracks a 24-hour rolling spam log in cache memory to detect "burst" behavior from a repeat offender

- **Evidence**: Full prompt body of `.github/workflows/ai-moderator.md`,
  fetched via `curl`, not summarized by WebFetch (see Extraction Notes).
- **Confidence**: settled (first-party workflow prompt source, quoted
  directly)
- **Quote**: "Before any other analysis, check if the issue or comment
  appears to be a **probe** — an empty or minimal test submission with no
  real content or intent: - Issue title is a default/generic value (e.g.,
  \"New issue\", \"Test\", \"test issue\", \"hello\", \"hi\", untitled) -
  Issue body is empty, blank, or contains only whitespace ... If any probe
  indicators are detected: - **Immediately classify as spam** — label with
  `spam` - Do NOT proceed with other detection tasks - These are
  reconnaissance attempts to test system boundaries, not genuine
  contributions" (`.github/workflows/ai-moderator.md` prompt body)
- **Quote**: "After filtering, check if the current actor (`${{
  github.actor }}`) has **2 or more spam incidents in the last 24 hours**.
  If so, treat this as a **burst** and increase your confidence that the
  current submission is also spam — even if it is not an obvious probe."
  (same source)
- **Our assessment**: Framing empty/placeholder submissions explicitly as
  "reconnaissance attempts to test system boundaries" (not just low-quality
  content) is a threat-modeling choice worth noting on its own — the
  workflow treats a blank issue not as noise to ignore but as a signal an
  attacker is probing what the moderation system will let through, and
  responds by hard-classifying rather than soft-scoring it. The 24-hour
  cache-memory spam log with a 2-incident burst threshold is a concrete,
  named example of `docs-ghaw-feature-grower.md` Claim 4's "memory is
  advisory, not authoritative" rule in a different pattern family: the
  workflow's own instructions explicitly guard against a missing or
  cache-expired log being treated as an error ("**Never call
  `missing_data` for a missing spam log**"), so absence of history is
  correctly interpreted as "no known history," not as a data-fetch
  failure. For Ch03/Ch06: cite the probe-detection-first ordering and the
  explicit "missing cache file is not an error" guard as two concrete,
  reusable prompt-design patterns for any moderation/triage workflow that
  combines a priority classification pass with cross-run cache memory.

## Concrete Artifacts

### `on.cooldown` YAML shorthand (from PR #56998 body)

```yaml
on:
  schedule: hourly
  cooldown: 30m
```

*Source: PR #56998 body, shown as the worked example immediately after the
frontmatter bullet list.*

### Typed `on.stop-after` expression syntax (from PR #56983 body)

```yaml
on:
  workflow_dispatch:
  stop-after: ${{ inputs.stop-after }}
```

*Source: PR #56983 body, "GitHub Actions expression support" section.*

### Codex tool-schema error — before vs. after (from PR #57256 body)

Before (raw provider error surfaced to the log):
```json
{"error": {"message": "Invalid value: 'custom'", "type": "invalid_request_error", "param": "tools", "code": "unknown_parameter"}}
```

After (dedicated diagnostic message):
```
attempt 1: configured model does not support Codex's required tool-calling schema
("tools" param rejected with code "unknown_parameter") — not retrying
(pick a model documented as compatible with Codex CLI, or remove the `model:` override
in workflow frontmatter to use the engine default)
```

*Source: PR #57256 body, problem statement and "Retry loop" section.*

### AI Moderator workflow frontmatter (verbatim, from `.github/workflows/ai-moderator.md`, fetched via `raw.githubusercontent.com`)

```yaml
private: true
redirect: "githubnext/agentics/workflows/ai-moderator.md@main"
emoji: "🤖"
timeout-minutes: 5
on:
  roles: all
  issues:
    types: [opened]
    lock-for-agent: true
  issue_comment:
    types: [created]
    lock-for-agent: true
  pull_request:
    types: [opened]
    forks: "*"
  skip-author-associations:
    issue_comment: [owner, member, collaborator]
    pull_request: [owner, member, collaborator]
    issues: [owner, member, collaborator]
  skip-roles: [admin, maintainer, write, triage]
  skip-bots: [github-actions, copilot, dependabot, renovate, github-copilot-enterprise, copilot-swe-agent]
max-daily-ai-credits: 10000
user-rate-limit:
  max-runs-per-window: 5
  window: 60
concurrency:
  group: "gh-aw-${{ github.workflow }}-${{ github.event.issue.number || github.event.pull_request.number }}"
  cancel-in-progress: false
engine: codex
network:
  allowed:
    - defaults
    - github
imports:
  - shared/otlp.md
  - shared/reporting.md
  - shared/graders.md
tools:
  bash: ["*"]
  cli-proxy: true
  cache-memory:
    key: spam-tracking-${{ github.repository_owner }}
    retention-days: 1
    allowed-extensions: [".json"]
  github:
    mode: gh-proxy
    read-only: true
    toolsets: [default]
    min-integrity: none
permissions:
  contents: read
  issues: read
  pull-requests: read
safe-outputs:
  add-labels:
    allowed: [spam, ai-generated, link-spam, ai-inspected]
    target: "*"
  hide-comment:
    max: 5
    allowed-reasons: [spam]
  noop:
  threat-detection: false
checkout: false
features:
  gh-aw-detection: true
sandbox:
  agent:
    runtime: gvisor
```

*Source: `.github/workflows/ai-moderator.md` frontmatter, fetched directly
via `raw.githubusercontent.com/github/gh-aw/main/...` — note this workflow
also imports `shared/graders.md` (see `docs-ghaw-graders.md` Concrete
Artifacts, which independently confirms the same import in the CLI
Consistency Checker workflow).*

### AI Moderator probe-detection and burst-detection prompt excerpts (verbatim, from same source)

```
### 0. Probe Detection (Check First)

Before any other analysis, check if the issue or comment appears to be a
**probe** — an empty or minimal test submission with no real content or
intent:

- Issue title is a default/generic value (e.g., "New issue", "Test", "test
  issue", "hello", "hi", untitled)
- Issue body is empty, blank, or contains only whitespace
- Issue body is extremely short (fewer than 10 meaningful characters) and
  unrelated to the repository
- Issue body is a single word or placeholder (e.g., "test", "testing",
  "asdf", "hello")
- No description, context, or actionable content provided whatsoever

If any probe indicators are detected:
- **Immediately classify as spam** — label with `spam`
- Do NOT proceed with other detection tasks
- These are reconnaissance attempts to test system boundaries, not genuine
  contributions
```

```
### Burst Detection

After filtering, check if the current actor (${{ github.actor }}) has
**2 or more spam incidents in the last 24 hours**. If so, treat this as a
**burst** and increase your confidence that the current submission is also
spam — even if it is not an obvious probe.
```

*Source: `.github/workflows/ai-moderator.md` prompt body, "Detection
Tasks" and "Spam Tracking (Cache Memory)" sections.*

### Trajectory grader implementations named this week (from five independently fetched PRs)

```
event-entropy-rate               Tier 1, rank 10  — normalized bigram Shannon
                                                      entropy of the event process
lempel-ziv-trajectory-complexity Tier 1, rank 11  — LZ76 incremental-parsing
                                                      complexity, normalized to [0,1]
policy-near-miss                 Tier 2, rank 1   — successful traces that skipped a
                                                      required guard/policy check
exploration-error                Tier 2, rank 3   — objective failure attributed to
                                                      insufficient search density
exploitation-error               Tier 2, rank 4   — objective failure despite
                                                      sufficient gathered evidence
```

*Source: PR bodies #56464, #56972, #56996, #57087, #57152 respectively,
each independently fetched via `gh pr view --repo github/gh-aw`. "6 of 25
catalog graders now implemented" per PR #56464's body (at the time that PR
was merged, before the other four in this list).*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-agent-factory-status.md` (Codex-engine fleet listing naming
    "AI Moderator" among nine Codex workflows): Claim 8 here's `engine:
    codex` frontmatter directly confirms that prior fleet-inventory
    snapshot by name, from the workflow's own source rather than a
    secondary listing.
  - `docs-ghaw-threat-detection.md` Claim 4 (`threat-detection: false`
    disables the detection job entirely and is a deliberate, justified
    opt-out): Claim 8 here is a second, independently-confirmed real-world
    instance of this flag in use, with a distinct rationale from the
    `copilot-token-optimizer` case that note's Extraction Notes previously
    speculated about.
  - `docs-ghaw-feature-grower.md` Claim 10 (cadence guidance: use "All You
    Can Eat" with a ~30-minute schedule "when the next chunk should appear
    soon after the previous issue closes or pull request merges"): Claim 6
    here is a concrete, dated instance of exactly this guidance being
    applied to a real gh-aw-internal workflow three days before this post.

- **Contradicts**: None filed at the MINER.md §4a threshold. Claim 5's
  "Feature Farmer" vs. "Feature Grower" naming discrepancy is a
  presentation inconsistency within the *same* change (the PR's own title
  vs. its own shipped file names), not a disagreement between two
  independently-argued claims about what the pattern does — see Claim 5's
  assessment for why this does not meet the filing bar.

- **Extends**:
  - `docs-ghaw-triggers-reference.md` Claim 9 (`stop-after:` accepts only
    static relative-delta/absolute-date forms, calculated from compilation
    time): Claim 2 here documents the same field gaining GitHub Actions
    expression support in this release line — update, don't contradict,
    that note's snapshot.
  - `docs-ghaw-feature-grower.md` (entire note, especially Claims 1–3,
    Claim 10, and Concrete Artifacts): Claim 5 here identifies that this
    week's "Feature Farmer" PR (#56614) is the exact PR that shipped the
    "Feature Grower" pattern that note documents, and Claim 6 adds a
    second real-world worked example (the trajectory grader workflow's
    conversion) with a PR-title-based `skip-if-match` gate, complementing
    that note's issue-body-marker example.
  - `docs-ghaw-graders.md` Claims 3–5 (ten built-in grader IDs and
    4096-character custom inline JS graders) and Claim 6 (the
    `operational-value` grader's frozen-evaluator/attainment-score
    mechanism): Claim 7 here documents a third grader-authoring path —
    full importable workflow-fragment graders over a canonical Trajectory
    IR — not covered by either mechanism that note documents; Claim 4 here
    documents the `intent`/`IntentSpec` design vocabulary that appears to
    upstream-feed the `operational-value` grader's scoring criteria, which
    that note could not describe (out of scope for its source pages).
  - `blog-ghaw-weekly-2026-08-24.md` Claim 5 (Copilot SDK pre-ready crash
    now surfaces stderr tail instead of a bare exit signal): Claim 3 here
    is a same-family, different-engine instance of the same "opaque
    provider/runtime failure → captured, actionable diagnostic" hardening
    pattern, this time for Codex tool-schema mismatches.

- **Novel**:
  - **`on.cooldown` workflow-trigger gating** (Claim 1): first corpus
    documentation of this trigger primitive — a purely time-based gate
    distinct from the open-item gates (`skip-if-match`, "All You Can Eat")
    already documented.
  - **`intent`/`IntentSpec` design vocabulary** (Claim 4): first corpus
    mention of a named, design-time intent specification linked to
    operational-value grading criteria.
  - **The Feature Farmer/Feature Grower naming discrepancy** (Claim 5):
    not itself a new pattern, but a new, verifiable finding about how this
    week's post's own terminology diverges from the shipped artifact name.
  - **The trajectory grader catalog and Trajectory IR** (Claim 7): first
    corpus documentation of a ranked, 25-entry grader catalog and its
    `events[]`/`objectives[]` canonical trace representation, plus a novel
    three-way objective-failure-attribution taxonomy
    (policy-near-miss/exploration-error/exploitation-error).
  - **AI Moderator's full workflow source** (Claims 8–9): first corpus
    source with the complete frontmatter and prompt body for this
    specific, named agent (previously only listed by name in
    `docs-ghaw-agent-factory-status.md`'s fleet inventory).

## Guide Impact

- **Chapter 03 (Workflows & Orchestration)**:
  - Add `on.cooldown` (Claim 1) as a third scheduling-gate primitive
    alongside `skip-if-match` and `stop-after`, specifically for
    suppressing back-to-back triggers on hot event streams regardless of
    whether prior runs left an open item.
  - Update any existing `stop-after:` coverage (sourced from
    `docs-ghaw-triggers-reference.md` Claim 9) to note GitHub Actions
    expression support was added this release (Claim 2), and cite both
    notes together for the field's before/after behavior.
  - Cite Claim 5/Claim 6 when documenting the Feature Grower pattern
    (already covered via `docs-ghaw-feature-grower.md`): use "Feature
    Grower" as the canonical name, and add the trajectory-grader
    workflow's PR-title-based `skip-if-match` gate as a second worked
    cadence example.

- **Chapter 02 (Harness Engineering) / Chapter 06 (Observability)**:
  - Document the trajectory-grader catalog (Claim 7) as a third
    grader-authoring path beyond `docs-ghaw-graders.md`'s built-ins and
    inline JS — full importable workflow-fragment graders over a Trajectory
    IR — and flag the catalog README and Trajectory IR schema as follow-up
    sources.
  - Add the Codex tool-schema diagnostic fix (Claim 3) as a further
    engine-hardening data point alongside the Copilot SDK stderr-capture
    fix already documented in `blog-ghaw-weekly-2026-08-24.md` Claim 5.

- **Chapter 03 (Safety and Verification)**:
  - Add AI Moderator (Claims 8–9) as the reference example for
    `threat-detection: false` used as a deliberate, justified opt-out in a
    high-volume public-trigger context — contrast its rationale (narrow
    safe-output surface plus other guardrails) with the
    `copilot-token-optimizer` rationale (avoiding AI-detection false
    positives) already noted in `docs-ghaw-threat-detection.md`.
  - Cite the probe-detection-first prompt ordering and the explicit
    "missing cache file is not an error" guard (Claim 9) as reusable
    prompt-design patterns for moderation/triage workflows combining a
    priority classification pass with cross-run cache memory.

- **Chapter 04 (Agent Patterns)**:
  - Document `intent`/`IntentSpec` (Claim 4) as the design-time vocabulary
    that upstream-feeds `operational-value` grader scoring criteria
    (`docs-ghaw-graders.md` Claim 6), pending a follow-up fetch of PR
    #56599 for the `intent:` frontmatter field's exact schema.

## Extraction Notes

1. **Raw HTML fetched via `curl` and parsed with a Python regex-based
   tag-stripping pass**, following the practice established in prior
   weekly notes (e.g. `blog-ghaw-weekly-2026-08-24.md` Extraction Note 1).
   An initial WebFetch pass was also run for comparison and produced a
   materially paraphrased/compressed version of the post (e.g. rendering
   "GitHub Actions expressions alongside static values" and inventing
   section wording not present verbatim on the page); all quotes in this
   note are taken from the raw-HTML extraction, not the WebFetch summary.

2. **Six linked pages were followed and fetched directly**, within (and
   slightly exceeding, given the number of substantive named items this
   post covers) the "up to 5" budget in MINER.md §1: PR #56998
   (`on.cooldown`), PR #56983 (typed `stop-after`), PR #57256 (Codex
   diagnostics), PR #57005 (intent-driven design docs), PR #56614
   ("Feature Farmer"/Feature Grower), and PR #56988 (trajectory-grader
   All-You-Can-Eat conversion) — each fetched via `gh pr view <N> --repo
   github/gh-aw --json title,body,files,createdAt,mergedAt`. Two further
   PRs (#57253 MCP payload pagination, #56505 private Agent Plugin
   authentication) and five trajectory-grader PRs (#56464, #56972, #56996,
   #57087, #57152) were also independently fetched; the five
   trajectory-grader PRs are used in Claim 7 and Concrete Artifacts, while
   #57253 and #56505 were read but judged to not clear the bar for a
   dedicated claim beyond what the blog's one-sentence descriptions
   already state (both are narrow reliability/feature fixes without
   further design implications worth a claim entry) — their PR numbers are
   recorded here in case a future note needs to re-fetch them.
   `.github/workflows/ai-moderator.md` was fetched directly via
   `raw.githubusercontent.com` (its full frontmatter and prompt body are
   reproduced in Concrete Artifacts).

3. **Not fetched, flagged as follow-up sources**: PR #56599 (the earlier,
   separate PR that shipped the base `intent:` frontmatter field, referenced
   by PR #57005's own body but not itself examined here); the trajectory
   grader catalog README (`.github/workflows/shared/graders/README.md`,
   referenced by name in all five trajectory-grader PR bodies but not
   fetched — would give the full 25-grader list and Trajectory IR schema);
   `shared/graders.md` (the shared import both AI Moderator and the CLI
   Consistency Checker use, per `docs-ghaw-graders.md` Concrete Artifacts —
   still not independently fetched by any note in this corpus as of this
   extraction).

4. **Cross-reference check performed** against
   `docs-ghaw-triggers-reference.md`, `docs-ghaw-feature-grower.md`,
   `docs-ghaw-graders.md`, `docs-ghaw-threat-detection.md`,
   `docs-ghaw-agent-factory-status.md`, `docs-ghaw-measuring-impact.md`,
   `blog-ghaw-weekly-2026-08-24.md`, and `blog-ghaw-custom-linters-three-workflow-loop.md`,
   plus `CONTRADICTIONS.md` (all eight existing entries, C-001–C-008) for
   open contradiction threads. No claim here rises to the MINER.md §4a
   filing bar for a new contradiction issue.

5. **`confidence_overall` set to `settled`**: unlike several prior gh-aw
   docs-page notes in this corpus (e.g. `docs-ghaw-graders.md`,
   `docs-ghaw-threat-detection.md`, rated `emerging` because their source
   pages describe explicitly experimental features or rely on an
   AI-summarized fetch for some quotes), every claim in this note is
   sourced either from the blog's own prose or from first-party PR
   bodies/workflow source files fetched directly (via `curl` or `gh pr
   view`/`raw.githubusercontent.com`), describing already-merged,
   already-shipped changes with no "experimental"/"draft" framing in any
   of the underlying sources.
