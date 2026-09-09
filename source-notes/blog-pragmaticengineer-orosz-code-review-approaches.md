---
source_url: https://newsletter.pragmaticengineer.com/p/what-is-happening-with-code-reviews
source_type: blog-post
title: "What is happening with code reviews?"
author: Gergely Orosz (The Pragmatic Engineer)
date_published: 2026-09-08
date_extracted: 2026-09-09
last_checked: 2026-09-09
status: current
confidence_overall: emerging
issue: "#3327"
---

# What is happening with code reviews?

> First-hand practitioner survey (named interviews with Weaviate's CTO,
> Duckbill Group's CEO, Sigil's CEO, and direct confirmation from Anthropic
> and OpenAI) cataloguing three concrete organizational responses to
> AI-generated code overwhelming review capacity: humans reviewing the AI's
> review instead of the code, blast-radius risk tiering (with a fully
> quantified before/after case study from Duckbill Group), and reviewing the
> plan/tests/database-schema instead of the implementation. Four further
> sections (produce less code, review everything by hand, no human review,
> why review exists) are paywalled and not covered here.

## Source Context

- **Type**: blog-post (The Pragmatic Engineer newsletter, Substack, free/paid
  mixed tier; published September 8, 2026). The free preview covers the
  article's introduction (GitHub PR-volume data) and the first three of
  seven numbered approaches in full, before the paywall cuts in immediately
  after section 3 ends, at the start of section 4 ("Produce less code").
- **Author credibility**: Gergely Orosz is an ex-Uber engineering manager who
  runs The Pragmatic Engineer, the largest paid technology newsletter on
  Substack, and is already a trusted, corroborated corpus author
  (`blog-pragmaticengineer-orosz-inside-anthropic.md`,
  `blog-pragmaticengineer-bun-rust-rewrite.md`,
  `blog-pragmaticengineer-orosz-slow-down-speed-up.md`). This post is
  first-hand reporting built from Orosz "asking around": it names and quotes
  Etienne Dilocker (cofounder/CTO, Weaviate), Mike Julian (cofounder/CEO,
  Duckbill Group), Jackie Luo (cofounder/CEO, Sigil; formerly an engineer at
  Square), and Andrea Francesco Speziale (Principal Engineer, Musixmatch),
  plus states Orosz personally confirmed the blast-radius approach "by
  talking with both companies" for Anthropic and OpenAI, naming Jarred
  Sumner as the Anthropic source.
