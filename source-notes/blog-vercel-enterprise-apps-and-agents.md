---
source_url: https://vercel.com/blog/vercel-for-enterprise-apps-and-agents
source_type: blog-post
title: "Vercel for Enterprise Apps and Agents"
author: Kim Neuwirth, Jeanne Grosser (Vercel)
date_published: 2026-06-16
date_extracted: 2026-07-16
last_checked: 2026-07-16
status: current
confidence_overall: emerging
issue: "#1928"
---

# Vercel for Enterprise Apps and Agents

> Vercel's enterprise platform announcement bundling four access/governance
> products for internally-built apps and agents — Vercel Passport (IdP-gated
> deployments), Vercel Connect (runtime-scoped credential exchange, detailed
> in a linked companion post), Enterprise Managed Users (SAML/Directory Sync
> lifecycle management), and bring-your-own-cloud on AWS (customer-owned
> compute/VPC with Vercel running only the control plane) — framed as making
> "internal" and "governed" the default state of a deployment rather than a
> per-project configuration burden.

## Source Context

- **Type**: blog-post (official Vercel Blog, `vercel.com/blog`, published
  June 16, 2026; company/product announcement, "Company News" category,
  authored by two named individuals). The article inline-links three other
  Vercel posts: `/blog/introducing-vercel-connect` (a same-day, June 17,
  2026 companion post going deep on the Connect product only briefly
  summarized here), `/blog/agent-stack`, and `/blog/introducing-eve`. Per
  MINER.md §1's "follow up to 5 linked pages that seem substantive," this
  note follows `/blog/introducing-vercel-connect` in full, since the
  Enterprise Apps and Agents post gives Connect only a two-paragraph
  summary and the companion post is the authoritative, much more detailed
  source for how Connect's credential-exchange mechanism actually works.
  `/blog/agent-stack` and `/blog/introducing-eve` are referenced only in the
  article's opening sentence ("we built them with eve on top of the Agent
  Stack") as context for Vercel's own internal tooling, not elaborated on
  anywhere in the Enterprise Apps and Agents article itself, and are outside
  this issue's triage scope (access/governance/deployment, not the agent
  framework itself) — not followed.
- **Author credibility**: First-party Vercel product announcement, with two
  named authors (Kim Neuwirth, Jeanne Grosser) and a separate three-author
  byline (Hedi Zandi, Dima Voytenko, Kevin Corbett) on the companion Connect
  post. Vercel operates the platform and products being described (Passport,
  Connect, Enterprise Managed Users, BYOC), so feature mechanics and
  availability tiers are authoritative first-party documentation of shipping
  or beta capabilities — not third-party reporting. No named customer
  quotes or case studies appear in either post (contrast with
  `blog-anthropic-claude-managed-agents-selfhosted.md`, which has five named
  customer testimonials); all claims here are vendor self-description of
  features, not independently validated deployment evidence.
- **Scope**: Covers four enterprise governance products for Vercel-deployed
  apps and agents — identity-gated internal deployments (Passport),
  runtime-scoped external-system credentials (Connect), centralized user
  lifecycle management (Enterprise Managed Users), and customer-owned
  compute (BYOC on AWS) — plus a brief mention of v0 (Vercel's AI app
  builder) connecting to Snowflake under IdP control. Does NOT cover:
  pricing for the enterprise bundle itself (Connect's per-token-request
  pricing is documented separately in the companion post and extracted
  below), technical implementation details of Passport or Enterprise
  Managed Users (only Connect gets a deep technical treatment, in the
  companion post), independent security audit or compliance-certification
  status for BYOC, or any named enterprise customer using these specific
  features (contrast with the adjacent `blog-anthropic-claude-managed-agents-selfhosted.md`
  and `blog-anthropic-enterprise-managed-auth.md`, both of which name real
  customers).

## Extracted Claims

