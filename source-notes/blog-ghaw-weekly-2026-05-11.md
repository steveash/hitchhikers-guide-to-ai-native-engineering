---
source_url: https://github.github.com/gh-aw/blog/2026-05-11-weekly-update/
source_type: blog-post
title: "Weekly Update – May 11, 2026 (GitHub Agentic Workflows)"
author: GitHub Agentic Workflows team (gh-aw)
date_published: 2026-05-11
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#654"
---

# Weekly Update – May 11, 2026 (GitHub Agentic Workflows)

> Four releases (v0.71.5–v0.72.1) shipped May 5–7, 2026 deliver four
> high-signal patterns: (1) `gh aw lint` as a validation gate that runs
> actionlint directly against `.lock.yml` files without recompilation; (2)
> inline sub-agents going default-on with a simultaneous default model change
> to `small` alias — both a breaking activation change and a cost-reduction
> change; (3) `gh aw forecast` as the first CLI command for projecting
> effective token usage before running a workflow; and (4) Claude's sandbox
> gaining default `/tmp` read/write access with associated sandbox isolation
> implications.

## Source Context

- **Type**: blog-post (weekly changelog/release update from the official GitHub
  Agentic Workflows blog; covers versions v0.71.5–v0.72.1 across May 5–7, 2026,
  plus notable merged PRs; includes an "Agent of the Week" spotlight on
  `auto-triage-issues`)
- **Author credibility**: The gh-aw blog is the official publication of GitHub's
  Agentic Workflows platform team (Don Syme, Peli de Halleux, Mara Kiefer). Releases
  report on shipped PRs with specific numbers, independently verifiable. The Agent
  of the Week metrics are instrumentation data from a live repository, not marketing.
  High credibility for first-party platform claims.
- **Scope**: Four releases across three days (May 5–7, 2026). Covers new commands
  (`gh aw lint`, `gh aw forecast`), breaking changes (inline sub-agents default-on,
  field renamings), Claude sandbox extension, OTel instrumentation additions, and a
  first-party coding-agent skill. Does NOT cover: migration effort required for the
  field renamings (`rate-limit` → `user-rate-limit`, `max-runs` →
  `max-runs-per-window`); the full list of sub-agent model choices available under
  the `small` alias; or the exact token-projection mechanism behind `gh aw forecast`.

## Extracted Claims

### Claim 1: `gh aw lint` runs actionlint directly against `.lock.yml` files without recompilation, and supports `--shellcheck`, `--pyflakes`, and `--dir` flags for deeper script analysis

- **Evidence**: v0.72.1 release. The command is described with specific flags.
  PR #30695 is associated with `&&` escaping fix in the same release, confirming
  the v0.72.1 release window.
- **Confidence**: emerging (feature shipped and named; how to integrate `gh aw lint`
  as a CI gate — whether it exits non-zero on errors, how it compares to
  `gh aw compile --validate` — is not specified in the changelog)
- **Quote**: "runs actionlint directly against your existing `.lock.yml` files — no recompile required"
- **Our assessment**: `gh aw lint` closes a practical gap: previously, detecting
  actionlint issues required recompilation of the entire workflow spec. This command
  lets practitioners run lint as a CI gate on the compiled output directly — faster
  feedback than a full recompile cycle. The `--shellcheck` and `--pyflakes` flags
  extend analysis to embedded shell and Python scripts within the compiled workflow.
  For Ch02 (Harness Engineering): add `gh aw lint` as a recommended pre-merge CI
  gate for `.lock.yml` files, analogous to linting compiled artifacts in other CI
  pipelines. The `--shellcheck` flag is especially relevant for harnesses with
  inline shell scripts in `run:` blocks.

### Claim 2: Inline sub-agents are now default-on in v0.72.0; the `features.inline-agents: true` flag is deprecated and can be auto-removed via the `features-inline-agents-removal` codemod

- **Evidence**: v0.72.0 release. The post describes inline sub-agents as
  "default-on" with the `features.inline-agents: true` flag now deprecated.
  Auto-removal via `gh aw fix --write` with `features-inline-agents-removal`
  codemod is documented.
- **Confidence**: settled (shipped breaking change with named codemod for migration;
  described as "default-on" in the post)
