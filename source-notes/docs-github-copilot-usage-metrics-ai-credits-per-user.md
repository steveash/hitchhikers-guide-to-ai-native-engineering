---
source_url: https://github.blog/changelog/2026-06-19-ai-credits-consumed-per-user-now-in-the-copilot-usage-metrics-api
source_type: docs
title: "AI credits consumed per user now in the Copilot usage metrics API"
author: GitHub (official changelog)
date_published: 2026-06-19
date_extracted: 2026-06-21
last_checked: 2026-06-21
status: current
confidence_overall: settled
issue: "#1251"
---

# AI Credits Consumed Per User in the Copilot Usage Metrics API (GitHub Changelog)

> GitHub's June 19, 2026 changelog introduces the `ai_credits_used` field to per-user
> Copilot usage metrics reports — a billing-derived cost metric that adds a spending
> dimension to the existing activity-count and behavioral-segmentation metrics, enabling
> per-user AI credit consumption tracking at the enterprise and organization level.

## Source Context

- **Type**: docs (GitHub official product changelog, ~200 words, June 19, 2026)
- **Author credibility**: GitHub engineering team announcing a production API change.
  Authoritative for the existence of the new field, its derivation from billing data, its
  scope limitations (no feature/model/surface breakdown), and the access requirements. Not
  a credible source for causal claims about cost-productivity correlations — no outcome data
  is cited.
- **Scope**: The new `ai_credits_used` field in the Copilot usage metrics REST API: what it
  measures, which reports it appears in, how it relates to billing data, its granularity
  limitations, and three stated use cases. Does NOT cover: the exact field schema or data
  type; how the field interacts with the adoption phase cohort model (introduced May 29,
  2026); how it behaves for users surfaced only via server-side telemetry (June 15, 2026
  expansion); whether feature-level breakdown will be added in future; or what constitutes
  a normal or high per-user AI credit consumption level.

## Extracted Claims

### Claim 1: A new `ai_credits_used` field has been added to per-user Copilot usage metrics reports, showing total AI credits consumed per user per day

- **Evidence**: Official GitHub product changelog announcing the feature with explicit
  field name, report location, and time granularity.
- **Confidence**: settled (product fact — the field exists as described)
- **Quote**: "The Copilot usage metrics API now includes an `ai_credits_used` field for
  each user in user-level reports, showing total AI credits consumed per day."
- **Our assessment**: This is the first per-user cost metric in the Copilot usage metrics
  API. All prior metrics documented in the corpus — active user counts (April 10, 2026),
  team-level attribution (May 14), adoption phase cohorts (May 29), server-side telemetry
  expansion (June 15) — measure behavioral activity: what users did, on which surfaces,
  at what frequency. This field answers the distinct question "how much did each user's
  Copilot activity cost?" — bridging the activity API with the billing record. The per-day
  granularity matches the existing per-user usage reports, enabling day-by-day cost tracking
  alongside activity counts.

### Claim 2: The `ai_credits_used` metric is derived from the same data used in the usage-based billing API, not from client-side telemetry

- **Evidence**: Explicit derivation statement in the official changelog.
- **Confidence**: settled (explicit derivation claim from the changelog)
- **Quote**: "This metric is derived from the same data used in the usage-based billing API"
- **Our assessment**: This is operationally significant in the context of the June 15, 2026
  server-side telemetry update (`docs-github-copilot-usage-metrics-server-side-telemetry.md`
  Claim 1), which noted that prior Copilot usage metrics were built from client-side
  telemetry that can fail to reach GitHub due to network conditions, proxy configurations,
  and client settings. The `ai_credits_used` field bypasses this gap — because billing
  data is server-authoritative, a user whose client telemetry was silently dropped will
  still have their AI credit consumption correctly recorded. This makes `ai_credits_used`
  more complete than activity-count fields for organizations in proxy or firewall environments.

### Claim 3: The `ai_credits_used` field is an overall per-user total across all Copilot activity and is not currently broken down by feature, model, or surface

- **Evidence**: Explicit "Important Notes" statement in the changelog.
- **Confidence**: settled (explicitly documented scope limitation)
- **Quote**: "`ai_credits_used` is an overall per-user total. It is not currently broken
  down by feature, model, or surface."
