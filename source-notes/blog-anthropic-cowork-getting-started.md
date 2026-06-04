---
source_url: https://claude.com/blog/best-practices-for-getting-started-with-claude-cowork
source_type: blog-post
title: "Best practices for getting started with Claude Cowork"
author: Austin Lau (Growth Marketing Lead, Anthropic)
date_published: 2026-06-03
date_extracted: 2026-06-04
last_checked: 2026-06-04
status: current
confidence_overall: emerging
issue: "#1056"
---

# Best practices for getting started with Claude Cowork

> A practitioner getting-started guide from Anthropic's growth marketing lead introducing a
> five-ingredient self-assessment checklist for identifying Cowork-shaped tasks, the "output
> type" decision boundary between Chat and Cowork, and a clarification-first onboarding
> pattern — providing individual-practitioner guidance that complements the enterprise
> deployment framework in `blog-anthropic-cowork-deploy-guide.md`.

## Source Context

- **Type**: blog-post (first-party Anthropic, bylined to Austin Lau, Growth Marketing Lead at
  Anthropic; June 3, 2026 on claude.com)
- **Author credibility**: Internal Anthropic employee in a growth marketing role. Speaks from
  direct operational experience using Cowork for marketing workflows. First-person account, not
  a research report. Credible for practitioner heuristics and usage patterns; treat time
  estimates and outcome claims as directional. The post is intentionally written for individual
  non-technical users, not IT/engineering teams.
- **Scope**: Covers the Chat/Cowork/Code distinction from an individual user perspective; a
  five-ingredient checklist for identifying Cowork-shaped tasks; three concrete marketing
  workflow examples; and a five-step first-session guide. Does NOT cover: enterprise deployment
  governance, plugin architecture, maturity model, technical MCP integrations, or pricing. This
  post targets individuals deciding whether and how to start using Cowork — the onboarding
  layer below the enterprise deployment framework in `blog-anthropic-cowork-deploy-guide.md`.

## Extracted Claims

### Claim 1: The key decision boundary between Chat and Cowork is output type — thought in your head vs. deliverable you hand to someone else

- **Evidence**: Directly stated by the author as the defining mental model. Supported by the
  entire post structure, which frames Cowork around tasks that produce files, reports, or
  dashboards intended for others.
- **Confidence**: settled (first-party Anthropic framing; clear and internally consistent)
- **Quote**: "Chat is for when the output is a thought in your head, and Claude Cowork is for
  when the output is something you'll hand to someone else."
- **Our assessment**: This is the most practitioner-accessible formulation of the Chat/Cowork
  distinction in the corpus. The deploy guide (Claim 1) frames the same distinction in
  enterprise terms — workspace properties and decision criteria for IT administrators — while
  this post provides the individual user-facing formulation. The two are complementary: the
  deploy guide describes the workspace properties that differ; this post describes the output
  type that should drive the choice. The output-type framing is the right entry point for
  non-technical users who are not selecting enterprise software configurations.

### Claim 2: Cowork inverts the Chat usage model — instead of bringing work to Claude, you bring Claude to your work

- **Evidence**: Direct authorial statement introducing the Cowork concept in the opening
  paragraphs.
- **Confidence**: settled (first-party product description)
- **Quote**: "Instead of bringing your work to Claude, you bring Claude to your work. You point
  it at a folder on your computer, connect it to the apps you already use, and tell it what you
  want done."
- **Our assessment**: This inversion framing is practically useful for onboarding Chat users.
  It sets correct expectations: Cowork requires upfront setup (connecting files, apps,
  connectors) that Chat does not, but that setup enables delegation rather than conversation.
  Cowork and Code "share the same engine underneath" per the post — the surface difference is
  the workspace and the nature of the work.

### Claim 3: A five-ingredient self-assessment checklist identifies tasks that are good fits for Claude Cowork

- **Evidence**: The core framework of the post, presented as a numbered checklist with
  sub-descriptions for each ingredient. The author uses it as the organizing principle for
  evaluating her own three examples.
- **Confidence**: emerging (first-party Anthropic practitioner heuristic; prescriptive but not
  empirically validated against alternative frameworks)
- **Quote**: (no single quote captures the full checklist; see Concrete Artifacts section)
- **Our assessment**: This checklist is the primary novel contribution of this post to the
  corpus. It is simpler and more self-applicable than the enterprise deployment guide's "four
  categories of pilot-worthy use cases" (`blog-anthropic-cowork-deploy-guide.md` Claim 6) —
  each ingredient is a yes/no test an individual can apply to their own workflows without IT
  or deployment context. The five ingredients together describe an ideal shape for Cowork
  tasks: multi-source synthesis, deliverable output, recurrence, evaluability, and boring
  execution.

