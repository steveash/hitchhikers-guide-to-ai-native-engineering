---
source_url: https://simonwillison.net/2026/Aug/22/llm/
source_type: blog-post
title: "llm 0.33"
author: Simon Willison
date_published: 2026-08-22
date_extracted: 2026-08-30
last_checked: 2026-08-30
status: current
confidence_overall: settled
issue: "#3097"
---

# llm 0.33

> An incremental, maintenance-plus-features release of the `llm` CLI: template composition via repeated `-t/--template` flags (a genuinely new CLI pattern for this corpus), per-call `--key` support for embedding models, a `reasoning_summary` control for Responses API models, `llm logs` now surfacing server-side tool results, and a defensive-fixes/dependency-upgrade tail (OpenAI Python 3.x, `httpx2`, stricter `schema_dsl()` errors, attachment validation, four bug fixes).

## Source Context

- **Type**: blog-post (Willison "annotated-release-notes" beat format — a short post combining verbatim release-note bullets with the author's own italicized commentary interleaved after each bullet he chose to highlight; tagged `annotated-release-notes, llm`). The post is explicitly a subset ("My highlights from this release") of the full GitHub release, so this note also draws on the complete GitHub release body (fetched via `gh api repos/simonw/llm/releases/tags/0.33`) to avoid missing content the author chose not to highlight in the blog post.
- **Author credibility**: Simon Willison is the creator and maintainer of the `llm` Python library/CLI. This is first-party release documentation from the person who designed and shipped the features described.
- **Scope**: Covers the `llm` 0.33 release only — dependency upgrades, embedding-model key handling, `llm logs` server-side tool result display, template composition, schema DSL error handling, reasoning-part preservation, `reasoning_summary` control, attachment validation, and four bug fixes. Does NOT cover companion plugin releases (`llm-anthropic`, `llm-gemini`, `llm-openrouter`, `llm-mistral`), which are separately mined in `blog-simonwillison-llm-gemini-033.md` and `blog-simonwillison-llm-openrouter-07.md` and are not mentioned in this post or the 0.33 release notes. Does NOT include workflow analysis, benchmarks, or a pelican-SVG test (absent from this particular post, unlike several other Willison `llm` release notes in this corpus).

## Extracted Claims

### Claim 1: `llm prompt -t/--template` can now be repeated to combine multiple templates in one invocation, letting a template that packages model configuration and default options be combined with a separate template that supplies the prompt content
- **Evidence**: Direct GitHub release-note bullet, corroborated and expanded with a worked example and rationale in the blog post's own commentary beneath the bullet.
- **Confidence**: settled (first-party; shipped stable-release CLI behavior with a runnable example)
- **Quote**: "llm prompt -t/--template can now be repeated to combine templates in order. This allows model configuration and options from one template to be used with a prompt from another."
- **Our assessment**: This is a new composition primitive, not previously documented in this corpus's existing `llm` release notes (`blog-simonwillison-llm031.md`, `blog-simonwillison-llm032.md`) — neither of those notes mentions `--save`/template chaining. The worked example (Concrete Artifacts, below) shows the concrete payoff: a `--save`d template can pin a model plus an option like `reasoning_effort high`, while a second `--save`d template pins only a prompt string, and `-t lhigh -t pelican` merges the two into one call. This is directly useful for practitioners who want to reuse a "high-effort model config" across many different one-off prompts without retyping `-m` and `-o` flags each time, or who want to build small libraries of interchangeable prompt/config templates.

### Claim 2: `llm embed` and `llm embed-multi`, plus their Python equivalents, now accept a per-call `--key`/`key=` parameter for embedding models, mirroring the key-resolution pattern already used by regular (non-embedding) `llm` models, with a compatibility fallback for plugins that still read `self.key`
- **Evidence**: Direct GitHub release-note bullet naming the CLI flag, the four affected Python methods, the compatibility mechanism, and a credited external contributor; corroborated by the blog post's own gloss on the same bullet.
- **Confidence**: settled (first-party; specific methods and fallback behavior named)
- **Quote**: "llm embed and llm embed-multi now accept --key. The Python EmbeddingModel.embed(), EmbeddingModel.embed_multi(), Collection.embed() and Collection.embed_multi() methods accept key= too, passing the resolved per-call key to embedding plugins without changing shared model state. Existing plugins that read self.key continue to work through a compatibility fallback. Thanks, ChrisJr404. #757, #1620"
- **Our assessment**: The stated motivation — passing a resolved key per call "without changing shared model state" — matters for any multi-tenant or multi-credential embedding workflow (e.g., embedding documents under different API keys/accounts in the same process) where mutating a shared model object's key would be a correctness hazard under concurrency. The release note frames this as bringing embedding models into parity with "the same pattern for keys that regular LLM models do" (per the blog post's own annotation), but no source note currently in this corpus documents that pre-existing regular-model key pattern in detail, so we can only report the parity claim as stated by the author, not independently verify what the prior regular-model behavior looked like.

