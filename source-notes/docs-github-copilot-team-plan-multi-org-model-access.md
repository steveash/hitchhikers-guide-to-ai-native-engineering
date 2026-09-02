---
source_url: https://github.blog/changelog/2026-08-31-copilot-model-access-update-for-github-team-plans
source_type: docs
title: "Copilot model access update for GitHub Team plans"
author: GitHub (official changelog)
date_published: 2026-08-31
date_extracted: 2026-09-02
last_checked: 2026-09-02
status: current
confidence_overall: settled
issue: "#3157"
---

# Copilot Model Access Update for GitHub Team Plans

> GitHub's August 31, 2026 changelog announcing that Copilot model access for
> users holding seats in more than one organization is now determined solely
> by the organization paying for that user's usage ("billing organization"),
> replacing the prior union rule where a model was accessible if *any* of the
> user's organizations had enabled it — scoped specifically to GitHub Team
> plan organizations outside an enterprise account.

## Source Context

- **Type**: docs (GitHub official product changelog, August 31, 2026; category
  "Improvement," "1 minute read," tags `copilot` and `enterprise management
  tools." Two linked pages followed per MINER.md §1: the "GitHub Copilot
  policies for enterprises and organizations" concepts page (specifically its
  "What about users with multiple licenses?" section, linked directly from
  the changelog) and the "Feature availability when GitHub Copilot policies
  conflict in organizations" reference page (linked from that concepts page).
  Both were fetched as raw HTML via `curl` and parsed directly, not via
  AI-summarizing WebFetch, so all quotes below are character-verified against
  the live pages.
- **Author credibility**: GitHub product/engineering team announcing a
  production policy change on its own official changelog. Authoritative for
  the fact that this change occurred, which scenario it applies to, and where
  to find the "billing organization" for an affected user. Not a source for
  why GitHub chose this mechanism, how many users are affected, or any
  transition/grace period for users whose model access narrows as a result.
- **Scope**: Covers model-access determination specifically for Copilot users
  who hold seats in more than one organization on a GitHub Team plan (i.e.,
  organizations not wrapped in a shared enterprise account). Does NOT cover:
  users whose Copilot access comes entirely through a single enterprise or
  its organizations (explicitly excluded — see Claim 4); the mechanics of
  Copilot Business/Enterprise enterprise-level model governance (targeted
  model rules, the global default-enablement policy); or any specific list of
  models affected by the change.

## Extracted Claims

### Claim 1: Copilot model access for users with multiple-organization Team plan seats is now determined only by the organization paying for their usage
- **Evidence**: Official GitHub changelog, opening summary sentence.
- **Confidence**: settled (product/policy fact, stated directly in official changelog, character-verified from raw HTML)
- **Quote**: "We have updated how model access is determined for Copilot users who hold seats in more than one organization. To keep billing and governance in sync, your model access is now determined only by the organization paying for your usage."
- **Our assessment**: This is the core mechanism change — model access resolution moves from a per-organization union to a single-source-of-truth (the billing org). GitHub's own framing ("to keep billing and governance in sync") suggests the prior union behavior had created a mismatch: a user could be granted access to a model enabled by an organization that was not the one paying for their Copilot usage. For Ch05: this is a concrete governance tightening worth flagging to any practitioner who holds Copilot seats across more than one standalone (non-enterprise) organization.

### Claim 2: Before this change, a user with Copilot seats in more than one organization could use any model enabled by any one of those organizations
- **Evidence**: Official changelog, "What's changing" section, describing the prior state.
- **Confidence**: settled (stated directly as the prior behavior being replaced)
- **Quote**: "Before this change, if you had Copilot seats in more than one organization, you could use a model as long as any of your organizations enabled it."
- **Our assessment**: This confirms the prior rule was a union/least-restrictive combination for model access specifically — matching the general "least restrictive" default described for most Copilot features in the linked policy-conflicts reference page (see Claim 7), rather than a model-specific carve-out that already existed. This is the first corpus source to state model access's *prior* combination rule explicitly; before this changelog, no corpus note documented what happened when a Team-plan user's organizations disagreed on model availability.

### Claim 3: A user's billing organization — the one determining their model access — is identified under "Usage billed to" on the Copilot features page
- **Evidence**: Official changelog, "What's changing" section, second sentence.
- **Confidence**: settled (concrete UI location stated directly in official changelog)
- **Quote**: "You can find this organization under \"Usage billed to\" in the Copilot features page."
- **Our assessment**: This is the operationally useful detail for an affected practitioner: to know which model set now applies to them, they should check "Usage billed to" at github.com/settings/copilot/features rather than assuming their most permissive organization still governs access. For Ch01/Ch05: worth including as a concrete first troubleshooting step for a user who notices a model they previously had access to has disappeared.

### Claim 4: Users whose Copilot access comes entirely through an enterprise or its organizations are not affected by this update
- **Evidence**: Official changelog, dedicated "What isn't changing" section.
- **Confidence**: settled (explicit scope exclusion stated directly in official changelog)
- **Quote**: "If your Copilot access comes entirely through an enterprise or its organizations, your model access will not be impacted by this update."
- **Our assessment**: This scopes the change tightly: it targets standalone GitHub Team plan organizations outside of any enterprise account, not the enterprise-governed model policies documented in `docs-github-copilot-global-model-policy-ga.md` (issue #2992) or `docs-github-copilot-org-targeted-model-rules.md` (issue #957). A practitioner whose organizations are all part of the same enterprise account should not expect any change in their effective model access from this changelog. For Ch05: the guide should present this as a narrow, Team-plan-specific fix, not a change to enterprise Copilot governance mechanics.

### Claim 5: The linked GitHub Copilot policy documentation independently states the same billing-organization rule for Team plan model policies
- **Evidence**: "GitHub Copilot policies for enterprises and organizations" concepts page, section "What about users with multiple licenses?" — linked directly from the changelog as "GitHub Copilot policy documentation." Fetched as raw HTML and character-verified.
- **Confidence**: settled (stated directly in official GitHub documentation, corroborating the changelog)
- **Quote**: "For model policies on a GitHub Team plan, a user's model access is determined by the organization paying for their usage. You can find this organization under \"Usage billed to\" on the Copilot features page."
- **Our assessment**: This is a near-verbatim restatement of Claims 1 and 3 in the standing (non-dated) documentation, confirming the changelog describes a durable policy rather than a temporary or reverting change. Because this documentation page is evergreen rather than dated, it is the page to re-check if this rule changes again in the future, rather than relying solely on the (now-historical) changelog entry.

### Claim 6: The billing-organization rule for Team-plan model access sits within a broader multiple-licenses framework where same-enterprise multi-org access defaults to least-restrictive and cross-enterprise multi-license access defaults to most-restrictive
- **Evidence**: Same "What about users with multiple licenses?" section, surrounding paragraphs.
- **Confidence**: settled (stated directly in official GitHub documentation, character-verified from raw HTML)
- **Quote**: "A user can receive access to Copilot from multiple organizations in the same enterprise. If these organizations have configured the same policy differently, the least restrictive policy usually applies, but there are some exceptions. More rarely, if a user receives a license from multiple different enterprises, the most restrictive policy across enterprises almost always applies."
- **Our assessment**: This places the Team-plan model-access change in context: it is a third, distinct combination rule (billing-org-only) alongside the pre-existing least-restrictive (same-enterprise, multi-org) and most-restrictive (multi-enterprise) defaults documented on the same page. None of the three rules is universal — which one applies depends on whether the user's multiple sources of Copilot access are Team-plan organizations, same-enterprise organizations, or different enterprises entirely. For Ch05: the guide should present these as three separate resolution rules keyed to license-source topology, not a single default a practitioner can assume without checking which topology applies to them.

### Claim 7: The general (non-model) Copilot feature-availability rules for members with Copilot from multiple organizations are per-feature least-restrictive or most-restrictive, enumerated in a dedicated reference table that does not include a line item for model access
- **Evidence**: "Feature availability when GitHub Copilot policies conflict in organizations" reference page, sections "How availability is determined" and "Availability for members with Copilot from multiple organizations," linked from the multiple-licenses section. Fetched as raw HTML.
- **Confidence**: settled (stated directly in official GitHub documentation, character-verified from raw HTML)
- **Quote**: "Feature, model, and privacy settings for users are set according to the least restrictive or the most restrictive policy defined by any of the organizations where they are granted a Copilot license. Least restrictive: if any of the organizations has enabled a feature, this feature is enabled for the user everywhere. This applies to all but the more sensitive Copilot features. Most restrictive: if any of the organizations has disabled a feature, this feature is disabled for the user in all their organizations. This applies only to the most sensitive Copilot features, for example: access to Copilot metrics using the API."
- **Our assessment**: This page's per-feature table (Copilot Metrics API, semantic indexing, code-suggestion privacy policy, code review, cloud agent, Spark, CLI, MCP servers, commit messages, and more — each tagged "Most restrictive organization" or "Least restrictive organization") lists 13 named policies as of this reading, none of which is "model access." That absence is consistent with Claim 2: model access previously followed the general default (least restrictive, i.e., union) described in this page's opening sentence rather than having its own dedicated, differently-configured row — and the August 31 changelog is what carves model access out of that general default into its own billing-organization rule for Team plan organizations specifically. For Ch05: this table is the reference point for practitioners asking "does my most permissive org or least permissive org win?" for any *other* Copilot feature besides model access.

## Concrete Artifacts

### Changelog full text (verbatim, raw HTML, August 31, 2026)

```
Title: Copilot model access update for GitHub Team plans
Published: August 31, 2026 (Improvement, 1 minute read)
Tags: copilot, enterprise management tools
Source: https://github.blog/changelog/2026-08-31-copilot-model-access-update-for-github-team-plans

[Summary]
We have updated how model access is determined for Copilot users who hold
seats in more than one organization. To keep billing and governance in sync,
your model access is now determined only by the organization paying for
your usage.

What's changing

Before this change, if you had Copilot seats in more than one organization,
you could use a model as long as any of your organizations enabled it. With
this update, your billing organization decides model access. You can find
this organization under "Usage billed to" in the Copilot features page.
For more information about how policies apply, read the GitHub Copilot
policy documentation.

What isn't changing

If your Copilot access comes entirely through an enterprise or its
organizations, your model access will not be impacted by this update.

Linked pages:
  "Copilot features page" -> https://github.com/settings/copilot/features
  "GitHub Copilot policy documentation"
    -> https://docs.github.com/enterprise-cloud@latest/copilot/concepts/policies#what-about-users-with-multiple-licenses
```

### Linked docs excerpt: "What about users with multiple licenses?" (verbatim, raw HTML, "GitHub Copilot policies for enterprises and organizations")

```
A user can receive access to Copilot from multiple organizations in the
same enterprise. If these organizations have configured the same policy
differently, the least restrictive policy usually applies, but there are
some exceptions.

More rarely, if a user receives a license from multiple different
enterprises, the most restrictive policy across enterprises almost always
applies. For example, if any enterprise disables Copilot Chat in GitHub,
that feature is disabled for the user.

For model policies on a GitHub Team plan, a user's model access is
determined by the organization paying for their usage. You can find this
organization under "Usage billed to" on the Copilot features page.

A user's individual plan is cancelled when they are added to a Copilot
Business or Copilot Enterprise plan, so a user's personal policies cannot
conflict with an enterprise's or organization's.

To see details for each policy, see Feature availability when GitHub
Copilot policies conflict in organizations.

Source: https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/policies
```

### Linked reference table excerpt: "Availability for members with Copilot from multiple organizations" (verbatim structure, raw HTML, "Feature availability when GitHub Copilot policies conflict in organizations")

```
Policy                                                              | Availability matches
---------------------------------------------------------------------------------------------
Copilot Metrics API                                                 | Most restrictive organization
Semantic indexing for non-GitHub repositories                       | Most restrictive organization
  (only available when all organizations explicitly set Enabled;
  Unconfigured behaves as disabled)
Suggestions matching public code (privacy policy)                   | Most restrictive organization
Allow members without a Copilot license to use Copilot code review
  in GitHub.com                                                     | Most restrictive organization
Copilot can search the web                                          | Least restrictive organization
Copilot Chat in GitHub Mobile                                       | Least restrictive organization
Copilot Chat in the IDE                                             | Least restrictive organization
Copilot Agent Mode in IDE Chat                                      | Least restrictive organization
Copilot code review                                                 | Least restrictive organization
Copilot cloud agent                                                 | Least restrictive organization
Spark                                                                | Least restrictive organization
Copilot in GitHub.com                                                | Least restrictive organization
Copilot in GitHub Desktop                                            | Least restrictive organization
Copilot CLI                                                          | Least restrictive organization
GitHub Copilot app                                                   | Least restrictive organization
Editor preview features                                              | Least restrictive organization
MCP servers in Copilot                                                | Least restrictive organization
Copilot-generated commit messages                                    | Least restrictive organization

Availability for members with Copilot from multiple enterprises:
"If a user receives a license from multiple different enterprises, the
most restrictive policy usually applies. The exceptions are: AI credit
paid usage (this applies to each enterprise, not the user); GitHub Spark."

Source: https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/enterprise-administrators/policy-conflicts
```

No line item for "model access" or "model policy" appears in this table as of the September 2, 2026 read — consistent with model access having been governed by the page's general default rule (least restrictive) prior to the August 31, 2026 changelog carving it out into the billing-organization rule for Team plan organizations.

## Cross-References

- **Corroborates**: None directly — no existing corpus source documents the prior (pre-August-31) model-access combination rule for multi-organization Team plan users, so there is nothing in the corpus to corroborate against for this specific mechanism. The general least-restrictive/most-restrictive framing in Claim 7 is newly introduced to the corpus by this note, not confirmed elsewhere.

- **Extends**: `docs-github-copilot-global-model-policy-ga.md` (issue #2992, Claim 6 and its Cross-References → Extends): that source documents a four-state model-availability taxonomy (Enabled / Disabled / Delegate to enterprise teams-apps-or-organizations / Delegate to default policy) for Copilot Business and Copilot Enterprise plans, and its Source Context explicitly flags as unresolved "how this global policy interacts precedence-wise with the org-level 'targeted model rules'... when both apply to the same organization." This note adds a distinct, non-overlapping resolution rule for a different plan tier and topology: GitHub Team plan organizations outside an enterprise account, where the deciding factor is the single billing organization rather than any enabled/disabled/delegated per-model state. Per this note's Claim 4, the two mechanisms are scoped to be mutually exclusive by design — a user is either governed by this note's billing-org rule (Team-plan, non-enterprise, multi-org) or by issue #2992's four-state enterprise policy (access entirely through an enterprise), not both.

- **Extends**: `docs-github-copilot-org-targeted-model-rules.md` (issue #957, Claim 3): that source documents the enterprise-level Enabled/Optional model-availability taxonomy and per-organization targeted model rules, scoped to Copilot Business and Copilot Enterprise plans (issue #957 Claim 5). This note's Claim 4 confirms that scope boundary from the other direction: the August 31 billing-organization change explicitly does not touch users whose access comes "entirely through an enterprise or its organizations" — i.e., issue #957's targeted-model-rules mechanism and this note's billing-org rule apply to disjoint populations of multi-org Copilot users (enterprise-wrapped organizations vs. standalone Team plan organizations).

- **Contradicts**: None. No existing corpus source describes a different rule for how multi-organization Team plan users' model access was determined prior to August 31, 2026, so there is no conflicting claim to reconcile. No contradiction issue filed per MINER.md §4a.

- **Novel**:
  - First corpus source to document the *prior* (pre-August-31, 2026) model-access combination rule for multi-organization Copilot users at all — the union/"any org enables it" rule (Claim 2) — and its replacement with a billing-organization-only rule (Claim 1), specifically for GitHub Team plan organizations outside an enterprise account.
  - First corpus source to document the general non-model feature-availability least-restrictive/most-restrictive combination table (Claim 7) for members with Copilot access from multiple organizations or multiple enterprises — useful general-purpose reference material not previously captured from any corpus source, even though it predates this specific changelog.
  - First corpus source to state explicitly that a user's individual Copilot plan is cancelled upon being added to a Business or Enterprise plan, eliminating personal-vs-enterprise policy conflicts by construction (Claim 6, second quoted paragraph) — not previously documented in the corpus's individual-plan-change notes.

## Guide Impact

- **Chapter 05 (Team Adoption / Enterprise Governance)**: Add this as a narrow but concrete governance fact for any practitioner or team lead managing Copilot access across multiple *standalone* GitHub Team plan organizations (not wrapped in a shared enterprise account): as of August 31, 2026, a user's available models are determined solely by whichever organization is billed for their usage, not by the union of all organizations that have enabled a given model. Recommend practitioners check "Usage billed to" on the Copilot features page (github.com/settings/copilot/features) as the first diagnostic step if an expected model disappears from their picker. Explicitly scope this guidance away from Chapter 05's existing enterprise-governance content (citing `docs-github-copilot-global-model-policy-ga.md` and `docs-github-copilot-org-targeted-model-rules.md`), which governs a disjoint population (users whose access comes entirely through an enterprise).
- **Chapter 05 (reference material)**: Incorporate the least-restrictive/most-restrictive per-feature table (Claim 7 / Concrete Artifacts) as reusable reference material for any guide content answering "which organization's policy wins" for a practitioner with Copilot access from multiple non-enterprise organizations, for features other than model access.

## Extraction Notes

1. **Changelog is short by design**: The primary changelog is approximately 100 words. Both linked pages ("GitHub Copilot policy documentation," reached via the changelog's own link, and the further-linked "Feature availability when GitHub Copilot policies conflict in organizations" reference page) were fetched to provide the depth for Claims 5–7 and the second and third Concrete Artifacts blocks, per MINER.md §1's instruction to follow substantive linked pages.
2. **Raw HTML fetched directly, not only via AI-summarizing WebFetch**: An initial WebFetch pass against the changelog returned a paraphrased summary. All quotes in this note were instead sourced from direct `curl` fetches of the raw HTML for all three pages (changelog, after following a 301 redirect to the canonical trailing-slash URL; the "policies" concepts page; the "policy-conflicts" reference page), with HTML tags stripped and entities decoded programmatically, then verified character-for-character against the raw text before inclusion.
3. **"GitHub Team plan" scope, not "Team" as a Copilot license tier**: The changelog's title and body use "GitHub Team plans" to mean GitHub organizations on the platform-level Team plan (an organization hosting tier, distinct from any enterprise account wrapper) — not a distinct Copilot license tier alongside Individual/Business/Enterprise. This is confirmed by the "What isn't changing" section's contrast with users whose access comes "through an enterprise or its organizations." The note's title and claims preserve GitHub's own terminology rather than substituting "organization" for "Team plan," since the changelog and linked docs both use "Team plan" specifically and consistently.
4. **Reference table contents are a snapshot, not dated**: The per-feature least-restrictive/most-restrictive table (Claim 7, third Concrete Artifacts block) is drawn from an evergreen documentation page, not a dated changelog, so its contents may change independently of this changelog entry. It is included here as supporting context for Claim 2's inference about model access's prior default, not as a claim about the table's permanence.
5. **No contradictions filed**: See Cross-References → Contradicts. This is the first corpus source to state the prior model-access combination rule for Team-plan multi-org users, so there is no existing claim to conflict with.
