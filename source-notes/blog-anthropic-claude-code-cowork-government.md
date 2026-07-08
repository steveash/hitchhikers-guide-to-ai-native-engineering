---
source_url: https://claude.com/blog/bringing-claude-code-and-claude-cowork-to-government
source_type: blog-post
title: "Bringing Claude Code and Claude Cowork to government"
author: Anthropic
date_published: 2026-07-07
date_extracted: 2026-07-08
last_checked: 2026-07-08
status: current
confidence_overall: settled
issue: "#1652"
---

# Bringing Claude Code and Claude Cowork to government

> Official Anthropic announcement that Claude Code and Claude Cowork are in public
> beta on "Claude for Government Desktop," delivered through a FedRAMP High
> authorized environment with a split architecture (conversation history stays on
> the agency-managed device; inference runs in the FedRAMP High environment) — the
> first corpus source documenting a hash-chained administrative audit log,
> two-person approval for sensitive Anthropic-side operations, and an
> appropriations-shaped billing model (fixed-increment prepaid usage, hard
> not-to-exceed caps, burndown alerts) for a government AI deployment.

## Source Context

- **Type**: blog-post (official Anthropic product announcement, claude.com,
  published July 7, 2026, category "Product announcements," 5-minute read, no
  individual byline).
- **Author credibility**: First-party Anthropic communication describing a
  shipping (public beta) product surface. Feature claims — FedRAMP High
  authorization, the local/remote data-split architecture, billing mechanics,
  audit-log and approval controls, SCIM-based seat administration, and
  compliance-artifact availability — are settled first-party descriptions of a
  real deployment. No named agencies, customer testimonials, or case studies are
  included in this post (a notable contrast with the Cowork enterprise/deployment
  posts already in the corpus, which lead with named customers).
- **Scope**: Covers the beta launch of Claude Code and Claude Cowork inside
  Claude for Government Desktop, the FedRAMP High authorization boundary, the
  local-storage/remote-inference data split, appropriations-shaped billing,
  department/sub-agency administration via SCIM, the hash-chained audit log and
  two-person approval controls, and the compliance-artifact publication process
  (Secure Configuration Guide, FedRAMP change notification, penetration-test
  summary). Does NOT cover: pricing figures, the technical implementation of the
  hash chain, which specific agencies have adopted it, a timeline for GA, how this
  FedRAMP High-authorized path relates technically to the GCC High/DoD path
  documented for Claude Desktop via Microsoft Foundry (see Cross-References), or
  any independent security assessment of the claims (the pentest summary and
  FedRAMP change notification are gated under NDA via Anthropic's trust center
  and were not accessible for this extraction).

## Extracted Claims

### Claim 1: Claude Code and Claude Cowork are now available in public beta on Claude for Government Desktop, built on the same application commercial customers use, delivered through a FedRAMP High authorized environment
- **Evidence**: Opening statement of the post, stated without qualification.
- **Confidence**: settled (first-party launch announcement)
- **Quote**: "Claude Code and Claude Cowork are now available in public beta in Claude for Government Desktop, built on the same application our commercial customers use and delivered through a FedRAMP High authorized environment."
- **Our assessment**: The "same application" framing is the key claim — Anthropic is not describing a government-specific fork of the product with reduced capability, but the same Claude Code/Cowork commercial customers use, wrapped in a FedRAMP High-authorized delivery boundary. This matters for practitioners evaluating whether government deployment lags commercial feature parity: the post's later claim ("same cadence as our commercial users," Claim 2) reinforces that this is a delivery/authorization difference, not a capability difference.

### Claim 2: Conversation history is stored locally on the agency-managed device while inference runs inside the FedRAMP High authorized environment — a split local/remote architecture
- **Evidence**: Stated directly under the "What's new" section.
- **Confidence**: settled (explicit first-party architecture description)
- **Quote**: "Agencies get new capabilities on the same cadence as our commercial users. Conversation history is stored locally on the agency-managed device. Inference runs inside a FedRAMP High authorized environment."
- **Our assessment**: This is the most architecturally specific claim in the post and is new to the corpus. It describes a concrete data-residency boundary: the record of what a user asked and discussed lives on agency-controlled hardware, while only the inference computation itself crosses into Anthropic's FedRAMP High environment. For a regulated deployment, this is a materially different model than a fully cloud-hosted conversation history (as in standard Claude Enterprise) — it reduces the surface of agency data that ever leaves agency control at rest, though the query/response content necessarily transits to the inference environment. The post does not specify whether this local-storage model is government-specific or shared with commercial Claude Desktop.

