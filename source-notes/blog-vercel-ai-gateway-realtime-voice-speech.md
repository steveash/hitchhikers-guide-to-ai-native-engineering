---
source_url: https://vercel.com/changelog/realtime-voice-speech-and-transcription-now-supported-on-ai-gateway
source_type: blog-post
title: "Realtime voice, speech, and transcription now supported on AI Gateway"
author: Kevin Dawkins, Jerilyn Zheng (Vercel)
date_published: 2026-06-29
date_extracted: 2026-07-27
last_checked: 2026-07-27
status: current
confidence_overall: emerging
issue: "#2260"
---

# Realtime voice, speech, and transcription now supported on AI Gateway

> AI Gateway adds three beta audio capabilities — realtime speech-to-speech
> voice agents, text-to-speech, and speech-to-text/transcription — with the
> same observability, spend controls, and BYOK as text/image/video models
> and "no markup or platform fees"; but the changelog's own headline
> understates how uneven the three capabilities' maturity actually is once
> the linked docs are read: realtime is canary-only (not in any released AI
> SDK version), enforces a stricter 25-minute session ceiling than the
> underlying OpenAI model's own 30-minute limit, does not resume across
> reconnects, and TTS is restricted to OpenAI models only with no streaming
> output — all detail entirely absent from the announcement itself.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`,
  published June 29, 2026; a short, ~2-minute-read feature announcement with
  one embedded code example). Per MINER.md §1, this note follows four
  linked pages in full, since the changelog itself states almost no
  mechanism detail: `/docs/ai-gateway/getting-started/realtime` (the
  "realtime quickstart"), `/docs/ai-gateway/modalities/realtime` (the
  realtime reference, including the session-limits table the changelog
  omits entirely), `/docs/ai-gateway/modalities/text-to-speech`, and
  `/docs/ai-gateway/modalities/speech-to-text`. All four docs pages carry
  their own "Last updated June 20, 2026" stamp — nine days *before* this
  changelog entry was published, meaning the reference documentation
  predates the announcement that points to it.
- **Author credibility**: First-party Vercel changelog entry, two named
  authors (Kevin Dawkins, Jerilyn Zheng) verified directly against the raw
  page HTML byline. Jerilyn Zheng is also a listed author on
  `blog-vercel-ai-gateway-api-key-budgets.md` and
  `blog-vercel-ai-gateway-production-index-may2026.md`, both already in
  this corpus — a recurring AI Gateway product-team byline. Vercel operates
  both AI Gateway and the AI SDK described here, so the mechanics (token
  minting, session limits, model names, API shapes) are first-party
  documentation of a shipping/beta capability, not third-party reporting.
  No customer, production deployment, or independent benchmark is cited
  anywhere in the changelog or its four linked docs pages.
- **Scope**: Covers what AI Gateway's realtime, text-to-speech, and
  speech-to-text capabilities do, how to call them (AI SDK and REST), and
  their documented limits (session duration, message size, provider
  restrictions). Does NOT cover: exact per-model or per-minute pricing for
  any of the three capabilities (the "no markup" claim describes fee
  structure, not the underlying provider rates it passes through), a GA
  timeline for any of the three (all beta/canary), independent
  latency/quality benchmarks, or named production deployments using these
  capabilities.

## Extracted Claims

### Claim 1: AI Gateway added three beta audio/voice capabilities — realtime voice agents, text-to-speech, and speech-to-text — available via AI SDK 7, with the same observability, spend controls, and BYOK support as AI Gateway's existing text/image/video models, and "no markup or platform fees"
- **Evidence**: The changelog's opening paragraph, its only framing statement before the capability table.
- **Confidence**: settled (first-party, unambiguous statement of a shipping feature's scope and fee structure)
- **Quote**: "AI Gateway now supports voice and audio models. You can build realtime voice agents, generate speech from text, and transcribe audio to text. This provides the same observability, spend controls, and bring-your-own-key support as text, image, and video models in AI Gateway, with no markup or platform fees. These capabilities are in beta and available via AI SDK 7."
- **Our assessment**: The "no markup or platform fees" line is a specific pricing-model claim not documented anywhere else in this corpus — `blog-vercel-ai-gateway-api-key-budgets.md` documents dollar-denominated spend *caps* on a key, and `blog-vercel-ai-gateway-production-index-may2026.md`'s methodology appendix says spend is measured at "market-rate pricing (published list price)," but neither states that Vercel itself adds no markup on top of that list price. Taken together, the three notes now describe a coherent picture: AI Gateway passes through provider list pricing unmarked-up, and layers spend caps and usage reporting on top — but this is the first source to state the "no markup" pass-through claim explicitly, and it is Vercel's own unverified assertion, not an independently audited comparison of Gateway prices against providers' own direct API prices.

### Claim 2: Realtime voice agents are architecturally a single model that takes audio in and produces audio out directly (speech-to-speech), enabling near-real-time spoken back-and-forth instead of chaining separate transcription, language-model, and speech-generation models
- **Evidence**: A dedicated explanatory sentence introducing the realtime capability, immediately preceding the three-row capability table.
- **Confidence**: settled (first-party architectural description of the capability's design)
- **Quote**: "With realtime support, a single model takes audio in and audio out, so a user can talk and hear a reply back in near real time instead of waiting on a chain of separate models."
- **Our assessment**: This single-model, audio-to-audio framing is the same architectural pattern `blog-simonwillison-openai-webrtc-document-context.md` documents for OpenAI's Realtime API directly (Claim 6 there: "speech-to-speech (audio in, audio out) through the `/v1/realtime` endpoint" rather than a pipeline of separate STT/LLM/TTS calls). This changelog corroborates that architecture is now exposed generically through AI Gateway across multiple providers (Claim 7 below), not just OpenAI's own API surface.

### Claim 3: AI Gateway enforces four hard limits on every realtime session regardless of provider: a 25-minute maximum session duration, a 5-minute idle timeout, a 30-second window for the client's first message after connecting, and a 256 KB maximum message size — plus an unspecified per-team concurrent-session cap
- **Evidence**: A "Session limits" table on the realtime modalities reference page, introduced as limits AI Gateway itself enforces (distinct from any provider-side limit).
- **Confidence**: settled (first-party documentation of specific, numeric platform limits)
- **Quote**: "AI Gateway enforces these limits on every realtime session:" followed by the table rows "Maximum session duration | 25 minutes | The session closes gracefully", "Idle timeout | 5 minutes | The session closes if nothing is sent or received", "First client message | 30 seconds | The session closes if the client sends nothing after connecting", "Maximum message size | 256 KB | The message is rejected." / "Teams also have a limit on concurrent realtime sessions. Additional connection attempts beyond the limit are rejected until a session ends."
- **Our assessment**: This is the answer to the Prospector's "key question" about performance/latency/connection characteristics for this source. Notably, AI Gateway's 25-minute ceiling is *stricter* than the underlying OpenAI model's own limit: `blog-simonwillison-openai-webrtc-document-context.md` Claim 2 documents that an OpenAI Realtime API session "will last for up to 30 minutes" once established via ephemeral token. A team routing `openai/gpt-realtime-2` through AI Gateway therefore hits Gateway's own tighter 25-minute wall five minutes before OpenAI's own session limit would end the call — the gateway layer, not the model provider, is the binding constraint for session length on this path.

### Claim 4: Realtime sessions use a server-mints-token architecture — a server-side `gateway.experimental_realtime.getToken({ model })` call returns a short-lived token and WebSocket URL, so the AI Gateway API key never reaches the browser; the client then connects via the `useRealtime` hook (or, outside the browser, drives the WebSocket directly using the model object as a codec)
- **Evidence**: Both the changelog's own code example and the more detailed quickstart/reference pages describe the same token-minting split.
- **Confidence**: settled (first-party API description with runnable code examples across three separate pages)
- **Quote**: "getToken runs on the server, where your API key lives. It returns a token and the WebSocket URL to connect with." / "Keep AI_GATEWAY_API_KEY on the server. The browser never sees it. Your token route exchanges it for a single-use, short-lived client secret that the browser uses to connect."
- **Our assessment**: This is the identical security pattern `blog-vercel-ai-sdk-7-release.md` and the OpenAI ephemeral-token mechanism (`blog-simonwillison-openai-webrtc-document-context.md` Claim 2, a 60-second connection token) both use: never ship the long-lived credential to a browser client, mint a narrow, short-lived, single-use secret instead. AI Gateway's realtime token adds a gateway-specific detail neither of those two sources states: the minted token is scoped to a specific `model` argument at mint time, so the credential itself is bound to one model, not just short-lived.

### Claim 5: Realtime support in the AI Gateway provider is only available on canary releases of the AI SDK (`@ai-sdk/gateway@canary`, `ai@canary`, `@ai-sdk/react@canary`) — it has not shipped in any stable, released AI SDK version as of this source
- **Evidence**: Stated as a callout box on both the quickstart and reference pages, immediately before any code example.
- **Confidence**: settled (explicit, first-party statement of a specific release-channel restriction)
- **Quote**: "Realtime support in the AI Gateway provider is available on the canary releases of the AI SDK. Install them with pnpm add @ai-sdk/gateway@canary." / "The browser voice agent also needs the canary React bindings. Install them with pnpm add ai@canary @ai-sdk/gateway@canary @ai-sdk/react@canary."
- **Our assessment**: This is a materially stronger caveat than `blog-vercel-ai-sdk-7-release.md` Claim 13's framing of realtime as merely "(experimental)" alongside video generation — "experimental" there described a stable-release API surface marked with an `experimental_` prefix (as this source's own code confirms: `experimental_useRealtime`, `gateway.experimental_realtime`), while "canary-only" here means the capability is not installable from a tagged npm release at all, only from the bleeding-edge pre-release channel. A team reading only the June 25 AI SDK 7 changelog could reasonably assume realtime was available (if unstable) in the `ai@7.x` release they'd just installed; this source clarifies that assumption is wrong for realtime specifically — canary is a separate, less stable install target than the tagged `experimental_` APIs the June 25 changelog otherwise describes.

### Claim 6: The realtime model object doubles as a protocol codec for non-browser environments — `getWebSocketConfig` builds the raw WebSocket connection parameters from a token, and `serializeClientEvent`/`parseServerEvent` translate between normalized AI SDK event types and each provider's own wire format, letting a Node.js script drive the same WebSocket manually instead of using the `useRealtime` browser hook
- **Evidence**: The Node.js quickstart and reference-page "Node.js" section, both with a complete worked script.
- **Confidence**: settled (first-party API description with two matching runnable code examples)
- **Quote**: "The realtime model is a codec: it builds the WebSocket config and translates between normalized AI SDK events and the provider wire format." / "getWebSocketConfig builds the connection from the token, and serializeClientEvent and parseServerEvent translate events to and from the normalized format."
- **Our assessment**: This is the concrete mechanism by which AI Gateway achieves cross-provider normalization for realtime specifically: rather than every provider's raw WebSocket event schema leaking through to application code, the AI SDK's codec functions translate to one normalized event vocabulary (`conversation-item-create`, `response-create`, `audio-transcript-delta`, `audio-delta`, `response-done`, `error`) regardless of which underlying provider model is connected. This is a provider-abstraction pattern distinct from, but philosophically similar to, the cross-provider `reasoning` parameter documented in `blog-vercel-ai-sdk-7-release.md` Claim 3 — both normalize a provider-specific surface behind one AI SDK vocabulary.

### Claim 7: Two specific realtime models are named across the quickstart and reference docs — `openai/gpt-realtime-2` (used in the browser/React example) and `xai/grok-voice-think-fast-1.0` (used in the Node.js script example) — and the two are not interchangeable in capability: `xai/grok-voice-think-fast-1.0` "supports speech-to-speech only," explicitly excluding transcription or translation
- **Evidence**: Both quickstart sections and the reference page state the model names and the xAI model's capability restriction in the same sentence introducing the example code.
- **Confidence**: settled (first-party naming of specific models with an explicit, stated capability boundary for one of them)
- **Quote**: "The script below uses xai/grok-voice-think-fast-1.0 and the browser agent uses openai/gpt-realtime-2. Both are realtime speech-to-speech models, so swap the model ID to switch between them. xai/grok-voice-think-fast-1.0 supports speech-to-speech only, so it does not handle transcription or translation."
- **Our assessment**: This is a concrete, checkable example of provider-model capability variance within a single AI Gateway modality that this corpus has not previously documented at this granularity — "realtime" is not a uniform capability across providers even when both models are nominally "realtime speech-to-speech." `blog-simonwillison-openai-webrtc-document-context.md` documents `gpt-realtime-2` specifically (Claim 3: "GPT-5-class reasoning," a September 30 2024 knowledge cutoff, released May 2026); this source corroborates that model name and adds the AI-Gateway-routing detail plus a second, differently-capable realtime model (xAI's) as a named point of comparison.

### Claim 8: Text-to-speech (`experimental_generateSpeech`) and speech-to-text (`experimental_transcribe`, `experimental_streamTranscribe`) access on AI Gateway is beta and "rolling out gradually," meaning speech and transcription models may not yet appear in a given team's model catalog — a materially narrower access claim than the June 25 AI SDK 7 changelog's statement that `generateSpeech` and `transcribe` are already "stable exports"
- **Evidence**: Identical beta-rollout callout boxes on both the text-to-speech and speech-to-text reference pages.
- **Confidence**: settled (explicit, first-party statement of gradual, team-gated feature rollout)
- **Quote**: "Text to speech is in beta and access is rolling out gradually. Speech models may not appear in the model catalog yet for your team." / "Speech to text is in beta and access is rolling out gradually. Transcription models may not appear in the model catalog yet for your team."
- **Our assessment**: This does not contradict `blog-vercel-ai-sdk-7-release.md` Claim 13 (which states the AI SDK *function exports* `generateSpeech`/`transcribe`/`SpeechResult`/`TranscriptionResult` are stable, non-experimental symbols in the `ai` package) — the two claims describe different layers: the SDK-level function signature is stable and won't change, but AI-Gateway-specific *model access* to actually call those functions against Gateway-routed speech/transcription models is still a gradually-rolling-out beta with team-by-team gating. A practitioner who reads only the AI SDK 7 changelog and assumes "stable" means "generally available to call today via AI Gateway" would be wrong for the Gateway-routing path specifically; this is a nuance worth flagging in the guide rather than a corpus contradiction, since neither source makes a claim the other directly opposes.

### Claim 9: Streaming transcription (`experimental_streamTranscribe`) is a distinct code path from batch transcription (`experimental_transcribe`) — it streams partial results over a WebSocket as audio arrives, supports a different (smaller) set of models than batch transcription, and for browser use requires its own short-lived, single-use, model-scoped token (60-second default expiry, 300-second maximum) minted via `gateway.experimental_transcription.getToken`
- **Evidence**: A dedicated "Streaming transcription" section plus a "Stream from the browser" subsection on the speech-to-text reference page, with two separate worked code examples.
- **Confidence**: settled (first-party API description with runnable code examples and explicit numeric token-lifetime bounds)
- **Quote**: "For live audio, use experimental_streamTranscribe to receive transcript updates before the audio stream is complete. AI Gateway connects to the model over a WebSocket and streams results back as the provider produces them." / "The token is single use, expires after 60 seconds by default (300 seconds maximum), and only opens streaming transcription connections for the model it was minted for." / "Recorded audio and streaming support different model sets. Browse transcription models and add the WebSockets filter to see which models support streaming."
- **Our assessment**: The streaming-transcription token (60s default/300s max, single-use, model-scoped) is a third instance of the same short-lived-credential-minting pattern this source uses for realtime (Claim 4) — AI Gateway applies the identical security architecture across two of its three new audio capabilities, with the specific expiry numbers documented here for the first time in this corpus (the realtime `getToken` call's own token lifetime is not given a specific expiry number anywhere in this source, unlike the transcription token's explicit 60s/300s bounds).

### Claim 10: Text-to-speech is restricted to OpenAI speech models only, returns only a full base64-encoded audio payload in a single JSON response (no streaming audio output), and the REST endpoint for transcription accepts only a base64-encoded body (no multipart file upload)
- **Evidence**: Explicit "Limitations" sections on both the text-to-speech and speech-to-text reference pages.
- **Confidence**: settled (first-party statement of specific, checkable capability restrictions)
- **Quote**: "Audio returns base64-encoded in a JSON response. Streaming audio output is not supported." / "Text to speech supports OpenAI speech models only." / "Audio for the REST API is sent base64-encoded in a JSON body. Multipart file uploads are not supported. The REST API returns the full transcript in a single JSON response. To stream results, use experimental_streamTranscribe with the AI SDK."
- **Our assessment**: The OpenAI-only restriction on text-to-speech is notable because it cuts against AI Gateway's general multi-provider value proposition (documented across `blog-vercel-ai-gateway-production-index-may2026.md`'s multi-provider routing data) — for this one specific modality, "AI Gateway" currently means "an AI-Gateway-routed call to one provider's models," not a genuine multi-vendor choice the way text generation or even realtime (Claim 7: OpenAI and xAI models both shown) already is.

### Claim 11: A realtime session cannot resume its prior conversation state after a reconnect — a client must start an entirely new session and re-supply whatever context it needs; realtime sessions also do not accept image input
- **Evidence**: A dedicated "Limitations" section on the realtime reference page.
- **Confidence**: settled (first-party statement of two specific capability boundaries)
- **Quote**: "Image input is not supported in realtime sessions." / "Reconnecting does not resume a previous session. Start a new session and replay any context you need."
- **Our assessment**: Combined with Claim 3's 25-minute/5-minute-idle enforced limits, this means every AI-Gateway-routed realtime session is architecturally disposable by design: a session will eventually be closed by the gateway (duration, idle, or disconnect), and reconnecting is always a cold start requiring the client to replay context, not a resume. This mirrors the exact "treat every connection as ephemeral, externalize state" architectural requirement `blog-vercel-websocket-support-public-beta.md` Claim 5 documents for Vercel's general-purpose Function-hosted WebSockets — though that is a structurally different WebSocket (a Vercel Function serving an application-defined WS endpoint) from this one (AI Gateway's own managed realtime proxy to a model provider), the same "no session resume, replay context on reconnect" operational discipline applies to both.

## Concrete Artifacts

### Full changelog capability table (verbatim, from the changelog itself)

```
Capability | What it does
Realtime voice agents | Model listens to the user, works out a response, and
  speaks it back in a live, low-latency conversation. It can call your tools
  mid-conversation to look something up or take an action. The useRealtime
  hook handles microphone capture and playback.
