---
source_url: https://github.github.com/gh-aw/reference/mcp-gateway
source_type: docs
title: "GitHub Agentic Workflows: MCP Gateway Reference Specification v1.14.0"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: 2026-06-01
date_extracted: 2026-06-21
last_checked: 2026-06-21
status: current
confidence_overall: emerging
issue: "#399"
---

# GitHub Agentic Workflows: MCP Gateway Reference Specification v1.14.0

> The formal RFC-style technical specification for the MCP Gateway — a transparent proxy
> enabling unified HTTP access to multiple MCP servers (containerized stdio and HTTP types)
> via protocol translation, with a guard policy framework using integrity-level access
> control, GitHub Actions OIDC for upstream auth, OpenTelemetry tracing, health monitoring,
> lifecycle management, and a 3-conformance-level compliance testing framework spanning 11
> test suites (50+ cases) — the authoritative gateway-layer companion to the workflow-level
> integrity reference (`docs-ghaw-integrity-reference.md`) and the Safe Outputs spec
> (`docs-ghaw-safe-outputs-specification.md`).

## Source Context

- **Type**: docs (formal RFC-style normative specification, v1.14.0, published June 2026.
  Uses RFC 2119 requirement language — MUST, SHALL, SHOULD, MAY — throughout. This is the
  definitive gateway-level implementation reference, distinct from the workflow-configuration
  perspective in `docs-ghaw-integrity-reference.md` and the Safe Outputs implementation in
  `docs-ghaw-safe-outputs-specification.md`.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the same team
  behind the Peli de Halleux agent factory blog series and the gh-aw platform. Claims about
  MUST/SHALL requirements, conformance levels, protocol translation semantics, guard policy
  precedence, and compliance test categories are authoritative for this specification. Claims
  about generalizability to other MCP hosting environments require additional evidence.
- **Scope**: The MCP Gateway as a proxy infrastructure layer — configuration format (JSON
  stdin), protocol translation from stdio containers to HTTP, guard policy with integrity
  levels, API key and OIDC upstream authentication, health monitoring endpoints, lifecycle
  management, OpenTelemetry integration, isolation guarantees, and compliance testing with
  three conformance levels and 11 test suites. Does NOT cover: workflow-level frontmatter
  configuration of `tools.github.min-integrity` (that is `docs-ghaw-integrity-reference.md`),
  the workflow compilation process (`docs-ghaw-compilation-process.md`), individual MCP
  server configuration types in the workflow author's view (`docs-ghaw-mcps.md`), or the
  Safe Outputs specification (`docs-ghaw-safe-outputs-specification.md`).

## Extracted Claims

### Claim 1: Stdio-based MCP servers MUST be containerized; direct command execution without containerization is explicitly not supported by the gateway

- **Evidence**: Normative requirement from the specification with SHALL NOT language:
  "Stdio-based MCP servers MUST be containerized... The gateway SHALL NOT support
  non-containerized process execution."
- **Confidence**: settled (RFC 2119 MUST/SHALL NOT language in a first-party specification
  document; this is a hard architectural constraint, not a recommendation)
- **Quote**: "Stdio-based MCP servers MUST be containerized... The gateway SHALL NOT support
  non-containerized process execution."
- **Our assessment**: This is the single most security-significant constraint in the entire
  spec. The explicit SHALL NOT on non-containerized execution closes the attack surface
  that would exist if stdio servers ran as child processes in the gateway's own environment.
  The `docs-ghaw-mcps.md` Claim 2 notes that stdio servers use `command` + `args` for local
  process execution — that is the workflow-author configuration view; the gateway's containerization
  requirement is the underlying enforcement mechanism that makes it safe. For Ch02 (Harness
  Engineering): when building or selecting MCP servers for the gh-aw platform, practitioners
  cannot use bare stdio command invocation — all stdio servers must be packaged as container
  images.

### Claim 2: The gateway translates stdio container communication to HTTP responses while preserving tool signatures and supporting concurrent requests

- **Evidence**: Protocol Translation test suite (T-PTL-001 through T-PTL-008) enumerates:
  "stdio request/response cycles, HTTP passthrough behavior, 'Tool signature preservation,'
  concurrent request handling, large payload handling, partial response buffering, and HTTP
  connection failure error responses."
- **Confidence**: settled (first-party spec; test categories explicitly enumerate what is
  verified)
- **Quote**: (no direct quote; derived from the T-PTL compliance test enumeration — see
  Concrete Artifacts)
- **Our assessment**: Tool signature preservation is operationally significant: the HTTP
  endpoint exposed by the gateway must present the same tool names, parameter schemas, and
  return types that the underlying stdio server advertises. This means workflow authors who
  use the gateway's HTTP interface can rely on the same tool surface as if calling the stdio
  server directly. The concurrent request handling requirement means the gateway must multiplex
  requests across containerized servers without ordering or isolation violations. For Ch02:
  the gateway's HTTP translation layer means that from the workflow's perspective, all MCP
  servers appear as HTTP endpoints — the transport heterogeneity (stdio vs. HTTP) is hidden
  behind the gateway's unified interface.

### Claim 3: The gateway configuration uses a JSON stdin format with server definitions, variable expression rendering, volume mounts, OpenTelemetry configuration, and guard policy

- **Evidence**: Configuration format examples from the specification document the top-level
  JSON structure with `mcpServers`, `gateway`, and nested fields. Variable expressions use
  `"${VARIABLE_NAME}"` syntax. Volume mounts use `"host:container:mode"` format (e.g.,
  `"/var/data/input:/app/input:ro"`). OpenTelemetry is configured under
  `gateway.opentelemetry`. Guard policy fields include `min-integrity`, `allowed-repos`,
  `blocked-users`, `trusted-users`, `approval-labels`, and `refusal-labels`.
- **Confidence**: emerging (configuration examples from WebFetch summarization; exact field
  names and nested structure are as returned but not independently verified against the raw
  spec text)
- **Quote**: (no direct quote; see Concrete Artifacts for the JSON configuration examples)
- **Our assessment**: The gateway's JSON stdin configuration is distinct from the workflow
  YAML frontmatter configuration documented in `docs-ghaw-mcps.md`. Workflow authors configure
  MCP servers in workflow frontmatter (YAML); the gateway reads this translated configuration
  at startup as JSON via stdin. This layered configuration model means practitioners who write
  workflows do not write gateway JSON directly — the compilation process (`docs-ghaw-compilation-process.md`)
  generates the gateway input from the workflow frontmatter. For Ch02: document the distinction
  between the workflow-author's view (YAML frontmatter) and the gateway's runtime view (JSON
  stdin configuration output by the compiler).

### Claim 4: The guard policy framework defines five integrity levels in hierarchical order — merged > approved > unapproved > none > blocked — where blocked cannot be used as a threshold

- **Evidence**: Specification section "Integrity Levels" defines the hierarchy: "merged >
  approved > unapproved > none > blocked". Definitions: `merged` (merged PRs; commits on
  default branch), `approved` (OWNER/MEMBER/COLLABORATOR; recognized platform bots;
  trusted-users list), `unapproved` (CONTRIBUTOR or FIRST_TIME_CONTRIBUTOR), `none` (all
  other content), `blocked` (users in blocked-users — always denied).