- **Our assessment**: "Not currently" implies breakdown granularity may be added in a
  future API iteration. For now, a user who uses Copilot completions, Copilot chat, and
  Copilot cloud agent in a single day will have a single combined `ai_credits_used` value
  with no way to attribute costs to individual features from this field alone. This is a
  meaningful limitation for teams trying to understand ROI per Copilot surface or justify
  individual feature investments. The phrasing "not currently" should be watched for a
  future changelog adding feature-level cost breakdown.

### Claim 4: The field appears in both single-day and 28-day user-level reports at enterprise and organization levels

- **Evidence**: Explicit scope statement in the official changelog.
- **Confidence**: settled (definitional product fact)
- **Quote**: "The field appears in both single-day and 28-day user-level reports at
  enterprise and organization levels."
- **Our assessment**: Availability in both report windows enables two analytical modes:
  (1) day-level cost tracking for operations monitoring and anomaly detection, and (2)
  28-day rolling cost totals for monthly budget tracking and trend analysis. The 28-day
  window aligns with the `monthly_active_copilot_cloud_agent_users` field (April 10
  changelog) and the `ai_adoption_phase` classification window (May 29 changelog), creating
  a consistent 28-day analytical horizon across activity, phase, and cost dimensions.
  Both enterprise and organization level access means the same field is queryable at two
  scopes without custom aggregation.

### Claim 5: The `ai_credits_used` field is a metrics signal for consumption analysis, not a billed total — billing documentation should be consulted for invoicing information

- **Evidence**: Explicit "Important Notes" statement in the official changelog.
- **Confidence**: settled (explicitly documented behavioral constraint)
- **Quote**: "The field serves as a metrics signal for consumption analysis, not a billed
  total—refer to billing documentation for invoicing information."
- **Our assessment**: This is a critical distinction for teams building cost governance
  pipelines. The `ai_credits_used` value in the metrics API should not be treated as the
  definitive invoiced amount — rounding, billing adjustments, or aggregation differences
  between the metrics API and the billing API may produce discrepancies. For cost
  attribution and chargebacks, the metrics value is appropriate; for financial
  reconciliation, the billing API is authoritative. Any dashboard or alert built on this
  field should clearly label it as "estimated consumption" rather than "billed amount."

### Claim 6: Access requires enterprise administrator or organization owner status with access to Copilot usage metrics through the REST API

- **Evidence**: Explicit "Important Notes" access tier statement in the official changelog.
- **Confidence**: settled (consistent with access tier documented across all prior Copilot
  metrics changelog notes)
- **Quote**: "These metrics are available to enterprise administrators and organization
  owners with access to Copilot usage metrics through the REST API."
- **Our assessment**: Consistent with the access tier documented across the full Copilot
  metrics API series (April 8, April 10, May 14, May 29, June 15 changelogs). The May 14
  changelog additionally documented a "View Enterprise Copilot Metrics" custom role as a
  metrics-access path — that custom role likely grants access to this new field as well,
  though this changelog does not explicitly confirm it. Teams granting metrics access to
  data analysts or engineering managers via the custom role should verify access to
  `ai_credits_used` in practice.

### Claim 7: Three intended use cases are correlating AI credit consumption with productivity outcomes, understanding credit distribution across teams, and planning for usage-based billing

- **Evidence**: Explicit "Why This Matters" section in the official changelog, three
  bullet points.
- **Confidence**: anecdotal (vendor framing of intended use cases; no evidence that
  organizations have successfully applied this field for these purposes)
- **Quote**: "Connect consumption to value: The metric sits alongside existing usage
  tracking, enabling visibility into consumption relative to the work driving it."
- **Quote**: "Understand adoption across teams: Organizations can see how AI credit usage
  distributes across teams to identify where Copilot delivers maximum value."
- **Quote**: "Plan for usage-based billing: Monitoring consumption patterns helps
  anticipate AI credit ranges and inform budgeting decisions."
- **Our assessment**: The first use case (connecting consumption to value) is analytically
  ambitious: placing `ai_credits_used` alongside activity metrics (completions accepted,
  suggestions generated) and outcome metrics (PRs merged, time to merge) could enable a
  rudimentary cost-per-outcome calculation. The second use case (team credit distribution)
  builds directly on the May 14 team-level metrics infrastructure — team-level
  `ai_credits_used` aggregation now gives teams a cost layer on top of existing activity
  attribution. The third use case (billing planning) is the most immediately practical:
  per-user consumption trends help predict monthly bills before the billing cycle closes.
  None of these use cases are evidence-based; they represent vendor-suggested patterns.