Text to speech | Generate spoken audio from text, with a selectable voice
  and output format such as MP3. Use it for voiceovers, audio versions of
  written content, and spoken responses.
Speech to text | Transcribe recordings into text, from a file buffer,
  base64 string, or URL. Use it for voice notes or other transcriptions.

Source: https://vercel.com/changelog/realtime-voice-speech-and-transcription-now-supported-on-ai-gateway
```

### Changelog's own token route + browser hook example (verbatim)

```typescript
// app/api/realtime/token/route.ts
import { gateway } from '@ai-sdk/gateway';

export async function POST() {
  const { token, url } = await gateway.experimental_realtime.getToken({
    model: 'openai/gpt-realtime-2',
  });
  return Response.json({ token, url, tools: [] });
}
```

```typescript
'use client';
import { experimental_useRealtime as useRealtime } from '@ai-sdk/react';
import { gateway } from '@ai-sdk/gateway';

const { status, connect, startAudioCapture } = useRealtime({
  model: gateway.experimental_realtime('openai/gpt-realtime-2'),
  api: { token: '/api/realtime/token' },
  sessionConfig: { voice: 'alloy', turnDetection: { type: 'server-vad' } },
});
// Call connect(), then startAudioCapture(stream) to start talking.
```
Source: https://vercel.com/changelog/realtime-voice-speech-and-transcription-now-supported-on-ai-gateway

### Node.js realtime script as WebSocket codec (verbatim, from the realtime quickstart)

```typescript
// realtime.ts
import { gateway } from '@ai-sdk/gateway';
import WebSocket from 'ws';

