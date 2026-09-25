---
source_url: https://github.blog/changelog/2026-09-24-default-enablement-of-copilot-features-for-copilot-business-and-enterprise
source_type: docs
title: "Default Enablement of Copilot Features for Copilot Business and Enterprise"
author: GitHub (official changelog)
date_published: 2026-09-24
date_extracted: 2026-09-25
last_checked: 2026-09-25
status: current
confidence_overall: settled
issue: "#3691"
---

# Default Enablement of Copilot Features for Copilot Business and Enterprise

> GitHub's September 24, 2026 changelog introduces a second, sibling global
> default-enablement policy — this one for generally available Copilot
> *features and client capabilities* (as opposed to *models*, which already
> has its own GA policy) — covering the enterprise "Features & clients" page,
> the Copilot Code Review policy, and the MCP servers in Copilot policy, with
> a 28-day pre-enforcement window before it takes effect on October 22, 2026
> and is itself enabled by default.

## Source Context

- **Type**: docs (GitHub official product changelog, September 24, 2026;
  tagged "Improvement," "1 minute read," tags `copilot` and `enterprise
  management tools`). One linked documentation page was followed per
  MINER.md §1: "About default availability of Copilot features and models"
  (`docs.github.com/copilot/concepts/enterprise/default-availability`),
  which turned out to be the same docs page already cited by
  `docs-github-copilot-global-model-policy-ga.md` for the models policy,
  now retitled and expanded to cover the new features policy alongside the
  models policy. A second linked page, the GitHub Community discussion at
  `github.com/orgs/community/discussions/208757`, was also checked but
  contains no substantive comments beyond the initial post and an automated
  bot acknowledgment (see Extraction Notes) — not followed further. Both
  the changelog and the docs page were fetched as raw HTML via `curl` and
  parsed directly (tags stripped, HTML entities decoded), not relied on via
  AI-summarizing WebFetch alone, so quotes below are character-verified
  against the live source.
- **Author credibility**: GitHub engineering/product team announcing a
  production policy change to enterprise/organization Copilot
  administration. Authoritative for the policy's configuration surface, its
  scope (which settings count as "features"), the rollout timeline, and the
  stated exceptions. Not a source for adoption data, why GitHub chose to
  split features and models into two separate policies rather than one, or
  practitioner reaction (the linked discussion has none).
- **Scope**: Covers the new "Default policy for new features" policy: what
  it controls, how to configure it, the three available settings, the
  enterprise/organization cascade behavior, what counts as a "feature" for
  this policy's purposes, and the named exceptions. Does NOT cover: pricing
  or billing impact of any newly-enabled feature, which specific *named*
  features are currently "Unconfigured" and therefore in scope (the
  changelog only says a banner will show the count), or how this policy
  interacts operationally with the separate models policy beyond both being
  described as sibling mechanisms on the same docs page.

## Extracted Claims

### Claim 1: GitHub is introducing a new global default-enablement policy for GA Copilot features and supported client capabilities in enterprise/organization settings, with a 28-day window during which admins can configure it before it has any effect on user access
- **Evidence**: Official GitHub changelog, opening summary paragraph.
- **Confidence**: settled (product fact, official changelog, character-verified from raw HTML)
- **Quote**: "We're introducing a new global default policy for generally available GitHub Copilot features and supported client capabilities in enterprise and organization Copilot settings. For the next 28 days, you can configure this policy, but it won't affect feature access for your users yet."
- **Our assessment**: This is the direct feature-level counterpart to the model-level "Default availability for released models" policy documented in `docs-github-copilot-global-model-policy-ga.md`. The 28-day pre-enforcement window mirrors that policy's own July-announcement/August-enforcement staggered rollout pattern, giving admins a comparable grace period to configure before the policy is live.

