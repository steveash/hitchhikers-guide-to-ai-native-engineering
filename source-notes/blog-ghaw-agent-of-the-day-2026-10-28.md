---
source_url: https://github.github.com/gh-aw/blog/2026-10-28-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – October 28, 2026: Issue Monster (five live runs and one classified failure)"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-10-28
date_extracted: 2026-10-29
last_checked: 2026-10-29
status: current
confidence_overall: anecdotal
issue: "#4411"
---

# Agent of the Day – October 28, 2026: Issue Monster

> A vendor-reported but checkable run table for Issue Monster (5 runs, 4 successes, one `driver_exit` failure with zero tokens) that offers a concrete "visible, classified failure" example and an explicitly open question about repeat comments on the same issues.

## Source Context

- **Type**: blog-post (first-party gh-aw "Agent of the Day" entry, bylined "Copilot"). Submitted as `documentation`, but it is a dated blog post.
- **Author credibility**: Official gh-aw blog; five run IDs are given, so the numbers are checkable in principle. Figures come from the `agentic-workflows logs` output; the post says its structured audit timed out.
- **Scope**: One workflow (Issue Monster), one ~2-hour window of five runs. It does NOT show the prompt, the issue-selection logic, comment contents, or why the driver exited. The schedule, gates, dispatch model and `cookie` label are not re-described; those are covered in earlier notes. The "Try it" section only links to `github/gh-aw`; no sub-pages were followed.

## Extracted Claims

### Claim 1: Per-run footprint is compact: about 8–10 minutes, 60,000–83,000 tokens, three comments, on the Pi engine with `copilot/gpt-5`
- **Evidence**: Run table (four successful runs of 8.1–9.5 min, 3 comments each) and prose summary.
- **Confidence**: anecdotal (vendor-reported, one morning window)
- **Quote**: "roughly eight to ten minutes, around 60,000 to 83,000 tokens, and three comments"
- **Our assessment**: Consistent with the ~62k tokens / 7.9 min audited run in `blog-ghaw-agent-of-the-day-2026-10-20.md` Claim 5 and the ~70k average in `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 4. The prose says "eight to ten minutes" while the table's successful runs span 8.1–9.5 min; the failed run took 6.6 min. Note this post says three comments per run while Oct 20 reported three assignments plus three comments; this post does not mention assignments at all.

### Claim 2: Window aggregate: 4 of 5 runs successful, 12 safe-output items, about 284,000 tokens, roughly 2.5 AI credits, and zero missing-tool or missing-data requests
- **Evidence**: Summary from `agentic-workflows logs`.
- **Confidence**: anecdotal
- **Quote**: "The summary reports 4 of 5 runs successful, 12 safe-output items, about 284,000 tokens and roughly 2.5 AI credits in total."
- **Our assessment**: Gives a cost denominator that earlier notes lacked: ~0.5 credit per run, ~71k tokens per successful run if the failed run burned none (284k / 4). 12 items = 4 successful runs x 3 comments, so no assignments appear in this window or the post does not count them; the post does not say. n=5, one morning, so not a rate.

### Claim 3: One run failed with a `driver_exit` at the "Execute Pi CLI" step, zero tokens recorded, and the conclusion job's failure handler fired as designed
- **Evidence**: Run table row (run 40704218234, 14:15 UTC, 6.6 min, "Failure (driver exit)") plus prose.
- **Confidence**: anecdotal (single instance; root cause not given)
- **Quote**: "The 14:15 run ended in a driver_exit failure at the “Execute Pi CLI” step, with zero tokens recorded."
- **Our assessment**: A rare failure datapoint for this series; the 09-03 note (Claim 3) reported ten of ten runs clean, so this is a first recorded failure for Issue Monster in our corpus. The failure is at the engine-driver step before any model tokens, i.e. an infrastructure/engine failure rather than an agent-judgment failure. The post gives no cause, no retry behavior, and no statement of whether the next 30-minute run recovered. The 6.6 minutes of runtime with zero tokens is unexplained.

### Claim 4: For a frequently-scheduled agent, the property that matters is that failure is visible and classified, not that it never happens
- **Evidence**: Authorial argument, supported by the single classified failure above.
- **Confidence**: anecdotal (opinion)
- **Quote**: "what matters is that the failure is visible and classified rather than silent."
- **Our assessment**: We buy the principle for scheduled agents; it is a harness-reliability framing, not a measurement. The post shows the failure handler fired but not what the handler does (issue? notification?), so "classified" here means the run was labeled `driver_exit`, nothing more.

### Claim 5: The same issues received comments in repeated runs (#72589 in three consecutive runs, #72330 in three of four), and the post declines to say whether this is healthy follow-up or circling
- **Evidence**: Issue numbers from the logs; other commented issues listed (#72119, #72479, #70975, #68171).
- **Confidence**: anecdotal; explicitly left open by the authors
- **Quote**: "Whether that repetition is healthy follow-up or a sign the workflow keeps circling the same threads is a fair question for its maintainers, and we are not going to pretend the logs answer it."
- **Our assessment**: The most useful item for Ch03: a possible looping smell in a 30-minute unattended agent, visible only by cross-run comparison of targets. Compare `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 8 (retry-blocked comment on repeatedly-closed PRs) which is an intentional repeat comment; the post does not say whether that mechanism explains these. Treat as an open question, not a finding. Do not assert that the agent is looping.

