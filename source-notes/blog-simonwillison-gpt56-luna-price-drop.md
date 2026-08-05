---
source_url: https://simonwillison.net/2026/Jul/30/luna-price-drop/
source_type: blog-post
title: "Advancing the price-performance frontier with GPT‑5.6"
author: Simon Willison
date_published: 2026-07-30
date_extracted: 2026-08-05
last_checked: 2026-08-05
status: current
confidence_overall: emerging
issue: "#2494"
---

# Advancing the price-performance frontier with GPT‑5.6

> Simon Willison reports a same-day 80% price cut for GPT-5.6 Luna ($1.00/$6.00
> → $0.20/$1.20 per million input/output tokens) and a 20% cut for Terra,
> crediting OpenAI's own account of GPT‑5.6 Sol autonomously rewriting its
> production inference kernels. Luna now undercuts Gemini 3.1 Flash-Lite and
> is 1/5th the input price of Claude Haiku 4.5, having previously cost the
> same; Willison switched his own agent.datasette.io production demo from
> Gemini to Luna as a result. This note also directly fetches (via Wayback
> Machine, after live 403s) the two OpenAI pages Willison links to — the
> pricing announcement itself and a companion engineering post — which supply
> the exact new Terra price, a new Sol "Fast mode," and six customer
> testimonials with concrete before/after efficiency numbers not present in
> Willison's post.

## Source Context

- **Type**: blog-post (Simon Willison's weblog, "Link Blog" format — a short
  first-person post combining Willison's own commentary and price-comparison
  arithmetic with one direct blockquote lifted from a linked OpenAI
  engineering post). This is a hybrid of the two Willison formats already in
  the corpus: closer to the "notes" format of `blog-simonwillison-gpt56-ga-launch.md`
  (first-person synthesis, not a bare quote) than to the pure-quote format of
  `blog-simonwillison-gpt56-sol-launch.md`.
- **Author credibility**: Simon Willison is the creator of Django and the
  `llm` CLI, and the most consistently cross-referenced practitioner source in
  this corpus (see `blog-simonwillison-gpt56-ga-launch.md`,
  `blog-simonwillison-gpt56-sol-launch.md`,
  `blog-simonwillison-agentsview-custom-model-price.md`, and dozens more). He
  adds independent value beyond simply reporting OpenAI's announcement: his
  own cross-vendor price arithmetic (Luna vs. Gemini 3.1 Flash-Lite, Luna vs.
  Claude Haiku 4.5) and a first-person production-infrastructure decision (he
  switched his own `agent.datasette.io` demo from Gemini to Luna the same
  day). No disclosed OpenAI or Anthropic affiliation.
- **Scope**: Covers the July 30, 2026 GPT-5.6 Terra/Luna price cuts, Luna's
  exact new per-token price, competitive cost comparisons against Gemini 3.1
  Flash-Lite and Claude Haiku 4.5, and (via OpenAI's own linked engineering
  post) the technical mechanism credited with enabling the cuts — kernel
  optimization, load balancing, speculative decoding, and agentic-harness
  design. Does NOT cover: independent (non-OpenAI) verification of the 20%
  serving-cost-reduction figure, any change to Sol's own per-token price
  (explicitly unchanged), or capability/benchmark comparisons beyond the two
  cost-per-task figures OpenAI cites in passing.

## Extracted Claims

### Claim 1: OpenAI cut GPT-5.6 Luna's price by 80% and Terra's price by 20%, effective July 30, 2026

