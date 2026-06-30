---
source_url: https://martinfowler.com/fragments/2026-06-16.html
source_type: blog-post
title: "Fragments: June 16"
author: Martin Fowler (curator); contributors include Chelsea Troy, Dave Thomas, Eric Evans, Charity Majors, Simon Willison, Mike Masnick
date_published: 2026-06-16
date_extracted: 2026-06-30
last_checked: 2026-06-30
status: current
confidence_overall: emerging
issue: "#1362"
---

# Fragments: June 16 (Martin Fowler)

> A Fowler-curated fragment collection whose most novel contribution is Chelsea Troy's
> four-register framework for LLM conversation management (Exploring, Brainstorming,
> Deciding, Implementing), paired with Dave Thomas's and Eric Evans's practitioner
> validation that LLMs can enhance rather than degrade the craft of programming;
> also summarizes Charity Majors' enthusiast/skeptic analysis (already in corpus)
> and Willison's April 2026 PMF inflection (already in corpus).

## Source Context

- **Type**: blog-post (curated fragment collection — Fowler's "Fragments" series
  synthesizes external sources with brief editorial framing and linked quotes into a
  single post; each fragment is a distinct voice with its own linked source URL)
- **Author credibility**: Martin Fowler is Chief Scientist at Thoughtworks, author of
  *Refactoring* and *Patterns of Enterprise Application Architecture*, and one of the
  original Agile Manifesto signatories. His Fragments series is a high-trust, vendor-
  neutral editorial curation. The `martinfowler.com` feed is designated `trusted-feed`
  in this repository. Individual contributors (Troy, Thomas, Evans, Majors, Willison,
  Masnick) are named and their sources linked; confidence varies per claim. Chelsea Troy
  is a software engineer whose work focuses on developer practice; Dave Thomas is co-author
  of *The Pragmatic Programmer* (with Andy Hunt) — one of the most influential books in
  software craftsmanship. Eric Evans is the originator of Domain-Driven Design (the
  concept and the book). Simon Willison is the creator of Django and one of the highest-
  signal independent AI commentators (multiple prior corpus notes). Charity Majors is
  CTO of Honeycomb, an expert in reliability and engineering culture (prior corpus note).
- **Scope**: Covers six distinct fragments (June 16, 2026): Chelsea Troy's LLM
  conversation registers (from DDD Europe 2026), Dave Thomas's perspective on programming
  joy with LLMs, Eric Evans's LLM experimentation at DDD Europe, Charity Majors'
  enthusiast/skeptic analysis (previously captured), Simon Willison on April 2026 PMF
  inflection (previously captured), and Mike Masnick on internet decentralization. Does
  NOT address: specific harness configurations, context-engineering implementation details,
  or empirical measurements — this is a perspective/synthesis collection, not a how-to.
  Fowler's DDD Europe attendance gives him first-hand access to the Evans and Troy content.

## Extracted Claims

### Claim 1: Chelsea Troy identifies four distinct registers of LLM conversation that require different conversational stances

- **Evidence**: Chelsea Troy's talk at DDD Europe 2026, synthesized by Martin Fowler
  who attended the conference. The four registers are given with specific characterizations
  for each mode.
