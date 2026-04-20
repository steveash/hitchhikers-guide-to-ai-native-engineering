---
source_url: https://github.blog/changelog/2026-04-15-enable-copilot-cloud-agent-via-custom-properties
source_type: docs
title: "Enable Copilot cloud agent via custom properties"
author: GitHub (official changelog)
date_published: 2026-04-15
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: anecdotal
issue: "#172"
---

# Enable Copilot Cloud Agent via Custom Properties (GitHub Changelog)

> GitHub's official announcement of per-organization selective enablement for
> Copilot Cloud Agent (CCA) via custom properties and a new REST API, documenting
> the progressive-rollout model for enterprise AI agent adoption and a non-obvious
> footgun: custom property matching is evaluated once at configuration time, so
> future property changes do not retroactively update CCA access.

## Source Context

- **Type**: docs (GitHub official product changelog, ~300 words + linked API
  reference pages at `docs.github.com/enterprise-cloud@latest/rest/copilot/
  copilot-coding-agent-management` and the CCA management how-to guide)
- **Author credibility**: GitHub engineering team announcing a production API
  change. Authoritative for the fact that these endpoints exist, what they do,
  and the stated behavioral semantics. Not a credible source for whether the
  progressive-rollout model produces better outcomes than enterprise-wide
  enablement — that claim is vendor framing with no empirical support.
- **Scope**: Three new enterprise-level API endpoints for CCA policy management,
  plus the custom-property matching mechanism for bulk org selection. Covers the
  UI path for non-API management. Does NOT cover: CCA's underlying task
  capabilities, how CCA compares to other AI coding assistants, cost implications
  of CCA usage by organization, what happens to in-flight CCA tasks if an org
  is disabled, or failure modes of the custom-property-based selection. The API
  reference pages (fetched separately) also document organization-level
  repository-scoped restriction endpoints in public preview.

## Extracted Claims

### Claim 1: Enterprise admins can now selectively enable CCA for specific organizations using custom property filters or direct org selection

- **Evidence**: Official GitHub product changelog announcing the feature as
  generally available. The REST API endpoints are documented and versioned
  (`X-GitHub-Api-Version: 2026-03-10`).
- **Confidence**: settled (these endpoints exist — this is a product fact)
- **Quote**: "provides the flexibility to pilot CCA with select teams,
  progressively expand access, and manage adoption at your own pace"
- **Our assessment**: The capability is real and settled. Before this, enterprise
  policy was coarser-grained. The practical implication for enterprise adoption
  patterns is significant: teams can now run a genuine controlled pilot (specific
  orgs only) before committing to enterprise-wide enablement. The vendor framing
  ("flexibility," "manage at your own pace") is marketing; the underlying
  capability — per-org API-driven enablement — is the extractable signal.

### Claim 2: Custom property matching is evaluated exactly once at configuration time — future property changes do not retroactively update CCA access

- **Evidence**: Stated explicitly in both the changelog and the linked API
  reference. The changelog warns: "using custom properties to enable CCA is
  evaluated once at the time of configuration. Organizations will not be
  automatically enabled or disabled for CCA if the custom property is added,
  removed, or modified later." The API reference confirms: "This is a one-time
  operation, setting the property on an organization in the future will not
  automatically update its coding agent policy."
- **Confidence**: settled (explicitly documented behavioral constraint)
- **Quote**: "using custom properties to enable CCA is evaluated once at the time
  of configuration. Organizations will not be automatically enabled or disabled
  for CCA if the custom property is added, removed, or modified later."
- **Our assessment**: This is the most practically important claim in the source.
  It is a footgun for enterprise admins who reason about custom properties as
  live policy filters (the mental model from Attribute-Based Access Control
  systems). In this implementation, custom properties are a one-time batch
  selector, not a continuous policy condition. An admin who adds a custom property
  `copilot-cca-pilot: true` to new organizations after initial configuration will
  find those organizations do NOT get CCA access automatically — they must issue
  a new POST request. Similarly, removing the property does not revoke access.
  Any enterprise CCA rollout playbook must document this behavior prominently to
  prevent silent access drift.

### Claim 3: Three enterprise-level API endpoints provide programmatic CCA management

- **Evidence**: API reference documentation at
  `docs.github.com/enterprise-cloud@latest/rest/copilot/copilot-coding-agent-management`.
  All three endpoints require `manage_billing:copilot` or `admin:enterprise` scope
  and `X-GitHub-Api-Version: 2026-03-10`.
