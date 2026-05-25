---
source_url: https://github.github.com/gh-aw/reference/github-tools
source_type: docs
title: "GitHub Agentic Workflows: GitHub Tools Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: emerging
issue: "#396"
---

# GitHub Agentic Workflows: GitHub Tools Reference

> The authoritative reference for `tools.github` in gh-aw workflows — documents
> the 18-toolset catalogue (with `default` and `all` shorthands), the three
> transport modes (`local`, `remote`, `gh-proxy`), the default read scope across
> public and current repositories, authentication options for private/cross-org
> access including the `GH_AW_GITHUB_MCP_SERVER_TOKEN` magic secret, and the
> `dependabot` toolset's explicit opt-in requirement and non-standard permission
> prerequisites.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/github-tools` page —
  in the "Reference" section alongside `reference/permissions`, `reference/integrity`,
  `reference/tools`. This is the dedicated reference for `tools.github` configuration,
  complementing `reference/tools` which covers all twelve built-in tool types at a
  higher level of abstraction.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same
  team behind Peli de Halleux's agent factory blog series and the `gh aw` CLI. Toolset
  names, transport mode descriptions, authentication requirements, and default values
  are settled platform facts. Claims about cross-repo access constraints are
  authoritative for the `gh-aw` platform and reflect the underlying GitHub Actions
  `GITHUB_TOKEN` scoping model.
- **Scope**: Complete reference for `tools.github` configuration — the 18-toolset
  catalogue, two shorthand values (`default`, `all`), three transport modes (`local`,
  `remote`, `gh-proxy`), the default repository access scope, three authentication
  options for additional access (PAT, GitHub App, magic secret), and the `dependabot`
  toolset's explicit opt-in requirement with its specific non-standard permissions.
  Does NOT cover: integrity filtering sub-configuration (`tools.github.min-integrity`
  and related fields — see `docs-ghaw-integrity-reference.md`), the broader built-in
  tool catalogue (`reference/tools` — see `docs-ghaw-tools-reference.md`), or the
  permissions model (`reference/permissions` — see `docs-ghaw-permissions-reference.md`).

## Extracted Claims

### Claim 1: GitHub Tools are included by default in every gh-aw workflow, so no configuration of `tools.github` is necessary for the common case

- **Evidence**: The page opens with a direct statement about the default inclusion,
  establishing that practitioners do not need to add `tools.github` to their workflow
  frontmatter to get GitHub API read access via the five default toolsets.
- **Confidence**: settled (first-party documentation; the default-inclusion behavior
  is an explicit platform design choice, not a user configuration)
- **Quote**: "In most workflows, no configuration of the GitHub Tools is necessary
  since they are included by default with the default toolsets."
- **Our assessment**: This default-on design means the cost of basic GitHub read
  access (issues, PRs, repos, users, context) is zero configuration. The five
  default toolsets (`context`, `repos`, `issues`, `pull_requests`, `users`) cover
  the most common agent use cases — triaging issues, reviewing PRs, reading repo
  metadata. Practitioners only need to touch `tools.github` when they need a
  non-default toolset (e.g., `discussions`, `actions`, `projects`), a different
  transport mode, or additional authentication. For Ch02 (Harness Engineering): do
  not instruct practitioners to add `tools.github: {}` to every workflow — it is
  already there. Document it as opt-in configuration for non-default behavior.

### Claim 2: 18 toolsets are available, organized into a complete catalogue, with `dependabot` excluded from the `all` shorthand and requiring explicit opt-in

- **Evidence**: The page lists 18 toolsets by name: `context`, `repos`, `issues`,
  `pull_requests`, `users`, `actions`, `code_security`, `discussions`, `labels`,
  `notifications`, `orgs`, `projects`, `gists`, `search`, `dependabot`,
  `experiments`, `secret_protection`, `security_advisories`. Two shorthands:
  `default` expands to the five standard toolsets; `all` expands to all toolsets
  "except `dependabot`", which "must be opted into explicitly."
- **Confidence**: settled (first-party documentation; the toolset names and shorthand
  expansions are explicitly enumerated)
- **Quote**: (no single contiguous quote covers the full catalogue; see Concrete
  Artifacts for the complete enumeration)
- **Our assessment**: The `dependabot` opt-out from `all` is the most significant
  design decision in the toolset catalogue. It means a workflow using `toolsets: all`
  does not get vulnerability alert access — a practitioner who wants `dependabot`
  data in their agent must declare it explicitly. The rationale is the non-standard
  permission requirements (`vulnerability-alerts: read` and `security-events: read`),
  which are not part of the standard GITHUB_TOKEN permission set and must be
  explicitly requested. The `experiments` and `secret_protection` toolsets are
  similarly non-default — they are named but not in the default set or `all`. For
  Ch02: document the 18-toolset taxonomy as the complete GitHub API surface available
  to gh-aw agents. `default` is the right starting point for most workflows;
  `all` expands access but excludes `dependabot`. Explicitly name `dependabot` as
  the one toolset that requires both explicit declaration AND non-standard
  permissions.

### Claim 3: Three transport modes control how GitHub API calls are made — `local` (Docker MCP server, default), `remote` (hosted MCP server), and `gh-proxy` (pre-authenticated `gh` CLI) — with `gh-proxy` preferred for performance and required for integrity reactions

- **Evidence**: The page documents three modes in a table:
  - `local` (default): "Docker-based GitHub MCP Server inside the Actions VM" with
    "No extra authentication required"
  - `remote`: "Hosted GitHub MCP Server managed by GitHub" with "Requires additional
    authentication"
  - `gh-proxy`: "Pre-authenticated `gh` CLI directly (no MCP server)" described as
    "Preferred for performance; required for integrity reactions"
- **Confidence**: settled (first-party documentation; mode names, transport descriptions,
  and notes are explicitly stated)
- **Quote**: "Preferred for performance; required for integrity reactions" (describing
  `gh-proxy` mode)
- **Our assessment**: The three-mode architecture reveals a significant design coupling:
  if a workflow uses reaction-based integrity endorsement (`features.integrity-reactions:
  true`, documented in `docs-ghaw-integrity-reference.md` Claim 9), it MUST use
  `gh-proxy` mode — there is no choice. This is a constraint not documented in the
  integrity reference itself. The performance advantage of `gh-proxy` is that it
  bypasses the Docker MCP Server container (used in `local` mode) and the hosted
  server round-trip (used in `remote` mode), making direct `gh` CLI calls instead.
  `remote` mode may be preferred when the Docker container startup cost is
  prohibitive or when the hosted server offers capabilities not available locally.
  For Ch02: when documenting `gh-proxy`, name the integrity reactions dependency
  explicitly — practitioners who want to use reaction-based endorsement must set
  `mode: gh-proxy`. For Ch03: the transport mode is a security-adjacent decision
  because `local` mode requires no additional auth (relying on the Actions VM's
  built-in credentials), while `remote` mode introduces an external dependency on
  GitHub-hosted infrastructure.

### Claim 4: By default, GitHub Tools can read from the current repository and all public repositories — private repository access requires additional authentication

- **Evidence**: The page states the default scope of GitHub Tools read access
  explicitly, naming the network firewall as a conditional constraint on public
  repository access.
- **Confidence**: settled (first-party documentation; this is a GitHub Actions
  `GITHUB_TOKEN` scoping constraint, not a gh-aw-specific design)
- **Quote**: "By default, the GitHub Tools can read from the current repository
  and all public repositories (if permitted by the network firewall)."
- **Our assessment**: The default scope (current repo + all public repos) is larger
  than most practitioners expect. A workflow that reads public repositories needs no
  additional authentication — the default `GITHUB_TOKEN` and network configuration
  handle it. The constraint is on private repositories: any private repo other than
  the workflow's own requires additional authentication (PAT, GitHub App token, or
  magic secret). This is the precise scoping rule that explains why
  `docs-ghaw-multi-repo-ops.md` Claim 3 warns about the "GITHUB_TOKEN only has
  access to the current repository" — that claim is specifically about private
  cross-repo access, not public repositories. The network firewall caveat matters
  for enterprise gh-aw deployments where egress is restricted; in those cases, even
  public repos may be inaccessible without network allowlist configuration (see
  `docs-ghaw-network-reference.md`). For Ch02: clarify the access scope in the
  harness documentation — default is current + public, not just current. For Ch03:
  the public-repo read access without additional auth is a potential data exposure
  concern for organizations with strict information security policies.

### Claim 5: The `GH_AW_GITHUB_MCP_SERVER_TOKEN` magic secret provides cross-repo authentication for GitHub Tools without requiring explicit workflow references — setting the secret is sufficient

- **Evidence**: The page documents the magic secret as a PAT option that "does not
  need to be explicitly referenced in your workflow" — the practitioner sets it via
  the `gh aw secrets set` CLI and it is automatically used by the GitHub Tools.
- **Confidence**: settled (first-party documentation; the magic secret name, setup
  command, and auto-use behavior are explicitly described)
- **Quote**: "does not need to be explicitly referenced in your workflow"
- **Our assessment**: The "magic" in the magic secret is the auto-use behavior: the
  practitioner does not write `github-token: ${{ secrets.GH_AW_GITHUB_MCP_SERVER_TOKEN }}`
  in the workflow — they just set the secret name and it is automatically picked up
  by the GitHub Tools runtime. This is the lowest-friction path for adding cross-repo
  read access: no workflow changes required, just a one-time `gh aw secrets set`
  command. The trade-off is reduced transparency — a workflow with no visible
  `github-token:` configuration may still be using a PAT via this mechanism, which
  could be surprising during security reviews. This also corroborates and extends
  `docs-ghaw-multi-repo-ops.md` Claim 9, which named the magic secret as an option
  for cross-repo reads without fully explaining the "no explicit reference needed"
  mechanism. For Ch02: document the magic secret as the lowest-friction option for
  adding cross-repo read capability. Recommend explicit `github-token:` references
  for production workflows where auditability is important.

### Claim 6: The `dependabot` toolset requires two non-standard permissions — `vulnerability-alerts: read` and `security-events: read` — now supported natively by `GITHUB_TOKEN`

- **Evidence**: The page documents the specific permissions required for the
  `dependabot` toolset, with the note that these permissions have been added to the
  standard `GITHUB_TOKEN` capabilities.
- **Confidence**: settled (first-party documentation; the permission names and their
  current GITHUB_TOKEN support are explicitly stated)
- **Quote**: "now supported natively by `GITHUB_TOKEN`"
- **Our assessment**: The note that `vulnerability-alerts: read` and
  `security-events: read` are "now supported natively by `GITHUB_TOKEN`" implies
  a historical context where they were not — practitioners had to use a PAT or
  GitHub App token to access Dependabot data. The current state: these permissions
  are available to GITHUB_TOKEN but must still be explicitly requested in the
  `permissions:` frontmatter section. The `dependabot` toolset is the only toolset
  in the catalogue with documented non-standard permission prerequisites — all other
  toolsets operate within the standard ten read scopes documented in
  `docs-ghaw-permissions-reference.md` Claim 4. For Ch02: when documenting the
  `dependabot` toolset, always pair it with the required permissions declaration —
  a workflow that declares `toolsets: [dependabot]` without the permissions block
  will fail at runtime. For security automation workflows: this is the mechanism
  for agents that need to read vulnerability alerts, make recommendations, or
  automate Dependabot PR triage.

### Claim 7: Configuring a custom toolset list via `toolsets:` replaces the default five toolsets — the `default` shorthand must be included explicitly if the defaults are still needed alongside custom toolsets

- **Evidence**: The page provides a configuration example showing that `toolsets`
  accepts an array of toolset names, and documents that `default` is a shorthand
  expanding to the standard five. The design implies that specifying custom toolsets
  replaces rather than augments the default set.
- **Confidence**: settled (first-party documentation; the YAML example explicitly
  shows selected toolsets, and the `default` shorthand's purpose implies this behavior)
- **Quote**: (no direct quote; the replacement behavior is implied by the shorthand
  documentation and YAML example — see Concrete Artifacts)
- **Our assessment**: This is a footgun for practitioners who add a custom toolset
  expecting the defaults to remain active. Adding `toolsets: [actions]` to get
  GitHub Actions API access likely removes `issues` and `pull_requests` access —
  the agent can no longer see issues unless the practitioner includes `default`
  in the array (`toolsets: [default, actions]` or explicitly lists all needed
  toolsets). The `default` shorthand's value is exactly this composability — it
  lets practitioners extend the default set without enumerating all five standard
  toolsets. For Ch02: always use `toolsets: [default, ...]` when adding toolsets
  rather than replacing them with a standalone list. Document the replacement
  semantics as a required-reading note.

## Concrete Artifacts

### Complete 18-Toolset Catalogue (from reference page)

```
Available toolsets:

STANDARD (in default set):
  context         — Repository and workflow context
  repos           — Repository operations
  issues          — Issue management
  pull_requests   — Pull request management
  users           — User information

EXTENDED (require explicit toolset declaration):
  actions         — GitHub Actions workflow operations
  code_security   — Code security features
  discussions     — GitHub Discussions
  labels          — Label management
  notifications   — Notification management
  orgs            — Organization data
  projects        — GitHub Projects
  gists           — GitHub Gists
  search          — Search operations
  experiments     — Experimental features
  secret_protection — Secret protection features
  security_advisories — Security advisories

OPT-IN ONLY (excluded from 'all' shorthand):
  dependabot      — Dependabot vulnerability alerts and security events
                    Requires: vulnerability-alerts: read + security-events: read

SHORTHANDS:
  default         → context, repos, issues, pull_requests, users
  all             → all toolsets EXCEPT dependabot
```

*Source: gh-aw reference/github-tools, "Available Toolsets" section*

### Three Transport Modes (from reference page)

```
Mode        Transport                                           Notes
----------- ------------------------------------------------- --------------------------------
local       Docker-based GitHub MCP Server inside the          No extra authentication required
(default)   Actions VM
remote      Hosted GitHub MCP Server managed by GitHub         Requires additional authentication
gh-proxy    Pre-authenticated `gh` CLI directly                Preferred for performance;
            (no MCP server)                                    required for integrity reactions
