---
source_url: https://github.blog/changelog/2026-11-05-usage-metrics-api-flags-telemetry-and-version-gaps
source_type: docs
title: "Usage metrics API flags telemetry and version gaps"
author: GitHub (official changelog)
date_published: 2026-11-05
date_extracted: 2026-11-06
last_checked: 2026-11-06
status: current
confidence_overall: settled
issue: "#4547"
---

# Usage Metrics API Flags Telemetry and Version Gaps (GitHub Changelog, Nov 5, 2026)

> GitHub adds per-user and per-day diagnostics to the Copilot usage metrics API that reveal which users are missing client telemetry or run IDE/extension versions below the minimums, turning the June 2026 "undercounted users" caveat into something admins can query and act on.

## Source Context

- **Type**: docs (GitHub official product changelog, ~300 words, 2-minute read, Nov 5, 2026)
- **Author credibility**: GitHub's own team, authoritative on the API fields and their semantics. It gives no data on how many users are typically affected and does not specify field types or schema beyond names.
- **Scope**: Four new fields (two per-user, two daily counts), their scope (1-day and 28-day reports), access requirements, and null/overlap rules. Does NOT cover: the minimum version numbers themselves (linked as "minimum supported versions"), how "unknown" is determined, remediation steps beyond "follow up", or how this interacts with the adoption-phase fields.

## Extracted Claims

### Claim 1: The API now exposes a per-user flag showing whether editor telemetry arrived that day, with `false` meaning activity was seen server-side but no editor events arrived
- **Evidence**: Field definition in the changelog's "What's new" section.
- **Confidence**: settled
- **Quote**: "Whether client telemetry was received for the user that day. false means Copilot saw the user’s activity, but no usage events arrived from their editor."
- **Our assessment**: This is the per-user diagnostic that the June 15 server-side telemetry change lacked: previously server-side-only users were indistinguishable except by empty breakdowns. The flag is per user per day, so it can flicker for intermittently-blocked clients.

### Claim 2: Each user's IDEs and Copilot extensions are graded met / unmet / unknown against minimum supported versions
- **Evidence**: Field definition for `usage_metrics_requirements`.
- **Confidence**: settled
- **Quote**: "Lists each of the user’s IDEs and Copilot extensions as met, unmet, or unknown against the minimum supported versions."
- **Our assessment**: This is the API mechanism for the IDE version floors discussed after the October agent-attribution bug. It makes "who needs to upgrade" a query rather than a survey. The meaning of `unknown` is not defined; treat it as neither pass nor fail.

### Claim 3: Two daily counts quantify the affected population
- **Evidence**: Field definitions for `missing_client_telemetry_user_count` and `below_usage_metrics_minimum_user_count`.
- **Confidence**: settled
- **Quote**: "The number of users that day with at least one IDE or extension below the minimum version."
- **Our assessment**: Good for a coverage-health dashboard ("what share of active users are blind to us"). Counts are per day and, per the notes, only usable as daily snapshots.

### Claim 4: Users without client telemetry still count as active, but their reports lack detail
- **Evidence**: "Why this matters" section.
- **Confidence**: settled
- **Quote**: "Users without client telemetry still count as active, but their reports lack detail such as lines of code, feature breakdowns, and model breakdowns."
- **Our assessment**: Confirms the two-tier population described in the June note. Any per-feature or per-model analysis is computed on the telemetry-present subset and should be reported with that denominator.

### Claim 5: Common causes of missing telemetry are outdated editors/extensions, disabled IDE telemetry, and proxies/firewalls
- **Evidence**: Official enumeration; no frequency data.
- **Confidence**: settled (that these are causes); anecdotal on relative prevalence (none given)
- **Quote**: "Common causes include outdated editors or extensions, disabled IDE telemetry, and proxies or firewalls that block events."
- **Our assessment**: The three causes need different fixes (upgrade push, IDE settings policy, network allowlisting). The version signal only addresses the first, which motivates Claim 7.

### Claim 6: The fields let admins identify and follow up with affected users without a support ticket
- **Evidence**: Stated purpose.
- **Confidence**: settled (design intent)
- **Quote**: "These fields show how many users are affected and who to follow up with. This way you can close gaps without opening a support ticket."
- **Our assessment**: Shifts diagnosis to the customer side. It is user-identifying, so follow-up outreach should respect the org's privacy norms around per-user usage data.

### Claim 7: Version compliance and telemetry presence are independent signals
- **Evidence**: Explicit note.
- **Confidence**: settled
- **Quote**: "A user can meet every version minimum and still be missing telemetry (e.g., they’re behind a proxy)."
- **Our assessment**: Do not use `usage_metrics_requirements` alone as a proxy for coverage; cross-tabulate the two (met+present, met+absent, unmet+present, unmet+absent). The met+absent cell points to network/policy causes.

