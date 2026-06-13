---
source_url: https://github.blog/changelog/2026-06-12-copilot-code-review-new-configurations-and-controls
source_type: docs
title: "Copilot code review: New configurations and controls"
author: GitHub (official changelog)
date_published: 2026-06-12
date_extracted: 2026-06-13
last_checked: 2026-06-13
status: current
confidence_overall: settled
issue: "#1168"
---

# Copilot Code Review: New Configurations and Controls

> GitHub's June 12, 2026 changelog announcing three governance and customization improvements
> to Copilot code review: organization-level runner configuration with lock enforcement,
> content exclusion support at repository/organization/enterprise levels, and removal of the
> 4,000-character limit on custom instruction files — extending the governance surface for
> organizations deploying code review at scale.

## Source Context

- **Type**: docs (GitHub official product changelog, June 12, 2026; approximately 200-300 words
  across three feature sections)
- **Author credibility**: GitHub engineering team announcing production feature updates. Authoritative
  for the existence of these features, their navigation paths, and their availability. Not
  authoritative for: real-world compliance coverage of content exclusions, whether longer
  instruction files materially change review quality, or how runner lock enforcement interacts
  with existing repo-level configurations in edge cases.
- **Scope**: Three specific configuration improvements to Copilot code review: (1) org-level
  runner defaults with lock settings, (2) content exclusion integration at repo/org/enterprise
  levels, and (3) removal of the 4,000-character limit on instruction files. Does NOT cover:
  how these changes interact with the June 2 agent skills and MCP tier features; whether content
  exclusions affect skill invocations or MCP server calls; or quantitative impact of longer
  instruction files on review quality.

## Extracted Claims

### Claim 1: Organization admins can now set a default runner for Copilot code review at the organizational level, automatically applied across all repositories without requiring per-repo configuration

- **Evidence**: Official GitHub product changelog describing the organizational runner
  configuration capability and navigation path.
- **Confidence**: settled (product fact stated in official changelog)
- **Quote**: (no direct quote; WebFetch processed the source through a small model and verbatim
  text was not recoverable — see Our assessment for paraphrase)
