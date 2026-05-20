---
source_url: https://claude.com/blog/claude-managed-agents-updates
source_type: blog-post
title: "New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels"
author: Anthropic (product announcement)
date_published: 2026-05-19
date_extracted: 2026-05-20
last_checked: 2026-05-20
status: current
confidence_overall: anecdotal
issue: "#820"
---

# New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

> May 19, 2026 Anthropic product update introducing two new deployment options
> for Claude Managed Agents: self-hosted sandboxes (public beta) that move tool
> execution into customer-controlled infrastructure while keeping orchestration on
> Anthropic, and MCP tunnels (research preview) that connect agents to private
> network MCP servers via a single outbound gateway connection with no inbound
> firewall rules.

## Source Context

- **Type**: blog-post (official Anthropic product announcement, claude.com blog,
  May 19, 2026; feature update to Claude Managed Agents, which launched April 8,
  2026 — see blog-anthropic-claude-managed-agents.md)
- **Author credibility**: First-party Anthropic announcement — authoritative on
  what the platform provides and which access tier features occupy. Five customer
  quotes from named individuals with titles (Ryan Chang/Clay AI Engineering,
  Strib Walker/Rogo Head of Product, Sai Yandapalli/Mason CTO, Will Newton/Amplitude
  Design, Andy Fang/DoorDash Co-founder), similar evidential weight to the April 8
  announcement's eight named executives. DoorDash is "excited to evaluate" rather
  than in production — weaker than the other four.
- **Scope**: Covers two new features: (1) self-hosted sandboxes — moving tool
  execution from Anthropic-hosted to customer-managed infrastructure, with four
  named provider integrations (Cloudflare, Daytona, Modal, Vercel) plus a
  bring-your-own-client option; (2) MCP tunnels — a single-outbound-connection
  gateway for reaching private network MCP servers without public exposure. Does
  NOT cover: changes to pricing, harness/orchestration architecture, memory or
  dreaming features, outcomes or multiagent orchestration (covered in prior notes).
  The post's technical level is marketing/product — no SDK code, no API details.

## Extracted Claims

### Claim 1: Self-hosted sandboxes split the Managed Agents architecture — orchestration stays on Anthropic infrastructure, tool execution moves to customer-controlled environments

- **Evidence**: First-party architectural description of the split. This is the
  core structural claim: the harness loop (orchestration, context management, error
  recovery) remains hosted by Anthropic; the sandbox (where tools execute) is now
  a customer-pluggable component.
- **Confidence**: settled (explicit product design description from first-party source)
- **Quote**: "The agent loop that handles orchestration, context management, and
  error recovery stays on Anthropic's infrastructure, while tool execution moves
  to your own configured environment."
- **Our assessment**: This announcement represents a significant evolution from
  the April 8 launch (blog-anthropic-claude-managed-agents.md), which described
  sandboxed code execution as a platform-managed feature. The April 8 platform
  capability matrix listed "Sandboxed code execution (for all agents)" in the
  EXECUTION LAYER without distinguishing who hosts it. This post makes the sandbox
  layer a customer-pluggable component, formalizing the split described abstractly
  in blog-anthropic-scaling-managed-agents.md (Claim 2: session/harness/sandbox
  as three virtualized components with stable interfaces). The key implication for
  practitioners: you can adopt Managed Agents for its orchestration layer while
  keeping execution compute within your own infrastructure.

### Claim 2: Customer-controlled sandboxes enable enterprises to keep sensitive files, packages, services, and data within their own security perimeter

- **Evidence**: First-party feature description with explicit enterprise framing
  (perimeter, network policies, audit logging, security tooling).
- **Confidence**: settled (explicit product feature description)
- **Quote**: "With self-hosted sandboxes, you keep sensitive files, packages, and
  services in your own infrastructure or with a managed sandbox provider. [...] Inside
  your perimeter, network policies, audit logging, and security tooling are already
  in place, and files and repositories don't leave."
