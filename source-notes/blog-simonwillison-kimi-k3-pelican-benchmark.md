---
source_url: https://simonwillison.net/2026/Jul/16/kimi-k3/
source_type: blog-post
title: "Kimi K3, and what we can still learn from the pelican benchmark"
author: Simon Willison
date_published: 2026-07-16
date_extracted: 2026-07-22
last_checked: 2026-07-22
status: current
confidence_overall: emerging
issue: "#2123"
---

# Kimi K3, and what we can still learn from the pelican benchmark

> Simon Willison's hands-on review of Moonshot AI's Kimi K3 (2.8T parameters), covering its benchmark positioning against Claude Opus 4.8/Fable 5 and GPT-5.5/5.6 Sol, its Sonnet-tier pricing, a "pelican riding a bicycle" SVG test that burned 13,241 reasoning tokens for 25 cents, and Willison's own reflection that the pelican benchmark no longer tracks overall model quality — its remaining value is as a forcing function for actually running a model and a rough signal on tokenization/reasoning-cost behavior, not a capability ranking.

## Source Context

- **Type**: blog-post (Willison "notes" format — first-person practitioner
  testing plus editorial reflection, not a bare quotation post)
- **Author credibility**: Simon Willison is the creator of Django and the
  `llm` CLI, and one of the most widely-cited practitioner commentators on
  LLM tooling in this corpus. His "pelican on a bicycle" SVG generation test
  is a running cross-model benchmark he has applied to dozens of model
  releases (established in this corpus by
  `blog-simonwillison-glm51.md` and `blog-simonwillison-gpt55-codex-plugin.md`).
  This post is first-person hands-on testing (he ran the model himself via
  API) plus his own editorial reflection on the benchmark's continued
  utility, not vendor marketing reproduced uncritically — though the
  competitive-positioning benchmark numbers he cites (Elo scores, arena
  rankings) originate from Moonshot AI's own announcement and from
  Artificial Analysis / Arena.ai third-party leaderboards, not from
  Willison's independent measurement.
- **Scope**: Covers Kimi K3's announced specs and self-reported benchmark
  position, API pricing, one practitioner-run pelican SVG test (token
  counts, cost, a system-prompt-size inference, and a vision-capability
  spot check), and Willison's reflection on what the pelican test can and
  can't tell practitioners about a new model. Does NOT cover agentic
  tool-calling benchmarks, long-horizon task reliability, independent
  third-party replication of Moonshot's self-reported Elo numbers, or any
  coding-agent/harness integration testing of K3.

## Extracted Claims

### Claim 1: Moonshot AI announced Kimi K3, a 2.8 trillion parameter model, describing it as their most capable model to date

- **Evidence**: Opening of the post, quoting Moonshot AI's own announcement framing.
- **Confidence**: settled (published parameter count and release framing; the "most capable" superlative is vendor self-description)
- **Quote**: "Chinese AI lab Moonshot AI announced Kimi K3 this morning, describing it as their 'most capable model to date, with 2.8 trillion parameters'."
- **Our assessment**: The 2.8T parameter figure is more than double Kimi K2.6's 1T total parameters (documented in `blog-thebatch-gpt55-hallucination-kimi-k26.md` Concrete Artifacts → Kimi K2.6 Architecture and Agent Swarm Specifications). Parameter count alone is not a capability measure, but it marks K3 as a further scale-up in Moonshot's model family within roughly two months of K2.6 (May → July 2026).

### Claim 2: Moonshot's self-reported benchmarks place K3 mostly ahead of Claude Opus 4.8 max and GPT-5.5 high, but behind Claude Fable 5 and GPT-5.6 Sol