- **Quote**: "default-on"
- **Our assessment**: This is an activation-model change: inline sub-agents
  previously required explicit opt-in via `features.inline-agents: true`; they now
  run by default for all workflows that define inline sub-agent blocks. The practical
  implication: any workflow that already defines inline sub-agent blocks will activate
  them without the flag. Workflows that previously had `features.inline-agents: true`
  should run `gh aw fix --write` to remove the deprecated flag. For Ch02 (Harness
  Engineering): update inline sub-agent documentation to remove the opt-in requirement.
  For practitioners: run `gh aw fix --write` with codemod `features-inline-agents-removal`
  on all workflow repos after upgrading to v0.72.0.

### Claim 3: Inline sub-agent blocks were switched to use the `small` model alias as default in v0.71.6, changing the prior documented default of inheriting the parent workflow's model

- **Evidence**: v0.71.5/v0.71.6 release. Framed as a cost-reduction change:
  inline sub-agent blocks were "switched … to use the `small` model alias" for
  cost reduction.
- **Confidence**: settled (named release, named change direction, named rationale;
  contrasts with the prior behavior documented in `docs-ghaw-inline-sub-agents.md`
  Claim 4)
- **Quote**: (no direct quote; release notes describe switching inline sub-agent
  blocks to use the `small` model alias)
- **Our assessment**: This change has a significant cost and quality implication.
  Inline sub-agents that previously inherited the parent model (e.g., Claude
  Opus 4.7) now run on `small` by default. For teams that relied on
  parent-model inheritance, this is a stealth cost reduction that may also reduce
  quality on inference-heavy sub-tasks. The tradeoff: most inline sub-tasks are
  bounded/focused, so `small` is often appropriate; but teams using sub-agents for
  complex reasoning should explicitly set `model: <preferred>` in sub-agent
  frontmatter. **See contradiction issue #714**: this claim materially opposes
  `docs-ghaw-inline-sub-agents.md` Claim 4 (which documented parent-model
  inheritance as the default before v0.71.6). Until resolved, the guide should not
  prescribe either behavior as settled — recommend practitioners explicitly set
  `model:` to avoid ambiguity.

### Claim 4: `gh aw forecast` is a new experimental command for projecting workflow effective token usage before running the workflow

- **Evidence**: PR #31377. Described as experimental. Enables "projecting token
  usage" for workflows.
- **Confidence**: emerging (experimental command; projection mechanism and accuracy
  against actual runs are not documented in the changelog)
- **Quote**: (no direct quote; post describes `gh aw forecast` as an experimental
  command for projecting workflow effective token usage)
- **Our assessment**: `gh aw forecast` is the first CLI command in the gh-aw corpus
  that enables pre-run cost projection. Prior effective-token (ET) work has focused
  on post-run measurement (`gh aw logs --json` with `effective_tokens` field, per
  `docs-ghaw-effective-tokens-specification.md`). A forecast command enables
  budget-before-you-run workflows — valuable for teams running expensive multi-step
  workflows on large codebases where a single run's cost is non-trivial. For Ch04
  (Operations): `gh aw forecast` should be incorporated into CI pre-flight checks
  for cost-sensitive workflows. The experimental label warrants caution about
  accuracy; validate against actual runs before relying on it for hard budget decisions.

### Claim 5: Claude engine in sandboxed gh-aw workflows now has default `/tmp` read/write access without requiring explicit sandbox configuration

- **Evidence**: PR #31357. The post describes this as a capability addition in the
  "notable merged PRs" section.
- **Confidence**: emerging (change documented; the sandbox security implications —
  whether `/tmp` is isolated per run, and whether contents persist across runs —
  are not specified in the changelog)
- **Quote**: (no direct quote; post grants Claude engine default `/tmp` read/write
  access in sandboxed workflows)
