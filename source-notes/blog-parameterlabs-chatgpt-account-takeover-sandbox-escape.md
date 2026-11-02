---
source_url: https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/
source_type: blog-post
title: "How We Took Over ChatGPT Accounts (Willison link post on the Parameter Labs write-up)"
author: Simon Willison (linking Parameter Labs)
date_published: 2026-10-31
date_extracted: 2026-11-02
last_checked: 2026-11-02
status: current
confidence_overall: emerging
issue: "#4483"
---

# How We Took Over ChatGPT Accounts

> A vendor-side, disclosed-and-fixed attack chain in which untrusted model-generated HTML in a sandboxed iframe escaped via a parent-page `postMessage` handler and a CSP allowlist entry, giving a layered-defense lesson for any team that renders LLM-generated HTML or artifacts.

## Source Context

- **Type**: blog-post (Willison link post, 2026-10-31) plus the primary write-up by Parameter Labs, "We found a gap at OpenAI" (https://www.parameter.ai/labs/we-found-a-gap-at-openai, Oct 2026), which was also read.
- **Author credibility**: Willison is a high-signal LLM tooling commentator. Parameter Labs is the security team that found the bug and reported it through OpenAI's bug bounty; the exploit details are theirs, not independently verified.
- **Scope**: One incident in ChatGPT's HTML Preview feature (formerly Canvas). It is not a claim about OpenAI's current architecture. Exploit details are deliberately kept at the level of failure points, not a usable recipe.

## Extracted Claims

### Claim 1: A parent-page message handler that trusts any sender is a hole in an otherwise sandboxed iframe
- **Evidence**: Parameter Labs: a MathLive listener on the main ChatGPT page accepted messages from any origin without verifying the sending window. An untrusted Preview frame could replace the on-screen keyboard layout with attacker-supplied HTML, and the helper handling that HTML did not sanitize it. Willison's summary says the receiving code used `innerHTML`.
- **Confidence**: emerging (one incident; vendor confirmed and fixed)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The per-frame sandbox was fine. The failure was a trusted third-party component on the parent page exposing a message bus any frame could reach. Sandbox strength equals the weakest parent-side handler.

### Claim 2: Injected markup could create a new iframe without sandbox restrictions
- **Evidence**: Willison's summary: this let untrusted code insert an iframe lacking the sandbox restrictions. Parameter Labs' recommendations include keeping dynamically created documents sandboxed when an untrusted frame can influence their content.
- **Confidence**: emerging
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Even where `innerHTML` does not run `<script>`, it can create frames, so "no script execution" is not a sufficient property.

### Claim 3: A CSP allowlist entry for a host with a reflective endpoint defeats "no inline script"
- **Evidence**: Parameter Labs: the CSP blocked inline scripts but allowed YouTube; a YouTube oEmbed endpoint accepted a JSONP callback parameter and echoed it back as JavaScript, even on an error response, giving code execution under the chatgpt.com origin.
- **Confidence**: emerging
- **Quote**: "It did, however, allow scripts from YouTube."
- **Our assessment**: Each allowlisted script host is part of the trust boundary. Allowlists should be audited for JSONP/callback-style reflection.

### Claim 4: A share link alone was enough to compromise another signed-in user, with private data reachable
- **Evidence**: Parameter Labs: the attacker publishes a conversation via normal sharing and sends the link; opening it is the only victim action. They listed private conversations, retrieved content never shared with the attacker, and sent a small piece of data to an external server. Willison: "it was trivial to fetch private user data from APIs."
- **Confidence**: emerging
- **Quote**: "an ordinary public ChatGPT share into attacker-controlled JavaScript"
- **Our assessment**: Shared artifacts are an attacker-to-victim delivery channel. Rendering LLM-generated content from other users is the real threat model, not just the owner's own session.

### Claim 5: Chaining three individually "ordinary" features produced the exploit
- **Evidence**: Parameter Labs: the attack combined a graph feature, the HTML Preview feature, and a public share into one chain.
- **Confidence**: emerging
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Feature-by-feature review misses cross-feature paths; threat models need to cover interactions.

### Claim 6: Recommended defenses are sender verification, no raw HTML in cross-window settings, sandboxed dynamic documents, and CSP as backup only
- **Evidence**: Parameter Labs' recommendations: verify both origin and the specific window granted permission; do not accept raw HTML across windows; keep dynamically created documents sandboxed; treat CSP as a backup control.
- **Confidence**: settled (standard web-security practice)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Matches conventional guidance; useful as a concrete checklist for agent-artifact renderers.

### Claim 7: Disclosure was fast and the bounty was modest
- **Evidence**: Timeline per Parameter Labs: MathLive path confirmed Oct 13; reported Oct 18; OpenAI reproduced and raised severity P2 to P1 on Oct 21; partial fixes and CSP changes Oct 22-23; both frontends rejected the messages and a $5,000 bounty was awarded Oct 26. Willison considered the bounty low for this severity.
- **Confidence**: anecdotal (vendor-reported timeline, single case)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Useful as evidence the issue was real (severity raised) and fixed; the bounty size is an opinion.

## Concrete Artifacts

```
Attack chain at the level of failure points (Parameter Labs, via Willison):
1. Sandboxed Preview frame -> postMessage -> parent-page MathLive handler -> unsanitized HTML written to the DOM
2. Injected markup creates a frame lacking sandbox restrictions
3. CSP allows YouTube; oEmbed endpoint reflects JS via callback parameter -> script runs on chatgpt.com origin
4. Authenticated API calls -> private data -> exfiltrated to an external server
Trigger: victim opens a crafted ChatGPT share URL.
```

## Cross-References

- **Corroborates**: `blog-green-sandboxing-rogue-agents.md` (Claim 5: sandboxes cannot perfectly isolate; here the leak is via a sanctioned channel) and `blog-simonwillison-smolmachines-untrusted-sandbox.md` (untrusted-code sandboxing as a boundary problem).
- **Contradicts**: None found.
- **Extends**: `blog-simonwillison-ai-worming-through-word.md` (AI-generated content as an exfiltration vector) by showing an app-level, non-prompt-injection route; `blog-anthropic-zero-trust-ai-agents.md` (Claim 4: controls should make the path non-existent rather than tedious), as the CSP allowlist and message bus were paths that existed.
- **Novel**: A concrete post-sandbox-escape chain (postMessage + innerHTML + CSP allowlist reflection) in a shipping AI product's artifact renderer. Distinct from `blog-simonwillison-prompt-injection-role-confusion.md`, which is model-level.

## Guide Impact

- **Chapter 06**: Add this incident as a worked example under the sandbox-as-control discussion for teams rendering LLM-generated HTML: audit parent-side message handlers, CSP-allowlisted hosts for reflective endpoints, and third-party embeds as part of the trust boundary. Frame as a threat-model lesson, not a claim about OpenAI's current state.
- **Chapter 02**: Optional one-line pointer for harnesses that render model-generated artifacts: serve them from a separate origin and avoid a shared message bus with the host page.

## Extraction Notes

- Read Willison's link post and the primary Parameter Labs write-up; both were retrieved via a summarizing fetch tool, so verbatim quotes are limited to the short fragments shown and other claims are paraphrased with "no direct quote". Please spot-check the two quotes against the source pages.
- The Willison post attributes `innerHTML`; the Parameter Labs text says the helper did not sanitize HTML. These are consistent, not contradictory.
- Evidence is a researcher's own account, vendor-confirmed fixed; exploit steps are intentionally not detailed.