### Claim 2: Admins configure the new policy by going to the "AI Controls" page, opening the "Copilot" subpage, and selecting an option under "Default policy for new features"
- **Evidence**: Official changelog, "What's changing" section.
- **Confidence**: settled (character-verified from raw HTML)
- **Quote**: "Today, you can configure the new policy by going to the \"AI Controls\" page, opening the \"Copilot\" subpage, and selecting an option under \"Default policy for new features\"."
- **Our assessment**: This names the exact UI path for the feature policy, giving practitioners a concrete, checkable location distinct from wherever the models policy lives in the same "AI Controls" area — useful for a Ch05 admin checklist entry.

### Claim 3: The feature policy applies to eligible features managed on the enterprise's "Features & clients" page, as well as the Copilot Code Review policy on the "Agents" page and the MCP servers in Copilot policy
- **Evidence**: Official changelog, "What's changing" section, and independently confirmed with near-identical wording by the linked docs page's "What counts as a feature?" section.
- **Confidence**: settled (both changelog and docs page character-verified from raw HTML)
- **Quote**: "This policy applies to eligible features managed on your enterprise's \"Features & clients\" page (i.e., https://github.com/enterprises/YOUR-ENTERPRISE-SLUG/ai-controls/copilot/features), as well as the Copilot Code Review policy on the \"Agents\" page and the MCP servers in Copilot policy."
- **Our assessment**: This is the scope definition practitioners most need: the policy is not limited to whatever appears on the "Features & clients" page — it also silently governs two other named admin surfaces (Copilot Code Review and MCP servers in Copilot). An admin who only audits "Features & clients" before October 22 would miss the Code Review and MCP-servers policies that this same default also touches.

### Claim 4: Admins can choose from three settings for the policy — Enabled (current and future eligible features available by default), Disabled (current features stay unavailable, future ones require admin approval), or Let organizations decide (org admins choose per-organization)
- **Evidence**: Official changelog, enumerated list following "You can choose from the following settings:"
- **Confidence**: settled (character-verified from raw HTML)
- **Quote**: "Enabled: Current and future eligible features will be available to users by default. Disabled: Current eligible features will remain unavailable, and future eligible features will require administrator approval. Let organizations decide: Organization administrators can choose whether to enable or disable eligible features."
- **Our assessment**: This three-option shape (Enabled / Disabled / delegate-to-org) matches the enterprise/organization delegation pattern already used by the models policy's "Delegate to enterprise teams/apps or organizations" and "Let organizations decide"-style states in `docs-github-copilot-global-model-policy-ga.md` Claim 6 — GitHub is reusing a consistent governance vocabulary across the two sibling policies rather than inventing a distinct scheme for features.

### Claim 5: Starting October 22, unconfigured eligible GA features/capabilities follow the selected global default, explicit per-feature decisions are preserved and never overridden, and preview features remain opt-in with existing choices preserved when they later reach GA
- **Evidence**: Official changelog, "Starting October 22, the policy takes effect" bullet list.
- **Confidence**: settled (character-verified from raw HTML)
- **Quote**: "Eligible generally available features and capabilities left Unconfigured will follow your selected global default of enabled, disabled, or let organizations decide. Explicit decisions are preserved. If you've explicitly enabled or disabled a feature, we won't override that choice. Preview features remain opt-in. If you opt into a preview and it later becomes generally available, your existing choice will be preserved."
- **Our assessment**: This is the same "opt-out default, but explicit choices are sacrosanct" behavior already established for the models policy (`docs-github-copilot-global-model-policy-ga.md` Claims 2 and 4) and now confirmed for the deprecation-successor mechanism (`docs-github-copilot-oct2026-model-deprecations.md` Claim 4). GitHub is applying one consistent default-enablement philosophy across models, features, and now feature-adjacent client capabilities.

