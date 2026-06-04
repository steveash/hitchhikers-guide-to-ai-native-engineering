---
source_url: https://github.blog/changelog/2026-06-02-shape-copilot-code-review-around-your-team
source_type: docs
title: "Shape Copilot code review around your team"
author: GitHub (official changelog)
date_published: 2026-06-02
date_extracted: 2026-06-04
last_checked: 2026-06-04
status: current
confidence_overall: settled
issue: "#1052"
---

# Shape Copilot Code Review Around Your Team

> GitHub's June 2, 2026 changelog announcing two public-preview capabilities for Copilot
> code review: agent skills and MCP server connections that inject organizational context
> into every review, and a new Medium analysis tier that routes complex PRs to a
> higher-reasoning model — the first corpus documentation of per-repository review-depth
> configuration and of MCP integration specifically for code review.

## Source Context

- **Type**: docs (GitHub official product changelog, June 2, 2026; approximately 400 words
  across four sections: opening, skills/MCP, medium tier, getting started)
- **Author credibility**: GitHub engineering team announcing a production preview. Authoritative
  for the fact that these features exist, the setup paths, the configuration locations, and
  the availability conditions. Not authoritative for: actual accuracy improvement rates from
  Medium tier, whether MCP latency materially affects review speed, or how much more AI
  Credits Medium consumes relative to Low (no quantified ratio given).
- **Scope**: Agent skills setup (`.github/skills/code-review/SKILL.md`), MCP server
  configuration for code review, per-repository tier selection (Low vs. Medium), and the
  shared-config relationship between code review and Copilot cloud agent. Does NOT cover:
  how agent skills differ from AGENTS.md or CLAUDE.md for code review purposes; what
  happens when MCP servers are unavailable during a review; whether Medium tier introduces
  meaningful latency increase; or whether skills/MCP configurations apply to PR auto-review
  vs. manual-trigger review differently.

## Extracted Claims

### Claim 1: Copilot code review can now invoke custom agent skills that call a team's internal tools and standards during the review, extending Copilot beyond its built-in analysis

- **Evidence**: Official GitHub product changelog with explicit description of the feature
  and its purpose.
- **Confidence**: settled (product fact — feature is in public preview, announced officially)
- **Quote**: "Custom agent skills invoke your team's internal tools and standards during a
  review, extending Copilot beyond its built-in analysis."
- **Our assessment**: This is a meaningful architectural shift. Prior to this, Copilot code
  review was limited to what the model could infer from the diff and repository context alone.
  Agent skills make the review agentic: the review agent can now call team-defined tools during
  the review pass, injecting results back into its analysis. For Ch02 (Harness Engineering):
  code review is now an agentic workflow where the agent can invoke tools, not just read files.
  For Ch05 (Team Adoption): the "extending Copilot beyond its built-in analysis" framing
  enables teams to encode their own review standards (style guides, security checks, org-specific
  patterns) as skills rather than relying entirely on the model's training data.

### Claim 2: MCP server connections pull context directly into code reviews from third-party platforms and internal systems a team already uses — including issue tracking, documentation, service catalogs, and incident tooling

- **Evidence**: Official GitHub product changelog enumerating the categories of external
  systems MCP can connect to.
- **Confidence**: settled (product fact stated in official changelog)
- **Quote**: "MCP server connections, once configured, pull context directly into the review
  from the third-party platforms and internal systems your team already uses, including issue
  tracking, documentation, service catalogs, and incident tooling."
- **Our assessment**: This is the most practically significant claim. The four categories named
  (issue tracking, documentation, service catalogs, incident tooling) are exactly the systems
  that human reviewers consult when reviewing PRs that touch service boundaries, shared
  libraries, or incident-prone components. MCP enables Copilot to do the same lookups
  automatically. For Ch04 (Agents): this is a concrete MCP integration pattern — code review
  as a MCP consumer, pulling context from org-internal systems. For Ch02 (Harness Engineering):
  this is how teams encode "what the reviewer needs to know" as machine-readable configuration
  rather than relying on institutional knowledge in senior engineers' heads. The framing
  "internal systems your team already uses" is significant: no new infrastructure required, only
  MCP configuration of existing systems.

