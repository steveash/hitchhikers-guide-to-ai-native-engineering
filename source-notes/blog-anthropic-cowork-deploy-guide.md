---
source_url: https://claude.com/blog/new-guide-deploying-claude-across-the-enterprise-with-claude-cowork
source_type: blog-post
title: "Deploying Claude across the enterprise with Claude Cowork (Practitioner Guide)"
author: Anthropic
date_published: 2026-04-29
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#464"
---

# Deploying Claude across the enterprise with Claude Cowork (Practitioner Guide)

> A 24-page Anthropic-authored deployment guide (accompanying a short April 29 blog post)
> that introduces a five-level maturity model for Claude Cowork adoption, a three-phase
> six-month deployment roadmap, a plugin architecture (Skills + Subagents + Connectors in
> markdown), and four detailed internal Anthropic team case studies (Finance, Legal, Sales,
> Product) — the most operationally specific enterprise deployment guidance Anthropic has
> published for non-engineering knowledge workers.

## Source Context

- **Type**: blog-post + linked PDF guide (24 pages). The blog post at the source URL is ~400
  words and serves as an introduction; the substantive content is in the downloadable guide
  at `https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/69f24d3e09b921b92403774e_Claude-Deploying-Claude-Across-Your-Organization-04292026.pdf`
  (title: "Deploying Claude across your organization: How Anthropic uses Claude Cowork").
  Both were fully read for this extraction.
- **Author credibility**: First-party Anthropic, house-authored. Maximum authority on product
  capabilities and prescriptive deployment guidance. Internal case studies (Finance, Legal,
  Sales, Product) are first-person accounts from Anthropic's own teams using their own product
  in production — credible as practitioner reports but subject to promotional selection effects.
  External customer case studies (Thomson Reuters, Zapier, Jamf) are brief named testimonials.
  The five-level maturity model and three-phase roadmap are vendor-prescribed frameworks, not
  externally validated adoption research.
- **Scope**: Covers the Chat/Cowork/Code decision framework, a five-level maturity ladder,
  plugin architecture (Skills + Subagents + Connectors), a month-by-month deployment
  roadmap, a function-specific use-case table, and four Anthropic team archetype case studies.
  Does NOT cover: pricing, API/SDK integration details, technical architecture of Cowork's
  sandboxing or session management, security controls (these are covered in
  `blog-anthropic-cowork-enterprise.md`), or how Cowork compares to competing platforms.
  The PDF was published April 29, 2026 (20 days after the GA announcement in
  `blog-anthropic-cowork-enterprise.md`).

## Extracted Claims

### Claim 1: Claude Cowork occupies a defined middle tier in a three-surface decision framework — Chat for quick exchanges, Cowork for knowledge-work deliverables, Code for software development

- **Evidence**: First-party decision table in Chapter 1. The guide provides explicit decision
  criteria with examples per surface: Chat is for questions, rewrites, and quick brainstorms;
  Cowork is for research, analysis, and finished documents built from files and systems; Code
  is for writing, testing, or shipping software. The table format and explicit surface
  comparison imply deliberate product positioning to help enterprise users choose correctly.
- **Confidence**: settled (first-party product definition; authoritative for how Anthropic
  intends the surfaces to be used)
- **Quote**: "Chat is for quick exchanges: exploring an idea, iterating on a paragraph, getting
  an answer without leaving the app you're already in"
- **Our assessment**: This three-surface framework is the clearest mental model Anthropic has
  published for enterprise deployment. The key differentiator is *output type*: Chat produces
  answers; Cowork produces deliverables; Code produces software artifacts. The guide also
  specifies the deployment implication: "The three share the same Claude underneath; what
  changes is the workspace around it." This has direct guide impact — enterprises deploying
  Cowork need to train users on when NOT to use it (Chat suffices for most quick questions)
  to avoid wasted sessions.

### Claim 2: A five-level maturity model describes Claude Cowork adoption progression from passive Q&A to department-wide plugins

- **Evidence**: Chapter 2 of the guide. The five levels are: Level 0 (use as chat Q&A),
  Level 1 (building something from files/connectors), Level 2 (turn it into a repeatable
  skill), Level 3 (bundle skills, schedule them), Level 4 (create department plugins for
  everyone). Examples given per level. The guide states: "nobody is expected to jump straight
  to the top" and "the goal is to get every user one level higher than they are now."
- **Confidence**: settled (first-party vendor-prescribed model; authoritative for how Anthropic
  defines adoption maturity)
- **Quote**: "Chat is everyone's Level 0. Claude Cowork is where Levels 1 through 4 happen
  for knowledge work, and Code is where the same progression happens for engineering."
- **Our assessment**: The maturity model is practically useful as a deployment planning tool —
  it prevents the common failure of trying to deploy Level 4 capabilities to Level 0 users.
  The explicit "one level higher" target sets an achievable short-term goal. The model is
  vendor-prescribed rather than empirically derived from studying adoption trajectories, so
  treat it as planning heuristic rather than measured adoption science. The guide's structure
  (Sections 3-5) is explicitly organized around the model levels, making it a genuine
  organizing framework rather than marketing taxonomy.

### Claim 3: Plugins bundle three distinct components — Skills (encoded workflows in markdown), Subagents (autonomous end-to-end workflows), and Connectors (MCP-based two-way integrations)

