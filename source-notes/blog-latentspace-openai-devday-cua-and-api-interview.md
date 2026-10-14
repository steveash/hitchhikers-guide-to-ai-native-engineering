---
source_url: https://www.latent.space/p/devday-2026
source_type: blog-post
title: "Why Dwarkesh is Wrong about Computer Use + How OpenAI shipped its Jev competitor in 1 Week"
author: Latent Space (swyx, Vibhu) interviewing Ari Weinstein (OpenAI, Computer Use) and Nikunj Handa (OpenAI, API product)
date_published: 2026-09-30
date_extracted: 2026-10-14
last_checked: 2026-10-14
status: current
confidence_overall: anecdotal
issue: "#4110"
---

# Why Dwarkesh is Wrong about Computer Use + How OpenAI shipped its Jev competitor in 1 Week

> Same-day DevDay interview with two OpenAI product leads: the Computer Use (CUA) harness is now multimodal and code-writing (JavaScript, Playwright, accessibility tree, DOM), and the API side adds async tool calling, mid-turn steering, 12-hour cache guarantees, pre-warming, server-side compaction and a Luna-based Decisions API; every claim is first-party and unverified.

## Source Context

- **Type**: blog-post (podcast show notes plus full transcript, ~39 minutes; recorded right after the DevDay keynote)
- **Author credibility**: Hosts are Latent Space (swyx, Vibhu), who are well-connected AI-engineering commentators. Guests are OpenAI staff: Ari Weinstein (product and engineering lead for Computer Use, previously Apple Shortcuts and cofounder of Sky) and Nikunj Handa (product lead for the API, ex-Stripe). They speak from direct knowledge but also as vendor marketing on launch day.
- **Scope**: CUA internals (modalities, speed, self-debugging, testing loop), Agents API safety advice, and the API platform (async tools, steering, WebSockets, UltraFast, Decisions API, caching, compaction, higher-level primitives). It gives no benchmarks, code or configs. The "Dwarkesh is wrong" headline is the hosts' framing; the Dwarkesh position is only summarised via an embedded tweet.

## Extracted Claims

### Claim 1: Computer use became much more capable in a year mainly because agents now debug and retry instead of failing after a reliable start
- **Evidence**: First-hand observation by the CUA lead, comparing today with his earlier company Sky. No metrics.
- **Confidence**: anecdotal
- **Quote**: "before they could, like, reliably start tasks, but then they would run into problems, and now they’re really good at debugging. They’re really good at trying again, introspecting what is and isn’t working."
- **Our assessment**: Plausible and consistent with the verification-loop theme of Ch03, but unmeasured. The rebuttal to the Dwarkesh framing is assertion plus product anecdotes, not data.

### Claim 2: The CUA harness mixes screenshots, accessibility, Playwright and model-written JavaScript, chosen per task, so one tool call can do many actions
- **Evidence**: Description of what is visible when expanding Codex tool calls.
- **Confidence**: anecdotal
- **Quote**: "It’s actually writing JavaScript code that it executes, that the computer executes to perform sometimes many actions at once, which is a great, you know, speed up and great capability."
- **Our assessment**: Strong, concrete architectural signal: action batching via code rather than one click per turn. Not independently verifiable, but it matches the other direction of travel (code-as-action). Contrast with Anthropic’s guidance that batching helps only for independent actions (see Cross-References).

### Claim 3: Direct DOM / accessibility access removes the screenshot-scroll-screenshot loop because the model can see a whole page or app
- **Evidence**: Weinstein names this the biggest "aha moment"; a lot of the speed gain also comes from many small fixes.
- **Confidence**: anecdotal
- **Quote**: "now the language model can actually see, like, an entire page or an entire application. It can write code that can do multiple steps at once."
- **Our assessment**: Credible mechanism (fewer round trips, richer context). The "paper cuts" remark is a useful reminder that latency work is cumulative engineering, not one trick.

### Claim 4: App Shots give the model the accessibility representation (links, untruncated text), not just pixels, and are engineered to be token-efficient
- **Evidence**: Describes inspecting the raw attachment in Codex/ChatGPT; screenshots lose link targets and truncate calendar titles.
- **Confidence**: anecdotal
- **Quote**: "The screenshot doesn’t include where the link goes."
- **Our assessment**: Useful Ch04 point: structured UI state beats images for context quality per token. The token-efficiency "art" is not described, so nothing to copy beyond the principle.

### Claim 5: As agents get faster, remaining time is dominated by waiting on the target app, so triggering the next LLM step should be event-driven where possible
- **Evidence**: Weinstein says a non-trivial share of benchmark time is waiting for pages like doordash.com to load; some waits (e.g. customer-service replies) cannot be event-driven.
- **Confidence**: anecdotal
- **Quote**: "When possible, you want it to be event-driven."
- **Our assessment**: Practical and generalisable harness advice (use load events rather than fixed waits or polling). Pairs with the async tool-calling claim below.