### Claim 6: The feature default policy does not apply to features that are still in preview — only to GA features and capabilities
- **Evidence**: Linked docs page, "Default availability of features" section.
- **Confidence**: settled (character-verified from raw HTML of the linked docs page)
- **Quote**: "The policy does not apply to features in preview."
- **Our assessment**: This is stated more explicitly on the docs page than in the changelog itself (the changelog only implies it via "Preview features remain opt-in" in Claim 5). It confirms the feature policy, like the models policy's pre-GA exclusion (`docs-github-copilot-global-model-policy-ga.md` Claim 8), is strictly scoped to GA — an admin cannot accidentally have a preview feature switched on by this global default no matter how the policy is configured.

### Claim 7: At the enterprise level the policy applies to features labeled "Unconfigured"; at the organization level it applies only to features an enterprise owner has set to "Let organizations decide" that the organization owner has not itself explicitly configured
- **Evidence**: Linked docs page, "What does the policy do?" section.
- **Confidence**: settled (character-verified from raw HTML of the linked docs page)
- **Quote**: "The policy can be configured in an enterprise and its organizations. At the enterprise level, it applies to features labeled as Unconfigured. At the organization level, it applies to features that an enterprise owner has set to Let organizations decide, but that an organization owner has not explicitly configured."
- **Our assessment**: This is a level of cascade detail the changelog itself does not state — it clarifies that an organization's own default policy setting only ever takes effect for features the enterprise has explicitly delegated via "Let organizations decide"; an enterprise-level "Enabled"/"Disabled" choice is not something an org can override with its own default policy. For Ch05: this is the precise precedence rule admins need before assuming an org-level policy configuration will have any effect.

### Claim 8: Three named policies are explicit exceptions and are not affected by the feature default policy: the GHE.com-only "Restrict Copilot to data residency models" and "Restrict Copilot to FedRAMP models" policies, and "Store local sessions in the Cloud" for Copilot CLI and VS Code
- **Evidence**: Linked docs page, "What counts as a feature?" section, closing list.
- **Confidence**: settled (character-verified from raw HTML of the linked docs page)
- **Quote**: "The following policies are exceptions and are not affected: Restrictive model policies on GHE.com: Restrict Copilot to data residency models and Restrict Copilot to FedRAMP models. Store local sessions in the Cloud for Copilot CLI and VS Code."
- **Our assessment**: This exception list is not mentioned anywhere in the changelog itself — it only appears on the linked docs page, and would be easy for a practitioner to miss if they read only the changelog. It matters because two of the three exceptions are compliance-critical restriction policies (data residency, FedRAMP); confirming they are immune to the new default-enablement policy means a compliance-restricted enterprise's model/session-residency posture cannot be silently loosened by this feature policy regardless of its configuration.

### Claim 9: The feature policy is enabled by default itself — if an admin takes no action, unconfigured features will be enabled on October 22
- **Evidence**: Linked docs page, "Default availability of features" section.
- **Confidence**: settled (character-verified from raw HTML of the linked docs page)
- **Quote**: "This policy is enabled by default. If you don't take action, unconfigured features will be enabled on October 22."
- **Our assessment**: This makes explicit what Claim 5's "Enabled ... by default" language leaves implicit for the *global policy setting itself*: doing nothing is not a neutral choice — the default state of the new policy is "Enabled," so an admin who never visits the "AI Controls" > "Copilot" page at all will still see unconfigured features turn on October 22, exactly as if they had explicitly chosen "Enabled." This reinforces the same "opt-out, not opt-in" default framing already flagged for the models policy in `docs-github-copilot-global-model-policy-ga.md` Claim 2's assessment.

### Claim 10: Admins will see a banner in their policy settings showing how many eligible policies are currently unconfigured, so they can assess the impact of the global default and explicitly configure individual policies before October 22
- **Evidence**: Linked docs page, "Default availability of features" section.
- **Confidence**: settled (character-verified from raw HTML of the linked docs page)
- **Quote**: "In your policy settings, you will see a banner showing how many eligible policies are currently unconfigured, so you can assess the impact of your global default and explicitly configure individual policies before October 22."
- **Our assessment**: This gives admins a concrete, quantified starting point for the pre-October-22 audit (a count of at-risk unconfigured policies) rather than requiring them to manually inventory the "Features & clients," "Agents," and "MCP" pages themselves. For Ch05: recommend enterprises check this banner as the first step of any pre-enforcement review, before deciding whether to leave the global default enabled, disable it, or delegate to organizations.

