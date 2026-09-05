---
source_url: https://simonwillison.net/2026/Sep/1/codex-libreoffice/
source_type: blog-post
title: "Codex bundles LibreOffice"
author: Simon Willison
date_published: 2026-09-01
date_extracted: 2026-09-05
last_checked: 2026-09-05
status: current
confidence_overall: emerging
issue: "#3246"
---

# Codex bundles LibreOffice

> Simon Willison's incidental discovery, via a disk-usage tool, that OpenAI's ChatGPT desktop app (formerly branded "Codex") caches 1.7GB of local runtime dependencies — including a full headless LibreOffice install, Poppler, git, Python, and Node.js — with a "skills" folder that tells the agent how to find and use them.

## Source Context

- **Type**: blog-post (Willison "link-blog" observational format — a short factual writeup of something he noticed, with a screenshot, no extended analysis)
- **Author credibility**: Simon Willison is the creator of Django and the `llm` CLI, and one of the most widely-cited practitioner commentators on LLM tooling. This post is a first-hand technical observation (his own machine, his own disk-usage inspection) rather than secondhand reporting — independently verifiable by any user of the app who inspects the same cache path. No vendor affiliation disclosed.
- **Scope**: The post covers exactly one thing: the directory structure and file sizes of `~/.cache/codex-runtimes/codex-primary-runtime/` on his macOS machine, plus one sentence about a "skills" folder that wires the agent to the bundled binaries. It does NOT cover: why OpenAI bundles these dependencies, whether other platforms (Windows/Linux) have the same footprint, version numbers of the bundled tools, how the skills invoke the binaries in practice, disk-space or performance implications, or any comparison to how competing AI tools handle the same problem.

## Extracted Claims

### Claim 1: The ChatGPT desktop app (formerly the OpenAI Codex desktop app) caches approximately 1.7GB of runtime dependencies at `~/.cache/codex-runtimes/codex-primary-runtime/` on macOS
- **Evidence**: First-hand filesystem inspection using OmniDiskSweeper (a macOS disk-usage application), with a screenshot showing the folder and its byte-exact size.
- **Confidence**: settled (direct, independently reproducible first-hand observation by a credible technical author)
- **Quote**: "The OpenAI Codex desktop app (since rebranded to just ChatGPT) has 1.7GB of stuff in there in a folder called `codex-primary-runtime`"
- **Our assessment**: This is a concrete, checkable data point about the local footprint of a mainstream AI desktop app. 1.7GB is a substantial download/cache size for what most users would assume is a lightweight chat client — this is the kind of footprint normally associated with an IDE or a full development toolchain, not a chat app.

### Claim 2: Within the runtime cache, the largest single bundled dependency is a full headless LibreOffice install at 429.7 MB, alongside Poppler (187.9 MB) and git (148.1 MB)
- **Evidence**: Screenshot of the `native/` subfolder contents with per-item byte counts, described column-by-column in the post.
- **Confidence**: settled (direct filesystem measurement)
- **Quote**: "Fourth column: 429.7 MB libreoffice-headless (selected), 187.9 MB poppler, 148.1 MB git"
- **Our assessment**: Bundling a full headless LibreOffice install — rather than, say, calling a cloud conversion API — signals that OpenAI treats office-document conversion (docx/xlsx/pptx and similar) as a core, always-available local agent capability, not an optional or server-side one. Poppler (PDF rendering/extraction) reinforces the same pattern for PDF handling specifically.

### Claim 3: The runtime cache also bundles complete standalone Python and Node.js installations, alongside the native binaries
- **Evidence**: Directory breakdown of `codex-primary-runtime/` showing a `python/` folder (440.6 MB) and a `node/` folder (446.4 MB) as siblings to `native/` (771.0 MB), `plugins/` (6.3 MB), and `runtime.json` (4.1 kB).
- **Confidence**: settled (direct filesystem measurement)
- **Quote**: "...including a full Python installation, a full Node.js installation"
- **Our assessment**: Bundling entire language runtimes locally means the agent's code-execution tooling works out of the box regardless of what's installed on the host machine, trading disk footprint for zero-setup reliability. This is the same tradeoff make/buy decision practitioners face when building their own agent harnesses: ship your own hermetic toolchain, or depend on (and detect/handle the absence of) whatever the user's system already has.

### Claim 4: A "skills" folder nested inside the runtime's plugins directory is what tells Codex how to find and use the bundled binaries
- **Evidence**: Willison names the specific nested path and states its function directly.
- **Confidence**: settled (stated directly by the author, describing his own inspection of the folder contents)
- **Quote**: "The `~/.cache/codex-runtimes/codex-primary-runtime/plugins/openai-primary-runtime/plugins/documents` folder includes skills which tell Codex how to find and use those binaries."
- **Our assessment**: This confirms OpenAI uses a "skill = packaged instructions + resources that wire an agent to a capability" pattern structurally similar to what Anthropic documents for Claude Code (see Cross-References) — except here the resource being wired up is a locally bundled native binary rather than an internal API, script, or team convention. This is evidence that "skill" (or an equivalent packaging concept) is converging as the general mechanism by which agent harnesses declare "how to use this capability," regardless of vendor or what the underlying capability actually is.

