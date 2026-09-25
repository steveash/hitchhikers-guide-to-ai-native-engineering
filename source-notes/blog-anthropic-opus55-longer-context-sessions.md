---
source_url: https://claude.com/blog/claude-opus-5-5-built-for-coding-sessions-that-use-more-context
source_type: blog-post
title: "Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind."
author: Anthropic (Claude blog, no individual byline)
date_published: 2026-09-24
date_extracted: 2026-09-25
last_checked: 2026-09-25
status: current
confidence_overall: settled
issue: "#3693"
---

# Coding Sessions Are Longer and Use More Context. Claude Opus 5.5 Is Built With That in Mind.

> First-party Anthropic post arguing that Claude Opus 5.5's ~40% cost reduction versus
> Opus 5 is disproportionately concentrated in long, context-heavy agentic sessions,
> backed by aggregate Claude Code usage telemetry from March–September 2026 (context per
> request up 2.6x, input:output ratio shifted from 189:1 to 324:1) and three named
> mechanisms — pricing cuts, harness-level cache-miss reduction, and fewer turns per task.

## Source Context

- **Type**: blog-post (claude.com/blog — Anthropic's official product blog, no
  individual author byline is shown on the page; auto-discovered via the
  `claude-blog` trusted RSS feed).
- **Author credibility**: First-party Anthropic product/economics post. Authoritative
  for Opus 5.5 pricing figures, the stated aggregate Claude Code usage telemetry (March
  through September 2026), and the description of Claude Code harness cache-management
  changes. Not independently audited — the usage statistics and the "cache misses
  decreased by more than 50%" figure are Anthropic's own aggregate measurements with no
  disclosed methodology (sample size, cohort definition, or measurement window
  granularity are not given). The one named customer case study (Zeta Labs) and the one
  named external quote (Addy Osmani) are anecdotal by nature.
- **Scope**: Covers the economic mechanics of Opus 5.5 for long-running, context-heavy
  Claude Code sessions: three cost levers (pricing, cache-hit-rate improvements in the
  harness, fewer turns per task), aggregate developer behavior trends from March–
  September 2026, and session-management recommendations (pick model at session start,
  compact before stepping away, one-hour cache TTL). Does NOT cover: Opus 5.5's raw
  capability/benchmark scores (covered on the companion `anthropic.com/claude-opus-5-5`
  announcement page), full per-token pricing tables beyond the percentage cuts stated
  in-line, or non-Claude-Code product surfaces (API-only usage, Claude apps).

## Extracted Claims

### Claim 1: Claude Opus 5.5 costs about 40% less to run than Opus 5 for typical token-billed workloads, with the largest savings concentrated in longer-running, higher-context sessions
- **Evidence**: Anthropic's own cost estimate, stated as the post's opening claim and
  linked to the `anthropic.com/claude-opus-5-5` announcement page.
- **Confidence**: settled (vendor-stated pricing/cost-model fact, consistent with the
  40% figure independently stated on the companion Anthropic announcement page)
