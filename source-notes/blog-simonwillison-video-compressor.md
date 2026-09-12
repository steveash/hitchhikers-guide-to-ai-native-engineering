---
source_url: https://simonwillison.net/2026/Sep/7/video-compressor/
source_type: blog-post
title: "Tool: Video compressor"
author: Simon Willison
date_published: 2026-09-07
date_extracted: 2026-09-12
last_checked: 2026-09-12
status: current
confidence_overall: anecdotal
issue: "#3396"
---

# Tool: Video compressor

> A one-paragraph "beat" post in which Willison had Claude Fable 5.1 in Claude Code for web
> build, in a single delegation, a browser-only video compression tool (FFmpeg compiled to
> WebAssembly) to solve a narrow personal need — publishing an optimized phone-recorded demo
> video on his blog. The generated tool independently adds production-quality codec-compatibility
> defaults, a self-disclosed performance caveat, and an embed-code generator that go beyond the
> literal one-sentence request.

## Source Context

- **Type**: blog-post (a "beat" — Willison's shortest link-blog post format, used for tool
  drops rather than long-form essays). The entire body text is one sentence plus a screenshot;
  there is no workflow narrative, prompt transcript, or reflection in the post itself.
- **Author credibility**: Simon Willison is the creator of Django, maintainer of 200+ tools at
  `tools.simonwillison.net`, and a `trusted-feed` source in this repo (see
  [[blog-simonwillison-liteparse-browser]] and [[blog-simonwillison-equal-earth-map-projection]]
  for his established credibility as a first-person AI-tooling practitioner). This post is
  thinner than his typical workflow write-ups, but the linked artifact — the deployed tool at
  `tools.simonwillison.net/video-compressor` — is publicly inspectable and was read directly for
  this note.
- **Scope**: Covers a single act of tool creation — a client-side video compressor built by
  Claude Fable 5.1 in "Claude Code for web" in one delegation. Does NOT cover: the underlying
  prompt(s) beyond the one sentence quoted in the post, any iteration or debugging narrative, or
  code review practices. The post links directly to the Claude Code session
  (`claude.ai/code/session_01QHTdJZ4xg6TZfDXCmuvAE9`), but that link requires authentication and
  returned HTTP 403 on automated fetch — its contents (the actual multi-turn prompt/build
  transcript, if any) could not be extracted for this note.

## Extracted Claims

### Claim 1: Willison delegated the entire tool build to Claude Fable 5.1 in "Claude Code for web" from a single narrative request, framed as solving a specific personal need rather than a general product goal
- **Evidence**: Direct first-person statement in the post body naming the model, the product surface ("Claude Code for web"), and the motivating need (publishing an optimized version of a phone-recorded demo video).
- **Confidence**: anecdotal (single example, self-reported, no prompt transcript beyond the paraphrase in the post itself)
- **Quote**: "I recorded a short demo video of my Equal Earth animation on my phone and wanted to publish an optimized version of that video (using FFMPEG) on my blog, so I had Claude Fable 5.1 in Claude Code for web build me this tool using the WebAssembly build of FFMPEG."
- **Our assessment**: This is another data point in Willison's recurring "notice a narrow personal need → delegate the whole tool build to an AI coding agent in one shot → publish the result" loop, already well established in this corpus (e.g. [[blog-simonwillison-liteparse-browser]], [[blog-simonwillison-equal-earth-map-projection]]). The demo video referenced here is the Equal Earth animation from the same day's other beat post, making this a directly-linked, same-day pair of one-shot tool builds from two different vendors (Claude here; GPT-6 Astra in the Equal Earth post).

