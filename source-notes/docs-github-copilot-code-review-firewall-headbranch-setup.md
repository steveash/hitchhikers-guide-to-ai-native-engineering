---
source_url: https://github.blog/changelog/2026-07-17-copilot-code-review-customization-and-configurability-improvements
source_type: docs
title: "Copilot code review: Customization and configurability improvements"
author: GitHub (official changelog)
date_published: 2026-07-17
date_extracted: 2026-07-18
last_checked: 2026-07-18
status: current
confidence_overall: settled
issue: "#1988"
---

# Copilot Code Review: Customization and Configurability Improvements

> GitHub's July 17, 2026 changelog announcing four Copilot code review changes: custom
> instructions (including `AGENTS.md`, `copilot-instructions.md`, `*.instructions.md`,
> and agent skills) are now read from the pull request's head branch instead of the base
> branch; three new instruction file types (`REVIEW.md`, `GEMINI.md`, `CLAUDE.md`) are now
> recognized; a dedicated `copilot-code-review.yml` workflow file allows repository-level
> environment setup independent of Copilot cloud agent; and code review now runs behind a
> default, separately-configurable firewall with the org-level runner configuration split
> into two independent sections for review vs. cloud agent — extending the configuration
> surface documented across the June 2, June 12, and June 18, 2026 changelogs.

## Source Context

- **Type**: docs (GitHub official product changelog, July 17, 2026; ~500 words across an
  overview paragraph and four numbered/emoji-headed sections, retrieved via `curl` and
  parsed from the raw article HTML — not through a WebFetch small-model summary)
- **Author credibility**: GitHub engineering team announcing production features on the
  official changelog. Authoritative for the existence of these features, the exact file
  names and paths involved, the navigation paths for configuration, and stated availability
  caveats (e.g., self-hosted runners not supporting the firewall). Not authoritative for:
  how head-branch instruction reading interacts with content exclusion rules from
  `docs-github-copilot-code-review-config-controls.md`; the relative precedence when both
  `copilot-code-review.yml` and `copilot-setup-steps.yml` exist alongside a base-branch
  `copilot-instructions.md`; or whether firewall-restricted network access causes review
  failures/timeouts for repositories whose review depends on reachable external services
  (e.g., MCP servers documented in `docs-github-copilot-code-review-skills-mcp-tier.md`).
- **Scope**: Four features: (1) custom instructions now read from the head branch, (2)
  three new recognized instruction file types (`REVIEW.md`, `GEMINI.md`, `CLAUDE.md`), (3)
  `copilot-code-review.yml` custom setup steps with fallback to `copilot-setup-steps.yml`,
  (4) default firewall for code review (configurable separately from Copilot cloud agent,
  unsupported on self-hosted runners) and a split of the previously-shared organization
  runner configuration into two independent sections. Does NOT cover: quantified security
  benefit of the firewall, what specific domains/hosts the firewall allows or blocks by
  default, whether `REVIEW.md`/`GEMINI.md`/`CLAUDE.md` are merged or take precedence over
  each other when multiple exist in the same repository, or migration guidance for
  organizations that already rely on the shared runner configuration being split.

## Extracted Claims

### Claim 1: Custom instructions — including `copilot-instructions.md`, `*.instructions.md`, agent skills, and `AGENTS.md` — are now read from the pull request's head branch instead of the base branch, enabling teams to iterate on and test instructions in a feature branch before merging

- **Evidence**: Official GitHub changelog, dedicated subsection "📝 Custom instructions now
  read from the head branch."
- **Confidence**: settled (product behavior change stated in official changelog)
- **Quote**: "Custom instructions are now read from the head branch of the pull request
  instead of the base branch. This includes copilot-instructions.md, *.instructions.md,
  agent skills, and AGENTS.md. This means you can iterate on and test custom instructions
  in a feature branch without needing to merge them first."