- **Our assessment**: The first WebFetch returned: "Organization admins can now configure
  default runners at the organizational level rather than requiring individual repository setup."
  This extends the per-repository runner configuration documented in
  `docs-github-copilot-code-review-actions-billing.md` (Claim 6: "GitHub Copilot code review
  supports self-hosted runners and larger GitHub-hosted runners") and the configurable Actions
  workflow layer from `docs-github-copilot-code-review-skills-mcp-tier.md` (Claim 4:
  "Configurable Actions workflows give you control over the compute and environment Copilot
  uses for review"). Previously, runner configuration was per-repository; org-level defaults
  reduce setup overhead for fleets onboarding many repositories simultaneously. For Ch02
  (Harness Engineering): the runner layer now has both per-repo and org-level configuration
  surfaces. For Ch05 (Team Adoption): org-level defaults simplify fleet-wide deployment.

### Claim 2: Organization admins can lock runner settings so organizational defaults override repository-level runner configurations

- **Evidence**: Official GitHub changelog describing lock enforcement behavior alongside the
  org-level runner default capability.
- **Confidence**: settled (product fact stated in official changelog)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The first WebFetch returned: "lock settings to override repository-level
  configurations." The lock introduces a governance hierarchy where org defaults take precedence
  over repo-level settings. This matters for enterprise environments with compliance requirements
  (e.g., "all code reviews must run on self-hosted runners within our network boundary, not
  GitHub-hosted public runners"). Previously, any repository admin could configure their own
  runner type; the lock removes that autonomy when organizational governance requires it. For
  Ch05: the lock pattern is a first-class governance control for regulated industries where
  compute environment is an audit concern. For Ch02: document the lock as the enforcement
  mechanism that makes org-level runner policy binding rather than advisory.

### Claim 3: The navigation path for organizational runner configuration is organization settings → Copilot → Runner type → Runner type configuration

- **Evidence**: First WebFetch captured this path with bolded navigation arrows, consistent
  with how GitHub changelogs format UI navigation paths.
- **Confidence**: settled (navigation path stated in source)
- **Quote**: (no direct quote; path inferred from bolded markdown in WebFetch output)
- **Our assessment**: The path is in organization settings, not repository settings — confirming
  the feature operates at the organizational governance layer. Contrast with the per-repository
  tier configuration from `docs-github-copilot-code-review-skills-mcp-tier.md` (Claim 14:
  "Navigate to repository settings → Copilot → Code review → Review effort level"). The two
  paths form a clear mental model: org settings govern runner type; repo settings govern
  analysis tier, skills, and MCP. For Ch02: document both paths to avoid conflating org-level
  and repo-level configuration surfaces.

### Claim 4: Copilot code review now respects content exclusion settings at repository, organization, and enterprise levels, preventing the agent from accessing specified files or directories during reviews

- **Evidence**: Official GitHub changelog announcing content exclusion integration as a new
  capability across three hierarchy levels.
- **Confidence**: settled (product fact stated in official changelog)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Both WebFetch attempts confirmed: Copilot code review respects content
  exclusion settings at repository, organization, and enterprise levels using path-based rules.
  Use cases include: preventing review of files containing hardcoded secrets, excluding
  proprietary algorithm implementations from AI analysis, complying with data handling
  agreements restricting AI access to certain code paths, and reducing noise on generated
  code (vendored libraries, proto-generated files). The three-tier hierarchy allows layered
  policy: enterprise admins set blanket exclusions; org admins add org-specific exclusions;
  repo admins add project-specific exclusions. For Ch05 (Team Adoption): content exclusion
  removes a key deployment blocker for organizations with compliance constraints on AI
  accessing certain code — the feature converts the binary "enable everywhere or nowhere"
  into granular, path-scoped access control. For Ch02 (Harness Engineering): content
  exclusion is a platform team responsibility to configure before fleet-wide code review
  deployment.

### Claim 5: The previously enforced 4,000-character limit on custom instruction files (`.github/copilot-instructions.md` and `*.instructions.md`) has been removed, enabling more extensive review customization

- **Evidence**: Official GitHub changelog announcing the character limit removal for both
  instruction file types.
- **Confidence**: settled (product fact stated in official changelog)
- **Quote**: "allowing additional customization and flexibility in your custom instructions"
  (second WebFetch placed this phrase in double quotes — likely a verbatim fragment from
  the source's description of the benefit)
- **Our assessment**: The 4,000-character limit was a significant constraint for teams with
  detailed review standards. Removing it allows: comprehensive style guides, multi-section
  coding standards, detailed security patterns, and team-specific domain knowledge — all in
  a single instruction file. Important distinction: `.github/copilot-instructions.md` and
  `*.instructions.md` are DISTINCT from `.github/skills/code-review/SKILL.md` documented
  in `docs-github-copilot-code-review-skills-mcp-tier.md` (Claim 12). Instruction files
  provide general context and guidelines to the code review agent; SKILL.md files define
  agentic skill invocations with tools and external calls. Both customization surfaces now
  have no length constraint. For Ch02: document both file types in the customization surface
  matrix, explaining their different roles. For Ch01: teams that split instructions across
  multiple files to work around the 4,000-character limit can consolidate them.

### Claim 6: The June 12 governance improvements are additive to the June 2 customization features, together completing a seven-layer configuration surface for Copilot code review

- **Evidence**: Cross-source analysis of June 2 and June 12 changelogs showing non-overlapping
  feature domains.
- **Confidence**: settled (factual composition of official product announcements)
- **Quote**: (no direct quote; this is the Miner's cross-source synthesis)
- **Our assessment**: The June 2 changelog (`docs-github-copilot-code-review-skills-mcp-tier.md`)
  addressed *what the agent does and how deep it analyzes* (skills, MCP context, analysis tier).
  The June 12 changelog addresses *what the agent can access and from where it runs* (content
  exclusions, runner governance) plus *how extensively it can be instructed* (character limit
  removal). Together, the seven layers as of June 12, 2026 are: (1) agent skills
  (`.github/skills/code-review/SKILL.md`), (2) MCP servers (repo settings → Copilot → MCP
  servers), (3) Actions workflow environment (configurable), (4) review tier (Low/Medium),
  (5) org runner default + lock (org settings → Copilot → Runner type), (6) content exclusions
  (repo/org/enterprise), (7) instruction files (`.github/copilot-instructions.md`, now
  unlimited). For Ch02: document this as the complete code review harness configuration
  matrix. For Ch05: teams evaluating Copilot code review should assess all seven layers.

## Concrete Artifacts

### Feature Summary (from changelog, June 12, 2026)

```
Copilot Code Review — New Configurations and Controls (June 12, 2026)
Source: https://github.blog/changelog/2026-06-12-copilot-code-review-new-configurations-and-controls

Feature 1: Organization Runner Controls
  Capability: Set a default runner at the org level, applied automatically to all repos
  Lock:       Org defaults can override repository-level runner configurations
  Navigation: Organization settings → Copilot → Runner type → Runner type configuration

Feature 2: Content Exclusion Support
  Scope:      Repository, organization, and enterprise levels
  Behavior:   Prevents Copilot from accessing specified files/directories during reviews
  Use cases:  Secrets files, proprietary code, generated/vendored files, PII-adjacent paths

Feature 3: Removed Character Limits
  Files:      .github/copilot-instructions.md and *.instructions.md
  Prior limit: 4,000 characters (now removed)
  Benefit:    "allowing additional customization and flexibility in your custom instructions"
```

### Complete Code Review Configuration Surface (as of June 12, 2026)

```
# Complete configuration surface for Copilot code review
# Compiled from June 2 + June 12 2026 changelogs

AGENT CONTEXT (what the agent reads during review):
  .github/skills/code-review/SKILL.md   → agent skill context (June 2)
  MCP servers (repo settings → Copilot → MCP servers) → external context (June 2)
  .github/copilot-instructions.md       → general instructions (now unlimited — June 12)
  *.instructions.md                     → additional instructions (now unlimited — June 12)

CONTENT GOVERNANCE (what the agent can access):
  Content exclusion settings            → repo / org / enterprise levels (June 12)

COMPUTE CONFIGURATION (where the agent runs):
  Org-level runner default              → org settings → Copilot → Runner type (June 12)
  Runner lock                           → org setting overrides repo-level config (June 12)
  Per-repo Actions workflow             → configurable compute environment (June 2)

ANALYSIS DEPTH (how thoroughly the agent reviews):
  Review tier (Low / Medium)            → repo settings → Copilot → Code review (June 2)
```

### Copilot Code Review Feature Evolution Arc (updated to June 12, 2026)

```
Date        Source Note                                          What Changed
----------  ---------------------------------------------------  ------------------------------------
2026-04-08  docs-github-copilot-pr-review-metrics               Measurement: code review API fields
2026-04-27  docs-github-copilot-code-review-actions-billing     Billing: AI Credits + Actions mins
2026-05-12  docs-github-copilot-code-review-comment-ux          UX: severity labels + grouping
2026-05-19  docs-github-copilot-cca-apply-review-feedback       Action: Fix with Copilot dialog
2026-06-02  docs-github-copilot-code-review-skills-mcp-tier     Customization: skills + MCP + tier
2026-06-12  THIS NOTE (code-review-config-controls)             Governance: org runner defaults +
                                                                 content exclusion + unlimited
                                                                 instruction files
```

## Cross-References

- **Extends** `docs-github-copilot-code-review-actions-billing.md` (issue #445):
  - Claim 6 of that note: "GitHub Copilot code review supports self-hosted runners and larger
    GitHub-hosted runners which are billed at different rates than standard GitHub-hosted runners."
    This source adds organizational governance on top of per-repo runner capability: org admins
    can now set a default runner and lock it. The April 27 note established that runner type is a
    configuration variable; this source establishes it is now also a governance variable with
    org-level enforcement. Together: April 27 reveals that runner configuration exists and affects
    billing; June 12 reveals it can be governed centrally with lock enforcement.

- **Extends** `docs-github-copilot-code-review-skills-mcp-tier.md` (issue #1052):
  - Claim 4: "Configurable Actions workflows give you control over the compute and environment
    Copilot uses for review." Claims 1-3 of this note add the organizational governance layer
    on top of that workflow configurability — org admins can now set and lock runner defaults
    rather than each repo configuring its own. The June 2 source established the configuration
    surface; this source establishes who can enforce standards fleet-wide.
  - Claim 12: SKILL.md files provide agent skill context. This source's character limit removal
    for `copilot-instructions.md` and `*.instructions.md` is a distinct but complementary
    customization mechanism. Instruction files and SKILL.md files serve different purposes:
    instruction files provide general guidelines; SKILL.md files define agentic skill invocations.
    Both are now length-unlimited. Platform teams should understand and maintain both.
  - Claims 13-14 establish that per-repo tier and MCP configuration live in repository settings.
    This source's org runner configuration lives in organization settings — a parallel but distinct
    hierarchy level. Mental model: org settings govern runner; repo settings govern tier, skills, MCP.

- **Extends** `docs-github-copilot-code-review-comment-ux.md` (issue #723):
  - That source (May 12) documented UX noise reduction via severity labels and comment grouping.
    This source adds content exclusion (Claim 4), which reduces noise at the source: files that
    generate irrelevant review comments can be excluded entirely, reducing total comment volume
    before grouping or severity labeling applies. Teams that adopted May 12's noise-reduction
    features should evaluate whether content exclusion can further reduce irrelevant comment
    volume by scoping agent access to relevant code paths only.

- **Contradicts**: None found. No existing source note claims runner configuration is only
  available at repository level, or that content exclusion is not supported, or that instruction
  files have a character limit. All three June 12 features extend prior notes rather than
  contradict them. No contradiction issue to file.

- **Novel**:
  - **Org-level runner configuration with lock enforcement**: No prior corpus source documents
    organizational-level runner defaults or lock enforcement for Copilot code review. Prior
    sources documented per-repo runner type support but not organizational governance.
  - **Content exclusion support for code review**: No prior corpus source documents content
    exclusion integration with Copilot code review. This is the first documentation that the
    review agent respects content exclusion policies set at repo/org/enterprise levels.
  - **4,000-character instruction file limit removal**: No prior corpus source documents this
    limit or its removal. The `.github/copilot-instructions.md` and `*.instructions.md` file
    types are documented here for the first time as Copilot code review customization surfaces,
    distinct from SKILL.md agent skills.
  - **Three-tier governance hierarchy (repo / org / enterprise) for content exclusion**: First
    corpus source to document this governance hierarchy for any Copilot code review configuration.
    Prior sources documented per-repo settings (tier, MCP, skills); this source introduces the
    org and enterprise tiers as configuration levels for content access policy.

## Guide Impact

### Chapter 02: Harness Engineering

- **Document the complete seven-layer code review configuration surface**: As of June 12, 2026,
  Copilot code review has seven configurable layers: (1) agent skills, (2) MCP servers,
  (3) Actions workflow environment, (4) review tier, (5) org runner default + lock,
  (6) content exclusions, (7) instruction files (now unlimited). No prior guide section captures
  all seven. Add or update a "Code Review Configuration Surface" section referencing both the
  June 2 and June 12 changelogs.
- **Content exclusion as a pre-deployment checklist item**: Before enabling Copilot code review
  fleet-wide, platform teams should define content exclusion policies at the org or enterprise
  level. Secrets patterns, vendored dependencies, generated files, and compliance-restricted
  paths should be excluded before the first reviews run. Content exclusion is easier to set
  before broad rollout than to retrofit after teams have started dismissing high-volume irrelevant
  comments.
- **Instruction file customization surface**: Document `.github/copilot-instructions.md` and
  `*.instructions.md` as a customization surface distinct from SKILL.md. Instruction files are
  appropriate for: general review standards, coding conventions, team norms, security guidelines.
  SKILL.md files are appropriate for: agentic skill invocations, tool calls, external data access.

### Chapter 05: Team Adoption

- **Updated code review deployment checklist (as of June 12, 2026)**: Six deployment layers:
  (1) Billing model — `docs-github-copilot-code-review-actions-billing.md`
  (2) Triage UX — `docs-github-copilot-code-review-comment-ux.md`
  (3) Suggestion application — `docs-github-copilot-cca-apply-review-feedback.md`
  (4) Org context injection (skills + MCP) — `docs-github-copilot-code-review-skills-mcp-tier.md`
  (5) Analysis depth (Low/Medium tier) — same note
  (6) Governance controls (content exclusion + org runner + instruction files) — this source
  Teams that evaluated before June 12, 2026 are missing layer 6 entirely.
- **Content exclusion as an adoption unlocker for regulated organizations**: Organizations that
  blocked Copilot code review deployment due to AI access concerns can now use content exclusion
  to precisely scope what the agent reviews. This converts an all-or-nothing adoption decision
  into a scoped, compliant one.
- **Org runner lock for regulated environments**: Enterprises with requirements around compute
  environment (air-gapped networks, on-premises, specific network boundaries) can enforce
  self-hosted runner usage via org-level lock without per-repo admin cooperation.

### Chapter 01: Daily Workflows

- **Instruction file customization is now length-unconstrained**: Teams maintaining
  `.github/copilot-instructions.md` around the 4,000-character limit can now write
  comprehensive review guidance without truncation. Note: keep instructions focused — broader
  context is better than exhaustive context that dilutes the agent's attention.

## Extraction Notes

1. **WebFetch returned AI-processed summaries, not verbatim text**: Both WebFetch attempts
   returned content processed through a small model rather than the raw source text. As a
   result, all quotes except one are marked `(no direct quote; see paraphrase in Our assessment)`.
   The one verbatim fragment used — "allowing additional customization and flexibility in your
   custom instructions" — appeared in double quotes in the second WebFetch output and is
   likely a direct lift from the source. The Assayer should verify this and all navigation
   paths against the source URL directly.

2. **Navigation paths**: The org runner configuration path (Copilot → Runner type → Runner type
   configuration) appeared with bolded navigation arrows in the first WebFetch output, consistent
   with how GitHub changelogs format UI paths. It is captured in Claim 3's assessment but not
   presented as a verbatim quote given the AI-processing caveat.

3. **Content exclusion format not detailed**: The source confirms content exclusion is supported
   but does not describe the specific file format or syntax for path-based rules. The mechanics
   likely follow GitHub's existing content exclusion format but this is not confirmed from this
   source alone. A linked documentation page was not fetched.

4. **Instruction files vs. SKILL.md**: The source names `.github/copilot-instructions.md` and
   `*.instructions.md` as the affected file types. These differ from `.github/skills/code-review/SKILL.md`
   (agent skills). The distinction is noted throughout Claims 5-6 and the Concrete Artifacts
   section to prevent conflation by guide readers.

5. **No sub-pages followed**: The changelog likely links to documentation pages for each feature.
   Content exclusion docs would elaborate on rule format; runner lock docs would detail the
   hierarchy override behavior. These were not fetched.

6. **No contradictions to file**: All three features extend prior corpus capabilities. No existing
   source makes claims this source would refute. No contradiction issue required.
