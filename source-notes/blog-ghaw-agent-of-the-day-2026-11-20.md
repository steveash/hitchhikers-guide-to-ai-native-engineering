---
source_url: https://github.github.com/gh-aw/blog/2026-11-20-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – November 20, 2026: agentic-token-optimizer (a scheduled agent that audits one high-AIC workflow per weekday and files one issue)"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-11-20
date_extracted: 2026-11-21
last_checked: 2026-11-21
status: current
confidence_overall: anecdotal
issue: "#4874"
---

# Agent of the Day – November 20, 2026: agentic-token-optimizer

> A first-party profile of a weekday meta-agent that picks one high-AIC workflow, audits its recent runs and files a single capped issue with cut recommendations; contributes a three-run data point that duration does not predict cost (23–29 min, 18–71 AIC), but is anecdotal (n=3, no measured savings).

## Source Context

- **Type**: blog-post (first-party gh-aw "Agent of the Day" entry, bylined "Copilot"; filed as `documentation` but it is a dated blog post).
- **Author credibility**: Official gh-aw blog. Run IDs (44548468229, 44329115341, 44107903322) and issue #79297 are cited, so figures are checkable in principle; not independently verified here. The opening "Desmond Varga" vignette is narrative framing, not evidence.
- **Scope**: One workflow, a three-run table, the audit findings for the latest run, and the one issue it filed about a target workflow (Ponytail Reviewer). It does NOT show the optimizer's source or prompt, how AIC is computed, how "highest-AIC" is chosen, or whether the recommendations were applied and saved anything.

## Extracted Claims

### Claim 1: A scheduled agent picks one high-AIC workflow per weekday, audits its runs, and files a single issue
- **Evidence**: Prose description of `agentic-token-optimizer` ("Agentic Workflow AIC Usage Optimizer"); example issue #79297.
- **Confidence**: anecdotal (first-party description)
- **Quote**: "Each run picks one high-AIC agentic workflow, audits its recent runs, and files a single issue with efficiency recommendations."
- **Our assessment**: A concrete "agent that optimizes agents" pattern that complements the audit-only sibling in the 2026-11-18 note: this one targets a single workflow and produces actionable recommendations rather than a fleet ranking. No workflow source is shown, so it cannot be reproduced from this page.

### Claim 2: Issue-tracker hygiene is designed in: one issue per run, older same-prefix issues are closed
- **Evidence**: Stated design constraint; issue title carries the `[agentic-token-optimizer]` prefix.
- **Confidence**: anecdotal
- **Quote**: "The workflow is capped at one issue per run, and it closes older issues with the same prefix so the tracker stays readable."
- **Our assessment**: Transferable and cheap: cap output volume and supersede stale reports by prefix. Trade-off (not discussed): auto-closing older issues discards history of recommendations that were never acted on.

### Claim 3: Run duration does not predict cost: 23–29 min runs spanned 18–71 AIC
- **Evidence**: Three-run table (Concrete Artifacts): 70.58 AIC / 28.7 min, 18.48 / 29.1 min, 40.09 / 23.0 min; all succeeded, one turn, zero errors/warnings.
- **Confidence**: anecdotal (n=3, one workflow)
- **Quote**: "Durations range from 23 to 29 minutes, yet AIC ranges from 18 to 71. Duration alone does not tell you what a run cost."
- **Our assessment**: Directionally believable, and the table supports it (the longest run is not the costliest, the 29.1-min run is the cheapest). Three points cannot establish a general rule, and the post does not explain what drove the variance. Our arithmetic: mean ≈ 43 AIC, 129.15 AIC total over three days.

### Claim 4: Judge agent runs by cost, not just pass/fail
- **Evidence**: Author's takeaway from Claim 3's table.
- **Confidence**: anecdotal (advice)
- **Quote**: "look at AIC per run, not just pass or fail."
- **Our assessment**: Sound, and matches the observability stance of the 2026-11-17 and 2026-11-18 notes. All three runs here are green yet differ by ~3.8x; pass/fail would hide that. The post's "nearly four times" phrasing is consistent (70.58 / 18.48 ≈ 3.8).

