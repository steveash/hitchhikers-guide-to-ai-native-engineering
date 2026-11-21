---
source_url: https://developers.googleblog.com/how-to-handle-user-connector-and-agent-auth-in-gemini-enterprise-with-a-custom-ui/
source_type: blog-post
title: "How to handle user, connector, and agent auth in Gemini Enterprise with a custom UI"
author: Neeraj Agrawal (Forward Deployed Engineer, Google Cloud)
date_published: 2026-11-20
date_extracted: 2026-11-21
last_checked: 2026-11-21
status: current
confidence_overall: emerging
issue: "#4880"
---

# How to handle user, connector, and agent auth in Gemini Enterprise with a custom UI

> A vendor how-to that separates three auth layers for agents acting on behalf of a user (caller identity, per-user connector OAuth, per-tool on-demand OAuth via a token vault), contributing a concrete "consent only when a protected tool is called" pattern and a per-user vs. shared-bot identity trade-off.

## Source Context

- **Type**: blog-post (vendor implementation guide with architecture diagrams; companion repo `gemini-enterprise-custom-ui-auth` not reviewed)
- **Author credibility**: Google Cloud Forward Deployed Engineer writing about Google's own product. First-hand product knowledge, but no independent validation, no metrics, no customer results.
- **Scope**: Gemini Enterprise StreamAssist API called from a custom UI/backend; Federated Connectors; custom ADK agents on Vertex AI Agent Engine with GCP Auth Manager. Product-specific (IAM roles, endpoints). Agent-to-agent auth is NOT covered. Extract patterns, not vendor claims.

## Extracted Claims

### Claim 1: Building a custom UI over a managed agent API makes three auth flows the builder's responsibility that the built-in web app handled automatically
- **Evidence**: Architectural description (Figure 1); enumerates the three layers: authenticating to StreamAssist, Federated Connectors, per-tool OAuth for custom ADK agents. No measurements.
- **Confidence**: emerging
- **Quote**: "The moment an application builds a custom UI and calls the StreamAssist API directly, the three authentication flows that the built-in web app handled automatically become the responsibility of Customer UI and Customer BE:"
- **Our assessment**: Credible and generalizable: any team that bypasses a vendor's first-party client inherits its identity plumbing. A useful framing for a checklist.

### Claim 2: Pass the signed-in user's identity (not a shared identity) when document ACLs, chat isolation, or restricted agent permissions matter; use keyless workload identity only for non-personalized bots
- **Evidence**: Three patterns: 1A Google Identity, 1B Workforce Identity Federation + Google STS, 1C Workload Identity Federation + STS (machine JWT, no keys on disk).
- **Confidence**: emerging
- **Quote**: "Because Workload Identity Federation authenticates a machine rather than an individual human employee, Gemini Enterprise sees every request as coming from the same workload identity."
- **Our assessment**: Sound least-privilege reasoning; the failure mode (shared bot identity loses per-user ACLs, and the article notes it also rules out user-specific 3LO connectors) is named explicitly. Practical consequence: a shared bot in a Slack/Teams webhook sees the union of what the workload can see, so do not expose it to restricted data.

### Claim 3: Keyless federation (exchange an external IdP token at Google STS) avoids service-account JSON keys
- **Evidence**: Pattern 1B/1C step lists; token exchange against Workforce/Workload Identity Pool providers.
- **Confidence**: emerging
- **Quote**: "Customer BE exchanges that machine JWT at Google STS against the project's Workload Identity Pool Provider with zero keys on disk."
- **Our assessment**: Standard cloud best practice, applied to agents. Compare the Anthropic WIF note.

### Claim 4: For connector 3-legged OAuth, the platform (not the customer backend) should hold per-user refresh tokens
- **Evidence**: 11-step flow (Figure 3): connector discovery, Keystore check, consent popup, redirect relay via postMessage, code exchange performed by the platform server, refresh token saved in the Keystore.
- **Confidence**: emerging
- **Quote**: "Gemini Enterprise stores those per-user refresh tokens inside its own managed Keystore, so Customer BE never has to store third-party credentials in its own database."
- **Our assessment**: Reduces the app's blast radius (a compromised customer DB leaks no third-party tokens), but it moves trust to the platform; the property holds only as far as the vendor Keystore is trusted. Customer BE still handles the authorization code/callback URL in transit (Step 8), so "never stores" is not "never sees".

### Claim 5: Root-level OAuth on agent registration gates the whole agent before any tool runs, blocking multi-tool agents
- **Evidence**: Named failure mode with example (Drive + SharePoint). Assertion by the author; no reproduction shown.
- **Confidence**: anecdotal
- **Quote**: "Root-level OAuth gates the entire agent before the first turn even reaches your agent code."
- **Our assessment**: Plausible and a real UX/least-privilege problem (users forced to grant every scope upfront). Product-specific mechanism, but the design lesson generalizes: scope consent to the tool, not the agent.

### Claim 6: Root-level agent authorization is coupled to the vendor's built-in UI, so it cannot return tool-specific auth prompts over the API
- **Evidence**: Stated as the second issue with root-level OAuth.
- **Confidence**: anecdotal
- **Quote**: "Root-level agent authorization is designed around the built-in Gemini Enterprise web UI rather than returning tool-specific authorization prompts over the StreamAssist API."
- **Our assessment**: Vendor limitation rather than a general principle; may change as the product evolves.

### Claim 7: Wrap only protected tools in an auth provider so unprotected tools run with zero prompts, and consent is requested on first use of a protected tool
- **Evidence**: Setup steps: `AuthenticatedFunctionTool` + `GcpAuthProvider`; Agent Identity (SPIFFE) for the agent; 3LO Auth Provider per third-party app. 19-step flow (Figure 4).
- **Confidence**: emerging
- **Quote**: "Standard tools that do not need user login run as normal Python functions with zero OAuth prompts."
- **Our assessment**: A good concrete incarnation of just-in-time authorization. No evidence beyond the walkthrough that it works at scale, but the repo ships runnable code.

