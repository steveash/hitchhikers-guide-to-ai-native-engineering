---
source_url: https://openai.com/index/building-an-ai-native-finance-function
source_type: blog-post
title: "What building an AI-native finance function taught me"
author: Sarah Friar (CFO, OpenAI)
date_published: 2026-08-10
date_extracted: 2026-08-19
last_checked: 2026-08-19
status: current
confidence_overall: anecdotal
issue: "#2780"
---

# What building an AI-native finance function taught me

> OpenAI CFO Sarah Friar's first-party account of building OpenAI's finance
> function from scratch around two aspirational goals — a "zero-day close"
> and continuously updated forecasting — organized into five practitioner
> lessons: broad access paired with structured experimentation, redesigning
> the full decision workflow rather than individual tasks, finance
> professionals becoming tool builders, pairing AI speed with explicit
> accountability, and measuring AI value per unit of intelligence rather
> than seats or tokens consumed.

## Source Context

- **Type**: blog-post (OpenAI company blog, `openai.com/index/`, bylined to
  Sarah Friar, OpenAI's CFO; published August 10, 2026; auto-discovered via
  the `openai-news` trusted RSS feed)
- **Author credibility**: Named, senior first-party source — Friar is
  OpenAI's own CFO, writing about the finance function she has built at
  OpenAI over the two years since joining ("When I joined OpenAI two years
  ago, there was only a small finance team..."). This is the OpenAI-vendor
  counterpart to Anthropic's `blog-anthropic-fong-finance-narrative.md`
  (a corporate finance analyst's account of Claude usage): both are
  first-party practitioner accounts from AI labs describing their own
  internal finance functions, with the obvious incentive that OpenAI is
  both the subject and the AI vendor. Friar's account is at a higher
  organizational altitude than Fong's (CFO/function-owner vs.
  individual-contributor analyst) and is explicitly framed as strategic
  lessons "every CFO can apply," not a walkthrough of Friar's own daily
  tool use — the article never names a specific OpenAI product (ChatGPT,
  Codex, GPT) as *the* mechanism for a claim except in two places (custom
  GPTs; "ChatGPT Work and Codex"), and gives no architecture diagrams, no
  named case-study companies other than OpenAI itself, and no independent
  verification of any figure.
- **Scope**: Covers OpenAI's own internal finance-function transformation
  across five named lessons: (1) broad access paired with structured
  hackathon-style experimentation, (2) redesigning the full workflow around
  a decision rather than a single task, illustrated by the "zero-day close"
  and continuous-forecasting ambitions, (3) finance professionals building
  their own tools with ChatGPT Work and Codex, (4) pairing AI speed with
  explicit accountability and controls, illustrated by IR-GPT, and (5)
  measuring AI value "per unit of intelligence" via a four-question
  workflow scorecard. Does NOT cover: OpenAI's actual current close-cycle
  time or forecast-accuracy numbers (both ambitions are explicitly
  described as in-progress, not achieved), a token/dollar cost figure for
  any of the AI tooling described, headcount of the finance team, or any
  named finance-team member other than Friar herself. No sub-pages were
  linked from the article that required following.

## Extracted Claims

### Claim 1: OpenAI organized its finance-function transformation around two explicit, still-unfinished ambitions — a "zero-day close" and automated, continuously updated forecasting — rather than a list of point-tool deployments

- **Evidence**: Friar's own framing of the article's central thesis, stated early and returned to at the close of the piece.
- **Confidence**: anecdotal (single CFO's account of her own organization's strategic framing; not a benchmarked methodology)
- **Quote**: "So we set two bold ambitions: a zero-day close and automated, continuously updated forecasting."
- **Our assessment**: Naming two destination states up front — rather than a tool rollout plan — is a notable structural choice: it gives the finance team a shared target to redesign workflows around (Claim 5 below), instead of a checklist of AI features to adopt. The honesty signal worth flagging is that Friar explicitly states this is unfinished work ("We are still building toward both ambitions"), not a completed transformation — the guide should not cite either ambition as an achieved outcome.

### Claim 2: A "zero-day close" means a continuously reconciled, traceable view of financial position where AI drafts variance explanations and flags exceptions, but finance retains validation, judgment, and final sign-off

- **Evidence**: Friar's direct architectural description of the close workflow, paired with a described (not literally reproduced) dashboard screenshot captioned as a "finance-owned review."
- **Confidence**: anecdotal (architectural description from a single company; no metrics on reconciliation accuracy, exception volume, or cycle-time reduction are given)
- **Quote**: "AI can prepare an initial explanation and flag the exceptions that require attention. Finance validates the numbers, applies judgment, and owns the final sign-off."
- **Our assessment**: This is the same "AI drafts, human retains sign-off" division of labor already well established in this corpus's finance-vertical sources (see Cross-References), but Friar's specific mechanism — AI proposes an explanation *and* flags which variances need human attention, rather than requiring a human to first find the exceptions — is a slightly more automated framing than Fong's "integrity layer" (Claude validates consistency; the human still initiates the check). The guide should note this is Friar's stated target architecture, not a described, shipped system with measured exception-detection accuracy.

### Claim 3: Broad AI access creates the most value only when paired with structured experimentation on real problems — illustrated by a cross-functional finance hackathon that produced IR-GPT, a custom GPT for investor-diligence questions grounded in approved materials

- **Evidence**: Direct description of a hackathon that brought sales engineers into the finance team and asked participants to bring their own work to transform, with IR-GPT named as one concrete output.
- **Confidence**: anecdotal (single described event; no participation count, no before/after time metric for IR-GPT specifically is given in this section — see Claim 7 for the accountability framing of the same tool)
- **Quote**: "We brought sales engineers into a finance hackathon and asked the team to bring work they wanted to transform. One result was IR-GPT, a custom GPT grounded in the approved materials our investor relations team uses to answer diligence questions."
- **Our assessment**: The specific claim — access alone is necessary but not sufficient, and *structured experimentation around real problems* is what converts access into usable tools — is Friar's answer to "how do you get an organization from having AI access to actually using it well." Pairing engineers with finance staff for the hackathon (rather than running it finance-only) is a concrete cross-functional-enablement mechanism not otherwise detailed in the article.

### Claim 4: CFOs should combine bottom-up experimentation (people closest to the work identify use cases) with top-down strategy (leadership focuses resources on what matters most), because the highest-value ideas emerge where the two meet

- **Evidence**: Friar's direct prescriptive statement, generalizing from the hackathon experience (Claim 3) into advice for other CFOs.
- **Confidence**: anecdotal (prescriptive opinion generalized from one company's experience)
- **Quote**: "For CFOs, the lesson is simple: you need bottom-up experimentation and top-down strategy. Put secure, capable AI in people's hands and let those closest to the work identify better ways of getting things done. At the same time, focus leadership attention and resources on the changes that will matter most to the business. The real opportunity comes when both meet: practical ideas from the front lines applied to your biggest priorities."
- **Our assessment**: This "meet in the middle" framing — bottom-up discovery of *what's possible*, top-down direction of *what matters* — is a specific articulation of the general access-plus-strategy adoption pattern documented elsewhere in the corpus for enterprise AI rollouts, restated here for a finance-specific audience with no new mechanism beyond the hackathon example already given.

### Claim 5: Finance leaders should redesign the entire path from source data to decision — mapping data, tools, approvals, and handoffs and determining which parts AI can analyze, coordinate, or complete — rather than automating individual tasks within the existing process

- **Evidence**: Friar's direct statement of the article's broadest prescriptive claim, following the close/forecasting examples (Claim 1-2).
- **Confidence**: anecdotal (prescriptive framing; no comparison given between task-level automation and full-workflow redesign outcomes)
- **Quote**: "The broader lesson is to begin with a consequential decision and work backward. Map the data, tools, approvals, and handoffs required to support it. Then determine which parts AI can analyze, coordinate, or complete. This improves the speed and quality of the entire decision cycle."
- **Our assessment**: "AI changes the unit of work" (stated earlier in the same section) is the underlying claim this lesson operationalizes: rather than asking "which task can AI do faster," Friar's prescription is to ask "which decision matters, and what is the full assembly chain behind it." This reframes AI adoption scoping from task-level to decision-level, which is a more specific and more actionable framing than generic "find high-value AI use cases" advice.

### Claim 6: Finance professionals are becoming builders — citing OpenAI's own cross-occupation research that 40% of finance professionals' specialized AI use is work outside traditional finance and 22% is engineering-related, illustrated by a non-coding teammate who used Codex to build an advertising-forecast tool

- **Evidence**: A cited internal OpenAI statistic (linked to a separate OpenAI report) plus a named-role (not named-individual) case example: an advertising-business teammate with no prior coding experience used Codex to build a tool converting monthly ad forecasts into weekday/holiday-aware weekly and daily plans.
- **Confidence**: emerging for the cited statistic (a specific, sourced OpenAI research figure, though this Miner did not re-verify it against the underlying report in this extraction pass); anecdotal for the Codex case example (single unnamed individual, no before/after time metric)
- **Quote**: "Recent [OpenAI research](https://openai.com/index/how-ai-is-expanding-what-people-do-at-work/) shows that 40% of finance professionals' specialized AI use involves work outside traditional finance, and 22% involves engineering-related tasks."
- **Quote**: "One teammate supporting our advertising business had never coded. He used Codex to build a tool that turns our monthly advertising forecast into weekly and daily plans. It accounts for weekdays and holidays, compares forecasts, and keeps every number tied to the approved model."
- **Our assessment**: The 40%/22% figures are drawn from OpenAI's own "Work at the Frontier" task-crossover report, already extracted in depth in `blog-openai-work-frontier-task-crossover.md` — see Cross-References for why this is a genuine *extension* of that note (finance-specific figures the earlier note's Miner did not capture) rather than a repeated claim. The Codex anecdote is a concrete, named-product instance of "finance professionals become builders": it corroborates the corpus's existing evidence that non-developers are adopting Codex faster than developers (see Cross-References), giving that statistical trend a specific finance-domain example (ad-forecast planning) rather than a generic one.

### Claim 7: AI should accelerate drafting work while humans retain ownership of the result — illustrated by IR-GPT, where the investor-relations team reads every draft, adds judgment, and checks cross-investor consistency before anything goes out

- **Evidence**: Direct description of how IR-GPT output is used downstream of generation, contrasted with the pre-AI process (hours of manual search, sometimes continuing overnight).
- **Confidence**: anecdotal (single tool, single team, no error rate or rework-rate data given for IR-GPT drafts)
- **Quote**: "With a custom GPT grounded in approved sources, work that previously took hours, and sometimes continued overnight, can now produce a strong first draft in seconds." ... "The human role remains central. Our investor relations team reads the draft, adds judgment and context, and checks that our answers remain consistent across investors. AI accelerates the work. People own the result."
- **Our assessment**: "AI accelerates the work. People own the result." is the article's clearest single-sentence formulation of its human-AI division-of-labor thesis, and it is a two-clause, ownership-centered variant of the same principle Fong names as "integrity layer underneath / narrative on top" (see Cross-References) — Friar's version foregrounds *accountability* (who owns the result) rather than *where the work happens* (which layer). The "sometimes continued overnight" detail is a concrete, checkable characterization of the pre-AI diligence-response process that grounds the "hours" claim in a specific operational pain point (after-hours turnaround pressure) rather than a generic time estimate.

### Claim 8: CFOs should work with IT and governance teams to define upfront which data an AI system can access, which actions it can take, when approval is required, and when an issue should be escalated — treating this as a control design question, not an afterthought

- **Evidence**: Friar's direct prescriptive statement, generalizing from the IR-GPT example into a governance framework for CFOs broadly.
- **Confidence**: anecdotal (prescriptive framing; no description of how OpenAI itself implements this framework operationally beyond the general statement)
- **Quote**: "CFOs should work with IT and governance teams to define which data an AI system can access, which actions it can take, when approval is required, and when an issue should be escalated. Every output should connect to a reliable source. Every forecast should carry a clear explanation. Every change to an approved baseline should require finance authorization."
- **Our assessment**: The three-part control checklist (data access scope, action scope, escalation triggers) is a specific, actionable governance framework distinct from generic "have a human in the loop" advice — it names three separate control points (access, action, escalation) that a CFO can audit independently. The three "every output/forecast/change" sentences that follow function as concrete acceptance criteria for what "controlled" looks like in practice (source-traceable, explained, authorization-gated), giving the abstract framework testable shape.

### Claim 9: The "tokenmaxxing" era has ended, and usage limits, budget controls, role-based access, model-routing rules, and approval thresholds are now straightforward for CFOs to configure, allowing AI spend to be managed with the same discipline as any variable expense

- **Evidence**: Friar's own characterization of the current state of AI usage-governance tooling, presented without a supporting metric or named vendor/product.
- **Confidence**: anecdotal (a single CFO's characterization of tooling maturity, dated August 2026, with no metric, product name, or comparison to the prior "craze" state given)
- **Quote**: "The brief craze of "tokenmaxxing" has come and gone. It is now straightforward to set usage limits, budget controls, role-based access, model-routing rules, and approval thresholds. CFOs can manage AI usage with the same discipline they bring to any variable expense while giving teams room to build and experiment."
- **Our assessment**: This is a specific and checkable-in-principle claim about the AI-governance tooling market having matured to "straightforward" by August 2026 — see Cross-References for a discussion of the tension between this claim and `blog-thoughtworks-kamelman-token-crisis.md`'s (June 2026) characterization of AI token spend as an ongoing, unresolved "crisis" requiring architectural and cultural change. This Miner judged the tension to be a scope/vintage difference rather than a direct contradiction (see Extraction Notes) and did not file a contradiction issue, but flags it here for the Assayer/Smith to weigh independently.

### Claim 10: A useful CFO scorecard for AI value asks four questions per workflow — did AI complete work that mattered, what did it cost including human time, was the result good enough to use, and did it help move faster or decide better — rather than tracking seat counts or token volume

- **Evidence**: Friar's own stated framework, presented as a direct alternative to seat- or token-based AI usage metrics.
- **Confidence**: anecdotal (prescriptive framework; no worked numerical example applying all four questions to a specific OpenAI workflow is given)
- **Quote**: "CFOs need a scorecard for AI grounded in operating performance. Buying more seats or using more tokens doesn't tell you much. What matters is whether the work gets done well and what it really costs." followed by: "Did AI complete work that mattered?" / "What did it cost, including employee time, review, and rework?" / "Was the result good enough to use?" / "Did it help us move faster or make a better decision?"
- **Our assessment**: "Value per unit of intelligence" is Friar's named framing for this scorecard (used in the section heading), and the explicit inclusion of "employee time, review, and rework" in the cost question is the most operationally important detail — it rules out counting only API/token spend as "cost," requiring the reviewing/rework burden a tool creates to be netted against its output. The companion claim that "the cheapest model isn't always the most economical" (a separate sentence in the same section) extends this to model-selection decisions specifically: a higher-priced model that reaches a reliable answer in fewer attempts and with less review may have a lower *total* cost than a cheaper model that requires more rework.

### Claim 11: An AI-native finance function is defined by faster cycles, stronger controls, better decisions, and more time for judgment — and CFOs have a unique, board/strategy-adjacent mandate to lead AI transformation because finance sits at the intersection of strategy, capital, data, risk, and performance

- **Evidence**: Friar's closing summary framing, presented as the article's thesis restated at the top organizational altitude (CFO mandate, not team-level workflow detail).
- **Confidence**: anecdotal (closing editorial framing; not a separately measured or evidenced claim beyond the workflow examples given earlier in the piece)
- **Quote**: "Finance sits at the center of strategy, capital, data, risk, and performance. That gives CFOs a unique view of how the company works and a powerful mandate to lead its AI transformation." ... "An AI-native finance function is defined by faster cycles, stronger controls, better decisions, and more time for judgment."
- **Our assessment**: This four-part definition (faster cycles, stronger controls, better decisions, more time for judgment) functions as Friar's own summary rubric for "AI-native" in the finance context specifically — useful as a named, citable definition distinct from the guide's general-purpose "AI-native" framing, since it explicitly folds in *controls* (not just speed) as a defining criterion, consistent with Claim 8's governance emphasis.

### Claim 12: CFOs must personally model AI use to their teams — "you can't be what you can't see" — framing leadership demonstration as a prerequisite for finance teams embracing AI

- **Evidence**: Friar's closing line, presented as a personal maxim ("As I always say") applied to the CFO's role specifically.
- **Confidence**: anecdotal (personal maxim; no description of how Friar herself models this behavior day-to-day is given in the article)
- **Quote**: "As I always say, you can't be what you can't see. If we want our finance teams to embrace what's possible with AI, we have to show them what it looks like—and as CFOs, that starts with us."
- **Our assessment**: This is a finance-specific, CFO-level instance of the "leaders must use the tool themselves to drive adoption" pattern already documented elsewhere in the corpus at a similar or higher executive altitude (see Cross-References) — Friar's contribution is the specific aphorism ("you can't be what you can't see") rather than a new mechanism, and the article gives no concrete example of Friar's own personal AI usage to substantiate the claim beyond her general authorial voice throughout the piece.

## Concrete Artifacts

```
Source: OpenAI, "What building an AI-native finance function taught me,"
Sarah Friar (CFO), https://openai.com/index/building-an-ai-native-finance-function
(published August 10, 2026)

FIVE NAMED LESSONS (article's own section structure):
  1. Give everyone access, then create a reason to use it
  2. Redesign the full workflow around the decision
  3. Finance professionals become builders
  4. Pair speed with clear accountability and controls
  5. Measure value per unit of intelligence

FOUR-QUESTION AI VALUE SCORECARD ("per unit of intelligence"):
  - Did AI complete work that mattered?
  - What did it cost, including employee time, review, and rework?
  - Was the result good enough to use?
  - Did it help us move faster or make a better decision?

SUGGESTED PER-DOMAIN SCORECARD METRICS (from article prose, not a
verbatim source list):
  Close:        cycle time; share of transactions reconciled
                automatically; number of exceptions requiring review;
                time required to explain a variance
  Forecasting:  forecast accuracy; refresh frequency; time to produce
                a new scenario; quality of decisions the forecast
                supports

NAMED TOOLS/ARTIFACTS:
  IR-GPT           — custom GPT grounded in approved investor-relations
                      materials, built at a finance hackathon, used to
                      draft first-pass answers to diligence questions
  (unnamed)        — custom GPTs also being built for procurement and tax
  Ad-forecast tool — built via Codex by a non-coding advertising-business
                      teammate; converts monthly ad forecast into
                      weekday/holiday-aware weekly and daily plans,
                      keeping every number tied to the approved model

DASHBOARD CAPTIONS (images not reproduced; captions quoted verbatim,
each attributed to a described screenshot in the article):
  "Budget-versus-actuals reconciliation: approved inputs, source checks,
  and a finance-owned review" — captioned as a "Codex-generated finance
  review" per the image's own alt text
  "Interactive forecasting and scenario planning"
  "Dynamic capital allocation: diminishing-return curves highlight where
  investment should be rebalanced"

CFO GOVERNANCE CHECKLIST (from "Pair speed with clear accountability
and controls" section):
  - Define which data an AI system can access
  - Define which actions it can take
  - Define when approval is required
  - Define when an issue should be escalated
  - Every output should connect to a reliable source
  - Every forecast should carry a clear explanation
  - Every change to an approved baseline should require finance
    authorization
```

## Cross-References

### Cross-reference verification notes

`blog-anthropic-fong-finance-narrative.md`, `blog-anthropic-kepler-verifiable-ai-financial.md`,
`blog-openai-work-frontier-task-crossover.md`, `blog-openai-codex-knowledge-work.md`,
`blog-simonwillison-uber-caps-usage.md`, and `blog-thoughtworks-kamelman-token-crisis.md`
were re-read directly (MINER.md §4b) and the claim numbers cited below were
confirmed against each note's own numbered `### Claim N:` headings in
document order before writing this section.

- **Corroborates**:
  - `blog-anthropic-fong-finance-narrative.md` Claim 5 ("Claude does all of
    this for me now: it holds the integrity layer underneath the work, so
    my time goes to the narrative on top") and Claim 3 (narrative-integrity
    validation as the primary board-cycle value driver): Friar's Claim 7
    ("AI accelerates the work. People own the result.") is the OpenAI-vendor
    restatement of the same human-AI division of labor in a finance
    context, from a different company and a different named product
    (custom GPTs vs. Claude Cowork). The two independently converge on
    "AI drafts/accelerates, humans retain ownership/judgment" as the
    finance-function division of labor, from competing AI labs describing
    their own internal finance teams.
  - `blog-openai-codex-knowledge-work.md` Claim 2 (non-developers now
    ~20% of Codex's user base and adopting more than 3x faster than
    developers): Friar's Claim 6 example (a non-coding advertising
    teammate building a forecasting tool with Codex) is a specific,
    named-domain instance of exactly this adoption trend — a finance/
    ad-ops worker, not a developer, using Codex as a builder tool.
  - `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 3 (Claude
    treated as one stage in a pipeline; deterministic infrastructure
    handles what must be provably correct) and Claim 9 (provenance must
    be designed in from day one): Friar's zero-day-close description
    (Claim 2 — "every number tied to the approved model," AI flags
    exceptions but finance owns sign-off) is directionally consistent
    with Kepler's reasoning/execution separation, though far less
    architecturally specific — Friar names no deterministic-execution
    layer or provenance chain, only that finance validates and signs off.

- **Contradicts**: None filed. A tension was evaluated and not filed — see
  Extraction Notes for the reasoning.

- **Extends**:
  - `blog-openai-work-frontier-task-crossover.md` Claim 3 (per-occupation
    outside-task shares: customer experience 77%, design 75%, HR 69%,
    legal 56%, marketing 53% — finance was one of the seven occupation
    groups studied but was not among the five reported in that note's
    Claim 3 list, and that note's Concrete Artifacts section does not
    include a finance-specific figure): Friar's Claim 6 cites the same
    underlying OpenAI "Work at the Frontier" report but supplies the
    finance-specific figures the earlier note's Miner did not capture —
    40% of finance professionals' specialized AI use is outside
    traditional finance, and 22% is specifically engineering-related.
    These two figures should be read together with the earlier note's
    Claim 4 (financial calculation appears among the top-3 "outside
    tasks" borrowed by all seven other occupation groups) as a fuller
    picture of finance's position in the task-crossover data: finance
    work is both commonly borrowed by other occupations (per the earlier
    note) and finance professionals themselves borrow substantially from
    other occupations, especially engineering (per this note).
  - `blog-anthropic-fong-finance-narrative.md`: Fong documents a single
    finance analyst's tool-level workflow (Claude Cowork + Claude for
    Excel) inside an existing, presumably already-somewhat-mature
    Anthropic finance function. Friar documents the same domain (AI-native
    finance) at the CFO/function-design altitude — two ambitions
    (zero-day close, continuous forecasting), an organization-wide
    hackathon, and a CFO-level governance and ROI-measurement framework.
    The two notes are complementary vendor-paired case studies at
    different organizational altitudes: Fong shows what daily practitioner
    use looks like; Friar shows how a CFO frames the function-wide
    transformation strategy around it.
  - `blog-anthropic-kepler-verifiable-ai-financial.md`: Kepler's
    deterministic-execution/provenance architecture is a far more
    specific, engineered version of the "AI drafts, deterministic/human
    layer verifies" pattern Friar describes only in prose (Claim 2, Claim
    8). Friar's article gives the CFO-level governance vocabulary
    (access/action/approval/escalation) that a team could use to scope
    what Kepler's engineers then built architecturally — the two sources
    operate at different levels of the same problem (governance framing
    vs. implemented architecture).

- **Novel**:
  - **"Zero-day close" and "value per unit of intelligence" as named,
    citable framings** (Claims 1, 10): Neither phrase appears elsewhere in
    the corpus. "Zero-day close" is a specific, named target-state for
    financial close automation (distinct from Kepler's provenance-chain
    architecture or Fong's narrative-integrity workflow) and "value per
    unit of intelligence" is a specific, named alternative to seat- or
    token-based AI usage metrics, with a four-question operationalization.
  - **The CFO-level access/action/approval/escalation governance
    checklist** (Claim 8): a specific, four-part control-design framework
    for AI systems handling financial data, not previously named in this
    corpus's finance-vertical sources at this level of operational
    specificity (Fong and Kepler describe what their systems do, not a
    generalized CFO checklist for scoping any AI system's access).
  - **A hackathon as the specific mechanism for converting broad AI access
    into adopted tools** (Claim 3): the corpus's existing finance-adoption
    sources (Fong, Kepler, BBVA) do not describe a hackathon as the
    adoption-catalyst event; BBVA's champions/wizards network and Fong's
    individual practitioner workflow are both different enablement
    mechanisms.
  - **"Tokenmaxxing" declared over, with governance tooling now
    "straightforward"** (Claim 9): the first source in this corpus to
    claim the token/usage-governance problem has moved from crisis to
    solved-by-tooling — see Cross-References → Contradicts discussion in
    Extraction Notes for why this was evaluated but not filed as a formal
    contradiction against `blog-thoughtworks-kamelman-token-crisis.md`.

## Guide Impact

- **Chapter 02 (Knowledge Work Transformation) / non-engineering AI
  adoption**: Add Friar's "AI changes the unit of work" framing (Claim 5)
  — scope AI adoption at the *decision* level (map data, tools, approvals,
  handoffs behind a consequential decision, then determine which parts AI
  can handle) rather than the individual-task level. This is a more
  specific scoping heuristic than the guide's existing general "find
  high-value use cases" advice, and pairs directly with Fong's narrative-
  synthesis framing as two ways of describing the same finance-function
  redesign.

- **Chapter 04 (Enterprise Adoption, non-engineering functions)**: Add the
  hackathon-with-cross-functional-engineers mechanism (Claim 3) as a named,
  concrete adoption-catalyst event, distinct from BBVA's champions/wizards
  network (`blog-openai-bbva-banking-transformation.md` Claim 4) and Fong's
  individual-practitioner adoption path. Pair with Claim 4's "bottom-up
  experimentation, top-down strategy" framing as the underlying principle
  the hackathon operationalizes.

- **Chapter 04 (Enterprise Adoption) / AI governance for regulated or
  high-stakes functions**: Add the access/action/approval/escalation
  checklist (Claim 8) as a citable, four-part control-design framework
  CFOs (or any function owner deploying AI against sensitive data) can use
  to scope a new AI system before deployment. Pair with Kepler's
  deterministic-execution architecture as the engineered instantiation of
  the same governance goal, one level more specific than Friar's prose
  checklist.

- **Chapter 06 (Tool Selection / Workflow Orchestration) / measuring AI
  value**: Add the four-question "value per unit of intelligence" scorecard
  (Claim 10) as a named alternative to seat-count or token-volume usage
  metrics. The explicit inclusion of "employee time, review, and rework" in
  the cost question, and the "cheapest model isn't always the most
  economical" corollary, are the most actionable, reusable pieces of this
  source for a guide section on evaluating whether an AI workflow is
  actually paying for itself.

- **Chapter 05 (Team Adoption) / leadership modeling**: Add Friar's "you
  can't be what you can't see" framing (Claim 12) alongside existing
  leaders-must-model-usage evidence (see Cross-References) as a finance-
  specific, CFO-level instance of the same pattern — useful as a citable
  aphorism, not as new mechanism.

## Extraction Notes

- **Retrieval method**: The live URL
  (`https://openai.com/index/building-an-ai-native-finance-function`)
  returned HTTP 403 to both the `WebFetch` tool directly and a `curl` fetch
  with a browser user-agent from Bash (the `curl` response was a
  client-side Cloudflare bot-challenge shell, ~10KB, no article content),
  consistent with the recurring `openai.com/index/` access difficulty
  already documented in this corpus's other OpenAI source notes (e.g.
  `blog-openai-work-frontier-task-crossover.md`,
  `blog-openai-bbva-banking-transformation.md`). The article was
  successfully retrieved via the `r.jina.ai` reader proxy fetched with
  `curl` directly (not through `WebFetch`, which would otherwise summarize
  through an intermediate model and risk paraphrasing per MINER.md §2a) —
  this returned the full raw article markdown, which was then read in full
  and used as the sole source for every quote in this note. The RSS feed
  (`https://openai.com/news/rss.xml`) was also checked directly and
  confirmed to contain only a one-sentence description, not full article
  text, so it was not usable as a primary extraction source.
