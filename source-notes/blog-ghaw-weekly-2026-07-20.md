---
source_url: https://github.github.com/gh-aw/blog/2026-07-20-weekly-update/
source_type: blog-post
title: "Weekly Update – July 20, 2026 (GitHub Agentic Workflows)"
author: GitHub Agentic Workflows team (gh-aw); byline "Copilot"
date_published: 2026-07-20
date_extracted: 2026-07-20
last_checked: 2026-07-20
status: current
confidence_overall: emerging
issue: "#2059"
---

# Weekly Update – July 20, 2026 (GitHub Agentic Workflows)

> v0.82.13 (published July 18) ships one breaking change — `gh aw add` now
> refuses to install packages containing an `aw.yml` config file (PR #46273) —
> alongside four "What's New" items (auto-configured
> `COPILOT_PROVIDER_WIRE_API`, default-on issue intent metadata, `NO_COLOR`
> support, stronger ESLint alias detection for `@actions/core`) and five
> additional notable PRs: a firewall bump to v0.27.37 adding
> `ANTHROPIC_AUTH_TOKEN` credential isolation and rootless-install PATH
> support, a new `--rootless` flag for `install_copilot_cli.sh` on ARC/DinD
> runners, a new `timenowsub` linter explicitly credited to "the linter-miner,"
> a workshop redesign (moved to `/workshop/`, step-count displays), and an
> MCP toolset sync with upstream `github-mcp-server`. The Agent of the Week is
> Avenger, an hourly CI-guardian agent — new to the corpus — that merges
> `main`, runs `recompile`/`fmt`/`lint`/`test`, and opens a fix PR when
> something breaks; this week it verified all 258 recompiled `.lock.yml`
> files survived the firewall bump without CI regressions.

## Source Context

- **Type**: blog-post (weekly changelog/update from the official GitHub
  Agentic Workflows blog; covers the week around the July 18, 2026 release of
  v0.82.13; one breaking change, four "What's New" release-note items, five
  "Notable Pull Requests" not bundled into the release notes, and an Agent of
  the Week spotlight)
- **Author credibility**: The gh-aw blog is the official publication of
  GitHub's Agentic Workflows platform team. The page's `schema.org/BlogPosting`
  JSON-LD and on-page byline both name the author as "Copilot" (same
  non-human byline pattern documented in `blog-ghaw-weekly-2026-07-13.md` and
  `blog-ghaw-weekly-2026-07-06.md`, distinct from the human-bylined "Meet the
  Workflows" series). PR numbers appear as visible inline text in this post
  (e.g., "gh aw add now rejects packages with aw.yml config (#46273)"),
  verified directly against the raw page HTML fetched via `curl`, not a
  WebFetch summary (see Extraction Notes).
- **Scope**: One breaking change and nine named PRs across CLI ergonomics,
  audit metadata, linting, sandbox/firewall credential handling, custom
  runner support, the developer workshop UI, and MCP toolset definitions,
  plus one Agent of the Week spotlight (`avenger`, its first appearance in
  this corpus). Does NOT cover: the internal implementation of the ESLint
  alias-detection rule; the exact semantics of "issue intent metadata" beyond
  "richer audit trails"; the `avenger` workflow's YAML/frontmatter; how
  `ANTHROPIC_AUTH_TOKEN` credential isolation is implemented inside
  `gh-aw-firewall`; or a numeric list of the "runner doctor catalog updates"
  bundled into the firewall bump.

## Extracted Claims

### Claim 1: `gh aw add` now refuses to install any package that contains an `aw.yml` configuration file, requiring maintainers to update those packages before upgrading (PR #46273) — a breaking change

- **Evidence**: "! Breaking Change" section, single PR.
- **Confidence**: settled (specific PR, the new refusal behavior and required
  remediation are both stated plainly)
- **Quote**: "`gh aw add` now rejects packages with `aw.yml` config (#46273):
  If you maintain packages that include an `aw.yml` configuration file,
  update them before upgrading — the CLI will now refuse to install them
  outright."
- **Our assessment**: This is a hard compatibility break for any
  package-based workflow-sharing setup that still ships an `aw.yml` at the
  package root — installation now fails outright rather than warning. No
  existing corpus note (including `docs-ghaw-sharing-workflows.md`) documents
  `aw.yml` as a deprecated or disallowed package-root file, so this is the
  first evidence in the corpus that `gh aw add` enforces a package-content
  restriction rather than only resolving imports. For Ch02 (Harness
  Engineering): flag this as an upgrade blocker to check before bumping to
  v0.82.13 — any shared workflow package with a root-level `aw.yml` must be
  restructured first, or `gh aw add` will refuse to install it.

### Claim 2: The CLI now auto-configures `COPILOT_PROVIDER_WIRE_API` from the model catalog, removing a manual setup step (PR #46156)

- **Evidence**: "What's New" list item, single PR.
- **Confidence**: emerging (single PR, first-party changelog description; the
  prior manual configuration process and which providers/models trigger
  auto-resolution are not described)
- **Quote**: "Auto-configure `COPILOT_PROVIDER_WIRE_API` from the model
  catalog (#46156): The CLI now resolves the provider wire API endpoint
  automatically, so you don't have to set it by hand."
- **Our assessment**: A configuration-ergonomics fix consistent with the
  general gh-aw pattern of reducing manual frontmatter/environment setup as
  the model catalog and engine matrix grow (see `docs-ghaw-engines-reference.md`
  for the broader engine/provider configuration surface this auto-resolution
  presumably simplifies). For Ch02: minor; note as a removed manual-setup
  step for teams configuring custom model providers.

### Claim 3: `set_issue_type`, `set_issue_field`, and `add_labels` now emit issue intent metadata by default, with no configuration required (PR #46207)

- **Evidence**: "What's New" list item, single PR.
- **Confidence**: emerging (single PR, first-party changelog description;
  what "intent metadata" contains structurally, and whether it was
  previously available only opt-in or not at all, is not specified)
- **Quote**: "Default-on issue intent metadata (#46207): `set_issue_type`,
  `set_issue_field`, and `add_labels` now emit intent metadata by default —
  richer audit trails with zero extra config."
- **Our assessment**: This is an audit-trail enrichment for three specific
  issue-management safe-output actions, changing their default behavior
  rather than adding a new action type. No existing corpus note documents
  "issue intent metadata" as a concept, so this is new terminology to the
  corpus. For Ch04 (Safety and Constraints) / Ch06 (Agentic Operations): note
  that issue-mutation safe outputs (`set_issue_type`, `set_issue_field`,
  `add_labels`) now carry richer default audit metadata — relevant to any
  guide section on tracing which workflow run made a given issue-field
  change, though the post does not describe what fields the metadata
  contains.

### Claim 4: The CLI now honours the `NO_COLOR` environment variable for cleaner output in CI and accessibility-focused terminals (PR #46197)

- **Evidence**: "What's New" list item, single PR.
- **Confidence**: settled (specific PR, specific environment variable and
  stated purpose)
- **Quote**: "`NO_COLOR` support (#46197): The CLI now honours the `NO_COLOR`
  environment variable for cleaner output in CI and accessibility-focused
  terminals."
- **Our assessment**: `NO_COLOR` is an established cross-tool convention
  (no-color.org); adopting it is a low-risk compatibility fix rather than a
  novel design choice. For Ch02: minor; worth a one-line mention in any CLI
  output/logging configuration checklist for teams running `gh aw` in
  CI pipelines that parse or archive raw log output.

### Claim 5: The `no-core-setoutput` and `exportvariable` ESLint rules now catch aliased and destructured `@actions/core` bindings, closing a bypass pattern that previously let those imports evade detection (PR #46365)

- **Evidence**: "What's New" list item, single PR, naming both rule names and
  the specific bypass class (aliased/destructured imports).
- **Confidence**: settled (specific PR, specific rule names, specific bypass
  mechanism named)
- **Quote**: "Stronger ESLint alias detection (#46365): The
  `no-core-setoutput` and `exportvariable` rules now catch aliased and
  destructured `@actions/core` bindings, closing a common bypass pattern."
- **Our assessment**: This is a static-analysis precision fix for a JS/TS
  linting layer distinct from the Go-focused `linter-miner`/Sergo/LintMonster
  loop documented in `blog-ghaw-custom-linters-three-workflow-loop.md` — same
  underlying failure class Sergo hunts for in that loop (a linter rule with a
  detection gap that lets a semantically-equivalent-but-differently-written
  pattern slip through), but applied here to JavaScript/TypeScript Actions
  code rather than Go. `import { setOutput as x } from '@actions/core'` or
  `const { setOutput } = require('@actions/core')` are the kind of
  alias/destructure patterns a naive rule matching only `core.setOutput(...)`
  would miss; closing that gap tightens enforcement of whatever
  `no-core-setoutput`/`exportvariable` are meant to prevent (presumably
  writing step outputs or exported variables through the deprecated/unsafe
  `@actions/core` surface rather than the workflow's own safe-output
  mechanism). For Ch02 (Harness Engineering): add "alias/destructure evasion"
  as a named class of linting-rule gap to check for when writing custom
  JS/TS static-analysis rules, corroborating the same precision-gap concern
  Sergo enforces for Go analyzers in the three-workflow loop.

### Claim 6: The default `gh-aw-firewall` was bumped from v0.27.35 to v0.27.37, adding `ANTHROPIC_AUTH_TOKEN` credential isolation, `~/.local/bin` added to the sandbox PATH for rootless Copilot installs, and runner doctor catalog updates (PR #46637)

- **Evidence**: "Notable Pull Requests" list item, single PR, naming the
  exact version bump and three distinct changes bundled into it.
- **Confidence**: settled (specific PR, specific version strings, three
  named changes)
- **Quote**: "Firewall bump to v0.27.37: The default `gh-aw-firewall` was
  updated from v0.27.35 to v0.27.37, bringing `ANTHROPIC_AUTH_TOKEN`
  credential isolation, `~/.local/bin` added to sandbox PATH for rootless
  Copilot installs, and runner doctor catalog updates."
- **Our assessment**: This is the second consecutive weekly release to bump
  `gh-aw-firewall` with a version-pinning discipline consistent with
  `blog-ghaw-weekly-2026-06-29.md` Claim 4 (gh-aw-firewall v0.27.12 → v0.27.13
  with SHA-pinned digests) — the firewall is evidently on a near-weekly patch
  cadence. `ANTHROPIC_AUTH_TOKEN` credential isolation is the first corpus
  mention of Anthropic-specific credential handling inside the firewall
  layer itself (as opposed to the engine/provider configuration surface in
  `docs-ghaw-engines-reference.md`); it is conceptually the same principle
  Anthropic's own agent-identity architecture describes — credentials
  injected at a boundary rather than exposed to the running agent process
  (`blog-anthropic-agent-identity-access-model.md` Claim 8: "Credentials are
  stored independently, mapped to channel identity, and injected at the
  network boundary at request time") — though these are two different
  products (gh-aw's per-agent-process firewall vs. Claude Tag's per-channel
  identity system) and the post does not describe gh-aw's isolation mechanism
  in enough detail to confirm they work identically. The `~/.local/bin`
  PATH addition is a companion fix for the same rootless-Copilot-install
  theme as Claim 7 below — this bump makes the sandboxed environment aware of
  a rootless install location, while Claim 7 adds the installer flag that
  produces a rootless install in the first place. For Ch04 (Safety and
  Constraints): add `ANTHROPIC_AUTH_TOKEN` credential isolation to the
  firewall's documented capabilities (currently `docs-ghaw-sandbox-reference.md`
  covers network/filesystem/MCP-Gateway controls but not credential
  isolation specifically) — flagged as a new dimension pending a dedicated
  reference source describing the isolation mechanism.

### Claim 7: `install_copilot_cli.sh` now accepts a `--rootless` flag for ARC and Docker-in-Docker runner environments, fixing installation for teams running Copilot on custom runners (PR #46047)

- **Evidence**: "Notable Pull Requests" list item, single PR.
- **Confidence**: settled (specific PR, specific flag name, specific target
  environments named)
- **Quote**: "Rootless flag for ARC/DinD runners: `install_copilot_cli.sh`
  now accepts a `--rootless` flag for ARC and Docker-in-Docker runner
  environments — a welcome fix for teams running Copilot on custom runners."
- **Our assessment**: This targets a specific operational pain point:
  Actions Runner Controller (ARC) and Docker-in-Docker runner setups often
  run without root privileges inside the runner container, and a Copilot CLI
  installer that assumes root access would fail or require workarounds in
  that environment. No existing corpus note documents rootless runner
  support as a gh-aw capability — this is new to the corpus and, paired with
  Claim 6's `~/.local/bin` PATH fix, represents a small coordinated push
  toward rootless-runner compatibility across two different PRs in the same
  week. For Ch02 (Harness Engineering): add `install_copilot_cli.sh
  --rootless` to the setup guidance for teams self-hosting runners via ARC
  or Docker-in-Docker, cross-referenced with Claim 6's sandbox PATH change
  as the two halves of rootless-install support.

### Claim 8: A new `timenowsub` Go linter, explicitly credited to "the linter-miner," flags `time.Now().Sub(t)` and automatically rewrites it to the idiomatic `time.Since(t)` (PR #46633)

- **Evidence**: "Notable Pull Requests" list item, single PR, naming the
  linter, its detection pattern, its rewrite target, and its origin.
- **Confidence**: settled (specific PR, specific anti-pattern and rewrite
  target named, explicit attribution to "the linter-miner")
- **Quote**: "New `timenowsub` linter: The linter-miner contributed another
  Go linter that flags `time.Now().Sub(t)` and auto-rewrites it to the
  idiomatic `time.Since(t)`. Small but satisfying."
- **Our assessment**: `time.Now().Sub(t)` and `time.Since(t)` are
  functionally equivalent in Go, but `time.Since(t)` is idiomatic and avoids
  a redundant intermediate `time.Now()` call — a style/readability linter
  rather than a correctness or resource-leak linter, distinct in character
  from `timeafterleak` (resource leak) or `errorfwrapv` (error-chain
  correctness) documented in
  `blog-ghaw-custom-linters-three-workflow-loop.md` Claim 2 / Concrete
  Artifacts. This post's explicit, lowercase-hyphenated attribution to "the
  linter-miner" is more definite phrasing than `blog-ghaw-weekly-2026-06-29.md`
  Claim 5's `osgetenvlibrary`, where the source did not explicitly name
  Linter Miner as the origin and the Miner's note flagged that as an
  uncertain attribution. Taken together, this extends the named
  Linter-Miner-produced-analyzer catalog (six examples: `fprintlnsprintf`,
  `timeafterleak`, `errorfwrapv`, `wgdonenotdeferred`, `lenstringsplit`,
  `stringreplaceminusone`, per `blog-ghaw-custom-linters-three-workflow-loop.md`
  Concrete Artifacts) with a seventh explicitly-attributed member,
  `timenowsub`, and an eighth likely-but-unconfirmed member (`osgetenvlibrary`)
  from the prior month. For Ch02 (Harness Engineering): add `timenowsub` to
  the running catalog of Linter Miner output, and note that this week's post
  uses definite attribution language ("the linter-miner contributed") where
  a prior week's post did not — worth tracking whether the blog is becoming
  more consistent about crediting linter provenance.

### Claim 9: The developer workshop was moved to `/workshop/`, restyled to match docs styling (PR #46593), and now shows step counts on entry and scenario cards (PR #46622), making it easier to gauge remaining work before starting (PR #46616 overall)

- **Evidence**: "Notable Pull Requests" list item bundling three PR numbers
  under one headline change.
- **Confidence**: emerging (three specific PRs named; the workshop's prior
  URL path, prior styling, and the specific UI mechanism for step-count
  display are not described)
- **Quote**: "Workshop redesign: The workshop has been moved to `/workshop/`,
  simplified to match docs styling (#46593), and now shows step counts on
  entry and scenario cards (#46622) — making it much easier to gauge how much
  is left before you start."
- **Our assessment**: No existing corpus note documents a gh-aw "workshop" as
  a distinct developer-facing surface — this is new to the corpus. The
  combination of a URL move, a styling pass to match the main docs site, and
  a step-count affordance on cards suggests the workshop is a hands-on
  tutorial/exercise section (the "step counts on entry and scenario cards"
  phrasing implies a catalog of scenarios each with a bounded number of
  steps) rather than a reference doc. For Ch02 (Harness Engineering): flag
  the gh-aw workshop (`/workshop/`) as a practitioner onboarding resource
  worth a dedicated follow-up source-note mining pass, since this post only
  describes UI changes to it, not its content or scope.

### Claim 10: GitHub MCP toolset mappings were synchronized with the upstream `github-mcp-server` main branch, keeping tool definitions current (PR #46604)

- **Evidence**: "Notable Pull Requests" list item, single PR.
- **Confidence**: emerging (single PR, first-party changelog description;
  what specifically changed in the toolset mappings, or whether any
  gh-aw-facing tool names/schemas shifted as a result, is not stated)
- **Quote**: "MCP toolsets sync: GitHub MCP toolset mappings were synced with
  the upstream `github-mcp-server` main branch, keeping tool definitions up
  to date."
- **Our assessment**: A maintenance-sync PR keeping gh-aw's bundled GitHub
  MCP tool definitions aligned with the upstream `github-mcp-server` project,
  relevant to `docs-ghaw-github-tools.md` and `docs-ghaw-mcps.md`'s coverage
  of the GitHub MCP surface gh-aw workflows can call. For Ch02: minor;
  note as routine dependency-currency maintenance for the GitHub MCP
  toolset, analogous to the SHA-pinned-digest maintenance pattern documented
  in `blog-ghaw-weekly-2026-06-29.md` Claim 4 for firewall/gateway runtime
  components.

### Claim 11: Avenger is an hourly-scheduled "CI guardian" agent that checks whether CI is passing and, if not, merges `main`, runs `recompile`/`fmt`/`lint`/`test`, and opens a PR with any fixable issues; this week it verified all 258 recompiled `.lock.yml` files survived the v0.27.37 firewall bump without introducing CI regressions

- **Evidence**: "Agent of the Week" section, three paragraphs describing
  Avenger's function, this week's run outcomes, and a specific highlighted
  run tied to the Claim 6 firewall bump.
- **Confidence**: anecdotal for the specific weekly narrative (run counts,
  the 258-file check, "achieved `success` across the board" framing); the
  described *function* (hourly schedule, merge-and-quality-gate-and-fix-PR
  behavior) reads as settled first-party description of the workflow's
  design, though no workflow YAML/frontmatter is shown
- **Quote**: "The CI guardian who never sleeps — Avenger runs every hour,
  checks whether CI is passing, and if it's not, merges `main`, runs
  `recompile`/`fmt`/`lint`/`test`, and opens a PR with any fixable issues."
  Weekly narrative: "This week, Avenger ran multiple times and achieved
  `success` across the board, quietly keeping the codebase tidy during the
  busy firewall bump and workshop refactor merge storm. Each run it
  faithfully pulled in the latest `main`, ran the full quality gauntlet, and
  — finding nothing broken — went back to sleep without making a fuss."
  Highlighted run: "The highlight of Avenger's week was its run right after
  the v0.27.37 firewall bump landed, where it dutifully checked that all 258
  recompiled `.lock.yml` files hadn't introduced any CI regressions. They
  hadn't. Avenger nodded once and clocked out." Usage tip: "Avenger shines in
  repos where automated PRs (dependency bumps, codegen, lock file updates)
  can quietly break CI — it catches those regressions within the hour so
  humans don't have to."
- **Our assessment**: Avenger is the first Agent of the Week in this corpus
  whose core function is *self-referential CI maintenance of the gh-aw
  project's own generated artifacts* (recompiled `.lock.yml` files) rather
  than an external-facing task like triage, reporting, investigation, or
  persona-based evaluation — distinct from `auto-triage-issues`,
  `api-consumption-report`, `weekly-issue-summary`, `aw-failure-investigator`
  (`blog-ghaw-weekly-2026-06-15.md`, `blog-ghaw-weekly-2026-07-06.md`,
  `blog-ghaw-weekly-2026-07-13.md`), `delight` (`blog-ghaw-weekly-2026-06-22.md`),
  and `agent-persona-explorer` (`blog-ghaw-weekly-2026-06-29.md` Claim 9). It
  is conceptually closest to `aw-failure-investigator` (also reactive to CI/
  workflow failures) but Avenger's remit is narrower and more mechanical:
  merge, recompile, run the standard quality gates, and fix what's fixable —
  a scheduled regression-catcher for a specific, high-churn artifact class
  (compiled lock files) rather than open-ended failure investigation across
  the whole run history. The 258-`.lock.yml`-file check after the firewall
  bump is a concrete instance of exactly the failure mode the usage tip
  describes: an automated dependency-style PR (the firewall version bump)
  that could silently break CI if the regenerated lock files didn't compile
  cleanly, caught within the scheduled hour rather than left for a human to
  discover later. This makes the firewall bump (Claim 6) and Avenger's
  highlighted run two halves of the same story: one PR changes a pinned
  dependency and regenerates 258 derived files; a separate, unrelated
  scheduled agent independently verifies none of those 258 files broke
  anything. For Ch06 (Agentic Operations): add `avenger` as a named pattern
  for "scheduled regression-catcher for bulk-regenerated derived artifacts"
  — generalizes beyond gh-aw/lock-files to any codebase where a config or
  dependency change triggers regeneration of many derived files (generated
  code, compiled configs, lockfiles) that could each silently fail to
  recompile; pair with the usage tip's framing ("repos where automated PRs...
  can quietly break CI") as the trigger condition for when this pattern is
  worth adopting.

## Concrete Artifacts

### Release Summary: v0.82.13 (published July 18, 2026)

```
Breaking Change:
  gh aw add rejects packages with aw.yml config (#46273)
    Packages containing an aw.yml configuration file are now refused at
    install time; maintainers must update affected packages before upgrading

What's New:
  Auto-configure COPILOT_PROVIDER_WIRE_API from model catalog (#46156)
  Default-on issue intent metadata (#46207)
    set_issue_type, set_issue_field, add_labels now emit intent metadata
    by default
  NO_COLOR support (#46197)
  Stronger ESLint alias detection (#46365)
    no-core-setoutput, exportvariable rules now catch aliased/destructured
    @actions/core bindings

Notable Pull Requests:
  Firewall bump to v0.27.37 (#46637)
    gh-aw-firewall v0.27.35 -> v0.27.37
    Adds: ANTHROPIC_AUTH_TOKEN credential isolation
          ~/.local/bin added to sandbox PATH for rootless Copilot installs
          runner doctor catalog updates
  Rootless flag for ARC/DinD runners (#46047)
    install_copilot_cli.sh --rootless flag
  New timenowsub linter (#46633)
    Flags time.Now().Sub(t) -> auto-rewrites to time.Since(t)
    Attributed to "the linter-miner"
  Workshop redesign (#46616, #46593, #46622)
    Moved to /workshop/; restyled to match docs; step counts on cards
  MCP toolsets sync (#46604)
    Synced with upstream github-mcp-server main branch
```

*Source: this week's blog post, "! Breaking Change," "What's New," and
"Notable Pull Requests" sections (raw HTML fetched via `curl`, 2026-07-20)*

### Agent of the Week: `avenger` — July 2026 (first spotlight)

```
Agent:          avenger
Function:       "CI guardian" — runs every hour, checks whether CI is
                passing; if not, merges main, runs recompile/fmt/lint/test,
                opens a PR with any fixable issues
Schedule:       Hourly

This week's activity:
  Ran multiple times, achieved `success` across the board throughout the
  firewall bump (#46637) and workshop refactor (#46616) merge storm

Highlighted run:
  Ran right after the v0.27.37 firewall bump landed
  Verified: all 258 recompiled .lock.yml files
  Result: no CI regressions introduced

Usage tip (from source):
  Best suited to repos where automated PRs (dependency bumps, codegen,
  lock file updates) can quietly break CI — catches regressions within
  the hour

Workflow definition:
  https://github.com/github/gh-aw/blob/main/.github/workflows/avenger.md
```

*Source: this week's blog post, "Agent of the Week: Avenger" section (raw
HTML fetched via `curl`, 2026-07-20)*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-weekly-2026-06-29.md` Claim 4 (`gh-aw-firewall` v0.27.12 →
    v0.27.13 bump, paired with SHA-pinned container digest re-attestation):
    Claim 6 here (firewall v0.27.35 → v0.27.37) corroborates that
    `gh-aw-firewall` receives near-weekly version bumps as an ongoing
    maintenance cadence, consistent with the supply-chain re-attestation
    pattern that note documents.
  - `blog-ghaw-custom-linters-three-workflow-loop.md` Claim 2 and Concrete
    Artifacts (six named Linter-Miner-produced analyzers:
    `fprintlnsprintf`, `timeafterleak`, `errorfwrapv`, `wgdonenotdeferred`,
    `lenstringsplit`, `stringreplaceminusone`): Claim 8 here (`timenowsub`)
    corroborates the Linter Miner production pattern with a seventh named,
    explicitly-attributed example.
  - `blog-anthropic-agent-identity-access-model.md` Claim 8 (credentials
    "injected at the network boundary at request time," never attached to
    individual users): Claim 6 here's `ANTHROPIC_AUTH_TOKEN` credential
    isolation in `gh-aw-firewall` corroborates the same general architectural
    principle — isolate credentials at a boundary layer rather than exposing
    them to the running agent process — though the two are different
    products (gh-aw's per-workflow-run firewall vs. Claude Tag's per-channel
    identity system) and this post does not describe gh-aw's mechanism in
    enough detail to confirm the implementations are analogous beyond the
    shared principle.

- **Extends**:
  - `docs-ghaw-sandbox-reference.md` (documents AWF firewall network/
    filesystem/MCP-Gateway controls as of its 2026-05-12 extraction):
    Claim 6 here adds `ANTHROPIC_AUTH_TOKEN` credential isolation as a
    firewall capability not covered in that reference — a new dimension
    (credential isolation) alongside the network/filesystem/gateway
    dimensions already documented, similar to how
    `blog-ghaw-weekly-2026-07-13.md` Claims 1 and 6 extended that same
    reference with `sandbox.agent.runtime` options (gVisor, docker-sbx).
  - `blog-ghaw-weekly-2026-06-29.md` Claim 5 (`osgetenvlibrary` linter,
    attribution to Linter Miner left uncertain because the source did not
    explicitly name it): Claim 8 here extends that observation — this
    week's post uses explicit, definite attribution ("the linter-miner
    contributed another Go linter") for `timenowsub`, suggesting the blog's
    attribution practice may be becoming more consistent, though this alone
    doesn't retroactively confirm `osgetenvlibrary`'s origin.
  - `blog-ghaw-weekly-2026-06-15.md` and `blog-ghaw-weekly-2026-07-06.md`
    and `blog-ghaw-weekly-2026-06-22.md` and `blog-ghaw-weekly-2026-06-29.md`
    Claim 9 (Agent of the Week spotlights: `aw-failure-investigator`,
    `weekly-issue-summary`, `delight`, `agent-persona-explorer`): Claim 11
    here extends the Agent of the Week catalog with `avenger`, a distinct
    "scheduled regression-catcher for bulk-regenerated derived artifacts"
    pattern not previously represented — the closest prior analogue,
    `aw-failure-investigator`, investigates failures broadly rather than
    specifically re-verifying a bulk-regenerated artifact class after a
    triggering change.
  - `docs-ghaw-github-tools.md` / `docs-ghaw-mcps.md` (GitHub MCP tool
    surface documentation): Claim 10 here (MCP toolset sync with upstream
    `github-mcp-server`) is a maintenance update to the tool definitions
    those references describe.

- **Contradicts**: None identified at the MINER.md §4a filing threshold. No
  claim in this source materially opposes an existing source note's claim on
  the same topic. The firewall version bump (Claim 6) and the linter
  attribution language (Claim 8) are updates/clarifications to prior notes,
  not disagreements with them.

- **Novel**:
  - **`gh aw add` refusing to install packages containing `aw.yml`** (Claim 1):
    the first corpus source documenting a hard package-content restriction
    enforced by the CLI's install path, rather than an import-resolution
    behavior change.
  - **Issue intent metadata as a named audit-trail concept** (Claim 3): no
    prior corpus note uses this term for issue-mutation safe outputs.
  - **`ANTHROPIC_AUTH_TOKEN` credential isolation inside `gh-aw-firewall`**
    (Claim 6): the first corpus source documenting Anthropic-credential-
    specific handling at the firewall/sandbox layer, as opposed to the
    engine/provider configuration surface.
  - **Rootless runner support (`--rootless` flag, `~/.local/bin` PATH fix)**
    (Claims 6, 7): no existing corpus note documents gh-aw rootless-runner
    compatibility for ARC or Docker-in-Docker environments.
  - **The gh-aw developer workshop as a distinct product surface** (Claim 9):
    no existing corpus note mentions a gh-aw "workshop" at `/workshop/` —
    entirely new to the corpus, though this post only describes UI changes
    to it, not its content.
  - **`avenger` as a scheduled CI-guardian / bulk-artifact-regression-catcher
    agent** (Claim 11): the first Agent of the Week in the corpus whose
    function is self-referential maintenance of the gh-aw project's own
    generated artifacts rather than an externally-facing reporting,
    triage, investigation, or evaluation task.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Flag the `aw.yml`-in-package install refusal (Claim 1) as an upgrade
    blocker to check when bumping to v0.82.13 or later.
  - Add `timenowsub` to the running Linter Miner output catalog alongside
    the six examples in `blog-ghaw-custom-linters-three-workflow-loop.md`
    (Claim 8).
  - Add `install_copilot_cli.sh --rootless` and the `~/.local/bin` sandbox
    PATH fix (Claims 6, 7) to setup guidance for teams self-hosting runners
    via ARC or Docker-in-Docker.
  - Add "alias/destructure evasion" as a named class of linting-rule
    detection gap to check for in custom JS/TS static-analysis rules
    (Claim 5), corroborating the same precision-gap concern Sergo enforces
    for Go analyzers.

- **Chapter 04 (Safety and Constraints)**:
  - Add `ANTHROPIC_AUTH_TOKEN` credential isolation (Claim 6) to the
    firewall's documented security capabilities, pending a dedicated
    reference source for the isolation mechanism's implementation details —
    `docs-ghaw-sandbox-reference.md` currently covers network/filesystem/
    MCP-Gateway controls only.
  - Note the issue-intent-metadata default-on change (Claim 3) as a richer
    default audit trail for issue-mutation safe outputs.

- **Chapter 06 (Agentic Operations)**:
  - Add `avenger` (Claim 11) as a named "scheduled regression-catcher for
    bulk-regenerated derived artifacts" pattern — generalizes beyond gh-aw
    to any codebase where a config/dependency change triggers regeneration
    of many derived files. Pair with the source's own usage tip: best suited
    to repos where automated PRs (dependency bumps, codegen, lock file
    updates) can quietly break CI.
  - Flag the gh-aw workshop (`/workshop/`, Claim 9) as a practitioner
    onboarding resource worth a dedicated follow-up mining pass, since this
    post only covers its UI redesign, not its content.

## Extraction Notes

1. **Raw HTML fetched via `curl` and used for all quotes and figures in this
   note.** An initial WebFetch pass returned a condensed, accurate-looking
   summary, but per the practice established in `blog-ghaw-weekly-2026-07-13.md`
   Extraction Note 1 (where a WebFetch summary misattributed a qualified
   figure), this note verifies every quote against the page's raw HTML
   (fetched via `curl`) rather than relying on the WebFetch summary alone.
   All `<code>`-tagged inline elements in the source are rendered as
   backtick-quoted code spans in this note's quotes, consistent with the
   convention used in prior weekly-update notes.

2. **PR numbers are visible inline text in this post**, as in
   `blog-ghaw-weekly-2026-07-13.md` (and unlike `blog-ghaw-weekly-2026-07-06.md`,
   where PR numbers were link-only). This week's post prints PR numbers
   directly in prose (e.g., "#46273", "#46156"), confirmed against the raw
   HTML's visible text content.

3. **The "runner doctor catalog updates" bundled into the firewall bump
   (Claim 6) are named but not itemized** in the source — the post lists
   this as one of three changes in the v0.27.37 bump without further detail.
   This note preserves it as an unspecified catalog update rather than
   inferring its content.

4. **No sub-pages followed.** This is a single blog post page. It links to
   ten PRs/issues on GitHub, the v0.82.13 release tag, and the `avenger`
   workflow definition file. Per MINER.md §1, up to 5 substantive linked
   pages may be followed; these are primary-source artifacts referenced by,
   rather than sub-pages of, the blog post itself, and (consistent with the
   practice in `blog-ghaw-weekly-2026-07-13.md` Extraction Note 5) were not
   independently fetched in full for this note — their URLs are recorded in
   Concrete Artifacts for follow-up mining if deeper verification is needed
   (especially for the gh-aw workshop, per Guide Impact above, and for the
   `ANTHROPIC_AUTH_TOKEN` isolation mechanism, per Claim 6).

5. **No contradictions filed.** Reviewed all cross-referenced source notes
   (`docs-ghaw-sandbox-reference.md`, `docs-ghaw-engines-reference.md`,
   `blog-ghaw-weekly-2026-06-29.md`, `blog-ghaw-weekly-2026-07-06.md`,
   `blog-ghaw-weekly-2026-07-13.md`, `blog-ghaw-custom-linters-three-workflow-loop.md`,
   `blog-anthropic-agent-identity-access-model.md`). No claim in this source
   materially opposes an existing source note's claim at the MINER.md §4a
   filing threshold — the differences noted (version bumps, attribution
   clarity, schema growth) are extensions/updates, not disagreements, so no
   contradiction issue was filed.
