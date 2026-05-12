---
source_url: https://github.github.com/gh-aw/reference/awf-reflect
source_type: docs
title: "GitHub Agentic Workflows: AWF Reflect Route Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#697"
---

# GitHub Agentic Workflows: AWF Reflect Route Reference

> The canonical reference for the AWF `/reflect` endpoint — a runtime API for
> discovering configured inference providers and available models, enabling shared
> workflows and tools to route inference dynamically rather than hardcoding upstream
> model URLs.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/awf-reflect` page —
  in the "Reference" section alongside `reference/tools`, `reference/network`,
  `reference/sandbox`. This is the primary and only reference page for the
  `/reflect` endpoint. Linked from the Cost Management and MCP Gateway references.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's agent factory blog series and the `gh aw` CLI.
  Endpoint specifications, field names, and behavioral guarantees are authoritative
  for the gh-aw platform.
- **Scope**: The AWF `/reflect` endpoint exclusively — its purpose, response schema,
  recommended selection algorithm, and retry protocol. Does NOT cover: the MCP
  gateway configuration in depth (see `docs-ghaw-mcps.md`), network egress controls
  (see `docs-ghaw-network-reference.md`), model alias definitions, cost management
  commands, or how the gateway proxies inference (see MCP Gateway reference).

## Extracted Claims

### Claim 1: The AWF API proxy exposes a `GET /reflect` endpoint at `http://api-proxy:10000/reflect` for runtime model routing inside the AWF network

- **Evidence**: The opening sentence of the reference page states this precisely,
  naming both the HTTP method and the internal hostname/port.
- **Confidence**: settled (first-party reference specification; the endpoint address
  is an authoritative platform fact)
- **Quote**: "Inside the AWF runtime network, the AWF API proxy exposes `GET /reflect` at `http://api-proxy:10000/reflect`. Use this route when building shared workflows, tools, or extensions that need runtime model routing."
- **Our assessment**: The `api-proxy:10000` hostname is an internal DNS name within
  the AWF runtime network — it is not accessible from outside workflow execution.
  This is the same proxy whose logs appear in `firewall-audit-logs/api-proxy-logs/`
  (see `docs-ghaw-artifacts-reference.md` Claim 4). The endpoint is specifically
  scoped to "shared workflows, tools, or extensions" — the phrasing implies it is
  most valuable for reusable components that must work across different deployment
  environments rather than single-purpose workflows with hardcoded model preferences.

### Claim 2: `/reflect` provides four runtime capabilities: endpoint discovery, configuration status, model availability, and dynamic provider/model selection

- **Evidence**: The "Why Use /reflect" section enumerates these capabilities as a
  bulleted list under the statement that the endpoint "returns the currently
  configured inference providers and their model availability for the active run."
- **Confidence**: settled (first-party documentation; the four capabilities are
  explicitly listed)
- **Quote**: "`/reflect` returns the currently configured inference providers and their model availability for the active run. This allows a shared workflow or tool to: Discover which gateway endpoints are available, Check whether each endpoint is configured, Read or refresh model availability, Select a provider/model dynamically at runtime"
- **Our assessment**: The "Read or refresh model availability" capability implies
  `/reflect` can be called multiple times during a run — not just at startup. This
  matters for long-running workflows where model availability may change or where
  the startup race condition (see Claim 5) requires a retry loop. Dynamic
  provider/model selection is the highest-value use case: a shared tool that
  selects between OpenAI, Anthropic, and Gemini based on what's configured in the
  deployment environment gains environment portability without code changes.

### Claim 3: Practitioners must not hardcode direct upstream model API URLs in shared workflow logic — all inference must go through the AWF gateway for cost control and observability

- **Evidence**: A Caution callout on the page states this explicitly as a
  prohibition, giving three reasons: cost control, tracking, and optimization.
- **Confidence**: settled (first-party documentation; the prohibition is stated as
  a Caution callout — the strongest warning level used in GHAW docs)
