---
source_url: https://github.github.com/gh-aw/gallery/multi-repo/feature-sync
source_type: docs
title: "GitHub Agentic Workflows Gallery: Feature Synchronization"
author: GitHub Agentic Workflows team (official documentation)
date_published: null
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: emerging
issue: "#3064"
---

# GitHub Agentic Workflows Gallery: Feature Synchronization

> Four worked YAML implementations of upstream-to-downstream repository
> synchronization — basic push-triggered sync, multi-target dispatch,
> release-triggered version upgrades, and bidirectional sync with
> conflict detection — filling in the concrete implementation the
> abstract "upstream-to-downstream" topology in
> `docs-ghaw-multi-repo-ops.md` left undemonstrated.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows "Gallery" section — worked
  implementations of design patterns, one level more concrete than the
  `examples/` section pages; distinct from the `patterns/` reference pages
  which document abstract design primitives.)
- **Author credibility**: GitHub Agentic Workflows team — same team behind
  the `gh aw` CLI and the patterns/examples pages already in this corpus
  (`docs-ghaw-multi-repo-ops.md`, `docs-ghaw-central-repo-ops.md`,
  `docs-ghaw-multi-repo-issue-tracking.md`). YAML configurations are
  first-party examples demonstrating supported platform behavior. Claims
  about configuration schemas and field semantics are authoritative for the
  gh-aw platform.
- **Scope**: Four workflow patterns for propagating file/config changes from
  one repository to one or more downstream repositories using
  `create-pull-request` with `target-repo`, triggered by `push` (path-filtered)
  or `release` events. Covers PAT vs. GitHub App authentication for this use
  case. Does NOT cover: the abstract MultiRepoOps topology taxonomy (see
  `docs-ghaw-multi-repo-ops.md`), issue-tracking use cases (see
  `docs-ghaw-multi-repo-issue-tracking.md`), or the checkout+rsync-based
  "Deterministic Feature Sync" artifact shown in
  `docs-ghaw-multi-repo-ops.md`'s Concrete Artifacts (a different,
  non-safe-output implementation of file sync — see Extraction Notes).

## Extracted Claims

### Claim 1: Basic feature sync propagates changes to a single downstream repo using a path-filtered `push` trigger and `create-pull-request` with `target-repo`, opened as a draft with a fixed reviewer
- **Evidence**: Complete YAML configuration reproduced in Concrete Artifacts.
  Trigger is `on: push: branches: [main]: paths: ['shared/**']`; safe output is
  `create-pull-request: target-repo: "myorg/downstream-service"` with
  `title-prefix: "[sync] "`, `labels: [auto-sync, upstream-update]`,
  `reviewers: [team-lead]`, `draft: true`.
- **Confidence**: settled (first-party YAML example with explicit fields)
- **Quote**: (no direct quote; see paraphrase in Our assessment — quote fields
  are drawn from the reproduced YAML block in Concrete Artifacts, not prose)
