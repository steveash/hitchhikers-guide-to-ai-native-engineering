---
source_url: https://github.blog/changelog/2026-06-17-enterprise-managed-settings-now-support-bypass-permission-controls
source_type: docs
title: "Enterprise-managed settings now support bypass permission controls"
author: GitHub (official changelog)
date_published: 2026-06-17
date_extracted: 2026-06-19
last_checked: 2026-06-19
status: current
confidence_overall: emerging
issue: "#1219"
---

# Enterprise-Managed Settings Now Support Bypass Permission Controls

> GitHub's June 17, 2026 changelog extends the enterprise-managed settings system with a
> `disableBypassPermissionsMode` control that prevents Copilot CLI and VS Code from
> automatically approving permission prompts, giving enterprise administrators a concrete
> governance lever against auto-approval ("yolo mode") behavior across the organization.

## Source Context

- **Type**: docs (GitHub official product changelog, June 17, 2026; approximately 300 words)
- **Author credibility**: GitHub engineering team announcing a governance extension to the
  enterprise-managed settings system. Authoritative for: the existence and name of the
  `disableBypassPermissionsMode` setting, the configuration file paths, the scope (VS Code
  and Copilot CLI), license requirements, and the new preferred configuration path. Not a
  credible source for: how bypass permissions mode operates at the technical level, whether
  individual users can partially override the setting, adoption data, or performance impact
  of disabling bypass mode.
- **Scope**: A single new governance control (`disableBypassPermissionsMode`) in the
  enterprise-managed settings system. Covers the configuration paths, what the control does,
  scope of application, license requirements, how to verify the setting is active, and the
  relationship to the existing `.github-private` source organization. Does NOT cover: the
  full JSON schema for the settings file, other available controls in the same system,
  technical details of what "bypass permissions mode" actually permits at the OS or API
  level, or per-user override capability.

## Extracted Claims

### Claim 1: Enterprise administrators can prevent Copilot CLI and VS Code from automatically skipping permission prompts by setting `disableBypassPermissionsMode` to `"disable"` in the enterprise-managed settings file

- **Evidence**: Official GitHub product changelog announcing the new setting. The technical
  identifiers (`disableBypassPermissionsMode`, `"disable"`) are specific enough to treat as
  authoritative configuration facts. The setting addresses a mode informally referred to in
  the WebFetch summary as "yolo mode" — automatic bypass of permission prompts.
- **Confidence**: settled (product fact in official changelog; setting name and value
  are technical identifiers unlikely to be misquoted by WebFetch summarization)
- **Quote**: (no direct verbatim quote available — WebFetch AI-summarized the source
  content; see Extraction Notes and paraphrase in Our assessment)
- **Our assessment**: This control addresses a governance gap in the prior enterprise-managed
  settings coverage. The June 5, 2026 note (`docs-github-copilot-enterprise-managed-plugins-vscode.md`)
  documented enterprise-enforced hooks and MCP configurations but did not mention any
  control over automatic permission approval behavior. This new setting adds an explicit
  enterprise-level control over whether Copilot tools can automatically accept permission
  prompts without user evaluation. In environments where prompt injection or social
  engineering could exploit auto-approved permissions (see `blog-anthropic-how-contain-claude.md`
  Claim 11: 96% success rate on a credential-exfiltration prompt injection test), the ability
  to mandate human review of every permission prompt is a significant security control.

### Claim 2: The bypass permissions control applies uniformly to both Copilot CLI and VS Code using the same enterprise settings mechanism as the June 5 plugin governance feature

- **Evidence**: Official changelog describes scope as both Copilot CLI and VS Code clients —
  consistent with the dual-client architecture documented in
  `docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 2.
- **Confidence**: settled (dual-client scope consistent with prior source and with the
  architecture stated in the June 17 changelog)
- **Quote**: (no direct verbatim quote; dual-client scope consistent across WebFetch
  summary and prior note)
- **Our assessment**: Uniform application across both clients is architecturally important.
  A bypass-permissions control that applied only to one client would create a governance gap
  (e.g., a developer who switches from VS Code to CLI could bypass a VS Code-level
  restriction). The dual-client enforcement means the enterprise governance posture is
  consistent regardless of which Copilot surface is used. This follows the architecture
  established in `docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 2:
  "The baseline standards you set for your enterprise apply to every user's Copilot CLI
  and VS Code clients."

