---
source_url: https://hamel.dev/blog/posts/claude-auto-evals/
source_type: blog-post
title: "Claude's new auto eval tool"
author: Hamel Husain
date_published: 2026-09-30
date_extracted: 2026-10-01
last_checked: 2026-10-01
status: current
confidence_overall: anecdotal
issue: "#3837"
---

# Claude's new auto eval tool

> Hamel Husain's hands-on review of Anthropic's `build_eval` / `hill-climb` plugin commands: strong one-shot issue discovery, but a workflow that commits to evaluators before the user has looked at data — with the principle that an eval tool must put looking at data at the center of the workflow.

## Source Context

- **Type**: blog-post (personal blog, hamel.dev, September 30, 2026; tool review)
- **Author credibility**: Hamel Husain is an applied-AI/evals practitioner and educator (see [blog-hamel-eval-smell.md](blog-hamel-eval-smell.md)). He co-authored the "Eval skills" he compares against, so he is not a neutral reviewer of competing tooling; he says so implicitly ("these Eval skills Shreya and I put together").
- **Scope**: One livestreamed session (with Isaac Flath) on conversation traces from an apartment leasing assistant (voice agent). Covers the plugin's call-transfer eval workflow only. No quantitative results; screenshots are not reproduced here. The Anthropic announcement post (claude.dev/blog/automating-eval-design-and-hillclimbing/) was not mined here; the review itself describes it. The author says the plugin's author will update it, so the critiques may be stale quickly.

## Extracted Claims

### Claim 1: The plugin pushes users to commit to an eval before they have looked at the data
- **Evidence**: Livestream observation: Claude proposed a menu of potential failures (call-transfer rules recommended) and asked the user to pick one immediately; the authors went with the recommendation as a typical user would.
- **Confidence**: anecdotal
- **Quote**: "We hadn’t yet reviewed the conversations ourselves, so it was hard to know if this was a real failure or worth prioritizing."
- **Our assessment**: Credible single-session observation of a design choice, and consistent with the data-first eval doctrine. Whether it is still true after the promised update is unknown.

### Claim 2: Agents can help find issues, but error analysis is still needed to decide which failures deserve evals
- **Evidence**: Author's stated belief; links to his error-analysis FAQ.
- **Confidence**: emerging
- **Quote**: "An agent can help you find issues, but you still should do"
- **Our assessment**: Quote is a fragment (link text follows in the source: error analysis). The position is a core part of the author's eval methodology; it is asserted, not tested here.

### Claim 3: Asking humans to validate labels in an editor/chat loop is poor design for a coding agent, which should build an annotation UI
- **Evidence**: Claude asked them to skim `inputs.md` and "tell it" which labels were wrong; they eventually asked Claude to build a web app and used it instead.
- **Confidence**: anecdotal
- **Quote**: "We found this very silly as we were using a coding agent, so it should have built an annotation app that made the conversations easy to read and let us leave feedback in-situ."
- **Our assessment**: Practical and actionable; also shows the workaround (ask the agent to build the review app) is cheap.

### Claim 4: The workflow repeatedly asks for approval without giving enough context to judge
- **Evidence**: Claude presented aggregate label counts and asked "Would you have scored any case differently?"
- **Confidence**: anecdotal
- **Quote**: "A recurring theme of the workflow was to jump too fast into creating artifacts or asking us for approval without helping us understand the data."
- **Our assessment**: A generalizable failure mode of agentic human-in-the-loop checkpoints: approval requests without evidence become rubber stamps.

### Claim 5: The generated evaluator bundled four failure checks (mixed LLM-judge and code-based) into one score
- **Evidence**: Four checks listed: repeated/missing confirmation (LLM judge); speech between consent and transfer, speech during/after transfer, and tool mechanics spoken aloud (code-based). A case passes only if all four pass (`protocol_ok`).
- **Confidence**: anecdotal
- **Quote**: "There were too many things bundled into this evaluator."
- **Our assessment**: Matches common eval practice (one failure mode per evaluator; separate deterministic checks from LLM judges). A single headline pass/fail hides which check fails.

### Claim 6: Prefer evaluators scoped to one error at a time, or at least split by code-based vs. LLM-as-judge
- **Evidence**: Author preference, no experiment.
- **Confidence**: emerging
- **Quote**: "I would prefer to scope the eval to focus on one error at a time, or at the very least separate the evals into those that needed a code-based eval vs a LLM as a Judge."
- **Our assessment**: Widely held heuristic; a reasonable default.

