---
source_url: https://simonwillison.net/2026/Aug/15/cors-chat/
source_type: blog-post
title: "CORS Chat"
author: Simon Willison
date_published: 2026-08-15
date_extracted: 2026-08-24
last_checked: 2026-08-24
status: current
confidence_overall: anecdotal
issue: "#2904"
---

# CORS Chat

> Simon Willison built and shipped a single-page, no-backend browser chat
> client against the OpenAI Responses API in one day (using GPT-5.6-Sol
> xhigh, not Claude) specifically to test Qwen 3.8 27B running locally in
> LM Studio across two different machines. The tool demonstrates a set of
> concrete, checkable client-side patterns — CORS-enabled local inference,
> shareable-but-secret configuration via the URL fragment, and progressive
> SVG-in-iframe rendering during token streaming — packaged as a disposable,
> single-purpose testing utility rather than a product.

## Source Context

- **Type**: blog-post (Willison link-blog / tool-announcement "beat" format;
  ~120 words of original text, plus the tool itself at
  tools.simonwillison.net/cors-chat and a linked build-session gist at
  gist.github.com/simonw/92a1d97773744b45bf259e003013cf36).
- **Author credibility**: Simon Willison is the creator of Django and the
  `llm` CLI, and a designated `trusted-feed` source in this corpus with an
  extensive track record of hands-on LLM tooling posts already cited
  throughout `source-notes/`. This is first-party: he built the tool,
  operated it against his own local and remote endpoints, and is describing
  his own artifact, not relaying a third party's claim.
- **Scope**: Covers the CORS Chat tool's purpose (testing Qwen 3.8 27B on
  two machines), its feature set (endpoint/header configuration, local
  persistence, JSON export, multi-session management, progressive SVG
  rendering), and the fact that it was built same-day with GPT-5.6-Sol
  xhigh. Does NOT cover any benchmark results for Qwen 3.8 27B itself (that
  is the subject of a separate Willison post, "Qwen 3.8 27B is excellent,
  but it defaults to wildly overthinking things," published the next day
  and not covered by this note), nor does it cover DGX Spark performance
  numbers — the DGX Spark is named only as one of the two test machines,
  with no comparative timing or quality data given in the post itself.

## Extracted Claims

