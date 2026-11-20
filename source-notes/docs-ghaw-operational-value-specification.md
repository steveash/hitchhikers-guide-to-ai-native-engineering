---
source_url: https://github.github.com/gh-aw/specs/operational-value-specification
source_type: docs
title: "GitHub Agentic Workflows: Operational Value Report Specification"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-11-20
last_checked: 2026-11-20
status: current
confidence_overall: emerging
issue: "#4863"
---

# GitHub Agentic Workflows: Operational Value Report Specification

> A formal measurement contract (v1.0.0, Experimental, report schema 1) for `gh aw value`: how a team may claim that an agentic workflow produced value, with strict attribution gates (human acceptance, first-parent whole-PR boundary, durability windows) and anti-inflation rules (unknown is not zero, never aggregate grades, no causal inference from correlation).

## Source Context

- **Type**: docs (first-party formal spec; header reads "Version: 1.0.0 · Feature status: Experimental · Report schema: 1"; page shows no publication date)
- **Author credibility**: GitHub Next & Microsoft Research, authors of gh-aw. Authoritative for what the tool does; the spec is design-by-the-vendor, with no reported field results.
- **Scope**: The report side of value measurement: evidence matching, clocks, attribution, replay and resource limits. It consumes grades produced by the `operational-value` grader (see `docs-ghaw-graders.md`) and adoption data (see `docs-ghaw-delivery-adoption.md`). It does not report any measured results, and defers CLI inputs to a separate reference. The page is short (~4 dense paragraphs per section); all substantive rules are extracted below.

## Extracted Claims

### Claim 1: Value measurement separates five distinct layers, and a workflow is a reporting dimension rather than the unit of measurement
- **Evidence**: Normative design statement in the "Measurement contract" section; no empirical backing.
- **Confidence**: emerging
- **Quote**: "gh aw value separates delivery, adoption, recorded run grades, independently measured outcomes, and attributed value. A workflow is a reporting dimension, not the unit of measurement."
- **Our assessment**: Sound and consistent with the corpus's layered-metrics advice. The unit-of-measurement point is useful: the unit is a subject (e.g., a PR) with its own eligibility, not "the workflow".

### Claim 2: The owner must fix one primary metric and its full measurement definition before adoption
- **Evidence**: Enumerated list of what must be fixed: native unit, eligible population, independent producer, formula, direction, baseline, sampling, lag, durability, overlap, missing-data rules.
- **Confidence**: emerging
- **Quote**: "The owner chooses one primary metric in its native unit and fixes its eligible population, independent producer, formula, direction, baseline, sampling, lag, durability, overlap and missing-data rules."
- **Our assessment**: Pre-registration discipline applied to agent ROI. Most teams skip this, which is how post-hoc metric shopping happens. The "independent producer" requirement (the metric must not come from the agent itself) is the key piece.

### Claim 3: Prospective designs must be frozen before adoption with no target results in the design context; post-hoc designs must be labelled retrospective
- **Evidence**: Normative rules; also states a digest only identifies inputs.
- **Confidence**: emerging
- **Quote**: "For prospective use, freeze the definition, recipe and semantic fixtures before adoption, with no target results or adoption decisions in the design context."
- **Our assessment**: Strong guardrail against the designer (human or LLM) tuning the metric to observed outcomes. The honest limitation is stated too (next claim).

### Claim 4: Rules apply uniformly to all eligible subjects including negatives, and a digest is not proof of blindness, timing or causality
- **Evidence**: Normative statement.
- **Confidence**: emerging
- **Quote**: "A digest identifies the inputs; it does not certify blindness, timing or causality. Label post-hoc designs retrospective."
- **Our assessment**: Good epistemic humility: tamper-evidence of inputs is not evidence of an unbiased design. Preceded by "Apply the same rules afterward to all eligible subjects, including negative outcomes." (no cherry-picking of wins).

### Claim 5: Execution or a delivery fallback is not explicit human acceptance, and effects are matched by host, repository, workflow path and delivery time
- **Evidence**: Normative matching rule in "Evidence and clocks".
- **Confidence**: emerging
- **Quote**: "Match native lifecycle effects by host, repository, workflow path and delivery time. A later GitHub decision can be observed after the report cutoff. Execution or a delivery fallback is not explicit human acceptance."
- **Our assessment**: Separates "the agent ran / the output auto-landed" from "a human chose it". Directly extends the fallback-flagging in delivery-adoption (Claim 6 there).

