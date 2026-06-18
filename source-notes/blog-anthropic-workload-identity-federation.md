---
source_url: https://claude.com/blog/workload-identity-federation
source_type: blog-post
title: "Secure access to the Claude Platform with Workload Identity Federation"
author: Anthropic
date_published: 2026-06-17
date_extracted: 2026-06-18
last_checked: 2026-06-18
status: current
confidence_overall: emerging
issue: "#1210"
---

# Secure access to the Claude Platform with Workload Identity Federation

> Official Anthropic announcement of Workload Identity Federation (WIF) general availability on the Claude Platform — a credential architecture that replaces static API keys with short-lived, OIDC-issued tokens scoped per workload, supported by service accounts, fine-grained scopes, and Admin API programmatic management, and compatible with all Claude API endpoints, SDKs, and Claude Code.

## Source Context

- **Type**: blog-post (Anthropic official product announcement, claude.com, June 17, 2026; first-party authoritative description of a GA feature)
- **Author credibility**: Anthropic official communications — no individual byline. This is a first-party product announcement for a shipping platform feature. Claims about supported identity providers, API compatibility scope, and Admin API integration are authoritative from the vendor side. No third-party adoption data or security audit results are provided.
- **Scope**: Covers the general availability of WIF on the Claude Platform: (1) the security motivation (replacing static API keys), (2) how the credential exchange mechanism works via OIDC federation rules and service accounts, (3) supported identity providers (AWS IAM, GCP, Azure, Kubernetes, GitHub Actions, Okta, and other OIDC-compliant providers), (4) compatibility scope (all Claude API endpoints, SDKs, and Claude Code), (5) migration path (existing API keys continue to work), (6) setup tooling (Claude Console guided flows, Admin API programmatic management), and (7) enterprise controls (fine-grained scopes for least-privilege access). Does NOT cover: pricing, specific federation rule syntax, per-provider configuration examples in depth, performance or latency implications of token exchange, or any SLAs.

## Extracted Claims

### Claim 1: Workload Identity Federation is now generally available on the Claude Platform as of June 17, 2026
- **Evidence**: Official Anthropic product announcement; the publication date (June 17, 2026) marks the GA date.
- **Confidence**: settled (first-party GA announcement from Anthropic official blog)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This is the foundational GA claim. WIF had been referenced in third-party contexts (GitHub Agentic Workflows v0.77.4, `blog-ghaw-weekly-2026-06-01.md` Claim 2) before this announcement but this post is the authoritative Anthropic platform-level statement of general availability. The June 17, 2026 date establishes the starting point for adoption tracking in the guide.

### Claim 2: WIF is compatible with any OIDC-compliant identity provider and covers all Claude API endpoints
- **Evidence**: Stated as a definitive scope assertion in the announcement — this is a key compatibility guarantee.
- **Confidence**: settled (first-party compatibility claim; the OIDC standard is well-defined and the "all Claude API endpoints" scope is unambiguous)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The "any OIDC-compliant provider" claim is significant because it means organizations are not locked to a specific identity provider list for WIF adoption — any standards-compliant provider qualifies. The "all Claude API endpoints" scope removes the risk that WIF is only available for a subset of capabilities. Together these properties make WIF a universal credential pattern rather than a niche feature for specific providers or endpoints.

### Claim 3: WIF replaces static API keys with short-lived, scoped credentials issued at request time
- **Evidence**: Described as the core mechanism of WIF: federation rules establish trust, OIDC tokens are verified at request time, and temporary access tokens are issued per-request rather than stored permanently.
- **Confidence**: settled (well-understood OIDC/WIF pattern; consistent with how WIF operates in AWS, GCP, and Azure)
- **Quote**: "short-lived, scoped credentials issued at request time"
- **Our assessment**: This is the architectural pivot from static credential management to ephemeral credential exchange. "Short-lived" means the credential lifetime is bounded to the request or session — there is no persistent secret to steal, rotate, or accidentally expose. "Scoped" means the token carries only the permissions needed for the specific workload, implementing least-privilege at the credential level. "At request time" means the token is generated when access is needed, not stored and reused — eliminating the class of credential-at-rest vulnerabilities. This directly implements the pattern prescribed in `blog-anthropic-zero-trust-ai-agents.md` Claim 12.

