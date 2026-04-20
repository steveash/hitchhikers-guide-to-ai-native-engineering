---
source_url: https://claude.com/blog/claude-platform-compliance-api
source_type: blog-post
title: "Audit Claude Platform activity with the Compliance API"
author: Anthropic
date_published: 2026-03-30
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: settled
issue: "#191"
---

# Audit Claude Platform activity with the Compliance API

> Official Anthropic product announcement for the Claude Platform Compliance API — the authoritative definition of what enterprise audit logging covers (admin/resource activities) and critically what it does NOT cover (inference activities / model conversations), establishing the gap that regulated-industry teams must fill themselves.

## Source Context

- **Type**: blog-post (Anthropic official product announcement, published on claude.com; first-party authoritative description of a shipping production feature)
- **Author credibility**: Anthropic official communications. This is the definitive vendor description of the Compliance API scope and setup process. Claims about what is and is not logged are authoritative — no practitioner reverse-engineering or inference involved. The post is short and dense with concrete specifics, which is typical of Anthropic product announcements.
- **Scope**: Covers the Compliance API's two activity categories, what is explicitly excluded (inference/model activities), setup process, filtering capabilities, no-retroactive-logging constraint, and multi-organization unified feed support. Does NOT cover: API response schema or example payloads, rate limits, pricing, SLAs, retention periods, geographic data residency, or how the API compares to third-party alternatives. The Anthropic Trust Center documentation is referenced for full details but not reproduced in the post.

## Extracted Claims

### Claim 1: The Compliance API addresses a scaling failure in regulated-industry compliance — manual exports and periodic reviews cannot scale to the audit density required

- **Evidence**: Direct framing in the post: "Organizations in regulated industries—like financial services, healthcare, legal—need detailed records of who accessed what, when, and what changed. Without programmatic access to this data, compliance teams need to rely on manual exports and periodic reviews, which don't scale."
- **Confidence**: settled (stated problem framing by the vendor; consistent with well-understood enterprise compliance requirements)
- **Quote**: "Without programmatic access to this data, compliance teams need to rely on manual exports and periodic reviews, which don't scale."
- **Our assessment**: The scale argument is the motivation for the API's existence. The implication for practitioners: if your organization is manually exporting Claude Platform logs for compliance review, you are operating in a mode the Compliance API is designed to replace. The framing ("don't scale") also signals that Anthropic expects Claude usage density to grow to a point where manual review is not viable — the API is forward-looking infrastructure, not just a convenience.

### Claim 2: Admin and system activities — covering access and configuration changes — are logged

- **Evidence**: Explicit category definition from the post: "Actions that modify access or configuration of resources, like adding a member to a workspace, creating an API key, updating account settings, or modifying entity access."
- **Confidence**: settled (first-party feature description with enumerated examples)
- **Quote**: "Admin and system activities: Actions that modify access or configuration of resources, like adding a member to a workspace, creating an API key, updating account settings, or modifying entity access."
- **Our assessment**: This category covers the typical enterprise IAM audit trail: who got access, when, and via what mechanism. For regulated industries, these are the events that satisfy "who can access sensitive systems" requirements. The API key creation logging is particularly useful for security teams tracking credential proliferation across an organization. These events correspond to the "access layer" in a defense-in-depth compliance model.

### Claim 3: Resource activities — covering file and skill operations that may affect sensitive data — are logged

- **Evidence**: Explicit category definition: "User-driven actions that create or modify resource data, such as creating a file, downloading a file, or deleting a skill. These cover actions that may affect data or allow resources to access sensitive information, excluding direct interactions with the model."
- **Confidence**: settled (first-party feature description with enumerated examples)
- **Quote**: "Resource activities: User-driven actions that create or modify resource data, such as creating a file, downloading a file, or deleting a skill. These cover actions that may affect data or allow resources to access sensitive information, excluding direct interactions with the model."
- **Our assessment**: The inclusion of file downloads and skill deletions suggests Anthropic is treating data exfiltration risk and capability modification as the primary resource-layer threats. The explicit carve-out "excluding direct interactions with the model" within the resource activities definition (before the broader exclusion in Claim 4) is notable — Anthropic takes care to exclude inference even within resource-adjacent activities. This is a deliberate, repeated scope boundary.

### Claim 4: Inference activities — actual model conversations and interactions — are explicitly NOT logged by the Compliance API

- **Evidence**: Direct statement: "The API does not log inference activities, such as user interactions with the model or model activities." This is the single most consequential scope statement in the post.
- **Confidence**: settled (explicit first-party exclusion statement)
- **Quote**: "The API does not log inference activities, such as user interactions with the model or model activities."
- **Our assessment**: This is the load-bearing claim for enterprise compliance planning. Teams designing audit programs around the Compliance API must understand that they will have complete records of who set up the environment and what files were touched, but zero record of what the model was asked or what it said. For regulated industries with requirements around "what AI systems decided or recommended" (e.g., loan underwriting, clinical decision support, legal research), the platform's built-in compliance logging is insufficient on its own. Teams in these industries must implement application-layer conversation logging — either via their own infrastructure or via third-party tools — to capture inference activity. This is not a criticism of the Compliance API's design; it is a documentation of a known, explicit gap that practitioners must plan around.

