---
source_url: https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale
source_type: blog-post
title: "How Anthropic's business development team uses Claude to run inbound and outbound at scale"
author: John Albert (Business Development Representative, Anthropic)
date_published: 2026-08-07
date_extracted: 2026-08-11
last_checked: 2026-08-11
status: current
confidence_overall: anecdotal
issue: "#2620"
---

# How Anthropic's business development team uses Claude to run inbound and outbound at scale

> First-party Anthropic practitioner case study documenting a named BDR's individual-
> contributor-level Cowork workflows — an hourly knowledge-base-grounded inbox skill, an
> overnight 100+-account prospecting skill wired to Salesforce/Apollo/Common Room/Gong/data
> warehouse, a Gong-transcript discovery-call coach, and an explicit feedback-loop and
> plugin-promotion governance model — extending the sales archetype documented in
> `blog-anthropic-bryant-cowork-sales.md` and `blog-anthropic-cowork-deploy-guide.md` down
> to the individual-BDR, inbound-heavy layer of a sales org.

## Source Context

- **Type**: blog-post (first-party Anthropic practitioner case study, claude.com/blog;
  published August 7, 2026)
- **Author credibility**: Bylined to John Albert, a business development representative at
  Anthropic, describing his own daily workflow with his employer's own product. High
  credibility for what the workflows do structurally (skill triggers, data sources, review
  gates); the time-savings framing ("5 hours per day" of manual inbox work before
  automation) is self-reported and not independently measured. No third-party
  corroboration. Clear incentive to present Cowork favorably.
- **Scope**: Covers Albert's inbound inbox automation, an overnight outbound prospecting
  skill, administrative skills (no-show/disengagement tracking, Salesforce hygiene), a
  discovery-call coaching skill, ad-hoc analytics requests, and a closing four-item advice
  list. Does NOT cover: pricing, the technical configuration of the Salesforce/Apollo/Common
  Room/Gong/data-warehouse connectors, the literal skill/plugin file contents, team size, or
  how the workflows were rolled out to the rest of the BD org.

## Extracted Claims

### Claim 1: Manual inbound inbox management consumed roughly 5 hours per day before the team automated it with a knowledge-base-grounded skill

- **Evidence**: Albert states he personally managed the sales inbox and quantifies the time
  spent before automation.
- **Confidence**: anecdotal (single practitioner, self-reported time estimate)
- **Quote**: "When I joined Anthropic last summer, I took over the responsibility of
  managing our sales inbox. I would spend around 5 hours per day manually responding to
  inbound interest from prospects, often answering the same or similar questions about our
  products, on top of managing my own book of business."
- **Our assessment**: This is the clearest "surrounding work first" data point yet at the
  individual-contributor level — corroborates the same adoption pattern Travis Bryant
  describes at the GTM-leadership level in `blog-anthropic-bryant-cowork-sales.md` Claim 10
  ("data assembly, report formatting... used to fill my week"), but here the surrounding
  work is inbox triage rather than reporting. The 5-hour figure is a specific, testable
  claim about a single role, not a productivity benchmark for BD generally.

### Claim 2: A shared FAQ knowledge base, built before any automation, is the foundation the inbox skill and other workflows draw on

- **Evidence**: Albert describes compiling commonly-received sales-inbox questions and
  answers into a single document that grounds the inbox skill's drafts.
- **Confidence**: anecdotal (single practitioner's build order)
- **Quote**: "A foundational piece of our inbound setup is a document where I've collected
  the questions we most commonly receive in our sales inbox, along with our best answers to
  those questions."
- **Our assessment**: This is a concrete instance of the "knowledge base before workflows"
  sequencing that Claim 9 (below) states explicitly as prescriptive advice. It's also a
  specific example of the tribal-knowledge-codification pattern in
  `blog-anthropic-cowork-deploy-guide.md` Claim 13 (encoding expert answers as organizational
  infrastructure) — here the "expert" is Albert's own accumulated FAQ knowledge rather than
  a formal playbook.

### Claim 3: An hourly-scheduled inbox skill scans for unanswered threads and drafts replies grounded in the FAQ document and each rep's individual writing style

- **Evidence**: Albert describes the skill's trigger (hourly schedule), its scope (every
  thread needing a reply), and its personalization mechanism (per-rep writing-style
  learning).