### Claim 3: The setting is configured in `.github-private/.github/copilot/settings.json`, the same private repository path used by the enterprise plugin settings from June 5

- **Evidence**: Official changelog states the configuration file path — consistent with the
  path documented in `docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 3.
- **Confidence**: settled (file path stated in official changelog; consistent with prior note)
- **Quote**: (no direct verbatim quote; path consistent with prior source note Claim 3)
- **Our assessment**: Path consistency is significant for enterprise configuration management.
  All enterprise-managed Copilot settings — plugin distribution, hooks, MCP configurations,
  and now bypass permissions mode — live in the same configuration file. This means the
  bypass permissions control is version-controlled alongside the other enterprise governance
  settings, and teams already managing the enterprise plugin settings file can add the new
  control without setting up a separate configuration surface. For Ch02 (Harness Engineering):
  document `.github-private/.github/copilot/settings.json` as the growing single file for
  all enterprise Copilot governance — not just plugin distribution.

### Claim 4: A new preferred configuration path `copilot/managed-settings.json` has been introduced, with backward compatibility maintained for `.github/copilot/settings.json`

- **Evidence**: Official changelog mentions a new preferred configuration path with backward
  compatibility for the existing path.
- **Confidence**: settled (path change stated in official changelog)
- **Quote**: (no direct verbatim quote; see paraphrase in Our assessment)
- **Our assessment**: This path migration signals that the enterprise-managed settings are
  maturing into a more dedicated namespace. The practical implication: teams that configured
  settings using the old `.github/copilot/settings.json` path do not need to migrate
  immediately, but new configurations should use the new preferred `copilot/managed-settings.json`
  path. For Ch02: update documentation of the enterprise-managed settings paths to note both,
  with `copilot/managed-settings.json` as the new preferred location. This is a breaking
  change in naming convention for new configurations.

### Claim 5: VS Code v1.122 and later already satisfies the client version requirement for enterprise-managed settings, including this new control

- **Evidence**: Official changelog confirms that VS Code 1.122+ already respects
  enterprise-managed settings — the same version requirement documented in
  `docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 1.
- **Confidence**: settled (version consistency with prior note, stated in official changelog)
- **Quote**: (no direct verbatim quote; see paraphrase in Our assessment)
- **Our assessment**: Enterprises that have already standardized VS Code 1.122+ for the June 5
  plugin governance features receive the bypass permissions control with no additional
  client-side requirement. The version baseline is the same. This lowers the deployment
  barrier for organizations that moved to VS Code 1.122+ in June 2026 for the initial
  enterprise-managed plugin feature.

### Claim 6: If a source organization for custom agents is already configured, the bypass permissions setting uses the existing `.github-private` repository — no new repository setup is required

- **Evidence**: Official changelog states that existing `.github-private` repository
  configurations are reused for this new setting.
- **Confidence**: settled (operational fact stated in official changelog)
- **Quote**: (no direct verbatim quote; see paraphrase in Our assessment)
- **Our assessment**: This reduces setup friction for enterprises that have already
  configured custom agents. The bypass permissions control is additive — it is a new key in
  an existing configuration file. Enterprises that have NOT yet configured a source
  organization for custom agents will need to do so before they can apply this control, which
  may be a meaningful prerequisite for some organizations new to the enterprise-managed
  settings system.

### Claim 7: Administrators can verify the bypass permissions control is active by checking the Agents page under AI controls in enterprise settings

