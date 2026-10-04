---
source_url: https://simonwillison.net/2026/Sep/27/bluesky-bot-check/
source_type: blog-post
title: "Bluesky reply bot checker"
author: Simon Willison
date_published: 2026-09-27
date_extracted: 2026-10-04
last_checked: 2026-10-04
status: current
confidence_overall: anecdotal
issue: "#3888"
---

# Bluesky reply bot checker

> A short tool-announcement post (plus a linked prompt transcript PR) showing a vibe-coded, single-HTML-file investigation tool whose spec explicitly requires it to "reveal its working" so it does not accuse people without justification.

## Source Context

- **Type**: blog-post (short "Tool" entry; the linked tools PR holds the actual prompts)
- **Author credibility**: Simon Willison, co-creator of Django and Datasette, prolific documenter of LLM-assisted development; speaking here from first-hand experience as a high-follower account targeted by reply bots.
- **Scope**: Post is ~5 short paragraphs: motivation, the tool, the signals it checks. Does not describe the code, the thresholds, or any validation of detection accuracy. The prompt text is in https://github.com/simonw/tools/pull/348 (read; PR body = the prompts, 2 files: `bluesky-bot-check.html` +2080 lines, `tests/test_bluesky_bot_check.py` +335 lines). The tool itself is at https://tools.simonwillison.net/bluesky-bot-check.

## Extracted Claims

### Claim 1: Reply bots have spread from Twitter to Bluesky, and Bluesky's open API makes investigating them tractable
- **Evidence**: Author's first-hand experience as a high-follower account; no measurements.
- **Confidence**: anecdotal
- **Quote**: "Unlike Twitter, Bluesky still has a freely available and useful API."
- **Our assessment**: Plausible and unquantified. Relevant as a "what AI-generated spam looks like in the wild" data point; the API-availability point explains why the tool is feasible as a client-only page.

### Claim 2: The tool was produced by prompting Opus 5.5 to "vibe code" it rather than hand-writing it
- **Evidence**: Linked PR contains the prompt and a Claude Code session link; PR adds a 2,080-line HTML file and a 335-line Python test file.
- **Confidence**: settled (as a statement of how this artifact was made)
- **Quote**: "So I had Opus 5.5"
- **Our assessment**: Notable that even in "vibe coding" the PR includes a test file — consistent with Willison's stance that tests are cheap to generate but not a trust signal (see cross-references). The post doesn't say whether he reviewed the code.

### Claim 3: Detection relies on simple behavioral heuristics: reply latency, reply-only accounts, and question marks
- **Evidence**: Description of the tool's signals; no precision/recall data provided.
- **Confidence**: anecdotal
- **Quote**: "replies posted within seconds of other posts from the same account"
- **Our assessment**: Heuristics are cheap and explainable but unvalidated; a human power-replier could trip some. The post does not claim accuracy.

### Claim 4: Reply-only accounts that target higher-follower users are a bot signal
- **Evidence**: Stated as a design signal; PR prompt adds "Yea to considering follower count of parents".
- **Confidence**: anecdotal
- **Quote**: "accounts that never post their own content (or images or links) but instead consistently reply to messages from other, higher-follower users"
- **Our assessment**: Reasonable heuristic; a feature of engagement-farming economics rather than of LLMs per se.

### Claim 5: Personal annoyance drives a specific signal — questions that no human asked
- **Evidence**: Author's stated motivation.
- **Confidence**: anecdotal
- **Quote**: "It also looks for question marks, because I'm extra infuriated by reply bots that trick me into wasting my time answering a question that no human ever posed."
- **Our assessment**: Illustrates that vibe-coded tools are built to the builder's own pain point; a one-user spec is enough to start.

