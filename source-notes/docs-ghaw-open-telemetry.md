---
source_url: https://github.github.com/gh-aw/reference/open-telemetry
source_type: docs
title: "GitHub Agentic Workflows: OpenTelemetry Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-17
last_checked: 2026-05-17
status: current
confidence_overall: emerging
issue: "#787"
---

# GitHub Agentic Workflows: OpenTelemetry Reference

> Implementation-level complement to the observatory architecture in
> `blog-ghaw-agent-observability.md` — documents the concrete OTLP configuration
> patterns, auto-emitted GenAI span attributes, `logSpan()` API for custom tool
> instrumentation, automatic security sanitization of trace data, and local
> JSONL file fallback for debugging without a live collector.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/open-telemetry`
  page — in the "Reference" section, the authoritative implementation guide for
  distributed tracing integration. Distinct from the `blog/` series posts on
  observability architecture and the `patterns/monitoring` page on issue-based
  monitoring.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team
  (same team behind Peli de Halleux's agent factory and the `gh aw` platform
  documentation). YAML configuration, environment variable names, and JavaScript
  API signatures are authoritative for the `gh aw` platform. High credibility
  for platform-specific claims; behavioral details do not automatically
  generalize to non-`gh-aw` agentic systems, though OpenTelemetry GenAI
  semantic conventions are an industry-wide standard.
- **Scope**: Covers OTLP endpoint configuration (all three endpoint forms),
  `if-missing` error handling, runtime environment variables injected by the
  platform, agent span attribute definitions following the OpenTelemetry GenAI
  semantic conventions, the `logSpan()` API for custom instrumentation from
  shared imports, security sanitization rules for attribute values, and local
  JSONL file output for debugging without a live collector. Does NOT cover:
  the three-tier observatory architecture (see `blog-ghaw-agent-observability.md`),
  GitHub Projects v2 monitoring or failure issue aggregation (see
  `docs-ghaw-monitoring-patterns.md`), how to build consumer workflows that
  analyze audit data (see `docs-ghaw-audit-with-agents.md`), or
  vendor-specific OTLP backend setup.

## Extracted Claims

### Claim 1: OTLP is configured via `observability.otlp` in workflow frontmatter, keeping telemetry setup co-located with workflow definition

- **Evidence**: YAML configuration shown on the page places the OTLP endpoint
  and headers under `observability.otlp` in the workflow frontmatter alongside
  other workflow configuration fields. Uses GitHub Actions secret syntax
  (`${{ secrets.OTLP_ENDPOINT }}`) for credential management.
- **Confidence**: settled (first-party documentation; YAML config is explicit
  and matches the overall gh-aw frontmatter-driven configuration model)
- **Quote**: (no direct prose quote; the configuration pattern is expressed
  as YAML examples — see Concrete Artifacts below)
- **Our assessment**: Placing OTLP config in workflow frontmatter rather than
  in a separate config file or environment-level settings keeps observability
  configuration versioned with the workflow definition. This mirrors the
  gh-aw philosophy of making all workflow behavior declarative and
  repository-checked. The use of secrets for endpoint credentials aligns with
  the platform's standard secret-injection model. For Ch02 (Harness Engineering):
  document OTLP configuration as part of the workflow frontmatter specification,
  not a separate infrastructure concern.

### Claim 2: Three endpoint forms support simple string, single-object, and array fan-out to multiple collectors

- **Evidence**: The page documents three distinct endpoint forms:
  (1) string — backward-compatible simple URL,
  (2) object — single endpoint with per-endpoint `url` and `headers`,
  (3) array — multiple endpoint objects for concurrent fan-out.
  The `headers` field additionally accepts both map format and
  comma-separated string format (`"Authorization=${{ secrets.TOKEN }},X-Tenant=acme"`).
- **Confidence**: settled (first-party documentation; all three forms are
  shown with explicit YAML examples)
- **Quote**: (no direct prose quote; structural claim expressed via YAML
  examples — see Concrete Artifacts)
- **Our assessment**: The three-form design reflects practical deployment
  needs: string form for simple single-collector setups, object form for
  per-endpoint auth, array form for sending traces to multiple backends
  simultaneously (e.g., a team collector and an org-wide collector). The
  comma-separated header string form enables header values to be passed as
  a single secret rather than multiple secrets. For Ch06 (Observability):
  document the array form as the recommended pattern for multi-tenant or
  multi-team deployments where traces need to reach both a local team
  collector and an org-wide backend.

### Claim 3: Array mode provides fault tolerance — if one endpoint fails, export continues to remaining endpoints

- **Evidence**: Direct statement on the page describing array-mode behavior.
- **Confidence**: settled (first-party documented behavior guarantee)
- **Quote**: "If one endpoint fails in array mode, export still continues for the remaining endpoints."
- **Our assessment**: This fault-tolerance guarantee makes the array form
  suitable for production deployments where trace data must not be silently
  dropped. A primary collector failure does not interrupt tracing to a backup
  collector. For Ch07 (Production Operations): recommend the array form for
  production workflows where trace data completeness is important — configure
  both a primary backend and a secondary fallback endpoint.

### Claim 4: `if-missing` controls startup behavior when OTLP endpoint or header values resolve to empty, defaulting to error (startup failure)

- **Evidence**: The page documents the `if-missing` field with three values:
  `error` (default — fails startup), `warn`, and `ignore`. The description
  states it "controls behavior when OTLP endpoint/header values resolve to
  empty values at runtime."
- **Confidence**: settled (first-party documentation; explicit field name,
  values, and default are given)
- **Quote**: "`if-missing` (string: `error`, `warn`, `ignore`) — Controls behavior when OTLP endpoint/header values resolve to empty values at runtime. `error` (default) fails startup."
- **Our assessment**: Defaulting to `error` on missing values is a sensible
  safety default: it prevents silent trace data loss when a secret is not
  configured. Teams that want optional observability (where the workflow
  should run even if the OTLP endpoint is not configured) should use
  `if-missing: ignore`. `warn` is appropriate for development environments
  where traces are desired but not required for correctness. For Ch02: document
  this as a required decision when adding OTLP config — production workflows
  should keep the `error` default; CI/dev workflows may use `ignore`.

### Claim 5: The platform injects trace context environment variables (trace ID and parent span ID) so tools can participate in the distributed trace without custom setup

- **Evidence**: The page lists `GITHUB_AW_OTEL_TRACE_ID` (32-char hex) and
  `GITHUB_AW_OTEL_PARENT_SPAN_ID` (16-char hex) among the injected runtime
  environment variables, alongside the standard OTLP headers variable.
- **Confidence**: settled (first-party documented variables with format
  specifications)
- **Quote**: (no direct prose description; expressed in the runtime environment
  variables table — see Concrete Artifacts)
- **Our assessment**: Injecting the trace ID and parent span ID as environment
  variables enables any subprocess or tool invoked by the workflow to
  participate in the same distributed trace by reading these values, without
  requiring the tool to have any awareness of the gh-aw tracing infrastructure.
  This is the standard W3C Trace Context propagation pattern adapted for
  environment-variable injection rather than HTTP header propagation. For Ch06:
  document these variables as the mechanism for trace propagation to child
  processes — tools that want to emit correlated spans should read these.

### Claim 6: `OTEL_SERVICE_NAME` is set to `gh-aw.<sanitized-workflow-id>` format, creating a predictable, queryable service identity for each workflow

- **Evidence**: The page specifies `OTEL_SERVICE_NAME` as
  `gh-aw.<sanitized-workflow-id> when WorkflowID is available` in the runtime
  environment variables table.
- **Confidence**: settled (first-party documented format)
- **Quote**: "`gh-aw.<sanitized-workflow-id>` when `WorkflowID` is available"
- **Our assessment**: The `gh-aw.` prefix namespace ensures workflow traces
  are distinguishable from other services in a shared OTLP backend. The
  `<sanitized-workflow-id>` suffix creates per-workflow service identity,
  enabling backend filtering and dashboards scoped to individual workflows.
  Teams using multi-tenant observability backends benefit from this convention
  because they can filter spans by `service.name` prefix to see all gh-aw
  workflows. For Ch06: document the `gh-aw.<workflow-id>` naming convention
  as the standard service name pattern — backends should be configured to
  accept this prefix as a service family.

### Claim 7: Agent spans follow OpenTelemetry GenAI semantic conventions and include token usage and cache metrics as span attributes

- **Evidence**: The page lists 10 specific span attributes on agent spans,
  including `gen_ai.request.model`, `gen_ai.usage.input_tokens`,
  `gen_ai.usage.output_tokens`, `gen_ai.usage.cache_read.input_tokens`,
  `gen_ai.usage.cache_creation.input_tokens`, and `gen_ai.response.finish_reasons`.
  The page states these follow "OpenTelemetry GenAI semantic conventions."
- **Confidence**: emerging (first-party documentation; OpenTelemetry GenAI
  conventions are an emerging CNCF/OTel standard that gh-aw has adopted)
- **Quote**: (no direct prose quote beyond the attribute names; the claim
  "OpenTelemetry GenAI semantic conventions" appears in the source)
- **Our assessment**: The inclusion of `cache_read.input_tokens` and
  `cache_creation.input_tokens` alongside standard token usage attributes
  means trace data automatically captures cache efficiency per agent turn —
  a detail that would otherwise require custom instrumentation. This makes
  OTLP the richer data source for cost analysis compared to issues/discussions
  (which carry no per-turn token breakdown). For Ch06: document the GenAI
  span attributes as the standard cost accounting surface for per-turn LLM
  usage — backend queries on `gen_ai.usage.*` attributes enable per-workflow
  and per-model cost reporting without any custom instrumentation.

### Claim 8: Custom tools can emit correlated spans via `logSpan()` from the `otlp.cjs` shared import, making tool-level observability available without bespoke tracing setup

- **Evidence**: The page documents the `logSpan()` API with full parameter
  specification: `toolName` (string), `attributes` (Record), and an `options`
  object with `startMs`, `endMs`, `isError` (boolean), and `errorMessage`
  (string). Example shows `otlp.logSpan('my-tool', {'my-tool.version': '1.2.3',
  'my-tool.items_processed': 42}, { startMs, endMs })`.
- **Confidence**: settled (first-party API documentation with parameter types)
- **Quote**: (API expressed in code example — see Concrete Artifacts;
  `toolName` described as "Logical name for the tool (e.g. `my-scanner`)")
- **Our assessment**: The `logSpan()` API lowers the instrumentation bar for
  shared tools in gh-aw workflows: rather than wiring up a full OpenTelemetry
  SDK, a shared import can emit a single span that is automatically correlated
  to the parent workflow trace via `GITHUB_AW_OTEL_TRACE_ID`. The `isError`
  and `errorMessage` parameters enable error classification without custom
  span status manipulation. For Ch02: recommend `logSpan()` as the standard
  pattern for any shared tool that processes meaningful quantities or durations
  that practitioners would want to see in traces. Domain-specific attributes
  (e.g., `my-tool.items_processed`) make spans immediately useful for
  cross-run comparisons.

### Claim 9: Attribute values matching security-sensitive key patterns are automatically redacted before export, replacing the value with `[REDACTED]`

- **Evidence**: The page specifies the complete list of key patterns that
  trigger redaction: `token`, `secret`, `password`, `passwd`, `key`, `auth`,
  `credential`, `api-key`, `access-key` — all matched case-insensitively.
  Values matching these patterns are replaced with `[REDACTED]` before
  the span is exported to OTLP backends or written to local files.
- **Confidence**: settled (first-party security documentation with explicit
  key list)
- **Quote**: "**Redacts** the value of any attribute whose key matches `token`, `secret`, `password`, `passwd`, `key`, `auth`, `credential`, `api-key`, or `access-key` (case-insensitive), replacing it with `[REDACTED]`."
- **Our assessment**: Automatic redaction is a significant safety property:
  tools that accidentally emit credential values as span attributes (e.g.,
  logging an API key for debugging) will have those values stripped before
  reaching the OTLP backend. The case-insensitive pattern match covers
  common naming conventions. However, note the keyword `key` is broad —
  attributes like `cache_key` or `partition_key` that contain non-sensitive
  values will also be redacted. Teams should avoid using `key` as a substring
  in attribute names for non-sensitive data, or expect redaction. For Ch03
  (Safety and Verification): document this as a defense-in-depth measure for
  trace data, noting the intentionally broad `key` pattern and its implications
  for naming.

### Claim 10: Every span emitted by `logSpan()` is written to a local JSONL file at `/tmp/gh-aw/otel.jsonl` regardless of whether an OTLP endpoint is configured

- **Evidence**: Direct statement on the page specifying the file path and
  the unconditional write behavior.
- **Confidence**: settled (first-party documented behavior)
- **Quote**: "Every span emitted by `logSpan` is always appended as a sanitized JSON line to `/tmp/gh-aw/otel.jsonl`, even when `OTEL_EXPORTER_OTLP_ENDPOINT` is not set."
- **Our assessment**: The unconditional local file write means that
  instrumentation added via `logSpan()` has zero-config observability:
  practitioners can download the workflow artifact and inspect all custom
  spans without configuring an OTLP backend. This design lowers the adoption
  threshold — teams can add instrumentation and inspect results locally before
  committing to a backend. The "sanitized" qualifier confirms redaction also
  applies to the local file, not just remote export. For Ch06: document the
  local JSONL file as the first-resort debugging tool for instrumented workflows
  — before standing up an OTLP backend, retrieve the `agent` artifact and
  inspect `otel.jsonl`.

### Claim 11: Span files are included in the `agent` workflow artifact when OTLP is enabled, enabling post-run trace analysis without a live collector

- **Evidence**: The page states both `otel.jsonl` and `copilot-otel.jsonl`
  are included in the `agent` artifact when OTLP is configured.
- **Confidence**: settled (first-party documented artifact inclusion)
- **Quote**: "Both files are included in the `agent` artifact when OTLP is enabled, so you can inspect spans after the run."
- **Our assessment**: Artifact-based trace inspection is the bridge between
  ad-hoc debugging and full observability infrastructure. A practitioner can
  download the `agent` artifact from any workflow run and immediately inspect
  spans in JSONL format — no OTLP backend required. This complements
  `docs-ghaw-artifacts-reference.md`'s taxonomy of the `agent` artifact;
  span files are an additional artifact component beyond the AI interaction
  logs already documented there. For Ch07 (Production Operations): document
  artifact-based span inspection as the day-1 debugging workflow before
  organizations invest in OTLP infrastructure — the trace data is already
  there, just in the artifact rather than a backend.

## Concrete Artifacts

### OTLP Configuration — All Three Endpoint Forms

```yaml
# String form (backward-compatible, simplest)
observability:
  otlp:
    endpoint: ${{ secrets.OTLP_ENDPOINT }}
    headers:
      Authorization: ${{ secrets.OTLP_TOKEN }}

