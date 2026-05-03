---
source_url: https://github.github.com/gh-aw/patterns/multi-repo-ops
source_type: docs
title: "GitHub Agentic Workflows: MultiRepoOps Pattern"
author: GitHub Agentic Workflows team (official documentation)
date_published: null
date_extracted: 2026-05-03
last_checked: 2026-05-03
status: current
confidence_overall: emerging
issue: "#329"
---

# GitHub Agentic Workflows: MultiRepoOps Pattern

> The canonical reference for gh-aw's cross-repository coordination pattern —
> documents the `target-repo` safe-output parameter as the primary primitive,
> three topology archetypes (hub-and-spoke, upstream-to-downstream, org-wide
> broadcast), PAT vs. GitHub App authentication trade-offs, and the critical
> `GITHUB_TOKEN` footgun for cross-repo reads.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, "Patterns"
  section; first-party reference for the MultiRepoOps design pattern. Not a
  blog post or practitioner account.)
- **Author credibility**: GitHub Agentic Workflows team — the same team behind
  the Peli de Halleux / Don Syme agent factory blog series. Claims about
  platform schema, token scoping, and safe-output support matrix are
  authoritative for the gh-aw platform. Claims about general multi-repo
  orchestration should be treated as implementation perspective, not universal
  findings.
- **Scope**: The MultiRepoOps pattern — `target-repo` safe-output parameter,
  three topology archetypes, PAT and GitHub App authentication models, the
  `GH_AW_GITHUB_MCP_SERVER_TOKEN` secret for cross-repo reads, deterministic
  multi-checkout, the full safe-output cross-repo support matrix, and the
  relationship to CentralRepoOps. Does NOT cover: single-repo IssueOps or
  ChatOps patterns, the full Safe Outputs permission model (see
  `docs-ghaw-how-they-work.md`), or MCP server configuration (see
  `docs-ghaw-mcps.md`).

## Extracted Claims

### Claim 1: The `target-repo` parameter on safe outputs is the primary primitive for cross-repository coordination in gh-aw

- **Evidence**: The page's "How It Works" section states: "MultiRepoOps
  workflows use the `target-repo` parameter on safe outputs to create issues,
  pull requests, and comments in external repositories." The parameter is
  supported on eight safe output types: `create-issue`, `add-comment`,
  `update-issue`, `add-labels`, `create-pull-request`, `create-discussion`,
  `create-agent-session`, and `update-release`. A complete configuration
  example shows `target-repo: "org/tracking-repo"` as a top-level
  `safe-outputs` field under a specific output type.
- **Confidence**: settled (first-party documentation; the schema is explicitly
  demonstrated with a YAML example)
- **Quote**: "MultiRepoOps workflows use the `target-repo` parameter on safe
  outputs to create issues, pull requests, and comments in external
  repositories."
- **Our assessment**: `target-repo` is the single configuration primitive that
  unlocks all cross-repo safe output operations — there is no separate
  "cross-repo mode." The same safe output types used for single-repo operations
  become cross-repo when `target-repo` is specified. This is a clean design:
  the API surface doesn't change, only the target. For Ch02 (Harness
  Engineering): `target-repo` is the key field to document for teams moving
  from single-repo to multi-repo operations.

### Claim 2: Without `target-repo`, all safe outputs operate on the workflow's own repository — the parameter is opt-in, not the default

- **Evidence**: The page's Cross-Repository Safe Outputs table includes the
  note: "**Without `target-repo`, these safe outputs operate on the repository
  where the workflow is running.**" This is emphasized in the table footer.
- **Confidence**: settled (first-party documentation; explicitly stated)
- **Quote**: "Without `target-repo`, these safe outputs operate on the
  repository where the workflow is running."
- **Our assessment**: The opt-in design means single-repo workflows are not
  accidentally affected by the multi-repo configuration. It also means
  practitioners who want cross-repo behavior must explicitly declare it, making
  the intent visible in the workflow spec. For Ch02: this is a safe default
  that requires no action for single-repo use cases.

### Claim 3: The default `GITHUB_TOKEN` is scoped to the current repository only — cross-repo operations silently fail without additional authentication configuration

- **Evidence**: The page's "Teaching Agents Multi-Repo Access" section includes
  a prominent caution: "When reading from repositories other than the workflow's
  repository, you must configure additional authentication. The default
  `GITHUB_TOKEN` only has access to the current repository. Use a PAT, GitHub
  App token, or the magic secret `GH_AW_GITHUB_MCP_SERVER_TOKEN`."