const modelId = 'xai/grok-voice-think-fast-1.0';
const { token, url } = await gateway.experimental_realtime.getToken({ model: modelId });
const model = gateway.experimental_realtime(modelId);
const config = model.getWebSocketConfig({ token, url });
const ws = new WebSocket(config.url, config.protocols);

ws.on('open', async () => {
  ws.send(JSON.stringify(await model.serializeClientEvent({
    type: 'conversation-item-create',
    item: { type: 'text-message', role: 'user', text: 'Say hello in one sentence.' },
  })));
  ws.send(JSON.stringify(await model.serializeClientEvent({ type: 'response-create' })));
});

ws.on('message', (data) => {
  const parsed = model.parseServerEvent(JSON.parse(data.toString()));
  for (const event of Array.isArray(parsed) ? parsed : [parsed]) {
    if (event.type === 'audio-transcript-delta') process.stdout.write(event.delta);
    // event.type 'audio-delta' carries base64 PCM16 audio chunks
  }
});
```
"Realtime audio streams as PCM16 at 24 kHz, so the script adds a WAV header to make reply.wav playable."
Source: https://vercel.com/docs/ai-gateway/getting-started/realtime

### Realtime session limits table (verbatim, from the realtime reference page)

| Limit | Value | What happens when exceeded |
|---|---|---|
| Maximum session duration | 25 minutes | The session closes gracefully |
| Idle timeout | 5 minutes | The session closes if nothing is sent or received |
| First client message | 30 seconds | The session closes if the client sends nothing after connecting |
| Maximum message size | 256 KB | The message is rejected |

"Teams also have a limit on concurrent realtime sessions. Additional connection attempts beyond the limit are rejected until a session ends."
Source: https://vercel.com/docs/ai-gateway/modalities/realtime

### Text-to-speech AI SDK and REST examples (verbatim, from the text-to-speech reference page)

```typescript
// generate-speech.ts
import { experimental_generateSpeech as generateSpeech } from 'ai';
import { gateway } from '@ai-sdk/gateway';
import { writeFile } from 'node:fs/promises';