### Claim 11: The docs page frames the feature policy and the (pre-existing) models policy as "two separate policies," with the models policy already active and the feature policy "becom[ing] active soon"
- **Evidence**: Linked docs page, opening paragraph.
- **Confidence**: settled (character-verified from raw HTML of the linked docs page)
- **Quote**: "For enterprises with Copilot Business or Copilot Enterprise plans, two separate policies control whether unconfigured generally available (GA) features and models default to enabled or disabled. If these policies are enabled, users benefit from the latest features and models without the need for administrator intervention. The models policy is already active. The feature policy will become active soon."
- **Our assessment**: This is GitHub's own framing confirming that the features policy documented in this note is a deliberately separate mechanism from the models policy documented in `docs-github-copilot-global-model-policy-ga.md`, not a rename or supersession of it. Both policies now live on the same docs page and share near-identical mechanics (three-state configuration, "Unconfigured" delegation, explicit-choice preservation), but an enterprise must configure each independently — disabling one does not disable the other.

### Claim 12: The linked docs page's models-policy exclusion list has grown by one entry since the changelog documented in `docs-github-copilot-global-model-policy-ga.md`: the data-retention-agreement exclusion now names both "Claude Fable 5" and "Claude Fable 5.1," where the earlier source named only "Claude Fable 5"
- **Evidence**: Linked docs page, "Default availability of models" section, "The following models are not in scope" list — compared against `docs-github-copilot-global-model-policy-ga.md` Claim 8's quote of the same docs page as it read around August 26–29, 2026.
- **Confidence**: settled for the current list text (character-verified from raw HTML); emerging for the "this is an update, not a discrepancy" interpretation, since no changelog entry announcing the "Claude Fable 5.1" addition to this exclusion list was independently located
- **Quote**: "Models that are not covered by GitHub's data retention agreement (Claude Fable 5, Claude Fable 5.1)"
- **Our assessment**: This is a living-docs-page update rather than a contradiction: the same docs page URL now lists an additional model in the same exclusion category. Consistent with the "Novel" note in `docs-github-copilot-global-model-policy-ga.md`'s Extraction Notes that this source's role is corpus-completeness tracking rather than a claim the changelog itself asserts, this confirms the exclusion list is maintained on a rolling basis as new non-data-retention-covered models ship, not fixed at GA time.

## Concrete Artifacts

### Changelog full text (verbatim, raw HTML, September 24, 2026)

```
Title: Default Enablement of Copilot Features for Copilot Business and Enterprise
Published: September 24, 2026 (Improvement, 1 minute read)
Tags: copilot, enterprise management tools
Source: https://github.blog/changelog/2026-09-24-default-enablement-of-copilot-features-for-copilot-business-and-enterprise

[Summary]
We're introducing a new global default policy for generally available GitHub
Copilot features and supported client capabilities in enterprise and
organization Copilot settings. For the next 28 days, you can configure this
policy, but it won't affect feature access for your users yet.

[What's changing]
Today, you can configure the new policy by going to the "AI Controls" page,
opening the "Copilot" subpage, and selecting an option under "Default policy
for new features". This policy applies to eligible features managed on your
enterprise's "Features & clients" page (i.e.,
https://github.com/enterprises/YOUR-ENTERPRISE-SLUG/ai-controls/copilot/features),
as well as the Copilot Code Review policy on the "Agents" page and the MCP
servers in Copilot policy. For feature eligibility and exceptions, see our
docs on default availability.
  -> https://docs.github.com/copilot/concepts/enterprise/default-availability

You can choose from the following settings:
- Enabled: Current and future eligible features will be available to users
  by default.
- Disabled: Current eligible features will remain unavailable, and future
  eligible features will require administrator approval.
- Let organizations decide: Organization administrators can choose whether
  to enable or disable eligible features.

Starting October 22, the policy takes effect. At that point:
- Eligible generally available features and capabilities left Unconfigured
  will follow your selected global default of enabled, disabled, or let
  organizations decide.
- Explicit decisions are preserved. If you've explicitly enabled or
  disabled a feature, we won't override that choice.
- Preview features remain opt-in. If you opt into a preview and it later
  becomes generally available, your existing choice will be preserved.

Join the discussion within GitHub Community.
  -> https://github.com/orgs/community/discussions/208757
```

