---
source_url: https://www.latent.space/p/ainews-muse-spark-13-matches-gpt
source_type: blog-post
title: "[AINews] Muse Spark 1.3 matches GPT-5.6-Sol, confirming Meta Superintelligence as the newest Frontier Lab, >90% discount for training"
author: swyx / smol.ai (AINews aggregation, published under Latent Space)
date_published: 2026-09-03
date_extracted: 2026-09-21
last_checked: 2026-09-21
status: current
confidence_overall: anecdotal
issue: "#3596"
---

# [AINews] Muse Spark 1.3 matches GPT-5.6-Sol, confirming Meta Superintelligence as the newest Frontier Lab, >90% discount for training

> A daily AI-news aggregation digest (covering 8/22–8/24/2026, sourced from 544
> tracked Twitter accounts and 12 subreddits) documenting Meta's Muse Spark 1.3
> release: a #3-of-all-models Artificial Analysis Intelligence Index ranking
> (no numeric score given), a repeated-but-still-unfulfilled promise of open
> weights, an extension of the same data-sharing-conditioned "contributor"
> pricing tier already documented for Spark 1.2 (Meta's own pricing table is
> an image, not transcribed as text), a screenshotted MRCR 512k–1m score of
> 98.1% that Reddit commenters treat with real skepticism, and — notably —
> zero uses of the phrase "Meta Superintelligence" anywhere in the article's
> own free-preview body text, despite that phrase driving the headline. This
> is the first dedicated source note in the corpus for Muse Spark 1.3, which
> `blog-simonwillison-gpt6-astra-launch.md` had flagged as a release existing
> in the corpus only as an index-standing mention, with "no ... score,
> pricing, release date, or capability detail."

## Source Context

- **Type**: blog-post (daily news-aggregation digest, "AINews" — a section of
  Latent Space / smol.ai, published 2026-09-03 for the 8/22–8/24 news cycle,
  per the post's own dateline: "AI News for 8/22/2026-8/24/2026. We checked
  12 subreddits, 544 Twitters and no further Discords."). Editorially this is
  a curated roundup of Twitter/X and Reddit discussion, written and lightly
  synthesized by the AINews/swyx editorial process, not original reporting or
  an interview — the same format as `blog-latentspace-ainews-meta-harness-summer.md`.
- **Author credibility**: swyx (Shawn Wang) co-founded Latent Space; AINews is
  an automated-plus-edited aggregation product whose value is curation and
  framing of what AI-engineering Twitter/Reddit found noteworthy that day, not
  first-party reporting. Individual claims trace back to named Twitter
  accounts (@ArtificialAnlys, @shengjia_zhao, @alexandr_wang) or Reddit
  threads quoted/paraphrased by the digest, so credibility varies
  claim-by-claim — read as "notable people/threads said X," not independently
  verified fact. Two of the post's own benchmark claims (the AAII #3 ranking,
  the MRCR 98.1% score) are relayed from screenshotted images embedded in
  tweets/Reddit posts, not from text Meta itself published in the post — a
  weaker evidentiary chain than a directly-quoted vendor announcement.
- **Scope**: Covers, in the portion readable via this post's free preview
  (see Extraction Notes on the paywall): (1) the Muse Spark 1.3 launch story
  and pricing framing; (2) an "AI Twitter Recap" spanning agent-engineering
  courses, model-architecture rumors (Astra), agent-harness/RL tooling,
  Gemini 3.8 Flash Cyber, and a dedicated Muse Spark 1.3 item; (3) the start
  of an "AI Reddit Recap" covering a Muse Spark/Spark-X2.5 thread and a
  Qwen3.8 benchmarks thread. Does **not** cover (paywalled, not reached):
  the remainder of the Reddit recap beyond the Qwen3.8 section, per the
  post's stated 4,776-word total against the ~2,601 words recovered in the
  free preview (see Extraction Notes). Does not include Meta's own official
  announcement text — the post relays Zuckerberg's/Meta's claims exclusively
  via embedded screenshot images and secondhand paraphrase, never a directly
  quoted or transcribed Zuckerberg statement.

## Extracted Claims

### Claim 1: Per Artificial Analysis's Intelligence Index (AAII), Muse Spark 1.3 is now ranked the #3 model in the world — a ranking the digest itself treats as surprising, with no numeric score given
- **Evidence**: The digest's opening sentence, sourced to a linked
  @ArtificialAnlys tweet, expressing surprise via its own punctuation.
