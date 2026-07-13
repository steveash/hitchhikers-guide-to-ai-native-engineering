---
source_url: https://github.github.com/gh-aw/blog/2026-07-13-weekly-update/
source_type: blog-post
title: "Weekly Update – July 13, 2026 (GitHub Agentic Workflows)"
author: GitHub Agentic Workflows team (gh-aw); byline "Copilot"
date_published: 2026-07-13
date_extracted: 2026-07-13
last_checked: 2026-07-13
status: current
confidence_overall: emerging
issue: "#1814"
---

# Weekly Update – July 13, 2026 (GitHub Agentic Workflows)

> v0.82.8 (published July 11) adds two new sandbox runtime options — a gVisor
> container runtime (PR #44796) and a KVM-isolated `docker-sbx` microVM runtime
> (PR #45006) — expanding `sandbox.agent.runtime` beyond the AWF-only model
> documented in `docs-ghaw-sandbox-reference.md`. A second fix (PR #45146) emits
> a fresh `sbx login` immediately before agent execution to resolve intermittent
> "user is not authenticated to Docker" errors caused by Docker Hub OAuth token
> expiry between daemon setup and agent run. A new `private-to-public-flows: allow`
> frontmatter field (PR #45113) lets teams opt specific MCP servers out of
> sink-visibility enforcement. The `aw-failure-investigator` Agent of the Week —
> previously profiled in `blog-ghaw-weekly-2026-06-15.md` Claim 13 at ~1.57M
> tokens/run — is revisited with post-AI-Credits-migration cost figures (250+ AIC
> per run on claude-opus-4-8) and a self-referential anecdote: one of its three
> July 11–12 runs failed, and it recovered cleanly on the next scheduled cycle.

## Source Context

- **Type**: blog-post (weekly changelog/update from the official GitHub Agentic
  Workflows blog; covers the week around the July 11, 2026 release of v0.82.8;
  five "What's New" release-note items, five additional "Notable Pull Requests"
  not bundled into the release notes, and an Agent of the Week revisit)
- **Author credibility**: The gh-aw blog is the official publication of GitHub's
  Agentic Workflows platform team. The page's `schema.org/BlogPosting` JSON-LD
  and on-page byline both name the author as "Copilot" (same non-human byline
  pattern as `blog-ghaw-weekly-2026-07-06.md`, distinct from the human-bylined
  "Meet the Workflows" series by Don Syme / Peli de Halleux / Mara Kiefer). PR
  numbers appear as visible inline text in this post (e.g., "gVisor container
  runtime (#44796)"), unlike the July 6 post where they were link-only —
  verified directly against the raw page HTML, not a WebFetch summary (see
  Extraction Notes).
- **Scope**: Ten named PRs across sandbox runtime selection, MCP-server-visibility
  control, credential lifecycle, dependency resolution, and safe-output tooling,
  plus one Agent of the Week spotlight (`aw-failure-investigator`, its second
  appearance in this corpus). Does NOT cover: the internal implementation of the
  gVisor or docker-sbx runtime integrations; the full guard-policy schema for
  `private-to-public-flows`; the root cause or fix details of the July 11th
  `aw-failure-investigator` self-failure beyond "had its own failure... bounced
  back cleanly"; or exact per-PR authorship/reviewer information.

## Extracted Claims

### Claim 1: v0.82.8 (published July 11, 2026) adds `sandbox.agent.runtime: gvisor` as a new sandbox runtime option, running the agent inside a gVisor sandbox for stronger isolation on workflows that process untrusted input

- **Evidence**: "What's New" list item, PR #44796.
- **Confidence**: emerging (single PR, first-party changelog description; the
  underlying gVisor integration mechanism, performance overhead, and compatibility
  constraints are not described in this post)
- **Quote**: "gVisor container runtime (#44796): Set `sandbox.agent.runtime: gvisor`
  in your workflow frontmatter to run the agent inside a gVisor sandbox for
  stronger isolation — great for workflows processing untrusted input."
- **Our assessment**: `docs-ghaw-sandbox-reference.md` (extracted 2026-05-12) documents
  `sandbox.agent` as accepting only `awf` (default) or `false` (partial disable) —
  no `runtime` sub-field and no non-AWF runtime option appears anywhere in that
  reference. This PR is the first evidence in the corpus that `sandbox.agent` has
  grown a `runtime` sub-field with alternative isolation backends, a structural
  change to the sandbox configuration schema beyond what that reference describes.
  gVisor itself is a well-known user-space kernel-emulation sandbox (used by Google
  gVisor/runsc) that intercepts syscalls without full hardware virtualization —
  lighter-weight than a microVM but stronger than a bare container namespace. For
  Ch02 (Harness Engineering): update the sandbox configuration reference to note
  `sandbox.agent.runtime` as a new selector field, with `gvisor` as one option
  positioned for untrusted-input workflows; this doesn't replace AWF's network/
  filesystem controls (`docs-ghaw-sandbox-reference.md` Claims 2–7) but adds a
  process-isolation dimension alongside them.

### Claim 2: Shared workflow partials can now declare `sandbox.agent.mounts`, and these mount configurations merge into the parent workflow, enabling reusable sandbox setups without copy-pasting mount declarations

- **Evidence**: "What's New" list item, PR #44500.
- **Confidence**: emerging (single PR, first-party changelog description; the
  merge semantics when parent and partial both declare mounts, e.g. override vs.
  union, are not specified)
- **Quote**: "Shared partials can declare `sandbox.agent.mounts` (#44500): Partial
  workflow files can now define mount configurations that get merged into the
  parent, enabling reusable sandbox setups without copy-paste."
- **Our assessment**: This extends the shared-workflow-partial pattern (already
  used for `network:` and other frontmatter blocks per general gh-aw partial
  composition) to sandbox mount configuration specifically. For teams standardizing
  sandbox setups across many workflows, this removes a class of configuration
  drift where each workflow file must independently repeat identical mount
  declarations. For Ch02: add `sandbox.agent.mounts` to the list of frontmatter
  fields supported in shared partials, alongside whatever fields
  `docs-ghaw-sharing-workflows.md` already documents as partial-composable.

### Claim 3: A new `disclosure-header` safe-output message type lets agents declare AI authorship inline in PR comments and issues

- **Evidence**: "What's New" list item, PR #44497.
- **Confidence**: emerging (single PR, first-party changelog description; the
  exact header format/content and whether it is opt-in or automatically applied
  are not described)
- **Quote**: "AI authorship disclosure header (#44497): A new `disclosure-header`
  safe-output message type lets agents declare AI authorship inline in PR comments
  and issues."
- **Our assessment**: This is a transparency/disclosure mechanism at the safe-output
  layer — the same layer documented in `docs-ghaw-safe-outputs-specification.md` —
  rather than a sandbox or credential control. No existing corpus note documents
  an AI-authorship disclosure convention for gh-aw's own safe outputs; this is the
  first appearance of "declare AI authorship inline" as a named, built-in message
  type rather than a manually-authored disclaimer. For Ch04 (Safety and
  Constraints): add `disclosure-header` as a concrete mechanism for AI-authorship
  transparency in agent-generated PR comments/issues — relevant to any guide
  section on responsible-disclosure norms for agent-authored content.

### Claim 4: `gh aw add` now automatically resolves transitive `uses:` references, so importing a workflow partial pulls in any nested imports without manual dependency hunting

- **Evidence**: "What's New" list item, PR #44763.
- **Confidence**: emerging (single PR, first-party changelog description; whether
  this changes existing lockfile/compilation output for previously-imported
  workflows, or only affects new imports, is not stated)
- **Quote**: "`gh aw add` resolves transitive `uses:` references (#44763): Importing
  a workflow partial now automatically pulls in any nested imports — no more manual
  dependency hunting."
- **Our assessment**: This is a dependency-resolution usability fix for the
  workflow-sharing/import mechanism (`docs-ghaw-sharing-workflows.md`), analogous
  to a package manager resolving transitive dependencies rather than requiring the
  importer to manually list every nested `uses:` reference. For Ch02: note this as
  a `gh aw add` behavior change — teams that previously worked around missing
  transitive resolution by manually copying nested partials should be able to
  simplify their import process after upgrading to v0.82.8.

### Claim 5: OAuth token failures now surface visibly in the conclusion job rather than being silently swallowed

- **Evidence**: "What's New" list item, PR #44777 and PR #44756 (two PRs credited
  for this item).
- **Confidence**: emerging (single changelog line covering two PRs; the prior
  failure mode — what "silently swallowed" looked like operationally, e.g. a
  green run with no output vs. a generic error — is not described)
- **Quote**: "OAuth token failures surface in conclusion job (#44777, #44756):
  Token failures are no longer silently swallowed — they now show up where you'd
  expect."
- **Our assessment**: This is a diagnosability fix for the `conclusion` job —
  the same job `docs-ghaw-compilation-process.md` documents as running `always()`
  to aggregate results when safe outputs exist (per
  `blog-ghaw-weekly-2026-07-06.md` Claim 1's description of that job's role).
  Silently-swallowed auth failures are a class of bug where a workflow appears to
  succeed (or fails with a misleading generic error) while the actual root cause —
  an expired or invalid OAuth token — never reaches a human. For Ch02: this
  generalizes beyond OAuth specifically — any credential/auth failure that a
  compiler-generated job graph can swallow silently is worth an explicit
  "surface this in conclusion" design rule, alongside PR #43570's dependency
  auto-wiring fix (`blog-ghaw-weekly-2026-07-06.md` Claim 1) as another example of
  the `conclusion`/`pre_activation` job plumbing receiving correctness attention
  across consecutive weekly releases.

### Claim 6: `docker-sbx` is a new sandbox runtime (`sandbox.agent.runtime: docker-sbx`) that runs the agent inside a KVM-isolated Docker sbx microVM while keeping infrastructure containers on the host, for workloads needing full hardware-virtualization isolation

- **Evidence**: "Notable Pull Requests This Week" list item, PR #45006.
- **Confidence**: emerging (single PR, first-party changelog description; no
  performance/cost comparison against gVisor or AWF is given, and "keeping
  infrastructure containers on the host" is not elaborated)
- **Quote**: "docker-sbx runtime support — You can now run your agent inside a
  KVM-isolated Docker sbx microVM (`sandbox.agent.runtime: docker-sbx`) while
  keeping infrastructure containers on the host. Full hardware-virtualization
  isolation for workloads that need it."
- **Our assessment**: Together with Claim 1 (gVisor), this establishes
  `sandbox.agent.runtime` as a three-way (at minimum) selector: the default AWF
  firewall-based sandbox (`docs-ghaw-sandbox-reference.md` Claims 1–8), a gVisor
  user-space-kernel sandbox (lighter-weight process isolation), and now a
  KVM-isolated microVM (hardware virtualization — the strongest isolation tier of
  the three, at presumably the highest overhead). This is a genuine architectural
  shift from "one firewall sandbox with on/off + mount options" to "choose your
  isolation tier by threat model," which the Prospector's triage comment
  anticipated. For Ch02/Ch03 (Harness Engineering / Safety and Constraints): add a
  decision framework for `sandbox.agent.runtime` selection — AWF for the default/
  general case, gVisor for untrusted-input workflows needing lighter isolation
  than a full VM, docker-sbx/microVM for workloads requiring hardware-level
  isolation guarantees (e.g., processing genuinely adversarial input, multi-tenant
  execution). No cost or latency data is given for any of the three tiers in this
  source, so the guide should flag that trade-off as unverified pending further
  sources.

### Claim 7: A Docker Hub OAuth token obtained during the daemon-setup step could expire before the agent ran, causing intermittent "user is not authenticated to Docker" errors on `sbx`-runtime workflows; the fix (PR #45146) runs a fresh `sbx login` immediately before agent execution for all `sbx`-runtime workflows

- **Evidence**: "Notable Pull Requests This Week" list item, PR #45146, plus the
  post's opening paragraph, which independently frames this as the week's headline
  fix.
- **Confidence**: settled (specific PR, the failure symptom is quoted verbatim,
  the root cause (token-expiry race between daemon setup and agent execution) and
  fix mechanism (re-run `sbx login` immediately before agent execution) are both
  named)
- **Quote**: "Emit sbx credential refresh before agent execution — Fixes those
  maddening intermittent `"user is not authenticated to Docker"` errors. Docker
  Hub OAuth tokens from the daemon-setup step could expire by the time the agent
  ran. Now a fresh `sbx login` runs immediately before agent execution for all
  `sbx`-runtime workflows." Opening paragraph: "we... squashed a frustrating Docker
  authentication bug that had been interrupting `sbx`-runtime workflows."
- **Our assessment**: This is a concrete instance of a credential-lifecycle bug
  class familiar from any system that acquires a short-lived token early in a
  pipeline and consumes it later: if the time-to-live is shorter than the gap
  between acquisition and use, the token can expire mid-pipeline, and the failure
  presents as an intermittent authentication error rather than a deterministic one
  (making it hard to reproduce and easy to misdiagnose as flakiness). The fix
  pattern — move the credential-refresh step to immediately precede the consuming
  step, rather than refreshing once early and hoping the token outlives the whole
  job — generalizes to any agentic harness that provisions infra (Docker daemons,
  cloud sessions, database connections) in a setup phase distinct from the agent
  execution phase. No existing corpus note documents a Docker-Hub-token-expiry
  failure mode specifically (`docs-ghaw-sandbox-reference.md` documents AWF's
  environment/PATH handling but not `sbx`-runtime credential lifecycle at all —
  `sbx` as a runtime name doesn't appear in that reference, consistent with
  `docker-sbx`/`sbx`-runtime being a newer addition than that reference's May 2026
  extraction date). For Ch02 (Harness Engineering): add "refresh short-lived
  credentials immediately before the step that consumes them, not once at
  pipeline start" as a named credential-lifecycle pattern, with this Docker Hub
  OAuth case as the concrete example.

### Claim 8: A new `private-to-public-flows: allow` frontmatter field wires the frontmatter → struct → gateway JSON pipeline for `tools.github.private-to-public-flows`, letting workflow authors opt specific MCP servers out of sink-visibility enforcement when they explicitly trust those flows

- **Evidence**: "Notable Pull Requests This Week" list item, PR #45113.
- **Confidence**: emerging (single PR, first-party changelog description; the
  definition of "sink-visibility enforcement" itself, what a "flow" denotes
  concretely, and the default behavior when the field is omitted are not
  explained in this post)
- **Quote**: "`private-to-public-flows: allow` frontmatter field — Wires the full
  frontmatter → struct → gateway JSON pipeline for
  `tools.github.private-to-public-flows`, letting you opt specific MCP servers out
  of `sink-visibility` enforcement when you explicitly trust those flows."
- **Our assessment**: No existing corpus note — including
  `docs-ghaw-mcp-gateway-reference.md` (the RFC-style MCP Gateway spec, extracted
  2026-06-21, which documents a guard-policy framework using *integrity levels*
  for upstream auth) — mentions "sink-visibility" as a concept or
  "private-to-public-flows" as a field. This reads as a data-exfiltration control:
  "sink-visibility enforcement" plausibly restricts whether output computed from
  private-repository data can flow to public-repository-visible sinks (comments,
  issues, PRs) by default, with this field as an explicit, named opt-out for
  specific MCP servers. That would make it a policy control distinct from the
  gateway's integrity-level guard policy (`docs-ghaw-mcp-gateway-reference.md`
  Claim 1 and surrounding claims) — integrity levels gate *what* a server can do,
  while sink-visibility (as best we can infer, absent a definition in this source)
  gates *where private data can flow to*. We flag this as an inference, not a
  verified claim, since the source does not define "sink-visibility" directly. For
  Ch04 (Safety and Constraints): flag `private-to-public-flows` and
  "sink-visibility enforcement" as a new gh-aw safety primitive worth a dedicated
  follow-up source note once the underlying reference documentation for this field
  is published — this note alone is insufficient to fully specify the guide's
  private-data-flow guidance.

### Claim 9: The pinned gVisor release was bumped to 20250707.0 to keep the sandbox runtime current with upstream security and reliability patches

- **Evidence**: "Notable Pull Requests This Week" list item, PR #45101.
- **Confidence**: settled (specific PR, specific version string named)
- **Quote**: "Bump gVisor release to 20250707.0 — Keeps the pinned gVisor release
  current with upstream security and reliability patches."
- **Our assessment**: A routine dependency-currency maintenance PR, notable mainly
  as corroborating evidence that gVisor (Claim 1) is a pinned, versioned
  dependency the gh-aw team tracks and updates deliberately — not a
  set-and-forget integration. For Ch02: minor; worth a one-line mention that
  gVisor sandbox support carries its own upstream-patch-tracking maintenance
  burden, same as any pinned third-party dependency.

### Claim 10: Missing copilot safe-output fixture files were added for `close-discussion`, `assign-to-agent`, `assign-to-user`, and `unassign-from-user`, filling gaps in the safe-output test suite

- **Evidence**: "Notable Pull Requests This Week" list item, PR #45004.
- **Confidence**: settled (specific PR, four specific fixture/message types named)
- **Quote**: "Add missing copilot safe-output fixture files — Adds fixtures for
  `close-discussion`, `assign-to-agent`, `assign-to-user`, and
  `unassign-from-user`, filling gaps in the safe-output test suite."
- **Our assessment**: A test-coverage hygiene PR for the Copilot engine's
  safe-output message types, complementary to the `disclosure-header` message
  type added this same week (Claim 3) — both are additions/fixes to the
  safe-output surface documented at the specification level in
  `docs-ghaw-safe-outputs-specification.md`. For Ch02: minor; worth noting only
  as evidence that safe-output message-type test coverage is an ongoing,
  incrementally-filled area rather than a one-time specification exercise.

### Claim 11: `aw-failure-investigator` ran three times across July 11–12, 2026, filing 3 issues in total (2 from one run, 1 from another); one of the three runs itself failed on July 11th but the workflow recovered cleanly on its next scheduled cycle

- **Evidence**: "Agent of the Week" section, two adjacent sentences describing the
  week's run outcomes and the July 11th self-failure.
- **Confidence**: anecdotal (single narrative account of three runs over a
  two-day window; no root cause is given for the July 11th failure beyond "had
  its own failure," and it is not stated whether the failed run is one of the
  "three runs" whose issue-filing count (2+1=3) is reported, or a fourth,
  unfiled-count run — see Extraction Notes)
- **Quote**: "This week `aw-failure-investigator` ran three times across July
  11–12, filing 3 issues in total (2 in one run, 1 in another). Each run clocked
  in around 15 minutes and consumed 250+ AI credits running on claude-opus-4-8 —
  because when you're investigating failures, you don't want to cut corners. The
  July 11th run had its own failure (meta!), but bounced back cleanly on its next
  scheduled cycle."
- **Our assessment**: `blog-ghaw-weekly-2026-06-15.md` Claim 13 first documented
  `aw-failure-investigator` as the Agent of the Week (June 14–15, 2026) at ~1.57M
  tokens/run, ~4.7M tokens/week across three 6-hour-schedule runs, 16.6
  minutes/investigation. This is the first time in the corpus that the *same*
  named agent receives a second, separate Agent of the Week spotlight — every
  other Agent of the Week in the corpus (`api-consumption-report`,
  `weekly-issue-summary`, `delight`, etc., per `blog-ghaw-weekly-2026-06-01.md`,
  `blog-ghaw-weekly-2026-07-06.md`, `blog-ghaw-weekly-2026-06-22.md`) has appeared
  exactly once. The metrics are not directly comparable across the two spotlights:
  June 15 reports token counts (pre-AI-Credits-migration unit), while July 13
  reports AI Credits (250+ AIC ≈ $2.50+ per run per
  `blog-ghaw-ai-credits-migration.md` Claim 7's 1 AIC = $0.01 USD conversion) — the
  migration itself is documented in that note, dated after June 15 in the corpus
  timeline. This is also the first corpus source to name the specific LLM model
  (`claude-opus-4-8`) that `aw-failure-investigator` runs on; no prior spotlight of
  this agent named a model. `blog-ghaw-weekly-2026-07-06.md` Claim 7 separately
  documents a *different* scheduled agent (`weekly-issue-summary`) whose June 15th
  run was flagged by "the observability report" and recommended a smaller model
  after a "heavy execution profile" — by contrast, this post's framing of
  `aw-failure-investigator`'s cost ("you don't want to cut corners") explicitly
  argues *against* downsizing this particular agent's model, i.e., an editorial
  case for accepting higher per-run cost for investigation depth rather than an
  automatic right-sizing recommendation. For Ch06 (Agentic Operations): update the
  `aw-failure-investigator` cost profile with the July 13 AIC figure alongside the
  June 15 token figure (flagging the unit change rather than converting one to
  the other, since no stated AIC-per-token conversion is given in either source);
  add "a scheduled monitoring/investigation agent can itself fail and recover on
  its next scheduled run" as a concrete example of self-healing-by-schedule for
  monitoring agents, distinct from a one-off crash requiring manual intervention.

### Claim 12: In one particularly busy shift, `aw-failure-investigator` made 13 GitHub API calls in 15 minutes

- **Evidence**: "Agent of the Week" section, standalone sentence following the
  three-run summary.
- **Confidence**: anecdotal (a single described shift, not stated whether typical
  or an outlier; the post itself frames it ambiguously — "either impressive
  efficiency or evidence that it found a lot to worry about")
- **Quote**: "In one particularly busy shift it made 13 GitHub API calls in 15
  minutes, which is either impressive efficiency or evidence that it found a lot
  to worry about. Probably both."
- **Our assessment**: We flag this because an earlier WebFetch pass against this
  same source page (a summarized/condensed extraction, not the raw HTML) rendered
  this same figure as "making approximately 13 API calls during peak operation
  periods" attached to "recent runs" in general, losing the "one particularly busy
  shift" qualifier and the post's own explicit uncertainty about whether 13 calls
  is efficient or symptomatic. This is not a claim from the source itself but an
  artifact of relying on a condensed AI-summarized fetch rather than the raw page
  — see Extraction Notes. Taken from the raw HTML, the correct reading is: 13 API
  calls in 15 minutes describes one specific (self-described as unusually busy)
  shift, not a per-run average across the week's three runs. For the Assayer:
  verify this figure against the raw page, not a WebFetch summary, given the
  demonstrated discrepancy.

### Claim 13: The post recommends pairing `aw-failure-investigator` with a label-based notification rule so the responsible team is pinged asynchronously when it files an issue, without requiring anyone to watch the Actions tab

- **Evidence**: "Usage tip" callout at the end of the Agent of the Week section.
- **Confidence**: anecdotal (a single usage recommendation from the workflow's own
  authors, not independently tested or measured in this post)
- **Quote**: "Usage tip: Pair `aw-failure-investigator` with a label-based
  notification rule so the right team gets pinged when it files an issue — that
  way failures surface asynchronously without requiring anyone to watch the
  Actions tab."
- **Our assessment**: This is the same category of "pair the reporting/monitoring
  agent with a labeling strategy" usage tip that
  `blog-ghaw-weekly-2026-07-06.md` Claim 8 documents for `weekly-issue-summary`
  (pair with a consistent issue-label strategy for better chart breakdowns) — a
  second instance of the same underlying pattern (a monitoring/reporting agent's
  output value depends on a labeling convention the agent itself doesn't create),
  but applied here to routing *notifications* to the right team rather than to
  *segmenting analytics charts*. For Ch06 (Agentic Operations): add this as a
  second data point for the "monitoring agent + labeling convention" pairing
  pattern established by the July 6 note, distinguishing the two use cases
  (notification routing vs. chart segmentation) as two applications of the same
  underlying dependency.

## Concrete Artifacts

### Release Summary: v0.82.8 (published July 11, 2026)

```
What's New:
  gVisor container runtime (#44796)
    sandbox.agent.runtime: gvisor — stronger isolation for untrusted input
  Shared partials: sandbox.agent.mounts (#44500)
    Partial workflow files can declare mount configs merged into the parent
  AI authorship disclosure header (#44497)
    New `disclosure-header` safe-output message type for PR comments/issues
  gh aw add resolves transitive uses: references (#44763)
    Nested imports auto-pulled; no manual dependency hunting
  OAuth token failures surface in conclusion job (#44777, #44756)
    Token failures no longer silently swallowed

Notable Pull Requests This Week:
  docker-sbx runtime support (#45006)
    sandbox.agent.runtime: docker-sbx — KVM-isolated microVM,
    infra containers stay on host
  Emit sbx credential refresh before agent execution (#45146)
    Root cause: Docker Hub OAuth tokens from daemon-setup step could expire
                before agent ran -> intermittent "user is not authenticated
                to Docker" errors
    Fix: fresh `sbx login` runs immediately before agent execution for all
         sbx-runtime workflows
  private-to-public-flows: allow frontmatter field (#45113)
    Wires frontmatter -> struct -> gateway JSON pipeline for
    tools.github.private-to-public-flows
    Lets specific MCP servers opt out of sink-visibility enforcement
  Bump gVisor release to 20250707.0 (#45101)
  Add missing copilot safe-output fixture files (#45004)
    Fixtures added: close-discussion, assign-to-agent, assign-to-user,
    unassign-from-user
```

*Source: this week's blog post, "What's New" and "Notable Pull Requests This Week"
sections (raw HTML fetched 2026-07-13)*

### Agent of the Week: `aw-failure-investigator` — July 11–12, 2026 (second spotlight)

```
Agent:          aw-failure-investigator
Function:       "on-call teammate" — wakes every 6 hours, scans recent
                workflow run failures, files GitHub issues
Schedule:       Every 6 hours

This week's runs (July 11-12, 2026):
  Total runs:        3
  Issues filed:      3 total (2 from one run, 1 from another)
  Duration:          ~15 minutes per run
  Cost:              250+ AI Credits per run (~$2.50+ at 1 AIC = $0.01 USD,
                     per blog-ghaw-ai-credits-migration.md Claim 7)
  Model:             claude-opus-4-8 (first time this agent's model is named
                     in the corpus)
  Notable incident:  July 11th run had its own failure ("meta!"); recovered
                     cleanly on next scheduled cycle
  Busy-shift stat:   13 GitHub API calls in 15 minutes ("one particularly
                     busy shift" — not stated as a per-run average)

Usage tip (from source): pair with a label-based notification rule so the
  right team is pinged asynchronously when it files an issue

Workflow definition:
  https://github.com/github/gh-aw/blob/main/.github/workflows/aw-failure-investigator.md

Prior spotlight (for comparison — blog-ghaw-weekly-2026-06-15.md Claim 13,
June 14-15, 2026):
  ~1.57M tokens/run, ~4.7M tokens/week across 3 runs, 16.6 min/investigation
  (pre-AI-Credits-migration unit; not directly convertible to this week's AIC
  figure without a stated tokens-per-AIC rate)
```

*Source: this week's blog post, "Agent of the Week" section (raw HTML fetched
2026-07-13); prior-spotlight figures from `blog-ghaw-weekly-2026-06-15.md` Claim 13*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-weekly-2026-06-15.md` Claim 13 (`aw-failure-investigator`
    established as an Agent of the Week, 6-hour schedule, files issues on
    detected failures): Claim 11 here corroborates the 6-hour schedule and the
    issue-filing behavior, updating the cost/duration figures for a second,
    later spotlight of the same agent.
  - `blog-ghaw-ai-credits-migration.md` Claim 7 (1 AIC = $0.01 USD): the 250+
    AIC figure in Claim 11 uses the post-migration unit, consistent with all
    gh-aw cost reporting in the corpus since that migration (e.g.
    `blog-ghaw-weekly-2026-06-29.md`'s ~24 AIC persona-rotation figure,
    `blog-ghaw-weekly-2026-07-06.md` Claim 6's ~59 AIC `weekly-issue-summary`
    figure).
  - `blog-ghaw-weekly-2026-06-29.md` Claim 2 (sandbox hardening milestone:
    `sandbox.agent.sudo: false` on 80.16% of workflows): that note documents a
    *privilege-restriction* dimension of sandbox hardening; Claims 1 and 6 here
    document a *runtime-selection* dimension (gVisor, docker-sbx) — both are
    part of the same broader sandbox-hardening effort the Prospector's triage
    comment identified across recent weekly updates, but along different axes
    (what the agent can do vs. what isolates the agent's execution).

- **Extends**:
  - `docs-ghaw-sandbox-reference.md` (documents `sandbox.agent: awf` default and
    `sandbox.agent: false` as the only two `sandbox.agent` values as of its
    2026-05-12 extraction, plus the three-tier AWF filesystem model): Claims 1
    and 6 here document `sandbox.agent.runtime` as a new sub-field with `gvisor`
    and `docker-sbx` values that did not exist in that reference at extraction
    time — this is a schema extension the existing note does not cover and
    should be updated to reflect. Claim 2 here (`sandbox.agent.mounts` in shared
    partials) extends that same reference's sandbox configuration surface into
    the shared-partial composition mechanism.
  - `blog-ghaw-weekly-2026-07-06.md` Claim 8 (usage tip: pair
    `weekly-issue-summary` with a consistent label strategy for chart
    breakdowns): Claim 13 here is a second instance of "pair the monitoring/
    reporting agent with a labeling convention," applied to notification routing
    rather than chart segmentation.
  - `blog-ghaw-weekly-2026-07-06.md` Claim 1 (compiler auto-wires
    `pre_activation` job dependency when a template references its outputs,
    fixing broken generated expressions in `safe_outputs`/`conclusion` jobs):
    Claim 5 here (OAuth token failures now surface in the `conclusion` job
    rather than being silently swallowed) is a second correctness fix to the
    same `conclusion`/`pre_activation` job-graph machinery in consecutive
    weekly releases.
  - `docs-ghaw-mcp-gateway-reference.md`
    (RFC-style MCP Gateway spec; guard-policy framework using integrity levels
    for upstream auth): Claim 8 here (`private-to-public-flows` /
    "sink-visibility enforcement") introduces an MCP-server visibility control
    that is not part of that spec's documented guard-policy vocabulary —
    plausibly a distinct policy dimension (data-flow direction) layered above
    or alongside integrity-level gating, but this source does not define the
    term, so the relationship is inferred, not confirmed.

- **Contradicts**: None identified at the MINER.md §4a filing threshold. No
  claim in this source materially opposes an existing source note's claim on
  the same topic. See Claim 11's discussion of the June 15 vs. July 13
  `aw-failure-investigator` cost figures — these are not contradictory, just
  reported in different units (tokens vs. AI Credits) across a metric-system
  migration already documented in `blog-ghaw-ai-credits-migration.md`.

- **Novel**:
  - **`sandbox.agent.runtime` as a multi-tier isolation selector** (Claims 1, 6):
    the first corpus source documenting that gh-aw's sandbox model has grown
    beyond "AWF firewall, on or off" into a choice of isolation backends
    (AWF / gVisor / docker-sbx-microVM), each presumably trading off overhead
    against isolation strength — no existing note names more than the single
    AWF runtime.
  - **`sink-visibility` enforcement and `private-to-public-flows`** (Claim 8):
    entirely new terminology and mechanism to the corpus; no existing source
    note (including the MCP Gateway RFC spec) mentions a visibility-enforcement
    control gating data flow from private to public contexts.
  - **Docker Hub OAuth token expiry as a named credential-lifecycle failure
    mode for `sbx`-runtime workflows** (Claim 7): the first corpus source
    describing a concrete token-expiry race condition between a daemon-setup
    phase and agent-execution phase, and the "refresh immediately before
    consumption" fix pattern.
  - **A named agent (`aw-failure-investigator`) receiving a second, separate
    Agent of the Week spotlight** (Claim 11): the first time in the corpus the
    same agent is featured twice, allowing a same-agent cost/behavior
    comparison across a metric-unit migration (tokens → AI Credits) that no
    other corpus agent currently supports.
  - **A monitoring/investigation agent failing and self-recovering on its next
    scheduled run** (Claim 11): distinct from `weekly-issue-summary`'s
    timeout-and-bail failure mode documented in
    `blog-ghaw-weekly-2026-07-06.md` Claim 7 — here the agent that itself
    investigates failures is the one that failed, with no stated root cause
    beyond "had its own failure."

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Update the sandbox configuration guidance (currently reflecting
    `docs-ghaw-sandbox-reference.md`'s AWF-only model) to add
    `sandbox.agent.runtime` as a selector field with (at least) `awf`
    (default), `gvisor`, and `docker-sbx` values (Claims 1, 6) — with an
    explicit caveat that no cost/latency comparison across the three tiers is
    documented yet in the corpus.
  - Add `sandbox.agent.mounts` in shared partials (Claim 2) to the
    partial-composable frontmatter fields list.
  - Add "refresh short-lived credentials immediately before the consuming
    step, not once at pipeline start" (Claim 7, the `sbx login` / Docker Hub
    OAuth fix) as a named credential-lifecycle pattern for any harness that
    provisions infra in a setup phase distinct from agent execution.
  - Add "surface auth/credential failures in the aggregation job rather than
    swallowing them" (Claim 5) as a correctness pattern, alongside the
    `pre_activation` dependency auto-wiring fix from
    `blog-ghaw-weekly-2026-07-06.md` Claim 1 — both are `conclusion`/
    `pre_activation` job-graph correctness fixes shipped in consecutive weeks.

- **Chapter 03 (Agent Orchestration)** / **Chapter 04 (Safety and Constraints)**:
  - Flag `private-to-public-flows: allow` and "sink-visibility enforcement"
    (Claim 8) as a new gh-aw data-flow safety primitive worth a dedicated
    follow-up source note once reference documentation for the field is
    published — this weekly-update mention alone under-specifies the
    mechanism for confident guide inclusion.
  - Add `disclosure-header` (Claim 3) as a concrete built-in mechanism for
    AI-authorship transparency in agent-generated PR comments/issues.

- **Chapter 06 (Agentic Operations)**:
  - Update the `aw-failure-investigator` cost/behavior profile with the
    July 13 figures (250+ AIC/run, claude-opus-4-8, ~15 min/run) alongside the
    June 15 figures (~1.57M tokens/run, 16.6 min/run), flagging the unit
    change rather than attempting a false-precision conversion (Claim 11).
  - Add "a scheduled monitoring agent can itself fail and self-heal on its
    next scheduled run" (Claim 11) as a named operational pattern, and
    "monitoring/reporting agent + labeling convention" (Claim 13) as a second
    data point alongside `blog-ghaw-weekly-2026-07-06.md` Claim 8, this time
    for notification routing rather than chart segmentation.

## Extraction Notes

1. **WebFetch produced a condensed, imprecise summary; raw HTML was used for
   all quotes and figures in this note.** An initial WebFetch pass against the
   source URL returned a six-paragraph AI-generated summary that flattened
   several distinct claims and, notably, misattributed the "13 GitHub API
   calls" figure from "one particularly busy shift" (the source's own
   qualifier) to "recent runs... during peak operation periods" in general —
   see Claim 12, which exists specifically to flag this discrepancy for the
   Assayer. All quotes, PR numbers, and figures in this note were verified
   against the page's raw HTML (fetched via `curl`), consistent with the
   practice recommended in `blog-ghaw-weekly-2026-07-06.md` Extraction Note 1
   for this same blog's Astro/Starlight-rendered pages.

2. **PR numbers are visible inline text in this post**, unlike
   `blog-ghaw-weekly-2026-07-06.md`, where PR numbers were link-only
   (`href` targets not shown as visible text). This week's post prints PR
   numbers directly in the prose (e.g., "gVisor container runtime (#44796)"),
   confirmed by inspecting the raw HTML's visible text content, not just link
   targets. Presentation of PR citations is evidently inconsistent week to
   week in this blog.

3. **"Sink-visibility enforcement" is not defined by this source.** Claim 8's
   assessment of what this term likely means (a control on private-to-public
   data flow) is our inference, explicitly flagged as such, not a claim
   sourced from the post. The post uses the term as if the reader already
   knows what it refers to, without a definition or link to a definition. This
   is a case where the source itself provides an under-specified account of
   a safety-relevant mechanism — the guide should not treat Claim 8's
   assessment as confirmed until a reference-documentation source is mined.

4. **`aw-failure-investigator`'s "three runs, 3 issues (2+1)" framing leaves
   the failed run's place in the count ambiguous.** Claim 11's confidence is
   downgraded to anecdotal partly because it is not clear whether the July
   11th self-failure is one of the "three runs" whose issue counts are given
   (in which case only 2 runs succeeded and filed issues, and the "three
   runs" total includes the failed one), or whether "ran three times... filing
   3 issues" describes only the successful subset and the failed run is a
   fourth, separately-mentioned event. We preserved this as flagged ambiguity
   rather than resolving it, consistent with the verbatim-quote-first
   instruction in MINER.md §2a.

5. **No sub-pages followed.** This is a single blog post page. It links to
   ten PRs on GitHub, the v0.82.8 release tag, and the `aw-failure-investigator`
   workflow definition file. Per MINER.md §1, up to 5 substantive linked pages
   may be followed; these are primary-source artifacts referenced by, rather
   than sub-pages of, the blog post itself, and (consistent with the practice
   in `blog-ghaw-weekly-2026-07-06.md` Extraction Note 5) were not
   independently fetched in full for this note — their URLs are recorded in
   Concrete Artifacts for follow-up mining if deeper PR-level or field-level
   verification is needed (especially for `private-to-public-flows`, per Note 3
   above).

6. **No contradictions filed.** Reviewed all cross-referenced source notes
   (`docs-ghaw-sandbox-reference.md`, `docs-ghaw-mcp-gateway-reference.md`,
   `blog-ghaw-weekly-2026-06-15.md`, `blog-ghaw-weekly-2026-06-22.md`,
   `blog-ghaw-weekly-2026-06-29.md`, `blog-ghaw-weekly-2026-07-06.md`,
   `blog-ghaw-ai-credits-migration.md`). No claim in this source materially
   opposes an existing source note's claim at the MINER.md §4a filing
   threshold — the differences noted (unit changes, schema growth, term
   coverage gaps) are extensions/updates, not disagreements, so no
   contradiction issue was filed.
