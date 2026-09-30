---
source_url: https://simonwillison.net/2026/Sep/22/llm/
source_type: blog-post
title: "llm 0.36"
author: Simon Willison
date_published: 2026-09-22
date_extracted: 2026-09-30
last_checked: 2026-09-30
status: current
confidence_overall: settled
issue: "#3798"
---

# llm 0.36

> A Willison "beat" release note for `llm` 0.36 whose substance is a small plugin-API capability declaration, `supports_conversation = False`, for single-turn-only models (with a core-enforced `llm.ConversationNotSupported` error), plus `<details>`-wrapped reasoning traces in `llm logs` Markdown and GPT-6 Sol/Luna model IDs.

## Source Context

- **Type**: blog-post (release beat, ~100 words). Per MINER.md §1 the note also follows the GitHub release notes for 0.36, issue #1692 (the feature's origin), issue #1701 (reasoning-trace wrapping), and the "Models that do not support conversations" section of the advanced-model-plugins docs.
- **Author credibility**: Simon Willison is the creator and maintainer of `llm`; this is first-party release documentation. Issue text and the docs page are also his.
- **Scope**: The three headline features and the bug-fix list. Does not cover GPT-6 Sol/Luna capabilities or pricing (see issue #3799), and contains no benchmarks.

## Extracted Claims

### Claim 1: Model plugins can declare `supports_conversation = False`, and core enforces it with a dedicated exception
- **Evidence**: Release notes; docs section with a minimal `SingleTurnModel` example; closes #1692.
- **Confidence**: settled (shipped, documented API)
- **Quote**: "Model plugins can now declare supports_conversation = False for models that only accept single-turn prompts."
- **Our assessment**: A capability flag in the same family as the existing `supports_schema` and `supports_tools` flags. It moves a constraint that each plugin would otherwise hand-roll into the harness layer, so callers get one uniform failure mode.

### Claim 2: Enforcement happens before the model is invoked, at both library and CLI level
- **Evidence**: Release notes and docs.
- **Confidence**: settled
- **Quote**: "LLM raises llm.ConversationNotSupported when these models receive assistant or tool history, and llm chat rejects them before starting a session."
- **Our assessment**: Fail-fast validation on message history (assistant or tool roles) rather than a provider error mid-session. The docs add that the exception is a `ValueError` subclass raised "before calling execute()", and that `llm -c` / `--cid` also report an error. Plugins registering both sync and async models must set the flag on both classes.

### Claim 3: The feature was motivated by a non-chat model shape (a typed "decision model") that still fits the abstraction layer
- **Evidence**: Issue #1692, which shows the prior per-plugin workaround (an `execute()` that raises `ValueError` if any message has role assistant or tool).
- **Confidence**: settled for the motivation; the flagged-model example is anecdotal (one alpha plugin).
- **Quote**: "it's a different shape of model that could still fit LLM's abstraction layer, but only if we mark it as not allowing replies/conversations."
- **Our assessment**: Illustrates a harness design lesson: to keep one interface across heterogeneous models, add explicit capability declarations instead of assuming every model is a chat model. The first adopter is `llm-typesafe`.

### Claim 4: Reasoning traces in `llm logs` Markdown are now collapsed in `<details><summary>`
- **Evidence**: Release notes; issue #1701, which says a prototype renderer was used and liked.
- **Confidence**: settled
- **Quote**: "Reasoning traces in the Markdown output of llm logs are now wrapped in <details><summary> tags."
- **Our assessment**: Motivation per the issue: "The reasoning traces get in the way of viewing the responses." A readability choice: keep traces in the log but fold them by default. Relevant to transcript review.

### Claim 5: GPT-6 Sol and Luna are added as built-in model IDs
- **Evidence**: Release notes, #1702.
- **Confidence**: settled (as a release fact)
- **Quote**: "New OpenAI models: gpt-6-sol for GPT-6 Sol and gpt-6-luna for GPT-6 Luna."
- **Our assessment**: Routine continuation of `llm` tracking frontier OpenAI models; no analysis in the source.

### Claim 6: Release includes several community-contributed robustness fixes from five new contributors
- **Evidence**: Release notes list, including async logging, SQLite connection cleanup, and stream-close behavior.
- **Confidence**: settled
- **Quote**: "Closing an asynchronous response.astream_events() stream before completion now closes the underlying provider generator, allowing it to release streaming connections and other resources."
- **Our assessment**: Minor, but the stream-cleanup and `AsyncResponse.log_to_db()` fixes show the async/event-streaming surface introduced in 0.32 still being hardened.

## Concrete Artifacts

```python
# Source: llm docs, "Models that do not support conversations"
# (https://llm.datasette.io/en/stable/plugins/advanced-model-plugins.html)
class SingleTurnModel(llm.Model):
    model_id = "single-turn"
    supports_conversation = False

    def execute(self, prompt, stream, response, conversation):
        yield "A response to this prompt"
```

```python
# Source: github.com/simonw/llm issue #1692 — the per-plugin workaround the flag replaces
def execute(self, prompt, stream, response, conversation, key=None):
    if any(
        message.role in ("assistant", "tool")
        for message in prompt.messages
    ):
        raise ValueError(
            "TypeSafe supports single-turn evaluation only. "
            "Start a new prompt instead of continuing or replying."
        )
```

## Cross-References

- **Corroborates**: `blog-simonwillison-llm032.md` Claim 2 (reasoning traces handled as a distinct stream in the CLI) — 0.36 continues treating traces as separable, collapsible output.
- **Contradicts**: None identified.
- **Extends**:
  - `blog-simonwillison-llm-typesafe-010a0.md` Claim 1 (Jev exposed as a typed-answer model via the ordinary LLM CLI) — this source explains the core change that plugin depended on; that note does not mention `supports_conversation`.
  - `blog-simonwillison-llm032.md` Claim 7 (`model.prompt(messages=[])` accepts full conversation history) — 0.36 adds the guard that rejects assistant/tool history for single-turn models.
  - `blog-simonwillison-llm034.md` (llm logs improvements: duration fields, caching) — same log-viewing readability thread.
- **Novel**: The capability-flag-plus-core-exception pattern for single-turn-only models; no prior note covers it.

## Guide Impact

- **Chapter 02**: Where the guide discusses multi-model harness or plugin design, cite `supports_conversation = False` (Claims 1–3) as an example of declaring model capabilities explicitly and enforcing them in the harness before dispatch, rather than per-plugin ad hoc checks. Narrow evidence: single tool, one adopter.
- **Chapter 04**: Optional minor mention that collapsing reasoning traces by default in log output (Claim 4) keeps transcripts reviewable.

## Extraction Notes

- Blog post is thin (three feature bullets); substance comes from release notes, issues #1692 and #1701, and the docs page. Issue #1702 and the bug-fix PRs were not fetched individually.
- Cross-reference claim numbers verified against the cited notes by document-order count (llm032 Claims 2 and 7; typesafe Claim 1). llm034 is cited by note, not claim number.
- No contradictions found; nothing filed under MINER.md §4a.
- The triage comments reference `blog-simonwillison-gpt6-astra-launch.md`; GPT-6 details were not needed here.
