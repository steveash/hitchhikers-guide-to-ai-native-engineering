---
source_url: https://simonwillison.net/2026/Aug/4/new-release-of-llm/
source_type: blog-post
title: "New release of LLM adds support for reasoning traces, OpenAI Responses, server-side tools, and smarter logging"
author: Simon Willison
date_published: 2026-08-04
date_extracted: 2026-08-11
last_checked: 2026-08-11
status: current
confidence_overall: settled
issue: "#2617"
---

# New release of LLM adds support for reasoning traces, OpenAI Responses, server-side tools, and smarter logging

> The stable release of `llm` 0.32 ships the architectural foundation previewed in the 0.32a0 alpha (messages input, typed streaming parts) as concrete, practitioner-usable features — server-side provider tools (OpenAI CodeInterpreter/WebSearch, Anthropic WebSearch/WebFetch/CodeExecution/AnthropicMCP), a Git-modeled content-addressable SQLite message store, an OpenAI-compatible server plugin, and core-library primitives (`llm.PauseChain`, `tool_call_id`) for pausable, resumable tool loops — while the author explicitly adopts "agent framework" as a description of what LLM has become.

## Source Context

- **Type**: blog-post (first-party stable release announcement; ~900 words with inline code examples, published as a full blog post at `simonwillison.net/2026/Aug/4/new-release-of-llm/`, linked from a short "beat" entry at `simonwillison.net/2026/Aug/4/llm/` which is the URL originally filed in this issue). The beat entry itself contains no substantive content beyond a link to this post and to the GitHub release; both were fetched and used as primary sources for this note.
- **Author credibility**: Simon Willison is the creator and maintainer of the `llm` Python library/CLI, the `llm-anthropic` plugin, and Datasette/Datasette Agent. This is first-party release documentation from the person who designed and shipped the features described. No vendor affiliation with OpenAI or Anthropic.
- **Scope**: Covers the stable `llm` 0.32 release (reasoning trace display, GPT-5.6 model family, server-side tools, `llm openai endpoint`, the `messages=` Python parameter, `stream_events()`, the `llm-chat-completions-server` plugin, the content-addressable message store) and the companion `llm-anthropic` 0.26 release (Claude 5 models, server-side tools, reasoning-option simplification). Does NOT cover: the full GitHub release notes for every intermediate alpha/rc (0.32a2, 0.32a3, 0.32rc1, 0.32rc2 — referenced but not individually followed as sub-pages), performance benchmarks, or plugin author migration mechanics beyond a single link to the "Structured messages and streaming events" plugin guide.

## Extracted Claims

