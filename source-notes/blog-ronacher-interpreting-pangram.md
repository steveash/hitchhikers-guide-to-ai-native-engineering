---
source_url: https://lucumr.pocoo.org/2026/9/14/interpreting-pangram/
source_type: blog-post
title: "Interpreting Pangram"
author: Armin Ronacher
date_published: 2026-09-14
date_extracted: 2026-09-15
last_checked: 2026-09-15
status: current
confidence_overall: anecdotal
issue: "#3446"
---

# Interpreting Pangram

> Armin Ronacher runs a controlled two-stage experiment against the Pangram
> AI-text detector — LLM-generated text, then a full sentence-by-sentence
> human rewrite of that same text — and finds the detector still scores the
> fully human-rewritten version "100% AI," suggesting LLM-supplied structure
> and ideation leave a persistent signal that manual rewriting does not
> remove, even as a light LLM typo-pass on genuinely human-written text
> leaves no signal at all.

## Source Context

- **Type**: blog-post (lucumr.pocoo.org personal blog; ~900 words; published
  2026-09-14). The site publishes a parallel markdown mirror at
  `https://lucumr.pocoo.org/2026/9/14/interpreting-pangram.md`, which this
  note was extracted from directly (see Extraction Notes).
- **Author credibility**: Armin Ronacher is the creator of Flask, Jinja2,
  Click, and Sentry, and the author of the Pi coding agent — a `trusted-feed`
  source already extensively used in this corpus (`blog-ronacher-pi-oss.md`,
  `blog-ronacher-content-for-contents-sake.md`, `blog-ronacher-astra-why.md`,
  among others). This post is a first-person, reproducible experiment: he
  publishes the exact prompt he used, the full LLM-generated text, and his
  own full hand-rewritten version, along with links to the three individual
  Pangram detection reports. It is not a controlled study (n=2 texts,
  single detector, single author) but the methodology and raw texts are
  fully disclosed, making the claims independently checkable by a reader.
  He also maintains a standing "AI Transparency Statement" page for the
  blog, which this note followed as a linked sub-page (see Extraction
  Notes).
- **Scope**: Covers one detector (Pangram, specifically "Pangram 4" per the
  linked technical report), one practitioner's two-text experiment, and
  Ronacher's own reflection on what the experiment implies about his
  blogging workflow. Does **not** cover other AI-text detectors (GPTZero,
  Originality.ai, etc.), a statistically powered sample, or Pangram's full
  published benchmark suite beyond the headline metrics in the paper
  abstract.

## Extracted Claims

### Claim 1: Text produced with LLM assistance as a "writing assistant" is frequently flagged "100% AI" by Pangram even when the author doesn't feel the result reads as AI-generated

- **Evidence**: Ronacher's direct first-person observation, stated as the
  motivating premise of the post, prior to running his own experiment.
- **Confidence**: anecdotal
- **Quote**: "Now Pangram has a pretty low false positive rate, but if you
  have ever used an LLM as a writing assitant, you will have probably
  noticed that it claims your posts 100% AI, even though you don't *feel*
  like they are."
- **Our assessment**: This is the felt problem the rest of the post
  investigates empirically. The gap between "feels human-authored" and
  "scores as AI" is exactly the ambiguity zone that matters for engineering
  teams whose written artifacts (PR descriptions, design docs, incident
  postmortems) are co-authored with LLMs — see Guide Impact.

### Claim 2: Pangram trains its classifier on synthetically manufactured co-authorship data — an LLM is tasked to write a fresh text from a description of human-authored text, and separately to make partial edits directly on human text, so the model learns to recognize these co-authored patterns

- **Evidence**: Ronacher's summary of Pangram's published methodology paper
  (linked in the post as "they published a paper," arXiv:2607.27183,
  "Pangram 4 Technical Report").
- **Confidence**: emerging (Ronacher's paraphrase of a vendor-published
  technical report; the report itself is a primary source but this is not a
  direct quote from it — see Claim 3 for the primary-source abstract text)