- **Confidence**: settled (first-party specification; the five levels and their member
  definitions are explicitly listed; consistent with `docs-ghaw-integrity-reference.md`
  Claim 3)
- **Quote**: "merged > approved > unapproved > none > blocked"
- **Our assessment**: The integrity level hierarchy here is the gateway-level specification
  of the same mechanism that `docs-ghaw-integrity-reference.md` documents from the
  workflow-configuration perspective. The key reinforcement: `blocked` is not a configurable
  threshold level (you cannot set `min-integrity: blocked`) — it is an unconditional denial
  state for users in the `blocked-users` list. The `min-integrity` default for public repos
  is `approved` (consistent with `docs-ghaw-integrity-reference.md` Claim 4). This spec
  provides the gateway-layer implementation view of the same filtering that the integrity
  reference describes from the practitioner configuration view. For Ch03 (Safety and
  Verification): the guard policy and the `min-integrity` workflow configuration are the
  same system seen from different vantage points; this spec is the authoritative implementation
  layer.

### Claim 5: The guard policy's effective integrity computation is a six-step precedence algorithm where blocked-users wins unconditionally, refusal-labels override promotion, and trust elevation cannot lower integrity

- **Evidence**: The specification describes the effective integrity computation order:
  "1. Base integrity... 2. blocked-users check... 3. refusal-labels check...
  4. trusted-users check... 5. approval-labels check... 6. Default". Key constraints:
  "blocked-users MUST take precedence over all other policy fields. Blocked items MUST be
  denied even if they carry an approval-labels label" and "refusal-labels MUST override
  promotion from trusted-users and approval-labels."
