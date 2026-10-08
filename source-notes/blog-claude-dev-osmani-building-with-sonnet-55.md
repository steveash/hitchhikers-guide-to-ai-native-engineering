---
source_url: https://claude.dev/blog/building-with-claude-sonnet-5-5/
source_type: blog-post
title: "Building with Claude Sonnet 5.5"
author: Addy Osmani (Claude blog)
date_published: 2026-09-28
date_extracted: 2026-10-08
last_checked: 2026-10-08
status: current
confidence_overall: emerging
issue: "#3981"
---

# Building with Claude Sonnet 5.5

> Vendor playbook for Sonnet 5.5: pricing and model details, six Sonnet 5 → 5.5 migration changes (`between_tools` thinking, forced `tool_choice` removal, append-only thinking blocks, computer-use toolset, advisor pairing, thinking-block progress text), effort-tuning starting points, a "run a real check" system-prompt paragraph, and refusal handling.

## Source Context

- **Type**: blog-post (vendor "Playbooks" guide, ~9 min read)
- **Author credibility**: Byline is Addy Osmani on the Claude blog. First-party, so authoritative on API behavior (parameter names, 400 errors are checkable against the API); performance claims ("30% faster", "up to 30% less") come with no methodology.
- **Scope**: Model choice vs Opus 5.5, pricing, model details table, migration steps with code, tuning, refusals/fallback, availability and Claude Code defaults. Does NOT cover benchmarks or independent measurements. Links to a separate migration guide and prompting guide that were not followed.

## Extracted Claims

### Claim 1: Per-token price is unchanged from Sonnet 5, but total cost per task drops because Sonnet 5.5 uses fewer tokens
- **Evidence**: Vendor statement; price table; no measured methodology.
- **Confidence**: emerging (vendor claim)
- **Quote**: "The per-token price is unchanged and because Sonnet 5.5 typically needs far fewer tokens to do the same work, it costs up to 30% less for most work."
- **Our assessment**: Hedged ("up to", "most work") and unmeasured here. Same story as the Willison and GitHub notes; three channels, one vendor source. Record as vendor-reported.

### Claim 2: Sonnet 5.5 is half the price of Opus 5.5 on every token class except cache reads
- **Evidence**: Pricing table: input $2 vs $4, output $10 vs $20, 5-min cache write $2.50 vs $5, 1-hour write $4 vs $8, cache read $0.20 for both.
- **Confidence**: settled (published price list, as of the post date)
- **Quote**: "All Sonnet 5.5 prices, including batch processing and prompt caching, match Sonnet 5's, so swapping the model ID doesn't change your per-token bill."
- **Our assessment**: The table is reproduced under Concrete Artifacts. Useful for routing/cost reasoning; verify prices before citing in the guide.

### Claim 3: `thinking: {"type": "disabled"}` now returns 400; `between_tools` replaces it, with strict limits
- **Evidence**: Before/after code; list of limits.
- **Confidence**: settled (API behavior, first-party)
- **Quote**: "With between_tools, thinking only happens between tool calls, and total response time is the same or faster."
- **Our assessment**: A breaking change for any harness that disabled thinking. Limits: works only at low/medium/high (400 at xhigh/max), accepts no `display`, `budget_tokens` or `block_binding`, and effort can't change mid-conversation. Source says: "between_tools works at low, medium and high effort. At xhigh or max it returns a 400 error; to run there, use adaptive thinking."

### Claim 4: Forced `tool_choice` (`any` or `tool`) returns 400; use `auto` + `strict: true` + `additionalProperties: false`
- **Evidence**: Code example; applies to token counting endpoint too.
- **Confidence**: settled (API behavior)
- **Quote**: "tool_choice of type any or tool returns a 400 error, including on the token counting endpoint."
- **Our assessment**: Directly affects harnesses that force a structured-output tool call. The replacement relies on the prompt saying when to use the tool (the example prompt says "Use the get_weather tool."), so reliability is prompt-dependent, not guaranteed.