```

*Source: gh-aw reference/github-tools, "GitHub Tools Access Modes" section*

### Toolset Configuration Examples (from reference page)

```yaml
# Custom toolset selection (REPLACES default set):
tools:
  github:
    toolsets: [repos, issues, pull_requests, actions]

# Extend defaults without losing them:
tools:
  github:
    toolsets: [default, actions]

# Remote mode with explicit token:
tools:
  github:
    mode: remote
    github-token: ${{ secrets.CUSTOM_PAT }}

# gh-proxy mode (required for integrity reactions):
tools:
  github:
    mode: gh-proxy
```

*Source: gh-aw reference/github-tools, "Default Configuration" and "GitHub Tools Access Modes" sections*

### Authentication Options for Cross-Repo and Private Repo Access

```
Option                              How it works
---                                 ---
PAT (github-token: in workflow)     Explicit reference in workflow YAML:
                                    github-token: ${{ secrets.CUSTOM_PAT }}

GitHub App Installation Token       Per-job minting, automatic revocation,
                                    fine-grained permissions

GH_AW_GITHUB_MCP_SERVER_TOKEN      "Magic secret": set once via CLI, auto-used
(magic secret)                      without explicit workflow reference.
                                    Setup: gh aw secrets set GH_AW_GITHUB_MCP_SERVER_TOKEN \
                                           --value "<your-pat-token>"
                                    "does not need to be explicitly referenced
                                    in your workflow"
