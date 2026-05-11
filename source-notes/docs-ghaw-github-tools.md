---
source_url: https://github.github.com/gh-aw/reference/github-tools
source_type: docs
title: "GitHub Agentic Workflows: GitHub Tools Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#396"
---

# GitHub Agentic Workflows: GitHub Tools Reference

> The authoritative configuration reference for `tools.github` in gh-aw workflows —
> documents the 18-toolset catalog with `default`/`all` shorthands, the `min-integrity`
> content-gating setting, the `allowed-repos` repository scope field with pattern-matching
> rules, three access modes (`local`, `remote`, `gh-proxy`), and authentication options
> for cross-repository reads including the `GH_AW_GITHUB_MCP_SERVER_TOKEN` magic secret.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/github-tools` page — in
  the "Reference" section alongside `reference/permissions` and `reference/network`.
  Reference pages document platform configuration authoritatively; this one specifies the
  complete GitHub toolsets, access modes, repository scoping, and authentication options
  for gh-aw workflows.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same
  team behind Peli de Halleux's agent factory blog series and the `gh aw` CLI.
  Configuration schema, toolset names, access mode behavior, and authentication
  requirements are authoritative for this platform. Claims about platform behavior are
  settled for the `gh aw` system; they do not automatically generalize to other agentic
  frameworks.
- **Scope**: Complete configuration reference for the `tools.github` block in gh-aw
  workflow frontmatter — toolset catalog and shorthands, `min-integrity` content
  filtering, `allowed-repos` repository scoping, three access modes with their transport
  and authentication properties, PAT and GitHub App authentication options, the
  `GH_AW_GITHUB_MCP_SERVER_TOKEN` magic secret, and the `dependabot` toolset's
  special permission requirements. Does NOT cover: the conceptual overview of tool
  integration (see `docs-ghaw-how-they-work.md`), MCP server configuration for external
  tools (see `docs-ghaw-mcps.md`), the Safe Outputs permission model, or cross-repository
  orchestration patterns (see `docs-ghaw-multi-repo-ops.md`).

## Extracted Claims

### Claim 1: The `tools.github` block enables agentic steps to read GitHub data via 18 available toolsets, with `default` and `all` shorthands for common configurations

- **Evidence**: The page documents the full toolset catalog and both shorthand values,
  providing a complete reference for configuring GitHub data access in workflow frontmatter.
- **Confidence**: settled (first-party documentation; toolset names and shorthands are
  authoritative platform specifications)
- **Quote**: (no direct quote; the catalog appears as a list without a lead sentence to
  quote verbatim — see Concrete Artifacts)
- **Our assessment**: The 18 toolsets cover the full breadth of GitHub's object model:
  code (`repos`), collaboration (`issues`, `pull_requests`, `discussions`), user/team
  identity (`context`, `users`, `orgs`), CI/CD (`actions`), security (`code_security`,
  `dependabot`, `secret_protection`, `security_advisories`), metadata (`labels`,
  `notifications`, `projects`, `gists`), and discovery (`search`, `experiments`). The
  `default` shorthand (5 toolsets) covers the daily operational surface; `all` covers
  everything except `dependabot` for broad-access workflows. This complete toolset
  taxonomy is not documented in any existing corpus source note.

### Claim 2: The `default` shorthand expands to exactly five core toolsets — `context`, `repos`, `issues`, `pull_requests`, and `users` — covering the operational requirements of most agentic workflows

- **Evidence**: The page explicitly states: "`default` expands to `context`, `repos`,
  `issues`, `pull_requests`, `users`."
- **Confidence**: settled (first-party documentation; the expansion is explicitly defined)
- **Quote**: "`default` expands to `context`, `repos`, `issues`, `pull_requests`, `users`"
- **Our assessment**: The five-toolset default is well-calibrated for common use cases:
  user/team identity (`context`), code and commit access (`repos`), issue tracking
  (`issues`), PR management (`pull_requests`), and contributor lookup (`users`). Workflows
  that need CI/CD visibility (`actions`), discussion threads (`discussions`), or security
  data (`code_security`) must explicitly add those toolsets. The `default` shorthand
  implements least-privilege by starting with the minimum useful set. For Ch02 (Harness
  Engineering): recommend `toolsets: [default]` as the starting configuration, adding
  specific toolsets only as needed — rather than defaulting to `all`.

### Claim 3: The `all` shorthand includes all toolsets *except* `dependabot`, which must be explicitly added as `[all, dependabot]` and carries additional permission requirements

- **Evidence**: The page states: "`all` includes everything except `dependabot`." A
  separate section documents the additional `vulnerability-alerts: read` and
  `security-events: read` permissions required for the `dependabot` toolset.
- **Confidence**: settled (first-party documentation; the exclusion is explicit)
- **Quote**: "`all` includes everything except `dependabot`"
- **Our assessment**: The explicit exclusion of `dependabot` from `all` reflects a
  deliberate design choice: vulnerability data access requires additional permissions
  beyond the standard `GITHUB_TOKEN` scope. Practitioners who configure `toolsets: [all]`
  without reading this reference will silently not receive dependabot access — the `all`
  shorthand looks complete but is not. For Ch02: document this exclusion prominently as a
  footgun for practitioners who assume `all` means every toolset. For Ch03 (Safety and
  Verification): the `dependabot` toolset's requirement for explicit opt-in is
  security-by-default — vulnerability data is not available to workflows without the
  workflow author declaring it.

### Claim 4: The `min-integrity` setting gates agent access to content by its integrity level; `min-integrity: approved` is automatically applied for public repositories

- **Evidence**: The page states: "Sets the minimum integrity level required for content
  the agent can access. For public repositories, `min-integrity: approved` is applied
  automatically."
- **Confidence**: settled (first-party documentation; default behavior for public repos
  is explicitly stated)
- **Quote**: "For public repositories, `min-integrity: approved` is applied automatically."
- **Our assessment**: The `min-integrity` setting is a content-gating primitive —
  it prevents the agent from accessing repository content below a minimum trust threshold.
  The automatic `approved` enforcement for public repositories means workflows accessing
  public repos via GitHub tools cannot bypass integrity filtering below `approved` level.
  This connects to the defense-in-depth security model from `docs-ghaw-how-they-work.md`
  Claim 3: integrity filtering is a runtime security layer protecting against agents
  reading untrusted content. For Ch03: `min-integrity` is a content-access control layer
  distinct from `permissions:` frontmatter — it constrains *what content* the agent can
  read, while `permissions:` constrains *what API scopes* it can use. The two operate
  independently.

### Claim 5: The `allowed-repos` field controls the repository scope of GitHub tools with four access levels — `"all"`, `"public"`, exact patterns (`"owner/repo"`), and prefix wildcards (`"owner/*"`, `"owner/prefix*"`) — with patterns required to be lowercase and wildcards permitted only at the end of the repository name component

- **Evidence**: The page documents the four values and their semantics. The pattern
  constraint is stated explicitly: "Patterns must be lowercase. Wildcards are only
  permitted at the end of the repository name component."
- **Confidence**: settled (first-party documentation; the schema and pattern rules are
  explicitly specified)
- **Quote**: "Patterns must be lowercase. Wildcards are only permitted at the end of the
  repository name component."
- **Our assessment**: The `allowed-repos` field is a blast-radius control for GitHub
  data access — it limits which repositories the agent can query even if the configured
  token could access more. The "wildcards only at end" constraint prevents overly broad
  patterns like `"*/shared-repo"` that would match across organizations. The combination
  of `min-integrity` and `allowed-repos` gives two independent scope axes: `allowed-repos`
  controls *which repositories* are accessible; `min-integrity` controls *what content
  quality level* within accessible repositories. For Ch02: recommend scoping
  `allowed-repos` to the specific organizations or repository patterns the workflow needs
  rather than defaulting to `"all"`. For Ch03: `allowed-repos: "public"` is the maximum
  restriction for workflows that should only access public data.

### Claim 6: Three access modes exist for GitHub tools — `local` (default, Docker-based MCP Server inside Actions VM), `remote` (hosted by GitHub, requires additional authentication), and `gh-proxy` (pre-authenticated `gh` CLI, preferred for performance and required for integrity reactions)

- **Evidence**: The page documents all three modes in a table with their transport
  mechanisms, notes, and requirements. `gh-proxy` is described as "Preferred for
  performance; required for integrity reactions."
- **Confidence**: settled (first-party documentation; all three modes and their properties
  are explicitly defined)
- **Quote**: "Preferred for performance; required for integrity reactions" (describing
  `gh-proxy` mode)
- **Our assessment**: The three modes serve different deployment contexts. `local` is
  the default — a Docker-based GitHub MCP Server runs inside the Actions VM with no extra
  authentication required. `remote` offloads the MCP server to GitHub's hosted
  infrastructure, which requires additional auth because the token must be forwarded to
  an external service. `gh-proxy` uses the pre-authenticated `gh` CLI already available
  in the Actions runner — avoiding Docker overhead and benefiting from the CLI's built-in
  auth. The "required for integrity reactions" qualifier for `gh-proxy` is notable: certain
  integrity-related operations can only be performed via the `gh` CLI transport, not via
  the Docker MCP or remote modes. For Ch02: document `gh-proxy` as the performance-first
  choice for production workflows, especially those that interact with integrity workflows.
  For Ch03: `remote` mode's additional authentication requirement means the workflow token
  is transmitted to GitHub's hosted infrastructure — practitioners should assess whether
  this is acceptable for their security model.

### Claim 7: GitHub tools default to reading from the current repository and all public repositories; private repository reads beyond the current repository require additional authentication configuration

- **Evidence**: The page states: "By default, the GitHub Tools can read from the current
  repository and all public repositories (if permitted by the network firewall). To read
  from other private repositories, you must configure additional authentication."
- **Confidence**: settled (first-party documentation; default access scope is explicitly
  stated)
- **Quote**: "By default, the GitHub Tools can read from the current repository and all
  public repositories (if permitted by the network firewall). To read from other private
  repositories, you must configure additional authentication."
- **Our assessment**: The default scope combines "current repo always accessible" with
  "public repos accessible if network permits." The network firewall qualifier from
  `docs-ghaw-network-reference.md` Claim 1 is a gating layer even for public repo access —
  the default `network: defaults` allows only basic infrastructure domains, which may or
  may not include GitHub's public API depending on configuration. The private repo access
  requirement creates a clear architectural boundary: a workflow cannot accidentally read
  private repositories beyond its own without explicitly configuring additional credentials.
  This directly corroborates `docs-ghaw-multi-repo-ops.md` Claim 3 (the `GITHUB_TOKEN`
  footgun for cross-repo reads). For Ch02: the "current repo + public repos" default is
  the correct mental model for practitioners configuring GitHub tools access.

### Claim 8: Four specific scenarios require additional authentication beyond the default `GITHUB_TOKEN` for GitHub tools: reading org/user information, reading other private repositories, reading projects, and using `remote` mode

- **Evidence**: The page enumerates the four cases in an "Additional Authentication
  Requirements" section: "Read access to GitHub org/user information", "Read access to
  other private repositories", "Read access to projects", and "Remote mode GitHub tools
  access."
- **Confidence**: settled (first-party documentation; the four cases are explicitly
  enumerated)
- **Quote**: (no direct quote; the four cases appear as a bulleted list without a
  quotable lead sentence — see paraphrase in Our assessment)
- **Our assessment**: These four scenarios define the boundary between what `GITHUB_TOKEN`
  can and cannot access in GitHub tools context. Organization/user information beyond the
  token owner requires higher-privilege access. GitHub Projects v2 requires additional
  project-read scope. `remote` mode requires forwarding credentials to GitHub's hosted
  infrastructure. The failure mode for all four is typically silent (empty results, not
  errors), making this a configuration pitfall that is hard to diagnose without careful
  pre-flight review. For Ch02: document as a pre-flight checklist for workflows that
  touch org data, projects, or remote mode. For Ch03: silent failures in cross-repo
  or org-read scenarios are a diagnostic anti-pattern — add verification steps when
  these scenarios apply.

### Claim 9: A fine-grained PAT for GitHub tools requires specific minimum permissions — repository-level (Contents/Issues/Pull requests/Projects/Security Events: Read) and organization-level (Members/Teams: Read) — and is referenced via `github-token:` in the tools block

- **Evidence**: The page specifies the exact PAT permissions needed and shows the
  `github-token: ${{ secrets.MY_PAT_FOR_GITHUB_TOOLS }}` configuration field.
- **Confidence**: settled (first-party documentation; the permission list and YAML field
  are explicitly defined)
- **Quote**: (no direct quote; the permission list appears as a structured list — see
  Concrete Artifacts)
- **Our assessment**: The minimum PAT permissions list is the reference for any
  practitioner needing cross-repo or org access in gh-aw workflows. The permissions are
  deliberately minimal: read-only access to the specific API areas GitHub tools require.
  The `github-token:` field in the `tools.github` block overrides `GITHUB_TOKEN` for all
  GitHub tools operations in that workflow. For Ch02: this is the PAT configuration
  specification for any workflow that hits the Claim 8 scenarios. Cross-reference the PAT
  least-privilege scope guidance from `docs-ghaw-multi-repo-ops.md` Claim 7 (read on
  source, write only on target) for a complete cross-repo auth reference.

### Claim 10: The `GH_AW_GITHUB_MCP_SERVER_TOKEN` magic secret provides GitHub tools cross-repository authentication without requiring an explicit `github-token:` reference in each workflow's frontmatter

- **Evidence**: The page states: "Set `GH_AW_GITHUB_MCP_SERVER_TOKEN` to a suitable PAT
  without explicit workflow reference."
- **Confidence**: emerging (the secret is named and described here and corroborated by
  `docs-ghaw-multi-repo-ops.md` Claim 9, but full provisioning mechanics and whether it
  works across organization boundaries are not detailed on this page)
- **Quote**: (no direct quote; the description appears in a short callout without
  quotable prose — see paraphrase in Our assessment)
- **Our assessment**: The magic secret is a convenience credential for the common case:
  practitioners who want cross-repo GitHub tools access without editing individual workflow
  files can set `GH_AW_GITHUB_MCP_SERVER_TOKEN` at the repository or organization level,
  and all workflows automatically inherit it. This is distinct from the explicit
  `github-token:` field, which is per-workflow. Corroborates `docs-ghaw-multi-repo-ops.md`
  Claim 9, which names the same secret as an option for cross-repo reads via toolset
  configuration. The emerging confidence reflects that the exact token scope, behavior
  across organization boundaries, and interaction with the three access modes are not
  fully documented on this page. For Ch02: document as the low-friction path for
  org-wide cross-repo read configuration; note that the full auth reference page
  should be consulted for production use.

### Claim 11: The `dependabot` toolset requires `vulnerability-alerts: read` and `security-events: read` workflow-level permissions, which are supported natively by `GITHUB_TOKEN` via explicit `permissions:` declaration

- **Evidence**: The page states: "The `dependabot` toolset requires the
  `vulnerability-alerts: read` and `security-events: read` permissions." These must be
  added to the workflow `permissions:` block and are natively supported by `GITHUB_TOKEN`.
- **Confidence**: settled (first-party documentation; the specific permission names and
  GITHUB_TOKEN compatibility are explicitly stated)
- **Quote**: "The `dependabot` toolset requires the `vulnerability-alerts: read` and
  `security-events: read` permissions."
- **Our assessment**: Unlike the GitHub App-Only permissions in `docs-ghaw-permissions-reference.md`
  Claim 6 (which require additional GitHub App authentication), the `dependabot` toolset's
  permissions are supported by the standard `GITHUB_TOKEN` — no additional PAT or App
  authentication is needed, just explicit declaration in `permissions:`. The barrier to
  using the `dependabot` toolset is therefore lower than the four scenarios in Claim 8:
  no credential setup is required, only a `permissions:` block addition. For Ch03: the
  `dependabot` toolset's opt-in permission requirement is security-by-default — agents
  cannot access vulnerability alerts without the workflow author explicitly declaring it,
  which prevents accidental exposure of security data to low-privilege workflows.

## Concrete Artifacts

### Complete `tools.github` Configuration Example

From the source page documentation:

```yaml
tools:
  github:
    mode: remote
    toolsets: [default]
    allowed-repos:
      - "myorg/*"
      - "partner/shared-repo"
      - "myorg/api-*"
    min-integrity: approved