- **Confidence**: settled (documented and versioned in the official REST API)
- **Quote**: N/A (endpoint definitions stated directly in API reference)
- **Our assessment**: The API surface is clean and consistent. The three-endpoint
  pattern (set policy, add orgs, remove orgs) gives enterprise admins the
  primitives needed to build CCA rollout automation — e.g., an onboarding script
  that enables CCA when a new organization is provisioned. The 204-or-400 response
  pattern is simple. The required API version header (`2026-03-10`) means this API
  may change; any automation script that calls these endpoints should pin the
  version header explicitly and monitor for deprecation.

### Claim 4: Four policy states control enterprise CCA deployment scope

- **Evidence**: `policy_state` parameter documented in the PUT endpoint.
- **Confidence**: settled (documented API parameter values)
- **Quote**: N/A (enum values listed in API reference)
- **Our assessment**: The four states map to a spectrum of centralization:
  `enabled_for_all_orgs` (all-in, enterprise decides), `disabled_for_all_orgs`
  (off, enterprise decides), `enabled_for_selected_orgs` (selective, enterprise
  manages the list), and `configured_by_org_admins` (delegated, orgs decide
  within their own settings). The last state is noteworthy for adoption patterns:
  it shifts responsibility to org admins, which may accelerate adoption in
  federated enterprises but removes enterprise-level visibility into who has CCA
  enabled. For Ch07 (enterprise governance): the `configured_by_org_admins`
  state is a governance decision, not just a technical one.

### Claim 5: CCA is enabled for ALL repositories within selected organizations by default; repository-level restriction is a separate, organization-level concern

- **Evidence**: Management how-to docs state: "By default, the agent will be
  available in all repositories in selected organizations." Org-level repository
  restriction is handled via separate public-preview endpoints at
  `/orgs/{org}/copilot/coding-agent/permissions/repositories`.
- **Confidence**: settled (stated in official documentation)
- **Quote**: "By default, the agent will be available in all repositories in
  selected organizations."
- **Our assessment**: The default is permissive. Enterprise admins enabling CCA
  for an organization should understand this means ALL repos in that org get CCA
  by default — including internal tooling repos, repos with sensitive data, or
  repos where autonomous agent access may be undesirable. The repository-level
  restriction API exists but is in public preview and must be configured
  separately by org admins. This creates a gap: an enterprise rollout that
  selects orgs via the enterprise API does not automatically inherit repository
  exclusions. Practitioners doing CCA rollouts should document a three-step
  sequence: (1) set enterprise policy, (2) select orgs, (3) have org admins
  configure repo exclusions before the policy goes live.

### Claim 6: MCP Registry URL and Restrict MCP access policies do NOT apply to Copilot Cloud Agent

- **Evidence**: Management how-to docs explicitly note: "The 'MCP Registry URL'
  and 'Restrict MCP access to registry servers' policies do not apply to Copilot
  cloud agent."
- **Confidence**: settled (explicitly documented exception)
- **Quote**: "The 'MCP Registry URL' and 'Restrict MCP access to registry
  servers' policies do not apply to Copilot cloud agent."
- **Our assessment**: This is a second footgun, qualitatively different from the
  custom-property timing issue. Enterprise admins who configure MCP access
  restrictions to control what external services their Copilot users can connect
  to will find those restrictions do not cover CCA. CCA operates under different
  MCP governance. This matters most for enterprises that allow third-party MCP
  servers (e.g., error-tracking integrations) — the restriction policy they set
  does not gate what CCA can access. Security-conscious enterprises must review
  CCA's MCP access separately from their standard Copilot MCP policy.

### Claim 7: The prescribed enterprise adoption pattern is pilot-first progressive rollout

- **Evidence**: The changelog's stated framing and the management docs recommend
  "run a trial before enabling Copilot cloud agent for the enterprise" via the
  piloting process.
- **Confidence**: anecdotal (vendor recommendation without supporting data on
  outcomes of pilot-first vs. all-at-once rollouts)
- **Quote**: "provides the flexibility to pilot CCA with select teams,
  progressively expand access, and manage adoption at your own pace"
- **Our assessment**: The pilot-first recommendation is sensible engineering
  practice and consistent with standard enterprise feature rollout norms — but
  it is vendor guidance, not empirical evidence that pilot-first adoption produces
  better outcomes for CCA. The feature supports this pattern (per-org enablement
  is the mechanism); whether it produces better outcomes than immediate
  enterprise-wide enablement is unstudied. For Ch07: cite this as GitHub's own
  recommended rollout pattern, paired with the custom-property footgun (Claim 2)
  as the operational caveat that makes the pattern harder to automate than it
  appears.

## Concrete Artifacts

### Enterprise-Level CCA Management API (API version 2026-03-10)

