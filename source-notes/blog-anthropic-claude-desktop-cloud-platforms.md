---
source_url: https://claude.com/blog/the-full-claude-desktop-experience-on-aws-google-cloud-and-microsoft-foundry
source_type: blog-post
title: "The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry"
author: Anthropic (no individual byline)
date_published: 2026-06-22
date_extracted: 2026-06-23
last_checked: 2026-06-23
status: current
confidence_overall: emerging
issue: "#1281"
---

# The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry

> Official Anthropic announcement (June 22, 2026) that Claude Desktop now delivers
> chat, Claude Cowork, and Claude Code as a single unified deployment for organizations
> on AWS, Google Cloud, and Microsoft Foundry — completing cloud platform parity for
> the full Desktop experience and introducing enterprise deployment controls including
> per-surface policy keys, MDM template support, pre-rollout validation, a model guard,
> and a local connector option for strict data residency.

## Source Context

- **Type**: blog-post (official claude.com/blog, June 22, 2026; no individual byline;
  product announcement for a shipping feature change, not a research preview)
- **Author credibility**: First-party Anthropic product announcement on the same channel
  as recent enterprise infrastructure announcements (enterprise-managed-auth, WIF). Claims
  about which features are now available, the per-surface policy key mechanism, and the
  supported SSO providers are vendor-authoritative. The single customer testimonial
  (Hanwha Solutions) is a named individual with a specific claim but cannot be
  independently verified.
- **Scope**: Covers (1) the addition of Chat to the cloud-platform-hosted Claude Desktop,
  completing the three-surface experience; (2) per-surface policy keys for access control;
  (3) five categories of enterprise deployment controls (SSO, MDM deployment, pre-rollout
  validation, gradual rollout, M365 connector + data residency); (4) one named customer
  case (Hanwha Solutions). Does NOT cover: pricing of the cloud-provider-hosted Desktop
  offering, technical architecture differences between the cloud-hosted Desktop and the
  direct Claude Desktop, how inference is billed through each provider, or the API-level
  features (dynamic workflows, Managed Agents) on these platforms (those are covered in
  separate notes). The post is short (~500 words); no sub-pages were linked from the
  deployment-controls section.

## Extracted Claims

### Claim 1: Claude Desktop deployed through AWS, Google Cloud, and Microsoft Foundry now includes Chat alongside the previously available Claude Cowork and Claude Code, completing a unified three-surface experience

- **Evidence**: First-party announcement of a specific feature addition. The post names
  the pre-announcement state explicitly: only Cowork and Code were available; Chat is now
  added.
- **Confidence**: settled (first-party product announcement of a shipping feature)
- **Quote**: "Organizations that use Claude Desktop through AWS, Google Cloud, and
  Microsoft Foundry now get the full Desktop experience — chat, Claude Cowork, and Claude
  Code, all in one app."
- **Quote (prior state)**: "Until today, customers using Claude Desktop through AWS,
  Google Cloud, and Microsoft Foundry only had access to Claude Cowork and Claude Code."
- **Our assessment**: This claim is the core news of the announcement. The strategic
  implication: organizations that had already deployed Claude through these cloud providers
  can now give non-technical staff access to Chat without requiring a separate Claude.ai
  deployment or plan. The "all in one app" framing matters for enterprise procurement —
  one deployment covers every role (non-technical workers on Chat, knowledge workers on
  Cowork, engineers on Code). The fact that this was NOT available previously (cloud
  deployments were Cowork-and-Code-only) is the significant fact: Chat was previously
  only available through the direct Claude.ai/Claude Desktop path, not through the
  cloud-provider-managed offering. This completes feature parity.

### Claim 2: Each of the three Desktop surfaces (Chat, Claude Cowork, Claude Code) has its own policy key, enabling role-based access control at the surface level with org-wide hard-deny rules

- **Evidence**: First-party feature description with explicit example of how to use the
  policy keys for staged rollout.
- **Confidence**: settled (first-party product feature description)
- **Quote**: "Now, one deployment covers every role, and each surface has its own policy
  key, so you decide who gets what, and when."
- **Quote (deployment pattern)**: "Chat, Claude Cowork, and Claude Code each have their
  own policy key, so you can give non-technical teams chat and Claude Cowork, engineering
  Claude Code, and then broaden access as teams adopt each surface. Your hard-deny rules
  apply across every tab."
