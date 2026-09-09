---
source_url: https://simonwillison.net/2026/Sep/4/astra-pelicans/
source_type: blog-post
title: "The Pelican comparison grid for Astra is pretty interesting"
author: Simon Willison
date_published: 2026-09-04
date_extracted: 2026-09-09
last_checked: 2026-09-09
status: current
confidence_overall: emerging
issue: "#3318"
---

# The Pelican comparison grid for Astra is pretty interesting

> Simon Willison's first hands-on evaluation of GPT-6 Astra: he re-ran his
> "pelican riding a bicycle" SVG benchmark at all five of Astra's reasoning
> levels (low/medium/high/xhigh/max — Astra has no `none` level) and built
> an interactive grid comparing the results against GPT-5.6 Sol, Terra, and
> Luna at every shared reasoning level, with exact token counts and per-run
> pricing for all 19 model/level combinations. Astra beats every GPT-5.6 Sol
> output at every reasoning level, including Astra's cheapest (low, 9.55¢);
> a token-efficiency quirk (Astra and Luna both use 16 input tokens vs. 26
> for Sol/Terra) leads Willison to speculate Astra and Luna share more
> architecture than OpenAI has disclosed. The linked grid page's own Sol
> pricing caption ($4/$20) contradicts both the post's prose ($5/$30) and
> prior corpus pricing — see Contradicts below.

## Source Context

- **Type**: blog-post (Willison's weblog, September 4, 2026 — a short
  same-day reaction post, ~230 words, built around an embedded interactive
  comparison grid hosted separately at
  `static.simonwillison.net/static/2026/gpt-6-and-5.6-pelicans.html`). Per
  MINER.md §1, this note follows that linked grid page directly (fetched
  raw, not summarized) because it is where the actual token-count and
  pricing data lives — the blog post prose only summarizes and interprets
  it.
