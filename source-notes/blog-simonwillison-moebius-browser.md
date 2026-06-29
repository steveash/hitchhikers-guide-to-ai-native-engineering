---
source_url: https://simonwillison.net/2026/Jun/22/porting-moebius/
source_type: blog-post
title: "Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code"
author: Simon Willison
date_published: 2026-06-22
date_extracted: 2026-06-29
last_checked: 2026-06-29
status: current
confidence_overall: anecdotal
issue: "#1343"
---

# Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code

> Simon Willison documents a complete vibe-coding session in which Claude Code converts a PyTorch image inpainting model to ONNX, adds browser-side weight caching, deploys weights to Hugging Face, and ships a GitHub Pages demo — providing a dense set of transferable workflow patterns: research-first with research.md as context handoff, the "commit early and often + notes.md + plan.md" setup prompt, parallel idle-time work, subagent token conservation, the "muse on X" open-ended exploration pattern, and explicit final-URL in deployment prompts.

## Source Context

- **Type**: blog-post (Simon Willison's blog, June 22, 2026; ~1,500 words; first-person practitioner experience report documenting a complete Claude Code session from initial idea to shipped demo; includes linked Claude Code session transcript published via the `claude-code-transcripts` tool, a working demo, and the Hugging Face model repository)
- **Author credibility**: Simon Willison is the creator of Django, creator of Datasette, author of the `llm` CLI, and a designated trusted-feed source in this repo. He has a long track record of documenting real experiments with publicly verifiable outputs. He has no vendor affiliation. He is candid about limitations (typos in prompts reproduced verbatim, notes about incomplete ASCII diagrams) and is one of the most rigorous independent AI-tooling practitioners. This is his sixth (approximate) browser-native Claude Code experiment in the corpus, providing a stable baseline for cross-source comparison. The working demo (`simonw.github.io/moebius-web/`), the Claude Code transcript, and the Hugging Face model repository (`huggingface.co/simonw/Moebius-ONNX`) are publicly verifiable.
- **Scope**: Covers: (1) the complete workflow from initial Claude.ai feasibility research to a shipped GitHub Pages demo; (2) PyTorch → ONNX model conversion with dynamic axes; (3) browser weight caching via CacheStorage API; (4) Hugging Face model weight publishing delegated entirely to Claude Code; (5) GitHub Pages deployment with explicit URL; (6) browser compatibility validation (Chrome, Firefox, Safari). Does NOT cover: privacy implications of client-side ML inference, performance benchmarks, model quality evaluation, the inpainting accuracy of the Moebius model itself, or why WebGPU was preferred over WebGL.

## Extracted Claims

### Claim 1: Starting a Claude Code project by first running a research session with Claude.ai yields higher-quality initial direction

- **Evidence**: Willison's first step before writing any code or invoking Claude Code was a Claude.ai session to investigate feasibility. He describes this as his standard pattern for this class of project.
- **Confidence**: anecdotal (one practitioner, consistent pattern across multiple projects; see liteparse-browser.md Claim 4 for the same mobile-to-desktop two-phase inception pattern)
- **Quote**: "My first step was to ask regular Claude about the feasibility of this project."
- **Our assessment**: The research phase does two things: it surfaces the key technical path before the coding agent is invoked (Claude suggested ONNX Runtime Web over Transformers.js, which became the entire architecture), and it produces a document (research.md) that the coding agent can read as context, avoiding re-explanation. The pattern is consistent across at least two Willison experiments (this and LiteParse) — enough to treat it as deliberate, not coincidental.

### Claim 2: Saving Claude.ai research output as research.md, then having Claude Code read it as its starting context, bridges chat and coding agent sessions without re-explaining the problem

- **Evidence**: Willison explicitly describes saving the last Claude.ai response to a file for later use by Claude Code. The Claude Code goal prompt explicitly references this file.
- **Confidence**: anecdotal (single practitioner; deliberate and named pattern)
- **Quote**: "I copied out the last answer and saved it as research.md for Claude Code to read later."
- **Our assessment**: The research.md approach is a refinement over the notes.md handoff pattern documented in `blog-simonwillison-liteparse-browser.md` Claim 5. In LiteParse, the user pasted prior chat output into notes.md; here, research.md stores the human-curated input and notes.md is reserved for the agent's own working notes. The semantic separation is cleaner: research.md = what the human knows going in; notes.md = what the agent discovers along the way. Both files serve the same function (bridging context across sessions) but the two-file pattern has clearer separation of concerns.

### Claim 3: An explicit project-setup prompt establishing commit discipline, notes.md, and plan.md at session start reduces context drift and produces a recoverable work trail

- **Evidence**: Willison's first Claude Code prompt (reproduced verbatim with typos) establishes three session hygiene practices before any technical work begins. This is presented as his standard setup, not a one-off choice.
- **Confidence**: anecdotal (single practitioner; pattern consistent with liteparse-browser Claim 5 and Claim 8)
- **Quote**: "Bulid this in /tmp/Moebius/moebius-web and commit early and often, also maintain a notes.md file in there with notes about what you figure out along the way - also start by writing out a plan.md in there and update that plan as oy work too"
- **Our assessment**: The three elements — small commits, notes.md, plan.md — address three different failure modes of long agentic sessions: (1) commits prevent total rollback from being the only recovery path; (2) notes.md allows the practitioner to inspect the agent's reasoning without reading all the code; (3) plan.md externalizes the agent's approach and makes it correctable. The prompt was typed with typos ("Bulid", "oy") and still produced the desired behavior — another data point that exact phrasing matters less than clear intent for this class of setup instruction.

### Claim 4: Using a coding agent as a parallel side project during idle time between main-project tasks is a practical multiplier on productive output

- **Evidence**: Willison describes his main project (Datasette feature landing) as the primary focus and the Moebius port as a parallel task he checked in on during waits. He explicitly notes that longer agent tasks create more productive idle time for other work.
- **Confidence**: anecdotal (one practitioner; personal workflow observation)
- **Quote**: "I kicked it off and went back to my main project, checking in occasionally to see how Claude was doing."
- **Quote**: "An amusing thing about coding agents is that the harder a problem is the more time you have to get distracted while you wait"
- **Our assessment**: The irony Willison identifies — harder problems create more slack time for other work — is a structural property of agentic coding that practitioners can deliberately exploit. A long-running Claude Code task is not dead time; it is an opportunity for parallel human-directed work. The inverse also follows: trivial tasks that complete in under a minute are the ones that break flow most, because the practitioner stays idle rather than context-switching. For practitioners: schedule the harder, longer-running agentic tasks when you have other meaningful work you can do in parallel.

### Claim 5: Using a subagent to inspect reference code avoids burning the main session's token context on obfuscated or low-value source material

- **Evidence**: Willison needed Claude Code to study the Whisper Web demo for caching patterns. Rather than reading its obfuscated JavaScript directly in the main session, he directed Claude Code to delegate that read to a subagent.
- **Confidence**: anecdotal (one practitioner; deliberate token management decision)
- **Quote**: "That project was entirely obfuscated, built JavaScript files so I figured using a subagent would avoid spending the rest of my top-level token context deciphering those files."
- **Quote**: "look in /tmp/Moebius/whisper-web (with a subagent) and see how they do this"
- **Our assessment**: The subagent-for-dirty-reads pattern is a specific token budget management technique: when a reference implementation is large, obfuscated, or otherwise verbose, reading it in the main session may consume most of the available context. A subagent can ingest all of that material and return only the relevant summary (in this case: how Whisper Web handles caching), preserving the main session's token budget for the actual implementation. This is architecturally similar to using retrieval rather than full-context injection — delegate the dirty work to a separate context window and surface only the signal.

### Claim 6: "Muse on X" is the shortest effective prompt for asking a model to open-endedly explore a problem without committing to a concrete solution path

- **Evidence**: Willison describes this as his own discovered shorthand, with an explicit statement of what it means to him.
- **Confidence**: anecdotal (one practitioner's named pattern; no evidence of widespread use outside Willison's practice)
- **Quote**: "I like telling models to 'muse on X', it's the shortest way I've found of expressing that I want them to contemplate a problem for me without providing them with a concrete goal."
- **Our assessment**: The "muse on X" pattern is distinct from "explain X" (which asks for an explanation of something known) or "solve X" (which asks for a solution). "Muse on" requests open-ended contemplation — useful for surfacing considerations, tradeoffs, and approaches before committing to a specific direction. The shorthand saves the practitioner from writing a longer meta-prompt explaining that they want exploration rather than execution. For practitioners who use Claude for pre-implementation exploration: this is a low-friction way to trigger that mode without a lengthy meta-prompt.

### Claim 7: Agent-maintained notes.md serves dual purposes — capturing discoveries in real time and bootstrapping future agent sessions on the same project

- **Evidence**: Willison explicitly names both purposes when describing why he asks agents to maintain notes files.
- **Confidence**: anecdotal (one practitioner; pattern corroborated across multiple Willison projects)
- **Quote**: "I often ask agents to keep notes like this—the end result is often interesting, both for myself and for the next agent session that touches the same project."
- **Our assessment**: The two purposes pull in slightly different directions: real-time capture optimizes for completeness (every discovery noted), future-session bootstrapping optimizes for relevant signal (what will the next session need to know?). In practice, the real-time capture serves both: a comprehensive notes.md from the first session becomes the context injection document for a second session, exactly as research.md did here. The "often interesting for myself" observation is the surprise artifact: practitioners who haven't read the notes.md often find it provides a more legible narrative of what the agent did than the commit history or the code itself.

### Claim 8: Providing the exact final production URL in a deployment prompt prevents URL-construction errors in deployed artifacts

- **Evidence**: Willison explicitly explains why he included the final URL in his GitHub Pages deployment prompt — to allow Claude Code to fix any URLs in the built artifact that needed to match the production domain.
- **Confidence**: anecdotal (one practitioner; direct causal explanation)
- **Quote**: "Telling it the final URL was important in case it needed to fix the URLs in the demos that it was building so they would work when deployed to production."
- **Our assessment**: The failure mode Willison anticipates is real and common: demo apps built locally often hardcode `localhost:3000` or relative paths that break when deployed to a specific production URL. By specifying `https://simonw.github.io/moebius-web/` in the deployment prompt, he allowed Claude Code to identify and correct any such URLs in the build artifacts before publishing. This is a one-sentence addition to a deployment prompt that prevents a common class of post-deploy breakage. For practitioners deploying browser-native apps: include the final URL in the deployment prompt, not as an afterthought.

### Claim 9: Pasting browser error messages and screenshots directly into Claude Code is the primary iterative feedback mechanism in browser-native vibe coding

- **Evidence**: Willison describes his feedback loop: test in browser, get errors, paste errors + screenshots into Claude Code.
- **Confidence**: anecdotal (one practitioner; but this is the standard human-in-the-loop feedback pattern for browser development with an agent)
- **Quote**: "Then I tried it out in Chrome and pasted some errors (and screenshots of errors) back into Claude Code."
- **Our assessment**: The feedback loop is minimal: the practitioner does not write fixes, does not explain the error, and does not debug. They test, observe, paste the observable symptom (error message + screenshot), and let the agent interpret and resolve. This is the "testing feedback" role Willison identified in his vibe coding post (`blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 1): the practitioner restricts their role to testing. The screenshot addition is significant — visual feedback (a browser error rendered in a UI) is more information than a bare error message in the console, and Claude Code can interpret screenshots directly. For multimodal error feedback, screenshots are a zero-overhead addition to the error paste.

### Claim 10: Browser-side ML model weights (here ~1.3GB) must be explicitly cached via the CacheStorage API or they re-download on every page reload

- **Evidence**: Willison discovered the re-download problem through testing, then asked Claude Code to investigate caching solutions by asking how other similar projects handled it.
- **Confidence**: settled (the browser behavior — no automatic caching for large model files unless explicitly programmed — is a browser specification fact; the CacheStorage solution is the standard approach used by other projects like Whisper Web)
- **Quote**: "each time I reloaded the page it seemed to download ~1.3GB of model weights"
- **Quote**: "Claude figured out that it was using `caches.open(\"transformers-cache\")`—the CacheStorage API—and added that to our project."
- **Our assessment**: The CacheStorage API discovery illustrates a high-value instance of the "point Claude at a reference implementation" pattern: rather than asking Claude to invent a caching solution, Willison asked it to study how Whisper Web did it (via a subagent). Claude found the specific API call, understood it, and replicated it. For practitioners building browser-native ML apps: model weights must be explicitly cached on first download. `caches.open("transformers-cache")` (or equivalent) is the standard solution. Without it, every user session downloads the full model size.

### Claim 11: Claude Code can autonomously publish large model artifacts to Hugging Face and deploy the frontend to GitHub Pages with minimal practitioner involvement

- **Evidence**: Willison describes both publishing steps as delegated to Claude Code and presents them as completed facts, not as things he did.
- **Confidence**: anecdotal (single practitioner observation; verifiable via the public Hugging Face repository and GitHub Pages deployment)
- **Quote**: "It published the 1.24GB of converted ONNX weights to huggingface.co/simonw/Moebius-ONNX for me."
- **Our assessment**: The autonomous publication of 1.24GB to Hugging Face is a striking data point: the agent not only converted the model but completed the entire publishing workflow (creating the repo, uploading weights, configuring the metadata) without step-by-step human guidance. This extends the CI/CD delegation pattern from `blog-simonwillison-liteparse-browser.md` Claim 13 (delegating GitHub Actions setup to a separate Claude Code session) to include third-party model hosting. The pattern generalizes: any well-documented deployment target with a clear CLI or API interface is a delegatable Claude Code task.

### Claim 12: ONNX Runtime Web on the WebGPU backend is Claude's preferred recommendation over Transformers.js for running custom models in the browser

- **Evidence**: The Claude.ai feasibility research surfaced this recommendation. It chose ONNX Runtime Web "the layer below Transformers.js" — indicating it understood the architectural tradeoff.
- **Confidence**: anecdotal (one session, one model type; Claude's recommendation was correct for this use case but generalizability depends on the model)
- **Quote**: "Claude suggested using ONNX Runtime Web on the WebGPU backend—the layer _below_ the Transformers.js library"
- **Our assessment**: The recommendation to go below Transformers.js to ONNX Runtime Web directly reflects the fact that Transformers.js is a higher-level library primarily designed for transformer models. For a custom model architecture (Moebius is an inpainting model, not a transformer), the lower-level ONNX Runtime Web provides more direct control and broader model format compatibility. Claude's understanding of this architectural hierarchy is notable — it did not default to the more commonly mentioned Transformers.js but chose the level appropriate for the model type.

### Claim 13: A complete browser-native ML project (PyTorch to ONNX conversion, browser UI, model hosting, deployment) can be executed via vibe coding with zero lines of code authored by the practitioner

- **Evidence**: Willison explicitly declares this as vibe coding and confirms he reviewed no code.
- **Confidence**: anecdotal (single practitioner, single project; working demo provides external validation)
- **Quote**: "This definitely counts as vibe coding: I didn't look at a single line of code from the project, restricting my input to testing, suggesting small feature improvements and pointing the model in the direction of examples."
- **Quote**: "Chrome, Firefox and Safari are all now capable of running this kind of model—I tried it in all three."
- **Our assessment**: The project scope here is substantially larger than the LiteParse port: model format conversion (PyTorch → ONNX with dynamic axes), browser inference runtime integration (ONNX Runtime Web + WebGPU), browser caching (CacheStorage API), model publishing (Hugging Face), and frontend deployment (GitHub Pages). The successful cross-browser validation (Chrome, Firefox, Safari) confirms the implementation is not a trivial stub. For the guide: this is additional evidence that the "blast-radius-conditioned vibe coding" framework from `blog-simonwillison-liteparse-browser.md` Claim 12 extends to non-trivial ML inference projects when the deployment conditions (static site, client-side only, no user data) are met.

## Concrete Artifacts

### Project setup prompt (verbatim, with original typos)

```
# Source: simonwillison.net/2026/Jun/22/porting-moebius/
# First Claude Code prompt: project hygiene setup

Bulid this in /tmp/Moebius/moebius-web and commit early and often, also
maintain a notes.md file in there with notes about what you figure out
along the way - also start by writing out a plan.md in there and update
that plan as oy work too
```

*Note: "Bulid" (should be "Build") and "oy" (should be "you") are original typos from Willison's post, preserved verbatim.*

### Goal prompt (verbatim)

```
# Source: simonwillison.net/2026/Jun/22/porting-moebius/
# Second Claude Code prompt: project goal

Read ./moebius-web/research.md - your goal is to port this model to ONNX
and WebGPU so we can run it directly in a browser, with a simple UI
```

### Subagent reference inspection prompt (verbatim, paraphrased structure)

```
# Source: simonwillison.net/2026/Jun/22/porting-moebius/
# Prompt to Claude Code to delegate reference code inspection

look in /tmp/Moebius/whisper-web (with a subagent) and see how they do this
```

*Context: /tmp/Moebius/whisper-web was a local copy of the Whisper Web demo, which had obfuscated build artifacts. The parenthetical "(with a subagent)" is Willison's own annotation.*

### GitHub Pages deployment prompt (verbatim)

```
# Source: simonwillison.net/2026/Jun/22/porting-moebius/
# Deployment prompt with explicit final URL

I want to publish the moebius-web folder to GitHub, minus the large files
(so maybe minus the models/ folder), such that when I turn on GitHub Pages
for that repo navigating to https://simonw.github.io/moebius-web/ serves the UI
```

### PyTorch → ONNX conversion with dynamic axes (verbatim from article)

```python
# Source: simonwillison.net/2026/Jun/22/porting-moebius/
# Generated by Claude Code for the Moebius model conversion

torch.onnx.export(
    dec,
    (lat,),
    dec_path,
    opset_version=args.opset,
    input_names=["latent"],
    output_names=["image"],
    dynamic_axes={"latent": {0: "B"}, "image": {0: "B"}},
)
```

### Workflow pattern: research.md → agent implementation

```
Pattern: Context handoff from Claude.ai to Claude Code
Source: simonwillison.net/2026/Jun/22/porting-moebius/

Step 1: Claude.ai feasibility research session
        Prompt example: "Clone https://github.com/hustvl/Moebius/ and tell me
        if they published the code and weights to run this model anywhere"
        Result: Architecture recommendation (ONNX Runtime Web + WebGPU backend)

Step 2: Save last Claude.ai response verbatim as research.md in project root

Step 3: Claude Code setup prompt (establishes hygiene):
        "commit early and often, maintain notes.md [...], start by writing
        plan.md and update as you work"

Step 4: Claude Code goal prompt:
        "Read ./moebius-web/research.md - your goal is to [concrete task]"

Outcome: Agent grounds its implementation plan in prior research.
         notes.md captures ongoing discoveries.
         research.md vs notes.md separation: research.md = human-curated input;
         notes.md = agent's working memory.
```

### Subagent token conservation pattern

```
Pattern: Subagent for dirty reads
Source: simonwillison.net/2026/Jun/22/porting-moebius/

Problem:  Reference implementation uses obfuscated build artifacts —
          reading them in the main session would consume most of the
          main token context.

Solution: Direct Claude Code to use a subagent for the inspection step:
          "look in /tmp/[reference-dir] (with a subagent) and see how
           they do this"

Result:   Main session receives only the relevant summary (e.g., "uses
          caches.open('transformers-cache')"). Obfuscated source is
          consumed by the subagent context, not the main context.

When to use: Any time a reference implementation is large, obfuscated,
             or low-signal relative to the specific question being asked.
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-liteparse-browser.md` Claim 4 (mobile-to-desktop two-phase inception: explore with Claude.ai, then build with Claude Code): Claim 1 of this note is the same research-first pattern. In LiteParse, the first phase was on mobile; here it was desktop Claude.ai, but the structure is identical: Claude.ai for feasibility → Claude Code for implementation. Two Willison experiments using the same pattern corroborates it as deliberate.
  - `blog-simonwillison-liteparse-browser.md` Claim 8 ("small commits along the way" as an explicit prompt addition): Claim 3 of this note includes the same "commit early and often" discipline as part of the setup prompt. Same practitioner, same discipline, different project.
  - `blog-simonwillison-liteparse-browser.md` Claim 12 (blast-radius-conditioned vibe coding: static site, in-browser processing, no data transfer as conditions for zero-review justification): Claim 13 of this note is another instance satisfying those same three conditions. The Moebius port is a static GitHub Pages deployment, all processing in-browser, no user data. Two Willison projects, same blast-radius justification, corroborates the framework.
  - `blog-simonwillison-liteparse-browser.md` Claim 13 (GitHub Pages + separate Claude Code session for CI/CD setup, fully delegated): Claim 11 of this note extends the same delegation pattern to include Hugging Face model publishing as an additional autonomous step. Both projects delegated the complete deployment pipeline to Claude Code.
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 1 ("the boundary between vibe coding and responsible agentic engineering has begun to blur"): Claim 13 here is a further concrete instance of that blur. Willison declares it vibe coding, ships it, does not review the code. This is the fourth (approximate) in-corpus Willison example of shipping working browser-native infrastructure without code review.
  - `blog-simonwillison-pyodide-asgi-browser.md` Claim 1 (Claude Opus 4.8 implementing a complete multi-component infrastructure architecture from a single task description): Claim 13 of this note is a parallel example — different model, different stack, same result: working multi-component browser-native ML system built from high-level task descriptions without code authorship.

- **Extends**:
  - `blog-simonwillison-liteparse-browser.md` Claim 5 (notes.md → plan.md context handoff pattern): This note extends that pattern with a cleaner semantic separation — research.md holds the human-curated input; notes.md is reserved for the agent's ongoing discoveries. The LiteParse note mixed both functions in notes.md; the Moebius pattern separates them. This is an evolution of the same workflow primitive.
  - `blog-simonwillison-liteparse-browser.md` Claim 13 (deployment delegation): Extended here to include third-party model hosting (Hugging Face) as an autonomous step alongside the GitHub Pages frontend deployment. The delegation pattern now covers: GitHub Actions setup, Hugging Face model publishing, and static site deployment — all initiated from single natural-language prompts.

- **Contradicts**: None identified.

- **Novel**:
  - **research.md / notes.md semantic separation**: No existing corpus source explicitly separates the human-curated context handoff file (research.md) from the agent's working notes file (notes.md). The liteparse note conflated both in notes.md. This note introduces the two-file pattern as a refinement.
  - **Subagent for dirty-read token conservation**: No existing corpus source documents the specific practice of directing a subagent to inspect obfuscated or verbose reference code to avoid consuming main-session token budget. The subagent-as-context-firewall pattern for reference code inspection is new to the corpus.
  - **"Muse on X" prompt shorthand**: No existing corpus source documents this specific prompt pattern by name. The pattern (ask for open-ended contemplation without a concrete goal) is implicit in some other sources, but Willison names it and explains its purpose explicitly here.
  - **Explicit final URL in deployment prompts**: No existing corpus source documents the practice of including the exact production URL in the deployment prompt to prevent URL-construction errors in build artifacts. The LiteParse note documents delegation but not this specific correctness technique.
  - **Parallel idle-time agent work**: No existing corpus source names the pattern of scheduling Claude Code as a parallel task during human wait time on a separate project, treating agent idle-time as productive rather than dead time.
  - **CacheStorage API for browser ML weight caching**: No existing corpus source documents the specific browser caching constraint (large ML model weights re-download on every reload without explicit CacheStorage programing) or the `caches.open("transformers-cache")` solution.

## Guide Impact

- **Chapter 01 (Daily Workflows — Parallel Agent Tasking)**: Claim 4 documents the idle-time parallel-work pattern: schedule hard, long-running Claude Code tasks when you have other meaningful work that can proceed in parallel. The structural observation — harder tasks create more agent idle time, and that time can be productively used — should be named explicitly in the guide as a workflow design principle. The guide currently does not address how to schedule agentic tasks relative to human work cadence.

- **Chapter 02 (Harness Engineering — Research-to-Agent Context Handoff)**: Claims 1 and 2 together extend the context handoff framework established in `blog-simonwillison-liteparse-browser.md`. The guide should document the two-file refinement: "Use research.md for human-curated AI chat output and notes.md for agent working notes — keeping them separate makes the handoff more legible and prevents the agent from treating its own working notes as the human's ground truth." Cite both this note and the liteparse note as practitioner-confirmed examples of the same pattern.

- **Chapter 02 (Harness Engineering — Standard Session Setup Prompt)**: Claim 3 provides a second in-corpus verbatim example of the "commit early and often + maintain notes.md + write plan.md" session hygiene prompt. The guide should elevate this to a recommended starting prompt template for multi-hour Claude Code sessions, citing both liteparse (the first example) and this note (a second confirmation). The verbatim typos in the prompt are worth noting: exact phrasing matters less than the three structural elements.

- **Chapter 02 (Harness Engineering — Token Budget Management with Subagents)**: Claim 5 introduces the subagent-as-context-firewall pattern, which has no prior in-corpus documentation. Add to the guide: "When a reference implementation is large, obfuscated, or otherwise verbose, direct Claude Code to use a subagent for the inspection step. The parenthetical '(with a subagent)' in a prompt is sufficient to trigger this delegation. The subagent consumes the dirty-read context; the main session receives only the relevant summary."

- **Chapter 04 (Context Engineering — "Muse on X" Prompt Pattern)**: Claim 6 names a specific open-ended exploration prompt shorthand. Add to the prompt pattern reference section: "'Muse on X' asks the model to contemplate a topic without committing to a concrete solution path — useful for surfacing tradeoffs, approaches, and considerations before choosing a direction. Shorter and more effective than 'please think about X from multiple angles.'"

- **Chapter 04 (Context Engineering — Deployment Correctness via Explicit URL)**: Claim 8 is a one-sentence technique that prevents a common class of post-deploy URL breakage. Add as a deployment-prompt checklist item: "Include the exact production URL in the deployment prompt to allow the agent to fix production-relative URLs in build artifacts before publishing."

- **Chapter 03 (Agent Patterns — Browser-Native ML Inference via ONNX + WebGPU)**: Claims 10, 11, and 12 together establish a complete browser-native ML deployment stack that Claude Code can implement autonomously: (1) ONNX Runtime Web + WebGPU backend for in-browser inference, (2) CacheStorage API for weight caching, (3) Hugging Face for model hosting, (4) GitHub Pages for frontend. The guide should document this stack as a validated option for deploying custom models to the browser, with the CacheStorage step named explicitly as a required addition for models above a few hundred MB.

## Extraction Notes

- **Verbatim quotes obtained via targeted WebFetch**: The WebFetch tool returns summaries by default rather than verbatim text. All quoted passages were obtained via multiple targeted requests asking for character-for-character text. Quotes were confirmed in multiple fetches for the most critical passages (the Claude Code setup prompt, the goal prompt, the "muse on X" description).
- **Original typos preserved**: The initial Claude Code setup prompt contains two typos ("Bulid" and "oy"). These are Willison's own, preserved in the article as a demonstration that typos in prompts do not prevent the agent from understanding intent. They have been preserved verbatim in this note's artifacts.
- **Fragment URL**: The source issue was filed with the URL `https://simonwillison.net/2026/Jun/22/porting-moebius/#atom-everything`. The `#atom-everything` fragment is an Atom feed anchor artifact from the automated scanner. The `source_url` field uses the canonical page URL without the fragment.
- **understanding.md**: Multiple triage comments reference an "understanding.md" file with a glossary and ASCII-art diagram. The article text confirms Claude produced "a handy glossary and an only-slightly-broken ASCII-art diagram showing how the model pipeline fits together" but the specific filename could not be independently confirmed from the article text via WebFetch. The content (glossary + diagram) is confirmed; the filename attribution is from the triage comments.
- **Three triage comments**: Three separate Prospector triage assessments were filed on this issue. The first focuses on agent workflow patterns (Ch02/Ch04); the second focuses on model conversion and browser ML patterns (Ch03/Ch04/Ch05); the third focuses on context engineering patterns for Claude Code workflows (Ch01/Ch02/Ch04). All three were read and synthesized into this note.
- **Confidence set to anecdotal**: The source is a single practitioner's first-person report. The working demo and Claude Code transcript are publicly verifiable artifacts that confirm the project succeeded, but the workflow claims are one practitioner's account of one project. `anecdotal` is appropriate — the working artifacts validate the outcome, not the workflow generalizability.
- **Cross-references verified**: All claim numbers cited from other source notes were verified by reading the respective notes and counting claims in document order before citing. No claim numbers were guessed.
