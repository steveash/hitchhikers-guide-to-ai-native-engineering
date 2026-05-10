---
source_url: https://github.github.com/gh-aw/reference/permissions
source_type: docs
title: "GitHub Agentic Workflows: GitHub Read Permissions Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#401"
---

# GitHub Agentic Workflows: GitHub Read Permissions Reference

> The authoritative configuration reference for gh-aw's `permissions:` frontmatter
> section — documents the read-only-by-default model, the four explicit security
> rationales for the read/safe-outputs separation (audit trail, blast radius,
> compliance gates, prompt injection defense), the ten standard read scopes, two
> shorthand variants, the GitHub App-Only permission taxonomy, and the anomalous
> `id-token` permission whose `write` value bypasses the safe-outputs model while
> granting no repository modification ability.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/permissions` page —
  in the "Reference" section, distinct from conceptual `introduction/` pages and
  practitioner `guides/`. Reference pages document platform configuration
  authoritatively; this one specifies the complete permissions model for gh-aw
  workflows.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's agent factory blog series and the `gh aw`
  CLI. Configuration field names, permission scope lists, and validation behavior
  are settled platform facts. The four-reason security rationale (Claim 2) is
  architectural framing from the platform team, not third-party measurement.
- **Scope**: The complete permissions configuration for gh-aw workflows — the
  `permissions:` frontmatter section, ten standard read scopes, shorthand options,
  GitHub App-Only permissions, and the `id-token` special case. Does NOT cover:
  the Safe Outputs mechanism in depth (see `docs-ghaw-how-they-work.md` Claim 5
  and the separate `reference/safe-outputs` page), the compilation process that
  validates permissions at compile time (see `docs-ghaw-compilation-process.md`),
  or the concurrency model for the Safe Outputs job (see
  `docs-ghaw-concurrency-reference.md`).

## Extracted Claims

### Claim 1: The `permissions:` frontmatter section defaults to read-only in gh-aw workflows, with all write operations exclusively routed through the separate safe outputs mechanism

- **Evidence**: The page opens with the architectural statement and provides a
  canonical code example pairing `permissions:` (read-only scopes) with
  `safe-outputs:` (write operations). Both are required for any workflow that
  needs to modify GitHub state.
- **Confidence**: settled (first-party documentation; this is a design principle
  of the platform with an explicit canonical code example)
- **Quote**: "GitHub Agentic Workflows uses read-only permissions by default for
  security, with write operations handled through safe outputs."
- **Our assessment**: This is the concrete configuration expression of the
  "zero capability by default" principle documented at a conceptual level in
  `docs-ghaw-how-they-work.md` Claim 4. The permissions reference makes the split
  actionable: if you need read access, put it in `permissions:`; if you need write
  access (create an issue, add a comment, open a PR), put it in `safe-outputs:`.
  The agent job runs with only the `permissions:` scopes; a separate job executes
  the `safe-outputs:` operations using its own write-capable permissions. For
  Ch02 (Harness Engineering): the canonical pattern is
  `permissions: {read scopes} + safe-outputs: {write ops}`.

### Claim 2: The read/safe-outputs separation serves four distinct security purposes: audit trail creation, blast radius limitation, compliance approval gate support, and prompt injection defense

- **Evidence**: The page states this explicitly immediately after the canonical
  code example, providing all four rationales in one sentence. The statement
  characterizes the trade-off (one extra job) as worth the security benefit.
- **Confidence**: settled (first-party architectural rationale; the four purposes
  are explicitly named on the page)
- **Quote**: "This separation provides an audit trail, limits blast radius if an
  agent misbehaves, supports compliance approval gates, and defends against prompt
  injection."
- **Our assessment**: Each of the four reasons addresses a distinct threat model:
  (1) Audit trail — the separate safe-outputs job creates a structured log of every
  write operation the agent requested, enabling post-hoc review; (2) Blast radius —
  a misbehaving agent can only request operations declared in `safe-outputs:`, not
  arbitrary GitHub API writes; (3) Compliance approval gates — organizations
  requiring human sign-off for certain operations can inspect and gate the
  safe-outputs job independently; (4) Prompt injection — even if an attacker crafts
  a prompt that causes the agent to produce malicious instructions, those instructions
  must pass through the safe-outputs validation layer before reaching the GitHub API.
  This is the most complete articulation of the safe-outputs security rationale in
  our corpus. For Ch03 (Safety and Verification): add these four reasons as the
  canonical justification for the read/write permission separation in agentic
  workflow design.

### Claim 3: Safe outputs cost exactly one extra job — the page makes the trade-off explicit and characterizes it as justified by critical safety guarantees

- **Evidence**: Direct statement on the page, immediately after the four security
  rationales. The phrasing "but provide critical safety guarantees" frames the
  extra job as non-negotiable overhead, not an optimization target.
- **Confidence**: settled (first-party; the cost quantification is explicit)
- **Quote**: "Safe outputs add one extra job but provide critical safety guarantees."
- **Our assessment**: Explicitly quantifying the cost ("one extra job") makes the
  trade-off concrete for practitioners evaluating whether to use safe outputs or
  request write permissions directly. The framing is useful for teams pushing back
  on perceived overhead — one extra job in a CI pipeline is a negligible cost
  relative to the four security guarantees it provides. For Ch02: when explaining
  why gh-aw uses safe outputs instead of direct write permissions, cite this as
  the platform team's explicit cost/benefit statement.

### Claim 4: Ten standard read permission scopes cover all major GitHub API operation areas available to gh-aw workflows

- **Evidence**: The page lists the primary read permission categories with their
  semantic purposes, covering the full breadth of GitHub repository and
  collaboration features available to workflow agents.
- **Confidence**: settled (first-party documentation; this is the enumeration of
  supported scopes)
- **Quote**: (no direct quote; the scopes are listed as a bullet list without
  introductory prose to quote verbatim — see Concrete Artifacts)
- **Our assessment**: The ten scopes map cleanly to the major GitHub operation
  areas a workflow agent needs to read: `contents` (code), `issues` (issue
  management), `pull-requests` (PR management), `discussions`, `actions`
  (workflow control), `checks` (CI status), `deployments`, `packages`, `pages`,
  and `statuses` (commit status). Practitioners designing a new workflow should
  enumerate which read scopes they need and specify them explicitly rather than
  defaulting to `read-all` — the principle of least privilege applies to read
  access too. For Ch02: provide this list as the starting point for permissions
  design.

### Claim 5: Two shorthand permission values serve distinct workflow archetypes — `read-all` for inspection workflows needing broad read access, and `{}` for computation-only workflows requiring zero GitHub API access

- **Evidence**: The page defines both shorthands with explicit use cases.
  `read-all` is described as "useful for inspection workflows"; `{}` is described
  as for "computation-only workflows."
- **Confidence**: settled (first-party documentation; the shorthand values and
  their use cases are explicitly defined)
- **Quote**: (no single contiguous quote captures both shorthands; the page
  describes them in separate bullet items — see Concrete Artifacts)
- **Our assessment**: The `{}` (no permissions) shorthand is particularly notable —
  it means a workflow can run without any GitHub API access at all. This is the
  correct configuration for workflows that only process data passed via `inputs:`
  or perform pure computation (e.g., running a calculation and writing results
  to a safe output without needing to read any repository content). The `read-all`
  shorthand is appropriate for audit/inspection workflows that need to scan a
  repository comprehensively. Both shorthands represent intentional design choices,
  not fallbacks. For Ch02: add `{}` and `read-all` as the permission design
  boundary cases, with explicit guidance on when each is appropriate.

### Claim 6: GitHub App-Only Permissions — a three-category taxonomy of repository-level, organization-level, and user-level scopes — require additional authentication beyond standard token access and must always be declared as `read`

- **Evidence**: The page names three categories of GitHub App-Only Permissions and
  provides an extensive list of specific scopes within each. A hard constraint
  applies to all: "These scopes must always be declared as `read`." The page links
  to `reference/github-tools` for additional authentication setup.
- **Confidence**: settled (first-party documentation; the constraint and scope
  lists are authoritative for the platform)
- **Quote**: "These scopes must always be declared as `read`."
- **Our assessment**: The GitHub App-Only Permissions category exists because
  certain GitHub API operations (accessing organization members, managing
  codespaces, custom org roles) require a GitHub App installation's token rather
  than the standard GITHUB_TOKEN. This reflects GitHub's underlying authentication
  model, not a gh-aw-specific constraint. The "must always be declared as `read`"
  rule means these scopes cannot be used for write operations through the
  `permissions:` section — writes still go through safe outputs. The practical
  implication: if a workflow needs to read organization membership or access
  repository administration settings, it must configure additional GitHub App
  authentication. For Ch02: warn practitioners that not all GitHub API operations
  are accessible via the standard GITHUB_TOKEN.

### Claim 7: The `id-token` permission is anomalous — it accepts only `write` or `none` (never `read`), `id-token: read` is rejected at compile time, and `id-token: write` grants no ability to modify repository content

- **Evidence**: The page dedicates a section to this special case, stating:
  "The only valid values are `write` and `none`. `id-token: read` is not a valid
  permission and will be rejected at compile time." The explanation of why
  `id-token: write` is safe despite the "write" keyword is given directly.
- **Confidence**: settled (first-party documentation; compile-time rejection of
  `id-token: read` is an explicit platform behavior)
- **Quote**: "Unlike other write permissions, `id-token: write` does not grant any
  ability to modify repository content."
- **Our assessment**: The `id-token` anomaly is a potential confusion point for
  practitioners who assume all `write` permissions grant repository modification
  access. The OIDC token permission is about authentication, not authorization to
  modify state — it allows the workflow to prove its identity to external cloud
  providers (AWS, GCP, Azure) using short-lived tokens from GitHub's token service.
  The compile-time rejection of `id-token: read` prevents a common misconfiguration
  (attempting to grant "minimal" access by specifying `read` instead of `write`).
  For Ch02: when documenting OIDC-based cloud deployments in gh-aw, make the
  `id-token: write` exception explicit — it is not a violation of the read-only
  policy.

### Claim 8: The `id-token: write` permission does not require safe outputs routing because OIDC token issuance is stateless and does not create, modify, or delete any GitHub repository content

- **Evidence**: The page states explicitly: "This permission does not require
  safe-outputs." The rationale: OIDC authentication with cloud providers involves
  receiving a short-lived token (not writing to GitHub state).
- **Confidence**: settled (first-party documentation; explicit statement in the
  `id-token` section)
- **Quote**: "This permission does not require safe-outputs."
- **Our assessment**: This is the sole documented exception to the safe-outputs
  routing model for write-labeled permissions. The exception is principled: safe
  outputs exist to control write operations against GitHub state; OIDC token
  issuance is a credential-issuance operation (the workflow receives a token,
  it does not write to GitHub). Wrapping OIDC authentication in a safe-outputs
  block would not work — OIDC must happen at the job level before safe outputs
  execute. For Ch03: document this as the only explicitly stated exception to
  "writes go through safe-outputs," with a clear explanation of why (OIDC is
  stateless with respect to GitHub state).

## Concrete Artifacts

### Canonical Read + Safe Outputs Pattern (from source)

```yaml
permissions:
  contents: read
  actions: read