- **Confidence**: settled (RFC 2119 MUST language; algorithm order is normative; consistent
  with `docs-ghaw-integrity-reference.md` Claim 5)
- **Quote**: "blocked-users MUST take precedence over all other policy fields. Blocked items
  MUST be denied even if they carry an approval-labels label"
- **Our assessment**: The MUST language here confirms the normative status of the precedence
  from `docs-ghaw-integrity-reference.md` Claim 5's six-step algorithm. The guard policy
  implementation is defense-in-depth: the most restrictive controls (blocked-users, refusal-labels)
  are checked before positive adjustments (trusted-users, approval-labels) and cannot be
  overridden by them. Trust elevation via `trusted-users` or `approval-labels` implements
  `max(base, approved)` — it can only raise integrity, never lower it. For Ch03: the
  MUST/MUST NOT language in the spec means this precedence is a testable conformance
  requirement, not just recommended practice.

### Claim 6: The gateway exposes two required HTTP endpoints — GET /health (authentication-exempt) and POST /close (graceful shutdown) — plus per-server MCP endpoints at POST /mcp/{server-name}

- **Evidence**: Specification states: "The gateway MUST expose the following HTTP endpoints:
  `POST /mcp/{server-name}`, `GET /health`, `POST /close`". The `/health` response includes
  status, specification version, gateway version, and per-server health information.
  Critically: "The gateway MUST NOT require authentication" for the `/health` endpoint.
- **Confidence**: settled (RFC 2119 MUST/MUST NOT language; endpoint paths are explicitly
  specified)
- **Quote**: "The gateway MUST expose the following HTTP endpoints: `POST /mcp/{server-name}`,
  `GET /health`, `POST /close`"
- **Our assessment**: The authentication exemption for `/health` is a deliberate design
  decision enabling health-check orchestration (container schedulers, load balancers, CI
  health probes) without requiring credentials. The per-server MCP endpoints
  (`/mcp/{server-name}`) are the unified HTTP interface that hides transport heterogeneity
  — a workflow calling the gateway doesn't need to know whether the underlying server is
  stdio or HTTP. For Ch04 (Observability and Cost): the `/health` endpoint's per-server
  status response is the operational visibility surface for gateway monitoring — document
  it as the observability entry point for MCP infrastructure health.

### Claim 7: The gateway implements a graceful shutdown sequence via POST /close that: stops new requests, completes in-flight requests, terminates containers (SIGTERM then SIGKILL after 10 seconds), and returns HTTP 410 on subsequent calls

- **Evidence**: Lifecycle management section describes the `/close` shutdown sequence:
  "1. Stop Accepting New Requests: Immediately reject any new RPC requests;
  2. Complete In-Flight Requests: Allow currently processing requests to complete;
  3. Terminate All Containers: Stop all running MCP server containers" with "SIGTERM followed
  by SIGKILL after 10-second timeout; 4. Release Resources" and exit with status 0.
  "The endpoint is idempotent — subsequent calls return HTTP 410 Gone."
- **Confidence**: settled (first-party spec; lifecycle sequence is explicitly specified with
  signal and timeout details)
- **Quote**: (no direct quote; lifecycle steps are presented as a numbered list — see
  Concrete Artifacts)
- **Our assessment**: The 10-second SIGTERM → SIGKILL window is the key operational
  parameter for containerized MCP servers: servers must be designed to shut down cleanly
  within 10 seconds of SIGTERM or they will be forcibly killed. The HTTP 410 idempotency
  response enables safe multi-call shutdown coordination. For Ch02 (Harness Engineering):
  when building custom stdio MCP servers, the 10-second graceful shutdown window must be
  considered in the server's SIGTERM handler design.

### Claim 8: The gateway enforces startup timeout (default 30 seconds) and per-invocation tool timeout (default 60 seconds) with distinct semantics and error responses