```

*Source: `reference/github-tools` — configuration example*

### GitHub Toolset Catalog

```
Available toolsets (18 total):
  context              — user and team information
  repos                — repository operations, code search, commits, releases
  issues               — issue management and comments
  pull_requests        — PR operations
  users                — user information
  actions              — workflows, runs, artifacts
  code_security        — code scanning alerts
  discussions          — discussions and comments
  labels               — label management
  notifications        — notification access
  orgs                 — organization information
  projects             — GitHub Projects access
  gists                — gist access
  search               — search operations
  dependabot           — Dependabot alerts (requires extra permissions; excluded from `all`)
  experiments          — experimental features
  secret_protection    — secret scanning alerts
  security_advisories  — security advisory access

Shorthands:
  default → context, repos, issues, pull_requests, users
  all     → all toolsets EXCEPT dependabot
           (to include dependabot: toolsets: [all, dependabot])
```

*Source: `reference/github-tools` — toolset listing and shorthand values*

### Access Mode Comparison

```
Mode       Transport                                    Notes
---------  -------------------------------------------  -----------------------------------
local      Docker-based GitHub MCP Server               Default; no extra auth required
           inside the Actions VM
remote     Hosted GitHub MCP Server managed              Requires additional authentication
           by GitHub
gh-proxy   Pre-authenticated gh CLI                      Preferred for performance;
                                                        required for integrity reactions
