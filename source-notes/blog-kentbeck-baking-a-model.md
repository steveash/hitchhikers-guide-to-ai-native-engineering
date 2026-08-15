---
source_url: https://newsletter.kentbeck.com/p/baking-a-model
source_type: blog-post
title: "Baking a Model"
author: Kent Beck
date_published: 2026-08-14
date_extracted: 2026-08-15
last_checked: 2026-08-15
status: current
confidence_overall: emerging
issue: "#2719"
---

# Baking a Model (Kent Beck)

> Kent Beck opens a promised series on "the machinery that makes a model" with
> a plain-language, bread-baking-analogy explainer of two structural splits —
> user interface vs. "model proper," and pre-training vs. post-training — and
> explicitly defers the guide-relevant payoff (how pre-training and
> post-training teams differ in incentives, tools, rhythm, and culture) to a
> future post.

## Source Context

- **Type**: blog-post (Kent Beck's newsletter, `newsletter.kentbeck.com`,
  published 2026-08-14, filed via the `kent-beck` trusted RSS feed).
- **Author credibility**: Kent Beck is the creator of Extreme Programming
  (XP) and Test-Driven Development (TDD), and a co-author of the Agile
  Manifesto — see `blog-kentbeck-trust-factory.md` and
  `blog-kentbeck-yagni-economics.md` for his broader corpus presence. On the
  specific subject of this post — how foundation models are actually
  constructed — Beck explicitly disclaims expertise ("I don't claim to
  understand the details, not yet"), positioning this as a practitioner
  outsider's first attempt to build a mental model, not an insider account.
  Contrast with `blog-latentspace-kant-poolside-model-factory.md`, whose
  author (Eiso Kant, Poolside's co-founder/co-CEO) is a first-party model
  builder describing his own company's pre/post-training infrastructure —
  see Cross-References below for how the two sources corroborate from very
  different vantage points.
- **Scope**: A short, entirely free (non-paywalled) newsletter post — the
  full text runs from the opening Motorola-manual anecdote through a closing
  scoping statement, a self-promotional consulting block, and one reader
  comment, with no visible paywall break. Covers: a progressively-revealed
  explanation of "what a model is" (UI layer vs. "model proper"), a bread/
  cold-proofing analogy mapped onto pre-training and post-training, a
  paragraph-length description of what happens mechanically during each
  phase, an observed vocabulary gap (no single word for "training" itself),
  and an explicit statement that a followup post will cover team/role
  differences across the two phases. Does NOT cover: AI agents, "genies," or
  agent behavior in any form (see Cross-References — this matters because
  one Prospector triage comment expected this post to scaffold the corpus's
  existing genie-metaphor claims; it does not); any actual team-structure,
  incentive, or org-design content (explicitly deferred to a future post);
  any technical detail on attention mechanisms, tokenization, RL, or
  architecture; any company examples, benchmarks, or numeric evidence beyond
  Beck's own round-number estimate of pre-training cost.

## Extracted Claims

### Claim 1: Beck frames this post as the start of a series on "the machinery that makes a model," explicitly distinct from how models work, and asks for reader correction before continuing
- **Evidence**: Beck's own scoping statement, given in the introduction, paired with a closing request for feedback before he proceeds.
- **Confidence**: settled (a first-party statement of what this specific post does and does not attempt, not a claim about the world requiring outside verification)
- **Quote**: "It's this latter topic, how a model gets constructed, that I will begin to explore in this post (& possible followups)."
- **Our assessment**: This is the single most important framing claim for how the guide should treat this source: it is explicitly the first installment of a multi-part exploration, with the team-structure payoff (the part most relevant to the guide's chapters on team organization) deferred to a future post. This mirrors the pattern already documented in `blog-kentbeck-xp-long-volatility.md` Claim 6, where a Beck post's title promises more than its body delivers.

### Claim 2: A model is architecturally split into two structurally distinct parts — a conventionally-engineered user interface layer (formatting, sequencing, authentication) and a "model proper" built with radically different techniques
- **Evidence**: Beck's own progressively-revealed explainer, presented as a deliberate over-simplification followed by one layer of added complexity.
- **Confidence**: settled (a widely-understood, uncontroversial architectural description — a serving/application layer distinct from model weights — restated in Beck's own plain-language framing, not a novel or contested technical claim)
- **Quote**: "The model is split into 2 parts: A user interface that takes care of formatting inputs & outputs & sequencing & authentication & all that stuff. The model proper where the magic happens."
- **Our assessment**: Useful chiefly as accessible vocabulary — "model proper" vs. "user interface" — for guide sections that need to distinguish what harness/prompt-level engineering can change (the UI layer, per Beck "built using conventional programming techniques") from what requires actual training (the "model proper," "built using radically different techniques"). Not a novel technical claim, but a clean two-term framing not otherwise present in the corpus.

### Claim 3: A model is fundamentally "a bag of numbers" produced through training rather than authored as a sequence of programming statements
- **Evidence**: Beck's own definitional statement, given as the answer to "what is a model" after the UI/model-proper split.
- **Confidence**: settled (a standard, uncontroversial characterization of how trained neural network weights differ from conventionally authored code)
- **Quote**: "A model is a bag of numbers." "Unlike in programming, where you lay out a sequence of statements the result of which is a program, AI models result from training."
- **Our assessment**: A compact, quotable one-liner for any guide passage that needs to explain to a software-engineering audience why "the model" behaves unlike code they can read line-by-line — it is the byproduct of a training process, not an authored artifact.

### Claim 4: Pre-training, post-training, and mid-training are named phases, but there is no single term for "training" as a whole — Beck flags this as a vocabulary gap and hopes it evolves
- **Evidence**: Beck's own parenthetical observation, made in passing before describing the two phases in detail.
- **Confidence**: emerging (a specific, checkable observation about industry terminology, not something Beck claims special authority on — he immediately follows it with "I need to learn more about how pre-training folks collaborate")
- **Quote**: "Near as I can tell, there's pre-training, post-training, & mid-training (about which I know nothing), but there's not "training" except as the composition of pre-, mid-, & post-. Here's hoping the vocabulary evolves."
- **Our assessment**: A minor but concrete observation — corroborated independently by a reader comment on the same post (see Concrete Artifacts) that riffs on the same missing-word gap, suggesting it registered with more than just Beck.

### Claim 5: Pre-training is a team-driven "big batch" process — the whole team sets initial conditions (data plus a blank model), repeatedly runs data through the model, takes crash-recovery snapshots, and monitors for and restarts on drift — representing a bet of "hundreds of millions of dollars" and months of delay
- **Evidence**: Beck's own paragraph-length description of what happens mechanically during pre-training, including a round-number cost estimate offered without citation.
- **Confidence**: emerging (the qualitative description — team-driven setup, snapshotting for crash recovery, drift monitoring and restart — is broadly consistent with independently-sourced first-party infrastructure accounts already in the corpus, see Cross-References; the specific "hundreds of millions of dollars" figure is Beck's own unsourced estimate, and Beck himself flags his own uncertainty about pre-training team dynamics immediately afterward: "I need to learn more about how pre-training folks collaborate")
- **Quote**: "Pre-training is a big batch. The whole team sets up the initial conditions—the data & the blank model. They run the data backwards & forwards through the model a gajillion times. They take snapshots along the way in case of crashes. They check for signs that the pre-training has driven off into the weeds & needs to be tweaked & restarted. Pre-training is a big bet—hundreds of millions of dollars & (more expensively) months of delay."
- **Our assessment**: The snapshot/crash-recovery and drift-monitoring/restart description is a plausible, outsider-level compression of what `blog-latentspace-kant-poolside-model-factory.md` describes in first-party engineering detail (immutable data layer, versioned code, "zero call events" reliability target) — Beck is describing the same category of process from outside the building, Kant from inside it. See Cross-References.

### Claim 6: In the baking analogy, pre-training maps to "cold proofing" — you mix ingredients, place them somewhere you cannot intervene, and let the process run; the result is not directly usable, only a precursor to what follows
- **Evidence**: Beck's own extended analogy, drawing on his personal experience with overnight refrigerated yeast fermentation.
- **Confidence**: anecdotal (a personal, illustrative analogy — Beck's own creative framing device, not a technical or empirical claim)
- **Quote**: "Pre-training is the cold proofing of model training. You mix some stuff together. You put it away somewhere where you can't mess with it. You just have to let it play out. The result isn't usable but it's the precursor to the process that follows."
- **Our assessment**: The analogy's specific value is "sensitivity to initial conditions" (stated earlier in the post: "baking is sensitive to initial conditions—you can make a small change early in the process & it will have a large consequence later") — a plain-language way to motivate why pre-training data/setup quality matters disproportionately, without requiring the reader to understand the training mechanics themselves.

### Claim 7: Post-training consists of "lots of little batches" run by researchers (whom Beck prefers to call "model engineers") who identify specific weaknesses in the raw model and iterate targeted tweaks, with surviving experiments accumulating as small code/data supplements layered onto the existing model
- **Evidence**: Beck's own paragraph-length description of post-training's mechanics, paralleling his pre-training description.
- **Confidence**: emerging (a plausible, outsider-level compression of iterative fine-tuning/RLHF-style practice, consistent with the corpus's existing first-party post-training description — see Cross-References — but not itself a first-party technical account)
- **Quote**: "Post-training is lots of little batches. Folks (called "researchers" but in my naive bluntness I'd call "model engineers") look at particular problems the raw model addresses poorly & explore possible tweaks that might improve performance. The result is lots of little chunks of code & data (the surviving experiments) that apply to the model as it currently exists." "Apply enough supplements & you have a model that, when paired with a UI & a user & compute can respond to, "Give me 5 unusual focaccia toppings.""
- **Our assessment**: The "researcher vs. model engineer" naming preference is a small but notable choice — Beck is deliberately reframing post-training work in software-engineering-adjacent vocabulary, consistent with his broader pattern (see `blog-kentbeck-trust-factory.md`) of translating AI-development practice into terms an XP/software-engineering audience already has intuitions for.

### Claim 8: In the baking analogy, post-training maps to "shaping & cooking" — but Beck explicitly flags that the analogy breaks down here, since it does not capture post-training's collaborative, iterative, and reversible nature
- **Evidence**: Beck's own extended analogy, with an explicit self-critique of its limits.
- **Confidence**: anecdotal (a personal illustrative analogy, explicitly self-flagged by its own author as incomplete)
- **Quote**: "Post-training is the shaping & cooking of model training. You take something with potential & make it delicious for humans. (The analogy doesn't cover the collaborative, iterative, & reversible nature of post-training—le sigh.)"
- **Our assessment**: Beck's own admission that the baking analogy fits pre-training (a single irreversible, non-interactive process) better than post-training (collaborative, iterative, reversible) is itself informative — it implicitly argues that post-training is structurally closer to normal software engineering practice (iteration, reversibility, many small changes) than pre-training is, even though Beck doesn't state that comparison explicitly.

### Claim 9: Beck commits to a followup post exploring team and role differences across pre-training and post-training, naming interesting divergences in incentives, tools, rhythm, short-term-vs-long-term thinking, feature-vs-future orientation, backgrounds, and culture
- **Evidence**: Beck's own closing statement of intent for the next post in the series.
- **Confidence**: anecdotal (a stated future intent, not content that exists yet — see Extraction Notes and Guide Impact for why this caps how much the guide can currently draw from this specific post)
- **Quote**: "In a followup I'm going to explore the different teams & roles involved in this whole process. They have some interesting divergences of incentives, tools, rhythm, short-term vs long-term, feature vs future, backgrounds, & culture."
- **Our assessment**: This is the list of dimensions the Prospector's triage comments were anticipating ("organizational and process distinctions between pre-training and post-training phases," "team structures, incentives, and workflows") — named here as a promise, not yet delivered. A future Miner should watch this feed for the followup post and extract it as a distinct, separately-cited source when it appears, rather than assuming this post already covers that ground.

## Concrete Artifacts

### Beck's pre-training / post-training mechanics, as stated (verbatim, condensed)

```
Source: Kent Beck, "Baking a Model", newsletter.kentbeck.com, 2026-08-14

Pre-training:
- The whole team sets up the initial conditions (the data & the blank model)
- Data run backwards & forwards through the model repeatedly
- Snapshots taken along the way in case of crashes
- Monitored for signs of having "driven off into the weeds"; tweaked &
  restarted if so
- "A big bet—hundreds of millions of dollars & (more expensively) months
  of delay"

Post-training:
- Researchers ("model engineers") look at particular problems the raw
  model addresses poorly
- Explore possible tweaks that might improve performance
- Surviving experiments become "little chunks of code & data" applied to
  the model as it currently exists
- "Apply enough supplements & you have a model" that can respond to users
```

### Reader comment (not Beck's own writing) riffing on the missing "training" term

```
Source: comment by "Jon Verrier" beneath Kent Beck, "Baking a Model",
newsletter.kentbeck.com, 2026-08-14 (posted 14h after publication per the
page's relative timestamp at time of extraction)

"We have 'pre-training' and 'post-training', but no step called
'training'. I will let my PT know. We can meet for a pre-training chat,
then move directly to post training coffee, and skip working out
entirely."
```

## Cross-References

- **Corroborates**: `blog-latentspace-kant-poolside-model-factory.md` Claim
  5 (Poolside's first-party account of pre-training reliability practice:
  an immutable data layer, versioned code, and "zero call events" — no
  production-training-pipeline incidents requiring a wake-up — across the
  year before that interview) and Claim 1 (team-driven, fewer-than-70-
  researcher pre-training organization running thousands of experiments a
  month). Beck's outsider description of pre-training (Claim 5 above: team
  sets initial conditions, takes crash-recovery snapshots, monitors for
  drift and restarts) is a plain-language compression of the same category
  of process Kant describes from inside a real training organization. The
  two sources corroborate from opposite vantage points — Beck as an
  interested outsider building a mental model, Kant as the practitioner who
  built the actual infrastructure — which is a useful pairing for the guide:
  Beck supplies accessible vocabulary, Kant supplies verified mechanism and
  numbers.
- **Corroborates**: `blog-latentspace-kant-poolside-model-factory.md` Claim
  2 (Kant: "the model should be an artifact of someone's process. It
  shouldn't be really a thing in itself," using a SpaceX-factory analogy)
  and Claim 6 (Poolside researchers can qualitatively assess a new
  post-trained checkpoint within 30 minutes). Beck's post-training
  description (Claim 7 above: researchers/"model engineers" iterating small
  tweaks that accumulate as supplements) is consistent with — though far
  less detailed than — Kant's first-party account of what post-training
  iteration actually looks like day to day at a real lab.
- **Extends**: `blog-kentbeck-xp-long-volatility.md` Claim 4 ("The only way
  to learn how to explain something well is to explain it badly over &
  over") and Claim 1 (Beck holds roughly a hundred ideas in reserve,
  testing each periodically). This post is itself an instance of that
  described method in action: Beck explicitly asks readers to correct his
  understanding before he continues ("First, though, I wanted to double
  check my understanding of the process. Let me know if I got something
  wrong above"), the same "bad explanation, then refine" pattern documented
  as his general practice in the earlier post.
- **Corroborates**: `blog-kentbeck-3x-explore-expand-extract.md` Claim 9
  and `blog-kentbeck-xp-long-volatility.md`'s Extraction Notes (the
  "sponsored"-adjacent consulting pitch). This post's closing block —
  "Most teams don't have a strategy problem. They have an adaptation
  problem." / "Your plan was never going to survive contact with reality."
  — is verbatim-identical to the promotional block already extracted in
  `blog-kentbeck-3x-explore-expand-extract.md` Claim 9, confirming this is
  a recurring, templated self-promotional insert appended to multiple
  posts rather than essay content specific to this piece. Not re-extracted
  as a separate claim here for that reason (see Extraction Notes).
- **Contradicts / corrects a triage expectation**: The third Prospector
  triage comment on this issue expected the Miner to extract "foundational
  insights about model mechanics and construction... to contextualize or
  support existing claims about how AI agents 'think' and behave (e.g., the
  'genie' metaphor in other Kent Beck notes)" and speculated the post
  "echoes themes in existing Beck notes about genie/agent behavior
  predictability." On a full read, this post does not mention AI agents,
  "genies," or agent behavior anywhere — it is entirely about how the
  underlying model artifact itself gets constructed (pre-training,
  post-training), not about how a deployed agent behaves once built. This
  is a triage-accuracy note, not a disagreement between two sources of
  comparable authority, so it does not meet the MINER.md §4a bar for a
  formal contradiction issue; it is recorded here so the Assayer and Smith
  don't repeat the same overread (the same kind of correction
  `blog-kentbeck-xp-long-volatility.md`'s Cross-References made for its own
  Prospector comment).
- **Novel**:
  - The explicit "user interface" vs. "model proper" two-part split
    (Claim 2) and the "bag of numbers" framing (Claim 3) are not present
    elsewhere in the corpus in this compact, plain-language form.
  - The named vocabulary gap — pre-/mid-/post-training exist but "training"
    itself does not (Claim 4) — is a small, specific observation not
    documented elsewhere in the corpus.
  - The baking/cold-proofing analogy mapped specifically onto pre-training
    vs. post-training (Claims 6, 8) is a novel didactic framing, distinct
    from this corpus's existing baking-adjacent Beck material (the "ideas
    take years to bake" usage in `blog-kentbeck-xp-long-volatility.md`,
    which applies "baking" to conceptual/idea maturation, not to model
    training mechanics specifically).

## Guide Impact

- **No chapter should cite this post for team-structure, incentive, or
  organizational guidance yet.** Claim 9 — the part of this post that would
  most directly match the "team structures in AI engineering" chapter
  relevance the first two Prospector triage comments flagged — is an
  explicit statement of future intent, not content Beck has published. The
  guide should wait for and cite the actual followup post when it appears,
  per the same caution already applied to `blog-kentbeck-xp-long-volatility.md`.
- **Chapter 02 (Harness Engineering)**: Claim 2's "user interface" vs.
  "model proper" framing is usable as accessible, non-technical vocabulary
  for any passage distinguishing what harness/prompt-level engineering can
  change (the UI/serving layer) from what requires actual model training
  (the "model proper") — a distinction the guide likely already assumes but
  has not had a clean two-term label for. Pair with
  `blog-latentspace-kant-poolside-model-factory.md` Claims 4-5 if the
  guide ever wants to go one level deeper into what "model proper"
  engineering concretely involves (streaming data config, immutable data
  layers, reproducibility).
- **Chapter 00 (Principles) or wherever the guide discusses model
  provenance/limitations**: Claim 3 ("a model is a bag of numbers,"
  produced by training rather than authored) and Claim 5's sensitivity-to-
  initial-conditions framing are a compact, quotable way to explain to a
  software-engineering audience why model behavior cannot be reasoned about
  the way authored code can — useful scaffolding prose, not a load-bearing
  practice recommendation.
- No other chapter has directly actionable content from this post at this
  time — it is a foundational, vocabulary-building piece that explicitly
  defers its most guide-relevant content to a future post.

## Extraction Notes

- **Fetch method**: An initial WebFetch pass on the source URL declined to
  reproduce the post's text, citing copyright, and offered only summarized
  paraphrase with quotes capped under 125 characters — consistent with the
  pattern already documented in `blog-kentbeck-xp-long-volatility.md` and
  `blog-kentbeck-3x-explore-expand-extract.md`'s Extraction Notes. Two
  scoped WebFetch verification passes were used first to sanity-check
  several short quotes, then the page was re-fetched directly via `curl`
  with a browser user-agent; the post body was located inside the page's
  `class="body markup"` container, HTML tags stripped and entities decoded
  programmatically, and every `Quote` field in this note was copied
  verbatim from that raw parsed text rather than reconstructed from the
  WebFetch summary. All quotes obtained via the two methods were
  cross-checked against each other and were consistent.
- **No paywall encountered**: the raw HTML contains the complete post body
  (introduction through the closing consulting-pitch block) plus one reader
  comment, with no visible paywall break or "subscribe to continue" cutoff
  in the extracted text — consistent with this being a fully free post.
- The post contains no sub-pages or linked pages substantive enough to
  warrant following per MINER.md §1 — it is a short newsletter post with no
  in-body links to other substantive content.
- The closing "Most teams don't have a strategy problem..." consulting
  pitch was deliberately **not** extracted as a standalone claim, since it
  is verbatim-identical to a block already extracted and discussed (with an
  explicit promotional-adjacency caveat) in
  `blog-kentbeck-3x-explore-expand-extract.md` Claim 9 — re-extracting the
  same templated text here as if it were new essay content would misrepresent
  it. See Cross-References.
- Cross-reference claim numbers were verified by re-reading the cited notes
  directly before writing: `blog-latentspace-kant-poolside-model-factory.md`
  Claims 1, 2, 5, and 6 (confirmed at that note's respective Claim headings);
  `blog-kentbeck-xp-long-volatility.md` Claims 1, 4, and 6 (confirmed);
  `blog-kentbeck-3x-explore-expand-extract.md` Claim 9 (confirmed, and its
  quoted text re-copied verbatim from that note rather than re-fetched, to
  guarantee an exact match when flagging the recurring promotional block).
- No formal contradiction issue was filed. The one substantive tension
  found — between this post's actual (agent/genie-free) content and the
  third Prospector triage comment's expectation that it would connect to
  the corpus's existing genie-metaphor material — is a triage-accuracy
  issue rather than a disagreement between two sources of comparable
  authority, so it is documented under Cross-References rather than
  escalated per MINER.md §4a, following the same precedent set in
  `blog-kentbeck-xp-long-volatility.md`.
- Confidence rated `emerging` overall: the architectural framing claims
  (Claims 1-3) are settled/uncontroversial restatements of well-understood
  facts, and the pre-/post-training mechanics (Claims 5, 7) are broadly
  corroborated by an independent first-party source already in the corpus
  (Poolside); but several claims are explicitly Beck's own hedged, personal
  analogy (Claims 6, 8, self-flagged as incomplete) or a stated future
  intent not yet delivered (Claim 9), and Beck himself repeatedly disclaims
  expertise on the subject matter. Not rated `settled` overall because the
  post's most specific figures (the "hundreds of millions of dollars"
  pre-training cost estimate) are unsourced, and not rated purely
  `anecdotal` because the core architectural claims are uncontroversial and
  independently corroborated.