- **Confidence**: settled (this is a documented constraint of the GitHub
  Actions platform itself, not a gh-aw-specific design choice)
- **Quote**: "The default `GITHUB_TOKEN` only has access to the current
  repository."
- **Our assessment**: This is the primary footgun for cross-repo agent
  workflows. An agent that queries multiple repositories via GitHub toolsets
  will silently receive empty or unauthorized results without noticing the
  authentication failure. The failure mode is silent — no error, just missing
  data — which makes this particularly dangerous for orchestration workflows
  that need to scan or read from many repos. For Ch03 (Safety and
  Verification): document this as a required pre-flight check for any workflow
  using the `github` toolset with cross-repo reads.

### Claim 4: Hub-and-spoke is the canonical topology where component repositories forward tracking issues to a central coordination repository via `target-repo`

- **Evidence**: The Common MultiRepoOps Patterns table defines Hub-and-spoke as:
  "Each component workflow creates tracking issues in a central repo via
  `target-repo`." The example configuration shows a workflow triggered on
  issue events, with `safe-outputs.create-issue.target-repo: "org/tracking-repo"`
  and a `title-prefix: "[component-a] "` to namespace the issue in the central
  tracker.
- **Confidence**: settled (first-party documentation with a complete YAML
  example)
- **Quote**: "Each component workflow creates tracking issues in a central repo
  via `target-repo`"
- **Our assessment**: Hub-and-spoke is the simplest topology — each component
  repo runs its own workflow that writes to one shared destination. The
  `title-prefix` convention is important: without consistent namespacing,
  the central tracker becomes unreadable when many components forward to it.
  For Ch06 (Orchestration): the hub-and-spoke pattern is the entry point for
  multi-repo coordination — minimal infrastructure, each component independently
  operable.

### Claim 5: Upstream-to-downstream is the topology where the main repository propagates changes to sub-repositories using `create-pull-request` with `target-repo` per downstream

- **Evidence**: The Common MultiRepoOps Patterns table defines
  Upstream-to-downstream as: "Main repo propagates changes using
  `create-pull-request` with `target-repo` per downstream." This is listed as
  a distinct pattern from hub-and-spoke, with the directionality reversed —
  the main repo writes out rather than components writing in.
- **Confidence**: settled (first-party documentation; pattern is named and
  described in the table)
- **Quote**: "Main repo propagates changes using `create-pull-request` with
  `target-repo` per downstream"
- **Our assessment**: This topology maps to scenarios like shared library
  updates, security patch rollouts, or standard configuration enforcement. The
  PRs created in downstream repos go through the normal human review process
  there — the automation generates the change proposal, not the merge decision.
  For Ch06: upstream-to-downstream is the topology for "one source of truth
  → many consumers" scenarios.

### Claim 6: Org-wide broadcast is the topology where a single workflow creates issues in many repositories up to a configured `max` limit

- **Evidence**: The Common MultiRepoOps Patterns table defines Org-wide
  broadcast as: "Single workflow creates issues in many repos up to the
  configured `max` limit." This references the same `max` parameter documented
  in CentralRepoOps for bounding fan-out.
- **Confidence**: settled (first-party documentation)
- **Quote**: "Single workflow creates issues in many repos up to the configured
  `max` limit"
- **Our assessment**: The `max` limit reference is key — without it, a
  single workflow could create issues in every repo in the organization
  simultaneously. The `max` parameter provides the blast radius bound. For
  Ch06: org-wide broadcast combined with `max` is the pattern for policy
  enforcement or announcement workflows that must reach all repos but should
  not run unchecked.

### Claim 7: PAT authentication for cross-repo operations should be scoped to read on the source repo and write only on target repos — not bidirectional write access

- **Evidence**: The "Personal Access Token (PAT)" subsection states: "The PAT
  needs permissions only on target repositories — `contents: write`,
  `issues: write`, or `pull-requests: write` depending on operations (not on
  the source repo)." The "Security Best Practice" callout adds: "If you only
  need to read from one repo and write to another, scope your PAT to have read
  access on the source and write access only on target repositories."
- **Confidence**: settled (first-party security guidance; the permission scope
  is deterministic for the described operations)