safe-outputs:
  create-issue:
  add-comment:
```

*Source: "GitHub Tools Read Permissions" page, opening example*

### Ten Standard Read Permission Scopes

```
contents        — code access
issues          — issue management
pull-requests   — PR management
discussions     — discussions and comments
actions         — workflow control
checks          — checks and statuses
deployments     — deployment management
packages        — package management
pages           — GitHub Pages management
statuses        — commit status management
```

*Source: "Permission Scopes" section*

### Shorthand Permission Values

```yaml
# Universal read access across all scopes (inspection workflows):
permissions: read-all

# No permissions at all (computation-only workflows):
permissions: {}
```

*Source: "Permission Scopes — Shorthand Options" section*

### id-token OIDC Example (from source)

```yaml
# Example: Deploy to AWS using OIDC authentication
permissions:
  id-token: write      # Allowed for OIDC authentication
  contents: read       # Read repository code
```

*Source: "Special Permission: id-token" section*

### GitHub App-Only Permission Taxonomy

```
Repository-level (require GitHub App additional authentication):
  administration, environments, git-signing, workflows, repository-hooks,
  single-file, codespaces, repository-custom-properties

Organization-level (require GitHub App additional authentication):
  organization-projects, members, organization-administration, team-discussions,
  organization-hooks, organization-members, organization-packages,
  organization-self-hosted-runners, organization-custom-org-roles,
  organization-custom-properties, organization-custom-repository-roles,
  organization-announcement-banners, organization-events, organization-plan,
  organization-user-blocking, organization-personal-access-token-requests,
  organization-personal-access-tokens, organization-copilot,
  organization-codespaces

