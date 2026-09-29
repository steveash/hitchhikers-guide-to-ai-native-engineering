---
source_url: https://github.github.com/gh-aw/blog/2026-09-28-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – September 28, 2026: Issue Arborist (partial-failure run)"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-09-28
date_extracted: 2026-09-29
last_checked: 2026-09-29
status: current
confidence_overall: emerging
issue: "#3784"
---

# Agent of the Day – September 28, 2026: Issue Arborist (partial-failure run)

> Profiles a September 28 Issue Arborist run in which most of 34 `link_sub_issue` calls failed on a trigger-context mismatch, yet two parent issues and a discussion report still landed — a first-party example of independent safe outputs giving partial-success semantics, with the failure surfaced as a critical audit finding rather than hidden.

## Source Context

- **Type**: blog-post (short "Agent of the Day" entry, bylined "Copilot", from the official gh-aw blog; a later entry in the series covered in e.g. `blog-ghaw-agent-of-the-day-2026-08-20.md`).
- **Author credibility**: First-party platform team; AI-authored post. It links the specific run, audit report, previous-day run, and issue/discussion numbers (#63931, #63932, discussion #63933) in `github/gh-aw`, so its claims are checkable in principle. I did not follow those links, so run-level figures are taken from the post's prose only.
- **Scope**: One run (Sept 28) of Issue Arborist plus a one-line comparison to the previous day's empty run. Does NOT include the workflow source, safe-outputs config, the audit report contents, the exact count of failed vs. successful link calls ("most" only), or any fix for the context mismatch.

## Extracted Claims

### Claim 1: Issue Arborist is a daily codex-powered, topology-only agent that reads the last 100 open issues and writes only through safe outputs.
- **Evidence**: Prose description of the workflow's configuration (schedule, `github: mode: local`, read-only issue scope, three safe-output types).
- **Confidence**: emerging
- **Quote**: "Issue Arborist’s job description is disarmingly simple: fetch open issues without a parent, spot the ones that belong together, and link them as sub-issues under a fresh tracking parent."
- **Our assessment**: Consistent with earlier notes (Claim 1 of `blog-ghaw-agent-of-the-day-2026-08-20.md`). New detail: the engine is named as codex, and the safe-output set is `create-issue`, `link-sub-issue`, `create-discussion`.

### Claim 2: Restricting all writes to safe outputs makes each action logged, reviewable and reversible.
- **Evidence**: Assertion from the workflow design; no reversal demonstrated in this post.
- **Confidence**: emerging
- **Quote**: "so every action it takes is logged, reviewable, and reversible"
- **Our assessment**: Plausible for issue/sub-issue links; "reversible" is asserted, not shown.

### Claim 3: The Sept 28 run cost 63.2k tokens and 11.6 AIC and found two clusters: 33 recurring incident issues and 12 deep-report quick-win issues.
- **Evidence**: Run metrics and parent issue numbers #63931 and #63932 cited in the post.
- **Confidence**: emerging
- **Quote**: "Working from 63.2k tokens and 11.6 AIC of compute, Issue Arborist scanned the open backlog and found two clusters worth grouping:"
- **Our assessment**: Useful concrete cost datapoint for a scheduled triage agent. Note the issue-cluster sizes (33 + 12 = 45) roughly match the "45 issues" the post mentions, but the 34 link attempts do not equal 45 — the post does not reconcile this.

### Claim 4: Most of the 34 `link_sub_issue` calls failed because the scheduled trigger had no issue context.
- **Evidence**: The run's audit trail, per the post; error string quoted.
- **Confidence**: emerging
- **Quote**: "the run’s audit trail shows it attempted 34 link_sub_issue calls and most of them failed with"
- **Our assessment**: The post gives the error text (see Concrete Artifacts) but only "most" failed; the triage comment's "~50%" is not in the source. A root-cause reading: the tool defaults its target to the triggering issue ("triggering"), which does not exist for schedule triggers, so an explicit issue target is likely needed. That is our inference, not the post's statement.

### Claim 5: Safe outputs are independent: a failed tool call does not roll back outputs that already succeeded, so the run shipped a usable result.
- **Evidence**: Two parent issues and a discussion were created despite the failures.
- **Confidence**: emerging
- **Quote**: "because gh-aw’s safe-outputs model treats each output independently — a broken tool call doesn’t roll back the ones that already succeeded."
- **Our assessment**: Real design tradeoff. It yields partial success, but here it also yields parents that were created while most sub-issue links were missing — i.e., the "usable triage hub" is only partially wired. The post claims value ("one place a maintainer can actually triage") without saying how many links actually landed.

### Claim 6: The failure was flagged plainly as a critical audit finding instead of being buried in a green run.
- **Evidence**: The run's audit report reports `workflow_failed` as critical.
- **Confidence**: emerging
- **Quote**: "The workflow’s own audit report flags this plainly as a workflow_failed critical finding, not something smoothed over."
- **Our assessment**: `workflow_failed` is a real finding code (see `blog-ghaw-agent-of-the-day-2026-09-24.md`, which lists it among audit finding codes). Good pattern: separate "run completed" from "run's goals achieved". Caveat: the failure was still not fixed or retried in-run.

### Claim 7: Reporting "the win and the wart in the same breath" is the desired behavior for unsupervised automation touching an issue tracker.
- **Evidence**: Editorial framing of the above run.
- **Confidence**: anecdotal
- **Quote**: "It reports the win and the wart in the same breath, which is exactly what you want from automation touching your issue tracker unsupervised."
- **Our assessment**: We agree with the principle. Note that the honesty comes from the audit tooling, not from the agent's own discussion summary, which the post says follows "the same reporting convention" and is not shown to mention the failures.

### Claim 8: Running the same agent daily yields quiet days and real-cluster days; the previous day's run had nothing to group.
- **Evidence**: Comparison with the Sept 27 run linked from the post.
- **Confidence**: anecdotal
- **Quote**: "some days there’s nothing to say, and some days there’s a real cluster to surface"
- **Our assessment**: Supports the "scheduled sweeper with empty-run tolerance" pattern; a no-op day is a valid success.

## Concrete Artifacts

```
# Source: gh-aw blog, 2026-09-28 (Issue Arborist run of Sept 28)
Tokens: 63.2k   Compute: 11.6 AIC
Created: #63931 (parent, 33 incident issues), #63932 (parent, 12 quick-win issues), discussion #63933 (category: audits)
link_sub_issue calls attempted: 34 (most failed)
Error: Target is "triggering" but not running in issue context, skipping link_sub_issue
Audit finding: workflow_failed (critical)
Safe outputs: create-issue, link-sub-issue, create-discussion
Config fragment named in post: github: mode: local
```

## Cross-References

- **Corroborates**: `blog-ghaw-agent-of-the-day-2026-08-20.md` Claim 1 (Issue Arborist scans 100 parentless issues and links them as sub-issues) and Claim 6 (results are published as a daily discussion report); `blog-ghaw-issue-pr-mgmt.md` Claim 1 (Issue Arborist creating parent issues and discussion reports).
- **Contradicts**: None found. (Claim 7 of `blog-ghaw-agent-of-the-day-2026-08-20.md` reports five runs with zero errors; this is a later run, not a conflict.)
- **Extends**: `blog-ghaw-agent-of-the-day-2026-08-20.md` Claim 7 (five-run reliability with zero errors) — here is the first documented Issue Arborist run with a critical audit finding. `blog-ghaw-agent-of-the-day-2026-09-24.md` also covers gh-aw audit findings including `workflow_failed`; that note additionally shows a blog claiming a "successful" run that first-party data contradicted, so treat this post's run-level claims with the same caution.
- **Novel**: Independent-output (no-rollback) semantics demonstrated in production with a trigger-context tool error; per-run token/AIC cost for Issue Arborist.

## Guide Impact

- **Chapter 04 (Operations)**: Candidate example for a resilience/partial-failure subsection: independent write outputs plus an audit layer that flags failed tool calls as critical, so "run finished" is not read as "run succeeded". Cite this post with the caveat that it is self-reported.
- **Chapter 03**: Note the tool/trigger-context pitfall — a tool that targets "the triggering issue" silently fails under schedule triggers; test write tools under every trigger type a workflow uses.
- **Chapter 06**: The empty-run/cluster-run contrast is a small supporting datapoint for scheduled sweeper agents; needs no new claim.

## Extraction Notes

- The post is short (~450 words); read in full. I did not follow the linked run, audit report, or the issues, so figures are unverified beyond the post. The triage comment's "~50% failure" figure does not appear in the source; the post says only "most".
- No registry edit (derived from front-matter).
