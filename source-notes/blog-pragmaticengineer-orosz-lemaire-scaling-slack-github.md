---
source_url: https://newsletter.pragmaticengineer.com/p/scaling-slack-and-github-with-maude
source_type: blog-post
title: "Scaling Slack and GitHub with Maude Lemaire"
author: Gergely Orosz (The Pragmatic Engineer), guest Maude Lemaire
date_published: 2026-11-05
date_extracted: 2026-11-06
last_checked: 2026-11-06
status: current
confidence_overall: anecdotal
issue: "#4555"
---

# Scaling Slack and GitHub with Maude Lemaire

> A podcast write-up whose only AI-native content is one practitioner stance: for platform ("foundational") work, the guest personally verifies everything an LLM produces, while a platform/product engineer rotation is proposed for org design.

## Source Context

- **Type**: blog-post (Pragmatic Engineer podcast episode page: summary, takeaways, timestamps; full discussion is in the audio/video).
- **Author credibility**: Host Gergely Orosz (see other `blog-pragmaticengineer-*` notes). Guest Maude Lemaire spent nearly eight years at Slack leading backend performance infrastructure, joined GitHub in 2024, and most recently worked on performance (including time to first token) at Cursor.
- **Scope**: Mostly pre-AI infrastructure scaling (Slack, GitHub Rails monolith, load testing). The AI content is one takeaway plus a "How Maude uses AI" timestamp (1:02:26). The page text does not contain the transcript, so the reasoning behind the AI stance is not available to this extraction.

## Extracted Claims

### Claim 1: For platform work, the guest personally verifies everything she gets from an LLM
- **Evidence**: Self-reported practice of a senior performance/platform engineer; no metrics.
- **Confidence**: anecdotal
- **Quote**: "For platform work, Maude personally verifies everything she gets from an LLM."
- **Our assessment**: A clear instance of risk-tiered verification: verification effort scales with the blast radius of the code. It matches the tiered review pattern in other notes, but here it is one person's practice and the page gives no detail on how she verifies.

### Claim 2: Foundational work gets more scrutiny than non-foundational work
- **Evidence**: Stated rationale (paraphrased by the page), no data.
- **Confidence**: anecdotal
- **Quote**: "ambitious structures can only be built on stable foundations"
- **Our assessment**: The principle is plausible and consistent with risk-stratified review. It does not define "foundational" operationally. Use it as framing, not as a rule.

### Claim 3: Platform and product engineers should rotate more
- **Evidence**: Guest's observation that the best platform engineers were product engineers who rebuilt similar features repeatedly and then built tools to remove the repetition. Platform engineers can drift from the product experience.
- **Confidence**: anecdotal
- **Quote**: "Platform and product engineers should rotate more."
- **Our assessment**: Org-design opinion that is not AI-specific. Marginal relevance to team adoption.

### Claim 4: Naive load testing of 500,000 WebSocket connections would have been prohibitively expensive, so Slack built a lightweight client simulator (Koi Pond)
- **Evidence**: Specific cost figure and tool name from the guest's Slack experience.
- **Confidence**: anecdotal
- **Quote**: "Load testing 500,000 WebSocket connections the simple way would have cost $150,000 per run."
- **Our assessment**: Not an AI claim. Possible indirect hook: simulated clients for agentic workloads face similar cost pressures. The source does not make that argument.

### Claim 5: Design limits can be deliberate protections against load spikes
- **Evidence**: Slack's custom emoji cap, as cited in the takeaways.
- **Confidence**: anecdotal
- **Quote**: "Slack limits custom emojis to 23 to avoid thundering herds."
- **Our assessment**: Not AI-related; out of scope for the guide.

### Claim 6: Database sharding at GitHub was bounded by scatter queries
- **Evidence**: Takeaway list only.
- **Confidence**: anecdotal
- **Quote**: "GitHub could not add more than 16 database shards because of scatter query problems."
- **Our assessment**: Not AI-related; out of scope.

## Concrete Artifacts

```
Takeaway list (Pragmatic Engineer episode page):
- "Performance should matter even if there’s no competition."
- "For platform work, Maude personally verifies everything she gets from an LLM."
- "Platform and product engineers should rotate more."

Timestamps: 1:02:26 "How Maude uses AI"; 1:12:40 "Advice for engineers interested in product/platform work"
```

## Cross-References

- **Corroborates**: `blog-pragmaticengineer-orosz-slow-down-speed-up.md` (Claim 10: OpenAI's Codex team uses a tiered review system where only higher-risk changes get human review). Lemaire's foundational/non-foundational split is the same risk-tiering idea applied to one person's own LLM output.
- **Contradicts**: none found.
- **Extends**: `blog-pragmaticengineer-orosz-code-review-approaches.md` (verification and judgment theme) with one more practitioner data point.
- **Novel**: Perf-infrastructure practitioner view on verification; load-testing cost anecdotes (non-AI).

## Guide Impact

- **Chapter 03**: At most, add Lemaire as a single anecdotal example that verification effort should be tiered by how foundational the code is. Do not rely on it as a primary citation.
- **Chapter 05**: The platform/product rotation idea is too thin and non-AI to change guidance.

## Extraction Notes

- Only the public episode page was read (fetched twice with different prompts). It contains the summary, takeaways and timestamps; no transcript. The AI discussion at 1:02:26 was not accessible, so the how and why of her verification is unknown.
- The fetch tool summarizes pages, so quotes were taken from its extraction of the takeaways list; the Assayer should spot-check them against the live page.
- Slack/GitHub scaling material was deliberately skipped per the triage guidance.
- Confidence is anecdotal; this is a low-priority note.