```

*Source: gh-aw reference/github-tools, "Default Repository Access" and "Magic Secret for Authentication" sections*

### Dependabot Toolset Permissions (from reference page)

```yaml
# Required permissions for dependabot toolset:
permissions:
  vulnerability-alerts: read
  security-events: read

# With toolset declaration:
tools:
  github:
    toolsets: [default, dependabot]
```

*Source: gh-aw reference/github-tools, "Dependabot Toolset Requirements" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-multi-repo-ops.md` Claim 3 (default GITHUB_TOKEN scoped to current
    repo only; cross-repo reads require additional auth): Claim 4 here documents the
    precise default scope — "the current repository and all public repositories" —
    which extends the multi-repo note's caution to clarify that public repos are
    accessible without additional auth, but private repos are not. Together, the
    two notes give the complete cross-repo access picture: public = default; private
    = requires explicit auth.
  - `docs-ghaw-multi-repo-ops.md` Claim 9 (GH_AW_GITHUB_MCP_SERVER_TOKEN magic
    secret enables cross-repo reads via GitHub toolsets): Claim 5 here explains the
    "does not need to be explicitly referenced in your workflow" mechanic that the
    multi-repo note named but did not fully explain. This is the authoritative source
    for the magic secret's auto-use behavior.
  - `docs-ghaw-integrity-reference.md` Claim 9 (reaction-based endorsement v0.68.2+
    via `features.integrity-reactions: true`): Claim 3 here adds the transport
    constraint: `gh-proxy` mode is "required for integrity reactions." The integrity
    reference documents the feature but not the transport dependency; this reference
    documents the transport dependency but not the feature details. Together they give
    the complete picture: enable `features.integrity-reactions: true` AND set
    `mode: gh-proxy` or reactions will not function.
  - `docs-ghaw-permissions-reference.md` Claim 6 (GitHub App-Only Permissions require
    additional authentication; page links to `reference/github-tools` for auth setup):
    This source IS the referenced page. The permissions reference sends practitioners
    here for authentication configuration details; this source provides those details
    (PAT, GitHub App, magic secret options).

