---
source_url: https://github.github.com/gh-aw/examples/multi-repo/feature-sync
source_type: docs
title: "GitHub Agentic Workflows Examples: Multi-Repo Feature Synchronization"
author: GitHub Agentic Workflows team (official documentation)
date_published: null
date_extracted: 2026-05-22
last_checked: 2026-05-22
status: current
confidence_overall: emerging
issue: "#852"
---

# GitHub Agentic Workflows Examples: Multi-Repo Feature Synchronization

> Seven concrete workflow implementations of the upstream-to-downstream feature sync
> topology — demonstrating path-based change detection, multi-target PR fan-out,
> release-aligned sync, type-selective propagation, bidirectional conflict detection,
> feature-branch integration testing, and scheduled drift detection — extending the
> abstract MultiRepoOps `create-pull-request` + `target-repo` primitive from
> `docs-ghaw-multi-repo-ops.md` with worked examples for the feature-sync use case.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows "Examples" section — worked
  implementations of design patterns. Examples pages provide concrete configurations
  for specific use cases; distinct from the "Patterns" reference pages which document
  the abstract design primitives.)
- **Author credibility**: GitHub Agentic Workflows team — same team behind the Peli
  de Halleux "Agent Factory" blog series and the `gh aw` CLI. Workflow configurations
  are first-party examples demonstrating supported platform behavior. Claims about
  configuration schemas and field semantics are authoritative for the gh-aw platform.
- **Scope**: Seven workflow patterns for feature synchronization using
  `create-pull-request` safe outputs with `target-repo`. Covers push-based, release-based,
  branch-based, and scheduled sync triggers. Covers PAT and GitHub App authentication
  for cross-repo PR creation. Does NOT cover: the abstract MultiRepoOps design
  primitives (see `docs-ghaw-multi-repo-ops.md`), the issue-based cross-repo patterns
  (see `docs-ghaw-multi-repo-issue-tracking.md`), or the side-repo code quality
  monitoring use case (see `docs-ghaw-code-quality-monitoring.md`).

## Extracted Claims

### Claim 1: Feature sync is the upstream-to-downstream topology in practice — the main repository monitors specific paths and automatically creates pull requests in downstream repositories when those paths change

- **Evidence**: Page overview and "How It Works" section describe the core mechanism.
  Seven implementation patterns are provided — all following the same underlying
  topology: trigger on changes in main → create PR in target.
- **Confidence**: settled (first-party documentation; the upstream-to-downstream topology
  is explicitly demonstrated with seven concrete implementations)
- **Quote**: "Use feature sync when maintaining related projects in separate repositories
  (monorepo alternative), propagating library updates to dependent projects, updating
  platform-specific repos after core changes, or keeping downstream forks synchronized
  with upstream."
