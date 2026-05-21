---
source_url: https://claude.com/blog/how-an-anthropic-sales-leader-uses-claude-cowork-to-run-a-4-000-account-book
source_type: blog-post
title: "How an Anthropic sales leader uses Claude Cowork to run a 4,000-account book"
author: Travis Bryant (Head of US Mid-Market GTM, Anthropic)
date_published: 2026-05-20
date_extracted: 2026-05-21
last_checked: 2026-05-21
status: current
confidence_overall: anecdotal
issue: "#835"
---

# How an Anthropic sales leader uses Claude Cowork to run a 4,000-account book

> First-party Anthropic practitioner case study documenting a named sales leader's daily,
> weekly, and quarterly Cowork workflows — including a 4,000-account overnight propensity
> scoring run — introducing the dimension-based scoring methodology and the overnight
> strategic-project pattern as the fourth documented non-engineering Cowork archetype
> (sales/account management at scale).

## Source Context

- **Type**: blog-post (first-party Anthropic practitioner case study; bylined to Travis
  Bryant, Head of US Mid-Market GTM at Anthropic; published May 20, 2026)
- **Author credibility**: Internal Anthropic employee in a senior GTM role, speaking from
  direct operational experience with the product his company sells. High credibility for
  workflow claims; the outcomes described (time savings, scoring runs) are testable in
  principle. No third-party corroboration of the metrics. The author has a clear interest in
  demonstrating Cowork value — treat efficiency claims as directional, not benchmarks.
- **Scope**: Covers Travis Bryant's personal daily, weekly, and quarterly Cowork workflows
  for a 4,000-account mid-market sales book. Focuses on scheduled task automation, a weekly
  forecast skill, and a large-scale overnight account propensity scoring run. Ends with
  prescriptive recommendations for sales teams. Does NOT cover: pricing, implementation
  details of Salesforce/BigQuery MCP connectors, or how to configure the skills technically.

## Extracted Claims

### Claim 1: Daily sales operations micro-automations (conference room booking + customer call prep) save approximately 90 minutes per day when run as scheduled skills

- **Evidence**: Travis Bryant describes two daily scheduled tasks: (1) a skill that scans
  Google Calendar and books conference rooms for external meetings missing one; (2) call prep
  that pulls BigQuery spend and Salesforce pipeline status into a brief automatically before
  each meeting.
- **Confidence**: anecdotal (single practitioner account; time estimate is author-reported)
- **Quote**: "Each morning, a scheduled task runs a skill that scans my Google Calendar and
  books a conference room for any external meeting that's missing one."
