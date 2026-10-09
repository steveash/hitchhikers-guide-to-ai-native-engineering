---
source_url: https://github.github.com/gh-aw/patterns/daily-report-portfolio
source_type: docs
title: "GitHub Agentic Workflows: Daily Report Portfolio Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-10-09
last_checked: 2026-10-09
status: current
confidence_overall: emerging
issue: "#4019"
---

# GitHub Agentic Workflows: Daily Report Portfolio Pattern

> A worked design for fanning ten scheduled report workflows through one dispatcher and the native `tools.work-queue` ledger: deterministic admission rotation, scheduler-chosen winners, claim-scoped publication, and an explicit list of what the design does not guarantee.

## Source Context

- **Type**: docs (first-party `patterns/` page in the gh-aw documentation; sibling of the Linter Factory example). The page carries no publication date.
- **Author credibility**: GitHub Next / Microsoft Research team that builds `gh aw`. Authoritative on the design intent, but the page itself says it is not a live deployment.
- **Scope**: Ten report workers, one dispatcher, planner/rotation rule, queue Policy parameters, MCP call shapes, worker frontmatter, ledger operations, diagnostics artifacts, failure/backlog handling, provisioning commands, pitfalls. Does not cover observed results, cost, or report quality; no metrics are given.

## Extracted Claims

### Claim 1: Ten independent scheduled reports can be converted to dispatch-only workers behind a single daily dispatcher that owns the only schedule
- **Evidence**: Roster table of ten worker sources; dispatcher frontmatter with the single `schedule: daily around 10:00` and a `dispatch-workflow` allowlist of all ten with `max: 3`. Design description, no runtime data.
- **Confidence**: emerging
- **Quote**: "The dispatcher source has the only portfolio schedule. The workers keep their engines, read tools, categories and report logic, but no longer have independent cron triggers."
- **Our assessment**: Credible, concrete consolidation of cron sprawl into one control point. Worth noting that reports lose their independent cadence; the trade (central fairness vs. per-report autonomy) is not discussed.

### Claim 2: Admission rotation is deterministic and gives every profile equal slots, but is separate from queue authority
- **Evidence**: Formula and code excerpt `reportsForDay(date)` in `daily_report_portfolio.cjs`; worked example for report date 2026-10-07 (token-consumption, compiler-quality, evals).
- **Confidence**: emerging
- **Quote**: "Every profile receives three admission slots in any ten consecutive days, including weekends."
- **Our assessment**: Arithmetic checks out (3 per day x 10 days = 30 slots over 10 profiles). Simple, auditable, reproducible; a stateless alternative to a mutable "last-run" cursor. Starting index is `(UTC epoch day * 3) % 10`.

### Claim 3: Admission is not launch: the native scheduler, not the planner or agent, picks winners from fresh queue state, so fewer than three launches (and fewer published reports) are normal outcomes
- **Evidence**: Policy table (`max_claims: 3`, `max_dispatches: 3` are ceilings; `logical_limit: 3`, `native_limit: 3` bound active reservations) and prompt instruction not to select winners from the snapshot.
- **Confidence**: emerging
- **Quote**: "Three launches do not guarantee three published Discussions."
- **Our assessment**: The key design lesson: a plan the agent produces is a request, not a grant. Guards against agents "helpfully" forcing the target count.

### Claim 4: The report date is derived from the original run's API `created_at`, not wall-clock or rerun time, so delayed launches analyze the same window
- **Evidence**: Trusted `actions/github-script` step computes `new Date(Date.parse(run.created_at) - 86400000)`; example: activation on October 8 gives report date October 7.
- **Confidence**: emerging
- **Quote**: "The planner derives the previous complete UTC report date from the original run's GitHub API created_at."
- **Our assessment**: Good determinism practice: time-dependent inputs are computed in trusted code and frozen into the Work payload. Same date, repo and repo ID yield identical nodes.

### Claim 5: The three-per-day rotation is not a queue-enforced daily quota; a `github.run_attempt == 1` gate and single trigger stop reruns from admitting extra cohorts
- **Evidence**: Dispatcher `if: github.run_attempt == 1`; prose on `native_limit`; pitfalls table row on `native_limit: 3`.
- **Confidence**: emerging
- **Quote**: "This is not a queue-enforced UTC-day quota: adding another trigger or dispatcher requires a new calendar-budget design."
- **Our assessment**: Honest about a real gap. The daily budget depends on convention (one trigger, attempt gate) rather than enforcement; a reader should not assume the queue caps per-day volume.