- **Confidence**: emerging (practitioner framework from a single talk; not empirically
  validated but conceptually coherent and consistent with wider practitioner knowledge
  about context management; Fowler's curatorial signal is a positive quality indicator)
- **Quote**: "She classified them in four ways:
  - Exploring: I want to understand before touching anything
  - Brainstorming: Generate options, I'll evaluate them separately
  - Deciding: I need a recommendation with a rationale, not a list
  - Implementing: The decision is made, help me build it"
- **Our assessment**: This is the most actionable framework in this source and the most
  novel addition to the corpus. The four-way classification maps directly to the different
  cognitive modes a developer uses during a feature's lifecycle: understanding first
  (Exploring), generating possibilities (Brainstorming), evaluating and committing
  (Deciding), then executing (Implementing). Each register requires a fundamentally
  different stance from the LLM — asking for options in Implementing mode leads to
  premature reconsideration; asking for decisions in Brainstorming mode short-circuits
  evaluation. The framework gives engineers a vocabulary for diagnosing prompt failures
  without knowing which is at fault.

### Claim 2: The primary framing for Chelsea Troy's registers is context-window health management — mixing registers corrupts context

- **Evidence**: Fowler's own framing of Troy's talk, which he attended.
- **Confidence**: emerging
- **Quote**: "The main thrust of her talk was managing the context window of LLMs so
  that it was kept in a healthy state. Much of what she said was familiar, but one thing
  I hadn't thought about was her thoughts about the different registers of conversations
  with LLMs. These registers are different styles of conversation we can have with The
  Genie (or indeed other humans). She classified them in four ways..."
- **Our assessment**: Fowler explicitly frames registers as a context-management tool.
  The key insight is that context accumulated in Exploring mode (open-ended, wide-ranging)
  is incompatible with Implementing mode (focused, execution-oriented). Carrying Exploring
  context into Implementing mode brings irrelevant material into the active context window,
  which degrades output quality. This is the mechanism that makes starting a fresh
  conversation when switching registers more than mere hygiene — it is a correctness
  intervention.

### Claim 3: When changing LLM conversation register, starting a new conversation with a fresh context is the recommended practice

- **Evidence**: Chelsea Troy's recommendation (same talk, reported by Fowler who attended).
- **Confidence**: emerging
- **Quote**: "Her point is that whenever I have a session with an LLM, I need to be
  conscious about which register I'm using. And should I change register, I should start
  a new conversation with a fresh context."
- **Our assessment**: This is directly actionable for engineers working across long AI-
  assisted sessions. The recommendation is more demanding than it appears: most developers
  default to continuing a single session for an entire work item, moving from initial
  exploration to implementation without resetting. Troy's claim is that this practice
  degrades output quality as the session accumulates register-mismatched context. Practical
  implication: treat conversation reset as a first-class workflow step when transitioning
  between phases of a task, not as overhead.

### Claim 4: Dave Thomas (co-author of The Pragmatic Programmer) reports that LLMs make programming more fun and cites Kent Beck's corroboration

- **Evidence**: Fowler's summary of Dave Thomas's blog post, reporting Thomas's first-
  person experience. Kent Beck is cited by Thomas as a corroborating voice ("Like Kent
  Beck and others have told me").
- **Confidence**: anecdotal (multiple named senior practitioners' first-person reports;
  convergent but not controlled)
- **Quote**: "Like Kent Beck and others have told me, programming with LLMs is more fun
  than ever. His post lists reasons why: removing drudgery, speeding up feedback loops,
  reviving long abandoned projects, and exploring new technologies."
- **Our assessment**: The source of this claim is significant beyond its content. Dave
  Thomas is one of the most influential voices in software craftsmanship — his "Pragmatic
  Programmer" framework shaped a generation of engineers' relationship to their craft.
  The convergent reports from Thomas and Kent Beck (both foundational figures in
  developer craft culture) provide a counter-narrative to the "AI threatens craftsmanship"
  position. Their framing — drudgery removal enabling craft expression — is consistent
  with the thesis that AI-native engineering is a form of craftsmanship elevation rather
  than replacement.

### Claim 5: Dave Thomas's reasons for increased programming joy with LLMs are specific and enumerable

- **Evidence**: Fowler's summary of Dave Thomas's blog post listing four reasons.
- **Confidence**: anecdotal
- **Quote**: "His post lists reasons why: removing drudgery, speeding up feedback loops,
  reviving long abandoned projects, and exploring new technologies."
- **Our assessment**: The four reasons Thomas lists are themselves meaningful. Drudgery
  removal addresses the repetitive/mechanical parts of programming that have always
  created the "boring parts" of software work. Faster feedback loops address the latency
  in the code→test→debug cycle. Reviving abandoned projects speaks to reducing activation
  energy for returning to old work. Exploring new technologies addresses learning curve
  acceleration. Together they describe AI as amplifying exactly the parts of programming
  that practitioners find most joyless, while leaving the creative and analytical parts
  (which Thomas emphasizes as his source of joy) intact or enhanced.

### Claim 6: Eric Evans (DDD originator) gave a keynote at DDD Europe 2026 on his multi-year LLM experimentation

- **Evidence**: Martin Fowler's first-hand account of attending DDD Europe 2026.
- **Confidence**: settled (Fowler was present at the conference)
- **Quote**: "The highlight of the conference was the opening keynote by Eric Evans, who
  gave a fascinating description of some of his experimentation with LLMs over the last
  couple of years."
- **Our assessment**: The claim here is primarily a pointer, not a detailed content
  extraction — Fowler notes the talk as a highlight but does not reproduce Evans' specific
  findings in this fragments post. The significance is that Evans (the most authoritative
  voice in domain-driven design) has been actively experimenting with LLMs for "the last
  couple of years" and chose DDD Europe 2026 as the venue for presenting this
  experimentation. That Evans finds LLMs worth presenting on at a DDD conference is
  itself a signal that the DDD community's engagement with AI tools is substantive.

### Claim 7: Martin Fowler predicts Domain-Driven Design will remain important and may become even more important as AI-driven programming evolves

- **Evidence**: Fowler's own commentary in this fragments post, grounded in his DDD
  Europe 2026 attendance.
- **Confidence**: emerging (Fowler is one of the most authoritative voices on DDD;
  this is his own reasoned prediction, not an empirical finding; consistent with corpus
  evidence that domain modeling skill grows in relative importance as AI handles
  syntactic/mechanical work)
- **Quote**: "With all the changes to programming due to LLMs, I suspect Domain-Driven
  Design is going to be one of those things that will continue to be useful, indeed may
  become even more important."
- **Our assessment**: Fowler's prediction is reasoning-by-elimination: as LLMs automate
  syntactic programming and boilerplate, the remaining differentiated skill is domain
  modeling — understanding the problem well enough to specify what to build. DDD is
  precisely the practice of developing rigorous vocabulary and structure for that domain
  understanding. If mechanical coding recedes as the bottleneck, domain clarity becomes
  proportionally more important. This is consistent with the corpus finding that the
  quality of context given to an LLM (domain knowledge, domain vocabulary) determines
  output quality more than prompt syntax.

### Claim 8: Simon Willison argues the April 2026 pricing changes at Anthropic and OpenAI reflect product-market fit with coding/agent products, not just IPO preparation

- **Evidence**: Willison's analysis quoted on Fowler's fragments page. This content is
  already fully documented in `blog-simonwillison-product-market-fit.md`; this claim
  records Fowler's curatorial decision to amplify it.
- **Confidence**: emerging
- **Quote**: "Why these sudden aggressive moves on pricing? Both Anthropic and OpenAI
  are planning to IPO, but I suspect there's a more important factor here: I think
  they've finally found product-market fit, with the coding/general-purpose agent
  products embodied by Claude Code/Cowork and Codex."
- **Our assessment**: The content is already captured in `blog-simonwillison-product-market-fit.md`
  (Claims 1 and 3). What is additionally notable here is that Fowler chose to include
  this in his curated fragments — amplifying Willison's PMF thesis to the Fowler/
  Thoughtworks audience represents a quality endorsement from a different trusted curator.

### Claim 9: Charity Majors' enthusiast/skeptic analysis concludes that engineering discipline — not advocacy for one side — is the path to credibility

- **Evidence**: Fowler's curation of Majors' post; this content is already fully
  documented in `blog-simonwillison-charity-majors-enthusiast-skeptic.md`.
- **Confidence**: emerging
- **Quote**: "understand the opportunity, the stakes, and the tradeoffs"
- **Our assessment**: The content of Majors' analysis is captured in
  `blog-simonwillison-charity-majors-enthusiast-skeptic.md`. What Fowler adds here is
  a specific framing: credibility accrues to those who "understand the opportunity,
  the stakes, and the tradeoffs" rather than to advocates for either position. Fowler's
  framing positions engineering discipline — not enthusiasm or skepticism — as the
  basis for team credibility in AI adoption decisions.

## Concrete Artifacts

### Chelsea Troy's Four Conversation Registers (verbatim from page)

```
Source: Chelsea Troy (DDD Europe 2026 talk), as reported by Martin Fowler
        https://martinfowler.com/fragments/2026-06-16.html

The main thrust of her talk was managing the context window of LLMs so that it
was kept in a healthy state. Much of what she said was familiar, but one thing
I hadn't thought about was her thoughts about the different registers of
conversations with LLMs. These registers are different styles of conversation
we can have with The Genie (or indeed other humans). She classified them in
four ways:

  - Exploring:     I want to understand before touching anything
  - Brainstorming: Generate options, I'll evaluate them separately
  - Deciding:      I need a recommendation with a rationale, not a list
  - Implementing:  The decision is made, help me build it

Her point is that whenever I have a session with an LLM, I need to be
conscious about which register I'm using. And should I change register,
I should start a new conversation with a fresh context.
```

### Dave Thomas on LLM Joy (verbatim from page)

```
Source: Dave Thomas (via Martin Fowler's summary)
        https://martinfowler.com/fragments/2026-06-16.html

"Like Kent Beck and others have told me, programming with LLMs is more fun
than ever. His post lists reasons why: removing drudgery, speeding up
feedback loops, reviving long abandoned projects, and exploring new technologies."
```

### Fowler on DDD's Future (verbatim from page)

```
Source: Martin Fowler
        https://martinfowler.com/fragments/2026-06-16.html

"With all the changes to programming due to LLMs, I suspect Domain-Driven
Design is going to be one of those things that will continue to be useful,
indeed may become even more important."
```

### Eric Evans at DDD Europe 2026 (verbatim from page)

```
Source: Martin Fowler (first-hand attendee)
        https://martinfowler.com/fragments/2026-06-16.html

"The highlight of the conference was the opening keynote by Eric Evans, who
gave a fascinating description of some of his experimentation with LLMs over
the last couple of years."
```

### Simon Willison on PMF and Pricing (verbatim from page)

```
Source: Simon Willison (as quoted by Martin Fowler)
        https://martinfowler.com/fragments/2026-06-16.html

"Why these sudden aggressive moves on pricing? Both Anthropic and OpenAI
are planning to IPO, but I suspect there's a more important factor here:
I think they've finally found product-market fit, with the coding/general-
purpose agent products embodied by Claude Code/Cowork and Codex."

"I think April 2026 is a new inflection point where the revenue implications
of this have started to land, to the benefit of the frontier AI labs and
with material impacts on the budgets of large companies."
```

## Cross-References

- **Corroborates**: `blog-simonwillison-charity-majors-enthusiast-skeptic.md` (Claims
  1–6): The Charity Majors content Fowler curates here (Claim 9 above) is the same
  source material fully documented there. Fowler's framing adds "engineering discipline"
  and "credibility" as the resolution path — consistent with that note's Claim 6
  (treating the tension as both leadership and engineering challenge).

- **Corroborates**: `blog-simonwillison-product-market-fit.md` (Claims 1 and 3): The
  Willison PMF and April 2026 inflection content Fowler curates (Claim 8 above) is
  the same analytical content documented in full there. The Willison note documents
  the detailed evidence; this Fowler fragments note adds Fowler's curatorial amplification.

- **Corroborates**: `blog-fowler-fragments-2026-06-02.md` (Claims 13–14 on organizational
  burden absorption): Dave Thomas's four reasons for LLM joy (Claim 5 here) — especially
  "removing drudgery" — maps to the June 2 fragments' Jamie Hurst observation that build
  costs have collapsed while alignment costs have not. Thomas describes the upside (less
  drudgery); Hurst describes the organizational consequence (output volume expectations
  fill the reclaimed capacity). Together they complete the picture.

- **Extends**: `blog-fowler-fragments-2026-06-02.md` (Claims 11–12 on the GIL-of-human-
  attention): Chelsea Troy's registers framework (Claims 1–3 here) operationalizes the
  human-attention bottleneck at the individual session level. The June 2 fragments'
  Osmani GIL framing describes the architectural constraint (human attention is serial);
  Troy's registers provide a practical technique for reducing the per-session cost of
  that constraint by keeping context focused. The two frameworks should be cited together
  in any guide section on context engineering.

- **Novel**:
  - **Chelsea Troy's four conversation registers**: No existing corpus note introduces
    the register classification (Exploring / Brainstorming / Deciding / Implementing)
    as a named framework for LLM session management. The closest existing content is
    general advice to provide context and clear goals; Troy's framework gives that advice
    structural vocabulary.
  - **Context reset on register switch**: The specific recommendation to start a fresh
    conversation when changing registers is not documented in any existing corpus note.
    Other notes discuss context window management (length, pruning, summarization) but
    not the register-mismatch mechanism that motivates proactive resets.
  - **Dave Thomas and Kent Beck as craftsmanship-positive voices**: No existing corpus
    note documents the perspective from foundational craftsmanship authors (Pragmatic
    Programmer, Kent Beck / XP) that LLMs enhance rather than degrade programming joy.
    This provides a counter-signal to any "AI threatens craftsmanship" framing.
  - **Eric Evans actively experimenting with LLMs**: No corpus note documents Evans'
    multi-year LLM experimentation or his DDD Europe 2026 keynote. Evans is the
    originator of DDD; his engagement with LLMs signals legitimacy for the domain-
    modeling community's exploration of AI tools.
  - **Fowler's DDD+AI prediction**: No corpus note captures Fowler's explicit prediction
    that DDD will grow in importance with AI-driven programming. This is the most senior
    practitioner voice in the corpus on this specific question.

## Guide Impact

- **Chapter 04 (Context Engineering — Conversation Structure)**: Chelsea Troy's
  registers framework (Claims 1–3) is the most actionable addition from this source.
  Add a named section or callout "Conversation Registers" in any chapter covering how
  engineers interact with LLMs. The four registers provide vocabulary for diagnosing
  prompt failures: if an Implementing-mode session is giving open-ended suggestions, the
  register may be wrong. Pair with the register-reset recommendation (start fresh when
  switching). No existing guide section covers this framing.

- **Chapter 01 (Daily Workflows — The Joy Argument)**: Claims 4–5 (Dave Thomas + Kent
  Beck on LLM joy) provide the most credible counter-narrative to craftsmanship anxiety
  in the corpus. Adding a named practitioner voice — "Prag Dave Thomas reports…" — gives
  the guide a specific authority to cite when addressing the concern that AI-native
  engineering is less satisfying than traditional programming. The four specific reasons
  (drudgery, feedback loops, abandoned projects, new technologies) are quotable.

- **Chapter 04 or Chapter 02 (Domain Engineering with AI)**: Claim 7 (Fowler on DDD
  becoming more important) and Claim 6 (Evans at DDD Europe) together support a section
  on how domain modeling skill becomes more valuable as AI handles mechanical coding.
  Current corpus coverage on domain knowledge and AI is sparse; Fowler's explicit
  prediction and Evans' engagement provide the seed for this section.

- **Chapter 05 (Team Adoption — Understanding Both Sides)**: Claim 9 (Fowler's framing
  of Majors' analysis) adds "credibility comes from understanding the opportunity, stakes,
  and tradeoffs" as a guide principle for practitioners navigating internal adoption
  debates. This extends the Majors source note
  (`blog-simonwillison-charity-majors-enthusiast-skeptic.md`) with a Fowler-endorsed
  framing of how to earn credibility with both sides.

## Extraction Notes

- The Fragments format presents multiple distinct voices under one URL. Each fragment
  is a different author's work, with Fowler providing editorial framing. Chelsea Troy
  and Eric Evans content comes from DDD Europe 2026, which Fowler attended in person,
  giving him first-hand access. Dave Thomas content comes from a linked blog post.
  Charity Majors content comes from her Substack (previously extracted via Willison);
  Simon Willison content from his blog (previously extracted in dedicated note).
- The WebFetch tool returned consistent summaries rather than full verbatim text in most
  calls. Verbatim quotes were extracted via targeted fetch calls asking for specific
  passages. The Chelsea Troy register list, Fowler's framing of the registers, and
  the Dave Thomas / Eric Evans passages were returned with high verbatim fidelity across
  multiple fetches. The Willison and Fowler/DDD passages are also quoted verbatim.
  The Charity Majors summary is paraphrased in the WebFetch output — only "understand
  the opportunity, the stakes, and the tradeoffs" was returned in quotes; the broader
  Majors content is extracted in `blog-simonwillison-charity-majors-enthusiast-skeptic.md`.
- Confidence rated "emerging" overall: Troy's registers framework is conceptually
  coherent but single-source; Thomas/Beck reports are anecdotal; Fowler's DDD prediction
  is expert opinion. Evans' attendance at DDD Europe is settled (Fowler was present).
- Mike Masnick's decentralization section in the source is noted but not extracted in
  depth: the Prospector's triage identifies it as "less core to AI engineering." The
  core claims (internet middlemen evolve toward lock-in and algorithmic exploitation;
  user data control and low exit barriers are countermeasures) are noted as context.
- No sub-pages beyond the main fragments page were followed. The Chelsea Troy talk
  itself (from DDD Europe 2026) is reported only through Fowler's summary; a dedicated
  Chelsea Troy source note (if a video or transcript of her DDD Europe talk is available)
  would provide higher-confidence extraction of her registers framework.
- Cross-reference claim numbers verified by direct re-reading of
  `blog-simonwillison-charity-majors-enthusiast-skeptic.md` (Claims 1–6) and
  `blog-simonwillison-product-market-fit.md` (Claims 1, 3) and
  `blog-fowler-fragments-2026-06-02.md` (Claims 11–14).
