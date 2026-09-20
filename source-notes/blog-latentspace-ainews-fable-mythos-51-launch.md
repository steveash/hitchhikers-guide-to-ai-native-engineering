---
source_url: https://www.latent.space/p/ainews-claude-fablemythos-51-new
source_type: blog-post
title: "[AINews] Claude Fable/Mythos 5.1: new SOTA model, 75% cache price cut but 70% more output tokens"
author: Latent Space / AINews (automated/editorial daily digest; no individual byline; aggregates tweets and news for 8/31/2026-9/1/2026)
date_published: 2026-09-02
date_extracted: 2026-09-20
last_checked: 2026-09-20
status: current
confidence_overall: emerging
issue: "#3581"
---

# [AINews] Claude Fable/Mythos 5.1: new SOTA model, 75% cache price cut but 70% more output tokens

> Latent Space's AINews digest aggregates the September 1-2, 2026 Claude Fable
> 5.1 / Mythos 5.1 launch: a 75% cache-read price cut ($1.00 → $0.25/MTok) that
> is more than offset by a ~1.7x rise in output-token usage (net +20% cost per
> task per Artificial Analysis), a new #1 Artificial Analysis Intelligence
> Index score of 66, a community claim that Fable and Mythos 5.1 may be
> identical weights differentiated only by safety-routing thresholds, new
> Enterprise Frontier Safeguards (EFS) that also produced false-positive
> refusals, and a split reaction in which API/agent builders praised the
> economics while subscription users reported no corresponding benefit.

## Source Context