### Claim 2: The generated tool processes video entirely client-side, with no server uploads, despite handling a workload (video transcoding) that would conventionally be done server-side
- **Evidence**: Stated both in the blog post's link metadata and independently in the deployed tool's own introductory copy.
- **Confidence**: settled (consistent statement across the blog post and the tool's own UI text; verifiable by inspecting the tool's network behavior/source, which contains no upload endpoint)
- **Quote**: "Open a video and this tool encodes several smaller versions of it entirely in your browser, using FFmpeg compiled to WebAssembly. Nothing is uploaded anywhere." (tool intro text, tools.simonwillison.net/video-compressor)
- **Our assessment**: This continues a pattern already documented across several Willison browser-native tool builds ([[blog-simonwillison-liteparse-browser]] Claim 12's "almost non-existent" blast radius reasoning for static, in-browser, no-data-transfer tools). A video compressor is a heavier client-side workload than a PDF parser or map-projection animation, and the tool still holds to the no-upload, no-backend model — evidence that WASM-compiled native libraries (FFmpeg here, Tesseract/PDF parsing elsewhere) are making increasingly resource-intensive tasks tractable as fully client-side, zero-infrastructure AI-generated tools.

### Claim 3: The tool ships five named quality/size presets with specific, differentiated encoding parameters (resolution, CRF, audio bitrate) rather than a single one-size-fits-all compression setting
- **Evidence**: The tool's own JavaScript source defines a `DEFAULT_VARIANTS` array with five presets, each independently tuned.
- **Confidence**: settled (directly observed in the fetched tool source, `tools.simonwillison.net/video-compressor`)
- **Quote**: "const DEFAULT_VARIANTS = [\n  { id: 'xl', name: 'Largest', shortSide: 1080, crf: 22, audio: 128 },\n  { id: 'l', name: 'Large', shortSide: 720, crf: 23, audio: 128 },\n  { id: 'm', name: 'Medium', shortSide: 720, crf: 27, audio: 96 },\n  { id: 's', name: 'Small', shortSide: 480, crf: 26, audio: 96 },\n  { id: 'xs', name: 'Smallest', shortSide: 360, crf: 28, audio: 64 },\n];"
- **Our assessment**: This is a concrete, checkable example of the model producing a genuinely useful default configuration space (five distinct resolution/quality/bitrate tiers spanning a sensible range) from a one-sentence request, rather than a minimal single-setting tool. The tool also lets users add fully custom presets (short side, CRF, audio bitrate), so the five defaults are a starting point, not a hard limit.

### Claim 4: In the demonstrated run, the tool generated five encoded versions of a real video in 11.8 seconds, with the smallest output reaching 48% of the original file size
- **Evidence**: Screenshot alt text embedded in the blog post, describing the tool's UI state after a real compression run.
- **Confidence**: anecdotal (single demonstrated run, one source video, no systematic benchmark across video types/lengths)
- **Quote**: "A green \"Generate versions\" button reads \"Done: 5 versions in 11.8s.\" Below, \"Results, smallest first\" shows three video players: Smallest at 145 KB (48% of original), Medium at 241 KB (79%), and Small at 264 KB (87%), each with a Download .mp4 button and a collapsible ffmpeg command."
- **Our assessment**: This is the only quantitative evidence in the post of the tool actually working end-to-end. It's a single demonstration on an unspecified (likely short, low-resolution phone-recorded) source video, so the 11.8-second figure and the specific compression ratios should not be generalized to other video sizes — the tool's own documentation (Claim 6) explicitly warns that WASM encoding is much slower than native FFmpeg for longer or higher-resolution input.

### Claim 5: The generated tool independently applies a set of production-oriented codec-compatibility defaults (H.264 Main profile, 8-bit 4:2:0 color, even dimensions, automatic H.264 level selection, AAC-LC audio, MP4 faststart, single-track output, baked-in rotation correction) that were not spelled out in the one-sentence build request
- **Evidence**: Directly observed in the deployed tool's "How the output files are made compatible" info panel.
- **Confidence**: settled (directly observed in the fetched tool source)
- **Quote**: "H.264 video (libx264) in the Main profile by default, 8-bit 4:2:0 colour (yuv420p), even width and height, capped at 1080p and 60 fps. The H.264 level is picked automatically from the resolution and frame rate. AAC-LC audio at 44.1 or 48 kHz, downmixed to stereo when the source has more channels. MP4 container with the index moved to the front (+faststart) so playback can begin before the file has fully downloaded. Only the first video and first audio track are kept. Rotation metadata from phones is baked into the pixels so every player shows the video the right way up." (tool info panel, tools.simonwillison.net/video-compressor)
- **Our assessment**: The original request was "build me this tool using the WebAssembly build of FFMPEG" — it did not specify H.264 profile choice, chroma subsampling, faststart, or phone rotation-metadata handling. These are exactly the kind of "boring but correct" defaults a video-engineering practitioner would know to apply (e.g., phone-shot vertical video needs rotation baked in or it plays sideways in some players; faststart matters for web playback; Main profile balances compatibility and file size). This is evidence that a narrowly-scoped, single-sentence prompt for a well-understood domain (video transcoding for web) can still surface non-trivial domain-correct defaults without the user enumerating them — a positive data point for the "trust the model to backfill standard practice" question in low-blast-radius, well-documented technical domains.

### Claim 6: The tool discloses its own performance limitation directly in its shipped UI copy — WASM-compiled FFmpeg runs on a single CPU core and is much slower than native FFmpeg — along with a built-in workaround
- **Evidence**: Directly observed in the deployed tool's info panel text.
- **Confidence**: settled (directly observed in the fetched tool source)
- **Quote**: "Encoding runs on a single CPU core inside WebAssembly, so it is much slower than a native ffmpeg. Long or high resolution videos can take a while: use the \"first N seconds\" option to compare settings quickly, then encode the full version of the one you like. The ffmpeg engine (about 32 MB) is downloaded once and cached by your browser." (tool info panel, tools.simonwillison.net/video-compressor)
- **Our assessment**: This is the second in-corpus instance (after [[blog-simonwillison-equal-earth-map-projection]] Claim 3's "Intermediate frames blend projected coordinates; they are not equal-area" disclosure, built by a different vendor's model the same day) of a Willison vibe-coded tool surfacing its own known limitation directly in end-user-facing copy, rather than silently underperforming or overpromising. The tool also ships a concrete mitigation (the "first N seconds" quick-comparison mode) rather than just a warning. Two independent same-day examples, from two different model vendors, is enough to flag this as a repeatable, promptable pattern worth naming explicitly in the guide rather than a one-off.

### Claim 7: The generated tool includes a full "embed on a web page" feature — ready-to-paste HTML with an extracted poster-frame JPEG and lazy-load semantics — that was not part of the literal one-sentence build request
- **Evidence**: Directly observed in the deployed tool's embed-card UI and its accompanying poster-frame extraction feature.
- **Confidence**: settled (directly observed in the fetched tool source)
- **Quote**: "Upload the video and the poster JPEG alongside your page, then paste this in. It uses the first video shown in the results above. preload=\"none\" means the browser only shows the poster image and does not download any of the video until someone presses play." (tool embed card, tools.simonwillison.net/video-compressor)
- **Our assessment**: The stated need was "publish an optimized version of that video... on my blog" — the model appears to have inferred that publishing a compressed video to a blog also requires a poster image (extracted as the first frame, saved as JPEG) and copy-pasteable embed markup with lazy-loading (`preload="none"`) rather than stopping at "produce a smaller .mp4 file." This is a concrete example of scope expansion that stays tightly coupled to the user's actual underlying goal (publishing to a blog) rather than wandering into unrelated feature territory — worth distinguishing from unwanted scope creep in the guide's treatment of one-shot delegation.

### Claim 8: The post links directly to the specific Claude Code session that produced the tool, continuing Willison's practice of citing verifiable session artifacts as evidence for his tool-building claims — though this particular session link is not publicly accessible
- **Evidence**: The post embeds a hyperlink on the phrase "build me this tool" pointing to `claude.ai/code/session_01QHTdJZ4xg6TZfDXCmuvAE9`. An automated fetch of that URL for this note returned HTTP 403.
- **Confidence**: anecdotal (link presence confirmed; contents not independently verifiable)
- **Quote**: (no direct quote; see paraphrase above — the link itself, not additional prose, is the evidence)
- **Our assessment**: Unlike [[blog-simonwillison-liteparse-browser]], where the linked Claude Code transcript was publicly exportable and directly quoted, or [[blog-simonwillison-equal-earth-map-projection]], where the linked ChatGPT share page rendered only a client-side shell, this session link returns an outright 403 — Claude Code for web sessions appear to require authentication to view, unlike some GitHub-hosted or export-based transcripts. This is a minor but practically relevant finding for anyone trying to independently audit Willison's (or others') Claude-Code-for-web-linked claims: the link is real and specific, but not currently a publicly verifiable artifact the way a public GitHub commit or exported transcript would be.

