---
source_url: https://claude.com/blog/compliance-api-security-partners
source_type: blog-post
title: "Claude now works with more security and compliance tools"
author: Anthropic
date_published: 2026-05-21
date_extracted: 2026-05-22
last_checked: 2026-05-22
status: current
confidence_overall: settled
issue: "#847"
---

# Claude now works with more security and compliance tools

> Official Anthropic announcement of 28 security and compliance partner integrations built on the Claude Compliance API, establishing that IT and security teams can now govern Claude through the same DLP, SIEM, identity, and eDiscovery tools they use for other enterprise applications — and documenting that the Compliance API provides conversation content from Claude Enterprise to security partners, which materially updates the compliance architecture picture from the March 2026 Compliance API launch note.

## Source Context

- **Type**: blog-post (Anthropic official product announcement, claude.com, May 21, 2026; first-party authoritative description of a shipping production feature)
- **Author credibility**: Anthropic official communications — no individual byline. This is a vendor product announcement describing shipping integrations with named enterprise security partners. Claims about which data types are accessible and which partner categories are covered are authoritative from the vendor side. The 28 partner names are verifiable against published partner documentation. No third-party validation of integration scope or data fidelity is provided in this post.
- **Scope**: Covers the 28-partner integration network built on the Claude Compliance API, the two data access types provided (conversation content for Claude Enterprise; activity events for both Claude Enterprise and Claude Platform), the eight integration categories, the data flow into existing security dashboards, and the process for customers and new partners. Does NOT cover: specific per-partner integration scope, data retention policies, API schema or payload format, rate limits, pricing, SLAs, geographic data residency, which specific DLP or SIEM policies are applicable, or how conversation content is filtered or anonymized before it reaches partner platforms. The post is short (~400 words); no sub-pages were linked from the main content.

## Extracted Claims

### Claim 1: Anthropic has launched 28 security and compliance tool integrations, enabling enterprise governance of Claude through existing security infrastructure

- **Evidence**: Direct announcement statement: "Today we're introducing 28 integrations with notable security and compliance tools."
- **Confidence**: settled (first-party product announcement with named partners; verifiable against published partner list)
- **Quote**: "Today we're introducing 28 integrations with notable security and compliance tools."
- **Our assessment**: This is the broadest and most unambiguous claim in the post — the number (28) and the category (security and compliance) are concrete and verifiable. The significance is organizational: organizations that have been treating Claude governance as a separate, Claude-specific workflow can now integrate it into existing security tooling. The guide should present this as the beginning of Claude governance maturity — from custom pipelines to standard enterprise security tool integration.

### Claim 2: The Claude Compliance API provides two distinct data access types to security integration partners: conversation content from Claude Enterprise, and activity events from both Claude Enterprise and Claude Platform

- **Evidence**: Direct product description: "All of these new integrations are powered by the Claude Compliance API, which gives enterprise security and compliance teams programmatic access to two types of data" followed by the enumeration of both types.
- **Confidence**: settled (first-party enumeration of data access types for a shipping feature)
- **Quote**: "All of these new integrations are powered by the Claude Compliance API, which gives enterprise security and compliance teams programmatic access to two types of data"
- **Our assessment**: This is the most architecturally significant claim in the post, and the one that creates a potential contradiction with the March 2026 Compliance API launch post (see Cross-References). The two-type data model is: (1) conversation content specifically from Claude Enterprise, and (2) activity events from both products. The Enterprise/Platform distinction in data type 1 is important — conversation content is NOT described as accessible for Claude Platform (API) deployments, only for Claude Enterprise (the productized SaaS offering for business users). See contradiction issue #858.

### Claim 3: Security partners can access conversation content from Claude Enterprise including chats, uploaded files, and projects

- **Evidence**: Direct enumeration: "Conversation content from Claude Enterprise — including chats, uploaded files, and projects"
- **Confidence**: settled (explicit first-party enumeration of content types)
- **Quote**: "Conversation content from Claude Enterprise — including chats, uploaded files, and projects"
- **Our assessment**: This claim is in direct tension with the original Compliance API launch post (March 2026, blog-anthropic-compliance-api.md), which stated "The API does not log inference activities, such as user interactions with the model or model activities." That claim has been filed as contradiction issue #858. The most likely interpretation: the March post described the Platform Compliance API's activity-event-only scope; this post announces that Claude Enterprise conversation content is also accessible to security partners (either as a newly-added capability or as a pre-existing Enterprise capability not previously documented). Either way, this updates the compliance architecture picture: teams using Claude Enterprise (not just Claude Platform) can now route conversation content to DLP and SIEM tools through standard integrations. See also Cross-References: Contradicts.