### Claim 3: Reasoning-capable Responses API models gain a `reasoning_summary` option accepting `auto`, `concise`, or `detailed`, usable together with `llm openai endpoint --responses`
- **Evidence**: Direct GitHub release-note bullet with a doc link, corroborated by the blog post's own annotation on the same bullet.
- **Confidence**: settled (first-party; named option and compatible command flag)
- **Quote**: "Reasoning-capable Responses API models now support a reasoning_summary option with auto, concise, and detailed values. This can be used with llm openai endpoint --responses. #1600"
- **Our assessment**: The blog post's own gloss — "This is particularly useful for exercising different models that provide their own imitation of the OpenAI Responses API" — frames this as a testing/compatibility-probing feature for third-party endpoints that implement an OpenAI-Responses-API-shaped surface, not primarily an OpenAI-model feature. This directly extends `blog-simonwillison-llm032.md` Claim 6, which documented `llm openai endpoint` as a zero-configuration way to run prompts against any OpenAI-compatible endpoint; `reasoning_summary` gives that same escape-hatch command a knob for controlling how much of a reasoning-capable third-party endpoint's "thinking" gets surfaced.

### Claim 4: `llm logs` now displays the output of server-side (provider-executed) tool calls in a dedicated "Tool results" section, and `llm logs --json`/`llm logs --short` include a new `server_executed` key to distinguish these from locally executed tool results
- **Evidence**: Direct GitHub release-note bullet (not repeated in the blog post's highlighted subset).
- **Confidence**: settled (first-party; specific new JSON key named)
- **Quote**: "llm logs now includes the output of server-side tool calls, shown in a Tool results section within the response. These results are also included in llm logs --json and llm logs --short output, with a new server_executed key distinguishing them from locally executed tool results. #1629"
- **Our assessment**: This closes an observability gap in the server-side-tool architecture that `blog-simonwillison-llm032.md` Claims 4 and 5 documented as shipping in the prior stable release (`-T CodeInterpreter`, `-T WebSearch`, `-T AnthropicMCP`, etc.) — before this fix, a provider-executed tool call's actual output was presumably not fully visible via `llm logs`, only whatever the model surfaced in its response text. The `server_executed` flag lets tooling built on `llm logs --json` (dashboards, audit scripts, cost-tracking) programmatically separate provider-executed tool activity from locally executed tool activity, which matters for anyone auditing which computations ran inside a provider's infrastructure versus the caller's own process.

### Claim 5: `llm` upgraded to the OpenAI Python library 3.x and switched its HTTP client dependency from `httpx` to `httpx2`, following a narrower same-week `0.32.1` patch that addressed the same underlying issue less comprehensively
- **Evidence**: Direct GitHub release-note bullet; the "more comprehensive fix" framing and timing ("yesterday") is from the blog post's own annotation on the same bullet, not the GitHub release body.
- **Confidence**: settled (first-party; author's own account of a same-week patch sequence)
- **Quote**: "Upgraded to the OpenAI Python library 3.x and switched the HTTP client dependency from httpx to httpx2. #1608, #1631" — annotated: "I shipped a quick 0.32.1 fix for this yesterday, but this is the more comprehensive fix."
- **Our assessment**: This is a dependency-compatibility item rather than a user-facing feature, but the two-step patch pattern (a fast, narrow `0.32.1` fix followed eight days later by 0.33's more complete migration) is worth noting as a signal of how quickly upstream SDK/HTTP-client breakage can force reactive point releases in a widely-depended-on CLI tool — practitioners pinning `llm` versions in CI should treat rapid-succession patch releases like this as a cue to re-check changelogs rather than assume patch versions are purely cosmetic.

### Claim 6: Reasoning stream events carrying provider metadata but no visible text are now preserved as `ReasoningPart` objects instead of being dropped, specifically enabling opaque state such as Anthropic's reasoning signatures and redacted-thinking data to round-trip correctly
- **Evidence**: Direct GitHub release-note bullet, cross-referencing an upstream `llm-anthropic` issue.
- **Confidence**: settled (first-party changelog entry, tied to a specific upstream issue reference)
- **Quote**: "Reasoning stream events that contain provider metadata but no text are now preserved as ReasoningPart objects. This allows opaque state such as Anthropic signatures and redacted thinking data to round-trip correctly. simonw/llm-anthropic#81"
- **Our assessment**: This is a correctness fix for the typed-streaming-events architecture `blog-simonwillison-llm032.md` Claim 8 documented as shipping in 0.32 (`event.type` discriminated events including a `"reasoning"` branch). Before this fix, a reasoning event that carried only provider-internal metadata (no human-readable text) risked being silently lost when logged and replayed — which would have been especially damaging for Anthropic's redacted/signed thinking blocks, where the opaque signature itself (not the text) is what the provider needs back on a subsequent turn to validate the reasoning chain. This is the kind of fix that matters specifically for multi-turn tool loops using extended thinking, not for single-turn prompts.

### Claim 7: `schema_dsl()` now raises descriptive `ValueError` exceptions for unknown field types and duplicate field names, instead of silently treating unknown types as strings or silently overwriting earlier fields with the same name
- **Evidence**: Direct GitHub release-note bullet, with two upstream issue references.
- **Confidence**: settled (first-party changelog entry describing a behavior change from silent-failure to explicit-error)
- **Quote**: "schema_dsl() now raises descriptive ValueError exceptions for unknown field types and duplicate field names, instead of silently treating unknown types as strings or overwriting earlier fields. #1607, #1616"
- **Our assessment**: This is a fail-fast correctness improvement for anyone using `llm`'s schema DSL (`--schema`/`--schema-multi`) to constrain structured output — the prior silent behavior (typo'd field type quietly becomes a string field; duplicate field name quietly overwrites) is exactly the kind of bug that produces a schema that "works" but silently extracts the wrong shape of data, discoverable only by manually inspecting output rather than by an immediate error at schema-definition time. Worth flagging for any guide content recommending `llm --schema` for structured extraction: upgrading to 0.33 will turn previously-silent schema-definition typos into hard errors, which is a desirable but potentially CI-breaking change for pinned schema strings with existing typos.

### Claim 8: Conversation prompts now validate, before execution, that all attachments are supported by the selected model — for both synchronous and asynchronous conversations
- **Evidence**: Direct GitHub release-note bullet, crediting an external contributor.
- **Confidence**: settled (first-party changelog entry)
- **Quote**: "Conversation prompts now validate that attachments are supported by the selected model before execution, for both synchronous and asynchronous conversations. Thanks, Daniel Peng. #1626, #1628"
- **Our assessment**: This moves an attachment/model-capability mismatch from a runtime API-call failure (presumably a rejected or erroring request from the provider) to a pre-execution validation error inside `llm` itself — useful in scripted pipelines that attach files/images to conversation turns programmatically, where an early, `llm`-native error is easier to catch and handle than an arbitrary provider-specific API error surfaced mid-request.

### Claim 9: The release includes four bug fixes: a `conversation_id` duplication bug in `llm logs --data-ids`, a `ValueError` crash in `llm aliases list` when no aliases are defined, an embedding-model-reuse/error-masking bug in `llm embed-multi`, and a redundant message printed by `llm tools -m MODEL` for models with no server-side tools
- **Evidence**: Four discrete GitHub release-note bullets under a "Bug fixes" heading, two crediting external contributors by name.
- **Confidence**: settled (first-party changelog entries, each with a specific symptom description and issue/PR reference)
- **Quote**: "llm logs --data-ids now sets conversation_id to the ID of the conversation instead of incorrectly duplicating the response ID. Thanks, K Merchant. #1598, #1613" / "Fixed llm aliases list raising a ValueError when no aliases are defined. Thanks, Taraka Abhiram. #1602" / "llm embed-multi now reuses an existing collection's stored embedding model when no default embedding model is configured, and no longer masks unrelated ValueError exceptions with a missing-model error. #1523" / "llm tools -m MODEL no longer prints a redundant message when the model has no server-side tools."
- **Our assessment**: The `llm embed-multi` fix is the most substantive of the four for practitioners: previously, an unrelated `ValueError` (any cause) raised while embedding could be masked and reported as a generic "missing model" error, which would misdirect debugging effort toward checking model configuration when the real fault lay elsewhere. The other three are narrow, low-blast-radius CLI ergonomics fixes (a metadata field, an empty-state crash, a redundant status line) not individually significant enough to warrant separate claims but worth recording as concrete evidence the release received routine maintenance attention beyond the four headline features.

## Concrete Artifacts

### CLI: template composition — packaging a model+option config template with a separate prompt template
```bash
llm -m gpt-5.6-luna -o reasoning_effort high --save lhigh
llm "Generate an SVG of a pelican riding a bicycle" --save pelican
# Combine and run the templates
llm -t lhigh -t pelican
```
*Source: simonwillison.net/2026/Aug/22/llm/ (author's own worked example, verified verbatim against the raw page HTML)*

### GitHub release notes — New features (verbatim, github.com/simonw/llm, tag 0.33, published 2026-08-22T17:01:16Z)
```
- Upgraded to the OpenAI Python library 3.x and switched the HTTP client
  dependency from httpx to httpx2. #1608, #1631
- llm embed and llm embed-multi now accept --key. The Python
  EmbeddingModel.embed(), EmbeddingModel.embed_multi(), Collection.embed()
  and Collection.embed_multi() methods accept key= too, passing the
  resolved per-call key to embedding plugins without changing shared model
  state. Existing plugins that read self.key continue to work through a
  compatibility fallback. Thanks, ChrisJr404. #757, #1620
- llm logs now includes the output of server-side tool calls, shown in a
  Tool results section within the response. These results are also
  included in llm logs --json and llm logs --short output, with a new
  server_executed key distinguishing them from locally executed tool
  results. #1629
- llm prompt -t/--template can now be repeated to combine templates in
  order. This allows model configuration and options from one template to
  be used with a prompt from another.
- Expanded the llm prompt --help documentation for --schema and
  --schema-multi with details and examples of the supported schema DSL.
- schema_dsl() now raises descriptive ValueError exceptions for unknown
  field types and duplicate field names, instead of silently treating
  unknown types as strings or overwriting earlier fields. #1607, #1616
- Reasoning stream events that contain provider metadata but no text are
  now preserved as ReasoningPart objects. This allows opaque state such as
  Anthropic signatures and redacted thinking data to round-trip correctly.
  simonw/llm-anthropic#81
- Reasoning-capable Responses API models now support a reasoning_summary
  option with auto, concise, and detailed values. This can be used with
  llm openai endpoint --responses. #1600
- Conversation prompts now validate that attachments are supported by the
  selected model before execution, for both synchronous and asynchronous
  conversations. Thanks, Daniel Peng. #1626, #1628
```
*Source: GitHub API, github.com/simonw/llm/releases/tags/0.33*

### GitHub release notes — Bug fixes (verbatim, github.com/simonw/llm, tag 0.33)
```
- llm logs --data-ids now sets conversation_id to the ID of the
  conversation instead of incorrectly duplicating the response ID. Thanks,
  K Merchant. #1598, #1613
- Fixed llm aliases list raising a ValueError when no aliases are defined.
  Thanks, Taraka Abhiram. #1602
- llm embed-multi now reuses an existing collection's stored embedding
  model when no default embedding model is configured, and no longer
  masks unrelated ValueError exceptions with a missing-model error. #1523
- llm tools -m MODEL no longer prints a redundant message when the model
  has no server-side tools.
```
*Source: GitHub API, github.com/simonw/llm/releases/tags/0.33*

## Cross-References

- **Corroborates**: None identified — this release does not restate or independently re-confirm a claim already made in another source note; it extends prior notes instead (see below).

- **Contradicts**: None identified.

- **Extends**:
  - `blog-simonwillison-llm032.md` Claim 6 (`llm openai endpoint` as a zero-configuration way to run prompts against any OpenAI-compatible endpoint): Claim 3 here adds a `reasoning_summary` control usable specifically with `llm openai endpoint --responses`, extending that command's usefulness to probing how third-party Responses-API-compatible endpoints summarize reasoning.
  - `blog-simonwillison-llm032.md` Claims 4 and 5 (server-side tools shipping in 0.32: `-T CodeInterpreter`, `-T WebSearch`, `-T AnthropicMCP`, etc.): Claim 4 here closes an observability gap in that architecture by surfacing server-side tool call output in `llm logs`, with a new `server_executed` distinguishing key.
  - `blog-simonwillison-llm032.md` Claim 8 (typed `event.type`-discriminated `stream_events()`, including a `"reasoning"` branch, shown as stable in 0.32): Claim 6 here is a correctness fix within that same typed-event system, preventing loss of metadata-only reasoning events during round-tripping.
  - `blog-simonwillison-llm031.md` (a four-bullet, comparably thin release note for `llm` 0.31, covering `-o verbosity`/`-o image_detail` CLI option flags): this release continues the pattern of `llm` shipping incremental, well-scoped CLI/API additions roughly every few months, with 0.33 following 0.32 (Aug 4, 2026) by eighteen days.

- **Novel**:
  - **First in-corpus documentation of template composition via repeated `-t/--template` flags** (Claim 1) — no other `llm`-focused source note in this corpus (`blog-simonwillison-llm031.md`, `blog-simonwillison-llm032.md`, `blog-simonwillison-llm032a0.md`) documents `--save`-based template chaining.
  - **First in-corpus documentation of per-call embedding-model key resolution** (Claim 2) — prior corpus notes do not cover `llm embed`/`llm embed-multi` credential handling at all.
  - **First in-corpus documentation of the `server_executed` distinguishing key in `llm logs --json`/`--short`** (Claim 4).
  - **First in-corpus documentation of `ReasoningPart` as the object type used to preserve metadata-only reasoning events** (Claim 6).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add `llm -t template1 -t template2` (repeated `-t/--template`) as a concrete CLI composition pattern: a `--save`d template can pin a model plus default options (e.g., `-m gpt-5.6-luna -o reasoning_effort high`), a second `--save`d template can pin a reusable prompt, and combining them at call time avoids retyping model/option flags across many one-off invocations. Cite Claim 1 and the Concrete Artifacts worked example.
- **Chapter 01 (Daily Workflows)**: If the guide documents `llm embed`/`llm embed-multi` for building local vector stores, note the new per-call `--key`/`key=` parameter as the mechanism for multi-credential embedding workflows (e.g., embedding under different API accounts in the same process) without mutating shared model state. Cite Claim 2.
- **Chapter 03 (Verification)**: If the guide recommends `llm --schema`/`--schema-multi` for structured-output extraction, note that upgrading to 0.33 turns previously-silent schema-definition mistakes (unknown field types, duplicate field names) into explicit `ValueError`s at definition time rather than silent data corruption at extraction time — a correctness improvement worth flagging as a reason to stay current on `llm` versions when relying on its schema DSL. Cite Claim 7.
- **Chapter 04 (Context Engineering)**: If the guide discusses multi-turn tool loops with extended-thinking/reasoning models (e.g., Anthropic's signed or redacted thinking blocks), note that `llm` 0.33 fixes a round-tripping gap where metadata-only reasoning events (no visible text) could previously be lost, which specifically affects providers whose reasoning continuity depends on opaque signature data surviving a full request/response/request cycle. Cite Claim 6.

## Extraction Notes

- **Fetched two sources**: the blog post itself (via `curl` with a browser user-agent, HTML-stripped to extract the `entryBody` content, then manually verified against the raw HTML for exact wording of bullets, the code example, and the two annotated asides — WebFetch's own summarization pass paraphrased and lost several bullets on first attempt, so the raw HTML fetch was used as the source of truth for all quotes) and the GitHub release notes (via `gh api repos/simonw/llm/releases/tags/0.33`, raw markdown body). The blog post explicitly frames itself as "My highlights from this release," i.e., a curated subset of the full GitHub release — Claims 4, 6, 7, 8, and 9 are drawn from GitHub-release-only content not repeated in the blog post's highlighted bullets, following MINER.md §1's instruction not to stop at a summary when a fuller primary source is one link away.
- **No sub-pages followed beyond the two primary sources**: the release notes link to the `llm openai endpoint --responses` documentation page (`llm.datasette.io/en/stable/other-models.html#openai-endpoint`); this was not separately fetched as it is general command reference documentation already partially covered by `blog-simonwillison-llm032.md` Claim 6, and the 0.33-specific addition (`reasoning_summary`) is fully described in the release-note bullet itself.
- **No contradictions found requiring MINER.md §4a filing**: this release's content is either genuinely novel to the corpus or a direct extension/fix of prior `llm` release notes already in this corpus; no claim here opposes an existing source note.
- **Cross-reference verification performed**: `blog-simonwillison-llm032.md` Claim 6 confirmed at lines 56–60 (`llm openai endpoint` zero-configuration command). `blog-simonwillison-llm032.md` Claims 4 and 5 confirmed at lines 44–54 (`-T CodeInterpreter`, Anthropic server-side tools). `blog-simonwillison-llm032.md` Claim 8 confirmed at lines 68–72 (typed `event.type` streaming with a `"reasoning"` branch). `blog-simonwillison-llm031.md` confirmed as a four-bullet, thin release note by direct reading of the full file. All claim numbers verified by document-order count in each cited note before writing this note's cross-references. Searched the full `source-notes/` directory for any existing coverage of `llm`'s regular-model `--key`/key-resolution pattern (referenced by this release's Claim 2 as prior art) and found none — this is noted explicitly in Claim 2's Our assessment rather than asserted as independently verified.