### Claim 1: Vercel frames its own internal experience — hundreds of employee-built agents and apps — as the origin of this product bundle, with the hard problems being access/security questions that arose only after deployment, not deployment itself
- **Evidence**: The article's opening framing paragraph, presented as the vendor's own dogfooding narrative and motivation for building the four products.
- **Confidence**: anecdotal (vendor's own internal-usage narrative, not independently verified; no numbers given beyond "hundreds")
- **Quote**: "Over the past year, employees across Vercel shipped hundreds of agents and internal apps. Getting to production was the easy part, because we built them with eve on top of the Agent Stack and deployed them on Vercel. The difficult questions came after those agents were being used by employees across the company:"
- **Our assessment**: This is a specific, vendor-authored problem framing worth preserving: it explicitly separates "shipping to production" (claimed as the easy part) from "governing who can access what" (claimed as the hard part) as two distinct problems. The four named follow-up questions — "Who is allowed to use each agent?", "How do we keep internal agents internal?", "Which data and systems are agents allowed to touch?", "Which models are agents using, and how much are they costing us?" — map directly onto the four products that follow (Passport→who's allowed/keep internal, Connect→data/system access, Enterprise Managed Users→lifecycle, and cost is notably NOT addressed by any of the four products described in this post, despite being one of the four framing questions — see Claim 9).

### Claim 2: Vercel Passport puts every internal app and agent deployment behind the organization's identity provider by default, replacing a prior model where "internal" was a per-project setting an employee had to remember to configure
- **Evidence**: Direct product description with an explicit before/after framing of the prior failure mode.
- **Confidence**: settled (first-party description of a named, shipping product feature)
- **Quote**: "Vercel is the fastest way to publish software to the web, but that previously meant \"internal\" was a setting someone had to configure on every project. One employee forgetting to make one deployment private risked exposing access to sensitive company systems and data. Vercel Passport puts every internal app and agent behind your identity provider by default, so you can control access with Okta, Microsoft Entra, Auth0, or any other OpenID Connect-compatible provider."
- **Our assessment**: The "default, not opt-in" framing is the load-bearing claim — Vercel is explicitly naming its own platform's prior default (public-unless-configured-private) as a security anti-pattern it is now correcting. This is a "secure by default" architectural change to the deployment model itself, not an add-on control layered on top of an unchanged default. Named identity providers (Okta, Microsoft Entra, Auth0, "or any other OpenID Connect-compatible provider") mirror the same "standard OIDC federation, not a closed provider list" pattern documented for Anthropic's Workload Identity Federation (`blog-anthropic-workload-identity-federation.md` Claim 2).

### Claim 3: Passport's stated security properties are: private from the moment a deployment exists, access authenticated against employee identity, every access event auditable, and admin-set centralized policy rather than per-builder configuration
- **Evidence**: A single summary sentence in the article enumerating four properties together.
- **Confidence**: settled (first-party enumeration of a shipping feature's properties)
- **Quote**: "App and agent deployments are private from the moment they exist, access is authenticated against your employee identity, every entry is auditable, and admins set the policy centrally rather than relying on each builder to configure it correctly."
- **Our assessment**: This is a compact four-property spec for what "identity-gated by default" means in Vercel's implementation: (1) temporal — private at creation, not after a follow-up configuration step; (2) authentication — against employee identity, not a shared secret; (3) auditability — every access event logged; (4) policy locus — admin-centralized rather than per-builder. Property 4 (centralized admin policy replacing per-builder configuration) is the same governance-locus shift documented for Anthropic's enterprise-managed MCP auth (`blog-anthropic-enterprise-managed-auth.md` Claim 4: "folds MCP access management into the same workflow that governs the rest of your stack: provision once, scope by group, manage revocation through the IdP") — both vendors are independently converging on "move governance from individual builder discipline to centralized IdP-backed admin policy" as the correct enterprise default.

### Claim 4: Vercel Connect replaces long-lived, broadly-provisioned credentials sitting in environment variables with short-lived credentials an agent requests per task, which expire when the task completes
- **Evidence**: Direct problem/solution framing in the main announcement, corroborated and given much greater mechanical detail in the companion "Introducing Vercel Connect" post.
- **Confidence**: settled (first-party description of a named, shipping/beta product mechanism, corroborated at a deeper technical level in a companion post from the same vendor published one day later)
- **Quote**: "Vercel Connect consolidates OAuth, OIDC, and secret injection into one product that replaces those static keys. Instead of storing a secret, an agent requests short-lived credentials as it works. Tokens are granted per task rather than once and forever, and expire when the task is complete."
- **Our assessment**: "Per task rather than once and forever" is the precise framing this corpus has seen from multiple vendors for the same underlying architectural shift (ephemeral, scoped credentials issued at the point of use rather than static keys stored at rest) — see Cross-References for the specific parallel to Anthropic's Workload Identity Federation and Vercel's own prior sandbox-credential-injection pattern. The companion Connect post's Section 9 states the same idea even more sharply: "Nothing is provisioned for everything. Nothing is shared by every user. Nothing lasts forever. Nothing reaches past the task in front of it." (see Concrete Artifacts).

### Claim 5: In the companion Connect post, Vercel argues that a secrets vault does not solve the core problem with long-lived tokens — it only makes the token harder to steal, not less dangerous once it is
- **Evidence**: The companion post's opening framing, presented as the specific gap Connect is built to close (as distinct from existing secrets-management practice).
- **Confidence**: settled (first-party architectural argument, framed as the specific problem statement motivating the product's existence)
- **Quote**: "A vault makes that token harder to steal. It doesn't make it less dangerous. The problem is what happens when the token leaks: everything it can touch is now exposed."
- **Our assessment**: This is a sharp, quotable articulation of blast-radius reasoning that goes a step further than "don't leak credentials" advice: even a well-vaulted, never-leaked static token is still a standing liability by virtue of its broad, permanent scope — the vault reduces leak *probability*, not leak *impact*. This directly corroborates the zero-trust "assume breach, minimize blast radius" framing already in the corpus (`blog-anthropic-agent-identity-access-model.md` Claim 8's "credentials... never attached to individual users" and the underlying zero-trust eBook's short-lived-token principle) but supplies a new, more precise verbal distinction — vault-hardening (probability) vs. scope-minimization (impact) — that the guide could use to explain *why* short-lived scoped tokens are architecturally superior to a well-secured static key, not merely an incremental hardening of the same idea.

### Claim 6: Vercel Connect scopes credentials at the level of an individual request, not just per-connector — a GitHub token request can be restricted to a named repository and specific permissions (e.g. read-only) for that one call, distinct from a standing GitHub App installation which persists as a trusted grant
- **Evidence**: A worked code example and explicit contrast with GitHub App installations in the companion post.
- **Confidence**: settled (first-party code example with explicit architectural contrast to an existing, well-understood access-control mechanism)
- **Quote**: "A fine-grained GitHub App install can be narrow too, but an install is a standing grant, set up once and trusted from then on. This limit exists for one request, one task. Least privilege becomes the shape of the request."
- **Our assessment**: This is the single most concrete architectural distinction in the companion post: least privilege is enforced at request granularity, not connector/installation granularity. The code example (`repositories: ['myorg/repo1']`, `permissions: ['contents:read']`) demonstrates that even a request-time scope restriction narrower than what a standing installation could offer is possible. "Least privilege becomes the shape of the request" is a reusable framing for the guide — it names request-scoped authorization as architecturally distinct from (and stricter than) installation-scoped or connector-scoped authorization, which is the granularity most OAuth-app integrations stop at.

### Claim 7: The Connect post explicitly limits its own security guarantee for token revocation — when a provider doesn't support revocation APIs, Vercel Connect can only stop issuing new tokens, not invalidate ones already issued, which remain valid until they expire
- **Evidence**: An explicit self-imposed caveat in the companion post's revocation section, phrased as a stated limitation rather than a claimed capability.
- **Confidence**: settled (first-party, and notably a limitation the vendor states about its own product rather than a marketed capability — self-disclosed constraints carry more weight than marketed claims)
- **Quote**: "Where the provider supports revocation, Vercel Connect revokes the token at the provider. Where it does not, Vercel Connect stops issuing new tokens for that grant, and a token already issued stays valid at the provider until it expires. That is a real limit on any provider without a revocation API, and the shorter the provider keeps its tokens, the smaller that window is."
- **Our assessment**: This is exactly the kind of load-bearing operational nuance MINER.md flags as high-value (parallel to the "soft cap, not a hard limit" caveat already documented for Vercel's AI Gateway API-key budgets, `blog-vercel-ai-gateway-api-key-budgets.md` Claim 2) — a vendor stating a real gap between the marketed security property ("short-lived, revocable credentials") and the actual guarantee for providers lacking revocation support. For an incident-response scenario (a leaked credential, an offboarded employee), a practitioner relying on Connect must know that "revoke" is not instantaneous everywhere — it is bounded by the underlying provider's token lifetime for non-revocation-capable providers, not by Connect's own action.

### Claim 8: Enterprise Managed Users is built on SAML SSO and Directory Sync, automatically provisioning Vercel/v0 accounts the moment the identity provider grants them and removing access the moment the directory does, with group-based access controls, deployment protection, and MFA enforcement applying org-wide and landing in a single audit trail
- **Evidence**: Direct product description enumerating the mechanism and four org-wide controls.
- **Confidence**: settled (first-party description of a named feature, though explicitly gated as Private Beta — see Claim 9)
- **Quote**: "Enterprise Managed Users gives administrators full lifecycle control over every builder using Vercel. Built on SAML SSO and Directory Sync, it provisions seats automatically through your existing directory, so an account exists the moment your identity provider says it should and off-boarding removes access the moment the directory does. Group-based access controls, deployment protection, and MFA enforcement on Vercel apply org-wide, and every action lands in a single audit trail."
- **Our assessment**: "Off-boarding removes access the moment the directory does" is the specific claim worth flagging for guide purposes on account lifecycle risk: it asserts synchronous (not eventually-consistent or batch-scheduled) deprovisioning tied to the directory event itself. No latency figure is given (contrast with the AI Gateway budget note's specific "up to a minute or two" and "tens of seconds to five minutes" propagation-delay figures, `blog-vercel-ai-gateway-api-key-budgets.md` Claim 7) — this claim should be treated as a directional design intent ("tied to directory state," not "polled periodically") rather than a verified real-time SLA, since no timing detail is disclosed here the way it was for the unrelated API-key-budget feature.

### Claim 9: Bring your own cloud (BYOC) on AWS runs customer compute, build artifacts, and data inside the customer's own AWS account and VPC, with Vercel operating only the control plane on top of it; apps and agents reach private backends the same way anything else in that AWS account does, and source code never leaves the customer's CI
- **Evidence**: Direct architectural description of the BYOC split, framed as answering a boundary question that goes beyond what private deployments (Passport) alone can address.
- **Confidence**: settled (first-party architectural description, though explicitly Private Beta)
- **Quote**: "With bring your own cloud (BYOC) on AWS, your compute, build artifacts, and data run inside your own AWS account and VPC, and Vercel runs the control plane on top of it. Your apps and agents reach private backends and internal systems the same way anything else in your AWS account does, and your source code never leaves your CI."
- **Our assessment**: This is architecturally the same control-plane/data-plane split pattern already documented for Anthropic's Claude Managed Agents self-hosted sandboxes (`blog-anthropic-claude-managed-agents-selfhosted.md` Claim 1: "orchestration stays on Anthropic's infrastructure, while tool execution moves to your own configured environment") — but applied one layer up the stack: this is Vercel's own hosting platform for entire *apps and agents* moving execution into customer-owned AWS, not (as in that note) a sandboxed tool-execution layer plugged into an externally-hosted agent orchestration loop. Notably, that same self-hosted-sandboxes note already documented Vercel offering "VPC peering, and bring your own cloud" as a property of *Vercel Sandbox* specifically (Claim 8 there, dated May 19, 2026) — this June 16, 2026 announcement is a broader, platform-level BYOC offering (the entire app/agent deployment, not just the sandbox tool-execution layer) and should be read as an extension of Vercel's own prior sandbox-level BYOC into a full-platform BYOC, not a duplicate or contradictory claim (see Cross-References).

### Claim 10: v0 (Vercel's AI app builder) now connects to Snowflake, letting any employee build data apps backed by the company's warehouse without an engineering ticket, with access to v0 and Snowflake gated by the organization's IdP so data stays internal and generated apps can deploy directly to the customer's Snowflake account
- **Evidence**: A dedicated subsection describing the v0/Snowflake integration as an example of "democratizing data" under the same governance model as the rest of the announcement.
- **Confidence**: settled (first-party description of a shipping integration)
- **Quote**: "v0 now connects to Snowflake, so you can let anyone safely build data apps backed by your warehouse without an engineering ticket. Access to v0 and Snowflake is controlled through your IDP, so data stays internal. You decide who gets a seat, and apps can deploy directly to your Snowflake account."
- **Our assessment**: This is a concrete, named application of the Passport/Enterprise-Managed-Users governance model (IdP-gated access) to a specific low-code/no-code builder product (v0) and a specific enterprise data system (Snowflake) — the guide-relevant point is not the Snowflake integration itself but that it is explicitly framed as inheriting the same IdP-based access control as the rest of the platform, i.e., v0 is not a governance-exempt side door into enterprise data. No prior corpus source documents a no-code AI app builder connecting directly to a data warehouse under centralized IdP control — this is novel (see Cross-References → Novel).

### Claim 11: Vercel frames "ideas dying in security review" as historically a rational tradeoff (breach risk outweighing innovation gain), and positions this product bundle as making the secure path the default so that path is no longer necessary
- **Evidence**: The article's closing framing paragraph, presented as the overall thesis tying the four products together.
- **Confidence**: anecdotal (vendor's own strategic/marketing framing, not a specific technical or measured claim)
- **Quote**: "Traditionally, ideas died in security review for good reason: the risk of a data breach wasn't worth the potential gain of innovation. Vercel Enterprise Apps and Agents builds safety controls into the platform and tools themselves, meaning everyone in your company can ship apps and agents at the speed of their ideas, without your CISO losing sleep."
- **Our assessment**: This is marketing framing rather than a falsifiable technical claim, appropriately rated anecdotal. It is nonetheless useful context for guide purposes as the vendor's own stated intent for the bundle: replace security review as a bottleneck gate with security controls as a structural default. The three-item "what building looks like" list that follows (secure prototyping at scale via v0, domain experts building their own tools, "an immediate graduation path to production" — "When a prototype proves it matters, engineering takes it into production on the same platform it was prototyped on, rather than rebuilding it from scratch or banning it outright") names a specific failure mode this framing is positioned against: prototypes either get banned outright or require a full rebuild before production — both treated as undesirable outcomes the bundle is meant to avoid.

## Concrete Artifacts

### Platform components table (verbatim, from the main article)

```
| Platform components        | Security implementation |
|-----------------------------|--------------------------|
| Vercel Passport              | Puts every internal app and agent behind your identity provider by default |
| Vercel Connect                | Gives agents short-lived, scoped credentials for the systems they use, like Slack, GitHub, Snowflake, Salesforce, and Linear |
| Enterprise Managed Users      | Full lifecycle control over every Vercel and v0 user through your existing directory |
| Bring your own cloud on AWS   | Runs apps and agents inside your own AWS account (currently in Private Beta) |

Source: https://vercel.com/blog/vercel-for-enterprise-apps-and-agents
```

### FAQ (verbatim, from the main article)

```
Q: What is Vercel for Enterprise Apps and Agents?
A: "It is the platform for deploying, governing, and connecting the apps and
   agents your employees build, across the whole organization. It brings
   ownership, access control, identity, and security to everything your
   company ships, whether someone prototyped it in v0 or an engineering team
   built it from the ground up. The platform includes Vercel Passport,
   Vercel Connect, Enterprise Managed Users, and the option to run inside
   your own AWS account."

Q: Do I need to use a particular framework to use Passport, Connect, and
   Enterprise Managed Users?
A: "No. Passport, Connect, and Enterprise Managed Users govern anything you
   deploy to Vercel, regardless of how it was built. They apply to your
   existing projects the same way they apply to new ones."

Q: Which identity providers and external services are supported?
A: "Enterprise Managed Users works with Okta and any SAML or OIDC identity
   provider. Vercel Connect gives agents secure access to Slack, GitHub,
   Snowflake, Salesforce, and Linear, plus anything else reachable over
   OAuth or an API."

Q: What is available today?
A: "Vercel Passport and Vercel Connect are in Beta. Enterprise Managed Users
   and BYOC on AWS are in Private Beta."

Source: https://vercel.com/blog/vercel-for-enterprise-apps-and-agents
```

### Availability tiers (verbatim, cross-checked between main article and companion post)

```
Vercel Passport:          Beta
Vercel Connect:           Public Beta (per companion post: "Now in Public
                          Beta, Vercel Connect replaces the stored token
                          with runtime credential exchange.")
Enterprise Managed Users: Private Beta
Bring your own cloud on AWS (platform-level): Private Beta

Source: https://vercel.com/blog/vercel-for-enterprise-apps-and-agents and
        https://vercel.com/blog/introducing-vercel-connect
```

### Vercel Connect — request-scoped GitHub token code example (verbatim, from companion post `/blog/introducing-vercel-connect`)

```typescript
// app/lib/github-token.ts
import { getToken } from '@vercel/connect';
const token = await getToken('github/mybot', {
  subject: { type: 'app' },
  authorizationDetails: [
    {
      type: 'github_app_installation',
      repositories: ['myorg/repo1'], // one repo, not the whole org
      permissions: ['contents:read'], // read-only, not write
    },
  ],
});
```

### Vercel Connect — user-delegated token code example (verbatim, from companion post)

```typescript
// app/lib/user-token.ts
import { getToken } from '@vercel/connect';
const token = await getToken('linear/mybot', {
  subject: { type: 'user', id: 'user_123' },
});
```

### Vercel Connect — revocation CLI (verbatim, from companion post)

```bash
# Revoke just your own tokens for a connector
vercel connect revoke-tokens slack/mybot --my-tokens
# Or revoke every token, across all users and installations
vercel connect revoke-tokens slack/mybot --all-tokens
```

### Vercel Connect — connector creation CLI (verbatim, from companion post)

```bash
vercel connect create slack --name mybot
```

### Vercel Connect — supported connectors and pricing (verbatim, companion post FAQ)

```
Q: Which connectors are available?
A: "Vercel Connect supports generic OAuth and API key connectors, plus
   dedicated connectors for Slack, GitHub, Linear, Discord, Notion,
   Salesforce, Figma, and Snowflake. Resend, Workday, Microsoft Teams, and
   more are coming soon."

Q: How does pricing work?
A: "Pricing is based on token requests. The Hobby plan includes 5K token
   requests per month at no additional cost. On Pro and Enterprise plans,
   token requests are billed at $3 per 10K token requests."

Q: What are the current Beta limitations?
A: "Trigger forwarding is limited to Slack, GitHub, and Linear, connector
   branding fields cannot be fully cleared after you set them, and token
   revocation, token lifetime, and scope granularity depend on provider
   support."

Source: https://vercel.com/blog/introducing-vercel-connect
```

### Vercel Connect — event-driven trigger flow (verbatim, companion post Section 7)

```
"The flow runs end to end without a provider secret in your app:
- A user posts a message in Slack.
- Slack sends the event to Vercel Connect.
- Vercel Connect verifies the event against the Slack signing secret it
  holds, then forwards it to your Vercel app, re-attested with its OIDC
  identity.
- Your app verifies that attestation, then requests a scoped runtime token.
- The agent acts and responds."

Source: https://vercel.com/blog/introducing-vercel-connect, Section 7
("Drive Event-Driven Agents from Verified Slack Triggers")
```

## Cross-References

### Cross-reference verification notes
`blog-vercel-ai-gateway-api-key-budgets.md`, `blog-vercel-ai-gateway-production-index-may2026.md`,
`blog-anthropic-enterprise-managed-auth.md`, `blog-anthropic-agent-identity-access-model.md`,
`blog-anthropic-workload-identity-federation.md`, and
`blog-anthropic-claude-managed-agents-selfhosted.md` were re-read in full during
this extraction (MINER.md §4b), and every claim number cited below was located
and confirmed against that note's own numbered `### Claim N:` headings in
document order before writing this section.

- **Corroborates**:
  - `blog-anthropic-workload-identity-federation.md` Claim 3 ("WIF replaces
    static API keys with short-lived, scoped credentials issued at request
    time") and Claim 4 ("eliminates the need to create, rotate, or leak
    static... credentials"): Vercel Connect's core mechanism (Claim 4/5
    here) is the identical architectural pattern — ephemeral, scoped,
    request-time credential issuance replacing static keys — applied to a
    different authentication boundary (Vercel app → external SaaS/data
    system, versus WIF's workload → Claude Platform). Two independent
    vendors converging on "credentials issued per request, not stored at
    rest" as the enterprise-grade default is a strong corroboration this is
    now an industry-standard pattern, not a single-vendor design choice.
  - `blog-anthropic-agent-identity-access-model.md` Claim 8 ("credential is
    stored independently and mapped to that channel's identity, then
    injected at the network boundary at request time... never attached to
    individual users"): the architectural principle is the same as this
    source's request-scoped credential model (Claim 6), though the
    Anthropic source scopes credentials to a persistent channel/agent
    identity while Vercel Connect scopes them per individual request/task —
    Vercel's granularity is finer (task-level vs. channel-level).
  - `blog-anthropic-claude-managed-agents-selfhosted.md` Claim 1
    (self-hosted sandboxes split orchestration, kept on Anthropic
    infrastructure, from tool execution, moved to customer infrastructure)
    and Claim 8 (Vercel Sandbox specifically: "firewall injects credentials
    at the network boundary so they never enter the sandbox," plus "VPC
    peering, and bring your own cloud"): this source's BYOC-on-AWS claim
    (Claim 9 here) is the same control-plane/data-plane split pattern,
    applied one layer up — the entire app/agent deployment rather than just
    a sandboxed tool-execution environment. That prior note already
    documented Vercel offering sandbox-level BYOC; this source extends the
    same architectural philosophy to full-platform BYOC.
  - `blog-anthropic-enterprise-managed-auth.md` Claim 4 ("folds MCP access
    management into the same workflow that governs the rest of your stack:
    provision once, scope by group, manage revocation through the IdP"):
    Vercel Passport's "admins set the policy centrally rather than relying
    on each builder to configure it correctly" (Claim 3 here) is the same
    governance-locus argument — move access control decisions from
    individual builders/users to centralized, IdP-backed admin policy — for
    a different product surface (whole-app private-by-default deployment
    vs. MCP connector provisioning).

- **Contradicts**: None identified as a MINER.md §4a contradiction. One
  potential tension was evaluated and ruled out: this source's BYOC-on-AWS
  claim (Claim 9, platform-level, Private Beta, announced June 16, 2026)
  could be read as overlapping with or superseding the sandbox-level "bring
  your own cloud" already documented in
  `blog-anthropic-claude-managed-agents-selfhosted.md` Claim 8 (Vercel
  Sandbox, May 19, 2026). These are not contradictory — they describe BYOC
  at two different architectural layers (a tool-execution sandbox product
  vs. an entire application/agent hosting platform) and neither source
  claims the other layer's scope. No contradiction issue filed.

- **Extends**:
  - `blog-vercel-ai-gateway-api-key-budgets.md`: that note documents
    Vercel's cost-governance controls for AI Gateway API keys (dollar
    budgets, soft-cap enforcement). This source covers a different
    governance dimension for a different Vercel product line entirely
    (identity/access governance for the app-hosting and agent-deployment
    platform, not cost governance for the AI Gateway). Notably, this
    source's own Claim 1 names "which models are agents using, and how much
    are they costing us" as one of the four original motivating questions,
    but none of the four products described in this article (Passport,
    Connect, Enterprise Managed Users, BYOC) address cost — that gap is
    filled by the separate AI Gateway budget feature in the other note, not
    by anything in this source (see Guide Impact).
  - `blog-anthropic-workload-identity-federation.md` and
    `blog-anthropic-agent-identity-access-model.md`: both document
    Anthropic's identity/credential architecture at, respectively, the
    Claude-Platform-API layer and the Claude-Tag-in-team-channels layer.
    This source extends the same "identity-first, ephemeral-credential"
    architectural philosophy to a third, independent vendor's app-hosting
    platform (Vercel), and to a specific technical mechanism (request-level,
    not just channel-level, credential scoping via `authorizationDetails`)
    not previously documented in the corpus at this granularity.
  - `blog-anthropic-claude-managed-agents-selfhosted.md`: extends Vercel's
    own prior sandbox-level BYOC/credential-injection offering (documented
    there as one of four sandbox-provider integrations for Claude Managed
    Agents) into a full-platform enterprise BYOC product for Vercel's own
    hosting service, independent of any Anthropic integration.

- **Novel**:
  - **Request-scoped (not just connector- or installation-scoped) external
    credentials** (Claim 6): the corpus's first documented case of an
    OAuth/token credential scoped down to a single API call's specific
    resource and permission list (one repository, read-only) rather than a
    standing per-connector or per-installation grant. "Least privilege
    becomes the shape of the request" is a new framing for this level of
    granularity.
  - **Explicit self-disclosed revocation-completeness caveat depending on
    provider support** (Claim 7): no prior corpus source documents a vendor
    stating that its own "revoke access" feature has an unavoidable window
    of continued validity for providers lacking a revocation API. This is a
    new, concrete operational caveat for incident-response planning.
  - **"Vault hardens against theft, not against impact of a leak" framing**
    (Claim 5): a new, quotable articulation of blast-radius reasoning
    distinguishing leak-probability mitigation (vaulting) from
    leak-impact mitigation (scope minimization) — not phrased this way in
    any existing corpus source.
  - **No-code AI app builder (v0) connecting directly to an enterprise data
    warehouse (Snowflake) under centralized IdP governance** (Claim 10): no
    prior corpus source documents a low-code/no-code AI builder product with
    direct, IdP-gated warehouse access and direct-to-customer-account
    deployment.
  - **Full-platform bring-your-own-cloud on AWS** (Claim 9): distinct from
    the previously-documented sandbox-level BYOC (Vercel Sandbox, per
    `blog-anthropic-claude-managed-agents-selfhosted.md` Claim 8), this is
    the first corpus documentation of an entire app/agent hosting platform
    (not just a tool-execution sandbox) offering customer-account,
    customer-VPC compute with the vendor retaining only the control plane.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Vercel Connect's request-scoped
  credential model (Claim 6, code example in Concrete Artifacts) as a
  concrete implementation pattern for the "credentials should be scoped to
  the smallest unit of work, not the broadest standing grant" principle —
  currently the guide's credential-scoping material draws mainly from
  Anthropic sources (WIF, agent identity, self-hosted sandboxes); this adds
  a third, independent vendor's implementation at finer (per-request, not
  per-channel or per-workload) granularity, with a runnable code example
  (`authorizationDetails` restricting a GitHub token to one repository,
  read-only, for a single call).

- **Chapter 02 (Harness Engineering)**: Add the vault-vs-scope distinction
  from Claim 5 ("A vault makes that token harder to steal. It doesn't make
  it less dangerous.") as a explanatory device for why ephemeral scoped
  credentials are architecturally superior to well-secured static ones —
  useful for explaining to teams who already have a secrets-vault practice
  why that alone does not close the blast-radius gap.

- **Chapter 05 (Team Adoption)**: Add Vercel Passport's "private by default,
  not by builder configuration" model (Claims 2-3) as a concrete example of
  the "move governance from individual discipline to centralized IdP-backed
  default" pattern already emerging across vendors (corroborates
  `blog-anthropic-enterprise-managed-auth.md` Claim 4). Frame the specific
  failure mode it corrects — "one employee forgetting to make one
  deployment private" — as a named, guide-relevant risk of any platform
  whose default state is public/shared rather than private/gated.

- **Chapter 06 (Security Threat Model)**: Add Claim 7's revocation caveat
  (token revocation is provider-dependent; for providers without a
  revocation API, a leaked or compromised token remains valid until its
  natural expiry even after "revocation") as a concrete incident-response
  planning detail — parallel to the "soft cap, not hard limit" caveat
  already flagged for AI Gateway budgets. When evaluating any credential-
  broker product for its blast-radius/incident-response properties,
  practitioners should ask specifically what "revoke" guarantees for each
  connected provider, not assume uniform instant invalidation.

- **Chapter 06 (Security Threat Model)**: Add the BYOC-on-AWS control-plane
  /data-plane split (Claim 9) as a third documented instance (alongside
  Anthropic's self-hosted sandboxes and Claude Managed Agents' hybrid model)
  of the "vendor keeps orchestration, customer keeps execution/data" pattern
  for organizations with data-residency or account-ownership requirements —
  now documented as available at the whole-application-platform layer, not
  only at the tool-execution-sandbox layer.

- **Chapter 04 (Cost Engineering at Scale)** — gap flag, not a positive
  claim: note that this announcement's own stated motivating questions
  (Claim 1) include "which models are agents using, and how much are they
  costing us," but none of the four products this bundle actually ships
  (Passport, Connect, Enterprise Managed Users, BYOC) address cost
  governance — that remains a separate Vercel product line (AI Gateway
  budgets, `blog-vercel-ai-gateway-api-key-budgets.md`). Guide text should
  not imply this enterprise bundle is a complete answer to the four
  framing questions it opens with; cost is conspicuously unaddressed here.

## Extraction Notes

1. **Verified against raw HTML, not WebFetch summarization alone.** Per
   MINER.md §2a's caution about WebFetch paraphrasing, this note's WebFetch
   output was cross-checked by fetching both pages' raw HTML directly via
   `curl` (the site is a Next.js app; article text is present in escaped
   form inside the page's embedded RSC/JSON payload) and searching for each
   quoted phrase verbatim. Every `Quote` field in this note — including
   the platform-components table, the Passport/Connect/EMU/BYOC section
   bodies, the FAQ, and every quote pulled from the companion Connect
   post — was located character-for-character in the raw HTML before being
   used here. No quote in this note comes from an unverified WebFetch pass.
2. **One companion page followed, per MINER.md §1.** The main article gives
   Vercel Connect only a two-paragraph summary and inline-links
   `/blog/introducing-vercel-connect` (published the following day, June 17,
   2026) for the full mechanism. That page was fetched and extracted in
   full, since it is the authoritative, substantially more detailed source
   for how Connect's credential exchange actually works (Claims 4-7,
   several Concrete Artifacts). Two other inline links
   (`/blog/agent-stack`, `/blog/introducing-eve`) were identified but not
   followed — they are referenced only in the article's opening sentence
   as context for Vercel's own internal agent-building tools and are outside
   this issue's triage scope (enterprise access/deployment governance, not
   the agent framework itself).
3. **No named customer evidence in either post.** Unlike several adjacent
   corpus sources (`blog-anthropic-claude-managed-agents-selfhosted.md`,
   `blog-anthropic-enterprise-managed-auth.md`), neither the main
   announcement nor the companion Connect post names a single customer using
   any of these four products. All claims here are vendor self-description
   of shipping or beta features, not independently validated deployment
   outcomes — this is reflected in the overall "emerging" confidence rating
   despite most individual claims being rated "settled" (first-party,
   unambiguous descriptions of what a shipping/beta feature does).
4. **No contradiction issues filed.** One near-tension (platform-level BYOC
   here vs. sandbox-level BYOC already documented for Vercel Sandbox in
   `blog-anthropic-claude-managed-agents-selfhosted.md`) was evaluated
   against MINER.md §4a and judged to be two different architectural layers
   of the same vendor's BYOC offering, not a factual disagreement — see
   Cross-References → Contradicts.
5. **Confidence calibration: emerging.** Individual claims are largely rated
   "settled" (first-party, unambiguous descriptions of named, shipping or
   beta product mechanics, several independently verified against raw HTML
   and cross-checked against a same-vendor companion post published one day
   apart). The note's overall confidence is "emerging" rather than "settled"
   because: (a) three of the four headline products (Connect, Enterprise
   Managed Users, BYOC) are explicitly Beta or Private Beta with no GA date
   given; (b) no named customer or independent security review validates any
   of the four products in production; and (c) the framing claims (Claim 1,
   Claim 11) are vendor marketing narrative rather than independently
   verifiable technical fact.
