---
source_url: https://simonwillison.net/2026/Jul/30/llm-chat-completions-server/
source_type: blog-post
title: "Release: llm-chat-completions-server 0.1a0"
author: Simon Willison
date_published: 2026-07-30
date_extracted: 2026-08-03
last_checked: 2026-08-03
status: current
confidence_overall: anecdotal
issue: "#2445"
---

# Release: llm-chat-completions-server 0.1a0

> Simon Willison's six-sentence release "beat" for a new `llm` plugin that
> serves an OpenAI Chat Completions-compatible endpoint is a thin wrapper
> around the real artifact: a linked ~1,800-word GitHub Gist session
> transcript showing GPT-5.6 Sol building the entire plugin end-to-end under
> an explicit red/green-TDD-plus-manual-verification directive, catching and
> root-causing a real data-integrity bug that its own test suite missed, and
> passing a final multi-part completion checklist that includes exercising
> the official OpenAI Python client against the live server.

## Source Context

- **Type**: blog-post (Willison "beat" — his shortest release-announcement
  format at simonwillison.net, four paragraphs plus two code blocks) with a
  linked GitHub Gist (`github.com/simonw/53be513c1bd4a29a7aa480d9bde9b4a5`,
  titled `server.md`, created 2026-07-27) containing the full AI-agent
  development session transcript. Both were read in full. A second linked
  Willison post, "llm 0.32rc1" (`simonwillison.net/2026/Jul/30/llm-rc1/`,
  same-day release notes for the underlying `llm` library RC), was also read
  in full because it is the direct technical antecedent this plugin exists
  to exercise.
- **Author credibility**: Simon Willison is the creator of the `llm` Python
  library/CLI and Django, and one of the most widely-cited independent LLM
  tooling practitioners. This is first-party release documentation for a
  plugin he personally directed the construction of; the gist is a primary-
  source, unedited record of that session (not retrospective commentary). No
  vendor affiliation.
- **Scope**: Covers (1) the motivation for `llm-chat-completions-server` —
  exercising `llm` 0.32rc1's new content-addressable message logging; (2)
  install/run commands and the resulting server's behavior; (3) a full
  agentic development session in which GPT-5.6 Sol built the plugin under
  Willison's direction, including a TDD-plus-manual-verification workflow, a
  real bug caught by manual log inspection, and a final verification
  checklist. Does NOT cover: the plugin's source code in full (only fragments
  are quoted in the transcript), performance/load characteristics, or how the
  plugin behaves with authentication enabled (it explicitly has none).

## Extracted Claims