### Claim 3: Claude Cowork enables agency staff to delegate memo creation, RFP reviews, casework, and deck creation by working directly with files on the desktop
- **Evidence**: Direct capability description in the opening section.
- **Confidence**: settled (first-party feature description)
- **Quote**: "Claude Cowork works directly with files on the desktop, allowing agency staff to delegate memo creation, RFP reviews, casework, and decks to Claude."
- **Our assessment**: These four named use cases (memos, RFP reviews, casework, decks) are government-specific analogs to the non-engineering "surrounding work" use cases already documented for commercial Cowork deployments (`blog-anthropic-cowork-enterprise.md` Claim 6; `blog-anthropic-cowork-deploy-guide.md` function-specific use case table). "Casework" in particular is a public-sector-specific term (constituent/beneficiary case processing) not present in the commercial Cowork use-case vocabulary already in the corpus.

### Claim 4: Program offices can bill Claude spend against appropriated funds using standard seats or custom seat tiers with independent spend and model limits, purchased in fixed increments with a hard not-to-exceed cap
- **Evidence**: Direct description under "Billing that fits appropriations."
- **Confidence**: settled (first-party billing-mechanism description)
- **Quote**: "Program offices can tie AI spend to appropriated funds with standard seats or they can define their own seat tiers with spend and model limits, and usage is purchased in fixed increments with a hard not-to-exceed cap."
- **Our assessment**: "Appropriated funds" is a specific government budgeting concept (funds allocated by legislative appropriation, typically use-it-or-lose-it within a fiscal cycle) — a hard not-to-exceed cap purchased in fixed increments is the billing mechanism that lets a program office map AI spend onto that appropriations model without risk of open-ended overage. This is a novel billing pattern for the corpus: commercial Cowork billing documented elsewhere (`blog-anthropic-cowork-enterprise.md` Claim 5) uses adjustable per-team budgets, not fixed-increment prepaid purchases with hard caps.

### Claim 5: Administrators can track usage per user and per model in the admin console, with automatic burndown alerts before the prepaid balance runs low
- **Evidence**: Direct description, same section as Claim 4.
- **Confidence**: settled (first-party feature description)
- **Quote**: "Administrators can track usage per user and per model in the admin console, and automatic burndown alerts warn them before the balance runs low."
- **Our assessment**: The burndown-alert mechanism is the operational complement to the hard not-to-exceed cap in Claim 4 — without it, a hard cap risks agency staff losing access mid-task when a prepaid balance is exhausted unexpectedly. This is a specific, actionable governance detail: budget owners get a warning window rather than a silent cutoff.

### Claim 6: Department-level administrators can allocate seats and prepaid usage to sub-agencies while each sub-agency manages its own users, using SCIM group mappings to set rate limits, dollar caps, and allowed models per seat tier
- **Evidence**: Direct description under "Administration that matches how departments are organized."
- **Confidence**: settled (first-party feature description)
- **Quote**: "Department-level administrators can allocate seats and prepaid usage to sub-agencies while allowing each to manage its own users. Administrators can use SCIM group mappings to set rate limits, dollar caps, and allowed models for specific seat tiers."
- **Our assessment**: This extends the SCIM-based governance pattern already documented in `blog-anthropic-cowork-enterprise.md` Claim 1 (SCIM groups → custom capability roles) to a new dimension: SCIM groups here drive rate limits, dollar caps, and model allowlists per seat tier, in a hierarchical department-to-sub-agency delegation structure. The prior corpus claim covered capability access control; this claim covers financial and rate governance delegated down an organizational hierarchy — a distinct but complementary use of the same SCIM-to-Claude-governance mechanism. This is the first corpus evidence that SCIM group mappings control per-tier dollar caps specifically (as opposed to role/capability access).

