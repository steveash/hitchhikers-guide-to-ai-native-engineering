---
source_url: https://github.blog/changelog/2026-08-26-global-model-policy-generally-available
source_type: docs
title: "Global model policy generally available"
author: GitHub (official changelog)
date_published: 2026-08-26
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: settled
issue: "#2992"
---

# Global Model Policy Generally Available

> GitHub's August 26, 2026 changelog announces the gradual enforcement rollout (through
> September 1) of a default model enablement policy for GA Copilot models on Business/Enterprise
> plans, replacing per-model manual enablement with a global "Delegate to default policy" state
> that dynamically tracks an admin-set enterprise/org policy — while a linked GitHub Community
> discussion (authored by GitHub product staff) reveals a second, not-yet-corpus-documented
> preview feature, "Enterprise teams targeting" (July 30, 2026+), that adds per-model
> enable/disable/optional targeting at the enterprise-team level with a "least restrictive wins"
> multi-team combination rule.

## Source Context

- **Type**: docs (GitHub official product changelog, August 26, 2026; tagged "Improvement",
  2-minute read, tags `copilot` and `enterprise management tools`). Two linked pages followed
  per MINER.md §1: the documentation page "About default availability of Copilot models"
  (`docs.github.com/enterprise-cloud@latest/copilot/concepts/models/default-availability`),
  and the linked GitHub Community discussion #203163 ("Copilot models policy update - default
  on and enterprise teams targeting"), which contains the original staff-authored feature
  announcement this changelog is the GA/enforcement follow-up to. Both the changelog HTML and
  the discussion HTML were fetched and parsed directly (not only via AI-summarizing WebFetch),
  so the quotes below are character-verified against the live source, not AI-paraphrased.
- **Author credibility**: GitHub engineering/product team announcing a production policy change
  to the enterprise Copilot model-governance system. The changelog itself is authoritative for
  the rollout schedule, the four model states, and the excluded-model categories. The linked
  Community discussion's opening post is authored by GitHub account `gpadak` under discussion
  type "Product Feedback," posted July 27, 2026 — the WebFetch AI summary characterized this
  account as GitHub staff/a product manager, but no "Staff" badge was independently confirmed in
  the raw HTML (see Extraction Notes). Treat the discussion content as a credible staff
  product-feedback announcement, one step below the changelog's confirmed-authoritative status.