```

*Source: `reference/github-tools` — GitHub Tools Access Modes table*

### Fine-Grained PAT Permission Requirements

```
Required PAT permissions for tools.github cross-repo/org access:

Repository permissions:
  Contents: Read
  Issues: Read
  Pull requests: Read
  Projects: Read
  Security Events: Read

Organization permissions:
  Members: Read
  Teams: Read
```

```yaml
# Reference in workflow frontmatter:
tools:
  github:
    github-token: ${{ secrets.MY_PAT_FOR_GITHUB_TOOLS }}
```

*Source: `reference/github-tools` — Personal Access Token section*

### `dependabot` Toolset Permissions

```yaml
# Required workflow permissions for the dependabot toolset:
permissions:
  vulnerability-alerts: read
  security-events: read

# Enable the toolset explicitly (not covered by `all`):
tools:
  github:
    toolsets: [all, dependabot]
```

*Source: `reference/github-tools` — Dependabot Toolset section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-multi-repo-ops.md` Claim 3 ("The default `GITHUB_TOKEN` only has access
    to the current repository"): Claim 7 here corroborates directly — the "current repo +
    public repos" default scoping means any private cross-repo read requires additional
    auth. Both notes identify the same failure mode (silent empty results, not errors)
    and the same fix (explicit additional auth configuration).
  - `docs-ghaw-multi-repo-ops.md` Claim 9 (`GH_AW_GITHUB_MCP_SERVER_TOKEN` as an option
    for cross-repo reads via GitHub toolsets without explicit workflow reference): Claim
    10 here is the reference documentation page for that same mechanism. The multi-repo-ops
    note names it as an option; this reference page explains the configuration.
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer defense-in-depth security pipeline):
    The `min-integrity` setting (Claim 4) and `allowed-repos` field (Claim 5) are concrete
    implementations of runtime and permission-separation security layers within that
    pipeline. Integrity filtering operates as a content-access control within the runtime
    layer; `allowed-repos` scoping is a permission-separation control.

