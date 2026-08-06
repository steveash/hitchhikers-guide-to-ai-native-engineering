---
source_url: https://www.latent.space/p/xaira
source_type: blog-post
title: "🔬Causal Models Need Causal Data - Xaira's X-Cell model for Drug Discovery (Bo Wang & Ci Chu, Chief Discovery Officer & Chief AI Scientist)"
author: Latent Space (RJ Honicky), interviewing Bo Wang (Chief AI Scientist) and Ci Chu (Chief Discovery Officer), Xaira Therapeutics
date_published: 2026-07-21
date_extracted: 2026-08-06
last_checked: 2026-08-06
status: current
confidence_overall: anecdotal
issue: "#2526"
---

# Causal Models Need Causal Data - Xaira's X-Cell model for Drug Discovery

> A Latent Space podcast episode page (written intro + bulleted show notes;
> no full spoken transcript is published) arguing that observational
> gene-expression data cannot support causal predictions about drug/gene-edit
> effects, and describing Xaira Therapeutics' response: a CRISPR-based
> perturbation dataset (X-Atlas) and model (X-Cell) built to generate the
> missing causal signal.

## Source Context

- **Type**: blog-post (podcast episode page, Latent Space Substack,
  published 2026-07-21). Per the page's own embedded metadata, the written
  text totals 667 words: a short framing essay ("Bet on information"),
  a labeled section on the CELLxGENE dataset and Virtual Cell models
  ("Reverse engineering the human cell"), a section stating the core
  correlation-vs-causation problem ("RNA expression ≠ Virtual Cell"), a
  one-line naming reveal ("X-Atlas → X-Cell"), and a bulleted "In this
  episode, we discuss" list of six topics. A "Transcript" UI control is
  present on the page, but no rendered transcript text of the spoken
  interview appears in the page's HTML or embedded JSON — see Extraction
  Notes.
- **Author credibility**: Latent Space is a widely-read AI engineering
  podcast/newsletter (per its own byline, "over 10 million readers and
  listeners" in 2025) that has hosted named founders and researchers from
  OpenAI, Anthropic, Databricks, and others; this episode was sourced from
  the Prospector's `latent-space` trusted feed. The interview subjects, Bo
  Wang (Chief AI Scientist) and Ci Chu (Chief Discovery Officer) of Xaira
  Therapeutics, are named company officers describing their own company's
  model and data strategy — treat their claims as first-party positioning,
  not independently audited research. The written text itself is the
  host's (RJ Honicky's) framing and summary, not a direct transcription of
  either guest's spoken words.
- **Scope**: Covers Xaira's stated rationale for building a
  perturbation-based causal dataset (X-Atlas) and model (X-Cell): a
  data-information ceiling diagnosed via test-loss/training-loss
  divergence, the CELLxGENE/Virtual Cell modeling landscape Xaira's prior
  model (scGPT) came from, and the correlation-vs-causation limitation of
  observational RNA-expression data. Does NOT cover, in accessible text:
  the actual diffusion-vs-autoregression architectural decision, the
  CRISPR experimental protocol, benchmark numbers against the "linear
  baseline," or the "kitchen-sink of priors" discussion — these are named
  only as episode-topic bullets with zero elaboration in the written page;
  the substantive discussion of each is audio/video-only.

## Extracted Claims

### Claim 1: A test-loss plateau that persists while training loss keeps falling as parameters scale indicates the model is capped by the information content of its training data, not by model capacity or compute

- **Evidence**: Stated as the article's opening framing claim, illustrated
  by a referenced (not textually reproduced) chart showing Xaira's earlier
  3.1B-parameter model falling off its scaling trend.
- **Confidence**: emerging (a plausible and commonly invoked diagnostic in
  ML scaling-law discussions, but presented here without a citation to
  published methodology, and applied to a single anecdotal internal case)
- **Quote**: "If test loss flatlines after 1.5B parameters while training
  loss continues to drop as you scale, that tells you that your model is
  limited by the amount of information in your data."
- **Our assessment**: A reasonable and fairly standard scaling-law
  heuristic (a train/test loss gap that widens with scale usually points to
  a data rather than capacity bottleneck), but it's asserted here as a
  general rule rather than demonstrated with the underlying loss curves, so
  we treat the general principle as plausible and the specific
  attribution to Xaira's own model as a self-reported anecdote.

