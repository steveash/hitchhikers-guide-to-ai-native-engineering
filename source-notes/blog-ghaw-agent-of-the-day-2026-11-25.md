---
source_url: https://github.github.com/gh-aw/blog/2026-11-25-agent-of-the-day/
source_type: blog-post
title: "Agent of the Day – November 25, 2026: Archivx Workflow Visualizer (86 turns, 8.78M tokens; ~96% of turns estimated as deterministic data gathering)"
author: GitHub Agentic Workflows team (gh-aw), bylined "Copilot"
date_published: 2026-11-25
date_extracted: 2026-11-26
last_checked: 2026-11-26
status: current
confidence_overall: anecdotal
issue: "#4965"
---

# Agent of the Day – November 25, 2026: Archivx — Workflow Visualizer

> A first-party single-run profile of a weekly diagram-drawing workflow whose audit estimates ~96% of 86 turns were data gathering that could be deterministic, even though a setup step already pre-downloads the logs.

## Source Context

- **Type**: blog-post (first-party gh-aw "Agent of the Day" entry, bylined "Copilot"; filed as `documentation`, triaged as text). Narrated by a fictional "Wren Halvorsen" cartographer persona, which is framing, not evidence.
- **Author credibility**: Official gh-aw blog. Run ID, PR #80342 and discussion #80343 are cited; not independently verified here. Metrics are vendor-reported from one run.
- **Scope**: One workflow (`.github/workflows/archivx-agentic-workflows-analyzer.md`), one run (45138657416), six audit findings. Does NOT show the prompt, a per-turn breakdown, the tool-call mix, or any applied fix. The post does not say what the data-gathering turns fetched.

## Extracted Claims

### Claim 1: The workflow pre-downloads seven days of logs in a setup step, then the agent draws an SVG, with tightly bounded outputs
- **Evidence**: Post's description of the workflow definition (not shown).
- **Confidence**: anecdotal
- **Quote**: "Before the agent starts, a setup step downloads seven days of agentic workflow logs."
- **Our assessment**: Good example of a declared, narrow output surface (at most one discussion, a draft PR limited to `docs/src/assets/archivx/*.svg`). It also sets up the puzzle in Claim 3: the data is already local, yet the agent used 86 turns.

### Claim 2: One scheduled run took 86 turns, 8,775,485 tokens, 250.2 AIC and 28.7 minutes, with zero errors
- **Evidence**: Run table for run 45138657416 (2026-11-23, scheduled, `main`): Turns 86; Tokens 8,775,485; AIC 250.2; Action minutes 29; Errors / warnings 0 / 0; created 1 pull request, 1 discussion.
- **Confidence**: anecdotal (vendor-reported, single run)
- **Quote**: "Its latest scheduled run took 28.7 minutes and 86 turns."
- **Our assessment**: Roughly 102k tokens per turn by our arithmetic (8,775,485 / 86), which is above the 56k–77k per turn in the 2026-11-17 note (Claim 3). The comparison is ours; sample sizes are tiny. The run was green and delivered a merged PR, so the cost is for a successful outcome.

### Claim 3: The audit estimates about 96% of turns were data gathering that could move into deterministic steps
- **Evidence**: Audit finding quoted in the post; method not shown. The post says it is not a measurement.
- **Confidence**: anecdotal (audit estimate, n=1)
- **Quote**: "The audit estimates that about 96% of the run’s turns were data gathering that could move into deterministic steps."
- **Our assessment**: Higher than the 77–91% range in the 2026-11-17 note (Claim 5). Interesting because the setup step already fetches logs, so the turns must have been doing something else (further filtering, per-run lookups, reading skills?). The post leaves this open and no one tested a scripted variant. Treat as a lead, not proof.

### Claim 4: The post flags the 96% figure as unverified and worth checking in the next iteration
- **Evidence**: Author's own caveat.
- **Confidence**: anecdotal
- **Quote**: "That is an audit estimate, not a measurement, and it is worth checking in the next iteration."
- **Our assessment**: Honest labeling; keep this caveat attached anywhere the 96% is cited. The post says "what those turns were still gathering" is an open question.

### Claim 5: The audit raised six findings including high tokens, a blocked-domain access attempt, resource-heavy profile and weak agentic control
- **Evidence**: Audit findings listed in the post.
- **Confidence**: anecdotal
- **Quote**: "It marked the execution profile as resource heavy for its task shape, and it rated agentic control as weak because the run showed signs of broad or weakly controlled behavior."
- **Our assessment**: Post names four of the six (high tokens / 86 turns read as complexity or unclear instructions, blocked domain `clients2.google.com`, resource heavy, weak control) plus the 96% finding; the sixth is not clearly itemised, so we do not infer it. The blocked-domain attempt is notable: a firewall/allowlist blocked it, yet the run was green with 0 errors/warnings, so a green status hid an egress attempt.