```
Required headers (all enterprise endpoints):
  Authorization: Bearer <token>
  Accept: application/vnd.github+json
  X-GitHub-Api-Version: 2026-03-10

Required scopes: manage_billing:copilot OR admin:enterprise

---

1. Set enterprise CCA policy
   PUT /enterprises/{enterprise}/copilot/policies/coding_agent
   Body: { "policy_state": "<state>" }

   policy_state values:
     enabled_for_all_orgs      — CCA on for every org
     disabled_for_all_orgs     — CCA off for every org
     enabled_for_selected_orgs — CCA on for specific orgs only
     configured_by_org_admins  — delegates to each org's own admin

   Response: 204 (success) | 400 (bad request)

---

2. Add organizations to CCA policy
   POST /enterprises/{enterprise}/copilot/policies/coding_agent/organizations
   Body (option A — direct org list):
     { "organizations": ["org-login-1", "org-login-2"] }
   Body (option B — custom property filter):
     { "custom_properties": [
         { "property_name": "<name>", "values": ["<val1>", "<val2>"] }
       ]
     }

   ⚠️ FOOTGUN: custom_properties evaluated once at invocation time.
   Adding/removing the property from an org later has NO effect.

   Response: 204 (success) | 400 (bad request)

---

3. Remove organizations from CCA policy
   DELETE /enterprises/{enterprise}/copilot/policies/coding_agent/organizations
   Body: same structure as POST (org list or custom_properties)

   Response: 204 (success) | 400 (bad request)
```

### Organization-Level Repository Restriction API (public preview)

```
Required scope: admin:org

GET    /orgs/{org}/copilot/coding-agent/permissions
         → { "enabled_repositories": "all" | "selected" | "none" }

PUT    /orgs/{org}/copilot/coding-agent/permissions
         Body: { "enabled_repositories": "all" | "selected" | "none" }

GET    /orgs/{org}/copilot/coding-agent/permissions/repositories
         → paginated list of enabled repositories

PUT    /orgs/{org}/copilot/coding-agent/permissions/repositories
         Body: { "selected_repository_ids": [<id1>, <id2>] }

PUT    /orgs/{org}/copilot/coding-agent/permissions/repositories/{repository_id}
         → enable single repo (only when policy is "selected")

DELETE /orgs/{org}/copilot/coding-agent/permissions/repositories/{repository_id}
         → disable single repo (only when policy is "selected")
```

### UI Navigation Path

```
GitHub.com → Enterprise Settings
  → [Copilot icon at top] → AI Controls
  → Agents (left sidebar)
  → Copilot Cloud Agent (under "Available agents")
  → Set global policy
  → If "Enabled for selected organizations": select orgs in UI
    (custom property selection requires REST API, not available in UI)
```

### Enterprise CCA Rollout Sequence (synthesized from docs)

```
Step 1: Set enterprise policy
  PUT /enterprises/{enterprise}/copilot/policies/coding_agent
  { "policy_state": "enabled_for_selected_orgs" }

Step 2: Enable pilot organizations
  POST /enterprises/{enterprise}/copilot/policies/coding_agent/organizations
  { "organizations": ["pilot-org-1", "pilot-org-2"] }
  OR custom_properties (evaluated once — snapshot, not live filter)

Step 3: Org admins configure repo exclusions (if needed)
  PUT /orgs/{org}/copilot/coding-agent/permissions
  { "enabled_repositories": "selected" }
  + enumerate restricted repos via repository endpoints

Step 4: Expand rollout (repeat step 2 for additional orgs)
  NOTE: custom_properties from step 2 do NOT auto-enroll new orgs —
  must re-POST with new org names or re-run property filter.

⚠️ MCP caveat: Copilot MCP Registry URL / Restrict MCP access policies
  do NOT apply to CCA — review CCA MCP access separately.
```

## Cross-References

- **Corroborates** `docs-github-copilot-pr-review-metrics.md` in type and scope:
  both are official GitHub changelog entries documenting enterprise-tier Copilot
  API surface. That source covers measurement primitives (PR review metrics API);
  this source covers governance primitives (CCA enablement API). Together they
  show GitHub extending its enterprise API control surface to cover both measuring
  Copilot use and managing AI agent access — two complementary enterprise concerns.
- **Extends** `docs-github-copilot-pr-review-metrics.md`: the PR review metrics
  note documents measuring what Copilot does after it's been enabled; this source
  documents controlling whether and where CCA is enabled in the first place. The
  governance layer (this source) is logically prior to the measurement layer (that
  source) in a mature enterprise rollout.
- **Complements** `blog-cursor-security-agents.md` (Claim 1 — progressive trust
  model): Cursor's security agent deployment describes a trust escalation path
  (shadow mode → suggestion → blocking). This source describes the organizational
  equivalent — progressive rollout at the organization level (pilot orgs → expand).
  Both instantiate the same principle: don't deploy AI agents enterprise-wide
  without a controlled expansion path. The level of analysis differs (repository
  pipeline vs. enterprise policy), but the underlying governance model is the same.