### Claim 6: Use the model-vendor’s in-distribution computer-use harness rather than building your own, for speed, cost and accuracy
- **Evidence**: Authority only; the claim is hedged ("might").
- **Confidence**: anecdotal
- **Quote**: "we train our models on our Computer Use harness, so there is, an advantage to using the one that’s in distribution for the model."
- **Our assessment**: Vendor interest is obvious, but the model/harness co-training point is real and relevant to the guide’s harness-portability discussion. Treat as a trade-off, not a rule: it cuts against harness-agnostic advice.

### Claim 7: Safety advice for computer-use apps: consent before consequential actions, safety checks, and limit access to needed sites/apps
- **Evidence**: Stated recommendations; the host separately says they let it pay "tens of thousands of dollars" of bills unsupervised, which contrasts with the advice.
- **Confidence**: anecdotal
- **Quote**: "by asking for the user’s consent before doing something consequential like making a payment"
- **Our assessment**: Standard least-privilege guidance; thin on mechanism. The host’s admitted "yoloing" is a good illustration of the gap between advice and practice.

### Claim 8: Computer use closes the build-then-test loop so the agent, not the human, is QA
- **Evidence**: Weinstein’s own workflow; swyx adds a "visual play test skill" that catches design issues not visible in code.
- **Confidence**: anecdotal
- **Quote**: "Computer Use letting the agent- actually test the software that the agent has built, which is far more consequential than it sounds."
- **Our assessment**: Directly relevant to Ch03 (verification). No failure rates given, so evidence is testimony only.

### Claim 9: Async function calling and mid-turn steering let the model keep reasoning while tools run and accept injected messages mid-turn, and rely on post-training plus WebSockets
- **Evidence**: Handa describes the GPT-6 API features; swyx notes the model must be trained for it; WebSockets first shipped for GPT-5.3 Codex Spark.
- **Confidence**: anecdotal
- **Quote**: "you don’t have to, like, pause the model’s execution while, the tool is running."
- **Our assessment**: A genuine harness-shape change: the sequential tool-call loop gives way to a bidirectional stream. No code or API schema shown, so harness authors cannot yet apply it beyond awareness.

### Claim 10: OpenAI’s stated API policy is to expose a capability only once it is trained into the harness and good enough
- **Evidence**: Handa’s description of API strategy.
- **Confidence**: anecdotal
- **Quote**: "put things in the API once it’s trained into the harness."
- **Our assessment**: Explains why model-side features (steering, async) arrive late relative to app-side versions. Useful framing for model-harness co-evolution.

### Claim 11: The Decisions API is the same Luna weights with constrained output, parallel batching of questions and a latency-tuned stack, built in about a week after Jev; it is no reasoning, faster and weaker at long-horizon tasks
- **Evidence**: Handa and Weinstein explain it directly; prototype to near-launch in roughly one week; hill-climbing on latency.
- **Confidence**: anecdotal
- **Quote**: "We’re, like, building this purely on top of the same Luna weights that we have."
- **Our assessment**: Notable that the "decision model" category is, at first release, a serving-layer feature, not a new model; calibration is acknowledged as open. Supports the guide treating this as a routing/classification primitive, not a reasoner.

### Claim 12: Decision models suit fast classification and the "talker" front-end of a talker/thinker split (GPT Live), with internal use for support-ticket classification
- **Evidence**: Internal prototypes of GPT Live controlling a computer via Decisions; user-ops classifying tickets. Anecdotal; no numbers.
- **Confidence**: anecdotal
- **Quote**: "We gotta classify all of our support tickets."
- **Our assessment**: Corroborates the delegation architecture in the DevDay live blog. Handa also concedes the model will not match a stronger model writing a script, so it is a complement to, not a replacement for, large-model computer use.

### Claim 13: Caching: 30-minute hit guarantees, a preview 12-hour guarantee for an extra cache-write fee, explicit pre-warming, and a cache diagnostics tool
- **Evidence**: Product details stated by Handa; 12-hour window is "in preview", not public.
- **Confidence**: anecdotal
- **Quote**: "So we have, like, a 12-hour caching guarantee, that we offer so that you have, like, guaranteed cache hits"
- **Our assessment**: Concrete, actionable Ch04 detail for long-lived single-thread personal agents; pre-warming lets you pay the cache write ahead of time and fan out many instances. Pricing numbers are not given (only "25% cheaper" cache reads, said by the host), so verify against docs.