- **Evidence**: Moonshot AI's own benchmark comparison, as reported in the post's opening section.
- **Confidence**: emerging (vendor self-reported benchmark positioning; not independently replicated in this source)
- **Quote**: "Their self-reported benchmarks have K3 mostly beating Claude Opus 4.8 max and GPT-5.5 high, while losing out to Claude Fable 5 and GPT-5.6 Sol."
- **Our assessment**: This places K3 in the upper-middle of the current frontier tier: above the previous Claude and OpenAI flagship-adjacent models, but below the newest top-tier releases (Fable 5, Sol). Because the comparison is self-reported by Moonshot, practitioners should treat it as a starting hypothesis rather than a settled ranking — consistent with how this corpus treats vendor self-reported benchmarks elsewhere (e.g., OpenAI's "competitive with GPT-5.5" claim for Terra in `blog-simonwillison-gpt56-sol-launch.md` Claim 3, which this note's Extraction Notes explicitly flags as unverified marketing framing pending third-party corroboration).

### Claim 3: Kimi K3 is priced at $3/million input tokens and $15/million output tokens — the same tier as Claude Sonnet, and a large increase over Kimi K2.6

- **Evidence**: Moonshot AI's published API pricing, reported in the post's pricing section, with an explicit comparison to K2.6.
- **Confidence**: settled (published pricing at time of post)
- **Quote**: "$3/million input tokens and $15/million output tokens, putting it at the same level as Anthropic's Claude Sonnet series" and "This is a significant increase on their earlier models such as Kimi K2.6 at $0.95/$4."
- **Our assessment**: This is a roughly 3x input / 3.75x output price increase over K2.6's $0.95/$4 (per `blog-thebatch-gpt55-hallucination-kimi-k26.md` Concrete Artifacts → Kimi K2.6 Architecture and Agent Swarm Specifications, which lists $0.95/$0.16/$4.00 input/cached/output). Moonshot is moving away from the "cheap open-weights alternative" positioning and into direct price parity with a proprietary mid-tier flagship (Claude Sonnet). For practitioners who selected K2.6 specifically for its cost advantage, K3 no longer offers that advantage — it must now be justified on capability alone.

### Claim 4: The pelican SVG test on Kimi K3 consumed 95 input tokens and 16,658 output tokens (13,241 of them reasoning tokens), for a total cost of 25 cents

- **Evidence**: Willison's own API call and token accounting for the standard "generate an SVG of a pelican riding a bicycle" prompt.
- **Confidence**: anecdotal (single prompt, single model, one practitioner run)
- **Quote**: "That pelican took 95 input tokens and 16,658 output tokens (13,241 were reasoning tokens), for a total cost of 25 cents!"
- **Our assessment**: 13,241 reasoning tokens for a simple, static SVG-generation prompt is a very high reasoning-token burn — for comparison, `blog-simonwillison-gpt55-codex-plugin.md` Claim 1 documents GPT-5.5 at `reasoning_effort xhigh` using 9,322 reasoning tokens on the same style of pelican prompt, and only 39 tokens at default effort. K3's 13,241 tokens exceed even GPT-5.5's most expensive manually-selected reasoning tier, and K3 has no lower-effort option to fall back to (see Claim 9). This is a concrete, quantified illustration of the reasoning-token cost tax that extended-thinking models can impose on tasks that don't obviously require deep reasoning.

### Claim 5: Willison states that the pelican benchmark's correlation to overall model quality has been "mostly severed" — it is no longer a useful capability ranking signal

- **Evidence**: Willison's own editorial reflection, based on having run this test across many model generations over an extended period.
- **Confidence**: emerging (longitudinal practitioner observation across dozens of prior pelican tests, not a single-instance anecdote, but also not a formal correlation study)
- **Quote**: "That connection has been mostly severed now."
- **Our assessment**: This is a notable self-correction from the practitioner who created and popularized this exact benchmark. It's a useful caution against treating any single informal, viral benchmark as a durable capability signal — a test that was once loosely diagnostic of overall model quality can stop being so as models specialize and as labs may optimize for known public benchmarks. The guide should cite this directly when discussing informal/viral benchmarks as evaluation tools: even benchmark creators can and do revise their own view of a benchmark's validity as models evolve.

### Claim 6: Willison identifies the pelican benchmark's biggest limitation as not measuring agentic tool calling or long-horizon reliability, which he calls "the thing that matters most" for current models