## Concrete Artifacts

### New API Field (from changelog, June 19, 2026)

```
# Copilot usage metrics API — per-user AI credits field (added June 19, 2026)
# Available at:
#   GET /enterprises/{enterprise}/copilot/metrics
#   GET /orgs/{org}/copilot/metrics
# Report types: single-day (users-1-day) and 28-day (users-28-day) user-level reports
# Scope: enterprise and organization levels
# Access: enterprise administrators and organization owners with Copilot usage metrics
#         REST API access

ai_credits_used
  Type:        numeric (exact type unspecified in changelog)
  Description: Total AI credits consumed by the user across all Copilot activity
               for the reporting period.
  Granularity: per-user total only — NOT broken down by feature, model, or surface.
  Derivation:  Same data source as the usage-based billing API (server-side;
               not affected by client-side telemetry gaps).
  Note:        Metrics signal for consumption analysis, not a billed total.
               Consult billing API / billing documentation for invoicing purposes.
```

*Source: AI credits consumed per user now in the Copilot usage metrics API,
GitHub Changelog, June 19, 2026*

### Copilot Usage Metrics Analytical Dimensions (as of June 19, 2026)

```
Copilot Usage Metrics — Cumulative Analytical Dimensions (as of June 19, 2026)

Activity dimension (WHAT users did, HOW OFTEN):
  daily_active_copilot_cloud_agent_users   → CCA DAU            (added April 10, 2026)
  weekly_active_copilot_cloud_agent_users  → CCA WAU            (added April 10, 2026)
  monthly_active_copilot_cloud_agent_users → CCA MAU            (added April 10, 2026)
  monthly_active_agent_users               → IDE agent MAU      (pre-existing)
  used_copilot_coding_agent                → per-user CCA flag  (March 25, 2026)

Team dimension (WHO in which team):
  user-teams-1-day report + JOIN on user_id+day → team attribution (May 14, 2026)

Maturity/behavior dimension (AT WHAT CAPABILITY LEVEL):
  ai_adoption_phase (user-level field)     → Phase 0–3 per user  (May 29, 2026)
  totals_by_ai_adoption_phase (org/ent)    → aggregate by phase  (May 29, 2026)

Cost dimension (HOW MUCH usage costs):          ← NEW June 19, 2026
  ai_credits_used                          → per-user total AI credits consumed

Telemetry note:
  Activity counts: client-side primary + server-side supplement (effective June 15, 2026)
  ai_credits_used: billing-derived (server-side) — NOT affected by client
                   telemetry gaps that can undercount activity fields.

Still missing (as of June 19, 2026):
  Cost by feature, model, or surface       → not yet available
  Outcome metrics (task completion rate)   → not yet available
  Cost breakdown per adoption phase        → not confirmed available
  Cost trends / alerts in GitHub-native UI → not confirmed available
```

*Compiled from: April 10, May 14, May 29, June 15, and June 19, 2026 GitHub changelogs*

## Cross-References

