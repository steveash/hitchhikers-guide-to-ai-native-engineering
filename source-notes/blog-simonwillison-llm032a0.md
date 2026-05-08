---
source_url: https://simonwillison.net/2026/Apr/29/llm/
source_type: blog-post
title: "LLM 0.32a0 is a major backwards-compatible refactor"
author: Simon Willison
date_published: 2026-04-29
date_extracted: 2026-05-08
last_checked: 2026-05-08
status: current
confidence_overall: emerging
issue: "#559"
---

# LLM 0.32a0 is a major backwards-compatible refactor

> Simon Willison's `llm` Python library replaces its text-in/text-out abstraction with a messages-based input API and typed streaming output parts — a foundational shift driven by modern LLMs returning mixed content (reasoning tokens, tool calls, images, audio) that the original single-string abstraction could not represent.

## Source Context

- **Type**: blog-post (first-party release announcement; ~1,200 words; includes full code examples for both sync and async usage and a sample tool-calling output transcript)
- **Author credibility**: Simon Willison is the creator of the `llm` Python library and CLI tool. This is first-party release documentation — architectural decisions are described directly by the person who made them. No vendor affiliation with OpenAI or Anthropic; the library is independently maintained and supports models from multiple providers.
- **Scope**: Covers two specific architectural changes in `llm` 0.32a0 (alpha): (1) prompts modeled as message sequences rather than single text, and (2) responses streamed as typed parts rather than undifferentiated text chunks. Also covers response serialization, a new `-R/--no-reasoning` CLI flag, and a future plan for graph-based SQLite conversation logging. Does NOT cover breaking changes to the plugin API (described as backwards-compatible), migration guides for existing plugin authors, or performance benchmarks.

## Extracted Claims

### Claim 1: The original `llm` text-in/text-out abstraction could no longer represent the full range of inputs and outputs required by modern LLMs

- **Evidence**: Author's direct statement, with enumeration of the capabilities that pushed beyond the original model: image/audio/video attachments, structured JSON schema outputs, tool execution, reasoning tokens, image/audio in responses.
- **Confidence**: settled (first-party; the enumerated capabilities are verifiable features of the current library)
- **Quote**: "The original abstraction—of text input that returns text output—was no longer able to represent everything I needed it to."
- **Our assessment**: This is a design-honesty statement worth preserving for the guide: even well-designed abstractions require periodic redesign as the underlying technology evolves. The `llm` library started in April 2023; by April 2026, frontier LLMs had grown tool use, reasoning tokens, and multi-modal output — none of which mapped cleanly onto the original string I/O contract. The pattern generalizes: harness engineers should plan for their core abstractions to be insufficient as model capabilities expand.

### Claim 2: The growth of `llm` library features was incremental and additive, exposing the underlying abstraction mismatch