### Claim 2: Xaira's earlier ~3.1B-parameter model, trained on a single smaller dataset, hit exactly this data-information wall — neither more parameters nor more compute could push performance further

- **Evidence**: Stated directly in the same framing section, tied to
  gene-expression prediction specifically.
- **Confidence**: anecdotal (single self-reported case, no published loss
  curves or dataset size given)
- **Quote**: "Training on a single, smallish data set exposed an
  information gap: the 3.1B model falls off the scaling trend. Neither
  parameters nor compute will improve performance past this wall. For
  predicting changes to gene expression, you need more information rich
  data."
- **Our assessment**: This is the article's concrete evidence for Claim 1
  — a specific model size (3.1B) and a specific failure mode (falling off
  the scaling trend) — but it's a single, unaudited data point volunteered
  by the company, not a benchmarked result.

### Claim 3: Generating roughly 30x more information-rich data restored healthy scaling behavior, letting the team scale performance with parameters and compute again

- **Evidence**: Stated as the direct resolution to Claims 1-2, referencing
  a chart caption describing the effect of the new dataset.
- **Confidence**: anecdotal (self-reported multiplier with no disclosed
  measurement methodology for "information," and no published benchmark)
- **Quote**: "Now we can scale with parameters and training compute!"
- **Our assessment**: The "~30x the information" figure (from the
  preceding chart caption) is presented without a defined unit — it's
  unclear whether this means 30x more perturbation experiments, 30x more
  matrix entries, or something else. Worth citing as a company claim about
  the shape of the fix (more of a specific *kind* of data, not more
  parameters/compute), not as a validated scaling coefficient.

### Claim 4: The author estimates data-collection infrastructure cost "a few tens of millions" while compute, headcount, and research cost "a few million" — a budget shape closer to an RL rollout than a data-rich pretraining run

- **Evidence**: Explicitly labeled by the author as a guess, not a
  disclosed figure from Xaira.
- **Confidence**: anecdotal (author's own speculation, not a company
  disclosure)
- **Quote**: "We don't know how much this effort costed, but we can guess
  that data collection experiments and infrastructure was a few tens of
  millions, and compute + headcount + research was a few million. The
  budget looks like a RL rollout budget, rather than a data rich
  pre-training one."
- **Our assessment**: Flagged explicitly as an outside guess by the
  article's own author, not a Xaira-disclosed number — should not be cited
  in the guide as a company figure. The "budget shape" framing (data
  generation as the dominant cost center, not compute) is the interesting
  part if it holds, but it is unverified speculation.

### Claim 5: Xaira promoted the two interview subjects to Chief Discovery Officer (Chu) and Chief AI Scientist (Wang) shortly after the episode was recorded, which the author reads as a signal of how strategically central this data bet is to the company

- **Evidence**: Stated in the framing section with a footnote clarifying
  timing.
- **Confidence**: anecdotal
- **Quote**: "Chu was recently promoted to Chief Discovery Officer and Bo
  to Chief AI Scientist, underscoring just how strategic Xaira considers
  this bet." (footnote: "These promotions happened after we recorded the
  episode")
- **Our assessment**: A title change is a weak proxy for strategic
  importance on its own, but it's a verifiable, checkable fact (unlike most
  of the other claims in this piece) — an interested reader could confirm
  the promotions independently of the podcast.

### Claim 6: CELLxGENE, a 168M-cell gene-expression database built by the Chan Zuckerberg Institute, played the same field-unlocking role for "Virtual Cell" models that the Protein Data Bank played for structural biology models

- **Evidence**: Description of a named, independently checkable public
  dataset and an analogy to a well-established precedent (PDB unlocking
  structural biology models).
- **Confidence**: settled (CELLxGENE is a real, publicly documented
  dataset; its scale and structure are independently verifiable outside
  this source)
- **Quote**: "That is CELLxGENE, a database of 168M cells built by Chan
  Zuckerberg Institute that maps each cell to a count of how many times
  20K-30K genes were detected in that cell, plus detailed metadata about
  every cell. A ~4 trillion-entry matrix."
- **Our assessment**: This is the most independently verifiable factual
  claim in the piece and useful background for understanding the size of
  the observational-data ecosystem that Claim 8 argues is fundamentally
  insufficient for causal prediction.

### Claim 7: Bo Wang's own prior model, scGPT — built on CELLxGENE — became the architectural starting point for Xaira's new X-Cell model

