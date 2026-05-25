---
source_url: https://github.blog/changelog/2026-05-18-audit-repository-copilot-cloud-agent-configuration-via-the-rest-api
source_type: docs
title: "Audit repository Copilot cloud agent configuration via the REST API"
author: GitHub (official changelog)
date_published: 2026-05-18
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: settled
issue: "#807"
---

# Audit Repository Copilot Cloud Agent Configuration via the REST API

> GitHub's May 18, 2026 changelog announces a "Get Copilot cloud agent configuration for a repository" REST API (public preview) that returns per-repository CCA configuration — MCP server config, enabled tools, GitHub Actions workflow policy, and firewall settings — enabling security posture auditing across repositories at scale.

## Source Context

- **Type**: docs (GitHub official product changelog, May 18, 2026, ~3 sentences of body text)
- **Author credibility**: GitHub engineering team announcing a production feature in public preview. Authoritative for the existence of the API and the four stated returned fields. Not a credible source for API endpoint path, authentication requirements, access tier restrictions, rate limits, or response schema — those details are absent from this changelog and presumably in API reference documentation that is not linked.
- **Scope**: The existence and basic capabilities of the CCA configuration audit REST API, four configuration categories returned, and the stated use case (security posture auditing at scale). Does NOT cover: endpoint path, request parameters, authentication requirements, access tier restrictions (Business/Enterprise vs. Pro — not stated), rate limits, response schema, or how this API interacts with the enterprise-level CCA management API.

## Extracted Claims

### Claim 1: A new "Get Copilot cloud agent configuration for a repository" REST API in public preview enables programmatic auditing of CCA repository configuration

- **Evidence**: Official GitHub product changelog announcing the feature. The "public preview" qualifier signals the API surface may change before GA.
- **Confidence**: settled (product fact — the API exists and is announced by the authoritative source)
- **Quote**: "You can now programmatically audit a repository's Copilot cloud agent configuration with the new Get Copilot cloud agent configuration for a repository REST API, available in public preview."
- **Our assessment**: The new API is a *configuration audit* (read) endpoint, not a task execution (write) endpoint — it reads state rather than triggering action. This makes it a distinct capability from `docs-github-copilot-cca-rest-api-tasks.md` Claim 1 (which triggers task execution). Together, the two REST APIs announced in May 2026 (task invocation May 13, configuration audit May 18) give practitioners a more complete programmatic CCA interface. For Ch02 (Harness Engineering): extend the CCA REST API taxonomy to include this configuration-reading path alongside the task-invocation path. For Ch06 (Safety & Security): document this as the first explicit security-posture audit API for CCA.

### Claim 2: The API returns four categories of CCA configuration: MCP server configuration, enabled tools, GitHub Actions workflow policy, and firewall configuration

- **Evidence**: Explicit list of returned fields stated in the changelog. The word "including" suggests this may be a partial list.
- **Confidence**: settled (field categories stated directly in official changelog)
- **Quote**: "The new API returns details about a repository's Copilot cloud agent setup, including its MCP server configuration, enabled tools, GitHub Actions workflow policy, and firewall configuration."
- **Our assessment**: All four fields are security-relevant and address enterprise governance concerns:
  - **MCP server configuration**: What external MCP servers is CCA configured to use for this repo? Directly addresses the governance gap in `docs-github-copilot-cca-custom-properties.md` Claim 6 — MCP Registry URL and Restrict MCP Access policies do not apply to CCA. Per-repo MCP configuration is now auditable.
  - **Enabled tools**: Which tools/capabilities are available to the CCA agent for this repo? Affects the agent's capability surface and blast radius.
  - **GitHub Actions workflow policy**: What workflow permissions govern CCA's Actions execution? Affects CCA's ability to trigger downstream workflows.
  - **Firewall configuration**: What network egress restrictions are in place? Affects CCA's network access scope — a key enterprise security concern.
  The "including" language (rather than "consisting of") suggests additional fields may be present in the response. For Ch06/Ch07: these four fields map directly to the key security audit questions enterprises should ask about their CCA setup.

### Claim 3: The API enables auditing CCA security posture at scale — across multiple repositories, not just per-repository debugging