- **Quote**: "If you only need to read from one repo and write to another,
  scope your PAT to have read access on the source and write access only on
  target repositories."
- **Our assessment**: This is the least-privilege principle applied to
  cross-repo PAT configuration. Many practitioners would create a PAT with
  write access on all repos involved; the guidance explicitly restricts write
  to the target only. For Ch03: this is the reference scope guidance for any
  cross-repo PAT. Pair with the CentralRepoOps three-token model
  (`docs-ghaw-central-repo-ops.md` Claim 3) as complementary least-privilege
  references.

### Claim 8: GitHub App Installation Tokens are preferred over PATs for cross-repo operations due to per-job minting and automatic revocation

- **Evidence**: The "GitHub App Installation Token" subsection lists four
  advantages over PATs: "Per-job minting", "Automatic revocation after job
  completion", "Fine-grained permissions", and "Better attribution than
  long-lived PATs." The page links to an auth reference page for complete
  configuration details.
- **Confidence**: settled (first-party recommendation; the advantages listed
  are platform-level properties of GitHub App tokens, not opinions)
- **Quote**: "Per-job minting" / "Automatic revocation after job completion"
- **Our assessment**: The four advantages make GitHub Apps strictly better
  than PATs on every security dimension: shorter-lived (per-job vs. indefinite),
  automatically revoked (no manual rotation), scoped to specific installations
  (not broad org access), and attributable to an app identity (not a user).
  The practical barrier is setup cost — GitHub Apps require org admin
  configuration. For Ch03: recommend GitHub Apps as the default for production
  cross-repo workflows, with PATs acceptable for development/testing or
  single-developer contexts.

### Claim 9: The `GH_AW_GITHUB_MCP_SERVER_TOKEN` magic secret enables cross-repository reads via GitHub toolsets without a separately-configured PAT

- **Evidence**: The "Teaching Agents Multi-Repo Access" caution names three
  options for cross-repo read auth: "Use a PAT, GitHub App token, or the magic
  secret `GH_AW_GITHUB_MCP_SERVER_TOKEN`." The toolset configuration example
  shows `github-token: ${{ secrets.CROSS_REPO_PAT }}` as the explicit form;
  the magic secret is presented as an alternative.
- **Confidence**: emerging (named in documentation but the documentation defers
  to an unfetched reference page for full mechanics; the exact scope and setup
  of `GH_AW_GITHUB_MCP_SERVER_TOKEN` are not detailed on this page)
- **Quote**: "Use a PAT, GitHub App token, or the magic secret
  `GH_AW_GITHUB_MCP_SERVER_TOKEN`."