- **Quote**: "Do not hardcode direct upstream model API URLs in shared workflow logic. All inference requests should go through the AWF gateway so usage remains controllable and observable for cost control, tracking, and optimization."
- **Our assessment**: This is the most operationally important claim on the page.
  The AWF gateway is not just a convenience layer — routing through it is what
  enables the cost tracking documented in the Cost Management reference
  (`gh aw logs` per-run token metrics, `gh aw audit <run-id>` cost breakdowns).
  Bypassing the gateway by hardcoding `api.anthropic.com` or `api.openai.com`
  would make inference costs invisible to the AWF cost tooling and would break
  the per-run attribution model. For Ch06 (Observability and Cost): this is a
  concrete architectural constraint, not merely a recommendation — bypassing it
  breaks the cost observability stack.

### Claim 4: The `/reflect` response schema contains six fields — `endpoints[].provider`, `endpoints[].base_url`, `endpoints[].configured`, `endpoints[].models` (nullable), `endpoints[].models_url`, and top-level `models_fetch_complete`

- **Evidence**: The "Response Shape" section lists all six fields with their types
  and descriptions.
- **Confidence**: settled (first-party specification; field names and semantics are
  authoritative)
- **Quote**: "The response includes an `endpoints` array and a `models_fetch_complete` flag: `endpoints[].provider`: provider identifier (e.g., `openai`, `anthropic`, `copilot`, `gemini`) / `endpoints[].base_url`: gateway base URL for inference calls / `endpoints[].configured`: whether credentials/config are present for that provider / `endpoints[].models`: discovered model IDs, or `null` when model discovery is not yet complete / `endpoints[].models_url`: gateway URL used to query models for that provider / `models_fetch_complete`: whether startup model discovery is complete"
- **Our assessment**: The `configured` field is the correct first-pass filter —
  an unconfigured provider has no credentials, so routing to it will fail regardless
  of model availability. The `models` field is nullable specifically to handle the
  startup race condition (see Claim 5). The `models_url` field provides an
  alternative path for model querying that doesn't depend on the cached `models`
  array — useful when a workflow needs the authoritative model list rather than
  the discovery snapshot. Four named providers are documented: openai, anthropic,
  copilot, gemini — a practitioner can use this to reason about the possible
  `provider` values they'll see in the response.

### Claim 5: The `models_fetch_complete` flag signals whether startup model discovery has finished — it exists to handle the race condition where a workflow begins executing before the gateway completes model enumeration

- **Evidence**: The field is described as "whether startup model discovery is
  complete" in the response schema. The selection algorithm (Claim 6) references
  it via the `models` null check: "If `models` is `null`, retry discovery with
  bounded backoff." The `models_fetch_complete` flag and nullable `models` together
  are the documented mechanism for this race condition.
- **Confidence**: emerging (the race condition is implicit in the design rather
  than explicitly named; inferred from the combination of the flag and the null
  check in the algorithm)
- **Quote**: (no direct quote naming "race condition"; see schema quote in Claim 4
  and selection flow quote in Claim 6)
- **Our assessment**: The startup race condition is a real operational concern for
  workflows with fast triggers (e.g., `push` or `issue_comment`). The gateway
  performs model discovery asynchronously at startup — a workflow that starts
  querying /reflect immediately may see `models: null` with `models_fetch_complete:
  false` even when the gateway is healthy. The correct behavior (retry with backoff,
  per Claim 6) should be the default implementation pattern for any shared tool
  that calls /reflect. Practitioners who treat `models: null` as a hard failure
  will see spurious errors on fast-start workflows.

### Claim 6: The recommended selection flow is a 6-step algorithm — query, filter configured, prefer non-empty models, match aliases, route to base_url, retry with backoff if null

- **Evidence**: The "Recommended Selection Flow" section enumerates all six steps
  as a numbered list.
