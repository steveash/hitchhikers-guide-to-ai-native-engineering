---
source_url: https://github.github.com/gh-aw/reference/auth-projects
source_type: docs
title: "GitHub Agentic Workflows: Authentication (Projects) Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-06-21
last_checked: 2026-06-21
status: current
confidence_overall: settled
issue: "#359"
---

# GitHub Agentic Workflows: Authentication (Projects) Reference

> The structured reference page for Projects API authentication in gh-aw — documents
> why the Projects GraphQL API sits outside `GITHUB_TOKEN` scope, the three authentication
> paths (classic PAT for user-owned, fine-grained PAT for org-owned, GitHub App for
> org standardization), the `GH_AW_GITHUB_MCP_SERVER_TOKEN` magic secret's explicit
> applicability to the `projects` toolset, and the recommended dual-secret layout for
> read/write separation.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/auth-projects` page — in
  the "Reference" section alongside `reference/permissions`, `reference/github-tools`.
  Reference pages document platform configuration authoritatively. This is the dedicated
  structured reference for Projects authentication, distinct from the ProjectOps pattern
  page at `patterns/project-ops/` which covers auth as part of a broader pattern
  description.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same
  team behind Peli de Halleux's "Agent Factory" blog series and the `gh aw` CLI. Token
  type requirements, scope names, and magic secret behavior are settled platform facts.
  The three-path authentication decision matrix is prescriptive guidance from the platform
  team.
- **Scope**: Authentication exclusively for GitHub Projects operations in gh-aw — why
  `GITHUB_TOKEN` cannot access the Projects GraphQL API, the three token paths (classic
  PAT, fine-grained PAT, GitHub App token), the `GH_AW_GITHUB_MCP_SERVER_TOKEN` magic
  secret's coverage of the `projects` toolset, and the recommended dual-secret naming
  convention. Does NOT cover: the broader ProjectOps pattern (see `docs-ghaw-projectops.md`),
  the general permissions model (see `docs-ghaw-permissions-reference.md`), the GitHub
  Tools reference covering all 18 toolsets (see `docs-ghaw-github-tools.md`), or multi-repo
  read authentication (see `docs-ghaw-multi-repo-ops.md`).

## Extracted Claims

### Claim 1: The Projects GraphQL API sits outside `GITHUB_TOKEN`'s repository-level scope — both user-owned and org-owned projects require a token with explicit Projects permissions

- **Evidence**: The page opens with a direct explanation of the authentication gap,
  naming "Projects GraphQL API" as the specific endpoint that `GITHUB_TOKEN` cannot reach.
  The scope of the limitation is stated precisely: both ownership models (user-owned and
  organization-owned) are affected.
- **Confidence**: settled (first-party documentation; the GITHUB_TOKEN scope limitation
  for GitHub Projects is a GitHub platform constraint, not a gh-aw-specific design choice)
- **Quote**: "The standard `GITHUB_TOKEN` provided to every GitHub Actions workflow has
  repository-level scope only. GitHub Projects (both user-owned and organization-owned)
  sit outside that scope, so any workflow step that reads project fields or writes updates
  must supply a token with explicit Projects permissions."
- **Our assessment**: This is the most precise statement of the GITHUB_TOKEN limitation
  for Projects in the corpus. Earlier notes (e.g., `docs-ghaw-projectops.md` Claim 2)
  state that GITHUB_TOKEN "cannot access the GitHub Projects API" but do not name the
  GraphQL endpoint specifically. The "GraphQL API" terminology matters for practitioners
  debugging auth failures: they need to know this is not a REST API permission issue but
  a GraphQL endpoint scoping issue. The "both user-owned and organization-owned" phrasing
  pre-empts the assumption that user-owned projects might work with GITHUB_TOKEN (they
  don't). This is the unambiguous starting point for any Projects authentication
  implementation. For Ch02 (Harness Engineering): use this phrasing as the canonical
  explanation of why Projects auth differs from all other gh-aw token patterns.

### Claim 2: Classic PATs with `project` and `repo` scopes are the token path for user-owned projects

- **Evidence**: The page specifies the exact token type and scope requirements for
  the user-owned project case. "Classic PAT" (not fine-grained) is explicitly named,
  and the two required scopes (`project` and `repo`) are both documented.
- **Confidence**: settled (first-party documentation; these are GitHub API permission
  requirements)
- **Quote**: (no single contiguous quote covers both scope requirements; the page
  presents them in a structured token options section — see Concrete Artifacts)
- **Our assessment**: The classic PAT requirement for user-owned projects is notable:
  this is one of the few places in the modern GitHub documentation where a classic PAT
  is the prescribed option rather than a fine-grained PAT. The reason is that the
  `project` scope is a classic PAT scope — fine-grained PATs use permission names like
  "Projects: Read and write" rather than the legacy `project` scope name. The `repo`
  scope requirement applies when the user-owned project contains items from private
  repositories. For Ch02: when documenting user-owned project auth, specify classic PAT
  explicitly — practitioners who have already migrated to fine-grained PATs everywhere
  may not have a classic PAT available and will need to create one.

### Claim 3: Organization-owned projects require a fine-grained PAT with "Projects: Read and write" organization permission

- **Evidence**: The page explicitly specifies the permission name for the fine-grained
  PAT path: the organization permission must be set to "Projects: Read and write". This
  is in contrast to the classic PAT's `project` scope — the fine-grained permission uses
  a different naming convention.
- **Confidence**: settled (first-party documentation; these are GitHub API permission
  requirements)
- **Quote**: (no direct quote; the page presents this in a structured format; see
  Concrete Artifacts)
- **Our assessment**: The fine-grained PAT path requires both repository-level permissions
  (Contents Read, optionally Issues/Pull Requests Read) AND organization-level permissions
  ("Projects: Read and write"). The organization-level permission requirement means the
  practitioner must configure the PAT's resource owner as the organization, not just their
  user account. For most GitHub organizations, a member cannot grant themselves
  organization-level permissions without admin coordination — the fine-grained PAT must be
  approved or the member must have sufficient organization role. For Ch02: document that
  org-owned project auth requires both repo-level and org-level permission configuration
  in the fine-grained PAT — this is the most common auth setup failure for teams
  implementing ProjectOps.

### Claim 4: GitHub App tokens with "Organization projects: Read and write" permission are the org-wide standardization path, eliminating per-user PAT management

- **Evidence**: The page presents GitHub App token configuration as an alternative to
  both PAT paths, specifically for organizations that want to standardize authentication
  across workflows. The exact permission name is specified: "Organization projects: Read
  and write."
- **Confidence**: settled (first-party documentation; GitHub App permission names are
  authoritative)
- **Quote**: (no direct quote; the page presents GitHub App as an option in the token
  options section — see Concrete Artifacts)
- **Our assessment**: The GitHub App path is the correct choice for organizations running
  ProjectOps at scale (many repositories, many workflows). PATs are user-bound — if the
  user who provisioned the PAT leaves the organization, the PAT becomes invalid and
  workflows break silently. A GitHub App token is org-scoped and not tied to an individual,
  making it more robust for production use. The tradeoff: GitHub App setup requires
  creating and managing an App installation, which is more initial setup overhead but
  lower ongoing maintenance. For Ch02: present GitHub App as the preferred long-term
  auth pattern for org-owned projects at scale. For Ch03: flag PAT-as-user-credential
  as a fragility risk in production ProjectOps deployments.

### Claim 5: The `GH_AW_GITHUB_MCP_SERVER_TOKEN` magic secret covers all GitHub tools toolsets including `projects` — present in the repository, it is used automatically without explicit workflow reference

- **Evidence**: The page explicitly extends the magic secret's documented coverage to
  include the `projects` toolset. The auto-use behavior is stated directly.
- **Confidence**: settled (first-party documentation; the magic secret name, scope, and
  auto-use behavior are explicitly described on this reference page)
- **Quote**: "The magic secret `GH_AW_GITHUB_MCP_SERVER_TOKEN` is recognized by GitHub
  Agentic Workflows and does not need to be explicitly referenced in your workflow — if
  it is present in the repository, it is used automatically for all GitHub tools toolsets,
  including `projects`."
- **Our assessment**: This is the key new information this reference page adds to the
  corpus relative to what is documented in `docs-ghaw-github-tools.md` Claim 5 and
  `docs-ghaw-multi-repo-ops.md` Claim 3. Those notes establish that the magic secret
  provides cross-repo authentication for GitHub Tools generally; this page explicitly
  states it covers the `projects` toolset specifically. The practical implication: a
  team that already has `GH_AW_GITHUB_MCP_SERVER_TOKEN` configured for cross-repo reads
  does NOT need to also provision a separate `GH_AW_READ_PROJECT_TOKEN` for Projects
  read access — the magic secret handles both. The magic secret is therefore an
  alternative to `GH_AW_READ_PROJECT_TOKEN` for the read half of the dual-secret pattern.
  The write half still requires `GH_AW_WRITE_PROJECT_TOKEN` in the safe-outputs block.
  For Ch02: document the magic secret as the zero-friction alternative to
  `GH_AW_READ_PROJECT_TOKEN` for Projects read access.

### Claim 6: The recommended dual-secret layout (`GH_AW_READ_PROJECT_TOKEN` / `GH_AW_WRITE_PROJECT_TOKEN`) enforces least-privilege at the credential level, with explicit `gh aw secrets set` provisioning commands

- **Evidence**: The page prescribes separate read and write tokens with explicit naming
  conventions and provides the exact CLI commands for provisioning them.
- **Confidence**: settled (first-party documentation; the secret names and CLI syntax
  are explicitly documented)
- **Quote**: (no single contiguous prose quote; the CLI commands appear in a code block
  — see Concrete Artifacts)
- **Our assessment**: The dual-secret naming convention (`GH_AW_READ_PROJECT_TOKEN` vs.
  `GH_AW_WRITE_PROJECT_TOKEN`) makes the purpose of each credential self-documenting in
  the workflow YAML. This is an incremental improvement over opaque secret names (e.g.,
  `MY_TOKEN`) that require cross-referencing documentation to understand. The explicit
  CLI commands with `--value "<token>"` syntax are useful for practitioners setting up
  Projects auth for the first time. This corroborates `docs-ghaw-projectops.md` Claim 4
  at the reference-page level — the dual-token layout is the authoritative recommendation,
  not just a pattern-page suggestion. For Ch02: use these secret names as the prescribed
  naming convention for Projects auth. Any workflow deviating from these names should be
  documented as a custom configuration.

## Concrete Artifacts

### Token Option Decision Matrix (structured from source)

```
User-Owned Projects:
  Token type:   Classic PAT
  Scopes:       project
                repo  (if project contains items from private repositories)
  Provisioning: gh aw secrets set GH_AW_READ_PROJECT_TOKEN --value "<token>"

