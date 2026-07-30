---
source_url: https://www.thoughtworks.com/insights/blog/architecture/modularity-mortality-importance-skin-game
source_type: blog-post
title: "Modularity and mortality: The importance of 'skin in the game'"
author: Andrew Harmel-Law and Richard Gall (Thoughtworks)
date_published: 2026-07-17
date_extracted: 2026-07-30
last_checked: 2026-07-30
status: current
confidence_overall: emerging
issue: "#2327"
---

# Modularity and Mortality: The Importance of 'Skin in the Game'

> Harmel-Law and Gall argue that enterprise codebases decay into a "Big Ball
> of Mud" because two things are missing that successful plugin ecosystems
> (WordPress, Drupal, Linux) have: a mortality mechanism that lets unfit
> components die, and personal "skin in the game" driven by long-term
> ownership — and that both problems are amplified, not created, by LLMs,
> which will find "the most efficient mathematical path" through a codebase
> regardless of encapsulation unless boundaries are enforced by the harness
> itself.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, "Architecture" category; filed
  via the trusted `thoughtworks` RSS feed; published 2026-07-17, page
  `dateModified` 2026-07-23; co-authored practitioner/opinion essay, roughly
  1,500 words, no case-study data, no code blocks, no named client
  engagement).
- **Author credibility**: Andrew Harmel-Law and Richard Gall are both credited
  Thoughtworks authors (confirmed via the page's embedded `application/ld+json`
  structured data: `"author":[{"name":"Andrew Harmel-Law",...},{"name":"Richard
  Gall",...}]`). Harmel-Law has one prior corpus appearance
  (`blog-thoughtworks-harmellaw-nfr-guardrail.md`, published nine days earlier,
  on non-functional requirements as an AI-generation guardrail); Gall has one
  prior corpus appearance (`blog-thoughtworks-gall-supervisory-engineering.md`,
  on the "middle loop"/supervisory engineering). Neither author's specific
  title or years of architecture-consulting experience is stated in this
  article's own byline beyond the Thoughtworks affiliation. The piece is
  argumentative/conceptual synthesis — it cites named external concepts (Brian
  Foote and Joseph Yoder's "Big Ball of Mud," David Parnas's information-hiding
  papers, Eric Evans's DDD, Conway's Law, unnamed "Microsoft research") but no
  primary source links, case study, or measured outcome data for its own
  central claims.
