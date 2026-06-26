---
source_url: https://simonwillison.net/2026/Jun/17/charity-majors/
source_type: blog-post
title: "Quoting Charity Majors on the economics of code production"
author: Charity Majors (excerpted by Simon Willison)
date_published: 2026-06-17
date_extracted: 2026-06-26
last_checked: 2026-06-26
status: current
confidence_overall: emerging
issue: "#1316"
---

# Quoting Charity Majors: Code Economics Turned Upside Down

> Charity Majors names the supply-side economic inversion underlying all current AI
> engineering tension: code generation shifted from expensive and time-consuming to free
> and instant in 2025, inverting code's status from capital asset (treasured, reused,
> curated) to consumable (disposable, regenerable) — and argues this demands *more*
> engineering discipline, not less.

## Source Context

- **Type**: blog-post (Simon Willison link-blog post, June 17, 2026; a brief quote excerpt
  with attribution. Willison excerpts two passages from Charity Majors' Substack article
  "AI demands more engineering discipline. Not less." Tags on the Willison post: ai,
  charity-majors, generative-ai, llms, ai-assisted-programming. The Substack article
  returned HTTP 403 Forbidden on direct fetch — the Willison page is the only accessible
  version of this content.)
- **Author credibility**: Charity Majors is co-founder and CTO of Honeycomb (the
  observability platform for distributed systems) and co-author of *Database Reliability
  Engineering* (O'Reilly). Her commentary on engineering economics and code quality
  consequences carries strong authority from a practitioner who has spent her career
  studying what happens to systems under reliability strain. Simon Willison is the creator
  of Django and one of the highest-signal independent AI tooling commentators; his
  selection of this piece for his curated feed is itself a relevance signal.
- **Scope**: The accessible content (two blockquoted passages on the Willison page) covers
  the economic diagnosis of what changed in 2025: code generation cost and code's
  capital/consumable status. The article title ("AI demands more engineering discipline.
  Not less") indicates the accessible passages are a foundation for arguing increased
  engineering discipline is required. Specific recommendations from the full Substack
  article are not accessible. Does NOT cover (from accessible content): specific practices,
  tooling configurations, team structures, or empirical data.

## Extracted Claims

### Claim 1: In 2025, the economics of code production were turned upside down — generation shifted from expensive and time-consuming to effectively free and instant

- **Evidence**: Charity Majors' direct statement, excerpted by Willison. Majors names 2025
  as a specific historical inflection point — a before/after claim about the economics of
  software production, not a gradual trend.
- **Confidence**: emerging (Majors is a high-credibility authority on engineering
  economics; the claim is consistent with multiple corpus measurements of velocity gains —
  Miller et al.'s 281% first-month LOC spike, Willison's 10× throughput estimate — but
  Majors' claim is a characterization of systemic economics, not a measured result)
- **Quote**: "What happened in 2025 was this: the economics of code production were turned
  upside down. Instead of being very hard, time-consuming, and expensive to generate code,
  it became effectively free and instant."
- **Our assessment**: "Turned upside down" is a stronger claim than "improved
  significantly." Majors asserts a qualitative category shift, not a quantitative
  improvement. The distinction matters: if code generation is merely cheaper, engineering
  practices can scale down proportionally. If it is "effectively free and instant," the
  constraint moves entirely to other activities — design, verification, maintenance,
  comprehension — and practices calibrated to "expensive code" become miscalibrated. This
  is the conceptual foundation for why AI adoption requires organizational and process
  restructuring, not just tool adoption. Consistent with Willison's framing that the SDLC
  was designed around code-as-bottleneck, which is now obsolete.

### Claim 2: The economic shift happened "practically overnight" — a rapid, discontinuous transition in 2025, not gradual evolution

- **Evidence**: Majors' phrasing "practically overnight" in the second passage, together
  with the specific year "2025" named in the first passage. This implies the shift was
  sudden enough to outpace organizational adaptation.
- **Confidence**: emerging (single-author characterization; consistent with corpus sources
  that independently observe similar shifts in the same timeframe, including the June 4
  Majors source and Willison's May 2026 vibe-coding post)
- **Quote**: "Lines of code went from being treasured, reused, cared for and carefully
  curated, to being disposable and regenerable, practically overnight."
- **Our assessment**: "Practically overnight" matters because it implies organizational
  structures, engineering norms, and individual habits calibrated for one economic reality
  now operate in a different one without time to adapt. The June 4 Majors source argues
  that the enthusiast/skeptic tension persists because "there is no natural feedback loop
  connecting enthusiasts with skeptics"; this rapid-transition framing explains *why* no
  feedback loop had time to form. When economic conditions change over years, organizations
  adapt incrementally; when they change over months, the gap between old norms and new
  economics is maximally wide. The speed of the shift is itself a structural risk factor,
  independent of the direction of change.

### Claim 3: Code's epistemic status shifted from capital asset ("treasured, reused, cared for and carefully curated") to consumable ("disposable and regenerable")

- **Evidence**: Majors' direct contrast of the two states, embedded in the second passage.
  The vocabulary is deliberate and parallel: the pre-2025 vocabulary (treasured, reused,
  cared for, curated) describes a capital asset maintained for long-term value; the
  post-2025 vocabulary (disposable, regenerable) describes a consumable reproduced on
  demand.
- **Confidence**: emerging (this is a conceptual characterization, not a measured outcome;
  but the contrast is precise and the vocabulary is Majors' own)
- **Quote**: "Lines of code went from being treasured, reused, cared for and carefully
  curated, to being disposable and regenerable, practically overnight."
- **Our assessment**: The capital-to-consumable shift is the most specific and novel
  contribution in the accessible content. It names the *behavioral consequence* of the
  economics shift: if code is free to regenerate, the rational response to imperfect code
  changes from "fix and maintain" to "discard and regenerate." This is not necessarily
  wrong — but it changes what engineering practices deliver value. Practices designed to
  maximize code reuse and minimize regeneration (DRY principles, library investment,
  extensive documentation) were optimal when code was expensive. Practices designed to
  maximize comprehension speed and testability become more important when code is
  disposable. Majors' choice of "treasured" and "curated" implies the old practices had
  genuine value that the economics shift risks discarding alongside the code.

### Claim 4: The article title indicates that engineering discipline should increase, not decrease, in response to the economic inversion

- **Evidence**: The title of the Substack article being excerpted: "AI demands more
  engineering discipline. Not less." This is Majors' explicit framing; the economic claims
  in the accessible excerpt are the foundation for the argument the title announces.
- **Confidence**: anecdotal (the title is accessible but the full argument is not; this is
  an inference about the article's normative direction, not a documented body claim)
- **Quote**: (no direct body quote available; article title: "AI demands more engineering
  discipline. Not less")
- **Our assessment**: The title is a direct rebuttal of the attitude that "code is free,
  so standards matter less." Majors argues the economic shift makes discipline *more*
  important, not less: disposable code accumulates without curation, and regenerable code
  does not automatically regenerate with comprehensibility or maintainability. This
  normative claim aligns with Shore's maintenance cost argument and the Miller et al.
  finding that AI adoption persistently increases complexity — the economic ease of
  generation does not reduce the disciplinary requirements for producing good code. It may
  increase them, because the volume of code requiring discipline-checking is larger.

## Concrete Artifacts

### Verbatim Passages from Willison's Page

```
Source: Simon Willison, https://simonwillison.net/2026/Jun/17/charity-majors/
(excerpting Charity Majors, Substack: "AI demands more engineering discipline. Not less")
Published: 17th June 2026
Tags: ai, charity-majors, generative-ai, llms, ai-assisted-programming

[Passage 1 — The Economics Inversion:]
"What happened in 2025 was this: the economics of code production were turned upside down.
Instead of being very hard, time-consuming, and expensive to generate code, it became
effectively free and instant."

[Passage 2 — Capital Asset to Consumable:]
"Lines of code went from being treasured, reused, cared for and carefully curated, to being
disposable and regenerable, practically overnight."

[Article title, as attributed by Willison:]
"AI demands more engineering discipline. Not less"
```

### The Capital-to-Consumable Vocabulary Shift

```
Code status before 2025 (Charity Majors via Willison, June 17, 2026):
  Adjectives: "treasured," "reused," "cared for," "carefully curated"
  Model: capital asset (maintained for long-term value)

Code status after 2025:
  Adjectives: "disposable," "regenerable"
  Model: consumable (reproduced on demand)

Timeframe of transition: "practically overnight"
Economic characterization: "effectively free and instant" to generate
Named inflection year: 2025
```

## Cross-References

- **Corroborates**: `blog-simonwillison-charity-majors-enthusiast-skeptic.md` Claim 4
  ("Velocity without comprehension is the specific failure mode — the problem is code
  shipped faster than engineers can read it") and Claim 2 ("The current AI adoption cycle
  is different from normal technology cycles — waiting creates an existential competitive
  risk") — this June 17 source provides the *economic foundation* for those organizational
  claims. The June 4 piece names what happens when code is shipped "faster than engineers
  can read it"; this June 17 piece names *why* that is happening economically. Together,
  the two Majors sources form a causal chain: economics changed (June 17) → organizational
  tension and failure modes emerged (June 4).

- **Corroborates**: `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 7
  ("The SDLC was designed for ~200 LOC/day and does not scale to 2,000 LOC/day — every
  downstream process breaks") and Claim 8 ("The SDLC disruption implies that design
  processes need to operate faster and at lower cost per iteration, because code is no
  longer the expensive step") — Willison documents the SDLC-throughput expression of the
  same economics shift Majors names directly. Majors describes the supply-side cause (code
  generation became free); Willison describes the SDLC-disruption effect (the whole
  process broke because it was calibrated for expensive code). The two sources describe
  the same economic reality from different vantage points.

- **Corroborates**: `blog-simonwillison-james-shore-maintenance-costs.md` Claim 1 ("AI
  coding agents only produce a net productivity benefit if they reduce maintenance costs by
  exactly the inverse of their productivity gain ratio") — Shore's inverse maintenance cost
  requirement is the mathematical downstream consequence of what Majors names. If code is
  "effectively free" to generate, teams will generate at high volume; unless maintenance
  cost per unit drops proportionally, the total maintenance burden compounds. Majors names
  the supply shift; Shore models its economic consequence.

- **Corroborates**: `paper-miller-speed-cost-quality.md` Claim 1 ("Cursor adoption causes
  a 281.3% increase in lines added in month 1, 48.4% in month 2, then disappears") — the
  empirical velocity spike is the direct measurement of the economics shift Majors
  characterizes. A 281% increase in lines added in the first month is precisely what
  "effectively free and instant" code generation produces in practice. The claim that code
  became "disposable and regenerable" is behaviorally evidenced by teams generating at
  that rate.

- **Extends**: `blog-simonwillison-charity-majors-enthusiast-skeptic.md` — the June 4
  Majors source addresses the *organizational tension* created by the transition; this June
  17 source names the *economic cause* of that tension. The June 4 piece is the symptom
  diagnosis; this June 17 piece is the etiology. The guide should present these as a
  two-piece explanation: disposable-code economics (June 17) → organizational
  enthusiast/skeptic split with no feedback loop (June 4).

- **Extends**: `blog-anthropic-ai-native-engineering-org.md` Claim 1 ("Verification, code
  review, and security replaced code-writing as the primary bottlenecks when agentic
  coding became the default") — Fung's organizational observation at Anthropic is the
  process-level consequence of what Majors describes economically. When code generation is
  free, writing code is no longer the constraint; verification and review become the
  constraint. The Majors economic framing is the "why" behind the Fung bottleneck
  observation.

- **Novel** (not present in any existing corpus note):
  - **Supply-side framing of the economics shift**: No existing corpus note names code
    generation *cost* (supply side) as the key variable that changed. Willison documents
    the SDLC throughput disruption; Shore documents maintenance cost consequences; Miller
    measures velocity spikes; Fung documents bottleneck shifts. Majors names the root:
    generation became free, and that is the cause of all the downstream effects the
    corpus has been documenting.
  - **Capital-asset-to-consumable vocabulary**: "Treasured, reused, cared for and carefully
    curated" → "disposable and regenerable" is entirely new vocabulary for the corpus. It
    names what changed about how teams *relate* to code, not just how fast they produce it.
    No existing source uses this asset-vs-consumable taxonomy.
  - **"Practically overnight" as a named risk factor**: The speed of the transition — not
    just its direction — is new to the corpus. If the shift had happened gradually,
    organizations would have adapted incrementally. "Practically overnight" names the
    adaptation gap as a specific structural problem, separate from the economic change
    itself.
  - **"AI demands more engineering discipline. Not less" as a direct normative claim**:
    While the corpus documents consequences of reduced discipline (complexity increases,
    maintenance burdens), no source states the normative counter-position this directly.
    This is the first corpus source to argue that the disposability economics specifically
    increase, rather than reduce, the required level of engineering discipline.

## Guide Impact

- **Chapter 00 (Principles — Root Cause of the AI Engineering Transition)**: This source
  provides the most economically precise foundation for why the guide exists. The guide
  should anchor its framing on Majors' supply-side claim: the practices described in the
  guide are responses to an economics shift, not arbitrary new preferences. Add to
  principles: code generation became "effectively free and instant" in 2025; this is the
  root cause of every downstream disruption the guide addresses — not a new feature of a
  familiar trend, but a qualitative economic inversion.

- **Chapter 02 (Fundamentals — Code Curation and Reuse)**: Claim 3 (capital-to-consumable
  shift) directly challenges guide advice calibrated to "treasured, curated" code
  assumptions. If code is disposable and regenerable, recommendations about library
  investment depth, DRY enforcement, and documentation density need to be revisited
  through a cost/value lens. Recommend adding: practices that maximize comprehension speed
  and testability may deliver more value than practices that minimize code replication, when
  code is cheap to generate but expensive to understand. Pair with Shore's maintenance cost
  framework for the quantitative argument.

- **Chapter 04 (Engineering Patterns — Economic Foundations)**: The three-source cluster
  (Majors economics + Shore maintenance model + Miller empirical data) is the most complete
  account in the corpus of why AI-native engineering requires different practices. Recommend
  a dedicated "Economics of AI-native code" section: Majors names the supply shift; Shore
  quantifies the maintenance cost consequence; Miller measures the quality outcome. All
  three sources point to the same conclusion: treating generated code as a costless
  consumable is economically rational in the short term but accumulates compounding
  maintenance debt in the long term.

- **Chapter 05 (Team Adoption — Framing the Transition)**: The capital-to-consumable
  vocabulary is actionable framing for team adoption conversations. Recommend using
  Majors' vocabulary when explaining why adoption requires process change: "Code went from
  being treasured and curated to disposable and regenerable. Processes built for the first
  reality don't work in the second." This is more precise than "AI is faster" because it
  locates the change in economics, not just in tools, and explains *why* verification and
  comprehension bottlenecks emerged.

## Extraction Notes

- The primary source (Charity Majors' Substack at charitydotwtf.substack.com, article
  "AI demands more engineering discipline. Not less") returned HTTP 403 Forbidden on
  direct fetch — consistent with the June 4 Majors source note (issue #1167), which also
  found the Substack inaccessible. All extraction is limited to the two passages Willison
  excerpted on his link-blog page.
- Two independent WebFetch calls to the Willison page returned consistent passages. The
  first call returned the fuller opening: "What happened in 2025 was this: the economics
  of code production were turned upside down." The second call's excerpt omitted the
  opening clause, but both agreed on the remainder of the passage. The first call's
  version is used as authoritative throughout this note.
- The article title ("AI demands more engineering discipline. Not less") is attributed to
  Majors' Substack post via the Willison page. Claim 4 explicitly marks this as an
  inference from the title alone, not an extracted body claim.
- Confidence is rated `emerging` rather than `anecdotal` because: (1) Majors is a
  high-credibility authority on engineering culture and code economics; (2) the economic
  characterization is consistent with multiple independent corpus measurements; (3) the
  claim names a specific year (2025) as the inflection point, making it specific and
  falsifiable rather than a vague directional assertion.
- The Prospector filed three triage comments with slightly varying chapter relevance and
  novelty ratings (medium, high, medium). This extraction follows the second triage
  comment's higher novelty assessment, which correctly identifies the supply-side economic
  framing as new to the corpus.
- Cross-reference verification: All cited claim numbers were verified by re-reading the
  actual source notes before writing:
  - `blog-simonwillison-charity-majors-enthusiast-skeptic.md` Claim 4 (line 111):
    "Velocity without comprehension is the specific failure mode" — verified.
  - `blog-simonwillison-charity-majors-enthusiast-skeptic.md` Claim 2 (line 68):
    "The current AI adoption cycle is different from normal technology cycles" — verified.
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 7 (line 162):
    "The SDLC was designed for ~200 LOC/day" — verified.
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 8 (line 182):
    "The SDLC disruption implies design processes need to operate faster" — verified.
  - `blog-simonwillison-james-shore-maintenance-costs.md` Claim 1 (line 50):
    "AI coding agents only produce a net productivity benefit if they reduce maintenance
    costs by exactly the inverse of their productivity gain ratio" — verified.
  - `paper-miller-speed-cost-quality.md` Claim 1 (line 45):
    "Cursor adoption causes a 281.3% increase in lines added in month 1" — verified.
  - `blog-anthropic-ai-native-engineering-org.md` Claim 1 (line 26):
    "Verification, code review, and security replaced code-writing as the primary
    bottlenecks" — verified.