- **Our assessment**: `/tmp` access in a sandboxed agent is a meaningful expansion
  of surface area. Before this change, Claude in gh-aw sandboxes lacked default
  `/tmp` access, causing failures for tools or scripts that write to `/tmp` as
  scratch space (a very common pattern for coding agents). Granting default access
  removes a class of tool-invocation failures. The sandbox implication: if `/tmp`
  is shared across concurrent agent runs in the same sandbox environment, default
  read access could allow one run to read another run's intermediate files. For
  Ch03 (Safety and Verification): document that Claude engine now has `/tmp` access
  by default; verify that the sandbox design isolates `/tmp` per run. If `/tmp` is
  shared, sensitive intermediate files written by one agent are readable by another.
  For Ch02 (Harness Engineering): workflows that previously required explicit sandbox
  configuration for `/tmp` no longer need it after this change.

### Claim 6: `rate-limit` and `max-runs` configuration field names are renamed to `user-rate-limit` and `max-runs-per-window` as breaking changes in v0.72.0

- **Evidence**: PR #31390. Explicit renamings: `rate-limit` → `user-rate-limit`;
  `max-runs` → `max-runs-per-window`.
- **Confidence**: settled (specific PR, named field mappings)
- **Quote**: (no direct quote; post describes the field renamings as breaking
  configuration changes)
- **Our assessment**: The new names are semantically more precise. `user-rate-limit`
  clarifies this is a per-user constraint (not a global system rate limit), and
  `max-runs-per-window` clarifies the temporal scope of the constraint. These renames
  follow the gh-aw pattern of progressive semantic clarification as the platform
  matures (cf. `bypassPermissions` → `acceptEdits` in the April 27 release,
  `blog-ghaw-weekly-2026-04-27.md` Claim 2). For Ch02 (Harness Engineering): update
  any workflow configurations using `rate-limit` or `max-runs` to the new field
  names. Workflows using the old names will break on v0.72.0+.

### Claim 7: Shared workflows now inherit `engine.mcp.tool-timeout` settings from the caller, resolving a silent timeout mismatch for MCP tool calls in composed workflows

- **Evidence**: PR #30634, v0.72.1.
- **Confidence**: emerging (feature shipped; the exact inheritance mechanism —
  whether caller settings override or augment shared workflow defaults — is not
  specified in the changelog)
- **Quote**: (no direct quote; post describes `engine.mcp.tool-timeout`
  inheritance for shared workflows)
- **Our assessment**: Before this fix, a shared workflow called from a parent
  workflow would use its own `engine.mcp.tool-timeout` setting regardless of the
  caller's configuration. This created a class of silent timeout failures: a caller
  that increased its timeout for a slow MCP tool would not propagate that setting
  to shared workflows it called, which would hit their shorter default timeouts.
  For Ch02 (Harness Engineering): timeout inheritance for shared workflows is now
  working; teams who added timeout workarounds for this gap should validate whether
  they can simplify configurations.

### Claim 8: A first-party coding-agent skill for Copilot, Claude, and other coding agents shipped as PR #27259 in v0.72.1

- **Evidence**: PR #27259, v0.72.1. Described as "first-party coding-agent skill."
- **Confidence**: emerging (PR shipped; the specific capabilities of the skill —
  what tools it exposes, how it differs from engine-default coding behavior — are
  not described in the changelog)
- **Quote**: (no direct quote; post describes a first-party coding-agent skill for
  Copilot, Claude, and other coding agents)
- **Our assessment**: A first-party coding-agent skill from the gh-aw team represents
  an opinionated packaging of coding capabilities for use across multiple coding
  agents. Prior gh-aw tooling has focused on workflow composition and orchestration;
  a coding-agent skill extends this to include core coding behaviors as a configurable
  component. For Ch02: the first-party coding-agent skill may become a recommended
  base configuration for coding-focused workflows; its capabilities should be evaluated
  against team-specific requirements once the full feature surface is documented.

### Claim 9: A HTML-escaping bug was converting `&&` to `&&` in compiled expressions, breaking shell conditional logic in `.lock.yml` files

- **Evidence**: PR #30695, v0.72.1. Specifically describes `&&` being converted to
  `&&` in compiled expressions.
- **Confidence**: settled (specific PR, specific symptom: `&&` → `&&`,
  clear fix)
- **Quote**: (no direct quote; post describes `&&` being converted to
  `&&` in expressions)
