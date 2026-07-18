---
source_url: https://github.blog/changelog/2026-07-17-repository-level-github-copilot-usage-metrics-generally-available
source_type: docs
title: "Repository-level GitHub Copilot usage metrics generally available"
author: GitHub (official changelog)
date_published: 2026-07-17
date_extracted: 2026-07-18
last_checked: 2026-07-18
status: current
confidence_overall: settled
issue: "#1990"
---

# Repository-Level Copilot Usage Metrics in the Usage Metrics API (GitHub Changelog)

> GitHub's July 17, 2026 changelog announces general availability of two new
> REST endpoints (`repos-1-day`, enterprise and org scope) that return a
> daily, signed-URL NDJSON report of per-repository pull request activity for
> Copilot coding agent (CCA) and Copilot code review (CCR) — a new
> repository-granularity tier that sits alongside, not above or below, the
> existing org/enterprise-aggregate, team-level, and per-user tiers already
> documented in this corpus, and whose own "why this matters" framing
> inaccurately claims no such intermediate tier previously existed.

## Source Context

- **Type**: docs (GitHub official product changelog, ~130 words of body text,
  "1 minute read," July 17, 2026; cross-checked against the linked REST API
  reference page at `docs.github.com/rest/copilot/copilot-usage-metrics`,
  which was fetched directly to confirm the endpoint response schema, access
  scopes, and fine-grained permission names not stated in the changelog
  itself)
- **Author credibility**: GitHub engineering team announcing a production API
  change, corroborated by GitHub's own REST API reference documentation.
  Authoritative for the fact that these endpoints exist, their response
  shape, and their access requirements. Not authoritative for the historical
  framing claim in the "Why this matters" section (see Claim 6) or for any
  outcome/effectiveness data about repository-level reporting driving actual
  "AI-readiness" decisions — no such evidence is cited.
- **Scope**: Two new REST endpoints (`repos-1-day`) returning per-repository,
  single-day Copilot PR activity reports at the enterprise and organization
  level; the signed-URL/NDJSON delivery model; the CCA/CCR activity
  breakdown; the "only repositories with activity" inclusion rule; and the
  access tiers/scopes for both endpoints (confirmed via the linked docs
  page). Does NOT cover: the exact JSON field names inside the downloaded
  NDJSON report rows (the REST reference page documents only the wrapper
  response — `download_links` and a single `report_day` field — not
  the per-repository row schema); whether a `repos-28-day` rolling-window
  variant exists (confirmed absent from the docs page as of this
  extraction — see Claim 5); how repository-level totals relate
  arithmetically to the team-level or org-level aggregates (no join or
  non-additivity guidance is given, unlike the team-level report); or any
  guidance on what constitutes a "high" or "low" repository-level PR
  activity count.

## Extracted Claims

### Claim 1: Two new REST endpoints return a daily, per-repository breakdown of Copilot pull request activity, at both the enterprise and organization level

- **Evidence**: Official GitHub changelog body text, confirmed verbatim via
  direct HTML fetch of the changelog page (WebFetch's model-processed
  summary of the same passage rendered a corrupted, truncated version of the
  "why this matters" quote — see Extraction Notes item 2 — so the changelog
  was re-fetched via raw HTML to guarantee verbatim accuracy per MINER.md
  §2a).
- **Confidence**: settled (product fact — the endpoints exist, confirmed
  independently against the REST API reference page)
- **Quote**: "The Copilot usage metrics REST API now reports repository-level
  activity. Two new endpoints return a daily, per-repository breakdown of
  pull request activity for Copilot coding agent and Copilot code review.
  They do this for both enterprise and organization reports."
- **Our assessment**: This follows the exact same per-surface, per-tier
  expansion pattern the corpus has already documented for the Copilot usage
  metrics API: aggregate CCA counts (April 10), aggregate code review counts
  (April 22), team-level attribution (May 14), per-user AI credits (June
  19) — each adds one new dimension without replacing the others. This
  release adds a *repository* dimension, not previously available at any
  granularity in the corpus (existing tiers are enterprise/org aggregate,
  team, and per-user — none are keyed by repository).

