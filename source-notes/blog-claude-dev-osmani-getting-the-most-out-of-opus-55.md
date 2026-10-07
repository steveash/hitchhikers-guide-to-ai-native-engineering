---
source_url: https://claude.dev/blog/getting-the-most-out-of-opus-5-5/
source_type: blog-post
title: "Getting the most out of Opus 5.5 in Claude and Claude Code"
author: Addy Osmani (Claude blog)
date_published: 2026-09-22
date_extracted: 2026-10-07
last_checked: 2026-10-07
status: current
confidence_overall: emerging
issue: "#3948"
---

# Getting the most out of Opus 5.5 in Claude and Claude Code

> Official vendor usage guide for Opus 5.5: prompt for a finish line rather than steps, drop "think hard" lines, put stop/continue rules in CLAUDE.md, split large work across subagents, keep the task list in a file, and handle the new model-switch-on-flag behavior.

## Source Context

- **Type**: blog-post (vendor "how to use our model" guide)
- **Author credibility**: Byline is Addy Osmani on the Claude blog, reviewed by Molly Vorwerck. First-party guidance from the model vendor, so authoritative on intended behavior, but claims about "testers" and "our testing" are unquantified.
- **Scope**: Prompting, long-run steering in Claude Code, result checking, Claude apps tips, flagged-message model switching, fast mode. No benchmarks, no cost figures, no code beyond prompt snippets.

## Extracted Claims

### Claim 1: Give the whole task plus an explicit definition of "done" and a narrow stop condition, then let Opus 5.5 run
- **Evidence**: Vendor statement; early-tester anecdote of multi-hour runs; example prompt (see artifacts).
- **Confidence**: emerging
- **Quote**: "Opus 5.5 keeps going on long, multi-part work better than Opus 5 did."
- **Our assessment**: Consistent with the "delegate, don't pair" stance for Opus 4.7. No numbers; the "hours with little oversight" claim is anecdotal.

### Claim 2: "Think carefully"/"think step by step" lines should be removed because Opus 5.5 always thinks before replying
- **Evidence**: Vendor testing in a chat product: replies started sooner, no clear quality drop (no data shown).
- **Confidence**: emerging
- **Quote**: "Opus 5.5 always thinks before it replies, and it decides how much."
- **Our assessment**: Plausible given adaptive thinking; actionable as a cleanup of CLAUDE.md/system prompts. Use effort, not prose, to control depth.

### Claim 3: You can type follow-up messages while a run is in progress, which matters more as runs get longer
- **Evidence**: Feature description.
- **Confidence**: settled
- **Quote**: "Runs are longer now, so a restart costs more."
- **Our assessment**: Small but practical; implies steering mid-run beats restarting.

### Claim 4: For design output, naming specific unwanted patterns works much better than a generic "avoid a generic look"
- **Evidence**: Vendor assertion with an example negative-list prompt.
- **Confidence**: anecdotal
- **Quote**: "A general instruction like "avoid a generic look" mostly swaps one default for another."
- **Our assessment**: Tension with the Opus 4.7 guide's preference for positive examples over "don't" instructions (see Cross-References). Context differs (visual defaults vs. voice/length), so a conditioning variable rather than a contradiction.

### Claim 5: Opus 5.5 sometimes stops to report mid-task, so CLAUDE.md should state when to keep going and when to stop
- **Evidence**: Vendor observation; supplied CLAUDE.md rule.
- **Confidence**: emerging
- **Quote**: "It follows instructions that name these stops."
- **Our assessment**: Valuable and concrete: a failure mode (premature "Want me to continue?") with a config-level fix. Inverse (plan up front, recap at end) is recommended for pair programming.

### Claim 6: Keep guardrails for destructive actions even when telling the model to keep going
- **Evidence**: Vendor caution; the rule's last line limits scope to the repo.
- **Confidence**: settled
- **Quote**: "Keep permission prompts on for destructive commands too."
- **Our assessment**: Sound; pairs autonomy rules with permission-layer enforcement rather than relying on prompt text.

### Claim 7: Ask Opus 5.5 to split audits/migrations across subagents and verify each subagent's evidence before accepting
- **Evidence**: Early testers had it coordinate parallel subagents; example prompt requiring an evidence table.
- **Confidence**: emerging
- **Quote**: "When a subagent reports back, check its evidence before you accept it."
- **Our assessment**: Notable that the vendor recommends explicit instruction to delegate, and bakes verification into the prompt.

### Claim 8: Keep the task list in a file (e.g., TASKS.md) because it survives context summarization
- **Evidence**: Mechanism argument (context fills, older turns get summarized).
- **Confidence**: emerging
- **Quote**: "A list in a file survives that, and it shows you at a glance what's done and what's left."
- **Our assessment**: Matches the external-memory/state-file pattern in other notes; vendor-endorsed.

### Claim 9: At end of a long run, read the "needs from you" part of the summary first; its format can be dictated in CLAUDE.md
- **Evidence**: Vendor claim that Opus 5.5 reports more clearly than Opus 5.
- **Confidence**: anecdotal
- **Quote**: "End every run with three headings: Blocked on me, Changed, Found."
- **Our assessment**: Useful human-review ergonomics; the quote is the source's example CLAUDE.md instruction.

### Claim 10: Opus 5.5 is a good first-pass code reviewer, even at lowest effort
- **Evidence**: One unnamed early tester, no data.
- **Confidence**: anecdotal
- **Quote**: "One early tester said Opus 5.5 at its lowest effort caught more bugs than Opus 5 at high effort, with fewer false alarms."
- **Our assessment**: Single anecdote; treat as hypothesis. The "block-the-merge-only, with repro" review prompt is the more reusable part.