### Claim 5: Thinking blocks are model-bound; only Sonnet 5 → 5.5 switching keeps reasoning, so keep conversations append-only
- **Evidence**: Vendor statement.
- **Confidence**: settled
- **Quote**: "Sonnet 5.5 reads Sonnet 5's thinking blocks, so a conversation you switch from Sonnet 5 to Sonnet 5.5 keeps its reasoning. No other model reads Sonnet 5.5's blocks."
- **Our assessment**: Implies mid-conversation downgrades to other models lose reasoning continuity. Relevant to model-routing designs that swap models per turn.

### Claim 6: Computer use requires `computer_toolset_20260801` on Claude API and Google Cloud; old tool type returns 400
- **Evidence**: Migration step 4 with header and SDK changes.
- **Confidence**: settled
- **Quote**: "a request that declares computer_20251124 returns a 400 error."
- **Our assessment**: Also requires dropping the `computer-use-2025-11-24` beta header and `fine-grained-tool-streaming-2025-05-14` (use `eager_input_streaming: true` per tool). Bedrock still accepts `computer_20251124`, so behavior is platform-dependent.

### Claim 7: Advisor pairing is restricted, and advice comes back encrypted
- **Evidence**: Migration step 5.
- **Confidence**: settled
- **Quote**: "Advice from every accepted advisor comes back encrypted, as an advisor_redacted_result block, so your code can't read the advice text."
- **Our assessment**: Sonnet 5.5 executor rejects Opus 4.8, Opus 4.7, Sonnet 5; accepts Opus 5.5, Opus 5, Sonnet 5.5. Notable: the harness cannot log or audit advisor text.

### Claim 8: Progress notes between tool calls now arrive as `thinking` blocks that are empty at default `display`
- **Evidence**: Migration step 6.
- **Confidence**: settled
- **Quote**: "This change causes no errors, but a UI can stop showing the model's notes between tool calls."
- **Our assessment**: A silent failure mode (no error). Fix: `display` of `"updates"` (beta) or `"summarized"`, rendering each non-empty thinking block before the following `tool_use`.

### Claim 9: Re-run the effort sweep; effort levels are recalibrated, and start points depend on workload
- **Evidence**: Vendor guidance; no data.
- **Confidence**: emerging
- **Quote**: "Effort levels are recalibrated, so a level doesn't produce the same amount of thinking as it did on Sonnet 5, and your old setting won't carry over."
- **Our assessment**: Start `high` by default; `medium` for well-specified agentic coding, `high` for harder/longer; `medium`/`low` for chat/latency-sensitive; "Use xhigh or max only where your evals show a quality gain." Consistent with Willison's "max" failure (Claim 3 there).

### Claim 10: Asking the model in the system prompt to think less does not reliably reduce thinking; lower the effort instead
- **Evidence**: Vendor statement.
- **Confidence**: emerging
- **Quote**: "To get less thinking, lower the effort level, because asking the model in the system prompt to think less doesn't reliably reduce it."
- **Our assessment**: Matches the Opus 5.5 note's advice to drop "think hard" lines. Also: thinking counts toward `max_tokens`; for agentic coding set it to 128,000 and stream.

### Claim 11: Remove Sonnet 5 workarounds and re-run evals before other tuning
- **Evidence**: Vendor guidance.
- **Confidence**: emerging
- **Quote**: "If your prompts carry workarounds such as refusal steering, tool-call retry shims, or \"do not be lazy,\" remove them and re-run your evals before tuning anything else."
- **Our assessment**: Good hygiene advice; unquantified.

### Claim 12: At `low` effort the model sometimes skips a check that exercises the change; add a system-prompt rule requiring real checks
- **Evidence**: Vendor-provided prompt paragraph (see artifacts).
- **Confidence**: emerging
- **Quote**: "at low effort it sometimes skips a check that exercises the change."
- **Our assessment**: Concrete, copyable verification prompt. It defines what does not count (syntax-only, failed-to-start check) and requires reporting the unrun check otherwise.

