---
source_url: https://simonwillison.net/2026/Jun/12/openai-webrtc/
source_type: blog-post
title: "OpenAI WebRTC Audio Session, now with document context"
author: Simon Willison
date_published: 2026-06-12
date_extracted: 2026-06-20
last_checked: 2026-06-20
status: current
confidence_overall: anecdotal
issue: "#1233"
---

# OpenAI WebRTC Audio Session, now with document context

> Simon Willison's June 2026 update to his WebRTC audio playground demonstrates two
> practitioner patterns for the guide: (1) client-side document context injection as a
> mechanism for grounding real-time voice conversations, and (2) the ephemeral token
> security model required for browser-based voice AI deployments — set against the debut
> of GPT-Realtime-2, OpenAI's first "GPT-5-class" voice model.

## Source Context

- **Type**: blog-post (link-blog format; ~4 sentences; Willison updating his own December
  2024 tool to support GPT-Realtime-2 and document context). The post links to two
  substantive sub-pages that were read per MINER.md §1: the original December 2024 tool
  post (`simonwillison.net/2024/Dec/17/openai-webrtc/`) and the OpenAI GPT-Realtime-2
  API documentation (`developers.openai.com/api/docs/models/gpt-realtime-2`).
- **Author credibility**: Simon Willison is the creator of Django and Datasette, a
  prolific open-source practitioner, and a curated high-signal commentator on LLM tooling
  in this corpus. His link-blog posts are first-person observation, not vendor marketing.
  He built the original tool in December 2024 and maintained it through this June 2026
  update — this is a practitioner keeping hands-on contact with a live API, not a
  one-time evaluation.
- **Scope**: Covers the June 2026 update to his WebRTC playground at
  `tools.simonwillison.net/openai-webrtc`, specifically: (1) adding GPT-Realtime-2 model
  selection, (2) adding a client-side document context textarea. Does NOT cover:
  transcription accuracy, latency measurements, cost analysis for production use, or any
  evaluation methodology. The source is thin (~4 sentences + screenshot) but the December
  2024 sub-page and OpenAI API docs provide concrete technical artifacts.

## Extracted Claims

### Claim 1: OpenAI's Realtime API accepts WebRTC connections via browser-native SDP offer/answer — the full client-side audio session setup fits in ~10 lines of JavaScript

- **Evidence**: Verbatim JavaScript code example tweeted by OpenAI in December 2024 and
  embedded in Willison's original tool post. Willison successfully used this code to build
  a working demo. The code is OpenAI's own recommended pattern.
