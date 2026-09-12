---
source_url: https://www.latent.space/p/anima
source_type: blog-post
title: "\"We have foundation models for language, not for physics\" — Anima Anandkumar, Bren Professor of Computing"
author: Latent Space (Brandon Anderson, co-host of AI Science podcast), interviewing Anima Anandkumar (Bren Professor, Caltech; co-founder, Accelerated Understanding)
date_published: 2026-08-26
date_extracted: 2026-09-12
last_checked: 2026-09-12
status: current
confidence_overall: emerging
issue: "#3406"
---

# "We have foundation models for language, not for physics" — Anima Anandkumar

> A Latent Space podcast episode (written intro/show-notes essay; no full
> spoken transcript is published on the page) arguing that continuous
> physical-simulation domains (weather, fusion, fluid/heat flow) resist
> transformer-style data-and-compute scaling because of a data ceiling and a
> combinatorial context-length wall, and that progress instead comes from
> encoding physical structure (Neural Operators) directly into the model.

## Source Context

- **Type**: blog-post (podcast episode landing page, Latent Space Substack,
  published 2026-08-26). The page's rendered content is an ~875-word written
  essay by the host (Brandon Anderson) plus an audio/video embed of the
  interview itself. Confirmed via the page's embedded JSON (`post.wordcount:
  875`, matching the extracted body text exactly) that this essay is the
  *entire* public text content — there is no separate rendered transcript of
  the spoken interview on this page. Two passages are set off in
  `<blockquote>` tags and are direct quotations of Anandkumar; the rest of
  the essay is the host's own paraphrase/summary of her work and the
  conversation.
- **Author credibility**: Anima Anandkumar is a named, credentialed subject
  speaking about her own published research — Bren Professor at Caltech,
  co-founder of Accelerated Understanding, and (per the essay) a co-inventor
  of Neural Operators, with published work cited in the essay: FourCastNet
  (arXiv:2202.11214) and Neural Operators (arXiv:2108.08481). The host,
  Brandon Anderson, is credited as "Co-host of AI Science podcast as part of
  Latent.Space" — Latent Space is a widely-cited AI engineering
  podcast/newsletter already represented many times in this corpus. Treat the
  headline architectural claims (data ceiling, context-length infeasibility,
  Neural Operators' mechanism) as backed by peer-reviewed publications; treat
  the specific numbers relayed only in the essay (sample counts, "a million
  times faster") as self-reported, secondhand-paraphrased claims with no
  disclosed methodology.
- **Scope**: Covers Anandkumar's argument for why token/parameter scaling
  fails for continuous physical-simulation domains, the Neural Operator
  technique and its application in FourCastNet (global weather), a fusion
  plasma-disruption result, TorchLean (formal verification of neural networks
  in the Lean proof assistant), and her appointment to the UN Scientific
  Advisory Board. Does NOT cover: training methodology or hyperparameters for
  FourCastNet, benchmark comparisons against specific physics simulators,
  the plasma-disruption dataset or evaluation protocol, or any detail on
  TorchLean's verification guarantees — all of these are named but not
  elaborated on the page itself.

## Extracted Claims

### Claim 1: Physics-simulation domains have far less usable training data than language, with open datasets in the tens-to-hundreds-of-thousands-of-examples range rather than the token counts modern transformers are trained on

- **Evidence**: Stated as the host's framing claim for why scaling ideas
  don't transfer from language modeling to physics.
- **Confidence**: anecdotal (host's general claim, no specific dataset named
  or counted)
- **Quote**: "The data isn't there: open source datasets in many of these
  domains are limited to tens or hundreds of thousands of examples, far from
  what token-hungry transformers need."
- **Our assessment**: Plausible and consistent with the domain (physical
  experiments and high-fidelity simulations are expensive to generate,
  unlike scraped text), but presented as an unquantified generalization
  across "many of these domains" rather than a specific, checkable figure.

### Claim 2: The spatial resolution physics problems demand would require transformer context lengths in the hundreds of billions to a trillion tokens, which is computationally infeasible with any foreseeable amount of compute

- **Evidence**: Direct quotation from Anandkumar, reasoning from grid
  dimensionality (a few hundred grid points per dimension at "industrial
  scale") to total context length.
- **Confidence**: emerging (a first-party technical argument from a domain
  expert, but presented as an order-of-magnitude estimate rather than a
  worked derivation on the page)
- **Quote**: "If each dimension is even a few hundred grid points, which is
  where industrial scale starts... we're talking hundreds of billions to
  even a trillion context length. So forget ever having a transformer for
  anything of this scale, all of the world's compute will not be enough."
- **Our assessment**: This is the essay's central technical claim and the
  most load-bearing one: it isn't just "less data than language," it's a
  structural argument that naively tokenizing a high-resolution physical
  grid produces a context-length requirement that scales combinatorially
  with dimensionality, putting it permanently out of reach of
  transformer-style scaling regardless of future compute growth. Worth
  flagging that "all of the world's compute will not be enough" is a strong,
  unfalsifiable-sounding claim on its own — it becomes credible mainly
  because of the concrete grid-dimensionality argument that precedes it.

### Claim 3: Progress in physics-simulation AI comes from building in structure and inductive biases rather than from pure data/compute scale — this is a slower path, not a dead end

- **Evidence**: Host's synthesis of the argument, framed explicitly against
  "the bitter lesson."
- **Confidence**: emerging (architecturally coherent framing, directly
  connected to Anandkumar's published Neural Operators work, but the
  "slower road, not a ceiling" framing is the host's own characterization)
- **Quote**: "That isn't a ceiling though, just a slower road: progress here
  comes from building in structure and inductive biases. Sorry for all you
  bitter-lesson-pilled language modelers."
- **Our assessment**: This is a direct, explicit counter-claim to "the
  bitter lesson" (general methods + scale beat hand-engineered structure) —
  but scoped specifically to continuous, grid-based physical simulation
  domains, not to AI broadly. See Cross-References for how this sits next to
  other bitter-lesson claims already in the corpus.

### Claim 4: Neural Operators model a function that evolves across multiple scales, rather than a fixed grid, letting physical laws and domain priors be built directly into the architecture

- **Evidence**: Host's description of Anandkumar's Neural Operators
  technique, linking to the published paper (arXiv:2108.08481).
- **Confidence**: settled (published, peer-reviewed technique with the
  primary inventor as the source)
- **Quote**: "These allow you to combine data and physical laws to enable
  multi-scale inputs and outputs. We're no longer modeling a grid, we're
  modeling a function that evolves over many scales."
- **Our assessment**: This is the essay's clearest statement of the
  mechanism, not just the motivation — it names the specific representational
  shift (function-valued rather than grid-valued modeling) that makes
  building in physical priors possible. This is the concrete alternative the
  essay offers to naive high-resolution tokenization (Claim 2).

### Claim 5: FourCastNet's Fourier Neural Operator learns directly in the frequency domain — using spherical harmonics for global weather modeling — which keeps rollouts stable for months instead of days, unlike grid-based approaches that "blow up fast"

- **Evidence**: Host's description tied to the published FourCastNet work
  (arXiv:2202.11214) and a specific basis-set choice (spherical harmonics,
  chosen because "the earth is a sphere").
- **Confidence**: emerging (specific technical mechanism attributed to a
  published paper by the same author, but the "months instead of days"
  stability comparison is asserted in the essay without a cited figure or
  ablation)
- **Quote**: "Run a weather model on a grid and it blows up fast. Move to
  the natural basis for the problem and it stays stable far longer, long
  enough to roll out months ahead instead of days."
- **Our assessment**: A concrete, checkable-in-principle claim (rollout
  stability duration is measurable), but the essay gives no side-by-side
  numbers — "days" vs. "months" is qualitative here, not a reported
  benchmark result.

### Claim 6: FourCastNet is a predictive weather model competitive with the best physics-based simulations available, built within about a year, and runs on consumer-grade GPUs rather than requiring supercomputers

- **Evidence**: Host's opening framing story, describing initial expert
  skepticism followed by the FourCastNet result.
- **Confidence**: emerging (tied to a published, citable paper, but the
  "competitive with the best physics-based simulations" framing and the
  one-year timeline are the host's summary, not a benchmark table on the
  page)
- **Quote**: "Within a year her team had developed FourCastNet, a predictive
  model that is competitive with the best physics-based simulations
  available. Thanks to Anima, and her follow up work, anyone can now predict
  weather accurately over a short timescale using consumer grade GPUs."
- **Our assessment**: The consumer-GPU-vs-supercomputer contrast is the
  practically interesting part for an engineering audience: it reframes the
  win as an inference-cost/accessibility result, not purely an accuracy
  result. Should be read as a directional claim (this class of model is far
  cheaper to run than a physics simulator) rather than a specific,
  reproducible cost figure.

### Claim 7: In fusion research, a few thousand samples were sufficient to train a model to predict plasma disruptions, running roughly a million times faster than traditional simulation

- **Evidence**: Host's summary of a separate application of Neural Operators
  outside weather, presented as evidence that "the physical world is more
  forgiving than you'd expect."
- **Confidence**: anecdotal (specific numbers — "a few thousand samples,"
  "a million times faster" — given with no citation, dataset description, or
  simulation baseline named on the page)
- **Quote**: "In fusion, a few thousand samples are enough to predict plasma
  disruptions, and to do it a million times faster than traditional
  simulation."
- **Our assessment**: The most eye-catching figure in the source and also
  the least substantiated on the page — no paper link, no definition of
  "sample," and no description of what "traditional simulation" means as
  the speed baseline. Treat as a directional data point (small-sample
  regimes can work when physical structure is built in) rather than a
  benchmarked result; would need the underlying paper to verify.

### Claim 8: Anandkumar's stated long-term goal is a "foundation model for physics" — one model spanning many physical phenomena that does both simulation and design — built by encoding the physical world's existing structure rather than by waiting for internet-scale data to materialize

- **Evidence**: Host's synthesis plus a direct quotation of Anandkumar's own
  framing of her approach.
- **Confidence**: emerging (a stated research goal from the primary
  researcher, not yet a demonstrated result)
- **Quote**: "All of the things that work with deep learning, let's take
  them, but make them a bit more principled."
- **Our assessment**: This is the clearest articulation of the essay's
  overall thesis in Anandkumar's own words: not a rejection of deep learning
  methods, but a claim that they need additional structure/principles to
  work in physics. Notably this is presented as a goal, not a result — the
  essay does not claim a physics foundation model already exists.

### Claim 9: TorchLean lets researchers write PyTorch-style neural networks inside the Lean proof assistant and formally verify them, which matters for use cases like adding a neural network to a fusion reactor's control loop where provable bounds are needed

- **Evidence**: Host's description of a named framework and a specific
  motivating use case (safety-critical control loops).
- **Confidence**: anecdotal (framework named and use case given, but no
  detail on what properties TorchLean can actually verify, what the
  performance/expressiveness tradeoffs are, or whether it has been applied
  to a real control loop)
- **Quote**: "We talk about TorchLean, a new framework that lets you write
  PyTorch-style networks inside the proof assistant Lean and formally verify
  them. This is a major step for proving bounds on neural networks, something
  that would be really important for someone trying to, e.g., add a neural
  network as part of the control loop to their fusion reactor!"
- **Our assessment**: Interesting adjacent claim about formal verification
  of neural networks, but it's named as a discussion topic with an
  illustrative hypothetical ("someone trying to...") rather than a reported
  deployment. The written page gives no technical detail on TorchLean itself
  — that discussion is audio/video-only.

## Concrete Artifacts

Direct quotations from Anandkumar (set off as `<blockquote>` in the
source's HTML, distinguishing them from the host's paraphrase):

```
"If each dimension is even a few hundred grid points, which is where
industrial scale starts... we're talking hundreds of billions to even a
trillion context length. So forget ever having a transformer for anything
of this scale, all of the world's compute will not be enough."

