---
source_url: https://vercel.com/changelog/xai-grok-audio-models-now-available-on-vercel-ai-gateway
source_type: blog-post
title: "xAI Grok audio models now available on Vercel AI Gateway"
author: Kevin Dawkins, Jerilyn Zheng, Carlton Aikins (Vercel)
date_published: 2026-06-29
date_extracted: 2026-07-28
last_checked: 2026-07-28
status: current
confidence_overall: emerging
issue: "#2275"
---

# xAI Grok audio models now available on Vercel AI Gateway

> A short Vercel changelog entry announcing that all three xAI Grok audio
> models — `xai/grok-voice-think-fast-1.0` (realtime), `xai/grok-tts` (text
> to speech), and `xai/grok-stt` (speech to text) — are now routable through
> AI Gateway with runnable code examples for each; but the `xai/grok-tts`
> availability claim directly contradicts AI Gateway's own text-to-speech
> reference documentation, which as of this extraction (a full month after
> this changelog) still states "text to speech supports OpenAI speech
> models only" — filed as a contradiction (issue #2282) rather than resolved
> silently in this note.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`,
  published June 29, 2026, `dateModified` June 30, 2026 per the page's own
  JSON-LD; a short, single-screen feature announcement with four code
  examples and no prose beyond brief section intros).
- **Author credibility**: First-party Vercel changelog entry, three named
  authors verified against the page's JSON-LD metadata and byline anchor
  tags: Kevin Dawkins and Jerilyn Zheng (both also credited on
  `blog-vercel-ai-gateway-realtime-voice-speech.md`, a recurring AI-Gateway
  product-team byline pairing in this corpus), plus Carlton Aikins (new to
  this corpus, listed jobTitle "Software Engineer"). Vercel operates AI
  Gateway and the AI SDK described here, so this is first-party
  documentation of a shipping integration, not third-party reporting. No
  customer, production deployment, or independent benchmark is cited.
- **Scope**: Covers which xAI audio model IDs are routable through AI
  Gateway and minimal runnable code for each (realtime token route +
  browser hook, `generateSpeech`, `transcribe`). Does NOT cover: pricing for
  any of the three xAI models, a GA timeline, latency/quality benchmarks,
  named production deployments, or — despite naming `xai/grok-tts` as
  available — any update to the separate reference-docs page that
  documents text-to-speech's Limitations (see Claim 4, Cross-References).

## Extracted Claims

### Claim 1: All three of xAI's audio models — realtime voice, text to speech, and speech to text — are now available on AI Gateway via AI SDK 7, with "the same routing, observability, and spend controls as your other models"
- **Evidence**: The changelog's opening paragraph, its only framing statement before the capability table.
- **Confidence**: settled (first-party, unambiguous statement of a shipping integration's scope)
- **Quote**: "xAI's audio models are now live on AI Gateway. Realtime voice, text to speech, and speech to text are all available through the AI SDK with the same routing, observability, and spend controls as your other models. These capabilities are available on the AI SDK 7 release."
- **Our assessment**: This is a narrower, single-vendor (xAI-only) companion announcement to the broader multi-vendor rollout `blog-vercel-ai-gateway-realtime-voice-speech.md` documents (three audio capabilities across OpenAI and xAI models generally). The "same routing, observability, and spend controls" line corroborates that note's Claim 1 verbatim in substance, extended here specifically to xAI's models.

### Claim 2: Three specific xAI model IDs are named as the available model for each of the three audio capabilities: `xai/grok-voice-think-fast-1.0` for realtime voice, `xai/grok-tts` for text to speech, and `xai/grok-stt` for speech to text
- **Evidence**: An "Available models" table, the first content block after the intro paragraph, mapping each capability to exactly one model ID.
- **Confidence**: settled (first-party naming of specific model identifiers in a structured table)
- **Quote**: "Capability | Models" / "Realtime voice | xai/grok-voice-think-fast-1.0" / "Text to speech | xai/grok-tts" / "Speech to text | xai/grok-stt"
- **Our assessment**: `xai/grok-voice-think-fast-1.0` is already documented in `blog-vercel-ai-gateway-realtime-voice-speech.md` Claim 7 as the Node.js-quickstart realtime model, corroborating that model ID. `xai/grok-tts` and `xai/grok-stt` are new model IDs not present anywhere else in this corpus — this is the first source-note documentation of xAI-specific text-to-speech and speech-to-text model identifiers.

### Claim 3: A complete `generateSpeech()` example demonstrates `xai/grok-tts` producing spoken audio with the voice `'eve'`, written to an MP3 file
- **Evidence**: A full, runnable TypeScript code block under the "Text to speech" section heading.
- **Confidence**: settled (first-party runnable code example naming the specific model and a specific voice parameter value)
- **Quote**: "Generate spoken audio from text with generateSpeech. Pass a voice and an output format, then write the result to a file with xai/grok-tts:"
- **Our assessment**: The voice value `'eve'` is new to this corpus — `blog-vercel-ai-gateway-realtime-voice-speech.md`'s text-to-speech example uses `'alloy'` (an OpenAI voice name) for `openai/tts-1`. This confirms `xai/grok-tts` has its own distinct voice catalog rather than sharing OpenAI's voice names, though this source does not enumerate the full set of available xAI voices.

### Claim 4: This changelog's `xai/grok-tts` example directly contradicts AI Gateway's own text-to-speech reference documentation, which states text to speech "supports OpenAI speech models only" and was last updated nine days before this changelog and has not been revised as of a month after it
- **Evidence**: Cross-check performed during this extraction: the `vercel.com/docs/ai-gateway/modalities/text-to-speech` reference page (re-fetched live on 2026-07-28, the date of this extraction) still carries a "Limitations" section reading "Text to speech supports OpenAI speech models only," stamped "Last updated June 20, 2026" — nine days before this changelog's June 29 publish date, and unrevised as of this extraction, roughly a month later.
- **Confidence**: emerging (the changelog's own claim is settled/first-party; the *conflict* with the still-live reference doc is the emerging, unresolved part)
- **Quote**: "Text to speech supports OpenAI speech models only." (from `vercel.com/docs/ai-gateway/modalities/text-to-speech`, "Limitations" section, re-fetched 2026-07-28, page stamped "Last updated June 20, 2026")
- **Our assessment**: This is a genuine, material contradiction, not a rollout-timing nuance — filed as issue #2282 per MINER.md §4a rather than resolved unilaterally here. Two readings are both plausible: (a) the reference doc is simply stale and nobody updated its Limitations bullet when `xai/grok-tts` shipped, or (b) the changelog is describing a capability that exists in the AI SDK/model catalog but isn't actually callable for most teams yet, consistent with the same reference page's separate statement that "text to speech is in beta and access is rolling out gradually. Speech models may not appear in the model catalog yet for your team" (also documented in `blog-vercel-ai-gateway-realtime-voice-speech.md` Claim 8). Either way, a practitioner who read only the existing source note's Claim 10 ("OpenAI speech models only") as a hard architectural constraint would now be wrong for at least the `xai/grok-tts` case — see Guide Impact.

### Claim 5: The realtime voice-agent architecture for xAI's model follows the identical two-piece pattern already documented for OpenAI's realtime model: a server route mints a short-lived token so the API key never reaches the client, and a browser component connects using that token
- **Evidence**: The "Realtime" section's introductory sentence plus two runnable code examples (server token route, browser `useRealtime` hook), both using `xai/grok-voice-think-fast-1.0` in place of `openai/gpt-realtime-2`.
- **Confidence**: settled (first-party API description with runnable code, mirroring an already-verified pattern)
- **Quote**: "A voice agent has two pieces: a server route that mints a short-lived token, so your API key never reaches the client, and a browser component that connects with it."
- **Our assessment**: This corroborates `blog-vercel-ai-gateway-realtime-voice-speech.md` Claim 4 (server-mints-token architecture) exactly, confirming the same short-lived-credential pattern applies regardless of which realtime model (OpenAI or xAI) is selected — the architecture is provider-agnostic, only the `model` string argument changes between the two sources' examples.

### Claim 6: The xAI realtime browser example configures `turnDetection: { type: 'server-vad' }` but, unlike the existing OpenAI-model example in the corpus, does not set a `voice` parameter in `sessionConfig`
- **Evidence**: Direct comparison of this source's `useRealtime()` call against `blog-vercel-ai-gateway-realtime-voice-speech.md`'s Concrete Artifacts code block for the same hook.
- **Confidence**: anecdotal (a code-example difference; this source does not state whether `voice` is unsupported or simply omitted for brevity)
- **Quote**: "const { status, connect, startAudioCapture } = useRealtime({ model: gateway.experimental_realtime('xai/grok-voice-think-fast-1.0'), api: { token: '/api/realtime/token' }, sessionConfig: { turnDetection: { type: 'server-vad' } } });"
- **Our assessment**: Given `blog-vercel-ai-gateway-realtime-voice-speech.md` Claim 7 already establishes that `xai/grok-voice-think-fast-1.0` "supports speech-to-speech only" and excludes transcription/translation, it is plausible (but not confirmed by this source) that xAI's realtime model also has a narrower or differently-named voice-selection surface than OpenAI's; this source simply doesn't exercise that parameter, so we flag the omission as a gap rather than asserting a capability restriction.

### Claim 7: An `xai/grok-stt` speech-to-text example uses the same `transcribe()` API and response shape (`result.text`) already documented for OpenAI transcription models
- **Evidence**: A complete "Speech to text" code block importing `transcribe` from `ai` and passing `model: 'xai/grok-stt'`.
- **Confidence**: settled (first-party runnable code example)
- **Quote**: "Transcribe recordings into text with transcribe. This example uses xai/grok-stt:"
- **Our assessment**: Corroborates the provider-agnostic `transcribe()` interface `blog-vercel-ai-gateway-realtime-voice-speech.md` documents (its own example uses `openai/whisper-1`) — the same AI SDK function signature works across at least two providers for this modality, unlike the text-to-speech restriction flagged in Claim 4.

### Claim 8: Vercel provides an interactive playground where the `xai/grok-voice-think-fast-1.0` realtime model can be tried directly in the browser without writing code
- **Evidence**: A "Playground" section pointing to the AI Gateway models list and a specific playground link for the realtime model.
- **Confidence**: settled (first-party statement of a product feature)
- **Quote**: "You can also try the xAI audio models directly in the AI Gateway playground. Open the models list and click into any of the models to use them directly in the browser. The xai/grok-voice-think-fast-1.0 playground here allows you to talk to the agent and see responses instantly."
- **Our assessment**: New to this corpus — neither `blog-vercel-ai-gateway-realtime-voice-speech.md` nor `blog-vercel-ai-sdk-7-release.md` mentions a no-code playground for trying realtime voice models. This lowers the evaluation cost for a team deciding whether to adopt `xai/grok-voice-think-fast-1.0` versus `openai/gpt-realtime-2` — they can compare the two directly in-browser before writing any integration code.

## Concrete Artifacts

### Available models table (verbatim)

```
Capability | Models
Realtime voice | xai/grok-voice-think-fast-1.0
Text to speech | xai/grok-tts
Speech to text | xai/grok-stt

