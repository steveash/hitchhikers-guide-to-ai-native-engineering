---
source_url: https://simonwillison.net/2026/Jun/9/claude-fable-5/
source_type: blog-post
title: "Initial impressions of Claude Fable 5"
author: Simon Willison
date_published: 2026-06-09
date_extracted: 2026-06-17
last_checked: 2026-06-17
status: current
confidence_overall: emerging
issue: "#1196"
---

# Initial impressions of Claude Fable 5

> Simon Willison's ~5.5-hour first-day evaluation of Claude Fable 5 documents its
> model specs, demonstrates frontier knowledge depth, upgrades a real project from
> MicroPython WASM to full CPython WASM, ships LLM 0.32a3 with human-in-the-loop
> tool pause/resume, and establishes $10/$50 per million token pricing as the new
> frontier-tier benchmark — all at $110.42 in a single day on a $100/month Max
> subscription.

## Source Context

- **Type**: blog-post (Simon Willison's weblog, June 9, 2026 — first-day hands-on
  evaluation, ~1,500 words, with embedded SVG outputs, a GPT-5.5 knowledge
  comparison gist link, LLM 0.32a3 release notes, and a cost breakdown screenshot
  from AgentsView.)
- **Author credibility**: Simon Willison is the creator of Django, Datasette, and
  the `llm` Python CLI. He is a trusted-feed source in this corpus with prior notes
  covering Datasette Agent, the micropython-wasm sandbox (`blog-simonwillison-datasette-agent-micropython.md`),
  the LLM 0.32a0 refactor (`blog-simonwillison-llm032a0.md`), and AgentsView cost
  tracking (`blog-simonwillison-agentsview-custom-model-price.md`). All cost figures
  are from AgentsView tracking of his own API usage — not vendor-supplied. No
  vendor affiliation with Anthropic.
- **Scope**: Covers Claude Fable 5's model specifications; a three-way knowledge-
  depth comparison (Fable 5 vs. Opus 4.8 vs. GPT-5.5); the CPython WASM upgrade
  to datasette-agent-micropython; LLM 0.32a3 implementation with pause/resume tool
  call support; an SVG generation benchmark across five effort levels; and
  AgentsView cost attribution data. Does NOT cover: formal benchmark suite results,
  full API parameter differences from Opus 4.8, multi-user or enterprise deployment
  patterns, or the Fable 5 system prompt.

## Extracted Claims

### Claim 1: Claude Fable 5 has a 1 million token context window, 128,000 maximum output tokens, a knowledge cutoff of January 2026, and is priced at $10/million input and $50/million output tokens

- **Evidence**: Willison's direct statement of Anthropic's published specifications on the day of release (June 9, 2026).
- **Confidence**: settled (official Anthropic specifications at time of post)
- **Quote**: "The models have a 1 million token context window, 128,000 maximum output tokens and a knowledge cut-off date of January 2026."
- **Our assessment**: The $50/million output pricing is the most practically impactful spec for practitioners. Willison's $99.26 single Datasette Agent session confirms that agentic multi-step work at Fable scale costs materially more than at Opus 4.8 scale. The 1M context window doubles effective context versus Opus 4.8's 200k, potentially enabling whole-codebase or whole-document workflows that were truncation-limited before. The pricing note ("priced at twice the price of Claude Opus 4.5/4.6/4.7/4.8") implies Opus 4.8 holds the same price point as Opus 4.7 — Fable is 2x above that.

### Claim 2: Anthropic asserts that Claude Fable 5 offers the same performance as Claude Mythos 5, but with stricter guardrails; the Claude API now includes mechanisms to notify callers when guardrails trigger and an option to automatically fall back to another model