### Claim 5: The discovery was incidental — Willison found this while browsing disk usage generally, not while investigating Codex's architecture
- **Evidence**: The author states his discovery method directly in the opening line of the post.
- **Confidence**: settled (author's own account of how he found this)
- **Quote**: "I was poking around in my `~/.cache/` folder using OmniDiskSweeper when I spotted something interesting."
- **Our assessment**: Because the discovery was incidental rather than the result of OpenAI's own documentation or disclosure, this tells us the bundling is not something OpenAI surfaces to users — the only reason it's known at all is that a technically curious user happened to inspect disk usage with a dedicated tool. Practitioners evaluating desktop AI agent apps for their own machines (or for rollout to a team) should not assume vendor documentation will disclose local dependency footprints or contents; direct inspection may be the only way to know what an app actually installs.

### Claim 6: The app under discussion was previously named "OpenAI Codex" (desktop app) and has since been rebranded to just "ChatGPT"
- **Evidence**: Explicit parenthetical in the post's own framing of the app.
- **Confidence**: settled (stated directly)
- **Quote**: "The OpenAI Codex desktop app (since rebranded to just ChatGPT)"
- **Our assessment**: This is a naming/identity note relevant to practitioners tracking OpenAI's product lineup — the "Codex" name has been used for multiple distinct things over time (a CLI, a model tier, and now this desktop app that has since dropped the name). Readers cross-referencing this note against `blog-simonwillison-codex-base-instructions.md` (which covers the Codex CLI's model system prompts) should not assume the two posts describe the same product surface — one is CLI model behavior, this one is the desktop app's local runtime footprint.

### Claim 7: The post itself offers no editorial judgment — no stated rationale for the bundling, no comparison to other AI tools, and no opinion on whether this is good or bad practice
- **Evidence**: Confirmed by close reading of the full post: it consists of the disk-usage discovery, the directory/size breakdown, and the one sentence about the skills folder, with no further discussion.
- **Confidence**: settled (absence confirmed directly)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This matters for how much interpretive weight this source note can carry. All "why this matters for practitioners" framing in this note's Our assessment and Guide Impact sections is the Miner's own synthesis, not sourced editorial judgment from Willison — he reports the finding and stops. Readers should not attribute the "local bundling vs. API orchestration" framing used elsewhere in this note to Willison himself.

## Concrete Artifacts

### Runtime cache directory breakdown (from the post's screenshot, macOS)