- **Our assessment**: HTML-entity escaping of `&&` would break any compiled workflow
  expression that uses `&&` as a logical AND operator — a common pattern in shell
  conditions. This is a correctness bug that would silently produce invalid compiled
  output: the `.lock.yml` file would contain `&&` literals where `&&` was
  expected, and any shell script or expression relying on `&&` short-circuit evaluation
  would fail. For Ch02: workflows that used `&&` in compiled expressions before v0.72.1
  should recompile to pick up the fix.

### Claim 10: OpenTelemetry `gen_ai.response.finish_reasons` attribute is now emitted, making model termination reasons queryable in OTel backends

- **Evidence**: PR #31332. New OTel attribute: `gen_ai.response.finish_reasons`.
- **Confidence**: emerging (attribute added; semantic alignment with OpenTelemetry
  GenAI semantic conventions is implied but not confirmed in the changelog)
- **Quote**: (no direct quote; post describes `gen_ai.response.finish_reasons`
  attribute emission in OTel spans)
- **Our assessment**: `gen_ai.response.finish_reasons` carries why the model stopped
  generating — values like `stop`, `max_tokens`, `tool_calls`, etc. Emitting this
  as a queryable OTel attribute enables dashboards that distinguish between normal
  completions, token-limit hits, and tool-call terminations without requiring parsing
  of log lines. For Ch04 (Operations): add `gen_ai.response.finish_reasons` as a
  recommended dashboard attribute. A spike in `max_tokens` finish reasons is an
  early indicator of token exhaustion before runs start failing visibly. This
  extends the OTel observability story begun in the April 6 release
  (`blog-ghaw-weekly-2026-04-06.md` Claim 1) into model response metadata.

### Claim 11: Synthetic OTel exception events are now emitted for silent workflow failures, filling a visibility gap where failures left no trace

- **Evidence**: PR #31334. Described as "Synthetic OTel exception events for silent
  failures."
- **Confidence**: emerging (feature shipped; what constitutes a "silent failure" and
  whether all failure modes are covered by synthetic events is not specified)
- **Quote**: (no direct quote; post describes synthetic OTel exception events for
  silent workflow failures)
- **Our assessment**: Silent failures in agentic workflows — where the workflow exits
  without raising an exception but also without completing its task — have been a
  persistent observability gap. Without a trace event, these failures are invisible
  in OTel dashboards; they appear as normal-duration runs with no error signal.
  Synthetic exception events manufacture the missing signal by emitting a trace event
  that marks the run as an exception even when the underlying failure mode did not
  produce one naturally. For Ch04: configure alerts on synthetic exception event
  counts alongside standard error spans. This pairs with the April 13 OTel exception
  span improvements (`blog-ghaw-weekly-2026-04-13.md` Claim 6 — `exception.type`
  attribute) to complete the exception observability surface: April 13 made raised
  exceptions queryable; May 11 surfaces silent failures that don't raise exceptions.

### Claim 12: `auto-triage-issues` ran at nine API requests and ~270K input tokens from cache per issue, completing in under 40 seconds — the first Agent of the Week report to explicitly measure cache utilization

- **Evidence**: "Agent of the Week" spotlight for May 11. Metrics: "nine API
  requests, ~270 K input tokens from cache, under 40 seconds per issue turnaround."
- **Confidence**: anecdotal (snapshot data from the Agent of the Week section;
  sample size and time window not specified)
- **Quote**: "nine API requests, ~270 K input tokens from cache, under 40 seconds per issue turnaround"
- **Our assessment**: This is the fifth appearance of `auto-triage-issues` in the
  gh-aw weekly series. The longitudinal record: March 30 (18 turns, 817K tokens,
  FAILED — `blog-ghaw-weekly-2026-03-30.md` Claim 7); April 13 (100% coverage, 4
  labels in single pass — `blog-ghaw-weekly-2026-04-13.md` Claim 10); April 27
  (4–6 turns, 6 API calls per run — `blog-ghaw-weekly-2026-04-27.md` Claim 8);
  May 11 (nine API requests, ~270K cached input tokens, under 40 seconds). The new
  dimension this week is cache utilization: reporting "~270 K input tokens from
  cache" signals that the workflow prompt cache is warm and being hit — inputs
  are being reused across invocations rather than computed fresh. This is the first
  week this metric is reported explicitly. For Ch04 (Operations): cache engineering
  (stable system prompts, predictable invocation patterns) should be a design
  principle for high-frequency triage agents. The under-40-second per-issue
  turnaround is consistent with April 27's trajectory; the cache fraction provides
  the mechanism explanation for how that speed is achieved.

