---
source_url: https://github.github.com/gh-aw/blog/2026-11-04-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – November 4, 2026: PR Sous Chef (prefilter-then-agent, scoped safe outputs, 2 of 4 runs failed)"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-11-04
date_extracted: 2026-11-05
last_checked: 2026-11-05
status: current
confidence_overall: anecdotal
issue: "#4533"
---

# Agent of the Day – November 4, 2026: PR Sous Chef

> A short first-party profile of PR Sous Chef's design (deterministic prefilter job → compact queue artifact → scoped agent with capped safe outputs) plus a four-run sample in which two runs failed unexplained and the audit itself says ~72% of turns could be deterministic; single-window, vendor-reported.

## Source Context

- **Type**: blog-post (first-party gh-aw "Agent of the Day" entry, bylined "Copilot").
- **Author credibility**: Official gh-aw blog. Run IDs are given (41842360684, 41840856940, 41839326366, 41845059126; PR Finisher runs 41843766445, 41840487772) so the figures are checkable in principle; not independently verified here.
- **Scope**: One workflow (PR Sous Chef): its prefilter/agent split, safe-output budget, a four-run table, one detailed audit, and two PR Finisher dispatches. It does NOT explain the two failures, show the prompt or frontmatter, give nudge counts or outcome data, or show the prefilter's query. Triage asked that configuration already in the 10-19 note not be repeated.

## Extracted Claims

### Claim 1: PR Sous Chef splits cheap deterministic work (a prefilter job that builds a PR-queue artifact) from the agent, which only reads that queue
- **Evidence**: Prose description of the design; no config shown.
- **Confidence**: anecdotal (first-party description)
- **Quote**: "job fetches the actionable PR queue and uploads a compact artifact."
- **Our assessment**: The page continues "Only then does the agent run, reading that queue instead of crawling the repository." This is an extension of the `skip-if-no-match` gate in the 10-19 note: there the gate only decides *whether* to run; here the prefilter also hands the agent a *prepared input*. Same shape as the pre-step candidate list in `blog-ghaw-agent-of-the-day-2026-10-20.md` Claim 4. Whether the prefilter replaced the `skip-if-no-match` gate or sits beside it is not stated.

### Claim 2: The safe-output budget is narrow and enumerated
- **Evidence**: Prose list: dispatch `pr-finisher` up to 4 times (always on `main`), up to 5 comments, approve up to 8 runs of a short allow-list of workflows, dismiss reviews, and open an expiring `[pr-sous-chef]` issue for anything needing a human.
- **Confidence**: anecdotal (caps stated, not verified against frontmatter)
- **Quote**: "approve up to 8 runs of a short allow-list of workflows, dismiss reviews"
- **Our assessment**: A concrete example of per-run blast-radius caps on a frequent trigger, including a human-escalation path (expiring issue). It also resolves the open tension in the 10-19 note Claim 3 ("read-only" yet nudging): writes go through safe outputs. Note "approve runs" and "dismiss reviews" are higher-privilege actions than comments; the post does not say what guards them beyond the caps and allow-list.

### Claim 3: Narrow safe-output limits keep a frequent trigger from becoming noisy
- **Evidence**: Author's takeaway; no noise measurements.
- **Confidence**: anecdotal (opinion)
- **Quote**: "Narrow safe-output limits keep a frequent trigger from becoming noisy."
- **Our assessment**: Plausible and consistent with the design, but untested in the post: the sampled run emitted only two outputs, so it shows caps exist, not that they bound anything.

### Claim 4: Two of four sampled runs ended in failure, and the authors did not investigate
- **Evidence**: Table of four runs: 41842360684 success 9.9 min; 41840856940 failure 8.0 min; 41839326366 success 8.9 min; 41845059126 failure 9.5 min.
- **Confidence**: anecdotal (n=4, one window)
- **Quote**: "Two of the four runs above ended in failure. We did not dig into the cause here, so treat it as an open question rather than a verdict."
- **Our assessment**: A 50% failure rate on a 5-minute heartbeat agent, honestly flagged as unexplained. Do NOT cite as a failure rate for the workflow; four runs were hand-picked from "recent runs". Failures lasting 8–9.5 minutes are similar in length to successes, so they are not early aborts. Contrasts with the 10-19 note's 1.9-minute quiet run.

### Claim 5: The audit of run 41842360684 reports 11 turns, no errors/warnings, "selective_write" style, using `create_issue` and `dispatch_workflow`
- **Evidence**: Audit summary in prose.
- **Confidence**: anecdotal (n=1)
- **Quote**: "a selective_write actuation style, meaning it wrote only when it had a reason to."
- **Our assessment**: Gives an audit taxonomy term ("actuation style") not seen in earlier PR Sous Chef notes. The 11 turns here contrast with the ~186 turns/run in the May figures (see `blog-ghaw-agent-of-the-day-2026-06-02.md`), plausibly reflecting the prefilter change, but the post does not claim that.

### Claim 6: The audit says ~72% of turns look like data-gathering that could move into deterministic steps (~249k tokens)
- **Evidence**: Audit finding on run 41842360684.
- **Confidence**: anecdotal (automated audit heuristic, n=1)
- **Quote**: "That is a fair note for a workflow whose prefilter already does a lot of that work."
- **Our assessment**: The 72% and 249k figures are in the same paragraph ("roughly 249k tokens and says about 72% of the turns look like data-gathering that could move into deterministic steps"), but the quote above is the contiguous fragment that carries the post's reaction. Notable that even after a prefilter, the audit still flags most turns as shiftable — evidence for iterating prefilters. Inconsistency to flag: the table lists "about 4k in the logs summary" tokens for this same run versus ~249k in the audit; the post does not reconcile them (likely different counting, e.g. cached/input tokens), so neither number should be quoted as cost without caveat.

