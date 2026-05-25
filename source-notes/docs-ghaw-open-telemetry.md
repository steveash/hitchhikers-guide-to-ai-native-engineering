---
source_url: https://github.github.com/gh-aw/reference/open-telemetry
source_type: docs
title: "GitHub Agentic Workflows: OpenTelemetry Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: emerging
issue: "#787"
---

# GitHub Agentic Workflows: OpenTelemetry Reference

> The implementation-level counterpart to the OTLP overview in
> `blog-ghaw-weekly-2026-04-06.md` — documents the exact configuration
> schema (three endpoint forms), every runtime environment variable injected
> by gh-aw, the full OpenTelemetry GenAI span attribute set, the `logSpan`
> custom-span API, JSONL trace artifact layout, and the complete security
> sanitization rule set practitioners need to safely export traces to external
> backends.

## Source Context

- **Type**: docs (GitHub Agentic Workflows `reference/open-telemetry` page — a
  technical reference in the `reference/` section, distinct from the `patterns/`
  and `guides/` sections. Reference pages document the full configuration schema
  and API surface rather than patterns or end-to-end examples.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team
  (GitHub Next / Microsoft Research — the same team behind Peli de Halleux's
  "Agent Factory" blog series and the `gh aw` CLI platform). Configuration fields,
  environment variable names, span attribute names, and the `logSpan` API are
  authoritative for the `gh aw` platform. Claims about OpenTelemetry GenAI
  semantic conventions are a subset of the broader OpenTelemetry specification;
  the gh-aw implementation is one conforming instantiation.
- **Scope**: Covers OTLP configuration in workflow frontmatter (all three endpoint
  forms, headers, `if-missing`, custom attributes), runtime environment variables
  injected by gh-aw, built-in agent span attributes, trace artifact layout, the
  `otlp.cjs` `logSpan` API for custom spans, security sanitization rules, attribute
  naming conventions, debugging without a live collector, and the advanced
  `send_otlp_span.cjs` low-level API. Does NOT cover: how to configure specific
  OTLP backends (Honeycomb, Grafana Tempo, Sentry) beyond the endpoint URL;
  span schema for MCP tool calls specifically; or the observatory-plane architecture
  (covered in `blog-ghaw-agent-observability.md`).

## Extracted Claims

### Claim 1: The `observability.otlp` frontmatter block supports three endpoint forms — string, object, and array — where the array form fans out traces concurrently to multiple collectors

- **Evidence**: Reference page documents three distinct YAML forms with working
  examples. The array form explicitly supports concurrent fan-out to multiple
  endpoints (e.g., primary + backup collector).
- **Confidence**: settled (first-party reference documentation; the three forms
  are schema choices by the platform team with working YAML examples)
- **Quote**: (no direct prose quote; schema documented via YAML examples on the
  reference page; see Concrete Artifacts below)
- **Our assessment**: The array endpoint form is the most architecturally
  significant option. Teams running multi-tenant agentic systems or needing
  high-availability trace collection can fan out to primary and backup OTLP
  backends without any agent-side code changes. The `if-missing` field (accepting
  `error`, `warn`, or `ignore`) adds operational flexibility: a workflow that
  requires observability can set `if-missing: error` to fail fast if the endpoint
  secret is absent, preventing silent unobserved runs. For Ch02 (Harness
  Engineering): document all three endpoint forms and the `if-missing` field as
  the full OTLP configuration surface — the string form is backward-compatible,
  the object form is for single-endpoint production, and the array form is for
  HA or multi-tenant scenarios.

### Claim 2: When OTLP is configured, gh-aw injects six environment variables into every job, including `GH_AW_OTLP_ENDPOINTS` (full JSON array) and `COPILOT_OTEL_FILE_EXPORTER_PATH` (local span output path)

- **Evidence**: Reference page lists six variables with their derivation rules:
  `OTEL_EXPORTER_OTLP_HEADERS` (first endpoint auth), `OTEL_SERVICE_NAME`
  (sanitized workflow ID/name), `GH_AW_OTLP_ENDPOINTS` (JSON array of all
  endpoints), `GH_AW_OTLP_IF_MISSING` (from config), `GH_AW_OTLP_ATTRIBUTES`
  (JSON-encoded custom attributes), and `COPILOT_OTEL_FILE_EXPORTER_PATH` (local
  path).
- **Confidence**: settled (explicit variable list with derivation rules on the
  reference page; consistent with the implementation described in the weekly
  blog post)
- **Quote**: (no single prose quote; list of variables documented on the reference
  page; see Concrete Artifacts)
- **Our assessment**: The environment variable layer matters for shared import
  tooling: custom steps and shared workflow scripts can read `GH_AW_OTLP_ENDPOINTS`
  to discover all configured backends (not just the first) and `GH_AW_OTLP_ATTRIBUTES`
  to access custom span attributes set in the frontmatter. This is the mechanism
  that makes the `otlp.cjs` `logSpan` API possible — it reads these variables at
  runtime. The `OTEL_SERVICE_NAME` derived from sanitized workflow ID enables
  OTLP backends to group spans by workflow without further configuration. For
  Ch02: these environment variables are the integration contract between gh-aw's
  frontmatter-level config and any custom tooling that wants to emit compatible
  spans.

### Claim 3: Built-in agent spans follow OpenTelemetry GenAI semantic conventions and include separate token counters for cache reads and cache writes alongside input/output token counts

- **Evidence**: Reference page lists agent span attributes: `gen_ai.request.model`,
  `gen_ai.response.model`, `gen_ai.operation.name` (always "chat"), `gen_ai.system`,
  `gh-aw.engine.id`, `gen_ai.workflow.name`, `gen_ai.usage.input_tokens`,
  `gen_ai.usage.output_tokens`, `gen_ai.usage.cache_read.input_tokens`,
  `gen_ai.usage.cache_creation.input_tokens`, and `gen_ai.response.finish_reasons`.
- **Confidence**: emerging (first-party documentation; the GenAI semantic
  conventions are an evolving OpenTelemetry specification; field names may
  change as the spec matures)
- **Quote**: (no direct prose quote; attribute list documented on reference page;
  see Concrete Artifacts)
- **Our assessment**: The cache token attributes are the most operationally
  interesting entries. `gen_ai.usage.cache_read.input_tokens` and
  `gen_ai.usage.cache_creation.input_tokens` surface cache efficiency in
  distributed traces — practitioners can query their OTLP backend for runs
  with low cache-read ratios to identify workflows that would benefit from
  prompt caching. The `gen_ai.response.finish_reasons` array allows distinguishing
  normal completions from stop-reason events (e.g., max tokens reached) without
  parsing log text. For Ch02: document the cache token span attributes as the
  trace-level equivalent of the portfolio analyst's cost metric — traces enable
  per-span cache efficiency analysis rather than per-run aggregate analysis.

### Claim 4: Custom attributes set in the `observability.otlp.attributes` frontmatter field support GitHub Actions expressions and are automatically masked from job logs

- **Evidence**: Reference page documents the `attributes` field with a YAML
  example using `${{ github.run_id }}` and `${{ github.actor }}` expressions,
  and states values are "automatically masked from logs."
- **Confidence**: settled (first-party documented field with YAML example; the
  masking behavior is an explicit platform guarantee)
- **Quote**: (no single prose quote; behavior documented via YAML example and
  field description; see Concrete Artifacts)
- **Our assessment**: The expression support enables correlating traces to GitHub
  context: `langfuse.session.id: ${{ github.run_id }}` and
  `langfuse.user.id: ${{ github.actor }}` are the example field names shown,
  revealing the use case — OTLP backends that support session/user correlation
  (e.g., Langfuse) can receive this context without any custom instrumentation.
  The automatic log masking means these attribute values (which may include
  tokens or user identifiers from expressions) will not appear in GitHub Actions
  debug logs. For Ch02: the custom `attributes` field is how practitioners inject
  GitHub workflow context into every span, enabling cross-system correlation
  between GitHub Actions runs and OTLP observability platforms.

### Claim 5: Trace data is mirrored to JSONL files included in the `agent` artifact — `otel.jsonl` for gh-aw helpers and `copilot-otel.jsonl` for Copilot CLI spans

- **Evidence**: Reference page states: "Trace data is mirrored to JSONL files
  and included in the `agent` artifact." Two files: `otel.jsonl` (from gh-aw
  JavaScript helpers) and `copilot-otel.jsonl` (from Copilot CLI).