- **Evidence**: Official changelog describes the administrative verification mechanism.
- **Confidence**: settled (verification path stated in official changelog)
- **Quote**: (no direct verbatim quote; see paraphrase in Our assessment)
- **Our assessment**: The Agents page under AI controls provides a UI-based audit surface
  for enterprise-managed settings. This means administrators do not need to inspect the
  settings file directly to confirm whether the control is active — they can verify via the
  GitHub Enterprise settings UI. For enterprise governance: add the Agents page verification
  step to the enterprise Copilot configuration checklist. This is the first documented
  verification path for enterprise-managed settings in the corpus.

### Claim 8: The setting requires Copilot Business or Copilot Enterprise licensing — the same license tier required for all enterprise-managed settings

- **Evidence**: Official changelog states license tier requirement — consistent with
  `docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 6.
- **Confidence**: settled (license requirement stated in official changelog; consistent
  with prior note Claim 6)
- **Quote**: (no direct verbatim quote; consistent with prior source note)
- **Our assessment**: The license tier gate is unchanged from the June 5 enterprise-managed
  settings feature. Organizations on individual or team-tier Copilot licenses cannot use
  enterprise-managed bypass permissions controls — the feature is exclusively for Business
  and Enterprise accounts. For Ch05 (Team Adoption): organizations evaluating whether to
  upgrade from team-tier to Business/Enterprise licenses should now include both plugin
  governance AND bypass permissions mode control as concrete differentiating capabilities.

## Concrete Artifacts

### Enterprise Settings Configuration (bypass permissions control)

```json
// Location: .github-private/.github/copilot/settings.json
// OR new preferred path: copilot/managed-settings.json
// (backward compat: .github/copilot/settings.json also accepted)

{
  "disableBypassPermissionsMode": "disable"
}

// Effect: Prevents Copilot CLI and VS Code from automatically
//         approving permission prompts ("bypass permissions mode")
// Scope:  All Copilot Business or Copilot Enterprise licensed users
// Client: VS Code v1.122+ and Copilot CLI
// Verify: Agents page → AI controls → GitHub Enterprise settings
// Prereq: Source org for custom agents must be configured
//         (reuses existing .github-private repository if already set up)
```

*Source: GitHub Copilot changelog, June 17, 2026. Configuration key name
(`disableBypassPermissionsMode`) and value (`"disable"`) extracted from WebFetch
summary and treated as verbatim technical identifiers. The surrounding JSON schema
is illustrative — verify exact schema format against the live source URL and the
enterprise managed client settings documentation.*

### Enterprise-Managed Settings Capability Map (as of June 17, 2026)

```
Configuration file: .github-private/.github/copilot/settings.json
New preferred path: copilot/managed-settings.json
License required:   Copilot Business or Copilot Enterprise
Client versions:    VS Code 1.122+ and Copilot CLI

Capabilities announced as of June 17, 2026:

1. Plugin distribution (June 5, 2026)
   - Define plugin marketplaces
   - Auto-install custom agents and skills
   - Source: docs-github-copilot-enterprise-managed-plugins-vscode.md

2. Governance controls (June 5, 2026)
   - Hooks that are "always enabled" across the enterprise
   - MCP configurations that are "always enabled"
   - Source: docs-github-copilot-enterprise-managed-plugins-vscode.md

3. Bypass permissions control (June 17, 2026) ← THIS NOTE
   - disableBypassPermissionsMode: "disable"
   - Prevents automatic approval of permission prompts
   - Source: docs-github-copilot-enterprise-bypass-permissions.md

