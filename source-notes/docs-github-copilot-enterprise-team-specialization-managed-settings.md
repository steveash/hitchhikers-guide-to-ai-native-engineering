---
source_url: https://github.blog/changelog/2026-08-03-enterprise-team-specialization-for-managed-settings
source_type: docs
title: "Enterprise team specialization for managed settings"
author: GitHub (official changelog)
date_published: 2026-08-03
date_extracted: 2026-08-04
last_checked: 2026-08-04
status: current
confidence_overall: settled
issue: "#2473"
---

# Enterprise Team Specialization for Managed Settings

> GitHub's August 3, 2026 changelog adds team-level specialization to the enterprise
> `managed-settings.json` system: enterprise administrators can mark specific keys
> `overridable` so that enterprise teams can set their own values (falling back to the
> enterprise default when unset), let plugin/marketplace keys grow additively per team,
> and route different team settings files to different team slugs via `team-mappings.json`
> — with non-overridable keys always winning as a compliance ceiling.

## Source Context

- **Type**: docs (GitHub official product changelog, August 3, 2026; ~2-minute read,
  tagged `client-apps`, `copilot`, `enterprise management tools`). One linked
  documentation page followed per MINER.md §1: "Applying different settings to
  enterprise teams" (a subsection of the enterprise-managed-settings reference at
  `docs.github.com/enterprise-cloud@latest/copilot/reference/enterprise-managed-settings-reference`),
  which supplied additional schema detail. The linked GitHub Community discussion
  (`orgs/community/discussions/199139`) is the same general enterprise-managed-settings
  thread already noted as off-topic-for-specific-features in
  `docs-github-copilot-enterprise-auto-model-default.md` (Claim 10, Extraction Note 3);
  not re-fetched for this note since it predates this feature and is not scoped to it.
- **Author credibility**: GitHub engineering team announcing a production capability
  extension to the enterprise-managed-settings system that has been the subject of four
  prior corpus source notes (June 5, June 17, June 25, July 1, 2026 — see
  Cross-References). Authoritative for: the existence and syntax of the `overridable`
  mechanism, the additive semantics of `enabledPlugins`/`extraKnownMarketplaces`, the
  `team-mappings.json` routing mechanism, the `copilot/teams/` file location, the
  precedence/combination rules for multi-team users, and the supported-client list. Not
  a credible source for: how conflicts between overlapping overridable values are
  surfaced to admins in the UI, performance/latency of settings resolution at scale,
  or real-world adoption data — this is a day-one feature announcement.