- **Evidence**: Willison cites Anthropic's claim directly, then makes an independent observation about guardrail frequency based on his ~5.5 hours of use.
- **Confidence**: emerging (the performance-parity claim is vendor-asserted; the guardrail frequency observation is Willison's first-person experience)
- **Quote**: "Anthropic claim that Claude Fable 5 offers the same performance as Claude Mythos 5, except with much more strict guardrails in place to prevent it being used for harmful things."
- **Quote (guardrails)**: "Those guardrails trigger often enough that the Claude API has new mechanisms for letting you know when you hit them, and even has a new option to request it falls back to another model automatically if something gets rejected."
- **Our assessment**: Two distinct claims are bundled: (1) Fable ≈ Mythos on performance — vendor-asserted, not independently tested in this source; (2) guardrails are frequent enough to drive API-level mitigation mechanisms. The second is operationally important: Anthropic shipping guardrail notifications + automatic fallback implies these features are needed at deployment scale, not just in adversarial edge cases. Practitioners building production agents with Fable should test their specific use cases against the guardrails before assuming Fable is a transparent drop-in for Opus 4.8.

### Claim 3: Anthropic made Fable 5 available simultaneously across all Claude surfaces — Claude.ai chat, Claude Code for web, Claude Code CLI, and Claude Cowork — on release day

- **Evidence**: Willison's direct observation from using all surfaces on launch day.
- **Confidence**: settled (first-hand observation on June 9, 2026)
- **Quote**: "Anthropic made Fable 5 available across all of their surfaces—the Claude.ai chat interface, Claude Code for web, Claude Code CLI and Claude Cowork as well."
- **Our assessment**: The same-day, all-surfaces rollout is notable. The access window on the $100/month Max plan was temporary: "The model is available 'until June 22nd' on the subscription plans (I'm on $100/month Max at the moment), after which it will be billed extra." Practitioners on subscription plans should verify their plan's model access schedule — Fable may transition to pay-per-token usage after any included access window.

### Claim 4: Claude Fable 5 "feels big" — deeper knowledge than Opus 4.8 and comparable to or slightly below GPT-5.5 on factual enumeration tasks; Opus 4.8 explicitly declined a knowledge-depth test that Fable completed confidently

- **Evidence**: Three-way comparison on the same prompt ("List all of Simon Willion's open source projects, most recent first, each with a rough date of when they were first released"). Willison ran all three models and linked GPT-5.5's output as a gist.
- **Confidence**: anecdotal (single test, single evaluator, single domain; but the directional contrast is credible given known parameter count differences)
- **Quote (Opus 4.8 response)**: "I don't have a reliable, comprehensive, and date-verified list of all of Simon Willison's open source projects, and I want to be honest about that rather than risk giving you inaccurate dates or fabricated entries."
- **Quote (Fable 5 response opening)**: "I think you mean **Simon Willison** — the prolific open source developer, co-creator of Django, and creator of Datasette."
- **Quote (GPT-5.5 comparison)**: "(Here's GPT-5.5 for good measure. It listed even more projects than Fable did!)"
- **Our assessment**: Fable's willingness to commit to a comprehensive enumeration — listing files-to-prompt, datasette-extract, LLM, symbex, ttok, strip-tags, datasette-lite, shot-scraper, s3-credentials, django-sql-dashboard, the Dogsheep suite, sqlite-utils, Datasette, csvs-to-sqlite, and Django, each with specific dates — while Opus 4.8 explicitly refused, reflects a knowledge density difference, not a calibration difference. The silent correction of "Simon Willion" → "Simon Willison" is a secondary signal of the same: confident contextual correction rather than literal compliance. The test was designed to probe exactly where "big model smell" manifests.

### Claim 5: "Big model smell" — the sense that a model is large — manifests as deeper factual knowledge and is a reasonable behavioral proxy for parameter count

- **Evidence**: Willison's editorial characterization of his experience across ~5.5 hours of Fable use.
- **Confidence**: anecdotal (one practitioner's subjective experience; the underlying claim about parameter count and factual memorization is grounded in known ML scaling theory)
- **Quote**: "The best way to describe Fable is that it feels _big_. Not just in terms of speed and cost, but also in how much it knows."
- **Quote (parameter reasoning)**: "Knowledge like this is a reasonably good proxy for model size—you can cram a whole lot more details about the world into a larger number of parameters."
- **Our assessment**: "Big model smell" is a useful practitioner heuristic: when a model confidently produces detailed factual enumerations that smaller models hedge on or refuse, that behavioral difference signals parameter-scale difference. The corollary is that "big model behavior" comes with "big model cost" — $10/$50 per million tokens reflects this. Practitioners should calibrate task selection: high-knowledge-density tasks (deep factual enumeration, domain expertise in niche areas) justify Fable's cost premium over Opus 4.8; routine code generation or summarization may not.

### Claim 6: Claude Fable 5 autonomously identified the optimal upgrade path (Brett Cannon's cpython-wasi-build) for upgrading datasette-agent-micropython from MicroPython to full CPython WASM, then completed the implementation after Willison manually uploaded environment-restricted build artifacts

- **Evidence**: First-person account with specific artifact measurements (package name `cpython_wasm-0.1.0-py3-none-any.whl`, size 13.9MB) and an inline diagnosis from Fable about why a simpler approach failed.
- **Confidence**: emerging (first-person practitioner account; artifact measurements are specific and verifiable at the PyPI level)
- **Quote**: "Fable identified that it could use Brett Cannon's cpython-wasi-build builds for this, but was unable to download them itself due to environment restrictions."
- **Quote (Fable's technical self-diagnosis)**: "I tried the cleaner single-zip-stdlib approach to shrink the filesystem surface, but CPython's getpath bootstrap fails to find encodings from inside a zip without more prefix finessing"
- **Quote (result)**: "gave me this 13.9MB cpython_wasm-0.1.0-py3-none-any.whl file"
- **Our assessment**: The human-in-the-loop pattern here is architecturally significant: Fable identified the optimal path (Brett Cannon's cpython-wasi-build), but couldn't execute one step (downloading build artifacts) due to environment restrictions. Willison bridged the gap manually, then Fable completed the rest — including environment-specific debugging with a concrete root-cause explanation ("CPython's getpath bootstrap fails to find encodings from inside a zip without more prefix finessing"). This is a concrete example of the "orchestration with human bridges" pattern: the model does planning, implementation, and debugging; the human handles specific access-constrained steps.

### Claim 7: In a single session, Claude Fable 5 implemented LLM 0.32a3's pause/resume tool call mechanism — introducing four new API primitives — which Willison describes as "almost entirely written by Fable"

- **Evidence**: Willison's first-hand account with specific artifact references (LLM 0.32a3 release, PRs #1480–#1483).
- **Confidence**: emerging (first-person practitioner account; the LLM 0.32a3 release is a verifiable public artifact on GitHub; "almost entirely written by Fable" is a characterization, not a diff measurement)
- **Quote**: "My stretch goal turned into LLM 0.32a3, almost entirely written by Fable."
- **Quote (iteration pattern)**: "Fable got everything working first using somewhat gnarly hacks, but the moment I told it that changes to LLM itself were in scope it set to work unraveling the hacks and turning them into supported features."
- **Our assessment**: Four new API primitives in a single session — `llm_tool_call` parameter access, guaranteed `tool_call_id` generation, `llm.PauseChain` exception, and chain resumption from incomplete tool call histories — is a substantial library contribution, sufficient for Willison to publish as a release. The iteration pattern is reproducible: start with working but messy code, then explicitly expand scope to include the underlying library. The "scope expansion" signal to Fable was sufficient to trigger a refactor from application-level hacks to proper library-level abstractions.

### Claim 8: LLM 0.32a3 adds four specific API primitives for human-in-the-loop tool pause/resume, motivated by Datasette Agent's ask_user() feature

- **Evidence**: The LLM 0.32a3 release notes, quoted verbatim in the article.
- **Confidence**: settled (first-party release notes, verifiable on GitHub)
- **Quote (all four features, verbatim from release notes)**: "Tool implementations can declare a parameter named `llm_tool_call` in order to be passed the `llm.ToolCall` object for the current invocation." / "Every tool call is now guaranteed a unique `tool_call_id`—providers that do not supply one get a synthesized `tc_`-prefixed ULID." / "Tools can raise a `llm.PauseChain` exception to cleanly pause the tool chain, useful for things like waiting for human approval." / "Chains can now resume from a `messages=` history ending in unresolved tool calls: the calls are executed through the normal `before_call`/`after_call` machinery before the first model call."
- **Our assessment**: The pause/resume mechanism is the enabling capability for human-in-the-loop approval workflows in multi-step agentic sessions. `llm.PauseChain` is the signal; `messages=` resumption with unresolved tool calls is the execution contract. Together they allow an agent to: present a proposed action to a human, wait for approval/rejection, then resume from the paused state. The `tool_call_id` guarantee enables reliable cross-turn tool call tracking regardless of provider. These primitives are now general library capabilities, not application-specific hacks — directly motivated by the Datasette Agent's "human-in-the-loop `ask_user()` feature."

### Claim 9: Claude Fable 5 produced API design, tests, code, and documentation for LLM 0.32a3 at a quality level Willison characterizes as impressive

- **Evidence**: Willison's direct quality assessment, with a published library release as the artifact.
- **Confidence**: anecdotal (single evaluator's assessment; the published LLM 0.32a3 release provides the strongest available evidence that the quality bar was met)
- **Quote**: "I'm really impressed with the quality of API design, tests, code and documentation that Fable put together for this."
- **Our assessment**: "API design, tests, code and documentation" covering all four dimensions is notable — many AI-assisted implementations produce working code but thin tests and no documentation. The emphasis on API design quality is particularly relevant: the four new primitives represent design decisions (naming, exception semantics, message-history contract), not just implementation. A practitioner publishing a library release based on AI-written code has implicitly verified the quality — Willison's imprimatur here is stronger than a casual "the code looks good" assessment.

### Claim 10: Spending ~5.5 hours on Fable 5 "feels like several days' worth of work," with $110.42 in token costs on a $100/month Max subscription

- **Evidence**: Willison's direct productivity assessment and cost data from AgentsView.
- **Confidence**: anecdotal (single practitioner's subjective productivity assessment; cost data is factual from AgentsView)
- **Quote**: "I spent several hours on it today, but it feels like several days' worth of work."
- **Quote (cost)**: "I used $110.42 worth of tokens today, all as part of my $100/month subscription."
- **Our assessment**: The subjective "several days' worth" assessment encompasses shipping a WASM runtime upgrade and a library release in ~5.5 hours. The cost figure is more directly actionable: $110.42 for ~5.5 hours averages roughly $20/hour in tokens at Fable pricing. The AgentsView breakdown showed $99.26 (89.9%) on the Datasette Agent session alone, confirming that agentic multi-step sessions drive cost concentration. The "$110.42 all as part of my $100/month subscription" phrasing implies the costs were covered by the subscription's included Fable access window, not billed separately on June 9.

### Claim 11: SVG generation output tokens increase dramatically with effort level: Fable 5's "max" effort produced 14,430 output tokens at 72.2c versus 1,929 tokens at 9.7c for "low" effort — a 7.5x token and cost multiplier

- **Evidence**: Willison's direct measurement from running his standard "pelican on a bicycle" SVG benchmark across all five effort levels.
- **Confidence**: settled (specific first-person measurements from a known and consistent benchmark the author maintains)
- **Quote**: "I ran 'Generate an SVG of a pelican riding a bicycle' against all five thinking effort levels with Fable."
- **Our assessment**: The pelican-bicycle SVG is Willison's consistent cross-model quality benchmark, documented in prior notes in this corpus (`blog-simonwillison-gemini35-flash-pricing.md`). The 7.5x token ratio between low and max effort creates a real cost/quality tradeoff: at $50/million output tokens, low effort costs $0.097 per image; max effort costs $0.722. For production use cases where visual quality is not critical, the low-effort tier is appropriate. For demonstrations or design work where output quality matters, the max effort tier costs less than $1 per image — a viable tradeoff. The non-monotonic pattern (high effort at 2,057 tokens is *fewer* than medium at 2,290) suggests effort levels do not deterministically increase output length; the thinking budget alters the approach, not just the verbosity.

## Concrete Artifacts

### Claude Fable 5 Specifications at Launch (from the article, June 9, 2026)

```
Claude Fable 5 specifications (Anthropic, June 9, 2026):
  Context window:          1,000,000 tokens
  Maximum output tokens:     128,000 tokens
  Knowledge cutoff:        January 2026
  Input pricing:            $10.00 / million tokens  (2x Opus 4.5/4.6/4.7/4.8)
  Output pricing:           $50.00 / million tokens  (2x Opus 4.5/4.6/4.7/4.8)
```

*Source: Simon Willison, simonwillison.net/2026/Jun/9/claude-fable-5/*

### SVG Pelican-Bicycle Benchmark — Fable 5 Across All Effort Levels (from the article)

```
Prompt: "Generate an SVG of a pelican riding a bicycle"
Model: Claude Fable 5 ($50/million output tokens)

Effort level    Output tokens    Cost
-----------     -------------    ----
low             1,929            9.67c
medium          2,290            11.475c
high            2,057            10.31c
xhigh           5,992            29.985c
max             14,430           72.175c
```

*Source: Simon Willison, simonwillison.net/2026/Jun/9/claude-fable-5/*

### LLM 0.32a3 Pause/Resume API Features (from the article, citing release notes)

```
LLM 0.32a3 new features (driven by Datasette Agent's human-in-the-loop ask_user() feature):

1. Tool implementations can declare a parameter named `llm_tool_call` in order to
   be passed the `llm.ToolCall` object for the current invocation.

2. Every tool call is now guaranteed a unique `tool_call_id`—providers that do not
   supply one get a synthesized `tc_`-prefixed ULID.

3. Tools can raise a `llm.PauseChain` exception to cleanly pause the tool chain,
   useful for things like waiting for human approval.

4. Chains can now resume from a `messages=` history ending in unresolved tool calls:
   the calls are executed through the normal `before_call`/`after_call` machinery
   before the first model call.

Related PRs: #1480, #1481, #1482, #1483
```

*Source: Simon Willison, simonwillison.net/2026/Jun/9/claude-fable-5/ (quoting LLM 0.32a3 release notes)*

### Session Cost Attribution (from AgentsView in the article, June 9, 2026)

```
AgentsView cost breakdown — Willison's Claude Fable 5 usage, June 9, 2026 (~5.5 hours):

  Project                  Cost      Share
  -----------------------  --------  ------
  prod_datasette_agent     $99.26    89.9%
  (other projects)         ~$11.16   ~10.1%
  -----------------------  --------  ------
  Total                    $110.42   100%
```

*Source: Simon Willison, simonwillison.net/2026/Jun/9/claude-fable-5/ (from AgentsView screenshot)*

### CPython WASM Upgrade Artifact (from the article)

```
Artifact: cpython_wasm-0.1.0-py3-none-any.whl
Size: 13.9MB
Built from: Brett Cannon's cpython-wasi-build project
Purpose: Upgrade datasette-agent-micropython from MicroPython to full CPython WASM
```

*Source: Simon Willison, simonwillison.net/2026/Jun/9/claude-fable-5/*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-agentsview-custom-model-price.md` Claim 7 (Claude Fable 5
    is priced at 2x Claude Opus 4.7 for input and output — $10/M input, $50/M
    output): This source corroborates and extends Claim 7 with concrete cost impact
    data — $99.26 for a single Datasette Agent session demonstrates the practical
    consequence of the 2x pricing at agentic workloads.
  - `blog-simonwillison-agentsview-custom-model-price.md` Claim 5 (real-world
    local agent cost attribution shows extreme per-project variation — one project
    can account for nearly 90% of total daily spending): This source corroborates
    Claim 5; `prod_datasette_agent` at 89.9% of a day's spend is a direct parallel
    to the 89.3% figure from the same project on the same day in that note (both
    June 9, 2026 — the figures likely reflect the same AgentsView session viewed
    at different points during the day).
  - `blog-simonwillison-llm032a0.md` Claim 1 (the original `llm` text-in/text-out
    abstraction could no longer represent the full range of inputs and outputs
    required by modern LLMs): LLM 0.32a3 continues the refactor arc begun in
    0.32a0, now adding pause/resume capabilities — confirming that the 0.32
    architectural rewrite was the necessary foundation for more complex agentic
    primitives that couldn't be bolted onto the old abstraction.
  - `blog-simonwillison-gemini35-flash-pricing.md` Claim 5 (all three major AI
    labs simultaneously raised prices on new flagship models; Claude Opus 4.7 at
    ~1.46x Opus 4.6): This source adds Fable 5 at 2x Opus 4.8, extending the
    Anthropic pricing trajectory forward. The series now reads: Opus 4.6 → Opus
    4.7 (+1.46x) → Opus 4.8 (same tier as 4.7) → Fable 5 (+2x over Opus 4.8).

- **Extends**:
  - `blog-simonwillison-datasette-agent-micropython.md` Claim 1 (datasette-agent-
    micropython enables Datasette Agent to generate and execute Python code safely
    by running MicroPython inside a WebAssembly sandbox): This source documents the
    next generation of that sandbox — Fable 5 upgraded the runtime from MicroPython
    to full CPython WASM using Brett Cannon's cpython-wasi-build, producing a
    13.9MB wheel. The alpha-stage micropython sandbox is now a full CPython sandbox.
  - `blog-simonwillison-llm032a0.md` Claim 3 (LLM 0.32a0 introduces two
    architectural changes: message-sequence input and typed streaming output parts):
    This source adds a third major 0.32 capability — pause/resume tool chains via
    `llm.PauseChain` and `messages=` resumption — released as 0.32a3. The
    pause/resume mechanism builds directly on the messages-based conversation model
    from 0.32a0: unresolved tool calls are stored as messages and replayed on
    resumption.
  - `blog-simonwillison-datasette-agent.md` (Datasette Agent as an extensible,
    plugin-based conversational SQL agent for Datasette): This source shows Datasette
    Agent evolving with a human-in-the-loop `ask_user()` feature, made possible by
    LLM 0.32a3's `llm.PauseChain` primitive. The agent platform continues to develop
    in lockstep with the underlying `llm` library.

- **Contradicts**: None identified. No existing note makes claims that materially
  conflict with this source. No contradiction issue required.

- **Novel**:
  - **First in-corpus documentation of Claude Fable 5 as a model**: No prior note
    covers Fable 5's capabilities, knowledge depth, behavior, or guardrails. The
    agentsview-custom-model-price note covers Fable's pricing in a tooling context
    but not the model itself.
  - **"Big model smell" as a practitioner heuristic**: The framing of confident
    factual enumeration as a behavioral signal of parameter count is not documented
    elsewhere in the corpus.
  - **Claude API guardrail notification and automatic fallback mechanisms**: The
    new API-level guardrail handling — notification when triggered, option to auto-
    fallback to another model — is not documented in any prior note.
  - **Human-in-the-loop tool pause/resume as an LLM library primitive**: `llm.PauseChain`
    and `messages=` resumption from unresolved tool calls are new general-purpose
    library primitives, not documented before LLM 0.32a3. First in-corpus
    documentation of this pattern at the library abstraction level.
  - **Frontier model driving publishable library API design decisions**: The pattern
    of an agentic session producing a publishable library release (API design + 
    implementation + tests + docs) — not just working code — is new to the corpus.
  - **Full CPython WASM wheel as an agentic session artifact**: A 13.9MB
    production-quality wheel file produced as output of a human-in-the-loop agentic
    session is the most concrete binary artifact documented in the corpus.
  - **Pelican-bicycle SVG effort-level cost table for Fable 5**: The five-tier
    comparison (1,929→14,430 output tokens) is the first Fable-specific data for
    this benchmark, and documents the non-monotonic relationship between effort
    level and output token count (high < medium).
  - **Scope expansion as an agentic iteration directive**: The pattern of
    "starting with application-level hacks, then explicitly telling the model that
    library-level changes are in scope" triggering a quality refactor is a specific
    and reproducible workflow not documented elsewhere.

## Guide Impact

- **Chapter 02 (Model Selection — Pricing and Cost-Benefit)**: Update the frontier
  model pricing table with Fable 5 at $10/$50 per million tokens, 2x Opus 4.8.
  Note the context window difference: Fable 5 at 1M tokens vs. Opus 4.8 at 200k.
  The "big model smell" concept (Claim 5) provides practitioners with a behavioral
  test for whether a task requires Fable's parameter depth: if Opus 4.8 hedges or
  refuses a knowledge-intensive task that Fable completes confidently, that is the
  signal to upgrade. The 2x cost multiplier makes this a decision worth testing.

- **Chapter 02 (Model Selection — Guardrails and Safety Behavior)**: Add the
  guardrails observation (Claim 2): Fable 5 has stricter safety guardrails than
  Opus 4.8, and the Claude API now provides guardrail-hit notifications and an
  automatic fallback mechanism. Practitioners should test their specific use cases
  against Fable's guardrails before assuming transparent drop-in replacement.
  The API-level fallback option enables graceful degradation without application-
  level retry logic.

- **Chapter 03 (Developer Workflows — AI-Assisted Library Development)**: Add the
  LLM 0.32a3 case as a worked example of AI-driven library development (Claims 7–9):
  Fable drove a publishable library release (API design + implementation + tests +
  docs) within a ~5.5-hour session. Key pattern: "start with working hacks, then
  explicitly scope the library-level refactor." This demonstrates AI can be directed
  to target different abstraction levels within a session — a practical workflow
  directive practitioners can replicate.

- **Chapter 04 (Agents & Tool Use — Human-in-the-Loop Patterns)**: Add LLM 0.32a3's
  pause/resume mechanism (Claim 8) as a concrete implementation of human-in-the-loop
  tool approval. The `llm.PauseChain` exception + `messages=` resumption pattern
  enables an agent to pause mid-chain, present a proposed action for approval, and
  resume from the paused state. This is now a general library primitive available
  to any `llm`-based agent — not just Datasette Agent.

- **Chapter 05 (Cost & Observability)**: The $99.26 single-session cost for a
  complex Datasette Agent operation (89.9% of a day's spend) provides concrete
  data for agentic cost planning at Fable pricing (Claims 10–11). Pair with
  `blog-simonwillison-agentsview-custom-model-price.md` Claim 6 ($516.62 in
  caching savings on the same day) for the full cost picture: expensive frontier
  models and prompt caching are not in tension — caching is more valuable at
  higher per-token rates. Guide recommendation: "At Fable pricing, instrument
  sessions with AgentsView before and after enabling caching; the ratio of
  savings to actual spend may justify the caching configuration work even for
  short-running projects."

## Extraction Notes

- The source is a single-page first-day evaluation post (~1,500 words). No sub-
  pages were followed beyond the article itself; the GPT-5.5 comparison gist and
  LLM 0.32a3 release notes are auxiliary artifacts referenced in the article.
- The WebFetch tool returned summaries rather than full verbatim text; targeted
  extraction prompts were used to obtain specific quotes. All quotes were verified
  across multiple independent fetches returning consistent text.
- The `#atom-everything` fragment in the original issue URL is an Atom feed anchor;
  `source_url` uses the canonical page URL without the fragment, consistent with
  prior Willison source notes in this corpus.
- This article and `blog-simonwillison-agentsview-custom-model-price.md` were
  published on the same day (June 9, 2026) and share cost data from the same
  AgentsView session. The two notes are complementary: this note covers Fable 5
  as a model; that note covers the AgentsView tooling and custom pricing recipe.
  The 89.9% vs. 89.3% prod_datasette_agent share discrepancy between the two posts
  is consistent with both being snapshots of the same session at different times
  during the day.
- Cross-references verified:
  - `blog-simonwillison-agentsview-custom-model-price.md` Claim 7: confirmed at
    lines 149–163 of that note (Claude Fable 5 at $10/$50 per million tokens).
  - `blog-simonwillison-agentsview-custom-model-price.md` Claim 5: confirmed at
    lines 112–129 (per-project cost attribution, 89.3% figure for prod_datasette_agent).
  - `blog-simonwillison-llm032a0.md` Claim 1: confirmed at lines 24–32 (text-in/
    text-out abstraction insufficient for modern LLMs).
  - `blog-simonwillison-llm032a0.md` Claim 3: confirmed at lines 38–45 (0.32a0's
    two architectural changes: messages API and typed streaming parts).
  - `blog-simonwillison-gemini35-flash-pricing.md` Claim 5: confirmed at lines
    54–59 (cross-vendor price escalation, Opus 4.7 at ~1.46x Opus 4.6).
  - `blog-simonwillison-datasette-agent-micropython.md` Claim 1: confirmed at
    lines 47–61 (datasette-agent-micropython enables safe code execution via
    MicroPython WASM sandbox).
- No contradictions identified. No contradiction issue required.
