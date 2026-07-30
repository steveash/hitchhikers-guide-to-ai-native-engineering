---
source_url: https://github.github.com/gh-aw/guides/docs-automation
source_type: docs
title: "GitHub Agentic Workflows: Keeping documentation up to date automatically"
author: GitHub Agentic Workflows team (official documentation)
date_published: null
date_extracted: 2026-07-30
last_checked: 2026-07-30
status: current
confidence_overall: emerging
issue: "#2332"
---

# GitHub Agentic Workflows: Keeping documentation up to date automatically

> A short, official gh-aw guide for a single starter workflow — `docs-updater` —
> that runs weekly, detects doc/code drift over the prior seven days, and proposes
> fixes as a draft PR using a read-only permission block plus `create-pull-request`.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows "Guides" page, part of the
  gh-aw documentation site's practitioner-facing guide section, not a blog post)
- **Author credibility**: First-party documentation from the GitHub Agentic
  Workflows team (GitHub Next / Microsoft Research). Authoritative for what
  gh-aw supports and recommends as a starter configuration; not independently
  validated with production usage data or metrics.
- **Scope**: Extremely narrow and short — one use case (documentation drift
  detection), one starter installer command, one YAML example, and one paragraph
  of security rationale. Does not cover multi-repo docs automation, AGENTS.md
  maintenance (covered elsewhere in the corpus), doc-quality metrics, or how to
  customize the drift-detection prompt beyond the shipped default.

## Extracted Claims

### Claim 1: Documentation automation with gh-aw is defined as running an agent on a schedule or after code changes to detect doc/code drift, prepare updates, and propose them as a pull request
- **Evidence**: This is the page's opening definitional sentence, framing the
  whole guide.
- **Confidence**: settled (first-party definitional statement)
- **Quote**: "Documentation automation with gh-aw means running an agent on a
  schedule or after code changes so it can detect drift between code and docs,
  prepare updates, and propose them as a pull request."
- **Our assessment**: This is a narrow, specific instance of the broader
  "Continuous AI" framing in `docs-ghaw-how-they-work.md` Claim 8 (documentation
  currency is named as one of four canonical Continuous AI categories there).
  This guide operationalizes that category into one shippable workflow. For
  Ch02/Ch09: cite this as the canonical minimal-viable docs-drift workflow when
  a team wants the simplest possible starting point rather than the full DailyOps
  phased pattern.

### Claim 2: The starter workflow is installed with a single wizard command, `gh aw add-wizard githubnext/agentics/docs-updater`, rather than authored from scratch
- **Evidence**: Directly stated install instruction on the page, paired with the
  resulting file path `.github/workflows/docs-updater.md`.
- **Confidence**: settled (first-party install instruction)
- **Quote**: "Install the starter with `gh aw add-wizard githubnext/agentics/docs-updater`."
- **Our assessment**: This confirms the `agentics` catalog (referenced elsewhere
  in the corpus, e.g. `daily-doc-updater.md` in `docs-ghaw-dailyops.md` Claim 7)
  contains a `docs-updater` entry installable via `add-wizard`, distinct from
  the `daily-` prefixed DailyOps catalog entries — see Cross-References below
  for the naming/cadence discrepancy this surfaces.

### Claim 3: The docs-updater starter workflow runs weekly, not on the daily weekday cadence that is the stated DailyOps convention
- **Evidence**: The shipped frontmatter sets `on: schedule: weekly` with no
  `workflow_dispatch` trigger shown.
- **Confidence**: settled (first-party YAML, directly quoted)
- **Quote**:
  ```yaml
  on:
    schedule: weekly
  ```
- **Our assessment**: `docs-ghaw-dailyops.md` Claim 2 documents `cron: "0 2 * * 1-5"`
  (weekday-only, daily) as "the standard DailyOps scheduling convention" and
  lists a `daily-doc-updater.md` reference implementation (Claim 7) alongside
  other daily-cadence workflows. This guide's `docs-updater` starter — for what
  looks like the same use case (keeping docs in sync with code) — instead
  defaults to a weekly cadence with no manual-dispatch trigger. This reads as a
  conditioning-variable difference rather than a true contradiction: documentation
  drift accumulates more slowly than code-quality or test-coverage drift, so a
  weekly cadence is plausibly the right choice for *this* narrower starter even
  though daily is the stated DailyOps default. We did not file a contradiction
  issue for this (see Cross-References) but flag it because a reader skimming
  both pages could reasonably expect the same cadence and be surprised it differs.
  For Ch02: when documenting DailyOps cadence, note that documentation-specific
  variants may reasonably deviate from the daily-weekday default.

### Claim 4: The workflow's `permissions` block grants only `contents: read` and `pull-requests: read` — no write permissions of any kind, even though the workflow ultimately opens a pull request
- **Evidence**: Frontmatter block shown in full on the page.
- **Confidence**: settled (first-party YAML)
- **Quote**:
  ```yaml
  permissions:
    contents: read
    pull-requests: read
  ```