- **Our assessment**: The "magic secret" naming implies this is a gh-aw
  platform-provisioned token rather than one the user configures — a
  convenience credential for the common case of cross-repo reads in the
  GitHub toolset. The emerging confidence reflects that the full mechanics
  (how it's provisioned, its actual scope, whether it works across orgs) are
  not described on this page. For Ch02: document as an option for simplifying
  cross-repo read configuration, with a note that the full auth reference page
  should be consulted for production use.

### Claim 10: MultiRepoOps (component-initiated, event-driven) is architecturally distinct from CentralRepoOps (control-plane-initiated, orchestrator-dispatched)

- **Evidence**: The page positions MultiRepoOps as event-driven coordination
  from component repositories, where each component repo has its own workflow
  that writes to a central destination. CentralRepoOps (documented in
  `docs-ghaw-central-repo-ops.md`) uses a central control plane that
  orchestrates workers dispatched to target repos. The Related section links
  to IssueOps, ChatOps, and Orchestration as companion patterns — Orchestration
  being CentralRepoOps's home.
- **Confidence**: emerging (architectural distinction is implied by the pattern
  structure; the page does not explicitly compare the two in a side-by-side
  analysis)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The architectural distinction matters for choosing the
  right pattern: MultiRepoOps is bottom-up (component repos push to a central
  destination on their own triggers), CentralRepoOps is top-down (a central
  orchestrator pushes workers out to target repos on a schedule or event). For
  org-wide rollouts of a standard configuration, CentralRepoOps is correct —
  one orchestrator coordinates everything. For ongoing coordination between
  existing component repos, MultiRepoOps is correct — each component continues
  to own its own automation. For Ch06: document both patterns with explicit
  guidance on when to use each.

## Concrete Artifacts

### Cross-Repo Issue Tracker — Complete Workflow Example

From the MultiRepoOps documentation, "Example Configuration" section.

```yaml
---
on:
  issues:
    types: [opened, labeled]
permissions:
  contents: read
  actions: read
safe-outputs:
  github-token: ${{ secrets.GH_AW_CROSS_REPO_PAT }}
  create-issue:
    target-repo: "org/tracking-repo"
    title-prefix: "[component-a] "
    labels: [tracking, multi-repo]
---
# Cross-Repo Issue Tracker
When issues are created in component repositories, automatically create tracking issues in the central coordination repo.
Analyze the issue and create a tracking issue that:
- Links back to the original component issue
- Summarizes the problem and impact
- Tags relevant teams across the organization
- Provides context for cross-component coordination
```

*Source: MultiRepoOps documentation, "Example Configuration" section*

### Cross-Repo GitHub Toolset Authentication

From the MultiRepoOps documentation, "Teaching Agents Multi-Repo Access" section.

```yaml
tools:
  github:
    toolsets: [repos, issues, pull_requests, actions]
    github-token: ${{ secrets.CROSS_REPO_PAT }}  # Required for cross-repo reading
```

*Source: MultiRepoOps documentation, "Teaching Agents Multi-Repo Access" section*

### Deterministic Multi-Repo Checkout

From the MultiRepoOps documentation, "Deterministic Multi-Repo Workflows" section.
Note: source documentation shows `actions/checkout@v6`, which is ahead of current
stable (v4) — reproduced as-is from the source page (see Extraction Notes).

```yaml
---
engine:
  id: claude
steps:
  - name: Checkout main repo
    uses: actions/checkout@v6
    with:
      path: main-repo
  - name: Checkout secondary repo
    uses: actions/checkout@v6
    with:
      repository: org/secondary-repo
      token: ${{ secrets.GH_AW_CROSS_REPO_PAT }}
      path: secondary-repo
  - name: Compare and sync
    run: |
      # Deterministic sync logic
      rsync -av main-repo/shared/ secondary-repo/shared/
      cd secondary-repo
      git add .
      git commit -m "Sync from main repo"
      git push
---
# Deterministic Feature Sync
Workflow that directly checks out multiple repos and synchronizes files.
```

*Source: MultiRepoOps documentation, "Deterministic Multi-Repo Workflows" section*

### Common MultiRepoOps Patterns Table

From the MultiRepoOps documentation, "Common MultiRepoOps Patterns" section.

```
Pattern               | Description
--------------------- | -------------------------------------------------
Hub-and-spoke         | Each component workflow creates tracking issues
                      | in a central repo via `target-repo`
Upstream-to-downstream| Main repo propagates changes using
                      | `create-pull-request` with `target-repo` per downstream
Org-wide broadcast    | Single workflow creates issues in many repos
                      | up to the configured `max` limit
```

*Source: MultiRepoOps documentation, "Common MultiRepoOps Patterns" section*

### Cross-Repository Safe Outputs Support Matrix

From the MultiRepoOps documentation, "Cross-Repository Safe Outputs" section.

```
Safe Output           | Cross-Repo Support | Example Use Case
--------------------- | ------------------ | ------------------------------------
create-issue          | ✓                  | Create tracking issues in central repo
add-comment           | ✓                  | Comment on issues in other repos
update-issue          | ✓                  | Update issue status across repos
add-labels            | ✓                  | Label issues in target repos
create-pull-request   | ✓                  | Create PRs in downstream repos
create-discussion     | ✓                  | Create discussions in any repo
create-agent-session  | ✓                  | Create tasks in target repos
update-release        | ✓                  | Update release notes across repos

Default behavior (no target-repo): all safe outputs operate on the workflow's own repo.
```

*Source: MultiRepoOps documentation, "Cross-Repository Safe Outputs" section*

### GitHub App vs. PAT Comparison

From the MultiRepoOps documentation, "GitHub App Installation Token" subsection.

```
GitHub App Installation Token advantages over PAT:
  - Per-job minting
  - Automatic revocation after job completion
  - Fine-grained permissions
  - Better attribution than long-lived PATs

PAT least-privilege scope (security best practice):
  - Source repo: read only
  - Target repos: write only (contents/issues/pull-requests as needed)
  - NOT bidirectional write access
```

*Source: MultiRepoOps documentation, "Authentication for Cross-Repo Access" section*

### Best Practices (Verbatim)

From the MultiRepoOps documentation, "Best Practices" section.

```
- Use GitHub Apps over PATs for automatic token revocation
- Scope tokens minimally to target repositories
- Set appropriate `max` limits and consistent label/prefix conventions
- Test against public repositories first before rolling out to private or org-wide targets
```

*Source: MultiRepoOps documentation, "Best Practices" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 5 (Safe Outputs as permission-separated
    GitHub operations the AI can request without write permissions): this page
    extends the Safe Outputs model to cross-repository targets. The base
    permission-separation mechanism is the same; `target-repo` adds the
    cross-repo dimension.
  - `docs-ghaw-ephemerals.md` Claim 12 (SideRepoOps): the SideRepoOps pattern
    mentioned there uses the same `target-repo` mechanism on `safe-outputs` to
    write to the main repo from a side repo. MultiRepoOps generalizes this to
    multiple target repos from multiple source repos.
  - `docs-ghaw-central-repo-ops.md` Claim 3 (three-PAT model): the PAT
    least-privilege guidance here (read on source, write on target only) is
    consistent with the three-token model — each token grants minimum permissions
    for its specific cross-repo role.
  - `docs-ghaw-sharing-workflows.md` Claim 7 (`target-repo` and `allowed-repos`
    for cross-repository execution): that note documents the `allowed-repos`
    allowlist as a companion blast-radius control to `target-repo`; this page
    focuses on the `target-repo` routing parameter. Together they give the full
    cross-repo safe-output configuration picture.

- **Extends**:
  - `docs-ghaw-how-they-work.md`: that note covers Safe Outputs at the
    conceptual level (what they are, why no write access by default). This
    page covers the cross-repo application of Safe Outputs — what happens when
    you add `target-repo` to the same primitives.
  - `docs-ghaw-mcps.md`: that note covers MCP authentication for reading from
    external services. This page adds the cross-repo read auth story specifically
    for GitHub repositories (the `GH_AW_GITHUB_MCP_SERVER_TOKEN` and explicit
    `github-token` in toolset config). Together they form the complete picture
    of cross-boundary read authentication in gh-aw.
  - `docs-ghaw-central-repo-ops.md`: that note covers the CentralRepoOps
    Orchestrator+Worker pattern as a top-down fan-out model. This page covers
    the complementary MultiRepoOps bottom-up model. Together they give the two
    primary multi-repo coordination topologies in gh-aw.
  - `blog-gh-aw-operations-release-workflows.md` (Source Context → Scope):
    that source explicitly notes "multi-repo scenarios" as out of scope. This
    source fills that gap — the cross-repo coordination model this blog post
    excluded.

- **Contradicts**: None identified. The cross-repo auth guidance (read on source,
  write on target) is consistent with the three-token model in
  `docs-ghaw-central-repo-ops.md`. The topology descriptions do not conflict
  with any existing source notes.

- **Novel**:
  - **`target-repo` parameter surface as a cross-repo primitive** (Claim 1):
    While `target-repo` is mentioned in `docs-ghaw-central-repo-ops.md`'s
    worker YAML artifacts, its role as the primary cross-repo coordination
    primitive — and the full list of eight supported safe-output types — is
    documented here for the first time as a first-class topic.
  - **Three topology archetypes with names** (Claims 4–6): Hub-and-spoke,
    upstream-to-downstream, and org-wide broadcast as a named taxonomy for
    multi-repo coordination patterns are new to the corpus. CentralRepoOps
    covers one topology (top-down orchestration); this page names two more.
  - **PAT least-privilege scope for cross-repo** (Claim 7): The explicit
    "read on source, write on target only" guidance is new. Prior PAT guidance
    in the corpus (three-token model) covers role separation; this page adds
    the directional read/write scope constraint.
  - **`GH_AW_GITHUB_MCP_SERVER_TOKEN` magic secret** (Claim 9): Not mentioned
    in any existing source note. A platform-provisioned convenience token for
    cross-repo GitHub toolset reads.
  - **MultiRepoOps vs. CentralRepoOps architectural distinction** (Claim 10):
    The bottom-up vs. top-down framing is not drawn explicitly in any existing
    source note. This is a decision-aid for choosing between the two patterns.
  - **Safe-output cross-repo support matrix** (eight types, all supporting
    `target-repo`): Concrete and enumerative; not present in any existing note.

## Guide Impact

### Chapter 06: Orchestration and Multi-Agent Coordination

- **Add `target-repo` as the foundational cross-repo coordination primitive**
  (Claim 1): The guide should explain `target-repo` as the key safe-output
  parameter before introducing the topology archetypes. It is the mechanism
  underlying all three patterns.

- **Add three topology archetypes with selection guidance** (Claims 4–6):
  Hub-and-spoke for event-driven component → central tracking. Upstream-to-downstream
  for propagating changes from one source to many consumers. Org-wide broadcast
  for policy enforcement or announcements. Cross-reference CentralRepoOps as
  the fourth topology (top-down orchestrator pattern from
  `docs-ghaw-central-repo-ops.md` Claim 1).

- **Add MultiRepoOps vs. CentralRepoOps decision guidance** (Claim 10):
  Bottom-up component coordination (MultiRepoOps) vs. top-down control-plane
  orchestration (CentralRepoOps). Selection criterion: does the coordination
  flow from individual components to a center (MultiRepoOps), or from a central
  plan to individual repos (CentralRepoOps)?

### Chapter 03: Safety and Verification

- **Add `GITHUB_TOKEN` repo-scope footgun as a cross-repo pre-flight check**
  (Claim 3): Any workflow that uses the `github` toolset to query repositories
  beyond its own must configure explicit cross-repo authentication. Silent
  failure (empty results, not errors) makes this especially dangerous for
  orchestration workflows.

- **Add PAT least-privilege scope guidance for cross-repo** (Claim 7):
  Cross-repo PATs should be scoped to read on the source and write only on
  target repositories. Pair with the three-token model from
  `docs-ghaw-central-repo-ops.md` Claim 3 as complementary least-privilege
  references for different complexity levels.

- **Recommend GitHub Apps over PATs for production cross-repo workflows**
  (Claim 8): Per-job minting and automatic revocation eliminate the static
  secret rotation burden. PATs remain appropriate for development and
  single-developer contexts.

### Chapter 02: Harness Engineering

- **Add safe-output cross-repo support matrix** (Claims 1–2): Document the
  eight supported safe-output types with their `target-repo` behavior. Note
  that the default (no `target-repo`) is same-repo operation — cross-repo is
  always opt-in.

- **Document `GH_AW_GITHUB_MCP_SERVER_TOKEN` as the lightweight cross-repo
  read option** (Claim 9): For workflows that only need cross-repo reads via
  GitHub toolsets without full PAT configuration, this magic secret is the
  lower-friction path. Note that full mechanics require consulting the gh-aw
  auth reference.

## Extraction Notes

1. **`actions/checkout@v6` in deterministic workflow YAML**: The source
   documentation uses `actions/checkout@v6` in the multi-checkout example.
   This is ahead of the current stable release (v4). The YAML block in
   Concrete Artifacts reproduces the source as-is, with a parenthetical note.
   If the source page is updated to v4 or a later stable release, the artifact
   should be updated accordingly.

2. **`GH_AW_GITHUB_MCP_SERVER_TOKEN` mechanics not fully documented on this
   page**: The magic secret is named in the caution callout but the source
   defers to an unfetched reference page for complete configuration. Assessed
   as `emerging` for this reason. A dedicated source note on the gh-aw auth
   reference page would fill this gap.

3. **MultiRepoOps vs. CentralRepoOps distinction is structural, not
   explicit**: The page does not include a side-by-side comparison of the two
   patterns. The architectural distinction (Claims 10) is inferred from the
   topology descriptions and the position of each page in the patterns
   reference. Assessed as `emerging`.

4. **Sub-pages not followed**: The page links to "Feature Synchronization" and
   "Cross-Repo Issue Tracking" example pages, plus the Cross-Repository
   Operations reference and the GitHub App auth guide. These were not fetched —
   they appear to be extended examples rather than conceptual additions. A
   future note on the Cross-Repository Operations reference page may surface
   additional `target-repo` configuration details.

5. **No explicit publication date**: The documentation does not carry a
   publication date. Content is consistent with gh-aw platform behavior post-
   December 2025 based on the `safe-outputs` API surface described.

6. **No contradictions to file**: Reviewed all existing corpus source notes.
   No claims in this source materially oppose existing source notes. The PAT
   scope guidance is consistent with (and extends) the three-token model in
   `docs-ghaw-central-repo-ops.md`. No contradiction issue filed.