- **Confidence**: settled (first-party prescriptive guidance; this is the
  canonical algorithm from the platform documentation)
- **Quote**: "1. Query `/reflect` at start of execution. 2. Filter endpoints to `configured: true`. 3. Prefer endpoints with a non-empty `models` list. 4. Match requested model aliases/patterns against available models. 5. Route inference to the selected endpoint `base_url`. 6. If `models` is `null`, retry discovery with bounded backoff (for example, every 3 seconds up to 5 attempts) before failing."
- **Our assessment**: The algorithm is a portable decision procedure that any
  shared workflow tool can implement verbatim. Key nuances: Step 3 uses "prefer"
  not "require" — an endpoint that is `configured: true` but has `models: null`
  is still usable (via its `models_url`), just less ideal. Step 4 references
  "model aliases/patterns" which connects to the Model Aliases reference (linked
  from the page) — shared tools should accept model alias strings (e.g., "claude-sonnet")
  rather than exact model IDs to benefit from the alias layer. Step 6's "before
  failing" is important: the algorithm specifies that null models should trigger
  retries, not immediate failure. For Ch04 (Tools and Integrations): this
  6-step algorithm should be presented as the reference implementation for
  portable shared tool model routing.

### Claim 7: The retry backoff specification is bounded — "every 3 seconds up to 5 attempts" — not open-ended

- **Evidence**: Step 6 of the selection flow names the specific parameters: "retry
  discovery with bounded backoff (for example, every 3 seconds up to 5 attempts)
  before failing."
- **Confidence**: emerging (the "for example" qualifier means these are reference
  values, not hard platform requirements)
- **Quote**: "retry discovery with bounded backoff (for example, every 3 seconds up to 5 attempts) before failing"
- **Our assessment**: The "for example" framing is notable — the 3s/5-attempt values
  are illustrative, not mandatory. This gives implementers latitude to tune based
  on their workflow's latency requirements. However, the bounded constraint IS
  normative: retry must have an upper limit. Open-ended retries would violate the
  anti-runaway principles documented in `docs-ghaw-rate-limiting-controls.md`
  (Claim 1). For Ch02 (Harness Engineering): when implementing /reflect clients,
  use bounded backoff aligned with the workflow's overall `timeout:` setting.
  A workflow with a 5-minute timeout should not spend more than 30-45 seconds
  waiting for model discovery.

## Concrete Artifacts

**AWF API endpoint (from source):**
```
GET http://api-proxy:10000/reflect
```

**Example request (from source):**
```bash
curl -s http://api-proxy:10000/reflect
```

**Response schema (from source):**
```
{
  "endpoints": [
    {
      "provider": "openai" | "anthropic" | "copilot" | "gemini",
      "base_url": "<gateway base URL for inference calls>",
      "configured": true | false,
      "models": ["<model-id>", ...] | null,
      "models_url": "<gateway URL for model queries>"
    },
    ...
  ],
  "models_fetch_complete": true | false
}
```

**Recommended selection algorithm (from source, verbatim):**
```
1. Query /reflect at start of execution.
2. Filter endpoints to configured: true.
3. Prefer endpoints with a non-empty models list.
4. Match requested model aliases/patterns against available models.
5. Route inference to the selected endpoint base_url.
6. If models is null, retry discovery with bounded backoff
   (for example, every 3 seconds up to 5 attempts) before failing.
```

**Caution (from source, verbatim):**
```
Do not hardcode direct upstream model API URLs in shared workflow logic.
All inference requests should go through the AWF gateway so usage remains
controllable and observable for cost control, tracking, and optimization.
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-artifacts-reference.md` Claim 4: The `api-proxy-logs/` path in the
    `firewall-audit-logs` artifact confirms that `api-proxy:10000` is real
    infrastructure that logs all inference traffic — consistent with the cost
    observability claims in Claim 3 above.
  - `docs-ghaw-how-they-work.md` Claim 4: The "no write access by default"
    zero-capability principle is mirrored by /reflect being a read-only discovery
    endpoint — it observes what's available rather than modifying configuration.
  - `docs-ghaw-rate-limiting-controls.md` Claim 1: The bounded retry specification
    in Claim 7 (max 5 attempts) aligns with the defense-in-depth anti-runaway
    philosophy — no open-ended loops in the platform design.