- **Evidence**: Chapter 1 plugin anatomy section with explicit three-part definition. Skills
  are described as "encoded workflows (markdown files) that tell Claude how your team does
  something." Subagents are "autonomous workflows Claude runs end to end without you watching."
  Connectors are "two-way integrations built on MCP (Model Context Protocol, a universal
  standard for connecting AI applications to external data and tools)."
- **Confidence**: settled (first-party component definition; authoritative on plugin structure)
- **Quote**: "A plugin bundles three things: Skills are encoded workflows (markdown files) that
  tell Claude how your team does something."
- **Our assessment**: The three-part anatomy is the most precise definition of Claude Cowork's
  plugin system published to date. The distinction between Skills (prescriptive, markdown
  instructions for how to do a task), Subagents (autonomous, self-directed), and Connectors
  (data integration via MCP) maps cleanly to three deployment concerns: process encoding,
  automation trust, and system integration. The guide explicitly notes that connectors
  "respect your existing permissions; Claude sees what the user sees" — this is the
  permission model for MCP in Cowork. Guide chapters on MCP tooling and plugin governance
  should use this taxonomy.

### Claim 4: Plugins are file-based markdown documents, making them portable, version-controllable, and authorable by non-engineers

- **Evidence**: Chapter 1 direct description: "Plugins are file-based and written in markdown,
  which means they're portable, version-controllable, and editable by anyone who can write a
  how-to doc." Reinforced by the Anthropic Legal case study: "the plugin is markdown files
  that tell Claude how Anthropic's legal team thinks about risk, reviews launches, and
  structures advice." The guide also states the Legal plugin was built by a lawyer, not an
  engineer.
- **Confidence**: settled (first-party technical description of how plugins are implemented;
  confirmed by internal case study)
- **Quote**: "Plugins are file-based and written in markdown, which means they're portable,
  version-controllable, and editable by anyone who can write a how-to doc. You don't need an
  engineering team to build one."
- **Our assessment**: This is architecturally significant for enterprise deployment planning.
  Markdown-based plugins mean: (1) no proprietary plugin format to learn; (2) version control
  via standard git workflows; (3) the people who understand the business process (lawyers,
  analysts, ops managers) can build and maintain the plugins themselves. The guide's claim
  that Anthropic's Legal plugin "is system instructions, not case law" makes the generality
  explicit: any team with documented processes can encode them. The guide's open-source plugin
  library (referenced in additional resources) corroborates this by publishing plugins for
  Sales, Legal, Finance, Marketing, Product, and HR.

### Claim 5: A three-phase six-month deployment roadmap (Evaluate → Pilot → Scale) maps directly to the maturity levels

- **Evidence**: Chapter 4 deployment framework table and narrative. Phase 1 (Month 1 Evaluate):
  security review, install pre-built plugins, connect 1-2 core systems, champions reach
  Level 1. Phase 2 (Months 2-3 Pilot): run real workflows, measure against criteria, demo
  wins, champions reach Levels 2-3. Phase 3 (Months 4-6 Scale): admin-provisioned plugin
  marketplace, encode pilot learnings as org-wide skills, department reaches Level 4. Each
  phase has explicit "target level," "actions," and "what you'd expect to see."
- **Confidence**: settled (first-party prescriptive framework; structured and internally
  consistent)
- **Quote**: "In this section, we share a month-by-month framework for scaling Claude Cowork
  across your organization that maps to our adoption levels. Month 1 gets your champions to
  Level 1, familiarizing themselves with the solution. Months 2 and 3 get those champions to
  Levels 2 and 3, building and scheduling their own skills. Months 4 through 6 take what the
  champions built and provision it as Level 4 department plugins for everyone else."