### Claim 5: The auditor raised three findings on the latest run, two rated high
- **Evidence**: Audit of run 44548468229: "Resource heavy for domain" (high; 36 bash calls, two write actions), "Weak agentic control" (high; four control events), "High token usage" (medium; 40 model invocations, ~5,900 tokens of rebuild excess). Network: 49 requests to api.github.com and api.githubcopilot.com, none blocked.
- **Confidence**: anecdotal (vendor-reported, unexplained thresholds)
- **Quote**: "High token usage (medium): 40 model invocations and about 5,900 tokens of rebuild excess."
- **Our assessment**: Notable inconsistency: the run is described as "one turn each" yet shows 40 model invocations, so "turn" and "model invocation" are different units (consistent with the 2026-11-18 note's oddity about single-turn runs flagged for poor control). As in that note, the flag taxonomy is applied to the auditor itself and fires on a successful run.

### Claim 6: The optimizer chose its target by highest AIC; the target was cache-read dominated
- **Evidence**: Issue #79297, "[agentic-token-optimizer] Optimize Ponytail Reviewer: cut exploration, setup turns, and re-reads"; 14.34 AIC across three runs (~4.8 per run, our arithmetic: 14.34 / 3 = 4.78); about 90% of input as cache reads.
- **Confidence**: anecdotal
- **Quote**: "The optimizer chose the Ponytail Reviewer because it was the highest-AIC workflow in its data, at 14.34 AIC across three runs, or about 4.8 AIC per run. Roughly 90% of its input was cache reads."
- **Our assessment**: Important scoping point: the ~90% cache-read share and 4.8 AIC belong to the TARGET (Ponytail Reviewer), not to the optimizer. Our arithmetic also shows the optimizer's own runs (18–71 AIC) each cost roughly 4–15x the per-run cost of the workflow it was optimizing; the post does not comment on whether the optimizer pays for itself. Also, "highest-AIC" here means highest within a tiny sample (3 runs), so the selection rule is weakly grounded.

### Claim 7: The issue states its own limits: three no-op runs and a run-query cap
- **Evidence**: Issue content as summarized by the post.
- **Confidence**: settled (the post states the limitation); anecdotal for the findings
- **Quote**: "It also notes that the run query hit its 50-run cap, so the window may hold more runs than it analyzed."
- **Our assessment**: Good practice mirroring the 2026-11-18 note's window caveat (Claim 6 there). Per the post, the analyzed runs were "three successful pull_request runs, all ending in noop with no review findings", so the optimizer recommended cuts for a reviewer observed only on runs where it found nothing; recommendations could degrade runs that do find issues. The post does not address this.

### Claim 8: Recommendations target exploration, setup turns and re-reads, where a reviewer burns context without adding value
- **Evidence**: Issue title and the post's description; no recommendation text or diff is shown.
- **Confidence**: anecdotal
- **Quote**: "The recommendations target exploration, setup turns, and re-reads, which are the places where a reviewer agent burns context without adding review value."
- **Our assessment**: Plausible and consistent with the turn-count-as-cost-lever theme (2026-11-17 note, Claim 3). Asserted, not demonstrated: no before/after AIC is shown.

### Claim 9: The value of an optimizer is a specific, actionable issue
- **Evidence**: Author's opinion.
- **Confidence**: anecdotal
- **Quote**: "An issue that names a target workflow, a time window, and a cache-read share is something a person can act on in an afternoon."
- **Our assessment**: Good design heuristic for audit outputs (target, window, a number). But "can act on in an afternoon" is untested; the post reports no action taken on #79297.

### Claim 10: Ask what the agent did that a script could have done in one step
- **Evidence**: Author's advice; no per-turn classification is given in this post.
- **Confidence**: anecdotal (advice)
- **Quote**: "Start with the most expensive row, read its last few runs, and ask what the agent did that a script could have done in one step."
- **Our assessment**: A compact triage procedure. Note the triage comments mention a "77–91% of turns reducible to deterministic" figure; that figure is NOT on this page (it is in the 2026-11-17 note, Claim 5), so it is not extracted here.

### Claim 11: Spotlight selection skipped a workflow with only failed zero-token runs
- **Evidence**: Rotation is least-recently-featured; `ace-editor` had two failed runs (July 13 and 31) with zero tokens.
- **Confidence**: anecdotal
- **Quote**: "so there was no trustworthy evidence to write from."
- **Our assessment**: Same editorial rule as the 2026-11-17 note (Claim 8): no live evidence, no profile. Minor; useful only as a process observation.

## Concrete Artifacts

Run table from the post (vendor-reported; all runs succeeded, one turn each, zero errors/warnings):

```
Run            Date (UTC)   Duration   AIC
44548468229    2026-11-19   28.7 min   70.58
44329115341    2026-11-18   29.1 min   18.48
44107903322    2026-11-17   23.0 min   40.09
```

Latest-run audit findings (post's wording of labels):

```
Resource heavy for domain (high): General Automation run, 36 bash calls, two write actions
Weak agentic control (high): four control events, exploratory execution, selective writes
High token usage (medium): 40 model invocations, ~5,900 tokens of rebuild excess
Network: 49 requests to api.github.com and api.githubcopilot.com, none blocked
```

Issue filed: #79297 "[agentic-token-optimizer] Optimize Ponytail Reviewer: cut exploration, setup turns, and re-reads" (target: 14.34 AIC over 3 runs, ~90% of input cache reads, 50-run query cap hit).

## Cross-References

- **Corroborates**: `blog-ghaw-agent-of-the-day-2026-11-18.md` (Claim 7: cheap scheduled audit as cost observability; Claim 6: disclosing window/run-cap limits); `blog-ghaw-agent-of-the-day-2026-11-17.md` (Claim 3: turn count as the main cost lever; Claim 8: skip workflows without live evidence).
- **Contradicts**: none found. No claim materially opposes an existing note, so no contradiction issue was filed.
- **Extends**: `docs-ghaw-cost-management.md` (Claim 11: scheduled meta-agent for cost optimization; this is a worked example, though it files issues rather than PRs with frontmatter changes; Claim 4: `gh aw logs` is the data source, here via `agenticworkflows logs`). Extends the 2026-11-18 note by moving from fleet-wide ranking to a single-target recommendation issue.
- **Novel**: Three green runs of near-equal duration with a 3.8x AIC spread; the "one issue per run, close older same-prefix issues" output-hygiene rule; the observation that the optimizer's own per-run cost exceeds its target's per-run cost (our arithmetic) with no payback evidence.

## Guide Impact

- **Chapter 05**: Add this as a second, anecdotal example beside the 2026-11-18 audit for the guide's cost-visibility guidance: report AIC/cost per run, not pass/fail or duration. Cite the three-run table with an n=3 caveat; do not present as measured savings.
- **Chapter 05**: When recommending an optimizer agent, add the caution that its own cost must be tracked against savings; this source gives no savings figure and its runs cost 18–71 AIC each.
- **Chapter 02**: Optional design note for scheduled meta-agents: cap to one issue per run and supersede older same-prefix issues; state the analysis window and query cap in the output.

## Extraction Notes

- Read the full post (fetched raw HTML and stripped tags for verbatim quotes). No sub-pages followed; the post links only to the gh-aw repository and the blog index.
- The triage comments attribute "~90% cache reads" loosely and cite a 77–91% "reducible to deterministic" figure; on reading the page, the 90% belongs to the target workflow (Ponytail Reviewer) and the 77–91% figure does not appear, so it was omitted. Cited cross-reference claim numbers were checked against the cited notes' headings.
- Source is thin (short profile, no artifacts beyond one table); claims are therefore limited and confidence is anecdotal overall.