### Claim 5: The activity feed supports filtering by time range, specific users, and API keys

- **Evidence**: Described in the post: "Admins can fetch activity logs filtered by time range, specific users, or API keys."
- **Confidence**: settled (first-party feature description)
- **Quote**: "Admins can fetch activity logs filtered by time range, specific users, or API keys."
- **Our assessment**: The filtering capability defines the practical query patterns for compliance workflows: security incident investigation (filter by user + time range), credential audit (filter by API key), and temporal reviews (filter by time range for periodic compliance reports). The absence of filtering by activity type in this list is notable — it is not clear whether the API supports "show me only API key creation events" without also pulling all other events and filtering client-side. This is a detail to confirm against the Trust Center documentation.

### Claim 6: Logging is not retroactive — the activity feed begins only from the point of enablement, with no access to historical pre-enablement events

- **Evidence**: Direct statement: "Logging begins once the API is enabled—historical activities prior to that point aren't available."
- **Confidence**: settled (explicit first-party limitation statement)
- **Quote**: "Logging begins once the API is enabled—historical activities prior to that point aren't available."
- **Our assessment**: This is the most operationally urgent constraint for organizations that have been using Claude Platform without the Compliance API. Any compliance gap review, incident investigation, or historical audit covering the period before enablement cannot use the Compliance API. Organizations enabling the API today have no retroactive access to membership changes, API key creation, or file operations that occurred previously. The practical implication: enable the Compliance API immediately upon deploying Claude Platform in a regulated context, not after an incident has already occurred.

### Claim 7: Multi-organization unified feed is supported — Claude Enterprise and Claude API organizations under the same parent can be filtered from a single activity feed

- **Evidence**: "Organizations that already use the Compliance API for Claude Enterprise can add their Claude API organization to the same parent organization and filter activity across both from a single feed."
- **Confidence**: settled (first-party feature description)
- **Quote**: "Organizations that already use the Compliance API for Claude Enterprise can add their Claude API organization to the same parent organization and filter activity across both from a single feed."
- **Our assessment**: This is the enterprise consolidation pattern — a single pane of glass for organizations running both Claude Enterprise (human users) and Claude API (programmatic access / agents). For teams building AI-native engineering workflows that combine Claude Code (consuming Claude API) with Claude Enterprise for their non-engineering users, this unified feed is operationally significant: one compliance integration point covers both populations. Without this, teams would need two separate compliance integrations and a merge/correlation step to get a complete picture.

### Claim 8: Setup requires contacting the account team to enable, followed by admin API key creation and activity feed endpoint querying

- **Evidence**: "Contact your account team to enable the Compliance API for your organization. Once enabled, create an admin API key and use it to query the activity feed endpoint."
- **Confidence**: settled (explicit setup procedure from the vendor)
- **Quote**: "Contact your account team to enable the Compliance API for your organization."
- **Our assessment**: The account-team-gated enablement model (rather than self-serve) is typical of enterprise compliance features that require explicit customer acknowledgment of scope and limitations. It is not technically complex, but it implies the API is not available by default — organizations that want it must actively request it. For enterprise teams planning compliance programs: include Compliance API enablement in the Claude Platform onboarding checklist, not as an afterthought after deployment.

## Concrete Artifacts

### Two-Category Activity Taxonomy

```
Claude Platform Compliance API — Activity Categories
(Anthropic, 2026-03-30)

LOGGED:
  Category 1 — Admin and system activities:
    - Adding a member to a workspace
    - Creating an API key
    - Updating account settings
    - Modifying entity access
    - [General: "actions that modify access or configuration of resources"]

  Category 2 — Resource activities:
    - Creating a file
    - Downloading a file
    - Deleting a skill
    - [General: "user-driven actions that create or modify resource data...
      that may affect data or allow resources to access sensitive information"]

  Additionally logged (per post):
    - User login and logout events
    - Account setting updates
    - Workspace changes
    - Other organizational audit events

NOT LOGGED:
  - Inference activities
  - User interactions with the model
  - Model activities (responses, outputs)
```

### Setup Procedure

```
Claude Platform Compliance API — Setup Steps
(Anthropic, 2026-03-30)

1. Contact account team to enable the Compliance API for your organization
   [Note: not self-serve; requires explicit enablement request]

2. Create an admin API key

3. Query the activity feed endpoint
   [Documentation: Anthropic Trust Center]

Constraints:
  - Logging begins at enablement date; no retroactive access
  - Multi-org: add Claude API org to same parent as Claude Enterprise
    org to get unified feed across both
```

### Enterprise Compliance Gap Matrix