- **Confidence**: settled (first-party documented behavior; consistent with the
  local-file debugging path also described on the same page)
- **Quote**: "Trace data is mirrored to JSONL files and included in the `agent`
  artifact"
- **Our assessment**: The JSONL artifact is the trace equivalent of the token
  usage artifact described in `blog-ghaw-weekly-2026-04-06.md` Claim 8 — durable,
  queryable, and available even if the OTLP backend is unavailable or misconfigured.
  For teams that cannot run a live OTLP collector in CI (e.g., due to network
  restrictions), the JSONL artifact is the primary trace record. The two-file
  split (gh-aw vs. Copilot CLI) reflects that spans come from two separate
  instrumentation sources that are merged into a single trace but written to
  separate JSONL files. For Ch02: document JSONL trace artifacts as the fallback
  trace store that survives backend outages — teams should configure OTLP for
  live analysis but rely on the artifact for retrospective debugging.

### Claim 6: Custom spans from shared workflow imports use the `logSpan` API from `otlp.cjs`, which is non-fatal and never throws — export failures surface as warnings only

- **Evidence**: Reference page documents the `logSpan` API with a JavaScript
  example calling `await otlp.logSpan('my-tool', {...}, { startMs, endMs })`.
  States explicitly: "The API is non-fatal and never throws; export failures
  surface as warnings only."