- **Our assessment**: The data-residency framing is the primary enterprise driver for
  self-hosted sandboxes. The original platform required that tool execution happen in
  Anthropic-hosted sandboxes; for organizations with regulatory constraints (data
  residency requirements, export controls, contractual limits on third-party data
  processing), this was a blocker. Self-hosted sandboxes remove the blocker by making
  the execution layer customer-sovereign. The "files and repositories don't leave"
  property is the key data-residency guarantee. This corroborates the build-vs-buy
  framing in blog-anthropic-claude-managed-agents.md (Claim 8) by adding a third
  option: managed orchestration + customer execution.

### Claim 3: Customers control compute resources — resource sizing, runtime images, and capacity — enabling agents to handle compute-heavy workloads like long builds or image generation

- **Evidence**: First-party feature description with concrete workload examples.
- **Confidence**: settled (explicit product feature announcement)
- **Quote**: "You also control the compute: resource sizing and the runtime image are
  set on your side, so agents running compute-heavy work such as long builds or image
  generation get the CPU, memory, and capacity the task needs."
- **Our assessment**: Compute resource control addresses a fundamental limitation of
  managed sandboxes: Anthropic-hosted execution environments have fixed resource
  allocations optimized for typical agent workloads, not compute-heavy tasks. This
  claim extends agent applicability to workloads that require GPU compute (image
  generation), large memory (ML inference), or sustained CPU (long builds). The
  "runtime image" control also enables customers to pre-install domain-specific
  dependencies (e.g., language runtimes, specialized tools) without having the agent
  install them on each session.

### Claim 4: Any sandbox client can be plugged in — the platform is not limited to the four named providers

- **Evidence**: First-party statement of the open design.
- **Confidence**: settled (explicit "bring any sandbox client" statement)
- **Quote**: "Bring any sandbox client you want, or start with one of our supported providers"
- **Our assessment**: The "bring any" framing is architecturally important — it confirms
  that Anthropic has exposed a stable sandbox interface (the execute(name, input) → string
  interface described in blog-anthropic-scaling-managed-agents.md Claim 8) as a customer-
  facing extension point, not just as an internal platform component. The four named
  providers (Cloudflare, Daytona, Modal, Vercel) are convenience integrations, not the
  limit of what's supported. This validates the "opinionated about interfaces, unopinionated
  about implementations" design philosophy from blog-anthropic-scaling-managed-agents.md
  (Claim 10): the sandbox interface is stable enough to support arbitrary provider plug-ins.

### Claim 5: Daytona sandboxes are full stateful computers with SSH access and pause/restore capability, suited to long-running and extended agent sessions

- **Evidence**: First-party provider description with specific technical properties named.
- **Confidence**: settled (first-party architectural description of a supported provider)
- **Quote**: "sandboxes are full composable computers, long-running and stateful" —
  "accessible while a session runs over SSH or an authenticated preview URL, or can
  be paused and restored with full state preserved"
- **Our assessment**: Daytona's pause/restore capability is architecturally significant
  for long-running agent workflows. The ability to pause a running sandbox and restore
  it with full state (filesystem, processes, network connections) enables workflows that
  exceed the typical session window without losing intermediate computation. SSH access
  during a session also enables human inspection or debugging of agent-managed environments
  mid-workflow. This is the first corpus mention of pause/restore for agent execution
  environments — distinct from the session log persistence described in
  blog-anthropic-scaling-managed-agents.md (Claim 5: stateless harness recovery via
  wake(sessionId)), which recovers harness state but not sandbox state.

### Claim 6: Cloudflare sandboxes provide microVM isolation with zero-trust secrets injection and customizable egress proxy controls for network-sensitive workloads

- **Evidence**: First-party provider description with specific security feature names.
- **Confidence**: settled (explicit provider feature description)
- **Quote**: "runs sandboxes at scale using microVMs and lighter weight isolates" with
  "zero-trust secrets injection, customizable proxies to audit, reroute, or modify
  egress, and the ability to connect to internal services over Cloudflare's network."
