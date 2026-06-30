---
source_url: https://claude.com/blog/introducing-the-claude-apps-gateway
source_type: blog-post
title: "Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud"
author: Anthropic (no individual byline)
date_published: 2026-06-29
date_extracted: 2026-06-30
last_checked: 2026-06-30
status: current
confidence_overall: emerging
issue: "#1355"
---

# Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud

> Official Anthropic announcement (June 29, 2026) of the Claude apps gateway — a
> self-hosted control plane that adds corporate SSO, centrally enforced policy,
> role-based access, and per-user cost attribution to Claude Code deployments on
> Amazon Bedrock and Google Cloud, shipping as a stateless Linux container inside
> the existing `claude` binary.

## Source Context

- **Type**: blog-post (official claude.com/blog, June 29, 2026; no individual
  byline; product announcement for a shipping feature, not a research preview)
- **Author credibility**: First-party Anthropic product announcement on the same
  channel as the June 22, 2026 Claude Desktop cloud platforms post and the June 18,
  2026 enterprise-managed-auth post. Claims about feature behavior, supported identity
  providers, architecture, and data residency guarantees are vendor-authoritative.
  No third-party customer testimonials appear in the post.
- **Scope**: Covers the apps gateway for Amazon Bedrock and Google Cloud deployments
  of Claude Code: (1) the three operational problems it solves (per-developer cloud
  credentials, manual settings distribution, lack of per-developer spend visibility);
  (2) the gateway's control plane capabilities (SSO, policy enforcement, spend caps,
  telemetry); (3) the deployment architecture (stateless container, PostgreSQL,
  OIDC); (4) client-side configuration (`managed-settings.json`, `forceLoginMethod`,
  `forceLoginGatewayUrl`); (5) the data residency guarantee for Bedrock/GCP
  deployments; and (6) the announcement of an open protocol so third-party gateway
  developers can implement compatible features. Does NOT cover: Claude.ai or Claude
  Desktop authentication (separate product paths), pricing, specific gateway
  performance SLAs, the detailed `gateway.yaml` configuration schema, specific
  managed-settings fields beyond model selection and defaults, or any customer
  case studies. The post links to documentation but does not reproduce configuration
  schemas inline.

## Extracted Claims

### Claim 1: Before the gateway, running Claude Code on Amazon Bedrock or Google Cloud required provisioning a cloud credential per developer, manually pushing settings to every laptop, and standing up separate tooling to track per-developer spend

- **Evidence**: Opening problem statement in the announcement, framing the motivation
  for the new gateway feature.
- **Confidence**: settled (first-party problem framing that motivated the feature;
  the three operational gaps are structural properties of the pre-gateway deployment
  model)
- **Quote**: "Previously, running Claude Code on these platforms has meant provisioning
  a cloud credential per developer, manually pushing settings to every laptop, and
  standing up separate tooling to see per-developer spend."
- **Our assessment**: The three-problem framing is the clearest statement of the
  enterprise Claude Code deployment gap on Bedrock and GCP before this announcement.
  Each gap represents a category of operational friction: (1) credential distribution
  — manual, per-developer cloud credential provisioning is an IT bottleneck that
  doesn't scale and creates lingering-access risk when developers leave; (2) settings
  management — manually pushing settings to every developer laptop creates drift and
  prevents org-wide policy enforcement; (3) spend observability — without per-developer
  spend data, finance and engineering managers cannot attribute costs, set budgets, or
  detect runaway usage. The gateway directly addresses all three in one component. For
  teams currently operating Claude Code on Bedrock or GCP without a gateway, this
  tripling of problems is the adoption ceiling.

### Claim 2: The Claude apps gateway is a self-hosted control plane providing corporate SSO, centrally enforced policy, role-based access, and per-user cost attribution for Claude Code

- **Evidence**: Core feature description from the announcement's opening paragraph.
- **Confidence**: settled (first-party feature description of a shipping capability)
- **Quote**: "The gateway is a self-hosted control plane that gives you corporate SSO
  login, centrally enforced policy, role-based access, and per-user cost attribution
  for Claude Code."