const result = await generateSpeech({
  model: gateway.speechModel('openai/tts-1'),
  text: 'Hello! Thanks for trying out AI Gateway.',
  voice: 'alloy',
  outputFormat: 'mp3',
});
await writeFile('greeting.mp3', result.audio.uint8Array);
```

```bash
curl -X POST https://ai-gateway.vercel.sh/v4/ai/speech-model \
  -H "Authorization: Bearer $AI_GATEWAY_API_KEY" \
  -H "ai-model-id: openai/tts-1" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello! Thanks for trying out AI Gateway.", "voice": "alloy", "outputFormat": "mp3"}' \
  | jq -r '.audio' | base64 -d > greeting.mp3
```
Request options table: `text` (required), `voice`, `outputFormat`, `instructions`, `speed` (defaults to 1), `language` — "Support for each option varies by model. Unsupported options are reported in warnings on the result instead of failing the request."
Source: https://vercel.com/docs/ai-gateway/modalities/text-to-speech

### Speech-to-text batch, streaming, and browser-token examples (verbatim, from the speech-to-text reference page)

```typescript
// transcribe.ts
import { experimental_transcribe as transcribe } from 'ai';
import { gateway } from '@ai-sdk/gateway';
import { readFile } from 'node:fs/promises';

const result = await transcribe({
  model: gateway.transcriptionModel('openai/whisper-1'),
  audio: await readFile('meeting.mp3'),
});
console.log(result.text);
console.log(`Audio duration: ${result.durationInSeconds} seconds`);
```
"Transcription support requires recent releases of the AI SDK: ai 7.0.31 and @ai-sdk/gateway 4.0.23 or later."

```typescript
// stream-transcribe.ts
import { experimental_streamTranscribe as streamTranscribe } from 'ai';
import { gateway } from '@ai-sdk/gateway';