- **Our assessment**: The Cloudflare security model extends the basic credential-isolation
  approach (credentials never in sandbox) with network-layer controls: egress can be
  audited, rerouted, or blocked at the proxy level. The "zero-trust secrets injection"
  pattern is a production implementation of the credential security design documented in
  blog-anthropic-scaling-managed-agents.md (Claim 7: credentials structured to be
  inaccessible from Claude-generated code). The ability to connect internal services over
  Cloudflare's own network (not the public internet) also addresses data-residency concerns
  for network-level data flows, complementing the filesystem-level data-residency of
  self-hosted sandboxes generally.

### Claim 7: Modal provides sub-second startup with GPU and CPU compute on demand, scaling to hundreds of thousands of concurrent sandboxes — suited to AI-intensive agent workloads

- **Evidence**: First-party provider description with specific metrics.
- **Confidence**: settled (first-party provider description with named scale metric)
- **Quote**: "cloud platform built for AI workloads, where sandboxes share the same
  foundation as Modal's functions, storage, and networking primitives." "custom container
  runtime delivers sub-second startup on any image, scales to hundreds of thousands of
  concurrent sandboxes, and gives you CPU and GPU resources on demand."
- **Our assessment**: Modal is the only provider in this announcement that explicitly
  offers GPU compute. This is the first corpus mention of GPU resource availability for
  agent tool execution, enabling agent workloads like ML model inference, image processing,
  or video generation within agent-managed sandboxes. The sub-second startup on any image
  (including custom images with pre-installed ML libraries) combined with GPU availability
  positions Modal as the provider for compute-intensive AI-adjacent tasks. The "hundreds of
  thousands of concurrent sandboxes" scale figure is also the most aggressive scaling claim
  among the four providers, suggesting Modal is positioned for high-throughput multi-agent
  deployments.

### Claim 8: Vercel sandboxes inject credentials at the network boundary so they never enter the sandbox — a structural credential security guarantee

- **Evidence**: First-party provider description with explicit security mechanism named.
- **Confidence**: settled (explicit security design description from first-party source)
- **Quote**: "combine VM security, VPC peering, and bring your own cloud with millisecond
  startup time." "Vercel Sandbox firewall injects credentials at the network boundary so
  they never enter the sandbox."
- **Our assessment**: Vercel's credential injection pattern is a live production
  implementation of the credential security design in blog-anthropic-scaling-managed-agents.md
  (Claim 7): "the tokens are never reachable from the sandbox where Claude's generated
  code runs." The "firewall injects credentials at the network boundary" mechanism is
  a third pattern alongside the two documented in the engineering post (bundle-with-resource
  and vault+proxy) — here the firewall itself is the trusted intermediary, and credentials
  are injected at the network layer rather than at provision time or via a proxy. VPC
  peering and "bring your own cloud" add network-level isolation and flexibility beyond
  the basic sandbox model. The millisecond startup is the fastest quoted among the providers,
  suited to workloads that need to minimize cold-start latency.

### Claim 9: MCP tunnels enable private network MCP servers to become agent-callable tools through a single outbound connection — no inbound firewall rules, no public endpoints, encrypted end to end

- **Evidence**: First-party architectural description with specific network topology details.
- **Confidence**: settled (explicit product architecture description)
- **Quote**: "With MCP tunnels, your agents reach MCP servers inside your private network
  without exposing them to the public internet. Internal databases, private APIs, knowledge
  bases, and ticketing systems become tools your agents can call. A lightweight gateway you
  deploy makes a single outbound connection, no inbound firewall rules, no public endpoints,
  and traffic encrypted end to end."
- **Our assessment**: MCP tunnels address a fundamental enterprise deployment barrier: the
  private-network integration problem. blog-anthropic-mcp-production-agents.md (Claim 5)
  recommends building remote MCP servers for production cloud agents; but for enterprises
  with private internal systems (internal databases, ticketing systems, knowledge bases),
  "remote" means public-internet-exposed, which conflicts with their security posture.
  MCP tunnels resolve this by inverting the connection model: instead of the agent reaching
  into the private network (which requires firewall rules), the private-network gateway
  reaches out to Anthropic (single outbound connection). This is the network-level
  complement to self-hosted sandboxes: sandboxes keep compute within the perimeter;
  tunnels keep data access within the perimeter.

### Claim 10: MCP tunnels are managed from workspace settings by organization admins and work with both Managed Agents and the Messages API