## Concrete Artifacts

### Full blog post body text (verbatim, entire post)

```
Source: https://simonwillison.net/2026/Sep/7/video-compressor/
Posted 7th September 2026 at 6:29 pm
Tags: ffmpeg, video, webassembly, claude, claude-code, claude-mythos-fable

Title: Video compressor

Beat link description:
"Compress videos in your browser using FFmpeg compiled to WebAssembly. Upload
a video file to generate multiple encoded versions with different quality
settings and output sizes, then compare and download the smallest file that
meets your needs. All processing happens locally with no uploads to external
servers."

Body:
"I recorded a short demo video of my Equal Earth animation on my phone and
wanted to publish an optimized version of that video (using FFMPEG) on my
blog, so I had Claude Fable 5.1 in Claude Code for web build me this tool
using the WebAssembly build of FFMPEG."

Screenshot alt text:
"Screenshot of a video compression web tool. Under \"Versions to generate\"
is a table of five presets (Largest, Large, Medium, Small, Smallest) with
output sizes of 854×370 or 640×276, CRF quality settings from 22 to 28, and
audio bitrates from 128 to 64 kbps, plus options for encoder speed, H.264
profile, 30 fps limit, stripping metadata, dropping audio, and encoding only
the first 10 seconds. A green \"Generate versions\" button reads \"Done: 5
versions in 11.8s.\" Below, \"Results, smallest first\" shows three video
players: Smallest at 145 KB (48% of original), Medium at 241 KB (79%), and
Small at 264 KB (87%), each with a Download .mp4 button and a collapsible
ffmpeg command."
```