- **Evidence**: Timeout semantics from the specification: startup — "Start timer when server
  container is launched; wait for server ready signal; if timeout expires, kill server
  container and return error." Tool invocation — "Start timer when RPC request is sent to
  server; wait for complete response; if timeout expires, return timeout error to client."
  Defaults: startup timeout 30 seconds, tool invocation timeout 60 seconds.
- **Confidence**: settled (first-party spec; timeout values and behavior are explicitly
  specified)
- **Quote**: (no direct quote for timeout values; see Concrete Artifacts for the timeout
  configuration field)
- **Our assessment**: The two-timeout model matches distinct failure modes: startup timeouts
  catch unresponsive containers (hung initialization, missing image); tool timeouts catch
  slow or hanging tool invocations (long-running queries, network unavailability). For Ch02:
  practitioners deploying stdio MCP servers should tune both timeout values based on their
  server's initialization characteristics and expected tool invocation latencies. A server
  whose initialization pulls data might need a higher startup timeout; a server calling slow
  external APIs might need a higher tool timeout.

### Claim 9: OpenTelemetry integration is configured via gateway.opentelemetry with endpoint and service name, and the compliance suite includes 10 OTLP trace tests covering span creation, trace ID propagation, and failure handling

- **Evidence**: Configuration examples from the specification show
  `gateway.opentelemetry.endpoint` and `gateway.opentelemetry.serviceName` fields.
  Compliance test suite T-OTEL-001 through T-OTEL-010 covers "OTLP endpoint configuration,
  trace ID/span ID propagation, span creation for tool invocations, and failure handling."
- **Confidence**: settled (field names from configuration examples; test suite enumeration
  from compliance section)
- **Quote**: (no direct quote; see Concrete Artifacts for the OpenTelemetry configuration
  example)
- **Our assessment**: OpenTelemetry integration at the gateway level means every MCP tool
  invocation can be traced end-to-end — from the workflow trigger through the gateway to the
  underlying MCP server and back. The trace ID/span ID propagation requirement means gateway
  spans are linkable to broader distributed traces. For Ch04 (Observability and Cost): the
  gateway's OTLP integration is the instrumentation layer for MCP observability — document
  as the recommended configuration for organizations that need audit trails of MCP tool
  invocations.

### Claim 10: Container isolation is a four-property guarantee: process isolation via separate containers, environment variable isolation between servers, credential isolation (no cross-server config access), and per-server independent volume mount isolation

- **Evidence**: Isolation guarantees from the specification: "Each container's mounts MUST
  be independent; mounts configured for one server MUST NOT affect other servers" and
  "The gateway MUST NOT allow servers to access each other's configuration." Isolation test
  suite T-ISO-001 through T-ISO-008 covers "container isolation, environment variable
  isolation, credential isolation, cross-container communication prevention, container
  failure isolation, and volume mount isolation enforcement."
- **Confidence**: settled (RFC 2119 MUST/MUST NOT language; isolation test suite enumerates
  each property)
- **Quote**: "Each container's mounts MUST be independent; mounts configured for one server
  MUST NOT affect other servers"
- **Our assessment**: The four isolation properties together mean that a compromised or
  malicious MCP server running inside the gateway cannot access credentials, configuration,
  or filesystem data belonging to co-hosted servers. This is the gateway's security answer
  to the multi-tenancy problem: multiple MCP servers share a gateway process but are
  isolated from each other at the container boundary. For Ch03: document this isolation
  guarantee when recommending the gateway pattern for multi-server MCP deployments — the
  isolation model contains blast radius if one server is compromised.

### Claim 11: The specification defines three conformance levels — Required (Level 1: basic proxy + stdio + config parsing), Standard (Level 2: HTTP transport + auth + health endpoints), Complete (Level 3: all optional features including variable expressions + timeout configuration)

- **Evidence**: Compliance section from the specification: "Level 1 (Required): Basic proxy
  functionality, stdio transport, configuration parsing"; "Level 2 (Standard): HTTP
  transport, authentication, health endpoints"; "Level 3 (Complete): All optional features
  including variable expressions, timeout configuration."
- **Confidence**: settled (first-party spec; conformance levels are explicitly named and
  scoped)
- **Quote**: "Level 1 (Required): Basic proxy functionality, stdio transport, configuration
  parsing"