- **Confidence**: settled (standard WebRTC SDP negotiation; OpenAI's official code example;
  confirmed working by Willison's demo)
- **Quote**: (see Concrete Artifacts — the full code block is the artifact; no prose
  quote captures the pattern adequately)
- **Our assessment**: The brevity of the client-side code is deceptive — the complexity
  lives in server-side token management (see Claim 2), not in the WebRTC connection itself.
  The `RTCPeerConnection` → `createOffer` → POST to `api.openai.com/v1/realtime` →
  `setRemoteDescription` sequence is the complete audio channel. Practitioners who have
  worked with WebRTC for conferencing will find this familiar; those who haven't will find
  it surprisingly concise. The server-side ephemeral token call is the piece that doesn't
  appear in this client code.

### Claim 2: Ephemeral tokens solve the API key exposure problem for browser-based voice AI — a server-side call requests a 60-second connection token; the established session then lasts up to 30 minutes

- **Evidence**: December 2024 post explains the security architecture explicitly, including
  the problem it solves (having to build a full server-side WebSocket proxy) and the
  concrete time bounds on the ephemeral token (60 seconds to initiate) and session
  (30-minute lifetime). This is OpenAI's own described architecture.
- **Confidence**: settled (first-party explanation from a practitioner who implemented
  it; the time bounds are specific and verifiable from OpenAI docs)
- **Quote**: "Ephemeral tokens solve that by letting you make a server-side call to
  request an ephemeral token which will only allow a connection to be initiated to their
  WebRTC endpoint for the next 60 seconds. The user's browser then starts the connection,
  which will last for up to 30 minutes."
  *(Simon Willison, simonwillison.net/2024/Dec/17/openai-webrtc/)*
- **Our assessment**: Before ephemeral tokens, exposing a voice AI to browser users
  required a full server-side WebSocket proxy just to hide the API key — Willison
  explicitly describes this as the pre-ephemeral-token "only secure way." Ephemeral tokens
  collapse that requirement: one thin server endpoint mints the token, the browser handles
  the rest. The 60-second/30-minute split is architecturally significant: the server
  doesn't need to stay involved once the session starts, but the initiation window is
  narrow enough that tokens can't be stockpiled. For practitioners building demos: the
  direct-API-key path (Willison's demo) is appropriate only for personal/controlled use.
  Any public-facing deployment needs the ephemeral token server call.

### Claim 3: GPT-Realtime-2 is OpenAI's first voice model described as "GPT-5-class reasoning," released May 2026, with a September 30, 2024 knowledge cutoff — approximately 8 months before its release

- **Evidence**: OpenAI's promotional description quoted by Willison, confirmed by
  OpenAI's own API documentation (128K context window, 32K max output, Sep 30 2024
  knowledge cutoff, reasoning token support).
- **Confidence**: settled (OpenAI's own documentation; Willison confirms the Sep 30 2024
  cutoff in his post)
- **Quote**: "Last month OpenAI introduced a brand new model to that API called
  GPT‑Realtime‑2, which they promoted as 'our first voice model with GPT‑5‑class
  reasoning' - with a Sep 30, 2024 knowledge cut-off."
  *(Simon Willison, simonwillison.net/2026/Jun/12/openai-webrtc/)*
- **Our assessment**: The "GPT-5-class reasoning" + September 2024 knowledge cutoff
  pairing is notable. Practitioners asking GPT-Realtime-2 about events from 2025 onwards
  will hit a hard wall, despite the model's capability tier. This extends the
  voice-mode-weaker pattern (`blog-simonwillison-voice-mode-weaker.md`): even when voice
  models receive capability upgrades, their knowledge currency may still lag. The Sep 30
  2024 cutoff is more recent than GPT-4o's April 2024 cutoff (cited in the voice-mode
  note) but still leaves voice AI 8+ months behind the model's own release date.

### Claim 4: Client-side document context injection — pasting text into a pre-session textarea — is a working mechanism for grounding real-time voice conversations on arbitrary content

- **Evidence**: Working tool with screenshot showing an active session. The screenshot
  alt text (verbatim from the page HTML) shows: (a) the collapsible "Document context"
  UI element, (b) a DuckDB-related document pasted into the textarea, and (c) a live
  "Last transcript" panel showing the model reasoning about that document's content.
- **Confidence**: anecdotal (one practitioner's working demo; single test case; not a
  controlled evaluation of context fidelity or document size limits)
- **Quote**: "you can also paste in a big chunk of document context so you can have as
  audio conversation in your browser about whatever information you think would be useful
  to explore in a conversational way."
  *(Simon Willison, simonwillison.net/2026/Jun/12/openai-webrtc/)*
- **Our assessment**: The mechanism is architecturally simple: text is injected into the
  session context before the WebRTC connection starts; the model treats it as grounding
  material during the audio conversation. What the source does not reveal is where in the
  API this context is passed — whether as a system message, a user turn, or a dedicated
  context parameter. The screenshot confirms the model actively uses the pasted content
  (the DuckDB transcript excerpt reasons about SQL safety from the pasted document).
  For practitioners: this pattern enables the "talk to your documentation" use case
  without any server-side retrieval infrastructure. The constraint is browser context
  window size and any limits the Realtime API places on pre-session text injection.

### Claim 5: GPT-Realtime-2 supports configurable reasoning effort for speech-to-speech interactions, with audio tokens priced at approximately 8× text token rates

- **Evidence**: OpenAI's API documentation explicitly states reasoning effort support and
  the latency/cost tradeoff. Pricing is from the official model docs: text input $4/M,
  audio input $32/M; text output $24/M, audio output $64/M.
- **Confidence**: settled (OpenAI official documentation)
- **Quote**: "GPT-Realtime-2 is our most capable realtime voice model. It supports
  speech-to-speech interactions with configurable reasoning effort, stronger instruction
  following, and more reliable tool use for complex voice-agent workflows."
  *(OpenAI API docs, developers.openai.com/api/docs/models/gpt-realtime-2)*