- **Confidence**: settled (first-party documented API guarantee; the non-fatal
  behavior is an explicit design decision stated on the page)
- **Quote**: "The API is non-fatal and never throws; export failures surface as
  warnings only."
- **Our assessment**: The non-fatal design is the correct choice for shared
  tooling: a custom tool that calls `logSpan` should not fail because the OTLP
  backend is unreachable. The workflow's primary task must not be blocked by
  observability infrastructure failures. This is a defensively designed API.
  For Ch02: the `logSpan` API is the sanctioned extension point for adding
  domain-specific observability to shared workflow steps — extract the `require`
  path (`/tmp/gh-aw/actions/otlp.cjs`) as the integration pattern. The non-fatal
  guarantee means it can be freely used without try/catch wrapping.

### Claim 7: The `logSpan` API accepts `traceId`, `parentSpanId`, and `endpoint` override options, enabling custom spans to be correlated into the existing trace hierarchy or routed to alternative backends

- **Evidence**: Reference page lists `logSpan` options including `options.traceId`
  (override trace ID), `options.parentSpanId` (override parent span ID), and
  `options.endpoint` (override OTLP endpoint). All are optional.
- **Confidence**: emerging (first-party documentation; the option set is complete
  but how these interact with gh-aw's automatic trace correlation is not described
  in detail)
- **Quote**: (no direct prose quote; option list documented on reference page;
  see Concrete Artifacts)
- **Our assessment**: The `traceId` and `parentSpanId` overrides are what make
  custom tool spans truly composable with the built-in trace hierarchy. Without
  these, custom spans would be disconnected roots rather than children of the
  current workflow run's root span. Teams building custom shared tools should
  pass the `GITHUB_AW_OTEL_TRACE_ID` and `GITHUB_AW_OTEL_PARENT_SPAN_ID`
  environment variables (documented in the advanced API section) as the `traceId`
  and `parentSpanId` to attach their spans to the existing trace. For Ch02:
  document this trace correlation pattern as the recommended way to add custom
  instrumentation — use the environment variables as the correlation handshake,
  not hardcoded trace IDs.

