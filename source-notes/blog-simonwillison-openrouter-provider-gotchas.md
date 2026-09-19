---
source_url: https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/
source_type: blog-post
title: "So you want to use OpenRouter?"
author: Simon Willison (link-blog), amplifying Mohamed Moustafa (mmoustafa.com)
date_published: 2026-09-11
date_extracted: 2026-09-19
last_checked: 2026-09-19
status: current
confidence_overall: emerging
issue: "#3555"
---

# So you want to use OpenRouter?

> Willison's link-blog post points to Mohamed Moustafa's operational deep-dive
> on OpenRouter's automatic provider-routing behavior — drawn from running
> Olly, an iMessage AI assistant that has transacted over 18 million messages
> (roughly a third on open models via OpenRouter). The post documents ten
> concrete pitfalls (benchmark variance across providers for the same model,
> vision "blind" providers, inconsistent reasoning-effort handling, unreliable
> quantization filters, tool-calls landing as raw text, silent-empty 200
> responses, per-provider history-validation rules, IP-based rate limiting,
> and a fully-pinned three-provider fallback chain that still went down) and
> the concrete API controls (`provider.only`, the `/endpoints` method) that
> mitigate provider heterogeneity.

## Source Context

- **Type**: blog-post (Willison "link blog" format — a ~90-word post pairing
  brief commentary with a link out to Mohamed Moustafa's substantive original
  article, itself surfaced to Willison via a Hacker News discussion). This is
  the same link-blog pattern already documented in this corpus for
  `blog-simonwillison-llm-openrouter-07.md` (where the substantive content
  lived in a linked GitHub README, not the blog post itself) — here the
  substantive content lives in Moustafa's linked article
  (`mmoustafa.com/blog/so-you-want-to-use-openrouter/`, dated September 7,
  2026), which this Miner followed per MINER.md §1 and treats as the primary
  evidentiary source, consistent with that prior note's precedent.
- **Author credibility**: Simon Willison is a widely-cited practitioner
  commentator on LLM tooling already established throughout this corpus
  (creator of Django and the `llm` CLI). His role here is curation/amplification,
  not authorship of the underlying claims. Mohamed Moustafa is the actual
  author of the substantive content: he runs Olly, an AI assistant operating
  inside iMessage, and states it has "transacted over 18 million messages,"
  roughly a third of those routed through OpenRouter to open-weight models —
  this is first-party, high-volume production operational experience, not a
  vendor announcement or a single-session anecdote. His claims are backed by
  his own probing (per-provider benchmark boards pulled from OpenRouter's own
  UI, a controlled vision test across four providers x two models x three
  images, a controlled reasoning-effort sweep across the 23 providers named in the chart legend at three
  effort levels x three calls each, and a two-week production incident with a
  pinned three-provider fallback chain) rather than assertion alone, and he
  links to raw data behind several of his charts (see Concrete Artifacts).
- **Scope**: Covers operational pitfalls specific to OpenRouter's
  provider-routing layer — benchmark variance, vision-capability gaps,
  reasoning-effort handling, quantization-filter reliability, tool-call
  parsing inconsistency, empty/hollow-completion failure modes, per-provider
  history-validation rules, IP-based rate limiting, and fallback-chain
  fragility — illustrated primarily with DeepSeek V4 Flash 0731 and, for one
  pitfall, GLM 5.3 Flash, Qwen3.5 122B, and MiniMax M3. Does NOT cover:
  OpenRouter's business/financial layer (covered by
  `blog-latentspace-ainews-stripe-buys-openrouter.md`), the `llm-openrouter`
  CLI plugin's own feature set (covered by `blog-simonwillison-llm-openrouter-06.md`
  and `-07.md`), pricing comparisons across routing platforms, or any
  provider's serving stack internals beyond what's externally observable
  through OpenRouter's API and benchmark UI.

## Extracted Claims