- **Evidence**: Willison's own editorial assessment of what the pelican test fails to capture.
- **Confidence**: emerging (editorial opinion from a widely-cited practitioner, not an empirical study)
- **Quote**: "The biggest limitation of the pelican is that it doesn't touch at all on the thing that matters most for today's model: agentic tool calling and the ability to operate tools reliably as conversations grow in length."
- **Our assessment**: This is a direct, named articulation of the gap between viral single-shot creative-output benchmarks (pelican SVGs, one-shot code generation) and the capability that actually determines agentic-coding and agent-harness usefulness: sustained, reliable tool use across a long-running conversation. This corroborates the corpus's general drift toward valuing agentic/tool-use reliability metrics over single-turn output quality (e.g., the AA-Omniscience and Apollo Research task-completion metrics in `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claims 2-3). For the guide's model-selection chapters, this is a citable, named-practitioner statement that informal creative benchmarks should not be a substitute for agentic reliability testing when selecting models for harness work.

### Claim 7: K3 appears to have a hidden system prompt of roughly 85 tokens, inferred because prompting just "hi" consumed 86 tokens

- **Evidence**: Willison's own token-count observation from a minimal-prompt test.
- **Confidence**: anecdotal (single inference from one minimal-prompt test, not confirmed by Moonshot documentation)
- **Quote**: "Prompting 'hi' to Kimi K3 counted 86 tokens, suggesting there may be an 85 token hidden system prompt."
- **Our assessment**: This is an indirect inference (token accounting), not a confirmed disclosure from Moonshot — Willison frames it as "suggesting," not asserting as fact. It's still a useful practitioner technique worth noting: minimal-prompt token counting as a lightweight way to estimate undisclosed system-prompt overhead, relevant to cost modeling for high-volume API usage where every request pays this fixed token tax.

### Claim 8: Vision capability testing showed K3 generating accurate image alt text

- **Evidence**: Willison's own vision test, described briefly in the post.
- **Confidence**: anecdotal (single test, single image)
- **Quote**: "Vision works well: the alt text it generated is very good."
- **Our assessment**: A minimal but concrete positive data point for K3's multimodal capability. Thin evidence (one image, no comparison baseline against other models on the same image), but consistent with frontier models generally having solid image-description capability at this point in the corpus's timeline.

### Claim 9: K3 currently exposes only a single reasoning effort level, "max," with no lower-effort option

- **Evidence**: Willison's observation of the model's available configuration options, connected to the high reasoning-token cost in Claim 4.
- **Confidence**: settled (documented current API behavior, though subject to change if Moonshot adds effort tiers later)
- **Quote**: "It only has one reasoning effort right now, 'max'—and it shows."
- **Our assessment**: This is architecturally significant for cost control: `blog-simonwillison-gpt55-codex-plugin.md` Claim 1 shows GPT-5.5 offering a spectrum from 39 to 9,322 reasoning tokens depending on the selected `reasoning_effort`, letting practitioners trade quality for cost per task. K3 offers no such lever yet — every request pays the "max" reasoning-token cost (13,241 tokens in the pelican test), whether or not the task needs that depth. Until Moonshot exposes lower-effort tiers, K3 is a worse fit than reasoning-tunable competitors for high-volume, low-complexity tasks where cost matters.

### Claim 10: Artificial Analysis reports K3 reaching an Elo of 1547 on a private long-context knowledge-work evaluation, a gain of 732 points over Kimi K2.6

- **Evidence**: Third-party benchmark (Artificial Analysis), reported in the post.
- **Confidence**: emerging (third-party benchmark snapshot at a point in time; methodology of the "private long-context knowledge work" eval not detailed in this source)
- **Quote**: "On our private long-context knowledge work evaluation, Kimi K3 reaches an overall Elo of 1547, +732 points from Kimi K2.6"
- **Our assessment**: A 732-Elo-point jump in one model generation (roughly two months) is a very large single-generation improvement if the methodology is stable and comparable across K2.6 and K3 runs. Because this figure comes from Artificial Analysis's own private evaluation (not independently reproducible from this post alone), it should be treated as a notable but unverified data point pending cross-checking against Artificial Analysis's own published methodology.