- **Our assessment**: This is the concrete implementation of the
  "upstream-to-downstream" topology named abstractly in
  `docs-ghaw-multi-repo-ops.md` Claim 5 ("Main repo propagates changes using
  `create-pull-request` with `target-repo` per downstream"). The `draft: true`
  default is notable — the PR is opened but not marked ready for review,
  requiring a human to promote it. Combined with a named `reviewers` entry,
  this is a conservative default posture for a pattern that writes changes
  into a repository the workflow's own team may not fully control. For Ch06
  (Orchestration): use this as the first concrete YAML template when
  documenting the upstream-to-downstream topology.

### Claim 2: Feature sync workflows narrow their trigger scope with `paths` filters so only specific file trees (e.g. a shared library directory) initiate a sync run, rather than every push to `main`
- **Evidence**: Basic sync filters on `paths: ['shared/**']`; Multi-Target
  sync filters on `paths: ['core/**']`; Bidirectional sync filters on
  `paths: ['shared-config/**']`. All three push-triggered patterns use a
  distinct, narrow path filter matched to their specific propagation scope.
- **Confidence**: settled (directly observable across three reproduced YAML
  configurations)
- **Quote**: (no direct quote; pattern observed across YAML blocks — see
  Concrete Artifacts)
- **Our assessment**: Path filtering is the mechanism that keeps sync workflows
  incremental and targeted rather than re-triggering on unrelated repo
  activity (e.g., a docs-only commit to `main` should not fire a sync run).
  This is a cheap, GitHub Actions-native control — no agent logic required —
  that bounds how often the (costlier) agent-driven sync step runs. For Ch02
  (Harness Engineering): recommend `paths` filters as the default cost and
  noise control for any push-triggered cross-repo sync workflow.

### Claim 3: Multi-target dispatch fans a single upstream change out to several named downstream repositories in one workflow run, bounded by `create-pull-request: max: 3`, with the target repos identified in the agent prompt rather than fixed in a `target-repo` field
- **Evidence**: The Multi-Target Sync YAML sets `create-pull-request: max: 3`
  with no `target-repo` key in the safe-outputs block; the markdown body
  instructs the agent: "create PRs in dependent services
  (`myorg/api-service`, `myorg/web-frontend`, `myorg/mobile-backend`)."
- **Confidence**: emerging (the absence of a fixed `target-repo` field is
  confirmed in the reproduced YAML, but the mechanism by which the agent's
  prompt-named repos become actual `target-repo` values per created PR is not
  spelled out on the page — see Extraction Notes)
- **Quote**: "create PRs in dependent services (`myorg/api-service`,
  `myorg/web-frontend`, `myorg/mobile-backend`)"
- **Our assessment**: This is architecturally the same "agent-determined
  target" pattern already documented in
  `docs-ghaw-multi-repo-issue-tracking.md` Claim 6 (automated triage/routing,
  where `create-issue` omits a fixed `target-repo` and the agent picks the
  tracker from a fixed set of candidates named in the prompt). Multi-target
  feature sync applies the same "list candidates in the prompt, bound the
  count with `max`" shape to `create-pull-request` instead of `create-issue`.
  The `max: 3` here does double duty: it matches the exact number of
  candidate repos named in the prompt, so it functions as both a safety cap
  and (incidentally) an exact quota. For Ch06: document this as the
  "agent-selected multi-target" variant of upstream-to-downstream, distinct
  from the fixed single-`target-repo` basic pattern (Claim 1).

### Claim 4: Release-based sync fires on `release: types: [published]` and opens a non-draft PR with an assigned human reviewer, in contrast to the draft-by-default posture of the push-triggered patterns
- **Evidence**: Complete YAML reproduced in Concrete Artifacts:
  `on: release: types: [published]`, `create-pull-request: target-repo:
  "myorg/production-service"`, `title-prefix: "[upgrade] "`,
  `labels: [version-upgrade, auto-generated]`, `reviewers: [release-manager]`,
  `draft: false`.
- **Confidence**: settled (first-party YAML example with explicit
  `draft: false`, contrasting directly with `draft: true` in the other three
  patterns)
- **Quote**: (no direct quote; field values drawn from the reproduced YAML
  block in Concrete Artifacts)
- **Our assessment**: The `draft: false` choice is the one deliberate
  deviation from the otherwise-consistent "open as draft" posture across the
  gallery's four patterns. A published release is a discrete, well-defined
  trigger with an unambiguous payload (the release notes), which likely
  explains the platform team's confidence in opening a ready-for-review PR
  directly rather than a draft — this mirrors the "unambiguous success
  criteria" argument already made for release automation in
  `blog-gh-aw-operations-release-workflows.md` Claim 2. For Ch03 (Safety and
  Verification): note `draft` as a per-pattern trust dial — push-triggered
  sync (higher trigger frequency, more implicit judgment about what changed)
  defaults to draft; release-triggered sync (rarer, well-defined trigger)
  defaults to non-draft with a named reviewer.

### Claim 5: Bidirectional sync adds a conflict-detection step — comparing timestamps and change history on both sides before choosing between an automatic merge or a manual-review draft PR
- **Evidence**: The Bidirectional Sync workflow body instructs the agent:
  "Compare timestamps and change history; if conflicts are detected, create a
  PR marked for manual review with conflict notes. If no conflict, apply
  changes automatically and record sync timestamp." The YAML adds the
  `pull_requests` toolset (`tools: github: toolsets: [repos, pull_requests]`)
  alongside `repos`, not present in the other three patterns.
