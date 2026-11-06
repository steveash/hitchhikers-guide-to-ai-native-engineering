---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/what-is-context-rot
source_type: blog-post
title: "Context rot in AI agents: How to recognize and fix it"
author: Piyush Sonawane
date_published: 2026-11-05
date_extracted: 2026-11-06
last_checked: 2026-11-06
status: current
confidence_overall: emerging
issue: "#4558"
---

# Context rot in AI agents: How to recognize and fix it

> A conceptual Thoughtworks explainer that separates context rot from context poisoning and pollution, gives a symptom checklist and a five-fix menu (each with a trade-off), and frames the harness as the place where context policy runs.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, Generative AI)
- **Author credibility**: Piyush Sonawane, Thoughtworks. The page carries a disclaimer that the views are the author's, not Thoughtworks'. The piece is practitioner-level and vendor-neutral; the opening anecdote about a coding agent on a bug fix is unattributed and has no data.
- **Scope**: Definition, causes, symptoms, rot vs. poisoning vs. pollution, five mitigations, harness role and a harness checklist. It has no code, no metrics of its own, and no experiments. The only external evidence is a passing citation of a 2025 Chroma evaluation of 18 LLMs. The page is structured as an explainer with an FAQ.

## Extracted Claims

### Claim 1: Context rot is a decline in the model's *use* of context, not a lack of information
- **Evidence**: Definition plus an opening anecdote (coding agent revisits failed approaches although the information is still in context). No measurement.
- **Confidence**: emerging
- **Quote**: "Context rot is the decline in an AI model's ability to use its context effectively as that context grows or becomes less relevant, noisy or difficult to navigate."
- **Our assessment**: Matches the term as already used by Anthropic and in the guide. The useful emphasis is that the information is present but under-used, which is what distinguishes it from a missing-context problem.

### Claim 2: A longer window does not by itself solve rot
- **Evidence**: Argument, plus a passing reference to a Chroma evaluation of 18 LLMs showing degradation with context length even on controlled tasks.
- **Confidence**: emerging
- **Quote**: "A long context window allows a model to process more information, but it doesn't guarantee that all of it will be used equally well."
- **Our assessment**: Consistent with other notes. The Chroma study is cited secondhand and not examined here, so we should cite Chroma directly (if at all) rather than via this post.

### Claim 3: Five causes: history growth, noisy tool output, stale/conflicting info, upfront over-loading, window limits forcing lossy compaction
- **Evidence**: Listed with short illustrations (e.g., a test run emitting hundreds of lines when only a failing assertion and a few stack-trace lines matter).
- **Confidence**: emerging
- **Quote**: "When space becomes constrained, a system may need to summarize, compact or truncate older content. These techniques help, but a summary can omit a subtle requirement and truncation can remove a detail that later becomes important."
- **Our assessment**: A reasonable checklist. Note that compaction is listed as both a remedy and a cause, which matches the empirical picture in the compaction survey note.

### Claim 4: Rot shows up as five behavioural symptoms, and a single mistake is not evidence of rot
- **Evidence**: Checklist: forgetting earlier constraints, repeating failed approaches, losing track of current state, distraction by irrelevant details, inconsistent decisions.
- **Confidence**: anecdotal
- **Quote**: "One mistake doesn't necessarily indicate context rot."
- **Our assessment**: Useful as a triage list. The "look for a pattern as context grows" rule is the key discriminator, but the post gives no thresholds or measurements.

### Claim 5: Diagnose by inspecting the context that was present before the decision
- **Evidence**: Procedural advice, no worked example.
- **Confidence**: anecdotal
- **Quote**: "When investigating, inspect the context available before the agent made its decision."
- **Our assessment**: Practical and cheap, and it implies the harness must make the exact model input inspectable (see the observability item in the checklist, Claim 11). Not validated.

### Claim 6: Rot and poisoning are distinct and need different safeguards, though they can overlap
- **Evidence**: Definitions with one example each; the overlap case is stale information that is treated as current.
- **Confidence**: emerging
- **Quote**: "Reducing clutter won't automatically make misleading information safe, and validating sources won't prevent a context from becoming overloaded."
- **Our assessment**: The main contribution. It links a context-management concern to a security concern and warns against applying one fix to both. Reasonable and uncontroversial; not tested.

### Claim 7: Context pollution is a third term: accumulated unnecessary, outdated or irrelevant content
- **Evidence**: FAQ definition only; the body of the article does not use the term.
- **Confidence**: anecdotal
- **Quote**: "Context pollution is the accumulation of unnecessary, repetitive, outdated or irrelevant information in an agent's working context."
- **Our assessment**: Pollution is nearly a cause of rot rather than a separate failure. The taxonomy is looser than it first appears, and the body text and FAQ are not fully aligned. Terms are not standardised across the industry.

### Claim 8: Five fixes, each with a "use when" and a trade-off
- **Evidence**: Filter tool outputs; summarize long tasks; retrieve on demand; separate persistent instructions from temporary task state; start fresh with a handoff. The post states that no single fix suffices.
- **Confidence**: emerging
- **Quote**: "There's no single solution to context rot."
- **Our assessment**: The fixes are all established practice. The value is the paired trade-offs (aggressive filtering removes evidence; summaries omit details; retrieval misses material; persistent instructions go stale; handoffs lose detail).