- **Evidence**: Stated directly, naming a specific prior model and its
  creator.
- **Confidence**: anecdotal (self-reported lineage; scGPT itself is a real,
  published model, but its role as "the starting point" for X-Cell is
  asserted, not detailed)
- **Quote**: "Bo Wang built one of the most influential, scGPT, that became
  the starting point for Xaira's new model."
- **Our assessment**: Useful provenance detail (X-Cell isn't built from
  scratch; it evolves from a named, publicly known predecessor), but the
  nature of the evolution (architecture reuse vs. just a research lineage)
  isn't specified in the text.

### Claim 8: Models trained purely on observational gene-expression data (like CELLxGENE) can describe correlations between cell types and states but cannot reliably predict the causal effect of changing a gene's expression, because gene-expression changes are highly correlated and it is largely impossible to disentangle cause from effect in observational data alone

- **Evidence**: Stated as the article's central thesis, directly supporting
  the piece's title ("Causal Models Need Causal Data").
- **Confidence**: settled (the observational-data-cannot-establish-causation
  limitation is a well-established principle in both causal inference and
  genomics, independent of this specific source)
- **Quote**: "Models trained on CELLxGENE describe the relationship between
  cell types and cell states, but they are not good at predicting what will
  happen if we make changes to RNA expression. Changes in gene expression
  are highly correlated, and its is difficult (impossible) to figure out
  what causes what in most cases." [sic — "its is" appears verbatim in the
  source]