### Default compression presets (verbatim, from the deployed tool's source)

```javascript
// Source: https://tools.simonwillison.net/video-compressor (view-source, fetched 2026-09-12)
const DEFAULT_VARIANTS = [
  { id: 'xl', name: 'Largest', shortSide: 1080, crf: 22, audio: 128 },
  { id: 'l', name: 'Large', shortSide: 720, crf: 23, audio: 128 },
  { id: 'm', name: 'Medium', shortSide: 720, crf: 27, audio: 96 },
  { id: 's', name: 'Small', shortSide: 480, crf: 26, audio: 96 },
  { id: 'xs', name: 'Smallest', shortSide: 360, crf: 28, audio: 64 },
];
```

### Output-compatibility rules (verbatim, tool's "info" panel)

```
Source: https://tools.simonwillison.net/video-compressor (view-source, fetched 2026-09-12)

How the output files are made compatible:
- H.264 video (libx264) in the Main profile by default, 8-bit 4:2:0 colour
  (yuv420p), even width and height, capped at 1080p and 60 fps. The H.264
  level is picked automatically from the resolution and frame rate.
- AAC-LC audio at 44.1 or 48 kHz, downmixed to stereo when the source has
  more channels.
- MP4 container with the index moved to the front (+faststart) so playback
  can begin before the file has fully downloaded.
- Only the first video and first audio track are kept. Rotation metadata
  from phones is baked into the pixels so every player shows the video the
  right way up.

Encoding runs on a single CPU core inside WebAssembly, so it is much slower
than a native ffmpeg. Long or high resolution videos can take a while: use
the "first N seconds" option to compare settings quickly, then encode the
full version of the one you like. The ffmpeg engine (about 32 MB) is
downloaded once and cached by your browser.
```