- **Extends**:
  - `docs-ghaw-how-they-work.md` Claim 9 (multi-engine support, all engines use MCP-based
    tool protocol including `tools.github`): That note establishes `tools.github` as a
    conceptual building block. This reference provides the full configuration API for it —
    the complete toolset catalog, access modes, scope controls, and authentication
    requirements that practitioners need to actually configure GitHub tool access.
  - `docs-ghaw-permissions-reference.md` Claim 6 (GitHub App-Only Permissions taxonomy
    and its cross-reference link to `reference/github-tools` for additional auth setup):
    That note's `reference/github-tools` cross-reference points to this page. This note
    fills the content of that cross-reference — specifically the PAT requirements, GitHub
    App alternative, and magic secret option for cross-repo auth that the permissions
    reference page defers here.
  - `docs-ghaw-multi-repo-ops.md` (cross-repo orchestration patterns): That note documents
    safe-output routing to target repos; this note documents the read-side companion — how
    the `tools.github` toolsets are scoped for cross-repo reads. Together they form the
    complete picture of cross-repo interaction in gh-aw: read via `tools.github` with
    `allowed-repos` + write via `safe-outputs` with `target-repo`.
  - `docs-ghaw-mcps.md` Claim 1 (read-only policy for custom MCP servers): This note
    extends the read-only access story specifically for the built-in GitHub tools MCP —
    the same principle (read via tools, write via safe-outputs) but with the specific
    toolset catalog, access modes, and auth requirements for the platform's own GitHub
    integration.
  - `docs-ghaw-network-reference.md` Claim 1 (the `network:` field defaults to
    infrastructure-only egress): Claim 7 here notes that public repository access via
    GitHub tools is gated by "if permitted by the network firewall" — the network
    reference explains the default behavior that could block public repo access in
    restrictive configurations.