### Claim 11: Ask the model to mark what it couldn't confirm and where it looked
- **Evidence**: Prompt suggestion only.
- **Confidence**: anecdotal
- **Quote**: ""I couldn't find this" is worth reading, and asking for it makes it easy to find."
- **Our assessment**: Cheap mitigation for confident-fabrication; no evidence of efficacy.

### Claim 12: In long chats/projects, tell the model earlier answers are settled to avoid slow re-examination (except for long-analysis projects)
- **Evidence**: Vendor observation.
- **Confidence**: anecdotal
- **Quote**: "In a long chat, Opus 5.5 sometimes goes back over an earlier answer while it thinks about a short follow-up."
- **Our assessment**: Interesting tradeoff: speed vs. self-correction; source itself says to omit it for analysis work.

### Claim 13: Opus 5.5 is the first Opus to ship with Fable-level bio/cyber safeguards; flagged messages switch the session to an older model, and requests to reproduce internal reasoning can be flagged
- **Evidence**: Product behavior description with UI settings and /commands.
- **Confidence**: settled (as vendor product behavior)
- **Quote**: "A request to reproduce its internal reasoning in the reply can be declined."
- **Our assessment**: Operational risk for unattended pipelines: a silent model downgrade mid-run. Prompts that ask for chain-of-thought dumps should be rewritten as "explain why in three sentences".

### Claim 14: Fast mode for Opus 5.5 is the same model with faster output at higher per-token cost, best for interactive back-and-forth
- **Evidence**: Product description (research preview).
- **Confidence**: settled
- **Quote**: "You get the same model, and the text arrives sooner."
- **Our assessment**: Useful guidance on when to pay for speed: only when a human waits on each reply.

## Concrete Artifacts

Source's example Claude Code task prompt (blog post, "Say what 'done' looks like"):

```
Migrate the payment endpoints from the old client to the new one.
Done means: every endpoint uses the new client, the old client is deleted, and the test suite passes.
Stop and ask me only if a test fails for a reason you can't explain.
```

Source's suggested CLAUDE.md rule (blog post, "Tell it which stops you want"):

```
When a step doesn't need my input, keep going. Put status notes in the same message as your next action.
Stop and ask only when you can't continue without me, or before anything destructive: deleting data, force-pushing, or changing anything outside this repository.
```

Source's subagent audit prompt:

```
Audit every service in services/ for the retry bug in the linked issue.
Give each service to its own subagent. When a subagent reports back, check its evidence before you accept it.
Finish with one table: service, affected yes or no, and the evidence.
```

Source's review prompt:

```
Review the diff on this branch against main.
List only problems you'd block the merge for. For each one, give the file and line, why it's wrong, and how to show it fails.
```

Source's project instruction for settled answers:

```
Once you have answered something, treat that answer as done. Focus on what I'm asking now, and don't go back over an earlier answer unless I ask about it or point out a problem with it.
```

Source's design negative-list prompt:

```
Build a personal website with placeholder content.
Don't use a cream or off-white background, italic accent words in headings, numbered "01 / 02 / 03" section labels, monospace labels, or pill-shaped buttons.
```

Flag-handling commands listed in the source: `/model` (switch back), Esc twice (edit last message), `/config` ("Switch models when a message is flagged"), `/feedback` (report wrong flag), `/fast`.

## Cross-References

- **Corroborates**: `blog-anthropic-opus47-best-practices.md` Claim 9 (delegate to the model like a capable engineer rather than guiding step by step) and Claim 10 (batch context into the first turn); Claim 6 (adaptive thinking, model decides how much to think) supports the "drop think-hard lines" advice. `blog-claude-dev-thariq-spending-your-effort.md` Claim 2 (effort as a compute signal) matches "change effort instead". `blog-addyosmani-loop-engineering.md` Claim 10 (state file carries context between runs) corroborates the task-list-in-a-file advice.
- **Contradicts**: None filed. Mild tension only: Claim 4 here (list specific "don't" patterns for design) vs. `blog-anthropic-opus47-best-practices.md` Claim 12 (positive examples beat "Don't do this"); differing contexts (visual defaults vs. voice/length), so treated as a conditioning variable per MINER §4a.
- **Extends**: `blog-anthropic-opus47-best-practices.md` Claim 14 (Opus 4.7 spawns fewer subagents, must be told to delegate) by giving a verified-fan-out prompt for 5.5; `blog-humanlayer-writing-a-good-claude-md.md` by showing vendor-recommended CLAUDE.md rules for stop/continue behavior and report format.
- **Novel**: Premature-stop failure mode and its CLAUDE.md fix; model-switch-on-flag behavior and its implications for reasoning-dump prompts; "settled answers" instruction for long chats.

## Guide Impact

- **Chapter 02**: Add the "definition of done + narrow stop condition" prompt pattern and advice to delete "think hard" lines from saved instructions, citing Claims 1-2.
- **Chapter 03**: In long-run guidance, add the task-list-in-file practice (Claim 8) and subagent fan-out with evidence verification (Claim 7); note that flagged-message model switching can silently change the model mid-run (Claim 13).
- **Chapter 05**: Add the CLAUDE.md stop/continue rule (Claim 5) with the caveat to keep permission prompts on for destructive commands (Claim 6), and the "block-the-merge-only" review prompt (Claim 10, flagged as anecdotal).

## Extraction Notes

Read the full post (single page, no sub-pages followed). Source contains no quantitative data; evidence is vendor assertion and unnamed "early testers", hence overall confidence "emerging". Cross-referenced claim numbers were verified against the headings in the cited notes. Page fetched via a markdown-conversion tool; quotes copied from that output.
