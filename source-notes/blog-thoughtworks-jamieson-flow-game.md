---
source_url: https://www.thoughtworks.com/insights/blog/agile-engineering-practices/modern-engineering-flow-game
source_type: blog-post
title: "Modern Engineering is a Flow Game"
author: Anne Jamieson (Principal Data Engineer, Thoughtworks)
date_published: 2026-06-02
date_extracted: 2026-07-01
last_checked: 2026-07-01
status: current
confidence_overall: anecdotal
issue: "#1386"
---

# Modern Engineering is a Flow Game

> Thoughtworks' Anne Jamieson reframes Agile engineering through a sports
> metaphor — waterfall as American football ("the game of the plan"), Agile
> as a flow game like soccer/hockey — and uses it to argue for "expert
> generalists" who deliberately "fill lanes" outside their specialty, anchored
> by a written playbook/North Star, with AI recast as an "assistant coach"
> that raises velocity but also raises the stakes of a hard guardrail: if a
> developer can't explain what they need built or what their code does, that
> code shouldn't ship.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, published 2026-06-02, filed via
  the trusted `thoughtworks` RSS feed)
- **Author credibility**: Anne Jamieson is identified in the piece's pull-quote
  as a Principal Data Engineer at Thoughtworks. Thoughtworks is a
  well-established global technology consultancy with a long public history of
  Agile/XP thought leadership (Martin Fowler's personal blog, syndicated
  separately, is hosted under the same `thoughtworks.com` domain but is a
  distinct source already represented in this corpus via
  `blog-fowler-fragments-2026-06-02.md` and related notes). This piece is not
  by Fowler and is not empirical research — it is a practitioner opinion/
  framework essay using an extended sports analogy, consistent with
  Thoughtworks' house style of pattern-naming essays (e.g. their Technology
  Radar). No data, survey, or case study is cited; the one external reference
  is to sports psychologist Dr. Saul Miller's book *Why Teams Win* for the
  "game of the plan" framing of traditional (waterfall) project structure.
- **Scope**: Covers a role/team-structure framework (expert generalist,
  filling the lane, playbook/North Star, ceremonies-as-drills, improvisation
  under pressure) and then applies AI specifically to that framework in two
  final sections ("AI as the assistant coach" and "The game plan"). Does NOT
  cover: specific tooling, harness configuration, measured productivity data,
  team-size scoping, or hiring/compensation implications. The AI-specific
  content is concentrated in roughly the final third of the piece.

## Extracted Claims

### Claim 1: Traditional waterfall engineering, likened to American football's "game of the plan," produces monotony, slow feedback loops, and burnout because engineers are locked into fixed positions waiting for handoffs
- **Evidence**: Author's framing, citing sports psychologist Dr. Saul Miller's book *Why Teams Win* for the football/"game of the plan" terminology, then applying it to software team structure.
- **Confidence**: anecdotal
- **Quote**: "Traditional engineering follows a \"waterfall\" approach, most likened to American football, which sports psychologist Dr. Saul Miller calls \"the game of the plan\" in his book, Why Teams Win. [...] The downside for the engineer is the monotony of only ever solving one type of problem, the constant waiting for the next handoff and the lack of systemic understanding that leads to slow feedback loops and burnout."
- **Our assessment**: This is scene-setting rather than a load-bearing claim — a rhetorical contrast to motivate the flow-game framing that follows. The burnout/monotony diagnosis is asserted, not measured, and is a fairly standard critique of waterfall already well established in Agile literature generally. Its main function in the piece is as the foil for Claim 2.