- **Extends**:
  - `docs-ghaw-tools-reference.md` Claim 9 (`github:` tool provides GitHub API access
    with configurable toolsets, remote/local modes, and authentication — assessed as
    the primary mechanism for reading GitHub state): This source is the complete
    specification for that tool. The tools reference acknowledged the `github:`
    tool's toolset configuration and mode options but deferred to this page (issue
    #396, PR #647) for the full details. This source fills that gap: 18 named
    toolsets, the `default` and `all` shorthands, three mode descriptions, and
    three authentication paths.
  - `docs-ghaw-integrity-reference.md` (integrity filtering as a sub-configuration of
    `tools.github`): This source documents all the other `tools.github` configuration
    fields — toolsets, mode, authentication — alongside which integrity filtering is
    configured. Practitioners configuring `tools.github` will configure both toolsets
    and integrity filtering in the same block; these two notes together give the
    complete `tools.github` surface.
  - `docs-ghaw-multi-repo-ops.md` Claim 9 (GH_AW_GITHUB_MCP_SERVER_TOKEN named as an
    option): This source adds the setup command and the "auto-used without workflow
    reference" behavior that the multi-repo note lacked.

- **Contradicts**: None identified. The public-repo default access documented here
  is complementary to (not in conflict with) `docs-ghaw-multi-repo-ops.md` Claim 3's
  "GITHUB_TOKEN only has access to the current repository" — that claim was specifically
  about private cross-repo access. The transport mode documentation provides factual
  detail that supplements (not contradicts) `docs-ghaw-tools-reference.md` Claim 9's
  assessment that "remote/local modes" govern GitHub API access. No contradiction
  issue required.

- **Novel** (what this note adds that no prior source covers):
  - **Complete 18-toolset catalogue with names**: No existing source note enumerates
    all 18 toolsets. `docs-ghaw-tools-reference.md` Claim 9 names `github:` as a tool
    type but does not list the toolsets. This is the first authoritative catalogue.
  - **`default` and `all` shorthands with their expansions**: No existing source note
    documents that `default` expands to the five standard toolsets or that `all`
    expands to all except `dependabot`.
  - **Three-mode transport architecture**: No existing source note documents the
    `local` / `remote` / `gh-proxy` transport modes with their specific transport
    descriptions (Docker MCP server vs. hosted MCP server vs. `gh` CLI).
  - **`gh-proxy` required for integrity reactions**: No existing source note (including
    `docs-ghaw-integrity-reference.md`) documents the transport mode constraint for
    reaction-based integrity endorsement.
  - **Default read scope includes all public repositories**: No existing source note
    states that the default `GITHUB_TOKEN` within gh-aw enables reading from all
    public repositories, not just the current repo.
  - **`GH_AW_GITHUB_MCP_SERVER_TOKEN` auto-use behavior**: The magic secret's
    "does not need to be explicitly referenced in your workflow" mechanic is novel —
    `docs-ghaw-multi-repo-ops.md` named the secret but did not explain this.
  - **`dependabot` opt-in design and permission prerequisites**: The explicit
    exclusion of `dependabot` from `all`, the requirement to declare it separately,
    and the specific permission prerequisites (`vulnerability-alerts: read`,
    `security-events: read`) are not documented in any existing source note.
  - **Toolset replacement semantics**: The fact that specifying `toolsets:` replaces
    (not augments) the default set, and that `default` must be included explicitly
    to preserve the standard toolsets, is not documented elsewhere.

## Guide Impact

### Chapter 02: Harness Engineering

- **Correct the default-inclusion framing** (Claim 1): The guide should not instruct
  practitioners to add `tools.github: {}` to workflows — it is already there. Document
  `tools.github` configuration as needed only for non-default toolsets, non-default
  transport modes, or additional authentication.