- **Our assessment**: Per-surface policy keys are the access governance primitive that
  makes the unified deployment work in practice for enterprises. Without them, adding
  Chat to a cloud-provider deployment would mean all employees could access all surfaces
  immediately. With policy keys, admins can execute a staged rollout: Chat first (lower
  risk, high value), then Cowork, then Code — and the "hard-deny rules apply across every
  tab" statement ensures that org-wide restrictions are not bypassable by switching
  surfaces. This is a distinct and more granular control than the workspace-level SCIM
  RBAC described in `blog-anthropic-cowork-enterprise.md` Claim 1 — SCIM controls
  capability access per user group across the workspace; policy keys control which
  Desktop surface is enabled per org.

### Claim 3: Cloud-hosted Claude Desktop uses enterprise SSO — IAM Identity Center, Workforce Identity Federation, Microsoft Entra ID, or any OIDC provider — with no shared keys or cloud credentials on end-user machines

- **Evidence**: First-party feature description with specific named authentication
  providers.
- **Confidence**: settled (first-party authentication options with named providers)
- **Quote**: "Employees use the same work account they use for everything else: IAM
  Identity Center, Workforce Identity Federation, Microsoft Entra ID, or any OIDC
  provider like Okta. No shared keys to rotate, no cloud credentials on end-user
  machines."
- **Our assessment**: The "no shared keys to rotate, no cloud credentials on end-user
  machines" statement is the security headline for enterprise IT. Each cloud provider's
  native identity mechanism is supported: AWS IAM Identity Center, Google's Workforce
  Identity Federation, and Microsoft Entra ID — meaning the Desktop deployment doesn't
  require organizations to configure a separate identity provider for Claude. The "any
  OIDC provider like Okta" tail extends this to organizations that use a third-party
  IdP on top of any of the three cloud platforms. This aligns with the authentication
  architecture documented in `blog-anthropic-enterprise-managed-auth.md` (IdP-based
  access provisioning for MCP connectors) and `blog-anthropic-workload-identity-federation.md`
  (OIDC federation for API workloads) — together they describe a coherent IdP-first
  authentication architecture at all layers of Claude deployment.

### Claim 4: Claude Desktop can be deployed via MDM policy templates (Intune, GPO, Jamf) or an offline installer for air-gapped environments

- **Evidence**: First-party feature description with named MDM platforms and air-gapped
  deployment option.
- **Confidence**: settled (first-party deployment option description with named tools)
- **Quote**: "Export policy templates from the setup UI and push them through Intune,
  GPO, or Jamf. An offline installer covers air-gapped environments."
- **Our assessment**: The three named MDM systems (Intune for Microsoft, GPO for
  Windows domain environments, Jamf for macOS/iOS) cover the dominant enterprise device
  management platforms. "Export policy templates from the setup UI" suggests the Claude
  Console provides pre-built configuration artifacts for each MDM system, rather than
  requiring admins to author configurations from scratch. The offline installer for
  air-gapped environments is notable — it extends cloud-hosted Claude Desktop to
  organizations with strict network segmentation (defense, financial, healthcare
  environments that cannot make outbound connections during app installation). No prior
  corpus source documents Claude Desktop air-gapped deployment.

### Claim 5: A pre-rollout validation mechanism lets admins test connectors, confirm available models, and verify connections before users see the deployment; a model guard maintains Claude routing including in GovCloud even if settings are misconfigured

- **Evidence**: First-party feature description with specific named benefit ("model guard"
  and GovCloud mention).
- **Confidence**: settled (first-party feature description with specific behavior named)
- **Quote**: "Test every connector, confirm which Claude models your provider serves, and
  verify the connection, all before rollout. A model guard keeps routing on Claude,
  including in GovCloud, even if a setting is misconfigured."
- **Our assessment**: Pre-rollout validation addresses a real enterprise deployment risk:
  launching to hundreds or thousands of users before verifying that connectors are
  working and the right models are available. The "confirm which Claude models your
  provider serves" detail is important — different cloud providers may have different
  model availability, and admins should know what model users will actually interact
  with before rollout. The "model guard" is the more architecturally interesting claim:
  it guarantees that routing stays on Claude even in misconfiguration scenarios,
  specifically calling out GovCloud. This is the first corpus mention of GovCloud
  support, and the model guard appears to be a guardrail that prevents accidental
  routing to non-Claude models in sensitive deployment environments.