### Claim 6: Missing item records do not prove zero deliveries
- **Evidence**: Normative rule, explicitly including the case where a run summary records a no-op.
- **Confidence**: emerging
- **Quote**: "Missing item records do not prove zero deliveries, even when a separate run summary records a no-op."
- **Our assessment**: Absence of a record is absence of evidence. Matches delivery-adoption Claim 3 (unavailable is not verified zero).

### Claim 7: Only the recorded primary operational-value grade of a matching completed run/attempt is read; zero, unavailable and error are preserved; grades are never aggregated into an outcome
- **Evidence**: Normative rule; custom grader execution is assigned to the grader job, not the report.
- **Confidence**: emerging
- **Quote**: "Preserve zero, unavailable and error; never aggregate grades into an outcome or rewrite a session."
- **Our assessment**: The report is a consumer, not a re-grader — keeps the evaluator and reporter independent. Grade selection is by creation time among matching completed run attempts ("selected by creation time").

### Claim 8: Changed context, missing samples or insufficient coverage cannot establish improvement; imported values never establish native adoption, full-window surveillance, or attributed value
- **Evidence**: Normative rules for typed observations (caller-supplied references, event and observation clocks, subject IDs, raw values; clock rule at ≤ observed_at ≤ report collection).
- **Confidence**: emerging
- **Quote**: "Changed context/population, missing samples or insufficient coverage cannot establish improvement. Imported values never establish native adoption, full-window surveillance, or attributed value."
- **Our assessment**: Provenance hierarchy: natively observed lifecycle data outranks externally imported numbers. Worth teaching: external dashboards can describe but not attribute.

### Claim 9: Daily rows end at noon UTC, count distinct human-accepted effects, and a positive count is only a lower bound; no decision means unknown
- **Evidence**: Precise window definition: decision time in (previous noon, this noon]; the baseline includes only decisions exactly at the start instant.
- **Confidence**: emerging
- **Quote**: "A positive count is a lower bound. No matching decision is unknown, not a certified zero. Do not interpolate sparse observations or infer a causal association."
- **Our assessment**: Notable because decisions can arrive after the cutoff, so every count is provisional upward. The specific noon-UTC choice is an implementation detail; the lower-bound/unknown semantics are the transferable idea.

### Claim 10: Attribution requires a native delivered `create_pull_request` effect, explicit-human adoption verified by GitHub at the exact merge time
- **Evidence**: Normative gate in "Attribution".
- **Confidence**: emerging
- **Quote**: "Require one matching native delivered create_pull_request effect for the producer-linked PR, its canonical URL and run. Adoption must be available, explicit_human, verified by GitHub at the exact merge time."
- **Our assessment**: A very strict gate — only PRs can carry attributed value, and only if a human merged them. Conservative by design, and it intentionally undercounts (see Claim 14). Non-PR effects "retain native lifecycle observations but cannot contribute to this subtotal."

### Claim 11: The whole-PR boundary must be proven on first-parent main history; otherwise return `whole_pr_boundary_unverified` rather than measuring the last commit
- **Evidence**: Rule distinguishes two-parent merges (first parent), single-commit linear merges (parent), and ambiguous multi-commit linear tips that may be squash or rebase.
- **Confidence**: emerging
- **Quote**: "Without proof of its full boundary, return whole_pr_boundary_unverified; do not measure only the final commit or infer its changed files."
- **Our assessment**: Real and subtle failure mode: squash/rebase merges hide PR boundaries, so naive before/after measurement silently measures the wrong diff. Refusing to answer is the correct behavior. Also: "Use the same verified boundary for measurement, changed-file isolation and survival."

### Claim 12: Credit requires comparable populations, sample minima, a mature window and untouched changed files through durability; later aggregate changes without subject linkage are descriptive only
- **Evidence**: Normative list of gates.
- **Confidence**: emerging
- **Quote**: "Require comparable populations, sample minima, a mature outcome/durability/isolation window, and untouched changed files through durability. A later aggregate change without subject linkage remains descriptive."
- **Our assessment**: The "untouched changed files" isolation rule avoids crediting an agent for code later reworked by someone else. Complements delivery-adoption Claim 12 ("survived once" is not "survived").

### Claim 13: Pending vs unavailable vs zero are distinct states; verified zero stays zero; only qualifying individual windows are summed
- **Evidence**: Reporting rules with `windows[].reason` and `attributed_value: null`.
- **Confidence**: emerging
- **Quote**: "An incomplete follow-up is pending; a missing gate is unavailable. A verified zero stays zero. Sum only qualifying individual windows; attributed_value: null means none qualified."
- **Our assessment**: Three-way (plus null) result semantics prevent both inflation (counting pending as success) and deflation (treating unmeasured as failure). Caveat from source: "Complete coverage refers to this report's windows, not the workflow's entire history."