### Claim 4: Activity events — covering user logins, admin actions, and configuration changes — are accessible across both Claude Enterprise and Claude Platform

- **Evidence**: Direct enumeration: "Activity events across both Claude Enterprise and the Claude Platform — user logins, admin actions, and configuration changes"
- **Confidence**: settled (first-party enumeration with both products explicitly named)
- **Quote**: "Activity events across both Claude Enterprise and the Claude Platform — user logins, admin actions, and configuration changes"
- **Our assessment**: This corroborates and extends the March 2026 Compliance API note's claim about activity event logging (admin and resource events). The explicit "both Claude Enterprise and the Claude Platform" phrasing confirms that activity event logging spans both product lines — organizations using the API for agent workloads (Claude Platform) and organizations using the productized SaaS (Claude Enterprise) both have access to activity event data through the 28 partner integrations.

### Claim 5: The 28 integrations span eight distinct security and compliance tool categories

- **Evidence**: Direct category enumeration: "DLP, SASE, data security, SIEM and security operations, identity, eDiscovery, AI security posture management, and AI observability and telemetry infrastructure."
- **Confidence**: settled (first-party categorization of partner integrations)
- **Quote**: "DLP, SASE, data security, SIEM and security operations, identity, eDiscovery, AI security posture management, and AI observability and telemetry infrastructure."
- **Our assessment**: The eight categories reveal the breadth of enterprise security workflows that Anthropic is targeting with this announcement. Notable inclusions: (1) "AI security posture management" — a category that treats AI deployments as a security posture concern on par with cloud infrastructure; (2) "AI observability and telemetry infrastructure" — suggesting dedicated AI monitoring beyond conventional SIEM. The inclusion of eDiscovery is significant for regulated industries (legal, financial) where conversation content must be preserved and searchable. The SASE and SIEM categories confirm that Claude governance is being integrated into network-level (Cloudflare, Zscaler, Palo Alto) and event-management-level (Sumo Logic, ReliaQuest, Trellix) tooling.

### Claim 6: Governance parity — IT and security teams can govern Claude the same way they govern other enterprise applications

- **Evidence**: Direct framing: "Now IT and security teams can govern Claude across our platform and suite of products, the same way they govern other applications in their stack."
- **Confidence**: settled (first-party strategic framing describing an achieved capability)
- **Quote**: "Now IT and security teams can govern Claude across our platform and suite of products, the same way they govern other applications in their stack."
- **Our assessment**: This is the strategic claim behind the entire announcement. "Governance parity" — treating Claude like any other enterprise application in the security stack — is the design goal that the 28 integrations implement. The "same way" framing is operationally significant: it means no Claude-specific security tooling is required. Organizations can reuse existing DLP policies, SIEM correlation rules, and identity governance workflows. This shifts Claude from a governance exception (requiring bespoke security design) to a governed asset (fitting into existing security operations). The guide should present this as a maturity milestone for enterprise Claude deployment.

### Claim 7: Data from Claude flows directly into existing security dashboards and alerting workflows without custom integration per tool

- **Evidence**: Direct product description: "Connect and configure your Claude instance, and the data flows into the same dashboards and alerting workflows you use for everything else."
- **Confidence**: settled (first-party product description of the integration model)
- **Quote**: "Connect and configure your Claude instance, and the data flows into the same dashboards and alerting workflows you use for everything else."
- **Our assessment**: The "same dashboards" framing describes the operational benefit: security analysts see Claude activity in the same context as other application activity, enabling correlation without manual data export or custom tooling. For SOC teams, this is the difference between "Claude is a blind spot in our security posture" and "Claude activity is visible in our existing alert triage queue." This is the practical implementation of the governance parity claim (Claim 6). The guide should note that this requires organizations to first be on a supported partner platform — the integration is not generic; it is partner-specific.

### Claim 8: Customers connect through the Help Center; security, compliance, or IT platform providers can apply to join the integration network

- **Evidence**: Two distinct action items described: "To connect your Claude instance to a supported partner platform, visit our Help Center and review the Compliance API documentation." and "If you're a security, compliance, or IT platform that has built a Compliance API integration, apply here to join the network."
- **Confidence**: settled (first-party operational guidance)
- **Quote** (customer path): "To connect your Claude instance to a supported partner platform, visit our Help Center and review the Compliance API documentation."
- **Quote** (partner path): "If you're a security, compliance, or IT platform that has built a Compliance API integration, apply here to join the network."
- **Our assessment**: The two-path model (customer connection via Help Center; partner application via form) indicates the integration network is growing. The "apply here" partner path suggests the 28 partners are not exhaustive — additional tools can integrate via the Compliance API. For practitioners: if your organization uses a security tool not on the current 28-partner list, it may be worth checking whether that vendor has filed a Compliance API integration or can be prompted to do so. For the guide: document the Help Center as the starting point for enabling an integration, not a technical API configuration step.

