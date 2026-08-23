---
source_url: https://simonwillison.net/2026/Aug/13/llm-gemini/
source_type: blog-post
title: "llm-gemini 0.33"
author: Simon Willison
date_published: 2026-08-13
date_extracted: 2026-08-23
last_checked: 2026-08-23
status: current
confidence_overall: settled
issue: "#2877"
---

# llm-gemini 0.33

> A release-note post (Willison "beat" format) announcing llm-gemini 0.33, which adds Gemini 3.7 Flash plus three other new models and two embedding models, and — more substantively, per the linked GitHub release notes — brings the plugin up to date with LLM 0.32's structured-message and typed-streaming-event architecture: visible reasoning traces, replayable Gemini "thought signatures" across tool-use turns, and native Google Search/URL-context/code-execution server-side tools exposed through LLM's provider-agnostic `-T` interface.

## Source Context

- **Type**: blog-post (Willison "beat" format — a short link-blog post combining his own commentary with a linked GitHub release page; same minimal format as the predecessor note `blog-simonwillison-llm-gemini-032.md`). Unlike that predecessor, the linked GitHub release notes for 0.33 are substantially richer (six detailed bullets vs. one line for 0.32), so this note draws claims from both the blog post prose and the GitHub release body.
- **Author credibility**: Simon Willison is the creator of the `llm` CLI and, per the GitHub release credits, a direct contributor to this llm-gemini release alongside at least two external contributors (John Blomberg, Andrew Hoddinott) credited by name for specific PRs. First-party release documentation from the plugin's maintainer.
- **Scope**: Covers the llm-gemini 0.33 plugin release only — new/removed model slugs, LLM 0.32 compatibility work, server-side tool support, embedding-model changes, and Willison's own pelican-benchmark test of Gemini 3.7 Flash's thinking-effort levels. Does NOT include a deep dive on Gemini 3.7 Flash's model card, benchmarks, or pricing (a separate Google blog post, fetched only for GA-status corroboration; see Extraction Notes) — nor does it cover the underlying llm 0.32 architecture in detail (already mined in `blog-simonwillison-llm032.md`).

## Extracted Claims

### Claim 1: llm-gemini 0.33 adds Gemini 3.7 Flash plus three other new chat models and two new embedding models, arriving after an unusually long gap since the prior release
- **Evidence**: Direct statement opening the blog post; model list corroborated by the GitHub release notes' second and third bullets.
- **Confidence**: settled (first-party; model slugs independently confirmed in the GitHub release body)
- **Quote**: "It's been a while since the last llm-gemini release. This version of the plugin adds support for today's Gemini 3.7 Flash release, plus gemini-3.6-flash, gemini-3.5-flash-lite and two embedding models gemini-embedding-2 and gemini-embedding-001."
- **Our assessment**: The gap is measurable against the corpus: the predecessor note (`blog-simonwillison-llm-gemini-032.md`) documents llm-gemini 0.32 shipping May 19, 2026; this release is dated August 13, 2026 — roughly three months, versus the single-feature, same-day-as-GA pattern documented for 0.32. That gap, plus the release notes' scope (an architecture upgrade, not just a model add), suggests 0.33 was held back to land alongside LLM 0.32 compatibility work rather than rushed out for Gemini 3.7 Flash's launch day.