- **Evidence**: First-party feature description with specific management surface and API scope.
- **Confidence**: settled (explicit product feature description)
- **Quote**: "MCP tunnels is managed from workspace settings within the Claude Console by
  organization admins."
- **Our assessment**: The workspace-admin management model (rather than per-project or per-
  developer configuration) signals that MCP tunnels are designed as an enterprise infrastructure
  capability — set up once by admins, available to all agents in the workspace. The Messages
  API support (not just Managed Agents) is notable: it means the private-network MCP access
  pattern extends beyond the Managed Agents platform to any Claude API integration that uses
  the Messages API with MCP. This broadens the impact of the feature significantly — it is
  not a Managed Agents-only capability. Research preview status means access requires a
  separate request.

### Claim 11: Named customer implementations demonstrate the self-hosted sandbox model in production across diverse workloads — Clay (GTM automation with Daytona), Rogo (financial AI with Vercel), Mason (enterprise tools with Modal), Amplitude (design agent with Cloudflare)

- **Evidence**: Four customer testimonials from named individuals with titles, with
  specific provider, workload, and deployment timeline evidence.
- **Confidence**: anecdotal (named customers with real individuals and titles; no independent
  audit; DoorDash specifically notes "evaluating" rather than deployed)
- **Quote (Clay, Ryan Chang, AI Engineering)**: "Claude Managed Agents let us replicate
  the power of a local agent with the reliability, versioning, and background execution of
  a cloud agent. And running it with our sandboxes, like Daytona, gives us control over the
  filesystem, so we can mount external file stores and install packages on the fly."
- **Quote (Rogo, Strib Walker, Head of Product)**: "Claude Managed Agents handles the agent
  loop, Vercel's sandboxes give us an environment we can configure for our workloads. This
  gives us the option to leverage best-in-class infrastructure while we focus on what
  compounds for a financial AI platform: depth and breadth of tools and data, and a product
  surface built for how investors and bankers actually work."
- **Quote (Mason, Sai Yandapalli, CTO)**: "Modal's sandbox gives us the security boundary
  our enterprise customers need, and combining it with Claude Managed Agents gives us a
  powerful harness without hand-rolling extra complexity. We had a working version up in
  under a week, raising reliability for our customers."
- **Quote (Amplitude, Will Newton, Design)**: "Claude Managed Agents and Cloudflare let us
  get the first useful version of our design agent running in two days on infrastructure we
  already know and trust."