- **Our assessment**: The explicit mapping from deployment phase to maturity level makes this
  a usable operational plan, not just a vision. The security review as a Month 1 prerequisite
  (before users are waiting on it) is sound operational advice — getting security review done
  first prevents the common scenario where users discover they can't connect to key systems
  after launch. The OTel/SIEM setup advice ("OpenTelemetry support lets admins export usage
  and tool activity to Datadog, Splunk, or whatever backend you run. Get this done before users
  are waiting on it") reinforces this pattern. Corroborates the enterprise governance controls
  described in `blog-anthropic-cowork-enterprise.md`.

### Claim 6: Four categories of pilot-worthy use cases identify high-ROI entry points for Cowork deployment

- **Evidence**: Chapter 3 explicit list with rationale for each category. The four are:
  (1) High volume, high repetition — "dozens of times a week and follows a knowable pattern";
  (2) Information-dense synthesis — "anywhere a human is spending time being the integration
  layer between systems"; (3) Bottleneck-creating work — "speeding up cross-functional work
  doesn't save one person time; it unblocks everyone downstream"; (4) Expertise-dependent but
  process-driven — "the work only your best people do well today, because they've internalized
  a process nobody wrote down."
- **Confidence**: emerging (first-party prescriptive framework; consistent with practitioner
  accounts in corpus but vendor-authored, not an empirical study of what works)
- **Quote**: "Expertise-dependent but process-driven. Business reviews, specialized recruiting
  screens, or product briefs–in other words, the work only your best people do well today,
  because they've internalized a process nobody wrote down–fit the bill. This category pays
  back the most: encode that process in a skill and everyone on the team inherits it."
- **Our assessment**: The fourth category (expertise-dependent but process-driven) is the most
  distinctive and highest-value claim. This is precisely the case where tribal knowledge
  codification creates organizational leverage: the best analyst's workflow becomes everyone's
  baseline. The guide frames this correctly as the highest-payback category, not just a
  nice-to-have. The "bottleneck-creating work" category is also notable: it shifts the ROI
  calculation from individual time savings to unblocked downstream throughput — a better frame
  for enterprise adoption than "hours saved per person."

### Claim 7: The cold-start problem — users who open Cowork without direction close it immediately — is solved by pre-configured plugins delivering value within 90 seconds

- **Evidence**: Chapter 4, Month 1 section. Direct description: "The cold-start problem is
  real: if someone opens Claude Cowork and doesn't know what to do, they close it. If they
  open it, type /morning-briefing, and get something useful in ninety seconds, they come back
  tomorrow." The recommendation: have champions leverage pre-configured plugins so they get
  value in the first session.
- **Confidence**: emerging (named, specific failure mode described by Anthropic from observed
  deployment behavior; not a controlled study, but specific and actionable)
- **Quote**: "The cold-start problem is real: if someone opens Claude Cowork and doesn't know
  what to do, they close it. If they open it, type /morning-briefing, and get something useful
  in ninety seconds, they come back tomorrow."
- **Our assessment**: This is one of the most practically useful claims in the guide. The
  cold-start failure mode is a specific, named anti-pattern with a specific solution
  (pre-configured plugins). The "ninety seconds" specificity suggests this comes from
  observed user behavior. The recommendation to connect systems and data sources early — "A
  sales plugin that reads your most critical Salesforce dashboard is categorically more useful
  than one that doesn't" — extends the cold-start solution: plugins need real data to be
  immediately valuable.

### Claim 8: The deployment pattern is bottom-up discovery, top-down scale — let teams experiment, then provision org-wide through admin-managed plugin marketplaces

- **Evidence**: Chapter 4, Scale phase section. Explicit statement: "The pattern is bottom-up
  discovery, top-down scale. Let teams experiment and find what works for their function, then
  take what works and provision it org-wide through admin-managed plugin marketplaces."
  Additional: "The finance plugin that one team built becomes the finance plugin the whole
  finance org runs, with version control and the ability to push improvements to everyone at
  once."
- **Confidence**: emerging (first-party prescriptive pattern; consistent with the Jamf and
  Zapier case studies in the corpus but vendor-authored)
- **Quote**: "The pattern is bottom-up discovery, top-down scale. Let teams experiment and
  find what works for their function, then take what works and provision it org-wide through
  admin-managed plugin marketplaces."
- **Our assessment**: This is the key organizational pattern for avoiding both failure modes:
  top-down mandates (which generate resentment and shadow AI) and bottom-up fragmentation
  (which produces undiscoverable, un-maintained private workflows). The admin-provisioned
  plugin marketplace is the mechanism that converts experimental individual skills into
  organizational infrastructure. The guide warns explicitly against top-down mandates: "when
  individuals adopt AI tools without oversight you get shadow AI: dozens of private workflows
  nobody can see, audit, or improve." This inverts the typical enterprise software rollout
  playbook.

### Claim 9: Champion-authored skills are the leading indicator for the scale phase — tracking skill authorship is a better pilot success metric than hours saved

- **Evidence**: Chapter 4, Pilot phase section. Direct recommendation: "The signal that a
  pilot is working isn't just hours saved. It's champions starting to write their own skills.
  When a rep takes the call-prep workflow she's been running by hand and turns it into a
  /call-prep skill, she's crossed from Level 1 to Level 2, and that skill is now an asset
  the rest of the org can inherit...Track how many champion-authored skills exist at the end
  of the pilot; it's the leading indicator for the scale phase."
- **Confidence**: emerging (vendor-prescribed metric; consistent with the maturity model but
  not empirically validated)
- **Quote**: "The signal that a pilot is working isn't just hours saved. It's champions
  starting to write their own skills."
- **Our assessment**: This is a genuinely useful operational metric. Hours saved is a lagging,
  self-reported measure; skill authorship is observable and leading (it predicts whether the
  organization has the capability to scale). The framing also reveals the correct success
  criterion for each phase: Phase 1 success = value in first session; Phase 2 success =
  champions building skills; Phase 3 success = skills shared across teams, new hires start
  at Level 2.

### Claim 10: The supervised-then-scheduled autonomy progression is the Level 2-to-Level-3 move — run with validation, then remove it once behavior is confirmed

- **Evidence**: Chapter 5, Sales team case study. One rep built a skill that auto-updates
  Salesforce opportunities after calls: "He started with a validation step on every update.
  After enough manual checks confirmed Claude was getting it right, he removed the validation
  and lets it run. That progression, run it supervised, then run it scheduled, is the Level 2
  to Level 3 move, and it saves hours per week."
- **Confidence**: anecdotal (one rep's specific experience at Anthropic; the pattern is
  well-grounded in the maturity model but the evidence is a single case study)
- **Quote**: "That progression, run it supervised, then run it scheduled, is the Level 2 to
  Level 3 move, and it saves hours per week."
- **Our assessment**: This is the most concrete description in the guide of the trust-building
  process for agent autonomy. The mechanism — start with a mandatory human validation step,
  confirm reliability empirically, then disable the validation and run autonomously — is a
  reproducible pattern for any enterprise deploying Cowork agents. It is directly analogous
  to the MCP connector permission expansion pattern in `blog-anthropic-cowork-enterprise.md`
  (Claim 2: read-only first, validate, then expand to write). The guide gives this pattern
  a named level transition (Level 2→3), which makes it teachable to champions.

### Claim 11: Level 4 plugin adoption raises the floor for new hires — they start at Level 2 rather than Level 0

- **Evidence**: Chapter 4, Scale phase section. "Level 4 also changes the onboarding equation.
  A new hire who installs the department's plugin on day one starts at Level 2, not Level 0.
  They get the encoded workflows before they've had time to develop bad habits, and the floor
  for the whole team rises."
- **Confidence**: emerging (vendor claim with logical basis; not empirically measured but
  consistent with the maturity model)
- **Quote**: "A new hire who installs the department's plugin on day one starts at Level 2,
  not Level 0. They get the encoded workflows before they've had time to develop bad habits,
  and the floor for the whole team rises."
- **Our assessment**: This is the organizational compounding argument for plugin investment.
  If plugins encode the team's best practices, new hires inherit those practices rather than
  having to rediscover them. The "bad habits" framing is also practically important: Level 0
  users who develop their own prompting habits before installing the plugin may need to
  unlearn those habits. Early plugin installation prevents this. The guide doesn't quantify
  "floor rises" but the logic is sound.

### Claim 12: Plugin stacking — layering multiple plugins in a single Cowork session — creates compound context greater than any individual plugin

- **Evidence**: Chapter 5, Product team case study. The PM team layers four plugins:
  productivity plugin (personal context and calendar), data plugin (live analytics), sales
  plugin (customer insights from calls/tickets), product plugin (PRD structure and roadmap
  methodology). "Individually, each plugin is useful. Stacked, Claude has org context, real
  usage data, actual customer quotes, and a framework for turning all of it into a PRD, at
  the same time, in the same session."
- **Confidence**: anecdotal (one team's specific architecture; the compound-context logic
  is sound but the evidence is a single case study)
- **Quote**: "Individually, each plugin is useful. Stacked, Claude has org context, real usage
  data, actual customer quotes, and a framework for turning all of it into a PRD, at the same
  time, in the same session."
- **Our assessment**: Plugin stacking is the most architecturally interesting claim in the
  guide. It implies that Cowork's value compounds as the number of installed plugins increases,
  because each plugin expands the context Claude holds in-session. The product team example
  demonstrates a specific four-plugin stack where the output (PRD) synthesizes inputs from
  four different data sources simultaneously. The guide's closing observation — "the context
  from one informs the others: a customer complaint from the sales plugin shapes the priority
  call in the product plugin, grounded in the usage data from the data plugin" — makes the
  cross-plugin context flow explicit.

### Claim 13: Tribal knowledge codification — encoding expert workflows as skills — converts individual expertise into organizational infrastructure

- **Evidence**: Chapter 1 "Scale" section. "When your best analyst's workflow lives in a skill
  rather than in her head, it stops being tribal knowledge and becomes organizational
  infrastructure. Claude Cowork allows organizations to tackle complex, multi-step tasks at
  scale, across teams." Also: "The playbook your top AE uses to prep for renewals, the
  checklist your senior counsel runs on every MSA, and the format your RevOps lead built for
  pipeline reviews become encoded in your organizational workflows, allowing every person on
  the team to work with the same context and processes."
- **Confidence**: emerging (vendor claim consistent with the Airtree VC and Jamf case studies
  in `blog-anthropic-cowork-enterprise.md` Claim 7; the codification pattern is supported by
  multiple independent examples but remains vendor-framed)
- **Quote**: "When your best analyst's workflow lives in a skill rather than in her head, it
  stops being tribal knowledge and becomes organizational infrastructure."
- **Our assessment**: This is the organizational leverage argument that justifies the skill
  investment. The framing shift — from "saving time" to "converting tribal knowledge to
  infrastructure" — is the correct level of abstraction for executive audiences. It also
  implies the governance requirement: if expert workflows become org-wide infrastructure,
  then the quality, accuracy, and currency of those skills matter organizationally, not
  just personally. The guide doesn't address skill governance (review, versioning,
  deprecation) — that gap is noted in `blog-anthropic-cowork-enterprise.md` Claim 7.

