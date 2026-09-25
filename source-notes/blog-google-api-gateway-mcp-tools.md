---
source_url: https://developers.googleblog.com/turn-your-rest-apis-into-mcp-tools-with-google-cloud-api-gateway/
source_type: blog-post
title: "Turn your REST APIs into MCP tools with Google Cloud API Gateway"
author: Sanjay Pujare, Paul Howell, Geir Sjurseth (Software Engineers / Product Manager)
date_published: 2026-09-24
date_extracted: 2026-09-25
last_checked: 2026-09-25
status: current
confidence_overall: settled
issue: "#3701"
---

# Turn your REST APIs into MCP tools with Google Cloud API Gateway

> Google Cloud API Gateway's MCP support (Public Preview, announced Sept 24,
> 2026) turns an already-deployed OpenAPI spec into a remote MCP server via
> two extension annotations (`x-google-api-management.mcp`,
> `x-google-mcp-tool`) — no separate MCP server to build, host, or maintain.
> The announcement blog post is thin; the two linked first-party docs pages
> disclose a long list of Public-Preview constraints (1,000-tool cap, no
> resources/prompts, no streaming, mutual exclusion with model routing) and
> at least one non-obvious configuration gotcha (configuring `tools/list`
> security silently globally enables MCP for every eligible operation)
> entirely absent from the blog post itself.

## Source Context

- **Type**: blog-post (Google Developers Blog, first-party Google Cloud
  product announcement) plus three linked first-party documentation pages —
  `cloud.google.com/api-gateway/docs/mcp-overview`,
  `.../docs/mcp-configure`, and the MCP-specific section of
  `.../docs/openapi-v3-limitations` — all dated "Last updated 2026-09-24
  UTC," i.e. published simultaneously with the blog post as one coordinated
  launch. The blog post is short (~900 words including code); the two
  MCP-specific docs pages are substantially longer and contain most of the
  concrete configuration, validation, and troubleshooting detail extracted
  below.
- **Author credibility**: First-party Google Cloud product announcement,
  co-authored by two named Software Engineers (Sanjay Pujare, Paul Howell)
  and a Product Manager (Geir Sjurseth). Authoritative for the feature's
  existence, annotation syntax, and stated Public Preview
  constraints/limitations. Not independently verified: no third-party
  practitioner account of using this Public Preview feature in production
  exists yet, so this note documents vendor-stated capability and
  vendor-disclosed limitation, not field-tested reliability or agent
  tool-selection accuracy in practice.
- **Scope**: Covers Google Cloud API Gateway's MCP support for exposing
  existing OpenAPI 3.x-described REST operations as remote MCP tools —
  annotation syntax, deployment, authentication model, argument-mapping
  mechanics, discovery via API Hub/Agent Registry, and Public Preview
  limitations. Does NOT cover: MCP Resources or Prompts (explicitly
  unsupported), streaming tool responses, non-Google/non-Cloud-Run backends
  in the worked examples, pricing for the MCP surface itself, or any GA
  timeline beyond "on the roadmap" language for resources/prompts,
  streaming, and Model Armor payload inspection.

## Extracted Claims

### Claim 1: Google Cloud API Gateway now offers remote MCP server support in Public Preview, transcoding an already-deployed OpenAPI spec's REST operations into agent-callable MCP tools with no separate server to build
- **Evidence**: Direct product announcement in the blog post's opening
  section, framed as closing a stated gap ("most enterprise capability sits
  behind REST APIs that agents cannot see").
- **Confidence**: settled (first-party, dated product-launch statement of a
  feature's existence and availability tier)
- **Quote**: "Google Cloud API Gateway now closes that gap. In Public
  Preview, API Gateway can act as a remote MCP server: annotate the OpenAPI
  spec you already deploy, deploy it, and your existing REST operations are
  available as agent-ready MCP tools — with no separate server to build,
  host, or maintain."
- **Our assessment**: This is the core claim the Prospector's triage
  comments flagged as high-novelty: a major cloud vendor now offers
  REST-to-MCP conversion as a managed, spec-annotation-driven gateway
  feature rather than requiring teams to hand-build and operate a
  standalone MCP server. "Public Preview" caveat should travel with any
  guide citation — pre-GA, typically without an SLA.

### Claim 2: Google explicitly positions this MCP feature as the companion, inbound-facing capability to API Gateway's separately-launched model routing feature, and distinguishes API Gateway (lightweight on-ramp) from Apigee (full enterprise platform) and Agent Gateway (outbound egress governance)
- **Evidence**: Direct positioning statement in the blog post's opening
  section, naming three sibling Google Cloud products by name.
- **Confidence**: settled (explicit first-party product-positioning
  statement)
- **Quote**: "API Gateway is the lightweight on-ramp in Google Cloud's
  gateway lineup. If you have a service on Cloud Run and you want its API
  secured, managed, and exposed to agents in minutes, this is the fast
  path. For a full enterprise API and MCP platform — lifecycle management,
  advanced traffic policies, monetization — use Apigee. To govern what your
  agents call on the way out, including MCP servers like this one, use
  Agent Gateway. Model routing, which gives you one stable endpoint for
  outbound LLM calls, is the companion capability for the other direction
  of AI traffic."
- **Our assessment**: This source explicitly, by name, links itself to
  `blog-google-api-gateway-model-routing.md` — MCP support is the *inbound*
  half (agents calling your APIs) to model routing's *outbound* half (your
  code calling LLM APIs), both riding the same API Gateway product. Notably,
  the two features were not launched together: model routing published
  2026-08-04, this MCP feature 2026-09-24 — about seven weeks apart, not a
  same-launch or back-to-back announcement, despite the "companion
  capability" framing implying a tightly coordinated product story. (See
  Extraction Notes for why this date gap matters for how this claim should
  be cited.)

