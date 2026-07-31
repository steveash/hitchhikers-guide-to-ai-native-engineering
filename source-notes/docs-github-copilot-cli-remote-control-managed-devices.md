---
source_url: https://github.blog/changelog/2026-07-30-limit-remote-control-to-managed-devices
source_type: docs
title: "Limit remote control to managed devices"
author: GitHub (official changelog)
date_published: 2026-07-30
date_extracted: 2026-07-31
last_checked: 2026-07-31
status: current
confidence_overall: settled
issue: "#2353"
---

# Limit Remote Control to Managed Devices

> GitHub's July 30, 2026 changelog adds a device-level `remoteControl` key to the
> enterprise `managed-settings.json` schema, letting enterprise owners restrict which
> devices are eligible to host remotely-controlled Copilot sessions (`disabled` /
> `requireSSO` / `enabled`) — a new access-control layer stacked on top of the
> existing org/enterprise "Store local sessions in the Cloud" policy that gates
> remote control on/off, and a sibling capability to the `permissions.*`,
> `enabledPlugins`, `extraKnownMarketplaces`, `strictKnownMarketplaces`, and
> `telemetry` keys already documented elsewhere in the corpus.

## Source Context

- **Type**: docs (GitHub official product changelog, July 30, 2026; ~150 words, tagged
  "Improvement", 1-minute read). Followed two linked documentation pages per
  MINER.md §1: "About remote control of GitHub Copilot CLI sessions"
  (`docs.github.com/copilot/concepts/agents/copilot-cli/about-remote-control`, linked
  from the changelog as "existing enterprise policy") and "Enterprise managed
  settings reference" (`docs.github.com/en/copilot/reference/enterprise-managed-settings-reference`,
  linked in turn from the "About remote control" page as "Enterprise managed settings
  reference"). Also fetched "Configuring enterprise managed settings"
  (`docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/configure-enterprise-managed-settings`,
  linked directly from the changelog as "the GitHub docs"). All four pages were
  fetched as raw HTML and parsed programmatically (not via AI-summarizing WebFetch),
  so quotes below are character-verified against the live pages at extraction time.
- **Author credibility**: GitHub engineering team announcing a production feature
  addition to the enterprise-managed settings system. Authoritative for: the
  existence and name of the `remoteControl` key, its schema (`mode`,
  `githubDotComOrganizations`), the three deployment mechanisms, the client support
  matrix, and the relationship to the pre-existing "Store local sessions in the
  Cloud" policy. Not a credible source for: adoption data, how IT teams are actually
  using device-group targeting in practice, or whether other AI coding tools plan
  equivalent device-trust controls.
- **Scope**: A single new key (`remoteControl`) in the enterprise `managed-settings.json`
  schema, layered on top of the org/enterprise-level policy that already gates
  whether remote control exists at all (documented in the "About remote control"
  page, not in the changelog itself). Covers: the `mode` values, the
  `githubDotComOrganizations` array, the three deployment mechanisms and their
  precedence order, and which clients (Copilot CLI, VS Code, GitHub Copilot app)
  respect the setting. Does NOT cover: how MDM tooling vendors (Intune, Jamf)
  concretely enroll a device as "managed" for GitHub's purposes, whether the
  setting can be scoped per-organization rather than per-device, or any UI for
  administrators to audit which devices currently qualify as managed.

## Extracted Claims

### Claim 1: Enterprises and organizations can now restrict which devices are eligible to host remotely controlled Copilot sessions, giving administrators fine-grained control over where remote control access is permitted

- **Evidence**: Lead sentence of the changelog body, raw-HTML-verified.
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "Enterprises and organizations can now restrict which devices are eligible to host remotely controlled Copilot sessions, giving administrators fine-grained control over where remote control access is permitted."
- **Our assessment**: This is a device-identity control layered on top of the
  account-level admin gate already documented in `docs-github-copilot-cli-remote-control-ga.md`
  Claim 7 ("an administrator will have to enable remote control and CLI policies
  before you can use it"). That May 2026 gate was binary (remote control on/off for
  the account); this July 2026 addition is granular (which *device* a given account's
  sessions may run on when controlled remotely). The Prospector's triage framed this
  as a "managed-device constraint" — the source confirms that framing, but the actual
  mechanism restricts the *controlling client's SSO status*, not device MDM enrollment
  per se (see Claim 5).