### Claim 6: Per-surface policy keys enable a staged rollout pattern — non-technical teams get Chat and Cowork, engineers get Code — with access expanded as each team adopts

- **Evidence**: Explicit example provided in the announcement.
- **Confidence**: settled (explicit vendor-provided rollout pattern)
- **Quote**: "you can give non-technical teams chat and Claude Cowork, engineering Claude
  Code, and then broaden access as teams adopt each surface"
- **Our assessment**: This is the operationally actionable rollout pattern the announcement
  endorses. The framing "broaden access as teams adopt each surface" positions the staged
  rollout as evidence-based expansion — wait for demonstrated adoption before granting
  access to more powerful or complex surfaces. This pattern complements the bottom-up
  discovery, top-down scale deployment pattern in `blog-anthropic-cowork-deploy-guide.md`
  Claim 8, applied at the Desktop surface level rather than the Cowork plugin level.

### Claim 7: A Microsoft 365 connector provides access to mail and documents through the organization's own Entra app with tenant allowlisting and beta support for GCC High/DoD endpoints

- **Evidence**: First-party feature description with explicit beta status for GCC
  High/DoD.
- **Confidence**: settled (GA feature) / emerging (GCC High/DoD endpoint support is beta)
- **Quote**: "A Microsoft 365 connector gives Claude access to mail and documents through
  your own Entra app, with tenant allowlisting and beta support for GCC High/DoD endpoints."
- **Our assessment**: Two claims are bundled here. The first (M365 connector via the org's
  Entra app) is the standard enterprise M365 integration, where Claude accesses mail and
  documents through the organization's own registered Entra application — not through
  Anthropic's Entra app — which means data access follows the organization's own
  permission model. Tenant allowlisting prevents cross-tenant data access. The second
  (beta GCC High/DoD endpoint support) is the first corpus mention of GCC High and DoD
  endpoints for Claude Desktop. GCC High/DoD are US government-classified cloud
  environments (IL4/IL5 data). The beta status means this is not yet production-ready
  for sensitive government workloads.

### Claim 8: A local connector option limits data movement strictly to the device and Microsoft, satisfying the strictest data residency requirements

- **Evidence**: First-party feature description with an explicit data-flow constraint.
- **Confidence**: settled (first-party technical description of a shipping feature)
- **Quote**: "For the strictest residency requirements, use our local connector, and the
  connection stays between the device and Microsoft."
- **Our assessment**: This is the data residency headline claim in the deployment
  controls section. The local connector explicitly limits where Claude's data connections
  go: device → Microsoft only, with no Anthropic infrastructure in the data path for
  that connector. This addresses a real enterprise blocker: organizations with strict
  data residency requirements (e.g., financial data that cannot leave a specific
  regulatory boundary, or government data that cannot route through commercial Anthropic
  infrastructure) have an option that keeps data entirely within the device-to-Microsoft
  path. No prior corpus source documents a connector option that explicitly routes
  around Anthropic infrastructure for data residency compliance.

### Claim 9: Hanwha Solutions deployed Claude Desktop to hundreds of users worldwide via their existing LLM Gateway, using one team and no separate vendor contract or heavy infrastructure build-out

- **Evidence**: Named customer testimonial from a named individual with specific
  deployment claims (hundreds of users worldwide, via existing LLM Gateway, one team,
  no separate vendor contract).
- **Confidence**: anecdotal (single named testimonial; no independent verification;
  specific deployment details are self-reported)
- **Quote**: "We rolled out Claude Desktop fast through our existing cloud environment
  — no separate vendor contract. Our own LLM Gateway let one team deploy it to hundreds
  of users worldwide, with no heavy infrastructure build-out." — Sarang Oh, Analytics/AI
  Team Leader, Hanwha Solutions
