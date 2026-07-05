---
source_url: https://github.blog/changelog/2026-07-01-enterprises-can-default-to-auto-model-selection
source_type: docs
title: "Enterprises can default to auto model selection"
author: GitHub (official changelog)
date_published: 2026-07-01
date_extracted: 2026-07-05
last_checked: 2026-07-05
status: current
confidence_overall: settled
issue: "#1542"
---

# Enterprises Can Default to Auto Model Selection

> GitHub's July 1, 2026 changelog adds a `model: auto` permission to the enterprise
> `managed-settings.json` schema, letting enterprise administrators set Copilot auto
> model selection as the organization-wide default for new conversations while
> preserving per-conversation user override — a new admin-side governance lever that
> sits alongside (not on top of) the CCA-specific and Free/Student-specific auto
> features already in the corpus.

## Source Context

- **Type**: docs (GitHub official product changelog, July 1, 2026; ~150 words of primary
  announcement text, tagged "Improvement", 1-minute read). Followed one linked
  documentation page per MINER.md §1: "managed-settings.json permissions"
  (`docs.github.com/.../configure-enterprise-managed-settings`), which supplied the
  JSON schema example. Also checked the linked GitHub Community discussion
  (`orgs/community/discussions/199139`), which turned out to be the general
  enterprise-managed-settings discussion thread (covering plugin marketplaces and
  bypass-permissions bugs) rather than a thread specific to this auto-default feature.