### Linked docs page full text (verbatim, raw HTML: "About default availability of Copilot features and models")

```
For enterprises with Copilot Business or Copilot Enterprise plans, two
separate policies control whether unconfigured generally available (GA)
features and models default to enabled or disabled. If these policies are
enabled, users benefit from the latest features and models without the need
for administrator intervention.

The models policy is already active. The feature policy will become active
soon.

Default availability of features

The Default policy for new features policy is available to configure but is
not currently active. It will start applying to new and existing GA features
from October 22, 2026. In your policy settings, you will see a banner showing
how many eligible policies are currently unconfigured, so you can assess the
impact of your global default and explicitly configure individual policies
before October 22.

This policy is enabled by default. If you don't take action, unconfigured
features will be enabled on October 22.

What does the policy do?
Your setting for this policy determines the enablement status of:
- New GA (general availability) features
- Features that move from preview to GA
- Existing GA features that are Unconfigured in your policy settings

The policy can be configured in an enterprise and its organizations. At the
enterprise level, it applies to features labeled as Unconfigured. At the
organization level, it applies to features that an enterprise owner has set
to Let organizations decide, but that an organization owner has not
explicitly configured.

The policy does not apply to features in preview.

What counts as a feature?
For the purposes of this policy, a "feature" refers to any policy configured
on an enterprise's "Features & clients" page
(github.com/enterprises/ENTERPRISE/ai-controls/copilot/features), plus:
- The Copilot code review policy on the "Agents" page
- The MCP servers in Copilot policy on the "MCP" page

The following policies are exceptions and are not affected:
- Restrictive model policies on GHE.com: Restrict Copilot to data residency
  models and Restrict Copilot to FedRAMP models
- Store local sessions in the Cloud for Copilot CLI and VS Code

Default availability of models

The Default availability for released models policy is active and affects
new and unconfigured GA models.

Which models follow the policy?
The default policy applies to models that you have not explicitly
configured. These models are indicated in your enterprise or organization's
model settings with the Delegate to Default Policy label. When a new model
is released, it inherits the default until you explicitly configure it.

The following models are not in scope. They are disabled by default,
regardless of your "Default availability" policy setting.
- Pre-GA models
- Open weight models (DeepSeek, Kimi K2.7 Code, Kimi K3)
- Models that are not covered by GitHub's data retention agreement (Claude
  Fable 5, Claude Fable 5.1)
- For enterprises that have restricted models to data-resident or
  FedRAMP-compliant models, any models that do not respect these policies

How do I prevent default enablement?
To disable default enablement entirely, disable the default policies in your
enterprise or organization's settings. You can set a policy for the entire
enterprise, or disable the policy only in organizations with stricter
compliance requirements.
If you keep the default availability policies enabled, you can explicitly
disable individual features and models so that they are not eligible for
automatic enablement.
For features, see Managing policies and features for GitHub Copilot in your
enterprise and Managing policies and features for GitHub Copilot in your
organization.
For models, see Managing availability of models in your enterprise and
Managing the availability of models in an organization.

How do I prepare for new releases?
We recommend keeping up with new releases and GA announcements so you can
choose your enablement settings. New features and models are announced on
GitHub's changelog. For more information, see Learning about new features
and models.

Source: https://docs.github.com/copilot/concepts/enterprise/default-availability
```

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-global-model-policy-ga.md` (issue #2992, Claims 2,
    4, and 5–6): this note's Claim 5 (unconfigured items follow the global
    default, explicit choices always preserved, preview stays opt-in) is
    the same governance philosophy that source documents for the models
    policy, now applied to features and client capabilities. Claim 4 of
    this note (three-option Enabled/Disabled/Let-organizations-decide
    configuration) mirrors the enterprise/organization delegation shape
    already used by the models policy's state taxonomy in that source's
    Claim 6.
  - `docs-github-copilot-oct2026-model-deprecations.md` (issue #3558, Claim
    4): that source documents the models-policy default-enablement
    mechanism reaching a deprecation-notice successor-model context for the
    first time on September 18, 2026 — six days before this changelog
    extends the same "default-on, opt-out" philosophy to an entirely
    separate features/capabilities policy.

- **Extends**:
  - `docs-github-copilot-global-model-policy-ga.md`: the linked docs page
    cited by that note (`docs.github.com/.../concepts/models/
    default-availability`, then models-only) has since been retitled
    "About default availability of Copilot features and models" and now
    documents both policies side by side, explicitly as "two separate
    policies" (Claim 11). This note's Claim 12 additionally catches a
    living update to that page's models-exclusion list (addition of
    "Claude Fable 5.1" alongside "Claude Fable 5") since that note's
    August 29, 2026 extraction — an incremental docs-page change, not a
    contradiction of that note's Claim 8, per MINER.md §4a.
  - `docs-github-copilot-mcp-allowlists-enterprise.md` (issue #2564): that
    source documents the `allowedMcpServers`/`deniedMcpServers` keys that
    govern *which* MCP servers Copilot clients may run. This note's Claim 3
    documents a related but distinct mechanism — the "MCP servers in
    Copilot" *policy* (whether the MCP-servers capability is enabled at
    all) is one of the surfaces this new features-default policy governs.
    Neither source states how these two MCP-related governance layers
    (capability on/off vs. per-server allow/deny) interact; this is a gap
    between complementary mechanisms, not a contradiction, and is flagged
    here for future mining rather than filed as a contradiction issue.

- **Contradicts**: None. No existing corpus source makes a claim about the
  "Features & clients" page, the Copilot Code Review policy's enable/disable
  state, or the MCP servers in Copilot policy defaulting to a different
  behavior than this note describes. No contradiction issue filed per
  MINER.md §4a.

- **Novel**:
  - First corpus source to document a global default-enablement policy for
    GA Copilot *features and client capabilities*, as a deliberately
    separate mechanism from the models policy (Claim 11).
  - First corpus source to document that the "Copilot Code Review policy"
    and the "MCP servers in Copilot policy" are governed by this same
    features-default mechanism, alongside the "Features & clients" page
    (Claim 3).
  - First corpus source to document the enterprise/organization cascade
    precedence for a default-enablement policy in this much detail (Claim
    7): enterprise-level applies to "Unconfigured," org-level applies only
    to features explicitly delegated via "Let organizations decide."
  - First corpus source to document the named exceptions to a
    default-enablement policy (Claim 8): the GHE.com data-residency/FedRAMP
    model-restriction policies and "Store local sessions in the Cloud" are
    immune regardless of configuration.
  - First corpus source to document that a default-enablement policy is
    itself "enabled by default" prior to any admin action (Claim 9), and
    that GitHub surfaces a quantified "unconfigured policy count" banner to
    support pre-enforcement audits (Claim 10).

## Guide Impact

- **Chapter 05 (Team Adoption / Enterprise Governance)**:
  - Add the "Default policy for new features" policy as a second,
    independent pre-October-22, 2026 governance checklist item alongside
    the existing models-policy checklist derived from
    `docs-github-copilot-global-model-policy-ga.md`. Recommend enterprises:
    (1) check the "AI Controls" > "Copilot" > "Default policy for new
    features" banner (Claim 10) for the current unconfigured-policy count;
    (2) explicitly decide Enabled/Disabled/Let-organizations-decide rather
    than rely on the "enabled by default" fallback (Claim 9); and (3)
    remember this audit must separately cover the "Agents" page (Copilot
    Code Review policy) and "MCP" page (MCP servers in Copilot policy), not
    just "Features & clients" (Claim 3).
  - Document the enterprise/organization precedence rule from Claim 7
    precisely: an organization-level default choice only has effect for
    features the enterprise has explicitly set to "Let organizations
    decide" — organizations cannot use their own policy setting to override
    an enterprise's explicit Enabled/Disabled choice.
  - Flag the three named exceptions (Claim 8) — data-residency/FedRAMP
    model-restriction policies and "Store local sessions in the Cloud" — as
    the one part of enterprise Copilot governance this new policy cannot
    touch, useful reassurance for compliance-restricted enterprises
    auditing the October 22 rollout.
  - Note the "two separate policies" framing (Claim 11): guide advice
    should not conflate this features policy with the existing models
    policy documented in `docs-github-copilot-global-model-policy-ga.md` —
    an enterprise must configure each independently, and disabling one has
    no effect on the other.

## Extraction Notes

1. **Both primary sources fetched as raw HTML, not via AI-summarizing
   WebFetch alone**: An initial WebFetch pass over the changelog and the
   linked docs page returned reasonably accurate but non-verbatim
   paraphrases (e.g., collapsing the three-bullet "Starting October 22"
   list into a single summarized sentence, and abbreviating the models
   exclusion list). Both pages were then fetched directly via `curl` and
   the article body extracted programmatically (tags stripped, HTML
   entities decoded). All quotes in Claims 1–12 and both Concrete Artifacts
   blocks are taken from that raw-HTML extraction and are
   character-for-character verbatim from the source pages as of
   2026-09-25, not from the WebFetch summaries.
2. **Linked GitHub Community discussion checked but not substantive**: The
   discussion linked from the changelog's "Join the discussion" link
   (`github.com/orgs/community/discussions/208757`) is a client-rendered
   React page that does not expose its post body to a plain `curl` fetch. A
   WebFetch pass over the same URL reported no user comments beyond an
   automated bot acknowledgment of the original post — no practitioner
   questions or concerns to extract, unlike the analogous discussion
   (#203163) followed for `docs-github-copilot-global-model-policy-ga.md`,
   which did contain a substantive staff-authored announcement post.
3. **Cross-reference verification performed**: All `Claim N` citations to
   `docs-github-copilot-global-model-policy-ga.md` and
   `docs-github-copilot-oct2026-model-deprecations.md` were checked against
   those notes' actual claim numbering by re-reading each note in full
   before citing; none were guessed. The `docs-github-copilot-mcp-
   allowlists-enterprise.md` reference under Extends cites by topic/scope
   description rather than by claim number, since no single claim number in
   that note directly addresses the "MCP servers in Copilot" on/off policy
   this note describes.
4. **No contradiction issue filed**: See Cross-References → Contradicts.
   The one candidate discrepancy found (Claim 12's model-exclusion-list
   addition of "Claude Fable 5.1") is treated as a living-docs-page update
   rather than a disagreement between sources describing the same point in
   time, consistent with the precedent set in
   `docs-github-copilot-global-model-policy-ga.md`'s own Extraction Notes
   for similar docs-page evolution. No new contradiction issue was
   warranted per MINER.md §4a.
5. **Source is thin by design; the linked docs page carries most of the
   governance detail**: The changelog itself is approximately 170 words of
   primary text (Claims 1–5). Claims 6–10 all come from the linked docs
   page, which is substantially more detailed than the changelog it
   supports — consistent with the pattern already noted in
   `docs-github-copilot-global-model-policy-ga.md`'s Extraction Notes that
   GitHub's changelog posts for this policy family serve as pointers to a
   fuller, separately-maintained docs page rather than self-contained
   announcements.