const result = streamTranscribe({
  model: gateway.transcriptionModel('openai/gpt-realtime-whisper'),
  audio: audioStream, // ReadableStream<Uint8Array | string>
  inputAudioFormat: { type: 'audio/pcm', rate: 24000 },
});
for await (const part of result.fullStream) {
  if (part.type === 'transcript-delta') process.stdout.write(part.delta);
  if (part.type === 'transcript-final') console.log('final:', part.text);
}
```

```typescript
// app/api/transcription/token/route.ts
import { gateway } from '@ai-sdk/gateway';
export async function POST() {
  const { token, url } = await gateway.experimental_transcription.getToken({
    model: 'openai/gpt-realtime-whisper',
  });
  return Response.json({ token, url });
}
```
Response shape: `{ "text": "...", "segments": [], "language": "en", "durationInSeconds": 4.2, "warnings": [] }`
Source: https://vercel.com/docs/ai-gateway/modalities/speech-to-text

## Cross-References

### Cross-reference verification notes
`blog-vercel-ai-sdk-7-release.md`, `blog-vercel-ai-gateway-api-key-budgets.md`,
`blog-vercel-ai-gateway-production-index-may2026.md`,
`blog-vercel-websocket-support-public-beta.md`, and
`blog-simonwillison-openai-webrtc-document-context.md` were re-read in full
during this extraction (MINER.md §4b), and every claim number cited below
was located and confirmed against that note's own numbered `### Claim N:`
headings in document order before writing this section.

