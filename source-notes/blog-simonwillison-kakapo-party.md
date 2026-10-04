---
source_url: https://simonwillison.net/2026/Sep/26/kakapo-party/
source_type: blog-post
title: "Kākāpō Party"
author: Simon Willison
date_published: 2026-09-26
date_extracted: 2026-10-04
last_checked: 2026-10-04
status: current
confidence_overall: anecdotal
issue: "#3887"
---

# Kākāpō Party

> A short single-practitioner demo: a two-sentence prompt plus three reference photos got Claude Opus 5.5 to produce a pixel-art HTML5 canvas animation, and a three-sentence Claude Code prompt got a short Playwright script that recorded it as a 15-second video for a keynote slide.

## Source Context

- **Type**: blog-post (a short "beat"/tool post on Simon Willison's weblog, 26 Sep 2026, ~300 words plus two transcript links, one script, and an embedded video).
- **Author credibility**: Simon Willison is a trusted-feed author already heavily represented in this corpus (creator of Django/Datasette, `llm`, `shot-scraper`). Here he reports his own first-person use; there are no measurements.
- **Scope**: One creative-generation task (animation) and one browser-automation task (video capture), both done to produce a slide for a keynote at WeAreDevelopers World Congress North America. It does not cover cost, number of iterations, failure modes, or how the animation was reviewed. The two transcripts (claude.ai share link and gisthost link) were not readable in this run; only the blog post text and script were extracted.

## Extracted Claims

### Claim 1: Claude Opus 5.5 produced a usable pixel-art canvas animation from one prompt plus three reference photos
- **Evidence**: Author's own report; the result is published as a live tool at tools.simonwillison.net/kakapo-party, with a claude.ai transcript linked. Described as having 20+ birds, confetti, balloons, streamers, a disco ball and music-synced dance moves (per the tool's blurb).
- **Confidence**: anecdotal
- **Quote**: "Here's the transcript, and this is the resulting page. It's pretty great!"
- **Our assessment**: Plausible but a single run, judged subjectively by the author; no mention of retries. Useful as a data point on Opus 5.5's visual/creative code generation, not as a benchmark. Note the prompt is also image-grounded: photos supplied "just to remind you what they look like".

### Claim 2: Willison picked Opus 5.5 for this because of community buzz about its pixel-art ability
- **Evidence**: Hearsay ("some buzz"); no cited source.
- **Confidence**: anecdotal
- **Quote**: "I had seen some buzz around how good Claude Opus 5.5 was at creating pixel art animations."
- **Our assessment**: Shows model selection by capability reputation in practice. Unverified claim about the model; treat as a lead, not evidence.

### Claim 3: A short, loosely specified natural-language prompt was sufficient for the generation step
- **Evidence**: The full prompt is reproduced in the post: references, medium (animated pixel art, HTML5 canvas), subject, mood, and one hard numeric constraint (at least 20 birds).
- **Confidence**: anecdotal
- **Quote**: "I need you to make an animation in animated pixel art on HTML 5 canvas of obviously pixel art kakapo jumping up and down having a party with confetti and suchlike - there should be at least 20 of them"
- **Our assessment**: The prompt pattern (reference images + explicit output medium + one countable acceptance criterion) is reusable. The interactive features (click/Space for confetti) were not requested in the prompt, so they came from the model's elaboration — the post's blurb describes them but we cannot confirm this from the prompt alone.

### Claim 4: Claude Code can turn a three-line spec into a working Playwright video-capture script
- **Evidence**: Prompt and the complete resulting script are reproduced; the author says the output "was exactly what I needed for my final slide". Transcript linked.
- **Confidence**: anecdotal
- **Quote**: "Claude Code used Playwright (transcript here) and produced this video, which was exactly what I needed for my final slide:"
- **Our assessment**: Credible; Playwright's `record_video_dir` makes this a small task. The spec is behavioral (duration, delay, spread of clicks) rather than implementation-level — the agent chose the tool and the coordinates.

### Claim 5: The script was short and self-contained (PEP 723 inline dependencies)
- **Evidence**: The script opens with an inline `# /// script` dependency block, so it can be run directly with a tool like `uv run`; ~35 lines.
- **Confidence**: anecdotal
- **Quote**: "Here's the full Playwright script it used, which was pleasingly short:"
- **Our assessment**: The agent's choice of inline script metadata (the post doesn't say how it was run) lets throwaway automation stay a single file with no project setup. Our inference, not the author's claim.

### Claim 6: Prompt constraints map directly onto script structure
- **Evidence**: Prompts: "15s long", "don't start clicking until 3s in", "several clicks are spread around the clickable area". Script: first click at t=3.0, ten clicks at timed offsets across centre/corners/edges, and a final sleep to 16.0s.
- **Confidence**: anecdotal
- **Quote**: "don't start clicking until 3s in"
- **Our assessment**: The agent satisfied the constraints faithfully (and padded 16.0s to cover the 15s requirement, with video trimming left to the user — unverified whether the output was exactly 15s). Good evidence that concrete numeric constraints in a prompt are reliably honored in simple scripts.