- **Our assessment**: This is the source's sharpest and most guide-relevant
  claim: it's not a claim about data *volume* (Claims 1-3's scaling-wall
  framing) but about data *type* — no amount of additional observational
  data fixes a confound/correlation problem; only interventional
  (perturbation) data can. This generalizes past biology: any domain where
  training data is purely observational (logs, telemetry, past decisions)
  faces the same ceiling for causal questions ("if we change X, what
  happens to Y?").

### Claim 9: The proposed fix is single-gene perturbation experiments — "turning the dial down" on one gene at a time to observe first-order upstream/downstream effects — which, aggregated across genes, could train a model to predict the effect of a drug or gene edit, or to find the least invasive way to shift a given gene's expression

- **Evidence**: Stated as the methodological bridge from Claim 8's problem
  statement to Xaira's actual approach; a footnote explicitly caveats that
  this covers only first-order effects.
- **Confidence**: emerging (the underlying logic — single-variable
  intervention to establish causal direction — is classic
  causal-inference methodology; applying it exhaustively across ~20-30K
  genes as a training-data-generation strategy is the source's specific,
  less-established proposal)
- **Quote**: "If you could "turn the dial down" on one gene at a time,
  however, then you would be able to observe what is upstream and
  downstream of a given gene. You could tell if A → B & C or B → A & C or
  B → A, C → B → …"
- **Our assessment**: The footnote's own caveat is important and easy to
  miss: "There can be cycles in the chain reaction, of course, and there
  can be second, third, etc. order effects... but the first order effects
  are a great place to start." The source is explicit that this is a
  simplifying first approximation, not a claim that single-gene knockdowns
  fully solve causal attribution in a system with feedback loops and
  higher-order interactions.

### Claim 10: This is exactly what Xaira built: a perturbation dataset (X-Atlas) and a model trained on it (X-Cell), generated via CRISPR-based experiments that the show notes describe as running "millions of tests in parallel"

- **Evidence**: Direct naming statement, plus a one-line show-notes bullet
  describing experimental scale.
- **Confidence**: anecdotal (company's own naming and scale claim; no
  detail on the CRISPR protocol, cell types used, or how "millions of
  tests" was measured)
- **Quote**: "This is exactly what Chu and Bo's teams have done. The data
  set is called X-Atlas and the model is called X-Cell."
- **Our assessment**: This is the concrete artifact the rest of the piece
  builds toward, but the show notes bullet about the CRISPR experiments
  ("The CRISPR-based experiments that run millions of tests in parallel,
  and generate the raw data for X-Atlas and X-cell") is a bare topic label
  with no elaboration in the written text — the actual protocol,
  throughput, and cost are discussed only in the audio/video episode,
  which was not accessible for this extraction (see Extraction Notes).

### Claim 11: The episode discusses why the team abandoned autoregressive modeling in favor of diffusion for X-Cell, but the written page gives no supporting detail

- **Evidence**: A single bulleted topic label in the "we discuss" list.
- **Confidence**: anecdotal (bare teaser, zero elaboration in accessible
  text)
- **Quote**: "Why the team abandoned autoregression for diffusion"
- **Our assessment**: This is exactly the kind of architecture-choice
  claim (diffusion vs. autoregression for a non-language, biological
  sequence/expression domain) that would be genuinely useful to the guide
  if the reasoning were available — but no rationale, ablation, or
  benchmark is given in the text. Flagging as a gap: worth re-mining if a
  transcript or a written follow-up (e.g. a paper) becomes available.

### Claim 12: X-Cell reportedly beats a "linear baseline" that had previously outperformed more complex prior models on this task

- **Evidence**: A single bulleted topic label; no benchmark numbers or
  task definition given.
- **Confidence**: anecdotal (bare teaser)
- **Quote**: "Beating the linear baseline that has outperformed previous
  models"
- **Our assessment**: Read alongside Claim 8, a simple linear model
  outperforming more complex prior models is a plausible symptom of the
  same underlying problem — if the training data is observational and
  confounded, more complex models may just be better at fitting the
  confound, not at causal prediction. This connection is our inference,
  not something the source itself draws; the source gives no detail to
  confirm or refute it.

## Concrete Artifacts

### Full "In this episode, we discuss" list (verbatim, 6 bullets)

```
Why the team abandoned autoregression for diffusion

The CRISPR-based experiments that run millions of tests in parallel, and
generate the raw data for X-Atlas and X-cell

Generalization to real lab experiments in real human cells

Beating the linear baseline that has outperformed previous models

Justifying a kitchen-sink of priors, and how that stacks up vs. data and
architecture

Bo also shared with us some of the (major) advantages he has as an
academic vs. industry leader, and how his labs keep up with the breakneck
pace of AI innovation.

Source: latent.space, "Causal Models Need Causal Data - Xaira's X-Cell
model for Drug Discovery," July 21, 2026
```

### Framing essay (verbatim, "Bet on information" section)

```
If test loss flatlines after 1.5B parameters while training loss continues
to drop as you scale, that tells you that your model is limited by the
amount of information in your data.

Training on a single, smallish data set exposed an information gap: the
3.1B model falls off the scaling trend. Neither parameters nor compute
will improve performance past this wall. For predicting changes to gene
expression, you need more information rich data.

This is what Chu and Bo's teams have done, and here is what ~30x the
information buys you:

Now we can scale with parameters and training compute! We don't know how
much this effort costed, but we can guess that data collection experiments
and infrastructure was a few tens of millions, and compute + headcount +
research was a few million. The budget looks like a RL rollout budget,
rather than a data rich pre-training one.

Source: latent.space, "Causal Models Need Causal Data - Xaira's X-Cell
model for Drug Discovery," July 21, 2026
```

## Cross-References

- **Corroborates**: `blog-latentspace-lila-sciences-lab-data-center.md`
  (Claim 4: physically/experimentally verified reasoning traces are a data
  *category* that internet-scale corpora structurally lack, not just a
  volume gap) — this source's Claim 8 (observational data cannot support
  causal prediction) and Claim 9/10 (perturbation experiments as the fix)
  make the same underlying argument in a different domain: some modeling
  problems require deliberately generating a specific *kind* of real-world
  data (there: physically verified outcomes; here: causal/interventional
  perturbations), and no amount of scraping or scaling the existing data
  supply closes that gap.
- **Extends**: Chapter 04's existing "training data gap" discussion
  (`guide/04-context-engineering.md`, "Pre-Session Corpus Loading for
  Low-Coverage Domains" section, ~lines 536-559, citing
  `failure-htdt-godogen-game-generation.md`) — that section frames the
  training-data gap as a *coverage* problem (a language/framework is
  under-represented in training corpora, so provide a reference corpus).
  This source describes a structurally different kind of data gap: the
  data isn't thin, it's abundant (CELLxGENE's ~4-trillion-entry matrix) but
  of the *wrong type* (observational, not interventional) for the task
  (causal prediction). Recommend distinguishing these as two distinct
  training-data-gap patterns if Ch04 is expanded: coverage gaps (fixed by
  more/better reference data of the same kind) vs. causal/type gaps (fixed
  only by generating a different kind of data via intervention/experiment,
  no matter how much observational data already exists).
- **Novel**: No existing source note in this corpus documents: (1) a
  test-loss-vs-training-loss divergence as a diagnostic for a
  data-information ceiling; (2) the correlation-vs-causation limitation of
  observational data as a distinct, named failure mode from generic
  "training data scarcity"; (3) single-variable perturbation experiments
  (CRISPR gene knockdowns) as a deliberate strategy for generating causal
  training data; (4) the CELLxGENE / Virtual Cell / scGPT modeling
  ecosystem. This note is the first in the corpus to touch computational
  biology / drug discovery as an application domain.

## Guide Impact

- **Chapter 04 (Context Engineering) — a distinct "data-type gap" alongside
  the existing "data-coverage gap"**: Ch04 currently frames training-data
  gaps as thin coverage for a given domain (see Extends above). This
  source's Claim 8 provides a clear, independently-grounded example of a
  different failure mode worth naming explicitly if Ch04's data-gap
  material is expanded: the data can be abundant and still be the wrong
  *type* for the task (observational vs. interventional/causal), and only
  generating new data via deliberate intervention closes that gap — more
  of the same observational data, or more parameters/compute applied to
  it, does not. This is a general point beyond biology: any team training
  or prompting a model to answer "if we change X, what happens to Y?"
  questions from purely historical/observational logs should recognize the
  same structural ceiling.

## Extraction Notes

- Fetched via `curl` with a browser user agent (`curl -s -L -A
  "Mozilla/5.0..." https://www.latent.space/p/xaira`), then cross-checked
  against the episode's own embedded `window._preloads` JSON blob
  (`post.body_html` and `post.wordcount` fields) rather than relying on an
  initial WebFetch pass, per MINER.md §2a's warning that WebFetch
  paraphrases rather than reproducing text verbatim. The embedded JSON's
  `wordcount` field (667) matches the length of the extracted text,
  confirming the full written page content was captured and nothing was
  paywall-truncated.
- The page's static HTML and embedded JSON contain a "Transcript" UI label
  and `transcript_url`/`transcription` field *names* in client-side script
  code, but the fetched `post` object itself has no populated transcript
  text, and no transcript is rendered anywhere in the page's HTML. This
  episode's full spoken interview (where the diffusion-vs-autoregression
  decision, the CRISPR protocol, the linear-baseline benchmark, and the
  "kitchen-sink of priors" discussion would presumably be covered) exists
  only as audio/video, consistent with the pattern already documented for
  another Latent Space episode in this corpus
  (`blog-latentspace-lila-sciences-lab-data-center.md`, Extraction Notes).
  Every `Quote` in this note is therefore the host's (RJ Honicky's) own
  written framing or a bare show-notes topic label, not a direct
  transcription of Bo Wang's or Ci Chu's spoken words — reflected in the
  `confidence_overall: anecdotal` rating.
- The written page is short (667 words per the source's own metadata) —
  most of its substance is in Claims 1-10; Claims 11-12 are included
  despite being bare, unelaborated topic labels because they name specific,
  checkable technical questions (architecture choice, baseline comparison)
  that a future miner could re-extract if a transcript or written paper
  becomes available.
- No linked sub-pages were followed: the episode page links only to
  external prior episodes (Boltz, ESM/BioHub) as background context and to
  YouTube/podcast platforms for the full audio, none of which contain
  additional written text to mine.
- Checked for contradictions against `blog-latentspace-lila-sciences-lab-data-center.md`
  (data-generation-as-strategy, closest topical match) and against Ch04's
  existing training-data-gap material — found extension/corroboration
  relationships (see Cross-References), not contradiction. No existing
  source note in this corpus makes a claim about observational-data
  sufficiency for causal prediction that this source's Claim 8 would
  oppose, so no contradiction issue was filed per MINER.md §4a.
- The three Prospector triage comments on this issue gave inconsistent
  chapter guidance (Ch03/Ch04; Ch02/Ch03/Ch04/Ch05; Ch02/Ch03). This note's
  Guide Impact section reflects independent judgment from reading the
  source directly: only Ch04's training-data-gap material has content this
  thin a source can actually change with confidence. Ch02 (harness
  engineering) and Ch03 (verification) were considered but not used,
  because the source gives no accessible detail on Xaira's actual
  engineering harness, evaluation loop, or verification methodology — only
  bare topic teasers pointing at where that detail would live in the
  audio.