- **The article's embedded images were not independently viewed** — this
  Miner extracted only the images' alt-text captions and italic
  photo-captions from the markdown, both reproduced verbatim in Concrete
  Artifacts. No dashboard UI detail, chart values, or on-screen numbers
  from the three referenced images (budget-vs-actual reconciliation,
  interactive forecasting, capital allocation) are represented in this
  note beyond what the captions themselves state.
- **Tension evaluated and not filed as a contradiction**: Claim 9's
  "the brief craze of 'tokenmaxxing' has come and gone... it is now
  straightforward to set usage limits, budget controls..." (August 10,
  2026) sits in some tension with
  `blog-thoughtworks-kamelman-token-crisis.md`'s framing (June 10, 2026,
  two months earlier) of AI token spend as an ongoing, unresolved "crisis"
  requiring architectural governance (semantic caching, tiered model
  routing, token circuit breakers) and organizational-culture change, tied
  to a deeper data-center energy-scarcity constraint. This Miner judged the
  tension does not rise to a filable contradiction per MINER.md §4a because
  the two sources address different scopes: Kamelman's "token crisis" is
  specifically about engineering-architectural token/context consumption
  costs (premium models on non-premium tasks, unbounded agent loops, verbose
  context) documented via named engineering-org budget overruns (Uber,
  Microsoft, GitHub); Friar's "tokenmaxxing" reference is a single sentence
  about CFO-level *usage-governance tooling* (limits, budgets, RBAC,
  model-routing rules, approval thresholds) becoming easier to configure —
  a claim about tooling/enablement availability, not a claim that
  enterprise AI token spend is no longer a material cost or architectural
  concern. The word "tokenmaxxing" itself, as defined in
  `blog-simonwillison-uber-caps-usage.md` Claim 4, refers narrowly to
  internal leaderboards rewarding raw token consumption as a productivity
  proxy — a narrower anti-pattern than Kamelman's broader cost-architecture
  crisis — and Friar's usage does not cleanly map to either the Uber note's
  narrow definition or Kamelman's broad one. Given this ambiguity plus the
  two-month gap and different intended audiences (CFO governance vs.
  engineering-architecture), this was judged a scope/vintage difference
  rather than a material contradiction that would force different guide
  advice on the same question. Flagged prominently here per MINER.md §4
  for the Assayer and Smith to weigh independently and file a contradiction
  themselves if they judge otherwise.
- **The 40%/22% statistic (Claim 6) was not independently re-verified**
  against the underlying `blog-openai-work-frontier-task-crossover.md`
  report in this extraction pass beyond confirming that note's existing
  text does not already contain a finance-specific breakdown (it does not
  — that note's Claim 3 lists only customer experience, design, HR, legal,
  and marketing). The 40%/22% figures are taken on Friar's authority as an
  OpenAI CFO citing OpenAI's own research, linked in-line in the source
  article.
- No contradiction issue was filed (see above). No sub-pages beyond the one
  linked OpenAI research report (`how-ai-is-expanding-what-people-do-at-work`,
  already covered by an existing source note per Cross-References → Extends)
  were followed, since that report is already separately extracted in this
  corpus.