- **Confidence**: emerging (the decision logic is stated as an agent
  instruction in the prompt body, not as a deterministic platform-enforced
  rule; the page does not specify exactly what counts as a "conflict" beyond
  "compare timestamps and change history")
- **Quote**: "Compare timestamps and change history; if conflicts are
  detected, create a PR marked for manual review with conflict notes. If no
  conflict, apply changes automatically and record sync timestamp."
- **Our assessment**: This is the one pattern in the gallery where the agent
  is trusted with a branching safety decision (auto-sync vs. escalate to
  human) rather than always producing a PR for human review. The trust boundary
  is still bounded by the safe-output surface — "apply changes automatically"
  still routes through `create-pull-request`, since the workflow has no
  direct-push safe output configured; there's no YAML evidence that a
  detected "no-conflict" case bypasses PR creation. But the page's language
  ("apply changes automatically") is ambiguous about whether an automatic
  merge is actually performed by the agent, or whether it means a PR is
  still opened but without the manual-review label. Because this ambiguity
  is not resolved on the page, we flag it as a config detail practitioners
  must verify before relying on it in production. For Ch03: document this as
  an example of an agent-driven safety branch, and flag the "automatic"
  outcome as one to verify against actual `gh aw` behavior before trusting the
  no-review path.

### Claim 6: The additional `pull_requests` GitHub toolset entry in bidirectional sync implies the agent needs to read existing PR state (not just repo contents) to detect conflicts across the two repositories
- **Evidence**: Bidirectional Sync is the only one of the four patterns whose
  `tools.github.toolsets` list includes `pull_requests` in addition to
  `repos`; the other three patterns list `toolsets: [repos]` only.
- **Confidence**: emerging (inferred from the toolset diff across the four
  reproduced YAML blocks; the page does not explain why this toolset is
  needed)
- **Quote**: (no direct quote; toolset list difference observed directly in
  the reproduced YAML — see Concrete Artifacts)
- **Our assessment**: Conflict detection based on "change history" plausibly
  requires checking whether an existing sync PR is already open (to avoid
  duplicate PRs) or what the last sync PR changed, which needs `pull_requests`
  read access beyond plain repo contents. This is a small but concrete signal
  that "conflict detection" here is implemented at least partly via GitHub
  API state (existing PRs), not purely via file-content diffing. For Ch02:
  when documenting toolset selection for cross-repo sync workflows, note that
  conflict-aware variants need `pull_requests` in addition to `repos`.

### Claim 7: All four feature-sync patterns pair `tools.github.toolsets: [repos]` with `tools.edit.bash: ["git:*"]`, combining deterministic git operations with agent-driven analysis inside the same workflow
- **Evidence**: Every one of the four reproduced YAML configurations includes
  identical `tools:` blocks granting both the GitHub `repos` toolset and
  unrestricted `git:*` bash access under `edit`.
- **Confidence**: settled (directly observable and consistent across all four
  reproduced YAML blocks)
- **Quote**: (no direct quote; field observed identically across all four
  YAML blocks — see Concrete Artifacts)
- **Our assessment**: This is a hybrid design: the agent can both query
  GitHub state via the `repos` toolset (e.g., compare file contents, check
  release metadata) and run arbitrary `git` commands directly (diff, log, blame)
  to determine what changed and how to adapt it for the target repo, while
  the actual repo-write side effect (the PR) is still delivered exclusively
  through the `create-pull-request` safe output. `git:*` bash access is scoped
  to read/inspect operations in practice here (there is no evidence of `git push`
  in any prompt body — writes go through the PR safe output), but the tool
  grant itself is unrestricted at the YAML level. For Ch03: flag `bash: ["git:*"]`
  as a broad grant that should be paired with a review of what the agent
  prompt actually instructs it to do with git, since the YAML alone does not
  constrain git subcommands.

### Claim 8: The documented PAT scope for feature-sync workflows (`repo`, `contents: write`, `pull-requests: write`) is broader than the least-privilege guidance for cross-repo PATs documented elsewhere in the corpus
- **Evidence**: The Authentication section states: "Create a PAT with `repo`,
  `contents: write`, and `pull-requests: write` permissions, then store it as
  a repository secret." No source-repo/target-repo scope distinction is drawn.
- **Confidence**: settled (first-party authentication guidance, directly
  quoted)
