---
source_url: https://simonwillison.net/2026/Jul/22/are-ai-labs-pelicanmaxxing/
source_type: blog-post
title: "Are AI labs pelicanmaxxing?"
author: Simon Willison
date_published: 2026-07-22
date_extracted: 2026-07-27
last_checked: 2026-07-27
status: current
confidence_overall: emerging
issue: "#2255"
---

# Are AI labs pelicanmaxxing?

> Willison's link-blog post surfaces Dylan Castillo's rigorous, systematic
> replacement for Willison's own long-running informal "pelican riding a
> bicycle" SVG benchmark: an 8-animal × 6-vehicle (48-prompt) factorial
> design, 3 samples per prompt, across 7 frontier models (1,008 SVGs total,
> ~$80 of API spend), scored by an LLM judge and analyzed with a
> difficulty-adjusting fixed-effects regression. The finding: no statistically
> significant evidence that any lab specifically optimizes for the
> pelican-on-a-bicycle combination — a concrete case study in how to design,
> and how to statistically de-bias, a multi-model creative-output evaluation.

## Source Context

- **Type**: blog-post (Willison's link-blog format — three short paragraphs
  of framing plus an inline screenshot and a blockquoted excerpt of Dylan
  Castillo's conclusion; auto-discovered via trusted feed `simon-willison`).
  Per MINER.md §1, this note follows the single substantive link in
  Willison's post to its primary source: Dylan Castillo's full analysis at
  `dylancastillo.co/posts/pelicanmaxxing.html`, fetched directly (raw HTML,
  not summarized) so that quotes and statistics could be reproduced verbatim.
  Almost all of the extracted claims below are Castillo's, not Willison's —
  Willison's own post contributes framing and endorsement, not new data.
- **Author credibility**: Simon Willison is a designated `trusted-feed`
  source in this repo (creator of Django, Datasette, `sqlite-utils`, `llm`)
  and the originator of the "pelican riding a bicycle" SVG test that this
  entire source examines (established in this corpus via
  `blog-simonwillison-glm51.md`, `blog-simonwillison-gpt55-codex-plugin.md`,
  and most directly `blog-simonwillison-kimi-k3-pelican-benchmark.md`). Here
  he is a curator amplifying someone else's rigorous follow-up work, not the
  investigator. Dylan Castillo, the linked author, identifies himself as
  affiliated with "Iwana Labs" in the article's own byline; the piece is a
  first-hand, code-and-data-backed empirical study (full pipeline and
  regression code published on GitHub) rather than vendor marketing or pure
  opinion.
- **Scope**: Covers a single, narrowly-scoped empirical question — whether
  AI labs deliberately train models to do better on the specific
  pelican-on-a-bicycle prompt than their general animal/vehicle drawing
  ability would predict — using SVG image generation across 7 named models.
  Does NOT cover agentic tool-calling, code generation, reasoning
  benchmarks, or any capability dimension besides single-shot SVG drawing
  quality as scored by an LLM judge. Does not claim to settle whether the
  pelican benchmark is diagnostic of *general* model quality (a distinct
  question addressed by `blog-simonwillison-kimi-k3-pelican-benchmark.md`).

## Extracted Claims

### Claim 1: Willison's own prior spot-checking of the pelican benchmark's generality was informal and unsystematic compared to Castillo's methodology
- **Evidence**: Willison's own direct comparison of his past testing practice to Castillo's study.
- **Confidence**: anecdotal (self-reported practitioner comparison)
- **Quote**: "I've been randomly spot-checking this in the past by testing models against other animals riding other types of vehicle, but never with anything close to the diligence of Dylan's methodology here."
- **Our assessment**: A useful admission from the benchmark's own creator that his prior informal cross-checks (which this corpus has otherwise cited as first-look capability signals, e.g. `blog-simonwillison-tencent-hy3.md` Claim 8) were not rigorous enough to actually test whether the benchmark itself was being gamed. This frames Castillo's work as an upgrade in evaluation rigor, not a duplicate of existing practice.

### Claim 2: Castillo tested 7 frontier models across a 48-prompt factorial design (8 animals × 6 vehicles), generating 3 samples per prompt for 1,008 total SVGs, at a total API cost of roughly $80
- **Evidence**: Castillo's own methodology section, describing the experimental design and stating the budget constraint directly.
- **Confidence**: settled (author-reported, directly checkable design parameters; full pipeline code published to GitHub)
- **Quote**: "I built a grid of 8 animals × 6 vehicles = 48 prompts, where the famous prompt is one cell" / "I generated 1,008 SVGs across seven frontier models, scored them with an LLM judge, and used Claude Fable 5 for the analysis." / "The whole experiment ran on roughly $80 of API credits."
- **Our assessment**: A concrete, low-budget template for systematic multi-model creative-output evaluation: a full factorial parameter sweep (animal × vehicle) rather than a single anecdotal prompt, repeated for statistical power (3 samples/cell), across a genuinely competitive model set (GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.5 Flash, Grok 4.5, Qwen3.7-Max, GLM-5.2, DeepSeek V4 Pro). The $80 total spend demonstrates this class of evaluation design doesn't require a large budget to be statistically meaningful.

### Claim 3: The evaluation pipeline used a three-stage process — automatic SVG-to-PNG rendering with retry-until-valid, LLM-judge scoring (1-5 scale for animal, vehicle, and action coherence), and separate LLM-based feature extraction (subject/vehicle identity, facing direction, open-ended scene elements)
- **Evidence**: Castillo's own pipeline description, naming the specific models used at each stage.
- **Confidence**: settled (author-described pipeline architecture)
- **Quote**: "Rendering: Each SVG is rendered to PNG. If a model returns no SVG or one that fails to render, I regenerate until it produces a valid one, and record the number of attempts. There were only 11 retries across the 1,008 generations." / "Judging: GPT-5.6 Luna scores each image with 1-5 ratings for the animal, the vehicle, and the coherence of the action... I use the average of the three, which I call the judge score." / "Feature extraction: For a more detailed analysis, I also passed each rendered image to Gemini 3.1 Flash-Lite, which recorded the animal and vehicle it recognized, which way the subject faces, and an open-ended list of scene elements."
- **Our assessment**: A reusable evaluation-pipeline pattern for anyone doing multi-model generative-output comparison: separate the "does the output even parse/render" check (with automatic retry, here only 11/1,008 = ~1.1% failure rate) from the subjective quality judging, and use a second, different model for structured feature extraction rather than overloading a single judge call with both scoring and description tasks.

### Claim 4: Pooled across all 7 models, pelicans rank 6th of 8 animals by mean judge rating — behind cats, whales, raccoons, herons, and antelopes — contradicting the hypothesis that labs specifically optimize pelican drawing
- **Evidence**: Castillo's pooled animal-rating analysis (Figure 1 in the source).
- **Confidence**: emerging (single-judge-model scoring, pooled across labs, but a directly stated numeric ranking)
- **Quote**: "The pelican is 6th of 8, behind cat, whale, raccoon, heron, and antelope. If AI labs were training on the benchmark, you'd expect pelicans at the top. Instead they're in the bottom half. All seven labs draw cats, whales, and raccoons better than pelicans."
- **Our assessment**: A direct, simple falsification test: if pelicans were a specially-trained-for target, they should rank near the top of the animal list, not in the bottom half. Castillo appropriately caveats that this alone can't separate "not specially trained" from "just an inherently hard animal to draw," which motivates Claims 6-7's difficulty-adjustment.

### Claim 5: Pooled across all 7 models, bicycles rank second-to-last of 6 vehicles by mean judge rating, in a near-tie with planes (which rank last)
- **Evidence**: Castillo's pooled vehicle-rating analysis (Figure 2 in the source).
- **Confidence**: emerging (single-judge-model scoring, pooled across labs)
- **Quote**: "Bicycles fare even worse. They sit second from last, in a near-tie with planes, which come in last... If labs were training on the benchmark, you'd expect bicycles near the top of this ranking. They're not."
- **Our assessment**: Same logic as Claim 4 applied to the vehicle half of the prompt — bicycles are not the best-drawn vehicle, which is the opposite of what deliberate benchmark optimization would predict. Castillo notes bicycles are also intrinsically harder to draw (two matching wheels, connected frame, handlebars, seat, pedals — the judge flags a missing/disconnected part on two-thirds of bicycle images), reinforcing the need for difficulty adjustment before drawing conclusions.

### Claim 6: The raw pelican-on-a-bicycle combination ranks #42 of the 48 animal-vehicle combinations tested, before any difficulty adjustment
- **Evidence**: Castillo's combined ranking of all 48 combos (Figure 3 in the source).
- **Confidence**: emerging (single-judge-model scoring; raw, pre-adjustment ranking)
- **Quote**: "Put the two together and the \"pelican on a bicycle\" ends up near the bottom of the ranking, at #42 of 48."
- **Our assessment**: The single most direct headline number in the piece — the famous benchmark prompt, unadjusted, scores in the bottom 13% of all combinations tested. Castillo is careful to flag this as still confounded by combination-specific difficulty, which is exactly what the regression in Claim 7 controls for.

### Claim 7: A difficulty-adjusted fixed-effects regression (score ~ lab + animal×vehicle, with per-lab interaction terms for pelican, bicycle, and the pelican-bicycle cell) found no statistically significant benchmark-specific effect for any lab, on any of pelican, bicycle, or the pelican-bicycle combination
- **Evidence**: Castillo's regression methodology and reported per-lab effect sizes and p-values, with the full estimate table published to the linked GitHub repo.
- **Confidence**: emerging (author-run statistical analysis; methodology described but not independently re-run by this extraction; code is public and checkable)
- **Quote**: "Every per-lab pelican effect (the lab's boost on pelicans across all six vehicles) lands between -0.11 and +0.14 judge points, and none comes close to significance (smallest p = 0.25)." / "No pelican-bicycle cell effect (the extra boost on the specific combination, on top of the lab's pelican and bicycle effects) clears p < 0.05. The largest positive is GLM-5.2 at +0.35 (p=0.12), which is the one I mentioned earlier. It's the closest thing to a signal in this experiment, but still within chance."
- **Our assessment**: This is the core statistical result the whole piece builds toward — a proper difficulty-adjusted analysis, not just raw rankings, and it still finds nothing. The one nominally-significant sub-result (Gemini 3.5 Flash's bicycle effect, p=0.022) is explicitly shown not to survive multiple-comparisons correction (Claim 8), which is the kind of rigor a simpler "eyeball the rankings" analysis would have missed — a good template for the guide's evaluation-methodology guidance on correcting for multiple comparisons in any per-model/per-category statistical testing.

### Claim 8: The one nominally-significant per-lab effect found (Gemini 3.5 Flash's bicycle-drawing boost, p=0.022) does not survive Bonferroni correction across the 21 statistical tests run, and is consistent with the single false positive chance alone predicts
- **Evidence**: Castillo's explicit multiple-comparisons accounting.
- **Confidence**: settled (a directly stated statistical correction on the author's own reported numbers)
- **Quote**: "But with 21 tests at p < 0.05, chance alone predicts about one false positive (21 × 0.05 ≈ 1.05), and one is exactly what came up. It also doesn't survive a multiple-comparisons correction: the Bonferroni threshold across the 21 tests is 0.05/21 ≈ 0.002, and its p-value is 0.022."
- **Our assessment**: This is a model of statistical honesty that the guide should hold up as a positive example: rather than reporting the one "significant" finding as a discovery, Castillo explicitly computes the expected false-positive rate for the number of tests run and shows the one hit is exactly what chance predicts. Any guide section on evaluation methodology should flag this as the standard multiple-comparisons practitioners should apply when testing many models/categories at once (e.g., leaderboards with dozens of per-category breakdowns).

### Claim 9: All 21 pelican-on-a-bicycle images (across all 7 labs) face right — the only one of the 48 animal-vehicle combinations where every single image agrees on direction — but this is not anomalous, since right-facing is the modal direction for 60% of all 1,008 images and three other combinations independently reach 90%+ agreement
- **Evidence**: Castillo's direction/composition analysis, intended to test whether the pelican-bicycle scene looks "memorized."
- **Confidence**: emerging (author-run frequency analysis with an explicit statistical framing of why the finding is not surprising)
- **Quote**: "All 21 pelican-bicycle images, across all seven labs, face right. No other animal/vehicle combination does that." / "However, facing right is common: 60% of all 1,008 images do it." / "antelope on a scooter and pelican on a scooter land at 20 of 21, and heron on a bicycle at 19 of 21. So 21 out of 21 doesn't seem like an outlier."
- **Our assessment**: This directly addresses (and refutes) a specific counter-argument — that the pelican-bicycle scene "looks memorized" because of its consistent right-facing composition — by showing the base rate for right-facing images is already 60% and that three other combinations come within one image of the same unanimous result. A good example of pre-registering and testing an alternative hypothesis (memorization) rather than stopping at the first null result.

### Claim 10: A scene-element extraction pass found no unique "memorized" elements specific to the pelican-bicycle combination, but did find strong recurring elements for several *other* animal-vehicle combinations (flamingo-on-boat always includes a sun; otter-on-plane includes a scarf 38% of the time; cat-on-bicycle includes a basket 38% of the time)
- **Evidence**: Castillo's open-ended scene-element extraction analysis (via Gemini 3.1 Flash-Lite), comparing the pelican-bicycle combo's element consistency against other combos.
- **Confidence**: emerging (single-extractor-model analysis; a comparative rather than absolute measurement)
- **Quote**: "Every single flamingo on a boat has a sun in it. Otters on planes wear scarves 38% of the time. Cats on bicycles get a basket 38% of the time." / "The pelican on a bicycle doesn't seem to have anything particularly different about it. It just has some elements that appear more frequently, like every other animal-vehicle combination."
- **Our assessment**: An unexpected, incidental finding: models do have strong, consistent stylistic associations for *some* specific animal-vehicle pairings (flamingo+boat+sun being the strongest example found) — just not for pelican+bicycle specifically. This is itself a novel, guide-relevant observation about model output consistency/stereotypy on structured creative prompts, independent of the pelicanmaxxing question.

### Claim 11: Castillo names two limitations he cannot rule out: (1) a single LLM judge (GPT-5.6 Luna) with no inter-rater reliability check, drawn from the same model family as one of the tested contestants (GPT-5.6 Terra); and (2) "SVGmaxxing" — labs optimizing SVG-generation capability broadly (which some labs, per Castillo, do openly) is indistinguishable in this design from genuine general capability, and would raise every cell at once rather than showing up as a pelican-bicycle-specific effect
- **Evidence**: Castillo's own "Limitations" section, stated directly and without hedging.
- **Confidence**: settled (author-disclosed methodological limitations)
- **Quote**: "Using a single LLM judge for scoring. Every score here comes from one model, GPT-5.6 Luna, looking at one image at a time. I didn't do much alignment and didn't check how often it agrees with itself on a re-run... The judge is also from the same family as one of the contestants, GPT-5.6 Terra." / "SVGmaxxing. A lab that optimized SVG generation as a whole (or a subset such as animals on vehicles) rises on every cell at once and looks identical to a lab that's just good. Some labs, such as Google/DeepMind, openly do this. This experiment can't detect that."
- **Our assessment**: The SVGmaxxing caveat is the single most important limitation for how the guide should frame this source's conclusion: the study rules out narrow, prompt-specific gaming of "pelican riding a bicycle," but explicitly does *not* rule out (and Castillo says some labs openly practice) broader capability-class optimization for SVG/vector-graphics generation as a whole. The "no pelicanmaxxing" headline should be cited with that scope limitation intact, not as a blanket claim that labs don't optimize for benchmarks at all.

### Claim 12: A word-choice ambiguity ("plane" vs. "airplane") caused several models to draw a flat geometric plane/surface instead of an aircraft, measurably depressing that vehicle category's scores — the only vehicle where the feature extractor sometimes found no vehicle at all
- **Evidence**: Castillo's own observation and quantification of the prompt-wording artifact.
- **Confidence**: settled (a directly observed and quantified prompt-design failure mode)
- **Quote**: "I should've picked \"airplane\" instead of \"plane\" because models often read it geometrically. They drew the animal standing on a flat surface instead of flying an aircraft. The plane is the only vehicle where the feature extractor sometimes found no vehicle at all (25 of 168 images, against zero for the other five), and 20% of plane images scored a 1 or 2 on the vehicle rating, against 5% for bicycles and none at all for boats, scooters, or skateboards."
- **Our assessment**: A concrete, quantified example of how lexical ambiguity in an evaluation prompt (not model capability) can be the actual driver of a category's low scores — a caution directly applicable to any guide section on designing evaluation prompts: word choice needs to be checked for alternate readings before the results are interpreted as a capability signal, and this can be caught (as here) by cross-checking the low-scoring category against a structured feature-extraction pass rather than the judge score alone.

## Concrete Artifacts

### Experimental design parameters (Castillo, dylancastillo.co, retrieved 2026-07-27)
```
Animals (8):  pelican, flamingo, heron, otter, raccoon, antelope, whale, cat
Vehicles (6): bicycle, unicycle, skateboard, scooter, plane, boat
Prompts:      8 x 6 = 48
Samples per prompt: 3
Models tested (7): GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.5 Flash,
                   Grok 4.5, Qwen3.7-Max, GLM-5.2, DeepSeek V4 Pro
Total SVGs generated: 1,008
Generation temperature: 1.0 (same requested reasoning effort across models)
Judge model: GPT-5.6 Luna (1-5 ratings: animal, vehicle, action coherence)
Feature-extraction model: Gemini 3.1 Flash-Lite (subject/vehicle ID,
                          facing direction, open-ended scene elements)
Rendering retries: 11 across 1,008 generations
Total API cost: ~$80
Code/data: https://github.com/dylanjcastillo/blog/tree/main/_extras/pelicanmaxxing
```

### Regression results summary (Castillo's fixed-effects model: score ~ lab + animal x vehicle + per-lab pelican/bicycle/cell interactions)
```
Per-lab pelican effect range:      -0.11 to +0.14 judge points (smallest p = 0.25)
Per-lab bicycle effect range:      -0.18 (Grok 4.5, p=0.11) to +0.27 (Gemini 3.5 Flash, p=0.022)
Per-lab pelican-bicycle cell effect (largest): GLM-5.2 at +0.35 (p=0.12)
Statistical tests run: 21 (7 labs x 3 effect types)
Expected false positives at p<0.05 across 21 tests: ~1.05
Actual significant results (uncorrected): 1 (Gemini bicycle effect)
Bonferroni-corrected threshold: 0.05/21 ~ 0.002 (Gemini's p=0.022 does not clear this)
Confidence interval width: ~+/-0.6 judge points on average
```

### Facing-direction consistency by vehicle and animal (Castillo, Evidence #5)
```
By vehicle:  scooter 83% right / bicycle 81% right / skateboard 60% right /
             plane 58% right / unicycle 45% right / boat 35% right
By animal:   antelope 78% right / pelican 78% right / heron 77% right /
             whale 65% right / flamingo 64% right / otter 45% right /
             cat 40% right / raccoon 36% right
Pelican-on-bicycle: 21/21 (100%) face right -- the only 21/21 combination,
  but antelope-on-scooter and pelican-on-scooter both reach 20/21, and
  heron-on-bicycle reaches 19/21.
```

## Cross-References

- **Corroborates**: `blog-simonwillison-tencent-hy3.md` (Claim 8), which
  documents Willison's own first-hand, single-run pelican-SVG test as an
  informal capability signal — this source's Claim 1 explicitly frames that
  exact style of ad hoc spot-check as the less-rigorous baseline Castillo's
  systematic study improves on.
- **Contradicts**: None identified, and no contradiction issue filed. This
  source's conclusion (no evidence of narrow, prompt-specific benchmark
  optimization) does not conflict with
  `blog-simonwillison-kimi-k3-pelican-benchmark.md` Claim 5 (the pelican
  benchmark's correlation with *general* model quality has "mostly
  severed") — the two sources address different questions. Willison's
  Kimi K3 note asks whether the benchmark still *tracks overall capability*;
  Castillo's study asks whether labs *specifically train toward* this one
  benchmark. A model could plausibly be true on both counts (the benchmark
  stops tracking general quality for reasons unrelated to deliberate
  targeting, e.g. broad SVG-capability convergence per this note's Claim 11
  "SVGmaxxing" caveat) without contradiction.
- **Extends**: `blog-simonwillison-kimi-k3-pelican-benchmark.md` (Claim 6,
  Willison's observation that the pelican test "doesn't touch at all on the
  thing that matters most for today's models: agentic tool calling") — this
  source provides the rigorous statistical backing for treating the pelican
  benchmark's *specific* form (this exact animal/vehicle pair) as not
  specially gamed, which is a distinct but complementary caution to Kimi
  K3's note on the benchmark's fading *general* diagnostic value. Together
  the two sources give the guide both halves of a "why not to over-index on
  the pelican benchmark" argument: it doesn't measure what matters most
  (Kimi K3 note), and even on its own terms, it isn't being specifically
  gamed by labs in gross, isolable ways this study could detect within its
  budget and design (this note, with the SVGmaxxing caveat as an important
  scope limit).
- **Novel**: First corpus source to apply a designed factorial experiment
  (8x6 parameter sweep) with a difficulty-adjusting fixed-effects
  regression and explicit multiple-comparisons correction to a multi-model
  creative-output comparison. First corpus documentation of the
  "SVGmaxxing" concept (broad capability-class benchmark optimization,
  contrasted with narrow single-prompt gaming) as a named, explicit
  limitation of any single-benchmark evaluation design. First corpus
  documentation of model-consistent stylistic associations for specific
  non-benchmark animal-vehicle prompts (flamingo+boat+sun, otter+plane+scarf,
  cat+bicycle+basket) as an incidental finding.

## Guide Impact

- **Chapter on evaluation methodology (per Prospector triage, Ch03)**: Cite
  this source as a worked example of upgrading an informal single-prompt
  benchmark into a statistically rigorous multi-model comparison: (1) use a
  full factorial design (animal x vehicle) rather than one anecdotal case,
  (2) repeat samples for statistical power, (3) fit a difficulty-adjusting
  regression rather than comparing raw scores, and (4) apply
  multiple-comparisons correction (Bonferroni) before treating any one
  per-model result as significant (Claims 2, 7, 8). Recommend the guide add
  a callout that a single nominally-significant p-value among many tests
  run (here, 1 of 21) is exactly what chance predicts and should not be
  reported as a finding without correction.
- **Chapter on evaluation methodology — prompt design pitfalls (Ch03)**:
  Add Claim 12 (the "plane" vs. "airplane" wording ambiguity) as a concrete
  example that a category's low benchmark score can be a prompt-wording
  artifact rather than a capability gap — recommend cross-checking
  low-scoring categories against a structured feature-extraction pass (what
  did the model actually draw?) before concluding a capability difference.
- **Chapter on model capability assessment / informal benchmarks (Ch03-04,
  alongside `blog-simonwillison-kimi-k3-pelican-benchmark.md`)**: Update any
  existing discussion of the pelican-riding-a-bicycle benchmark to note this
  source's finding — no statistically significant evidence that any of the
  7 tested labs specifically optimizes for the pelican-bicycle combination
  (Claims 4-8) — while flagging the explicit scope limit (Claim 11) that
  broader, capability-class "SVGmaxxing" is not ruled out and is stated by
  the author to be openly practiced by some labs (Google/DeepMind is named).
  The guide should not cite this source as evidence labs never optimize for
  public benchmarks generally — only that this one narrow prompt-pair is not
  detectably targeted.

## Extraction Notes

- Willison's own post is short (three paragraphs plus a screenshot and a
  blockquote excerpting Castillo's conclusion); nearly all substantive
  content in this note comes from following the single link to Castillo's
  full article, per MINER.md §1's instruction to follow substantive linked
  pages. Both pages were fetched as raw HTML (not via a summarizing
  WebFetch pass, which on an initial attempt refused to reproduce quoted
  text citing copyright and returned only a thin paraphrase) and every
  `Quote` field above was verified character-for-character against that raw
  HTML before inclusion, per MINER.md §2a.
- Did not follow the Hacker News discussion thread linked from Willison's
  post (id 49010129) or the GitHub repo containing Castillo's full pipeline
  code and regression estimate table — the repo is referenced in Claim 7/8
  and the Concrete Artifacts section by URL but its contents (raw code, not
  prose analysis) were not separately extracted as claims.
- The apparent typo in Willison's blockquoted excerpt of Castillo's
  conclusion ("and and its first pelican-on-bicycle sample caught my eye")
  is present in Willison's post's raw HTML but not in Castillo's own article
  (which reads "and its first pelican-on-bicycle sample"). This note quotes
  each source from its own text rather than reproducing Willison's
  copy-paste artifact as if it were Castillo's wording.
- Confidence set to `emerging` overall: the experimental design, retry
  counts, and statistical corrections (Claims 2, 3, 8, 12) are directly
  checkable, author-disclosed facts, but the core findings rest on a single
  LLM judge model with no disclosed inter-rater reliability check (Claim 11)
  and a $80 budget capping sample size at 3 per cell — real constraints the
  author himself discloses. This is a well-designed but resource-constrained
  single-author study, not an independently replicated result.