### Claim 6: A tool that makes accusations should show every measurement and rule so the user can verify the reasoning
- **Evidence**: Stated in the post's description and as a hard requirement in the prompt.
- **Confidence**: emerging
- **Quote**: "The tool displays every measurement and rule so you can verify the reasoning and see example replies that triggered the most signals."
- **Our assessment**: Strongest transferable pattern: put an explainability requirement in the spec for any LLM-built classifier. Prompt version: "The tool must reveal its working, it needs to be very clear about the signals it uses so it doesn't accuse people without justification".

### Claim 7: Brainstorming signals with the model before building improves the spec (interactive scoping)
- **Evidence**: The PR prompt ends the first message with a question, and the second message answers the model's proposals.
- **Confidence**: anecdotal
- **Quote**: "Before we start building, any suggestions for more signals?"
- **Our assessment**: A concrete example of a "plan before build" turn: the human accepts some model suggestions ("Yes scan 1000 - and yes to account age, quiet window, and length consistency") and rejects others ("Don't bother with those LLM style markers yet"), keeping scope controlled. The post itself doesn't discuss this; it's visible only in the PR.

## Concrete Artifacts

Prompt, first turn (from https://github.com/simonw/tools/pull/348, PR body):

```
> Build a tool to help evaluate if a user on Bluesky is likely an AI reply bot (inspired by previous bluesky tools in this repo)
>
> It should start by showing their follow and follower counts, and how many posts they have made...
> It should evaluate their replies. I want it to list their most recent 50 replies to other people and for each one note:
> - how long after the original post was the reply sent?
> - does the reply include a question mark?
> - time of day - I want to spot if accounts post 24 hours a day or if they have more human looking patterns
>
> Before we start building, any suggestions for more signals?
```

Second turn (same PR), including the output-structure requirement:

```
> Build this tool so it starts with headline stats and a one paragraph of why the tool thinks it may be a bot (or not), then it shows some examples of recent bot-like replies, then it has much more detail, and it finishes with all of the recent posts and replies with an indicator on each one for if it has bot signals
>
> The tool must reveal its working, it needs to be very clear about the signals it uses so it doesn't accuse people without justification
```

Model attribution in PR: "Claude Opus 5.5". Prompt also anchors on existing repo tools ("inspired by previous bluesky tools in this repo").

## Cross-References

- **Corroborates**: `blog-simonwillison-rss-vibe-coded-apps.md` Claim 2 (vibe-coded apps are personal and situated) and Claim 5 (individual portfolios of many small tools) — this is another instance of a one-off tool built for a personal pain point.
- **Contradicts**: None found. Mild tension worth noting, not a contradiction: `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 4 says artifacts like test suites aren't reliable quality signals, yet this tool ships with one; the post doesn't say how it was validated.
- **Extends**: `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 5 (sustained use as the quality signal) — here the explainability requirement is a way to let users judge a tool's output without trusting the code.
- **Novel**: (a) Explicit "reveal its working" requirement for an LLM-built accusatory classifier; (b) a worked example of a plan-then-build prompt pair with a public PR transcript; (c) AI-reply-bot detection as a use case.

## Guide Impact

- **Ch02/Ch03 (vibe coding / rapid tool building)**: Candidate short example: an end-to-end prompt pair (spec + "any suggestions?" scoping turn + decision turn) from PR #348. Weak evidence (single anecdote), so use as illustration only.
- **Spec-writing guidance**: Add the pattern "for tools that judge people/content, require the output to show its inputs and rules" citing Claim 6.
- **AI misuse section (if present)**: Cite as a one-line example of AI reply spam on Bluesky; no measured prevalence is given, so don't cite for statistics.

## Extraction Notes

- Source is very thin (about five paragraphs). Read in full via raw HTML, and followed the one substantive link (simonw/tools PR #348) for prompts. The tool page was fetched but its 2,000-line source was not audited, so claims about the detection logic come only from the post and prompts.
- The Prospector comments mention reply timing "seconds between posts", "question marks", etc.; all are verified in the post. Claims in the triage about "behavioral tricks" or rapid-iteration speed are not supported by the post text and were not extracted.
- No contradictions filed.