- **Our assessment**: Both workflows address the "prep overhead" problem common to account
  management roles. The conference room booking skill is a low-stakes, high-frequency
  automation — an ideal Level 3 candidate (bundle + schedule). The call prep automation
  demonstrates pulling from multiple live systems (BigQuery + Salesforce) into a synthesized
  brief. Together these illustrate how Level 3 skills reclaim time previously spent on
  mechanical data assembly tasks, consistent with `blog-anthropic-cowork-deploy-guide.md`
  Concrete Artifacts → "Five-Level Maturity Model" (Level 3: "Skills run on their own,
  return analysis, or run daily workflows").

### Claim 2: A weekly Friday forecast skill saves 3 hours per week by pulling Salesforce and BigQuery data into a single-page leadership report in the exact format required

- **Evidence**: Travis Bryant describes a scheduled skill that pulls Salesforce opportunity
  records and submitted commits, BigQuery token spend, and assembles a single-page web report
  for Anthropic's sales leadership — including top-line metrics, top deals, movers/decliners,
  and a forecast snapshot rolled up from first-line managers.
- **Confidence**: anecdotal (single practitioner, self-reported time savings)
- **Quote**: "It assembles a single-page web report in the exact format Anthropic's sales
  leadership wants to read: top-line metrics, top deals, movers and decliners, and the
  forecast snapshot rolled up from each first-line manager."
- **Our assessment**: The "exact format leadership wants to read" framing is practically
  significant: the skill encodes not just what data to pull but how to present it — a
  process-encoding win consistent with tribal knowledge codification in
  `blog-anthropic-cowork-deploy-guide.md` Claim 13. The 3-hour weekly savings is specific
  and plausible. The cross-system data pull (Salesforce + BigQuery) demonstrates the MCP
  connector pattern in a concrete sales ops context; the deploy guide's Sales archetype
  (Concrete Artifacts → SALES section) describes the same morning briefing and call prep
  patterns but does not specify these data sources.

### Claim 3: Account propensity scoring for 4,000 accounts — work previously requiring "hundreds of hours across RevOps, FP&A, and marketing" — can run overnight as a single Cowork skill

- **Evidence**: Travis Bryant describes running a full mid-market territory propensity
  scoring job overnight, using web research, Salesforce data, and BigQuery data to score all
  4,000 accounts with a numerical score and written rationale per dimension. He explicitly
  contrasts this with the prior state at "previous companies and roles."
- **Confidence**: anecdotal (single internal case study; the "hundreds of hours" comparison
  is from the author's career experience, not a controlled measurement)
- **Quote**: "In previous companies and roles, work like this ran for hundreds of hours
  across RevOps, FP&A, and marketing."
- **Quote**: "The biggest project I've run through Claude Cowork was account propensity
  scoring for the whole mid-market segment...I did it in one night."
- **Our assessment**: This is the highest-novelty claim in the source. The scale (4,000
  accounts, overnight) is a meaningful data point for practitioners evaluating what "large
  strategic project" workloads are feasible with Cowork. The contrast with multi-team,
  multi-week sprints is directionally credible — propensity scoring at this scale historically
  requires data pipeline work, analyst time, and cross-functional coordination. The
  generalization Bryant offers is the Prospector's key extraction target: "The 4,000-account
  scoring run is the showcase example, but the same shape works for TAM sizing, account
  research, comp benchmarking, anything historically deferred because no team had the hours
  for it." This positions the pattern as domain-agnostic.

### Claim 4: A two-tier dimension-based scoring methodology — separate rubrics for tech vs. industry accounts with 5 dimensions each — is a reusable template for account classification at scale

- **Evidence**: Travis Bryant describes defining two five-dimension scoring rubrics with
  Claude, one for tech accounts and one for industries. The tech rubric dimensions are
  explicitly named; the industry rubric includes knowledge-worker density and public AI
  commitments (measured via job posting mentions), with three additional dimensions not
  named in the article.
- **Confidence**: anecdotal (single practitioner methodology; not tested against other
  classification approaches)
- **Quote**: "I started by defining two five-dimension scoring rubrics with Claude: one for
  tech accounts and one for industries."
- **Our assessment**: The tech-vs-industry split acknowledges that propensity drivers differ
  by account type — a methodologically sound segmentation. The explicitly named tech
  dimensions (agent opportunity, internal transformation, AI commitment, white space against
  existing spend, industry fit) are a concrete example of translating business logic into a
  scoring framework. The "white space against existing spend" dimension is particularly
  notable: it incorporates current relationship data as a scoring input alongside market-fit
  signals, blending customer intelligence with prospecting logic.

### Claim 5: The "define → test → adjust → scale" methodology for scoring skills reduces iterative calibration risk before full-territory runs

- **Evidence**: Travis Bryant describes testing the scoring rubric on one territory, checking
  output, adjusting dimension weights based on the result, then running the next territory —
  before scaling to the full 4,000-account list.
- **Confidence**: anecdotal (single practitioner methodology; no comparison to other
  approaches)
- **Quote**: "run a test territory, check the output, adjust the weights ('I think D4 is
  probably weighted a little heavy; bring it down a bit'), run the next territory."
- **Our assessment**: This is the most operationally reproducible claim in the source. The
  pattern (test on a subset, calibrate, scale) is standard practice in scoring model
  development and translates directly to Cowork skill design. The specificity of the
  weight-adjustment step ("D4 is probably weighted a little heavy") illustrates that Cowork
  produces outputs that are human-reviewable at an intermediate stage — enabling iterative
  calibration without re-running the full territory. Guide chapters on scaling analytical
  skills should cite this as a risk-reduction pattern.

### Claim 6: Scheduled skills are more reliable than slash-command invocation because they remove the human as the triggering dependency

- **Evidence**: Travis Bryant explicitly contrasts pre-scheduled patterns with on-demand
  slash commands, noting that scheduling removes the forgetting risk.
- **Confidence**: anecdotal (author opinion; consistent with general observations about
  cognitive load and habit formation)
- **Quote**: "Once prep stops being a slash command I have to remember and starts running
  on its own, I stop forgetting it."
- **Our assessment**: This is a concrete formulation of the Level 2-to-Level-3 transition
  in `blog-anthropic-cowork-deploy-guide.md` Claim 10: the move from "invoke manually" to
  "runs on schedule." The "forgetting" framing reframes the value proposition of scheduling
  from time savings to reliability — a useful communication angle for practitioners who see
  Level 3 as optional. For a daily recurring workflow, the expected value of "not forgetting
  it" compounds over time.

### Claim 7: Building an interactive dashboard from analytical results converts scoring output into a sales operations tool with per-AE territory views and prospecting guidance

- **Evidence**: After running the overnight propensity scoring, Travis Bryant describes asking
  Claude Cowork to build an interactive dashboard from the results, where each AE clicks into
  their territory to see ranked accounts with rationales and hoverable case studies.
- **Confidence**: anecdotal (single case; implementation details of the dashboard not
  described)
- **Quote**: "Each AE clicks into their territory's pie slice and sees their accounts ranked
  by score, with the rationale generated for each dimension. Hovering over an account
  surfaces potential use cases and comparable case studies for prospecting."
- **Our assessment**: The "build a dashboard from the results" pattern is a distinct
  post-processing step — not part of the scoring skill itself. It converts analytical output
  into an operational tool, chaining two Cowork skills: (1) analytical scoring skill → 
  (2) dashboard generation skill → operational interface. The hover-to-surface-comparable-
  cases feature implies retrieval of similar accounts or prior case studies, making the
  dashboard useful for prospecting preparation, not just score reference.

### Claim 8: Interface accessibility — Cowork's document-centric, no-terminal interface — was the critical adoption enabler for a sales professional blocked by Claude Code's CLI requirement

- **Evidence**: Travis Bryant explicitly states he tried Claude Code but could not get
  comfortable with terminal interfaces, and that Cowork's interface was the turning point
  for his adoption.
- **Confidence**: anecdotal (single practitioner; plausibly representative of a broader
  non-technical knowledge-worker audience)
- **Quote**: "I tried Claude Code, but never got comfortable with working with the terminal.
  Claude Cowork wraps the same engine in an interface I can work in. That was when it
  clicked: I finally had a way to hand off the work and trust it would get done."
- **Our assessment**: This is the clearest first-person account in the corpus of the
  interface-as-adoption-barrier dynamic. The claim is not about preference but adoption
  completeness: Bryant could not use the product before Cowork's current form. The "same
  engine in an interface I can work in" framing positions Cowork as an accessibility layer
  over the same underlying capability, not a different product. For guide chapters on
  enterprise adoption, this is concrete evidence that interface choice determines reachable
  audience — consistent with `blog-anthropic-cowork-enterprise.md` Claim 6 ("vast majority
  of Cowork usage comes from outside engineering teams").

### Claim 9: The human-in-the-loop approval pattern — Claude proposes, human approves before anything ships — is the recommended deployment posture for scheduled skills with external outputs

- **Evidence**: Travis Bryant describes the approval-before-anything-ships pattern as built
  into his workflow.
- **Confidence**: anecdotal (single practitioner choice; consistent with staged autonomy
  patterns documented elsewhere)
- **Quote**: "the human-in-the-loop pattern is built in so Claude proposes and I approve
  before anything ships."
- **Our assessment**: This is the standard staged-autonomy posture from
  `blog-anthropic-cowork-deploy-guide.md` Claim 10 ("run it supervised, then run it
  scheduled"), applied to the external-output case (things that "ship" to AEs or
  leadership). Bryant has not yet removed the approval step — consistent with the documented
  pattern that trust-building precedes full automation. The fact that a senior Anthropic GTM
  employee uses this posture is credible evidence that human-in-the-loop approval remains
  appropriate even for well-characterized, internally-deployed workflows.

### Claim 10: The productivity dividend from automating data assembly and report formatting should be redirected to customer conversations and strategic decisions, not further automation

- **Evidence**: Travis Bryant frames the time reclaimed from mechanical data tasks as
  returning to "customer conversations and strategic decisions," and explicitly positions
  this as the reason sales professionals should adopt Cowork.
- **Confidence**: anecdotal (single practitioner intent; no measurement of how time is
  actually reallocated)
- **Quote**: "Before Claude Cowork, data assembly, report formatting, and the rebaseline
  when a number changes used to fill my week. Now, I have the hours back to dedicate to
  the strategic and customer-relationship work that pushes the needle."
- **Quote**: "Sales is full of people who got into the job for the customer conversations.
  Claude Cowork can give them back the hours to do just that."
- **Our assessment**: The "give back the hours" framing is a role-specific instantiation of
  the "surrounding work first" pattern from `blog-anthropic-cowork-enterprise.md` Claim 6.
  Bryant adds the normative claim: reclaimed time should go to relationship work. This is the
  sales-professional equivalent of the CTO framing in `blog-anthropic-cowork-enterprise.md`
  Claim 8 ("The human role becomes validation, refinement, and decision-making. Not
  repetitive rework."), applied to a non-executive knowledge-worker role.

## Concrete Artifacts

### Two-Tier Account Propensity Scoring Rubric (from article)

```
Travis Bryant's Cowork Account Propensity Scoring Rubric — May 2026
(Travis Bryant, Head of US Mid-Market GTM, Anthropic)

TECH ACCOUNTS — 5 Dimensions:
  1. Agent opportunity
  2. Internal transformation
  3. AI commitment
  4. White space against existing spend
  5. Industry fit

INDUSTRIES ACCOUNTS — 5 Dimensions (partial):
  1. Knowledge-worker density
  2. Public AI commitments (measured by job posting mentions)
  3-5. [Three additional dimensions not named in source article]

CALIBRATION METHODOLOGY (verbatim from article):
  "run a test territory, check the output, adjust the weights
   ('I think D4 is probably weighted a little heavy; bring it down a bit'),
   run the next territory."

DATA SOURCES: Web research + Salesforce + BigQuery
OUTPUT: Numerical score + written rationale per dimension per account
POST-PROCESSING: Interactive dashboard with pie-slice territory view;
  accounts ranked by score; rationale per dimension; hover surfaces use
  cases and comparable case studies
```

### Three-Horizon Workflow Stack (from article)

```
Travis Bryant's Claude Cowork Workflow Stack — May 2026
(Travis Bryant, Head of US Mid-Market GTM, Anthropic)

DAILY (~90 min/day saved):
  Skill 1: Conference room booking
    - Trigger: Scheduled scan of Google Calendar
    - Logic:   Books conference room for any external meeting missing one
    - Pattern: Level 3 (scheduled + automated)

  Skill 2: Customer call prep
    - Trigger: Scheduled before each customer meeting
    - Sources: BigQuery (spend data), Salesforce (pipeline status)
    - Output:  Customer brief assembled automatically
    - Pattern: Level 3 (scheduled, multi-source data pull)

WEEKLY (~3 hours/week saved):
  Skill 3: Friday forecast report
    - Trigger: Scheduled (Friday)
    - Sources: Salesforce (opportunity records, submitted commits),
               BigQuery (token spend), internal documents
    - Output:  Single-page web report — top-line metrics, top deals,
               movers and decliners, forecast snapshot rolled up from
               first-line managers
    - Format:  "the exact format Anthropic's sales leadership wants to read"
    - Pattern: Level 3 (scheduled, multi-source synthesis, formatted output)

QUARTERLY (overnight run, strategic project):
  Skill 4: Account propensity scoring
    - Trigger: On-demand (quarterly strategic project)
    - Sources: Web research + Salesforce + BigQuery
    - Scope:   4,000 accounts
    - Output:  Numerical score + written rationale per dimension per account
    - Post-processing: Interactive dashboard (built as separate Cowork step)
    - Prior state:  "hundreds of hours across RevOps, FP&A, and marketing"
    - New state:    "I did it in one night"
    - Pattern: Overnight routine (strategic project as async batch job)
    - Generalizes to: TAM sizing, account research, comp benchmarking,
      "anything historically deferred because no team had the hours for it"
```

### Sales Team Starting Point Recommendations (from "Where sales teams should start" section)

```
Travis Bryant's Sales Team Recommendations — May 2026
(from "Where sales teams should start" section)

1. Put prep on a schedule
   Rationale: "Once prep stops being a slash command I have to remember
                and starts running on its own, I stop forgetting it."
   Apply to:  Morning briefing, call prep, weekly forecast reports

2. Run big strategic projects as overnight Cowork routines
   Rationale: "The 4,000-account scoring run is the showcase example, but
                the same shape works for TAM sizing, account research,
                comp benchmarking, anything historically deferred because
                no team had the hours for it."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-cowork-enterprise.md` Claim 6 ("surrounding work first" adoption
    pattern) — Bryant's explicit description of his prior state ("data assembly, report
    formatting, and the rebaseline when a number changes used to fill my week") is a
    concrete sales-ops instantiation of the "surrounding work" category. His framing that
    Cowork returns hours to "strategic and customer-relationship work" maps directly to the
    pattern that non-engineering teams delegate peripheral tasks before core tasks.
  - `blog-anthropic-cowork-enterprise.md` Claim 9 (three workflow archetypes: data analysis,
    structured review, research aggregation) — this source introduces a fourth archetype:
    sales/account management at scale, combining data synthesis (forecast), structured output
    (scoring rubric), and analytical dashboarding (territory view).
  - `blog-anthropic-cowork-deploy-guide.md` Claim 2 (five-level maturity model) and
    Concrete Artifacts → "Five-Level Maturity Model" — Bryant's workflows are explicit Level
    3 demonstrations: scheduled skills running autonomously and pulling from multiple data
    sources, matching the Level 3 description exactly ("Skills run on their own, return
    analysis, or run daily workflows").
  - `blog-anthropic-cowork-deploy-guide.md` Claim 10 (supervised-then-scheduled autonomy
    progression) — Bryant uses the supervision-before-autonomy posture: "the human-in-the-
    loop pattern is built in so Claude proposes and I approve before anything ships." He has
    not yet removed the approval step, consistent with the documented pattern that validation
    precedes full automation.
  - `blog-anthropic-cowork-deploy-guide.md` Concrete Artifacts → "Anthropic Internal Team
    Case Studies Summary" → SALES section — that section documents Anthropic's Sales
    archetype with five skills (morning briefing, call prep, post-call follow-up, competitive
    intelligence, asset creation). This article corroborates the call prep and briefing
    patterns with first-person specifics, adds the propensity scoring use case, and
    documents particular data sources (BigQuery, Salesforce) not named in the deploy guide.

- **Contradicts**: None filed. No existing source note makes a material claim that conflicts
  with the patterns documented here. The "overnight strategic project" pattern is new but
  does not oppose any existing claim.

- **Extends**:
  - `blog-anthropic-cowork-enterprise.md` Claim 9 — extends the three documented
    non-engineering Cowork archetypes with a fourth: sales/account management at scale.
    Adds specific data source combinations (Salesforce + BigQuery + web research) and the
    overnight batch run pattern not present in the three prior archetypes.
  - `blog-anthropic-cowork-deploy-guide.md` Claim 13 (tribal knowledge codification) —
    Bryant's scoring rubric is a concrete example: the rubric dimensions (agent opportunity,
    internal transformation, AI commitment, white space against existing spend, industry fit)
    represent Bryant's accumulated practitioner judgment about what makes a good mid-market
    account — codified and now reproducible by any rep using the skill.
  - `blog-anthropic-cowork-enterprise.md` Claim 8 (human role shifts to validation,
    refinement, decision-making) — Bryant's specific framing ("I have the hours back to
    dedicate to the strategic and customer-relationship work that pushes the needle") is the
    sales-role articulation of the abstract shift described by Joel Hron.

- **Novel**:
  - **Overnight strategic project as a reusable pattern** (Claim 3 + Concrete Artifacts →
    Three-Horizon Workflow Stack → QUARTERLY section): No prior corpus source names or
    operationalizes "run big strategic projects as overnight Cowork routines." The framing
    that multi-team, multi-week strategic work can be deferred to overnight async runs is new
    to the corpus.
  - **Two-tier dimension-based scoring methodology** (Claim 4 + Concrete Artifacts → Two-
    Tier Rubric): No prior corpus source documents a specific scoring rubric structure
    (multiple segments × multiple dimensions with named weights) as a reusable template for
    account classification.
  - **Define → test → adjust → scale methodology** (Claim 5): The iterative calibration
    pattern for scoring skills (test territory → adjust weights → scale) is not described in
    any prior source note.
  - **Interface accessibility as adoption blocker/enabler** (Claim 8): The explicit first-
    person account of being blocked by Claude Code's terminal interface and enabled by
    Cowork's document-centric interface is new — prior corpus sources document non-technical
    adoption broadly but not this specific interface-as-blocker dynamic.
  - **Dashboard-from-results as skill chaining** (Claim 7): Treating post-processing of
    analytical output into an interactive dashboard as a distinct Cowork skill chained after
    the analytical scoring skill is not described in any prior source note.

## Guide Impact

- **Chapter on Enterprise & Team Adoption (Ch05/Ch06)**: Add the overnight strategic project
  pattern (Claim 3 + Three-Horizon Workflow Stack → QUARTERLY section) as a named Cowork
  use-case pattern. Frame it as: work historically requiring weeks of cross-functional effort
  (data pipelines, analyst hours, RevOps coordination) can now run overnight as a single
  Cowork skill, with results delivered before the next business morning. Bryant's 4,000-
  account scoring run is the concrete example; TAM sizing and comp benchmarking are the
  generalizations.

- **Chapter on Enterprise & Team Adoption (Ch05/Ch06)**: Add the dimension-based scoring
  methodology (Claims 4-5 + Two-Tier Rubric artifact) as a reusable template for account
  classification tasks. The tech vs. industry segmentation pattern and the define-test-
  adjust-scale calibration methodology are reproducible by any sales organization with
  similar account data.

- **Chapter on Enterprise & Team Adoption (Ch05/Ch06)**: Extend the three existing Cowork
  archetypes (data analysis, structured review, research aggregation) in
  `blog-anthropic-cowork-enterprise.md` Claim 9 with the fourth archetype: sales/account
  management at scale. Add Bryant's three-horizon workflow stack as a concrete example of
  deploying Cowork across daily, weekly, and quarterly time horizons from a single
  practitioner.

- **Chapter on Enterprise & Team Adoption / Interface-as-Adoption-Barrier**: Add the
  interface accessibility claim (Claim 8) as evidence that non-technical enterprise adoption
  requires non-CLI interfaces. A named Anthropic GTM employee explicitly could not adopt
  Claude Code due to terminal friction; Cowork's document-centric interface was the enabler.
  Pair with `blog-anthropic-cowork-enterprise.md` Claim 6 to make the complete picture:
  non-engineering teams adopt AI for surrounding work via interfaces designed for knowledge
  workers, not developers.

- **Chapter on Maturity Levels / Skill Scheduling**: Add the "scheduled over slash-command"
  principle (Claim 6) as the Level 2-to-Level-3 upgrade rationale. The "stop forgetting it"
  framing is the practitioner-accessible explanation for why Level 3 is better than Level 2
  for daily recurring workflows.

- **Chapter on Multi-Agent Patterns / Skill Chaining**: Add the "build dashboard from
  results" pattern (Claim 7) as a concrete example of skill chaining: analytical scoring
  skill → dashboard generation skill → operational tool. The pattern generalizes beyond
  sales: any analytical skill that produces structured output can be followed by a
  visualization skill.

## Extraction Notes

- **Source is a first-party practitioner case study** published on claude.com (blog),
  authored and bylined to Travis Bryant, Head of US Mid-Market GTM at Anthropic. Published
  May 20, 2026.
- **Verbatim quotes**: All quotes were verified against the source URL across three separate
  WebFetch operations with targeted prompts. The fetch model returned short verbatim
  fragments; claims were triangulated across multiple fetch responses.
- **Partial rubric**: The industry account scoring dimensions are only partially enumerated
  in the article (2 of 5 named). This is noted in the Concrete Artifacts section.
- **Time savings are self-reported**: The "~90 minutes/day" and "3 hours/week" figures are
  Bryant's own estimates, not measured against a baseline.
- **No contradictions found**: Reviewed all relevant corpus source notes
  (blog-anthropic-cowork-enterprise, blog-anthropic-cowork-deploy-guide,
  blog-anthropic-building-enterprise-agents, blog-anthropic-claude-managed-agents).
  No material contradictions identified. No contradiction issue filed.
- **Confidence calibration**: Overall anecdotal — a single named practitioner account from a
  credible first-party Anthropic source, with specific metrics that are self-reported and not
  independently validated. Individual claims rated at appropriate levels within the note.