### Claim 6: High turn count is read by the audit as task complexity or unclear instructions
- **Evidence**: Audit interpretation in the post.
- **Confidence**: anecdotal
- **Quote**: "the 86 turns were read as a sign of task complexity or unclear instructions"
- **Our assessment**: A generic heuristic; the post does not say which applied here. Pairs with Claim 3 to suggest "unclear instructions" could mean the agent was told to explore rather than handed prepared data.

### Claim 7: The visible output was a draft PR (#80342) that merged the same day
- **Evidence**: PR title "[archivx] Update workflow diagram — 2026-11-23", merged 12:55 UTC; discussion #80343.
- **Confidence**: anecdotal
- **Quote**: "The pull request was merged at 12:55 UTC the same day."
- **Our assessment**: Output was accepted, so the expensive run was useful. Cost-reduction advice should be weighed against that: the problem is efficiency, not failure.

### Claim 8: Spotlight selection skips workflows without trustworthy run evidence
- **Evidence**: Post lists five skipped workflows (ace-editor, agentic-token-trend-audit, agy-conformance-reusable, approach-validator, archie) whose latest runs were zero-turn push failures or never executed.
- **Confidence**: anecdotal
- **Quote**: "Archivx had no spotlight in any earlier post, and it was the first never-featured workflow with a trustworthy run record."
- **Our assessment**: Same selection rule as earlier series notes, so the series over-represents workflows that actually ran and spent tokens.

## Concrete Artifacts

Run metrics as reported in the post (vendor-reported, single run):

```
Workflow:        .github/workflows/archivx-agentic-workflows-analyzer.md
Schedule:        weekly, Mondays ~09:00
Run:             45138657416 (scheduled, main), started 08:26 UTC 2026-11-23
Duration:        28.7 minutes, concluded successfully
Turns:           86
Tokens:          8,775,485
AIC:             250.2
Action minutes:  29
Errors/warnings: 0 / 0
Created items:   1 pull request (#80342), 1 discussion (#80343)
Safe-output bounds: at most one discussion; draft PR limited to docs/src/assets/archivx/*.svg
Blocked domain attempted: clients2.google.com
Audit estimate:  ~96% of turns = data gathering movable to deterministic steps
```

## Cross-References

- **Corroborates**: `blog-ghaw-agent-of-the-day-2026-11-17.md` (Claim 3: token use tracks turns so turn count is the cost lever; Claim 5: audit estimates a large share of turns is scriptable data gathering). `blog-ghaw-agent-observability.md` (Claim 4: cost-optimisation agents can identify expensive LLM call patterns).
- **Contradicts**: none found; no contradiction issue filed.
- **Extends**: `blog-ghaw-agent-of-the-day-2026-11-17.md` Claim 5: 96% is higher than 77–91%, and here the logs were already pre-downloaded in a setup step, so pre-fetching alone did not remove the data-gathering turns. `blog-ghaw-agent-of-the-day-2026-11-24.md` (Claim 8: weak agentic control flag; here it co-occurs with a useful merged output rather than an unverifiable one).
- **Novel**: Archivx workflow and run 45138657416; the "setup step already downloads logs yet turns remain mostly data gathering" puzzle; blocked-domain attempt (`clients2.google.com`) in an otherwise clean green run.

## Guide Impact

- **Chapter 04 (context engineering)**: Add as an anecdotal example that pre-fetching data in a setup step is not sufficient; audit for what the agent still fetches. Cite the 96% as an unverified audit estimate from one run.
- **Chapter 02 (harness engineering)**: Example of a narrowly declared output surface (one discussion, SVG-only draft PR) alongside a high turn budget; supports per-workflow turn/token tracking.
- **Chapter 03 (verification)**: A green run with 0 errors can still contain a blocked-egress attempt and a "weak agentic control" flag; audit signals are separate from run status.
- **Chapter 05 (adoption/cost)**: 8.78M tokens / 250.2 AIC per week for one diagram workflow is an illustrative cost data point; the sizing is vendor-reported, n=1.

## Extraction Notes

- Fetched the raw page and stripped tags; read the full post (short, no substantive sub-pages). Quotes copied from stripped text with curly apostrophes preserved; Claim 6 quote is a fragment from a longer sentence.
- Triage comments asked for a "six audit flags" list; the post's prose clearly names high tokens, blocked domain, resource heavy, weak control and the 96% finding, so the sixth is not asserted here.
- Chapter mapping differed across triage comments and is not confirmed against the guide.
- Claim numbers cited in other notes were checked against their headings (2026-11-17 Claims 3, 5; observability Claim 4; 2026-11-24 Claim 8).
- Persona "Wren Halvorsen" not used as attribution. Run ID/PR numbers not independently verified.