## Concrete Artifacts

### Full Partner List (28 partners)

```
Claude Compliance API — Security Integration Partners (May 21, 2026)
(Anthropic, 2026-05-21)

Cloudflare, Cribl, CrowdStrike, Cyera, Datadog, Forcepoint, Fortinet,
Geordie AI, IBM Guardium, Microsoft Purview, Mimecast, Netskope, Okta,
Palo Alto Networks, Proofpoint, Relativity, ReliaQuest, Rubrik, SailPoint,
Smarsh, Snyk, Sumo Logic, Tenable, Theta Lake, Trellix, Varonis, Wiz,
Zscaler

Total: 28 partners
```

### Integration Category Map

```
Claude Compliance API — 8 Integration Categories (May 21, 2026)
(Anthropic, 2026-05-21)

From the post: "DLP, SASE, data security, SIEM and security operations,
identity, eDiscovery, AI security posture management, and AI observability
and telemetry infrastructure."

Category breakdown:
  DLP (Data Loss Prevention)
  SASE (Secure Access Service Edge)
  Data Security
  SIEM and Security Operations
  Identity
  eDiscovery
  AI Security Posture Management
  AI Observability and Telemetry Infrastructure
```

### Two Data Access Types for Security Partners

```
Claude Compliance API — Data Access Types (May 21, 2026)
(Anthropic, 2026-05-21)

Type 1: Conversation content
  - Source: Claude Enterprise only
  - Content: "chats, uploaded files, and projects"
  - Use case: DLP policies, security monitoring

Type 2: Activity events
  - Source: "both Claude Enterprise and the Claude Platform"
  - Events: "user logins, admin actions, and configuration changes"
  - Use case: SIEM, compliance, identity governance

Note: Conversation content access is limited to Claude Enterprise;
      Activity events span both Enterprise and Platform.
      See contradiction issue #858 re: conflict with March 2026 Compliance API note.
```

### Updated Compliance Architecture (accounting for both notes)

```
Enterprise Claude Compliance Architecture — Post-May 2026

Layer 1: Compliance API activity events (both Enterprise + Platform)
  - Admin events: workspace membership, API key creation, access changes
  - Resource events: file creation/download, skill deletion
  - Now feeds to 28 security partner tools via standard integrations

Layer 2: Conversation content (Claude Enterprise only)
  - Chats, uploaded files, projects
  - Accessible to DLP, eDiscovery, data security tools via partner integrations
  - CONTRAST: March 2026 note said conversations NOT logged (see C-NNN)

Layer 3: OTel agent action events (Claude Cowork, per blog-anthropic-cowork-enterprise)
  - Tool/connector calls, files read/modified, skills used, approval status
  - SIEM-compatible (Splunk, Cribl); correlatable with Compliance API via user ID

Still not covered first-party:
  - Inference content for Claude Platform (API) deployments
  - [The conversation gap persists for API-based agent workloads]
```

## Cross-References

- **Corroborates**: `blog-anthropic-cowork-enterprise.md` (Claim 3: OTel/SIEM integration) — The Cowork note established that Claude Cowork emits OpenTelemetry events compatible with Splunk and Cribl pipelines, with a shared user identifier for correlating with Compliance API records. This new note adds 28 dedicated security platform integrations (including Cribl explicitly in the partner list, and SIEM tools like Sumo Logic, ReliaQuest, Trellix). Together they form a two-path SIEM integration story: OTel events via Cowork for agent-action visibility, and Compliance API partner integrations for activity-event and conversation-content visibility. Both are first-party Anthropic capabilities.