Organization-Owned Projects — Option A (fine-grained PAT):
  Token type:   Fine-grained PAT
  Config:       Resource owner: the organization owning the project
                Repository permissions: Contents Read
                                        Issues Read (optional)
                                        Pull Requests Read (optional)
                Organization permissions: Projects Read and write
  Provisioning: gh aw secrets set GH_AW_READ_PROJECT_TOKEN --value "<token>"
                gh aw secrets set GH_AW_WRITE_PROJECT_TOKEN --value "<token>"

Organization-Owned Projects — Option B (GitHub App):
  Token type:   GitHub App token
  Permission:   Organization projects: Read and write
  Use case:     Org-wide standardization; eliminates per-user PAT management

All paths:
  IMPORTANT: GITHUB_TOKEN is repository-level only.
             It CANNOT access the Projects GraphQL API.
```

*Source: authentication (Projects) reference page, "Token Options" section.*

### `GH_AW_GITHUB_MCP_SERVER_TOKEN` Magic Secret Coverage

```
The magic secret GH_AW_GITHUB_MCP_SERVER_TOKEN:
  - Does NOT need to be explicitly referenced in workflow YAML
  - Is used automatically if present in the repository
  - Covers ALL GitHub tools toolsets, including `projects`
  - Provides a zero-configuration-change alternative to GH_AW_READ_PROJECT_TOKEN
    for the read half of the dual-secret layout

