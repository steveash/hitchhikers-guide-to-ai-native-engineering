---
source_url: https://cursor.com/blog/grab
source_type: blog-post
title: "How Grab put Cursor in the hands of Design, Ops, and Engineering"
author: "Cursor Team (vendor case study; named practitioners from Grab: Arun Makkath — Head of Tech Strategic Initiatives; Clement Gougeon — Head of Design Tech; Michelle Ng — Senior Manager, CEO's Office; Akshay Misra — Engineering Manager II)"
date_published: 2026-09-15
date_extracted: 2026-09-17
last_checked: 2026-09-17
status: current
confidence_overall: emerging
issue: "#3503"
---

# How Grab Put Cursor in the Hands of Design, Ops, and Engineering

> A vendor case study analyzing 100,000+ sanitized Cursor messages across ~4,000 people at Grab (Southeast Asian ride-hailing/delivery/payments platform), quantifying role-specific usage patterns across Design, Analytics, Technical Program Management, and the CEO's Office, and documenting bug fixing as a universal cross-role entry point (39% of activity in engineering and ops-and-business roles) at the highest reported adoption saturation (~98% monthly, ~75% weekly) in the corpus.

## Source Context

- **Type**: blog-post (vendor case study published on Cursor's commercial blog, September 15, 2026; ~750 words across five named sections with attributed quotes from four named Grab practitioners)
- **Author credibility**: Four named Grab practitioners provide direct quotes: Arun Makkath (Head of Tech Strategic Initiatives), Clement Gougeon (Head of Design Tech), Michelle Ng (Senior Manager, CEO's Office), and Akshay Misra (Engineering Manager II). Grab is a large publicly traded Southeast Asian technology company serving "millions of people across 8 countries" through rides, deliveries, and payments. The underlying data claim — analysis of "more than 100,000 sanitized Cursor messages across roughly 4,000 people" — is specific and gives the role-specific percentages more evidentiary weight than a typical anecdote-only vendor post. Published on Cursor's commercial blog — vendor-sourced marketing, with an inherent incentive to present adoption favorably. No discussion of failure modes, teams where adoption stalled, or the criteria used to select which 4,000 people's messages were sanitized/analyzed.
- **Scope**: Covers aggregate usage-pattern analysis by professional role (software engineering, ops-and-business, design, analytics, technical program management, product management, and non-engineering functions including the CEO's Office, finance, and regional teams), a cross-country training program, and Grab's stated "enablement, not mandate" adoption philosophy. Does NOT cover: the specific methodology used to classify the 100,000+ messages into activity categories, per-team financial or velocity outcomes (e.g., no deployment-frequency or cycle-time metric is given, unlike `blog-cursor-paypal-enterprise-adoption.md` or `blog-cursor-coinbase-agent-first-adoption.md`), how designers' Git training was structured, or any account of adoption resistance or roles where usage did not take hold.

## Extracted Claims

### Claim 1: About 98% of employees in Grab's tech organization use Cursor monthly and about 75% use it weekly — the highest reported enterprise adoption saturation in the corpus

- **Evidence**: Headline statistic stated directly in the article's opening paragraph, reinforced by a stat-card callout ("~98%" / "Monthly active Cursor usage in Grab's tech org").
- **Confidence**: emerging (self-reported organizational usage statistic; no definition given for what counts as "active use" — e.g., one message vs. sustained daily work)
- **Quote**: "Grab serves millions of people across 8 countries in Southeast Asia through rides, deliveries, payments, and the systems behind them. About 98% of employees in Grab's tech organization use Cursor monthly, and about 75% use it weekly."
- **Our assessment**: This is the highest monthly/weekly saturation figure reported for a large enterprise anywhere in the corpus (compare PayPal's 90%+ adoption threshold specifically among "high-impact teams" in `blog-cursor-paypal-enterprise-adoption.md` Claim 1, which is a subset, not an org-wide figure). The claim is scoped to "Grab's tech organization," not the whole company — the cross-functional reach described later in the article (Design, Finance, Ops, Marketing) is a claim about which functions participate within or adjacent to that tech org, not that 98% of all Grab employees company-wide use the tool. This distinction matters for how the guide cites the figure.

### Claim 2: Bug fixing ranked in the top three activities across every professional group studied, accounting for about 39% of activity in both software engineering and ops-and-business roles

- **Evidence**: Stated as a finding from the 100,000+-message analysis, with an explanation for why bug fixing is a natural universal entry point (concrete starting artifact: an error, failed test, broken query, or visibly wrong UI).
- **Confidence**: emerging (quantified finding from a large sanitized-message sample; methodology for activity classification not disclosed)
- **Quote**: "When Grab looked at more than 100,000 sanitized Cursor messages across roughly 4,000 people, bug fixing ranked in the top three activities in every professional group it studied. It accounted for about 39% of activity in both software engineering and ops-and-business roles. That tracks with how debugging works: it starts with something concrete, like an error, a failed test, a broken query, or a UI that looks wrong, so both the person and Cursor have a place to begin and a way to check the result."
- **Our assessment**: This is the most novel and specific finding in the source: bug fixing is not just an engineering-heavy task, it is the single largest or near-largest activity share across professional groups with very different day-to-day work (software engineers and "ops-and-business" roles both land at ~39%). The stated mechanism — a concrete starting artifact with a checkable end-state — is a generalizable explanation for which task types transfer most easily to non-specialist users of coding agents, independent of the user's job title. This is a candidate universal on-ramp pattern for cross-functional rollout: start non-engineers on bug-fix-shaped tasks specifically because they are self-verifying.

### Claim 3: Designers used Cursor 5.3x more than the company baseline for styling and layout work, and after Git-fundamentals training have merged hundreds of production UI fixes, each reviewed by design managers, often same-day

- **Evidence**: Quantified usage-ratio finding plus a described workflow and review gate (design-manager review before merge).
- **Confidence**: emerging (quantified ratio from the message-sample analysis; the "hundreds" of merged fixes is an approximate count, not exact)
- **Quote**: "For Design, that starting point turned into production work. Designers used Cursor 5.3x more than the company baseline for styling and layout. After training on Git fundamentals, designers have merged hundreds of UI fixes, each reviewed by design managers, often the same day."
- **Our assessment**: The review-gate detail ("each reviewed by design managers") is important: this is not designers bypassing engineering review, it is a parallel review lane where designers self-serve implementation but a human (a design manager, not necessarily an engineer) still gates the merge. This differs structurally from `blog-anthropic-claude-design-product-designer-workflow.md` Claim 5, where Claude Design is explicitly scoped to pre-commitment ideation and is not intended for production software at all ("Claude Design is for the other parts of the design work: early ideation, collaboration, or getting buy-in on a direction before anyone commits to building it"). Grab's designers, by contrast, use a general-purpose coding agent (Cursor) plus baseline Git skills to ship and merge real production fixes. These are not contradictory claims — they describe two different tools with two different intended scopes — but they represent two distinct design-tool philosophies worth contrasting in the guide: (a) a dedicated ideation-only surface with round-trip handoff to an engineer-owned coding tool, versus (b) designers using the same general-purpose coding agent as engineers, gated by review rather than by tool capability.

### Claim 4: A designer's account of the underlying behavior change — going directly from noticing a UI defect to producing a working implementation, rather than filing a ticket

- **Evidence**: Named first-person quote from Clement Gougeon, Head of Design Tech.
- **Confidence**: anecdotal (single named practitioner's account of his own workflow change)
- **Quote**: "I understood the potential when a UI did not look or behave as intended. Instead of raising a bug or handing over a design file, I used Cursor to follow it into the implementation and produce a working change that Engineering could validate. That was when I saw how Design could take more direct ownership of product quality."
- **Our assessment**: The phrase "that Engineering could validate" is the key qualifier — Gougeon frames this as producing a change for engineering validation, not as bypassing engineering entirely. This is consistent with Claim 3's "reviewed by design managers" detail but adds a second, engineering-facing validation step implied by "could validate," suggesting the review chain may involve both a design manager and engineering depending on the change. The source does not disambiguate whether both reviews always occur or whether "could validate" describes an available-but-optional escalation path.

### Claim 5: Among software engineers, power users sent 18x as many messages as light users, and power users' share of high-complexity work was 15.6% higher than light users'

- **Evidence**: Quantified comparison between engineering power users and light users from the message-volume analysis.
- **Confidence**: emerging (quantified usage-distribution finding; "power user" and "light user" thresholds are not defined in the source)
- **Quote**: "Among software engineers, power users sent 18x as many messages as light users, and their share of high-complexity work was 15.6% higher. The jobs themselves were familiar ones, like tests, refactors, bug fixes, and navigating unfamiliar code."
- **Our assessment**: The 18x message-volume gap between power and light users is a specific, large power-law usage distribution — the source does not say what fraction of engineers fall into each bucket, so this cannot be read as "engineers as a whole are 18x more productive." The explicit note that "the jobs themselves were familiar ones" (not novel task types) indicates the power-user advantage is about depth/frequency of use on already-familiar work categories, not about power users doing categorically different things than light users.

### Claim 6: Tasks that once took days now take a few hours; engineers now take on refactors and tests they would previously have skipped under time pressure; over a third of merge requests incorporate Cursor; suggestion acceptance sits around 50%

- **Evidence**: Cluster of headline metrics presented together as the engineering-outcome summary, including a stat-card callout ("Days to hours" / "Tasks that used to take days now finish in a few hours").
- **Confidence**: emerging (aggregate self-reported metrics; "over a third of merge requests incorporate Cursor" and "~50% suggestion acceptance" are given without a measurement window or definition of "incorporate")
- **Quote**: "The difference showed up in what got finished. Grab has said publicly that tasks that once took days now take a few hours, and that engineers now take on refactors and tests they would have skipped under time pressure. Over a third of merge requests incorporate Cursor, and suggestion acceptance sits around 50%."
- **Our assessment**: "Tasks they would have skipped under time pressure" is a distinct claim from pure speedup — it says the tool changed which work gets done, not only how fast existing work gets done (previously-deprioritized refactors and tests are now completed). The days-to-hours compression is directionally consistent with but far less precisely quantified than Coinbase's 20-days-to-1.8-days idea-to-production metric (`blog-cursor-coinbase-agent-first-adoption.md` Claim 9) — Grab gives a qualitative bucket ("days" to "hours"), not a specific before/after number.

### Claim 7: Writing code was roughly half of Cursor activity in every professional group studied, with the "second job" differing by role: analytics leaned toward SQL/transforms (4.7x baseline), technical program management toward Git/build/deploy (3.1x baseline), and product management toward documentation, including turning PRDs into working HTML/JS/CSS demos

- **Evidence**: Cross-role breakdown of the "second most common activity" after code-writing, with named usage-ratio figures for two of the three named non-engineering-adjacent roles and a specific anecdote for product management.
- **Confidence**: emerging (quantified ratios for analytics and TPM; the PM claim is anecdotal — "at least one PM" — rather than a role-wide ratio)
- **Quote**: "Writing code was roughly half of Cursor activity in every group. The second job changed by role: analytics leaned toward SQL and transforms (4.7x the company baseline), technical program management clustered on Git, build, and deploy (3.1x), and product managers used Cursor more for documentation. At least one PM turned PRDs into working HTML, JavaScript, and CSS demos."
- **Our assessment**: This is the most granular role-by-role activity breakdown in the Cursor corpus to date — three named non-engineering-adjacent roles (analytics, TPM, PM) each with a distinct dominant secondary activity, and two of the three with a specific baseline-multiple. The "at least one PM" phrasing is a meaningful hedge: unlike the analytics and TPM figures (stated as role-wide ratios), the PRD-to-working-demo capability is presented as an example, not a role-wide statistic, and should not be generalized to "PMs at Grab typically build working demos."

### Claim 8: Non-engineers in finance, operations, and regional teams are building tools for their own problems without sitting in an engineering queue, illustrated by a CEO's-office team member turning ideas directly into working tools

- **Evidence**: Named first-person quote from Michelle Ng, Senior Manager in the CEO's Office, plus a general framing statement about finance/ops/regional teams.
- **Confidence**: anecdotal (single named practitioner's account, generalized to "finance, operations, and regional teams" without per-team metrics)
- **Quote**: "Cursor has been transformative for me in the CEO's Office. As someone who isn't a traditional technologist, I can now turn ideas into working tools, improve processes, and solve workflow challenges directly. It has changed not only my own productivity, but also what our team is capable of achieving."
- **Our assessment**: Ng's framing — "changed not only my own productivity, but also what our team is capable of achieving" — attributes a team-level capability expansion to one non-technologist's tool use, not merely personal time savings. This directly corroborates the "work moves without sitting in an engineering queue" framing given in the surrounding article text, and is analogous in kind (though from a different tool, Claude Cowork, at a different company) to `blog-anthropic-cowork-marketing-ops.md` Claim 2's description of Anthropic marketing-ops staff redirecting recovered time toward enabling other people's self-service use of AI, rather than only personal output.

### Claim 9: Grab ran workshops that trained several hundred people across 5 countries, including senior leaders who personally built and deployed their own applications

- **Evidence**: Stated directly as part of the non-engineering adoption description.
- **Confidence**: emerging (specific headcount-range and country-count claim; no breakdown of workshop content, duration, or per-country participation)
- **Quote**: "In each of these roles, work moves without sitting in an engineering queue. Non-engineers in finance, operations, and regional teams are building tools for their own problems, and Grab's workshops have trained several hundred people across 5 countries, including senior leaders who built and deployed their own apps."
- **Our assessment**: "Senior leaders who built and deployed their own apps" (not merely attended training) is the notable detail — leadership participation as hands-on builders, not just program sponsors, is a specific and relatively rare claim in the corpus. This is a training-program scale data point (hundreds of people, 5 countries) comparable in kind to NAB's "intentional enablement" sprint-day training (`blog-cursor-nab-legacy-migration.md` Claim 4), though NAB's training was scoped to developers on real production projects, while Grab's explicitly targeted non-engineers and leadership across multiple countries.

### Claim 10: Grab treated cross-functional AI adoption as enablement, not a mandate — people started on a real problem they cared about, then took on the next piece of relevant work, rather than being directed top-down

- **Evidence**: Explicit framing statement contrasting "enablement" with "mandate," followed by a description of the organic mechanism (start on a real problem, then take the next piece of work).
- **Confidence**: anecdotal (organizational-philosophy framing, not a measured comparison against a mandate-based control group)
- **Quote**: "Grab treated that as enablement, not a mandate. Someone would start on a real problem they cared about, then take on the next piece of work that mattered in their day: a query for an analyst, a workflow for ops, a demo for a PM."
- **Our assessment**: This is the explicit articulation of an "enable, don't mandate" adoption philosophy, stated in almost identical framing to `blog-anthropic-cowork-marketing-ops.md` Claim 2's self-service framing and structurally similar to PayPal's organic-spread rollout strategy (`blog-cursor-paypal-enterprise-adoption.md` Claim 1: high-impact teams seeded first, then organic peer-driven spread) — though Grab's version is framed around individual non-engineers pursuing self-relevant problems rather than PayPal's team-level seeding strategy. It also stands in implicit tension with the corpus's existing "top-down mandate replacing engineering judgment" concern noted as a legitimate pushback risk in the guide's own team-adoption chapter (`guide/05-team-adoption.md`, discussing objections to top-down AI mandates) — Grab's case is offered as a positive example of avoiding exactly that failure mode.

### Claim 11: In roles where fewer people had adopted Cursor, the people who did adopt it often used it more heavily than engineers or the company overall — adoption depth compensates for adoption breadth in low-uptake roles

- **Evidence**: Stated as an observed pattern from the usage-distribution analysis, without a specific ratio.
- **Confidence**: anecdotal (qualitative pattern description, no quantified comparison given)
- **Quote**: "In roles where fewer people had opened Cursor, the people who did often used it more heavily than engineers and the company overall. Once someone found a real job for the tool, they stuck with it."
- **Our assessment**: "Once someone found a real job for the tool, they stuck with it" is a retention/stickiness claim distinct from the adoption-breadth claims elsewhere in the article (98% monthly, 75% weekly). It suggests usage in low-adoption roles is bimodal — most people in a given low-uptake role may not use Cursor at all, but those who find a genuine use case become heavy, persistent users — rather than a uniform light-usage distribution across the role. No quantification is given for what fraction of any given role falls into the "found a real job for it" category.

### Claim 12: Grab's stated organizational philosophy is that AI is for everyone, and Design, Finance, Ops, and Marketing are now building and shipping on top of the Tech organization, with existing employees framed as the source of that capability rather than new hires or specialists

- **Evidence**: Named closing quote from Akshay Misra, Engineering Manager II, and a companion quote from Arun Makkath, Head of Tech Strategic Initiatives, framing the overall narrative.
- **Confidence**: anecdotal (executive/manager framing statements, not measurements)
- **Quote**: "At Grab, we believe AI is for everyone, so we focused on upskilling everyone. Today Design, Finance, Ops, Marketing are all building and shipping on top of Tech. The builders were always here — we just handed them the keys." — Akshay Misra, Engineering Manager II
- **Quote**: "In the early days, when we were still figuring out how to turn this new wave of AI into real changes in the way we work, Cursor was one of the tools that helped it click. It found its own product-market fit inside Grab without much of a push, pulling in non-tech teams and executives alongside Tech. Beyond adoption, it began to shift how people thought about their workflows and ways of working which was an important part of opening up our AI journey." — Arun Makkath, Head of Tech Strategic Initiatives
- **Our assessment**: Makkath's "found its own product-market fit inside Grab without much of a push" is functionally the same organic-adoption claim as PayPal's peer-driven spread (`blog-cursor-paypal-enterprise-adoption.md` Claim 1) and Coinbase's internal-champion mechanism (`blog-cursor-coinbase-agent-first-adoption.md` Claim 6), but applied here to cross-functional (non-engineering) spread specifically, rather than engineering-team spread. Misra's "the builders were always here — we just handed them the keys" is the most quotable single-line articulation in the corpus of the thesis that non-engineers' capability was latent and tool-gated, not something that had to be created from scratch through hiring or specialist training.

## Concrete Artifacts

### Headline Metrics (stat-card callouts and body text)

```
Grab x Cursor — Key Metrics (Cursor blog, published 2026-09-15)
Source: https://cursor.com/blog/grab

ORGANIZATIONAL SCALE
  Grab tech org monthly active Cursor usage:  ~98%
  Grab tech org weekly active Cursor usage:   ~75%
  Messages analyzed:                          100,000+ sanitized Cursor messages
  People covered by analysis:                 ~4,000

CROSS-ROLE FINDING
  Bug fixing — top-3 activity in every professional group studied
  Bug fixing share of activity (software engineering):  ~39%
  Bug fixing share of activity (ops-and-business):       ~39%
  Code-writing share of activity: "roughly half" in every group studied

ROLE-SPECIFIC USAGE RATIOS (vs. company baseline)
  Design — styling/layout:                5.3x baseline
  Analytics — SQL/transforms:             4.7x baseline
  Technical Program Management — Git/build/deploy: 3.1x baseline

ENGINEERING OUTCOMES
  Task duration:            "days" -> "a few hours"
  Power-user vs light-user message volume (engineers): 18x
  Power-user high-complexity work share vs light users: +15.6 percentage points
  Merge requests incorporating Cursor:  "over a third"
  Suggestion acceptance rate:           ~50%

DESIGN-SPECIFIC OUTCOME
  Production UI fixes merged by designers: "hundreds," often same-day,
  each reviewed by a design manager, after Git-fundamentals training

TRAINING PROGRAM
  People trained in workshops:  "several hundred"
  Countries covered:            5
  Included:                     senior leaders who built/deployed own apps
```

### Named Quote Collection

```
Arun Makkath, Head of Tech Strategic Initiatives — Grab:
  "In the early days, when we were still figuring out how to turn this new
  wave of AI into real changes in the way we work, Cursor was one of the
  tools that helped it click. It found its own product-market fit inside
  Grab without much of a push, pulling in non-tech teams and executives
  alongside Tech."

Clement Gougeon, Head of Design Tech — Grab:
  "I understood the potential when a UI did not look or behave as intended.
  Instead of raising a bug or handing over a design file, I used Cursor to
  follow it into the implementation and produce a working change that
  Engineering could validate. That was when I saw how Design could take
  more direct ownership of product quality."

Michelle Ng, Senior Manager, CEO's Office — Grab:
  "Cursor has been transformative for me in the CEO's Office. As someone
  who isn't a traditional technologist, I can now turn ideas into working
  tools, improve processes, and solve workflow challenges directly."

Akshay Misra, Engineering Manager II — Grab:
  "At Grab, we believe AI is for everyone, so we focused on upskilling
  everyone. Today Design, Finance, Ops, Marketing are all building and
  shipping on top of Tech. The builders were always here — we just handed
  them the keys."
```

### Section Structure (from article)

```
How Grab put Cursor in the hands of Design, Ops, and Engineering
(Cursor blog, 2026-09-15) — section headings, in order:

1. Designers ship the fix instead of filing a ticket
2. Engineers take on work they used to skip
3. People outside engineering stop waiting in the queue
4. The builders were already there
```

## Cross-References

- **Corroborates**:
  - `blog-cursor-paypal-enterprise-adoption.md` Claim 1 (organic adoption: high-impact teams seeded first, then peer-driven spread; no top-down mandate) — Grab's Makkath quote ("found its own product-market fit inside Grab without much of a push") and Claim 10 above (enablement, not mandate) describe the same organic-spread mechanism, now documented for cross-functional (non-engineering) adoption rather than PayPal's team-to-team engineering spread.
  - `blog-cursor-coinbase-agent-first-adoption.md` Claim 6 (change management via modeling and internal champions rather than top-down mandate; "You can't tell people to use AI and expect meaningful change. You have to show them what is possible.") — Grab's "enablement, not a mandate" framing (Claim 10) is a third independently named enterprise case rejecting mandate-driven rollout in favor of organic, self-selected adoption.
  - `blog-cursor-nab-legacy-migration.md` Claim 4 (intentional enablement via structured training on real production work) — Grab's cross-country workshop program (Claim 9: several hundred people, 5 countries, including senior leaders who built and deployed their own apps) is a structured-training case, extending NAB's engineer-focused training model to a non-engineering, multi-country population.
  - `blog-anthropic-cowork-marketing-ops.md` Claim 2 (recovered time redirected toward enabling other people's self-service use of AI, "as more people across the company pull their own numbers and drive their own programs") — Grab's Michelle Ng quote (Claim 8) and the "non-engineers... building tools for their own problems" framing describe the same self-service-enablement pattern, corroborated across two different companies and two different AI tools (Cursor vs. Claude Cowork).

- **Contradicts**: None filed. The closest apparent tension is with `blog-anthropic-claude-design-product-designer-workflow.md` Claim 5 (Claude Design is explicitly scoped to pre-commitment ideation, not production software), since Grab's designers do ship reviewed production code via Cursor (Claim 3, Claim 4 above). This is not a contradiction under the MINER.md §4a bar: the two sources describe different tools with different declared scopes (a dedicated ideation-only surface vs. a general-purpose coding agent used by designers under a human review gate), not two sources disagreeing about the same claim. Captured under Claim 3's assessment as a conditioning-variable contrast, not filed as a contradiction issue.

- **Extends**:
  - `blog-cursor-paypal-enterprise-adoption.md` Claim 7 (role boundaries between PMs and engineers blurring productively) — Grab's finding that "at least one PM turned PRDs into working HTML, JavaScript, and CSS demos" (Claim 7 above) is a concrete instance of the same PM-builds-a-prototype pattern PayPal described qualitatively, now with a specific artifact type (working HTML/JS/CSS) named.
  - `blog-cursor-nab-legacy-migration.md` Claim 4 (structured training on real production work as an enablement strategy) — Grab extends this from an engineering-only training population to a specifically cross-functional and cross-country one (several hundred people, 5 countries, including senior leaders as hands-on builders rather than only sponsors).

- **Novel**:
  - **Quantified role-by-role usage-ratio breakdown across four distinct non-engineering-adjacent roles** (Design 5.3x, Analytics 4.7x, TPM 3.1x, plus a PM example): no prior corpus source gives per-role baseline-multiple usage ratios at this granularity across this many distinct roles within one organization.
  - **Bug fixing as a quantified universal cross-role entry point** (39% of activity in both software engineering and ops-and-business roles, top-3 in every group studied): no prior corpus source names a single task category as the dominant or near-dominant activity share across multiple, structurally different professional roles, nor offers the "concrete starting point, checkable result" explanation for why debugging transfers across roles.
  - **Highest reported enterprise-wide adoption saturation figure in the corpus** (~98% monthly / ~75% weekly for Grab's tech organization): exceeds PayPal's 90%+ figure, which was scoped to "high-impact teams" rather than an org-wide population.
  - **Designer-shipped production code under a design-manager (not engineering) review gate**: no prior corpus source documents designers merging production code fixes reviewed by design managers specifically, as distinct from engineering review.
  - **Multi-country (5-country), cross-functional training program with senior leaders as hands-on builders**: no prior corpus source documents leadership training that resulted in leaders personally building and deploying their own applications, at this geographic scale.

## Guide Impact

- **Chapter 05 (Team Adoption) — cross-functional rollout patterns**: The guide currently discusses domain-expert unblocking (Layer 5 framework around line 1186 of `guide/05-team-adoption.md`) and warns that "any team-adoption playbook that mandates a single tool is fighting the median practitioner reality" (line 60-61). Add Grab's four quantified role-specific usage ratios (Design 5.3x, Analytics 4.7x, TPM 3.1x) as the first corpus-level quantified evidence base for that Layer 5 framework's question "how long does it take a non-engineer SME to ship a rule change?" — Grab gives concrete role-by-role multipliers rather than a single generic "non-engineers can use AI too" claim.

- **Chapter 05 (Team Adoption) — enablement vs. mandate**: The guide already flags "top-down mandate replacing engineering judgment" as a legitimate adoption objection (Objection 5, per line 1390-1392). Add Grab's explicit "enablement, not a mandate" framing (Claim 10) plus its "once someone found a real job for the tool, they stuck with it" observation (Claim 11) as a third named enterprise case — alongside PayPal's organic spread and Coinbase's champion-modeling — showing organic, self-selected adoption succeeding at very high saturation (98%/75%) without a mandate. This strengthens the guide's existing recommendation against mandate-driven rollout with the highest-saturation data point in the corpus.

- **Chapter 05 (Team Adoption) — universal on-ramp task selection**: Add Claim 2 (bug fixing as a ~39% cross-role activity share, explained by "a concrete starting point and a way to check the result") as a specific, actionable recommendation for choosing which task type to use as the entry point when rolling out AI tools to non-engineering roles: prefer self-verifying, concretely-scoped tasks (an error, a failed test, a wrong-looking UI) over open-ended or judgment-heavy tasks for first exposure.

- **Chapter 01 (Daily Workflows) — role-specific secondary activities**: Add the "second job by role" breakdown (Claim 7: analytics → SQL/transforms, TPM → Git/build/deploy, PM → documentation and working demos from PRDs) as a concrete illustration of how the same tool produces different day-to-day workflows depending on role, useful for a section describing what AI-native daily work looks like outside of core software engineering.

## Extraction Notes

- Full article text was recovered from the page's embedded React Server Components (RSC) flight-data payload in the raw HTML (fetched via `curl`), not from a summarizing WebFetch pass, because an initial WebFetch call returned only a condensed paraphrase. All quotes above were copied verbatim from the escaped JSON string literals in that payload (pattern `\"children\":\"...\"`), which reproduce the rendered page's exact text, including named speaker attributions found in adjacent `<div>` elements. This is the same verification method noted as a best practice in `blog-anthropic-cowork-marketing-ops.md`'s Extraction Notes (raw-HTML extraction catching passages a summarizing pass dropped or shortened).
- Speaker attributions (Arun Makkath, Clement Gougeon, Michelle Ng, Akshay Misra) and their titles were independently confirmed from `<div class="type-sm text-theme-text-sec">` caption elements immediately following each quoted `<p>` block in the raw HTML, not inferred from quote content or the WebFetch summary alone.
- The article is short (~750 words) and consists of an intro, one framing quote card, four named sections (Design; Engineering; non-engineering/CEO's Office; "the builders were already there"), and a closing quote. All four section quotes, both stat-card callout sets, and the closing quote were extracted; nothing substantive was left unexamined. No sub-pages were linked from the article body (only a site-wide "More customer stories" carousel, not inline content).
- The article does not disclose: (1) the message-classification methodology used to compute activity-share percentages, (2) what "power user" and "light user" thresholds mean quantitatively (Claim 5), (3) any team or role where adoption did not take hold, or (4) a specific pre/post velocity metric comparable to Coinbase's 20-days-to-1.8-days figure — the "days to hours" claim (Claim 6) is qualitative. These gaps are noted in each relevant claim's confidence rating rather than treated as settled figures.
- No contradiction issue filed. The Claude Design scope-boundary tension (Claim 3's assessment) was evaluated against the MINER.md §4a bar and judged to be a conditioning-variable/different-tool distinction, not a material disagreement about the same claim — both sources agree engineers should validate/review before production, they differ only in which tool and review path designers use to get there.
- Confidence set to `emerging` overall: this is a vendor case study with a specific, sizable underlying dataset claim (100,000+ messages, ~4,000 people) and four named practitioners, which is stronger evidentiary grounding than a single-anecdote vendor post, but all figures are self-reported by Cursor/Grab with no independent verification, no disclosed methodology for the activity-classification percentages, and an inherent commercial incentive to present adoption favorably.