### Claim 7: Layered configuration sets defaults for sub-agencies, including what Claude can connect to, which features are available, and instructions that guide how Claude interacts with users
- **Evidence**: Direct description, same section as Claim 6.
- **Confidence**: settled (first-party feature description)
- **Quote**: "Additionally, layered configuration sets defaults for sub-agencies including what Claude can connect to, which features are available, and instructions that guide how Claude interacts with users."
- **Our assessment**: "Instructions that guide how Claude interacts with users" set at the sub-agency default layer implies a system-prompt-like configuration inherited hierarchically — sub-agencies get a baseline behavioral configuration set above them (by the department) that they can presumably further customize. This is consistent with the "layered configuration" pattern found in `blog-anthropic-cowork-deploy-guide.md` (admin-provisioned Level 4 department plugins), applied here specifically to the department → sub-agency government hierarchy rather than a corporate department hierarchy.

### Claim 8: Every administrative action is recorded in a hash-chained, tamper-evident audit log that organization administrators can review directly in the product
- **Evidence**: Direct description under "Oversight by design."
- **Confidence**: settled (explicit first-party feature description)
- **Quote**: "Every administrative action is recorded in a hash-chained audit log that organization administrators can review directly in the product."
- **Our assessment**: This is the single most consequential and novel governance claim in the post. A hash chain provides cryptographic tamper-evidence — each log entry incorporates a hash of the prior entry, so retroactively altering or deleting a past entry breaks the chain and is detectable. This is a materially stronger integrity guarantee than the general Compliance API described in `blog-anthropic-compliance-api.md`, which documents *what* is logged (admin/resource activities, explicitly excluding inference) but makes no claim about tamper-evidence of the log itself. Whether this hash-chained log is a government-specific hardening of the same underlying Compliance API log stream, or a distinct product-level (Desktop-app) audit mechanism, is not stated in either post — this relationship is unclear from the corpus and worth flagging to the Smith as an open question rather than treating the two as either identical or contradictory.

### Claim 9: Sensitive operations on Anthropic's own side require two-person approval
- **Evidence**: Direct statement, same section as Claim 8.
- **Confidence**: settled (first-party internal-control description)
- **Quote**: "Sensitive operations on Anthropic's side require two-person approval."
- **Our assessment**: This is a claim about Anthropic's *own* internal operational controls (not a customer-configurable feature) — a two-person integrity rule for sensitive operations affecting the government environment. This is the first corpus mention of a named vendor-side two-person-approval control. It is not independently verifiable from this post alone (no description of what counts as a "sensitive operation" or how the rule is enforced/audited), so its practical scope should be treated as directionally informative rather than a fully specified control.

### Claim 10: Usage exports are metering data only, letting agencies answer ATO and Inspector General (IG) requests without moving sensitive material
- **Evidence**: Direct statement, same section as Claims 8-9.
- **Confidence**: settled (first-party feature description)
- **Quote**: "Usage exports are metering data only so agencies can answer ATO and IG requests without moving sensitive material."
- **Our assessment**: This directly addresses a specific government compliance friction: satisfying an Authority to Operate (ATO) review or an Inspector General inquiry often requires demonstrating usage patterns without exposing the underlying content those usage records describe. By scoping exports to metering data (who/what/when, not content), Anthropic lets agencies produce audit evidence without a separate data-minimization or redaction step. This is conceptually adjacent to the Compliance API's exclusion of inference-content logging (`blog-anthropic-compliance-api.md` Claim 4) but framed here as a deliberate export-scoping decision aimed specifically at the ATO/IG use case, rather than a general platform logging boundary.