- **Confidence**: anecdotal (single practitioner + team-level description)
- **Quote**: "The heaviest workflow built on that document is an inbox skill that runs
  every hour: it scans a rep's inbox, finds every thread that the rep needs to answer, and
  drafts a reply for the rep to read, edit, and send."
- **Quote**: "Each rep can also have Claude learn their writing style, so drafts arrive
  sounding like the sender."
- **Our assessment**: The combination of (a) a shared knowledge base and (b) a per-individual
  writing-style layer is a distinct two-tier context architecture — shared factual grounding
  plus personal voice — not previously documented this explicitly in the corpus's sales
  case studies. `blog-anthropic-bryant-cowork-sales.md` describes scheduled skills pulling
  from shared data sources (Salesforce, BigQuery) but does not describe a per-individual
  style/voice context layer.

### Claim 4: An overnight scheduled skill prospects across a 100+-account book by connecting to Salesforce, Apollo, Common Room, Gong, and the data warehouse, validating findings against curated outbound guidance and ICP criteria

- **Evidence**: Albert describes the trigger (scheduled overnight task), the scope (his
  entire book, "upwards of a hundred accounts"), the specific systems it connects to, and
  the validation step against team-curated criteria.
- **Confidence**: anecdotal (single practitioner)
- **Quote**: "On average, I work upwards of a hundred accounts at any given time. I'm able
  to cover all these accounts thanks to a skill that runs as a scheduled task overnight. It
  prospects across my entire book, observing the current state of each account; for
  example, who are we in touch with, how do they use Claude today, and what signals are
  relevant. To accomplish this, Claude connects to Salesforce, sales tools like Apollo and
  Common Room, Gong, and our data warehouse, performs deep research, and validates it
  against outbound guidance and ICP criteria that our team has curated."
- **Our assessment**: This is the overnight-scheduled-scoring pattern from
  `blog-anthropic-bryant-cowork-sales.md` Claim 3 (4,000-account propensity scoring
  overnight), reproduced at a smaller, individual-BDR scale (100+ accounts) with a
  different and more specific tool stack. Apollo and Common Room are named integrations not
  present in any prior corpus source note — both are sales-intelligence/prospecting tools,
  distinct from the Salesforce+BigQuery combination Bryant describes. This is the strongest
  novel-artifact evidence in this source: a concrete five-system connector stack
  (Salesforce, Apollo, Common Room, Gong, data warehouse) for one skill.

### Claim 5: A Gong-transcript discovery-call coaching skill scores calls against a team playbook with a written scorecard and explicit pass/fail assessments

- **Evidence**: Albert describes a skill that evaluates recorded discovery calls against a
  documented playbook.
- **Confidence**: anecdotal (single practitioner description of a team-shared skill)
- **Quote**: "We use a skill that evaluates Gong transcripts against our discovery call
  playbook and builds a scorecard for each call, with specific feedback based on the
  conversation."
- **Our assessment**: Novel to the corpus — no prior source note documents a call-coaching
  skill with explicit pass/fail scorecard output. It's a specific instance of using Claude
  as an evaluator against a codified rubric (playbook), structurally similar to the
  dimension-based account scoring rubric in `blog-anthropic-bryant-cowork-sales.md` Claim 4,
  but applied to call performance rather than account propensity.

### Claim 6: Administrative skills track meeting no-shows and prospect disengagement via Gmail/Calendar monitoring, and cross-check Salesforce opportunity-stage accuracy against actual Gmail and Gong activity

- **Evidence**: Albert describes two distinct administrative skills: one that watches for
  no-shows/disengagement, another that audits Salesforce hygiene against real activity.
- **Confidence**: anecdotal (single practitioner/team description)
- **Quote**: "Every BDR knows the pain of meeting no-shows and prospects going dark. To
  address this, I built a skill that watches Gmail and Google Calendar to notify me when
  that happens, so I can follow up quickly."
- **Quote**: "We also have a skill that keeps Salesforce current by reading our internal
  guidance on opportunity stages and checking it against what's actually happening in Gmail
  and Gong."
