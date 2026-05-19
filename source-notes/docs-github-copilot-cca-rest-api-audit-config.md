---
source_url: https://github.blog/changelog/2026-05-18-audit-repository-copilot-cloud-agent-configuration-via-the-rest-api
source_type: docs
title: "Audit repository Copilot cloud agent configuration via the REST API"
author: GitHub (official changelog)
date_published: 2026-05-18
date_extracted: 2026-05-19
last_checked: 2026-05-19
status: current
confidence_overall: settled
issue: "#807"
---

# Audit Repository Copilot Cloud Agent Configuration via the REST API

> GitHub's May 2026 announcement of a "Get Copilot cloud agent configuration for
> a repository" REST API (public preview, API version 2026-03-10) adds a programmatic
> query path for reading a repository's CCA configuration state — including MCP server
> configuration, enabled tools, GitHub Actions workflow policy, and firewall
> configuration — enabling security posture auditing across many repositories at scale.

## Source Context

- **Type**: docs (GitHub official product changelog, May 18, 2026, ~150 words, "1 minute
  read")
- **Author credibility**: GitHub engineering team announcing a production feature in
  public preview. Authoritative for the existence of the endpoint, the stated fields
  it returns, and the API version. Not a credible source for completeness of the
  returned schema (the linked API reference documentation contains the full field
  definitions), for performance characteristics of bulk auditing, or for outcomes of
  organizations that have deployed this audit workflow.
- **Scope**: The existence and stated purpose of the "Get Copilot cloud agent
  configuration for a repository" REST API. The four named categories of returned
  data (MCP server configuration, enabled tools, GitHub Actions workflow policy,
  firewall configuration). The security-posture-at-scale use case. Does NOT cover:
  the specific request/response schema (those are in the linked API documentation),
  authentication requirements, subscription-tier eligibility, rate limits, how the
  returned fields map to the governance settings managed by the enterprise API
  documented in `docs-github-copilot-cca-custom-properties.md`, or whether the
  returned configuration reflects live state or a cached snapshot.

## Extracted Claims

### Claim 1: A new "Get Copilot cloud agent configuration for a repository" REST API endpoint enables programmatic auditing of CCA configuration, in public preview as of May 18, 2026

- **Evidence**: Official GitHub product changelog announcing the feature with explicit
  public-preview status and API version 2026-03-10.
- **Confidence**: settled (product fact — the endpoint exists and is documented)
- **Quote**: (no direct quote; see paraphrase in Our assessment — the WebFetch layer
  produced consistent paraphrase across three independent fetches but did not return
  the opening sentence verbatim; Assayer should verify the exact wording against the
  live URL)
- **Our assessment**: The announcement states that users can now programmatically audit
  a repository's Copilot cloud agent configuration using this new endpoint. This is a
  read-only configuration query API, not a task invocation API — it complements the
  May 13, 2026 Agent tasks REST API (`docs-github-copilot-cca-rest-api-tasks.md`)
  by addressing the "what is CCA configured to do?" question rather than the
  "start a CCA task" action. The public preview status and `apiVersion=2026-03-10`
  constraint mean practitioners should pin the version header and monitor for GA
  announcement before building production tooling on this endpoint.

### Claim 2: The API returns four categories of CCA configuration data: MCP server configuration, enabled tools, GitHub Actions workflow policy, and firewall configuration

- **Evidence**: Four configuration categories are explicitly named in the changelog.
  These are the only fields the announcement names; the full schema is in the linked
  API documentation.
- **Confidence**: settled (explicitly listed in official changelog)
- **Quote**: "MCP server configuration, enabled tools, GitHub Actions workflow policy,
  and firewall configuration"
- **Our assessment**: These four categories cover the main axes of CCA's operational
  footprint: (1) what external services it can reach (MCP server configuration),
  (2) what internal capabilities it can use (enabled tools), (3) what workflow
  constraints apply (GitHub Actions workflow policy), and (4) what network-level
  controls are in place (firewall configuration). Together they constitute a fairly
  complete picture of a repository's CCA security surface. Notably, the firewall
  configuration field implies CCA has per-repository network-level controls that
  have not been documented in any prior corpus source — this is new signal. The MCP
  server configuration field directly addresses the footgun documented in
  `docs-github-copilot-cca-custom-properties.md` Claim 6: since Copilot MCP Registry
  URL and Restrict MCP Access policies do NOT apply to CCA, there was previously no
  easy way to audit what MCP servers CCA was actually connecting to. This API closes
  that gap.

### Claim 3: The primary use case is understanding and auditing the security posture of repositories at scale

- **Evidence**: Stated explicitly in the changelog as the motivation for the feature.
- **Confidence**: settled (stated rationale in official product announcement)
- **Quote**: "understand and audit the security posture of your repositories at scale"
- **Our assessment**: The "at scale" framing is the operative signal. A single-repo
  configuration inspection is trivial via the GitHub UI; the REST API enables
  programmatic enumeration across many repositories — an org-wide or enterprise-wide
  configuration audit that would be impractical through the UI. This use case complements
  the governance API documented in `docs-github-copilot-cca-custom-properties.md`:
  the governance API controls *which repos* have CCA enabled and at what policy level;
  the audit API answers *what is CCA configured to do* in each of those repos. Together
  they enable a complete governance loop: enable → configure → audit.

### Claim 4: The configuration audit API is a read-only query endpoint, distinct from the task invocation API released five days earlier

- **Evidence**: The announcement describes the endpoint as providing information about
  existing configuration state, not invoking or managing tasks. The endpoint name
  "Get Copilot cloud agent configuration for a repository" uses the HTTP GET verb
  semantics (read-only) in its name.
- **Confidence**: emerging (the GET-semantics inference from the endpoint name is
  reasonable but the HTTP method is not explicitly stated in the changelog — the
  linked API documentation would be definitive)
- **Quote**: (no direct quote; the read-only nature is implied by the endpoint name
  and the "audit" framing throughout the announcement)
- **Our assessment**: Treating this as a read/query endpoint is the correct
  interpretation — "audit" and "understand" language throughout implies inspection
  of existing state, not mutation. This makes it architecturally distinct from the
  Agent tasks REST API (`docs-github-copilot-cca-rest-api-tasks.md`), which starts
  tasks (write/action). Enterprise practitioners should design audit scripts that
  call this endpoint frequently (e.g., nightly configuration drift checks) without
  concern for triggering CCA tasks — the two APIs are independent capabilities.

### Claim 5: The MCP server configuration field in the API response makes the MCP policy exemption footgun operationally detectable

- **Evidence**: The changelog explicitly lists "MCP server configuration" as one of
  the four returned data categories. The MCP policy exemption is documented in
  `docs-github-copilot-cca-custom-properties.md` Claim 6.
- **Confidence**: emerging (the inference that this field addresses the footgun is
  analytical synthesis — the changelog does not make this connection explicitly)
- **Quote**: (no direct quote for this synthesis claim; see Our assessment)
- **Our assessment**: `docs-github-copilot-cca-custom-properties.md` Claim 6
  establishes that the standard Copilot MCP Registry URL and Restrict MCP Access
  policies do NOT apply to CCA — a security footgun for enterprises that rely on
  those policies to control external service access. Previously, verifying what MCP
  servers CCA was connecting to required manual UI inspection per repository.
  The MCP server configuration field in this new API response means that a compliance
  team can now programmatically enumerate MCP server configurations across all
  CCA-enabled repositories in an org, identify unauthorized or unexpected MCP server
  registrations, and detect configuration drift over time. This is a meaningful
  closing of a previously noted security gap. Guide sections documenting the MCP
  exemption footgun should reference this audit API as the mitigation path.

### Claim 6: The firewall configuration field reveals that CCA has per-repository network-level controls

- **Evidence**: "Firewall configuration" is one of the four explicitly named fields
  in the API response.
- **Confidence**: emerging (the existence of a firewall configuration field implies
  per-repo network controls, but the specific semantics — what constitutes a "firewall
  configuration" for CCA, and whether it's the same firewall referenced in general
  CCA documentation — are not explained in this changelog and must be inferred from
  the linked API documentation)
- **Quote**: (no direct quote for this inference; "firewall configuration" is listed
  as one of the four return fields)
- **Our assessment**: No prior corpus source documents per-repository firewall
  configuration for CCA. The presence of this field suggests CCA has some form of
  outbound or inbound network policy at the repo level — possibly restricting what
  external hosts CCA can reach from its cloud development environment. This is
  entirely new to the corpus. Security teams should consult the API documentation
  to understand the semantics of this field before building compliance rules around
  it. If CCA's firewall configuration can be compared across repos, it becomes a
  valuable consistency check — repos with permissive firewall settings can be
  flagged for review.

### Claim 7: The enabled-tools and GitHub Actions workflow policy fields support compliance verification of CCA capability scope

- **Evidence**: Both "enabled tools" and "GitHub Actions workflow policy" are named
  in the four returned configuration categories.
- **Confidence**: emerging (inference from field names — the changelog does not
  describe the semantics of these fields in detail)
- **Quote**: (no direct quote for this synthesis; the field names are directly listed)
- **Our assessment**: "Enabled tools" implies CCA has a per-repository tool access
  list (likely controlling which of CCA's built-in capabilities — file editing,
  terminal, browser, etc. — are permitted in that repo). "GitHub Actions workflow
  policy" implies a per-repository control over whether CCA can trigger or interact
  with GitHub Actions workflows. For enterprises concerned about CCA modifying CI/CD
  pipelines without approval, the workflow policy field is particularly relevant —
  it can be audited to confirm CCA's workflow access is appropriately restricted
  across all repos. Together, the four API fields form a security-relevant
  configuration inventory that supports both point-in-time snapshots and over-time
  drift detection.

## Concrete Artifacts

### CCA Configuration Audit API — Key Facts (from changelog, May 18, 2026)

```
Title:     Audit repository Copilot cloud agent configuration via the REST API
Published: 2026-05-18 (public preview)
API version: 2026-03-10

Endpoint name: Get Copilot cloud agent configuration for a repository
Operation type: Read/query (audit, not invocation)

Configuration fields returned (four categories, from announcement):
  1. MCP server configuration
  2. Enabled tools
  3. GitHub Actions workflow policy
  4. Firewall configuration

Primary use case (per announcement):
  "understand and audit the security posture of your repositories at scale"

Relationship to other CCA REST APIs (same API version 2026-03-10):
  May 13, 2026 — Agent tasks REST API: START a CCA task (invocation)
  May 18, 2026 — Configuration audit REST API: READ CCA config state (query)
```

### Enterprise CCA Observability Suite (synthesized from corpus, 2026-05-19)

```
Complete enterprise CCA observability, as of May 2026:

Layer 1 — Governance (who has CCA access)
  Source: docs-github-copilot-cca-custom-properties.md
  API:    PUT /enterprises/{enterprise}/copilot/policies/coding_agent
          POST/DELETE /enterprises/{enterprise}/copilot/policies/coding_agent/organizations
  Answers: Which orgs have CCA enabled? Under what policy?

Layer 2 — Usage (who is using CCA)
  Source: docs-github-copilot-cca-usage-metrics-aggregate.md
  API:    Copilot usage metrics API (enterprise + org level)
          Fields: copilot_cloud_agent_active_users_1_day / 7_day / 28_day
  Answers: How many users are actively using CCA? Trend over time?

Layer 3 — Configuration (what is CCA configured to do)
  Source: THIS NOTE (docs-github-copilot-cca-rest-api-audit-config.md)
  API:    Get Copilot cloud agent configuration for a repository
          (apiVersion=2026-03-10, public preview)
  Returns: MCP server config, enabled tools, workflow policy, firewall config
  Answers: What is CCA permitted to access and do in each repo?

Full governance loop:
  Enable (Layer 1) → Use (Layer 2) → Audit configuration (Layer 3)
  → Detect drift → Re-configure → Repeat
```

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-cca-custom-properties.md` Claim 3 (three enterprise-level
    API endpoints provide programmatic CCA management): Both sources document the
    pattern of REST API exposure for CCA operational concerns. The custom-properties
    note covers management-plane APIs (enable/disable CCA); this source covers a
    data-plane query API (read CCA configuration state). The API version is the same
    (`2026-03-10`) for both, confirming a unified REST API versioning approach for
    CCA enterprise features.

- **Extends**:
  - `docs-github-copilot-cca-rest-api-tasks.md` Claim 1 (Agent tasks REST API enables
    programmatic CCA task invocation, public preview): This source adds a second
    distinct REST API surface for CCA — configuration query — alongside the task
    invocation API. Together they form the two sides of CCA's REST API: invocation
    (tasks API) and observation (configuration audit API). The "public preview" status
    and `apiVersion=2026-03-10` are consistent between both APIs.
  - `docs-github-copilot-cca-custom-properties.md` Claim 6 (MCP Registry URL and
    Restrict MCP Access policies do NOT apply to Copilot Cloud Agent): The MCP server
    configuration field in this audit API is the operational mechanism for detecting
    and remediating the MCP exemption footgun. The custom-properties note documents
    the gap; this note provides the detection tool. Guide sections citing Claim 6
    should add a cross-reference here as the mitigation.
  - `docs-github-copilot-cca-usage-metrics-aggregate.md` Claim 1 (aggregate
    CCA active-user-count fields in the usage metrics API): The usage metrics API and
    the configuration audit API together form two layers of a complete enterprise CCA
    observability stack. The metrics API answers "how much CCA usage?" and the
    configuration API answers "what is CCA permitted to do?" A mature enterprise
    governance program needs both. The "Concrete Artifacts → Enterprise CCA
    Observability Suite" section above synthesizes all three layers.
  - `docs-github-copilot-cca-startup-custom-images.md` (CCA execution environment):
    The firewall configuration field in this audit API implies per-repository network
    controls on the CCA execution environment. That note documents the startup
    environment (custom container images); this source adds evidence that the runtime
    environment also has auditable network-level controls.

- **Contradicts**: None identified. This is a new capability announcement that adds
  a REST API query surface with no prior claims in the corpus to contradict. No
  contradiction issue filed.

- **Novel**:
  - **Repository-level CCA configuration as a queryable REST API resource**: No prior
    corpus source documents a programmatic API for reading CCA configuration state
    at the repository level. All prior configuration-related sources cover management
    APIs (setting policy) or UI inspection.
  - **Firewall configuration as a per-repository CCA attribute**: No prior source
    documents per-repository firewall configuration for CCA. The presence of this
    field implies CCA has repository-scoped network controls that have not been
    previously described.
  - **Security posture auditing at scale as an explicit CCA use case**: Prior sources
    treat CCA governance as an enable/disable concern (which orgs get access). This
    source frames configuration auditing — checking what CCA is configured to *do*
    across many repos — as a first-class enterprise use case.
  - **Two-API REST surface for CCA (invocation + configuration query)**: The
    combination of the May 13 tasks API and this May 18 configuration API establishes
    CCA's REST API as having two distinct surfaces. This taxonomy (invocation vs.
    observation) is new to the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering — CCA Integration Patterns)**:
  - Add the configuration audit API to the CCA REST API taxonomy documented in
    `docs-github-copilot-cca-rest-api-tasks.md`. The taxonomy should now include:
    (a) task invocation (Agent tasks API, May 13), and (b) configuration query
    (this API, May 18). Document that these are independent capabilities on the
    same API version.
  - Note the `apiVersion=2026-03-10` requirement and the public-preview status.
    Any harness that uses the configuration audit API for compliance checks should
    pin the version and monitor for GA.

- **Chapter 06 (Safety & Security)**:
  - Add the configuration audit API as the primary mechanism for detecting CCA
    security posture misconfigurations. Specifically: use the MCP server
    configuration field to verify CCA's MCP access (closing the MCP exemption
    gap from `docs-github-copilot-cca-custom-properties.md` Claim 6), use the
    firewall configuration field to verify network-level controls, and use the
    enabled-tools field to confirm CCA's capability scope matches organizational
    policy.
  - Add "nightly CCA configuration audit" as a concrete security operations
    pattern: script a call to this API for each CCA-enabled repository, compare
    results against a baseline, alert on drift.

- **Chapter 07 (Enterprise Operations — CCA Governance and Audit)**:
  - Add the three-layer CCA observability stack (governance API → usage metrics
    API → configuration audit API) as the complete enterprise CCA operational
    framework. Each layer answers a distinct governance question; a mature
    deployment requires all three.
  - Reference the MCP server configuration field as the closure path for the
    MCP policy exemption footgun: configure enterprise MCP policy as desired,
    verify actual CCA MCP server configuration via this API, detect and remediate
    mismatches programmatically.
  - Add "cross-repository configuration inventory" as an enterprise pattern:
    enumerate all CCA-enabled repos (via governance API), query each repo's
    configuration (via this API), build an inventory, and enforce consistency
    policies (e.g., all production repos must have firewall configuration X).

## Extraction Notes

1. **Very brief source (~150 words)**: The changelog is a short announcement
   like the May 13, 2026 Agent tasks REST API entry. The full technical schema
   (endpoint path, HTTP method, request headers, response body, authentication
   requirements, rate limits) is in the linked API documentation, which was not
   separately fetched. A source note for that documentation page would be high-value
   for practitioners building configuration audit tooling.

2. **Quote verbatim accuracy**: Three independent WebFetch calls were made to the
   source URL. The quote "understand and audit the security posture of your
   repositories at scale" appeared consistently in quotation marks across two of
   the three fetches and is presented as verbatim. The four configuration fields
   ("MCP server configuration, enabled tools, GitHub Actions workflow policy, and
   firewall configuration") appeared in quotation marks in one fetch. Other claims
   are marked `(no direct quote; see paraphrase in Our assessment)` per MINER.md §2a.
   The Assayer should spot-check the core quotes against the live URL.

3. **No contradictions filed**: All claims are additive to existing corpus notes.
   The MCP server configuration field closes a previously identified security gap
   (documented in `docs-github-copilot-cca-custom-properties.md` Claim 6) — this
   is resolution, not contradiction.

4. **Public preview caveat**: As with the May 13 Agent tasks API, this endpoint is
   in public preview as of its announcement. Breaking changes before GA are possible.
   Any guide advice citing specific behavior derived from the API documentation
   should note the public preview status.

5. **Linked API documentation not fetched**: The announcement links to API reference
   documentation that would contain the endpoint path, authentication requirements,
   and complete response schema. These details are not in this source note.
   A high-priority follow-up extraction would be the linked API reference page,
   which would fill in the concrete technical parameters the changelog intentionally
   omits.
