---
source_url: https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/
source_type: blog-post
title: "deepseek-ai/DeepSeek-V4-Flash-0731"
author: Simon Willison
date_published: 2026-07-31
date_extracted: 2026-08-07
last_checked: 2026-08-07
status: current
confidence_overall: emerging
issue: "#2541"
---

# deepseek-ai/DeepSeek-V4-Flash-0731

> A short Willison link-blog post on a new DeepSeek V4-Flash checkpoint
> (304B params, 167GB HF, $0.14/$0.27 per M input/output tokens) that
> Artificial Analysis places at the far edge of its "most attractive
> quadrant" on an Intelligence-Index-vs-Cost-per-Task chart — but the
> post's headline claim of "substantially enhanced agentic capabilities"
> is asserted, not benchmarked, and Willison's own reasoning-effort test
> shows the model needs an explicit `reasoning_effort high` setting to
> produce good output; the default reasoning level was "disappointing."

## Source Context

- **Type**: blog-post (Willison's link-blog format — a single short post,
  roughly 150 words of original prose plus three image alt-text
  descriptions; auto-discovered via the `simon-willison` trusted feed)
- **Author credibility**: Simon Willison is creator of Django and the
  `llm` CLI, and a widely-cited practitioner commentator on LLM tooling
  in this corpus (see `blog-simonwillison-deepseek-v4.md`,
  `blog-simonwillison-glm51.md`, `blog-simonwillison-kimi-k3-pelican-benchmark.md`).
  This post is his standard link-blog pattern: a linked release + a short
  first-person reaction plus his own hands-on pelican-SVG test. The
  Artificial Analysis ranking and chart are third-party data he links to
  and describes, not his own benchmarking; the "substantially enhanced
  agentic capabilities" phrase is DeepSeek's own release framing, quoted
  by Willison, not independently verified by him in this post.
- **Scope**: Covers the model's parameter count and HuggingFace size,
  its Artificial Analysis Intelligence-Index-vs-Cost-per-Task chart
  position, its API pricing, and one hands-on reasoning-effort
  comparison test (default vs. `high`) using the pelican-riding-a-bicycle
  SVG prompt via OpenRouter. Does NOT cover: any agentic-task benchmark
  (SWE-bench, tool-use, terminal-bench), context window size, license,
  active-parameter count (MoE sparsity), or code/reasoning benchmarks.

## Extracted Claims

