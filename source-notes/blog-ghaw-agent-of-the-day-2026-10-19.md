---
source_url: https://github.github.com/gh-aw/blog/2026-10-19-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – October 19, 2026: PR Sous Chef (skip-if-no-match gate and a quiet run)"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-10-19
date_extracted: 2026-10-20
last_checked: 2026-10-20
status: current
confidence_overall: anecdotal
issue: "#4225"
---

# Agent of the Day – October 19, 2026: PR Sous Chef

> A short first-party profile of PR Sous Chef's current configuration — a 5-minute schedule behind a `skip-if-no-match` search gate, read-only, small model — plus one audited 1.9-minute "stable, no action" run; a single-run, vendor-reported datapoint, not evidence about nudge quality.

## Source Context

- **Type**: blog-post (first-party gh-aw "Agent of the Day" entry, bylined "Copilot").
- **Author credibility**: Official gh-aw blog; two run IDs are given (39268406664 and 39264765467) so the audit is checkable in principle. The post is short and reports aggregate audit values only.
- **Scope**: One workflow (PR Sous Chef), its trigger/gate/engine configuration as described in prose, and one scheduled run on `main`. It does NOT report how many PRs matched the gate, how many nudges the workflow has sent, whether nudges helped, per-run token/AIC cost, or the workflow's prompt. The "Try it" section only links to `github/gh-aw` (workflow source not read for this note).

## Extracted Claims

### Claim 1: PR Sous Chef is a scheduled-every-five-minutes workflow that nudges idle PRs, with manual and slash-command triggers
- **Evidence**: The post paraphrases the workflow's own frontmatter description; no config block is shown.
- **Confidence**: anecdotal (first-party description, config not displayed)
- **Quote**: "It fires every five minutes, and also on"
- **Our assessment**: The quote is truncated at a code-formatting boundary; the post continues with `workflow_dispatch` or a `/souschef` slash command on a pull request comment. The "nudges PRs idle for ten minutes with unanswered reviews and a branch update, without duplicate agent work" description is the post's paraphrase of frontmatter. Note the 5-minute cadence differs from earlier notes (see Cross-References).

### Claim 2: A `skip-if-no-match` search is the key design element — the agent does not spin up unless a candidate PR exists
- **Evidence**: Prose description of the gate query: open, non-draft PRs, excluding Dependabot, Renovate and anything labeled `broccoli`.
- **Confidence**: anecdotal for this instance; the underlying mechanism is documented as settled in the docs note.
- **Quote**: "The trick is the gate."
- **Our assessment**: A concrete, named real-world use of the declarative gate described in `docs-ghaw-deterministic-agentic-patterns.md` Claim 8. The post's follow-on sentence — "means the agent doesn’t spin up unless there is a PR worth looking at" — states the intent. Note the gate is a deterministic pre-check (no model tokens), unlike the agent-driven skip in `blog-ghaw-agent-of-the-day-2026-05-20.md`. The exact query string is not shown verbatim (rendered as split inline code), so reconstructing it should be done from the workflow source, not this note.

### Claim 3: The workflow is read-only with a concurrency group so runs queue rather than overlap
- **Evidence**: Prose statement; no frontmatter shown. Consistent with a 5-minute schedule where a slow run could otherwise overlap the next.
- **Confidence**: anecdotal
- **Quote**: "Permissions are read-only, with a concurrency group so runs queue instead of overlapping."
- **Our assessment**: Sensible pairing for any high-frequency schedule. Tension worth noting: "read-only permissions" yet the workflow is described as nudging PRs — nudges presumably go through safe outputs (earlier notes show Sous Chef comments in PR history), which this post does not explain. Do not read "read-only" as "produces no output ever."

### Claim 4: A small model (`copilot/claude-haiku-4.5` on the `pi` engine) is used for a small, frequent job
- **Evidence**: Prose statement of engine and model.
- **Confidence**: anecdotal
- **Quote**: "a small model for a small, frequent job."
- **Our assessment**: Explicit model-to-job matching. The post offers no cost comparison against a larger model. Contradictory-looking earlier data (gpt-5.4 on `pi`) is treated as config drift over time — see Cross-References.

