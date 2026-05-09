---
source_url: https://github.blog/changelog/2026-05-08-more-flexible-secrets-and-variables-for-copilot-cloud-agent
source_type: docs
title: "More flexible secrets and variables for Copilot cloud agent"
author: GitHub (official changelog)
date_published: 2026-05-08
date_extracted: 2026-05-09
last_checked: 2026-05-09
status: current
confidence_overall: settled
issue: "#573"
---

# More Flexible Secrets and Variables for Copilot Cloud Agent (GitHub Changelog)

> GitHub's May 2026 announcement of dedicated "Agents" secrets and variables for
> Copilot Cloud Agent — enabling organization-level credential distribution and
> per-repository access control, replacing the previous per-repo `copilot` environment
> workaround that made multi-repository MCP server and package registry rollouts painful.

## Source Context

- **Type**: docs (GitHub official product changelog, May 8, 2026, ~200 words + linked
  GitHub Docs page "Configuring secrets and variables for Copilot cloud agent")
- **Author credibility**: GitHub engineering team announcing a production feature change.
  Authoritative for the fact that these capabilities exist, their scope (organization-level,
  repository-level, per-repo access control), and the stated behavioral semantics. Not
  a credible source for operational outcomes of this change — no empirical data on
  adoption friction reduction is provided.
- **Scope**: Introduction of a dedicated "Agents" secrets/variables category for CCA,
  and the three new capabilities it unlocks (org-level config, repo-level "Agents"
  section, per-repo access control). Covers the primary use cases: private resource
  access and MCP server configuration. Does NOT cover: the secrets/variables API surface
  (endpoints, scopes, request format), pricing or quota implications, interaction with
  Actions reusable workflows, how CCA secrets differ from Actions secrets in terms of
  encryption or storage, or whether org-level variables support expressions/templating.
  The linked Docs page ("Configuring secrets and variables for Copilot cloud agent")
  returned HTTP 404 during extraction and could not be read.

## Extracted Claims

### Claim 1: CCA operates in a background GitHub Actions-powered development environment, and secrets and variables are the mechanism for giving it access to private resources and MCP servers

- **Evidence**: Opening two sentences of the changelog entry, describing CCA's runtime
  environment and the role of secrets/variables in it.
- **Confidence**: settled (official product documentation of an existing feature)
- **Quote**: "When you delegate a task to Copilot cloud agent, it works in the background
  in its own development environment powered by GitHub Actions. You can pass secrets and
  variables to the agent to give it access to private resources or to configure MCP
  servers."
- **Our assessment**: This is a foundational architectural fact about CCA: it is not a
  stateless API call but a stateful background process running inside GitHub Actions. The
  implication is that CCA's access to private resources (package registries, internal APIs,
  MCP servers) is gated entirely on what secrets and variables have been configured for it.
  Practitioners deploying CCA need to treat secrets/variables configuration as a first-class
  deployment concern — not an afterthought. The explicit mention of MCP server configuration
  as a first-class use case confirms that MCP integration is a primary driver of this feature.

### Claim 2: Before May 2026, CCA secrets/variables had to be configured per-repository in a dedicated `copilot` environment under Actions settings, making cross-repository rollout of shared credentials painful