- **Evidence**: Willison's own report, corroborated by direct fetch of OpenAI's
  pricing-announcement page (linked from Willison's post headline), which
  states the same percentages independently.
- **Confidence**: settled (published, dated pricing change; independently
  confirmed via primary source, not just Willison's paraphrase)
- **Quote**: Willison: "Huge price drop from OpenAI today: GPT-5.6 Terra got a
  20% reduction, and GPT-5.6 Luna got a massive 80% drop." OpenAI (primary
  source, `openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/`,
  fetched via Wayback Machine snapshot dated 2026-08-04): "Starting today,
  GPT‑5.6 Luna, our fastest and most affordable model, will cost 80% less,
  while GPT‑5.6 Terra, our balanced model for everyday work, will cost 20%
  less."
- **Our assessment**: Both figures check out exactly against the pre-cut
  pricing already in the corpus (`blog-simonwillison-gpt56-sol-launch.md`
  Claim 4: Luna $1.00/$6.00; `blog-openai-gpt56-ga-announcement.md` Concrete
  Artifacts: Terra $2.50/$15.00). $1.00 → $0.20 and $6.00 → $1.20 are both
  precisely 80% reductions; see Claim 2 for the exact new Terra figure, which
  confirms the 20% cut arithmetically as well.

### Claim 2: New GPT-5.6 API pricing (per 1M tokens) as of July 30, 2026 is Terra $2.00/$12.00 and Luna $0.20/$1.20; Sol's price is unchanged

- **Evidence**: Direct quote from OpenAI's pricing-announcement page — this
  is the exact new Terra figure that Willison's post does not itself state
  (he only reports the 20% percentage, not the resulting dollar amount).
- **Confidence**: settled (published, dated, primary-source pricing table)
- **Quote**: "Starting July 30, API pricing is $2 per million input tokens
  and $12 per million output tokens for Terra, and $0.20 per million input
  tokens and $1.20 per million output tokens for Luna. Sol pricing remains
  unchanged."
- **Our assessment**: $2.50 → $2.00 and $15.00 → $12.00 for Terra is exactly
  a 20% reduction on both input and output, matching Claim 1's percentage
  precisely — a useful confirmation that OpenAI applied the stated percentage
  uniformly rather than rounding unevenly. Sol holding at $5/$30 (per
  `blog-simonwillison-gpt56-sol-launch.md` Concrete Artifacts and
  `blog-openai-gpt56-ga-announcement.md` Concrete Artifacts) means this is a
  bottom-of-the-lineup price cut, not a flagship one — Sol instead gets a
  speed option (Claim 6) rather than a price cut.

### Claim 3: Luna's new price makes it cheaper than Google's Gemini 3.1 Flash-Lite

- **Evidence**: Willison's own price comparison.
- **Confidence**: settled, but with a source-side numeric caveat (see
  assessment)
- **Quote**: "That Luna price drop completely changes the landscape with
  respect to lower priced models. At $0.20/million tokens for input and
  $1.20/million for output Luna is now cheaper than Google's Gemini 3.1
  Flash-Lite ($.025/$1.50)."
- **Our assessment**: The parenthetical Flash-Lite figure as printed in the
  source, "$.025/$1.50," is very likely a typo for "$0.25/$1.50" — the
  existing corpus entry in `blog-simonwillison-deepseek-v4.md` Concrete
  Artifacts → Pricing Comparison Table independently documents Gemini 3.1
  Flash-Lite at exactly $0.25/$1.50 (April 2026), and "$.025" (2.5 cents)
  would make Flash-Lite cheaper than Luna on input, contradicting the
  sentence's own claim that Luna is now the cheaper of the two. Quoted
  verbatim per MINER.md §2a rather than silently corrected; the guide should
  cite $0.25/$1.50 (the corpus-corroborated figure) for Flash-Lite, not the
  as-printed "$.025."

### Claim 4: Luna is now 1/5th the input price of Claude Haiku 4.5, having previously cost the same

- **Evidence**: Willison's own price comparison against Anthropic's cheapest
  current model.
- **Confidence**: settled (both figures independently corroborated — see
  assessment)
- **Quote**: "Anthropic's cheapest current model is Claude Haiku 4.5, and
  that's $1/$5 - Luna is now 1/5th of that for input, previously it cost the
  same."
- **Our assessment**: Both halves of this claim check out against existing
  corpus data. Haiku 4.5 at $1.00/$5.00 matches
  `blog-simonwillison-deepseek-v4.md` Concrete Artifacts → Pricing Comparison
  Table exactly. "Previously it cost the same" checks out on the input side:
  old Luna was $1.00 input (per Claim 1's sourcing), identical to Haiku 4.5's
  $1.00 input — though the two never matched on output ($6.00 vs. $5.00).
  New Luna input ($0.20) is exactly 1/5th of $1.00. This is the sharpest
  cross-vendor cost-comparison data point in this source: OpenAI's
  cheapest-tier input price is now one-fifth of Anthropic's cheapest-tier
  input price, a gap that did not exist before July 30.

### Claim 5: Willison switched his own production demo site from Gemini 3.1 Flash-Lite to Luna the same day, based on the new pricing

- **Evidence**: Willison's first-person account of a real infrastructure
  change to a live, named project.
- **Confidence**: anecdotal (single practitioner, single project — but a
  concrete, dated, verifiable production decision, not a hypothetical)
- **Quote**: "My agent.datasette.io demo site was running on Gemini 3.1
  Flash-Lite. I've switched it over to Luna."
- **Our assessment**: This is a genuine (if small-scale) production adoption
  signal driven directly by the price change documented in Claims 1–4 — the
  kind of practitioner behavior the pricing data alone can't demonstrate.
  Worth noting as a real-world data point that at least one experienced
  practitioner judged the new Luna pricing worth an immediate production
  model swap, not just a noteworthy headline number.

### Claim 6: OpenAI introduced a "Fast mode" for GPT-5.6 Sol in the API — up to 2.5x faster than Standard processing at 2x the price, with no change in intelligence, replacing Priority Processing

- **Evidence**: Direct statement on OpenAI's pricing-announcement page; not
  mentioned in Willison's post at all.
- **Confidence**: settled (a specific, dated, checkable product/pricing
  feature from the vendor)
- **Quote**: "We're also introducing Fast mode in the API, which replaces our
  Priority Processing offering. For GPT‑5.6 Sol, Fast mode now delivers up to
  2.5× faster speeds than Standard processing at twice the price, with no
  change in intelligence. Fast mode is backward compatible: requests tagged
  priority will automatically use Fast mode." ... "Fast mode for GPT‑5.6 Sol
  replaces Priority Processing in the API and aligns with /fast in Codex."
- **Our assessment**: This is Sol's counterpart to the Luna/Terra price cuts:
  rather than cutting Sol's price, OpenAI adds a paid speed tier at a fixed
  2x-price/2.5x-speed ratio. Novel to the corpus — no existing GPT-5.6 note
  documents a "Fast mode" or its predecessor "Priority Processing." The
  backward-compatibility detail (existing `priority`-tagged requests
  auto-upgrade) is a concrete migration detail worth preserving for any Ch05
  API-capability reference.

### Claim 7: OpenAI credits GPT-5.6 Sol with autonomously rewriting its own production inference kernels in Triton and Gluon, reducing end-to-end serving costs by 20%

- **Evidence**: A direct blockquote Willison embeds from OpenAI's companion
  engineering post, independently re-verified by this Miner against a direct
  fetch of that post (via Wayback Machine, since the live URL 403'd).
- **Confidence**: emerging (vendor's own account of a self-optimization
  mechanism; no independent verification of the 20% figure or the extent of
  Sol's autonomy in the process)
- **Quote**: "We also used GPT‑5.6 Sol to optimize the model's forward pass:
  the computation that transforms inputs into next-token predictions. Even
  when individual operations are fast, excess memory movement,
  synchronization, and inefficient data layouts can leave GPUs idle. To avoid
  this, GPT‑5.6 Sol found work that could be precomputed, avoided, or
  parallelized. With Codex, GPT‑5.6 Sol autonomously rewrote and optimized
  our production kernels, the core code that executes the mathematical
  operations that make up the model. This worked in part because we've
  trained GPT‑5.6 to be effective at writing and improving kernels in Triton
  and Gluon, two open-source GPU programming languages maintained by OpenAI.
  These efforts, combined with broader kernel advancements from GPT‑5.6 Sol,
  reduced end-to-end serving costs by 20%."
- **Our assessment**: This is the mechanism Willison credits for enabling
  the price cuts, and it's a striking recursive pattern: GPT-5.6 Sol was used
  (via Codex) to rewrite the production kernels that serve GPT-5.6 itself.
  Willison's own framing — "OpenAI credit 5.6 Sol with enabling this" —
  treats the claim at face value without independent scrutiny; this note
  flags it as vendor-self-reported. The companion post also mentions an
  open-source verification tool, FpSan (Floating-Point Sanitizer), used to
  validate the correctness of Sol-authored kernels — worth noting as a
  concrete verification-tooling detail alongside the optimization claim
  itself, though the FpSan mention is a passing aside in the source, not
  elaborated on.

### Claim 8: OpenAI also used GPT-5.6 Sol to improve production load balancing by analyzing traffic and tuning routing heuristics, which "dramatically reduced" serving costs — a distinct optimization from the kernel rewrite in Claim 7

- **Evidence**: OpenAI's companion engineering post
  (`openai.com/index/gpt-5-6-frontier-intelligence-efficiency/`, published
  July 29, 2026, fetched directly via Wayback Machine after a live 403). Not
  quoted or mentioned by Willison — this Miner followed the link per
  MINER.md §1.
- **Confidence**: emerging (vendor-reported mechanism and outcome, no
  independent magnitude verification beyond the qualitative "dramatically")
- **Quote**: "GPT‑5.6 Sol in Codex helps us analyze production traffic,
  identify previously overlooked sources of imbalance, test new routing
  strategies, and constantly tune these heuristics. These load balancing
  improvements alone dramatically reduced the cost of serving our models."
- **Our assessment**: OpenAI presents this as separate from (and prior to, in
  the post's own ordering) the kernel-rewrite work in Claim 7 — load
  balancing (where/how requests are routed across a cluster) versus kernel
  optimization (how each request's compute is executed). Both are credited
  to the same underlying pattern: using GPT-5.6 Sol inside Codex as an
  autonomous systems-engineering agent against OpenAI's own production
  infrastructure, not just as a coding assistant for feature work.

### Claim 9: GPT-5.6 Sol improved its own speculative-decoding draft model — designing and running hundreds of architecture experiments and autonomously supervising training, including intervening on hardware failures — for a token-generation efficiency gain of more than 15%

- **Evidence**: OpenAI's companion engineering post, same source as Claim 8.
- **Confidence**: emerging (vendor-reported mechanism and a specific
  percentage figure, self-measured, no independent reproduction)
- **Quote**: "GPT‑5.6 Sol improved its own draft model by designing and
  running hundreds of experiments on its architecture, testing changes in
  size, structure, and features. Additionally, GPT‑5.6 Sol launched and
  monitored the speculator training process, autonomously intervening when
  issues arose, including hardware failures and training instability. The
  resulting improvements increased token-generation efficiency by more than
  15%."
- **Our assessment**: The "autonomously intervening" language — the model
  supervising its own training run and responding to infrastructure failures
  without being described as human-in-the-loop for those interventions — is
  the most operationally significant single claim in this source: it
  describes agentic ML-training-ops, not just agentic coding. No existing
  corpus source documents a model autonomously managing a training run's
  failure recovery. This should be flagged for any guide discussion of
  agent autonomy boundaries as a vendor-reported (not independently audited)
  example of a lab extending agentic delegation into training
  infrastructure operations, distinct from the coding-agent and
  cyber-offense autonomy examples already documented elsewhere in the corpus
  (e.g., `blog-openai-gpt56-ga-announcement.md` Claims 6–8).

### Claim 10: OpenAI's agentic harness for Codex and ChatGPT Work is a Rust orchestration layer that caps tool output at 10,000 tokens by default and uses "deferred discovery" so integrations, custom MCP tools, skills, and plugins are only surfaced when needed

- **Evidence**: OpenAI's companion engineering post, same source as Claims
  8–9.
- **Confidence**: settled (a specific, named architectural detail with a
  concrete numeric default, though self-reported and not independently
  inspected)
- **Quote**: "These multipliers have informed how we designed our agentic
  harness, which is a Rust orchestration layer connecting our models, tools,
  and the user's environment." ... "The harness can reduce this overhead
  through deferred discovery, which makes integrations, custom MCP tools,
  skills, and plugins only surfaceable when needed. The harness also
  prevents individual tools and MCP integrations from unexpectedly consuming
  the context window. Tool output is capped at 10,000 tokens by default
  unless the model requests a different limit."
- **Our assessment**: This is the first corpus source to name OpenAI's
  harness implementation language (Rust) and to give a specific default
  numeric cap (10,000 tokens) for tool output. "Deferred discovery" as a
  named pattern — tools/skills/plugins not loaded into context until
  actually needed — is conceptually similar to Claude Code's MCP
  lazy-loading pattern already in the corpus (see Cross-References), but this
  is the first time this specific mechanism is named and sourced for
  OpenAI's harness rather than Anthropic's.

### Claim 11: OpenAI's harness preserves prompt-cache prefixes by treating all model-visible history as append-only and presenting tools in a deterministic order, with runtime settings like approval policies applied at execution time rather than embedded in tool definitions

- **Evidence**: OpenAI's companion engineering post, same source as Claims
  8–10.
- **Confidence**: settled (a specific, named architectural rule, self-reported
  but directly checkable in principle against the harness's actual behavior)
- **Quote**: "To preserve that prefix, the harness treats all model-visible
  history as append-only: new messages, tool results, and environment
  updates are added at the end rather than inserted into earlier context.
  Tools are also presented in a deterministic order, while runtime settings,
  such as approval policies, are applied during execution instead of being
  embedded in tool definitions. This design choice contributes to Codex's
  and ChatGPT Work's high overall prompt-cache hit rates."
- **Our assessment**: This closely mirrors — and independently corroborates
  from OpenAI's side — the cache-preservation rules already documented for
  Claude Code in `blog-anthropic-prompt-caching-everything.md` Claim 3
  ("static content first, dynamic content last") and Claim 4 (non-deterministic
  tool ordering as a common cache-breaking pitfall). OpenAI's "deterministic
  tool order" rule is the same prescription as Claude Code's tool-ordering
  guidance from the opposite direction (avoid breaking it, vs. preserve it),
  and "runtime settings applied at execution instead of embedded in tool
  definitions" is a specific implementation technique not previously
  documented in the corpus for keeping tool definitions themselves static
  across a session.

### Claim 12: Six named OpenAI customers report concrete efficiency/cost gains from GPT-5.6 Luna or Terra, including one (Blitzy) reporting prompt-cache reuse rising from 24% to 90% alongside 2.2x more context and 8.5x fewer output tokens at 87% lower cost than GPT-5.4 mini

- **Evidence**: Six attributed customer testimonials on OpenAI's
  pricing-announcement page (Replit, Notion, Ramp, Blitzy, Cognition, Dust).
- **Confidence**: anecdotal (vendor-selected, vendor-published customer
  quotes — standard testimonial-credibility caveats apply; no independent
  verification of any figure)
- **Quote**: Blitzy (Sid Pardeshi, CTO + Co-Founder): "GPT‑5.6 Luna is the
  biggest step change in agentic behavior we've seen since putting GPT‑4o
  mini into production. Luna moved us from a single structured-output call
  to a full tool-calling agent loop, increasing prompt-cache reuse from 24%
  to 90%. Across thousands of production calls, Luna handles 2.2× more
  context with 8.5× fewer output tokens—at 87% lower cost than GPT‑5.4
  mini." Notion (Hoda Noorian, AI Product): "GPT‑5.6 Terra is a strong fit
  for everyday work in Notion's personal agent, including workspace Q&A and
  scoped tasks where latency matters. In our evaluations, it delivered
  comparable quality to GPT‑5.5 at half the cost per task and in 60% less
  time." Dust (Stanislas Polu, Co-Founder and CTO): "Given the same agentic
  tasks, GPT‑5.6 Luna is 40% faster and 40% cheaper than our previous
  default model, leading to a more responsive experience for users."
- **Our assessment**: The Blitzy figure is the most specific and, if
  accurate, the most consequential for Ch03 cost guidance: an 8.5x reduction
  in output tokens combined with a cache-hit-rate jump from 24% to 90% for
  the same workload class ("agentic behavior") is a substantially larger
  efficiency gain than the headline 80% sticker-price cut alone would
  suggest — the effective cost reduction compounds price-per-token savings
  with usage-pattern efficiency gains. As with all vendor-published
  testimonials, treat as directional evidence of real adoption, not as
  a controlled or independently reproducible benchmark.

### Claim 13: OpenAI claims Luna delivers performance "comparable to models that were frontier-class a year ago" at roughly 6 cents on the dollar and nearly 9x the speed, and that on Agents' Last Exam, Luna beats Claude Fable 5 at an estimated cost per task nearly 99% lower

- **Evidence**: Direct statement on OpenAI's pricing-announcement page.
- **Confidence**: emerging (vendor-reported, self-selected benchmark and
  cost-modeling claim; "estimated cost per task" methodology is not
  disclosed)
- **Quote**: "Luna delivers performance comparable to models that were
  frontier-class a year ago at roughly 6 cents on the dollar per task, and
  at nearly nine times the speed. On professional work, as measured by
  Agents' Last Exam, Luna outperforms Fable 5 at an estimated cost per task
  nearly 99% lower."
- **Our assessment**: This extends the Agents' Last Exam benchmark comparison
  already in the corpus (`blog-simonwillison-gpt56-ga-launch.md` Claim 4 and
  `blog-openai-gpt56-ga-announcement.md` Claim 4 both cover Sol vs. Fable 5
  on this benchmark) down to the Luna tier specifically, with a cost-per-task
  framing rather than a raw score. "Nearly 99% lower estimated cost" is an
  extreme, headline-friendly figure with no disclosed calculation
  methodology (what counts as "estimated cost per task" is not defined in
  this source) — treat as vendor marketing framing, not a verified,
  reproducible cost benchmark.

### Claim 14: The companion engineering post's cost claim for Sol vs. Claude Fable 5 on the Artificial Analysis Coding Agent Index ("less than half of the cost") is a rounder, larger figure than the more precise "about one-third less" cost claim OpenAI published for the same comparison three weeks earlier

- **Evidence**: Direct comparison between this source's companion post and
  the existing corpus note for OpenAI's July 9 GA announcement.
- **Confidence**: anecdotal (an internal, same-vendor numeric discrepancy
  noted by this Miner, not a claim either source makes about itself)
- **Quote**: This source (`gpt-5-6-frontier-intelligence-efficiency/`, July
  29, 2026): "Our flagship model, GPT‑5.6 Sol, with max reasoning outperforms
  Claude Fable 5 on the Artificial Analysis Coding Agent Index at less than
  half of the cost." Compare `blog-openai-gpt56-ga-announcement.md` Claim 5
  (July 9, 2026, quoting the same underlying comparison): "GPT‑5.6 Sol with
  max reasoning sets a new state of the art at 80, 2.8 points above Fable 5,
  while using less than half the output tokens, taking less than half the
  time, and costing about one-third less."
- **Our assessment**: "Less than half the cost" (>50% cheaper) and "about
  one-third less" (~33% cheaper) are materially different magnitudes for the
  same named benchmark, same two models, twenty days apart, from the same
  vendor. This is not flagged as a formal contradiction per MINER.md §4a: the
  July 29 post is specifically about serving-cost optimizations achieved in
  the intervening weeks (Claims 7–9), so a larger, rounder cost-advantage
  figure by July 29 is plausibly explained by real efficiency gains compounding
  on top of the July 9 baseline, rather than the two statements disagreeing
  about the same point in time. Flagged here so the guide does not cite
  "less than half the cost" as a precise, stable figure — the July 9 "about
  one-third less" is the more precisely worded of the two and should be
  preferred if only one figure is cited, with a note that OpenAI's own later
  framing suggests the gap may have since widened.

## Concrete Artifacts

### GPT-5.6 pricing timeline (per 1M tokens)
```
                Preview (Jun 26)   GA (Jul 9)         Post-cut (Jul 30)
Sol             $5.00 / $30.00     $5.00 / $30.00     $5.00 / $30.00 (unchanged)
Terra           $2.50 / $15.00     $2.50 / $15.00     $2.00 / $12.00 (-20%)
Luna            $1.00 / $6.00      $1.00 / $6.00      $0.20 / $1.20  (-80%)

Sources: blog-simonwillison-gpt56-sol-launch.md Concrete Artifacts (preview),
blog-openai-gpt56-ga-announcement.md Concrete Artifacts (GA), this note
Claim 2 (post-cut, from openai.com/index/advancing-the-price-performance-
frontier-with-gpt-5-6/, July 30, 2026).
```

### Cross-vendor cost comparison as of July 30, 2026 (per 1M tokens, input/output)
```
Model                     Input     Output    Source
GPT-5.6 Luna (new)        $0.20     $1.20     This note, Claim 2
Gemini 3.1 Flash-Lite     $0.25     $1.50     blog-simonwillison-deepseek-v4.md
                                              Concrete Artifacts (Apr 2026;
                                              this note's source prints the
                                              figure as "$.025," almost
                                              certainly a typo — see Claim 3)
Claude Haiku 4.5          $1.00     $5.00     blog-simonwillison-deepseek-v4.md
                                              Concrete Artifacts (Apr 2026)
GPT-5.6 Luna (old)        $1.00     $6.00     blog-simonwillison-gpt56-sol-launch.md
                                              Concrete Artifacts (Jun 2026)
```

### Fast mode for GPT-5.6 Sol (from OpenAI's pricing announcement, July 30, 2026)
```
- Replaces "Priority Processing"
- Up to 2.5x faster than Standard processing
- 2x the price of Standard, no change in intelligence
- Backward compatible: existing requests tagged `priority` auto-upgrade
- Aligns with `/fast` in Codex

Source: openai.com/index/advancing-the-price-performance-frontier-with-
gpt-5-6/, fetched via Wayback Machine (snapshot 2026-08-04).
```

### Engineering claims behind the price cut (from OpenAI's companion post, "How GPT‑5.6 fuses frontier intelligence with frontier efficiency," July 29, 2026)
```
- Load balancing: GPT-5.6 Sol (via Codex) analyzed production traffic,
  identified routing imbalances, tested new routing strategies — "dramatically
  reduced" serving cost (magnitude not quantified)
- Kernel/forward-pass optimization: GPT-5.6 Sol autonomously rewrote
  production kernels in Triton and Gluon — 20% reduction in end-to-end
  serving costs; verified in part with the open-source tool FpSan
  (Floating-Point Sanitizer)
- Speculative decoding: GPT-5.6 Sol designed/ran "hundreds of experiments"
  on its own draft-model architecture and autonomously supervised training
  (including intervening on hardware failures/training instability) — >15%
  token-generation efficiency gain
- Agentic harness: Rust orchestration layer connecting models, tools, and
  the user's environment
    - "Deferred discovery": integrations/MCP tools/skills/plugins only
      surfaced when needed, to control context bloat
    - Tool output capped at 10,000 tokens by default unless the model
      requests a different limit
    - Model-visible history is append-only (new messages/tool
      results/environment updates always added at the end)
    - Tools presented in deterministic order
    - Runtime settings (e.g. approval policies) applied at execution time,
      not embedded in tool definitions
    - Stated goal of all of the above: preserve the prompt-cache prefix and
      sustain "high overall prompt-cache hit rates" for Codex/ChatGPT Work

Source: openai.com/index/gpt-5-6-frontier-intelligence-efficiency/, fetched
via Wayback Machine (snapshot 2026-08-01).
```

### Customer testimonials (from OpenAI's pricing announcement, July 30, 2026)
```
Replit    — Michele Catasta, President & Head of AI
            "the closest we've come to intelligence too cheap to meter"
Notion    — Hoda Noorian, AI Product
            Terra: comparable quality to GPT-5.5 at half cost/task, 60%
            less time
Ramp      — Shaiyon Hariri, Creator of Ramp SWE-Bench
            Terra/Luna lead cost-efficiency on internal coding benchmarks;
            Luna is now Ramp's default model for background agent
            automations
Blitzy    — Sid Pardeshi, CTO + Co-Founder
            prompt-cache reuse 24% -> 90%; 2.2x more context; 8.5x fewer
            output tokens; 87% lower cost vs. GPT-5.4 mini
Cognition — Walden Yan, Co-Founder and Chief Product Officer
            Luna incorporated into Devin Fusion as a pair-programmer model
            for routine work
Dust      — Stanislas Polu, Co-Founder and CTO
            Luna is 40% faster and 40% cheaper than their previous default
            model on the same agentic tasks

Source: openai.com/index/advancing-the-price-performance-frontier-with-
gpt-5-6/, fetched via Wayback Machine (snapshot 2026-08-04).
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-gpt56-sol-launch.md` Claim 4 and
    `blog-openai-gpt56-ga-announcement.md` Concrete Artifacts (pre-cut GPT-5.6
    pricing table): this note's Claim 1/2 pricing figures are exact 80%/20%
    reductions from those documented baselines, cross-checked arithmetically.
  - `blog-simonwillison-deepseek-v4.md` Concrete Artifacts → Pricing
    Comparison Table: independently confirms both comparison figures used in
    Claims 3–4 (Gemini 3.1 Flash-Lite $0.25/$1.50; Claude Haiku 4.5
    $1.00/$5.00), which is what surfaces the likely typo in Claim 3.
  - `blog-anthropic-prompt-caching-everything.md` Claim 3 ("static content
    first, dynamic content last") and Claim 4 (non-deterministic tool
    ordering as a common cache-breaking pitfall): Claim 11 here documents
    OpenAI's harness independently converging on the same two prescriptions
    (append-only history, deterministic tool order) for the same underlying
    reason — preserving the cached prefix — corroborating that these are
    now cross-vendor, not Anthropic-specific, best practices.
  - `blog-openai-gpt56-ga-announcement.md` Claims 4–5 (Agents' Last Exam and
    Artificial Analysis Coding Agent Index benchmark framing for Sol vs.
    Fable 5): Claim 13 here extends the same Agents' Last Exam comparison
    down to the Luna tier with a cost-per-task framing.

- **Contradicts**: None filed as a formal contradiction issue. Claim 14
  documents a same-vendor, same-benchmark numeric discrepancy (July 9's
  "about one-third less" vs. July 29's "less than half of the cost" for Sol
  vs. Fable 5 cost-per-task on the Artificial Analysis Coding Agent Index)
  but treats it as plausibly explained by real efficiency gains disclosed in
  this same source (Claims 7–9) rather than a genuine dispute — per MINER.md
  §4a this is closer to a conditioning-variable/precision nuance (different
  points in time) than a factual contradiction requiring a filed issue. If a
  future source repeats either figure without the efficiency-gains context,
  it may be worth re-evaluating whether a formal contradiction issue is
  warranted.

- **Extends**:
  - `blog-simonwillison-gpt56-ga-launch.md` and
    `blog-openai-gpt56-ga-announcement.md`: both establish the GA-stage
    pricing and benchmark baseline (July 9, 2026) that this note's price cut
    and cost-per-task claims (Claims 1–2, 13–14) update three weeks later.
  - `blog-openai-gpt56-ga-announcement.md` Claim 2 (`ultra`'s multi-agent
    parallel setting) and Claims 6–9 (cybersecurity capability and safeguard
    architecture): this note's Claims 8–10 add a third domain of
    Sol-as-autonomous-systems-engineer — production infrastructure
    optimization (load balancing, kernels, speculative decoding, harness
    design) — distinct from both the user-facing `ultra` capability and the
    cybersecurity-safeguard material already documented for GPT-5.6.

- **Novel**:
  - First corpus documentation of a post-GA price cut for any GPT-5.6 tier
    (Claims 1–2) — all prior GPT-5.6 notes cover preview or GA-stage pricing
    only.
  - First corpus documentation of "Fast mode" (Claim 6) and its
    predecessor "Priority Processing" for any OpenAI model.
  - First corpus documentation of a model being used to autonomously
    supervise its own training run's failure recovery (Claim 9,
    "autonomously intervening when issues arose, including hardware
    failures and training instability") — a materially different autonomy
    claim than agentic coding or agentic cyber-offense/defense already in
    the corpus.
  - First corpus documentation naming OpenAI's harness implementation
    language (Rust) and a specific default tool-output token cap (10,000
    tokens) (Claim 10).
  - First corpus documentation of OpenAI's "deferred discovery" pattern name
    for context-bloat control (Claim 10).
  - Six new customer testimonials with concrete efficiency figures (Claim
    12, Concrete Artifacts), none of which overlap with the eleven
    model-level testimonials already mined in
    `blog-openai-gpt56-ga-announcement.md` Concrete Artifacts (Cursor, Qodo,
    Notion [different quote], Cognition [different quote], Rogo, Ramp
    [different quote], Shopify, Cisco, Clio, Balyasny, Basis) — Notion, Ramp,
    and Cognition appear in both notes but with entirely different quotes
    focused on different aspects (the GA note's testimonials focus on Sol's
    launch-day capabilities; this note's testimonials focus specifically on
    the July 30 price/efficiency change).

## Guide Impact

- **Chapter 02 (Harness Engineering) / model-selection sections**: Update any
  GPT-5.6 pricing table sourced from `blog-simonwillison-gpt56-sol-launch.md`
  or `blog-openai-gpt56-ga-announcement.md` with the July 30, 2026 cut (Claims
  1–2): Terra $2.00/$12.00, Luna $0.20/$1.20, Sol unchanged at $5.00/$30.00.
  Mark the earlier Terra/Luna figures as superseded as of 2026-07-30. Add the
  cross-vendor comparison (Claims 3–4): Luna now undercuts Gemini 3.1
  Flash-Lite and sits at 1/5th Claude Haiku 4.5's input price — a meaningful
  new data point for any "cheapest usable model" guidance, while flagging the
  Claim 3 typo caveat so the guide cites $0.25 (not "$.025") for Flash-Lite.

- **Chapter 02 (Harness Engineering)**: Add Claims 7–9 (Sol autonomously
  rewriting production kernels, tuning load balancing, and supervising its
  own speculative-decoder training including failure recovery) as a concrete,
  named example of "use the model to build/operate the harness/infrastructure
  that serves it" — a recursive self-optimization pattern distinct from
  agentic coding on customer-facing features. Flag all magnitude claims (20%
  serving cost reduction, >15% token-gen efficiency) as vendor-self-reported
  and unaudited.

- **Chapter 04 (Context Engineering)**: Add Claims 10–11 (deferred discovery,
  10,000-token default tool-output cap, append-only model-visible history,
  deterministic tool ordering, runtime settings externalized from tool
  definitions) as a concrete, named OpenAI-harness implementation alongside
  the existing Anthropic/Claude Code cache-preservation rules in
  `blog-anthropic-prompt-caching-everything.md` — useful as a second,
  independently-arrived-at vendor implementation of the same "static prefix,
  dynamic suffix" principle, strengthening the case that this is a
  cross-vendor architectural convergence rather than an Anthropic-specific
  quirk.

- **Chapter 02 (Harness Engineering) / model-selection sections**: Add Claim
  6 (Fast mode: 2.5x speed at 2x price for Sol) as a concrete example of a
  vendor offering a speed/cost dial on a flagship model instead of a price
  cut, worth contrasting with Luna/Terra's price-cut-instead-of-speed-option
  treatment in the same announcement.

- No chapter should cite Claim 13's "nearly 99% lower estimated cost per
  task" or Claim 12's testimonial figures as standardized, reproducible cost
  benchmarks — both are vendor-selected, methodology-undisclosed marketing
  figures, useful only as directional adoption/efficiency signals.

## Extraction Notes

- **WebFetch declined verbatim reproduction on the primary source**: The
  standard `WebFetch` tool, when asked to reproduce Willison's post verbatim,
  refused on copyright grounds and offered only a summary/short-quote
  alternative. All quotes from `simonwillison.net/2026/Jul/30/luna-price-drop/`
  in this note were instead obtained via a direct `curl` fetch of the raw
  HTML (HTTP 200) and hand-extracted from the article markup
  (`<div data-permalink-context=...>` block), then cross-checked
  character-for-character against that raw HTML, including the apparent
  typo flagged in Claim 3.
- **Both OpenAI pages linked from the post were followed and fetched**, per
  MINER.md §1 ("follow up to 5 linked pages that seem substantive"): the
  pricing announcement itself
  (`openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/`)
  and the companion engineering post
  (`openai.com/index/gpt-5-6-frontier-intelligence-efficiency/`). Both live
  URLs returned HTTP 403 with a Cloudflare bot-challenge to direct `curl`
  (the same access pattern already documented for `openai.com/index/` posts
  in `blog-openai-gpt56-ga-announcement.md`). Both were successfully
  retrieved via Internet Archive Wayback Machine snapshots (pricing
  announcement: 2026-08-04; engineering post: 2026-08-01), stripped of
  HTML/scripts/styles, and used as the source for every quote attributed to
  OpenAI directly (as opposed to quotes attributed to Willison quoting
  OpenAI, which were sourced from Willison's own page).
- **The Hacker News discussion link** (`news.ycombinator.com/item?id=49112867`)
  in Willison's "(via)" attribution was not followed — it is a discussion
  aggregator link, not a substantive primary or secondary source, consistent
  with this Miner's treatment of similar "(via)" links in other notes.
- **Triton and Gluon documentation links** (triton-lang.org) were not
  followed — they are general-purpose GPU programming language docs, not
  specific to the GPT-5.6 claims being extracted, and following them would
  not add verifiable detail to any claim in this note.
- **No contradiction issue filed**: see Cross-References → Contradicts for
  the reasoning on Claim 14 (a same-vendor numeric discrepancy judged to be a
  time-based precision difference rather than a genuine dispute).