- **Our assessment**: The Salesforce-hygiene-auditing pattern corroborates
  `blog-anthropic-cowork-deploy-guide.md` Concrete Artifacts → Anthropic Internal Team Case
  Studies Summary → SALES section, which describes "one rep built supervised Salesforce
  auto-update; after validation confirmed accuracy, removed supervision." This source adds
  the specific cross-check logic (comparing stated opportunity stage guidance against Gmail
  and Gong activity) that the deploy guide does not spell out.

### Claim 7: Ad-hoc analytics requests surface accounts with usage signals but no open sales opportunity ("undiscovered usage"), and generate on-demand spend-trend dashboards and webinar-eligible prospect lists

- **Evidence**: Albert describes three distinct ad-hoc analytical requests: undiscovered
  usage detection, spend dashboards, and ICP-scored webinar invite lists.
- **Confidence**: anecdotal (single practitioner)
- **Quote**: "One of my favorite workflows is running an undiscovered usage prompt. It
  considers an AE's full book and finds usage signals on the account level where we do not
  yet have a sales opportunity."
- **Quote**: "If an AE is curious about usage trends for a top account, we are a prompt away
  from providing a legible and descriptive dashboard that highlights the relevant trends."
- **Quote**: "Claude checked usage data and CRM history across the book, scored each account
  against our ICP, and flagged the best fits with contacts worth inviting."
- **Our assessment**: These are on-demand (not scheduled) analytical requests, distinct from
  the scheduled skills described in Claims 3-6. They demonstrate the same
  data-synthesis-into-dashboard pattern as `blog-anthropic-bryant-cowork-sales.md` Claim 7
  (dashboard built from propensity-scoring results), but here the dashboard generation is
  itself ad hoc rather than a fixed post-processing step after a named scheduled skill.

### Claim 8: Corrections and dismissed drafts should be written back into the skill's own instructions so it doesn't repeat the same mistake