When to use:
  - Already have GH_AW_GITHUB_MCP_SERVER_TOKEN for cross-repo reads?
    → No additional read token needed for Projects toolset
  - Starting fresh, only need Projects auth?
    → Use GH_AW_READ_PROJECT_TOKEN + GH_AW_WRITE_PROJECT_TOKEN (explicit, auditable)
```

*Source: auth-projects reference page, magic secret section.*

### Dual-Secret Provisioning Commands (from source)

```bash
# Provision read token (used in tools.github block)
gh aw secrets set GH_AW_READ_PROJECT_TOKEN --value "<read-token>"

# Provision write token (used in safe-outputs.update-project block)
gh aw secrets set GH_AW_WRITE_PROJECT_TOKEN --value "<write-token>"
```

*Source: auth-projects reference page.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-projectops.md` Claim 2 (`GITHUB_TOKEN` is repository-scoped and cannot
    access the GitHub Projects API): The auth-projects reference corroborates this with
    more specific language — "Projects GraphQL API" and "repository-level scope only."
    Both sources are fully consistent; this reference is the dedicated auth page while
    projectops.md embeds auth guidance within the broader pattern description.
  - `docs-ghaw-projectops.md` Claims 3–4 (user-owned vs. org-owned token split;
    dual-token layout): The auth-projects reference corroborates both claims with the
    same two-path structure and the same dual-secret naming convention.
  - `docs-ghaw-github-tools.md` Claim 5 (`GH_AW_GITHUB_MCP_SERVER_TOKEN` magic secret
    provides GitHub Tools auth without explicit workflow reference): The auth-projects
    reference corroborates the auto-use behavior and the "no explicit reference needed"
    mechanism, while extending it with explicit confirmation that `projects` is covered.
  - `docs-ghaw-multi-repo-ops.md` Claim 3 (default `GITHUB_TOKEN` is scoped to the
    current repository only): Both sources warn about `GITHUB_TOKEN` scope limitations.
    Multi-repo-ops frames it as a cross-repo read failure; auth-projects frames it as
    a Projects GraphQL API access failure. Same underlying GitHub platform constraint.