- **Scope**: Covers the enforcement rollout (Aug 26–Sept 1, 2026) of a global default-enablement
  policy for GA Copilot models on Business/Enterprise plans, the resulting four-state model
  taxonomy, and the model categories permanently excluded from default enablement. The linked
  discussion additionally covers a separate "Enterprise teams targeting" preview (July 30,
  2026+) for per-model access differentiation by enterprise team. Does NOT cover: how this
  global policy interacts precedence-wise with the org-level "targeted model rules" documented
  in `docs-github-copilot-org-targeted-model-rules.md` (issue #957) when both apply to the same
  organization, API/programmatic configuration (explicitly flagged as missing by community
  commenters), or adoption/usage data.

## Extracted Claims

### Claim 1: GitHub is gradually rolling out enforcement (through September 1, 2026) of a default model policy for GA Copilot models on Business/Enterprise plans that it announced in July 2026, so the policy will take effect at different times for different enterprises
- **Evidence**: Official GitHub changelog, opening summary paragraph.
- **Confidence**: settled (product fact, official changelog, character-verified from raw HTML)
- **Quote**: "In July, we announced a default model policy for generally available GitHub Copilot models on Copilot Business and Copilot Enterprise plans. Starting today, we're gradually rolling out enforcement of the policy through September 1, so it will take effect at different times for different enterprises."
- **Our assessment**: This changelog is explicitly a rollout/enforcement milestone for a policy announced the prior month, not a brand-new feature. The staggered per-enterprise rollout means two enterprises checking their Copilot model settings on the same day in late August could see different effective states — a practical detail worth flagging for Ch05 readers auditing governance settings during this window.

### Claim 2: Models an enterprise/organization hasn't previously configured will change state to "Delegate to default policy" and begin following the policy setting; if the policy is enabled (the default), those models become available to users
- **Evidence**: Official changelog, "What's changing" section.
- **Confidence**: settled (character-verified from raw HTML)
- **Quote**: "Models you haven't previously configured will change their state to \"Delegate to default policy\", and they'll begin following your policy setting. If your policy is enabled — which is the default — those models will become available to your users."
- **Our assessment**: This is the core behavioral change: previously-unconfigured GA models silently flip from (implicitly) unavailable to available once enforcement reaches an enterprise, unless the admin has disabled the default-enablement policy itself. Enterprises that have never touched model settings and assumed new models stay off until explicitly enabled will see new/unconfigured models switch on during this rollout window — this is an opt-out, not opt-in, default.

### Claim 3: "Delegate to default policy" is a live, dynamic state that always tracks the policy setting — changing the policy at any time causes all applicable models to follow the change
- **Evidence**: Official changelog, "What's changing" section, second bullet.
- **Confidence**: settled (character-verified from raw HTML)
- **Quote**: "\"Delegate to default policy\" is a live, dynamic state that always tracks your policy. You can change the policy at any time, and all applicable models follow that state change."
- **Our assessment**: This distinguishes "Delegate to default policy" from a one-time inherited value — it's a standing subscription to future policy changes, not a snapshot taken at configuration time. Toggling the enterprise default-availability policy off retroactively disables every model still in this delegated state, without an admin having to touch each model individually. This is the mechanism's main operational value (bulk control) and its main audit risk (a single policy toggle silently changes availability for an unbounded, growing set of unconfigured models).

### Claim 4: Explicit model choices are always preserved — deliberately enabled or disabled models are not changed by the policy rollout
- **Evidence**: Official changelog, "What's changing" section, third bullet.
- **Confidence**: settled (character-verified from raw HTML)
- **Quote**: "We always preserve explicit choices. If you've deliberately enabled or disabled a specific model, we do not change that setting."
- **Our assessment**: This is the safety valve for the opt-out default described in Claim 2 — the rollout cannot silently override a prior explicit admin decision, only the "unconfigured" residual category. For Ch05: this means the risk surface of Claim 2 is bounded to models an enterprise has genuinely never made a decision about, not a wholesale reset of existing configuration.

### Claim 5: Open-weight models (e.g., DeepSeek and Kimi K2) and models not covered by GitHub's data retention agreement (e.g., Fable 5) are excluded from default enablement regardless of the enterprise's policy setting
- **Evidence**: Official changelog, "What's changing" section, fourth bullet; corroborated and extended with more specific model examples by the linked documentation page.
- **Confidence**: settled (changelog text character-verified from raw HTML; docs page also raw-HTML-verified, giving a longer example list)
- **Quote**: "We exclude open-weight models (e.g., DeepSeek and Kimi K2) and models not covered by GitHub's data retention agreement (e.g., Fable 5) from default enablement, regardless of your policy."
- **Our assessment**: This is a hard-coded carve-out that a permissive global policy cannot override — these model categories require an explicit admin opt-in no matter what. The linked docs page (see Claim 8) gives a more granular list (Pre-GA models; open-weight models named as DeepSeek, Kimi K2.7 Code, and Kimi K3; "Claude Fable 5" specifically rather than just "Fable 5"; and models incompatible with data-residency/FedRAMP restrictions), suggesting the changelog's examples are illustrative, not exhaustive, and the docs page is the source of truth for the full exclusion list.

### Claim 6: After the rollout, each model in an enterprise's/organization's settings shows one of four states: Enabled, Disabled, Delegate to enterprise teams/apps or organizations, or Delegate to default policy
- **Evidence**: Official changelog, "What's changing" section, state definitions.
- **Confidence**: settled (character-verified from raw HTML)
- **Quote**: "Enabled: You've explicitly turned the model on. Disabled: You've explicitly turned the model off. Delegate to enterprise teams/apps or organizations: The model follows a setting inherited from your enterprise team or organization. Delegate to default policy: The model follows your default enablement policy."
- **Our assessment**: This is a genuinely new four-state taxonomy, and it appears to supersede the two-state "Enabled"/"Optional" model-availability taxonomy documented in `docs-github-copilot-org-targeted-model-rules.md` (issue #957, Claim 3) as of May 26, 2026. "Delegate to enterprise teams/apps or organizations" looks like the successor to that note's "Optional" state (org/team discretion), while "Delegate to default policy" is the wholly new state introduced by this changelog for models nobody has configured at any level. This reads as product terminology evolving over three months rather than a disagreement between sources — see Cross-References.

### Claim 7: GitHub is soliciting community feedback on making the global model policy state an explicit decision and potentially removing the "Delegate to default policy" state, to ensure every policy reflects an intentional choice rather than an inferred one
- **Evidence**: Official changelog, "What's next" section.
- **Confidence**: emerging (a stated future direction, not a shipped change — GitHub is explicitly asking for input, not announcing a decision)
- **Quote**: "We're evaluating making the global model policy state an explicit decision and removing the \"Delegate to default policy\" state. This would help ensure that every policy reflects an explicit, intentional choice rather than an inferred one."
- **Our assessment**: Notable because it signals GitHub itself sees a governance downside in its own new "Delegate to default policy" state (Claim 2/3) — an inferred rather than deliberate policy outcome — barely a month after the July announcement. For Ch05: guide advice on this feature should flag it as actively evolving; the four-state model in Claim 6 may not be stable, and enterprises that build governance documentation or tooling around "Delegate to default policy" should expect the state to potentially disappear in a future changelog.

### Claim 8: The "Default availability for released models" policy applies only to models an enterprise/organization has not explicitly configured, which are marked with a "Delegate to Default Policy" label; new models inherit this default until explicitly configured, and the models permanently excluded are: pre-GA models, open-weight models (DeepSeek, Kimi K2.7 Code, Kimi K3), models not covered by GitHub's data retention agreement (Claude Fable 5), and — for enterprises restricted to data-resident or FedRAMP-compliant models — any model that doesn't respect those constraints
- **Evidence**: Linked documentation page "About default availability of Copilot models," fetched as raw HTML.
- **Confidence**: settled (character-verified from raw HTML of the linked docs page)
- **Quote**: "The following models are not in scope. They are disabled by default, regardless of your \"Default availability\" policy setting. Pre-GA models. Open weight models (DeepSeek, Kimi K2.7 Code, Kimi K3). Models that are not covered by GitHub's data retention agreement (Claude Fable 5). For enterprises that have restricted models to data-resident or FedRAMP-compliant models, any models that do not respect these policies."
- **Our assessment**: This is the authoritative, more complete version of Claim 5's exclusion list. Two additions not in the changelog itself: (1) pre-GA models are excluded — meaning the global policy is strictly scoped to GA models and cannot accidentally enable a preview/beta model; (2) a fourth exclusion category for data-residency/FedRAMP-restricted enterprises, layering an additional compliance filter on top of the open-weight/data-retention exclusions. For Ch05: this fourth category means enterprises operating under data-residency or FedRAMP constraints have a materially different effective default-enablement surface than a standard Business/Enterprise customer, even with the same global policy setting.

### Claim 9: Admins can prevent default enablement entirely by disabling the "Default availability for released models" policy at the enterprise or organization level, or keep the policy enabled while explicitly disabling individual models; the policy can be set enterprise-wide or disabled only in organizations with stricter compliance requirements
- **Evidence**: Linked documentation page, "How do I prevent default enablement?" section.
- **Confidence**: settled (character-verified from raw HTML of the linked docs page)
- **Quote**: "To disable default enablement entirely, disable the Default availability for released models policy in your enterprise or organization's models policies. You can set a policy for the entire enterprise, or disable the policy only in organizations with stricter compliance requirements. If you keep the Default availability for released models policy enabled, you can explicitly disable individual models so that they are not eligible for automatic enablement."
- **Our assessment**: This confirms the policy can be scoped at either the enterprise level or overridden per-organization — a governance shape consistent with the layered enterprise/org model already documented in `docs-github-copilot-org-targeted-model-rules.md`. Practically, this gives risk-averse organizations within a generally permissive enterprise (or vice versa) an escape hatch without requiring the whole enterprise to adopt the stricter posture.

### Claim 10: GitHub recommends keeping up with new model releases via its changelog so admins can proactively choose enablement settings for each new model, rather than relying on the default policy
- **Evidence**: Linked documentation page, "How do I prepare for new models?" section.
- **Confidence**: settled (character-verified from raw HTML of the linked docs page)
- **Quote**: "We recommend keeping up with new model releases so you can choose your enablement settings for each one. New models are announced on GitHub's changelog."
- **Our assessment**: This is GitHub's own documentation acknowledging that relying on the default policy (rather than actively reviewing each new model) is the passive option, with an implicit recommendation against it for governance-conscious admins. For Ch05: pair this with Claim 7 — GitHub's own stated unease with "inferred" policy outcomes reinforces that the guide should recommend active per-model review as the default operating posture, treating "Delegate to default policy" as a stopgap rather than an end state.

### Claim 11: A separate, not-yet-GA "Enterprise teams targeting" preview (launching July 30, 2026) lets admins set a baseline of available models for the entire enterprise and then allow additional models to specific enterprise teams, differentiating access by job role, training level, or experimentation status; at the enterprise level each model can be enabled (all members), disabled (no members), or optional (assignable to enterprise teams)
- **Evidence**: Opening post of GitHub Community discussion #203163, authored by GitHub account `gpadak`, posted July 27, 2026, under discussion type "Product Feedback"; linked from this changelog's "What's next" section. Fetched as raw HTML, not AI-summarized.
- **Confidence**: emerging (a public preview feature, not yet GA; sourced from a Community discussion post rather than a changelog or docs page, though the poster identifies as announcing the feature on GitHub's behalf)
- **Quote**: "Enterprise teams targeting - public preview July 30th+ ... We are launching a preview that changes models policy to directly support user-based governance flows. AI administrators can set a baseline of available models for the entire enterprise, and then allow additional models to specific enterprise teams. This allows model access differentiation based on job role, training level, or experimentation with new models by frontier teams. At the enterprise level, models can be: enabled: available to all members of the enterprise. disabled: not available to any member of the enterprise. optional: models are available to be assigned to enterprise teams."
- **Our assessment**: This is a materially different feature from the global default-policy enforcement this changelog announces (Claims 1–8) — it targets enterprise *teams* (a sub-enterprise unit) rather than a single enterprise-wide policy state. It is also a different targeting axis from the org-level "targeted model rules" in `docs-github-copilot-org-targeted-model-rules.md` (issue #957): that source lets an enterprise differentiate model access by *organization*; this discussion describes differentiation by *enterprise team*. Neither this discussion nor the org-targeted-model-rules note describes how the two interact if both are configured for the same user. Not previously documented anywhere in the corpus — see Cross-References → Novel.

### Claim 12: Enabling the Enterprise teams targeting preview is opt-in and replaces the customer's existing models policy and organization (resource-based) decisions in favor of enterprise teams, via an "Enterprise teams mode" toggle; turning the toggle off rolls back to the customer's last configuration
- **Evidence**: Same discussion post, "This is an opt-in preview" section.
- **Confidence**: emerging (preview feature, Community-discussion source)
- **Quote**: "Enabling this preview will replace a customers' existing models policy and organization (resource-based) decisions in favor of enterprise teams. There is a toggle to turn on \"Enterprise teams mode\" that will allow you to get started. The rollback strategy is to turn off \"Enterprise teams mode\", which will reset the customer's policy to the last configuration."
- **Our assessment**: This is a significant operational detail: enabling the preview does not layer on top of existing org-level "targeted model rules" (issue #957) — it *replaces* org-level resource-based model decisions with team-based ones. An enterprise that has already invested in per-organization targeted model rules would need to understand that flipping on Enterprise teams mode supersedes that configuration, not augments it. The rollback path (toggle off, revert to last configuration) is stated but not detailed — whether "last configuration" means the pre-toggle org-level rules are fully restored, or only approximately restored, is not addressed by the source.

### Claim 13: When a user belongs to multiple enterprise teams, Enterprise Teams model access evaluates using a least-restrictive strategy — if the user gets a model from any one enterprise team, they have access to that model everywhere
- **Evidence**: Same discussion post, describing the combination rule for the Enterprise teams targeting preview.
- **Confidence**: emerging (preview feature, Community-discussion source)
- **Quote**: "Enterprise Teams model access evaluates in a least-restrictive strategy, which means that if a user gets a model from any one enterprise team the user will have access to the model everywhere."
- **Our assessment**: This corroborates a pattern already documented for a *different* enterprise-team mechanism in `docs-github-copilot-enterprise-team-specialization-managed-settings.md` (issue #2473, Claim 10), which independently states that multi-team `managed-settings.json` overridable-key combination also uses "the least restrictive value for each key." That source governs general `managed-settings.json` keys (e.g., `permissions.model`, `permissions.disableBypassPermissionsMode`); this source governs per-model enable/disable/optional policy specifically. Two GitHub sources one week apart (this discussion posted July 27, 2026; the managed-settings changelog published August 3, 2026) describe "least restrictive wins" for multi-team membership across two different enterprise-team-scoped mechanisms. That proximity cuts against reading them as independent confirmations: a week apart is consistent with a single internal design decision surfacing in two nearly-simultaneous shipping vehicles, so this is better treated as one design choice observed twice than as two data points — worth watching as a possible standing design principle, but not establishing one. The corpus already complicates the generalization: `docs-github-copilot-mcp-allowlists-enterprise.md` (issue #2564, Claims 9 and 11) documents GitHub using the *opposite*, most-restrictive-wins operators (allow = intersection, deny = union) for combining `allowedMcpServers`/`deniedMcpServers` across settings *sources*, in the same managed-settings schema whose team-level `overridable` mechanism is governed by the least-restrictive rule (that note's Claim 5). Those are different combination axes — multi-team membership vs. multi-source layering — and that note explicitly declines to resolve how they interact, filing it as an open question rather than a contradiction (its Cross-References → Contradicts). So the honest reading is narrower: least-restrictive appears to be GitHub's rule for the *multi-team-membership* axis specifically, not a blanket enterprise-teams design principle, and this source is a second data point for that narrower claim. For Ch05: this still reinforces the guide's existing recommendation (from issue #2473's Guide Impact) to treat team-membership overlap as a standing governance audit item, with two mechanisms now exhibiting the same risk shape — a user in both a locked-down team and a permissive team inherits the permissive team's access — while inheriting issue #2564's open caveat that the multi-team rule's interaction with multi-source combination is undocumented.

## Concrete Artifacts

### Changelog full text (verbatim, raw HTML, August 26, 2026)

```
Title: Global model policy generally available
Published: August 26, 2026 (Improvement, 2 minute read)
Tags: copilot, enterprise management tools
Source: https://github.blog/changelog/2026-08-26-global-model-policy-generally-available

[Summary]
In July, we announced a default model policy for generally available GitHub Copilot
models on Copilot Business and Copilot Enterprise plans. Starting today, we're
gradually rolling out enforcement of the policy through September 1, so it will take
effect at different times for different enterprises. Previously unconfigured and new
generally available models will inherit the global policy state. Administrators can
make durable decisions for individual models at their discretion. Open-weight models
and any models that require data retention are disabled by default.

[What's changing]
Once the policy takes effect for your organization or enterprise:
- Models you haven't previously configured will change their state to "Delegate to
  default policy", and they'll begin following your policy setting. If your policy is
  enabled — which is the default — those models will become available to your users.
- "Delegate to default policy" is a live, dynamic state that always tracks your
  policy. You can change the policy at any time, and all applicable models follow
  that state change.
- We always preserve explicit choices. If you've deliberately enabled or disabled a
  specific model, we do not change that setting.
- We exclude open-weight models (e.g., DeepSeek and Kimi K2) and models not covered
  by GitHub's data retention agreement (e.g., Fable 5) from default enablement,
  regardless of your policy.

After the rollout, each model in your settings shows one of four states:
- Enabled: You've explicitly turned the model on.
- Disabled: You've explicitly turned the model off.
- Delegate to enterprise teams/apps or organizations: The model follows a setting
  inherited from your enterprise team or organization.
- Delegate to default policy: The model follows your default enablement policy.

To learn more, see default model availability.
  -> https://docs.github.com/enterprise-cloud@latest/copilot/concepts/models/default-availability

[What's next]
We are looking for your feedback in the community discussion below. We're evaluating
making the global model policy state an explicit decision and removing the "Delegate
to default policy" state. This would help ensure that every policy reflects an
explicit, intentional choice rather than an inferred one.
Join the discussion within GitHub Community.
  -> https://github.com/orgs/community/discussions/203163
```

### Linked docs page full text (verbatim, raw HTML: "About default availability of Copilot models")

```
Who can use this feature? Copilot Business and Copilot Enterprise

For enterprises with Copilot Business or Copilot Enterprise plans, the Default
availability for released models policy controls whether unconfigured generally
available (GA) models default to enabled or disabled. If this policy is enabled,
users benefit from the latest models without the need for administrator
intervention.

Which models follow the policy?
The default policy applies to models that you have not explicitly configured. These
models are indicated in your enterprise or organization's model settings with the
Delegate to Default Policy label. When a new model is released, it inherits the
default until you explicitly configure it.

The following models are not in scope. They are disabled by default, regardless of
your "Default availability" policy setting.
- Pre-GA models
- Open weight models (DeepSeek, Kimi K2.7 Code, Kimi K3)
- Models that are not covered by GitHub's data retention agreement (Claude Fable 5)
- For enterprises that have restricted models to data-resident or FedRAMP-compliant
  models, any models that do not respect these policies

How do I prevent default enablement?
To disable default enablement entirely, disable the Default availability for
released models policy in your enterprise or organization's models policies. You can
set a policy for the entire enterprise, or disable the policy only in organizations
with stricter compliance requirements.
If you keep the Default availability for released models policy enabled, you can
explicitly disable individual models so that they are not eligible for automatic
enablement.

How do I prepare for new models?
We recommend keeping up with new model releases so you can choose your enablement
settings for each one. New models are announced on GitHub's changelog.

Source: https://docs.github.com/enterprise-cloud@latest/copilot/concepts/models/default-availability
```

### Linked Community discussion opening post (verbatim, raw HTML excerpt, posted July 27, 2026 by `gpadak`)

```
Discussion Type: Product Feedback
Title: Copilot models policy update - default on and enterprise teams targeting
Posted: Jul 27, 2026 by gpadak
Source: https://github.com/orgs/community/discussions/203163

We are simplifying how enterprise customers control access to models in Copilot. The
current policy experience is difficult to understand, difficult to target precisely,
and difficult to evolve as we add more models. For GitHub Enterprise customers that
have Copilot Business or Copilot Enterprise licenses, we are changing a couple things:

Default on global policy for generally available models
We're introducing a global default enablement policy for all GA Copilot models for
Copilot Business and Copilot Enterprise customers. Instead of requiring admins to
manually enable each new model as it ships, models that reach GA will be on by
default with a single opt-out control for enterprises & organizations that need
stricter governance.
Open-weight models and those that require data retention will not be automatically
enabled, regardless of this global policy choice.

Rollout schedule
- July 29, 2026: the global policy is available but does not have effect. Access to
  unconfigured models stay as-is (disabled) for next 28 days.
- August 26th, 2026: Unconfigured models honor the global policy, on or off, and will
  state that they inherit the global policy decision. For most customers, this means
  those unconfigured models become available to their users.

AI administrators are always encouraged to make an explicit enable/disable decision
for every model.

Enterprise teams targeting - public preview July 30th+
We are launching a preview that changes models policy to directly support user-based
governance flows. AI administrators can set a baseline of available models for the
entire enterprise, and then allow additional models to specific enterprise teams.
This allows model access differentiation based on job role, training level, or
experimentation with new models by frontier teams.
At the enterprise level, models can be:
- enabled: available to all members of the enterprise
- disabled: not available to any member of the enterprise
- optional: models are available to be assigned to enterprise teams
Enterprise Teams model access evaluates in a least-restrictive strategy, which means
that if a user gets a model from any one enterprise team the user will have access to
the model everywhere.

This is an opt-in preview
Enabling this preview will replace a customers' existing models policy and
organization (resource-based) decisions in favor of enterprise teams. There is a
toggle to turn on "Enterprise teams mode" that will allow you to get started. The
rollback strategy is to turn off "Enterprise teams mode", which will reset the
customer's policy to the last configuration.

Tell us your thoughts
If you're an administrator, setting AI standards for your business, a developer, or
any user of Copilot Business/Enterprise we'd love to hear from you.
```

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-enterprise-team-specialization-managed-settings.md` (issue #2473,
    Claim 10): that source separately documents a "least restrictive value" multi-team
    combination rule for `managed-settings.json` overridable keys (`permissions.model`,
    `permissions.disableBypassPermissionsMode`), published August 3, 2026. This note's Claim 13
    documents the same "least-restrictive wins" combination rule for a *different* mechanism
    (per-model enterprise-team policy, announced in a discussion posted July 27, 2026 for a
    preview launching July 30, 2026+) — one week before that changelog. Two GitHub sources
    describing the identical combination principle across two distinct enterprise-team mechanisms
    makes least-restrictive the likely rule for the *multi-team-membership* axis specifically,
    though their one-week spacing suggests a single design decision shipping through two vehicles
    rather than genuinely independent corroboration — and see the
    MCP-allowlists entry under Extends before generalizing it further; two data points on one
    axis are not yet a demonstrated enterprise-teams-wide design principle, and a third in-corpus
    mechanism in the same schema uses the opposite operators on a neighbouring axis. Claim 13's
    assessment is hedged accordingly.
  - `docs-github-copilot-org-targeted-model-rules.md` (issue #957, Claim 5) and
    `docs-github-copilot-enterprise-auto-model-default.md` (issue #1542, Claim 5): both restate
    Copilot Business/Copilot Enterprise as the license floor for enterprise Copilot model
    governance; this source's linked docs page ("Who can use this feature? Copilot Business and
    Copilot Enterprise," Claim 8) reconfirms the same floor for the global default-policy
    feature specifically.

- **Extends**:
  - `docs-github-copilot-org-targeted-model-rules.md` (issue #957): that May 26, 2026 source
    documented a two-state enterprise-wide model-availability taxonomy ("Enabled" = on for all
    orgs, "Optional" = orgs decide) plus a three-state org-level control (Enabled/Disabled/
    Unconfigured) for "Optional" models. This source's four-state taxonomy (Claim 6) — Enabled,
    Disabled, "Delegate to enterprise teams/apps or organizations," "Delegate to default
    policy" — appears to be the successor terminology three months later: "Delegate to
    enterprise teams/apps or organizations" plausibly corresponds to the old "Optional"/
    "Unconfigured (inherits enterprise default)" states, while "Delegate to default policy" is
    the genuinely new addition (a model that has never been configured at any level now
    delegates to a global policy rather than defaulting to off). This is read as terminology/
    product evolution over time, not a contradiction between two sources describing the same
    point in time — no contradiction issue filed. The Assayer and Smith should treat issue
    #957's two-state description as historical (May 2026) and this note's four-state
    description as current (August 2026 GA).
  - `docs-github-copilot-mcp-allowlists-enterprise.md` (issue #2564, August 6, 2026): that source
    documents a second, independent combination axis inside the *same* enterprise
    `managed-settings.json` schema — when multiple settings *sources* (MDM, server-managed,
    file-based) define the same key, `allowedMcpServers` combines by intersection ("A server must
    be permitted by every source to run," its Claim 9) and `deniedMcpServers` by union ("A server
    blocked by any source is blocked for all," its Claim 11). Both are most-restrictive-wins
    operators, i.e. the opposite posture from the least-restrictive multi-team rule this note's
    Claim 13 documents — and that note's Claim 5 establishes that the MCP keys are themselves
    `overridable` by enterprise teams, so the two axes provably meet in at least one real
    configuration. That note's Cross-References → Contradicts already files this as an explicit
    open question: whether the multi-team "least restrictive wins" rule and the multi-source
    intersection/union rules are evaluated in a defined order for an `overridable`, multi-team,
    multi-layer value. This note does not resolve that question, and its per-model
    enterprise-teams policy (Claims 11–13) adds a *third* mechanism to the same unresolved
    interaction — the discussion post states the multi-team rule without addressing multi-source
    layering at all. Per MINER.md §4a this remains a gap between complementary mechanisms rather
    than a contradiction (no new issue filed; issue #2564's existing caveat covers it), but it is
    the reason Claim 13's generalization is scoped to the multi-team axis only.
  - `docs-github-copilot-enterprise-auto-model-default.md` (issue #1542): that source documents
    an enterprise-level `model: auto` default (which model-selection *mode* a new conversation
    starts in, among already-available models) as a distinct governance layer from model
    *availability* itself. This note's global model policy governs the prior, upstream question
    — whether a given model is available to select at all. The two layers compose: a model must
    first be available (this note) before the `model: auto` default (#1542) or a user's manual
    selection can choose it.

- **Contradicts**: None. No existing corpus source claims that GA model availability defaults to
  disabled for unconfigured models, or that enterprise model governance is limited to a
  two-state taxonomy going forward — the two-state description in issue #957 is superseded by
  product evolution (see Extends above), not disputed as of a shared point in time. No
  contradiction issue required per MINER.md §4a. One pre-existing open question is inherited
  rather than newly raised: `docs-github-copilot-mcp-allowlists-enterprise.md` (issue #2564)
  already flags that the multi-team "least restrictive wins" rule and the multi-source
  intersection/union rules have no stated evaluation order; this note's Claim 13 adds a third
  mechanism governed by the multi-team rule without resolving that interaction. Per that note's
  own reasoning, a contradiction issue would only be warranted if a future source states an
  evaluation order that conflicts with either rule as independently written.

- **Novel**:
  - First corpus source to document the global default-enablement policy's *enforcement*
    rollout (as opposed to its July announcement, which is not independently documented
    elsewhere in the corpus) and the resulting four-state model taxonomy.
  - First corpus source to document the "Delegate to default policy" state as a live, dynamic
    subscription to policy changes (Claim 3) — a materially different mechanism from a
    one-time-inherited default.
  - First corpus source to document GitHub's own stated intent to reconsider/remove the
    "Delegate to default policy" state in favor of forcing explicit decisions (Claim 7) —
    evidence the feature is still actively evolving rather than settled.
  - First corpus source to document the "Enterprise teams targeting" preview (Claims 11–13):
    per-model enable/disable/optional policy scoped to enterprise teams (a sub-enterprise unit),
    distinct from both the org-level targeting in issue #957 and the general-purpose
    `managed-settings.json` team specialization in issue #2473. No prior corpus note documents
    per-model (as opposed to per-key) enterprise-team targeting.
  - First corpus source to document that enabling a new enterprise-team-based governance
    mechanism can *replace* (not layer on top of) an existing org-level ("resource-based")
    configuration (Claim 12) — a migration/precedence detail with no precedent in the prior
    enterprise-managed-settings or targeted-model-rules notes, all of which described strictly
    additive capabilities.

## Guide Impact

- **Chapter 05 (Team Adoption / Enterprise Governance)**:
  - Document the four-state model-availability taxonomy (Claim 6) as the current (August 2026)
    state of enterprise Copilot model governance, explicitly noting it supersedes the two-state
    taxonomy from issue #957 (May 2026) — the guide should not present both as simultaneously
    current without this note.
  - Add the global default-enablement policy itself as a governance decision point: recommend
    enterprises decide, per GitHub's own Claim 10 recommendation, between (a) leaving the policy
    enabled and passively accepting new GA models, or (b) actively reviewing each new model via
    the changelog before enabling it — flagging (a) as the default but administratively passive
    choice, and citing GitHub's own Claim 7 unease with "inferred" policy outcomes as supporting
    evidence for recommending (b) to governance-conscious teams.
  - Document the exclusion list (Claim 8: pre-GA models, named open-weight models, models
    without GitHub's data retention agreement, data-residency/FedRAMP-restricted models) as the
    concrete floor beneath the global policy — useful for enterprises assessing what does *not*
    change no matter how permissive their policy setting is.
  - Add the "Enterprise teams targeting" preview (Claims 11–13) as an emerging (not yet GA)
    governance primitive to watch: per-model access differentiation by enterprise team, using
    the same "least restrictive wins" multi-team rule already documented for
    `managed-settings.json` team specialization (issue #2473). Flag the precedence detail from
    Claim 12 — enabling this preview replaces, rather than layers on, existing org-level
    targeted model rules (issue #957) — as a migration consideration enterprises must plan for
    before opting in, not a default recommendation given its preview status.
  - Cross-link the "least restrictive wins" pattern (this note's Claim 13; issue #2473's Claim
    10) as a single governance audit item spanning two independent mechanisms: any enterprise
    granting differentiated access via enterprise teams (whether per-model or per-`managed-
    settings.json`-key) should audit for multi-team membership overlap, since overlap silently
    grants the more permissive team's access. Present this as the rule for the multi-team axis
    specifically, not as a universal enterprise-teams principle — `docs-github-copilot-mcp-
    allowlists-enterprise.md` (issue #2564, Claims 9 and 11) documents most-restrictive-wins
    operators for the multi-*source* axis of the same schema, and its open question about how the
    two axes combine should be carried into the guide alongside the audit recommendation.

- **Chapter 02 (Harness Engineering / Tooling Landscape)**:
  - Note that model availability (this source) is a distinct, upstream governance layer from
    the `model: auto` default-selection-mode setting (`docs-github-copilot-enterprise-auto-
    model-default.md`, issue #1542) — a harness or CLAUDE.md-equivalent configuration that
    references a specific model name should account for the possibility that the model is
    unavailable under a restrictive global policy, independent of any auto-routing behavior.

## Extraction Notes

1. **Raw HTML fetched directly, not only via AI-summarizing WebFetch**: For this note, both the
   changelog and the linked "default availability" docs page were fetched as raw HTML via
   `curl` and parsed directly (tags stripped, HTML entities decoded), rather than relying solely
   on WebFetch's AI-summarized output. Two independent WebFetch calls to the changelog returned
   inconsistent paraphrased wording for the same passages (e.g., "tracks policy changes"
   vs. "tracks your policy in real-time" for the same sentence), confirming the AI-summarization
   risk flagged in prior notes in this family (`docs-github-copilot-enterprise-auto-model-
   default.md`, `docs-github-copilot-enterprise-team-specialization-managed-settings.md`). All
   quotes in Claims 1–10 and the first two Concrete Artifacts blocks are character-verified
   against the raw HTML retrieved directly, not the WebFetch paraphrases.
2. **Community discussion also raw-HTML-verified**: The linked Community discussion (#203163)
   was similarly fetched as raw HTML rather than relying on the WebFetch AI summary, which had
   conflated docs-page content into its discussion summary and could not be trusted for verbatim
   quotation. The exact opening-post text (Claims 11–13, third Concrete Artifacts block) was
   located and extracted directly from the page's embedded HTML, giving higher confidence than a
   typical Community-discussion citation would normally warrant — but the claims are still rated
   `emerging` rather than `settled` because the underlying feature (Enterprise teams targeting)
   is itself a preview, not GA, regardless of quote-verification confidence.
3. **`gpadak`'s staff status not independently confirmed**: The raw HTML for the discussion page
   did not surface an explicit "Staff" role badge for the `gpadak` account in the markup
   inspected (no `MEMBER`/`OWNER`/`STAFF` association string or badge text was found via
   pattern search). A WebFetch AI-summary pass separately characterized this account as "GitHub
   author/product manager." Given the discussion type ("Product Feedback"), the first-person
   plural voice ("we are simplifying," "we're introducing"), and that this is the exact
   discussion linked from the official changelog's "join the discussion" link, treat the content
   as a credible staff product announcement, but the Assayer should not cite it with the same
   confidence as changelog or docs-page text.
4. **Two other Community triage comments on this issue independently spotted the same rollout
   schedule and Enterprise teams targeting preview**: the Prospector's triage comments on issue
   #2992 (second and third comments) already flagged the four-state model and the July
   announcement/August enforcement relationship; this note's independent raw-HTML read confirms
   those observations and adds the previously-untriaged "Enterprise teams targeting" preview
   detail (Claims 11-13), which none of the three triage comments mentioned by name.
5. **No contradiction issue filed**: see Cross-References → Contradicts. The apparent shift from
   a two-state to a four-state model-availability taxonomy is treated as product evolution over
   a three-month span (May 26 to August 26, 2026), not a disagreement between two sources
   describing the same point in time.
