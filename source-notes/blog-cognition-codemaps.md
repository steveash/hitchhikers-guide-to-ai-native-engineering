---
source_url: https://cognition.com/blog/codemaps
source_type: blog-post
title: "Windsurf Codemaps: Understand Code, Before You Vibe It"
author: The Cognition Team
date_published: 2025-11-04
date_extracted: 2026-07-19
last_checked: 2026-07-19
status: current
confidence_overall: emerging
issue: "#2041"
---

# Windsurf Codemaps: Understand Code, Before You Vibe It

> Cognition's announcement of Windsurf Codemaps — AI-annotated, navigable maps
> of a codebase generated on demand from a task prompt — framed around a
> product philosophy that AI tools should deepen a developer's understanding
> of their own code rather than substitute for it, positioning code
> comprehension as the prerequisite for both safe "vibe coding" and effective
> agent delegation.

## Source Context

- **Type**: blog-post (Cognition's own blog, cognition.com; byline "By The
  Cognition Team," no individual author named, published 11.04.25 per the
  page's own byline format, i.e. 2025-11-04 — the same MM.DD.YY format used
  on the other Cognition posts already in this corpus, e.g. "04.15.26" =
  2026-04-15 in `blog-cognition-devin-in-windsurf.md`). This is chronologically
  the earliest-dated Cognition source in this corpus at time of writing — it
  predates the Windsurf 2.0 / Devin-in-Windsurf launch (April 2026) and Devin
  Desktop (June 2026), both already covered by existing notes.
