---
source_url: https://github.blog/changelog/2026-06-05-enterprise-managed-plugins-in-vs-code-in-public-preview
source_type: docs
title: "Enterprise-managed plugins in VS Code in public preview"
author: GitHub (official changelog)
date_published: 2026-06-05
date_extracted: 2026-06-08
last_checked: 2026-06-08
status: current
confidence_overall: emerging
issue: "#1111"
---

# Enterprise-Managed Plugins in VS Code in Public Preview

> GitHub's June 2026 changelog extends enterprise-managed plugin distribution to VS Code
> (v1.122+), establishing a concrete configuration path — `.github-private/.github/copilot/settings.json` —
> through which enterprise administrators can define plugin marketplaces, auto-install custom agents
> and skills, and enforce hooks and MCP configurations across Copilot Business and Enterprise users
> in both VS Code and Copilot CLI.

## Source Context

- **Type**: docs (GitHub official product changelog, June 5, 2026; approximately 300 words)
- **Author credibility**: GitHub engineering team announcing a production public preview feature.
  Authoritative for the fact that this capability exists, the specific configuration file path,
  the supported client versions (VS Code 1.122+), the license requirements (Copilot Business or
  Copilot Enterprise), and the two configuration categories (plugin distribution and governance
  controls). Not a credible source for how well automatic plugin enforcement works in practice,
  how conflicts between user-installed and enterprise-managed plugins are resolved, or what the
  full schema of the settings.json file looks like. No empirical data on adoption outcomes.