- **Evidence**: Changelog's explicit "until now" statement describing the prior state.
- **Confidence**: settled (GitHub's own description of the prior product state)
- **Quote**: "Until now, these had to be configured one repository at a time, in a
  `copilot` environment under the repository's Actions settings. That made it painful to
  roll out shared configuration (e.g., an internal package registry token or a common MCP
  server) across many repositories."
- **Our assessment**: The prior state is significant: teams deploying CCA at scale (many
  repos in an org) had to manually configure secrets in every repository. The word "painful"
  is GitHub's own characterization, which is unusually candid. The two examples cited —
  "an internal package registry token" and "a common MCP server" — reveal the primary
  real-world deployment patterns GitHub sees: private artifact access and shared tooling
  integration. For practitioners currently using the old per-repo `copilot` environment
  approach, this change offers a direct migration path to centralized management.

### Claim 3: The May 2026 update introduces a dedicated "Agents" secrets/variables type for CCA, logically separate from the existing Actions, Codespaces, and Dependabot types

- **Evidence**: Changelog's explicit description of the new product structure.
- **Confidence**: settled (product fact — this categorization now exists in GitHub settings UI)
- **Quote**: "Today, Copilot cloud agent gets its own dedicated 'Agents' secrets and
  variables, sitting alongside the existing 'Actions', 'Codespaces', and 'Dependabot'
  types."
- **Our assessment**: The introduction of a separate "Agents" category is architecturally
  meaningful: it signals that GitHub is treating CCA as a distinct secrets principal, not
  a variant of Actions. This separation has security implications — secrets configured for
  "Actions" do not automatically flow into CCA, and vice versa. Teams migrating from the
  old `copilot` environment approach must re-configure secrets under the new "Agents" type;
  they cannot simply rely on existing Actions secrets being inherited. This is also a signal
  about GitHub's roadmap: a dedicated type suggests first-class expansion of agent capabilities
  over time, mirroring how Dependabot got its own type when its access model diverged from
  Actions.

### Claim 4: Organizations can now configure CCA secrets and variables at the organization level for the first time, distributable across any or all repositories

- **Evidence**: First bullet point under the new capabilities list in the changelog.
- **Confidence**: settled (official product announcement of a newly available capability)
- **Quote**: "Configure secrets and variables at the organization level for the first
  time, and share them across any or all repositories in your organization."
- **Our assessment**: The phrase "for the first time" confirms this capability is net-new,
  not a refinement of an existing mechanism. Org-level secrets/variables eliminate the
  O(n) configuration cost of adding a shared credential to n repositories — particularly
  valuable for large organizations where CCA might be deployed across dozens or hundreds
  of repos. The "any or all" phrasing implies granular distribution control (see Claim 6),
  not a binary all-or-nothing toggle. Practitioners running centralized developer platform
  teams should treat this as the preferred provisioning path for org-wide credentials.

### Claim 5: Repository-level CCA secrets/variables now have a dedicated "Agents" section in repository settings, separate from Actions configuration

- **Evidence**: Second bullet point under the new capabilities list.
- **Confidence**: settled (product fact about UI structure)
- **Quote**: "Manage repository-level secrets and variables in a dedicated 'Agents'
  section in your repository settings, separate from your Actions configuration."
- **Our assessment**: The separation is practically important for teams that manage
  Actions secrets and CCA secrets independently. Previously, CCA secrets lived inside
  the Actions settings under a `copilot` environment — a non-obvious location. A dedicated
  "Agents" section reduces the discoverability problem for developers trying to configure
  CCA without deep GitHub Actions familiarity. The separation also reduces risk of
  accidentally exposing CCA secrets to Actions workflows or vice versa.

### Claim 6: Organization-level CCA secrets/variables support per-repository access control, matching the access model already used for Actions secrets

- **Evidence**: Third bullet point under the new capabilities list.
- **Confidence**: settled (product announcement of a documented capability)
- **Quote**: "Choose which repositories in an organization can access each secret or
  variable, just like with Actions."
- **Our assessment**: The "just like with Actions" phrasing is intentional — it signals
  that the access control model is familiar to practitioners already managing Actions
  secrets at scale. Admins who know how to restrict an Actions secret to specific repos
  can apply the same mental model to CCA secrets. This reduces the learning curve for
  platform teams. The implication for security-conscious teams: a CCA secret provisioned
  at the org level does not implicitly become available to every repo — repositories must
  be explicitly granted access. This is a tighter default than the enterprise-level CCA
  enablement policy (which enables CCA for all repos in a selected org by default, per the
  existing governance note).

### Claim 7: The primary benefit is eliminating duplicate configuration across repositories when deploying shared CCA credentials at scale

- **Evidence**: Closing sentence of the changelog.
- **Confidence**: settled (vendor summary of the stated benefit)
- **Quote**: "This makes it much easier to configure Copilot cloud agent at scale, without
  having to duplicate configurations across every repository."
- **Our assessment**: The benefit is real and direct. The prior O(n) per-repo configuration
  overhead was a genuine deployment blocker for organizations wanting to deploy CCA
  uniformly. "Duplicate configurations" is the specific pain GitHub is solving — not
  discoverability or complexity, but operational scale. For practitioners: if you have a
  shared MCP server URL or an internal artifact registry token that every CCA-enabled repo
  needs, org-level configuration is now the correct approach. Repository-level "Agents"
  secrets should be reserved for repo-specific credentials.

## Concrete Artifacts

### New Secrets/Variables Type Structure (from changelog)

```
GitHub Settings → Secrets and Variables
  Previous types:
    - Actions
    - Codespaces
    - Dependabot

  New type (added May 2026):
    - Agents   ← CCA-specific secrets and variables

Organization-level path:
  Organization Settings → Secrets and Variables → Agents
    → Can specify which repositories can access each secret/variable

Repository-level path:
  Repository Settings → Secrets and Variables → Agents
    → Dedicated section, separate from Actions configuration
```

### Prior State vs. New State

```
BEFORE (pre-May 2026):
  Per-repo setup required:
    Repository Settings → Environments → copilot → Secrets
  
  Limitation: Repeat for every CCA-enabled repository
  Use case friction: "painful to roll out shared configuration
    (e.g., an internal package registry token or a common MCP server)
    across many repositories"

AFTER (May 2026+):
  Organization-level:
    Org Settings → Secrets and Variables → Agents
    → Configure once, distribute to any/all repositories
  
  Repository-level:
    Repo Settings → Secrets and Variables → Agents (new dedicated section)
    → Repository-specific credentials
```

### Primary Use Cases Cited by GitHub

```
1. Internal package registry token
   → shared org credential; configure once at org level,
     distribute to all CCA-enabled repos

2. Common MCP server configuration
   → shared tooling; provision at org level rather than
     duplicating server URL / auth token per repository
```

## Cross-References

- **Extends** `docs-github-copilot-cca-custom-properties.md`: That note covers the
  CCA governance layer (which orgs and repos CCA is *enabled* for, via enterprise policy
  API). This note covers the CCA runtime configuration layer (what credentials and
  tools the agent can *access* once it's running). Together they describe the full CCA
  deployment surface: Claim 5 in the custom-properties note notes that CCA is enabled
  for all repos in selected orgs by default (permissive default), while Claim 6 here
  notes that org-level secrets require per-repo access grants (restrictive default).
  The two defaults pull in opposite directions — a practitioner deploying CCA must
  understand both to avoid either silent over-exposure (CCA enabled everywhere) or
  silent under-provisioning (secrets not reaching all needed repos).

- **Complements** `docs-github-copilot-cca-custom-properties.md` Claim 6 (MCP policy
  exception): That note documents that the enterprise MCP Registry URL / Restrict MCP
  Access policies do NOT apply to CCA, meaning MCP governance must be handled separately.
  This note provides the mechanism for that separate governance: org-level "Agents"
  secrets/variables are where MCP server configuration for CCA should live. The two notes
  together clarify the CCA MCP governance path: enterprise MCP policies don't cover CCA
  → use org-level Agents secrets/variables to configure and control what MCP servers CCA
  can access.

- **Corroborates** `blog-bswen-mcp-token-cost.md` in that MCP server configuration is
  a high-operational-cost concern: Bswen's note documents that loading too many MCP
  servers bloats context significantly. This changelog note provides the mechanism for
  controlling which MCP servers are provisioned for CCA — org-level secrets/variables
  are the centralized control point for what MCP servers CCA can reach. A platform team
  can limit CCA's MCP exposure by selectively provisioning only approved server configs
  as org-level secrets, rather than letting individual repos add arbitrary MCP servers.

- **Complements** `docs-github-copilot-agent-skills-cli.md` (Claim 1 — package manager
  for agent capabilities): That note documents `gh skill` as a mechanism for distributing
  agent capabilities (skills) across repos. This note documents org-level secrets/variables
  as a mechanism for distributing agent credentials (secrets). Both address the same
  organizational deployment problem — "how do I provision CCA consistently across many
  repositories?" — from different angles (capabilities vs. credentials).

- **Novel**:
  - First source in corpus to document the CCA dedicated "Agents" secrets/variables type
    and its separation from the `copilot` environment under Actions.
  - First source to describe org-level secrets/variables for CCA and their per-repo
    access control model.
  - Clarifies that MCP server configuration for CCA is done via secrets/variables (not
    via enterprise MCP policies, which don't apply to CCA) — closes the gap left open by
    the MCP policy exception in `docs-github-copilot-cca-custom-properties.md`.

## Guide Impact

### Chapter 02: AI Coding Assistants / Copilot

- **Section "Deploying CCA in an organization"** (new or existing): Add org-level
  secrets/variables as the recommended path for shared CCA credential distribution.
  Distinguish between org-level secrets (shared across repos, with per-repo access grants)
  vs. repo-level secrets (repo-specific, in dedicated "Agents" section). Cite Claim 4 for
  the capability and Claim 7 for the motivation (eliminate per-repo duplication). Note that
  the prior `copilot` environment under Actions is superseded.

- **Section "MCP server configuration for CCA"** (add if not present): Use this source
  to explain that MCP servers for CCA are configured via secrets/variables (org-level
  "Agents" type), not via enterprise MCP policies (which do not apply to CCA per
  `docs-github-copilot-cca-custom-properties.md` Claim 6). This closes the governance gap
  that the custom-properties note left open. Cite Claim 1 (CCA runtime env + MCP use case)
  and Claim 2 ("a common MCP server" as an explicit use case).

### Chapter 07: Enterprise AI Adoption and Governance (planned or equivalent)

- **Section "CCA configuration governance"**: Pair with `docs-github-copilot-cca-custom-properties.md`
  to present the full two-layer CCA governance picture:
  - Layer 1 (Access): Enterprise policy API controls which orgs/repos can USE CCA (custom-properties note).
  - Layer 2 (Credentials): Org-level Agents secrets control what CCA can ACCESS at runtime (this note).
  - Note the polarity mismatch: Layer 1 defaults to permissive (all repos in selected org), Layer 2
    requires explicit repo grants for org secrets. Practitioners must configure both layers deliberately.

- **Section "Enterprise AI footguns"**: Add the runtime configuration equivalent of the
  custom-property timing footgun: migrating from the old `copilot` environment approach
  requires re-creating secrets under the new "Agents" type — old `copilot` environment
  secrets are NOT automatically migrated or inherited by the "Agents" type.

## Extraction Notes

1. **Source is intentionally brief**: The changelog itself is ~200 words. A linked GitHub
   Docs page ("Configuring secrets and variables for Copilot cloud agent") was referenced
   but returned HTTP 404 during extraction. All claims are sourced solely from the changelog
   text. The Docs page likely contains the procedural detail (UI steps, API surface, quota
   limits) that would extend these claims. An Assayer re-check of the Docs page when it
   becomes accessible is recommended.
2. **No contradictions to file**: This source does not contradict any existing source note.
   It is additive to `docs-github-copilot-cca-custom-properties.md` (governance layer) and
   complementary to MCP-related notes. No existing source claimed that CCA secrets must
   be managed per-repository forever or that org-level CCA configuration was available before
   May 2026.
3. **Migration implication not explicitly documented in source**: The claim that old `copilot`
   environment secrets are not automatically migrated to the new "Agents" type is an inference
   from the changelog's structure (it describes a "new" type, not a rename). This should be
   verified against the linked Docs page when accessible.
4. **MCP governance gap closed**: The CCA custom-properties note (Claim 6) documents that
   enterprise MCP policies don't cover CCA but does not say what mechanism DOES cover CCA's
   MCP access. This changelog closes that gap: org-level "Agents" secrets/variables are the
   correct mechanism. This is a cross-note synthesis, not a claim from either source alone.