- **Our assessment**: The "self-hosted" property is the defining architectural
  characteristic: the gateway runs on operator infrastructure, not Anthropic's. This
  means operator data residency requirements are honored by default for non-Claude-API
  routing paths. "Centrally enforced policy" and "role-based access" position the
  gateway as the single enforcement point for org-wide Claude Code governance —
  analogous to what an LDAP/AD server is for Unix access or what an MCP proxy is for
  connector access. "Per-user cost attribution" is the financial control layer that
  was absent before this announcement.

### Claim 3: The gateway runs as a single stateless container on Linux backed by PostgreSQL, minimizing infrastructure footprint

- **Evidence**: Direct architectural description in the announcement.
- **Confidence**: settled (first-party architectural claim about a shipping deployment
  model)
- **Quote**: "The gateway is run as a single stateless container deployed on Linux and
  backed by a PostgreSQL database"
- **Our assessment**: "Single stateless container" is the most important word cluster
  for DevOps planning. "Stateless" means the container itself holds no persistent state
  — state lives in PostgreSQL — which enables standard container orchestration patterns:
  horizontal scaling, rolling restarts, blue/green deployments, and recovery from
  container failure without data loss. "Single" means the operational model is
  deliberately minimalist: one container type to manage. The PostgreSQL backing is the
  only external state dependency. This architecture is deployable in any Kubernetes
  cluster, ECS, Cloud Run, or bare-metal Linux environment with a Postgres instance.
  The footprint is intentionally comparable to deploying a typical enterprise web
  service — not specialized AI infrastructure.

### Claim 4: The gateway authenticates developers against the organization's identity provider via OIDC, supporting Google Workspace, Microsoft Entra ID, Okta, or any standards-compliant OIDC provider

- **Evidence**: Direct feature description of the authentication mechanism and named
  supported providers.
- **Confidence**: settled (first-party feature description with named providers)
- **Quote**: "It acts as an OpenID Connect (OIDC) relying party against Google
  Workspace, Microsoft Entra ID, Okta, or any standards-compliant OIDC provider"
- **Our assessment**: OIDC relying party is the standard enterprise SSO pattern —
  the gateway exchanges the developer's IdP session token for authorized access to
  Claude Code, with no shared static credentials distributed to individual developers.
  The three named IdPs (Google Workspace, Entra ID, Okta) cover the dominant enterprise
  identity ecosystems: Google-first organizations, Microsoft-first organizations, and
  organizations using a standalone IdP. The "any standards-compliant OIDC provider"
  tail means the gateway works with PingFederate, Auth0, Keycloak, and other OIDC
  implementations. This is the same OIDC-first authentication architecture as the
  enterprise-managed-auth connector provisioning (`blog-anthropic-enterprise-managed-auth.md`
  Claim 4) and the WIF workload authentication (`blog-anthropic-workload-identity-federation.md`
  Claim 3), applied specifically to developer-to-gateway authentication.

### Claim 5: Managed settings are defined once on the gateway server and automatically distributed to clients at sign-in; the gateway enforces policy on every subsequent request

- **Evidence**: Feature description in the "How the gateway works" section of the
  announcement.
- **Confidence**: settled (first-party feature description)
- **Quote**: "You can define managed settings once on the server, and clients receive
  the policy at sign-in"
- **Quote (enforcement)**: "gateway enforces it on every request"
- **Our assessment**: The "define once, receive at sign-in" architecture eliminates
  the second pre-gateway operational gap (manually pushing settings to every laptop).
  Sign-in is the synchronization point: whenever a developer logs in to Claude Code,
  they automatically receive the current org-wide managed settings — allowed models,
  default configuration, policy restrictions — without manual distribution. The
  "enforces it on every request" enforcement means policy cannot be bypassed by
  modifying local client settings after sign-in; the gateway re-applies the org policy
  at the API call level. This is a server-side enforcement model, not a client-side
  honor-system model.

### Claim 6: Claude Code usage telemetry is stamped per-request by the client and relayed by the gateway over OTLP to an operator-configured collector in the operator's own network on the operator's own retention schedule

- **Evidence**: Direct feature description in the announcement.
- **Confidence**: settled (first-party feature description of a specific data flow)
- **Quote**: "The client stamps a usage metric for every request, and the gateway
  relays it over OTLP to a collector you configure, in your network and on your
  retention schedule."
