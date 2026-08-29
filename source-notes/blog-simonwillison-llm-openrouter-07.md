---
source_url: https://simonwillison.net/2026/Aug/21/llm-openrouter/
source_type: blog-post
title: "llm-openrouter 0.7"
author: Simon Willison
date_published: 2026-08-21
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: settled
issue: "#3048"
---

# llm-openrouter 0.7

> A first-party release announcement for llm-openrouter 0.7, which brings the plugin up to LLM 0.32 compatibility (enabling reasoning-trace display), switches OpenRouter model access to OpenRouter's own Responses API by default, and adds three provider-executed server-side tools — Shell, WebFetch, and WebSearch — accessible through LLM's `-T` interface.

## Source Context

- **Type**: blog-post (Willison "beat" format — a short link-blog post pairing brief commentary with a linked GitHub release page; same minimal format documented for the predecessor release in `blog-simonwillison-llm-openrouter-06.md`). The beat post itself is ~35 words of prose plus a three-bullet blockquote; the plugin's GitHub README (fetched at the `0.7` tag) carries the substantive per-tool documentation and was followed as a linked page per MINER.md §1.
- **Author credibility**: Simon Willison is the creator and maintainer of both the `llm` CLI/library and the `llm-openrouter` plugin itself. This is first-party release documentation from the person who wrote the code.
- **Scope**: Covers the llm-openrouter 0.7 release only — LLM 0.32 compatibility, the switch to OpenRouter's Responses API, and the three new server-side tools (Shell, WebFetch, WebSearch), plus the pre-existing usage surface documented in the README (model listing, images, schemas, tool calling, reasoning options, provider routing) which did not change in this release. Does NOT cover OpenRouter's own Responses API implementation in depth (a separate OpenRouter docs page is linked but is a JS-rendered SPA that yielded no substantive prose on fetch — see Extraction Notes), OpenRouter's pricing for the new server-side tools, or the llm-mistral/llm-gemini plugins' parallel 0.32-compatibility work (covered in `blog-simonwillison-llm-gemini-033.md`).

## Extracted Claims

### Claim 1: llm-openrouter 0.7 is now compatible with LLM 0.32, which enables the plugin to display reasoning traces for OpenRouter-hosted models
- **Evidence**: Opening sentence of the blog post, corroborated by the GitHub release notes' first bullet.
- **Confidence**: settled (first-party release documentation; the underlying reasoning-trace-to-stderr mechanism this depends on is documented as an LLM-core-library feature in `blog-simonwillison-llm032.md` Claim 2)
- **Quote**: "Now that this plugin is compatible with LLM 0.32 it can display the reasoning traces for LLMs available through OpenRouter."
- **Our assessment**: This is a straightforward compatibility claim, not a new mechanism — the reasoning-trace-to-stderr display behavior itself was already shipped in LLM 0.32 core (`blog-simonwillison-llm032.md` Claim 2); this release is the OpenRouter-specific plugin work needed to participate in that behavior. Believable and low-risk to accept as stated, since it is a direct, verifiable compatibility statement about the plugin's own code.

### Claim 2: OpenRouter models accessed through the plugin now use OpenRouter's own implementation of the Responses API by default, with an explicit option to fall back to the older Chat Completions API per-prompt
- **Evidence**: Blog post bullet plus the README's Usage section, which states the default and gives the exact override flag.
- **Confidence**: settled (first-party; documented default behavior plus a concrete escape-hatch flag)
- **Quote**: "Models use OpenRouter's Responses API by default. You can temporarily use the older Chat Completions API for a prompt with `-o chat_completions 1`."
- **Our assessment**: This is a default-behavior change with real migration implications: any workflow or script depending on Chat-Completions-API-specific response shapes now needs `-o chat_completions 1` per prompt to preserve old behavior, since the default silently switched. The presence of an explicit opt-out flag (rather than a breaking change with no escape hatch) is a reasonable backwards-compatibility accommodation, consistent with the "existing plugins should all continue to work" compatibility posture LLM 0.32 itself stated (`blog-simonwillison-llm032.md` Claim 13).

