---
source_url: https://github.github.com/gh-aw/examples/multi-repo/issue-tracking
source_type: docs
title: "GitHub Agentic Workflows Examples: Multi-Repo Issue Tracking"
author: GitHub Agentic Workflows team (official documentation)
date_published: null
date_extracted: 2026-05-22
last_checked: 2026-05-22
status: current
confidence_overall: emerging
issue: "#853"
---

# GitHub Agentic Workflows Examples: Multi-Repo Issue Tracking

> Concrete YAML implementations of eight cross-repository issue-tracking workflow
> patterns — basic tracking creation, status synchronization, multi-component
> coordination, external dependency monitoring, automated triage/routing, aggregated
> reporting, bidirectional linking, and priority-based routing — extending the abstract
> MultiRepoOps `target-repo` primitive from `docs-ghaw-multi-repo-ops.md` with
> worked examples for the issue-tracking use case.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows "Examples" section — worked
  implementations of design patterns. Examples pages demonstrate specific configurations
  for concrete use cases; distinct from the "Patterns" reference pages which document
  the abstract design primitives.)
- **Author credibility**: GitHub Agentic Workflows team — same team behind the Peli
  de Halleux "Agent Factory" blog series and the `gh aw` CLI. YAML configurations are
  first-party examples that demonstrate supported platform behavior. Claims about
  configuration schemas and field semantics are authoritative for the gh-aw platform.
- **Scope**: Eight workflow patterns for cross-repository issue tracking using
  `create-issue`, `add-comment`, and `create-discussion` safe outputs with `target-repo`.
  Covers authentication setup (PAT vs. GitHub App) for cross-repo workflows. Does NOT
  cover: the abstract MultiRepoOps design primitives (see `docs-ghaw-multi-repo-ops.md`),
  the `assign-to-agent` safe output for routing issues to Copilot (see
  `docs-ghaw-assign-to-copilot.md`), or the IssueOps trigger pattern in isolation
  (see `docs-ghaw-issueops.md`).

## Extracted Claims

### Claim 1: Cross-repo issue tracking is suited for component-based architectures requiring centralized visibility, external dependency monitoring, cross-project coordination, and distributed metrics aggregation

- **Evidence**: The page's overview and "When to Use" section enumerate these four use
  cases as the primary motivation for cross-repo issue-tracking workflows.
- **Confidence**: settled (first-party; use cases stated directly on the page)
- **Quote**: "Use cross-repo issue tracking for component-based architectures where
  multiple teams need centralized visibility, when tracking external dependencies,
  coordinating cross-project initiatives, or aggregating metrics from distributed
  repositories."
- **Our assessment**: These four use cases map directly to the eight workflow patterns
  on the page: basic tracking and bidirectional linking address centralized visibility;
  the external dependency workflow addresses cross-org monitoring; multi-component
  tracking addresses cross-project coordination; aggregated reporting addresses
  distributed metrics aggregation. The taxonomy is a useful decision matrix for
  practitioners choosing which patterns to implement — start with the use case, then
  pick the matching pattern.

### Claim 2: Basic tracking issue creation for hub-and-spoke cross-repo coordination uses `create-issue` with `target-repo`, `title-prefix`, and component-specific labels to namespace the tracking issue in the central tracker

- **Evidence**: Complete YAML configuration on the page (reproduced verbatim in
  Concrete Artifacts). Key fields: `target-repo: "myorg/central-tracker"`,
  `title-prefix: "[component-alpha] "`, `labels: [from-component-alpha, tracking-issue]`.
- **Confidence**: settled (first-party YAML example; fields are explicit)
- **Quote**: (from YAML configuration block on page; see Concrete Artifacts)
- **Our assessment**: This is the hub-and-spoke pattern (`docs-ghaw-multi-repo-ops.md`
  Claim 4) applied concretely to issue tracking — each component workflow creates a
  tracking issue in the central tracker when an issue opens. The `title-prefix`
  convention namespaces issues from different components; without consistent namespacing,
  the central tracker becomes unreadable when many components forward to it. The
  `labels: [from-component-alpha, tracking-issue]` supports label-based filtering
  across all component issues in the central tracker. For Ch04: this is the practical
  entry point for teams building cross-repo issue visibility.

