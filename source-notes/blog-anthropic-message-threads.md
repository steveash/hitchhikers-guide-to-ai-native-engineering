---
source_url: https://claude.com/resources/articles/message-threads
source_type: blog-post
title: "Make long-running agents faster with message threads"
author: Anthropic (Claude Platform announcement)
date_published: 2026-11-02
date_extracted: 2026-11-03
last_checked: 2026-11-03
status: current
confidence_overall: emerging
issue: "#4496"
---

# Make long-running agents faster with message threads

> Anthropic announces a `thread` parameter for the Messages API (public beta) that holds conversation state server-side for five minutes so agents send only new messages each turn, cutting time to first token but not token usage.

## Source Context

- **Type**: blog-post (first-party product announcement, ~3 min read)
- **Author credibility**: Anthropic itself, so authoritative on API mechanics. The performance figure is vendor-reported with no methodology, and this is not independent practitioner evidence.
- **Scope**: Covers the mechanism, lifecycle (in-memory, encrypted, 5-minute expiry), best-fit workloads, and availability. It does not cover request/response schema (deferred to docs), error behavior on expired threads, interaction with prompt caching, pricing beyond "standard rates", or failure modes. The linked documentation was not followed (the page's link target was not retrievable as text).

## Extracted Claims

### Claim 1: Resending the full history every turn adds latency before Claude starts responding once conversations reach hundreds of thousands of tokens
- **Evidence**: Vendor description of coding-agent behavior; no measurements for this specific claim.
- **Confidence**: settled
- **Quote**: "A coding agent might make hundreds of requests in one session, and each request resends every earlier message and tool result."
- **Our assessment**: Matches the stateless Messages API model the guide already assumes. The framing that request size (not just model compute) drives TTFT is the motivating premise.

### Claim 2: Message threads is a client-side API change: first request sends the full conversation and starts a thread; later requests send only new messages plus the previous response ID
- **Evidence**: Mechanism description; no code sample in the article.
- **Confidence**: settled
- **Quote**: "The first request includes the full conversation and starts a thread. Each request after that includes only the new messages and the ID of the previous response."
- **Our assessment**: Concrete and implementable. Moves the Messages API toward stateful, response-ID-chained semantics, which changes retry/idempotency and harness-side history management (client must still retain the full history for fallback).

### Claim 3: Thread state is held server-side in memory, encrypted, not written to disk
- **Evidence**: Vendor assertion; no independent audit cited.
- **Confidence**: anecdotal
- **Quote**: "Between turns, we hold each thread in memory, where it’s encrypted and not written to disk."
- **Our assessment**: Relevant to data-retention and compliance reviews, but only a one-sentence assurance. Teams with strict requirements should check the docs.

### Claim 4: Threads expire 5 minutes after the last request, after which the client must resend the full conversation to start a new thread
- **Evidence**: Stated lifecycle rule.
- **Confidence**: settled
- **Quote**: "A thread expires 5 minutes after its last request and your client then resends the full conversation to start a new one."
- **Our assessment**: Key operational caveat. Any pause longer than 5 minutes (human-in-the-loop approval, slow tools, long builds) forces a full resend, so harnesses must always keep the full history locally and handle expiry. The same 5-minute figure matches the default prompt-cache TTL that Ch04 discusses, though the article does not say the two are linked.

### Claim 5: Token usage is unchanged because Claude still reads the full conversation every turn
- **Evidence**: Vendor statement; "Standard Claude token rates and existing rate limits apply."
- **Confidence**: settled
- **Quote**: "While each request is smaller with message threads, Claude still reads the full conversation on every turn, so token usage stays the same."
- **Our assessment**: Important to avoid misreading threads as a cost or context-window saver. It reduces transmission/processing overhead before first token only. Context-budget advice in Ch04 is unaffected.

### Claim 6: Median TTFT drops about 35% for 500k–1M-token requests in Claude Code, where threads are on by default for most users
- **Evidence**: A single vendor-reported figure; no methodology, sample size, baseline, or percentile detail.
- **Confidence**: anecdotal
- **Quote**: "With message threads on by default for most Claude Code users, requests with 500k to 1M tokens see median TTFT drop by about 35%."
- **Our assessment**: Plausible direction, unverified magnitude. Attribute to Anthropic; do not cite as a benchmark. Note it applies only to very large contexts and says nothing about typical (<200k) sessions.

### Claim 7: Benefit scales with carried context and suits active, latency-sensitive sessions (coding agents, computer use, document/image-heavy flows)
- **Evidence**: Qualitative; the listed workload types are asserted, not measured.
- **Confidence**: emerging
- **Quote**: "The more context an agent carries, the more message threads can reduce time to first token."
- **Our assessment**: Sensible. The computer-use point ("screenshots stay with the thread instead of being re-uploaded on every turn") is a distinct benefit: image payload upload is avoided, not just text.

### Claim 8: Availability and pricing: public beta across the native Claude Platform and cloud-partner offerings, at standard token rates and existing rate limits
- **Evidence**: Availability statement.
- **Confidence**: settled
- **Quote**: "Standard Claude token rates and existing rate limits apply."
- **Our assessment**: Beta status means behavior may change; guide text should flag it as beta.

## Concrete Artifacts

No code samples in the source. Lifecycle as described (source: article body):

```
Request 1:   thread param + FULL conversation          -> starts thread, returns response ID
Request 2..n: thread param + NEW messages + previous response ID
Idle > 5 min after last request -> thread expires -> client resends FULL conversation (new thread)
Server side: thread held in memory, encrypted, not written to disk
Billing/tokens: unchanged (Claude reads full conversation each turn)
Reported: ~35% median TTFT reduction at 500k-1M tokens (Claude Code, vendor-reported)
```

## Cross-References

- **Corroborates**: `blog-anthropic-prompt-caching-everything.md` Claim 1 (long-running agents depend on infrastructure that makes resending a large, growing prefix cheap); this article attacks the transmission/latency side rather than the compute-cost side.
- **Contradicts**: None found. No contradiction issue filed.
- **Extends**: `blog-anthropic-prompt-caching-everything.md` (Claims 10–11 on compaction and cache-safe forking assume stateless full-history requests; threads add a separate server-side state layer whose interaction with cache-safe forking and compaction is not described). `blog-anthropic-fold-subagents-into-main-agent-loop.md` Claim 4 (single-loop agents reduce runtime) is a different latency lever, orthogonal to this one.
- **Novel**: The `thread` parameter, response-ID chaining, 5-minute server-side expiry, and the "token usage unchanged" clarification are not covered anywhere in the corpus.

## Guide Impact

- **Chapter 04**: Where prompt caching / compaction cost is discussed, add a short note that message threads (public beta) reduce request size and TTFT but not tokens billed or context consumed, so they do not replace caching or compaction. Attribute the ~35% figure to Anthropic as unverified.
- **Chapter 02**: Add a harness-design caveat: with threads, the harness must still persist the full history locally and handle the 5-minute expiry (resend and start a new thread), especially around human approval pauses and long-running tools.
- **Open question for Smith**: how threads interact with cache-safe forking (Ch04 / prompt-caching Claims 10–11) is undocumented in this source; do not assert one.

## Extraction Notes

- Fetched the full article HTML and read the complete body; quotes are copied verbatim from the page text (apostrophe in "it’s" is the source's curly one). The article is short, so the claim count is below the usual 5–15 target by design but fine for this source.
- Did not follow the "documentation" link; schema details and expiry error behavior remain unverified.
- Cross-referenced claim numbers verified against the cited notes' `### Claim` headings.
