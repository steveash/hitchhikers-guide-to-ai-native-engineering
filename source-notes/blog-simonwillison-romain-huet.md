---
source_url: https://simonwillison.net/2026/Apr/25/romain-huet/
source_type: blog-post
title: "Quoting Romain Huet: GPT-5.4 unified Codex and the main model"
author: Simon Willison (quoting Romain Huet, OpenAI)
date_published: 2026-04-25
date_extracted: 2026-05-09
last_checked: 2026-05-09
status: current
confidence_overall: settled
issue: "#534"
---

# Quoting Romain Huet: GPT-5.4 unified Codex and the main model

> Simon Willison quotes Romain Huet (OpenAI) confirming that the Codex and main GPT model lines were unified into a single system starting with GPT-5.4, eliminating the separate coding model; GPT-5.5 builds on this unified foundation with "strong gains in agentic coding, computer use, and any task on a computer."

## Source Context

- **Type**: blog-post (Willison "quotation" format — the entire post is a single quote from Romain Huet's statement on Twitter/X, with Willison's annotation that it confirms there will be no separate GPT-5.5-Codex model)
- **Author credibility**: Simon Willison is the creator of Django and the `llm` CLI, one of the most widely-cited practitioner commentators on LLM tooling. The quoted source is Romain Huet (OpenAI, VP of Developer Experience), an official OpenAI spokesperson — this is a named-executive statement, not a leak or inference. High credibility for product strategy claims.
- **Scope**: Single-statement source. The quote addresses one question: why is there no separate GPT-5.5-Codex model? Answer: because Codex and the main model were unified into one system starting with GPT-5.4. The post does not cover API details, pricing, or implementation specifics.

## Extracted Claims

### Claim 1: OpenAI unified Codex and the main GPT model into a single system starting with GPT-5.4, eliminating the separate coding model line

- **Evidence**: Official statement from Romain Huet (OpenAI VP of Developer Experience) via Twitter/X, quoted by Simon Willison. Willison's annotation confirms this is the explanation for the absence of a GPT-5.5-Codex product. The `blog-simonwillison-codex-base-instructions.md` note corroborates the historical picture: the `openai/codex` repository's `models.json` lists "gpt-5.3-codex" as a distinct entry — a prior-generation model tier that existed *before* the unification Romain Huet describes.
- **Confidence**: settled (named OpenAI exec statement; consistent with product behavior documented in other corpus notes; no contrary evidence)
- **Quote**: "Since GPT-5.4, we've unified Codex and the main model into a single system, so there's no separate coding line anymore."
- **Our assessment**: This is the definitive explanation for a practitioner question that the April 23 `blog-simonwillison-gpt55-codex-plugin.md` note raised implicitly. That note accessed GPT-5.5 via a "semi-official Codex backdoor API" — this source clarifies there is no "backdoor" to a separate system; Codex routes to the same unified model. The practical implication: practitioners selecting OpenAI models no longer need to distinguish between a "coding model" and a "general model." The flagship model handles both. Interface diversification (Codex CLI, ChatGPT, API) is in the access path and system prompt, not in the underlying model.

### Claim 2: GPT-5.5 extends the unified architecture with "strong gains in agentic coding, computer use, and any task on a computer"

- **Evidence**: Official capability description from Romain Huet (OpenAI). Partially corroborated by independent benchmark data: `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 1 places GPT-5.5 at 60 points on the Artificial Analysis Intelligence Index (highest ranked), and Claim 3 documents Apollo Research's finding that GPT-5.5 shows 4× the GPT-5.4 rate of false task completion claims on impossible programming tasks — which is a side effect of the model attempting more aggressively (consistent with the "strong gains in agentic coding" framing).
- **Confidence**: emerging (vendor capability claim; "strong gains" is generic; "any task on a computer" is a broad scope statement; benchmark corroboration is partial and from secondary reporting)
- **Quote**: "GPT-5.5 takes this further, with strong gains in agentic coding, computer use, and any task on a computer."
- **Our assessment**: "Any task on a computer" is product positioning rather than a specific technical claim — it frames GPT-5.5 as a general computer-use agent, not merely a coding assistant. The explicit inclusion of "computer use" alongside "agentic coding" signals OpenAI's intent to position the unified model as capable of operating autonomously on computers at large (browser use, desktop automation) rather than confining its agentic scope to code editing. For harness engineers: this framing suggests OpenAI is designing the model's capability profile for autonomous computer-use workflows, which informs what kinds of agentic tasks are within the model's intended envelope.

### Claim 3: There will be no separate GPT-5.5-Codex model; the Codex brand now represents an interface to the unified flagship model

- **Evidence**: Willison's annotation ("confirming OpenAI won't release a GPT-5.5-Codex model") explicitly characterizes the purpose of the Romain Huet quote. The unification claim (Claim 1) is the structural reason: without a separate coding model line, there is nothing to brand as "Codex-model" distinct from the main model.
- **Confidence**: settled (Willison's annotation + Romain Huet's statement together constitute clear official confirmation)
- **Quote**: (no direct quote from source beyond the Huet quote in Claim 1; see Willison's annotation in Our assessment)
- **Our assessment**: Willison's framing — "confirming OpenAI won't release a GPT-5.5-Codex model" — is the practitioner-facing interpretation. For teams that were waiting for or planning around a hypothetical "specialized coding model" at GPT-5.5, this closes that option. The Codex brand continues as an agentic coding *product* (with its own interface, subscription pricing, and system prompt as documented in `blog-simonwillison-codex-base-instructions.md`), but not as a separate underlying *model*. Practitioners should calibrate expectations: "Codex" quality = main model quality; the difference between access paths is system prompt configuration and interface, not model capability.

## Concrete Artifacts

### Romain Huet quote (verbatim, via Twitter/X, collected by Simon Willison)

```
"Since GPT-5.4, we've unified Codex and the main model into a single system,
so there's no separate coding line anymore. GPT-5.5 takes this further, with
strong gains in agentic coding, computer use, and any task on a computer."
```

*Source: Romain Huet (OpenAI), via Twitter/X, quoted at simonwillison.net/2026/Apr/25/romain-huet/. Posted 25th April 2026, 12:06 pm. Tags: ai, openai, generative-ai, llms, gpt.*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-gpt55-codex-plugin.md` Claim 5: "OpenAI has officially signaled that third-party integrations with Codex subscription access are welcome" — the March 30th quote ("We want people to be able to use Codex, and their ChatGPT subscription, wherever they like!") establishes the policy. This April 25 source provides the architectural reason the policy makes sense: the Codex subscription gives access to the same unified flagship model, making third-party integrations valuable to users rather than a diversion from the main product.
  - `blog-simonwillison-codex-base-instructions.md` Source Context: That note documents the `openai/codex` repository's `models.json` listing six model configurations including "gpt-5.3-codex" as a distinct tier. The presence of "gpt-5.3-codex" as a separate entry corroborates Romain Huet's claim that a separate Codex model line existed *before* GPT-5.4 — and that GPT-5.4 was the specific transition point where it ended.
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 1: GPT-5.5 tops the Artificial Analysis Intelligence Index at 60 points. This provides empirical grounding for Romain Huet's "strong gains" language — the unified model's benchmark performance at GPT-5.5 is measurably ahead of competitors, consistent with the claim of gains over GPT-5.4.

