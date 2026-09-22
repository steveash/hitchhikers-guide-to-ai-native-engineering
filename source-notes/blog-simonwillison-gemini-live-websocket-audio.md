---
source_url: https://simonwillison.net/2026/Sep/15/gemini-live/
source_type: blog-post
title: "Tool: Gemini Live audio"
author: Simon Willison
date_published: 2026-09-15
date_extracted: 2026-09-22
last_checked: 2026-09-22
status: current
confidence_overall: emerging
issue: "#3605"
---

# Tool: Gemini Live audio

> Simon Willison's link-blog note on Google's Gemini 3.8 Live / Live Extended
> Thinking launch links to a working, library-free browser voice client he
> had an agent build against the official docs — the implementation reveals
> Google's WebSocket-based Live API protocol, a from-scratch PCM resampling
> AudioWorklet, session-resumption/reconnect handling, and a model-specific
> API gotcha (`thinkingConfig` rejected by the non-Extended-Thinking model),
> none of which appear in Willison's four-sentence post itself.

## Source Context

- **Type**: blog-post (link-blog/"beat" format; ~5 sentences plus a
  screenshot; Willison's own preview-access note on a same-day Google model
  launch). The post itself is thin. Per MINER.md §1, five linked pages were
  followed as substantive sub-sources: (1) the actual tool implementation at
  `github.com/simonw/tools/blob/main/gemini-live.html` (full HTML/JS source,
  ~500 lines), (2) the build-transcript gist at
  `gist.github.com/simonw/067b7430c5b1f743af9419b0184c38ef` (the coding
  agent's own session log), (3) Google's official `Get started with Gemini
  Live API using WebSockets` tutorial, (4) Google's official launch post
  `Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking`, and (5)
  OpenAI's `Introducing GPT-Live` announcement, which returned an HTTP 403
  and could not be read (see Extraction Notes).
- **Author credibility**: Simon Willison is the creator of Django and
  Datasette, a prolific open-source practitioner, and the corpus's most
  frequent voice-AI commentator (see Cross-References). This is a hands-on
  practitioner note: Willison built and is hosting the tool himself, not
  reporting on someone else's build.
- **Scope**: Covers the WebSocket transport and Web Audio API client
  architecture for Google's newly-launched Gemini 3.8 Live / Live Extended
  Thinking models, as implemented in a single, dependency-free HTML file,
  plus the agentic build/test/verify workflow used to produce it, plus
  Google's own first-party performance claims for the new models. Does
  **not** cover: independent benchmarking of Gemini 3.8 Live's audio quality
  or latency, production-scale deployment guidance, pricing, or a systematic
  comparison against OpenAI's GPT-Live beyond Willison's one-line framing.

## Extracted Claims

### Claim 1: Google positions Gemini 3.8 Live and 3.8 Live Extended Thinking as occupying the same product category as OpenAI's GPT-Live — both are speech-to-speech models, not a text model bolted to separate ASR/TTS
- **Evidence**: Willison's direct framing in the opening sentence of the post, linking to both the Google announcement and OpenAI's GPT-Live announcement as points of comparison.
- **Confidence**: emerging (a single practitioner's one-line categorical comparison; not a feature-by-feature comparison)
- **Quote**: "Google released Gemini 3.8 Live and 3.8 Live Extended Thinking today - two new speech-to-speech models that are a similar shape to OpenAI's GPT-Live family."
- **Our assessment**: This confirms the corpus's existing observation (`blog-simonwillison-gptlive-voice-delegation.md` Claim 1) that GPT-Live is a distinct, named product category — Willison uses the exact same author's-eye framing to slot Gemini 3.8 Live into that category five weeks later. "Similar shape" is doing real work here: both are dedicated speech-to-speech models (audio in, audio out) rather than a text LLM wrapped in separate transcription/synthesis steps, which is the architectural point, even though Willison does not elaborate further on what "shape" means beyond that.

### Claim 2: Willison built the tool by pointing an agentic coding tool ("GPT-6 Astra Extra High") at Google's documentation and having it build the web UI directly, rather than hand-writing the client himself
- **Evidence**: Willison's first-person account of his own build process.
- **Confidence**: anecdotal (single practitioner, single build)
- **Quote**: "I pointed GPT-6 Astra Extra High at the documentation and had it build me this web UI for trying out the new models."
- **Our assessment**: This is the now-familiar "paste opaque vendor docs into an agent, get a working demo" pattern the corpus already documents for OpenAI's WebRTC API (`blog-simonwillison-openai-webrtc-document-context.md` Claim 8, where Willison pasted an OpenAI code sample into Claude). The pattern generalizes across vendors and protocols: Willison used it for OpenAI's WebRTC Realtime API in 2024 and for Google's WebSocket Live API here in 2026, in both cases treating official docs as a spec for an agent to implement against rather than material he reads and hand-codes from himself.

### Claim 3: The resulting implementation uses no client-side libraries or SDK — it connects directly to Google's WebSocket endpoint and uses the browser's native Web Audio API `AudioContext` for both microphone capture and audio playback
- **Evidence**: Willison's direct description, independently confirmed by reading the full implementation source at `github.com/simonw/tools/blob/main/gemini-live.html`, which contains no `import`/`<script src=...>` dependencies — only a single inline `<script type="module">`.
- **Confidence**: settled (verified directly against the shipped implementation, not just the blog post's claim)
- **Quote**: "The implementation uses no libraries. It connects to the wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContent?key=... WebSocket endpoint and uses a Web Audio API AudioContext for both capture and playback."
- **Our assessment**: This is Google's flagship voice API implemented over a raw WebSocket, not WebRTC — a real, shipping-today instance of exactly the architecture Luke Curley recommends in `blog-simonwillison-luke-curley-webrtc.md` Claim 8 ("if I was working at OpenAI, I'd start by stream[ing] audio over WebSockets"). The library-free implementation also means every protocol detail (setup message shape, audio chunking, reconnection) is visible in application code rather than hidden inside an SDK, which is why this source note can extract as much protocol-level detail as it does.

### Claim 4: The UI supports interrupting the model mid-response either by speaking over it or by sending a typed message, and the implementation immediately stops in-flight audio playback and marks the interrupted turn in the transcript
- **Evidence**: Willison's post states the interruption capability; the implementation code confirms the mechanism — `content.interrupted` from the server triggers `clearAudio(s)` (stopping and disconnecting all queued `AudioBufferSourceNode`s) and `finishMessage('model', true)`, which appends a visible "Interrupted" label to the transcript entry; sending a typed message independently calls the same `clearAudio`/`finishMessage(..., true)` pair before sending.
- **Confidence**: settled (post text plus directly-verified implementation code)
- **Quote**: "including the ability to interrupt the model while it is talking" / (implementation) "Sending a message interrupts the current response. Transcripts may include speech interrupted before playback."
- **Our assessment**: Interruption is handled at two levels — server-signaled (`content.interrupted`, presumably from voice-activity detection on Google's side) and client-initiated (typed message pre-empting an in-progress spoken response) — and both funnel through the same `clearAudio`/`finishMessage(role, true)` cleanup path. The UI hint text explicitly warns that transcripts "may include speech interrupted before playback," i.e., the model can generate more audio than the user actually hears, which is a concrete UX detail for anyone building a transcript view on top of a live audio API.

### Claim 5: Microphone audio is resampled to exactly 16kHz inside a custom `AudioWorkletProcessor` that tracks fractional sample position across render quanta (so it works correctly against any input sample rate, including 44.1kHz mics), batching output into 640-sample (40ms) 16-bit PCM chunks
- **Evidence**: The full `PCMRecorder` `AudioWorkletProcessor` source, including its own explanatory comment.
- **Confidence**: settled (directly falsifiable code artifact)
- **Quote**: (code comment, verbatim from `gemini-live.html`) "Average samples over exact 16 kHz intervals, preserving fractional position between render quanta (including 44.1 kHz microphones). Output 40 ms chunks."
- **Our assessment**: This is a specific, reusable resampling technique for any browser client that must produce a fixed sample rate (here 16kHz, matching the Live API's required input format — see Claim 6) from a `MediaStream` whose native rate is whatever the OS/hardware reports (commonly 44.1kHz or 48kHz). The worklet accumulates a running `remaining`/`sum` fractional-position state across `process()` calls rather than naively decimating every Nth sample, which avoids the periodic timing drift a simpler nearest-neighbor downsample would introduce over a long session.

### Claim 6: Google's official Live API requires audio to be sent as raw 16-bit PCM at 16kHz, little-endian, base64-encoded inside a `realtimeInput.audio` message with an explicit `mimeType` field
- **Evidence**: Google's official WebSocket get-started tutorial, "Send audio" section, plus matching runnable Python and JavaScript code samples.
- **Confidence**: settled (official first-party API documentation, and independently confirmed by matching `mimeType: 'audio/pcm;rate=16000'` in Willison's implementation code)
- **Quote**: "Audio needs to be sent as raw PCM data (raw 16-bit PCM audio, 16kHz, little-endian). Construct a BidiGenerateContentRealtimeInput message with the audio data. The mimeType is crucial."
- **Our assessment**: This is the concrete input-format contract Claim 5's resampling worklet exists to satisfy. The tutorial's own code samples send raw microphone/file bytes without demonstrating a resampling step at all — a gap the implementation fills, and a gap any practitioner following only the official quickstart would hit as soon as their input device wasn't already natively 16kHz.

### Claim 7: The implementation schedules received audio playback using the `AudioContext`'s own clock (`audio.currentTime`), chaining each decoded buffer to start exactly when the previous one ends, rather than using JavaScript timers to pace playback
- **Evidence**: Direct code inspection of `playAudio()`, including its own explanatory comment.
- **Confidence**: settled (directly falsifiable code artifact)
- **Quote**: (code comment, verbatim) "Schedule contiguous chunks on the audio clock, not with JS timers."
- **Our assessment**: `setTimeout`/`setInterval`-based audio pacing is a well-known source of audible clicks and gaps because JS timer callbacks are not sample-accurate; scheduling `AudioBufferSourceNode.start()` calls against the audio hardware's own clock (`s.nextAudioTime = Math.max(s.nextAudioTime, s.audio.currentTime + .03); ... source.start(s.nextAudioTime); s.nextAudioTime += buffer.duration;`) keeps streamed TTS-style chunks glitch-free regardless of how bursty their arrival over the WebSocket is. This is a reusable pattern for any browser client streaming synthesized audio in small chunks, independent of which vendor's API is producing the audio.

### Claim 8: The client implements Google's Live API session-resumption mechanism — it captures a resumable session handle from server `sessionResumptionUpdate` messages, and on receiving a server-initiated `goAway` pre-disconnect warning, automatically reconnects using that handle once no audio is playing and no response is in progress (capped at 3 reconnect attempts)
- **Evidence**: Direct code inspection of `receive()`, `reconnect()`, and the polling check `if (s.goAway && s.resumeHandle && s.interaction !== 'IN_PROGRESS' && !s.sources.size) reconnect(s);`, run both immediately on `goAway` receipt and once per second from a session timer.
- **Confidence**: settled (directly falsifiable code artifact; the mechanism's existence — `sessionResumptionUpdate`, `goAway` — is a server-driven protocol feature, not something the client invented)
- **Quote**: (code, `receive()`) "Google is refreshing this connection. The session will resume when a saved state is available." / (code comment) "The Thinking guide shows status at both envelope and serverContent levels."
- **Our assessment**: This is a distinct connection-resilience pattern from anything the corpus's existing WebRTC voice note documents: rather than a client-initiated reconnect-on-drop, Google's server proactively warns the client (`goAway`, with an optional `timeLeft` hint) before forcibly closing the connection, and expects the client to reconnect using a previously-issued resumable handle. The client deliberately waits for a "safe" moment (no audio currently playing, no response in progress) before reconnecting, rather than reconnecting the instant the warning arrives — avoiding an audible interruption mid-utterance for a refresh the server scheduled, not the user.

### Claim 9: Sending a `thinkingConfig` parameter — even at a minimal level — to the standard Gemini 3.8 Live model causes the API to reject the request; only the separate `gemini-3.8-live-extended-thinking` model variant accepts it
- **Evidence**: A defensive code comment directly above the conditional that only sets `generationConfig.thinkingConfig` when `s.extended` is true.
- **Confidence**: anecdotal (a single code comment recording what reads as the builder's own empirical finding while implementing against the two model variants; not corroborated by an explicit statement in either Google doc read for this note)
- **Quote**: (code comment, verbatim) "Standard 3.8 Live rejects thinkingConfig, even a minimal level."
- **Our assessment**: This reads as a first-hand API gotcha discovered during implementation rather than something copied from documentation — Google ships two separate model IDs (`gemini-3.8-live` and `gemini-3.8-live-extended-thinking`) with an overlapping request schema that is not accepted identically by both; sending a thinking-related field to the non-thinking model is a hard error, not a silently-ignored no-op. Practitioners building against both model variants from shared request-construction code need to branch on model choice for this field specifically, not just for output behavior.

### Claim 10: Extended Thinking's ability to "speak while it continues reasoning in the background" is a first-party design goal, not just an implementation detail — Google's launch post frames it as acknowledging prompts with verbal filler ("Let me check that…") while narrating multi-step background progress live
- **Evidence**: Google's official launch blog post, "Experience more fluid, intelligent conversations" section.
- **Confidence**: settled (first-party vendor description of shipped model behavior, corroborated by the implementation's separate `interactionStatus` (`IDLE`/`IN_PROGRESS`) tracking used to show "Gemini thinking" as a distinct UI state from "Gemini speaking")
- **Quote**: "For tasks that require deeper reasoning, 3.8 Live Extended Thinking reasons and speaks simultaneously. It delivers increased intelligence for complex workflows while maintaining an uninterrupted conversational flow — using early verbal cues like "Let me check that…" to acknowledge prompts naturally, and live progress narration to walk users through multi-step background tasks as they progress."
- **Our assessment**: This is the same "keep talking while a slower process runs in the background" design goal the corpus already documents for OpenAI's GPT-Live delegation architecture (`blog-simonwillison-gptlive-voice-delegation.md` Claim 1), but implemented differently: GPT-Live delegates to a separate background *model* (GPT-5.5) and merges its result back into the live conversational model's output, whereas Gemini 3.8 Live Extended Thinking appears to be a single model that reasons and speaks concurrently within itself, using verbal filler and live narration rather than a silent handoff. Both vendors converged on the same UX problem (don't go silent while doing slow work in a live voice session) with architecturally distinct solutions.

### Claim 11: Google's own first-party benchmark claims for Gemini 3.8 Live Extended Thinking include the #1 overall spot on Artificial Analysis' Speech to Speech Quality Index (82.6), 68.6% on τ-Voice, 35.1% on Sierra's τ-Voice-banking benchmark, and 97.7% on Big Bench Audio
- **Evidence**: Google's official launch blog post.
- **Confidence**: emerging (first-party vendor-reported benchmark scores; no independent reproduction or third-party confirmation was located during this extraction)
- **Quote**: "Gemini 3.8 Live Extended Thinking provides enterprise-grade task completion and intelligence, capturing the #1 overall spot on Artificial Analysis' Speech to Speech Quality Index (82.6), and leads in agentic task completion with 68.6% on τ-Voice and 35.1% on Sierra's τ-Voice-banking benchmark. It also provides strong reasoning capabilities, scoring 97.7% on Big Bench Audio, while maintaining a highly competitive price point compared to other frontier models."
- **Our assessment**: These are the first appearances of the τ-Voice, Sierra τ-Voice-banking, and Big Bench Audio benchmark names in this corpus. They are self-reported at launch, from the vendor whose model is being scored, with no methodology detail in the announcement itself (only the Artificial Analysis leaderboard is externally linked). Treat as directional signal that Google is explicitly targeting agentic voice-task benchmarks, not as a verified capability claim.

### Claim 12: The build process for this tool (per the linked build-transcript gist) included an 11-test pytest suite exercising a simulated Gemini connection, Playwright screenshots at both desktop and mobile viewport sizes, and a raw Node.js `vm.Script` syntax check of the extracted JS module — all run before the agent reported the tool complete
- **Evidence**: The agent's own session transcript, published by Willison as a gist alongside the tool.
- **Confidence**: settled (a first-hand transcript of the actual build session, not a secondhand description)
- **Quote**: (gist transcript) "All 11 tests passed using a simulated Gemini connection and real browser audio processing. I'm checking the final page layout and opening a local preview. A live conversation still needs your Gemini API key."
- **Our assessment**: This is a concrete instance of the self-verification pattern already well-represented elsewhere in this corpus (agent writes tests, runs them, takes screenshots, checks syntax, before declaring a UI build done) — see the widespread `playwright`-tagged notes already in `source-notes/`. What is specific to this source is the combination for a *live audio* client: since a real Live API conversation requires a user-supplied API key the agent doesn't have, the agent substituted a simulated Gemini connection for the pytest suite and relied on static syntax checking plus static screenshots (not live audio playback) to gain confidence before handing the tool back to Willison for the one thing it could not self-verify — an actual voice exchange with a real key.

### Claim 13: The client sends the raw Gemini API key directly from the browser to Google as a WebSocket query parameter with no server-side proxy or ephemeral-token exchange step; the key can optionally be persisted in `localStorage`, and event-log output redacts the key by string substitution before it is ever rendered to the page
- **Evidence**: Direct code inspection — `new WebSocket(\`${ENDPOINT}?key=${encodeURIComponent(s.key)}\`)`, the `remember-key` checkbox gated `localStorage` persistence, and the `log()`/`fail()` functions' `String(text).split(session.key).join('[redacted]')` redaction before appending to the visible `#events` panel.
- **Confidence**: settled (directly falsifiable code artifact)
- **Quote**: (implementation UI hint, verbatim) "Audio and text go directly to Google. Get an API key." / (code comment) "Deliberately log summaries, never credentials, session handles or PCM payloads."
- **Our assessment**: This is architecturally the opposite security model from the ephemeral-token pattern the corpus already documents for OpenAI's Realtime WebRTC API (`blog-simonwillison-openai-webrtc-document-context.md` Claim 2: a 60-second server-minted token, no long-lived key ever reaching the browser). Here the long-lived Gemini API key itself is typed directly into the page and sent over the wire on every session; the only mitigations are UI-level (password-masked input field, opt-in-only persistence, log redaction) rather than protocol-level. This is consistent with that OpenAI note's existing guidance that a direct-API-key browser demo is "appropriate only for personal/controlled use" — this Gemini tool is exactly that kind of personal-use demo, and neither Willison's post nor the implementation claims otherwise. It is a concrete negative example for a guide security section: log redaction and optional persistence reduce *some* exposure, but they do not substitute for not putting a long-lived credential in the browser at all.

## Concrete Artifacts

### WebSocket setup message construction (verbatim from `gemini-live.html`)
```javascript
function setupMessage(s, handle) {
  const generationConfig = {
    responseModalities: ['AUDIO'],
    speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: s.voice } } }
  };
  // Standard 3.8 Live rejects thinkingConfig, even a minimal level.
  if (s.extended) generationConfig.thinkingConfig = { thinkingLevel: s.thinkingLevel };
  const setup = {
    model: `models/${s.model}`, generationConfig,
    inputAudioTranscription: {}, outputAudioTranscription: {},
    contextWindowCompression: { slidingWindow: {} },
    sessionResumption: handle ? { handle } : {}
  };
  if (s.instructions) setup.systemInstruction = { parts: [{ text: s.instructions }] };
  // Proactive audio is always enabled for these models. Affective dialog is removed.
  return { setup };
}
```
Source: `github.com/simonw/tools/blob/main/gemini-live.html`, lines 286-302.

### PCM microphone resampling AudioWorklet (verbatim from `gemini-live.html`)
```javascript
// Average samples over exact 16 kHz intervals, preserving fractional position
// between render quanta (including 44.1 kHz microphones). Output 40 ms chunks.
class PCMRecorder extends AudioWorkletProcessor {
  constructor() {
    super(); this.ratio = sampleRate / 16000; this.remaining = this.ratio;
    this.sum = 0; this.index = 0; this.energy = 0; this.buffer = new ArrayBuffer(1280);
    this.view = new DataView(this.buffer);
  }
  process(inputs) {
    const input = inputs[0]?.[0];
    if (!input) return true;
    for (const sample of input) {
      let available = 1;
      while (available > 1e-8) {
        const weight = Math.min(available, this.remaining);
        this.sum += sample * weight; this.remaining -= weight; available -= weight;
        if (this.remaining < 1e-8) {
          const value = Math.max(-1, Math.min(1, this.sum / this.ratio));
          this.view.setInt16(this.index * 2, Math.round(value * (value < 0 ? 32768 : 32767)), true);
          this.energy += value * value; this.index++;
          this.remaining = this.ratio; this.sum = 0;
          if (this.index === 640) {
            this.port.postMessage({ pcm: this.buffer, level: Math.sqrt(this.energy / 640) }, [this.buffer]);
            this.buffer = new ArrayBuffer(1280); this.view = new DataView(this.buffer);
            this.index = 0; this.energy = 0;
          }
        }
      }
    }
    return true;
  }
}
```
Source: `github.com/simonw/tools/blob/main/gemini-live.html`, lines 250-284.

### Session-resumption / goAway reconnect handling (verbatim from `gemini-live.html`)
```javascript
if (message.goAway) {
  s.goAway = true;
  notice('Google is refreshing this connection. The session will resume when a saved state is available.');
  log(`Connection refresh requested (${message.goAway.timeLeft || 'soon'})`);
}
if (s.goAway && s.resumeHandle && s.interaction !== 'IN_PROGRESS' && !s.sources.size) reconnect(s);
```
Source: `github.com/simonw/tools/blob/main/gemini-live.html`, lines 348-353.

### Official Live API input-format requirement (from Google's own tutorial)
```
Endpoint (generic quickstart, v1beta):
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=YOUR_API_KEY

Audio format requirement:
"Audio needs to be sent as raw PCM data (raw 16-bit PCM audio, 16kHz, little-endian)."

mimeType used in realtimeInput.audio: "audio/pcm;rate=16000"
```
Source: `ai.google.dev/gemini-api/docs/live-api/get-started-websocket`, "Authentication" and "Send audio" sections, page last-updated 2026-09-15 UTC per its own footer.

### Build verification transcript excerpt (from Willison's linked gist)
```
Wrote ~/dev/tools/tests/test_gemini_live.py (+236 -0)
Ran uv run pytest tests/test_gemini_live.py -q
[... iterative edits and reruns ...]
Ran a Playwright script: launch Chromium, screenshot at 1200x1100 (desktop),
then resize to 390x844 and select the Extended Thinking model, screenshot again (mobile).
Ran a Node.js syntax check: extract the <script type="module"> block from the HTML
and pass it to `new vm.Script(source)` to confirm it parses.

"All 11 tests passed using a simulated Gemini connection and real browser audio
processing. I'm checking the final page layout and opening a local preview.
A live conversation still needs your Gemini API key."
```
Source: `gist.github.com/simonw/067b7430c5b1f743af9419b0184c38ef`, agent build-session transcript.

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-gptlive-voice-delegation.md` Claim 1 — Willison's own comparison (Claim 1 here) independently confirms that GPT-Live occupies a distinct, named "speech-to-speech model" product category, since he uses the same framing to place Gemini 3.8 Live in the same category five weeks after documenting GPT-Live.
  - `blog-simonwillison-luke-curley-webrtc.md` Claim 8 — Curley's recommendation that LLM voice AI should be built on WebSockets rather than WebRTC ("if I was working at OpenAI, I'd start by stream[ing] audio over WebSockets") is directly corroborated by this source: Google's flagship Live API, released the same week this note was mined, is a WebSocket protocol (Claim 3 here), not WebRTC.
  - `blog-google-adk-live-voice-agent-evaluation.md` Claim 3 — that note's three-agent ADK `Workflow` runs on `gemini-live-2.5-flash-native-audio` and documents the *evaluation* layer for Gemini Live agents; this source documents the *raw protocol* layer immediately beneath whatever ADK's live-agent runtime does internally, for the newer 3.8 model generation. Neither note describes the other's layer.

- **Contradicts**: None filed as a formal contradiction. One internal Google documentation inconsistency was found during extraction (Claim 9's endpoint note): the generic WebSocket quickstart tutorial's own code samples target the `v1beta` endpoint (see Concrete Artifacts), while Willison's implementation deliberately targets `v1alpha`, with a code comment stating "The Thinking guide specifies v1alpha for both 3.8 models." This is a narrow API-version detail across two Google-authored pages, not a guide-relevant claim about practice or architecture that two sources take opposing sides on, so it does not meet MINER.md §4a's bar for a contradiction issue — it is recorded here and in Extraction Notes as a practitioner gotcha instead.

- **Extends**:
  - `blog-simonwillison-openai-webrtc-document-context.md` — that note documents OpenAI's WebRTC voice architecture including its ephemeral-token security model (Claim 2) and client-side document-context injection (Claim 4). This source is the Google-side counterpart at the transport level (WebSocket vs. WebRTC) and reveals a materially weaker security posture for the equivalent browser-demo use case (Claim 13 here: direct long-lived API key over the wire, vs. that note's 60-second ephemeral token). Together the two sources give the guide concrete opposite-ends-of-the-spectrum examples of browser voice-AI key handling.
  - `blog-google-adk-live-voice-agent-evaluation.md` — extends the corpus's Gemini Live coverage from the evaluation/testing layer down to the wire protocol and client-implementation layer, for a newer model generation (3.8 vs. 2.5) than that note covers.
  - `blog-simonwillison-luke-curley-webrtc.md` — extends Curley's transport-protocol argument from a theoretical/critique framing into a concrete, currently-shipping example of a major vendor's flagship voice API implemented exactly as WebSockets-first.

- **Novel**:
  - **Fractional-position AudioWorklet PCM resampling technique** (Claim 5): not documented anywhere else in this corpus. A reusable pattern for any browser client that must produce a fixed sample rate from an arbitrary-rate `MediaStream`.
  - **`AudioContext`-clock playback scheduling for streamed TTS-style audio** (Claim 7): a specific glitch-avoidance technique not previously captured in the corpus's audio/voice notes.
  - **Server-initiated `goAway` + resumable-handle reconnect flow** (Claim 8): a connection-resilience pattern distinct from the corpus's existing coverage of client-initiated retry logic or OpenAI's ephemeral-token session timing.
  - **Model-variant-specific request-schema rejection** (Claim 9: `thinkingConfig` accepted by one model ID, rejected by a sibling model ID with an otherwise-shared schema) — a specific multi-model-variant API gotcha not previously documented in the corpus.
  - **Two independent vendor solutions to "keep talking while slow background work happens" in a live voice session** (Claim 10): GPT-Live's background-model delegation vs. Gemini 3.8 Live Extended Thinking's single-model concurrent reason-and-speak — the corpus now has both named architectural answers to the same UX problem, from competing vendors, in the same season.
  - **First-party agentic build-verification transcript for a live-audio browser tool specifically** (Claim 12): the corpus already has playwright-based UI self-verification examples, but none previously involving a simulated real-time audio/WebSocket connection as the substitute for a credential-gated live test.

## Guide Impact

- **Voice AI System Design (currently accumulating under Chapter 03, per prior notes' Guide Impact sections)**: Add this source as the Google/WebSocket counterpart to the existing OpenAI/WebRTC coverage, explicitly citing it as real-world confirmation of Curley's WebSockets-first recommendation (`blog-simonwillison-luke-curley-webrtc.md` Claim 8) now that a major vendor's flagship live-voice API ships that way. Cite Claim 3.
- **Chapter 02 (Harness Engineering) — browser audio capture/playback patterns**: Add the AudioWorklet fractional resampling technique (Claim 5, with the Concrete Artifacts code block) and the `AudioContext`-clock playback scheduling technique (Claim 7) as vendor-agnostic, reusable patterns for any team building a browser client that streams audio to or from an LLM API — neither pattern is specific to Gemini's protocol.
- **Chapter 02 (Harness Engineering) — session resilience**: Add the server-initiated `goAway` + resumable-handle reconnect pattern (Claim 8) as a concrete example of designing a client to defer reconnection until a "safe" moment (no in-flight audio, no response in progress) rather than reconnecting immediately on a server-scheduled refresh notice.
- **Chapter 06 (Security & Threat Model) — browser-based voice AI credential handling**: Add Claim 13 as a named negative example: a direct, long-lived API key sent from the browser on every session, mitigated only by UI-level controls (password field, opt-in persistence, log redaction), explicitly contrasted with the ephemeral-token pattern already documented from OpenAI's Realtime API (`blog-simonwillison-openai-webrtc-document-context.md` Claim 2). The guide should state plainly that log redaction and optional persistence are not a substitute for not shipping a long-lived credential to the browser, and that this specific tool is a personal-use demo, not a deployment template.
- **Chapter 01 (Daily Workflows) / Chapter 03 (Verification) — agent self-verification when a credential is unavailable to the agent**: Cite Claim 12 as a specific instance of an agent substituting a simulated connection plus static checks (syntax parse, Playwright screenshots at multiple viewports) for the one thing it structurally cannot verify itself (an actual authenticated live session) — a reusable pattern for any agent building against a credential-gated API it doesn't hold the credential for.
- No change recommended to Chapter 00 (Principles), Chapter 04 (Context Engineering), or Chapter 05 (Team Adoption) — this source's content (voice-AI protocol/client implementation, one vendor benchmark claim, one build-verification transcript) does not bear on those chapters as currently framed.

## Extraction Notes

- **Primary post is thin; five linked pages were read in full**: Willison's own post is a ~5-sentence "beat"/link-blog entry. Per MINER.md §1, the following were fetched and read in full: the tool's actual implementation source (`github.com/simonw/tools/blob/main/gemini-live.html`, ~500 lines, read completely), the linked build-transcript gist, Google's official WebSocket get-started tutorial, and Google's official launch blog post. A fifth linked page, OpenAI's `Introducing GPT-Live` announcement (`openai.com/index/introducing-gpt-live/`), returned an HTTP 403 and could not be read; Claim 1's comparison to GPT-Live relies on Willison's own framing plus the corpus's existing `blog-simonwillison-gptlive-voice-delegation.md` note (which independently documents that OpenAI's announcement page was also unreachable via `curl` when that note was mined, returning a Cloudflare challenge instead — consistent with OpenAI's announcement page being generally difficult to fetch programmatically).
- **All quotes verified against raw `curl` output, not WebFetch summaries**: Every `Quote` field above was matched character-for-character against raw HTML fetched via `curl` (for the Willison post, the Google tutorial, and the Google announcement) or against the literal file contents (for the implementation source and the gist), consistent with this corpus's established practice of avoiding WebFetch's paraphrasing summarizer for verbatim quoting (see Extraction Notes in `blog-simonwillison-gptlive-voice-delegation.md` and `blog-google-adk-live-voice-agent-evaluation.md` for the same caveat about WebFetch on this corpus's other sources).
- **v1alpha/v1beta discrepancy not filed as a contradiction**: See Cross-References → Contradicts above for the reasoning. This is recorded as a practitioner-facing detail (use `v1alpha` if targeting either 3.8 Live model, per the implementation's own comment, rather than the `v1beta` endpoint shown in Google's generic quickstart) rather than a CONTRADICTIONS.md-worthy disagreement about guide advice.
- **Screenshot alt text used as a quotable artifact**: The UI description embedded in the post's `<img alt="...">` attribute is verbatim page-source text (not image recognition) and was used to corroborate Claim 4's interruption-handling description (the alt text shows an "Interrupted" label and "Sending a message interrupts the current response" hint matching the implementation code), consistent with how `blog-simonwillison-openai-webrtc-document-context.md` treats screenshot alt text as a citable direct quote.
- **Cross-reference verification**: `blog-simonwillison-gptlive-voice-delegation.md`, `blog-simonwillison-luke-curley-webrtc.md`, `blog-google-adk-live-voice-agent-evaluation.md`, and `blog-simonwillison-openai-webrtc-document-context.md` were all read in full before writing Cross-References. All claim numbers cited (gptlive-voice-delegation Claim 1; luke-curley-webrtc Claim 8; google-adk-live-voice-agent-evaluation Claim 3; openai-webrtc-document-context Claims 2, 4, 8) were verified against each note's numbered `### Claim N:` headings in document order.
- **Overall confidence graded "emerging"**: The implementation-level artifacts (Claims 3, 4, 5, 6, 7, 8, 9, 13) are directly falsifiable, verified code and are effectively settled. The vendor benchmark claims (Claim 11) are self-reported and ungraded by any third party located during this extraction. The overall grade sits at "emerging" — one notch below "settled" — because the source's most novel and guide-relevant content (the protocol/client patterns) is a single practitioner's implementation against a same-day model launch, not yet corroborated by an independent second implementation or a production deployment report.
