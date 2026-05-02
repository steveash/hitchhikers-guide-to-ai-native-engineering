---
source_url: https://simonwillison.net/2026/Apr/23/gpt-5-5/
source_type: blog-post
title: "A pelican for GPT-5.5 via the semi-official Codex backdoor API"
author: Simon Willison
date_published: 2026-04-23
date_extracted: 2026-05-02
last_checked: 2026-05-02
status: current
confidence_overall: anecdotal
issue: "#473"
---

# A pelican for GPT-5.5 via the semi-official Codex backdoor API

> A first-person demonstration that `reasoning_effort xhigh` produces qualitatively different SVG output at 240× the reasoning token cost (9,322 vs 39 tokens), paired with a concrete example of using Claude Code to reverse-engineer the openai/codex OAuth flow and ship a working LLM plugin in a single afternoon session.

## Source Context

- **Type**: blog-post (Willison "link-blog + notes" format; ~600–800 words; includes concrete commands, token counts, and a model pricing table)
- **Author credibility**: Simon Willison is the creator of Django, creator of the `llm` CLI, and one of the most widely-cited practitioner commentators on LLM tooling. His "pelican on a bicycle" SVG test is a consistent cross-model benchmark he applies publicly. Posts in this format are first-person observation, not vendor marketing, with verifiable public artifacts (the plugin is published on PyPI). No disclosed affiliation with OpenAI or Anthropic.
- **Scope**: Two things: (1) reasoning_effort token tradeoff measured via the pelican SVG benchmark; (2) the Claude Code workflow that produced a working plugin (`llm-openai-via-codex`). Also includes GPT-5.5 pricing data. Does NOT cover: multi-session workflows, team patterns, or controlled comparison of reasoning effort across task types. The Codex subscription access mechanism is current ecosystem context — it may change as OpenAI formalizes official API access for GPT-5.5.

## Extracted Claims

### Claim 1: `reasoning_effort xhigh` produces qualitatively superior SVG output at 240× the reasoning token cost vs default

- **Evidence**: Willison ran the same "generate an SVG of a pelican on a bicycle" prompt with default settings (39 reasoning tokens, seconds to complete) and with `-o reasoning_effort xhigh` (9,322 reasoning tokens, ~4 minutes). The xhigh output was observably better — the default used simpler geometric approaches while xhigh used CSS-heavy gradients and more anatomically correct structure.
- **Confidence**: anecdotal (single prompt, single model, one practitioner; no controlled benchmark across task types)
- **Quote**: Default produced 39 reasoning tokens in seconds; xhigh produced 9,322 reasoning tokens and took nearly four minutes but was noticeably better.
- **Our assessment**: The 240× token ratio is a concrete data point practitioners can use to calibrate cost expectations before turning up reasoning effort. The qualitative output difference (approach strategy changed, not just polish level) suggests reasoning effort is selecting a different problem-solving strategy, not merely thinking longer about the same approach. Generalizing from one SVG prompt to code generation or other tasks requires caution — this is anecdote, not controlled evidence.

### Claim 2: Reasoning effort `xhigh` causes the model to adopt a qualitatively different solution strategy, not just improve output polish

- **Evidence**: At default settings, the model chose simpler geometric techniques; at xhigh, it adopted CSS-heavy gradient approaches — a different strategy for the same problem, not a more polished version of the same approach.
- **Confidence**: anecdotal (single task, single model instance)
- **Quote**: (Willison observes the technique difference; the CSS gradient approach is qualitatively distinct from the simpler default geometry)
- **Our assessment**: This is the more actionable signal for practitioners choosing reasoning effort settings. If xhigh only polished identical output, it would be a quality lever. If it changes strategy, it becomes relevant for tasks where the default strategy is wrong. This claim is based on one data point (the pelican SVG) — it needs corroboration from other task types before the guide should state it as a general principle.

### Claim 3: Claude Code can reverse-engineer an open-source OAuth/auth flow and produce a working CLI plugin in a single session

- **Evidence**: Willison used Claude Code to read the `openai/codex` OSS repository, identify where auth tokens are stored after a Codex CLI login, and build a working LLM plugin (`llm-openai-via-codex`) that routes through existing Codex subscriptions to access GPT-5.5. The plugin was published and is installable via `llm install llm-openai-via-codex`.
- **Confidence**: anecdotal (single session; publicly verifiable output — the plugin exists and is installable on PyPI)
- **Quote**: (Willison credits Claude Code with locating the auth token storage location in the openai/codex repo — the specific path not quoted verbatim in available summaries)
- **Our assessment**: The task framing is worth preserving: Willison did not know where Codex stored auth tokens — he gave Claude Code the repo and asked it to figure it out. This is the same "cold-start on undocumented code" pattern seen in the servo crate exploration (`blog-simonwillison-servo-crate-exploration.md`), but applied to OAuth/auth flow reverse-engineering rather than library API discovery. The publicly verifiable artifact (a working, installable plugin) raises confidence above purely anecdotal single-session claims.