- **Evidence**: Stated as prescriptive advice in the article's closing recommendations.
- **Confidence**: anecdotal (author's own practice, offered as generalizable advice)
- **Quote**: "Write feedback back into the skills. When you dismiss a hook or correct a
  draft, have Claude record the reason in the skill so it doesn't make the same mistake
  again."
- **Our assessment**: This is a specific, actionable feedback-loop mechanism not previously
  documented this explicitly in the corpus's Cowork/sales case studies — it names the
  concrete action (recording the rejection *reason*, not just re-running with a corrected
  output) and ties it to skill-file persistence rather than one-off prompt correction. This
  is a good candidate for a general harness-engineering pattern (self-correcting skill
  instructions), not just a sales-specific tip.

### Claim 9: Team advice prescribes building the knowledge base before workflows, keeping a human on every send, promoting skills to a shared plugin only after individual reps use them consistently, and keeping shared skills general rather than scoped to one person's routine

- **Evidence**: Stated as the article's closing prescriptive advice, in four distinct
  points.
- **Confidence**: anecdotal (author/team's own practice, offered as generalizable advice)
- **Quote**: "Build the knowledge base before the workflows. Collect the questions your team
  answers repeatedly, and your best answers, into a single external-facing document."
- **Quote**: "Keep a person on every send. Claude can generate drafts, but we still read,
  edit, and send them."
- **Quote**: "Our team keeps its most-used skills in a shared plugin, promoting a skill
  there once we establish that reps use it consistently in their daily work."
- **Quote**: "We keep shared skills general enough to adapt rather than scoped to one
  person's routine."
- **Our assessment**: The "human on every send" point corroborates the human-in-the-loop
  approval posture in `blog-anthropic-bryant-cowork-sales.md` Claim 9 ("Claude proposes and
  I approve before anything ships") — same posture, applied to individual-rep-level
  outbound communication rather than leadership-facing reports. The plugin-promotion rule
  ("once we establish reps use it consistently") is a specific, previously undocumented
  governance criterion — it's more concrete than the "champion-authored skills" leading
  indicator in `blog-anthropic-cowork-deploy-guide.md` Claim 9, which flags skill authorship
  itself as the signal; this source adds a second-order bar (consistent *usage*, not just
  authorship, before a skill graduates to the shared plugin).

## Concrete Artifacts

### John Albert's BD Skill Stack (from article)

```
John Albert, Business Development Representative, Anthropic — August 2026

INBOUND (hourly + on-demand):
  Skill 1: Inbox skill
    - Trigger: Scheduled, every hour
    - Sources:  Shared FAQ knowledge base + per-rep writing-style profile
    - Logic:    Scans rep's inbox, finds every thread needing a reply, drafts response
    - Output:   Draft for rep to read, edit, and send (human-in-the-loop)

  Skill 2: No-show / disengagement tracker
    - Trigger: Watches Gmail + Google Calendar
    - Logic:    Notifies rep when a meeting no-show or prospect-gone-dark occurs
    - Output:   Follow-up prompt

  Skill 3: Salesforce hygiene auditor
    - Sources:  Internal opportunity-stage guidance vs. actual Gmail + Gong activity
    - Logic:    Flags mismatches between recorded stage and real activity
    - Output:   Salesforce currency/accuracy corrections

OUTBOUND (overnight):
  Skill 4: Overnight prospecting skill
    - Trigger: Scheduled task, overnight
    - Scope:   100+ accounts ("upwards of a hundred accounts at any given time")
    - Sources:  Salesforce, Apollo, Common Room, Gong, internal data warehouse
    - Logic:    Deep research per account; validates against curated outbound
                guidance and ICP criteria
    - Output:   Account state, signals, recommended outreach plays

COACHING:
  Skill 5: Discovery call coach
    - Sources:  Gong call transcripts + team discovery-call playbook
    - Output:   Per-call scorecard with specific feedback and pass/fail assessment

AD-HOC ANALYTICS (on demand, not scheduled):
  Request A: Undiscovered usage — finds account-level usage signals with no open
             sales opportunity, across an AE's full book
  Request B: Spend-trend dashboard — on-demand descriptive dashboard of usage
             trends for a given account
  Request C: Webinar-eligible prospects — scores accounts against ICP using usage
             data + CRM history, flags best-fit invite contacts
```

### Governance / Advice List (verbatim, from closing section)

```
John Albert's closing advice, "How Anthropic's business development team uses
Claude..." (claude.com/blog, Aug 2026):

1. "Build the knowledge base before the workflows. Collect the questions your
    team answers repeatedly, and your best answers, into a single
    external-facing document."
2. "Keep a person on every send. Claude can generate drafts, but we still
    read, edit, and send them."
3. "Write feedback back into the skills. When you dismiss a hook or correct
    a draft, have Claude record the reason in the skill so it doesn't make
    the same mistake again."
4. Plugin promotion rule: "Our team keeps its most-used skills in a shared
    plugin, promoting a skill there once we establish that reps use it
    consistently in their daily work." Shared skills are kept "general
    enough to adapt rather than scoped to one person's routine."

Closing line: "My best advice? Just start experimenting. The more context
and tools you give it, the more you can get done."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-bryant-cowork-sales.md` Claim 9 (human-in-the-loop approval before
    anything ships) — Claim 9 of this note ("Keep a person on every send") is the same
    posture applied to individual-rep outbound communication.
  - `blog-anthropic-bryant-cowork-sales.md` Claim 3 (overnight scheduled skill for
    large-scale account work) — Claim 4 of this note (overnight 100+-account prospecting
    skill) reproduces the same overnight-batch pattern at individual-BDR scale.
  - `blog-anthropic-bryant-cowork-sales.md` Claim 10 ("surrounding work first" — reclaiming
    hours from mechanical data/report tasks) — Claim 1 of this note (5 hours/day on manual
    inbox triage before automation) is the individual-contributor instance of the same
    adoption pattern.
  - `blog-anthropic-cowork-deploy-guide.md` Concrete Artifacts → Anthropic Internal Team
    Case Studies Summary → SALES section (Salesforce auto-update skill, supervised then
    unsupervised) — Claim 6 of this note (Salesforce hygiene auditor comparing stated stage
    against Gmail/Gong activity) is a more detailed account of the same skill category.

- **Contradicts**: None filed. No existing source note makes a claim that materially
  conflicts with the patterns documented here.

- **Extends**:
  - `blog-anthropic-bryant-cowork-sales.md` — extends the sales/account-management Cowork
    archetype down from GTM leadership (4,000-account propensity scoring, weekly forecast
    reports) to the individual BDR layer (inbound inbox triage, 100+-account prospecting,
    call coaching). Different tool stack (Apollo, Common Room, Gong vs. BigQuery) and a
    different primary workload (inbound response vs. outbound account scoring).
  - `blog-anthropic-cowork-deploy-guide.md` Claim 13 (tribal knowledge codification) —
    Claim 2 of this note (shared FAQ knowledge base as the foundation for the inbox skill)
    is a concrete instance of codifying one BDR's accumulated Q&A knowledge into shared
    infrastructure.
  - `blog-anthropic-cowork-deploy-guide.md` Claim 9 (champion-authored skills as the leading
    scale-phase indicator) — Claim 9 of this note adds a second-order governance bar:
    skills are promoted to the shared plugin only after *consistent use*, not merely after
    being authored by a champion.

- **Novel**:
  - **Named tool stack for outbound prospecting** (Claim 4): Apollo and Common Room as
    named sales-intelligence connectors are new to the corpus; no prior source note
    documents these tools.
  - **Discovery-call coaching skill with pass/fail scorecards** (Claim 5): Not previously
    documented in the corpus.
  - **Per-rep writing-style context layer** (Claim 3): A distinct personal-voice context
    layer alongside a shared knowledge base is new to the corpus's sales case studies.
  - **Explicit feedback-loop mechanism — recording rejection reasons in the skill itself**
    (Claim 8): New to the corpus as a named, generalizable harness-engineering pattern.
  - **Plugin-promotion governance rule based on consistent usage** (Claim 9): A more
    concrete graduation criterion than any prior source note's plugin-scaling guidance.

## Guide Impact

- **Chapter on Enterprise & Team Adoption (Ch05/Ch06)**: Add John Albert's individual-BDR
  workflow stack (Concrete Artifacts → BD Skill Stack) as a second, individual-contributor
  data point for the sales/account-management Cowork archetype, alongside
  `blog-anthropic-bryant-cowork-sales.md`'s GTM-leadership example. Note the specific tool
  stack difference (Apollo, Common Room, Gong vs. Salesforce+BigQuery) so the guide doesn't
  present a single canonical sales connector set.

- **Chapter on Harness Engineering / Feedback Loops (Ch02)**: Add the "write feedback back
  into the skill" mechanism (Claim 8) as a concrete, generalizable pattern for
  self-correcting skills: when a human dismisses or corrects Claude's output, the
  *reason* — not just the corrected output — gets recorded into the skill's own
  instructions so future runs avoid the same mistake.

- **Chapter on Enterprise & Team Adoption / Plugin Governance (Ch05/Ch06)**: Add the
  consistent-usage promotion criterion (Claim 9) as a refinement to the champion-authored-
  skills scaling indicator in `blog-anthropic-cowork-deploy-guide.md` Claim 9 — authorship
  alone isn't the bar; sustained individual use before promotion to a shared plugin is.

## Extraction Notes

- Fetched via three separate WebFetch passes with targeted prompts (summary pass, then two
  verbatim-quote-extraction passes) because the first pass returned only a condensed
  summary rather than exact wording. All quotes in this note were cross-checked across the
  verbatim-focused fetches for consistency; no quote in this note came from the summary-only
  pass.
- The article does not name specific dollar figures, percentages, or a headcount for the BD
  team — the only concrete numbers given are "5 hours per day" (pre-automation inbox time)
  and "upwards of a hundred accounts" (book size). This is noted so the guide doesn't
  over-claim precision the source doesn't provide.
- No sub-pages were linked from the article body to follow.
- Checked all sales/Cowork-adjacent source notes for contradictions
  (`blog-anthropic-bryant-cowork-sales.md`, `blog-anthropic-cowork-deploy-guide.md`,
  `blog-anthropic-cowork-marketing-ops.md`, `blog-anthropic-cowork-enterprise.md`,
  `blog-anthropic-cowork-usage-taxonomy.md`). No material contradictions found; no
  contradiction issue filed.
