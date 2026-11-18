---
source_url: https://simonwillison.net/2026/Nov/17/gpt62-astra-and-sol/
source_type: blog-post
title: "GPT‑6.2 Astra and GPT‑6.2 Sol"
author: Simon Willison
date_published: 2026-11-17
date_extracted: 2026-11-18
last_checked: 2026-11-18
status: current
confidence_overall: anecdotal
issue: "#4788"
---

# GPT‑6.2 Astra and GPT‑6.2 Sol

> Willison's link post on OpenAI's GPT‑6.2 release: Astra drops to $8/$40 (matching Claude Fable 5.2) with a cached-input price of $0.40/M, Sol stays at $2/$10, and one secondhand practitioner anecdote (Theo Browne) of a long-running `/goal` session stalling on an irrelevant internal-detail question.

## Source Context

- **Type**: blog-post (link blog entry, 17 Nov 2026). Quotes OpenAI's announcement sentence, then adds pricing commentary, pelican outputs, one hands-on Codex test, and a "mixed reception" paragraph.
- **Author credibility**: Simon Willison is a long-running LLM tooling practitioner (co-creator of Django, creator of the `llm` CLI) and a heavily used feed in this corpus. Pricing here is vendor list pricing relayed by him; benchmark statements are not his own measurements.
- **Scope**: Prices for 6.2 Astra/Sol, a single informal "Yonkers mech" prompt test at Codex "Ultra" effort, and reception. Does not cover benchmark numbers, context limits, or caching mechanics. The Browne complaint is quoted secondhand from a pre-release feedback letter.

## Extracted Claims

### Claim 1: GPT‑6.2 Astra is priced at $8/MTok input and $40/MTok output, 80% of GPT‑6 Astra and equal to Claude Fable 5.2
- **Evidence**: Willison's statement of list prices; compares to 6 Astra and Fable 5 at $10/$50.
- **Confidence**: settled (published vendor pricing, as reported)
- **Quote**: "6.2 Astra is 80% of the price of 6 Astra - $8/MTok input and $40/MTok output, the same price as Claude Fable 5.2 (which was also 80% of its predecessor)."
- **Our assessment**: Continues cross-vendor flagship price parity first noted at Astra's launch ($10/$50 = Fable 5/5.1). Both vendors made the same 20% cut in the same generation step, which suggests tracking each other rather than independent pricing.

### Claim 2: Astra 6.2's cached-input price fell from $1/M to $0.40/M, a bigger discount than the list-price cut
- **Evidence**: Price comparison by Willison; the percentages are derivable (-60% cached vs -20% list).
- **Confidence**: settled (price) / anecdotal (the "great news" effect, unmeasured)
- **Quote**: "The cached price is an even bigger discount - $0.40/million compared to $1/million for the older model. This is great news for longer running agentic sessions."
- **Our assessment**: Consistent with the thesis that cache-read price dominates agent cost (`blog-simonwillison-opus55-gpt6-sol-luna-price-war.md` Claim 7). Cached price is 5% of list input here (0.40/8), versus the 10% convention in GPT‑5.6.

### Claim 3: GPT‑6.2 Sol stays at $2/$10, unchanged from 6.1 Sol and 6 Sol, and is half the price of GPT‑5.6 Sol, which the post gives as $4/$20
- **Evidence**: Willison's statement; no table in this post.
- **Confidence**: emerging
- **Quote**: "GPT-6.2 Sol is the same $2/$10 price as 6.1 Sol and 6 Sol - which are half the price of GPT-5.6 Sol ($4/$20)."
- **Our assessment**: Third Willison appearance of $4/$20 for 5.6 Sol (here in prose, not just a caption or table), which weighs on contradiction #3331. Earlier corpus notes record $5/$30; the price-war note's Claim 2 attributes the lower figure to promotional pricing ahead of a scheduled November increase. This post does not mention promotion, and it is dated after that increase was due, so the post's "$4/$20" may be a stale baseline. Unresolved; do not pick a verdict here.

### Claim 4: Sol and Astra "Ultra" outputs on a Three.js "Yonkers mech" prompt were not good enough versus Claude Fable 5.2 and Gemini 4 Carbon
- **Evidence**: One prompt, one run each, in Codex CLI at "Ultra" effort; outputs linked, judged by eye.
- **Confidence**: anecdotal
- **Quote**: "Neither of them did a good enough job of morphing Yonkers into a big mech, at least in comparison to Claude Fable 5.2 and Gemini 4 Carbon."
- **Our assessment**: n=1, subjective, and the comparison models' outputs are not shown here. Do not use as a capability ranking.

