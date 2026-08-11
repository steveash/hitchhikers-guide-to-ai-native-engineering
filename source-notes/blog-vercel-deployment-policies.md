---
source_url: https://vercel.com/changelog/configure-which-sources-can-create-deployments-with-deployment-policies
source_type: blog-post
title: "Configure which sources can create deployments with Deployment Policies"
author: Tom Knickman (Vercel)
date_published: 2026-07-13
date_extracted: 2026-08-11
last_checked: 2026-08-11
status: current
confidence_overall: settled
issue: "#2624"
---

# Configure which sources can create deployments with Deployment Policies

> A short Vercel changelog entry announcing Deployment Policies: per-team,
> per-project, per-environment rules restricting which Git providers/
> organizations/repositories and which deployment mechanisms (Git, CLI, v0,
> REST API, Deploy Hooks, Marketplace Integrations) are allowed to create a
> deployment — an Enterprise/Pro, Owner-role-gated access-control feature for
> the deployment pipeline itself, distinct from runtime/app-access controls.

## Source Context

- **Type**: blog-post (Vercel Changelog, `vercel.com/changelog`, published
  July 13, 2026; a single-author, three-sentence changelog entry — the
  shortest granularity of Vercel first-party announcement in this corpus).
  The entry links to one substantive companion page,
  `https://vercel.com/docs/deployments/deployment-policy`, which contains
  the actual feature mechanics the changelog entry itself does not describe.
  Per MINER.md §1, that docs page was fetched and read in full, since the
  changelog entry alone (two sentences of body text) is too thin to extract
  meaningfully on its own — this is the same pattern already documented for
  `blog-vercel-flags-oidc-default-auth.md`, another short changelog entry
  whose only comparable-detail lives on a linked docs page (though in that
  case the linked page turned out to be a generic, non-substantive overview;
  here the linked docs page is the primary source of every mechanical claim
  in this note).
