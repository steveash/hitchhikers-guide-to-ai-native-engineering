---
source_url: https://github.github.com/gh-aw/gallery/dependency-analysis
source_type: docs
title: "GitHub Agentic Workflows Gallery: Automated Dependency Analysis (Go Fan)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-09-22
last_checked: 2026-09-22
status: current
confidence_overall: emerging
issue: "#3614"
---

# GitHub Agentic Workflows Gallery: Automated Dependency Analysis (Go Fan)

> A short gallery page presenting "Go Fan" — a weekday-scheduled, cache-memory-
> backed workflow that round-robins through a Go repository's direct dependencies,
> researches each one's upstream best practices, and opens a single GitHub Issue
> with improvement recommendations — as the platform's worked example for
> dependency analysis. Like the sibling "Code Improvement" gallery page, this page
> is thin (four short sections, no reproduced YAML), but its "Go Fan workflow
> source" link points to the full, non-portable production workflow
> (`github/gh-aw/.github/workflows/go-fan.md`), which carries substantially more
> concrete configuration, prompt engineering, and tool-scoping detail than the
> gallery page shows. Notably, the primary source directly contradicts an existing
> corpus note's characterization of Go Fan's output type (see Cross-References).

## Source Context

- **Type**: docs (official GitHub Agentic Workflows "Gallery" section — the same
  worked-example tier as `docs-ghaw-gallery-code-improvement.md`, one level more
  concrete than the `examples/` pages). The page links out to the full production
  workflow it profiles, hosted in the same `github/gh-aw` repository (not a
  separate `githubnext/agentics` repo, unlike the Code Improvement gallery page).
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team and doc set behind every other `docs-ghaw-*` note in this corpus. The
  gallery prose and the linked `go-fan.md` / `go-fan.lock.yml` source files are
  both authoritative, shipped platform artifacts (Go Fan runs in gh-aw's own
  repository), not third-party commentary.
- **Scope**: Covers exactly one worked example — a Claude-engine, weekday-scheduled
  agent that reviews one direct Go module per run against upstream best practices.
  Does NOT cover: the general ResearchPlanAssignOps pattern in depth (see
  `docs-ghaw-research-plan-assign-ops.md`), the Safe Outputs specification (see
  `docs-ghaw-safe-outputs-specification.md`), cache-memory semantics in depth (see
  `docs-ghaw-cache-memory-reference.md`), or Serena MCP configuration in depth (see
  `docs-ghaw-guides-serena.md`). The gallery page's own prose has no YAML block at
  all — all configuration in this note comes from the linked source workflow (see
  Extraction Notes).

## Extracted Claims

### Claim 1: Go Fan is a weekday-scheduled workflow that reviews exactly one Go module per run and creates a single GitHub Issue with its findings — not a Discussion
- **Evidence**: Gallery page opening summary and "What the workflow reports" section; corroborated mechanically by the linked `go-fan.md` source, which imports `shared/daily-issue-base.md` (a bundle documented as being "for daily/scheduled code quality workflows that create GitHub issues") configured with `safe-outputs: create-issue: ... max: 1`.
- **Confidence**: settled (verbatim gallery prose plus a directly-fetched, verbatim workflow-source YAML block)
- **Quote**: "Go Fan is a weekday dependency-analysis workflow for Go repositories. On each run, it selects a direct dependency from `go.mod`, researches upstream changes and recommended usage, compares those findings with the repository's code, and creates a single issue containing actionable recommendations."
- **Our assessment**: This is a straightforward, single-purpose research-and-report agent — one dependency, one issue, one run. It directly contradicts `docs-ghaw-research-plan-assign-ops.md` Claim 11, which describes Go Fan as creating "categorized discussions with improvement suggestions." That existing claim was already graded anecdotal with no verbatim quote available; this note's evidence (the gallery page's own prose plus the actual shipped workflow's `create-issue` safe-output configuration) is settled and verbatim. Filed as contradiction issue #3620 rather than silently overriding the existing note — see Cross-References.