# Object form (single endpoint with per-endpoint headers)
observability:
  otlp:
    endpoint:
      url: ${{ secrets.OTLP_ENDPOINT }}
      headers:
        Authorization: ${{ secrets.OTLP_TOKEN }}
        X-Tenant: acme

# Array form (concurrent fan-out to multiple collectors)
observability:
  otlp:
    endpoint:
      - url: ${{ secrets.OTLP_ENDPOINT_PRIMARY }}
        headers:
          Authorization: ${{ secrets.OTLP_TOKEN_PRIMARY }}
      - url: ${{ secrets.OTLP_ENDPOINT_BACKUP }}
        headers:
          Authorization: ${{ secrets.OTLP_TOKEN_BACKUP }}
```

*Source: gh-aw reference/open-telemetry, "Configure observability.otlp" and "Endpoint forms" sections*

### Runtime Environment Variables Injected by the Platform

| Variable | Description |
|---|---|
| `OTEL_EXPORTER_OTLP_HEADERS` | "Comma-separated `key=value` headers for the first endpoint" |
| `OTEL_SERVICE_NAME` | "`gh-aw.<sanitized-workflow-id>` when `WorkflowID` is available" |
| `GH_AW_OTLP_ENDPOINTS` | "JSON array of all endpoint entries, used by gh-aw JavaScript span exporters" |
| `GH_AW_OTLP_IF_MISSING` | "Set to `warn` or `ignore` when configured" |
| `COPILOT_OTEL_FILE_EXPORTER_PATH` | "Path for Copilot CLI span output (`/tmp/gh-aw/copilot-otel.jsonl`)" |
| `GITHUB_AW_OTEL_TRACE_ID` | 32-char hex trace ID for the current workflow run |
| `GITHUB_AW_OTEL_PARENT_SPAN_ID` | 16-char hex parent span ID for the current workflow run |

*Source: gh-aw reference/open-telemetry, "Runtime environment variables" section*

### Agent Span Attributes (OpenTelemetry GenAI Semantic Conventions)

```
gen_ai.request.model
gen_ai.operation.name
gen_ai.system
gh-aw.engine
gen_ai.workflow.name
gen_ai.usage.input_tokens
gen_ai.usage.output_tokens
gen_ai.usage.cache_read.input_tokens
gen_ai.usage.cache_creation.input_tokens
gen_ai.response.finish_reasons
```

*Source: gh-aw reference/open-telemetry, "Agent span attributes" section*

### `logSpan()` API — Custom Span Emission from Shared Imports

```javascript
// Import from the shared otlp helper
await otlp.logSpan(toolName, attributes, options);