- **Author credibility**: Tom Knickman, credited as "Software Engineer" at
  Vercel — a named first-party employee byline, consistent with the
  changelog-entry granularity seen elsewhere in this corpus (e.g. Luis
  Meyer's byline on the OIDC-default changelog entry). The linked docs page
  carries no individual byline (standard for reference documentation, not a
  narrative post) but is served from `vercel.com/docs`, the same
  first-party, vendor-operated documentation surface used throughout this
  corpus's other Vercel docs citations.
- **Scope**: Covers exactly one feature: Deployment Policies, a pair of
  independently-configurable rule types (Git Sources, Deployment Sources)
  that restrict what can create a deployment for a team or project, per
  environment. Covers plan/role gating (Enterprise and Pro plans, Owner
  role), the team-default/project-override inheritance model, the six named
  deployment mechanisms the Deployment Sources rule can allow or block, and
  the "saved but not enforced" pause state for a rule. Does NOT cover:
  pricing beyond the plan-tier gate itself, a rollout/GA date distinct from
  the changelog's July 13, 2026 publish date, audit-logging or alerting
  behavior when a policy blocks a deployment attempt, any named customer
  using the feature, or how Deployment Policies interact with Deployment
  Protection (a separate, pre-existing Vercel feature governing *access to*
  already-created deployments rather than *creation of* deployments) beyond
  both appearing under the same docs sidebar section ("Secure and govern").

## Extracted Claims

### Claim 1: Deployment Policies restrict which Git sources and deployment mechanisms are allowed to create deployments, with defaults settable at the team level and overridable per project
- **Evidence**: The docs page's opening definition sentence, corroborated by the changelog entry's own one-line summary.
- **Confidence**: settled (first-party docs description of a named, currently-available feature)
- **Quote**: "Deployment Policies are a set of rules that control which Git sources and deployment mechanisms can create deployments for your team and projects. You can define default rules for a team, and override these as neccesary per project."
- **Our assessment**: The team-default/project-override structure is the same governance-locus shape already documented for Vercel Passport's admin-centralized policy model (`blog-vercel-enterprise-apps-and-agents.md` Claim 3: "admins set the policy centrally rather than relying on each builder to configure it correctly") — but applied to the deployment pipeline's *entry points* rather than to *who can access* a deployment once it exists. The docs page's own worked example — "you can require that production only accepts deployments from a specific repository while preview stays open to any source" — makes the practical use case concrete: tighter restriction on the environment closest to real users, looser restriction upstream.

### Claim 2: A Deployment Policy has two independent rule types — Git Sources (which Git providers, organizations, and repositories may deploy) and Deployment Sources (which mechanisms, such as Git, the Vercel CLI, or Deploy Hooks, may deploy) — and each can be configured separately
- **Evidence**: Direct docs enumeration of the two rule types with one-sentence definitions each.
- **Confidence**: settled (first-party docs description of named, distinct configuration primitives)
- **Quote**: "A policy has two independent rules that can be configured: Git Sources restrict which Git providers, organizations, and repositories can deploy. Deployment Sources restrict which mechanisms, such as Git, the Vercel CLI, or Deploy Hooks, can deploy."
- **Our assessment**: This is a meaningful distinction for guide purposes: "who can deploy" (Git Sources — which repo/org) and "how a deployment can be triggered" (Deployment Sources — which mechanism) are separately controllable. A team could, for example, require that production deploys only come from a specific GitHub organization's repos (Git Sources) while separately blocking the REST API and Deploy Hooks as valid deploy mechanisms entirely (Deployment Sources), independent of which repository they'd otherwise be attributed to.

### Claim 3: Six named deployment mechanisms can each be individually allowed or blocked under a Deployment Sources rule: Git, Vercel CLI, v0 (Git-disconnected projects), REST API, Deploy Hooks, and Marketplace Integrations
- **Evidence**: A docs table enumerating each mechanism with a one-line description.
- **Confidence**: settled (first-party docs enumeration of a named configuration surface)
- **Quote**: "Deployment Sources rules limit which mechanisms can deploy to the selected environments. You can allow or block each of the following: Git — Deployments from a connected Git provider. Vercel CLI — Deployments created with the Vercel CLI. v0 — Deployments created from v0 projects without a Git connection. REST API — Deployments created through the REST API. Deploy Hooks — Deployments triggered by a project Deploy Hook URL. Marketplace Integrations — Deployments from a third-party Marketplace integration."
- **Our assessment**: This enumerated list is the most concrete, guide-relevant artifact in the source: it names every distinct way a deployment can currently be triggered on Vercel, which functions as an implicit map of the platform's deployment attack surface. Notably, "v0" (Vercel's AI app builder, previously documented in `blog-vercel-enterprise-apps-and-agents.md` Claim 10 as connecting directly to Snowflake under IdP control) and "REST API" are both named as independently blockable deployment sources — meaning a team can allow human-triggered Git-based deployment to production while blocking both an AI app builder and programmatic API calls from creating a production deployment at all, a relevant control for organizations concerned about agent- or API-originated deployments bypassing a review process.

### Claim 4: Rules can be created and saved without being enforced, letting a team pause a rule's enforcement without deleting its configuration
- **Evidence**: A single explanatory sentence about the rule lifecycle, distinct from the rule-definition mechanics.
- **Confidence**: settled (first-party docs description of a named lifecycle state)
- **Quote**: "Rules can be created and saved before they are enforced. When a rule is not enforced, Vercel keeps your configuration but stops applying it, so you can pause a rule without deleting it."
- **Our assessment**: This is a specific, reusable operational detail: the enforcement toggle is decoupled from the rule's existence, so a team can stage a policy (build out the exact source/mechanism restrictions it wants) before switching it on, and later pause it temporarily (e.g., during an incident requiring an out-of-band deploy) without having to reconstruct the rule from scratch afterward. No corpus source previously documented this specific "configured but not enforced" pattern for an access-control rule.