### Claim 6: Work identity is derived from `graph_id` + `node_key`; identical resubmission is idempotent and a changed payload is a conflict
- **Evidence**: Node JSON example (`graph_id: daily-report-cohort:2026-10-07`) and prose on ID derivation.
- **Confidence**: emerging
- **Quote**: "A changed payload under that identity is a conflict, not an update."
- **Our assessment**: Idempotency by construction, upgrading the check-before-act technique in `docs-ghaw-workqueue-ops.md` (Claim 8) to a runtime-enforced property. Nodes are independent graph roots (`depends_on: []`), so no report waits on another.

### Claim 7: Agent writes are staged intents, not state transitions; submit/dispatch acknowledgements are not Claims
- **Evidence**: Acknowledgement example `{"intent_id":"intent:example","status":"staged"}`; sequence diagram showing trusted runtime replaying the ledger and publishing via compare-and-swap.
- **Confidence**: emerging
- **Quote**: "That response is neither a Claim nor proof of a native launch."
- **Our assessment**: Consistent with the "finish is intent, not proof" rule in `docs-ghaw-deploy-work-queue.md` (Claim 9). The agent is a proposer; trusted code is the committer.

### Claim 8: Workers must consume exactly one original Claim, carry the claim handle on every output, and finish it; no-data runs finish `cancelled`
- **Evidence**: Worker frontmatter (`work-queue: worker: true, require-assignment: true`), worker prompt, and the `create_discussion` + `work_queue_claim_finish` call pair using handle `h1`.
- **Confidence**: emerging
- **Quote**: "If no qualifying report can be prepared, stage a scoped noop or report_incomplete and finish the Claim as cancelled instead."
- **Our assessment**: Gives a typed way to say "nothing to report" without counting it as delivery. Page also says to copy the handle, not `claim_id`/`work_id`, and never send an empty or foreign selector.

### Claim 9: Completion is not Result; delivery must be independently read back before Result is recorded
- **Evidence**: Ledger operation table (Policy, Work, Claim, Dispatch, Completion, Result, ClaimCancellation, Release) and sequence diagram with "Independently read back the contract".
- **Confidence**: emerging
- **Quote**: "Completion is not Result. An API success response or a native run's success conclusion is also not proof that the required Discussion exists."
- **Our assessment**: Strong verification principle applicable beyond gh-aw: success signals from the actor or the runner do not substitute for checking the artifact. Not validated by any reported incident.

### Claim 10: Ambiguous launches keep their reservation; the system will not release capacity to hit the target count of reports
- **Evidence**: Flowchart for backlog/unknown launch; pitfalls row "Releasing an ambiguous launch to reach three reportsRetain its reservation until exact native evidence permits release".
- **Confidence**: emerging
- **Quote**: "The reporting count is an operating target, never a reason to bypass queue authority or release an unknown native launch:"
- **Our assessment**: Prefers safety (possible duplicate/stuck capacity) over throughput. Also: operator cancellation neither stops a native run nor refunds Claim debt; a failed Discussion does not fall back to an issue.

### Claim 11: Per-claim diagnostics are audit exports, redacted, short-retention, and explicitly not scheduling authority
- **Evidence**: File table under `/tmp/gh-aw/claims/<original-identity-hash>/`, modes 0700/0600, default one-day retention, `GH_AW_DEFAULT_ARTIFACT_RETENTION_DAYS` override, stated redaction limits.
- **Confidence**: emerging
- **Quote**: "Redaction does not anonymize repository names, resource IDs or URLs, and cannot identify arbitrary personal data or unknown secrets."
- **Our assessment**: Useful candor about redaction limits. Also notes the redundant `delivery-receipt.json` was dropped in favor of ledger outcomes.

### Claim 12: Compiling the workflows does not make the example operational; an administrator must install Policy and verified immutable worker bindings
- **Evidence**: Caution block; provisioning commands (`policy` generator then `gh aw work-queue ... policy --file ... --epoch daily-reports-v1`); warning not to overwrite a shared queue's policy; pending nodes bounded at thirty.
- **Confidence**: emerging
- **Quote**: "The sources are an orchestration example, not an already provisioned live deployment."
- **Our assessment**: Critical caveat: all claims here are design claims. Nothing shows the pattern running at scale, so treat as documented intent. Matches the administrator-role split in `docs-ghaw-deploy-work-queue.md` (Claim 2, Claim 3).

## Concrete Artifacts

```js
// actions/setup/js/daily_report_portfolio.cjs (rotation excerpt) — source page
function reportsForDay(date) {
  const offset = (reportDay(date) * REPORTS_PER_DAY) % DAILY_REPORTS.length;
  return Array.from(
    { length: REPORTS_PER_DAY },
    (_, index) => DAILY_REPORTS[(offset + index) % DAILY_REPORTS.length]
  );
}
```

