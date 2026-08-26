---
source_url: https://vercel.com/blog/how-sandstone-grew-40x-in-147-days-on-vercel
source_type: blog-post
title: "How Sandstone grew 40x in 147 days on Vercel"
author: Susan Aziz, Madison McIlwain, Ben Sabic (Vercel); contributor Eric Dodds
date_published: 2026-07-27
date_extracted: 2026-08-26
last_checked: 2026-08-26
status: current
confidence_overall: anecdotal
issue: "#2971"
---

# How Sandstone grew 40x in 147 days on Vercel

> Single-customer case study: Sandstone, a legal-intake/workflow startup,
> attributes 40x revenue growth and a $30M Series A in under six months to
> three Vercel infrastructure properties — fast preview deployments, a
> composable AI SDK stack, and a named "Secure Compute" private-networking
> product — all described through one named executive (CTO Liam Germain)
> with no independent metrics beyond the top-line growth and Series A
> figures.

## Source Context

- **Type**: blog-post (official Vercel Blog customer story, `vercel.com/blog`,
  published July 27, 2026; canonical URL is `vercel.com/customers/...`, see
  Extraction Notes). Three named Vercel authors (Susan Aziz, Madison
  McIlwain, Ben Sabic) plus a contributor (Eric Dodds), auto-discovered from
  Vercel's trusted Atom feed.
- **Author credibility**: First-party vendor marketing content — Vercel
  publishing a customer's growth story to promote its own platform. All
  quantitative claims (40x revenue growth, $30M Series A, 1,000+ daily
  requests, "five minutes" for a production fix) are self-reported by
  Sandstone via a single named individual, CTO and co-founder Liam Germain,
  who is the only person quoted. No other Sandstone employee, no
  independent customer of Sandstone's, and no third-party source (investor,
  press coverage of the raise) is cited. As with the ABC Legal case study
  already in the corpus (`blog-anthropic-abc-legal-managed-agents.md`), a
  company with a weak or average outcome would not be the subject of a
  featured vendor case study — the entire piece exists to make Vercel look
  good, which does not make the claims false but does mean they are
  unaudited and one-sided.
- **Scope**: Covers Sandstone's product (legal request intake/triage/context
  assembly for in-house legal teams), its founding team composition, three
  Vercel platform properties Germain credits for growth (preview
  deployments, the AI SDK stack, Secure Compute), a brief mention of how
  Sandstone connected with Vercel (Sequoia startup partnership), and
  top-line growth/funding results. Does **not** cover: Sandstone's pricing,
  its actual AI model provider(s) (Claude, GPT, or otherwise — not named
  anywhere in the piece), any specific agent architecture or prompt design,
  engineering headcount, any metric other than "1,000+ legal requests...
  daily" and the 40x/Series A figures, or any customer of Sandstone's by
  name.

## Extracted Claims

### Claim 1: Sandstone attributes its growth to three specific Vercel platform properties — preview-deployment speed, AI SDK composability, and Secure Compute's simplified security story — not to Vercel generally
- **Evidence**: The article's own explicit three-item framing, stated
  immediately after the top-line growth figure and used as the piece's
  section structure (each of the three becomes its own H2/H3 section).
- **Confidence**: anecdotal (single customer's self-reported causal
  attribution; no counterfactual or comparison to what growth would have
  looked like on another platform)
- **Quote**: "That attention to detail has paid off: in less than 6 months after their launch, their revenue grew 40x. Three things made their growth possible on Vercel: Preview deployments fast enough to win enterprise trust / An AI layer flexible enough to ship agentic workflows in minutes / Secure Compute that makes security a one-sentence answer"
- **Our assessment**: Framing growth as caused by exactly three named
  platform properties is a clean marketing structure, and the article gives
  no way to weigh the three against each other or against non-Vercel
  factors (the founding team's legal-domain credibility, described
  separately in Claim 8, is itself offered as a growth explanation).
  Treat this as Vercel's/Sandstone's chosen narrative frame, not a
  validated causal analysis.

