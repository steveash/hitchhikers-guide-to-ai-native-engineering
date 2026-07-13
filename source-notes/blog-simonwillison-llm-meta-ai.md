---
source_url: https://simonwillison.net/2026/Jul/9/llm-meta-ai/
source_type: blog-post
title: "Release: llm-meta-ai 0.1"
author: Simon Willison
date_published: 2026-07-09
date_extracted: 2026-07-13
last_checked: 2026-07-13
status: current
confidence_overall: anecdotal
issue: "#1813"
---

# Release: llm-meta-ai 0.1

> A minimal release announcement for a new `llm` CLI plugin giving CLI access to
> Meta's muse-spark-1.1 model — notable not for its prose (a two-sentence post)
> but for the plugin's README, which shows the `llm` ecosystem's vendor-plugin
> template (auth via `llm keys set` / env var, model-list caching + `refresh`,
> `-o` option flags, tool/schema/image-attachment support) has now been applied
> to a fourth vendor (after OpenRouter, Gemini, and OpenAI-via-Codex already in
> the corpus), reinforcing it as a stable, repeatable plugin architecture rather
> than a one-off convention.

## Source Context

- **Type**: blog-post (Willison "beat" format — a minimal link-blog post, roughly
  two sentences of original text, linking out to a GitHub release page and Meta's
  own model-API announcement). To get past the thinness of the blog post itself,
  this note also extracts the plugin's GitHub release notes and README (linked
  directly from the post) and Meta's muse-spark-1.1 API announcement (linked from
  the post as the model reference), per the Miner's instruction to follow
  substantive linked pages.
- **Author credibility**: Simon Willison is the creator of the `llm` CLI and the
  author of this plugin (`llm-meta-ai`) himself. This is first-party release
  documentation — the plugin name, model slug, and CLI flags are authoritative
  because he wrote the code. He has no independent hands-on usage report in this
  post (no pelican benchmark, no session transcript) — this is a bare release
  announcement, thinner even than his usual "beat" posts.
- **Scope**: Covers the existence and initial feature set of `llm-meta-ai` 0.1
  (auth, model listing, basic invocation, options, tool/schema/image support) as
  documented in the plugin's own README and release notes. Does NOT cover any
  hands-on evaluation of muse-spark-1.1's output quality, pricing, comparative
  benchmarks, or Meta's API pricing/rate-limit specifics (Meta's own announcement
  omits pricing, endpoint URLs, and rate limits entirely).

## Extracted Claims