- **Scope**: The free preview substantively covers: (1) an introductory
  GitHub PR/commit volume statistic; (2) "Humans review the AI code
  reviews" (vendor landscape, Weaviate's process, WeTravel's noise problem,
  Uber's uReview pipeline); (3) "Triage by 'blast radius' & choose an
  approach" (Anthropic/OpenAI/Duckbill adoption, Duckbill's full before/after
  numbers, Uber's Code Review Inbox); (4) "Review the plan/tests/database
  schema, but not the implementation" (the `/grill-me` skill, TDD, Jackie
  Luo's schema-only argument). It does NOT substantively cover sections 4-7
  ("Produce less code," "Review everything by hand," "No human code
  review?," "Why do we review code, anyway?") — only the one-sentence
  table-of-contents teaser for each is visible before the paywall.

## Extracted Claims

### Claim 1: GitHub's own platform-wide data shows the number of PRs opened increased fivefold over three years, with growth specifically accelerating from the end of 2025 (PRs and commits nearly doubling in that period alone)
- **Evidence**: Named source (a GitHub-provided graphic embedded in the
  article, captioned "Change in number of PRs, commits, and new repos across
  three years. Source: GitHub"), cited without further methodology detail
  (no repo sample, no breakdown by org size or language).
- **Confidence**: emerging
- **Quote**: "Over that time, the number of PRs opened has increased
  fivefold, which is a lot! And growth sped up from the end of 2025, when
  PRs and commits nearly doubled just in that period alone!"
- **Our assessment**: This is the article's load-bearing framing statistic —
  the entire piece is a response to this volume increase — but it is a
  single vendor-supplied graphic with no visible methodology (total PR count
  across all of GitHub? A sampled cohort? Public repos only?). Treat as
  directionally credible (GitHub is the primary source for its own platform
  data) but not independently audited. It's the same evidentiary class as
  `blog-addyosmani-agentic-code-review.md` Claim 4 ("GitHub Copilot review
  has run over 60 million reviews, a 10x increase in under a year") —
  platform-scale adoption/volume statistics from the platform vendor itself,
  useful for establishing scale rather than precision.

### Claim 2: The most common organizational response is for AI code-review vendors/agents to review the pull request, and for the human engineer to review the AI's review rather than the code itself
- **Evidence**: Author's synthesis from conversations, backed by a named
  vendor list and a concrete example (Anthropic's own Bun project running
  three review tools on the same PRs).
- **Confidence**: anecdotal
- **Quote**: "There are dozens of vendors offering this functionality – ones
  like CodeRabbit, Gitar, Greptile, GitHub Copilot Code Review, Qodo, Claude
  Code Review, Ellipsis and more. Many teams choose one or more, and the
  bots then review PRs, leaving comments for devs. For example, the Bun
  project by Anthropic has CodeRabbit, GitHub Code Review, and Claude Code
  Review all generating comments on PRs."
- **Our assessment**: The "review the review, not the code" reframing is the
  single most useful organizing idea in this claim — it names a distinct
  behavior change in the reviewer's job, not just a new tool. The Bun
  three-tool detail directly corroborates
  `blog-pragmaticengineer-orosz-inside-anthropic.md` Claim 11, which
  documents the same project running "Claude Code review... and CodeRabbit's
  code review" on the same PRs (via Jarred Sumner, a different Orosz
  interview); this article adds a third named tool (GitHub Code Review) not
  present in that account. Multiple simultaneous reviewers on the same PR is
  also a practical resolution to the precision/recall spread documented in
  `blog-addyosmani-agentic-code-review.md` Claim 5 (no single AI review tool
  wins on both precision and recall) — stacking heterogeneous reviewers
  compensates for any one tool's blind spots, which is exactly the
  mitigation that post's assessment recommended without a concrete example;
  this article supplies one.

### Claim 3: Weaviate's CTO structures AI-assisted review as a four-step loop where an adversarial AI agent reviews first, a human makes only the scope decision, and roughly 90% of the work is left to agents
- **Evidence**: Named, on-the-record practitioner account (Etienne Dilocker,
  cofounder and CTO of Weaviate).
- **Confidence**: anecdotal
- **Quote**: "It's very hard for agents to get the balance [of the code
  review] right. If you ignore human code review entirely and leave it to
  agents, every PR will either suffer from scope creep or ship critical
  issues. But, of course, you can't review everything by hand. So my current
  favorite setup is: 1. an (adversarial) agent does a review 2. a human
  makes a scope decision 3. an agent implements the feedback 4. either
  repeat or break the loop (likely a human decision) So basically, 90% is
  left to agents, with humans in the loop for critical scope decisions and
  exit criteria."
- **Our assessment**: This is a concrete, named-practitioner instantiation
  of the "human on the loop" posture already established in
  `blog-addyosmani-agentic-code-review.md` Claim 11 ("sampling,
  spot-checking and auditing" rather than reading every diff) — Dilocker's
  specific loop (agent reviews, human scopes, agent implements, human decides
  exit) is one concrete mechanism for what "on the loop" looks like in
  practice, with a numeric estimate (90% agent-handled) this corpus did not
  previously have attached to that framing.

### Claim 4: AI code review's noise/false-positive problem is a real adoption barrier — Weaviate CTO's own framing implies it must be managed, and a named company (WeTravel) declined to adopt AI review specifically because of the volume of noise it generated
- **Evidence**: Named company example (WeTravel, described as a "Series C
  travel tech company"), with a stated follow-up re-evaluation.
- **Confidence**: anecdotal
- **Quote**: "WeTravel, a Series C travel tech company, decided to not use AI
  for code reviews because of the amount of noise it generated. In June,
  they did an updated evaluation which showed lots of improvement, but still
  not enough to justify adopting AI for the task."
- **Our assessment**: This is a genuinely useful negative case for the
  corpus's mostly-adoption-positive coverage of AI code review — a named
  company evaluated twice (initial rejection, then a June re-evaluation) and
  still found the noise-to-signal ratio insufficient to adopt, as of this
  article's September 2026 publication. It's a concrete, dated counterpoint
  worth citing anywhere the guide otherwise implies AI code review adoption
  is now a default, solved decision.

### Claim 5: Uber built a custom pipeline (uReview) that grades AI-generated review comments, discards low-confidence ones, and merges/categorizes the remainder specifically to reduce noise before comments reach developers
- **Evidence**: Named company and named internal tool, described as a
  step-by-step pipeline; no effectiveness metrics given in the free content.
- **Confidence**: anecdotal
- **Quote**: "What uReview does: Bots generate lots of code review comments /
  Comments are graded, and low-confidence comments removed / Comments are
  merged, categorized, and unimportant ones removed / … in the end, the AI
  review results in important comments being shown to devs"
- **Our assessment**: This is the concrete engineering answer to Claim 4's
  noise problem — a purpose-built triage/filtering layer sitting between
  raw AI review output and the developer, rather than a raw vendor feed.
  No precision/recall numbers are given for uReview itself, so we can't
  independently assess how well it works; treat as evidence that
  "custom noise-reduction tooling" is a real, deployed pattern at a
  large-scale adopter, not evidence of a specific effectiveness bar.

### Claim 6: Blast-radius risk tiering (AI-only review and automatic shipping for low-risk changes; mandatory human review for high-risk changes) is used by Anthropic, OpenAI, and Duckbill Group, with Anthropic and OpenAI's use directly confirmed by the author
- **Evidence**: Author states this was independently confirmed via direct
  conversation with both companies, plus a fully named and quantified
  third example (Duckbill Group, covered in Claim 8-9).
- **Confidence**: emerging
- **Quote**: "Low-risk change: only AI, without human review. It can ship to
  production once AI agents are happy" / "High-risk change: mandatory
  human review" / "This is the approach that Anthropic and OpenAI follow,
  which I confirmed by talking with both companies."
- **Our assessment**: This is the single most valuable corroboration in the
  post for the corpus: `blog-addyosmani-agentic-code-review.md` Claim 7
  proposed blast-radius tiering as a prescriptive framework ("Tier by risk,
  not by author") without naming which organizations, if any, actually run
  it. This article names three named adopters, with two (Anthropic, OpenAI)
  independently confirmed by the reporter rather than inferred, moving the
  framework from "a practitioner-synthesizer's proposal" to "an observed,
  multi-company practice" in our corpus's evidentiary record.

### Claim 7: At Anthropic, a human still manually merges even low-risk, AI-approved changes as of this article's publication, but the team's stated goal is to eventually have another Claude instance perform that merge
- **Evidence**: Author's paraphrase of a direct statement from Jarred
  Sumner (not rendered in quotation marks in the source, i.e., not a direct
  quote of Sumner's own words, but a reported statement attributed to him
  by name).
- **Confidence**: anecdotal
- **Quote**: "At Anthropic, Jarred Sumner told me that a human merges even
  low-risk changes, but that their goal is eventually to get another Claude
  instance to merge low-risk changes."
- **Our assessment**: This is a dated status update on a specific prediction
  already in the corpus. `blog-pragmaticengineer-orosz-inside-anthropic.md`
  Claim 12 quotes the same Jarred Sumner (in a July 28, 2026 article,
  reporting on Bun specifically) predicting auto-merge for low-blast-radius
  changes "within a few months," gated by "another Claude with a fresh
  context window" judging blast radius. This September 8, 2026 article —
  about six weeks later — confirms that prediction had not yet shipped
  ("a human merges even low-risk changes") while the stated goal remains
  identical ("get another Claude instance to merge low-risk changes"). This
  is useful evidence that the six-week gap did not close the gap between
  prediction and practice, without indicating whether the goal was
  abandoned, delayed, or still actively in progress.

### Claim 8: Duckbill Group (a fifteen-person startup) publicly reported quantified before/after results from adopting a risk-based review system plus tightened guardrails: PRs merged per week rose from 80 to 154 (+94%), the share merged within 1 hour rose from 28% to 45%, and human-reviewed PRs took a median 26 hours to merge versus 1 hour for PRs that received no human review
- **Evidence**: Named company and named on-the-record source (Mike Julian,
  cofounder and CEO, Duckbill Group), quoted at length with specific
  self-reported figures; not independently audited by the author or a
  third party.
- **Confidence**: emerging
- **Quote**: "We ditched code review at Duckbill Group (mostly) About a
  month ago, we found ourselves with 60 open PRs for a team of five. […]
  Results before vs after: PRs merged: 353 → 684 (80/wk → 154/wk, +94%)
  Merged within 1h: 28% → 45%; within 24h: 76% → 80% Human-reviewed PRs
  median merge time: 26h No human-review median merge time: 1h."
- **Our assessment**: This is the strongest, most specific quantitative
  evidence in the post — a named CEO publishing his own team's before/after
  numbers for a real process change, rather than a vendor benchmark or an
  unnamed "researchers" claim (compare
  `blog-addyosmani-agentic-code-review.md` Claim 10's vague, unattributed
  "circuit breaker" finding). The 26h-vs-1h merge-time gap is a striking,
  directly actionable data point: it quantifies exactly how much latency
  human review adds relative to AI-only merging at this specific team's
  scale, and corroborates (with company-specific numbers) the general
  premise that human review is the throughput bottleneck once code volume
  rises — the same underlying mechanism Faros AI's 441.5% review-duration
  increase documents in `blog-addyosmani-agentic-code-review.md` Claim 2,
  here shown from the opposite direction (the time saved when human review
  is skipped, rather than the time added when it's required to keep pace).
  As a single self-reported case study from a 5-person team, this should
  not be treated as generalizable to larger organizations' risk profiles.

### Claim 9: Duckbill Group's specific high-risk trigger categories requiring mandatory human review are: public API/MCP changes, authentication, the design system, non-additive database schema changes, and agent skills — enforced automatically via a shell script that applies a GitHub label
- **Evidence**: Named company, named source (Mike Julian), specific and
  falsifiable list of trigger categories plus the named enforcement
  mechanism.
- **Confidence**: emerging
- **Quote**: "Switch to a risk-based system. With a risk-based system, we
  agreed that if your change touched the public API/MCP, auth, design
  system, non-additive database schema changes, or agent skills, it needed
  a human review. We then enforced that with a shell script to add a GitHub
  label."
- **Our assessment**: This is a concrete, directly reusable checklist for
  any team implementing blast-radius tiering — more specific than Osmani's
  abstract "config change vs. payments path" example in
  `blog-addyosmani-agentic-code-review.md` Claim 7. The inclusion of
  "non-additive database schema changes" as a distinct high-risk category
  (as opposed to schema changes generally) directly corroborates Claim 11
  below (Jackie Luo's schema-centric review philosophy) from an independent
  source: both identify database schema changes as categorically riskier
  than other code, though Luo frames schema as the *only* thing worth
  reviewing while Duckbill treats it as one of five triggers alongside
  auth, API surface, design system, and agent skills.

### Claim 10: Some teams have replaced implementation review with upfront plan review, using structured interrogation tools (e.g., the "/grill-me" skill) to produce a detailed enough specification that the resulting implementation needs no further review
- **Evidence**: Named tool (the `/grill-me` skill, attributed to Matt
  Pocock) plus a named, on-the-record endorsement from a second
  practitioner (Andrea Francesco Speziale, Principal Engineer at
  Musixmatch).
- **Confidence**: anecdotal
- **Quote**: "The /grill-me skill by Matt Pocock is a popular method, and
  I'm also a fan of it for thorough upfront planning, as is Andrea
  Francesco Speziale, Principal Engineer at Musixmatch: \"After 3 hours of
  /grill-me, it better one-shot the implementation. I'm not spending a
  single minute on any review!\""
- **Our assessment**: Speziale's "not spending a single minute on any
  review" is a genuinely extreme claim — a named practitioner asserting
  zero implementation review is acceptable given sufficient upfront spec
  investment (3 hours of interrogation). This is a specific, concrete
  answer to the gap flagged in
  `blog-simonwillison-more-than-just-code-review.md` Claim 2, which asserts
  "there are other ways to achieve that goal" (validating a change) beyond
  line-by-line review but names none — this article supplies one named
  alternative (exhaustive upfront plan review substituting entirely for
  implementation review) with a named practitioner willing to attach his
  name to the "zero minutes of review" claim. We'd flag this as the most
  aggressive point on the review-reduction spectrum in the corpus, and note
  it is a single anecdote, not a measured outcome (no defect-rate or
  incident data accompanies the claim).

### Claim 11: Sigil's CEO argues that in a fast-moving startup, the database schema is the only artifact worth reviewing carefully, because it is the "hard," effectively unrecoverable representation of the system, while code and business logic are "fluid and recoverable" and can be cheaply regenerated
- **Evidence**: Named, on-the-record practitioner argument (Jackie Luo,
  cofounder and CEO of Sigil, formerly an engineer at Square), given as a
  structured three-point argument.
- **Confidence**: anecdotal
- **Quote**: "My current take is that all that really matters is the
  database schema. Speaking from a fast-moving startup perspective: 1.
  Everything, besides data, is fluid and recoverable. 2. The schema is the
  \"hard\" representation of what's been built and reveals the riskiest
  changes, so it's a good attention/impact tradeoff. 3. Business logic only
  matters because product behavior matters—so ideally align on that before
  interacting with a coding agent at all."
- **Our assessment**: This names a specific mechanism (data as the
  "rigid"/unrecoverable layer; code as cheap to regenerate) for why schema
  review should be prioritized over implementation review, which is more
  precise than the general "review what doesn't transfer to a model"
  framing in `blog-addyosmani-agentic-code-review.md` Claim 11. Orosz's own
  editorial gloss immediately following the quote (not part of Luo's
  quote, but the author's assessment) explicitly scopes this to
  early-stage startups: "once you have a business, you'll want to 'guard'
  the business logic with tests: else your product could break, and
  existing users will be unhappy." We treat the underlying claim as a
  context-dependent recommendation (startup pre-PMF vs. an established
  product with real users), not a universal review policy — consistent
  with the context-dependence already established in
  `blog-addyosmani-agentic-code-review.md` Claim 6.

## Concrete Artifacts

```
Source: https://newsletter.pragmaticengineer.com/p/what-is-happening-with-code-reviews

The article's own seven-approach table of contents (verbatim from the
free-content introduction, including the four paywalled section titles and
their one-line teasers):

1. Humans review the AI code reviews.
   The most popular approach: AI code review tools go through code changes,
   and devs review the review itself.
2. Triage by "blast radius" & decide an approach.
   Low-risk changes don't need human review, and high-risk ones do. Adopted
   by OpenAI, Anthropic, and others.
3. Review the plan/tests/database schema, but not implementation.
   Focus on reviewing the "before" and "after" states of an implementation,
   rather than the implementation itself.
4. Produce less code. [PAYWALLED]
   Set up AI agents to produce smaller PRs that are easier to review and
   reason about.
5. Review everything by hand. [PAYWALLED]
   Not everyone has adopted AI code review tools – even those that have
   sometimes still expect devs to read through all the new code, before
   allowing it to go to prod.
6. No human code review? [PAYWALLED]
   There's more talk about dropping human code reviews than there is
   evidence of this actually happening, so far. The most I could find was
   AI startups doing it and building additional layers for safer production
   rollouts.
7. Why do we review code, anyway? [PAYWALLED]
   Before figuring out whether or not code review should stay, it's worth
   going back to the fundamental technical, team, and organizational
   reasons for code reviews.

Paywall cutoff point (verbatim, end of free content, immediately after
section 3 ends):
"4. Produce less code
This post is for paid subscribers
Subscribe"
```

```
Source: https://newsletter.pragmaticengineer.com/p/what-is-happening-with-code-reviews
Speaker: Mike Julian, cofounder and CEO, Duckbill Group (full quoted post)

"We ditched code review at Duckbill Group (mostly)

About a month ago, we found ourselves with 60 open PRs for a team of five.
They had been accumulating for a few weeks and we all had the sudden
realization we were looking at two days of just code review.

I had been tossing around the idea for a while about having AI do all code
review and so I just asked the team: what if we just didn't review the
PRs?

We decided to do a couple of things:

Switch to a risk-based system. With a risk-based system, we agreed that if
your change touched the public API/MCP, auth, design system, non-additive
database schema changes, or agent skills, it needed a human review. We then
enforced that with a shell script to add a GitHub label.

Improve our guardrails (unit and end-to-end testing, post-deploy
observability, stricter linting and type checking, etc). Improving
guardrails was pretty easy, just expensive in tokens and attention. We
enabled nearly every rule in ruff/prettier/eslint/ty, and we improved our
unit test coverage to a floor of 85%.

Results before vs after:
PRs merged: 353 → 684 (80/wk → 154/wk, +94%)
Merged within 1h: 28% → 45%; within 24h: 76% → 80%
Human-reviewed PRs median merge time: 26h
No human-review median merge time: 1h."
```

## Cross-References

- **Corroborates**:
  - `blog-addyosmani-agentic-code-review.md` Claim 7 (tier review effort by
    blast radius, not by author) — this article's Claim 6 supplies the
    named, directly-confirmed adopters (Anthropic, OpenAI) that Osmani's
    post lacked, moving the framework from proposal to observed practice.
  - `blog-addyosmani-agentic-code-review.md` Claim 11 ("human on the loop":
    sampling/spot-checking/auditing rather than reading every diff) — this
    article's Claim 3 (Dilocker's 90%-agent-handled loop) is a concrete,
    named instantiation of that posture.
  - `blog-addyosmani-agentic-code-review.md` Claim 5 (no single AI review
    tool wins on both precision and recall) — this article's Claim 2 (Bun
    running three review tools simultaneously) is a practical example of
    the "stack heterogeneous reviewers" mitigation that claim's assessment
    called for without a concrete example.
  - `blog-pragmaticengineer-orosz-inside-anthropic.md` Claim 11 (Bun runs
    "Claude Code review... and CodeRabbit's code review" on the same PRs)
    — this article's Claim 2 independently reports the same Bun review
    stack with a third tool (GitHub Code Review) added.
  - `blog-addyosmani-agentic-code-review.md` Claim 6 (review needs are
    highly context-dependent, from solo project to decade-old enterprise
    system) — this article's Claim 11 (Jackie Luo's schema-only philosophy,
    explicitly scoped by Orosz to pre-PMF startups) is a concrete instance
    of a review policy that only makes sense at one end of that spectrum.

- **Contradicts**: None identified. No claim in this source was found to
  materially oppose an existing corpus source note's claim about the same
  situation; where positions differ (e.g., Speziale's "zero minutes of
  review" vs. sources recommending some ongoing review), the difference is
  explained by a conditioning variable (upfront planning investment,
  project stage) already recognized in the corpus per
  `blog-addyosmani-agentic-code-review.md` Claim 6, not a same-context
  disagreement, so no contradiction issue was filed per MINER.md §4a.

- **Extends**:
  - `blog-pragmaticengineer-orosz-inside-anthropic.md` Claim 12 (Sumner's
    July 2026 prediction of near-term auto-merge for low-blast-radius
    changes, gated by a fresh-context-window Claude instance) — this
    article's Claim 7, published roughly six weeks later, reports the
    prediction had not yet shipped as of September 8, 2026, while the
    stated goal is unchanged. This is a dated status update the corpus
    did not previously have.
  - `blog-simonwillison-more-than-just-code-review.md` Claim 2 (eyeballing
    every line "has never been the most effective way to validate a
    change," but names no alternative) — this article's Claim 10
    (upfront `/grill-me`-style plan review substituting entirely for
    implementation review) and Claim 11 (schema-only review) each supply a
    named, concrete alternative that source lacked, alongside the
    Cognition-agent-verification alternative already flagged in that
    note's own cross-references.
  - `blog-addyosmani-agentic-code-review.md` Claim 2 (Faros AI: median
    review duration up 441.5% under agent-generated volume) — this
    article's Claim 8 (Duckbill: 26h median merge with human review vs. 1h
    without) quantifies the same underlying mechanism from a single named
    team's before/after numbers rather than an aggregate industry dataset.

- **Novel**:
  - The specific, reusable list of high-risk trigger categories (Claim 9:
    public API/MCP, auth, design system, non-additive schema changes, agent
    skills) and its automated shell-script/GitHub-label enforcement
    mechanism is new to the corpus as a concrete, adoptable checklist.
  - Uber's uReview comment-grading/filtering pipeline (Claim 5) is a new,
    named concrete artifact for how one large-scale adopter engineers away
    AI review noise.
  - WeTravel's twice-evaluated, twice-declined adoption of AI code review
    (Claim 4) is the corpus's first named, dated negative case for AI code
    review adoption.
  - Duckbill Group's fully quantified before/after case study (Claim 8) is
    the first named, single-team, before/after quantification of adopting
    blast-radius tiering in the corpus (as distinct from the aggregate,
    cross-company datasets Osmani cites).

## Guide Impact

- **Chapter 02 (Core Patterns / agentic workflows)**: Strengthen the
  existing blast-radius-tiering recommendation (currently sourced from
  `blog-addyosmani-agentic-code-review.md` Claim 7) by adding this source's
  named adopters (Claim 6: Anthropic, OpenAI, Duckbill) and Duckbill's
  concrete trigger-category checklist (Claim 9) as an adoptable starting
  point, plus Duckbill's quantified results (Claim 8) as evidence the
  approach produces measurable throughput gains at small-team scale.

- **Chapter 04 (Systems & Automation)**: Add Uber's uReview pattern (Claim
  5) as a concrete example of a noise-reduction layer for teams running
  multiple AI review tools, and the "stack multiple heterogeneous
  reviewers" pattern (Claim 2, Bun's three-tool stack) as a practical
  mitigation for single-tool precision/recall gaps already flagged via
  `blog-addyosmani-agentic-code-review.md` Claim 5.

- **Chapter 05 (Team Adoption / human-agent collaboration)**: Add WeTravel's
  negative case (Claim 4) as an explicit counterexample wherever the guide
  discusses AI code review adoption, to avoid implying universal adoption
  is settled. Add Dilocker's four-step "90% to agents" loop (Claim 3) as a
  concrete, named example of the "human on the loop" posture. Add the
  plan-review/schema-review alternatives (Claims 10-11) as named, adoptable
  answers to "what do I do instead of reading every line," filling the gap
  `blog-simonwillison-more-than-just-code-review.md` left open.

## Extraction Notes

- **Paywall boundary verified via raw HTML, not WebFetch summarization**:
  An initial WebFetch pass returned a condensed, AI-paraphrased summary
  rather than verbatim article text (the same pattern already documented in
  `blog-pragmaticengineer-orosz-inside-anthropic.md`'s Extraction Notes).
  The full free-preview text was instead fetched via `curl` with a browser
  user-agent (HTTP 200, ~201KB HTML), the `available-content` div was
  isolated, and HTML tags/entities were stripped to produce flat text. All
  quotes above were copied character-for-character from that flat-text
  extraction (saved locally during extraction), and the exact paywall
  cutoff ("This post is for paid subscribers / Subscribe") was located
  immediately after the "4. Produce less code" heading, confirming the
  paywall falls precisely at the start of section 4 with zero body content
  for sections 4-7.
- Sections 4-7 (Produce less code, Review everything by hand, No human code
  review?, Why do we review code, anyway?) are entirely paywalled beyond
  their one-sentence table-of-contents teasers, which are reproduced
  verbatim in Concrete Artifacts above. No claims were extracted from these
  sections beyond what the teaser sentences themselves state, to avoid
  inventing content not actually visible.
- No sub-pages were followed. The article links to a prior Pragmatic
  Engineer piece on WeTravel's code-review measurement (referenced in
  Claim 4's evidence) and to an external "How Uber uses AI for development"
  source for the Code Review Inbox graphic; neither link's destination text
  was independently fetched, since the article's own quoted/described
  content for each was sufficient to extract the claims made in this post
  specifically (a full extraction of either linked source, if warranted,
  should be filed as a separate source-submission issue rather than folded
  into this note).
- No contradiction issue was filed. The closest candidate — Speziale's
  "not spending a single minute on any review" (Claim 10) against sources
  recommending continued review under agent-generated volume — was
  evaluated against MINER.md §4a's bar and judged a conditioning-variable
  difference (upfront planning investment substituting for downstream
  review), not a same-context disagreement; see Cross-References above.
- Cross-references verified: `blog-addyosmani-agentic-code-review.md`
  Claims 2, 5, 6, 7, and 11 and
  `blog-simonwillison-more-than-just-code-review.md` Claim 2 were each
  re-read in their source notes before this note was written, and all
  quoted text from those notes above is copied verbatim from them.
  `blog-pragmaticengineer-orosz-inside-anthropic.md` Claims 11 and 12 were
  likewise re-read directly in that note; the "11 rounds"/three-tool Bun
  review-stack detail and the auto-merge prediction quote were confirmed
  against that note's own numbered claim text rather than reconstructed
  from memory.