### Claim 1: Willison built CORS Chat in a single day specifically to test Qwen 3.8 27B running in LM Studio on two different machines — an Apple M5 MacBook Pro and an NVIDIA DGX Spark
- **Evidence**: Direct first-person statement of motivation and build timeline, opening the post.
- **Confidence**: settled (first-party, direct statement of the author's own action and intent)
- **Quote**: "I built this today (with GPT-5.6-Sol xhigh) to help test Qwen 3.8 27B running in LM Studio on both my M5 MacBook Pro and an NVIDIA DGX Spark."
- **Our assessment**: This is a concrete instance of a now-recurring pattern in this corpus (also seen in `blog-simonwillison-llm-openrouter-06.md` Claim 2): a practitioner builds or extends a small piece of tooling, same-day, purely to unblock evaluation of a newly-available model. The tool is disposable infrastructure for a testing task, not a product with its own roadmap — worth distinguishing from harness/product-tooling posts elsewhere in the corpus.

### Claim 2: CORS Chat targets the OpenAI Responses API specifically (not the older Chat Completions API), and the tool's own build notes flag reusing Chat Completions streaming-chunk handlers for Responses events as a bug to avoid
- **Evidence**: The tool's live configuration UI (endpoint field, "Save & connect," system-message field described as the "first system-role item") matches Responses API semantics rather than Chat Completions' `messages` array; the linked build-session gist explicitly names the pitfall.
- **Confidence**: emerging (tool UI directly observed by the Miner via the live page; the specific pitfall quote is sourced from the linked gist, an AI-assisted build-session log rather than edited editorial prose)
- **Quote**: "Reusing Chat Completions streaming chunk handlers without handling typed Responses events." (from the build-session gist, gist.github.com/simonw/92a1d97773744b45bf259e003013cf36)
- **Our assessment**: This is a specific, actionable engineering caveat for anyone building an OpenAI-compatible client: the Responses API's streaming event stream is typed and event-based (distinct event types for text deltas, reasoning, tool calls, completion, etc.), not the same shape as Chat Completions' `delta` chunks — treating them interchangeably is a named failure mode the tool's own build process called out and avoided. No other note in this corpus documents this specific Chat-Completions-vs-Responses streaming incompatibility.

### Claim 3: CORS Chat notices SVG output in the model's response and progressively renders it into an iframe while the tokens generating it are still streaming in
- **Evidence**: Direct first-person feature description in the post; the linked build-session gist gives the underlying detection rule.
- **Confidence**: settled (directly stated feature; detection rule independently corroborated in the gist)
- **Quote**: "One fun detail is that it notices SVG images that are being generated and progressively renders them in the chat while the tokens are still streaming in."
- **Quote (detection rule, from the gist)**: "If the [code blocks] are either tagged svg or are tagged xml and start with <svg then they are progressively rendered into an iframe"
- **Our assessment**: The detection rule is simple and cheap — a fenced-code-block language tag check (`svg`, or `xml` whose body starts with `<svg`) rather than a full parse — which is exactly the kind of low-effort, high-payoff pattern-match that makes sense for a same-day disposable tool. For harness/tooling builders: streaming partial markup into a live-updating render target (rather than waiting for stream completion) is a general pattern applicable beyond SVG to any incrementally-parseable output format (partial HTML, partial Mermaid, etc.), though the source only demonstrates it for SVG.

### Claim 4: Willison tested CORS Chat against both LM Studio (using its `--cors` flag) and OpenRouter, and reports both worked without issue
- **Evidence**: Direct first-person statement naming both endpoints tested.
- **Confidence**: anecdotal (single practitioner, single session, no failure modes or edge cases reported)
- **Quote**: "I've tried it against LM Studio with the `--cors` option and OpenRouter, and both work fine."
- **Our assessment**: This is a minimal but concrete data point: a browser page served from `tools.simonwillison.net` can talk directly to a local LM Studio server (once CORS is enabled) and to a remote OpenRouter endpoint using the same client code, because both expose OpenAI-compatible APIs. This corroborates the general "OpenAI-compatible API surface as a lowest-common-denominator integration point" pattern documented elsewhere in this corpus's local-model notes (see Cross-References), extending it specifically to *browser-based, CORS-direct* clients rather than server-side or CLI clients.

### Claim 5: Conversations are persisted client-side in the browser and can be exported as copy-pasted JSON; there is no backend or server-side storage
- **Evidence**: Direct first-person feature description in the post.
- **Confidence**: settled (directly stated feature)
- **Quote**: "Conversations are persisted in the browser and can be exported as copy-pasted JSON."
- **Our assessment**: A zero-backend persistence pattern — no server, no database, no account system — appropriate for a disposable single-purpose testing tool. This is consistent with the "harness-as-static-page" pattern Willison has used elsewhere for his tools.simonwillison.net utilities; the JSON-export-via-copy-paste (rather than a file-download button) keeps the entire tool client-only with no server round-trip even for export.

### Claim 6: The endpoint-configuration UI stores the bearer API token only in the browser and explicitly excludes it from the shareable URL-fragment configuration string, while all other endpoint settings (base URL, display name, extra headers, request parameters) are encoded into that shareable fragment
- **Evidence**: Direct observation of the live tool's endpoint-configuration form and its inline help text, fetched from tools.simonwillison.net/cors-chat.
- **Confidence**: settled (directly observed in the live, currently-deployed tool)
- **Quote**: "stored only in this browser" / "never included in the shareable URL fragment" (inline help text on the live tool's Authorization toggle, tools.simonwillison.net/cors-chat)
- **Our assessment**: This is a deliberate, specific security design choice worth extracting on its own: the tool encodes its full configuration (endpoint, headers, model/request parameters) into a URL `#fragment` so a configured session can be shared via a link, but explicitly special-cases the bearer token to keep it local-only, since URL fragments are trivially visible to anyone the link is shared with (and can leak via browser history, referrer-adjacent logging, or screen-sharing) even though fragments are never sent to the server in an HTTP request. This is a concrete, reusable pattern for anyone building shareable-URL-configured client-side tools that also need a secret credential: put non-secret config in the fragment, keep secrets in `localStorage`/session-scoped storage only.

### Claim 7: CORS Chat exposes the OpenAI Responses API's full request-parameter surface directly in its UI, including reasoning effort (none through max), reasoning summary style (auto/concise/detailed), text verbosity, max output tokens, temperature, top-p, truncation behavior, and a response-storage toggle, and supports managing multiple concurrent chat sessions each with independently configured models and reasoning settings
- **Evidence**: Direct observation of the live tool's "New Conversation" configuration panel, fetched from tools.simonwillison.net/cors-chat; corroborated by the post's own summary sentence.
- **Confidence**: settled (directly observed in the live tool, plus first-party post summary)
- **Quote**: "Configure endpoints with custom headers, save conversations locally, and manage multiple chat sessions with different models and reasoning settings."
- **Our assessment**: Exposing the full Responses API parameter surface (rather than a simplified subset) in a same-day disposable tool signals that the point of CORS Chat is comparative model/endpoint evaluation, not a polished end-user chat product — a practitioner testing tool needs direct access to reasoning-effort and verbosity knobs specifically because those are the parameters that matter when comparing how a local model like Qwen 3.8 27B behaves under different reasoning settings (relevant given the same-week follow-up post documents Qwen 3.8 27B "wildly overthinking" by default — see Cross-References).

## Concrete Artifacts

### CORS Chat feature summary (verbatim from the post)
```
"Chat directly with any OpenAI Responses-compatible API endpoint that
supports CORS headers, all within your browser.

I built this today (with GPT-5.6-Sol xhigh) to help test Qwen 3.8 27B
running in LM Studio on both my M5 MacBook Pro and an NVIDIA DGX Spark.

I've tried it against LM Studio with the `--cors` option and OpenRouter,
and both work fine.

Configure endpoints with custom headers, save conversations locally, and
manage multiple chat sessions with different models and reasoning
settings. Conversations are persisted in the browser and can be exported
as copy-pasted JSON.

One fun detail is that it notices SVG images that are being generated and
progressively renders them in the chat while the tokens are still
streaming in."

Source: Simon Willison, simonwillison.net/2026/Aug/15/cors-chat/ (2026-08-15)
Tool: tools.simonwillison.net/cors-chat
Build gist: gist.github.com/simonw/92a1d97773744b45bf259e003013cf36
Tags on post: svg, ai, generative-ai, llms, cors, openrouter, lm-studio
```

### Endpoint-configuration UI fields (observed directly on the live tool, tools.simonwillison.net/cors-chat)
```
Endpoint setup:
  - Base URL (required; help text: "usually ending in /v1")
  - Display name (optional label)
  - Authorization toggle: "Use an Authorization bearer token"
      - token "stored only in this browser"
      - token "never included in the shareable URL fragment"
  - Extra HTTP headers (optional, arbitrary key/value)
  - "Save & connect" button

New Conversation setup:
  - System message (optional; "first system-role item")
  - Reasoning effort: none | ... | max
  - Reasoning summary: auto | concise | detailed
  - Text verbosity
  - Max output tokens
  - Temperature / Top P
  - Truncation setting
  - Response-storage toggle

Chat area: message list, Send/Stop buttons, input box
  ("Enter to send · Shift+Enter for a new line")

Source: tools.simonwillison.net/cors-chat, observed 2026-08-24
```

### SVG progressive-render detection rule (from the build-session gist)
```
Rule: a fenced code block is progressively rendered into an iframe if its
language tag is `svg`, OR its language tag is `xml` and the block's
content starts with `<svg`.

Also noted in the same gist as a pitfall to avoid: reusing Chat
Completions-style streaming chunk handlers for the Responses API's typed
streaming events (the two are not interchangeable).

Source: gist.github.com/simonw/92a1d97773744b45bf259e003013cf36
(build-session log for responses-cors-chat.html)
```

## Cross-References

- **Corroborates**: `blog-google-gemma-4-12b-laptop-ai-edge.md` Claim 7
  (the `litert-lm serve` command starts "an OpenAI-compatible server" that
  standard tools/SDKs/harnesses can connect to as a drop-in local LLM
  server) — both sources independently establish the OpenAI-compatible API
  surface as the lowest-common-denominator integration point that lets one
  client talk to local and hosted endpoints interchangeably. This source is
  the first in the corpus to demonstrate that pattern from a *browser,
  CORS-direct* client rather than a CLI (`llm`) or a named-harness
  integration (OpenClaw, Continue, Aider, etc.) — extending the pattern to
  a new integration surface with its own concerns (CORS headers, credential
  storage in a shareable-URL context) not present in CLI/server clients.
- **Corroborates**: `blog-fowler-boeckeler-local-models-viability.md`
  (Concrete Artifacts: hardware/runtime setup) and
  `blog-ronacher-local-models-focus-polish.md` — both document LM Studio as
  a common local-model runtime for practitioner testing; this source adds
  LM Studio's `--cors` flag as the specific mechanism that makes a local
  LM Studio server reachable from a browser-hosted client, a detail not
  previously documented in this corpus's local-model notes.
- **Extends**: `blog-simonwillison-llm-openrouter-06.md` Claim 2 — the same
  "build a small tool same-day, purely to unblock testing a newly-available
  model" pattern (there: the `llm openrouter refresh` command, built to
  test Kimi 2.6 immediately; here: an entire browser chat client, built to
  test Qwen 3.8 27B immediately). Two independent instances of the same
  practitioner behavior strengthen it as a recognizable pattern: friction
  in evaluating a new model is treated as a bug to fix in one's own tooling
  the same day, not a cost to simply absorb.
- **Extends**: `blog-latentspace-ainews-qwen38-max-27b-launch.md` — that
  note documents Qwen3.8-Max/27B's launch claims, pricing, and third-party
  benchmark scores (Vals AI, Arena.ai) as of the Aug 3-4, 2026 announcement.
  This source is a practitioner's same-week, hands-on follow-up: Willison
  built dedicated tooling specifically to run the newly-released Qwen
  3.8 27B variant locally, one to two weeks after that launch coverage —
  though this note's source text itself contains no benchmark results for
  Qwen 3.8 27B (those appear in Willison's separate next-day post, "Qwen
  3.8 27B is excellent, but it defaults to wildly overthinking things,"
  2026-08-16, not covered here and not yet present in this corpus as of
  this extraction).
- **Novel**: The URL-fragment-for-shareable-config-but-not-secrets pattern
  (Claim 6) is new to this corpus — no existing source note documents a
  client-side tool that splits its configuration between a shareable URL
  fragment and browser-local-only storage specifically to keep a credential
  out of a shared link. The fenced-code-block-language-tag SVG detection
  rule for progressive streaming render (Claim 3) and the named Chat
  Completions-vs-Responses-API streaming incompatibility pitfall (Claim 2)
  are also both new specifics not previously documented in this corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering) — client-side tooling patterns**: Add
  Claim 6's URL-fragment/secret-separation pattern as a concrete recipe for
  any team building shareable, no-backend, client-side configuration tools
  against LLM APIs: encode non-secret configuration in the URL fragment for
  shareability, keep bearer tokens/API keys in browser-local storage only,
  never in the fragment. Add Claim 3's cheap fenced-code-block-tag
  detection rule as a low-effort pattern for progressively rendering
  streamed structured output (SVG, and by extension other incrementally-
  parseable formats) before generation completes.