### Claim 5: Each rule applies to one or more selected environments, and a given environment can belong to at most one rule of the same type; environments are either the two system environments (Production and Preview) or project-defined custom environments
- **Evidence**: Direct docs description of the rule/environment binding model.
- **Confidence**: settled (first-party docs description of a named configuration constraint)
- **Quote**: "Each rule applies to one or more environments that you select, and an environment can belong to at most one rule of the same type. ... Environments come in two kinds: System environments: Production and Preview. Custom environments: any custom environments you've created on the project. Custom environments are only available when you edit a project's policy."
- **Our assessment**: The "at most one rule of the same type per environment" constraint is the mechanism that makes the docs page's earlier example work without ambiguity (production restricted to one repository, preview left open) — it guarantees a given environment has exactly one active Git Sources rule and exactly one active Deployment Sources rule at a time, rather than allowing conflicting or overlapping rules to be defined for the same environment.

### Claim 6: Deployment Policies are gated to Enterprise and Pro plans, and only team members with the Owner role can access the feature
- **Evidence**: A plan/role gate stated at the top of the docs page, before the feature description itself.
- **Confidence**: settled (first-party docs statement of a named access/plan restriction)
- **Quote**: "Deployment Policies are available on Enterprise and Pro plans. Those with the Owner role can access this feature."
- **Our assessment**: This double-gates the feature — by plan tier (Enterprise, Pro; not Hobby) and by role (Owner specifically, not any team admin) — which is a meaningfully tighter access restriction than, e.g., Vercel Connect's revocation CLI (`blog-vercel-enterprise-apps-and-agents.md` Concrete Artifacts), which the corpus does not document as role-gated at this granularity. Restricting configuration of "who/what can create a deployment" to the Owner role specifically (rather than any project admin) is consistent with treating deployment-pipeline entry-point control as a higher-stakes governance surface than day-to-day project administration.

### Claim 7: Overriding a team's inherited Deployment Policy is done per project, per rule type (Git Sources or Deployment Sources can each independently switch from Inherit to Override), and a project can revert to inheriting the team policy at any time
- **Evidence**: A dedicated docs subsection with a step-by-step override/revert procedure.
- **Confidence**: settled (first-party docs description of a named configuration workflow)
- **Quote**: "By default, a project inherits its team's deployment policy. You can override either part of the policy on a single project without affecting the rest of the team. ... To stop overriding and return to the team policy, switch the section back to Inherit and save. Inherited rules are shown as a read-only summary, with a link to view the team policy."
- **Our assessment**: The "read-only summary with a link to view the team policy" detail is a specific UI/legibility choice worth noting: a project that inherits the team policy cannot silently drift from it or accidentally show stale rule text, since the inherited state is always rendered as a live read-only view of the current team policy rather than a copied snapshot. This is the same team-default/project-override shape as Claim 1, restated here at the level of the actual UI workflow rather than the conceptual model.

## Concrete Artifacts

### Full changelog entry body (verbatim, from `vercel.com/changelog/configure-which-sources-can-create-deployments-with-deployment-policies`, published 13 Jul 2026, author Tom Knickman)

```
Deployment Policies are now available and enable teams to restrict which
mechanisms, organizations, and repositories are allowed to create
deployments.

Each policy can be configured per environment at the team and project
level, allowing flexible combinations of rules.

Learn more about Deployment Policies.
```

### Deployment Sources table (verbatim, from `vercel.com/docs/deployments/deployment-policy`)

```
Source                    | Description
---------------------------|---------------------------------------------
Git                        | Deployments from a connected Git provider.
Vercel CLI                 | Deployments created with the Vercel CLI.
v0                         | Deployments created from v0 projects without
                            | a Git connection.
REST API                   | Deployments created through the REST API.
Deploy Hooks                | Deployments triggered by a project Deploy
                            | Hook URL.
Marketplace Integrations    | Deployments from a third-party Marketplace
                            | integration.

Source: https://vercel.com/docs/deployments/deployment-policy
```

### Team-level Git Sources configuration steps (verbatim, from docs page)