### Claim 3: Status synchronization from component to central tracker uses `add-comment` with both `target-repo` and `target: "*"` — the agent identifies which central tracking issue to update, triggered by closed/reopened/labeled/unlabeled events

- **Evidence**: YAML configuration for the status sync workflow (see Concrete Artifacts).
  Triggers on `issues: types: [closed, reopened, labeled, unlabeled]`. Uses
  `add-comment: target-repo: "myorg/central-tracker"` with `target: "*"` — requiring
  the agent to output which tracking issue to comment on.
- **Confidence**: settled (first-party YAML configuration; fields are explicit)
- **Quote**: (from YAML configuration block; trigger verbatim: `types: [closed, reopened,
  labeled, unlabeled]`)
- **Our assessment**: The `target: "*"` pattern on `add-comment` with `target-repo` is
  notable — the agent must look up which tracking issue corresponds to the triggering
  component issue and output its number for the Safe Output Processor to resolve. This
  creates a dependency on the agent's ability to find the tracking issue reliably (e.g.,
  by searching for matching title or a stored cross-reference). The sync is
  one-directional: component → central. Bidirectional sync (where closing the tracking
  issue also closes component issues) would require a separate workflow watching the
  central tracker. For Ch04: document this as the "status propagation" complement to
  the basic "tracking creation" pattern; note the agent lookup dependency.

### Claim 4: Multi-component tracking uses `create-issue: max: 3` to create coordinated tracking issues across multiple repositories in a single workflow run when an issue is flagged as cross-component

- **Evidence**: YAML configuration for multi-component workflow (see Concrete Artifacts).
  `create-issue: max: 3` with `labels: [cross-component, needs-coordination]`.
- **Confidence**: settled (first-party YAML configuration)
- **Quote**: (from YAML configuration block on page)
- **Our assessment**: `max: 3` is the specific fan-out limit for this pattern — it
  allows tracking issues in up to three repositories per workflow run. The `cross-component`
  label signals that this issue spans multiple teams/repos. The `max` parameter is
  the critical fan-out control: teams tracking more than three components must raise
  `max` accordingly or risk all-or-nothing rejection per the Safe Outputs semantics
  documented in `docs-ghaw-safe-outputs-specification.md`. For Ch04: note that `max`
  on `create-issue` bounds how many tracking issues the agent can create per trigger —
  an essential guard for multi-component workflows that could otherwise create dozens
  of tracking issues for a single root issue.

### Claim 5: External dependency tracking uses `workflow_dispatch` with an `external_issue_url` input and the `web-fetch` toolset to fetch external upstream issue content and create an internal tracking issue with `[upstream]` prefix

- **Evidence**: YAML configuration for the external dependency workflow (see Concrete
  Artifacts). `on: workflow_dispatch` with `external_issue_url` input; `tools: web-fetch:`
  toolset; `target-repo: "myorg/dependency-tracker"` with `title-prefix: "[upstream] "`.
- **Confidence**: settled (first-party YAML configuration; fields are explicit)
- **Quote**: (from YAML configuration block on page; input description verbatim:
  `description: 'URL of external issue to track'`)
- **Our assessment**: The combination of `workflow_dispatch` + `web-fetch` toolset is
  novel in the corpus: the workflow is manually triggered with an external URL, fetches
  that upstream issue's content, and creates an internal tracking issue. This is the
  pattern for monitoring third-party upstream issues (e.g., bugs in dependencies that
  your org is waiting on) without requiring the external repo to participate or grant
  access. The `web-fetch` toolset is what makes this cross-organization — it fetches
  the public issue page as HTML, bypassing GitHub API scoping. For Ch04: document
  external dependency tracking as the cross-org pattern; it requires no access to the
  external repository, unlike all other patterns on this page.

### Claim 6: Automated triage and routing accesses issue content via `steps.sanitized.outputs.text` and uses `create-issue: max: 2` with agent-determined `target-repo` — the agent classifies the issue and dynamically picks which specialized tracker to route it to