- **Our assessment**: Configurable reasoning effort in a voice model is significant for
  harness design: practitioners can tune the latency/quality tradeoff based on use case.
  A low-reasoning-effort setting suits conversational chitchat; a high-reasoning-effort
  setting suits document analysis or complex voice agents (at the cost of increased
  first-audio latency and output token spend). The 8× audio pricing premium ($32 vs. $4
  per M input tokens) means audio conversations are materially more expensive than text
  API calls for equivalent content — practitioners designing voice-augmented harnesses
  should model audio cost separately from text cost. See `blog-thebatch-ng-ai-andrew-
  agentic-harness.md` for corroboration on the five-level reasoning-effort tradeoff.

### Claim 6: GPT-Realtime-2 supports function calling but not streaming responses in the standard completions sense — it uses speech-to-speech (audio in, audio out) through the `/v1/realtime` endpoint

- **Evidence**: OpenAI API docs feature table: "Streaming: Not supported / Function
  calling: Supported" — alongside the modality spec: Text (input/output), Image (input
  only), Audio (input/output).
- **Confidence**: settled (OpenAI official API documentation)
- **Quote**: (no single prose quote; see Concrete Artifacts for the feature matrix)
- **Our assessment**: The "Streaming: Not supported" line is a potential source of
  confusion — it means SSE-style token streaming is not available, not that the audio
  output isn't streamed. The Realtime API is inherently streaming audio; what practitioners
  lose is the text-layer streaming pattern that text-chat harnesses commonly use. Function
  calling support is important for voice agent workflows — it enables GPT-Realtime-2 to
  take actions (search, fetch, submit forms) during a voice conversation, not just respond
  verbally.

### Claim 7: Voice model deployment in consumer apps lags API availability by weeks to months — GPT-Realtime-2 was in API production by early May 2026 but had not appeared in the ChatGPT iPhone app as of June 12, 2026

- **Evidence**: Willison's explicit statement that he waited for the model to appear in
  the iPhone app and, when it didn't, turned to the API instead.
- **Confidence**: anecdotal (one practitioner's observation; not a systematic deployment
  lag study)
- **Quote**: "I've been waiting for that model to show up in the ChatGPT iPhone app but
  it still hasn't, so I revisited my old playground."
  *(Simon Willison, simonwillison.net/2026/Jun/12/openai-webrtc/)*
- **Our assessment**: This extends the pattern documented in
  `blog-simonwillison-voice-mode-weaker.md` — that voice interfaces run on different (and
  generally older) model tiers than text interfaces. Here the stratification is temporal
  and channel-specific: the same model is available via API before it is available in the
  consumer product. Practitioners who need the latest voice model capabilities should
  target the API directly rather than waiting for consumer app deployment. This also
  implies that API users of voice AI have access to capabilities that consumer users
  cannot yet reach — a reversal of the usual assumption that consumer apps trail API
  capabilities only in stability and polish, not in capability tier.

### Claim 8: A working browser-based WebRTC voice demo can be assembled from an opaque vendor API code example by feeding it to Claude for UI scaffolding

- **Evidence**: December 2024 post describes the exact workflow: OpenAI tweeted "this
  opaque code example" for the new WebRTC API; Willison pasted it into Claude and had it
  build an interactive demo.
- **Confidence**: anecdotal (one practitioner, one demo)
- **Quote**: "So I pasted that into Claude and had it build me this interactive demo for
  trying out the new API."
  *(Simon Willison, simonwillison.net/2024/Dec/17/openai-webrtc/)*
- **Our assessment**: The "opaque code example" framing is significant — this is not a
  well-documented API with tutorials. OpenAI released a raw JavaScript snippet on the same
  day they launched the feature. Willison's workflow: treat the code example as a spec,
  delegate the UI scaffolding to Claude, evaluate the result. The resulting tool was
  maintained for 18 months through this June 2026 update, suggesting the AI-scaffolded
  demo was production-sufficient for his use case. For practitioners encountering new APIs
  with sample code but little other documentation, this pattern (paste the sample into
  Claude → request an interactive harness) reduces evaluation time from days to hours.

