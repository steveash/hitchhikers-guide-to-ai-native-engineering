---
source_url: https://github.github.com/gh-aw/blog/2026-10-20-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – October 20, 2026: Issue Monster (three gates and one audited run)"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-10-20
date_extracted: 2026-10-21
last_checked: 2026-10-21
status: current
confidence_overall: anecdotal
issue: "#4244"
---

# Agent of the Day – October 20, 2026: Issue Monster

> A short first-party profile of Issue Monster's three pre-run gates plus one audited 7.9-minute run (3 `assign_to_agent` + 3 `add_comment`), useful as a second batched-dispatch datapoint for contradiction #2979; single-run, vendor-reported.

## Source Context

- **Type**: blog-post (first-party gh-aw "Agent of the Day" entry, bylined "Copilot"). Submitted as `documentation`, but it is a dated blog post.
- **Author credibility**: Official gh-aw blog. Two run IDs are given (39438401745, 39433043735), so the audit is checkable in principle. Aggregate audit values only.
- **Scope**: One workflow (Issue Monster), its gating frontmatter as described in prose, and one scheduled run on `main`. It does NOT show the candidate-selection logic, the prompt, which issues were assigned, or any failure case. The three commented issues are named (#70227, #69063, #68043) but not described. The "Try it" section only links to `github/gh-aw`; the workflow source was not read for this note. No sub-pages were followed (the page links only to the run and issue numbers and blog navigation).

## Extracted Claims

### Claim 1: Issue Monster runs every 30 minutes and on demand, and its frontmatter is mostly a set of "manners" (gates)
- **Evidence**: Prose description of the frontmatter; no config block shown.
- **Confidence**: anecdotal (first-party description; consistent with the 08-25 note)
- **Quote**: "The Issue Monster runs every 30 minutes, and on demand via"
- **Our assessment**: The quote is truncated at a code-formatting boundary (the post continues with `workflow_dispatch`). Restates cadence already recorded in `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 1; no change in cadence.

### Claim 2: A cap on open Copilot draft PRs (five or more, excluding those labeled `broccoli`) skips the run
- **Evidence**: Prose description of the first gate.
- **Confidence**: anecdotal for this instance
- **Quote**: "If five or more open Copilot draft PRs (excluding those labeled"
- **Our assessment**: Same gate as `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 2. New detail here is the `broccoli` exclusion label (continuing the post's food theme; the 10-19 PR Sous Chef note also excludes `broccoli`). The post does not say how the count is computed or whether it is done in frontmatter or a pre-step. The quote is truncated at a formatting boundary; the post continues with `broccoli`) already exist, it skips the run.

### Claim 3: `skip-if-no-match` requires at least one open issue, and `skip-if-check-failing` pauses the workflow when `build`, `test`, `lint-go` or `lint-js` are red
- **Evidence**: Prose description of the second and third gates.
- **Confidence**: anecdotal for this instance; the mechanisms are documented in `docs-ghaw-deterministic-agentic-patterns.md` Claim 8.
- **Quote**: "pauses it when the"
- **Our assessment**: The quote is a short fragment because the gate names sit in separate inline-code elements; the full sentence reads (rendered) "`skip-if-check-failing` pauses it when the `build`, `test`, `lint-go` or `lint-js` checks are red." A concrete named use of declarative, zero-model-token gates. Nothing here verifies the gate behavior; the audited run happened to execute, so it only shows the gates passed.

### Claim 4: A pre-step script searches for candidates and checks recent Copilot PRs for rate-limit signals, so the agent sees only a short prepared list
- **Evidence**: Prose description.
- **Confidence**: anecdotal
- **Quote**: "so the agent only sees a short, prepared list."
- **Our assessment**: Matches the rate-limit scan in `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 3 and the precompute pattern in `docs-ghaw-deterministic-agentic-patterns.md` Claim 1. Slight internal tension: "short" list, yet the post later attributes medium token usage to "a roughly 36 KB prompt that carries the candidate list" (Claim 7). 36 KB is short relative to the repo, not small in token terms.

### Claim 5: One audited scheduled run (39438401745) succeeded in 7.9 minutes, 4 turns, about 62k tokens, 0 errors / 0 warnings, 19 firewall requests allowed and 0 blocked, on the Pi engine with `copilot/gpt-5`
- **Evidence**: Audit table in the post.
- **Confidence**: anecdotal (n=1, vendor-reported, aggregate only)
- **Quote**: "4 turns, about 62k tokens"
- **Our assessment**: A checkable datapoint. For scale, `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 4 reports 350k tokens across five runs (about 70k average), so 62k per write-capable run is in the same range. The 08-25 figure is across mixed read-only and write runs, so the comparison is loose. Engine choice (Pi on `copilot/gpt-5`) is a new datapoint for this workflow.

### Claim 6: The run made six safe-output calls (three `assign_to_agent`, three `add_comment`); the single MCP server `safeoutputs` reported 6 requests and no errors
- **Evidence**: Prose after the audit table; comments landed on #70227, #69063 and #68043.
- **Confidence**: anecdotal
- **Quote**: "The agent made six safe-output calls:"
- **Our assessment**: Three assignments in one run is a second datapoint for the batched side of open contradiction #2979 (first was run 32856106356 in the 08-25 note). It is consistent with `assign-to-agent` `max: 3`, but the post never states the cap, never says the three issues were topic-separated, and does not name the assigned issues, so it cannot confirm the topic-separation mechanism and does not resolve the contradiction. Also, the three comments went to three issues; the post does not say whether those are the same issues assigned. The post's own "in order" framing (Claim 8) sits uneasily beside a three-at-once run.

### Claim 7: The audit compared the run with an earlier successful run (39433043735); everything matched except turn count, flagged as "worth a glance rather than a problem", and token usage was rated medium severity because of a roughly 36 KB prompt
- **Evidence**: Audit-comparison prose.
- **Confidence**: anecdotal
- **Quote**: "which the audit flagged as a change worth a glance rather than a problem"
- **Our assessment**: Another instance of the baseline-diff audit pattern seen in `blog-ghaw-agent-of-the-day-2026-10-19.md` Claim 6. The post does not give the earlier run's turn count, so the size of the change is unknown. The claim that prompt size drives token use is stated as plausible ("which makes sense given"), not measured.

### Claim 8: Issue Monster works "politely and in order", and its writes are narrow (comments and assignments via safe outputs)
- **Evidence**: Narrative framing in intro and "Why it matters"; no ordering mechanism shown.
- **Confidence**: anecdotal (rhetorical)
- **Quote**: "Issue Monster’s gates keep the queue of draft PRs short, avoid rate-limited moments and stay quiet while CI is failing."
- **Our assessment**: "In order" is flavor text, not evidence of serialization. The concrete evidence in the same post (three assignments in one run) points toward batching. The narrow-writes point is consistent with the safe-outputs model in the 08-25 note, though Claim 5 there shows the job-level permissions are broader than the post's description of the agent. Note the quote contains a typographic apostrophe copied from the source.

## Concrete Artifacts

Audit table, from the post (run 39438401745, scheduled, on `main`):

```
Measure             Value
Conclusion          Success
Duration            7.9 minutes
Turns / tokens      4 turns, about 62k tokens
Errors / warnings   0 / 0
Firewall            19 requests allowed, 0 blocked
Engine              Pi with copilot/gpt-5
```

Gate summary as described in prose (not verbatim config; frontmatter not shown in the post):

```
schedule: every 30 minutes + workflow_dispatch
skip if >=5 open Copilot draft PRs (excluding label "broccoli")
skip-if-no-match: requires >=1 open issue
skip-if-check-failing: build, test, lint-go, lint-js
pre-step: candidate search + rate-limit scan of recent Copilot PRs
safe outputs used in run: assign_to_agent x3, add_comment x3
```

## Cross-References

- **Corroborates**: `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 2 (same three gates) and Claim 3 (rate-limit pre-scan); Claim 4 (token scale); Claim 6 (up to three assignments per run, `max: 3`) now has a second observed 3-assignment run. `docs-ghaw-deterministic-agentic-patterns.md` Claim 8 (`skip-if-no-match` gating). `blog-ghaw-agent-of-the-day-2026-10-19.md` Claim 2 (skip-if-no-match gate) and Claim 6 (diff against previous run).
- **Contradicts:** Existing open contradiction #2979 (Issue Monster dispatch: strict one-at-a-time per `blog-ghaw-issue-pr-mgmt.md` Claim 2 vs batched up to three per `blog-ghaw-agent-of-the-day-2026-08-25.md` Claim 6). This post is one datapoint on the batched side (three `assign_to_agent` in one run); it does not state the cap or topic separation, and its "in order" wording is non-specific. No new contradiction filed and no verdict picked here.
- **Extends**: `blog-ghaw-agent-of-the-day-2026-08-25.md` (adds one audited run, the `broccoli` exclusion, and the Pi / `copilot/gpt-5` engine); `blog-ghaw-agent-of-the-day-2026-09-15.md` Claim 10 and `blog-ghaw-agent-of-the-day-2026-08-28.md` (`cookie` queue feeds Issue Monster; this post does not mention the `cookie` label, so that dependency is not re-confirmed).
- **Novel**: Run-level audit numbers for Issue Monster (7.9 min, 4 turns, ~62k tokens, 19 allowed / 0 blocked firewall requests); the Pi + `copilot/gpt-5` engine for this workflow; the statement that a ~36 KB prompt drives medium-severity token usage.

## Guide Impact

- **Chapter 02**: Issue Monster's gating (draft-PR cap, `skip-if-no-match`, `skip-if-check-failing`, pre-step candidate list) can be cited as a concrete deterministic-pre-check example, but this adds nothing beyond the 08-25 note's Claim 2; cite that note first and this one only for the `broccoli` exclusion and the run audit. Do not describe the gates as verified beyond the post's prose.
- **Chapter 04**: If a scheduled dispatch agent cost profile is given, "~62k tokens and 7.9 minutes for a write-capable 30-minute run (one run, vendor-reported)" is a usable illustrative figure, labeled n=1. Any text that says Issue Monster dispatches strictly one at a time should wait for the resolution of #2979; this post adds a second observed three-assignment run in favor of the batched reading.

## Extraction Notes

- Read the full post (short; one workflow, one table). The page text was fetched directly and the audit table and prose read in full.
- Cross-reference claim numbers were verified against the headings in the cited source notes (08-25 Claims 1-6, issue-pr-mgmt Claim 2, deterministic-patterns Claims 1 and 8, 10-19 Claims 2 and 6, 09-15 Claim 10).
- Contradiction #2979 already exists (open); no new contradiction issue was filed.
- Quotes were copied from the rendered page; where the source splits a sentence across inline-code elements, only the contiguous plain-text fragment is quoted.