- **Our assessment**: This is a meaningful workflow change, not just a customization
  surface addition. Previously, any change to `copilot-instructions.md` or `AGENTS.md` had
  to be merged to the base branch before Copilot code review would use the updated version
  — meaning a team could not verify "does this new instruction actually change review
  behavior?" without a merge-then-observe cycle, or a second throwaway PR. Reading from the
  head branch turns instruction files into something a team can develop and validate in
  the same PR that introduces them. This directly extends
  `docs-github-copilot-code-review-agents-md-ui.md` (Claim 2: AGENTS.md is read
  "automatically as part of its workflow") — that note did not specify which branch AGENTS.md
  is read from; this source clarifies it is now the head branch for all four instruction
  mechanisms (instructions, `*.instructions.md`, skills, AGENTS.md). For Ch02 (Harness
  Engineering): document a validation workflow — propose instruction-file changes in a
  draft PR, request a Copilot code review on that same PR, and observe whether the new
  instructions changed review output, before merging.

### Claim 2: Copilot code review now reads `REVIEW.md`, `GEMINI.md`, and `CLAUDE.md` files from the repository and automatically incorporates any review guidelines or model-specific instructions already maintained there

- **Evidence**: Official changelog, subsection "📄 Expanded custom instructions file
  support."
- **Confidence**: settled (product behavior stated in official changelog)
- **Quote**: "Copilot code review now reads REVIEW.md, GEMINI.md, and CLAUDE.md files from
  your repository, so your customizations are understood regardless of where they live. If
  your team already maintains review guidelines or model-specific instructions in these
  files, Copilot code review will automatically pick them up and incorporate them into its
  review process."
