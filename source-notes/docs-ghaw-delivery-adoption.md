---
source_url: https://github.github.com/gh-aw/reference/delivery-adoption
source_type: docs
title: "GitHub Agentic Workflows: Delivery and adoption"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-11-18
last_checked: 2026-11-18
status: current
confidence_overall: emerging
issue: "#4805"
---

# GitHub Agentic Workflows: Delivery and adoption

> First-party reference defining a measurement ledger that separates *delivery* (a safe-output effect was applied) from *adoption* (a rule-based decision about it), with an explicit evidence model: missing evidence is `unknown`, automated acceptance is flagged `human_verified: false`, and a 404 is never read as deletion.

## Source Context

- **Type**: docs (gh-aw `reference/delivery-adoption`, Reference section; a CLI-flavored page whose substance is a conceptual measurement model).
- **Author credibility**: First-party from the team that builds `gh aw`. Authoritative for the platform's behavior; the evidence-handling principles generalize, the CLI flags and limits are platform-specific. Undated; no production metrics are given.
- **Scope**: Delivery evidence, adoption states and rules, retention/refresh of a lifecycle ledger, how the gh-aw repo's own Metrics Collector runs it, and survival/attributed-value/cost caveats. Does not cover the type-by-type rule registry (lives in `pkg/lifecycle`) or the lifecycle spec (linked only).

## Extracted Claims

### Claim 1: Delivery and adoption are recorded as separate facts

- **Evidence**: Definitional statement at the top of the page; CLI exposes separate `--delivery` and `--adoption` reports (`--adoption` includes delivery).
- **Confidence**: emerging
- **Quote**: "Delivery records a successfully applied safe-output effect. Adoption records the"
- **Our assessment**: Counting "PRs opened by the agent" conflates the agent acting with a human keeping the result. Recording them separately is the mechanism-level version of the cost-vs-outcome split in `docs-ghaw-measuring-impact.md`. Quote is a verbatim line fragment; the rest of the sentence ("decision defined by that output type's versioned rule.") continues on the next line.

### Claim 2: Only successful handler results count as delivery; requests, previews, placeholders, skips and failures do not

- **Evidence**: Explicit rule list in "Delivery evidence".
- **Confidence**: emerging
- **Quote**: "Requests, staged previews, deferred placeholders, skipped actions, and failed"
- **Our assessment**: Makes concrete that staged-mode previews (see `docs-ghaw-staged-mode-reference.md`, Claim 1) are not deliveries. Also: "Successful handler results establish delivery even when another job fails" — delivery is per-effect, not per-run-success.

### Claim 3: Missing or malformed evidence is "unavailable or partial coverage", not a verified zero

- **Evidence**: Stated in Delivery evidence; echoed for adoption (`unknown`) and refresh ("A failed provider check preserves the previous decision with unavailable coverage").
- **Confidence**: emerging
- **Quote**: "unavailable or partial coverage, not a verified count of zero."
- **Our assessment**: Strong, reusable principle for any agent metrics pipeline: a dashboard showing 0 adopted outputs when collection failed is a false negative. Also notes "A recorded skipped safe-output job can establish zero deliveries" — zero must be positively evidenced.

### Claim 4: Six adoption states, with `unknown` and `lifecycle` distinguishing missing evidence and automated decisions from human ones

- **Evidence**: State table in "Adoption rules".
- **Confidence**: emerging
- **Quote**: "lifecycleAn observed automated decision is not a verified human decision."
- **Our assessment**: States are accepted, rejected, pending, lifecycle, not_applicable, unknown. This is a finer taxonomy than the six outcome states in `docs-ghaw-outcomes-reference.md` (Claim 4) and adds `unknown`/`lifecycle` handling. Table cells are rendered without separators in the page text; the quote is the verbatim cell text.

### Claim 5: A human-verified decision requires a non-bot, non-publisher actor with current repository authorization; unverifiable decisions stay unknown

- **Evidence**: "Adoption rules" prose for created issues/PRs: exact delivered resource plus authoritative decision timestamp required.
- **Confidence**: emerging
- **Quote**: "Current authorization does not prove historical authorization or reveal hidden"
- **Our assessment**: Notably candid about limits: authorization is checked at refresh time, so historical authorization and machine-user ownership can't be proven. The rule excludes "known bots and the publisher" — self-approval by the publishing identity doesn't count. Relevant to Ch03 verification: who accepted matters.

### Claim 6: Delivery-time "fallback" acceptance is permitted for some types but is flagged not-human and summarized separately

- **Evidence**: Rule text plus summary field split.
- **Confidence**: emerging
- **Quote**: "Summaries separate accepted_human from accepted_delivery_fallback."
- **Our assessment**: Records carry `acceptance_kind: "fallback_delivery"` and `human_verified: false`, "they are not human approvals". Prevents inflating acceptance rate with outputs (e.g. labels, comments) that have no review step. Directly corrects naive "acceptance rate" figures (`docs-ghaw-measuring-impact.md`, Claim 4).

### Claim 7: A 404 is lost visibility, not proof of deletion; provider errors are diagnostics, not rejections

- **Evidence**: Stated in Adoption rules; reinforced in refresh ("it does not fabricate rejection").
- **Confidence**: emerging
- **Quote**: "A 404 can mean lost visibility and does not prove that an object was deleted."
- **Our assessment**: Practical gotcha (private repos, token scope changes return 404). Rejection/reversal only comes from "a supported provider observation".

### Claim 8: Lifecycle ledger is retained with explicit bounds and merge semantics

- **Evidence**: Retention section.
- **Confidence**: emerging
- **Quote**: "Retention is 365 days from delivery, capped at 20,000 identities and 16 MiB;"
- **Our assessment**: Ledger in `lifecycle.jsonl`; repeated collection merges by delivery identity; "Replayed delivery cannot overwrite a later provider observation." Idempotent, monotone merge design is worth copying. Capacity errors are explicit rather than silent truncation.

