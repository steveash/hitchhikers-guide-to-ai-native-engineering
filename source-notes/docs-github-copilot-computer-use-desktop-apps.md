---
source_url: https://github.blog/changelog/2026-10-01-github-copilot-can-now-interact-with-desktop-apps/
source_type: docs
title: "GitHub Copilot can now interact with desktop apps with computer use"
author: GitHub (changelog)
date_published: 2026-10-01
date_extracted: 2026-10-02
last_checked: 2026-10-02
status: current
confidence_overall: emerging
issue: "#3855"
---

# GitHub Copilot can now interact with desktop apps with computer use

> GitHub ships computer use in public preview for Copilot CLI and the Copilot app (macOS, Windows), positioned as the fallback for GUI-only software with no API, CLI, or MCP integration, gated by per-app approval and org-level disable.

## Source Context

- **Type**: docs (official GitHub changelog entry, "1 minute read")
- **Author credibility**: First-party GitHub announcement; authoritative on what shipped, but it is a short capability announcement. It has no API shape, model list, benchmarks, or safety-model detail beyond the approval flow.
- **Scope**: Covers what Copilot can do, the control/approval model, how to enable it, and a prompting tip. Does not cover supported models, prompt-injection defenses, screenshot handling, reliability, or pricing. It links to separate docs ("computer use in GitHub Copilot CLI and the GitHub Copilot app"), which were not fetched.

## Extracted Claims

### Claim 1: Computer use is in public preview in both Copilot CLI and the Copilot app, on macOS and Windows only
- **Evidence**: Vendor announcement; no usage data.
- **Confidence**: settled (as a statement of availability)
- **Quote**: "Computer use is now available in public preview in GitHub Copilot CLI and the GitHub Copilot app on macOS and Windows."
- **Our assessment**: Preview status and no Linux support mean it is not yet a dependable part of a team harness. Surfaces are the terminal agent and the desktop app, not the cloud agent.

### Claim 2: The capability set is a general GUI action space, not only screenshots and clicks
- **Evidence**: Enumerated list in the announcement. The source lists the actions only; it says nothing about how they are implemented.
- **Confidence**: settled (as a statement of the advertised action list only; the implementation inference below is ungraded speculation)
- **Quote**: "reading accessible app content and visual context, clicking controls, entering and editing text, pressing keys, scrolling, dragging, and navigating workflows across applications"
- **Our assessment**: The action list is broad: reading, pointer, keyboard, scrolling, dragging and cross-app navigation. *Inference (ours, not stated in the source):* the phrase "accessible app content and visual context" may indicate a hybrid of accessibility-tree reads and screenshots. The source does not describe the mechanism, so the guide should not cite this note for a hybrid design.

### Claim 3: Computer use targets legacy and GUI-only software that lacks an API, CLI, or MCP integration
- **Evidence**: Positioning statement. It frames GUI control as the last resort after API, CLI, and MCP.
- **Confidence**: emerging
- **Quote**: "workflows in legacy and GUI-only software that do not provide an API, command-line interface, or MCP integration"
- **Our assessment**: This matches Anthropic's stance that connectors come first and computer use is the fallback (see Cross-References). Two vendors now state the same tool-preference ordering.

### Claim 4: Control model is approval-before-control, with a persistent per-app allowlist the user can review and reset
- **Evidence**: Described in the announcement; no detail on granularity or on what the approval prompt shows.
- **Confidence**: emerging
- **Quote**: "Copilot asks for approval before controlling an app, and you can review or reset apps that you have chosen to always allow."
- **Our assessment**: Similar to Anthropic's "permission before new app access" safeguard. The "always allow" list is a standing grant, which is a prompt-injection blast-radius question the source does not address.

### Claim 5: On macOS the feature guides the user through OS Accessibility and Screen Recording permissions
- **Evidence**: Single sentence.
- **Confidence**: settled
- **Quote**: "On macOS, computer use also guides you through the required Accessibility and Screen Recording permissions."
- **Our assessment**: The OS permissions requested fit, but do not confirm, the hybrid-design inference in Claim 2. They also mean the OS-level grants apply to the host process, so they are wider than the per-app approvals.

### Claim 6: Organizations can disable the feature through managed settings
- **Evidence**: One sentence; no key name or schema given.
- **Confidence**: settled
- **Quote**: "Organization-managed settings can disable the feature."
- **Our assessment**: Disable-only is a coarse admin control. Compare the finer-grained enterprise `sandbox` key documented for the Copilot app. The source does not say whether computer use is covered by the local sandbox.