Source: https://vercel.com/changelog/xai-grok-audio-models-now-available-on-vercel-ai-gateway
```

### Realtime token route + browser hook (verbatim)

```typescript
// app/api/realtime/token/route.ts
import { gateway } from '@ai-sdk/gateway';

export async function POST() {
  const { token, url } = await gateway.experimental_realtime.getToken({
    model: 'xai/grok-voice-think-fast-1.0',
  });
  return Response.json({ token, url, tools: [] });
}
```

```typescript
'use client';
import { experimental_useRealtime as useRealtime } from '@ai-sdk/react';
import { gateway } from '@ai-sdk/gateway';

// Inside a client component:
const { status, connect, startAudioCapture } = useRealtime({
  model: gateway.experimental_realtime('xai/grok-voice-think-fast-1.0'),
  api: { token: '/api/realtime/token' },
  sessionConfig: { turnDetection: { type: 'server-vad' } },
});
// Call connect(), then startAudioCapture(stream) to start talking.
```
Source: https://vercel.com/changelog/xai-grok-audio-models-now-available-on-vercel-ai-gateway

### Text-to-speech example with `xai/grok-tts` (verbatim)

```typescript
import { generateSpeech } from 'ai';
import { writeFile } from 'node:fs/promises';

const result = await generateSpeech({
  model: 'xai/grok-tts',
  text: 'Thanks for trying out AI Gateway.',
  voice: 'eve',
  outputFormat: 'mp3',
});
await writeFile('speech.mp3', result.audio.uint8Array);
```
Source: https://vercel.com/changelog/xai-grok-audio-models-now-available-on-vercel-ai-gateway

### Speech-to-text example with `xai/grok-stt` (verbatim)

```typescript
import { transcribe } from 'ai';
import { readFile } from 'node:fs/promises';

