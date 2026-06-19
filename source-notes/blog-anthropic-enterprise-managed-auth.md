---
source_url: https://claude.com/blog/enterprise-managed-auth
source_type: blog-post
title: "Centrally manage authorization for MCP connectors"
author: Anthropic (no individual byline)
date_published: 2026-06-18
date_extracted: 2026-06-19
last_checked: 2026-06-19
status: current
confidence_overall: emerging
issue: "#1223"
---

# Centrally manage authorization for MCP connectors

> Official Anthropic announcement of enterprise-managed authorization for MCP
> connectors — admin-provisioned org-wide connector access via identity provider
> (Okta at launch) that eliminates per-user authorization steps, reduces token
> lifetimes, and integrates MCP access management into existing IdP workflows.

## Source Context

- **Type**: blog-post (official claude.com/blog, June 18, 2026; no individual
  byline — published as Anthropic; product announcement for a shipping beta feature)
- **Author credibility**: First-party Anthropic product announcement on the same
  publishing channel as "Building agents that reach production systems with MCP"
  and "Observability for developers building connectors." This is the authoritative
  Anthropic description of the enterprise-managed auth feature at GA beta. Claims
  about what the feature does, which providers are supported, and availability are
  vendor-authoritative. The launch ecosystem (7 MCP providers, 3 customer names)
  is directly verified by Anthropic.
- **Scope**: Covers the enterprise-managed authorization feature for MCP connectors —
  specifically: (1) the problem it solves (two-step provisioning burden), (2) how it
  works (IdP-based connector provisioning with zero-touch for end users), (3) security
  improvements (shorter token lifetimes, faster deprovisioning, work/personal
  separation), (4) the underlying MCP extension specification, (5) launch ecosystem
  partners (MCP connectors, identity providers, early customers), and (6) availability
  (beta, Team/Enterprise plans, starting with Okta). Does NOT cover: how to build
  an MCP connector that supports this extension, connector-level observability (see
  `blog-anthropic-connector-observability.md`), or the broader WIF credential pattern
  for workload-to-Claude-Platform authentication (see
  `blog-anthropic-workload-identity-federation.md`).

## Extracted Claims

### Claim 1: Previously, enabling MCP connectors required two steps — admin enablement org-wide AND per-user individual authorization — creating adoption friction at scale

- **Evidence**: Direct description of the prior state in the announcement, used as
  the motivation for the new feature.
- **Confidence**: settled (first-party problem framing; the two-step friction is a
  structural property of the prior connector setup flow)
- **Quote**: "Until now, turning them on required action at two steps: admins enabled
  a connector for the organization, and then every individual user authorized it
  themselves."
- **Our assessment**: This is the concrete friction point that enterprise-managed
  auth solves. At small team scale, per-user authorization is manageable. At
  enterprise scale (hundreds or thousands of employees), requiring each user to
  individually authorize each connector is an adoption bottleneck — each employee
  who doesn't complete the authorization step is not getting the benefit of the
  connector. For Ch05 (Team Adoption): this is the operational reason why the
  admin-provisioned pattern is better than individual-provisioned for enterprise
  deployments. The two-step description is the sharpest articulation of the
  "enterprise MCP deployment gap" in the corpus.

### Claim 2: Enterprise-managed auth eliminates the per-user authorization step — admins provision once, users inherit access via IdP groups and roles, and connectors appear on first login

- **Evidence**: Core feature description in the announcement.
- **Confidence**: settled (first-party feature description)
- **Quote**: "Enterprise-managed authorization streamlines that second step. Admins
  authorize a connector once, users inherit access through the IdP groups and roles
  they already have, and the connector is there the first time someone opens Claude."
- **Our assessment**: The access inheritance mechanism — through "IdP groups and
  roles they already have" — is the key architectural decision. This means MCP
  connector access becomes a property of an employee's existing organizational
  identity rather than a separate authorization act. An employee who is in the
  "Sales" IdP group and the org has provisioned the CRM connector for the Sales
  group: the connector is present in Claude from day one, without any user action.
  For Ch05: this is the correct enterprise deployment pattern when connector access
  should track organizational role membership rather than individual user choice.

### Claim 3: The result for end users is zero-touch connector setup — no user authorization steps required

- **Evidence**: Explicit characterization in the announcement.
- **Confidence**: settled (first-party feature claim)
- **Quote**: "The result is zero-touch connector setup for the end user"
- **Our assessment**: "Zero-touch" is the specific outcome that makes this feature
  valuable for enterprise rollouts. Org-wide MCP connector adoption goes from
  "requires email blast + per-user action" to "transparent at login." For the guide:
  teams deploying Claude enterprise-wide should use the admin-provisioned pattern
  whenever they want uniform connector access across a role or team, rather than
  relying on individual users to discover and authorize connectors themselves.