- **Evidence**: YAML configuration for the triage workflow (see Concrete Artifacts).
  `safe-outputs: create-issue: max: 2` without a fixed `target-repo` — the agent
  determines the target based on issue classification. Issue content accessed via
  `"${{ steps.sanitized.outputs.text }}"` in the workflow body.
- **Confidence**: settled (first-party YAML configuration; the absence of fixed
  `target-repo` is intentional, consistent with agent-driven routing)
- **Quote**: (from YAML block; workflow body verbatim: `**Content:** "${{ steps.sanitized.outputs.text }}"`)
- **Our assessment**: This is the most flexible routing pattern — the agent, not the
  workflow YAML, decides the target tracker based on classification. `steps.sanitized.outputs.text`
  provides sanitized issue content per `docs-ghaw-issueops.md` Claim 4 for safe
  classification. The `max: 2` bound means the agent can create tracking issues in at
  most two trackers for a single issue — useful for issues spanning categories (e.g.,
  a security bug that also has infrastructure impact). For Ch04: this is the dynamic
  routing complement to the fixed-target patterns; document alongside the IssueOps
  trigger pattern as the full triage-and-route pipeline.

### Claim 7: Aggregated reporting uses `create-discussion` with `target-repo` on a weekly schedule to publish cross-repo issue summaries as GitHub Discussions in the central tracker

- **Evidence**: YAML configuration for the reporting workflow (see Concrete Artifacts).
  `on: weekly on monday`, `safe-outputs: create-discussion: target-repo: "myorg/central-tracker"`,
  `category: "Status Reports"`, `title-prefix: "[weekly] "`.
- **Confidence**: settled (first-party YAML configuration)
- **Quote**: (from YAML block; workflow body verbatim: `Generate weekly summary of
  tracked issues across all component repositories.`)
- **Our assessment**: `create-discussion` with `target-repo` is a new configuration
  in the corpus — prior notes document `create-discussion` in same-repo contexts only.
  The weekly schedule trigger combined with cross-repo `create-discussion` creates a
  pattern for automated metrics dashboarding in GitHub Discussions format. The agent
  queries issues across repositories via the GitHub toolset and posts the aggregated
  summary as a Discussion. The `category: "Status Reports"` parameter routes the
  discussion to the correct category in the central tracker. For Ch04: document
  cross-repo `create-discussion` as the reporting layer for multi-repo tracking setups.

### Claim 8: Bidirectional linking requires two safe output types in a single workflow — `create-issue: target-repo` creates the tracking issue in the central tracker, then `add-comment: max: 1` adds a link back to the original component issue

- **Evidence**: YAML configuration for the bidirectional linking workflow (see Concrete
  Artifacts). Two safe output types in one workflow: `create-issue: target-repo: "myorg/central-tracker"`
  and `add-comment: max: 1` targeting the triggering component issue.
- **Confidence**: settled (first-party YAML configuration)
- **Quote**: (from YAML block; workflow body verbatim: `**Original issue:** ${{ github.event.issue.html_url }}`)
- **Our assessment**: The bidirectional link is implemented by a single workflow doing
  two things: (1) create the tracking issue in the central tracker, (2) comment back on
  the original component issue with the tracking issue URL. The `max: 1` on `add-comment`
  ensures exactly one link-back comment per run. The `${{ github.event.issue.html_url }}`
  in the workflow body provides the agent with the original issue URL to embed in the
  tracking issue and link-back comment. For Ch04: document bidirectional linking as
  the navigation/audit-trail pattern — it requires no additional tooling beyond what
  other patterns already use, just a second safe output type in the same workflow.

### Claim 9: Priority-based routing uses `create-issue: max: 1` triggered on both opened and labeled events — the agent reads P0-P3 labels to determine the target tracker, with P0 triggering incident response procedures