### Claim 3: The vendor frames agent skills and MCP as solving the "senior engineer bottleneck" for consistency across repositories

- **Evidence**: Opening framing paragraph of the changelog's skills/MCP section.
- **Confidence**: anecdotal (vendor framing — plausible but not empirically supported in the
  source)
- **Quote**: "This means senior engineers stop being the bottleneck for consistency across
  repositories."
- **Our assessment**: This is a vendor adoption argument worth recording as framing even if
  unsubstantiated. The implicit claim: consistency currently depends on senior engineers reviewing
  PRs because they hold context that the diff alone does not contain (service catalog knowledge,
  team standards, incident history). If that context is injected into Copilot's review via MCP
  and agent skills, the per-PR dependency on senior reviewer availability is reduced. This is
  a plausible mechanism but the source provides no metrics. For Ch05: use this framing as a
  team adoption motivation — the target audience for agent skills and MCP is teams where
  review quality is inconsistent across repositories because senior context is not distributed.

### Claim 4: Configurable Actions workflows give teams control over the compute and environment Copilot uses for code review

- **Evidence**: Listed as one of four bullet points in the skills/MCP feature section.
- **Confidence**: settled (stated in official changelog)
- **Quote**: "Configurable Actions workflows give you control over the compute and environment
  Copilot uses for review."
- **Our assessment**: This extends the runner configuration capability documented in
  `docs-github-copilot-code-review-actions-billing.md` (Claim 6): that source noted self-hosted
  and larger runners were supported; this source confirms that the Actions workflow itself is
  configurable, not just the runner type. The implication: teams can now set environment
  variables, custom tooling, or network access within the review workflow. For Ch02: this is
  a harness engineering surface — code review is no longer a black-box service call but a
  configurable workflow with team-defined compute context.

### Claim 5: Skills and MCP configuration is shared between Copilot code review and Copilot cloud agent — platform teams configure once and get consistent behavior across both agents

- **Evidence**: Listed as one of four bullet points in the skills/MCP feature section.
- **Confidence**: settled (product guarantee stated in official changelog)
- **Quote**: "Shared configuration across review and cloud agent means platform teams invest
  once and get consistent behavior across both agents."
- **Our assessment**: This is a significant operational simplification. Prior to this, a team
  that wanted both code review and CCA to use the same internal tools would need to configure
  them separately. Shared configuration collapses this to a single investment. For Ch02: this
  is the key reason to invest in agent skills and MCP infrastructure — the configuration pays
  off across both code review and CCA. For teams that have already set up MCP for CCA (see
  `docs-github-copilot-cca-apply-review-feedback.md` context), code review inherits that
  configuration automatically.

### Claim 6: Existing MCP configurations for Copilot cloud agent automatically apply to Copilot code review without migration

- **Evidence**: Note in the "Setting up MCP servers" section of the changelog.
- **Confidence**: settled (migration note stated in official changelog)
- **Quote**: "Note: Any existing MCP configurations for Copilot cloud agent will now apply
  to Copilot code review automatically."
- **Our assessment**: Zero migration cost for teams already using MCP with CCA. This claim
  is operationally important for teams evaluating whether to enable the code review MCP feature:
  if they have already invested in CCA MCP configuration, code review becomes immediately MCP-
  capable. For Ch05 (Team Adoption): lower adoption barrier for code review MCP — existing CCA
  infrastructure transfers. Conversely, teams that have not yet invested in MCP can treat this
  as a prompt to do so once and get dual-agent benefit.

### Claim 7: Existing agent skills in the `.github/skills` directory automatically become available to Copilot code review if relevant to the review

- **Evidence**: Note in the "Setting up agent skills" section of the changelog.
- **Confidence**: settled (stated in official changelog)
- **Quote**: "Note: Existing agent skills within the .github/skills directory will automatically
  be available to use by Copilot code review if relevant to the review."
- **Our assessment**: Same zero-migration-cost pattern as MCP (Claim 6). Teams that have
  already authored skills for CCA or CLI agent use get code review integration automatically.
  The qualifier "if relevant to the review" implies a relevance gate — Copilot selects skills
  contextually rather than always loading all skills. For Ch02 (Harness Engineering): skill
  design for code review should consider that skills are contextually selected, not universally
  applied. A code-review-specific skill directory (`.github/skills/code-review/`) ensures
  review-specific context is prioritized; shared skills in `.github/skills/` will only activate
  when relevant.