- **Contradicts**: None identified. The `allowed-repos` scoping and `min-integrity`
  filtering are additive configuration primitives not previously described in the corpus —
  they do not conflict with any existing claims. The `gh-proxy` mode preference for
  performance and integrity reactions is new information but does not contradict prior
  claims about access modes. No contradiction issue required.

- **Novel**:
  - **Complete 18-toolset catalog with `default`/`all` semantics** (Claims 1–3): No
    existing source note documents the full toolset catalog or the explicit expansion of
    `default` and `all` shorthands. The `dependabot` exclusion from `all` is not mentioned
    in any prior note.
  - **`min-integrity` content-gating setting** (Claim 4): No existing corpus note describes
    the `min-integrity` field or its automatic application for public repositories. This is
    the first corpus entry for this content-access control primitive.
  - **`allowed-repos` repository scoping** (Claim 5): The `allowed-repos` field with its
    four-level access hierarchy and pattern-matching rules (lowercase, end-of-name wildcard
    only) is not documented in any existing source note.
  - **Three access modes with transport properties** (Claim 6): While GitHub tools appear
    in several notes, none document the `local`/`remote`/`gh-proxy` mode taxonomy, the
    Docker-based local transport, the additional authentication requirement for `remote`,
    or the "preferred for performance; required for integrity reactions" rationale for
    `gh-proxy`.
  - **Four additional-auth scenarios enumerated** (Claim 8): No existing note enumerates
    the specific four scenarios where `GITHUB_TOKEN` is insufficient for GitHub tools
    operations. The scenarios are identified as trigger conditions for additional auth,
    not just a general warning.
  - **`dependabot` toolset GITHUB_TOKEN-compatible permissions** (Claim 11): No prior
    note documents that `vulnerability-alerts: read` and `security-events: read` are
    `GITHUB_TOKEN`-supported (vs. requiring GitHub App auth like the organization-level
    scopes in `docs-ghaw-permissions-reference.md`). The distinction is important for
    practitioners evaluating what credential setup is required.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add `toolsets: [default]` as the recommended starting configuration for any workflow
    needing GitHub data access, with a reference to the complete 18-toolset catalog for
    targeted expansion. Document the `dependabot` exclusion from `all` as a known footgun.
  - Add `allowed-repos` as the blast-radius control for GitHub data access — recommend
    scoping to the specific organizations or patterns the workflow needs rather than
    `"all"`. Document the pattern rules (lowercase, end-of-name wildcards only).
  - Add `min-integrity` as a content-access control layer distinct from `permissions:`,
    noting its automatic enforcement for public repos.
  - Document `gh-proxy` as the performance-preferred access mode for production workflows,
    especially those requiring integrity reactions. Add a note that `remote` mode carries
    additional auth requirements.
  - Add the four additional-auth scenarios (org/user info, private repos, projects, remote
    mode) as a pre-flight checklist for cross-repo and org-aware workflows.
  - Add the PAT permission specification as the reference configuration for practitioners
    needing cross-repo auth beyond the default `GITHUB_TOKEN`.

