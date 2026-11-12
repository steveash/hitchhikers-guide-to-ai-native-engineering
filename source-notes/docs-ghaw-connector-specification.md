---
source_url: https://github.github.com/gh-aw/specs/connector-specification
source_type: docs
title: "GitHub Agentic Workflows: Connector Specification"
author: GitHub Agentic Workflows Team (GitHub Next / Microsoft Research)
date_published: 2026-11-08
date_extracted: 2026-11-12
last_checked: 2026-11-12
status: current
confidence_overall: emerging
issue: "#4681"
---

# GitHub Agentic Workflows: Connector Specification

> A normative spec (v1.0.0, Experimental Working Draft) for declaration-only connectors: imports select nothing, consumers pick each read/effect, credentials are phase-scoped and host-resolved, resources are exact IDs with no wildcards, and every response and write path is typed and bounded. It is a concrete least-privilege checklist for agent tool access, stated as design intent rather than validated practice.

## Source Context

- **Type**: docs (formal spec using RFC 2119 keywords; "Version: 1.0.0 / Status: Experimental Working Draft / Publication Date: 2026-11-08").
- **Author credibility**: First-party, the team that builds the gh-aw compiler and shared Go/Node runtimes. Authoritative for what gh-aw intends to enforce. It is not independent evidence that the controls work in production.
- **Scope**: imported provider declarations, explicitly selected reads, safe outputs, protected event subscriptions. Excludes a provider catalog, token acquisition, webhook receiver deployment, and arbitrary API/script execution. The spec says its provider examples "are not live-readiness certifications", so every claim below is design intent. There are no metrics or incident reports.

## Extracted Claims

### Claim 1: Connectors are declaration-only; there is no arbitrary API/script execution surface
- **Evidence**: Scope section; unknown declaration fields fail; requests are fixed paths with typed values; "Arbitrary agent-provided queries, URLs, scripts, and JSON patches are unsupported."
- **Confidence**: emerging
- **Quote**: "This specification defines the declaration-only connector interface implemented by the gh-aw compiler and shared Go/Node runtimes."
- **Our assessment**: Strong pattern: the agent gets named operations with typed parameters, never a generic HTTP or query tool. Trade-off is authoring cost per operation.

### Claim 2: Importing a connector selects nothing; the consumer must independently select each read, effect, and trigger
- **Evidence**: §3 table of selection surfaces; native-tool subsets must be nonempty and exact (unknown, duplicate, wildcard, empty subsets fail).
- **Confidence**: emerging
- **Quote**: "Importing a declaration selects nothing."
- **Our assessment**: Separates "capability available" from "capability granted". It guards against supply-chain-style imports quietly widening an agent's tool surface.

### Claim 3: The compiler prunes unselected capabilities, endpoints, grants and credentials from each phase plan, and writer credentials never reach the agent
- **Evidence**: §3. An imported endpoint is not network approval; the workflow/host network policy must also approve it.
- **Confidence**: emerging
- **Quote**: "Writer credentials MUST NOT reach the agent."
- **Our assessment**: Compile-time least privilege per phase. It corroborates the read-only-agent, write-elsewhere split in the safe-outputs spec.

### Claim 4: Resource authority is exact approved IDs only; empty grants grant nothing; IDs returned by a read never become write authority
- **Evidence**: §2 and §4. Resource-constrained arguments must be required strings matching an exact authored grant before credential resolution; no silent coercion or trimming; independent grant lists "do not prove tenant, parent, or tuple membership."
- **Confidence**: emerging
- **Quote**: "IDs returned by a read MUST NOT become write authority automatically."
- **Our assessment**: Directly addresses confused-deputy and prompt-injection escalation: data read from an untrusted record cannot name a new write target. The tuple-membership caveat is an honest limitation.

### Claim 5: Credentials are never in declarations; each is phase-scoped, resolved only by a host-owned resolver, and scopes are documentation not grants
- **Evidence**: §4. A credential declares phase, header, scheme, scopes and exactly one source route. Agent-phase GitHub App permissions must not include write.
- **Confidence**: emerging
- **Quote**: "Binding values MUST NOT contain credential values."
- **Our assessment**: Credential-by-reference is standard, but the rules that scope strings are not authority and that the resolver is per phase are useful specifics. Token acquisition and renewal are explicitly out of scope.

### Claim 6: Hosts must reject redirects and endpoint changes before forwarding credentials, and must not fall back to other credentials after a denial
- **Evidence**: §4 and §5.3 (canonical URL comparison, no redirects, different paths prohibited).
- **Confidence**: emerging
- **Quote**: "Hosts MUST reject redirects and endpoint changes before forwarding credentials, and MUST NOT switch credentials after an authorization denial."
- **Our assessment**: Concrete, checkable credential-leak controls that are often missed in custom tool wrappers.