### Claim 3: The gateway transcodes MCP JSON-RPC `tools/call` requests into the corresponding REST request in-flight, applying the operation's existing authentication, quota, and logging policies unchanged — MCP and REST traffic share exactly one policy path and one quota allocation per operation
- **Evidence**: Direct mechanism description in the blog post's "How it
  works" section.
- **Confidence**: settled (first-party architectural description of the
  core transcoding mechanism)
- **Quote**: "API Gateway accepts standard MCP JSON-RPC requests on a
  single endpoint, transcodes each tools/call into the corresponding REST
  request, applies your existing policies, and translates the response
  back. Because the transcoded request is indistinguishable from a normal
  REST call, the JWT or API-key authentication, quota, and logging you
  already configured for that operation keep working unchanged — MCP and
  REST traffic share exactly one policy path, and a given operation draws
  on one quota allocation however it is invoked."
- **Our assessment**: This is the headline operational benefit: no policy
  drift between an operation's REST and MCP-tool identities, because they
  are the same backend call under the hood. It also means MCP exposure adds
  zero new places to configure auth/quota/logging — a meaningful
  operational-simplicity claim, though untested at scale by any third
  party in this corpus yet.

### Claim 4: MCP support requires OpenAPI 3.0.x or 3.1.x (not 2.0), opted in at the document level via `x-google-api-management.mcp` and customized per-operation via `x-google-mcp-tool`; every exposed operation needs a configured backend and a non-empty description
- **Evidence**: Step-by-step annotation instructions in the blog post's
  "Annotate your OpenAPI spec" section, plus a full worked OpenAPI 3.0.4
  YAML example (Concrete Artifacts).
- **Confidence**: settled (concrete, executable configuration syntax
  reproduced identically across the blog post and both docs pages)
- **Quote**: "MCP requires OpenAPI 3.0.x or 3.1.x; OpenAPI 2.0 is not
  supported, so if your gateway still runs a 2.0 spec, migrate it first.
  Opt in at the document level with x-google-api-management.mcp, and
  customize or skip individual operations with x-google-mcp-tool. Each
  exposed operation needs a backend and a non-empty description."
- **Our assessment**: The OpenAPI-3.x-only requirement is a concrete
  migration prerequisite for any team still on a 2.0 spec — the blog post
  itself flags this and links a migration guide, so it is not a hidden
  gotcha, unlike several limitations below that appear only in the docs
  pages.

### Claim 5: A tool's description is the primary signal an LLM uses to decide when to call it, so the description should state when and why to use the tool, not merely what it returns
- **Evidence**: Direct authorial guidance immediately following the worked
  OpenAPI annotation example in the blog post.
- **Confidence**: emerging (a design-practice recommendation stated as
  fact but without a benchmark or citation in this source)
- **Quote**: "A tool's description is the primary signal an LLM uses to
  decide when to call it, so write when and why to use the tool, not just
  what it returns."
- **Our assessment**: This is a specific, actionable tool-description
  design principle — write for agent tool-selection, not for a human API
  reference — but it is asserted without evidence in this source (no
  benchmark comparing description styles). It is directionally consistent
  with the broader "design for tool selection, not just correctness"
  concern that motivates the tool-sprawl caution in
  `blog-fowler-sadalage-chandrasekaran-ai-ready-data.md` Claim 13, but this
  source does not itself address tool *count* or *sprawl* — only
  description *quality* for a single tool.

### Claim 6: The `tools/list` discovery method defaults to unauthenticated (publishing tool names and input schemas to anyone who can reach the gateway); production deployments should require JWT, and API keys cannot secure this specific method at all
- **Evidence**: Explicit security guidance in the blog post's "Decide who
  can discover your tools" step, corroborated by the docs configure page's
  "Authentication restrictions" limitation and "Tool Discovery" bullet.
- **Confidence**: settled (explicit, first-party disclosed default
  behavior plus a named security best-practice recommendation, repeated
  identically across the blog post and both docs pages)
- **Quote**: "By default tools/list is unauthenticated, which is
  convenient for development but publishes your tool names and input
  schemas to anyone who asks. For production, require a JWT — note that
  API keys cannot secure this method." (blog); "as a security best
  practice, it is strongly recommended to protect tool discovery by
  enabling authentication for this method using tools-list.security. If
  you choose to enable authentication, you must use a JWT security scheme.
  API key authentication is not supported for tools/list." (docs configure
  page)
- **Our assessment**: This is a genuine, disclosed default-insecure
  posture worth flagging prominently: an unauthenticated `tools/list`
  endpoint is a schema/tool-name information-disclosure surface by design
  in dev mode, and the fix (JWT) is narrower than a team might assume —
  API keys, otherwise usable for `tools/call` and ordinary REST auth on
  this same gateway, are explicitly excluded for securing discovery.