- **Corroborates**:
  - `blog-simonwillison-openai-webrtc-document-context.md` Claim 6
    (`gpt-realtime-2` uses speech-to-speech, "audio in, audio out," not a
    streaming-completions model) and Claim 3 (naming `gpt-realtime-2`
    specifically, "GPT-5-class reasoning," May 2026 release): this source's
    Claim 2 (single model, audio in/audio out) and Claim 7 (naming
    `openai/gpt-realtime-2` as the browser-quickstart model) independently
    confirm the same model and the same speech-to-speech architecture from
    the infrastructure-provider (Vercel) side rather than the model-vendor
    (OpenAI) side.
  - `blog-vercel-ai-sdk-7-release.md` Claim 13 ("Realtime (experimental):
    Browser-to-provider WebSocket sessions for OpenAI, Google, and xAI...
    normalized routing through AI Gateway"): this source is the detailed,
    AI-Gateway-specific documentation of exactly the capability that
    changelog announced four days earlier, supplying the token-minting
    architecture, session limits, and named models that note's brief
    changelog bullet did not include.
  - `blog-vercel-ai-sdk-7-release.md` Claim 4/Claim 3 (provider-abstraction
    patterns: `HarnessAgent` normalizing five external harnesses; the
    `reasoning` parameter fanning out to ten providers): this source's Claim
    6 (the realtime codec's `serializeClientEvent`/`parseServerEvent`
    normalizing provider-specific WebSocket wire formats to one AI SDK
    event vocabulary) is a third instance of the same general AI-SDK design
    philosophy — normalize a fragmented provider surface behind one typed
    interface — applied to realtime's wire protocol specifically.

- **Contradicts**: None filed as a formal MINER.md §4a contradiction. One
  near-miss was evaluated and ruled out: this source's Claim 8 (speech/
  transcription AI-Gateway model access is beta and "rolling out
  gradually") in tension with `blog-vercel-ai-sdk-7-release.md` Claim 13
  (`generateSpeech`/`transcribe` are "stable exports"). These are not
  opposing claims about the same fact — one describes the stability of an
  AI SDK function's *code signature*, the other describes the rollout
  status of AI-Gateway-routed *model access* for calling that function —
  so no contradiction issue was filed; the distinction is carried forward
  explicitly in Claim 8's "Our assessment" and in Guide Impact below.

- **Extends**:
  - `blog-simonwillison-openai-webrtc-document-context.md` Claim 2 (OpenAI's
    own Realtime API session lasts "up to 30 minutes" after a 60-second
    ephemeral token): this source's Claim 3 (AI Gateway enforces its own,
    stricter 25-minute session ceiling, 5-minute idle timeout, and 30-second
    first-message window) extends that note with the gateway-layer limit
    that sits *in front of* the provider's own limit — for a Gateway-routed
    `gpt-realtime-2` session, AI Gateway's 25-minute wall binds before
    OpenAI's 30-minute one would.
  - `blog-vercel-websocket-support-public-beta.md` Claim 5 (Vercel Function-
    hosted WebSocket connections are forced-ephemeral by design: reconnects
    may land on a different instance, state must be externalized) and Claim
    4 (Function-hosted WebSocket lifetime bounded by the Function's max
    duration, up to 1800s beta): this source's Claim 11 (a realtime session
    does not resume across reconnects; the client must replay context) is
    the same "connection is disposable, state does not travel with it"
    operational discipline applied to a structurally different WebSocket —
    AI Gateway's own managed realtime proxy, not an application-defined
    Vercel Function WebSocket endpoint. The two sources describe two
    separate Vercel WebSocket implementations that independently arrive at
    the identical "no resume, replay on reconnect" architecture.
  - `blog-vercel-ai-gateway-api-key-budgets.md` and
    `blog-vercel-ai-gateway-production-index-may2026.md`: both document
    AI Gateway's spend-governance and usage-telemetry surfaces for
    text/image/video traffic. This source extends that same governance
    surface explicitly to the three new audio capabilities (Claim 1: "the
    same observability, spend controls, and bring-your-own-key support"),
    while adding the first "no markup or platform fees" pricing-structure
    statement this corpus has seen for any AI Gateway modality.

- **Novel**:
  - **A dollar-cost-neutral ("no markup or platform fees") pricing claim
    for an AI-gateway product** (Claim 1): no prior corpus source states
    this explicitly for AI Gateway, though it is consistent with the
    market-rate/list-price framing in
    `blog-vercel-ai-gateway-production-index-may2026.md`'s methodology
    appendix.
  - **A model-scoped, single-use, numerically-bounded (60s/300s) streaming-
    transcription token distinct from the realtime token** (Claim 9): the
    first source in this corpus to give exact expiry numbers for an AI SDK
    ephemeral browser-connection token.
  - **Canary-only (not merely "experimental") release-channel gating for a
    named AI SDK capability** (Claim 5): a stronger and more specific
    caveat than the `experimental_`-prefix convention this corpus has
    otherwise documented for AI SDK 7's other beta features.
  - **Explicit per-provider capability variance within one nominal realtime
    modality** (Claim 7: `xai/grok-voice-think-fast-1.0` cannot transcribe
    or translate, unlike `openai/gpt-realtime-2`): a concrete, checkable
    example that "realtime" is not a uniform capability contract across
    AI-Gateway-routed providers.
  - **A single-provider restriction (OpenAI-only) on one AI Gateway
    modality specifically** (Claim 10, text-to-speech): the first
    documented case in this corpus of an AI Gateway modality *not*
    offering genuine multi-provider choice, in contrast to the gateway's
    general multi-vendor routing value proposition documented elsewhere.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add AI Gateway's realtime
  voice-agent architecture (Claims 2, 4, 6) as a concrete, primary-sourced
  pattern for building voice-driven agent harnesses: a server-minted,
  short-lived, model-scoped token keeps the long-lived AI Gateway key off
  the browser, and the realtime model object doubles as a protocol codec
  for non-browser (Node.js) integration paths. Explicitly carry forward
  the session-lifetime constraints (Claim 3: 25 min max, 5 min idle, no
  resume on reconnect per Claim 11) as a design requirement — any
  voice-agent harness built on this capability must externalize
  conversation context and replay it on reconnect, the same operational
  discipline `blog-vercel-websocket-support-public-beta.md` already
  established for Vercel's general-purpose Function-hosted WebSockets.

- **Chapter 02 (Harness Engineering) — maturity caveat**: Flag the
  canary-only release-channel requirement for realtime specifically (Claim
  5) as a stronger caveat than "experimental" — a team should not expect
  to `pnpm add ai` and get realtime support; it requires opting into
  pre-release canary builds across three separate packages. Pair this with
  Claim 8's beta/gradual-rollout caveat for speech and transcription model
  *access* specifically (distinct from the AI SDK function signatures
  themselves being stable, per `blog-vercel-ai-sdk-7-release.md` Claim 13)
  so the guide does not overstate how "ready" any of these three
  capabilities are for production use as of this source's date.

- **Chapter 02 (Harness Engineering) — provider variance**: Add Claim 7
  (per-provider capability variance within the realtime modality) and
  Claim 10 (text-to-speech's OpenAI-only restriction) as concrete
  reminders that AI Gateway's multi-provider routing promise does not
  apply uniformly across every modality — a team building on realtime or
  TTS specifically should verify per-model/per-modality capability
  support rather than assuming Gateway-wide provider interchangeability.

## Extraction Notes

1. **WebFetch output not trusted for quotes; raw HTML fetched and parsed
   directly, per MINER.md §2a.** An initial WebFetch pass on the changelog
   URL returned an accurate-reading but AI-condensed summary (correct in
   substance, but not a verbatim reproduction — e.g., it paraphrased the
   capability table as flowing prose rather than the source's actual
   three-row table structure). This note instead retrieved the changelog
   and its four linked docs pages via direct `curl` requests with a
   browser user-agent, isolated each page's `<article>` element, stripped
   markup to plain text with a Python script, and read the resulting text
   in full for every page. Every `Quote` field in this note was located
   character-for-character in that locally-parsed plain text, not the
   WebFetch summary. The byline authors and publish date were independently
   verified against the raw HTML's JSON-LD metadata
   (`datePublished: 2026-06-29T00:00+00:00`) and `<a class="...author...">`
   anchor text, not taken from the WebFetch pass.
2. **Four linked pages followed, per MINER.md §1's "up to 5" guidance.**
   The changelog itself contains almost no mechanism detail (session
   limits, token-minting flow, model names, and every code example beyond
   the single token-route/hook snippet in the changelog all come from the
   linked pages), so all four substantive docs links
   (`/docs/ai-gateway/getting-started/realtime`,
   `/docs/ai-gateway/modalities/realtime`,
   `/docs/ai-gateway/modalities/text-to-speech`,
   `/docs/ai-gateway/modalities/speech-to-text`) were fetched and read in
   full. A fifth potential link (the AI Gateway Models catalog page,
   linked for browsing available realtime/speech/transcription models) was
   not followed, since it is a filterable model-listing page rather than a
   substantive explanatory page — no additional claims would have come
   from it beyond what the docs pages already name.
3. **No contradiction issues filed.** One tension (Claim 8's beta/
   gradual-rollout framing versus `blog-vercel-ai-sdk-7-release.md`'s
   "stable exports" framing) was evaluated against MINER.md §4a and judged
   not to rise to a contradiction, since the two claims describe different
   things (SDK function-signature stability vs. AI-Gateway model-access
   rollout status) rather than opposing assertions about the same fact;
   see Cross-References → Contradicts.
4. **Confidence calibration: emerging.** Individual claims are mostly rated
   "settled" because they are first-party, unambiguous descriptions of a
   shipping/beta feature's documented mechanics (session-limit numbers,
   token-expiry numbers, named models, explicit capability restrictions),
   verified against directly-fetched raw HTML rather than an
   AI-summarized intermediate. The note's overall confidence is "emerging"
   rather than "settled" because: (a) this is a single vendor's own
   release announcement with no independent verification, benchmark, or
   named customer/production evidence anywhere in the source or its four
   linked pages; (b) all three headline capabilities are explicitly
   beta, and realtime specifically is gated behind canary (pre-release)
   package versions, not a tagged release (Claim 5); and (c) the "no
   markup or platform fees" pricing claim (Claim 1) is asserted, not
   independently audited against provider list prices in this source.