### Claim 2: Modern software engineering is better modeled as a "flow game" (soccer/hockey) than a "game of the plan" (football) — success comes from "filling lanes" rather than "staying in one's lane," while still maintaining a clear, fixed direction
- **Evidence**: Author's central metaphor, elaborated across the whole piece.
- **Confidence**: anecdotal
- **Quote**: "The players on the field should know the playbook, but it's not unheard of for a forward to hop into a defender's spot mid-play. [...] success comes from maintaining a clear, fixed direction while embracing adaptable, flexible roles (\"filling lanes\") to reach that goal efficiently in a non-linear environment."
- **Our assessment**: This is the organizing thesis of the whole essay; every other claim is either an elaboration of it (expert generalist, filling the lane, playbook/North Star) or an application of it to AI. As a metaphor it is not falsifiable, but the specific tension it names — specialization plus flexible role-filling, anchored by a shared fixed goal — is a coherent, guide-relevant framing distinct from a generic "be agile" statement.

### Claim 3: The "expert generalist" — someone with deep domain knowledge who also has the flexibility and systemic view to contribute across the non-linear development process — is an especially key skillset in modern engineering
- **Evidence**: Author's direct definitional claim, immediately followed by a caveat that specialized roles (infrastructure, DevOps, security engineers as "defense"; front-end/product engineers as "forwards") still exist within the model.
- **Confidence**: anecdotal
- **Quote**: "The \"expert generalist\" is a unique professional who delivers deep domain knowledge but also possesses the flexibility and systemic view to contribute across the non-linear development process; this is an especially key skillset in modern engineering."
- **Our assessment**: The explicit qualifier that generalism means "deep + flexible," not "shallow everywhere," is the same precision Andrew Ng makes independently in `blog-thebatch-ng-aiteam-structure.md` (Claim 7: "deep + broad," not "shallow everywhere") — two independently authored sources converging on the same distinction, though Ng scopes his claim to 2–10 person teams and ties it explicitly to AI-driven capacity headroom, while Jamieson does not scope by team size and frames it as a general property of Agile/flow-based work, only later layering AI onto it.

### Claim 4: "Filling the lane" is a deliberate, targeted act to solve an emergent bottleneck, explicitly distinct from the "capacity-driven development" anti-pattern of taking on unrelated work merely to maximize resource utilization
- **Evidence**: Author's explicit contrast, with a worked example (a front-end engineer spending an afternoon tuning database queries during a security audit) and a named anti-pattern to distinguish it from.
- **Confidence**: anecdotal
- **Quote**: "It is critical to distinguish this practice from the capacity-driven development anti-pattern. Filling the lane is a deliberate, targeted act focused solely on solving emergent bottlenecks within the team's current product or stream to unblock the core mission. Unlike capacity-driven development, which increases cognitive load by taking on external work simply to maximize resource utilization, filling the lane is driven by systemic need and maintains focus on the team's existing goal."
- **Our assessment**: This is the most operationally precise claim in the piece — it gives a concrete decision rule ("is this solving a bottleneck in our own stream, or am I just picking up unrelated work to look busy?") rather than a vague exhortation to "be a team player." No other corpus source names "capacity-driven development" as an anti-pattern; this is a genuinely new distinction worth preserving verbatim rather than folding into a generic "generalist" recommendation.

### Claim 5: A documented team mission statement/"North Star" and a written playbook (development standards, deployment processes, technology frameworks) are necessary preconditions for role-filling to work, because without them the person holding the tacit knowledge becomes a silo
- **Evidence**: Author's direct argument for why the playbook must exist and be written down, distinguishing "mission statement" (tactical, phase-specific) from "North Star" (overarching, program-level) as related but sometimes distinct artifacts.
- **Confidence**: anecdotal
- **Quote**: "Without these artifacts in a common format which can be viewed by any team member at any time, there is a risk of divergence among the team's understanding of and approach to the work. It also means that whoever has the true source of this information poses as a silo to the project and will likely have to repeat themselves several times as they convey this information to the team. Do yourself a favour and write it down."
- **Our assessment**: The mechanism named here — undocumented context makes one person a bottleneck who must repeat themselves — is the team-level version of the individual-level argument in `blog-addyosmani-intent-debt.md` (Claim 4: agents carry none of the tacit intent humans build up over years, so un-externalized intent that used to cost a team "once in a while, at onboarding or after someone left" now compounds every session). Jamieson's version predates and doesn't mention AI in this specific section — it's presented as a general flow-game precondition — but the underlying logic (undocumented tacit knowledge = a silo that must repeatedly retransmit itself) is the same argument Osmani makes for why AI-native teams specifically can no longer tolerate it.