const result = await transcribe({
  model: 'xai/grok-stt',
  audio: await readFile('audio.mp3'),
});
console.log(result.text);
```
Source: https://vercel.com/changelog/xai-grok-audio-models-now-available-on-vercel-ai-gateway

### Contradicting reference-doc excerpt (verbatim, for issue #2282)

```
Text to speech supports OpenAI speech models only.

Last updated: June 20, 2026
Source: https://vercel.com/docs/ai-gateway/modalities/text-to-speech
(re-fetched live 2026-07-28, page unrevised since the date stamped above)
```

## Cross-References

### Cross-reference verification notes
`blog-vercel-ai-gateway-realtime-voice-speech.md` and `blog-vercel-ai-sdk-7-release.md`
were re-read in full during this extraction (MINER.md §4b); every claim number
cited above was located and confirmed against each note's own numbered
`### Claim N:` headings in document order before writing this section.

- **Corroborates**:
  - `blog-vercel-ai-gateway-realtime-voice-speech.md` Claim 1 ("the same
    observability, spend controls, and bring-your-own-key support as
    text, image, and video models... with no markup or platform fees"):
    this source's Claim 1 restates the same "same routing, observability,
    and spend controls" framing specifically for xAI's audio models.
  - `blog-vercel-ai-gateway-realtime-voice-speech.md` Claim 4
    (server-mints-token architecture for realtime) and Claim 7 (naming
    `xai/grok-voice-think-fast-1.0` as a realtime model, "speech-to-speech
    only"): this source's Claim 2 and Claim 5 independently confirm the
    same model ID and the same token-minting architecture applied to it.
  - `blog-vercel-ai-gateway-realtime-voice-speech.md`'s speech-to-text
    example (`openai/whisper-1` via `transcribe()`): this source's Claim 7
    confirms the identical `transcribe()` function signature works
    unchanged against `xai/grok-stt`.

- **Contradicts**:
  - `blog-vercel-ai-gateway-realtime-voice-speech.md` Claim 10 ("Text to
    speech supports OpenAI speech models only") is directly contradicted
    by this source's Claim 3/Claim 4 (`xai/grok-tts` shown as a working,
    named, non-OpenAI text-to-speech model). **Filed as contradiction
    issue #2282** — see Claim 4 above for the full analysis. Do not treat
    either side as settled guide guidance until #2282 is resolved and
    logged in CONTRADICTIONS.md.

- **Extends**:
  - `blog-vercel-ai-sdk-7-release.md` Claim 13 ("Realtime (experimental):
    Browser-to-provider WebSocket sessions for OpenAI, Google, and xAI...
    normalized routing through AI Gateway"): this source's Claim 5 and
    Claim 2 supply the concrete xAI-specific model ID and worked example
    for the xAI branch of that claim, which the AI SDK 7 changelog itself
    only named at the provider level (not model-ID level).
  - `blog-vercel-ai-gateway-realtime-voice-speech.md` Claim 7 (per-provider
    capability variance within the realtime modality: xAI's model
    "supports speech-to-speech only," no transcription/translation): this
    source's Claim 6 flags a second, unconfirmed instance of the same
    pattern (xAI's realtime example omits the `voice` sessionConfig
    parameter the OpenAI example sets) without asserting it as a
    documented restriction, since this source alone does not state
    whether the omission is a capability gap or a code-example choice.

- **Novel**:
  - **`xai/grok-tts` and `xai/grok-stt` as named AI Gateway model
    identifiers** (Claim 2): neither appears anywhere else in this corpus.
  - **The voice value `'eve'` for `xai/grok-tts`** (Claim 3): the first
    non-OpenAI voice-name value documented in this corpus, evidence that
    xAI's TTS model has its own voice catalog rather than reusing OpenAI's
    naming.
  - **A no-code playground for trying realtime voice models in-browser**
    (Claim 8): not mentioned in either prior AI-Gateway-audio source note.
  - **A live, checkable contradiction between two of Vercel's own
    first-party documents on the same modality** (Claim 4): the first
    instance in this corpus of a *product's own changelog and its own
    reference docs* disagreeing with each other, as opposed to two
    different third-party sources disagreeing.

## Guide Impact

- **Chapter 02 (Harness Engineering) — retract the "OpenAI-only" TTS
  framing pending #2282**: The existing note's Guide Impact language
  (informed by its Claim 10) should not be carried into the guide as "AI
  Gateway text-to-speech is OpenAI-only" without a caveat. This source
  provides working, first-party counter-evidence (`xai/grok-tts`) that at
  minimum some non-OpenAI TTS models are available. The guide should treat
  this as an open, dated question — "as of late June 2026, xAI TTS support
  was announced but Vercel's own reference docs had not been updated to
  reflect it a month later" — rather than asserting either side is settled,
  per contradiction issue #2282.

- **Chapter 02 (Harness Engineering) — provider-agnostic architecture
  holds across models**: Add this source's Claims 5 and 7 as further
  confirmation that AI Gateway's realtime token-minting and
  `transcribe()`/`generateSpeech()` interfaces are genuinely
  provider-agnostic at the code level — switching from OpenAI's to xAI's
  models for realtime and speech-to-text requires only a `model` string
  change, no different integration pattern. This strengthens (does not
  merely repeat) the existing note's architectural guidance.

- **Chapter 02 (Harness Engineering) — evaluation cost**: Note the
  in-browser playground (Claim 8) as a lower-friction way for a team to
  compare `xai/grok-voice-think-fast-1.0` against `openai/gpt-realtime-2`
  before committing to an integration, worth mentioning alongside any
  guidance on model selection for voice agents.

## Extraction Notes

1. **Raw HTML fetched and parsed directly, not WebFetch-summarized, per
   MINER.md §2a.** The changelog page and the `text-to-speech` reference
   docs page were both retrieved via direct `curl` with a browser
   user-agent, the `<article>` element isolated with BeautifulSoup, and
   the resulting plain text read in full. Every `Quote` field above was
   located character-for-character in that locally-parsed text. Author
   names and publish/modified dates were verified against the page's own
   JSON-LD (`datePublished`, `dateModified`, `author` array), not inferred
   from a WebFetch summary.
2. **No additional linked pages followed.** Unlike
   `blog-vercel-ai-gateway-realtime-voice-speech.md`, this changelog entry
   is short and self-contained (four code examples, no unexplained
   mechanism requiring a linked quickstart to understand), so per MINER.md
   §1 no further pages beyond the changelog itself were needed for the
   changelog's own claims. The one exception is Claim 4, where the
   `text-to-speech` reference docs page was deliberately fetched
   specifically to check for a contradiction the Prospector's triage
   comment flagged — that fetch is documented above, not a general
   "follow linked pages" pass.
3. **Contradiction filed, not resolved, per MINER.md §4a.** Issue #2282
   filed for the OpenAI-only-vs-`xai/grok-tts` conflict identified in
   Claim 4. This note does not pick a winner; Guide Impact above
   deliberately hedges pending resolution.
4. **Confidence calibration: emerging.** Most individual claims are rated
   "settled" (first-party, unambiguous statements/code from the model
   vendor's infrastructure partner), but the note's overall confidence is
   "emerging" because: (a) this is a single vendor's own brief changelog
   with no independent verification, benchmark, or named customer; (b)
   the source's headline claim about `xai/grok-tts` availability is in
   live, unresolved conflict with Vercel's own separate reference
   documentation (Claim 4); and (c) several details a practitioner would
   need (xAI TTS voice catalog beyond `'eve'`, pricing, rollout/catalog
   gating for `xai/grok-tts` specifically) are not covered by this source
   at all.