### Claim 2: Go Fan selects which module to review using a cache-memory-backed round-robin algorithm that prioritizes dependencies with the most recent upstream activity, and resets the "already reviewed" list once every direct dependency has been reviewed within the last 7 days
- **Evidence**: Gallery page "How Go Fan selects modules" section; elaborated in `go-fan.md` §2 ("Select Today's Module with Priority") with explicit sort and fallback rules.
- **Confidence**: settled (verbatim gallery quote, corroborated by matching prose in the linked workflow source)
- **Quote**: "Go Fan tracks previously reviewed modules with `cache-memory`. It prioritizes recently updated GitHub-hosted dependencies, then cycles through the remaining direct dependencies. It avoids selecting a module reviewed in the last seven days unless every direct dependency is still within that review window, in which case it resets the list and starts from the top."
- **Our assessment**: This is a concrete, fully-specified deterministic selection algorithm layered on top of an LLM-driven research step — the *which module* decision is rule-based (sort by `pushed_at` descending, round-robin with a 7-day cooldown, deterministic fallback to module-path-ascending when GitHub metadata is unavailable per `go-fan.md` §2.3), while the *what to say about it* step is left to the model. This is a specific, reusable pattern for scoping a recurring research agent's target selection deterministically rather than letting the model choose what to review each day — worth documenting alongside `docs-ghaw-deterministic-agentic-patterns.md`'s existing coverage of deterministic gh-aw controls, but applied here to *task selection* rather than trigger filtering or deduplication.

### Claim 3: The gallery page explicitly recommends the ResearchPlanAssignOps pattern as the correct way to move from Go Fan's raw findings to planned, assigned work, rather than treating Go Fan's own issue as directly actionable
- **Evidence**: Closing sentence of "What the workflow reports," linking to `/gh-aw/patterns/research-plan-assign-ops/`.
- **Confidence**: settled (verbatim gallery-page prose)
- **Quote**: "Review the recommendations before implementing them. For a structured handoff from research to planning, assignment, and human review, use the ResearchPlanAssignOps pattern."
- **Our assessment**: This is a meaningful piece of context missing from `docs-ghaw-research-plan-assign-ops.md`'s own extraction: that source note treats Go Fan as *the* reference implementation of ResearchPlanAssignOps's Research phase (Claim 11), implying Go Fan is already wired into the four-phase pattern. This gallery page's own wording is weaker and more advisory — it says to *use* ResearchPlanAssignOps for the Discussion→Plan→Assign→Merge handoff, phrased as a recommendation for what a practitioner should layer on top of Go Fan, not as a description of what Go Fan itself already does. Combined with Claim 1 (Go Fan creates an Issue, not a Discussion — the object type ResearchPlanAssignOps's Plan phase's `/plan` command is designed to act on), this suggests Go Fan is presented by this page as a *precursor* or *inspiration* for the pattern rather than a literal instance of it in production — worth flagging for whoever resolves contradiction #3620, since it bears on how tightly coupled Go Fan actually is to the four-phase pattern.