- **Quote**: "Create a PAT with `repo`, `contents: write`, and
  `pull-requests: write` permissions, then store it as a repository secret"
- **Our assessment**: This repeats the same gap already flagged in
  `docs-ghaw-multi-repo-issue-tracking.md` Claim 10: the gallery/examples-tier
  pages show a single broad PAT scope for working configurations, while
  `docs-ghaw-multi-repo-ops.md` Claim 7 gives the security-hardened guidance
  (read-only on the source repo, write-only on target repos). This is not a
  new contradiction — it is the same known gap recurring in a third worked
  example, which strengthens rather than weakens the case that the
  patterns-tier least-privilege guidance should be the one the guide
  recommends for production, with gallery/examples pages flagged as
  "minimal-effort, not hardened" starting points. For Ch03: cross-reference
  `docs-ghaw-multi-repo-ops.md` Claim 7 whenever citing this page's auth
  section.

### Claim 9: The page frames feature sync as a "monorepo alternative" for teams maintaining related projects across separate repositories
- **Evidence**: The "When to Use" section lists "maintaining related projects
  in separate repositories (monorepo alternative)" as the first use case,
  alongside propagating library updates, updating platform-specific repos
  after core changes, and keeping downstream forks synchronized with upstream.
- **Confidence**: anecdotal (framing/positioning language from the platform
  team, not a benchmarked comparison against actual monorepo tooling)
- **Quote**: "Use feature sync when maintaining related projects in separate
  repositories (monorepo alternative)"
- **Our assessment**: This framing is a positioning claim, not a technical
  one — the page does not compare feature-sync workflows against monorepo
  tooling (e.g., shared build graphs, atomic cross-package commits) on any
  concrete dimension (latency, consistency guarantees, tooling cost). Treat
  as a marketing framing for why the pattern exists, not as evidence that
  agentic feature-sync is a drop-in substitute for monorepo tooling. For Ch06:
  if citing this page's motivation, note the comparison is asserted, not
  demonstrated.

## Concrete Artifacts

### Basic Feature Sync

Reconstructed from two independent WebFetch passes over the source page;
consistent across both. Source: gh-aw gallery, "Feature Synchronization —
Basic Feature Sync" section.

```yaml
---
on:
  push:
    branches: [main]
    paths:
      - 'shared/**'
permissions:
  contents: read
  actions: read
tools:
  github:
    toolsets: [repos]
  edit:
    bash:
      - "git:*"
safe-outputs:
  github-token: ${{ secrets.GH_AW_CROSS_REPO_PAT }}
  create-pull-request:
    target-repo: "myorg/downstream-service"
    title-prefix: "[sync] "
    labels: [auto-sync, upstream-update]
    reviewers: [team-lead]
    draft: true
---
```

### Multi-Target Sync

Source: gh-aw gallery, "Feature Synchronization — Multi-Target Sync" section.

```yaml
---
on:
  push:
    branches: [main]
    paths:
      - 'core/**'
permissions:
  contents: read
  actions: read
tools:
  github:
    toolsets: [repos]
  edit:
    bash:
      - "git:*"
safe-outputs:
  github-token: ${{ secrets.GH_AW_CROSS_REPO_PAT }}
  create-pull-request:
    max: 3
    title-prefix: "[core-sync] "
    labels: [automated-sync]
    draft: true
---
```

Prompt body (paraphrased by the fetch tool, presented here as reported, not
as a verbatim quote — see Extraction Notes): when core library files change,
create PRs in dependent services (`myorg/api-service`, `myorg/web-frontend`,
`myorg/mobile-backend`); for each target, check if they use the changed
modules, adapt imports/paths, and create a PR with compatibility notes and
links to source commits.

### Release-Based Sync

Source: gh-aw gallery, "Feature Synchronization — Release-Based Sync"
section.

```yaml
---
on:
  release:
    types: [published]

permissions:
  contents: read
  actions: read

tools:
  github:
    toolsets: [repos]
  edit:
    bash:
      - "git:*"

safe-outputs:
  github-token: ${{ secrets.GH_AW_CROSS_REPO_PAT }}
  create-pull-request:
    target-repo: "myorg/production-service"
    title-prefix: "[upgrade] "
    labels: [version-upgrade, auto-generated]
    reviewers: [release-manager]
    draft: false
---
```

