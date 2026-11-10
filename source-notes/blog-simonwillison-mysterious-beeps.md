---
source_url: https://simonwillison.net/2026/Nov/9/mysterious-beeps/
source_type: blog-post
title: "Locating the source of a mysterious beep with Claude"
author: Simon Willison
date_published: 2026-11-09
date_extracted: 2026-11-10
last_checked: 2026-11-10
status: current
confidence_overall: anecdotal
issue: "#4614"
---

# Locating the source of a mysterious beep with Claude

> Willison built "Beep Locator" with Claude Code, giving the agent a perception channel (browser microphones) and a hot-swap code-delivery path (`installModule()` over WebSocket) so it could iterate on a live system; the evidence is a single hobby project with no published metrics.

## Source Context

- **Type**: blog-post (single-author build log / experience report)
- **Author credibility**: Simon Willison is a prolific LLM-tooling writer who usually links prompts and session transcripts. Here the code (`detector.js`) and a starter session are referenced, but the post reports no systematic measurements.
- **Scope**: Covers the problem, system design (Python server, browser listeners, FFT + high-pass beep detection, chirp-based clip alignment, BeepBeep-style ranging), the prompt sequence, and the "give the agent ears" takeaway. Does not cover failure analysis, safety of pushing arbitrary code to clients, or any team-scale practice. Triage guidance: treat the acoustics as background.

## Extracted Claims

### Claim 1: A coding agent can be given a perception channel for the physical world even without native input modality
- **Evidence**: Claude has no audio input, but wrote JS/Python that captured browser-microphone audio on several devices; the agent queried audio logs and reconfigured listeners. Final result: located a beeping carbon monoxide detector within about 40cm.
- **Confidence**: anecdotal
- **Quote**: "Claude doesn’t have native audio input (yet), but it can run JavaScript and Python code that can analyze audio captured by a microphone."
- **Our assessment**: A credible, reusable pattern: expose the world as logs/queryable files the agent can read. One successful home project; no comparison to alternatives.

### Claim 2: A hot-swap module mechanism lets the agent deploy new code to running remote clients without human interaction per device
- **Evidence**: Opus 5.5 built `installModule()` on the listeners, triggered over WebSocket. Motivation: some browsers re-prompt for microphone permission on every page reload.
- **Confidence**: anecdotal
- **Quote**: "Opus 5.5 had built an installModule() method on the listeners that could be triggered over the WebSocket connection, meaning the admin server could execute arbitrary new code on any of its clients."
- **Our assessment**: Strong harness-engineering pattern: remove the human from the deploy loop where deploys are costly. It is also remote code execution by design; the post says nothing about keeping it safe. This works only on a trusted LAN hobby setup.

### Claim 3: The hot-swap path was requested by the human in the prompt, so the agent could be left alone to experiment
- **Evidence**: The prompt after the research step asked for the mechanism explicitly.
- **Confidence**: anecdotal
- **Quote**: "add a mechanism so you can send new code to the listeners which they will then run automatically - that way I can set everything up in the room and then leave you alone to continue hacking and experiment while I do something else"
- **Our assessment**: Notable that the autonomy-enabling infrastructure was specified up front as a design requirement, not discovered later. Note the author's later description says he mostly sat chatting with the agent, so "walk away" was only partly realized.

### Claim 4: Verification by known-signal injection (clapping) built confidence that the sensing system could locate sound before trusting it on the real target
- **Evidence**: A clap mode shows claps as diamonds on the map, versus X for beeps; timestamps on each symbol made it easy to match symbols to real-world sounds.
- **Confidence**: anecdotal
- **Quote**: "This helped me gain confidence that it was capable of locating a sound."
- **Our assessment**: Classic calibration-by-known-source. The human generated the claps; the post does not show the agent running this check autonomously. No accuracy numbers from the clap tests.

### Claim 5: Human-in-the-loop confirmation (replay, then "This is the mystery beep") gates what the system learns
- **Evidence**: A log with play buttons replays each listener's recording in sequence (mic muted during replay); user clicks a button to label a detection as the target, after which the system categorizes future noises and refines the location.
- **Confidence**: anecdotal
- **Quote**: "You can replay these sounds (from each device in turn) to confirm they are the mysterious beep you are looking for, then click “This is the mystery beep” to mark them as such."
- **Our assessment**: Human labels are the ground truth that prevents the detector from learning from false positives. Only the human can say what "the mystery beep" sounds like.

### Claim 6: Starting with a spec file written with the agent, then research, then build, gave a good foundation
- **Evidence**: First prompt to a new empty repo from an iPhone in Claude Code Cloud (Opus 5.5, Extra thinking effort) asked for `problem.md`; Claude found and read the BeepBeep 2007 paper while writing it.
- **Confidence**: anecdotal
- **Quote**: "Write out a problem.md file describing the problem we want to solve"
- **Our assessment**: Spec-first with agent-assisted research is a repeatable workflow. The agent surfaced prior art (BeepBeep) the author did not name. The user judged the research "looked good" before authorizing the build.