## Concrete Artifacts

### WebRTC Client-Side Session Setup (from December 2024 post)

```javascript
// OpenAI's reference code for browser-side WebRTC session setup
// Source: OpenAI (via Simon Willison, simonwillison.net/2024/Dec/17/openai-webrtc/)

async function createRealtimeSession(inStream, outEl, token) {
  const pc = new RTCPeerConnection();
  pc.ontrack = e => outEl.srcObject = e.streams[0];
  pc.addTrack(inStream.getTracks()[0]);
  const offer = await pc.createOffer();
  await pc.setLocalDescription(offer);
  const headers = { Authorization: `Bearer ${token}`, 'Content-Type': 'application/sdp' };
  const opts = { method: 'POST', body: offer.sdp, headers };
  const resp = await fetch('https://api.openai.com/v1/realtime', opts);
  await pc.setRemoteDescription({ type: 'answer', sdp: await resp.text() });
  return pc;
}
```

*Source: OpenAI reference code, embedded in Simon Willison's blog post,
simonwillison.net/2024/Dec/17/openai-webrtc/, December 17, 2024*

### Ephemeral Token Security Architecture

```
Browser-based WebRTC voice AI deployment pattern:
  1. User initiates session in browser
  2. Browser calls your server endpoint (POST /get-voice-token or similar)
  3. Server makes authenticated call to OpenAI: request ephemeral token
     - Token valid for: 60 seconds (connection initiation window)
  4. Server returns ephemeral token to browser
  5. Browser uses token in Authorization header for WebRTC SDP exchange
     (as shown in createRealtimeSession above)
  6. WebRTC session established; lasts up to 30 minutes
  7. Server not involved for session duration

"Ephemeral tokens solve that by letting you make a server-side call to request
an ephemeral token which will only allow a connection to be initiated to their
WebRTC endpoint for the next 60 seconds. The user's browser then starts the
connection, which will last for up to 30 minutes."

Source: Simon Willison, simonwillison.net/2024/Dec/17/openai-webrtc/
```

### Document Context UI (from screenshot alt text, verbatim from HTML)

```
OpenAI WebRTC Audio Session interface fields (as of June 2026):
  - OpenAI API Token       (masked password field)
  - Voice                  (dropdown: "Coral" shown)
  - Model                  (dropdown: "gpt-realtime-2" shown)

  ▼ Document context (optional — paste text to talk about)

     [bold label]: "Paste a document here before starting the session
                    and the model will be able to discuss it with you"
     [textarea]:   DuckDB SQL safety document pasted here

  [Start Session]  [Mute Mic (disabled)]
  ✓ Session established successfully!

  Last transcript:
    "DuckDB can be made about as safe as SQLite for running untrusted
    SELECT queries, but only if you lock it down properly. Using read
    only true by itself is not enough, because SQL can still" (text cut off)

Source: screenshot alt attribute, simonwillison.net/2026/Jun/12/openai-webrtc/
```

### GPT-Realtime-2 Model Specification (from OpenAI API docs)

```
Model:           gpt-realtime-2
Description:     "our most capable realtime voice model"
                 "speech-to-speech interactions with configurable reasoning effort,
                  stronger instruction following, and more reliable tool use"
Context window:  128,000 tokens
Max output:      32,000 tokens
Knowledge cutoff: September 30, 2024

Modalities:
  Text   — input and output
  Image  — input only
  Audio  — input and output

Key features:
  Reasoning:        Supported (configurable effort levels)
  Streaming (SSE):  Not supported
  Function calling: Supported
  Fine-tuning:      Not supported

Pricing (per 1M tokens):
  Text input:   $4.00   | Cached: $0.40  | Output: $24.00
  Audio input:  $32.00  | Cached: $0.40  | Output: $64.00
  (Audio ≈ 8× text for input, ≈ 2.7× for output)

Note: "GPT-Realtime-2 supports configurable reasoning effort.
      Higher reasoning effort can increase latency and output token usage."

Source: developers.openai.com/api/docs/models/gpt-realtime-2 (read 2026-06-20)
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-voice-mode-weaker.md` Claim 1 — "ChatGPT's voice mode runs on a
    GPT-4o era model (April 2024 knowledge cutoff)" — this source extends the same
    stratification pattern: GPT-Realtime-2 carries a Sep 2024 cutoff despite "GPT-5-class"
    capability. The gap has narrowed (April → September 2024) but the pattern persists.
  - `blog-simonwillison-voice-mode-weaker.md` Claim 5 — "Most users do not understand
    that the AI interfaces they use may run on substantially different model tiers" — this
    source's Claim 7 (API availability precedes iPhone app deployment) is a temporal
    instance of the same interface-to-model stratification: API users have access to
    GPT-Realtime-2 for weeks before consumer app users.