- **Our assessment**: The OTLP-to-operator-collector pattern is architecturally
  significant for two reasons. First, OpenTelemetry Protocol (OTLP) is the industry
  standard observability wire format — organizations already running Prometheus,
  Grafana, Datadog, or Honeycomb OTLP pipelines can ingest Claude Code usage data
  into their existing observability stack without a separate analytics system. Second,
  "in your network and on your retention schedule" means usage data never leaves the
  operator's infrastructure unless the operator explicitly routes it elsewhere — the
  gateway does not send telemetry to Anthropic, and the operator controls how long
  usage records are kept. This closes the compliance gap for organizations with data
  residency requirements on usage metadata (not just inference traffic). Together with
  Claim 9's inference traffic residency guarantee, the gateway provides end-to-end
  data residency: neither inference content nor usage metadata leaves the operator's
  infrastructure.

### Claim 7: The gateway enables per-organization, per-group, and per-user spend limits with daily, weekly, and monthly granularity

- **Evidence**: Direct feature description in the announcement.
- **Confidence**: settled (first-party feature description with explicit time and
  scope granularities)
- **Quote**: "The gateway allows you to set daily, weekly, and monthly spend limits.
  Limits can be applied per organization, group, or user"
- **Our assessment**: The three-dimensional spend control matrix (time dimension:
  daily/weekly/monthly × scope dimension: org/group/user) is the most granular cost
  governance mechanism documented in the corpus for Claude Code specifically. Finance
  teams can set org-wide monthly budgets; engineering managers can set per-team weekly
  budgets; and individual developer daily limits can be applied to prevent runaway
  usage from a single session. The combination of scopes means limits compose: a
  developer can be simultaneously subject to a personal daily limit, a team weekly
  limit, and an org monthly limit — whichever binding limit is reached first applies.
  This is the per-developer spend tracking solution to the third pre-gateway operational
  gap (Claim 1), now delivered as a configurable control rather than passive reporting.

### Claim 8: The gateway holds the organization's upstream cloud credential and routes inference requests to the Claude API, Amazon Bedrock, or Google Cloud, with optional failover between providers

- **Evidence**: Direct feature description of the routing architecture.
- **Confidence**: settled (first-party feature description of a shipping routing
  capability)
- **Quote**: "The gateway holds your upstream credential and routes inference to the
  Claude API, Amazon Bedrock, or Google Cloud, with optional failover between providers."
- **Our assessment**: The gateway is the single credential holder for the organization's
  cloud provider API access — individual developer machines hold no cloud credentials.
  This is the solution to the first pre-gateway operational gap (Claim 1): instead of
  provisioning and distributing cloud credentials per developer, the organization
  provisions one credential in the gateway and routes all developer inference through
  it. The "optional failover between providers" is an availability feature: if
  inference to Amazon Bedrock is unavailable, the gateway can automatically route to
  Google Cloud (or the Claude API), improving reliability for time-sensitive developer
  workloads without requiring developer-side failover configuration.

### Claim 9: Bedrock and Google Cloud deployments through the gateway do not send inference traffic or usage data to Anthropic — a data sovereignty guarantee for organizations with strict residency requirements

- **Evidence**: Direct statement in the announcement about the data flow from
  gateway-routed deployments.
- **Confidence**: settled (first-party explicit data residency claim; this is an
  architectural property of routing to Bedrock/GCP rather than Claude API)
- **Quote**: "The gateway does not send inference traffic or usage data to Anthropic
  unless you configure it to use the Claude API"
- **Our assessment**: This is the key data sovereignty statement for Bedrock and
  Google Cloud deployments. When organizations route Claude Code through the gateway
  to Bedrock or GCP, two data categories stay within the cloud provider's boundaries:
  (1) inference traffic (the prompts and completions) — which flows developer → gateway
  → Bedrock/GCP, never to Anthropic; and (2) usage data (the telemetry described in
  Claim 6) — which flows to the operator's OTLP collector, not to Anthropic. The
  "unless you configure it to use the Claude API" carve-out is important: if the
  organization routes through the Claude API instead, data flows to Anthropic's
  infrastructure as in any Claude API call. The default Bedrock/GCP path is the
  residency-safe path; Claude API routing is an opt-in.

### Claim 10: The gateway ships inside the same `claude` binary developers already install — no separate gateway binary or package required

- **Evidence**: Description of the delivery mechanism in the announcement.
- **Confidence**: settled (first-party delivery mechanism claim)
- **Quote**: "is built and shipped by Anthropic inside the same `claude` binary your
  developers already install"
