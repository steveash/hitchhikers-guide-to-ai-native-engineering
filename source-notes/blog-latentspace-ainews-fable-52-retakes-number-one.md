---
source_url: https://latent.space/p/ainews-fable-5-2-retakes-world-1-llm-spot-as-ant-ipo-roadshow-begins/
source_type: blog-post
title: "[AINews] Fable 5.2 retakes World #1 LLM spot as $ANT IPO roadshow begins"
author: Latent Space / AINews (swyx daily digest; aggregates tweets, Reddit and vendor/third-party numbers)
date_published: 2026-11-09
date_extracted: 2026-11-22
last_checked: 2026-11-22
status: current
confidence_overall: anecdotal
issue: "#4900"
---

# [AINews] Fable 5.2 retakes World #1 LLM spot as $ANT IPO roadshow begins

> A daily digest whose useful new content for the guide is the per-token vs per-task cost distinction for Fable 5.2 (SemiAnalysis GDPx: $67.16 to $88.15 per task despite a 20% per-token price cut) and community reports that Fable at Max underperforms High.

## Source Context

- **Type**: blog-post (AINews daily digest)
- **Author credibility**: swyx / Latent Space is a well-known AI-engineering outlet, but this is an aggregation of tweets, Reddit posts and third-party benchmark reports, not original measurement. Numbers belong to SemiAnalysis, Anthropic, Vals and Artificial Analysis, as relayed.
- **Scope**: Covers the Fable 5.2 launch aftermath (benchmarks, cost, effort levels, subagent demos, RSI "nerf" discussion, naming, an OpenRouter data-retention policy post). Does not cover methodology of any benchmark.

## Extracted Claims

### Claim 1: Per-token price fell 20% but cost per task rose on SemiAnalysis GDPx ($67.16 to $88.15)
- **Evidence**: SemiAnalysis GDPx (professional-task benchmark) run, relayed by the digest. Fable 5.2 reportedly ranked first at 16.4%; cost per task up ~31%.
- **Confidence**: emerging
- **Quote**: "Yet on GDPx, a benchmark of professional tasks, SemiAnalysis paid $88.15 per task, up from $67.16."
- **Our assessment**: Credible and consistent with the 5.1 digest's finding that output-token volume offsets price cuts. Third-party but not independently verified by us. Practical lesson: compare cost per task, not price per token.

### Claim 2: The cost increase is attributed to Fable 5.2 writing far more tests and spawning verification subagents
- **Evidence**: SemiAnalysis run-log explanation as relayed; Opus 5.5 and Fable 5.1 reportedly stopped at about 20 test cases.
- **Confidence**: anecdotal
- **Quote**: "5.2 sometimes wrote hundreds or thousands and spun up subagents to check its work independently."
- **Our assessment**: Plausible mechanism and relevant to verification chapters: the model's self-verification is both a quality driver and a cost driver. Mechanism is the digest's relay, not our measurement.

### Claim 3: Fable at High matched Opus 5.5 at Max for about half the cost per task
- **Evidence**: Anthropic's FrontierCode 2.0 claim, relayed.
- **Confidence**: emerging (vendor-reported)
- **Quote**: "Fable at High matched Opus 5.5 at Max for about half the cost per task"
- **Our assessment**: Duplicate of the Anthropic launch note (Claim 7) and not independent evidence; the digest just repeats it.

### Claim 4: Max effort on Fable reportedly underperforms High
- **Evidence**: Digest summarises Vals (High best, ahead of xhigh and max), Artificial Analysis and other commenters; one analyst said only Fable models show the dip, not Opus or Sonnet. Commenter @Yuchenj_UW advises against Max.
- **Confidence**: anecdotal
- **Quote**: "Don't use Fable 5.2 Max."
- **Our assessment**: Directionally consistent with Cognition's finding that score can fall with higher effort (cognition-frontiercode-2-0 Claim 9). The "Fable-only" observation is a single analyst's remark. Treat as a hypothesis, not a rule.