### Claim 11: Anthropic is publishing a public-facing FedRAMP Secure Configuration Guide, a formal FedRAMP change notification, and a penetration-test summary for the new desktop client, with the change notification and pentest summary available under NDA through Anthropic's trust center
- **Evidence**: Direct description under "Security and oversight."
- **Confidence**: settled (first-party statement of documentation availability; the actual documents were not independently accessible for this extraction — the pentest summary and change notification are gated under NDA)
- **Quote**: "For security teams evaluating the desktop deployment, we're publishing our FedRAMP Secure Configuration Guide as a public-facing document that customers can use to configure their Claude for Government product in a secure manner. In addition, FedRAMP requires us to provide our formal change notification, which contains details associated with this change. Lastly, a penetration-test summary is available for the new desktop client, and subsequent follow up penetration-tests summaries will be provided once available. The change notification and pentest summary are available under NDA through Anthropic's trust center."
- **Our assessment**: This is a three-tier compliance-documentation model: (1) a fully public configuration guide, (2) a formal change notification required by the FedRAMP process itself (gated under NDA), and (3) a penetration-test summary with a stated commitment to follow-up summaries (also gated under NDA). The tiered public/NDA split means the guide's own content (the Secure Configuration Guide) is independently checkable by any reader, but the change notification and pentest summary require an existing NDA relationship with Anthropic — this note cannot independently verify the content of those two gated documents.

### Claim 12: Claude for Government is available in beta starting the publication date; Anthropic remains the contracted and billing party, so agencies do not need a separate cloud-provider relationship to get started
- **Evidence**: Direct statement under "Getting started."
- **Confidence**: settled (first-party acquisition-model description)
- **Quote**: "Claude for Government is available in beta starting today. Anthropic remains the contracted and billing party—agencies don't need a separate cloud-provider relationship to get started."
- **Our assessment**: This is a distinct acquisition/deployment path from the one documented in `blog-anthropic-claude-desktop-cloud-platforms.md`, where Claude Desktop (including beta GCC High/DoD endpoint support) is delivered through a customer's existing AWS, Google Cloud, or Microsoft Foundry relationship — i.e., the hyperscaler is the contracted/billing party and Claude rides on top of an existing cloud contract. This government post describes the opposite model: Anthropic itself is the direct contracted and billing party for Claude for Government Desktop, with no hyperscaler intermediary required. The guide should treat these as two distinct, coexisting government/regulated deployment paths rather than one superseding the other — see Cross-References.

## Concrete Artifacts

### Government Deployment Feature Summary (verbatim section-by-section, from post)

```
Bringing Claude Code and Claude Cowork to government
(Anthropic, 2026-07-07, https://claude.com/blog/bringing-claude-code-and-claude-cowork-to-government)

What's new:
  - Claude Code + Claude Cowork in public beta on Claude for Government Desktop
  - "Agencies get new capabilities on the same cadence as our commercial users."
  - Conversation history: stored locally on agency-managed device
  - Inference: runs inside a FedRAMP High authorized environment

Billing that fits appropriations:
  - Spend tied to appropriated funds via standard seats OR custom seat tiers
    (own spend + model limits)
  - Usage purchased in fixed increments, hard not-to-exceed cap
  - Per-user / per-model usage tracking in admin console
  - Automatic burndown alerts before balance runs low

Administration that matches how departments are organized:
  - Department-level admins allocate seats + prepaid usage to sub-agencies
  - Sub-agencies manage their own users
  - SCIM group mappings set: rate limits, dollar caps, allowed models per seat tier
  - Layered configuration sets sub-agency defaults: connections, features,
    interaction instructions

Oversight by design:
  - Every admin action → hash-chained, tamper-evident audit log (reviewable in-product)
  - Sensitive operations on Anthropic's side → two-person approval required
  - Usage exports: metering data only (supports ATO / IG requests without
    moving sensitive material)

Security and oversight (compliance artifacts):
  - FedRAMP Secure Configuration Guide: public-facing document
  - Formal FedRAMP change notification: NDA via Anthropic trust center
  - Penetration-test summary (new desktop client) + future follow-ups: NDA
    via Anthropic trust center

Getting started:
  - Beta available starting 2026-07-07
  - Anthropic is the contracted + billing party (no separate cloud-provider
    relationship required)
  - Access request: claude.com/solutions/government
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-cowork-enterprise.md` Claim 1 (SCIM-based RBAC for AI
    capability access control) — this post's Claim 6 (SCIM group mappings set
    rate limits, dollar caps, allowed models per seat tier) confirms SCIM
    groups are a general-purpose governance lever for Claude deployments, now
    shown driving financial/rate controls in addition to the capability-access
    controls the enterprise post documented.
  - `blog-anthropic-cowork-deploy-guide.md` (layered/admin-provisioned
    department plugin configuration, Level 4 of the maturity model) — this
    post's Claim 7 (layered configuration setting sub-agency defaults for
    connections, features, and interaction instructions) is the same
    hierarchical-default pattern applied to a government department →
    sub-agency structure instead of a corporate department structure.