- **Scope**: The public preview of enterprise-managed plugins in VS Code, covering the configuration
  file path, two capability categories (auto-install and governance/hooks/MCP), license requirements,
  version requirements, and the relationship to the prior Copilot CLI enterprise launch from May 2026.
  References enterprise-managed client settings documentation (URL not directly provided in
  changelog). Also links to a GitHub Community discussion (#178247). Does NOT cover: the exact
  JSON schema for settings.json, what happens when a user runs a different VS Code version, how
  plugin conflicts are resolved, whether individual users can override enterprise-managed settings,
  cost implications of enterprise plugin management, or how this interacts with VS Code workspace
  extensions vs. Copilot agent plugins specifically.

## Extracted Claims

### Claim 1: Enterprise-managed plugin capabilities for VS Code entered public preview in VS Code 1.122, achieving feature parity with the Copilot CLI enterprise launch from May 2026

- **Evidence**: Official changelog states: "Last month we launched a public preview with Copilot
  CLI that allows enterprise administrators the ability to configure and distribute plugins to
  GitHub Copilot CLI users across their enterprise." VS Code 1.122 is named as the version where
  VS Code support was added.
- **Confidence**: settled (product fact — public preview status and version requirement documented
  in official changelog)
- **Quote**: "Last month we launched a public preview with Copilot CLI that allows enterprise
  administrators the ability to configure and distribute plugins to GitHub Copilot CLI users across
  their enterprise."
- **Our assessment**: This is significant for the corpus because it establishes that enterprise
  plugin governance is now a two-client story (VS Code + CLI), not a CLI-only feature. The May
  2026 CLI launch was not documented in our corpus. This changelog is the first source to confirm
  that the enterprise plugin model applies equally to VS Code and CLI clients. For Ch05 (Team
  Adoption): the availability on both major developer-facing clients makes this a practical
  governance lever, not an edge case.

### Claim 2: The baseline enterprise plugin standards apply uniformly to every user's Copilot CLI and VS Code clients, creating a single point of configuration for both clients

- **Evidence**: Official changelog states: "The baseline standards you set for your enterprise
  apply to every user's Copilot CLI and VS Code clients."
- **Confidence**: settled (product guarantee stated in official changelog)
- **Quote**: "The baseline standards you set for your enterprise apply to every user's Copilot
  CLI and VS Code clients."
- **Our assessment**: The single-configuration-for-two-clients property is a meaningful governance
  simplification. Before this, enterprises that wanted consistent tooling across CLI and VS Code
  users would need to manage per-client configuration paths or rely on user compliance. With
  enterprise-managed settings, a single settings.json file at the `.github-private/` path controls
  both surfaces. For Ch02 (Harness Engineering): this is the first documented mechanism in the
  corpus for enforcing a consistent AI tooling baseline across multiple developer clients from a
  single configuration artifact.

### Claim 3: Enterprise plugin settings are defined in a settings.json file at `.github-private/.github/copilot/settings.json`

- **Evidence**: Official changelog states: "Define plugin marketplaces in a `settings.json` file
  located at `.github-private/.github/copilot/settings.json`."
- **Confidence**: settled (file path documented in official changelog)
- **Quote**: "Define plugin marketplaces in a `settings.json` file located at
  `.github-private/.github/copilot/settings.json`."
- **Our assessment**: The `.github-private/` path prefix is the significant architectural signal
  here. The `.github-private/` convention is a GitHub-documented mechanism for enterprise-wide
  configuration stored in a private repository that propagates to all enterprise members. This
  means the enterprise plugin settings live in source control (in a designated private repo), are
  version-controlled, and can be managed via PRs and code review — not via a GUI-only admin console.
  For Ch02: document `.github-private/.github/copilot/settings.json` as the new configuration
  surface for enterprise-wide Copilot plugin governance. Teams should treat this file with the
  same rigor as other infrastructure-as-code artifacts.

### Claim 4: Enterprises can automatically install plugins to improve developer onboarding and broadly distribute custom agents and skills

- **Evidence**: Official changelog states: "automatically install, helping improve developer
  onboarding and reduce setup time by broadly sharing custom agents and skills."
- **Confidence**: settled (capability described in official changelog)
- **Quote**: "automatically install, helping improve developer onboarding and reduce setup time
  by broadly sharing custom agents and skills."
- **Our assessment**: Auto-install of plugins at the enterprise level closes a gap that existed
  in the prior `gh skill install` model (documented in `docs-github-copilot-agent-skills-cli.md`):
  that model required each developer to explicitly run `gh skill install` to get enterprise skills.
  Enterprise-managed auto-install removes the manual step — developers who authenticate through
  the enterprise Copilot account receive the configured plugins automatically. For Ch05 (Team
  Adoption): this is the enterprise-scale push model complementing the individual pull model of
  `gh skill install`. Organizations that want to ensure all developers start with a baseline
  set of custom agents and skills should use auto-install rather than relying on developer-
  initiated installation.

### Claim 5: Enterprises can strengthen governance by defining hooks and MCP configurations that are always enabled across the enterprise

- **Evidence**: Official changelog states: "strengthen your governance strategy by defining hooks
  and MCP configurations that are always enabled across your enterprise."
- **Confidence**: emerging (capability asserted in official changelog, but the enforcement mechanism
  — whether users can disable enterprise-enforced hooks — is not described)
- **Quote**: "strengthen your governance strategy by defining hooks and MCP configurations that
  are always enabled across your enterprise."
- **Our assessment**: The mention of hooks and MCP configurations as enterprise-governed items is
  novel. Prior corpus sources document hooks (e.g., Claude Code's pre-tool-call hooks) and MCP
  servers as per-developer or per-project configuration concerns. This is the first source to
  describe a mechanism for enterprise-level enforcement of hooks and MCP configurations. For Ch02
  (Harness Engineering): hooks that enforce security policies (e.g., "always run static analysis
  before file edits") or MCP configurations that enforce approved data sources can now be deployed
  at enterprise scale without per-developer action. The word "always enabled" is strong — it
  implies these configurations cannot be disabled by individual users, though this is not
  explicitly confirmed in the source. The Assayer should verify the enforcement semantics when
  the full documentation becomes available.

### Claim 6: The enterprise managed plugin feature requires Copilot Business or Copilot Enterprise license for the settings to apply to users

- **Evidence**: Official changelog states: "both VS Code and Copilot CLI will automatically pull
  and apply these settings for users licensed through your enterprise account with Copilot Business
  or Copilot Enterprise."
- **Confidence**: settled (license requirement stated explicitly in official changelog)
- **Quote**: "both VS Code and Copilot CLI will automatically pull and apply these settings for
  users licensed through your enterprise account with Copilot Business or Copilot Enterprise."
- **Our assessment**: The license gate is practically significant for adoption planning. Teams
  with individual or team-tier Copilot licenses cannot use enterprise-managed plugins — the feature
  is exclusively for Business and Enterprise accounts. For Ch05 (Team Adoption): organizations
  evaluating whether to upgrade from team-tier to Business/Enterprise licenses should include
  enterprise-managed plugin governance as one concrete differentiation, alongside CCA custom
  properties (documented in `docs-github-copilot-cca-custom-properties.md`) and enterprise-level
  model selection controls.

## Concrete Artifacts

### Enterprise Plugin Configuration Path

```
Configuration file: .github-private/.github/copilot/settings.json

Notes:
  - .github-private/ is a GitHub-documented enterprise-wide private repository path
  - Changes here propagate to all Copilot Business / Enterprise licensed users
  - Applies uniformly to both VS Code (1.122+) and Copilot CLI clients
  - Settings auto-apply when users authenticate through the enterprise account
```

Source: github.blog changelog, retrieved 2026-06-08

### Enterprise Plugin Capability Categories

```
Category 1: Plugin Distribution
  - Define plugin marketplaces
  - Auto-install plugins for licensed users
  - Distribute custom agents and skills broadly
  - Goal: improve developer onboarding, reduce setup time

Category 2: Governance Controls
  - Define hooks that are "always enabled" across the enterprise
  - Define MCP configurations that are "always enabled" across the enterprise
  - Goal: "strengthen your governance strategy"

Scope: Copilot Business and Copilot Enterprise licensed users
Client support: VS Code 1.122+ and Copilot CLI (as of June 2026 public preview)
```

Source: github.blog changelog, retrieved 2026-06-08

### Timeline: Enterprise Plugin Rollout

```
May 2026:   Public preview launched for Copilot CLI
            (referenced in June changelog, no specific date or note in corpus)

June 5, 2026: Public preview extended to VS Code (v1.122+)
              Both clients now share enterprise-managed plugin settings
              from .github-private/.github/copilot/settings.json
```

Source: github.blog changelog, retrieved 2026-06-08

## Cross-References

- **Corroborates**:
  - **docs-github-copilot-agent-skills-cli.md** (Claim 4): The `gh skill` note documents the
    individual `gh skill install` model for distributing agent skills. The enterprise-managed
    auto-install capability described here (Claim 4) is the administrator-push complement to
    that individual-pull model. Both sources converge on the same goal: consistent skill
    distribution across teams. The difference is the control locus — `gh skill install` is
    developer-initiated; enterprise auto-install is administrator-initiated.
  - **docs-github-copilot-cca-custom-properties.md** (Claim 1): The CCA custom properties
    note documents enterprise-level selective enablement for Copilot Cloud Agent (CCA) via
    custom properties. Both sources document administrative governance mechanisms in the
    Copilot Enterprise tier. Together they show a maturing enterprise governance stack: custom
    properties control which orgs can access CCA; managed plugins control what tooling baseline
    all licensed users receive.
  - **docs-github-copilot-vs-may-2026.md** (Claim 11): The May 2026 VS update documented
    commit message custom instructions migrating from IDE settings to the repository Copilot
    instructions file — a pattern of centralizing Copilot configuration in repository-controlled
    files. This source continues that same pattern at the enterprise level: administrator-defined
    hooks and MCP configs live in `.github-private/` (a source-controlled path), not in a GUI
    admin console.

- **Contradicts**: None identified. No existing corpus source documents a conflicting claim
  about enterprise plugin management. The `gh skill install` individual model
  (`docs-github-copilot-agent-skills-cli.md`) is not contradicted — enterprise auto-install
  complements it. No contradiction issue filed.

- **Extends**:
  - **docs-github-copilot-agent-skills-cli.md**: Adds the enterprise-push layer on top of the
    individual-pull layer. The lifecycle of a managed skill is now: author skill → publish to
    marketplace or private repo → enterprise admin adds to settings.json auto-install list →
    all licensed users receive it automatically. The CLI note covers the individual steps; this
    source covers the enterprise-scale distribution endpoint.
  - **docs-github-copilot-cca-custom-properties.md**: Extends the enterprise governance surface
    from "which orgs can access CCA" (that note) to "what tooling baseline every licensed user
    receives" (this note). Together they define the two axes of enterprise Copilot governance:
    access control and tooling standardization.
  - **docs-github-copilot-vs-april-2026.md** (Claim 1): April documented multi-path skill
    discovery from `.claude/skills/`, `.agents/skills/`, and `.github/skills/`. This source
    adds a fourth path relevant to enterprise administrators: skills defined in the enterprise
    settings.json and auto-installed override or complement what developers discover locally.
    The two mechanisms operate at different levels of the configuration hierarchy.

- **Novel**:
  - **Enterprise-level hooks enforcement**: No prior corpus source documents a mechanism for
    an enterprise administrator to enforce that specific hooks are "always enabled" across all
    developer clients. Hook configuration has been documented exclusively as per-developer or
    per-project (Claude Code hooks in `.claude/settings.json`, Copilot hooks in local config).
    The ability to enforce hooks enterprise-wide is a new governance primitive.
  - **Enterprise-level MCP configuration enforcement**: Similarly, all prior MCP configuration
    in the corpus is at the individual or project level. This is the first documented mechanism
    for enterprise-enforced MCP server configurations.
  - **`.github-private/` as an AI tooling governance path**: The `.github-private/` repository
    convention is established in GitHub Enterprise for some configuration scenarios, but this
    is its first appearance in the corpus as a path for AI tooling governance (Copilot plugin
    settings, hooks, MCP). Document this path as an emerging enterprise AI configuration layer.
  - **Auto-install of custom agents and skills across enterprise**: While `gh skill install`
    documents developer-initiated installation, enterprise auto-install removes the requirement
    for developer action entirely. First documented instance of a push-based agent configuration
    model in the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering — Enterprise Configuration)**:
  - Add a new subsection on enterprise-managed Copilot settings, centered on the
    `.github-private/.github/copilot/settings.json` configuration file. Document its scope
    (all Copilot Business/Enterprise users, both VS Code and CLI), its two categories (plugin
    distribution and governance/hooks/MCP), and its infrastructure-as-code nature (lives in
    source control). This is a new configuration surface with no prior guide coverage.
  - Add the auto-install of custom agents and skills as the enterprise-scale alternative to
    `gh skill install`. Practitioners building enterprise AI tooling should evaluate whether
    to use developer-initiated install (for user-choice environments) or enterprise auto-install
    (for standardized baseline enforcement).
  - Add the hooks and MCP governance capability as a new enterprise hardening pattern. Teams
    that have defined security hooks (e.g., always-run static analysis, always-block certain
    file writes) should evaluate enterprise-managed hooks as the deployment mechanism that
    scales without relying on each developer configuring their own client.

- **Chapter 05 (Team Adoption — Enterprise Governance)**:
  - Add enterprise-managed plugins as a new lever in the enterprise adoption toolkit alongside
    CCA custom properties (`docs-github-copilot-cca-custom-properties.md`) and model rules.
    The adoption arc for an enterprise AI engineering program now has two distinct governance
    mechanisms: access control (who gets CCA) and tooling standardization (what baseline
    everyone gets).
  - Document the Copilot Business vs. Enterprise license gate as a practical prerequisite for
    this governance approach. Organizations on individual or team tier cannot use enterprise-
    managed plugins — upgrade planning should include this capability as a concrete benefit
    of Business/Enterprise licensing.
  - Note the VS Code 1.122+ requirement for VS Code clients. Enterprises with standardized
    developer environments should ensure VS Code version management includes this as a minimum.

## Extraction Notes

1. **Short changelog (~300 words)**: The source is a brief changelog entry. All substantive
   content was exhausted in 6 claims above. Three WebFetch calls were made to ensure verbatim
   accuracy. The full JSON schema for settings.json was not included in the changelog — the
   source references "enterprise managed client settings docs" without providing the direct URL.
   A separate fetch of the most likely documentation URL
   (`docs.github.com/en/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-copilot-client-settings-for-your-enterprise`)
   returned 404, suggesting the docs page may be behind authentication or at a different path.
   The full schema detail is therefore not available from this extraction.

2. **WebFetch verbatim limitations**: The WebFetch tool processes content through an AI model.
   All quotes in this note were explicitly marked as verbatim by the WebFetch responses and were
   verified across multiple independent fetches of the same URL for consistency. The Assayer
   should spot-check quotes against the live source URL. Any claim for which no reliable verbatim
   text was recoverable is marked `(no direct quote; see paraphrase in Our assessment)`.

3. **May 2026 CLI launch not in corpus**: The changelog references a "last month" Copilot CLI
   enterprise plugin preview launch (May 2026) that is not currently documented in any corpus
   source note. The CLI note (`docs-github-copilot-agent-skills-cli.md`) covers `gh skill`
   from April 2026 but not the enterprise-managed plugin feature. The May 2026 CLI launch may
   warrant a separate source note if the changelog entry for that feature is findable.

4. **Public preview status**: This feature is in public preview as of June 5, 2026. Behaviors
   and configuration schema may change before GA. Confidence ratings reflect the current
   published documentation, not GA-stable behavior. Guide sections citing this note should
   note the preview status until GA is announced.

5. **No contradictions to file**: Cross-referencing all enterprise governance, skills, and
   Copilot configuration notes found no opposing claims. The `gh skill install` individual model
   is complementary, not contradictory, to enterprise auto-install. No contradiction issue filed.
