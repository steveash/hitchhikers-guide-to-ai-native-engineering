---
source_url: https://claude.com/blog/agent-identity-access-model
source_type: blog-post
title: "Agent identity in Claude Tag: a new access model for autonomous, team-wide AI"
author: Anthropic (no individual byline)
date_published: 2026-06-24
date_extracted: 2026-06-24
last_checked: 2026-06-24
status: current
confidence_overall: emerging
issue: "#1291"
---

# Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

> Official Anthropic announcement introducing "agent identity" — an access model for Claude
> Tag (Claude in team workspaces) where Claude operates under its own service accounts rather
> than individual user credentials, with a two-level workspace/channel identity hierarchy,
> credential isolation injected at the network boundary, per-channel compartmentalization,
> dual audit trails, and a planned roadmap for JIT credential grants and identity-aware overlays.

## Source Context

- **Type**: blog-post (official claude.com/blog, June 24, 2026; first-party product
  announcement of a shipping feature in the Claude Tag / Claude Cowork product; no individual
  byline — published as Anthropic)
- **Author credibility**: First-party Anthropic product announcement on the same channel as
  "Zero Trust for AI Agents," "Workload Identity Federation," and "Centrally manage
  authorization for MCP connectors." This is the authoritative Anthropic description of the
  agent identity access model at ship time. Architectural claims about how credentials are
  stored and injected are vendor-authoritative for the Claude Tag product. The roadmap items
  (JIT grants, identity-aware overlay) are described as planned future enhancements — treat as
  forward-looking vendor intent, not shipped behavior.
- **Scope**: Covers the agent identity access model specifically for Claude Tag (Claude in team
  channels): (1) why per-user ACLs fail for team AI (two concrete reasons), (2) how agent
  identity works (service accounts per connected system), (3) the two-level identity hierarchy
  (workspace baseline + per-channel override), (4) admin-configurable components (repos,
  connectors, skills, standing instructions), (5) credential isolation mechanism, (6)
  channel-level compartmentalization (private vs. public channel identity scoping), (7) dual
  audit trail, (8) recommended best practice for incremental access grants, and (9) the
  identity revocation model. Does NOT cover: pricing, MCP connector details, Claude Code
  integration, API-level authentication (see `blog-anthropic-workload-identity-federation.md`
  for that), or the specific identity provider integration mechanism.

## Extracted Claims

### Claim 1: Two structural reasons make per-user ACLs unworkable for team AI — increasing agent autonomy and multiplayer team environments
- **Evidence**: First-party Anthropic framing of the access model problem. Both reasons are
  structural properties of how modern agentic AI operates in teams, not edge cases.
- **Confidence**: settled (sound logical derivation from agent properties; first-party framing
  from the vendor with the most deployment data)
- **Quote**: "This model doesn't work for Claude Tag for two reasons: Increasing agent
  autonomy...Multiplayer teams."
