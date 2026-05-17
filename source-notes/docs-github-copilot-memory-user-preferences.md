---
source_url: https://github.blog/changelog/2026-05-15-copilot-memory-supports-user-preferences-for-pro-pro-users
source_type: docs
title: "Copilot Memory supports user preferences for Pro, Pro+ users"
author: GitHub (official changelog)
date_published: 2026-05-15
date_extracted: 2026-05-17
last_checked: 2026-05-17
status: current
confidence_overall: emerging
issue: "#786"
---

# Copilot Memory Supports User Preferences for Pro, Pro+ Users

> GitHub's May 15, 2026 changelog expanding Copilot Memory from repository-level
> to user-level scope: stated and inferred preferences now persist across all
> repositories and Copilot agents for individual Pro and Pro+ subscribers in early
> access — the first commercial AI coding tool in the corpus to document user-level
> preference inference and cross-session, cross-repository personalization.

## Source Context

- **Type**: docs (GitHub official product changelog, May 15, 2026; approximately
  300–400 words; early-access feature announcement)
- **Author credibility**: GitHub engineering team announcing a production feature
  expansion. Authoritative for the fact that this capability exists, which plan
  tiers have access, and what preference categories are supported. Not a credible
  source for the underlying preference-inference mechanism, how Copilot determines
  what to store vs. discard, whether preferences affect model output measurably, or
  performance implications of user preference retrieval. No empirical data on
  preference accuracy or user-reported improvement.
- **Scope**: Extension of the existing Copilot Memory feature (previously
  repository-scoped) to the user scope for Copilot Pro and Pro+ individual
  subscribers in early access. Covers: what kinds of preferences are stored,
  the stated-vs-inferred distinction, cross-repository persistence, isolation
  between users, management interface, and future expansion plans. Does NOT cover:
  Business or Enterprise plan availability, the prior repository-level Copilot
  Memory feature, how user-level memory interacts with repository-level memory,
  the technical mechanism for preference inference, token cost implications, or
  whether preferences are stored on GitHub infrastructure or in-context.

## Extracted Claims

### Claim 1: Copilot Memory now operates at the user scope, not just the repository scope — preferences follow the user across all repositories and Copilot agents

- **Evidence**: Official GitHub changelog describing the expansion from repository-level
  to user-level scope. The cross-repository persistence is stated explicitly as the
  defining characteristic of the new capability.
- **Confidence**: settled (product fact from official first-party changelog)
- **Quote**: "your preferences can follow you wherever you work, across all your
  repositories and Copilot agents, without affecting other users"
- **Our assessment**: The scope shift from repository to user is architecturally
  significant. Repository-level memory binds learned behavior to a specific codebase
  context — useful for project-specific conventions, but requires re-learning in new
  repositories. User-level memory binds learned behavior to the individual practitioner
  — coding style, communication preferences, PR conventions — which are stable across
  projects. The "without affecting other users" clause is the critical isolation
  guarantee: user-level preferences are per-individual, not shared with teammates.
  This distinguishes user memory from repository-level memory (which would affect all
  contributors) and from org-level memory (which would apply to all members). For
  Ch05: this separation is the key design principle for teams adopting user-level
  personalization — each team member accumulates their own preference profile
  independently. For Ch02: the user scope introduces a new layer in the Copilot
  configuration hierarchy (user > repository > organization) that practitioners need
  to understand when troubleshooting unexpected agent behavior.

### Claim 2: Copilot Memory stores both explicitly stated preferences and preferences inferred from behavior patterns