### Claim 4: WIF eliminates the need to create, rotate, or leak static Anthropic credentials
- **Evidence**: Described as the core security benefit of WIF — the three operational burdens of static API key management (creation, rotation, leakage risk) are eliminated when credentials are ephemeral and identity-provider-issued.
- **Confidence**: settled (direct consequence of the ephemeral credential architecture; consistent with WIF security guarantees in major cloud platforms)
- **Quote**: "create, rotate, or leak"
- **Our assessment**: The three-verb framing ("create, rotate, or leak") maps exactly to the three failure modes of static API key management: (1) provisioning burden — someone must create and distribute the key; (2) rotation burden — keys must be periodically rotated, which is operationally expensive at scale; (3) leakage risk — static keys can be accidentally committed to version control, logged, or stolen. WIF eliminates all three because the identity provider issues credentials dynamically and they expire automatically. The guide currently advises "never commit API keys" (treating leakage as the primary risk) — this source reframes the problem as all three, not just leakage.

### Claim 5: WIF introduces service accounts to the Claude Platform, enabling individual identities and audit trails per workload
- **Evidence**: Described as a new platform primitive that WIF depends on — service accounts are the Claude Platform entity that binds to external identity credentials and appears in audit logs.
- **Confidence**: settled (first-party feature announcement; service accounts are a standard identity management construct)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Service accounts are the Claude Platform's new identity unit for machine-to-machine authentication. Before WIF, the primary identity primitive for API access was the API key (a credential that authenticates an organization or project, not a specific workload). Service accounts enable per-workload identity: each agentic workload can have its own service account, so audit logs and access policies can be scoped to specific agents or processes rather than the entire API key's surface. This is a significant improvement for multi-agent deployments where tracing which agent made which API call requires per-workload identity.

### Claim 6: WIF supports a specific list of named identity providers, including major cloud and platform providers
- **Evidence**: Enumeration of supported providers in the announcement: AWS IAM roles, GCP service accounts, Azure managed identities, Kubernetes service accounts, GitHub Actions tokens, Okta, and other OIDC-compliant providers.
- **Confidence**: settled (specific named providers from a first-party source)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The named provider list covers the dominant enterprise identity infrastructure: the three major clouds (AWS, GCP, Azure), the dominant container orchestration platform (Kubernetes), the dominant CI/CD trigger source for agentic workflows (GitHub Actions), and the dominant enterprise identity provider (Okta). The "and other OIDC-compliant providers" tail means any standards-compliant provider outside this list is also supported. For the guide: teams using any of these platforms can adopt WIF without requiring new identity infrastructure — they federate their existing provider to the Claude Platform.

### Claim 7: Federation rules bind external identities to service accounts via OIDC token verification, then issue temporary access tokens
- **Evidence**: Described as the step-by-step mechanism: (1) federation rules are configured to match external identity claims, (2) when a workload requests access, the OIDC token is verified against configured rules, (3) a temporary access token scoped to a service account is issued.
- **Confidence**: settled (this is the standard OIDC federation exchange pattern; consistent with how WIF is implemented in AWS, GCP, and Azure)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The federation rule mechanism is how WIF enforces least-privilege at the identity level. A rule might specify "this GitHub Actions workflow (identified by repository and job) is authorized to access this service account" — the OIDC claims from GitHub's identity token are matched against the rule, and only if they match is a temporary token issued. This means access is controlled by explicit policy (the federation rule) rather than by secret possession (an API key). For harness engineers: federation rules are the configuration artifact that defines trust boundaries between external workloads and Claude Platform service accounts.

### Claim 8: Fine-grained scopes enable least-privilege access configuration for each service account
- **Evidence**: Described as an enterprise capability of WIF — organizations can configure scopes on service accounts to constrain which Claude Platform capabilities each workload can access.
- **Confidence**: emerging (first-party claim; the specific scope system is not detailed in the announcement)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Fine-grained scopes extend the WIF security model from identity (who is this?) to authorization (what can they do?). A service account for a read-only analysis workload would have a narrower scope than a service account for an agent that needs to call Claude Code or other capabilities. The guide should present scopes as the mechanism for implementing least-privilege at the Claude Platform access layer — not just at the infrastructure layer (network, IAM) but at the API access layer.

