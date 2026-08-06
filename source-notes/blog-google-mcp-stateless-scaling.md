---
source_url: https://developers.googleblog.com/scaling-ai-agent-infrastructure-with-the-mcp-stateless-updates/
source_type: blog-post
title: "Scaling AI Agent Infrastructure with the MCP Stateless updates"
author: Kurtis Van Gent (Senior Staff Software Engineer, Google Cloud Data) and Alan Blount (Senior Technical Product Manager)
date_published: 2026-08-05
date_extracted: 2026-08-06
last_checked: 2026-08-06
status: current
confidence_overall: emerging
issue: "#2524"
---

# Scaling AI Agent Infrastructure with the MCP Stateless updates

> Google's first-party technical writeup of the 2026-07-28 MCP specification release
> candidate, which removes the `initialize` handshake and `Mcp-Session-Id` header
> entirely in favor of a fully stateless, self-describing request model — enabling
> plain round-robin load balancing, serverless MCP deployment, standardized HTTP
> routing headers (SEP-2243) for deep-packet-inspection-free gateways, stateless
> elicitation via Multi Round-Trip Requests (SEP-2322), a first-class async Tasks
> Extension (SEP-2663), and a formal 12-month deprecation policy (SEP-2577).

## Source Context

- **Type**: blog-post (official Google Developers Blog, first-party technical
  announcement/explainer, published August 5, 2026, describing the MCP Transports
  Working Group's 2026-07-28 spec release candidate)
- **Author credibility**: Written by two named Google engineers — a Senior Staff
  Software Engineer on Google Cloud Data and a Senior Technical Product Manager —
  not an anonymous team byline. The post states Google "co-founded the MCP Transports
  Working Group" with Hugging Face and other industry partners and "led the charge"
  on the stateless redesign, making Google a primary author of the spec change itself,
  not merely a commentator. This is first-party protocol documentation from one of
  the parties who wrote the spec. It is a vendor announcement, not independent
  practitioner validation — the "no Redis sessions needed" and "GitHub MCP Server"
  claims are asserted, not benchmarked, by this post.
- **Scope**: Covers the architectural rationale and mechanics of the MCP stateless
  core redesign — the deprecated session handshake, the new self-describing request
  model, HTTP header standardization (SEP-2243), caching fields (SEP-2549), Multi
  Round-Trip Requests / elicitation (SEP-2322), the Tasks Extension (SEP-2663),
  security enhancements (issuer verification, resource indicators, JSON Schema
  2020-12), the deprecation policy (SEP-2577), and SDK migration paths for Python,
  TypeScript, Go, and C#. Does NOT cover: MCP server design principles (tool
  grouping, code-orchestration patterns — see `blog-anthropic-mcp-production-agents.md`),
  gh-aw's gateway implementation details, MCP token/context cost, or real-time
  bidirectional streaming infrastructure (a related but distinct problem domain —
  see Extraction Notes).

## Extracted Claims

### Claim 1: The original (2025-11-25) MCP session model required a stateful handshake and pinned clients to specific server instances, breaking horizontal scaling for cloud-native deployments

- **Evidence**: First-party architectural description with a named failure taxonomy
  (Load Balancing Tax, Sticky Routing Overheads, Zero Fault Tolerance, Complex
  Infrastructure Demands) and a concrete symptom (`400 Session Not Found` errors
  behind a round-robin load balancer).
- **Confidence**: settled (structural protocol description of a now-deprecated
  mechanism; the failure mode is a well-understood distributed-systems problem —
  sticky sessions vs. horizontal scaling)
- **Quote**: "The server responded with an Mcp-Session-Id header. To make any
  subsequent tool call or resource query, the client had to include that unique
  session ID on every request, pinning the client to the specific container or pod
  that held its in-memory session state."
- **Quote (symptom)**: "Deploying behind a Kubernetes cluster with three pods meant
  a second request from a client would randomly hit another pod, returning a 400
  Session Not Found error."