### Claim 4: GPT-5.5 is priced at 2× GPT-5.4 ($5/$30 vs $2.5/$15 per 1M tokens), mirroring the Claude Sonnet/Opus pricing hierarchy

- **Evidence**: Willison cites the published OpenAI pricing: GPT-5.5 at $5/$30 per 1M input/output tokens; GPT-5.4 remaining at $2.5/$15. GPT-5.5 Pro at $30/$180. He explicitly draws the Sonnet/Opus analogy.
- **Confidence**: settled (published pricing at time of post; subject to change by OpenAI)
- **Quote**: "GPT-5.4 is to GPT-5.5 as Sonnet is to Opus" (Willison's characterization of the pricing tier relationship)
- **Our assessment**: The Sonnet/Opus mental model for cross-vendor model pricing tiers is a practitioner-useful heuristic: as of April 2026, both Anthropic and OpenAI have a consistent 2× step between standard and premium tiers. For practitioners building cost-aware routing logic, this enables like-for-like cost comparisons between providers. Pricing will evolve; the tier-structure mental model is more durable than the specific numbers.

### Claim 5: OpenAI has officially signaled that third-party integrations with Codex subscription access are welcome

- **Evidence**: Willison cites an official OpenAI statement from March 30th: "We want people to be able to use Codex, and their ChatGPT subscription, wherever they like!" This suggests the `/backend-api/codex/responses` endpoint Willison used is not unauthorized, but an officially permitted integration surface.
- **Confidence**: emerging (one official statement; OpenAI's policies on subscription API access may evolve as official GPT-5.5 API access expands and normalizes the access path)
- **Quote**: "We want people to be able to use Codex, and their ChatGPT subscription, wherever they like!" — OpenAI official statement, March 30th (cited by Willison)
- **Our assessment**: The signal is ecosystem-level: model vendors are beginning to distinguish "official API" from "subscription integration" access, and OpenAI has explicitly welcomed the latter. For practitioners building harnesses, this is relevant context for tool-layering decisions — but the specific Codex endpoint is a transient mechanism likely to be superseded once official API access for GPT-5.5 is fully formalized. Extract the ecosystem signal, not the specific endpoint.

### Claim 6: The `llm` CLI `reasoning_effort` option is the command-line primitive for controlling extended reasoning on capable models

- **Evidence**: Willison demonstrates the flag `-o reasoning_effort xhigh` as a command-line argument to the `llm` CLI when targeting GPT-5.5 via `llm-openai-via-codex`. This is consistent with how the `llm` CLI exposes model-specific options.
- **Confidence**: settled (the commands are published; the flag is documented in the plugin's interface)
- **Quote**: `llm -m openai-codex/gpt-5.5 -o reasoning_effort xhigh 'Your prompt'`
- **Our assessment**: The `-o reasoning_effort` flag generalizes across `llm` CLI plugins that support reasoning-capable models. It is the consistent interface for reasoning effort control in the `llm` ecosystem — analogous to the `-c` flag for multi-turn continuation documented in `blog-simonwillison-glm51.md`. Both are worth noting in harness-agnostic workflow documentation.

## Concrete Artifacts

### Full CLI workflow for GPT-5.5 via Codex subscription

```bash
# One-time setup: install the plugin
llm install llm-openai-via-codex

# Standard inference
llm -m openai-codex/gpt-5.5 'Generate an SVG of a pelican on a bicycle'

# Extended reasoning mode
llm -m openai-codex/gpt-5.5 -o reasoning_effort xhigh 'Generate an SVG of a pelican on a bicycle'
# → 9,322 reasoning tokens, ~4 minutes, qualitatively better output
```

*Source: Simon Willison, simonwillison.net/2026/Apr/23/gpt-5-5/*

### GPT-5.5 pricing table (at time of post, April 2026)

```
Model           Input             Output
GPT-5.5         $5/1M tokens      $30/1M tokens
GPT-5.5 Pro     $30/1M tokens     $180/1M tokens
GPT-5.4         $2.5/1M tokens    $15/1M tokens   (unchanged; 2× cheaper than GPT-5.5)
```

*Source: Simon Willison citing OpenAI published pricing, simonwillison.net/2026/Apr/23/gpt-5-5/*

### Reasoning token comparison for the pelican SVG benchmark

```
Settings                 Reasoning tokens   Wall time     Output strategy
Default                  39                 ~seconds      Simple geometry, basic approach
-o reasoning_effort xhigh  9,322            ~4 minutes    CSS-heavy gradients, better anatomy
```

*Source: Simon Willison, simonwillison.net/2026/Apr/23/gpt-5-5/, single-run observation on GPT-5.5*

## Cross-References

- **Corroborates**:
  - **blog-simonwillison-servo-crate-exploration.md** (Claim 1 — Claude Code cold-start on undocumented code): That note documents Claude Code reverse-engineering the `servo` v0.1.0 crate from sparse documentation; this post documents the same pattern applied to OAuth/auth flow detection in `openai/codex`. Both demonstrate the agent successfully extracting undocumented information and delivering a publicly verifiable artifact in one session. This is now two in-corpus examples of the same pattern from the same author — enough to call it a repeatable workflow, not a one-off.
  - **blog-simonwillison-glm51.md** (Claims on `llm` CLI plugin pattern and pelican benchmark context): The GLM-5.1 note documents the `llm` CLI + OpenRouter pattern and establishes the pelican benchmark as Willison's cross-model creative-code test. This post uses the same `llm` interface with a new plugin; the `-o reasoning_effort` flag is the novel addition. Both notes together trace the evolution of the `llm` CLI as a practitioner interface: plugin install → model flag → effort flag.

- **Contradicts**: None identified. No existing corpus note makes claims about reasoning_effort token counts or Claude Code OAuth reverse-engineering that conflict with this source.

- **Extends**:
  - **blog-simonwillison-servo-crate-exploration.md** (Claude Code codebase exploration pattern): The servo note establishes "give Claude Code a repo and a loose goal" for library API exploration. This post extends the pattern to a more targeted reverse-engineering framing: "find where this tool stores auth tokens." Both succeeded and produced verifiable artifacts; the combined evidence strengthens the case for this task-framing approach in Ch01.
  - **blog-simonwillison-glm51.md** (pelican benchmark and `llm` CLI): This post adds the `-o reasoning_effort` parameter to the `llm` CLI usage documented in the GLM-5.1 note, extending the interface coverage to reasoning-capable models and providing the first in-corpus token count data for a reasoning effort comparison.

- **Novel**:
  - **Concrete reasoning token counts for a specific task**: No existing corpus source documents quantitative reasoning token counts for any model or task. The 39 vs 9,322 token comparison is the first in-corpus measurement of reasoning effort cost.
  - **Reasoning effort → strategy change, not just polish**: No existing note distinguishes reasoning effort raising output quality from changing the solution approach. This is the first in-corpus observation that xhigh reasoning selects a qualitatively different strategy on the same prompt.
  - **Claude Code for OAuth/auth flow reverse-engineering → working plugin in one session**: The servo note covers library API exploration; this is the first in-corpus example of Claude Code performing auth flow reverse-engineering from OSS source code and producing a deployable integration artifact (not just a demo or exploration report).

## Guide Impact

- **Chapter 01 (Daily Workflows — Reasoning Effort Calibration)**: This post is the only in-corpus source with concrete reasoning token counts for a specific task. Recommend adding a note: "Reasoning effort levels produce qualitatively different outputs — Willison observed 9,322 reasoning tokens (xhigh) vs 39 (default) for the same SVG prompt, with xhigh adopting a different solution strategy, not just more polish. Budget ~4 minutes and ~240× the reasoning token cost for xhigh runs on creative/generative tasks." Caveat this as single-task anecdote; needs corroboration from code-generation tasks before broad claims.

- **Chapter 01 (Daily Workflows — AI-Assisted Tool Building)**: This is the second in-corpus example (after `blog-simonwillison-servo-crate-exploration.md`) of using Claude Code to reverse-engineer an unfamiliar codebase and ship a working tool in one session. Two examples from the same practitioner establish this as a repeatable workflow pattern: "Give Claude Code a repo and a goal (find where auth tokens live / figure out this API); expect a working, verifiable artifact within a single session." The combined evidence is strong enough to recommend adding this pattern explicitly to Ch01 workflows, with the caveat that both examples are from a single highly-experienced practitioner.

- **Chapter 02 (Harness Engineering — Model Selection / Cost)**: The 2× pricing tier signal and Sonnet/Opus mental model are worth a brief note for practitioners building cost-aware routing logic. As of April 2026, both Anthropic and OpenAI have a 2× step between standard and premium tiers — enabling like-for-like cost comparisons across providers when building model routing strategies.

## Extraction Notes

- **Three Prospector triage comments**: Three separate triage runs were filed (automated system ran multiple times). The second triage explicitly advises against extracting the Codex subscription access mechanism as a durable pattern; the third includes it as "harness/provider tension" context. I extracted it as Claim 5 with emerging confidence and noted the expected change. The pricing data is included because it was already published at time of post and is a concrete practitioner input for model selection cost modeling.
- **Fragment URL**: The issue body includes `#atom-everything` (an Atom feed anchor). `source_url` uses the canonical page URL without the fragment.
- **WebFetch limitations**: Full post verbatim text was not directly reproducible via WebFetch (returned structured summaries). Token counts and pricing figures are specific enough to be reliable in summary form, but some quotes are reconstructed paraphrases rather than directly quoted text. The post artifacts (commands, numbers) are verifiable via the published plugin.
- **No sub-pages followed**: The post links to the `llm-openai-via-codex` plugin on PyPI and the pelican SVG gallery. The install workflow and token counts are fully captured from the main post; no substantive engineering content was found to require sub-page follow-up.