- **Evidence**: YAML configuration for the priority routing workflow (see Concrete
  Artifacts). `on: issues: types: [opened, labeled]` with `create-issue: max: 1` and
  `title-prefix: "[priority-routed] "`. Four-tier routing (P0 → incidents, P1 →
  priority-tracker, P2 → central-tracker, P3 → backlog) described on the page.
- **Confidence**: settled (first-party YAML configuration and routing tier description)
- **Quote**: (from YAML block; trigger verbatim: `types: [opened, labeled]`)
- **Our assessment**: The `labeled` event type is critical here — it fires when a
  priority label is added, enabling retrospective routing for issues that opened without
  a priority label and were labeled later. `max: 1` ensures one tracking issue per run.
  P0 routing to an "incidents" tracker implies integration with incident response
  procedures — the most urgent issues receive a dedicated tracking workflow beyond
  standard issue management. For Ch04: document the `labeled` trigger addition as the
  key that makes priority routing work retroactively, not just at issue creation time.

### Claim 10: Authentication for cross-repo issue-tracking workflows requires a PAT with `repo` scope for private repositories or `public_repo` for public repositories; GitHub App installation tokens are preferred for enhanced security

- **Evidence**: Authentication section of the page. All eight YAML configurations use
  `github-token: ${{ secrets.GH_AW_CROSS_REPO_PAT }}`. PAT scopes stated explicitly.
- **Confidence**: settled (first-party authentication guidance)
- **Quote**: "For enhanced security, use GitHub App installation tokens."
- **Our assessment**: The PAT scope described (`repo` or `public_repo`) is broader than
  the least-privilege recommendation in `docs-ghaw-multi-repo-ops.md` Claim 7, which
  specifies read on source and write only on target repos. The examples page shows
  minimal-effort working configurations; the MultiRepoOps pattern page provides the
  security-hardened version. Teams should use the `docs-ghaw-multi-repo-ops.md` Claim 7
  scoping guidance for production deployments rather than the examples-page defaults.
  The GitHub App preference is consistent with `docs-ghaw-multi-repo-ops.md` Claim 8
  (GitHub App Installation Tokens preferred for per-job minting and automatic revocation).

## Concrete Artifacts

### Basic Tracking Issue Creation (hub-and-spoke)

```yaml
---
on:
  issues:
    types: [opened]
permissions:
  contents: read
  actions: read
tools:
  github:
    toolsets: [issues]
safe-outputs:
  github-token: ${{ secrets.GH_AW_CROSS_REPO_PAT }}
  create-issue:
    target-repo: "myorg/central-tracker"
    title-prefix: "[component-alpha] "
    labels: [from-component-alpha, tracking-issue]
---
# Create Tracking Issue for Component Issues
When issues are created in component repositories, automatically create corresponding
tracking issues in the central tracker.
**Original issue:** ${{ github.event.issue.html_url }}
```

*Source: gh-aw examples, "Cross-Repository Issue Tracking — Basic Tracking Issue Creation"*

### Status Synchronization

```yaml
---
on:
  issues:
    types: [closed, reopened, labeled, unlabeled]
permissions:
  contents: read
  actions: read
tools:
  github:
    toolsets: [issues]
safe-outputs:
  github-token: ${{ secrets.GH_AW_CROSS_REPO_PAT }}
  add-comment:
    target-repo: "myorg/central-tracker"
    target: "*"
---
# Update Central Tracking Issue Status
When this component issue changes status, update the central tracking issue.
**Original issue:** ${{ github.event.issue.html_url }}
**Action:** ${{ github.event.action }}
```

*Source: gh-aw examples, "Cross-Repository Issue Tracking — Status Synchronization"*

### Multi-Component Tracking

```yaml
---
on:
  issues:
    types: [opened]
permissions:
  contents: read
  actions: read
tools:
  github:
    toolsets: [issues]
safe-outputs:
  github-token: ${{ secrets.GH_AW_CROSS_REPO_PAT }}
  create-issue:
    max: 3
    target-repo: "myorg/central-tracker"
    title-prefix: "[cross-component] "
    labels: [cross-component, needs-coordination]
---
# Track Cross-Component Issues
When an issue is marked as cross-component, create coordinated tracking issues.
**Original issue:** ${{ github.event.issue.html_url }}
```