- **Author credibility**: GitHub engineering team announcing a production feature
  change to the enterprise-managed settings system. Authoritative for: the existence
  of the `model` permission key, its accepted value, the configuration file paths,
  the license/client-version requirements, and the interaction with the existing
  `.github-private` source-organization mechanism. Not a credible source for: whether
  the enterprise default interacts with CCA auto (issue #745) or Free/Student auto-only
  (issue #1305) routing heuristics, whether the default can be scoped per-organization
  (as targeted model rules can, issue #957), or any usage/adoption data.
- **Scope**: A single new permission (`model: auto`) in the enterprise `managed-settings.json`
  schema, scoped to Copilot Business and Copilot Enterprise licensed users. Covers:
  the configuration key and value, file paths (new and legacy), client version
  requirement, reuse of the existing custom-agent source-org mechanism, and the
  admin verification path. Does NOT cover: whether individual organizations within
  the enterprise can opt out of the default, how this default composes with targeted
  model rules (issue #957) or per-org "Optional"/"Enabled" model availability, which
  specific models are in the resulting auto pool, or whether this changes the routing
  heuristic itself (it does not — it only sets which mode a new conversation starts in).

## Extracted Claims

### Claim 1: Enterprise administrators can set `model` to `auto` in `managed-settings.json` to make Copilot auto model selection the default for new conversations

- **Evidence**: Official GitHub changelog, direct statement of the feature.
- **Confidence**: settled (product fact stated in official changelog)
- **Quote**: "Enterprise administrators can now set `model` to `auto` in the enterprise
  `managed-settings.json` to make Copilot auto model selection the default for new
  conversations."
- **Our assessment**: This is a distinct governance layer from the auto-routing
  features already in the corpus. `docs-github-copilot-cca-auto-model-selection.md`
  (issue #745) and `docs-github-copilot-cli-auto-model-selection.md` (issue #203)
  document auto as a per-surface *option* a user opts into; `docs-github-copilot-free-student-auto-only-model-selection.md`
  (issue #1305) documents auto as a *mandatory, sole* mode for a plan tier. This
  source adds a third pattern: auto as an enterprise-configured *default* for
  Business/Enterprise users, who retain the ability to opt out per conversation
  (see Claim 2). For Ch05: the guide's auto-model-selection surface map needs a new
  row — "enterprise default" — distinct from "mandatory" (Free/Student) and
  "opt-in" (CCA, CLI, VS Code as documented in issues #745, #203, #844).

### Claim 2: Users can still switch to a different model on a per-conversation basis even when the enterprise default is set to auto

- **Evidence**: Official changelog, stated directly as a qualifier immediately following
  the configuration instructions.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Users can still switch to a different model on a per-conversation basis."
- **Our assessment**: This is the key distinction from the Free/Student auto-only
  policy (issue #1305, Claim 1: "the default and only model selection experience...
  manual model selection is fully removed"). The enterprise default documented here
  changes the *starting point* of a new conversation, not the *availability* of manual
  selection. An enterprise that sets `model: auto` is nudging behavior, not removing a
  capability — architecturally closer to a changed default value than to a policy
  restriction. For Ch02: this is not equivalent to the targeted-model-rules governance
  primitive (issue #957) or to Free/Student's picker removal; it should be documented
  as a "soft default," and guide advice should not conflate it with the harder
  restrictions in those two sources.

### Claim 3: The setting is configured by adding `auto` to `.github-private/.github/copilot/managed-settings.json` in the enterprise's source organization

- **Evidence**: Official changelog, direct statement of the configuration path and
  mechanism.
- **Confidence**: settled (configuration path stated in official changelog)
- **Quote**: "Add `auto` to `.github-private/.github/copilot/managed-settings.json`
  in your source organization for enterprise governance so new conversations start
  with Copilot auto model selection by default."
- **Our assessment**: This confirms the `.github-private` source-organization
  mechanism — already documented for plugin distribution and hooks/MCP governance
  (`docs-github-copilot-enterprise-managed-plugins-vscode.md`) and for
  `disableBypassPermissionsMode` (`docs-github-copilot-enterprise-bypass-permissions.md`,
  issue #1219) — is the same file used for model-selection defaults. For Ch02: the
  `.github-private/.github/copilot/managed-settings.json` file continues to grow
  as the single enterprise-wide Copilot configuration surface; this is now its
  fourth documented capability category (plugin distribution, hooks/MCP enforcement,
  bypass-permissions control, and now model-selection default).

### Claim 4: The `model: auto` permission requires VS Code 1.126+

- **Evidence**: Official changelog, stated in the "Backward Compatibility" section.
- **Confidence**: settled (version requirement stated in official changelog)
- **Quote**: "The `model` permission is available in VS Code 1.126+"
- **Our assessment**: This is a newer version floor than the VS Code 1.122+
  requirement documented for the June 5 plugin-governance feature and the June 17
  `disableBypassPermissionsMode` control (`docs-github-copilot-enterprise-bypass-permissions.md`,
  Claim 5). Enterprises that standardized on VS Code 1.122–1.125 for those earlier
  enterprise-managed-settings features will need a further client update before the
  model-selection default takes effect. For Ch02: the guide's enterprise-managed-settings
  client-version table should track per-permission-key minimum versions rather than
  a single "1.122+" floor for the whole file — this source shows the floor has already
  moved for at least one key.

### Claim 5: GitHub Copilot automatically pulls and applies these settings for users licensed through the enterprise account with Copilot Business or Copilot Enterprise

- **Evidence**: Official changelog, direct statement of license scope and application
  mechanism.
- **Confidence**: settled (stated in official changelog)
- **Quote**: "GitHub Copilot automatically pulls and applies these settings for users
  licensed through your enterprise account with Copilot Business or Copilot Enterprise."
- **Our assessment**: Consistent with the license gate already documented for every
  other enterprise-managed-settings capability in the corpus (plugin distribution,
  bypass-permissions control, targeted model rules — issue #957, Claim 5). This
  reconfirms that Copilot Business/Enterprise remains the single license floor for
  the entire enterprise-managed-settings system; no new licensing tier or add-on is
  introduced for the model-default capability specifically.

### Claim 6: The supported configuration path is `copilot/managed-settings.json`, with backward compatibility maintained for `.github/copilot/settings.json`

- **Evidence**: Official changelog, "Backward Compatibility" section.
- **Confidence**: settled (stated in official changelog)
- **Quote**: "The supported path for AI standards is copilot/managed-settings.json,
  with backward compatibility for `.github/copilot/settings.json`."
- **Our assessment**: This corroborates `docs-github-copilot-enterprise-bypass-permissions.md`
  Claim 4, which documented the same path migration (new preferred
  `copilot/managed-settings.json`, legacy `.github/copilot/settings.json` retained
  for compatibility) as of June 17. This July 1 source confirms the migration is
  still the current state six weeks later and that new capabilities (model default)
  are being added to the new path rather than reviving the legacy one. For Ch02:
  the guide should cite `copilot/managed-settings.json` as the canonical path name
  going forward, noting the legacy path only as a compatibility fallback for
  enterprises that have not yet migrated.

### Claim 7: If a source organization for custom agents is already configured, the model-default setting reuses that same `.github-private` repository, verifiable via the Agents page under AI controls

- **Evidence**: Official changelog, direct statement.
- **Confidence**: settled (stated in official changelog)
- **Quote**: "If you've already configured a source organization for custom agents,
  this setting uses that same `.github-private` repository. You can confirm that
  your configuration is active on the Agents page under AI controls in your
  enterprise settings."
- **Our assessment**: This matches the reuse pattern and verification path already
  documented in `docs-github-copilot-enterprise-bypass-permissions.md` (Claims 6 and 7:
  reuse of the existing `.github-private` repo, verification via the Agents page
  under AI controls). No new verification mechanism is introduced; this confirms
  the Agents page is the durable, general-purpose verification surface for all
  enterprise-managed-settings capabilities added so far, not a one-off for the
  bypass-permissions feature specifically.

### Claim 8: The `model` permission is nested under a `permissions` object in the `managed-settings.json` schema, alongside `disableBypassPermissionsMode`

- **Evidence**: The linked "managed-settings.json permissions" documentation page
  (followed per MINER.md §1) shows a JSON example with both keys under the same
  `permissions` object.
- **Confidence**: emerging (schema structure from a linked docs page fetched via
  AI-summarizing WebFetch, not the changelog itself — see Extraction Notes)
- **Quote**: (no direct quote from the changelog; the JSON structure is reproduced
  as a Concrete Artifact below, sourced from the linked documentation page rather
  than character-verified against raw HTML)
- **Our assessment**: This confirms `model` and `disableBypassPermissionsMode`
  (issue #1219) are sibling keys in one growing `permissions` schema within
  `managed-settings.json`, rather than separate top-level settings files. For Ch02:
  document `managed-settings.json`'s `permissions` object as the unified schema
  location for enterprise Copilot behavioral controls, expecting further keys to be
  added here rather than in new files.

### Claim 9: In Copilot CLI, new sessions default to Auto unless the user manually specifies otherwise; in VS Code, the model picker defaults to Auto when starting conversations

- **Evidence**: The linked "managed-settings.json permissions" documentation page
  describes the per-client effect of the setting.
- **Confidence**: emerging (from linked docs page via AI-summarizing WebFetch, not
  independently character-verified; see Extraction Notes)
- **Quote**: (no direct quote; see paraphrase above and in Concrete Artifacts)
- **Our assessment**: This clarifies that the enterprise default applies uniformly
  across both Copilot CLI and VS Code — consistent with the dual-client enforcement
  architecture already established for other enterprise-managed-settings capabilities
  (`docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 2; corroborated
  again in `docs-github-copilot-enterprise-bypass-permissions.md` Claim 2). No
  client-specific carve-out is documented — an enterprise that sets the default gets
  it applied consistently regardless of which Copilot surface a licensed user opens.

### Claim 10: A GitHub staff engineer, responding in the linked Community discussion, confirmed that `disableBypassPermissionsMode` interacts with autopilot behavior in the latest VS Code

- **Evidence**: GitHub Community discussion #199139 (linked from the changelog's
  "Join the discussion" link), staff reply from user `joshspicer`. This discussion
  thread is the general enterprise-managed-settings discussion (covering plugin
  marketplace and bypass-permissions questions), not one scoped specifically to the
  auto-default feature in this changelog — flagged as a scope caveat.
- **Confidence**: anecdotal (a single staff forum reply, not first-party documentation;
  and tangential to this changelog's specific feature)
- **Quote**: "With `permissions.disableBypassPermissionsMode` appropriately set, I
  would expect in the latest VS Code for auto-pilot to be disabled."
- **Our assessment**: This is not directly about the `model: auto` default, but it
  corroborates `docs-github-copilot-enterprise-bypass-permissions.md`'s claim that
  `disableBypassPermissionsMode` is a `permissions`-object key with real enforcement
  in VS Code, and it independently confirms VS Code 1.126.0 as the version where a
  related enterprise-managed-settings bug (autopilot permission bypass not fully
  disabled) was fixed — the same version floor this changelog states for the
  `model` permission (Claim 4). This is circumstantial but suggests VS Code 1.126
  was a release that hardened enterprise-managed-settings enforcement broadly, not
  just for the model-default feature specifically. Not high-value enough to change
  guide recommendations on its own; included for corpus completeness.

## Concrete Artifacts

### `managed-settings.json` — model default (from changelog + linked docs page)

```json
{
  "permissions": {
    "disableBypassPermissionsMode": "disable",
    "model": "auto"
  }
}
```
Source: GitHub changelog (July 1, 2026) for the `model` key's existence/value;
linked docs page "managed-settings.json permissions" for the surrounding JSON
structure and the `disableBypassPermissionsMode` sibling key (this file's schema
was AI-summarized by WebFetch, not raw-HTML-verified — see Extraction Notes).

### Enterprise-Managed Settings Capability Map (updated to July 1, 2026)

```
Configuration file: .github-private/.github/copilot/managed-settings.json
Legacy path (compat): .github/copilot/settings.json
License required:     Copilot Business or Copilot Enterprise

Capabilities announced to date:
1. Plugin distribution (June 5, 2026) — VS Code 1.122+
   Source: docs-github-copilot-enterprise-managed-plugins-vscode.md
2. Hooks/MCP "always enabled" governance (June 5, 2026) — VS Code 1.122+
   Source: docs-github-copilot-enterprise-managed-plugins-vscode.md
3. disableBypassPermissionsMode (June 17, 2026) — VS Code 1.122+
   Source: docs-github-copilot-enterprise-bypass-permissions.md
4. model: auto default (July 1, 2026) — VS Code 1.126+  ← THIS NOTE
   Source: docs-github-copilot-enterprise-auto-model-default.md

Verification path (all capabilities): Agents page → AI controls →
  GitHub Enterprise settings
```
Source: GitHub Copilot changelogs, June 5 / June 17 / July 1, 2026.

## Cross-References

- **Corroborates** `docs-github-copilot-enterprise-bypass-permissions.md` (issue
  #1219, Claims 3, 4, 6, 7): Same `.github-private/.github/copilot/managed-settings.json`
  file, same legacy-path backward-compatibility note (`.github/copilot/settings.json`),
  same reuse of an existing custom-agent source organization, and same Agents-page
  verification path. This source reconfirms all four mechanics six weeks later and
  adds a fourth capability to the same file.
- **Corroborates** `docs-github-copilot-org-targeted-model-rules.md` (issue #957,
  Claim 5): Both sources restate the Copilot Business/Copilot Enterprise license
  gate as the floor for enterprise-level Copilot governance features.
- **Extends** `docs-github-copilot-enterprise-bypass-permissions.md` (issue #1219,
  Claim 5): That source documented VS Code 1.122+ as the client-version floor for
  enterprise-managed settings as of June 17. This source shows the floor has moved
  to 1.126+ for at least the `model` permission key — the guide should not assume a
  single fixed version floor applies to the whole `managed-settings.json` schema
  going forward; each new permission key may carry its own minimum client version.
- **Extends** `docs-github-copilot-cca-auto-model-selection.md` (issue #745) and
  `docs-github-copilot-cli-auto-model-selection.md` (issue #203): Those sources
  document auto model selection as a per-surface, per-user opt-in routing mode.
  This source adds an administrative layer above both: an enterprise can now set
  the *starting* selection mode for CLI and VS Code conversations to auto, without
  changing the underlying routing heuristic documented in those sources (CLI auto's
  plan/policy/rate-limit routing, or VS Code auto's task-aware routing, remain
  exactly as previously documented — this source only changes what a conversation
  defaults to before a user makes a choice).
- **Contradicts**: None. This is a strictly additive governance capability layered
  on the existing `managed-settings.json` mechanism. It does not conflict with
  `docs-github-copilot-free-student-auto-only-model-selection.md` (issue #1305)
  because that source's auto-only *mandatory* policy applies to a different plan
  tier (Free/Student, individual non-enterprise plans) than this source's
  Business/Enterprise *default-but-overridable* policy — these are two different
  populations of users with two different levels of restriction, not two competing
  claims about the same population. No contradiction issue filed.
- **Novel**:
  - First corpus source to document an enterprise-administered *default* for model
    selection mode (as distinct from a mandatory restriction, issue #1305, or a
    per-surface user opt-in, issues #745/#203/#844).
  - First corpus source to show a `managed-settings.json` permission key requiring
    a client version floor (VS Code 1.126+) newer than the file's original 1.122+
    baseline, establishing that version requirements are per-key, not per-file.
  - First corpus evidence (via the linked Community discussion, Claim 10) of a
    GitHub staff engineer directly confirming enforcement behavior for
    `disableBypassPermissionsMode` outside of official documentation.

## Guide Impact

- **Chapter 02 (Harness Engineering / Tooling Landscape)**: Add `model: auto` to
  the documented `managed-settings.json` `permissions` schema as the fourth known
  enterprise-managed-settings capability (after plugin distribution, hooks/MCP
  enforcement, and `disableBypassPermissionsMode`). Update the client-version table
  to track per-key minimums rather than a single file-wide floor — VS Code 1.122+
  suffices for the first three capabilities, but 1.126+ is required for `model: auto`
  specifically.
- **Chapter 02 / Ch05 (auto-model-selection surface map)**: The guide's existing
  auto-routing surface map (CLI, VS Code, CCA, Chat, per issues #203/#844/#745/#1218)
  should gain a new row distinguishing *who sets the default* from *how routing
  works*: this source lets an enterprise admin pre-select "auto" as the starting
  mode for CLI and VS Code conversations, while the routing heuristic within "auto"
  (task-aware for VS Code/Chat, availability-driven for CLI) is unchanged and
  documented separately.
- **Chapter 05 (Team Adoption / Enterprise Governance)**: Recommend this setting as
  a low-friction adoption lever distinct from the harder restrictions in
  `docs-github-copilot-free-student-auto-only-model-selection.md` (issue #1305):
  enterprises can nudge Business/Enterprise users toward auto (capturing the 10%
  billing-discount pattern documented across CLI/CCA/VS Code auto) while explicitly
  preserving per-conversation override — a softer governance posture than removing
  the manual picker outright. Pair with the existing `disableBypassPermissionsMode`
  and targeted-model-rules (issue #957) documentation as a growing "enterprise
  Copilot defaults" checklist, and flag the VS Code 1.126+ requirement as a
  prerequisite to verify before rollout.

## Extraction Notes

1. **Source is short by design (~150 words of primary changelog text)**: All
   substantive claims from the changelog itself are exhausted in Claims 1–7. Claims
   8–9 draw on the linked "managed-settings.json permissions" documentation page,
   followed per MINER.md §1 for depth; Claim 10 draws on the linked Community
   discussion.
2. **WebFetch AI-summarization risk**: Both WebFetch calls (changelog and linked
   docs page) return content processed through an AI model rather than raw HTML.
   Two independent fetches of the changelog page returned consistent wording for
   Claims 1–7, giving reasonable confidence in those quotes. The JSON schema in
   Concrete Artifacts and Claims 8–9, however, come from a single fetch of the
   linked docs page and are marked `emerging` rather than `settled` for that reason.
   The Assayer should spot-check Claims 1–9 directly against the live URLs.
3. **Community discussion was largely off-topic**: The linked discussion
   (`orgs/community/discussions/199139`) is the general enterprise-managed-settings
   thread, not one scoped to this specific auto-default feature — it predates this
   changelog and covers plugin-marketplace and bypass-permissions questions. Only
   the `disableBypassPermissionsMode`/VS Code 1.126.0 staff reply (Claim 10) was
   judged substantive enough to extract; the rest of the thread (Azure DevOps
   marketplace support, CCA plugin access) is out of scope for this source note.
4. **No contradictions found**: This source is purely additive to the existing
   enterprise-managed-settings and auto-model-selection corpus. See Cross-References
   for the reasoning on why it does not contradict the Free/Student auto-only policy
   (issue #1305) despite both being about "auto as the default."