- **Our assessment**: This is the most significant cross-agent-portability claim in this
  source, and it goes beyond the AGENTS.md-only support documented in
  `docs-github-copilot-code-review-agents-md-ui.md`. Copilot code review reading `CLAUDE.md`
  directly means a team's Claude Code project instructions — written for an entirely
  different vendor's coding agent — now also shape GitHub's own review agent, with zero
  additional authoring effort. This corroborates and extends the "investment multiplier"
  framing from `docs-github-copilot-code-review-agents-md-ui.md` Guide Impact ("a single
  AGENTS.md file can shape both Claude Code and Copilot code review"): as of this source,
  a `CLAUDE.md` alone accomplishes the same multiplier without an AGENTS.md at all. `REVIEW.md`
  is new to our corpus as a concept — no prior source documents a `REVIEW.md` convention for
  any tool, so this changelog is effectively defining a Copilot-specific review-guidelines
  filename. `GEMINI.md` is Google Gemini's project-instructions convention; its inclusion here
  means three distinct vendor ecosystems' context files (Anthropic's CLAUDE.md, Google's
  GEMINI.md, and GitHub's own REVIEW.md) are all now first-class inputs to Copilot's review
  agent. For Ch02: the instruction-file surface for Copilot code review is not one file but
  a family: `AGENTS.md`, `copilot-instructions.md`, `*.instructions.md`, `REVIEW.md`,
  `GEMINI.md`, `CLAUDE.md` — six file names to check for and consolidate before enabling
  review fleet-wide, to avoid duplicated or conflicting guidance across files nobody
  remembers exist.

### Claim 3: Teams can now configure the environment available to Copilot code review at runtime using a `copilot-code-review.yml` file in `.github/workflows/`, to install dependencies, configure repository-level runners, or run other preparation steps independently of Copilot cloud agent

- **Evidence**: Official changelog, section "🔧 Custom setup steps," opening paragraph.
- **Confidence**: settled (product feature stated in official changelog)
- **Quote**: "You can now configure the environment available to Copilot code review during
  runtime using a copilot-code-review.yml file in your .github/workflows/ directory. This
  lets you install dependencies, configure runners on the repository level independently of
  Copilot cloud agent, set up tooling, or run any preparation steps that Copilot code review
  needs to produce the reviews you desire for your repository."
- **Our assessment**: This is the first corpus source to document a dedicated,
  review-specific setup-steps file. It extends Claim 4 of
  `docs-github-copilot-code-review-skills-mcp-tier.md` ("Configurable Actions workflows give
  you control over the compute and environment Copilot uses for review") by naming the exact
  mechanism: a `copilot-code-review.yml` file, distinct from whatever workflow file
  configures Copilot cloud agent. The explicit framing "independently of Copilot cloud agent"
  matters because it is the opposite pattern from the shared-configuration principle in
  `docs-github-copilot-code-review-skills-mcp-tier.md` Claim 5 ("shared configuration across
  review and cloud agent means platform teams invest once") — skills and MCP configuration
  are shared between the two agents, but setup-step environment configuration is now
  intentionally separable. Teams whose CI dependencies differ between "what code review needs
  to lint/build a diff" and "what the cloud agent needs to make a full commit" can now
  configure each independently. For Ch02: document `copilot-code-review.yml` as the
  environment-preparation layer, distinct from the agent-context layer (instruction files,
  skills, MCP) and the governance layer (content exclusion, runner lock).

### Claim 4: If no `copilot-code-review.yml` file exists, Copilot code review falls back to the repository's existing `copilot-setup-steps.yml` file, if one is present

- **Evidence**: Official changelog, bulleted fallback behavior under "🔧 Custom setup
  steps."
- **Confidence**: settled (fallback behavior stated in official changelog)
- **Quote**: "If no copilot-code-review.yml file exists, Copilot code review will fall back
  to your existing copilot-setup-steps.yml file if one is present."
- **Our assessment**: This is a zero-migration-cost design, matching the pattern already
  documented for skills and MCP in `docs-github-copilot-code-review-skills-mcp-tier.md`
  (Claims 6-7: existing CCA MCP configurations and `.github/skills` skills automatically
  apply to code review with no migration). Teams that already maintain a
  `copilot-setup-steps.yml` for Copilot cloud agent get equivalent environment setup applied
  to code review automatically, with no new file required, until they choose to diverge by
  adding a dedicated `copilot-code-review.yml`. For Ch05 (Team Adoption): this lowers the
  adoption bar for the new setup-steps feature to zero for teams already using
  `copilot-setup-steps.yml` — no action is required unless the team wants review-specific
  environment behavior that differs from the cloud agent's.

### Claim 5: Copilot code review now runs behind a firewall by default, restricting network access during a review; the firewall is configurable separately from Copilot cloud agent in repository and organization settings

- **Evidence**: Official changelog, section "🛡️ Firewall support," opening paragraph.
- **Confidence**: settled (product feature and default-on status stated in official
  changelog)
- **Quote**: "Copilot code review now runs behind a firewall by default, restricting network
  access during a review. The firewall is configurable separately from Copilot cloud agent
  in repository and organization settings, giving you independent control over each agent's
  network access."
- **Our assessment**: This is the first corpus source to document network-access
  restriction as a default, security-relevant property of Copilot code review specifically.
  It is a governance control in the same family as content exclusion (repo/org/enterprise
  path-based access restriction, documented in
  `docs-github-copilot-code-review-config-controls.md` Claim 4) but addresses a different
  attack surface: content exclusion restricts what files the agent can read; the firewall
  restricts what network destinations the agent's runner can reach during execution. Together
  they narrow both the read surface and the exfiltration/egress surface of the review agent.
  The "independent control over each agent's network access" framing matches the
  independently-configurable pattern from Claim 3 (setup steps) and Claim 6 below (runner
  split) — as of this changelog, code review and cloud agent are being deliberately decoupled
  across three configuration dimensions (environment setup, network access, runner type) even
  though skills/MCP context remains shared per
  `docs-github-copilot-code-review-skills-mcp-tier.md` Claim 5. For Ch03 (if the guide
  addresses agent security) and Ch02: document the firewall as a default-on network
  containment control for the review agent, and flag that it is a separate toggle from
  Copilot cloud agent's own network restrictions — auditing one does not confirm the state
  of the other.

### Claim 6: The firewall is enabled by default for all repositories and is configured via repository settings → Copilot → Internet access; self-hosted runners do not currently support the firewall, so reviews on self-hosted runners continue running without it

- **Evidence**: Official changelog, two bullet points and a warning callout under "🛡️
  Firewall support."
- **Confidence**: settled (default status, navigation path, and self-hosted exception all
  stated in official changelog)
- **Quote**: "The firewall is enabled by default for all repositories." / "To configure this
  setting in your repository, navigate to your repository settings, then go to Copilot →
  Internet access." / "Self-hosted runners do not currently support the firewall. If you
  have self-hosted runners configured for Copilot code review, your reviews will continue to
  run as usual without the firewall."
- **Our assessment**: The self-hosted runner exception is the operationally important detail
  here, and it directly qualifies the runner-choice guidance from
  `docs-github-copilot-code-review-actions-billing.md` (Claim 6 and its Concrete Artifacts
  "Runner Configuration Options for Code Review": self-hosted runners were framed purely as a
  cost-optimization lever — "teams with existing runner infrastructure seeking cost
  optimization"). As of this source, choosing self-hosted runners for cost reasons also means
  opting out of the default firewall protection, silently, with no equivalent control
  surfaced for self-hosted environments. A team that migrated Copilot code review to
  self-hosted runners purely for billing reasons (per the April 27 changelog) may not realize
  it also forfeited the July 17 firewall default unless it reads this changelog specifically.
  For Ch02 and Ch05: add this as an explicit trade-off in the runner-selection decision —
  self-hosted runners now cost teams a security control (firewall) that GitHub-hosted runners
  get automatically, and this should be weighed against the billing-rate benefits documented
  in `docs-github-copilot-code-review-actions-billing.md`.

### Claim 7: Copilot code review and Copilot cloud agent previously shared a single organization-level runner configuration; that configuration is now split into two independent sections on the organization's "Runner type" settings page, letting admins choose different runner types for each agent

- **Evidence**: Official changelog, section "⚙️ Organization runner configuration updates
  for Copilot code review," full paragraph.
- **Confidence**: settled (configuration-surface change stated in official changelog)
- **Quote**: "Copilot code review and Copilot cloud agent previously shared a single runner
  configuration at the organization level. That configuration is now split into two separate
  sections on the Runner type settings page in your organization settings, allowing you to
  independently choose different runner types for each agent."
- **Our assessment**: This directly extends and refines Claims 1-3 of
  `docs-github-copilot-code-review-config-controls.md` (June 12), which documented that
  "organization admins can now set a default runner for Copilot code review at the
  organizational level" with lock enforcement, at navigation path "organization settings →
  Copilot → Runner type → Runner type configuration." That June 12 note did not state — and
  had no way to know — that this org-level runner setting was shared with Copilot cloud
  agent; this July 17 source retroactively clarifies that the June 12 feature was, until this
  release, a *shared* runner configuration across both agents, and is only now split into
  independent per-agent sections. This is not a contradiction (the June 12 claims about the
  navigation path and lock behavior remain accurate) but a refinement the Assayer/Smith should
  fold into the June 12 note's understanding: readers should not assume "org runner default"
  meant "review-specific runner default" before July 17, 2026. For Ch02: update the seven/
  eight-layer configuration surface tables in `docs-github-copilot-code-review-config-controls.md`
  and `docs-github-copilot-code-review-agents-md-ui.md` to note that the org-level runner
  layer is, as of July 17, 2026, agent-specific rather than shared.

### Claim 8: To update the (now-independent) organization runner configuration for Copilot code review, admins navigate to organization settings → Copilot → Runner type

- **Evidence**: Official changelog, closing sentence of the "⚙️ Organization runner
  configuration updates" section.
- **Confidence**: settled (navigation path stated in official changelog)
- **Quote**: "To update your configuration, navigate to your organization settings, then go
  to Copilot → Runner type."
- **Our assessment**: This is the same top-level navigation path documented in
  `docs-github-copilot-code-review-config-controls.md` Claim 3 ("organization settings →
  Copilot → Runner type → Runner type configuration"), confirming the page itself did not
  move — only its internal layout changed to show two sections instead of one shared control.
  For Ch02: no path change needed in existing guide navigation instructions; only the
  in-page expectation changes (admins will now see and must choose between two runner-type
  selectors instead of one).

## Concrete Artifacts

### Source Changelog Text (verbatim, July 17, 2026, retrieved via curl + HTML parse)

```
Title: Copilot code review: Customization and configurability improvements
Published: July 17, 2026
Source: https://github.blog/changelog/2026-07-17-copilot-code-review-customization-and-configurability-improvements
Category: Improvement

--- OPENING ---

Copilot code review now utilizes a firewall, custom setup steps, and independent runner
configurations. It now reads custom instructions from the head branch to allow for easy
testing and validation of custom instructions. These changes give administrators and
developers more control over how Copilot code review runs in their environment.

--- SECTION: Expanding custom instructions, now easier to validate ---

📝 Custom instructions now read from the head branch

Custom instructions are now read from the head branch of the pull request instead of the
base branch. This includes copilot-instructions.md, *.instructions.md, agent skills, and
AGENTS.md. This means you can iterate on and test custom instructions in a feature branch
without needing to merge them first.

📄 Expanded custom instructions file support

Copilot code review now reads REVIEW.md, GEMINI.md, and CLAUDE.md files from your
repository, so your customizations are understood regardless of where they live. If your
team already maintains review guidelines or model-specific instructions in these files,
Copilot code review will automatically pick them up and incorporate them into its review
process.

--- SECTION: 🔧 Custom setup steps ---

You can now configure the environment available to Copilot code review during runtime
using a copilot-code-review.yml file in your .github/workflows/ directory. This lets you
install dependencies, configure runners on the repository level independently of Copilot
cloud agent, set up tooling, or run any preparation steps that Copilot code review needs to
produce the reviews you desire for your repository.

  - Add a copilot-code-review.yml file to your repository to define setup steps specific to
    Copilot code review.
  - If no copilot-code-review.yml file exists, Copilot code review will fall back to your
    existing copilot-setup-steps.yml file if one is present.

To learn more about how to set up a copilot-code-review.yml file, see our documentation on
setting the Copilot code review environment.
[link: https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review#customizing-copilot-code-reviews-environment]

--- SECTION: 🛡️ Firewall support ---

Copilot code review now runs behind a firewall by default, restricting network access
during a review. The firewall is configurable separately from Copilot cloud agent in
repository and organization settings, giving you independent control over each agent's
network access.

  - The firewall is enabled by default for all repositories.
  - To configure this setting in your repository, navigate to your repository settings,
    then go to Copilot → Internet access.

    ⚠️ Self-hosted runners do not currently support the firewall. If you have self-hosted
    runners configured for Copilot code review, your reviews will continue to run as usual
    without the firewall.

--- SECTION: ⚙️ Organization runner configuration updates for Copilot code review ---

Copilot code review and Copilot cloud agent previously shared a single runner
configuration at the organization level. That configuration is now split into two separate
sections on the Runner type settings page in your organization settings, allowing you to
independently choose different runner types for each agent.

To update your configuration, navigate to your organization settings, then go to Copilot →
Runner type.
```

### Instruction File Family for Copilot Code Review (as of July 17, 2026)

```
# All file types Copilot code review now reads, and which branch each is read from

Branch read from: HEAD branch of the pull request (as of July 17, 2026 — was base branch)

  copilot-instructions.md   → Copilot-specific general instructions (unlimited length,
                               per docs-github-copilot-code-review-config-controls.md)
  *.instructions.md         → additional Copilot-specific instructions (unlimited length)
  agent skills              → .github/skills/**/SKILL.md (agentic tool invocations,
                               per docs-github-copilot-code-review-skills-mcp-tier.md)
  AGENTS.md                 → cross-agent project conventions (GA since June 18, 2026,
                               per docs-github-copilot-code-review-agents-md-ui.md)
  REVIEW.md                 → Copilot code-review-specific guidelines (NEW, July 17, 2026 —
                               first corpus documentation of this filename for any tool)
  GEMINI.md                 → Google Gemini project conventions (NEW as a Copilot code
                               review input, July 17, 2026)
  CLAUDE.md                 → Claude Code project conventions (NEW as a Copilot code
                               review input, July 17, 2026)
```

### Environment Setup Files for Copilot Code Review vs. Cloud Agent

```
copilot-code-review.yml    → .github/workflows/ — review-specific environment setup
                              (dependencies, runners, tooling); NEW, July 17, 2026
copilot-setup-steps.yml    → fallback used by review if copilot-code-review.yml absent;
                              this is the pre-existing Copilot cloud agent setup file
```

### Copilot Code Review Feature Evolution Arc (updated to July 17, 2026)

```
Date        Source Note                                          What Changed
----------  ---------------------------------------------------  ------------------------------------
2026-04-08  docs-github-copilot-pr-review-metrics               Measurement: code review API fields
2026-04-27  docs-github-copilot-code-review-actions-billing     Billing: AI Credits + Actions mins
2026-05-12  docs-github-copilot-code-review-comment-ux          UX: severity labels + grouping
2026-05-19  docs-github-copilot-cca-apply-review-feedback       Action: Fix with Copilot dialog
2026-06-02  docs-github-copilot-code-review-skills-mcp-tier     Customization: skills + MCP + tier
2026-06-12  docs-github-copilot-code-review-config-controls     Governance: org runner defaults +
                                                                 content exclusion + unlimited
                                                                 instruction files
2026-06-18  docs-github-copilot-code-review-agents-md-ui        Cross-agent: AGENTS.md support GA;
                                                                 draft PR button; timeline collapse
2026-07-17  THIS NOTE (code-review-firewall-headbranch-setup)   Validation + security: head-branch
                                                                 instructions; REVIEW.md/GEMINI.md/
                                                                 CLAUDE.md support; copilot-code-review.yml
                                                                 setup steps; default firewall; runner
                                                                 config split from cloud agent
```

## Cross-References

- **Extends** `docs-github-copilot-code-review-config-controls.md` (issue #1168):
  - Claims 1-3 of that note (org-level runner default with lock, navigation path
    "organization settings → Copilot → Runner type → Runner type configuration") are
    retroactively refined by Claim 7 of this note: the org runner configuration those claims
    describe was, until July 17, 2026, *shared* between Copilot code review and Copilot cloud
    agent — a fact the June 12 note could not have known and did not state. This is not a
    contradiction (the navigation path and lock mechanics remain accurate) but the Smith
    should note the "shared until split" history when synthesizing the runner-configuration
    section of the guide, so readers don't assume review-specific runner control existed
    before July 17.
  - Claim 6 ("the June 12 governance improvements are additive... completing a seven-layer
    configuration surface") is extended again: this source adds a ninth-plus layer
    (environment setup via `copilot-code-review.yml`, network firewall) on top of the eight
    layers already tracked through June 18. The configuration surface is no longer static
    enough to enumerate as a fixed N; the Smith should consider framing it as categories
    (agent context, content governance, compute configuration, analysis depth, network
    governance, environment setup) rather than a numbered layer count that requires revision
    with each changelog.

- **Extends** `docs-github-copilot-code-review-agents-md-ui.md` (issue #1236):
  - Claim 1 of that note ("AGENTS.md is now the eighth configuration surface... adding to the
    seven-layer surface") is extended by Claim 2 of this note: three more file types
    (`REVIEW.md`, `GEMINI.md`, `CLAUDE.md`) join AGENTS.md as automatically-read,
    repository-root-level context files. That note's Guide Impact framed AGENTS.md as a
    "zero-friction Copilot code review activation path" for teams with an existing AGENTS.md;
    this source extends that same zero-friction principle to teams whose only existing context
    file is a `CLAUDE.md` (no AGENTS.md required at all).
  - Claim 2 of that note ("Copilot code review reads AGENTS.md automatically... no manual
    configuration or invocation required") did not specify branch semantics. Claim 1 of this
    note fills that gap: AGENTS.md (along with the other three instruction mechanisms) is now
    read from the head branch, not the base branch — an update the Smith should merge into
    that note's understanding of "automatic" behavior.

- **Extends** `docs-github-copilot-code-review-skills-mcp-tier.md` (issue #1052):
  - Claim 4 ("Configurable Actions workflows give you control over the compute and
    environment Copilot uses for review") is made concrete by Claim 3 of this note: the
    specific mechanism is a `copilot-code-review.yml` file in `.github/workflows/`, separable
    from Copilot cloud agent's `copilot-setup-steps.yml`.
  - Claim 5 ("Shared configuration across review and cloud agent means platform teams invest
    once and get consistent behavior across both agents") is now only true for skills and MCP.
    As of this source, three other configuration dimensions — environment setup steps (Claim
    3), network firewall (Claim 5), and runner type (Claim 7) — are explicitly *not* shared
    and must be configured per-agent. The Smith should note this split: shared vs.
    independent configuration is now feature-specific, not a blanket policy across the two
    agents.

- **Extends** `docs-github-copilot-code-review-actions-billing.md` (issue #445):
  - Claim 6 of that note and its "Runner Configuration Options for Code Review" artifact
    framed self-hosted runners purely as a cost-optimization lever. Claim 6 of this note adds
    a security trade-off that note did not and could not anticipate: self-hosted runners do
    not support the new default firewall, so teams choosing self-hosted runners for billing
    reasons also forfeit network egress restriction during reviews. For Ch05 TCO/adoption
    guidance: this is now a two-sided trade-off (cost vs. security control), not a
    cost-only decision.

- **Corroborates** `docs-github-copilot-code-review-comment-ux.md` (issue #723) and
  `docs-github-copilot-code-review-agents-md-ui.md` (issue #1236) noise-reduction framing
  only indirectly — this source does not address comment volume or timeline UX, so no direct
  extension there.

- **Contradicts**: None found. All four features in this source extend or refine prior
  corpus claims about Copilot code review configuration; none deny or reverse a previously
  stated fact. The runner-configuration "split" (Claim 7) clarifies rather than contradicts
  the June 12 note — see the Extends entry above for why this is a refinement, not a
  contradiction. No contradiction issue filed.

- **Novel**:
  - **Head-branch instruction reading**: First corpus source documenting that any AI coding
    or review tool reads its steering-context files from a PR's head branch rather than base
    branch, enabling same-PR validation of instruction changes.
  - **`REVIEW.md` as a review-guidelines filename**: First corpus documentation of this
    filename for any tool or vendor.
  - **Cross-vendor context file consumption (`GEMINI.md`, `CLAUDE.md`) by a competitor's
    product**: First corpus source documenting that GitHub Copilot code review directly reads
    Anthropic's (`CLAUDE.md`) and Google's (`GEMINI.md`) project-instruction file conventions,
    not just the vendor-neutral `AGENTS.md` standard.
  - **`copilot-code-review.yml` environment setup file with fallback to `copilot-setup-steps.yml`**:
    First corpus documentation of a review-specific environment setup mechanism, and of the
    fallback relationship between it and the cloud agent's setup file.
  - **Default-on network firewall for a GitHub Copilot code review agent**: First corpus
    source documenting network egress restriction as a default security control for Copilot
    code review specifically (distinct from content exclusion, which restricts file access,
    not network access).
  - **Per-agent independent runner configuration (split from a previously shared org-level
    setting)**: First corpus source revealing that the org-level runner configuration
    documented on June 12 was a *shared* setting between Copilot code review and Copilot
    cloud agent until this July 17 release.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add head-branch validation as the recommended instruction-authoring workflow**: When
  proposing changes to `copilot-instructions.md`, `AGENTS.md`, `*.instructions.md`, or agent
  skills for a repository using Copilot code review, propose the change in a PR, request a
  Copilot code review on that same PR, and observe whether review output changed — before
  merging. This is only possible because of head-branch reading (Claim 1); document it as a
  concrete pattern, not just a feature mention.
- **Document the six-file instruction family and the two-file setup family**: Update the
  configuration-surface reference to list all instruction-context files Copilot code review
  now reads (`copilot-instructions.md`, `*.instructions.md`, agent skills, `AGENTS.md`,
  `REVIEW.md`, `GEMINI.md`, `CLAUDE.md` — Claims 1-2) and the environment setup files
  (`copilot-code-review.yml` with fallback to `copilot-setup-steps.yml` — Claims 3-4). Warn
  that teams with multiple of these files risk duplicated or conflicting guidance across
  files whose precedence is not documented by GitHub (see Extraction Notes).
- **Update the (currently numbered) configuration-surface tables in
  `docs-github-copilot-code-review-config-controls.md` and `docs-github-copilot-code-review-agents-md-ui.md`**:
  Both used a fixed layer count (seven, then eight) that this source's four new features
  already outdate. Recommend the Smith replace layer counting with categorized documentation
  (agent context / content governance / network governance / compute configuration / analysis
  depth / environment setup) that can absorb new features without a recount each changelog.
- **Firewall as a default security control worth auditing**: Recommend platform teams verify
  the firewall's default-on status (repository settings → Copilot → Internet access) rather
  than assume it, especially for repositories that migrated to self-hosted runners for cost
  reasons before July 17, 2026 — those repositories do not get the firewall at all (Claim 6).

### Chapter 05: Team Adoption

- **Updated code review deployment checklist (as of July 17, 2026)**: Add an eighth layer
  to the checklist tracked across `docs-github-copilot-code-review-config-controls.md` and
  `docs-github-copilot-code-review-agents-md-ui.md`: (8) validation and security controls —
  head-branch instruction testing, expanded instruction file support, review-specific
  environment setup, default network firewall, and independent (no longer shared) runner
  configuration. Teams that evaluated before July 17, 2026 are missing this layer entirely,
  and specifically do not know whether their self-hosted runner choice forfeits the firewall.
- **Self-hosted runner decision now has a security cost, not just a billing benefit**: Update
  any runner-selection guidance derived from `docs-github-copilot-code-review-actions-billing.md`
  to include the firewall trade-off from Claim 6 of this note: self-hosted runners do not
  support the default firewall as of July 17, 2026.
- **Cross-vendor context file consumption lowers the Copilot code review adoption bar
  further**: Teams already standardized on `CLAUDE.md` (Claude Code users) or `GEMINI.md`
  (Gemini users) with no `AGENTS.md` and no GitHub-specific instruction file get Copilot code
  review customization for free, per Claim 2. Add this as an adoption-checklist item: "check
  for an existing CLAUDE.md or GEMINI.md before assuming Copilot code review needs new
  instruction authoring."

## Extraction Notes

1. **Retrieved via curl + Python HTML parsing, not WebFetch's small-model summarization**:
   An initial WebFetch pass returned a paraphrased five-bullet summary that read plausibly
   but was not verified as verbatim (headings and phrasing did not match a direct source
   fetch). Per MINER.md §2a, all quotes in this note were instead sourced from a direct
   `curl` fetch of the article HTML, isolated to the `<article>` element, and converted from
   HTML to text programmatically — not reconstructed by an LLM. Every `Quote` field above is
   a character-for-character fragment from that extraction, cross-checked against the full
   verbatim reproduction preserved in Concrete Artifacts.
2. **No sub-pages followed**: The changelog links to one documentation page — "our
   documentation on setting the Copilot code review environment"
   (`https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review#customizing-copilot-code-reviews-environment`)
   — which was not fetched. That page likely contains the full `copilot-code-review.yml`
   schema and syntax examples; a follow-up source note on that documentation page would be
   warranted if the guide needs concrete YAML syntax rather than just the existence and
   fallback behavior of the file.
3. **Precedence between instruction files not documented by the source**: Neither this
   changelog nor prior corpus notes state what happens when a repository has both, e.g., a
   `CLAUDE.md` and a `copilot-instructions.md` with conflicting guidance, or both `REVIEW.md`
   and `AGENTS.md`. This is an open question for a future source or documentation follow-up,
   flagged identically in `docs-github-copilot-code-review-agents-md-ui.md` Extraction Note 4
   for the AGENTS.md/instructions/SKILL.md interaction.
4. **Firewall default allow/deny list not documented**: The source states the firewall
   "restrict[s] network access during a review" but does not enumerate which destinations are
   allowed by default (e.g., github.com, npm/PyPI registries) versus blocked. This detail
   would matter for any team whose review process depends on reaching an internal service or
   MCP server (per `docs-github-copilot-code-review-skills-mcp-tier.md`) and is not available
   from this source.
5. **No contradictions to file**: All claims in this source extend or refine existing corpus
   notes (see Cross-References). The runner-configuration split (Claim 7) is a refinement of
   the June 12 note's scope, not a reversal of any stated fact — no contradiction issue
   required.
