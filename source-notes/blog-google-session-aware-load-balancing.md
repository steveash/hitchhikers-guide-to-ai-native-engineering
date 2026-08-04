---
source_url: https://developers.googleblog.com/scaling-real-time-ai-agents-with-session-aware-load-balancing/
source_type: blog-post
title: "Scaling Real-Time AI Agents with Session-Aware Load Balancing"
author: Simerus Mahesh (Google, Site Reliability Engineer)
date_published: 2026-08-03
date_extracted: 2026-08-04
last_checked: 2026-08-04
status: current
confidence_overall: emerging
issue: "#2477"
---

# Scaling Real-Time AI Agents with Session-Aware Load Balancing

> A Google SRE argues that QPS and CPU utilization — the two metrics
> traditional load balancers optimize for — both fail to represent load for
> long-lived, stateful, bidirectional AI streams (voice, video), and proposes
> a hybrid model where application-level active-session counts are
> normalized into a rate ("pretend QPS") and combined with CPU utilization
> via a capacity-estimation formula with a tunable safety scaler.

## Source Context

- **Type**: blog-post (Google Developers Blog, `developers.googleblog.com`,
  published August 3, 2026). A single-author technical explainer with one
  embedded Kotlin code sample, one embedded plain-text formula (`remaining_capacity
  = max_sessions - active_sessions`), and one embedded capacity-estimation
  formula presented as an image rather than text (see Extraction Notes).
  Cross-posted under categories AI, Best Practices, Industry Trends,
  Solutions, Load Balancing, AI Infrastructure, AI Agents.
- **Author credibility**: Simerus Mahesh is credited as a Google Site
  Reliability Engineer. This is a first-party post on Google's own developer
  blog, written from an SRE's operational vantage point (the author writes in
  first person about validating tracker overhead, JVM microbenchmarking, and
  production load-balancing design), not a marketing or product-launch post.
  No specific Google product (e.g., a named load balancer or Cloud Run
  feature) is cited as shipping this behavior — the post presents a general
  architectural pattern and reasoning, not a product announcement.