```
~/.cache/codex-runtimes/codex-primary-runtime/          1.7 GB total
├── dependencies/
│   ├── native/                                         771.0 MB
│   │   ├── libreoffice-headless                        429.7 MB
│   │   ├── poppler                                      187.9 MB
│   │   ├── git                                          148.1 MB
│   │   ├── libheif                                        4.7 MB
│   │   └── jxrlib                                       679.9 kB
│   ├── node/                                            446.4 MB
│   └── python/                                          440.6 MB
├── plugins/                                               6.3 MB
│   └── openai-primary-runtime/plugins/documents/
│       └── (skills that tell Codex how to find/use the binaries above)
└── runtime.json                                           4.1 kB

Source: Simon Willison, "Codex bundles LibreOffice," simonwillison.net,
2026-09-01, discovered via OmniDiskSweeper (macOS disk-usage app).
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-claude-code-skills-lessons.md` (Claim 4): That note documents Anthropic's first-party description of Claude Code skills as "folders that can include scripts, assets, data, etc. that the agent can discover, explore and manipulate" — not just markdown instructions. This source's Claim 4 (a "skills" folder wiring Codex to bundled native binaries) is an independent, cross-vendor data point for the same underlying pattern: a skill is a packaged bridge between an agent and a concrete local resource, not just prose guidance.
  - `docs-github-copilot-agent-skills-cli.md` (Claim 1): That note documents GitHub's `gh skill` package manager, which defines agent skills as "portable sets of instructions, scripts, and resources that teach AI agents how to perform specific tasks." This source's discovery of a Codex-specific skills folder tied to bundled binaries is consistent with that definition, adding a third vendor (OpenAI, alongside Anthropic and GitHub's cross-host spec) observed using the skills-as-capability-wiring pattern — though this source shows no evidence OpenAI's implementation follows the same agentskills.io spec; the two are only conceptually, not technically, confirmed to align.

- **Contradicts**: None identified. The closest tension is with `blog-simonwillison-accenture-pdf-tokens.md` (Claim 3), where Willison separately argues that PDFs are a poor medium for information transfer and that converting PDFs to images/markdown is a major token cost driver for enterprises. This is not a contradiction: this source shows OpenAI bundling non-LLM, local document-conversion tooling (Poppler, LibreOffice) that would let some document handling happen without burning model tokens at all — a plausible architectural response to the exact cost problem Willison raises in the other post, not a conflicting claim. No contradiction issue filed.

- **Extends**:
  - `blog-simonwillison-codex-base-instructions.md`: That note documents the behavioral/system-prompt layer of OpenAI's Codex model family (via the open-source `models.json`). This source documents a different layer of the same product family's stack: the local runtime and tool-provisioning layer bundled with the desktop app. Together they give a fuller picture of the Codex/ChatGPT agent stack — what the model is instructed to do, and what local capabilities it actually has bundled to do it with. Note the naming caveat in Claim 6: the base_instructions note covers the Codex CLI's model configs, while this note covers the separately-branded desktop app; they should not be treated as describing the identical product surface.

- **Novel**:
  - **First in-corpus evidence of a vendor bundling full native GUI-application binaries (LibreOffice, Poppler) inside an AI agent's local runtime**, as opposed to routing document conversion through a cloud API or requiring the user's own system installs. Prior corpus sources on document/PDF handling (`blog-simonwillison-accenture-pdf-tokens.md`) discuss the token-cost problem of LLM-based document conversion; none document a vendor's local, non-LLM tooling response to it.
  - **First in-corpus concrete disk-footprint data point for a desktop AI agent app** (1.7GB, broken down by component) — a practical fact for anyone evaluating desktop AI tools for rollout to machines with constrained storage.
  - **First in-corpus example of a "skills" folder wiring an agent to pre-installed local native executables** rather than to authored task instructions, internal APIs, or team conventions (contrast with the Claude Code and GitHub skills examples in Corroborates, which are about packaging knowledge/scripts, not wrapping bundled third-party GUI-application binaries).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: The guide's coverage of skills-as-extension-points (anchored on `blog-anthropic-claude-code-skills-lessons.md` and `docs-github-copilot-agent-skills-cli.md`) currently frames skills as author-written packages of instructions/scripts/data. Add this source as a data point showing the pattern extends to wiring an agent to large, pre-bundled native binaries the vendor ships alongside the app — not just to author-created content. Practical note for practitioners building or evaluating agent harnesses: "skill" as a concept spans everything from a markdown runbook to a folder that hands an agent an entire bundled LibreOffice install.
- **Chapter 04 (Context Engineering)**: If the guide discusses document ingestion (PDF/Office file handling) as a context-engineering concern, add this source as evidence that at least one major vendor addresses document conversion via bundled local tooling (LibreOffice, Poppler) rather than exclusively through model-mediated conversion — relevant to practitioners weighing whether to build their own local conversion pipeline versus routing documents through the model directly (which `blog-simonwillison-accenture-pdf-tokens.md` shows can be token-expensive).

## Extraction Notes

- **Source is very short (~150-200 words)**: This is a Willison "link-blog" observational post — screenshot plus a few sentences, no extended analysis, no comparison to other tools, no stated rationale for the bundling. All 7 claims above exhaust the post's substantive content; claim 7 explicitly documents this absence of editorializing so the Assayer and Smith don't mistake the Miner's own synthesis (in Our assessment / Guide Impact) for sourced claims.
- **No sub-pages followed**: The post links only to general reference pages (OmniDiskSweeper's own site, the LibreOffice and Poppler project pages) which are not substantive for extraction purposes — they describe the linked tools generally, not anything about Codex's use of them. Per MINER.md §1, these were not among the "up to 5 linked pages that seem substantive."
- **Quotes verified via multiple targeted WebFetch passes**: The live page could not be reproduced in full (WebFetch declines full verbatim reproduction for copyright reasons), so all quotes here were obtained via several targeted fetch requests asking for specific verbatim sentences, cross-checked against each other for consistency across passes. The Assayer should spot-check all quotes against the live URL: https://simonwillison.net/2026/Sep/1/codex-libreoffice/
- **Confidence set to `emerging` at the note level** despite most individual claims being `settled`: each individual factual claim (sizes, paths, quotes) is a directly-observed, checkable fact from a credible first-hand source, but the note as a whole rests on a single practitioner's single-machine observation of one vendor's app at one point in time (macOS only; no confirmation for Windows/Linux; no vendor confirmation or documentation; could change in a future app update). The guide-impact framing (bundling as a deliberate architecture strategy) is the Miner's inference, not a vendor-confirmed design rationale.
- **Three duplicate Prospector triage comments were present on the issue** with inconsistent chapter numbers/novelty ratings (medium / high / medium-high) and different chapter suggestions (Ch01-Ch05 variously). All three were read; none contained information not independently verifiable from the source itself, so none changed the extraction. Guide Impact above targets Ch02 and Ch04 based on this Miner's own read of actual guide chapter contents (`guide/02-harness-engineering.md`, `guide/04-context-engineering.md`), not the triage comments' chapter numbers, since the three triage comments disagreed with each other.
