---
source_url: https://openai.com/index/continuous-voice-interaction-with-gpt-live
source_type: blog-post
title: "How we built a realtime system for responsive voice AI in six months"
author: Justin Uberti and Zahan Malkani (OpenAI, Members of Technical Staff)
date_published: 2026-08-03
date_extracted: 2026-08-12
last_checked: 2026-08-12
status: current
confidence_overall: emerging
issue: "#2641"
---

# How we built a realtime system for responsive voice AI in six months

> OpenAI's first-party engineering deep-dive on GPT‑Live's production
> architecture: a full-duplex voice model that removes the "turn detector"
> entirely, a seamless model-instance handoff mechanism that also powers
> zero-interruption context compaction, a pre-warmed/pinned delegation path
> to frontier models, and two new open WebRTC protocol extensions (WARP,
> Instant Connect) that cut connection setup from six round trips to one —
> published five days after this same claim ("WebRTC lets us make real-time
> AI products") was directly disputed by an OpenAI-affiliated WebRTC expert
> already in this corpus, and reaffirming (not abandoning) WebRTC across two
> consecutive voice-system generations.

## Source Context

- **Type**: blog-post (OpenAI's official "Engineering" blog, `openai.com/index/`,
  published August 3, 2026; a long-form, ~2,300-word technical deep-dive with
  one architecture diagram/caption). Per MINER.md §1, two linked sub-pages were
  followed in full: OpenAI's July 8, 2026 product announcement
  ("Introducing GPT‑Live," `openai.com/index/introducing-gpt-live/`) and
  OpenAI's May 4, 2026 predecessor engineering post ("How OpenAI delivers
  low-latency voice AI at scale," `openai.com/index/delivering-low-latency-voice-ai-at-scale/`),
  which this post explicitly cites as "an important foundation" it built on.
  Both are attributed by page and byline throughout this note. A third set of
  links — the WARP/SPED/SNAP IETF drafts and the DTLS 1.3/DCEP RFCs — were
  identified but not fetched as separate sources; they are primary protocol
  specifications rather than explanatory prose, and the blog post's own text
  already states the mechanism-level claims this note extracts from them (see
  Extraction Notes).
- **Author credibility**: Justin Uberti and Zahan Malkani are named as OpenAI
  Members of Technical Staff. Uberti is independently identified, in the
  linked May 2026 predecessor post (by different OpenAI authors, Yi Zhang and
  William McDonald), as "one of WebRTC's original architects" who is "now
  a colleague here at OpenAI" — i.e., this post's co-author has personal
  authorship history on the WebRTC standard itself. Uberti is also the named
  author of the WARP IETF draft this post describes (`draft-uberti-tsvwg-warp`,
  confirmed via the draft's own URL). This is first-party, technically
  authoritative engineering content from the team that built and ships the
  system described, not third-party reporting or marketing copy.
- **Scope**: Covers GPT‑Live's production system architecture end-to-end:
  full-duplex model design, Go-based media frontend, stateful model-instance
  handoff (for scaling and context compaction), frontier-model delegation
  latency engineering, deriving discrete conversational turns from continuous
  speech, two new WebRTC protocol extensions for faster session startup, and
  pre-launch shadow/silent production testing methodology and lessons. Does
  NOT cover: pricing, exact latency numbers (beyond the qualitative "p95
  matches previous system's p50" claim), model architecture/training details,
  or a systematic comparison against competitors. Per MINER.md's guidance to
  follow substantive linked pages, this note also extracts distinct claims
  from the two linked OpenAI pages named above — the product-level launch
  announcement (evaluation results, safety design, availability/limitations)
  and the predecessor infrastructure post (the relay+transceiver WebRTC
  deployment architecture this new system extends) — each clearly attributed
  to its own page in every claim below.

## Extracted Claims

### Claim 1: Prior turn-based voice AI systems relied on separate "turn detector" models that had to decide when the user finished speaking before the LLM could respond at all, forcing a tradeoff between cutting the user off and feeling sluggish
- **Evidence**: The post's own framing of the problem it set out to solve, stated in its opening paragraph.
- **Confidence**: settled (first-party description of the architecture GPT-Live replaces)
- **Quote**: "Their turn-based architecture relied on tiny models known as turn detectors, which faced an unenviable task: guess too soon, and the user gets cut off; guess too late, and the response feels sluggish. Only after the detector made its decision could the much larger LLM get to work."
- **Our assessment**: This names the specific mechanical bottleneck GPT-Live's full-duplex design (Claim 2) eliminates — not "make the turn detector smarter" but "remove the sequential dependency on a turn detector entirely." It is a clean example of solving a latency problem by deleting a pipeline stage rather than optimizing it, a pattern worth generalizing beyond voice AI.

### Claim 2: GPT‑Live, OpenAI's third-generation voice system, is full-duplex — it can listen and speak at the same time — which removes the turn detector from the audio path, and can consult frontier models like GPT‑5.5 for deeper reasoning or tool use without interrupting the conversation
- **Evidence**: The post's core architectural claim, stated directly.
- **Confidence**: settled (first-party architectural description of a shipped system)
- **Quote**: "GPT‑Live, our third-generation voice system, removes the turn detector from the audio path. Its voice model is full-duplex, which means it can listen and speak at the same time. That eliminates the need for a separate detector and makes conversation feel more immediate and natural. When deeper reasoning or tool use is needed, GPT‑Live can also consult our frontier models, such as GPT‑5.5, without interrupting the flow of the conversation."
- **Our assessment**: This directly corroborates and adds first-party mechanism detail to `blog-simonwillison-gptlive-voice-delegation.md` Claim 1, which documented the same delegation-to-GPT‑5.5 behavior from Simon Willison's own preview-access observation and a quote from OpenAI's product announcement. This source is the engineering-team account of *why* that architecture exists (eliminating the turn-detector bottleneck) and *how* it's built (Claims 3, 6-9 below), not just that it exists.

### Claim 3: GPT‑Live's system architecture streams audio continuously in both directions rather than using typical request-response inference, with frontier-model delegation running on a separate asynchronous path; the rebuild took six months and touched model inference, context management, and media transport
- **Evidence**: The post's direct statement of the system's shape and development timeline.
- **Confidence**: settled (first-party project-scope and architecture description)
- **Quote**: "Unlike typical request-response inference, our system streams incoming audio into the voice model and outbound speech back to the user, while handling delegation on a separate asynchronous path. Over the last six months, we reworked model inference, context management, and media transport to keep speech flowing smoothly from end to end."
- **Our assessment**: This is the single sentence that frames every other claim in this note as one coordinated system: streaming replaces request-response at the model layer, delegation is architecturally isolated onto its own path (Claim 8), and three separate subsystems (inference, context, transport) were rebuilt together rather than incrementally patched. Six months is a concrete, credible timeline for a ground-up real-time system rebuild at this scale.

### Claim 4: The media frontend and inference logic were rewritten in Go, replacing a previous Python `asyncio` implementation, and this significantly improved frame-delivery smoothness — the new system's p95 latency matches the old system's p50
- **Evidence**: A direct before/after language-and-metric statement.
- **Confidence**: settled (first-party statement with a specific, checkable relative metric, though no absolute latency numbers are given)
- **Quote**: "We wrote the media frontend and inference logic in Go, replacing a previous Python asyncio implementation. This significantly improved the smoothness of frame delivery, with the new system's p95 matching the previous system's p50."
- **Our assessment**: "p95 matches previous p50" is a specific, useful way to communicate a language/runtime rewrite's tail-latency impact without disclosing absolute numbers — it says the *worst* 5% of frames under the new system are no worse than the *median* frame under the old one. This is a concrete data point for practitioners evaluating whether a Python-asyncio-to-Go rewrite is worth the engineering cost for a latency-critical streaming media path specifically (not a general claim that Go beats Python for all AI workloads).

### Claim 5: WebRTC is used as GPT‑Live's transport foundation specifically because it can continue operating through packet loss, clock drift, and client connection changes, and because it can subtly stretch and then accelerate audio playback to smooth over late-arriving packets
- **Evidence**: A direct architectural justification for the transport choice.
- **Confidence**: settled (first-party statement of the transport layer and the specific resilience properties cited as the reason for choosing it)
- **Quote**: "WebRTC provides the transport foundation. It's designed for low-latency media, and can continue operating through packet loss, clock drift, and client connection changes. If packets arrive late, WebRTC can subtly stretch audio to prevent gaps, and then briefly accelerate playback to catch back up to real time."
- **Our assessment**: **This directly contradicts the architectural recommendation in `blog-simonwillison-luke-curley-webrtc.md`** — see Cross-References → Contradicts and the filed contradiction issue (#2655). Curley's critique (from an OpenAI-affiliated WebRTC expert) argues WebRTC's packet-dropping, no-buffering, arrival-time-based rendering ("timestamps are just suggestions") is a structural mismatch for LLM voice AI, and recommends WebSockets first, QUIC/WebTransport long-term. This source frames the *same* WebRTC behavior (audio stretching to survive late packets) as a strength, not a flaw, and OpenAI's own engineering team chose to keep and extend WebRTC (via WARP, Claim 10) rather than replace it. Notably, GPT-Live's full-duplex, continuously-streaming architecture (Claim 2) may not map cleanly onto Curley's framing, which was written against a discrete-prompt, turn-based mental model where a dropped packet "corrupts a prompt" — GPT-Live has no discrete prompt to corrupt in the same sense. Neither source resolves this distinction explicitly; it is flagged as unresolved context in the filed contradiction.

### Claim 6: Stateful voice-model instances use a "seamless handoff" mechanism for transitions — a replacement instance is warmed alongside the existing one, prefilled with the current session context, run in parallel with the original, and cut over to once fully ready
- **Evidence**: A dedicated explanation of the mechanism used to manage model-instance lifecycle changes (e.g., scaling up/down) without interrupting an active session.
- **Confidence**: settled (first-party description of a specific, named engineering mechanism)
- **Quote**: "To address these concerns, we built a seamless handoff mechanism across model instances. When a transition is needed, we can warm a replacement model instance alongside the existing one, prefill it with the current session context, run inference against both in parallel, and cut over when the new instance is fully ready."
- **Our assessment**: This is a concrete, reusable pattern for any long-running, stateful, latency-sensitive service that needs to survive instance churn (autoscaling, rolling deploys, node eviction) without a user-visible interruption: run two instances briefly in parallel, warm the new one with full state before routing to it, cut over only once ready. This is architecturally distinct from the "just reconnect" pattern documented in `blog-vercel-websocket-support-public-beta.md` Claim 5 — see Cross-References → Extends.

### Claim 7: The same handoff mechanism supports dynamic context compaction — compacting a conversation's context invalidates the model's KV cache and requires a costly reprefill, so the system runs compaction on a new replacement instance while the original instance keeps the conversation going, then switches over once ready, with no media interruption
- **Evidence**: A direct explanation of how compaction is implemented as a specific instance of the general handoff mechanism from Claim 6.
- **Confidence**: settled (first-party technical explanation, including the specific causal mechanism — KV cache invalidation forcing reprefill — that makes naive in-place compaction slow)
- **Quote**: "Instead, we treat compaction as another managed transition. While the original model instance keeps chatting, the system compacts the context and prepares a replacement model instance with the new context. Once that instance is ready, we can switch over without any media interruption. This allows the system to support long-running calls, compacting whenever necessary."
- **Our assessment**: This is a specific, technically grounded answer to a general problem in long-running stateful LLM sessions: context eventually exceeds the model's window, and compacting it (rewriting or summarizing history) invalidates cached attention state, making the compaction operation itself slow enough to be user-visible if done naively. Reusing the handoff mechanism (Claim 6) rather than building compaction as a separate code path is a notable design economy — one mechanism solves both "the instance needs to change" and "the context needs to change" because both ultimately require a state transition between two model instances.

### Claim 8: Delegation to frontier models is engineered as a pre-warmed, pinned resource — at session start, the application server creates and prefills a frontier-model inference session with the initial conversation context, keeps that session pinned via stable affinity for the call's duration, combines it with prompt caching, and tunes reasoning effort, output limits, and tool schemas specifically to reduce delegation latency
- **Evidence**: A dedicated explanation of the latency-optimization techniques applied to the background delegation path, framed as treating the full delegation loop as part of the system's responsiveness budget.
- **Confidence**: settled (first-party description of specific, named latency-optimization techniques)
- **Quote**: "When a voice session starts, the application server creates an inference session for the frontier model and prefills it with the initial conversation context, ensuring the prompt has been fully processed prior to the first delegated request. We then keep that inference session available for the duration of the voice conversation and use stable session affinity for successive requests. Together with prompt caching, these techniques improve latency while a worker failure remains easily recoverable. Reasoning effort, output limits, tool schemas, and model-tool round trips also affect when the conversation receives a useful result, and we adjusted these levers to get faster responses."
- **Our assessment**: This is the concrete engineering behind the "GPT‑Live delegates to GPT‑5.5 without interrupting the conversation" claim already in the corpus (`blog-simonwillison-gptlive-voice-delegation.md` Claim 1, assessed there as "architecturally close to a fire-and-forget subagent delegation pattern"). This source shows it is not a naive cold-start delegation call — the entire delegation path is pre-provisioned (prefilled session, pinned affinity) before it's ever needed, specifically to avoid paying setup latency on the critical path of a live conversation. This is directly actionable guidance for any harness that keeps a user-facing session open while delegating to a slower background model: pre-warm and pin the delegate's session at the start of the parent session, not at the moment of first delegation.

### Claim 9: To reconcile continuous full-duplex speech with turn-based downstream systems (the ChatGPT UI, analytics, safety infrastructure), the application server derives discrete messages from overlapping speech using partial transcripts and timing signals, maintaining a provisional "speculative" view for the live UI and a separately finalized "authoritative" view for analytics logging — with special handling so brief acknowledgements ("mm hmm," "okay") don't become their own messages while substantive interjections do
- **Evidence**: A dedicated section describing the message-segmentation problem and its resolution, including the specific dual-view design.
- **Confidence**: settled (first-party description of a specific, named design tradeoff and mechanism)
- **Quote**: "As audio arrives, the server uses partial transcripts and timing signals to infer which speaker has the floor and build a queue of messages. The newest message remains provisional; its text, timing, and speaker assignment can all change as more speech arrives... A brief acknowledgement from the assistant while the user is talking (e.g. 'mm hmm,' or 'okay') should not necessarily become its own message. However, a substantive assistant interjection often should... The system therefore maintains two related views of the conversation: a speculative view of the current state and an authoritative record of what was said."
- **Our assessment**: This is a specific, previously undocumented pattern in this corpus for any system that must present a continuous, ambiguous stream (overlapping speech) as discrete, orderable units to downstream consumers that expect turns. The "speculative view for UI, authoritative view for logging" split is a generalizable design: optimize the user-facing view for freshness (accept it may be revised) and the durable-record view for correctness (accept it lags). This has direct relevance to any multi-agent or streaming system where a live status display and a permanent audit log have different tolerance for revision.

### Claim 10: OpenAI developed and open-specified WARP (WebRTC Abridged Roundtrip Protocol) — a set of backward-compatible protocol improvements (piggybacking the DTLS handshake over ICE via SPED, using the faster DTLS 1.3 handshake, pre-negotiating the SCTP handshake via SNAP, and pre-negotiating data channels instead of using DCEP) — that reduces WebRTC media and data connection startup from six network round trips to one; WARP is being advanced through the IETF's TSVWG working group and is already implemented in libwebrtc and Pion
- **Evidence**: A dedicated section naming and describing WARP's four constituent protocol changes, plus a statement of its standardization and implementation status, corroborated by the WARP IETF draft itself (`datatracker.ietf.org/doc/draft-uberti-tsvwg-warp/`, authored by this post's co-author Justin Uberti, confirmed via the draft's URL when following the post's own link).
- **Confidence**: settled (first-party technical description of a named protocol, independently verifiable via a public IETF draft under the same author's name — not solely a vendor's own unverifiable claim)
- **Quote**: "We analyzed the stack and developed the WebRTC Abridged Roundtrip Protocol (WARP), which reduces media and data startup from six network round trips to just one... We're advancing the proposals through the IETF's TSVWG working group, and WARP support has already been added to both libwebrtc and Pion, with efforts underway in other WebRTC implementations."
- **Our assessment**: This is the second half of the WebRTC contradiction (alongside Claim 5): rather than abandoning WebRTC for the round-trip-heavy connection setup Curley's critique also names as a problem (`blog-simonwillison-luke-curley-webrtc.md` Claim 5: "a minimum of 8 round trips" for WebRTC vs. "1 for QUIC+TLS"), OpenAI's team built a WebRTC-compatible extension that gets the round-trip count down to a number competitive with QUIC (one) while keeping WebRTC itself. The IETF submission and existing libwebrtc/Pion support are concrete, checkable evidence this is a real, durable engineering artifact and not just marketing framing — worth citing directly if the guide ever discusses WebRTC vs. QUIC/WebSockets tradeoffs for real-time AI.

### Claim 11: OpenAI built "Instant Connect," which pre-negotiates WebRTC SDP signaling parameters ahead of time without reserving server capacity; if the pre-negotiated parameters are still valid when a session starts, the server can materialize the session on the first media packet, and if they're stale, the client falls back to standard signaling with no added latency — together with WARP, this lets a client start a session with a single UDP packet
- **Evidence**: A dedicated section describing the mechanism and its fallback behavior.
- **Confidence**: settled (first-party description of a specific, named mechanism with an explicit fallback path)
- **Quote**: "Instant Connect runs alongside the standard signaling flow. If the pre-negotiated parameters are valid, the server can materialize the session when the first media packet arrives. If they are stale or invalid, the signaling flow is already underway, so the client can fall back with no additional latency... the client can now start a session with a single UDP packet."
- **Our assessment**: The "runs alongside the standard flow, with no-penalty fallback" design is the notable engineering discipline here — Instant Connect is an optimistic optimization layered on top of a always-correct baseline path, not a replacement that could fail outright. This graceful-degradation-by-construction pattern (try the fast path speculatively, always have the slow path already in flight as a safety net) is a reusable design principle for any latency optimization on top of an existing, reliable protocol.

### Claim 12: Before general rollout, OpenAI ran a "silent test" that routed a small, gradually increasing share of real production ChatGPT Voice sessions through the new GPT‑Live system in read-only inference mode alongside the existing live Advanced Voice Mode system, exposing it to real clients, networks, session lengths, and geographic distribution without changing what any user actually heard
- **Evidence**: A dedicated section describing the pre-launch testing methodology.
- **Confidence**: settled (first-party description of a specific testing methodology)
- **Quote**: "Before letting GPT‑Live chat with users, we ran a silent test that routed a small, gradually increasing share of production ChatGPT Voice sessions to both the existing Advanced Voice Mode experience and our new system. Advanced Voice Mode continued serving users as usual, while the shadow path ran inference in read-only mode. This exposed the system to real clients, networks, session lengths, and geographic distribution without changing what users heard."
- **Our assessment**: This is a concrete shadow-deployment pattern for validating a real-time, stateful system against production traffic characteristics that synthetic load tests cannot reproduce (Claim 14), without any user-facing risk — the shadow path is read-only, so a bug in the new system cannot affect what a user hears. This is directly citable as a deployment-safety pattern for any team building a replacement for a live, stateful, latency-sensitive production system.

### Claim 13: Shadow-test load revealed that voice-session capacity could not be modeled as GPU throughput alone — CPU-side stream handlers, queues, and network paths had to scale alongside inference, and a non-GPU supporting component saturated earlier than load-test estimates predicted, forcing the team to reframe the capacity question from "how many requests can a GPU handle" to "how many concurrent sessions can the system sustain while keeping every frame on schedule"; the same testing made geography a first-order concern, since routing a session to distant capacity added delay at multiple points in both startup and streaming
- **Evidence**: A dedicated section describing specific capacity-planning lessons drawn from the silent test.
- **Confidence**: settled (first-party account of a specific, named operational lesson from production shadow testing)
- **Quote**: "One of the first lessons was that capacity could not be reduced to GPU throughput. Voice sessions stay open and send frames continuously, so CPU-side stream handlers, queues, and network paths must scale alongside inference. Under real load, a supporting component saturated earlier than our load test estimates predicted, causing inference requests to accumulate and latency to compound. We changed the capacity question from 'How many requests can a GPU handle?' to 'How many concurrent sessions can the system sustain while keeping every frame on schedule?'"
- **Our assessment**: This is a specific, generalizable capacity-planning failure mode for any long-lived, continuously-streaming (as opposed to short-request) AI service: GPU-centric capacity models miss non-GPU bottlenecks (connection handlers, queues, network paths) that scale with concurrent open sessions rather than request rate. Teams capacity-planning a streaming or agentic system with long-lived connections should explicitly test for this rather than extrapolating from GPU-throughput load tests alone.

### Claim 14: Realistic-session-lifecycle production testing surfaced failure modes that short load tests missed entirely: long-running sessions exposed memory and persistence pressure, reconnects exercised bugs in compaction and state restoration, and ordinary client disconnects revealed races in the shutdown handshake — prompting the team to add more granular telemetry, validation against known-good configurations, staged rollout ramps, and the ability to quickly isolate or disable individual paths
- **Evidence**: A dedicated section listing specific categories of production-only failures and the resulting observability/rollout investments.
- **Confidence**: settled (first-party account of specific failure categories and the resulting engineering response)
- **Quote**: "Other failures appeared only across realistic session lifecycles. Long-running sessions exposed memory and persistence pressure. Reconnects exercised compaction and state restoration. Ordinary client disconnects revealed races in the shutdown handshake. These problems rarely appeared in short load tests because they depended on time, accumulated state, and behavior across service boundaries... we added more granular telemetry, validation against known-good configurations, staged ramps, and the ability to isolate or disable individual paths quickly."
- **Our assessment**: The explicit causal claim — these bugs "depended on time, accumulated state, and behavior across service boundaries," which is exactly what short synthetic load tests don't exercise — is a specific, useful heuristic: for any stateful, long-running system, testing must include realistic session *duration* and *lifecycle events* (reconnect, disconnect, idle), not just realistic request *volume*. This corroborates and sharpens the general "shadow test with real production traffic" pattern from Claim 12 by naming exactly what that traffic reveals that synthetic load doesn't.

### Claim 15 (from linked predecessor post, "How OpenAI delivers low-latency voice AI at scale," May 4, 2026): OpenAI's prior-generation voice infrastructure deliberately kept WebRTC and built a custom "relay + transceiver" split architecture specifically to make WebRTC deployable on Kubernetes at scale — a stateless relay does first-packet routing (using the ICE `ufrag` field, a protocol-native routing hook, to identify the owning transceiver) while a stateful transceiver owns the full WebRTC session (ICE, DTLS, SRTP); this was deployed globally as "Global Relay" for geo-steered ingress
- **Evidence**: The predecessor post's dedicated architecture sections, authored by different OpenAI engineers (Yi Zhang and William McDonald) than the GPT‑Live post being mined, describing the system this GPT‑Live post explicitly says it built upon.
- **Confidence**: settled (first-party, detailed technical architecture description, cited by name and explicitly identified as prior work in the mined GPT‑Live post itself: "We had already rebuilt our voice infrastructure to stream audio and video directly in and out of our systems with lower and more predictable latency")
- **Quote**: "The team at OpenAI responsible for real-time AI interactions recently rearchitected our WebRTC stack to address three constraints that started to collide at scale: one-port-per-session media termination does not fit OpenAI infrastructure well, stateful ICE... and DTLS... sessions need stable ownership, and global routing has to keep first-hop latency low." / "Every WebRTC session already carries a protocol-native routing hook: the ICE username fragment, or ufrag... This architecture lets us run WebRTC media in Kubernetes without exposing thousands of UDP ports... [and] confirms that an SFU-less design was the right default for our workload."
- **Our assessment**: This is the strongest piece of evidence for the filed contradiction (issue #2655): this predecessor post was published May 4, 2026 — five days *before* Luke Curley's WebRTC critique (`blog-simonwillison-luke-curley-webrtc.md`, May 9, 2026), which was written in direct response to it ("How OpenAI delivers low-latency voice AI at scale" is the exact post Curley's blog post quotes and rebuts). The GPT‑Live post mined in this note (August 2026) explicitly builds on this same relay+transceiver WebRTC foundation as "an important foundation," three months after Curley's critique was published. OpenAI's own infrastructure choice — twice, across two consecutive voice-system generations, spanning a public critique from a WebRTC expert now at the same company — was to keep and extend WebRTC rather than adopt Curley's recommended WebSockets/QUIC path.

### Claim 16 (from linked product announcement, "Introducing GPT‑Live," July 8, 2026): In head-to-head evaluations, GPT‑Live‑1 and GPT‑Live‑1 mini were strongly preferred over the turn-based predecessor (ChatGPT Advanced Voice Mode) on human conversational-quality ratings, and GPT‑Live‑1 substantially outperformed Advanced Voice Mode on GPQA (expert-level scientific reasoning), showed strong gains on BrowseComp (agentic web search), and outperformed it on τ³-Voice Telecom (an internal variant testing realistic multi-turn telecom support tasks); OpenAI also cites more than 150 million weekly users of ChatGPT's Voice and Dictation features
- **Evidence**: The product announcement's dedicated "Evaluations" section, naming three specific benchmarks (GPQA, BrowseComp, τ³-Voice Telecom) and comparison conditions (matched 5-10 minute conversations). The τ³-Voice Telecom result carries a footnote marker disclosing that the eval was run against a synthetic counterpart: "We used a customized user model, powered by our latest reasoning models, for this eval."
- **Confidence**: emerging (first-party evaluation results with named benchmarks and comparison methodology stated, but no independent replication, and all three benchmark results are described only qualitatively — "substantially outperforms," "strong gains," "outperforms" — with no numeric scores given in the prose; the τ³-Voice Telecom result is additionally labeled by OpenAI itself as an "internal variant," scored against an OpenAI-built simulated user)
- **Quote**: "In these head-to-head comparisons, GPT‑Live‑1 and GPT‑Live‑1 mini are strongly preferred over Advanced Voice Mode in matched 5–10 minute conversations that measure overall preference, turn-taking, interruptions, conversational flow, and how natural each interaction felt." / "GPQA: GPT‑Live‑1 substantially outperforms Advanced Voice Mode on GPQA, which tests expert-level scientific reasoning across biology, chemistry, and physics." / "BrowseComp: GPT‑Live‑1 shows strong gains over Advanced Voice Mode on BrowseComp, which tests agentic web search and the ability to find difficult-to-locate information." / "τ³-Voice Telecom (internal variant)**: GPT‑Live‑1 outperforms Advanced Voice Mode on τ³-Voice Telecom, which tests voice agents on realistic, multi-turn telecom support tasks." / "We used a customized user model, powered by our latest reasoning models, for this eval." / "Each week, more than 150 million people talk to ChatGPT using features like Voice and Dictation."
- **Our assessment**: This is vendor-run, vendor-scored benchmarking without published numeric results or third-party replication — treat the *direction* of the claim (GPT‑Live is better than its own predecessor) as more credible than any specific magnitude, since no magnitude is actually given in prose. The τ³-Voice Telecom result is the weakest of the three for external readers and the most interesting for practitioners: weakest because it is explicitly an "internal variant" scored against a customized OpenAI user model, so both the benchmark and the simulated counterparty are vendor-controlled; most interesting because it is the only one of the three that measures the *agentic, multi-turn* task shape (telecom support) rather than single-shot knowledge or search, which is the shape most real voice-agent deployments actually have. The 150M weekly user figure is a scale data point establishing that this is not a niche feature; any latency or capacity lesson in Claims 12-14 should be read against a system serving hundreds of millions of weekly voice/dictation interactions.

### Claim 17 (from linked product announcement, "Introducing GPT‑Live," July 8, 2026): GPT‑Live ships with dedicated voice-specific safety training and safeguards that can act *while the model is speaking* — steering toward a safer response, surfacing safety resources, or ending the call in higher-risk cases — including adapted crisis-support flows for self-harm conversations, additional protections for teen users, and a restriction to a fixed set of predefined voices specifically to prevent voice impersonation
- **Evidence**: The product announcement's dedicated "Safety designed for voice" section.
- **Confidence**: settled (first-party statement of specific, named safety mechanisms and design constraints)
- **Quote**: "Because voice conversations unfold in real time, we also built safeguards that can act while the model is speaking. When the system detects potentially unsafe output, it can steer the model toward a safer response, surface additional safety messaging or resources, or end the voice conversation in higher-risk cases. For conversations involving self-harm, we adapted ChatGPT's support flows for voice, including offering expert-vetted crisis helpline support." / "GPT‑Live is designed for conversation, not voice impersonation. It uses a set of predefined voices in ChatGPT, with safeguards to prevent it from imitating a real person's voice."
- **Our assessment**: The "safeguards that can act while the model is speaking" claim is architecturally notable in light of Claim 2's full-duplex design — a mid-utterance safety intervention in a system that has no discrete "turn" to complete before intervening is a materially harder engineering problem than gating output before a single batched turn-based response is sent, though this source does not describe the intervention mechanism's own latency or false-positive/negative rate. No independent evaluation of these safeguards' effectiveness is cited in this source (see the "system card" link mentioned but not fetched — Extraction Notes).

### Claim 18 (from linked product announcement, "Introducing GPT‑Live," July 8, 2026): At launch, GPT‑Live does not support voice combined with video or screen sharing (features still available via legacy Standard/Advanced Voice Mode), and some languages have uneven fluency or a non-native accent, since GPT‑Live was optimized for "some of the most popular languages in ChatGPT" rather than uniformly across all supported languages
- **Evidence**: The product announcement's dedicated "Availability & limitations" section.
- **Confidence**: settled (first-party, explicit statement of specific launch-time feature gaps)
- **Quote**: "At launch, GPT‑Live will not support voice with video or screen sharing in ChatGPT, but we're working to introduce these capabilities soon. You can still access legacy versions of ChatGPT Voice, including Standard and Advanced Voice Mode, where these features are available." / "We've optimized GPT‑Live for some of the most popular languages in ChatGPT. For certain languages, the model may have a non-native accent or gaps in fluency."
- **Our assessment**: This is a directly useful practitioner caveat for anyone evaluating GPT‑Live for a non-English-first or video/screen-share-dependent use case: the new architecture is not yet a strict superset of the old one, and OpenAI's own retention of "legacy" Standard/Advanced Voice Mode for feature parity is itself an acknowledgment that the new system's capability surface is currently narrower along these two dimensions.

## Concrete Artifacts

### GPT‑Live's system architecture, end-to-end (synthesized from the mined post's section structure and prose, each element attributed to the source claim above)

```
Client (audio in/out)
   |
   |  WebRTC (Claim 5), started via Instant Connect + WARP (Claims 10-11):
   |    - 1 UDP packet to start a session (down from 6 RTT via WARP alone)
   |    - SDP params pre-negotiated ahead of time (Instant Connect)
   v
Media frontend + inference logic (Go, replacing Python asyncio — Claim 4)
   |  p95 latency now matches previous system's p50
   v
GPT-Live voice model (full-duplex, no turn detector — Claims 1-2)
   |  - continuous audio stream in/out
   |  - stateful; handled by "seamless handoff" mechanism for both
   |    instance transitions AND context compaction (Claims 6-7):
   |      warm replacement instance -> prefill with session context
   |      -> run both instances in parallel -> cut over when ready
   |
   |  Discrete turns derived from continuous speech (Claim 9):
   |      speculative view (live UI) + authoritative view (analytics/logging)
   |
   +--> Delegation path (async, does not block conversation - Claim 8):
          - frontier model (GPT-5.5 at launch) inference session
            created + prefilled with context AT SESSION START (not
            at first delegation)
          - stable session affinity + prompt caching for duration of call
          - reasoning effort / output limits / tool schemas tuned for
            delegation-path latency specifically

Source: OpenAI, "How we built a realtime system for responsive voice AI
in six months" (Justin Uberti, Zahan Malkani), openai.com/index/
continuous-voice-interaction-with-gpt-live, 2026-08-03
```

### WARP protocol breakdown (verbatim list of constituent changes)

```
WARP (WebRTC Abridged Roundtrip Protocol) — reduces media/data startup
from 6 network round trips to 1:

  - SPED: piggyback the DTLS handshake over ICE
  - DTLS 1.3: use the faster DTLS 1.3 handshake (vs. DTLS 1.2)
  - SNAP: pre-negotiate the SCTP handshake
  - Pre-negotiate data channels rather than using DCEP

Standardization: advancing through IETF's TSVWG working group.
Implementation status: already added to libwebrtc and Pion; efforts
underway in other WebRTC implementations.
IETF draft: draft-uberti-tsvwg-warp (authored by this post's co-author
Justin Uberti, per the draft's own URL, datatracker.ietf.org/doc/
draft-uberti-tsvwg-warp/ — followed from the post's own "WARP" link)

Source: OpenAI, "How we built a realtime system for responsive voice AI
in six months," openai.com/index/continuous-voice-interaction-with-gpt-live,
2026-08-03
```

### Silent-test capacity reframing (verbatim before/after question)

```
Before (load-test assumption):
  "How many requests can a GPU handle?"

After (production shadow-test finding):
  "How many concurrent sessions can the system sustain while keeping
  every frame on schedule?"

Cause: "Voice sessions stay open and send frames continuously, so
CPU-side stream handlers, queues, and network paths must scale alongside
inference. Under real load, a supporting component saturated earlier
than our load test estimates predicted."

Source: OpenAI, "How we built a realtime system for responsive voice AI
in six months," openai.com/index/continuous-voice-interaction-with-gpt-live,
2026-08-03
```

### Predecessor WebRTC deployment architecture (verbatim summary, from the linked May 2026 post)

```
"Relay + transceiver" split architecture (OpenAI, May 2026, predecessor
to the system in this note's primary source):

  Relay (stateless, small public UDP footprint):
    - does NOT decrypt media, run ICE state machines, or negotiate codecs
    - reads only the STUN packet's ICE "ufrag" field to identify the
      destination transceiver, then forwards packets
    - deployed globally as "Global Relay" for geo-steered ingress
    - written in Go; SO_REUSEPORT + runtime.LockOSThread for per-core
      flow affinity; no kernel-bypass framework used

  Transceiver (stateful, owns full WebRTC session):
    - owns ICE connectivity checks, DTLS handshake, SRTP keys,
      session lifecycle
    - originally: single Go service built on Pion, handling both
      signaling and media termination for ChatGPT voice, the Realtime
      API's WebRTC endpoint, and research projects

Purpose: make one-port-per-session WebRTC deployable on Kubernetes/cloud
load balancers without exposing large public UDP port ranges, while
keeping session state ownership stable across a fleet of autoscaling pods.

Source: OpenAI, "How OpenAI delivers low-latency voice AI at scale"
(Yi Zhang, William McDonald), openai.com/index/
delivering-low-latency-voice-ai-at-scale, 2026-05-04 — linked from and
described as foundational by the primary source of this note
```

## Cross-References

### Cross-reference verification notes
`blog-simonwillison-gptlive-voice-delegation.md`, `blog-simonwillison-luke-curley-webrtc.md`,
`blog-simonwillison-openai-webrtc-document-context.md`, `blog-vercel-websocket-support-public-beta.md`,
and `blog-anthropic-voice-mode-tools-multilingual.md` were each read in full
during this extraction, and every claim number cited below was located and
confirmed against that note's own numbered `### Claim N:` headings in
document order before writing this section.

- **Corroborates**:
  - `blog-simonwillison-gptlive-voice-delegation.md` Claim 1 (GPT‑Live
    delegates to GPT‑5.5 in the background without interrupting the
    conversation, per Willison's quote of OpenAI's product announcement):
    this source's Claims 2 and 8 independently confirm the same
    architecture from the engineering-team side, and supply the specific
    mechanism (pre-warmed, pinned, prompt-cached delegation session) that
    Willison's note explicitly says it does not cover ("no technical
    detail of how the delegation handoff is implemented").
  - `blog-anthropic-voice-mode-tools-multilingual.md`'s Cross-References
    section already speculated that "OpenAI's GPT‑Live delegates silently
    within a session" as a contrast to Claude voice mode's user-selected
    model tiers — this source confirms that characterization directly and
    supplies the mechanism (Claims 6-8) that note did not have access to.

- **Contradicts**:
  - **`blog-simonwillison-luke-curley-webrtc.md`** (entire note, particularly
    Claims 1, 3, 4, 5, and 8): Curley argues WebRTC is architecturally wrong
    for LLM voice AI (packet-dropping harms prompt accuracy, browser
    retransmission is impossible, WebRTC's 8-RTT connection setup is a
    structural cost, and recommends WebSockets first / QUIC long-term
    instead). This source's Claims 5, 10, and 15 show OpenAI's own
    production system reaffirming WebRTC as the transport across two
    consecutive voice-system generations — including a dedicated protocol
    extension (WARP) built specifically to address the round-trip-count
    objection Curley raised, rather than abandoning WebRTC. **A
    contradiction issue has been filed: issue #2655** (per MINER.md §4a),
    since this bears directly on the guide's transport-protocol-selection
    guidance for voice AI (Chapter 03). Do not treat either source's
    transport recommendation as settled guide advice until that issue is
    resolved; the filed issue also notes an important nuance neither
    source addresses explicitly — Curley's critique targets discrete,
    corruptible "prompts," while GPT‑Live's continuous full-duplex stream
    (Claim 2) may not have the same failure mode.

- **Extends**:
  - `blog-simonwillison-openai-webrtc-document-context.md` Claim 2 (OpenAI's
    Realtime API ephemeral-token/session model: a 60-second connection
    token, then a session lasting "up to 30 minutes") and Claim 5
    (GPT-Realtime-2's configurable reasoning effort as a latency/quality
    tradeoff knob): this source's Claim 8 (pre-warmed, pinned delegation
    sessions with tuned reasoning effort) describes a related but distinct
    latency-management mechanism — instead of tuning one model's own
    reasoning effort per request, GPT‑Live routes to a separate,
    continuously-warm background model and tunes *that* model's reasoning
    effort specifically for the delegation path.
  - `blog-vercel-websocket-support-public-beta.md` Claim 5 (Vercel Function-
    hosted WebSocket connections cannot resume across reconnects; state
    must be externalized and replayed) and Claim 4 (connection lifetime is
    hard-capped by the hosting Function's max duration): this source's
    Claims 6-7 describe a materially different design philosophy for
    session continuity — rather than accepting forced disconnection and
    requiring the client to replay context (Vercel's pattern), GPT‑Live's
    "seamless handoff" mechanism keeps a session's *state* alive across an
    *instance* transition, so the client-visible session itself never
    needs to reconnect at all. These are not contradictory (they solve
    different problems — Vercel's Functions are a general-purpose hosting
    primitive with hard duration ceilings; GPT‑Live is a purpose-built
    voice system optimizing specifically for zero-interruption long calls)
    but are a useful architectural contrast for the guide: "accept
    disconnection and externalize state" vs. "engineer around ever needing
    to disconnect" are two different answers to the same underlying
    long-lived-session problem, with different engineering costs.

- **Novel**:
  - **Reusing one "seamless handoff" mechanism for both instance-scaling
    transitions and context compaction** (Claims 6-7): no existing corpus
    source documents this specific unification — treating "the model
    instance needs to change" and "the context needs to change" as the
    same underlying operation (warm a replacement, prefill it, run in
    parallel, cut over) is a distinctive design economy not previously
    captured in this corpus's coverage of long-running stateful AI systems.
  - **WARP and Instant Connect as concrete, IETF-submitted WebRTC
    round-trip-reduction protocols** (Claims 10-11): no existing corpus
    source documents a specific, standardized (in-progress) protocol
    extension that reduces WebRTC's connection-setup round-trip count;
    this is new, checkable technical detail (verifiable via the public
    IETF draft) directly relevant to the WebRTC-vs-QUIC/WebSockets debate
    already present in the corpus via the Curley note.
  - **Speculative vs. authoritative dual views for reconciling continuous
    streams with turn-based downstream consumers** (Claim 9): no existing
    corpus source documents this specific pattern for deriving discrete,
    orderable units from an inherently continuous, ambiguous stream.
  - **Shadow/silent production testing for a stateful, real-time voice
    system, and the specific capacity-planning and session-lifecycle
    lessons it surfaced** (Claims 12-14): no existing corpus source
    documents this specific pre-launch validation methodology (route a
    growing share of live production traffic through the new system in
    read-only mode) or the specific finding that GPU-throughput-based
    capacity models miss non-GPU bottlenecks that scale with concurrent
    open sessions.
  - **A dedicated mid-utterance safety-intervention mechanism for a
    full-duplex (no discrete turn boundary) conversational system**
    (Claim 17): no existing corpus source documents a voice AI safety
    mechanism designed to act while the model is still speaking, as
    distinct from gating a single batched response before it is sent.

## Guide Impact

- **Chapter 03 (Architecture & Design — Voice AI System Design / Transport
  Protocol Selection)**: This source is first-party, technically detailed
  counter-evidence to the existing recommendation (sourced from
  `blog-simonwillison-luke-curley-webrtc.md`) that the guide advise against
  WebRTC for LLM voice AI. Do not resolve this in the guide text until
  contradiction issue #2655 is resolved; when it is, cite this source's
  Claims 5, 10, and 15 as OpenAI's own, twice-repeated, production
  decision to keep and extend WebRTC (via WARP/Instant Connect) rather
  than switch to WebSockets/QUIC as Curley recommended.
- **Chapter 02 (Harness Engineering — Delegation & Latency-Hiding
  Patterns)**: Add Claim 8's pre-warm/pin-at-session-start delegation
  pattern as a concrete technique for any harness that keeps a live
  session open while delegating slower work to a background model: create
  and prefill the delegate's inference session when the parent session
  starts (not at first delegation), pin it with stable affinity, and
  layer prompt caching on top — this measurably reduces the latency a
  live session-holder experiences on first delegation, extending the more
  general delegation framing already in `01-daily-workflows.md` with a
  specific pre-provisioning technique.
- **Chapter 02 (Harness Engineering — Stateful Session Continuity)**: Add
  Claims 6-7's "seamless handoff" pattern (warm replacement instance,
  prefill with session state, run in parallel, cut over) as a concrete
  alternative to the "accept disconnection, externalize state, replay on
  reconnect" pattern already documented via
  `blog-vercel-websocket-support-public-beta.md` — present both as valid
  answers to the long-lived-stateful-session problem, with the tradeoff
  made explicit: GPT‑Live's approach requires running two model instances
  briefly in parallel (a real compute cost) to avoid ever forcing a
  client-visible reconnect, while Vercel's approach accepts forced
  reconnects but avoids that duplicate-compute cost.
- **Chapter 02/03 (Testing & Deployment Safety)**: Add Claims 12-14 (silent
  shadow testing against real production traffic; the GPU-throughput
  capacity-modeling failure; realistic-session-lifecycle testing surfacing
  bugs short load tests miss) as a concrete deployment-validation pattern
  for any team replacing a live, stateful, real-time production system —
  directly relevant if the guide ever covers rollout/testing strategy for
  agentic or streaming systems beyond simple blue/green deploys.
- No new change recommended to `04-context-engineering.md`,
  `05-team-adoption.md`, or `06-security-threat-model.md` from this
  source's core engineering claims — though Claim 17's mid-utterance
  safety-intervention mechanism could be cited in `06-security-threat-model.md`
  if that chapter ever covers voice as a distinct attack/harm surface,
  since it documents a materially different safety-gating mechanism than
  the turn-based, pre-response gating the corpus otherwise documents (e.g.
  `blog-anthropic-voice-mode-tools-multilingual.md` Claim 4's
  confirm-before-tool-use gate, which operates between turns, not mid-turn).

## Extraction Notes

- **Primary source required a Wayback Machine fetch; both direct `curl`
  and WebFetch failed.** The live URL
  (`openai.com/index/continuous-voice-interaction-with-gpt-live`) returned
  HTTP 403 to both a browser-UA `curl` request and a Googlebot-UA `curl`
  request (an anti-bot/Cloudflare-style challenge page, consistent with
  the same blocking behavior noted in `blog-simonwillison-gptlive-voice-delegation.md`'s
  Extraction Notes for a different OpenAI announcement page), and
  WebFetch returned a bare HTTP 403 with no content. The article was
  instead retrieved via the Internet Archive Wayback Machine (snapshot
  `20260806030730`, captured August 6, 2026 — three days after original
  publication), fetched via `curl` and parsed with BeautifulSoup to
  extract plain article text. All `Quote` fields in this note were
  matched character-for-character against that locally-parsed plain text,
  not against any AI-summarized intermediate.
- **Two linked sub-pages followed in full, per MINER.md §1.** The
  post's own links to OpenAI's July 8, 2026 product announcement
  ("Introducing GPT‑Live") and its May 4, 2026 predecessor engineering
  post ("How OpenAI delivers low-latency voice AI at scale") were both
  substantive (the latter is explicitly named by the mined post as "an
  important foundation" it built on, and turned out to be the exact post
  `blog-simonwillison-luke-curley-webrtc.md`'s Curley critique responds
  to — a directly relevant discovery for the contradiction filed below).
  Both were fetched via the same Wayback Machine approach (snapshots
  `20260725135547` and `20260718004526` respectively) after confirming
  the live URLs were also behind the same anti-bot block. Claims from
  each are explicitly labeled by source page in this note's Extracted
  Claims section.
- **IETF drafts and RFCs linked from the WARP/SPED/DTLS-1.3/SNAP/DCEP
  references were not fetched as separate sources.** These are primary
  protocol specifications (IETF datatracker drafts, RFC documents), not
  additional explanatory prose — the mined post's own text already states
  the claims this note extracts about them (what each does, and that WARP
  reduces round trips from six to one). The WARP draft's URL
  (`datatracker.ietf.org/doc/draft-uberti-tsvwg-warp/`) was used only to
  confirm authorship (Justin Uberti, this post's co-author) as an
  authority signal in Source Context and Claim 10, not to extract
  additional claims from its technical content.
- **Contradiction filed**: Per MINER.md §4a, this source's Claims 5, 10,
  and 15 materially oppose `blog-simonwillison-luke-curley-webrtc.md`'s
  recommendation against WebRTC for LLM voice AI. Filed as issue #2655
  before this PR was opened, using the contradiction issue template, with
  Side A (Curley) and Side B (this source) both summarized with their own
  evidence and confidence levels, and a filer-recommended verdict of
  `debated` (since WARP addresses only the round-trip-count objection, not
  Curley's separate packet-dropping/retransmission critique, and GPT-Live's
  full-duplex streaming architecture may not map onto Curley's
  discrete-prompt framing — neither source resolves this explicitly). No
  verdict is asserted in this source note itself; see issue #2655 and
  (once resolved) CONTRADICTIONS.md for the eventual resolution.
- **Cross-reference verification**: `blog-simonwillison-gptlive-voice-delegation.md`,
  `blog-simonwillison-luke-curley-webrtc.md`,
  `blog-simonwillison-openai-webrtc-document-context.md`,
  `blog-vercel-websocket-support-public-beta.md`, and
  `blog-anthropic-voice-mode-tools-multilingual.md` were each re-read in
  full before writing Cross-References; all claim numbers cited were
  located and confirmed against each note's own numbered `### Claim N:`
  headings in document order.
- **Confidence calibration: emerging.** Individual engineering-mechanism
  claims (Claims 1-15) are rated "settled" because they are detailed,
  first-party, mechanism-level descriptions from the engineers who built
  the system, with some independently verifiable via public artifacts
  (the WARP IETF draft). The two evaluation/product claims drawn from the
  launch announcement (Claims 16, 17) are more marketing-adjacent —
  vendor-run, vendor-scored comparisons with qualitative rather than
  numeric results reported in prose. The note's overall confidence is
  "emerging" rather than "settled" because this is a single vendor's own
  account of its own system with no independent benchmarking,
  third-party production validation, or disclosed absolute latency
  numbers anywhere in the source family — the qualitative "p95 matches
  previous p50" comparison (Claim 4) is the closest thing to a hard
  metric in the entire source.