- **Our assessment**: The Hanwha Solutions case is the only customer evidence in this
  announcement. It makes three specific operational claims: (1) no separate vendor
  contract — deploying Claude Desktop through their existing cloud provider avoided a new
  Anthropic contract negotiation; (2) LLM Gateway integration — they routed Claude
  Desktop through their internal LLM gateway, enabling centralized usage tracking and
  policy enforcement without modifying each user's deployment; (3) hundreds of users
  worldwide from one team — a small team achieved enterprise-wide scale. The LLM Gateway
  detail is the most operationally useful: it suggests that organizations with existing
  AI infrastructure (LLM gateways, internal routing layers) can use those to manage
  Claude Desktop traffic rather than configuring each deployment separately. This aligns
  with the "deploy like any app you already manage" framing in the deployment controls
  section.

## Concrete Artifacts

### Feature Availability Change (June 22, 2026)

```
# Claude Desktop — Cloud Provider Feature Matrix Change
# Source: claude.com/blog, June 22, 2026

BEFORE (before June 22, 2026):
  Cloud provider deployments (AWS, Google Cloud, Microsoft Foundry):
    ✓ Claude Cowork
    ✓ Claude Code
    ✗ Chat (not available)

AFTER (as of June 22, 2026):
  Cloud provider deployments (AWS, Google Cloud, Microsoft Foundry):
    ✓ Chat
    ✓ Claude Cowork
    ✓ Claude Code
    — Each surface has its own policy key for access control
    — Hard-deny rules apply across every tab org-wide
```

### Desktop Deployment Controls Summary

```
# Claude Desktop Enterprise Deployment Controls (June 22, 2026)
# Source: https://claude.com/blog/the-full-claude-desktop-experience-on-aws-google-cloud-and-microsoft-foundry

AUTHENTICATION:
  "Employees use the same work account they use for everything else:
   IAM Identity Center, Workforce Identity Federation, Microsoft Entra ID,
   or any OIDC provider like Okta. No shared keys to rotate, no cloud
   credentials on end-user machines."

MDM DEPLOYMENT:
  "Export policy templates from the setup UI and push them through Intune,
   GPO, or Jamf. An offline installer covers air-gapped environments."

PRE-ROLLOUT VALIDATION:
  "Test every connector, confirm which Claude models your provider serves,
   and verify the connection, all before rollout."
  Model guard: "keeps routing on Claude, including in GovCloud, even if
   a setting is misconfigured."

STAGED ROLLOUT (per-surface policy keys):
  "Chat, Claude Cowork, and Claude Code each have their own policy key,
   so you can give non-technical teams chat and Claude Cowork, engineering
   Claude Code, and then broaden access as teams adopt each surface."
  "Your hard-deny rules apply across every tab."

DATA RESIDENCY:
  M365 connector: "gives Claude access to mail and documents through your
   own Entra app, with tenant allowlisting and beta support for GCC
   High/DoD endpoints."
  Local connector: "For the strictest residency requirements, use our
   local connector, and the connection stays between the device and Microsoft."
```

### Customer Deployment Evidence

```
# Hanwha Solutions Claude Desktop Deployment
# Source: claude.com/blog, June 22, 2026
# Contact: Sarang Oh, Analytics/AI Team Leader, Hanwha Solutions

Claim:  "We rolled out Claude Desktop fast through our existing cloud
        environment — no separate vendor contract. Our own LLM Gateway
        let one team deploy it to hundreds of users worldwide, with no
        heavy infrastructure build-out."

Key factors:
  - Existing cloud environment (no separate vendor contract)
  - Internal LLM Gateway (centralized routing through existing AI infra)
  - One team, hundreds of users worldwide
  - "No heavy infrastructure build-out"

Note: Self-reported; no independent verification of user count or timeline.
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-dynamic-workflows-claude-code.md` Claim 9: That note documents
    that dynamic workflows in Claude Code are available on Amazon Bedrock, Vertex AI,
    and Microsoft Foundry at the API level. This note confirms the same three-platform
    enterprise deployment strategy at the Desktop app level — both sources together
    establish that Anthropic's multi-cloud enterprise deployment covers both API access
    (dynamic workflows) and the Desktop application (this note). The platforms align
    exactly: Amazon Bedrock/AWS, Vertex AI/Google Cloud, Microsoft Foundry.
  - `blog-anthropic-enterprise-managed-auth.md` Claim 2: That note documents
    "Admins authorize a connector once, users inherit access through the IdP groups
    and roles they already have, and the connector is there the first time someone
    opens Claude." The SSO mechanism in this note (Claim 3: IAM Identity Center,
    Workforce Identity Federation, Entra ID, OIDC/Okta) is the Desktop-login-level
    counterpart of that connector-access-provisioning model. Both are IdP-first access
    patterns; this note handles Desktop login, enterprise-managed-auth handles MCP
    connector provisioning after login.
  - `blog-anthropic-cowork-enterprise.md` Claim 1 (SCIM RBAC): Per-user group
    capability control at workspace level (SCIM groups → custom roles → capabilities).
    This note's per-surface policy keys operate at a coarser, app-level granularity.
    Together they form two layers of access control: org-wide surface access via
    policy keys (this note) + team-level capability control within surfaces (SCIM RBAC).
  - `blog-anthropic-workload-identity-federation.md` Claim 3 (short-lived, scoped
    credentials): WIF is about API workload authentication; this note's SSO references
    Workforce Identity Federation as a user login method. Both are OIDC-based patterns
    from the same underlying authentication standard applied at different layers — API
    workloads (WIF) and human users (Desktop SSO). Together they describe a complete
    enterprise authentication picture for Claude: human user login (this note) +
    workload API auth (WIF note) + connector provisioning (enterprise-managed-auth note).