- **Chapter 03 (Safety and Verification)**:
  - Add `allowed-repos: "public"` as the maximum-restriction option for workflows that
    should access only public data, and `allowed-repos: "myorg/*"` as the standard
    organization-scope restriction.
  - Document the `dependabot` toolset as a controlled-access design note — vulnerability
    data requires explicit permission opt-in, consistent with security-by-default
    philosophy across the platform.
  - Add the cross-repo private access default (current repo + public only) as a security
    property: accidental private repo reads are prevented by default, not just by
    convention.
  - Add `min-integrity: approved` auto-enforcement for public repos as a platform-provided
    integrity guarantee that practitioners cannot weaken.

- **Chapter 04 (Multi-Agent Orchestration)**:
  - Add `gh-proxy` mode as the preferred transport for orchestration workflows that
    coordinate integrity operations across agents.
  - Add `GH_AW_GITHUB_MCP_SERVER_TOKEN` as the org-level configuration pattern for giving
    multiple orchestration workflows cross-repo read access without per-workflow token
    configuration. Cross-reference the full auth reference page for production mechanics.

## Extraction Notes

1. **Source processed via WebFetch AI model**: The gh-aw documentation site is an
   Astro/Starlight SPA. WebFetch converts and summarizes page content through an AI
   model before returning results. Quotes are from content that appeared consistently
   across two independent fetches and reads as technical documentation prose. Any
   `(no direct quote; see paraphrase in Our assessment)` attribution reflects uncertainty
   about verbatim fidelity.