- **Evidence**: Official changelog uses a specific two-category framing ("stated or
  inferred") that distinguishes deliberate user declaration from passive behavioral
  observation. The distinction is stated explicitly in the product description.
- **Confidence**: settled (the two-category framing appears directly in the changelog)
- **Quote**: "store stated or inferred personal preferences about how you like to
  interact with it"
- **Our assessment**: The stated-vs-inferred distinction is the most architecturally
  interesting claim in this changelog. "Stated" preferences require deliberate user
  action — telling Copilot something explicitly. "Inferred" preferences require no
  deliberate action — the system observes behavioral patterns (e.g., consistently
  writing commit messages in imperative voice) and stores them without explicit
  instruction. The inference mechanism is not described, but the implication is that
  Copilot observes patterns across interactions and identifies stable user behaviors
  worth encoding. This is qualitatively different from preference management systems
  that require explicit configuration — the system learns from normal usage. For Ch06:
  practitioners should understand that Copilot may store inferred preferences that
  the user did not consciously provide. The management interface (Claim 4) provides
  the recourse mechanism — users can review and delete stored inferences. The
  stated-vs-inferred architecture is consistent with the emergent expertise accumulation
  pattern in [[blog-anthropic-claude-managed-agents-memory]] (Claim 11: Wisedocs found
  that cross-session memory "identify and remember common issues — including ones we
  didn't think about"), applied here at the user preference layer rather than the
  agent knowledge layer.

### Claim 3: The documented preference categories include commit message style, PR structure, and communication/tone preferences

- **Evidence**: Official changelog enumerates these as examples of stored preferences.
  These are illustrative examples, not an exhaustive list.
- **Confidence**: settled (examples listed in official changelog)
- **Quote**: (no direct quote; the preference categories are enumerated as examples
  without a single extractable sentence — see paraphrase in Our assessment)
- **Our assessment**: The three example categories reveal the design target: user-level
  preferences are intended for stable practitioner habits rather than project-specific
  conventions. Commit message style (e.g., imperative vs. past tense, ticket number
  prefixes) and PR structure (e.g., description length, checklist format, reviewer
  mention patterns) are practitioner conventions that persist across every project the
  developer works on. Communication/tone preferences (e.g., formal vs. casual review
  comments, level of explanation detail) are even more stable — they reflect
  personality and professional habits. None of these three categories are codebase-
  specific, which makes them appropriate targets for user-level (not repository-level)
  storage. For Ch02: practitioners configuring AI-assisted code review workflows should
  note that these preferences will be accumulated from normal usage without explicit
  CLAUDE.md or AGENTS.md configuration — the preference layer is below the
  configuration-file layer.

### Claim 4: User preferences are reviewable and individually deletable via personal Copilot Memory settings on GitHub

- **Evidence**: Official changelog describes the management interface as a personal
  Copilot Memory settings page, with deletion of specific memories supported.
- **Confidence**: settled (management interface described in official changelog)
- **Quote**: (no direct quote for the management interface description; the capability
  is stated but not with a single extractable sentence)
- **Our assessment**: The management interface matters for two practitioner scenarios:
  (1) privacy and data governance — users who do not want behavioral inference stored
  persistently can delete specific entries rather than disabling the feature entirely;
  (2) incorrect preference correction — if Copilot infers a preference incorrectly
  (e.g., inferring that a user prefers short commit messages when the short examples
  were context-specific), the user can delete that inference and allow re-learning.
  The individual-deletion granularity (rather than all-or-nothing) is a better user
  experience than the alternative. For Ch06: this management interface is the
  governance surface for user-level memory — analogous to the enterprise governance
  features (audit logs, version rollback, content redaction) described for
  Claude Managed Agents memory in [[blog-anthropic-claude-managed-agents-memory]]
  (Claim 8), but at the individual-user level rather than the enterprise level.

### Claim 5: The feature is available in early access for Pro and Pro+ only, with GitHub signaling plans to expand to additional subscription tiers

- **Evidence**: Official changelog states Pro and Pro+ as the initial access tier
  ("early access"). Future expansion is indicated with: "bring it to more plans in
  the future." Community feedback is explicitly solicited.
- **Confidence**: settled (access tier); emerging (future expansion — stated intent,
  no timeline or specific plans)
- **Quote**: "bring it to more plans in the future"
- **Our assessment**: The early-access framing signals this is a beta capability —
  behavior may change before general availability. The Pro/Pro+ gating is consistent
  with the pattern established in [[docs-github-copilot-individual-plan-changes]]
  (Claim 6), where Opus 4.7 was also gated to Pro+, and new feature development is
  concentrated in paid individual tiers before broader availability. The "bring it
  to more plans" statement implies Business and Enterprise availability is planned
  but not announced — relevant for teams evaluating whether to deploy user-level
  personalization at scale. Early-access status means practitioners should treat
  specific behaviors as subject to change and monitor the GitHub changelog before
  building workflows that depend on this feature.

### Claim 6: Enabling user-level memory requires an explicit opt-in toggle in individual Copilot settings — it is not enabled by default

- **Evidence**: Official changelog describes activation as navigating to Copilot
  settings and enabling the Copilot Memory toggle. This implies the feature is
  opt-in rather than automatically active.
- **Confidence**: emerging (the opt-in nature is implied by the toggle-to-enable
  description, not stated explicitly as "disabled by default")
- **Quote**: (no direct quote; the activation path is described procedurally but
  not in a single extractable sentence)
- **Our assessment**: The explicit opt-in model has two implications for practitioners.
  First, the feature is under user control — no preference inference happens without
  deliberate activation. This addresses the privacy concern that would arise if
  inference were automatic. Second, team-wide adoption requires individual activation
  per user — there is no org-level forced enablement described in this changelog
  (though that may change when Business/Enterprise support arrives). For Ch05: teams
  advising developers on Copilot configuration should add the Copilot Memory toggle
  to their onboarding checklist, alongside CLAUDE.md and AGENTS.md setup, with a
  note that preferences will accumulate passively from normal usage after activation.

## Concrete Artifacts

### Copilot Memory User-Level Feature Summary (as of May 15, 2026)

```
GitHub Copilot Memory — User-Level Preferences

SCOPE:
  Previous:    Repository-level only
  New:         User-level (user > repository)
  Isolation:   Preferences are per-user; do NOT affect teammates

PREFERENCE STORAGE:
  Stated:      Explicitly declared by the user
  Inferred:    Derived from observed behavioral patterns
  Examples:    - Commit message style
               - Pull request structure
               - Communication and tone preferences

CROSS-SESSION AVAILABILITY:
  Follows user: across ALL repositories
  Follows user: across ALL Copilot agents (CLI, IDE, web)

MANAGEMENT:
  Interface:   Personal Copilot Memory settings on GitHub
  Granularity: Individual memory deletion supported
  Review:      Users can inspect stored preferences

ACTIVATION:
  Path:        Copilot settings → enable Copilot Memory toggle
  Default:     Opt-in (requires explicit activation)

ACCESS TIER (as of May 15, 2026):
  Early access: Copilot Pro, Copilot Pro+
  Planned:      "more plans in the future" (no timeline given)
  Status:       Early access — behavior subject to change

Source: GitHub official changelog, May 15, 2026
```

### Copilot Memory Configuration Scope Hierarchy

```
GitHub Copilot — Configuration Scope Hierarchy (with Memory)

Level 1 — Organization/Enterprise (admin-controlled):
  • Copilot policy settings (which third-party agents are allowed)
  • [Memory: not yet available at this scope as of May 15, 2026]

Level 2 — Repository (repo owner/contributor-controlled):
  • .github/copilot-instructions.md
  • Agent skills in .github/skills/, .claude/skills/, .agents/skills/
  • [Memory: pre-existing repository-level Copilot Memory]

Level 3 — User (individual-controlled):
  • User-level custom agents in %USERPROFILE%/.github/agents/ (VS, per
    docs-github-copilot-vs-april-2026.md Claim 5)
  • [NEW] User-level Copilot Memory preferences (this source)
  • Does not affect teammates; follows user across all repos/agents

Note: Interaction between repository-level and user-level memory is
not documented in this changelog.
```

## Cross-References

- **Corroborates**:
  - **blog-anthropic-claude-managed-agents-memory.md** (Claim 5): The scoped
    sharing model ("org-wide store might be read-only, while per-user stores allow
    reads and writes") maps directly to the isolation guarantee in this source
    ("without affecting other users"). Both sources independently document the
    same design principle: user-level memory is isolated from other users, while
    org-level memory is shared but access-controlled. GitHub Copilot and Claude
    Managed Agents have converged on the same user/org scope model for memory
    architecture.
  - **docs-github-copilot-individual-plan-changes.md** (Claim 6): Opus 4.7 is
    gated to Pro+ on individual plans. User-level Copilot Memory is now gated to
    Pro/Pro+ in early access. Both confirm the pattern that new premium features
    on GitHub Copilot land first on paid individual tiers (Pro/Pro+) before
    broader availability.

- **Extends**:
  - **blog-anthropic-claude-managed-agents-memory.md**: That source documents
    agent-level cross-session memory for Claude Managed Agents (filesystem-based,
    with org-wide and per-user scoping). This source adds a second major commercial
    tool instance of the same pattern, applied at the user-preference layer rather
    than the agent-knowledge layer. The corpus now has two independent implementations
    of cross-session memory with user-level isolation, increasing confidence that
    user-scoped persistent memory is an emerging platform primitive for AI coding tools.
  - **docs-github-copilot-vs-april-2026.md** (Claim 5): That note established
    user-level custom agent definitions in `%USERPROFILE%/.github/agents/` that
    "travel across projects without per-project configuration." This source adds
    user-level *preferences* (memory) as a second cross-project, user-scoped
    persistence mechanism in Copilot. Together, these two sources establish a
    pattern: GitHub Copilot is building a user-scope layer for AI configuration
    (agent definitions + memory preferences) that complements the existing
    repository-scope and organization-scope layers.
  - **docs-github-copilot-individual-plan-changes.md**: That source documented
    plan-level Opus model access changes (Opus removed from Pro; Opus 4.7 on Pro+).
    This source adds another plan-gated capability to the Pro/Pro+ tier. Together,
    they reveal an emerging GitHub strategy: premium individual features — high-capability
    models and advanced personalization — are being concentrated in the Pro/Pro+ tier.

- **Contradicts**: None found. No existing corpus note claims that Copilot Memory
  is limited to repository scope only; the prior scope was documented only by
  implication in model-selection notes. No contradiction issue required.

- **Novel**:
  - **Stated vs. inferred preference distinction in a commercial AI coding tool**:
    No prior corpus source documents a commercial AI coding tool that distinguishes
    between explicitly stated and behaviorally inferred user preferences. The inference
    mechanism — learning from normal usage patterns rather than requiring deliberate
    configuration — is new to the corpus and qualitatively different from CLAUDE.md /
    AGENTS.md configuration approaches.
  - **User-level scope for preference persistence in GitHub Copilot**:
    Prior corpus sources on Copilot Memory (if any) covered repository scope.
    This is the first source documenting user-level scope with cross-repository
    persistence. The isolation guarantee ("without affecting other users") establishes
    the first named user-scope isolation property for GitHub Copilot memory.
  - **Passive preference accumulation as a configuration mechanism**:
    Unlike CLAUDE.md or agent skill files (which require deliberate authoring),
    user-level Copilot Memory accumulates inferred preferences from normal usage.
    This "configuration as a side effect of work" model is new to the corpus —
    no prior source documents a Copilot feature that self-configures from observed
    behavior without explicit user action.

## Guide Impact

- **Chapter 02 (Harness Engineering / Tool Configuration)**: Add a note that the
  GitHub Copilot configuration hierarchy now has a user scope below the repository
  scope. The user scope covers both user-level custom agent definitions
  (`docs-github-copilot-vs-april-2026.md`, Claim 5) and user-level memory preferences
  (this source). Practitioners debugging unexpected Copilot behavior should check
  all three layers: org policy, repository instructions/skills, and user-level memory.
  The existence of inferred preferences (Claim 2) means the effective configuration
  surface is larger than just the explicitly authored files.

- **Chapter 05 (Team Adoption / Personalization vs. Team Settings)**: This source
  is directly relevant to the key question the Prospector flags: how do user preferences
  interact with team settings? The answer this changelog provides: user-level memory
  is strictly per-user ("without affecting other users") and is currently individual-
  plan only (Pro/Pro+). Teams should plan for a two-track personalization model:
  (a) team-level conventions encoded in repository-scope configuration
  (`.github/copilot-instructions.md`, agent skills); (b) individual-level habits
  accumulated passively in user-level memory. For Ch05: advise teams to include
  Copilot Memory activation in individual onboarding checklists, with guidance on
  what the three example preference categories (commit style, PR structure, tone) mean
  for team conventions — should individual preferences align with team norms, or is
  deviation acceptable?

- **Chapter 06 (Scaling / Maintaining AI-Native Systems)**: The management interface
  (Claim 4) and opt-in activation (Claim 6) are the governance touch points for
  user-level memory in a team setting. For Ch06: practitioners maintaining AI-native
  systems should document which Copilot features are expected to be active for team
  members (including user-level memory) and establish a review process for incorrect
  inferences. The early-access status (Claim 5) means behavior may change —
  recommending teams monitor the GitHub changelog as a maintenance practice.

## Extraction Notes

- The source is a short GitHub changelog entry (~300–400 words by estimate, consistent
  with other GitHub changelog entries in the corpus). The WebFetch tool returned
  summaries that were consistent across two separate fetch calls with different prompts.
  Quotes marked as (no direct quote) are cases where the changelog described a
  capability without a single extractable verbatim sentence; the content is paraphrased
  in Our assessment. The three verbatim quotes (Claims 1, 2, 5) appeared in quotation
  marks in the WebFetch output and are treated as direct quotes from the source.
- The source is labeled `triaged:text` and the second Prospector triage comment
  classified it as a blog-post for routing purposes, while the first triage comment
  classified it as docs. The file naming convention follows the existing GitHub
  Copilot changelog entries in this corpus, which use the `docs-github-copilot-`
  prefix regardless of whether the source is the changelog or documentation proper.
- No linked sub-pages were identified in the WebFetch output. The changelog appears
  to link to the Copilot settings page and the GitHub Community discussions forum,
  but these are navigation targets rather than substantive content pages. No
  sub-pages were followed.
- The interaction between the pre-existing repository-level Copilot Memory and the
  new user-level Copilot Memory is not documented in this changelog. It is unclear
  whether user-level and repository-level memories are additive, whether one takes
  precedence, or whether they are retrieved and composed together. This gap should
  be flagged when this source informs guide content.
- No contradictions were identified against existing corpus notes. Two potential
  areas of comparison were examined: the Claude Managed Agents memory note
  (different tool, same scoping architecture — corroborates rather than contradicts)
  and the individual plan changes note (same subscription tier framing — extends
  rather than contradicts).
