---
source_url: https://github.github.com/gh-aw/blog/2026-11-16-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – November 16, 2026: Agent Job Health Monitor (a steady monitor with a 60-turn outlier)"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-11-16
date_extracted: 2026-11-17
last_checked: 2026-11-17
status: current
confidence_overall: anecdotal
issue: "#4771"
---

# Agent of the Day – November 16, 2026: Agent Job Health Monitor

> A short first-party profile of a daily monitor workflow whose three successful runs ranged from 2 to 60 turns and from ~339k to ~3.25M audit tokens; useful as a vendor-reported example that a healthy monitor can still be expensive and that duration does not track turn count, weak as evidence of a cause or a pattern (n=3).

## Source Context

- **Type**: blog-post (first-party gh-aw "Agent of the Day" entry, bylined "Copilot"; the issue was filed as `documentation`, but the page is a blog post).
- **Author credibility**: Official gh-aw blog. Run IDs (43525284919, 43651937051, 43773614833) and discussion numbers (#77583, #77876, #78176) are given, so the figures are checkable in principle; not independently verified here.
- **Scope**: One workflow (Agent Job Health Monitor), a three-run table, the Nov 15 audit checks, and a short takeaway. It does NOT show the workflow source, prompt, tool list, what the 60 turns were spent on, or any budget or alert threshold. The post says its repository activity chart is "shown for context" and is not about this workflow, so it was not extracted.

## Extracted Claims

### Claim 1: Agent Job Health Monitor runs daily, produces one discussion per run, and all three runs in the window succeeded
- **Evidence**: Prose plus run table with discussion numbers #77583, #77876, #78176.
- **Confidence**: anecdotal (first-party description, n=3)
- **Quote**: "Each run produces one discussion, and every run in this window succeeded and created exactly one."
- **Our assessment**: A concrete instance of the MonitorOps report-to-discussion step (`docs-ghaw-monitor-ops.md` Claim 3 and Claim 5). The post notes this is the workflow's first feature and that the rotation skipped ace-editor for having no recent runs, so selection is by recency of feature, not by interest.

### Claim 2: Turn count varied 30x across three successful runs (60, 3, 2) while audit tokens varied about 10x (3.25M, 547k, 339k)
- **Evidence**: Run table: 43525284919 (Nov 13, 21.6m, 60 turns, 3.25M); 43651937051 (Nov 14, 26.5m, 3 turns, 547k); 43773614833 (Nov 15, 24.1m, 2 turns, 339k).
- **Confidence**: anecdotal (n=3)
- **Quote**: "The November 13 run is the outlier. It took 60 turns and about 3.25 million tokens, roughly ten times the November 15 run’s total."
- **Our assessment**: Turns and tokens are not proportional: 30x turns gave ~10x tokens versus the Nov 15 run, and the Nov 14 run used 3 turns for 547k. That fits per-turn context re-reading (Claim 5) plus differing task size. The post does not say why Nov 13 took 60 turns, so the cause is unknown.

### Claim 3: Wall-clock duration does not track turn count
- **Evidence**: 60 turns took 21.6m, while 3 and 2 turns took 26.5m and 24.1m.
- **Confidence**: anecdotal (n=3)
- **Quote**: "The later runs took two or three turns, yet they still ran for 24 to 27 minutes, so turn count does not explain duration on its own."
- **Our assessment**: Corroborates the token/wall-clock decoupling in earlier entries. Run time of 24-27 minutes for 2-3 turns suggests long individual turns or waiting (tool or API latency), but the post does not diagnose it. Do not use duration as a cost proxy.

### Claim 4: Every audit labelled the runs "resource heavy for domain" and "poor agentic control", which the post calls judgments, not failures
- **Evidence**: Audit assessments reported for all three runs; all completed, no errors, two write actions each.
- **Confidence**: anecdotal
- **Quote**: "Every audit in the window carries the same two assessments: “resource heavy for domain” and “poor agentic control.” These are judgments, not failures."
- **Our assessment**: The audit penalises the steady runs, including the 2-turn Nov 15 run, as well as the outlier. A constant flag on every run carries little discriminating signal; the audit's baseline for the task domain may be miscalibrated for a monitor. The post also describes the Nov 13 run as being classed against "an issue-response task", so the domain classification itself looks questionable for a health monitor (the post does not comment on this).

### Claim 5: The Nov 15 audit's loops check failed (275 vs threshold 3) with zero retries, and the post treats it as a signal, not proof of a retry storm
- **Evidence**: Audit output for the Nov 15 run, as reported in prose.
- **Confidence**: anecdotal
- **Quote**: "The run recorded zero retries, so this is a signal to investigate, not proof of a retry storm."
- **Our assessment**: A grader that fails at 275 against a threshold of 3 on a 2-turn run with zero retries is either counting something other than retries or is mis-specified for this workflow. The post does not say what the metric measures. Useful caution for the guide: a failing automated check needs interpretation, and the vendor's own reading is "investigate".

### Claim 6: Context grew about 29x over the Nov 15 run, which the post gives as a reason for the high token total despite only two turns
- **Evidence**: Audit check reported in prose; no per-turn token breakdown.
- **Confidence**: anecdotal
- **Quote**: "That growth is one reason the token total is high for a run of only two turns."
- **Our assessment**: The 29x figure is the audit's. With two turns, a 29x rise implies large tool outputs (for example, fetched job logs) landing in context between turns. Plausible, but the post does not identify the source, so treat as a hypothesis.

### Claim 7: Gaps between turns may exceed the five-minute prompt-cache lifetime, in which case context is re-read at full cost
- **Evidence**: Audit warning on the Nov 15 run; combined with 24-27 minute runs of 2-3 turns (Claim 3).
- **Confidence**: anecdotal (audit warning, "may")
- **Quote**: "If they do, the context is re-read at full cost."
- **Our assessment**: Ties together Claims 3 and 6: long turns plus a large context make cache expiry likely, so cost is driven by context size times cache misses, not turn count alone. The post hedges with "may" and does not measure cache hits. Not verified; worth testing.

### Claim 8: The firewall logged 155 requests and blocked none
- **Evidence**: Audit network-activity check for the Nov 15 run.
- **Confidence**: anecdotal
- **Quote**: "the firewall logged 155 requests and blocked none."
- **Our assessment**: Small data point that the audit reports egress for a monitor; no domains are listed, so it cannot be assessed further.

### Claim 9: A steadily successful monitor can still be expensive, and turn count is the clearest cost lever; whether Nov 13 is an outlier or the start of a pattern is open
- **Evidence**: Author's takeaway from the three-run table; the audit for Nov 13 "recommended trimming turns, tools, or write actions".
- **Confidence**: anecdotal (author inference from n=3)
- **Quote**: "A monitor that succeeds every day can still be expensive. The clearest lever in this data is the turn count."
- **Our assessment**: Partly in tension with the post's own data (Claim 3: duration does not follow turns; Claim 2: a 3-turn run used 547k tokens). Turn count is a plausible lever for tokens, but the data supports "context size and turn count together", and the post itself leaves the pattern question open: "The open question is whether that run was an outlier or an early sign of a pattern that the next few weeks of runs will show." Do not present as settled.

### Claim 10: Audit token figures are audit-specific and should not be compared with the log summary or other tools
- **Evidence**: Caveat under the run table.
- **Confidence**: anecdotal (vendor caveat)
- **Quote**: "The log summary counts tokens differently, so compare the audit numbers with each other rather than against other tools."
- **Our assessment**: Consistent with earlier notes in the series that the counting basis is unstated. Do not convert to dollars.

## Concrete Artifacts

Run table (source: gh-aw blog, 2026-11-16, "What the last three runs show"):

```
Run          Date (UTC)  Duration  Turns  Audit tokens  Discussion
43525284919  Nov 13      21.6m     60     3.25M         #77583
43651937051  Nov 14      26.5m     3      547k          #77876
43773614833  Nov 15      24.1m     2      339k          #78176
```

Nov 15 audit checks (source: same post, "Signals worth a closer look"):

```
Loops grader:   failed, 275 against a threshold of 3; zero retries recorded
Context growth: about 29x over the run
Cache window:   gaps between turns may exceed the five-minute prompt-cache lifetime
Network:        155 firewall requests, none blocked
All runs:       "resource heavy for domain", "poor agentic control"; no errors; two write actions each
Nov 13 audit:   recommended trimming turns, tools, or write actions
```

## Cross-References

- **Corroborates**: `blog-ghaw-agent-of-the-day-2026-10-15.md` Claim 3 (token cost varying roughly 10x across runs of one workflow); `blog-ghaw-agent-of-the-day-2026-11-13.md` Claim 7 (successful runs flagged "Resource Heavy For Domain" with the authors calling cost "worth tracking" without a threshold) and Claim 6 (token-heavy successful runs).
- **Contradicts**: None. Claim 9 (turn count as the clearest cost lever) differs in emphasis from Claim 3's duration finding, but that is a within-source tension, not an opposition to another note, so no contradiction issue was filed.
- **Extends**: `blog-ghaw-agent-of-the-day-2026-10-14.md` Claim 2 (about 6k tokens in a single turn for a quiet watchdog; here a monitor ranges from 339k to 3.25M); `docs-ghaw-monitor-ops.md` Claim 3 and Claim 4 (monitors report to a durable record and target abnormal token consumption; this monitor is itself flagged by the same audit for heavy consumption); `docs-ghaw-cost-management.md` Claim 4 (`gh aw audit` as the per-run breakdown source) and Claim 7 (context limiting).
- **Novel**: The loops-grader failure (275 vs 3) with zero retries; ~29x context growth in a two-turn run; the prompt-cache-lifetime gap warning tied to long turns; a 30x turn-count spread within the same successful workflow.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: If the guide discusses turn or tool budgets for scheduled agents, add this as a vendor example where the audit recommended "trimming turns, tools, or write actions" for a 60-turn run, noting that the post leaves open whether it is a pattern and does not state a budget.
- **Chapter 03 (Verification)**: Add the loops-grader reading (Claim 5) as an example of a failing automated check that needs interpretation, not automatic action.
- **Chapter 04 (Context Engineering)**: Claims 6 and 7 are a vendor-reported illustration that context growth and prompt-cache expiry can dominate cost for few-turn runs; cite as an audit-derived hypothesis, not a measurement.
- **Chapter 05 (Team adoption)**: Cost visibility for steady-state automation: a daily "healthy" monitor can vary about 10x in tokens run to run (Claim 2). Do not quote token totals as dollars (Claim 10).

## Extraction Notes

- Fetched the post HTML and read the full article text (short). The first fetch tool summarized rather than returned text, so quotes were taken from a raw-HTML text extraction of the page. Followed no sub-pages; the linked workflow source was not fetched.
- Quotes copied character-for-character from the page text; typographic apostrophes and quote marks are preserved as on the page. Claim 8's quote begins with a lowercase "the" because it is a mid-sentence fragment.
- Triage comments differed on relevant chapters (Ch02/03/04/05); all are covered above. The cost-versus-turn-count question is recorded as the post frames it: open.
- Cross-reference claim numbers were verified against the cited notes' headings before writing.
