---
source_url: https://github.blog/changelog/2026-11-16-control-where-github-copilot-customizations-come-from
source_type: docs
title: "Control where GitHub Copilot customizations come from"
author: GitHub (official changelog)
date_published: 2026-11-16
date_extracted: 2026-11-17
last_checked: 2026-11-17
status: current
confidence_overall: emerging
issue: "#4769"
---

# Control where GitHub Copilot customizations come from

> GitHub's Nov 16, 2026 changelog adds the `strictPluginOnlyCustomization` managed setting, which lets enterprise admins force skills, custom agents, hooks, MCP servers and executable extensions to arrive via plugins or managed settings rather than user/project config, while explicitly not acting as a marketplace allowlist.

## Source Context

- **Type**: docs (GitHub official changelog, category "Improvement", ~300 words, no author listed)
- **Author credibility**: GitHub product team; authoritative for the setting's name, scope and licensing. Not authoritative for enforcement mechanics, JSON schema, precedence with other policies, or behavior for already-configured items (the linked admin guide at docs.github.com, "managing plugin marketplaces and plugins with enterprise-managed settings", was not read).
- **Scope**: One governance control. No config example, version numbers, or metrics.

## Extracted Claims

### Claim 1: Admins can require selected Copilot customizations to come from plugins or managed settings instead of standalone user/project configuration
- **Evidence**: Official changelog statement; no example config.
- **Confidence**: emerging (vendor doc, thin)
- **Quote**: "you can now require selected GitHub Copilot customizations to come from plugins or managed settings, rather than standalone user or project configuration."
- **Our assessment**: Shifts the trust boundary from "whatever is in the repo/home directory" to "what the enterprise distributes". Directly addresses the threat of a cloned repo shipping its own hooks or MCP servers.

### Claim 2: The setting is `strictPluginOnlyCustomization`; it blocks user- and project-sourced standalone customizations while eligible plugins and managed settings stay allowed
- **Evidence**: Named setting in changelog.
- **Confidence**: emerging
- **Quote**: "The strictPluginOnlyCustomization managed setting blocks standalone customizations from user and project sources. Eligible plugins and managed settings remain allowed, subject to your other policies."
- **Our assessment**: "Subject to your other policies" means this composes with, rather than overrides, e.g. MCP allow/deny lists. Precedence is not specified.

### Claim 3: Restriction is per-category across five categories
- **Evidence**: Changelog lists categories and gives an example.
- **Confidence**: emerging
- **Quote**: "You can apply the restriction to all five supported categories or select individual ones: skills, custom agents, hooks, MCP servers, and executable Copilot extensions."
- **Our assessment**: Granularity allows staged rollout: lock the executable/high-risk categories (MCP servers, extensions) first and leave low-risk markdown ones (skills, agents) open. Hooks are arguably high-risk too (arbitrary commands), but the source's own example leaves them open.

### Claim 4: Example policy: restrict MCP servers and extensions, leave skills, agents, hooks open
- **Evidence**: Illustrative example in the changelog.
- **Confidence**: anecdotal (illustrative, not a recommendation backed by data)
- **Quote**: "For example, restrict MCP servers and extensions while leaving skills, agents, and hooks open."
- **Our assessment**: Useful as a vendor-suggested starting posture; we would not endorse leaving hooks open without justification.

### Claim 5: "Extensions" means executable canvas providers, not VS Code Marketplace extensions
- **Evidence**: Clarification in changelog.
- **Confidence**: emerging
- **Quote**: "Extensions here include executable canvas providers, not VS Code Marketplace extensions."
- **Our assessment**: Easy to misread; admins should not assume this governs VS Code extension installs.

### Claim 6: Plugin-only is not a marketplace allowlist; pair with `strictKnownMarketplaces`
- **Evidence**: Explicit caveat.
- **Confidence**: emerging
- **Quote**: "Plugin-only does not mean enterprise-managed plugins only, and it isn’t a marketplace allowlist. Pair it with strictKnownMarketplaces to restrict eligible marketplace sources."
- **Our assessment**: Key gotcha: used alone, any public marketplace plugin could still supply the blocked categories, moving rather than closing the supply-chain hole. Needs both settings for a real control.

### Claim 7: Goal is to keep MCP tools and canvases usable via a curated shared plugin library rather than disabling them
- **Evidence**: Stated motivation.
- **Confidence**: emerging
- **Quote**: "this lets you distribute approved MCP tools and canvases through a shared plugin library without disabling those capabilities entirely."
- **Our assessment**: Frames governance as "curate and distribute" rather than "ban", consistent with the earlier managed-plugins notes.

### Claim 8: Existing managed settings can supply marketplace definitions and require or block specific plugins
- **Evidence**: Changelog sentence.
- **Confidence**: emerging
- **Quote**: "Your existing managed settings can supply marketplace definitions and require or block specific plugins."
- **Our assessment**: Confirms this is a layer atop existing settings, not a new mechanism.

### Claim 9: Availability limited to GitHub Enterprise Cloud with Copilot Business/Enterprise licenses
- **Evidence**: Availability statement.
- **Confidence**: emerging
- **Quote**: "Enterprise administrators can configure these controls on GitHub Enterprise Cloud for members with Copilot Business or Copilot Enterprise licenses issued by the enterprise or one of its organizations."
- **Our assessment**: Individual/free-tier users are out of scope; the control is enterprise-only.

## Concrete Artifacts

No config snippets in the source. Only the setting names `strictPluginOnlyCustomization` and `strictKnownMarketplaces`, and the five category names: skills, custom agents, hooks, MCP servers, executable Copilot extensions. Linked admin guide: https://docs.github.com/enterprise-cloud@latest/copilot/how-tos/administer-copilot/manage-for-enterprise/use-managed-settings/manage-plugin-marketplaces-and-plugins (not read).

## Cross-References

- **Corroborates**: `docs-github-copilot-enterprise-strict-known-marketplaces.md` (Claim 2, whitelist marketplace restriction) — this note's Claim 6 depends on it.
- **Contradicts**: none found.
- **Extends**: `docs-github-copilot-enterprise-managed-plugins-vscode.md` (Claim 5, always-enabled hooks and MCP configs distributed via enterprise plugins; this adds the enforcement side, blocking non-plugin sources); `docs-github-copilot-mcp-allowlists-enterprise.md` (Claims 1 and 4: allow/deny lists gate which MCP servers may run; this gates where MCP config may originate, and the two compose); `docs-github-copilot-enterprise-managed-settings-enforcement-oct2026.md` and `docs-github-copilot-enterprise-team-specialization-managed-settings.md` (same managed-settings thread).
- **Novel**: `strictPluginOnlyCustomization`, per-category source restriction, and the explicit "not a marketplace allowlist" caveat; no prior note covers them.

## Guide Impact

- **Chapter 06 (security)**: Add source-of-origin control (plugin-only) as a distinct layer from allowlists (what may run) and marketplace restrictions (where plugins come from); recommend combining all three.
- **Chapter 05 (team adoption)**: Mention curated shared plugin library plus per-category lockdown as an enterprise rollout pattern.
- **Chapter 02 (harness)**: Note Copilot now has a policy separating standalone config from plugin-delivered config across the five customization categories.

## Extraction Notes

Read the full changelog page (fetched raw HTML; quotes copied from the page text). Short entry; the linked admin guide was not followed, so schema and precedence details are unknown. Confidence kept at emerging.