- **Relevant to** `blog-faros-claude-code-roi.md` (Claim 4 — measurement
  framework): Faros's three-layer framework begins with adoption measurement.
  This source provides the governance mechanism by which adoption is controlled
  — selective org enablement is the upstream decision that shapes what adoption
  metrics can be measured downstream. A team tracking Copilot ROI should track
  which orgs are CCA-enabled and when, since the custom-property footgun means
  that cohort membership can silently drift without re-POSTing.
- **Novel**: 
  - First source in corpus to document the CCA enterprise management API surface
    specifically (three endpoints, four policy states, custom-property evaluation
    semantics).
  - The custom-property one-time evaluation footgun is entirely new to the corpus
    — no existing source discusses the gap between expected continuous-policy and
    actual snapshot-evaluation semantics in any enterprise AI tool configuration.
  - The MCP policy exception (CCA is exempt from enterprise MCP Registry and
    Restrict MCP Access policies) is a new enterprise security consideration not
    documented in any other source note.
  - No source in corpus previously documents the full three-step enterprise CCA
    rollout sequence (enterprise policy → org selection → repo exclusion) and its
    interaction with defaults (all repos in selected org = enabled by default).

## Guide Impact

### Chapter 07: Enterprise AI Adoption and Governance (planned or equivalent)

- **Section "Progressive AI agent rollout"**: Use this changelog as the canonical
  example of how GitHub itself prescribes phased enterprise AI agent adoption.
  The per-org enablement API is the mechanism; the pilot-first recommendation is
  the practice. Reference Claim 1 (the capability) and Claim 7 (the pattern).
  Be explicit that the pattern requires manual expansion — the custom-property
  evaluation footgun (Claim 2) means it does not self-propagate as the enterprise
  grows.
- **Section "Enterprise AI governance footguns"** (new section if not present):
  Add two specific gotchas from this source:
  1. Custom property filters snapshot-at-configuration, not live-filter. New orgs
     that match the filter after the POST call will NOT be automatically enrolled.
  2. MCP Registry URL and Restrict MCP Access policies do NOT apply to CCA. If
     your MCP governance policy is important, audit CCA's MCP configuration
     separately.
- **Section "API-driven governance"**: Reference the three enterprise endpoints
  as the recommended approach for automating CCA rollout in large enterprises.
  Note the `X-GitHub-Api-Version: 2026-03-10` requirement and the need to pin
  this version in any automation tooling.

### Chapter 02: AI Coding Assistants / Copilot

- **Section "Deploying Copilot in an enterprise"**: Add the CCA-specific rollout
  sequence (enterprise policy → org selection → repo restriction) as a concrete
  procedure. Distinguish between the enterprise-level enablement API (this source)
  and the org-level repository restriction API (in public preview) and note that
  repo-level restrictions are NOT applied by default. A team that enables CCA for
  an org without configuring repo restrictions implicitly exposes all repos in
  that org to CCA.

## Extraction Notes

1. **Two web fetches**: The primary changelog page was fetched once (the core claims
   and the custom-property footgun). The API reference page at
   `docs.github.com/enterprise-cloud@latest/rest/copilot/copilot-coding-agent-management`
   was fetched separately and provided the full endpoint schema, request body
   structure, and additional footgun details. The management how-to guide at
   `docs.github.com/enterprise-cloud@latest/copilot/how-tos/administer-copilot/
   manage-for-enterprise/manage-agents/manage-copilot-cloud-agent` was also fetched
   and provided the UI navigation path, repo-default behavior, and MCP policy exception.
2. **Source is intentionally brief**: The changelog itself is ~300 words; the
   substance is in the linked API reference and management guide. The extraction
   above reflects reading all three pages. Claims were fully exhausted in 7 items.
3. **Vendor framing quarantined**: The "pilot CCA with select teams, progressively
   expand access" language is vendor marketing without supporting data. It is
   extracted as a pattern recommendation (Claim 7) but flagged as anecdotal.
4. **No contradictions to file**: No existing source note claims enterprise AI
   agents should be enabled all-at-once rather than progressively, or that custom
   property filters should be live. The footgun claims in this source are novel
   to the corpus, not contradictions of existing claims.
5. **Public preview caveat**: The organization-level repository restriction
   endpoints are in public preview as of April 2026 and may change. The enterprise
   policy endpoints (three main endpoints) appear to be generally available.
6. **CCA capabilities not covered**: Neither the changelog nor the linked docs
   describe what CCA actually does (what tasks it performs, how it executes code,
   how it differs from Copilot in the IDE). This source covers governance, not
   capability. Any guide section discussing CCA capabilities must reference other
   sources.