### Claim 2: A customer-requested scrollbar accessibility fix went from report to live production in five minutes on a Sunday, which Germain says would have taken five to ten times longer on another platform
- **Evidence**: Narrated anecdote attributed to Germain by the article
  authors (not rendered as a direct first-person quote for this specific
  detail — see Our assessment), used to open the "Deployment Speed" section.
- **Confidence**: anecdotal (single, unverified incident; "five to ten
  times longer" is Germain's own unsubstantiated comparison to unnamed
  "other platforms," not a measured benchmark)
- **Quote**: (no direct first-person quote for this anecdote; see paraphrase below — the article's own prose is: "Liam Germain, Co-Founder and CTO, puts it simply: when a customer asked for a scrollbar accessibility change on a Sunday, he had it live in production in five minutes. On any other platform, he said that same change would have taken five or ten times longer.")
- **Our assessment**: This is the article's most concrete, specific
  incident (a named day, a named change type, a named time-to-production),
  which makes it more falsifiable than the vaguer claims elsewhere in the
  piece — but it is still a single self-reported anecdote with no
  corroborating detail (which platform Sandstone compares against, whether
  "five minutes" includes code-review time, whether this was a genuinely
  representative fix or a best-case example chosen for the story).

### Claim 3: Preview branches with inline commenting are, in Germain's own words, the single most time-saving Vercel feature for Sandstone
- **Evidence**: Direct first-person quote, presented as a pull-quote
  attributed to Germain by name and title.
- **Confidence**: anecdotal (subjective ranking by one executive, no
  quantification of "saved time")
- **Quote**: "Nothing has saved us more time than Vercel preview branches with comments."
- **Our assessment**: This is a genuine direct quote (verified in raw page
  HTML as a blockquote attributed to Germain, not an AI-summarized
  paraphrase), but it is a superlative with no supporting metric — "most
  time-saving" relative to what baseline is not stated. Useful as
  practitioner sentiment, not as an engineering benchmark.

### Claim 4: Vercel Toolbar comments on a live marketing page are configured to automatically create and assign a Linear issue to engineering, collapsing a workflow that used to take an afternoon into a single comment
- **Evidence**: Direct product-mechanism description specific to
  Sandstone's own configuration (not a generic description of what Toolbar
  can do — the Linear auto-assignment is described as something Sandstone
  itself configured).
- **Confidence**: settled (specific, mechanistic description of a concrete
  workflow, though the "used to take an afternoon" baseline is unquantified)
- **Quote**: "Preview branches with inline commenting mean Sandstone's head of marketing can leave a note on a live landing page with Vercel Toolbar, which is configured to automatically creates a Linear issue and assigns it to engineering. What used to take an afternoon happens in a single comment."
- **Our assessment**: This is the most concrete, reusable workflow pattern
  in the source: a non-engineer (head of marketing) can generate a
  triaged, assigned engineering ticket directly from a live preview without
  going through a separate bug-tracker UI or a human relay step. It is a
  specific instance of the toolbar-comment-to-ticket integration pattern,
  distinct from AI-agent-authored work — the ticket still requires an
  engineer to act on it.

### Claim 5: Sandstone runs a monorepo of 7+ applications across multiple Vercel projects, with environment-variable linking, a custom CLI built on Vercel's API layer, and an automatic preview generated on every push to every repo
- **Evidence**: Direct architectural description, plus the same figure
  repeated as a headline bullet at the top of the article.
- **Confidence**: settled (specific, falsifiable infrastructure description
  — app count, CLI existence, per-push preview behavior — though unaudited
  by a third party)