- **Add the 18-toolset catalogue as a GitHub API surface reference** (Claim 2,
  Concrete Artifacts): The complete toolset list is the starting point for
  practitioners designing agents that need specific GitHub API areas. Add the
  `default` and `all` shorthand semantics with the critical note that `all`
  excludes `dependabot`.

- **Document toolset replacement semantics as a footgun** (Claim 7): When
  practitioners customize `toolsets:`, they replace the defaults. Always recommend
  `toolsets: [default, ...]` for extending, not replacing, the standard set.

- **Add `gh-proxy` mode as the recommended mode for integrity-reaction workflows**
  (Claim 3): Any workflow using `features.integrity-reactions: true` must configure
  `mode: gh-proxy` — document this co-requirement explicitly. Even without
  integrity reactions, `gh-proxy` is preferred for performance.

- **Document three authentication options for private/cross-org access** (Claim 5,
  Concrete Artifacts): PAT (explicit, auditable), GitHub App (per-job, preferred for
  production), magic secret (lowest friction, implicit). Add guidance on when to use
  each: magic secret for development/simple cases; GitHub App for production
  cross-repo workflows.

- **Pair `dependabot` toolset documentation with permission prerequisites** (Claim 6):
  A workflow declaring `toolsets: [default, dependabot]` without the permissions block
  will fail at runtime. Always document them together.

### Chapter 03: Safety and Verification

- **Document public-repo default read scope as a security consideration** (Claim 4):
  Practitioners in enterprise environments with strict information security policies
  should be aware that gh-aw agents can read any public repository by default.
  Organizations that want to restrict this should configure network controls (see
  `docs-ghaw-network-reference.md`).

- **Document `GH_AW_GITHUB_MCP_SERVER_TOKEN` transparency trade-off** (Claim 5):
  Workflows using the magic secret have implicit authentication that is not visible
  in the workflow YAML. Recommend explicit `github-token:` references for
  production workflows where security reviewers need to see authentication
  configuration at a glance.

- **Add `gh-proxy` + integrity reactions co-requirement to the integrity filtering
  section** (Claim 3): Ch03's coverage of trust-based input restriction
  (`docs-ghaw-integrity-reference.md`) should note that reaction-based endorsement
  requires `mode: gh-proxy`. A team that enables `features.integrity-reactions: true`
  without setting `gh-proxy` will see silent reaction-based endorsement failures.

### Chapter 04: Multi-Agent Orchestration

- **Cross-repo agent patterns require private-repo auth** (Claim 4): Agents
  orchestrating across multiple repositories must configure authentication for any
  private target. The three authentication options (PAT, GitHub App, magic secret)
  apply. Cross-reference `docs-ghaw-multi-repo-ops.md` for topology patterns and
  `docs-ghaw-central-repo-ops.md` for the three-token model.

## Extraction Notes

1. **Source rendered via two WebFetch calls**: The gh-aw documentation is an
   Astro/Starlight SPA. Two targeted fetches were made — one requesting a full
   verbatim reproduction, one requesting specific technical fields. Quoted text in
   double quotes within the fetched content is assessed as verbatim from the source.
   The transport mode table descriptions were captured with surrounding quotes from
   the second fetch; these are used as quotes in Claims 3 and 5.

2. **Toolset replacement semantics (Claim 7) are inferred from shorthand documentation**:
   The page does not include an explicit "toolsets: replaces defaults" warning. The
   replacement behavior is implied by the `default` shorthand's purpose (if toolsets
   always augmented, the shorthand would be unnecessary). This is assessed as settled
   because it matches standard configuration field semantics in YAML frontmatter
   across gh-aw, but practitioners should test this in a safe environment before
   relying on it.

3. **`experiments` and `secret_protection` toolsets not documented in detail**: The
   page lists these toolsets by name in the catalogue but does not provide
   descriptions of their API surface. They appear to require explicit declaration
   (not in `default` or `all`) but their permission prerequisites are not documented
   on this page.

4. **No publication date**: The documentation page does not carry an explicit
   publication date. Content is consistent with the current gh-aw platform state
   as of 2026-05-25.

5. **No contradictions filed**: Reviewed all existing corpus source notes. No claims
   in this source materially oppose existing notes. The public-repo default access
   scope is complementary to (not in conflict with) the multi-repo note's cross-repo
   auth caution. No contradiction issue required.
