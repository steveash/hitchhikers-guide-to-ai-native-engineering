---
source_url: https://simonwillison.net/2026/Sep/28/llm-anthropic/
source_type: blog-post
title: "llm-anthropic 0.30"
author: Simon Willison
date_published: 2026-09-28
date_extracted: 2026-10-06
last_checked: 2026-10-06
status: current
confidence_overall: settled
issue: "#3922"
---

# llm-anthropic 0.30

> A two-sentence Willison "beat" release note whose linked GitHub release notes show two tooling patterns: runtime model discovery from the provider's models API (no plugin release per new model) and pre-flight token counting via Anthropic's free token-counting API.

## Source Context

- **Type**: blog-post (Willison "beat" format, about 80 words, no code of its own). Following MINER.md §1, this note also reads the linked GitHub release notes for tag `0.30` (https://github.com/simonw/llm-anthropic/releases/tag/0.30), which hold the detail the beat omits.
- **Author credibility**: Simon Willison created and maintains `llm` and `llm-anthropic`, so these are first-party statements about design intent and behaviour.
- **Scope**: Covers three features (Sonnet 5.5 support, `refresh`, `count`). It does not give measurements, usage guidance, or cost data. The `count` and `refresh` material is announcement-level; the only mechanism detail comes from the release notes.

## Extracted Claims

### Claim 1: Runtime model refresh removes the need for a plugin release for every new model
- **Evidence**: Author statement. The release notes say `llm anthropic refresh` fetches the models available to the API key and caches them in `anthropic_models.json` in the LLM user directory.
- **Confidence**: settled (a stated design fact about a shipped feature; no measured benefit)
- **Quote**: "this release adds the ability to run llm anthropic refresh to refresh the list of Anthropic models directly from their API - which means I don't need to push a new release just to add support for a newly released model."
- **Our assessment**: Credible, and the context supports it. The same plugin shipped a release for each new model: Fable 5.1 in 0.28 and Sonnet 5.5 here. Sonnet 5.5 still needed a release, as the "In addition to Claude Sonnet 5.5" wording shows, so the benefit applies only to future models. The release notes name the cost: newly discovered models are registered from API-reported capabilities rather than hand-curated metadata.

### Claim 2: Unknown models are registered from the capabilities the API reports, not from hard-coded knowledge
- **Evidence**: Release notes (GitHub release 0.30), issues #77 and #97.
- **Confidence**: settled
- **Quote**: "Models this plugin does not know about are registered using the capabilities the API reports for them: image and PDF input, thinking, effort, structured outputs and maximum output tokens."
- **Our assessment**: This is the mechanism that makes Claim 1 work. A static table of per-model flags is replaced by capability discovery. Anything the API does not report (pricing, for example) is not covered. The release notes do not say what happens then.

### Claim 3: A companion `llm anthropic models` command lists what your key can access, with a `--json` option for the full capability data
- **Evidence**: Release notes, issue #77.
- **Confidence**: settled
- **Quote**: "New `llm anthropic models` command listing the models available to your API key. Add `--json` to see the full API response, including each model's capabilities."
- **Our assessment**: Small, but it makes the discovery inspectable. Registering models you can't see would be hard to debug.

### Claim 4: Token counts can be obtained before a prompt is sent, using a free API
- **Evidence**: The beat post, plus the release notes linking Anthropic's token-counting docs, issue #92.
- **Confidence**: settled
- **Quote**: "I also added an llm anthropic count command which can use their free token counting API to return a count of tokens that will be used by any prompt, before you send that prompt."
- **Our assessment**: The "free" claim comes from the author and was not checked against Anthropic's docs here. It supports a "measure before you spend" workflow. The post gives no example of the counts being used for cost control.

### Claim 5: The count command has parity with `llm prompt`, including tools, schemas, attachments, templates and conversation follow-ups
- **Evidence**: Release notes. The Python API is `model.count_tokens()` and returns an integer.
- **Confidence**: settled
- **Quote**: "It accepts the same options as `llm prompt`, including system prompts, attachments, fragments, templates, tools, schemas, model options and `-c` to count a follow-up in an existing conversation."
- **Our assessment**: This matters more than the headline. Tool definitions and schemas count towards input tokens, so counting the real assembled request, not just the text, is what makes the number useful for context budgeting.

### Claim 6: A bug broke every follow-up prompt after a refusal
- **Evidence**: Release notes, issues #37 and #94, credited to an outside contributor (Raj Royal).
- **Confidence**: settled
- **Quote**: "Fixed a bug where every follow-up prompt in a conversation after a refusal failed with a 400 error: \"all messages must have non-empty content except for the optional final assistant message\"."
- **Our assessment**: A concrete failure symptom. A refused turn leaves an empty message in the history, and the API rejects it on replay. It is relevant to anyone persisting conversation state across refusals. It is the same refusal path that 0.28 added (`ClaudeRefusal`), so that earlier feature shipped with this gap.

## Concrete Artifacts

```
# From the GitHub release notes for llm-anthropic 0.30 (simonw/llm-anthropic)
llm -m claude-sonnet-5.5 hi
llm anthropic refresh      # cache models from Anthropic models API -> anthropic_models.json
llm anthropic models --json
llm anthropic count ...    # same options as `llm prompt`; -c counts a follow-up
# Python: model.count_tokens(...) -> int  (same arguments as model.prompt())
```

Error string quoted in the release notes: `all messages must have non-empty content except for the optional final assistant message` (HTTP 400).

## Cross-References

- **Corroborates**: `blog-simonwillison-claude-sonnet-55.md` (same-day Sonnet 5.5 coverage). Its Claim 3 describes a max-effort run that burned 128,000 reasoning tokens for no output, a runaway-cost case that pre-flight counting does not prevent. See Our take under Guide Impact.
- **Contradicts**: none found.
- **Extends**: `blog-simonwillison-llm-anthropic-028.md` (0.28 introduced the refusal exception; 0.30 fixes a follow-up bug on that path) and `blog-simonwillison-llm-anthropic-027.md` (earlier release in the series).
- **Novel**: Runtime model discovery as an alternative to per-model releases, and CLI-level pre-flight token counting; neither appears in the earlier notes in this series.

## Guide Impact

- **Building Tools & APIs / LLM integration chapter**: Candidate pattern: tools that wrap a provider API should discover models and capabilities at runtime, with a cached refresh command, and not ship a static model list. Cite this note, as a single example.
- **Token management / cost chapter**: Add as an example of pre-flight counting. Note the limit: it counts input tokens only. Output and reasoning tokens are not covered, so it does not address the runaway-reasoning case in `blog-simonwillison-claude-sonnet-55.md` Claim 3.
- **Failure modes**: The refusal follow-up 400 error is a small example of conversation-replay bugs after a refusal.
- Low priority overall. The source is a release beat, and the evidence is one author's tool.

## Extraction Notes

- The beat post is two sentences. The release notes are the only linked page and are the source of Claims 2, 3, 5 and 6. I did not follow the issues (#77, #92, #94, #96, #97) or Anthropic's token-counting docs, so "free" and the capability list are as stated by the author.
- No contradictions with existing notes, so none were filed.