### Claim 5: Subagent fleets and orchestrator patterns are the showcased usage
- **Evidence**: Digest cites Anthropic demos (an OS build with 1,000+ subagents over 8 days; a 1,000-agent Fermat's Last Theorem formalization) and one engineer using Fable as orchestrator over Opus 5.5 subagents.
- **Confidence**: emerging
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Corroborates the multi-agent note and the orchestrator guidance in the launch note; digest adds nothing beyond what primary sources give.

### Claim 6: Community claims Anthropic deliberately nerfed RSI capability and that a stronger model remains internal
- **Evidence**: SemiAnalysis / Dylan Patel comments and tweets; Reddit users alleging nerfing and A/B tests in Claude Code.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The deliberate AI R&D limitation is vendor-stated (launch note Claim 11). The Claude Code nerf/A-B allegations are unverified Reddit anecdotes and should not enter the guide.

### Claim 7: The "5.2, not 5.5" naming is read as a marginal improvement
- **Evidence**: Theo, SemiAnalysis and The Rundown commentary as relayed.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Opinion, low value for the guide.

### Claim 8: OpenRouter's CSAM screening may override Zero Data Retention
- **Evidence**: A Reddit post of an OpenRouter policy, relayed; commenters worry about scope expanding to text.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Not confirmed outside the digest. At most a note that ZDR guarantees through routers can have exceptions; verify against OpenRouter's own docs first.

## Concrete Artifacts

```
Per-token price (Fable 5.1 -> 5.2): $10/$50 -> $8/$40 per 1M input/output (-20%)
SemiAnalysis GDPx cost per task:     $67.16 -> $88.15 (about +31%)
GDPx rank: Fable 5.2 first at 16.4%
Test cases per task: ~20 (Opus 5.5, Fable 5.1) vs hundreds/thousands (Fable 5.2, sometimes)
Source: digest relaying SemiAnalysis; the $10/$50 prior price comes from the issue triage, not re-verified
```

## Cross-References

- **Corroborates**: `blog-anthropic-claude-fable-and-mythos-5-2.md` Claim 5 (pricing $8/$40) and Claim 7 (High at about half the cost of Opus 5.5 at Max; Medium default); `blog-cognition-frontiercode-2-0.md` Claim 9 (score can fall with higher reasoning effort); `blog-anthropic-safely-scaling-multi-agent-teams-fable-5-2.md` (1,000-agent runs).
- **Contradicts**: none found. No contradiction issue filed.
- **Extends**: `blog-latentspace-ainews-fable-mythos-51-launch.md` (prior digest on price cuts offset by higher output-token usage) and `blog-simonwillison-fable-end-free-lunch.md` (cost framing and model routing), adding per-task GDPx numbers.
- **Novel**: SemiAnalysis GDPx per-task cost figures and the verification-behaviour explanation; community reports of Max underperforming High on Fable.

## Guide Impact

- **Chapter 01 (model selection / effort)**: If effort guidance is revised, add that Medium/High are recommended defaults and that third-party reports (anecdotal) say Max can underperform High on Fable; cite alongside the Anthropic launch note, flagged as not independently verified.
- **Cost / token economics chapter**: Add the example that a 20% per-token cut coincided with a ~31% per-task cost increase, so budgets should track cost per task (SemiAnalysis via this digest).
- **Verification chapter**: Note that stronger models may self-verify extensively (more tests, verification subagents), trading cost for quality.
- No change recommended from the nerf, naming or OpenRouter material.

## Extraction Notes

- Page fetched via a summarising fetch tool; only the four quoted sentences were returned verbatim and are the only quoted text. Other claims are marked as having no direct quote.
- No sub-pages followed; tweets and Reddit links were not opened, so all claims remain second-hand.
- The prior $10/$50 price is from the triage comment and was not re-checked in the digest.
