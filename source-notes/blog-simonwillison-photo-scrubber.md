---
source_url: https://simonwillison.net/2026/Sep/29/photo-scrubber/
source_type: blog-post
title: "Photo Scrubber — local face blur & metadata removal"
author: Simon Willison
date_published: 2026-09-29
date_extracted: 2026-10-07
last_checked: 2026-10-07
status: current
confidence_overall: anecdotal
issue: "#3943"
---

# Photo Scrubber — local face blur & metadata removal

> Simon Willison had GPT-6 Astra build a single-file, browser-only tool that detects and blurs faces (MediaPipe BlazeFace via WebAssembly) and strips photo metadata; the post is three sentences, but the linked commit exposes the actual prompts and a ~191-line generated artifact whose design (CSP lockdown, structural metadata removal, verify-before-download) is the substantive content.

## Source Context

- **Type**: blog-post (Willison's "Tool" category: a short note linking to a live tool and the commit that added it).
- **Author credibility**: Simon Willison is a trusted-feed author already heavily represented in this corpus (Django, Datasette, `llm`). Here he is reporting on a tool he commissioned and published himself, so the claims are first-hand; the commit makes them checkable.
- **Scope**: The post itself covers motivation (photo of protesters), the model used, and the ML stack. It says nothing about prompts, review of generated code, or testing. Those details come from the linked commit `simonw/tools@aa733ec` (patch fetched and read), which is a secondary artifact and is labelled as such below. Not covered anywhere: accuracy of face detection, whether the metadata stripping was independently verified, or any human code review.

## Extracted Claims

### Claim 1: The tool was motivated by a personal privacy preference about identifiable strangers in photos
- **Evidence**: First-person account of a specific incident (a photograph of protesters).
- **Confidence**: anecdotal
- **Quote**: "I took a photograph of some protesters, then thought about how I don't like sharing photographs of strangers with identifiable faces."
- **Our assessment**: A genuine, concrete use case rather than a demo. Shows the "personal itch → single-purpose tool" pattern in a privacy setting. Nothing to dispute; just a motivation.

### Claim 2: The whole tool was produced by prompting GPT-6 Astra rather than hand-writing it
- **Evidence**: Author statement; the commit message of the linked commit records the prompts (see Concrete Artifacts), including a ChatGPT share link.
- **Confidence**: emerging
- **Quote**: "I had GPT-6 Astra build this experimental tool that would identify faces and automatically blur them out."
- **Our assessment**: Credible, and the commit message corroborates it. Note the word "experimental" — the author does not claim the output was audited. The commit shows only two user turns (a spec prompt and a "Ditch the eyebrow and the marketing copy" cleanup), i.e. very little iteration for a ~191-line, feature-rich file.

### Claim 3: Face detection runs client-side using MediaPipe compiled to WebAssembly plus BlazeFace
- **Evidence**: Author statement; the commit code imports `vision_bundle.mjs` from jsDelivr pinned at `@mediapipe/tasks-vision@0.10.21` and loads `blaze_face_short_range.tflite` with `delegate:'CPU'`.
- **Confidence**: settled
- **Quote**: "It uses Google's MediaPipe C++ library, compiled to WebAssembly via @mediapipe/tasks-vision, plus the BlazeFace face detection model."
- **Our assessment**: Verified against the commit. Caveat the post does not mention: the library and model weights are fetched at runtime from `cdn.jsdelivr.net` and `storage.googleapis.com`, so "local" applies to the photo bytes, not to the tool's dependencies (it needs network on first use).

### Claim 4: All processing happens in the browser and photos never leave the device
- **Evidence**: Tool description on the post; in the commit, a `Content-Security-Policy` meta tag restricts `connect-src` to two hosts (jsDelivr, storage.googleapis.com), plus `form-action 'none'`, `default-src 'none'`, `base-uri 'none'`, and a header comment that no analytics/storage are used.
- **Confidence**: emerging
- **Quote**: "All processing occurs in the browser—photos never leave your device."
- **Our assessment**: Plausible and better supported than most such claims because the generated page enforces it with a CSP (our reading of the code, not something the post states). Still a self-attested claim; a CSP allowing `script-src 'unsafe-inline'` and a third-party CDN means a compromised CDN could in principle exfiltrate. Worth noting as a limit of "local-first" guarantees.

### Claim 5: The tool combines automatic detection with manual redaction and adjustable blur, and exports with all personal metadata removed
- **Evidence**: Tool description; commit code implements draw/select tools, undo/redo (history capped at 60), blur strength/padding sliders, a solid-fill mode, a "hold to compare original" button, a "reviewed" checkbox gating export, and a deep-scan tiling pass.
- **Confidence**: emerging
- **Quote**: "The tool automatically detects faces using machine learning, allows manual redaction with adjustable blur strength, and exports cleaned images with all personal metadata stripped."
- **Our assessment**: Matches the code. The design acknowledges that ML detection is not trustworthy alone (human review step required before export is enabled) — a good human-in-the-loop pattern for safety-relevant ML output.

### Claim 6 (from the linked commit, not the post text): Metadata is removed structurally, by dropping whole containers, and the output is verified before download
- **Evidence**: Code comments and functions in the commit: `sanitizeBytes` keeps only non-metadata JPEG/PNG segments/chunks (`PNG_KEEP` whitelist: IHDR, PLTE, tRNS, IDAT, IEND), and `verifyBytes` throws if metadata or trailing bytes remain, blocking download.
- **Confidence**: anecdotal (one generated file, no independent test results shown; a `?test` hook exposes helpers for local tests but no test run is reported)
- **Quote**: "No EXIF parser is needed because the export removes entire metadata containers instead of editing individual tags." (code comment in commit; the actual comment text reads "No EXIF parser is needed because\n   the export removes entire metadata containers instead of editing individual tags.")
- **Our assessment**: Allowlist-over-denylist is the right design for scrubbing, and the fail-closed verify step is notable for LLM-generated code. But we have no evidence it was exercised against real files. Treat as an interesting design the model produced, not as a validated tool.

## Concrete Artifacts

From the commit message of `simonw/tools@aa733ecc3458d5703e3b40c84507ae362f5fb294` (https://github.com/simonw/tools/commit/aa733ecc3458d5703e3b40c84507ae362f5fb294), the entire prompt history:

```
> Build an HTML page that loads necessary dependencies from a CDN and implements a tool which lets the user select a photo and then both strips EXIF data from that photo and also finds and blurs any faces in that photo - discuss implementation options first

> Ditch the eyebrow and the marketing copy

https://chatgpt.com/share/6abbeb1d-4d64-83e8-bf7b-3355ea405df7
```

CSP generated into the page (same commit, `photo-scrubber.html`):

```
default-src 'none'; script-src 'unsafe-inline' 'wasm-unsafe-eval' https://cdn.jsdelivr.net; connect-src https://cdn.jsdelivr.net https://storage.googleapis.com; img-src blob: data:; style-src 'unsafe-inline'; worker-src blob:; base-uri 'none'; form-action 'none'; object-src 'none'
```

Constants and header comment from the same file:

```
const CDN = 'https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.21';
const MAX_BYTES = 75 * 1024 * 1024;
const SOFT_PIXELS = 24_000_000, SOFT_EDGE = 8192, HARD_PIXELS = 64_000_000, HARD_EDGE = 16384;
/* 0.10.21 uses hard-coded short-range anchors; do not swap in full-range weights. */
```

Post metadata: published 29 September 2026; tool at https://tools.simonwillison.net/photo-scrubber.

## Cross-References

- **Corroborates**: `blog-simonwillison-blend-url-viewer.md` — same pattern of Willison commissioning a single-file, fully client-side browser tool from a frontier model (see its Claim 1, client-side parsing with no server step) and publishing it under tools.simonwillison.net.
- **Contradicts**: None found.
- **Extends**: `blog-simonwillison-gpt6-astra-launch.md` — gives a small, concrete example of GPT-6 Astra used for code generation after launch (that note's claims concern launch, pricing and benchmarks, e.g. its Claims 1–4, not this kind of use). `blog-simonwillison-nilay-patel-ar-privacy.md` — that note (Claim 3) argues continuous camera data ends up in the cloud because on-device chips are inadequate; Photo Scrubber is a small counter-example of useful vision ML running fully on-device in a browser (for single still images, not real-time video, so it is not a direct rebuttal).
- **Novel**: A privacy-redaction tool (face blur plus metadata stripping) in the corpus; the use of a CSP as an enforcement mechanism for a "nothing leaves the device" claim; allowlist-based metadata stripping with a fail-closed verification step; the commit message used as a complete record of an AI-built tool's prompts.

## Guide Impact

- **Chapter 03 / Chapter 04 (tool building)**: A usable small example for "single-prompt tool builds": two prompts, one 191-line file, published. The first prompt ends with "discuss implementation options first", a cheap plan-before-code instruction worth listing among prompting patterns. Evidence is anecdotal (single instance), so suggest as illustrative, not as a recommendation.
- **Chapter 05 (privacy/safety)**: Could cite the CSP-as-guarantee idea and the "require human review before export" gate as patterns for local-first tools handling sensitive data, with the caveat that CDN-loaded scripts weaken the guarantee. No existing chapter claim is contradicted.
- The guide should not claim the tool is verified secure; the post and commit show no testing or code review.

## Extraction Notes

- The post body is three short paragraphs plus a tool blurb; read in full. Followed the linked commit patch (the one substantive link) and read the full generated HTML/JS. Did not follow the ChatGPT share link or the live tool. The MediaPipe docs link was not followed.
- Claim 6's quote is a code comment from the commit, not the blog post; the formatted quote in the Quote field is the comment text with its line break joined by a space, and the exact original is given alongside it. Claims 4–6 interpretations of the code are the Miner's reading.
- Source is thin by nature; confidence kept at anecdotal.
