---
source_url: https://cursor.com/blog/grok-4-5
source_type: blog-post
title: "Introducing Grok 4.5"
author: Cursor Team (jointly with SpaceXAI)
date_published: 2026-07-08
date_extracted: 2026-07-10
last_checked: 2026-07-10
status: current
confidence_overall: anecdotal
issue: "#1704"
---

# Introducing Grok 4.5 (Cursor / SpaceXAI)

> Cursor's launch post for Grok 4.5 — the concrete fulfillment of the
> SpaceXAI "significantly larger model from scratch" promise from
> `blog-cursor-composer-2-5.md` — a mixture-of-experts model deliberately
> trained beyond software engineering (STEM, research papers, knowledge
> work), using a distributed agent system to construct difficult RL
> training environments at scale, with a disclosed CursorBench contamination
> incident from an accidentally-included Cursor codebase snapshot.

## Source Context

- **Type**: blog-post (product/model launch announcement, official Cursor
  blog, published July 8, 2026)
- **Author credibility**: Attributed to "Cursor Team" with no named individual
  authors (consistent with the Composer 2.5 announcement style rather than the
  named-author Composer 2 technical report). This is a first-party vendor
  announcement with a clear commercial incentive to present the model
  favorably. Notably, the post includes an unflattering, self-disclosed
  admission — a CursorBench contamination incident — which is the kind of
  detail a purely promotional post would omit; this raises the credibility of
  the post's other claims somewhat, even though none of them carry numeric
  benchmark evidence in the page text.
- **Scope**: Covers the Grok 4.5 launch (joint Cursor/SpaceXAI model),
  architecture (mixture-of-experts), training data composition and RL
  methodology at a high level, a disclosed benchmark contamination issue,
  positioning relative to Composer 2.5, platform availability, and pricing.
  Does NOT cover: specific benchmark scores or numeric comparisons (a
  benchmark chart image is referenced but not extractable as text), the
  underlying RL algorithm, model parameter counts, or a timeline for when the
  SpaceXAI-trained model was expected (per `blog-cursor-composer-2-5.md`
  Claim 10, announced May 2026 with no disclosed timeline).

## Extracted Claims

### Claim 1: Grok 4.5 is Cursor's first model built for domains beyond software engineering, developed jointly with SpaceXAI