- **Extends** `docs-github-copilot-cca-usage-metrics-aggregate.md` Claim 6 (multi-surface
  Copilot adoption view — "These counts sit alongside existing metrics like
  `monthly_active_agent_users` (IDE agent mode) and the user-level
  `used_copilot_coding_agent` flag, giving you a full view of Copilot adoption across
  surfaces"): The April 10 source documented the first multi-surface activity view of
  Copilot metrics. `ai_credits_used` (June 19) extends that view from behavioral activity
  to cost — the same multi-surface total, now expressed as a cost value. Together, the
  April 10 activity counts and June 19 cost metric give enterprise admins both "how often?"
  and "how much?" dimensions at the user level.

- **Extends** `docs-github-copilot-team-level-usage-metrics.md` Claim 1 (team-level
  attribution via the user-teams report JOIN on user_id and day): The May 14 source enables
  team-level activity aggregation. That same JOIN pattern can now include `ai_credits_used`
  to produce team-level cost totals — joining the user-teams report to per-user cost records
  gives a team AI credit spend summary. This is the "Understand adoption across teams" use
  case described in the June 19 changelog. Note the same non-additivity constraint from
  `docs-github-copilot-team-level-usage-metrics.md` Claim 9 applies: users in multiple
  teams will have their `ai_credits_used` counted in each team's aggregate, so team cost
  totals cannot be summed to reproduce an org total.

- **Extends** `docs-github-copilot-usage-metrics-adoption-cohorts.md` Claim 7 (per-phase
  metrics include engaged users, interaction averages, code generation/acceptance activity,
  PR metrics, and median time-to-merge averages — but no cost metrics): The May 29 phase
  model provides behavioral segmentation and delivery velocity signals. `ai_credits_used`
  now adds a cost dimension: by cross-referencing phase data with per-user cost records,
  teams can compute average AI credit spend per user by adoption phase — answering whether
  Phase 3 (multi-agent) users spend proportionally more than Phase 1 users or whether they
  achieve more per credit consumed. The changelog does not address whether
  `totals_by_ai_adoption_phase` will be extended with per-phase cost totals.

- **Extends** `docs-github-copilot-usage-metrics-server-side-telemetry.md` Claim 1
  (Copilot usage reports have historically been built from client-side telemetry only,
  which can fail to reach GitHub due to network conditions, proxy configurations, or client
  settings — causing active, billed users to be absent from reports): The June 15 source
  documented a coverage gap in client-side activity metrics. `ai_credits_used` (June 19)
  is explicitly "derived from the same data used in the usage-based billing API" — a
  server-side source not affected by client telemetry gaps. A user whose client telemetry
  silently failed will appear in `ai_credits_used` with correct credit consumption but may
  appear in activity counts only via the server-side supplement (with empty
  `totals_by_ide` and `totals_by_feature` breakdowns per Claim 4 of that note). For cost
  governance pipelines in enterprise environments, `ai_credits_used` provides more complete
  per-user coverage than activity-based cost proxies.

- **Corroborates** `docs-github-copilot-aw-github-token-auth.md` Claim 3 ("When you use
  the Actions token in an agentic workflow running in an organization-owned repository, AI
  credits consumed by your agentic workflow are billed directly to the organization"):
  The June 11 source established that org billing shifts AI credit costs from individual
  users to the organization when GITHUB_TOKEN is used for agentic workflows. The
  `ai_credits_used` field (June 19) provides the metrics API visibility into those
  per-user costs — enabling organizations to see, per user, how many AI credits their
  agentic workflow activity is consuming. Together, the two sources describe the complete
  billing → tracking loop: costs accrue to the org (June 11 enablement), costs are
  queryable per user via the metrics API (June 19 field).

- **Novel**:
  - **First per-user cost metric in the Copilot usage metrics API**: All prior corpus notes
    cover activity, adoption, and behavioral segmentation. `ai_credits_used` is the first
    field in the metrics API that directly measures cost rather than behavioral activity.
  - **Billing-derived metric exposed via the metrics API**: `ai_credits_used` crosses the
    boundary between the activity/usage metrics API and the billing API — derived from
    billing data but accessible via the metrics endpoint. This is a novel architectural
    pattern in the Copilot API surface in the corpus.
  - **Cost vs. metrics signal distinction** (Claim 5): The explicit "not a billed total"
    caveat is the first time any corpus source distinguishes between a metrics API signal
    and the authoritative billing record. Teams building cost dashboards need to understand
    this distinction.
  - **Differential completeness within the metrics API**: The observation (from Claim 2 and
    the June 15 cross-reference) that `ai_credits_used` has different and superior coverage
    to activity-count fields due to its billing derivation is novel. No prior corpus source
    notes that different fields in the same metrics API have different completeness
    characteristics based on their underlying data source.

## Guide Impact

### Chapter 05: Measurement — Cost Governance Metrics

- **Section "Per-user AI credit consumption tracking" (new)**: Reference `ai_credits_used`
  as the first vendor-native per-user cost metric for Copilot in the metrics API.
  Distinguish from activity-count metrics — those answer "how much was Copilot used?";
  this answers "what did each user's usage cost?" Document the "not a billed total" caveat:
  `ai_credits_used` is appropriate for consumption dashboards and cost attribution but not
  for financial invoice reconciliation.
- **Section "Cost attribution via team JOIN" (add or extend)**: Note that joining
  `ai_credits_used` from the per-user report with the user-teams report (May 14 JOIN
  pattern, `docs-github-copilot-team-level-usage-metrics.md` Claim 1) produces team-level
  AI credit spend totals — the same JOIN pattern used for team activity attribution now
  extends to cost. This enables showback/chargeback models aligned with existing team
  structures. Apply the same non-additivity caveat from `docs-github-copilot-team-level-usage-metrics.md`
  Claim 9: team cost totals cannot be summed to reproduce org totals.
- **Section "Cost-phase correlation" (add)**: Suggest cross-referencing `ai_credits_used`
  against `ai_adoption_phase` (May 29) per user to compute average cost-per-phase. If
  Phase 3 (multi-agent) users generate materially different credit consumption than Phase 1
  (code-first) users, this informs AI budget allocation. Flag selection bias: higher-phase
  users may already be heavier tool users independently of Copilot.
- **Section "Usage-based billing forecasting" (add)**: Document the "Plan for usage-based
  billing" use case — monitoring 28-day rolling `ai_credits_used` trends provides early
  signals for monthly billing before the invoice closes. Because the field is billing-derived
  (not client-telemetry-derived), it is more reliable for full-population coverage than
  activity-based cost proxies, particularly in proxy/firewall environments.

### Chapter 02: Harness Engineering — Observability and Cost Management

- **Section "Enterprise Copilot observability pipeline"**: Add `ai_credits_used` as a
  new field tier in the recommended metrics pipeline. Note its different completeness
  characteristics from activity fields: billing-derived means it will NOT have the coverage
  gaps noted in the June 15 server-side telemetry note
  (`docs-github-copilot-usage-metrics-server-side-telemetry.md` Claim 1). Pipelines that
  validate total active users against breakdown field sums (per that note's guidance) should
  NOT apply the same validation to `ai_credits_used` — its coverage basis is different.
- **Section "Agentic workflow cost management"**: Link this field to the June 11 GITHUB_TOKEN
  announcement (`docs-github-copilot-aw-github-token-auth.md` Claim 3): when GITHUB_TOKEN
  triggers org billing for agentic workflows, `ai_credits_used` in the per-user metrics
  reports becomes the observability mechanism for tracking how much each user's agentic
  workflow activity draws from the org's AI credit pool. Document this as the "billing loop"
  — costs accrue to org (June 11 enablement), costs tracked per user via metrics API
  (June 19 field).

## Extraction Notes

1. **Source is an extremely short product changelog (~200 words)**: Described as a
   "1 minute read." All substantive claims are exhausted in the seven claims above. The
   source is a concise announcement covering one new field, three use cases, and three
   important notes.
2. **Two WebFetch passes**: Two separate fetches were made. The second pass returned a
   closer-to-verbatim rendering. All quotes used above appeared consistently across both
   passes. The em dash in the Claim 5 quote ("not a billed total—refer to billing
   documentation") appears in the source; the Assayer should verify this punctuation
   character against the live URL.
3. **Field type not stated**: The `ai_credits_used` data type (integer vs. float, unit
   definition of "AI credits") is not specified in the changelog. The linked API documentation
   would be the authoritative source for field schema. This gap is noted in Concrete Artifacts.
4. **No contradictions filed**: No existing source note claims that per-user cost tracking
   is unavailable in the Copilot metrics API or that cost metrics are inappropriate in
   the activity metrics layer. The June 19 update is additive. No contradiction issue opened.
5. **`users-1-day` and `users-28-day` report type names**: These names appeared in one
   WebFetch pass and are consistent with naming patterns in prior Copilot metrics changelogs.
   The Assayer should verify these report type names against the source URL.
6. **Interaction with phase model and server-side telemetry not addressed by source**: The
   changelog does not state how `ai_credits_used` behaves for server-side-only users (those
   lacking `totals_by_ide`/`totals_by_feature` breakdowns after June 15). Since the field
   is billing-derived, it should be present for any user who consumed billable AI credits
   regardless of telemetry source — but this is an inference, not an explicit statement in
   the changelog.