### Claim 1: The author characterizes LLM 0.32 as the most significant release since the project's initial launch, driven by five converging feature areas
- **Evidence**: Author's direct framing statement opening the post, immediately followed by an enumeration of what the release includes.
- **Confidence**: settled (first-party characterization of the author's own release; the enumerated features are independently verifiable in the GitHub release notes)
- **Quote**: "I released LLM 0.32 this morning, the most significant new version of LLM since the initial launch of the project. The new version includes support for visible reasoning traces, server-side provider tools, redesigned content-addressable SQLite logs, new models, and new features enabled by the OpenAI Responses API."
- **Our assessment**: This framing statement is a useful index for the rest of the note — it names the five areas (reasoning traces, server-side tools, logging redesign, new models, Responses API features) that the rest of the post and the GitHub release notes elaborate on. Coming from the tool's creator rather than a third party, "most significant since launch" is a credible claim about scope, not necessarily about difficulty of adoption — the post repeatedly stresses backwards compatibility (see Claim 13).

### Claim 2: Reasoning traces from reasoning-capable models are now streamed to standard error by default, suppressible with a renamed `-R/--hide-reasoning` flag
- **Evidence**: Direct statement in the "Headline features for LLM CLI users" section, plus confirmation in the GitHub release notes ("Visible reasoning summaries are streamed to standard error by `llm prompt` and `llm chat`. Use `-R/--hide-reasoning` or the new `hide_reasoning=True` Python argument to hide them.").
- **Confidence**: settled (first-party; behavior is a shipped stable-release default)
- **Quote**: "Running LLM against reasoning models now displays their reasoning traces to standard error, so you can see what they are “thinking” without that information being included in the standard output that you might pipe to another tool. Add -R/--hide-reasoning to turn this off."
- **Our assessment**: This is a naming change worth flagging for the guide, not a contradiction: `blog-simonwillison-llm032a0.md` Claim 12 documented the 0.32a0 alpha flag as `-R/--no-reasoning`, described there as "the only CLI-facing change" in that alpha. The stable release renames the long-form flag to `--hide-reasoning` (short form `-R` unchanged) and flips the default from opt-in display to display-by-default-with-opt-out — the alpha's framing ("suppress reasoning tokens") and the stable framing ("displays by default, hide with -R") describe the same short flag but different default behavior. Practitioners who scripted around the alpha's `-R/--no-reasoning` long-form name need to update to `--hide-reasoning`.

### Claim 3: LLM 0.32 adds built-in support for the GPT-5.6 model family, with GPT-5.6 Luna replacing GPT-4o mini as the CLI's default model
- **Evidence**: Direct statement in the post; corroborated by the GitHub release notes, which name three new built-in models (`gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`) and state that models no longer available from OpenAI have been removed.
- **Confidence**: settled (first-party; verifiable against the GitHub release notes)
- **Quote**: "LLM includes support out-of-the-box for the GPT-5.6 model family, and the new default model used with llm \"prompt\" is now the inexpensive but capable GPT-5.6 Luna."
- **Our assessment**: This continues the pattern documented in `blog-simonwillison-llm031.md` Claim 1 (native `gpt-5.5` support arriving in 0.31, closing the Codex-workaround access path) — `llm` keeps tracking OpenAI's frontier releases as built-in models within one to two point releases. The default-model swap (GPT-4o mini → GPT-5.6 Luna) changes behavior for any script or workflow that calls `llm "prompt"` without an explicit `-m` flag.

### Claim 4: LLM calls can now invoke provider-executed server-side tools, demonstrated with OpenAI's CodeInterpreter via a single CLI flag
- **Evidence**: Direct statement with a runnable CLI example.
- **Confidence**: settled (first-party; concrete command shown)
- **Quote**: "LLM calls can now use server-side tools from various providers. OpenAI provide a code execution environment as a server-side tool; LLM can now run prompts that benefit from that like so:"
- **Our assessment**: This is the practical payoff of the typed-parts architecture introduced in the 0.32a0 alpha (`blog-simonwillison-llm032a0.md` Claims 3 and 8): server-side tool execution requires representing tool calls and tool results as structured message parts, which the alpha's messages/parts redesign made possible. `-T CodeInterpreter` is now a one-flag way to give a prompt a real Python/SQLite execution environment without the caller running any code itself.

### Claim 5: The `llm-anthropic` plugin adds WebSearch, WebFetch, CodeExecution, and AnthropicMCP as server-side tools, demonstrated with a live example calling a specific MCP server through Claude
- **Evidence**: Direct statement with a runnable CLI example targeting a real deployed server (`https://datasette.simonwillison.net/-/mcp`).
- **Confidence**: settled (first-party; concrete, targetable command against a live service)
- **Quote**: "The llm-anthropic plugin adds WebSearch, WebFetch, CodeExecution, and AnthropicMCP, which looks like this: llm -m claude-sonnet-5 -T 'AnthropicMCP(\"https://datasette.simonwillison.net/-/mcp\")' 'how many rows in the blog_blogmark table?' \\ ... That causes Anthropic to execute MCP calls against my new datasette-mcp plugin as part of a single request/response interaction with their API."
- **Our assessment**: The MCP server targeted here (`datasette.simonwillison.net/-/mcp`) is the exact same deployment documented in `blog-simonwillison-stateless-mcp-tooling.md` Claim 8 — a Datasette plugin exposing three read-only tools (`list_databases()`, `get_database_schema()`, `execute_sql()`). That earlier note documented reaching this server via `llm-mcp-client`, a separate alpha plugin that runs MCP tool calls client-side from `llm`. `AnthropicMCP` is architecturally different: it is Anthropic's own server-side MCP connector, so the MCP round-trip happens inside Anthropic's infrastructure as part of one API call rather than as a client-side loop driven by `llm`. The same target server is now reachable through two distinct mechanisms in the `llm` ecosystem — client-side (`llm-mcp-client`) and provider-side (`AnthropicMCP`).

### Claim 6: The new `llm openai endpoint` command runs prompts against any OpenAI-compatible endpoint as a one-liner, without requiring prior configuration, and without logging the calls
- **Evidence**: Direct statement plus a runnable example against a local LM Studio server, combined with `uvx` (no LLM installation required) and a third-party tool plugin (`llm-tools-quickjs`).
- **Confidence**: settled (first-party; concrete `uvx` command shown)
- **Quote**: "The new llm openai endpoint command provides a tool for executing prompts against any OpenAI compatible endpoint as a one-liner. These aren’t logged, which makes this a handy tool for running one-off prompts against anything that speaks the lingua franca of the LLM API world."
- **Our assessment**: This is a zero-configuration escape hatch distinct from the `extra-openai-models.yaml` mechanism documented in `blog-simonwillison-llm031.md` Claim 4 (which requires editing a config file and produces persistently-registered, loggable models). `llm openai endpoint` trades persistence and logging for zero setup — useful for one-off probing of local model servers (LM Studio, vLLM, etc.) or of the very `llm-chat-completions-server` this release also introduces (Claim 9).

### Claim 7: A new `model.prompt(messages=[])` Python parameter lets callers pass a complete conversation history in one call, replacing the need to build it up turn-by-turn through a `conversation` object
- **Evidence**: Direct statement with a full runnable code example (`system(...)`, `user(...)`, `assistant(...)` message constructors).
- **Confidence**: settled (first-party; shipped in the stable release, not the alpha)
- **Quote**: "LLM's Python API previously required you to create a conversation and then send messages to it one at a time. This was an abstraction over the true nature of LLMs, where each request carries a complete history of the messages that came before it. That abstraction started to get in the way for some more advanced cases, so the new release introduces a model.prompt(messages=[]) parameter that can be used like this:"
- **Our assessment**: This is the `messages=` keyword argument first introduced as an alpha feature in `blog-simonwillison-llm032a0.md` (that note's Concrete Artifacts section shows an equivalent `model.prompt(messages=[...])` example from the April 2026 alpha) now confirmed shipping unchanged in the August 2026 stable release. It directly resolves the limitation `blog-simonwillison-llm032a0.md` Claim 4 identified in the old `conversation` API — "it didn't provide a way to feed in a previous conversation from the start" — which the alpha note flagged as the specific blocker for building OpenAI chat-completions-style API emulation layers. This release's `llm-chat-completions-server` plugin (Claim 9) is exactly that emulation layer, now built on top of the `messages=` API this claim documents.

### Claim 8: `response.stream_events()` yields a discriminated stream of typed events (reasoning, text, and others) that callers switch on by `event.type`, and this typed-event model is what makes robust OpenAI chat-completions emulation possible
- **Evidence**: Full runnable code example iterating `model.prompt("Explain cats").stream_events()` and branching on `event.type in {"reasoning", "text"}` with a fallback `else` branch for other event types; author's explicit statement connecting this to the chat-completions server.
- **Confidence**: settled (first-party; shown as working stable-release code, not alpha)
- **Quote**: "Combine these features and we can finally provide a robust implementation of the semi-standard OpenAI chat completions API, which I've now released as the llm-chat-completions-server plugin:"
- **Our assessment**: `blog-simonwillison-llm032a0.md` Claim 10 documented `stream_events()`/`astream_events()` as an alpha API with event types `"text"`, `"tool_call_name"`, and `"tool_call_args"`, flagging that "the specific event field names... may change before stable release." This post's example adds a `"reasoning"` branch to the same `event.type` pattern and confirms the design is stable enough to build a production-facing plugin (`llm-chat-completions-server`) on top of it — the alpha's uncertainty about field-name stability appears to have resolved without a breaking rename of the event-type discriminator itself (only the CLI reasoning-flag name changed, per Claim 2).

### Claim 9: The `llm-chat-completions-server` plugin wraps LLM as a locally-runnable, OpenAI-compatible Chat Completions endpoint, and it can itself be queried through the new `llm openai endpoint` command
- **Evidence**: Install/run commands plus a follow-up example querying the just-started server via `llm openai endpoint`.
- **Confidence**: settled (first-party; concrete install and invocation commands shown)
- **Quote**: "llm install llm-chat-completions-server\nllm chat-completions-server --port 9000\n# Server is now running on http://127.0.0.1:9000/v1"
- **Our assessment**: This closes a loop the author names explicitly in the post: LLM can now both emulate an OpenAI-compatible server (this plugin) and consume any OpenAI-compatible server (`llm openai endpoint`, Claim 6) — including its own. For practitioners standardizing internal tooling on the OpenAI Chat Completions request/response shape, this plugin turns any model `llm` can already access (including local models via other plugins) into a drop-in endpoint other OpenAI-SDK-based tools can call without modification.

### Claim 10: A new Git-modeled, content-addressed message store deduplicates repeated conversation history in LLM's SQLite logs, motivated specifically by API-emulation servers that resend the full growing message history on every turn
- **Evidence**: Author's direct statement of the problem and design choice in the post; the GitHub release notes describe the same mechanism in schema terms ("Messages are stored once and referenced by their content hash, preserving structured text, reasoning, attachments and tool activity without duplicating repeated conversation history.").
- **Confidence**: settled (first-party; shipped, documented schema, with backward-compatible reading of legacy logs confirmed in the GitHub release notes: "Existing records in the legacy responses table are left untouched, and llm logs combines both generations of data.")
- **Quote**: "The bigger challenge with that kind of API concerns logging. If we're going to support the pattern where the message sequence is appended to on every request, ideally we can avoid logging all of that duplicate JSON for every turn. The solution is the new content-addressable message store, modeled after Git."
- **Our assessment**: This is the concrete resolution of a design intent `blog-simonwillison-llm032a0.md` Claim 14 recorded as unsettled in April 2026 ("Ideally I'd like to model this as a graph... I want to be able to store those without duplicating them in the database... undecided as to whether that should be a feature in 0.32 or I should hold it for 0.33"). The stable 0.32 release resolves that open question: the author chose a Git-like content-addressed store (messages referenced by content hash) rather than a general graph structure, specifically to solve the OpenAI chat-completions replay-and-resend pattern. This is a directly citable answer to a question the alpha note flagged as open.

### Claim 11: Tool loops in LLM 0.32 are now individually addressable and pausable/resumable at the core-library level — every tool call has a unique `tool_call_id`, and tools can raise `llm.PauseChain` to suspend execution for human approval, later resuming from a stored message history without repeating already-resolved calls
- **Evidence**: GitHub release notes, "More controllable tool loops" section: "Every tool call now has a unique tool_call_id, synthesized when the provider does not supply one... Tools can raise llm.PauseChain to pause execution for human approval or another external event. Chains can later resume from a message history ending in unresolved tool calls, without repeating calls that already have results." Corroborated in the blog post itself: "Tool chains can now pause for human approval and resume from a stored message history—both needed by Datasette Agent."
- **Confidence**: settled (first-party; documented in both the release notes and the announcement post; explicitly tied to a real consuming application)
- **Quote**: "Tool chains can now pause for human approval and resume from a stored message history—both needed by Datasette Agent."
- **Our assessment**: This formalizes, at the core LLM library level, the same suspend/resume pattern `blog-simonwillison-datasette-agent-askuser.md` documented as an application-level feature in Datasette Agent's `ask_user()` mechanism (0.2a0, June 2026). That note's Claim 1 and Claim 4 describe a `ToolContext`-based `ask_user()` that suspends a tool call, persists the pending question, and re-executes the tool from the top with stored answers replayed on resume. This post states directly that "tool chains can now pause... and resume... both needed by Datasette Agent" — meaning the `llm.PauseChain` primitive documented here is very likely the core-library generalization that Datasette Agent's `ask_user()` was built on top of (or converged with). Practitioners building their own human-in-the-loop tool chains on `llm` now have a documented core-library primitive rather than needing to build custom suspend/resume logic as Datasette Agent originally did.

### Claim 12: The author explicitly adopts "agent framework" as a description of what LLM has become, citing his own September 2025 definition that "an LLM agent runs tools in a loop to achieve a goal," while stopping short of formally baking an "agent" concept into the library
- **Evidence**: A dedicated closing section of the post ("I guess LLM is an agent framework now"), explicitly tracing the terminology shift back to a specific prior post and explicitly naming Datasette Agent as the driver of the underlying tool-loop changes. The same section states the library does not yet formalize an "agent" concept: "Maybe the next version of LLM will bake the concept of an “agent” into the core library. I’m still trying to figure out what that would look like."
- **Confidence**: settled (both halves of the claim are direct, dated, first-party statements: the author's adoption of the term and his explicit statement that the library does not yet formalize an "agent" concept. How much this positioning shift matters in practice is a separate and less certain question — treated as interpretation in Our assessment rather than as part of the graded claim.)
- **Quote**: "When I started work on LLM, the term “agent” had such a vague definition that I refused to use it. In September 2025 I came around to the idea that \"An LLM agent runs tools in a loop to achieve a goal\" is well established enough now that I could stop avoiding the term entirely."
- **Our assessment**: This is a datable terminology milestone from a widely-read practitioner voice, useful for the guide's own definitional discussion of "agent." It is explicitly qualified, not a marketing claim: the author names the concrete driver (Datasette Agent's pause/resume needs), names the specific definition he's now comfortable using, and explicitly declines to claim LLM has become a formal agent framework in the architected sense — "Looking at LLM today it’s beginning to look very agent-shaped to me" is presented as an informal, retrospective observation, not a product positioning statement. How much the terminology shift matters in practice is the genuinely uncertain part here and should be treated as emerging: the label change is documented fact, but no "agent" abstraction exists in the library yet to build on. The Prospector's triage question ("is this positioning change significant or marketing framing?") is answered directly by the source: it is the author's own retrospective observation, explicitly hedged, not a marketing claim.

### Claim 13: Existing LLM plugins continue to work without modification, but plugins that provide extra models must be upgraded to 0.32 to participate in the new streaming-events system, and LLM now requires sqlite-utils 4.0+ while dropping its dependency on sqlite-migrate
- **Evidence**: Direct compatibility statement in the post; sqlite-utils/sqlite-migrate requirement confirmed in the GitHub release notes ("LLM now requires sqlite-utils 4.0 or higher and no longer depends on sqlite-migrate.").
- **Confidence**: settled (first-party; explicit compatibility statement plus a verifiable dependency-version requirement)
- **Quote**: "Existing LLM plugins should all continue to work, but plugins that provide extra models will need to be upgraded to 0.32 in order to participate fully in the new streaming events system."
- **Our assessment**: This is the release's explicit backwards-compatibility boundary: general-purpose plugins (tools, output formatters) are unaffected, but model-provider plugins (like `llm-anthropic`, `llm-gemini`, `llm-openrouter`, `llm-mistral`) need updating to expose the new typed-event streaming behavior. The post confirms `llm-anthropic` 0.26 is already updated (Claim 5's server-side tools depend on this); it states `llm-gemini`, `llm-openrouter`, and `llm-mistral` are "nearly there, releases coming soon" — meaning as of this release date, only Anthropic-model users get the full streaming-events experience out of the box.

## Concrete Artifacts

### CLI: OpenAI server-side CodeInterpreter tool
```
llm --tool CodeInterpreter 'Show current python and SQLite versions'
```
*Source: simonwillison.net/2026/Aug/4/new-release-of-llm/*

### CLI: Anthropic server-side AnthropicMCP tool against a live datasette-mcp server
```bash
llm -m claude-sonnet-5 -T 'AnthropicMCP("https://datasette.simonwillison.net/-/mcp")' \
'how many rows in the blog_blogmark table?'
```
*Source: simonwillison.net/2026/Aug/4/new-release-of-llm/ — targets the same datasette-mcp deployment documented in `blog-simonwillison-stateless-mcp-tooling.md` Claim 8.*

### CLI: `llm openai endpoint` against a local LM Studio server via uvx
```bash
uvx --with llm-tools-quickjs \
 llm openai endpoint http://localhost:1234/v1 -m google/gemma-4-12b \
 -T QuickJS 'Use QuickJS to multiply 3434 * 2434' --td
```
*Source: simonwillison.net/2026/Aug/4/new-release-of-llm/*

### Python: `messages=` parameter for full-history prompts
```python
import llm
from llm import user, assistant, system

model = llm.get_model("gpt-5.6-luna")
response = model.prompt(messages=[
    system("You are a helpful pirate."),
    user("What is the capital of France?"),
    assistant("Paris, matey."),
    user("And Germany?"),
])
print(response.text())
```
*Source: simonwillison.net/2026/Aug/4/new-release-of-llm/*

### Python: typed `stream_events()` loop with a reasoning branch
```python
for event in model.prompt("Explain cats").stream_events():
    if event.type == "reasoning":
        print(f"[thinking] {event.chunk}", end="", flush=True)
    elif event.type == "text":
        print(event.chunk, end="", flush=True)
    else:
        print(f"Other event: {event}")
```
*Source: simonwillison.net/2026/Aug/4/new-release-of-llm/*

### CLI: installing and running `llm-chat-completions-server`, then calling it via `llm openai endpoint`
```bash
llm install llm-chat-completions-server
llm chat-completions-server --port 9000
# Server is now running on http://127.0.0.1:9000/v1

llm openai endpoint http://127.0.0.1:9000/v1 'hello' -m gpt-5.4-mini
```
*Source: simonwillison.net/2026/Aug/4/new-release-of-llm/*

### GitHub release notes (verbatim excerpts, simonw/llm tag 0.32, published 2026-08-04T17:15:33Z)
```
LLM 0.32 is a major, backwards-compatible update to the way prompts,
responses, tools and logs are represented. It adds structured messages
and parts throughout the Python API, adopts the OpenAI Responses API
for reasoning-capable models, substantially expands control over
pausable and resumable tool loops and introduces a new content-addressed
SQLite logging schema.

### More controllable tool loops
- Every tool call now has a unique tool_call_id, synthesized when the
  provider does not supply one.
- Tools can raise llm.PauseChain to pause execution for human approval
  or another external event. Chains can later resume from a message
  history ending in unresolved tool calls, without repeating calls
  that already have results.
- Conversations that use configured tools can be continued with
  llm -c or llm chat -c without repeating the toolbox configuration.

### New SQLite logging schema
- Messages are stored once and referenced by their content hash,
  preserving structured text, reasoning, attachments and tool activity
  without duplicating repeated conversation history.
- LLM now requires sqlite-utils 4.0 or higher and no longer depends on
  sqlite-migrate.
```
*Source: GitHub API, github.com/simonw/llm/releases/tags/0.32*

### llm-anthropic 0.26 release notes (verbatim, github.com/simonw/llm-anthropic, published 2026-08-04T22:00:58Z)
```
- New models: claude-fable-5, claude-sonnet-5, and claude-opus-5. #75, #76
- Added server-side tools for WebSearch, WebFetch, CodeExecution, and
  AnthropicMCP, available through LLM's -T interface or Python tools=.
  The previous -o web_search* options have been removed in favor of
  -T WebSearch. #79
- Upgraded to llm>=0.32. Reasoning, tool calls, tool results, and
  server-side tool results now stream as typed events. Reasoning for
  llm CLI prompts now displays to standard error unless you pass
  --hide-reasoning/-R.
- Simplified extended thinking to thinking and thinking_effort (low,
  medium, high, xhigh, or max). Claude 5 models think by default;
  -o thinking 0 disables thinking for Sonnet 5 and Opus 5, while Fable 5
  always thinks. -R/--hide-reasoning now omits reasoning from responses
  and logs. The thinking_budget, thinking_display, and thinking_adaptive
  options have been removed. #80
```
*Source: GitHub API, github.com/simonw/llm-anthropic/releases/tags/0.26*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-llm032a0.md` Claim 3 (the 0.32a0 alpha's two key changes: messages-sequence input and typed streaming output parts) — this stable release confirms both shipped essentially unchanged, with Claim 7 (`messages=`) and Claim 8 (`stream_events()`) here matching that alpha's design.
  - `blog-simonwillison-llm032a0.md` Claim 10 (typed `event.type`/`event.chunk` streaming API, alpha status, field names possibly unstable) — Claim 8 here shows the same pattern in shipped stable code with an added `"reasoning"` branch, indicating the field-name uncertainty flagged in the alpha resolved without a breaking rename.
  - `blog-simonwillison-stateless-mcp-tooling.md` Claim 8 (datasette-mcp: three read-only tools, deployed at `datasette.simonwillison.net/-/mcp`) — Claim 5 here shows a second, provider-side mechanism (`AnthropicMCP`) reaching the identical deployed server that note documented being reached via the client-side `llm-mcp-client` plugin.
  - `blog-simonwillison-datasette-agent-askuser.md` Claims 1 and 4 (Datasette Agent's application-level `ask_user()` suspend/persist/re-execute-from-top pattern) — Claim 11 here documents LLM 0.32's core-library `llm.PauseChain`/resume mechanism, which the post states directly was needed by, and driven by, Datasette Agent.

- **Contradicts**: None identified as a genuine claim conflict. Note for the Assayer: the CLI flag long-form name changed between sources (`blog-simonwillison-llm032a0.md` Claim 12 documents `-R/--no-reasoning` in the 0.32a0 alpha; this stable release renames it to `-R/--hide-reasoning` per Claim 2 here). This is a version-to-version naming change during active alpha development, not a factual disagreement between two sources describing the same shipped state, so no contradiction issue was filed per MINER.md §4a's "conditioning variable" guidance (the two notes describe different points in time of the same feature's evolution).

- **Extends**:
  - `blog-simonwillison-llm032a0.md` overall — the architectural preview (alpha, April 2026) is now shipped stable (August 2026) with concrete server-side tool integrations, a Git-modeled content-addressable logging schema resolving that note's Claim 14 open design question, and a production-facing OpenAI-compatible server plugin built on the alpha's `messages=`/`stream_events()` APIs.
  - `blog-simonwillison-llm031.md` Claim 1 (native `gpt-5.5` support arriving in 0.31) — Claim 3 here extends the same frontier-model-tracking pattern to the GPT-5.6 family, with GPT-5.6 Luna replacing GPT-4o mini as the CLI default.
  - `blog-simonwillison-llm-anthropic-0251.md` Claim 1 (Opus 4.8 model support in llm-anthropic 0.25.1) — superseded by llm-anthropic 0.26's Claude 5 family (`claude-fable-5`, `claude-sonnet-5`, `claude-opus-5`), documented in this note's Concrete Artifacts.
  - `blog-simonwillison-llm-anthropic-0251.md` Claims 2/3 (the `-o fast 1` fast-mode flag and the max_tokens default change, both llm-anthropic 0.25.1-era `-o` options) — this release's llm-anthropic 0.26 removes and consolidates a different set of `-o` options (`thinking_budget`, `thinking_display`, `thinking_adaptive` → `thinking`/`thinking_effort`; `-o web_search*` → `-T WebSearch`), continuing the pattern of the plugin's option surface changing across releases as new model generations ship.

- **Novel**:
  - **First in-corpus documentation of a provider-executed MCP connector (`AnthropicMCP`) as a first-class `llm -T` tool**, distinct from the client-side `llm-mcp-client` plugin documented in `blog-simonwillison-stateless-mcp-tooling.md`.
  - **First in-corpus documentation of a Git-modeled, content-addressed message store for LLM conversation logging** — resolves the open graph-vs-duplication design question from `blog-simonwillison-llm032a0.md` Claim 14.
  - **First in-corpus documentation of `llm.PauseChain` and `tool_call_id` as core-library primitives for pausable/resumable tool loops**, distinct from the application-level `ask_user()` pattern in `blog-simonwillison-datasette-agent-askuser.md`.
  - **First in-corpus documentation of `llm-chat-completions-server`**, an OpenAI Chat Completions-API-compatible server built on `llm`, pairable with the also-new `llm openai endpoint` client command to form a full emulate-and-consume loop.
  - **First in-corpus dated record of the author formally adopting "agent framework" language for LLM**, with an explicit, hedged rationale and a specific cited prior definition ("an LLM agent runs tools in a loop to achieve a goal," from a September 2025 post).

## Guide Impact

- **Chapter 05 (Orchestration & Integration)**: Add `llm openai endpoint` + `llm-chat-completions-server` as a concrete, minimal-setup pattern for (a) probing any OpenAI-compatible model server without prior configuration and (b) exposing any `llm`-accessible model (including local ones) as a standard OpenAI Chat Completions endpoint for other tooling to consume. Cite Claims 6 and 9.
- **Chapter 03 (Tooling & Developer Experience)**: If the guide documents `llm` CLI reasoning-trace handling (building on `blog-simonwillison-llm032a0.md`'s coverage of `-R/--no-reasoning`), update the flag name to `-R/--hide-reasoning` and note the default flipped to display-by-default. Cite Claim 2.
- **Chapter 02 (Agent frameworks & tool orchestration)**: Add `llm.PauseChain` and `tool_call_id` as a reference core-library implementation of pausable, resumable tool loops, worth pairing with the application-level `ask_user()` pattern already documented from Datasette Agent — the guide can now show both a library-level primitive and an application built on top of the same need. Cite Claim 11.
- **Chapter 06 (Production Patterns)**: Add the content-addressed message store as a reference pattern for deduplicating logged conversation history in systems that resend growing message arrays on every turn (the OpenAI chat-completions replay shape) — directly relevant to any harness building its own conversation logging. Cite Claim 10.
- **Chapter 01 (Daily Workflows — model access)**: Update any `llm` CLI default-model references to GPT-5.6 Luna (from GPT-4o mini), and note `AnthropicMCP(...)` as a one-flag way to drive an MCP server through Claude without a separate MCP client plugin. Cite Claims 3 and 5.

## Extraction Notes

- **Followed the beat → full post → GitHub release notes chain**: The URL filed in the issue (`simonwillison.net/2026/Aug/4/llm/`) is a short "beat" entry containing no substantive content beyond a link to the detailed post (`simonwillison.net/2026/Aug/4/new-release-of-llm/`, used as the `source_url` for this note) and a link to the GitHub release. Both linked pages were fetched in full: the detailed post via `curl` + HTML-stripping (all quotes verified character-for-character against the raw HTML, including exact smart-quote characters), and the GitHub release notes via the GitHub API (`gh api` equivalent, raw markdown body). The companion `llm-anthropic` 0.26 release notes were also fetched via the GitHub API since the post explicitly names and links to that release as part of the same day's work.
- **No sub-pages beyond these three were followed**: the post links to several intermediate alpha/rc changelog anchors (0.32a0, 0.32a2, 0.32a3, 0.32rc1, 0.32rc2) and to plugin-author documentation ("Structured messages and streaming events"); these were not individually fetched as they are implementation-detail or migration-guide pages for plugin authors rather than practitioner-facing usage documentation, and the 0.32a0 alpha content is already covered by the existing `blog-simonwillison-llm032a0.md` note.
- **No contradictions filed**: see the Cross-References → Contradicts entry above for the reasoning on why the `-R` flag rename is treated as version evolution, not a contradiction requiring MINER.md §4a filing.
- **Cross-reference verification performed**: `blog-simonwillison-llm032a0.md` Claims 3, 4, 10, 12, 14 confirmed by direct reading at their stated line ranges. `blog-simonwillison-llm031.md` Claim 1 and Claim 4 confirmed at lines 26–31 and 47–52. `blog-simonwillison-llm-anthropic-0251.md` Claims 1, 2, 3 confirmed at lines 26–45. `blog-simonwillison-stateless-mcp-tooling.md` Claim 8 confirmed at lines 202–227 (exact tool names and quote verified). `blog-simonwillison-datasette-agent-askuser.md` Claims 1 and 4 confirmed at lines 42–57 and 94–110. All claim numbers verified by document-order count in each cited note before writing this note's cross-references.
- **Fragment URL**: The issue body cites `https://simonwillison.net/2026/Aug/4/llm/#atom-everything` (an Atom feed anchor on the "beat" entry, not the detailed post). `source_url` in this note's frontmatter points to the canonical detailed-post URL (`.../new-release-of-llm/`), which is where the substantive content used throughout this note actually lives, consistent with prior Willison notes in this corpus preferring the canonical content URL over feed-anchor URLs.