```
# Dispatcher prompt (.github/workflows/daily-report-dispatcher.md, excerpt) — source page
Read /tmp/gh-aw/agent/daily-report-plan.json.
Call work_queue_read with {"pool":"daily-reports","limit":32}.
Call work_queue_submit once with {"nodes": <the exact plan.nodes array>}.
Call work_queue_dispatch_next once with the exact plan.dispatch:
{"pool":"daily-reports","max_claims":3,"max_dispatches":3}.
Do not select winning Work IDs, workflows or revisions from the snapshot.
Do not call ordinary dispatch_workflow or target-specific dispatch tools.
```

```yaml
# Worker frontmatter (.github/workflows/daily-compiler-quality.md, excerpt) — source page
on:
  workflow_dispatch: null
imports:
  - shared/daily-report-worker.md
tools:
  work-queue:
    worker: true
    require-assignment: true
safe-outputs:
  create-discussion:
    category: audits
    title-prefix: "[daily-compiler-quality] "
    max: 1
    min-body-length: 200
    fallback-to-issue: false
```

```json
// Output + finish calls — source page
{"name": "create_discussion", "arguments": {"claim_handle": "h1", "title": "...", "body": "..."}}
{"name": "work_queue_claim_finish", "arguments": {"claim_handle":"h1","outcome":"completed"}}
```

Policy parameters (source table): priority 3; per-profile fairness key weight 1; `max_claims: 3, max_dispatches: 3`; `logical_limit: 3, native_limit: 3`; `max_attempts: 1`; pending nodes bounded at thirty.

Operator commands (source): `gh aw work-queue --repo OWNER/REPO state | tui | replay --json`.

## Cross-References

- **Corroborates**: `docs-ghaw-deploy-work-queue.md` — Claim 9 (finish is intent, not proof; Result requires verified delivery) ↔ Claim 7/9 here; Claim 5 (`require-assignment: true`, one Claim = one attempt) ↔ Claim 8 here; Claim 4 (dispatch allowlist is approval, not authorization) ↔ the prompt's ban on ordinary dispatch tools.
- **Contradicts**: None found. (The "no live deployment" caveat is a limitation, not a conflict.)
- **Extends**: `docs-ghaw-workqueue-ops.md` — Claim 8 (idempotency techniques) and Claim 9 (concurrency) now have a runtime-enforced realisation (identity from graph_id+node_key, compare-and-swap, reservation limits); `docs-ghaw-dailyops.md` — Claim 1 (scheduled daily automation) and Claim 4 (Discussions as output) scaled to ten workers with fair rotation; `docs-ghaw-orchestration-patterns.md` — Claim 1 (orchestrator/worker) and Claim 2 (`dispatch-workflow` fan-out up to 10 workers; this page uses exactly ten in the allowlist, with `max: 3` per run); `blog-ghaw-weekly-2026-10-05.md` — Claim 1 and Claim 2 (Git-backed work-queue operators, dispatching to trusted workers); `docs-ghaw-dispatch-ops.md` — workers keep `workflow_dispatch` but the manual path does not authorize effects (contrast with Claim 1 there).
- **Novel**: Stateless modular rotation for fair scheduling; admission-vs-launch separation with explicit non-guarantees; report windows frozen from the original run's `created_at`; the cancelled-finish convention for no-data runs; retention of ambiguous reservations rather than meeting a count target. Sibling example referenced: `blog-ghaw-custom-linters-three-workflow-loop.md` (Linter Factory; the page says it covers multi-Claim batching while this one uses singleton profiles).

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add the portfolio as the scaled form of scheduled reports: one dispatcher, dispatch-only workers, date-pinned windows. Cite `docs-ghaw-dailyops.md` for the base pattern and this note (Claims 1, 2, 4).
- **Chapter 02 (Harness Engineering)**: Add "plan ≠ grant": the agent submits and requests, the trusted scheduler decides (Claims 3, 7, 10). Include the caveat that daily volume is convention-bound, not enforced (Claim 5).
- **Chapter 03 (Verification)**: Cite Claim 9 as the clearest statement that actor success and runner success are not evidence of delivery; require independent readback.
- **Chapter 05 (Team Adoption)**: Note that org-level fair-share needs an administrator-installed Policy and quiescence before merging into shared queues (Claim 12).
- All of the above must be labelled design intent, not observed production results.

## Extraction Notes

- Fetched raw HTML with curl and read the full rendered text, including code excerpts, tables and mermaid diagrams. Quotes were copied from that text.
- Did not follow linked pages (Linter Factory, operator reference, policy generator); no claims made about them beyond what this page states.
- No dates, metrics, or incident reports on the page; every claim is graded `emerging` at best.
- Cross-referenced claim numbers verified against the `### Claim` headings of the cited notes.
