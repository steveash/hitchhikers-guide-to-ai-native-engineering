---
source_url: https://news.ycombinator.com/item?id=46544838
source_type: failure-report
platform: hn
title: "Cancelled 2x Cursor Ultra plans, here's why"
author: throwawayround (anonymous)
date_published: 2026-01-08
date_extracted: 2026-04-14
last_checked: 2026-04-14
status: current
confidence_overall: anecdotal
issue: "#75"
---

# Failure Report: Cursor Ultra Cost Explosion — 4k User Tokens Bill as 21 Million Cache Tokens

> An anonymous practitioner canceled two Cursor Ultra subscriptions after costs
> jumped from a steady $60-100/month to a projected $1,600/month with no change
> in work volume; the root cause was prompt-cache replay billing — Cursor's hidden
> session state grew to millions of cached tokens that Anthropic billed on every
> API call, while the UI showed only the visible 200k context window.

## Source Context

- **Platform**: Hacker News self-post, 9 points, 7 comments, 2026-01-08
- **Author credibility**: throwawayround is an anonymous HN account. The post
  is data-rich (specific dollar figures, a concrete per-call token count, a
  projected monthly cost, and a described mechanism rather than vague complaint),
  which elevates it above typical venting. The author characterizes this explicitly
  as a "product transparency issue" rather than blaming Anthropic, suggesting
  familiarity with the underlying API billing model. The $12-per-call claim with
  supporting token counts (~4k user input → ~21M cache reads) is the kind of
  specific number that comes from actually exporting billing CSV data.