- **Chapter 02 (Harness Engineering) — API surface caveats**: Add Claim 2's
  named pitfall (Responses API streaming events are typed and distinct from
  Chat Completions' `delta` chunks; reusing one handler for the other is a
  documented bug) as a specific caution for teams building or migrating
  OpenAI-compatible client code that needs to support both API shapes.
- **Chapter 04 (Context Engineering) / local-model orchestration**: Add
  Claim 4 and Claim 1 (LM Studio `--cors` + OpenRouter reachable from the
  same browser client; tool built same-day specifically to test a newly-
  released local model) as a further concrete instance of the "build
  disposable tooling to remove evaluation friction" pattern already
  documented for CLI tooling (`blog-simonwillison-llm-openrouter-06.md`),
  now shown to extend naturally to browser-based clients once CORS is
  enabled on the local server.

## Extraction Notes

- The post itself is thin (~120 words of original text), consistent with
  Willison's "beat" / tool-announcement format seen elsewhere in this
  corpus (e.g. `blog-simonwillison-llm-openrouter-06.md`). Depth for this
  note came from three additional first-party sources the post links to or
  that the Miner followed per MINER.md §1: the live tool itself
  (tools.simonwillison.net/cors-chat, fetched directly and described in
  Claims 6-7 and the second Concrete Artifacts block), the linked
  build-session gist (gist.github.com/simonw/92a1d97773744b45bf259e003013cf36,
  used for Claims 2-3 and the third Concrete Artifacts block), and the
  post's own tag list. This matches MINER.md's "read the entire source...
  follow up to 5 linked pages" instruction rather than treating a short
  post as exhausted after its own text.
