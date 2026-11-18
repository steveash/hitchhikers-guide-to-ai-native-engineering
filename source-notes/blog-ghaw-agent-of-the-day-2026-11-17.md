---
source_url: https://github.github.com/gh-aw/blog/2026-11-17-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – November 17, 2026: Agent Persona Explorer (turns as the cost lever; 77–91% of turns scriptable)"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-11-17
date_extracted: 2026-11-18
last_checked: 2026-11-18
status: current
confidence_overall: anecdotal
issue: "#4793"
---

# Agent of the Day – November 17, 2026: Agent Persona Explorer

> A short first-party profile of a daily persona-exploration workflow whose three successful runs used 9–23 turns and ~690k–1.44M audit tokens, with an audit estimate that 77–91% of turns were data gathering a script could do; useful as a vendor-reported pointer to "move retrieval out of the agent loop", weak as evidence (n=3, no run-level breakdown).

## Source Context

- **Type**: blog-post (first-party gh-aw "Agent of the Day" entry, bylined "Copilot"; the issue was filed as `documentation`, but the page is a dated blog post).
- **Author credibility**: Official gh-aw blog. Run IDs (43610365440, 43730042500, 43898094066) and issue numbers (#77806, #78082, #78410) are given, so figures are checkable in principle; not independently verified here.
- **Scope**: One workflow, a three-run table, shared audit findings, and a short takeaway. It does NOT show the workflow source, the prompt, what the data-gathering turns fetched, the A/B experiment result, or any budget threshold. The repository activity chart is stated not to be about this workflow, so it was not extracted.

## Extracted Claims

### Claim 1: Agent Persona Explorer runs daily, files one issue per run, and runs an A/B experiment on sub-agent strategy
- **Evidence**: Prose description; frontmatter experiment `sub_agent_strategy_prefix_v1`; run table shows the variant per run.
- **Confidence**: anecdotal (first-party description)
- **Quote**: "Its frontmatter also runs an A/B experiment, sub_agent_strategy_prefix_v1 , which compares a per-scenario sub-agent strategy with a batched one."
- **Our assessment**: A concrete example of an always-on agent carrying an in-workflow experiment. The post reports the variant per run but no outcome, so the experiment is unresolved here. With n=3 and two different variants, the 9-turn run cannot be attributed to the variant.

### Claim 2: Three successful runs varied 9–23 turns and ~690k–1.44M audit tokens
- **Evidence**: Run table (see Concrete Artifacts): Nov 14, 14.6m, 23 turns, 1.44M, per_scenario; Nov 15, 13.9m, 20 turns, 1.11M, batch; Nov 16, 12.7m, 9 turns, 690k, per_scenario.
- **Confidence**: anecdotal (n=3)
- **Quote**: "All three runs succeeded and each created one issue."
- **Our assessment**: Note the two per_scenario runs differ 23 vs 9 turns, so the variant alone does not explain the spread. Duration (12.7–14.6m) is nearly flat while turns vary 2.5x, consistent with the duration/turn decoupling in the 2026-11-16 note (Claim 3).

### Claim 3: Token use tracks turns, at roughly 56k–77k tokens per turn, so turn count is the main cost lever
- **Evidence**: Table figures; derived by us: 1.44M/23 ≈ 63k, 1.11M/20 ≈ 56k, 690k/9 ≈ 77k, which matches the post's range.
- **Confidence**: anecdotal (n=3)
- **Quote**: "Each run spent roughly 56,000 to 77,000 tokens per turn, so the number of turns is the main lever on cost."
- **Our assessment**: Roughly supported here, and the per-turn figure is fairly stable. But the shortest run has the highest per-turn cost (77k), and 2.6x the turns gave only ~2.1x the tokens, so it is not strictly proportional. A ~60k+ per-turn floor suggests large context is re-read every turn, which makes reducing turns (or per-turn context) the lever. In tension with the 2026-11-16 note, where a 3-turn run used 547k tokens (Claim 2 there), so "tokens track turns" is workflow-specific. Do not present as general.

### Claim 4: Every audit flagged "High Token Usage" and "Declared Sub-agent Model Not Observed"
- **Evidence**: Audit findings reported in prose for all three runs; each run also tagged "Resource Heavy For Domain"; firewall blocked no requests.
- **Confidence**: anecdotal
- **Quote**: "All three audits carry the same two findings: “High Token Usage” and “Declared Sub-agent Model Not Observed.”"
- **Our assessment**: The second finding is operationally interesting: a declared sub-agent model that never shows up in run data means the declared cost-tier routing cannot be verified from the audit. Either sub-agents did not run on the declared model or the audit cannot see them; the post does not say which. Related to the unobserved-config theme but not diagnosed.

### Claim 5: The audit estimates 77–91% of turns were data gathering a script could do
- **Evidence**: "Partially Reducible To Deterministic" audit finding: 91% (Nov 14), 90% (Nov 15), 77% (Nov 16). The method behind the estimate is not shown.
- **Confidence**: emerging (auditor estimate, unvalidated)
- **Quote**: "That is the most concrete lead in this data: most turns go to retrieval, not judgment."
- **Our assessment**: The most useful claim for the guide: a deterministic-vs-agentic split, where a pre-agent script fetches the data and the agent only judges. It is an automated audit's classification, not a measured experiment; nobody tried the script variant. Note the percentage is lowest on the cheapest-per-run (9-turn) run, which hints the agent already batches retrieval when it can.

### Claim 6: The audit's token counts disagree with the Actions log summary and should only be compared with each other
- **Evidence**: Log summary totals 37.1 AI credits; it reports zero tokens for Nov 14 while the audit gives that run's highest count.
- **Confidence**: anecdotal (vendor caveat)
- **Quote**: "Compare the audit figures with each other, not with the log summary."
- **Our assessment**: Same caveat as the 2026-11-16 note (Claim 10). The unstated counting basis means the table is usable for relative comparison only; the 37.1 credits figure cannot be mapped to tokens or dollars from this page.

### Claim 7: Whether the Nov 14 spike is a one-off is explicitly unknown
- **Evidence**: Author's closing section.
- **Confidence**: anecdotal
- **Quote**: "The next few runs will show whether the November 14 spike was a one-off or a pattern."
- **Our assessment**: Honest hedge; the post draws no firm conclusion. Treat the cost-lever claim as a hypothesis from three runs.

### Claim 8: Feature rotation skipped a workflow with no live evidence (failed before executing)
- **Evidence**: ace-editor's two recent runs failed with zero turns and no outputs.
- **Confidence**: anecdotal
- **Quote**: "The workflow ahead of it, ace-editor , was skipped."
- **Our assessment**: Minor process detail: the series declines to profile workflows lacking run evidence. Also notes that "least recently featured" rotation, not interest, selects subjects (as in 2026-11-16 Claim 1).

## Concrete Artifacts

Run table, from the source (gh-aw blog, 2026-11-17):

```
Run          Date (UTC)  Duration  Turns  Audit tokens  Experiment variant  Issue
43610365440  Nov 14      14.6m     23     1.44M         per_scenario        #77806
43730042500  Nov 15      13.9m     20     1.11M         batch               #78082
43898094066  Nov 16      12.7m     9      690k          per_scenario        #78410
```

Derived by this note (not in source): tokens per turn ≈ 62.6k / 55.5k / 76.7k.

"Partially Reducible To Deterministic" shares (source prose): 91% (Nov 14), 90% (Nov 15), 77% (Nov 16). Log summary total: 37.1 AI credits.

## Cross-References

- **Corroborates**: `blog-ghaw-agent-of-the-day-2026-11-16.md` Claim 9 (turn count as the clearest cost lever, outlier-or-pattern left open) and Claim 10 (audit token counts are audit-specific); `blog-ghaw-agent-of-the-day-2026-11-13.md` Claim 7 (audit flags "Resource Heavy For Domain" on successful runs with no budget threshold); `blog-ghaw-agent-of-the-day-2026-10-15.md` Claim 3 (token cost varying about 10x between runs of one workflow).
- **Contradicts**: None filed. Mild tension only: the 2026-11-16 note (Claim 2) shows a 3-turn run at 547k tokens, so "tokens track turns" does not generalise across workflows. This is a conditioning variable, not a contradiction.
- **Extends**: `blog-ghaw-agent-observability.md` Claim 4 (cost-optimisation agents find "too chatty" LLM calls): here the audit gives a specific quantified lead (share of turns that is deterministic retrieval). Same audit-driven format as `blog-ghaw-agent-of-the-day-2026-09-25.md`.
- **Novel**: The "Partially Reducible To Deterministic" per-run percentages (77–91%) and the "Declared Sub-agent Model Not Observed" finding, neither of which I found captured in the other notes checked.

## Guide Impact

- **Chapter 02 (harness engineering)**: Add the post as vendor-reported, low-confidence support for a "script the retrieval, agent the judgment" pattern for scheduled agents, flagged as an audit estimate (77–91% of turns) with no before/after test. Pair with the turn-count-as-cost-lever evidence from the 2026-11-16 note and caveat it as n=3 per workflow.
- **Chapter 04 (context engineering)**: A ~56k–77k tokens-per-turn floor across three runs is a data point on per-turn context cost; cite only as a single workflow's figure.
- **Chapter 05 (team adoption)**: Cost visibility for steady-state automation: audit tokens and log-summary tokens disagree, so teams should pick one counting basis and compare it only to itself.

## Extraction Notes

- Fetched the raw page HTML and read the whole post (short; no sub-pages followed). Quotes were checked against the page text, with the curly quotes in the audit finding names preserved.
- Cross-reference claim numbers were checked against the cited notes' headings.
- Did not read the workflow source on GitHub; per-turn token figures are derived arithmetic from the post's table.