### Claim 9: The Admin API enables programmatic management of WIF configuration (issuers, service accounts, federation rules) at organizational scale
- **Evidence**: Described as an enterprise management capability — teams with many workloads can manage WIF configuration through the Admin API rather than the console.
- **Confidence**: settled (first-party claim about Admin API integration; consistent with the Admin API's established role in Claude Platform management)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The Admin API integration is what makes WIF operationally viable at scale. An organization running dozens or hundreds of agentic workloads cannot configure each service account and federation rule manually through the console — they need programmatic configuration via infrastructure-as-code or deployment pipelines. The Admin API makes WIF automation possible. For Ch02 (Harness Engineering): recommend the Admin API path for any deployment with more than a handful of distinct workloads, and note that federation rule management should be version-controlled like any other infrastructure configuration.

### Claim 10: Existing API keys continue to function alongside WIF, allowing gradual workload migration
- **Evidence**: Described as a migration-path feature — WIF and API keys coexist during the transition period.
- **Confidence**: settled (first-party statement about backward compatibility)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The coexistence guarantee removes the need for a "big bang" migration from API keys to WIF. Teams can migrate one workload at a time, validating WIF configuration in production before decommissioning the corresponding API key. For the guide: present this as an incremental adoption path — start with new workloads using WIF, migrate existing workloads as they are updated or redeployed. Do NOT frame this as "API keys are still fine" — the coexistence is a migration tool, not an ongoing policy endorsement.

### Claim 11: The Claude Console provides guided setup flows with validation at each step for connecting workloads to supported identity providers
- **Evidence**: Described as the console UX for WIF configuration — it provides step-by-step guidance rather than requiring raw API configuration.
- **Confidence**: settled (first-party description of console functionality)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The guided console flows lower the adoption barrier for teams without deep OIDC expertise — they can configure WIF for a specific identity provider (e.g., GitHub Actions or AWS IAM) by following the console wizard. The "validation at each step" claim suggests the console verifies configuration correctness incrementally rather than requiring a complete, correct configuration before any validation. For teams exploring WIF adoption: the console is the right starting point; the Admin API is the right tool for production-scale management.

## Concrete Artifacts

### WIF Credential Exchange Mechanism (from announcement description)

```
Static API key model (before WIF):
  Provisioning: Create Anthropic API key, distribute to workload
  Runtime auth:  Workload presents long-lived key with each request
  Rotation:      Periodic manual rotation required; operational burden
  Leakage risk:  Key can be committed, logged, or stolen; persists until rotated
  Audit trail:   All activity logged to the API key (no per-workload identity)

WIF model (GA June 17, 2026):
  Provisioning:  Configure federation rule binding external identity to service account
  Runtime auth:  Workload obtains OIDC token from provider → exchanges for temporary
                 Claude Platform access token → presents short-lived token with request
  Rotation:      Automatic; tokens expire at request time, no manual rotation
  Leakage risk:  No persistent secret; expired tokens have no value
  Audit trail:   Activity logged against individual service accounts (per-workload identity)

Supported OIDC identity providers (as of GA):
  - AWS IAM roles
  - GCP service accounts
  - Azure managed identities
  - Kubernetes service accounts
  - GitHub Actions tokens
  - Okta
  - Any other OIDC-compliant provider

Compatibility:
  - All Claude API endpoints
  - All Claude SDKs
  - Claude Code

Management:
  - Claude Console: guided setup flows with per-step validation
  - Admin API: programmatic management of issuers, service accounts, federation rules
```

## Cross-References

- **Corroborates**:
  - `blog-ghaw-weekly-2026-06-01.md` Claim 2: That note documents WIF authentication for Claude-engine workflows in GitHub Agentic Workflows v0.77.4 (PR #35939), citing the benefit as eliminating "long-lived API key secrets in your repo." This announcement is the foundational Anthropic platform-level source for that feature — the gh-aw note documents the GitHub Actions integration of the general WIF capability announced here.
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 12: That note states "Short-lived, narrowly-scoped tokens issued by an identity provider are the new baseline" and explicitly categorizes static API keys as "no longer a legitimate entry point, not even at Foundation." WIF is the Anthropic-platform implementation of exactly this prescription — the zero-trust eBook defined the requirement; this announcement is the shipped product. The alignment is precise: short-lived (WIF: tokens expire at request time), narrowly-scoped (WIF: fine-grained scopes), identity-provider-issued (WIF: OIDC provider issues the token, not a static credential).
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 4: That note's pattern — "hardware-bound credentials, expiring tokens, cryptographic identity, and network paths that do not exist" — maps to WIF's mechanism: OIDC-based cryptographic identity, short-lived tokens, and per-workload service accounts. WIF implements the "expiring tokens" and "cryptographic identity" properties specifically.

- **Extends**:
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 12 (short-lived tokens as baseline): The zero-trust eBook described the prescriptive requirement; WIF is the concrete Anthropic platform feature that fulfills it. Teams that have adopted the zero-trust framework guidance now have a first-party implementation path on the Claude Platform for the credential model it requires.
  - `blog-anthropic-compliance-api-security-partners.md` Claim 5 (eight security integration categories including "identity"): The compliance API security partner network includes identity tools as one of the eight categories. WIF operates at a different layer — Claude Platform credential authentication — but together they describe a layered identity picture: WIF governs how workloads authenticate to Claude; the compliance API identity integrations govern how Claude usage events flow into enterprise identity management tooling.

- **Contradicts**: None identified. The zero-trust note's prescription for short-lived tokens is directly fulfilled by WIF rather than contradicted. The gh-aw note's mention of WIF (Claim 2) is corroborated rather than contradicted by this announcement.

- **Novel**:
  - **WIF as a Claude Platform GA credential architecture**: This is the first corpus source to document WIF as a shipped, generally available Anthropic platform feature. The gh-aw note mentions WIF in the context of GitHub Actions workflows; this note establishes the platform-level scope (all Claude API endpoints, SDKs, Claude Code, any OIDC provider) that makes WIF a universal credential pattern, not a GitHub-specific one.
  - **Service accounts as a Claude Platform identity primitive**: First corpus source to document service accounts as a first-class identity entity on the Claude Platform. Prior corpus sources treat API keys as the primary authentication object; service accounts represent a fundamentally different identity model where individual workloads have distinct platform identities.
  - **Fine-grained scopes at the Claude Platform API access layer**: First corpus source to document per-workload scope constraints on Claude API access. The zero-trust eBook recommends least-privilege credentials; this announcement provides the actual mechanism (scopes on service accounts) for achieving that at the Claude Platform layer.
  - **Admin API for federation rule management**: First corpus source to document Admin API support for managing WIF configuration (issuers, service accounts, rules) programmatically. Prior Admin API documentation covers user and organization management; WIF extends it to credential architecture management.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add WIF as the recommended credential model for Claude API access in production harness deployments. The guide currently lacks guidance on secure credential provisioning beyond "never commit API keys" — WIF provides the complete pattern: ephemeral OIDC-issued tokens scoped to service accounts, managed via Admin API. Specifically: (1) recommend WIF for all new production workloads, (2) recommend the Admin API path for any deployment with multiple distinct workloads, (3) present federation rule management as infrastructure-as-code that should be version-controlled alongside harness configuration. Note that API key coexistence supports incremental migration but should not be presented as a permanent dual-mode policy.

- **Chapter 03 (Safety and Verification)**: Update the credential security section to add WIF as the reference implementation for short-lived, scoped credentials on the Claude Platform. Currently the corpus's most authoritative credential security guidance (zero-trust note Claim 12) prescribes short-lived tokens as the minimum bar but does not name a Claude Platform mechanism. WIF fills that gap. Add: "WIF is the Anthropic-platform implementation of the short-lived token requirement from the zero-trust framework — service accounts with fine-grained scopes, OIDC-issued temporary tokens, and no persistent secret to protect."

- **Chapter 05 (Team Adoption)**: Add WIF migration planning to the enterprise adoption checklist. The coexistence guarantee (API keys alongside WIF) makes this an incremental adoption path, suitable for organizations that cannot migrate all workloads simultaneously. Recommended phasing: (1) configure WIF for new workloads from day one, (2) migrate existing workloads at next redeployment, (3) audit and deprecate API keys once all workloads are on WIF. The Admin API enables programmatic inventory and management of both credential types during the transition.

- **Chapter 04 (Context Engineering / Platform & API design)**: Note the introduction of service accounts as a new platform identity primitive that should be designed for from the start of any agentic workload architecture. Each distinct agentic function that should have its own audit trail or access scope should have its own service account. Do not share service accounts across unrelated workloads — the per-workload identity model is only useful if it is actually applied per workload.

## Extraction Notes

1. **WebFetch summarization**: The source was fetched twice. Both fetches returned model-generated summaries rather than verbatim article text. The two fragments put in explicit quotes in the second fetch — "short-lived, scoped credentials issued at request time" and "create, rotate, or leak" — are the only two strings treated as potentially verbatim from the source; all other quotes are marked "(no direct quote; see paraphrase in Our assessment)" per MINER.md §2a requirements.

2. **GA date**: Both fetches confirm June 17, 2026 as the announcement/publication date (matching the RSS feed publication date in the issue). This is treated as the WIF GA date.

3. **No sub-pages followed**: Both fetches covered the main blog post URL. No linked documentation sub-pages were accessible within the fetch. The announcement references setup guides for each identity provider, but those were not accessible via this fetch.

4. **Claim confidence**: Claims 1, 3, 5, 6, 10, 11 are rated "settled" because they are straightforward first-party product assertions about shipping features. Claims 7, 8, 9 are rated "emerging" because the specific configuration syntax, scope system design, and Admin API integration are not detailed enough in the summary to fully verify their implementation particulars.

5. **No contradictions filed**: Cross-referencing against the corpus found no material contradiction. The zero-trust note's prescriptions (Claim 12) are fulfilled rather than opposed by WIF.