- **Scope**: Covers why enterprise codebases erode into a Big Ball of Mud
  despite constant industry talk about modularity; a "mortality" theory
  (successful plugin ecosystems survive because unfit components die,
  enterprise codebases don't); two named failure modes of applying
  domain-driven design; a worked example of business-model/boundary
  misalignment (airline "seat" as value object vs. entity); an organizational
  argument that ownership churn produces a "Swamp Guide" archetype that
  entrenches codebase chaos; and a closing argument that LLMs remove the
  option of soft, unenforced boundaries and require harness-level enforcement.
  Does NOT cover: any named client engagement or measured outcome for any of
  its claims; the Microsoft ownership-churn research by name, author, or link;
  technical detail on how "harness-enforced boundaries" or "contract-verified
  interfaces" would actually be implemented; or any account of Vlad Kononov's
  "modularity skill" beyond a one-paragraph description.

## Extracted Claims

### Claim 1: The industry's chronic inability to design and maintain meaningful architectural boundaries stems from a fundamental misunderstanding of evolutionary mechanics — specifically, a failure to align domain boundaries with actual business models combined with the systematic elimination of personal "skin in the game" from modern engineering teams
- **Evidence**: The authors' own diagnostic thesis, stated as the article's central claim after describing the industry's "chronic inability" to maintain boundaries; developed in the rest of the article via the mortality argument (Claims 2-4), the DDD-misalignment argument (Claims 5-7), and the ownership-churn argument (Claims 8-9).
- **Confidence**: emerging (a reasoned, internally-developed thesis connecting two previously-separate observations — evolutionary/mortality dynamics and business-model alignment — but not empirically tested; no measured comparison of codebases with vs. without either factor)
- **Quote**: "The root of our challenges could be a fundamental misunderstanding of evolutionary mechanics, arising from a failure to align domain boundaries with actual business models and the systematic elimination of personal 'skin in the game' from modern engineering teams."
- **Our assessment**: This is the article's thesis statement and the frame the rest of the piece hangs from — two distinct causal claims (evolutionary/mortality dynamics; business-model misalignment) bundled with a third (loss of ownership) that gets its own full section later. It should be cited as the organizing hypothesis, not as a settled finding — the article's own supporting evidence for each strand is itself anecdotal or conceptual (see Claims 2-9).

### Claim 2: Genuinely successful, highly modular software ecosystems (WordPress, Drupal, Linux, Android) are powered by extension/plugin/"commands and pipes" architectures whose real driver of cleanliness is not superior initial design but the ever-present threat of mortality — plugins that fail to adapt, become bloated, or lose utility simply die and are never used again
- **Evidence**: The authors' own conceptual argument, illustrated by four named ecosystems (with Drupal singled out as "the most controversial example" given its reputation for aesthetic messiness despite achieving massive scale).
- **Confidence**: emerging (a plausible evolutionary analogy applied to named real ecosystems, but no citation, data, or measurement of plugin "death rates" is given — it is an argued mechanism, not a demonstrated one)
- **Quote**: "Its secret isn't a pristine API or superior initial design; it might, though, be the ever-present threat of mortality. Biologically, evolution involves death. These plugin ecosystems may be thriving because they possess an inherent process for shedding the less fit members over time. If a plugin fails to adapt, becomes bloated or loses its utility, it 'dies' and is never used again."
- **Our assessment**: The "mortality drives modularity" framing is the article's most novel contribution — a specific mechanism (death of unfit components) for *why* plugin architectures stay clean, distinct from the more common explanation (a well-designed initial API). It's presented with appropriate hedging ("might, though") rather than as settled fact, which this note preserves.

### Claim 3: Enterprise codebases suffer from "absolute immortality" — nothing ever dies, so technical debt accumulates like sedimentary rock — because internal teams are "too close to each other" to enforce the strict separation and contracts that external-facing plugin architectures are forced into by not knowing who their consumers are
- **Evidence**: The authors' own contrastive argument, extending Claim 2's plugin-ecosystem observation to the enterprise case.
- **Confidence**: emerging (a coherent extension of Claim 2's mortality argument, but — like Claim 2 — asserted rather than measured; no data on debt-accumulation rates or a comparative study of internal vs. external-facing codebases is given)
- **Quote**: "In contrast, enterprise codebases frequently suffer from absolute immortality. Nothing ever dies. We accumulate layers of technical debt like sedimentary rock, in great part because we deprioritize the forcing functions that might compel clean contracts, a primary prerequisite for the gradual, incremental evolution of individual components."
- **Quote** (the "too close" mechanism): "When you build a plugin for external users, you're forced into a strict separation and a proper contract because you don't know who your consumers are. But when we build internal enterprise codebases for our colleagues or our future selves, we are too close to each other. The boundaries aren't enforced, so we choose the shortest path to call a function and the architecture degrades."
- **Our assessment**: This is a specific, citable mechanism for *why* internal codebases decay even when teams know good practice — the absence of an external, unknown consumer removes the pressure that normally forces contract discipline. It directly motivates the article's later claim (Claim 10) that LLMs, unlike human colleagues, don't respect the informal social contract of "we're all close, so we won't abuse this," which is why the authors argue AI-assisted development needs harder, harness-enforced boundaries than human teams have tolerated.

### Claim 4: Migrating to microservices by breaking a system down until there is one entity per service is not modularity but "an architectural panic attack" that produces a "distributed monolith," because boundaries that are purely technical rather than conceptual don't solve the original monolith problem — they just add network latency to already-tangled code
- **Evidence**: The authors' own critique of a common industry pattern (microservice migration motivated by "too big to reason about" codebases).
- **Confidence**: emerging (a specific, falsifiable-in-principle critique of a widely-observed anti-pattern, consistent with existing "distributed monolith" discourse in the wider industry, though not independently measured in this article)
- **Quote**: "Many teams migrate to microservices because they feel the codebase is 'too big to reason about.' But often they fumble the opportunity to meaningfully modularize. Breaking your system down until you have one entity per service isn't modularity; it's an architectural panic attack that leads to a 'distributed monolith'. The issue here is that boundaries which are purely technical rather than conceptual don't solve the monolith problem. They just introduce another problem, that of network latency, to the already spaghetti-tending code."
- **Our assessment**: This is a sharp, quotable distinction between technical decomposition (splitting into N services) and conceptual decomposition (aligning boundaries to meaningful domain concepts) — directly relevant to any guide content warning against treating "more services" as a proxy for "better modularity," a distinction that becomes more urgent when an LLM can generate service-boundary code quickly without the domain understanding to place the boundaries well.

### Claim 5: Domain-driven design (DDD) has existed since 2003 but is applied badly in one of two ways — either as a "tactical handbook" (debating Entity vs. Value Object, treating aggregates as "holy writ" without understanding their purpose) or as vague talk about "bounded contexts" and "sub domains" with no intent to actually uncover and evolve those boundaries in code
- **Evidence**: The authors' own critique of common DDD-adoption failure modes; no survey or count of how often each failure mode occurs is given.
- **Confidence**: emerging (a specific, two-part taxonomy of a named, well-established methodology's misapplication — plausible and consistent with widely-reported DDD adoption difficulties, but asserted rather than measured)
- **Quote**: "Yet we fail in applying it in one of two key ways. Either we treat it as a tactical handbook, debating ad nauseam whether a concept is an Entity or a Value Object, and treat aggregates as holy writ (without really understanding what they are or what they offer), or we talk about 'bounded contexts' and 'sub domains' without any intent to uncover, design and evolve those meaningful edges and relationships in a way that gets into the code."
- **Our assessment**: This two-way taxonomy (over-tactical vs. all-talk-no-code) is a specific, actionable diagnostic for teams evaluating their own DDD practice — more precise than a generic "you're not doing DDD right" complaint, since it names two opposite failure directions rather than one.

### Claim 6: Modularity fails when technologists draw boundaries around a business concept they don't sufficiently understand — if technical boundaries can't be mapped directly to the specific business model, the modules are wrong from day one, illustrated by how a "seat" means something structurally different to a budget airline (a volatile, fluidly-swapped value object) than to a luxury carrier with bespoke cabins (a highly specific, stateful entity)
- **Evidence**: The authors' own architectural-practice claim, illustrated with a constructed (not real-company) worked example contrasting two airline business models.
- **Confidence**: emerging (the underlying practice — that generic domain nouns hide business-specific structure — is a well-established DDD principle; the specific airline "seat" illustration is the authors' own constructed example, not a named real case)
- **Quote**: "The key point is that modularity fails when technologists attempt to draw boundaries around a concept they don't sufficientlyly understand. If you cannot map your technical boundaries directly to your specific business model, your modules will be wrong from day one."
- **Quote** (the airline example): "Consider two airlines booking places on planes. To a budget carrier, a 'seat' might be a volatile value object, fluidly swapped until the moment of boarding. To a luxury liner with bespoke cabins, that same seat is a highly specific, stateful entity. The business processes around both will be very different also. If you design your software based on generic industry nouns rather than your specific workflows and value streams that drive your enterprise, your boundaries will never emerge in a sustainable way."
- **Our assessment**: This is the article's most concrete, memorable worked example — a specific, transferable heuristic ("does this concept mean the same thing to any two competitors in this space, or is that apparent sameness hiding structurally different business processes?") that a team can apply directly when deciding where to draw a module boundary. Note: the source text contains a typo, "sufficientlyly," reproduced verbatim as published (flagged `[sic]`).

### Claim 7: Modularity is not a top-down architectural blueprint delivered by an all-knowing architect, nor the encoding of database tables in software — it is the outcome of an ongoing, iterative, bottom-up-plus-top-down discovery process where the language of the code evolves in lockstep with breakthroughs in business understanding
- **Evidence**: The authors' own conceptual claim, presented as the resolution of the DDD-misapplication critique (Claims 5-6) and as a restatement of what the authors say Eric Evans's DDD "core" already supports.
- **Confidence**: emerging (a coherent conceptual claim consistent with established DDD literature's emphasis on iterative model refinement, though the specific "bottom-up-plus-top-down" framing is the authors' own synthesis rather than a direct DDD citation)
- **Quote**: "Modularity is not a top-down architectural blueprint delivered by an all-knowing system or domain architect. Nor is it the encoding of database tables in software. It's the outcome of an ongoing, iterative, bottom-up-plus-top-down discovery process where the language of the code evolves in lockstep with the breakthroughs in business understanding. Domain-driven design knows and supports this at its core; we just keep forgetting it."
- **Our assessment**: This directly counters any guide framing that treats "define the module boundaries up front, then generate the code" as a sufficient AI-assisted-development workflow — the authors argue boundary discovery is inherently iterative and coupled to evolving business understanding, which has implications for how much boundary-setting an agent can be trusted to do unsupervised before business understanding has caught up.

### Claim 8: Microsoft research identified a single non-code metric that directly correlates with systemic software bugs — ownership churn — which sets off a chain: high team/contractor churn leads to loss of shared mental model, which leads to short-term tactical wins, which leads to the emergence of the "Swamp Guide"
- **Evidence**: Cited to unnamed "Microsoft research," with no link, paper title, or author given within the article; the causal chain itself is the authors' own diagrammed synthesis.
- **Confidence**: anecdotal (the article references external research but gives no citation, title, author, or link — the specific "ownership churn as a single non-code metric" claim should be independently verified against a primary Microsoft source before being cited as settled fact in the guide; the causal chain built on top of it is the authors' own argument, not itself sourced to Microsoft)
- **Quote**: "The technical decay of a codebase is directly correlated with the organizational dynamics of the teams that build it. Microsoft research famously isolated a single non-code metric that directly correlates with systemic software bugs: ownership churn."
- **Quote** (the causal chain, verbatim from the article's own diagram formatting): "High team/contractor churn → Loss of shared mental model → Short-term tactical wins → The emergence of the 'Swamp Guide'"
- **Our assessment**: This is a concrete, guide-relevant organizational claim, but the "Microsoft research" citation is unverifiable from this article alone — no title, author, or link is given, so it should be flagged in the guide as an oft-cited-but-unsourced-here claim rather than an independently confirmed research finding, consistent with how this corpus treats other uncited "widely discussed" claims (e.g., `blog-thoughtworks-lewis-gov-structural-modernization.md` Claim 8's unnamed "MIT study," similarly flagged as needing independent verification).

### Claim 9: High churn environments naturally select for a "Swamp Guide" (or, per Alberto Brandolino's naming, "Dungeon Master") archetype — the developer who thrives navigating chaotic, undocumented codebases by knowing where the bodies are buried and which side-effects to exploit — and the business rewards this speed while remaining blind to the fact that the Swamp Guide's own survival strategies deepen the swamp and ensure no one else can cross it
- **Evidence**: The authors' own organizational-dynamics argument, attributing the "Dungeon Master" naming to a specific named individual (Alberto Brandolino); no citation or link is given for Brandolino's naming, and no data on Swamp Guide prevalence or productivity impact is provided.
- **Confidence**: emerging (a specific, well-developed organizational archetype with a plausible self-reinforcing feedback mechanism — the person best rewarded is the one whose skills depend on the codebase staying chaotic — but presented as authorial argument, not measured or surveyed)
- **Quote**: "It gets worse. For those who do stay with organizations, this environment naturally selects for a dangerous corporate archetype: the Swamp Guide (or, as Alberto Brandolino named them, the Dungeon Master). This is the developer who thrives in the chaotic, unmapped depths of broken codebases. They know exactly where the bodies are buried, which undocumented side-effects to leverage and how to get a feature shipped in half the time by ignoring encapsulation."
- **Quote** (the feedback loop): "They might not even like it, but because they can navigate the swamp, they become indispensable. The business rewards them for their speed, completely blind to the fact that their survival strategies are actively making the swamp deeper and ensuring no one else can cross it."
- **Our assessment**: This is the article's most memorable named archetype and a genuinely useful diagnostic concept for the guide — a self-reinforcing organizational failure mode where the incentive structure (reward speed) actively selects against the people and behaviors that would fix the underlying decay. It gives teams a specific question to ask: "are we structurally rewarding people for successfully navigating chaos, rather than for reducing it?"

### Claim 10: Given free rein across a massive, unstructured repository, an LLM will find the most efficient mathematical path to accomplish a task even if that means completely obliterating encapsulation, changing visibility modifiers, or introducing hidden semantic coupling — because agents have no intrinsic motivation to preserve clean abstractions or concern for their future agent selves — which means safely leveraging AI in software engineering may require enforcing harder boundaries than humans have traditionally tolerated, such as sharding systems into stricter subdirectories, separate repositories, or isolated sub-modules that a harness strictly forbids an agent from crossing without an explicit, contract-verified interface
- **Evidence**: The authors' own extension of the article's central thesis (Claims 1-4) to LLM-assisted development specifically; no benchmark, incident, or named case of an LLM actually "obliterating encapsulation" is given — this is presented as a reasoned prediction, not an observed/measured event.
- **Confidence**: emerging (a plausible, mechanistically-argued extrapolation from the article's own established argument about why unenforced internal boundaries erode — "we are too close to each other" (Claim 3) becomes "the agent has no stake in the relationship at all" — but the specific claim about LLM behavior is asserted, not evidenced by a cited incident or study)
- **Quote**: "Agents don't think about their future agent selves; nor do they possess intrinsic motivation to preserve clean abstractions. Given free rein across a massive, unstructured repository, an LLM will find the most efficient mathematical path to accomplish a task, even if that means completely obliterating encapsulation, changing visibility modifiers or introducing hidden semantic coupling."
- **Quote** (the prescription): "In order to safely leverage AI in software engineering, we may have to enforce harder boundaries than humans have traditionally tolerated. This could mean sharding systems into far-stricter subdirectories, separate repositories or isolated sub-modules where an agent is strictly forbidden by a harness from crossing boundaries without an explicit, contract-verified interface."
- **Our assessment**: This is the article's central AI-native-engineering contribution and its most actionable claim: it reframes modularity from a code-quality nicety into what the article elsewhere calls "a cognitive prerequisite" for safe agent operation, and it names a specific mechanism (harness-enforced, contract-verified subdirectory/repository boundaries) rather than a vague call for "more discipline." Note: the source text contains a typo, "future agent selve" (singular, apparently for "selves"), reproduced verbatim as published (flagged `[sic]`).

### Claim 11: LLMs can also serve as boundary monitors — tools like Vlad Kononov's "modularity skill" can surface structural and semantic coupling trade-offs to a team in real time by listening for lexical shifts in user stories, ADRs, and pull requests, flagging architectural drift (e.g., "this code is treading on the toes of the billing domain") before a build simply breaks
- **Evidence**: A single named tool reference (Vlad Kononov's "modularity skill"), described in one paragraph with no link, no usage data, and no independent account of how the tool works beyond the authors' own one-sentence characterization.
- **Confidence**: anecdotal (a single named-but-unlinked tool cited as an example of an emerging capability; no data on adoption, accuracy, or false-positive rate for this or any comparable "boundary monitor" tool is given)
- **Quote**: "There's hope arising concurrently from the same source, with particularly fascinating promise in using LLMs as conversational boundary monitors. Tools like Vlad Kononov's modularity skill demonstrate that AI can surface structural and semantic tradeoffs, explaining different types of coupling to a team in real-time."
- **Quote** (the flagged-drift illustration): "'This code is treading on the toes of the billing domain. It's time for the humans to get in a room and talk.'"
- **Our assessment**: This is presented as a counterweight to Claim 10's "harder boundaries" prescription — instead of (or alongside) hard, harness-enforced barriers, an LLM could act as a soft, conversational early-warning system for boundary drift. Because it names one specific, unlinked tool without independent verification, this should be treated as an illustrative example of an emerging pattern (LLM-as-architecture-monitor) rather than as evidence the pattern is proven or widely adopted.

### Claim 12: Three concrete practices are recommended for becoming "more modular": design for deletability rather than reusability (a module's cleanliness is tested by whether it can be ripped out and rewritten quickly); align core and supporting subdomains to the specific business model rather than generic domain nouns; and fight team churn to fight code decay by prioritizing longer-lived, durable teams that own outcomes rather than outputs
- **Evidence**: The authors' own closing prescriptive list, titled "Advice to technologists," presented as three named, bolded action items.
- **Confidence**: emerging (three specific, actionable recommendations, directly following from the article's own argued claims — deletability follows from the mortality argument (Claims 2-3), business-model alignment follows from Claims 5-7, and fighting churn follows from Claims 8-9 — but none is independently validated with outcome data in the article)
- **Quote** (deletability): "Design for deletability, not reusability. Stop trying to write the perfect, infinitely extensible module. Instead, focus on building small, autonomous components with clean contracts. The test of this cleanliness and understandability is if it can be ripped out and rewritten in short order when they need a refresh"
- **Quote** (business-model alignment): "Align your core and supporting subdomains to your business model. If your software modules rely too much on generic domain nouns (e.g., 'user,' 'product') rather than the unique operational workflows that differentiate your business from your competitors, your architecture is likely built on sand."
- **Quote** (fight churn): "Fight team churn to fight code decay. If your organization treats engineers like interchangeable cogs in short-lived 'mission teams,' accept that your architecture will inevitably reflect that fractured, short-term thinking. Prioritize longer-lived, durable teams that own outcomes, not outputs."
- **Our assessment**: "Design for deletability, not reusability" is the single most quotable, guide-ready line in the article — it reframes the traditional software-engineering goal (build reusable, extensible components) into a mortality-compatible one (build components that are cheap to kill and replace), which is directly consistent with Claim 2's mortality-drives-modularity thesis. All three items are restatements of claims already developed earlier in the article, packaged as an actionable checklist.

## Concrete Artifacts

### Ownership-churn causal chain (verbatim, reproduced from the article's own diagram-style formatting)
```
Source: Andrew Harmel-Law and Richard Gall, "Modularity and mortality: The
importance of 'skin in the game'", Thoughtworks Insights, 2026-07-17

High team/contractor churn ──>
Loss of shared mental model ──>
Short-term tactical wins ──>
The emergence of the 'Swamp Guide'
```

### "Advice to technologists" — three-item checklist (verbatim)
```
Source: as above

Design for deletability, not reusability.
  Stop trying to write the perfect, infinitely extensible module. Instead,
  focus on building small, autonomous components with clean contracts. The
  test of this cleanliness and understandability is if it can be ripped out
  and rewritten in short order when they need a refresh

Align your core and supporting subdomains to your business model.
  If your software modules rely too much on generic domain nouns (e.g.,
  'user,' 'product') rather than the unique operational workflows that
  differentiate your business from your competitors, your architecture is
  likely built on sand.

Fight team churn to fight code decay.
  If your organization treats engineers like interchangeable cogs in
  short-lived 'mission teams,' accept that your architecture will
  inevitably reflect that fractured, short-term thinking. Prioritize
  longer-lived, durable teams that own outcomes, not outputs. Also consider
  the sense of ownership and domain understanding within the teams that own
  parts of your codebases. It's the difference between short and long-term
  gains from our new toolsets.
```

### Article structure (section headings, in order)
```
Source: as above

1. (intro, unheaded) — the "chronic inability" thesis
2. Mortality drives modularity
3. The misalignment of the core domain
4. Churn, 'Swamp Guides' and the erasure of ownership
5. The next challenge for modular boundaries
6. Advice to technologists
7. Questions for further exploration
```

### Closing open questions (verbatim, for potential guide discussion prompts)
```
Source: as above

- If Parnas's principles of information hiding hold true when the word
  'module' is replaced by 'microservices,' does the widespread availability
  of source code across collaborating internal services inherently doom
  enterprise architectures to semantic drift?
- How will Conway's Law adapt to agentic environments? If AI coordinates the
  communication and implementation across domains, what structural
  mutations will manifest in the resulting software architectures?
- Can an engineering organization truly scale if it relies on 'Swamp
  Guides,' or must a healthy culture actively incentivize the systematic
  draining of the swamp, even if it temporarily slows down tactical feature
  delivery?
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-thoughtworks-harmellaw-nfr-guardrail.md`,
`blog-thoughtworks-gall-supervisory-engineering.md`,
`blog-thoughtworks-lewis-gov-structural-modernization.md`,
`blog-fowler-fragments-2026-07-06.md`, and `blog-anthropic-how-contain-claude.md`
were re-read directly (MINER.md §4b) and claim numbers below were confirmed
against those notes' numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-fowler-fragments-2026-07-06.md` Claim 5 (Laura Tacho's "the Venn
    Diagram of Developer Experience and Agent Experience is a circle" —
    "the Genie uses the same constructs to understand a code base that
    humans do, so things like good modularity and naming help it as much as
    it helps humans"): This article's Claim 10 makes the same underlying
    point from the opposite framing — where Tacho argues good modularity
    *helps* an agent the same way it helps a human, this article argues an
    agent given a badly-bounded codebase will exploit the lack of boundaries
    exactly as efficiently, since an LLM "will find the most efficient
    mathematical path to accomplish a task" regardless of encapsulation.
    Both sources converge on architecture/modularity mattering *more*, not
    less, once an LLM is reading and writing the code.
  - `blog-thoughtworks-lewis-gov-structural-modernization.md` Claim 10
    (test-driven development, continuous integration, refactoring
    discipline, pair programming, small services with clear
    responsibilities, and Unix-style modularity named as guardrails for
    AI-assisted development): This article's Claim 4 (purely-technical
    service boundaries don't solve the monolith problem; boundaries must be
    conceptual) and Claim 12 (align subdomains to the business model) sharpen
    what "modularity as an AI guardrail" concretely requires — not simply
    "more/smaller services," but conceptually meaningful ones.
  - `blog-thoughtworks-gall-supervisory-engineering.md` Claim 8 ("directing"
    means codifying engineering standards explicitly "so an agent doesn't
    hallucinate its own design patterns"): This article's Claim 10 (an LLM
    given free rein "will find the most efficient mathematical path...even
    if that means completely obliterating encapsulation") is the same
    underlying risk — an agent inventing or ignoring architectural
    conventions absent explicit, enforced constraints — restated with a
    specific mechanism (mathematical path-of-least-resistance) rather than
    Gall's "hallucinate" framing.

- **Contradicts**: None identified. This Miner checked
  `blog-thoughtworks-gall-supervisory-engineering.md` Claim 11 (the industry
  "no longer requires you to be a walking syntax dictionary," favoring
  mental models of system architecture over syntax mastery) as a plausible
  tension candidate against this article's emphasis on conceptual/DDD-level
  domain understanding (Claims 5-7), since both concern what skill matters
  most in AI-assisted development. On inspection this is not a
  contradiction: Gall's claim is about which *human skill* remains valuable
  (architectural mental models over syntax), and this article's claim is
  about what a *codebase* needs (conceptually meaningful boundaries) — the
  two are complementary rather than opposed (architectural mental models are
  precisely what's needed to draw the conceptually meaningful boundaries
  this article argues for). No contradiction issue filed per MINER.md §4a.

- **Extends**:
  - `blog-anthropic-how-contain-claude.md` (Anthropic's first-party
    containment architecture for claude.ai, Claude Code, and Claude Cowork,
    organized around a likelihood × blast-radius risk framework and a
    preference for environmental over model-layer controls): That note
    documents boundary/containment enforcement at the *execution-environment*
    layer (sandboxes, ephemeral filesystems, permission gating — Claims 4-9
    of that note) to limit what an agent's *tool calls* can reach. This
    article's Claim 10 (sharding into stricter subdirectories/repositories,
    harness-forbidden boundary crossing without a contract-verified
    interface) argues for enforcement at the *codebase-architecture* layer —
    which domains and modules an agent's *edits* may touch — a distinct but
    complementary containment surface. Read together, they suggest a
    harness needs both: environmental sandboxing (what commands/network/
    filesystem an agent can reach) and architectural/domain sandboxing
    (which parts of the codebase's conceptual boundaries an agent's code
    changes may cross). No existing corpus note previously connected these
    two containment layers explicitly.
  - `blog-thoughtworks-harmellaw-nfr-guardrail.md` (same co-author,
    published nine days earlier; that note's Claim 5 argues NFRs like
    PCI-DSS compliance should be scoped precisely to the specific components
    that need them, illustrated by Amazon's PCI boundary, rather than applied
    as a blanket obligation): This article's business-model-alignment
    argument (Claims 5-6) and the "harder boundaries" prescription (Claim
    10) extend the same precise-scoping instinct from non-functional
    requirements to structural/domain boundaries — both articles argue that
    precision and explicitness in *where* a boundary or requirement applies
    is what makes it effective, rather than diffusing it everywhere.

- **Novel**:
  - **"Mortality drives modularity"** (Claim 2): the specific evolutionary
    mechanism — unfit plugin components literally dying and never being
    reused — as the explanation for why extension-based ecosystems
    (WordPress, Drupal, Linux, Android) stay cleaner than enterprise
    codebases, is not present elsewhere in the corpus.
  - **"Absolute immortality" / "too close to each other"** (Claim 3) as the
    named mechanism for why internal enterprise codebases specifically lack
    the forcing function that external-facing plugin architectures have —
    a distinct causal story from the generic "technical debt accumulates"
    framing found elsewhere in the corpus.
  - **The Swamp Guide / Dungeon Master archetype and its self-reinforcing
    feedback loop** (Claims 8-9): a named organizational pattern — high
    churn selects for people whose value depends on the codebase staying
    chaotic, and the business rewards them for exactly the behavior that
    deepens the chaos — not documented elsewhere in the corpus.
  - **"Design for deletability, not reusability"** (Claim 12) as a named,
    quotable reframing of the traditional software-engineering goal of
    building reusable/extensible components.
  - **LLM-as-conversational-boundary-monitor via a named tool (Vlad
    Kononov's "modularity skill")** (Claim 11): a specific, if thinly
    documented, example of AI used to detect architectural drift from
    lexical signals in user stories/ADRs/PRs, not present elsewhere in the
    corpus.
  - **The airline "seat" value-object-vs-entity illustration** (Claim 6): a
    specific, transferable worked example for diagnosing business-model
    misalignment in domain boundaries.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claim 10 (LLMs will find "the
  most efficient mathematical path" through a codebase regardless of
  encapsulation, requiring harder, harness-enforced boundaries — sharding
  into subdirectories/repositories/sub-modules an agent is "strictly
  forbidden by a harness from crossing... without an explicit,
  contract-verified interface") as a specific, actionable recommendation for
  harness design, distinct from the existing CLAUDE.md/engineering-standards
  content — this is about structural/filesystem-level enforcement of domain
  boundaries, not just documented conventions an agent might ignore. Pair
  with `blog-anthropic-how-contain-claude.md`'s environmental-containment
  content (Claims 4-9 of that note) to give a fuller picture of the two
  distinct containment layers a harness needs (execution environment vs.
  codebase architecture).

- **Chapter 02 or Chapter 04 (Architecture/Design in the AI Era)**: Add
  Claim 2's "mortality drives modularity" thesis and Claim 12's "design for
  deletability, not reusability" reframing as a specific architectural
  principle for AI-assisted codebases — since LLMs can generate replacement
  modules cheaply, a codebase organized around small, deletable, clean-contract
  components may be a better fit for agentic maintenance than one organized
  around maximally reusable, extensible abstractions. This is a novel
  argument not currently reflected in the guide's architecture content.

- **Chapter 03 (Verification) or Chapter 04 (Architecture)**: Add Claim 4's
  distinction between technical decomposition (splitting into N services) and
  conceptual decomposition (boundaries mapped to actual business workflows)
  as a specific caution against treating microservice/module count as a
  modularity proxy — directly relevant when an agent can generate
  service-boundary code quickly without the domain understanding to place
  boundaries well. Pair with Claim 6's airline "seat" example as a concrete
  illustration technologists can apply when reviewing agent-proposed module
  boundaries.

- **Chapter 05 (Team Adoption)**: Add Claims 8-9 (ownership churn → Swamp
  Guide archetype) as an organizational-dynamics caution for teams
  restructuring around AI-assisted development — if AI-assisted throughput
  lets an organization tolerate even higher team/contractor churn, this
  article's causal chain suggests that would *accelerate* the Swamp Guide
  dynamic rather than mitigate it. Flag the underlying "Microsoft research"
  citation (Claim 8) as unverified-at-source per the Our-assessment note
  above; do not cite the "single non-code metric" claim as an independently
  confirmed research finding without locating the primary source.

## Extraction Notes

1. **Fetched via direct HTML retrieval, not WebFetch's summarization path.**
   Per MINER.md §2a, the raw HTML was fetched directly via `curl` with a
   browser user-agent (HTTP 200), then parsed locally in Python: stripped
   `<script>`/`<style>` blocks, converted remaining tags to newlines, and
   decoded HTML entities (including `&#39;` for apostrophes and quote marks,
   which a first-pass decoding missed and which would otherwise have
   produced quotes with literal `&#39;` sequences instead of apostrophes).
   Every quote in this note is copied character-for-character from that
   locally-parsed text, not from any WebFetch summary.
2. **Author names and publish/modify dates confirmed via the page's embedded
   `application/ld+json` structured-data block**
   (`"author":[{"name":"Andrew Harmel-Law",...},{"name":"Richard
   Gall",...}]`, `"datePublished":"2026-07-17T00:00:00.000Z"`,
   `"dateModified":"2026-07-23T15:39:07.372Z"`), in addition to the visible
   on-page byline ("By Andrew Harmel-Law and Richard Gall").
3. **Two verbatim source typos preserved rather than silently corrected**,
   per the verbatim-quoting requirement: "a concept they don't
   sufficientlyly understand" (Claim 6, apparently a duplicated syllable —
   "sufficiently" typed as "sufficientlyly") and "Agents don't think about
   their future agent selve" (Claim 10, apparently missing a final "s" on
   "selves"). Both are reproduced as published and flagged `[sic]` above
   rather than corrected.
4. **No sub-pages followed.** The article's substantive outbound links are
   to Wikipedia-style background on "Big Ball of Mud," a Thoughtworks
   profile link for "key breakthroughs Eric Evans offered us," and an
   unlinked-in-text mention of "Vlad Kononov's modularity skill" (the visible
   anchor text links to a hosted page, but this Miner did not independently
   fetch it — the article's own one-paragraph description is the sole basis
   for Claim 11 above, which is rated anecdotal accordingly). None of the
   three unrelated "More Insights" teaser links at the bottom of the page
   (on semantic drift/AI, the AI token crisis, and a codeless-future
   question) were followed, as none bear on this article's own claims
   beyond what related existing corpus notes already cover.
5. **No contradiction issue filed.** The one plausible tension candidate
   checked (`blog-thoughtworks-gall-supervisory-engineering.md` Claim 11 on
   syntax-mastery vs. architectural mental models) was resolved as
   complementary rather than opposed — see Cross-References → Contradicts.
6. **Overall confidence rated "emerging."** The article's central claims
   (Claims 1-7, 10, 12) are the authors' own coherent, well-argued
   conceptual synthesis, consistent with and extending established external
   concepts (Big Ball of Mud, DDD, Conway's Law) but not independently
   tested or measured within the article itself. Claims 8 and 11 are rated
   individually as anecdotal, since they rest on an unnamed/uncited external
   study (Claim 8's "Microsoft research") or a single unlinked, unverified
   tool reference (Claim 11's Kononov "modularity skill") respectively.
   This mirrors this corpus's treatment of comparable single- or co-authored
   Thoughtworks thought-leadership pieces without supporting data (e.g.,
   `blog-thoughtworks-harmellaw-nfr-guardrail.md`, also rated emerging
   overall for the same reason: a coherent, citable practitioner argument
   without measured backing).