### Claim 14: Elapsed time, survival of files and temporal correlation alone do not prove causation; replay retains evaluator version, digests, SHAs, run IDs and native exports
- **Evidence**: "Replay and limits" section; replay never fetches Git history, dispatches workflows, mutates records or executes repository code, though it still reads live PR metadata.
- **Confidence**: emerging
- **Quote**: "Elapsed time, survival of files and temporal correlation alone do not prove the workflow caused an outcome."
- **Our assessment**: Honest ceiling on what this report can show: "attributed" means passed gates, not proven causal. Teams should read attributed value as conservative evidence, not an ROI proof.

### Claim 15: The report fails rather than truncates when evidence limits are exceeded
- **Evidence**: Explicit numeric bounds (512 KiB definitions/recipes/bundles, 1,024 observations, 50 MiB grade summaries, 16 MiB / 20,000-item lifecycle cache, 8 MiB stdout / 16 KiB stderr per subprocess, 32 MiB evidence budget, 1,000-result search cap).
- **Confidence**: emerging
- **Quote**: "exceeding a limit fails the report rather than truncating evidence."
- **Our assessment**: Fail-closed evidence handling is a good pattern for measurement tooling; also "it is not a journal" — the lifecycle cache is bounded and prunes, so it is not a durable audit record.

## Concrete Artifacts

Report result vocabulary (source: "Attribution" section, verbatim identifiers):

```
whole_pr_boundary_unverified     # reason when full PR boundary cannot be proven
windows[].reason                 # reported when proof is absent
pending                          # incomplete follow-up
unavailable                      # missing gate
attributed_value: null           # no window qualified
adoption: available + explicit_human, verified by GitHub at exact merge time
```

Header metadata (source): `Version: 1.0.0 · Feature status: Experimental · Report schema: 1`

Daily window rule (source): decisions in (previous noon UTC, this noon UTC]; baseline includes only decisions exactly at the start instant.

## Cross-References

- **Corroborates**: `docs-ghaw-delivery-adoption.md` Claim 3 (missing evidence is unavailable, not verified zero), Claim 6 (fallback acceptance flagged as not human), and Claim 12 (survived once is not survived); `docs-ghaw-measuring-impact.md` Claim 1 (don't collapse signals into one score) and Claim 5 (layered metrics).
- **Contradicts**: None found.
- **Extends**: `docs-ghaw-graders.md` (the `operational-value` grader, Claim 6 there, produces the grades this report reads without aggregating); `docs-ghaw-outcomes-reference.md` Claim 11 (outcomes framework declines to estimate business value) — this spec defines the stricter attribution gates for when value is claimed anyway; `docs-ghaw-measuring-impact.md` Claim 8 (outcome metrics).
- **Novel**: Whole-PR boundary proof on first-parent history with `whole_pr_boundary_unverified`; pending/unavailable/zero semantics for attribution windows; pre-adoption freezing and "retrospective" labelling; lower-bound daily counts with noon-UTC windows; imported values cannot establish attributed value; fail-rather-than-truncate evidence limits.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Add a "measurement contract" checklist for claiming agent ROI: pick one primary metric with fixed population, baseline, lag and durability before rollout; label after-the-fact designs retrospective (Claims 2–4).
- **Chapter 03 (Verification)**: Add anti-inflation rules: unknown ≠ zero, pending ≠ unavailable, never sum grades into outcomes, correlation/survival ≠ causation (Claims 6, 9, 13, 14). Add the squash/rebase warning: do not measure only a PR's final commit (Claim 11).
- **Chapter 05**: Note that only human-accepted, merge-verified PRs should count toward attributed value; auto-landed or fallback output must not (Claims 5, 10).

## Extraction Notes

- Read the full page (≈10 KB of text; no sub-pages followed — the CLI reference is the only linked detail and was out of scope). The source is a concise spec, so claims are dense; claim count reflects its actual sections.
- Overlap with existing gh-aw notes is topical; the attribution-window and whole-PR-boundary rules are the incremental contribution.
- No publication date on the page; recency inferred from the surrounding 2026-era gh-aw docs. Feature is Experimental and no field evidence is presented, hence `confidence_overall: emerging`.