### Claim 9: A handoff/summary must contain specific fields, or the agent repeats work
- **Evidence**: A five-item list for coding tasks, and a counter-example of an inadequate summary.
- **Confidence**: anecdotal
- **Quote**: "A summary such as "tried a few fixes, but the issue remains" isn't enough if it causes the agent to repeat work."
- **Our assessment**: Actionable template (see Concrete Artifacts). Overlaps with Anthropic's /rewind "summarize from here" handoff and /compact hints.

### Claim 10: The harness is where context policy should live, at four points in the loop
- **Evidence**: Enumeration: before a model call (select/retrieve), after a tool call (filter/structure), as the task progresses (update task state), when unwieldy (compact or fresh context with handoff).
- **Confidence**: emerging
- **Quote**: "Rather than relying entirely on the model or requiring developers to intervene manually, a harness can apply rules and coordinate supporting components throughout the workflow."
- **Our assessment**: A useful framing for Ch02. It is a design description, not evidence that harness-managed policy outperforms manual management.

### Claim 11: A seven-question harness checklist
- **Evidence**: Relevant context, controlled tool outputs, task state, context refresh, on-demand retrieval, persistent instructions, observability and evaluation.
- **Confidence**: anecdotal
- **Quote**: "Not every agent needs every capability from the outset."
- **Our assessment**: Good review checklist. The post advises adding controls only where context management is demonstrably hurting performance.

### Claim 12: Measure task outcomes, not context size
- **Evidence**: Key takeaway only.
- **Confidence**: anecdotal
- **Quote**: "Evaluate outcomes, not just context size."
- **Our assessment**: Sensible, but the post offers no evaluation method.

## Concrete Artifacts

Handoff/summary contents for a coding task (Sonawane, "Summarize long-running tasks"):

```
- The goal and important constraints.
- What has been investigated and established.
- Which approaches failed and why.
- Changes already made.
- Open questions and next steps.
```

Fresh-context handoff fields (from "Start a fresh context when needed"): goal, current state, important findings, relevant files, constraints and unresolved questions.

Harness checklist headings (Sonawane, "Agent harness essentials at a glance"): Relevant context; Controlled tool outputs; Task state; Context refresh; On-demand retrieval; Persistent instructions; Observability and evaluation.

No code, configs or metrics appear in the source.

## Cross-References

- **Corroborates**:
  - `blog-thoughtworks-nandyala-pani-bounded-context-bounded-attention.md` Claim 2 (rot is a relevance problem, larger window does not fix it) and Claim 3 (loading vs. exploration causes; compare Sonawane's "loading too much upfront" and "retrieve on demand").
  - `blog-anthropic-session-management-1m-context.md` Claim 1 (context rot as the official term) and Claim 5 (summarize-from-here handoff).
  - `blog-humanlayer-long-context-isnt-the-answer.md` Claim 8 (isolation beats expansion).
  - `research-wasnotwas-context-compaction.md` Claim 3 (most harnesses use lossy LLM-summary compaction), which supports Sonawane's warning that summaries can omit requirements.
- **Contradicts**: None found.
- **Extends**:
  - `blog-anthropic-context-engineering-claude-5.md` Claim 6 (progressive disclosure) and Claim 7 (keep CLAUDE.md lightweight). Sonawane's persistent-vs-task-state split gives the same advice a rationale.
  - `blog-thoughtworks-patole-context-real-bottleneck-ai-agents.md`: that note is about business context; this one is operational context in a session, and the two are complementary.
- **Novel**: The rot / poisoning / pollution split with the "different safeguards" argument; the symptom checklist; the "inspect the context before the decision" diagnostic; the harness-checkpoints framing and checklist; the trade-off paired with each fix.

## Guide Impact

- **Chapter 04**: In the "Context rot — when wrong information accumulates" section, add a short distinction between rot (poor use of context), pollution (accumulated stale content) and poisoning (misleading or untrusted input), and say the fixes differ. Consider adding the five-symptom checklist and the "inspect the context before the decision" diagnostic. Cite this note, keeping the evidence level at emerging.
- **Chapter 04**: Add the five-field handoff template to any handoff/compaction guidance.
- **Chapter 02**: The four harness checkpoints and the seven-question checklist could back a short "context policy" subsection.
- **Chapter 01**: Optionally link the "fresh context with handoff" advice from the daily-workflow guidance on when to start a new session.
- Do not cite the Chroma figure through this post.

## Extraction Notes

- The page renders client-side. The full article text was recovered from the served HTML and read completely, including the FAQ; all quotes were copied from that text.
- The article has no sub-pages worth following; its single external link (Chroma, Anthropic context engineering) was not fetched since the post only mentions them in passing.
- Conceptual article: treat as vocabulary and checklist, not evidence. Pollution appears only in the FAQ.
- No contradictions were found, so no contradiction issue was filed.