### Claim 4: A prerequisite for delegating a task to Cowork is the user's ability to evaluate the output in 15 seconds

- **Evidence**: Sub-description for the fourth ingredient: the specific "15 seconds" criterion
  is stated as a calibration for output familiarity.
- **Confidence**: emerging (author's stated heuristic; consistent with broader practitioner
  guidance on AI oversight)
- **Quote**: "You're familiar with the shape of the output, so you can tell in 15 seconds
  whether the output is right, wrong, or 70% there."
- **Our assessment**: This is a concrete operationalization of the human oversight prerequisite
  for AI delegation. It reformulates "you need to be able to evaluate AI output" into a
  specific performance test: can you assess this particular output in 15 seconds? Tasks where
  the user cannot quickly evaluate output quality are not good Cowork candidates by this
  framework. This is consistent with the broader corpus guidance about keeping humans in the
  loop, but stated here as a task-selection criterion rather than a governance requirement.
  The "70% there" formulation also sets a realistic bar: users do not need to verify every
  word, only recognize whether the structure and substance are on track.

### Claim 5: Recurring tasks with boring middle steps are the sweet spot for Cowork automation

- **Evidence**: Two of the five ingredients describe this: "You'll do it again" and "The
  middle is the boring part."
- **Confidence**: emerging (first-party practitioner heuristic; consistent with Cowork usage
  patterns documented in the corpus)
- **Quote**: "One-offs are fine, but recurring tasks are the sweet spot. You can schedule them
  to run before you're even at your desk."
- **Quote**: "The thinking lives at the start (deciding what you want) and the end (deciding
  if it's right)."
- **Our assessment**: The recurrence criterion maps directly to Level 3 in the deploy guide's
  maturity model (`blog-anthropic-cowork-deploy-guide.md` Claim 2 + Artifact: Level 3 is
  "Skills run on their own, return analysis, or run daily workflows"). The "boring middle"
  formulation is a useful task-selection heuristic: the test is not "is this task complex?"
  but "is the execution between the start and end mechanical?" Legal review, data
  reconciliation, and briefing generation all have complex inputs and outputs but mechanical
  middle steps — which is exactly the Cowork pattern.

### Claim 6: The optimal first-session technique is a clarification-first prompt that asks Claude to confirm the ask and surface questions before beginning

- **Evidence**: Step 5 of the "Your first 10 minutes" sequence. Author provides a specific
  prompt string.