- **Scope**: Covers why QPS/CPU-based load balancing breaks down for
  real-time, bidirectional AI streams; how to track active sessions inside a
  runtime; how to combine session counts with CPU utilization into a hybrid
  capacity-estimation model; what dimensions to vary when benchmarking
  session-aware balancers; and how to validate that the session tracker
  itself doesn't become a concurrency bottleneck. Does NOT cover: a specific
  named load balancer product or proxy (the article says "the exact algorithm
  depends on your proxy and workload"), any measured before/after production
  numbers for this technique, WebRTC/transport-protocol selection, or model
  inference cost/latency.

## Extracted Claims

### Claim 1: Traditional load balancing (request throughput + CPU utilization) assumes each request consumes predictable, similarly-sized resources and that finishing a task frees capacity — an assumption that breaks down for long-lived, stateful AI streams
- **Evidence**: A direct comparison of two hypothetical backend tasks with identical request counts but wildly different session durations.
- **Confidence**: emerging (first-party SRE reasoning with an illustrative example, no measured production comparison given)
- **Quote**: "Consider two backend tasks: Task A handles 100 short requests, each finishing in 50 milliseconds. Task B accepts just 5 requests, but each turns into a 20-minute session. If you only judge these by request arrival rates, Task B appears less busy by request rate, yet it may actually be shouldering a significantly heavier, more committed workload."
- **Our assessment**: This is the article's central motivating example and it is logically sound: request-rate metrics are blind to session duration entirely. The claim is presented as illustrative reasoning rather than a measured production incident, so we treat it as a well-argued but anecdotal framing device rather than settled empirical fact.

### Claim 2: QPS tracks arrival volume but cannot capture how many live conversations a server is already committed to handling
- **Evidence**: A direct, standalone statement following the Task A/Task B example.
- **Confidence**: emerging (architectural reasoning, consistent with how QPS is defined, not independently measured)
- **Quote**: "QPS tracks arrival volume, but fails to capture the number of live conversations a server is already managing."
- **Our assessment**: This is the crisper, more citable restatement of Claim 1's example — a one-sentence definition of the QPS blind spot for streaming workloads. Worth quoting directly in the guide as the compact version of the argument.

### Claim 3: CPU utilization under-reports load for backends holding many silent/idle streaming sessions, then can spike suddenly when those sessions simultaneously become active
- **Evidence**: A voice-runtime example: 20 silent sessions look like low utilization until all 20 users start speaking at once.
- **Confidence**: emerging (illustrative example, no measured spike magnitude or timing given)
- **Quote**: "A voice runtime, for example, might host 20 silent sessions; because there's no active speech processing or model inference happening, the server looks underutilized. But as soon as those 20 users start speaking simultaneously, CPU usage can spike suddenly."
- **Our assessment**: This is the CPU-side mirror of Claim 2's QPS-side blind spot — together they establish that neither of the two metrics traditional load balancers already have is sufficient on its own for session-heavy AI workloads. The claim implies (but does not measure) that a CPU-only autoscaler/balancer would route new sessions onto a backend that looks idle but is actually holding a large latent-demand pool.

### Claim 4: Standard load balancers cannot distinguish a genuinely active conversation from an idle listener or background noise (retries, health checks) inside a bidirectional stream, because that state exists only at the application layer
- **Evidence**: Direct architectural statement contrasting a "network observer's" view of a stream with the application's view of it as a stateful session holding audio buffers, partial transcripts, active tool calls, and model context.
- **Confidence**: emerging (architectural reasoning about protocol-layer visibility, internally consistent, not independently benchmarked)
- **Quote**: "Standard load balancers struggle with this. They see the stream, but they can't distinguish between a genuinely active user conversation, an idle listener, or background noise like retries and health checks."
- **Our assessment**: This is the article's justification for why the fix has to live in the application/service layer rather than the load-balancing layer itself — the load balancer structurally cannot see what it would need to see to make this distinction on its own, so the backend service has to compute and report the signal.

### Claim 5: A minimal pattern for tracking active sessions is to increment a counter when a streaming session starts and decrement it in a `finally` block when it ends, since the counter's accuracy for routing decisions depends entirely on the decrement always firing
- **Evidence**: A complete Kotlin code sample (`handleAudioSession`) using `activeSessions.incrementAndGet()` before a `withTimeout` block and `activeSessions.decrementAndGet()` in a `finally` clause.
- **Confidence**: emerging (a concrete, runnable-looking code pattern presented as illustrative guidance, not confirmed as Google's own production implementation)
- **Quote**: "The finally block goes beyond basic cleanup. It is what keeps the active-session count accurate enough for routing decisions." / "If the counter fails to decrement, your backend might look overloaded long after the session finishes."
- **Our assessment**: The pattern itself is a standard resource-cleanup idiom, but the article's framing is useful: it explicitly ties correct cleanup to routing correctness, not just memory hygiene. A stuck counter doesn't just leak memory — it actively misleads the balancer into avoiding a backend that has capacity, or (in the double-decrement case) overloading one that doesn't.

### Claim 6: A session counter that fails to decrement or double-decrements produces "ghost sessions" that act as misleading routing signals, not merely as a memory leak — and production implementations must handle the case where a timeout, cancellation, and disconnect fire simultaneously for the same session
- **Evidence**: Direct follow-on statement after the Kotlin example, naming the specific race condition (concurrent timeout/cancel/disconnect) that risks a double-decrement.
- **Confidence**: emerging (architectural/operational guidance, no incident data or measured frequency given)
- **Quote**: "Conversely, a double-decrement might report false capacity, drawing in excessive traffic. Production implementations also need to carefully manage edge cases where a timeout, cancellation, or disconnect event all trigger simultaneously to clean up the same session." / "Essentially, ghost sessions act as misleading routing signals rather than simple memory leaks."
- **Our assessment**: The "ghost sessions" framing is a useful, memorable name for this failure mode. The specific race condition named (timeout + cancellation + disconnect firing together) is a concrete, checkable edge case a team implementing this pattern should write a test for — the article doesn't give a code fix for it, only names it as a hazard.

### Claim 7: Because load balancers poll metrics at intervals while sessions start and stop continuously, a session-tracking service must report a consistent snapshot of active sessions rather than a value that can change mid-read, or the load balancer will route decisions against stale data
- **Evidence**: Direct statement on synchronization requirements for the reported metric.
- **Confidence**: emerging (architectural reasoning about polling vs. continuous state, no specific synchronization mechanism prescribed)
- **Quote**: "Even with a precise counter, you have to account for synchronization. Because load balancers generally pull metrics at intervals, while sessions start and stop fluidly, your service needs to report a consistent snapshot of active sessions to prevent the load balancer from making decisions based on outdated data."
- **Our assessment**: This claim identifies a requirement (snapshot consistency) without prescribing an implementation (e.g., no mention of atomic snapshot reads, versioned counters, or specific consistency guarantees). It's a design constraint worth carrying into the guide, but practitioners will need to supply their own mechanism.

### Claim 8: Active session counts should not replace CPU/memory-utilization-based balancing but be combined with it in a hybrid model, because utilization captures current resource pressure while session count captures already-committed future load
- **Evidence**: Direct architectural statement following a critique of a naive static-slot capacity model (`remaining_capacity = max_sessions - active_sessions`), which the article calls "brittle" because it assumes every session costs the same CPU.
- **Confidence**: emerging (architectural reasoning; the naive-model critique is logically sound, the "hybrid" prescription is the article's own design recommendation, not independently validated)
- **Quote**: "This is why active session counts should not replace utilization-based balancing; they must be combined into a hybrid model. Utilization (CPU/Memory) captures current resource pressure, while the session count captures committed future load."
- **Our assessment**: This is the article's core thesis, stated most directly here. The two signals are framed as complementary rather than substitutable — one is a snapshot of current cost, the other a snapshot of accepted (but not necessarily currently CPU-intensive) commitments.

### Claim 9: Session counts can be normalized into a rate ("pretend QPS") by dividing the session count by the reporting-window duration, so that a session-aware routing layer can add session pressure to traditional rate-based signals like QPS without redefining the balancer's unit of measurement
- **Evidence**: A worked example converting 90 active sessions over a 10-second window into "9 pretend QPS."
- **Confidence**: emerging (a specific, checkable normalization technique presented as "one implementation," not stated as the only or standard approach)
- **Quote**: "Because load balancers inherently think in rates, they translate the static session count into a continuous flow. For example, if a backend holds 90 active sessions over a 10-second reporting window, one implementation could treat this as 9 \"pretend QPS.\" By converting static sessions into a standard rate, the routing layer can seamlessly add session pressure to traditional signals like QPS."
- **Our assessment**: This is a concrete, reusable integration technique for teams that already have a QPS-based load balancer and don't want to rip it out — session pressure gets folded into the existing rate-based signal rather than requiring a net-new routing dimension. The article is explicit that this is "one implementation," not a standard, so practitioners should treat the specific normalization (divide by window duration) as a starting point, not a spec.

### Claim 10: A capacity-estimation formula combining Target Utilization, Average Utilization, Cost Per Session, and a Safety Scaler produces an "Additional_Session_Rate" that, added to current active sessions, estimates a backend's true effective capacity — with the Safety Scaler specifically dampening allocation because CPU scales non-linearly with concurrent streams
- **Evidence**: A named formula (presented as an image in the source, not extractable as text — see Extraction Notes) with four defined input variables and two worked numeric scenarios.
- **Confidence**: emerging (a named formula and defined variables, but the article itself calls it "simplified" and states "the exact algorithm depends on your proxy and workload")
- **Quote**: "Target Utilization: The ceiling you want to safely run at (e.g., 80% CPU)." / "Safety Scaler: A dampening multiplier (e.g., 2.0). Because CPU utilization often scales non-linearly with concurrent streams, this acts as a penalty factor to prevent the load balancer from dumping too many new sessions onto a seemingly idle backend at once." / "Once the load balancer computes this Additional_Session_Rate, it multiplies it by the reporting interval and adds it to the currently active sessions to find the true Effective Capacity."
- **Our assessment**: The two worked examples make the formula's behavior concrete without needing the underlying equation: "a backend with 10 active sessions and 90% CPU will have a very high Cost_Per_Session, driving its Additional_Session_Rate to zero, resulting in it receiving no new traffic," while "a backend with 80 active sessions but only 40% CPU might seem like it has room, but the Safety_Scaler ensures it is only fed new sessions gradually, preventing sudden spikes." The article explicitly disclaims this as prescriptive ("the exact algorithm depends on your proxy and workload"), so we read this as a worked illustration of a design pattern, not a formula to copy verbatim into production.

### Claim 11: Session-aware load-balancing benchmarks must vary session-specific dimensions (concurrent session counts, session duration, arrival patterns, idle-to-active speaking ratios, cancellation/disconnect rates, backend counts, max sessions per backend) because fire-and-forget short-request load tests don't replicate long-lived AI session behavior, and request-based balancing tends to produce "lumpy" traffic where some backends accumulate long sessions while others idle
- **Evidence**: An explicit list of benchmark dimensions, plus a named list of streaming-specific metrics to track (active-session distribution, overloaded assignment rates, p95/p99 startup latency, time-to-first-stream, dropped sessions, counter behavior after forced disconnects).
- **Confidence**: emerging (methodological guidance/checklist, no specific benchmark results or numbers reported)
- **Quote**: "Tests that send bursts of short requests primarily measure request throughput, which doesn't replicate the behavior of long-lived AI sessions." / "Request-based balancing often creates lumpy traffic, where some backends accumulate long-lived sessions while others sit idle."
- **Our assessment**: This is a practical checklist for teams validating a session-aware balancer, distinct from a benchmark result — the article gives the dimensions to vary and metrics to watch, not measured numbers from running such a benchmark. Useful as a starting checklist, not as evidence the described hybrid model outperforms request-based balancing by any specific margin.

### Claim 12: Session trackers sit on a critical path (every stream start/end hits them), so validating their overhead requires proper microbenchmarking (accounting for JIT warmup and dead-code elimination on the JVM) focused on contention behavior rather than single-threaded latency — a plain `AtomicInteger` can suffer severe cache-line contention at high concurrency, where sharded counters or `LongAdder`-style aggregation may be more appropriate
- **Evidence**: A dedicated "Validating tracker overhead" section naming a specific Java concurrency primitive and its failure mode at scale.
- **Confidence**: emerging (specific, checkable technical claim about JVM concurrency primitives; consistent with well-documented `AtomicInteger`/`LongAdder` behavior, but no benchmark numbers given in this article)
- **Quote**: "Every stream start and end hits them, so if you're managing massive concurrency, it's important that it's designed to ensure that this tracking doesn't bottleneck a service." / "Using Java as an example, an AtomicInteger may be perfectly fine for many workloads, but at high concurrency, it can suffer from severe cache-line contention (bouncing) as multiple threads constantly attempt to update the same memory address. In high-throughput scenarios, designs such as sharded counters or LongAdder-style aggregation may become more appropriate to maintain throughput."
- **Our assessment**: This is the most concrete, implementation-level guidance in the article and the only claim naming a specific runtime (JVM) and specific primitives (`AtomicInteger`, `LongAdder`, sharded counters). It's a well-known JVM concurrency pattern (not novel computer science), but its application here — specifically to session-tracking counters that gate load-balancing decisions — is a useful, concrete implementation detail for anyone building the Claim 5 pattern at scale.

## Concrete Artifacts

### Kotlin session-tracking pattern (verbatim, from "Tracking active sessions inside the runtime")

```kotlin
suspend fun handleAudioSession(audioStream: Flow<AudioFrame>) {
    activeSessions.incrementAndGet()

    try {
        withTimeout(20.minutes) {
            audioStream.collect { frame ->
                processAndRespond(frame)
            }
        }
    } finally {
        activeSessions.decrementAndGet()
    }
}
```
Source: developers.googleblog.com/scaling-real-time-ai-agents-with-session-aware-load-balancing/

### Naive static-slot capacity model (verbatim, rejected as "brittle")

```
remaining_capacity = max_sessions - active_sessions
```
"If you have room for 100 sessions and are holding 80, you have 20 slots left. But this is brittle. It assumes every session costs the same amount of CPU, which is rarely true in generative AI."

### Benchmark dimensions checklist (verbatim, from "Benchmarking session-aware balancing")

```
Effective benchmarks should vary:
- concurrent session counts
- session duration
- arrival patterns
- ratios of idle to active speaking
- cancellation and disconnect rates
- backend counts
- maximum sessions per backend

Metrics to track beyond average latency and QPS:
- active-session distribution across backends
- overloaded assignment rates
- p95 and p99 startup latency
- time-to-first-stream
- dropped sessions
- counter behavior after forced disconnects
```

### Capacity-estimation formula variables (verbatim quotes; the formula expression itself is an embedded image, not extractable text — see Extraction Notes)

```
Target Utilization: The ceiling you want to safely run at (e.g., 80% CPU).
Average Utilization: The smoothed CPU consumption over the last reporting
  window (e.g., the last 10 seconds).
Cost Per Session: The dynamically calculated average CPU cost of an active
  stream during the last reporting window.
Safety Scaler: A dampening multiplier (e.g., 2.0) — a penalty factor to
  prevent the load balancer from dumping too many new sessions onto a
  seemingly idle backend at once, because CPU utilization often scales
  non-linearly with concurrent streams.

Worked scenarios:
- 10 active sessions, 90% CPU -> very high Cost_Per_Session -> Additional_
  Session_Rate drops to zero -> backend receives no new traffic.
- 80 active sessions, 40% CPU -> looks like it has room, but Safety_Scaler
  ensures new sessions are fed gradually rather than in a spike.
```

## Cross-References

### Cross-reference verification notes
`blog-simonwillison-luke-curley-webrtc.md`, `blog-vercel-websocket-support-public-beta.md`,
and `blog-vercel-ai-gateway-realtime-voice-speech.md` were re-read in full during this
extraction (MINER.md §4b), and every claim number cited below was located and confirmed
against that note's own numbered `### Claim N:` headings in document order before writing
this section.

- **Corroborates**: None identified as a matching claim on the same fact. This
  source's central argument (QPS/CPU are insufficient signals for streaming
  AI workloads) is a novel contribution not directly asserted by any prior
  corpus note; the closest adjacent notes (below) address related but
  distinct layers of the same problem space, so they are filed under Extends
  rather than Corroborates.

- **Contradicts**: None filed as a formal MINER.md §4a contradiction. One
  near-miss was evaluated: `blog-simonwillison-luke-curley-webrtc.md` Claim 8
  recommends streaming audio over WebSockets specifically because it lets a
  team "leverage existing TCP/HTTP infrastructure instead of inventing a
  custom WebRTC load balancer," calling the resulting architecture "simple"
  and something that just "SCALES" with Kubernetes. This source, writing from
  inside a team operating exactly that kind of infrastructure, argues that
  standard (QPS/CPU) load balancing silently fails for long-lived streaming
  sessions and that a custom, application-level, session-aware routing layer
  is required on top of the transport choice. These are not opposing claims
  about the same fact: Curley's claim is about *connection-establishment*
  simplicity (WebSockets vs. WebRTC's NAT/ICE/port-exhaustion machinery, a
  problem this source never mentions), while this source is about *ongoing
  capacity-routing* correctness once connections already exist (a problem
  Curley's post never addresses). A team could accept both claims at once:
  WebSockets remain the simpler transport to establish and route at the
  connection-setup layer, while still needing the session-aware capacity
  model this source describes to route *new* connections well once volume
  grows. No contradiction issue filed.

- **Extends**:
  - `blog-simonwillison-luke-curley-webrtc.md` Claim 8 (WebSockets/gRPC over
    existing TCP/HTTP infrastructure as the pragmatic transport choice for
    LLM voice/streaming AI, avoiding a "custom WebRTC load balancer"): this
    source assumes exactly that transport substrate ("bidirectional
    streaming protocols like gRPC or WebSockets") and extends it with the
    next-layer problem Curley's post doesn't address — once you're routing
    traffic to backends serving many such connections, what signal should
    the load balancer actually use to pick a backend for a *new* session.
  - `blog-vercel-websocket-support-public-beta.md` Claim 2 (a WebSocket
    connection is pinned to one Function instance for its lifetime, with
    Fluid compute letting one instance multiplex many connections) and Claim
    5 (new connections aren't guaranteed to reach the same instance, so
    durable state must live externally): this source's active-session
    tracking and hybrid capacity model is the routing-decision layer that
    determines *which* instance a new connection should be pinned to in the
    first place — Vercel's note documents the pinning mechanism and its
    consequences for state; this source documents how a platform operator
    would decide where to route a new connection before pinning happens.
  - `blog-vercel-ai-gateway-realtime-voice-speech.md` Claim 3 (AI Gateway
    enforces a 25-minute max session duration, 5-minute idle timeout, and an
    unspecified per-team concurrent-realtime-session cap): that source
    documents fixed, gateway-enforced session limits as guardrails; this
    source's active-session-count signal is the raw input a load balancer
    would need to track in order to enforce or approach a concurrent-session
    cap intelligently (i.e., which backend has room for another session)
    rather than as a flat per-team ceiling.

- **Novel**:
  - **The QPS/CPU-utilization blind spot for streaming AI sessions, stated
    as a named, general architectural problem** (Claims 1-4): no prior
    corpus source articulates why request-rate and CPU metrics specifically
    fail for long-lived bidirectional AI streams, as opposed to discussing
    session duration limits (Vercel notes) or transport protocol choice
    (Curley note) as separate concerns.
  - **"Ghost sessions" as a named failure mode for session counters**
    (Claim 6): a new, memorable term for stuck/double-decremented counters
    that mislead a load balancer, not previously named in the corpus.
  - **The "pretend QPS" normalization technique for folding session counts
    into rate-based load-balancing signals** (Claim 9): a concrete,
    reusable integration pattern not documented elsewhere in the corpus.
  - **A named hybrid capacity-estimation formula (Target Utilization,
    Average Utilization, Cost Per Session, Safety Scaler) for session-aware
    routing** (Claim 10): the first corpus source to propose a specific
    (if explicitly "simplified" and non-prescriptive) formula for this
    problem.
  - **JVM-specific concurrency guidance for session-tracking counters**
    (Claim 12: `AtomicInteger` cache-line contention vs. `LongAdder`/sharded
    counters at high concurrency): a new, implementation-level detail not
    present anywhere else in the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the QPS/CPU blind-spot argument
  (Claims 1-4) as the motivating problem statement whenever the guide
  discusses deploying real-time, streaming AI harnesses (voice, video,
  bidirectional agent connections) behind a load balancer — the guide should
  flag that a team reusing a standard request-based load balancer for a
  streaming AI backend will silently mis-route traffic once sessions become
  long-lived, well before that team hits an obvious error or outage. Pair
  this with the concrete Kotlin session-tracking pattern (Claim 5) and the
  "ghost sessions" failure mode (Claim 6) as the minimum-viable fix: track
  active sessions in application code with a guaranteed decrement, and
  explicitly design for the case where timeout/cancel/disconnect fire
  together.

- **Chapter 02 (Harness Engineering) — capacity model**: Add the hybrid
  utilization + session-count model (Claims 8-10) as a design pattern for
  teams that need more than "add a session-tracking counter" — the "pretend
  QPS" normalization (Claim 9) is a low-effort way to fold session pressure
  into an existing QPS-based load balancer without replacing it wholesale.
  Explicitly carry forward the article's own caveat that the specific
  formula is illustrative ("the exact algorithm depends on your proxy and
  workload," per Claim 10) — the guide should present this as a pattern to
  adapt, not a formula to copy verbatim.

- **Chapter 02 (Harness Engineering) — validation checklist**: Add the
  benchmark-dimension checklist (Claim 11) and the tracker-overhead
  validation guidance (Claim 12, including the specific `AtomicInteger` vs.
  `LongAdder`/sharded-counter tradeoff on the JVM) as a concrete pre-launch
  checklist for teams building session-aware routing for real-time AI
  infrastructure, alongside the existing WebSocket/transport guidance from
  `blog-simonwillison-luke-curley-webrtc.md` and
  `blog-vercel-websocket-support-public-beta.md`.

## Extraction Notes

1. **WebFetch output not trusted for quotes; raw HTML fetched and parsed
   directly, per MINER.md §2a.** An initial WebFetch pass on the article URL
   returned an accurate-in-substance but AI-paraphrased summary (sentences
   reworded, some quotes lightly tightened). This note instead retrieved the
   page via direct `curl` with a browser user-agent, stripped HTML markup
   with a Python script, and read the resulting plain text in full. Every
   `Quote` field in this note was located character-for-character in that
   locally-parsed plain text (`/tmp/gblog.txt` during extraction), not the
   WebFetch summary.
2. **The capacity-estimation formula (Claim 10) is an embedded image, not
   extractable text.** Inspecting the raw HTML confirmed the sentence "A
   simplified capacity estimate formula could look like this:" is
   immediately followed by an `<img>` tag
   (`gweb-developer-goog-blog-assets/images/Image_2.original.png`) rather
   than a text or code block containing the equation itself; only the four
   input-variable definitions and two worked numeric scenarios that follow
   the image are extractable as text. This note quotes those definitions and
   scenarios verbatim but does not reconstruct the formula's exact
   mathematical notation, since doing so would not be a verbatim quote per
   MINER.md §2a.
3. **No sub-pages followed.** The article is a single, self-contained post
   with no links to related documentation pages beyond the "Related Posts"
   footer (other Google Developers Blog posts on unrelated topics: Agent
   Skills in Genkit Go, ADK 2.0, modular prompt transpilation, Gemini
   Enterprise Agent Platform evaluations). None of those was substantively
   linked from within the article body itself, so none was followed per
   MINER.md §1.
4. **No contradiction issues filed.** One near-miss (tension with
   `blog-simonwillison-luke-curley-webrtc.md` Claim 8 on WebSocket
   simplicity) was evaluated against MINER.md §4a and judged not to rise to
   a contradiction, since the two claims address different layers of the
   problem (connection-establishment simplicity vs. ongoing capacity-routing
   correctness) rather than opposing assertions about the same fact; see
   Cross-References → Contradicts.
5. **Confidence calibration: emerging.** Every individual claim is rated
   "emerging" rather than "settled": the article is a single first-party
   author's architectural reasoning and design recommendations, illustrated
   with hypothetical examples and worked numeric scenarios rather than
   measured production data. No before/after benchmark, named production
   deployment, or specific product/proxy shipping this exact behavior is
   cited anywhere in the source. The technical substance (the QPS/CPU
   blind-spot argument, the session-tracking pattern, the hybrid capacity
   model) is internally consistent and written by a credible first-party SRE
   author, which is why it is not rated "anecdotal" — but the complete
   absence of measured results anywhere in the article caps the overall
   confidence below "settled."