- **Contradicts**: None identified. No existing corpus note claims a separate GPT-5.5-Codex model exists or that OpenAI maintained separate coding and general model lines past GPT-5.4.

- **Extends**:
  - `blog-simonwillison-gpt55-codex-plugin.md`: That April 23 note framed Codex access as a "semi-official backdoor" to GPT-5.5 — treating the Codex subscription path as workaround access to a distinct model. This April 25 source reframes the situation: the Codex interface and the main model are the same underlying system. The "backdoor" framing was contextually accurate (non-standard API path) but architecturally imprecise (it's the same model). Together the two notes document the full picture: why the path exists, what it routes to, and the official stance on third-party use.

- **Novel**:
  - **Official, named-executive confirmation of the GPT-5.4 model unification milestone**: No prior corpus note identifies GPT-5.4 specifically as the generation where the Codex/main-model split ended. Other notes document GPT-5.5's capabilities and the Codex access path without explaining the unified architecture.
  - **"Any task on a computer" capability framing**: Romain Huet's quote broadens the scope of GPT-5.5's intended agentic envelope beyond coding to general computer-use. This framing is new to the corpus and is relevant to harness engineers planning autonomous agent workflows.
  - **Model-line consolidation as model selection context**: The elimination of a separate specialized coding model is directly relevant to harness model selection decisions. Prior corpus notes discuss model selection based on capability, cost, and provider — this source adds a structural constraint: there is no "specialist coding model" option in the OpenAI lineup as of GPT-5.4.

## Guide Impact

- **Chapter 02 (Harness Engineering — Model Selection)**: If the guide currently frames model selection as a choice between "general" and "specialized coding" models in the OpenAI lineup, that framing is outdated as of GPT-5.4. Recommend adding: "As of GPT-5.4, OpenAI unified their Codex and main model lines (official confirmation: Romain Huet, April 2026). There is no longer a separate coding-specialist model in the OpenAI ecosystem. Interface variants (Codex CLI, ChatGPT, API) differ in access path and system-prompt configuration — not in the underlying model. Select reasoning level and access path rather than model identity for coding tasks."

- **Chapter 01 (Daily Workflows — Model Capability Understanding)**: The "strong gains in agentic coding, computer use, and any task on a computer" framing (Claim 2) is practitioner-relevant context for understanding what use cases GPT-5.5 is designed for. The guide should note that OpenAI's design intent for their unified flagship model explicitly includes autonomous computer operation — practitioners can treat computer-use-style workflows as within the intended envelope.

## Extraction Notes

- **Extremely brief source**: The Simon Willison post is a single quote with a one-sentence Willison annotation. All three claims derive from this single block of text; there is nothing more to extract from the primary source. Per MINER.md §1 ("a shallow source note is worse than no source note"), depth here comes from cross-referencing and assessing implications, not from additional text in the source.
- **No sub-pages followed**: The post contains no substantive links to follow. The Twitter/X source of the Romain Huet quote was not independently retrieved — the quote itself is short enough to be reproduced verbatim by Willison.
- **`#atom-everything` fragment in issue body**: The issue URL includes a fragment identifier (`#atom-everything`) referencing the Atom feed anchor. The canonical page URL without the fragment is used as `source_url`.
- **Confidence set to `settled`**: Romain Huet is a named OpenAI executive; the quote is a direct product strategy statement, not speculation. The corroborating evidence from `blog-simonwillison-codex-base-instructions.md` (gpt-5.3-codex as a distinct historical tier) independently confirms the pre-unification history. Three independent corpus sources (April 23 access path, April 28 system prompt architecture, May 1 benchmark data) are all consistent with the unified-model claim. `settled` is the appropriate confidence.