### Claim 3: The release adds three new provider-executed server-side tools — Shell, WebFetch, and WebSearch — enabled through LLM's `-T` flag interface
- **Evidence**: Direct statement in both the blog post blockquote and the GitHub release notes (identical text in both).
- **Confidence**: settled (first-party; each tool individually documented with a runnable example in the README, see Claims 4–6)
- **Quote**: "Three new server-side tools: Shell, WebFetch, and WebSearch. Enable these with options like `-T WebSearch`."
- **Our assessment**: This extends the same `-T`-flag server-side-tool convention already documented for OpenAI (`-T CodeInterpreter`), Anthropic (`-T WebSearch`, `-T WebFetch`, `-T CodeExecution`, `-T AnthropicMCP`, per `blog-simonwillison-llm032.md` Claims 4–5), and Gemini (`-T GoogleSearch`, `-T URLContext`, `-T CodeExecution`, per `blog-simonwillison-llm-gemini-033.md` Claim 3) to OpenRouter, making it the fourth model-provider plugin in this corpus to expose provider-executed tools through LLM's unified interface. Notably, OpenRouter's WebFetch and WebSearch tool *names* now match Anthropic's exactly, while its Shell tool is functionally distinct from anything documented for the other three providers (none of which expose a general-purpose remote shell).

### Claim 4: The new Shell tool runs arbitrary commands in an isolated container hosted by OpenRouter rather than on the user's local machine, configurable via `engine`, `environment`, and `sleep_after_seconds` options
- **Evidence**: README "Shell" section, with a runnable CLI example and an explicit statement that execution happens remotely, not locally.
- **Confidence**: settled (first-party plugin documentation with a concrete, copy-pasteable example)
- **Quote**: "Commands run in an isolated container hosted by OpenRouter, not on your local machine."
- **Our assessment**: This is the first server-side tool in this corpus that grants a model general command execution rather than a narrowly scoped capability (web search, web fetch, code interpretation in a sandboxed notebook-like environment). The isolation boundary is opaque to the caller — practitioners are trusting OpenRouter's hosted container isolation rather than a self-managed sandbox. This is architecturally different from the hardware-isolated VM approach evaluated in `blog-simonwillison-smolmachines-untrusted-sandbox.md` (Claims 1–2), which tests and documents the isolation properties (KVM-backed VMs, resource limits, fork-bomb containment) of a self-hosted sandbox in detail; OpenRouter's Shell tool offers no equivalent documented isolation guarantees in this source — practitioners must trust OpenRouter's infrastructure without independent verification of its containment properties.

### Claim 5: The new WebFetch tool retrieves and extracts the contents of a specific URL as a provider-side tool, configurable via `engine`, `max_uses`, `max_content_tokens`, `allowed_domains`, and `blocked_domains` options
- **Evidence**: README "Web fetch" section, with a runnable CLI example.
- **Confidence**: settled (first-party plugin documentation, concrete example and option list)
- **Quote**: "`WebFetch` accepts `engine`, `max_uses`, `max_content_tokens`, `allowed_domains` and `blocked_domains` options."
- **Our assessment**: The domain-allowlist/blocklist options are a concrete, checkable safety control for practitioners worried about a model fetching arbitrary or malicious URLs — worth citing directly if the guide discusses constraining agentic web-fetch tools. `max_content_tokens` is also a useful cost/context control absent from some other providers' documented WebFetch equivalents in this corpus.

### Claim 6: The new WebSearch tool lets supported OpenRouter models decide autonomously when to search the web, configurable via `max_results`, `engine`, `max_uses`, `max_total_results`, `search_context_size`, `max_characters`, `user_location`, `allowed_domains`, and `excluded_domains` options
- **Evidence**: README "Web search" section, with a runnable CLI example (`-T 'WebSearch(max_results=3)'`).
- **Confidence**: settled (first-party plugin documentation, concrete example and full option list)
- **Quote**: "The model decides when and whether to search."
- **Our assessment**: The autonomous-decision framing ("the model decides") matters for cost predictability — a practitioner cannot assume a WebSearch-enabled prompt will or won't trigger a paid search call; `max_uses`/`max_total_results` are the available levers to bound worst-case cost, not a way to force or suppress search on a specific call.

