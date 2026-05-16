---
source_url: https://claude.com/blog/deploying-claude-across-the-legal-industry
source_type: blog-post
title: "Deploying Claude across the legal industry"
author: Anthropic
date_published: 2026-05-15
date_extracted: 2026-05-16
last_checked: 2026-05-16
status: current
confidence_overall: emerging
issue: "#760"
---

# Deploying Claude across the legal industry

> A 21-page Anthropic deployment guide for legal organizations that extends the
> general Cowork deployment playbook to a regulated vertical: a five-product
> surface matrix, 12 practice-area plugins with detailed capability descriptions,
> four Anthropic legal team case studies with concrete time metrics, and a
> legal-specific three-phase adoption roadmap covering privilege protection,
> legal-specific connectors, pilot success criteria, and skill governance.

## Source Context

- **Type**: blog-post + linked 21-page PDF guide. The blog post at the source URL
  is a ~400-word introduction; the substantive content is in the downloadable guide
  at `https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6a0775c566cb42bd866e108b_Claude-for-the-legal-industry-05152026_v6.pdf`
  (title: "Claude for the legal industry: A practical deployment guide"). Both were
  fully read for this extraction. All claims below come from the PDF unless noted
  as from the blog post.
- **Author credibility**: First-party Anthropic, house-authored. Authoritative on
  product capabilities, legal plugin descriptions, and prescriptive deployment
  guidance. The four Anthropic legal team case studies are first-person accounts
  from their own teams in production — credible as practitioner reports, subject
  to promotional selection effects. Industry adoption statistics cite the 2026 FTI
  Consulting / Relativity General Counsel Report, an independent third-party survey.
  Plugin descriptions are product specifications, not independently validated.
- **Scope**: Covers the five-surface Claude product matrix for legal, three
  building blocks for customization (connectors, skills, plugins), detailed
  descriptions of 12 practice-area plugins, four Anthropic legal team case studies
  with concrete metrics, a three-phase adoption roadmap with legal-specific actions,
  a segment-level use-case table (in-house, transactional, litigation, compliance),
  and IT/CIO FAQ covering hosting, privilege protection, SSO, ZDR, and data
  retention. Does NOT cover: pricing, comparative analysis against competing
  platforms, or empirical study of legal AI outcomes beyond Anthropic's own team.
  Published May 15, 2026 — three days after issue #725's related legal plugin focus.

## Extracted Claims

### Claim 1: Legal AI adoption has tripled from 20% to 87% in three years, with summarization, contract clause identification, and transcription as the top current use cases

- **Evidence**: Third-party survey data cited from the 2026 FTI Consulting /
  Relativity General Counsel Report. Specific percentages for top use cases also
  from the same report.
- **Confidence**: emerging (third-party self-report survey; methodology not detailed
  in this guide; "genAI use within their teams" is broad — does not distinguish
  light use from integrated workflows)
- **Quote**: "A 2026 FTI Consulting / Relativity General Counsel Report found that
  87% of general counsel now report genAI use within their teams, compared with 44%
  the prior year. The longer-term trajectory is even sharper: CLO gen AI use has
  climbed from 20% in 2023 to 87% in this year's report."
- **Our assessment**: The growth trajectory is striking and plausible — it aligns
  with broad enterprise AI adoption curves across sectors. The top use cases
  (summarization at 83%, contract clause identification at 63%, transcription at 53%)
  are consistent with task types that benefit from LLM strength in text understanding
  without high-stakes generation risk. The guide frames this as validating the
  industry's readiness for agentic AI: "systems that act on the work, not just answer
  questions about it." The jump from 44% to 87% in a single year suggests rapid
  normalization rather than cautious specialized adoption.

### Claim 2: Legal organizations should select from five distinct Claude surfaces — Chat, Cowork, Microsoft 365, Platform, and Managed Agents — based on the scope and autonomy of the task

- **Evidence**: First-party product matrix table (PDF Chapter 1) with explicit
  mapping of surface → best-for → primary users → where it runs → example task.
  Each surface has an explicitly different operational model.
- **Confidence**: settled (first-party product definition; authoritative for how
  Anthropic intends each surface to be used)
- **Quote**: "Claude shows up to work for lawyers in a few forms: Claude chat,
  Claude Cowork, Claude for Microsoft 365, Claude Platform, and Claude Managed
  Agents."
- **Our assessment**: The five-surface matrix is more granular than the three-surface
  framework (Chat / Cowork / Code) in `blog-anthropic-cowork-deploy-guide.md` Claim 1.
  Claude Managed Agents is a new fifth surface not covered in the general deployment
  guide — it enables teams to build agents on the Claude Platform and have Anthropic
  run them as hosted services with "long-running sessions, scoped permissions, and
  audit trail handled for them." The legal application (NDA triage agent across
  thousands of incoming agreements) is the first concrete example in the corpus of
  Managed Agents used for high-volume, document-intensive legal work. Claude Platform
  is positioned for legal engineering teams and legal tech vendors building custom CLM,
  e-discovery, or matter management integrations.

### Claim 3: Three building blocks — MCP Connectors, Skills, and Plugins — customize Claude to legal organizations, with the MCP standard preserving privilege by honoring existing DMS access controls

- **Evidence**: PDF Chapter 1, "Customizing Claude: connectors, skills, and plugins"
  section. The privilege protection mechanism is explicitly described in both
  Chapter 1 and the CIO FAQ (Chapter 3).