- **Quote**: "We estimate Claude Opus 5.5 costs about 40% less to run than Opus 5 for typical workloads billed by token."
- **Our assessment**: This is the post's central thesis and is corroborated verbatim by
  the companion `anthropic.com/claude-opus-5-5` page ("costs 40% less to run than Opus
  5"). The qualifier — that per-token billed users see the *greatest* difference on
  long, high-context sessions — is the framing the rest of the post exists to justify;
  it is a directional claim (more savings for bigger sessions), not a separately
  quantified one.

### Claim 2: Between March and September 2026, Claude works 3.3x longer per prompt with more than 40% more model calls per prompt, and sessions have 68% fewer interruptions
- **Evidence**: Aggregate Claude Code usage data, stated as pulled directly by
  Anthropic; no cohort size, sampling method, or statistical methodology disclosed.
- **Confidence**: emerging (directionally plausible and specific, but self-reported
  aggregate telemetry with no disclosed methodology)
- **Quote**: "Claude works 3.3x longer on each prompt with more than 40% more model calls per prompt. There are 68% fewer interruptions."
- **Our assessment**: This is the most concrete telemetry figure in the post and a
  genuinely new data point for the corpus — no other mined source quantifies session
  length growth or interruption-rate change over a six-month window. "Fewer
  interruptions" is presented as a proxy for less human intervention needed mid-task,
  which is a reasonable but unstated inference the post does not spell out explicitly.

### Claim 3: Developers are about twice as likely to have a tool server connected or use a skill, and a third less likely to paste text into a prompt, compared to six months earlier
- **Evidence**: Same aggregate usage data pull as Claim 2.
- **Confidence**: emerging (self-reported aggregate telemetry, no methodology disclosed)
- **Quote**: "Developers are about twice as likely to have a tool server connected or use a skill and a third less likely to paste text into a prompt."
- **Our assessment**: This is indirect evidence of MCP/skill adoption maturing as a
  practice over the same window, and of context increasingly arriving via structured
  mechanisms (tool servers, skills, @-mentions) rather than manual copy-paste. Directly
  relevant to Ch02/Ch03 discussions of context-assembly patterns, though the post does
  not break down "tool server" vs. "skill" usage separately.

### Claim 4: Context per request has grown 2.6x over the same six-month window, and the input-to-output token ratio moved from 189:1 to 324:1
- **Evidence**: Same aggregate usage data pull as Claims 2–3.
- **Confidence**: emerging (self-reported aggregate telemetry, no methodology disclosed,
  but a specific and checkable-in-principle ratio)
- **Quote**: "Context per request has grown 2.6x. The input to output token ratio moved from 189:1 to 324:1."
- **Our assessment**: This is the single most citable number in the post for cost-
  modeling purposes: it quantifies why cache-read pricing (rather than output pricing)
  increasingly dominates the Claude Code cost structure, and directly motivates Claim 5
  (the 60% cache-read price cut). A 324:1 input:output ratio means the overwhelming
  majority of billed tokens on a typical session are input/cache-read tokens, not
  output.

### Claim 5: Opus 5.5 pricing cuts input and output tokens 20% and cached token reads 60% versus Opus 5, making a cached token on Opus 5.5 cost a fifth of what competing models charge as of publication
- **Evidence**: Stated pricing change, directly tied to the aggregate cache-read-
  dominant usage pattern described in Claim 4.
- **Confidence**: settled (specific, vendor-stated pricing figures, consistent with the
  companion Anthropic announcement page's pricing table: $4/$20/$0.20 per million
  input/output/cache-read tokens, a 20%/20%/60% cut from Opus 5's $5/$25/$0.50)
- **Quote**: "For usage billed by the token, we reduced the cost of input and output tokens 20%, and we dropped the price of reading a cached token 60%. The latter reduction is significant because cache reads make up the majority of agentic and coding work costs."
- **Our assessment**: The framing is explicit that the pricing cut is sized to match
  where the cost actually accumulates (cache reads, per Claim 4), rather than being an
  across-the-board discount. A separate sentence later in the same section adds: "As of
  the publication date, a cached token on Opus 5.5 costs a fifth of what it does
  compared to competing models while outperforming them" — a point-in-time claim with
  no named competitor or source cited; treat as directional marketing framing, not an
  audited comparison.

### Claim 6: Claude Code's rate of cache misses decreased by more than 50%, driven by harness fixes that prevent accidental cache invalidation (e.g., login refreshes, mid-conversation instruction additions, on-demand tool loading)
- **Evidence**: Stated as a measured outcome of "many of the Claude Code features
  we've added in the last six months," described as counterintuitive given the
  increased session length/context trend documented in Claims 2–4.
- **Confidence**: emerging (specific percentage, but self-reported with no
  methodology, baseline period, or measurement definition of "cache miss" disclosed)
- **Quote**: "Given the coding session trends we just discussed, you would expect a higher rate of cache misses, but the opposite is true. Input that misses the cache decreased by more than 50%. For example, we made it harder to unintentionally break your cache with smaller papercuts like refreshing a login. We also made it harder to break with larger actions, like adding instructions mid-conversation or loading tools on demand."
- **Our assessment**: This complements, and does not contradict, the harness-level cache
  discipline documented in `blog-anthropic-prompt-caching-everything.md` (see
  Cross-References). That April 2026 article describes the *design principles*
  (static-first prompt structure, `<system-reminder>` injection, deterministic tool
  ordering, `defer_loading` MCP stubs) that make caching robust; this September 2026
  post reports the *aggregate outcome* of applying those principles plus newer fixes
  (login-refresh handling, mid-conversation instruction additions, on-demand tool
  loading) over the following five months.

### Claim 7: For Opus 5.5 and Fable 5.1, changing effort level during a session no longer resets the prompt cache
- **Evidence**: Stated as a harness/model-pairing change specific to "newer models like
  Opus 5.5 and Fable 5.1."
- **Confidence**: settled (specific, checkable operational behavior change), though the
  companion "cost of a task" article (Addy Osmani, see Extraction Notes) qualifies this
  as conditional on billing surface — see Our assessment
- **Quote**: "For newer models like Opus 5.5 and Fable 5.1, you can now change effort levels during your sessions without resetting your cache."
- **Our assessment**: This directly reverses prior guidance in this corpus that
  changing settings mid-session busts the cache (e.g.
  `blog-anthropic-maximizing-session-value.md`'s TL;DR: "Set your model and effort
  level before you start. Changing either one mid-conversation can bust your prompt
  cache"). The companion cost-mechanics article linked from this post narrows the claim:
  it states effort changes preserve the cache "with an API key or a Claude
  subscription," but still clear the cache on "Amazon Bedrock, Google Cloud's Agent
  Platform or a Claude apps gateway." This post's blanket phrasing ("you can now change
  effort levels ... without resetting your cache") omits that billing-surface caveat —
  worth flagging for the guide rather than treating as an unconditional behavior change.

### Claim 8: Developers on API keys and cloud providers can now set a one-hour cache lifetime (previously subscriber-only), and forked subagents start from the parent's cache instead of re-paying for the same context
- **Evidence**: Stated as a Claude Code harness change; the one-hour TTL mechanism is
  also documented in Anthropic's prompt-caching docs (`code.claude.com/docs/en/prompt-
  caching`), which name the specific settings.
- **Confidence**: settled (specific, checkable operational feature; corroborated by the
  linked prompt-caching documentation, which names the `promptCacheTtl` setting and
  `CLAUDE_CODE_PROMPT_CACHE_TTL` environment variable, and the `subagentPromptCacheTtl`
  / `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` equivalents for subagents)
- **Quote**: "Developers on API keys and cloud providers can now set a one-hour cache lifetime (which subscribers already had) and forked subagents start from the parent's cache instead of paying for the same context again."
- **Our assessment**: This is a genuinely new corpus data point: subagents inheriting
  the parent's cache on fork was not previously documented in this corpus's caching
  notes (`blog-anthropic-prompt-caching-everything.md` describes cache-safe forking for
  *compaction*, not for spawning subagents). If accurate, this changes the cost calculus
  for delegation-heavy multi-agent patterns — a subagent spawned mid-session would no
  longer need to cold-read the accumulated parent context. Worth a dedicated follow-up
  check against the harness release notes, since this post is the only source in the
  corpus asserting it.

### Claim 9: Opus 5.5 can need fewer turns than other models to accomplish the same task; in a Zeta Labs case study it used fewer turns and tool calls than Opus 5, at nearly half the cost, with twice as many of their hardest tasks completed
- **Evidence**: Named customer case study (Zeta Labs), stated in-line with no
  quantified turn-count or task-count figures, no link to a fuller case study, and no
  description of Zeta Labs' business or task set.
- **Confidence**: anecdotal (single named customer, no disclosed methodology, no
  verifiable numbers beyond "nearly half the cost" and "twice as many")
- **Quote**: "Zeta Labs saw fewer turns and tool calls per task than Opus 5, but at nearly half the cost and twice as many of their hardest tasks completed."
- **Our assessment**: This is a paraphrase/summary of a case study, not a direct quote
  from Zeta Labs — no named individual or title is attached, unlike the customer quotes
  on the companion `anthropic.com/claude-opus-5-5` page (e.g. Quantium, Spotify,
  Optiver, none of which mention Zeta Labs by that name). Treat as a single-customer
  anecdote illustrating the "fewer turns" mechanism, not as a general efficiency
  benchmark.

### Claim 10: Turn-count savings from Opus 5.5 are task-dependent — well-scoped tasks see the same turn count (price cut only), while open-ended tasks see the largest turn reduction, because a model can otherwise spend many turns pursuing a wrong approach
- **Evidence**: Direct quote attributed to Addy Osmani, from the linked companion post
  "The cost of a task on Opus 5.5" (`claude.com/blog/what-a-task-costs-on-opus-5-5`).
- **Confidence**: settled (specific, falsifiable claim about where the savings mechanism
  applies, attributed to a named author on a companion first-party post)
- **Quote**: "On a well-scoped task, both models finish in about the same number of turns, and the price cut is all you get. The gap should be biggest on open-ended tasks, where a model can spend many turns on the wrong idea. No single number holds for every codebase, so measure it."
- **Our assessment**: This is the most important qualifier in the whole post: it
  explicitly rules out interpreting the Zeta Labs case study (Claim 9) or the "fewer
  turns" framing (this claim's headline) as a universal expectation. The companion post
  (verified directly, see Extraction Notes) frames this as a general principle backed by
  the mechanics of turn-based billing, not a vendor benchmark number — it is the
  strongest, most self-critical piece of evidence in either post and should anchor any
  guide passage citing the "Opus 5.5 needs fewer turns" claim.

### Claim 11: Opus 5.5 generates output more than 30% faster than Opus 5, which reduces wait time on long runs without itself increasing cache hit rate or reducing token usage
- **Evidence**: Stated performance figure, explicitly scoped by the post as orthogonal
  to the cost-saving mechanisms (pricing, cache hit rate) described elsewhere in the
  post.
- **Confidence**: settled (specific figure, corroborated verbatim by the companion
  `anthropic.com/claude-opus-5-5` announcement page: "Opus 5.5 also generates output
  more than 30% faster than Opus 5")
- **Quote**: "Opus 5.5 generates output more than 30% faster than Opus 5. While this doesn't increase cache hit rate or use less tokens, it means waiting less on long runs."
- **Our assessment**: The post is careful to separate this from the cost-saving
  mechanisms — it is a latency improvement, not an economic one. Relevant to guide
  passages about "waiting on Claude" during long unattended/uninterrupted runs, distinct
  from token-cost guidance.

### Claim 12: To protect cached-read spend, developers should pick their model at the start of a session rather than switching mid-session, compact before stepping away rather than after, and (on API key or cloud provider billing) set the one-hour cache lifetime for long sessions
- **Evidence**: Stated as direct practitioner recommendations, framed around running
  `/usage` in Claude Code to see how much of current usage is cached reads.
- **Confidence**: settled (direct, actionable first-party guidance, consistent with
  prior corpus guidance — see Cross-References)
- **Quote**: "Run /usage in Claude Code to see how much of your usage is cached reads. Then protect that number: Pick your model at the start of a session rather than switching midway, Compact before you step away rather than after, and If you're on an API key or cloud provider, set the one-hour cache lifetime for long sessions."
- **Our assessment**: This overlaps substantially with guidance already captured in
  `blog-anthropic-maximizing-session-value.md`'s TL;DR, which separately advises
  setting model and effort level before starting a session and compacting before a
  break (see that note's Concrete Artifacts / TL;DR for its own wording). This post
  adds one new, dated-specific practice not in that August 2026 note: setting a
  one-hour cache TTL is now available to API-key and cloud-provider users, not just
  subscribers (see Claim 8) — the August note predates that availability change.

### Claim 13: Organizations have shifted from asking developers to "scale at all costs" to asking developers to "scale efficiently," as agentic coding has matured
- **Evidence**: Framing statement, unattributed to any specific data source; presented
  as Anthropic's own characterization of the market/practitioner mood.
- **Confidence**: anecdotal (unattributed characterization, not tied to any of the
  quantified telemetry elsewhere in the post)
- **Quote**: "As agentic coding has matured, organizations have shifted from asking developers to scale at all costs to asking developers to scale efficiently."
- **Our assessment**: This is scene-setting rhetoric, not a data claim — no survey, quote,
  or customer citation backs it. Useful only as framing color for a guide section on the
  maturation of organizational AI-adoption posture, not as evidence in its own right.

## Concrete Artifacts

### Full article text (verbatim, extracted from raw page HTML, published 2026-09-24)

```
Source: https://claude.com/blog/claude-opus-5-5-built-for-coding-sessions-that-use-more-context

We estimate Claude Opus 5.5 costs about 40% less to run than Opus 5 for typical
workloads billed by token. For developers, exactly how those savings stack up
matters. If you pay by the token, you will see the greatest cost difference for
longer-running, higher context sessions–the exact type of Claude Code sessions
that have become more prevalent in the last six months. This post will dive into
the mechanics of what makes Opus 5.5 cost effective for how developers are coding
today (and likely tomorrow).

## Claude Code trends

We've pulled aggregate data on how developers have been using Claude Code from
March to September 2026. As model capabilities improve, developers have been
deploying agents in increasingly sophisticated ways. The number of prompts per
session has been steady, but we found some interesting behaviors:

- Claude works 3.3x longer on each prompt with more than 40% more model calls
  per prompt. There are 68% fewer interruptions.
- Developers are about twice as likely to have a tool server connected or use a
  skill and a third less likely to paste text into a prompt.
- Context per request has grown 2.6x. The input to output token ratio moved
  from 189:1 to 324:1.

All of this points to developers aiming a harder working, better informed
Claude toward bigger, more open-ended tasks. For these types of sessions, the
economic impact of context engineering is compounded. Simply put, Claude reads
more tokens. You need to make sure all the context you are providing is
necessary, and that as much of that context as possible is reading from cache.

## What makes Opus 5.5 cost effective for long, context heavy sessions

There are three changes that make long-running, context-heavy sessions more
cost effective: changes to pricing, model behavior, and the Claude Code
harness. Let's look at each.

### Cache is cheap

For usage billed by the token, we reduced the cost of input and output tokens
20%, and we dropped the price of reading a cached token 60%. The latter
reduction is significant because cache reads make up the majority of agentic
and coding work costs. And as we just discussed, context per request has
increased roughly 2.6x in six months, which means savings are trending in the
right direction. The same price change for those billed by token saves more on
today's Claude Code traffic than it would have six months ago, because more of
the bill is now re-read context. As of the publication date, a cached token on
Opus 5.5 costs a fifth of what it does compared to competing models while
outperforming them.

### Claude Code is better at using the cache

This is less specific to Opus 5.5, and more the result of many of the Claude
Code features we've added in the last six months. Given the coding session
trends we just discussed, you would expect a higher rate of cache misses, but
the opposite is true. Input that misses the cache decreased by more than 50%.
For example, we made it harder to unintentionally break your cache with
smaller papercuts like refreshing a login. We also made it harder to break
with larger actions, like adding instructions mid-conversation or loading
tools on demand. For newer models like Opus 5.5 and Fable 5.1, you can now
change effort levels during your sessions without resetting your cache.

We also made the cache more useful for longer-running and delegated sessions.
Developers on API keys and cloud providers can now set a one-hour cache
lifetime (which subscribers already had) and forked subagents start from the
parent's cache instead of paying for the same context again.

### The same task, but with fewer turns

Opus 5.5 can need fewer turns than other models to accomplish the same task.
Zeta Labs saw fewer turns and tool calls per task than Opus 5, but at nearly
half the cost and twice as many of their hardest tasks completed.

This won't hold for every task. In The cost of a task on Opus 5.5, Addy wrote,
"On a well-scoped task, both models finish in about the same number of turns,
and the price cut is all you get. The gap should be biggest on open-ended
tasks, where a model can spend many turns on the wrong idea. No single number
holds for every codebase, so measure it."

In other words, simple, short, and mechanical tasks will take the same amount
of turns while longer, harder tasks have more potential for Opus 5.5 to avoid
burning tokens on the wrong approach. A reduced turn is even more cost
efficient than a cached token.

Also worth noting, especially as Claude works longer unattended or
uninterrupted, is that Opus 5.5 generates output more than 30% faster than
Opus 5. While this doesn't increase cache hit rate or use less tokens, it means
waiting less on long runs.

## Protect your cached reads

As agentic coding has matured, organizations have shifted from asking
developers to scale at all costs to asking developers to scale efficiently.
Run /usage in Claude Code to see how much of your usage is cached reads. Then
protect that number:

- Pick your model at the start of a session rather than switching midway,
- Compact before you step away rather than after, and
- If you're on an API key or cloud provider, set the one-hour cache lifetime
  for long sessions.

Point Opus 5.5 at the open-ended, context-heavy work where those habits
compound, and see What a task costs on Opus 5.5 for the worked numbers.
```

### Six-month usage telemetry (March-September 2026), reformatted

```
# Aggregate Claude Code usage change, March 2026 -> September 2026
# Source: claude.com/blog/claude-opus-5-5-built-for-coding-sessions-that-use-more-context

Per-prompt duration:        3.3x longer
Model calls per prompt:     +40% or more
Session interruptions:      -68%
Tool server / skill usage:  ~2x more likely
Pasted text into prompt:    ~1/3 less likely
Context per request:        2.6x growth
Input:output token ratio:   189:1 -> 324:1
```

### Opus 5.5 vs Opus 5 pricing (as stated in this post, corroborated by anthropic.com/claude-opus-5-5)

```
                    Opus 5      Opus 5.5     Change
Input tokens        $5/M        $4/M         -20%
Output tokens       $25/M       $20/M        -20%
Cache reads         $0.50/M     $0.20/M      -60%

Cache misses (aggregate, Claude Code): -50%+ vs six months earlier
Output generation speed: +30%+ faster than Opus 5
```

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-opus55-availability.md` (Claim 2): GitHub's changelog states
    Opus 5.5 "resolved tasks comparably to Claude Opus 5 while using significantly fewer
    steps and tokens" with no disclosed methodology. This post's "fewer turns" mechanism
    (Claims 9-10) and Addy Osmani's qualifier (Claim 10) give the fuller, more
    self-critical version of the same underlying claim: fewer turns is real but
    task-dependent, not a flat efficiency multiplier as the bare Copilot changelog
    phrasing might suggest.
  - `blog-anthropic-prompt-caching-everything.md` (Claims 1, 3, 7): that April 2026
    first-party post establishes caching as the foundational economic mechanism for
    Claude Code and names the specific harness-level anti-patterns (tool-set changes,
    non-deterministic tool ordering) that break the cache. This post's "cache misses
    decreased by more than 50%" (Claim 6) is the aggregate, dated outcome of continuing
    to apply and extend those design principles.
  - `blog-anthropic-maximizing-session-value.md`: near-identical session-management
    guidance (pick model/effort before starting, compact before stepping away) appears
    in that August 2026 post's TL;DR, restated here in Claim 12. This post is not novel
    on that guidance but reconfirms it five weeks later, at the Opus 5.5 launch.

- **Contradicts**: None filed as a formal contradiction issue. Note one tension worth
  flagging for editorial awareness rather than a contradiction issue: this post states
  flatly that "you can now change effort levels during your sessions without resetting
  your cache" for Opus 5.5/Fable 5.1 (Claim 7), while `blog-anthropic-maximizing-
  session-value.md`'s TL;DR (predating this post by ~6 weeks) instructs "Set your model
  and effort level before you start. Changing either one mid-conversation can bust your
  prompt cache" with no model-specific carve-out. This reads as the August guidance
  being superseded by a September model/harness change (not a genuine disagreement
  between two sources describing the same moment in time), so per MINER.md §4a this
  is a conditioning-variable case (a capability that arrived later), not a
  contradiction to file. The guide should date the effort-level exception explicitly
  to Opus 5.5/Fable 5.1 onward, and per the companion cost-mechanics article, further
  scope it to API-key/Claude-subscription billing (not Bedrock, Google Cloud's Agent
  Platform, or a Claude apps gateway).

- **Extends**:
  - `blog-anthropic-prompt-caching-everything.md` Claim 11 (cache-safe forking during
    compaction reuses the parent's cached prefix): this post's Claim 8 (forked
    subagents start from the parent's cache) describes a related but distinct
    mechanism — cache inheritance on subagent *spawn*, not on compaction. Neither prior
    corpus source documents subagent-fork cache inheritance; this is new.
  - `docs-github-copilot-opus55-availability.md`: that source documents Opus 5.5's
    GitHub Copilot availability, plan gating, and an undisclosed-methodology efficiency
    claim, with explicit no-pricing-disclosed caveats. This post fills exactly the gap
    that note's "Our assessment" flagged — concrete percentage figures for the pricing
    cut (20%/20%/60%) and the usage telemetry behind it — for the Claude-first-party
    (not Copilot-integration) surface.

- **Novel**:
  - The six-month aggregate Claude Code usage telemetry (Claims 2-4) — session length
    growth, interruption rate, tool-server/skill adoption, context growth, input:output
    ratio shift — is not present in any other mined source in this corpus.
  - Subagent fork cache inheritance (Claim 8) is a newly documented harness mechanism.
  - The Addy Osmani turn-parity qualifier (Claim 10) is the sharpest available
    statement in the corpus of when "fewer turns" claims for a new model do and do not
    apply.

## Guide Impact

- **Chapter 04 (Model Selection and Cost Management)**: Add the Opus 5.5 pricing cut
  (20% input/output, 60% cache reads, Claim 5) and the aggregate usage telemetry (Claims
  2-4) as the current evidentiary basis for "pick models based on session shape, not
  just capability" guidance. Cite Addy Osmani's turn-parity qualifier (Claim 10)
  explicitly alongside any "Opus 5.5 needs fewer turns" framing, so the guide does not
  imply a universal efficiency multiplier — the Zeta Labs anecdote (Claim 9) should be
  labeled a single-customer case study, not a general benchmark.

- **Chapter 04 (Prompt Caching / Cache Economics)**: Update any existing "changing
  effort level busts the cache" guidance (currently sourced to
  `blog-anthropic-maximizing-session-value.md`) with the Opus 5.5/Fable 5.1 exception
  (Claim 7), dated to this September 2026 change and scoped to API-key/subscription
  billing per the linked companion cost-mechanics post. Add the one-hour cache TTL's
  new availability to API-key and cloud-provider users (Claim 8), not just subscribers,
  as a session-cost lever for Ch04's practitioner checklist.

- **Chapter 03/05 (Multi-Agent / Delegation Patterns)**: If corroborated by a
  harness-release-notes source, add subagent-fork cache inheritance (Claim 8) as a cost
  consideration for delegation-heavy multi-agent workflows — spawning a subagent mid-
  session may no longer require a cold re-read of the parent's accumulated context.
  Flag as single-source until corroborated, since this post is the only corpus source
  asserting it.

## Extraction Notes

1. **WebFetch was insufficient for verbatim quoting.** An initial WebFetch pass against
   the source URL returned only an AI-generated summary, not the source's own wording.
   The full article text used for every `Quote` field above was instead extracted by
   fetching the raw page HTML directly (`curl`), isolating the `data-readtime="content"`
   rich-text div, stripping tags, and decoding HTML entities — the same character-
   verification approach used in `docs-github-copilot-opus55-availability.md`.
2. **Followed 4 of the 5 linked pages per MINER.md §1**, to verify quotes attributed to
   them and to check for contradictions/overlaps:
   - `anthropic.com/claude-opus-5-5` (the companion capability/benchmark announcement) —
     used to corroborate the 40% cost figure, the pricing table, and the 30%+ output
     speed figure (Claims 1, 5, 11); confirmed the Zeta Labs case study does not appear
     by that name among the named customer quotes on that page (Quantium, Spotify,
     Optiver, and others), supporting the "unattributed paraphrase, not a direct quote"
     read of Claim 9.
   - `claude.com/blog/what-a-task-costs-on-opus-5-5` (by Addy Osmani) — read in full to
     verify the Claim 10 quote verbatim and to confirm its authorship; this is a rich,
     separate companion post (pricing mechanics, effort-level guidance, a worked-numbers
     calculator) that would merit its own dedicated source-note issue — it is not fully
     extracted here since it is outside this issue's source URL, and no existing source
     note in this corpus covers it (checked: no `blog-addyosmani-*.md` file references
     it).
   - `code.claude.com/docs/en/prompt-caching` — used to verify the one-hour TTL
     mechanism (Claim 8) and confirm the `promptCacheTtl` / `CLAUDE_CODE_PROMPT_CACHE_TTL`
     setting names, and the billing-surface-dependent default TTL behavior referenced in
     the Claim 7 assessment.
   - `claude.com/blog/maximizing-the-value-of-your-claude-code-sessions` — confirmed
     this already has a dedicated source note (`blog-anthropic-maximizing-session-
     value.md`); read enough to confirm the TL;DR overlap described in Claim 12 and
     Cross-References, not re-extracted in full here.
   - Not followed: `claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-
     generation-models` — already has a dedicated source note in this corpus
     (`blog-anthropic-context-engineering-claude-5.md`, issue #2218), so re-extraction
     was skipped per the existing-notes check in MINER.md §1(e).
3. No paywall or access issues; the source and all four followed linked pages were
   fully readable via direct HTTP fetch.