2. **No publication date**: The documentation page does not carry an explicit publication
   date. `date_published` is left null. Content is consistent with current gh-aw platform
   state as of 2026-05-11.

3. **`GH_AW_GITHUB_MCP_SERVER_TOKEN` mechanics partially documented**: The magic secret
   is named on this page and corroborated by `docs-ghaw-multi-repo-ops.md` Claim 9, but
   full provisioning mechanics, token scope, and cross-org behavior are deferred to an
   auth reference page not yet in the corpus. Claim 10 is assessed as `emerging` for
   this reason.

4. **GitHub App authentication mentioned but not detailed**: The page references GitHub
   App as an alternative to PAT authentication and links to an "Authentication Reference"
   page for setup details. That page was not fetched. The GitHub App option is noted in
   Claim 9's Our assessment but not extracted as a separate claim because the
   configuration details are on the linked page, not this one.

5. **`dependabot` toolset vs. Dependabot compiler feature**: This note's Claim 11 covers
   the `dependabot` toolset within `tools.github` (reading Dependabot vulnerability
   alerts in workflow agents). This is distinct from `docs-ghaw-dependabot.md`, which
   covers `gh aw compile --dependabot` (generating Dependabot dependency manifests for
   runtime tool invocations). The two `dependabot` references address different platform
   features.

6. **No contradictions filed**: Reviewed all existing corpus source notes. No claims in
   this source materially oppose existing notes. The `allowed-repos` scoping,
   `min-integrity` filtering, and three access modes are new additive primitives.
   No contradiction issue required.
