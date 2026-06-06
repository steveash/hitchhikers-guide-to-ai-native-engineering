---
source_url: https://simonwillison.net/2026/May/28/llm-anthropic/
source_type: blog-post
title: "llm-anthropic 0.25.1"
author: Simon Willison
date_published: 2026-05-28
date_extracted: 2026-06-06
last_checked: 2026-06-06
status: current
confidence_overall: emerging
issue: "#1075"
---

# llm-anthropic 0.25.1

> A first-party release announcement for the `llm-anthropic` plugin documenting three practitioner-relevant changes: Claude Opus 4.8 support, a new fast mode option (`-o fast 1`), and a breaking behavior change where default max_tokens now matches each model's maximum output instead of 8,192.

## Source Context

- **Type**: blog-post (first-party release announcement; ~80 words; three bullet points + link to companion Opus 4.8 post; published as a "beat" entry on Willison's weblog at simonwillison.net/2026/May/28/llm-anthropic/)
- **Author credibility**: Simon Willison is the creator and maintainer of the `llm` Python CLI tool and the `llm-anthropic` plugin. This is first-party release documentation — factual accuracy about what was added is high. No vendor affiliation with Anthropic; independently maintained. The post links to a companion Opus 4.8 notes post (`simonwillison.net/2026/May/28/claude-opus-4-8/`) and to Anthropic's fast mode documentation (`platform.claude.com/docs/en/build-with-claude/fast-mode`).
- **Scope**: Covers three specific changes in `llm-anthropic` 0.25.1: (1) Claude Opus 4.8 model registration, (2) new `-o fast 1` CLI option for fast mode, and (3) a max_tokens default behavior change. The extraction also covers the linked fast mode documentation page and the Anthropic Opus 4.8 announcement page (`anthropic.com/news/claude-opus-4-8`), which provide technical depth about fast mode and Opus 4.8 capabilities. Does NOT cover the full Opus 4.8 capability profile, plugin compatibility requirements for LLM 0.32a0, or prior llm-anthropic release history.

## Extracted Claims

### Claim 1: llm-anthropic 0.25.1 adds support for Claude Opus 4.8, available via the `claude-opus-4.8` model identifier in the `llm` CLI

- **Evidence**: Verbatim bullet from the release note, first-party from the plugin's author. Claude Opus 4.8 was announced by Anthropic on the same date (May 28, 2026).
- **Confidence**: settled
- **Quote**: "New model: Claude Opus 4.8 (`claude-opus-4.8`)."
- **Our assessment**: Practitioners using the `llm` CLI can access Opus 4.8 via `llm -m claude-opus-4.8 'your prompt here'` after installing or upgrading to llm-anthropic 0.25.1. The identifier `claude-opus-4.8` is the slug registered in the plugin (not the REST API identifier `claude-opus-4-8`); the plugin handles the translation internally.

### Claim 2: A new `-o fast 1` option in llm-anthropic 0.25.1 enables Anthropic's fast mode for organizations that have the feature enabled on their account

- **Evidence**: Verbatim bullet from the release note, first-party. The `fast mode` link in the release note points to Anthropic's fast mode documentation, which confirms the feature is in research preview and gated by account access.
- **Confidence**: settled
- **Quote**: "New `-o fast 1` option for fast mode, for organizations with that feature enabled on their account."
- **Our assessment**: The `-o fast 1` syntax follows the existing `llm` CLI option pattern (`-o option_name value`). The value `1` acts as a boolean flag enabling fast mode. This maps to the `speed: "fast"` parameter in the underlying Anthropic API with the `fast-mode-2026-02-01` beta header. The access restriction ("for organizations with that feature enabled") reflects that fast mode is in research preview — practitioners must contact their Anthropic account manager or join the waitlist before this option has any effect.

### Claim 3: The default max_tokens behavior in llm-anthropic 0.25.1 changed from a fixed 8,192 to each model's maximum output — a breaking change for code that relied on the prior limit as an implicit cost cap

- **Evidence**: Verbatim bullet from the release note with GitHub issue citation (#72). For Claude Opus 4.8, the maximum output is 128,000 tokens (from the Anthropic Opus 4.8 announcement linked from the companion Willison post).
- **Confidence**: settled
- **Quote**: "Default max_tokens for each model now defaults to that model's maximum output rather than 8,192."
- **Our assessment**: This is the most consequential change for practitioners upgrading from llm-anthropic ≤0.25 to 0.25.1. Code that called Anthropic models via `llm` without an explicit `--max-tokens` argument previously generated at most 8,192 output tokens. After upgrade, the same calls can generate up to the model's full maximum (128,000 tokens for Opus 4.8). This has two effects: (1) longer responses are now possible without hitting a limit — useful for bulk extraction tasks; (2) potential cost increases for callers who relied on the 8,192 default as an implicit cost cap. Practitioners upgrading llm-anthropic should audit callers that did not set `--max-tokens` explicitly and add an explicit cap if cost control is required.

### Claim 4: Fast mode delivers up to 2.5x higher output tokens per second for supported Anthropic Opus models at premium pricing, with a dedicated rate limit separate from standard Opus rate limits

- **Evidence**: From the Anthropic fast mode documentation page linked from the release note (`platform.claude.com/docs/en/build-with-claude/fast-mode`). Official first-party Anthropic documentation.
- **Confidence**: settled (official documentation)
- **Quote**: "Up to 2.5x higher output tokens per second compared to standard speed" (from linked fast mode docs)
- **Our assessment**: Fast mode is an inference acceleration option using the same model weights with no capability difference. The speedup is specifically in output tokens per second (OTPS), not time to first token (TTFT). This distinction matters for latency-sensitive applications: fast mode helps throughput (tokens/second) but not responsiveness (time until the first token arrives). For agentic workflows where total wall-clock time is the bottleneck, fast mode is relevant; for interactive UIs where perceived responsiveness matters, the TTFT distinction is a limitation.

### Claim 5: Fast mode pricing for Claude Opus 4.8 ($10/$50 per MTok input/output) is three times cheaper than fast mode for Opus 4.6 and Opus 4.7 ($30/$150 per MTok)

- **Evidence**: Pricing table from the Anthropic fast mode documentation and the Anthropic Opus 4.8 announcement: "fast mode for Opus 4.8—where the model can work at 2.5× the speed—is now three times cheaper than it was for previous models." (from Anthropic's claude-opus-4-8 announcement page, linked via the companion Willison post)
- **Confidence**: settled (first-party pricing documentation)
- **Quote**: "fast mode for Opus 4.8—where the model can work at 2.5× the speed—is now three times cheaper than it was for previous models" (from linked Anthropic Opus 4.8 announcement)
- **Our assessment**: The 3x price reduction at Opus 4.8 is significant for practitioners who previously avoided fast mode at the Opus 4.6/4.7 price point ($30/$150). At $10/$50, Opus 4.8 fast mode input pricing is exactly 2x standard Opus 4.8 input pricing ($5/MTok). For practitioners targeting cost-predictable agentic workloads with high output volume, the fast mode price premium may be acceptable at the Opus 4.8 tier where it was not at Opus 4.6/4.7 pricing.

### Claim 6: Switching between fast and standard speed invalidates the prompt cache — requests at different speeds do not share cached prefixes

- **Evidence**: Stated as a "Considerations" item in the Anthropic fast mode documentation page. Non-obvious operational constraint with cost implications for fallback patterns.
- **Confidence**: settled (official documentation)
- **Quote**: "Switching between fast and standard speed invalidates the prompt cache. Requests at different speeds do not share cached prefixes." (from linked fast mode docs)
- **Our assessment**: This is the most operationally dangerous consideration in the fast mode feature. Practitioners who build fallback logic (e.g., "try fast mode, fall back to standard on rate limit") will incur a prompt cache miss on every fallback — paying twice for cache-eligible prefixes. For high-volume agentic workloads with large system prompts, this cost penalty can significantly erode fast mode's price advantage. The correct pattern is to designate a workflow as fast-mode-only or standard-only, not to switch dynamically per request unless cache miss costs are acceptable.

### Claim 7: Fast mode for Opus 4.8 is available only on the Claude API and Claude Managed Agents — not on Vertex AI, Amazon Bedrock, or Microsoft Foundry

- **Evidence**: Warning note in the Anthropic fast mode documentation page.
- **Confidence**: settled (official documentation)
- **Quote**: "Fast mode for Claude Opus 4.8 launches as a research preview on the Claude API, including Claude Managed Agents, only. It is not available on third-party platforms, including Vertex AI, Amazon Bedrock, and Microsoft Foundry." (from linked fast mode docs)
- **Our assessment**: Practitioners using Anthropic models via cloud provider platforms (AWS, GCP, Azure) cannot access Opus 4.8 fast mode at launch. This is a significant limitation for enterprise deployments that route through Bedrock or Vertex AI for data residency, compliance, or billing reasons. The `llm-anthropic` plugin (and by extension the `-o fast 1` flag) works with the direct Anthropic API, so it is unaffected by this restriction — but practitioners whose underlying infrastructure uses cloud provider endpoints need to be aware of this gap.

### Claim 8: Fast mode for Claude Opus 4.6 is deprecated at the Opus 4.8 launch, with approximately 30 days notice before removal — after which `speed: "fast"` requests to Opus 4.6 will silently fall back to standard speed

- **Evidence**: Deprecation warning in the Anthropic fast mode documentation page.
- **Confidence**: settled (official documentation)
- **Quote**: "Fast mode for Claude Opus 4.6 is deprecated as of the Claude Opus 4.8 launch and will be removed approximately 30 days later. After removal, requests to `claude-opus-4-6` with `speed: 'fast'` will fall back to standard speed at standard pricing rather than return an error." (from linked fast mode docs)
- **Our assessment**: The silent fallback behavior (standard speed, standard pricing, no error) is counterintuitive: practitioners who have Opus 4.6 fast mode in production will not receive a failure signal after removal, they will simply get slower responses and lower bills. This makes the deprecation undetectable through error monitoring alone. Practitioners should add explicit speed assertions or usage monitoring to detect the fallback. The migration path is to `claude-opus-4-8` or `claude-opus-4-7` with `speed: "fast"`.

### Claim 9: Claude Opus 4.8 is around four times less likely than Opus 4.7 to allow flaws in code it has written to pass unremarked — a measurable improvement in code honesty for agentic coding workflows

- **Evidence**: From the Anthropic Claude Opus 4.8 announcement page (`anthropic.com/news/claude-opus-4-8`), linked from Willison's companion notes post, which is linked from the main source. Backed by Anthropic's internal evaluation data.
- **Confidence**: emerging (specific metric from Anthropic's own evaluation; methodology not fully described in the announcement)
- **Quote**: "Opus 4.8 is around four times less likely than its predecessor to allow flaws in code it has written to pass unremarked." (from linked Anthropic Opus 4.8 announcement)
- **Our assessment**: The "allowing flaws to pass unremarked" failure mode is specifically relevant for agentic coding workflows where the model reviews its own code. If the model doesn't flag its own bugs, the human reviewer must catch them. A 4x improvement in self-critical code review is a meaningful capability claim that affects how much trust practitioners can place in unattended agentic code generation. The "around four times" qualifier acknowledges imprecision in the evaluation.

### Claim 10: The llm-anthropic 0.25.1 release is likely the "updated llm-anthropic plugin with streaming event support" required by LLM 0.32a0's new typed streaming parts architecture

- **Evidence**: Cross-reference: `blog-simonwillison-llm032a0.md` Concrete Artifacts section explicitly notes that the CLI reasoning display example `llm -m claude-sonnet-4.6 '...' -o thinking_display 1` "requires updated llm-anthropic plugin with streaming event support." llm-anthropic 0.25.1 was released on May 28, 2026 — approximately one month after LLM 0.32a0 alpha (April 29, 2026). The main source does not explicitly state this dependency, but timing is consistent.
- **Confidence**: emerging (inferred from timing and cross-reference; not explicitly stated in the main source)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: LLM 0.32a0 introduced typed streaming parts (reasoning tokens, tool call names, tool call args as separate event types) and its documentation noted the need for an updated llm-anthropic plugin. llm-anthropic 0.25.1 is the most likely candidate for this update. If confirmed, this means 0.25.1 is also the release that enables `-o thinking_display 1` for Claude models in the LLM 0.32a0 architecture. Practitioners who upgraded to LLM 0.32a0 should also upgrade llm-anthropic to 0.25.1 to unlock the full streaming events experience (reasoning token display, fast mode, etc.).

## Concrete Artifacts

### Release note bullets (verbatim from simonwillison.net/2026/May/28/llm-anthropic/)

```
* New model: Claude Opus 4.8 (claude-opus-4.8).
* New -o fast 1 option for fast mode, for organizations with that feature
  enabled on their account.
* Default max_tokens for each model now defaults to that model's maximum
  output rather than 8,192. #72
```

*Source: Simon Willison, simonwillison.net/2026/May/28/llm-anthropic/*

### CLI usage patterns for llm-anthropic 0.25.1

```bash
# Access Claude Opus 4.8 via llm CLI
llm -m claude-opus-4.8 'Your prompt here'

# Enable fast mode (requires org to have fast mode enabled on account)
llm -m claude-opus-4.8 -o fast 1 'Your prompt here'

# Set explicit max_tokens to preserve cost-capping behavior from pre-0.25.1
llm -m claude-opus-4.8 --max-tokens 8192 'Your prompt here'
```

*Source: simonwillison.net/2026/May/28/llm-anthropic/ (first two patterns); --max-tokens flag is standard llm CLI interface*

### Anthropic fast mode API usage (from fast mode documentation, linked from release note)

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    speed="fast",
    betas=["fast-mode-2026-02-01"],
    messages=[
        {"role": "user", "content": "Refactor this module to use dependency injection"}
    ],
)

print(response.content[0].text)
```

*Source: Anthropic fast mode documentation, platform.claude.com/docs/en/build-with-claude/fast-mode (linked from release note)*

### Fast mode pricing table (from Anthropic fast mode documentation, linked from release note)

```
Model                         Input        Output
---------------------------------------------------
Claude Opus 4.6/4.7 (fast)   $30 / MTok   $150 / MTok
Claude Opus 4.8 (fast)       $10 / MTok   $50 / MTok

Standard Opus 4.8 pricing:   $5 / MTok    $25 / MTok
```

*Source: platform.claude.com/docs/en/build-with-claude/fast-mode pricing table*

### Fast mode rate limit response headers (from Anthropic fast mode documentation)

```
anthropic-fast-input-tokens-limit     — Maximum fast mode input tokens per minute
anthropic-fast-input-tokens-remaining — Remaining fast mode input tokens
anthropic-fast-input-tokens-reset     — Time when the fast mode input token limit resets
anthropic-fast-output-tokens-limit    — Maximum fast mode output tokens per minute
anthropic-fast-output-tokens-remaining — Remaining fast mode output tokens
anthropic-fast-output-tokens-reset    — Time when the fast mode output token limit resets
```

*Source: platform.claude.com/docs/en/build-with-claude/fast-mode rate limits section*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-llm032a0.md` Concrete Artifacts section (CLI reasoning display example, lines 256–258): That note's example `llm -m claude-sonnet-4.6 'Think about 3 cool dogs then describe them' -o thinking_display 1` is annotated "requires updated llm-anthropic plugin with streaming event support." llm-anthropic 0.25.1 is the likely plugin update that supplies this streaming event support, confirming the dependency noted there.
  - `blog-simonwillison-llm031.md` Claim 1 (lines 26–31): The prior `llm` release (0.31) documents the same pattern — a version bump that adds a specific model to the base `llm` package via a single release bullet. llm-anthropic 0.25.1 follows the identical release cadence pattern.
  - `blog-simonwillison-llm-openrouter-06.md` Claim 1 (lines 27–30): The `llm-openrouter` 0.6 release is a structural parallel — same plugin release-note format, same brief announcement style. Both are incremental tooling releases in the `llm` ecosystem.

- **Contradicts**: None identified. The max_tokens default change is a documented update, not a conflict with any prior corpus claim. No existing note claims 8,192 as the correct permanent default for `llm-anthropic`; the prior behavior was implicit.

- **Extends**:
  - `blog-simonwillison-llm032a0.md`: LLM 0.32a0 introduced typed streaming parts and noted that `llm-anthropic` would need updating for streaming event support. llm-anthropic 0.25.1 is most likely that update. Together, the two notes document the full chain: `llm` library architectural change (0.32a0) → dependent plugin update (llm-anthropic 0.25.1) → practitioner-visible features (reasoning display, fast mode, Opus 4.8).
  - `blog-simonwillison-llm031.md`: Prior `llm` CLI release (0.31) documents GPT-5.5 and verbosity flags. llm-anthropic 0.25.1 is the Anthropic-side equivalent of the same rapid incremental tooling cadence responding to model and API changes.

- **Novel**:
  - **First in-corpus documentation of the `llm` CLI interface to Anthropic's fast mode feature**: The `-o fast 1` option is the first documented CLI primitive for accessing fast mode from the `llm` tool. No prior corpus note documents fast mode access via any CLI tool.
  - **First in-corpus documentation of the max_tokens behavior change** (from 8,192 fixed to model-maximum): This is a breaking change for existing `llm-anthropic` callers that did not set `--max-tokens` explicitly. Not documented elsewhere in the corpus.
  - **First in-corpus documentation of the prompt cache invalidation constraint of fast mode**: The "fast and standard speed do not share cached prefixes" constraint has significant cost implications for fallback patterns. Not documented elsewhere in the corpus.
  - **First in-corpus documentation of the Opus 4.6 fast mode deprecation timeline and silent fallback behavior**: The 30-day removal window and silent standard-speed fallback (no error) are new practitioner-relevant operational information.
  - **First in-corpus access path for Claude Opus 4.8 via the `llm` CLI**: Prior corpus notes document Opus 4.8 availability via the Anthropic REST API; this is the first note documenting the CLI-level access path via the `llm-anthropic` plugin.

## Guide Impact

- **Chapter 01 (Daily Workflows — `llm` CLI Tooling)**: If the guide documents the `llm -m <model> 'prompt'` pattern for Anthropic models:
  1. Add `claude-opus-4.8` as the current Opus model identifier for `llm` CLI usage after installing llm-anthropic ≥0.25.1.
  2. Add `-o fast 1` as the CLI flag for fast mode (note the account access requirement — research preview).
  3. **Migration warning** for the max_tokens default change: code not setting `--max-tokens` explicitly will now request up to the model's full max output (128,000 tokens for Opus 4.8) instead of 8,192. Practitioners upgrading from ≤0.25 should add `--max-tokens 8192` (or another explicit limit) if cost control matters.

- **Chapter 03 (Using LLM APIs — Accessing Anthropic Models)**:
  1. Add fast mode as a speed/cost tradeoff: 2.5x OTPS improvement; Opus 4.8 fast mode priced at $10/$50 per MTok (2x standard, 3x cheaper than prior Opus fast mode); available only via direct Anthropic API (not Vertex AI/Bedrock/Foundry at launch).
  2. **Cache invalidation caveat**: fast mode and standard speed requests do not share cached prefixes. Fallback patterns from fast → standard incur a full cache miss penalty on every fallback — this significantly reduces fast mode's cost advantage for workloads with large cached prompts.
  3. For practitioners doing Opus 4.6 fast mode migration: the deprecation produces no error — only a silent downgrade to standard speed. Add speed field assertions or usage monitoring to detect the fallback.

- **Chapter 04 (Build-time Patterns — Plugin Ecosystem / `llm` Tool Integrations)**: Document the `llm-anthropic` plugin as the `llm` CLI's access layer to Claude models. The 0.25.1 release is the version that adds Opus 4.8, fast mode, and model-maximum max_tokens defaults. This connects guide CLI tooling coverage to the LLM 0.32a0 streaming architecture documented in `blog-simonwillison-llm032a0.md`.

## Extraction Notes

- **Source is three bullet points**: The main simonwillison.net page is a brief "beat" post (< 100 words). The extraction depth comes from two linked pages followed per the MINER rubric:
  1. **Anthropic fast mode documentation** (`platform.claude.com/docs/en/build-with-claude/fast-mode`): Full page fetched via WebFetch; contains code examples in multiple languages, pricing tables, rate limit headers, and a Considerations section. Claims 4–8 are sourced primarily from this page.
  2. **Anthropic Opus 4.8 announcement** (`anthropic.com/news/claude-opus-4-8`): Fetched via WebFetch; returned structured verbatim content including practitioner testimonials with named people and organizations. Claim 9 and the fast mode price comparison in Claim 5 are sourced from this page.
  3. A third linked page (Willison's companion Opus 4.8 notes post) was fetched but the WebFetch returned a summarized result; used for context but not quoted directly.
- **Quote fidelity**: All three bullet quotes from the main simonwillison.net source are verbatim from the full page fetch. Quotes from the fast mode docs and Opus 4.8 announcement are from WebFetch results; the fast mode docs content appears verbatim (structured documentation with code blocks and tables is unlikely to be paraphrased by a summarizing model). The Assayer should spot-check linked-page quotes against their URLs (`platform.claude.com/docs/en/build-with-claude/fast-mode` and `anthropic.com/news/claude-opus-4-8`) if any doubt arises.
- **Claim 10 is inferred**: The connection between llm-anthropic 0.25.1 and the LLM 0.32a0 streaming events dependency is an inference from timing and the explicit note in `blog-simonwillison-llm032a0.md`'s Concrete Artifacts section. The main source does not state this relationship explicitly.
- **Fragment URL**: The issue body includes `#atom-everything` (Atom feed anchor). `source_url` uses the canonical page URL without the fragment, consistent with prior Willison notes in this corpus (see `blog-simonwillison-llm032a0.md` extraction notes).
- **Cross-reference verification performed**:
  - `blog-simonwillison-llm032a0.md` Concrete Artifacts section (lines 256–258) confirmed: CLI command with annotation "requires updated llm-anthropic plugin with streaming event support."
  - `blog-simonwillison-llm031.md` Claim 1 (lines 26–31) confirmed: native GPT-5.5 CLI access pattern via single release bullet.
  - `blog-simonwillison-llm-openrouter-06.md` Claim 1 (lines 27–30) confirmed: `llm openrouter refresh` command as sole release change, same brief-announcement format.