### Claim 4: Enterprise-managed auth folds MCP access management into existing IT admin workflows — provision once, scope by group, revoke through IdP

- **Evidence**: Direct quote from the announcement describing the admin workflow
  experience.
- **Confidence**: settled (first-party feature description)
- **Quote**: "For admins, this folds MCP access management into the same workflow
  that governs the rest of your stack: provision once, scope by group, manage
  revocation through the IdP."
- **Our assessment**: "The same workflow that governs the rest of your stack" is
  the key enterprise benefit — MCP connector governance becomes an extension of
  existing IT access management rather than a separate process. Admins who already
  manage Okta (or another OIDC provider) for SaaS application access can manage
  MCP connector access through the same tooling, policies, and review processes.
  For Ch02 (Harness Engineering): when designing enterprise Claude deployments,
  MCP access governance should be integrated into the organization's IAM/IdP
  system — not managed as a Claude-specific sidecar process. This is the correct
  enterprise-scale pattern.

### Claim 5: The feature provides a security improvement — admins can shorten access token lifetimes without impacting productivity, and deprovisioning is faster

- **Evidence**: Security benefit described in the announcement.
- **Confidence**: settled (first-party feature claim; the mechanism — IdP-issued
  tokens with configurable lifetimes — is well-understood)
- **Quote**: "Admins can shorten access token lifetimes without impacting
  productivity — so when someone is deprovisioned, their connector access expires
  fast instead of lingering on an old token."