### Claim 2: The `remoteControl` enterprise managed setting lets administrators define exactly how remote control works on managed devices, including requiring SSO authorization for specific organizations or tailoring access per device, and works alongside the existing enterprise policy that controls whether remote control is available at all

- **Evidence**: Second paragraph of the changelog body, raw-HTML-verified.
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "The new remoteControl enterprise managed setting gives administrators the ability to define exactly how remote control works on managed devices, whether that means requiring SSO authorization for specific organizations or tailoring access on a per-device basis. This setting works alongside the existing enterprise policy, which controls whether remote control is available to users at all. Together, this gives you layered control from broad access down to per-device restrictions."
- **Our assessment**: GitHub is explicit that this is a *second, additive* layer, not
  a replacement for the existing gate. The "existing enterprise policy" the changelog
  points to (hyperlinked to the "About remote control" doc's Administering section)
  turns out to be named "Store local sessions in the Cloud" — see Claim 4. The
  two-layer structure (account-level policy + device-level `remoteControl` setting)
  mirrors the two-layer pattern already documented for plugin governance in
  `docs-github-copilot-enterprise-strict-known-marketplaces.md` (marketplace
  *definition* vs. marketplace *restriction*): a broad enablement policy, then a
  narrower restriction control layered on top.

### Claim 3: Administrators set `mode` to `requireSSO` to enforce SSO authorization, `disabled` to block remote control entirely, or `enabled` to allow it without restriction, and can add the `remoteControl` key to their `copilot-settings.json` file

- **Evidence**: "Getting started" section of the changelog, raw-HTML-verified.
- **Confidence**: settled (configuration values stated directly in official changelog)
- **Quote**: "Set mode to requireSSO to enforce SSO authorization, disabled to block remote control entirely, or enabled to allow it without restriction."
- **Our assessment**: The changelog's own prose calls the file `copilot-settings.json`,
  but the "Enterprise managed settings reference" page (fetched separately, see
  Extraction Notes) consistently calls it `managed-settings.json` and shows
  `remoteControl` as a top-level key in that same file, not nested under
  `permissions` the way `disableBypassPermissionsMode` and `model` are (contrast
  with `docs-github-copilot-enterprise-auto-model-default.md` Claim 8). This is a
  minor naming inconsistency within GitHub's own documentation (see Claim 4 for a
  related, pre-existing path-naming inconsistency already flagged in the corpus)
  rather than a claim we're taking a side on — practitioners should treat
  `managed-settings.json` (per the reference page) as canonical and `copilot-settings.json`
  (per the changelog prose) as likely a same-file informal reference.

### Claim 4: The setting is deployable via three mechanisms — server-managed (`.github-private` repository, applies to enterprise user accounts), MDM-managed (applies to specific managed devices), and file-based (applies to any machine that receives the file) — with a defined precedence order when multiple sources are present

- **Evidence**: Changelog "Deployment Mechanisms" list (raw-HTML-verified) combined
  with the "Enterprise managed settings reference" page's "Precedence rules" section
  (separately fetched, raw-HTML-verified).
- **Confidence**: settled (deployment mechanisms in official changelog; precedence
  order in official reference doc)
- **Quote**: "Server-managed (.github-private repository): Applies to user accounts in your enterprise. MDM-managed: Applies to specific devices and is ideal for enforcing policies on managed machines. File-based: Applies to any machine that receives the file." (changelog) / "When multiple settings sources are present, settings earlier in this list take precedence over settings later in the list: MDM-managed settings, Server-managed settings, File-based settings, User-level settings" (reference page)
- **Our assessment**: This confirms the three deployment mechanisms are shared
  infrastructure across every enterprise-managed setting in the corpus — the same
  three methods (server/MDM/file) also apply to `disableBypassPermissionsMode`
  (`docs-github-copilot-enterprise-bypass-permissions.md`), `strictKnownMarketplaces`
  (`docs-github-copilot-enterprise-strict-known-marketplaces.md`), and `model: auto`
  (`docs-github-copilot-enterprise-auto-model-default.md`), which were previously
  documented only via the `.github-private` server-managed path. This is the first
  corpus source to name the MDM-managed and file-based paths explicitly and to
  state the precedence order (MDM > server > file > user-level) — a practically
  important detail for enterprises deploying more than one mechanism simultaneously,
  since MDM-managed settings silently win conflicts over server-managed ones.