- **Evidence**: Direct opening statement of the launch post, framed as both a
  capability milestone ("most intelligent") and a scope milestone ("first...
  for more than software engineering").
- **Confidence**: anecdotal (vendor launch framing; no independent verification
  of "most intelligent" is possible from this source)
- **Quote**: "Today we are releasing Grok 4.5 together with SpaceXAI, our most
  intelligent model and the first we've built for more than software
  engineering."
- **Our assessment**: This is the headline positioning claim of the entire
  post and the organizing frame for every other claim below (broader training
  data, broader RL environments, multi-domain capability claim). It directly
  fulfills the forward-looking SpaceXAI partnership announced two months
  earlier in `blog-cursor-composer-2-5.md` Claim 10 ("training a significantly
  larger model from scratch, using 10x more total compute").

### Claim 2: Grok 4.5 can handle difficult, long-running tasks across software engineering, data science, finance, legal work, and general computer-based work

- **Evidence**: Direct capability claim describing the target task
  distribution, explicitly naming domains beyond coding.
- **Confidence**: anecdotal (vendor capability claim; no task-level evidence
  or benchmark numbers given for the non-coding domains specifically)
- **Quote**: "Grok 4.5 can handle difficult, long-running tasks that require
  creatively using tools to solve problems, whether in software engineering,
  data science, finance, legal work, or anything else you do on a computer."
- **Our assessment**: This is the concrete unpacking of Claim 1's "more than
  software engineering" framing. "Creatively using tools to solve problems"
  echoes the same long-horizon, tool-use-centric framing used throughout the
  Composer line (`blog-cursor-composer-2-5.md`, `blog-cursor-real-time-rl.md`),
  but this is the first source in the corpus to extend that framing explicitly
  to non-coding professional domains (finance, legal). No task-level evidence
  is given for how well the model performs in those domains — this is a scope
  claim, not a performance claim.

### Claim 3: Grok 4.5 is a mixture-of-experts model trained jointly by Cursor and SpaceXAI

- **Evidence**: Direct architecture statement.
- **Confidence**: settled (specific, falsifiable architectural fact stated by
  the model's co-developer)
- **Quote**: "Grok 4.5 is a mixture-of-experts model that we trained jointly
  with SpaceXAI."
- **Our assessment**: MoE is consistent with the architecture pattern already
  established in the corpus for Cursor's coding models — Composer 2 was built
  via continued pretraining on Kimi K2.5, itself "a 1.04 trillion parameter
  mixture-of-experts model with 32 billion active parameters" (Claim 1,
  `blog-cursor-composer2-technical-report.md`). Grok 4.5 is a different lineage
  (trained from scratch with SpaceXAI per the Composer 2.5 announcement,
  rather than continued pretraining on a Kimi base), but the MoE architecture
  choice for large-scale coding-capable models is corroborated across both
  lineages. No parameter count is disclosed for Grok 4.5 in this source.

### Claim 4: Training included trillions of tokens of Cursor data capturing real user interactions with codebases and software tools

- **Evidence**: Direct training-data composition statement.
- **Confidence**: anecdotal (vendor-stated data volume; no independent
  verification possible, no breakdown of what fraction of total training
  tokens this represents)
- **Quote**: "Training included trillions of tokens of Cursor data which
  capture a wide-range of user interactions with codebases and software
  tools."
- **Our assessment**: This is the same production-interaction-data strategy
  documented elsewhere in the corpus (e.g., the real-time RL pipeline in
  `blog-cursor-real-time-rl.md`, which trains on "billions of tokens from user
  interactions"), but here it is described as pretraining/base-training data
  volume ("trillions of tokens") rather than an RL reward signal. This
  reinforces that Cursor's proprietary interaction data — not just its RL
  reward signal — is a core training asset shared with training partners like
  SpaceXAI/xAI.

### Claim 5: Grok 4.5's training deliberately broadened beyond coding to include high-quality STEM tasks, research papers, and other knowledge work

- **Evidence**: Direct statement of training data strategy, framed as a
  deliberate choice ("this involved drawing on") to build cross-domain
  proficiency.
- **Confidence**: anecdotal (vendor-stated training strategy; no data mixture
  ratios or ablation evidence given)
- **Quote**: "This involved drawing on high-quality STEM tasks, research
  papers, and other knowledge work, so that the model gained proficiency
  across a wide range of domains."
- **Our assessment**: This is the concrete training-side mechanism behind
  Claims 1 and 2's "more than software engineering" positioning. It is a
  direct contrast with Composer 2.5's specialist framing — that model's
  training techniques (targeted textual feedback, feature-deletion synthetic
  tasks) were all coding-specific (`blog-cursor-composer-2-5.md`). Grok 4.5
  represents a deliberate strategic choice to trade some of that
  coding-specific focus for domain breadth, consistent with the "different
  weight class" framing in Claim 10 below.

### Claim 6: RL training for Grok 4.5 used difficult problems in realistic environments spanning both software engineering and broader knowledge work

- **Evidence**: Direct statement describing the RL training scope.
- **Confidence**: anecdotal (vendor-stated training approach; mechanism
  described qualitatively, no reward function or algorithm details given)
- **Quote**: "We used reinforcement learning on difficult problems in
  realistic environments spanning both software engineering and broader
  knowledge work."
- **Our assessment**: This extends the "realistic environments" RL framing
  already established in the corpus for Composer (`blog-cursor-real-time-rl.md`,
  `blog-cursor-composer2-technical-report.md` Claim 2: "RL training uses
  realistic Cursor sessions with the same tools and harness the deployed model
  uses") to non-coding domains. The corpus previously had no evidence that
  Cursor's realistic-environment RL methodology was portable outside
  software engineering; this is the first such claim.

### Claim 7: A distributed agent system was built to construct difficult RL training environments at scale, with engineers specifying problems and verification methods and large groups of agents building, testing, and refining each environment

- **Evidence**: Direct mechanism description of the environment-construction
  pipeline, with named roles (engineers specify, agents construct/test/refine).
- **Confidence**: emerging (first-party mechanism description; specific enough
  to be technically coherent as an infrastructure claim, though no scale
  metrics — number of environments, number of agents, wall-clock time — are
  given)
- **Quote**: "We developed a distributed agent system to construct these
  environments at scale."
- **Quote**: "Engineers specify a problem and how a solution is verified, and
  large groups of agents construct, test, and refine each environment."
- **Our assessment**: This is the most novel infrastructure claim in the post
  and a natural extension of the corpus's existing synthetic-task-generation
  material. It is structurally similar to the "feature deletion" synthetic
  task recipe in `blog-cursor-composer-2-5.md` Claim 6 (verifiable-reward
  tasks generated at scale), but generalizes the pattern: instead of one fixed
  recipe (delete-and-reimplement), engineers now specify arbitrary
  problem/verification pairs and delegate the environment-construction work
  itself to agents. This is agents-building-agent-training-environments — a
  meta-level application of agentic labor to RL infrastructure that is new to
  the corpus.

### Claim 8: Many of the RL training problems had to be designed to be difficult enough that even frontier models fail at them

- **Evidence**: Direct statement about problem difficulty calibration.
- **Confidence**: anecdotal (vendor-stated design goal; no specific frontier
  models named as having failed, no failure rate given)
- **Quote**: "Many of these problems had to be designed to be difficult enough
  that even frontier models fail at them."
- **Our assessment**: This is a difficulty-calibration claim consistent with
  the broader industry pattern (also seen in `blog-cursor-cursorbench.md`'s
  discussion of benchmark saturation at the frontier) that current-generation
  eval and training tasks must be deliberately hard to produce a useful
  training/differentiation signal at all. No specifics are given about how
  "frontier model failure" was verified (which models, what failure rate), so
  this should be treated as a design intention rather than a measured result.

### Claim 9: Grok 4.5 has a disclosed, unquantified advantage on CursorBench because an earlier snapshot of the Cursor codebase was accidentally included in its training data

- **Evidence**: Direct, self-disclosed admission of a contamination incident,
  including an explicit statement that the impact is not fully known and that
  the offending data has been excluded going forward.
- **Confidence**: settled (this is a first-party factual disclosure of a
  specific, named incident — not a projection or aspiration)
- **Quote**: "Grok 4.5 has an advantage on CursorBench because an earlier
  snapshot of the Cursor codebase was accidentally included in training. The
  exact impact is unclear. That data has been removed for future models."
- **Our assessment**: This is the single highest-value claim in the post for
  guide purposes. It directly undercuts the "internal codebase sourcing is
  structurally contamination-proof" argument made in
  `blog-cursor-cursorbench.md` Claim 3 — see Cross-References below and filed
  contradiction #1724. The disclosure is commendably candid (Cursor did not
  have to publish this), which raises confidence that the admission itself is
  accurate, even though "the exact impact is unclear" means the magnitude of
  CursorBench score inflation for Grok 4.5 cannot be determined from this
  source. Any future guide citation of Grok 4.5's CursorBench performance
  should carry this contamination caveat.

### Claim 10: Grok 4.5 and Composer 2.5 are positioned as two different model weight classes that Cursor will continue to support side by side, not as a replacement

- **Evidence**: Direct positioning statement distinguishing the two models.
- **Confidence**: settled (explicit vendor product-positioning statement)
- **Quote**: "Grok 4.5 and Composer 2.5 are two different model weight
  classes, and we're excited to support both sizes and weights."
- **Our assessment**: This is an important corrective to any assumption that
  Grok 4.5 supersedes or deprecates Composer 2.5 — Cursor explicitly frames
  this as a dual-track product strategy (a specialist, smaller, cheaper coding
  model in Composer 2.5, and a larger, more general, more expensive model in
  Grok 4.5) rather than a generational replacement. This tempers the "shift
  from specialist to generalist" framing that a purely surface-level reading
  of the release might suggest.

### Claim 11: Grok 4.5 is available at launch across desktop, web, iOS, CLI, and Cursor's SDK

- **Evidence**: Direct platform availability statement.
- **Confidence**: settled (stated availability at time of publication)
- **Quote**: "Grok 4.5 is available today in Cursor across desktop, web, iOS,
  CLI, and our SDK."
- **Our assessment**: Simultaneous availability across five surfaces at
  launch (including the relatively new iOS mobile surface documented in
  `blog-cursor-ios-mobile-app.md`) indicates Grok 4.5 was integrated into
  Cursor's full existing product surface rather than launched as a
  desktop/web-only preview. No qualitative detail is given about
  surface-specific behavior differences.

### Claim 12: Grok 4.5 pricing is $2/M input and $6/M output tokens for the base model, and $4/M input and $18/M output tokens for a fast variant

- **Evidence**: Explicit stated pricing for both variants.
- **Confidence**: settled (stated pricing at launch; subject to change)
- **Quote**: "The base model is priced at $2/M input tokens and $6/M output
  tokens. There is also a fast variant at $4/M input tokens and $18/M output
  tokens."
- **Our assessment**: Grok 4.5's base tier ($2/$6) is substantially more
  expensive than Composer 2.5's standard tier ($0.50/$2.50, per
  `blog-cursor-composer-2-5.md` Claim 11) — roughly 4x on input and 2.4x on
  output. The fast variant ($4/$18) is comparatively closer to Composer 2.5's
  fast tier ($3.00/$15.00) but still higher on both axes. This pricing gap is
  consistent with Claim 10's "different weight class" framing: Grok 4.5 is
  priced as the larger, more capable, more expensive option, with Composer 2.5
  remaining the cheaper specialist. For practitioners doing cost modeling,
  this is the first Grok-4.5-specific pricing reference point in the corpus.

### Claim 13: Cursor added new safeguards reflecting Grok 4.5's cybersecurity capabilities, and offers double usage for the first week on individual and team plans

- **Evidence**: Direct statements about safety measures and a launch
  promotion.
- **Confidence**: settled (stated launch-time facts)
- **Quote**: "We've also added new safeguards reflecting the model's
  cybersecurity capabilities."
- **Quote**: "Cursor subscription plans for individuals and teams include
  significant usage of the model with double usage for the first week."
- **Our assessment**: The cybersecurity-safeguards statement is notable but
  unspecific — no detail is given about what capability increase prompted the
  safeguards or what the safeguards consist of (rate limits, use-case
  restrictions, monitoring, etc.). This is a claim to flag for follow-up
  rather than one that can be acted on directly; the guide should note that
  Cursor itself considers Grok 4.5's cybersecurity-relevant capability
  increase significant enough to warrant new safeguards, without being able
  to specify what those safeguards are from this source.

## Concrete Artifacts

```
# Grok 4.5 Launch Facts (Cursor / SpaceXAI, July 8, 2026)
# Source: https://cursor.com/blog/grok-4-5

ARCHITECTURE
  Type: Mixture-of-experts
  Co-developed with: SpaceXAI
  Parameter count: not disclosed in this source

TRAINING DATA
  Volume: "trillions of tokens" of Cursor data (user interactions with
          codebases and software tools)
  Composition: broadened beyond coding — STEM tasks, research papers,
               other knowledge work

RL TRAINING
  Environments: realistic, spanning software engineering + broader
                knowledge work
  Construction: distributed agent system — engineers specify problem +
                verification method, "large groups of agents construct,
                test, and refine each environment"
  Difficulty target: hard enough that "even frontier models fail at them"

DISCLOSED CONTAMINATION INCIDENT
  Cause: earlier snapshot of the Cursor codebase accidentally included
         in training
  Effect: "advantage on CursorBench" — "exact impact is unclear"
  Remediation: contaminating data "removed for future models"

PRODUCT POSITIONING
  Relationship to Composer 2.5: "two different model weight classes";
    both continue to be supported, not a replacement

AVAILABILITY (at launch)
  Surfaces: desktop, web, iOS, CLI, SDK

PRICING
  Base:  $2/M input tokens,  $6/M output tokens
  Fast:  $4/M input tokens, $18/M output tokens
  Promo: double usage, first week, individual + team plans

SAFETY
  "New safeguards reflecting the model's cybersecurity capabilities"
  (unspecified in source)
```

## Cross-References

- **Corroborates**: `blog-cursor-composer2-technical-report.md` Claim 1 —
  Composer 2's base model, Kimi K2.5, is "a 1.04 trillion parameter
  mixture-of-experts model with 32 billion active parameters." Grok 4.5's
  Claim 3 here (mixture-of-experts architecture) confirms MoE as the
  consistent architecture pattern Cursor has used across both the
  Composer/Kimi lineage and the new SpaceXAI/Grok lineage for large,
  coding-capable models — though the two are separately trained systems, not
  variants of the same base.

- **Extends**: `blog-cursor-composer-2-5.md` Claim 10 — that post announced
  "training a significantly larger model from scratch, using 10x more total
  compute" with SpaceXAI on Colossus 2, timeline undisclosed. This post
  (published ~7 weeks later) is the concrete product delivery of that
  announcement: Grok 4.5, a joint Cursor/SpaceXAI model. This closes the loop
  on a previously forward-looking, unverified claim in the corpus.

- **Extends**: `blog-cursor-real-time-rl.md` Claims 1 and 2 (real production
  interaction data as RL signal, "billions of tokens") — Claim 4 here shows
  the same class of Cursor interaction data being used at "trillions of
  tokens" scale for base/pretraining of a partner-trained model, not just as
  an RL reward signal for Cursor's own Composer line. This is a broader
  application of the same proprietary-data asset than previously documented.

- **Extends**: `blog-cursor-composer-2-5.md` Claim 5 ("Feature deletion"
  synthetic task generation with verifiable rewards, built by engineers
  defining a task template) — Claim 7 here generalizes this pattern: rather
  than one fixed recipe, engineers now specify arbitrary problem/verification
  pairs and agents themselves construct, test, and refine the resulting
  environments at scale. This is a meaningful infrastructure evolution: agentic
  labor applied to RL-environment construction itself, not just to solving
  tasks within a fixed environment type.

- **Contradicts** (filed as issue #1724, `needs-resolution`): `blog-cursor-cursorbench.md`
  Claim 3 states that sourcing CursorBench tasks from Cursor's own internal
  codebase (via "Cursor Blame") "solves the benchmark-contamination problem
  structurally: the tasks come from internal codebases and real sessions, not
  from public GitHub repositories in training data." Claim 9 in this note
  directly documents a case where that same internal, non-public Cursor
  codebase was "accidentally included" in a partner model's (Grok 4.5's)
  training data anyway — not via public scraping, but via the close
  Cursor/SpaceXAI training partnership. Both claims cannot stand unqualified:
  either internal-codebase sourcing is a structural fix for contamination, or
  it isn't once the eval designer and a model vendor share a training data
  pipeline. See contradiction issue #1724 for the full framing; no verdict is
  asserted here.

- **Novel**: Compared to the existing corpus:
  - **Distributed agent system for RL environment construction** (Claim 7):
    no other source describes agents themselves being used to build, test,
    and refine RL training environments at scale, as opposed to solving tasks
    within pre-built environments.
  - **Cross-domain training data broadening for a Cursor-affiliated model**
    (Claim 5): the corpus's prior Cursor model posts (Composer 2, Composer
    2.5) describe exclusively coding-focused training data and technique
    design. This is the first source describing a deliberate strategic shift
    to non-coding domains (STEM, research papers, finance, legal) for a
    Cursor-distributed model.
  - **Self-disclosed benchmark contamination incident** (Claim 9): no other
    source in the corpus documents a vendor voluntarily disclosing that its
    own flagship eval (CursorBench) was contaminated by an accidental data
    inclusion, with an explicit "impact is unclear" admission.
  - **Dual-weight-class product strategy** (Claim 10): the explicit framing of
    two co-existing model tiers ("weight classes") from the same vendor,
    rather than a generational replacement, is new positioning language in the
    corpus.

## Guide Impact

- **Chapter 03 (Benchmark Selection / Evaluation Architecture)**: Claim 9 (the
  disclosed CursorBench contamination incident) should update any guide
  section that cites `blog-cursor-cursorbench.md`'s "internal codebase
  sourcing avoids contamination" claim. Recommend adding a caveat: internal,
  non-public codebases used as eval-source material are not automatically
  immune to contamination — they can still leak into a partner or vendor's
  training corpus through data-sharing relationships (e.g., joint training
  partnerships), which is a distinct vector from the public-GitHub-scraping
  contamination that internal sourcing does prevent. Track contradiction
  issue #1724 for the resolved guidance once a verdict is reached.

- **Chapter 02 (Harness Engineering — synthetic/RL environment construction)**:
  Claim 7 (distributed agent system building RL environments: engineers
  specify problem + verification, agents construct/test/refine) should be
  added alongside the existing feature-deletion synthetic task recipe
  (`blog-cursor-composer-2-5.md` Claim 6) as a second, more general pattern
  for scaling RL training environment construction. Specific recommendation:
  teams building RL training pipelines for agents should consider using
  agents themselves to construct and validate training environments, not just
  to solve tasks within them — this is a meta-level scaling technique with
  only qualitative description available so far (no metrics on agent-hours,
  environment yield rate, or quality of agent-constructed environments).

- **Chapter 05 (Team Adoption — model selection / competitive landscape)**:
  Claim 1, 2, 5, and 10 together mark Grok 4.5 as the first Cursor-affiliated
  model explicitly positioned for non-coding professional work (data science,
  finance, legal). Recommend noting this as a competitive-landscape signal:
  teams evaluating AI tooling for non-engineering knowledge work should be
  aware that coding-agent vendors are now training models with explicit
  cross-domain ambitions, not staying in a narrow coding lane. Claim 12
  (pricing: base $2/$6, fast $4/$18) should be logged as the current
  reference point for cost modeling, alongside Composer 2.5's cheaper
  specialist pricing, with the note that the two are marketed as different
  "weight classes" (Claim 10) rather than a strict upgrade path.

- **Chapter 04 (Economics, Governance, Supply Chain)**: Claim 4 and Claim 9
  together are relevant to the supply-chain risk framing already established
  in `blog-simonwillison-xai-anthropic-datacenter.md` (Cursor/SpaceXAI's own
  training-data sharing with xAI is exactly the kind of close infrastructure
  partnership that source flags as a risk vector, albeit for a different
  concern — compute governance rather than eval contamination). Recommend
  cross-linking: organizations should consider that deep training partnerships
  between an AI vendor and its infrastructure/model partner can produce
  unexpected data-sharing side effects (here, eval contamination) beyond the
  compute-governance risks already documented for the Cursor/SpaceXAI/xAI
  relationship.

## Extraction Notes

- The post is a short product/model launch announcement (comparable in length
  and style to `blog-cursor-composer-2-5.md`), not a technical report. No
  named individual authors; attributed only to "Cursor Team." No sub-pages
  were linked from the post that appeared substantive enough to follow — the
  post references a benchmark comparison chart but it is rendered as an image
  and its numeric content could not be extracted via WebFetch.
- All direct quotes in this note were confirmed via multiple targeted
  WebFetch requests against the source URL, each explicitly asking for
  verbatim text rather than a summary, per MINER.md §2a. No quote was
  constructed by paraphrasing a summarized version of the post.
- No specific benchmark scores, percentages, or model-vs-model numeric
  comparisons are available in the extractable page text. Any future
  quantitative comparison of Grok 4.5 to other frontier models must be sourced
  from the (unextracted) chart image or from independent third-party
  benchmarking, not from this source.
- No information is given in this source about agentic task duration limits,
  context window size, or the RL algorithm used (PPO, GRPO, etc.) — these
  remain open questions for future sources.
- One contradiction was identified and filed as issue #1724 (see
  Cross-References → Contradicts). No verdict is asserted in this note per
  MINER.md §4a; the verdict is left for human/Smith resolution and will be
  logged in CONTRADICTIONS.md as C-NNN once resolved.
- Confidence overall is set to `anecdotal`: the majority of the post's
  substantive claims (capability scope, training data composition, RL
  methodology, difficulty calibration) are qualitative vendor statements
  without independent verification or numeric evidence. The pricing,
  availability, and contamination-disclosure claims are individually more
  solid (`settled`), but they do not carry the bulk of the post's guide-
  relevant content, so the overall confidence reflects the weaker majority.