- **Author credibility**: First-party product-announcement and
  product-philosophy blog post from the company that builds Devin, Windsurf,
  DeepWiki, and Ask Devin. It opens with a Paul Graham epigraph and cites two
  external, hyperlinked figures (an unnamed "estimates" source for onboarding
  time, and a named "Stripe" finding) as supporting evidence for its
  motivating problem statement, rather than presenting first-party usage
  data of its own. No customer quote, adoption number, or benchmark result
  for Codemaps itself appears anywhere in the post — it is evidenced only by
  its own dogfooding description ("in our dogfooding, we find particular
  effectiveness...") rather than any named practitioner or measured outcome.
- **Scope**: Covers the motivating problem (onboarding/comprehension tax on
  engineering productivity), the Codemaps feature itself (how to invoke it,
  the two backing models, the two view modes, the `@{codemap}` agent-context
  syntax), and an extended philosophical argument about "vibe coding,"
  accountability, and the engineer's role as AI takes over more code
  generation. Does **not** cover: any accuracy, adoption, or session-count
  metric for Codemaps; a named customer using it; the underlying indexing/
  analysis mechanism in technical detail; how Codemaps content is generated
  or invalidated as code changes (staleness); or a worked, step-by-step
  example of a specific codemap for a specific bug.

## Extracted Claims

### Claim 1: Cognition frames real engineering as distinct from code generation by the presence of understanding, and argues most current AI coding tools increase the separation between a developer and their code rather than closing it
- **Evidence**: Opening thesis statement of the post, contrasting
  "engineering" against "low value, commodity tasks."
- **Confidence**: anecdotal (philosophical framing/thesis statement, not a
  measured claim; no criteria given for what makes a task "commodity" vs.
  "hard, sensitive, and high value")
- **Quote**: "Software development only becomes engineering with understanding." / "This is fine for low value, commodity tasks, but absolutely unacceptable for the hard, sensitive, and high value work that defines real engineering."
- **Our assessment**: This is the post's organizing thesis and the
  motivating premise for the Codemaps feature: that comprehension, not
  code-output speed, is the actual engineering bottleneck for consequential
  work. It's a value judgment about what counts as "real" engineering rather
  than an empirical claim, but it is a citable, specific articulation of a
  position — AI tools should widen understanding, not just widen output —
  that is more precisely stated here than in this corpus's existing
  vibe-coding coverage (see Cross-References → Corroborates).

### Claim 2: Cognition cites (via hyperlink, not its own data) that new engineers take 3-9 months to fully ramp, senior engineers lose 5+ hours per week onboarding others, and Stripe found legacy-code maintenance to be the #1 productivity drag among its customers
- **Evidence**: Three hyperlinked, externally-sourced figures presented as
  the quantified cost of the onboarding/comprehension problem; none of the
  three is Cognition's own measurement.
- **Confidence**: anecdotal (all three figures are secondhand citations via
  hyperlink, not verified or reproduced by this extraction, and no date or
  methodology is given for any of the three within the post itself)
- **Quote**: "New engineers take 3–9 months to fully ramp" / "Senior engineers lose 5+ hours per week onboarding others" / "Stripe found legacy maintenance to be the #1 drag on productivity on their customers"
- **Our assessment**: These figures should be cited, if at all, as
  third-party-sourced statistics relayed by Cognition to motivate its own
  product, not as Cognition's own research — the post does not name the
  underlying studies inline (they are hyperlinked "estimates" and "source"
  links this extraction did not independently verify, consistent with
  MINER.md's guidance to follow only substantive linked pages; these are
  citation footnotes, not additional Cognition content). Treat as
  plausible-but-unverified supporting evidence for a real, widely-cited
  problem, not as this source's own contribution.

### Claim 3: Windsurf Codemaps are announced as "first-of-its-kind AI-annotated structured maps" of a codebase, generated on demand and powered by two named models (SWE-1.5 for a Fast mode, Claude Sonnet 4.5 for a Smart mode)
- **Evidence**: Direct product-announcement sentence naming both backing
  models and the feature's positioning relative to Cognition's prior
  products (DeepWiki, Ask Devin).
- **Confidence**: emerging (concrete, named, shipped feature announcement
  with two specific named models; no detail on what differs in the
  underlying map-generation process between the two modes beyond speed/
  model choice)
- **Quote**: "Windsurf Codemaps, which are first-of-its-kind AI-annotated structured maps of your code, powered by SWE-1.5 and Claude Sonnet 4.5."
- **Our assessment**: This is the first source in this corpus to name
  "SWE-1.5" as a Cognition model choice for a shipped feature, and the
  first to name a codebase-mapping/comprehension artifact (distinct from
  DeepWiki's "browsable, linked documentation" framing) as a discrete
  product. It is positioned explicitly as an evolution of two prior,
  named Cognition products rather than a standalone launch — see
  Cross-References → Extends.

### Claim 4: A Codemap is invoked with a task-specific prompt (or an automatic suggestion) via a keyboard shortcut or icon in Windsurf, choosing between a Fast and Smart model, and every generated Codemap is a snapshot of the code that respects Zero Data Retention (ZDR)
- **Evidence**: Direct mechanics description of the invocation flow and a
  stated data-handling property.
- **Confidence**: emerging (concrete, shipped product-mechanics
  description; no detail on how a snapshot is invalidated or refreshed
  once the underlying code changes, i.e. staleness handling)
- **Quote**: "When you first open Codemaps (click the new maps icon or Cmd+Shift+C in Windsurf)... you can enter in a prompt for the task you are trying to do, or take one of the automatic suggestions." / "Every Codemap is a snapshot of your code and respects ZDR."
- **Our assessment**: The explicit ZDR (Zero Data Retention) claim is a
  specific, checkable data-handling property worth flagging distinctly from
  the feature-mechanics claim itself — it is a compliance-relevant detail
  for security-conscious teams evaluating the feature, though this source
  gives no further detail on ZDR's scope (does it cover only the Codemap
  artifact, or the underlying code read to generate it?).

### Claim 5: Cognition's own dogfooding found Codemaps particularly effective for tracing client-server problems, data pipelines, and debugging auth/security issues, and claims its grouped, line-linked navigation is already an improvement over asking the same question in Cascade's chat interface
- **Evidence**: First-person dogfooding claim naming three task categories,
  plus an explicit comparative claim against Cognition's own existing
  chat-based agent product (Cascade).
- **Confidence**: anecdotal (internal dogfooding observation with no
  session count, no user study, and no criteria given for what "densely
  linked" means quantitatively; the Cascade comparison is asserted, not
  benchmarked)
- **Quote**: "In our dogfooding, we find particular effectiveness tracing through client-server problems or a data pipeline or debugging auth/security issues" / "this is already an improvement compared to asking the same question in Cascade, where answers are not as densely linked to the exact lines of code."
- **Our assessment**: This is the post's central differentiation claim —
  the value-add over a generalist chat agent (Cascade) is framed as
  navigation density and code-line grounding, not new reasoning capability.
  It is a vendor's internal, unbenchmarked comparison of its own two
  products, so it should be read as a design rationale (why build Codemaps
  at all, given Cascade already exists) rather than an independently
  verified improvement.

### Claim 6: Codemaps has two view modes — a grouped/linked text view and a visually-drawn graph view where clicking a node jumps to the corresponding code — plus an expandable "trace guide" that gives a more descriptive explanation of why lines are grouped together
- **Evidence**: Direct feature-mechanics description of both view modes and
  the expansion mechanism.
- **Confidence**: settled (concrete description of a shipped, current UI
  surface — this is what a user of the feature sees today, not a forecast
  or experiment)
- **Quote**: "You can also toggle over to a visually drawn Codemap, which performs the same functions when you click on individual nodes: they send you to the exact part of the codebase you clicked on." / "if you want a little more context, then you can hit "See more" in any section to expand our "trace guide" that gives a more descriptive explanation of what groups the discovered lines together."
- **Our assessment**: The two-tier design (fast grouped-list skim vs. a
  visual graph, plus an on-demand deeper "trace guide" explanation) mirrors
  the two-tier reviewability pattern (fast skim + deep drill-down) already
  documented for a different artifact — Devin's test reports — in
  `blog-cognition-verifying-agentic-development.md` Claim 10, suggesting
  Cognition applies the same summary-plus-drill-down UI principle across
  distinct products (test verification and code comprehension).

### Claim 7: A generated Codemap can be injected directly into an agent prompt inside Cascade using an `@{codemap}` reference syntax (whole map or a subsection), which Cognition says "dramatically" improves agent performance on the task
- **Evidence**: Direct mechanics description of the agent-context
  integration syntax and a stated performance claim.
- **Confidence**: anecdotal ("dramatically improve the performance" is
  asserted with no before/after benchmark, task set, or success-rate
  number attached)
- **Quote**: "inside Cascade you can also reference a codemap for the agent with @{codemap} (all of it, or a particular subsection) in your prompt to provide more specific context and dramatically improve the performance of your agent for your task."
- **Our assessment**: This is the most concrete, transferable mechanism in
  the post: a human-facing comprehension artifact (the Codemap) doubling as
  a structured, reusable context object that can be handed to an agent by
  reference rather than re-explained in prose each time. This is a
  specific instance of "pre-computed, structured context beats ad hoc
  prose context," though the "dramatically" claim itself is unquantified
  and should be cited as a vendor assertion, not a measured result.

### Claim 8: Cognition argues productive vs. problematic AI-assisted coders are distinguished by whether the code they generate stays within their own ability to understand it, and states plainly that "to understand is to be accountable"
- **Evidence**: Direct philosophical claim under the "Fight back against
  Vibeslop" heading, contrasting productive and problematic AI-assisted
  coding by comprehension rather than by tool or output volume.
- **Confidence**: anecdotal (conceptual/philosophical claim, not measured;
  no criteria given for what threshold of understanding separates
  "productive" from "problematic" usage)
- **Quote**: "people get into trouble when the code they generate and maintain starts to outstrip their ability to understand it." / "To understand is to be accountable."
- **Our assessment**: This is a specific, quotable articulation of the
  vibe-coding risk already discussed elsewhere in this corpus (see
  Cross-References → Corroborates) — the risk is framed not as "AI writes
  bad code" but as "the human's comprehension falls behind the code's
  growth," which is a comprehension-gap framing rather than a
  code-quality framing. Useful for the guide as a compact definition of
  where vibe coding becomes unsafe.

### Claim 9: Cognition states the engineer's role is shifting from "authoring" to "accountability" — an engineer may not write every line, but remains responsible for what ships — and positions Codemaps as the shared artifact that lets both the human and the AI hold a common picture of the system's structure, data flow, and dependencies
- **Evidence**: Direct role-reframing statement followed immediately by the
  product-positioning claim tying that reframing back to Codemaps
  specifically.
- **Confidence**: anecdotal (role-of-the-engineer reframing is a product-
  philosophy claim, not a measured organizational trend; no data on how
  many engineers or teams have actually shifted responsibility this way)
- **Quote**: "the engineer's role shifts from authoring to accountability — you might not write every line, but you're still responsible for what ships." / "Codemaps closes that gap by giving both the human and the AI a shared picture of the system: how it's structured, how data flows, where dependencies live."
- **Our assessment**: This generalizes the accountability framing in Claim 8
  from an individual-discipline question ("understand your own code") to
  an organizational-responsibility question ("you're still responsible for
  what ships, regardless of who wrote it") — and explicitly ties the two
  together via a shared, structured artifact (the Codemap itself) rather
  than leaving "shared understanding" as an abstract goal. This is directly
  corroborated by an independent, non-Cognition source already in this
  corpus that argues from the opposite direction — that AI lacks the
  professional accountability that would let humans trust its output
  unreviewed the way they trust human teammates (see Cross-References →
  Corroborates).

### Claim 10: Cognition explicitly rejects full-autonomy-only messaging (paraphrased in the post as "pls ultrathink high, no mistakes") as a competing "local minima," arguing it gives autonomy only to the agent at the engineer's expense, and states its own goal is to augment engineers for high-value work rather than replace them
- **Evidence**: Direct critique of a competing product-messaging pattern in
  the coding-agent industry, followed by an explicit statement of
  Cognition's own stated design goal.
- **Confidence**: anecdotal (competitive/philosophical positioning
  statement; no named competitor, product, or evidence that this messaging
  pattern actually produces worse outcomes)
- **Quote**: "The other local minima that the coding agent industry has gotten stuck in is in the general messaging of replacing engineers for low value work and not having any solutions for the hardest tasks apart from "pls ultrathink high, no mistakes", which only gives autonomy to the agent, at the expense of the engineer." / "the AI product that engineers will love most is the one that makes them better at their job, not the one that tries to replace them with a sloppy facsimile of themselves."
- **Our assessment**: This positions Codemaps as an argument-by-product
  against a specific rival philosophy (maximize agent autonomy, minimize
  human involvement) without naming which competitor(s) it is describing —
  it should be read as Cognition's stated design stance, not as a
  characterization of any named competitor's actual position or a
  demonstrated outcome comparison between the two philosophies.

### Claim 11: Cognition states it has not yet benchmarked whether exposing this internal indexing/analysis to humans as Codemaps also improves its own coding agents (Devin, Cascade) at solving tasks autonomously, and names two future directions — connecting/annotating codemaps, and an open `.codemap` protocol for other agents and custom tooling
- **Evidence**: Direct, explicit admission of an unmeasured open question in
  the closing "What's Next" section, plus two named roadmap items.
- **Confidence**: settled (a first-party admission of a current limitation
  — "we have yet to benchmark" — is a candid negative-knowledge disclosure,
  which carries higher credibility than an unqualified capability claim,
  consistent with how this corpus treats similar admissions elsewhere; the
  roadmap items themselves are stated intentions, not shipped features)
- **Quote**: "we have yet to benchmark how much better they can make our coding agents like Devin and Cascade in solving challenging tasks on their own." / "we also see opportunities for connecting and annotating codemaps, as well as defining an open .codemap protocol that can be used by other code agents and custom tooling built by you."
- **Our assessment**: This is a meaningful scope caveat for the whole post:
  Codemaps is justified here purely as a human-comprehension tool, with
  Cognition explicitly declining to claim (yet) that the same underlying
  indexing measurably improves its own agents' autonomous task performance.
  The proposed open `.codemap` protocol is the most forward-looking,
  currently unshipped claim in the post — a proposal, not a shipped
  standard, and should be cited as such.

## Concrete Artifacts

### Codemap invocation and view mechanics (from the article, verbatim fragments)
```
Source: cognition.com/blog/codemaps, "Our solution: Just-in-Time mapping for any problem"

Invocation: click the maps icon, or Cmd+Shift+C, in Windsurf, with a
codebase open. Enter a task prompt, or accept an automatic suggestion.
Model choice: "Fast" (SWE-1.5) or "Smart" (Sonnet 4.5).
Data handling: "Every Codemap is a snapshot of your code and respects ZDR."
Views: grouped/linked list view (default) <-> visually drawn graph view
  (click a node to jump to the corresponding code).
Depth: "See more" on any section expands a "trace guide" with a fuller
  explanation of why the discovered lines are grouped together.
Agent integration: reference a generated codemap (whole or a subsection)
  inside a Cascade prompt via `@{codemap}` syntax.
```

### Onboarding-tax figures cited by Cognition (externally sourced, via hyperlink; not Cognition's own data)
```
Source: cognition.com/blog/codemaps, "Why Codemaps?" section

- New engineers take 3-9 months to fully ramp (linked "estimates")
- Senior engineers lose 5+ hours per week onboarding others (linked "source")
- Stripe found legacy maintenance to be the #1 drag on productivity on
  their customers (linked "source")
```

### Product-lineage framing (from the article, verbatim)
```
Source: cognition.com/blog/codemaps, "Why Codemaps?" section

"Ask Devin introduced focused agents that reason through real codebases.
DeepWiki made that reasoning transparent, turning your repos into
browsable, linked documentation. Windsurf brought these capabilities
into the IDE. Codemaps is our next investment in tooling that makes
engineers the best versions of themselves."
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 3 (AI
    agents lack the professional accountability that makes trusting human
    teams without review acceptable — "accountability for what it's done"
    is the specific disanalogy Willison names) — this source's Claim 9
    (the engineer's role shifts from authoring to accountability;
    "you're still responsible for what ships") approaches the identical
    conclusion from the opposite direction: Willison argues AI cannot hold
    accountability, so a human must; this source argues the human's role
    is now explicitly defined as holding that accountability. Two
    independent sources (an individual practitioner and a vendor) converge
    on accountability, specifically, as the property that does not
    transfer to an AI agent.
  - `blog-cognition-verifying-agentic-development.md` Claim 5 (Devin's
    test-plan generation "must be grounded in source, not assumptions,"
    since "without grounding in code, we found the models like to assume
    they can go down paths in the app that don't exist") — this source's
    Claim 5 and Claim 7 apply the identical grounding principle to human
    (and agent) code *navigation* rather than to autonomous *testing*:
    Codemaps' value proposition is explicitly that its answers are "densely
    linked to the exact lines of code" rather than assumption-based, the
    same underlying "ground claims in actual code, not model assumption"
    mechanism documented at the testing layer in that note.
  - `blog-cognition-verifying-agentic-development.md` Claim 10 (Devin's test
    report offers labeled screenshots for a fast skim plus a chaptered video
    for deep review) — this source's Claim 6 (a grouped/linked list view
    plus an expandable "trace guide" for deeper explanation, and a separate
    visual graph view) is the same two-tier summary-plus-drill-down UI
    principle applied to a different Cognition product (code comprehension
    rather than test verification).

- **Contradicts**: None filed. One candidate tension was considered and
  rejected: this source's philosophy that engineers must deeply understand
  their own codebase before "vibing" through changes could be read as being
  in tension with `blog-cognition-devin-in-windsurf.md`'s description of a
  developer delegating implementation work to Devin and then "clos[ing]
  their laptop and grab[bing] a coffee" while the cloud agent works
  unattended. This does not meet the MINER.md §4a bar for filing: the two
  sources describe different phases of the same workflow rather than
  opposing claims under matching conditions — this source's "understand
  before you vibe it" framing concerns the *planning and review* phases
  (using a Codemap to understand the codebase before delegating a task, and
  presumably again when reviewing the returned PR), while the Windsurf
  source's "step away" framing concerns the *unattended execution* phase in
  between. A developer can build a grounded Codemap-based understanding of
  the relevant code before clicking "send to Devin," then step away during
  execution, then review the PR against that same understanding — the two
  claims are compatible stages of one loop, not a same-claim conflict.

- **Extends**:
  - `blog-cognition-devin-in-windsurf.md` and `blog-cognition-devin-desktop.md`
    — this source, dated 2025-11-04, is chronologically the earliest
    Cognition post in this corpus's Windsurf/Devin product lineage, predating
    both the Windsurf 2.0 / Devin-in-Windsurf launch (2026-04-15) and Devin
    Desktop (2026-06-02). It establishes the "understanding first, then
    delegate" philosophy and names DeepWiki and Ask Devin as prior Cognition
    investments in codebase comprehension that those two later posts do not
    revisit at all — the later posts focus on delegation and multi-agent
    management mechanics, taking comprehension as a given rather than
    re-arguing for it, so this source supplies the philosophical foundation
    those later, mechanics-focused posts build on without restating.
  - `blog-cognition-devin-in-windsurf.md` (linked, per that note's Extraction
    Notes, to a companion post naming a "Semi-Async Valley of Death" mental
    model) — this source explicitly references "the Semi-Async Valley of
    Death" by name in its own text ("as we discussed in the Semi-Async
    Valley of Death, our goal isn't just about speed, it is to help your
    human engineers stay in flow"), giving this corpus a second,
    independent sighting of that term from a different Cognition post, still
    without a formal definition in either source.

- **Novel**: The Codemaps product itself — a generated, navigable, dual-view
  (linked-list / graph) map of a codebase, invoked per-task and injectable
  into an agent prompt via `@{codemap}` syntax — is entirely new to this
  corpus; no existing source note documents a comprehension-artifact product
  distinct from chat-based Q&A or documentation generation. "SWE-1.5" as a
  named Cognition model is new to this corpus. The "Vibeslop" framing and
  the compact claim "to understand is to be accountable" (Claim 8) are new,
  specific articulations of the vibe-coding risk not previously phrased this
  way in this corpus. The proposed open `.codemap` protocol (Claim 11) is a
  novel, currently-unshipped interoperability proposal with no analog
  elsewhere in this corpus.

## Guide Impact

- **Chapter 00 (Principles) / Chapter 04 (Context Engineering)**: Add Claim
  1 (engineering requires understanding, not just code output) and Claim 8
  ("to understand is to be accountable") as a compact, citable definition
  of where vibe coding becomes unsafe — comprehension falling behind code
  growth, not code quality per se. Pair with
  `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 3 for the
  complementary "AI lacks accountability" argument, since both sources
  converge on accountability as the property that must remain with the
  human.

- **Chapter 04 (Context Engineering)**: Add Claim 7 (`@{codemap}` syntax
  injecting a generated, structured comprehension artifact directly into an
  agent prompt) as a concrete, named example of pre-computed structured
  context beating ad hoc prose context for grounding an agent's task — flag
  the "dramatically improve performance" claim as an unquantified vendor
  assertion, not a benchmarked result.

- **Chapter 02 (Harness Engineering)**: Add Claim 6 (two-tier
  list-view-plus-graph-view design, with an expandable "trace guide" for
  deeper explanation) as a second instance, from the same vendor, of the
  fast-skim-plus-deep-drill-down UI pattern already documented for Devin's
  test reports in `blog-cognition-verifying-agentic-development.md` Claim
  10 — useful as a reusable design pattern for any tool surfacing agent- or
  AI-generated analysis to a human reviewer.

- **Chapter 01 (Daily Workflows)**: If the guide discusses onboarding to
  unfamiliar codebases, add Claim 2's cited (not Cognition's own) onboarding-
  tax figures only with an explicit caveat that they are third-party,
  hyperlinked citations relayed by a vendor to motivate its own product, not
  independently verified by this extraction.

## Extraction Notes

- WebFetch's summarizing pass declined to reproduce article text verbatim
  (citing an internal ~125-character quote-length constraint), consistent
  with the same difficulty already recorded in this corpus's other Cognition
  source notes (e.g. `blog-cognition-devin-in-windsurf.md`,
  `blog-cognition-devin-desktop.md` Extraction Notes). The full article was
  instead fetched via `curl` with a browser user-agent, HTML tags stripped
  with a Python script, and all quotes above were taken from that
  raw-text extraction, which was read in full (the article is short, ~700
  words across an intro, "Why Codemaps?", "Our solution," "Fight back
  against Vibeslop," and "What's Next" sections).
- No sub-pages were followed. The only inline hyperlinks in the article
  body are: three citation links behind the onboarding-tax figures (Claim
  2 — an "estimates" link, a "source" link, and a second "source" link for
  the Stripe figure) and a reference to "the Semi-Async Valley of Death,"
  which is the same term already followed and recorded (from a different
  Cognition post) in `blog-cognition-devin-in-windsurf.md`'s Extraction
  Notes. Neither set of links was re-fetched here: the three citation links
  are footnote-style attributions to figures already fully quoted above
  (following them would add a third party's data, not more of this source),
  and the Semi-Async Valley of Death term is already documented in this
  corpus as an unglossed mental-model reference, so re-fetching it would
  not add new information beyond what is already recorded.
- Publish date (2025-11-04) is read from the page's own byline
  ("11.04.25"), interpreted in the same MM.DD.YY format used consistently
  across this corpus's other Cognition posts (verified against the site's
  own "Articles" footer list on the same page, which shows other posts in
  the same format, e.g. "06.02.26," "04.15.26," ordered most-recent-first
  and all later than this post's date — consistent with this being an
  older article surfaced alongside newer ones in a generic "latest
  articles" footer, not a sign of a misread date).
- Cross-references verified before writing: re-read
  `blog-simonwillison-vibe-coding-agentic-engineering.md` in full and
  confirmed Claim 3 by number and content; re-read
  `blog-cognition-verifying-agentic-development.md` in full and confirmed
  Claims 5 and 10 by number and content; re-read
  `blog-cognition-devin-in-windsurf.md` in full, including its Extraction
  Notes' account of the Semi-Async Valley of Death reference; re-read
  `blog-cognition-devin-desktop.md` in full. No claim number was guessed or
  approximated.
- No contradiction meeting the MINER.md §4a filing bar was identified — see
  Cross-References → Contradicts for the one candidate considered and
  rejected as describing different phases of one workflow rather than a
  same-claim conflict. No contradiction issue filed.