### Claim 1: DeepSeek frames this release as having "substantially enhanced agentic capabilities" — a claim the post itself does not independently test or benchmark
- **Evidence**: Opening sentence of the post, describing the release. No agentic-task benchmark (tool use, coding-agent eval, long-horizon task) is cited anywhere in the post to substantiate this specific claim — the only benchmark data shown is the Intelligence-Index-vs-Cost chart (Claim 4) and Willison's own single creative-SVG test (Claim 7).
- **Confidence**: anecdotal (vendor release framing, quoted uncritically; no supporting agentic benchmark in this source)
- **Quote**: "The latest release in DeepSeek's V4 family, "with substantially enhanced agentic capabilities"."
- **Our assessment**: This is the exact claim the Prospector's triage flagged as the "key question" for this source, and the post does not answer it. Willison quotes DeepSeek's own framing without independent agentic-task testing — his hands-on test in this post is a single creative-SVG generation, not an agentic/tool-use evaluation. Practitioners should not treat this post as evidence that V4-Flash-0731 has improved agentic capability; it should be treated as an unverified vendor claim pending an agentic-specific benchmark (SWE-bench Verified, Terminal-Bench, or similar), consistent with how this corpus treats other unverified vendor self-description (e.g., the "competitive with GPT-5.5" framing flagged in `blog-simonwillison-kimi-k3-pelican-benchmark.md`'s Extraction Notes).

### Claim 2: V4-Flash-0731 is 304 billion parameters, 167GB on Hugging Face — a new checkpoint distinct from the April V4-Flash (284B / 160GB)
- **Evidence**: Directly stated parameter count and file size in the post.
- **Confidence**: settled (published specification at time of post)
- **Quote**: "It's 304 billion parameters - 167GB on Hugging Face - but it appears to punch well above its weight."
- **Our assessment**: This confirms the Prospector's assessment that 0731 is a genuinely new checkpoint, not a re-post of the April release documented in `blog-simonwillison-deepseek-v4.md` Claim 1 (which gave V4-Flash as 284B total / 13B active / 160GB HF). The post does not state an active-parameter count for the 0731 checkpoint, so the MoE sparsity ratio for this specific variant is unconfirmed — practitioners comparing efficiency to the April Flash should note this gap rather than assume the 13B-active figure still applies.

### Claim 3: Artificial Analysis ranks V4-Flash-0731 ahead of MiniMax M3, a substantially larger 428B model
- **Evidence**: Direct statement attributing the ranking to Artificial Analysis, a third-party benchmarking organization already used elsewhere in this corpus (e.g., `blog-thebatch-gpt55-hallucination-kimi-k26.md`).
- **Confidence**: emerging (third-party leaderboard ranking, no specific numeric score given for MiniMax M3 in this post — only the qualitative "ahead of" framing plus the chart's cost comparison in Claim 5)
- **Quote**: "Artificial Analysis rank it ahead of MiniMax M3 - a 428B model."
- **Our assessment**: A 304B model outranking a 428B competitor on Artificial Analysis's index is a genuine parameter-efficiency data point, but "ranks ahead of" is qualitative here — the post doesn't give MiniMax M3's own Intelligence Index score for direct comparison, only that MiniMax M3 "costs ten times more" for similar-or-lower intelligence per the chart (Claim 5). Treat as directionally credible (third-party source) but not independently reproducible from this post alone.

### Claim 4: At $0.14/million input and $0.27/million output tokens, this "may currently be the best value-per-intelligence model out there"
- **Evidence**: Willison's own editorial judgment, following directly from the stated pricing.
- **Confidence**: anecdotal (single practitioner's qualitative superlative, hedged with "may currently be")
- **Quote**: "It's $0.14/million input and $0.27/million output pricing means this may currently be the best value-per-intelligence model out there."
- **Our assessment**: The hedge ("may currently be") signals this is Willison's impression rather than a settled ranking. The pricing itself is nearly identical to the April V4-Flash ($0.14/$0.28 per `blog-simonwillison-deepseek-v4.md` Claim 2) — output is marginally cheaper (¢0.27 vs ¢0.28) — so the "best value" claim rests on the new checkpoint's higher capability at essentially the same price, not on a price cut. This is a stronger endorsement than Willison's April framing ("very, very inexpensive," `blog-simonwillison-deepseek-v4.md` Claim 7), which stopped short of a "best value" superlative.

### Claim 5: On Artificial Analysis's Intelligence Index vs. Cost-per-Task chart, V4-Flash-0731 sits alone at roughly $0.028/task and an intelligence score of ~50 — at the far-left edge of the "most attractive quadrant," where the Pareto line jumps sharply upward
- **Evidence**: The chart's image alt-text (written to accessibly describe an embedded Artificial Analysis scatter plot), which gives specific axis ranges, the model's plotted position, and the quadrant/Pareto-line framing.
- **Confidence**: emerging (third-party (Artificial Analysis) chart data, mediated through a textual description on Willison's site rather than the raw chart/dataset itself; axis is "Cost per Task," a different unit than the corpus's usual per-token pricing)
- **Quote**: "DeepSeek V4 Flash 0731 (max) is highlighted in dark blue at roughly $0.028 and an intelligence score of 50, sitting alone at the far left edge of the green quadrant where the Pareto line jumps sharply upward." (image alt-text, `static.simonwillison.net/static/2026/deepseek-flash-chart.webp`)
- **Our assessment**: This is a genuinely new metric type for the corpus: **cost per completed task**, not cost per million tokens. Cost-per-task normalizes for how many tokens a model actually consumes to finish a benchmark task (relevant for reasoning models with variable output length) — a more decision-relevant number for agentic workloads than the raw per-token pricing tables used elsewhere in the corpus (e.g., the 12-model table in `blog-simonwillison-deepseek-v4.md` Concrete Artifacts). An intelligence score of ~50 places this Flash variant close to April's V4-Pro (Index score 52, per `blog-thebatch-gpt55-hallucination-kimi-k26.md` Concrete Artifacts → Artificial Analysis Intelligence Index Leaderboard) — meaning a smaller, cheaper Flash checkpoint released three months later has nearly closed the gap to the larger April Pro model's Index score, at a small fraction of Pro's $1.74/$3.48 per-token pricing.

### Claim 6: The same chart shows models of similar-or-lower intelligence (MiniMax-M3, Kimi K3 low, GLM-5.1, Kimi K2.6) costing roughly 10× more per task, while models that beat it on intelligence (Grok 4.5, Gemini 3.6 Flash, GLM-5.2, Kimi K3, Claude Opus 5, Claude Fable 5, GPT-5.6 Sol) all sit at $0.4–$3 per task
- **Evidence**: Same image alt-text as Claim 5, describing the full comparison set plotted on the chart.
- **Confidence**: emerging (same sourcing/caveats as Claim 5 — third-party chart data mediated through a textual description)
- **Quote**: "Models of similar or lower intelligence like MiniMax-M3, Kimi K3 (low), GLM-5.1 and Kimi K2.6 cost ten times more, and the models that beat it (Grok 4.5, Gemini 3.6 Flash, GLM-5.2, Kimi K3, Claude Opus 5, Claude Fable 5, GPT-5.6 Sol) all sit far to the right at $0.4 to $3 per task." (image alt-text, `static.simonwillison.net/static/2026/deepseek-flash-chart.webp`)
- **Our assessment**: This is the concrete evidence behind the "best value-per-intelligence" claim (Claim 4): a roughly 15–100× cost-per-task spread between V4-Flash-0731 (~$0.028) and the frontier models that outperform it on intelligence ($0.4–$3). For cost-sensitive agentic pipelines that can tolerate somewhat lower intelligence, this is a specific, named list of models this new checkpoint undercuts on cost-per-task — though "task" here is Artificial Analysis's benchmark-task definition, not necessarily representative of any given practitioner's own workload token consumption.

### Claim 7: Default reasoning level produced a "disappointing" pelican SVG with structurally broken elements; setting `reasoning_effort high` via OpenRouter produced a materially better result
- **Evidence**: Willison's own hands-on test, described in prose plus two image alt-text descriptions of the resulting SVGs, plus the exact `llm` CLI command used for the high-effort run.
- **Confidence**: anecdotal (single practitioner, single test, single creative/visual task — not a systematic reasoning-effort sweep)
- **Quote**: "I got a disappointing pelican from it using the default reasoning level via OpenRouter" ... "But when I bumped reasoning level up to high I got something much better"
- **Our assessment**: The default-reasoning image's alt-text confirms concrete failure modes: "the wheels are just orange arcs with no rims or spokes, the frame tubes float apart and the handlebars connect to nothing." The high-reasoning image alt-text describes a correctly-assembled bicycle with the pelican gripping the handlebars and a foot on the pedal. This corroborates a reasoning-effort-sensitivity pattern already documented for a different vendor in `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 5 (GPT-5.5's xhigh reasoning producing 9,322 tokens vs. 39 at default, per `blog-simonwillison-gpt55-codex-plugin.md`) — the pattern that default/low reasoning settings can produce materially worse output isn't DeepSeek-specific. For practitioners: do not benchmark or deploy a reasoning-capable model at its API default without first testing whether a higher `reasoning_effort` setting is needed for the target task quality — this applies across vendors, not just to this one release.

## Concrete Artifacts

### Model release framing and specs (verbatim, post body)

```
"The latest release in DeepSeek's V4 family, "with substantially enhanced
agentic capabilities". It's 304 billion parameters - 167GB on Hugging Face
- but it appears to punch well above its weight."

Pricing: $0.14/million input tokens, $0.27/million output tokens

Source: Simon Willison, simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/,
31st July 2026
```

### Artificial Analysis chart description (verbatim image alt-text)

```
"Scatter plot from Artificial Analysis titled with axes "Artificial
Analysis Intelligence Index" (20 to 65) and "Cost per Task (USD, Log
Scale)" ($0.02 to $3), with a green "Most attractive quadrant" box in
the upper left and a dotted "Pareto line". DeepSeek V4 Flash 0731 (max)
is highlighted in dark blue at roughly $0.028 and an intelligence score
of 50, sitting alone at the far left edge of the green quadrant where
the Pareto line jumps sharply upward. Models of similar or lower
intelligence like MiniMax-M3, Kimi K3 (low), GLM-5.1 and Kimi K2.6 cost
ten times more, and the models that beat it (Grok 4.5, Gemini 3.6 Flash,
GLM-5.2, Kimi K3, Claude Opus 5, Claude Fable 5, GPT-5.6 Sol) all sit
far to the right at $0.4 to $3 per task."

Source: image alt-text, static.simonwillison.net/static/2026/deepseek-flash-chart.webp
(embedded in simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/)
```

### Reasoning-effort test command and result descriptions

```
Default reasoning level (OpenRouter), described by Willison as
"disappointing." Image alt-text: "the wheels are just orange arcs with
no rims or spokes, the frame tubes float apart and the handlebars
connect to nothing."

High reasoning effort, invoked via:
  llm -m openrouter/deepseek/deepseek-v4-flash-0731 -t pelican -o reasoning_effort high

Result described by Willison as "much better." Image alt-text: "The
pelican grips the handlebars with its wings and one orange foot rests
on the pedal, and a small blue fish is visible tucked in the corner of
its large orange beak pouch."

Source: simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/, 31st July 2026
```

## Cross-References

- **Corroborates**:
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md` Concrete Artifacts → Artificial Analysis Intelligence Index Leaderboard: that table places DeepSeek-V4-Pro at Index score 52 (May 2026). This post's chart gives V4-Flash-0731 an Index score of ~50 (Claim 5) — a smaller, cheaper Flash checkpoint released three months later has nearly closed the gap to April's larger V4-Pro on the same Artificial Analysis metric, independently corroborating rapid efficiency gains within the DeepSeek V4 family.
  - `blog-simonwillison-deepseek-v4.md` Claim 6 (V4's self-reported "3 to 6 months" trail behind frontier models): an Index score of ~50 for V4-Flash-0731, still below GPT-5.5 (60), Claude Opus 4.7/Gemini 3.1 Pro (57), and even Kimi K2.6 (54) per the same leaderboard, is consistent with the V4 family remaining sub-frontier on raw intelligence while being highly cost-competitive — this post doesn't contradict that framing, it reinforces it with a newer data point.
  - `blog-simonwillison-kimi-k3-pelican-benchmark.md`: that note documents Willison's reasoning-token-cost testing methodology (13,241 reasoning tokens costing 25 cents for one pelican SVG) and his reflection that the pelican test's remaining value is as "a forcing function for actually running a model," not a capability ranking. This post's default-vs-`reasoning_effort high` comparison (Claim 7) is a direct instance of that same reasoning-effort-sensitivity testing pattern, applied to a different vendor.

- **Contradicts**: None identified. No existing source note makes a claim about DeepSeek V4-Flash-0731 specifically or about cost-per-task metrics that this post's data conflicts with.

- **Extends**:
  - `blog-simonwillison-deepseek-v4.md`: the April note thoroughly documented V4-Flash (284B/13B active, 160GB HF, $0.14/$0.28) and V4-Pro specs, pricing, and paper-cited efficiency metrics. This post extends that with a new checkpoint (304B, 167GB, $0.14/$0.27) three months later, adding an "agentic capabilities" claim (Claim 1, unverified in this source) and a cost-per-task chart position (Claims 5–6) not present in the April note.

- **Novel**:
  - **Cost-per-task (rather than cost-per-token) leaderboard framing**: the Artificial Analysis Intelligence-Index-vs-Cost-per-Task chart (Claims 5–6) is the first in-corpus benchmark using a per-completed-task cost unit rather than per-million-token pricing. This is a materially different practitioner-relevant metric for agentic/reasoning workloads where token consumption per task varies by model.
  - **An unverified "agentic capabilities" claim flagged at the source-note level**: Claim 1 explicitly documents that DeepSeek's "substantially enhanced agentic capabilities" framing is not backed by any agentic benchmark in this specific post — useful as a marker for future mining if a dedicated DeepSeek V4-Flash-0731 agentic benchmark source surfaces later.
  - **Cross-vendor reasoning-effort sensitivity via OpenRouter's `reasoning_effort` parameter**: Claim 7 is the first in-corpus documentation of DeepSeek-specific reasoning-effort testing using OpenRouter's `reasoning_effort` parameter (as opposed to the vendor-native reasoning-level parameters documented for GPT-5.5 and Kimi K3 elsewhere in the corpus).

## Guide Impact

- **Ch03 (Model Selection)**: The pricing/spec table sourced from `blog-simonwillison-deepseek-v4.md` should be updated with this newer V4-Flash-0731 checkpoint (304B, 167GB HF, $0.14/$0.27) as the more current DeepSeek Flash data point, noting the active-parameter count is unconfirmed for this specific checkpoint (Claim 2). Recommend flagging that this supersedes, rather than replaces, the April entry — both remain valid historical data points for tracking DeepSeek's release cadence.

- **Ch03 / Ch05 (Cost Optimization)**: Introduce cost-per-task as a distinct model-selection metric alongside cost-per-token, citing Claims 5–6's specific comparison set (V4-Flash-0731 at ~$0.028/task vs. $0.4–$3/task for higher-intelligence competitors). Recommend the guide note this metric is more decision-relevant for reasoning-heavy or agentic workloads than raw per-token pricing, since token consumption per completed task varies significantly by model and reasoning-effort setting.

- **Ch02 (Model Capability Claims / Agentic Systems)**: Use Claim 1 as a worked example of the gap between vendor release framing and demonstrated evidence: "substantially enhanced agentic capabilities" is asserted in DeepSeek's release notes but not tested with any agentic benchmark in this source. Recommend the guide explicitly caution practitioners against treating headline capability claims as verified until a task-specific benchmark (SWE-bench, tool-use eval, terminal-bench) is cited.

- **Ch02 (Reasoning-Effort Configuration)**: Claim 7's default-vs-`high` reasoning-effort comparison, combined with the GPT-5.5 default-vs-xhigh token-count disparity already documented via `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 5, supports a cross-vendor recommendation: "Always test a reasoning-capable model at an explicit non-default reasoning-effort setting before drawing conclusions about its output quality — default settings on multiple vendors' models (OpenAI, DeepSeek) have shown materially worse results than an explicitly elevated setting."

## Extraction Notes

- This is an unusually short source: the post body is roughly 150 words of
  original prose. To reach a substantive claim count, this note extracts
  the three embedded image alt-text descriptions (the Artificial Analysis
  chart and the two pelican-SVG results) as primary evidence alongside the
  prose — these alt-texts are detailed, specific descriptions authored for
  the post and contain data (axis ranges, exact model comparisons, dollar
  figures) not repeated in the prose itself.
- Raw HTML was fetched directly via `curl` with a browser user-agent
  (not through an AI-summarizing fetch tool) to obtain exact wording for
  all quotes and the full image alt-text, following the extraction
  approach flagged as more reliable in `blog-simonwillison-inkling-open-weights.md`
  Extraction Notes. All quotes in this note were copied character-for-
  character from that fetched HTML.
- No linked sub-pages were followed — the post does not link to a
  separate DeepSeek announcement page or technical paper (unlike the
  April V4 post, which the prior note traced to the DeepSeek V4 technical
  paper). The Artificial Analysis chart is embedded as an image with no
  linked source page for the underlying dataset.
- Claim 1 (the "substantially enhanced agentic capabilities" claim) is
  intentionally reported as unverified rather than assessed as true or
  false — this note does not have access to an agentic benchmark for this
  checkpoint. If a future source (e.g., a DeepSeek technical report or an
  independent agentic-benchmark post) tests this claim directly, that
  source should be cross-referenced back to this note.
- No contradictions identified against existing source notes; none filed
  per MINER.md §4a.
- Confidence set to `emerging`: Claim 2 (specs) is `settled`; Claims 3, 5,
  and 6 (Artificial Analysis rankings/chart) are `emerging` (credible
  third-party source, but mediated through image alt-text rather than raw
  data); Claims 1, 4, and 7 are `anecdotal` (vendor framing, editorial
  superlative, and a single hands-on test, respectively). The note-level
  confidence reflects this mix — solid on the published specs, weaker on
  the capability and value claims.