- **Our assessment**: The three-level conformance model enables incremental compliance
  implementation: a minimal gateway must pass Level 1 (35+ test cases covering
  configuration, protocol translation, isolation); a production gateway should reach Level 2
  (adding authentication and health monitoring); a complete gateway reaches Level 3 (adding
  variable expressions, configurable timeouts, and full OpenTelemetry). For Ch02: when
  evaluating or building a gateway implementation, use the conformance levels as a
  capability checklist. Level 2 is the minimum for production use; Level 1 is the floor
  for a viable development environment.

### Claim 12: GitHub Actions OIDC is supported for authenticating the gateway's HTTP calls to upstream MCP servers, using the same audience field and OIDC token issuance as the workflow-level OIDC pattern

- **Evidence**: Configuration example from the spec shows upstream HTTP server auth using
  `"auth": {"type": "github-oidc", "audience": "https://my-server.example.com"}`. This
  mirrors the workflow-level OIDC configuration in `docs-ghaw-mcps.md` Claim 4 but applies
  at the gateway's outbound HTTP connections rather than at the workflow runner.
- **Confidence**: settled (first-party spec; OIDC configuration example is explicit;
  field names match the workflow-level configuration)
- **Quote**: (no direct quote; OIDC configuration example — see Concrete Artifacts)
- **Our assessment**: The gateway-level OIDC support means practitioners can use the same
  secretless authentication pattern at both the workflow layer (for runner → gateway
  connections) and the gateway layer (for gateway → upstream MCP server connections).
  This is consistent security architecture: no static credentials at either translation
  boundary. For Ch03 (Safety and Verification): recommend OIDC at both layers for HTTP
  MCP integration. The gateway handling upstream OIDC token acquisition means workflow
  authors do not need to manage upstream credentials in the workflow frontmatter — the
  gateway handles the token exchange.

## Concrete Artifacts

### Gateway Configuration Format (JSON Stdin)

```json
{
  "mcpServers": {
    "data-processor": {
      "container": "ghcr.io/example/data-mcp:latest",
      "type": "stdio",
      "mounts": [
        "/var/data/input:/app/input:ro",
        "/var/data/output:/app/output:rw"
      ]
    },
    "github": {
      "container": "ghcr.io/github/github-mcp-server:latest",
      "env": {
        "GITHUB_TOKEN": "${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  },
  "gateway": {
    "port": 8080,
    "apiKey": "string",
    "domain": "string"
  }
}
```

*Source: `reference/mcp-gateway` — Configuration Format section*

### OpenTelemetry Configuration

```json
{
  "gateway": {
    "opentelemetry": {
      "endpoint": "https://collector.example.com:4318/v1/traces",
      "serviceName": "my-mcp-gateway"
    }
  }
}
```

*Source: `reference/mcp-gateway` — OpenTelemetry Configuration section*

### GitHub OIDC Authentication for Upstream HTTP Servers

```json
{
  "mcpServers": {
    "my-mcp-server": {
      "type": "http",
      "url": "https://my-server.example.com/mcp",
      "auth": {
        "type": "github-oidc",
        "audience": "https://my-server.example.com"
      }
    }
  }
}
```

*Source: `reference/mcp-gateway` — Authentication section*

### Gateway Output Configuration (Unified HTTP Endpoints)

After startup, the gateway rewrites server configurations as unified HTTP endpoints:

```json
{
  "mcpServers": {
    "server-name": {
      "type": "http",
      "url": "http://{domain}:{port}/mcp/server-name",
      "headers": {
        "Authorization": "{apiKey}"
      }
    }
  }
}
```

*Source: `reference/mcp-gateway` — Configuration Output section*

### Guard Policy Configuration Fields

| Field | Type | Default |
|-------|------|---------|
| `min-integrity` | string | `approved` (public repos) |
| `allowed-repos` | string or array | `"all"` |
| `blocked-users` | array or expression | `[]` |
| `trusted-users` | array or expression | `[]` |
| `approval-labels` | array or expression | `[]` |
| `refusal-labels` | array or expression | `[]` |

*Source: `reference/mcp-gateway` — Guard Policy section*

### Effective Integrity Computation Algorithm