- **Confidence**: settled (first-party technical description of the product's access
  control mechanism; the MCP end-user entitlement model is confirmed in the CIO FAQ)
- **Quote**: "MCP Connectors give Claude access to a specific data source over the
  Model Context Protocol (MCP), an open standard that lets Claude query the provider's
  system directly rather than working off an uploaded copy. This matters in legal
  work, where confidentiality and privilege must be preserved end to end."
- **Our assessment**: The privilege protection claim is grounded in a concrete
  mechanism: "Connectors in Cowork honor the access controls already configured in
  your DMS or matter management system." This means privilege protection is inherited
  from the firm's existing iManage/NetDocuments/Box access controls, not from a
  separate AI-specific permission layer. This is architecturally significant — firms
  don't need to re-configure access controls for AI; they need to ensure their DMS
  controls are correctly configured. The guide pairs this with "Anthropic does not
  train on customer data" and "Enterprise plans support custom retention" as the
  three legs of the privilege protection argument.

### Claim 4: Subagents are distinct from Skills — they run in their own context window with their own system prompt and tool access, designed for bounded tasks that would overload a single context window or require tighter tool restrictions

- **Evidence**: PDF Chapter 1, "Subagents" section. Explicit comparison to Skills
  in the same section.
- **Confidence**: settled (first-party technical definition; authoritative on how
  the two components differ)
- **Quote**: "Where a skill tells Claude how to do something, a subagent is an agent
  that runs in its own context window with its own system prompt and tool access,
  completes one bounded job (check a citation, extract a clause, audit defined terms)
  and reports back."