### Claim 7: Prose descriptions of an evaluator are less useful than the code or judge prompt; always read the prompt
- **Evidence**: Quoted Claude description of `protocol_ok` judged unreadable; links to the author's earlier post on reading prompts.
- **Confidence**: anecdotal
- **Quote**: "I’d much rather see the code or the judge prompt so I can understand whats being created."
- **Our assessment**: Sound: the evaluator is itself an artifact to be reviewed, and summaries by the same model that wrote it are weak evidence of what it does.

### Claim 8: Out-of-the-box issue discovery was the strongest the author has seen for one-shot approaches
- **Evidence**: Found issues with human handoff, formatting, voice agents, and more; compared to other auto-eval approaches (linked Parlance Labs post). No counts or precision measurements.
- **Confidence**: anecdotal
- **Quote**: "this was the strongest performance I’ve seen with a more “one-shot” issue discovery approach."
- **Our assessment**: Notable positive from a skeptical reviewer, but unquantified and from one dataset.

### Claim 9: Anthropic's announcement reflects sound eval thinking (look at data, sample intelligently, don't saturate evals)
- **Evidence**: Author's reading of the Anthropic blog post.
- **Confidence**: anecdotal
- **Quote**: "such as the importance of looking at data, sampling intelligently, not saturating your own evals, etc."
- **Our assessment**: Implies the gap is between Anthropic's stated philosophy and the plugin's actual workflow. Worth checking in a separate note on the announcement post.

### Claim 10: Eval workflow should largely live in a web application rather than chat, and a tool not centered on data is not worth using
- **Evidence**: Conclusion drawn from the session; author's recommendation. He would hold off adopting and prefers his less opinionated Eval skills.
- **Confidence**: emerging
- **Quote**: "Remember, if an eval tool doesn’t put looking at data at the center of your workflow, it’s not worth using."
- **Our assessment**: Strong stance from an interested party; useful as a checklist criterion for evaluating eval tooling.

## Concrete Artifacts

Menu/evaluator structure described in the post (paraphrased list, attributed to Hamel Husain's account of the plugin output):

```
call-transfer evaluator (4 checks, bundled)
1. Asking for confirmation more than once, or transferring without asking for confirmation. (LLM as a Judge)
2. Saying something between the caller’s consent and the transfer. (Code-based eval)
3. Saying something during or after the transfer. (Code-based eval)
4. Saying tool mechanics aloud, such as “triggering” a transfer. (Code-based eval)
```

Plugin Claude's own description of the headline metric (quoted in the post):

```
protocol_ok is the headline. A case passes only if all four checks pass. On “should not transfer” calls, protocol_ok is 1 if no transfer happened.
```

Tool: `claude-api` plugin for Claude Code, commands `build_eval` and `hill-climb`.

## Cross-References

- **Corroborates**: [blog-hamel-eval-smell.md](blog-hamel-eval-smell.md) — Claim 1 and Claim 9 there (design for builder/user verifiability; ask what the user needs to check) align with this post's demand that the tool help users understand data before approving judgments. Same author, so not independent corroboration.
- **Contradicts**: None found.
- **Extends**: blog-hamel-eval-smell.md applies verification-first thinking to a concrete first-party tool; adds the annotation-UI and evaluator-scoping critiques.
- **Novel**: First note in the corpus reviewing an Anthropic eval-generation plugin (`build_eval`, `hill-climb`); the "bundled evaluator" and "approval without context" failure modes of auto-eval tools; the data-first test for eval tools.

## Guide Impact

- **Evals/quality chapter (Ch05 per triage)**: Add a short criteria list for auto-eval tools: lets you explore data before choosing evals; provides in-context annotation UI; one failure per evaluator, code vs. judge separated; exposes evaluator code/prompts. Cite as practitioner-reported, single session (anecdotal).
- **Tooling chapter**: Note that agent-built annotation web apps are a cheap workaround for chat-based review friction.
- Do not make strong claims about the plugin's current behavior; the author expects it to change.

## Extraction Notes

- Read the full post (short, ~700 words) via direct HTML fetch; quotes copied from the page text. Quote in Claim 2 is a fragment ending before a hyperlink.
- Did not fetch linked pages (Anthropic announcement, livestream, Parlance auto-evals post, Eval skills); these are candidates for separate sources. No existing note covers them.
- Screenshots in the source were not visible to extraction.