### Claim 14: Anthropic's Legal team built a department plugin in an afternoon by pointing Claude at existing memos, risk frameworks, and policy documents — no coding required

- **Evidence**: Chapter 5, Legal team case study. "The team built the Legal plugin in an
  afternoon, not by coding anything, but by pointing Claude at their actual work product: the
  memos, the risk frameworks, the policy docs. The plugin is markdown files that tell Claude
  how Anthropic's legal team thinks about risk, reviews launches, and structures advice." Also:
  "As Pike describes it, the project is recursive: he used Claude to build the plugin, and
  now uses the plugin every day to do his actual job."
- **Confidence**: anecdotal (one team's specific experience; the "afternoon" timing is
  corroborated by Jamf's 45-minute case study but is still a single data point per team)
- **Quote**: "The team built the Legal plugin in an afternoon, not by coding anything, but
  by pointing Claude at their actual work product: the memos, the risk frameworks, the
  policy docs."
- **Our assessment**: The "recursive" framing (used Claude to build the plugin that Claude
  uses to do the work) is a concrete illustration of the bootstrap process for knowledge
  workers. More importantly: the Legal plugin's input (memos, risk frameworks, policy docs)
  is documentation that any legal team already has. This lowers the activation energy for
  legal plugin creation significantly — no AI engineering background required. The guide also
  notes the plugin is open-source on GitHub because "there's nothing proprietary about it.
  It's system instructions, not case law."

### Claim 15: Anthropic Finance connected Cowork to the data warehouse via MCP, enabling non-technical staff to build interactive dashboards and generate contextualized alerts without SQL or engineering tickets

- **Evidence**: Chapter 5, Finance team case study. Before Cowork: "Dashboard builds took
  weeks. Alerts surfaced raw metrics with no context: 'revenue down 3%' instead of 'revenue
  down 3% driven by a dip in APAC enterprise renewals.'" After: "Development velocity moved
  from weeks to hours. Non-technical team members build interactive dashboards without filing
  a ticket. One account executive built a book-of-business dashboard, credit usage, per-account
  ARR, momentum indicators, drill-downs, that he uses multiple times a day."
- **Confidence**: anecdotal (single Anthropic team's internal experience; detailed and
  specific but self-reported)
- **Quote**: "Development velocity moved from weeks to hours. Non-technical team members build
  interactive dashboards without filing a ticket."
- **Our assessment**: The before/after contrast (weeks to hours; raw metrics to contextualized
  alerts) is the clearest ROI statement in the guide. The underlying mechanism — a data skill
  that encodes schema knowledge, naming conventions, and table quirks so non-technical users
  can query the warehouse without SQL — is the MCP connector pattern in practice. The alert
  quality improvement ("revenue down 3%" → "down 3% driven by APAC enterprise renewals dip")
  illustrates the shift from data delivery to contextual synthesis, which is the distinct
  value proposition of agent-based analysis over BI tools.

## Concrete Artifacts

### Five-Level Maturity Model (from PDF guide, Chapter 2)

```
Claude Cowork Maturity Model — Five Levels
(Anthropic, April 2026 Deployment Guide)

Level 0: Chat Q&A
  - Connect Slack or Drive, ask a question, get an answer
  - Example: "Summarize what was decided in #project-atlas this week."

Level 1: Building something
  - Claude reads files and connects to tools to create a deliverable
  - Example: "Here's the deal folder. Draft an investment memo."

Level 2: Turn it into a skill
  - One markdown file runs the same task the same way every time
  - Example: A /variance-analysis skill that knows your tables, thresholds, and CFO's format

Level 3: Bundle skills, schedule them
  - Skills run on their own, return analysis, or run daily workflows
  - Example: Morning briefing at 7:30am pulling calendar, pipeline, and overnight Slack into one page

Level 4: Create a plugin for every department
  - Curated, admin-provisioned bundle of skills, subagents, and connectors
  - Example: Anthropic's Legal plugin — intake triage, regulatory monitoring, exec updates

Note: Chat is Level 0 for everyone. Code is the same progression for engineers.
Goal: get every user one level higher than they are now, every deployment cycle.
```

### Three-Phase Deployment Roadmap (from PDF guide, Chapter 4)

```
Claude Cowork Deployment Framework — Six Months
(Anthropic, April 2026 Deployment Guide)

Phase       | Timeline   | Target Level | Key Actions                          | Success Signal
------------|------------|--------------|--------------------------------------|----------------------------------
Evaluate    | Month 1    | Champions → 1| Security review; pre-built plugins;  | "This saved me an hour" moments
            |            |              | connect 1-2 core systems             |
Pilot       | Months 2-3 | Champions → 2-3 | Real workflows; weekly check-ins; | Measurable time savings; champions
            |            |              | demo wins to adjacent teams          | building and scheduling own skills
Scale       | Months 4-6 | Dept → 4     | Admin-provisioned plugin marketplace;| Skills shared across teams; new
            |            |              | encode pilot as org-wide skills;     | hires ramping on encoded workflows;
            |            |              | onboard next wave                    | declining "how do I" support tickets

Month 1 prerequisite: Run security review before users are waiting on it.
Month 1 prerequisite: Connect systems early — plugins are significantly more
  useful with real organizational data.
Pilot success signal: Count champion-authored skills at end of pilot (leading indicator).
```

### Chat / Cowork / Code Decision Table (from PDF guide, Chapter 1)

```
Which Claude Surface to Use
(Anthropic, April 2026 Deployment Guide)

If the task is...                          | Reach for     | Why
-------------------------------------------|---------------|----------------------------
A question, a rewrite, a quick brainstorm  | Chat          | Fast, conversational, no setup
Research, analysis, or a finished document | Claude Cowork | Folder access, connectors,
  built from your files and systems        |               | skills, scheduled runs
Writing, testing, or shipping software     | Claude Code   | Codebase access, diffs, git,
                                           |               | dev environments

"The three share the same Claude underneath; what changes is the workspace around it."
```

### Function-Specific First Use Case Table (from PDF guide, Chapter 3)

```
Starting Points by Function — Level 1 Entry Points
(Anthropic, April 2026 Deployment Guide)

Function  | First use case                                | What you'd measure
----------|-----------------------------------------------|----------------------------
Legal     | NDA review and redline against your playbook  | Review turnaround time; queue depth
Finance   | Variance analysis with root-cause commentary  | Time from close to narrative; analyst hours per cycle
Sales     | Pre-call research and brief generation        | Prep time per call; rep-reported confidence
Product   | PRD drafting from customer feedback/analytics | Time to first reviewable draft
HR        | Performance review drafting from rubric/notes | Cycle completion rate; manager time per review
Marketing | Campaign brief to asset draft vs. brand guide | Concept-to-review time; rounds of revision
```

### Plugin Anatomy (from PDF guide, Chapter 1)

```
Claude Cowork Plugin Components
(Anthropic, April 2026 Deployment Guide)

A plugin bundles three things:

1. Skills — encoded workflows (markdown files) that tell Claude how your team
   does something. Can be invoked via slash commands (/variance-analysis) or
   triggered automatically when Claude recognizes they're relevant.

2. Subagents — autonomous workflows Claude runs end to end without you watching.
   Example: an agent that monitors regulatory filings across jurisdictions and
   flags what's material to your business, or one that checks your book of
   accounts for untracked revenue every Friday.

3. Connectors — two-way integrations built on MCP (Model Context Protocol)
   that let Claude read from and write to external systems: Salesforce, Slack,
   BigQuery, Docusign, Jira, Google Workspace, and others.
   "Connectors respect your existing permissions; Claude sees what the user sees."

Format: Plugins are file-based and written in markdown — portable,
  version-controllable, editable without engineering background.
```

### Anthropic Internal Team Case Studies Summary (from PDF guide, Chapter 5)

```
Anthropic Internal Deployment Archetypes — Four Teams
(Anthropic, April 2026 Deployment Guide)

FINANCE (data-heavy):
  Problem: Dashboard builds took weeks; alerts surfaced raw metrics ("revenue down 3%")
    with no context; SQL and schema knowledge locked in 2-3 people's heads.
  Approach: Connected to data warehouse via MCP; built 4 skills (insight agent,
    financial statements, variance analysis with root-cause, dashboard builder).
    Then: company-wide data skill so PMs and sales managers can query warehouse
    without SQL.
  Impact: "Development velocity moved from weeks to hours." Non-technical staff build
    dashboards without tickets. Alerts now include likely driver alongside the number.

LEGAL (document-heavy):
  Problem: Regulatory monitoring across jurisdictions, ticket triage, exec updates
    consumed judgment time; institutional knowledge in memos/wikis most hadn't read.
  Approach: Built Legal plugin in an afternoon using existing memos, risk frameworks,
    policy docs. "The project is recursive: he used Claude to build the plugin, and
    now uses the plugin every day to do his actual job."
  Impact: Regulatory monitoring went from reading everything to reading what Claude
    flagged. Biweekly exec updates went from near a full day to a fraction of that.
    Analyzed 742 Jira tickets; analysis reshaped intake structure.
  Note: Legal plugin is open-source on GitHub; "It's system instructions, not case law."

SALES (relationship-heavy):
  Problem: 30 min of call prep per call; context scattered across Salesforce, email,
    Gong, Slack, and "somebody's memory."
  Approach: Five skills — morning briefing, call prep, post-call follow-up,
    competitive intelligence, asset creation.
  Impact: Morning briefing in ~2 minutes. Call prep happens in background while on
    previous call. One rep built supervised Salesforce auto-update; after validation
    confirmed accuracy, removed supervision — Level 2→3 move, saves hours/week.

PRODUCT (cross-functional):
  Problem: Decisions made in meetings not written down; customer insights from sales
    calls never reaching PRDs; Claude lacked org context to help with strategy.
  Approach: Plugin stacking — productivity + data + sales + product plugins in a
    single session.
  Impact: PRDs written from real usage data and actual customer quotes, not generic
    templates. "The PM's job shifts from gathering to deciding."
```

### External Customer Case Studies (from PDF guide, Chapters 3 and 4)

```
External Customer Deployments
(Anthropic, April 2026 Deployment Guide)

JAMF — Matt Benyo, Director of AI Initiatives:
  Workflow: 7-facet performance review spreadsheet (branching logic by level/role)
    converted to a guided, interactive Cowork skill in 45 minutes.
  Quote: "We built a skill that turns a complex performance review spreadsheet,
    seven competency facets, branching logic by level and role, into a guided,
    interactive experience in Claude Cowork. What would have required a team of
    engineers building a custom React app, Claude Cowork delivered in 45 minutes.
    And it's more adaptive than anything we would have built."
  Pattern: HR rubric → guided skill (Level 1 to Level 2 in 45 min because
    process was already proven; encoding made it repeatable).

ZAPIER — Joe Stych, Head of Product Marketing:
  Workflow: Homepage messaging prototyping — Claude navigates live page,
    identifies core modules, generates HTML mockup aligned to new positioning.
  Quote: "I connected Claude Cowork to our homepage, a custom skill with our
    PMM guidelines, and our internal tools through MCP so it could pull from
    Slack threads, Glean searches, whatever context it needed. Now I give Claude
    new positioning and ask it to develop versions of our homepage with improved
    messaging. It looks at the page, works through its steps, and generates an
    HTML mockup. After 15 minutes I'm sharing it with our team to build on."
  Pattern: PMM context encoded in skill travels between projects;
    "Level 2 asset doing Level 4 work."

THOMSON REUTERS — Joel Hron, CTO, Thomson Reuters:
  Pattern: Non-developers moving into automation and light prototyping using
    documents and data they already work with. Skeptics converted after running
    real workflows (not after demos).
  Quote: "Claude Cowork helps teams do work at a scale that was hard to justify
    before. The human role becomes validation, refinement, and decision-making.
    Not repetitive rework."

NOTE: Joel Hron is identified as CTO of Thomson Reuters in this guide. The existing
  source note blog-anthropic-cowork-enterprise.md Claim 8 attributes the same quote
  ("The human role becomes validation, refinement, and decision-making. Not repetitive
  rework.") to "Joel Hron (CTO of Cowork)" — this appears to be an attribution error
  in the existing note. The PDF guide is unambiguous: "Joel Hron, CTO, Thomson Reuters."

NOTE ON JAMF NAMES: The existing source note blog-anthropic-cowork-enterprise.md Claim 9
  cites "Nick Benyo / Jamf" (Software Engineer). This guide cites "Matt Benyo, Director
  of AI Initiatives, Jamf." These may be different Jamf employees or an attribution
  discrepancy in the existing note.
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-cowork-enterprise.md` Claim 6 ("surrounding work first" adoption
    pattern) — this guide's five-level maturity model and deployment roadmap operationalize
    that observation: the maturity model describes what "surrounding work" tasks look like
    at Levels 1-2, before teams reach core-work automation at Levels 3-4.
  - `blog-anthropic-cowork-enterprise.md` Claim 7 (skills-as-shared-infrastructure) —
    this guide's tribal knowledge codification claim (Claim 13) and the Level 4 onboarding
    effect (Claim 11) provide the operational mechanism: admin-provisioned plugins convert
    individual skills into org-wide infrastructure with explicit governance (version control,
    admin push).
  - `blog-anthropic-building-enterprise-agents.md` Claim 2 ("encoding institutional
    knowledge into systems that compound over time") — this guide's plugin stacking (Claim 12)
    and tribal knowledge codification (Claim 13) are the concrete mechanisms behind that
    abstract framing. The Cowork guide gives the "compounding" claim operational substance:
    the compound is skills shared across users, contextualized by stacked plugins, and
    inherited by new hires.
  - `blog-bvp-shopify-ai-playbook.md` — the bottom-up discovery, top-down scale pattern
    (Claim 8) inverts Shopify's top-down governance approach. Both sources agree that
    admin-level controls matter; they differ on whether the workflow discovery is driven
    top-down (Shopify mandate) or bottom-up (Cowork champion model).

- **Contradicts**: None material requiring a contradiction issue per MINER.md §4a.
  However, two attribution discrepancies in `blog-anthropic-cowork-enterprise.md` are
  surfaced by this guide and should be corrected:
  1. Joel Hron's affiliation: existing note says "CTO of Cowork"; this guide says "CTO,
     Thomson Reuters." This guide is unambiguous. The existing note should be corrected.
  2. Jamf contact name: existing note says "Nick Benyo / Jamf (Software Engineer)"; this
     guide says "Matt Benyo, Director of AI Initiatives, Jamf." These may be different people,
     or one source has an error.
  Neither rises to a material contradiction about guide advice, so no contradiction issue
  is filed. But the Smith should correct the existing note's attribution before citing.

- **Extends**:
  - `blog-anthropic-cowork-enterprise.md` — the GA announcement established four enterprise
    controls (SCIM RBAC, MCP connector action controls, OTel observability, group spend limits)
    and named-customer use cases. This guide adds: the Chat/Cowork/Code decision framework,
    the five-level maturity model, the plugin anatomy taxonomy, the three-phase deployment
    roadmap, the four pilot use-case categories, the four internal Anthropic team archetypes,
    and the cold-start problem + solution. The two notes together give a complete picture:
    the GA note covers governance infrastructure; this note covers deployment practice.
  - `blog-anthropic-building-enterprise-agents.md` — that post was thin (~500 words) and
    referenced a PDF guide that was inaccessible at time of extraction. This guide is the
    practical analog: where that post set strategic framing, this guide provides the
    operational playbook.
  - `blog-anthropic-compliance-api.md` — this guide explicitly cites OTel support (for
    Datadog/Splunk) as a Month 1 prerequisite. The security review and OTel setup
    instructions in Chapter 3 extend the compliance integration architecture from the
    compliance-api note into an operational deployment sequence.

- **Novel** (not in prior corpus):
  - **Five-level maturity model** (Claim 2): No prior corpus source provides a named,
    vendor-defined maturity model for non-engineering AI adoption. This is the first.
  - **Plugin anatomy as Skills + Subagents + Connectors** (Claim 3): The three-part
    classification with explicit mechanics for each component is not described in prior
    corpus sources. MCP connector notes cover the connector piece; this note adds the
    full three-part bundle.
  - **Markdown-first plugin architecture** (Claim 4): The explicit description of plugins
    as portable markdown files, version-controllable, authorable by non-engineers, is not
    in any prior corpus source.
  - **Cold-start problem + 90-second solution** (Claim 7): Named anti-pattern with specific
    remedy; not previously described.
  - **Champion-authored skills as leading indicator** (Claim 9): A concrete, observable
    pilot success metric distinct from lagging measures like hours saved; not in prior corpus.
  - **Supervised-then-scheduled autonomy progression** (Claim 10): Named, level-tagged
    (Level 2→3) trust-building sequence for agent automation; more specific than prior
    corpus descriptions of human-in-the-loop patterns.
  - **Plugin stacking / compound context** (Claim 12): Multi-plugin layering as a design
    pattern for session-level context accumulation; not previously described.
  - **Level 4 onboarding effect** (Claim 11): The claim that department plugins raise the
    starting floor for new hires is new to the corpus.
  - **Function-specific first use case table** (Artifact): The six-function table (Legal,
    Finance, Sales, Product, HR, Marketing) with specific first use cases and metrics is
    a unique operational artifact not found elsewhere.

## Guide Impact

- **Chapter on Enterprise & Team Adoption (Ch04 planned)**: Add the Chat/Cowork/Code
  decision framework (Claim 1 + decision table artifact) as the prerequisite mental model
  for any enterprise Cowork deployment guide. Users must understand when NOT to use Cowork
  (most quick questions stay in Chat) before deployment scales.

- **Chapter on Enterprise & Team Adoption (Ch04 planned)**: Add the five-level maturity
  model (Claim 2 + maturity table artifact) as the deployment planning backbone. The current
  corpus has no vendor-defined maturity model for non-engineering AI adoption. This fills
  that gap. Present the model as a planning heuristic (first-party, not externally validated)
  with the explicit framing: "get every user one level higher, every deployment cycle."

- **Chapter on Enterprise & Team Adoption (Ch04 planned)**: Add the three-phase six-month
  deployment roadmap (Claim 5 + roadmap table artifact) as the recommended deployment
  sequence. Frame the security review + OTel setup as Month 1 prerequisites (before users
  are waiting). Champion-authored skills count as the leading success indicator for Phase 2.

- **Chapter on Enterprise & Team Adoption (Ch04 planned)**: Add the four pilot use-case
  categories (Claim 6) as selection criteria for the pilot phase. The fourth category
  (expertise-dependent but process-driven) should be highlighted as the highest-payback
  category and framed as tribal knowledge codification.

- **Chapter on Enterprise & Team Adoption (Ch04 planned)**: Add the cold-start problem and
  the 90-second pre-configured plugin solution (Claim 7) as a deployment anti-pattern to
  avoid. This is the most actionable insight in the guide for launch day planning.

- **Chapter on Enterprise & Team Adoption (Ch04 planned)**: Add the bottom-up discovery,
  top-down scale pattern (Claim 8) as the recommended organizational dynamic for Cowork
  rollout. Contrast with top-down mandate approaches that generate shadow AI.

- **Chapter on MCP Tooling & Permissions (Ch02 or planned)**: Add the plugin anatomy —
  Skills + Subagents + Connectors in markdown (Claims 3-4) — as the canonical Cowork
  plugin model. The markdown-first, non-engineer-authorable architecture lowers the
  activation energy for enterprise plugin creation significantly. The function-specific
  first use case table (Artifact) provides concrete entry points per department.

- **Chapter on MCP Tooling & Permissions / Governance**: Add the supervised-then-scheduled
  autonomy progression (Claim 10) as the recommended Level 2→3 transition pattern. This is
  the most concrete mechanism in the corpus for building toward agent autonomy without
  skipping trust-building steps.

- **Correction needed in `blog-anthropic-cowork-enterprise.md`**: Claim 8 attributes the
  "The human role becomes validation, refinement, and decision-making. Not repetitive rework."
  quote to "Joel Hron (CTO of Cowork)." This guide clearly attributes it to "Joel Hron, CTO,
  Thomson Reuters." The existing note's attribution should be corrected before the Smith cites
  it in the guide. (The Smith should not act on this — the Assayer or a human should correct
  the note in a separate PR.)

## Extraction Notes

- **Source is a blog post + linked PDF**: The blog post at the issue URL is ~400 words and
  contains minimal extractable content beyond the five-item description of what's in the guide.
  The substantive source is the 24-page PDF guide. Both were fully read. All claims above come
  from the PDF unless noted.
- **PDF was extracted via pdfplumber**: The PDF was downloaded locally and extracted page by
  page. All quotes were verified against the extracted text.
- **No sub-pages were followed**: The guide's "Additional Resources" section links to Cowork
  support documentation and an open-source plugin repository. Neither was followed (the
  resources page contains webinar links and doc references, not extractable claims; the
  plugin repository was not read). The support page (get-started-with-claude-cowork) was
  fetched but adds no claims beyond what the guide contains.
- **Attribution discrepancies flagged**: Two attribution discrepancies with the existing
  `blog-anthropic-cowork-enterprise.md` note were found (Joel Hron's affiliation; Matt/Nick
  Benyo at Jamf). These are noted in Cross-References and the Concrete Artifacts section
  but do not meet MINER.md §4a criteria for contradiction issues (no material guide advice
  difference).
- **Confidence calibration**: The maturity model and deployment framework are first-party
  vendor prescriptions (authoritative but untested externally → settled for what Anthropic
  recommends, emerging for whether it works in practice). Internal case studies are first-
  person Anthropic team accounts (specific but promotional → anecdotal). External case studies
  (Thomson Reuters, Zapier, Jamf) are brief testimonials (anecdotal). Overall: **emerging**
  because the deployment patterns rest on first-party prescriptions and self-reported case
  studies, not independently validated research.
- **No contradictions filed**: Reviewed CONTRADICTIONS.md (two open issues; neither related
  to Cowork deployment). No new contradiction issues filed — the attribution discrepancies
  do not meet the threshold in MINER.md §4a.