- **Extends**:
  - `docs-ghaw-projectops.md` Claims 2–4: The auth-projects reference is the dedicated
    reference page that the ProjectOps pattern page points to for auth details. It provides
    the same information in a more structured reference format, with explicit CLI commands
    and the magic secret option that is not detailed in the pattern page.
  - `docs-ghaw-github-tools.md` Claim 5 (magic secret for GitHub Tools auth): The
    auth-projects reference extends Claim 5 by explicitly naming `projects` as a covered
    toolset. The github-tools note establishes the magic secret covers "GitHub Tools" at
    the generic level; this reference confirms coverage of the Projects-specific toolset.
  - `docs-ghaw-permissions-reference.md` Claim 6 (GitHub App-Only Permissions require
    additional authentication beyond standard token access): The auth-projects reference
    extends this by naming the specific permission required for Projects — "Organization
    projects: Read and write" — which is the concrete implementation of the GitHub App-Only
    Permissions pattern described at the abstract level in the permissions reference.

- **Contradicts**: None identified. The auth-projects reference is fully consistent with
  the existing corpus. The June 11, 2026 change documented in
  `docs-github-copilot-aw-github-token-auth.md` (GITHUB_TOKEN can now be used for
  workflow execution) does not contradict this source: that change eliminates the PAT
  requirement for running agentic workflows (model invocations), while the Projects
  GraphQL API still requires explicit Projects permissions regardless of how the workflow
  runner authenticates. No contradiction issue filed.