### Claim 13: Do not ask the model to write out its reasoning; it invites `reasoning_extraction` declines
- **Evidence**: Vendor statement.
- **Confidence**: emerging
- **Quote**: "Don't ask the model to write out its reasoning in the response, because that invites reasoning_extraction declines."
- **Our assessment**: Corroborates the Opus 5.5 note's warning (Claim 13 there) that reasoning-reproduction requests can be flagged. Use summarized thinking instead.

### Claim 14: Minimum cacheable prompt drops to 512 tokens; changing top-level effort invalidates the cache; per-message effort (beta) preserves it
- **Evidence**: Model details table and tuning section.
- **Confidence**: settled
- **Quote**: "Changing the top-level effort between requests invalidates the cache; to run one turn at a different level, use per-message effort (beta), which keeps the cache."
- **Our assessment**: The effort/cache interaction is a non-obvious cost trap for harnesses that vary effort per turn. Cache read is a tenth of input price.

### Claim 15: Refusals are HTTP 200 with `stop_reason: "refusal"`; five `stop_details` categories; fallback retries only two
- **Evidence**: API description.
- **Confidence**: settled
- **Quote**: "A declined request returns HTTP 200 with stop_reason: \"refusal\", and stop_details names one of five categories: cyber, bio, frontier_llm, reasoning_extraction or general_harms."
- **Our assessment**: Harnesses that only check HTTP status will miss refusals. Server-side fallback (`fallbacks: "default"`, beta) retries only `cyber` and `frontier_llm` "on Sonnet 5"; the other three need own handling.

### Claim 16: Use Sonnet 5.5 for well-scoped tasks with a clear spec and a way to check; Opus 5.5 for long-horizon work
- **Evidence**: Routing table; Epic Games testimonial (Daniel Vogel, COO).
- **Confidence**: anecdotal (testimonial) / emerging (routing)
- **Quote**: "Sonnet 5.5 fits best when the task has a clear spec and a way to check the result."
- **Our assessment**: Sensible heuristic; the Epic testimonial is marketing. Also high effort can erode Sonnet's cost/speed advantage ("consider Opus 5.5").

### Claim 17: In Claude Code, `sonnet` alias resolves to Sonnet 5.5 at medium effort, thinking cannot be turned off, no fast mode, default model stays Opus 5.5
- **Evidence**: Availability section.
- **Confidence**: settled (product fact at post date)
- **Quote**: "You can't turn thinking off for Sonnet 5.5 in Claude Code, and effort sets how much the model thinks."
- **Our assessment**: Version-specific (Claude Code v2.1.284+); will age.

## Concrete Artifacts

```
Pricing per million tokens (source: pricing table)
                      Sonnet 5.5   Opus 5.5
Input                 $2           $4
Output                $10          $20
Cache write, 5 min    $2.50        $5
Cache write, 1 hour   $4           $8
Cache read            $0.20        $0.20
US-only inference (inference_geo: "us"): 1.1x
```

```python
# Source: migration step 1 ("After: Claude Sonnet 5.5")
client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=16000,
    thinking={"type": "between_tools"},
    output_config={"effort": "high"},
    messages=[{"role": "user", "content": "..."}],
)
```

```python
# Source: migration step 2
tool_choice={"type": "auto"},  # was {"type": "tool", "name": "get_weather"}
# tool: "strict": True, input_schema includes "additionalProperties": False
```

```
# Source: "Ask for real checks at low effort" (system-prompt paragraph)
When you change code that can be run, built, or type-checked, run a real
check that exercises the change before reporting it done: the project's
tests, type-checker, or build, or the changed command itself. A syntax-only
check, or a check command that failed to start, does not count; if all
that is missing is the project's declared dependencies, install them with
its own package manager and lockfile (e.g. npm install, pip
install -r requirements.txt), never via sudo or the system package manager,
unless told not to. Only if no real check can run here, say which one you
did not run and why instead of reporting the change as done.
```

