---
source_url: https://simonwillison.net/2026/May/14/not-so-locked-in/
source_type: blog-post
title: "Not so locked in any more"
author: Simon Willison
date_published: 2026-05-14
date_extracted: 2026-05-23
last_checked: 2026-05-23
status: current
confidence_overall: anecdotal
issue: "#871"
---

# Not So Locked In Any More

> Simon Willison documents a real-world case where AI coding agents changed the risk
> calculus of a major platform decision: a tech company completed an agent-driven
> iOS/Android → React Native rewrite and treated it as reversible because agents make
> "port back to native" a viable fallback — illustrating Mitchell Hashimoto's
> observation that programming language and platform lock-in is decreasing.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, May 14, 2026; a short reflective post
  connecting a first-person conference anecdote to a Mitchell Hashimoto quote. This is
  Willison's own editorial voice. The referenced Hashimoto quote appears on a linked
  Willison post at https://simonwillison.net/2026/May/14/mitchell-hashimoto/, which was
  read as a substantive linked page per MINER.md §1. Tags on the post: ai, react,
  generative-ai, llms, ai-assisted-programming, coding-agents.)
- **Author credibility**: Simon Willison is the creator of Django and one of the
  highest-signal independent AI tooling commentators; his link-blog selection is itself
  a relevance signal. He is reporting a direct first-person conference conversation with
  a practitioner. Mitchell Hashimoto (quoted via the linked post) is the co-founder and
  former CEO of HashiCorp (Terraform, Vagrant, Vault) and is commenting on Bun's
  Zig→Rust migration as a practitioner observer with rare commercial and technical
  depth.
- **Scope**: Covers one concrete practitioner case (iOS/Android → React Native agent
  rewrite framed as reversible) and one general Hashimoto observation (programming
  language/platform lock-in is decreasing). Does NOT cover: specific agent tools used,
  workflow details, time or cost metrics for the rewrite, team size, maintenance cost
  outcomes, or how teams should measure rewrite quality. The source is short — roughly
  eight sentences of content — so the extractable claim set is correspondingly small.

## Extracted Claims

### Claim 1: A medium-sized tech company completed an agent-driven rewrite of legacy iOS/Android apps to React Native

- **Evidence**: Willison's first-person account of a conference conversation with an
  employee at the company. No company name, agent tooling, or specific timeline given.
- **Confidence**: anecdotal
- **Quote**: "They told me they had just completed a coding-agent driven rewrite of both apps to React Native."
- **Our assessment**: The anecdote is credible as reported — Willison is relaying a
  specific first-person conversation, not an abstract claim. The absence of company
  name, specific agent tool, and timeline limits independent verification. Its primary
  value is as an existence proof: at least one mid-market company is treating major
  mobile platform rewrites as feasible via agents, enough to have actually executed one.

### Claim 2: The company justified the React Native decision with both technical merit and agent-enabled reversibility as a risk hedge

- **Evidence**: Willison reports a compound justification from the conference contact:
  (1) React Native has technically improved, AND (2) "port back to native" is viable
  via agents if needed. Willison's own question frames the context explicitly.
- **Confidence**: anecdotal
- **Quote**: "They said that React Native has improved a lot over the past few years and covered everything their apps needed to do."
- **Our assessment**: The two-part justification is the most analytically interesting
  element of the anecdote. Willison's question — "given that coding agents presumably
  drive down the cost of maintaining separate iPhone and Android apps" — implies that
  agents alone might have provided reason to stay on native. What agents added to the
  decision was not the primary technical case for React Native, but the risk hedge:
  reversibility. This framing is new — platform decisions have typically been justified
  on technical adequacy alone, not on fallback optionality.

### Claim 3: Coding agents make technology decisions more reversible — "port back to native" is now a viable fallback strategy

- **Evidence**: Direct quote from the conference contact as reported by Willison. The
  phrase "just port back" signals the person viewed agent-driven reversion as a
  realistic low-friction option.
- **Confidence**: anecdotal
- **Quote**: "if it turned out to be the wrong decision, they could **just port back to native** in the future."
- **Our assessment**: The word "just" is load-bearing. It signals that the contact
  views the reversion as straightforward rather than costly. Whether this perception
  accurately reflects the true rewrite cost at their app's scale is unknown — but the
  *perception* of reversibility was sufficient to influence the original decision. Even
  if a future reversion would actually be costly, teams that treat decisions as
  reversible take larger bets and recover faster when bets go wrong. This has
  significant implications for how organizations approach architectural risk under
  agent-assisted development.

### Claim 4: Programming language and platform lock-in is decreasing as AI coding agents lower the cost of rewrites

- **Evidence**: Mitchell Hashimoto quote, published the same day (May 14) and linked
  from the main post, discussing Bun's Zig→Rust migration as evidence of language
  fungibility. Willison invokes it to generalize from his conference anecdote.
  Two independent practitioner observations — the conference contact on mobile platform
  reversal, Hashimoto on language migration — point to the same mechanism.