### Claim 7: Enablement is a slash command in the CLI and a settings toggle in the app
- **Evidence**: Step-by-step instructions.
- **Confidence**: settled
- **Quote**: "In Copilot CLI, run /computer on. Use /computer show to check its status and /computer off to disable it." and "In the GitHub Copilot app, open Settings, select Computer Use, and turn on Enable Computer Use. You can also use /computer on."
- **Our assessment**: Three CLI commands (on, show, off) and an app settings toggle, with `/computer on` working in both surfaces. It is opt-in and off by default, and it is toggleable mid-session like `/sandbox`.

### Claim 8: Prompting guidance is outcome-first: state the outcome, the applications involved, and constraints
- **Evidence**: One-sentence tip with example tasks (summarize browser notifications, update a presentation, move information through a desktop workflow).
- **Confidence**: anecdotal
- **Quote**: "Computer use works best when you describe the outcome you want, the applications involved, and any important constraints."
- **Our assessment**: Reasonable but thin, with no evidence offered. Anthropic's best-practices post has far more specific guidance (resolution, effort, injection defense).

## Concrete Artifacts

```
# Copilot CLI (source: GitHub changelog, 2026-10-01)
/computer on     # enable
/computer show   # check status
/computer off    # disable

# GitHub Copilot app (same source)
Settings -> Computer Use -> "Enable Computer Use"   (or /computer on)
```

Example workflow shown in the source's image caption: "Copilot uses computer-use tools to navigate an expense-report workflow in Safari."

## Cross-References

- **Corroborates**: `blog-anthropic-dispatch-computer-use.md` Claim 1 (computer use is the fallback behind precise connectors) and Claim 3 (permission before new app access). `blog-anthropic-computer-use-best-practices.md` is the Anthropic implementation guide for the same pattern.
- **Contradicts**: None found. Anthropic's Claim 6 (early, slower, less reliable; limit to trusted apps) is not echoed by GitHub, which makes no reliability statement. That is an omission, not a disagreement, so no contradiction issue was filed.
- **Extends**: `docs-github-copilot-app-local-sandboxing.md` (Copilot app OS-level sandbox; the source does not say how the sandbox and computer use interact). `blog-cognition-devin-desktop.md` covers desktop agent management, not GUI control, so the overlap is only thematic.
- **Novel**: GitHub's `/computer on|show|off` control surface, the explicit "no API, CLI, or MCP" scoping, and macOS Accessibility + Screen Recording gating. These are the first Copilot computer-use material in the corpus.

## Guide Impact

No guide chapter currently covers computer use (no chapter in `guide/` mentions it), so this note offers new material rather than corrections.

- **Ch06 (Security Threat Model, `guide/06-security-threat-model.md`)**: Add GUI/computer-use control as an attack surface. The material: per-app approval with a standing "always allow" list (Claim 4), OS-level Accessibility and Screen Recording grants that are wider than per-app approval (Claim 5), and disable-only org control (Claim 6). Note the gap. GitHub documents approval and org disable but not prompt-injection scanning or a default denylist (Anthropic documents both). Do not claim parity on safety from this source alone.
- **Ch02 (Harness Engineering, `guide/02-harness-engineering.md`)**: In the permission-model and "Three-Tier Boundary System" material, support a tool-preference ladder of MCP/API, then CLI, then GUI control, with "Ask First" (per-app human approval) for the GUI tier. Cite the shared "last resort after API/CLI/MCP" ordering as two-vendor convergence (Claim 3 here, Claim 1 of the Anthropic dispatch note). The `/computer on|show|off` opt-in toggle (Claim 7) is a concrete example of an off-by-default capability switch.

## Extraction Notes

- Raw page HTML was fetched and read in full; quotes were checked against that text. On re-check (2026-10-02) the URL without a trailing slash returns a 301 to the trailing-slash URL, which returns 200. `source_url` now records the final URL. All quotes were re-verified against the live page. In Claim 7, the inline `<code>` markup and the bold UI labels are rendered as plain text. The page is a single short changelog entry, so claims are few (8) and the evidence is vendor assertion only.
- The linked "computer use in GitHub Copilot CLI and the GitHub Copilot app" docs and the related changelog entries (VS Code, new models) were not followed. A follow-up on the docs page would likely yield the safety and model details missing here.
- Prospector comments asked about model support and API shape; the source states neither.