- **Our assessment**: The single-binary distribution model is significant for
  enterprise deployment friction. Developers who have already installed the Claude
  Code CLI do not need to install a new package to get gateway support — the gateway
  is already present in the binary they have. For the operator side: the gateway
  server is not a separate download from a different source; it comes from the same
  `claude` binary installation. This means the gateway stays synchronized with the
  client by construction — when the binary is updated, both client and gateway update
  together. No "gateway version is incompatible with client version" failure mode
  exists.

### Claim 11: Deploying the gateway requires pointing `gateway.yaml` at an OIDC issuer and upstream credential, then configuring `forceLoginMethod` and `forceLoginGatewayUrl` in `managed-settings.json` on client machines

- **Evidence**: Deployment procedure description in the "Getting started" section
  of the announcement.
- **Confidence**: settled (first-party deployment procedure)
- **Quote (server-side)**: "Download the Claude Code CLI binary, point `gateway.yaml`
  at your OIDC issuer and upstream credential, and register one OIDC app in your IdP"
- **Quote (client-side)**: "Configure the `forceLoginMethod` and
  `forceLoginGatewayUrl` parameters in `managed-settings.json` on client machines."
- **Our assessment**: The deployment procedure has two configuration surfaces: the
  gateway server side (`gateway.yaml` with OIDC issuer and upstream Bedrock/GCP
  credential) and the client side (`managed-settings.json` with the two `force*`
  parameters that redirect the Claude Code login flow to the gateway). The client-side
  configuration is a standard managed settings push — the same MDM or policy template
  mechanism an organization already uses to push corporate laptop settings can deploy
  `forceLoginMethod` and `forceLoginGatewayUrl`. The `forceLogin*` naming implies
  these are mandatory redirect parameters: once set, the Claude Code client cannot
  bypass the gateway login flow.

### Claim 12: Anthropic is publishing the gateway protocol as an open specification so third-party gateway developers can build compatible implementations

- **Evidence**: Direct statement in the announcement.
- **Confidence**: settled (first-party intent claim; the open protocol commitment is
  stated explicitly)
- **Quote**: "We're also publishing the protocol the gateway uses, so other gateway
  developers can implement the same features."
- **Our assessment**: The open protocol commitment is architecturally significant for
  the enterprise ecosystem. It means the Claude apps gateway is not a proprietary
  Anthropic-only integration point; organizations with existing LLM gateway infrastructure
  (like the Hanwha Solutions LLM Gateway described in `blog-anthropic-claude-desktop-cloud-platforms.md`
  Claim 9) can potentially build Claude Code integration into their own gateways
  without deploying a second control plane. The "same features" phrasing implies the
  protocol specification covers SSO login, managed settings distribution, telemetry
  relay, and spend enforcement — not just basic request routing. This mirrors the open
  MCP extension pattern established for enterprise-managed auth
  (`blog-anthropic-enterprise-managed-auth.md` Claim 7), where Anthropic published an
  open standard and implemented it first, inviting third-party connector developers to
  follow.

## Concrete Artifacts

### Problem Statement and Solution Architecture

```
# Claude Apps Gateway: Pre/Post Comparison
# Source: "Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud"
# Anthropic, June 29, 2026 — https://claude.com/blog/introducing-the-claude-apps-gateway

BEFORE (pre-gateway, Claude Code on Bedrock/GCP):
  Credential distribution: "provisioning a cloud credential per developer"
  Settings management:     "manually pushing settings to every laptop"
  Spend visibility:        "standing up separate tooling to see per-developer spend"

AFTER (with apps gateway):
  "The gateway is a self-hosted control plane that gives you corporate SSO login,
   centrally enforced policy, role-based access, and per-user cost attribution
   for Claude Code."
```

### Gateway Architecture

```
# Claude Apps Gateway — Deployment Architecture
# Source: "Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud"
# Anthropic, June 29, 2026

RUNTIME:
  "The gateway is run as a single stateless container deployed on Linux and
   backed by a PostgreSQL database"
  "run it in one stateless container on your infrastructure"

DISTRIBUTION:
  "is built and shipped by Anthropic inside the same `claude` binary your
   developers already install"
  (Gateway and client are co-shipped; gateway-aware /login flow included)

AUTHENTICATION:
  "It acts as an OpenID Connect (OIDC) relying party against Google Workspace,
   Microsoft Entra ID, Okta, or any standards-compliant OIDC provider"
  "authenticates developers against your identity provider"

ROUTING:
  "The gateway holds your upstream credential and routes inference to the Claude
   API, Amazon Bedrock, or Google Cloud, with optional failover between providers."

DATA RESIDENCY:
  "The gateway does not send inference traffic or usage data to Anthropic unless
   you configure it to use the Claude API"
```