// Parameters:
// toolName  (string)  — "Logical name for the tool (e.g. `my-scanner`)"
// attributes (Record) — "Domain-specific attributes emitted on the span"
// options.startMs     (number)  — Span start time (ms since epoch)
// options.endMs       (number)  — Span end time (ms since epoch)
// options.isError     (boolean) — When true, sets span status to ERROR
// options.errorMessage (string) — Human-readable status message

// Example from the page:
await otlp.logSpan('my-tool', {
  'my-tool.version': '1.2.3',
  'my-tool.items_processed': 42,
}, { startMs, endMs });
```

*Source: gh-aw reference/open-telemetry, "Custom spans from shared imports" and "logSpan API" sections*

### Security Sanitization Rules

```
Redacted key patterns (case-insensitive substring match):
  token, secret, password, passwd, key, auth, credential, api-key, access-key
  → replaced with [REDACTED]

String value truncation:
  Values longer than 1,024 characters are truncated.

Applies to:
  - OTLP export (remote backends)
  - Local JSONL file (/tmp/gh-aw/otel.jsonl)
```

*Source: gh-aw reference/open-telemetry, "Security" section*

### Local JSONL Files for Debugging

```
/tmp/gh-aw/otel.jsonl         — All logSpan() output (always written, even without OTLP)
/tmp/gh-aw/copilot-otel.jsonl — Copilot CLI span output (path via COPILOT_OTEL_FILE_EXPORTER_PATH)