*Source: gh-aw examples, "Cross-Repository Issue Tracking — Multi-Component Tracking"*

### External Dependency Tracking

```yaml
---
on:
  workflow_dispatch:
    inputs:
      external_issue_url:
        description: 'URL of external issue to track'
        required: true
        type: string
permissions:
  contents: read
tools:
  github:
    toolsets: [issues]
  web-fetch:
safe-outputs:
  github-token: ${{ secrets.GH_AW_CROSS_REPO_PAT }}
  create-issue:
    target-repo: "myorg/dependency-tracker"
    title-prefix: "[upstream] "
    labels: [external-dependency, upstream-issue]
---
# Track External Dependency Issue
Create tracking issue for external dependency problem.
**External issue URL:** ${{ github.event.inputs.external_issue_url }}
```

*Source: gh-aw examples, "Cross-Repository Issue Tracking — External Dependency Tracking"*

### Automated Triage and Routing

```yaml
---
on:
  issues:
    types: [opened]
permissions:
  contents: read
  actions: read
tools:
  github:
    toolsets: [issues]
safe-outputs:
  github-token: ${{ secrets.GH_AW_CROSS_REPO_PAT }}
  create-issue:
    max: 2
    title-prefix: "[auto-triaged] "
---
# Triage and Route to Tracking Repos
Analyze new issues and create tracking issues in appropriate repositories.
**Original issue:** ${{ github.event.issue.html_url }}
**Content:** "${{ steps.sanitized.outputs.text }}"
```

*Source: gh-aw examples, "Cross-Repository Issue Tracking — Automated Triage and Routing"*

### Aggregated Reporting

```yaml
---
on: weekly on monday
permissions:
  contents: read
tools:
  github:
    toolsets: [issues]
safe-outputs:
  github-token: ${{ secrets.GH_AW_CROSS_REPO_PAT }}
  create-discussion:
    target-repo: "myorg/central-tracker"
    category: "Status Reports"
    title-prefix: "[weekly] "
---
# Weekly Cross-Repo Issue Summary
Generate weekly summary of tracked issues across all component repositories.
```

*Source: gh-aw examples, "Cross-Repository Issue Tracking — Aggregated Reporting"*

### Bidirectional Linking

```yaml
---
on:
  issues:
    types: [opened]
permissions:
  contents: read
  actions: read
tools:
  github:
    toolsets: [issues]
safe-outputs:
  github-token: ${{ secrets.GH_AW_CROSS_REPO_PAT }}
  create-issue:
    target-repo: "myorg/central-tracker"
    title-prefix: "[linked] "
  add-comment:
    max: 1
---
# Create Tracking Issue with Bidirectional Links
Create tracking issue and add comment to original with link.
**Original issue:** ${{ github.event.issue.html_url }}
```

*Source: gh-aw examples, "Cross-Repository Issue Tracking — Bidirectional Linking"*

### Priority-Based Routing

```yaml
---
on:
  issues:
    types: [opened, labeled]
permissions:
  contents: read
  actions: read
tools:
  github:
    toolsets: [issues]
safe-outputs:
  github-token: ${{ secrets.GH_AW_CROSS_REPO_PAT }}
  create-issue:
    max: 1
    title-prefix: "[priority-routed] "
---
# Route Issues Based on Priority
Route issues to appropriate tracking repository based on priority level.
**Original issue:** ${{ github.event.issue.html_url }}
**Labels:** Check for priority labels (P0, P1, P2, P3)
```