### Policy and Spend Management

```
# Claude Apps Gateway — Policy and Cost Controls
# Source: "Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud"
# Anthropic, June 29, 2026

MANAGED SETTINGS:
  "You can define managed settings once on the server, and clients receive the
   policy at sign-in"
  "gateway enforces it on every request"
  (Allowed models and default settings can be adjusted centrally)

TELEMETRY:
  "The client stamps a usage metric for every request, and the gateway relays it
   over OTLP to a collector you configure, in your network and on your retention
   schedule."

SPEND CONTROLS:
  "The gateway allows you to set daily, weekly, and monthly spend limits.
   Limits can be applied per organization, group, or user"
```

### Deployment Configuration

```
# Claude Apps Gateway — Setup Summary
# Source: "Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud"
# Anthropic, June 29, 2026

SERVER-SIDE SETUP:
  "Download the Claude Code CLI binary, point `gateway.yaml` at your OIDC issuer
   and upstream credential, and register one OIDC app in your IdP"

CLIENT-SIDE CONFIGURATION:
  "Configure the `forceLoginMethod` and `forceLoginGatewayUrl` parameters in
   `managed-settings.json` on client machines."

LOGIN FLOW INTEGRATION:
  "The gateway and the client are built together, the `/login` flow is
   gateway-aware, the client applies managed settings automatically at sign-in"

OPEN PROTOCOL:
  "We're also publishing the protocol the gateway uses, so other gateway developers
   can implement the same features."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-claude-desktop-cloud-platforms.md` Claim 3: That note documents
    Desktop SSO using "IAM Identity Center, Workforce Identity Federation, Microsoft
    Entra ID, or any OIDC provider like Okta. No shared keys to rotate, no cloud
    credentials on end-user machines." The apps gateway's OIDC relying party pattern
    (Claim 4 here) is the developer-focused counterpart — the same no-shared-keys OIDC
    principle applied to Claude Code authentication instead of Desktop app login. Both
    are part of Anthropic's consistent OIDC-first enterprise authentication strategy,
    applied at different product layers.
  - `blog-anthropic-enterprise-managed-auth.md` Claim 4: "For admins, this folds MCP
    access management into the same workflow that governs the rest of your stack:
    provision once, scope by group, manage revocation through the IdP." The apps
    gateway's managed settings model (Claim 5 here: "define once on the server, clients
    receive the policy at sign-in") implements the same "provision once at the center"
    pattern for Claude Code policies that enterprise-managed-auth implements for MCP
    connector access. Both centralize governance through server-side definition and IdP
    integration, eliminating per-user and per-device configuration steps.
  - `blog-anthropic-workload-identity-federation.md` Claim 3: Short-lived, scoped
    OIDC credentials replace static secrets. The apps gateway's OIDC relying party
    pattern (Claim 4 here) applies this same short-lived credential principle to
    developer-to-gateway authentication — no static cloud API keys on developer
    machines, replaced by IdP-issued OIDC tokens that expire with the session. Together
    WIF (API workload → Claude Platform auth) + apps gateway (developer → gateway auth)
    form a layered OIDC-first credential architecture for both human users and automated
    workloads in Bedrock/GCP deployments.
  - `blog-anthropic-enterprise-managed-auth.md` Claim 7: The enterprise-managed-auth
    extension ("built on an open standard so any connector can support it") and this
    note's Claim 12 ("publishing the protocol the gateway uses, so other gateway
    developers can implement the same features") follow the same strategy: Anthropic
    implements a feature first, then publishes the underlying protocol/standard for
    third-party adoption. Both announcements are from June 2026, suggesting a
    deliberate open-protocol strategy across the enterprise tooling layer.