- **Contradicts**: None identified. The /reflect endpoint is additive documentation
  not previously covered by any existing source note.

- **Extends**:
  - `docs-ghaw-mcps.md`: Extends understanding of the AWF gateway layer — /reflect
    exposes the inference proxy side (which providers are behind the gateway) while
    `docs-ghaw-mcps.md` covers the MCP tool side. Together they document both
    halves of the api-proxy.
  - `docs-ghaw-inline-sub-agents.md` Claim 4: Per-sub-agent model selection is
    static (declared in frontmatter, defaults to parent model). `/reflect` provides
    the runtime dynamic complement — selecting from what's actually configured and
    available, rather than what's declared. The two patterns address different
    scopes: intra-workflow static selection vs. inter-environment dynamic routing.
  - `docs-ghaw-tools-reference.md` Claim 1: Import-merge semantics enable shared
    tool libraries; /reflect is what makes those shared tools portable — by
    discovering available models at runtime, shared tools avoid being tied to
    provider configurations specific to the deployment environment.
  - `docs-ghaw-network-reference.md`: Gateway routing as an observability mechanism
    is consistent with the firewall/audit tooling documented there. The AWF gateway
    is Layer 4 (network controls) and Layer 6 (cost observability) simultaneously.

- **Novel**:
  - The `/reflect` endpoint itself is completely new to the corpus — no existing
    source note documents this API or its response schema.
  - The 6-step selection algorithm with specific retry/backoff parameters is the
    first concrete model-routing algorithm documented in the corpus.
  - The `models_fetch_complete` startup race condition handling pattern is novel —
    no existing note addresses the gap between workflow start and gateway model
    discovery completion.
  - The explicit prohibition on hardcoding upstream model URLs (Claim 3) is the
    first stated architectural constraint on how inference should be routed in gh-aw.

## Guide Impact

- **Chapter 04 (Tools and Integrations)**: Add the 6-step /reflect selection
  algorithm as the reference implementation pattern for portable shared tools
  that need dynamic model routing. Currently no chapter content addresses how
  shared tools should discover and route to available providers at runtime. This
  source fills that gap with a concrete, first-party algorithm.

- **Chapter 06 (Observability and Cost)**: Add Claim 3's "no hardcoded upstream
  URLs" constraint as an architectural requirement for cost observability — bypassing
  the gateway makes inference invisible to `gh aw logs` and `gh aw audit`. Connects
  to the `api-proxy-logs/token-usage.jsonl` artifact documented in
  `docs-ghaw-artifacts-reference.md`.

- **Chapter 02 (Harness Engineering)**: The /reflect pattern is the correct approach
  for shared workflow components that need environment portability. A shared tool
  library configured once but deployed across multiple repos (each with different
  provider configurations) needs runtime discovery, not static frontmatter. Add
  /reflect as a harness engineering primitive for multi-environment shared components.

- **Chapter 03 (Agent Design)**: The startup race condition handling (Claim 5) and
  bounded retry protocol (Claim 7) are concrete examples of defensive agent
  implementation — agents must be designed to handle infrastructure not being
  immediately ready, with bounded rather than open-ended wait loops.

## Extraction Notes

The source page is compact (~400 words) but technically dense. I followed the two
linked pages (Cost Management and MCP Gateway) to provide additional context for
the cross-references. A third linked page (Model Aliases & Multipliers) returned
HTTP 404. The "for example" qualifier on the retry parameters (Claim 7) is present
in the source and is captured accurately — the values are illustrative, not
mandatory. The page was fully readable with no paywall or authentication requirement.
