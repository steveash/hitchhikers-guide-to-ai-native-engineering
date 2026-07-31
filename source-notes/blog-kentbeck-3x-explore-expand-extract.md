---
source_url: https://newsletter.kentbeck.com/p/canon-3x-exploreexpandextract
source_type: blog-post
title: "Canon 3X: Explore/Expand/Extract"
author: Kent Beck
date_published: 2026-07-30
date_extracted: 2026-07-31
last_checked: 2026-07-31
status: current
confidence_overall: emerging
issue: "#2360"
---

# Canon 3X: Explore/Expand/Extract (Kent Beck)

> Kent Beck's canonical explanation of "3X" — a three-phase model (Explore,
> Expand, Extract) for how a product/growth-loop idea matures along an
> S-curve, with the central thesis that applying the approach appropriate to
> one phase to an idea that is actually in a different phase kills the idea.
> The post names nine business dimensions that should differ by phase but
> only elaborates one compact tactical one-liner per phase, not per-dimension
> detail. The post does not mention AI, AI agents, or AI-native development
> anywhere.

## Source Context

- **Type**: blog-post (Kent Beck's newsletter, `newsletter.kentbeck.com`,
  published 2026-07-30, filed via the `kent-beck` trusted RSS feed). Labeled
  by Beck as a "Canon" post — part of a series positioned as his systematic,
  from-first-principles explanation of a named idea, rather than a one-off
  reflection or announcement.
- **Author credibility**: Kent Beck is the creator of Extreme Programming
  (XP) and Test-Driven Development (TDD), and a co-author of the Agile
  Manifesto — see `blog-kentbeck-trust-factory.md` and
  `blog-kentbeck-yagni-economics.md` for his broader corpus presence. This
  post is Beck presenting his own named framework, not a third-party report.
- **Scope**: Covers the S-curve/logistic-growth framing for product
  maturation, the "emergence" mechanism (two competing feedback loops) that
  produces that curve, the core thesis that phase-mismatched approaches kill
  ideas, and one-line tactical summaries for the Explore, Expand, and Extract
  phases (goal, risk, and tactics for each). Names nine dimensions —
  finance, team size, project management, personnel, technology, risk
  management, implementation, marketing, sales — as varying by phase, but
  does **not** work through most of those dimensions individually per phase;
  only the compact "tiny teams, no dependencies, quickly discard failures" /
  "throttle growth, discard non-essential features, good-enough-for-now
  scaling" / "small, safe experiments; roll out successes; optimize costs"
  one-liners are given. Does NOT cover: AI, AI agents, or AI-assisted
  development in any form; no company examples, case studies, or numeric
  metrics are given anywhere in the piece; the article is entirely
  conceptual/theoretical.

## Extracted Claims

### Claim 1: Product/idea growth follows an S-shaped (logistic) curve whose apparent smoothness is a "dangerous illusion" — the beginning, middle, and final portions of the curve require completely different approaches despite looking like one continuous process
- **Evidence**: Beck's own framing device, presented as the article's opening argument, in the "The growth of anything forms a logistic curve" section.
- **Confidence**: emerging (a stated organizing principle from a credible author, not independently measured, but consistent with — and foundational to — his own later phase breakdown)
- **Quote**: "The smoothness of this curve is a dangerous illusion. The beginning, middle, and final portions of this curve require completely different approaches."
- **Our assessment**: This is the article's load-bearing premise — everything downstream (the three named phases, the "kills ideas" thesis) depends on accepting that a single visually-continuous growth curve actually masks several qualitatively different regimes that call for different behavior.

### Claim 2: The S-curve is produced by two competing feedback loops — a reinforcing loop that drives early growth, and an inhibiting loop that later takes over and caps it — and the phase transitions in 3X correspond to where control shifts from one loop to the other
- **Evidence**: Beck's own mechanistic explanation, in the "Emergence" section, of why growth curves take an S shape rather than growing unboundedly.
- **Confidence**: emerging (a systems-dynamics framing applied by Beck to product growth; internally coherent but not empirically demonstrated in this piece for the software-product case specifically)
- **Quote**: "To create the S curve, first you get the reinforcing loop on the left operating...Then later you get the inhibiting loop on the right taking over."
- **Our assessment**: This gives 3X a causal mechanism rather than leaving the three phases as an arbitrary taxonomy — the phase you're in is defined by which of the two loops currently dominates, which is a more falsifiable framing than a purely descriptive lifecycle-stage label.

