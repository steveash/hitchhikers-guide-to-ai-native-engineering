---
source_url: https://github.github.com/gh-aw/blog/2026-11-23-agent-of-the-day/
source_type: failure-report
title: "Agent of the Day – November 23, 2026: API Consumption Report (five runs that spent tokens and never emitted a terminal safe output)"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-11-23
date_extracted: 2026-11-24
last_checked: 2026-11-24
status: current
confidence_overall: anecdotal
issue: "#4921"
---

# Agent of the Day – November 23, 2026: API Consumption Report

> A first-party failure profile of a daily Codex-engine workflow whose five consecutive runs spent 49k–412k tokens yet ended `missing_terminal_safe_output`, with a hypothesized declared-vs-prompted safe-output mismatch; useful as a checkable failure pattern, but the diagnosis is explicitly unconfirmed.

## Source Context

- **Type**: failure-report (first-party gh-aw "Agent of the Day" blog post, bylined "Copilot"; filed as `documentation` but is a dated blog post). Narrated by a fictional "Tally" bookkeeper persona, which is framing, not evidence.
- **Author credibility**: Official gh-aw blog. Five run IDs and per-run token/AIC/duration figures are cited, so they are checkable in principle; not independently verified here.
- **Scope**: One workflow (`.github/workflows/api-consumption-report.md`), one five-row run table, the audit state of the latest run, a hypothesized cause, and a suggested fix. It does NOT show the workflow's frontmatter or prompt, any session transcript, the actual tool-call errors, or a confirmed/applied fix.

## Extracted Claims

### Claim 1: Five consecutive scheduled runs spent real tokens and all recorded a failed conclusion
- **Evidence**: Five-row table with run IDs (see Concrete Artifacts).
- **Confidence**: anecdotal (vendor-reported, checkable run IDs)
- **Quote**: "Each run spent real tokens and recorded a failed conclusion:"
- **Our assessment**: A concrete cost-of-silent-failure data point: failed runs are not free. Our arithmetic from the table: 210,831 + 49,117 + 412,148 + 177,633 + 222,439 = 1,072,168 tokens and 9.28 + 4.85 + 17.53 + 8.10 + 8.59 = 48.35 AIC over five days with zero delivered output. The failure persisted at least five days with no visible intervention, which is itself a finding about unattended scheduled agents.

### Claim 2: The failure is at the handoff, not the analysis: the agent job succeeded but the conclusion job failed
- **Evidence**: Audit of the latest run (45158707380).
- **Confidence**: anecdotal
- **Quote**: "The conclusion job failed on its “Handle agent failure” step."
- **Our assessment**: Notable that the agent, detection and safe-output jobs are all green while the run is red; the pipeline's final step is what enforces "an outcome must be recorded." This is the harness acting as a verifier of the agent's output contract, not of its work quality.

### Claim 3: Every run reports the same incomplete state, `missing_terminal_safe_output`, with zero safe-output items and calls
- **Evidence**: Audits of all five runs.
- **Confidence**: anecdotal
- **Quote**: "Across all five runs, the audits count zero safe-output items and zero safe-output calls. The agent did its analysis and then never recorded an outcome."
- **Our assessment**: Defines a distinct failure class: "work done, no declared terminal outcome." Distinct from the zero-token auth/config failures and the `report_incomplete` epistemic signal in existing notes (see Cross-References). A run must end in exactly one recognised terminal output; silence is a failure, not a no-op.

### Claim 4: Likely cause is a mismatch between the declared safe outputs (frontmatter) and the outputs the prompt instructs
- **Evidence**: Author's reading of the workflow definition. Frontmatter declares only `upload-asset`; prompt says to finish with `create_discussion`, `report_incomplete`, or `noop`.
- **Confidence**: anecdotal (explicitly a hypothesis)
- **Quote**: "Its frontmatter declares only the upload-asset safe output, but the prompt tells the agent to finish with create_discussion, report_incomplete, or noop."
- **Our assessment**: Plausible and cheaply checkable (diff the prompt's named outputs against the frontmatter's declared set), which makes it a good lint candidate. But note the oddity: if `noop` and `report_incomplete` were unavailable, the agent had no legal way to end the run at all. Whether the runtime auto-exposes `noop`/`report_incomplete` is not stated here; see `docs-ghaw-custom-safe-outputs.md`.

### Claim 5: The author did not confirm the diagnosis and says what confirming it would take
- **Evidence**: Author's own caveat.
- **Confidence**: settled (the caveat itself); the diagnosis stays unconfirmed
- **Quote**: "This is a hypothesis, not a confirmed diagnosis. Confirming it would mean reading the session transcript for the failed calls, which this post does not do."
- **Our assessment**: Honest, and it caps how much weight the cause can bear. Treat the mismatch as a candidate, not a finding. The post also says "An agent that follows the prompt may be calling tools the runtime never exposed" (hedged with "may"), so even the failed-call mechanism is unobserved.

### Claim 6: The audit's own error list misclassifies success output as `agent_failure`; the `incomplete` field is the reliable signal
- **Evidence**: Author's observation about the audit report format.
- **Confidence**: anecdotal
- **Quote**: "The audit’s error list classifies the agent’s own success output as an agent_failure. The incomplete field is the more reliable signal, and it points at the handoff, not at the analysis."
- **Our assessment**: A practical warning for anyone building on audit output: prefer the structured state field over free-form error classification. Consistent with earlier gh-aw notes where auditor flags fire on successful runs (2026-11-20 note, Claim 5).