Both files included in the `agent` workflow artifact when OTLP is enabled.
```

*Source: gh-aw reference/open-telemetry, "Trace files and artifacts" and "Debugging without a live collector" sections*

## Cross-References

- **Corroborates**:
  - `blog-ghaw-agent-observability.md` Claim 1 ("Observability isn't optional
    when you're running dozens of AI agents"): This reference page provides
    the OTLP instrumentation layer that backs the observatory architecture.
    The blog post names the observatory plane and describes what it measures;
    this page documents how to configure the tracing infrastructure that feeds
    it. The two together give motivation + mechanism.
  - `blog-ghaw-agent-observability.md` Claim 4 (Portfolio Analyst identifying
    agents "way too chatty with their LLM calls"): The `gen_ai.usage.input_tokens`
    and `gen_ai.usage.output_tokens` span attributes documented here are the
    raw data that makes such cross-run cost analysis possible. The Portfolio
    Analyst's finding (chatty LLM calling as a detectable pattern) is only
    discoverable if token usage is captured per-span — which this page confirms
    is the default.
  - `docs-ghaw-monitoring-patterns.md` Claim 7 (`gh aw audit <run-id>` as a
    per-run operational inspection tool): The OTLP span data documented here is
    the underlying tracing data that audit commands surface. Monitoring patterns
    covers the CLI commands for inspection; this page covers what data is
    available to inspect and how it got there.

- **Extends**:
  - `blog-ghaw-agent-observability.md` — that note covers the *what* (three-tier
    observatory architecture, meta-audit loop) and the *why* (observability as
    first-class architecture). This page covers the *how to instrument* —
    OTLP configuration, span emission, and security properties. The two together
    give the complete observability picture for the gh-aw platform: architectural
    motivation + technical implementation.
  - `docs-ghaw-monitoring-patterns.md` — that note covers issue-based monitoring
    (Projects v2 safe outputs, failure aggregation, CLI commands). This page
    covers distributed tracing (OTLP config, span attributes, logSpan API). The
    two are orthogonal instrumentation layers: issue-based monitoring for
    structured workflow outcomes; distributed tracing for per-turn LLM usage,
    tool latency, and error classification. Neither replaces the other.
  - `docs-ghaw-artifacts-reference.md` — that note documents the `agent`
    artifact taxonomy. This page adds that span files (`otel.jsonl`,
    `copilot-otel.jsonl`) are included in the `agent` artifact when OTLP is
    enabled — a component not covered in the artifact taxonomy.

- **Contradicts**: None. No existing source note makes claims about OTLP
  configuration, GenAI span attribute conventions, or trace context propagation
  in gh-aw. The nearest thematic overlap is the three-tier observability
  architecture in `blog-ghaw-agent-observability.md`, which describes what
  the observatory measures; this source describes how tracing works at the
  infrastructure level. These are complementary, not contradictory.

- **Novel**:
  - **OTLP configuration in workflow frontmatter** (Claim 1): No existing source
    note documents `observability.otlp` as a frontmatter configuration field.
    This is the first corpus entry for the tracing configuration layer of gh-aw.
  - **Array-mode fault-tolerant fan-out** (Claim 3): The guarantee that array-
    mode export continues to remaining endpoints when one fails is new to the
    corpus and has direct implications for production OTLP deployment patterns.
  - **`if-missing` error handling** (Claim 4): The three-value field controlling
    startup behavior for missing OTLP credentials is not described elsewhere.
  - **Trace context env vars** (Claim 5): `GITHUB_AW_OTEL_TRACE_ID` and
    `GITHUB_AW_OTEL_PARENT_SPAN_ID` as mechanism for sub-process trace
    participation is not documented in any existing note.
  - **OpenTelemetry GenAI span attributes** (Claim 7): The complete 10-attribute
    list including cache token metrics is not described anywhere in the corpus.
    This is the first corpus entry establishing what LLM telemetry data is
    available per-turn from the platform.
  - **`logSpan()` custom instrumentation API** (Claim 8): No existing source
    note documents the `otlp.cjs` shared import or the `logSpan()` API. This is
    the first corpus entry for tool-level custom tracing in gh-aw.
  - **Automatic security sanitization of trace data** (Claim 9): The specific
    key-pattern list, replacement value, and scope (both remote and local files)
    are not described elsewhere. Relevant to Ch03 (Safety and Verification).
  - **Unconditional local JSONL file output** (Claim 10): The always-write
    behavior to `/tmp/gh-aw/otel.jsonl` regardless of OTLP configuration is not
    documented elsewhere and is the key enabler of zero-config instrumentation
    debugging.

## Guide Impact

- **Chapter 06 (Observability and monitoring)**:
  - Add OTLP configuration as the concrete implementation layer beneath the
    observatory architecture from `blog-ghaw-agent-observability.md`. Recommend
    the string form for simple setups, array form for production with failover.
    Document `if-missing: error` as the production default (prevents silent
    trace loss), `if-missing: ignore` for optional telemetry in dev workflows.
  - Add the OpenTelemetry GenAI span attributes (especially
    `gen_ai.usage.input_tokens`, `gen_ai.usage.cache_read.input_tokens`,
    `gen_ai.usage.cache_creation.input_tokens`) as the per-turn cost accounting
    surface — these are richer than issue-based monitoring for granular cost
    analysis.
  - Document `OTEL_SERVICE_NAME` = `gh-aw.<workflow-id>` naming convention for
    backend filtering and per-workflow dashboards.

- **Chapter 02 (Harness Engineering)**:
  - Add `logSpan()` as the standard pattern for instrumenting shared tools:
    lower bar than a full OTel SDK, co-located with existing gh-aw imports,
    automatically correlated to the parent trace. Recommend domain-specific
    attributes (e.g., `my-tool.items_processed`) for cross-run comparisons.
  - Document `GITHUB_AW_OTEL_TRACE_ID` and `GITHUB_AW_OTEL_PARENT_SPAN_ID`
    as the trace context propagation mechanism for tools and subprocesses.

- **Chapter 03 (Safety and Verification)**:
  - Add automatic trace attribute sanitization as a defense-in-depth property
    for OTLP export. Note the broad `key` pattern (matches `cache_key`,
    `partition_key`, etc.) and its implication: avoid `key` as an attribute
    name substring for non-sensitive data.

- **Chapter 07 (Production Operations)**:
  - Recommend array-mode OTLP with a backup endpoint for production workflows
    where trace data must not be silently dropped (fault-tolerance guarantee from
    Claim 3).
  - Document artifact-based span inspection (`agent` artifact → `otel.jsonl`)
    as the day-1 operational debugging workflow before OTLP infrastructure is
    established — traces are already captured in artifacts even without a backend.

## Extraction Notes

1. **Source is a reference page, not a guide page**: The `reference/` section
   of `github.github.com/gh-aw/` documents authoritative platform behavior
   with explicit field names, parameter types, and example configurations. This
   page is dense with technical detail (YAML configs, env var tables, API
   signatures) rather than extended prose explanation.

2. **Two WebFetch passes**: The source was fetched twice — a summary pass and
   a verbatim-detail pass targeting specific sections. Full technical content
   was obtained on both passes with consistent results. No sub-pages were
   linked; this is a self-contained reference page.

3. **GenAI span attribute conventions**: The page cites "OpenTelemetry GenAI
   semantic conventions" — this is an emerging CNCF specification for
   standardizing LLM observability across vendors. The `confidence_overall`
   is `emerging` rather than `settled` because the GenAI convention spec is
   still under active development, which means attribute names may evolve
   as the spec matures.

4. **`key` redaction pattern is intentionally broad**: The security
   sanitization section's `key` pattern (Claim 9) will match attribute
   names like `cache_key`, `partition_key`, `primary_key` — any name
   containing "key" as a substring. Teams adding custom span attributes
   should avoid the word "key" in attribute names unless the value genuinely
   requires redaction.

5. **No contradictions found**: Reviewed `blog-ghaw-agent-observability.md`,
   `docs-ghaw-monitoring-patterns.md`, `docs-ghaw-artifacts-reference.md`,
   `docs-ghaw-audit-with-agents.md`, and `docs-ghaw-how-they-work.md`. No
   claims in this source materially oppose existing source notes at the
   MINER.md §4a filing threshold. The OTLP instrumentation layer is
   entirely new material to the corpus.