### Claim 8: Tokens are held in a vault keyed to the agent's own identity, with a validate-and-finalize step binding the token to the session owner
- **Evidence**: Steps 4, 11-13: sub-agent checks the Token Vault with Agent Identity; Customer BE calls Validate User Authorization with the user's bearer token; GE Server verifies the session owner and calls FinalizeCredentials.
- **Confidence**: emerging
- **Quote**: "GE Server verifies the session owner and calls FinalizeCredentials on GCP Auth Manager, which permanently saves the user's 3LO token in the Token Vault and returns success (Step 13)."
- **Our assessment**: The validation hop mitigates a confused-deputy/token-injection risk (someone else's callback completing for your session). Worth highlighting as a design element; the article does not frame it as a threat mitigation itself, so that interpretation is ours.

### Claim 9: After consent completes the backend automatically retries the original query on the same session, so subsequent queries need no popups
- **Evidence**: Phase 4, Steps 15-19.
- **Confidence**: emerging
- **Quote**: "As soon as Customer BE receives HTTP 200 OK in Step 14, Customer BE automatically retries the StreamAssist query on the same session (Step 15)."
- **Our assessment**: The "auth-required interrupt, then resume/retry" pattern is the important agent-UX contract; it implies tool calls must be safely retryable.

### Claim 10: Custom-domain popup handoff requires a vendor-side flag, otherwise the callback is not delivered to the custom UI
- **Evidence**: Note for Custom UIs: fixed `/oauth-redirect` callback only posts to the built-in app origin by default.
- **Confidence**: anecdotal
- **Quote**: "When deploying Customer UI on a custom domain, work with your Gemini Enterprise team to enable the custom origin flag so Step 7 automatically posts the callback URL to Customer UI and closes the popup."
- **Our assessment**: A concrete integration failure mode; vendor-specific operational dependency.

## Concrete Artifacts

```
Paraphrase (not verbatim) of Part 1 "Required IAM Role and License"
- Every StreamAssist caller: Discovery Engine User IAM role on the project
- Human patterns (1A/1B): also an active Gemini Enterprise license
```

```
Attribution: summary of "Part 3" setup steps (source: Google Developers Blog, 2026-11-20)
1. Wrap protected tools: ADK AuthenticatedFunctionTool + GcpAuthProvider -> Auth Provider resource in GCP Auth Manager
2. Deploy to Vertex AI Agent Engine with Agent Identity (SPIFFE); grant "Agent Identity Service Agent" role
3. Create a 3LO Auth Provider per third-party OAuth app; Default Continue URI = <website-url>/validateUserId;
   Auth Manager callback (/oauthcallback) registered as Redirect URI in Entra ID / third-party app
```

Flow summary (our condensation): connector flow = 11 steps (discover, Keystore check, popup, postMessage relay, code exchange, store refresh token); tool flow = 19 steps (route, vault miss, auth URL bubbles up through the stack, popup, finalize, retry, cache hit). Repo layout: `01_user_auth_streamassist/`, `02_federated_connector_oauth/`, `03_adk_agent_oauth/`.

## Cross-References

- **Corroborates**: `blog-anthropic-mcp-production-agents.md` (Claim 9: standardized OAuth for cloud-hosted agent auth): both treat OAuth consent flows as the way agents reach user-owned third-party systems. `blog-anthropic-workload-identity-federation.md` (keyless federation for workloads) aligns with Claim 3 above; not re-verified claim by claim.
- **Contradicts**: None filed. `blog-anthropic-agent-identity-access-model.md` (Claim 4, Claim 5) argues per-user permissions are unworkable for team agents and prefers the agent's own per-compartment identity; this article keeps per-user delegated tokens. This is a conditioning difference (single-user custom UI vs. shared multiplayer channels), not a contradiction, so no contradiction issue was filed.
- **Extends**: `blog-google-adk-zero-trust-agents.md` (Claims 3, 4: per-agent cryptographic identity via KMS signing): this note adds the delegated-user-authorization layer (token vault, 3LO) on top of agent identity (SPIFFE Agent Identity). `blog-anthropic-agent-identity-access-model.md` Claim 8 (credentials stored independently of users, injected at request time) is a parallel to the vault-held-token design.
- **Novel**: Token-vault/3LO-per-tool pattern with auth-required interrupt and automatic retry; per-user vs. shared-bot trade-off for calling a managed agent API; custom-UI consent popup relay.

## Guide Impact

- **Chapter 06 (security threat model)**: add a subsection or sidebar on delegated-user authorization for agents: (a) per-user identity vs. shared workload identity trade-off (Claims 2, 3), (b) platform-held token vault vs. app-held credentials (Claim 4), (c) tool-scoped just-in-time consent instead of agent-level upfront consent (Claims 5, 7). Present as one vendor's implementation with `emerging` confidence, contrasted with the Anthropic per-compartment identity model.
- **Chapter 02 (harness)**: mention the "auth-required interrupt then retry on the same session" contract for tool calls (Claim 9) when discussing tool wiring.

## Extraction Notes

- Fetched and read the full article text (Part 1-3 and repo section); did not follow the companion GitHub repo. Figures were not viewable; flow step numbers come from the prose.
- The article reports no metrics, incidents, or security evaluation; all claims are design assertions by the vendor, hence `emerging`/`anecdotal`.
- Triage asked to verify the "root-level OAuth blocks multi-tool agents" claim: the article only asserts it; independent verification not possible from the source.
- Quotes copied from the page text; the Concrete Artifacts first block is a paraphrase and is labelled as such.