- **Our assessment**: This is a clean, concrete confirmation of the
  no-write-access-by-default model documented abstractly in
  `docs-ghaw-how-they-work.md` Claim 4 ("Workflows run with minimal permissions —
  no write access by default"). The PR itself is created entirely through the
  separate `safe-outputs` elevated-permission path (Claim 5, below), not through
  the workflow's own token. For Ch02/Ch03: use this exact permissions block as a
  minimal worked example of "read-only agent, writes only via Safe Outputs" —
  it's shorter and easier to reason about than the multi-token cross-repo
  examples elsewhere in the corpus (e.g. `docs-ghaw-central-repo-ops.md`).

### Claim 5: The `safe-outputs.create-pull-request` block pins the output to a single fixed branch name (`docs/automation`), a fixed title prefix (`"[docs] "`), and draft status — three settings working together to keep repeated runs from spawning duplicate or unreviewable PRs
- **Evidence**: Frontmatter block shown in full on the page.
- **Confidence**: settled (first-party YAML)
- **Quote**:
  ```yaml
  safe-outputs:
    create-pull-request:
      branch: docs/automation
      title-prefix: "[docs] "
      draft: true
  ```
- **Our assessment**: The fixed `branch: docs/automation` (rather than a
  per-run-unique branch name) is a dedup mechanism we have not seen documented
  elsewhere in the corpus — other examples (e.g. `docs-ghaw-central-repo-ops.md`,
  which shows `create-pull-request: { target-repo, title-prefix, max: 1 }`) rely
  on the `max:` field to cap open PRs, not on a static branch name. A fixed
  branch name achieves a similar "at most one open docs-automation PR" outcome
  implicitly: a second run before the first PR merges would push to the same
  branch and update the existing PR rather than opening a new one. The
  `title-prefix: "[docs] "` pattern directly corroborates
  `docs-ghaw-dependabot-rollout.md` Claim 7 (`title-prefix: '[dependabot] '`
  "for easy filtering" of agent-created PRs), and `draft: true` corroborates the
  same field shown in `docs-ghaw-ephemerals.md`'s pull-request-expiration
  example. For Ch02: document the fixed-branch-name pattern as an alternative
  (simpler, but coarser) dedup mechanism to `max:`, worth calling out precisely
  because it isn't the `max:`-based approach seen elsewhere in the corpus.

### Claim 6: The workflow's natural-language instructions scope the drift review to a fixed seven-day lookback window and name three specific drift symptoms to check for
- **Evidence**: Markdown body of the shipped workflow file.
- **Confidence**: settled (first-party workflow prompt, quoted directly)
- **Quote**: "Review code and documentation changes from the last seven days.
  Identify outdated setup steps, missing option descriptions, and examples that
  no longer match current behavior. Update the relevant documentation files and
  open a draft pull request describing the changes and any areas that still
  require human review."
- **Our assessment**: The seven-day window matches the workflow's own weekly
  schedule (each run reviews exactly the window since the last run, no gaps and
  no overlap). The three named drift symptoms — outdated setup steps, missing
  option descriptions, stale examples — are a concrete, reusable checklist for
  what "documentation drift" means operationally, more specific than the generic
  "keeps documentation synchronized with merged code changes" description in
  `docs-ghaw-dailyops.md` Claim 7. For Ch09: use this three-item checklist
  verbatim as a starting prompt template for doc-drift-detection workflows.

### Claim 7: `create-pull-request` is framed as a security-relevant choice specifically because it prevents the agent from pushing directly to the default branch, routing all proposed changes through gh-aw's PR-creation validation and human review
- **Evidence**: Explicit security-rationale paragraph on the page, the only
  prose on the page not describing the YAML or the install command.
- **Confidence**: settled (first-party security rationale, directly quoted)
- **Quote**: "`create-pull-request` matters for security because the agent does
  not push directly to the default branch. gh-aw validates the proposed changes
  and opens a pull request for human review, which keeps documentation updates
  reviewable before merge."
- **Our assessment**: This restates, in a docs-specific frame, the general
  Safe Outputs permission-separation argument in `docs-ghaw-how-they-work.md`
  Claim 5 ("Safe Outputs are pre-approved GitHub operations the AI can request
  without write permissions"). Notable here is that the guide states the
  security property as the *primary* justification for the pattern, ahead of
  convenience or review-workflow ergonomics — for a documentation-specific
  guide, that's a deliberate signal that even "just docs" changes are treated
  as untrusted agent output requiring the same review gate as code changes.
  For Ch03: cite this as a plain-language explanation of why Safe Outputs matter
  even for low-risk-seeming content like documentation.

## Concrete Artifacts

```yaml
# .github/workflows/docs-updater.md frontmatter
# Source: gh-aw "Docs Automation" guide
---
on:
  schedule: weekly
permissions:
  contents: read
  pull-requests: read
safe-outputs:
  create-pull-request:
    branch: docs/automation
    title-prefix: "[docs] "
    draft: true
---
# Documentation Updater

Review code and documentation changes from the last seven days.
Identify outdated setup steps, missing option descriptions, and examples that
no longer match current behavior. Update the relevant documentation files and
open a draft pull request describing the changes and any areas that still
require human review.
```

```
# Install command
# Source: gh-aw "Docs Automation" guide
gh aw add-wizard githubnext/agentics/docs-updater
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 4 (no write access by default) and
    Claim 5 (Safe Outputs as permission-separated pre-approved operations) —
    this workflow's `contents: read` / `pull-requests: read` permissions block
    plus `create-pull-request` safe output is a concrete, minimal worked
    example of both claims together.
  - `docs-ghaw-dependabot-rollout.md` Claim 7 (`title-prefix` for filtering
    agent-created PRs) — the `"[docs] "` prefix here is the same pattern
    applied to a different use case.
  - `docs-ghaw-ephemerals.md` (pull-request expiration example, `draft: true`
    on `create-pull-request`) — corroborates `draft: true` as a recurring
    default for agent-opened PRs across use cases.
- **Contradicts**: None filed as a formal contradiction issue. See Claim 3 for
  a cadence discrepancy (`docs-updater` runs weekly; `docs-ghaw-dailyops.md`
  Claim 2 states weekday-daily cron is "the standard DailyOps scheduling
  convention," and Claim 7 lists a same-purpose `daily-doc-updater.md`
  reference implementation). We judged this a conditioning-variable difference
  (docs drift more slowly than code, so weekly cadence is defensible for this
  narrower starter) rather than a genuine contradiction requiring adjudication,
  per the MINER.md guidance that differences explainable by context/use-case
  aren't contradictions. Worth a second look if a future source clarifies
  whether `docs-updater` and `daily-doc-updater.md` are the same underlying
  workflow under two names, or two genuinely distinct catalog entries.
- **Extends**: `docs-ghaw-dailyops.md` Claim 7, which names `daily-doc-updater.md`
  as a DailyOps reference implementation but gives no configuration detail
  beyond "keeps documentation synchronized with merged code changes." This
  source supplies the first full worked configuration (permissions, safe-outputs
  block, prompt text) we have in the corpus for a documentation-drift workflow,
  and it is a noticeably lighter-weight pattern than the full three-stage
  Research/Configuration/Execution DailyOps approach with GitHub Discussions
  tracking (`docs-ghaw-dailyops.md` Claims 3-4) — no discussion-based tracking
  appears anywhere on this page.
- **Novel**: The fixed-branch-name (`branch: docs/automation`) dedup pattern
  for `create-pull-request` is new to the corpus; every other `create-pull-request`
  example we have documented uses `max:` (or `target-repo` fan-out) rather than a
  static branch name to bound duplicate PRs.

## Guide Impact

- **Ch02 (Harness Engineering)**: Add this exact YAML block as the minimal
  "docs-drift starter" example — it's the shortest complete Safe-Outputs-gated
  workflow in the corpus (5 lines of permissions/safe-outputs config) and pairs
  well with the fuller DailyOps pattern already cited for readers who want more
  structure. Note the fixed-branch-name dedup approach as a simpler alternative
  to `max:` when only one style of PR (docs updates) is ever produced by a
  workflow.
- **Ch09 (or wherever documentation-maintenance workflows are covered)**: Use
  the three-item drift checklist (outdated setup steps, missing option
  descriptions, stale examples) and the seven-day-lookback-matches-weekly-cadence
  design as a concrete template, and flag the cadence discrepancy with the
  DailyOps daily-weekday convention so readers don't assume one cadence fits
  all DailyOps-style workflows.
- **Ch03 (Safe Outputs / permission model)**: Cite the page's explicit security
  rationale ("the agent does not push directly to the default branch") as a
  plain-language justification readers can quote back to skeptical stakeholders
  who think documentation changes are low-risk enough to skip PR review.

## Extraction Notes

- The source page itself is very short: one definitional paragraph, one install
  command, one YAML/markdown workflow example, one security-rationale paragraph,
  and a "Related pages" list. There is no additional content behind tabs,
  accordions, or pagination — I fetched the rendered HTML directly (the guide
  is a static docs site) and confirmed the extracted text above is the complete
  page body.
- The page's "Related pages" list points to generic, already-covered ground:
  the Claude Code engine integration guide, the GitHub Copilot agent integration
  guide, the Safe Outputs reference, and the Quick Start guide. None of these
  are specific to documentation automation — they're the same generic
  engine-setup and Safe-Outputs material already documented elsewhere in the
  corpus (e.g. `docs-ghaw-how-they-work.md`, `docs-ghaw-safe-outputs-specification.md`).
  I did not do a full deep-read of those four linked pages since they are
  general infrastructure pages, not incremental to the docs-automation-specific
  question this issue asks about; a future miner revisiting engine-integration
  or Safe-Outputs topics directly should read them fresh rather than relying on
  this note.
- Because the source is this thin, several claims above lean on
  cross-referencing existing corpus notes for the deeper "why it matters"
  analysis rather than on additional material from the source itself — flagging
  this so the Assayer can judge whether that's sufficient depth for a page this
  short (I believe it is, given there simply isn't more primary content to mine).