- **Confidence**: emerging (a specific, named third-party benchmark
  aggregator's ranking claim, though only the rank — not a numeric score —
  is given in the post's own text, and the underlying tweet was not
  independently fetched for this note)
- **Quote**: "Per AAII it is now the #3 model in the world (!?!)"
- **Our assessment**: This is the first numeric-adjacent standing this corpus
  has for Muse Spark 1.3 specifically — `blog-simonwillison-gpt6-astra-launch.md`
  Claim 4 only established that Muse Spark 1.3 ranks *ahead of* GPT-6 Astra
  and GPT-5.6 Sol on the same Intelligence Index, with no score or rank
  given. This is directionally consistent (a top-3 ranking is compatible
  with "ahead of Astra/Sol, which are themselves tied at 61"), but a "(!?!)"
  reaction from the digest's own author signals this is being read as a
  genuinely surprising jump, not confirmation of a long-expected outcome —
  worth flagging that the guide should not cite "#3 in the world" as a
  settled, checkable score without the underlying Artificial Analysis number.
  Note also that "#3 in the world" on the *Intelligence Index* should not be
  conflated with coding-agent performance specifically — see Cross-References
  for a materially less flattering Coding Agent Index score for the same
  model reported elsewhere in the corpus.

### Claim 2: Meta again promises Muse Spark open weights "coming soon" for the 1.3 release — the same unfulfilled promise pattern documented for Spark 1.2 a month earlier
- **Evidence**: The digest's own framing plus the Reddit recap's description
  of the screenshotted Zuckerberg/X announcement.
- **Confidence**: emerging (a specific, repeated, checkable claim about
  release status — "coming soon" said twice about two different version
  numbers a month apart is a directly comparable, trackable pattern)
- **Quote**: "Just look at the confidence displayed finally putting up
  comparable numbers to the frontier models from OpenAI and Anthropic (Opus,
  not Fable)… and promising that it will be open weights as well(!!!):"
- **Quote (Reddit recap)**: "a screenshot of a Mark Zuckerberg/X post
  announcing Muse Spark 1.3 rollout, claiming major improvements in coding,
  agentic workflows, and long-context tasks, with Muse Spark open weights
  "coming soon.""
- **Our assessment**: This is a direct repeat of the same promise: the
  linked prior AINews post from 2026-08-10 (`latent.space/p/ainews-muse-glimmer-and-spark-open`,
  followed as a substantive linked page per MINER.md §1) states Meta
  "released MSL's first real open weights frontier-ish small LLM, with Spark
  to also be released soon" at the time of the Muse Glimmer launch — i.e.
  Spark 1.2 weights were promised "soon" in August, and now, a month later,
  Spark 1.3 weights are again promised "coming soon." Neither this source
  nor any existing corpus note documents Spark weights of any version
  actually having shipped. The guide should treat Meta's open-weights
  promise for the hosted Spark line as a standing, repeatedly-renewed
  commitment rather than an imminent, dated release — worth an explicit
  "promised twice, not yet delivered" framing rather than repeating "coming
  soon" as if it were new news each time.

### Claim 3: Meta offers Muse Spark 1.3 at a 90%+ discount for customers who opt in to letting Meta use their data for training — continuing the same data-sharing-conditioned "contributor" pricing lever Meta introduced for Spark 1.2
- **Evidence**: The digest's own pricing-section sentence, illustrated with an
  embedded pricing-table image whose exact figures are not transcribed as
  text in the post (see Concrete Artifacts and Extraction Notes).
- **Confidence**: emerging (a specific, quantified discount percentage stated
  in the post's own prose, though the underlying pricing table itself is an
  image the post does not transcribe, so exact dollar figures for 1.3 are
  not independently checkable from this source)
- **Quote**: "They have an interesting pricing model where it is 90%+
  cheaper if you opt in to training:"
- **Our assessment**: This corroborates and extends
  `blog-simonwillison-muse-code-spark-12.md` Claim 8, which documents the
  exact figures for the equivalent Spark 1.2 tier: standard `muse-spark-1.2`
  at $1.25/M input, $4.25/M output vs. the data-sharing-consented
  `muse-spark-1.2-contributor` at $0.10/M input, $0.20/M output — a ~92%
  discount, matching "90%+" almost exactly. This is strong evidence Meta is
  applying the identical two-tier, data-rights-conditioned pricing structure
  to Spark 1.3 rather than introducing a new pricing mechanism — the "90%+"
  headline figure in this source is not a new discovery so much as
  confirmation that the pattern documented for 1.2 persists into 1.3. The
  guide's existing citation of Claim 8's pricing lever (data rights vs.
  efficiency as two orthogonal ways vendors move price) should be updated to
  note it is now a two-release pattern for Meta specifically, not a one-off.