### Claim 11: Kimi K3 is now the leading model on Arena.ai's Frontend Code arena, ahead of Claude Fable 5

- **Evidence**: Third-party leaderboard (Arena.ai), reported in the post.
- **Confidence**: emerging (point-in-time leaderboard position; leaderboards shift as new models and votes come in, per the same caveat applied to Arena.ai data in `blog-thebatch-gpt55-hallucination-kimi-k26.md` Concrete Artifacts → Artificial Analysis Intelligence Index Leaderboard)
- **Quote**: "The model is also now the leading model on Arena.ai's Frontend Code arena, surpassing even Claude Fable 5."
- **Our assessment**: Frontend/webdev-arena leadership is a human-preference signal specifically for UI/frontend code generation, not a general capability ranking — worth noting alongside Claim 2's more general (and lower) self-reported positioning, since K3 topping a specific narrow leaderboard while trailing Fable 5 on Moonshot's own general benchmarks is not contradictory, just two different measurement axes (task-specific human preference vs. general self-reported eval suite).

### Claim 12: Willison frames the pelican test's remaining value as a "hello world" exercise for actually trying a new model, saying he still gets real value from running it himself

- **Evidence**: Willison's closing reflection on why he continues running the test despite Claim 5/6's caveats about its diminished diagnostic value.
- **Confidence**: emerging (editorial reflection from the benchmark's creator)
- **Quote**: "It's a 'hello world' exercise for prompting a model" and "I still get a decent amount of value out of running the benchmark myself."
- **Our assessment**: This reframes the pelican test's purpose: not a capability ranking (which Claim 5 says it no longer provides), but a forcing function that gets a practitioner to actually run API calls against a new model — surfacing real, concrete signals like tokenization overhead (Claim 7), reasoning-token cost (Claim 4), and basic multimodal competence (Claim 8) that a practitioner would otherwise only read about secondhand. This is a transferable evaluation practice: maintain one small, cheap, consistent "hello world" prompt per new model release specifically to surface cost/token accounting facts, independent of whether the prompt's output quality is itself diagnostic.

## Concrete Artifacts

### Kimi K3 vs. Kimi K2.6 pricing (per million tokens)

```
Model        Input    Output   Notes
Kimi K2.6    $0.95    $4.00    (per blog-thebatch-gpt55-hallucination-kimi-k26.md
                                Concrete Artifacts → Kimi K2.6 Architecture and
                                Agent Swarm Specifications)
Kimi K3      $3.00    $15.00   Same price tier as Claude Sonnet, per this post

Source: simonwillison.net/2026/Jul/16/kimi-k3/, 16 July 2026
```

### Pelican SVG benchmark token/cost accounting (Kimi K3)

```
Input tokens:      95
Output tokens:      16,658
  of which reasoning tokens: 13,241
Total cost:         $0.25

Comparison — GPT-5.5 pelican test (blog-simonwillison-gpt55-codex-plugin.md
Concrete Artifacts → Reasoning token comparison for the pelican SVG benchmark):
  Default reasoning:  39 reasoning tokens, seconds to complete
  reasoning_effort xhigh: 9,322 reasoning tokens, ~4 minutes

Kimi K3's single "max" reasoning tier (13,241 tokens) exceeds GPT-5.5's most
expensive selectable tier (xhigh, 9,322 tokens) on the same style of prompt.

Source: simonwillison.net/2026/Jul/16/kimi-k3/, 16 July 2026
```

### Benchmark positioning snapshot (July 2026)

```
Self-reported (Moonshot AI): K3 mostly beats Claude Opus 4.8 max and GPT-5.5
  high; loses to Claude Fable 5 and GPT-5.6 Sol.
Artificial Analysis (third-party): Elo 1547 on private long-context
  knowledge-work eval, +732 vs. Kimi K2.6.
Arena.ai (third-party): #1 on Frontend Code arena, ahead of Claude Fable 5.

Source: simonwillison.net/2026/Jul/16/kimi-k3/, 16 July 2026
```

## Cross-References

- **Corroborates**:
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md` (Concrete Artifacts → Kimi
    K2.6 Architecture and Agent Swarm Specifications): confirms and extends
    the K2.6 pricing baseline ($0.95/$0.16/$4.00) that this note uses to
    quantify K3's price increase (Claim 3).
  - `blog-simonwillison-glm51.md` (Source Context) and
    `blog-simonwillison-gpt55-codex-plugin.md` (Source Context): both
    establish the pelican-riding-a-bicycle SVG test as Willison's recurring
    cross-model creative-code benchmark. This post is a direct continuation
    of that running series, applied to Kimi K3.
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claims 2-3 (AA-Omniscience
    hallucination/task-completion metrics as more actionable safety signals
    than raw accuracy): corroborates this note's Claim 6 — both sources
    independently push toward agentic reliability and task-completion
    trustworthiness as the metrics that matter, over single-turn creative
    output quality.

- **Contradicts**: None filed. Claim 2 (Moonshot's self-reported general
  benchmark ranking, K3 below Fable 5) and Claim 11 (Arena.ai's narrow
  Frontend Code arena ranking, K3 above Fable 5) might look contradictory at
  a glance, but they are not — they measure different things (a broad
  self-reported eval suite vs. a single-domain human-preference arena). Both
  are captured as distinct claims per MINER.md guidance that differing scope
  is a conditioning variable, not a contradiction.

- **Extends**:
  - `blog-simonwillison-gpt55-codex-plugin.md` Claim 1 (reasoning-effort
    token-cost tradeoff for GPT-5.5, 39 vs. 9,322 reasoning tokens): this
    note's Claims 4 and 9 extend that reasoning-token-cost dataset with a
    third model (Kimi K3, 13,241 tokens) and a new observation — a model that
    exposes no lower-cost reasoning tier at all, unlike GPT-5.5's selectable
    effort levels.
  - `blog-simonwillison-gpt56-sol-launch.md` Claim 3 (OpenAI's own
    "competitive performance" claim for Terra, flagged there as unverified
    vendor marketing pending third-party benchmarks): this note's Claim 2
    applies the same skepticism to Moonshot's self-reported K3 benchmark
    position, reinforcing the corpus's general stance that vendor
    self-reported benchmark comparisons should be treated as a starting
    hypothesis, not a settled ranking, until corroborated by third parties
    such as Artificial Analysis or Arena.ai (as this note itself does in
    Claims 10-11).

- **Novel**:
  - **A benchmark creator revising his own view of his benchmark's validity**:
    Claim 5 (pelican benchmark's correlation to model quality "mostly
    severed") is the first instance in this corpus of a practitioner
    explicitly walking back the diagnostic value of a benchmark he
    personally created and popularized, while still defending its residual
    utility (Claim 12) for a narrower purpose (forcing-function / cost and
    tokenization signal). This is a useful case study for how the guide
    should frame informal/viral benchmarks generally: their utility can
    degrade over time even for their own creator, and a benchmark's
    continued popularity is not evidence of continued diagnostic validity.
  - **Explicit naming of "agentic tool calling and long-horizon reliability"
    as the capability current benchmarks fail to measure** (Claim 6): a
    concise, citable framing of the benchmark gap this corpus has been
    accumulating evidence for piecemeal (hallucination rates, task-completion
    confabulation rates) without a single practitioner naming it this
    directly as "the thing that matters most."
  - **A reasoning-only model with no lower-cost effort tier** (Claim 9): the
    first corpus example of a frontier-scale model exposing a single,
    maximal reasoning setting with no cheaper alternative, contrasted with
    the increasingly common multi-tier reasoning-effort pattern (GPT-5.5's
    five levels per `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 5).