### Claim 7: Operations are typed with bounded inputs and fixed requests; unknown or missing arguments fail
- **Evidence**: §5.1/5.2. String `maxLength` is required (1 to 65536); no object/array/expression inputs; fixed absolute paths with single-safe-segment substitution; `request.headers` must not replace authentication routing; GraphQL reads must start with `query ` and may not contain mutation/subscription tokens.
- **Confidence**: emerging
- **Quote**: "Unknown arguments and missing required values MUST fail."
- **Our assessment**: A reasonable template for hardening tool schemas: no free-form strings without length caps, no agent-built URLs.

### Claim 8: Hosted HTTP MCP servers are only admitted read-only, with exact tool contracts, and remote annotations are advisory
- **Evidence**: §5.3. Registrations require `readOnly: true`, a fixed HTTPS URL, a nonempty exact tools map and `maxResponseBytes`; the local adapter validates selection, arguments, grants, phase and endpoint before forwarding `tools/call`.
- **Confidence**: emerging
- **Quote**: "Remote read-only annotations are advisory, not proof of provider authorization."
- **Our assessment**: Do not trust a remote server's own `readOnly` hint; enforce at a local adapter. Aligns with the MCP gateway pattern.

### Claim 9: Response evidence is bounded and verified; responses stay untrusted data even after validation
- **Evidence**: §6. `maxResponseBytes` 1 to 1048576; checks (`responseChecks`, `responseRequired`, `responseResourceInputs`, `responseLimits` etc.); pagination is never automatic; `project` exposes only named fields, but omission returns the validated response rather than a minimal projection.
- **Confidence**: emerging
- **Quote**: "Responses and MCP content remain untrusted data even after validation."
- **Our assessment**: Verifies that the response is about the resource that was asked for (identity echo), then projects minimal fields. Good context-hygiene guidance. The projection-is-opt-in default is a noted weakness.

### Claim 10: Selected plans are size-limited and fail loudly rather than dropping controls
- **Evidence**: §6. Serialized plan at most 65536 UTF-8 bytes; plans must be human-reviewable JSON, not base64; generated hosts load plans from compiler-owned env vars.
- **Confidence**: emerging
- **Quote**: "Oversized plans MUST fail with a request to select fewer capabilities, not silently omit controls."
- **Our assessment**: A fail-closed principle for any policy compiler, where truncation would silently weaken enforcement.

### Claim 11: Connector writes run outside the agent boundary, are revalidated by the host, and are non-reviewable outputs under the threat-detection gate
- **Evidence**: §7. Failed or missing detection conclusions cannot be overridden by agent-supplied policy fields; `max` (1 to 100, default 1) counts attempted calls, including failures.
- **Confidence**: emerging
- **Quote**: "Safe outputs MUST execute outside the agent credential boundary and require explicit host write authorization."
- **Our assessment**: Extends the safe-outputs model to third-party providers. Counting failed attempts against the budget prevents retry-loop amplification.

### Claim 12: Narrowing policies can only reduce authority; agent-supplied IDs, aliases and staged creations are not receipts
- **Evidence**: §7.2. `trustedInputs`, `preflight`, `checks` (at most 4), `lookups` (at most 4, cycles fail). Receipts must be verified against the authenticated creation response.
- **Confidence**: emerging
- **Quote**: "All policy reads narrow existing authority; they MUST NOT grant a new destination."
- **Our assessment**: Monotonic-narrowing is a clean design rule for write guards.

### Claim 13: Staging suppresses writes, writer credential resolution and receipts, but does not suppress readers or workflow scripts, and samples are not a dry run
- **Evidence**: §7.1.
- **Confidence**: emerging
- **Quote**: "Samples alone do not enable staging and MUST NOT be described as a dry run."
- **Our assessment**: Honest about dry-run limits: reads still happen and still contact the provider.

### Claim 14: Retries are opt-in, bounded, and never apply to creates, authorization failures, redirects or uncertain outcomes
- **Evidence**: §7.3. `maxAttempts` 1 to 4, 20-second total deadline; POST creates and appends never retry; writes retry only with `idempotent: true` on a reviewed PUT/PATCH/DELETE.
- **Confidence**: emerging
- **Quote**: "An HTTP method alone does not establish idempotency."
- **Our assessment**: A useful, specific retry policy for agent write tools. Retrying a POST that has an uncertain outcome is how duplicate side effects happen.

### Claim 15: Event triggers use evidence-only matching: missing or ambiguous evidence is a non-match, and compiling a trigger claims no operability
- **Evidence**: §8. Predicates follow `gh-aw/event-predicates/v1`; the compiler emits digest-bound subscription data; the subscription is nonactivating until an approved receiver supports the profile.
- **Confidence**: emerging
- **Quote**: "Missing or ambiguous lifecycle evidence MUST be a nonmatch, not permission to fetch a resource or infer a transition."
- **Our assessment**: Triggers carry references, not hydrated content, so the agent must use an explicitly selected reader to see content. This is the context boundary.