- **Quote**: "The short summary is that they are manufacturing its own
  training data by starting from collections of known human authored text.
  An LLM is then tasked to understand the text and write a fresh new text
  on the same topic. They also let the LLM perform partial edits on that
  original human text and through that they can pick up on these
  co-authored details."
- **Our assessment**: This explains the mechanism behind Claim 1: the
  detector isn't just trained on "pure AI vs. pure human" text, it is
  specifically trained on the boundary case — partially-edited,
  co-authored text — which is exactly the category most LLM-assisted
  human writing falls into. That training choice is a plausible reason the
  detector is aggressive about flagging LLM-influenced prose even when a
  human did substantial editing.

### Claim 3: Pangram 4's own published technical report claims an AUROC of 0.9916, a false positive rate of 0.0041%, and a false negative rate of 0.3396%, with a specific claimed improvement in distinguishing "fine-grained edits and mixed AI-human co-authored text"

- **Evidence**: Direct text from the abstract of the linked primary source,
  "Pangram 4 Technical Report" (Glickenhaus, Thai, Russell, Masrour, Han,
  Spero, Emi; arXiv:2607.27183, submitted 29 Jul 2026), followed from
  Ronacher's "they published a paper" link.
- **Confidence**: emerging (vendor's own self-reported benchmark metrics in
  a published technical report; not independently audited in this source,
  but a named, citable primary document rather than a vague vendor claim)
- **Quote**: "We achieve an AUROC of 0.9916 with a false positive rate of
  0.0041% and a false negative rate of 0.3396%... Another novel
  contribution of Pangram 4 is its improved ability to distinguish
  fine-grained edits and mixed AI-human co-authored text."
- **Our assessment**: This corroborates Ronacher's 0.0041% / 0.34% figures
  character-for-character (his "0.34% missed AI text" matches the paper's
  0.3396% false negative rate). The paper's own framing — that the
  headline improvement in this version is specifically about "fine-grained
  edits and mixed AI-human co-authored text" — is consistent with, and
  gives vendor-side confirmation to, the training methodology Ronacher
  describes in Claim 2.

### Claim 4: In a first experiment, Ronacher had an LLM (Opus 5) generate a complete text end-to-end from an LLM-assisted prompt, attempting to recreate a public tweet by David Sacks; Pangram scored the resulting text 100% AI

- **Evidence**: Ronacher's documented, reproducible experiment — he
  publishes the exact prompt used (itself partly LLM-suggested) and the
  full Opus-5-generated text in the post, plus a link to the specific
  Pangram detection report for that text.
- **Confidence**: anecdotal (n=1 practitioner demonstration, but fully
  reproducible: prompt, model, and generated text are all disclosed)
- **Quote**: "And well, Pangram agrees that this is 100% AI. So far, so
  uninteresting."
- **Our assessment**: Ronacher frames this result as the expected,
  unsurprising baseline — a fully LLM-generated text scoring as AI is not
  informative on its own. Its value is as the control condition for
  Claim 5.

### Claim 5: In a second experiment, Ronacher manually rewrote every paragraph of the AI-generated text by hand — with an LLM used only afterward to fix typos, not to write or rephrase — producing a version that similarity checkers rated only about 50% similar to the original with, in Ronacher's words, not a single identical sentence; Pangram still scored this fully human-rewritten text 100% AI ("100% slop")

- **Evidence**: Ronacher's documented experiment; he publishes his full
  hand-rewritten text in the post and a link to its separate Pangram
  detection report, plus a self-reported similarity-checker percentage
  comparing it to the original AI-generated text.
- **Confidence**: anecdotal (n=1, but methodology and both full texts are
  disclosed, making the result independently checkable and falsifiable by
  a reader who runs the same texts through Pangram)