### Claim 7: `tools/call` always enforces whatever authentication the underlying REST operation already requires, independently of whatever (or no) security is configured on `tools/list`
- **Evidence**: Direct statement in the blog post immediately following the
  `tools/list` security guidance, corroborated by the docs configure page's
  "Tool Invocation" authentication-model bullet.
- **Confidence**: settled (explicit, first-party stated authentication
  model, repeated identically across sources)
- **Quote**: "tools/call always enforces whatever authentication the
  underlying REST operation requires, whether or not you secure
  discovery." (blog); "Tool Invocation (tools/call): Reuses the
  authentication policies defined for the underlying operation in your
  OpenAPI specification. It enforces the same API key or JWT requirements
  as calling the REST endpoint directly." (docs configure page)
- **Our assessment**: Read together with Claim 6, this means an operator
  can leave `tools/list` open in dev (cheap iteration, tool names visible)
  while every actual invocation still requires whatever auth the REST
  operation already demands — discovery and invocation are independently
  gated. A team that assumes "MCP is closed because my REST API requires a
  token" is correct about `tools/call` but should not assume the same
  about `tools/list` unless they explicitly configured it (Claim 6).

### Claim 8: An MCP-enabled gateway connected to API Hub is automatically published there as an MCP server with MCP-specific metadata and also appears in Agent Registry, with no separate registration step
- **Evidence**: Explicit statement in the docs overview page's "Discovery
  through API Hub and Agent Registry" section, restated more briefly in
  the blog post's "Why serve MCP from the gateway" section.
- **Confidence**: settled (explicit first-party stated discoverability
  behavior)
- **Quote**: "If you integrate your gateway with API hub, your MCP-enabled
  gateway is published to API hub as an MCP server with additional
  MCP-specific metadata, and it also appears in Agent Registry
  automatically... No separate registration step is needed. Agents can
  then discover the server and its tools through either catalog."
- **Our assessment**: This is a concrete "nothing new to operate" benefit
  distinct from the transcoding mechanism itself (Claim 3): turning on MCP
  changes what API Hub publishes about an existing, already-cataloged
  gateway rather than requiring a net-new registration workflow. The docs
  page notes non-MCP-enabled gateways publish only standard API metadata,
  so this MCP-specific discovery layer is additive, gated strictly behind
  the `x-google-api-management.mcp` opt-in.

### Claim 9: During Public Preview, API Gateway supports only four MCP lifecycle methods (`initialize`, `notifications/initialized`, `tools/list`, `tools/call`); every other MCP method — including `resources/*`, `prompts/*`, `sampling/*`, `completion/*`, `ping`, and `logging/*` — is unsupported and returns JSON-RPC error code `-32601`
- **Evidence**: Explicit "Supported MCP lifecycle methods" list and "Note"
  callout in the docs overview page, with the fuller method list given in
  the "Unsupported MCP methods" bullet on the openapi-v3-limitations page.
- **Confidence**: settled (explicit, first-party enumerated protocol
  support scope, consistent across both docs pages)