### Claim 8: The new Medium analysis tier routes pull requests to a higher-reasoning model for deeper analysis of complex logic, security-sensitive code, and cross-service changes

- **Evidence**: Official GitHub product changelog with explicit description of Medium tier
  scope and intended use case.
- **Confidence**: settled (product fact — Medium tier is in public preview)
- **Quote**: "The new Medium tier routes pull requests to a higher-reasoning model purpose-built
  for deeper analysis of complex logic, security-sensitive code, and cross-service changes."
- **Our assessment**: This introduces model routing at the code review layer — not a single
  model for all reviews, but automatic selection of a higher-reasoning model when the admin
  has configured Medium tier for that repository. The three use cases named (complex logic,
  security-sensitive code, cross-service changes) are the exact scenarios where lighter-weight
  model analysis is most likely to miss issues. For Ch04 (Agents): this is a per-repository
  model routing pattern — admins trade cost for analysis depth at the repository granularity.
  For Ch02 (Harness Engineering): teams can align review-model selection with code criticality:
  core service repos on Medium, documentation repos on Low.

### Claim 9: Low tier remains the default for straightforward work such as docs and small repositories, prioritizing speed and cost efficiency

- **Evidence**: Official changelog's description of Low tier in contrast to Medium.
- **Confidence**: settled (stated in official changelog)
- **Quote**: "Low remains a fast, cost-efficient default for straightforward work like docs
  and small repositories."
- **Our assessment**: The Low/Medium distinction is framed as a complexity-routing decision,
  not a quality-tier choice. "Docs and small repositories" as the Low tier examples signals
  that the expected quality delta is in proportion to code complexity — a docs PR has limited
  surface area for subtle logic bugs or cross-service interactions where higher-reasoning
  models add value. For Ch05 (Team Adoption): Low tier is the appropriate starting point for
  most teams. Medium should be reserved for repositories where review depth materially affects
  merge safety.

### Claim 10: Medium tier delivers more actionable comments with fewer false positives and catches subtle bugs that lighter reviews miss

- **Evidence**: One of three bullet points describing Medium tier benefits in the changelog.
- **Confidence**: anecdotal (vendor claim — no metrics or study cited to support these
  comparisons)
- **Quote**: "Medium delivers more actionable comments with fewer false positives and catches
  subtle bugs lighter reviews miss."
- **Our assessment**: This is a vendor claim that the higher-reasoning model produces
  qualitatively better output. The specific improvements named (fewer false positives, catches
  subtle bugs) are the exact failure modes that teams using AI code review most commonly cite.
  Without a controlled study, this remains a vendor assertion. For Ch05: treat as a hypothesis
  teams should validate in their own context — enable Medium on one complex repository and
  track whether High-severity comment rate or false positive rate changes. See
  `docs-github-copilot-pr-review-metrics.md` for the measurement approach.

### Claim 11: Medium tier consumes more AI Credits than Low, with "clear cost signals" for admin management under usage-based billing

- **Evidence**: One of three bullet points describing Medium tier implications in the changelog.
- **Confidence**: settled (cost difference stated in official changelog; specific multiplier
  not provided)
- **Quote**: "Medium consumes more AI Credits than Low, with clear cost signals so admins can
  manage spend under usage-based billing."
- **Our assessment**: The exact AI Credit multiplier is not stated — the changelog confirms
  only that Medium costs more, not by how much. For Ch05 (TCO analysis): Medium tier adds a
  new cost variable to the GitHub Copilot code review TCO model (which already includes
  AI Credits and Actions minutes per `docs-github-copilot-code-review-actions-billing.md`).
  The cost model is now: tier × (AI Credits + Actions minutes). "Clear cost signals" likely
  means usage-based billing dashboards show Medium vs. Low consumption separately. Teams
  enabling Medium should check whether their Copilot spending limit accommodates the higher
  per-review credit cost at their PR volume.

### Claim 12: Agent skills for code review are set up by creating a `.github/skills/code-review/` directory containing a SKILL.md file with context and instructions