- **Our assessment**: This is `docs-ghaw-multi-repo-ops.md` Claim 5 (upstream-to-downstream:
  "Main repo propagates changes using `create-pull-request` with `target-repo` per
  downstream") made concrete with seven worked examples. The four use cases in the quote
  map to distinct configurations in the page: monorepo-alternative/library updates →
  Basic Feature Sync (Claim 2); core-changes → Multi-Target Sync (Claim 3);
  platform-specific repos → Selective File Sync (Claim 6); downstream forks →
  Release-Based Sync (Claim 4). For Ch06: these seven patterns are the operational
  vocabulary for upstream-to-downstream coordination.

### Claim 2: Basic feature sync triggers on `push` to `main` with a `paths:` filter and creates a PR in the downstream repository, adapting path structures and linking each PR back to the originating upstream commits

- **Evidence**: Page's "Basic Feature Sync" example. Trigger: `push` to `main`,
  `paths: shared/**`. Safe-outputs: `create-pull-request` with `target-repo`. Agent
  instructions include review of git diff, reading current target repo versions, path
  adaptation, and descriptive commit messages linking to original commits.
- **Confidence**: settled (first-party YAML example)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `paths:` filter is the key mechanism for scoping the trigger —
  only changes inside `shared/**` fire the workflow. Without `paths:`, every push to
  `main` would trigger a sync, including unrelated changes. The agent's responsibility
  to adapt paths and link back to original commits provides the audit trail the page
  describes as "maintaining complete audit trails." The PR-as-proposal model means
  downstream humans review and merge — the agent creates the change proposal, not the
  merge decision. For Ch06: document `paths:` filtering as the required trigger scoping
  mechanism for all push-based feature sync workflows.

### Claim 3: Multi-target sync uses `create-pull-request: max: 3` to fan out PRs simultaneously to up to three downstream repositories from a single push trigger, with the agent checking compatibility per target

- **Evidence**: Page's "Multi-Target Sync" example. Trigger: `push` to `main`,
  `paths: core/**`. Safe-outputs: `create-pull-request: max: 3`. Agent instructions
  include checking whether each target uses the changed modules, adapting imports/paths
  per target, and creating PRs with compatibility notes.
- **Confidence**: settled (first-party YAML example; `max:` behavior is documented
  in `docs-ghaw-multi-repo-ops.md`)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `max: 3` bound is the critical fan-out control — it caps
  how many downstream PRs can be created per workflow run. Teams with more than three
  downstream consumers must either raise `max:` or batch across multiple orchestration
  runs. The per-target compatibility check ("check if they use the changed modules")
  is a significant capability requirement: the agent must query each downstream repo's
  codebase to determine whether the change applies, not blindly propagate to all three.
  This is the multi-target case of `docs-ghaw-multi-repo-ops.md` Claim 5's
  `create-pull-request` + `target-repo` model, with the `max:` fan-out control from
  Claim 6 applied to PRs rather than issues. For Ch06: document `max:` on
  `create-pull-request` as the PR fan-out bound, analogous to `max:` on `create-issue`
  for issue fan-out.

### Claim 4: Release-based sync triggers on `release: [published]` rather than `push` — aligning downstream API updates, version-reference changes, and breaking-change adaptations with the upstream release cycle rather than individual commits

- **Evidence**: Page's "Release-Based Sync" example. Trigger: `release` event,
  `types: [published]`. Agent instructions include updating version references,
  applying API changes from release notes, and updating configuration for breaking
  changes.
- **Confidence**: settled (first-party YAML example)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The release trigger is the correct mechanism when downstream
  consumers should update on a release cadence, not on every commit. This avoids
  creating downstream PRs for intermediate commits that may be incomplete or unstable.
  The agent's use of release notes as input for identifying breaking changes is a
  significant distinction from commit-diff-based sync: the agent reads the release
  notes (structured documentation) rather than inferring intent from raw diffs. For
  Ch06: document release-based sync as the appropriate topology when downstream
  projects consume versioned releases rather than tracking a rolling main branch.

### Claim 5: Selective file sync uses file-type-specific `paths:` patterns (e.g., `types/**/*.ts`, `interfaces/**/*.ts`) to propagate only TypeScript definition files to downstream consumers, preserving client-specific extensions

- **Evidence**: Page's "Selective File Sync" example. Trigger: `push` to `main`,
  `paths: types/**/*.ts, interfaces/**/*.ts`. Agent instructions include identifying
  changed `.ts` files, updating them while preserving client-specific extensions,
  and validating no breaking changes.
- **Confidence**: settled (first-party YAML example)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The double-glob path pattern (`types/**/*.ts`) narrows the sync
  scope beyond directory-level filtering to specific file types. This is critical for
  shared-type-definition workflows where only interface contracts need propagating —
  not implementation files. The instruction to "preserve client-specific extensions"
  implies the agent must merge upstream type changes with downstream customizations
  rather than overwriting. This is a higher-capability requirement than basic file
  copy: the agent must perform a semantic merge. For Ch06: document selective file
  sync as the cross-repo type contract maintenance pattern; flag the merge-not-overwrite
  requirement as the key operational complexity.

### Claim 6: Bidirectional sync adds conflict detection via the `pull_requests` toolset — comparing timestamps and change history across both repos; detected conflicts produce PRs flagged for manual review rather than triggering automated merges

- **Evidence**: Page's "Bidirectional Sync with Conflict Detection" example. Trigger:
  `push` to `main`, `paths: shared-config/**`. Tools: `github` with `[repos,
  pull_requests]` toolsets. Agent instructions include comparing timestamps and
  change history; if conflicts are detected, creating a PR marked for manual review
  with conflict notes.
- **Confidence**: settled (first-party YAML example)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `pull_requests` toolset addition (compared to the single
  `repos` toolset in basic feature sync) is what enables conflict detection — the
  agent can query open/merged PRs in both repos to detect divergent changes. The
  "mark for manual review" outcome is significant: the workflow does not attempt
  automated conflict resolution, only detection and flagging. This is conservative
  and correct — automated conflict resolution in bidirectional sync is error-prone;
  surfacing conflicts to humans is the safer path. For Ch06: document bidirectional
  sync as a higher-complexity variant requiring the `pull_requests` toolset; note
  the human-review-on-conflict discipline as a mandatory design constraint.

### Claim 7: Feature branch sync triggers on `pull_request` events (`opened`, `synchronize`) on `feature/**` branches — creating a matching branch in an integration test repository and syncing relevant changes for cross-repo integration testing before main merge

- **Evidence**: Page's "Feature Branch Sync" example. Trigger: `pull_request`
  events (`opened`, `synchronize`), branches `feature/**`. Permissions: `contents:
  read`, `pull-requests: read`, `actions: read`. Tools: `github` with
  `[repos, pull_requests]` toolsets. Agent instructions include creating matching
  branch in the integration test repo, syncing relevant changes, and updating test
  configurations.
- **Confidence**: settled (first-party YAML example)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `pull_request` trigger with `branches: feature/**` fires
  on every push to any feature branch that has an open PR — not on merge. This enables
  integration testing to run in a separate repo while the feature branch is still in
  review. The `synchronize` type is essential: it refires when the feature branch is
  updated, keeping the integration test environment current. The `pull-requests: read`
  permission addition (not present in other feature sync examples) is required to
  read the PR's branch metadata. For Ch06: document feature branch sync as the
  cross-repo integration testing enablement pattern; note that it requires `pull-requests:
  read` permissions (not just `contents: read`) and re-triggers on every feature branch
  push.

### Claim 8: Scheduled sync check (weekly) serves as a drift-detection safety net independent of push events — identifying the last sync PR and all unsynced commits since then, then creating catch-up PRs for any missed changes

- **Evidence**: Page's "Scheduled Sync Check" example. Trigger: weekly on Monday.
  Tools: `github` with `[repos, pull_requests]` toolsets. Agent instructions include
  finding the last sync PR, identifying all commits since then, and categorizing
  changes (features, fixes, docs).
- **Confidence**: settled (first-party YAML example)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The scheduled safety net is architecturally important: push-based
  sync can fail (workflow timeout, rate limit, transient error) and leave downstream
  repos silently drifted. A weekly catch-up identifies and remedies drift that
  event-driven sync missed. The `pull_requests` toolset access enables the agent to
  query the last sync PR to establish a baseline — without PR history access, the
  agent cannot determine what was last synced. The change categorization (features,
  fixes, docs) enables the catch-up PR to carry meaningful context. For Ch06:
  document scheduled drift detection as the recommended complement to event-driven
  feature sync for any production cross-repo synchronization setup.

### Claim 9: Feature sync PAT authentication requires `contents: write` and `pull-requests: write` on target repositories — broader than the issue-tracking pattern's scope because PR creation requires both content write access and pull request write access

- **Evidence**: Page's "Authentication Setup" section. PAT configuration requires
  `repo`, `contents: write`, and `pull-requests: write` permissions. GitHub App
  installation tokens are offered as the enhanced-security alternative.
- **Confidence**: settled (first-party authentication guidance)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The scope requirement for feature sync (`contents: write` +
  `pull-requests: write`) is broader than the issue-tracking pattern's scope
  (described in `docs-ghaw-multi-repo-issue-tracking.md` Claim 10 as `repo`/`public_repo`),
  because creating a PR requires pushing a branch (contents write) as well as
  opening the PR (pull-requests write). This is consistent with the principle in
  `docs-ghaw-multi-repo-ops.md` Claim 7 (write access only on target repositories,
  not on source), but requires a wider write scope than issue-only workflows.
  GitHub App tokens remain the preferred alternative for per-job minting and
  automatic revocation per `docs-ghaw-multi-repo-ops.md` Claim 8. For Ch02:
  document `contents: write` + `pull-requests: write` as the minimum PAT scope
  for PR-based cross-repo sync workflows; distinguish from the narrower issue-only
  scope.

### Claim 10: Changes are adapted for each downstream target's structure rather than copied verbatim — the agent reads the target repo's current state, adapts imports/paths, and validates compatibility before creating the PR

- **Evidence**: Multiple workflow examples on the page instruct the agent to check
  whether targets use changed modules, adapt imports and paths, preserve client-specific
  extensions, and validate no breaking changes — not to simply apply a diff.
- **Confidence**: emerging (this behavioral requirement is stated in agent instructions
  but the actual adaptation quality depends on model capability; not a platform-enforced
  guarantee)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The adaptation requirement distinguishes AI-assisted feature sync
  from deterministic file-copy tools like `rsync`. Deterministic file copy (as shown
  in `docs-ghaw-multi-repo-ops.md` Concrete Artifacts → Deterministic Multi-Repo
  Checkout section) is appropriate when target directory structures match exactly.
  AI-assisted adaptation is required when downstream consumers have diverged from
  the upstream structure. The tradeoff: AI adaptation is more flexible but less
  predictable; deterministic copy is more reliable but requires structural alignment.
  For Ch06: document the adaptation model as the key differentiator between AI-assisted
  and deterministic feature sync; recommend deterministic sync when structures align,
  AI-assisted sync when adaptation is needed.

## Concrete Artifacts

### Seven Feature Sync Workflow Patterns — Structure Overview

Note: The WebFetch tool returned descriptive summaries rather than verbatim YAML
for this source page (see Extraction Notes). The structures below are derived from
those descriptions and should be verified against the source URL before use as
reference implementations.

```
Pattern                    | Trigger                          | Tools               | Safe-Outputs
---------------------------|----------------------------------|---------------------|--------------------------------
Basic Feature Sync         | push/main, paths: shared/**      | github[repos],      | create-pull-request
                           |                                  | bash[git:*]         | → target-repo (single)
Multi-Target Sync          | push/main, paths: core/**        | github[repos],      | create-pull-request (max: 3)
                           |                                  | bash[git:*]         | → multiple targets
Release-Based Sync         | release: [published]             | github[repos],      | create-pull-request
                           |                                  | bash[git:*]         | → target-repo
Selective File Sync        | push/main,                       | github[repos],      | create-pull-request
                           | paths: types/**/*.ts,            | bash[git:*]         | → target-repo
                           |        interfaces/**/*.ts        |                     |
Bidirectional Sync         | push/main,                       | github[repos,       | create-pull-request
  (Conflict Detection)     | paths: shared-config/**          |  pull_requests],    | → target-repo (manual review flag)
                           |                                  | bash[git:*]         |
Feature Branch Sync        | pull_request (opened,            | github[repos,       | create-pull-request
                           |   synchronize),                  |  pull_requests],    | → integration-test-repo
                           | branches: feature/**             | bash[git:*]         |
Scheduled Sync Check       | weekly on Monday                 | github[repos,       | create-pull-request
                           |                                  |  pull_requests],    | (catch-up PRs)
                           |                                  | bash[git:*]         |
```

### Permissions Progression Across Patterns

```
Pattern                        | Additional permissions beyond "contents: read, actions: read"
-------------------------------|--------------------------------------------------------------
Basic Feature Sync             | (none beyond base)
Multi-Target Sync              | (none beyond base)
Release-Based Sync             | (none beyond base)
Selective File Sync            | (none beyond base)
Bidirectional Sync             | (none beyond base; pull_requests toolset provides read via tools)
Feature Branch Sync            | pull-requests: read  [needed for PR branch metadata]
Scheduled Sync Check           | (none beyond base)
```

### PAT Scope for Feature Sync

From the page's "Authentication Setup" section (described, not verbatim YAML):

```
PAT scope for feature sync workflows:
  Permissions required: repo, contents: write, pull-requests: write
  Stored as: repository secret
  Alternative: GitHub App installation token (preferred for enhanced security)

Note: Broader than issue-only cross-repo workflows which require only
      issues: write on the target. Feature sync requires contents: write
      to push branches and pull-requests: write to open PRs.
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-multi-repo-ops.md` Claim 5 (upstream-to-downstream: "Main repo
    propagates changes using `create-pull-request` with `target-repo` per downstream"):
    All seven workflows on this page implement exactly this topology — the main repo
    triggers, creates branches, and opens PRs in downstream targets. This is the
    concrete instantiation of that abstract topology description.
  - `docs-ghaw-multi-repo-ops.md` Claim 8 (GitHub App Installation Tokens preferred
    over PATs for per-job minting and automatic revocation): Claim 9 above echoes
    the GitHub App preference for enhanced security, consistent with the pattern
    documentation.
  - `docs-ghaw-multi-repo-ops.md` Claim 7 (PAT least-privilege: read on source,
    write on target only): The feature-sync PAT scope follows this directional
    principle — `contents: write` and `pull-requests: write` on target repos only,
    not on the source repo.
  - `docs-ghaw-multi-repo-issue-tracking.md` Claim 10 (authentication requires PAT
    with cross-repo scopes; GitHub App preferred): Consistent recommendation across
    both examples pages — PATs are the working-configuration default in examples,
    GitHub App is the production recommendation.

- **Extends**:
  - `docs-ghaw-multi-repo-ops.md`: That note documents `create-pull-request` +
    `target-repo` as the upstream-to-downstream primitive (Claim 5) and the
    deterministic multi-checkout artifact as one implementation approach. This source
    provides seven distinct agent-driven implementations that demonstrate the full
    range of trigger types (push, release, pull_request, scheduled) and sync
    complexities (basic copy, adaptive merge, bidirectional, selective) for the
    same topology.
  - `docs-ghaw-multi-repo-issue-tracking.md`: That note provides eight cross-repo
    issue-tracking workflow patterns. This note provides the PR-based counterpart —
    together they give the full cross-repo coordination vocabulary for the two primary
    safe-output types used in cross-repo workflows: `create-issue` (issue tracking)
    and `create-pull-request` (feature sync).
  - `docs-ghaw-code-quality-monitoring.md`: That note demonstrates the side-repo
    pattern where a monitoring repo reads from and writes to a target. Feature branch
    sync (Claim 7) uses a similar cross-repo trigger model but from a main-to-integration
    direction. The `pull-requests: read` permission requirement in feature branch sync
    maps to `docs-ghaw-code-quality-monitoring.md` Claim 8's `pull_requests` toolset
    for accessing PR history.

- **Contradicts**: None identified. The PAT scope for feature sync (`contents: write`
  + `pull-requests: write`) is broader than issue-tracking workflows but follows the
  same directional principle (write on target only). This is a scope difference driven
  by different operation requirements, not a contradiction. No contradiction issue filed.

- **Novel**:
  - **Release-based sync trigger (`release: published`) as a distinct topology**
    (Claim 4): No existing source note documents the release event as a feature sync
    trigger, or the associated pattern of using release notes as agent input for
    identifying breaking changes. This is distinct from commit-by-commit push-based sync.
  - **Feature branch sync (`pull_request` trigger on `feature/**`)** (Claim 7): The
    cross-repo pattern where a PR in the main repo triggers branch creation and content
    sync in an integration test repository is not documented in any existing source
    note. This enables cross-repo integration testing before merge without requiring
    shared infrastructure.
  - **Scheduled drift detection as a safety net** (Claim 8): The pattern of using
    a weekly scheduled workflow to find the last sync PR and identify unsynced commits
    as a catch-up mechanism is new to the corpus. Prior notes cover scheduled monitoring
    (`docs-ghaw-monitoring-patterns.md`) but not scheduled drift-detection for cross-repo
    sync specifically.
  - **Adaptation requirement distinguishes AI-assisted from deterministic sync**
    (Claim 10): The framing that AI-assisted feature sync adds value specifically when
    downstream structure differs from upstream (requiring imports/paths adaptation) is
    not drawn explicitly in any existing source note. `docs-ghaw-multi-repo-ops.md`
    shows deterministic rsync-based checkout as one approach; this source frames
    AI-assisted sync as the answer when deterministic copy is insufficient.
  - **Seven complete feature-sync workflow configurations for the PR-creation use
    case** (Concrete Artifacts): The MultiRepoOps note documents `create-pull-request`
    in one example as part of the topology table. This source provides seven
    differentiated PR-based sync configurations, substantially expanding the
    implementation vocabulary for practitioners building upstream-to-downstream
    coordination.

## Guide Impact

### Chapter 06: Orchestration and Multi-Agent Coordination

- **Add seven feature sync patterns as concrete implementations of the
  upstream-to-downstream topology** (Claims 1–8): Ch06 currently covers upstream-to-downstream
  abstractly via `docs-ghaw-multi-repo-ops.md` Claim 5. This source provides the
  decision matrix for the topology: push-based (basic or multi-target) for continuous
  propagation; release-based for versioned API consumers; selective-type-based for
  interface contract maintenance; bidirectional for shared-config scenarios;
  feature-branch for cross-repo integration testing; scheduled for drift detection.

- **Add `release: published` trigger as the release-cycle-aligned sync mechanism**
  (Claim 4): When downstream consumers track releases (not rolling main), the release
  trigger is correct. Document as distinct from push-based sync with the explicit
  trade-off: less frequent PRs but more semantically meaningful (aligned with upstream
  release notes and breaking change documentation).

- **Add feature branch sync as the cross-repo integration testing enablement pattern**
  (Claim 7): The `pull_request` trigger on `feature/**` with downstream branch
  creation enables cross-repo integration testing before merge. Document the
  `synchronize` event type addition (refires on every feature branch push) and the
  `pull-requests: read` permission requirement.

- **Add scheduled drift detection as the required safety net for production sync
  setups** (Claim 8): Document weekly scheduled sync check as a complement to
  event-driven sync — it catches failures that the event-driven workflows missed.
  Reference the `pull_requests` toolset as required for last-sync-PR lookup.

### Chapter 02: Harness Engineering

- **Document `contents: write` + `pull-requests: write` as the minimum PAT scope for
  PR-based cross-repo sync** (Claim 9): PR creation requires both scopes. Distinguish
  from the narrower issue-tracking scope (issues: write only). Pair with the
  `docs-ghaw-multi-repo-ops.md` Claim 7 directional principle (write on target only)
  as the framing for both use cases.

- **Add `paths:` filter as the required trigger scoping mechanism for push-based
  feature sync** (Claim 2): Without `paths:`, every push triggers a sync regardless
  of whether relevant files changed. Document the glob pattern syntax (e.g.,
  `shared/**`, `types/**/*.ts`) and the file-type-specific double-glob variant for
  selective sync.

- **Add the adaptation requirement as the key differentiator between AI-assisted
  and deterministic sync** (Claim 10): When downstream structure matches upstream,
  use deterministic file copy (rsync-based, per `docs-ghaw-multi-repo-ops.md`
  Concrete Artifacts). When downstream has diverged and requires path/import
  adaptation, use AI-assisted sync. Frame as a design choice with explicit trade-offs.

### Chapter 03: Safety and Verification

- **Document `pull_requests: read` as a required permission for feature branch sync
  and bidirectional sync** (Claim 7): Both patterns access PR history via the
  `pull_requests` toolset. Inconsistency between declared permissions and toolset
  usage will cause silent failures (empty PR query results, not errors).

## Extraction Notes

1. **WebFetch returned summaries, not verbatim YAML**: Three WebFetch calls were made
   to the source URL. The first two returned structured summaries. The second call
   explicitly declined to reproduce verbatim YAML. The third returned descriptive
   structure matching the first. Concrete Artifacts in this note reflect the
   described structures, not character-for-character YAML reproductions. One verbatim
   quote was captured from the "When to Use" section (Claim 1). All other quotes are
   marked "(no direct quote; see paraphrase in Our assessment)."

2. **Source is in the `examples/` section, not `patterns/`**: Like
   `docs-ghaw-multi-repo-issue-tracking.md` and `docs-ghaw-code-quality-monitoring.md`,
   this is a practitioner implementation walkthrough, not a conceptual reference page.
   Claims about workflow behavior beyond what is shown in the YAML descriptions are
   inferred from the agent instruction summaries provided by WebFetch.

3. **Multi-target sync `target-repo` configuration not specified**: The WebFetch
   description of Multi-Target Sync indicates `create-pull-request: max: 3` but does
   not specify whether `target-repo` is set to a fixed value or determined dynamically
   by the agent (as in `docs-ghaw-multi-repo-issue-tracking.md` Claim 6's triage
   routing). This is unresolved — the source should be consulted directly.

4. **Bidirectional sync conflict detection mechanism**: The agent instruction
   description ("compare timestamps and change history") implies use of the
   `pull_requests` toolset and potentially `repos` toolset for git log access. The
   exact conflict detection algorithm is not specified; this is an AI-executed
   heuristic, not a platform-enforced detection mechanism.

5. **No publication date**: The documentation page does not carry an explicit
   publication date. Content is consistent with gh-aw platform behavior as of 2026-05-22.

6. **No contradictions filed**: Reviewed all existing source notes against all claims.
   The PAT scope difference between feature sync and issue tracking is driven by
   different operation requirements (PR creation vs. issue creation), not a material
   contradiction leading to different guide advice. No contradiction issue filed.