- **Contradicts**: None filed. No existing source note makes a claim that
  conflicts with this post's specific government deployment mechanics.

- **Extends**:
  - `blog-anthropic-claude-desktop-cloud-platforms.md` Claim 7 (beta support
    for GCC High/DoD endpoints via a Microsoft 365 connector, within Claude
    Desktop deployed through Microsoft Foundry) — this post documents a
    second, architecturally distinct government/regulated deployment path:
    "Claude for Government Desktop" delivered directly by Anthropic through a
    FedRAMP High authorized environment, versus the GCC High/DoD path that
    rides on a customer's existing Azure/Foundry relationship (hyperscaler as
    contracted party). Claim 12 of this note makes the "Anthropic remains the
    contracted and billing party" distinction explicit. The guide should
    present these as two coexisting government-deployment routes with
    different authorization boundaries (FedRAMP High direct vs.
    hyperscaler-hosted GCC High/DoD, still beta per the Desktop note), not as
    one superseding the other — the two posts do not state how (or whether)
    they interoperate.
  - `blog-anthropic-compliance-api.md` (Compliance API activity-log scope:
    admin/resource events logged, inference explicitly excluded) — this
    post's hash-chained audit log (Claim 8) and metering-only usage exports
    (Claim 10) describe a government-hardened audit posture that is
    consistent with, but more specific than, the general Compliance API
    description. The relationship between the two logging mechanisms (same
    underlying system with an added integrity guarantee, vs. a separate
    Desktop-app-level log) is not stated in either source and should be
    flagged as an open question rather than assumed.
  - `blog-anthropic-compliance-api-security-partners.md` — that note documents
    28 named security/compliance partner integrations built on the Compliance
    API, including "AI security posture management" and "eDiscovery" as named
    categories. This government post's ATO/IG-focused metering export (Claim
    10) is a concrete instance of the eDiscovery/regulatory-response use case
    that note names abstractly.

- **Novel**:
  - **Hash-chained tamper-evident administrative audit log** (Claim 8): No
    prior corpus source documents a cryptographically tamper-evident log
    structure for any Claude product; prior audit-logging claims
    (`blog-anthropic-compliance-api.md`) describe log *scope*, not log
    *integrity guarantees*.
  - **Vendor-side two-person approval control** (Claim 9): First corpus
    mention of an internal Anthropic operational control (as opposed to a
    customer-configurable governance feature) for sensitive operations.
  - **Appropriations-shaped billing (fixed-increment prepaid, hard cap,
    burndown alerts)** (Claims 4-5): No prior corpus source documents a
    billing model built specifically around government appropriated-funds
    budgeting mechanics.
  - **Local conversation storage + remote FedRAMP High inference split
    architecture** (Claim 2): Not previously documented for any Claude
    product in the corpus.
  - **ATO/IG-scoped metering-only usage export** (Claim 10): A specific,
    named compliance-request use case (Authority to Operate review, Inspector
    General inquiry) not previously named in the corpus's compliance-logging
    coverage.
  - **Sub-agency SCIM-driven dollar caps and model allowlists per seat tier**
    (Claim 6): Extends SCIM-based governance into financial/rate control
    territory not previously documented.

## Guide Impact

- **Chapter on Enterprise Deployment / Governance (planned)**: Add this post as
  the government/regulated-industry deployment case study. It should sit
  alongside `blog-anthropic-claude-desktop-cloud-platforms.md` as the *second*
  documented government-deployment path (direct FedRAMP High vs.
  hyperscaler-hosted GCC High/DoD) — the guide should explicitly name both
  paths and note that neither source states how they relate to or supersede
  each other.

- **Chapter on Enterprise Deployment / Governance (planned)**: Add the
  hash-chained audit log (Claim 8) and two-person approval (Claim 9) as the
  strongest integrity-guarantee audit controls documented in the corpus so
  far, distinct from (and stronger a claim than) the Compliance API's
  scope-only logging description. Flag the open question of whether this is
  the same underlying log with an added guarantee or a separate system.

