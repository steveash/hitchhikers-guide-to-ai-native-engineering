---
source_url: https://github.blog/changelog/2026-06-15-copilot-usage-metrics-now-include-more-of-your-active-users
source_type: docs
title: "Copilot usage metrics now include more of your active users"
author: GitHub (official changelog)
date_published: 2026-06-15
date_extracted: 2026-06-16
last_checked: 2026-06-16
status: current
confidence_overall: settled
issue: "#1189"
---

# Copilot Usage Metrics — Server-Side Telemetry Expansion (GitHub Changelog, June 15, 2026)

> GitHub's June 15, 2026 changelog announces the addition of server-side telemetry to Copilot usage metrics, closing coverage gaps where active, billed users were absent from reports due to client-side telemetry failures — with the trade-off that newly surfaced users appear in high-level DAU counts but lack detailed feature and IDE breakdowns.

## Source Context

- **Type**: docs (GitHub official product changelog, ~200 words, June 15, 2026)
- **Author credibility**: GitHub engineering team announcing a production metrics methodology change. Authoritative for the fact that the change happened, what was previously missing, and the operational trade-offs. Not a credible source for what fraction of any given organization's users were previously undercounted — the 5% example is illustrative, not a measured average.
- **Scope**: The addition of server-side telemetry to enterprise single-day and 28-day Copilot usage reports, with the consequence that newly surfaced users have full high-level DAU counts but empty `totals_by_ide` and `totals_by_feature` breakdowns. Covers: what was broken before (client-only telemetry), what changes (server-side supplement), what the practical scale looks like (~5% illustrative), and why it matters (consistency with activity log/billing, reporting resilience). Does NOT cover: which specific API endpoints or response fields carry the active user count; how server-side telemetry determines that a user was "active"; whether this affects the adoption phase cohorts introduced May 29, 2026; or any SLA on when richer telemetry becomes available for newly surfaced users.

## Extracted Claims

### Claim 1: Copilot usage reports have historically been built from client-side telemetry only, which can fail to reach GitHub due to network conditions, proxy configurations, or client settings — causing active, billed users to be absent from reports