- **Extends**:
  - `blog-anthropic-claude-desktop-cloud-platforms.md`: That note (June 22, 2026)
    covers the Claude Desktop app experience — Chat, Cowork, and Code — as a unified
    managed application deployed through AWS, Google Cloud, and Microsoft Foundry,
    targeting non-technical and knowledge workers alongside engineers. This note (June
    29, 2026) covers the apps gateway specifically for Claude Code, targeting
    developer-specific deployment concerns: per-developer cloud credentials, developer
    spend management, programmatic settings distribution. Together, the two June 2026
    announcements describe Anthropic's complete enterprise deployment architecture on
    cloud providers: unified Desktop app (all surfaces, all users) + apps gateway
    (developer-specific control plane). The Desktop note covers how non-engineering
    users access Claude through cloud providers; this note covers how engineering teams
    deploy and govern Claude Code specifically.
  - `blog-anthropic-enterprise-managed-auth.md`: Enterprise-managed-auth (June 18,
    2026) provides IdP-provisioned access to MCP connectors — the "what tools can this
    user access?" layer. The apps gateway (June 29, 2026) provides the developer
    authentication and policy enforcement layer — the "who is this developer and what
    Claude configuration do they get?" layer. Together they cover two dimensions of
    enterprise Claude Code governance: developer identity + tool access. The three June
    2026 announcements (enterprise-managed-auth → Desktop cloud platforms → apps
    gateway) form a sequential build-out of enterprise governance primitives across
    different Claude product layers.
  - `blog-anthropic-cowork-enterprise.md`: That note documents group spend limits for
    Claude Cowork (one of the four enterprise governance controls). The apps gateway
    extends the same spend management pattern to Claude Code with greater granularity:
    per-org/group/user limits at daily/weekly/monthly time horizons (Claim 7 here),
    vs. the group-level spend controls in Cowork. Together they establish spend limits
    as a cross-product enterprise governance primitive that Anthropic is standardizing
    across its product surface.

- **Contradicts**: None identified. The apps gateway operates in a distinct deployment
  and authentication domain from the existing corpus claims. No contradiction issues
  to file.

- **Novel**:
  - **Self-hosted control plane for Claude Code on Bedrock/GCP**: This is the first
    corpus source documenting a purpose-built, self-hosted enterprise deployment
    component specifically for Claude Code on Amazon Bedrock and Google Cloud. Prior
    corpus sources covered API-level access (WIF) and Desktop-app-level access (cloud
    platforms note) but not a developer-specific control plane.
  - **Stateless container + PostgreSQL architecture for Claude Code enterprise
    deployment**: First corpus specification of a concrete infrastructure blueprint
    for enterprise Claude Code operations. The single-stateless-container design
    makes this the lowest-footprint enterprise AI gateway architecture documented in
    the corpus.
  - **Per-developer, per-group, per-org daily/weekly/monthly spend limits for Claude
    Code**: The three-dimensional spend control matrix (time × scope granularity) is
    new to the corpus for Claude Code specifically. Cowork has group spend limits; the
    apps gateway adds daily/weekly/monthly time granularity and extends to user-level
    limits.
  - **OTLP telemetry with operator-controlled retention in operator's own network**:
    The specific architectural guarantee — client stamps usage per request, gateway
    relays to operator's OTLP collector, data stays in operator's network on
    operator's retention schedule — is the first corpus documentation of this complete
    data-residency-safe telemetry path for Claude Code usage.
  - **Dual data residency guarantee (inference traffic + usage metadata)**: The
    explicit statement that neither inference traffic nor usage data leaves the
    operator's infrastructure when routing through Bedrock/GCP is the most complete
    data sovereignty claim in the corpus. Prior notes cover inference routing (Bedrock,
    GCP) but not the explicit combination of inference + metadata residency.
  - **Open gateway protocol**: The commitment to publish the gateway protocol for
    third-party implementers is the first corpus documentation of an open protocol for
    Claude Code enterprise gateway infrastructure. Parallel to the open MCP extension
    pattern, but at the control plane layer rather than the connector layer.
  - **Single-binary gateway/client co-distribution**: The co-shipping of gateway server
    and client in the same `claude` binary is a novel distribution model in the corpus —
    no version mismatch between gateway and client is possible, and no separate
    installation step is required for operators deploying the gateway server.

## Guide Impact