- **Our assessment**: This is the most precise definition of subagents in the corpus.
  The key distinction from Skills: Skills encode a workflow (a set of instructions Claude
  follows within the same context), while Subagents execute as separate agents with
  independent context windows. The legal rationale ("let firms put tighter tool
  restrictions on the parts of a workflow that touch sensitive systems") gives a
  concrete security motivation — a citation-checking subagent should only have read
  access to legal databases, not write access to matter management systems. Plugins
  can "package subagents alongside skills and connectors so a practice area ships
  with the right helpers built in." This extends `blog-anthropic-cowork-deploy-guide.md`
  Claim 3 (which described the three-component plugin anatomy) by specifying what
  subagents are architecturally versus skills.

### Claim 5: Twelve legal practice-area plugins cover distinct practice domains with integrated workflow capabilities, including specialist areas like Law Student, Legal Clinic, and Legal Builder Hub not previously described

- **Evidence**: PDF Chapter 1, "Plugins" section — explicit bullet-point description
  of each plugin with specific capabilities listed. The guide states these "expand
  beyond our initial legal plugin launched in early 2026."
- **Confidence**: settled (first-party product specification; authoritative on what
  the plugins do)
- **Quote**: "Lawyers have different areas of expertise and focus. These plugins
  expand beyond our initial legal plugin launched in early 2026, aligned to more
  specific practice areas."
- **Our assessment**: The 12 plugins cover Commercial, Corporate, Employment,
  Privacy, Product, Regulatory, AI Governance, IP, and Litigation (specialized
  practice areas) plus three infrastructure/education plugins: Law Student
  (Socratic drilling without giving answers), Legal Clinic (client intake with
  "pedagogy dial per practice area that controls how much the plugin does versus
  how much the student does" — explicitly built within ABA Formal Op. 512), and
  Legal Builder Hub (a trust layer for finding, reviewing, and installing
  community-built legal skills with security review, license gate, and freshness
  check). The Legal Builder Hub is architecturally significant — it's a governed
  plugin registry within a plugin, effectively a trust layer for third-party
  skill ecosystems. The ABA Formal Op. 512 reference in the Legal Clinic plugin
  is notable: it demonstrates that Anthropic is building guardrails aligned to
  professional conduct rules, not just generic AI ethics frameworks.

### Claim 6: The cold-start problem for legal is addressed by using Claude to analyze existing ticket queues and inboxes before the pilot, turning the work backlog into a deployment roadmap

- **Evidence**: PDF Chapter 3 (Adoption roadmap), Phase 1 section. This extends
  the general cold-start solution with a legal-specific mechanism.
- **Confidence**: emerging (first-party prescriptive advice; the "ticket queue
  analysis" approach is specific and actionable but not backed by measured outcomes)
- **Quote**: "Next, use Claude to analyze your legal ticket requests to solve the
  cold start problem. Point Claude at your inbox, your ticket queues, and other
  work to figure out what Claude might be able to assist your department with."
- **Our assessment**: This is a more concrete cold-start solution than the general
  Cowork guide's "install pre-configured plugins" advice (Claim 7 in
  `blog-anthropic-cowork-deploy-guide.md`). The ticket-queue-analysis approach
  solves two problems simultaneously: it produces an evidence-based use-case
  prioritization (what does your team actually spend time on?), and it gives
  champions a reason to open Claude on day one. The guide's legal-specific cold-start
  example is the /nda-triage command: "If they open it, type /nda-triage, and get
  a clean redline in ninety seconds, they're more likely to return." The specific
  legal command (/nda-triage) makes this more concrete than the general Cowork
  guide's /morning-briefing example.

### Claim 7: Successful legal pilots follow a specific product surface sequence — Skills and plugins first (low-risk, high-reuse), then Microsoft 365 add-ins, then Claude Cowork for matter-level work at the back end

- **Evidence**: PDF Chapter 3, Phase 2 (Pilot) section. Explicit description of
  the product surface rollout sequence.
- **Confidence**: emerging (first-party prescriptive sequencing; rationale is
  provided but sequencing is vendor advice, not empirically derived from observing
  which sequences succeed vs. fail)
- **Quote**: "Skills and plugins come first because they are low-risk and high-reuse.
  The Microsoft 365 add-ins come next, extending what a pilot team has built into
  Word, Excel, PowerPoint, and Outlook. Claude Cowork tends to come in at the back
  end of the pilot, when the team is ready to move from single-document work to
  matter-level work that spans files and apps."
- **Our assessment**: This sequencing inverts the intuitive expectation (that Cowork,
  as the flagship product, would come first). The rationale is that Skills/plugins
  are document-type-specific and recoverable from errors more easily than multi-step
  Cowork sessions that "span files and apps." The M365 add-ins are positioned as a
  bridge — they extend the Skills the team has built into the document environment
  most lawyers already live in (Word/Outlook), without requiring new behavioral
  patterns. Cowork requires lawyers to adopt a new workflow pattern ("delegating a
  project to Claude and reviewing the result"), which is higher behavioral lift and
  better suited to teams that have already built trust through Skills/add-ins.

### Claim 8: Legal pilot success requires two measurable criteria — cycle time reduction on the pilot job AND keeper rate (how often lawyers keep Claude's draft without meaningful rewrite)

- **Evidence**: PDF Chapter 3, Phase 2 (Pilot) section. Explicit description of
  both metrics with rationale.
- **Confidence**: emerging (first-party prescriptive metrics; the dual-metric
  approach is well-reasoned but vendor-prescribed rather than empirically derived)
- **Quote**: "Time saved is a common metric, specifically tracking the team's cycle
  time on the pilot job before and after Claude. Another is how often a lawyer keeps
  Claude's draft without a meaningful rewrite. Together, these two criteria help you
  assess whether the pilot is working."
- **Our assessment**: The dual-metric approach is more rigorous than hours-saved alone.
  Cycle time is a workflow metric (speed); keeper rate is a quality metric (Claude's
  output is good enough to use as-is, not just as a starting point). Together they
  prevent two failure modes: a pilot that saves time but produces unusable drafts, and
  a pilot that produces high-quality drafts but takes longer than the manual process.
  Neither metric alone is sufficient. This is more operationally specific than the
  general Cowork guide's reliance on "hours saved" as the primary pilot metric
  (see `blog-anthropic-cowork-deploy-guide.md` Claim 9).

### Claim 9: Champion skill-authorship is the leading pilot success indicator — a privacy counsel building her own DPIA skill signals the pilot has crossed from tool use to workflow transformation

- **Evidence**: PDF Chapter 3, Phase 2 (Pilot) section. The specific example
  (privacy counsel building a DPIA skill) gives the general principle a legal-specific
  illustration.
- **Confidence**: emerging (consistent with the general Cowork deployment guide's
  same claim; adds legal-specific evidence)
- **Quote**: "Another strong signal that a pilot is working is when champions start
  to build their own skills. A privacy counsel takes the DPIA workflow she has been
  running by hand and turns it into a skill with the firm's template and approval
  flow embedded. That is now a skill the rest of the legal team can begin using
  immediately."
- **Our assessment**: This directly corroborates `blog-anthropic-cowork-deploy-guide.md`
  Claim 9 (champion skill-authorship as leading indicator) with a legal-specific
  example. The DPIA-skill example is more illustrative than the sales call-prep
  example in the general guide because it involves a compliance domain with
  genuine format requirements (firm template and approval flow embedded in the
  skill). The result — "a skill the rest of the legal team can begin using
  immediately" — illustrates the organizational leverage of the skill-authorship
  milestone: one privacy counsel's workflow becomes everyone's starting point.

### Claim 10: Skills compound across practice areas — commercial and employment contract review workflows share enough structure that the second practice group's deployment is faster than the first

- **Evidence**: PDF Chapter 3, Phase 3 (Scale) section. Explicit example of
  cross-practice-area skill adaptation.
- **Confidence**: emerging (first-party prescriptive observation; plausible given
  the structural similarity of contract review across domains, but no measured
  evidence of actual deployment speed differences)
- **Quote**: "Over time, skills begin compounding across teams. A skill built for
  one practice area can be adapted for another when their work shares structure.
  A commercial contract review workflow and an employment contract review workflow
  share most of their structure. Adding a second practice group usually goes faster
  than the first, and the firm's skill library grows."
- **Our assessment**: This is the legal-specific version of the "tribal knowledge
  codification" claim in `blog-anthropic-cowork-deploy-guide.md` Claim 13 and the
  "encoding institutional knowledge into systems that compound over time" framing in
  `blog-anthropic-building-enterprise-agents.md` Claim 2. The legal context adds
  specificity: skills compound because legal practice areas share document structure
  (contracts have clauses, parties, representations, risk language regardless of
  domain). The commercial-to-employment adaptation claim is a concrete, verifiable
  prediction — if it is true, the second practice group deployment should be
  measurably faster. The guide doesn't report measured data on this. It does,
  however, give a usable heuristic: identify the structural overlap before deciding
  which practice group to target second.

### Claim 11: Anthropic's legal team achieved specific time savings across four workflows — marketing review from 2-3 days to 24 hours; PIA from 2 hours to 30 minutes; contract redlining from hours to minutes

- **Evidence**: PDF Chapter 2 (Anthropic legal team case studies). Four specific
  workflows described with before/after metrics.
- **Confidence**: anecdotal (self-reported first-person Anthropic team accounts;
  specific and detailed, but single-team experience at the AI vendor themselves
  — promotional selection effects are high)
- **Quote**: "Turnaround time dropped from two to three days down to 24 hours after
  the tool went live. Lawyers still read every blog post; the self-review layer just
  clears the obvious issues so review time can go to the calls that require judgment."
- **Our assessment**: The four workflows (Marketing Material Self-Review, Outside
  Business Activity/COI review, PIA drafting, contract redlining) represent distinct
  legal workflow archetypes: gating/pre-screening, form-based decision support,
  template-driven drafting, and document comparison. Together they cover the most
  common types of in-house legal work. The metrics are plausible — a 4x speed
  improvement on PIAs (2 hours → 30 minutes) and marketing review (2-3 days → 24
  hours) is consistent with automation of the structure-following portions of the
  workflow, while keeping lawyers "read every blog post" maintains quality.
  The COI review workflow has no published metric — it's described qualitatively as
  "employees were previously spending significant time on routine COI form reviews."
  The redlining claim ("from hours to minutes per agreement") is the most dramatic
  ratio but also the least specific. These cases add to the Anthropic internal team
  portrait started in `blog-anthropic-cowork-deploy-guide.md` (Claim 14: the Legal
  plugin built in an afternoon) with operational metrics.

### Claim 12: ZDR (Zero Data Retention) is not available for Claude.ai and Claude Cowork because they are stateful products; custom retention down to 30 days is the minimum for those surfaces

- **Evidence**: PDF CIO FAQ, "Do you support Zero Data Retention (ZDR)?" section.
  Explicit distinction between stateful (Claude.ai / Cowork) and non-stateful
  (Platform / Code) products.
- **Confidence**: settled (first-party technical specification; product design
  constraint with explicit rationale)
- **Quote**: "ZDR is available on the Claude Platform (API) and Claude Code for
  approved customers. Claude.ai and Claude Cowork are stateful products—conversation
  history, Projects, and Cowork sessions require server-side storage to function—so
  ZDR does not apply there."
- **Our assessment**: This is an important constraint for regulated legal organizations
  — particularly firms that operate under data residency or sovereignty requirements.
  A law firm that requires ZDR for privileged client matters cannot use Claude.ai or
  Cowork directly; they must build on the Claude Platform (API) via Bedrock/Vertex/
  Foundry or use Claude Code. The 30-day minimum retention window for Claude.ai/Cowork
  Enterprise plans is the practical alternative. The guide explicitly acknowledges
  that firms "need workloads to run inside their own cloud perimeter typically build
  custom applications on the Claude Platform via Amazon Bedrock, Google Vertex AI, or
  Microsoft Foundry, rather than using Claude.ai or Cowork directly." This is novel
  to the corpus — no prior source note has explicitly documented which Claude surfaces
  support ZDR and which do not.

### Claim 13: Privilege protection rests on three pillars — MCP connectors honor existing DMS access controls, Anthropic doesn't train on customer data, and Enterprise plans support custom retention — not on AI-specific privilege controls

- **Evidence**: PDF CIO FAQ, "How is attorney-client privilege protected?" section.
  Three-pillar description.
- **Confidence**: settled (first-party product specification on the data handling
  and access control model; the three pillars are product facts, not contested claims)
- **Quote**: "Privilege protection rests on access control and data handling.
  Connectors in Cowork honor the access controls already configured in your DMS
  or matter management system."
- **Our assessment**: The privilege protection model is permission-inheritance, not
  a separate AI privilege layer. A firm that configures iManage or NetDocuments
  correctly (matter-level access control, folder-level entitlements) gets AI privilege
  protection as a byproduct of their existing DMS governance. The guide explicitly
  notes: "Firms working with privileged content typically pair this with firm-defined
  policies on which matters and document types can be processed." This shifts
  privilege protection from a product feature to an organizational policy requirement.
  The guide does not address the harder case: what happens when a lawyer uses Cowork
  to process a document they have DMS access to but that is under a common interest
  or joint defense privilege with another party outside the firm's DMS scope?
  That gap is not flagged in the guide.

### Claim 14: Legal organizations must establish a skills governance framework before scaling — quality control, pre-deployment testing, and post-deployment maintenance are not optional at scale

- **Evidence**: PDF Chapter 3, Phase 3 (Scale) Pro-tip section.
- **Confidence**: emerging (first-party prescriptive advice; the governance
  requirement follows logically from the claim that skills become shared
  infrastructure, but no empirical evidence of what happens when governance is absent)
- **Quote**: "Align as a team on an intentional governance framework to enable
  scaling with confidence and velocity. Have an understanding of how skills are
  quality-controlled, tested before being rolled out, and maintained after deployment
  to be kept up-to-date and functional."
- **Our assessment**: This is the governance gap identified in
  `blog-anthropic-cowork-deploy-guide.md` (note in Claim 13: "The guide doesn't
  address skill governance — review, versioning, deprecation") explicitly filled.
  The three-part governance model (quality control → pre-deployment testing →
  post-deployment maintenance) maps to software engineering's standard CI/CD model,
  applied to skills. The "kept up-to-date and functional" requirement is particularly
  important in legal: a regulatory monitoring skill that is not updated as regulations
  change will produce stale analysis without warning. Unlike software bugs that
  cause crashes, a stale skill produces confidently wrong output. The guide doesn't
  specify what "quality control" or "testing" look like in practice for skills —
  this is a gap the Smith should flag when synthesizing a chapter on skill governance.

### Claim 15: Legal pilots should avoid novel or high-stakes matters; document-heavy, standard-shape work with human review before shipping is the right pilot target

- **Evidence**: PDF Chapter 3, Phase 1 (Foundation) section. Explicit caution
  about pilot scope.
- **Confidence**: settled (sound risk management advice; consistent with AI deployment
  best practices across domains; stated as Anthropic's explicit recommendation)
- **Quote**: "Avoid piloting Claude on novel or high-stakes matters without strong
  human review."
- **Our assessment**: This is the clearest risk boundary in the guide. "Novel or
  high-stakes" covers two distinct risk categories: novelty (Claude has no prior
  examples to draw from in the skill/plugin, so outputs are less reliable) and
  stakes (consequences of error are high — malpractice exposure, client harm,
  regulatory violation). The guide's positive framing of the right pilot target —
  "Pick work that is document-heavy and standard-shape" — is the flip side: standard
  shape means the skill's playbook is well-defined and verifiable, and document-heavy
  means there are observable artifacts to review before output ships. The "for an
  in-house team, that might be NDA triage or PIA drafting; for a law firm, that could
  be diligence document review or first-draft research memos" guidance gives concrete
  starting points that fit this profile.

## Concrete Artifacts

### Five-Surface Claude Product Matrix for Legal (PDF Chapter 1)

```
Claude Product Matrix: When to Use What
(Anthropic, "Claude for the legal industry," May 15, 2026)

Surface             | Best for                                         | Primary users
--------------------|--------------------------------------------------|----------------------------
Claude.ai           | Conversational drafting, research, analysis      | All legal staff
Claude Cowork       | Cross-app matter work (files + multiple tools)   | All legal staff
Claude for M365     | In-place drafting, redlining across M365 suite   | All legal staff
Claude Platform     | Building custom CLM/e-discovery/matter mgmt apps | Legal engineering, legal tech vendors
Claude Managed      | Running custom agents as hosted cloud services   | Platform and legal engineering
Agents              | with scoped permissions and audit tracing        | teams

Key distinction: "The simplest distinction: Chat is for asking questions and
working with Claude in the moment. Cowork is for delegating a project to Claude
and reviewing the result."

Claude Managed Agents hosting model: Anthropic runs the agent with "long-running
sessions, scoped permissions, and audit trail handled for them." Example: "a Contract
Review agent might handle NDA triage across thousands of incoming agreements."
```

### 12 Legal Practice-Area Plugins (PDF Chapter 1)

```
Legal Practice-Area Plugins
(Anthropic, "Claude for the legal industry," May 15, 2026)

1. Commercial Legal — reviews vendor agreements, NDAs, SaaS subscriptions against
   playbook; tracks renewals, routes escalations, translates findings for business
   stakeholders. Separate positions for sales-side and purchasing-side work.

2. Corporate Legal — M&A diligence at scale: extracts issues from data room, builds
   disclosure schedules, drafts board consents, tracks closing checklist, runs
   tabular review across hundreds of agreements. Modular for deals, board work,
   public company governance, entity compliance.

3. Employment Legal — jurisdiction-aware: reviews hires/terminations, classifies
   workers, tracks leave deadlines, runs investigations, drafts policies with state
   supplements.

4. Privacy Legal — reviews DPAs against playbook, triages PIAs and DPIAs, drafts
   DSAR responses with correct statutory timeline, watches for drift between policy
   and practice.

5. Product Legal — reviews launches against framework, checks marketing claims for
   substantiation, triages "can we do this?" questions, "learns what actually blocks
   a launch at your company."

6. Regulatory Legal — watches regulatory feeds, filters by materiality threshold,
   diffs new rules against policy library, tracks gaps and comment deadlines, drafts
   proposed policy updates.

7. AI Governance Legal — triages AI use cases against governance tiers, runs impact
   assessments, reviews vendor AI terms, checks AI policy currency. Ships with
   "policy-starter skill that drafts a firm AI policy from published model policies."

8. IP Legal — trademark clearance, FTO triage, cease-and-desist drafting/response,
   DMCA takedowns, OSS compliance, IP clause review, invention intake screening,
   portfolio tracking. "Loud guardrails on anything that needs a specialist."

9. Litigation Legal — matter intake, portfolio tracking, legal holds, demand letters,
   subpoena triage, chronologies, depo prep, privilege logs, claim charts, brief
   drafting. Adapts to in-house, firm associate, or solo practice.

10. Law Student — "Socratic drilling that won't give you the answer, because the
    point is learning." Case briefing, outlining, IRAC grading, bar prep with
    jurisdiction distinctions.

11. Legal Clinic — client intake, deadline tracking, case memos, supervisor review
    queues. "Supervisors set a pedagogy dial per practice area that controls how much
    the plugin does versus how much the student does." Built within ABA Formal Op. 512.

12. Legal Builder Hub — finds, reviews, installs, updates community-built legal
    skills from registries like Lawvable, with "security review, license gate, and
    freshness check on every install. The trust layer for the open legal skills
    ecosystem."

Notes:
- Each role runs as a plugin in Cowork and M365 add-ins for desktop use.
- "Lawyers stay in the workflow, reviewing and approving the agent's outputs
  before anything moves downstream."
- Plugins are open-source; firms can "fork them to swap in their own playbooks
  and add approval workflows."
```

### Three-Phase Legal Adoption Roadmap (PDF Chapter 3)

```
Claude for Legal: Three-Phase Adoption Roadmap
(Anthropic, "Claude for the legal industry," May 15, 2026)

Phase        | Actions                                        | What to Expect
-------------|------------------------------------------------|---------------------------
Foundation   | Security and privilege review.                 | Champions reporting back use
             | Identify 2–3 champion teams.                   | cases. First "this saved me
             | Install pre-built plugins.                     | an hour" moments.
             | Connect 1–2 core systems                       |
             | (iManage/NetDocuments, Thomson Reuters/Ironclad)|
-------------|------------------------------------------------|---------------------------
Pilot        | Champions run real workflows.                  | Measurable time savings.
             | Weekly check-ins.                              | Champions building and
             | Measure against defined criteria.              | sharing custom skills.
             | Demo wins to adjacent practice groups.         | Pull from other teams.
-------------|------------------------------------------------|---------------------------
Scale        | Admin-provisioned plugin marketplace.          | Skills shared across practice
             | Encode pilot learnings as firm-wide skills.    | areas. New hires ramping on
             | Onboard the next wave of users.                | encoded workflows. Declining
             |                                                | support tickets for "how do
             |                                                | I do this."

Pilot sequencing: Skills/plugins → M365 add-ins → Cowork (back end of pilot only).
Pilot success criteria: (1) Cycle time before vs. after Claude. (2) Keeper rate:
  "how often a lawyer keeps Claude's draft without a meaningful rewrite."
Cold-start solution: Analyze existing ticket queues and inboxes before piloting.
Pilot scope constraint: "Avoid piloting Claude on novel or high-stakes matters
  without strong human review." Start with NDA triage or PIA drafting (in-house)
  or diligence document review or first-draft research memos (law firm).
```

### Anthropic Legal Team Case Studies (PDF Chapter 2)

```
Anthropic Legal Team — Four Claude Workflows
(Anthropic, "Claude for the legal industry," May 15, 2026)

MARKETING REVIEW (Marketing Material Self-Review Tool):
  Workflow: Marketers paste draft into Claude Project → Claude analyzes via skill
    capturing legal team's historical guidance → flags issues (publicity rights,
    overstated claims, statistical accuracy) with low/medium/high risk labels
    → suggests fixes before formal review ticket.
  At formal review: triage to right lawyer with pre-flagged issues attached.
  Metric: Turnaround from 2–3 days to 24 hours.
  Note: "Lawyers still read every blog post; the self-review layer just clears
    the obvious issues so review time can go to the calls that require judgment."

OUTSIDE BUSINESS ACTIVITY (COI Review):
  Workflow: Employee fills form (department, manager, proposed activity) → Claude
    analyzes against COI policy framework → sends recommendation to lawyers via
    Slack for approval.
  Before: "Employment lawyers were previously spending significant time on routine
    COI form reviews."
  After: "The recommendation lands in the legal team's queue with the analysis
    already completed." Claude asks for more information if needed before proposing
    outcome.
  Metric: Not quantified.

PRIVACY IMPACT ASSESSMENTS (PIA Drafting):
  Workflow: MCP servers connect Claude to Google Drive folder of prior PIAs + Skill
    capturing firm's format and issues to look for → lawyer asks Claude to read
    prior assessments, apply standard concerns, draft new PIA → lawyer reviews and
    finalizes.
  Metric: End-to-end time from roughly 2 hours to 30 minutes (4x improvement).

CONTRACT REDLINING:
  Workflow: Claude compares document versions in Google Docs and Microsoft 365,
    highlights changes, recommends language from firm's commercial playbook.
    Configured to work inside Google Docs with real-time comment-with-suggested-edits.
    Team writes skills for specific document types (NDAs, third-party vendor
    agreements).
  Metric: "Reduced redlining from hours to minutes per agreement."
```

### IT/CIO FAQ — Key Data Handling Facts (PDF Chapter 3)

```
Data Handling and Security Facts for Legal IT Leaders
(Anthropic, "Claude for the legal industry," May 15, 2026)

Hosting:
  - Claude.ai and Claude Cowork: SaaS hosted by Anthropic.
  - For in-perimeter workloads: Claude Platform via Amazon Bedrock, Google Vertex
    AI, or Microsoft Foundry.

Training: "Anthropic does not train on inputs or outputs from Enterprise Plan
  accounts using Claude.ai or Cowork."

Retention: "Enterprise plans support custom data retention, including zero-retention
  configurations, for both Claude.ai conversations and Cowork sessions."
  Minimum retention: "30 days" for Claude.ai and Cowork Enterprise.

ZDR: "ZDR is available on the Claude Platform (API) and Claude Code for approved
  customers. Claude.ai and Claude Cowork are stateful products—conversation history,
  Projects, and Cowork sessions require server-side storage to function—so ZDR
  does not apply there."

Identity and Access: "Enterprise plans include SSO via SAML, SCIM for user
  provisioning, role-based access controls, and admin-managed plugin marketplaces
  for both surfaces."

Certifications: "Anthropic is ISO/IEC 42001:2023 certified for responsible AI
  management and SOC 2 Type II audited."

DMS Integration: "Cowork connects to iManage, NetDocuments, Box, and more document
  management systems through MCP connectors. The connectors authenticate as the end
  user and respect entitlements at the matter and folder level, so Cowork only sees
  what the user already has access to."

Privilege: "Privilege protection rests on access control and data handling.
  Connectors in Cowork honor the access controls already configured in your DMS
  or matter management system."

Endpoint: "Cowork is a signed desktop application available for macOS and Windows.
  It runs as a standard user-space application, requires no kernel-level components."
  Can be managed via MDM.

Local file access: "Cowork only reads files in folders the user explicitly grants
  access to from inside the application. Access is scoped per user. There is no
  background indexing of the user's drive."

Admin policy management: "Plugins, skills, and connectors can be provisioned through
  admin-managed marketplaces in both Claude.ai and Claude Cowork rather than installed
  per user. This gives IT a single place to control which workflows are available and
  which approval steps are required before output moves downstream."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-cowork-deploy-guide.md` Claim 9 (champion skill-authorship as
    pilot leading indicator) — Claim 9 in this note provides the legal-specific
    illustration: a privacy counsel building a DPIA skill with "the firm's template
    and approval flow embedded."
  - `blog-anthropic-cowork-deploy-guide.md` Claim 5 (three-phase six-month deployment
    roadmap) — Claim 7 in this note corroborates the general pattern and adds
    legal-specific actions: privilege review, iManage/NetDocuments connectors, Thomson
    Reuters for research, ticket-queue analysis for cold-start.
  - `blog-anthropic-cowork-deploy-guide.md` Claim 7 (cold-start problem + 90-second
    solution) — Claim 6 in this note corroborates with /nda-triage as the legal-specific
    90-second example, and adds the ticket-queue-analysis method for identifying the
    right first use cases before the pilot.
  - `blog-anthropic-building-enterprise-agents.md` Claim 2 ("encoding institutional
    knowledge into systems that compound over time") — Claim 10 in this note
    corroborates with the legal-specific mechanism: skills compound across practice
    areas because adjacent practice groups share document structure.

- **Extends**:
  - `blog-anthropic-cowork-deploy-guide.md` Claim 3 (plugin anatomy: Skills +
    Subagents + Connectors) — Claim 4 in this note extends the Subagents definition
    with the legal rationale for their isolation: "let firms put tighter tool
    restrictions on the parts of a workflow that touch sensitive systems." The
    prior note described Subagents as "autonomous workflows Claude runs end to end";
    this note clarifies they run in their own context window with their own system
    prompt.
  - `blog-anthropic-cowork-deploy-guide.md` Claim 13 (tribal knowledge codification /
    governance gap flagged) — Claim 14 in this note fills that gap explicitly: the
    three-part governance model (quality control → pre-deployment testing → post-
    deployment maintenance) is now vendor-prescribed, not just flagged as absent.
  - `blog-anthropic-cowork-deploy-guide.md` Claim 14 (Anthropic Legal team case
    study: plugin built in an afternoon) — Claim 11 in this note extends with four
    specific workflows and concrete metrics, giving the full picture of how
    Anthropic's legal team uses Claude in daily practice.
  - `blog-anthropic-cowork-enterprise.md` (enterprise controls: SSO, SCIM, OTel,
    spend limits) — the CIO FAQ in this note extends with additional legal-specific
    data handling facts: ZDR availability distinction (stateful vs. non-stateful
    surfaces), DMS integration details (iManage, NetDocuments, matter-level
    entitlements), privilege protection mechanism, ISO/IEC 42001:2023 certification,
    SOC 2 Type II audit.

- **Contradicts**: None material. The general Cowork deployment guide's three-surface
  framework (Chat / Cowork / Code) in `blog-anthropic-cowork-deploy-guide.md` Claim 1
  is not contradicted — the legal guide's five-surface matrix (Chat, Cowork, M365,
  Platform, Managed Agents) extends it, adding the Microsoft 365, Platform, and
  Managed Agents surfaces relevant for legal organizations. No contradiction issue
  filed.

- **Novel** (not in prior corpus):
  - **Claude Managed Agents as a fifth surface** (Claim 2): The prior three-surface
    framework (Chat/Cowork/Code) in the general enterprise guide does not include
    Managed Agents. This is the first corpus source to describe Managed Agents as a
    distinct deployment model for legal work, with Anthropic running the agent runtime
    with scoped permissions and audit tracing.
  - **Subagent isolation rationale** (Claim 4): The prior corpus defines subagents
    (in blog-anthropic-cowork-deploy-guide.md Claim 3) without specifying why they
    run in their own context window. This source adds the explicit rationale: to prevent
    context window overload for long matters and to enable tighter tool restrictions
    on sensitive system-touching parts of the workflow.
  - **ZDR distinction between Claude surfaces** (Claim 12): No prior corpus source
    specifies which Claude surfaces support ZDR and which do not. This is the first
    explicit mapping: Platform and Code support ZDR; Claude.ai and Cowork do not
    (stateful products).
  - **Dual pilot success metric** (Claim 8): Cycle time + keeper rate as a paired
    measurement framework for legal AI pilots is not in any prior corpus source.
    The prior corpus relies primarily on hours-saved as the pilot success measure.
  - **12 detailed practice-area plugin descriptions** (Artifact): The full plugin
    catalog with specific capabilities per plugin, including Law Student, Legal Clinic
    (with ABA Formal Op. 512 compliance), and Legal Builder Hub (governed skill
    registry), is not in any prior corpus source.
  - **Pilot product surface sequence** (Claim 7): Skills/plugins → M365 add-ins →
    Cowork as an explicit sequencing rationale is not in any prior corpus source.
    The general Cowork guide describes phases but not product surface sequencing
    within a pilot.
  - **MCP DMS entitlement inheritance** (Claim 3, Claim 13): The specific mechanism
    by which privilege is preserved — connectors authenticate as the end user and
    "respect entitlements at the matter and folder level" — is not described in any
    prior corpus source.
  - **Ticket-queue analysis as cold-start solution** (Claim 6): Using Claude to
    analyze existing ticket queues and inboxes to identify pilot use cases before
    launch is not in any prior corpus source. The general Cowork guide recommends
    pre-configured plugins; this adds the ticket-queue-analysis as the upstream step
    that selects which plugins to pre-configure.

## Guide Impact

- **Chapter on Enterprise Deployment in Regulated Verticals (planned)**: Add the
  five-surface Claude product matrix (Claim 2 + product matrix artifact) as the
  starting decision framework for legal teams and other regulated organizations.
  The addition of Claude Managed Agents as a fifth surface — for high-volume, hosted
  agent workloads — updates the three-surface model in the general deployment chapter.

- **Chapter on Enterprise Deployment in Regulated Verticals (planned)**: Add ZDR
  distinction (Claim 12 + CIO FAQ artifact) as a constraint that determines whether
  an organization can use Claude.ai/Cowork directly or must build on the Platform.
  This is a hard architectural constraint, not a preference — firms with ZDR
  requirements for privileged matter files must use Platform via cloud partners.

- **Chapter on Enterprise Deployment in Regulated Verticals (planned)**: Add the
  privilege protection model (Claim 3 + Claim 13) as an example of how regulated
  industry controls are inherited from existing governance infrastructure (DMS access
  controls) rather than requiring new AI-specific privilege controls. This pattern —
  AI permissions inherit from existing enterprise permissions — likely generalizes to
  healthcare (HIPAA), finance (FINRA), and other regulated sectors.

- **Chapter on Plugin Architecture / MCP (Ch02 or planned)**: Add the Subagent
  isolation rationale (Claim 4) as the canonical technical explanation for when and
  why to use subagents vs. skills. The legal framing (tighter tool restrictions on
  sensitive-system-touching parts of a workflow) gives a security motivation that
  the general corpus has not previously stated explicitly.

- **Chapter on Plugin Architecture / MCP (Ch02 or planned)**: Add the 12 legal
  practice-area plugins (Artifact) as the most detailed example of how practice-area
  specialization can be encoded in plugins. The Legal Builder Hub plugin (a governed
  registry within a plugin) and the Legal Clinic plugin (with ABA-compliance
  guardrails) are architecturally interesting patterns that generalize beyond legal.

- **Chapter on Enterprise Deployment — Pilot Design (planned)**: Add the dual pilot
  success metric (Claim 8) as the recommended measurement framework for legal AI
  pilots. Cycle time + keeper rate captures both speed and quality, preventing the
  single-metric failure modes. This is more rigorous than the hours-saved approach
  in the general Cowork guide.

- **Chapter on Skill Governance (planned or to add)**: Add the three-part skill
  governance model (Claim 14: quality control → pre-deployment testing → post-
  deployment maintenance) as the required governance framework before scaling skills
  to department-wide use. The risk of stale legal skills (producing confidently wrong
  analysis as regulations change) is higher than in most other domains.

## Extraction Notes

- **Source is a blog post + linked 21-page PDF**: The blog post at the issue URL is
  ~400 words and serves as introduction; the substantive content is in the downloadable
  PDF. Both were fully read. All claims above come from the PDF unless noted as from
  the blog post. The PDF was extracted using PyMuPDF after download via WebFetch.
- **PDF structure**: 21 pages, 4 chapters: (1) Product overview, (2) How Anthropic's
  Legal team uses Claude, (3) Adoption roadmap (including CIO FAQ and segment use
  cases), (4) Getting started + Resources.
- **Issue #725 context**: The triage notes that issue #725 (filed May 12, mining-complete)
  covers the same legal practice-area plugins and MCPs with a focus on tool integration.
  This extraction focuses on the organizational deployment layer: product selection,
  adoption roadmap, infrastructure/privilege controls, and skill governance — the scope
  the triage designated as novel for this issue.
- **No sub-pages followed**: The guide's Resources section links to legal tutorials,
  a Claude skills catalog, and an open-source legal plugins GitHub repository. None
  were followed — the resources page describes these as external references, and the
  claims in this note are fully supported by the PDF.
- **Confidence calibration**: The FTI/Relativity statistics are third-party survey
  data (emerging). The product descriptions and privilege protection mechanism are
  first-party settled. The deployment roadmap and pilot metrics are first-party
  prescriptive (emerging — vendor advice, not externally validated). The Anthropic
  legal team case studies are anecdotal. Overall: **emerging**, because the most
  operationally useful claims rest on first-party prescriptions and self-reported case
  studies, not independently validated research.
- **No contradictions filed**: Reviewed open contradiction issues and CONTRADICTIONS.md.
  No material contradiction between this source and existing corpus notes. The
  five-surface matrix extends (not contradicts) the three-surface framework in
  blog-anthropic-cowork-deploy-guide.md.