### Claim 1: `llm-meta-ai` 0.1 is the initial release of an `llm` CLI plugin adding support for Meta's muse-spark-1.1 model
- **Evidence**: Verbatim release note text from the GitHub release page
  (https://github.com/simonw/llm-meta-ai/releases/tag/0.1), corroborated by the
  blog post itself.
- **Confidence**: settled (first-party release documentation from the plugin's
  author; this is the plugin's first version, so there is no prior-version
  comparison to verify against)
- **Quote**: "Initial release. Support for the new muse-spark-1.1 model"
- **Our assessment**: This is a straightforward new-plugin release. The
  significance is not the prose but that it gives `llm` CLI users a fourth
  vendor-specific access path (alongside llm-gemini, llm-openrouter, and native
  OpenAI support), extending the "every major model vendor gets an `llm` plugin
  within days of API availability" pattern to Meta.

### Claim 2: The plugin requires a Meta AI API key, settable via `llm keys set meta-ai` or the `META_AI_TOKEN` environment variable
- **Evidence**: Plugin README (fetched from https://github.com/simonw/llm-meta-ai),
  which documents both the interactive key-registration command and the
  environment-variable alternative.
- **Confidence**: settled (first-party plugin documentation)
- **Quote**: (no direct quote confirmed verbatim from the README fetch; see
  Extraction Notes — the README content was returned as a structured paraphrase,
  not word-for-word text)
- **Our assessment**: This dual-auth pattern (`llm keys set <name>` interactive
  prompt, or `<VENDOR>_TOKEN`/`<VENDOR>_API_KEY` environment variable) is the
  same convention used across other `llm` vendor plugins. It is not novel to this
  plugin, but it confirms the convention holds for a fourth vendor, which matters
  for a guide section that wants to state the convention as a stable rule rather
  than an OpenRouter/Gemini-specific quirk.

### Claim 3: Models are addressed with a `meta-ai/` prefix (e.g. `meta-ai/muse-spark-1.1`), and the plugin exposes a `llm meta-ai models` subcommand plus an hourly-cached, manually-refreshable model list
- **Evidence**: Plugin README documents the naming convention, the
  `llm meta-ai models` / `llm models` commands, the `--json` flag, and the
  `llm meta-ai refresh` command with a stated default cache lifetime of one hour.
- **Confidence**: settled (first-party plugin documentation)
- **Quote**: (no direct quote confirmed verbatim; paraphrase per Extraction Notes)
- **Our assessment**: This is the third in-corpus instance of the cached-model-list
  + explicit-refresh pattern: `blog-simonwillison-llm-openrouter-06.md` Claim 1
  documents `llm openrouter refresh` (added in 0.6, April 2026) solving the exact
  same "new model isn't showing up yet" problem. `llm-meta-ai` ships this pattern
  from its very first release (0.1) rather than adding it later, suggesting the
  refresh-command convention has become a from-day-one expectation for new `llm`
  vendor plugins rather than a lesson learned after the fact.

### Claim 4: The plugin supports the standard `llm` option surface — `-o reasoning_effort <level>` and `-o max_tokens <n>` — for muse-spark-1.1, and reasoning tokens are billed out of the same output-token budget as regular output
- **Evidence**: README usage examples show
  `llm -m meta-ai/muse-spark-1.1 'Query' -o reasoning_effort low` and
  `llm -m meta-ai/muse-spark-1.1 'A short poem' -o max_tokens 2000`; the README's
  limitations section states reasoning tokens consume the output token budget.
- **Confidence**: settled (first-party plugin documentation)
- **Quote**: (no direct quote confirmed verbatim; paraphrase per Extraction Notes)
- **Our assessment**: The `-o reasoning_effort` flag matches the same option name
  used for OpenAI/GPT-5 reasoning control documented in
  `blog-simonwillison-llm-openrouter-06.md` Claim 5 ("`-o reasoning_effort medium`"
  for GPT-5 via llm-openrouter) and `blog-simonwillison-llm031.md`. This is a
  fourth confirmation that `-o reasoning_effort` has become a de facto standard
  option name across `llm` plugins for reasoning models, regardless of vendor —
  useful for a guide that wants to state CLI conventions independent of any one
  vendor's plugin.

### Claim 5: The plugin supports image attachments (PNG, JPEG, WebP, GIF, ICO, PDF) but not yet the MP4 video input that Meta's underlying API supports
- **Evidence**: README usage example
  `llm -m meta-ai/muse-spark-1.1 'Describe this' -a [image_url]` with the listed
  format set; the README's limitations section explicitly notes MP4 video exists
  in the API but is not yet implemented in the plugin.
- **Confidence**: settled (first-party plugin documentation, explicitly
  acknowledging a known gap)
- **Quote**: (no direct quote confirmed verbatim; paraphrase per Extraction Notes)
- **Our assessment**: This is a useful, concrete data point about lag between a
  vendor's underlying API capability and a community/first-party CLI plugin's
  coverage of that capability. It corroborates Meta's own announcement (see Claim
  8 below), which states the underlying model handles "full image and video
  processing" — the plugin currently only surfaces the image half of that. For
  practitioners: if you need video input to muse-spark-1.1, the `llm-meta-ai`
  plugin's 0.1 release will not get you there; you'd need to call Meta's API
  directly.

### Claim 6: The plugin supports `llm`'s tool-calling flag (`-T`) and structured-output schema flag (`--schema`) for muse-spark-1.1
- **Evidence**: README usage examples
  `llm -m meta-ai/muse-spark-1.1 -T llm_time 'What time is it?' --td` and
  `llm -m meta-ai/muse-spark-1.1 'Invent a dog' --schema 'name, age int, breed'`.
- **Confidence**: settled (first-party plugin documentation)
- **Quote**: (no direct quote confirmed verbatim; paraphrase per Extraction Notes)
- **Our assessment**: Both flags exactly match the general `llm` tool/schema
  conventions documented elsewhere in the corpus (`-T` for tool registration in
  `blog-simonwillison-llm-shebang.md` Claim 5; `--schema` and `--td` also appear
  there). This is another confirmation that a new vendor plugin, from its very
  first release, inherits the full `llm` library feature surface (tools, schemas,
  debug flags) rather than needing to reimplement it — the vendor plugin's job is
  narrowed to translating requests/responses to and from the vendor's API, not
  reimplementing the CLI's option system.

### Claim 7: Meta AI API rate limits are applied per model, independently
- **Evidence**: README limitations section states rate limits apply per model.
- **Confidence**: settled (first-party plugin documentation, though it reflects
  Meta's API behavior rather than something the plugin itself controls)
- **Quote**: (no direct quote confirmed verbatim; paraphrase per Extraction Notes)
- **Our assessment**: A minor but practically relevant operational detail — a
  practitioner calling multiple muse-spark model variants through this plugin
  should not assume a shared rate-limit budget across models. Thin signal on its
  own; included for completeness since it's an explicit README callout.

### Claim 8: Meta's own announcement describes muse-spark-1.1 as "a multimodal reasoning model built for agentic tasks," with a 1M-token context window, zero-shot tool/MCP/custom-skill use, and multi-agent orchestration (planning and delegating across parallel subagents)
- **Evidence**: Meta's own blog post
  (https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/), announcing
  the model alongside a new public-preview Meta Model API for developers.
- **Confidence**: anecdotal (vendor's own marketing description of capabilities;
  no independent verification of the "zero-shot generalization to new native
  tools, MCP servers, and custom skills" claim or the multi-agent orchestration
  claim in this note)
- **Quote**: (no direct quote confirmed verbatim; see Extraction Notes — the
  Meta blog content was returned as a structured paraphrase by WebFetch, not
  word-for-word text)
- **Our assessment**: Two elements are notable for harness engineering even
  though unverified: (1) Meta explicitly frames the model around MCP server and
  "custom skill" tool use, which is now the third vendor in the corpus (after
  Anthropic's Claude and the meta.ai chat product documented in
  `blog-simonwillison-muse-spark.md`) to ship MCP-aware or tool-native model
  behavior as a headline capability rather than an add-on. (2) The
  "plan and delegate across parallel subagents" framing is consistent with
  `blog-simonwillison-muse-spark.md` Claim 3, which documents `subagents.spawn_agent`
  as a first-class tool in the meta.ai chat harness — this announcement suggests
  the underlying muse-spark model family (not just the meta.ai product harness)
  has multi-agent delegation built into its training/capabilities, not merely
  bolted on as an external tool in one chat product's harness.

## Concrete Artifacts

### `llm-meta-ai` 0.1 release notes (GitHub, paraphrased from WebFetch — see Extraction Notes)

```
Release: 0.1
Commit: 3b7372c16dc55b7ca6435577d45f74ea59a644a2
Date: July 9, 2026 (16:12)

"Initial release. Support for the new muse-spark-1.1 model"

Usage:
  llm -m meta-ai/muse-spark-1.1 "What is the capital of France?"

Source: github.com/simonw/llm-meta-ai/releases/tag/0.1
```

### `llm-meta-ai` README usage examples (paraphrased from WebFetch — see Extraction Notes)

```bash
# Install
llm install llm-meta-ai

# Auth (either path)
llm keys set meta-ai
# or
export META_AI_TOKEN=...

# List models
llm models                    # all models, including meta-ai/*
llm meta-ai models             # meta-ai models only
llm meta-ai models --json      # full JSON model definitions
llm meta-ai refresh             # force-refresh the cached model list (default: hourly cache)

# Basic query
llm -m meta-ai/muse-spark-1.1 "What is the capital of France?"

# Reasoning effort control
llm -m meta-ai/muse-spark-1.1 'Query' -o reasoning_effort low

# Token limit
llm -m meta-ai/muse-spark-1.1 'A short poem' -o max_tokens 2000

# Image attachment (PNG, JPEG, WebP, GIF, ICO, PDF — no MP4/video yet)
llm -m meta-ai/muse-spark-1.1 'Describe this' -a [image_url]

# Tool calling with debug output
llm -m meta-ai/muse-spark-1.1 -T llm_time 'What time is it?' --td

# Structured output via schema
llm -m meta-ai/muse-spark-1.1 'Invent a dog' --schema 'name, age int, breed'
```

*Source: github.com/simonw/llm-meta-ai README, fetched via WebFetch 2026-07-13.*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-llm-openrouter-06.md` Claim 1 (`llm openrouter refresh`
    solving stale model-cache lists): `llm-meta-ai` ships the equivalent
    `llm meta-ai refresh` command from its very first release, confirming the
    cached-list + refresh pattern is now a standard part of the `llm` vendor-plugin
    template rather than a feature OpenRouter alone needed to add later.
  - `blog-simonwillison-llm-openrouter-06.md` Claim 5 and `blog-simonwillison-llm-shebang.md`
    Claims 5 and 8 (`-o reasoning_effort`, `-T`, `--td` as standard `llm` CLI
    option/flag names): `llm-meta-ai`'s identical use of `-o reasoning_effort`,
    `-T`, and `--td` is a fourth confirmation that these are fixed, vendor-agnostic
    conventions in the `llm` ecosystem, not per-plugin choices.
  - `blog-simonwillison-muse-spark.md` Claim 3 (`subagents.spawn_agent` as a
    first-class tool in the meta.ai chat harness): Meta's muse-spark-1.1
    announcement's "plan and delegate across parallel subagents" framing is
    consistent with the same product family already documenting multi-agent
    delegation as a core capability.

- **Contradicts**: None identified. No existing source note makes a claim that
  conflicts with this source.

- **Extends**:
  - `blog-simonwillison-muse-spark.md`: That note (issue #169, April 2026)
    documents Willison's hands-on exploration of muse-spark via the meta.ai chat
    product's 16-tool harness. This note documents a different, later access
    path (July 2026) — direct API access to a newer model version (muse-spark-1.1
    vs. the original muse-spark) via the `llm` CLI, rather than the chat product.
    Together they show two different integration surfaces Meta now offers for the
    same model family: a consumer chat harness (meta.ai, 16 tools) and a raw
    developer API (Meta Model API, now `llm`-CLI-accessible).
  - `blog-simonwillison-llm-openrouter-06.md` and `blog-simonwillison-llm-gemini-032.md`:
    Both document the same `llm` vendor-plugin template (install, auth, model
    listing/refresh, `-o` options, tool/schema support) applied to different
    vendors (OpenRouter, Gemini). This note is a fourth data point for the same
    template, now applied to Meta.

- **Novel**:
  - **First in-corpus documentation of `llm-meta-ai` as a Meta model access path**:
    No prior source note documents this plugin, its install command, or the
    `meta-ai/` model-slug prefix.
  - **First explicit README-documented gap between a vendor API's stated
    multimodal capability and a day-one plugin's actual coverage** (MP4 video
    supported by Meta's API per Claim 8, but not yet implemented in the plugin
    per Claim 5): prior plugin-release notes in the corpus (llm-openrouter,
    llm-gemini) document added capabilities but not an explicitly acknowledged
    capability gap at initial release. This is a useful, concrete example of
    "plugin coverage lags API surface" that the guide can cite.

## Guide Impact

- **Chapter 01 (Daily Workflows — `llm` CLI model access)**: If the guide
  documents the `llm` CLI vendor-plugin ecosystem (as recommended in
  `blog-simonwillison-llm-gemini-032.md` Guide Impact), add `llm-meta-ai` as the
  Meta-family access plugin alongside llm-gemini, llm-openrouter, and native
  OpenAI. This is now four vendor plugins in the corpus following the identical
  template, which is strong enough evidence to state the template as a general
  rule for the `llm` ecosystem rather than describing each plugin individually:
  install → auth via `llm keys set <vendor>` or `<VENDOR>_TOKEN` env var → model
  listing with hourly cache + explicit `refresh` → standard `-o`/`-T`/`--schema`
  option surface.
- **Chapter 02 (Harness Engineering — Model Selection Interface / Plugin
  Architecture)**: Use this source alongside `blog-simonwillison-llm-openrouter-06.md`
  and `blog-simonwillison-llm-gemini-032.md` as the third and fourth confirmations
  that a stable "vendor plugin template" exists in the `llm` ecosystem: cached
  model list + refresh command, reasoning-effort/max-tokens options, tool/schema
  support inherited from the base library. Recommend the guide state this as a
  reusable pattern for practitioners building their own multi-vendor CLI harness:
  isolate vendor-specific auth and request/response translation behind a thin
  plugin layer, and let the base CLI/library supply the option surface (tools,
  schemas, reasoning controls) uniformly.
- **Chapter 02 or 04 (capability gaps between vendor API and tooling)**: Claim 5
  (MP4 video supported by Meta's API but not the plugin) is worth a callout as a
  general caution: a first-party CLI plugin's day-one feature set does not
  necessarily match the full capability of the underlying vendor API. Practitioners
  evaluating a new model via a convenience plugin should check the plugin's stated
  limitations before concluding the model itself lacks a capability.

## Extraction Notes

- **Thin primary source, as the Prospector anticipated**: The blog post itself is
  two sentences. Per MINER.md §1, this note follows the two links the post itself
  provides — the GitHub release page and Meta's own muse-spark-1.1 API
  announcement — plus the plugin's README (one hop further, from the GitHub
  release page to the repo) — to extract enough substance for a real source note.
  This matches the pattern already used for `blog-simonwillison-llm-openrouter-06.md`
  and `blog-simonwillison-llm-gemini-032.md`, the two closest analogues in the
  corpus.
- **No verbatim quotes available for most claims**: WebFetch returned the GitHub
  release notes, the plugin README, and Meta's announcement as structured
  paraphrases rather than raw markdown/HTML text, despite two fetch attempts per
  page. Per MINER.md §2a, claims without a confirmed verbatim source passage are
  marked `Quote: (no direct quote; see paraphrase in Our assessment)` rather than
  reconstructing quoted text. The one claim with a confirmed verbatim quote
  (Claim 1) is the GitHub release note bullet, which WebFetch reproduced
  identically across both the blog post fetch and the GitHub release fetch.
- **Two conflicting Prospector triage comments on this issue**: The issue has two
  triage comments with contradictory novelty assessments (one rates novelty
  "low," the other "high," and they identify different overlapping notes — the
  first cites no overlap, the second cites `blog-simonwillison-llm-shebang.md`).
  This note treats both as advisory context rather than authoritative; the actual
  novelty, as determined by direct extraction and cross-referencing against the
  corpus, sits between the two: the plugin itself is incremental (a routine new
  vendor plugin, following an established template), but the specific
  MP4-capability-gap observation and the fourth-vendor confirmation of the
  refresh/option-surface conventions are genuinely new data points, not previously
  documented in the corpus under this specific combination.
- **Meta's own announcement was evaluated but not deeply mined for capability
  claims**: Per MINER.md's caution about vendor marketing language, Meta's
  "zero-shot generalization to new native tools, MCP servers, and custom skills"
  and multi-agent orchestration claims (Claim 8) are marked anecdotal/vendor-stated
  and not independently verified — no benchmark or practitioner test of these
  specific claims is included in this note.
- **Cross-reference verification performed**: `blog-simonwillison-llm-openrouter-06.md`
  Claim 1 (lines 26-30) and Claim 5 (lines 44-48, via the version-history artifact
  at lines 73-74) confirmed for the refresh-command and reasoning_effort-flag
  claims. `blog-simonwillison-llm-shebang.md` Claim 5 (lines 103-115) and Claim 8
  (lines 148-158) confirmed for the `-T` and `--td` flag claims.
  `blog-simonwillison-muse-spark.md` Claim 3 (lines 76-92) confirmed for the
  `subagents.spawn_agent` cross-reference. `blog-simonwillison-llm-gemini-032.md`
  reviewed in full for the vendor-plugin-template comparison.