- **Author credibility**: Simon Willison is a `trusted-feed` source already
  extensively used in this corpus (creator of Django, Datasette,
  `sqlite-utils`, the `llm` CLI, and originator of the "pelican riding a
  bicycle" SVG benchmark examined in `blog-simonwillison-pelicanmaxxing.md`
  and `blog-simonwillison-kimi-k3-pelican-benchmark.md`). Unlike
  `blog-simonwillison-gpt6-astra-launch.md` (a day-one post explicitly
  written *before* Willison had tried Astra himself, curating vendor and
  Artificial Analysis data secondhand), this post is Willison's own
  first-person hands-on test — "I got access to GPT-6 Astra this afternoon,
  so naturally I used it to generate SVGs of pelicans riding bicycles." That
  makes this note a stronger, more direct evidentiary source than the
  launch-day note for anything about Astra's actual output quality and
  token usage, though it is still a single-practitioner, single-benchmark,
  informal test (one prompt family, LLM-judged only by Willison's own eye).
- **Scope**: Covers relative SVG-generation quality and cost/token usage of
  GPT-6 Astra vs. GPT-5.6 Sol/Terra/Luna across reasoning levels, using one
  narrow creative-generation task (pelican-on-a-bicycle SVG). Does not cover
  coding-agent performance, reasoning/math benchmarks, safety evaluations,
  or any task closer to real harness-engineering workloads — this is a
  vibes-plus-token-accounting test, not a rigorous capability benchmark
  (contrast with the statistically-controlled methodology surfaced in
  `blog-simonwillison-pelicanmaxxing.md`, which this post's own single-shot,
  unreplicated design does not follow).

## Extracted Claims

### Claim 1: Every Astra pelican output, from its lowest to its second-highest reasoning level, looked better to Willison than the best GPT-5.6 Sol pelican at any reasoning level
- **Evidence**: Direct visual/qualitative judgment by Willison comparing the rendered SVG grid; he names his own preferred Sol baseline (xhigh) explicitly.
- **Confidence**: anecdotal (single practitioner's subjective visual judgment, no LLM-judge scoring or replication)
- **Quote**: "The very best GPT-5.6-Sol pelican (I liked xhigh better than max) is still pretty clearly a bunch of abstract shapes. Every single one of the Astra pelicans, from low to xhigh, looks better than that."
- **Our assessment**: Consistent with the corpus's general pattern of each new flagship model outperforming the prior generation on this benchmark, but this is a purely qualitative, single-rater judgment on one narrow creative task — treat as a data point on generational quality trend, not a rigorous capability claim.

### Claim 2: Astra below "max" reasoning does not reliably render the pelican with legs visible on both sides of its body
- **Evidence**: Willison's direct visual inspection of the rendered grid.
- **Confidence**: anecdotal
- **Quote**: "Astra below max still doesn't reliably get the pelican legs on both sides of the frame."
- **Our assessment**: A concrete, specific failure mode rather than a vague "not perfect" — useful as a small illustration that even a clearly-superior model has a specific, reasoning-level-gated rendering limitation. Low external validity beyond this one SVG task.

### Claim 3: Astra is priced roughly double Sol per token ($10/$50 vs. Sol's stated $5/$30 per million input/output tokens), but uses substantially fewer tokens at comparable reasoning levels, narrowing the effective cost gap across levels
- **Evidence**: Stated directly in the post prose ($5/$30 for Sol) and illustrated by the token-count table on the linked grid page — though that page's own pricing caption gives a different Sol figure (see Cross-References → Contradicts below).
- **Confidence**: emerging (pricing figures are precise, but the Sol number is internally inconsistent within this single source)
- **Quote**: "Astra may be around twice the price of Sol ($10/million input, $50/million output, compared to $5/$30 for Sol), but it uses significantly less tokens at each of the levels, making the prices at the different levels closer than they might otherwise be."
- **Our assessment**: The directional claim (Astra's token efficiency partially offsets its higher per-token price) is well-supported by the grid's own token counts (see Concrete Artifacts). The specific $5/$30 Sol figure is contradicted by the grid page's own caption ($4/$20) — flagged as issue #3331, do not cite Sol's exact price from this source without resolving that first.

### Claim 4: Astra's "low" reasoning level produces a better pelican, for 9.55 cents, than any GPT-5.6 Sol output at any reasoning level, including Sol runs that cost more than 9.55 cents
- **Evidence**: Willison's cost/quality comparison across the full grid, cross-referenced against the per-cell cost figures in the grid table.
- **Confidence**: anecdotal (single-rater quality judgment) combined with settled arithmetic (cost figures are directly computed from token counts and price)
- **Quote**: "Astra low produces a better pelican than ANY of the GPT-5.6 Sol models at any level, for 9.55 cents. Spending 10 cents on any other model gets a much worse result."
- **Our assessment**: This is the post's central practical claim — cheapest Astra beats most-expensive Sol on this task. If it generalizes even loosely beyond pelican SVGs, it's a real "just use the new model, even at its lowest setting" signal for cost-conscious model selection — but one benchmark family is thin evidence for that generalization.

### Claim 5: Astra and GPT-5.6 Luna both consumed 16 input tokens for the same prompt, while Sol and Terra both consumed 26 input tokens, leading Willison to speculate Astra and Luna may be more architecturally related than OpenAI has publicly stated
- **Evidence**: Directly read off the grid's per-cell token counts (see Concrete Artifacts); Willison's inference is explicitly speculative.
- **Confidence**: anecdotal (Willison flags it as speculation, not a confirmed architectural claim)
- **Quote**: "Look at the input token counts: Astra and Luna both used 16 input tokens, Sol and Terra used 26. That's interesting." / "I wonder if Astra and Luna are more related to each other than OpenAI let on?"
- **Our assessment**: An interesting inference from tokenizer/prompt-encoding behavior, but Willison himself only frames it as a "wonder if" — not a claim to build guide advice on. Worth noting as a pattern (matching input token counts across a "flagship + fast/cheap tier" pairing can hint at shared tokenizer or prompt-template lineage) but not as settled fact.

### Claim 6: Astra does not support a "none" (no reasoning) level, unlike GPT-5.6 Sol, Terra, and Luna, which all have a "none" row in the comparison grid
- **Evidence**: Stated directly in the post prose and confirmed by the grid page, where Astra's "none" row reads "Not available" while Sol/Terra/Luna all have populated none-level entries.
- **Confidence**: settled (directly observed, unambiguous)
- **Quote**: "Astra doesn't support reasoning=none"
- **Our assessment**: A concrete product/API capability difference — Astra always does at least some reasoning. Relevant for any guide advice about minimum-latency, reasoning-free model usage, where GPT-5.6 Luna (which does support `none`, at 0.14 cents per this task) would be the cheaper/faster choice by design, not just by setting.

## Concrete Artifacts

Full token-count and cost table from the linked comparison grid
(`static.simonwillison.net/static/2026/gpt-6-and-5.6-pelicans.html`),
reproduced verbatim from its per-cell text. Grid page's own pricing caption:
"Prices per 1M input/output tokens: Astra $10/$50, Sol $4/$20, Terra $2/$12,
Luna $0.20/$1.20." (Note: the Sol figure here — $4/$20 — conflicts with the
blog post prose's $5/$30; see Cross-References → Contradicts.)

```
Effort   | gpt-6-astra                        | gpt-5.6-sol                         | gpt-5.6-terra                        | gpt-5.6-luna
max      | 16 in, 12,638 out = 63.21 cents    | 26 in, 16,180 out = 32.37 cents     | 26 in, 21,390 out = 25.67 cents      | 16 in, 13,040 out = 1.57 cents
xhigh    | 16 in, 6,766 out  = 33.85 cents    | 26 in, 8,033 out  = 16.08 cents     | 26 in, 9,776 out  = 11.74 cents      | 16 in, 7,072 out  = 0.85 cents
high     | 16 in, 3,671 out  = 18.37 cents    | 26 in, 3,454 out  = 6.92 cents      | 26 in, 2,486 out  = 2.99 cents       | 16 in, 4,098 out  = 0.49 cents
medium   | 16 in, 2,560 out  = 12.82 cents    | 26 in, 3,511 out  = 7.03 cents      | 26 in, 2,302 out  = 2.77 cents       | 16 in, 2,089 out  = 0.25 cents
low      | 16 in, 1,906 out  = 9.55 cents     | 26 in, 2,772 out  = 5.55 cents      | 26 in, 2,312 out  = 2.78 cents       | 16 in, 1,258 out  = 0.15 cents
none     | Not available                      | 26 in, 1,961 out  = 3.93 cents      | 26 in, 1,731 out  = 2.08 cents       | 16 in, 1,176 out  = 0.14 cents
```

(Source: grid page at the URL above, fetched and parsed directly by the
Miner on 2026-09-09; blog post text attributes the underlying prompt
transcript to a linked gist,
`gist.github.com/simonw/f789d2784fc6c5b870cc80f0b7cd9d01`, not separately
fetched for this note.)

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-gpt6-astra-launch.md` — that note's secondhand,
    vendor/Artificial-Analysis-sourced claim that Astra is priced at "parity
    with Claude Fable 5/5.1 ($10/$50 per million tokens)" matches this
    post's first-person-confirmed $10/$50 Astra pricing exactly.
  - `blog-simonwillison-gpt56-luna-price-drop.md` (Claim 2) — this note's
    Terra ($2/$12) and Luna ($0.20/$1.20) figures, read directly off the
    grid page, match the July 30, 2026 post-price-cut figures exactly,
    reinforcing that those two figures are correct and making the grid's
    Sol figure the more likely outlier (see Contradicts).
  - `blog-simonwillison-pelicanmaxxing.md` — both posts use Willison's
    "pelican riding a bicycle" SVG benchmark as a comparative evaluation
    tool; that note's Dylan Castillo analysis found no lab-specific
    "pelicanmaxxing" effect, meaning this grid's quality differences are
    reasonably attributable to genuine model capability rather than any
    lab specifically tuning for this exact prompt.
- **Contradicts**: This source disagrees with itself on GPT-5.6 Sol's
  per-token price — post prose states $5/$30, the linked grid page's own
  caption states $4/$20, and the grid's displayed per-cell costs are
  arithmetically consistent with $4/$20, not $5/$30. Filed as
  **[contradiction issue #3331](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/3331)** —
  do not treat either Sol figure as settled from this source alone until
  that issue resolves. The corpus's prior figure ($5/$30, from
  `blog-simonwillison-gpt56-sol-launch.md` and
  `blog-simonwillison-gpt56-luna-price-drop.md`) is better corroborated and
  is the filer's recommended verdict, but this note does not pre-empt that
  call.
- **Extends**: `blog-simonwillison-gpt6-astra-launch.md` — upgrades that
  note's secondhand, not-yet-hands-on Astra assessment to a first-person
  practitioner test with concrete output-quality and token-usage data.
- **Novel**: The full per-reasoning-level token-count and cost table across
  four models (19 cells) is new to the corpus — no prior note has
  reasoning-level-granular token/cost data for Astra. The Astra/Luna
  input-token-count match (16 vs. 26 for Sol/Terra) is also a novel
  observation not present in any prior source note.

## Guide Impact

- **Chapter 04 (Context Engineering)**: The chapter's existing reasoning-effort
  cost discussion (around line 771, citing session-cost guidance for setting
  reasoning effort) could add this source as a concrete illustration that
  raw per-token price is a poor proxy for effective cost — Astra's ~2x
  per-token price is largely offset by using far fewer output tokens at
  comparable/superior quality (Claim 3, Claim 4). Recommend citing the
  token-count table (Concrete Artifacts) as an example of comparing
  *effective* per-task cost across reasoning levels, not headline
  per-million-token price. Do not cite the exact Sol $/token figure from
  this source until contradiction #3331 resolves — use the corroborated
  $5/$30 figure from `blog-simonwillison-gpt56-luna-price-drop.md` instead
  if a specific number is needed.
- **Chapter 02 (Harness Engineering)**: If the chapter discusses model
  selection defaults or "always use the newest flagship" heuristics, Claim 4
  (cheapest Astra beats priciest Sol on this task) is a relevant but
  narrow-evidence data point — flag clearly as a single-benchmark,
  single-rater result (pelican SVG generation), not a general capability
  finding, consistent with this corpus's existing caveats about the
  pelican benchmark's informal nature (`blog-simonwillison-pelicanmaxxing.md`).

## Extraction Notes

- Followed the linked comparison grid page
  (`static.simonwillison.net/static/2026/gpt-6-and-5.6-pelicans.html`)
  directly via raw fetch rather than relying on WebFetch's AI-summarized
  read of the main post, because a first WebFetch pass of the main post
  refused to reproduce prose verbatim (citing copyright) and, separately,
  did not surface the grid's own token/price table at all — the concrete
  numbers in this note come from parsing that page's raw HTML/text directly.
  Did not fetch the linked prompt-transcript gist
  (`gist.github.com/simonw/f789d2784fc6c5b870cc80f0b7cd9d01`) or the
  Mastodon/Bluesky/Twitter/newsletter links, which are non-substantive
  (author contact/subscribe links), consistent with MINER.md §1's "follow
  up to 5 linked pages that seem substantive" guidance.
- The Sol pricing contradiction (Claim 3, Cross-References) was the most
  significant finding of the extraction pass — flagged per MINER.md §4a
  rather than silently resolved in either this note or the corresponding
  contradiction issue.
- The main blog post itself is short (~230 words); most of the extractable
  data density is in the linked grid page's table, not the prose. This
  is reflected in the claim count (6, on the lower end of the 5-15 target)
  — the source is genuinely thin on distinct prose claims beyond the six
  extracted, even after fully parsing the grid page.
