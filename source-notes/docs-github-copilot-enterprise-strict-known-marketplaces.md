---
source_url: https://github.blog/changelog/2026-06-25-enterprise-managed-settings-now-support-strictknownmarketplaces-in-vs-code-and-the-cli
source_type: docs
title: "Enterprise-managed settings now support strictKnownMarketplaces in VS Code and GitHub Copilot CLI"
author: GitHub (official changelog)
date_published: 2026-06-25
date_extracted: 2026-06-26
last_checked: 2026-06-26
status: current
confidence_overall: emerging
issue: "#1318"
---

# Enterprise-Managed Settings Now Support strictKnownMarketplaces in VS Code and GitHub Copilot CLI

> GitHub's June 25, 2026 changelog extends the enterprise-managed settings system with a
> `strictKnownMarketplaces` control that restricts Copilot plugin installation in VS Code and
> Copilot CLI to only those marketplaces explicitly defined by enterprise administrators —
> a whitelist-based marketplace restriction that adds a supply-chain governance layer to
> the same configuration system as the June 5 plugin distribution controls and the June 17
> bypass permissions control.

## Source Context

- **Type**: docs (GitHub official product changelog, June 25, 2026; approximately 150 words)
- **Author credibility**: GitHub engineering team announcing a new enterprise governance feature
  in public preview. Authoritative for: the existence and name of the `strictKnownMarketplaces`
  setting, what it does at a high level (restrict plugin installation to explicitly defined
  marketplaces), which clients it applies to (VS Code and Copilot CLI), the license requirement
  (Copilot Business or Copilot Enterprise), and the auto-application mechanism. The linked
  documentation at https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/configure-enterprise-plugin-standards
  provides the JSON schema with supported marketplace source types. Not authoritative for: how
  enforcement works at the technical level (client-side or server-side), behavior for
  already-installed plugins when the setting is first activated, or the complete list of
  enterprise-managed settings available.
- **Scope**: A single new governance control (`strictKnownMarketplaces`) in the enterprise-managed
  settings system. Covers: what the setting does, license requirements, which clients it applies to,
  the JSON schema and supported marketplace source types (`"github"` and `"git"`), and the
  enforcement timing model (next authentication). Does NOT cover: technical enforcement details,
  behavior for plugins installed before the setting is activated, the complete settings schema,
  or operational impact of restricting available marketplaces.

## Extracted Claims

### Claim 1: Enterprises can now control which plugins their users can install in GitHub Copilot CLI and VS Code using a new `strictKnownMarketplaces` setting in the enterprise-managed settings.json

- **Evidence**: Official GitHub changelog announcement. The statement "Enterprises can now control
  which plugins their users can install in GitHub Copilot CLI and VS Code" is the lead sentence
  of the changelog body, directly followed by the in-public-preview status.
- **Confidence**: settled (product fact in official changelog; feature exists and is in public preview)
- **Quote**: "Enterprises can now control which plugins their users can install in GitHub Copilot CLI and VS Code. This setting is now available in public preview."
- **Our assessment**: This closes a governance gap in the enterprise-managed plugins system documented
  in `docs-github-copilot-enterprise-managed-plugins-vscode.md`. The June 5 note established that
  enterprises could define plugin marketplaces and auto-install plugins, but did not address
  restricting which marketplaces users could install from. This new setting adds the whitelist
  control: the administrator defines the allowed marketplace list, and Copilot enforces it. For Ch02
  (Harness Engineering): add `strictKnownMarketplaces` to the enterprise settings schema documentation
  alongside `disableBypassPermissionsMode`.

### Claim 2: The `strictKnownMarketplaces` setting restricts Copilot to only allowing plugin installations from marketplaces explicitly defined by the enterprise — a whitelist-based marketplace restriction

- **Evidence**: Official changelog body: "Add `strictKnownMarketplaces` to your enterprise-managed
  `settings.json`, and Copilot will only allow plugins to be installed from the marketplaces
  you've explicitly defined." The phrase "only allow" signals whitelist (allowlist) semantics —
  everything not listed is blocked.
- **Confidence**: settled (whitelist semantics directly stated in official changelog)
- **Quote**: "Add `strictKnownMarketplaces` to your enterprise-managed `settings.json`, and Copilot will only allow plugins to be installed from the marketplaces you've explicitly defined."
- **Our assessment**: The whitelist model is architecturally stronger than a blacklist approach.
  A whitelist-based restriction means the default when this setting is applied becomes "deny all not
  explicitly permitted." Organizations that want to restrict users to only company-approved plugin
  sources should use `strictKnownMarketplaces` with entries for each allowed marketplace. For Ch02:
  document this explicitly as a whitelist-based control to distinguish it from a blocklist approach.