### Claim 5: One audited scheduled run took 1.9 minutes with 0 errors/warnings, read-only posture and no GitHub writes
- **Evidence**: Audit table for run 39268406664 (scheduled, on `main`): conclusion Success, Duration 1.9 minutes, Errors/warnings 0 / 0, Posture "Read-only, no GitHub writes emitted", Behavior "Directed, narrow tool breadth, lean resources".
- **Confidence**: anecdotal (n=1)
- **Quote**: "Read-only, no GitHub writes emitted"
- **Our assessment**: A checkable single datapoint. No token or AIC count is given, so it cannot be put directly beside the 15.7M-token May figure. One unexplained point: the run executed for 1.9 minutes, so the gate presumably matched at least one PR (or the gate sits elsewhere in the pipeline); the post does not say what the agent examined. Hence "a run that finds nothing to do" is the author's framing, not a measured fact.

### Claim 6: The audit compared the run to the previous successful run (~25 minutes earlier) and classified it "stable", recommending no action
- **Evidence**: Comparison to run 39264765467 on event, task domain, execution style, resource profile, tool breadth; no change in turns, posture or blocked requests.
- **Confidence**: anecdotal
- **Quote**: "with no change in turns, posture or blocked requests."
- **Our assessment**: Shows an agentic-audit step that diffs a run against its predecessor — a baseline-comparison monitoring pattern. Note the ~25-minute gap implies runs between the two did not succeed or were skipped/not selected; the post does not explain (with a 5-minute schedule, skipped runs are plausible and consistent with the gate, but that is our inference).

### Claim 7: For a heartbeat agent, "healthy" means cheap and uneventful
- **Evidence**: Author's framing of the single audited run.
- **Confidence**: anecdotal (opinion)
- **Quote**: "A run that finds nothing to do, costs almost nothing and changes nothing is a healthy one."
- **Our assessment**: A useful monitoring heuristic (quiet = healthy) that echoes `blog-ghaw-agent-of-the-day-2026-05-20.md` Claim 10 ("knowing when NOT to run"). Caveat: quiet is also what a broken gate looks like, so quiet-run health needs a separate liveness signal; the post does not address this.

### Claim 8: Catching stalls early with a cheap model and a tight gate keeps review loops moving without humans polling a queue
- **Evidence**: Assertion in "Why it matters"; no outcome data (no nudge counts, no time-to-merge).
- **Confidence**: anecdotal
- **Quote**: "Catching these within minutes, with a cheap model and a tight gate, keeps review loops moving without humans polling a queue."
- **Our assessment**: Plausible but unsupported by this post — the audited run emitted no writes, so it demonstrates the cheap-idle half, not the effectiveness half. Do not cite as evidence that nudges improve review latency.

### Claim 9: Sous Chef runs alongside other automated helpers in parallel
- **Evidence**: Author notes other agents in flight in the same window.
- **Confidence**: anecdotal
- **Quote**: "so the Sous Chef is one of several automated helpers working in parallel."
- **Our assessment**: Names Architecture Guardian, Dead Code Removal Agent and Issue Monster. Minor context; reinforces the multi-agent-fleet picture in earlier notes.

## Concrete Artifacts

```
Audit of run 39268406664 (scheduled, main) — from "What the live run shows" table,
https://github.github.com/gh-aw/blog/2026-10-19-agent-of-the-day/

Measure            | Value
Conclusion         | Success
Duration           | 1.9 minutes
Errors / warnings  | 0 / 0
Posture            | Read-only, no GitHub writes emitted
Behavior           | Directed, narrow tool breadth, lean resources

Compared against previous successful run 39264765467 (~25 min earlier):
matched on event, task domain, execution style, resource profile, tool breadth.
Audit classification: stable; recommendation: no action.
```