- **Our assessment**: This is the direct application to MCP connectors of the
  short-lived token principle from `blog-anthropic-zero-trust-ai-agents.md`
  Claim 12 ("short-lived, narrowly-scoped tokens issued by an identity provider
  are the new baseline"). The productivity-neutral framing is important: shorter
  token lifetimes are typically resisted by users because they cause friction
  (re-authentication prompts). By making connector access inherit from the IdP
  session rather than requiring a separate MCP-specific auth, the token can be
  short-lived without imposing re-auth overhead on end users. For Ch03 (Safety
  and Verification): shorter token lifetimes + fast deprovisioning via IdP is the
  security posture this feature enables for MCP connector access — specifically
  addressing the "lingering access after offboarding" risk.

### Claim 6: Admins can require that connectors only connect through the IdP, enforcing separation between work and personal use

- **Evidence**: Feature description in the announcement.
- **Confidence**: settled (first-party feature claim)
- **Quote**: "Admins can also require that a connector only ever connects through
  the IdP, which keeps work and personal use cleanly separated."
- **Our assessment**: This control addresses a real governance concern in enterprise
  deployments — employees using work-provisioned Claude accessing personal accounts
  via connectors, or vice versa. By requiring that a connector only connects through
  the organizational IdP, admins ensure that the connector is only ever used in a
  work context (where the IdP session is active) and cannot be used with personal
  Claude accounts. For Ch05 (Team Adoption) and compliance-sensitive deployments:
  this is an enterprise governance control worth enabling for any connector that
  accesses organizational data (CRM, project management, internal docs).

### Claim 7: Enterprise-managed auth is the first implementation of a formal MCP extension specification — the "Enterprise-Managed Authorization extension to the Model Context Protocol"

- **Evidence**: Direct statement from the announcement about the technical basis
  of the feature.
- **Confidence**: settled (first-party spec attribution; the extension URL is given
  as `https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization`)
- **Quote**: "Enterprise-managed auth is the first implementation of the
  Enterprise-Managed Authorization extension to the Model Context Protocol. It's
  built on an open standard so any connector can support it."
- **Our assessment**: The "first implementation" phrasing is significant — it
  establishes that this is not a proprietary Anthropic mechanism but an open MCP
  protocol extension that any connector developer can implement. This means the
  enterprise-managed provisioning pattern is expected to become available across
  the broader MCP ecosystem as additional connectors implement the extension. For
  Ch02 and the MCP ecosystem coverage: practitioners evaluating enterprise MCP
  deployments should look for connectors that support this extension; connector
  developers building enterprise-facing tools should implement it. The open
  standard basis is what makes the "any connector can support it" claim credible.

### Claim 8: The feature launches with seven MCP connectors (Asana, Atlassian, Canva, Figma, Granola, Linear, Supabase), Okta as the first identity provider, and three named early-adopting customers (HubSpot, Ramp, Webflow)

- **Evidence**: Specific enumeration in the announcement.
- **Confidence**: settled (named companies confirmed by Anthropic as launch partners)
- **Quote**: (no single verbatim quote covers the full list; see Our assessment for
  specific names extracted from the announcement)
- **Our assessment**: Launch partners: Asana, Atlassian, Canva, Figma, Granola,
  Linear, Supabase (Slack "coming soon"). Identity providers: Okta (at launch,
  additional providers coming). Early customers: HubSpot, Ramp, Webflow. The
  breadth of launch partners — productivity tools (Asana, Linear), design tools
  (Canva, Figma), note-taking (Granola), developer tools (Supabase, Atlassian),
  with Slack pending — covers the major categories of workplace SaaS tools. The
  early customers are mid-to-large enterprise companies, suggesting the feature
  has been validated in real enterprise deployments before beta announcement.

### Claim 9: Enterprise-managed auth is available in beta for Claude Team and Enterprise plan customers as of June 18, 2026

- **Evidence**: Stated availability in the announcement.
- **Confidence**: settled (first-party availability claim)
- **Quote**: "Enterprise-managed auth is available today in beta for customers on
  the Claude Team and Enterprise plans."
- **Our assessment**: Beta availability means the feature is shipping and in active
  use, but the feature scope and UX may change before GA. For the guide: recommend
  evaluating this feature for any enterprise Claude deployment as of June 2026.
  The Team plan inclusion (not just Enterprise) is notable — this suggests the
  feature is intended for smaller organizations as well, not only large enterprise
  customers.

## Concrete Artifacts

### Problem Statement and Feature Description

```
# Enterprise-Managed Authorization for MCP Connectors
# Source: "Centrally manage authorization for MCP connectors," Anthropic, June 18, 2026

PREVIOUS STATE (two-step problem):
  Step 1: Admin enables connector for the organization
  Step 2: EVERY individual user authorizes it themselves
  Source: "Until now, turning them on required action at two steps: admins enabled
           a connector for the organization, and then every individual user
           authorized it themselves."

NEW STATE (enterprise-managed auth):
  Admin action:  "Admins authorize a connector once, users inherit access through
                  the IdP groups and roles they already have, and the connector is
                  there the first time someone opens Claude."
  User action:   None required — "The result is zero-touch connector setup for
                  the end user"
  Admin workflow: "For admins, this folds MCP access management into the same
                   workflow that governs the rest of your stack: provision once,
                   scope by group, manage revocation through the IdP."
```

### Setup Flow (from "How it works" section)

```
# Enterprise-Managed Auth Setup
# Source: "Centrally manage authorization for MCP connectors," Anthropic, June 18, 2026

HOW IT WORKS:
  "Connect your identity provider to Claude and choose which MCP connectors to
   enable for your organization. When an employee logs in, their connectors are
   already there."

TRUST FOUNDATION:
  "Access runs through the identity provider you already trust"
```

### Security Controls

```
# Security benefits of enterprise-managed auth
# Source: "Centrally manage authorization for MCP connectors," Anthropic, June 18, 2026

TOKEN LIFETIME MANAGEMENT:
  "Admins can shorten access token lifetimes without impacting productivity — so
   when someone is deprovisioned, their connector access expires fast instead of
   lingering on an old token."

WORK/PERSONAL SEPARATION:
  "Admins can also require that a connector only ever connects through the IdP,
   which keeps work and personal use cleanly separated."
```

### Technical Specification

```
# Enterprise-Managed Authorization MCP Extension
# Source: "Centrally manage authorization for MCP connectors," Anthropic, June 18, 2026

SPECIFICATION:
  "Enterprise-managed auth is the first implementation of the Enterprise-Managed
   Authorization extension to the Model Context Protocol. It's built on an open
   standard so any connector can support it."

SPEC URL: https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization

OPENING STATEMENT (page intro):
  "Admins can now provision MCP connectors for their whole organization through
   their identity provider, starting with Okta."
```

### Launch Ecosystem

```
# Enterprise-managed auth launch ecosystem (June 18, 2026)
# Source: "Centrally manage authorization for MCP connectors," Anthropic

MCP CONNECTOR LAUNCH PARTNERS:
  Asana, Atlassian, Canva, Figma, Granola, Linear, Supabase
  Coming soon: Slack

IDENTITY PROVIDERS:
  Okta (at launch); additional providers coming soon

EARLY CUSTOMERS (named in announcement):
  HubSpot, Ramp, Webflow

AVAILABILITY:
  Beta — Claude Team and Enterprise plans
  "Enterprise-managed auth is available today in beta for customers on the
   Claude Team and Enterprise plans."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 12 ("Short-lived,
    narrowly-scoped tokens issued by an identity provider are the new baseline"):
    The token-lifetime management control in Claim 5 here is a concrete
    product-level implementation of exactly this principle applied to MCP connector
    access. The zero-trust eBook prescribed short-lived tokens as the floor; this
    feature delivers short-lived tokens for MCP connectors without productivity
    impact. The "lingers on an old token" problem (after deprovisioning) is
    precisely the static-credential-leakage risk the zero-trust framework
    identifies.
  - `blog-anthropic-connector-observability.md` Claim 7 (access gate: "a Team
    or Enterprise account with Admin or Owner access"): Both features require
    Team or Enterprise plans and admin-level access. Together they form a coherent
    enterprise MCP management picture — admins provision access (this source) and
    monitor performance (connector-observability). The access tier is identical
    across both features.
  - `blog-anthropic-mcp-production-agents.md` Claim 9 (CIMD OAuth for MCP auth):
    CIMD addresses how individual MCP clients (agents, users) authenticate to MCP
    servers that require OAuth. Enterprise-managed auth addresses a different layer:
    how the organization provisions connector access so users don't have to
    authenticate individually. These are complementary — CIMD is the individual-
    level OAuth mechanism; enterprise-managed auth is the org-level provisioning
    mechanism layered on top.

- **Extends**:
  - `blog-anthropic-workload-identity-federation.md`: WIF covers OIDC-based
    authentication from workloads TO the Claude Platform (workload → Claude auth).
    Enterprise-managed auth covers IdP-based provisioning of connector access so
    Claude can reach external services via MCP (Claude → external service auth).
    These are different authentication boundaries. WIF is the credential pattern
    for "how does my agent identify itself to Claude?"; enterprise-managed auth is
    the credential pattern for "how does Claude, on behalf of my org, identify
    itself to external systems through MCP connectors?" Together they document
    both sides of the Claude Platform authentication picture: inbound (WIF) and
    outbound (enterprise-managed auth via connectors).
  - `blog-anthropic-connector-observability.md`: The observability note (June 8,
    2026) covers monitoring deployed connectors. This note (June 18, 2026) covers
    access provisioning for those same connectors. Together they advance the
    enterprise MCP management corpus from "build a connector" (production-agents
    note) → "monitor it" (observability note) → "govern who can access it"
    (this note). A more complete enterprise MCP deployment lifecycle emerges from
    the three sources in sequence.
  - `blog-anthropic-mcp-production-agents.md` Claim 9 (CIMD OAuth): CIMD is the
    per-agent dynamic registration mechanism for MCP OAuth. Enterprise-managed auth
    extends the MCP auth corpus with an org-level provisioning pattern. The two
    are complementary layers in the MCP auth stack: CIMD for programmatic agent
    registration; enterprise-managed auth for human-user access provisioning at
    organizational scale.

- **Contradicts**: None identified. The enterprise-managed auth feature operates
  at a different layer from the existing corpus claims about MCP auth (CIMD) and
  platform auth (WIF). No contradiction issues to file.

- **Novel**:
  - **Enterprise-Managed Authorization as a formal MCP extension specification**:
    First corpus source to document a named, open MCP extension for enterprise
    identity provider integration. The `modelcontextprotocol.io/extensions/auth/...`
    URL establishes this as a protocol-level artifact, not just a product feature.
  - **Two-step MCP connector provisioning problem named and solved**: The
    "admins enable + users authorize" two-step friction is named and solved here
    for the first time in the corpus. No prior source documents this as the
    operational bottleneck for enterprise MCP adoption.
  - **Zero-touch connector setup via IdP provisioning**: The combination of
    admin-once provisioning + user access inheritance through IdP groups is a
    completely new deployment pattern in the corpus. No prior source documents
    org-wide MCP connector access flowing from identity provider group membership.
  - **MCP access as a property of organizational identity**: The insight that
    MCP connector access should track IdP role membership (not individual user
    choice) is new. Prior corpus sources treat connector access as either per-user
    or per-deployment; this establishes per-role as the correct enterprise model.
  - **Work/personal connector separation via IdP requirement**: The capability
    to require connectors only connect through the org IdP (preventing personal
    use of work-provisioned connectors) is entirely new to the corpus.
  - **Named enterprise launch ecosystem** (Asana, Atlassian, Canva, Figma,
    Granola, Linear, Supabase; HubSpot, Ramp, Webflow as customers): First corpus
    documentation of specific enterprise MCP connector providers with identity
    federation support.

## Guide Impact

- **Chapter 05 (Team Adoption / Enterprise patterns)**: Add enterprise-managed
  auth as the recommended MCP connector provisioning pattern for multi-user Claude
  deployments. Currently the corpus covers connector design (production-agents),
  connector monitoring (observability), and connector-level auth mechanics (CIMD),
  but lacks guidance on org-wide access provisioning. The "provision once, scope
  by group, manage revocation through IdP" pattern (Claim 4) should be the
  canonical enterprise deployment recommendation for any Claude rollout where
  connector access should reflect organizational roles. Contrast with per-user
  authorization (appropriate for small teams or individual tool exploration) and
  establish the admin-provisioned pattern as the correct approach at enterprise
  scale.

- **Chapter 02 (Harness Engineering — enterprise integration)**: Add guidance
  that enterprise MCP deployments should integrate connector access governance
  into existing IdP infrastructure rather than managing MCP access separately.
  The feature's admin workflow ("same workflow that governs the rest of your
  stack") implies that Claude connector access should be planned alongside SaaS
  application access management — not treated as a one-off configuration. Recommend
  that organizations with Okta (or forthcoming providers) use the enterprise-managed
  auth beta for any connector that should have org-wide adoption rather than
  optional individual setup.

- **Chapter 03 (Safety and Verification — credential lifecycle)**: Add the
  connector-access-token lifecycle management benefit as a concrete security
  practice: enterprise-managed auth enables shorter token lifetimes without
  productivity impact, and fast deprovisioning through the IdP. This extends the
  zero-trust credential principle (short-lived tokens) from the Claude Platform
  level (WIF) and workload level (zero-trust eBook) to the MCP connector access
  level. The three together form a layered credential lifecycle pattern:
  1. Platform-level: WIF (short-lived tokens for workload → Claude auth)
  2. Connector-level: enterprise-managed auth (short-lived tokens + fast
     deprovisioning for Claude → external system auth)
  3. Spec-level: zero-trust framework (short-lived tokens as minimum baseline
     everywhere)

- **Chapter N (MCP Ecosystem / Connector selection)**: When the guide covers
  connector selection for enterprise deployments, flag Enterprise-Managed
  Authorization extension support as an evaluation criterion. Connectors that
  implement the open MCP extension (`modelcontextprotocol.io/extensions/auth/
  enterprise-managed-authorization`) support org-wide admin provisioning;
  connectors that don't require per-user setup. For enterprise buyers: preference
  connectors with this extension.

## Extraction Notes

1. **WebFetch returns model-summarized content**: The claude.com blog renders as
   a JavaScript SPA; WebFetch AI-summarizes rendered content. Three separate
   fetches were performed with targeted verbatim-extraction prompts to maximize
   quote fidelity. All quotes marked with `"..."` in this note appeared consistently
   across multiple fetches and are treated as verbatim from the source. The page
   title ("Centrally manage authorization for MCP connectors"), section headings
   ("How it works," "Built with an ecosystem," "Getting started"), and the extension
   spec URL were consistent across fetches.

2. **Short feature-announcement post**: This is a compact product announcement
   (~5 min read) focusing on what the feature does and who the launch partners are,
   not a deep technical implementation guide. Claims were fully exhausted at 9
   extractions — the article does not contain deep technical specifics beyond
   what is documented here.

3. **Beta caveat**: All features described are in public beta as of June 18, 2026.
   Feature scope, supported identity providers, and MCP connector partners may
   change before GA. The "additional providers coming soon" language suggests Okta
   is only the first of several planned identity providers.

4. **Open spec vs. Anthropic-proprietary**: The Enterprise-Managed Authorization
   extension is described as an open MCP spec (`modelcontextprotocol.io/extensions/...`).
   This is architecturally distinct from Anthropic-proprietary features. However,
   the open standard has not yet been independently verified in this corpus —
   no third-party implementations or spec analysis notes exist. Treating as
   "emerging" overall until broader ecosystem adoption is documented.

5. **No contradictions to file**: Cross-referencing against corpus found no
   material contradictions. WIF (workload → Claude) and enterprise-managed auth
   (Claude → external via MCP) operate at different auth boundaries. CIMD OAuth
   (individual per-server auth) and enterprise-managed auth (org-level provisioning)
   operate at different provisioning granularities. Both pairs are complementary,
   not contradictory.