### Claim 7: Server-side tool response items (from Shell, WebFetch, WebSearch, or any other OpenRouter Responses API tool) persist across continued conversations invoked with `llm -c`, allowing a single tool chain to mix hosted server-side tools with local LLM-defined tools without losing prior context
- **Evidence**: Direct statement in the README, positioned as the closing note after all three tool sections.
- **Confidence**: settled (first-party plugin documentation)
- **Quote**: "Server-tool response items are preserved in subsequent Responses API requests, including conversations continued using `llm -c`, so tool chains can combine hosted server tools with local LLM tools without losing prior context."
- **Our assessment**: This is the practical payoff of switching to the Responses API by default (Claim 2) — the Responses API's request/response shape is what allows OpenRouter to preserve server-tool state across turns without the caller re-supplying it. For harness engineers, this means an OpenRouter-routed agent loop can freely interleave a locally defined Python function tool with, say, a hosted WebFetch call in the same multi-turn conversation, and continuing with `-c` will not silently drop the WebFetch result from context on the next turn.

### Claim 8: llm-openrouter 0.7 (August 21, 2026) is the plugin's fulfillment of the LLM-0.32-compatibility gap explicitly flagged as outstanding for llm-openrouter as of LLM 0.32's stable release seventeen days earlier (August 4, 2026)
- **Evidence**: Date arithmetic between this release (2026-08-21, confirmed via GitHub API `published_at`) and the LLM 0.32 stable release date (2026-08-04, per this note's frontmatter cross-check against `blog-simonwillison-llm032.md`).
- **Confidence**: settled (dates independently verifiable via each release's own GitHub API record; the "not yet compatible" status being closed by this release is a direct reading of Claim 1 against the prior gap)
- **Quote**: (no direct quote in this source stating the prior gap; see Our assessment for the cited cross-reference)
- **Our assessment**: `blog-simonwillison-llm032.md` Claim 13's Our assessment records that as of LLM 0.32's stable release, the post "states `llm-gemini`, `llm-openrouter`, and `llm-mistral` are "nearly there, releases coming soon"" for full streaming-events participation — this release is that forecast's fulfillment for llm-openrouter specifically, arriving 17 days later. `blog-simonwillison-llm-gemini-033.md` Claim 2 documents the equivalent fulfillment for llm-gemini, arriving 9 days after LLM 0.32 (August 13, 2026) — meaning llm-openrouter was the slower of the two plugins to catch up, and (per Claim 13 of the same note) llm-mistral's equivalent release is not covered by any note currently in this corpus.

## Concrete Artifacts

### GitHub release notes (verbatim, github.com/simonw/llm-openrouter, tag 0.7, published 2026-08-21T16:58:19Z)
```
- Updated for compatibility with [LLM 0.32](https://llm.datasette.io/en/stable/changelog.html#v0-32).
- Models now use OpenRouter's implementation of the [Responses API](https://openrouter.ai/docs/api_reference/responses/overview).
- Three new server-side tools: [Shell](https://github.com/simonw/llm-openrouter#shell), [WebFetch](https://github.com/simonw/llm-openrouter#web-fetch), and [WebSearch](https://github.com/simonw/llm-openrouter#web-search). Enable these with options like `-T WebSearch`.
```
*Source: GitHub API, github.com/simonw/llm-openrouter/releases/tags/0.7*

### README: Shell server-side tool (verbatim, github.com/simonw/llm-openrouter at tag 0.7)
```bash
llm -m openrouter/openai/gpt-5.2 \
  -T 'Shell(engine="openrouter")' \
  'Run: printf "llm-openrouter-shell-ok\n"'
```
`Shell` accepts `engine`, `environment` and `sleep_after_seconds` options. Commands run in an isolated container hosted by OpenRouter, not on your local machine.
*Source: raw.githubusercontent.com/simonw/llm-openrouter/0.7/README.md*

### README: Web fetch server-side tool (verbatim)
```bash
llm -m openrouter/openai/gpt-5.2 \
  -T 'WebFetch(max_uses=1)' \
  'Fetch https://example.com and report its heading'
```
`WebFetch` accepts `engine`, `max_uses`, `max_content_tokens`, `allowed_domains` and `blocked_domains` options.
*Source: raw.githubusercontent.com/simonw/llm-openrouter/0.7/README.md*

### README: Web search server-side tool (verbatim)
```bash
llm -m openrouter/openai/gpt-5.2 \
  -T 'WebSearch(max_results=3)' \
  'key events on march 1st 2025'
```
The `WebSearch` tool also accepts OpenRouter's `engine`, `max_uses`, `max_total_results`, `search_context_size`, `max_characters`, `user_location`, `allowed_domains` and `excluded_domains` options. The model decides when and whether to search.
*Source: raw.githubusercontent.com/simonw/llm-openrouter/0.7/README.md*

### README: Responses API default and fallback (verbatim)
```
Models use OpenRouter's Responses API by default. You can temporarily use the
older Chat Completions API for a prompt with `-o chat_completions 1`.
```
*Source: raw.githubusercontent.com/simonw/llm-openrouter/0.7/README.md*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-llm-openrouter-06.md` Claim 5: That note characterized llm-openrouter's version history (0.1–0.6) as tracking the base `llm` library's capability surface closely, adding the corresponding OpenRouter-facing feature within one to two releases of the core library. This release continues that exact pattern — LLM 0.32 shipped server-side tools and typed streaming events for reasoning traces (`blog-simonwillison-llm032.md` Claims 2, 4–5), and llm-openrouter 0.7 is the OpenRouter-facing arrival of both capabilities.
  - `blog-simonwillison-llm-gemini-033.md` Claim 3: That note documented llm-gemini 0.33 exposing Google Search, URL context, and code execution as server-side tools via the same `-T` flag convention, as the third provider plugin (after OpenAI and Anthropic) to do so. This source is the fourth, extending the same convention to OpenRouter's model roster.

- **Contradicts**: None identified.

- **Extends**:
  - `blog-simonwillison-llm032.md` Claim 13: That note recorded llm-openrouter as one of three plugins ("nearly there, releases coming soon," per that note's Our assessment) not yet updated for full LLM 0.32 streaming-events compatibility as of the August 4, 2026 stable release. This source is the actual release closing that gap for llm-openrouter, 17 days later (Claim 8).
  - `blog-simonwillison-llm032.md` Claims 4–5: Those claims documented server-side tools for OpenAI (`-T CodeInterpreter`) and Anthropic (`-T WebSearch`, `-T WebFetch`, `-T CodeExecution`, `-T AnthropicMCP`). This source (Claim 3) extends the identically-named `-T WebSearch`/`-T WebFetch` pattern to OpenRouter, and adds a `-T Shell` tool with no direct equivalent documented for OpenAI or Anthropic in this corpus.
  - `blog-simonwillison-llm-openrouter-06.md`: The direct predecessor release (0.6, April 20, 2026 — the `llm openrouter refresh` command). This note documents the next release in the same plugin's version history, roughly four months later.

- **Novel**:
  - First in-corpus documentation of a general-purpose remote **Shell** server-side tool exposed through LLM's `-T` interface — distinct from the narrowly scoped code-execution/interpreter tools documented for OpenAI (`CodeInterpreter`) and Anthropic (`CodeExecution`), and with no equivalent in the smolvm-based self-hosted sandbox research documented in `blog-simonwillison-smolmachines-untrusted-sandbox.md` (that source hardens and measures a *local* VM sandbox; OpenRouter's Shell tool delegates isolation entirely to OpenRouter's own infrastructure with no documented isolation guarantees in this source).
  - First in-corpus documentation of OpenRouter switching a model-provider plugin to the Responses API as the *default* request format, with an explicit per-prompt opt-out to the legacy Chat Completions API.
  - First in-corpus documentation of the specific claim that server-tool response state survives `llm -c` conversation continuation for a given provider (OpenRouter) — a data-continuity detail not stated this explicitly for OpenAI or Anthropic's server-side tools elsewhere in this corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering — server-side tool patterns)**: Add OpenRouter's `-T Shell`, `-T WebFetch`, `-T WebSearch` as the fourth documented provider-side server tool surface (after OpenAI, Anthropic, Gemini). Specifically flag the Shell tool as qualitatively different from the others — general command execution in an opaque, provider-hosted sandbox — and note that this source provides no isolation guarantees a practitioner can independently verify, unlike the self-hosted smolvm sandbox evaluated in `blog-simonwillison-smolmachines-untrusted-sandbox.md`. Cite Claims 3–4.
- **Chapter 01 (Daily Workflows — `llm` CLI Tooling)**: If the guide documents OpenRouter model access via `llm -m openrouter/...`, note the default switch to the Responses API and the `-o chat_completions 1` fallback flag as a breaking-default change practitioners should check before relying on legacy Chat-Completions-shaped responses. Cite Claim 2.
- **Chapter 04/05 (Agentic Loops / Orchestration)**: Add the WebFetch domain allowlist/blocklist and WebSearch usage caps (`max_uses`, `max_total_results`) as concrete, checkable cost- and safety-control knobs for agentic loops that give a model autonomous web access. Cite Claims 5–6.
- **Chapter 05 (Orchestration & Integration)**: Note that OpenRouter's server-tool state persists across `llm -c` continuations, allowing hosted and local tools to be combined in one multi-turn tool chain without manually re-supplying prior tool results — a concrete detail worth citing if the guide discusses multi-turn tool-loop context management. Cite Claim 7.

## Extraction Notes

- **Fetched three sources directly**: the blog post's raw HTML (via `curl`, all quotes verified character-for-character against the raw markup, including the blockquote bullet list), the GitHub release notes (via the GitHub REST API, raw markdown body), and the plugin's README at the `0.7` git tag (via `raw.githubusercontent.com`, which is where the Shell/WebFetch/WebSearch tool documentation and the Responses-API-default note actually live — the blog post and release notes only summarize these in one line each).
- **One linked page yielded no usable content**: `openrouter.ai/docs/api_reference/responses/overview` (linked from both the blog post and the GitHub release notes) is a JavaScript-rendered documentation site; a direct `curl` fetch returned only navigation chrome and CSS, no article prose. This source note does not quote or make claims from that page's body text as a result — OpenRouter's own Responses API semantics are out of scope for this note beyond what llm-openrouter's own README states about defaulting to it.
- **No sub-pages followed for OpenRouter's own per-tool docs pages** (`openrouter.ai/docs/guides/features/server-tools/{shell,web-fetch,web-search}`, linked from the README): these are OpenRouter's own tool documentation rather than llm-openrouter plugin documentation; the README's own descriptions and option lists were treated as sufficient for a plugin-focused source note, consistent with the issue's scope (llm-openrouter, not OpenRouter's platform docs).
- **No contradictions found requiring MINER.md §4a filing.**
- **Cross-reference verification performed**: `blog-simonwillison-llm-openrouter-06.md` Claim 5 confirmed at lines 50–54 (version-history-tracks-core-library-capability characterization). `blog-simonwillison-llm-gemini-033.md` Claim 3 confirmed at lines 38–42 (`-T GoogleSearch`/`-T URLContext`/`-T CodeExecution`, third-provider framing) and Claim 2 confirmed at lines 32–36 (9-day gap after LLM 0.32, and Claim 13 of `blog-simonwillison-llm032.md` cited therein). `blog-simonwillison-llm032.md` Claim 13 confirmed at lines 98–102 (the "nearly there, releases coming soon" phrasing, and the explicit statement that plugins providing extra models need upgrading to participate fully in streaming events) and Claims 4–5 confirmed at lines 44–54 (`-T CodeInterpreter`, `-T WebSearch`/`-T WebFetch`/`-T CodeExecution`/`-T AnthropicMCP`). `blog-simonwillison-smolmachines-untrusted-sandbox.md` Claims 1–2 confirmed at lines 61–91 (smolvm's tested hardware-isolation security controls, used here only as a documented contrast to OpenRouter's opaque hosted Shell sandbox, not as a corroborating or contradicting claim about the same tool). All claim numbers verified by document-order count in each cited note before writing this note's cross-references.