### Claim 7: PR Sous Chef dispatches PR Finisher, whose runs are named after the target PR
- **Evidence**: Run 41843766445 for #74785 succeeded in 10.8 min, one turn, ~18k tokens; run 41840487772 for #74077 succeeded, ~9k tokens.
- **Confidence**: anecdotal
- **Quote**: "PR Sous Chef hands work to PR Finisher, whose runs are named after the PR they target."
- **Our assessment**: A small orchestrator → worker chain: the cheap watcher dispatches a single-turn worker per PR. Run naming by target PR aids traceability. No outcome (did the PR progress?) is reported.

### Claim 8: A cheap scheduled prefilter plus a scoped agent is a good pattern for queue-style work, and deterministic-shifting advice applies even to well-structured workflows
- **Evidence**: Author's takeaways, supported by the single audit.
- **Confidence**: anecdotal (opinion)
- **Quote**: "A cheap scheduled prefilter plus a scoped agent is a good pattern for queue-style work."
- **Our assessment**: Reasonable as a design heuristic; the evidence is thin (no cost comparison with a non-prefiltered version, 2/4 failures). Second takeaway: "The audit’s own advice, moving more data fetching into deterministic steps, applies even to well-structured workflows."

## Concrete Artifacts

```
Run sample — https://github.github.com/gh-aw/blog/2026-11-04-agent-of-the-day/
Run          | Conclusion | Duration | Tokens
41842360684  | success    | 9.9 min  | about 4k in the logs summary
41840856940  | failure    | 8.0 min  | under 1k
41839326366  | success    | 8.9 min  | about 2k
41845059126  | failure    | 9.5 min  | under 2k

Audit of 41842360684: 11 turns; no errors/warnings; actuation style selective_write;
safe outputs used: create_issue, dispatch_workflow; ~249k tokens flagged;
~72% of turns "data-gathering that could move into deterministic steps".

PR Finisher dispatches: run 41843766445 (#74785) success 10.8 min, 1 turn, ~18k tokens;
run 41840487772 (#74077) success, ~9k tokens.
```

```
PR Sous Chef safe-output budget (prose, not verbatim config):
  dispatch pr-finisher  <= 4 times, always on main
  add comments          <= 5
  approve runs          <= 8, short allow-list of workflows
  dismiss reviews
  create issue          expiring, titled [pr-sous-chef], for human escalation
  schedule              every 5m (description: nudge PRs idle 10 min w/ unanswered reviews + branch update)
```

## Cross-References

- **Corroborates**: `blog-ghaw-agent-of-the-day-2026-10-20.md` Claim 4 (pre-step script prepares a short candidate list so the agent sees only that) and `docs-ghaw-deterministic-agentic-patterns.md` Claim 8 (deterministic query gating). `blog-ghaw-agent-of-the-day-2026-10-19.md` Claim 2 (gate before agent) is the same cost-control theme.
- **Contradicts**: None filed. Run durations (8–10 min) differ from the 1.9-minute quiet run in `blog-ghaw-agent-of-the-day-2026-10-19.md` Claim 5, but those are different runs with different work, not opposing claims. The token mismatch within this post (4k vs ~249k) is an internal inconsistency in how counts are reported, not a contradicting position, so no issue was filed.
- **Extends**: `blog-ghaw-agent-of-the-day-2026-10-19.md` Claims 1–4 (schedule, gate, read-only posture) with the prefilter artifact, safe-output caps and failures; `blog-ghaw-agent-of-the-day-2026-09-07.md` Claim 5 and `blog-ghaw-weekly-2026-08-24.md` Claim 8 (earlier PR Sous Chef profiles). The 09-08 note covers a different workflow (CLI Version Checker), not relevant here.
- **Novel**: The enumerated safe-output caps (4/5/8 + dismiss + expiring escalation issue), the Sous Chef → PR Finisher dispatch chain with per-run figures, the `selective_write` audit classification, the audit's own "72% shiftable" finding, and an unexplained 2-of-4 failure sample.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Where PR Sous Chef is cited as a trigger-gating example (10-19 note), add that the later design uses a prefilter job that emits a queue artifact and a capped safe-output set; label single-source, vendor-reported. Possibly note the audit's "move data-gathering into deterministic steps" advice as an iterative-refinement signal.
- **Chapter 03**: Optional: the run-audit vocabulary (turns, actuation style, shiftable-turn share) and the caution that token counts differ between log summary and audit (4k vs ~249k) so cost claims need the counting method.
- **Chapter 06**: Optional example of per-run caps and expiring escalation issues as blast-radius controls; do not claim effectiveness.
- **Chapter 05**: Do not use as nudge-effectiveness evidence — no outcome data.

## Extraction Notes

- Fetched the post via `curl` and an HTML-stripping pass; read the full post (short). The linked `github/gh-aw` source, run pages and PR pages were not followed or verified.
- Inline code spans split some sentences, so quotes use contiguous fragments between code spans.
- Cross-reference claim numbers were checked against headings in the cited notes (10-19 Claims 1–5; 10-20 Claim 4; 09-07 Claim 5; weekly-08-24 Claim 8; deterministic-patterns Claim 8). The 06-02 note is cited generally for its turn-count figure, not by claim number.
- Confidence kept at anecdotal: single post, single window, vendor-reported.