- **Evidence**: Step-by-step setup instructions in the changelog.
- **Confidence**: settled (specific path and filename stated in official changelog)
- **Quote**: "Under .github/skills, create a code-review or similarly named directory to
  ensure that Copilot code review will read and utilize the skill."
- **Our assessment**: The directory naming convention ("code-review or similarly named") is
  intentionally flexible — the naming is the signal to Copilot that this skill is relevant to
  code review, not a rigid filename match. For Ch02 (Harness Engineering): the setup path is
  `.github/skills/code-review/SKILL.md`. This is consistent with the broader `.github/skills/`
  convention documented in `docs-github-copilot-agent-skills-cli.md` (Claim 1) and
  `docs-github-copilot-eclipse-byok-skills-chat.md` (Claim 6). The SKILL.md file is described
  as containing "the relevant context and instructions you want Copilot code review to utilize"
  — no structural format is specified beyond that, giving teams flexibility in content.

### Claim 13: MCP servers are configured in repository settings under Copilot → MCP servers, with authentication tokens stored under Secrets and variables → Agents

- **Evidence**: Step-by-step setup instructions in the changelog.
- **Confidence**: settled (specific settings paths stated in official changelog)
- **Quote**: "Add your desired JSON MCP configuration under repository settings → Copilot
  → MCP servers."
- **Quote**: "Store your token required for MCP authentication under repository settings
  → Secrets and variables → Agents."
- **Our assessment**: The setup paths are operational facts. The JSON MCP configuration model
  follows the standard MCP server config pattern. Storing tokens under Secrets and variables →
  Agents (distinct from the standard Actions Secrets location) indicates a separate secrets
  namespace for agent-invoked MCP authentication — relevant for security review of token
  access scope. For Ch02: document these exact paths as the configuration surface for code
  review MCP setup.

### Claim 14: Review tier is selected per repository by navigating to repository settings → Copilot → Code review → Review effort level

- **Evidence**: Step-by-step setup instructions in the changelog.
- **Confidence**: settled (specific navigation path stated in official changelog)
- **Quote**: "Navigate to repository settings → Copilot → Code review → Review effort level."
- **Our assessment**: Per-repository tier configuration means teams can implement a tiered
  strategy: Medium for production service repos, Low for documentation, tooling, and
  experimental repos. The setting is admin-controlled per repository, not user-controlled per
  PR — the review depth is a policy decision, not a practitioner choice at review time. For
  Ch05: recommend a repository classification framework that maps code criticality to tier:
  production services → Medium; internal tools, docs, experiments → Low.

## Concrete Artifacts

### Source Changelog Text (verbatim, June 2, 2026)