### Claim 1: LLM 0.32rc1's most important change is content-addressable hash IDs for stored messages, enabling database de-duplication and message trees for forked conversations
- **Evidence**: Author's direct statement in the companion "llm 0.32rc1" release post, which this plugin was built to exercise.
- **Confidence**: settled (first-party release note from the library's creator)
- **Quote**: "The most important change is the use of content-addressable hash IDs for stored messages. This allows de-duplication in the database, and means that LLM can now represent trees of messages for forked conversations."
- **Our assessment**: This is the schema change that makes an OpenAI-style Chat Completions emulation tractable without unbounded storage growth — see Claim 2. It directly delivers the graph-based logging design Willison said he wanted for exactly this use case three months earlier (see Cross-References → Extends).

### Claim 2: A key goal of the content-addressable logs was supporting OpenAI Chat Completion-style requests where each new request resends and extends the full prior conversation, deduplicated by hashing individual message parts
- **Evidence**: Author's explanation in the `llm-chat-completions-server` post, illustrated with a concrete `curl` example showing a growing `messages` array.
- **Confidence**: settled (first-party design rationale, with a working code example)
- **Quote**: "Here the conversation state is tracked by the client, so each of these requests gets longer and longer. The new schema design in LLM is designed to de-duplicate these using hashes of the individual message parts."
- **Our assessment**: This names a real storage problem for anyone building an OpenAI-compatible server on top of a stateful backend: the OpenAI Chat Completions contract is stateless from the server's point of view — the client resends the whole transcript every turn — so a naive logging implementation stores the same early messages over and over as a conversation grows. Content-addressed hashing turns that into a dedup problem instead of a data-explosion problem.

### Claim 3: The `llm-chat-completions-server` plugin exposes the user's full local collection of `llm` models (across all installed plugins) through an unauthenticated, OpenAI Chat Completions-compatible localhost endpoint
- **Evidence**: Author's description of the running server, install commands, and confirmed in the session transcript's own completion summary ("Async-only `/v1/models`", "Unauthenticated `/v1/chat/completions`").
- **Confidence**: settled (first-party; behavior independently confirmed by the build session's own final checklist)
- **Quote**: "Running this starts a localhost server on port 9001 that exposes your full collection of LLM models (from any plugins you have installed) using a ChatGPT Completions compatible endpoint."
- **Our assessment**: This is a practical "adapter" pattern — a local API-compatibility shim that lets any OpenAI-client-speaking tool (including the official `openai` Python SDK, see Claim 10) transparently target dozens of different model backends (Gemini, Anthropic, Apple Foundation Models, etc. in this session) without each of those tools needing native multi-provider support.

### Claim 4: Willison attributes authorship of the entire plugin implementation to GPT-5.6 Sol, describing it as fluent in the OpenAI Chat Completions API shape
- **Evidence**: Author's direct statement, linking to the gist as the supporting artifact.
- **Confidence**: anecdotal (a single practitioner's characterization of one model's output on one task)
- **Quote**: "GPT-5.6 Sol wrote the whole thing - it turns out it knows the OpenAI Chat Completions API shape really well."
- **Our assessment**: "Wrote the whole thing" is Willison's framing, not strictly literal — the transcript shows him giving substantive direction throughout (scope decisions in Claim 6, a bug report in Claim 8, plugin-list changes) rather than a single unattended prompt. The claim is best read as "the agent authored all the code," not "the agent worked without a human in the loop."

### Claim 5: Willison's opening instruction directed the agent to build the plugin using red/green TDD combined with continuous manual testing against a live, auto-reloading dev server, rather than automated tests alone
- **Evidence**: Willison's direct instruction early in the session transcript, which the agent explicitly restates as its working plan a few turns later.
- **Confidence**: anecdotal (single session; reflects one practitioner's stated workflow preference)
- **Quote**: "build this with red/green TDD but also do manual tests of it while you are building by running a copy of it on some port - support a --reload option so your dev server reloads as the code changes"
- **Our assessment**: This is a human explicitly specifying *how* an agent should verify its own work, not just *what* to build — a concrete instance of a practitioner encoding a verification methodology into the task prompt itself rather than trusting the agent's default approach or checking only at the end.

### Claim 6: Willison asked to see the live server URL for just the first working slice (`/v1/models`) before the agent continued building further features, prioritizing an early incremental check-in over a single end-of-session review
- **Evidence**: Willison's direct instruction, which the agent immediately re-planned around ("I'm switching the first red/green slice to exactly that... send you the live URL before continuing with completions").
- **Confidence**: anecdotal (single session)
- **Quote**: "let me know the URL as soon as you have that /v1/models endpoint up and running so I can see it, do that bit first"
- **Our assessment**: This reorders the agent's own stated plan (command wiring → `/v1/chat/completions` → tests → docs) to front-load a human checkpoint on the smallest possible working slice, rather than letting the agent run the full task to completion before any human inspection. It's a cheap way to catch scope or design drift early in a long single-session build.

### Claim 7: The agent wrote a large "red" (intentionally failing) test suite covering the full behavioral surface — auth, exact message translation including images and tool history, async-only model lookup, options, tool definitions/results, both streaming and non-streaming output, usage reporting, and OpenAI-shaped errors — before writing the implementation
- **Evidence**: The agent's own description of the test suite immediately after writing it, before the corresponding server code existed.
- **Confidence**: anecdotal (single session)
- **Quote**: "The completion tests are now red for the intended reason (the route does not exist yet). The new tests exercise unauthenticated calls, exact llm.Message translation—including images and tool history—async-only lookup, options, tool definitions/results, non-streaming output, SSE streaming, usage, and OpenAI-shaped errors."
- **Our assessment**: The breadth of the enumerated test surface (nine distinct behavioral dimensions) before any implementation code existed is a concrete illustration of what "red/green TDD" meant operationally in this session — not a token failing test, but a specification-complete failing suite written first.

### Claim 8: Willison caught a real data-integrity bug — a missing prompt on the most recently logged conversation — by manually inspecting `llm logs -c` output, a defect the automated test suite had not caught
- **Evidence**: Direct exchange in the transcript: Willison's bug report followed by the agent confirming the defect was real and undetected until then.
- **Confidence**: anecdotal (single session, single bug)
- **Quote**: "weird, look at the most recently logged message (uv run llm logs -c) - the prompt is missing"
- **Our assessment**: All ten of the session's automated tests were passing at this point, including a specific logging test (`test_completed_responses_are_logged`). The bug was invisible to that test suite and was only found because Willison independently inspected the actual persisted output via a real CLI command, not through the code path the tests exercised. This is a distinct failure mode from workspace-state mistakes documented elsewhere in the corpus (see Cross-References → Extends): tests can pass while behavior actually visible to a downstream consumer is still wrong.

### Claim 9: The agent root-caused the logging bug as a compatibility gap between the legacy and content-addressed logging schemas — the new message chain stored the prompt correctly, but the legacy `responses.prompt` column stayed null because the server called `model.prompt(messages=...)` without the legacy `prompt=` argument — by directly querying the SQLite tables rather than guessing
- **Evidence**: The agent's own stated hypothesis, followed by direct database introspection commands (querying both the legacy `responses` table and the content-addressed `turns`/message-chain tables), then a confirmed diagnosis.
- **Confidence**: anecdotal (single session, single bug)
- **Quote**: "Confirmed: this is a compatibility gap between the two logging schemas. The content-addressed chain has the full user prompt, but the legacy responses.prompt column is null, so llm logs -c renders -- none --."
- **Our assessment**: The diagnostic sequence — state a specific, falsifiable hypothesis, then verify it by querying the actual database state directly (`sqlite_utils.Database(...).query(...)`) rather than re-reading source code or guessing — is a concrete, reproducible root-cause pattern: go to the data before changing the code.

### Claim 10: Before declaring the work complete, the agent ran a multi-part verification pass spanning unit tests, lint, format checking, lockfile checking, package build, live curl checks, database log verification, and compatibility testing against the official OpenAI Python client library
- **Evidence**: The agent's own closing summary line, corroborated by the actual commands in the transcript, including one that imports `openai.OpenAI`, points its `base_url` at the locally running server, and issues a real chat completion request through it.
- **Confidence**: anecdotal (single session)
- **Quote**: "Documentation is complete, and unit, lint, formatting, lockfile, package-build, live curl, database-log, and OpenAI-client compatibility checks all passed."
- **Our assessment**: Testing an OpenAI-API-compatible server with the actual official OpenAI SDK — rather than only asserting response-shape equality in unit tests — is a stronger compatibility check: it exercises exactly the client code real consumers will use, including whatever request-building and response-parsing assumptions that SDK makes that a hand-written test might not replicate.

### Claim 11: The live dev server was restarted multiple times over the session with additional `--with-editable` plugin sources (first Gemini and Anthropic, later Apple Foundation Models) so it could be manually exercised against more real model backends as the plugin ecosystem under test grew
- **Evidence**: Multiple restart commands with an accumulating list of `--with-editable` flags, ending with a confirmation that the live `/v1/models` endpoint listed 113 async models including the newly added Apple Foundation Models plugin.
- **Confidence**: anecdotal (single session)
- **Quote**: "Restarted successfully. http://127.0.0.1:8003/v1/models is live again and now lists apple-foundation among 113 async models."
- **Our assessment**: This is the live-server counterpart to the automated test suite — every time the surface being tested widened (a new model plugin), the agent restarted the actual running process and re-verified against it via `curl`, rather than treating the earlier manual verification (Claim 6) as a one-time checkpoint that didn't need repeating.

## Concrete Artifacts

### Install and run commands (from the post, verbatim)
```
uv tool install llm --pre
llm install llm-chat-completions-server
llm chat-completions-server -p 9001
```
*Source: simonwillison.net/2026/Jul/30/llm-chat-completions-server/*

### Motivating example: growing client-tracked conversation (from the post, verbatim)
```
curl http://localhost:8002/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "qwen3.5-4b",
    "messages": [
      {"role": "user", "content": "Capital of France?"},
      {"role": "assistant", "content": "Paris."},
      {"role": "user", "content": "Germany?"}
    ]
  }'
```
*Source: simonwillison.net/2026/Jul/30/llm-chat-completions-server/*

### `llm` 0.32rc1 pre-upgrade backup command and new model support (from the companion rc1 post, verbatim)
```
llm logs backup logs-backup.db
```
> "The RC also adds support for `gpt-5.6-sol`, `gpt-5.6-terra`, and `gpt-5.6-luna`."

*Source: simonwillison.net/2026/Jul/30/llm-rc1/*

### Final session summary / completion checklist (from the gist transcript, verbatim)
```
Implemented and live at http://127.0.0.1:8003/v1/models.

Key results:
- llm chat-completions-server, default port 8002, with -p/--port and --reload
- Async-only /v1/models
- Unauthenticated /v1/chat/completions
- Streaming SSE and non-streaming responses
- Messages, images, tools, options, schemas, and usage
- Logging to legacy and content-addressed tables using the latest ~/dev/llm
- Live server includes Gemini, Anthropic, and Apple Foundation plugins
- 10 tests passing; lint, formatting, lockfile, package build, curl, and
  OpenAI Python client verified
```
*Source: gist github.com/simonw/53be513c1bd4a29a7aa480d9bde9b4a5 (server.md), closing summary*

### OpenAI Python client compatibility check (from the gist transcript, verbatim command)
```
uv run python -c 'from openai import OpenAI; c=OpenAI(base_url="http://127.0.0.1:8003/v1", api_key="ignored"); r=c.chat.completions.create(model="apple-foundation", messages=[{"role":"user","content":"Say hello in one word"}]); print(type(r).__name__, r.model, repr(r.choices[0].message.content), r.choices[0].finish_reason)'
```
*Source: gist github.com/simonw/53be513c1bd4a29a7aa480d9bde9b4a5 (server.md) — the final compatibility pass described in Claim 10*

### Full final verification command chain (from the gist transcript, verbatim)
```
git diff --check && uv lock --check && uv run pytest -q && uvx ruff check llm_chat_completions_server.py tests && uvx ruff format --check llm_chat_completions_server.py tests
```
*Source: gist github.com/simonw/53be513c1bd4a29a7aa480d9bde9b4a5 (server.md)*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-datasette-blog-codex-session.md` Claim 6 (Codex Desktop ran the project's test suite repeatedly as a verification mechanism and did not declare a refactor complete until it passed): the GPT-5.6 Sol session shows the same pattern with a different agent and tool — running the full check chain (tests, lint, format, lockfile, build) before declaring done, per Claim 10 here.
  - `blog-simonwillison-datasette-blog-codex-session.md` Claim 7 (Codex used headless-Chromium screenshots to visually verify a CSS fix before reporting completion): a different modality of the same principle documented in Claim 10/11 here — verifying against a live, real environment (a running server hit with actual `curl`/SDK calls) rather than trusting unit-test assertions alone.
  - `blog-simonwillison-datasette-agent-askuser.md` Claim 6 (Willison built a new `llm` alpha "yesterday" with the help of Claude Fable 5, days after that model's release): the same practitioner pattern recurs here — Willison uses a just-released frontier model (GPT-5.6 Sol, per the companion rc1 post's same-day model-support addition) to build supporting developer tooling almost immediately after that model becomes available.

- **Contradicts**: None identified. No existing corpus note claims that automated test suites alone are sufficient verification for agent-built code, so this source's emphasis on manual/live verification does not conflict with prior claims — it adds a concrete case study rather than opposing one.

- **Extends**:
  - `blog-simonwillison-llm032a0.md` Claim 4 (the prior `llm` conversation API "didn't provide a way to feed in a previous conversation from the start," making it "much harder than they should have been" to build an OpenAI Chat Completions emulation): this source is the direct fulfillment of that gap — the messages-array API from 0.32a0, combined with the content-addressable logging from 0.32rc1 (Claim 1 here), is exactly what made `llm-chat-completions-server` tractable to build.
  - `blog-simonwillison-llm032a0.md` Claim 14 (Willison's stated intent, three months earlier, to "model this as a graph, to best support situations like an OpenAI-style chat completions API where the same conversations are constantly extended and then repeated with every prompt... without duplicating them in the database"): Claim 1 and Claim 2 here confirm that intent shipped as content-addressable hash IDs in 0.32rc1, and this plugin is presented explicitly as the thing built "to test that out."
  - `blog-simonwillison-datasette-blog-codex-session.md` Claim 5 (Codex Desktop's accidental deletion of an untracked directory was a mistake caught by the developer, not by any automated check) and that note's Guide Impact distinction between "agent errors on code" (caught by tests) and "agent errors on workspace state" (only caught by developer noticing): Claim 8 here adds a third category to that framework — an agent error that automated tests explicitly targeting the affected feature (a logging test) still missed, caught only by a human manually inspecting real output. This nuances the corpus's existing tests-vs-manual-inspection framing: even a passing, on-topic test does not guarantee correct behavior.

- **Novel**:
  - First corpus documentation of a human giving an explicit upfront directive combining red/green TDD with continuous manual testing against a live, auto-reloading dev server (Claim 5), rather than the agent choosing a verification strategy unprompted or the human only reviewing at the end.
  - First corpus example of an "incremental live-URL check-in" interaction pattern, where the human asks to see the smallest working vertical slice live before the agent proceeds to the next feature (Claim 6).
  - First corpus documentation of an agent root-causing a bug by directly querying two different persistence schemas (legacy vs. content-addressed tables) in the underlying SQLite database, rather than only re-reading source code (Claim 9).
  - First corpus documentation of testing a hand-built OpenAI-API-compatible server against the official `openai` Python SDK client as a compatibility check, rather than only asserting response-shape equality in hand-written tests (Claim 10).
  - First corpus mention of content-addressable/hash-based message deduplication as a technique for LLM conversation logging (Claim 1, Claim 2).

## Guide Impact

- **Chapter on verification loops / definition-of-done**: Add the closing checklist from Claim 10 (unit tests → lint → format check → lockfile check → package build → live curl → database-log verification → official-client compatibility check) as a concrete, reusable template for what "done" can mean for an agent building an API-compatible server, citing this source alongside the existing Codex test-suite-as-verification-loop material in `blog-simonwillison-datasette-blog-codex-session.md`. Specifically recommend testing against the *official* client SDK when building any API-compatibility shim (Claim 10), not just hand-written request/response assertions.

- **Chapter on prompting / directing agents**: Add Claim 5 and Claim 6 as a concrete example of a human encoding *how* to verify into the task prompt itself (red/green TDD plus manual testing against a reloadable live server) and requesting an early incremental checkpoint on the smallest working slice, rather than trusting the agent's default verification approach or waiting for full completion before any human inspection.

- **Chapter on debugging / failure modes**: Add Claim 8 and Claim 9 as a case study of "tests pass, feature is still broken" — a logging test was green, but the actual persisted prompt was missing until a human manually inspected real CLI output. Pair with `blog-simonwillison-datasette-blog-codex-session.md`'s existing tests-vs-workspace-state framing (see Cross-References → Extends) to broaden that guidance: passing, on-topic tests are necessary but not sufficient; recommend practitioners spot-check real persisted output/logs even when the relevant tests are green. Also cite the agent's root-cause method (query the actual database state directly before changing code) as a reusable debugging pattern.

- **Chapter covering the `llm` library / OpenAI-compatibility tooling** (wherever `blog-simonwillison-llm032a0.md` is currently cited): note that the OpenAI Chat Completions emulation gap identified in that source (Claim 4) has since been closed by content-addressable logging in `llm` 0.32rc1 (Claim 1–2 here) and this reference-implementation plugin.

## Extraction Notes

- **WebFetch returned a compressed/paraphrased version of the main post.** The full verbatim text was obtained by fetching the raw HTML directly with `curl` and stripping markup with a Python script; all quotes and code blocks in this note are copied from that raw HTML, not from the WebFetch summary. The same direct-`curl` approach was used for the companion `llm-rc1` post and the linked gist.
- **Followed the linked "llm 0.32rc1" post** per MINER.md §1, since it is the direct technical antecedent this plugin was built to exercise (content-addressable logging) and is needed to support Claim 1.
- **Followed the linked GitHub Gist** (the "wrote the whole thing" link) — at ~17,700 characters of stripped text, it is the substantive AI-agent-development artifact; the blog post itself is six sentences plus two code blocks. This mirrors the pattern already documented in `blog-simonwillison-datasette-blog-codex-session.md` (a thin Willison "beat" pointing to a much larger session-transcript gist as the real content).
- **Gist was fetched via direct `curl` of the public gist page**, not `gh api gists/<id>`, since the rendered page (not the raw file) preserves the collapsible `<details>` transcript structure and inline `<code>` formatting needed to verify exact quote boundaries (e.g., confirming no stray whitespace around inline code spans like `` `uv run llm logs -c` ``).
- **Did not follow**: the "Stateless MCP has recaptured my interest" related-articles link (unrelated tangent, not linked from the post body) or the GitHub release-tag page (`github.com/simonw/llm-chat-completions-server/releases/tag/0.1a0`, which duplicates the post's own content without additional substance).
- **Cross-reference claim numbers verified by document-order count** before writing citations: `blog-simonwillison-llm032a0.md` Claim 4 confirmed at its lines 47–52, Claim 14 confirmed at lines 117–122; `blog-simonwillison-datasette-blog-codex-session.md` Claim 5 confirmed at lines 54–59, Claim 6 confirmed at lines 61–66, Claim 7 confirmed at lines 68–73; `blog-simonwillison-datasette-agent-askuser.md` Claim 6 confirmed at lines 131–146.
- **Overall confidence set to `anecdotal`**: the release-fact claims (1, 2, 3) are individually settled, but the bulk of this note's practitioner-relevant content (Claims 4–11) is drawn from a single, unreplicated AI-agent development session on one project, consistent with how `blog-simonwillison-datasette-blog-codex-session.md` — the closest analog in the corpus — was graded.
