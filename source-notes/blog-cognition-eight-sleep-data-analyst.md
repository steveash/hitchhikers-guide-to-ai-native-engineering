---
source_url: https://cognition.com/blog/how-eight-sleep-uses-devin-as-a-data-analyst
source_type: blog-post
title: "How Eight Sleep Uses Devin as a Data Analyst"
author: Andrew Foong, Technical Chief of Staff at Eight Sleep
date_published: 2025-09-04
date_extracted: 2026-07-21
last_checked: 2026-07-21
status: current
confidence_overall: emerging
issue: "#2105"
---

# How Eight Sleep Uses Devin as a Data Analyst

> A named customer's first-person account of deploying Cognition's Devin as a
> Slack-integrated data analyst across a small team's dbt/Snowflake/Looker/Amplitude
> stack — a phased "vibe context, then curated knowledge" onboarding, a worked
> incident-investigation example, quantified throughput and adoption outcomes, and
> an explicit (if thinly evidenced) design philosophy for how much of an AI
> analyst's context should be curated versus left open to exploration.

## Source Context

- **Type**: blog-post (published on Cognition's own blog, cognition.com,
  2025-09-04; article metadata confirms `article:published_time` = 2025-09-04).
  Unlike most Cognition-blog source notes already in this corpus, the byline is
  not "The Cognition Team" — it is a named external customer: "By Andrew Foong,
  Technical Chief of Staff at Eight Sleep." The entire article reads in first
  person as the customer's own account, not a Cognition-authored case study
  with an embedded customer quote.
- **Author credibility**: Andrew Foong is identified only by his title
  ("Technical Chief of Staff at Eight Sleep") with no further biographical
  detail given in the post. Eight Sleep is a named, identifiable company (a
  sleep-technology/smart-mattress maker). This is a vendor-hosted customer
  testimonial — Cognition has an obvious incentive to publish only favorable
  accounts, and the piece is unambiguously promotional in framing (headings
  like "Hero moment," a closing pun about a "return offer") — but it is more
  first-person and specific than a marketing-team-authored case study, and it
  discloses concrete operational detail (which systems Devin touches, a
  two-month timeline, a named worked example) rather than only aggregate
  claims.
- **Scope**: Covers how Eight Sleep integrated Devin into its data team's
  workflow (Slack interface, tool access, context-building strategy), one
  worked incident-investigation example, quantified before/after impact
  claims, the author's own two-extremes framework for AI-analyst context
  design, and three specific forward-looking investments the team was piloting
  two months in. Does NOT cover: any accuracy or error-rate metric, the size
  of Eight Sleep's data team or company, dollar cost or pricing, a defined
  denominator for the "3x" claim (features shipped is not stated as an
  absolute count), or any detail on how permissions/access boundaries are
  technically implemented.

## Extracted Claims

### Claim 1: Eight Sleep replaced its small data team as the single funnel for data requests by integrating Devin directly into Slack with access to its full analytics stack — dbt, Snowflake, and Looker natively, plus Amplitude via Devin's web browser
- **Evidence**: Direct description of the integration under "Bringing Devin into the workflow."
- **Confidence**: emerging (specific, named tool integrations for a shipped
  deployment; no detail on how access was technically provisioned or scoped)
- **Quote**: "Instead of forcing people in the team to funnel every question through our small data team, we integrated Cognition's Devin directly into our workflows: Slack as the interface. Anyone can tag Devin in our data channel. Access to our stack. Devin understands our dbt repo, queries Snowflake, uses Looker, and even checks data on Amplitude via its web browser."
- **Our assessment**: The detail that Amplitude access is via "its web browser"
  (i.e., browser-use/computer-use rather than a native API integration) is a
  specific, checkable implementation detail — it implies Eight Sleep did not
  build or need a dedicated Amplitude connector, instead relying on Devin's
  general browsing capability for the one tool without direct API/MCP access.
  This is a smaller-scale, single-team analogue of the four-layer "sources of
  truth" architecture in `blog-anthropic-selfservice-data-analytics.md`
  (semantic layer, lineage, historical SQL, knowledge graph) — Eight Sleep
  names the same category of tool coverage (semantic/BI layer, warehouse,
  behavioral analytics) without the architectural framing or governance layer.