- **Our assessment**: This is a concrete, specific production failure mode — not a
  hypothetical. Any team that deployed MCP servers over HTTP behind a standard
  load balancer (rather than stdio, or a single pinned instance) before this spec
  change would have hit exactly this error. It explains why remote/cloud MCP
  deployment historically required either sticky-session load balancer
  configuration or a shared session store (Redis), both of which this source frames
  as unwanted operational tax.

### Claim 2: The 2026-07-28 spec removes the `initialize`/`initialized` handshake (SEP-2575) and the `Mcp-Session-Id` header (SEP-2567) entirely; every request is now self-describing via an inline `_meta` field

- **Evidence**: First-party spec description with before/after JSON-RPC examples
  (legacy handshake POST vs. new stateless `tools/call` POST carrying
  `_meta["io.modelcontextprotocol/protocolVersion"]`,
  `_meta["io.modelcontextprotocol/clientCapabilities"]`, and
  `_meta["io.modelcontextprotocol/clientInfo"]` on every request).
- **Confidence**: settled (direct description of a named, numbered spec change —
  SEP-2575 and SEP-2567 — with worked code examples)
- **Quote**: "The handshake is gone. The initialize / initialized handshake
  (SEP-2575) and the logical Mcp-Session-Id header (SEP-2567) have been removed
  entirely."
- **Quote (mechanism)**: "Protocol version, client info, and client capabilities
  that used to be exchanged once at connection setup now travel in a _meta field
  inline on every single request."
- **Our assessment**: This is the load-bearing architectural change the entire
  article is built around. Moving connection-setup metadata from a one-time
  handshake into a per-request `_meta` payload is what makes any container instance
  interchangeable for any request — the mechanism directly enables Claim 3's
  architectural advantages. For practitioners, this means MCP client libraries
  built against the 2025-11-25 handshake model will not work unmodified against
  2026-07-28 servers; this is a breaking protocol change, softened only by the
  12-month deprecation window (Claim 9).

### Claim 3: Statelessness enables plain round-robin load balancing, serverless MCP deployment (Cloud Run/Cloud Functions), and transparent failover with zero session disruption

- **Evidence**: First-party list of architectural advantages following directly from
  Claim 2's mechanism.
- **Confidence**: settled (logical consequence of the stateless design described in
  Claim 2 — if no per-instance state exists, any instance can serve any request by
  construction)
- **Quote**: "Because any container instance can handle any incoming request, you
  can throw your stateful MCP servers behind a plain round-robin load balancer."
- **Quote (serverless)**: "You can now run MCP servers as serverless functions on
  platforms like Google Cloud Run or Google Cloud Functions. Since there is no
  persistent connection to maintain, your servers spin down to zero when idle,
  drastically reducing costs."
- **Our assessment**: The serverless/scale-to-zero claim is the most consequential
  cost implication for practitioners: previously, a persistent SSE connection for
  session state meant an MCP server had to stay warm to serve any client, which is
  incompatible with scale-to-zero serverless billing. Removing that requirement
  means MCP servers can adopt the same cost model as stateless HTTP APIs. This is
  the concrete "why should I care" answer for Ch06 (production infrastructure
  patterns) — teams currently running always-on MCP server pods purely to hold
  session state have a cost-reduction path once they adopt the new spec.

### Claim 4: The GitHub MCP Server has already upgraded to the new spec and removed its Redis session storage entirely, eliminating database reads/writes on every call

- **Evidence**: Named, specific production example cited as evidence of real-world
  adoption, not a hypothetical.
- **Confidence**: emerging (single named example, asserted by Google without
  independent benchmarking or a link to a GitHub-authored confirmation; still, it
  is a specific, falsifiable claim about a widely-used production MCP server rather
  than a generic assertion)
- **Quote**: "Major production servers, such as the GitHub MCP Server, have already
  upgraded to this spec and completely removed Redis session storage, eliminating
  database writes and reads on every single call to make interactions snappier."