### Claim 5: Reception is mixed; Astra 6.2 scores a little below Fable 5.2 on various benchmarks and some find its communication confusing
- **Evidence**: Willison's summary of what he's seen; no numbers or links given in the post.
- **Confidence**: anecdotal
- **Quote**: "Astra 6.2 isn't scoring quite as high as Fable 5.2 on various benchmarks, and I've seen a few complaints that its communication style can be confusing."
- **Our assessment**: Unsourced aggregate impression. Useful only as a flag; the same shape as Astra 6's launch (trailing Fable on Artificial Analysis, per `blog-simonwillison-gpt6-astra-launch.md` Claim 4) despite being cheaper per token.

### Claim 6: On long tasks Astra 6.2 manages many subagents well, then halts to ask the user an internal implementation question the user cannot meaningfully answer
- **Evidence**: Theo Browne's pre-release feedback letter to OpenAI, quoted by Willison: a `/goal make a new level for Outer Wilds` run was "blocked" two hours in over a clip-file naming question.
- **Confidence**: anecdotal
- **Quote**: "When this model is working on long tasks, it can pull in a lot of subagents and manage them pretty well."
- **Our assessment**: Single secondhand anecdote from a pre-release build, not a failure rate. Its value is as a named harness failure mode: an autonomous run that escalates low-level decisions upward and blocks, wasting the unattended time budget. Mitigations (defaults for internal naming decisions, a "decide and record" instruction, deferring questions to an end-of-run list) are our inference, not from the source.

### Claim 7: The concrete stall example: the agent asked which of two filenames a reviewer subtask writes clips to
- **Evidence**: Browne's quoted example.
- **Confidence**: anecdotal
- **Quote**: "I sent "/goal make a new level for Outer Wilds". 2 hours in, it's "blocked" because it wanted to ask me "does r24's reviewer write it's clips to 24_g521.mp4 or 24_p11.mp4?""
- **Our assessment**: Illustrates that subagent fan-out creates internal state (file names keyed to subagent IDs like "r24") that the parent then cannot reconcile and surfaces to the human. This points at orchestration bookkeeping, not user-facing ambiguity.

## Concrete Artifacts

```
Pricing per MTok as stated in the post (Willison, 2026-11-17)
GPT-6.2 Astra : $8 input / $40 output ; cached input $0.40
GPT-6 Astra   : $10 / $50 ; cached $1
Claude Fable 5.2 : $8 / $40 (stated same as 6.2 Astra)
GPT-6.2 Sol   : $2 / $10  (same as 6.1 Sol and 6 Sol)
GPT-5.6 Sol   : $4 / $20  (as stated in the post; see #3331)
API ids: gpt-6.2-astra, gpt-6.2-sol ; LLM 0.38 adds support
```

```
Browne's /goal anecdote (quoted in the post):
/goal make a new level for Outer Wilds
... 2 hours in -> status "blocked"
question: "does r24's reviewer write it's clips to 24_g521.mp4 or 24_p11.mp4?"
```

```
Willison's test prompt (Codex CLI/desktop, "Ultra" effort):
Make a three js animation where yonkers stands up as a big mech (cool stand up motion) and stomps around manhattan and queens and Brooklyn, use openstreetmap mapping data
```

## Cross-References

- **Corroborates**: `blog-simonwillison-opus55-gpt6-sol-luna-price-war.md` Claim 1 (GPT-6 Sol at half of GPT-5.6 Sol, table $4/$20) and Claim 7 (cache pricing matters for agentic sessions). `blog-simonwillison-gpt6-astra-launch.md` Claim 3 ($10/$50 baseline for Astra and Fable 5).
- **Contradicts**: Existing contradiction #3331 (GPT-5.6 Sol $5/$30 vs $4/$20) is directly relevant. This post repeats $4/$20 without a stated promotional caveat; see `blog-simonwillison-opus55-gpt6-sol-luna-price-war.md` Claim 2 for the promotional-pricing explanation. No new contradiction filed; evidence added to the existing one.
- **Extends**: `blog-simonwillison-gpt6-astra-launch.md` (6.2 follow-up on price and reception); `blog-simonwillison-astra-pelican-comparison-grid.md` (pelican/effort-sweep method continued).
- **Novel**: GPT-6.2 prices and $0.40 cached rate; Fable 5.2 priced at $8/$40; the Astra 6.2 subagent-then-"blocked" long-run stall anecdote.

## Guide Impact

- **Ch01 (model choice/cost)**: Update any price table to list Astra 6.2 at $8/$40 (cached $0.40) and Sol 6.2 at $2/$10 with an "as of 2026-11-17" label; flag the GPT-5.6 Sol baseline as unresolved pending #3331.
- **Ch02 (harness engineering)**: Add the "agent blocks on an internal detail question mid-`/goal` run" failure mode as a single-practitioner anecdote, with the design implication that long unattended runs need a policy for non-user-facing decisions. Do not present it as a measured rate.

## Extraction Notes

- Read the full post on simonwillison.net; linked pelican grids, videos and transcript not followed (not substantive for the guide). Browne's original letter was not available, so the quote is as reproduced by Willison.
- Post is thin on first-person evidence; most claims are relayed vendor pricing and secondhand reception.