### Claim 6: Sprint ceremonies and retrospectives function as "drills" — the mechanism by which the broader team gains the cross-disciplinary awareness needed to fill another lane, distinct from ticket-completion as the measure of success
- **Evidence**: Author's direct argument, framing ceremonies as skill-building repetitions analogous to sports drills rather than as status-reporting rituals.
- **Confidence**: anecdotal
- **Quote**: "Sprint ceremonies and retrospectives are essential for building the systemic context required to play the flow game. Just as drills exist for specialized positions, these ceremonies ensure the broader group gains the cross-disciplinary awareness needed to \"fill another lane\". Success isn't just about each individual finishing their own tickets; it's ensuring the entire solution crosses the goal line."
- **Our assessment**: This reframes standard Agile ceremonies (already near-universal practice) with a specific purpose — systemic-context building for role-filling — rather than the more common justifications (status visibility, process improvement). It's a useful secondary justification for ceremonies the guide likely already recommends, similar in structure to how Kent Beck's `blog-kentbeck-trust-factory.md` (Claim 3) reframes XP practices as trust-building mechanisms in addition to their usual productivity justification. Neither claim invalidates the other; both add a second "why" to already-standard practices.

### Claim 7: AI functions as an "assistant coach" for developers — reviewing code for security holes and inefficiencies faster and more consistently than human review alone, and analyzing project backlogs to surface cross-team bottlenecks and calibrate sprint goals
- **Evidence**: Author's direct claim, applying the flow-game/coaching metaphor specifically to AI's role once humans are still the primary code producers.
- **Confidence**: anecdotal
- **Quote**: "Checking for holes in the defense (security vulnerabilities) or stronger offense (more efficient queries) can be done faster on more lines of code and in a more consistent manner than relying on human reviews alone."
- **Our assessment**: This is an assertion about AI code review capability (faster, more consistent than human-only review) without evidence — no benchmark, no named tool, no measured false-positive/false-negative rate. It is directionally consistent with corpus claims about AI-assisted review as a volume multiplier (e.g. the code-review bottleneck convergence documented in `blog-bvp-shopify-ai-playbook.md` Claim 4), but should be cited as an asserted capability claim, not a validated one — notably, Shopify's own VP of Engineering is explicitly skeptical that AI writes or reviews more securely (`blog-bvp-shopify-ai-playbook.md` Claim 9), which tempers how confidently this claim should be repeated in the guide.