*Source: gh-aw examples, "Cross-Repository Issue Tracking — Priority-Based Routing"*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-multi-repo-ops.md` Claim 4 (hub-and-spoke: "Each component workflow
    creates tracking issues in a central repo via `target-repo`"): Claim 2 above is
    a direct implementation of this topology — the basic tracking pattern is the
    hub-and-spoke pattern with concrete field values filled in for the issue-tracking
    use case.
  - `docs-ghaw-multi-repo-ops.md` Claim 8 (GitHub App Installation Tokens preferred
    for per-job minting and automatic revocation): Claim 10 above echoes this preference,
    citing "enhanced security."
  - `docs-ghaw-issueops.md` Claim 1 (`on: issues: types: [opened]` trigger): The
    basic tracking, multi-component, bidirectional linking, triage, and bidirectional
    linking patterns all use this same trigger. The IssueOps note documents it for
    single-repo contexts; this source shows it powering cross-repo workflows.
  - `docs-ghaw-issueops.md` Claim 4 (`steps.sanitized.outputs.text` for issue content):
    The triage and routing workflow (Claim 6) uses `"${{ steps.sanitized.outputs.text }}"`
    in the agent body — consistent with IssueOps best practice for accessing issue
    content safely before AI processing.

- **Contradicts**: None identified. The PAT scope described in Claim 10 (`repo` /
  `public_repo`) is broader than the security-hardened guidance in
  `docs-ghaw-multi-repo-ops.md` Claim 7 (read on source, write on target only),
  but this is an examples page showing working configurations, not a security guidance
  page. The difference is context-dependent (examples vs. best practices), not a
  genuine contradiction leading to conflicting guide advice.

- **Extends**:
  - `docs-ghaw-multi-repo-ops.md`: That note documents the `target-repo` parameter
    and MultiRepoOps topology archetypes abstractly. This source provides eight
    concrete issue-tracking implementations that demonstrate those archetypes in
    practice: Claim 2 → hub-and-spoke (Claim 4 in multi-repo-ops); Claim 7 →
    org-wide reporting via `create-discussion`; Claim 9 → priority-based variant
    of hub-and-spoke.
  - `docs-ghaw-issueops.md`: That note documents IssueOps for single-repo contexts.
    This source combines IssueOps triggers with cross-repo safe outputs — extending
    the IssueOps pattern to multi-repo scenarios. The status sync workflow additionally
    extends the trigger set to `closed/reopened/labeled/unlabeled` events, not just
    `opened`.
  - `docs-ghaw-assign-to-copilot.md` Claim 6 (`pull-request-repo` for centralized
    issue, distributed code): That note describes centralized issue tracking with
    distributed code PRs. This source provides the issue-side implementation — the
    workflows that populate and maintain the centralized tracker that `assign-to-agent`
    workflows then route from.

- **Novel**:
  - **`add-comment` with both `target-repo` and `target: "*"` for cross-repo status
    sync** (Claim 3): No prior source documents `add-comment` with `target-repo`. Prior
    notes show `add-comment: target: "triggering"` (IssueOps, same repo) or
    `add-comment: target: "4750"` (DailyOps, fixed number). Cross-repo `add-comment`
    with agent-driven `target: "*"` for status propagation is new to the corpus.
  - **`workflow_dispatch` + `web-fetch` toolset for cross-org external dependency
    tracking** (Claim 5): No prior corpus note documents this combination. Using
    `web-fetch` to fetch external upstream issue content across organizational
    boundaries without GitHub API access is entirely new.
  - **`create-discussion: target-repo` for cross-repo aggregated reporting** (Claim 7):
    Prior notes document `create-discussion` for same-repo contexts only. Cross-repo
    `create-discussion` as a reporting output type is new to the corpus.
  - **Priority-based routing via P0-P3 labels with `labeled` event trigger** (Claim 9):
    The `labeled` event type as a routing trigger — enabling retrospective routing when
    priority labels are added after initial filing — is not documented in prior notes.
  - **Eight concrete issue-tracking workflow configurations** (Concrete Artifacts): The
    MultiRepoOps note documents one generic hub-and-spoke example. This source provides
    eight distinct, complete workflow configurations for the issue-tracking use case,
    substantially richer artifact coverage for practitioners implementing at scale.

## Guide Impact

### Chapter 04: Agent Patterns / Multi-Agent Architecture

- **Add eight issue-tracking workflow patterns as concrete implementations of
  MultiRepoOps** (Claims 2–9): Ch04 currently covers MultiRepoOps topology archetypes
  abstractly. This source provides worked implementations for the issue-tracking use
  case. The eight patterns form a decision matrix: choose basic tracking for simple
  centralized visibility; add status sync for lifecycle tracking; add bidirectional
  linking for navigation and audit trail; add priority routing for triage automation;
  add triage/routing for intelligent classification; add aggregated reporting for
  periodic dashboards; add external dependency tracking for cross-org monitoring.

- **Add `add-comment: target-repo` + `target: "*"` as the cross-repo status
  propagation primitive** (Claim 3): Ch04 should document this pattern specifically —
  it differs from same-repo `target: "triggering"` and from `create-issue: target-repo`
  for initial creation. Note the agent lookup dependency: the agent must identify the
  target tracking issue number by querying the central tracker.

- **Add `workflow_dispatch` + `web-fetch` as the cross-org external dependency
  monitoring pattern** (Claim 5): For teams monitoring upstream issues in repositories
  they don't control, `workflow_dispatch` with `web-fetch` is the correct pattern.
  Document as distinct from within-org cross-repo patterns (which use GitHub toolsets).

### Chapter 02: Harness Engineering

- **Add `create-discussion: target-repo` to the cross-repo safe-output coverage**
  (Claim 7): The safe-output cross-repo support matrix in `docs-ghaw-multi-repo-ops.md`
  lists `create-discussion` as cross-repo-capable. This source provides the first
  concrete use: aggregated reporting via Discussions. Ch02 should add this as an
  example of the reporting safe-output type in multi-repo setups.

- **Document `on: issues: types: [labeled]` as a routing trigger** (Claim 9): Priority
  routing fires on `labeled` events, enabling retrospective routing when labels are
  applied after initial filing. Ch02's IssueOps trigger coverage should note this
  event type addition alongside the standard `opened` trigger.

- **Note PAT scope gap between examples and best practices** (Claim 10): The examples
  page uses `repo`/`public_repo` PAT scopes (broader than needed). Ch02 should direct
  practitioners to `docs-ghaw-multi-repo-ops.md` Claim 7 least-privilege scope guidance
  rather than the examples-page defaults for production deployments.

## Extraction Notes

1. **Examples page, not reference page**: This is an `examples/` section page providing
   worked configurations, not a `reference/` or `patterns/` page. Behavioral claims
   beyond what is shown in the YAML (e.g., how the agent identifies which tracking issue
   to update in the status sync pattern) are inferred from configuration semantics, not
   stated explicitly.

2. **WebFetch content — YAML verbatim, prose selective**: Three WebFetch calls were
   made to the source URL. YAML configurations were returned consistently across multiple
   calls and are reproduced verbatim in Concrete Artifacts. Two direct prose quotes were
   captured verbatim (Claim 1 and Claim 10 quotes). All other claims cite the YAML
   block as evidence; `(from YAML configuration block on page)` is used where no prose
   quote captures the claim.

3. **`target-repo` in `add-comment` for status sync implies agent lookup**: The status
   sync workflow's `add-comment: target-repo` + `target: "*"` configuration requires
   the agent to identify and output the tracking issue number. The page describes the
   intended behavior but does not document the lookup mechanism explicitly. This likely
   relies on the agent searching the central tracker for an issue matching the component
   issue's title or HTML URL.

4. **Triage routing `target-repo` is agent-determined**: The triage workflow's
   `create-issue: max: 2` does not specify `target-repo` in the YAML. The agent
   determines the target dynamically based on issue classification. This is inferred
   from the absence of a fixed `target-repo` field; the page describes classification-
   based routing to specialized trackers (security tracker, feature tracker, bug tracker,
   ops tracker).

5. **No publication date**: The documentation page does not carry an explicit publication
   date. Content is consistent with gh-aw platform behavior as of 2026-05-22.

6. **No contradictions filed**: Reviewed all existing source notes. The PAT scope
   difference between this examples page and `docs-ghaw-multi-repo-ops.md` Claim 7
   is a context difference (examples vs. security guidance), not a material contradiction
   leading to different guide advice. No contradiction issue filed.