Verification path: Agents page → AI controls → GitHub Enterprise settings
```

*Source: GitHub Copilot changelogs, June 5 and June 17, 2026*

## Cross-References

- **Corroborates**:
  - **`docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 2**:
    "The baseline standards you set for your enterprise apply to every user's Copilot CLI
    and VS Code clients." The dual-client enforcement pattern established June 5 is confirmed
    and extended. The bypass permissions control uses the same single-configuration-for-
    two-clients architecture.
  - **`docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 3**:
    Configuration at `.github-private/.github/copilot/settings.json` is reaffirmed as the
    central enterprise governance configuration surface, with a new preferred path added.
  - **`docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 6**:
    License requirement (Copilot Business or Copilot Enterprise) is consistent.
  - **`blog-anthropic-how-contain-claude.md` Claim 3**: "Even with best-in-class defenses,
    protection in the model layer will never be 100% effective, which is why it can't stand
    alone." The bypass permissions control is an environmental-layer governance mechanism —
    it constrains what the tool will automatically approve, regardless of model behavior.
    This corroborates the environmental-controls-first principle: when prompt injection can
    succeed 96% of the time (Claim 11 of that note), enterprise-level prevention of
    auto-approval is a meaningful environmental backstop.
  - **`blog-anthropic-how-contain-claude.md` Claim 6**: Claude Code required 93% of
    permission prompts to be approved by users before sandboxing — demonstrating approval
    fatigue. The Copilot bypass permissions mode produces the same failure mode: users in
    bypass mode never evaluate permissions at all. `disableBypassPermissionsMode` prevents
    organizations from deploying Copilot in this fatigue-prone state enterprise-wide.

- **Extends**:
  - **`docs-github-copilot-enterprise-managed-plugins-vscode.md`**: The June 5 note
    established enterprise-managed settings with two capability categories (plugin
    distribution and hooks/MCP governance). This June 17 source adds a third capability —
    bypass permissions mode control — to the same system and the same configuration file.
    The 12-day gap between announcements reveals fast-moving expansion of the enterprise
    governance surface: hooks → MCP → plugin distribution → permission prompt governance,
    all within two weeks.
  - **`docs-github-copilot-cca-rest-api-audit-config.md`**: That source documented
    REST API-based auditing of CCA security configuration at scale. This source documents
    settings-based control over permission behavior at the client level. Together they reveal
    GitHub building governance controls at multiple levels of the Copilot enterprise stack:
    API-based configuration audit (CCA scope) and settings-based permission governance
    (VS Code + CLI scope).
  - **`docs-github-copilot-cli-settings-command.md`**: The June 11 `/settings` command
    note documented the developer-facing self-service settings surface for individual
    Copilot CLI configuration. This note documents the administrator-facing enterprise
    governance layer. The two operate at different levels of the settings hierarchy:
    developer self-service settings (CLI `/settings` command) vs. enterprise-enforced
    policies (enterprise-managed settings file). The enterprise bypass permissions control
    operates at a layer the individual developer presumably cannot override via `/settings`.

- **Contradicts**: None identified. No existing corpus source makes a conflicting claim
  about enterprise permission governance for Copilot. No contradiction issue filed.

- **Novel**:
  - **`disableBypassPermissionsMode` as enterprise governance control**: No prior corpus
    source documents an enterprise-level control for preventing automatic permission
    approval in AI coding tools. This is the first documented enterprise mechanism for
    enforcing "no bypass mode" organization-wide in the corpus.
  - **"Bypass permissions mode" as a named Copilot behavior**: No prior corpus source
    explicitly names or documents a "bypass permissions mode" feature in Copilot CLI or
    VS Code. This note is the first corpus evidence that such a mode exists as a default
    or optional behavior in these tools.
  - **`copilot/managed-settings.json` as new preferred configuration path**: The new
    preferred configuration path is not mentioned in any prior source note. This represents
    a naming evolution in the enterprise-managed settings architecture.
  - **Agents page under AI controls** as verification surface for enterprise settings:
    No prior corpus source documents this administrative UI for verifying active enterprise
    Copilot settings. This is the first corpus evidence of a dedicated verification page
    for enterprise-managed Copilot governance.
  - **Enterprise capability expansion rate**: The 12-day gap between the June 5 plugin
    governance note and this June 17 bypass permissions note reveals unusually fast
    enterprise governance capability expansion. Practitioners relying on the June 5 note
    alone for enterprise settings coverage are already missing a new capability.

## Guide Impact