### Claim 2: llm-gemini 0.33 is updated for LLM 0.32's structured-message and typed-streaming APIs, with reasoning, tool calls, and tool results now emitted as typed stream events, Gemini "thought signatures" preserved and replayed across tool-use turns, and stateless `messages=` histories replayed correctly — and the plugin now requires LLM 0.32 or later
- **Evidence**: GitHub release notes, first bullet (github.com/simonw/llm-gemini/releases/tag/0.33, PR #132).
- **Confidence**: settled (first-party changelog entry, specific PR referenced)
- **Quote**: "Updated for LLM 0.32's structured message and streaming APIs. Reasoning, tool calls and tool results are now emitted as typed stream events, Gemini thought signatures are preserved and replayed across tool-use turns and stateless `messages=` histories are replayed correctly. This release requires LLM 0.32 or later."
- **Our assessment**: This is the direct fulfillment of the "coming soon" gap flagged in `blog-simonwillison-llm032.md` Claim 13, which stated that as of the August 4, 2026 LLM 0.32 stable release, "llm-gemini, llm-openrouter, and llm-mistral" were "nearly there, releases coming soon" for full streaming-events participation, with only `llm-anthropic` fully updated at that time. This release, nine days later, is that arrival for the Gemini plugin. The "thought signatures... preserved and replayed across tool-use turns" detail is new in-corpus information about how Gemini's reasoning state survives a multi-turn tool loop — distinct from mere reasoning-trace *display* (already covered for the LLM core library in `blog-simonwillison-llm032.md` Claim 2) and closer to the mechanics that make server-side tool use with reasoning models actually work correctly across turns.

### Claim 3: The plugin now exposes Google Search, URL context, and code execution as LLM server-side tools via `-T GoogleSearch`, `-T URLContext`, and `-T CodeExecution`, with native Gemini server-side tool calls/results exposed as structured events, and Gemini 3 models able to combine server-side tools with local function tools in the same request
- **Evidence**: GitHub release notes, fifth bullet (PR/issue #141); demonstrated with a concrete CLI example in the blog post.
- **Confidence**: settled (first-party changelog plus a runnable example)
- **Quote**: "Google Search, URL context and code execution now use LLM's server-side tool interface and can be enabled using `-T GoogleSearch`, `-T URLContext` and `-T CodeExecution`. Native Gemini server-side tool calls and results are exposed as structured events, and Gemini 3 models can combine server-side tools with local function tools."
- **Our assessment**: This mirrors the server-side tool pattern `blog-simonwillison-llm032.md` Claim 4 and Claim 5 documented for OpenAI (`-T CodeInterpreter`) and Anthropic (`-T WebSearch`, `-T WebFetch`, `-T CodeExecution`, `-T AnthropicMCP`) — Gemini is now the third major provider plugin exposing provider-executed tools through the same `-T` flag convention. The detail that Gemini 3 models can mix server-side and local function tools in one request is new and not previously documented for the other two providers in this corpus; worth flagging as a Gemini-specific capability rather than assuming parity across providers without direct confirmation.

### Claim 4: The plugin demonstrates server-side code execution with a single CLI invocation
- **Evidence**: Runnable command shown directly in the blog post body.
- **Confidence**: settled (first-party, concrete command)
- **Quote**: "llm -m gemini-3.7-flash -T CodeExecution \\\n  'use python to calculate (factorial of 13) * 3'"
- **Our assessment**: A minimal, copy-pasteable validation of Claim 3's `-T CodeExecution` flag — the kind of one-liner practitioners can run immediately to confirm the upgrade works, consistent with the "concrete runnable example" pattern seen throughout `blog-simonwillison-llm032.md`.

### Claim 5: Google Search grounding now preserves Gemini's raw `groundingMetadata` unaltered, and search suggestions are emitted as display-only events (shown on stderr by the CLI) rather than being mixed into response text, logs, or subsequent conversation turns
- **Evidence**: GitHub release notes, sixth bullet, credited to external contributor Andrew Hoddinott (PR #40).
- **Confidence**: settled (first-party changelog entry with named external contributor and PR reference)
- **Quote**: "Google Search grounding now retains Gemini's raw `groundingMetadata` without altering the model's response text. Search suggestions are emitted as display-only events—shown on standard error by the CLI—so they are excluded from response text, logs and subsequent conversation turns."
- **Our assessment**: This is a data-hygiene fix as much as a feature: without it, search-suggestion UI hints could silently leak into logged conversation history and get replayed as if they were part of the actual dialogue on later turns — a subtle correctness bug for anyone building multi-turn agents on top of Gemini's grounded search. The stderr-for-side-channel-metadata pattern matches the reasoning-trace-to-stderr convention documented in `blog-simonwillison-llm032.md` Claim 2, suggesting stderr is becoming the `llm` ecosystem's general convention for "informational but not part of the conversation" output.

### Claim 6: llm-gemini 0.33 adds `gemini-embedding-2` and `gemini-embedding-001` as embedding models (each with `-768` and `-1536` dimension variants), removes the deprecated `text-embedding-004` and `gemini-embedding-exp-03-07` models, and warns that the two supported embedding models use incompatible vector spaces requiring re-embedding when switching
- **Evidence**: GitHub release notes, fourth bullet, credited to external contributor John Blomberg (PR #138).
- **Confidence**: settled (first-party changelog, explicit migration warning)
- **Quote**: "Added the `gemini-embedding-2` and `gemini-embedding-001` embedding models, each with `-768` and `-1536` variants for smaller vectors. The deprecated `text-embedding-004` and `gemini-embedding-exp-03-07` models have been removed. The two supported models use incompatible vector spaces, so existing collections must be re-embedded when switching between them."
- **Our assessment**: This is the first in-corpus documentation of Gemini embedding models being accessible through the `llm` CLI/plugin ecosystem — prior corpus coverage of `llm`'s embedding capabilities has been OpenAI/local-model focused. The explicit incompatible-vector-space warning is a concrete operational hazard worth flagging for any harness using `llm embed` against a vector store: swapping embedding models silently invalidates similarity search over previously-embedded content unless the whole collection is re-embedded.

### Claim 7: llm-gemini 0.33 removes 35 unavailable Gemini models — including retired Gemini 1.5 and 2.0, Gemma 3, and experimental/preview models — so the plugin's registry now reflects only model IDs verified to accept live `generateContent` requests
- **Evidence**: GitHub release notes, final bullet (issue #142).
- **Confidence**: settled (first-party changelog, specific count and verification method stated)
- **Quote**: "Removed 35 unavailable Gemini models, including retired Gemini 1.5 and 2.0, Gemma 3, experimental and preview models. The registry now reflects model IDs verified to accept live `generateContent` requests."
- **Our assessment**: A large one-time cleanup (35 models) rather than incremental pruning, and notable for the verification method: models were checked against live API behavior rather than removed on a schedule. This is a different mechanism from the advance-notice deprecation pattern documented in `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` (GitHub Copilot retiring Gemini 2.5 Pro/Gemini 3 Flash on a fixed 29-day-notice date) — the `llm-gemini` plugin instead reactively prunes model slugs that have already stopped working upstream, with no advance-notice period for plugin users. Practitioners pinning specific Gemini model slugs in scripts should not assume a deprecation grace period from this plugin's registry.

### Claim 8: Willison tested Gemini 3.7 Flash with his standard "pelican riding a bicycle" benchmark at three thinking-effort levels (high, medium, low), noting that the "minimal" effort option available in Gemini 3.6 Flash has been removed in 3.7
- **Evidence**: Direct statement in the blog post, with a linked SVG rendered by the model.
- **Confidence**: settled (first-party test, described same-day as the release)
- **Quote**: "I had Gemini 3.7 Flash draw me some pelicans riding bicycles at high, medium, and low thinking efforts (minimal, which was an option in 3.6 Flash, has been removed in 3.7.) Here's the high level one, which is pretty great:"
- **Our assessment**: This continues the "plugin update → immediate pelican benchmark → notes published same day" pattern already documented as a repeatable practitioner-validation habit in `blog-simonwillison-llm-gemini-032.md` Claim 3 (there, the third in-corpus instance; this is a further data point). The specific detail — that Gemini 3.7 Flash drops the "minimal" thinking-effort tier present in 3.6 Flash, leaving high/medium/low — is a concrete model-capability change worth noting for anyone comparing Gemini reasoning-effort controls across generations; it runs in the opposite direction from Anthropic's Claude 5 models, where `blog-simonwillison-llm032.md`'s Concrete Artifacts section documents `thinking_effort` options as "low, medium, high, xhigh, or max" (a wider, not narrower, effort range).

### Claim 9: Willison later issued a public correction: an SVG rendering glitch he had originally attributed to Gemini 3.7 Flash producing invalid SVG was in fact caused by a bug in his own rendering tool, which he then fixed
- **Evidence**: A dated "Update" appended to the post the following day.
- **Confidence**: settled (first-party, explicit self-correction with a linked commit fixing the bug)
- **Quote**: "Update 14th August 2026: I had originally said that the SVG rendered incorrectly in Chrome and Firefox, and blamed Gemini 3.7 Flash for producing invalid SVG. That was entirely incorrect: the rendering glitch was my fault, caused by a bug In my rendering tool. I've now fixed that bug."
- **Our assessment**: Worth extracting as a methodological caution rather than a model-capability claim: the pelican-SVG benchmark's output is only as reliable as the renderer used to display it, and a rendering-tool bug can look identical to a model producing invalid output. Anyone citing the pelican benchmark as a comparative capability signal should note that at least one instance of an apparent model failure in this corpus's primary benchmark source turned out to be tooling error, corrected within 24 hours by the same author who originally reported it.

## Concrete Artifacts

### CLI: server-side code execution via the upgraded Gemini plugin
```bash
llm -m gemini-3.7-flash -T CodeExecution \
  'use python to calculate (factorial of 13) * 3'
```
*Source: simonwillison.net/2026/Aug/13/llm-gemini/*

### GitHub release notes (verbatim, github.com/simonw/llm-gemini, tag 0.33, published 2026-08-13T19:37:34Z)
```
- Updated for LLM 0.32's structured message and streaming APIs. Reasoning,
  tool calls and tool results are now emitted as typed stream events,
  Gemini thought signatures are preserved and replayed across tool-use
  turns and stateless `messages=` histories are replayed correctly.
  This release requires LLM 0.32 or later. #132
- New model `gemini-3.7-flash` for Gemini 3.7 Flash. #145
- New models `gemini-3.6-flash` and `gemini-3.5-flash-lite` for
  Gemini 3.6 Flash and Gemini 3.5 Flash-Lite. #139
- Added the `gemini-embedding-2` and `gemini-embedding-001` embedding
  models, each with `-768` and `-1536` variants for smaller vectors.
  The deprecated `text-embedding-004` and `gemini-embedding-exp-03-07`
  models have been removed. The two supported models use incompatible
  vector spaces, so existing collections must be re-embedded when
  switching between them. Thanks, John Blomberg. #138
- Google Search, URL context and code execution now use LLM's
  server-side tool interface and can be enabled using `-T GoogleSearch`,
  `-T URLContext` and `-T CodeExecution`. Native Gemini server-side tool
  calls and results are exposed as structured events, and Gemini 3
  models can combine server-side tools with local function tools. #141
- Google Search grounding now retains Gemini's raw `groundingMetadata`
  without altering the model's response text. Search suggestions are
  emitted as display-only events—shown on standard error by the
  CLI—so they are excluded from response text, logs and subsequent
  conversation turns. Thanks, Andrew Hoddinott. #40
- Removed 35 unavailable Gemini models, including retired Gemini 1.5
  and 2.0, Gemma 3, experimental and preview models. The registry now
  reflects model IDs verified to accept live `generateContent`
  requests. #142
```
*Source: GitHub API, github.com/simonw/llm-gemini/releases/tags/0.33*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-llm-gemini-032.md` Claim 3: The "plugin update → immediate pelican benchmark → notes published same day" pattern recurs here (Claim 8), now with a fourth in-corpus data point.
  - `blog-ghaw-weekly-2026-08-17.md` Claim 5: That note documents gh-aw v0.87.0 adding Gemini 3.7 Flash to its supported-model inventory the same week this plugin release shipped — independent corroboration that Gemini 3.7 Flash's August 13, 2026 GA launch was tracked essentially simultaneously across at least two separate tools in the corpus.

- **Contradicts**: None identified.

- **Extends**:
  - `blog-simonwillison-llm032.md` Claim 13: That note documented `llm-gemini` as one of three model-provider plugins (with `llm-openrouter`, `llm-mistral`) described as "nearly there, releases coming soon" for full LLM 0.32 streaming-events compatibility, as of the August 4, 2026 stable release with only `llm-anthropic` fully updated. This source (Claim 2) is the actual llm-gemini release fulfilling that forecast, nine days later.
  - `blog-simonwillison-llm032.md` Claims 4 and 5: Those claims documented server-side tools for OpenAI (`-T CodeInterpreter`) and Anthropic (`-T WebSearch`, `-T WebFetch`, `-T CodeExecution`, `-T AnthropicMCP`). This source (Claim 3) extends the same `-T`-flag server-side-tool pattern to Gemini (`-T GoogleSearch`, `-T URLContext`, `-T CodeExecution`), making it the third provider plugin in-corpus to expose provider-executed tools through LLM's unified interface.
  - `blog-simonwillison-llm-gemini-032.md`: The direct predecessor release (0.32, May 19, 2026, single-feature `gemini-3.5-flash` addition). This note documents the next release in the same plugin's version history, roughly three months later and substantially larger in scope.

- **Novel**:
  - First in-corpus documentation of Gemini "thought signatures" being preserved and replayed across tool-use turns — a reasoning-state-continuity mechanism distinct from the reasoning-trace *display* mechanics already documented for the LLM core library.
  - First in-corpus documentation of Gemini embedding models (`gemini-embedding-2`, `gemini-embedding-001`) accessible via the `llm` CLI/plugin ecosystem, including the incompatible-vector-space migration hazard.
  - First in-corpus documentation of a Gemini-specific capability (combining server-side and local function tools in a single Gemini 3 request) not yet confirmed for the OpenAI or Anthropic plugins in this corpus.
  - First in-corpus example of a self-correction/erratum on a pelican-benchmark result, useful as a citable caution about attributing rendering artifacts to model behavior without first ruling out the renderer.

## Guide Impact

- **Chapter 02 (Harness Engineering — server-side tool patterns)**: Add Gemini's `-T GoogleSearch`, `-T URLContext`, `-T CodeExecution` flags as the third documented provider (alongside OpenAI's `-T CodeInterpreter` and Anthropic's `-T WebSearch`/`-T WebFetch`/`-T CodeExecution`/`-T AnthropicMCP` from `blog-simonwillison-llm032.md`) using LLM's unified server-side tool interface. Note the Gemini-specific detail that Gemini 3 models can combine server-side and local function tools in one request — worth flagging as a capability to verify before assuming parity with other providers. Cite Claims 3 and 4.
- **Chapter 01 (Daily Workflows — model access)**: Update any `llm`/`llm-gemini` model-slug references to include `gemini-3.7-flash`, `gemini-3.6-flash`, `gemini-3.5-flash-lite`, and note that this plugin release removed 35 stale model slugs (retired Gemini 1.5/2.0, Gemma 3, experimental/preview) — practitioners with hardcoded older Gemini slugs in scripts should expect them to start failing after upgrading the plugin. Cite Claim 7.
- **Chapter 05 (Orchestration & Integration — embeddings/RAG)**: If the guide covers embedding-model selection via `llm embed`, add Gemini's `gemini-embedding-2`/`gemini-embedding-001` as an access path and flag the incompatible-vector-space re-embedding requirement as an operational hazard when switching embedding models on an existing vector store. Cite Claim 6.
- **Chapter 03 (Tooling & Developer Experience — reasoning-effort controls)**: If the guide compares reasoning-effort controls across model families, note that Gemini 3.7 Flash narrowed its thinking-effort tiers to high/medium/low (removing "minimal," present in 3.6 Flash), while Anthropic's Claude 5 models widened theirs to low/medium/high/xhigh/max per `blog-simonwillison-llm032.md` — the two ecosystems are moving in opposite directions on effort-tier granularity. Cite Claim 8.

## Extraction Notes

- **Fetched three sources**: the blog post itself (via `curl` + HTML-stripping, all quotes verified character-for-character against the raw HTML including the exact code-block formatting), the GitHub release notes (via `gh api repos/simonw/llm-gemini/releases/tags/0.33`, raw markdown body), and the linked Google blog announcement for Gemini 3.7 Flash (fetched only to corroborate GA status and announcement date — not deeply mined, as the guide-relevant content for this issue is the plugin/tooling layer, not the model's own benchmark card).
- **The GitHub release notes carry most of the substantive claims**: the blog post itself is a thin "beat" (same minimal format as the 0.32 predecessor), but unlike 0.32 the linked release notes for 0.33 are unusually detailed (six bullets covering architecture, three model families, embeddings, server-side tools, grounding-metadata handling, and registry cleanup) — reading past the blog post into the release notes was necessary to avoid a shallow extraction, consistent with MINER.md §1's instruction to follow substantive linked pages.
- **No contradictions found requiring MINER.md §4a filing**: the only tension identified (Gemini 3.7 Flash narrowing thinking-effort tiers while Claude 5 widened them, Claim 8's Our assessment) is a cross-provider capability difference, not two sources disagreeing about the same fact — not a contradiction under MINER.md's "conditioning variable" guidance.
- **Cross-reference verification performed**: `blog-simonwillison-llm-gemini-032.md` Claim 3 confirmed at lines 40-45 (pelican-benchmark pattern, third instance stated there). `blog-simonwillison-llm032.md` Claim 13 confirmed at lines 98-102 (the "nearly there, releases coming soon" quote for llm-gemini/llm-openrouter/llm-mistral). `blog-simonwillison-llm032.md` Claims 2, 4, 5 confirmed at lines 32-54 (reasoning-to-stderr default, OpenAI CodeInterpreter, Anthropic server-side tools). `blog-simonwillison-llm032.md` Concrete Artifacts confirmed at lines 193-211 (llm-anthropic 0.26 `thinking_effort` options "low, medium, high, xhigh, or max"). `blog-ghaw-weekly-2026-08-17.md` Claim 5 confirmed at lines 169-181 (Gemini 3.7 Flash added to gh-aw v0.87.0 model inventory). `docs-github-copilot-gemini25pro-gemini3flash-deprecation.md` frontmatter/scope confirmed at lines 1-37 (GitHub Copilot's separate, scheduled-notice Gemini deprecation mechanism). All claim numbers verified by document-order count in each cited note before writing this note's cross-references.