```
Model details (source table): id claude-sonnet-5-5 (Bedrock anthropic.claude-sonnet-5-5);
1M context, no beta header; max output 128k (300k on Batches with output-300k-2026-03-24);
knowledge cutoff June 2026; efforts low|medium|high|xhigh|max; default high (API) / medium (Claude Code);
min cacheable prompt 512 tokens (1,024 on Sonnet 5); separate rate limits from Sonnet 5.
High-res image tier up to 2576 px; a 2000x1500 image costs ~2.5x the tokens vs Sonnet 4.6/4.5/Haiku 4.5.
```

## Cross-References

- **Corroborates**: `blog-simonwillison-claude-sonnet-55.md` Claim 1 (30% faster / up to 30% less, same list price); `docs-github-copilot-sonnet55-availability.md` Claim 2 (fewer steps/tokens/tool calls) and Claim 1 (well-scoped everyday positioning); `blog-claude-dev-osmani-getting-the-most-out-of-opus-55.md` Claim 2 (drop "think" lines because the model always thinks) and Claim 13 (reasoning-reproduction requests can be flagged).
- **Contradicts**: None found. Note a tension for future review: Willison's "max" failure (`blog-simonwillison-claude-sonnet-55.md` Claim 3) is consistent with this post's advice to use xhigh/max only where evals show a gain; no contradiction issue filed.
- **Extends**: `blog-simonwillison-claude-sonnet-55.md` (that note says it does not cover pricing, context or API changes; this supplies them); `blog-claude-dev-thariq-spending-your-effort.md` (effort guidance, here applied to Sonnet 5.5 and the effort/cache interaction). `blog-simonwillison-llm-anthropic-028.md` contains no `between_tools` or `computer_toolset` mentions (grep returned nothing), so no conflict found despite the triage hint.
- **Novel**: Exact 400-error migration changes (`thinking: disabled`, forced `tool_choice`, `computer_20251124`); `between_tools` limits; refusal `stop_reason` and five `stop_details` categories; encrypted advisor results; empty-by-default progress thinking blocks; effort change invalidating the cache; 512-token cache minimum; the "real check" prompt paragraph.

## Guide Impact

- **Chapter 02 (harness / tool definitions)**: Add that forced `tool_choice` (`any`/`tool`) returns 400 on Sonnet 5.5, with `auto` + `strict: true` + `additionalProperties: false` as the pattern (Claim 4); note thinking can't be disabled, only `between_tools` at low/medium/high (Claim 3); computer-use toolset migration (Claim 6). Handle `stop_reason: "refusal"` as a 200 response (Claim 15) and read content blocks by type.
- **Chapter 03 (verification)**: Add the low-effort "run a real check" paragraph as a concrete prompt, citing Claim 12.
- **Chapter 04 (context / cost)**: Document that changing effort invalidates the prompt cache and per-message effort preserves it (Claim 14), the 512-token cache minimum, and thinking blocks being model-bound so keep conversations append-only (Claim 5). Cost: describe "up to 30% cheaper" as vendor-reported (Claim 1).
- **Chapter 00/01 (model choice)**: Sonnet 5.5 for specified, checkable work; Opus 5.5 for long-horizon (Claim 16), flagged as vendor guidance.

## Extraction Notes

- Fetched the page HTML and read the full text (all sections through Availability). Did not follow the linked migration or prompting guides.
- WebFetch's summarizer would not reproduce text verbatim, so quotes were taken from the raw HTML text. Inline-code formatting in the HTML is flattened in quotes; escaped inner quotes reflect the source's own double quotes.
- The `thinking: disabled` 400 behavior in Claim 3 is stated in the source ("returns a 400 error") and described in Our assessment rather than quoted, because inline code flattens awkwardly.
- Vendor performance claims and the Epic testimonial are unverified.