- **Chapter 02 (Harness Engineering — Enterprise Configuration)**:
  - Add `disableBypassPermissionsMode: "disable"` to the documented enterprise settings
    controls. Currently, based on `docs-github-copilot-enterprise-managed-plugins-vscode.md`,
    guide coverage includes plugin distribution and hooks/MCP. This adds a third concrete
    enterprise-managed control to document. The "Concrete Artifacts" capability map above
    is a suggested structure.
  - Update the documented configuration paths: add `copilot/managed-settings.json` as the
    new preferred path alongside the existing `.github-private/.github/copilot/settings.json`,
    with a note that both paths are valid for backward compatibility but the new path is
    preferred for new configurations.
  - Add the Agents page under AI controls as the verification mechanism for active enterprise
    settings — currently no verification path is documented in the guide.

- **Chapter 04/05 (Governance & Team Adoption — Enterprise Controls)**:
  - Add bypass permissions mode control as a concrete governance lever for enterprise
    Copilot deployments where auto-approval of permission prompts is a compliance or
    security concern. Frame alongside the hooks/MCP governance controls from June 5:
    enterprises now control both what tooling is always active (hooks/MCP enforcement) and
    whether automatic approval behavior is permitted.
  - Organizations in regulated industries or with strict security postures should evaluate
    `disableBypassPermissionsMode: "disable"` as a baseline control, particularly where
    developers work with sensitive repositories, credentials, or infrastructure automation.

- **Chapter 06/07 (Safety & Security / Enterprise Operations)**:
  - Add `disableBypassPermissionsMode` to the enterprise security hardening checklist for
    Copilot deployments. Reference `blog-anthropic-how-contain-claude.md` Claim 11 (96%
    phishing success rate on credential exfiltration via prompt injection) and Claim 6
    (93% permission approval rate in Claude Code before sandboxing) as empirical context:
    auto-approval behavior at the enterprise level creates a permission rubber-stamp dynamic
    that cannot defend against prompt injection.
  - Document the three-tier verification practice: (1) configure in enterprise settings file,
    (2) confirm via Agents page under AI controls, (3) test that bypass mode is disabled for
    a sample licensed user in both Copilot CLI and VS Code.

## Extraction Notes

1. **WebFetch AI-summarized content**: The WebFetch tool processes source HTML through an
   AI model before returning content. No portion of the returned text can be verified as
   character-for-character verbatim from the source without independent access to the raw
   HTML. All claims are marked as "(no direct verbatim quote; see paraphrase in Our
   assessment)" except for technical identifiers (`disableBypassPermissionsMode`, `"disable"`,
   specific file paths) which are high-confidence technical facts that are hard to misquote
   by summarization. The Assayer should spot-check all factual claims — especially the
   setting name, value, and configuration paths — against the live source URL.

2. **Short changelog (~300 words)**: Based on the changelog entry style of comparable
   GitHub Copilot changelogs in the corpus (the June 5 note was ~300 words), this is a
   brief product announcement. The 8 claims above are judged to represent the complete
   substantive scope of the source.

3. **"Bypass permissions mode" / "yolo mode" terminology**: The WebFetch summary used
   "yolo mode" informally. Whether this exact informal term appears verbatim in the source
   changelog or is the WebFetch AI's paraphrase is unknown. The formal term is "bypass
   permissions mode" (derived from the setting name `disableBypassPermissionsMode`);
   practitioners should verify the informal terminology against the live source URL.

4. **New preferred path `copilot/managed-settings.json`**: The WebFetch mentioned both
   old and new preferred paths. The path strings are reported with high confidence as
   technical identifiers, but the Assayer should verify these exact paths against the
   live source URL.

5. **No contradictions filed**: No existing corpus source makes conflicting claims about
   enterprise Copilot permission governance. The bypass permissions control is additive
   to the enterprise-managed settings system documented in June 5. No contradiction issue
   filed.

6. **May represent only partial coverage of June 17 changes**: The changelog title
   references "bypass permission controls" (plural). This note documents `disableBypassPermissionsMode`
   as the primary control; it is possible the changelog mentions additional controls or
   configuration options that were not surfaced in the WebFetch summary. Practitioners
   should read the source directly for complete coverage.