"All of the things that work with deep learning, let's take them, but make
them a bit more principled."
```

Cited published work (linked inline in the source essay, not reproduced
verbatim here):
- FourCastNet: https://arxiv.org/abs/2202.11214
- Neural Operators: https://arxiv.org/abs/2108.08481

Pull-quote-style section captions from the source page (these read as
image/section captions embedded in the essay's HTML, attributed to the
host, not to Anandkumar):

```
"Neural Operators — What if we created a neural network where every layer
was itself a function?"

"FourCastNet 3 — The earth is (almost) a sphere — bake the spherical
harmonics into your network!"
```

## Cross-References

- **Corroborates**: `blog-latentspace-xaira-causal-data-drug-discovery.md`
  (Claim 1: "A test-loss plateau that persists while training loss keeps
  falling as parameters scale indicates the model is capped by the
  information content of its training data, not by model capacity or
  compute"). Both sources independently make the same underlying
  engineering point about scientific/physical domains: past a certain
  point, adding parameters or compute stops helping and the bottleneck is
  the information content of the data itself — Xaira's Claim 1-3 diagnose
  this via a train/test loss gap in gene-expression modeling, while this
  source's Claim 1-2 diagnoses it via a combinatorial context-length
  argument for grid-based physics. Different domains, same shape of
  argument: "you can't out-scale a data/structure bottleneck."
- **Extends (with a tension worth flagging)**:
  `blog-latentspace-lila-sciences-lab-data-center.md`. That note's Claim 6
  and Claim 13 describe Lila Sciences as explicitly "all in on the bitter
  lesson" for scientific discovery generally (chemistry, biology, materials,
  drug discovery) — a general model trained on breadth of experimental
  "reasoning tokens" is claimed to beat domain-specific models sample for
  sample — while also recording (Claim 13) their own internal caveat that
  "in materials, scaling is a filter, [not a roadmap] because only the
  things that scale end up mattering." This source's Claim 3 makes a
  stronger and more absolute version of that caveat for a different physical
  sub-domain: continuous, grid-based simulation (weather, fusion, fluid
  flow), where Claim 2's context-length argument is presented as a hard
  computational wall, not merely a filter on which discoveries end up
  mattering. We are **not** filing this as a contradiction issue per
  `agents/MINER.md` §4a — the two sources describe different problem
  shapes (Lila: discrete molecular/biological design over
  experimentally-generated reasoning traces; this source: continuous
  PDE-style field simulation over spatial grids) rather than opposing
  claims about the same conditions. Worth flagging for the Smith as a
  domain-conditioning nuance on "does the bitter lesson apply to
  scientific AI": the answer this corpus is converging on appears to be
  "it depends on whether the domain's data-generating process is discrete
  and experimentally samplable, or continuous and grid/resolution-bound."
- **Novel**: The specific mechanism by which grid resolution defeats
  transformer scaling (Claim 2's context-length-from-grid-dimensionality
  argument) is new to this corpus — prior data-scarcity claims (e.g., Xaira's
  test-loss-plateau diagnostic) describe a data *quantity* bottleneck, not a
  *representational* one where the natural tokenization of the problem
  itself is computationally intractable at any data quantity. Also novel:
  Neural Operators as a named alternative representational paradigm
  (function-valued rather than grid-valued modeling, Claim 4) and TorchLean
  as a formal-verification-for-neural-networks framework (Claim 9) — neither
  appears elsewhere in the corpus searched.

## Guide Impact

This source is only weakly and indirectly relevant to the guide's current
scope. The guide (`guide/00` through `guide/06`) is specifically about
AI-native *software engineering* practice — harness engineering, agent
verification loops, context engineering, and team adoption for coding
agents — not about ML model architecture choices for scientific computing.
None of the guide's chapters currently discuss physical-simulation domains,
neural network architecture design, or scaling laws for non-language
models, so there is no existing guide claim this source directly
supports, updates, or corrects.

- **No direct chapter update recommended.** The Prospector's three triage
  passes on this issue proposed inconsistent chapter mappings (Ch02/Ch04/
  Ch07/Ch09 in one pass, Ch02/Ch03/Ch04 in another) which, combined with the
  guide's actual chapter list (00-principles, 01-daily-workflows,
  02-harness-engineering, 03-verification, 04-context-engineering,
  05-team-adoption, 06-security-threat-model — there is no Ch07 or Ch09),
  suggests the triage over-fit this source to the guide's rubric rather than
  finding a genuine match.
- **Weak, analogical connection only**: `guide/02-harness-engineering.md`
  (~line 1230, "Domain-Specific Skills as Workflow Guides") already
  recommends extracting domain-specific procedural knowledge into skills
  rather than relying on a general model to infer it from context. This
  source's Claim 3/Claim 4 (build in domain structure rather than relying on
  scale) is the same shape of idea one level down the stack (model
  architecture vs. prompt/context engineering), but the domains are
  different enough (physical simulation vs. software workflows) that we do
  **not** recommend citing this source in that section — noting the parallel
  here for the Smith's awareness only, not as an actionable edit.
- Recommend the Smith treat this primarily as corpus background (useful for
  cross-referencing future scientific-AI sources, per Cross-References
  above) rather than as a source that should change guide text.

## Extraction Notes

- The page's rendered HTML contains only the host's written essay (~875
  words, confirmed against the page's embedded `post.wordcount` metadata
  field) plus an audio/video embed. There is no full transcript of the
  spoken interview in the page's static content — this was confirmed by
  fetching the page's raw HTML directly (not through a summarizing
  fetch) and locating the embedded `window._preloads` JSON payload, which
  contains the complete `post.body_html` field and no separate transcript
  field. All non-blockquoted claims are therefore the host's (Brandon
  Anderson's) written paraphrase of the conversation and Anandkumar's
  published work, not direct transcription of her spoken words — claims are
  attributed accordingly throughout ("the essay states" / host's
  description) except where a direct quotation is explicitly quoted.
- Followed the two inline links to Anandkumar's published papers
  (FourCastNet, arXiv:2202.11214; Neural Operators, arXiv:2108.08481) only
  to confirm they are real, citable publications backing the architectural
  claims — did not extract claims from the papers themselves, as that is
  outside the scope of this essay-level source note and would be a
  substantial secondary-source extraction task of its own.
- Did not attempt to transcribe the embedded audio/video, which is outside
  this Miner's text-extraction scope.
- Checked for a contradiction filing per `agents/MINER.md` §4a against
  `blog-latentspace-lila-sciences-lab-data-center.md`'s bitter-lesson framing
  (see Cross-References) and concluded the two sources differ by domain
  conditioning (continuous/grid-based physics vs. discrete/experimental
  molecular design) rather than by genuine disagreement on the same
  question, so no contradiction issue was filed.