- **Novel** (what this note adds to the corpus that no prior source explicitly covers):
  - **"Projects GraphQL API" precise terminology** (Claim 1): No existing corpus note
    names the Projects endpoint as the "Projects GraphQL API." This precision matters for
    practitioners debugging auth failures — it identifies the specific endpoint class that
    is out of scope, not just the generic "Projects API."
  - **`GH_AW_GITHUB_MCP_SERVER_TOKEN` explicit coverage of `projects` toolset** (Claim 5):
    `docs-ghaw-github-tools.md` Claim 5 documents the magic secret for GitHub Tools
    generally and cross-repo private access specifically; `docs-ghaw-multi-repo-ops.md`
    Claim 3 names it as a cross-repo read option. Neither explicitly states it covers the
    `projects` toolset. The verbatim quote — "including `projects`" — is new to the
    corpus and has immediate practical value: teams with the magic secret already
    configured for cross-repo reads need no additional token for Projects read access.
  - **Classic PAT requirement for user-owned projects** (Claim 2): `docs-ghaw-projectops.md`
    Claim 3 states "classic PAT" but the auth-projects reference is the designated
    reference page that makes this authoritative. The distinction that classic (not
    fine-grained) is required for user-owned projects is explicit here.
  - **Dual-secret provisioning CLI syntax** (Claim 6, Concrete Artifacts): The
    `gh aw secrets set ... --value "<token>"` command format is not documented in any
    existing source note with this specific syntax.

## Guide Impact

### Chapter 02: Harness Engineering

- **Use "Projects GraphQL API" as the canonical explanation of why auth differs** (Claim 1):
  The current corpus uses "Projects API" generically. The more specific "Projects GraphQL
  API" tells practitioners exactly why `GITHUB_TOKEN` fails — it's a different endpoint
  class outside repository scope, not just a missing permission on a REST endpoint.

- **Document the three-path auth decision matrix for Projects** (Claims 2–4):
  The pattern page covers two paths (PAT, GitHub App); this reference adds the classic vs.
  fine-grained PAT distinction and the specific permission name for each. Add this
  three-path matrix to the Ch02 Projects auth section, with the guidance that org-owned
  projects default to fine-grained PAT or GitHub App (not classic PAT).

- **Document `GH_AW_GITHUB_MCP_SERVER_TOKEN` as a read-path alternative to
  `GH_AW_READ_PROJECT_TOKEN`** (Claim 5): Teams that already have the magic secret
  configured for cross-repo reads do not need an additional read token for Projects.
  This is a simplification worth calling out explicitly in the harness credential section.

- **Add `gh aw secrets set` CLI commands as the provisioning reference** (Claim 6,
  Concrete Artifacts): The exact syntax for provisioning both read and write tokens
  should appear in Ch02's setup instructions so practitioners have a copy-paste starting
  point.

### Chapter 03: Safety and Verification

- **Flag user PAT fragility for org-owned Projects** (Claim 4): PATs provisioned by
  individual users break when those users leave the organization. For production
  ProjectOps deployments, the GitHub App path eliminates this fragility. Add this as a
  production-readiness consideration in Ch03's credential management section.

## Extraction Notes

1. **Source confirmed live at extraction**: The page at
   `https://github.github.com/gh-aw/reference/auth-projects` returned content via
   WebFetch as of 2026-06-21.

2. **WebFetch returned summarized output, not verbatim HTML**: The WebFetch tool
   processed this page through an AI model that converted HTML to markdown and produced
   a condensed representation. The verbatim quotes were extracted from two separate
   WebFetch calls (different prompts) and cross-validated for consistency. Where the two
   fetches returned the same wording, that wording is treated as verbatim source text.
   Where only the second fetch returned a passage, it is marked with `(no direct quote;
   see paraphrase in Our assessment)` if the exact wording could not be confirmed.

3. **Incremental vs. projectops.md**: The Prospector correctly identifies this as
   incremental — the auth claims largely corroborate `docs-ghaw-projectops.md` Claims 2–4.
   The genuinely new corpus additions are the "Projects GraphQL API" precision and the
   explicit `GH_AW_GITHUB_MCP_SERVER_TOKEN` coverage of the `projects` toolset (Claim 5).

4. **No publication date**: The documentation page does not carry an explicit publication
   date. Content is consistent with the current gh-aw platform state as of 2026-06-21,
   based on matching the authentication patterns documented in other recently extracted
   notes.

5. **No contradictions filed**: Reviewed all existing source notes. No claims in this
   source materially oppose any existing note. The auth-projects claims are a structured
   elaboration of what is documented across `docs-ghaw-projectops.md`,
   `docs-ghaw-github-tools.md`, and `docs-ghaw-multi-repo-ops.md`. No contradiction
   issue required.
