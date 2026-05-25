---
source_url: https://simonwillison.net/2026/May/14/not-so-locked-in/
source_type: blog-post
title: "Not so locked in any more"
author: Simon Willison
date_published: 2026-05-14
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: anecdotal
issue: "#871"
---

# Not so locked in any more

> Simon Willison reports a conference anecdote of a mid-sized company completing
> an AI-agent-driven React Native rewrite of legacy iOS and Android apps, citing
> the ability to port back to native in the future as a key factor in the decision
> — illustrating how coding agents are reducing technology lock-in by making
> previously irreversible platform choices reversible.

## Source Context

- **Type**: blog-post (Simon Willison link-blog post, May 14, 2026; five short
  paragraphs plus a blockquote attributed to Mitchell Hashimoto, framing a
  conference anecdote as a concrete example of Hashimoto's broader claim about
  declining programming language lock-in. Tags on the post: ai, react,
  generative-ai, llms, ai-assisted-programming, coding-agents.)
- **Author credibility**: Simon Willison is the creator of Django and one of the
  highest-signal independent AI tooling commentators; his link-blog is a curated
  feed of practitioner-level observations on LLM tooling. This post is his own
  first-person anecdote from a conference, not a relay of another source. The
  practitioner described is unnamed ("someone who worked for a medium sized
  technology company"), which limits verifiability but is consistent with
  conference-conversation confidentiality norms. The blockquote is attributed to
  Mitchell Hashimoto (co-founder and former CEO of HashiCorp), whose practitioner
  authority on technology adoption economics is well-established (see
  `blog-simonwillison-mitchell-hashimoto-tdm-dynamics.md` for source context on
  Hashimoto's credentials).
- **Scope**: A very short post — five paragraphs and a blockquote. Covers: (1) a
  concrete practitioner anecdote of an agent-driven iOS/Android → React Native
  rewrite where reversibility via AI agents was cited as a decision factor; (2)
  Hashimoto's structural claim that programming language/platform lock-in is
  declining. Does NOT cover: mechanics of the rewrite, which coding agents were
  used, timeline, team size, codebase size, what specifically improved in React
  Native, or any quantitative metrics.

## Extracted Claims

### Claim 1: A mid-market technology company completed a coding-agent-driven rewrite of legacy iOS and Android apps to React Native

- **Evidence**: Simon Willison's first-person conference conversation with an
  employee of the company. The company is unnamed but described as "medium sized"
  with "legacy/legendary iPhone and Android apps." The rewrite is described as
  already complete ("had just completed").
- **Confidence**: anecdotal (single conference conversation; unnamed practitioner;
  no corroborating evidence from the company directly)
- **Quote**: "They told me they had just completed a coding-agent driven rewrite
  of both apps to React Native."
- **Our assessment**: This is the concrete artifact that makes the post
  significant. "Coding-agent driven rewrite" as the mechanism is the novel
  element — prior mobile rewrite narratives involved manual porting effort.
  The claim is plausible and consistent with the NAB Assembly mainframe case
  (`blog-cursor-nab-legacy-migration.md` Claim 6), where agents enabled a
  similarly large migration. The anecdotal evidence limits confidence, but
  Willison's track record of reporting real practitioner accounts (not
  hypotheticals) raises its credibility above a speculative example.

### Claim 2: The company chose React Native partly because coding agents make reverting to native a viable fallback, treating the decision as reversible rather than locked-in

- **Evidence**: The practitioner's stated reasoning, relayed verbatim by Willison.
  The reversibility rationale is presented as a co-factor alongside React Native's
  improved technical quality.
- **Confidence**: anecdotal (single practitioner's stated reasoning; no follow-up
  on whether the reasoning reflected organizational consensus or individual
  framing)
- **Quote**: "And... if it turned out to be the wrong decision, they could just
  port back to native in the future."
- **Our assessment**: This is the load-bearing claim of the post. The company is
  not just choosing React Native — they are choosing it WITH the explicit belief
  that the decision is reversible via AI-agent-driven reversion. This is a
  qualitative shift in how platform decisions are made: from strategic commitment
  (requiring high confidence before committing) to reversible experiment (requiring
  only sufficient confidence that the exit path is viable). Prior to coding agents,
  "port back to native" was a prohibitively expensive fallback. The claim suggests
  agents have made that fallback cost-acceptable, changing the decision calculus.

### Claim 3: Coding agents reduce the traditional cost advantage of cross-platform frameworks by lowering the maintenance cost of separate native codebases — but simultaneously make cross-platform choices less risky by enabling cheap reversion

- **Evidence**: Willison's own framing of the paradox in his question to the
  practitioner. Willison notes the tension himself: if agents lower the cost of
  maintaining separate native codebases, the traditional rationale for
  cross-platform (reduce maintenance overhead) is weakened.
- **Confidence**: anecdotal (Willison's analysis, not a formal study; the
  cross-platform tradeoff is real but the specific AI cost dynamics are
  unquantified)
- **Quote**: "I asked why they chose that, given that coding agents presumably
  drive down the cost of maintaining separate iPhone and Android apps."
- **Our assessment**: Willison is identifying a real and underappreciated second-
  order effect: coding agents cut both ways on the cross-platform/native decision.
  They reduce the maintenance argument FOR cross-platform (separate codebases
  become cheaper to maintain) while simultaneously creating a new argument FOR
  cross-platform (the exit path back to native becomes viable). The net effect
  depends on which side of this tradeoff dominates in a given organization's
  situation. For the guide: the AI coding agent era does not have a single
  "correct" answer to native vs. cross-platform — it changes the tradeoffs on
  both sides of the equation.

### Claim 4: React Native's technical quality has improved sufficiently to cover the requirements of companies with legacy native apps

- **Evidence**: Practitioner account, stated as one of two co-factors in the
  decision (the other being reversibility). This is an independent technical
  judgment from a company that had previously maintained native iOS and Android
  apps.
- **Confidence**: anecdotal (single company's assessment; React Native's
  improvement trajectory is independently documented but this is not a benchmark)
- **Quote**: "They said that React Native has improved a lot over the past few
  years and covered everything their apps needed to do."
- **Our assessment**: This claim is secondary to the lock-in insight but
  contextually important: the company chose React Native on the merits, not
  solely because of reversibility. The reversibility argument functions as risk
  mitigation for a decision the team already found technically justified. For the
  guide: this suggests the lock-in-reduction effect of AI agents amplifies
  adoption of cross-platform technologies that have already crossed a quality
  threshold, rather than making low-quality alternatives viable.

### Claim 5: Programming language and platform lock-in is structurally declining as AI coding agents reduce the cost of switching between technologies

- **Evidence**: Mitchell Hashimoto's blockquote (about Bun migrating from Zig to
  Rust), cited by Willison as the provocation for his React Native anecdote.
  Hashimoto is making a general structural claim supported by the Bun example;
  Willison is adding the React Native case as a second corroborating data point.