### Claim 2: Eight Sleep deliberately built Devin's context in two phases — first broad, unstructured "vibe context" (repo and tool access only), then layered-in curated knowledge — modeling the approach explicitly on how they would onboard a new human employee or intern
- **Evidence**: Direct description under "Bringing Devin into the workflow," with an explicit analogy to onboarding.
- **Confidence**: anecdotal (single team's own characterization of their process; no measurement of what the curated-knowledge layer specifically improved)
- **Quote**: "Context is king, but needs to be built. We started by just giving Devin our repo and tools (“vibe context”). Then we layered in curated knowledge to help it find the right data. Like training a new employee or intern, we fed it more specific knowledge to support it for each task it took on."
- **Our assessment**: The "vibe context" term (used here and again in Claim 9)
  is the article's most citable coinage — a named, informal label for
  "give the agent broad tool/repo access with no curation" as a deliberate
  starting point, not an accident. Framing context-building as sequential,
  employee-onboarding-like, and task-driven ("more specific knowledge... for
  each task it took on") is a practitioner-level echo of the general
  principle that curated knowledge, not raw access, is what improves
  accuracy — compare `blog-anthropic-selfservice-data-analytics.md` Claim 6
  (skills, not raw retrieval, are the decisive accuracy lever) — though this
  source gives no before/after measurement of the kind Anthropic's team
  reports, only the narrative account that curation was added deliberately
  over time.

### Claim 3: Full setup — from getting Devin access to Eight Sleep's accounts to asking it the first real question in Slack — took only a couple of hours, and Devin began fielding real data requests immediately afterward
- **Evidence**: Direct timeline statement immediately following the context-building description.
- **Confidence**: anecdotal (single, unverified self-reported timeline; no
  definition of what "getting access" entailed — credential provisioning,
  permission review, etc. — so the couple-hours figure may understate any
  upfront IT/security work)
- **Quote**: "The setup only took a couple of hours from getting access to our account to asking Devin my first question via Slack. From there, Devin began fielding real data requests immediately."
- **Our assessment**: This is a strikingly fast time-to-first-value claim,
  directionally consistent with the "get started with minimal upfront
  investment" framing in `blog-anthropic-selfservice-data-analytics.md`
  Claim 15 ("a handful of canonical datasets, a few dozen offline evals, and
  a thin knowledge skill will capture most of the upside") — but the two
  claims measure different things: Anthropic's is about the *scope* of
  initial investment needed for production-grade accuracy; Eight Sleep's is
  about *elapsed clock time* to first use, with the accuracy question left
  entirely unaddressed. The two should not be conflated as the same claim in
  the guide.

### Claim 4: When a new sales dashboard showed an unusually high, suspicious revenue number, Devin independently investigated by tracing the Looker dashboard back through its underlying Snowflake queries and correctly identified the actual cause (a better-than-expected email campaign), rather than a data or model bug
- **Evidence**: A single named worked example under "Hero moment: When revenue looked suspicious," with explicit before/after framing of the competing hypotheses considered.
- **Confidence**: anecdotal (one specific incident, self-reported, not independently verified against Eight Sleep's actual underlying data)
- **Quote**: "Instead of a human analyst burning hours to untangle the logic, we asked Devin to investigate. It traced the Looker dashboard back to the underlying queries, ran checks in Snowflake, and quickly found the culprit: an email campaign that performed better than expected." / "The revenue was real. The model was fine. And Devin had defused what could have turned into a fire drill."
- **Our assessment**: This is the article's single most concrete evidentiary
  artifact — a specific, falsifiable-in-principle claim (dashboard number →
  traced query lineage → identified cause) rather than a vague assertion of
  usefulness. It is also a direct, practitioner-level illustration of exactly
  the "truth under pressure" value proposition that Eight Sleep names
  explicitly in its own impact list (Claim 6 below): resolving a
  "this-number-looks-off" moment by writing and validating the queries needed,
  not by asserting an answer. No detail is given on how long the
  investigation took or whether the "culprit" conclusion was independently
  double-checked by a human before being accepted.

### Claim 5: Since deploying Devin, Eight Sleep reports shipping 3x as many data features and data investigations per week compared to before, where "large requests" include new dbt models, semantic models, and dashboards
- **Evidence**: Direct quantified claim under "The impact," with an explicit definition of what counts as a "large request."
- **Confidence**: anecdotal (a single self-reported multiplier with no absolute
  baseline count, denominator, or measurement methodology disclosed — "3x"
  of an unstated starting number)
- **Quote**: "Faster shipping. We're shipping 3x as many data features and data investigations each week compared to before (large requests involve: new dbt models, semantic models, dashboards)."
- **Our assessment**: The explicit parenthetical scoping ("large requests
  involve...") is a small but useful piece of methodological transparency —
  it tells the reader what kind of work the multiplier covers, rather than
  leaving "data features and investigations" fully undefined. Even so, "3x"
  with no baseline count is a directional claim, not an auditable metric —
  it should be cited in the guide as illustrative, not as comparable to the
  production-scale, held-out-evaluated accuracy figures in
  `blog-anthropic-selfservice-data-analytics.md` Claim 1 (95% automation,
  ~95% aggregate accuracy) or the statistically validated productivity
  estimator in `blog-cognition-devin-productivity-estimation.md` Claim 6
  (r_log = 0.74 on a 233-session held-out set). This source has no comparable
  rigor and should not be presented at the same evidentiary tier.

### Claim 6: The queue of ad-hoc "pull data" requests to the human data team is now near zero, because Devin fields that traffic directly — described by the author as "democratized" data access
- **Evidence**: Direct claim under "The impact," under the heading "Democratized access."
- **Confidence**: anecdotal (self-reported, no queue-length data before/after, no definition of "near zero")
- **Quote**: "Democratized access. Our queue of random “pull data” asks is near zero. Devin now fields ad-hoc requests."
- **Our assessment**: This is the clearest statement of Devin's role as a
  bottleneck-removal mechanism rather than a productivity multiplier for the
  existing data team specifically — the value is framed as eliminating a
  queue, not as making the human data team faster at the same volume of work.
  This is the same "reduce team bottlenecks by giving an agent access to the
  team's tools and knowledge" pattern the Prospector's triage comment
  identified as generalizable beyond data analysis specifically.

### Claim 7: People across Product, Ops, Finance, Growth, and R&D who previously never asked the data team for help are now asking Devin questions directly, because — per the author — people hesitate to interrupt a human colleague out of curiosity but feel no such hesitation asking an AI
- **Evidence**: Direct claim and stated causal mechanism under "The impact," heading "New voices, increased curiosity."
- **Confidence**: anecdotal (author's own interpretation of *why* adoption
  broadened — a plausible but unverified psychological/social explanation, not
  a surveyed or measured behavioral finding)
- **Quote**: "New voices, increased curiosity. People who never asked our team for data before are now using Devin. It turns out folks might hesitate to ping if they're just curious, but never feel guilty about asking an AI. Devin is now answering questions for Product, Ops, Finance, Growth, and R&D."
- **Our assessment**: The specific causal claim — social friction/guilt about
  interrupting a human colleague is lower when asking an AI instead — is a
  distinct and reusable adoption-mechanism hypothesis that is new to this
  corpus (see Cross-References → Novel). It is stated as the author's own
  inference ("it turns out"), not as a surveyed finding, so it should be
  presented in the guide as a plausible adoption driver worth testing for,
  not as an established behavioral result.

### Claim 8: As teammates observed Devin in action inside the shared Slack channel, more employees asked to be onboarded every day, without any formal rollout campaign — an organic, viral internal-adoption pattern the author calls "internal product market fit"
- **Evidence**: Direct claim under "The impact," heading "Organic adoption."
- **Confidence**: anecdotal (self-reported observation, no adoption-rate
  numbers, headcount, or timeline given for how fast access requests grew)
- **Quote**: "Organic adoption. As teammates saw Devin in action, more asked to join. Every day a few new folks see the magic in our Slack channel and ask for access. It really feels like internal product market fit."
- **Our assessment**: This is the same peer-observation-driven adoption
  mechanism already documented at larger scale and higher evidentiary detail
  elsewhere in this corpus: `blog-anthropic-sires-gtm-claude-code.md`
  (Concrete Artifacts → Individual-to-Org Adoption Arc: personal pain point →
  peer Slack sharing within 24 hours → viral adoption → org-wide rollout) and
  `blog-cursor-paypal-enterprise-adoption.md` Claim 1 (organic spread across
  an 8,000-developer org as engineers witnessed peers' results after an
  initial seeded rollout). Eight Sleep's account adds a third, independent
  domain (internal data analytics, at a small-company scale) to a pattern
  this corpus has now observed across GTM tooling, enterprise coding-tool
  rollout, and data analytics — all describing visibility inside a shared
  channel (Slack in every case cited) as the adoption-driving mechanism, not
  top-down mandate.

### Claim 9: The author frames AI-analyst context design as a spectrum between two extremes — heavily curated, prescriptive context (accurate but labor-intensive) and broad, unstructured "vibe context" that lets the agent explore (fast to a first "aha moment" but less accurate) — and concludes that the right point for an AI analyst is "in between but towards exploration," leaning on the fact that Devin, as a coding agent, is unusually good at the exploratory end
- **Evidence**: Direct framework statement under "Building at the frontier of AI analysts," naming both approaches explicitly and stating a preferred position between them.
- **Confidence**: anecdotal (a single practitioner's stated design philosophy,
  not a measured comparison of the two approaches on the same task set)
- **Quote**: "Approach A: Provide as much curated context as possible. Highly prescriptive, but labor-intensive. E.g. When a user asks specifically about revenue, you can only use this table." / "Approach B: Give the AI broad access to what a new analyst would get and let it explore (“vibe context?”). Fastest to the “aha moment”/activation, but less accurate. Devin was great at this, just as you'd expect a coding agent to be." / "Our experience shows the future lies in between but towards exploration."
- **Our assessment**: Eight Sleep explicitly concedes Approach B is "less
  accurate" on its own — consistent with, not opposed to,
  `blog-anthropic-selfservice-data-analytics.md`'s finding that unstructured
  access underperforms structured skills (Claim 6: 21% without skills vs.
  95%+ with them). Where the two sources differ is emphasis and direction of
  travel: Anthropic's evidence argues for investing heavily in a structured
  skills layer to close that accuracy gap; Eight Sleep's stated preference
  leans toward keeping more of the "explore broadly" character and adding
  only "curated heuristics" on top (see Concrete Artifacts), rather than a
  comprehensive skills/governance layer. We considered filing this as a
  contradiction and did not — see Cross-References → Contradicts for the
  reasoning. The guide should present this source's framework as a named,
  citable vocabulary (Approach A / Approach B / "vibe context") for a design
  tension that Anthropic's source addresses with actual measurement and this
  source addresses only with an unmeasured stated preference.

### Claim 10: Eight Sleep treats Devin's query permissions the same way it would treat a human teammate's access — deliberately setting boundaries so Devin is powerful in the areas it should operate in, and restricted wherever compliance or privacy requires it
- **Evidence**: Direct statement under the fourth bulleted AI-analyst
  principle, "Operate with autonomy within clear boundaries."
- **Confidence**: anecdotal (a stated principle with no implementation
  detail — no mention of the specific access-control mechanism, what data is
  restricted, or how boundaries are enforced or audited)
- **Quote**: "Operate with autonomy within clear boundaries. Last, but certainly not least, giving Devin the right permissions is critical (just like your human teammates). By setting clear boundaries on what Devin can query, we make sure it's powerful where we want it to be, and restricted where compliance and privacy demand it."
- **Our assessment**: The "treat Devin's permissions like a human teammate's"
  framing is a clean, reusable mental model for the guide's treatment of
  agent access control in analytics contexts, but it is asserted as a
  principle with zero implementation specifics — contrast with
  `blog-cognition-auto-triage.md` Claim 8, which at least names the
  mechanism (network-sandboxed execution, explicit anti-prompt-injection
  protections) for a comparable "Devin touches sensitive/untrusted data"
  scenario. This source should be cited as evidence that practitioners are
  thinking about analytics-agent permissioning as a first-class design
  concern, not as evidence of any specific control mechanism.

### Claim 11: Two months after deployment, Eight Sleep describes Devin as having grown from a "Jr Analyst" to nearly a "Sr Analyst," attributing this to three concrete, ongoing investments: enriching the dbt semantic layer's metadata via the `meta` field, building an automated pipeline to feed prior-session context back into future sessions plus a Slack bot to crowdsource user corrections, and adopting Cognition's own Metabase MCP server so Devin can generate and screenshot charts directly in Slack
- **Evidence**: Direct description under "Growing Devin from a Jr Analyst to a Sr Analyst," naming three specific, named/linked investments.
- **Confidence**: anecdotal (a single team's self-described two-month
  progression narrative with no before/after measurement of what specifically
  improved as a result of each of the three investments)
- **Quote**: "With Devin, you really get what you put into it 100 fold. Two months ago, Devin started as our Jr Analyst, and is close to becoming our Senior Analyst." / "Augmenting our semantic layer. Context is king. There's no reason not to improve your documentation and semantic layer. So we will be trialing adding additional useful context into our dbt yaml files using the meta field." / "Building a context/feedback loop. We're experimenting with building an automated way to provide Devin with relevant data models and context from prior sessions to improve its retrieval. We're also experimenting with crowd sourcing our knowledge creation by building a Slack bot to ask users for feedback on Devin's answers." / "Experimenting with charting. ... Devin just launched a Metabase MCP server that Devin can use to create charts and screenshot them back to users in Slack."
- **Our assessment**: The "context/feedback loop" investment (an automated
  pipeline surfacing prior-session context, plus a Slack bot soliciting
  user corrections) is a lightweight, single-team analogue of the
  "correction harvesting" production pattern documented in far more
  operational detail in `blog-anthropic-selfservice-data-analytics.md`
  Claim 14 (a scheduled agent that scans stakeholder channels for correction
  language, drafts reference-doc fixes, and opens PRs to the domain owner).
  Eight Sleep's version is explicitly described as still experimental
  ("we're experimenting with") rather than a shipped, running system, and
  there is no PR/governance loop described — corrections appear to feed
  retrieval directly rather than through a reviewed-fix workflow. This is a
  smaller-scale, less mature version of the same underlying idea
  (user-signaled corrections closing the staleness gap), not an independent
  invention of it.

## Concrete Artifacts

### Tool integration and impact, verbatim (from the article)

```
Source: cognition.com/blog/how-eight-sleep-uses-devin-as-a-data-analyst,
"By Andrew Foong, Technical Chief of Staff at Eight Sleep," 09.04.25

Integration:
- Slack as the interface. Anyone can tag Devin in our data channel.
- Access to our stack. Devin understands our dbt repo, queries Snowflake,
  uses Looker, and even checks data on Amplitude via its web browser.

Impact (five headline items, verbatim):
- Faster shipping: "shipping 3x as many data features and data
  investigations each week compared to before (large requests involve:
  new dbt models, semantic models, dashboards)"
- Democratized access: "Our queue of random 'pull data' asks is near
  zero. Devin now fields ad-hoc requests."
- Truth under pressure: "Devin has helped us resolve 'this number looks
  off' moments multiple times, writing the exact queries needed to
  validate results."
- New voices, increased curiosity: Devin now answers questions for
  "Product, Ops, Finance, Growth, and R&D"
- Organic adoption: "Every day a few new folks see the magic in our
  Slack channel and ask for access."
```

### AI-analyst design framework, verbatim (from the article)

```
Source: ibid., "Building at the frontier of AI analysts"

Approach A: "Provide as much curated context as possible. Highly
  prescriptive, but labor-intensive. E.g. When a user asks specifically
  about revenue, you can only use this table."
Approach B: "Give the AI broad access to what a new analyst would get
  and let it explore ('vibe context?'). Fastest to the 'aha moment'/
  activation, but less accurate."
Stated conclusion: "Our experience shows the future lies in between but
  towards exploration."

Four named requirements for AI analysts:
1. "Grok your stack. Understand dbt, LookML, and dashboards directly."
2. "Leverage curated heuristics. Analysts can capture how we think about
   data without having to prescribe every dataset."
3. "Learn like an employee. Through memory, context injection, and
   feedback loops, AI analysts should improve just like new hires do."
4. "Operate with autonomy within clear boundaries... giving Devin the
   right permissions is critical (just like your human teammates)."
```

### Companion technical guide (followed links, not the primary source)

Two linked Cognition posts — "Build Your Own AI Data Analyst" Part 1
(`devin.ai/ai-data-analyst-1`) and Part 2 (`devin.ai/ai-data-analyst-2`),
both byline "Cognition Team," August 2025 — were followed per MINER.md §1
because the Eight Sleep article links to Part 2 for its Metabase MCP
server. These describe Cognition's *own* internal dogfooding of the same
Devin-as-analyst pattern (a separate, first-party case, not Eight Sleep's),
and provide a concrete practitioner setup pattern absent from the Eight
Sleep post itself:

```
Source: devin.ai/ai-data-analyst-1, "Cognition Team," August 2025

Cognition's own stated motivation and estimate:
"Previously, knowledge fragmentation made it extremely difficult to trace
data anomalies back to their source or ask new questions... Getting
answers often took days or weeks. Now, it takes minutes."

"This type of work is now repeated dozens of times every day across our
company. If you assume that every question would take an hour to answer,
we estimate that it would take a data team 150+ hours per month to do
this work manually. With Devin, we can do it in minutes."
```

```
Source: devin.ai/ai-data-analyst-2, "Cognition Team," August 2025

Setup pattern (Quick Start Guide, verbatim steps, condensed):
1. Install integrations from the "MCP Marketplace" for target databases
   (PostgreSQL, Firestore, Looker, SQL Server supported out of the box
   via Google's MCP Toolbox for Databases), or "Add Your Own"
2. Configure DB credentials
3. Click "Use MCP" to start a first session
4. Add "Knowledge" for Devin to use during analysis, attached to an
   invocation macro (e.g. `!analytics`) so any teammate can trigger it
   by name in a Slack message

Example Knowledge file content (verbatim, attributed to the article):
"## Purpose:
**Querying Redshift Data Warehouse:**
When you need to answer data-related questions or obtain analytics by
querying the Redshift data warehouse, you should use the `mcp-cli` tool.

## Guidelines when using this knowledge:
- Get the complete db schema to see what tables and columns are
  available using the `database://structure` resource
- Read the README.md docs in the analytics repo... to learn what the
  most important tables on the analytics schema are.
- Read all of the docs.yml files to learn about the analytics schema.
- ...
- Strongly prefer to use mart models... before int_ and stg_ models
- Strongly prefer to query tables under the analytics schema, before
  querying any other schemas like the devin or billing schemas (raw
  tables)
- If unsure, confirm with the user."

Output-format instruction (verbatim):
"When running queries against redshift and providing the user with a
final answer, always show the final query that produced the result
along with the result itself, so that the user is able to validate the
query makes sense."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-selfservice-data-analytics.md` Claim 6 ("Skills are the
    decisive accuracy lever — without skills, accuracy stays at 21%; with
    skills, accuracy rises above 95%") and Claim 7 (raw retrieval barely
    helps): this source's Claim 9 independently concedes that its own
    "vibe context" (unstructured, broad-access) approach is "less accurate"
    on its own, and its Claim 2/Claim 11 layering-in-curated-knowledge
    narrative describes the same qualitative direction (structure improves
    outcomes) that Anthropic's team quantifies precisely. This is a
    practitioner-anecdote-tier corroboration of a claim Anthropic's source
    establishes with production ablation data.
  - `blog-anthropic-selfservice-data-analytics.md` Claim 14 (automated
    correction harvesting: a scheduled agent scans stakeholder channels,
    drafts reference-doc fixes, and opens PRs to the domain owner): this
    source's Claim 11 "context/feedback loop" (crowdsourcing corrections via
    a Slack bot, feeding prior-session context back into future retrieval)
    is a smaller-scale, explicitly experimental version of the same
    underlying idea — user-signaled corrections closing a staleness/accuracy
    gap — from an independent, much smaller team.
  - `blog-anthropic-sires-gtm-claude-code.md` (Concrete Artifacts →
    Individual-to-Org Adoption Arc) and `blog-cursor-paypal-enterprise-adoption.md`
    Claim 1 (organic, peer-observation-driven adoption after an initial
    seeded rollout): this source's Claim 8 ("as teammates saw Devin in
    action, more asked to join... internal product market fit") is a third,
    independent instance of the same Slack-visibility-drives-viral-adoption
    pattern, in a new domain (data analytics) at a small-company scale.
  - `blog-cognition-devin-productivity-estimation.md` Claim 5 (the
    estimator's "account for codebase familiarity" design principle, credited
    as the mechanism behind Devin's advantage on unfamiliar/legacy
    codebases): this source's Claim 1 (Devin "understands our dbt repo") and
    Claim 4 (tracing a Looker dashboard back through unfamiliar query
    lineage to find a root cause) are a data-analytics-domain instance of
    the same underlying capability — rapid comprehension of an existing,
    not-freshly-authored system — that the productivity-estimation source
    documents as a measurement design principle for coding sessions
    specifically.

- **Contradicts**: None filed. One candidate tension was considered and
  rejected: this source's Claim 9 ("the future lies in between but towards
  exploration," i.e., lean away from heavy prescriptive curation) appears at
  first glance to sit in tension with `blog-anthropic-selfservice-data-analytics.md`
  Claim 6 (structured skills, not raw/unstructured access, are the decisive
  accuracy lever — implying invest *more* in curation, not less). This does
  not meet the MINER.md §4a filing bar: Eight Sleep explicitly concedes its
  own "vibe context" approach is "less accurate" in isolation and recommends
  layering "curated heuristics" on top (Concrete Artifacts → four named
  requirements, item 2) — it is not arguing against curation, only against
  *full, exhaustive* prescriptive curation ("you can only use this table"),
  which is a narrower target than what Anthropic's "knowledge skill" (a thin
  router to ~30 reference files, not an exhaustive whitelist) actually
  describes. Both sources agree pure unstructured exploration underperforms
  and that some curated layer is needed; Eight Sleep's account also carries
  no accuracy measurement at all, which is too weak an evidentiary basis to
  materially oppose Anthropic's quantified ablation. This reads as a
  difference of emphasis and unmeasured preference, not a same-claim
  conflict under matching conditions.

- **Extends**: `blog-anthropic-selfservice-data-analytics.md`, which
  documents a production-scale, quantitatively validated architecture for
  AI analytics agents from the vendor/model-provider side (Anthropic
  building for its own internal analysts). This source extends that
  coverage with an independent, customer-side account from a different
  vendor's product (Cognition's Devin) at a much smaller organizational
  scale, contributing a named worked incident example (Claim 4) and an
  explicit, if unmeasured, design-philosophy framework (Claim 9) that the
  more rigorous Anthropic source does not phrase in the same terms.

- **Novel**:
  - **"Vibe context" as a named, deliberate first-phase strategy** (Claim 2,
    Claim 9): No prior corpus source names giving an agent broad,
    uncurated tool/repo access as an explicit, intentional starting phase of
    context design (as opposed to an accident or anti-pattern to avoid).
  - **Social-friction-reduction adoption mechanism** (Claim 7): the specific
    hypothesis that people hesitate to interrupt a human colleague out of
    mere curiosity but feel no equivalent hesitation asking an AI is new to
    this corpus as a named adoption driver, distinct from the general
    "organic adoption via peer visibility" pattern already documented
    elsewhere (see Corroborates).
  - **A worked "is this number real" incident-investigation example**
    (Claim 4): this corpus's existing incident/triage coverage
    (`blog-cognition-auto-triage.md`) documents the general mechanism
    (monitor, investigate, route) but not a specific, named worked example
    of an agent resolving a live "is this data trustworthy" crisis; this
    source supplies one.
  - **The Approach A / Approach B naming convention** (Claim 9) is a new,
    reusable vocabulary for a design tension (prescriptive curation vs.
    exploratory access) that this corpus previously discussed only in terms
    of Anthropic's specific skills architecture.
  - **The companion "Build Your Own AI Data Analyst" setup guide** (Concrete
    Artifacts): the MCP Marketplace → credential configuration → Knowledge
    macro (`!analytics`) invocation pattern, and the specific example
    Knowledge-file content (model-tier preferences, schema-reading
    instructions, an explicit "always show the final query" output-format
    rule), is a concrete, reusable practitioner template not previously
    documented in this corpus at this level of implementation detail.

## Guide Impact

- **Chapter 04 (Context Engineering)**: Add the "vibe context" term and the
  Approach A / Approach B framework (Claim 9, Concrete Artifacts) as a named
  vocabulary for the curated-vs-exploratory context design tension, presented
  alongside `blog-anthropic-selfservice-data-analytics.md`'s measured finding
  that structure improves accuracy substantially. Flag explicitly that this
  source's "towards exploration" conclusion is an unmeasured customer
  preference, not a validated result, and that it does not actually reject
  Anthropic's core finding (see Cross-References → Contradicts).

- **Chapter 04 (Context Engineering)**: Add the companion setup guide's
  concrete artifacts (MCP Marketplace integration flow, the `!analytics`
  Knowledge-macro convention, and the example Knowledge-file content with its
  explicit model-tier preference rules and "always show the final query"
  output rule) as a reusable, implementation-level reference for teams
  building a similar Slack-invoked analytics agent — this is more concrete
  than any prior corpus source's analytics-agent setup material at the
  "here is an actual file" level.

- **Chapter 05 (Team Adoption)**: Add the organic/viral internal-adoption
  account (Claim 8) as a third corroborating instance (alongside
  `blog-anthropic-sires-gtm-claude-code.md` and
  `blog-cursor-paypal-enterprise-adoption.md`) of Slack-visibility-driven
  adoption, and add Claim 7's social-friction-reduction hypothesis as a named,
  testable mechanism for *why* peer-visible agent usage spreads — distinct
  from simply observing that it does.

- **Chapter 05 (Team Adoption) / Use Cases**: Add the worked incident example
  (Claim 4) as concrete illustrative material for a data-analytics use-case
  discussion, and the "queue near zero" / "3x" impact claims (Claims 5-6) as
  anecdotal-tier evidence to be clearly distinguished in the guide from the
  production-scale, statistically validated figures already sourced from
  `blog-anthropic-selfservice-data-analytics.md` and
  `blog-cognition-devin-productivity-estimation.md` — do not present these
  three sources' numbers as comparable in rigor.

- **Chapter 06 (Security / Threat Model)**: Add Claim 10 ("treat Devin's
  permissions like a human teammate's... restricted where compliance and
  privacy demand it") as a second, independent vendor-customer articulation
  of access-boundary design for analytics agents touching sensitive data,
  cross-referenced against the more mechanism-specific treatment in
  `blog-cognition-auto-triage.md` Claim 8 — flag that this source names the
  principle with zero implementation detail, unlike the auto-triage source.

## Extraction Notes

- cognition.com is a JavaScript-rendered (Next.js) site; consistent with the
  verbatim-extraction difficulty already documented in other Cognition source
  notes in this corpus (e.g. `blog-cognition-devin-in-windsurf.md`,
  `blog-cognition-devin-productivity-estimation.md` Extraction Notes), the
  raw HTML was fetched directly via `curl` with a browser user-agent rather
  than relying on WebFetch's summarizing pass. The HTML was stripped of
  script/style tags and markup with a Python script, and every quote used
  above was located and confirmed character-for-character in that stripped
  text before being copied into this note (per MINER.md §2a). Most
  apostrophes and quotation marks in the article body are literal Unicode
  curly-quote characters (’, “, ”) embedded directly in the HTML, not
  entities; the one exception is the sub-headline pull-quote near the top of
  the article ("Can you pull yesterday's sales..."), which is encoded in the
  raw HTML as `&quot;`/`&#x27;` (straight quotes) — confirmed by inspecting
  the raw markup directly, not assumed.
- Two linked pages were followed per MINER.md §1 (up to 5 permitted): Part 1
  and Part 2 of Cognition's own "Build Your Own AI Data Analyst" guide
  (`devin.ai/ai-data-analyst-1`, `devin.ai/ai-data-analyst-2`), reached via
  the Eight Sleep article's "Check out their guide here" link (which points
  to Part 2's Metabase MCP section). Both are first-party Cognition posts
  describing Cognition's *own* internal dogfooding of the same Devin-as-
  analyst pattern — a separate case from Eight Sleep's, not an extension of
  Eight Sleep's specific account — and are cited only in Concrete Artifacts
  and Cross-References, not as a source of numbered Claims, since the
  assigned source for this note (per issue #2105) is the Eight Sleep article
  specifically.
  No other outbound links on the primary article (the "articles" footer
  list, nav/legal links) were substantive enough to warrant following.
- The author, Andrew Foong, is the customer, not a Cognition employee —
  unlike `blog-cognition-auto-triage.md` (Cognition-authored, with one
  embedded customer quote from Modal) or `blog-cognition-devin-in-windsurf.md`
  (fully Cognition-authored, no customer voice at all), this entire post is
  customer-authored and hosted on the vendor's blog. Confidence is set to
  `emerging` rather than `anecdotal` because the account is more detailed,
  named, and specific (a named individual with a named title, a specific
  worked incident, a two-month timeline with three named forward
  investments) than a single embedded quote, but it is not rated `settled`
  or backed by any independent measurement — every quantitative claim (3x,
  near-zero, couple of hours, two months) is self-reported with no
  denominator, baseline, or methodology disclosed.
- Cross-references verified before writing: re-read
  `blog-anthropic-selfservice-data-analytics.md` in full and confirmed
  Claims 1, 6, 7, 14, and 15 by number and content; re-read
  `blog-anthropic-sires-gtm-claude-code.md` in full and confirmed the
  Individual-to-Org Adoption Arc artifact by name and content; re-read
  `blog-cursor-paypal-enterprise-adoption.md` in full and confirmed Claim 1
  by number and content; re-read `blog-cognition-devin-productivity-estimation.md`
  in full and confirmed Claim 5 by number and content; re-read
  `blog-cognition-auto-triage.md` in full and confirmed Claim 8 by number
  and content. No claim number was guessed or approximated.
- A candidate contradiction against
  `blog-anthropic-selfservice-data-analytics.md` Claim 6 was considered and
  rejected — see Cross-References → Contradicts for the full reasoning. No
  contradiction issue filed.