### Claim 2: Each endpoint's `GET` request takes a `day=YYYY-MM-DD` query parameter and the exact paths are `/enterprises/{enterprise}/copilot/metrics/reports/repos-1-day` and `/orgs/{org}/copilot/metrics/reports/repos-1-day`

- **Evidence**: Explicit endpoint paths given in the changelog body and
  independently confirmed as live, documented REST endpoints on the linked
  API reference page (titled "Get Copilot enterprise repository report for a
  specific day" and "Get Copilot organization repository report for a
  specific day").
- **Confidence**: settled (definitional — verified against two independent
  GitHub-authored sources: the changelog and the REST reference)
- **Quote**: "Two new endpoints return a per-repository report for a single
  day:
  `GET /enterprises/{enterprise}/copilot/metrics/reports/repos-1-day?day=YYYY-MM-DD`
  `GET /orgs/{org}/copilot/metrics/reports/repos-1-day?day=YYYY-MM-DD`"
- **Our assessment**: The `repos-1-day` naming and the `day=` query parameter
  mirror the naming convention already documented for the team-level
  `user-teams-1-day` report in `docs-github-copilot-team-level-usage-metrics.md`
  (Concrete Artifacts). Both are single-day report endpoints returning
  download links rather than inline data — this is now the established
  delivery pattern for any Copilot metrics report keyed by a dimension other
  than the top-level enterprise/org aggregate (team, and now repository).

### Claim 3: The endpoint response is a wrapper JSON object containing signed NDJSON download links and the report's date range, not inline per-repository data

- **Evidence**: Response schema shown directly on the linked REST API
  reference page for both the enterprise and organization `repos-1-day`
  endpoints (identical schema for both).
- **Confidence**: settled (definitional — response schema copied verbatim
  from the official REST reference page, fetched directly via `curl` rather
  than through WebFetch)
- **Quote**:
  ```
  {
    "download_links": [
      "https://example.com/copilot-usage-report-1.ndjson",
      "https://example.com/copilot-usage-report-2.ndjson"
    ],
    "report_day": "2025-07-01"
  }
  ```
- **Our assessment**: This is the identical signed-URL + NDJSON delivery
  model already documented for the May 14, 2026 team-level `user-teams-1-day`
  report in `docs-github-copilot-team-level-usage-metrics.md` Claim 2
  ("Two new endpoints return signed download URLs to NDJSON reports").
  Teams that already built a pipeline to consume the team-level report (redirect
  to a signed URL, parse NDJSON line-by-line, handle URL expiration) can reuse
  that same pipeline component for the repository-level report — this is not a
  new integration pattern, just a new report type using an established
  delivery mechanism. The wrapper response is even simpler than a date-range
  object: the schema (titled "Copilot Metrics 1 Day Report" on the reference
  page) carries only `download_links` plus a single `report_day` field, whose
  example value is `"2025-07-01"`. The single `report_day` (not a
  start/end pair) reinforces that this is a single-day report per its name
  and the `day=` query parameter — there is no 28-day window field in the
  response, consistent with the absence of a `repos-28-day` endpoint variant
  (see Claim 5).

### Claim 4: Each per-repository report entry covers pull requests created and merged by Copilot coding agent, and pull requests reviewed by Copilot code review with suggestion counts broken down by comment type — but only for repositories that had activity that day

- **Evidence**: Changelog body text plus corroborating detail from the REST
  reference page's endpoint description, which adds the "only repositories
  that had activity" inclusion rule not stated in the changelog itself.
- **Confidence**: settled (definitional — stated in both the changelog and
  the REST reference page)
- **Quote (changelog)**: "Each response returns the following activity:
  Pull requests created and merged by Copilot coding agent.
  Pull requests reviewed by Copilot code review, with suggestion counts
  broken down by comment type."
- **Quote (REST reference page)**: "The report contains repository-level
  pull request activity for the specified day, including the Copilot Coding
  Agent (CCA) and Copilot Code Review (CCR) breakdowns. Only repositories
  that had activity on the specified day are included."
- **Our assessment**: The "only repositories with activity" rule is an
  important sparse-reporting behavior the changelog itself never mentions —
  a team consuming this report should not treat a repository's absence from
  a given day's NDJSON file as "zero activity confirmed"; it could equally
  mean the report generation excluded it because it had no CCA/CCR events at
  all that day, which is functionally the same outcome for a dashboard but
  means the report is not a complete enumeration of all repositories in the
  org/enterprise (unlike the per-user reports, which the corpus's
  `docs-github-copilot-usage-metrics-ai-credits-per-user.md` does not
  describe as having a similar sparse-inclusion rule). Teams building
  repository coverage dashboards should union report dates over a rolling
  window rather than relying on a single day's report to see all active
  repositories. The "suggestion counts broken down by comment type" detail
  is new terminology not further defined in either the changelog or the
  fetched portion of the REST reference page — the exact comment-type
  categories are not documented in either source (see Extraction Notes item
  3).

### Claim 5: Unlike the per-user usage reports, the repository-level report has no documented 28-day rolling-window variant — only the single-day `repos-1-day` endpoint exists

- **Evidence**: Absence of any `repos-28-day` string anywhere on the fetched
  REST API reference page, in contrast to the confirmed presence of both
  `users-1-day` and `users-28-day` report types on the same page (6 matches
  each for `users-1-day`, `users-28-day`, and `repos-1-day`, 0 matches for
  `repos-28-day`).
- **Confidence**: settled (a negative product fact derived directly from the
  official REST reference page content, not from the changelog, which does
  not address windowing at all)
- **Quote**: (no direct quote; see Extraction Notes item 4 for the
  verification method — this is an inference from the absence of a string
  pattern in the source, not a stated claim)
- **Our assessment**: This is an operationally significant gap the changelog
  does not flag. Per-user reports (per
  `docs-github-copilot-usage-metrics-ai-credits-per-user.md` Claim 4) are
  available in both single-day and 28-day rolling windows, giving consumers
  a choice between day-level monitoring and month-level trend analysis
  without client-side aggregation. Repository-level reports offer only the
  single-day window — a team wanting a 28-day repository activity trend
  must download and sum 28 individual daily NDJSON reports itself, with the
  same "only repositories with activity" sparse-inclusion caveat from Claim
  4 applying independently to each day. This is a real client-side
  aggregation burden not present for the per-user report type, and the
  changelog gives no indication whether a `repos-28-day` variant is planned.

### Claim 6: The changelog's "Why this matters" framing states that prior to this release, "Copilot usage metrics stopped at the organization and user level" — a claim that omits the team-level tier this corpus already documents as generally available since May 14, 2026

- **Evidence**: Explicit "Why this matters" sentence in the changelog,
  compared against `docs-github-copilot-team-level-usage-metrics.md`, whose
  frontmatter and Claim 1 document the `user-teams-1-day` report reaching
  general availability on May 14, 2026 — over two months before this July 17
  changelog.
- **Confidence**: anecdotal (this is vendor "why this matters" framing prose,
  not a technical field definition, and it conflicts with GitHub's own prior
  changelog — see Cross-References → Contradicts)
- **Quote**: "Until now, Copilot usage metrics stopped at the organization
  and user level. Repository-level reporting lets you see exactly where
  Copilot coding agent and Copilot code review are driving pull request
  activity across your codebase. This is the foundation for repository
  insights and AI-readiness reporting, so you can target enablement at the
  repositories that stand to benefit most."
- **Our assessment**: Taken literally, "stopped at the organization and user
  level" is inaccurate — it ignores the `user-teams-1-day` team-level tier
  GitHub's own May 14, 2026 changelog announced as generally available. This
  is flagged as a contradiction (issue #2018, filed per MINER.md §4a) rather
  than silently corrected here, because a resolver may reasonably conclude
  the July 17 author was contrasting "aggregate" against "per-repository"
  data shapes and simply didn't count the JOIN-based team report as a
  distinct "level" — a looser use of "level" than a strict reading implies,
  rather than an assertion that the team tier doesn't exist. Regardless of
  intent, if the guide cites this sentence uncritically to describe the
  history of Copilot metrics granularity, it will omit the team tier from
  the documented hierarchy. The second half of the claim — positioning
  repository-level data as "the foundation for repository insights and
  AI-readiness reporting" so admins can "target enablement at the
  repositories that stand to benefit most" — is unverified vendor framing:
  no evidence is given that repository-level activity counts are a reliable
  signal for where enablement investment pays off, as opposed to simply
  where CCA/CCR happen to already be enabled or adopted.

### Claim 7: Enterprise-level access requires enterprise owner, billing manager, or a custom role granting "View Enterprise Copilot Metrics"; organization-level access requires organization owner or a custom role granting "View Organization Copilot Metrics" — with distinct OAuth/PAT scope requirements per level

- **Evidence**: The changelog states a single blanket access rule; the linked
  REST API reference page states two more specific, level-differentiated
  access rules not present in the changelog itself.
- **Confidence**: settled (access tiers stated explicitly in the official
  REST API reference page, which is more granular and specific than the
  changelog's summary)
- **Quote (changelog)**: "Enterprise owners and billing managers,
  organization owners, and anyone with a custom organization or enterprise
  role that grants the View Copilot Metrics permission can access these
  reports. The Copilot usage metrics policy must be enabled to support this
  functionality."
- **Quote (REST reference page, enterprise endpoint)**: "Enterprise owners,
  billing managers, and authorized users with fine-grained "View Enterprise
  Copilot Metrics" permission can retrieve Copilot metrics reports for the
  enterprise. OAuth app tokens and personal access tokens (classic) need
  either the `manage_billing:copilot` or `read:enterprise` scopes to use this
  endpoint."
- **Quote (REST reference page, organization endpoint)**: "Organization
  owners and authorized users with fine-grained "View Organization Copilot
  Metrics" permission can retrieve Copilot metrics reports for the
  organization. OAuth app tokens and personal access tokens (classic) need
  the `read:org` scope to use this endpoint."
- **Our assessment**: The changelog collapses two distinct, level-specific
  permission names ("View Enterprise Copilot Metrics" and "View Organization
  Copilot Metrics") into one generic phrase ("View Copilot Metrics") — the
  actual custom-role permission a Copilot metrics consumer must be granted
  differs depending on whether they need enterprise-scope or org-scope
  access, and granting one does not imply the other. This refines (does not
  contradict) the "View Enterprise Copilot Metrics" custom role already
  documented in `docs-github-copilot-team-level-usage-metrics.md` Claim 7 —
  that note's team-level source only documented the enterprise-scope
  permission name; this source is the first in the corpus to also document
  the parallel org-scope permission name and its distinct `read:org` OAuth
  scope requirement. Teams provisioning metrics-only access for data
  analysts must grant the correct scoped permission per report level, not a
  single blanket grant.

### Claim 8: The enterprise endpoint supports GitHub App user and installation access tokens as fine-grained token types; the organization endpoint additionally supports fine-grained personal access tokens

- **Evidence**: "Fine-grained access tokens for..." subsections on the REST
  API reference page, listed separately for each endpoint.
- **Confidence**: settled (definitional token-support matrix, stated
  explicitly and distinctly per endpoint on the official reference page)
- **Quote (enterprise endpoint)**: "This endpoint works with the following
  fine-grained token types: GitHub App user access tokens GitHub App
  installation access tokens"
- **Quote (organization endpoint)**: "This endpoint works with the following
  fine-grained token types: GitHub App user access tokens GitHub App
  installation access tokens Fine-grained personal access tokens"
- **Our assessment**: This is a token-support asymmetry not mentioned in the
  changelog and not previously documented for any other Copilot metrics
  endpoint in the corpus. A team automating enterprise-level repository
  report retrieval via a fine-grained personal access token (rather than a
  GitHub App) would find that token type unsupported at the enterprise
  scope, even though it works at the organization scope. Pipelines
  targeting the enterprise endpoint must use a GitHub App token instead.

## Concrete Artifacts

### API Endpoints and Response Schema (from GitHub REST API reference, `docs.github.com/rest/copilot/copilot-usage-metrics`, fetched 2026-07-18)

```
# Copilot usage metrics API — repository-level report endpoints (GA July 17, 2026)

GET /enterprises/{enterprise}/copilot/metrics/reports/repos-1-day?day=YYYY-MM-DD
  Access: enterprise owner, billing manager, or fine-grained
          "View Enterprise Copilot Metrics" permission
  OAuth/PAT (classic) scopes: manage_billing:copilot OR read:enterprise
  Fine-grained token types: GitHub App user access tokens,
                            GitHub App installation access tokens
  Fine-grained permission required: "Enterprise Copilot metrics" (read)

GET /orgs/{org}/copilot/metrics/reports/repos-1-day?day=YYYY-MM-DD
  Access: organization owner, or fine-grained
          "View Organization Copilot Metrics" permission
  OAuth/PAT (classic) scopes: read:org
  Fine-grained token types: GitHub App user access tokens,
                            GitHub App installation access tokens,
                            Fine-grained personal access tokens
  Fine-grained permission required: "Organization Copilot metrics" (read)

# Response schema (identical shape for both endpoints), Status: 200
# Schema title on reference page: "Copilot Metrics 1 Day Report"
{
  "download_links": [
    "https://example.com/copilot-usage-report-1.ndjson",
    "https://example.com/copilot-usage-report-2.ndjson"
  ],
  "report_day": "2025-07-01"
}

# Report content rule: only repositories with CCA or CCR activity on the
# specified day are included as rows in the downloaded NDJSON file(s).
# Exact per-row JSON field names are not documented on this reference page —
# only the wrapper response (download_links / report_day) is specified. The
# row schema is presumably documented inside the NDJSON file itself or a
# separate guide not linked from this reference page.
```

*Source: GitHub REST API reference, "Get Copilot enterprise repository report
for a specific day" and "Get Copilot organization repository report for a
specific day," fetched directly via `curl` on 2026-07-18 (not through
WebFetch, to guarantee verbatim field names and quotes per MINER.md §2a).*

### Verbatim Changelog Body Text (July 17, 2026, confirmed via raw HTML fetch)

```
Repository-level GitHub Copilot usage metrics generally available
Release | July 17, 2026 • 1 minute read

What's new
The Copilot usage metrics REST API now reports repository-level activity.
Two new endpoints return a daily, per-repository breakdown of pull request
activity for Copilot coding agent and Copilot code review. They do this for
both enterprise and organization reports.

Two new endpoints return a per-repository report for a single day:
GET /enterprises/{enterprise}/copilot/metrics/reports/repos-1-day?day=YYYY-MM-DD
GET /orgs/{org}/copilot/metrics/reports/repos-1-day?day=YYYY-MM-DD

Each response returns the following activity:
Pull requests created and merged by Copilot coding agent.
Pull requests reviewed by Copilot code review, with suggestion counts
broken down by comment type.

Why this matters
Until now, Copilot usage metrics stopped at the organization and user level.
Repository-level reporting lets you see exactly where Copilot coding agent
and Copilot code review are driving pull request activity across your
codebase. This is the foundation for repository insights and AI-readiness
reporting, so you can target enablement at the repositories that stand to
benefit most.

Important notes
Enterprise owners and billing managers, organization owners, and anyone with
a custom organization or enterprise role that grants the View Copilot
Metrics permission can access these reports. The Copilot usage metrics
policy must be enabled to support this functionality.

Visit the Copilot usage metrics API documentation to get started.
```

*Source: https://github.blog/changelog/2026-07-17-repository-level-github-copilot-usage-metrics-generally-available,
retrieved via direct `curl` fetch of the raw HTML `<article>` element on
2026-07-18.*

### Updated Metrics Granularity Landscape (as of July 17, 2026)

```
Copilot Usage Metrics — Granularity Tiers (corpus-compiled, July 17, 2026)

Tier: Enterprise/org aggregate (pre-computed, direct field access)
  GET /enterprises/{enterprise}/copilot/metrics
  GET /orgs/{org}/copilot/metrics
  → CCA active-user counts (Apr 10), code review active/passive counts
    (Apr 22), ai_credits_used (Jun 19), etc. — inline JSON fields, no download.

Tier: Team (NDJSON download, JOIN required)         — added May 14, 2026
  GET .../copilot/metrics/reports/user-teams-1-day
  → join to per-user report on user_id+day, then aggregate.

Tier: Per-user (NDJSON/JSON report, direct rows)     — reports since ~Mar 2026
  GET .../copilot/metrics/reports/users-1-day
  GET .../copilot/metrics/reports/users-28-day
  → one row per user per day (or per 28-day window); includes ai_credits_used.

Tier: Repository (NDJSON download, single-day only)  — added July 17, 2026 (THIS SOURCE)
  GET .../copilot/metrics/reports/repos-1-day
  → one row per repository per day, CCA + CCR breakdown.
  → constraint: only repos with activity that day are included (sparse).
  → constraint: no repos-28-day variant confirmed (single-day only, as of
    this extraction).
  → constraint: enterprise-scope token support excludes fine-grained PATs
    (GitHub App tokens only); org-scope supports fine-grained PATs.

Not yet unified: no documented JOIN or non-additivity relationship between
the repository tier and the team or aggregate tiers (contrast with the team
tier, which the May 14 changelog explicitly warns is non-additive against
org/enterprise totals).
```

*Compiled from: April 10, April 22, May 14, June 19, and July 17, 2026 GitHub
changelogs, cross-checked against the REST API reference page fetched
2026-07-18.*

## Cross-References

- **Extends** `docs-github-copilot-team-level-usage-metrics.md`:
  - Claim 2 (signed download URLs to NDJSON reports): This source's response
    schema (Claim 3 above) is the identical delivery pattern — a wrapper
    JSON object with `download_links` to signed NDJSON files — now applied
    to a repository-keyed report instead of a team-keyed one. Confirms the
    signed-URL/NDJSON pattern is now the standard delivery mechanism for any
    Copilot metrics report beyond the enterprise/org aggregate fields, not a
    one-off for the team-level report.
  - Claim 7 ("View Enterprise Copilot Metrics" custom role): This source's
    Claim 7 above adds the previously undocumented parallel org-scope
    permission name ("View Organization Copilot Metrics") and its distinct
    `read:org` scope requirement — refining, not contradicting, the
    enterprise-scope permission the May 14 source documented.
  - The May 14 source's Concrete Artifacts "Metrics Granularity Hierarchy"
    diagram (Tiers 1–4) predates and does not include a repository tier —
    this source is the update that diagram needs; see the "Updated Metrics
    Granularity Landscape" artifact above, which extends it with the new
    repository tier.

- **Extends** `docs-github-copilot-usage-metrics-ai-credits-per-user.md`
  Claim 4 (the `ai_credits_used` field appears in both single-day and 28-day
  user-level reports): This source's Claim 5 above documents that the new
  repository-level report, by contrast, has no confirmed 28-day variant —
  the per-user report's dual-window availability is not automatically true
  of every new report type the Copilot metrics API adds. Teams should not
  assume windowing parity across report types.

- **Corroborates** `docs-github-copilot-cca-usage-metrics-aggregate.md` and
  `docs-github-copilot-code-review-usage-metrics-aggregate.md`: Both prior
  sources document the systematic, incremental, per-surface expansion
  pattern of the Copilot usage metrics API (CCA aggregate counts April 10,
  code review aggregate counts April 22). This source's repository-level
  release on July 17 continues that same incremental pattern, this time
  adding a new dimension (repository) rather than a new surface.

- **Contradicts** `docs-github-copilot-team-level-usage-metrics.md` frontmatter
  and Claim 1 (team-level Copilot usage metrics reached general availability
  on May 14, 2026): This source's Claim 6 quote — "Until now, Copilot usage
  metrics stopped at the organization and user level" — omits that tier.
  **Filed as contradiction issue #2018** (per MINER.md §4a); no verdict is
  asserted here. See Claim 6's "Our assessment" for the filer's read of the
  likely reconciliation (a loose editorial use of "level" in the July 17
  changelog, not a technical claim that the team tier doesn't exist), which
  is not binding — the issue is open for human/Smith resolution.

- **Novel**:
  - **Repository as a queryable Copilot metrics dimension**: No prior source
    in the corpus documents any mechanism to attribute Copilot PR activity
    to individual repositories. All prior tiers (aggregate, team, per-user)
    are keyed by organizational scope or by user — this is the first
    repository-keyed report.
  - **Sparse-inclusion reporting rule** (Claim 4): "Only repositories that
    had activity on the specified day are included" is a report-completeness
    caveat not documented for any other Copilot metrics report type in the
    corpus — the per-user and team-level reports are not described as
    omitting inactive rows.
  - **Report-type windowing asymmetry** (Claim 5): The corpus's first
    documented case of a new Copilot metrics report type shipping with only
    a single-day window while an existing, structurally similar report type
    (per-user) has both single-day and 28-day windows.
  - **Token-type support asymmetry between enterprise and org scope**
    (Claim 8): Not documented for any other Copilot metrics endpoint in the
    corpus — fine-grained PATs work at org scope but not enterprise scope
    for this specific report.
  - **Self-contradicting vendor "why this matters" framing** (Claim 6): The
    first case in the corpus where a Copilot metrics changelog's own
    marketing framing appears to conflict with a prior changelog from the
    same vendor, rather than with an independent third-party source.

## Guide Impact

- **Chapter 05 (Measurement) — "Metrics granularity hierarchy" section**: If
  this section exists or is added (per the Guide Impact recommendation
  already made in `docs-github-copilot-team-level-usage-metrics.md`), update
  it to add the repository tier alongside enterprise/org aggregate, team, and
  per-user. Use the "Updated Metrics Granularity Landscape" artifact above as
  the current (as of July 17, 2026) reference diagram. Explicitly flag that
  no JOIN or non-additivity relationship between the repository tier and the
  other tiers is documented by GitHub — unlike the team tier, which came with
  an explicit non-additivity warning against org totals — so the guide
  should not assume repository totals sum cleanly to org or team totals
  without independent verification.
- **Chapter 05 — do not cite the July 17 changelog's "why this matters"
  framing as a factual history of Copilot metrics granularity** without
  flagging contradiction issue #2018. If Ch05 discusses the timeline of
  Copilot metrics API expansion, the timeline should be built from the dated
  claims in the corpus's own changelog notes (April 10, April 22, May 14,
  June 19, July 17), not from any single changelog's self-description of
  "what existed until now."
- **Chapter 02 (Harness Engineering) — "Enterprise Copilot observability
  pipeline" section**: Add the repository-level report as a third
  download-and-parse pipeline component (alongside the existing
  aggregate-field query and the team-level NDJSON+JOIN component documented
  from the May 14 source). Note the single-day-only windowing (Claim 5)
  means a rolling 28-day repository trend requires the pipeline to fetch and
  retain 28 daily reports itself — there is no server-side rolling window for
  this report type as there is for per-user reports.
- **Chapter 02 — "Metrics access governance" section**: Extend the existing
  recommendation (from `docs-github-copilot-team-level-usage-metrics.md`) to
  note that "View Copilot Metrics"-style custom roles are level-specific —
  "View Enterprise Copilot Metrics" and "View Organization Copilot Metrics"
  are two distinct grants (Claim 7), and pipelines using fine-grained PATs
  must additionally account for the enterprise-scope token-type restriction
  (Claim 8: GitHub App tokens only at enterprise scope, PATs supported at org
  scope).

## Extraction Notes

1. **Source is a very short product changelog (~130 words of body text)**:
   All substantive changelog-level claims are extracted above. To meet
   MINER.md's "read deeply, follow linked pages" requirement given how thin
   the changelog itself is, the linked REST API documentation page
   (`docs.github.com/rest/copilot/copilot-usage-metrics`) was fetched
   directly and searched for the two new endpoints' full documentation
   (response schema, access tiers, scopes, fine-grained token support) — this
   is the source of Claims 3, 5, 7, and 8, none of which are stated in the
   changelog itself.
2. **WebFetch produced a corrupted quote; raw HTML fetch was used instead**:
   An initial WebFetch call on the changelog page returned "Repository-level
   reporting lets you see exactly where Copilot coding agent and Copilot
   code" review drive pull request activity..." — a garbled, prematurely
   closed quotation with a missing word ("are") and a stray closing quote
   mark mid-sentence, consistent with model-processing corruption during
   WebFetch's summarization pass. Per MINER.md §2a, the changelog page was
   re-fetched via direct `curl` and the `<article>` element's raw text was
   extracted and used for every quote in this note instead. The corrected,
   verbatim sentence is quoted in full in Claim 6.
3. **Comment-type categories not resolved**: The changelog's "suggestion
   counts broken down by comment type" (Claim 4) does not define what the
   comment-type categories are. The fetched REST reference page's endpoint
   description does not enumerate them either — only the wrapper response
   schema (`download_links` and a single `report_day` field) is
   documented on that page; the per-row NDJSON schema, which would presumably
   define the comment-type enum, is not published on the reference page
   reachable from this changelog. This gap is noted in Concrete Artifacts
   rather than guessed at.
4. **Windowing-asymmetry verification method**: Claim 5's conclusion (no
   `repos-28-day` variant) is based on a full-text search of the fetched
   REST reference page HTML (460KB) for the literal strings `repos-28-day`,
   `repos-1-day`, `users-1-day`, `users-28-day`, and `user-teams-1-day`. The
   first returned 0 matches; the other four each returned 6 matches
   (consistent with each endpoint name appearing in a request-example block,
   a response-schema block, a prose description, and code-sample tabs). This
   is documentary evidence of absence on the specific page fetched on
   2026-07-18, not a claim that GitHub could never add a `repos-28-day`
   endpoint later — the Assayer or a future miner should re-check this if
   citing Claim 5 after this date.
5. **Contradiction filed, not resolved, in this note**: Per MINER.md §4a,
   this note does not pick a winner between this source's "why this matters"
   framing and the existing team-level source note. Contradiction issue
   #2018 was filed with a recommended verdict (`accepted-A`, i.e., trusting
   the team-level tier's documented GA date over the July 17 framing
   sentence) but that recommendation is not binding — see the issue for the
   full Side A / Side B writeup.
6. **Docs page fetched once, not paginated further**: The REST API reference
   page for `docs.github.com/rest/copilot/copilot-usage-metrics` is a single
   long page (460KB of HTML) covering many Copilot metrics endpoints beyond
   the two new repository-level ones; only the sections relevant to
   `repos-1-day` were extracted for this note. No additional linked pages
   (e.g., "How are metrics attributed across organizations," referenced in
   the org-level endpoint's description) were followed — that link covers
   organization-metrics attribution generally, not anything specific to the
   repository-level report, and is out of scope for this extraction.