### Claim 1: "Model" and "provider" are distinct concepts on OpenRouter — a single model ID resolves to roughly 20 different backend companies, each running their own serving stack, precision, and parser, making them "the same model on paper, but very different models in real life"
- **Evidence**: Author's own vocabulary framing, given as necessary context before listing pitfalls, drawn from operating Olly at the stated 18M-message/OpenRouter-routed-open-models scale.
- **Confidence**: settled (a definitional/architectural fact about how OpenRouter's routing works, not a performance claim)
- **Quote**: "The provider is who OpenRouter routes you to, they host the model on their GPUs, at their chosen precision, and their "proprietary" optimizations, with their own XML/tool parsers, which means each has a "proprietary" list of bugs too. When you ask for deepseek/deepseek-v4-flash you get one of ~20 companies you've mostly never heard of. They're the same model on paper, but very different models in real life."
- **Our assessment**: This is the load-bearing framing for every subsequent claim in the post and directly extends the operational-risk angle already flagged in this corpus's triage comments for this issue — it names the root cause (per-provider serving-stack divergence: precision, optimizations, parsers) behind the specific failure modes documented below, rather than treating them as isolated bugs.

### Claim 2: The same model checkpoint benchmarks very differently depending on which OpenRouter provider serves it — for DeepSeek V4 Flash 0731, first-party DeepSeek scored 90.2% GPQA / 81.3% TAU-Bench Airline while DigitalOcean scored 75.3% / 58.4% on the identical weights, with most providers clustering 5–7 points below first-party on tool calling and several falling further on knowledge
- **Evidence**: Author's own aggregation of OpenRouter's own published per-provider benchmark board (GPQA Diamond and TAU-Bench Airline, rolling 32-day average) for `deepseek/deepseek-v4-flash-0731`, captured 2026-09-07, with raw data linked.
- **Confidence**: emerging (a specific, dated, named-provider dataset pulled directly from OpenRouter's own benchmark UI with linked raw data, but not independently re-verified by this Miner, and OpenRouter's own benchmark methodology for that board is not itself audited in this source)
- **Quote**: "First-party DeepSeek: 90% GPQA, 81% TAU. DigitalOcean, same weights: 75% and 58%. Most hosts cluster 5 to 7 points below first-party on tool calling, and four of them fall off a cliff on knowledge. For an agent TAU is the score that matters and a 20 point swing is not noise. (In July it was worse: Fireworks scored 46% on TAU, a 30 point gap)"
- **Our assessment**: This is the post's central, most quantified claim and directly answers the Prospector's triage "key question" about operational gotchas from automatic fallback — a 20-30 point swing on a tool-calling benchmark for what OpenRouter presents as an interchangeable routing target is a materially different agent-reliability outcome depending purely on which provider a given request happened to land on. The author's own framing ("recheck when you switch models, the same providers looked completely different on GLM-5.3") explicitly warns against generalizing any single provider's ranking across models — see Claim 5, which shows the same non-transferability for quantization-to-quality correlation.

### Claim 3: Vision-capable models can have "blind" providers that silently fail image tasks while returning success — DeepInfra's Qwen3.5 122B endpoint misread a letter, misnamed a color, and mislabeled a word across three test images, while four other providers of the same model got all three right; two providers of MiniMax M3 (Venice, Together) reported "no image provided" for images that were actually sent
- **Evidence**: Author's own controlled test — three fixed test images (a letter, a solid color, a word on a background) sent to every host of two vision models, with per-host pass/fail results tabulated.
- **Confidence**: emerging (a small but controlled, direct test — 4 providers x 2 models x 3 images — run and reported by the practitioner himself, with specific per-host failure descriptions; not independently reproduced by this Miner, and the underlying reason for DeepInfra's specific misreadings is not diagnosed in the source)
- **Quote**: "DeepInfra's Qwen endpoint read a K as an R, called red blue, and described the word "umbrella" as "funny", while four other hosts of the same weights got everything right. Venice and Together didn't see the MiniMax images at all. The model page says it supports image input, but two of its providers don't and even worse they'll pretend everything is 200 OK."
- **Our assessment**: The "pretend everything is 200 OK" framing is the sharpest and most actionable part of this claim — a provider silently failing a documented capability (vision) rather than erroring is a categorically worse failure mode than a rejected request, because nothing in the API contract signals the caller that anything went wrong. This is architecturally distinct from, and a sharper practitioner-facing instance of, the general provider-heterogeneity risk already flagged (at a more abstract level, without this concrete example) in the Prospector's own triage comments for this issue.

### Claim 4: OpenRouter's `reasoning.effort` parameter is "accepted everywhere" syntactically, but whether it actually changes model behavior depends on the provider — a controlled sweep across the 23 providers serving DeepSeek V4 Flash 0731 at low/high/max effort (three calls each) found several (the author names digitalocean, gmi-cloud, mancer, venice) that do not track the requested effort level in their reasoning-token output
- **Evidence**: Author's own controlled test, "pinned every provider serving DeepSeek V4 Flash 0731 and sent the same prompt at low, high and max, three times each, from a prod machine," with reasoning-token counts per provider per effort level charted; raw probe data linked.
- **Confidence**: emerging (a controlled, named, dated test with linked raw data — the strongest-evidenced claim in the source alongside Claims 2 and 5 — but a single prompt/task type and not independently reproduced by this Miner)
- **Quote**: "reasoning.effort is accepted everywhere. Whether it does anything depends on the model and the provider." (prose) / "DeepSeek V4 Flash 0731, most providers respect the setting but look at digitalocean, gmi-cloud, mancer, venice." (chart caption) / "Track the reasoning tokens for your effort setting, per provider." (closing prescription)
- **Our assessment**: This corroborates and sharpens a claim already in this corpus's DeepSeek V4-Flash-0731 coverage: `blog-simonwillison-deepseek-v4-flash-0731.md` Claim 7 documents Willison's own single-provider test where the *default* reasoning level (unspecified provider, "via OpenRouter") produced a structurally broken pelican SVG while `reasoning_effort high` fixed it — that note treated this purely as a model-level effort-sensitivity finding. This source reframes the same parameter as having a *provider-level* reliability gap on top of the model-level sensitivity: even an explicit non-default `reasoning_effort` setting is not guaranteed to be honored, depending on which of the 23 charted providers serves the request. Practitioners who fixed a reasoning-quality problem by setting an explicit effort level (per that note's Guide Impact) should additionally verify the setting is actually being honored by the specific provider handling their traffic, not just by the model in general.

### Claim 5: Filtering OpenRouter providers by declared quantization (e.g. `quantizations: ["fp8"]`) does not reliably predict output quality — fp4-declared hosts scored in the middle of the fp8 pack on both GPQA and TAU-Bench for DeepSeek V4 Flash 0731, and GLM 5.3 Flash's single best scorer on both benchmarks (Wafer) declares no quantization level at all
- **Evidence**: Author's own cross-tabulation of OpenRouter's per-provider benchmark board against each provider's declared quantization field, run for two models (DeepSeek V4 Flash 0731 and GLM 5.3 Flash) across both benchmarks; a month-long personal experience ("I ran that filter on DeepSeek for a month") precedes the analysis.
- **Confidence**: emerging (a specific, tabulated cross-reference of two independently-sourced OpenRouter data fields — declared quantization and benchmark score — for two models, with linked raw data; the "unknown" quantization bucket, which contains both the best and some of the worst scorers, limits how strong a causal claim can be drawn, and the author's own conclusion is appropriately hedged to "quantization is a bad *proxy*," not "quantization has zero effect")
- **Quote**: "The fp4 hosts land in the middle of the fp8 pack. The three worst GPQA scores on DeepSeek are one of each: an fp4 host, an fp8 host, and one that declares nothing. GLM's best scorer on both benchmarks, Wafer, declares nothing at all. Precision is a bad proxy for quality, and a hard filter also shrinks the pool OpenRouter can fall back to when a provider goes down. Filter on the board, not the bits."
- **Our assessment**: The closing prescription — "filter on the board, not the bits" — is a concrete, actionable practitioner recommendation: use OpenRouter's own per-provider benchmark board (or an equivalent task-specific eval) to select/exclude providers, rather than trusting the `quantizations` request parameter as a quality proxy. The second half of the claim (a hard quantization filter "shrinks the pool OpenRouter can fall back to") is a distinct, separately-important point: even where quantization filtering doesn't help quality, it actively reduces fallback redundancy, compounding the fragility documented in Claim 10.

### Claim 6: Tool calls sometimes arrive as unparsed raw text in the model's reply instead of a structured tool-call object, because the provider's own parser failed to recognize the model's markup — and how often this happens "varies wildly by provider," requiring practitioners to write their own client-side parsing for both fully-wrapped and half-wrapped cases
- **Evidence**: Author's own operational observation from running Olly in production, with a literal example of the malformed output and a pointer to his own open-source parsing workarounds.
- **Confidence**: anecdotal (a described, recurring production failure mode with one concrete example, but no frequency/rate data or per-provider breakdown given, unlike Claims 2–5 which are numerically tabulated)
- **Quote**: "Ideally: the model emits a call in some markup, the provider's parser turns it into a structured tool call, my code runs it. Except sometimes the parser misses and this shows up as the reply: <use_skills><parameters>{"skills":["search"]}</parameters></use_skills> And the recurrence varies wildly by provider. You'll run into this often and stubbornly enough that you'll need to start parsing on your end."
- **Our assessment**: This is a concrete instance of the "different XML/tool parsers" root cause named in Claim 1 — each provider's proprietary tool-call parser can fail to recognize the model's own emitted markup, leaking it into the visible response instead of a structured tool call. For harness engineers building agent loops on top of OpenRouter, this argues for a defensive parsing layer that treats the raw-text-tool-call pattern as an expected failure mode to catch and retry/re-parse, not an edge case.

### Claim 7: A 200 OK response does not guarantee the model produced an answer — reasoning models sometimes return `content: null` with `finish_reason: "stop"` after consuming hundreds of reasoning tokens, and the author's prescription is to treat "no content and no tool call" as a failure requiring a throw-and-retry, not a successful empty response
- **Evidence**: Author's own operational observation, with a specific example (345 completion tokens, HTTP 200, no visible output).
- **Confidence**: anecdotal (a described, recurring failure mode with one specific numeric example, no frequency data)
- **Quote**: "Reasoning models sometimes put everything in the reasoning field and hand back content: null, finish_reason: "stop". 345 completion tokens, HTTP 200, nothing to show the user. A 200 tells you the request was served, not that there's an answer in it. No content and no tool call is a failure, throw and retry."
- **Our assessment**: A directly actionable API-contract caution: HTTP status code alone is an insufficient success signal for reasoning-capable models routed through OpenRouter — callers must also validate that the response body actually contains user-visible content or a tool call before treating a 200 as a successful turn.

### Claim 8: Distinct from Claim 7, some endpoints return a "hollow" 200 response with null content, null reasoning, AND no `usage` object at all — in July, StreamLake produced this on ~20% of the author's DeepSeek traffic (92% of all his empty completions that month), and a month later Together exhibited the identical failure on the 0731 checkpoint
- **Evidence**: Author's own production telemetry, with specific percentages and a named before/after provider pair on the same underlying failure signature.
- **Confidence**: anecdotal (production-scale percentages from the author's own traffic, but self-reported with no independent verification, and the underlying cause on either provider's side is not diagnosed)
- **Quote**: "Some endpoints return 200 with null content, null reasoning, and no usage object at all. In July that was StreamLake on DeepSeek: about 20% of my traffic and 92% of my empty completions. A month later Together did the same on the DeepSeek 0731 checkpoint."
- **Our assessment**: The author explicitly distinguishes this from Claim 7 ("Related but not the same") — the missing `usage` object specifically is the distinguishing signal, meaning a caller checking for `content`/`tool_call` absence alone (per Claim 7's prescription) may still need a second, distinct check for a missing `usage` object to catch this variant. The fact that the *same specific failure signature* recurred a month later on a *different* provider (StreamLake → Together) on the same model checkpoint suggests this is a systemic OpenRouter/provider-integration gap rather than a one-off bug particular to a single backend.

### Claim 9: The rules for what conversation history a provider will accept are per-provider, not per-model — passing back empty `reasoning_content` from a DeepSeek thinking-mode turn causes SiliconFlow to reject the request with HTTP 400 (error code 20015, "The reasoning_content in the thinking mode must be passed back to the API"), while Baidu, Alibaba, and Cloudflare accept the identical history without complaint
- **Evidence**: Author's own operational observation with a verbatim provider error code and message, plus an explicit caution against the naive workaround (skipping tool history entirely causes the model to retry the task).
- **Confidence**: anecdotal (a specific, named error code/message from one provider contrasted with three named providers that don't reject it, but no data on how common this specific history-validation divergence is across the full provider set)
- **Quote**: "If you pass the empty reasoning history back to OpenRouter and that goes to e.g. SiliconFlow it will 400 with code 20015, "The reasoning_content in the thinking mode must be passed back to the API". Baidu, Alibaba and Cloudflare take the exact same history without complaint. So the contract isn't per model, it's per provider. And don't think you can skip tool history, the model will keep retrying the task otherwise."
- **Our assessment**: "The contract isn't per model, it's per provider" is the single most quotable, generalizable line in the source — it reframes every preceding pitfall (benchmarks, vision, reasoning effort, quantization, tool parsing, empty completions) under one unifying principle: OpenRouter's promise of a uniform API surface for a given model ID does not extend to uniform *behavioral contracts* across the providers actually serving that model ID, and history-validation strictness is one more axis (alongside vision support and reasoning-effort handling) on which providers diverge even though the request/response schema is nominally identical.

### Claim 10: The same OpenRouter API key and request can succeed from a developer's laptop but be rate-limited (HTTP 429) from production infrastructure, for the same provider in the same minute — the author's inference is that some providers rate-limit by source IP rather than by API key
- **Evidence**: Author's own operational observation comparing identical requests from his Mac versus his production infrastructure for two named providers.
- **Confidence**: anecdotal (a described discrepancy with a plausible inferred mechanism — "my read is" — not confirmed by any provider's own documentation or support channel)
- **Quote**: "Venice and Novita worked perfectly from my Mac for DeepSeek V4 Flash, but 429'd nearly every probe from my infra. Same key, same minute. My read is they rate-limit by IP. Benchmark from where prod runs, a few at a time, more samples than feels necessary."
- **Our assessment**: A specific, practical testing-methodology warning: any pre-deployment provider evaluation done from a local development machine may not predict production rate-limit behavior if a provider keys its limits to source IP rather than account/API key — the author's own prescription ("benchmark from where prod runs") is the direct mitigation, and is a distinct, narrower recommendation than simply "test more" — it specifically calls out *where* the test traffic originates as a variable that changes the result.

### Claim 11: Pinning to multiple named, previously-reliable providers with fallbacks disabled does not guarantee availability — a three-provider pinned configuration (`provider.order: [cloudflare, baidu, alibaba]` with `allow_fallbacks: false`) for the #1 OpenRouter model (DeepSeek V4 Flash) went fully down within two weeks when Baidu began rate-limiting all requests, Cloudflare stopped serving the model entirely, and Alibaba (now receiving 100% of the pinned traffic) then also started 429ing — taking the author's production application (Olly) down with it
- **Evidence**: Author's own first-hand production incident, with the exact configuration, the specific failure sequence for each of the three named providers, and the stated outcome (the author's own application went down).
- **Confidence**: anecdotal (a single, specific, first-hand production incident — but concretely detailed, with exact configuration and named providers/failure modes, and directly answers a question the post itself poses rhetorically: "Why don't you just pin a single provider?")
- **Quote**: "At one point I had provider.order: [cloudflare, baidu, alibaba] with allow_fallbacks: false, so not just one but 3 different reliable providers pinned. Two weeks later Baidu was rate-limiting everything (429s), Cloudflare turned out not to serve that model at all any more, and 100% of traffic was going to Alibaba, which then started 429ing. The #1 OpenRouter model (DeepSeek V4 Flash) pinned to the 3 most reliable providers was now down, and so was Olly."
- **Our assessment**: This is the source's strongest counter-evidence against the seemingly obvious mitigation for provider heterogeneity — "just pin the providers you trust." Pinning trades the *behavioral inconsistency* risk documented in Claims 2–9 for a *correlated availability* risk: a fixed provider set can degrade independently (rate-limiting, silent model deprecation) over a two-week window with no code change on the caller's side, and disabling fallback removes OpenRouter's own recovery mechanism precisely when it would be needed. The author does not offer a clean resolution to this tension in the post — the practical implication is that provider selection is a tradeoff between behavioral consistency (Claims 2–9's argument for pinning) and availability resilience (this claim's argument against overly narrow pinning), not a problem either extreme choice solves outright.

### Claim 12: OpenRouter provides two documented, request-level controls for constraining provider heterogeneity — a `provider.only` array to allow-list specific provider slugs for a single request, and a `GET /models/{author}/{slug}/endpoints` API method to discover, per model, exactly which providers are currently available along with their declared quantization, supported parameters, pricing, and rolling uptime/latency/throughput stats
- **Evidence**: Willison's own post names both controls as the practical mitigation to the problems Moustafa's post documents; this Miner independently fetched both linked OpenRouter docs pages and confirmed their content and parameter schemas.
- **Confidence**: settled (first-party OpenRouter API documentation, independently fetched and confirmed by this Miner, not merely relayed)
- **Quote**: "Thankfully you can control which provider is routed to using the provider.only option. The /endpoints method returns the list of available providers for a specific model ID." (Willison's post) OpenRouter's own provider-routing docs separately warn of a direct tradeoff: "Only allowing some providers may significantly reduce fallback options and limit request recovery."
- **Our assessment**: OpenRouter's own documentation explicitly names the exact tradeoff Claim 11 demonstrates in production — the `only` field's own docs warn it "may significantly reduce fallback options and limit request recovery," which is precisely the mechanism that took Olly down in Claim 11 (`allow_fallbacks: false` plus a narrow provider set). The `/endpoints` API response schema (confirmed by this Miner's direct fetch) includes `quantization`, `supported_parameters`, `uptime_last_1d`/`uptime_last_30m`/`uptime_last_5m`, and `latency_last_30m`/`throughput_last_30m` percentile objects per endpoint — meaning a practitioner could, in principle, script Moustafa's own manual "filter on the board" prescription (Claim 5) and periodic pinned-provider health checks (implied by Claim 11) directly against this API rather than relying on OpenRouter's public benchmark UI and manual monitoring, though neither source in this note describes anyone actually doing so.

## Concrete Artifacts

### Willison's link-blog post (verbatim, simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/)
```
One of OpenRouter's selling points is that it "handles fallbacks
automatically and picks the most cost-effective option for each request",
so you can call a single API endpoint for a model and get routed to the
best available backend provider.

Mohamed Moustafa points out a whole set of ways that this can cause you
problems. Different providers run different serving software with
different optimizations and settings, which means that the same
OpenRouter endpoint can serve model requests that behave in different
ways.

Some providers even lack vision capability for vision models, and the
way the reasoning effort option is processed can differ as well.

Thankfully you can control which provider is routed to using the
provider.only option. The /endpoints method returns the list of
available providers for a specific model ID.

Source: simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/,
11th September 2026, via Hacker News (news.ycombinator.com/item?id=49621546)
```

### Malformed tool-call example (verbatim, mmoustafa.com/blog/so-you-want-to-use-openrouter/)
```
<use_skills><parameters>{"skills":["search"]}</parameters></use_skills>

Source: Mohamed Moustafa, "So you want to use OpenRouter?",
mmoustafa.com/blog/so-you-want-to-use-openrouter/, September 7, 2026
```

### SiliconFlow history-validation error (verbatim)
```
HTTP 400, code 20015:
"The reasoning_content in the thinking mode must be passed back to the API"

Source: Mohamed Moustafa, same post, pitfall #8 ("Same models, different
history rules")
```

### Pinned fallback configuration that still failed (config verbatim; outcome summarized by this Miner, full verbatim quote in Claim 11)
```
provider.order: [cloudflare, baidu, alibaba]
allow_fallbacks: false

Outcome after two weeks (summarized): Baidu 429ing everything, Cloudflare
no longer serving the model, Alibaba (100% of traffic) then also 429ing.
See Claim 11 for the author's verbatim account.

Source: Mohamed Moustafa, same post, pitfall #10 ("Why don't you just
pin a single provider?")
```

### OpenRouter `provider` object schema, relevant fields (subset transcribed from the docs table, not a verbatim excerpt; openrouter.ai/docs/guides/routing/provider-selection)
```
Field                Type            Default   Description
order                string[]        -         List of provider slugs to try in order.
allow_fallbacks      boolean         true      Whether to allow backup providers when the primary is unavailable.
only                 string[]        -         List of provider slugs to allow for this request.
ignore               string[]        -         List of provider slugs to skip for this request.
quantizations        string[]        -         List of quantization levels to filter by (e.g. ["int4", "int8"]).
require_parameters   boolean         false      Only use providers that support all parameters in your request.

"Only allowing some providers may significantly reduce fallback options
and limit request recovery."

Source: openrouter.ai/docs/guides/routing/provider-selection
(fetched directly by this Miner, 2026-09-19)
```

### OpenRouter `/endpoints` API response schema, relevant fields (field names transcribed from the documented example response, not a verbatim excerpt; openrouter.ai/docs/api/api-reference/endpoints/list-all-endpoints-for-a-model)
```
GET /api/v1/models/{author}/{slug}/endpoints

Per-endpoint response fields include:
  provider_name, quantization, supported_parameters,
  pricing (prompt/completion/image/request),
  context_length, max_prompt_tokens, max_completion_tokens,
  uptime_last_1d, uptime_last_30m, uptime_last_5m,
  latency_last_30m { p50, p75, p90, p99 },
  throughput_last_30m { p50, p75, p90, p99 }

Source: openrouter.ai/docs/api/api-reference/endpoints/list-all-endpoints-for-a-model
(fetched directly by this Miner, 2026-09-19)
```

## Cross-References

### Cross-reference verification notes
`blog-simonwillison-llm-openrouter-06.md`, `blog-simonwillison-llm-openrouter-07.md`,
`blog-latentspace-macmanus-glean-model-routing.md`,
`blog-latentspace-ainews-stripe-buys-openrouter.md`, and
`blog-simonwillison-deepseek-v4-flash-0731.md` were each read in full before
drafting this section. Claim numbers below were confirmed against each
cited note's numbered `### Claim N:` headings in document order. Where the
cited material does not live in a numbered claim, it is cited by section
name instead, per MINER.md §4b step 4 — this applies to the
`blog-simonwillison-llm-openrouter-06.md` version-history table below,
which an earlier draft of this note incorrectly attributed to that note's
Claim 5 (Claim 5 there is the plugin's seven-release evolution summary and
does not mention the `-o provider` option).

- **Corroborates**:
  - `blog-simonwillison-deepseek-v4-flash-0731.md` Claim 7 (Willison's own
    single-provider test: default reasoning level produced a structurally
    broken pelican SVG for DeepSeek V4 Flash 0731 via OpenRouter, fixed by
    setting `reasoning_effort high`): this note's Claim 4 independently
    confirms reasoning-effort sensitivity for the same model, and extends it
    with the provider-level finding that even an explicit effort setting is
    not honored consistently by all 23 charted providers.
  - `blog-latentspace-macmanus-glean-model-routing.md` Claim 3 (Glean's CEO:
    customers choose automatic model routing mainly for cost, not quality)
    and the broader routing-market framing in
    `blog-latentspace-ainews-stripe-buys-openrouter.md`: both establish that
    automatic routing/fallback is adopted primarily as a cost and
    availability optimization; this note's Claims 2–9 supply the
    quality/consistency cost of that same optimization at the
    provider-selection layer specifically (as opposed to Glean's
    model-selection layer), extending the corpus's routing coverage down one
    level of the stack.

- **Contradicts**: None identified. No existing source note makes a claim
  about OpenRouter's per-provider behavioral consistency, vision support, or
  fallback reliability that this source's claims materially oppose.

- **Extends**:
  - `blog-simonwillison-llm-openrouter-07.md` Claim 2 (llm-openrouter 0.7
    switched to OpenRouter's Responses API by default) and Claims 4–6 (the
    plugin's Shell/WebFetch/WebSearch server-side tools): those notes
    document the `llm-openrouter` CLI plugin's *access* layer to OpenRouter
    without addressing provider-selection reliability. This note adds the
    operational risk layer underneath that access path — a practitioner
    using `llm -m openrouter/...` (per those notes' Guide Impact
    recommendations) is still subject to the per-provider variance
    documented here regardless of which client library or CLI they use to
    reach OpenRouter.
  - `blog-simonwillison-llm-openrouter-06.md` → Concrete Artifacts →
    "llm-openrouter version history" table, 0.4 row (2025-03-10), which
    records `-o provider '{JSON}'` for custom provider routing: that note
    documents the *existence* of a provider-routing parameter in the plugin
    without discussing why a practitioner would need it; this note's
    Claims 2–11 supply the concrete operational motivation for reaching for
    that option (or the `provider.only` control documented in Claim 12) in
    the first place. (Cited by section rather than claim number: the
    `-o provider` detail appears only in that note's version-history table,
    not in any of its five numbered claims.)

- **Novel**:
  - **First in-corpus documentation of provider-level (not model-level)
    behavioral inconsistency on OpenRouter**, with concrete, numerically
    tabulated evidence across five distinct failure axes (benchmark score,
    vision capability, reasoning-effort compliance, quantization/quality
    correlation, history-validation strictness) — prior corpus coverage of
    OpenRouter (`blog-simonwillison-llm-openrouter-06.md`, `-07.md`,
    `blog-latentspace-ainews-stripe-buys-openrouter.md`) covers the CLI
    access layer and the business/financial layer, but not provider-level
    reliability.
  - **"200 OK, no answer" and "hollow completions" as named, distinct API
    failure modes** (Claims 7–8): no prior source note in this corpus names
    or distinguishes these two null-content response patterns for any
    model-routing provider.
  - **The pinned-fallback-chain-still-fails production incident** (Claim
    11): the first in-corpus first-hand account of a multi-provider pinned
    configuration failing in production despite disabling automatic
    fallback. The closest existing guide coverage is
    `05-team-adoption.md`'s "Model Deprecation Is a Recurring Governance
    Event" section, which documents the same silent-disappearance risk for
    pinned *model identifiers* (GitHub's GPT-5.2 deprecation); no source note
    in this corpus yet documents it for pinned *provider* lists. See Guide
    Impact for the recommended placement.

## Guide Impact

- **`02-harness-engineering.md` (Harness Engineering)** — new section on the
  routing-gateway layer of the harness. Add Claims 1, 9, and 11 as the core
  lesson: OpenRouter's uniform model-ID API surface does not imply a uniform
  provider *behavioral* contract, and neither "trust automatic fallback" nor
  "pin your own provider list" is a complete solution — pinning trades
  consistency risk for correlated-availability risk (Claim 11). Cite Claim
  12's `provider.only` / `/endpoints` controls as the concrete mechanism,
  paired with OpenRouter's own documented caveat that `only` "may
  significantly reduce fallback options." Nearest existing anchor in this
  chapter is Anti-Pattern "7. No Dollar Ceiling on Unsupervised Agent Spend"
  (the Vercel AI Gateway material), which is currently the chapter's only
  treatment of an LLM gateway sitting between the harness and the providers;
  this note supplies the reliability dimension of that same layer, where
  that section covers the spend dimension.
- **`02-harness-engineering.md` (Harness Engineering)** — same new section.
  Add Claim 5 (declared quantization is a poor proxy for output quality on
  OpenRouter, and filtering by it shrinks the fallback pool) as a caution
  against configuring the `quantizations` request parameter as a
  quality-control mechanism; cite the author's own prescription ("filter on
  the board, not the bits") as the recommended alternative. This is a
  provider-selection *configuration* recommendation, which belongs with the
  other routing-config guidance above rather than in a cost or
  model-selection discussion — this guide has no such chapter or theme.
- **`03-verification.md` (Verification)** — new section on validating a
  routed model response. Add Claims 7–8 ("200 OK, no answer" and "hollow
  completions") as two distinct, named response-validation failure modes any
  OpenRouter-routed agent loop should explicitly check for beyond HTTP
  status: (a) empty `content` with no tool call, and (b) a missing `usage`
  object entirely. Add Claim 6 (tool calls leaking as raw unparsed text) as a
  third defensive-parsing requirement. This extends the chapter's existing
  "Known Verification Failure Modes" section with failure modes that
  originate in the serving layer rather than in the model's reasoning.
- **`03-verification.md` (Verification)** — benchmark-methodology material.
  Add Claim 10 (IP-based rate limiting causing a laptop-vs-prod discrepancy
  for the same API key) as a specific, actionable evaluation-methodology
  caution: pre-deployment provider evaluation should run from production
  infrastructure, not a developer machine. Add Claim 2 (a 20–30 point
  TAU-Bench swing across providers serving identical weights) as a further
  reason a published score does not transfer to your deployment. Both sit
  naturally alongside the chapter's existing "Benchmark Scores Can Measure
  Retrieval, Not Coding" section, which already makes the more general
  argument that a benchmark number depends on the conditions under which it
  was measured.
- **`05-team-adoption.md` (Team Adoption) → existing "Model Deprecation Is a
  Recurring Governance Event" section**: Claim 11 is directly on point for
  this section's thesis that "Workflows that pin specific model identifiers
  have a shelf life measured in weeks, not months" and that the failure mode
  is silent. Claim 11 is the same governance risk one layer down — a pinned
  *provider* list, not a pinned model ID, degrading within two weeks
  (Cloudflare silently ceasing to serve the model at all is exactly the
  silent-disappearance pattern that section documents for GitHub's GPT-5.2
  deprecation). Recommend adding it there as a second, independently-sourced
  instance, and noting that the governance checklist should cover pinned
  provider/endpoint configuration alongside pinned model identifiers.

## Extraction Notes

- **Followed the linked primary source per MINER.md §1**: Willison's post
  itself is ~90 words of commentary; the substantive claims all live in
  Mohamed Moustafa's linked article at `mmoustafa.com/blog/so-you-want-to-use-openrouter/`
  (dated September 7, 2026, four days before Willison's post), which this
  Miner fetched directly via `curl` with a browser user-agent (HTTP 200) and
  read in full — all charts, per-provider tables, and prose. This mirrors
  the precedent set in `blog-simonwillison-llm-openrouter-07.md` (README
  followed as the substantive linked page) and is noted explicitly per
  MINER.md's convention for link-blog sources.
- **Two additional linked pages followed**: OpenRouter's own provider-routing
  docs (`openrouter.ai/docs/guides/routing/provider-selection`) and
  `/endpoints` API reference (`openrouter.ai/docs/api/api-reference/endpoints/list-all-endpoints-for-a-model`),
  both linked directly from Willison's post as the stated mitigation
  mechanisms. Both were fetched directly via `curl` and confirmed to render
  substantive documentation content (unlike the OpenRouter Responses API
  docs page, which `blog-simonwillison-llm-openrouter-07.md`'s Extraction
  Notes records as a JS-rendered page yielding no usable prose on a direct
  fetch — these two pages did not have that problem).
- **Chart data not independently re-verified**: The per-provider benchmark
  boards, vision test results, and reasoning-effort sweep charts in
  Moustafa's post are presented as static rendered content (SVG/chart
  elements) with numeric labels extracted via HTML-to-text conversion; this
  Miner did not independently query OpenRouter's live benchmark UI or API to
  re-verify the specific percentages as of the extraction date, though the
  author links raw data files (effort probes, benchmark boards, a probe
  script) behind several of the charts, which a future Miner or the Assayer
  could use to spot-check specific figures if needed.
- **No sub-pages followed beyond the three described above**: Moustafa's
  post links to his own open-source project (`github.com/0xmmo/190proof`,
  his "own parsing examples for DeepSeek/GLM") and several raw-data files
  (Google Sheets/CSV links for the effort probes and benchmark boards); these
  were not fetched, as they are supplementary data/code artifacts rather
  than additional prose sources, consistent with MINER.md's "up to 5 linked
  pages that seem substantive" guidance being satisfied by the three pages
  actually followed.
- **No contradictions identified requiring MINER.md §4a filing.**
- **Confidence calibration: emerging.** The three most rigorously evidenced
  claims (2, 4, 5) are individually rated `emerging` — controlled,
  numerically tabulated, dated tests with linked raw data, from a named
  practitioner operating at a stated production scale, but not independently
  reproduced by this Miner or corroborated by a second independent source.
  Claims 6–11 are individually rated `anecdotal` — real, specific, named
  production incidents and observations, but each is a single practitioner's
  single-application experience without statistical breadth. Claim 1
  (the model/provider vocabulary distinction) and Claim 12 (the documented
  API controls, independently confirmed by this Miner's own fetch) are rated
  `settled`. The note-level confidence is set to `emerging` rather than
  `anecdotal` because the source's strongest claims are backed by
  practitioner-run, linked-raw-data tests at meaningful production scale
  (18M+ messages), which is a materially stronger evidentiary basis than a
  single anecdote or an unaudited vendor claim, while still falling short of
  `settled` because none of it has been independently reproduced outside
  this one author's infrastructure.