### Claim 8: Over-reliance on AI weakens a team's posture; the concrete guardrail is that if a developer cannot explain what they need built or what their AI-generated code is doing, that code should not be used
- **Evidence**: Author's direct prescriptive claim in the "AI as the assistant coach" section, framed as a hard condition rather than a soft recommendation.
- **Confidence**: anecdotal
- **Quote**: "Despite all the benefits of AI, an over-reliance on it will weaken the posture of a team. While assistant coaches are important pieces of a team's success, the players must still play the actual game. An over-reliance on vibe coding introduces security, architectural and requirements risks. If developers cannot explain what they need to code, or what their code is doing, that code should not be used."
- **Our assessment**: This is the single most guide-actionable claim in the piece — a concrete, binary veto condition ("can you explain it? no? don't ship it") rather than a vague warning about over-reliance. It converges strongly with two independent senior-practitioner sources already in the corpus: Farhan Thawar's comprehension-debt warning at Shopify (`blog-bvp-shopify-ai-playbook.md` Claim 8, "The brain is a muscle. If you stop using your brain — it will atrophy") and Simon Willison's accountability-gap argument (`blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 3, AI agents lack the professional accountability that makes trusting-without-reviewing human teams acceptable). Three independent sources now converge on developer comprehension as the primary AI-adoption guardrail, each stating the mechanism slightly differently: Shopify frames it as skill atrophy, Willison frames it as an accountability gap, Jamieson frames it as an explainability precondition for shipping. This is a strong three-source convergence worth citing together.

### Claim 9: AI has amplified the flow-game nature of software engineering to unprecedented velocity, recasting the developer as a "playmaker" who must constantly read the play and supply the AI with precise context for its next move
- **Evidence**: Author's direct claim describing the changed tempo of development under AI assistance.
- **Confidence**: anecdotal
- **Quote**: "AI has amplified the flow game nature of modern software engineering to another level; it is faster, more continuous, and more intense than anything developers have experienced before. [...] For the developer to act as the ultimate playmaker, they must constantly 'read the play', anticipate the next move, and provide the AI with the precise context it needs to execute its next rapid-fire pass."
- **Our assessment**: This "playmaker/director" framing of the developer's role is the same shift documented from the job-market side in `discussion-hn-agentic-coding-jobs.md` (Claim 1, the Zapier posting: "Your daily development workflow is built around directing and reviewing agent-written code, not writing it by hand"). Jamieson supplies the sports-metaphor vocabulary for the same underlying role change the Zapier posting states as a literal hiring requirement — worth pairing the two in the guide as a conceptual framing (Jamieson) plus a market-evidence data point (Zapier) for the same claim. Note the tonal contrast with Kent Beck's `blog-kentbeck-trust-factory.md`: Beck's explicit prescription is to deliberately *slow down* AI-augmented development to preserve trust (Claim 9 there: "Slow development to ensure that the damn stuff actually works"), while Jamieson frames continuous, high-tempo AI-assisted flow positively. The two are not a filing-worthy contradiction — Jamieson pairs the high-tempo framing with her own hard guardrail (Claim 8 here), which functions similarly to Beck's trust-building brakes — but the difference in emphasis (embrace the tempo vs. deliberately resist it) is worth flagging if the guide cites both in the same section.

### Claim 10: Asking AI follow-up questions about its own generated code and design choices builds developer comprehension of the overall system and is available to technical and non-technical roles alike
- **Evidence**: Author's direct recommendation, framed as a way to accelerate the contextual awareness needed for "filling the lane."
- **Confidence**: anecdotal
- **Quote**: "AI should be used to build stronger comprehension of the overall system, vital for the flow game, for developers. [...] Technical and non-technical roles alike can benefit from asking the AI follow-up questions. Why did it choose a certain pattern? Can it rehearse complex architectural decisions? This capability accelerates learning and ensures system alignment, providing the contextual awareness and confidence necessary to maintain flow."
- **Our assessment**: This is presented as a mitigation for Claim 8's comprehension-debt risk — using the AI itself to interrogate its own rationale. It is a plausible but unverified claim, and it sits in some tension with `blog-addyosmani-intent-debt.md` (Claim 2: an agent cannot generate true intent, it can only infer a plausible-sounding rationale from the code, which "is not the same as the actual intent" and "will invent a confident-sounding reason, which is worse than admitting it doesn't know"). Jamieson recommends asking the AI "why did it choose a certain pattern" as a comprehension-building technique; Osmani's post argues the AI's answer to exactly that question is likely to be a fabricated, confident-sounding guess rather than the real rationale, particularly for design decisions predating the current session. This is a genuine point of tension between two corpus sources on a load-bearing practice recommendation (should teams trust AI's self-reported rationale for its own code?) — flagged here rather than in a filed contradiction issue, because Jamieson's claim is thin (one sentence, no worked example of what "asking why" actually surfaces) and doesn't rise to a fully-formed, evidenced position that materially opposes Osmani's more developed mechanism. The guide should lean toward Osmani's more specific caveat when the two are in tension: AI follow-up questions may build comprehension of *what* the code does, but should not be trusted as a source of *why* it was originally written that way, especially for legacy or multi-session code.

## Concrete Artifacts

### Playbook components (as named in the piece)
```
Source: Anne Jamieson, "Modern Engineering is a Flow Game," Thoughtworks
Insights, 2026-06-02

The key components of a playbook include:
- Documented development standards
- Deployment processes
- Technology frameworks
```

### Filling-the-lane worked example
```
Source: same as above

"Imagine a front-end engineer notices performance issues in the data layer
during a security audit. Instead of waiting for the data team to finish
their sprint, the front-end engineer dedicates an afternoon to tuning a
couple of key queries. They temporarily 'filled the data lane' to keep the
product moving."
```

### Rigid vs. flowing player under pressure (dependency-risk example)
```
Source: same as above

"[A] rigid player sees that the dependency defined in the original design
document (the 'Playbook') is unstable and will introduce significant
long-term risk. They continue coding against the flawed dependency, waiting
for a formal architecture review that may delay the project. The flowing
player, however, proactively documents the risk, selects and implements a
proven alternative, and immediately communicates the change to stakeholders,
ensuring the team stays aligned with the overall North Star of long-term
system stability."
```

### Closing action items ("The game plan")
```
Source: same as above

"The first step toward mastering the flow game is to schedule a team meeting
to draft your project's North Star or mission statement, and ask your
engineers to identify one 'lane' they will practice filling this sprint."
```

## Cross-References

- **Corroborates**:
  - `blog-thebatch-ng-aiteam-structure.md` (Claim 7): Ng's "deep + broad, not
    shallow everywhere" clarification of the generalist model matches
    Jamieson's Claim 3 "expert generalist" definition almost exactly, arrived
    at independently by a different author in a different genre (editorial
    letter vs. sports-metaphor essay).
  - `blog-bvp-shopify-ai-playbook.md` (Claim 8) and
    `blog-simonwillison-vibe-coding-agentic-engineering.md` (Claim 3): both
    converge with this note's Claim 8 (comprehension/explainability as the
    AI-adoption guardrail) — see Claim 8's assessment above for the three-way
    comparison.
  - `discussion-hn-agentic-coding-jobs.md` (Claim 1): the Zapier job posting's
    "directing and reviewing agent-written code, not writing it by hand" is
    the job-market evidence for the same developer-as-director role shift
    Jamieson names with the "playmaker" metaphor in Claim 9.
  - `blog-addyosmani-intent-debt.md` (Claim 4): Osmani's claim that agents
    carry none of the tacit intent humans accumulate, making undocumented
    context newly costly, is the AI-specific version of the general
    silo-risk argument in this note's Claim 5 (written playbook prevents any
    one person from being a repeat-yourself bottleneck).

- **Extends**:
  - `blog-kentbeck-trust-factory.md`: Beck's XP-practices-as-trust-building
    reframing (Claim 3) is structurally the same move as this note's Claim 6
    (ceremonies-as-drills) — both add a second justification to already-
    standard Agile practices. Beck's essay also creates a tonal tension with
    this note's Claim 9 (embrace continuous high-tempo AI-assisted flow vs.
    Beck's explicit prescription to deliberately slow down) — noted in
    Claim 9's assessment but not filed as a contradiction; both sources pair
    their velocity claims with their own guardrails (Beck: four slow-down
    practices; Jamieson: the explainability veto in Claim 8) and neither
    source's guardrail is incompatible with the other's.

- **Contradicts**: None filed. The closest candidate — Claim 10's "ask the AI
  why it chose a pattern" recommendation vs. `blog-addyosmani-intent-debt.md`
  Claim 2's argument that AI-reported rationale is fabricated, not inferred —
  is noted in Claim 10's assessment as a genuine point of tension, but
  Jamieson's claim is a single unsupported sentence, not a developed position,
  so it does not meet the bar in MINER.md §4a for filing a contradiction
  issue (a real claim on each side that would lead to different guide advice).
  If a future source makes the "ask the AI why" recommendation with actual
  supporting detail, this should be revisited.

- **Novel** (not present elsewhere in the corpus):
  - The football (waterfall) vs. flow-game (Agile) sports metaphor itself,
    and the specific vocabulary it introduces: "expert generalist," "filling
    the lane," "capacity-driven development" (named anti-pattern),
    ceremonies-as-"drills," AI as "assistant coach."
  - The explicit naming and definition of "capacity-driven development" as an
    anti-pattern distinct from legitimate lane-filling (Claim 4) — no other
    corpus source names this specific failure mode.
  - The "North Star" vs. "mission statement" distinction (tactical/
    phase-specific vs. overarching/program-level) as two related but
    sometimes-distinct artifacts (Claim 5).

## Guide Impact

- **Chapter 05 (Team Adoption)**: Claim 4 ("filling the lane" vs.
  "capacity-driven development") gives the guide a concrete decision rule for
  when a generalist's role-hopping is healthy vs. an anti-pattern — currently
  the corpus's generalist-model content (via `blog-thebatch-ng-aiteam-structure.md`)
  argues *for* generalism but doesn't name the failure mode of doing it for
  the wrong reason. Recommend adding this distinction to any section
  recommending expert-generalist team structures.

- **Chapter 05 (Team Adoption)**: Claim 5 (written playbook/North Star as
  precondition for role-filling) supports and slightly predates the
  AI-specific "intent debt" argument already slated for Chapter 00/02 via
  `blog-addyosmani-intent-debt.md`. Recommend citing both together: Jamieson
  supplies the team-structure rationale (undocumented context = a human
  silo), Osmani supplies the AI-specific compounding-cost mechanism.

- **Chapter 01 (Daily Workflows) or Chapter 03 (Safety/Verification)**: Claim
  8 (the explainability veto — "if developers cannot explain what they need
  to code, or what their code is doing, that code should not be used") is a
  strong, quotable, three-source-corroborated guardrail (alongside Shopify
  and Willison). Recommend the guide state this as a named, binary review
  gate rather than a soft warning about "understanding your code."

- **Chapter 04 (Context Engineering)**: Claim 10 (asking AI "why" it chose a
  pattern) should be cited with the caveat surfaced in this note's
  cross-reference to `blog-addyosmani-intent-debt.md` Claim 2 — useful for
  understanding *what* generated code does, but not a reliable source of the
  *original* rationale, especially across sessions or on inherited code. The
  guide should not present "just ask the AI why" as a substitute for written
  intent capture.

## Extraction Notes

- The full article was retrieved via a single WebFetch pass of the source
  URL; the page is a self-contained blog post with no sub-pages substantive
  enough to warrant following per MINER.md §1. All quotes above were checked
  against the fetched article text.
- The piece has a relatively thin evidentiary base for a sports-metaphor
  essay: one named external reference (Dr. Saul Miller's *Why Teams Win*) for
  the football/"game of the plan" framing, and otherwise entirely the
  author's own conceptual argument with worked hypothetical examples (no
  named companies, no data, no case studies). All claims are graded
  `anecdotal` individually and the overall confidence is set to `anecdotal`
  accordingly — the value of this source is in its vocabulary and framing,
  which independently corroborates claims already present elsewhere in the
  corpus with harder evidence (Shopify, Ng, Willison, Osmani, the Zapier
  posting), not in new empirical content.
- One point of tension was identified with `blog-addyosmani-intent-debt.md`
  (Claim 10 here vs. that note's Claim 2) but was judged too thin on
  Jamieson's side to meet the MINER.md §4a bar for filing a contradiction
  issue. See the Cross-References → Contradicts section for reasoning.
- No sub-pages, PDFs, or linked reports were part of this source; it is a
  single self-contained blog post.