- **Quote**: "I read the generated text. Then I read each paragraph and
  decided to rewrite and rephrase it without an LLM. According to some
  similarity checkers, they the final texts are 50% similar which seems
  about right. But strictly speaking, not a single sentence is the same.
  Here is the 100% human rewritten text of the above one. No LLM was used
  to write it, but an LLM was used to fix up typos in the end... So what
  does it say? Well this text too comes back as 100% slop."
- **Our assessment**: This is the central, most guide-relevant finding in
  the post. Sentence-level authorship (every sentence rewritten by hand)
  was not sufficient to change the detector's verdict once the underlying
  structure and ideas originated with an LLM. This complicates any
  practitioner assumption that "if I substantially rewrite AI output in my
  own words, it stops being detectable as AI-influenced" — at least for
  Pangram's classifier and at least for this one text pair.

### Claim 6: Ronacher's own interpretation is that LLM-supplied structure persists as a detectable signal through heavy sentence-level rewriting, and that it is unlikely a piece that "starts out as slop" can be edited into a structure that no longer registers as such

- **Evidence**: Ronacher's inference drawn directly from the Claim 4/5
  experiment pair, generalized to his broader writing experience beyond
  this single test.
- **Confidence**: anecdotal (single practitioner's interpretation of a
  two-text sample, though stated as consistent with his general
  experience)
- **Quote**: "I have generally noticed that if you rely on an LLM to give
  your text structure, it will score badly on Pangram even if you do
  plenty of edits over it. In fact, it's quite unlikely you're going to
  get a post that starts out as slop into a structure that will make it
  appear that it's not."
- **Our assessment**: This distinguishes "wording" from "structure" as the
  signal Pangram is actually picking up on — consistent with Claim 2's
  description of a classifier specifically trained to detect co-authorship
  patterns rather than just surface vocabulary. If accurate, it implies
  the practical lever for reducing an "AI" classification is not
  word-level paraphrasing but avoiding LLM-originated outlines/structure in
  the first place.

### Claim 7: Using an LLM only to fix typos in an otherwise entirely human-written and human-structured text does not trigger the detector

- **Evidence**: Ronacher's own report of his workflow for the rewritten
  text in the Claim 5 experiment.
- **Confidence**: anecdotal
- **Quote**: "No LLM was used to write it, but an LLM was used to fix up
  typos in the end. That from my experience really does nothing to tick
  off an LLM detector."
- **Our assessment**: This is an important qualifier on Claim 1: not every
  LLM touch triggers a "100% AI" verdict. Light copyediting/proofreading
  assistance on human-originated, human-structured text appears not to
  register, while LLM involvement in the ideation/structuring stage does.
  This is a meaningful nuance for any team writing a disclosure policy —
  see Guide Impact.

### Claim 8: Ronacher values Pangram because running the experiment made him newly aware of how reliant he has become on LLM tools for his own writing, and that those tools have become "much more aggressive editors" over time, which gave him pause

- **Evidence**: Ronacher's first-person reflection at the end of the post,
  cross-referencing his standing "AI Transparency Statement" page, which
  states the blog has used LLMs for "editing and stylistic improvements"
  for about two years, and separately for "ideas... and as a sparring
  partner in brain storming."
- **Confidence**: anecdotal
- **Quote**: "I came to quite appreciate the existance of Pangram because
  at the very least it has made me quite aware of some of the effects that
  using LLMs for writing blog posts has. This blog has been AI supported
  for about two years... but I did notice that I became both more reliant
  on those tools and that they have become much more aggressive editors
  and it gave me pause."
- **Our assessment**: This self-observation — that the same category of
  tool use ("editing help") has grown more invasive over roughly two years
  without a corresponding change in his own disclosure practice — is a
  plausible failure mode for any individual or team with a static AI-use
  disclosure policy: the tools' actual influence on output can silently
  expand within a stated policy that hasn't changed.

### Claim 9: Ronacher concludes that a "100% AI" rating can be misleading when substantial human editing occurred, while simultaneously questioning whether it is nonetheless fair to rate heavily LLM-structured text as entirely AI — he does not resolve the tension