- **Evidence**: Author's own retrospective enumeration of added features prior to 0.32.
- **Confidence**: settled (features are verifiable in the library's changelog)
- **Quote**: "Over time LLM itself has grown attachments to handle image, audio, and video input, then schemas for outputting structured JSON, then tools for executing tool calls. Meanwhile LLMs kept evolving, adding reasoning support and the ability to return images and all kinds of other interesting capabilities."
- **Our assessment**: This is the classic pattern of feature accretion on a mismatched abstraction: each new capability was bolted on rather than redesigned into. The 0.32 refactor is the consequence of that debt becoming untenable. For harness engineers, this is a cautionary pattern — extending a wrong abstraction works until it doesn't, and the cost of the eventual refactor scales with how many plugins/integrations depend on the old interface.

### Claim 3: LLM 0.32a0 introduces two architectural changes: message-sequence input and typed streaming output parts

- **Evidence**: Author's own summary statement of the 0.32a0 changes.
- **Confidence**: settled (alpha release; released for public testing by plugin authors)
- **Quote**: "The 0.32a0 alpha has two key changes: model inputs can be represented as a sequence of messages, and model responses can be composed of a stream of differently typed parts."
- **Our assessment**: The two changes are paired: the input side (messages array) aligns with how major provider APIs accept conversation history; the output side (typed stream parts) aligns with how modern LLMs actually emit content. Both changes move the `llm` abstraction closer to the provider API contracts, which reduces the impedance mismatch practitioners face when building plugins or adapters.

### Claim 4: The prior `conversation` API could not replay an existing conversation from the start, making it difficult to build API emulation layers

- **Evidence**: Author explains the concrete limitation: the old model built conversations interactively (turn by turn) but had no way to accept a pre-existing conversation history as input.
- **Confidence**: settled (first-party design explanation; the limitation is an architectural fact about the prior API)
- **Quote**: "it didn't provide a way to feed in a previous conversation from the start. This made tasks like building an emulation of the OpenAI chat completions API much harder than they should have been."
- **Our assessment**: This is an important concrete consequence: if you wanted to build something like an OpenAI-compatible endpoint on top of `llm`, you couldn't inject a pre-existing `messages` array because the library had no concept of replaying history. The 0.32 messages API directly addresses this. For practitioners wrapping `llm` in a server that receives standard OpenAI chat completion requests, this is the enabling change.

### Claim 5: The `llm` CLI's SQLite conversation persistence was a workaround that never became a stable Python API

- **Evidence**: Author's direct acknowledgment of the architectural debt in the CLI's prior persistence approach.
- **Confidence**: settled (first-party; author is describing their own design decision)
- **Quote**: "The llm CLI tool worked around this through a custom mechanism for persisting and inflating conversations using SQLite, but that never became a stable part of the LLM API—and there are many places you might want to use the Python library without committing to SQLite as the storage layer."
- **Our assessment**: This is a signal for harness engineers who built on the `llm` Python library's implicit SQLite coupling: that coupling was a CLI-specific workaround, not a supported design choice. The 0.32 serialization API (`response.to_dict()` / `Response.from_dict()`) makes the storage layer explicit and swappable. For practitioners who want to use `llm` as a library component without a SQLite dependency, this is the blocker being removed.

### Claim 6: Backwards compatibility is preserved: the old `prompt=` string argument is upgraded to a single-item messages array internally

- **Evidence**: Author's explicit statement about backwards compatibility in the release.
- **Confidence**: settled (first-party; the alpha is described as backwards-compatible throughout the post; title includes "backwards-compatible")
- **Quote**: "The previous prompt= option still works, but LLM upgrades it to a single-item messages array behind the scenes."
- **Our assessment**: This is significant for plugin authors: existing plugins that pass a string `prompt=` do not break. The library translates it. The backwards-compatible design is a practical necessity for an ecosystem with a large plugin surface — breaking changes would require simultaneous updates to all plugins, which the author explicitly wanted to avoid by shipping as an alpha for testing first.

### Claim 7: Modern LLMs return mixed-type streaming content that the old undifferentiated chunk model could not represent

- **Evidence**: Author's observation about current model behavior with a concrete Claude example.
- **Confidence**: emerging (specific to current frontier model behavior; accurate as of April 2026 based on Anthropic documentation and observed model outputs)
- **Quote**: "A prompt run against Claude might return reasoning output, then text, then a JSON request for a tool call, then more text content."
- **Our assessment**: This is the motivation for typed streaming parts. The observation is accurate for Claude with extended thinking enabled, and increasingly relevant as more models add tool use and reasoning. For practitioners building streaming UIs or harnesses, this makes the case for handling response streams as typed event sequences rather than raw text chunks — the content type changes mid-stream.

### Claim 8: Some models execute tools server-side, producing tool call outputs embedded in the response stream

- **Evidence**: Author cites specific examples of server-side tool execution from major providers.
- **Confidence**: emerging (specific models cited are real; server-side tool execution is a current feature of these providers)
- **Quote**: "Some models can even execute tools on the server-side, for example OpenAI's code interpreter tool or Anthropic's web search. This means the results from the model can combine text, tool calls, tool outputs and other formats."
- **Our assessment**: Server-side tool execution is the case where the model, not the caller, runs the tool — the caller's harness receives tool call outputs as part of the response stream without having invoked any tool itself. This is architecturally distinct from client-side tool execution (where the harness receives a tool call request, runs the function, and sends the result back). Both patterns require typed streaming parts to handle correctly.

### Claim 9: Multi-modal output (images, audio) is emerging in response streams alongside text and tool calls

- **Evidence**: Author's observation about multi-modal models.
- **Confidence**: anecdotal (described as "starting to emerge" — not yet a widespread pattern in the source's timeframe)
- **Quote**: "Multi-modal output models are starting to emerge too, which can return images or even snippets of audio intermixed into that streaming response."
- **Our assessment**: As of April 2026, most frontier models produce primarily text and tool call outputs; image/audio output remains limited to a few specific models. The author is signaling forward-looking necessity rather than current widespread need. For the guide, this is "horizon" context: the typed parts abstraction is designed to accommodate these output types when they arrive, rather than requiring another architectural refactor.

### Claim 10: The new `stream_events()` and `astream_events()` APIs expose typed event objects with `event.type` and `event.chunk` fields for fine-grained control over mixed-content streaming

- **Evidence**: Working code examples in the post, with sample output showing both text and tool call events interleaved.
- **Confidence**: emerging (alpha API; specific field names may change before stable 0.32 release)
- **Quote**: "The new LLM alpha models these as a stream of typed message parts."
- **Our assessment**: The alpha status means the specific event field names (`event.type`, `event.chunk`) and type strings (`"text"`, `"tool_call_name"`, `"tool_call_args"`) may change before stable release. Practitioners should not build production systems on this API until the stable 0.32 is released. The design pattern — a typed event stream with discriminated union via `event.type` — is itself architecturally stable even if the field names shift.

### Claim 11: The new streaming architecture enables CLI reasoning token display in a separate color, routed to stderr to avoid polluting piped output

- **Evidence**: Author's description of the concrete CLI improvement enabled by typed streaming parts.
- **Confidence**: settled (the CLI behavior is a direct consequence of having separate event types for reasoning vs text output; the stderr routing is standard Unix convention)
- **Quote**: "This new mechanism for streaming different token types means the CLI tool can now display "thinking" text in a different color from the text in the final response. The thinking text goes to stderr so it won't affect results that are piped into other tools."
- **Our assessment**: The stderr routing is a practitioner-relevant decision: if you pipe `llm` output to another tool (`llm -m claude-sonnet-4.6 '...' | grep foo`), you want reasoning tokens to not pollute the grep input. Sending reasoning to stderr is the correct Unix pattern. This also demonstrates a concrete benefit of the typed parts architecture at the CLI layer — UX improvements that were impossible with undifferentiated text chunks.

### Claim 12: A new `-R/--no-reasoning` CLI flag suppresses reasoning token output entirely

- **Evidence**: Author's statement in the release post, described as "the only CLI-facing change in this release."
- **Confidence**: settled (first-party release note; flag is described as the sole CLI change)
- **Quote**: "You can suppress the output of reasoning tokens using the new -R/--no-reasoning flag. Surprisingly that ended up being the only CLI-facing change in this release."
- **Our assessment**: The framing ("Surprisingly") indicates the author expected more surface-level CLI changes given the depth of the internal refactor. The fact that the architectural overhaul resulted in only one new flag for end users is itself evidence that the backwards-compatible design succeeded. For practitioners using `llm` in scripts that need deterministic output, `-R` provides a clean way to suppress the reasoning channel.

### Claim 13: A new storage-agnostic serialization mechanism (`response.to_dict()` / `Response.from_dict()`) lets Python API users persist responses outside SQLite

- **Evidence**: Author's description of the new API with code example. References `llm/serialization.py` as the implementation module.
- **Confidence**: emerging (alpha API; the interface is presented as intentionally simple and likely to be stable)
- **Quote**: "I've added a new mechanism in 0.32a0 that should provide Python API users a way to roll their own alternative"
- **Our assessment**: The key design decision here is the return type — "a JSON-style dictionary" via a `TypedDict` defined in `llm/serialization.py`. This means the serialized form is a plain Python dict serializable to any storage backend (JSON file, Redis, PostgreSQL, DynamoDB) without SQLite dependency. Combined with `Response.from_dict()` for inflation, this is the API that unlocks `llm` as a component in larger systems where SQLite is the wrong storage layer.

### Claim 14: Willison plans to redesign `llm`'s SQLite conversation logging as a graph to handle conversation branching without record duplication

- **Evidence**: Author's explicit statement of design intent for the next release.
- **Confidence**: anecdotal (stated intent, not a released feature; "undecided as to whether that should be a feature in 0.32 or I should hold it for 0.33")
- **Quote**: "Ideally I'd like to model this as a graph, to best support situations like an OpenAI-style chat completions API where the same conversations are constantly extended and then repeated with every prompt. I want to be able to store those without duplicating them in the database."
- **Our assessment**: The specific problem being solved: OpenAI-style chat completions replays the full message history with every request, so naively logging each request stores the same prior messages repeatedly. A graph model (where each message node points to its predecessors) avoids this duplication. This is a non-trivial schema design problem — the guide may want to call out the storage deduplication challenge as something practitioners building their own conversation logs will need to handle, regardless of whether `llm` solves it in 0.32 or 0.33.

## Concrete Artifacts

### New messages-based input API (from the post, verbatim)

```python
import llm
from llm import user, assistant

model = llm.get_model("gpt-5.5")

response = model.prompt(messages=[
    user("Capital of France?"),
    assistant("Paris"),
    user("Germany?"),
])
print(response.text())
```

*Source: Simon Willison, simonwillison.net/2026/Apr/29/llm/*

### Prior conversation API (from the post, verbatim — replaced by messages API)

```python
model = llm.get_model("gpt-5.5")

conversation = model.conversation()
r1 = conversation.prompt("Capital of France?")
print(r1.text())
# Outputs "Paris"

r2 = conversation.prompt("Germany?")
print(r2.text())
# Outputs "Berlin"
```

*Source: Simon Willison, simonwillison.net/2026/Apr/29/llm/ — this is the OLD API; shown for contrast*

### `response.reply()` for multi-turn continuation without a conversation object (from the post, verbatim)

```python
response2 = response.reply("How about Hungary?")
print(response2) # Default __str__() calls .text()
```

*Source: Simon Willison, simonwillison.net/2026/Apr/29/llm/*

### Typed streaming parts API — sync and async variants (from the post, verbatim)

```python
import asyncio
import llm

model = llm.get_model("gpt-5.5")
prompt = "invent 3 cool dogs, first talk about your motivations"

def describe_dog(name: str, bio: str) -> str:
    """Record the name and biography of a hypothetical dog."""
    return f"{name}: {bio}"

def sync_example():
    response = model.prompt(
        prompt,
        tools=[describe_dog],
    )
    for event in response.stream_events():
        if event.type == "text":
            print(event.chunk, end="", flush=True)
        elif event.type == "tool_call_name":
            print(f"\nTool call: {event.chunk}(", end="", flush=True)
        elif event.type == "tool_call_args":
            print(event.chunk, end="", flush=True)

async def async_example():
    model = llm.get_async_model("gpt-5.5")
    response = model.prompt(
        prompt,
        tools=[describe_dog],
    )
    async for event in response.astream_events():
        if event.type == "text":
            print(event.chunk, end="", flush=True)
        elif event.type == "tool_call_name":
            print(f"\nTool call: {event.chunk}(", end="", flush=True)
        elif event.type == "tool_call_args":
            print(event.chunk, end="", flush=True)

sync_example()
asyncio.run(async_example())
```

*Source: Simon Willison, simonwillison.net/2026/Apr/29/llm/*

### Sample output from tool-calling stream (from the post, verbatim)

```
My motivation: create three memorable dogs with distinct "cool" styles—one cinematic, one adventurous, and one charmingly chaotic—so each feels like they could star in their own story.

Tool call: describe_dog({"name": "Nova Jetpaw", "bio": "A sleek silver-gray whippet who wears tiny aviator goggles and loves sprinting along moonlit beaches. Nova is fearless, elegant, and rumored to outrun drones just for fun."}

Tool call: describe_dog({"name": "Mochi Thunderbark", "bio": "A fluffy corgi with a dramatic black-and-gold bandana and the confidence of a rock star. Mochi is short, loud, loyal, and leads a neighborhood 'security patrol' made entirely of squirrels."}

Tool call: describe_dog({"name": "Atlas Snowfang", "bio": "A massive white husky with ice-blue eyes and a backpack full of trail snacks. Atlas is calm, heroic, and always knows the way home—even during blizzards, fog, or confusing camping trips."}
```

*Source: Simon Willison, simonwillison.net/2026/Apr/29/llm/ — output from the sync_example() call above*

### Tool call execution and reply (from the post, verbatim)

```python
# Run tool functions and send results back to the model:
print(response.reply("Tell me about the dogs"))
```

*Source: Simon Willison, simonwillison.net/2026/Apr/29/llm/ — `response.execute_tool_calls()` also available to run tools without a model reply*

### Response serialization API (from the post, verbatim)

```python
serializable = response.to_dict()
# serializable is a JSON-style dictionary
# store it anywhere you like, then inflate it:
response = Response.from_dict(serializable)
```

*Source: Simon Willison, simonwillison.net/2026/Apr/29/llm/ — return type is a TypedDict from llm/serialization.py*

### CLI reasoning token display (from the post, verbatim)

```bash
llm -m claude-sonnet-4.6 'Think about 3 cool dogs then describe them' \
  -o thinking_display 1
```

*Source: Simon Willison, simonwillison.net/2026/Apr/29/llm/ — requires updated llm-anthropic plugin with streaming event support*

```bash
# Suppress reasoning tokens entirely:
llm -m claude-sonnet-4.6 -R 'Think about 3 cool dogs then describe them'
```

*Source: Simon Willison, simonwillison.net/2026/Apr/29/llm/ — -R / --no-reasoning flag, described as the only new CLI-facing flag in 0.32a0*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-llm031.md` Claim 4 (custom models in `extra-openai-models.yaml` now also registered as asynchronous): The async support added in 0.31 is consistent with the 0.32 async streaming API (`astream_events()`) — both are part of a pattern of expanding async coverage in the `llm` library. The 0.32 async example (`llm.get_async_model()` + `async for event in response.astream_events()`) builds on the same async infrastructure.
  - `blog-simonwillison-gpt55-codex-plugin.md` Claim 6 (the `-o reasoning_effort` flag as the CLI primitive for reasoning control on capable models): LLM 0.32a0 adds complementary reasoning output control at the display layer — `-o thinking_display 1` to show reasoning tokens in color, and `-R/--no-reasoning` to suppress them. These are display-layer controls that pair with the inference-layer `-o reasoning_effort` flag documented in the Codex plugin note.

- **Contradicts**: None identified. No existing corpus note makes claims about `llm` library input or output modeling that conflict with this source's architectural description.

- **Extends**:
  - `blog-simonwillison-llm031.md`: The 0.31 release (four incremental feature bullets, flagged as priority:low by the Prospector) is the direct predecessor. The 0.32a0 note is the architectural refactor that the 0.31 incremental releases were building toward. Together they document the `llm` library's evolution from a simple CLI wrapper to a multi-modal, multi-turn, tool-aware abstraction layer.
  - `blog-simonwillison-glm51.md` Claim 6 (the `llm` CLI + OpenRouter as a consistent interface for model testing): The 0.32 messages API and typed streaming parts make the unified interface more capable — where 0.25–0.31 could run model tests with single prompts, 0.32 can replay conversation histories and handle mixed-type responses. The same "consistent interface" pattern (one CLI, many models) is now extended to cover multi-turn and tool-calling workflows.
  - `blog-simonwillison-gpt55-codex-plugin.md` (the broader `llm` plugin ecosystem): The alpha release explicitly targets plugin authors as the first consumers — the Prospector noted that the author "will upgrade various plugins and exercise the new design in real world environments for a few days" before the stable 0.32. Plugin authors who need to implement the new messages and streaming parts interfaces are the primary audience for this post.

- **Novel**:
  - **First in-corpus documentation of a messages-based conversation replay API in the `llm` library**: Prior notes documented the `conversation()` object pattern; this is the first note documenting the messages-array alternative that supports replaying pre-existing history.
  - **First in-corpus description of typed streaming parts as an abstraction pattern for mixed-content LLM responses**: No prior note discusses how to handle a response stream that interleaves text, tool call names, tool call args, and reasoning tokens as distinct typed events.
  - **First in-corpus documentation of storage-agnostic response serialization in `llm`**: No prior note covers the `to_dict()` / `from_dict()` serialization contract.
  - **First in-corpus acknowledgment that SQLite coupling was an architectural limitation, not a design choice**: The author explicitly names the SQLite persistence as a CLI workaround that never became a stable API — framing it as debt, not a feature.
  - **Concrete pattern for routing reasoning tokens to stderr in CLI pipelines**: No prior note discusses how to handle reasoning token output in Unix pipes (`llm output | other-tool`); the stderr routing is a new practitioner-relevant pattern.

## Guide Impact

- **Chapter 02 (Harness Engineering — Abstraction design)**: The 0.32a0 refactor is a case study in when a core abstraction becomes insufficient and how to replace it without breaking downstream consumers. The guide could use this as a concrete example of: (1) feature-accretion forcing abstraction redesign; (2) backwards-compatible migration paths (old `prompt=` string automatically upgraded); (3) alpha-based plugin ecosystem migration strategy. Currently the guide may not have a worked example of abstraction evolution — this post provides one.

- **Chapter 02 (Harness Engineering — Streaming typed output handling)**: If the guide covers streaming response handling, it should add a note that modern LLMs produce mixed-content streams (text + tool calls + reasoning tokens) and that harnesses should handle these as typed event sequences, not raw text chunks. The `stream_events()` pattern in 0.32a0 is the reference implementation. No existing guide content on typed streaming is apparent from corpus coverage.

- **Chapter 03 (Using LLM APIs — Conversation history as messages arrays)**: The messages-based input pattern (user/assistant alternating turns as an array) is the standard API contract for all major providers (as noted in the post's OpenAI chat completions example). If the guide covers conversation management, it should document the messages-array pattern as the canonical approach, noting that it enables conversation history replay that stateful conversation objects do not. The prior conversation-object approach should be flagged as a weaker abstraction for multi-turn applications.

- **Chapter 05 (Orchestration / Scalable Systems — Storage-agnostic conversation persistence)**: The serialization API (`to_dict()` / `from_dict()`) and the future graph-based logging design are relevant to practitioners building conversation management layers. The guide should note: (1) SQLite coupling is an antipattern for library-level conversation storage; (2) conversation graphs are the right data model when conversations are extended and replayed (OpenAI chat completions pattern); (3) storing full message history with each request creates storage duplication at scale.

- **Chapter 01 (Daily Workflows — `llm` CLI reasoning token handling)**: If the guide covers `llm` CLI usage, add: the `-R/--no-reasoning` flag suppresses reasoning token output; `-o thinking_display 1` shows reasoning in a separate color via stderr (useful for interactive use, but does not pollute piped output). These pair with the existing `-o reasoning_effort` coverage from `blog-simonwillison-gpt55-codex-plugin.md`.

## Extraction Notes

- **Full verbatim text obtained via curl**: WebFetch returned a summarized/compressed version; the full post was fetched using `curl -s <url>` with an HTML-stripping Python pipeline. All code blocks and quotes in this note are copied character-for-character from the curl output, not from the WebFetch summary.
- **Alpha release caveat**: 0.32a0 is explicitly alpha. The author states "I expect the stable 0.32 release will be very similar to this alpha, unless alpha testing reveals some design flaw." API field names (e.g., `event.type`, `event.chunk`) are emerging confidence; the architectural patterns are settled.
- **No sub-pages followed**: The post does not link to sub-pages with substantive content. GitHub issue links (#1395, #1418 from the 0.31 post) are implementation tickets, not usage documentation. The llm-anthropic plugin page was not followed as it is a dependent ecosystem artifact, not an upstream source.
- **Cross-reference verification performed**: `blog-simonwillison-llm031.md` Claim 4 confirmed at lines 47-52 (async registration for custom models). `blog-simonwillison-gpt55-codex-plugin.md` Claim 6 confirmed at lines 63-66 (`-o reasoning_effort xhigh` as CLI primitive). `blog-simonwillison-glm51.md` Claim 6 confirmed at lines 56-60 (`llm` CLI + OpenRouter unified interface). All claim numbers verified by document-order count.
- **Fragment URL**: The issue body includes `#atom-everything` (Atom feed anchor). `source_url` uses the canonical page URL without the fragment, consistent with prior Willison source notes in this corpus.