- **Quote**: "Supported MCP lifecycle methods: initialize: Establishes
  protocol version and capabilities. notifications/initialized:
  Acknowledges the handshake. tools/list: Allows clients to discover
  available tools and their schemas. tools/call: Allows clients to invoke
  a tool with arguments. Note: All other MCP methods (such as resources/*
  or prompts/*) are not supported and return a JSON-RPC error code
  -32601." (docs overview page)
- **Our assessment**: This scopes the feature precisely: it implements
  only the tool-calling half of MCP, not the full protocol surface (no
  Resources, no Prompts, no sampling delegation, no logging notifications).
  Any guide mention of this feature should describe it as "MCP tool
  exposure for REST APIs," not "a full MCP server," to avoid overstating
  protocol coverage.

### Claim 10: Public Preview imposes a hard cap of 1,000 MCP tools per gateway, restricts exposable operations to GET/POST/PUT/PATCH/DELETE (no HEAD/OPTIONS/TRACE), is fully stateless (no `MCP-Session-Id` tracking), rejects JSON-RPC batch requests, supports only UTF-8 text responses (no binary), does not emit `destructiveHint`/`readOnlyHint` tool annotations, does not expose operations with empty (e.g. HTTP 204) response bodies, and cannot be enabled in the same API config as model routing
- **Evidence**: The "MCP limitations" section of the
  openapi-v3-limitations docs page, itself an enumerated bullet list of
  named constraints, cross-confirmed for the tool-count cap and the model
  routing exclusion by the docs overview and configure pages and the blog
  post's own "roadmap" paragraph.
- **Confidence**: settled (explicit, first-party enumerated Public Preview
  constraint list)
- **Quote**: "Tool count limit: Customers are limited to a maximum of
  1,000 MCP tools per Gateway." / "Statelessness: The implementation is
  stateless; session identifiers (like MCP-Session-Id) are not used or
  maintained." / "Model Routing Mutual Exclusion: You cannot use both MCP
  and Model Routing within the same API configuration." / "Multi-modal
  payloads: Tool responses are limited to UTF-8 text. Binary responses are
  not supported." / "No tool annotations: Hints such as destructiveHint or
  readOnlyHint are not emitted in tool declarations."
- **Our assessment**: The most consequential of these for guide readers is
  the mutual exclusion with model routing within one API config (a team
  cannot use a single gateway config to both expose REST-as-MCP-tools and
  route outbound model calls — they need two separate gateway
  configs/instances for the two halves of Claim 2's "companion
  capability" story) and the missing `destructiveHint`/`readOnlyHint`
  annotations, which are exactly the MCP-spec-native signals an agent
  harness would otherwise use to gate write/irreversible actions behind
  extra confirmation — their absence here means any such gating must be
  built by the calling agent framework, not inferred from this gateway's
  tool declarations.

### Claim 11: Protocol and application-level MCP errors are deliberately returned as HTTP 200 responses carrying a JSON-RPC error object, rather than a non-200 HTTP status, specifically because non-200 responses cause many MCP clients to fail at the transport layer; transport-layer failures (malformed JSON, wrong HTTP method, oversized body, auth failure) do use non-200 HTTP statuses
- **Evidence**: Explicit design statement plus a nine-row troubleshooting
  table in the docs configure page's "Troubleshooting MCP failures"
  section (Concrete Artifacts).
- **Confidence**: settled (explicit first-party stated design rationale
  and enumerated error taxonomy)
- **Quote**: "MCP distinguishes between transport failures and protocol
  failures. The gateway returns HTTP 200 with a JSON-RPC error object for
  protocol and application errors, as non-200 responses can cause many MCP
  clients to fail at the transport layer."
- **Our assessment**: This is an important operational-monitoring nuance:
  a naive alert or log filter keyed only on non-2xx HTTP status will miss
  most MCP-layer failures (unknown tool, invalid arguments, unsupported
  method, backend application error) entirely, since the gateway
  intentionally wraps them in a 200 response. Teams operating this gateway
  need to inspect the JSON-RPC `error` field (or `result.isError: true`
  for backend application errors) as a first-class signal, not just HTTP
  status codes — a distinct diagnostic taxonomy from the four-category
  HTTP-status-keyed error taxonomy documented for the sibling model
  routing feature in `blog-google-api-gateway-model-routing.md` Claim 11.

### Claim 12: Tool arguments are mapped onto the REST request by convention — path and query parameters become top-level properties of the `arguments` object, the request body is nested under a single `body` property, and headers also become top-level properties (except reserved system headers and any header prefixed `x-google-`) — making the transcoded backend request indistinguishable from a direct REST call
- **Evidence**: Explicit "How arguments map to the REST request" section
  in the docs configure page, including a worked example of the `body`
  nesting convention.
- **Confidence**: settled (explicit, first-party stated request-mapping
  convention)
- **Quote**: "Path and query parameters: Become top-level properties in
  the arguments object, keyed by their OpenAPI parameter names. Request
  body: Nested under a single property named body. For example, to create
  a resource, you pass {"body": {"fieldName": "value"}}... The transcoded
  backend request is indistinguishable from a direct REST request to your
  backend service. Backend services cannot programmatically distinguish
  between a direct REST call and one transcoded from MCP."
- **Our assessment**: This is the concrete implementation detail any team
  building or debugging an MCP tool call against this gateway needs: the
  `body` key nesting convention is not obvious from the OpenAPI spec alone
  and is a plausible first-integration error source (the docs
  troubleshooting table's "Invalid tool arguments" row explicitly names
  "Verify the body key nesting" as the typical fix). The backend-blindness
  property (a REST handler cannot tell whether a request came via MCP or
  direct REST) is also a security-relevant fact: any REST-side
  authorization logic keyed on request origin, rather than the
  already-enforced gateway-level auth, would not distinguish the two
  paths.

### Claim 13: Configuration validation enforces specific rules at spec-upload time — tool names must match `[A-Za-z0-9_.-]{1,128}` and be unique across the spec, only GET/POST/PUT/PATCH/DELETE operations are eligible, and every exposed operation must resolve to a non-empty description (from its description, summary, or an explicit override) or the operation is rejected outright
- **Evidence**: Explicit "Configuration validation" bullet list in the
  docs configure page ("Location," "HTTP Method," "Tool Name,"
  "Description," "Security" sub-bullets).
- **Confidence**: settled (explicit, first-party stated validation rules
  applied at spec-upload time)
- **Quote**: "Tool Name: Tool names must match [A-Za-z0-9_.-]{1,128} and be
  unique across the specification." / "Description: Every tool must
  resolve to a non-empty description (taken from the operation's
  description, summary, or override). Operations without a resolvable
  description are rejected."
- **Our assessment**: The description requirement is notable because it is
  enforced, not merely recommended — an operation with no description,
  summary, or override cannot be exposed as an MCP tool at all, which
  gives Claim 5's "write when and why" guidance real teeth: a spec author
  cannot skip the description field and still get the operation exposed.

### Claim 14: Configuring the `mcp` extension as an object at the document level — for example, solely to set `tools-list.security` — implicitly and globally enables MCP for every eligible operation in the spec; a team that wants `tools/list` authentication configured without exposing every eligible operation must explicitly opt out each unwanted operation with `x-google-mcp-tool: false`
- **Evidence**: An explicit "Note" callout in the docs configure page's
  step 3 ("Authenticate tools/list (Recommended)"), directly following the
  worked `tools-list.security` YAML example.
- **Confidence**: settled (explicit, first-party disclosed configuration
  side-effect, stated as a distinct warning rather than inferred)
- **Quote**: "Configuring the mcp extension as an object (for example, to
  enable authentication for tools/list) also enables MCP globally for all
  eligible operations. If you want to configure tools/list security but
  don't want to expose all eligible operations, you must explicitly
  opt-out those operations by setting x-google-mcp-tool: false."
- **Our assessment**: This is a genuine, easy-to-miss configuration
  gotcha: an operator who only intends to lock down tool *discovery*
  behind a JWT (a security-hardening step) simultaneously and silently
  broadens tool *exposure* to every eligible operation in the spec, unless
  they separately curate the exposed set. Combined with the 1,000-tool
  cap (Claim 10) and no built-in warning against broad exposure, this is
  the specific mechanism by which a well-intentioned security change could
  produce exactly the wide, undifferentiated tool surface that
  `blog-fowler-sadalage-chandrasekaran-ai-ready-data.md` Claim 13 warns
  degrades agent tool-selection accuracy (see Cross-References →
  Contradicts).

## Concrete Artifacts

### Document- and operation-level OpenAPI 3.x MCP annotation (verbatim, from the blog post)
```yaml
Source: developers.googleblog.com/turn-your-rest-apis-into-mcp-tools-with-google-cloud-api-gateway/

openapi: 3.0.4
info:
  title: Order Service
  version: 1.0.0
x-google-api-management:
  mcp: true                 # expose this spec's operations as MCP tools
  backends:
    orders-backend:
      address: https://orders-a1b2c3-uc.a.run.app
paths:
  /orders/{orderId}:
    get:
      operationId: getOrderStatus
      description: Returns the current status, carrier, and ETA for an order.
      x-google-backend: orders-backend
      x-google-mcp-tool:
        name: get_order_status
        description: "Look up the delivery status and ETA of a customer order.
          Use this when the user asks where an order is or when it will arrive."
      parameters:
        - name: orderId
          in: path
          required: true
          schema:
            type: string
```

### `tools/list` JWT-security annotation (verbatim, from the blog post)
```yaml
Source: developers.googleblog.com/turn-your-rest-apis-into-mcp-tools-with-google-cloud-api-gateway/

x-google-api-management:
  mcp:
    tools-list:
      security:
        orderServiceJwt: []   # the object form also enables MCP globally
```

### ADK agent integration (verbatim, from the blog post)
```python
Source: developers.googleblog.com/turn-your-rest-apis-into-mcp-tools-with-google-cloud-api-gateway/

from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset, StreamableHTTPConnectionParams

order_tools = McpToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="https://my-gateway-a12bcd345e67f89g0h.uc.gateway.dev/mcp",
        headers={"x-api-key": API_KEY},
    )
)

agent = Agent(
    model="gemini-2.5-flash",
    name="order_support_agent",
    instruction="Help the user check on their orders.",
    tools=[order_tools],
)
```

### `tools/call` request and response over the wire (verbatim, from the blog post)
```shell
Source: developers.googleblog.com/turn-your-rest-apis-into-mcp-tools-with-google-cloud-api-gateway/

curl -X POST "https://my-gateway-a12bcd345e67f89g0h.uc.gateway.dev/mcp" \
  -H "content-type: application/json" \
  -H "MCP-Protocol-Version: 2025-11-25" \
  -H "x-api-key: $API_KEY" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call",
       "params":{"name":"get_order_status","arguments":{"orderId":"A-1042"}}}'
```
```json
{"jsonrpc":"2.0","id":1,"result":{"content":[{"type":"text",
 "text":"{\"orderId\":\"A-1042\",\"status\":\"IN_TRANSIT\",\"eta\":\"2026-09-24\"}"}],
 "isError":false}}
```

### Global vs. per-operation enablement (verbatim, from the docs configure page)
```yaml
Source: cloud.google.com/api-gateway/docs/mcp-configure, "2. Update your OpenAPI specification"

# Global enablement
openapi: 3.0.3
info:
  title: Bookstore API
  version: 1.0.0
x-google-api-management:
  mcp: true
  backends:
    bookstore-backend:
      address: https://bookstore-backend-12345678.us-central1.run.app

# Per-operation override / opt-out
paths:
  /v1/shelves/{shelf}:
    delete:
      operationId: deleteShelf
      summary: Delete a shelf.
      x-google-backend: bookstore-backend
      x-google-mcp-tool:
        name: delete_shelf
        description: "Permanently delete a shelf and every book on it."
# An operation can be excluded from global enablement with:
#   x-google-mcp-tool: false
```

### MCP failure troubleshooting table (verbatim, from the docs configure page)
```
Source: cloud.google.com/api-gateway/docs/mcp-configure, "Troubleshooting MCP failures"

Symptom                         | JSON-RPC Code | HTTP Status | Meaning / Typical Fix
Method Not Allowed               | n/a            | 405         | A non-POST request reached /mcp. Only HTTP POST is supported.
JSON parse error                 | -32700         | 400         | The request body is not valid JSON.
Missing/Invalid Method or ID     | -32600         | 200         | Body is valid JSON but not a valid JSON-RPC request. Check jsonrpc/method/id fields.
Method is not supported          | -32601         | 200         | The method is outside the supported scope (e.g., ping).
Unsupported protocol version     | -32602         | 200         | The protocolVersion names a version the gateway does not support.
Missing Protocol Version         | -32602         | 200         | The initialize params omit protocolVersion or it is not a string.
Unknown tool                     | -32602         | 200         | Tool name not found. Clean client cache or verify deployment.
Invalid tool arguments           | -32602         | 200         | Arguments are missing or invalid. Verify the body key nesting.
Body too large                   | -32000         | 200         | The response payload exceeded size limits.
Transport body too large         | n/a            | 413         | The raw HTTP request body exceeded gateway transport limits.
Server error                     | -32000         | 200         | Unparseable backend response. Check logs.
Unauthorized / Forbidden         | n/a            | 401 / 403   | Authentication failure. Response carries a WWW-Authenticate header.

Backend application errors typically surface as a successful JSON-RPC response (HTTP 200)
with result.isError: true containing the backend error body.
```

### MCP limitations list (verbatim, from openapi-v3-limitations docs page, "MCP limitations")
```
Source: cloud.google.com/api-gateway/docs/openapi-v3-limitations

Tool count limit: Customers are limited to a maximum of 1,000 MCP tools per Gateway.
HTTP methods: Only GET, POST, PUT, PATCH, and DELETE operations can be exposed as MCP
  tools. HEAD, OPTIONS, and TRACE are not supported.
Streaming: Server-Sent Events (SSE) streaming of long-running tool calls is not supported.
Batch requests: JSON-RPC batch arrays are rejected.
Multi-modal payloads: Tool responses are limited to UTF-8 text. Binary responses are not
  supported.
Statelessness: The implementation is stateless; session identifiers (like MCP-Session-Id)
  are not used or maintained.
Unsupported MCP methods: Specialized methods such as resources/*, prompts/*, sampling/*,
  completion/*, ping, and logging/* are not supported and return a JSON-RPC error code
  -32601.
Authentication restrictions: The tools/list method supports JWT authentication only. API
  key authentication is not supported for this method.
No tool annotations: Hints such as destructiveHint or readOnlyHint are not emitted in
  tool declarations.
CORS Preflight: Automated CORS preflight handling (OPTIONS requests) on the /mcp path is
  not managed by the gateway.
Model Routing Mutual Exclusion: You cannot use both MCP and Model Routing within the same
  API configuration.
Unsupported MCP responses: Operations that return empty bodies in the response, such as
  HTTP 204 responses, are not supported.
Schema Discovery: Complex nested object schemas derived from your OpenAPI specification
  may not render fully or correctly in the tools/list discovery response due to a known
  configuration processing limitation.
```

## Cross-References

### Cross-reference verification notes
`blog-google-api-gateway-model-routing.md`,
`blog-fowler-sadalage-chandrasekaran-ai-ready-data.md`,
`blog-google-speakeasy-sdk-generation-open-source.md`, and
`blog-latentspace-ainews-amd-buys-taalas.md` were each re-read directly
(MINER.md §4b) and every claim number cited below was confirmed against
that note's numbered `### Claim N:` headings in document order before
writing this section.

- **Corroborates**:
  - `blog-latentspace-ainews-amd-buys-taalas.md` Claim 8 (Weaviate added a
    built-in `/v1/mcp` endpoint on the same port as its REST API, framed
    as "MCP is moving from novelty to table stakes"): this source is
    independent corroboration of the same trend from a second
    infrastructure vendor — Google Cloud API Gateway now offers the same
    "native MCP surface on your existing gateway/API, no separate MCP
    service" pattern Weaviate shipped, via a different mechanism
    (OpenAPI-spec annotation and gateway-level JSON-RPC-to-REST
    transcoding, vs. Weaviate's built-in endpoint on its own database
    product). Neither source references the other; this strengthens the
    "MCP as commodity infrastructure feature, not novelty" reading across
    two unrelated vendors in the same quarter.

- **Contradicts**: No formal contradiction filed. One design-level tension
  is worth flagging prominently per MINER.md §4a's "conditioning
  variable, not a contradiction" guidance, since this source makes no
  normative claim that directly opposes Fowler et al.'s — it is a feature
  description, not a best-practice recommendation:
  `blog-fowler-sadalage-chandrasekaran-ai-ready-data.md` Claim 13 warns
  that naively wrapping REST APIs 1:1 into MCP tools ("tool sprawl," the
  Thoughtworks Technology Radar's basis for putting "naive API-to-MCP
  conversion" on Hold) degrades agent tool-selection accuracy, and
  recommends 5-10 curated business capabilities over dozens of thin
  wrappers. This source's default "Global enablement" behavior (Concrete
  Artifacts) does exactly the 1:1 operation-to-tool mapping Fowler's
  source warns against, capped only at 1,000 tools per gateway (Claim
  10) — two orders of magnitude above the "50 tools" example Fowler's
  source cites as already degrading accuracy — and Claim 14 documents a
  specific mechanism by which a team intending only a security change
  (adding `tools-list` JWT auth) silently triggers this same broad,
  uncurated exposure. Neither the blog post nor either docs page mentions
  tool-selection accuracy, tool count as a design concern, or the
  Thoughtworks critique at all. This is not filed as a formal
  contradiction issue because the two sources are not making opposing
  factual claims about the same mechanism — Fowler's source is
  prescriptive best-practice guidance, this source is a feature/default
  description with an available (if easy-to-miss) opt-out mechanism
  (`x-google-mcp-tool: false`) — but the tension is real and directly
  actionable for guide readers: anyone following this source's "Global
  enablement" quick-start path without also reading Fowler's capability-
  design guidance will likely reproduce the exact anti-pattern Thoughtworks
  flagged.

- **Extends**:
  - `blog-google-api-gateway-model-routing.md`: this source is the
    explicitly-named "companion capability" (Claim 2) to that note's
    subject — model routing handles outbound LLM traffic through API
    Gateway, this MCP feature handles inbound agent-tool-call traffic
    through the same product. Claim 10's mutual-exclusion finding (MCP and
    model routing cannot share one API config) is a new, specific
    constraint on how these two "companion" features actually compose:
    they require separate gateway configs/instances, not one unified
    config, despite the blog's framing of them as two directions of one
    product. This source also repeats a pattern that note's Extraction
    Notes flagged explicitly: the announcement blog post is thin and
    omits most disclosed limitations, defects, and operational detail,
    which live almost entirely in the linked, same-day-dated
    documentation pages — this is now a second observed instance of the
    same editorial pattern in Google Cloud API Gateway's launch blog
    posts specifically, worth watching for in any future Miner extraction
    of a Google Cloud API Gateway announcement.
  - `blog-google-speakeasy-sdk-generation-open-source.md` Claim 9 (Google's
    open-sourced Speakeasy-based generator includes a "documentation MCP
    server generator" that compiles an OpenAPI spec and markdown docs into
    a standalone MCP server binary, so agents "query live, verified
    schemas instead of guessing outdated methods"): both sources solve the
    same stated problem — turning an OpenAPI spec into agent-callable MCP
    tools without hand-building an MCP server — via architecturally
    opposite mechanisms. Speakeasy's tool is a compile-time code
    generator that produces a standalone, deployable MCP server artifact;
    this source is a runtime gateway proxy with no generated server
    artifact at all — the OpenAPI spec is annotated and deployed as-is,
    and the gateway transcodes MCP requests to REST live, on every
    request. Neither source references the other. The guide should
    present these as two distinct, non-interchangeable patterns for the
    same goal: "generate a standalone MCP server from your spec" vs.
    "annotate your existing gateway to speak MCP over your existing REST
    deployment," with different operational tradeoffs (a generated server
    is a new deployable artifact to version and redeploy on spec changes;
    a gateway-annotation approach has no separate artifact, but is locked
    to whatever gateway product implements the transcoding).

- **Novel**:
  - The JSON-RPC `tools/call`-to-REST live transcoding architecture itself
    (Claim 3), with the explicit "one policy path, one quota allocation"
    design property — no other source in this corpus documents a gateway
    that transcodes MCP protocol calls into REST calls in-flight against
    an unmodified backend.
  - The deliberate HTTP-200-wraps-JSON-RPC-errors design choice and its
    stated rationale (many MCP clients fail at the transport layer on
    non-200) (Claim 11) — a concrete, MCP-specific operational-monitoring
    nuance not present elsewhere in this corpus's gateway/routing
    coverage.
  - The `arguments` → path/query/body/headers mapping convention,
    including the single-`body`-key nesting rule (Claim 12) — new,
    concrete implementation detail for any team debugging MCP tool calls
    against an OpenAPI-backed gateway.
  - The implicit-global-enablement configuration gotcha (Claim 14) and its
    direct tension with this corpus's existing tool-sprawl caution (see
    Contradicts) — new to this corpus's MCP-configuration coverage.
  - The absence of `destructiveHint`/`readOnlyHint` tool annotations
    (part of Claim 10) as a named, disclosed gap — relevant to any guide
    discussion of how agent harnesses gate potentially destructive tool
    calls, since this gateway's tool declarations cannot supply that
    signal even though the underlying MCP spec defines it.

## Guide Impact

- **Chapter 02/03 (Harness Engineering / Tool Integration)**: Add Google
  Cloud API Gateway's MCP support as a second, architecturally distinct
  entry in the "OpenAPI-spec-to-MCP-tools without hand-building a server"
  pattern family, alongside the existing Speakeasy-generator coverage
  (Claim 1, Claim 4). Make the mechanism difference explicit: generated
  standalone server (Speakeasy) vs. live gateway transcoding (this
  source) — different operational tradeoffs, not competing claims about
  the same thing.

- **Chapter 02/03 (Harness Engineering / Tool Integration)**: Flag Claim 14
  (configuring `tools-list` security silently globally enables MCP for
  every eligible operation) as a specific configuration caution, cited
  alongside `blog-fowler-sadalage-chandrasekaran-ai-ready-data.md` Claim
  13's tool-sprawl warning — a team using this gateway's quick-start path
  should be told explicitly to curate exposed operations with
  `x-google-mcp-tool: false` rather than rely on the 1,000-tool cap as a
  sufficient guardrail.

- **Chapter 04 (Observability & Reliability)**: Add Claim 11 (protocol/app
  errors return HTTP 200 with a JSON-RPC error object, not a non-200
  status) as a specific monitoring caution: alerting or log filtering
  keyed only on HTTP status codes will miss most MCP-layer failures for
  gateways using this feature; teams must also inspect the JSON-RPC
  `error` field and `result.isError`.

- **Chapter 05 (Security & Governance)** (or equivalent): Add Claim 6 (
  `tools/list` defaults to unauthenticated, discloses tool names/schemas,
  and cannot be secured with API keys — only JWT) as a specific
  production-readiness checklist item, and Claim 10's missing
  `destructiveHint`/`readOnlyHint` tool annotations as a gap any agent
  harness relying on those MCP-spec hints for write-action gating must
  compensate for independently when consuming tools from this gateway.

## Extraction Notes

- **WebFetch's summarizing pass was not used for quotes**, per MINER.md
  §2a. An initial WebFetch call against the blog post returned a
  compressed, paraphrased summary (collapsing exact sentences, renaming
  the third author, omitting the "companion capability" / Apigee / Agent
  Gateway positioning paragraph entirely, and misreporting several
  concrete details — e.g. it said the JWT security example showed
  `orderServiceJwt: []` as a bare snippet with no surrounding config,
  and it omitted the `tools/call` always-enforces-existing-auth statement
  and the entire "How arguments map to the REST request" mechanics). The
  blog post and all three linked docs pages/sections were instead
  retrieved via direct `curl` with a browser user-agent, HTML
  `<script>`/`<style>` blocks stripped, tags removed with a Python
  regex-based stripper, and HTML entities decoded. Every `Quote` field
  above, and every artifact in Concrete Artifacts, was taken from that
  raw-HTML-derived plain text.
- **Three linked docs pages/sections were followed**, per MINER.md §1's
  "follow up to 5 linked pages" guidance: the blog post links directly to
  `cloud.google.com/api-gateway/docs/mcp-overview`, which itself links to
  `.../docs/mcp-configure` ("What's next" section); both link to
  `.../docs/openapi-v3-limitations`, whose "MCP limitations" section (an
  anchor target, `#mcp-limitations`, referenced directly from the blog
  post's roadmap paragraph) was also fetched and extracted. All three are
  dated "Last updated 2026-09-24 UTC," the same day as the blog post,
  confirming they are the authoritative, simultaneously-published
  technical reference for this launch. The `OpenAPI 3.x extensions`
  reference page (linked from multiple "What's next" sections) was not
  followed — it documents general OpenAPI extension syntax unrelated
  specifically to MCP and was judged out of scope for this issue.
- **The blog post itself is thin (~900 words including three code
  examples) and its unique contribution, not restated in the docs pages,
  is limited to Claims 1, 2, 3 (partially), 5, and 8 (partially).** The
  substantial majority of the extracted claims (4's OpenAPI-version
  requirement detail, 6, 7, 9, 10, 11, 12, 13, 14) come from the two
  MCP-specific documentation pages, which disclose validation rules,
  limitations, and a detailed troubleshooting taxonomy the announcement
  post omits entirely — the same pattern already observed and flagged in
  `blog-google-api-gateway-model-routing.md`'s Extraction Notes for
  Google Cloud API Gateway's earlier model-routing launch. This is
  flagged explicitly so the Assayer weighs the docs-page claims as
  equally authoritative as the blog-post claims, since both are
  first-party Google Cloud content published the same day.
- **Prospector triage-comment inaccuracy not carried forward**: one of the
  three Prospector triage comments on issue #3701 described this feature
  as announced "the day after model routing." Direct verification against
  `blog-google-api-gateway-model-routing.md`'s frontmatter
  (`date_published: 2026-08-04`) against this source's confirmed
  2026-09-24 publish date shows the two launches are roughly seven weeks
  apart, not back-to-back. Claim 2 above states the corrected date gap
  explicitly rather than repeating the Prospector's inaccurate framing.
- **Contradiction-filing decision**: the tool-sprawl tension documented
  under Cross-References → Contradicts was evaluated against the
  MINER.md §4a filing bar and judged not to meet it — this source
  describes a feature default and an available opt-out, not a claim that
  opposes Fowler et al.'s prescriptive guidance about the same mechanism.
  It is flagged prominently in-note instead of filed as a formal
  contradiction issue, consistent with the precedent set in
  `blog-google-api-gateway-model-routing.md`'s own Extraction Notes for a
  comparably borderline case.
- **Confidence calibration: settled.** Nearly every individual claim is
  rated "settled" because the claims are direct, first-party statements
  of product fact, configuration syntax, or explicitly disclosed Public
  Preview limitations/defects from official Google Cloud documentation
  published the same day as the announcement — not marketing framing,
  estimates, or third-party inference. The one exception (Claim 5, the
  tool-description design guidance) is rated "emerging" because it is
  asserted as authorial advice without a supporting benchmark or
  citation. The overall note is rated "settled" because the bulk of its
  evidentiary weight is technical reference documentation (annotation
  syntax, validation rules, error-code tables, argument-mapping
  mechanics) rather than unverified performance, accuracy, or adoption
  claims — this note does not claim "this works well in practice" or
  "teams are adopting this," which would require independent,
  non-vendor evidence this Public-Preview-day source cannot yet provide.