- **Scope**: A single new capability layer (team-level specialization) added on top of
  the existing enterprise `managed-settings.json` system. Covers: the `overridable`
  syntax, which keys are overridable (per the linked docs, `permissions.model` and
  `permissions.disableBypassPermissionsMode`), additive plugin/marketplace keys,
  `team-mappings.json`, the `copilot/teams/` directory, precedence/combination rules,
  and supported clients. Does NOT cover: whether `overridable` can be applied to keys
  beyond the two named in the docs excerpt, how this interacts with the org-level
  targeted model rules from `docs-github-copilot-org-targeted-model-rules.md` (issue
  #957), UI/audit tooling for viewing effective per-team settings, or GA/preview status
  (the changelog text obtained does not state a preview label, unlike several prior
  entries in this family).

## Extracted Claims

### Claim 1: Enterprise administrators can now customize managed settings by targeting enterprise teams with itemized configuration files, letting large enterprises scale governance without bottlenecking every change through central administrators or one-size-fits-all policies

- **Evidence**: Official GitHub changelog, opening sentence of the entry.
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "Enterprise administrators can now customize managed settings by targeting enterprise teams with itemized configuration files. Large enterprises can scale governance without bottlenecking every configuration change through central administrators or one-size-fits-all policies."
- **Our assessment**: This is the headline capability and directly answers the
  Prospector's triage question about what enables team-level specialization. Prior
  corpus coverage of enterprise-managed settings (`docs-github-copilot-enterprise-managed-plugins-vscode.md`,
  `docs-github-copilot-enterprise-bypass-permissions.md`,
  `docs-github-copilot-enterprise-strict-known-marketplaces.md`,
  `docs-github-copilot-enterprise-auto-model-default.md`) documents a strictly
  enterprise-wide configuration model: one settings file, one set of values, applied
  uniformly to every licensed user. This changelog is the first to introduce a
  sub-enterprise unit (the team) as a first-class configuration target, which is a
  structural change to the governance model, not just a new key.

### Claim 2: Teams gain the flexibility to adapt Copilot to their workflows while staying within enterprise-defined boundaries

- **Evidence**: Official changelog, second sentence of the opening paragraph.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Teams gain the flexibility to adapt Copilot to their workflows while staying within the boundaries you've defined."
- **Our assessment**: This framing — flexibility bounded by admin-set limits — is the
  design philosophy the rest of the entry operationalizes via the ceiling/floor
  precedence model (Claim 10). It positions team specialization as risk-bounded
  delegation, not decentralized self-governance.

### Claim 3: GitHub recommends setting the AI standards source `.github-private` repository to `internal` visibility and letting users open pull requests to suggest changes that keep their team's specialized governance configuration up to date

- **Evidence**: Official changelog, second paragraph, framed as a shared-responsibility
  recommendation tied to the pace of AI ecosystem change.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Set your AI standards source `.github-private` repository to `internal` visibility and let your users open pull requests to suggest changes that keep their specialized governance configuration up to date."
- **Our assessment**: This is an operational recommendation, not just a feature
  description — GitHub is explicitly endorsing a PR-driven maintenance model for
  team-level governance configuration, extending the "governance lives in source
  control" pattern already established for the enterprise-wide file in
  `docs-github-copilot-enterprise-managed-plugins-vscode.md` (Claim 3: "the enterprise
  plugin settings live in source control... version-controlled, and can be managed via
  PRs and code review"). The novelty here is opening that PR workflow to end users
  (`your users`, not just admins) for the team-scoped files, which is a meaningfully
  different trust model than the admin-only enterprise file.

### Claim 4: Individual keys in `managed-settings.json` can be marked overridable using `{ "overridable": <value> }` syntax; an overridable key uses the team's value when the team sets one, or falls back to the enterprise default when the team leaves it unset

- **Evidence**: Official changelog, "What you can do" section, "Mark keys as
  overridable" bullet.
- **Confidence**: settled (mechanism and fallback semantics stated directly in
  official changelog)
- **Quote**: "Mark keys as overridable: In your `copilot/managed-settings.json` file, use the `{ \"overridable\": }` syntax to specialize the key's configuration on a per-team basis. An overridable key uses the team's value when set or falls back to your enterprise default when the team leaves it unset."
- **Our assessment**: This is the core mechanism of the entire feature. It is an
  explicit, per-key opt-in (the enterprise admin decides which keys are eligible for
  team override, not the teams themselves) — consistent with the "boundaries you've
  defined" framing in Claim 2. For Ch02: document `{ "overridable": <value> }` as the
  marker syntax that converts a normally-locked enterprise key into a team-specializable
  one, with the marked value acting as the enterprise-wide fallback.

### Claim 5: Keys not marked overridable remain an enterprise-level decision that teams cannot modify

- **Evidence**: Official changelog, same "Mark keys as overridable" bullet.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Keys you don't mark overridable remain an enterprise-level decision that teams can't modify."
- **Our assessment**: This is the default-deny complement to Claim 4 — specialization
  is opt-in per key, and the unmarked majority of the schema stays enterprise-locked.
  Combined with Claim 10's "ceiling" framing, this means adopting team specialization
  does not implicitly loosen any existing enterprise control; only explicitly
  designated keys become team-adjustable.

### Claim 6: A concrete example given in the changelog is setting `"disableBypassPermissionsMode": "unmanaged"` and `"model": "unmanaged"` in a team settings file, letting one team (e.g., an "AI Pioneers" team) pick its own default model and bypass-permissions posture while every other team inherits the enterprise defaults

- **Evidence**: Official changelog, "What you can do" section, worked example
  immediately following the overridable-syntax explanation.
- **Confidence**: settled (concrete example stated directly in official changelog)
- **Quote**: "In practice, you can set `\"disableBypassPermissionsMode\": \"unmanaged\"` and `\"model\": \"unmanaged\"` in a team settings file, providing a specialization that takes precedence over `managed-settings.json` for members of that team. For example, let your AI Pioneers team pick their own default model and bypass permissions, while every other team inherits your enterprise defaults."
- **Our assessment**: This names the two specific keys GitHub chose as the
  flagship example for the feature: `disableBypassPermissionsMode` (documented as an
  enterprise governance control in `docs-github-copilot-enterprise-bypass-permissions.md`)
  and `model` (documented as an enterprise default-setting control in
  `docs-github-copilot-enterprise-auto-model-default.md`). Both are prior corpus
  entries; this changelog is the first to show them being loosened per-team via
  `"unmanaged"` rather than set to a specific enforced value. The `"unmanaged"` value
  functions as an explicit opt-out signal at the team level — distinct from simply
  omitting the key.

### Claim 7: `enabledPlugins` and `extraKnownMarketplaces` are additive keys: the enterprise baseline is guaranteed everywhere, and individual teams can layer on extra plugins/marketplaces for specific job roles without weakening the enterprise floor

- **Evidence**: Official changelog, "Team-based plugin extensibility" bullet.
- **Confidence**: settled (additive semantics stated directly in official changelog)
- **Quote**: "Team-based plugin extensibility: Let plugins and marketplaces grow team-by-team, not shrink. `enabledPlugins` and `extraKnownMarketplaces` are additive (i.e, your enterprise baseline is guaranteed everywhere, and individual teams can layer on the extras they need for specific job roles without weakening the floor)."
- **Our assessment**: This is architecturally different from the `overridable`
  replace-or-fallback semantics of Claims 4-6: additive keys can only expand the set,
  never restrict it below the enterprise baseline. This is the first corpus source to
  name `enabledPlugins` and `extraKnownMarketplaces` as specific schema keys — prior
  notes (`docs-github-copilot-enterprise-managed-plugins-vscode.md`,
  `docs-github-copilot-enterprise-strict-known-marketplaces.md`) described plugin
  distribution and marketplace restriction capabilities but did not name these exact
  keys. Whether `extraKnownMarketplaces` at the team level can add marketplaces beyond
  what `strictKnownMarketplaces` permits at the enterprise level is not addressed by
  this changelog — see Extraction Notes.

### Claim 8: Enterprise administrators map each team settings file to one or more team slugs in `team-mappings.json`, so a single settings file (e.g., a shared `ai-users.json` for all teams that completed training) can apply across multiple teams, with additional files (e.g., `devs.json`) layered for other job roles

- **Evidence**: Official changelog, "Map settings files to teams" bullet, including
  the worked example.
- **Confidence**: settled (mechanism and example stated directly in official changelog)
- **Quote**: "Map settings files to teams: Ship different policies to different teams from one place. Map each team settings file to one or more team slugs in `team-mappings.json`. Each entry pairs a settings file with the teams that use it, so you can apply one file across multiple teams. For example, a single `ai-users.json` file can be applied to all teams that have completed training. Additional specializations can be applied for other job roles like `devs.json`."
- **Our assessment**: `team-mappings.json` is a many-to-one routing layer (multiple
  team slugs can point at one file), which avoids duplicating identical configuration
  across teams that share a governance posture (e.g., "completed AI training"). For
  Ch02: document `team-mappings.json` as the routing table that decouples "which teams
  get this policy" from "what the policy contains" — a reusable pattern for enterprises
  organizing teams by training status, job role, or risk tier rather than by
  org-chart team name alone.

### Claim 9: Team configuration is added under `copilot/teams/`, and should only include the keys marked as overridable — anything else falls back to the enterprise platform decision

- **Evidence**: Official changelog, "Create the team settings file" bullet.
- **Confidence**: settled (file location and scoping rule stated directly in official
  changelog)
- **Quote**: "Create the team settings file: Add the team's configuration under `copilot/teams/`. Only include the keys you marked as overridable. Anything else falls back to your enterprise platform decision."
- **Our assessment**: This confirms `copilot/teams/` as a new directory in the same
  `.github-private` source-org configuration surface documented across the prior four
  enterprise-managed-settings notes, alongside the existing `copilot/managed-settings.json`
  file. The "only include overridable keys" instruction is a practical authoring
  constraint: a team file that includes a non-overridable key presumably has no effect
  for that key (Claim 5), so GitHub is telling admins not to bother — though the
  changelog does not state whether including a non-overridable key in a team file
  produces a validation error or is silently ignored.

### Claim 10: Enterprise decisions always win for non-overridable keys, which set a compliance ceiling; overridable/unmanaged keys set a floor; and for a user belonging to multiple teams, team-level settings are combined using the least-restrictive value for each key, then applied beneath the enterprise file

- **Evidence**: Official changelog, "Trust that enterprise decisions always win"
  bullet — the precedence and multi-team-combination rule.
- **Confidence**: settled (precedence rule stated directly in official changelog)
- **Quote**: "Trust that enterprise decisions always win: Keys you don't mark overridable set a ceiling, so compliance-critical settings stay locked down by default. Unmanaged or overridable keys set a floor. If a user belongs to multiple teams, the team-level settings are combined using the least restrictive value for each key, then applied beneath the enterprise file."
- **Our assessment**: This is the single most operationally important claim in the
  source for anyone actually deploying the feature: "least restrictive value" as the
  multi-team combination rule means a user who is on both a locked-down team and a
  permissive team inherits the *permissive* team's value for any key both teams
  attempt to specialize. This is a meaningful governance risk practitioners must
  understand before granting team leads authority to set overridable keys — team
  membership overlap can silently widen a user's effective permissions beyond what any
  single team admin intended. For Ch04/05 (Governance): flag this "least restrictive
  wins" rule explicitly as a security review item for any enterprise adopting
  multi-team users with overridable `disableBypassPermissionsMode` values.

### Claim 11: As of this changelog, the team-specialized configuration is enforced in VS Code, Copilot CLI, the Copilot App, and Copilot cloud agent for users with a Copilot Business or Copilot Enterprise license issued from the enterprise or one of its organizations, with GitHub working to extend support across all Copilot clients through the Copilot SDK

- **Evidence**: Official changelog, "Supported clients" section.
- **Confidence**: settled (client list and license scope stated directly in official
  changelog; the SDK extension is a forward-looking statement, not yet delivered)
- **Quote**: "Today the configuration defined in `managed-settings.json` is enforced in VS Code, Copilot CLI, the Copilot App, and Copilot cloud agent whenever a user has a Copilot Business or Copilot Enterprise license issued from the enterprise or one of its organizations. We are working to extend this support across all Copilot clients through the Copilot SDK."
- **Our assessment**: This is a wider client list than any single prior
  enterprise-managed-settings note in the corpus — it explicitly adds "the Copilot App"
  and "Copilot cloud agent" alongside the VS Code + CLI pairing documented repeatedly
  in the June/July notes. Whether team-specialized settings are enforced identically
  across all four clients, or whether some clients only respect the enterprise-wide
  (non-team) portion of `managed-settings.json`, is not stated — the sentence covers
  "the configuration defined in `managed-settings.json`" generally, and this changelog
  does not distinguish team-file enforcement from base-file enforcement per client. The
  "working to extend... through the Copilot SDK" statement confirms the client list is
  still expanding and is not the final state.

### Claim 12 (secondary source, linked docs page): The `overridable` syntax is documented as applying specifically to `permissions.model` and `permissions.disableBypassPermissionsMode` — confirming these are sibling keys nested under a `permissions` object in the `managed-settings.json` schema

- **Evidence**: Linked documentation page "Applying different settings to enterprise
  teams" (part of the enterprise-managed-settings reference), fetched via
  AI-summarizing WebFetch rather than obtained as raw HTML.
- **Confidence**: emerging (from a secondary documentation page processed by
  AI-summarizing WebFetch, not the changelog itself, and not independently
  character-verified — see Extraction Notes)
- **Quote**: (no direct verbatim quote recoverable from the WebFetch summary for this
  page; see Extraction Notes and paraphrase above)
- **Our assessment**: This corroborates `docs-github-copilot-enterprise-auto-model-default.md`
  Claim 8, which independently documented `model` and `disableBypassPermissionsMode`
  as sibling keys under a `permissions` object in `managed-settings.json` as of July 1,
  2026. This changelog's own worked example (Claim 6) is consistent with that nesting
  — both keys are shown being overridden together in one team file. Practically, this
  means the changelog's `overridable` mechanism (as currently documented) may be scoped
  to the `permissions` object rather than the full schema; the Assayer should verify
  against the live documentation page whether `enabledPlugins` and
  `extraKnownMarketplaces` (Claim 7, additive rather than overridable) live in a
  different part of the schema than `permissions.model` / `permissions.disableBypassPermissionsMode`.

## Concrete Artifacts

### Team specialization mechanism (from changelog, August 3, 2026)

```
Enterprise file (existing):  copilot/managed-settings.json
New team files:               copilot/teams/<team-file-name>.json
New routing file:             copilot/teams/team-mappings.json  (per changelog prose;
                               exact path not given as a code block in the changelog —
                               only referred to as "team-mappings.json")

Mechanism:
  1. In copilot/managed-settings.json, mark a key overridable:
       { "overridable": <enterprise-default-value> }
  2. In a team file under copilot/teams/, set the same key to a team-specific value,
     or "unmanaged" to opt the team out of enterprise enforcement for that key:
       "disableBypassPermissionsMode": "unmanaged"
       "model": "unmanaged"
  3. In team-mappings.json, map the team file to one or more team slugs:
       ai-users.json  -> [teams that completed AI training]
       devs.json      -> [dev-role teams]

Precedence:
  - Non-overridable keys: enterprise value always applies (ceiling).
  - Overridable/unmanaged keys: team value applies if set, else enterprise
    default applies (floor).
  - Multi-team users: for each key, the least-restrictive value across the
    user's teams is combined, then applied beneath the enterprise file.

Additive-only keys (different mechanism from overridable):
  enabledPlugins, extraKnownMarketplaces
  - Enterprise baseline is guaranteed everywhere.
  - Team files can only ADD entries, never remove/shrink the baseline.
```
*Source: synthesized directly from the changelog's prose description (see Claims
4-10 above for verbatim quotes). GitHub did not publish a single consolidated JSON
code block for this feature in the changelog body — this is a structural summary of
the mechanism, not a verbatim code excerpt. The Assayer should verify exact file/key
names against the live changelog and linked documentation before treating this block
as a citable schema.*

### Enterprise-Managed Settings Capability Map (updated to August 3, 2026)

```
Configuration surface: .github-private source-org repository
Enterprise file:  copilot/managed-settings.json  (legacy compat: .github/copilot/settings.json)
Team files:       copilot/teams/*.json  (NEW)
Team routing:     team-mappings.json  (NEW)
License required: Copilot Business or Copilot Enterprise (issued by enterprise or one
                   of its organizations)

Capabilities announced to date:
1. Plugin distribution (June 5, 2026) — VS Code 1.122+
   Source: docs-github-copilot-enterprise-managed-plugins-vscode.md
2. Hooks/MCP "always enabled" governance (June 5, 2026) — VS Code 1.122+
   Source: docs-github-copilot-enterprise-managed-plugins-vscode.md
3. disableBypassPermissionsMode (June 17, 2026) — VS Code 1.122+
   Source: docs-github-copilot-enterprise-bypass-permissions.md
4. strictKnownMarketplaces (June 25, 2026, public preview) — VS Code + CLI
   Source: docs-github-copilot-enterprise-strict-known-marketplaces.md
5. model: auto default (July 1, 2026) — VS Code 1.126+
   Source: docs-github-copilot-enterprise-auto-model-default.md
6. Team-level specialization (August 3, 2026) — VS Code, CLI, Copilot App,
   Copilot cloud agent  ← THIS NOTE
   - overridable keys (permissions.model, permissions.disableBypassPermissionsMode)
   - additive keys (enabledPlugins, extraKnownMarketplaces)
   - team-mappings.json routing, copilot/teams/ file location
   Source: docs-github-copilot-enterprise-team-specialization-managed-settings.md

Verification path (prior capabilities): Agents page -> AI controls ->
  GitHub Enterprise settings (not independently reconfirmed for team specialization
  in this changelog; presumed same surface, not verified)
```
*Source: synthesis across all six enterprise-managed-settings source notes to date,
listed in chronological order of changelog publication.*

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-enterprise-auto-model-default.md` Claim 8: that note
    independently documented `model` and `disableBypassPermissionsMode` as sibling
    keys nested under a `permissions` object in `managed-settings.json`, based on a
    July 1, 2026 linked docs page. This changelog's worked example (Claim 6, both keys
    specialized together in one team file) and the linked docs excerpt (Claim 12) are
    consistent with that same nesting a month later.
  - `docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 3: the
    `.github-private` source-org repository, version-controlled and PR-manageable,
    continues to be the single configuration surface for all enterprise Copilot
    governance — team files and `team-mappings.json` are added to the same surface
    rather than a new one.
  - `docs-github-copilot-enterprise-bypass-permissions.md` Claims 6-8 and
    `docs-github-copilot-enterprise-auto-model-default.md` Claims 5, 7: the
    Copilot Business/Copilot Enterprise license gate is reconfirmed as the floor for
    this capability, now stated as "issued from the enterprise or one of its
    organizations" — the most explicit statement in the corpus of how the license
    scope resolves for multi-organization enterprises.

- **Extends**:
  - `docs-github-copilot-enterprise-managed-plugins-vscode.md`: the June 5 note
    established `.github-private/.github/copilot/settings.json` as a single,
    enterprise-uniform configuration file with two capability categories (plugin
    distribution, hooks/MCP governance). This source breaks that uniformity
    assumption — for the first time, the *same* configuration file system supports
    different effective values for different sub-populations (teams) of the same
    enterprise, not just different values across separate organizations.
  - `docs-github-copilot-enterprise-bypass-permissions.md` and
    `docs-github-copilot-enterprise-auto-model-default.md`: both notes documented
    `disableBypassPermissionsMode` and `model` respectively as enterprise-wide,
    single-value controls with no mechanism for exceptions below the enterprise level.
    This source adds exactly that missing exception mechanism for those two named
    keys via `overridable`/`"unmanaged"`.
  - `docs-github-copilot-enterprise-strict-known-marketplaces.md`: that note
    documented `strictKnownMarketplaces` as an enterprise-wide whitelist restricting
    plugin installation to explicitly defined marketplaces, described as "deny all not
    explicitly permitted." This source's `extraKnownMarketplaces` additive team key
    appears to be a distinct, differently-named key that lets teams add marketplaces
    on top of the enterprise baseline — see Extraction Notes for the open question of
    how `extraKnownMarketplaces` interacts with a `strictKnownMarketplaces` whitelist
    if an enterprise has both configured.
  - `docs-github-copilot-org-targeted-model-rules.md` (issue #957): that note
    documented per-*organization* model targeting as an enterprise governance
    primitive — a different sub-enterprise unit (org) than this source's per-*team*
    specialization. An enterprise with multiple organizations, each with multiple
    teams, now potentially has two independent, unreconciled axes of model-access
    customization (org-level targeted model rules vs. team-level `overridable` model
    key) that this changelog does not describe as interacting with one another.

- **Contradicts**: None filed as a formal contradiction issue. Two open interaction
  questions are noted (not filed, per MINER.md §4a's guidance that differences in
  scope/context are conditioning variables, not contradictions, unless they would lead
  to materially different guide advice on the same claim):
  1. Whether team-level `extraKnownMarketplaces` can add marketplaces beyond what an
     enterprise-level `strictKnownMarketplaces` whitelist permits, or whether
     `strictKnownMarketplaces` caps what `extraKnownMarketplaces` can add. Neither
     source states the interaction; this is a gap, not a disagreement between the two
     sources.
  2. Whether org-level targeted model rules (`docs-github-copilot-org-targeted-model-rules.md`)
     and team-level `overridable` model specialization (this source) are evaluated in
     a defined order when both apply to the same user. Neither source references the
     other. If future guide-impact work surfaces evidence that these two mechanisms
     produce conflicting model access for the same user, that would warrant a
     contradiction issue at that point — not yet warranted from this extraction alone.

- **Novel**:
  - **Team as a governance unit within enterprise-managed settings**: no prior corpus
    source documents any sub-enterprise, sub-organization targeting unit for Copilot
    governance. Prior differentiation was enterprise-wide (Claims across all four
    earlier notes) or per-organization (`docs-github-copilot-org-targeted-model-rules.md`).
    Team-level specialization is a third, finer-grained axis.
  - **`overridable` key marker syntax**: `{ "overridable": <value> }` is the first
    documented mechanism in the corpus for an admin to explicitly designate which
    specific enterprise-managed keys are eligible for delegated override, as opposed
    to all-or-nothing enterprise enforcement.
  - **`"unmanaged"` as an explicit team-level opt-out value**: distinct from simply
    omitting a key; this is the first corpus documentation of a sentinel value used to
    signal "this team sets its own policy" for an otherwise-enterprise-controlled key.
  - **`enabledPlugins` / `extraKnownMarketplaces` as named additive-only keys**: first
    corpus documentation of a schema field with additive-only (never-shrinking)
    combination semantics, distinct from the replace-or-fallback semantics of
    `overridable` keys.
  - **`team-mappings.json` many-to-one routing**: first corpus documentation of a
    settings-file-to-team routing table decoupling policy content from policy
    audience.
  - **"Least restrictive value wins" multi-team combination rule**: first corpus
    documentation of an explicit conflict-resolution rule for users with overlapping
    team memberships — a concrete, security-relevant detail (Claim 10) that has no
    precedent in the four prior enterprise-managed-settings notes, all of which assumed
    a single enterprise-wide value with no combination logic.
  - **Copilot App and Copilot cloud agent added to the enforced-client list**: prior
    notes documented enforcement only in VS Code and Copilot CLI; this is the first
    corpus mention of `managed-settings.json` enforcement extending to the Copilot App
    and Copilot cloud agent, alongside a forward-looking commitment to broaden this via
    the Copilot SDK.

## Guide Impact

- **Chapter 02 (Harness Engineering — Enterprise Configuration)**:
  - Add a new subsection on team-level specialization within enterprise-managed
    settings, using the "Concrete Artifacts" mechanism summary and capability map
    above as the suggested structure. This is the sixth documented capability in the
    `managed-settings.json` system and the first to introduce a delegation model rather
    than a single new enterprise-wide control.
  - Document the `overridable` / `"unmanaged"` mechanism explicitly, including the
    worked example (`disableBypassPermissionsMode`, `model`) and the fact that only
    admin-designated keys are eligible — teams cannot self-elect into overriding a
    non-overridable key.
  - Document `enabledPlugins` / `extraKnownMarketplaces` as additive-only keys,
    distinct in kind from `overridable` keys — the guide should not conflate "team can
    set its own value" with "team can add to the enterprise baseline," as these are two
    different mechanisms in the same schema.
  - Flag the open interaction question between `extraKnownMarketplaces` (this source)
    and `strictKnownMarketplaces` (`docs-github-copilot-enterprise-strict-known-marketplaces.md`)
    as an unresolved schema question worth verifying against live documentation before
    the guide makes a definitive claim about whether team-added marketplaces can exceed
    an enterprise whitelist.

- **Chapter 04/05 (Governance & Team Adoption — Enterprise Controls)**:
  - Add team-level specialization as a new governance pattern: "central guardrails,
    per-team exceptions within admin-defined limits." This is a materially different
    governance shape than the org-level targeted model rules
    (`docs-github-copilot-org-targeted-model-rules.md`) — teams are typically a finer
    unit than organizations, so this is likely the mechanism guide readers reach for
    when the customization need is "this specific squad/role needs different settings,"
    not "this entire subsidiary/BU needs different settings."
  - Add the "least restrictive value wins" multi-team combination rule (Claim 10) as a
    required governance review item. Recommend that enterprises adopting overridable
    keys for security-sensitive settings (especially `disableBypassPermissionsMode`)
    explicitly audit team membership overlap before granting any team the ability to
    set that key to `"unmanaged"`, since a single dual-membership user can silently
    inherit the more permissive of two teams' settings.
  - Add the PR-driven, user-suggested maintenance model (Claim 3 — `.github-private` at
    `internal` visibility, users can open PRs) as a concrete adoption practice for
    keeping team-scoped governance current, distinct from the admin-only model implied
    for the enterprise-wide file in earlier notes.

- **Chapter 06/07 (Safety & Security / Enterprise Operations)**:
  - Add the least-restrictive-wins combination rule to the enterprise security
    hardening checklist as a specific failure mode to test for: an enterprise that
    correctly locks down `disableBypassPermissionsMode` at the enterprise level, then
    grants one low-risk team an `"unmanaged"` override for legitimate reasons, may
    inadvertently grant that same override to any user who is also a member of an
    unrelated, higher-risk team — without any single admin action that looks like a
    security regression.

## Extraction Notes

1. **WebFetch AI-processing caveat**: Both the changelog and the linked documentation
   page were retrieved via WebFetch, which processes HTML through an AI model before
   returning text, rather than returning raw HTML. The changelog fetch explicitly
   returned content structured as a clean prose reproduction with headers matching the
   page's own section structure (title, body, "What you can do" bullets, "Supported
   clients"), and the quotes used in Claims 1-11 are taken directly from that returned
   text. The Assayer should spot-check these quotes against the live source URL
   (https://github.blog/changelog/2026-08-03-enterprise-team-specialization-for-managed-settings)
   for character-level accuracy, consistent with the verification practice in all four
   prior notes in this family.
2. **Linked docs page returned a summary, not raw text**: the second WebFetch call (to
   the enterprise-managed-settings reference page, `#applying-different-settings-to-enterprise-teams`
   anchor) returned an explicitly structured summary ("According to the documentation...")
   rather than a verbatim reproduction, and no directly quotable sentence was
   recoverable for Claim 12. That claim is rated `emerging` and its quote field is left
   empty rather than fabricated, per MINER.md §2a. The Assayer should independently
   fetch this documentation page if higher-confidence verification of the
   `permissions.model` / `permissions.disableBypassPermissionsMode` schema location is
   needed.
3. **No single consolidated JSON code block in the changelog**: unlike some prior
   entries in this family (e.g., the auto-model-default note's `permissions` object
   example), this changelog describes the `overridable` syntax, `team-mappings.json`,
   and `copilot/teams/` mechanism entirely in prose, without a rendered JSON example in
   the body text as fetched. The "Concrete Artifacts" mechanism summary above is
   therefore a structural synthesis of the prose description, explicitly marked as such
   and not presented as a verbatim code excerpt.
4. **No explicit public-preview label observed**: several prior notes in this family
   (`strict-known-marketplaces`, at minimum) explicitly stated public-preview status in
   the changelog body. The text returned for this changelog does not contain an
   explicit preview/GA label. This is noted as a gap rather than inferred either way —
   the Assayer should check the live page for a status badge or "Who can use this"
   section that may not have been surfaced by WebFetch.
5. **Community discussion not re-fetched**: the linked discussion
   (`github.com/orgs/community/discussions/199139`) is the same general
   enterprise-managed-settings thread already characterized as off-topic-for-specific-features
   in `docs-github-copilot-enterprise-auto-model-default.md` (Extraction Note 3). Since
   that thread predates this August 3 feature, it was not re-fetched for this
   extraction; a future miner covering a subsequent changelog in this family should
   check whether team-specialization-specific discussion has since been added to it.
6. **No contradiction issue filed**: per MINER.md §4a, the two open interaction
   questions identified in Cross-References → Contradicts (marketplace whitelist vs.
   additive team marketplaces; org-level vs. team-level model targeting precedence) are
   gaps in stated interaction between complementary mechanisms, not opposing claims by
   two sources about the same fact. Filing a contradiction issue was judged premature;
   both are flagged prominently for a future source or Smith synthesis pass to resolve
   if evidence of an actual conflict emerges.