- **Our assessment**: The article opens with "For an AI agent to do its best work on a
  human-agent team, it needs access to the same tools, documents, and context humans have."
  The two-reason framework then explains why the obvious answer (grant the user's permissions)
  is inadequate. This framing is important for guide purposes: it establishes that the problem
  is not a configuration limitation but a structural mismatch between how per-user ACLs work
  and how team agents operate. Any team deploying a persistent autonomous agent will encounter
  both of these reasons, not just one.

### Claim 2: Agent task duration has been doubling roughly every four months, making session-scoped user permissions structurally inadequate
- **Evidence**: Specific quantitative claim from the article about agent capability growth.
- **Confidence**: emerging (first-party Anthropic framing; the doubling rate is presented as
  an observed trend, not cited from an independent study; directionally consistent with
  published benchmarks on agentic task completion)
- **Quote**: "The length of a task that an AI agent can reliably complete on its own has been
  doubling roughly every four months."
- **Our assessment**: This is the sharpest quantification in the corpus of agent capability
  trajectory. Prior notes document the shift from session-bound to long-running agents
  (blog-anthropic-harness-long-running.md), but none provide this specific rate of change.
  The "doubling every four months" claim implies that agents now reliably complete tasks that
  extend far beyond a single user session — and will complete tasks far longer within months.
  Agents "schedule their own tasks for later and respond to events long after the person who
  asked has logged off" — this means the user whose session the agent is acting under may not
  even be online when the access decision matters. For guide purposes: this metric
  quantifies why session-scoped user permissions are architecturally incompatible with
  autonomous agents, not just inconvenient.

### Claim 3: In shared channel environments, the multiplayer problem eliminates the correct choice of "whose permissions apply"
- **Evidence**: Concrete scenario described in the article.
- **Confidence**: settled (logical derivation; the problem is structural for any multi-user
  channel environment)
- **Quote**: "Claude Tag places Claude in shared spaces where teams are already working—e.g.,
  a channel where three engineers and a PM are debugging together. But when more than one
  person is steering, whose permissions apply?"
- **Our assessment**: The multiplayer problem is distinct from the autonomy problem (Claim 2).
  It is not about duration; it is about authority. Even a brief, synchronous agent interaction
  in a shared channel has no correct answer to "whose user permissions should Claude inherit?"
  — any choice is either over-privileged (using the most permissive team member's credentials)
  or under-privileged (using the least permissive). Agent identity dissolves this problem by
  replacing the "which user?" question with a defined workspace identity.

### Claim 4: Agent identity replaces the per-user access question with a per-compartment agent access model
- **Evidence**: Direct statement of the access model reframe in the article.
- **Confidence**: settled (first-party Anthropic architectural framing; clear and internally
  consistent)
- **Quote**: "Agent identity replaces the question 'what can this user do?' with 'what can
  this agent do in this compartment?'"
- **Our assessment**: This is the most architecturally significant formulation in the article.
  The shift from user-centric to agent-centric access control is not merely a technical change
  — it is a reconceptualization of the access model for agentic systems. "In this compartment"
  is equally important: access is not granted to the agent globally, but to an agent operating
  within a defined scope (a workspace, a channel). For guide purposes: this reframe should
  anchor any discussion of access control architecture for team AI. Practitioners who carry
  user-centric mental models into agentic system design will build architectures that don't
  compose at scale.

### Claim 5: Claude Tag agent identity means Claude operates under its own service accounts per connected system, not on behalf of individual users
- **Evidence**: Concrete example enumeration in the article, with specific named systems.
- **Confidence**: settled (first-party product description of shipping behavior)
- **Quote**: "In a channel where Claude Tag is active, Claude isn't acting on behalf of a
  single user. It has its own account in each system it touches."
- **Quote** (examples): "it posts in Slack as the Claude app, opens pull requests as the
  Claude GitHub App, and queries your warehouse under a service account"
- **Our assessment**: The three concrete examples (Slack, GitHub, data warehouse) establish
  what "its own account" means in practice: distinct first-class identities in each connected
  system, not credentials borrowed or proxied from a user. This has direct implications for
  how connected systems log and audit Claude's actions — the agent shows up as "Claude app"
  or "Claude GitHub App," not as any individual employee. This is also the architecture that
  makes the dual audit trail (Claim 10) possible: because Claude has its own identity, its
  actions appear in connected systems' native logs under a distinguishable identity, not mixed
  with human user activity.

### Claim 6: A two-level identity hierarchy governs access — workspace-level baseline inherited by all channels, overridable per channel
- **Evidence**: Direct description of the identity configuration architecture.
- **Confidence**: settled (first-party product description of shipping configuration model)
- **Quote**: "admins define an identity—the baseline set of connections and skills Claude holds
  everywhere—at the workspace level, and every channel inherits it by default. Then, where it
  makes sense, they can override it at the channel level"
- **Our assessment**: The two-level hierarchy (workspace → channel) is the architectural
  pattern that makes the access model manageable at scale. A workspace admin can establish
  consistent baseline access across all channels without per-channel configuration, then
  selectively expand (or restrict) access for specific channels that have different
  requirements. This is the correct enterprise governance pattern: set the least-privilege
  default at the highest scope, then grant deliberate exceptions at narrower scope. For guide
  purposes: this hierarchy maps well to how organizations already structure role-based access
  — org-wide defaults, then department/team overrides.

### Claim 7: Admins configure four components of a channel's identity — repository access, connectors, skills/plugins, and standing instructions
- **Evidence**: Enumeration of admin-configurable components in the article with sub-headings.
- **Confidence**: settled (first-party product description of the admin configuration surface)
- **Quote**: "Repository access: which repos Claude can read and write to. Connectors: the
  tools and API keys that Claude uses to do its job... Skills and plugins: folders of
  instructions, scripts, and resources Claude loads dynamically... Standing instructions:
  custom instructions and context for each channel."
- **Our assessment**: The four-component taxonomy defines exactly what "agent identity" means
  in practice at the configuration level — it is not just credentials, but the full scope of
  Claude's capabilities and behavioral context within a compartment. "API keys" are listed
  within "Connectors" — they are part of the identity profile, not floating credentials
  attached to individual users. For harness engineers: the four-component taxonomy (repo
  access, connectors, skills, instructions) is the complete spec for what must be defined
  when establishing an agent identity. Any team-deployed agent should have these four
  components explicitly configured, not left at defaults.

### Claim 8: Credentials are stored independently, mapped to channel identity, and injected at the network boundary at request time — never attached to individual users
- **Evidence**: Direct architectural description of the credential storage and injection mechanism.
- **Confidence**: emerging (first-party architectural claim; the "injected at the network
  boundary" mechanism is described but not independently verifiable from outside the product)
- **Quote**: "When an admin adds a connection to a channel's profile, the credential is stored
  independently and mapped to that channel's identity, then injected at the network boundary
  at request time."
- **Our assessment**: "Stored independently and mapped to that channel's identity" is the key
  security property: credentials are not attached to user accounts or session tokens. "Injected
  at the network boundary at request time" means credentials are never exposed to the model or
  stored in the conversation context — they are applied at the infrastructure layer when the
  actual network call is made. This is architecturally equivalent to the "inject at runtime
  from secrets management" pattern prescribed in blog-anthropic-zero-trust-ai-agents.md
  (Phase 6: Protect Agent Credentials). For practitioners: this is the correct credential
  architecture for any agent with access to external services — credentials live outside the
  agent's context window and are applied at the call site, not passed through the model.

### Claim 9: Private channels receive distinct identities; public channels share workspace-level identity — memory and access enforcement respects these compartment boundaries
- **Evidence**: Direct statement of the identity scoping rules and their memory implications.
- **Confidence**: settled (first-party product description of shipping behavior)
- **Quote**: "Claude Tag creates a distinct identity for each private channel; public channels
  in a workspace share a workspace-level identity."
- **Quote** (boundary enforcement): "Memory and access respect those boundaries: what Claude
  learns in a private channel never appears in the wider workspace."
- **Our assessment**: The private/public channel distinction creates a natural compartmentalization
  aligned with the existing access model most team tools already provide (private channels have
  restricted membership; public channels are workspace-wide). Claude's identity model mirrors
  this: a private channel where a sensitive deal or personnel matter is discussed gets an
  isolated identity, so context from that discussion never bleeds into public channels. "What
  Claude learns in a private channel never appears in the wider workspace" is the memory
  boundary equivalent of the access boundary — both are scoped to the identity compartment.
  For guide purposes: this is the first corpus source to document that agent memory boundaries
  can be enforced through identity compartmentalization at the product level.

### Claim 10: Agent actions are logged through a dual audit trail — Claude's own audit log plus each connected system's native logs
- **Evidence**: Direct description of the audit architecture.
- **Confidence**: emerging (first-party product claim; "every routine, memory write, and
  network call" scope is an architectural assertion that would require independent verification
  to confirm completeness)
- **Quote**: "every routine, memory write, and network call made with agent credentials is
  recorded, and because Claude acts under its own service accounts, those actions also land in
  each connected system's own logs."
- **Our assessment**: The dual audit trail is architecturally significant because it creates
  two independent records of agent action: (1) Claude's audit trail, which is comprehensive
  across all actions regardless of which external system they touched, and (2) each connected
  system's own logs, which show the Claude agent's actions alongside human activity in that
  system's native format. This dual record enables both Claude-centric investigation ("what
  did the agent do overall?") and system-centric investigation ("what actions happened in our
  GitHub repo, and which were from the Claude agent?"). For guide purposes: this is the most
  complete audit trail architecture described in any corpus source for team agent deployments.
  The zero-trust note documents audit trail requirements in general (Phase 7, Phase 8); this
  source shows a concrete product implementation.

### Claim 11: The recommended security practice is a minimal-footprint start — baseline profile, then deliberate incremental grants informed by audit trail review
- **Evidence**: Direct prescriptive guidance from the article.
- **Confidence**: settled (first-party Anthropic security recommendation for the product they
  built; consistent with zero-trust principles of least privilege)
- **Quote**: "start with a baseline profile in a few channels, read the audit trail, and then
  extend access where the work justifies it, one deliberate grant at a time"
- **Our assessment**: This is the operational guidance pattern for Claude Tag deployments. It
  implements the zero-trust "start minimal, expand deliberately" principle in a product-specific
  way: (1) begin with the baseline workspace identity (not a custom identity with broad access),
  (2) deploy in a limited number of channels (not org-wide immediately), (3) read the audit
  trail to understand what access Claude actually uses, (4) extend access only where justified
  by observed need. "One deliberate grant at a time" explicitly rejects the common practice
  of granting broad access upfront and restricting later. For Ch05 (Team Adoption): this is
  the correct phased rollout pattern for team agent deployments, and it mirrors the access
  expansion approach already recommended for enterprise software generally.

### Claim 12: Revoking an agent identity ends access comprehensively — all systems where that identity was used, in a single operation
- **Evidence**: Stated as an administrative property of the identity model.
- **Confidence**: settled (first-party product claim; this is a direct architectural consequence
  of credential isolation per Claim 8)
- **Quote**: Revoking an identity "ends Claude's access everywhere that the identity was used"
- **Our assessment**: This is the "single revocation sweeps all access" property of service
  account identity, as distinct from per-credential revocation. In a user-credential model,
  revoking a user's Claude access doesn't necessarily revoke the API key the user configured
  for GitHub, the database connector they set up, or the Slack connection they created —
  each might need to be revoked separately. In the agent identity model, revoking the channel
  identity ends all access granted to that identity across all connected systems
  simultaneously. For guide purposes: this is the key operational advantage of agent identity
  over user-credential delegation at scale — offboarding an agent (or a channel) is a single
  administrative action, not an audit across every connected system.

### Claim 13: The roadmap includes JIT credential grants and identity-aware overlays — neither is shipped yet
- **Evidence**: Future enhancement described in the article.
- **Confidence**: emerging (forward-looking vendor intent; described as planned, not shipped)
- **Quote**: "just-in-time credential grants—so that a user can approve a single sensitive
  action in the moment without permanently widening the agent's scope—and an identity-aware
  overlay for organizations with more complex clearance structures."
- **Our assessment**: JIT credential grants are the most practically important roadmap item:
  they would allow a user to authorize a one-time sensitive action (e.g., deploying to
  production, accessing a confidential file) without permanently adding that capability to the
  agent's identity profile. This enables "approve the specific action, not the standing
  capability" — a more granular control than the current model's deliberate-grant approach.
  The identity-aware overlay for "more complex clearance structures" suggests a future
  capability to map organizational hierarchy or clearance levels to agent access scoping —
  relevant for organizations with formal information classification systems (government
  contractors, regulated industries). For guide purposes: note these as planned enhancements
  that will materially improve the security model when shipped; current deployments should
  rely on the deliberate incremental grant practice (Claim 11) in the interim.

## Concrete Artifacts

### Agent Identity Architecture Overview

```
# Claude Tag Agent Identity Model
# Source: "Agent identity in Claude Tag: a new access model for autonomous, team-wide AI"
# Anthropic, June 24, 2026

PROBLEM: Per-user ACLs fail for two reasons:
  1. Autonomy duration: "The length of a task that an AI agent can reliably complete on its
     own has been doubling roughly every four months" — agents operate after users log off
  2. Multiplayer: In shared channels, "when more than one person is steering, whose
     permissions apply?" — no correct choice exists

SOLUTION: Agent identity
  "Claude isn't acting on behalf of a single user. It has its own account in each
  system it touches."
  Examples:
    - Posts in Slack as the Claude app
    - Opens pull requests as the Claude GitHub App
    - Queries data warehouses under a service account

REFRAME:
  Old: "What can this user do?"
  New: "What can this agent do in this compartment?"
```

### Identity Hierarchy and Configuration

```
# Identity hierarchy: workspace → channel
# Source: "Agent identity in Claude Tag," Anthropic, June 24, 2026

LEVEL 1: Workspace identity (baseline)
  "admins define an identity—the baseline set of connections and skills Claude holds
   everywhere—at the workspace level, and every channel inherits it by default"

LEVEL 2: Channel overrides (where justified)
  "where it makes sense, they can override it at the channel level"

CHANNEL IDENTITY SCOPING:
  Private channels → distinct identity per channel
  Public channels  → shared workspace-level identity
  Boundary rule:   "Memory and access respect those boundaries: what Claude learns in a
                    private channel never appears in the wider workspace."

ADMIN-CONFIGURABLE COMPONENTS:
  Repository access:    "which repos Claude can read and write to"
  Connectors:           "the tools and API keys that Claude uses to do its job"
  Skills and plugins:   "folders of instructions, scripts, and resources Claude loads
                          dynamically"
  Standing instructions: "custom instructions and context for each channel"
```

### Credential Isolation and Audit Architecture

```
# Credential + audit architecture
# Source: "Agent identity in Claude Tag," Anthropic, June 24, 2026

CREDENTIAL ISOLATION:
  "When an admin adds a connection to a channel's profile, the credential is stored
   independently and mapped to that channel's identity, then injected at the network
   boundary at request time."

DUAL AUDIT TRAIL:
  "every routine, memory write, and network call made with agent credentials is recorded,
   and because Claude acts under its own service accounts, those actions also land in each
   connected system's own logs."

REVOCATION:
  Revoking the identity "ends Claude's access everywhere that the identity was used"

BEST PRACTICE (from article):
  "start with a baseline profile in a few channels, read the audit trail, and then extend
   access where the work justifies it, one deliberate grant at a time"
```

### Roadmap Items (Not Yet Shipped)

```
# Planned enhancements
# Source: "Agent identity in Claude Tag," Anthropic, June 24, 2026

JIT CREDENTIAL GRANTS:
  "just-in-time credential grants—so that a user can approve a single sensitive action in
   the moment without permanently widening the agent's scope"

IDENTITY-AWARE OVERLAY:
  "an identity-aware overlay for organizations with more complex clearance structures"
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 12: "Short-lived, narrowly-scoped tokens
    issued by an identity provider are the new baseline." Claude Tag's credential isolation
    (Claim 8 here: "stored independently...injected at the network boundary at request time")
    is the product-level implementation of this principle within the Cowork product. Both
    sources converge on the same architectural design: credentials are never stored in or
    passed through the agent's reasoning context, but applied at the infrastructure boundary.
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 19: "Identity-based isolation is the
    primary control for resource boundaries." Claude Tag's per-channel identity (Claim 9 here)
    is a production implementation of identity-based isolation at the team-collaboration product
    layer: private channels are isolated compartments, and the identity boundary (not network
    segmentation) enforces separation.
  - `blog-anthropic-workload-identity-federation.md` Claim 5: "WIF introduces service accounts
    to the Claude Platform, enabling individual identities and audit trails per workload." Both
    sources describe the same architectural shift from API keys to service accounts — WIF at
    the Claude Platform API access layer (workload → Claude), and Claude Tag agent identity at
    the Cowork product access layer (Claude → connected systems). Together they define service
    accounts as the correct identity primitive at both sides of the Claude Platform boundary.
  - `blog-anthropic-enterprise-managed-auth.md` Claim 4: "For admins, this folds MCP access
    management into the same workflow that governs the rest of your stack: provision once,
    scope by group, manage revocation through the IdP." Both sources describe admin-provisioned
    agent access models where revocation is a single operation with comprehensive scope. The
    enterprise-managed auth feature handles user access to MCP connectors; Claude Tag agent
    identity handles the agent's own service account access to connected systems. These are
    complementary layers in the same access management picture.

- **Extends**:
  - `blog-anthropic-zero-trust-ai-agents.md`: The zero-trust eBook (May 2026) described
    agent identity best practices as a security framework prescription (Phase 3: assign unique
    cryptographically rooted identity per agent; Phase 6: inject credentials at runtime from
    secrets management). This source (June 2026) documents Claude Tag's production
    implementation of those prescriptions at the product level. Relationship: eBook prescribed
    → Claude Tag delivered. Together they are the complete picture for how Anthropic thinks
    about agent identity at both the framework level and the product level.
  - `blog-anthropic-workload-identity-federation.md`: WIF (June 2026) covers the
    workload-to-Claude-Platform authentication boundary. Claude Tag agent identity covers the
    Claude-to-connected-systems authentication boundary within Cowork. These two sources
    together define both sides of the authentication picture: inbound (WIF: how workloads
    authenticate to Claude) and outbound (Claude Tag agent identity: how Claude authenticates
    to external systems on behalf of a channel).
  - `blog-anthropic-enterprise-managed-auth.md`: That source (June 2026) covers how
    organizations provision user access to MCP connectors via IdP. This source covers how the
    agent itself gets credentials to act under its own service accounts. Together they extend
    the enterprise MCP/connector access corpus: user provisioning (enterprise-managed auth) +
    agent service account identity (this source).

- **Contradicts**: None identified. The Claude Tag agent identity model is fully consistent
  with the zero-trust framework recommendations, WIF's service account architecture, and the
  enterprise-managed auth provisioning approach. The multiplayer problem framing (Claim 3)
  is novel in this corpus — no existing note argues the opposite position (that per-user
  credentials are adequate for multi-user team channels).

- **Novel**:
  - **Per-channel identity compartmentalization as a product feature**: No prior corpus
    source documents a product-level implementation where private channels automatically
    receive distinct agent identities and memory/access boundaries enforce separation between
    compartments. The zero-trust eBook describes compartmentalization as a design pattern
    (Phase 3: "break up some of the functions/goals of an agent into multiple agents — each
    with unique ID and own credentials"); this source shows it as a default product behavior.
  - **"Doubling every four months" as the agent task-duration growth rate**: This specific
    quantification of agent capability trajectory is new to the corpus. Prior notes document
    the shift to long-running agents qualitatively; this provides a quantitative rate.
  - **Dual audit trail architecture**: The specific combination of Claude's own audit trail
    plus each connected system's native logs as two independent records of agent action is
    new to the corpus. Prior sources describe audit trail requirements (zero-trust eBook Phase
    7, Phase 8); this is the first source to describe a shipped dual-trail implementation.
  - **Agent identity as the reframe from user-centric to compartment-centric access**:
    "Agent identity replaces the question 'what can this user do?' with 'what can this agent
    do in this compartment?'" — this formulation is new to the corpus and provides a vocabulary
    for the conceptual shift that practitioners need to make when designing team agent systems.
  - **JIT credential grants as a planned enhancement**: The concept of user-in-the-moment
    approval for a single sensitive action without permanent scope widening is new to the
    corpus as a forward-looking product capability (though the zero-trust eBook prescribes
    JIT access in Phase 6, no corpus source documents this as a planned Anthropic product
    feature before this announcement).
  - **Four-component identity profile taxonomy**: Repository access + connectors + skills/plugins
    + standing instructions as the explicit enumeration of what an agent identity comprises is
    new to the corpus as a named taxonomy.
  - **Single revocation sweep**: "Revoking an identity ends Claude's access everywhere that
    the identity was used" as a product property (rather than a security prescription) is
    documented here for the first time.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the agent identity model as the canonical access
  architecture for team-deployed autonomous agents. The four-component identity profile
  (repo access, connectors, skills/plugins, standing instructions) is the complete
  specification for what must be defined when standing up a team agent. The two-level
  hierarchy (workspace baseline + channel overrides) is the correct governance pattern:
  set least-privilege defaults at the broadest scope, grant exceptions at narrow scope.
  Currently the corpus has the zero-trust eBook's prescriptions and WIF's API-level
  implementation; this source adds the Cowork product-level example. Together these three
  sources define agent identity at framework, API, and product layers.

- **Chapter 05 (Team Adoption)**: Add the deliberate incremental grant practice (Claim 11)
  as the recommended Claude Tag rollout approach: baseline profile in a few channels, audit
  trail review, then expand one grant at a time. This is a concrete operationalization of
  the zero-trust least-privilege principle that practitioners can follow without needing to
  understand the underlying zero-trust framework. Also add: private channel identity
  compartmentalization is a default behavior that should be preserved — teams should not
  configure broad workspace-level identities for channels that discuss sensitive topics.

- **Chapter 05 (Team Adoption)**: Add the multiplayer problem (Claim 3) as the key
  explanation for why Claude in team channels needs its own identity rather than inheriting
  any individual user's credentials. "Whose permissions apply?" is the question that motivates
  the entire agent identity model. Teams evaluating this feature should understand this
  problem framing before evaluating the solution.

- **Chapter 06 (Security / Threat Model)**: Add the credential injection mechanism (Claim 8:
  "stored independently...injected at the network boundary at request time") as the reference
  implementation of secure credential handling in team agents. Credentials never enter the
  agent's reasoning context; they are applied at the infrastructure boundary at call time.
  Add the dual audit trail (Claim 10) as the audit architecture that makes agent actions
  investigatable in context: Claude's log (comprehensive cross-system record) + each
  connected system's log (native-format record for system-specific investigation).

- **Chapter 06 (Security / Threat Model)**: Update any section on agent offboarding or
  credential rotation to note the single-revocation-sweep property of agent identity (Claim
  12): revoking a Claude Tag identity ends access comprehensively across all connected
  systems in one operation, unlike per-credential revocation in user-delegated models. This
  is an operational security advantage that practitioners should factor into incident response
  planning.

- **Chapter 06 (Security / Threat Model) — future section on JIT access**: Flag the planned
  JIT credential grants (Claim 13) as the intended enhancement for the "approve single
  action without permanent scope widening" use case. Current deployments should use the
  baseline + incremental grant model; when JIT is shipped, it will provide more granular
  control for sensitive one-off actions. This planned feature directly implements Phase 6
  of the zero-trust eBook (zero-trust-ai-agents Claim 11: "JIT access: token lifetimes
  measured in minutes").

## Extraction Notes

1. **WebFetch returns AI-summarized content**: The claude.com blog renders as a JavaScript
   SPA; WebFetch AI-summarizes rather than returning verbatim HTML. Five separate WebFetch
   calls were made with progressively more targeted prompts to maximize quote fidelity.
   Quotes in this note that appear in double quotation marks were returned consistently
   across multiple fetches with identical wording; they are treated as verbatim. The two
   exceptions: "a departure from per-user Access Control Lists" appeared only in the first
   fetch (a general summary) and is not used as a verbatim quote here; the article's exact
   framing of the Increasing/Multiplayer reasons in full was only captured in fragments.
   All quotes presented as verbatim should be verified against the source URL before
   citation in the guide.

2. **Article is a compact product announcement**: Based on fetch content, the article is
   approximately a 5-8 minute read focused on the access model architecture. No sub-pages
   were linked that required following; the article is self-contained.

3. **"Claude Tag" product name**: The article describes the access model for "Claude Tag,"
   which appears to be the name for Claude operating within team workspace channels (a Claude
   Cowork capability). This is distinct from Claude Code and claude.ai chat. Context from
   `blog-anthropic-cowork-getting-started.md` confirms Claude Cowork as the team workspace
   product; Claude Tag is the specific in-channel agent identity within that product.

4. **Roadmap items**: Claims 13 describes features not yet shipped. The article describes
   JIT credential grants and identity-aware overlays as planned future enhancements, not
   current capabilities. These are treated as forward-looking vendor intent.

5. **No contradictions filed**: Cross-referencing against the corpus found no material
   contradictions. The agent identity model is consistent with and extends the zero-trust
   prescriptions, WIF's service account pattern, and enterprise-managed auth's admin
   provisioning approach. All three existing sources are complementary, not opposing.

6. **Overall confidence rated "emerging"**: Core architectural claims (credential isolation,
   channel compartmentalization, dual audit trail) are first-party vendor assertions about
   shipping product behavior — rated "settled" individually. The overall note is rated
   "emerging" because (a) the security properties cannot be independently verified from
   outside the product, (b) roadmap items are forward-looking, and (c) no third-party
   deployment data or security audit exists yet for this feature.