- **Extends**:
  - `blog-simonwillison-luke-curley-webrtc.md` overall — Curley's May 2026 analysis
    critiques WebRTC as architecturally wrong for LLM voice AI (dropped packets, no
    browser retransmission, 8-RTT setup). This source shows the *other side of that coin*:
    OpenAI uses WebRTC for GPT-Realtime-2, and a practitioner has been building on this
    API since December 2024 with sufficient success to maintain the tool through June 2026.
    The two sources together establish the practitioner reality: WebRTC has the structural
    problems Curley identifies AND OpenAI's implementation is what practitioners actually
    encounter. The guide should present both — the architectural critique AND the
    implemented API — without silently eliding either.
    **Note**: The triage explicitly assessed these as complementary rather than
    contradictory. No contradiction issue filed; see Curley note for the protocol-layer
    critique.
  - `blog-simonwillison-mlx-audio.md` Claim 1 — local audio transcription via
    `uv run` + MLX on macOS. This source provides the cloud-based real-time streaming
    counterpart: cloud API (OpenAI WebRTC) vs. local inference (MLX). Together they cover
    the full audio AI landscape for practitioners — the local path (data stays on machine,
    no ongoing cost, limited capability) and the cloud path (latest model capability,
    audio pricing premium, browser-accessible). Neither source covers comparison between
    the two; the guide should present them as complementary options.

- **Contradicts**: None identified. This source documents OpenAI's WebRTC API as it
  exists and functions; it does not make claims about whether WebRTC is the *right*
  protocol choice for LLM voice AI (that question is covered by the Curley note). No
  contradiction issue required.

- **Novel**:
  - **Client-side document context injection for real-time voice conversations**: No
    prior source in the corpus documents the "paste text into browser before starting
    audio session" pattern for grounding voice AI on external content. The mechanism is
    conceptually simple but practically important: it enables document-grounded voice
    conversations without any server-side retrieval infrastructure.
  - **Ephemeral token security architecture for browser-based voice AI**: No prior corpus
    source documents the 60-second initiation token / 30-minute session architecture as
    the production security model for browser WebRTC voice AI. This is the specific pattern
    that makes browser-based voice AI safe to expose publicly without a persistent server-
    side proxy.
  - **GPT-Realtime-2 audio pricing multiplier (8× text)**: No prior corpus source
    documents the specific audio/text token pricing ratio for production voice AI. The 8×
    premium is a concrete design constraint for practitioners building voice-augmented
    harnesses.
  - **Configurable reasoning effort in a voice model**: No prior corpus source outside the
    Curley cross-reference identifies that GPT-Realtime-2 exposes tunable reasoning effort
    as a first-class API parameter for voice AI.

## Guide Impact

- **Chapter 03 (Voice AI System Design — Document Context Pattern)**: Add the client-side
  text injection pattern as a concrete mechanism for grounding voice conversations on
  external documents. Currently the corpus covers retrieval-augmented generation for text
  AI; this source provides the voice AI equivalent. Frame it as: "For single-session
  document consultation via voice, paste the target text into the client before starting
  the audio session — no server-side retrieval infrastructure required." Cite Claims 4 and
  the screenshot artifact.

- **Chapter 03 (Voice AI System Design — Model Capability vs. Knowledge Currency)**:
  Add the "GPT-5-class reasoning, September 2024 knowledge" pairing as a concrete example
  that voice model capability tier and knowledge currency can diverge significantly. The
  guide should advise practitioners to check the knowledge cutoff of voice models
  explicitly — the promotional framing ("GPT-5-class") does not imply current knowledge.
  Cite Claim 3. Cross-reference `blog-simonwillison-voice-mode-weaker.md` Claim 1 for
  the broader model-stratification pattern.