### Claim 14: Two compaction modes in Responses API (server-side threshold-triggered, and manual /compact), with big coding agents preferring manual; Agents API bundles compaction in the harness; file-based techniques are being tried
- **Evidence**: Handa references the open-source Codex harness using /compact and says new techniques are already in Codex.
- **Confidence**: anecdotal
- **Quote**: "a lot of the big coding agents like to do it manually."
- **Our assessment**: Gives the guide a vendor-confirmed taxonomy (automatic threshold vs. explicit control) and a hint that harness authors with domain knowledge prefer explicit control. Inspectable in the open-source Codex repo, which is the real evidence to follow up.

### Claim 15: Where to draw the boundary between platform API and developer harness is an open question; OpenAI wants feedback
- **Evidence**: Handa’s Stripe analogy for higher-level primitives; the Assistants API is described as not the right fit.
- **Confidence**: anecdotal
- **Quote**: "how much of that do we build into the API is like a constant question that I’m thinking about."
- **Our assessment**: Honest signal that the Agents API/own-harness boundary is unsettled. The guide should not present either side as settled.

## Concrete Artifacts

No code, configs or transcripts of agent sessions. Concrete product facts as stated by guests (all first-party, unverified):

```
Source: Latent Space transcript, Handa (00:32:35-00:34:55), Weinstein (00:00:24)
- Cache hit guarantee: ~30 minutes (GA); 12-hour guarantee in preview (extra cache-write fee)
- Pre-warming: pay cache write up front; ready for ~30 minutes; can fan out many instances
- Compaction: server-side (token threshold) or /compact (manual); Agents API bundles it
- GPT-6.1 Sol: "a fifth of the cost of Astra", "a seventh" for Computer Use (Weinstein)
- Decisions API: Luna weights, no reasoning, parallel batched questions, limited preview
- Example: meal-prep order took 2 hours by hand, 15 minutes by Computer Use (Weinstein)
```

## Cross-References

- **Corroborates:**
  - `blog-simonwillison-openai-devday-2026-live-blog` Claim 7 (Decisions API constrains a small model to a predefined option set) and Claim 13 (delegating from a low-latency voice agent to a stronger background model), here with the "talker" GPT Live detail. Also Claim 8 (OpenAI used its own models to optimize the Computer Use harness): compare Weinstein’s "paper cuts" remark.
  - `blog-anthropic-computer-use-best-practices` Claim 10 (server-side compaction available for long computer-use sessions): the same two-mode idea appears at OpenAI.
  - `blog-latentspace-ainews-six-jev-clones` Claim 7 and Claim 8: decision models as routing/classification primitives with browser/computer-use integrations.
- **Contradicts:** None filed. Tension, not a contradiction: `blog-anthropic-computer-use-best-practices` Claim 6 says batching tools compounds errors when actions are sequentially dependent, while Weinstein presents model-written multi-action JavaScript as a major speed win; these differ in context (declarative batch tools vs. code that can branch), so recorded as a conditioning variable.
- **Extends:**
  - `blog-latentspace-jev-system-one-for-prod` Claim 1, Claim 9 and Claim 13: the incumbent’s view of System One models, now with a lab’s clone and its stated limits (no new weights, calibration open).
  - `blog-latentspace-khemani-unpacking-chatgpt-work` (ChatGPT Work harness and cloud computer): adds CUA modality details and Dots’ per-agent Linux computer.
- **Novel:** Async tool calling and mid-turn steering as API features; 12-hour cache guarantee and pre-warming; the explicit "in-distribution harness" argument; event-driven triggering of LLM steps for computer use; the build-then-test loop closed by computer use as stated by the CUA lead.

## Guide Impact

- **Chapter 02**: Add a short note that vendors are moving from a sequential tool-call loop to bidirectional (WebSocket) loops with async tool results and mid-turn steering, citing Claim 9; flag as vendor-only, anecdotal. Also note the in-distribution harness trade-off (Claim 6) alongside harness portability advice.
- **Chapter 04**: Add long-lived cache windows and pre-warming (Claim 13) and the server-side vs. manual compaction split (Claim 14) as vendor-confirmed options; prefer UI structure (accessibility/DOM) over screenshots for context (Claims 3-4). Do not quote prices.
- **Chapter 03**: Cite Claim 8 as testimony that computer-use agents can serve as the QA step in a build-test loop; do not state effectiveness figures since none are given.

## Extraction Notes

- Read the full transcript on the page (all ~39 minutes, both guests). No sub-pages followed; the embedded tweets were skimmed for context only (Dwarkesh’s framing question, DevDay Decisions API announcement).
- Quotes are copied from the transcript; speaker-turn filler words were kept inside quoted fragments, so quotes look rough. Fragments are single contiguous passages.
- The "Dwarkesh is wrong" headline cannot be assessed: the transcript contains no data on the actual claim, and Weinstein only says "I hope they have a different perspective now".
- All performance and cost claims ("a fifth of the cost of Astra", "faster than the average human") are vendor statements and unverified. Model names (Sol, Astra, Luna) are as used by the speakers.