- **Evidence**: Official GitHub product changelog explaining the prior methodology and its failure mode, under the "What's new" section.
- **Confidence**: settled (GitHub's own acknowledgment of a prior gap in their reporting methodology)
- **Quote**: "Copilot usage reports have historically been built from client-side telemetry emitted by IDEs and other clients. That telemetry is the richest source we have, but it does not always reach us. Network conditions, proxy configurations, client settings, and other factors outside of your control or ours can prevent a client from reporting activity. When that happened, an active, billed user could be absent from your reports."
- **Our assessment**: This is a significant admission: GitHub's prior reporting could structurally undercount active users in environments with restrictive network policies, corporate proxies, or misconfigured clients. Enterprise environments — the primary Copilot Enterprise deployment context — are exactly those most likely to have proxy configurations and network filtering. The gap between billing records ("this user has a seat") and usage reports ("this user shows zero activity") is a known pain point confirmed by the source's explicit mention of reducing "support escalations about 'missing' users."

### Claim 2: The June 15, 2026 update adds server-side telemetry to supplement client signals; any server-side-confirmed active user not already captured by client telemetry is now included in enterprise single-day and 28-day reports

- **Evidence**: Official GitHub product changelog announcing the methodology change.
- **Confidence**: settled (explicit product announcement of the change)
- **Quote**: "Any active user we can confirm from the server side who was not already captured from client telemetry is now included in your enterprise single-day and 28-day reports, increasing your daily active user (DAU) coverage."
- **Our assessment**: The change is additive — server-side telemetry supplements rather than replaces client telemetry. Client telemetry remains "the richest source" (Claim 1) because it provides detailed feature-level, IDE-level, and model-level breakdowns. Server-side confirmation only establishes that a user was active; it does not provide the attribution detail client telemetry supplies. This creates a two-tier user population within a single report: rich-detail users (client-confirmed) and count-only users (server-side-only). Any pipeline consuming Copilot metrics after June 15, 2026 must handle this heterogeneous user set.

### Claim 3: A concrete illustration shows this change may increase a report's DAU count by approximately 5%

- **Evidence**: Concrete example provided in the official changelog's "What you'll see in a typical report" section.
- **Confidence**: anecdotal (illustrative example, not a measured population average; actual gains will vary by deployment environment)
- **Quote**: "Suppose an enterprise single-day report previously showed 1,000 daily active users, all sourced from client telemetry. With this change, that same report might now show 1,050."
- **Our assessment**: The "might now show" wording is important — GitHub presents this as an illustrative case, not a guaranteed outcome. Organizations with well-configured clients and no proxy issues may see no change. Organizations in highly restricted network environments (government, financial services, regulated industries) may see larger gains. The example's value is establishing the order of magnitude: incremental rather than dramatic. A 5% step-up in DAU counts appearing on dashboards after June 15 should not be interpreted as genuine adoption growth — it reflects improved coverage of existing active users.

### Claim 4: Newly surfaced server-side-only users appear in high-level DAU counts but have empty breakdowns for totals_by_ide and totals_by_feature until richer telemetry is available

- **Evidence**: Explicit statement in the official changelog about the partial-data nature of server-side-only users.
- **Confidence**: settled (stated behavioral constraint from official changelog)
- **Quote**: "So for these users, the high-level counts go up while the detailed breakdowns stay empty until richer telemetry is available for them."
- **Our assessment**: This is the most operationally significant trade-off in the update. A downstream consumer that reads `totals_by_ide` or `totals_by_feature` to understand adoption patterns will not see the newly surfaced users in those breakdowns, even though those users appear in total DAU counts. Total active user counts and breakdown-level sums become intentionally inconsistent for organizations with significant proxy/client coverage gaps. Teams building dashboards must account for this: `sum(totals_by_ide)` will be less than the DAU total, and that gap is the server-side-only population — expected behavior, not a data pipeline bug.

### Claim 5: The change improves consistency between usage reports and the activity log and billing data, reducing support escalations about "missing" users

- **Evidence**: Explicit benefit statement in the official changelog's "Why this matters" section.
- **Confidence**: settled (stated design intent; the causal mechanism is plausible given the gap described in Claim 1)
- **Quote**: "Usage reports line up more closely with what you see in the activity log and billing, reducing the gaps that drive support escalations about 'missing' users."
- **Our assessment**: This addresses a documented reconciliation problem: billing showed N users with Copilot seats, the activity log showed M confirmed active users, but usage reports showed P daily active users (where P < M ≤ N). This three-number inconsistency confused administrators trying to understand whether users were genuinely inactive or simply undetected by client telemetry. The server-side supplement closes the P→M gap. The M→N gap (licensed but inactive users) remains by design — server-side telemetry does not invent activity where none occurred.

### Claim 6: Combining server-side and client-side signals creates resilience — a single client-side failure no longer erases a user from reports

- **Evidence**: Explicit benefit statement in the official changelog's "Why this matters" section, labeled "Resilient by design."
- **Confidence**: settled (stated design intent; the mechanism is straightforward — redundant signal sources)
- **Quote**: "Combining server-side and client-side signals means a single client-side hiccup no longer erases a user from your reports."
- **Our assessment**: "Resilient by design" signals that server-side telemetry is intended as a permanent architectural supplement, not a temporary patch. For organizations doing trend analysis: a user who showed up inconsistently in historical reports due to intermittent client connectivity will now appear consistently, eliminating false "dropped off" signals. However, this retrospective consistency benefit only applies to post-June 15 data — historical data before this date is not retroactively supplemented with server-side signals.

## Concrete Artifacts

### Methodology Change Summary (as of June 15, 2026)

```
# Copilot usage metrics reporting methodology — change effective June 15, 2026

BEFORE:
  Source: Client-side telemetry only (IDEs and other clients)
  Risk:   Network conditions, proxy configurations, client settings
          can prevent telemetry from reaching GitHub
  Result: Active, billed users can be absent from reports

AFTER:
  Source: Client-side telemetry (primary — "richest source") +
          Server-side telemetry (supplement — for coverage gaps)
  Logic:  Server-side confirms any active user not already
          captured from client telemetry
  Scope:  Enterprise single-day and 28-day reports (DAU coverage)
  Scale:  Illustrative ~5% increase in DAU count (varies by deployment)

TRADE-OFF for server-side-only users:
  High-level DAU count:       INCLUDED
  totals_by_ide breakdown:    EMPTY (until richer telemetry available)
  totals_by_feature breakdown: EMPTY (until richer telemetry available)
```

*Source: Copilot usage metrics now include more of your active users, GitHub Changelog, June 15, 2026*

### Three-Number Reconciliation Model (as of June 15, 2026)

```
# Pre-June 15, 2026 (inconsistent three-way):
  Billing:        N users with Copilot seats
  Activity log:   M confirmed active users    (M ≤ N)
  Usage reports:  P daily active users        (P < M — client-only gap)

# Post-June 15, 2026 (improved):
  Billing:        N users with Copilot seats
  Activity log:   M confirmed active users    (M ≤ N)
  Usage reports:  ~M daily active users       (server-side closes P→M gap)

  Residual gap: M < N — licensed-but-inactive users — by design;
  server-side telemetry does not manufacture activity.
```

*Compiled from: "What's new" and "Why this matters" sections, June 15, 2026 GitHub changelog*

## Cross-References

- **Extends** `docs-github-copilot-cca-usage-metrics-aggregate.md` Claim 2 (`daily_active_copilot_cloud_agent_users` counts unique users who used CCA on a given day): The April 10 source documents the fields that count active users (DAU, WAU, MAU); this June 15 source changes the underlying telemetry methodology that feeds those counts. Any organization-level active-user count reported through the API after June 15, 2026 may be higher than before the change — not due to adoption growth but due to improved coverage. The April 10 note's definitional claim remains correct; the June 15 change is methodological, not definitional.

- **Extends** `docs-github-copilot-usage-metrics-adoption-cohorts.md` Claim 1 (`ai_adoption_phase` classifies engaged users based on 28-day rolling window engagement): The May 29 source documents phase classification based on behavioral engagement. If newly surfaced server-side-only users lack feature-level telemetry, it is unclear whether they receive an `ai_adoption_phase` classification (which requires knowing what surfaces they engaged with) or default to Phase 0 (no cohort). The June 15 changelog does not address this interaction. Teams using phase data for adoption analysis should treat the Phase 0 count as potentially inclusive of server-side-only users whose phase cannot be determined from available telemetry.

- **Extends** `docs-github-copilot-team-level-usage-metrics.md` Claim 1 (team-level metrics via JOIN of user-teams report and per-user usage report): Newly surfaced server-side-only users will appear in per-user usage reports with confirmed active presence but empty `totals_by_ide`/`totals_by_feature` breakdowns. Team-level aggregates post-June 15 will therefore show slightly higher user counts while potentially carrying sparse breakdown detail for the server-side-only population.

- **Novel**:
  - **Server-side telemetry as a coverage supplement**: No prior source in the corpus documents the methodology underlying Copilot usage metrics counts. This is the first source to reveal that active user counts were previously client-only and were potentially undercounting users in proxy/restricted-network environments.
  - **Methodological inflection point for time-series comparability**: June 15, 2026 is a discontinuity in the Copilot metrics time series. Pre- and post-June 15 DAU counts are not directly comparable for trend analysis — a step-up in counts after this date may reflect improved coverage rather than genuine adoption growth. No prior source in the corpus addresses time-series comparability across methodology changes.
  - **Two-tier user populations within a single report**: The concept of users with full-detail breakdowns and users with count-only presence coexisting in the same report is new to the corpus. All prior sources treat per-user reports as uniform in data completeness.
  - **Three-number reconciliation (billing / activity log / usage reports)**: No prior source explicitly discusses the relationship between Copilot billing seat counts, activity log active users, and usage report active users as three distinct numbers. This source is the first to explain why they have historically differed and how the gap is being closed.

## Guide Impact

### Chapter 05: Measurement — Copilot Adoption Metrics

- **Section "Historical trend analysis and time-series comparability"** (add or extend): Flag June 15, 2026 as a methodological inflection point in the Copilot usage metrics time series. Organizations comparing DAU counts before and after this date will see a step-up that reflects improved measurement coverage, not adoption growth. Time-series analysis should treat pre- and post-June 15 data as potentially non-comparable, and adoption trend charts should note this break point to avoid misleading interpretation. Cite this source as the authority for the inflection point date and scale (~5% illustrative).
- **Section "What 'active user' counts actually measure"** (add): Reference this source as evidence that "active user" counts in the Copilot metrics API have always been a lower bound, not a precise count. The addition of server-side telemetry closes one gap; other coverage gaps may remain. Organizations should treat these numbers as directional indicators rather than exact enrollment counts.
- **Section "Metrics data quality tiers within a single report"** (new): Document that after June 15, 2026, Copilot reports contain a heterogeneous user population: rich-detail users (client telemetry confirmed, with full IDE/feature/model breakdowns) and count-only users (server-side confirmed only, with empty breakdown fields). Analysis that sums breakdown-level fields will produce a total lower than the top-level DAU count — this is expected and correct, not a data pipeline bug. Recommend making this gap explicit in dashboards as an "unlabeled activity" bucket.

### Chapter 02: Harness Engineering — Observability Pipelines

- **Section "Copilot metrics pipeline data completeness"** (add): Note that after June 15, 2026, `sum(totals_by_ide)` will be less than the total DAU count for any organization with server-side-only users. Pipelines that validate "sum of per-IDE counts equals total active users" should be updated to treat this as expected behavior. Recommend adding an explicit "unlabeled" segment capturing `total_dau - sum(totals_by_ide)` to make the coverage gap visible rather than silently hiding it.
- **Section "Activity log vs. usage report reconciliation"** (add): The June 15 update closes the gap between activity log data and usage report counts. For teams cross-validating Copilot billing against usage reports, the prior approach of treating "billing count > usage report count" as expected should be updated: post-June 15, discrepancies should be smaller and attributable to licensed-but-inactive users rather than missing telemetry. Any unusually large discrepancy after June 15 warrants investigation.

## Extraction Notes

1. **Source is a short product changelog (~200 words)**: All substantive content is exhausted in the six claims above. The changelog is a concise announcement, not a technical deep-dive — no additional passes would yield new signal.
2. **Three WebFetch passes**: Three separate fetches were made against the source URL using different prompt strategies. Verbatim quotes were cross-validated across passes for consistency. All quotes used above appeared consistently across multiple fetch responses.
3. **Field names `totals_by_ide` and `totals_by_feature`**: These field names appeared in WebFetch output as field names mentioned on the source page. They are structurally consistent with the existing Copilot metrics API schema documented in prior changelog sources. **Confirmed verbatim against the live source URL on 2026-06-21** (human verification during PR #1246 review); both field names appear exactly as written.
4. **No contradictions filed**: This source extends prior Copilot metrics sources by documenting a methodology change. No prior source claims that Copilot usage reports are complete or that client-only telemetry is sufficient — prior sources simply describe the API without addressing methodology. The June 15 update is an extension, not a contradiction.
5. **Phase model interaction not addressed by source**: The impact of the server-side telemetry on the May 29 adoption phase classification model is not addressed in the changelog. The gap is flagged in Cross-References but no contradiction issue is filed — the source makes no claims about phase classification, and no prior source makes a claim that the server-side supplement would or would not affect phase assignment.
6. **Prospector had three triage comments**: All three comments converged on Ch05 (Measurement) and Ch02 (Harness Engineering) as the relevant chapters. The second triage comment (rated "high" novelty) correctly identified the methodological change and historical comparability caveat as the key novel contribution — confirmed by this extraction.