### Claim 8: Security sanitization redacts attribute values for keys matching any of eight patterns (token, secret, password, key, auth, credential, api-key, access-key) and truncates string values exceeding 1,024 characters — applied to both wire exports and JSONL mirrors

- **Evidence**: Reference page lists the exact key patterns: "Redacts values for
  keys matching `token`, `secret`, `password`, `key`, `auth`, `credential`,
  `api-key`, or `access-key` (case-insensitive)" and "Truncates string values
  exceeding 1,024 characters." States both rules "apply to both wire exports and
  local JSONL mirrors."
- **Confidence**: settled (explicit enumeration in first-party reference
  documentation; consistent with the sanitization behavior described in
  `blog-ghaw-weekly-2026-04-06.md` Claim 3, which cited "token, secret, key,
  auth, etc.")
- **Quote**: "Redacts values for keys matching `token`, `secret`, `password`,
  `key`, `auth`, `credential`, `api-key`, or `access-key` (case-insensitive)"
- **Our assessment**: The reference page fills the gap left by the weekly blog
  note's "etc." — the complete list is eight patterns, notably adding `password`,
  `credential`, `api-key`, and `access-key` beyond the four cited in the April 6
  post. The 1,024-character truncation is new information not in the weekly note:
  it limits how much of any single attribute value can reach the OTLP backend,
  preventing large secrets or tokens that exceed the keyword patterns from being
  transmitted via value truncation. The dual-mirror guarantee (wire + JSONL) means
  sensitive data is sanitized in the artifact as well — a practitioner debugging
  locally with the JSONL artifact will also see redacted values. For Ch03 (Safety
  and Verification): document the complete eight-pattern list as the platform
  guarantee; practitioners who need to store sensitive data in spans must redesign
  their approach, as this sanitization cannot be disabled per-span.

### Claim 9: All `logSpan` output is appended to `/tmp/gh-aw/otel.jsonl` regardless of whether an OTLP endpoint is configured, providing a collector-free debugging path

- **Evidence**: Reference page states: "All spans from `logSpan` are appended to
  `/tmp/gh-aw/otel.jsonl` regardless of endpoint configuration."
- **Confidence**: settled (first-party documented behavior; consistent with the
  JSONL artifact claim in Claim 5 above)
- **Quote**: "All spans from `logSpan` are appended to `/tmp/gh-aw/otel.jsonl`
  regardless of endpoint configuration."
- **Our assessment**: This is the development and debugging path for practitioners
  who cannot wire up an OTLP backend in their local or staging environment. The
  file is always written, so custom tool instrumentation can be validated by
  inspecting the JSONL file directly without setting up Honeycomb or Grafana
  Tempo. When OTLP is enabled, Copilot CLI spans go to a separate file
  (`/tmp/gh-aw/copilot-otel.jsonl`). For Ch02: document the local JSONL file as
  the recommended debugging target when testing custom span instrumentation —
  no backend required until the spans are validated.

### Claim 10: An advanced low-level API (`send_otlp_span.cjs`) exposes `buildAttr`, `buildOTLPPayload`, `sendOTLPSpan`, `generateSpanId`, and `SPAN_KIND_CLIENT` for complex scenarios requiring direct OTLP payload construction

- **Evidence**: Reference page documents the require path
  (`/tmp/gh-aw/actions/send_otlp_span.cjs`) and lists the exported symbols.
  Also documents four environment variables available for the low-level path:
  `GITHUB_AW_OTEL_TRACE_ID`, `GITHUB_AW_OTEL_PARENT_SPAN_ID`,
  `OTEL_EXPORTER_OTLP_ENDPOINT`, and `OTEL_EXPORTER_OTLP_HEADERS`.
- **Confidence**: emerging (first-party documentation; the low-level API surface
  is documented but use cases are not shown; the `logSpan` high-level API covers
  most scenarios)
- **Quote**: (no direct prose quote; API documented via export list and environment
  variable table on reference page; see Concrete Artifacts)
- **Our assessment**: The low-level API is the escape hatch for teams building
  custom observability tooling that requires full control over OTLP payloads —
  custom span kinds, non-standard attribute formats, or batching. Most practitioners
  will not need this; the `logSpan` API covers the common case. However, the
  existence of the low-level API is architecturally significant: it means gh-aw's
  OTLP integration is extensible at the transport layer, not just at the span
  attribute layer. For Ch02: mention the low-level API exists for advanced cases
  but steer practitioners to `logSpan` as the starting point. The environment
  variables (`GITHUB_AW_OTEL_TRACE_ID`, `GITHUB_AW_OTEL_PARENT_SPAN_ID`) are also
  the handshake for `logSpan`'s `traceId`/`parentSpanId` options (Claim 7).

## Concrete Artifacts

### OTLP Endpoint Configuration — Three Forms

```yaml
# String form (backward-compatible, single endpoint)
observability:
  otlp:
    endpoint: ${{ secrets.OTLP_ENDPOINT }}
    headers:
      Authorization: ${{ secrets.OTLP_TOKEN }}

# Object form (single endpoint, explicit headers)
observability:
  otlp:
    endpoint:
      url: ${{ secrets.OTLP_ENDPOINT }}
      headers:
        Authorization: ${{ secrets.OTLP_TOKEN }}

# Array form (concurrent fan-out to multiple collectors)
observability:
  otlp:
    endpoint:
      - url: ${{ secrets.PRIMARY_ENDPOINT }}
        headers:
          Authorization: ${{ secrets.TOKEN_PRIMARY }}
      - url: ${{ secrets.BACKUP_ENDPOINT }}
        headers:
          Authorization: ${{ secrets.TOKEN_BACKUP }}
```

*Source: github.github.com/gh-aw/reference/open-telemetry, "Endpoint Forms" section*

### Custom Span Attributes Configuration

```yaml
# Attributes support GitHub Actions expressions; values are auto-masked from logs
observability:
  otlp:
    endpoint: ${{ secrets.OTLP_ENDPOINT }}
    attributes:
      deployment.environment: production
      langfuse.session.id: ${{ github.run_id }}
      langfuse.user.id: ${{ github.actor }}
```

*Source: github.github.com/gh-aw/reference/open-telemetry, "Custom Span Attributes" section*

### Runtime Environment Variables Injected by gh-aw When OTLP Is Configured

```
OTEL_EXPORTER_OTLP_HEADERS       — Authentication headers for the first endpoint
OTEL_SERVICE_NAME                 — Derived from sanitized workflow ID or name
GH_AW_OTLP_ENDPOINTS             — JSON array of all endpoint entries
GH_AW_OTLP_IF_MISSING            — Value from if-missing configuration
GH_AW_OTLP_ATTRIBUTES            — JSON-encoded custom attributes
COPILOT_OTEL_FILE_EXPORTER_PATH  — Local span output path
```

*Source: github.github.com/gh-aw/reference/open-telemetry, "Runtime Environment Variables" section*

### Agent Span Attributes (OpenTelemetry GenAI Semantic Conventions)

```
gen_ai.request.model                  — Model name used
gen_ai.response.model                 — Resolved runtime model
gen_ai.operation.name                 — Always "chat"
gen_ai.system                         — Standardized system identifier
gh-aw.engine.id                       — Raw engine identifier
gen_ai.workflow.name                  — Workflow name
gen_ai.usage.input_tokens             — Total input tokens
gen_ai.usage.output_tokens            — Total output tokens
gen_ai.usage.cache_read.input_tokens  — Reused cache tokens
gen_ai.usage.cache_creation.input_tokens — Written cache tokens
gen_ai.response.finish_reasons        — Agent stop reason array
```

*Source: github.github.com/gh-aw/reference/open-telemetry, "Agent Span Attributes" section*

### `logSpan` API — High-Level Custom Span Emission

```javascript
const otlp = require('/tmp/gh-aw/actions/otlp.cjs');

// Standard usage
await otlp.logSpan('my-tool', {
  'my-tool.version': '1.2.3',
  'my-tool.items_processed': 42,
  'my-tool.result': 'success',
}, { startMs, endMs });

// Error span
await otlp.logSpan('my-scanner', {
  'my-scanner.items_scanned': 100,
}, { isError: true, errorMessage: 'database connection timed out' });
```

**`logSpan` Parameters:**
- `toolName` (string): Logical tool identifier
- `attributes` (Record): Domain-specific key-value pairs
- `options.startMs` / `options.endMs`: Span timing
- `options.isError` (boolean): Marks span as error
- `options.errorMessage` (string): Error description
- `options.traceId` (string): Override trace ID (use `GITHUB_AW_OTEL_TRACE_ID`)
- `options.parentSpanId` (string): Override parent span ID (use `GITHUB_AW_OTEL_PARENT_SPAN_ID`)
- `options.endpoint` (string): Override OTLP endpoint

*Source: github.github.com/gh-aw/reference/open-telemetry, "Custom Spans from Shared Imports" and "logSpan API Parameters" sections*

### Security Sanitization Rules

```
Redacted keys (case-insensitive match):
  token, secret, password, key, auth, credential, api-key, access-key

Truncation:
  String values > 1,024 characters are truncated

Scope:
  Applied to both wire (OTLP export) and local JSONL mirror files
```

*Source: github.github.com/gh-aw/reference/open-telemetry, "Security Features" section*

### Advanced Low-Level API (`send_otlp_span.cjs`)

```javascript
const {
  buildAttr, buildOTLPPayload, sendOTLPSpan,
  generateSpanId, SPAN_KIND_CLIENT,
} = require('/tmp/gh-aw/actions/send_otlp_span.cjs');

// Correlation environment variables available for manual trace stitching:
//   GITHUB_AW_OTEL_TRACE_ID          — 32-char hex trace ID
//   GITHUB_AW_OTEL_PARENT_SPAN_ID    — 16-char hex parent span ID
//   OTEL_EXPORTER_OTLP_ENDPOINT      — Collector base URL
//   OTEL_EXPORTER_OTLP_HEADERS       — Authentication headers
```

*Source: github.github.com/gh-aw/reference/open-telemetry, "Advanced Low-Level API" section*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-weekly-2026-04-06.md` Claim 1 ("Agentic workflows can export full
    OpenTelemetry distributed traces to any OTLP-compatible backend via a single
    `observability.otlp` frontmatter block"): This reference page is the canonical
    schema documentation for the feature that Claim 1 announced. The reference
    confirms the single-frontmatter-block model and extends it with the full option
    set (three endpoint forms, `if-missing`, custom `attributes`).
  - `blog-ghaw-weekly-2026-04-06.md` Claim 3 ("OTLP payloads are automatically
    sanitized before export — sensitive span attribute values matching key patterns
    (token, secret, key, auth) are redacted"): This reference page confirms and
    extends that claim — the full redaction list is eight patterns (`token`,
    `secret`, `password`, `key`, `auth`, `credential`, `api-key`, `access-key`),
    and adds the 1,024-character truncation rule not mentioned in the weekly note.
    No contradiction: the weekly note's "etc." was accurate, just incomplete.
  - `blog-ghaw-agent-observability.md` Claim 1 ("Observability isn't optional
    when you're running dozens of AI agents"): This reference page is the
    implementation contract that backs that architectural principle — it provides
    the specific configuration, span attributes, and API needed to actually deploy
    the observability the blog post argues for.

- **Extends**:
  - `blog-ghaw-weekly-2026-04-06.md` — the weekly note announced OTLP tracing
    and its security model but noted in Extraction Note 3: "The `observability.otlp`
    frontmatter block structure is described but not shown in the post. The YAML
    artifact above is a plausible inference from the feature description; verify
    against current gh-aw documentation before recommending in the guide." This
    reference page is that verification — the three endpoint forms, the `if-missing`
    field, and the `attributes` field are the definitive schema. The inference in
    the weekly note's Concrete Artifacts section was correct in structure but
    incomplete in scope.
  - `blog-ghaw-agent-observability.md` — that note covers the three-tier
    observatory architecture (Metrics Collector / Portfolio Analyst / Audit Workflows).
    This reference page adds the implementation layer below those three agents: the
    per-span, per-job, per-tool-call trace data that OTLP provides. Together, the
    two sources cover both the analytical layer (what monitoring agents do) and the
    instrumentation layer (what spans look like and how to extend them).
  - `docs-ghaw-monitoring-patterns.md` — that note covers the config-layer safe
    output patterns for monitoring (Projects v2, failure aggregation, no-op control,
    CLI commands). This page extends the observability picture with the distributed
    tracing layer: while monitoring patterns handle structured workflow outputs
    (issues, project updates), OTLP handles the execution-level trace data (span
    timing, token usage, tool calls). Both layers are needed for full observability.

- **Contradicts**: None. The reference page's eight-pattern sanitization list is
  a superset of the four patterns named in `blog-ghaw-weekly-2026-04-06.md` Claim 3
  ("token, secret, key, auth, etc.") — the "etc." was intentional, not a
  contradiction. No existing source claims that custom span emission requires
  careful error handling (this page explicitly says it is non-fatal), and no
  existing source describes the local JSONL file path or the advanced low-level
  API. No contradiction issue is warranted.

- **Novel**:
  - **Array endpoint form for concurrent fan-out** (Claim 1): No existing source
    describes multi-endpoint fan-out for OTLP. The array form is new to the corpus.
  - **`if-missing` field behavior** (Claim 1): The ability to make OTLP
    misconfiguration a hard failure (`error`) vs. a warning vs. silent (`ignore`)
    is not documented in any other source note.
  - **Complete runtime environment variable set** (Claim 2): `blog-ghaw-weekly-2026-04-06.md`
    does not enumerate the variables injected by gh-aw. This reference page is
    the first corpus source to document the full set, including `GH_AW_OTLP_ENDPOINTS`
    and `GH_AW_OTLP_ATTRIBUTES` which are the integration contracts for custom tooling.
  - **Cache token span attributes** (Claim 3): `gen_ai.usage.cache_read.input_tokens`
    and `gen_ai.usage.cache_creation.input_tokens` as trace-level span attributes
    are not documented in any existing source. The weekly note covers per-tool-call
    metrics; this adds per-span cache efficiency data.
  - **`logSpan` API with trace correlation overrides** (Claims 6–7): No existing
    source describes the `logSpan` API or its `traceId`/`parentSpanId` options for
    correlating custom spans into the gh-aw trace hierarchy. The non-fatal design
    guarantee is also new.
  - **1,024-character truncation rule** (Claim 8): Not mentioned in the weekly
    note or any other corpus source. This is a new security data point.
  - **`/tmp/gh-aw/otel.jsonl` as collector-free debugging target** (Claim 9):
    The specific local file path for trace debugging without a live OTLP backend
    is not documented in any other source note.
  - **`send_otlp_span.cjs` low-level API** (Claim 10): Not mentioned anywhere
    else in the corpus. The exported symbol list (`buildAttr`, `buildOTLPPayload`,
    `sendOTLPSpan`, `generateSpanId`, `SPAN_KIND_CLIENT`) and the four correlation
    environment variables are entirely new to the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Update the `observability.otlp` recommendation (currently informed by the
    inferred schema in `blog-ghaw-weekly-2026-04-06.md` Concrete Artifacts, which
    noted it should be verified against documentation) to use the authoritative
    three-endpoint-form schema from this reference. Add the `if-missing: error`
    option as the recommended setting for workflows where observability is required.
  - Add the custom `attributes` field with `${{ github.run_id }}` correlation as
    the standard pattern for tying gh-aw traces to GitHub Actions run context in
    OTLP backends.
  - Add `logSpan` API documentation: the `require` path, the non-fatal guarantee,
    the `traceId`/`parentSpanId` override pattern for trace stitching. Frame as
    the recommended extension point for custom tool instrumentation in shared
    workflow imports.
  - Add the `/tmp/gh-aw/otel.jsonl` file as the debugging path for validating
    custom span instrumentation without a live OTLP backend.
  - Add the JSONL artifact pair (`otel.jsonl`, `copilot-otel.jsonl`) as the
    durable trace record, analogous to the token usage artifact from Claim 8 in
    the weekly note — traces survive backend outages via the artifact.

- **Chapter 03 (Safety and Verification)**:
  - Update the OTLP sanitization rule set from the weekly note's four-pattern
    list ("token, secret, key, auth") to the definitive eight-pattern list
    ("token, secret, password, key, auth, credential, api-key, access-key").
    Add the 1,024-character truncation rule as a second sanitization mechanism.
    Practitioners must know the full list to avoid naming span attributes that
    would be inadvertently redacted.
  - Document the dual-scope guarantee (wire + JSONL) so practitioners understand
    that local artifact inspection also shows redacted values — the sanitization
    is not bypassable by reading the local file.

- **Chapter 06 (Observability and Monitoring, planned)**:
  - Add the GenAI span attribute list as the canonical trace schema for gh-aw
    agent runs. The cache token attributes (`cache_read`, `cache_creation`) enable
    trace-level cache efficiency queries that complement the run-level Portfolio
    Analyst analysis from `blog-ghaw-agent-observability.md`.
  - Add the array endpoint form as the HA pattern for production observability —
    teams should configure both a primary and backup OTLP endpoint to avoid
    losing trace data during backend outages.

## Extraction Notes

1. **Source is a reference page, not a guide or patterns page**: The `reference/`
   section of `github.github.com/gh-aw/` documents the full configuration schema
   and API surface. The page is structured around configuration tables and code
   examples rather than narrative explanation. All content was read; the page is
   dense with specific field names, API options, and environment variable names
   that required careful extraction rather than summarization.

2. **This reference page resolves the open verification flag in `blog-ghaw-weekly-2026-04-06.md`**:
   That note's Extraction Note 3 flagged its OTLP frontmatter artifact as "a
   plausible inference from the feature description; verify against current gh-aw
   documentation before recommending in the guide." This reference page is the
   verification. The weekly note's inferred YAML was structurally correct but
   missing the object form, array form, `if-missing` field, and `attributes` field.

3. **No sub-pages followed**: The reference page is self-contained and does not
   link to sub-pages beyond cross-references to other parts of the gh-aw docs
   (patterns, guides). The `logSpan` and `send_otlp_span.cjs` APIs are fully
   documented on this single page.

4. **Security sanitization list is authoritative here**: The weekly note cited
   "token, secret, key, auth, etc." — the "etc." suggested the list was
   incomplete. The reference page provides the definitive enumeration. Both
   sources are correct; this source is more complete.

5. **No contradictions found**: Reviewed `blog-ghaw-weekly-2026-04-06.md`,
   `blog-ghaw-agent-observability.md`, `docs-ghaw-monitoring-patterns.md`,
   `docs-ghaw-monitor-ops.md`, and `docs-ghaw-frontmatter-full-reference.md`.
   No claims in any existing source note materially oppose the claims in this
   reference page at the MINER.md §4a filing threshold.
