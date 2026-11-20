---
source_url: https://github.blog/changelog/2026-11-17-github-copilot-fusion-updates-more-availability-benchmarks-and-models
source_type: docs
title: "GitHub Copilot Fusion updates: more availability, benchmarks, and models"
author: GitHub (official changelog)
date_published: 2026-11-17
date_extracted: 2026-11-20
last_checked: 2026-11-20
status: current
confidence_overall: emerging
issue: "#4853"
---

# GitHub Copilot Fusion updates: more availability, benchmarks, and models

> GitHub's Nov 17, 2026 changelog reports a Terminal-Bench 4.1 public-leaderboard listing for Copilot Fusion Max (71.2% resolution, with vendor-stated cost ratios), expands Fusion to github.com, Visual Studio and GitHub Mobile beta, and adds new models to each tier, showing the tier-to-model mapping is a moving pool.

## Source Context

- **Type**: docs (GitHub official changelog, short entry labeled "Improvement")
- **Author credibility**: GitHub's own changelog. Authoritative for availability and roster changes. Benchmark and cost figures are asserted by the vendor on the page; only the leaderboard listing itself is independently checkable.
- **Scope**: Benchmark listing, surface expansion, model additions per tier, link to Fusion docs. It gives no task set, run count, run configuration, or cost metric/baseline definition. Linked docs and the leaderboards were not followed (the fetch tool summarizes pages and returned only short exact fragments), so the 71.2% figure was NOT verified against the leaderboard.

## Extracted Claims

### Claim 1: Copilot Fusion is listed on public Terminal-Bench 4.1 leaderboards
- **Evidence**: Vendor statement naming three hosts (Stanford, Harbor, Laude Institute). No link details extracted.
- **Confidence**: emerging
- **Quote**: "Copilot Fusion is now listed on Terminal-Bench 4.1 public leaderboards hosted by Stanford, Harbor, and the Laude Institute"
- **Our assessment**: This is the first Fusion benchmark claim in our corpus that points to a public third-party leaderboard, so it is checkable in a way the Artificial Analysis claim (`docs-github-copilot-fusion-ga-oct2026.md` Claim 4) was not. Until someone confirms the entry on the leaderboard (including who ran it and under what harness), treat it as vendor-reported.

### Claim 2: Fusion Max achieved a 71.2% resolution rate, 5.4 points ahead of Opus 5.5 and Fable 5.2
- **Evidence**: Single headline number from the vendor page. No task set, number of runs, confidence interval, or configuration.
- **Confidence**: anecdotal (until verified on the leaderboard)
- **Quote**: "Copilot Fusion Max achieved a 71.2% resolution rate,"
- **Our assessment**: The 5.4-point margin is from the page's summary (the fragment we could quote verbatim covers only the 71.2%). It is a comparison of a routed system against single-model entries; the baselines' harnesses may differ. A margin of this size with no run-count or variance information should not be presented as a decisive ranking.

### Claim 3: Fusion Max cost 88% less than Fable 5.2 and 57% less than Opus 5.5
- **Evidence**: Vendor percentages; cost metric (API list price? average per task? billed?) and baseline configuration are not stated in the fragments extracted.
- **Confidence**: anecdotal
- **Quote**: "while costing 88% less than Fable 5.2 and 57% less than Opus 5.5."
- **Our assessment**: The two baselines give different ratios, so they are separate comparisons and must not be merged with the October "about half the average API cost" figure (different benchmark, different baseline). Since Fusion bills each underlying model leg (`docs-github-copilot-fusion-ga-oct2026.md` Claim 6), these ratios describe benchmark runs, not a user's invoice.

### Claim 4: Fusion is expanding to github.com, Visual Studio and GitHub Mobile beta
- **Evidence**: Vendor availability statement; production mobile apps said to be coming shortly.
- **Confidence**: settled (as stated availability)
- **Quote**: "select Copilot Fusion on the latest versions of github.com, Visual Studio, and GitHub Mobile beta apps"
- **Our assessment**: Supersedes the client list in `docs-github-copilot-fusion-ga-oct2026.md` Claim 7 (VS Code, Copilot app, CLI, JetBrains), adding web, Visual Studio and mobile beta (iOS/Android per the page summary). Also the page's framing line: "Copilot Fusion is coming to more places you use Copilot."