### Claim 16: Conformance claims need layered evidence, and compilation, mocks, staging and live provider access must be reported separately
- **Evidence**: §10 table (Authoring, Selection, Requests, Responses, Publication, Failure policy, Distribution, Trigger). `connector <id> setup` is offline; `--phase safe-output` always stages; `--phase agent` is a live test. Name presence is not proof of access.
- **Confidence**: emerging
- **Quote**: "Compilation, mocks, setup output, and staging MUST be reported separately from provider authorization, ingress readiness, live delivery, and operational value."
- **Our assessment**: Good discipline against overclaiming readiness for agent integrations.

### Claim 17: Connector documentation is embedded in an XML comment so imported usage notes never become system prompt, and is shown as untrusted reference data
- **Evidence**: §10. The whole Markdown body must be commented out; documentation is stripped before import-input substitution and prompt rendering; setup displays it as fenced untrusted data.
- **Confidence**: emerging
- **Quote**: "The entire Markdown body, including usage notes, MUST be commented out so it does not become an imported system prompt."
- **Our assessment**: Notable prompt-injection hygiene for imported files: even author docs are not trusted instructions.

### Claim 18: Imported declarations may not be silently replaced, and collisions fail closed
- **Evidence**: §2.
- **Confidence**: emerging
- **Quote**: "Imported declarations MUST NOT be silently replaced by built-in definitions, remote fallbacks, or a provider inferred from its name."
- **Our assessment**: Pairs with the SHOULD-pin-reviewed-commit rule for remote imports. Defends against name-based provider confusion.

## Concrete Artifacts

From §9 (synthetic, "not a claim about a real provider API"), abridged:

```yaml
connectors:
  example:
    experimental: true
    endpoints:
      api: https://api.example.com
    credentials:
      reader: {phase: agent, header: Authorization, scheme: bearer, scopes: [records:read], token: {secret: ...}}
      writer: {phase: safe-output, header: Authorization, scheme: bearer, scopes: [notes:write], token: {secret: ...}}
    resources:
      records: ${{ github.aw.import-inputs.records }}
    tools:
      get-record:
        tool: get_record
        credential: reader
        inputs:
          record-id: {type: string, required: true, maxLength: 64, pattern: "^[A-Za-z0-9-]+$"}
        resources: {record-id: records}
        request: {endpoint: api, method: GET, path: /v1/records/{record}, pathInputs: {record: record-id}}
        maxResponseBytes: 65536
        responseResources: {/id: records}
        project: {id: /id, status: /status}
    safe-outputs:
      add-note: {credential: writer, ... request: {method: POST, ... body: {text: {input: text}}}}
```

Consumer (from §9):

```yaml
imports:
  - uses: .github/workflows/connectors/example.md
    with:
      records: [RECORD-1]
tools:
  example: [get-record]
safe-outputs:
  example-add-note:
    max: 1
    staged: true
```

Section 10's conformance-evidence table, plus the limits: `maxResponseBytes` 1 to 1048576; plan at most 65536 bytes; declaration documents at most 256 KiB; retries `maxAttempts` 1 to 4, backoff 1 to 1000 ms, 20 s deadline; `max` 1 to 100; `checks` and `lookups` at most 4; `additionalPatch` at most 32 entries.

## Cross-References

- **Corroborates**: `docs-ghaw-safe-outputs-specification.md` Claim 3 (agents execute without write permissions) and Claim 4 (fail-secure and architectural separation principles); `docs-ghaw-mcp-scripts-specification.md` Claim 6 (explicit secret declaration).
- **Contradicts**: none found.
- **Extends**: `docs-ghaw-safe-outputs-specification.md` Claim 5 (security invariants) to third-party provider writes; `docs-ghaw-mcp-gateway-reference.md` by adding local-adapter validation of remote MCP tools; `docs-ghaw-threat-detection.md` (connector writes are non-reviewable under the detection gate). Shares the "absence is not evidence" posture with `docs-ghaw-unified-agent-session-specification.md` Claim 2, applied to response evidence and setup inventory.
- **Novel**: exact-ID-only resource grants with no wildcard; read results never becoming write authority; per-phase credential pruning at compile time; redirect and credential-switch prohibitions; response identity echo checks; opt-in, method-based retry rules; documentation-as-comment prompt hygiene.

## Guide Impact

- **Chapter 06**: Add the connector contract as a checklist for least-privilege tool access: exact-ID grants, no wildcards, read output never grants write authority, credentials resolved per phase by the host, no redirect or credential fallback. Attribute to the spec as design intent.
- **Chapter 02**: Cite typed fixed-request operations with a required `maxLength` and no free-form URLs/queries as a tool-design pattern; note the "import selects nothing" principle for tool registries.
- **Chapter 04**: Cite the context-boundary rule (triggers carry references, not hydrated content; project minimal fields; responses stay untrusted).

## Extraction Notes

- Read the full page (about 36k characters of extracted text, sections 1 to 11). Did not follow the linked connector reference or creation skill pages.
- Spec is Experimental; no production evidence. Confidence is capped at emerging.
- All quotes were copied from the fetched page text. No contradiction issue was filed.