- **Confidence**: emerging (author's recommended technique; no comparative evidence)
- **Quote**: "Before we begin, repeat my ask back to me so we're aligned, then ask me as many
  clarifying questions as you have."
- **Our assessment**: This is the most concrete onboarding technique in the post. It addresses
  a specific first-session failure mode: Claude proceeding on an ambiguous brief and producing
  output the user didn't want. The two-step structure — confirm understanding, then surface
  questions — ensures both alignment and completeness before any work starts. This pattern
  generalizes beyond first sessions; it is good practice for any Cowork task where output
  requirements are complex or partially specified. No prior corpus source provides a specific
  prompt string for clarification-first task initiation.

### Claim 7: Starting with a familiar task accelerates first-session learning because evaluation ability is highest for work you already do

- **Evidence**: Step 4 of the "Your first 10 minutes" section.
- **Confidence**: emerging (author recommendation; logically consistent with the evaluation
  prerequisite in Claim 4)
- **Quote**: "Start with a real task you know well. You'll see immediately where it's strong,
  where it needs context from you, and you already know what 'good' looks like for it."
- **Our assessment**: This guidance is the flip side of the evaluation prerequisite (Claim 4):
  not only must you be able to evaluate output, but first-session tasks should be specifically
  chosen for existing evaluation ability. The "you'll see immediately where it's strong"
  framing is practical — a familiar task exposes gaps in Claude's context, prompting the user
  to add connectors, files, or instructions and building the workflow incrementally. This is
  the individual-level analog to the deploy guide's cold-start solution (`blog-anthropic-
  cowork-deploy-guide.md` Claim 7: pre-configured plugins delivering value in 90 seconds).
  The difference: the deploy guide solves cold-start top-down via pre-built plugins; this post
  solves it bottom-up via starting with a known task.

### Claim 8: Practitioners should learn patterns from examples rather than copying specific workflows

- **Evidence**: Explicit authorial instruction in the "How I use Claude Cowork at Anthropic"
  section, before presenting her three examples.
- **Confidence**: anecdotal (author's stated pedagogical preference; no comparative evidence)
- **Quote**: "Don't read these looking for a workflow to copy—that's not going to be helpful in
  the long run. Watch how each one hits a few items from the checklist above, because that's
  the pattern you'll be looking for in your own Claude Cowork workflows."
- **Our assessment**: This is a meta-claim about adoption pedagogy: case study examples should
  teach pattern recognition, not template replication. The author explicitly anticipates and
  deflects the natural reader response (copy what the author does) and redirects toward the
  five-ingredient checklist as the durable learning tool. This is practically important for
  the guide: when presenting Cowork case studies, the guide should follow the same principle —
  annotate examples against the checklist criteria, not present them as templates.

### Claim 9: Chat remains the right tool for exploratory conversations and idea pressure-testing even for regular Cowork users

- **Evidence**: The "When I still reach for chat" section, where the author (a regular Cowork
  user) describes her continuing Chat use cases.
- **Confidence**: emerging (first-party Anthropic framing; consistent with the three-surface
  decision model across the corpus)
- **Quote**: "I still use chat extensively to talk through a positioning problem, pressure-test
  an idea before I commit to it, or to ask random questions."
- **Our assessment**: This claim prevents the misreading that Cowork replaces Chat. The
  output-type distinction (Claim 1) makes the same point structurally; this claim makes it
  concrete from a regular Cowork user's perspective: positioning discussions, idea iteration,
  and open-ended exploration are Chat use cases, not Cowork use cases. The guide should
  present Chat and Cowork as complementary tools used by the same people — not competing tools
  for different audiences.

### Claim 10: A growth marketing practitioner's three recurring Cowork workflows illustrate the five-ingredient pattern across daily briefings, budget pacing, and scheduled reporting

- **Evidence**: Three specific workflows from Austin Lau's daily practice with data sources,
  output types, and recurrence patterns described.
- **Confidence**: anecdotal (single practitioner account; first-party but reflects one person's
  usage from a marketing function)
- **Quote**: "I manage growth marketing at Anthropic, so my examples are marketing-flavored.
  Don't read these looking for a workflow to copy—that's not going to be helpful in the long
  run."
- **Our assessment**: The three workflows are not claim-making — they illustrate the checklist
  in practice. Daily briefing (Slack + Gmail → sorted report) demonstrates multi-source input,
  file out, recurring. Budget pacing (Google Ads + Meta Ads → live HTML dashboard) demonstrates
  automated multi-platform data reconciliation. Reporting (Google Search Console → single
  reconciled sheet weekly) demonstrates boring-middle elimination for repetitive data export.
  The Prospector's third triage comment correctly noted that these examples add practitioner
  color to existing Cowork patterns without providing the implementation depth of higher-value
  case studies. Their value is as checklist illustrations, not standalone workflow descriptions.

## Concrete Artifacts

### Five-Ingredient Cowork Task Checklist (from post)

```
Five ingredients of a Claude Cowork-shaped task
(Austin Lau, Growth Marketing Lead, Anthropic — June 3, 2026)

1. More than one thing goes in
   "Multiple files, a whole folder, or a file plus some connectors."

2. A file comes out
   "You need a deliverable that you can attach, present, share, or repurpose:
    a doc, a deck, a spreadsheet, or a CSV."

3. You'll do it again
   "One-offs are fine, but recurring tasks are the sweet spot. You can schedule
    them to run before you're even at your desk."

4. You already know what good looks like
   "You're familiar with the shape of the output, so you can tell in 15 seconds
    whether the output is right, wrong, or 70% there."

5. The middle is the boring part
   "The thinking lives at the start (deciding what you want) and the end
    (deciding if it's right)."
```

### First 10 Minutes Getting-Started Sequence (from post)

```
Your first 10 minutes with Claude Cowork
(Austin Lau, Growth Marketing Lead, Anthropic — June 3, 2026)

Step 1: Open the Claude desktop app and switch to the Claude Cowork tab.

Step 2: Give Claude something to work with.
  "Drop in a few files, point it at a folder on your computer, or connect an
   app you frequently use..."

Step 3: Tell Claude the outcome you want.
  Describe the deliverable you want at the end and provide any necessary context.

Step 4: Start with a real task you know well.
  "You'll see immediately where it's strong, where it needs context from you,
   and you already know what 'good' looks like for it."

Step 5: Make Claude ask clarifying questions first.
  Prompt: "Before we begin, repeat my ask back to me so we're aligned, then ask
           me as many clarifying questions as you have."
```

### Three Marketing Workflow Illustrations (from "How I use Claude Cowork at Anthropic")

```
Austin Lau's Cowork Workflows — Growth Marketing at Anthropic
(Austin Lau, Growth Marketing Lead, Anthropic — June 3, 2026)

DAILY BRIEFING:
  Connections: Slack + Gmail
  Task: "review my unread emails and the channels I care about, sort them into
         buckets, and produce a short report"
  Output: Sorted report with TLDR, flagged emails, incident alerts
  Checklist fit: Multiple inputs (Slack + Gmail), file out (report),
                 recurring (daily), boring middle (read/sort/format)

BUDGET PACING:
  Connections: Google Ads + Meta Ads
  Task: "create a live artifact (basically an HTML dashboard) in the desktop app
         that automatically pulls in my daily spend and calculates pacing"
  Output: Live HTML dashboard with daily spend and pacing metrics
  Checklist fit: Multiple inputs (two ad platforms), file out (HTML dashboard),
                 recurring (daily), boring middle (data extraction + calculation)

REPORTING (Google Search Console):
  Connections: Google Search Console
  Task: "It pulls what I care about (queries, countries, pages) and reconciles
         it into a single sheet, instead of Google's default of one CSV per
         dimension when you export data manually."
  Output: Single reconciled weekly sheet with comparison analysis and flags
  Checklist fit: Multiple inputs (three dimension CSVs), file out (single sheet),
                 recurring (weekly), boring middle (data reconciliation)
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-cowork-deploy-guide.md` Claim 1 (Chat/Cowork/Code three-surface decision
    framework): the output-type framing here ("thought in your head vs. something you'll hand
    to someone else") is an individual-user articulation of the same framework the deploy guide
    presents for enterprise deployment. Both are first-party Anthropic and agree on the core
    distinction; this post adds the more accessible practitioner formulation.
  - `blog-anthropic-cowork-deploy-guide.md` Claim 6 (four categories of pilot-worthy use
    cases): the five-ingredient checklist here is a simplified individual-level self-assessment
    version of the same concept. The deploy guide describes enterprise pilot categories; this
    post describes individual task criteria. Both identify recurring tasks and information
    synthesis as core Cowork patterns.
  - `blog-anthropic-cowork-enterprise.md` Claim 6 ("surrounding work first" adoption pattern):
    all three of Lau's workflow examples (briefing, budget pacing, reporting) are "surrounding
    work" — peripheral data-assembly and formatting tasks adjacent to core marketing strategy,
    not core marketing work itself. Consistent with the observation that non-engineering teams
    adopt AI for peripheral tasks first.
  - `blog-anthropic-bryant-cowork-sales.md` Claim 6 (scheduled skills more reliable than
    slash-commands): the "recurring tasks are the sweet spot, you can schedule them to run
    before you're even at your desk" in Claim 5 above corroborates Bryant's "once prep stops
    being a slash command I have to remember and starts running on its own, I stop forgetting
    it." Both sources independently recommend scheduling over on-demand invocation for
    recurring workflows.

- **Contradicts**: None. The deploy guide and this post use different framings for Chat vs.
  Cowork (enterprise workspace properties vs. individual output type) but these are
  complementary perspectives on the same decision, not opposing claims. No contradiction
  issue filed.

- **Extends**:
  - `blog-anthropic-cowork-deploy-guide.md`: that guide covers enterprise adoption strategy
    (maturity model, deployment roadmap, plugin architecture, governance). This post covers
    individual practitioner getting-started guidance. Together they form a complete picture:
    the deploy guide tells teams how to roll out Cowork organizationally; this post tells
    individuals how to pick their first task and run their first session.
  - `blog-anthropic-cowork-deploy-guide.md` Claim 7 (cold-start problem): the deploy guide
    identifies cold-start as a deployment risk solved at the enterprise level by pre-configured
    plugins. This post provides the individual-level complement: start with a familiar task and
    use the clarification-first prompt so the first session produces something recognizably
    valuable, without requiring pre-built plugins.

- **Novel** (not in prior corpus):
  - **Five-ingredient self-assessment checklist** (Claim 3 + Concrete Artifacts): the specific
    individual-user checklist for identifying Cowork-shaped tasks is not in any prior source
    note. The deploy guide provides enterprise pilot categories; this is the personal task
    filter for individual adoption.
  - **Evaluation-in-15-seconds prerequisite** (Claim 4): the explicit operationalization of
    output familiarity ("tell in 15 seconds whether the output is right, wrong, or 70% there")
    as a task-selection criterion is new to the corpus.
  - **Clarification-first prompt pattern** (Claim 6): the specific two-step prompt string
    ("repeat my ask back to me so we're aligned, then ask me as many clarifying questions as
    you have") as a first-session technique is not described in any prior source note.
  - **Anti-copy teaching principle** (Claim 8): the explicit instruction to learn patterns
    from examples rather than copying specific workflows is new to the corpus.
  - **Chat as pressure-testing tool for active Cowork users** (Claim 9): the concrete
    description of Chat's continuing role (positioning discussions, idea testing, random
    questions) from the perspective of a regular Cowork practitioner is new — prior corpus
    sources describe Chat and Cowork separately, not from an active Cowork user's combined
    workflow perspective.

## Guide Impact

- **Chapter on Individual Adoption / Getting Started (Ch02 or Ch04)**: Add the five-ingredient
  checklist (Claim 3 + Artifact) as the recommended self-assessment tool for individuals
  identifying their first Cowork tasks. Frame it as the individual-level complement to the
  enterprise pilot categories in `blog-anthropic-cowork-deploy-guide.md` Claim 6. The
  checklist is the right entry point for non-technical readers who need a quick personal
  filter, not a deployment framework.

- **Chapter on Individual Adoption / Getting Started**: Add the evaluation-in-15-seconds
  prerequisite (Claim 4) as a selection criterion alongside the checklist. Explicitly note:
  tasks where the user cannot quickly evaluate output quality are not good Cowork candidates —
  delegate only what you can check in seconds.

- **Chapter on Individual Adoption / Getting Started**: Add the clarification-first prompt
  pattern (Claim 6) as a recommended first-session technique. The specific prompt string
  ("Before we begin, repeat my ask back to me so we're aligned, then ask me as many
  clarifying questions as you have") is concrete enough to quote directly in the guide.

- **Chapter on Chat vs. Cowork vs. Code (wherever the three-surface decision appears)**: Add
  the output-type framing (Claim 1: "thought in your head vs. something you'll hand to
  someone") alongside the enterprise workspace framing from the deploy guide. The two framings
  serve different audiences; the guide should include both, noting that Chat and Cowork are
  complementary tools for the same users (Claim 9).

- **Chapter on Individual Adoption / Case Studies**: When presenting the three marketing
  workflow examples (Claim 10 + Artifact) to illustrate the checklist, follow the anti-copy
  principle (Claim 8): annotate each example against the checklist criteria rather than
  presenting it as a template. The guide should make explicit which ingredients each example
  satisfies.

## Extraction Notes

- **Source is a first-party Anthropic practitioner post**, bylined to Austin Lau (Growth
  Marketing Lead), published June 3, 2026 on claude.com. The post is approximately 1,000 words
  and was fully read across multiple WebFetch calls.
- **WebFetch returned summaries, not full verbatim text** due to copyright constraints. All
  quotes were obtained through multiple targeted WebFetch calls requesting specific passages by
  section and topic. Each quote was cross-confirmed across at least two fetch responses. The
  fetch model was consistent in returning the same specific phrases across independent requests,
  increasing confidence in accuracy.
- **Three Prospector triage comments**: Three separate triage comments were filed on the issue,
  with novelty rated high, medium, and low respectively. The convergence across comments
  consistently identified: (1) the five-ingredient checklist, (2) the output-type mental model,
  (3) the clarification-first onboarding pattern, and (4) the marketing use-case examples as
  the primary extraction targets.
- **No sub-pages followed**: The post contains no substantive links to sub-pages. The linked
  Claude desktop app download page and Cowork overview page were not followed (marketing/product
  pages with no extractable claims).
- **No contradictions found**: Reviewed CONTRADICTIONS.md (three entries; none related to
  Cowork getting-started guidance). Reviewed all overlapping source notes (deploy-guide,
  enterprise, bryant-cowork-sales). No claims in this post materially oppose any existing
  source note claim. No contradiction issue filed.
- **Confidence calibration**: Overall **emerging** — first-party Anthropic from a named
  practitioner, but the claims are prescriptive heuristics rather than empirically validated
  frameworks. The five-ingredient checklist and onboarding steps are specific and actionable
  but not tested against alternatives.