```
Title: Shape Copilot code review around your team
Published: 2026-06-02
Source: https://github.blog/changelog/2026-06-02-shape-copilot-code-review-around-your-team

--- OPENING ---

Copilot code review adapts to your team's tools and standards and scales its depth to the
complexity of each change. Today we're shipping two public previews:
  - Agent skills and MCP support that bring your organization's context into every review
  - A new medium analysis tier that routes complex pull requests to a higher-reasoning model

--- SECTION: Bring your tools and standards into every review with skills and MCP ---

A lot of what reviewers need to know lives in other tools, not in the diff itself. Agent
skills and MCP bring that context into Copilot's reviews, ensuring that reviews don't stall
on questions already answered elsewhere. This means senior engineers stop being the bottleneck
for consistency across repositories.

  - Custom agent skills invoke your team's internal tools and standards during a review,
    extending Copilot beyond its built-in analysis.
  - MCP server connections, once configured, pull context directly into the review from the
    third-party platforms and internal systems your team already uses, including issue tracking,
    documentation, service catalogs, and incident tooling.
  - Configurable Actions workflows give you control over the compute and environment Copilot
    uses for review.
  - Shared configuration across review and cloud agent means platform teams invest once and
    get consistent behavior across both agents.

--- SECTION: Match review depth to complexity with the new medium analysis tier ---

Review depth should scale with the complexity of the change. The new Medium tier routes pull
requests to a higher-reasoning model purpose-built for deeper analysis of complex logic,
security-sensitive code, and cross-service changes. Low remains a fast, cost-efficient default
for straightforward work like docs and small repositories. This enables you to invest compute
where it matters most and conserve it everywhere else.

  - Admins set Low or Medium per repository to align review intensity with code complexity
    and business value.
  - Medium delivers more actionable comments with fewer false positives and catches subtle
    bugs lighter reviews miss.
  - Medium consumes more AI Credits than Low, with clear cost signals so admins can manage
    spend under usage-based billing.

--- SECTION: Getting started ---

These features are available in public preview for existing Copilot Pro, Pro+, Business, and
Enterprise users. Copilot code review can also be enabled for non-Copilot users via Direct
Org Billing.

Setting up MCP servers for Copilot code review:
  1. Add your desired JSON MCP configuration under repository settings → Copilot → MCP servers.
  2. Store your token required for MCP authentication under repository settings → Secrets and
     variables → Agents.
  Note: Any existing MCP configurations for Copilot cloud agent will now apply to Copilot
  code review automatically.
  Read the docs to find examples of common MCP configurations you can get started with.

Setting up agent skills for Copilot code review:
  1. If one does not exist within your repository, create a .github/skills directory.
  2. Under .github/skills, create a code-review or similarly named directory to ensure that
     Copilot code review will read and utilize the skill.
  3. Create a SKILL.md file containing the relevant context and instructions you want
     Copilot code review to utilize.
  Note: Existing agent skills within the .github/skills directory will automatically be
  available to use by Copilot code review if relevant to the review.
  For more information, read our docs on agent skills.

View and change your review tier:
  1. Navigate to repository settings → Copilot → Code review → Review effort level.
  2. Select your desired review depth in the dropdown.
  For more details, read our docs on medium tier reviews.
```

### Setup Reference: Agent Skills for Code Review

```
# Agent skills setup for Copilot code review

DIRECTORY STRUCTURE:
  .github/
    skills/
      code-review/          ← "code-review or similarly named directory"
        SKILL.md            ← "relevant context and instructions you want Copilot
                               code review to utilize"

NOTES:
  - Skills in .github/skills/ (any subdirectory) are auto-available to code review
    "if relevant to the review"
  - No special format required for SKILL.md content; free-form instructions
  - Compatible with skills installed via `gh skill` CLI (docs-github-copilot-agent-skills-cli)
  - Also available in Eclipse (.github/skills/<name>/SKILL.md path) per
    docs-github-copilot-eclipse-byok-skills-chat
```

### Setup Reference: MCP Servers for Code Review

```
# MCP server setup for Copilot code review

CONFIGURATION LOCATION:
  Repository settings → Copilot → MCP servers
  → Add JSON MCP server configuration here

TOKEN STORAGE:
  Repository settings → Secrets and variables → Agents
  → Store authentication tokens here (separate from Actions Secrets namespace)

MIGRATION:
  "Any existing MCP configurations for Copilot cloud agent will now apply to
   Copilot code review automatically."
  → Zero migration cost for teams already using CCA MCP

COMMON INTEGRATIONS MENTIONED:
  - Issue tracking
  - Documentation
  - Service catalogs
  - Incident tooling
```

### Setup Reference: Review Tier Selection

```
# Review tier configuration for Copilot code review

NAVIGATION:
  Repository settings → Copilot → Code review → Review effort level → dropdown

TIERS:
  LOW    → "fast, cost-efficient default for straightforward work like docs and
             small repositories"
          → Default tier; no extra setup required

  MEDIUM → "higher-reasoning model purpose-built for deeper analysis of complex
             logic, security-sensitive code, and cross-service changes"
          → Consumes more AI Credits than Low
          → "more actionable comments with fewer false positives"
          → "catches subtle bugs lighter reviews miss"

RECOMMENDED STRATEGY:
  Production services / complex logic / security-sensitive → Medium
  Documentation / small repos / experiments               → Low

ACCESS:
  Available as public preview for Copilot Pro, Pro+, Business, Enterprise
  Also enabled for non-Copilot users via Direct Org Billing
```

### Copilot Code Review Feature Evolution Arc (as of June 2026)