- **Extends**: `blog-anthropic-compliance-api.md` — The March 2026 Compliance API note (issue #191) established the API itself, its two activity event categories, and the inference-logging exclusion. This new note documents the partner ecosystem built on top of that API, adds the conversation content access type for Claude Enterprise, and reveals that 28 enterprise security tools now integrate natively. The new note supersedes the original on scope of what's accessible through the API.

- **Contradicts**: `blog-anthropic-compliance-api.md` Claim 4 — The March 2026 note's Claim 4 states: "The API does not log inference activities, such as user interactions with the model or model activities." The new post's Claim 3 states that "Conversation content from Claude Enterprise — including chats, uploaded files, and projects" is accessible to security partners through the Compliance API. These two claims are materially inconsistent for Claude Enterprise deployments. **Contradiction issue filed: #858.** Do not treat either claim as the guide's settled position until #858 is resolved. The most likely verdict is `superseded` (the March note described Platform-only scope; the May note adds Enterprise conversation content as a new capability), but the resolver must confirm this.

- **Novel**:
  - **28-partner security integration network**: No prior corpus source documents a named set of enterprise security partners with native Compliance API integrations. This is the first ecosystem-scale governance announcement for Claude.
  - **Eight-category security taxonomy**: The specific categorization (DLP, SASE, data security, SIEM, identity, eDiscovery, AI security posture management, AI observability) is a new vocabulary for thinking about Claude's security integration surface.
  - **"AI security posture management" as a named category**: No prior corpus source names ASPM as a category relevant to Claude deployments. This signals that Anthropic is positioning Claude governance within the emerging ASPM discipline (alongside Snyk, Wiz, Tenable in the partner list).
  - **eDiscovery as a named integration use case**: The inclusion of Relativity and Smarsh (eDiscovery platforms) confirms that regulated-industry conversation preservation is a target use case for the Compliance API. This is the first explicit evidence that Anthropic's compliance story extends to legal hold and regulatory discovery workflows.
  - **Open partner network (application path)**: The explicit invitation for additional security tool vendors to apply to join the integration network establishes that the 28-partner list is not a closed set — it is a growing ecosystem.

## Guide Impact

- **Chapter on Enterprise Deployment / Governance (planned)**: Update the "what the platform provides vs. what you must build" compliance architecture section. The conversation content access claim (Claim 3) potentially fills the conversation-logging gap for Claude Enterprise users. If contradiction #858 resolves as `superseded` (likely), the guide should present a new two-tier model: for Claude Enterprise, conversation content is now accessible to security partners via Compliance API; for Claude Platform (API), the inference logging gap persists. This is a material change to the compliance architecture recommendation.

- **Chapter on Enterprise Deployment / Governance (planned)**: Add the governance parity framing (Claim 6) as a milestone marker: teams deploying Claude Enterprise can now achieve security governance parity with other SaaS applications in their stack. The 28-partner network is the practical implementation. Recommend that enterprise teams check their existing security tool vendor against the partner list and enable the integration from day one of Claude Enterprise deployment.

- **Chapter on Enterprise Deployment / Governance (planned)**: The eight-category integration taxonomy (Claim 5) provides a structured checklist for enterprise security teams assessing Claude governance coverage. The guide should use this taxonomy to audit coverage: DLP (is conversation content routing to your DLP tool?), identity (is Claude usage visible in your IdP audit logs?), eDiscovery (are chats captured for legal hold?), SIEM (are admin events flowing to your SOC dashboard?).

- **Chapter on Enterprise Deployment / Governance (planned)**: The open partner network (Claim 8, partner application path) has implications for tool selection. Recommend that teams evaluating enterprise security tools favor vendors that have already filed Compliance API integrations. For teams with existing security tools not on the 28-partner list, the "apply here" path signals that the vendor can pursue integration — worth raising in vendor conversations.

- **Chapter on Safety and Verification (Ch03)**: If contradiction #858 resolves as `superseded` (conversation content now accessible for Claude Enterprise), update the inference-logging guidance: the original note's Claim 4 ("teams must build their own conversation logging") still applies to Claude Platform (API-based agent workloads), but Claude Enterprise users now have a path to conversation content via Compliance API partner integrations. The guide should distinguish the two deployment models clearly on this point.

## Extraction Notes

- **Source is short** (~400 words). All substantive claims were fully extracted. No sub-pages were linked from the main content.
- **Verbatim quotes obtained**: All `Quote` fields in this note are character-for-character from the source as confirmed via repeated fetch attempts.
- **Contradiction issue filed**: The conversation content claim (Claim 3) contradicts the March 2026 Compliance API note's Claim 4 (inference/conversations excluded). Contradiction issue #858 was filed before this PR was opened, per MINER.md §4a. The resolution verdict will determine whether the guide's inference-logging guidance for Claude Enterprise needs to be updated.
- **Confidence calibration**: All claims are `settled` — this is a first-party Anthropic product announcement describing shipping capabilities with named partner companies. The overall note is `settled` because the feature existence, partner names, data access types, and integration categories are all definitively stated by the vendor.
- **No additional contradictions found**: The 28-partner network claim, eight-category taxonomy, governance parity framing, and customer/partner paths do not conflict with any other corpus source notes. The only contradiction is the conversation-content-vs-inference-exclusion tension with the March 2026 note, which has been filed.