- **Evidence**: GitHub's stated purpose in the changelog: the API "makes it easy to understand and audit the security posture of your repositories at scale."
- **Confidence**: emerging (use case is vendor-stated; no empirical data on adoption or effectiveness of this audit pattern in practice)
- **Quote**: "This makes it easy to understand and audit the security posture of your repositories at scale."
- **Our assessment**: The "at scale" framing positions this as a multi-repository compliance inventory tool, not a per-repository debug tool. An enterprise with hundreds of CCA-enabled repositories can now script a sweep: which repos have external MCP servers configured? Which have permissive firewall settings? Which have unexpected tool configurations? This directly addresses the governance gap created by `docs-github-copilot-cca-custom-properties.md` Claim 5 (CCA enabled for ALL repos in selected orgs by default with no automatic per-repo restriction). Enabling CCA for an org defaults to all repos, but previously there was no programmatic way to audit what CCA was configured to do per repo. This API closes that gap. For Ch07 (Enterprise Operations): add "CCA configuration audit sweep" as a recommended compliance practice.

### Claim 4: The configuration audit API is operationally distinct from the task invocation API — it is a read-only state-inspection endpoint

- **Evidence**: Structural distinction between the May 13, 2026 changelog (task invocation) and this May 18, 2026 changelog (configuration audit). The audit framing ("understand and audit," "security posture") contrasts with the task framing ("start tasks," "fan out refactors," "prepare releases").
- **Confidence**: settled (the read vs. write distinction follows directly from the stated purpose of each endpoint)
- **Quote**: (no direct quote; the distinction is structural — the May 18 announcement describes a read operation, the May 13 announcement describes a write operation)
- **Our assessment**: The configuration audit API is safe to poll repeatedly without side effects; the task invocation API creates a new CCA task with each call. This operational distinction matters for how practitioners integrate each API. A compliance scanner can call the configuration audit API frequently (daily sweeps, change detection) without triggering agent work. For Ch02: when documenting the CCA REST API surface, explicitly separate the task-invocation (write) and configuration-audit (read) endpoints — they serve different use cases, have different operational semantics, and may have different rate limits and access control requirements.

## Concrete Artifacts

### CCA Configuration Audit REST API — Key Facts (from changelog, May 18, 2026)

```
Title: Audit repository Copilot cloud agent configuration via the REST API
Published: 2026-05-18 (public preview)

Endpoint name: "Get Copilot cloud agent configuration for a repository"
Endpoint path: Not stated in changelog (see API reference documentation)
API version: Not stated in changelog

Fields returned (partial — changelog uses "including"):
  1. MCP server configuration
  2. Enabled tools
  3. GitHub Actions workflow policy
  4. Firewall configuration

Stated purpose: "understand and audit the security posture of your repositories at scale"

Access eligibility: Not stated in changelog
Authentication: Not stated in changelog
  (CCA pattern implies Business/Enterprise restriction — see docs-github-copilot-cca-rest-api-tasks.md Claim 8)
```

### CCA REST API Surface (synthesized from corpus, current as of 2026-05-25)