```
To restrict Git sources for a team:
1. Open your team's Git Sources settings.
2. Select Add Rule and choose the environments the rule applies to.
3. Select Add Source, choose a provider, and enter the organization or
   namespace. Leave the repository or project field empty to allow any
   repository under that organization or namespace.
4. Select Save.

Source: https://vercel.com/docs/deployments/deployment-policy
```

### Per-project override steps (verbatim, from docs page)

```
1. Open your project's build and deployment settings.
2. For Git Sources or Deployment Sources, switch from Inherit to Override.
3. Edit the rules for the project, then select Save.

Source: https://vercel.com/docs/deployments/deployment-policy
```

## Cross-References

### Cross-reference verification notes
`blog-vercel-enterprise-apps-and-agents.md`, `blog-vercel-flags-oidc-default-auth.md`,
and `blog-anthropic-zero-trust-ai-agents.md` were re-read in full during this
extraction (MINER.md §4b), and every claim number cited below was located and
confirmed against that note's own numbered `### Claim N:` headings in
document order before writing this section.

- **Corroborates**:
  - `blog-vercel-enterprise-apps-and-agents.md` Claim 3 (Vercel Passport:
    "admins set the policy centrally rather than relying on each builder to
    configure it correctly") and Claim 2 ("`internal` was a setting someone
    had to configure on every project. One employee forgetting to make one
    deployment private risked exposing access to sensitive company
    systems"): this source's team-default/project-override model (Claim 1,
    Claim 7) is the identical governance-locus pattern — centralized team
    policy as the default, per-project deviation as an explicit, visible
    opt-out — applied to a different control surface (who/what can *create*
    a deployment, vs. who can *access* one once created). Together, Vercel
    now has two independently documented instances of "centralized-by-
    default, per-project override, admin/Owner-role gated" governance
    across its platform.
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 3 ("controls whose value
    comes only from friction fail against agentic attackers" — the
    "impossible vs. tedious" test): Deployment Policies' Deployment Sources
    rule (Claim 3 here) is a control that makes an entire deployment
    mechanism (e.g., REST API or Marketplace Integrations) structurally
    unavailable for a given environment, rather than merely adding friction
    to using it — it satisfies the "impossible, not tedious" bar that note's
    Claim 3 and Claim 4 identify as the pattern that survives against
    automated/agentic misuse, though this source itself makes no explicit
    security-framing argument (that framing is this note's synthesis, not a
    claim in the Vercel source).

- **Contradicts**: None identified as a MINER.md §4a contradiction.

- **Extends**:
  - `blog-vercel-enterprise-apps-and-agents.md`: that note documents identity
    gating for *who can view/access* an internal deployment (Passport) and
    scoped runtime credentials for *what an agent can touch once deployed*
    (Connect). This source adds a third, distinct control point in the same
    deployment lifecycle — restricting *what can create a deployment in the
    first place*, before Passport or Connect are ever relevant — filling a
    gap neither of that note's products address (Passport and Connect both
    presuppose a deployment already exists).
  - `blog-vercel-flags-oidc-default-auth.md`: that note documents a separate
    Vercel governance/access mechanic (automatic OIDC token issuance
    replacing a manually-configured SDK Key) at the level of a single
    sub-product's runtime authentication. This source is a different kind of
    control entirely — pipeline-entry-point restriction, not runtime
    credential issuance — but both are examples of Vercel shipping narrow,
    single-purpose governance primitives as separate, composable platform
    features rather than one monolithic "security" product.

- **Novel**:
  - **Deployment-mechanism-level allow/block list** (Claim 3): no prior
    corpus source documents a platform enumerating and independently gating
    each distinct way a deployment can be triggered (Git, CLI, a no-code AI
    builder, REST API, webhook-style Deploy Hooks, and third-party
    Marketplace integrations) as six separately controllable entry points to
    the deployment pipeline itself.
  - **"Saved but not enforced" rule-pause lifecycle** (Claim 4): the
    corpus's first documented instance of an access-control rule that can be
    fully configured and stored while its enforcement is independently
    toggled off — a specific operational affordance (pause without
    reconstruction) not previously documented for any other governance
    feature in this corpus.
  - **Owner-role-specific (not general-admin) gate on a governance
    feature** (Claim 6): no prior corpus source documents a Vercel
    governance feature restricted specifically to the Owner role as distinct
    from broader admin/team-management roles.