### Claim 7: No downstream artifact exists, so run links are the only evidence
- **Evidence**: Author's statement.
- **Confidence**: anecdotal
- **Quote**: "Nothing in the audit shows the workflow filing an issue or pull request, so the run links above are the only evidence."
- **Our assessment**: The consumer-visible symptom is silence: no report, no issue. Without the audit, nobody would know the daily report had stopped arriving. Argues for a missing-output alert (expected cadence vs. delivered output), which the post does not propose.

### Claim 8: Suggested fix is small: align declared outputs with the prompt
- **Evidence**: Author's recommendation; not applied or tested in the post.
- **Confidence**: anecdotal (untested advice)
- **Quote**: "The fix would be a small one: align the declared safe outputs with the prompt, or update the prompt to use only what the workflow declares."
- **Our assessment**: Sensible single-source-of-truth principle for the output contract. Untested: the post reports no post-fix run. Also notes that a workflow can fail five days running before anyone aligns the two.

### Claim 9: Spotlight selection requires live token-spending runs as "trustworthy evidence"
- **Evidence**: Description of the rotation rule.
- **Confidence**: anecdotal
- **Quote**: "Earlier candidates in the rotation were skipped because their recent runs had no trustworthy evidence, either because they hadn’t run recently or because their runs failed without spending tokens."
- **Our assessment**: Same editorial rule as the 2026-11-17 and 2026-11-20 notes. Selection bias consequence: this series over-represents workflows with token-spending runs, and zero-token failures (usually config/auth) are systematically excluded from its failure picture.

## Concrete Artifacts

Run table from the post (vendor-reported; all five runs ended with a failed conclusion and audit state `missing_terminal_safe_output`):

```
Date (UTC)   Tokens    AIC     Duration   Run
2026-11-23   210,831   9.28    14.7 min   45158707380
2026-11-22    49,117   4.85     7.5 min   45013835996
2026-11-21   412,148   17.53   12.3 min   44895710558
2026-11-20   177,633   8.10    10.9 min   44721677578
2026-11-19   222,439   8.59    10.0 min   44508344832
```

Failure signature (post's wording, latest run): agent job, detection job and safe-output jobs succeeded; conclusion job failed at step "Handle agent failure"; audit state `missing_terminal_safe_output`; zero safe-output items; zero safe-output calls.

Hypothesized misconfiguration (per post, unconfirmed; actual files not shown):

```
frontmatter safe outputs declared:  upload-asset
prompt instructs final output via:  create_discussion | report_incomplete | noop
```

## Cross-References

- **Corroborates**: `blog-ghaw-agent-of-the-day-2026-11-20.md` (Claim 4: judge runs by cost, not just pass/fail, applies here, and failed runs hide cost entirely; Claim 5: auditor flags are unreliable as labels; Claim 11: same selection rule for trustworthy evidence). `blog-ghaw-weekly-2026-04-06.md` (Claim 10: zero-token 100% failure rates indicate auth/config failure; this case is the opposite, token-spending failure).
- **Contradicts**: none found. No claim materially opposes an existing note, so no contradiction issue was filed.
- **Extends**: `blog-ghaw-weekly-2026-04-06.md` (Claim 4: `report_incomplete` as a first-class signal; here the agent apparently could not emit it, so the signal path itself is a failure point). `blog-ghaw-agent-of-the-day-2026-09-28.md` (Claim 2: restricting writes to safe outputs; this shows the cost of that restriction when the declared set and the prompt diverge). `docs-ghaw-custom-safe-outputs.md` and `docs-ghaw-threat-detection.md` (safe-output declaration and job pipeline context).
- **Novel**: The `missing_terminal_safe_output` failure state; the declared-vs-prompted safe-output mismatch as a lintable pattern; the audit's `agent_failure` vs `incomplete` quirk; a five-day token-burning silent failure (~1.07M tokens, 48.35 AIC by our sum).

## Guide Impact

- **Chapter 02**: Add a harness-design note (anecdotal, vendor-reported): keep the prompt's instructed terminal outputs and the declared output surface in one source of truth, and lint for divergence. Cite as an unconfirmed hypothesis, not a confirmed root cause.
- **Chapter 03**: Add as a failure example for verification/observability: a run can complete its analysis and still deliver nothing; check a run-state field (`incomplete`) rather than free-form error labels, and alert on missing expected output for scheduled agents.
- **Chapter 05**: Optional cost note: failing runs spent 49k–412k tokens each; cost dashboards should include failed runs.
- **Chapter 06**: Weak relevance only (tool exposure limited to what the runtime declares); the post makes no security claim, so do not cite for the threat model beyond that.

## Extraction Notes

- Fetched raw HTML and stripped tags to copy quotes verbatim (curly quotes/apostrophes preserved as in the source). No sub-pages followed; the post links only to the gh-aw repo and blog index.
- Triage comments mention AIC "4.85 to 17.53" and token range "~49k–412k"; both match the table. Totals in Claim 1 are our own arithmetic.
- Source is short and its cause is unconfirmed; confidence is anecdotal overall. Cited claim numbers in other notes were checked against their headings (2026-11-20 Claims 4, 5, 11; weekly-2026-04-06 Claims 4, 10; 2026-09-28 Claim 2).
- Our take: probably a misconfiguration (declared vs prompted outputs) rather than a runtime limitation, but unverified.