## Concrete Artifacts

### Version Summary: v0.71.5–v0.72.1 (May 5–7, 2026)

```
v0.72.1 (May 7) — Linting + Bugfixes:
  - New: gh aw lint — actionlint against .lock.yml, no recompile required
         (--shellcheck, --pyflakes, --dir flags for deeper analysis)
  - New: Shared workflow engine.mcp.tool-timeout inheritance (#30634)
  - New: First-party coding-agent skill for Copilot, Claude, other agents (#27259)
  - Fix: && expression HTML-escaping bug (→ &&) corrected (#30695)

v0.72.0 (May 6) — Inline Sub-Agents Default-On (Breaking):
  - Breaking: inline sub-agents now default-on; features.inline-agents: true deprecated
  - Migration: gh aw fix --write (codemod: features-inline-agents-removal)
  - Fix: push_to_pull_request_branch rerun failures with add/add git conflicts

v0.71.6 / v0.71.5 (May 5–6) — Stability + Cost:
  - Fix: Claude engine stability (mid-session crashes)
  - Fix: Multi-line engine.env block-scalar YAML compilation issues
  - Change: Inline sub-agent blocks now default to small model alias (cost reduction)

Notable Merged PRs (outside release sets):
  - gh aw forecast (experimental): projects effective token usage before run (#31377)
  - Claude /tmp read/write access in sandboxed workflows (#31357)
  - Field renamings: rate-limit → user-rate-limit; max-runs → max-runs-per-window (#31390)
  - OTel: gen_ai.response.finish_reasons attribute added (#31332)
  - OTel: synthetic exception events for silent failures (#31334)
```

### Migration: Inline Sub-Agents to v0.72.0

```bash
# Auto-remove deprecated features.inline-agents: true flag
gh aw fix --write
# Codemod applied: features-inline-agents-removal

# After migration: inline sub-agents active by default in all workflows
# that define them. No opt-in flag required.
#
# IMPORTANT: sub-agent model default has changed to 'small' as of v0.71.6.
# If you need a specific model, set it explicitly in sub-agent frontmatter:
#   model: claude-sonnet-4-6  # or your preferred model
# See contradiction issue #714 for resolution status.
```

### `gh aw lint` Usage Pattern

```bash
# Run actionlint against compiled lock files (no recompile needed)
gh aw lint

# With deeper script analysis
gh aw lint --shellcheck    # check embedded shell scripts
gh aw lint --pyflakes      # check embedded Python scripts
gh aw lint --dir path/to/  # target specific directory

# Recommended use: add as pre-merge CI gate alongside gh aw compile --validate
```

### Agent of the Week: `auto-triage-issues` — May 11, 2026 Data

```
Agent:          auto-triage-issues
Period:         Week of May 11, 2026

Per-issue metrics:
  API requests:              nine
  Input tokens from cache:   ~270 K
  Turnaround:                under 40 seconds per issue

New dimension vs. prior reports: cache utilization explicitly measured

Longitudinal record:
  2026-03-30: 18 turns, 817K tokens, FAILED (blog-ghaw-weekly-2026-03-30)
  2026-04-13: 100% label coverage, 4 labels in single pass (blog-ghaw-weekly-2026-04-13)
  2026-04-27: 4–6 turns, 6 API calls/run (blog-ghaw-weekly-2026-04-27)
  2026-05-11: nine API requests, ~270K cached tokens, <40s/issue (this note)
```

## Cross-References