- **Chapter 03 (Voice AI System Design — API vs. Consumer Deployment Lag)**: Add the
  pattern that voice model capabilities appear at the API layer before consumer products.
  Practitioners who need the latest voice model should target the API directly rather
  than waiting for iPhone/app deployments. Cite Claim 7. Cross-reference
  `blog-simonwillison-voice-mode-weaker.md` Claim 5 for the interface-to-model
  stratification theme.

- **Chapter 02 (Harness Engineering — Browser Voice AI Security)**: Add the ephemeral
  token architecture as the required security pattern for browser-based voice AI
  deployments. The alternative (direct API key in browser) is explicitly marked as
  demo-only. The 60-second/30-minute timing model is a concrete harness constraint —
  the server endpoint only needs to be available at session initiation, not during the
  session. Cite Claim 2 and the ephemeral token architecture artifact.

- **Chapter 02 (Harness Engineering — Audio Token Cost Modeling)**: When discussing voice
  AI cost design, note that audio tokens carry an ~8× premium over text tokens at the
  same provider. A harness that routes 10% of queries through voice at 8× the token cost
  has meaningfully different unit economics than a text-only harness. Cite Claim 5 and
  the pricing artifact.

- **Chapter 04 (Tool Integration — API-First Prototyping Pattern)**: The "paste opaque
  vendor code example into Claude, get working demo" workflow is a concrete instance of
  using AI assistance to evaluate new APIs without waiting for complete documentation.
  Cite Claim 8. Cross-reference `blog-simonwillison-mlx-audio.md` Claim 1 for the
  parallel `uv run` one-liner pattern (both are "try a new capability in minutes"
  approaches).

## Extraction Notes

- **Very thin primary source**: The June 2026 post is ~4 sentences. Per MINER.md §1,
  two linked sub-pages were followed: the December 2024 original tool post (substantive —
  explains the WebRTC pattern and ephemeral token architecture) and the OpenAI
  GPT-Realtime-2 API docs (authoritative model specifications and pricing). All claims
  from sub-pages are attributed to their source explicitly.
- **WebFetch produced summaries, not verbatim text**: Multiple WebFetch attempts returned
  paraphrases rather than the source text. The full post text was obtained via `curl` and
  HTML parsing. The four prose quotes from the June 2026 post are verified against the
  `curl` output; they are character-for-character from the source. The December 2024 post
  quotes were obtained from a second `curl` fetch of that URL. The OpenAI docs content
  was also obtained via `curl`. All quotes in this note were verified against raw HTML
  output before writing.
- **Screenshot alt text**: The verbatim screenshot description comes from the `alt`
  attribute of the `<img>` tag in the page HTML. It is a 250-word alt attribute that
  fully describes the UI. This is not image recognition — it is verbatim text from the
  page source, making it citable as a direct quote.
- **Fragment URL**: The issue URL includes `#atom-everything` (an Atom feed anchor).
  `source_url` uses the canonical page URL without the fragment, consistent with prior
  Willison source notes in this corpus (`blog-simonwillison-mlx-audio.md`,
  `blog-simonwillison-voice-mode-weaker.md`, `blog-simonwillison-luke-curley-webrtc.md`).
- **Cross-reference verification**: Both `blog-simonwillison-luke-curley-webrtc.md` and
  `blog-simonwillison-mlx-audio.md` were read in full before writing cross-references.
  Claim numbers cited match document order in those notes. `blog-simonwillison-voice-
  mode-weaker.md` Claims 1 and 5 were verified against the note text at lines 44–59 and
  119–133 respectively.
- **No contradiction issue filed**: The Curley note critiques WebRTC for LLM voice AI;
  this source shows OpenAI using WebRTC. The triage explicitly assessed these as
  complementary. Curley's critique is aware that OpenAI uses WebRTC (it is critiquing
  that choice); this source does not argue that WebRTC has no problems. The positions
  do not produce contradictory guide advice — Ch03 can present both the working API
  pattern (this source) and the transport protocol critique (Curley) without contradiction.