## Guide Impact

- **Chapter 06 (Security Threat Model)**: Add Deployment Policies' Deployment
  Sources allow/block list (Claim 3) as a concrete example of closing off
  agent- or API-originated deployment as an attack/misuse vector: a team can
  permit human-reviewed Git-based deploys to production while structurally
  blocking the REST API, Deploy Hooks, and a no-code AI builder (v0) from
  ever creating a production deployment, independent of credentials any of
  those paths might otherwise hold. This is a pipeline-entry-point control
  that complements (and precedes) the identity/credential-scoping controls
  already cited from `blog-vercel-enterprise-apps-and-agents.md` — those
  govern an agent's access *after* a deployment exists; this source governs
  whether a given mechanism can create the deployment at all.

- **Chapter 06 (Security Threat Model)**: Add Claim 4's "saved but not
  enforced" rule-pause lifecycle as a specific operational property worth
  looking for when evaluating any deployment-pipeline access-control
  feature: the ability to stage a restrictive policy in advance and pause
  (not delete/reconstruct) it during an incident is a meaningfully different
  operational affordance than a binary on/off toggle with no persisted
  "off" configuration.

- **Chapter 05 (Team Adoption)**: Add the team-default/project-override
  inheritance model (Claims 1, 7) as a second, independent instance
  (alongside Vercel Passport, `blog-vercel-enterprise-apps-and-agents.md`
  Claims 2-3) of "centralized-by-default policy, explicit and visible
  per-project deviation" as Vercel's general governance shape across
  unrelated product surfaces (access-to-deployments vs.
  creation-of-deployments) — strengthening the case that this is a
  deliberate platform-wide design convention, not a one-off feature choice.

## Extraction Notes

1. **Changelog entry itself is extremely thin — three sentences total.**
   Verified against the raw page HTML (fetched via `curl` with a browser
   user agent; confirmed via the page's own `<time>` element and author
   byline: published 13 Jul 2026, "1 min read," author Tom Knickman,
   "Software Engineer"). An initial WebFetch pass returned a similarly thin
   summary, which was cross-checked character-for-character against the
   `data-blog-body="true"` section of the raw HTML — the WebFetch summary
   was accurate but does not itself supply the "Learn more" link text,
   which was located directly in the HTML.
2. **Linked docs page followed and is the primary source for this note, per
   MINER.md §1.** `https://vercel.com/docs/deployments/deployment-policy`
   was fetched via `curl` (raw HTML, not WebFetch) because the changelog
   entry's two-sentence body does not describe the two rule types, the
   deployment-mechanism list, the enforcement-pause behavior, the
   environment-binding constraint, or the plan/role gate — all of which come
   from the docs page. Every `Quote` field in this note was located
   character-for-character in that raw HTML (after stripping markup) before
   being used. No other linked pages (e.g. "Managing deployments," "Deploy
   Hooks" in the docs page's own "Related" section) were followed — they are
   generic cross-links to adjacent but distinct features, not substantive
   companion pages for Deployment Policies specifically.
3. **No named customer, metric, or incident example anywhere in either
   page.** Both the changelog entry and the docs page are pure feature
   description with no case study, adoption number, or before/after
   narrative — unlike several other Vercel sources in this corpus (e.g. the
   v0 staged-rollout narrative in `blog-vercel-flags-platform-native-
   feature-flags.md`). This is reflected in the "settled" overall confidence
   rating: every claim here is an unambiguous, currently-verifiable
   description of a named, shipping feature's mechanics, with no anecdotal
   or marketing content to weigh the rating down toward "emerging," but also
   no field evidence that the feature works as intended at scale beyond the
   vendor's own documentation.
4. **No contradiction issues filed.** No claim in this source materially
   opposes any existing source note; see Cross-References → Contradicts.