## Guide Impact

- **Chapter 02 (Model Selection & Cost Economics)**: Add Kimi K3's pricing
  ($3/$15 per million input/output tokens) to any per-vendor pricing table,
  explicitly noting the ~3x/3.75x increase over K2.6 (Claim 3) — Moonshot has
  moved from a cost-leadership position to Sonnet-tier price parity in one
  generation. Recommend the guide state plainly that K3 should no longer be
  selected purely for cost advantage over proprietary mid-tier models; it
  must now compete on capability.

- **Chapter 02 (Model Selection & Cost Economics) — reasoning-token cost**:
  Add the pelican-test reasoning-token comparison (Claim 4, Concrete
  Artifacts) as a concrete illustration that "extended thinking" is not free
  even for simple, static generation tasks, and that some models (K3) offer
  no lower-reasoning-effort option to control this cost (Claim 9). Recommend
  a guide callout: when evaluating a new reasoning-capable model for
  high-volume, low-complexity tasks, check whether it exposes a reasoning-effort
  dial before assuming cost will scale down for simple prompts.

- **Chapter 05 (Practical Model Evaluation)**: This source is the strongest
  citable argument in the corpus for de-emphasizing informal, viral,
  single-shot creative-output benchmarks (pelican SVGs, "write a poem," etc.)
  as model-selection tools, sourced from the benchmark creator's own
  reassessment (Claim 5) and his explicit naming of the actual gap — agentic
  tool-calling reliability over long conversations (Claim 6). Recommend
  adding a guide passage: "Even benchmarks' own creators revise their view of
  what those benchmarks measure as models evolve; treat informal creative
  benchmarks as a cheap 'does this basically work' smoke test (Claim 12), not
  a capability ranking, and prioritize agentic/tool-use reliability testing
  for harness-relevant model selection."