### Claim 4: A screenshotted benchmark table in Zuckerberg's announcement positions Muse Spark 1.3 above Muse Spark 1.2 and competitive with models labeled "GPT 5.6 Sol" and "Opus 5" across agent, long-context, and coding evaluations
- **Evidence**: Reddit recap's description of the announcement screenshot's
  contents (a secondhand description of an image, not a transcription of
  Meta's own benchmark numbers).
- **Confidence**: anecdotal (a Reddit summary of a benchmark table visible
  only as a screenshot image; no numeric scores, axis labels, or benchmark
  names are given in the readable text)
- **Quote**: "The included benchmark table positions Muse Spark 1.3 above
  Muse Spark 1.2 and competitive with models labeled GPT 5.6 Sol and Opus 5
  across agent, long-context, and coding evaluations, though the Reddit
  post's author notes Spark may be too large for their hardware and says
  they are waiting for Llama 5 or an intermediate model between Glimmer and
  Spark."
- **Our assessment**: This is the closest this source comes to explaining
  the headline's "matches GPT-5.6-Sol" framing, but it is thin: no numbers,
  only "competitive with" and "above [1.2]" from a Reddit poster's reading
  of a chart image. The corpus's more precise prior data point
  (`blog-simonwillison-gpt6-astra-launch.md` Claim 4: Astra "trails" Muse
  Spark 1.3 on the Intelligence Index, where Astra and Sol are tied at 61)
  implies Muse Spark 1.3 actually scores *above* Sol on that specific index,
  not merely "matches" it — a mild tension between this post's own headline
  framing ("matches") and the more precise index-standing claim already in
  the corpus. Not filed as a contradiction: both are vague/directional
  (neither gives a Muse Spark 1.3 number), and "matches" in a headline is
  plausibly loose marketing-adjacent framing rather than a specific,
  falsifiable claim in tension with a specific falsifiable claim elsewhere.

### Claim 5: Muse Spark 1.3 reportedly scored 98.1% on the MRCR 512k–1m long-context benchmark, a figure Reddit commenters treated as unusually high and asked whether it implies "context rot" is solved at million-token scale
- **Evidence**: Reddit recap's summary of commenter reaction to a number
  visible in the same screenshotted benchmark table.
- **Confidence**: anecdotal (a single number read off a screenshot by Reddit
  commenters, not independently verified, not corroborated by any other
  source in the corpus, and not even directly quoted from Meta's own text —
  this is a number Reddit users extracted from an image)
- **Quote**: "Commenters highlighted an unusually high reported long-context
  result: MRCR 512k–1m at 98.1%, with one user asking whether this implies
  Muse Spark has effectively solved "context rot" at million-token scale. If
  accurate, that benchmark would be the most technically notable claim in
  the thread because sustained retrieval/reasoning quality across 512k+
  contexts is still a major weakness for many open and closed models."
- **Our assessment**: This is the single most specific, checkable-if-verified
  number in the whole source, and also the one with the weakest chain of
  custody (screenshot → Reddit reader → digest paraphrase, with the digest
  itself flagging "if accurate"). It's directly relevant to
  `research-wasnotwas-context-compaction.md`'s empirical documentation of
  compaction/context-rot as a real, measured engineering problem across
  seven open-source harnesses, and to `blog-simonwillison-muse-code-spark-12.md`
  Claim 4 (Meta training Spark 1.2 explicitly against compaction
  trajectories) — a 98.1% MRCR score at 512k–1m tokens, if independently
  confirmed, would be a meaningful data point that long-context retrieval
  degradation is being substantially reduced at the frontier. Given the
  weak sourcing, the guide should not cite the 98.1% figure as a verified
  number — flag it as "an unverified, screenshot-sourced claim worth
  independent confirmation" rather than fact.

### Claim 6: Meta (via @shengjia_zhao) positions Muse Spark 1.3 as the strongest model in the Spark line specifically for agentic and coding tasks, emphasizing longer-horizon work and more reliable compliance with complex instructions
- **Evidence**: Digest paraphrase of a named Meta-affiliated announcement
  tweet, in the dedicated "Meta Muse Spark 1.3" Twitter-recap subsection.
- **Confidence**: emerging (a specific, named vendor-affiliated framing
  statement, consistent with — not merely asserted independently of — the
  training methodology already documented for the prior version)
- **Quote**: "Meta launched Muse Spark 1.3 for agentic and coding workloads:
  @shengjia_zhao introduced Muse Spark 1.3 as the strongest model in the
  Spark line for agentic and coding tasks, with emphasis on longer-horizon
  work and more reliable compliance with complex instructions."
- **Our assessment**: This directly continues the trajectory
  `blog-simonwillison-muse-code-spark-12.md` documents for Spark 1.2: Claim
  3 there records Spark 1.2 being "extensively trained on long-horizon
  coding tasks," and Claim 4 records explicit training against
  compaction/subagent/goal trajectories. This source gives no new mechanism
  detail (no equivalent of the co-training-with-Muse-Code disclosure,
  training methodology, or benchmark names for 1.3), only a restated
  positioning claim — corroborating continuity of Meta's stated strategy
  rather than revealing anything new about how 1.3 specifically was built.

### Claim 7: Twitter reaction to Muse Spark 1.3 emphasized favorable price/performance, with one prominent account (@alexandr_wang) highlighting what the model can do "for a single dime," and other users comparing it favorably on speed and token efficiency against competing "xhigh"-tier offerings
- **Evidence**: Digest paraphrase of Twitter reactions in the same Meta
  Muse Spark 1.3 subsection.
- **Confidence**: anecdotal (Twitter reactions, no controlled comparison or
  numbers given for "a single dime" or the speed/efficiency comparison)
- **Quote**: "Community reactions emphasized its price/performance envelope,
  including @alexandr_wang calling out what it can do "for a single dime,"
  while other users compared it favorably on speed and token efficiency
  versus competing "xhigh" offerings."
- **Our assessment**: Consistent in spirit with, but not a substitute for,
  the concrete corpus data point in `blog-simonwillison-astra-pelican-comparison-grid.md`
  Claim 4, which quantifies a comparable cost/quality tradeoff claim for a
  different model (GPT-6 Astra's "low" tier beating GPT-5.6 Sol at any tier
  for 9.55 cents). No comparable dollar figure or benchmark comparison is
  given for Muse Spark 1.3 here — "for a single dime" is a rhetorical
  flourish from a named account, not a quantified claim the guide can cite
  as evidence, though the account (Alexandr Wang, Meta's Chief AI Officer as
  of this corpus's timeline) carries some authority as a Meta-affiliated
  voice speaking to Meta's own pricing.

### Claim 8: Reddit commenters read the Muse Spark 1.3 benchmark claims as evidence of technical convergence across frontier labs ("no secret sauce," a "few months" gap), while a separate thread of commenters speculated the model could be trillion-parameter scale, raising local-deployment feasibility doubts despite the promised open weights
- **Evidence**: Reddit recap's summary of the top-level thread's comment
  section.
- **Confidence**: anecdotal (Reddit commenter speculation, no confirmed
  parameter count from Meta)
- **Quote**: "Commenters frame the results as evidence that multiple leading
  labs are converging technically, with one saying there is "no secret
  sauce" and that frontier gaps may only be a few months."
- **Quote (parameter speculation)**: "Several commenters questioned the
  likely parameter count behind the displayed scores, with speculation that
  Muse Spark could be trillion-parameter scale if the benchmarks are
  accurate. That raised practical deployment concerns: it may not be
  locally runnable for hobbyists, but open weights could still be useful
  for organizations needing non-Chinese model options for policy/compliance
  reasons."
- **Our assessment**: The "no secret sauce" / convergence framing echoes the
  broader cross-vendor convergence theme already in the corpus (e.g.
  `blog-simonwillison-muse-spark.md`'s file-editing API convergence, Claim
  2), now applied to raw capability rather than tool design. The
  parameter-count speculation is unconfirmed but relevant to Claim 2's
  open-weights promise: if Muse Spark 1.3 is genuinely trillion-parameter
  scale, "open weights" would not translate to practical local/hobbyist
  deployability even if delivered, a caveat worth pairing with any future
  guide mention of Meta's open-weights commitment for the Spark line
  specifically (as distinct from the much smaller, already-shipped Muse
  Glimmer, `blog-simonwillison-muse-glimmer.md`).

### Claim 9: Despite driving the article's headline ("confirming Meta Superintelligence as the newest Frontier Lab"), the phrase "Meta Superintelligence" does not appear anywhere in this post's own readable body text
- **Evidence**: Direct textual check of the ~2,601-word free-preview portion
  of the post (see Extraction Notes) against the headline framing; zero
  matches for "superintelligence" in any casing.
- **Confidence**: settled (a directly checkable absence in the text that was
  read; caveated by the fact that roughly 45% of the post, per its own
  stated word count, is paywalled and was not read — see Extraction Notes)
- **Quote**: (no direct quote; the claim is an absence — see paraphrase
  above and in Our assessment)
- **Our assessment**: This directly answers two of the three Prospector
  triage comments' key question ("Does the 'Meta Superintelligence' framing
  introduce new patterns?"). The answer, based on the readable text, is no:
  "Meta Superintelligence Labs" (MSL) is pre-existing terminology, not new
  framing invented by this post. The prior AINews post this article links
  to as "Zuck's big comeback letter" (`latent.space/p/ainews-muse-glimmer-and-spark-open`,
  2026-08-10, followed as a substantive linked page per MINER.md §1) already
  uses "MSL" repeatedly and unremarkably: "MSL seems to be feeling a second
  wind this year, as they slowly ramped up with the Dreamer acquisition and
  then Muse Spark and recently Muse Code. For a while it seemed like MSL
  was being rather timid with the launches… but today that all changed,"
  and itself links further back to an even earlier post titled
  "ainews-meta-superintelligence-labs." So this headline's "confirming Meta
  Superintelligence as the newest Frontier Lab" reads as this digest's own
  editorial framing — treating the #3 AAII ranking (Claim 1) as
  confirmation of a lab identity and "comeback" narrative AINews had
  already been tracking for at least a month — rather than as evidence
  Meta itself is newly branding around "Meta Superintelligence" in this
  specific release. The guide should not cite this post as the origin or
  a first announcement of "Meta Superintelligence" framing.

### Claim 10: Muse Spark 1.3's launch is explicitly framed by the digest as fulfilling a promise made in Zuckerberg's "big comeback letter" from the prior month — the same essay-driven "personal superintelligence" narrative already covered by an earlier AINews post about Muse Glimmer and Spark 1.2
- **Evidence**: The digest's own opening sentence, linking directly to the
  2026-08-10 prior post.
- **Confidence**: settled (a directly checkable narrative link between two
  posts in the same publication, both read for this note)
- **Quote**: "Muse Spark 1.3, promised in Zuck's big comeback letter last
  month, definitely deserved the title story win today."
- **Our assessment**: This confirms Muse Spark 1.3 is being read by AINews's
  own editorial process as a continuation of a single "Meta comeback" arc
  that started with the August 10 Muse Glimmer/Spark-1.2 announcement
  (essay reference: "Meta is the company primarily focused on building
  personal superintelligence for everyone," from the 2026-08-10 post),
  not a separate or newly-motivated release. This strengthens Claim 9's
  reading that "Meta Superintelligence" in this post's headline is a
  callback to an already-established narrative thread rather than a new
  naming event.

## Concrete Artifacts

### Reported figures for Muse Spark 1.3 (all secondhand — screenshot- or
tweet-sourced, none independently transcribed by the digest as text)
```
Source: latent.space/p/ainews-muse-spark-13-matches-gpt, 2026-09-03

Artificial Analysis Intelligence Index (AAII) rank: #3 model in the world
  (no numeric score given in readable text)
Training opt-in pricing discount:                    "90%+ cheaper"
                                                       (pricing table is an
                                                        embedded image;
                                                        exact $/M figures
                                                        not transcribed —
                                                        compare the exact
                                                        Spark 1.2 figures in
                                                        blog-simonwillison-muse-code-spark-12.md
                                                        Concrete Artifacts)
MRCR 512k-1m (long-context):                          98.1%
                                                       (read off a
                                                        screenshotted
                                                        benchmark table by
                                                        Reddit commenters;
                                                        not independently
                                                        verified)
Open weights status:                                  "coming soon"
                                                       (same status Spark
                                                        1.2 had a month
                                                        earlier per the
                                                        2026-08-10 post)
```

### Cross-post narrative link (Meta "comeback" arc, as tracked by AINews)
```
2026-08-10  "[AINews] Muse Glimmer and Spark: Open Weights return Personal
             Superintelligence promise" — Muse Glimmer (30B, Apache 2.0)
             ships; Spark 1.2 weights promised "soon" (not yet delivered
             per this post); "MSL seems to be feeling a second wind."
             (latent.space/p/ainews-muse-glimmer-and-spark-open)

2026-09-03  This post — Muse Spark 1.3 launches; #3 AAII ranking; Spark 1.3
             weights again promised "coming soon"; headline invokes
             "confirming Meta Superintelligence as the newest Frontier Lab."
             (latent.space/p/ainews-muse-spark-13-matches-gpt)
```
*Source: both dates directly fetched and read for this note (2026-08-10 post
followed as a substantive linked page per MINER.md §1).*

### A same-named but unrelated model: Spark-X2.5 (XHToken)
```
Source: latent.space/p/ainews-muse-spark-13-matches-gpt, Reddit recap,
"2. New Model: Spark-X2.5-4B, Spark-X2.5-1.7B"

Publisher: XHToken (not Meta; no relation to Muse Spark)
Sizes: 1.7B and 4B
Claims: native 1M token context, ~20T pretraining tokens, 4B variant
  "matches a ~9B model" (independent testing pending)
Runtime: not yet upstreamed in llama.cpp (depends on pending PR #27868)
```
*Note: this appears in the same Reddit thread title ("Muse Spark and
Spark-X2.5 Open-Weight Models") purely by naming coincidence — Spark-X2.5 is
an unrelated third-party model family, not a Meta release. Flagged here so
the guide (or a future Miner) does not conflate the two if citing this
thread.*

## Cross-References

- **Extends**: `blog-simonwillison-gpt6-astra-launch.md` (Claim 4 and
  Extraction Notes): that note's Claim 4 supplied the corpus's first mention
  of Muse Spark 1.3 (index standing only, no score/pricing/capability
  detail) and explicitly flagged "Muse Spark 1.3 is a candidate for its own
  Prospector scan; this note should not be cited as a source on that
  model." This note is that dedicated scan — it supplies Claim 1's #3 AAII
  rank, Claim 3's pricing-tier continuation, Claim 5's MRCR figure, and
  Claim 6's positioning statement, none of which the Astra-launch note
  covers.
- **Extends**: `blog-simonwillison-muse-code-spark-12.md` (Claim 8: the
  Spark 1.2 two-tier, data-sharing-conditioned pricing table; Claim 3: Spark
  1.2's long-horizon coding training; Claim 9: Spark 1.2's 1M context
  window). This note's Claim 3 (90%+ training-discount pricing) and Claim 6
  (agentic/coding positioning) show Meta continuing the same pricing
  mechanism and capability framing into 1.3, without any of the mechanism
  detail (co-training with Muse Code, rejection-sampled harness
  trajectories, named benchmarks) that note documents for 1.2 — this source
  restates positioning, it does not add architecture or training detail.
- **Extends**: `blog-simonwillison-muse-spark.md` (Claim 8: Muse Spark 1.0's
  April 2026 Artificial Analysis score of 52, top-4 at the time, "over an
  order of magnitude less compute" vendor efficiency claim). Claim 1 here
  (a #3 AAII ranking for 1.3, five months later) is a continuation of the
  same benchmark-tracking thread for the Spark lineage, though the index
  itself may differ or have been rescaled between April and September 2026
  — the guide should not directly compare "52" and "#3" as the same metric
  without checking whether Artificial Analysis's index methodology changed
  over that period.
- **Extends**: `blog-simonwillison-muse-glimmer.md` (Claim 5: Muse Glimmer
  was pretrained via logit distillation from Muse Spark's own outputs,
  making Glimmer a distilled sibling of the hosted Spark model, not a
  separate lineage). Claim 8's parameter-count speculation here (Spark
  could be trillion-parameter scale) is relevant context for that
  relationship: if accurate, Glimmer's 30B size represents a large
  distillation gap from its Spark "teacher," which is a data point (not
  confirmed in either note) worth flagging for anyone using Glimmer as a
  practical proxy for Spark's capabilities.
- **Corroborates**: `blog-latentspace-ainews-meta-harness-summer.md`
  (Extraction Notes and overall approach) — same publication, same
  AINews/swyx editorial process, same paywall structure (`only_paid`
  audience with a free preview, recovered here the same way: `curl` +
  Substack's embedded `window._preloads` JSON + `html2text`, per that
  note's precedent). Confirms this extraction methodology is now used
  consistently across multiple AINews source notes in the corpus.
- **Contradicts**: Evaluated one candidate tension, not filed. Claim 1's
  "#3 model in the world" (Artificial Analysis Intelligence Index) sits
  alongside a materially different, more middling result on a *different*
  Artificial Analysis benchmark reported elsewhere in the corpus:
  `blog-cognition-devin-local-fusion.md`, Concrete Artifacts → "Headline
  Artificial Analysis Coding Agent Index v1.5 comparison" section, lists
  "Muse Code, Muse Spark 1.3 (max): score 54.0" — tied with GLM-5.3, above
  Kimi K3 (52.0) and Grok 4.6 (47.0), but below Claude Code/Opus 5 (60.0)
  and well below Claude Code/Fable 5.1 (62.2) or either Devin Fusion
  pairing. This does not meet the `agents/MINER.md` §4a filing bar: the two
  sources measure different, named benchmarks (Artificial Analysis's
  general-purpose Intelligence Index vs. its separate Coding Agent Index),
  so a top-3 general-intelligence ranking and a mid-pack coding-agent score
  for the same model in the same month are not logically inconsistent —
  different axes, not opposing measurements of the same thing. Flagged here
  prominently per MINER.md §4a's "conditioning variable" guidance and
  because a reader skimming only the headline of this post could easily
  over-generalize "#3 in the world" to imply top-tier coding-agent
  performance, which the corpus's other data point does not support.
- **Novel**: The specific #3 AAII ranking claim for Muse Spark 1.3 (Claim
  1); the continuation of the exact ~90%+ training-discount pricing pattern
  into a second release (Claim 3); the screenshot-sourced MRCR 98.1%
  long-context figure (Claim 5); the direct textual absence of "Meta
  Superintelligence" from this post's own body despite the headline (Claim
  9); the two-post "comeback" narrative arc spanning 2026-08-10 to
  2026-09-03 (Claim 10, Concrete Artifacts); and the trillion-parameter
  scale speculation and its local-deployability implications for the
  promised-but-undelivered open weights (Claim 8) are all new to the
  corpus.

## Guide Impact

- **Chapter 01 (Frontier Labs Overview)**: If the guide names Meta
  Superintelligence Labs (MSL) as a frontier lab, cite this post's Claim 1
  (#3 AAII ranking) as the concrete benchmark-standing evidence, but do
  **not** cite this post as the origin of "Meta Superintelligence" framing
  (Claim 9) — that terminology predates this post by at least a month per
  the linked 2026-08-10 AINews coverage.
- **Chapter 02 / Chapter 05 (Model Capability Comparisons, Models & Costs)**:
  When citing Muse Spark 1.3's benchmark standing, explicitly distinguish
  the Intelligence Index ranking (#3 in the world, Claim 1, no score given)
  from the separate Coding Agent Index score (54.0, mid-pack, sourced from
  `blog-cognition-devin-local-fusion.md`) — see Cross-References →
  Contradicts. A single "Muse Spark 1.3 is a top-3 frontier model" framing
  without that distinction would overstate its coding-agent competitiveness
  specifically.
- **Chapter 05 (Models & Costs)**: Update the pricing-pattern discussion
  sourced from `blog-simonwillison-muse-code-spark-12.md` Claim 8 to note
  that Meta's data-sharing-conditioned "contributor" discount (there ~92%
  for Spark 1.2, here "90%+" for Spark 1.3, Claim 3) is now a two-release
  pattern specific to Meta's Spark line, not a one-off pricing experiment —
  worth flagging to practitioners evaluating whether to opt in to the
  training-data-sharing tier for future Spark releases too.
- **Chapter 01 or Chapter 05 (vendor commitments / release tracking)**: Add
  Claim 2 (open weights "coming soon" for both Spark 1.2 in August and
  Spark 1.3 in September, neither yet delivered per corpus sources) as a
  concrete, dated instance of a vendor open-weights promise not yet
  fulfilled across two releases — relevant if the guide ever advises
  practitioners on how much weight to put on vendor open-weights
  announcements before weights actually ship.

## Extraction Notes

- **Paywall encountered, worked around** (same method as
  `blog-latentspace-ainews-meta-harness-summer.md`): this post's `audience`
  field is `only_paid` with `should_send_free_preview: true`. The page's
  embedded Substack JSON payload (`window._preloads` → `post.body_html`)
  was recovered via `curl` with a browser user-agent, decoded from its
  JS-escaped JSON-string encoding, and converted to plain text with
  `html2text` (Python library). All quotes above were copied
  character-for-character from that recovered free-preview text (formatting
  markup such as bold/link-bracket syntax stripped, per MINER.md §2a's
  allowance for stripping "footnote markers, formatting").
- **The paywall cuts off partway through the Reddit recap**: the post's own
  `wordcount` field states 4,776 words; the recovered free-preview text is
  ~2,601 words (~54%). The recovered text ends after the "2. Qwen3.8
  Benchmarks and GGUF Speedups" Reddit subsection, mid-way through the "AI
  Reddit Recap" section — whatever Reddit content follows (additional
  subreddits, further discussion) was not read and is not represented in
  this note. Given the free portion's own structure (numbered items under
  "/r/LocalLlama + /r/localLLM Recap"), it's plausible other subreddit
  recaps exist behind the paywall, but this cannot be confirmed.
- **One additional linked page followed**: `latent.space/p/ainews-muse-glimmer-and-spark-open`
  (2026-08-10 AINews post, linked from this post's opening sentence as
  "Zuck's big comeback letter"), fetched and read via the same
  curl+preloads+html2text method, specifically to check whether "Meta
  Superintelligence" framing was novel to this post (Claim 9) and to verify
  the open-weights promise pattern (Claim 2). This is the only linked page
  followed beyond the target post itself — other links in the post (to
  individual tweets, Reddit threads, and GitHub PRs) were not fetched, as
  X/Twitter and Reddit permalinks are not fetchable as substantive
  standalone pages and the Reddit recap text already includes the digest's
  own summary of each thread's content.
- **Screenshot-sourced figures could not be independently verified**: this
  post's two most specific numeric claims (the #3 AAII ranking underlying
  score, and the MRCR 98.1% figure) both originate from images (an embedded
  benchmark-table screenshot and a Zuckerberg/X post screenshot) that were
  not visually inspected as part of this extraction — only the digest's and
  Reddit commenters' own textual descriptions of those images were read.
  This is reflected in each claim's confidence rating and explicitly
  flagged rather than treated as verified.
- **Confidence rated `anecdotal` overall**: despite several claims rated
  `emerging` (the pricing continuation, the vendor positioning statement,
  the repeated open-weights promise — all specific and checkable against
  the prior month's post), the source as a whole is a secondary
  Twitter/Reddit aggregation relaying vendor claims exclusively through
  screenshots and paraphrase, with no benchmark number in this post
  independently verified by AINews itself or by this extraction. Matches
  the overall confidence rating given to the other AINews-sourced note in
  this corpus, `blog-latentspace-ainews-meta-harness-summer.md`.
- **No contradiction issue filed**: the one candidate tension identified
  (Claim 1's Intelligence Index standing vs. the Coding Agent Index score in
  `blog-cognition-devin-local-fusion.md`) was evaluated against
  `agents/MINER.md` §4a and judged to be a conditioning-variable case
  (different named benchmarks measuring different things), not a genuine
  factual disagreement — see Cross-References → Contradicts for the full
  reasoning.
- **Cross-references verified before writing**: re-read
  `blog-simonwillison-gpt6-astra-launch.md` in full and confirmed Claim 4 by
  number and content, including its Extraction Notes' explicit flag that
  Muse Spark 1.3 needed its own Prospector scan; re-read
  `blog-simonwillison-muse-code-spark-12.md` in full and confirmed Claims 3,
  8, and 9 by number and content; re-read `blog-simonwillison-muse-spark.md`
  in full and confirmed Claim 8 by number and content; re-read
  `blog-simonwillison-muse-glimmer.md` and confirmed Claim 5 by number and
  content; re-read `blog-simonwillison-astra-pelican-comparison-grid.md`
  and confirmed Claim 4 by number and content; re-read
  `blog-cognition-devin-local-fusion.md` and confirmed the cited figure
  (54.0) by section name (Concrete Artifacts → "Headline Artificial
  Analysis Coding Agent Index v1.5 comparison"), not a fabricated claim
  number, per MINER.md §4b; re-read
  `blog-latentspace-ainews-meta-harness-summer.md` in full to confirm the
  shared extraction methodology and paywall-workaround precedent cited
  above. No claim number was guessed or approximated.
- **Three duplicate Prospector triage comments** were posted on this issue
  (consistent chapter guidance — Ch01/Ch02/Ch04/Ch05 variously named across
  the three — with each independently flagging the training-pricing and
  benchmark-parity questions as worth extraction). All three were read and
  reconciled into the single extraction above; none contained claims about
  the source's content that could not be verified against the fetched text.