```
PR Sous Chef configuration as described in prose (not a verbatim config):
  schedule: every 5 minutes; also workflow_dispatch and /souschef slash command on a PR comment
  gate:     skip-if-no-match search "is:pr is:open -is:draft"
            excluding Dependabot, Renovate, and label "broccoli"
  perms:    read-only; concurrency group (runs queue, don't overlap)
  engine:   pi, model copilot/claude-haiku-4.5
```

## Cross-References

- **Corroborates**: `docs-ghaw-deterministic-agentic-patterns.md` Claim 8 (`skip-if-match:` / `skip-if-no-match:` produce skipped, not failed, runs) — this post is a named production use of that gate. `blog-ghaw-agent-of-the-day-2026-05-20.md` Claim 10 (automation maturity as knowing when not to run) and Claim 9 (value of skip-when-idle agents) share the quiet-is-good framing, though that note's skip is agent-driven (Claims 3 and 5: 3 turns, 123k tokens) whereas this gate is deterministic.
- **Contradicts**: None filed. Configuration differs across notes, but this reads as config change over time, not a contradiction: `blog-ghaw-weekly-2026-08-24.md` Claim 8 reports three runs in a day on the `pi` engine (PR #55171's footer names `copilot/gpt-5.4`); `blog-ghaw-agent-of-the-day-2026-09-07.md` Claim 5 describes Sous Chef as a "daily workflow" with footer `openai/gpt-5.4`; this post describes a 5-minute schedule on `copilot/claude-haiku-4.5`. Dates are ~2 months apart and different workflow versions are plausible; no source claims the configs coexist.
- **Extends**: `blog-ghaw-weekly-2026-08-24.md` Claim 8 and `blog-ghaw-agent-of-the-day-2026-09-07.md` Claim 5 (earlier PR Sous Chef profiles) with the gate, model and schedule details. `blog-ghaw-agent-of-the-day-2026-06-02.md` (Concrete Artifacts → per-workflow token table) reports PR Sous Chef at 15.7M tokens across 5 runs, ~186 turns/run on May 29 — this post's 1.9-minute lean run is a much lighter datapoint, but without token counts the two cannot be compared numerically; contrast, do not merge. `blog-ghaw-agent-of-the-day-2026-10-16.md` is same-series telemetry (cost and activation failures) but covers a different workflow.
- **Novel**: The explicit gate query composition (open, non-draft, bot/label exclusions), the pairing of a 5-minute schedule with a small model, the concurrency-queue design for high-frequency schedules, and the run-vs-previous-run "stable" audit classification.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Sous Chef as a worked example under trigger gating: a deterministic search pre-check (`skip-if-no-match`) makes a 5-minute schedule affordable because the model is only invoked when candidates exist; pair with the concurrency-group note for high-frequency schedules. Cite alongside `docs-ghaw-deterministic-agentic-patterns.md` Claim 8, labelled single-source, vendor-reported.
- **Chapter 01**: A heartbeat-agent example (frequent, narrow, small model) to contrast with the daily, multi-turn agents already cited. Avoid quoting cost figures — none are given.
- **Chapter 05**: Only a weak mention: Sous Chef running alongside other fleet agents. Do not claim nudge effectiveness; the post has no outcome data.

## Extraction Notes

- Fetched the post via `curl` and a Python HTML-stripping pass; read the full post (short: overview, gate/config paragraph, audit table, "why it matters", "try it"). Linked workflow source on GitHub and the run pages were not followed; run IDs 39268406664 and 39264765467 were not independently verified.
- Inline code spans in the page split some sentences, so two quotes are truncated at those boundaries (noted in assessments).
- Cross-reference claim numbers were verified against the cited notes (weekly-08-24 Claim 8, 09-07 Claim 5, deterministic-patterns Claim 8, 05-20 Claims 3/5/9/10). The 06-02 note was cited by section because its claim numbering was not checked.
- The post is thin and single-run; confidence is kept at anecdotal.