### Claim 3: Applying the approach appropriate to one phase (Explore, Expand, or Extract) to an idea that is actually in a different phase kills the idea — this is presented as the article's central thesis, stated as a flat declarative rule rather than illustrated with a specific example
- **Evidence**: Beck's own stated thesis in the "3X's" section, given as the transition point before he details each phase separately.
- **Confidence**: emerging (a sharp, quotable diagnostic claim from a foundational practitioner, presented as a general rule; not illustrated with a concrete case study or measured in this piece)
- **Quote**: "Applying the approach from one phase to an idea in another phase kills ideas."
- **Our assessment**: This is the most portable, guide-relevant claim in the source — a general warning against exporting a single "how we do things" playbook across an organization regardless of which lifecycle stage a given initiative is actually in. Notably thin on evidence: no specific historical example of an idea being "killed" this way is given anywhere in the accessible text.

### Claim 4: The Explore phase's goal is to find a new growth loop through rapid, unpredictable experimentation; its risk is that nobody cares; its tactics are tiny teams, no dependencies, and quickly discarding failures
- **Evidence**: Beck's own phase-by-phase breakdown in the "Explore" section.
- **Confidence**: settled (first-party statement of what the Explore phase is, within Beck's own framework — not an empirical claim requiring outside verification)
- **Quote**: "Find the growth loop. You can't predict a new loop so you have to find it experimentally."
- **Quote (tactics)**: "Tiny teams, no dependencies, quickly discard failures."
- **Our assessment**: The "you can't predict a new loop so you have to find it experimentally" framing is a direct argument against heavyweight upfront planning specifically for Explore-phase work — a scoped, phase-conditional claim rather than a blanket anti-planning stance (contrast with Expand and Extract below, which do prescribe more deliberate throttling and optimization).

### Claim 5: The Expand phase's goal is to scale the already-validated growth loop while avoiding fatal bottlenecks; its risk is failure to scale; its tactics are throttling growth, discarding non-essential features, and "good-enough-for-now" scaling; the phase ends once cause-and-effect relationships become predictable
- **Evidence**: Beck's own phase-by-phase breakdown in the "Expand" section.
- **Confidence**: settled (first-party statement of what the Expand phase is, within Beck's own framework)
- **Quote**: "Avoid fatal obstacles while scaling furiously."
- **Quote (tactics)**: "Throttle growth, discard non-essential features, good-enough-for-now scaling."
- **Our assessment**: The "throttle growth" tactic is a counterintuitive addition worth flagging — Beck's model treats deliberately slowing or capping growth as an active Expand-phase tactic rather than something to avoid, framed as necessary to keep bottlenecks from becoming fatal.

### Claim 6: The Extract phase's goal is to optimize profitability as growth slows; its risk is unsustainability; its tactics are small, safe experiments, rolling out what succeeds, and optimizing costs
- **Evidence**: Beck's own phase-by-phase breakdown in the "Extract" section.
- **Confidence**: settled (first-party statement of what the Extract phase is, within Beck's own framework)
- **Quote**: "Growth with profit."
- **Quote (tactics)**: "Small, safe experiments; roll out successes; optimize costs."
- **Our assessment**: This is the phase where Beck's tactics most resemble conventional "mature product" management advice (cost optimization, incremental safe experimentation) — the framework's distinctive content is concentrated in the Explore/Expand phase definitions rather than here.

### Claim 7: Extract-phase products are the funding source for a portfolio of Explore-phase projects — mature, profitable products underwrite new experimentation elsewhere in the same organization
- **Evidence**: Beck's own statement in the "Extract" section, connecting the Extract phase's profit-optimization goal back to the Explore phase's need for resourcing.
- **Confidence**: emerging (a structural/financial claim about how organizations should relate mature and nascent product lines, asserted rather than demonstrated with a specific company's numbers)
- **Quote**: "You have some Extract products that pay the bills & pay for a portfolio of Explore projects."
- **Our assessment**: This is the one place the three phases are explicitly tied together as a simultaneous portfolio (rather than a single idea's sequential journey through the phases) — implying an organization runs Explore, Expand, and Extract work concurrently across different initiatives, not that a single company or team occupies one phase at a time.

### Claim 8: The article names nine dimensions that should differ by phase — finance, team size, project management, personnel, technology, risk management, implementation, marketing, sales — but the accessible text only elaborates a single compact tactical one-liner per phase, not per-dimension detail across those nine categories
- **Evidence**: Beck's own list, given in the "All Of The Above" section, cross-checked against the actual level of detail provided per phase throughout the rest of the piece.
- **Confidence**: settled (a direct observation about what content is and isn't present in the accessible text, not a claim requiring outside verification)
- **Quote**: (no single contiguous quote; the nine dimensions appear in the
  source as nine separate bullet items, reproduced individually in Concrete
  Artifacts → "Nine dimensions named as phase-dependent" below)
- **Our assessment**: This matters for calibrating this source's guide impact. The Prospector's triage comments anticipated "concrete changes to finance, team structure, project management, personnel, technology, and risk approach" broken out per phase — on a full read, the article names these nine dimensions as varying by phase but does not work through most of them individually; only the phase-level tactical one-liners (Claims 4-6) are actually given. A guide citation of this source for detailed per-dimension guidance (e.g., "here's specifically how personnel decisions should differ in Explore vs. Expand") would be citing content that isn't present in this piece.

### Claim 9: The article closes with a pivot from the 3X framework itself to a diagnostic claim about organizational failure generally — "most teams don't have a strategy problem, they have an adaptation problem" — positioned immediately before a call-to-action for Beck's own consulting/advisory services, in a block not explicitly labeled as sponsored or promotional
- **Evidence**: Text appearing after a horizontal-rule divider following the "All Of The Above" section, immediately preceding a paragraph soliciting inquiries about "custom talks and advisory engagements."
- **Confidence**: anecdotal (an aphoristic closing claim, not elaborated or connected back to the 3X framework with a specific mechanism, and positioned adjacent to promotional content — see Extraction Notes)
- **Quote**: "Most teams don't have a strategy problem. They have an adaptation problem."
- **Quote**: "Your plan was never going to survive contact with reality."
- **Our assessment**: Treat this claim with more caution than Claims 1-8. It is not explicitly marked "sponsored" the way the promotional block in `blog-kentbeck-xp-long-volatility.md` was, but it sits in the same structural position (after a divider, immediately before a paid-services pitch) as that post's disclosed sponsored insert. It reads as a plausible generalization of the "phase-mismatch kills ideas" thesis (an org failing to adapt its approach as it moves between phases = an adaptation problem, not a strategy problem) but Beck does not explicitly draw that connection himself in the accessible text.

## Concrete Artifacts

### The three phases, as stated (verbatim goal / risk / tactics, condensed)

```
Source: Kent Beck, "Canon 3X: Explore/Expand/Extract",
newsletter.kentbeck.com, 2026-07-30

Explore
  Goal:    Find the growth loop. You can't predict a new loop so you have
           to find it experimentally.
  Tactics: Tiny teams, no dependencies, quickly discard failures.

Expand
  Goal:    Avoid fatal obstacles while scaling furiously.
  Tactics: Throttle growth, discard non-essential features,
           good-enough-for-now scaling.

Extract
  Goal:    Growth with profit.
  Tactics: Small, safe experiments; roll out successes; optimize costs.
```

### Nine dimensions named as phase-dependent (verbatim list)

```
Source: Kent Beck, "Canon 3X: Explore/Expand/Extract",
newsletter.kentbeck.com, 2026-07-30, "All Of The Above" section
(reproduced as nine separate bullet items, matching the source's structure;
these are not a single running sentence in the original)

  - Finance
  - Team size
  - Project management
  - Personnel
  - Technology
  - Risk management
  - Implementation
  - Marketing
  - Sales
```

## Cross-References

- **Extends**: `blog-kentbeck-xp-long-volatility.md` Claim 3 (Beck names "3X:
  Explore/Expand/Extract" as one of several ideas that recently finished
  "baking," listed without elaboration: "Here are some recent examples: 3X:
  Explore/Expand/Extract 'Genie' as a metaphor for LLMs Thinkies") and Claim 5
  (Beck describes explaining 3X roughly 20 times over two weeks while
  teaching in Africa, with his friend Nadayar Enegesi observing that no two
  explanations were the same). That note recorded "3X" only as an unglossed
  term in a list; this note supplies Beck's own first-party definition of
  what the framework actually claims, confirming it is the same idea that
  note flagged as named-but-not-explained. (Note that the corpus already had
  a glossed definition of 3X from a different, third-party source — see
  **Corroborates** below — so this note is not the corpus's first content on
  the framework, only its first first-party and most granular one.)
- **Extends**: `blog-kentbeck-yagni-economics.md` Claim 8 ("YAGNI is... 'a
  meditation on timing,' and building structure too soon is as risky as
  building it too late"). Both sources are Beck arguing that the same action
  (building structure; applying a given operational approach) is correct or
  incorrect depending on *when*/*which phase* it happens — YAGNI's timing
  argument operates at the level of a single codebase's structural decisions,
  while 3X's phase-mismatch thesis (Claim 3 above) operates one level up, at
  the level of an entire idea's or product's organizational treatment. Beck
  does not connect the two explicitly in either piece, but they are the same
  underlying "timing/context determines correctness" move applied at
  different altitudes.
- **Corroborates**: `blog-pragmaticengineer-orosz-kentbeck-career.md` Claim 3
  ("Software product development has three phases — explore, expand, extract
  — and how an engineer should code, how a company should hire, and how a
  team should organize differs across each phase"). That note is **independent
  third-party testimony** for the same framework: Gergely Orosz's write-up of
  a Beck interview, quoting "Building software products has three phases:
  explore, expand, extract... This is Kent's '3X' model. 'Explore' means
  trying many cheap uncorrelated experiments, 'expand' involves focusing on
  the one thing that's working and overcoming obstacle after obstacle, while
  'extract' is a repeatable playbook and economies of scale. How you code,
  hire, and organize differs across each phase." Two things follow:
  - That note's closing sentence — "How you code, hire, and organize differs
    across each phase" — directly anticipates this note's **Claim 8** (the
    nine named phase-dependent dimensions, three of which are exactly
    implementation, personnel/team size, and project management). The
    phase-dependent-practice thesis is therefore attested twice, in two
    venues, in two different framings (Beck's own newsletter here; a
    third-party interview write-up there), which raises confidence that it
    is Beck's settled model rather than one essay's framing choice.
  - That note's Novel section (line 176) asserts the 3X framework is "not
    present anywhere else in the corpus" **as of its writing**. This note is
    the corpus update that assertion was waiting for; the two notes should
    be read together, and that assertion should now be treated as
    superseded rather than current.
  Where the two diverge: Orosz's gloss defines each phase by its
  characteristic activity ("many cheap uncorrelated experiments" / "focusing
  on the one thing that's working" / "a repeatable playbook and economies of
  scale"), while this source adds the goal/risk/tactics breakdown (Claims
  4-6), the S-curve and two-feedback-loop mechanism (Claims 1-2), and the
  Extract-funds-Explore portfolio structure (Claim 7). Neither gloss
  contradicts the other; this one is strictly more granular.
- **Corroborates**: No *other* existing kentbeck note corroborates the
  specific 3X phase mechanics (goal/risk/tactics per phase) — within Beck's
  own corpus presence here, this is the first statement of them.
- **Contradicts**: None identified. This source does not address AI-agent
  development at all, so it does not conflict with the corpus's existing
  AI-specific claims (e.g., `blog-kentbeck-trust-factory.md`'s "single
  player" genie-erosion diagnosis); it operates at the level of general
  product/idea lifecycle management, which is a different, non-conflicting
  layer.
- **Novel** (stated relative to the corpus's *existing* 3X coverage — the
  unglossed mention in `blog-kentbeck-xp-long-volatility.md` Claim 3 and the
  glossed third-party definition in
  `blog-pragmaticengineer-orosz-kentbeck-career.md` Claim 3 — not as though
  the framework were absent from the corpus before now):
  - **The per-phase goal / risk / tactics breakdown (Claims 4-6)**: Orosz's
    note already glossed what each phase *is* (the characteristic activity),
    but not what each phase's *goal* is, what *risk* defines it, or which
    *tactics* Beck prescribes for it. The specific tactical one-liners
    ("Tiny teams, no dependencies, quickly discard failures"; "Throttle
    growth..."; "Small, safe experiments; roll out successes; optimize
    costs") are new to the corpus, and "throttle growth" as a deliberate
    Expand-phase tactic is the most counterintuitive of them.
  - **The logistic-curve/emergence mechanism (Claims 1-2)**: a systems-
    dynamics explanation (reinforcing vs. inhibiting feedback loops) for why
    product growth takes an S-shape, not present elsewhere in the corpus.
    This is the biggest genuine addition: it supplies a *transition
    criterion* (which loop currently dominates) that the Orosz gloss lacks —
    that note explicitly records "no phase durations, transition criteria,
    or case study are given."
  - **The phase-mismatch-kills-ideas thesis (Claim 3)**: a general
    organizational-diagnosis claim not present in this specific form
    elsewhere in the corpus. Orosz's note reports that practice *differs*
    by phase; only this source states the sharp negative consequence of
    getting the phase wrong.
  - **The Extract-funds-Explore portfolio claim (Claim 7)**: a specific
    financial-structure claim about how organizations should relate mature
    and nascent initiatives, novel to the corpus.

## Guide Impact

- **Placement: consolidate with `blog-pragmaticengineer-orosz-kentbeck-career.md`
  before drafting.** That note's Guide Impact already recommends introducing
  3X by name in "Chapter 03 (Product/Team Lifecycle) or wherever
  phase-dependent practice guidance lives," for harness rigor, review
  discipline, hiring profile, and process formality. This note recommends
  **Chapter 05 (Team Adoption)**. These are the same framework, and a Smith
  drafting from the two notes independently would produce duplicated or
  fragmented 3X guidance. The two should be consolidated into a **single
  chapter decision, drafted once, citing both notes**. My argument for
  Chapter 05 over Chapter 03:
  - There is no "Chapter 03 (Product/Team Lifecycle)" in the guide.
    `guide/03-verification.md` is **Verification** ("The bottleneck is no
    longer generation. It is verification."), which is not where
    phase-dependent practice guidance lives. The Orosz note's own hedge —
    "or wherever phase-dependent practice guidance lives" — is the operative
    clause, and that place is Chapter 05, which already carries the guide's
    only phase-staged rollout framework (see the next bullet).
  - Of the four things the Orosz note wants varied by phase, three (review
    discipline, hiring profile, process formality) are team-adoption
    concerns; only harness rigor points at Chapter 02, and it points there
    as a cross-reference rather than as a home for the framework's
    introduction.
  - **Caveat the Smith must respect**: per Claim 8 of this note, neither
    source actually supplies per-dimension detail. Orosz's note states that
    coding/hiring/organizing differ by phase; this note names nine
    dimensions. Neither works through what, concretely, a hiring or review
    decision should look like in Explore vs. Expand. The consolidated guide
    text should introduce 3X as a *question to ask first*, not as a table of
    per-phase prescriptions, because no source in the corpus supports the
    latter.
- **Chapter 05 (Team Adoption)**: The phase-mismatch
  thesis (Claim 3) is directly usable as a named caution for AI-native
  adoption specifically: a team that adopts one AI-tooling/process posture
  (e.g., the "tiny teams, no dependencies, quickly discard failures" posture
  appropriate to an Explore-phase pilot) and then keeps that same posture
  once the effort has moved into an Expand-phase rollout is, by this
  framework, applying a phase-mismatched approach. Recommend citing Claims
  3-6 together as a structural check: before recommending a specific
  AI-adoption practice (pilot small vs. scale aggressively vs. optimize
  costs), the guide should first ask which of the three phases the
  team/initiative is actually in. This is a **new structural framing**, not
  a replacement for or contradiction of any existing chapter content.
- **Chapter 05 (Team Adoption) — do not conflate with the existing
  three-phase model already in that chapter**: `guide/05-team-adoption.md`
  already carries a three-phase maturity framework under the heading "Stage
  the harness rollout to match how usage matures" (Phase 1 / months 1-3,
  dominant usage refactoring-explanation-debugging; Phase 2 / months 3-9,
  feature implementation; Phase 3 / months 9+, design and planning), sourced
  from `research-anthropic-ai-transforming-work` Claim 6 plus
  `practitioner-getsentry-sentry`, and sharpened by
  `blog-cursor-better-models-ambitious-work` Claims 2-3. It is thematically
  adjacent to 3X (both are three-phase frameworks governing which practices
  are appropriate when) but the phase axes are **different**, and a Smith
  drafting from this note should keep them separate rather than merging
  them into one numbered sequence:
  - The existing guide model's axis is **usage composition over calendar
    time within one adopting team** — the phases advance because engineers
    progressively use the agent for harder task types, and the phase
    boundaries are stated in months.
  - 3X's axis is **which feedback loop currently dominates a given idea's
    growth loop** (Claims 1-2) — the phases advance (or don't) with the
    idea's growth dynamics, not with elapsed time, and per Claim 7 an
    organization runs all three concurrently across different initiatives.
  So this source **extends rather than corroborates** the existing model:
  it adds a second, orthogonal question ("which phase is this *initiative*
  in?") on top of the existing one ("how long has this *team* been
  adopting, and what are they using the agent for?"). A team can be at
  guide-Phase 3 harness maturity while running an Explore-phase AI
  initiative, and vice versa. Recommend that any guide text citing 3X
  explicitly names it as a distinct axis to avoid readers reading
  "Phase 1/2/3" and "Explore/Expand/Extract" as the same ladder.
- **Chapter 05 (Team Adoption)**: Claim 8 is a caution for the guide's own
  citation discipline, not a content recommendation — do not cite this
  source as though it provides detailed, phase-specific finance/personnel/
  technology/marketing/sales guidance; it names those dimensions but does
  not elaborate them. Any guide section wanting phase-specific personnel or
  technology guidance would need a different or future source.
- No other chapter has directly actionable content from this source at this
  time: the piece never mentions AI, AI agents, or AI-assisted development,
  so its applicability to the guide's core subject matter is entirely by
  extrapolation (mapping a general product-lifecycle framework onto
  AI-native team practices), not by the source's own stated scope.

## Extraction Notes

- WebFetch's summarizer declined to reproduce the article's full text
  verbatim, citing copyright (consistent with the pattern already noted in
  several other Kent Beck and Addy Osmani source notes in this corpus, e.g.
  `blog-addyosmani-software-factories-light-dark.md`'s Extraction Notes).
  Rather than attempting a workaround to extract the full raw text, this
  note was built from a series of narrowly-scoped fetches, each asking for a
  specific section's content and one short (under-40-word) verbatim quote
  per phase/topic. This is a more fragmentary extraction process than a
  single full-text read, but every quote above was independently confirmed
  against the source through its own targeted fetch rather than
  reconstructed from a paraphrased summary.
- The article's structure (confirmed via a dedicated structural-overview
  fetch) is: introduction → "The growth of anything forms a logistic curve"
  → "Emergence" → "3X's" → "Explore" → "Expand" → "Extract" → "All Of The
  Above" → a divider → the promotional/adaptation-problem close (Claim 9).
  This note's claims follow that order.
- Explicitly checked and confirmed absent from the accessible text: any
  mention of AI, AI agents, LLMs, or AI-assisted software development; any
  concrete company example, case study, or numeric metric. The piece is
  entirely conceptual/theoretical, unlike several other Beck posts in this
  corpus (e.g. `blog-kentbeck-smalltalk-genie.md`, which links to a shipped,
  inspectable GitHub repository).
- Claim 9's promotional-adjacent content was deliberately flagged at
  `anecdotal` confidence and given an explicit caution in its "Our
  assessment," rather than silently including it at the same confidence
  level as Claims 1-8, following the precedent set in
  `blog-kentbeck-xp-long-volatility.md`'s Extraction Notes (which excluded a
  similarly-positioned, explicitly-labeled sponsored block from its claims
  entirely). This piece's equivalent block is not explicitly labeled
  "sponsored," so it was extracted as a claim rather than excluded outright,
  but the structural similarity to that disclosed sponsored insert is called
  out here and in the claim itself so the Assayer and Smith can weigh it
  appropriately.
- No contradiction issue was filed. This source does not materially oppose
  any existing corpus source note's claim on the same topic — it introduces
  a new, non-conflicting product-lifecycle layer (see Cross-References →
  Contradicts).
- Cross-reference claim numbers were verified by re-reading the cited notes
  directly before writing: `blog-kentbeck-xp-long-volatility.md` Claim 3
  (3X named as a recently-baked idea, confirmed at that note's Claim 3
  heading) and Claim 5 (the Africa/Nadayar Enegesi 20-explanations anecdote,
  confirmed); `blog-kentbeck-yagni-economics.md` Claim 8 (YAGNI as "a
  meditation on timing," confirmed at that note's Claim 8 heading);
  `blog-pragmaticengineer-orosz-kentbeck-career.md` Claim 3 (the
  explore/expand/extract three-phase model, confirmed at that note's Claim 3
  heading, with its quote copied verbatim from that note's `Quote` field).
- **Revision (2026-07-31, post-Assayer):** the first draft of this note
  searched only `blog-kentbeck-*` filenames for prior 3X coverage and so
  missed `blog-pragmaticengineer-orosz-kentbeck-career.md`, a third-party
  interview write-up that already carried a glossed definition of the
  framework. That produced a false "first substantive extraction" /
  "corpus only had the unglossed term" framing and an empty Corroborates
  section. Corrected in this revision: the Orosz note is now logged as
  independent second-source corroboration of the phase-dependent-practice
  thesis, the Novel section is scoped against what that note already
  established, and the competing chapter placements are reconciled in Guide
  Impact. Lesson for future extractions of a named framework: search the
  corpus for the *framework's terms* ("explore expand extract", "3X"), not
  just for the author's own filenames — third-party coverage of an author's
  idea will not match an author-name file pattern.
- **Quote corrections (same revision):** two quoted passages in the first
  draft were not contiguous verbatim source text and were fixed against the
  live page. Claim 7 read "Extract products pay the bills & pay for a
  portfolio of Explore projects," dropping a word from the source's actual
  sentence, now quoted in full as "You have some Extract products that pay
  the bills & pay for a portfolio of Explore projects." Claim 8's nine
  dimensions were quoted as one comma-joined sentence, but they appear in
  the source as nine separate bullet items; the `Quote` field now says so
  explicitly and the Concrete Artifacts block reproduces them as bullets.
  All other quotes were re-confirmed present character-for-character.
- Confidence rated `emerging` overall: the phase definitions and thesis
  (Claims 1-7) are a coherent, internally consistent framework from a
  foundational practitioner, refined over years of iteration per
  `blog-kentbeck-xp-long-volatility.md`'s account of this same idea's
  incubation — but the framework is asserted rather than empirically
  validated in this piece (no case studies, no metrics, no falsification
  attempt), and Claim 9 in particular carries a promotional-adjacency
  caveat. Not rated `settled` because nothing here is externally verified
  beyond being an accurate restatement of what Beck himself states; not
  rated purely `anecdotal` because the core framework (Claims 1-8) is a
  structured, first-party theoretical model rather than a single unverified
  anecdote.