```
1. Start with base integrity from GitHub metadata
2. If author in blocked-users → effective integrity = blocked (UNCONDITIONAL)
3. Else if item has a refusal-labels label → effective integrity = none (OVERRIDES PROMOTION)
4. Else if author in trusted-users → effective integrity = max(base, approved)
5. Else if item has an approval-labels label → effective integrity = max(base, approved)
6. Else → effective integrity = base
Then: apply min-integrity threshold after all adjustments
```

*Source: `reference/mcp-gateway` — Guard Policy: Effective Integrity Computation section*

### Lifecycle Shutdown Sequence (POST /close)

```
1. Stop Accepting New Requests — Immediately reject any new RPC requests
2. Complete In-Flight Requests — Allow currently processing requests to complete
3. Terminate All Containers:
   a. Send SIGTERM to all running MCP server containers
   b. Wait up to 10 seconds
   c. Send SIGKILL to any containers that have not exited
4. Release Resources — exit with status 0
Note: Endpoint is idempotent — subsequent calls return HTTP 410 Gone
```

*Source: `reference/mcp-gateway` — Lifecycle Management section*

### Compliance Test Suites (11 Suites, 50+ Test Cases)

```
T-CFG-001 to T-CFG-019  — Configuration Tests
  stdio/HTTP server config, variable resolution, undefined variable detection,
  payload directory validation, unknown field rejection, custom server types
  with schema registration, volume mount formats, mount access modes

T-PTL-001 to T-PTL-008  — Protocol Translation Tests
  stdio request/response cycles, HTTP passthrough, tool signature preservation,
  concurrent request handling, large payload handling, partial response
  buffering, HTTP connection failure error responses

T-ISO-001 to T-ISO-008  — Isolation Tests
  container isolation, environment variable isolation, credential isolation,
  cross-container communication prevention, container failure isolation,
  volume mount isolation enforcement

T-AUTH-001 to T-AUTH-006 — Authentication Tests
  valid token acceptance, invalid token rejection, missing token handling,
  health endpoint exemption, token rotation, trusted bot identity config

T-TIMEOUT-001 to T-TIMEOUT-004 — Timeout Tests
  startup timeout enforcement, tool invocation timeout handling,
  timeout error responses

T-HEALTH-001 to T-HEALTH-005 — Health Monitoring Tests
  health endpoint responses, server status reporting, version info inclusion,
  health check behavior

T-CONFIG-001 to T-CONFIG-003 — Configuration Output Tests
  stdout configuration rewriting, headers object presence in output

T-ERROR-001 to T-ERROR-006 — Error Handling Tests
  startup failure handling, runtime error logging, error response formats,
  graceful degradation

T-LIFECYCLE-001 to T-LIFECYCLE-004 — Gateway Lifecycle Tests
  gateway startup, shutdown via /close endpoint, idempotent close behavior

T-OTEL-001 to T-OTEL-010 — OpenTelemetry Tests
  OTLP endpoint configuration, trace ID/span ID propagation, span creation
  for tool invocations, failure handling

T-GP-001 to T-GP-008 — Guard Policy Tests
  integrity level computation, approval label promotion, refusal label
  demotion, blocked-user enforcement
```