### Claim 6: Small, regular, bounded runs with safe-output-only writes make an agent easy to reason about and a bad day cheap to review
- **Evidence**: Authorial conclusion drawn from the run table; each run "well under a credit".
- **Confidence**: anecdotal (rhetorical; supported by the cost figures in Claim 2)
- **Quote**: "Small, regular, bounded runs make an agent easy to reason about."
- **Our assessment**: Plausible and consistent with the "no fanfare" thesis in `blog-ghaw-agent-of-the-day-2026-09-03.md` Claim 8. The cost half of the claim is supported by the numbers; the "easy to review" half is not, since repeated comments (Claim 5) are exactly the sort of thing a reviewer would have to notice across runs.

### Claim 7: The post discloses an evidence limitation: the structured audit timed out, so figures rely on the logs output alone
- **Evidence**: Author caveat naming run 40698326997.
- **Confidence**: settled (as a statement about the post's own method)
- **Quote**: "our attempt to run a structured audit on run 40698326997 timed out during report generation, so the figures above come from the logs output alone."
- **Our assessment**: Good practice to disclose, and it means this post lacks the firewall, turn-count and error data that the Oct 20 audited run had. Also an incidental data point that the audit tooling itself can fail on report generation.

## Concrete Artifacts

Run table, from the post (window "just over two hours" on 2026-10-28 UTC):

```
Run          Started (UTC)  Duration  Outcome
40687259037  12:22          9.5 min   Success, 3 comments
40689976483  12:42          8.1 min   Success, 3 comments
40694785400  13:15          9.3 min   Success, 3 comments
40698326997  13:38          9.2 min   Success, 3 comments
40704218234  14:15          6.6 min   Failure (driver exit)
```

Aggregates as stated in the post: 4 of 5 successful; 12 safe-output items; about 284,000 tokens; roughly 2.5 AI credits; zero missing-tool / missing-data requests. Repeated targets: #72589 (3 consecutive runs), #72330 (3 of 4 runs).

## Cross-References

- **Corroborates**: `blog-ghaw-agent-of-the-day-2026-10-20.md` Claim 5 (per-run token/duration scale, Pi + `copilot/gpt-5`); `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 4 (multi-run token totals, ~70k per run) and Claim 1 (30-minute cadence, consistent with run starts ~20–40 minutes apart); `blog-ghaw-agent-of-the-day-2026-09-03.md` Claim 8 (small unattended loop framing).
- **Contradicts:** None. Open contradiction #2979 (Issue Monster dispatch: one-at-a-time vs batched) is not advanced: this post reports three comments per run and never mentions `assign_to_agent`. The 09-03 note's Claim 3 (ten of ten runs clean) differs from this window's 1 of 5 failure, but those are different windows, not a conflict, so no issue was filed.
- **Extends**: `blog-ghaw-agent-of-the-day-2026-09-03.md` Claim 3 and `blog-ghaw-agent-of-the-day-2026-10-20.md` (adds the first recorded failure and the AI-credit cost figure).
- **Novel**: A `driver_exit` failure at "Execute Pi CLI" with zero tokens; the AI-credit unit (~2.5 credits over five runs); the repeat-comment-on-same-issue observation left as an open question; the disclosure that the structured audit can time out.

## Guide Impact

- **Chapter 02**: If a harness-reliability example of "visible, classified failure" for scheduled agents is wanted, cite this post's `driver_exit` run (Claim 3, Claim 4) as an n=1 illustration; do not claim the handler's behavior beyond "fired as designed".
- **Chapter 03**: Add the repeat-comment pattern (Claim 5) as an example of a loop/circling smell that per-run success status cannot reveal; recommend cross-run comparison of targets. Present it as the authors' open question.
- **Chapter 04**: Where cost of scheduled agents is discussed, "about 0.5 AI credit and ~70k tokens per run, ~8–10 minutes (one window, vendor-reported)" is a usable illustrative figure alongside the Oct 20 figure. Keep labeled n=5.

## Extraction Notes

- Read the full post (short; one table and four short sections). Text was fetched directly from the page and quotes copied from the rendered text; one quote retains the source's typographic quotation marks around "Execute Pi CLI".
- Triage suggested merging into the Oct 20 note; a standalone note was written because the new material (run table, failure, repeat comments) is separable, with cross-references pointing to the earlier notes. Schedule, gates, dispatch model and `cookie` claims were deliberately not re-extracted.
- Cross-reference claim numbers verified against headings: 08-25 Claims 1, 4, 8; 09-03 Claims 3, 8; 10-20 Claim 5 (from the note read in full).