### Claim 7: Generation and capture were split across two different agent surfaces
- **Evidence**: Chat interface (claude.ai-style, with transcript share) for design/generation; local Claude Code session for file-system and browser work against `file:///Users/simon/Downloads/kakapo-party.html`.
- **Confidence**: anecdotal
- **Quote**: "so I downloaded the HTML and told a local Claude Code session:"
- **Our assessment**: Illustrates matching the tool to the job: artifact-style generation in chat, local execution in the agent. Handoff was manual (download a file). The author doesn't discuss this as a design choice.

## Concrete Artifacts

Generation prompt (Simon Willison, https://simonwillison.net/2026/Sep/26/kakapo-party/), sent with three photos:

```
Here are some photos of kakapo parrots just to remind you what they look like
I need you to make an animation in animated pixel art on HTML 5 canvas of obviously pixel art kakapo jumping up and down having a party with confetti and suchlike - there should be at least 20 of them
```

Claude Code prompt (same source):

```
Make me a video of file:///Users/simon/Downloads/kakapo-party.html - you need to load it in a browser and click on it a few times to get the confetti effect, the video should be 15s long
don't start clicking until 3s in
make sure several clicks are spread around the clickable area
```

Playwright script produced by Claude Code (same source):

```python
# /// script
# dependencies = ["playwright"]
# ///
import time
from playwright.sync_api import sync_playwright
W, H = 1280, 720
# Canvas fills the viewport; spread clicks across corners, edges and centre
clicks = [
    (3.0, 640, 360),   # centre
    (4.2, 160, 120),   # top-left
    (5.4, 1120, 120),  # top-right
    (6.6, 180, 600),   # bottom-left
    (7.8, 1100, 600),  # bottom-right
    (9.0, 640, 100),   # top-centre
    (10.0, 380, 380),  # mid-left
    (11.0, 900, 380),  # mid-right
    (12.2, 640, 620),  # bottom-centre
    (13.2, 640, 300),  # finale centre
]
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={"width":W,"height":H}, record_video_dir="vids", record_video_size={"width":W,"height":H})
    page = ctx.new_page()
    t0 = time.time()
    page.goto("file:///Users/simon/Downloads/kakapo-party.html")
    for t,x,y in clicks:
        time.sleep(max(0, t-(time.time()-t0)))
        page.mouse.click(x,y)
    time.sleep(max(0, 16.0-(time.time()-t0)))
    ctx.close(); b.close()
```

## Cross-References

- **Corroborates**: `blog-simonwillison-shot-scraper-video.md` (Claim 1, Claim 3) — also uses Playwright to record scripted browser video, there via a new `shot-scraper video` command and a short prompt to GPT-5.5 in Codex; here the agent writes raw Playwright directly, which is the pre-tooling baseline for the same task. Also corroborates the recurring pattern of very short prompts producing working agent output.
- **Contradicts**: None found. No contradiction issue filed.
- **Extends**: `blog-simonwillison-introducing-opus-5.md` (Opus 5 family launch) with a first-hand creative-generation anecdote; `blog-ghaw-playwright-cli-only.md` (Claim 3) by showing the alternative of the agent writing a plain Playwright script rather than using MCP or `playwright-cli`.
- **Novel**: Image-grounded generation of a pixel-art canvas animation and the video-capture handoff to a coding agent for slide production. No existing note covers creative/pixel-art generation or keynote-asset production.

## Guide Impact

- **Chapter 03 (code generation)**: Optional short example of an image-grounded prompt pattern (reference photos + medium + one countable constraint), citing Claim 3. Anecdotal only; do not present as a benchmark.
- **Chapter 05 (tooling/automation)**: Optional example that timing-and-coverage requirements stated behaviorally in a prompt can yield a one-file Playwright capture script (Claim 4, Claim 6), alongside `blog-simonwillison-shot-scraper-video.md`. No existing recommendation is contradicted.
- Overall: low impact; a supporting illustration rather than a driver of change. Chapter numbers follow the Prospector's triage and were not re-verified against `guide/`.

## Extraction Notes

- Read the full post via raw HTML. The two linked transcripts (claude.ai share and gisthost) and the live tool were not opened, so claims about the animation's features rely on the tool's blurb on the blog page and the author's description.
- The post is short; seven claims is near its ceiling. Several claims are our inferences from the script and are flagged as such in "Our assessment".
- The Prospector triage comments mention "20+" birds; the prompt asked for "at least 20", and the blurb doesn't state a count.