- **Confidence**: emerging
- **Quote**: "Programming languages used to be LOCK IN, and they're increasingly not so."
  — Mitchell Hashimoto, as quoted on https://simonwillison.net/2026/May/14/not-so-locked-in/
- **Our assessment**: Hashimoto's claim is supported by the Bun case (a real production
  project that migrated from Zig to Rust) and Willison's conference anecdote. Neither
  is a controlled study, but they represent independent data points from practitioners
  operating at scale. The claim is plausible and directionally consistent with the
  cost-reduction logic of AI-assisted rewrites. The "increasingly" hedge acknowledges
  this is a trend, not yet a universal condition.

### Claim 5: The Bun JavaScript runtime's Zig→Rust migration demonstrates that core programming language choices can be executed or reversed in approximately one to two weeks with agents

- **Evidence**: Mitchell Hashimoto's May 14 quote (https://simonwillison.net/2026/May/14/mitchell-hashimoto/),
  the page linked from the source post. Bun is a real production JavaScript runtime
  that did execute a migration from Zig to Rust; the timeline is Hashimoto's estimate,
  not a documented project postmortem.
- **Confidence**: anecdotal
- **Quote**: "Bun has shown they can be in probably any language they want in roughly a week or two. Rust is expendable. Its useful until its not then it can be thrown out."
  — Mitchell Hashimoto, https://simonwillison.net/2026/May/14/mitchell-hashimoto/
- **Our assessment**: The "roughly a week or two" estimate is a practitioner estimate
  without citation. However, the Bun Zig→Rust migration is a publicly documented
  real-world event, making the rough timeline plausible for a well-defined codebase
  working with agents. The "Rust is expendable" framing signals a philosophical shift:
  previously, choosing a systems language was a permanent architectural commitment.
  Hashimoto is asserting that this permanence assumption breaks down with agents.
  Whether this generalizes beyond small-to-medium codebases at Bun's scale remains
  an open question — larger or less well-structured codebases likely have longer
  migration timelines.

## Concrete Artifacts

### The Source Post (verbatim, from https://simonwillison.net/2026/May/14/not-so-locked-in/)

```
Date: 14th May 2026
Tags: ai, react, generative-ai, llms, ai-assisted-programming, coding-agents

This Mitchell Hashimoto quote about Bun migrating from Zig to Rust reminded me of a
similar conversation I had at a conference last week.

I was talking to someone who worked for a medium sized technology company with a pair
of legacy/legendary iPhone and Android apps.

They told me they had just completed a coding-agent driven rewrite of both apps to
React Native.

I asked why they chose that, given that coding agents presumably drive down the cost of
maintaining separate iPhone and Android apps.

They said that React Native has improved a lot over the past few years and covered
everything their apps needed to do.

And... if it turned out to be the wrong decision, they could just port back to native
in the future.

Like Mitchell said:
"Programming languages used to be LOCK IN, and they're increasingly not so."
```

### The Mitchell Hashimoto Quote (verbatim, from https://simonwillison.net/2026/May/14/mitchell-hashimoto/)

```
"On the interesting side is how fungible programming languages are nowadays.
Programming languages used to be LOCK IN, and they're increasingly not so. You think
the Bun rewrite in Rust is good for Rust? Bun has shown they can be in probably any
language they want in roughly a week or two. Rust is expendable. Its useful until its
not then it can be thrown out. That's interesting!"

— Mitchell Hashimoto, discussing Bun's transition from Zig to Rust
```

## Cross-References