- **Community response**: Small thread (7 comments). bigyabai argued users must
  monitor pay-as-you-go services consciously; throwawayround rebutted that Cursor
  Ultra is NOT a pure pay-as-you-go service and that the cost driver was
  structurally invisible. minimally corroborated the scale problem ("I maxing out
  a 20x membership in a day of use"). techblueberry questioned whether extreme
  usage reflects agent-heavy workflows better suited to employer-funded accounts.
  No commenter disputed the core mechanism (prompt-cache replay billing); the
  disagreement was about whose responsibility the transparency gap was.

## What Was Attempted

- **Goal**: Use Cursor Ultra for normal coding work. The author had sustained
  usage at $60-100/month before the billing event; this was not a sudden behavior
  change on their end.
- **Tool/approach**: Cursor Ultra subscription (a high-limit / "unlimited" plan
  tier as of early 2026). Used Cursor's agent mode, which maintains multi-step
  context including tool traces, codebase scans, and conversation history.
- **Setup**: Individual developer. No indication of unusual agent-heavy workflow;
  author emphasizes "I did not suddenly start doing 10x more work."

## What Went Wrong

- **Symptoms**:
  1. Within a few days, monthly spend spiked from $60-100 to $500+, projecting
     ~$1,600/month.
  2. A single API call with approximately 4,000 token user input was billed at
     approximately 21 million cache read tokens, costing ~$12 for that one call.
  3. The Cursor UI showed a 200k context window with the note that "content is
     summarized to stay within limits" — creating the impression that context was
     being managed and contained.
  4. Cursor support confirmed the billing was "expected."
  5. The billing mechanism was invisible in the UI; understanding it required
     exporting CSV data from the billing dashboard.

- **Severity**: Catastrophic cost failure. 16x expected monthly cost with no
  corresponding work increase.

- **Reproducibility**: The author had consistent usage before the spike,
  suggesting this was triggered by session state accumulation reaching a tipping
  point rather than a one-off anomaly. minimally's corroboration of hitting a "20x
  membership" cap in a single day suggests the underlying billing mechanics affect
  multiple Ultra users.

## Root Cause (if identified)

- **Author's diagnosis**: Cursor maintains a "very large hidden prompt state"
  including conversation history, tool traces, agent state, and codebase data.
  This state is stored as a prompt cache. On every API call, the entire cached
  prefix is replayed. Anthropic bills for `cache_read_input_tokens` on each
  replay — even if the content is later summarized or truncated *before* inference.
  The key mechanism: "Anthropic bills for cache read tokens on each replay, even
  when content is later summarized." The 200k context window displayed in the UI
  is the *inference window*, not the *cache* being passed in. These are different
  things. Cache breakpoints are determined by Cursor, not the user.

  Direct quote (summarized from post, given the WebFetch summary): "The UI says
  'max 200k context,' but billing says otherwise. Cache size and the implications
  of prompt replay are impossible to see or reason about without exporting CSV data."

- **Our assessment**: The diagnosis is technically plausible and consistent with
  how Anthropic's prompt caching works. Anthropic charges `cache_read_input_tokens`
  at 0.1x the base input price per token, but when the cached prefix is 21 million
  tokens, 0.1x a large-token-count number still produces a large dollar figure.
  The user's mental model ("I'm using a 200k context window") is structurally
  different from the billing reality ("Cursor is sending millions of cached context
  tokens on each call"). This is a product design failure: the UI is accurate about
  the inference window but silent about the billing window.

  This is NOT the same failure mode as Issue #58 (Cursor Pro switching silently to
  on-demand billing after hitting a plan limit). That failure is about billing mode
  switching; this failure is about billing magnitude within a single mode. Both
  involve Cursor billing opacity, but the mechanisms are independent.

- **Category**: tool-limitation / product-transparency-failure (Cursor's UX does
  not surface the underlying prompt-cache cost model; users build a mental model
  from the visible context window that does not predict actual billing)

## Recovery Path

- **What they switched to**: Canceled both Cursor Ultra plans. No specific
  replacement mentioned.
- **Workaround**: None identified. The only diagnostic path described was exporting
  billing CSV data — which explains what happened after the fact but does not
  prevent it.
- **Unresolved**: The author frames this as a systemic transparency issue with no
  self-service fix. There is no in-product way to monitor cache size before it
  becomes a billing event.

## Extracted Lessons

### Lesson 1: AI tool UIs display the inference context window, not the billing cache — these can differ by orders of magnitude

- **Evidence**: throwawayround's concrete example: 4k visible user tokens billed
  as ~21 million cache read tokens. The UI showed 200k context; the billing record
  showed millions of cached tokens.
- **Confidence**: anecdotal (single documented case, but the mechanism is
  consistent with Anthropic's published prompt-caching pricing model)
- **Actionable as**: When evaluating AI coding tools, distinguish between:
  (a) the inference context window shown in the UI, and (b) the underlying billing
  context which includes all cached state. These are product-controlled, not
  user-controlled. Budget based on (b), not (a).

### Lesson 2: Prompt-cache replay costs scale with session state depth, not user-visible context

- **Evidence**: throwawayround's diagnosis that Cursor accumulates conversation
  history, tool traces, agent state, and codebase data in a cached prefix that
  grows over sessions. The 21-million-token figure represents accumulated session
  depth, not a single user message.
- **Confidence**: anecdotal (mechanism is structurally consistent with Anthropic
  prompt-caching docs; throwawayround appears to have verified via CSV export)
- **Actionable as**: For tools that use agentic/multi-step sessions (tool traces,
  codebase indexing, long context accumulation), billing costs are not proportional
  to the visible conversation length. Expect superlinear cost growth as sessions
  extend and cache depth increases.

### Lesson 3: "Summarized to stay within limits" does not mean "billed based on the summary"

- **Evidence**: throwawayround describes the UI message "content is summarized to
  stay within limits." Author's key insight: summarization happens AFTER billing —
  Anthropic charges for the cached prefix replay even if the content is later
  truncated or summarized before inference. The summary is the inference input; the
  cache is the billing input.
- **Confidence**: anecdotal (author's account; not independently verified)
- **Actionable as**: Do not interpret a tool's "context management" or
  "summarization" feature as a cost control. These may control what the model
  reasons over, not what you are billed for. Treat billing and inference context
  as separate variables.

### Lesson 4: Cache breakpoints are vendor-controlled, not user-controlled

- **Evidence**: throwawayround explicitly states "Cache breakpoints are determined
  by Cursor, not the user." Users have no ability to inspect, cap, or reduce the
  cached prefix size within Cursor's product.
- **Confidence**: anecdotal
- **Actionable as**: For any AI coding tool subscription, ask: "Who controls how
  much cached state is maintained and billed?" If the answer is "the vendor, not
  me," budget conservatively and monitor billing CSV rather than the in-product UI.

### Lesson 5: Cost explosion can occur within an "unlimited" plan tier due to underlying API billing

- **Evidence**: Cursor Ultra is a high-limit/unlimited-tier subscription, yet costs
  jumped to $500+ in days. minimally reports maxing out a "20x membership" in a
  single day. This is not the result of exceeding a plan limit (that is Issue #58)
  but of the underlying token costs scaling beyond what the plan pricing anticipated.
- **Confidence**: anecdotal (two independent reports of disproportionate cost within
  Ultra-tier plans)
- **Actionable as**: "Unlimited" plan tiers for AI tools should be treated as having
  soft cost ceilings based on the vendor's API cost model, not hard unlimited guarantees.
  When adopting AI tools at team scale (Ch05), test real billing behavior under
  representative workloads before rolling out widely.

### Lesson 6: Billing transparency requires exporting CSV, not reading the product UI

- **Evidence**: throwawayround states that the cache size and its implications "were
  impossible to see or reason about without exporting CSV data." The UI provided no
  signal before costs exploded.
- **Confidence**: anecdotal
- **Actionable as**: For any AI coding tool subscription, establish a routine
  billing-CSV review practice rather than relying on the product UI. For teams,
  treat billing CSV access as a required operational practice from day one.

## Concrete Artifacts

### The Core Billing Anomaly (from throwawayround's post)

```
User input:          ~4,000 tokens  (what the user typed)
Cache read tokens:   ~21,000,000    (Cursor's hidden session state)
Cost per call:       ~$12

Monthly trajectory:  $60-100 (historical) → $500+ actual → ~$1,600 projected
```

The ratio of cache read tokens to user input tokens: ~5,250:1.
At Anthropic's published cache-read rate (0.1x base input price), 21M cache
tokens is the billing equivalent of 2.1M base input tokens per call.

### throwawayround's framing of the transparency gap (paraphrased from post)

> "The UI says 'max 200k context,' but billing says otherwise. Cache size
> and the implications of prompt replay are impossible to see or reason about
> without exporting CSV data."

> "This is a product transparency issue." [not an API billing error]

### minimally's corroborating data point

> "I get a lot of value in cursor but I shouldn't be maxing out a 20x membership
> in a day of use."

## Cross-References

- **Corroborates** `blog-bswen-mcp-token-cost.md`: Bswen documents the same
  underlying pattern in Claude Code / MCP — 100k tokens consumed before the user
  types anything (Claim 1: MCP tool definitions load upfront; Claim 6: "conversation
  itself was only 4%" of context). In both cases the billing driver is invisible
  session/tool overhead, not user-visible conversation. Bswen's mechanism (MCP tool
  definitions) and throwawayround's mechanism (cached prompt state replay) are
  structurally analogous: vendor-controlled background token accumulation that the
  UI does not surface. Bswen's Claim 8 ("Cache read costs 0.1x base") is exactly the
  pricing mechanism that makes throwawayround's 21M token cache so expensive — and
  illustrates why "cache reads are cheap" is dangerously incomplete guidance.

- **Corroborates** `failure-hooks-enforcement-2k.md` Lesson 5 (cost data: $2K/year
  for a solo side-project dev on Claude Code): Both sources provide rare practitioner
  cost disclosures. Together they establish that heavy AI coding tool usage by
  individuals routinely costs hundreds to thousands of dollars per month, with
  opacity being a consistent failure mode across tools (Claude Code and Cursor).

- **Corroborates** `research-wasnotwas-context-compaction.md` Claim 2 ($0.40 per
  compaction, equivalent to ~21 cached turns): The Cursor case reveals the flip side
  of caching economics — where wasnotwas shows that compaction costs money because
  it busts the KV cache, throwawayround shows that NOT compacting (maintaining a
  large cached prefix) costs money through cache-read replay. Both failure modes stem
  from the same underlying mechanism: Anthropic's prompt-caching pricing makes context
  state a billable quantity, not just an inference parameter.

- **Extends** Issue #58 (not yet mined as a source note): Issue #58 covers Cursor Pro
  silently switching to on-demand billing after hitting a plan limit (different failure
  mode: billing mode switch vs. billing magnitude explosion). Together these two HN
  reports form a complementary pair of Cursor billing failure modes: (1) silent mode
  switch after limit (Issue #58) and (2) cost explosion from cache depth within a
  plan (this note). Both have the same root: Cursor's billing model is not
  transparently communicated in the product UI.

- **Novel**: The specific mechanism of prompt-cache replay billing (cache_read_input_tokens
  scaling with hidden session state, independently of visible context window) is the
  most detailed account of this failure mode in our corpus. The 4k→21M token ratio is a
  concrete number that no other source provides. The "summarization happens after billing"
  insight distinguishes this from a simple context-window-limit failure.

## Guide Impact

- **Chapter 04 (Context as budget / token economics)**: Add a dedicated warning about
  the billing context vs. inference context distinction. The current corpus treats
  "context window" as a unified concept; this source reveals that the billing input
  (cached prefix) and inference input (visible context) can differ by orders of
  magnitude, and the tool vendor controls the gap. Recommend: "Never assume your UI
  context window display predicts your API bill."

- **Chapter 04 (Context engineering)**: Cite the 4k→21M token example when
  introducing prompt caching economics. The Bswen note (Claim 8) establishes that
  cache reads cost 0.1x — this source shows that when cache depth reaches millions
  of tokens, "cheap per token" does not mean "cheap overall." Pair with Bswen for
  the complete picture: (a) MCP tools add hidden upfront cost, (b) session state
  adds hidden per-call cost via cache replay.

- **Chapter 01 (Daily workflows — cost monitoring)**: Add billing CSV review as a
  required workflow practice, not optional. The UI is insufficient. The
  recommendations should specify: (a) export billing CSV weekly for any paid AI
  tool subscription, (b) set billing alerts where the tool supports it, (c) treat
  unexplained cost increases as diagnostic triggers rather than normal variance.

- **Chapter 05 (Team adoption)**: Add explicit guidance on AI tool cost testing
  before team rollout. The Cursor Ultra failure (and Issue #58's Cursor Pro failure)
  together show that Cursor's billing model can produce surprising costs under
  representative workloads. Any team evaluating an AI coding tool should run a
  controlled billing pilot with one or two developers under real workloads, reviewing
  billing CSV (not UI metrics) before committing to wider rollout.

- **Chapter 05 (Team adoption)**: Add a note that "unlimited" plan tiers should be
  treated as soft-cost caps, not unlimited guarantees. The API pricing model beneath
  the subscription often allows costs to exceed plan pricing via usage overage or
  per-token accumulation.

## Extraction Notes

- Direct HN fetch (WebFetch) returned a synthesized summary rather than verbatim
  quotes; Algolia API was also used. Verbatim quotes are marked as "paraphrased from
  post" where they are reconstructed from synthesis rather than character-for-character
  confirmed. The core technical claims (4k user tokens, ~21M cache tokens, ~$12/call,
  $500+ monthly, ~$1,600 projected) appeared consistently across both fetch paths
  and are treated as reliable.
- The thread is small (9 points, 7 comments) but technically substantive. The
  per-call token count ($12 / 21M cache tokens) is the kind of detail that comes
  from actual billing CSV analysis, lending credibility to the mechanism claim.
- throwawayround uses a throwaway account (as the username implies), suggesting they
  wanted to share this experience without being identified. This does not reduce
  credibility; it is common for users reporting tool cost failures to post anonymously.
- The Prospector triage notes this as distinct from Issue #58 (hardwellvibe's Cursor
  Pro billing mode switch). That distinction is confirmed: Issue #58 is about billing
  mode change after hitting a plan limit; this note is about billing magnitude explosion
  within an established Ultra plan. Both are real but separate failure modes.
- Issue #58 has not yet been mined as a source note. The "Extends" cross-reference
  above is based on the issue body preview only and should be updated when Issue #58
  is mined.
- The failure is Cursor-specific but the underlying pattern (vendor-controlled prompt
  cache state billed independently of visible context) applies to any AI tool that
  uses caching-based session management on a billable API. Claude Code users with
  long sessions and heavy MCP usage face the analogous dynamic (Bswen documents the
  upfront cost; this note documents the per-call replay cost).