```
CCA REST API Capabilities (as of May 2026):

Capability 1 — Task Invocation (May 13, 2026, public preview)
  Operation:  Write — creates a new CCA task
  Use cases:  Fan-out scripting, portal integration, scheduled automation
  Auth:       PAT (classic/fine-grained) or OAuth; GitHub App tokens NOT yet supported
  Source:     docs-github-copilot-cca-rest-api-tasks.md

Capability 2 — Configuration Audit (May 18, 2026, public preview)
  Operation:  Read — returns current per-repository configuration state
  Returns:    MCP server config, enabled tools, Actions workflow policy, firewall config
  Use cases:  Security posture auditing at scale, compliance inventory
  Auth:       Not specified in changelog
  Source:     THIS NOTE (docs-github-copilot-cca-rest-api-audit-config.md)

Together these two APIs provide a minimal programmatic management surface:
  Enterprise enablement API  →  audit which orgs/repos have CCA
  Configuration Audit API    →  audit what CCA is configured to do per repo
  Task Invocation API        →  trigger CCA agent work programmatically
```

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-cca-custom-properties.md` Claim 5 (CCA enabled for ALL repos in selected orgs by default): The configuration audit API directly addresses the governance gap this creates. Before this API, there was no programmatic path to verify per-repository CCA configuration after org-level enablement. The audit API closes that gap — a practitioner can script a compliance sweep across org repositories to inventory per-repo CCA setup.
  - `docs-github-copilot-cca-custom-properties.md` Claim 6 (MCP Registry URL and Restrict MCP Access policies do NOT apply to CCA): The audit API's first returned field — "MCP server configuration" — is the per-repository compensating control for this enterprise gap. Enterprises that set MCP access restriction policies cannot rely on them for CCA; the configuration audit API enables them to instead query and audit CCA's actual MCP server configuration per repo.

- **Extends**:
  - `docs-github-copilot-cca-rest-api-tasks.md` Claim 1 (Agent tasks REST API enables programmatic task start, May 13, 2026): This source announces a second CCA REST API capability, announced five days later. The two together form a more complete programmatic CCA interface. The synthesis artifact above integrates both into a single taxonomy.
  - `docs-github-copilot-cca-custom-properties.md` (enterprise management layer): The custom-properties note documents enterprise-level API for enabling/disabling CCA at org level. This source adds a per-repository configuration query layer. Together they describe a two-tier governance model: enterprise enablement policy (custom-properties note) → per-repository configuration auditing (this source).

- **Contradicts**: None identified. No existing source note makes claims about CCA configuration auditing that conflict with this announcement.

- **Novel**:
  - **Per-repository CCA configuration audit via REST API**: No prior corpus source documents the ability to programmatically read CCA configuration state for a specific repository. Prior sources cover enabling/disabling CCA (enterprise policy), starting CCA tasks, and measuring CCA usage — none cover reading the agent's active configuration.
  - **Firewall configuration as an auditable CCA field**: No prior source note documents CCA's firewall configuration as a security-relevant enterprise concern. This is new to the corpus.
  - **CCA configuration audit as a security posture practice**: The framing of "understanding and auditing the security posture of your repositories at scale" establishes CCA configuration auditing as a governance practice — new to the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering — CCA Integration Patterns)**:
  - Update the CCA REST API documentation (currently only the May 13 task invocation API from `docs-github-copilot-cca-rest-api-tasks.md`) to include the configuration audit API as a second, read-only REST capability. The guide should document both: task invocation (write, creates agent work) and configuration audit (read, returns current state), with their distinct use cases and operational semantics.
  - Add a recommended pattern: before relying on CCA in a repository, script a configuration audit to verify expected settings (tools enabled, MCP servers, firewall config) match the enterprise baseline.

- **Chapter 06 (Safety & Security)**:
  - Add "CCA configuration auditing via REST API" as a recommended security practice for CCA deployments. Key audit fields: MCP server configuration (what external services can CCA contact?), firewall configuration (what network access does CCA have?), enabled tools (what is CCA's capability surface per repo?).
  - Cross-reference the MCP policy gap from `docs-github-copilot-cca-custom-properties.md` Claim 6: since MCP Registry URL / Restrict MCP Access policies don't apply to CCA, the configuration audit API is the compensating control — use it to inventory CCA's actual MCP configuration across repositories rather than relying on enterprise MCP policy.

- **Chapter 07 (Enterprise Operations — CCA Governance and Audit)**:
  - Add "CCA configuration inventory sweep" as a recurring compliance practice: script GET calls against the configuration audit API across CCA-enabled repositories, compare against a baseline (expected tools, approved MCP servers, required firewall settings), flag deviations for review.
  - Document the three-tier CCA governance model that emerges from combining:
    1. Enterprise management API (`docs-github-copilot-cca-custom-properties.md`): which orgs/repos have CCA enabled
    2. Configuration audit API (this source): what CCA is configured to do per repo
    3. Usage metrics API (`docs-github-copilot-cca-usage-metrics-aggregate.md`): how much CCA is being used
  These three together enable a complete enterprise CCA governance posture.

## Extraction Notes

1. **Very brief source (~3 sentences)**: The changelog entry is among the shortest in the corpus. All extractable claims are covered in 4 items. The endpoint path, API version, authentication requirements, access tier restrictions, and response schema are absent from the changelog and presumably in API reference documentation that is not linked in this changelog (unlike the May 13 tasks API, which explicitly linked to its API reference).

2. **API documentation not linked**: The May 13 tasks API changelog linked to `docs.github.com/rest/agent-tasks/...` for full technical details. This May 18 changelog provides no equivalent link. The complete technical schema for this API is unknown from this source alone and requires separate extraction from the API reference.

3. **Authentication and access tier not stated**: The changelog does not specify authentication requirements or access tier (Business/Enterprise vs. Pro). By strong analogy with all other CCA REST APIs (which are Business/Enterprise only and require PAT/OAuth), the same restrictions likely apply — but practitioners should verify against the API documentation before assuming.

4. **"Including" suggests partial field list**: The changelog says the API returns details "including" the four named fields. The use of "including" rather than "consisting of" or "limited to" suggests additional fields may be present in the actual API response.

5. **No contradictions filed**: All claims are consistent with and extend the existing corpus. The MCP configuration audit capability (Claim 2) specifically addresses a gap identified in `docs-github-copilot-cca-custom-properties.md` Claim 6, rather than contradicting it.