- **Confidence**: emerging (two named technology migrations support the claim —
  Bun's Zig-to-Rust rewrite and the unnamed company's iOS/Android-to-React-Native
  rewrite; Hashimoto's practitioner authority is high; but both examples are
  anecdotal and the claim is directional rather than quantified)
- **Quote**: "Programming languages used to be LOCK IN, and they're increasingly
  not so."
- **Our assessment**: Hashimoto's claim is the strongest version of the
  generalization. He is asserting that the structural nature of programming
  language lock-in — not just its cost — is changing. If accurate, this has
  significant implications for technology selection in engineering organizations:
  the long-term commitment framing of language/platform choice ("we're a Java
  shop; we're an iOS shop") may become less binding as rewrites become cheaper.
  For the guide: this suggests a category shift in how organizations should
  approach platform decisions — not as 5–10 year commitments requiring exhaustive
  upfront analysis, but as decisions with accessible exit paths that can be
  revisited more frequently.

### Claim 6: The "viable exit path" enabled by coding agents is becoming an explicit decision factor in technology selection — a new decision input that did not exist in pre-agent development

- **Evidence**: The practitioner cited reversibility explicitly as a decision
  factor, not just a risk-mitigation afterthought. The fact that it was mentioned
  in a conference conversation suggests it was salient enough to share as part of
  the decision rationale.
- **Confidence**: anecdotal (one practitioner's stated reasoning; no data on
  prevalence)
- **Quote**: (no additional direct quote beyond Claim 2's quote; this claim is
  our synthesis of the pattern)
- **Our assessment**: Prior to coding agents, "we can always rewrite it later" was
  a rationalization, not a credible decision factor — rewrites were expensive
  enough that organizations rarely followed through. The React Native case suggests
  that agents have made this a real option rather than a notional one, which
  changes how it should be weighted in technology selection. If the reversion path
  is genuinely cheap, then the expected cost of a wrong platform decision drops
  significantly, and organizations can accept a lower confidence threshold before
  committing. This is the expected value argument for why reversibility under AI
  agents is a real decision input: it reduces the downside of a wrong decision,
  which expands the set of acceptable decisions.

## Concrete Artifacts

### Full Blog Post Text (verbatim from https://simonwillison.net/2026/May/14/not-so-locked-in/)

```
Title: Not so locked in any more
Published: 14th May 2026 at 10:53 pm
Tags: ai, react, generative-ai, llms, ai-assisted-programming, coding-agents

[Body:]

This Mitchell Hashimoto quote about Bun migrating from Zig to Rust reminded me
of a similar conversation I had at a conference last week.

I was talking to someone who worked for a medium sized technology company with a
pair of legacy/legendary iPhone and Android apps.

They told me they had just completed a coding-agent driven rewrite of both apps
to React Native.

I asked why they chose that, given that coding agents presumably drive down the
cost of maintaining separate iPhone and Android apps.

They said that React Native has improved a lot over the past few years and
covered everything their apps needed to do.

And... if it turned out to be the wrong decision, they could just port back to
native in the future.

[Blockquote:]

"Programming languages used to be LOCK IN, and they're increasingly not so."

— Mitchell Hashimoto (about Bun migrating from Zig to Rust)
```

## Cross-References

- **Corroborates**:
  - **blog-simonwillison-mitchell-hashimoto-tdm-dynamics.md** Claim 5 ("The
    switching cost to adopt new technology is fundamentally higher than expanding
    existing vendor relationships" — quote: "The cost (cognitive, time, risk,
    money, etc.) of adopting a new thing is significantly higher than expanding
    an old thing."): The not-locked-in anecdote provides a concrete case where AI
    agents are reducing exactly the switching cost Hashimoto identified as
    structurally high. The Hashimoto TDM note (from May 12) describes the problem
    (switching costs are high); the not-locked-in post (from May 14, same author
    and the same Hashimoto's authority) documents a case where that structural
    cost is being overcome via agents. These two notes, written two days apart by
    the same Willison relay, form a coherent argument: lock-in is structural, AND
    agents are now chipping away at that structure.
  - **blog-cursor-nab-legacy-migration.md** Claim 6 ("Assembly mainframe migration
    was previously categorically impossible due to expertise scarcity; AI tools
    unblocked it" — quote: "Without Cursor, the time and cost of this migration
    would have been greater than the value we'd get from it."): Both cases show
    AI agents enabling technology migrations that would previously have been
    prohibitively expensive or impossible. The mechanism differs: NAB's Assembly
    case is about expertise scarcity; the React Native case is about reversion
    insurance. Both result in the same outcome: a previously-locked-in technology
    choice becomes traversable via agents.

- **Extends**:
  - **blog-simonwillison-james-shore-maintenance-costs.md** Claim 7 ("Alternative
    AI levers exist that can improve net productivity without increasing code
    volume — AI tools that make maintenance work itself more efficient" — quote:
    "There's other levers to pull, such as AI that makes maintenance itself more
    productive, even if it doesn't make the code more maintainable."): An
    agent-driven platform consolidation (iOS + Android → React Native) is a
    concrete instance of Shore's "Category 2" AI use: reducing ongoing maintenance
    burden (one codebase instead of two) rather than generating additional code
    volume. This is a use case where Shore's concern about inverse maintenance cost
    reduction does not apply in the same way — the goal is structural maintenance
    reduction, not velocity maximization. The not-locked-in case therefore expands
    the guide's account of Shore's Claim 7 with a real practitioner example.
  - **blog-cursor-nab-legacy-migration.md** Claim 5 ("AI coding tools reduced
    BizCalc monolith pre-development work from 2 months to 1 week by generating
    user stories and API specs via Ask Mode and Plan Mode"): The NAB BizCalc
    monolith-to-microservices migration and the React Native rewrite are both
    agent-driven architectural pivots. NAB's case is larger-scale with named
    metrics; the React Native case is smaller-scale but introduces the reversibility
    angle NAB does not address. Together they establish that agent-driven
    architectural rewrites span a range of scales and motivations.

- **Contradicts**: None filed. No existing corpus note claims that technology
  lock-in is stable or increasing under AI agent adoption. The TDM dynamics note
  (`blog-simonwillison-mitchell-hashimoto-tdm-dynamics.md` Claim 5) describes
  high switching costs as a structural reality but does not assert this is
  permanent — Hashimoto's own quote in the not-locked-in post ("increasingly not
  so") is consistent with his TDM framing evolving as agent costs drop.

- **Novel**:
  - **The "AI agent as reversion insurance" decision factor**: No prior corpus
    source documents practitioners choosing a technology platform specifically
    because AI agents make the exit path viable. Every other corpus migration
    story (NAB, Amplitude, etc.) describes agents enabling a specific migration;
    none describes agents enabling a DECISION to migrate by making the REVERSAL
    cheap. This is the first corpus source documenting the second-order effect:
    not "agents make migration X possible" but "agents change the risk profile of
    decisions about X."
  - **The AI agent double-bind on cross-platform development**: Willison's
    question ("given that coding agents presumably drive down the cost of
    maintaining separate iPhone and Android apps") identifies a genuine paradox
    that no prior corpus source has named: agents simultaneously reduce the
    traditional maintenance argument FOR cross-platform (by making separate native
    codebases cheaper to maintain) AND reduce the lock-in risk of cross-platform
    (by making reversion viable). No other corpus source names this bidirectional
    effect of agents on the native vs. cross-platform tradeoff.
  - **Hashimoto's structural lock-in decline claim in a programming language
    context**: The TDM dynamics note captures Hashimoto on TDM procurement
    dynamics (in a Redis/enterprise-software context). The not-locked-in post
    captures a different Hashimoto claim — in a programming language/platform
    context — about the structural decline of lock-in. These are from different
    Hashimoto statements and belong in separate notes.

## Guide Impact

- **Chapter 05 (Team Adoption — Technology Selection and Organizational Flexibility)**:
  The most direct impact. Chapter 05 should add a section or callout on how AI
  coding agents change the calculus of technology platform decisions. Current
  corpus coverage explains how organizations adopt AI tools; this source
  introduces how AI tools change the risk profile of OTHER technology decisions
  (platform, language). Specific recommendation: frame technology selection
  decisions in an AI-agent era as having materially different risk profiles —
  the expected cost of a wrong decision drops when the reversion path is
  agent-assisted. Cite this source alongside
  `blog-simonwillison-mitchell-hashimoto-tdm-dynamics.md` Claim 5 (switching
  cost structure) and `blog-cursor-nab-legacy-migration.md` Claim 6 (agents
  enabling previously-impossible migrations) to build the full argument.

- **Chapter 04 (Context Engineering — AI-Driven Rewrite Economics)**: The
  React Native rewrite is a concrete example of agents applied to a major
  context engineering challenge: migrating a large established codebase to a
  new platform. Chapter 04 should note that the agent use cases extending
  beyond code generation into architectural migration are already in production
  at mid-sized companies. The not-locked-in case and the NAB BizCalc case
  (`blog-cursor-nab-legacy-migration.md` Claim 5) together establish that
  agent-driven rewrites are not futuristic — they are occurring now.

- **Chapter 01 (Daily Workflows — AI Agents as Enablers of Flexible Architecture)**:
  The practitioner account suggests that individual developers and small teams
  should update their mental model of "locked-in" technology decisions. When
  practitioners assess whether a platform choice is irreversible, they should
  factor in the agent-enabled reversion cost — which is likely lower than the
  pre-agent estimate. Add a brief note: technology decisions made in an AI-agent
  context carry different reversibility assumptions. This changes how practitioners
  should weigh "what if we're wrong?" in technical discussions.

- **Chapter 05 (Team Adoption — Cross-Platform vs. Native Decision Framework)**:
  Willison's paradox (agents reduce the maintenance advantage of cross-platform
  while enabling cross-platform reversion) is worth a short sidebar in the guide.
  Teams choosing between native and cross-platform should evaluate both effects:
  "Will agents make our native codebases cheap enough to maintain that the
  cross-platform maintenance argument disappears? And if so, does reversibility
  via agents still tip the balance toward cross-platform?" These are now
  answerable, nuanced questions — not a fixed calculus.

## Extraction Notes

- **Very short source**: The blog post is five paragraphs and a blockquote. All
  substantive content was extracted. There are no sub-pages to follow; the post
  does not link to external documentation of the React Native rewrite (it is a
  conference anecdote). The Hashimoto blockquote is attributed to a quote "about
  Bun migrating from Zig to Rust" but no direct link to that Hashimoto source is
  provided on the Willison page.
- **Unnamed practitioner**: The company and individual are not named. This is the
  standard confidentiality pattern for Willison's conference anecdotes. The
  anecdotal confidence rating reflects this limitation.
- **Hashimoto blockquote context**: The "Programming languages used to be LOCK IN"
  quote is from a different Hashimoto statement than the TDM dynamics quote in
  `blog-simonwillison-mitchell-hashimoto-tdm-dynamics.md`. That note covers
  Hashimoto's Redis/Lobsters comment (May 12, 2026); this note's blockquote is
  from Hashimoto's statement about Bun's Zig-to-Rust rewrite. The Willison page
  provides no direct link to the Bun/Hashimoto source.
- **Cross-reference verification**:
  - `blog-simonwillison-mitchell-hashimoto-tdm-dynamics.md` Claim 5 (lines
    136–153): "The switching cost to adopt new technology is fundamentally higher
    than expanding existing vendor relationships" — verified by direct reading;
    quote "The cost (cognitive, time, risk, money, etc.) of adopting a new thing
    is significantly higher than expanding an old thing." confirmed at line 145.
  - `blog-simonwillison-james-shore-maintenance-costs.md` Claim 7 (lines 166–181):
    "Alternative AI levers exist that can improve net productivity without
    increasing code volume" — verified; quote "There's other levers to pull, such
    as AI that makes maintenance itself more productive, even if it doesn't make
    the code more maintainable." confirmed at line 172.
  - `blog-cursor-nab-legacy-migration.md` Claim 5 (lines 54–60): AI coding tools
    reduced BizCalc monolith pre-development work from 2 months to 1 week —
    verified.
  - `blog-cursor-nab-legacy-migration.md` Claim 6 (lines 61–68): Assembly
    mainframe migration was previously categorically impossible due to expertise
    scarcity — verified; quote "Without Cursor, the time and cost of this
    migration would have been greater than the value we'd get from it." confirmed
    at line 66.
