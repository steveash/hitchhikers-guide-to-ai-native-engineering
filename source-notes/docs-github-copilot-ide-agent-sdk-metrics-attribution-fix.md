---
source_url: https://github.blog/changelog/2026-10-06-update-your-ide-to-restore-agent-activity-in-copilot-usage-metrics
source_type: docs
title: "Update your IDE to restore agent activity in Copilot usage metrics"
author: GitHub (official changelog)
date_published: 2026-10-06
date_extracted: 2026-10-07
last_checked: 2026-10-07
status: current
confidence_overall: settled
issue: "#3947"
---

# Update Your IDE to Restore Agent Activity in Copilot Usage Metrics (GitHub Changelog, Oct 6, 2026)

> GitHub discloses that moving IDE agent sessions to the Copilot SDK silently broke attribution in Copilot usage metrics (agent activity dropped or was miscounted as CLI), that the fix is client-side and per-IDE, and that lost data cannot be backfilled — a concrete case study in how harness refactors create measurement gaps.

## Source Context

- **Type**: docs (GitHub official product changelog, short announcement, Oct 6, 2026)
- **Author credibility**: GitHub's own team, authoritative on what broke and the remediation. It gives no magnitude of the undercount and no root-cause detail beyond the missing IDE identifier.
- **Scope**: Covers the symptom (agent activity/agent lines of code falling while usage grew), cause (SDK-hosted agent sessions not identifying the source IDE), fix (IDE updates, VS Code first, others by November 2026), and limits (no backfill, billing unaffected, gradual recovery). Does NOT cover: how much data was lost, the affected date range, or exact field names in the API.

## Extracted Claims

### Claim 1: Agent activity metrics fell in reports while real Copilot usage grew, because of an attribution bug rather than declining usage
- **Evidence**: Official GitHub statement that the cause was found.
- **Confidence**: settled
- **Quote**: "If your Copilot usage metrics have shown agent activity or agent lines of code falling while Copilot usage kept growing, we've found the cause, and a fix is rolling out to each IDE."
- **Our assessment**: Declining agent metrics alongside rising total usage is the diagnostic signature. Teams that saw this and reported "agent adoption dropping" upward should re-check; the drop was a measurement artifact.

### Claim 2: Root cause was a refactor — IDEs moved agent sessions onto the Copilot SDK, and the sessions did not carry IDE identity
- **Evidence**: GitHub's explanation of the cause.
- **Confidence**: settled
- **Quote**: "Those sessions didn't identify which IDE they came from, so usage metrics couldn't attribute them correctly."
- **Our assessment**: Telemetry identity (which client produced this) was implicit in the old in-IDE code path and was lost when the runtime was swapped for a shared SDK. Generalizable: when consolidating onto a shared agent runtime, client/surface identity must be passed explicitly.

### Claim 3: Affected activity was mostly dropped, and some was misattributed to Copilot CLI
- **Evidence**: GitHub statement; no volumes given.
- **Confidence**: settled (that it happened); anecdotal on scale (none disclosed)
- **Quote**: "Most of that activity was left out of reports, and some was counted as Copilot CLI activity."
- **Our assessment**: Two failure modes at once: undercounting one surface and inflating another. CLI metrics for the affected period may be overstated, which matters for anyone comparing CLI vs IDE agent adoption.

### Claim 4: The fix ships client-side, per IDE; VS Code first, others through November 2026
- **Evidence**: Changelog rollout statement. The fetched summary also listed specific minimum versions (VS Code 1.139.0+, Visual Studio 18.12, JetBrains late Oct, Eclipse and Xcode Nov); those version numbers were not seen in a verbatim-quote pass, so treat them as unverified detail.
- **Confidence**: settled
- **Quote**: "Other IDEs will receive it in upcoming releases, which we expect to finish rolling out by November 2026."
- **Our assessment**: Server-side reports cannot fix this; correctness depends on endpoint fleet update cadence. Organizations with pinned or slow-updating IDE fleets will have persistent gaps.

### Claim 5: Data cannot be backfilled, and recovery is gradual
- **Evidence**: GitHub's explanation that the missing field makes retroactive attribution impossible.
- **Confidence**: settled
- **Quote**: "We can't backfill missing data."
- **Our assessment**: Creates a permanent hole in the time series. Related: "Expect a gradual recovery as developers move to these versions rather than a single jump." Trend charts will show a slow ramp that looks like organic adoption growth but is recovery.

### Claim 6: Billing is unaffected; only metrics attribution changed
- **Evidence**: Explicit statement.
- **Confidence**: settled
- **Quote**: "This issue only changed how agent activity was attributed in usage metrics, not what you were charged."
- **Our assessment**: Billing/metrics divergence widened during the affected period; consistent with the three-number reconciliation model in the June 15 note.

### Claim 7: The gap persists per developer until that developer updates
- **Evidence**: GitHub statement.
- **Confidence**: settled
- **Quote**: "The gap persists for any developer on an affected IDE version until they update."
- **Our assessment**: Actionable: track IDE version distribution (the fetched summary also advised monitoring user versions in reports and keeping telemetry enabled, but that wording was not verified verbatim).

## Concrete Artifacts

```
# Failure chain (synthesized from changelog, Oct 6, 2026)
IDE agent sessions -> moved to Copilot SDK
  -> sessions lack source-IDE identifier
  -> metrics pipeline cannot attribute
  -> agent activity omitted ("most") or counted as Copilot CLI ("some")
Remediation: IDE updates (client-side); no backfill; billing unaffected
```

## Cross-References

- **Extends**: `docs-github-copilot-usage-metrics-server-side-telemetry.md` (June 15, 2026) — that note covers client telemetry gaps from network/proxy; this is a distinct, GitHub-caused client telemetry gap from an SDK migration. Its Claim 1 ("client-side telemetry ... does not always reach us") gains a second failure class: telemetry that arrives but is unattributable.
- **Extends**: `docs-github-copilot-cli-activity-usage-metrics.md` Claim 1 (CLI activity integrated into top-level totals) — misattributed agent sessions inflated CLI counts in that integrated view.
- **Extends**: `docs-github-copilot-usage-metrics-agent-app-activity.md` Claim 11 (per-agent metrics sourced server-side rather than client telemetry) — contrast: IDE agent activity depends on client-emitted identity.
- **Corroborates**: `docs-ghaw-copilot-sdk-driver-specification.md` and `docs-github-copilot-cli-sdk-session-credit-limits.md` — the Copilot SDK is becoming the shared runtime under multiple surfaces, which is why one SDK change affected many IDEs.
- **Contradicts**: none found.
- **Novel**: A first-party admission that an agent-runtime refactor corrupted adoption metrics, with unrecoverable data and fleet-update-dependent recovery.

## Guide Impact

- **Chapter 05 (Measurement)**: Add a caveat that Copilot agent-activity metrics for roughly the period of the SDK migration up to ~November 2026 are undercounted and non-backfillable; dips in agent activity concurrent with rising total usage should be treated as artifacts. Cite this note with the June 15 note as a second time-series discontinuity.
- **Chapter 02 (Harness Engineering — Observability)**: Add the lesson that migrating to a shared agent runtime/SDK must preserve surface/client identity in telemetry; recommend a sanity check (per-surface totals vs overall usage trend) after such migrations.

## Extraction Notes

- Source is a short changelog; no sub-pages followed. Two fetch passes were made; quotes above come from the pass that returned sentence-level blockquotes. The first pass returned a summary with version numbers and a "why metrics vary" paragraph that did not appear in the second pass, so those details are flagged as unverified and not quoted.
- Chapter citations are by chapter name as in the Prospector triage.
