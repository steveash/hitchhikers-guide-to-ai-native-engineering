---
source_url: https://cursor.com/blog/imdex
source_type: blog-post
title: "IMDEX uses Cursor to build integrated subsurface data and analytics platform in months, not years"
author: "Cursor Team (vendor case study; named practitioners: Rob van Selm, Nathan Davey, Richard Zampieri — all IMDEX)"
date_published: 2026-08-25
date_extracted: 2026-08-26
last_checked: 2026-08-26
status: current
confidence_overall: emerging
issue: "#2964"
---

# IMDEX Uses Cursor to Build Integrated Subsurface Data and Analytics Platform in Months, Not Years

> A named-practitioner enterprise case study of a mining-technology company (IMDEX) consolidating fragmented geological data systems and migrating a legacy Angular application to React with Cursor, reporting an 8-month data-platform build (vs. an estimated 20 additional engineers / 2-3 years / millions of dollars without it) and a 6-month Angular-to-React migration (vs. 3-5 years), alongside a named enterprise tool-evaluation rationale and a dedicated month-long "AI July" training program.

## Source Context

- **Type**: blog-post (vendor case study published on Cursor's commercial blog; ~1,000 words, "6 min read"; six named sections with attributed quotes from three named IMDEX practitioners). Discovered via the trusted `cursor-blog` RSS feed, entry dated Tue, 25 Aug 2026.
- **Author credibility**: Byline is "Cursor Team" (the vendor). Three named IMDEX practitioners are quoted: Rob van Selm (Head of Software Development, later described as "Head of Software Development and Solutions"), Nathan Davey (Principal Software Engineer), and Richard Zampieri (Principal Engineer/AI Lead). IMDEX is described in the article as a "Global mining technology leader" in Australia with a "comprehensive portfolio of 600+ mining technologies." This is the same case-study genre as `blog-cursor-nab-legacy-migration.md`: vendor blog, named practitioners, specific timelines and quantified before/after estimates, no independent (non-Cursor) verification of the metrics.
- **Scope**: Covers two named IMDEX engineering projects (a data-platform consolidation and an Angular-to-React migration), IMDEX's stated criteria for standardizing on Cursor after evaluating other tools, a company-wide "AI July" training program, and IMDEX's use of the Cursor Dashboard/Analytics API for adoption tracking. Does NOT cover: which competing tools were evaluated by name, the technical architecture of the consolidated data platform, implementation-level detail on the Angular-to-React migration, cost of the Cursor license itself, or any measurement of output quality/defect rates post-migration.

## Extracted Claims

### Claim 1: IMDEX's legacy-migration and data-consolidation work moved at 10x the pace of its pre-AI development model using Cursor
- **Evidence**: Headline framing stated directly in the article's summary and stat callout, without a stated calculation method (not derived transparently from the two project timelines given, which imply different individual multiples).
- **Confidence**: anecdotal (headline vendor framing; the underlying 8-month/6-month figures are the more specific and checkable claims — see Claims 2-3)
- **Quote**: "Global mining technology leader, IMDEX, is using Cursor to consolidate fragmented geological data systems and re-platform legacy applications at 10x the pace of its pre-AI development model."
- **Our assessment**: The "10x" figure is a rounded, aggregate headline number rather than a per-project measured multiple — the two named projects below imply timeline compressions of roughly 3-4.5x (8 months vs. 2-3 years) and 6-10x (6 months vs. 3-5 years), which don't obviously average to a single clean "10x." Treat this as marketing-headline framing layered on top of the two more specific claims, not as an independently verified figure.

### Claim 2: Data-platform consolidation of two flagship IMDEX products landed in 8 months with Cursor, versus an estimated 20 additional engineers, millions of dollars, and 2-3 years without it
- **Evidence**: Specific named engineer (Rob van Selm, Head of Software Development) providing the counterfactual estimate; repeated twice in the article (once in the intro, once in the "One IMDEX platform for fragmented mining data" section) with consistent figures.
- **Confidence**: emerging (specific, consistently repeated figures from a named practitioner; the counterfactual — what it "would have" taken — is inherently unverifiable and vendor-favorable)
- **Quote**: "Without Cursor, building these workflows might have taken 20 new people, millions of dollars, and two to three years. With Cursor, we're increasing the leverage of people we already have. That's a huge technical and financial win for the organization." — Rob van Selm, Head of Software Development, IMDEX
- **Our assessment**: This is structurally identical to `blog-cursor-nab-legacy-migration.md` Claim 5's pattern (BizCalc monolith: 1 week vs. 2-month estimate) — a named engineer providing a counterfactual estimate rather than a measured baseline from a prior, non-AI attempt at the same project. The word "might have taken" in the quote is a hedge the article's own headline stat box drops (it states the comparison as flat fact: "8 months / 6 months ... vs 2-5 years"). For the guide, this should be flagged as an estimated counterfactual, not a measured before/after.

### Claim 3: The Angular-to-React migration landed in 6 months with Cursor, versus a previously estimated 3-5 years
- **Evidence**: Stated in the article body and the stat callout box; no named engineer attribution for this specific figure (attributed to the project description generally).
- **Confidence**: emerging (specific figure, consistently repeated in two places in the article; no independent baseline given for how the 3-5 year estimate was derived)
- **Quote**: "The second product migrates a legacy Angular application to a React micro frontend to allow for easier maintenance and new feature development. This work previously would have taken three to five years, but with Cursor it landed in six months."
- **Our assessment**: A 6-to-10x compression on a UI framework migration is a larger multiple than the platform-consolidation claim (Claim 2, ~3-4.5x) despite framework migrations typically being more mechanical/pattern-following than data-platform consolidation. This is plausible if the "3-5 years" baseline assumed a full parallel-team rewrite rather than an incremental migration, but the source gives no detail on how that baseline was derived — same limitation as Claim 2.

### Claim 4: IMDEX evaluated coding tools from multiple providers before standardizing on Cursor, citing user experience as the deciding factor
- **Evidence**: Named quote from Richard Zampieri (Principal Engineer/AI Lead); no specific competing tools are named (contrast with `blog-cursor-nab-legacy-migration.md` Claim 1, which names Amazon Q and GitHub Copilot as the evaluated alternatives).
- **Confidence**: anecdotal (single practitioner's summary judgment; "user experience is so much better" is not decomposed into specific criteria in this quote — see Claim 5 for the three criteria the article separately enumerates)
- **Quote**: "We've tried tools from multiple providers, but we have always landed back on Cursor because the user experience is so much better." — Richard Zampieri, Principal Engineer/AI Lead, IMDEX
- **Our assessment**: Unlike NAB's evaluation (which names the specific competitors and three explicit selection criteria tied to concrete technical capabilities), IMDEX's stated rationale here is a qualitative "user experience" judgment without naming which tools were tried or losing on what dimension. This is weaker evidentiary value than the NAB evaluation for a guide section on tool-selection frameworks, though the three capabilities in Claim 5 sharpen it somewhat.

### Claim 5: IMDEX names three specific capabilities behind its Cursor adoption — context management on large codebases, per-task model flexibility, and a familiar workspace that preserves existing developer tooling access
- **Evidence**: Article presents these as three distinct bulleted capabilities under the heading "Developers kept landing back on Cursor," each with a short description.
- **Confidence**: emerging (specific, named capabilities rather than generic praise; still vendor-sourced and not independently benchmarked against the "other tools tested")
- **Quote**: "Context management on large codebases: Cursor's agent harness managed context more effectively than other tools the team tested, helping agents recall relevant parts of the codebase and develop better implementation strategies for ambiguous tasks."
- **Quote**: "Model flexibility: Developers can pick the model that fits the task. Some rely on Auto, which selects the model based on speed and cost. Others choose higher-thinking models for ambiguous design decisions and simpler models for contained implementation work."
- **Quote**: "A familiar workspace for AI-assisted development: Cursor gave IMDEX developers a practical way to bring AI into their existing development workflow. Engineers could use agents to plan, generate, refactor, and review code, while still working in a familiar environment with access to files, debugging tools, browser context, and design resources."
- **Our assessment**: The model-flexibility criterion directly corroborates `blog-cursor-nab-legacy-migration.md` Claim 2's task-based model routing pattern (cheap models for routine work, thinking models for ambiguous/architectural work) — this is now two independent named enterprises describing the same routing heuristic. The "familiar workspace" criterion is a distinct, less-covered claim in the corpus: the value isn't the agent alone, it's that developers don't have to abandon their existing IDE-native workflow (files, debugger, browser, design tools) to use it. For the guide, this argues against "agent-only" or context-switching-heavy tool designs in enterprise settings.

### Claim 6: IMDEX ran a dedicated month-long training program ("AI July") combining structured curriculum with applied hackathons to accelerate coding-agent adoption
- **Evidence**: Described as a company-wide initiative with a three-part curriculum (101-level basics, 201-level advanced tooling, hackathons).
- **Confidence**: emerging (specific curriculum structure named; no data given on the program's measured effect on adoption or output, only that it "combined structured learning with applied product work")
- **Quote**: "To accelerate adoption of coding agents, IMDEX dedicated a full month to hands-on Cursor training and experimentation. Internally referred to as 'AI July', this program combined structured learning with applied product work so developers could build agentic workflows into their day-to-day practice."
- **Quote**: "101-level trainings on agent basics like context windows, model selection, and token consumption" / "201-level sessions on advanced tools like MCPs, skills, hooks, and agent parallelization" / "Dedicated hackathons to try Cursor on real product problems"
- **Our assessment**: This corroborates `blog-cursor-nab-legacy-migration.md` Claim 4's enablement pattern (Andrew Vaughan's "sprint days where developers use Cursor on real production projects") but is a distinct, more structured implementation: a tiered curriculum (101 → 201 → hackathon) rather than ad hoc sprint days, and time-boxed to a single calendar month rather than an ongoing rollout phase. The 101/201 tiering by concept (context windows and model selection first, then MCPs/skills/hooks/parallelization) is a concrete curriculum sequence a guide could recommend as a template, which neither the NAB nor the better-models-ambitious-work notes provide.

### Claim 7: IMDEX uses the Cursor Dashboard and Analytics API to track adoption, usage patterns, and delivery metrics, and cites this visibility as justification for continued investment
- **Evidence**: Named quote from Richard Zampieri describing the dashboard's role; separately, the article states the team uses the same API to "track PR volume per developer, and measure output and delivery time more precisely."
- **Confidence**: anecdotal (single practitioner's characterization of the dashboard's value; no specific numbers from the dashboard are disclosed in the article)
- **Quote**: "The Cursor Dashboard and Analytics API provide easy insights into usage patterns across our team so we can understand adoption. Those insights make it easy to justify our investment." — Richard Zampieri, Principal Engineer/AI Lead, IMDEX
- **Our assessment**: This is a governance/measurement claim distinct from the productivity claims: IMDEX is using vendor-supplied usage analytics (not independent engineering metrics like cycle time or defect rate) as the basis for continued investment justification. For a guide section on measuring AI adoption, this is worth flagging as a limitation as much as a pattern — "PR volume per developer" is a volume metric, not an outcome or quality metric, and the source does not report what values IMDEX actually observed.

### Claim 8: Mining exploration drilling programs cost $300k-$2 million per day, which the article frames as the reason IMDEX's data-platform work must protect data fidelity and why the org is cautious about adopting new technology for critical operational decisions
- **Evidence**: Stated as domain context early in the article, framing the stakes of the data-consolidation work described in Claims 2 and 5.
- **Confidence**: emerging (a domain fact about drilling economics, not a claim about Cursor itself; presented without a cited source for the $300k-$2M figure)
- **Quote**: "Mining exploration drilling programs cost anywhere from $300k to $2 million per day, and efficiency gains from data to decision are measured in these terms. It also means companies are rightly cautious about adopting new technologies that affect critical operational decisions."
- **Our assessment**: This is the most distinctive domain-specific framing in the source and the main reason the Prospector rated this as covering a "new domain" (mining vs. NAB's banking or Amplitude's SaaS). The stakes described here — a driller platform providing "live guidance so they can compare real-time drilling data against the planned hole path and stay within the defined cone of tolerance," and a geologist-facing side that "protects the quality and reliability of the data they depend on to interpret the subsurface" — describe a safety/cost-critical operational context, which is a different adoption-risk profile than the software-engineering-only migrations in the NAB and Amplitude notes. No claim in the article, however, states that the AI-built platform has been used in a live drilling decision or measures any operational outcome from it; the claim is about IMDEX's stated caution, not about validated safety in production use.

### Claim 9: After the two flagship engineering projects, IMDEX used Cursor to build a customer insight app in under 30 days and a sales training tool in under two weeks — projects the article says previously required outside vendors or quarters of internal work
- **Evidence**: Named examples with specific timelines, described as part of extending Cursor's use "beyond engineering."
- **Confidence**: anecdotal (two brief examples, no named engineer attribution, no detail on team size or scope of either tool)
- **Quote**: "Early signs are promising as the company built a new customer insight app in less than 30 days using Cursor and a sales training tool in just under two weeks. Both are projects that would previously have required outside vendors or quarters of internal work."
- **Our assessment**: This is a "beyond engineering" claim in the same vein as the NAB note's Claim 9 (10,000+ employee expansion including product, design, leadership), but the IMDEX version is about internal build-vs-buy substitution rather than training-path expansion — the claim is that non-core internal tools (customer insight, sales training) that would previously have gone to an outside vendor are now built in-house with Cursor. The "quarters of internal work" comparator is vague (no specific quarter count given) and the projects themselves are undescribed beyond their category, so this should be treated as a directional example rather than a measured claim.

### Claim 10: Richard Zampieri reframes the constraint on AI-accelerated delivery as organizational (decision-making, priorities) rather than technological
- **Evidence**: Closing quote of the article, presented as the forward-looking takeaway.
- **Confidence**: anecdotal (single practitioner's framing/opinion, not a measured claim)
- **Quote**: "Our limitation now is decision-making, priorities, not technology. We need to oil the entire company engine, not just software engineering to be able to build and deliver products faster." — Richard Zampieri, Principal Engineer/AI Lead, IMDEX
- **Our assessment**: This is the most guide-relevant framing claim in the source: once engineering delivery speed increases via AI, the bottleneck shifts to non-engineering decision-making (product prioritization, cross-functional sign-off, business process). This is conceptually adjacent to `blog-cursor-nab-legacy-migration.md`'s framing (Claim 8: AI tools as "cross-role coordination platform" bringing engineers, architects, product, and security into the same workflow) but makes a sharper claim: it isn't just that AI coordinates roles better, it's that once engineering is no longer the constraint, the whole company's decision cadence becomes the new limiting factor. Worth citing directly if the guide discusses what happens organizationally *after* AI removes an engineering bottleneck.

## Concrete Artifacts

### Headline Metrics (stat callout box)

```
IMDEX case study — Cursor blog stat callout

10x       — Faster pace on legacy migration vs. pre-AI model
8 months / 6 months — Data platform and Angular→React migration (vs. 2-5 years)
Millions  — Development cost avoided by leveraging the existing team
```

### Two Named Project Outcomes

```
Project 1: Data-platform consolidation (two flagship geological mapping tools → one platform)
  Attribution:  Rob van Selm, Head of Software Development
  Duration:     8 months with Cursor
  Counterfactual estimate: 20 additional engineers, millions of dollars, 2-3 years without Cursor
  Function:     Synchronizes core sample data to the cloud, connects IMDEX's IoT devices and
                analytics systems, shared data layer across the field/web platform
  Personas:     Drillers — live guidance vs. planned hole path, "cone of tolerance"
                Geologists — data quality/reliability protection for subsurface interpretation

Project 2: Angular-to-React migration (legacy Angular app → React micro frontend)
  Duration:     6 months with Cursor
  Counterfactual estimate: 3-5 years without Cursor
  Stated goal:  Easier maintenance and new feature development
```

### AI July Training Curriculum

```
IMDEX "AI July" program (attributed to company-wide initiative, one calendar month)

101-level: agent basics — context windows, model selection, token consumption
201-level: advanced tooling — MCPs, skills, hooks, agent parallelization
Applied:   dedicated hackathons on real product problems
```

### Three Named IMDEX Practitioner Quotes (full attribution)

```
Rob van Selm, Head of Software Development [also described as "Head of Software
Development and Solutions"], IMDEX:
  "Without Cursor, building these workflows might have taken 20 new people, millions
  of dollars, and two to three years. With Cursor, we're increasing the leverage of
  people we already have. That's a huge technical and financial win for the
  organization."
  "We are using Cursor to accelerate every part of the software lifecycle, ultimately
  making product releases much faster."

Nathan Davey, Principal Software Engineer, IMDEX:
  "The old ecosystem was not coherent for the customer and presented difficult
  challenges for us when it came to building new features and maintaining old ones."

Richard Zampieri, Principal Engineer/AI Lead, IMDEX:
  "We've tried tools from multiple providers, but we have always landed back on
  Cursor because the user experience is so much better."
  "The Cursor Dashboard and Analytics API provide easy insights into usage patterns
  across our team so we can understand adoption. Those insights make it easy to
  justify our investment."
  "Our limitation now is decision-making, priorities, not technology. We need to oil
  the entire company engine, not just software engineering to be able to build and
  deliver products faster."
```

## Cross-References

- **Corroborates**:
  - `blog-cursor-nab-legacy-migration.md` Claim 2 (task-appropriate model selection — cheaper models for routine work, advanced/thinking models for architecture — as a first-class enterprise tool-evaluation criterion). IMDEX's Claim 5 model-flexibility description ("higher-thinking models for ambiguous design decisions and simpler models for contained implementation work") independently describes the same routing heuristic NAB names explicitly. Two named enterprises now describe the identical pattern, which strengthens it from a single anecdote to a repeated practitioner pattern.
  - `blog-cursor-nab-legacy-migration.md` Claim 4 (intentional enablement strategy — training on real production work — as key to enterprise rollout). IMDEX's Claim 6 "AI July" program is a second, independently structured instance of dedicated hands-on training paired with real product work, corroborating that structured enablement (not organic/self-directed adoption alone) is a recurring enterprise pattern. IMDEX's version is more novel in its curriculum structure (101/201/hackathon tiering) than NAB's "sprint days," so treat this as corroboration of the pattern with a distinct implementation detail.
  - `blog-cursor-better-models-ambitious-work.md` Claim 2 (developers shift toward complex/ambiguous tasks with better models after an adoption lag). IMDEX's Claim 5 description of choosing "higher-thinking models for ambiguous design decisions" is consistent with — though does not independently measure — the complexity-routing behavior that study documents at the aggregate/behavioral level.

- **Contradicts**: None identified. The claimed multipliers (Claims 1-3) differ in magnitude from NAB's project-level multiples (e.g., NAB's BizCalc pre-dev compression of ~8x vs. IMDEX's platform-consolidation ~3-4.5x), but these describe different projects at different companies and are not framed as competing claims about the same phenomenon — this is variance between vendor case studies, not a contradiction as defined in MINER.md §4a (no single guide recommendation would need to pick a side between them).

- **Extends**:
  - `blog-cursor-nab-legacy-migration.md` Claim 1 (enterprise tool-evaluation criteria: model flexibility, codebase understanding, extensibility). IMDEX's Claim 4-5 add a second named-enterprise data point for tool evaluation, but with a materially thinner evidentiary basis — IMDEX does not name which competing tools were evaluated or what specific criteria eliminated them (unlike NAB, which names Amazon Q and GitHub Copilot and describes why each fell short). IMDEX does add one criterion NAB's note does not surface as clearly: preserving a "familiar workspace" (existing IDE, debugger, browser, design tool access) as a distinct adoption driver, separate from the agent's raw capability.
  - `blog-cursor-nab-legacy-migration.md`'s Guide Impact section on legacy modernization: this source provides a second (non-financial-services) domain — mining/geological data — for the "legacy migration + data consolidation" pattern, extending the corpus beyond banking (NAB) and general SaaS (Amplitude, Wayfair) into a physically safety/cost-critical operational domain.

- **Novel**:
  - **Operational-cost-critical domain framing** (Claim 8): No prior corpus source frames AI-coding-tool adoption risk against a concrete per-day operational cost figure comparable to mining's $300k-$2M/day drilling programs. This is a distinct "why does data fidelity matter here" argument that the guide's risk/adoption-caution sections do not yet have a domain example for.
  - **Tiered training curriculum (101/201/hackathon) for a company-wide adoption month** (Claim 6): The specific curriculum structure (concept tier → advanced-tooling tier → applied hackathon, time-boxed to one calendar month) is a more concrete, reusable template than NAB's "sprint days" framing or the general enablement claims elsewhere in the corpus.
  - **Post-engineering-bottleneck reframing** (Claim 10): The explicit claim that once AI removes the engineering-delivery bottleneck, the constraint shifts to company-wide decision-making and prioritization is not stated this directly elsewhere in the corpus (the NAB note's "cross-role coordination platform" claim is adjacent but frames it as tool-driven coordination, not a bottleneck-shift observation).
  - **Internal build-vs-buy substitution outside engineering** (Claim 9): The customer-insight-app (30 days) and sales-training-tool (2 weeks) examples are a distinct claim type — non-engineering internal tools that would previously have been outsourced now built in-house — not covered by the NAB note's non-engineering adoption claim (which is about training/onboarding expansion, not build-vs-buy substitution).

## Guide Impact

- **Chapter on Enterprise Governance / Adoption Playbooks (Ch04/Ch05)**: Add IMDEX's "AI July" curriculum (Claim 6, Concrete Artifacts) as a second, more structured template for enablement programs alongside NAB's sprint-days pattern (`blog-cursor-nab-legacy-migration.md` Claim 4). The guide could recommend the 101 (concepts) → 201 (advanced tooling) → hackathon (applied) sequence as a concrete curriculum shape for teams designing their own adoption month, rather than leaving "structured training" as an unspecified recommendation.

- **Chapter on Legacy Modernization / Technical Debt (Ch05 or planned)**: Add IMDEX's data-platform consolidation and Angular-to-React migration (Claims 2-3) as a second domain (mining/geological data, vs. NAB's banking) corroborating that legacy migration timelines compress substantially with AI-assisted development, while flagging — per Our assessment on Claims 2-3 — that both figures are engineer-estimated counterfactuals, not measured before/after baselines. The guide should keep this caveat explicit rather than presenting "8 months vs. 2-3 years" as a validated measurement.

- **Chapter on Risk / Adoption Caution in Critical-Operations Domains (Ch04 or new subsection)**: Add the drilling-cost framing (Claim 8) as the corpus's first example of an AI-coding-tool adoption case study explicitly set in a domain with a quantified per-day operational cost of error. Useful for a guide section distinguishing "move fast" domains from domains where data-fidelity stakes justify slower, more cautious rollout — note that the source itself does not report any operational outcome measurement of the AI-built platform in live drilling use, only IMDEX's stated design intent and caution.

- **Chapter on Measuring AI Adoption (Ch05 or planned)**: Add IMDEX's use of the Cursor Dashboard/Analytics API for "PR volume per developer" (Claim 7) as an example of vendor-supplied usage analytics being used for investment justification — paired with a caution that this is a volume metric, not an outcome/quality metric, and no specific values are disclosed in the source. Useful contrast case for a guide section on choosing better (outcome-based) adoption metrics.

## Extraction Notes

- **Full article fetched via WebFetch**: The article (~1,000 words, single page, no linked sub-pages) was fetched in full via WebFetch with an instruction to reproduce text verbatim rather than summarize. No sub-pages were followed (the article is self-contained; the only outbound link is a generic "start a Cursor trial" CTA, not a substantive linked page). As with the NAB note's extraction caveat, quotes here reflect the WebFetch-converted text; the Assayer should spot-check exact quotes against the live URL for any markdown-conversion artifacts (e.g., smart-quote/apostrophe normalization).
- **No named competing tools**: Unlike the NAB note (which names Amazon Q and GitHub Copilot), this source does not name which "multiple providers" IMDEX evaluated before standardizing on Cursor (Claim 4). This is a real gap in the source, not an extraction omission — flagged explicitly in Claim 4's assessment.
- **No independent validation of any metric**: All timelines, cost-avoidance figures, and the headline "10x" are vendor-published and sourced from named IMDEX practitioners with no external measurement. Consistent with `blog-cursor-nab-legacy-migration.md` and the general pattern across the corpus's Cursor customer case studies, this note rates confidence_overall as emerging rather than settled or anecdotal — several claims are specific and consistently repeated (raising them above anecdotal) but none are independently verifiable (keeping them below settled).
- **Triage comments in the source issue were partially inconsistent**: Issue #2964 carries three separate Prospector triage comments with differing chapter suggestions and one differing claim list. This extraction follows the most detailed and specific of the three (the third comment's "Extract guidance for Miner" section, which names the two most relevant overlapping notes) but independently verified all claims and quotes against the fetched article rather than trusting the triage comment's paraphrases.
- **No contradiction filed**: Per MINER.md §4a, differing productivity multiples between vendor case studies (IMDEX vs. NAB vs. Amplitude) are not filed as a contradiction — they describe different projects at different companies, not opposing claims about the same situation that would force a single guide recommendation to pick a side.