- **Corroborates**:
  - `blog-ghaw-weekly-2026-04-27.md` Claim 8 (`auto-triage-issues` at 4–6 turns,
    6 API calls per run): The May 11 Agent of the Week data (Claim 12 here)
    continues the same positive trajectory with a new dimension — cache utilization.
    April 27 reported turns and API calls; May 11 adds cache-hit fraction. Together
    they provide a more complete picture of how efficiency gains are achieved.
  - `blog-ghaw-weekly-2026-04-13.md` Claim 6 (OTel exception span events with
    `exception.type` and `exception.message`): The synthetic OTel exception events
    for silent failures (Claim 11 here) extend the same exception observability
    surface. April 13 added queryable exception types for raised exceptions; May 11
    adds synthetic events for failures that don't raise exceptions naturally.
    Together they close the full exception observability surface.
  - `blog-ghaw-weekly-2026-04-27.md` Claim 3 (OTel spans for manually cancelled
    runs): The OTel additions (Claims 10–11 here) continue the progressive
    completion of the gh-aw distributed tracing story: April 6 (OTLP framework),
    April 13 (cross-job parent spans), April 27 (cancellation spans), May 11
    (`gen_ai.response.finish_reasons` + synthetic exception events for silent
    failures).

- **Contradicts**:
  - `docs-ghaw-inline-sub-agents.md` Claim 4 (inline sub-agents default to parent
    workflow's model when no `model` field is specified — Quote from that note: "AI
    model to use (e.g. `claude-haiku-4.5`). Defaults to parent workflow's model."):
    The v0.71.6 release changes the default to the `small` model alias (Claim 3
    here). These two sources give conflicting guide advice: the docs note implies
    no explicit `model` setting is needed to inherit the parent's model; the May 11
    release shows the default has changed to `small`. **→ Contradiction issue #714
    filed before this PR.**

- **Extends**:
  - `docs-ghaw-effective-tokens-specification.md` Claim 1 (ET metric for computing
    normalized token cost across invocations): `gh aw forecast` (Claim 4 here) is
    the first CLI command that operationalizes the ET specification for pre-run cost
    projection. The ET spec defines what to measure; `gh aw forecast` enables
    projecting that measure before a run executes.
  - `docs-ghaw-inline-sub-agents.md` Claim 1 (inline sub-agent definition and
    syntax) and Claim 4 (model field defaults): Claims 2–3 here (default-on
    activation change and `small` model default) update the inline sub-agents
    reference by documenting the v0.72.0 activation change and v0.71.6 default
    model change. The docs note represents pre-v0.71.5 state; this note captures
    the post-v0.72.0 production state.
  - `blog-ghaw-weekly-2026-04-06.md` Claim 1 (OTLP distributed tracing via
    `observability.otlp` frontmatter): Claims 10–11 here extend the OTel
    instrumentation surface to include model response metadata
    (`gen_ai.response.finish_reasons`) and synthetic exception events for silent
    failures. The April 6 release delivered the framework; May 11 adds two further
    signal types.
  - `blog-ghaw-weekly-2026-03-30.md` Claim 6 (`agentic_fraction` metric identifying
    deterministic-conversion candidates): The May 11 Agent of the Week data (Claim 12)
    implicitly demonstrates the inverse of the `agentic_fraction` problem — a highly
    optimized agent hitting cache on ~270K tokens, completing in under 40 seconds,
    is one that has already reduced unnecessary agentic turns and engineered for
    cacheability.

- **Novel**:
  - **`gh aw lint` as a static analysis gate on compiled artifacts** (Claim 1):
    First corpus source to document a dedicated lint command for `.lock.yml` files
    that works without recompilation. Prior sources document `gh aw compile --validate`
    for spec validation; `gh aw lint` is a distinct tool operating on compiled output.
  - **`gh aw forecast` for pre-run token projection** (Claim 4): First corpus source
    to document a pre-run cost forecasting command. All prior effective-token work is
    post-run measurement.
  - **Claude `/tmp` access in sandboxed workflows** (Claim 5): First corpus source
    to document that Claude engine has default `/tmp` access in gh-aw sandboxes and
    the associated sandbox isolation consideration.
  - **Inline sub-agents going fully default-on** (Claim 2): The first documented
    de-flagging of an experimental opt-in feature in the gh-aw corpus.
  - **Cache utilization as a triage-agent performance dimension** (Claim 12): The
    May 11 Agent of the Week report is the first in the longitudinal
    `auto-triage-issues` record to explicitly report cache performance ("from cache"
    input tokens), adding a new benchmark dimension.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add `gh aw lint` as a recommended CI validation gate for `.lock.yml` files,
    with `--shellcheck` and `--pyflakes` flags for harnesses with embedded scripts
    (Claim 1). Pair with `gh aw compile --validate` (spec validation) to cover
    both pre-compilation and post-compilation correctness.
  - Update inline sub-agents guidance to reflect default-on activation (Claim 2):
    remove the `features.inline-agents: true` opt-in requirement. Add migration step:
    `gh aw fix --write` with `features-inline-agents-removal` codemod.
  - Add a note about the inline sub-agent `small` model default change (Claim 3):
    until contradiction issue #714 is resolved, recommend practitioners explicitly
    set `model:` in sub-agent frontmatter rather than relying on the default.
  - Update `rate-limit` / `max-runs` field names to `user-rate-limit` /
    `max-runs-per-window` in all harness configuration examples (Claim 6).
  - Note `engine.mcp.tool-timeout` inheritance fix for shared workflows (Claim 7):
    teams who added timeout workarounds for shared workflows may be able to simplify.
  - Add `&&` expression escaping bug fix (Claim 9) as a reminder to recompile
    workflows using `&&` in compiled expressions after upgrading to v0.72.1.

- **Chapter 03 (Safety and Verification)**:
  - Document Claude sandbox `/tmp` access (Claim 5): workflows running Claude engine
    in sandboxed mode should verify that `/tmp` is isolated per run. If the sandbox
    shares `/tmp` across concurrent runs, sensitive intermediate files are visible
    across runs. Recommend explicit verification of `/tmp` isolation scope before
    relying on it for scratch storage in security-sensitive workflows.

- **Chapter 04 (Operations)**:
  - Introduce `gh aw forecast` (Claim 4) as a pre-run cost management tool. Note
    experimental status; recommend validation against actual runs before using for
    hard budget decisions.
  - Add `gen_ai.response.finish_reasons` (Claim 10) as a recommended dashboard
    attribute. Alert on `max_tokens` finish reason spikes as an early warning for
    token exhaustion. Add synthetic exception events (Claim 11) as a mechanism for
    alerting on silent failures.
  - Update `auto-triage-issues` longitudinal record (Claim 12) with May 11 cache
    utilization dimension. Recommend prompt cache engineering (stable system prompts,
    predictable invocation cadences) as a design principle for high-frequency
    triage agents targeting sub-40-second turnarounds.

## Extraction Notes

1. **Source depth**: The weekly update is a changelog post covering four releases
   and additional merged PRs, with an Agent of the Week spotlight. Twelve claims
   were extracted across releases, bug fixes, and observability improvements.
2. **WebFetch extraction**: Source content was obtained via two WebFetch calls. The
   first gave structured extraction; the second asked for near-verbatim text. The
   `gh aw lint` description ("runs actionlint directly against your existing
   `.lock.yml` files — no recompile required") appears in double quotes in the
   second WebFetch output and is treated as verbatim from the source. The
   `auto-triage-issues` metrics ("nine API requests, ~270 K input tokens from
   cache, under 40 seconds per issue turnaround") also appear in the structured
   extraction and are treated as near-verbatim. Other descriptions are WebFetch
   model summaries; claims with "(no direct quote)" reflect descriptions that could
   not be verified character-for-character.
3. **Contradiction filed**: The inline sub-agent model default change (Claim 3)
   materially contradicts `docs-ghaw-inline-sub-agents.md` Claim 4 (documented
   parent-model inheritance default). Contradiction issue #714 was filed before
   this PR per MINER.md §4a. The contradiction is flagged in the source note
   without picking a verdict.
4. **Inline sub-agents breaking change**: v0.72.0 is the first version to make
   inline sub-agents default-on. Teams on v0.71.x and earlier who have
   `features.inline-agents: true` flags should upgrade carefully and run the
   codemod after verifying the `small` model default behavior is acceptable.
5. **`gh aw forecast` experimental status**: The forecast command is explicitly
   labeled experimental in the source. Extraction confidence is marked emerging;
   practitioners should validate against actual runs before production use.
6. **No prior May 2026 weekly note**: Issue #530 (May 4 update) was marked
   miner-blocked. This May 11 note is a distinct article and is the first May 2026
   weekly in the corpus.