### Bidirectional Sync with Conflict Detection

Source: gh-aw gallery, "Feature Synchronization — Bidirectional Sync"
section.

```yaml
---
on:
  push:
    branches: [main]
    paths:
      - 'shared-config/**'
permissions:
  contents: read
  actions: read
tools:
  github:
    toolsets: [repos, pull_requests]
  edit:
    bash:
      - "git:*"
safe-outputs:
  github-token: ${{ secrets.GH_AW_CROSS_REPO_PAT }}
  create-pull-request:
    target-repo: "myorg/sister-project"
    title-prefix: "[config-sync] "
    labels: [config-update, needs-review]
    draft: true
---
# Bidirectional Config Sync

Synchronize shared configuration between this project and
`myorg/sister-project`, which may be modified independently. Compare
timestamps and change history; if conflicts are detected, create a PR
marked for manual review with conflict notes. If no conflict, apply changes
automatically and record sync timestamp.
```

### Authentication Section (verbatim fragments)

From the page's Authentication section.

```
PAT: "Create a PAT with `repo`, `contents: write`, and `pull-requests: write`
permissions, then store it as a repository secret"

GitHub App: "For enhanced security, use GitHub App installation tokens."
```

*Source: gh-aw gallery, "Feature Synchronization" — Authentication section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-multi-repo-ops.md` Claim 5 (upstream-to-downstream topology:
    "Main repo propagates changes using `create-pull-request` with
    `target-repo` per downstream"): Claims 1 and 4 above are the concrete
    worked implementations of exactly this topology — basic and
    release-triggered sync both use `create-pull-request` + `target-repo`
    from the main/upstream repo out to a named downstream repo.
  - `docs-ghaw-multi-repo-ops.md` Claim 8 (GitHub App Installation Tokens
    preferred over PATs): Claim 8 above's Authentication section echoes this
    preference verbatim ("For enhanced security, use GitHub App installation
    tokens.").
  - `docs-ghaw-multi-repo-issue-tracking.md` Claim 6 (automated triage/routing
    omits a fixed `target-repo`, letting the agent pick the destination from
    candidates named in the prompt) and Claim 10 (PAT scope in
    examples/gallery pages is broader than the patterns-page least-privilege
    guidance): Claim 3 above shows the same agent-determined-target shape
    applied to `create-pull-request`; Claim 8 above shows the same PAT-scope
    gap recurring in a third source.
  - `docs-ghaw-central-repo-ops.md` Claim 2 (`max` as the documented
    blast-radius control for fan-out): Claim 3 above's `max: 3` on
    multi-target `create-pull-request` is the same bounded-fan-out primitive
    applied to feature sync instead of `dispatch-workflow`.
  - `docs-ghaw-safe-outputs-specification.md` Claim 6 (max limit violation
    triggers all-or-nothing rejection of every operation of that type, not
    just the excess): relevant to Claim 3 above — if the agent in Multi-Target
    Sync ever tried to create more than 3 PRs (e.g., a fourth dependent service
    is later added to the prompt without raising `max`), the platform-level
    behavior would reject all PR creations for that run, not just the fourth.
    This page does not state that consequence itself; it follows from the
    normative behavior documented in the cited note.
  - `blog-gh-aw-operations-release-workflows.md` Claim 2 (release automation
    works well because it has unambiguous success criteria): Claim 4 above's
    `draft: false` choice for release-triggered sync is consistent with this
    — a well-defined trigger (published release) supports more automation
    confidence than an open-ended push trigger.

- **Contradicts**: None identified as a genuine, guide-relevant contradiction.
  The broader PAT scope in Claim 8 above repeats — rather than newly
  conflicts with — the gap already surfaced in
  `docs-ghaw-multi-repo-issue-tracking.md` Claim 10 (examples/gallery pages
  show minimal-effort scope; patterns pages show hardened scope). Per
  MINER.md §4a, this is a conditioning-variable difference (which tier of
  documentation you're reading), not a case where two sources assert
  incompatible guide advice — no contradiction issue filed.

  One internal ambiguity worth flagging rather than filing as a
  contradiction: Claim 5 above notes the bidirectional-sync prompt says
  "apply changes automatically" for the no-conflict case, but the workflow's
  only configured write path is `create-pull-request` (there is no direct-push
  safe output in the YAML). This reads as loose language on the source page
  rather than a substantive disagreement between two claims or sources, so it
  is flagged in Claim 5's assessment and in Extraction Notes rather than
  filed as a contradiction issue.

- **Extends**:
  - `docs-ghaw-multi-repo-ops.md`: that note names the upstream-to-downstream
    topology abstractly (one line in a patterns table). This page provides
    four concrete, differentiated implementations — basic, multi-target,
    release-triggered, and bidirectional-with-conflict-detection — none of
    which existed as worked YAML anywhere in the corpus before this note.
  - `docs-ghaw-multi-repo-issue-tracking.md`: that note's agent-determined
    routing pattern (Claim 6) is shown here recurring for a different safe
    output type (`create-pull-request` instead of `create-issue`), suggesting
    "name candidates in the prompt, omit fixed `target-repo`, bound with `max`"
    is a general gh-aw idiom rather than one specific to issue triage.
  - `docs-ghaw-central-repo-ops.md`: that note's `max` fan-out control
    (Claim 2) for `dispatch-workflow` is shown here applied to
    `create-pull-request` directly, without an orchestrator/worker split —
    a lighter-weight fan-out mechanism for cases that don't need the full
    CentralRepoOps architecture.

- **Novel**:
  - **Conflict detection via timestamp/change-history comparison before
    choosing automated sync vs. manual-review PR** (Claim 5): not documented
    anywhere else in the corpus. The closest existing pattern
    (`docs-ghaw-central-repo-ops.md` Claim 10, conflict detection before
    overwriting) always escalates to an issue on conflict; this page is the
    first to describe an agent choosing between two different write
    behaviors (auto-sync vs. draft-for-review) based on a detected condition.
  - **`draft` field varying by trigger type as a trust signal** (Claim 4):
    not previously discussed in the corpus as a deliberate per-workflow
    safety dial.
  - **`tools.github.toolsets` diff (`pull_requests` added only for the
    conflict-detecting variant)** (Claim 6): a small but concrete signal, new
    to the corpus, that toolset grants should track what the agent's specific
    decision logic needs to read.
  - **Release event (`release: types: [published]`) as a feature-sync
    trigger**: no existing source note documents `release` as a trigger for
    cross-repo `create-pull-request` workflows; prior release-related
    coverage (`blog-gh-aw-operations-release-workflows.md`) is about
    generating a release inside one repo, not propagating a release's changes
    to other repos.

## Guide Impact

### Chapter 06: Orchestration and Multi-Agent Coordination

- **Add the four feature-sync variants as the worked template for the
  upstream-to-downstream topology** (Claims 1, 3, 4, 5): the guide currently
  names this topology in the abstract (per `docs-ghaw-multi-repo-ops.md`).
  This source gives copy-adaptable YAML for the common variants: fixed
  single-target (basic), agent-selected multi-target (bounded by `max`),
  release-triggered (non-draft, unambiguous trigger), and conflict-aware
  bidirectional.
- **Document the "name candidates in the prompt, bound with `max`" idiom as a
  general pattern**, not specific to issue routing (Claim 3): cross-reference
  `docs-ghaw-multi-repo-issue-tracking.md` Claim 6 as the first instance and
  this page's Multi-Target Sync as the second.

### Chapter 02: Harness Engineering

- **Recommend `paths` filters as the default noise/cost control for
  push-triggered cross-repo sync workflows** (Claim 2): a low-effort,
  platform-native control that should be the default recommendation whenever
  the guide documents a push-triggered sync pattern.
- **Note the toolset-follows-decision-logic principle**: `pull_requests`
  toolset access should be added only when the workflow's actual logic
  (e.g., conflict detection against existing PRs) requires it (Claim 6).

### Chapter 03: Safety and Verification

- **Add `draft` as a per-pattern trust dial, not a fixed default** (Claim 4):
  document the observed split (draft-by-default for push-triggered/ambiguous
  triggers, non-draft for well-defined triggers like a published release) as
  a design consideration, not a platform-enforced rule.
- **Flag `bash: ["git:*"]` as an unrestricted grant that needs prompt-level
  review** (Claim 7): the YAML alone permits any git subcommand; safety
  depends on what the prompt actually instructs, which the guide should call
  out as a verification step for reviewers of workflow YAML.
- **Reiterate the PAT least-privilege gap for a third time** (Claim 8):
  cross-reference `docs-ghaw-multi-repo-ops.md` Claim 7 whenever citing
  gallery/examples-tier auth guidance; the guide should state this gap once,
  prominently, rather than let it recur silently across chapters citing
  different gallery pages.
- **Flag the "apply changes automatically" ambiguity in bidirectional sync**
  (Claim 5) as a config detail to verify against actual `gh aw` runtime
  behavior before recommending the pattern for unattended production use.

## Extraction Notes

1. **This is a distinct page from the "Deterministic Feature Sync" artifact
   in `docs-ghaw-multi-repo-ops.md`**: that note's Concrete Artifacts section
   reproduces a YAML block titled "Deterministic Feature Sync" that uses
   `engine: id: claude` and `steps:` with `actions/checkout@v6` + `rsync` —
   a direct-checkout, non-safe-output implementation. The second triage
   comment on issue #3064 cited this artifact as "Claim 5" of
   `docs-ghaw-multi-repo-ops.md` and suggested this gallery page might be its
   worked example. Having read both pages, that citation does not hold up:
   `docs-ghaw-multi-repo-ops.md` Claim 5 is actually "Upstream-to-downstream
   is the topology where the main repository propagates changes... using
   `create-pull-request` with `target-repo` per downstream" (a numbered
   claim, matching this gallery page closely), and the "Deterministic Feature
   Sync" YAML is an unrelated, unnumbered artifact using direct git operations
   instead of safe outputs. This note cites the correct Claim 5 throughout
   Cross-References above. The first triage comment's assessment (this page
   is the worked example for the abstract upstream-to-downstream and
   multi-target patterns) is the one this extraction confirms; the second
   comment's low-novelty framing understated what this page actually
   contributes (the conflict-detection and multi-target-with-agent-selected-
   targets patterns are genuinely new to the corpus).

2. **WebFetch tool limitations on this page**: multiple WebFetch passes were
   needed. The tool (a small, fast model summarizing fetched HTML) initially
   returned prose summaries rather than verbatim YAML for some sections, and
   on one pass explicitly declined to reproduce the Release-Based Sync YAML
   "character-for-character" citing copyright, before doing so on a
   differently-worded follow-up request. The Basic Feature Sync and
   Bidirectional Sync YAML blocks were confirmed consistent across two
   independent fetches each; Multi-Target Sync and Release-Based Sync YAML
   were each obtained from a single fetch. Given this, and the absence of a
   way to view raw HTML/markdown source directly, confidence_overall for this
   note is set to `emerging` rather than `settled` — the YAML field values are
   very likely accurate (gh-aw YAML schemas are consistent with every other
   docs page in this corpus) but were not independently cross-checked against
   a second raw fetch for every block. The Multi-Target Sync prompt body is
   explicitly marked as fetch-tool paraphrase, not a verbatim quote, in
   Concrete Artifacts.

3. **No sub-pages followed**: the page's "Related Resources" links (MultiRepoOps
   Design Pattern, Cross-Repo Issue Tracking, Safe Outputs Reference, GitHub
   Tools documentation) all correspond to pages already mined in this corpus
   (`docs-ghaw-multi-repo-ops.md`, `docs-ghaw-multi-repo-issue-tracking.md`,
   `docs-ghaw-safe-outputs-specification.md`, `docs-ghaw-github-tools.md`) —
   confirmed by title match. No new sub-pages to follow.

4. **No publication date**: the page carries no explicit publication date.
   Content (safe-outputs schema, toolset names) is consistent with the
   gh-aw platform era already established by the three corroborating notes
   above.

5. **No contradiction issue filed**: per MINER.md §4a, the PAT-scope gap
   (Claim 8) is a recurrence of an already-identified conditioning-variable
   difference (examples/gallery tier vs. patterns tier), not a new material
   contradiction. The "apply changes automatically" ambiguity (Claim 5) is a
   loose-language question about one page's internal precision, not a
   disagreement between two claims or sources that would lead to different
   guide advice — flagged in-note rather than filed.