### Embed-code generator copy (verbatim, tool's embed card)

```
Source: https://tools.simonwillison.net/video-compressor (view-source, fetched 2026-09-12)

Embed on a web page
Upload the video and the poster JPEG alongside your page, then paste this
in. It uses the first video shown in the results above. preload="none"
means the browser only shows the poster image and does not download any of
the video until someone presses play.
```

### Technical constraints and settings surface (from the tool source)

```
Source: https://tools.simonwillison.net/video-compressor (view-source, fetched 2026-09-12)

MAX_INPUT_BYTES  = 1.5 GiB
WARN_INPUT_BYTES = 400 MB
CORE_VERSION     = 0.12.10  (@ffmpeg/core, loaded from cdn.jsdelivr.net)

Encoder speed options: ultrafast / superfast / veryfast (recommended) /
                        faster / fast / medium
H.264 profile options: main (recommended) / high / baseline
Additional options: limit to 30fps, strip metadata (location/camera/dates),
                     drop audio track, encode only first N seconds (default 10)
Custom preset builder: short side (px), CRF, audio bitrate (kbps)
```

## Cross-References

- **Corroborates**:
  - [[blog-simonwillison-equal-earth-map-projection]] Claim 3 (the tool's own UI copy
    discloses a known approximation limitation — "Intermediate frames blend projected
    coordinates; they are not equal-area"): Claim 6 of this note is an independent,
    same-day, different-vendor instance of the identical pattern — a vibe-coded tool's
    shipped copy honestly documenting its own limitation (WASM single-core slowness here,
    projection-accuracy here) rather than silently underperforming.
  - [[blog-simonwillison-liteparse-browser]] Claim 12 (static, in-browser, no-data-transfer
    tools have "almost non-existent" blast radius, justifying minimal review): Claim 2 of
    this note is another instance of the same no-upload, fully client-side architecture,
    now applied to a heavier workload (video transcoding rather than PDF text extraction).
- **Contradicts**: None identified.
- **Extends**:
  - [[blog-simonwillison-equal-earth-map-projection]]: That note and this one are the same
    day's (2026-09-07) two "Tool:" beat posts from Willison — the Equal Earth post is
    explicitly the source of the demo video this tool was built to compress (per Claim 1's
    quote: "I recorded a short demo video of my Equal Earth animation"). Read together they
    show a same-day, two-vendor pair of one-shot personal tool builds (GPT-6 Astra for the
    map projection; Claude Fable 5.1 for the video compressor), each solving a narrow need
    that arose directly from the other.
  - [[blog-simonwillison-liteparse-browser]]: Extends the "give an AI coding agent a single
    natural-language request, ship a browser-native tool built on a WASM-compiled native
    library" pattern (LlamaIndex/Tesseract there, FFmpeg here) to a new, more
    compute-intensive domain (video transcoding vs. PDF text extraction), with Claim 5's
    codec-compatibility defaults as a new example of a single-shot prompt still surfacing
    non-trivial domain-correct engineering decisions.
- **Novel**:
  - First corpus source documenting a Willison vibe-coded tool wrapping FFmpeg-compiled-to-WebAssembly
    specifically, and the first to document a full set of video-codec compatibility defaults
    (H.264 profile, chroma subsampling, faststart, rotation-metadata baking) chosen
    autonomously by the model for a one-sentence request.
  - The scope-expansion example in Claim 7 (poster-frame extraction + embed-code generation,
    inferred from the stated goal of "publish... on my blog" rather than requested outright)
    is a new example of goal-coupled (not unrelated) feature inference in a one-shot build —
    not documented elsewhere in the corpus at this level of specificity.
  - Claim 8 (the linked Claude Code session returning HTTP 403) is the first corpus note to
    record that a `claude.ai/code/session_...` link is not publicly viewable without
    authentication, unlike some other transcript/export mechanisms documented elsewhere in
    the corpus.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add as another concrete instance of the "notice a narrow
  personal need → delegate the entire tool build to an AI coding agent in one sentence →
  publish the result" loop already documented via [[blog-simonwillison-liteparse-browser]],
  [[blog-simonwillison-equal-earth-map-projection]], and other Willison `tools.simonwillison.net`
  entries. This instance is useful specifically because the "need" (compress a video for a
  blog post) arose directly from a sibling one-shot tool build the same day, illustrating how
  quickly these small AI-built tools can compound into solving each other's downstream needs.
- **Chapter 02 (Harness Engineering)**: Cite Claim 5 (autonomous codec-compatibility defaults)
  and Claim 7 (goal-coupled scope expansion — poster frame + embed code, inferred from "publish
  on my blog" rather than spelled out) as evidence that a narrowly-scoped, well-documented
  technical domain (web video encoding) allows a single-sentence prompt to still yield
  non-trivial, domain-correct engineering decisions without the user enumerating them. Useful
  as a positive counter-example when discussing how much a one-shot prompt needs to specify.
- **Chapter 03 (Verification)**: Add Claim 6 alongside [[blog-simonwillison-equal-earth-map-projection]]
  Claim 3 as a two-example, cross-vendor, same-day pattern: ask the agent to document known
  performance or accuracy limitations directly in the shipped tool's own UI copy, rather than
  relying on the author to remember to disclose them separately. Two independent same-day
  instances (different vendors, different domains) is a reasonable basis for a specific,
  named recommendation rather than treating it as a one-off anecdote.

## Extraction Notes

- **Source is a "beat"**: the entire blog post prose is one sentence (~50 words) plus a
  screenshot's alt text. As with [[blog-simonwillison-equal-earth-map-projection]] and
  [[blog-simonwillison-bun-webview-json-api]], most of this note's substantive claims and all
  of its concrete artifacts come from directly fetching and reading the linked deployed
  tool's own HTML/JS source (`tools.simonwillison.net/video-compressor`, fetched via `curl`),
  not from the blog post prose alone.
- **WebFetch limitation**: WebFetch's summarized read of the blog post URL did not return
  verbatim prose (it paraphrased and, on inspection, invented some framing not present in the
  source, e.g. describing preset details it had not actually reproduced accurately). All
  quotes in this note were instead extracted by fetching the raw HTML directly with `curl`
  and reading the markup by hand — the same workaround documented in
  [[blog-simonwillison-equal-earth-map-projection]] and
  [[blog-simonwillison-blender-coding-agents-macos]]'s Extraction Notes.
- **No TIL companion page**: checked `til.simonwillison.net/llms/video-compressor` (by analogy
  with [[blog-simonwillison-blender-coding-agents-macos]], which found its substantive content
  on a separate TIL page) — this returned HTTP 404. No longer companion write-up exists for
  this post; the beat post and the tool source are the only available primary material.
- **Claude Code session link inaccessible**: `claude.ai/code/session_01QHTdJZ4xg6TZfDXCmuvAE9`,
  linked directly from the post, returned HTTP 403 on automated fetch (see Claim 8). No claim
  in this note relies on that page's content.
- **No contradictions found**: this source is consistent with, and corroborates, existing
  corpus notes on Willison's vibe-coding practices; no contradiction issue was filed per
  MINER.md §4a.