- **Chapter on Enterprise Deployment / Governance (planned)**: Add the
  appropriations-shaped billing model (Claims 4-5: fixed-increment prepaid
  purchase, hard not-to-exceed cap, burndown alerts) as a distinct billing
  pattern from the adjustable per-team budgets documented for commercial
  Cowork (`blog-anthropic-cowork-enterprise.md` Claim 5) — useful for any
  guide section distinguishing commercial vs. government/regulated
  procurement-constrained billing needs.

- **Chapter on Enterprise Deployment / Governance (planned)**: Add the
  ATO/IG-scoped metering-only export (Claim 10) as a concrete example of how
  the general "audit scope excludes inference content" pattern
  (`blog-anthropic-compliance-api.md`) is packaged for a specific named
  compliance workflow (Authority to Operate review, Inspector General
  inquiry).

## Extraction Notes

- **Source is short** (~450 words per the page's own "5 min" reading-time
  estimate). All substantive claims were extracted; there is no deeper content
  within the post itself.
- **Verified via raw HTML fetch, not WebFetch summarization alone**: An
  initial WebFetch pass returned quoted strings; to satisfy MINER.md §2a, the
  raw page HTML was additionally fetched directly via `curl` with a browser
  user agent, stripped of markup with a Python script, and every `Quote`
  field in this note was cross-checked character-for-character against that
  raw-text extraction (confirmed at `/tmp/gov_blog.txt` in the extraction
  session — section headings "What's new," "Billing that fits
  appropriations.," "Administration that matches how departments are
  organized.," "Oversight by design.," "Security and oversight," and "Getting
  started" all match the visible page structure, along with the byline-free
  metadata: Category "Product announcements," Date "July 7, 2026," Reading
  time "5 min").
- **No customer testimonials or named agencies**: Unlike most other
  Anthropic Cowork/enterprise announcements in the corpus
  (`blog-anthropic-cowork-enterprise.md`, `blog-anthropic-cowork-deploy-guide.md`),
  this post contains no named customer, case study, or practitioner quote —
  it is a pure product/policy announcement. This is reflected in the
  `settled` confidence rating: every claim is a first-party feature or policy
  description, with no anecdotal case-study material to grade separately.
- **Gated documents not accessible**: The FedRAMP formal change notification
  and the penetration-test summary (Claim 11) are explicitly stated to require
  an NDA through Anthropic's trust center; these were not independently
  accessed or verified beyond the post's own description of their existence
  and availability. The FedRAMP Secure Configuration Guide is described as
  public-facing, but no direct URL was given in the post body (only the
  general `claude.com/solutions/government` access-request link and a trust
  center pentest-artifact link); it was not located and read as part of this
  extraction. This should not block the source note — the post's own claims
  about what these documents are and how they're gated are the extractable
  content — but the Smith should not treat the documents' *contents* as
  verified by this note.
- **Sub-pages**: The blog post links to `/product/claude-code`,
  `/product/cowork`, `/solutions/government`, a related post ("Claude Cowork
  is coming to mobile and web"), and a trust-center pentest-artifact link.
  None were followed — the first three are generic product pages with no
  additional government-specific claims expected, the mobile/web Cowork post
  is a different product surface out of scope for this extraction, and the
  trust-center link requires NDA access as noted above.
- **No contradictions found**: Reviewed all existing Cowork, compliance, and
  government-adjacent source notes (`blog-anthropic-cowork-enterprise.md`,
  `blog-anthropic-cowork-deploy-guide.md`, `blog-anthropic-compliance-api.md`,
  `blog-anthropic-compliance-api-security-partners.md`,
  `blog-anthropic-claude-desktop-cloud-platforms.md`,
  `blog-thoughtworks-lewis-gov-structural-modernization.md`,
  `blog-jetbrains-agentic-ai-governance.md`). No claim in this post materially
  opposes an existing note's claim at the level required by MINER.md §4a — the
  relationship to the GCC High/DoD Desktop path and to the general Compliance
  API are extensions/open questions, not contradictions, and are flagged as
  such above rather than filed as a contradiction issue.