- **Our assessment**: The customer testimonials make two structural arguments: (1) the
  managed orchestration layer is valuable enough to adopt even when you also want execution
  control ("powerful harness without hand-rolling extra complexity" — Mason); (2) familiar
  infrastructure is a meaningful productivity multiplier ("infrastructure we already know
  and trust" — Amplitude, "two days"). The speed claims (Mason: < 1 week, Amplitude: 2 days)
  are consistent with the weeks-to-days deployment timelines documented in the April 8
  announcement (blog-anthropic-claude-managed-agents.md, Claim 8). Clay's description of
  mounting external file stores and installing packages on the fly illustrates the key
  capability unlocked by Daytona's filesystem access that Anthropic-managed sandboxes cannot
  provide. Rogo's framing ("focus on what compounds") is the clearest articulation in any
  corpus source of the build-vs-buy argument for managed orchestration: let the platform
  handle the loop so the team can invest in domain-specific depth.

## Concrete Artifacts

### Self-Hosted Sandbox Architecture (May 19, 2026)

```
Claude Managed Agents — Self-Hosted Sandbox Model:

ANTHROPIC-HOSTED (unchanged from April 8, 2026):
  - Agent loop: orchestration, context management, error recovery
  - Session management (persistent event log)
  - Harness: stateless, recoverable via wake(sessionId)

CUSTOMER-CONTROLLED (new as of May 19, 2026):
  - Sandbox (execution environment for tool calls)
  - Network policies, audit logging, security tooling
  - Resource sizing and runtime images
  - Files, repositories, and sensitive data (never leave perimeter)

INTERFACE: execute(name, input) → string (per blog-anthropic-scaling-managed-agents.md Claim 8)
  - Any client implementing this interface can plug in
  - Four named provider integrations included

ACCESS TIER: Public beta (as of May 19, 2026)
```

### Sandbox Provider Technical Comparison

```
Provider    | Compute         | Security Pattern              | Startup     | Key Characteristic
------------|-----------------|-------------------------------|-------------|--------------------------------------------
Cloudflare  | CPU (microVMs)  | Zero-trust secrets injection, | Not stated  | Customizable egress proxy; internal services
            |                 | customizable egress proxy     |             | over Cloudflare network
Daytona     | CPU+state       | Filesystem isolation          | Not stated  | Full stateful computers; SSH access;
            |                 |                               |             | pause/restore with full state preserved
Modal       | CPU + GPU       | AI-workload-native            | Sub-second  | GPU resources on demand; scales to 100k+
            |                 |                               |             | concurrent sandboxes
Vercel      | CPU (VM)        | Firewall credential injection | Millisecond | Credentials injected at network boundary;
            |                 | at network boundary           |             | VPC peering; bring your own cloud

Custom      | Any             | Customer-defined              | Any         | "Bring any sandbox client you want"

Source: Anthropic product announcement (2026-05-19)
```

### MCP Tunnels Architecture

```
Claude Managed Agents — MCP Tunnels Model:

PRIVATE NETWORK (customer-controlled):
  - MCP servers: internal databases, private APIs, knowledge bases, ticketing systems
  - Lightweight gateway: deployed in customer's private network
  - Connection: single outbound connection from gateway → Anthropic
  - No inbound firewall rules required, no public endpoints required
  - Traffic: encrypted end to end

MANAGEMENT:
  - Managed via workspace settings in Claude Console
  - Administered by organization admins
  - Works with: Managed Agents + Messages API (not Managed Agents-only)

ACCESS TIER: Research preview (access request required, as of May 19, 2026)
```

### Customer Deployment Evidence

```
Company    | Provider   | Workload                   | Timeline        | Named individual
-----------|------------|----------------------------|-----------------|---------------------------
Clay       | Daytona    | GTM engineering agent      | Not stated      | Ryan Chang, AI Engineering
           |            | (Sculptor) — filesystem,   |                 |
           |            | file stores, packages      |                 |
Rogo       | Vercel     | Financial AI platform for  | Not stated      | Strib Walker, Head of Product
           |            | investors and bankers      |                 |
Mason      | Modal      | Enterprise internal tool   | Under a week    | Sai Yandapalli, CTO
           |            | orchestration              |                 |
Amplitude  | Cloudflare | Design agent               | Two days        | Will Newton, Design
DoorDash   | Modal      | Agentic commerce for local | Evaluating      | Andy Fang, Co-founder
           |            | businesses (pre-production)|                 |

Source: Anthropic product announcement (2026-05-19)
All deployment claims: customer-reported, no independent audit
```

## Cross-References

- **Corroborates**:
  - **blog-anthropic-scaling-managed-agents.md** (Claim 8): The `execute(name, input) → string`
    uniform sandbox interface, described there as the architectural abstraction that makes
    any execution environment a swappable "hand," is validated here by four production providers
    plugging in through the same interface. The "bring any sandbox client" statement confirms
    the interface is now exposed as a customer-facing extension point, not just an internal
    platform component.
  - **blog-anthropic-scaling-managed-agents.md** (Claim 7): Vercel's "Sandbox firewall injects
    credentials at the network boundary so they never enter the sandbox" is a live production
    implementation of the credential security design documented there ("make sure the tokens are
    never reachable from the sandbox where Claude's generated code runs"). Vercel's firewall
    injection is a third pattern alongside the two in that note (bundle-with-resource and vault+proxy).
  - **blog-anthropic-scaling-managed-agents.md** (Claim 10): The "opinionated about interfaces,
    unopinionated about implementations" design philosophy is confirmed by the "bring any sandbox
    client" statement — the interface is stable enough to support arbitrary third-party implementations.
  - **blog-anthropic-mcp-production-agents.md** (Claim 5): "Build remote servers so agents can use
    your system wherever they run." MCP tunnels extend this recommendation to private-network servers
    that cannot be made publicly remote without violating enterprise security policy. Tunnels are the
    infrastructure primitive that makes "remote" applicable to private-network MCP servers.
  - **blog-anthropic-claude-managed-agents.md** (Claim 8): The weeks-to-days deployment speed
    documented in the April 8 announcement is corroborated here — Amplitude reports 2 days; Mason
    reports under a week — extending the evidence base for this claim to self-hosted deployments.
  - **blog-anthropic-claude-managed-agents.md** (Claim 2): "The agent loop that handles
    orchestration, context management, and error recovery stays on Anthropic's infrastructure" —
    this post's architectural description repeats the same framing from the April 8 announcement
    verbatim, confirming that the harness layer is unchanged by the self-hosted sandbox option.

- **Extends**:
  - **blog-anthropic-claude-managed-agents.md**: The April 8 platform capability matrix listed
    "Sandboxed code execution (for all agents)" as a single platform feature. This post splits
    sandbox execution into managed (Anthropic-hosted, unchanged) and self-hosted (customer-pluggable,
    new). The build-vs-buy framing from that note gains a third option: managed orchestration +
    customer-controlled execution (in addition to fully-managed and fully-DIY).
  - **blog-anthropic-scaling-managed-agents.md** (Claim 2): The session/harness/sandbox
    three-component architecture now has the sandbox as an externally pluggable component.
    This post formalizes what was described as an internal architectural split into a
    customer-facing deployment model. The "virtualized with stable interfaces" design is
    confirmed as forward-looking: the sandbox interface was designed to be pluggable before
    self-hosting was a product feature.
  - **blog-anthropic-mcp-production-agents.md** (Claim 4): MCP as the production integration
    layer now includes private-network MCP servers via tunnels. The corpus previously covered
    public remote MCP servers (the recommended pattern) and local stdio servers (for development).
    MCP tunnels add a third connection topology for private/enterprise deployment.

- **Contradicts**: None identified. The shift from Anthropic-managed-only sandbox to
  customer-pluggable sandbox is an extension, not a contradiction of the April 8 announcement.
  The April 8 announcement did not state that Anthropic-hosted sandboxes were the only option
  — it described the platform's included execution infrastructure without foreclosing future
  customer-hosted variants.

- **Novel**:
  - **Hybrid orchestration-execution model as a named deployment pattern**: No prior corpus
    source describes an architecture where the orchestration/harness layer is managed by the
    platform vendor while the execution/sandbox layer is customer-controlled. This is a new
    point on the managed-vs-DIY spectrum: more control than fully managed, less build burden
    than fully DIY.
  - **MCP tunnels as a zero-firewall-change private network integration primitive**: No prior
    corpus source describes a mechanism for reaching private-network MCP servers without public
    exposure or inbound firewall rules. The single-outbound-connection gateway pattern is new.
  - **GPU compute availability in agent sandboxes**: Modal's GPU-on-demand is the first
    corpus mention of GPU resources being available for agent tool execution. Enables
    compute-intensive workloads (ML inference, image generation) in agent-managed sandboxes.
  - **Sandbox pause/restore with full state preserved (Daytona)**: No prior corpus source
    describes pauseable/restorable agent execution environments. Distinct from harness recovery
    (blog-anthropic-scaling-managed-agents.md Claim 5), which recovers agent loop state but
    not the execution environment state.
  - **Credential injection at the network boundary (Vercel)**: The Vercel Sandbox firewall
    pattern — credentials injected by the firewall, never entering the sandbox — is a third
    credential security pattern not documented in blog-anthropic-scaling-managed-agents.md,
    which described bundle-with-resource and vault+proxy. All three achieve the same security
    goal (credentials unreachable from agent-generated code) via different mechanisms.
  - **MCP tunnels for Messages API**: The revelation that MCP tunnels work with the Messages
    API (not only Managed Agents) significantly broadens the feature's reach. Any Claude API
    integration using the Messages API can leverage private-network MCP servers via tunnels,
    not just Managed Agents customers.

## Guide Impact

- **Chapter 02 (Harness Engineering)** — Build-vs-Buy section: Add a third option to the
  managed/DIY spectrum: *hybrid* (Anthropic-managed orchestration + customer-controlled
  execution). Current guide material frames the choice as binary (managed platform vs. DIY
  harness). Self-hosted sandboxes create a middle path — teams that need execution control
  (data residency, custom compute, network policies) without having to build the orchestration
  layer themselves. The Rogo quote is the clearest articulation: "Claude Managed Agents handles
  the agent loop, Vercel's sandboxes give us an environment we can configure for our workloads.
  This gives us the option to leverage best-in-class infrastructure while we focus on what
  compounds for a financial AI platform."

- **Chapter 02 (Harness Engineering)** — Credential security: Add Vercel's firewall injection
  pattern as a third credential security approach alongside the two in blog-anthropic-scaling-
  managed-agents.md (Claim 7: bundle-with-resource, vault+proxy). Frame all three as
  implementations of the same architectural invariant: agent-generated code must never be able
  to read credentials from its own execution environment.

- **Chapter 05 (Multi-Agent Orchestration) / MCP integration**: Add MCP tunnels as the
  infrastructure primitive for enterprise/private-network MCP deployment. Complement
  blog-anthropic-mcp-production-agents.md's remote-server guidance (Claim 5) with the
  private-network variant: for systems that cannot be publicly exposed, deploy a tunnel
  gateway rather than a public remote MCP server. Document the management model: workspace-
  admin configured, not per-developer.

- **Chapter 06 (Production Deployment)**: Update the deployment model taxonomy:
  - Fully managed (Anthropic-hosted execution): original April 8 offering
  - Hybrid (Anthropic orchestration + customer sandbox): this announcement
  - Fully DIY (custom harness + custom sandbox): traditional self-built approach
  The hybrid model serves the enterprise segment that needs execution control without
  orchestration build burden. The customer evidence (Clay, Rogo, Mason, Amplitude) provides
  validated deployment patterns across workload types: GTM automation, financial AI, enterprise
  tools, design agents.

- **Chapter 08 (Governance / Permissions)**: The self-hosted sandbox governance model —
  customer-controlled network policies, audit logging, and security tooling within their own
  perimeter — is a new governance pattern for agent deployments. Practitioners evaluating
  governance options should know that Managed Agents now supports delegating execution
  governance to existing enterprise security infrastructure (their own network controls,
  their own audit logs) rather than relying entirely on Anthropic-provided governance.

## Extraction Notes

- The Prospector's third triage comment listed "Clay (Daytona), Vercel, Modal, Cloudflare,
  Lyrebird" as five named customer implementations. **Lyrebird does not appear in the article.**
  The actual five customers named are Clay (Daytona), Rogo (Vercel), Mason (Modal), Amplitude
  (Cloudflare), and DoorDash (Modal, evaluating). The Lyrebird mention in the triage comment
  is incorrect — do not include Lyrebird in any guide citations derived from this source.
- The blog is a JavaScript-rendered SPA. Multiple WebFetch passes were made with targeted
  prompts to maximize verbatim quote fidelity. All customer quotes were extracted in a dedicated
  fetch pass and are treated as accurate. The technical descriptions of each provider were
  extracted in a separate pass and compared across fetches for consistency.
- No pricing changes are mentioned. The $0.08/session-hour rate from the April 8 announcement
  is presumably unchanged; self-hosted sandboxes may have different pricing implications
  (customer pays their sandbox provider separately) but this is not stated.
- The "Bring any sandbox client" statement implies a documented sandbox API/SDK, but the
  blog post does not describe it — directing readers to docs and cookbooks instead. A
  documentation extraction of the Managed Agents platform docs would provide the interface
  specification for custom sandbox implementations.
- DoorDash is described as "excited to evaluate" rather than deployed — weaker evidence than
  the four deployed customers. Their testimonial is treated as signaling intent rather than
  production validation.
- MCP tunnels availability is "research preview" (requiring access request), the same tier as
  dreaming in the May 6 announcement. Self-hosted sandboxes are "public beta" — broadly
  accessible. Claims about MCP tunnels should be treated with the research-preview caveat.
