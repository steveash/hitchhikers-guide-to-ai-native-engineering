---
source_url: https://claude.com/blog/compliance-api-cowork-and-claude-code
source_type: blog-post
title: "Compliance API coverage extends to Claude Cowork and Claude Code"
author: Anthropic
date_published: 2026-08-11
date_extracted: 2026-08-12
last_checked: 2026-08-12
status: current
confidence_overall: settled
issue: "#2638"
---

# Compliance API coverage extends to Claude Cowork and Claude Code

> Official Anthropic product announcement extending the Claude Compliance API (beta, Claude Enterprise customers) to cover Claude Cowork (desktop, web, mobile) and Claude Code (CLI, desktop) with a single consolidated per-session transcript containing prompts, responses, and tool activity — explicitly excluding Claude Code on the web, Claude Code via the Claude Platform, and sessions on Bedrock/Vertex AI/Microsoft Foundry, and adding further evidence to the still-unresolved Enterprise-vs-Platform inference-logging contradiction (issue #858).

## Source Context

- **Type**: blog-post (Anthropic official product announcement, published on claude.com, category "Enterprise AI" / "Product announcements," dated August 11, 2026, 5-minute read, no individual byline; first-party authoritative description of a shipping beta feature).
- **Author credibility**: Anthropic official communications. As with the two prior Compliance API posts already in the corpus (`blog-anthropic-compliance-api.md`, `blog-anthropic-compliance-api-security-partners.md`), this is the vendor's own definitive description of what the API covers and excludes — no practitioner reverse-engineering or third-party validation involved.
- **Scope**: Covers the extension of Compliance API session endpoints to Cowork and Claude Code, the two data types in a session record (session content, session metadata), the explicit beta exclusions, the API's coexistence with existing OpenTelemetry exports, and the enablement path. Does **not** cover: the session endpoint's URL/schema in machine-readable form, retention periods, rate limits, pricing, a GA timeline, or how "verified user ID" is established. The post is intentionally short (~350 words), consistent with the two prior Compliance API announcements in the corpus.

## Extracted Claims

### Claim 1: Compliance API coverage now extends to Claude Cowork (desktop app, web, and mobile) and Claude Code (CLI and desktop app), in beta for Claude Enterprise customers
- **Evidence**: Opening statement of the post.
- **Confidence**: settled (first-party launch announcement)
- **Quote**: "Claude's Compliance API now covers Cowork across the desktop app, web, and mobile, as well as Claude Code in the CLI and desktop app. Coverage is in beta for Claude Enterprise customers."
- **Our assessment**: This is the headline claim — the same Compliance API interface that already covered Claude Enterprise chats now spans two additional product surfaces. The "Claude Enterprise customers" gate is notable: this is scoped to Enterprise, not Claude Platform (API) customers, echoing the Enterprise/Platform product-line split that the (still-unresolved) Assayer assessment on contradiction issue #858 identified as the key mediating variable for compliance API scope. See Cross-References.

### Claim 2: The new session endpoints are additive — nothing changes about data already pulled from the Compliance API today
- **Evidence**: Direct statement immediately following the launch claim.
- **Confidence**: settled (first-party statement about API stability/compatibility)
- **Quote**: "The new endpoints are additive: nothing changes about the data you already pull from the Compliance API today."
- **Our assessment**: This is a compatibility guarantee for existing integrators — the 28 named security partners (`blog-anthropic-compliance-api-security-partners.md`) and any customer-built pipeline against the original admin/resource activity feed (`blog-anthropic-compliance-api.md`) do not need to change anything to keep working. New session-level data is opt-in via new endpoints, not a breaking schema change to the existing feed.

### Claim 3: The purpose is to close an audit gap — compliance and security teams previously needed separate logging infrastructure per surface, and Cowork/Claude Code sessions did not appear alongside Claude chats
- **Evidence**: Direct framing statement under the opening section.
- **Confidence**: settled (vendor's own problem framing, consistent with the "manual exports don't scale" framing in the original March 2026 Compliance API post)
- **Quote**: "Security and compliance teams rely on the Compliance API to see how Claude is used across their organization — for audits and eDiscovery — without deploying separate logging infrastructure for each surface. Extending coverage to Cowork and Claude Code closes a gap: those sessions now show up alongside Claude chats."
- **Our assessment**: The explicit naming of "eDiscovery" as a use case directly corroborates the eight-category integration taxonomy in `blog-anthropic-compliance-api-security-partners.md` (which names eDiscovery as one of the 28-partner integration categories, backed by partners Relativity and Smarsh). This confirms that closing the Cowork/Claude Code gap was motivated by the same regulated-industry discovery/audit use case already documented for Claude Enterprise chats, not a distinct new use case.

### Claim 4: New session endpoints return a single consolidated, server-hosted transcript per Cowork or Claude Code session, combining prompts, responses, and tool activity into one session record
- **Evidence**: Direct description under "How it works."
- **Confidence**: settled (first-party technical description of the data model)
- **Quote**: "The new session endpoints return a consolidated, server-hosted transcript for each Cowork and Claude Code session, so prompts, responses, and tool activity come back together in a single session record."
- **Our assessment**: The "single session record" framing is architecturally significant for compliance tooling: rather than reconstructing a session from separately-timestamped events (as the original admin/resource activity feed requires), an auditor can pull one record per session that already contains the full prompt/response/tool-activity narrative. This is a materially richer unit of audit data than anything documented in the two prior Compliance API notes, both of which describe discrete *events* (membership changes, file operations), not consolidated *session transcripts*.

### Claim 5: Each session record carries two kinds of data — session content (prompts, responses, tool call content, skills and artifacts content) and session metadata (verified user ID/email, org ID, session/message IDs, timestamps)
- **Evidence**: Direct two-part enumeration under "How it works."
- **Confidence**: settled (first-party schema-level enumeration)
- **Quote**: "Session content: prompts and responses, tool calls content (web and MCP), and skills and artifacts content captured as transcript text." / "Session metadata: verified user ID and email address, organization ID, session and per-message IDs, and timestamps."
- **Our assessment**: This is the claim with the most direct bearing on the Enterprise/Platform inference-logging tension. "Session content" explicitly includes "prompts and responses" captured "as transcript text" — full conversational content, not just event metadata. This is the same category of claim ("conversation content is accessible") that the May 2026 security-partners post made for Claude Enterprise chats, now extended to two more surfaces (Cowork, Claude Code). See Cross-References → Contradicts for how this interacts with the original March 2026 note's "no inference logging" claim and the open contradiction issue #858.

### Claim 6: The beta explicitly excludes Claude Code on the web, Claude Code accessed through the Claude Platform, and sessions run on Amazon Bedrock, Google Cloud's Vertex AI, or Microsoft Foundry
- **Evidence**: Direct scope-limitation statement under "How it works."
- **Confidence**: settled (explicit first-party exclusion list)
- **Quote**: "This beta doesn't include Claude Code on the web, Claude Code accessed through the Claude Platform, or sessions run on Amazon Bedrock, Google Cloud's Vertex AI, or Microsoft Foundry."
- **Our assessment**: Two distinct exclusion categories are bundled here. (1) A surface-level exclusion (Claude Code on the web) that is presumably a beta sequencing gap, expected to close over time. (2) A product-line exclusion ("Claude Code accessed through the Claude Platform") that is architecturally significant: it confirms Claude Code has (at least) two deployment paths — one associated with Claude Enterprise (CLI/desktop, now covered) and one associated with Claude Platform/API (explicitly excluded from this session-content coverage). This independently corroborates the Enterprise-vs-Platform mediating variable identified in the unresolved Assayer assessment on issue #858: session/conversation content coverage is expanding for Enterprise-adjacent surfaces while remaining absent for Claude Platform. (3) Cloud-provider hosting exclusions (Bedrock, Vertex AI, Microsoft Foundry) — consistent with the general pattern that first-party Anthropic compliance tooling lags on hyperscaler-hosted deployments, also seen in `blog-anthropic-claude-desktop-cloud-platforms.md`'s GCC High/DoD beta scoping.

### Claim 7: The Compliance API is designed to coexist with existing OpenTelemetry exports, requiring no additional infrastructure on the customer's side
- **Evidence**: Direct statement under "How it works."
- **Confidence**: settled (first-party interoperability statement)
- **Quote**: "Organizations already exporting OpenTelemetry data can keep it running: the Compliance API can work alongside it with no infrastructure required on your side."
- **Our assessment**: This directly confirms and extends `blog-anthropic-cowork-enterprise.md` Claim 3, which documented Cowork's OTel event stream (tool/connector calls, file operations, approval status) as SIEM-compatible and correlatable with Compliance API records via a shared user identifier. This new post clarifies the relationship is explicitly non-competing by design — organizations do not have to choose between OTel-based agent-action observability and Compliance API session-content audit; both can run simultaneously against the same underlying sessions.

### Claim 8: Coverage for Cowork and Claude Code is available immediately using an organization's existing Compliance Access Key, with no separate integration to build
- **Evidence**: Direct statement under "Getting started."
- **Confidence**: settled (first-party operational/enablement description)
- **Quote**: "Coverage for Cowork and Claude Code is available today and included with the Compliance API using your existing Compliance Access Key – there's no separate integration to build. If it's already enabled for your organization, query the new session endpoints directly. If not, review the Compliance API documentation to enable it."
- **Our assessment**: For organizations that already enabled the Compliance API per the original March 2026 setup procedure (contact account team → create admin API key → query activity feed endpoint, per `blog-anthropic-compliance-api.md`), this new session coverage requires zero additional procurement or setup work — it is reachable via the same access key, just a new endpoint to query. This lowers the practical adoption barrier for existing Compliance API customers relative to the account-team-gated enablement process for first-time adopters.

## Concrete Artifacts

### Session Record Data Model (new in this post)

```
Claude Compliance API — Cowork / Claude Code Session Record
(Anthropic, 2026-08-11)

One record per session, server-hosted, consolidated transcript:

Session content:
  - Prompts and responses (transcript text)
  - Tool calls content (web and MCP)
  - Skills and artifacts content (transcript text)

Session metadata:
  - Verified user ID and email address
  - Organization ID
  - Session ID and per-message IDs
  - Timestamps
```

### Beta Coverage Matrix (from post)

```
Claude Compliance API — Cowork / Claude Code Beta Scope (Aug 2026)

COVERED (beta, Claude Enterprise customers):
  - Claude Cowork: desktop app, web, mobile
  - Claude Code: CLI, desktop app

NOT COVERED (explicitly excluded from this beta):
  - Claude Code on the web
  - Claude Code accessed through the Claude Platform
  - Sessions run on Amazon Bedrock
  - Sessions run on Google Cloud's Vertex AI
  - Sessions run on Microsoft Foundry
```

### Getting Started (from post)

```
1. Existing Compliance API customers: query the new session endpoints
   directly using your existing Compliance Access Key — no separate
   integration required.
2. Not yet enabled: review the Compliance API documentation to enable it
   (same enablement path as the base Compliance API).
3. No changes required to existing Compliance API pulls — new endpoints
   are additive.
```

## Cross-References

- **Extends**: `blog-anthropic-compliance-api.md` (original March 2026 Platform Compliance API note — admin/resource activity events, explicit inference exclusion) and `blog-anthropic-compliance-api-security-partners.md` (May 2026 — conversation content from Claude Enterprise accessible to 28 security partners). This post extends the "conversation/session content is accessible" pattern established for Claude Enterprise chats in May 2026 to two further surfaces: Claude Cowork and Claude Code (CLI/desktop). The consolidated single-session-record transcript model (Claim 4) is a new data-shape detail not present in either prior note.

- **Corroborates**: `blog-anthropic-cowork-enterprise.md` Claim 3 (Cowork OTel events are SIEM-compatible and correlatable with Compliance API records via shared user identifier). This post's Claim 7 (Compliance API "can work alongside" existing OTel exports "with no infrastructure required") confirms the two logging mechanisms are designed as complementary, non-competing layers — OTel for agent tool/connector action events, Compliance API session endpoints for full session transcripts.

- **Corroborates**: `blog-anthropic-compliance-api-security-partners.md` (eDiscovery named as one of 28 partners' eight integration categories, backed by Relativity/Smarsh). This post's Claim 3 explicitly names "eDiscovery" as a driving use case for closing the Cowork/Claude Code coverage gap, confirming the same regulated-industry discovery use case now extends to agentic coding and cowork sessions, not just chat.

- **Corroborates**: `blog-anthropic-inference-hooks.md` (August 5, 2026 — Inference hooks, a beta Claude Enterprise feature providing synchronous, pre-inference block/allow enforcement across chat, Claude Code, and Claude Cowork). Published six days apart, the two posts form a "prevent vs. detect" pair for the same August 2026 surface set (chat + Claude Code + Cowork): Inference hooks blocks or allows content *before* it reaches the model in real time; this Compliance API extension provides an *after-the-fact* consolidated session transcript for audit and eDiscovery. Neither post references the other, but the Smith should present them together as the two halves of Claude Enterprise's August 2026 governance posture for these surfaces.

- **Contradicts**: `blog-anthropic-compliance-api.md` Claim 4 ("The API does not log inference activities, such as user interactions with the model or model activities") — same underlying tension already identified in **contradiction issue #858** (filed 2026-05-22 against `blog-anthropic-compliance-api-security-partners.md`). Issue #858 received a full Assayer assessment proposing verdict `superseded` (scoped by the Claude Enterprise vs. Claude Platform product-line distinction as the mediating variable), but the issue was closed without a corresponding entry ever being appended to `CONTRADICTIONS.md` — checked directly; no C-NNN entry for this topic exists as of this extraction. This post adds further evidence relevant to that still-open question rather than raising a new, independent contradiction: (1) it confirms "session content" (prompts and responses, i.e., conversation content) is now captured for two more Enterprise-adjacent surfaces (Cowork, Claude Code CLI/desktop), extending the pattern beyond Claude Enterprise chats; and (2) it independently corroborates the Platform/non-Platform mediating variable by explicitly excluding "Claude Code accessed through the Claude Platform" from this coverage, while including Claude Code's Enterprise-associated CLI/desktop surface. No new contradiction issue was filed per MINER.md §4a ("the contradiction is already filed") — this note instead surfaces the additional evidence so whoever revisits #858 (or files a fresh, better-scoped issue) has the full picture: the inference-logging gap appears to persist specifically for Claude Platform (API) deployments while closing for essentially all Claude Enterprise-adjacent surfaces (chats, Cowork, Claude Code CLI/desktop).

- **Novel**:
  - **Consolidated single-session-record transcript model**: No prior corpus source describes a compliance data model that bundles prompts, responses, and tool activity into one server-hosted record per session, as opposed to discrete timestamped events.
  - **Explicit multi-surface exclusion list naming a specific Claude Code deployment path**: "Claude Code accessed through the Claude Platform" as a named, explicitly-excluded surface is the first corpus evidence that Claude Code has an Enterprise-associated path (covered) and a Platform/API-associated path (not covered) for compliance purposes.
  - **Explicit Compliance-API/OTel coexistence statement**: No prior corpus source states outright that the two logging mechanisms are designed to run side-by-side with zero customer-side infrastructure changes; this was previously an inference from two separate posts (the Cowork OTel note and the original Compliance API note), now confirmed directly.

## Guide Impact

- **Chapter on Enterprise Deployment / Governance (planned)**: Update the "what the platform provides vs. what you must build" compliance architecture section (already flagged for updates by `blog-anthropic-compliance-api-security-partners.md`) to add: as of August 2026, Compliance API session endpoints (beta, Claude Enterprise customers) provide a consolidated prompt/response/tool-activity transcript for Claude Cowork (desktop/web/mobile) and Claude Code (CLI/desktop) sessions, in addition to the existing Claude Enterprise chat coverage. Explicitly excluded: Claude Code on the web, Claude Code via Claude Platform, and sessions on Bedrock/Vertex AI/Microsoft Foundry.

- **Chapter on Enterprise Deployment / Governance (planned)**: When this note's guide-impact recommendation and `blog-anthropic-compliance-api-security-partners.md`'s recommendation are synthesized, flag contradiction issue #858 explicitly to a human resolver — it has a full Assayer assessment on record (proposed verdict `superseded`, scoped by Enterprise vs. Platform) but was never appended to CONTRADICTIONS.md. This new source's evidence (Claims 1, 5, 6) should be added to whatever resolution is eventually recorded, since it extends the same Enterprise/Platform distinction to two more surfaces.

- **Chapter on Enterprise Deployment / Governance (planned)**: Present Inference hooks (`blog-anthropic-inference-hooks.md`) and this Compliance API extension together as a matched "prevent vs. detect" governance pair for Claude Enterprise's chat/Claude Code/Cowork surfaces, published within the same week of each other (Aug 5 and Aug 11, 2026).

## Extraction Notes

- **Verified via raw HTML fetch, not WebFetch summarization alone**: An initial WebFetch pass returned a paraphrased summary; per MINER.md §2a, the raw page HTML was additionally fetched directly via `curl` with a browser user agent, stripped of markup, and every `Quote` field in this note was cross-checked character-for-character against that raw-text extraction (saved during the extraction session). Section headings ("How it works," "Getting started"), the category/date/reading-time metadata (Category "Enterprise AI"/"Product announcements," Date "August 11, 2026," Reading time "5 min"), and all body paragraphs were confirmed against the visible page structure.
- **Source is short** (~350 words), consistent with the two prior Compliance API announcements already in the corpus. All substantive claims were extracted; there is no deeper content within the post itself.
- **No sub-pages followed**: The post links to a generic "Compliance API documentation" page (no direct URL text given, only an inline hyperlink) and to unrelated cross-promotional posts in a "Related posts" carousel (the Claude Cowork product guide, an Anthropic finance-team post, an Anthropic BD-team post, and the Inference hooks post). The Inference hooks post is already in the corpus (`blog-anthropic-inference-hooks.md`) and was used for cross-referencing rather than re-extracted; the others are marketing/cross-promotional with no additional compliance-relevant claims expected.
- **Contradiction handling**: Checked open `contradiction`-labeled issues and `CONTRADICTIONS.md` before extraction, per MINER.md §4a. Found issue #858 (closed, but carrying a full unactioned Assayer assessment and no corresponding CONTRADICTIONS.md entry) covering the same underlying Enterprise-vs-Platform inference-logging tension. Did not file a new contradiction issue since this is evidence for an already-filed, still-unresolved contradiction rather than a new one; documented the additional evidence in Cross-References → Contradicts above instead.
- **Confidence calibration**: `settled` overall — every claim is a first-party Anthropic description of a shipping (beta) feature with concrete, enumerable scope (data types, excluded surfaces, enablement mechanics). There are no anecdotal case-study claims in this post to grade separately, unlike the Cowork enterprise/deploy-guide notes.