### Claim 9: Adoption is re-observed on a schedule without re-downloading artifacts; deferral and coverage are surfaced

- **Evidence**: `gh aw logs --adoption --retained` mode; due after 24h; oldest first; `--count` bounds checks.
- **Confidence**: emerging
- **Quote**: "Supported records are due after"
- **Our assessment**: Full sentence continues "24 hours, or immediately if no provider check has been attempted." Adoption is a longitudinal measurement; "there is no built-in scheduling service", so the team must schedule it.

### Claim 10: Collection is bounded per execution and incomplete windows are never reported as complete

- **Evidence**: Repository collection section: five batches of at most 200 runs, 768 KiB new records, four-minute network budget per batch, at most 1,000 due deliveries per refresh.
- **Confidence**: emerging
- **Quote**: "Incomplete windows remain checkpointed rather than being reported as complete."
- **Our assessment**: Good pattern for deterministic pre-agent metrics collection. Also "Due does not guarantee a daily check; monitor deferred counts as the retained population grows" — admits the system can fall behind.

### Claim 11: Snapshot coverage describes the retained population and must not be mixed with recent-run cohort counts

- **Evidence**: Guidance for consumers of `metrics/lifecycle.json`.
- **Confidence**: emerging
- **Quote**: "must not be added to recent-run cohort counts."
- **Our assessment**: Warns against double-counting when joining two differently-scoped datasets. The first deployment also doesn't backfill older deliveries.

### Claim 12: "Survived once" is not "survived"; attributed value needs a defined measurement, attribution evidence and full-window survival

- **Evidence**: Survival/attributed value section.
- **Confidence**: emerging
- **Quote**: "It does not establish continuous survival across a measurement window."
- **Our assessment**: The page also states "Delivery counts, acceptance counts, label-derived weights, and an agent's claims are not attributed value." Strong anti-vanity-metric stance.

### Claim 13: cost_per_adopted_output is an efficiency ratio, not a value score, and is suppressed when inputs are incomplete

- **Evidence**: Final section.
- **Confidence**: emerging
- **Quote**: "It is an efficiency ratio, not a value score."
- **Our assessment**: Consistent with the anti-composite stance in `docs-ghaw-measuring-impact.md` Claim 1. Ratio is suppressed on "Missing cost, incomplete episode evidence, or zero adopted items" rather than showing misleading numbers.

## Concrete Artifacts

```
# Source: reference/delivery-adoption, "CLI reports"
gh aw logs weekly-research --delivery --json
gh aw logs weekly-research --adoption --json
gh aw audit https://github.com/owner/repo/actions/runs/123 --adoption --json
gh aw logs episode https://github.com/owner/repo/actions/runs/123 --adoption --json
```

```
# Source: "Refresh retained deliveries"
gh aw logs --adoption --retained --repo owner/repo \
  --output ./lifecycle-state --count 200 --timeout 2 --json
```

Adoption state table (source: "Adoption rules"): accepted (verified decision or explicit delivery-time fallback), rejected (supported provider observation of rejection/reversal), pending, lifecycle (observed automated decision, not verified human), not_applicable (infrastructure bookkeeping), unknown (evidence or supported rule missing).

Record markers (source: "Adoption rules"): `acceptance_kind: "fallback_delivery"`, `human_verified: false`, `survival.state: "observed"`, JSONL `kind: "output_lifecycle"`.

## Cross-References

- **Corroborates**: `docs-ghaw-measuring-impact.md` (Claim 1: don't collapse metrics into a single score; consistent with Claim 13 here). `docs-ghaw-outcomes-reference.md` (Claim 5: accepted outcomes as unweighted unit; Claim 11: declines to estimate business value).
- **Contradicts**: none found.
- **Extends**: `docs-ghaw-measuring-impact.md` Claim 4 (acceptance rate, time to adoption) — this page defines what "accepted" must mean evidentially and splits human vs fallback. `docs-ghaw-outcomes-reference.md` Claim 4 (six outcome states) and Claim 6 (varying acceptance coverage). `docs-ghaw-staged-mode-reference.md` Claim 1 (previews skip writes) — this page makes explicit that previews are not deliveries. `docs-ghaw-audit-reference.md` Claim 6 (`gh aw logs` cross-run reports) — adds `--delivery`/`--adoption` projections.
- **Novel**: fallback-vs-human acceptance split; `unknown` ≠ zero rule; 404-is-not-deletion; bot/publisher exclusion for human verification; bounded, checkpointed, idempotent lifecycle ledger; survival "observed once" vs continuous.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Where the guide recommends tracking acceptance rate, add that acceptance must distinguish human-verified decisions from automated/fallback ones, and that missing data should be reported as unknown, not zero (Claims 3, 6). Add a caution against equating delivery counts with value (Claim 12).
- **Chapter 03 (Verification)**: Add the idea that "output delivered" and "output accepted by an authorized non-bot human" are separate checkpoints, and that the publisher cannot be the verifier (Claim 5).
- **Chapter 04 (if it covers safe outputs/observability)**: Reference the bounded-collection and honest-coverage reporting pattern (Claim 10).

## Extraction Notes

- Page fetched via curl and read in full (HTML converted to text); no sub-pages followed since links (Measuring Impact, CLI reference, lifecycle spec) are covered by existing notes or not substantive here.
- Quotes are line-contiguous fragments of the page text; the page wraps lines, so some fragments end mid-sentence. Remainders are given in assessments where relevant.
- No production data or case studies; all claims are design/spec statements, hence `emerging`.
- No contradiction issue filed.