```
Enterprise AI Compliance Requirement            | Compliance API | Must Build Yourself
------------------------------------------------|----------------|--------------------
Who was added/removed from the workspace?       | ✓ COVERED      |
When were API keys created/deleted?             | ✓ COVERED      |
What account settings were changed?             | ✓ COVERED      |
Who accessed or deleted files?                  | ✓ COVERED      |
What prompts were sent to the model?            |                | ✗ NOT COVERED
What did the model respond with?                |                | ✗ NOT COVERED
What model was used for a conversation?         |                | ✗ NOT COVERED
What were the model's recommendations?          |                | ✗ NOT COVERED
```

## Cross-References

- **Corroborates**: `blog-ghaw-agent-observability.md` — The GitHub Agent Factory's three-tier observability architecture (performance tracking / cost optimization / meta-audit) addresses agent-fleet observability; the Compliance API addresses platform/organization-level access and resource audit logging. Both sources independently establish that observability in AI systems requires multiple distinct layers: the Compliance API is the "who did what to the environment" layer, while the ghaw observatory covers "what are agents doing operationally." Neither alone constitutes complete observability for a regulated-industry AI deployment. The ghaw three-tier split and the Compliance API's two-category split address non-overlapping concerns.

- **Corroborates**: `blog-anthropic-claude-code-auto-mode.md` — The auto mode source documents that auto mode classifies agent actions for safety and does NOT audit inference content in the compliance sense. Both sources reflect a consistent Anthropic architecture: platform-level audit logging (Compliance API) covers the access/resource layer, while action classification (auto mode classifier) covers the danger-assessment layer. Neither is designed to produce a record of what the model said. Together they establish what audit and safety capabilities exist at the platform level — and what the inference-logging gap means across both systems.

- **Extends**: `blog-ghaw-agent-observability.md` — That source establishes the observatory as a first-class architectural component for agent fleets. This source adds the platform-level compliance layer: before teams can instrument their agent fleets, they need the foundational access-and-resource audit trail that the Compliance API provides. The two sources together give a more complete picture: platform audit logging (Compliance API) → agent fleet observability (ghaw observatory pattern). The Compliance API is infrastructure; the observatory is the intelligence layer on top of it.

- **Novel**:
  - **The inference-logging gap as an explicitly documented vendor limitation**: No other source in our corpus cites Anthropic explicitly stating that model conversation content is excluded from platform compliance logging. This is the first vendor-authoritative statement of the gap that regulated-industry teams must plan around.
  - **No-retroactive-logging constraint**: The "logging begins at enablement" constraint is not documented in any other source. It has direct operational implications for incident response.
  - **Multi-org unified feed pattern**: The Claude Enterprise + Claude API unified feed under a parent org is not described in any other corpus source. For teams running hybrid human-user + agent deployments, this is the enterprise audit consolidation mechanism.

## Guide Impact

- **Chapter on Enterprise Deployment / Governance** (planned): The Compliance API should anchor a "What the platform provides vs. what you must build" section. The two-category coverage (admin/resource) and the inference exclusion together define the practitioner's compliance architecture decision: use the Compliance API for access/config/resource auditing; build application-layer logging for conversation content auditing. The no-retroactive-logging constraint should appear as a checklist item in any Claude Platform onboarding guide: "Enable Compliance API before users begin using the platform, not after."

- **Chapter on Enterprise Deployment / Governance** (planned): The multi-org unified feed (Claim 7) is directly relevant for teams running AI-native engineering workflows that combine Claude API (agents/Claude Code) with Claude Enterprise (human users). Recommend that such teams configure the unified parent org from day one, not retroactively.

- **Chapter on Safety and Verification (Ch03)**: The inference-logging gap has implications for any "verification" claim at the enterprise level. Anthropic's auto mode (blog-anthropic-claude-code-auto-mode) classifies and blocks dangerous actions but does not produce a conversation audit trail. The Compliance API logs access and resource changes but not conversation content. The guide should be explicit: there is currently no first-party Anthropic mechanism that gives regulated industries a complete record of what Claude was asked and what it said. Teams building compliance programs around Claude Platform must supplement with their own conversation logging.

- **Chapter on Observability (if separate from Ch03)**: Distinguish platform-level audit logging (Compliance API) from agent-level observability (metrics, traces, cost analysis). Both are required for enterprise AI deployments; they address different concerns and cannot substitute for each other.

## Extraction Notes

- **Source is intentionally short**: This is a product announcement post (~350 words). The post's brevity reflects the feature's bounded scope — the Compliance API is a specific, well-defined capability, not a broad platform. All substantive claims were fully extracted; there is no deeper content to find in this post.
- **No linked sub-pages followed**: The post references the "Anthropic Trust Center" for full documentation but does not provide a URL. The Trust Center documentation would contain the API schema, response format, endpoint URL, and rate limits — this post does not.
- **Source is post-cutoff (March 30, 2026)**: This is a new feature with no prior documentation in the corpus. All claims are novel relative to existing source notes.
- **Prospector alignment**: Both Prospector triage comments correctly identified the inference-logging exclusion as the primary extractable insight and listed the same four concrete facts (two activity categories, inference exclusion, no-retroactive-logging, multi-org support). All four were confirmed and extracted. The Prospector's identification of Ch03 and enterprise governance as the relevant chapters is confirmed.
