---
source_url: https://simonwillison.net/2026/Apr/25/gpt-5-5-prompting-guide/
source_type: blog-post
title: "GPT-5.5 Prompting Guide"
author: Simon Willison
date_published: 2026-04-25
date_extracted: 2026-05-04
last_checked: 2026-05-04
status: current
confidence_overall: emerging
issue: "#529"
---

# GPT-5.5 Prompting Guide

> Simon Willison's curated link-post highlights OpenAI's official guidance on prompting GPT-5.5: a concrete UX pattern for multi-step agent tasks (send a user-visible update before tool calls), and a migration principle — treat GPT-5.5 as a new model family requiring fresh baselines, not a drop-in replacement for gpt-5.2 or gpt-5.4.

## Source Context

- **Type**: blog-post (Willison link-post with commentary; short (~400 words), published April 25, 2026; links to two OpenAI official resources: the GPT-5.5 prompting guide on developers.openai.com and the "Using GPT-5.5" migration guide)
- **Author credibility**: Simon Willison is the creator of Django and the `llm` CLI, and one of the most widely-read practitioner commentators on LLM tooling. His link-posts curate and contextualize official releases, adding practitioner interpretation. The underlying sources he summarizes here are official OpenAI documentation and the Codex app. His curatorial judgment is high-signal; the content here is primarily official vendor guidance.
- **Scope**: Covers two distinct patterns from OpenAI's GPT-5.5 guidance: (1) a UX pattern for multi-step agent tasks, and (2) a prompt migration methodology for practitioners upgrading from older OpenAI models. Does NOT cover: GPT-5.5 reasoning token costs (see `blog-simonwillison-gpt55-codex-plugin.md`), hallucination rates (see `blog-thebatch-gpt55-hallucination-kimi-k26.md`), benchmark data, or non-OpenAI model migration. The guidance is GPT-5.5 specific; transferability to other model families (Claude, Gemini) is not addressed.

## Extracted Claims

### Claim 1: GPT-5.5 is now available in the API, triggering official OpenAI prompting guidance for practitioners

- **Evidence**: Willison's introduction states GPT-5.5 API availability directly and frames the post as a response to official guidance becoming available.
- **Confidence**: settled (API availability widely confirmed; official documentation release is the trigger for this post)
- **Quote**: "Now that GPT-5.5 is available in the API, OpenAI have released a wealth of useful tips on how best to prompt the new model."
- **Our assessment**: Context-setting claim. The significance is that API availability + official migration guidance together signal that practitioners should now be making active GPT-5.5 adoption decisions, not waiting. Corroborates the model availability context established in `blog-simonwillison-gpt55-codex-plugin.md`.

### Claim 2: For multi-step agent tasks, sending a user-visible progress update before tool calls prevents perceived application freeze

- **Evidence**: Official OpenAI guidance in the GPT-5.5 prompting guide. No empirical study is cited; the guidance is prescriptive from the model vendor.
- **Confidence**: emerging (official vendor guidance; the problem it addresses — users perceiving application freeze during silent tool execution — is a well-recognized UX failure mode, which increases plausibility)
- **Quote**: "Before any tool calls for a multi-step task, send a short user-visible update that acknowledges the request and states the first step. Keep it to one or two sentences."
- **Our assessment**: This is the most immediately actionable claim for harness engineers building agent UX. The problem it solves is real: agents that silently execute tool chains for seconds or minutes produce no visible signal to end users, who may assume the application has crashed. The specific prescription (1-2 sentences acknowledging the request + stating the first step, before the tool call, not after) is concrete enough to implement directly. The limitation: this is prompting advice — whether compliance can be enforced programmatically or only through system prompt instruction is not addressed.

### Claim 3: GPT-5.5 should be treated as a new model family requiring fresh tuning, not a drop-in replacement for gpt-5.2 or gpt-5.4

- **Evidence**: Official OpenAI guidance in the "Using GPT-5.5" guide, highlighted by Willison as a key migration principle. The explicit naming of gpt-5.2 and gpt-5.4 as prior versions not to treat as interchangeable suggests this was a concrete problem OpenAI observed.
- **Confidence**: emerging (official vendor guidance; authoritative for the intended behavior, though architectural reasons for the non-compatibility are not stated)
- **Quote**: "To get the most out of GPT-5.5, treat it as a new model family to tune for, not a drop-in replacement for `gpt-5.2` or `gpt-5.4`."
- **Our assessment**: This is the most significant migration signal in the post. The explicit "not a drop-in replacement" language directly contradicts the common practitioner assumption that incrementally numbered model versions can be swapped into existing prompt stacks with no rework. OpenAI is signaling that GPT-5.5 represents a qualitative change in behavior, not just a capability increment. For practitioners who built on GPT-5.2 or GPT-5.4, this means migration is a re-tuning exercise, not a version bump. The practical implication: any A/B test treating GPT-5.5 as a swap for an older model will measure performance under suboptimal prompting conditions.