- **Evidence**: Ronacher's closing reflection, presented as an open
  question rather than a settled position.
- **Confidence**: anecdotal
- **Quote**: "Yet, I also think that plenty of people will find a '100%
  AI' rating misleading when in fact the author has done plenty of
  editing. But maybe it's fair to have this to show up as entirely AI?"
- **Our assessment**: Ronacher deliberately leaves this unresolved rather
  than picking a side. For the guide, the value is in naming the tension
  precisely rather than in an answer: "100% AI" is technically defensible
  under Pangram's training definition (structure/ideation-origin) while
  being intuitively misleading under a layperson's definition (how much of
  the final wording is the human's own).

### Claim 10: Pangram's classifier attempts fine-grained, per-segment classification (human / AI / mixed) rather than a single binary document-level judgment, even though the headline number reported back to users (e.g. "100%") reads as one score

- **Evidence**: Ronacher's description of what Pangram is trying to do,
  stated before he runs his experiment.
- **Confidence**: emerging (consistent with the "fine-grained edits and
  mixed AI-human co-authored text" claim in the paper abstract, Claim 3)
- **Quote**: "Pangram itself is a trained model, that attempts to detect
  segments of text as being definitely human, definitely AI and a mixture
  of the two."
- **Our assessment**: This matters for interpreting the headline "100% AI"
  / "100% slop" verdicts reported elsewhere in the post — those are
  presumably an aggregate of segment-level classifications, not evidence
  that the model treats documents as atomically all-or-nothing. The post
  itself doesn't show the segment-level breakdown for either of Ronacher's
  two experimental texts, so this claim describes the detector's design
  intent rather than something demonstrated in this particular experiment.

## Concrete Artifacts

### The experiment prompt (verbatim, as published)

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/9/14/interpreting-pangram/
Disclosed as: "the prompt I used" to generate a David-Sacks-style tweet
(Ronacher states he used an LLM to help propose this prompt's structure
from the original tweet.)

Please write an 8 paragraph tweet about "Pacing the Frontier", not longer than 350 words.

Context of this tweet is this post by Dario:
https://darioamodei.com/post/we-must-pace-the-frontier

And this tweet by Sam Altman: "I agree with Dario that we need to pace
the frontier. This has been a primary topic of discussions we've had at OpenAI
in recent weeks.

Committing to having independent evaluators with employee-like access is a
great idea, and we will do the same. We'll have more to share soon."

Structure for the post:

- Open with a concession: Note that Dario ("We Must Pace the Frontier") and Sam Altman both want to slow down at the frontier. Say "go ahead" which reads as a surprising response.
- Establish they own the frontier: Argue OpenAI and Anthropic hold a duopoly on frontier intelligence by all kind of metrics (market share, capability, revenue etc.) and that they themselves claim the lead is widening via RSI.
- Concede you can't see their unreleased models, so if those are scary, being responsible is their call.
- Follow with a list of a rapid-fire paragraph ("stop pretending") rejecting the asks from Dario's post.
- Name the commercial self-interest (Slowing down isn't purely altruistic)
- Close with the challenge that pacing buys room for a smarter regulatory debate than Bernie Sanders "shut it all down". Say something about China and Open Weight models.
```

### Detection verdicts across the two-stage experiment (Ronacher's own summary, with linked Pangram reports)

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/9/14/interpreting-pangram/

Stage 1 — Opus 5 generates full text from the prompt above:
  Verdict: "100% AI"
  (linked Pangram report: pangram.com/history/6c189841-c4e3-4dfe-b3e7-0db39a183ef1)

Stage 2 — Ronacher hand-rewrites every paragraph of the Stage-1 text without
an LLM (LLM used only for a post-hoc typo pass); similarity checkers rate
Stage 2 vs. Stage 1 at ~50% similarity, with no identical sentences:
  Verdict: "100% slop" (i.e. 100% AI)
  (linked Pangram report: pangram.com/history/9106f398-e1c3-406b-bea5-127f230dfc03)

For reference — the original disputed case that motivated the experiment:
  David Sacks' tweet was scored by Pangram as "entirely AI generated"
  (pangram.com/history/a6f16402-f194-4cc7-8315-ae8caeffbb67), which Sacks
  publicly called "bogus."
```

### Pangram 4 Technical Report — reported metrics (primary source, followed link)

```
Source: Ben Glickenhaus, Katherine Thai, Jenna Russell, Elyas Masrour,
Yue Han, Max Spero, Bradley Emi. "Pangram 4 Technical Report."
arXiv:2607.27183 [cs.CL], submitted 29 Jul 2026.
https://arxiv.org/abs/2607.27183

AUROC:                0.9916
False positive rate:  0.0041%
False negative rate:  0.3396%

Claimed novel capability of this version: "improved ability to distinguish
fine-grained edits and mixed AI-human co-authored text," plus improvements
to "boundary detection tasks" and "detection of interleaved AI assistance."
```

### Ronacher's AI Transparency Statement (linked sub-page, followed)

```
Source: Armin Ronacher, https://lucumr.pocoo.org/ai-transparency/

"All blog posts on this site are written by me. I use LLMs for editing and
stylistic improvements. I use generative tools to help refine grammar,
improve clarity, or polish the writing style, but the substance and
original thinking are my own.

I also routinely use LLMs to give me ideas for how to simplify ideas and
as a sparring partner in brain storming of blog posts."
```

## Cross-References

- **Corroborates and extends**: `blog-ronacher-content-for-contents-sake.md`
  Claim 6 ("The inability to distinguish human from LLM-generated text
  erodes trust in people you know, not just strangers") and Claim 8
  ("Declaring AI assistance when there is ambiguity is necessary to
  preserve social trust"). That note documents the *social* symptom
  (people can no longer tell human from AI text, so they distrust known
  contacts); this note documents a concrete *technical* mechanism that
  helps explain why the ambiguity is so persistent — a state-of-the-art
  detector cannot cleanly separate "human wrote every sentence" from "AI
  originated the structure" (Claim 5, Claim 6 here). Both notes also
  independently confirm Ronacher's personal transparency practice: the
  content-for-contents-sake note documents him disclosing tool use at the
  end of that post; this note's Concrete Artifacts section quotes his
  standing transparency-statement page directly.

- **Extends**: `blog-fowler-fragments-2026-06-02.md` Claim 10 ("'Humanizer'
  tools exist specifically to strip AI linguistic markers from generated
  text, adding deliberate imperfections to defeat AI detection"). That
  claim describes an adversarial, detection-evasion tool category. This
  note's Claim 5 shows a *non-adversarial* case — a good-faith, complete,
  sentence-level human rewrite, with no attempt to game the detector —
  still fails to flip the verdict. Together they suggest Pangram-style
  detectors are hard to fool by two very different paths (deliberate
  humanizer tooling vs. honest full rewriting), for two very different
  reasons (surface-marker removal vs. structural-origin persistence) —
  though this note's case is about a detector correctly refusing to be
  fooled by honest effort, while the Fowler/Koebler claim is about tools
  built to fool it deliberately.

- **Contradicts**: None identified. No existing corpus source makes a
  claim that heavy human rewriting reliably removes AI-detector signal, or
  that AI-text detectors are unreliable/inaccurate in a way that would
  conflict with the specific findings here. No contradiction issue filed.

- **Novel**:
  - **A reproducible two-stage experiment isolating "structure origin" from
    "sentence-level authorship" as distinct signals a detector can pick
    up on**: No other corpus source runs a controlled before/after
    experiment (LLM-authored text → full human rewrite) against a named
    AI-text detector and publishes both full texts plus the detector
    verdicts for each. This is the first source in the corpus to test the
    "just rewrite it in your own words" mitigation empirically rather than
    assuming it works.
  - **The vendor's own published methodology for a commercial AI-text
    detector**: No other corpus source describes how a detector like
    Pangram is trained (synthetic co-authorship data manufactured by
    having an LLM both write fresh text and partially edit human text).
  - **A quantified split between "LLM for structure/ideation" and "LLM for
    typo-fixing" as having different detectability**: Claim 7 (typo-fixing
    LLM use "does nothing to tick off" the detector) is a specific,
    actionable distinction not present elsewhere in the corpus.

## Guide Impact

- **Chapter 03 (Verification) / Chapter 05 (Team Adoption — "Code Review
  When AI Wrote It")**: The core finding (Claim 5) is directly relevant
  anywhere the guide currently assumes that a human editing pass is
  sufficient to make AI-assisted text "count" as human-authored for
  review or disclosure purposes. This source is evidence — from a single
  detector and a two-text sample, so cite as anecdotal, not settled — that
  structural/ideational origin can persist as a detectable signal
  through complete sentence-level rewriting. If the guide recommends
  "review AI output and rewrite in your own words" as a mitigation for
  any AI-generated-content risk (not just code), this source suggests
  that mitigation may not fully erase the artifact's AI-origin
  characteristics, at least as measured by current detectors.

- **Chapter 05 (Team Adoption — Communication and transparency norms)**:
  Extends the transparency-norm recommendation already sourced from
  `blog-ronacher-content-for-contents-sake.md` (Claim 8 there) with a
  concrete, actionable split from this note's Claim 7: a team writing an
  AI-disclosure policy for written artifacts (design docs, postmortems,
  PR descriptions) could reasonably draw the disclosure line at
  "LLM supplied structure/ideation" rather than "LLM touched the text at
  all" — since this source suggests light copyediting assistance is
  functionally different (and, per this one experiment, undetectable) from
  LLM-originated structure. Should be framed as a plausible policy lever
  drawn from one practitioner's anecdote, not a validated rule.

- **Chapter 03 (Verification)**: Claim 9's unresolved tension (a "100% AI"
  rating can be both technically accurate and intuitively misleading) is
  useful context for any guide discussion of AI-content detection tools:
  it cautions against treating a detector's binary/percentage output as a
  simple ground-truth signal of "how much of this a human actually wrote,"
  since the detector is measuring origin-of-structure, not
  fraction-of-final-wording.

## Extraction Notes

- Full markdown source fetched directly from
  `https://lucumr.pocoo.org/2026/9/14/interpreting-pangram.md` (the blog
  provides a markdown export endpoint, as with other Ronacher posts already
  in this corpus). All quotes verified character-for-character against
  that markdown source.
- Followed two linked sub-pages per MINER.md §1: (1) the Pangram 4
  Technical Report abstract on arXiv (arXiv:2607.27183), fetched directly,
  used for Claim 3 and the Concrete Artifacts primary-source block; (2)
  Ronacher's standing "AI Transparency Statement" page
  (lucumr.pocoo.org/ai-transparency/), fetched directly, used for Claim 8
  and its own Concrete Artifacts block. Did not follow the two linked
  X/Twitter posts (David Sacks' original tweet and his "bogus" reply) or
  the three individual Pangram detection-report URLs — these are primary
  evidence for claims already fully captured via Ronacher's own quoted
  summary and are not general-audience-readable pages suited to further
  extraction.
- The post is short (~900 words) but dense and fully reproducible: the
  prompt, both experimental texts, and the specific Pangram report links
  for each stage are all published inline. This is unusually high
  verifiability for a single-practitioner anecdotal source.
- Confidence rated anecdotal overall: the core empirical claim (Claim 5)
  rests on a single detector, a single author, and a two-text sample (one
  LLM-generated pair). The vendor's own published error-rate metrics
  (Claim 3) are self-reported and not independently audited in this
  source. The methodology is unusually transparent and reproducible for
  this category of claim, which is why several individual claims are
  rated "emerging" rather than "anecdotal," but the overall confidence
  reflects the small sample size of the central experiment.