- **Our assessment**: This is the closest thing in the article to independent
  verification — a specific, named, widely-deployed server (referenced elsewhere in
  the corpus via `docs-ghaw-mcps.md`'s shared MCP library and multiple gh-aw notes)
  that removed a concrete piece of infrastructure (Redis) as a direct result of the
  spec change. If accurate, it is a real before/after production data point, not
  vendor marketing language alone. Practitioners running their own MCP servers with
  Redis-backed session stores have a direct migration incentive: removing Redis
  removes a stateful dependency, an operational cost, and a per-call latency hop.

### Claim 5: SEP-2243 promotes protocol version, method, and tool/resource name to standard HTTP headers (`Mcp-Protocol-Version`, `Mcp-Method`, `Mcp-Name`), letting gateways route, rate-limit, and audit traffic without deep packet inspection

- **Evidence**: First-party spec description with a worked HTTP request example
  showing all three headers alongside the mirrored JSON-RPC body, plus the explicit
  error behavior when header and body values disagree.
- **Confidence**: settled (direct description of a named spec section, SEP-2243,
  with a concrete error code)
- **Quote**: "These headers are mirrored to match the JSON-RPC body. If they
  disagree, the server rejects the request with a -32020 header mismatch code."
- **Quote (security/ops benefit)**: "By promoting these values to standard HTTP
  headers, proxies, gateways, and load balancers can route, rate-limit, and audit
  traffic without inspecting the request body. For security and logging teams, this
  is a massive win that drastically lowers the latency and processing overhead at
  the gateway layer."
- **Our assessment**: This is the single most relevant claim for Ch08 (Observability)
  and Ch06 (Infrastructure). Before this change, any gateway that wanted to route or
  rate-limit by MCP method/tool name had to parse the JSON-RPC body — deep packet
  inspection, which is expensive and fragile (the body schema can vary). Standard
  HTTP headers let existing HTTP-layer infrastructure (API gateways, WAFs, load
  balancers, `Mcp-Method`/`Mcp-Name`-aware rate limiters) do this without JSON
  parsing. The mirrored-header-vs-body integrity check (`-32020`) is a specific,
  citable detail: it prevents a client from spoofing the header to bypass gateway
  policy while sending a different actual method in the body — a real security
  property, not just a routing convenience.

### Claim 6: New `ttlMs` and `cacheScope` fields (SEP-2549) let clients cache tool/resource list responses, eliminating the need for a long-lived SSE connection just to monitor list changes

- **Evidence**: First-party spec description, framed as solving a specific prior
  pain point (long-lived SSE for change monitoring).
- **Confidence**: settled (direct description of a named spec section, SEP-2549)
- **Quote**: "To eliminate the need for long-lived Server-Sent Events (SSE)
  connections just to monitor if a tool or prompt list changed, the spec introduces
  caching fields modeled after HTTP's Cache-Control. Tool and resource results can
  now return a ttlMs (Time-to-Live in milliseconds) and a cacheScope."
- **Our assessment**: This closes a second stateful-connection requirement (the
  first being the session handshake) that previously forced MCP clients to hold an
  open SSE stream purely for change notification. Combined with Claim 2's removal
  of the handshake, this means an MCP client can now interact with a server using
  ordinary discrete HTTP request/response calls with no persistent connection at
  all — a meaningfully different operational profile from the original
  SSE-centric transport design.

### Claim 7: Multi Round-Trip Requests (MRTR, SEP-2322) handle server-to-client elicitation statelessly — the server returns an `InputRequiredResult` with an opaque `requestState` payload, and any server instance behind the load balancer can resume the retry

- **Evidence**: First-party spec description with a worked JSON example of the
  `InputRequiredResult` response (including a base64-encoded `requestState` blob)
  and an explicit statement of the resumability property.
- **Confidence**: emerging (this is presented as a new mechanism, SEP-2322, solving
  "one of the most complex challenges" the authors faced — a harder, newer design
  problem than the more mechanical header/caching changes, and thus less
  battle-tested)
- **Quote**: "Instead of blocking the thread or holding a connection open, the
  server immediately returns an InputRequiredResult with a requestState payload
  containing serialized context."
- **Quote (resumability)**: "The client prompts the user, gathers the boolean
  answer, and reissues the call with inputResponses and the echoed requestState.
  Because the requestState contains everything needed to resume the task, any
  server instance behind your load balancer can pick up the retry request!"
- **Our assessment**: This is the most architecturally interesting mechanism in the
  post because it solves a genuinely hard problem: how do you keep a
  human-in-the-loop confirmation step (e.g., "are you sure you want to delete these
  3 files?") stateless when the confirmation may arrive seconds or minutes later
  and land on a different server instance? The answer — push all resumption state
  into an opaque token the *client* carries and echoes back — is the same pattern
  used by stateless web session tokens (JWTs) and cursor-based pagination, applied
  here to elicitation. This is directly relevant to Ch03 (Safety and Verification):
  it is a protocol-level mechanism for confirmation gates on destructive tool calls
  that is compatible with horizontal scaling, extending the elicitation concept
  documented in `blog-anthropic-mcp-production-agents.md` Claim 8 with the specific
  stateless resumption mechanism that makes elicitation viable behind a load
  balancer.

### Claim 8: The Tasks Extension (SEP-2663) graduates from experimental to a first-class protocol feature, letting long-running tool calls (10-60 seconds) return a `taskId` immediately instead of blocking the client connection

- **Evidence**: First-party spec description with a worked TypeScript server example
  (an async refund-processing tool that stores initial task state, kicks off
  background work, and returns immediately) and named enterprise use cases (database
  backup, CRM sync, payment gateway refund).
- **Confidence**: settled for the mechanism (concrete code example and named
  `tasks/get`/`tasks/update` primitives); the "10 to 60 seconds" framing and
  enterprise use-case list are illustrative, not exhaustive
- **Quote**: "Sometimes a tool call simply takes a long time to run. A database
  backup, a CRM sync, or a refund through a payment gateway can take anywhere from
  10 to 60 seconds. Holding the client connection open blocks the customer
  conversation and creates massive connection queues."
- **Quote (mechanism)**: "The client continues the conversation, telling the user
  their request is processing, and can poll or subscribe using standard tasks/get
  and tasks/update primitives to monitor progress and fetch the final results."
- **Our assessment**: This is the enterprise-production-readiness claim of the
  article — it directly targets the class of MCP tool calls that wrap slow backend
  operations (payment processors, backup jobs, CRM syncs) where blocking the agent's
  turn for up to a minute is unacceptable UX. The pattern (return a task handle
  immediately, poll/subscribe for completion) is a standard async-job pattern
  applied to the MCP protocol level rather than left to each server's ad hoc
  implementation. For Ch06: this is the citable mechanism for "how do agents call
  slow tools without stalling the conversation," a gap not addressed by any prior
  MCP-focused source note in the corpus.

### Claim 9: The spec introduces a formal deprecation policy (SEP-2577) with a structured Active → Deprecated → Removed lifecycle and a minimum 12-month transition window; Roots, Sampling, and Logging enter deprecation immediately

- **Evidence**: First-party policy statement naming the specific features entering
  deprecation and their replacements.
- **Confidence**: settled (explicit policy statement with named affected features)
- **Quote**: "For the first time, MCP now has a formal deprecation policy. Features
  move through a structured Active -> Deprecated -> Removed lifecycle with a
  minimum 12-month transition window."
- **Quote (deprecated features)**: "Roots: Replaced by explicit tool parameters,
  resource URIs, or server configuration. Sampling: Replaced by calling LLM
  provider APIs directly. Logging: Replaced by standard stderr for stdio
  connections, or OpenTelemetry for structured cloud observability."
- **Our assessment**: The explicit 12-month minimum transition window is a
  practically important governance detail: it means practitioners with MCP servers
  or clients depending on Roots, Sampling, or Logging have a bounded, stated runway
  before those features are removed, rather than facing an undocumented breaking
  change. The Logging → OpenTelemetry replacement directly corroborates the
  observability direction already documented in `docs-ghaw-mcp-gateway-reference.md`
  Claim 9 (gateway-level OpenTelemetry integration with 10 OTLP compliance tests) —
  both sources converge on OpenTelemetry as the standard MCP observability substrate
  rather than protocol-native logging.

### Claim 10: The spec adds three security enhancements — Issuer Verification (RFC 9207), Resource Indicators (RFC 8707), and full JSON Schema 2020-12 for tool inputs — as state management shifts from transport to application layer

- **Evidence**: First-party security description naming the specific RFCs and the
  problems they solve.
- **Confidence**: settled (named, externally standardized RFCs — 9207 and 8707 are
  real IETF specifications independently defined outside this article, not
  MCP-invented mechanisms)
- **Quote**: "Issuer Verification (RFC 9207): Public clients must validate the iss
  parameter on authorization responses, protecting against session hijacking and
  redirect-based attacks in multi-server architectures."
- **Quote (confused deputy)**: "Resource Indicators (RFC 8707): Clients explicitly
  specify which MCP server a token is intended for, solving the "confused deputy"
  delegation problem."
- **Our assessment**: The framing — "As the responsibility of managing state shifts
  from the transport layer to the application layer, security becomes paramount" —
  is an explicit acknowledgment that statelessness is not a free lunch: removing
  server-side session pinning removes a passive isolation boundary, so the spec
  compensates with explicit token-scoping (Resource Indicators) and
  issuer-validation requirements. This is directly relevant to Ch03: the
  "confused deputy" problem (a client's token for server A being replayed against
  server B) is a real multi-server MCP risk that Resource Indicators specifically
  closes, and it is a new, more precise threat name for the corpus than the general
  auth-isolation framing in `blog-simonwillison-sean-lynch-mcp-auth-gateway.md`.

### Claim 11: All four Tier-1 MCP SDKs (Python, TypeScript, Go, C#) have beta releases for the 2026-07-28 spec; the TypeScript SDK splits the monolithic `@modelcontextprotocol/sdk` package into separate `server`/`client` packages with an automated codemod for common API renames

- **Evidence**: First-party migration guidance with exact package names and install
  commands.
- **Confidence**: settled (concrete, verifiable install commands and package names)
- **Quote**: "TypeScript v2 replaces the monolithic @modelcontextprotocol/sdk
  package with modular, focused libraries to keep your dependencies light."
- **Quote (codemod)**: "A convenient codemod is available to handle standard API
  renames (like renaming .tool() to registerTool)"
- **Our assessment**: The concrete migration tooling (a codemod, not just a
  changelog) signals Google/the working group anticipated this as a
  meaningfully disruptive breaking change for existing TypeScript MCP server code —
  consistent with Claim 2's assessment that this is a breaking protocol change
  requiring real client/server code updates, not a transparent wire-format tweak.
  For practitioners maintaining MCP servers today: the beta SDK availability across
  all four Tier-1 languages means migration can start in staging now, which is the
  article's explicit call to action ("We highly encourage you to start testing
  these in your staging environments today").

## Concrete Artifacts

### Legacy (2025-11-25) Stateful Handshake

```
// POST /mcp - Legacy 2025-11-25 Handshake
{
"jsonrpc": "2.0",
"id": 1,
"method": "initialize",
"params": {
"protocolVersion": "2025-11-25",
"capabilities": {},
"clientInfo": {
"name": "my-app",
"version": "1.0"
}
}
}
```
*Source: developers.googleblog.com, "Why Sessions Were a Production Bottleneck" section*

### New (2026-07-28) Stateless Tool Call

```
POST /mcp HTTP/1.1
Host: mcp-server.example
MCP-Protocol-Version: 2026-07-28
Mcp-Method: tools/call
Mcp-Name: search
Content-Type: application/json

{
"jsonrpc": "2.0",
"id": 1,
"method": "tools/call",
"params": {
"name": "search",
"arguments": {
"q": "otters"
},
"_meta": {
"io.modelcontextprotocol/protocolVersion": "2026-07-28",
"io.modelcontextprotocol/clientCapabilities": {},
"io.modelcontextprotocol/clientInfo": {
"name": "my-app",
"version": "1.0"
}
}
}
}
```
*Source: developers.googleblog.com, "The New Request Model: Going Fully Stateless" section*

### MRTR InputRequiredResult (Elicitation)

```
// InputRequiredResult Returned from Server
{
"resultType": "inputRequired",
"inputRequests": {
"confirm": {
"type": "elicitation",
"message": "Are you sure you want to delete these 3 files?",
"schema": {
"type": "boolean"
}
}
},
"requestState": "eyJzdGVwIjoxLCJmaWxlcyI6WyJhIiwiYiIsImMiXX0="
}
```
*Source: developers.googleblog.com, "Multi Round-Trip Requests (MRTR)" section*

### Tasks Extension Async Server Example (TypeScript)

```javascript
// Example: Kicking off an async task in a TypeScript server
server.tool(
"process_refund",
{ orderId: z.string(), amount: z.number() },
async ({ orderId, amount }) => {
const taskId = randomUUID();
// Store initial task state in a shared datastore (e.g. Redis)
await setTaskState(taskId, { status: "working" });
// Process the refund asynchronously in the background
processRefundAsync(taskId, orderId, amount);
// Return immediately to keep the conversation flowing
return {
content: [
{
type: "text",
text: JSON.stringify({
taskId,
status: "working",
message: `Refund of $${amount} for order ${orderId} is processing. Task ID: ${taskId}`
})
}
]
};
}
);
```
*Source: developers.googleblog.com, "The Tasks Extension (SEP-2663)" section*

### SDK Migration Commands

```
# Python (mcp v2 beta)
pip install "mcp[cli]==2.0.0b1"

# TypeScript v2 (split packages)
npm install @modelcontextprotocol/server@beta
npm install @modelcontextprotocol/client@beta

# TypeScript codemod for API renames (e.g. .tool() -> registerTool)
npx @modelcontextprotocol/codemod@beta v1-to-v2 .
```
*Source: developers.googleblog.com, "Getting Started and Migrating" section*

### Production Bottleneck Taxonomy (Legacy Session Model)

```
Named failure modes of the pre-2026-07-28 stateful session model:
Source: developers.googleblog.com, "Why Sessions Were a Production Bottleneck" section

- The Load Balancing Tax: round-robin balancers don't know which pod holds which
  session; second request from a client can hit the wrong pod -> 400 Session Not Found
- Sticky Routing Overheads: forces sticky session affinity config, preventing even
  traffic distribution and hurting autoscaling
- Zero Fault Tolerance: a pod restart/crash instantly loses session state, throwing
  transient errors to active client chats
- Complex Infrastructure Demands: remote MCP servers required shared Redis session
  stores or complex gateway-level packet inspection
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-mcp-gateway-reference.md` Claim 9 (gateway-level OpenTelemetry
    integration with 10 OTLP compliance tests): this source's deprecation of
    protocol-native Logging in favor of "OpenTelemetry for structured cloud
    observability" (Claim 9 here) independently converges on the same observability
    substrate gh-aw's gateway spec already implements. Two independent first-party
    sources now agree OpenTelemetry, not protocol-level logging, is the standard MCP
    observability layer.
  - `blog-simonwillison-sean-lynch-mcp-auth-gateway.md` Claim 1 (MCP's core value is
    isolating auth outside the agent's context/harness): this source's security
    section (Claim 10 — Issuer Verification, Resource Indicators) is the protocol-level
    machinery that makes that isolation trustworthy across multiple MCP servers
    specifically. Resource Indicators (RFC 8707) gives a concrete name — "confused
    deputy" — to exactly the multi-server credential-scoping risk that Lynch's more
    general observation gestures at.
  - `blog-anthropic-mcp-production-agents.md` Claim 8 (elicitation as a protocol-level
    human-approval mechanism for destructive tool calls): this source's MRTR
    mechanism (Claim 7) is the concrete stateless implementation of elicitation that
    Anthropic's post describes only at the conceptual level ("server pause[s]
    mid-tool call to ask the user for input"). This source adds the missing
    mechanism: how elicitation survives a load-balanced, session-less deployment.

- **Contradicts**: None identified in the corpus. Note: the same Google Developers
  Blog published a related post two days earlier — "Scaling real-time AI agents with
  session-aware load balancing" (Aug 3, 2026) — whose title superficially suggests
  tension with this post's stateless/session-free framing. Fetched and read in full:
  that post addresses a different problem domain entirely (bidirectional
  streaming/voice-agent infrastructure — gRPC/WebSocket sessions carrying live audio,
  transcripts, and tool calls in a continuous conversation) and explicitly argues for
  *session-aware* load balancing for that use case, distinct from MCP's discrete
  request/response tool-call protocol. This is a conditioning variable (continuous
  bidirectional streaming session vs. discrete stateless tool-call protocol), not a
  contradiction — the two posts describe different transport layers solving different
  problems, both published by Google in the same week. No contradiction issue filed.

- **Extends**:
  - `blog-anthropic-mcp-production-agents.md`: That post covers MCP server *design*
    (tool grouping, code orchestration, remote-vs-local server choice) from
    Anthropic's perspective. This source covers the underlying *protocol/transport*
    redesign from Google's perspective as a working-group co-founder. Together they
    give a fuller picture: design good servers (Anthropic post) on top of an
    infrastructure that now scales horizontally by default (this post).
  - `docs-ghaw-mcp-gateway-reference.md`: That spec documents gh-aw's own MCP gateway
    (a transparent proxy with guard policies, OIDC upstream auth, OTel tracing). This
    source documents the underlying MCP protocol-level changes (stateless core, HTTP
    header standardization) that a gateway like gh-aw's would sit in front of.
    SEP-2243's header-based routing (Claim 5) is directly relevant to how a gateway
    like gh-aw's could route/rate-limit without body inspection — the gh-aw gateway
    spec predates this MCP spec version and does not yet reference these headers, so
    this represents a potential future alignment point, not a documented one.
  - `blog-bswen-mcp-token-cost.md`: That note is about the *token* cost of loaded
    tool definitions in the client's context window — a client-side, per-session
    context-budget concern. This source is about *infrastructure* cost and scaling
    (server-side connection/session management) — a different layer of the MCP cost
    problem. The two are complementary, not overlapping: token cost lives in the
    context window; infrastructure cost lives in the deployment topology.

- **Novel**:
  - **Named, numbered SEPs for the stateless redesign**: SEP-2575 (handshake
    removal), SEP-2567 (session ID header removal), SEP-2243 (HTTP standardization),
    SEP-2549 (caching fields), SEP-2322 (MRTR/elicitation), SEP-2663 (Tasks
    Extension graduation), SEP-2577 (deprecation policy) — no prior corpus source
    names any of these specification enhancement proposals. This is the first
    protocol-spec-level documentation of the MCP transport redesign in the corpus.
  - **`-32020` header/body mismatch error code**: A specific, citable protocol
    integrity check preventing header spoofing at the gateway boundary — new to the
    corpus.
  - **Stateless elicitation via opaque `requestState` resumption tokens (MRTR)**: No
    prior source documents how MCP elicitation survives horizontal scaling; this is
    the first mechanism-level explanation in the corpus.
  - **Tasks Extension as a first-class async primitive** (`taskId`, `tasks/get`,
    `tasks/update`): No prior corpus source documents a standardized async/long-running
    tool call pattern at the MCP protocol level.
  - **Concrete Redis-removal production example (GitHub MCP Server)**: The first
    named, specific "before/after infrastructure" data point in the corpus for an
    MCP spec change, as opposed to a general architectural claim.
  - **MCP formal deprecation policy (12-month window)**: No prior source documents
    MCP's governance/versioning policy; this is new protocol-governance information.

## Guide Impact

- **Chapter 03 (Standards / Open protocols)**: Add the 2026-07-28 MCP spec release
  candidate as a major protocol milestone, citing the named SEPs (Claims 2, 5, 6, 7,
  8, 9, 10). Currently the guide's MCP coverage (via `docs-ghaw-mcps.md` and
  `blog-anthropic-mcp-production-agents.md`) documents the protocol as it existed
  under the 2025-11-25 session model; this source documents a breaking transport-level
  redesign that practitioners deploying or building MCP servers need to know about,
  including the 12-month deprecation runway for Roots, Sampling, and Logging (Claim 9).

- **Chapter 06 (Production patterns / Infrastructure)**: Add the stateless-core
  architecture (Claims 1-4) as the current recommended deployment model for
  production MCP servers: plain round-robin load balancing, serverless/scale-to-zero
  deployment (Cloud Run, Cloud Functions), and transparent failover, replacing the
  older guidance implicitly assuming sticky sessions or a shared Redis session store.
  Cite the GitHub MCP Server Redis-removal example (Claim 4) as concrete evidence.
  Add the Tasks Extension (Claim 8) as the recommended pattern for MCP tool calls
  wrapping slow backend operations (10-60+ second payment/backup/sync operations) —
  return a `taskId` immediately rather than holding the connection open.

- **Chapter 08 (Observability)**: Add SEP-2243's HTTP header standardization
  (`Mcp-Protocol-Version`, `Mcp-Method`, `Mcp-Name` — Claim 5) as the recommended
  mechanism for routing, rate-limiting, and auditing MCP traffic at the gateway
  layer without deep packet inspection. Cross-reference with
  `docs-ghaw-mcp-gateway-reference.md`'s existing OpenTelemetry integration as the
  two halves of an MCP observability stack: standard headers for gateway-layer
  routing/audit, OpenTelemetry for distributed tracing. Also note the Logging →
  OpenTelemetry deprecation (Claim 9) as further evidence that OTel is becoming the
  de facto MCP observability standard rather than protocol-native logging.

- **Chapter 03 (Safety and Verification)** (per Prospector's second triage comment):
  Add Multi Round-Trip Requests (Claim 7) as the stateless mechanism underlying
  protocol-level elicitation/confirmation gates for destructive tool calls,
  extending `blog-anthropic-mcp-production-agents.md` Claim 8's conceptual coverage
  with the concrete resumption mechanism. Add Resource Indicators (RFC 8707, Claim
  10) as the specific defense against the "confused deputy" risk in multi-MCP-server
  agent deployments — a token issued for server A must not be usable against server B.

## Extraction Notes

1. **Fetched raw HTML directly rather than via WebFetch summarization**: The
   Google Developers Blog page (`developers.googleblog.com`) was fetched via a
   direct HTTP request and its HTML tags stripped programmatically to produce
   plain text, rather than relying on WebFetch's AI-summarized rendering. This
   was done specifically to maximize verbatim quote fidelity per MINER.md §2a —
   all quotes in this note were copied character-for-character from the extracted
   plain text, not reconstructed from a summary. The full article text (~240
   lines) was read in its entirety before extraction began.

2. **Related post checked for contradiction, found to be a different domain**: The
   article's "Related Posts" section links to "Scaling real-time AI agents with
   session-aware load balancing" (Aug 3, 2026, same blog). Given the apparent
   tension in framing (session-aware vs. stateless), this related post was also
   fetched and read in full before concluding it addresses a different problem
   domain (bidirectional streaming/voice sessions) — see Cross-References →
   Contradicts. No contradiction issue filed; documented for future miners in case
   that post is separately triaged.

3. **Confidence grading rationale**: `confidence_overall` is set to `emerging`
   rather than `settled` because, while the mechanical/architectural claims
   (handshake removal, header standardization, deprecation policy) are settled
   descriptions of a published spec, the release itself is a release candidate
   (not final), published the day before this article, with only one named
   production adopter (GitHub MCP Server) and no independent practitioner
   validation yet in the corpus. Individual claims are graded settled or emerging
   per-claim based on how mechanical/verifiable vs. how new/untested each specific
   mechanism is.

4. **No sub-pages followed for spec/SDK details**: The article links to "the full
   2026-07-28 Specification," "the TypeScript SDK Upgrading Guide," and the Go SDK
   repository. These were not followed — the extraction is based on the announcement
   article's own description of the spec, which is sufficiently detailed (named SEPs,
   worked examples, error codes) for the claims extracted here. A deeper technical
   extraction of the formal spec document itself would be a candidate for a separate
   future source if the raw spec is submitted independently.