- **Extends**:
  - `blog-anthropic-cowork-deploy-guide.md`: That guide covers the five-level maturity
    model and three-phase deployment roadmap for Claude Cowork but does not address
    AWS/GCP/Azure-specific deployment options or the cloud-provider Desktop path.
    This note adds the cloud-provider deployment dimension to the enterprise adoption
    landscape. Practitioners following the deploy-guide roadmap and using AWS, GCP,
    or Azure should now use the cloud-provider Desktop path rather than the direct
    Claude Desktop path.
  - `blog-anthropic-enterprise-managed-auth.md` (June 18, 2026): That note covers
    MCP connector access provisioning via IdP (the "after login" access layer). This
    note (June 22, 2026) covers the Desktop login itself and the app-level access
    controls. Together they advance the enterprise Claude Desktop deployment lifecycle:
    SSO login setup (this note) → connector access provisioning (enterprise-managed-auth)
    → connector observability (connector-observability note). A more complete enterprise
    Desktop management lifecycle emerges from the three sources in sequence.

- **Contradicts**: None identified. No existing corpus note makes claims about the
  feature availability in cloud-provider Desktop deployments that contradict this
  announcement. No contradiction issues to file.

- **Novel**:
  - **Claude Desktop as a three-surface managed app via cloud providers**: This is the
    first corpus source documenting that Chat, Cowork, and Code are available together
    in a single cloud-provider-managed Desktop deployment on AWS, Google Cloud, and
    Microsoft Foundry. Prior corpus sources referenced these platforms for API and
    dynamic workflow access but not for the Desktop application.
  - **Per-surface policy keys as a Desktop access control primitive**: The separate
    policy keys for Chat, Cowork, and Code are a new access control mechanism not
    documented in prior corpus sources. Distinct from workspace-level SCIM RBAC and
    from API-level capability controls.
  - **Model guard for GovCloud routing consistency**: The "model guard keeps routing
    on Claude, including in GovCloud" is the first corpus mention of (a) a model-guard
    feature for Desktop deployments and (b) GovCloud as a supported deployment context.
  - **Local connector for device-to-Microsoft-only data flow**: The explicit data
    residency option that routes connector data solely between device and Microsoft
    (no Anthropic infrastructure) is a new data residency pattern. No prior corpus
    source documents a Claude connector that explicitly excludes Anthropic from the
    data path.
  - **GCC High/DoD endpoint beta support**: First corpus mention of US government
    classified cloud endpoint support (GCC High/DoD) for Claude Desktop.
  - **Air-gapped deployment via offline installer**: First corpus mention of an offline
    installer for Claude Desktop for air-gapped environments.
  - **LLM Gateway as a Desktop deployment integration pattern**: Hanwha's deployment
    via an internal LLM Gateway is the first corpus evidence of organizations routing
    Claude Desktop through their own AI infrastructure gateway.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add cloud-provider-hosted Claude Desktop as a
  deployment option for enterprise teams. Previously, the guide's coverage of AWS/GCP/
  Azure focused on API access (Claude API via Bedrock/Vertex AI/Foundry) or dynamic
  workflows. This note establishes that the full Desktop application (Chat + Cowork +
  Code) is now available through these platforms, enabling organizations already on
  one of the three cloud providers to deploy the Desktop without a separate Anthropic
  SaaS contract. Document the per-surface policy key mechanism as the Desktop-level
  access control primitive.