### Claim 4: The workflow scopes its Bash tool access to a fixed allowlist of read-only commands rather than granting general shell access, and explicitly sets `edit: null` — the agent has no file-editing tool at all
- **Evidence**: `go-fan.md` frontmatter `tools:` block (see Concrete Artifacts).
- **Confidence**: settled (verbatim YAML frontmatter, directly fetched)
- **Quote**: (no direct prose quote from either page states this design rationale; the YAML itself is verbatim — see Concrete Artifacts)
- **Our assessment**: This is a concrete instance of least-privilege tool scoping for a research-only agent: the `bash:` allowlist is seven fixed commands (`cat go.mod`, `cat go.sum`, `go list -m all`, a `grep -r "import"` pattern, a `find pkg -name "*.go"` pattern, and two `scratchpad/mods/` inspection commands), not an open shell. Combined with `edit: null` (no edit tool configured at all — contrast with `docs-ghaw-gallery-code-improvement.md`'s Code Simplifier, which is an edit-and-PR workflow), the agent is architecturally incapable of modifying repository files; its only write surface is the `create-issue` safe-output and its own `scratchpad/mods/` and cache-memory state files. This is a stronger and more mechanical form of "propose, don't act" than a prompt-level instruction not to edit code — the tool is simply absent. Useful for Ch03 (Safety and Verification) as a worked example of enforcing an agent's read-only/advisory role at the tool-configuration level rather than the prompt level.

### Claim 5: The workflow's cache-memory usage follows the platform's formal `missing_data` / `cache_memory_miss` error vocabulary when the persisted state file is malformed, rather than the workflow author inventing its own error-handling convention
- **Evidence**: `go-fan.md` §1 ("Load Round-Robin State from Cache"): "If the file exists but is malformed, call `missing_data` with `data_type: "cache_memory"` and `reason: "cache_memory_miss"`."
- **Confidence**: settled (verbatim instruction text from the linked source file)
- **Quote**: "If the file **exists but is malformed**, call `missing_data` with `data_type: \"cache_memory\"` and `reason: \"cache_memory_miss\"`"
- **Our assessment**: This is a real, production usage example of the `missing_data`/`cache_memory_miss` formal error vocabulary already documented abstractly in `docs-ghaw-cache-memory-reference.md` Claim 11 (which states this triggers an automatic failure issue via the platform's failure handler). Prior to this note, that claim had no named example of a real workflow actually emitting this signal in its own prompt instructions; Go Fan is now a concrete corroborating instance.

### Claim 6: Go Fan uses the Serena MCP server for semantic code analysis of how the selected module is used in the repository, explicitly instructed not to rely on `grep`-level text search alone
- **Evidence**: `go-fan.md` §4 ("Analyze Project Usage with Serena") and the "Serena Configuration" section, which sets project root, language (Go), and a dedicated cache-memory subpath (`/tmp/gh-aw/cache-memory/serena/`) for Serena's own index.
- **Confidence**: settled (verbatim configuration and prose from the linked source file)
- **Quote**: "Use the Serena MCP server to perform deep code analysis" / "Use Serena for: Semantic code analysis, Finding all usages of a module, Understanding code patterns, Identifying refactoring opportunities"
- **Our assessment**: This corroborates `docs-ghaw-guides-serena.md`'s general coverage of Serena as gh-aw's packaged semantic-analysis MCP server, with a concrete example of the *combination* pattern that note's Scope section flags as a best practice topic: Go Fan pairs a narrow, allowlisted `bash` toolset (Claim 4) for cheap textual lookups (`grep -r "import"`) with Serena for the deeper "which APIs are used, is usage idiomatic, are there simpler APIs available" analysis — a division of labor between cheap deterministic tools and a semantic-analysis MCP server for the parts of the task that actually need it.

### Claim 7: Go Fan's daily issue-creation configuration is inherited from a shared, parameterized bundle (`shared/daily-issue-base.md`) rather than hand-rolled per workflow, standardizing `expires`, `labels`, `title-prefix`, and a hard `max: 1` cap across many gh-aw workflows
- **Evidence**: `go-fan.md` frontmatter's `imports: - uses: shared/daily-issue-base.md` block with `expires: 1d`, `labels: [automation, cookie]`, `title-prefix: "[go-fan] "`; the bundle definition itself (fetched directly) declares `safe-outputs: create-issue: ... max: 1` and documents its own purpose in a header comment.
- **Confidence**: settled (verbatim YAML from both `go-fan.md` and the imported `shared/daily-issue-base.md` bundle definition)
- **Quote**: "Bundle for daily/scheduled code quality workflows that create GitHub issues. Bundles: activation-app + reporting guidelines + standardized create-issue safe-outputs." (`shared/daily-issue-base.md` header comment)
- **Our assessment**: The `import-schema` + `uses`/`with` mechanism itself is *not* new to the corpus — `docs-ghaw-sharing-workflows.md` Claim 6 already documents it generically, with its own syntax example. What is new here is the first extraction of a real, shipped bundle's *own* `import-schema` parameter table: a concrete importable YAML fragment declaring typed parameters (`title-prefix` required, `expires` default `2d`, `labels` default `[automated-analysis, cookie]`, `assignees` default `[]`) that expands into a standardized `create-issue` safe-output plus bundled `activation-app` and `reporting` imports. Go Fan overrides the bundle's default `expires: 2d` down to `expires: 1d` and its default `labels: [automated-analysis, cookie]` to `[automation, cookie]`, while accepting the bundle's `max: 1` cap (not itself overridable via the documented `import-schema`). Two other corpus notes already show this same bundle consumed in production with different parameter values (`blog-ghaw-agent-of-the-day-2026-09-10.md` Claim 9, `blog-ghaw-agent-of-the-day-2026-05-25.md` Claim 5 — see Cross-References), so Go Fan is the third documented consumer, and this note supplies the bundle definition those two notes cite by name but never reproduce. For Ch02: document this bundle-with-typed-parameters pattern as the mechanism gh-aw uses to standardize safe-output configuration across a fleet of similar scheduled workflows, distinct from copy-pasting the same `safe-outputs:` block into each workflow file.

### Claim 8: The workflow's frontmatter schedule uses the natural-language "friendly format" (`daily around 7:00 on weekdays`) rather than raw cron, and the compiled lock file confirms this resolves to a scattered, non-zero-minute cron expression
- **Evidence**: `go-fan.md` frontmatter: `schedule: - cron: daily around 7:00 on weekdays`; the compiled `go-fan.lock.yml` shows `cron: "53 7 * * 1-5"  # Friendly format: daily around 7:00 on weekdays (scattered)`.
- **Confidence**: settled (verbatim frontmatter and lock-file comment, both directly fetched)
- **Quote**: (no prose quote; see Concrete Artifacts for both YAML fragments)
- **Our assessment**: This is additional corroborating evidence for open contradiction issue #3043 (`docs-ghaw-dailyops.md`'s claim that weekday-only schedules have "no short syntax available" and require raw cron, vs. `blog-ghaw-agent-of-the-day-2026-08-26.md`'s finding that a "friendly format" natural-language weekday syntax exists and is used in production). Go Fan is a second, independent production workflow using the exact same `daily around HH:MM on weekdays` friendly-format string (compiling to a scattered, non-round-number minute — `53`, not `00` — matching the scattering behavior already documented for the CLI Consistency Checker in that contradiction's Side B). This note does not re-file the contradiction (already open); it adds corroborating evidence to Side B for whoever resolves #3043.

### Claim 9: The workflow restricts network egress to three named ecosystem allowlists (`defaults`, `github`, `go`) rather than an unrestricted or single-ecosystem allowlist
- **Evidence**: `go-fan.md` frontmatter `network: allowed: [defaults, github, go]`.
- **Confidence**: settled (verbatim YAML frontmatter)
- **Quote**: (no prose quote; see Concrete Artifacts)
- **Our assessment**: This extends `docs-ghaw-network-reference.md`'s existing coverage of ecosystem-identifier allowlists (already corroborated by the Code Simplifier's `[defaults, dotnet, node, python, rust, java]` list in `docs-ghaw-gallery-code-improvement.md` Claim 6) with a second real-world example, here scoped tightly to just the two ecosystems the workflow actually needs: `github` (for repository metadata and README/release lookups on dependency repos) and `go` (for module registry access), plus the baseline `defaults`. The narrower list (3 entries vs. Code Simplifier's 6) tracks the narrower actual task — a Go-only dependency reviewer needs less egress surface than a multi-language code simplifier.

### Claim 10: Go Fan persists two functionally distinct kinds of state across runs — a small round-robin tracking JSON in `cache-memory` (which module was reviewed when) and full per-module Markdown summaries under `scratchpad/mods/` (what was found) — rather than conflating the two into one cache-memory blob
- **Evidence**: `go-fan.md` §1 (cache-memory `state.json` schema: `last_reviewed_module`, `reviewed_modules` list) vs. §6 ("Save Module Summary") specifying a separate `scratchpad/mods/<module-name>.md` file per module with a fixed section structure (Overview, Version Used, Usage in gh-aw, Research Summary, Improvement Opportunities, References).
- **Confidence**: settled (verbatim schema and file-structure specifications from the linked source file)
- **Quote**: (no single prose quote covers both halves of this distinction; see Concrete Artifacts for both schemas)
- **Our assessment**: This is a specific memory-architecture pattern worth naming: a *small, structured control-plane state* (round-robin bookkeeping, cheap to read/write every run) kept separate from a *larger, human-readable content archive* (one Markdown file per module, accumulating detailed findings over time, readable by both the agent on a future run — via the `find scratchpad/mods/ -maxdepth 1 -ls` / `cat scratchpad/mods/*` bash-allowlist entries — and by a human browsing the repo checkout). This two-tier design avoids bloating the cache-memory JSON with full research content while still giving the agent (and human reviewers) a durable, per-module research trail. No existing corpus note names this specific split between a compact cache-memory control file and a separate content-archive directory as a deliberate pattern.

## Concrete Artifacts

### Full frontmatter — `github/gh-aw/.github/workflows/go-fan.md`

Fetched directly via `raw.githubusercontent.com/github/gh-aw/main/.github/workflows/go-fan.md`; reproduced verbatim.

```yaml
---
on:
  schedule:
  - cron: daily around 7:00 on weekdays
  workflow_dispatch: null
permissions:
  contents: read
  discussions: read
  issues: read
  pull-requests: read

network:
  allowed:
  - defaults
  - github
  - go
imports:
- uses: shared/daily-issue-base.md
  with:
    expires: 1d
    labels:
    - automation
    - cookie
    title-prefix: "[go-fan] "
- shared/go-source-analysis.md
- shared/otlp.md
description: "Daily Go module usage reviewer - analyzes direct dependencies prioritizing recently updated ones"
emoji: 🐹
engine: claude
name: Go Fan
strict: true
timeout-minutes: 30
tools:
  bash:
  - cat go.mod
  - cat go.sum
  - go list -m all
  - grep -r "import" --include="*.go"
  - find pkg -name "*.go"
  - find scratchpad/mods/ -maxdepth 1 -ls
  - cat scratchpad/mods/*
  cache-memory: true
  cli-proxy: true
  edit: null
  github:
    mode: local
    toolsets:
    - default
tracker-id: go-fan-daily
---
```

*Source: `github/gh-aw/.github/workflows/go-fan.md`, linked from the gallery page as "Go Fan workflow source"*

### Compiled schedule — `github/gh-aw/.github/workflows/go-fan.lock.yml`

```yaml
schedule:
  - cron: "53 7 * * 1-5"  # Friendly format: daily around 7:00 on weekdays (scattered)
```

*Source: `github/gh-aw/.github/workflows/go-fan.lock.yml`, linked from the gallery page as "Go Fan generated workflow"*

### Shared `daily-issue-base.md` bundle definition — `github/gh-aw/.github/workflows/shared/daily-issue-base.md`

Fetched directly via `raw.githubusercontent.com`; reproduced verbatim.

```yaml
---
# Bundle for daily/scheduled code quality workflows that create GitHub issues.
# Bundles: activation-app + reporting guidelines + standardized create-issue safe-outputs.
#
# Usage:
#   imports:
#     - uses: shared/daily-issue-base.md
#       with:
#         title-prefix: "[my-workflow] "
#         expires: "2d"      # optional, default: 2d
#         labels: [automation, cookie]
#         assignees: [copilot]  # optional, default: []

import-schema:
  title-prefix:
    type: string
    required: true
    description: "Title prefix for created issues, e.g. '[my-workflow] '"
  expires:
    type: string
    default: "2d"
    description: "How long to keep issues before expiry"
  labels:
    type: array
    default: [automated-analysis, cookie]
    description: "Labels to apply to created issues"
  assignees:
    type: array
    default: []
    description: "Assignees for created issues"

imports:
  - shared/activation-app.md
  - shared/reporting.md

safe-outputs:
  create-issue:
    expires: ${{ github.aw.import-inputs.expires }}
    title-prefix: "${{ github.aw.import-inputs.title-prefix }}"
    labels: ${{ github.aw.import-inputs.labels }}
    assignees: ${{ github.aw.import-inputs.assignees }}
    max: 1
  noop:
---
```

*Source: `github/gh-aw/.github/workflows/shared/daily-issue-base.md`, imported by `go-fan.md`*

### Cache-memory round-robin state schema (source workflow prompt body)

```json
{
  "last_reviewed_module": "<module-path>",
  "reviewed_modules": [{"module": "<path>", "reviewed_at": "<ISO 8601 date>"}, ...]
}
```

*Source: `go-fan.md`, "Step 1: Load Round-Robin State from Cache" — stored at `/tmp/gh-aw/cache-memory/state.json`*

### Per-module scratchpad summary structure (source workflow prompt body)

```markdown
# Module: <full module path>

## Overview
Brief description of what the module does.

## Version Used
Current version from go.mod.

## Usage in gh-aw
- Files using this module
- Key APIs utilized
- Usage patterns observed

## Research Summary
- Repository: <github link>
- Latest Version: <version>
- Key Features: <list>
- Recent Changes: <notable updates>

## Improvement Opportunities
### Quick Wins
- <list>

### Feature Opportunities
- <list>

### Best Practice Alignment
- <list>

## References
- Documentation: <link>
- Changelog: <link>
- Last Reviewed: <date>
```

*Source: `go-fan.md`, "Step 6: Save Module Summary" — saved to `scratchpad/mods/<module-name>.md`*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-cache-memory-reference.md` Claim 11 (`missing_data` / `cache_memory_miss` formal error vocabulary for a malformed cache-memory read): Claim 5 above is a real, named production workflow (Go Fan) instructed to emit exactly this signal — the first corpus example naming a specific workflow that does so.
  - `docs-ghaw-guides-serena.md` (Serena as gh-aw's packaged semantic-code-analysis MCP server): Claim 6 above is a concrete production usage example, including the dedicated cache-memory subpath (`/tmp/gh-aw/cache-memory/serena/`) for Serena's own index.
  - `docs-ghaw-network-reference.md` Claim 6 (ecosystem-identifier allowlists in `network.allowed`, corroborated once already by the Code Simplifier's 6-ecosystem list in `docs-ghaw-gallery-code-improvement.md` Claim 6): Claim 9 above is a second, more narrowly-scoped real-world example (`[defaults, github, go]`).
  - `docs-ghaw-deterministic-agentic-patterns.md` (deterministic, non-LLM controls layered around an agentic core): Claim 2 above's round-robin module-selection algorithm is a deterministic control applied to *task selection* specifically, a use of the pattern not previously named in the corpus (existing coverage is trigger filtering and deduplication).
  - `docs-ghaw-agent-factory-status.md` Claim 7 (the Go language specialization cluster — six-plus Claude-only Go workflows in the GitHub Next factory catalog): that claim's evidence list names "Go Fan (daily 7:00 weekdays)" by workflow name and schedule, and the same entry appears in that note's scheduling catalog table ("Go Fan (7:00)") and its Go Language cluster table. This is an independent, catalog-level corroboration of Claim 8 above's `daily around 7:00 on weekdays` friendly-format schedule, arrived at from a different source page (the agent-factory status page, not the gallery) and without reading the workflow frontmatter. It also places Go Fan in context: it is one member of a deliberate Go-specialist cluster, not a standalone example, which supports this note's reading of Go Fan as a narrow single-domain agent (Claims 4 and 9). Note that the factory-status claim is graded `anecdotal` (schedules inferred from the catalog listing); this note's Claim 8 upgrades that specific schedule fact to `settled` with verbatim frontmatter and lock-file evidence.
  - `blog-ghaw-agent-of-the-day-2026-09-10.md` Claim 9 (Package Specification Librarian's `imports:` block) and `blog-ghaw-agent-of-the-day-2026-05-25.md` Claim 5 (Architecture Guardian's noise-prevention mechanisms): both already document real production consumption of the same `shared/daily-issue-base.md` bundle central to Claim 7 above. The spec-librarian note reproduces that workflow's parameterization verbatim (`assignees: [copilot]`, `expires: 3d`, `labels: [pkg-specifications, review, automation]`, `title-prefix: "[spec-librarian] "`), and the Architecture Guardian note attributes its "2-day expiry on issues" to `daily-issue-base.md` — which matches the bundle's documented `expires` default of `"2d"` reproduced in Concrete Artifacts above. Together these give three independent workflows (spec-librarian, Architecture Guardian, Go Fan) consuming one bundle at three different parameter settings, which is exactly the "one shared component, many configurations" outcome the mechanism is designed for. This note's contribution to that set is the bundle's own definition and defaults, which neither blog note reproduces.
  - **Open contradiction issue #3043** (weekday-cron scheduling: raw-cron-only claim vs. natural-language "friendly format" claim): Claim 8 above adds a second, independent production workflow (Go Fan, alongside the already-cited CLI Consistency Checker) using the identical `daily around HH:MM on weekdays` friendly-format string and exhibiting the same scattered-minute compilation behavior. This note does not re-file #3043; it strengthens the existing Side B evidence for whoever resolves it.

- **Contradicts**:
  - **Filed as new issue #3620**: `docs-ghaw-research-plan-assign-ops.md` Claim 11 states Go Fan "creates categorized discussions with improvement suggestions" and frames it as the reference implementation of the ResearchPlanAssignOps pattern's Discussion-producing Research phase. This note's Claim 1 shows, from the gallery page's own verbatim prose and the linked workflow source's `create-issue` (not `create-discussion`) safe-output configuration, that Go Fan creates a single GitHub **Issue**, not a Discussion. The existing note's claim was already graded anecdotal with no verbatim quote; this note's evidence is settled and verbatim from the canonical, first-party source for Go Fan specifically. No verdict is picked in this note — see issue #3620 for the full Side A/Side B writeup and a recommended (but not binding) `accepted-B` verdict.

- **Extends**:
  - `docs-ghaw-sharing-workflows.md` Claim 6 (parameterized template imports via `import-schema` + `uses`/`with`, documented there with a generic syntax example and the first-party rationale that it "allows single shared components to serve multiple consuming workflows with distinct configurations without requiring separate copies"): Claim 7 above extends that generic mechanism documentation with a real, shipped bundle's own schema — the actual parameter names, types, requiredness, and default values of `shared/daily-issue-base.md`, plus how the `${{ github.aw.import-inputs.* }}` expressions wire those parameters into the resulting `safe-outputs` block (see Concrete Artifacts). That note documents *that* the mechanism exists; this one shows what a production bundle's schema actually looks like and which parameters a consuming workflow can and cannot override (`max: 1` is fixed, not exposed in the schema).
  - `docs-ghaw-gallery-code-improvement.md`: Both gallery pages follow the same "thin teaching page, richer linked source workflow" structure (per that note's Extraction Notes and this note's own Extraction Notes below) — this is now a corroborated pattern across two independent gallery pages rather than a one-off observation.
  - `docs-ghaw-wizard.md` Claim 3 (archetype success-rate data: `dependency-monitor.json` reports `"success_rate": 0.5, "count": 55`): Go Fan is a real-world, single-dependency-domain (Go modules specifically) example of the general class of workflow the wizard's corpus data buckets as `dependency-monitor`. This note does not claim Go Fan is literally represented in that 55-repo sample — the wizard's archetype data is not linked by name to specific workflows the way `code-improvement.json`'s `anti_patterns` list names `code-simplifier` — but it is a concrete instance of the same task class the archetype measures, useful context if the guide cites the 0.5 success rate figure.
  - `docs-ghaw-research-plan-assign-ops.md`: Claim 3 above (the gallery page's own advisory, not descriptive, framing of the ResearchPlanAssignOps recommendation) adds nuance to how tightly Go Fan is actually coupled to that four-phase pattern — worth considering alongside the contradiction in #3620 when the guide decides how to present Go Fan's relationship to ResearchPlanAssignOps.

- **Novel**:
  - The explicit, fixed bash-command allowlist combined with `edit: null` (Claim 4) as a tool-configuration-level enforcement of a research-only, non-editing agent role is new to the corpus — prior safety-pattern coverage (draft PRs, validation gates, protected-files policies) all assumes the agent has an edit/write capability that is then gated; this is the first documented example of a gh-aw workflow with no edit tool at all.
  - The `shared/daily-issue-base.md` bundle's own `import-schema` parameter table (Claim 7) is the first extraction of a concrete, shipped bundle's declared parameters — names, types, requiredness, and defaults — together with the `${{ github.aw.import-inputs.* }}` wiring into its `safe-outputs` block. The `import-schema` *mechanism* is not novel to the corpus (`docs-ghaw-sharing-workflows.md` Claim 6 documents it generically), and the fact that this specific bundle is consumed in production is not novel either (two blog notes already cite it by name — see Cross-References); what is new is the bundle definition itself, which no prior note reproduces.
  - The two-tier memory split between a compact cache-memory control file and a separate `scratchpad/`-directory content archive (Claim 10) is a new, reusable memory-architecture pattern not named in any existing corpus note.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the `shared/daily-issue-base.md`-style parameterized import bundle (Claim 7) as a concrete pattern for standardizing safe-output configuration across a fleet of similar scheduled workflows — a typed `import-schema` with defaults, overridden per-workflow via `with:`. Add the deterministic round-robin module-selection algorithm (Claim 2) as a worked example of applying deterministic, non-LLM logic to *task selection* for a recurring research agent, extending existing `docs-ghaw-deterministic-agentic-patterns.md` coverage beyond trigger filtering and dedup.
- **Chapter 03 (Safety and Verification)**: Add the fixed bash-command allowlist plus `edit: null` (Claim 4) as a worked example of enforcing a read-only/advisory agent role at the tool-configuration level — a stronger guarantee than a prompt instruction not to edit files, since the capability is simply absent from the agent's toolset.
- **Chapter 02 (Harness Engineering)**: Document the two-tier state pattern (Claim 10) — small cache-memory control state vs. larger content-archive directory — as a reusable design for any recurring research agent that needs to accumulate detailed findings over time without bloating its round-trip cache-memory payload.
- **Do not cite Go Fan as an instance of ResearchPlanAssignOps's Discussion-producing Research phase** without resolving contradiction #3620 first — if the guide currently or in future cites Go Fan this way (following `docs-ghaw-research-plan-assign-ops.md` Claim 11), it should be corrected to describe Go Fan as creating a single Issue, per this note's Claim 1.

## Extraction Notes

1. **WebFetch avoided for the gallery page**: Given `docs-ghaw-gallery-code-improvement.md`'s prior documented finding that this same Astro/Starlight documentation platform's WebFetch summaries invent section headings not present on the actual page, I fetched the raw HTML directly via `curl` and extracted the `sl-markdown-content` container's inner HTML by hand, preserving exact prose. All quotes in this note are copied from that raw extraction.
2. **Followed the linked source workflow and its import**: The gallery page's "Workflow source" section links to both `go-fan.md` (the workflow source) and `go-fan.lock.yml` (the compiled workflow). I fetched both directly via `raw.githubusercontent.com`. `go-fan.md`'s frontmatter itself imports `shared/daily-issue-base.md`, which I also fetched directly since it is the source of the `create-issue` safe-output configuration central to Claim 1 and Claim 7 — three pages followed in total (gallery page, `go-fan.md`, `shared/daily-issue-base.md`), within MINER.md §1's up-to-5-linked-pages budget. `go-fan.lock.yml` (2046 lines) was fetched but only its `schedule:` block was extracted (Claim 8) — the remainder is generated boilerplate (compiled tool wiring, MCP server config) not meaningfully different from what `go-fan.md`'s frontmatter already specifies in source form.
3. **Other linked pages not followed**: The gallery page's "Learn More" section also links to `/gh-aw/reference/safe-outputs/` and `/gh-aw/reference/triggers/#scheduled-triggers-schedule`, both general platform reference pages already covered by existing corpus notes (`docs-ghaw-safe-outputs-specification.md`, `docs-ghaw-triggers-reference.md` / `docs-ghaw-fuzzy-schedule-specification.md`) and not specific to the dependency-analysis pattern, so they were not re-fetched.
4. **`shared/go-source-analysis.md` and `shared/otlp.md` imports not fetched**: `go-fan.md`'s frontmatter also imports two other shared bundles (`shared/go-source-analysis.md`, `shared/otlp.md`) beyond `daily-issue-base.md`. These were not fetched — `otlp.md` is very likely the OpenTelemetry reporting bundle already covered by `docs-ghaw-open-telemetry-attributes.md`, and `go-source-analysis.md` appeared, from its name and from the Serena/bash-tool configuration already visible in `go-fan.md`'s own frontmatter, to be Go-specific tooling setup rather than a distinct pattern worth a fourth fetch within this note's scope. Flagging this as an area a future extraction pass could follow up on if `shared/go-source-analysis.md` turns out to carry additional Go-specific tool-scoping conventions.
5. **Contradiction filed**: Per MINER.md §4a, filed issue #3620 for the disagreement described in Cross-References → Contradicts (this page's and the linked workflow source's unambiguous "creates a single issue" framing vs. `docs-ghaw-research-plan-assign-ops.md` Claim 11's "creates categorized discussions" framing). No verdict is picked in this note.
6. **Existing contradiction #3043 not re-filed**: While reading `go-fan.md`'s schedule frontmatter, I found a second, independent production example of the "friendly format" weekday-cron syntax already at the center of open contradiction issue #3043. Per MINER.md §4a's "when NOT to file" guidance (already filed), I added this as corroborating evidence in Cross-References rather than opening a duplicate issue.
7. **No publication date**: The gallery page carries no visible publication or last-updated date; `date_published` is left null, consistent with other `docs-ghaw-*` notes in this corpus. `confidence_overall` is set to `emerging` rather than `settled` — the configuration and prompt claims themselves are settled, verbatim first-party facts, but the note's Claim 1 and Claim 3 findings materially conflict with an existing corpus note about the same workflow (pending resolution of issue #3620), which keeps the note as a whole from being presented as fully settled guidance.