## Extraction Notes

- **WebFetch could not reproduce the article verbatim.** Direct requests for
  the full article text returned a copyright-constrained summary rather than
  the raw text. All quotes in this note were obtained via targeted follow-up
  WebFetch requests explicitly asking for short (under-25-word), exact,
  attributed quotes on specific named topics, cross-checked across two
  separate fetch passes for consistency. This is the same limitation
  documented in `blog-simonwillison-gpt56-codex-deletion-bug.md` Extraction
  Notes and `blog-simonwillison-gpt55-codex-plugin.md` Extraction Notes for
  other Willison posts fetched the same way. Quotes should be treated as
  high-confidence but not independently re-verified character-for-character
  against the live page HTML by this extraction; the Assayer should spot-check
  against the source URL directly if possible.
- **No sub-pages followed**: the post links to a gist transcript of the API
  call and to the rendered pelican SVG image itself. Neither was fetched
  separately — the token counts and cost figures quoted in the main post
  fully capture the substantive engineering content of that transcript, and
  the SVG image itself is not text-extractable content relevant to a source
  note.
- **Three duplicate Prospector triage comments** appeared on issue #2123 (a
  known pattern in this corpus from automated re-triage runs, as also seen on
  `blog-thebatch-gpt55-hallucination-kimi-k26.md` and
  `blog-simonwillison-gpt56-sol-launch.md`). All three agree on high novelty
  and on Ch02/model-selection relevance; none flagged a disqualifying
  overlap. The most detailed (third) comment's chapter targeting was treated
  as authoritative, consistent with how prior notes handled the same
  multi-comment pattern.
- **No contradiction issue filed.** The only near-contradiction considered
  (Claim 2's general benchmark ranking vs. Claim 11's narrow Frontend Code
  arena ranking) resolves as a scope/conditioning-variable difference, not a
  genuine disagreement, per MINER.md §4a guidance — documented explicitly
  under Cross-References → Contradicts above.
- **Confidence set to `emerging` overall**: the post mixes settled facts
  (published pricing, parameter count) with vendor self-reported benchmark
  positioning (Claim 2), third-party point-in-time leaderboard snapshots
  (Claims 10-11), and single-practitioner anecdotal testing (Claims 4, 7, 8).
  No claim in this note rises to fully independently-verified/settled status
  across the board, but the practitioner-run token/cost accounting and the
  editorial reflection on benchmark validity (Claims 5, 6, 12) are
  first-person observations from a highly credible source, not secondhand
  vendor claims — hence `emerging` rather than `anecdotal` for the note as a
  whole.