- **Corroborates**:
  - **blog-simonwillison-mitchell-hashimoto-tdm-dynamics.md** (Issue #816): The
    May 12 Hashimoto post documents lock-in as a structural organizational phenomenon
    (TDM procurement inertia, switching costs in the enterprise procurement chain). The
    current note provides evidence that the *technical* dimension of lock-in is
    decreasing. Both are from the same author on related but distinct aspects of lock-in:
    the TDM note's Claim 5 — "The cost (cognitive, time, risk, money, etc.) of adopting
    a new thing is significantly higher than expanding an old thing" — applies to
    organizational procurement; this note shows that at the technical rewrite level, costs
    are falling. These are complementary, not contradictory: organizational procurement
    inertia may persist even as technical reversibility improves.

- **Contradicts**: None filed. No existing corpus note asserts that technology lock-in is
  *increasing* or that major rewrites are becoming harder as a result of AI agents. The
  Shore note (blog-simonwillison-james-shore-maintenance-costs.md) argues that AI tools
  can increase maintenance costs in ongoing codebases, but that is a claim about the
  quality of AI-generated code over time, not about the feasibility of agent-driven
  rewrites as a strategic option. The two are addressing different questions and are
  complementary rather than contradictory.

- **Extends**:
  - **blog-simonwillison-mitchell-hashimoto-tdm-dynamics.md** (Issue #816): The TDM
    note documents the structural organizational sources of lock-in. This note identifies
    an emerging counterforce: agents reducing the technical switching cost that is one
    component of total lock-in. The guide should present both together — as agents lower
    technical rewrite costs, organizational and procurement inertia becomes the dominant
    remaining source of lock-in, which requires different mitigation strategies
    (advocacy framing, TDM risk-transfer arguments) rather than technical ones.
  - **blog-simonwillison-james-shore-maintenance-costs.md** (Issue #804), Claim 7:
    Shore identifies "maintenance-reducing AI tools" as a distinct beneficial category.
    Agent-driven rewrites to better-maintained platforms (as in this note's React Native
    case) represent Shore's maintenance-reduction category in action — rewriting to a
    unified platform could reduce the ongoing maintenance cost of two separate native
    codebases. However, this connection is speculative; the conference contact did not
    discuss maintenance cost outcomes of the React Native choice.

- **Novel**:
  - **Reversibility as a first-class technology decision factor**: No existing corpus
    source identifies agent-enabled reversibility as part of the *original* decision
    calculus for platform choices. Prior notes discuss AI adoption decisions and
    switching costs; this is the first to document a practitioner explicitly
    incorporating "we can undo this with agents" into the platform justification logic.
  - **The "just port back" mentality as a behavioral shift**: The word "just" signals a
    new default assumption about the difficulty of major rewrites — from "rare expensive
    last resort" to "feasible fallback option." This attitudinal shift has significant
    downstream implications for how organizations architect systems and take technology
    bets.
  - **The Bun Zig→Rust migration as a real-world language-fungibility data point**: The
    Hashimoto quote references a concrete, publicly documented real-world migration event
    as evidence for the general claim about decreasing language lock-in. This is the
    first corpus note to cite Bun's language migration as a data point.

## Guide Impact

- **Chapter 05 (Team Adoption — Technology Decision-Making Under Agent-Enabled Flexibility)**:
  This is the primary addition this source makes. Chapter 05 currently documents team
  adoption of AI tools but does not address how agents change the risk profile of
  technology platform choices. Specific recommendation: add a section on
  "Architecture Decisions Are More Reversible" using this anecdote as a case study.
  Teams making major platform choices (mobile frameworks, programming languages,
  infrastructure providers) should explicitly evaluate whether agent-driven reversibility
  changes their risk tolerance for a platform bet. Pair with the Hashimoto TDM note
  (blog-simonwillison-mitchell-hashimoto-tdm-dynamics.md) to note that organizational
  procurement inertia persists even as technical reversibility improves — teams must
  address both dimensions when making platform decisions.

- **Chapter 01 (Daily Workflows — Agents Enable Flexible Architecture)**:
  Practitioners advising on technology choices can now frame agent-assisted rewriting
  as a risk mitigation option, not just a productivity tool. "If this turns out to be
  wrong, we can rewrite it with agents" is a substantively new argument in architectural
  decision-making. The guide should acknowledge this as a real (if scale-dependent)
  consideration, with appropriate caveats about maintenance cost accumulation
  (cross-reference Shore).

- **Chapter 04 (Context Engineering — Enabling Large-Scale Rewrites)**:
  Agent-driven rewrites of the scale described (full mobile app rewrite, programming
  language migration) are enabled partly by effective context management. Teams
  maintaining good context infrastructure — comprehensive CLAUDE.md, architecture
  documentation, codebase maps — are better positioned to execute agent-driven
  rewrites when needed. This note provides a motivating use case for context engineering
  investment beyond daily productivity.

## Extraction Notes

- **Source is short**: The canonical URL contains approximately eight sentences of
  substantive content. Five claims are extracted — the natural limit given source
  length. The main contextual weight comes from the linked Hashimoto post
  (https://simonwillison.net/2026/May/14/mitchell-hashimoto/), read as a substantive
  linked page per MINER.md §1.
- **Cross-reference verification**: Both cross-referenced notes were fully re-read
  before cross-references were written:
  - blog-simonwillison-mitchell-hashimoto-tdm-dynamics.md Claim 5 (lines 138–153):
    "The cost (cognitive, time, risk, money, etc.) of adopting a new thing is
    significantly higher than expanding an old thing." — content confirmed to match
    the corroboration claim.
  - blog-simonwillison-james-shore-maintenance-costs.md Claim 7 (lines 166–177):
    "There's other levers to pull, such as AI that makes maintenance itself more
    productive, even if it doesn't make the code more maintainable." — content
    confirmed to match the extension claim.
- **No company name given**: The anecdote does not name the company, team, agent tool,
  or specific timeline. It cannot be independently verified; its value is as a
  credible practitioner-reported existence proof.
- **Mitchell Hashimoto May 14 post vs. May 12 post**: Two distinct Hashimoto posts
  are relevant to this corpus. The May 12 post (blog-simonwillison-mitchell-hashimoto-
  tdm-dynamics.md, Issue #816) addresses TDM procurement dynamics and Redis strategy.
  The May 14 post (https://simonwillison.net/2026/May/14/mitchell-hashimoto/) addresses
  Bun's Zig→Rust migration and programming language fungibility. Both quote Hashimoto
  on simonwillison.net; they address different aspects of lock-in from the same author.
- **Bold formatting in Claim 3 quote**: Willison rendered "just port back to native"
  in bold in the source post (markdown: **just port back to native**). The bold is
  preserved verbatim in the Claim 3 quote as it appears in the source.