- **Quote**: "Sandstone runs a monorepo of over seven applications across multiple Vercel projects with clean environment variable linking and a custom CLI built on top of Vercel's API layer, and every push on every repo generates a preview of production."
- **Our assessment**: Building a custom CLI on top of Vercel's own API
  layer (rather than relying solely on the platform's built-in dashboard/CLI)
  suggests Sandstone needed cross-repo orchestration Vercel's stock tooling
  didn't provide out of the box — a detail the article doesn't elaborate on
  (what the custom CLI actually automates beyond what `vercel` CLI already
  does is not described). The underlying claim — monorepo + automatic
  per-push previews at 7+ app scale — is a concrete data point on
  Vercel's preview-deployment model applied to a larger-than-trivial
  application surface.

### Claim 6: Sandstone's AI stack is built entirely on Vercel's AI SDK family — Chat SDK for the Teams integration, Emulate SDK for Slack/Okta integration testing, Agent Browser SDK for local agentic testing, and Flags SDK for toolbar integration — described as "one SDK, four workflows, zero separate infrastructure"
- **Evidence**: Direct product-composition description naming four specific
  SDKs and their respective roles.
- **Confidence**: settled (specific, named product list, though "zero
  separate infrastructure" is the article's own summarizing claim rather
  than an independently verified architecture audit)
- **Quote**: "The composability shows up across the entire stack. Chat SDK powers the Teams integration. Emulate SDK handles integration testing for Slack and Okta. Agent Browser SDK runs agentic testing locally. Flags SDK drives the toolbar integration. One SDK, four workflows, zero separate infrastructure."
- **Our assessment**: This is the article's most specific technical
  inventory, but it names *product surfaces* (which SDK powers which
  integration) without describing *what the workflows actually do* beyond
  the "searching procurement agreements... alerting via Slack" summary
  given elsewhere in the piece (see Concrete Artifacts). Notably, the
  article never names which LLM/model provider sits underneath the AI SDK
  calls — this is infrastructure-composability marketing, not a model or
  prompt-engineering case study.

### Claim 7: Germain says adding a new tool to Sandstone's AI SDK setup takes about ten minutes, which he credits with making shipping easy and gives as his reason for trusting Vercel to stay "front of market"
- **Evidence**: Direct first-person quote attributed to Germain by name and
  title, presented as a pull-quote.
- **Confidence**: anecdotal (single executive's estimate, no definition of
  what "adding a tool" entails or whether ten minutes is typical vs.
  best-case)
- **Quote**: "I could add a new tool to our AI SDK setup in ten minutes. It's just made shipping super easy, and we trust that Vercel is front of market in terms of what's available."
- **Our assessment**: "Ten minutes to add a tool" is a specific, quotable
  number, but it's unclear whether this describes wiring an existing
  AI SDK tool integration into Sandstone's agent or building a genuinely
  new tool from scratch — the article gives no example of what tool was
  added. Read as directional evidence for AI SDK's tool-composition
  ergonomics, not a benchmarked or reproducible figure.

### Claim 8: Sandstone uses Vercel Secure Compute to keep all communication between Vercel and its data layer private and off the public internet, which the article frames as turning enterprise security conversations into a one-sentence answer
- **Evidence**: Direct product-mechanism description plus a supporting
  Germain quote about Vercel's pace of innovation (used in the same
  section but not specifically about Secure Compute's mechanics).
- **Confidence**: emerging (the mechanism claim — private communication,
  no public-internet exposure — is stated as fact but with no architecture
  diagram, no mention of which cloud/network boundary Secure Compute
  establishes, and no description of what "data layer" means for
  Sandstone specifically)
- **Quote**: "Sandstone uses Vercel Secure Compute to establish private communication between Vercel and its data layer. The setup was straightforward to implement and well-architected enough that it became a point of confidence rather than friction in every enterprise conversation. When the security question comes up with customers and prospects, and it always does, the answer is simple: all communication between Vercel and Sandstone's data layer is private and never touches the public internet."
- **Our assessment**: "Vercel Secure Compute" does not appear as a named
  product anywhere else in the corpus (the closest corpus analogs — Vercel
  Connect's short-lived per-task credentials and Bring Your Own Cloud's
  customer-VPC compute isolation, both in
  `blog-vercel-enterprise-apps-and-agents.md` — address a different
  problem: credential scope and compute location, not network-path
  privacy between Vercel and a customer's own data layer). This source is
  the corpus's first documentation of Secure Compute as a distinct named
  product; treat the "point of confidence... in every enterprise
  conversation" framing as a single customer's endorsement, not
  independent verification of the product's security properties.

### Claim 9: Sandstone applies the same "will this be ahead of the market in three to five years" evaluation framework to both frontier model providers and core infrastructure vendors, and judges Vercel to be the only platform moving at their pace
- **Evidence**: Direct statement of Sandstone's stated vendor-selection
  philosophy, followed immediately by a supporting Germain quote.
- **Confidence**: anecdotal (self-described internal decision framework,
  no description of what alternative platforms were evaluated or rejected
  under it)
- **Quote**: "Sandstone chooses platforms they believe will be ahead of the market in three to five years, a vendor evaluation framework they apply to both frontier model providers and core infrastructure."
- **Quote (Germain)**: "Vercel is the only platform that moves at our pace. Every day in my dev tools channel there's something new. No other company is pushing the industry forward like that."
- **Our assessment**: This is notable mainly for treating "frontier model provider" and "core infrastructure" as the same category of build-vs-buy decision, evaluated by the same forward-looking criterion — a framing relevant to any guide discussion of vendor-selection strategy for AI-native startups, though the article gives no specifics on which model providers or competing infrastructure platforms were actually compared.

### Claim 10: Sandstone connected with Vercel through the Sequoia startup partnership within ten days of founding, which gave them a shared Slack channel and direct access to Vercel engineers for real-time architecture discussions
- **Evidence**: Direct factual description of how the vendor relationship
  began, with a specific timeframe ("within ten days of starting the
  company").
- **Confidence**: settled (specific, falsifiable claim about program
  mechanics and timing, though unaudited)
- **Quote**: "Sandstone connected with the Vercel team through the Sequoia startup partnership. Within ten days of starting the company, the program gave them a shared Slack channel and access to engineers who could help think through architecture decisions in real time."
- **Our assessment**: This surfaces an under-documented growth-accelerant
  in the corpus: investor-brokered vendor relationships (Sequoia's startup
  program connecting a portfolio company directly to a platform vendor's
  engineers) as a distinct channel from self-serve platform adoption. It
  complicates the article's own "our infrastructure choices caused our
  growth" narrative (Claim 1) — direct engineer access via an investor
  program is a resource not equally available to a startup that simply
  signs up for Vercel without a Sequoia connection, which the guide should
  flag if citing this piece as general infrastructure-selection advice.

### Claim 11: Within six months of launch, Sandstone grew revenue 40x, landed customers in technology, manufacturing, and ecommerce, and raised a $30M Series A led by Lightspeed
- **Evidence**: Top-line growth and funding figures, stated twice in the
  article in near-identical wording (once in the intro, once in the
  closing "What's next" section).
- **Confidence**: anecdotal (self-reported growth multiple with no
  disclosed starting revenue base, making "40x" impossible to sanity-check
  in absolute terms; the Series A amount and lead investor are the kind of
  claim easiest to independently verify but were not cross-checked against
  an independent source such as a funding-announcement press release for
  this note)
- **Quote**: "Less than 6 months after launch, Sandstone had grown revenue 40x and landed customers across technology, manufacturing, and ecommerce, leading to a $30M Series A led by Lightspeed."
- **Our assessment**: The article's own title and URL slug claim "40x in
  147 days," but the number 147 never appears anywhere in the article's
  body text — the body consistently says "less than 6 months" (roughly
  183 days), never the precise 147-day figure. This is worth flagging
  explicitly: the single most attention-grabbing number in the piece (the
  147) is unsubstantiated by the article's own prose, which is looser
  ("less than 6 months") everywhere it actually describes the timeframe.
  A 40x multiple with no disclosed base revenue also cannot be sanity-checked
  as either a large absolute number or a small one growing off a tiny base.

### Claim 12: Sandstone's founding team combines a McKinsey legal tech veteran, a lawyer-turned-engineer, and a cybersecurity founder, and the article attributes Sandstone's product/domain credibility with legal buyers to legal professionals and engineers working side by side
- **Evidence**: Direct description of founding-team composition, followed
  by an explicit causal claim linking that composition to product quality
  for a "demanding" buyer segment.
- **Confidence**: anecdotal (a qualitative claim about team composition
  driving product-market fit for enterprise legal buyers, with no specific
  example of a "workflow detail" or "legal nuance" the team caught that a
  purely technical team would have missed)
- **Quote**: "The founding team includes a McKinsey legal tech veteran, a lawyer-turned-engineer, and cybersecurity founder. At Sandstone, that mix shows up directly in the product: legal professionals work alongside engineers, catching the workflow details and legal nuances that only someone who has practiced law would notice. That is how Sandstone ships fast and correctly for one of the most demanding buyers in enterprise software."
- **Our assessment**: This is a domain-expertise-embedded-in-the-building-team
  claim, structurally similar to the "practitioner + engineer" framing this
  corpus already documents inside a legal department for AI-adoption
  purposes (`blog-anthropic-claude-legal-industry.md`, `blog-anthropic-legal-industry-deploy.md`)
  — but applied here to the vendor's own founding team building a product
  *for* legal departments, not to an internal legal team adopting AI
  tooling. It's a plausible mechanism for enterprise trust with a
  regulated, detail-sensitive buyer, but the article offers no concrete
  example (a specific bug, a specific workflow nuance) to substantiate it.

## Concrete Artifacts

```
Sandstone product description (verbatim, article meta description and
"About Sandstone" closing section)
Source: https://vercel.com/blog/how-sandstone-grew-40x-in-147-days-on-vercel

"Sandstone is the Legal Relationship Management system that coordinates
a delightful day-to-day for legal departments."

"Sandstone was born out of the acute frustration experienced by in-house
legal teams who spend more time on process than progress due to
fragmentation across disparate business systems. The platform provides a
comprehensive solution for intake, triage, execution, fulfillment, and
measurement of legal work, designed to run across email, messaging, and
the business tools teams already use."
```

```
Sandstone's agentic workflow, as described (verbatim)
Source: same article, "AI SDK unlocks faster agentic workflows" section

"Sandstone has evolved into an AI system that executes complex,
multi-step legal workflows end-to-end, searching through thousands of
procurement agreements, surfacing the most at-risk agreements, alerting
owners via Slack, and notifying legal when responses come in."

Upstream context problem this replaced (verbatim, opening section):
"When in-house legal teams get a request from their business, it kicks
off a manual process of pulling data from multiple systems. In a typical
workflow, lawyers will pull deal details from Salesforce, review past
contracts, and chase account teams for missing context, all before they
start the legal work itself. Sandstone automates this data gathering
process, and centralizes requests into a single platform. When a request
is created, Sandstone automatically ingests context from every system,
including messaging and email tools."
```

```
Sandstone on Vercel — headline metrics (verbatim bullet list)
Source: same article, "Sandstone on Vercel" summary box

- 1,000+ legal requests managed daily across customer teams
- 7-app turborepo monorepo deployed seamlessly to multiple Vercel projects
- Multi-step agentic legal workflows built end-to-end with AI SDK
```

```
Sandstone's stated product vision (verbatim)
Source: same article, "What's next" section

"The vision they are building toward is a Legal Relationship Management
platform that not only manages intake but also connects every workflow
to the business context behind it, flags issues before they surface, and
operationalizes legal knowledge through supervised agents. Sandstone
describes this as a system of action for the legal department of the
future."
```

## Cross-References

- **Corroborates**:
  - `blog-vercel-flags-platform-native-feature-flags.md` Claim 7 ("Because
    every new feature is built behind a flag, developers merge to `main`
    continuously without releasing unfinished work") and Claim 8 (v0's
    staged rollout, kill-switch-without-redeploy): this source's Claim 1/
    description of "Vercel Flags runs feature flags across all
    applications, giving the team dynamic control over what is live, what
    is demoed, and what is still in progress, without touching a
    deployment" is a second, independent customer (Sandstone, not
    Vercel's own v0 team) reporting the same dynamic-control-without-
    redeploy value proposition for Vercel Flags. This strengthens that
    note's "emerging" confidence rating on real-world flag usage patterns
    with a genuinely external adopter, rather than Vercel's own dogfooding
    example.
  - `blog-anthropic-abc-legal-managed-agents.md` Claim 1 (self-reported,
    unaudited quantitative metrics in a vendor-published single-customer
    legal-AI case study): both sources share the identical evidentiary
    shape — a vendor blog, one named executive quoted, headline metrics
    with no independent audit — applied to a legal-domain AI product. This
    corroborates that vendor customer case studies remain the dominant
    evidence type for legal-AI adoption claims in this corpus, with the
    same limitations (self-reported figures, promotional selection bias)
    recurring across vendors (Anthropic, Vercel) and companies (ABC Legal,
    Sandstone).

- **Contradicts**: None identified. No claim here materially opposes a
  claim in an existing source note; the internal title-vs-body discrepancy
  on the "147 days" figure (Claim 11) is a discrepancy within this single
  source, not a disagreement with another source note, and does not rise
  to a MINER.md §4a contradiction (no guide advice would differ depending
  on whether the true figure is 147 days or "less than 6 months" — both
  describe the same rapid-growth claim at different precision).

- **Extends**:
  - `blog-vercel-enterprise-apps-and-agents.md` (Vercel Connect's
    short-lived per-task credentials, Claim 4; Bring Your Own Cloud's
    customer-VPC compute isolation, Claim 9): this source's Claim 8
    documents a third, previously-uncatalogued Vercel security/networking
    product — Secure Compute, for private Vercel-to-data-layer
    communication — extending the corpus's picture of Vercel's
    enterprise-security product surface beyond credential scoping (Connect)
    and compute location (BYOC) to network-path privacy specifically.
  - `blog-anthropic-claude-legal-industry.md` Claim 1 (legal work's native
    tech stack — CLM, DMS, e-discovery, data rooms, research platforms —
    is the gap Anthropic's MCP connectors are designed to close): this
    source's context-ingestion description ("Sandstone automatically
    ingests context from every system, including messaging and email
    tools," "lawyers will pull deal details from Salesforce, review past
    contracts") describes the same underlying legal-context-fragmentation
    problem from the product-vendor side rather than the AI-lab-connector
    side — a startup building its own integration layer (on Vercel's AI
    SDK, model provider unstated) rather than a customer adopting
    Anthropic's pre-built MCP connectors. Useful as a second, independently
    arrived-at description of the same problem space from a different
    vendor stack.

- **Novel**:
  - **"Vercel Secure Compute" as a named product** (Claim 8): not
    previously documented anywhere in the corpus, distinct in stated
    purpose from Vercel Connect and BYOC.
  - **Preview-comment-to-Linear-ticket auto-assignment** (Claim 4): the
    corpus's first concrete example of a non-engineer (a head of marketing)
    generating a triaged, assigned engineering ticket directly from a live
    preview-deployment comment, without a separate bug-tracker step.
  - **Investor-program-brokered vendor engineering access** (Claim 10):
    the Sequoia startup partnership as a distinct growth-accelerant channel
    (direct engineer access within 10 days of founding) is not documented
    elsewhere in the corpus's vendor-adoption sources, which otherwise
    describe self-serve or sales-led adoption paths.
  - **"Vendor evaluation framework applied equally to frontier model
    providers and core infrastructure"** (Claim 9): the corpus's first
    example of a company explicitly stating it uses one evaluation
    criterion (durability of market leadership, 3-5 years out) across both
    categories of AI-native vendor decision, rather than treating "which
    model" and "which infrastructure platform" as separate decision
    processes.

## Guide Impact

- **Chapter 02 (Harness Engineering — deployment infrastructure)**: Add
  Claim 4 (Toolbar comment → automatic Linear ticket, assigned to
  engineering) as a concrete example of collapsing a non-engineer's
  feedback into an actionable engineering artifact with zero manual
  triage step, citing this source alongside the corpus's other
  agent-addressable/automation-first tooling examples (e.g. the
  agent-native `vercel flags` CLI documented in
  `blog-vercel-flags-platform-native-feature-flags.md` Claim 4). Note the
  limitation explicitly: this automates ticket *creation*, not resolution
  — an engineer still has to act on it.

- **Chapter 02 or Chapter 05 (Security & Governance)**: Add "Vercel Secure
  Compute" (Claim 8) as a newly-documented named product for private
  compute-to-data-layer networking, distinct from credential scoping
  (Connect) and compute-location isolation (BYOC) already in the guide's
  Vercel security-product coverage via `blog-vercel-enterprise-apps-and-agents.md`.
  Flag it as single-customer-endorsed, not independently architecturally
  verified.

- **Chapter 05 (Team Adoption / Growth)**: If the guide discusses
  vendor-selection or infrastructure-choice narratives for AI-native
  startups, cite Claim 10 (Sequoia-brokered direct engineer access) as a
  caveat against generalizing "our infrastructure choice caused our
  growth" case studies — access to a vendor's own engineers via an
  investor relationship is a resource not available to every reader
  evaluating the same platform.

- **General accuracy/citation hygiene note (not chapter-specific)**: If the
  guide ever cites this source's headline "40x in 147 days" framing, note
  that "147 days" appears only in the title/URL/metadata and is never
  stated in the article's own body text (Claim 11) — the body consistently
  uses the looser "less than 6 months." Cite the growth claim as "40x in
  under six months" rather than repeating the more precise but
  unsubstantiated 147-day figure as if the article itself supports that
  precision.

## Extraction Notes

- **Two URLs for the same article.** The issue and Vercel's Atom feed cite
  `https://vercel.com/blog/how-sandstone-grew-40x-in-147-days-on-vercel`,
  which redirects (HTTP 308) to the canonical
  `https://vercel.com/customers/how-sandstone-grew-40x-in-147-days-on-vercel`.
  Both resolve to identical article content. `source_url` above uses the
  issue-filed `/blog/` URL per the task instructions.
- **Verified against raw HTML, not WebFetch summarization alone.** An
  initial WebFetch pass returned plausible but non-verbatim prose (e.g. it
  rendered section content as "AI Infrastructure" / "Security Architecture"
  / "Growth Results" H2 headings that do not exist in the actual page
  markup — the real headings are "Vercel deployments turned a Sunday
  request into a five-minute fix," "Without the right foundation,
  complexity kills velocity," "AI SDK unlocks faster agentic workflows,"
  and "Vercel Secure Compute makes security a one-sentence answer"). Per
  MINER.md §2a, the page's raw server-rendered HTML was fetched directly
  via `curl` and every quote used above was located and confirmed
  character-for-character in that raw HTML before inclusion. Claim 2's
  scrollbar-fix anecdote is explicitly marked as narrated prose rather
  than a first-person quote because, on inspection of the raw HTML, that
  specific sentence is the article authors' own paraphrase of Germain
  ("puts it simply: ... he had it live... he said..."), not text inside a
  blockquote/quotation attributed directly to him — unlike the four other
  Germain quotes in this note (Claims 3, 7, 8's supporting quote, 9), which
  are rendered as direct blockquotes in the source HTML.
- **No linked sub-pages followed.** The article contains one substantive
  outbound link (`vercel.com/docs/monorepos`, linked from the word
  "monorepo" in Claim 5) which is a general Vercel documentation page about
  monorepo support, not Sandstone-specific content — per MINER.md §1 this
  was judged peripheral (general product docs, not a companion article
  about this customer) and not fetched as a separate source.
- **No model/vendor name given.** The article never states which LLM
  provider powers Sandstone's "AI system" — this is a deliberate scope gap
  worth noting for anyone using this source to argue about model choice;
  it can only speak to infrastructure/deployment-layer decisions.
- **Confidence set to `anecdotal` overall**: every substantive claim is
  self-reported by a single vendor-selected customer via one named
  executive, with no independent audit, no comparison company, and (for
  the two most attention-grabbing numbers — "147 days" and "40x") an
  internal inconsistency between the article's title and its own body text
  (see Claim 11).