User-level (require GitHub App additional authentication):
  email-addresses, codespaces-lifecycle-admin, codespaces-metadata

Constraint: all must be declared as `read` — never `write`
```

*Source: "GitHub App-Only Permissions" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 4 ("Workflows run with minimal permissions —
    no write access by default — using tool allowlists to constrain the agent's
    action surface"): This permissions reference is the concrete configuration API
    that implements the "no write access by default" principle. The how-they-work
    note states the principle; this reference shows exactly how it is configured
    via the `permissions:` frontmatter section.
  - `docs-ghaw-how-they-work.md` Claim 5 ("Safe Outputs are pre-approved GitHub
    operations the AI can request without write permissions"): This reference
    corroborates by showing the frontmatter pairing — `permissions:` (read scopes)
    + `safe-outputs:` (write ops) — that implements the Safe Outputs model at the
    configuration level.
  - `docs-ghaw-compilation-process.md` Claim 3 ("These three jobs form a sequential
    security pipeline rooted in Plan-Level Trust — AI reasoning (read-only) is
    separated from write operations. They cannot be merged because GitHub Actions
    permissions are per-job and immutable for the duration of a job."): The
    permission scoping described here — read-only agent job, write-capable
    safe-outputs job — is enforced by the GitHub Actions job-level permission
    constraint that Claim 3 in the compilation process note explains. The two
    notes give the complete picture: this reference explains the configuration
    model; the compilation process note explains why separate jobs are
    architecturally required.

- **Extends**:
  - `docs-ghaw-how-they-work.md` Claims 4 and 5 (no write access by default, safe
    outputs model): This reference extends the how-they-work conceptual description
    with the specific scope enumeration (ten standard scopes), shorthand options
    (`read-all`, `{}`), the GitHub App-Only permission taxonomy, and the `id-token`
    exception. Practitioners reading the conceptual overview need this reference to
    actually configure their workflows.
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer security pipeline, Layer 3 is
    "Permission separation"): This reference is the implementation documentation
    for Layer 3. It specifies how the read/write separation is configured, not just
    that it exists as a security layer.
  - `docs-ghaw-concurrency-reference.md` Claim 6 (Safe Outputs jobs process
    independently from agent jobs, with `cancel-in-progress: false` when
    `safe-outputs.concurrency-group` is configured): The concurrency reference
    explains the job-level concurrency behavior of the separate safe-outputs job;
    this reference explains the permission architecture that necessitates that
    separate job in the first place.

- **Contradicts**: None identified. No existing source note makes claims that
  conflict with the read-only-by-default model, the safe-outputs routing of writes,
  or the `id-token` exception. The permission model is consistently stated across
  all corpus notes that touch permissions. No contradiction issue required.

- **Novel** (what this note adds that no prior source covers):
  - **The four-reason security rationale for the read/safe-outputs separation**
    (Claim 2): No existing note articulates all four purposes together (audit
    trail, blast radius, compliance gates, prompt injection defense).
    `docs-ghaw-how-they-work.md` names the five-layer model but does not state
    these four reasons. This is the most complete security framing for the
    safe-outputs design in the corpus.
  - **Explicit cost quantification of safe outputs** (Claim 3): "One extra job"
    as the concrete overhead is not stated in any prior note.
  - **The ten standard read permission scopes enumerated** (Claim 4): Prior notes
    reference specific scopes in examples but no existing note documents the full
    standard scope taxonomy.
  - **`read-all` and `{}` shorthand options** (Claim 5): Neither shorthand is
    documented in any existing source note.
  - **GitHub App-Only Permissions taxonomy** (Claim 6): The three-category
    taxonomy (repository-level, organization-level, user-level) with the
    "must always be declared as `read`" constraint is entirely new to the corpus.
  - **`id-token: write` anomaly and its safe-outputs exception** (Claims 7–8):
    The special-case behavior of `id-token` — write-only (never read), compile-time
    rejection of `read`, no repository modification, no safe-outputs requirement —
    is not documented in any existing source note.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add the canonical `permissions: + safe-outputs:` pattern as the harness
  permission template** (Claim 1, Concrete Artifacts): The page's opening example
  is the definitive configuration template for any gh-aw workflow that needs to
  modify GitHub state. Add this as the recommended starting point for workflow
  permission design. Pair with `docs-ghaw-how-they-work.md` Claim 4 as the
  conceptual rationale.

- **Add the ten standard read scopes as a reference table** (Claim 4): Practitioners
  designing workflows need to know which scopes exist so they can apply least
  privilege to read access. The full list is not available in any current guide note.

- **Document `read-all` and `{}` as permission design boundary cases** (Claim 5):
  Add `{}` for computation-only workflows and `read-all` for inspection workflows.
  Recommend that production workflows use explicit scopes rather than `read-all`.

- **Add GitHub App-Only Permissions as an advanced configuration note** (Claim 6):
  Warn practitioners that organization-level and some repository-level operations
  require additional GitHub App authentication beyond GITHUB_TOKEN.

- **Document `id-token: write` as the OIDC exception** (Claims 7–8): For workflows
  using OIDC-based cloud deployment (AWS, GCP, Azure), `id-token: write` is required
  and does not violate the read-only permission policy. This is a common confusion
  point when practitioners first encounter a gh-aw workflow deploying to cloud
  infrastructure.

### Chapter 03: Safety and Verification

- **Add the four-reason rationale as the canonical justification for safe outputs**
  (Claim 2): The four security purposes (audit trail, blast radius, compliance
  gates, prompt injection defense) are the complete articulation of why the read/write
  separation exists. Add as the conceptual foundation for the Ch03 section on
  permission design in agentic workflows.

- **Name "one extra job" as an explicit and acceptable trade-off** (Claim 3): When
  discussing safe-outputs overhead, cite this framing. The cost is quantified by the
  platform team and the benefit is characterized as non-negotiable.

- **Document `id-token: write` as the only safe-outputs exception** (Claim 8):
  Ch03's safety rules should note that `id-token: write` is the documented exception
  to "all writes go through safe outputs" — because OIDC token issuance is stateless
  with respect to GitHub repository state.

## Extraction Notes

1. **Source is a reference page, not a conceptual overview**: This is a `reference/`
   section page — it documents configuration options precisely. Claims are settled
   for the platform; they describe how the configuration works, not how practitioners
   should think about it.

2. **`reference/safe-outputs` not deeply extracted**: The permissions page links
   heavily to `reference/safe-outputs` for the write operation mechanism. A separate
   WebFetch of that page was attempted but returned only a structural summary. The
   safe outputs mechanism is covered at the conceptual level in
   `docs-ghaw-how-they-work.md` Claim 5; the full safe outputs configuration
   reference is not yet in the corpus.

3. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with the
   current gh-aw platform as of 2026-05-10.

4. **No contradictions filed**: Reviewed all existing corpus source notes. No
   claims in this source materially oppose existing notes. The permissions model is
   consistently stated across all corpus notes that touch permissions. No
   contradiction issue required.