```
Date        Source Note                                     What Changed
----------  -----------------------------------------------  -------------------------------------
2026-04-08  docs-github-copilot-pr-review-metrics           Measurement: new API fields for
                                                            code review adoption and merge time.

2026-04-27  docs-github-copilot-code-review-actions-billing Billing: PRU → dual billing
                                                            (AI Credits + Actions minutes).
                                                            Agentic architecture on GitHub Actions.

2026-05-12  docs-github-copilot-code-review-comment-ux      Triage: severity labels (H/M/L),
                                                            comment grouping, changeset UI.

2026-05-19  docs-github-copilot-cca-apply-review-feedback   Action: "Fix with Copilot" dialog,
                                                            "Fix batch with Copilot" button.

2026-06-02  THIS NOTE (code-review-skills-mcp-tier)         Customization: agent skills + MCP
                                                            for org context injection; Low/Medium
                                                            analysis tier per repository.

Together: April 27 = billing/infrastructure; May 12 = triage surface; May 19 = action surface;
June 2 = customization and depth controls. The full arc: Copilot code review now has billing
transparency, UX triage, suggestion application controls, AND organizational context injection.
```

## Cross-References

- **Extends** `docs-github-copilot-code-review-actions-billing.md` (issue #445):
  - That source (April 27) established that Copilot code review "runs on agentic tool-calling
    architecture" on GitHub Actions (Claim 2: "That agentic architecture runs on GitHub Actions
    using GitHub-hosted runners"). This source's "Configurable Actions workflows give you control
    over the compute and environment Copilot uses for review" (Claim 4 of this note) builds
    directly on that architectural fact: the Actions workflow is not just the billing substrate,
    it is a configurable harness layer that teams can customize. Together: April 27 reveals the
    architecture (agentic on Actions); June 2 reveals the configuration surface of that
    architecture (Actions workflows are configurable).
  - That source's Claim 6 (self-hosted and larger runner support) is complemented by Claim 4
    of this note (configurable Actions workflows) — together they document that the entire
    compute layer of code review is team-configurable: runner type + workflow environment.

- **Extends** `docs-github-copilot-code-review-comment-ux.md` (issue #723):
  - That source (May 12) documented the UX triage layer — severity labels and comment grouping
    to reduce noise on large PRs. This source adds the analysis depth layer: Medium tier selects
    "more actionable comments with fewer false positives" (Claim 10). The two sources form a
    coherent quality improvement pair: May 12 reduced noise in the UX layer; June 2 reduces
    noise at the model layer by using a higher-reasoning model for complex repos. Teams that
    adopted severity labeling to manage signal-to-noise should now evaluate whether Medium tier
    reduces the noise at the source, potentially making the labeling/grouping triage less needed
    for complex repos.

- **Extends** `docs-github-copilot-cca-apply-review-feedback.md` (issue #833):
  - That source (May 19) documented the "Shared configuration" concept implicitly: the "Fix with
    Copilot" dialog lets users select the model for CCA to apply the fix. This source makes
    shared configuration explicit: "Shared configuration across review and cloud agent means
    platform teams invest once and get consistent behavior across both agents" (Claim 5). The
    shared-config pattern confirms that the skills and MCP infrastructure built for CCA applies
    to code review automatically — no separate investment needed. Teams that used the May 19
    dialog to route fixes to specific models should note that the underlying skills context
    available to CCA is now also available to the code review that generated those suggestions.

- **Corroborates** `docs-github-copilot-agent-skills-cli.md` (issue #189):
  - That source documented `gh skill` as a package manager for agent skills distributed via the
    agentskills.io specification, with `.github/skills/` as the storage path. This source
    confirms that `.github/skills/code-review/SKILL.md` is the code-review-specific skills
    path. The two sources together define the full skills lifecycle for code review: `gh skill`
    manages distribution (install, update, publish, pin); the `.github/skills/code-review/`
    path is the consumption location for code review specifically. Claim 7 of this note ("if
    relevant to the review") is consistent with `docs-github-copilot-agent-skills-cli.md`
    Claim 10's host-specific installation (`--agent` flag) — skill relevance filtering exists
    at both the install layer and the runtime layer.
  - Note from `docs-github-copilot-agent-skills-cli.md` Claim 6: skills "are not verified by
    GitHub and may contain prompt injections, hidden instructions, or malicious scripts." This
    security warning applies equally to skills used by code review. Any SKILL.md file injected
    into a code review session has the same prompt injection attack surface. For Ch03: the
    security advisory for skills applies to code review skills, not just CCA skills.

- **Corroborates** `docs-github-copilot-eclipse-byok-skills-chat.md` (issue #1034):
  - That June 2 Eclipse changelog documented the `.github/skills/<name>/SKILL.md` path as
    the standard for skills in Eclipse IDE. This source confirms the same path structure for
    code review: `.github/skills/code-review/SKILL.md`. The two sources together confirm that
    `.github/skills/` is a cross-surface standard path — skills placed here work in Eclipse
    IDE (slash command picker), CCA, and Copilot code review, providing a unified deployment
    target for team skill investments.

- **Corroborates** `docs-github-copilot-pr-review-metrics.md` (issue #91):
  - That source established the measurement primitives: `total_merged_reviewed_by_copilot` and
    `median_minutes_to_merge_copilot_reviewed`. This source's Medium tier claim that it delivers
    "more actionable comments with fewer false positives" (Claim 10) is a vendor hypothesis
    that teams can now test using those metrics. Hypothesis: repos migrated from Low to Medium
    should show (a) reduced dismissal rate of Copilot comments (if fewer false positives), and
    (b) stable or lower `median_minutes_to_merge_copilot_reviewed` (if more actionable comments
    speed review). Neither effect is guaranteed — see Claim 10's assessment.

- **Contradicts**: None found. No existing source note makes claims about code review analysis
  depth tiers or per-repository model routing that would conflict with this source's claims.
  No contradiction issue to file.

- **Novel**:
  - **MCP as a code review context source**: No prior corpus source documents MCP server
    connections feeding into Copilot code review specifically. Prior MCP sources cover CCA and
    CLI agent use. This is the first documentation of MCP enabling code review to pull context
    from issue tracking, documentation, service catalogs, and incident tooling.
  - **Per-repository analysis tier configuration (Low/Medium)**: First corpus source to document
    admin-controlled review depth selection per repository. Prior code review sources (billing,
    UX, action surface) treat the model as fixed; this source introduces explicit model-routing
    as an admin configuration.
  - **Shared configuration surface across review and CCA**: First corpus source to explicitly
    document that skills and MCP configuration is shared between code review and CCA, enabling
    a single investment to cover both agents.
  - **Code review as an agentic workflow with configurable Actions environments**: Prior sources
    established that code review runs on Actions infrastructure; this source is the first to
    document that the Actions workflow environment itself is configurable by teams.
  - **MCP token storage in Secrets and variables → Agents namespace**: First corpus source to
    document the `Secrets and variables → Agents` secrets namespace, distinct from the standard
    Actions Secrets namespace.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add "Code Review as Configurable Agentic Pipeline" section**: The June 2 changelog
  establishes that Copilot code review is not a fixed service call but a configurable agentic
  pipeline with four layers: (1) agent skills (`.github/skills/code-review/SKILL.md`) defining
  review context, (2) MCP servers (repo settings → Copilot → MCP servers) providing external
  context, (3) Actions workflow (configurable compute and environment), and (4) review tier
  (Low/Medium) determining model depth. Document these four layers as the harness configuration
  surface for code review. Reference `docs-github-copilot-code-review-actions-billing.md`
  Claim 2 for the architectural basis and this source for the configuration surface.
- **Skills deployment pattern for code review**: Add the `.github/skills/code-review/SKILL.md`
  path as the code-review-specific skills deployment target. Recommend: put org-wide review
  standards (naming conventions, security patterns, service catalog references) in
  `.github/skills/code-review/SKILL.md`; put project-specific review context in the same
  directory per repo. Cross-reference `docs-github-copilot-agent-skills-cli.md` for the
  `gh skill` distribution mechanism.
- **MCP configuration for code review**: Document the setup path (repo settings → Copilot →
  MCP servers) and secrets path (Secrets and variables → Agents). Note that existing CCA MCP
  configurations apply automatically — zero migration cost for teams already using MCP with CCA.
  Common integrations: issue tracking, documentation, service catalogs, incident tooling.

### Chapter 04: Agents

- **MCP as code review context injection pattern**: Add this as a concrete MCP integration
  use case: code review agents using MCP to pull context from issue trackers (does this PR
  address the linked issue?), service catalogs (does this change affect documented service
  contracts?), and incident tools (has this code path been involved in recent incidents?).
  This is the pattern that makes code review MCP most practically valuable.
- **Review tier as model routing**: The Low/Medium tier decision is an admin-level model
  routing pattern — administrators select which model processes which PRs based on repository
  criticality. For the guide's agent architecture discussion: model routing at the repository
  granularity is now a first-class Copilot code review configuration.

### Chapter 05: Team Adoption / Tool Evaluation

- **Updated code review adoption checklist (as of June 2026)**: Teams evaluating Copilot
  code review should now assess all five layers of the feature: (1) billing model (AI Credits +
  Actions minutes since June 1, per `docs-github-copilot-code-review-actions-billing.md`),
  (2) triage UX (severity labels + grouping, per `docs-github-copilot-code-review-comment-ux.md`),
  (3) suggestion application (Fix with Copilot dialog, per
  `docs-github-copilot-cca-apply-review-feedback.md`), (4) organizational context injection
  (skills + MCP, this source), and (5) analysis depth (Low/Medium tier, this source). Teams
  that evaluated before June 2, 2026 are missing layers 4 and 5 entirely.
- **Review tier strategy by repository type**: Document a recommended tiering framework:
  - Production services, security-sensitive code, shared libraries → Medium tier
  - Documentation, tooling, experimental, small repositories → Low tier
  This aligns review depth with code criticality without uniform cost increase. Note that
  Medium costs more AI Credits — calculate expected cost delta before enabling fleet-wide.
- **MCP as adoption accelerator for teams with rich internal tooling**: For teams with mature
  service catalogs, incident tooling, and internal documentation, MCP integration is the highest-
  leverage Copilot code review investment — it encodes institutional knowledge that would otherwise
  require senior reviewers. Teams without these systems should focus on agent skills (SKILL.md)
  as the lower-infrastructure starting point.

### Chapter 01: Daily Workflows

- **Code review configuration is admin-controlled, not practitioner-controlled**: The review
  tier (Low/Medium), MCP servers, and agent skills are all configured by repository admins, not
  individual practitioners. Practitioners benefit from these configurations automatically. For
  Ch01: the practitioner-level workflow change is that code review comments may now reflect
  context from external systems (MCP) and team standards (agent skills) without the practitioner
  having explicitly provided that context. Reviews are richer but the practitioner interaction
  model (review comments → triage by severity → apply or dismiss) is unchanged.

## Extraction Notes

1. **Source is ~400 words**: This is a medium-length product changelog with four distinct
   sections. All substantive content was exhausted in fourteen claims above. The page was
   fetched via curl and HTML-parsed for verbatim text; the Concrete Artifacts section above
   preserves the verbatim source text for Assayer verification. All quoted passages were
   verified against the curl-extracted verbatim text.

2. **AI Credit multiplier for Medium tier not quantified**: The changelog confirms Medium costs
   more than Low but does not provide a ratio. Teams calculating TCO for Medium tier adoption
   cannot compute expected cost increase from this source alone. A separate benchmarking step
   is required after enabling Medium.

3. **Higher-reasoning model identity not stated**: The changelog describes Medium as "a higher-
   reasoning model purpose-built for deeper analysis" without naming the model. Whether this is
   Claude claude-sonnet-4-6, Claude Opus 4.8, or another model is not disclosed.

4. **SKILL.md content format not specified**: The changelog says SKILL.md should contain "relevant
   context and instructions" without specifying a format. The `docs-github-copilot-agent-skills-cli`
   note covers SKILL.md format for general skills but not code-review-specific structure. A
   separate documentation source may elaborate on what content most effectively guides code review.

5. **No sub-pages followed beyond the changelog**: The changelog references documentation pages
   ("Read the docs to find examples of common MCP configurations," "read our docs on agent
   skills," "read our docs on medium tier reviews"). These linked docs pages were not fetched.
   They likely contain more specific configuration examples that would warrant a separate source
   note if substantive.

6. **No contradictions to file**: All claims in this source either extend or corroborate
   existing corpus notes. No existing source makes claims that this source would refute. No
   contradiction issue required.