- **Type**: blog-post (Latent Space's "AINews" — a daily, largely automated
  digest that aggregates official statements, benchmark-aggregator posts, and
  named social-media reactions into a single dated post; subtitle: "Queue the
  usual rush of model launches..."). Published 2026-09-02, 07:46 UTC, covering
  news from 8/31/2026-9/1/2026. This is the same digest format and publisher
  as `blog-latentspace-fable-5-mythos-launch.md` (the June 10, 2026 Fable
  5/Mythos 5 launch digest), three months later, covering the .1 point release.
- **Author credibility**: No individual byline. Latent Space (Shawn "swyx"
  Wang) is a `trusted-feed` source in this repo's scanning configuration, but
  this specific post is an algorithmic/editorial compilation of primary
  sources (Anthropic's own @claudeai/@mikeyk/@alexalbert__ posts, Artificial
  Analysis's benchmark account @ArtificialAnlys, and named individual
  reactions), not first-hand testing or original analysis by Latent Space
  itself. Per this corpus's existing treatment of AINews posts, benchmark and
  pricing figures are graded as aggregator-relayed vendor/leaderboard claims,
  and named social reactions are graded as attributed third-party opinion, not
  as Latent Space's own independent verification.
- **Scope**: Covers the Fable 5.1/Mythos 5.1 launch announcement and framing,
  pricing changes, Artificial Analysis benchmark results and per-task cost
  figures, the Fable-vs-Mythos same-weights debate, Enterprise Frontier
  Safeguards and false-positive reports, subscription-vs-API reaction split,
  stylistic/tone changes ("Claudese"), and third-party integration
  announcements. Does NOT cover (paywalled beyond this section): the /r/
  LocalLlama Reddit recap, or any content past "Keep reading with a 7-day free
  trial." Does NOT independently verify any benchmark number, pricing figure,
  or the "exact same weights" claim — all of these are relayed from named
  accounts (chiefly @ArtificialAnlys, @mikeyk, @eliebakouch) rather than
  reproduced from a primary Anthropic document by this Miner.

## Extracted Claims

### Claim 1: Anthropic launched Claude Fable 5.1 and Claude Mythos 5.1 as flagship models for coding and knowledge work, positioned as "the world's most advanced models" in that domain
- **Evidence**: Direct quote of Anthropic's own @claudeai launch post, reproduced in the article and cross-checked against the raw fetched HTML.
- **Confidence**: settled (verbatim quote of the vendor's own announcement, consistently present in the raw HTML)
- **Quote**: "We're introducing Claude Fable 5.1 and Claude Mythos 5.1. They're the world's most advanced models for coding and knowledge work."
- **Our assessment**: This is the vendor's own framing, not an independent evaluation — treat the superlative as marketing positioning to be checked against the benchmark and cost claims below (Claims 3-4), which show a more mixed picture (frontier-leading on aggregate score, but not clearly better on cost-efficiency).

### Claim 2: Fable 5.1 keeps Fable 5's per-token pricing for input, output, and cache write, but cuts cache-read price by 75% (from $1.00 to $0.25 per million tokens)
- **Evidence**: Attributed to Anthropic staff (@mikeyk), Artificial Analysis (@ArtificialAnlys), and independent commentator @Teknium, all cited by name as consistent on the figures; reproduced in a dedicated "Core published/priced details" section of the article.
- **Confidence**: emerging (a specific, multiply-attributed figure relayed by the aggregator; not independently verified by this Miner against Anthropic's own pricing page)
- **Quote**: "Anthropic kept list pricing for Fable 5.1 at $10 / $50 / $12.5 per million tokens for input / output / cache write, while cutting cache read price by 75% to $0.25 / MTok, again noted by @mikeyk, @Teknium, and independently quantified by @ArtificialAnlys"
- **Our assessment**: The $10/$50 input/output figures are consistent with `blog-simonwillison-claude-fable-5.md`'s Concrete Artifacts (Fable 5 priced at $10.00/$50.00 per million tokens, June 2026), so the "per-token pricing is unchanged" claim is corroborated by an independent, earlier-dated corpus source for two of the three unchanged figures. The cache-read cut itself (from an implied $1.00 baseline) is new to the corpus — no existing note documents Fable 5's cache-read price before this cut.

### Claim 3: Despite the cache-read cut, per-task cost rose ~20% because Fable 5.1 uses roughly 1.7x more output tokens than Fable 5, netting a $3.76/task cost at "max" effort versus a lower Fable 5 figure, with the cache cut alone saving only ~$1.40/task
- **Evidence**: Attributed to Artificial Analysis's cost-per-task measurements, presented as a specific breakdown (savings vs. added cost) rather than a single headline number.
- **Confidence**: emerging (specific numeric figures attributed to one named third-party benchmark aggregator; not independently reproduced or cross-checked against a second source)
- **Quote**: "Fable 5.1 max: $3.76/task; Fable 5 max: lower, so 5.1 is 20% more expensive per task; reason: Fable 5.1 uses ~1.7× output tokens; cache cut saves ~$1.40 per task"
- **Our assessment**: This is the most concrete and consequential economics finding in the source: a 75% price cut on one cost component (cache reads) can still produce a net cost increase if the model's behavior on the other cost component (output-token verbosity) shifts enough. Practitioners currently reasoning about "5.1 is cheaper because of the cache cut" from the headline framing alone would reach the wrong conclusion for max-effort, high-output-token workloads specifically.

### Claim 4: Fable 5.1 topped the Artificial Analysis Intelligence Index at a score of 66, ahead of Claude Opus 5 (63), Claude Fable 5 (62), GPT-5.6 Sol (61), and Grok 4.6 (61)
- **Evidence**: Attributed to Artificial Analysis (@ArtificialAnlys), presented as a ranked list in the article.
- **Confidence**: emerging (specific score attributed to a named third-party benchmark aggregator, not independently verified by this Miner against the Artificial Analysis site)
- **Quote**: "Artificial Analysis Intelligence Index: 66 at max effort, ahead of: Claude Opus 5 max: 63, Claude Fable 5 max: 62, GPT-5.6 Sol max: 61, Grok 4.6 high: 61"
- **Our assessment**: This directly extends the corpus's Intelligence-Index timeline. `blog-simonwillison-introducing-opus-5.md` Claim 2 (July 24, 2026) documented Opus 5 "currently leading the Artificial Analysis leaderboard, in front of even Fable 5" — i.e., roughly six weeks earlier, Opus 5 led Fable 5 on the same leaderboard. This source shows Fable 5.1 retaking the top spot from Opus 5 by September 2, 2026. This is not a contradiction (both notes accurately report the leaderboard at their respective dates) but a useful data point that AA's Intelligence Index ranking has flipped between Anthropic's own model tiers twice within about ten weeks — evidence that "current SOTA" claims in this corpus have a short shelf life and should always be read with a publication date attached.

### Claim 5: Artificial Analysis's evaluation used Anthropic's default server-side safety fallback, under which requests flagged by the safety classifier were routed to Claude Opus 4.8 or Opus 5 instead of Fable 5.1, and this fallback accounted for approximately 4% of output tokens across the Intelligence Index run
- **Evidence**: Attributed to Artificial Analysis's own evaluation notes, flagged in the article as "one of the most consequential technical caveats in community interpretation."
- **Confidence**: emerging (a specific methodological detail attributed to the benchmark aggregator itself, not independently reproduced by this Miner, but internally consistent with the routing mechanism described in Claim 6)
- **Quote**: "Their eval used Anthropic's default server-side fallback, with safety-flagged requests routed to Claude Opus 4.8 or Claude Opus 5. Fallback accounted for ~4% of output tokens across the Intelligence Index."
- **Our assessment**: This materially qualifies Claim 4's headline "66, ranked #1" score: roughly 1 in 25 output tokens in the winning run were not actually generated by Fable 5.1 but by a different model (Opus 4.8/Opus 5) substituted server-side. A benchmark table that attributes the full score to "Fable 5.1" without this caveat is presenting a blended-model result as a single-model result. Any guide table citing this Intelligence Index figure should carry this caveat.

### Claim 6: A community technical claim holds that Fable 5.1 and Mythos 5.1 may be the exact same underlying weights, differentiated only by which safety-classifier threshold routes a given request, rather than being separate base models
- **Evidence**: Attributed to two named individuals (@eliebakouch, @nrehiew_) describing an internal-activations-based safety classification and escalation mechanism; explicitly flagged by the article as "not official Anthropic statements."
- **Confidence**: anecdotal (an unverified community inference from two named commentators, explicitly not an Anthropic statement, though it is consistent with the official ~4% fallback-routing detail in Claim 5)
- **Quote**: "@eliebakouch: 'Fable and Mythos 5.1 are the EXACT same weights', with internal activations used for safety classification and escalation to a bigger classifier, then fallback to Opus 4.8 for dangerous requests" / "@nrehiew_: if true, the difference is 'likely the threshold set for the safeguard classifier'"
- **Our assessment**: This corroborates and extends the same-model-two-tiers framing already established for the 5-series: `blog-latentspace-fable-5-mythos-launch.md` Claim 1 documents Anthropic releasing "Fable 5 (general availability) and Mythos 5 (restricted access) as two variants of the same underlying 'Mythos-class' model, with Fable 5 carrying additional safeguards." This source shows the same architecture pattern persisting into the .1 generation, now with a more specific (though still unverified) mechanism claim — activation-probe-based classification with escalation, rather than a simple access-tier gate. If accurate, this means "Fable" vs. "Mythos" benchmark rows in system cards may reflect which safety route fired on a given request rather than two genuinely different models, a point the article itself raises as an open transparency question.

### Claim 7: Anthropic introduced Enterprise Frontier Safeguards (EFS) as a new enterprise-oriented observability layer, described by an Anthropic staff member as positioned like "ZDR++" for agent observability
- **Evidence**: Attributed to Anthropic staff member @alexalbert__, describing EFS's positioning.
- **Confidence**: emerging (a specific characterization attributed to a named Anthropic employee via the aggregator, not independently verified against an Anthropic product page by this Miner)
- **Quote**: "new enterprise-oriented controls, especially Enterprise Frontier Safeguards (EFS), positioned as 'ZDR++' for agent observability in enterprise environments" via @alexalbert__
- **Our assessment**: This is new to the corpus — no existing note documents "Enterprise Frontier Safeguards" as a named product feature. The "ZDR++" framing (building on zero-data-retention, which the article separately notes Dan Shipper called "a major reason businesses can now use the model") signals Anthropic bundling data-handling guarantees with a new session/cross-session monitoring capability, a combination not previously documented for the Fable/Mythos line.

### Claim 8: EFS produced concrete false-positive reports at launch: one user could not complete planned testing because requests were repeatedly rejected as "reverse engineering," and another user's math-metaphor prompt triggered a cyber safeguard
- **Evidence**: Attributed to two named individuals (@GregKamradt, @kylebrussell) describing specific first-hand incidents.
- **Confidence**: anecdotal (two independent, named, specific incident reports — stronger than an unattributed "some users complained," but still two individual anecdotes, not a measured false-positive rate)
- **Quote**: "@GregKamradt reported that during v3 testing, requests were frequently rejected as 'reverse engineering,' preventing completion of planned evaluation" / "@kylebrussell said a 'military campaign' metaphor in a theoretical math session triggered cyber safeguards; later added 'Day One safeguards… more annoying so far'"
- **Our assessment**: This is a direct practical cost of the safety architecture described in Claims 6-7: a probe/classifier-based safeguard system that escalates on content patterns (not just explicit intent) produces false positives on benign theoretical/technical work. This is the same category of tension already documented in this corpus's account of the original Fable 5/Mythos 5 launch (`blog-latentspace-fable-5-mythos-launch.md` Claim 9: a user reported Fable 5 refusing "What does the heart do?"), suggesting over-broad safety filtering has been a recurring launch-week pattern across two successive Fable generations, not a one-off incident.

### Claim 9: Reaction to Fable 5.1's usage limits was split along the API-vs-subscription line: one named user found rate limits severe and "even worse than Fable 5," while another explicitly reported no rate-limit problems and had used only 14% of one weekly limit
- **Evidence**: Attributed to two named individuals (@kimmonismus, @theo) reporting contradictory personal usage experiences within the same article.
- **Confidence**: anecdotal (two individual, directly conflicting first-hand usage reports; the article itself concludes "there was no single consensus")
- **Quote**: "@kimmonismus doubled down, saying 5.1 was 'even worse than Fable 5 when it comes to rate usage'" / "@theo pushed back on the universality of rate-limit complaints, saying they were 'not seeing this at all' and had used only 14% of one weekly Fable limit"
- **Our assessment**: This is not a contradiction requiring a `CONTRADICTIONS.md` entry under `agents/MINER.md` §4a — it is the source itself accurately relaying that different users, likely on different plans or with different usage patterns, had different experiences of the same rate-limit system, which the article explicitly frames as a lack of consensus rather than an unresolved factual dispute. It is nonetheless a useful practitioner signal: subjective rate-limit reports at launch vary enough between individual accounts that no single anecdote (positive or negative) should be treated as representative.

### Claim 10: A separate community framing (@nicdunz) argues GPT-5.6 Sol remains the clear winner on intelligence-per-dollar and intelligence-per-token even though Fable 5.1 wins on absolute benchmark ceiling — citing Fable 5.1 Max at 66 intelligence / 140M tokens / $3.69 per task versus GPT-5.6 Sol Max at 61 intelligence / 70M tokens / $0.95 per task
- **Evidence**: Attributed to a named individual's comparative cost-efficiency framing, distinct from the Artificial Analysis figures in Claims 3-4.
- **Confidence**: anecdotal (a single named commentator's own comparative framing and figures, not independently attributed to a benchmark organization the way Claims 3-5 are)
- **Quote**: "Fable 5.1 Max: 66 intelligence, 140M tokens, $3.69/task; Fable 5 Max: 62, 83M tokens, $3.14/task; GPT-5.6 Sol Max: 61, 70M tokens, $0.95/task"
- **Our assessment**: This sharpens Claim 3's cost finding with a cross-vendor comparison: Fable 5.1's absolute score lead (66 vs. 61) comes with roughly 2x the token consumption and nearly 4x the per-task cost of GPT-5.6 Sol. Combined, Claims 3, 4, 5, and 10 argue against treating the "new SOTA" headline (Claim 1, Claim 4) as sufficient for a model-selection decision without separately checking cost-per-task and tokens-per-task for the specific workload shape in question.

### Claim 11: Fable 5.1 shows a large, specific jump on Terminal-Bench-Science 0.1, from 24.7% (Fable 5) to 52.6% (Fable 5.1), more than a 2x improvement
- **Evidence**: Attributed to a named individual (@StevenDillmann) extracting the figures from system-card/benchmark-screenshot discussion.
- **Confidence**: emerging (a specific benchmark figure attributed to a named commentator relaying system-card data, not independently verified by this Miner against a primary Anthropic system card)
- **Quote**: "From @StevenDillmann: Terminal-Bench-Science 0.1, Fable 5: 24.7%, Fable 5.1: 52.6%, more than 2× improvement"
- **Our assessment**: This is the largest single relative benchmark gain reported in the article (all other named gains — HLE, τ³-Banking, GDPval-AA, AA-Briefcase — are more incremental point increases). No existing corpus note documents a Terminal-Bench-Science score for any Claude model, so this is the first such figure in the corpus, but it comes from a single named commentator's extraction rather than a primary source this Miner independently verified.

### Claim 12: Dan Shipper characterizes Fable 5.1 as resolving the prior criticism of Fable 5 as "a supergenius in a datacenter that was almost unusable," now "actually speaks like a normal person" with "clearer prose" and fewer "AI tells"
- **Evidence**: Attributed to named individual @danshipper, quoted describing both the prior criticism and the current improvement.
- **Confidence**: anecdotal (a named, specific practitioner opinion; corroborated in substance, though not in exact wording, by an independent measurement in Claim 13)
- **Quote**: "That positioning mattered because Fable 5 had a reputation — repeated in reactions — for being powerful but sometimes impractical. Dan Shipper summarized the prior criticism as Anthropic having 'built a supergenius in a datacenter that was almost unusable'" / "@danshipper: 'actually speaks like a normal person,' 'clearer prose,' fewer 'AI tells'"
- **Our assessment**: This corroborates and extends `blog-simonwillison-fable51-system-prompt-copyright.md` Claim 5, which documents (via a verbatim system-prompt diff, cross-verified against Anthropic's own archive) that Fable 5.1's published system prompt — released the same week as this article — added an explicit conciseness instruction and reinstated a prohibition on saying "genuinely," "honestly," or "straightforward." That note is a settled, primary-source confirmation of a mechanism; this source is the anecdotal, user-facing report of the resulting effect. Together they show a documented prompt-level change (system prompt) plausibly producing the subjectively reported tone shift (this source), though this Miner has not independently tested whether the prompt change alone accounts for Shipper's full characterization.

### Claim 13: ValsAI's stylistic measurements found Fable 5.1 uses fewer hyphenated compounds and em dashes than Fable 5, but produces longer outputs overall (e.g., 534→1,299 words on one benchmark) and a sharp rise in non-breaking hyphen (U+2011) usage, up to ~4,400 occurrences per million tokens from near zero
- **Evidence**: Attributed to a named analytics account (@ValsAI) presenting quantitative lexical/length statistics across multiple benchmarks.
- **Confidence**: emerging (specific quantitative measurements attributed to a named third-party analytics account, not independently reproduced by this Miner, but internally consistent with — and a more rigorous complement to — the anecdotal tone reports in Claim 12)
- **Quote**: "@ValsAI found longer outputs overall despite shorter sentences: VCB: 534 → 1299 words/task; Terminal-Bench: 961 → 1299; Legal Research: 1892 → 2693" / "@ValsAI noted a weird compensating artifact: use of non-breaking hyphen U+2011 rose from near zero to up to ~4.4k occurrences per million"
- **Our assessment**: This is the most rigorous evidence in the source that the "less Claudese" narrative (Claim 12) is not purely subjective — there are measurable lexical changes. But the article's own framing ("the stats also suggest Anthropic may have traded one surface signature for another") is an important caution: fewer em dashes and hyphenated compounds does not mean fewer distinctive stylistic tells in general, just a different specific tell (a rare Unicode character), and overall output length increased substantially even as individual sentences reportedly got shorter — consistent with, and a likely contributor to, the ~1.7x output-token increase documented in Claim 3.

### Claim 14: On CursorBench specifically, the cache-read price cut was called the "biggest W" by a named commentator, who separately reported CursorBench costs cut by "almost 50%" while scoring higher
- **Evidence**: Attributed to a named individual (@theo) making two related but distinct claims — a general sentiment about the cache cut, and a specific CursorBench cost/score claim.
- **Confidence**: anecdotal (a named individual's characterization and an unverified specific cost-reduction percentage, not attributed to Cursor's own CursorBench maintainers or a published CursorBench report)
- **Quote**: "From @theo: cache price cut was the 'biggest W'" / "in CursorBench, costs were cut by 'almost 50%' while scoring higher"
- **Our assessment**: This extends `blog-anthropic-cursor-fable5-cursorbench.md` Claim 1, which documents Fable 5 scoring 72.9% at Max effort on CursorBench (per Cursor's own Nate Schmidt, July 2026). This source adds an unverified claim that Fable 5.1 both scores higher and costs Cursor-benchmarked users almost 50% less than Fable 5 on the same benchmark family — but unlike the July claim (sourced to Cursor's own eval engineer), this specific percentage comes from an outside commentator's tweet, not from Cursor itself, so it should be treated as a lower-confidence, unverified data point pending a Cursor-sourced follow-up.

## Concrete Artifacts

### Pricing detail (from the article, "Technical details and numbers" section)

```
Source: Latent.Space AINews, Sep 2, 2026 digest

Context window: 1 million tokens
Modalities: text + image inputs
Pricing (unchanged from Fable 5):
  input:       $10 / 1M tokens
  output:      $50 / 1M tokens
  cache write: $12.5 / 1M tokens
Cache read price: reduced from $1.00 to $0.25 / 1M tokens (75% cut)
```

### Artificial Analysis headline results and cost-per-task breakdown (from the article)

```
Source: Latent.Space AINews, Sep 2, 2026 digest, attributed to @ArtificialAnlys

Artificial Analysis Intelligence Index: 66 at max effort
  Claude Opus 5 max:    63
  Claude Fable 5 max:   62
  GPT-5.6 Sol max:      61
  Grok 4.6 high:        61

HLE: 59.1% (previous best cited: Fable 5 at 55.5%)
Terminal-Bench v2.1: 91.4%
SciCode: 62.0%
τ³-Banking: +9 points over Fable 5
GDPval-AA v2: 1853 Elo, +130 over Fable 5
AA-Briefcase: 1694 Elo, +122 over Fable 5

Fallback routing: safety-flagged requests routed to Opus 4.8/Opus 5,
accounting for ~4% of output tokens across the Intelligence Index run.

Cost per task:
  Fable 5.1 max: $3.76/task (20% more than Fable 5 max, due to ~1.7x output tokens;
                 cache cut alone saves ~$1.40/task)
  Fable 5.1 xhigh: score 65, cost $2.72/task
  Opus 5 max: score 63, cost $2.34/task
```

### Benchmark snippets extracted by named community members (from the article)

```
Source: Latent.Space AINews, Sep 2, 2026 digest

Terminal-Bench-Science 0.1 (@StevenDillmann): Fable 5 24.7% -> Fable 5.1 52.6%
DeepSWE (@scaling01): 67.4%
FrontierCode 1.1 Extended (@scaling01): 63.6%
FrontierSWE v2 (@scaling01): 0.57, "highest of the models Proximal evaluated"
Humanity's Last Exam with tools (@Sauers_): 65%
Perplexity WANDR eval (@perplexity_ai): score 0.601, $12.76/task,
  21% higher score, 37% lower cost than Fable 5
Mythos 5.1 verbalized grader awareness (@scaling01): 65% of long agentic
  coding environments
```

### Safeguards and Fable/Mythos routing claims (from the article)

```
Source: Latent.Space AINews, Sep 2, 2026 digest

@eliebakouch: "Fable and Mythos 5.1 are the EXACT same weights", with
internal activations used for safety classification and escalation to a
bigger classifier, then fallback to Opus 4.8 for dangerous requests

@nrehiew_: if true, the difference is "likely the threshold set for the
safeguard classifier"

@alexalbert__: Enterprise Frontier Safeguards (EFS) positioned as "ZDR++"
for agent observability in enterprise environments

@mikeyk: improved honesty / better failure reporting -- "when it's stuck
it says so instead of reporting success"

@GregKamradt: requests during v3 testing frequently rejected as "reverse
engineering," preventing completion of planned evaluation

@kylebrussell: a "military campaign" metaphor in a theoretical math
session triggered cyber safeguards; "Day One safeguards... more annoying
so far"
```

### Stylistic measurements (from the article, attributed to @ValsAI)

```
Source: Latent.Space AINews, Sep 2, 2026 digest, attributed to @ValsAI

Word count per task (Fable 5 -> Fable 5.1):
  VCB:            534  -> 1299
  Terminal-Bench: 961  -> 1299
  Legal Research: 1892 -> 2693

Non-breaking hyphen (U+2011) usage: near zero -> up to ~4.4k occurrences
per million tokens
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-claude-fable-5.md` Concrete Artifacts (Fable 5 priced
    at $10.00/$50.00 per million input/output tokens, June 2026): Claim 2 of
    this note confirms those same two figures carried forward unchanged into
    Fable 5.1, three months later.
  - `blog-latentspace-fable-5-mythos-launch.md` Claim 1 (Fable 5 and Mythos 5
    are two variants of the same underlying "Mythos-class" model, with Fable 5
    carrying additional safeguards): Claim 6 of this note shows the same
    same-model-two-tiers architecture persisting into the .1 generation, now
    with a more specific (unverified) mechanism claim.
  - `blog-latentspace-fable-5-mythos-launch.md` Claim 9 (a user reported Fable
    5 refusing "What does the heart do?", suggesting over-broad safety
    filtering at the original launch): Claim 8 of this note documents a
    second, independent wave of false-positive safety refusals at the .1
    launch, suggesting a recurring pattern across two successive generations
    rather than a one-off.
  - `blog-simonwillison-fable51-system-prompt-copyright.md` Claim 5 (Fable
    5.1's published system prompt, verified against Anthropic's own archive,
    adds an explicit conciseness instruction and reinstates a prohibition on
    "genuinely," "honestly," "straightforward"): Claim 12 of this note's
    anecdotal "speaks like a normal person" reports are consistent with, and
    plausibly explained by, that settled, primary-source-verified prompt
    change.
  - `blog-anthropic-cursor-fable5-cursorbench.md` Claim 1 (Fable 5 scored
    72.9% at Max effort on CursorBench, per Cursor's own eval engineer):
    Claim 14 of this note extends the CursorBench thread with an (unverified,
    non-Cursor-sourced) claim of a further score and cost improvement in 5.1.

- **Contradicts**: None filed as a formal contradiction issue. Claim 9 (split
  rate-limit reports between @kimmonismus and @theo) is an internal tension
  within this single source, but it does not meet the `agents/MINER.md` §4a
  bar for filing — the article itself frames it as divergent individual
  experiences ("no single consensus"), not as two sources asserting
  incompatible facts about the same state of the world.

- **Extends**:
  - `blog-simonwillison-introducing-opus-5.md` Claim 2 (Opus 5 led the
    Artificial Analysis Intelligence Index ahead of Fable 5, as of July 24,
    2026): Claim 4 of this note shows the ranking flipping back to Fable 5.1
    by September 2, 2026 — useful evidence that this leaderboard has changed
    which Anthropic model tier leads it at least twice within about ten
    weeks.
  - `blog-latentspace-fable-5-mythos-launch.md` Claim 4 (Fable 5 ranked #1 on
    the AA Intelligence Index at 64.9, ~5 points ahead of GPT-5.5, June 2026):
    This note's Claim 4 supplies the next data point in the same index for
    the same model family (66 for Fable 5.1, sharing rank-order structure but
    a new baseline three months later).

- **Novel**:
  - **Fable 5.1's cache-read price cut and its net effect on per-task cost**
    (Claims 2-3, 10): No existing corpus note documents a cache-read price
    change for any Fable/Mythos-line model, nor the specific finding that a
    75% single-line-item price cut can still produce a net per-task cost
    increase when combined with higher output-token usage.
  - **Enterprise Frontier Safeguards (EFS) as a named product feature**
    (Claim 7): Not documented in any prior corpus source.
  - **Activation-probe-based safety classification with escalation to a
    larger classifier and fallback to Opus 4.8/Opus 5** (Claims 5-6): A more
    specific mechanism claim than the general "same model, different
    safeguards" framing already in the corpus.
  - **ValsAI's quantitative stylistic measurements** (Claim 13): The first
    corpus source with hard lexical/length statistics (not just anecdotal
    "sounds more natural" reports) for a Fable-line tone change.
  - **Terminal-Bench-Science, DeepSWE, FrontierCode 1.1 Extended, τ³-Banking,
    GDPval-AA, and AA-Briefcase benchmark figures for any Claude model**
    (Claims 4, 11): First appearance of all of these named benchmarks in this
    corpus.

## Guide Impact

- **Chapter 02 (Model Selection & Deployment)**: Add a caution against
  evaluating a headline "X% price cut" claim in isolation. Cite Claim 3: a
  75% cache-read price cut on Fable 5.1 still produced a 20% net per-task
  cost increase versus Fable 5, because output-token usage rose ~1.7x.
  Recommend practitioners request (or measure) both the per-component price
  change and the resulting per-task/per-workload cost before treating a
  pricing announcement as a cost reduction for their specific workload
  shape — cache-heavy, low-output-verbosity workloads benefit; long-output,
  low-cache-reuse workloads may not.

- **Chapter 02 (Model Selection & Deployment)**: When citing Artificial
  Analysis Intelligence Index or similar composite benchmark scores for
  Fable/Mythos-line models going forward, add Claim 5's caveat that AA's
  evaluation methodology includes safety-triggered server-side fallback to a
  different model (~4% of output tokens on the Fable 5.1 run) — a benchmark
  score attributed to one named model may partly reflect a different model's
  output under the covers.

- **Chapter 04 (Safety & Guardrails)**: Add Claim 8 (EFS false-positive
  refusals on reverse-engineering-flagged and math-metaphor-triggered
  requests) alongside the existing "What does the heart do?" anecdote from
  the June 2026 launch (`blog-latentspace-fable-5-mythos-launch.md` Claim 9)
  as a second data point supporting the guide's existing skepticism toward
  vendor-supplied narrow-impact estimates for opaque, probe/classifier-based
  safeguards — this appears to be a recurring pattern across successive Fable
  generations, not an isolated launch-week issue.

## Extraction Notes

- WebFetch's small-model summarizer initially paraphrased the article rather
  than preserving exact wording, and on a follow-up request refused to
  reproduce longer verbatim passages citing copyright. To obtain
  character-for-character quotes, this extraction fetched the raw article
  HTML directly via `curl` and parsed it into plain text with a Python script
  (stripping tags, preserving block-level line breaks), then read the full
  parsed text directly. All quotes in this note are taken from that
  directly-fetched raw text, not from WebFetch's summarized output.
- The article's own JSON-LD metadata confirms: `datePublished`:
  "2026-09-02T07:46:08+00:00"; `isAccessibleForFree`: false (the post is
  behind a paid-subscriber paywall past the AI Twitter Recap and AI Reddit
  Recap section header). The Claude Fable/Mythos 5.1 section extracted here
  — "Top Story," "Official claims and model positioning," "Technical details
  and numbers," "Safeguards and routing details," "Facts vs opinions,"
  "Different opinions and reactions," "Writing quality and the 'Claudese'
  discussion," "The safeguards story," "Mythos vs Fable," and "Practical
  product implications" — is fully accessible before the paywall boundary
  (which begins at the "AI Reddit Recap" section). No paywalled content was
  used or guessed at.
- No linked sub-pages (X/Twitter status URLs for named individuals' posts,
  the Artificial Analysis site, or the World Labs/OpenAI Astra coverage in
  the same digest) were independently fetched; all quotes and figures
  attributed to named accounts are as relayed by this AINews digest, not
  independently re-verified against the original tweets or benchmark pages.
  The World Labs Atlas and OpenAI Astra sections of the same digest were read
  but judged out of scope for this note, which is filed specifically against
  the Fable/Mythos 5.1 release per the triage comment's guidance.
- No contradiction meeting the `agents/MINER.md` §4a bar was identified; see
  the "Contradicts" entry above for the one internal tension considered
  (split rate-limit reports) and why it was not filed.
- Cross-references verified:
  - `blog-latentspace-fable-5-mythos-launch.md` Claim 1: confirmed (two
    variants of the same "Mythos-class" model, Fable 5 with added
    safeguards).
  - `blog-latentspace-fable-5-mythos-launch.md` Claim 4: confirmed (AA
    Intelligence Index, Fable 5 #1 at 64.9, ~5 points ahead of GPT-5.5).
  - `blog-latentspace-fable-5-mythos-launch.md` Claim 9: confirmed ("What
    does the heart do?" refusal anecdote).
  - `blog-simonwillison-claude-fable-5.md` Concrete Artifacts: confirmed
    ($10.00/$50.00 per million token input/output pricing for Fable 5).
  - `blog-simonwillison-introducing-opus-5.md` Claim 2: confirmed (Opus 5
    leading the AA leaderboard ahead of Fable 5, as of July 24, 2026).
  - `blog-simonwillison-fable51-system-prompt-copyright.md` Claim 5:
    confirmed (Fable 5.1 system prompt adds conciseness instruction and
    "genuinely/honestly/straightforward" prohibition).
  - `blog-anthropic-cursor-fable5-cursorbench.md` Claim 1: confirmed (Fable 5
    scored 72.9% at Max effort on CursorBench).
