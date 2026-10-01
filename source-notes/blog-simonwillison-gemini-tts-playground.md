---
source_url: https://simonwillison.net/2026/Sep/23/gemini-tts-playground/
source_type: blog-post
title: "Tool: Gemini 3.8 TTS Playground"
author: Simon Willison
date_published: 2026-09-23
date_extracted: 2026-10-01
last_checked: 2026-10-01
status: current
confidence_overall: anecdotal
issue: "#3828"
---

# Tool: Gemini 3.8 TTS Playground

> Willison's short "beat" on Google's Gemini 3.8 TTS models records one vibe-coded, bring-your-own-key browser tool, one agent-generated multi-speaker script, and one cost/latency datapoint (2.74 cents, ~20 s for 1m 18s of audio) — thin on AI-engineering practice, useful mainly as a corroborating datapoint.

## Source Context

- **Type**: blog-post (link-blog "Tool" entry; about six short paragraphs plus an audio clip).
- **Author credibility**: Simon Willison, creator of Django and Datasette and the corpus's most frequent practitioner voice on LLM tooling. Hands-on: he built and hosts the tool.
- **Scope**: Covers the existence of two new Google TTS models, the playground he built, a multi-speaker demo, and one cost/latency measurement. Does **not** cover: the prompt used to build the tool, the API request shape, voice quality evaluation, or any comparison against other TTS providers.

## Extracted Claims

### Claim 1: Google released two new TTS models, with 2,000+ voices and custom voice creation from a 30-second sample
- **Evidence**: Willison's statement of the launch, quoting Google's marketing language; no independent verification.
- **Confidence**: anecdotal (vendor claim relayed second-hand)
- **Quote**: "They come with a library of over 2,000 voices, plus the ability to create a custom voice with \"just a 30-second audio sample of your voice or a voice you have the rights to use\"."
- **Our assessment**: Product-announcement fact, not engineering practice. The rights caveat in Google's wording is the only governance-relevant detail. Model IDs given: `gemini-3.8-flash-tts` and `gemini-3.8-flash-lite-tts`.

### Claim 2: The playground was vibe-coded with GPT-6 Astra and relies on the Gemini API's open CORS policy so no backend is needed
- **Evidence**: Author's first-person account; the tool is live and bring-your-own-key.
- **Confidence**: anecdotal
- **Quote**: "I vibe coded this bring-your-own-key playground interface with GPT-6 Astra, taking advantage of the open CORS policy of the underlying Gemini API."
- **Our assessment**: Credible and consistent with Willison's pattern of single-file browser tools. The security tradeoff (user's API key held in the browser) is implicit and not discussed here; see the Live note's Claim 13.

### Claim 3: The API makes multi-character conversations easy, with a distinct voice and style instruction per speaker
- **Evidence**: Author's observation, demonstrated by a two-pelican clip.
- **Confidence**: anecdotal
- **Quote**: "A notable feature of the API is that it makes it easy to define a full conversation between multiple characters, each with different voices and voice style instructions."
- **Our assessment**: Plausible; no request payload is shown, so it cannot be checked from this source.

### Claim 4: Agents can chain — Claude wrote the script and generated a URL that renders it in the tool
- **Evidence**: Demo clip description.
- **Confidence**: anecdotal
- **Quote**: "I had Claude 4.5 Opus write the script and generate a URL to render it using the tool."
- **Our assessment**: The tool description says compose settings are saved in bookmarkable URLs, which makes the tool agent-drivable: state-in-URL is an interface an agent can generate without browser automation. Inferred from the description; the post doesn't state the URL format.

### Claim 5: Cost and latency datapoint for Flash TTS
- **Evidence**: Single measured run, not Flash-Lite.
- **Confidence**: anecdotal (n=1)
- **Quote**: "It took ~20 seconds to generate 1m 18s of audio using Gemini 3.8 Flash TTS (not the cheaper Flash-Lite), at a cost of 2.74 cents."
- **Our assessment**: Roughly 3.9x faster than real-time at about 2.1 cents/minute. One sample; the script length and settings are unknown.

## Concrete Artifacts

```
Tool description (from the post): "Test and experiment with Google's Gemini 3.8
text-to-speech API through an interactive playground where you can compose
single-voice narration or multi-speaker conversations, preview the generated
audio, and explore request and response details. Save your compose settings to
bookmarkable URLs for easy sharing..."
Models: gemini-3.8-flash-tts, gemini-3.8-flash-lite-tts
Measured: ~20 s generation, 1m 18s audio, 2.74 cents (Flash TTS)
```

## Cross-References

- **Corroborates**: `blog-simonwillison-gemini-live-websocket-audio.md` Claim 2 (Willison has an agentic coding tool build a browser client for a fresh Gemini API) and Claim 13 (key handled in the browser, BYOK); `blog-simonwillison-cors-chat.md` (browser-direct API calls enabled by open CORS).
- **Contradicts**: None found.
- **Extends**: `blog-simonwillison-gemini-live-websocket-audio.md` — same author, same model family, but static REST TTS rather than the WebSocket Live API. The Prospector's REST-vs-WebSocket distinction is not stated in the post; it is inferred.
- **Novel**: TTS pricing/latency datapoint; per-speaker voice/style instructions; the agent-writes-script-then-emits-render-URL pattern.

## Guide Impact

- **Ch02 / Ch05**: At most a minor example: a state-in-URL tool lets one agent hand a renderable artifact to a human reviewer. Not enough on its own to justify guide changes.
- **Ch06**: BYOK browser tools with open-CORS APIs shift key exposure to the client. This post adds no new evidence beyond the Live note.

## Extraction Notes

- The post is very thin (the Prospector's pre-screen rejection also noted this). Read in full. I could not retrieve the tool's source (`tools.simonwillison.net/gemini-tts` is protected by a CSP, and the raw GitHub guess `simonw/tools/main/gemini-tts.html` returned 14 bytes, i.e. not found), so the request shape and build transcript were not examined.
- Claims about "Ch03 verification" and a REST-vs-WebSocket protocol comparison in the triage comment are not supported by the post's text. Overall confidence is therefore anecdotal.