- **Chapter 05 (Team Adoption)**: Update the enterprise deployment options to include
  the cloud-provider Desktop path alongside the direct Claude.ai path. Organizations
  that use AWS, GCP, or Azure as their primary cloud infrastructure can deploy Claude
  Desktop through their existing cloud account (no separate vendor contract) using
  existing MDM tooling (Intune, GPO, Jamf) and existing SSO (IAM Identity Center,
  Workforce Identity Federation, Entra ID, OIDC/Okta). The Hanwha Solutions deployment
  (hundreds of users, one team, via LLM Gateway) provides concrete evidence for the
  "quick enterprise rollout via existing cloud infrastructure" pattern. The staged
  rollout pattern (per-surface policy keys: Chat → Cowork → Code) is a Desktop-level
  analog to the bottom-up discovery, top-down scale pattern in `blog-anthropic-cowork-deploy-guide.md`.

- **Chapter 06 (Security and Threat Model)**: Add the local connector (device-to-Microsoft
  only, no Anthropic routing) as a data residency option for organizations with the
  strictest residency requirements. Add the model guard for GovCloud as a misconfiguration
  guardrail. Note that GCC High/DoD endpoint support is in beta (not production-ready
  for classified data as of June 2026). The SSO-only authentication model ("no cloud
  credentials on end-user machines") should be documented as the enterprise security
  baseline for Desktop deployments.

- **Chapter 08 (Enterprise patterns / multi-cloud)**: This note is the primary source
  for the cloud-provider Desktop deployment pattern. Document: (a) which providers are
  supported, (b) the cloud-provider-specific SSO options (IAM Identity Center/AWS,
  Workforce Identity Federation/GCP, Entra ID/Azure), (c) the M365 connector with
  tenant allowlisting as the standard Microsoft data integration, (d) the local
  connector as the strict-residency variant, and (e) the LLM Gateway integration
  pattern (Hanwha) as an advanced deployment option for organizations with existing
  AI infrastructure.

## Extraction Notes

- Source fetched June 23, 2026. The claude.com blog renders as a JavaScript SPA;
  WebFetch returns model-generated summaries rather than verbatim text. Multiple
  targeted fetches were performed: one for overall structure (headings and first
  sentences), one for full verbatim text under each section, and one for any missed
  content. All quoted text in this note was extracted in verbatim-targeting fetches
  and appeared consistently across multiple fetches. The customer testimonial
  (Sarang Oh, Hanwha Solutions) was extracted in a dedicated verbatim fetch.
- The blog post is intentionally short (~500 words). No sub-pages were linked from
  the deployment-controls section. The "Getting started" section directs admins to a
  deployment guide (not linked as a sub-page in the post) and to their account team.
  The linked deployment guide was not followed as it was not accessible via WebFetch.
- The "Workforce Identity Federation" in Claim 3 refers to the enterprise SSO concept
  (used by Google Cloud's Workforce Identity Federation product) as a user-login
  mechanism for Claude Desktop — this is distinct from Anthropic's Workload Identity
  Federation (WIF) documented in `blog-anthropic-workload-identity-federation.md`,
  which covers OIDC-based authentication from API workloads to the Claude Platform.
  The two share naming conventions but operate at different authentication boundaries.
- No pricing information is provided for the cloud-provider-hosted Desktop offering.
  The announcement does not clarify whether costs are billed through the cloud
  provider (Bedrock/Vertex/Foundry pricing) or through a separate Anthropic Claude
  plan.
- Confidence overall is "emerging" because while the feature availability claims are
  first-party and settled, the deployment-in-practice patterns (LLM Gateway integration,
  staged rollout effectiveness) rest on a single customer testimonial and vendor-prescribed
  guidance, not externally validated enterprise evidence.