### Claim 8: The two daily counts overlap and neither may be summed across metrics or across days
- **Evidence**: "Daily counts" note.
- **Confidence**: settled
- **Quote**: "A user can be counted in both missing_client_telemetry_user_count and below_usage_metrics_minimum_user_count, so don’t add the two counts together. Don’t add counts across days to count unique users."
- **Our assessment**: A common pipeline error. For unique affected users over a window, compute from per-user rows (distinct user IDs) rather than from `day_totals`.

### Claim 9: Null or omitted means unavailable (not false/zero), and pre-release days have no values
- **Evidence**: "Unavailable values" note.
- **Confidence**: settled
- **Quote**: "Null or omitted values mean the data is unavailable, not false or zero. Days before this release have no values."
- **Our assessment**: Pipelines must keep a tri-state (true/false/null). Coercing null to false would overstate the missing-telemetry population for historical data; coercing to zero understates it. This is another series discontinuity (cf. June 15).

### Claim 10: Availability scope and access are restricted
- **Evidence**: "Scope" and "Access" notes.
- **Confidence**: settled
- **Quote**: "User fields appear in enterprise and organization user reports (1-day and 28-day). Counts appear in enterprise and organization 1-day reports and in each day_totals entry of 28-day reports."
- **Our assessment**: Access: enterprise owners, enterprise billing managers, organization owners, and custom roles with the `View Copilot Metrics` permission, and the Copilot usage metrics policy must be enabled. Because this is a permission-gated per-user view, team leads without the role cannot self-serve.

## Concrete Artifacts

```
# New fields, Copilot usage metrics API (GitHub changelog, Nov 5, 2026)
Per-user (enterprise + org user reports, 1-day and 28-day):
  client_telemetry_present        true | false | null
  usage_metrics_requirements      per IDE / Copilot extension: met | unmet | unknown
Daily counts (enterprise + org 1-day reports; each day_totals entry in 28-day reports):
  missing_client_telemetry_user_count      # users with client_telemetry_present == false
  below_usage_metrics_minimum_user_count   # users with >=1 IDE/extension below minimum
Rules: counts overlap (do not add); do not sum across days; null/omitted != false/0.
```

Derived (our suggestion, not from source) coverage matrix:

```
                       client_telemetry_present
                       true            false
all requirements met   healthy         proxy/firewall/telemetry disabled
any requirement unmet  upgrade soon    upgrade first, then recheck
```

## Cross-References

- **Extends**: `docs-github-copilot-usage-metrics-server-side-telemetry.md` (Claims 1, 2 and 4): that note established that client telemetry can fail and that server-side-only users appear with empty `totals_by_ide`/`totals_by_feature`. This source supplies the per-user flag and daily count that identify exactly those users, and reaffirms its "two-tier population" point (Claim 4 here).
- **Extends**: `docs-github-copilot-ide-agent-sdk-metrics-attribution-fix.md`: that note covers IDE version floors needed for agent attribution; `usage_metrics_requirements` is the API-level way to find users below those floors.
- **Corroborates**: `docs-github-copilot-usage-metrics-server-side-telemetry.md` on proxies/network conditions as a cause of missing telemetry (Claim 5 here).
- **Related**: `docs-github-copilot-usage-metrics-adoption-cohorts.md` and `docs-github-copilot-usage-metrics-agent-app-activity.md` (server-sourced vs client-emitted metrics). Open issue #4314 (OpenCode usage in the same API) is a separate change.
- **Contradicts**: none found. No contradiction issue filed.
- **Novel**: the field names `client_telemetry_present`, `usage_metrics_requirements`, `missing_client_telemetry_user_count`, `below_usage_metrics_minimum_user_count`; the tri-state null semantics; the explicit independence of version and telemetry signals; the no-summing rules.

## Guide Impact

- **Chapter 05 (Team Adoption), usage-metrics section**: where the June 15 server-side telemetry change is discussed, add that coverage can now be measured directly: report "% of active users with client telemetry" using `missing_client_telemetry_user_count` alongside DAU, and caveat all feature/model/LOC breakdowns with that denominator. Add the null-handling rule (null is unavailable, pre-Nov 5 data has no values) and the no-summing rule for the overlapping counts.
- **Chapter 05**: recommend an operational workflow: list users with `client_telemetry_present == false` and `unmet` requirements, push upgrades first, then investigate proxies/telemetry settings for those who remain absent. Frame these as measurement-quality fields, not productivity evidence.
- **Chapter 02 (Harness Engineering), observability**: use as an example of self-reporting data-quality flags in a telemetry pipeline (distinguish "zero" from "unknown").

## Extraction Notes

- Source is a short changelog; read in full via raw HTML (the WebFetch summarizer could not return verbatim text, so quotes were taken from the raw page text). No linked sub-pages followed (API docs and minimum-versions page not read).
- Quotes copied from the page text; smart apostrophes preserved.
- Claim 10's quote is the scope note; access details are paraphrased in the assessment, with the access sentence in the source reading as given on the page.
- Cross-referenced claim numbers refer to `docs-github-copilot-usage-metrics-server-side-telemetry.md` (Claims 1, 2, 4 verified) .