*Source: `reference/mcp-gateway` — Compliance Testing section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-integrity-reference.md` Claims 3 and 5 (four integrity levels, six-step
    computation algorithm): this spec independently specifies the same integrity level
    hierarchy (`merged > approved > unapproved > none > blocked`) and the same computation
    precedence order (blocked-users → refusal-labels → trusted-users → approval-labels →
    base). The two sources are the workflow-configuration view (integrity reference) and
    the gateway-implementation view (this spec) of the same underlying mechanism. The MUST
    language here upgrades the precedence from "first-party documentation" to "normative
    requirement."
  - `docs-ghaw-integrity-reference.md` Claim 4 (public repos get `min-integrity: approved`
    automatically): this spec's guard policy default field (`min-integrity` defaults to
    `approved` for public repos) is the gateway-level implementation of the same default.
    Both sources agree on the default value and scope.
  - `docs-ghaw-mcps.md` Claim 4 (GitHub Actions OIDC for HTTP MCP authentication): Claim
    12 here documents the same OIDC pattern at the gateway level (gateway → upstream server),
    confirming OIDC as the consistent auth mechanism across both the workflow-to-gateway and
    gateway-to-upstream connections.
  - `docs-ghaw-safe-outputs-specification.md` Claim 1 (Safe Outputs MCP Gateway as a
    "security-centric translation layer"): the MCP Gateway spec here describes the same
    proxy architecture at the general level (all MCP servers), while the Safe Outputs spec
    documents the specialized write-operations gateway. The two specs are siblings at the
    same architectural layer, serving different traffic (read → general MCP Gateway;
    write → Safe Outputs MCP Gateway).

- **Extends**:
  - `docs-ghaw-integrity-reference.md` (user-configuration view): this spec adds the
    gateway-level implementation architecture — the protocol translation layer, isolation
    guarantees, health monitoring, lifecycle management, and compliance testing that
    *implement* the integrity filtering the integrity reference documents from the user's
    perspective. Together they give the complete picture: "how to configure" (integrity
    reference) + "how the gateway implements it" (this spec).
  - `docs-ghaw-mcps.md` Claims 2 and 6 (four server types, Docker network controls): the
    containerization MUST requirement here (Claim 1) explains WHY the workflow-level
    configuration uses container-based server types — the gateway enforces containerization
    as a normative requirement, so all stdio servers must be containers. The gateway spec
    is the implementation layer that makes `docs-ghaw-mcps.md`'s Docker/stdio distinction
    architecturally coherent.
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer defense-in-depth security pipeline):
    Claims 4–5 (guard policy enforcement) and Claim 10 (container isolation) add technical
    depth to Layers 2 (runtime isolation), 3 (permission separation), and 5 (output
    sanitization) of the five-layer model. The guard policy tests (T-GP-001 to T-GP-008)
    are the compliance test suite for Layer 3's content-filtering component.

- **Contradicts**: None identified. All integrity level definitions, computation algorithm
  precedence, default behaviors, and OIDC authentication patterns are consistent with
  existing source notes. No contradiction issue required.

- **Novel**:
  - **Stdio containerization as a SHALL NOT normative constraint** (Claim 1): No existing
    source note captures the explicit SHALL NOT on non-containerized execution. The
    `docs-ghaw-mcps.md` note documents "stdio" as one of four server types without stating
    that the gateway enforces containerization as a hard requirement. This closes that gap.
  - **Protocol translation architecture with tool signature preservation** (Claim 2): The
    specific requirement that the gateway preserve tool signatures across the stdio→HTTP
    translation is not documented in any existing source note. This is a conformance
    requirement (T-PTL "Tool signature preservation") with implications for how custom
    stdio servers are tested for gateway compatibility.
  - **Dual timeout model (startup 30s, tool invocation 60s)** (Claim 8): Neither the
    specific timeout values nor the two-tier timeout model (initialization vs. invocation)
    are documented in any existing source note. This is a concrete operational parameter
    for MCP server design.
  - **Graceful shutdown sequence with SIGTERM → SIGKILL 10-second window** (Claim 7): The
    specific shutdown sequence, 10-second SIGTERM window, SIGKILL escalation, and HTTP 410
    idempotency are not documented in any existing source note. MCP server authors must
    design SIGTERM handlers with this window in mind.
  - **Three-level conformance framework with 11 test suites** (Claim 11): No existing
    source note documents the compliance testing structure of the MCP Gateway. This is
    new to the corpus: a testable specification with formally scoped conformance levels.
  - **Gateway-level OpenTelemetry with 10 compliance test cases** (Claim 9): The OTel
    integration is mentioned conceptually in the triage comment but was not in any existing
    source note before this extraction. The 10 T-OTEL test cases make it a formally
    specified feature, not just a configuration option.
  - **HTTP 410 idempotent shutdown response** (Claim 7): The specific use of HTTP 410 Gone
    as the idempotent close response is a protocol-level detail not found elsewhere in the
    corpus.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add containerization as a hard architectural constraint for stdio MCP servers** (Claim
  1): The guide should document the SHALL NOT on non-containerized execution as a non-optional
  requirement, not just a recommendation. Practitioners building custom stdio MCP servers for
  gh-aw must package them as container images. Cite: "Stdio-based MCP servers MUST be
  containerized... The gateway SHALL NOT support non-containerized process execution."

- **Add the gateway's unified HTTP interface as the practitioner's mental model** (Claim 2):
  When explaining MCP server integration, introduce the MCP Gateway's role: regardless of
  whether a server is stdio or HTTP natively, it appears as an HTTP endpoint to the workflow
  at `/mcp/{server-name}`. The transport heterogeneity is implementation detail; the
  practitioner works with the unified HTTP surface.

- **Add the two-timeout operational parameters** (Claim 8): Document the default values
  (startup: 30 seconds, tool invocation: 60 seconds) as concrete tuning knobs for MCP
  server deployment. Practitioners with slow-initializing servers or long-running tool
  invocations must configure these explicitly.

- **Add SIGTERM handler design as a MCP server authoring requirement** (Claim 7): When
  building custom stdio MCP servers, the server's SIGTERM handler must complete within
  10 seconds or the container will be forcibly killed. Document this as a server authoring
  constraint.

### Chapter 03: Safety and Verification

- **Add four-property isolation guarantee as the gateway's security foundation** (Claim 10):
  The gateway provides process, environment variable, credential, and volume mount isolation
  between co-hosted MCP servers. When recommending multi-server MCP deployments, cite this
  as the blast-radius containment mechanism: a compromised server cannot read another
  server's credentials or filesystem.

- **Add guard policy as the gateway-layer implementation of integrity filtering** (Claims 4–5):
  Connect the workflow-level `min-integrity` configuration (`docs-ghaw-integrity-reference.md`)
  to the gateway-level guard policy implementation: the workflow YAML configuration maps to
  gateway JSON guard policy fields at runtime. The precedence algorithm (blocked-users →
  refusal-labels → trusted-users → approval-labels → base) is a normative MUST requirement,
  not just recommended behavior.

- **Add OIDC at both translation boundaries as the recommended credential-free pattern**
  (Claim 12): For HTTP MCP integration, recommend OIDC at both layers — workflow runner to
  gateway (via workflow frontmatter `auth: type: github-oidc`) and gateway to upstream server
  (via gateway `auth.type: github-oidc`). No static credentials at either boundary.

### Chapter 04: Observability and Cost

- **Add OpenTelemetry configuration as the MCP observability primitive** (Claim 9): Document
  `gateway.opentelemetry.endpoint` and `gateway.opentelemetry.serviceName` as the
  configuration path for MCP tool invocation tracing. The 10 T-OTEL compliance test cases
  mean OTel is a formally specified feature — organizations needing audit trails of MCP
  invocations should configure it as standard practice.

- **Add /health endpoint as the operational monitoring entry point** (Claim 6): For
  operations teams, the authentication-exempt `/health` endpoint provides per-server status
  without credential management — document as the health-check target for gateway monitoring
  infrastructure (container schedulers, uptime monitors, CI health probes).

## Extraction Notes

1. **WebFetch returns summarized content**: The gh-aw documentation is an Astro/Starlight
   SPA. WebFetch returns rendered text with AI summarization rather than raw page source.
   Three separate targeted fetches were made to maximize content coverage:
   (a) full-page summary for architecture overview,
   (b) configuration format and code blocks,
   (c) guard policy details and compliance testing.
   Quotes marked as verbatim were taken from fetch results; code blocks are representative
   of the spec's examples but minor formatting variations are possible.

2. **Conformance level names are settled**: The three level names (Required/Standard/Complete)
   and their scopes were consistent across the compliance section fetch. Confidence: settled.

3. **Guard policy field names settled**: The six field names (`min-integrity`, `allowed-repos`,
   `blocked-users`, `trusted-users`, `approval-labels`, `refusal-labels`) and the table's
   defaults are consistent with the integrity reference (`docs-ghaw-integrity-reference.md`),
   providing cross-source verification.

4. **Timeout default values**: The 30-second startup and 60-second tool invocation defaults
   were returned in the health/lifecycle fetch. These are consistent with what would be
   reasonable production defaults. Confidence: settled for the values as stated in the spec,
   though they may be overridable per-server.

5. **No contradictions to file**: Reviewed all existing source notes and CONTRADICTIONS.md
   (C-001 through C-003). No claims in this source materially oppose existing source notes.
   The guard policy integrity levels and computation algorithm are consistent with
   `docs-ghaw-integrity-reference.md`. No contradiction issue required.

6. **Publication date estimated**: The specification is dated as v1.14.0 and references
   June 2026 in the triage comment. `date_published` is set to 2026-06-01 as an estimate;
   the exact publication date was not explicitly found in the fetched content.