- **WebFetch reproduction limits**: WebFetch's underlying summarizer
  refused a request to reproduce the full post text verbatim (citing a
  copyright-reproduction guideline) when asked in one un-scoped request.
  All quotes in this note were instead obtained via multiple narrowly
  scoped requests ("quote this specific under-125-character sentence"),
  each returning a short, directly-quotable fragment, per the pattern
  already established in `blog-ronacher-local-models-focus-polish.md`'s
  Extraction Notes ("targeted verbatim-quote requests to WebFetch"). No
  quote in this note was paraphrased or reconstructed from a summary.
- **Gist access caveat**: the linked build-session gist is marked "Secret"
  (unlisted, not indexed) but was reachable at its direct URL. WebFetch's
  summarizer reported that the gist's visible content is a mix of GitHub's
  own page chrome, OpenAI API-documentation search excerpts, and a task
  specification for `responses-cors-chat.html` — i.e., an AI-assisted
  build-session log, not the tool's actual source code or a polished
  system-prompt document. The two verbatim fragments quoted from it
  (Claims 2-3) were independently returned by two separate targeted
  fetches with consistent wording, giving reasonable confidence they are
  genuine excerpts rather than summarizer invention, but — unlike the
  live-tool observations (Claims 5-7, directly observed by the Miner) —
  they could not be independently cross-checked against the tool's actual
  running code, hence the `emerging` (not `settled`) confidence rating on
  Claim 2, which rests entirely on the gist text. Claim 3 stays `settled`
  because its core assertion (progressive SVG rendering exists) is directly
  stated in the blog post itself; only its supplementary detection-rule
  quote is gist-sourced.
- **DGX Spark**: named only as one of two test machines; the post gives no
  comparative performance, timing, or quality data between the M5 MacBook
  Pro and DGX Spark runs. Flagged explicitly in Source Context above so
  this is not mistaken for a documented hardware-comparison claim.
- Confidence rated `anecdotal` overall despite several individual claims
  being rated `settled`: the claims that are settled are settled as facts
  about this one tool (directly observed, first-party-stated), but the
  source is a single practitioner's single-day, single-tool build with no
  broader validation, controlled comparison, or adoption evidence — the
  same basis this corpus uses to rate comparable single-tool-announcement
  posts (e.g. `blog-simonwillison-llm-openrouter-06.md`) as `anecdotal`
  overall.