### Claim 5: New models were added to each Fusion tier (Sonnet 5.5 to Max, GPT-6.1 Terra to High, MAI-Code-2 to Standard)
- **Evidence**: Vendor roster statement.
- **Confidence**: settled (as stated roster change)
- **Quote**: "Claude Sonnet 5.5 to Copilot Fusion Max"; "GPT-6.1 Terra to Copilot Fusion High"; "MAI-Code-2 to Copilot Fusion Standard"
- **Our assessment**: The pool listed in `docs-github-copilot-hydrafusion-max-update-oct2026.md` Claim 1 (Opus 5.5, GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna) is now stale. Any model-to-tier mapping in the guide would go out of date within weeks; the guide should describe tiers by intent (cost/quality dial), not by model list. Note that "added to" implies a pool additive change, and the page does not say what role each plays in Single/Cascade/Critique.

## Concrete Artifacts

```
Roster additions (GitHub changelog, 2026-11-17):
Max:      + Claude Sonnet 5.5
High:     + GPT-6.1 Terra
Standard: + MAI-Code-2

Vendor-reported benchmark (Terminal-Bench 4.1 public leaderboards):
Fusion Max resolution rate: 71.2%
Margin: 5.4 points over Opus 5.5 and Fable 5.2 (page summary; not a verbatim fragment)
Cost: 88% less than Fable 5.2; 57% less than Opus 5.5
```

## Cross-References

- **Corroborates**: `docs-github-copilot-fusion-ga-oct2026.md` Claim 4 only in direction (Fusion Max pitched as near/above frontier single-model quality at lower cost); the benchmarks differ and are not comparable.
- **Contradicts**: None. Note the October claim said Fusion Max was within two points of Claude Code + Opus 5.5 Max (i.e., slightly below), whereas this page says Fusion Max is ahead of Opus 5.5 by 5.4 points; the benchmarks (Artificial Analysis Coding Agent Index vs. Terminal-Bench 4.1), harnesses and pools differ, so this is a conditioning difference rather than a contradiction, and no issue was filed.
- **Extends**: `docs-github-copilot-fusion-ga-oct2026.md` Claim 4 (benchmark claim, now with a public leaderboard) and Claim 7 (client availability); `docs-github-copilot-hydrafusion-max-update-oct2026.md` Claim 1 (model pool).
- **Novel**: A public third-party leaderboard reference for Fusion; availability on github.com, Visual Studio and GitHub Mobile beta; Sonnet 5.5, GPT-6.1 Terra and MAI-Code-2 appearing in specific tiers.

## Guide Impact

- **Chapter 02 (model selection / routing)**: If Fusion benchmark figures are cited, use the Terminal-Bench entry as "vendor-reported, listed on public leaderboards", keep it separate from the Artificial Analysis figure, and avoid hard-coding tier-to-model mappings.
- **Chapter 01 (daily workflows)**: Update the surface list for Fusion to include github.com, Visual Studio and GitHub Mobile beta.
- **Chapter 05 (team adoption)**: Note that tier membership changes under the admin's feet; model policies (`docs-github-copilot-fusion-ga-oct2026.md` Claim 5) are the control that bounds which newly added models Fusion can use.

## Extraction Notes

- The fetch tool summarizes and refused full verbatim reproduction; quotes are short fragments returned on a second targeted fetch. The 5.4-point margin and mobile platform detail come from the summary, not a verbatim quote.
- The Terminal-Bench leaderboard was not consulted; the triage key question (run configuration, task set, cost basis) remains open.
- Cross-referenced claim numbers (Fusion GA: Claims 4, 5, 6, 7; Hydrafusion Oct 14: Claim 1) were checked against those notes' headings.
- Triage suggested updating the existing Fusion note; this is a separate note per the Miner task instructions.