### Claim 5: The `remoteControl` setting is applied per device and restricts whether a session hosted on that device can be remotely controlled, based on whether the controlling client is SSO-authorized for the organizations listed in `githubDotComOrganizations`; it does not affect the same user's ability to remotely control sessions hosted on other devices

- **Evidence**: "Administering remote control" section of the "About remote control
  of GitHub Copilot CLI sessions" docs page (raw-HTML-verified), corroborated by the
  `remoteControl` key description in the "Enterprise managed settings reference"
  page's Supported keys table (raw-HTML-verified).
- **Confidence**: settled (mechanism described consistently across two official docs pages)
- **Quote**: "Enterprise owners can further restrict remote control using the remoteControl enterprise managed setting, which applies on top of the \"Store local sessions in the Cloud\" policy. This setting is applied per device and controls whether a session hosted on that device can be remotely controlled: it can require that the controlling client is SSO-authorized for specific organizations, or disable remote control of sessions hosted on that device entirely. It doesn't affect the same user's ability to remotely control sessions hosted on other devices."
- **Our assessment**: This is the precise technical mechanism the Prospector's
  triage comments speculated about ("MDM enrollment, device compliance, or
  GitHub-specific device registration"). The answer: `remoteControl` does not check
  device MDM-compliance status at all — it restricts based on the *SSO-authorization
  status of the client attempting the remote connection*, evaluated against an
  organization allowlist (`githubDotComOrganizations`) configured on the *hosting*
  device. "Managed device" in this feature's context means "a device where an
  enterprise admin has deployed a `managed-settings.json` restricting who may
  remote-control it" — not device compliance/health attestation in the traditional
  MDM sense. This is a meaningful clarification for Ch05/Ch07 guide coverage: the
  feature name ("managed devices") could mislead readers into expecting MDM
  compliance checks it does not perform.

### Claim 6: The `remoteControl` setting schema requires `mode` (`"disabled"` / `"requireSSO"` / `"enabled"`) and an optional `githubDotComOrganizations` array of organization logins, required only when `mode` is `"requireSSO"`

- **Evidence**: "Enterprise managed settings reference" page, dedicated `remoteControl`
  subsection (raw-HTML-verified).
- **Confidence**: settled (schema stated directly in official reference documentation)
- **Quote**: "mode: Set to \"disabled\" to prevent remote control of sessions on the device, \"requireSSO\" to only allow remote control from a client that is SSO-authorized for the organizations listed in githubDotComOrganizations, or \"enabled\" to allow it unrestricted. githubDotComOrganizations: An array of organization logins. Required when mode is \"requireSSO\"."
- **Our assessment**: This is a complete, independently-fetched schema definition —
  not inferred from the changelog's looser prose. The three-value `mode` enum
  (`disabled`/`requireSSO`/`enabled`) matches the "Getting started" wording in Claim 3
  exactly, confirming the changelog and the reference page describe the same
  mechanism despite the file-naming inconsistency noted in Claim 3.

### Claim 7: `remoteControl` is a top-level key in `managed-settings.json`, not nested under the `permissions` object that holds `disableBypassPermissionsMode` and `model`

- **Evidence**: The official "Example configuration" JSON block on the "Enterprise
  managed settings reference" page shows `remoteControl` as a sibling of
  `permissions`, `enabledPlugins`, `extraKnownMarketplaces`, `strictKnownMarketplaces`,
  and `telemetry` — all top-level keys — with `disableBypassPermissionsMode` and
  `model` nested one level deeper inside `permissions` (raw-HTML-verified; full JSON
  reproduced in Concrete Artifacts).
- **Confidence**: settled (schema structure directly observable in official example JSON)
- **Quote**: (no prose quote states this structurally; see the verbatim JSON in
  Concrete Artifacts, which is the source's own example configuration)
- **Our assessment**: This resolves an open question implicit in
  `docs-github-copilot-enterprise-auto-model-default.md` Claim 8, which documented
  `model` and `disableBypassPermissionsMode` as sibling keys inside `permissions`
  without establishing whether *all* enterprise-managed settings live under that
  object. They do not: `permissions` groups only behavior-modifying flags
  (bypass mode, model default), while `remoteControl`, `telemetry`,
  `enabledPlugins`, `extraKnownMarketplaces`, and `strictKnownMarketplaces` are
  separate top-level keys. For Ch02: the guide's schema reference for
  `managed-settings.json` should show this two-tier structure (a `permissions`
  object plus five sibling top-level keys) rather than treating every setting as
  if it lived in one flat or one nested namespace.

### Claim 8: `remoteControl` is respected by all three Copilot clients GitHub currently supports for enterprise managed settings — Copilot CLI, VS Code, and the GitHub Copilot app — unlike `telemetry`, which is not supported in the GitHub Copilot app

- **Evidence**: The "Supported keys" table on the "Enterprise managed settings
  reference" page lists client support per key; `remoteControl`'s row marks all
  three client columns as supported, while `telemetry`'s row marks Copilot CLI and
  VS Code as supported but not the GitHub Copilot app (raw-HTML-verified via
  programmatic table parsing, including icon detection for the unsupported cell).
- **Confidence**: settled (table data directly parsed from official reference page)
- **Quote**: (no prose quote for table cell values; see Concrete Artifacts for the
  parsed table)
- **Our assessment**: This is the first corpus source to establish a per-key client
  support matrix for enterprise-managed settings rather than a single blanket
  "Copilot CLI and VS Code" scope statement (which is how prior notes, e.g.
  `docs-github-copilot-enterprise-bypass-permissions.md` Claim 2, described scope).
  `remoteControl` having full three-client support while `telemetry` does not
  suggests the "GitHub Copilot app" (a client not previously named in the corpus's
  enterprise-managed-settings notes) is itself a distinct, real-time-interaction
  surface where remote-control restrictions matter, but bulk telemetry export does
  not apply.

### Claim 9: The account-level gate for remote control is a policy named "Store local sessions in the Cloud," configurable at the organization level ("View from cloud" / "View and control", unconfigured by default) and enforceable at the enterprise level across all organizations, or delegated to organizations to decide individually

- **Evidence**: "Administering remote control" section of the "About remote control"
  docs page, linked directly from this changelog's "existing enterprise policy"
  hyperlink (raw-HTML-verified).
- **Confidence**: settled (policy name and configuration model stated directly in
  linked official documentation)
- **Quote**: "Enterprise and organization owners control whether users can enable remote control using the \"Store local sessions in the Cloud\" policy. Organization-level policy (unconfigured by default): Organization owners can set this policy to \"View from cloud\" (syncing only) or \"View and control\" (syncing plus remote control). ... Enterprise-level policy: Enterprise owners can enforce a setting across all organizations, or select \"Let organizations decide\" to let each organization choose its own level."
- **Our assessment**: This names, for the first time in the corpus, the specific
  policy GitHub's May 2026 GA changelog described only loosely as "remote control
  and CLI policies" (`docs-github-copilot-cli-remote-control-ga.md` Claim 7). We do
  not read this as a contradiction of that earlier claim — the GA changelog's prose
  was simply less precise than this dedicated concepts page, and the GA changelog's
  "CLI policies" may refer to a separate Copilot CLI enablement policy not covered
  by this source. No contradiction issue filed (see MINER.md §4a "when not to
  file": this is a specificity difference, not an opposing claim). For Ch05: update
  the guide's admin-policy documentation to name "Store local sessions in the
  Cloud" as the actual policy string administrators should look for in GitHub
  Enterprise/Organization settings, rather than the vaguer "remote control policy"
  language.

### Claim 10: Remote control requires an interactive CLI session — it is unavailable when Copilot CLI is invoked programmatically via the `--prompt` command-line option, such as in a script

- **Evidence**: "Prerequisites" section of the "About remote control" docs page
  (raw-HTML-verified).
- **Confidence**: settled (stated directly in official documentation)
- **Quote**: "An interactive session: Remote access is only available for interactive sessions. It is not available when you use the CLI programmatically with the --prompt command-line option, for example when you use the CLI in a script."
- **Our assessment**: This is a scope boundary not previously documented in the
  corpus's remote-control coverage. It clarifies that `remoteControl`'s device
  restrictions (and the underlying feature generally) are irrelevant to fully
  headless/scripted Copilot CLI usage — the governance surface this source and
  `docs-github-copilot-cli-remote-control-ga.md` both describe applies only to
  human-initiated interactive sessions that are later handed off for remote
  steering, not to unattended automation. For Ch02: the guide's distinction
  between "truly unattended headless sessions" and "remotely-supervised sessions"
  (already flagged as a needed update in `docs-github-copilot-cli-remote-control-ga.md`
  Guide Impact, Chapter 02) should note that `--prompt`-driven scripted sessions are
  categorically excluded from remote control, not merely unlikely to use it.

### Claim 11: Managed settings are loaded locally when a client starts, even with no network connection, and the `managed-settings.json` value takes precedence over any file-based configuration a user sets in their own client

- **Evidence**: "Configuring enterprise-managed settings" docs page, linked directly
  from the changelog as "the GitHub docs" (raw-HTML-verified).
- **Confidence**: settled (stated directly in official documentation)
- **Quote**: "These settings apply enterprise-wide, with no organization-level override. For each supported key, the managed-settings.json value takes precedence over any file-based configuration a user sets in their client. Managed settings are loaded locally when the client starts, even if the device has no network connection."
- **Our assessment**: This establishes that `remoteControl` restrictions (like all
  enterprise-managed settings) are enforced client-side at startup, not via a
  server-side check performed at connection time — meaning a device that received
  its `managed-settings.json` before going offline still enforces the restriction
  offline. This is a durability property worth documenting for Ch05/Ch07: an
  enterprise cannot rely on revoking a device's remote-control eligibility in
  real time by pushing a settings change; propagation still depends on the client
  next fetching (or being pushed, for MDM) an updated file.

## Concrete Artifacts

### `remoteControl` example configuration (verbatim from "Enterprise managed settings reference")

```json
{
  "permissions": {
    "disableBypassPermissionsMode": "disable",
    "model": "auto"
  },
  "enabledPlugins": {
    "my-plugin@agent-skills": true
  },
  "extraKnownMarketplaces": {
    "agent-skills": {
      "source": {
        "source": "github",
        "repo": "OWNER/REPO"
      }
    }
  },
  "strictKnownMarketplaces": [
    {
      "source": "github",
      "repo": "OWNER/REPO"
    }
  ],
  "telemetry": {
    "enabled": true,
    "endpoint": "https://otel-collector.example.com",
    "protocol": "http/protobuf",
    "captureContent": false,
    "lockCaptureContent": true,
    "serviceName": "copilot",
    "resourceAttributes": {
      "deployment.environment": "production"
    },
    "headers": {
      "Authorization": "Bearer TOKEN"
    }
  },
  "remoteControl": {
    "mode": "requireSSO",
    "githubDotComOrganizations": ["ORG-NAME"]
  }
}
```
*Source: docs.github.com/en/copilot/reference/enterprise-managed-settings-reference,
"Example configuration" section, fetched as raw HTML and reproduced verbatim
(minus the page's own internal syntax-highlighting markup). Note that this same
page's prose consistently calls this file `managed-settings.json`, while the
July 30 changelog's own "Getting started" section calls it `copilot-settings.json`
(see Claim 3) — a naming inconsistency in GitHub's own docs, not an error in this
extraction.*

### Supported-keys client matrix (parsed from the reference page's table, including icon cells)

```
Key                                        Copilot CLI   VS Code   GitHub Copilot app
permissions.disableBypassPermissionsMode   YES           YES       YES
permissions.model                          YES           YES       YES
enabledPlugins                             YES           YES       YES
extraKnownMarketplaces                     YES           YES       YES
strictKnownMarketplaces                    YES           YES       YES
telemetry                                  YES           YES       NO
remoteControl                              YES           YES       YES   <- this note
```
*Source: docs.github.com/en/copilot/reference/enterprise-managed-settings-reference,
"Supported keys" table, parsed programmatically from the raw table markup
(text cells plus check/x icon detection) rather than read visually.*

### Deployment mechanism precedence (verbatim from reference page)

```
Precedence (highest to lowest) when multiple settings sources are present:
1. MDM-managed settings
2. Server-managed settings
3. File-based settings
4. User-level settings

Deployment method guidance (from "Configuring enterprise-managed settings"):
- Server-managed:  "Default for most enterprises and best for review workflows
                     and audit history"
- MDM-managed:      "Best when IT teams need device-group targeting through
                     existing MDM tooling on macOS and Windows"
- File-based:       "Available on all platforms, and useful when server-managed
                     and MDM-managed deployment are not available, including
                     developer environments such as containers and Codespaces"
```
*Source: docs.github.com/en/copilot/reference/enterprise-managed-settings-reference
("Precedence rules") and .../configure-enterprise-managed-settings ("Choosing a
deployment method"), both fetched as raw HTML.*

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-enterprise-bypass-permissions.md` Claim 3 and Claim 4:
    the `.github-private`-repository server-managed path and the newer preferred
    `copilot/managed-settings.json` naming are reaffirmed as the shared
    configuration surface `remoteControl` also uses. This note adds MDM-managed
    and file-based deployment as explicitly named alternatives to that path —
    previously implied but not spelled out in the bypass-permissions note.
  - `docs-github-copilot-enterprise-strict-known-marketplaces.md` Claim 5: the
    "GitHub Copilot automatically pulls and applies these settings for users
    licensed through your Copilot Business or Copilot Enterprise account"
    auto-application pattern is consistent with the client-loads-at-startup model
    documented in Claim 11 of this note.
  - `docs-github-copilot-cli-remote-control-ga.md` Claim 2: the "approve or deny
    permission requests remotely" capability from the May 2026 GA note remains the
    interaction this July 2026 device restriction governs access *to* — this
    source restricts *which device* can perform that remote approval, not what
    the approval itself does.

- **Extends**:
  - `docs-github-copilot-cli-remote-control-ga.md` Claim 7: refines the loosely
    stated "an administrator will have to enable remote control and CLI policies"
    into the precisely named "Store local sessions in the Cloud" policy (Claim 9
    of this note), and adds an entirely new device-level restriction layer
    (`remoteControl`) that did not exist at GA in May 2026.
  - `docs-github-copilot-enterprise-auto-model-default.md` Claim 8: resolves the
    open question of whether all enterprise-managed settings nest under
    `permissions` — they do not; `remoteControl` (like `telemetry`,
    `enabledPlugins`, `extraKnownMarketplaces`, `strictKnownMarketplaces`) is a
    top-level sibling key (Claim 7 of this note).
  - `docs-github-copilot-enterprise-strict-known-marketplaces.md` (the
    "distribution vs. restriction" two-layer pattern for plugin marketplaces):
    this note's account-level policy + device-level `remoteControl` structure
    (Claim 2, Claim 9) is a second instance of the same two-layer governance
    shape GitHub is applying across different Copilot capabilities.

- **Contradicts**: None identified as a genuine opposing claim. The apparent
  discrepancy between the GA note's "remote control and CLI policies" phrasing
  and this source's single named "Store local sessions in the Cloud" policy
  (Claim 9) is treated as a specificity/precision difference, not a contradiction,
  per MINER.md §4a guidance — no contradiction issue filed.

- **Novel**:
  - First corpus documentation of a device-identity/SSO-based access control for
    an AI coding tool's remote-control feature (Claims 5, 6).
  - First corpus documentation of MDM-managed and file-based deployment as named,
    described alternatives to the `.github-private` server-managed path for
    enterprise-managed Copilot settings, plus the precedence order among all three
    (Claim 4).
  - First corpus documentation of a per-key client support matrix (Copilot CLI /
    VS Code / GitHub Copilot app) for enterprise-managed settings, and the first
    mention of "GitHub Copilot app" as a distinct managed-settings client
    (Claim 8).
  - First corpus clarification that `managed-settings.json` has a two-tier key
    structure (a `permissions` object plus separate top-level keys), rather than
    every setting nesting under one object (Claim 7).
  - First corpus documentation that remote control is unavailable for
    `--prompt`-driven scripted/headless Copilot CLI invocations (Claim 10).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: The `managed-settings.json` schema
  reference (already recommended for addition by `docs-github-copilot-enterprise-bypass-permissions.md`,
  `docs-github-copilot-enterprise-strict-known-marketplaces.md`, and
  `docs-github-copilot-enterprise-auto-model-default.md`, none of which appear to
  be reflected in `guide/02-harness-engineering.md` as of this extraction — the
  guide currently has no mention of `remote control`, `managed-settings`, or
  `enterpriseManaged` per a direct grep) should show the two-tier key structure
  (top-level `permissions` object plus sibling top-level keys `remoteControl`,
  `telemetry`, `enabledPlugins`, `extraKnownMarketplaces`, `strictKnownMarketplaces`)
  and the three-mechanism deployment model with its MDM > server > file > user
  precedence order (Claim 4, Claim 7).
- **Chapter 05 (Team Adoption)**: Add "Store local sessions in the Cloud" (Claim 9)
  as the precise policy name administrators should locate in enterprise/organization
  settings to enable remote control at all, distinct from the newer device-level
  `remoteControl` restriction. Note that `remoteControl` is a device-identity/SSO
  control, not an MDM-compliance check, despite the feature's "managed devices"
  name (Claim 5) — practitioners evaluating this for zero-trust or endpoint-security
  posture should not assume it verifies device health or enrollment status.
- **Chapter 06 (Security & Threat Model)**: Document the client-side, load-at-startup
  enforcement model (Claim 11): an enterprise cannot instantly revoke a device's
  remote-control eligibility by editing `managed-settings.json` — enforcement
  depends on the client's next fetch (server/file-based) or the MDM tool's next
  push cycle. For threat modeling, this creates a window between a policy change
  and full enforcement across all managed devices. Also document the `--prompt`
  scripted-session exclusion (Claim 10) as a boundary of the remote-control threat
  surface: fully headless CLI automation is unaffected by any of these controls.

## Extraction Notes

1. **Raw HTML fetched directly, not via AI-summarizing WebFetch**: The changelog
   and all three linked documentation pages were fetched with `curl` and parsed
   programmatically (regex tag-stripping plus, for the client-support table,
   structural `<tr>`/`<td>` parsing with icon detection) rather than passed through
   WebFetch's summarizing model. All quotes in this note are therefore verified
   character-for-character against the live pages at extraction time, not
   reconstructed from an AI summary — a stronger verification standard than several
   prior notes in this corpus achieved (compare the "WebFetch AI-summarized
   content" caveats in `docs-github-copilot-enterprise-bypass-permissions.md`
   Extraction Note 1 and `docs-github-copilot-enterprise-auto-model-default.md`
   Extraction Note 2).
2. **Followed three linked pages, one below the two-hop budget in MINER.md §1**:
   changelog → "About remote control" (linked from the changelog) → "Enterprise
   managed settings reference" (linked from "About remote control") and
   "Configuring enterprise-managed settings" (linked directly from the changelog).
   All three were substantive and materially expanded the claims beyond what the
   ~150-word changelog alone would support.
3. **File-naming inconsistency in GitHub's own docs**: the changelog prose says
   `copilot-settings.json`; the reference page consistently says `managed-settings.json`.
   Flagged in Claim 3 rather than silently resolved — the Assayer should treat
   both spellings as attested in the primary sources rather than assume one is a
   typo.
4. **No contradiction issue filed**: see Cross-References → Contradicts. The
   "Store local sessions in the Cloud" policy name (Claim 9) refines rather than
   opposes the GA note's looser "remote control and CLI policies" phrasing.
5. **guide/ grep performed to ground Guide Impact**: confirmed via
   `grep -n -i "remote control\|managed-settings\|managed device\|enterprise managed\|remoteControl" guide/*.md`
   that none of these terms currently appear anywhere in the guide, so the Guide
   Impact recommendations above (and the equivalent recommendations in the three
   related enterprise-managed-settings notes) remain unimplemented as of this
   extraction.