### Claim 7: Cloud session for scaffolding, then local session for running the live system
- **Evidence**: The cloud session produced "most of the system" but "nothing had actually tried running it yet". Author cloned the repo to a laptop and used Claude Code there (with Fable 5.2, just released) with the server running so the agent could see output and make live changes.
- **Confidence**: anecdotal
- **Quote**: "I had Claude Code on my laptop start the server running, then made sure it could both see what was happening and make live changes to the software as it ran."
- **Our assessment**: Illustrates a split: remote sessions can't touch physical devices; local sessions can. Hardware-in-the-loop work forces a local agent.

### Claim 8: Iterative feature prompts, driven by what the author observed, shaped the product; physical-world constraints produced fallback designs
- **Evidence**: Device-to-device localization by sound "didn't work particularly well", so he added "Rough mode" (drag icons to rough positions, then sounds refine them). Later prompts added timestamps, replay, a "Reposition the devices" flow, and a suggested location for an extra listener.
- **Confidence**: anecdotal
- **Quote**: "This didn’t work particularly well, so I added a “Rough mode”"
- **Our assessment**: The agent's ambitious design (auto-localization) partly failed; a human-assisted fallback rescued it. The post does not detail what failed or how it was diagnosed.

### Claim 9: Two-stage detection architecture: cheap client-side detection, server-coordinated alignment
- **Evidence**: Listeners keep a 60-second rolling audio buffer and run FFT + high-pass beep detection (`detector.js`). On a report the server picks the device with lowest round-trip time to play a chirp, then requests clips from every listener to align them.
- **Confidence**: anecdotal
- **Quote**: "This chirp allows the clips to be aligned with each other, a crucial step in locating the beep."
- **Our assessment**: Background on the system, not guide content (per triage). Useful only as evidence of how much non-trivial design the agent handled.

### Claim 10: Agents perceiving their environment is a broader emerging practice
- **Evidence**: Anecdote from GitHub Universe: Martin Woodward plugged badge computers into a computer over USB-C and pointed a webcam at their screens so his coding agent could tell if updates worked.
- **Confidence**: anecdotal
- **Quote**: "Figuring out ways to let coding agents perceive the world around them is a whole lot of fun."
- **Our assessment**: Second-hand anecdote, but it is the same pattern (sensor + deploy path = closed loop for hardware work).

## Concrete Artifacts

First prompt (from the post, quoted in a blockquote, attributed to Willison's starter session):

```
Write out a problem.md file describing the problem we want to solve
There is a device beeping in a room and I cannot find it
I want to set up several devices - laptops, phones, iPads - around the room all listening at the same time and have them help triangulate where the beep comes from
There needs to be a Python web app which coordinates it all - one device shows a web page for the app, other devices join a URL which turns them into listeners - all via browser WebAudio and WebSockets back to the Python server app
```

Hot-deploy requirement prompt:

```
Ok try and build it, add a mechanism so you can send new code to the listeners which they will then run automatically - that way I can set everything up in the room and then leave you alone to continue hacking and experiment while I do something else
```

Test-rig prompt (excerpt, as in the post, with "[...]" in the original):

```
what’s a good way for me to test this I wonder? Can we have it listen for claps, then I could clap and it could identify the location of the clap? [...]
Claps should use a different symbol on the map than beeps
```

Setup and results: two iPads, a phone, a MacBook Pro and a Surface Ultra as listeners; location accurate to "about 40cm"; the source was an old carbon monoxide detector.

## Cross-References

- **Corroborates**: `blog-simonwillison-vibe-game-development.md` Claim 5 (human playtesting is how interactive-system problems surface) is consistent with the human replay/confirm checkpoints here; Claim 6 there (build a working baseline, then escalate via follow-up prompts) matches the iterative feature-prompt flow here.
- **Contradicts**: None found.
- **Extends**: `blog-simonwillison-vibe-game-development.md` (iterative agent-built app) by adding a hardware/sensor-in-the-loop case.
- **Novel**: Agent-perceived physical sensing via browser microphones; an agent-built hot-swap code-delivery mechanism to remote clients; calibration by human-generated known signals in a sensing system. A search of existing notes found no notes on these.

## Guide Impact

- **Chapter 02 (harness engineering)**: Candidate example for "give the agent a live-deploy path and a readable observation channel" (installModule over WebSocket plus queryable audio logs). Must be paired with a caveat that arbitrary remote code execution was acceptable only in a trusted hobby setting; the source gives no safety guidance.
- **Chapter 03 (verification)**: Candidate short example of calibrating a sensing system with a known signal (claps) and of human replay-and-confirm gating before trusting detections. Do not present as measured evidence.
- **Chapter 01 (workflows)**: Weak support for spec-first (`problem.md`), cloud-scaffold then local-live-session splits for hardware work.

## Extraction Notes

- Read the full post (fetched raw HTML and stripped markup). Linked pages (BeepBeep paper, shared session, `problem.md`, `detector.js`) were not followed; their contents are known only through Willison's description.
- Single author, one hobby project, no failure analysis; all claims anecdotal. The "walk away" autonomy was only partly demonstrated: he reports sitting by the laptop chatting with Fable 5.2.
- Cross-referenced claim numbers verified against `blog-simonwillison-vibe-game-development.md`.