- **Chapter 02 (Harness Engineering — enterprise deployment architecture)**: Add the
  apps gateway as the reference enterprise deployment architecture for Claude Code on
  Amazon Bedrock and Google Cloud. Document the stateless container + PostgreSQL
  blueprint as a concrete infrastructure specification. The gateway solves the three
  pre-deployment operational gaps (Claim 1) that would otherwise block enterprise
  adoption of Claude Code on Bedrock/GCP. Engineers responsible for deploying Claude
  Code in enterprise Bedrock or GCP environments should use this as their deployment
  reference, not the per-developer cloud credential model.

- **Chapter 05 (Team Adoption — enterprise governance)**: Add the managed settings
  distribution pattern (define once on server, clients receive at sign-in, gateway
  enforces on every request) as the canonical enterprise settings management approach
  for Claude Code. The three-dimensional spend control matrix (per-org/group/user ×
  daily/weekly/monthly) should be documented as the financial governance mechanism for
  Claude Code at scale — addressing the enterprise concern about uncontrolled AI cost
  accumulation before deploying to large engineering teams.

- **Chapter 06 (Security and Threat Model)**: Document the dual data residency
  guarantee (Claim 9: no inference traffic or usage data to Anthropic on Bedrock/GCP
  paths) as a concrete property of gateway-routed deployments. This is the data
  sovereignty answer for enterprises that require Bedrock or GCP inference routing:
  the apps gateway + Bedrock/GCP path is provably residency-safe for both content and
  metadata. The OIDC relying party model (Claim 4) eliminates the static per-developer
  cloud credential as an attack surface — no credential on the developer's laptop means
  no credential to steal or misuse if a developer machine is compromised.

- **Chapter 08 (Enterprise Patterns — multi-cloud Claude Code deployment)**: This note
  is the primary source for the Bedrock/GCP enterprise Claude Code deployment pattern.
  Document: (a) the gateway as the deployment primitive, (b) the `gateway.yaml` /
  `managed-settings.json` configuration surface, (c) optional failover between Claude
  API, Bedrock, and GCP, (d) the open protocol commitment as a forward-looking signal
  for organizations with existing LLM gateway infrastructure (can integrate rather than
  replace). The June 2026 trio — enterprise-managed-auth (June 18) → Desktop cloud
  platforms (June 22) → apps gateway (June 29) — together define Anthropic's current
  enterprise deployment architecture; Chapter 08 should synthesize all three.

## Extraction Notes

1. **WebFetch returns AI-summarized content**: The claude.com blog renders as a
   JavaScript SPA; WebFetch AI-summarizes rendered content. Four separate fetches were
   performed with progressively targeted verbatim-extraction prompts. All quotes in
   this note appeared consistently across multiple fetches and are treated as verbatim
   from the source. The section headings ("Deploying the gateway," "How the gateway
   works," "Getting started") and key technical parameters (`gateway.yaml`,
   `forceLoginMethod`, `forceLoginGatewayUrl`, `managed-settings.json`) were consistent
   across all fetches.

2. **No customer testimonials**: The announcement contains no customer case studies
   or testimonials, unlike the June 22 Desktop cloud platforms post (Hanwha Solutions)
   or the June 18 enterprise-managed-auth post (HubSpot, Ramp, Webflow). This limits
   the real-world adoption evidence available from this source — all claims are
   vendor-first-party assertions about a newly-announced feature.

3. **Linked documentation not followed**: The "Getting started" section links to
   documentation for detailed configuration schema. The linked docs page was not
   followed as a sub-page because the announcement itself provides sufficient
   architectural and deployment content for the source note. A future deep-read of
   the gateway documentation would extend the concrete artifacts section significantly.

4. **Confidence is "emerging"**: While the feature availability claims are first-party
   and settled (shipping product, not research preview), the operational patterns
   described — how teams actually use managed settings, how spend limits interact at
   the boundary of multiple scopes, what the OTLP schema looks like in practice — are
   all derived solely from vendor description. No practitioner evidence, third-party
   analysis, or operational case studies corroborate these patterns. Settling from
   "emerging" to "settled" awaits practitioner reports.

5. **Amazon Bedrock vs. Google Cloud asymmetry**: The announcement title names both
   Amazon Bedrock and Google Cloud. The body does not distinguish whether any features
   differ between the two providers, or whether the gateway is available on other cloud
   providers (e.g., Microsoft Azure / Foundry). No Microsoft Foundry variant is
   mentioned in this announcement, in contrast to the June 22 Desktop note which
   explicitly includes Microsoft Foundry alongside AWS and Google Cloud.