### Claim 3: GitHub frames `strictKnownMarketplaces` as a supply-chain governance control that operates "prior to tool execution" — at install time, not at runtime

- **Evidence**: Official changelog: "This is a direct way to enforce your client governance strategy
  prior to tool execution by removing the risk of users installing untrusted plugins."
- **Confidence**: settled (verbatim from official changelog; GitHub's own framing of the control)
- **Quote**: "This is a direct way to enforce your client governance strategy prior to tool execution by removing the risk of users installing untrusted plugins."
- **Our assessment**: The phrase "prior to tool execution" is the key security signal: this control
  operates at install time, not at runtime. The restriction prevents installation of untrusted plugins
  in the first place, rather than monitoring or blocking behavior of installed plugins when they run.
  This is a supply-chain-level control: it governs what can be installed, not what installed tools
  do. For Ch06/07 (Safety & Security): frame `strictKnownMarketplaces` as a supply-chain control
  in the AI tooling governance stack, distinct from the runtime permission controls documented in
  `docs-github-copilot-enterprise-bypass-permissions.md` (`disableBypassPermissionsMode`).

### Claim 4: The `strictKnownMarketplaces` schema supports two marketplace source types: GitHub-hosted repositories (`source: "github"` with `repo: "OWNER/REPO"`) and external Git repositories (`source: "git"` with a `url` parameter)

- **Evidence**: Documentation at the linked URL (https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/configure-enterprise-plugin-standards)
  states `strictKnownMarketplaces` "restricts plugin installation to only the marketplaces
  explicitly defined by the enterprise" and provides the JSON schema with two source types.
- **Confidence**: emerging (from secondary documentation, not the changelog itself; schema may
  evolve during public preview)
- **Quote**: (no direct verbatim quote from the changelog itself; schema extracted from linked documentation — see Concrete Artifacts for the JSON structure)
- **Our assessment**: Supporting both GitHub-hosted repos and external Git repositories is practically
  significant. The `"github"` source type allows enterprises to use internal private GitHub repositories
  as approved marketplaces (useful for proprietary plugins). The `"git"` source type allows enterprises
  that host plugin artifacts outside GitHub to include those sources. For enterprises not yet fully
  on GitHub for all tooling, the `"git"` source type provides flexibility. The Assayer should verify
  the exact schema against the live documentation URL, as schema details may change during preview.

### Claim 5: The `strictKnownMarketplaces` settings automatically apply to users licensed through Copilot Business or Copilot Enterprise accounts across both Copilot CLI and VS Code

- **Evidence**: Official changelog: "GitHub Copilot automatically pulls and applies these settings
  for users licensed through your Copilot Business or Copilot Enterprise account."
- **Confidence**: settled (license requirement and auto-application mechanism stated explicitly in
  official changelog; consistent with June 5 and June 17 enterprise settings notes)
- **Quote**: "GitHub Copilot automatically pulls and applies these settings for users licensed through your Copilot Business or Copilot Enterprise account."
- **Our assessment**: Auto-application is the enforcement model: administrators configure the setting
  in the enterprise settings file, and it propagates automatically to all licensed users' clients
  without requiring individual user action or developer-side configuration. This is consistent with
  the architecture documented in `docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 2.
  The license gate (Business or Enterprise) is unchanged from the June 5 and June 17 enterprise
  settings features — organizations on individual or team-tier Copilot plans cannot use this control.

### Claim 6: Settings take effect the next time licensed users authenticate from a supported client, creating a potential lag between administrative configuration and full enforcement

- **Evidence**: Documentation states settings apply "the next time they authenticate from a
  supported client." This authentication-cycle model is consistent with how enterprise-managed
  settings propagate.
- **Confidence**: emerging (from secondary documentation, not the changelog; mechanism may change
  before GA)
- **Quote**: (no direct verbatim quote from changelog; from linked documentation — "the next time they authenticate from a supported client")
- **Our assessment**: The authentication-cycle application model means there may be a lag between when
  an administrator updates the enterprise settings and when all users have the new restrictions
  enforced. Users who were already authenticated may continue installing from any marketplace until
  their next authentication event. For Ch02: document this timing characteristic. Enterprise
  administrators rolling out `strictKnownMarketplaces` should communicate to users to re-authenticate
  (sign out and sign in) to receive the new restrictions immediately.

### Claim 7: `strictKnownMarketplaces` is explicitly described as building on earlier enterprise-managed plugin capabilities for Copilot CLI and VS Code, positioning it as an incremental governance extension rather than a new architectural feature

- **Evidence**: Official changelog: "This update builds on the enterprise-managed plugins for
  Copilot CLI and VS Code capabilities we launched earlier."
- **Confidence**: settled (verbatim from official changelog)
- **Quote**: "This update builds on the enterprise-managed plugins for Copilot CLI and VS Code capabilities we launched earlier."
- **Our assessment**: This explicitly positions `strictKnownMarketplaces` as the third enterprise
  governance control added to the same system in 20 days (June 5 → plugin distribution + hooks/MCP,
  June 17 → bypass permissions, June 25 → marketplace restriction). For organizations that have
  already set up the enterprise-managed settings infrastructure, adding `strictKnownMarketplaces`
  requires only adding a new key to the existing settings file — no new infrastructure. The pace
  of capability addition (3 governance additions in 20 days) signals GitHub is rapidly building out
  this enterprise governance surface.

### Claim 8: The feature is categorized as an "Improvement" in the GitHub changelog — an incremental addition to existing infrastructure, not a new feature requiring new setup

- **Evidence**: The GitHub changelog page categorizes this entry as "Improvement" in the page
  metadata/tag section.
- **Confidence**: settled (classification from the changelog page itself)
- **Quote**: (the "Improvement" label appears in the page's categorical tag, not in the body
  text — not a verbatim prose quote but a direct page-level classification)
- **Our assessment**: The "Improvement" classification confirms this extends existing infrastructure.
  Unlike the June 5 note (which introduced the entire enterprise-managed plugins framework), this note
  is incrementally additive. Organizations that have already configured the enterprise-managed settings
  infrastructure (`.github-private/.github/copilot/settings.json` or `copilot/managed-settings.json`)
  can add `strictKnownMarketplaces` with no new repository or infrastructure setup. For Ch02: document
  this control alongside the existing capability map rather than in a new section.

## Concrete Artifacts

### strictKnownMarketplaces Configuration Schema (from linked documentation)

```json
// Location: .github-private/.github/copilot/settings.json
// OR new preferred path: copilot/managed-settings.json
// (per docs-github-copilot-enterprise-bypass-permissions.md Claim 4)

{
  "strictKnownMarketplaces": [
    {
      "source": "github",
      "repo": "OWNER/REPO"
    }
  ]
}

// Marketplace source types:
//   "github" — GitHub-hosted repository marketplace
//              Required: repo: "OWNER/REPO"
//   "git"    — External Git repository marketplace
//              Required: url: "<git-repo-url>"

// Effect:    Copilot will only allow plugin installations from listed marketplaces
// Scope:     All Copilot Business or Copilot Enterprise licensed users
// Clients:   GitHub Copilot CLI and VS Code
// Status:    Public preview as of June 25, 2026
// Enforcement: Applied on next client authentication
```

*Source: GitHub Copilot changelog (June 25, 2026) and linked documentation at
https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/configure-enterprise-plugin-standards.
The JSON schema is extracted from the linked documentation via WebFetch. Verify exact schema format
against the live documentation URL before production use.*

### Enterprise-Managed Settings Capability Map (as of June 25, 2026)

```
Configuration file: .github-private/.github/copilot/settings.json
New preferred path: copilot/managed-settings.json
License required:   Copilot Business or Copilot Enterprise
Client versions:    VS Code 1.122+ and Copilot CLI
Enforcement:        Applied on next client authentication

Capabilities announced as of June 25, 2026:

1. Plugin distribution (June 5, 2026)
   - Define plugin marketplaces
   - Auto-install custom agents and skills
   - Source: docs-github-copilot-enterprise-managed-plugins-vscode.md

2. Governance controls (June 5, 2026)
   - Hooks "always enabled" across the enterprise
   - MCP configurations "always enabled"
   - Source: docs-github-copilot-enterprise-managed-plugins-vscode.md

3. Bypass permissions control (June 17, 2026)
   - disableBypassPermissionsMode: "disable"
   - Prevents automatic approval of permission prompts
   - Source: docs-github-copilot-enterprise-bypass-permissions.md

4. Marketplace restriction (June 25, 2026) ← THIS NOTE
   - strictKnownMarketplaces: [{ source, repo/url }, ...]
   - Restricts plugin installation to explicitly defined marketplaces only
   - Supply-chain governance: operates at install time, not runtime
   - Source: docs-github-copilot-enterprise-strict-known-marketplaces.md
```

*Source: GitHub Copilot changelogs, June 5, June 17, and June 25, 2026*

### Two-Layer Enterprise Plugin Governance Pattern

```
Layer 1 — Install-time restriction (supply-chain control):
  strictKnownMarketplaces: [...]
  Controls: Which marketplaces users can install plugins FROM
  Threat addressed: Untrusted plugin sources / supply-chain risk
  Timing: Enforced at plugin install time

Layer 2 — Runtime permission restriction:
  disableBypassPermissionsMode: "disable"
  Controls: Whether Copilot auto-approves permission prompts from installed plugins
  Threat addressed: Auto-approval rubber-stamp behavior / prompt injection exploitation
  Timing: Enforced at permission prompt time during tool execution

Combined effect: restricts what plugins can be installed AND enforces human
review of what installed plugins are permitted to do at runtime.
```

*Source: synthesis across docs-github-copilot-enterprise-bypass-permissions.md and this note*

## Cross-References

- **Corroborates**:
  - **`docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 2**: "The baseline standards
    you set for your enterprise apply to every user's Copilot CLI and VS Code clients." The dual-client
    enforcement architecture established June 5 is confirmed and extended. `strictKnownMarketplaces`
    uses the same automatic propagation mechanism across both clients.
  - **`docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 3**: Configuration at
    `.github-private/.github/copilot/settings.json` is reaffirmed as the central enterprise
    governance file. The new preferred path `copilot/managed-settings.json` (per
    `docs-github-copilot-enterprise-bypass-permissions.md` Claim 4) also applies here.
  - **`docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 6**: License requirement
    (Copilot Business or Copilot Enterprise) is consistent across all three enterprise-managed
    settings notes in the corpus.
  - **`docs-github-copilot-enterprise-bypass-permissions.md` Claim 1**: The pattern of adding
    specific named controls (`disableBypassPermissionsMode`, now `strictKnownMarketplaces`) to the
    enterprise-managed settings system is confirmed. Both controls follow the same architecture:
    named key in `settings.json`, applied automatically to both Copilot CLI and VS Code for licensed
    users.

- **Contradicts**: None identified. No existing corpus source makes a conflicting claim about
  enterprise marketplace restrictions. The June 5 note's ability to "define plugin marketplaces"
  and this note's ability to "restrict installations to defined marketplaces" are complementary
  layers, not opposing claims. No contradiction issue filed.

- **Extends**:
  - **`docs-github-copilot-enterprise-managed-plugins-vscode.md`**: The June 5 note established
    that enterprises can define marketplaces and distribute plugins. This note adds the enforcement
    layer: with `strictKnownMarketplaces`, defined marketplaces are not merely advisory — only
    plugins from explicitly listed marketplaces can be installed. Together, these two notes define
    the complete enterprise marketplace governance story: distribution (June 5) + restriction
    (June 25).
  - **`docs-github-copilot-enterprise-bypass-permissions.md`**: The June 17 note added
    `disableBypassPermissionsMode` as the second named control in the enterprise-managed settings
    system. This note adds `strictKnownMarketplaces` as the third, completing a two-layer
    plugin governance architecture: install-time restriction (this note) + runtime permission
    restriction (June 17 note). The "Concrete Artifacts → Two-Layer Enterprise Plugin Governance
    Pattern" section above synthesizes the two controls.

- **Novel**:
  - **Whitelist-based marketplace restriction as enterprise governance**: No prior corpus source
    documents an enterprise control that restricts which plugin marketplaces users can install
    from. The June 5 note describes marketplace *definition* (administrators can specify sources
    for distribution); this note adds marketplace *restriction* (only listed sources are permitted
    for any installation). The architectural distinction between distribution and restriction
    is new to the corpus.
  - **Dual marketplace source types**: No prior corpus source documents that enterprise-managed
    Copilot settings support both GitHub-hosted repositories (`"github"`) and arbitrary external
    Git repositories (`"git"`) as plugin marketplace source types. This is the first corpus
    documentation of non-GitHub marketplace sources in the enterprise Copilot governance system.
  - **Authentication-cycle enforcement timing**: No prior corpus source explicitly documents the
    latency model for enterprise-managed settings propagation ("the next time they authenticate
    from a supported client"). This is the first corpus documentation of the timing model for
    enterprise settings changes taking effect.
  - **Supply-chain framing of enterprise Copilot governance**: No prior corpus source explicitly
    frames enterprise Copilot governance as a supply-chain control ("prior to tool execution by
    removing the risk of users installing untrusted plugins"). This GitHub framing positions the
    enterprise-managed settings system as a supply-chain security mechanism, distinct from runtime
    behavioral controls. This framing is novel in the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering — Enterprise Configuration)**:
  - Add `strictKnownMarketplaces` to the documented enterprise settings controls. The "Concrete
    Artifacts → Enterprise-Managed Settings Capability Map" above provides a complete picture of
    all four capabilities (as of June 25, 2026) and is the suggested structure for Ch02 coverage.
  - Clarify the distinction between marketplace *definition* (June 5, for auto-install distribution)
    and marketplace *restriction* (June 25, for enforcing install-time supply-chain governance).
    Both capabilities exist in the same settings file; they serve complementary purposes.
  - Add the authentication-cycle enforcement timing note. Administrators should communicate to
    users to re-authenticate after enterprise settings changes to ensure immediate enforcement.
  - The "Concrete Artifacts → Two-Layer Enterprise Plugin Governance Pattern" section above is a
    suggested structure for documenting the interaction of `strictKnownMarketplaces` and
    `disableBypassPermissionsMode` as complementary controls addressing different threat vectors.

- **Chapter 04/05 (Governance & Team Adoption — Enterprise Controls)**:
  - Add `strictKnownMarketplaces` as the fourth enterprise governance control. Frame it alongside
    the earlier three (plugin distribution, hooks/MCP enforcement, bypass permissions) as a growing
    enterprise AI tooling governance stack with four concrete configuration points.
  - Organizations with security or compliance requirements around third-party tooling should
    evaluate `strictKnownMarketplaces` as a mandatory control for Copilot deployments. The
    whitelist model (only explicitly listed marketplaces permitted) is the appropriate posture
    for regulated environments where any untrusted plugin installation is a compliance issue.

- **Chapter 06/07 (Safety & Security / Enterprise Operations)**:
  - Add `strictKnownMarketplaces` to the enterprise security hardening checklist for Copilot
    deployments, framed as a supply-chain control that prevents installation of untrusted plugins
    before they can execute. Position it as the install-time complement to the runtime permission
    control (`disableBypassPermissionsMode`).
  - The two-layer governance pattern (install restriction + runtime permission restriction) is a
    concrete security architecture recommendation: enterprises should implement both controls to
    address two distinct threat vectors (untrusted plugin sources and auto-approval behavior).

## Extraction Notes

1. **Short changelog (~150 words)**: This is the shortest of the three enterprise-managed settings
   changelogs in the corpus. The body text is 4 sentences. All substantive content was exhausted
   in 8 claims above. The linked documentation page provided additional schema detail that was
   separately fetched via WebFetch.

2. **WebFetch verbatim accuracy**: Two independent WebFetch calls to the changelog URL returned
   consistent text. Quotes in Claims 1, 2, 3, 5, and 7 are verbatim from the WebFetch output.
   The Assayer should verify these quotes against the live source URL. Technical identifiers
   (`strictKnownMarketplaces`, `"github"`, `"git"`, `OWNER/REPO`) are treated as high-confidence
   technical facts unlikely to be misrepresented by WebFetch summarization.

3. **JSON schema from linked documentation**: The `strictKnownMarketplaces` JSON schema was
   extracted from the linked documentation page, not from the changelog itself. The changelog
   does not include a code example — it only names the setting and describes its effect. The
   Assayer should verify the exact schema format against the documentation URL, as schema details
   may change during public preview.

4. **Configuration path inferred from consistency**: The changelog body text says "enterprise-managed
   `settings.json`" without specifying the full path. The full paths (`.github-private/.github/copilot/settings.json`
   and the newer preferred `copilot/managed-settings.json`) are inferred from consistency with the
   June 5 and June 17 enterprise-managed settings notes. The linked documentation should confirm
   the applicable path.

5. **Public preview status**: This feature is in public preview as of June 25, 2026. Schema
   details and behavior may change before GA. Claims 4 and 6 are rated "emerging" to reflect
   preview status. Claims about basic functionality (what the setting does, license requirement)
   are rated "settled" as these are product-level facts unlikely to change at GA.

6. **No contradictions filed**: No existing corpus source makes conflicting claims about enterprise
   Copilot marketplace restrictions. The enterprise-managed plugins June 5 note's marketplace
   definition capability and this note's marketplace restriction capability are complementary
   controls, not contradictory positions. No contradiction issue filed.