### Claim 4: Prompt migration should begin with the smallest prompt that preserves the product contract, then tune specific parameters against representative examples

- **Evidence**: Official OpenAI guidance in the "Using GPT-5.5" guide, forming the second half of the migration methodology alongside Claim 3.
- **Confidence**: emerging (official vendor guidance; the "start minimal" framing is consistent with general prompt engineering best practice, increasing plausibility)
- **Quote**: "Begin migration with a fresh baseline instead of carrying over every instruction from an older prompt stack. Start with the smallest prompt that preserves the product contract, then tune reasoning effort, verbosity, tool descriptions, and output format against representative examples."
- **Our assessment**: This provides an ordered methodology for model migration at the prompt layer: (1) establish the minimal baseline that keeps your product functional; (2) tune four specific dimensions — reasoning effort, verbosity, tool descriptions, output format — against real examples, not synthetic tests. The "product contract" framing is precise: the baseline is not the simplest possible prompt but the simplest one that fulfills the observable external specification users depend on. The four named tuning dimensions correspond to distinct model behavior levers that GPT-5.5 exposes; this is not generic prompt engineering advice but GPT-5.5-specific parameter guidance.

### Claim 5: OpenAI's Codex app includes a migration skill command for updating existing projects to GPT-5.5

- **Evidence**: Willison's post mentions a Codex app command; the command is presented as a concrete migration tool alongside the manual methodology of Claims 3-4.
- **Confidence**: anecdotal (one mention in Willison's link-post; the command is presented as a Codex skill or shortcut, not a fully documented feature)
- **Quote**: "$openai-docs migrate this project to gpt-5.5"
- **Our assessment**: The existence of this command is evidence that OpenAI recognized migration friction as a real, common problem worth building tooling for. The `$openai-docs` invocation style suggests a Codex-specific skill (analogous to invoking a tool within the Codex chat interface). Practitioners on OpenAI's platform should be aware this exists before attempting manual migration. The command's scope and reliability are not described in the source.

## Concrete Artifacts

### GPT-5.5 Migration Methodology (from the "Using GPT-5.5" official guide, via Willison)

```
MODEL MIGRATION APPROACH FOR GPT-5.5

Principle: "treat it as a new model family to tune for, not a drop-in replacement
            for gpt-5.2 or gpt-5.4"

Step 1 — Establish a fresh baseline
  "Begin migration with a fresh baseline instead of carrying over every
   instruction from an older prompt stack."
  → Start with the minimum prompt that satisfies the product's external behavior contract.
  → Do NOT port the full existing system prompt.

Step 2 — Tune across four dimensions against representative examples:
  - Reasoning effort     (e.g., xhigh / high / medium / low / none)
  - Verbosity            (output length and detail calibration)
  - Tool descriptions    (how tools are described to the model)
  - Output format        (structure, schema, or presentation of responses)

  "Start with the smallest prompt that preserves the product contract, then
   tune reasoning effort, verbosity, tool descriptions, and output format
   against representative examples."

Optional: Codex migration skill
  $openai-docs migrate this project to gpt-5.5

Source: OpenAI "Using GPT-5.5" guide, cited in Simon Willison,
        simonwillison.net/2026/Apr/25/gpt-5-5-prompting-guide/, April 25, 2026
```

### User-Visible Progress Update Pattern (from the GPT-5.5 prompting guide, via Willison)

```
UX PATTERN: Pre-tool-call acknowledgment for multi-step agent tasks

Problem: Users perceive application freeze when agents silently execute tool chains.

Pattern:
  BEFORE any tool calls for a multi-step task:
    → Send a short user-visible update (1-2 sentences)
    → Acknowledge the request
    → State the first step to be taken

  THEN: proceed with the tool calls

Official guidance:
  "Before any tool calls for a multi-step task, send a short user-visible
   update that acknowledges the request and states the first step.
   Keep it to one or two sentences."

Source: OpenAI GPT-5.5 prompting guide, cited in Simon Willison,
        simonwillison.net/2026/Apr/25/gpt-5-5-prompting-guide/, April 25, 2026
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-harness-long-running.md` Claim 9: "every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing." The "treat as new model family" claim here corroborates this at the prompt layer: existing system prompts and harness instructions encode assumptions about how older models behave. On model upgrade, those assumptions go stale. The Anthropic post states the general principle; this source provides the OpenAI-specific operationalization.
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 4: The editorial "swap models as easily as bumping a dependency" principle. The fresh baseline approach here is the prompting-layer counterpart to that architectural principle — swapping model versions requires deliberate prompt re-tuning, not just a dependency bump. Together they make the same point from two directions: architectural and prompting.
  - `blog-simonwillison-gpt55-codex-plugin.md` Claim 1 and 4: That note (April 23, 2026) establishes GPT-5.5's reasoning effort token tradeoffs and pricing. This note (April 25, 2026) adds the prompting strategy for using those capabilities effectively. Both are from Willison, two days apart, forming a complementary pair.

- **Contradicts**: None filed. The "fresh baseline" recommendation potentially contradicts the implicit assumption that prompt stacks are incrementally transferable across model versions, but no existing source note in the corpus makes an explicit claim that GPT-5.5 or similar new-family models accept old prompts without re-tuning. No contradiction issue required.

- **Extends**:
  - `blog-simonwillison-gpt55-codex-plugin.md`: That note covers what GPT-5.5 can do (reasoning token costs, pricing, access via Codex). This note covers how to prompt it (fresh baseline, four-dimension tuning, pre-tool-call UX pattern). Together they give practitioners a more complete picture for GPT-5.5 adoption.
  - `blog-anthropic-harness-long-running.md` Claim 9: The Anthropic post establishes "re-examine harness components at each model upgrade." This source extends that principle to the prompt layer with specific OpenAI guidance on what to do: start from the smallest working prompt, not from the existing prompt stack.
  - `docs-github-copilot-gpt52-deprecation.md`: That note documents GPT-5.2 deprecation effective June 1, 2026 with GPT-5.5 as the named replacement. This source provides the migration methodology for exactly that transition — practitioners receiving the deprecation notice need a plan; this source provides it.

- **Novel**:
  - **Pre-tool-call user-visible update as a named pattern**: No existing note captures this specific UX pattern for preventing perceived freeze during silent tool execution in multi-step agent tasks. This is the first in-corpus prescriptive pattern for agent UX feedback loops.
  - **Official vendor guidance to discard old prompt stacks on model family transition**: No existing source provides explicit official OpenAI guidance on prompt migration strategy at the model-family level. This is the first in-corpus statement that prompt stacks are NOT incrementally portable across OpenAI model generations.
  - **Four-dimension prompt tuning framework**: The named dimensions (reasoning effort, verbosity, tool descriptions, output format) are the first in-corpus explicit enumeration of what to tune when migrating prompts to a new model. Other sources discuss prompt engineering generally; this provides GPT-5.5-specific parameter guidance.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the pre-tool-call user-visible update pattern as a concrete UX best practice for agent harness design. Current guide content (if any) on agent UX does not capture this specific pattern. Recommended addition: "For multi-step agent tasks, emit a brief acknowledgment + first step before any tool calls. Keep it to 1-2 sentences. This prevents users from perceiving application freeze during silent tool-chain execution." Cite this source and present the pattern from the Concrete Artifacts section.

- **Chapter 02 or Chapter 03 (Model Selection / Prompt Engineering)**: Add a "Model Family Migration" section or note. The guide should explicitly state: "When upgrading to a new model family — OpenAI's GPT-5.5 being the documented example — do not port existing prompt stacks. Establish the minimal prompt that preserves your product's external behavior, then tune reasoning effort, verbosity, tool descriptions, and output format against representative examples." This directly counters the dependency-bump assumption and gives practitioners a structured migration path. Cite this source alongside `blog-anthropic-harness-long-running.md` Claim 9 as the two-sided view: the general principle (Anthropic) and the specific methodology (OpenAI/Willison).

- **Chapter 04 (Context Engineering / Execution Patterns)**: The Codex migration skill (`$openai-docs migrate this project to gpt-5.5`) is worth a footnote for practitioners on OpenAI's platform — a tooling option alongside the manual methodology.

## Extraction Notes

- **Source is a curated link-post**: Willison's own prose is brief. The substantive content is from two OpenAI official resources he links: the GPT-5.5 prompting guide (developers.openai.com, returned 403 on direct fetch) and the "Using GPT-5.5" migration guide (URL not captured). The blockquotes in the source note are attributed to those official documents as surfaced through Willison's post.
- **WebFetch returned summaries, not raw HTML**: Multiple fetches were performed. Verbatim quotes were extracted from the final fetch which returned structured blockquote text. The quotes from the "Using GPT-5.5" guide (Claims 3-4) appear in the source as a single contiguous blockquote. The pre-tool-call update quote (Claim 2) is from the separate GPT-5.5 prompting guide.
- **Fragment URL in issue body**: The issue body includes `#atom-everything` (an Atom feed anchor). `source_url` uses the canonical page URL without the fragment, consistent with `blog-simonwillison-gpt55-codex-plugin.md` extraction notes.
- **No sub-pages followed**: The linked OpenAI developer docs page returned HTTP 403. The Codex app is not a text source suitable for extraction. All substantive content is from the main Willison post.
- **Three Prospector triage comments**: Three separate triage runs were filed on this issue (automated system ran multiple times). All three agree on high novelty and the core claims; chapter assignments vary across the three comments. This extraction follows the most specific guidance (triage comment 3: Ch02 for prompting/harness, Ch04 for model selection, Ch03 for tool use agents).
