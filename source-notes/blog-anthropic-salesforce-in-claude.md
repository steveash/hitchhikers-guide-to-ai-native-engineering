---
source_url: https://claude.com/blog/salesforce-in-claude
source_type: blog-post
title: "Bringing Salesforce into Claude"
author: "Anthropic (first-party product announcement, joint with Salesforce)"
date_published: 2026-09-15
date_extracted: 2026-09-16
last_checked: 2026-09-16
status: current
confidence_overall: anecdotal
issue: "#3475"
---

# Bringing Salesforce into Claude

> First-party Anthropic/Salesforce product announcement for "Salesforce in Claude," a
> beta plugin bundling 37 pre-built skills, a Salesforce connector, and a Slack connector
> into a single officially packaged CRM integration — evidence that Salesforce/CRM context
> assembly has moved from practitioner-built custom MCP tooling (documented earlier in the
> corpus) to a vendor-shipped, admin-provisioned product.

## Source Context

- **Type**: blog-post (first-party product announcement, published jointly by Anthropic and
  Salesforce on claude.com, September 15, 2026)
- **Author credibility**: Corporate announcement, not a practitioner account. No named
  Anthropic author; credibility rests on the two named third-party endorsements (a customer
  CFO and Salesforce's own President/CRO) plus the specificity of the adoption figure (7,000
  sellers). As a vendor announcement, treat feature claims as accurate descriptions of what
  shipped, but treat the adoption/impact framing ("seconds instead of hours") as marketing
  language rather than measured outcomes.
- **Scope**: Covers what the plugin is (37 skills, Salesforce + Slack connectors, setup
  skill), the five core workflows it enables (morning brief, call prep, deal review/close
  planning, post-call CRM updates, pipeline dashboard), the permission/approval model, three
  named customer deployments (GitLab, Siemens, Legora — only Legora is quoted directly), the
  7,000-seller adoption figure, and how admins install it (AgentExchange, Salesforce MCP via
  marketplace). Does NOT cover: technical implementation of the Salesforce connector, pricing,
  security/compliance review process, how the 37 skills were authored, or any quantified
  before/after time-savings data (the CFO quote uses "seconds instead of hours" but no number
  is given).

## Extracted Claims

### Claim 1: Salesforce in Claude is an officially co-built plugin (not a customer-assembled MCP integration) bundling 37 skills for daily account-executive work

- **Evidence**: Direct product description in the opening paragraph, naming the skill count
  and the core use cases.
- **Confidence**: settled (first-party, unambiguous product description)
- **Quote**: "Today we are releasing Salesforce in Claude in beta, a plugin built with Salesforce that brings a seller's accounts, opportunities, and pipeline into Claude under their existing Salesforce permissions. It includes 37 skills for the work account executives do daily, including account research, call prep, pipeline review, and CRM updates."
- **Our assessment**: This is the headline novelty of the source. The corpus already documents Salesforce/CRM context assembly built ad hoc by individual practitioners with Claude Code and custom MCP servers (`blog-anthropic-sires-gtm-claude-code.md` Claim 9: a 7-system `/customer-context` skill including Salesforce, built by one non-technical GTM PM) and by a sales leader using Cowork with Salesforce+BigQuery MCP connectors he configured himself (`blog-anthropic-bryant-cowork-sales.md`, Concrete Artifacts). This source represents the next maturation step: Anthropic and Salesforce jointly shipping the equivalent capability as a pre-built, 37-skill plugin that any seller can install without building anything. The practitioner-build-then-vendor-productize arc is now visible end to end in the corpus.

### Claim 2: The plugin operates strictly under the seller's existing Salesforce permissions, reading only what they're already authorized to see

- **Evidence**: Explicit statement of the read-permission model, echoing the general Cowork connector permission model.
- **Confidence**: settled (first-party technical/policy claim)
- **Quote**: (no direct quote recovered verbatim for "reads only what their permissions allow"; WebFetch reported this as the article's characterization of the permission model — see Extraction Notes)
- **Our assessment**: This is not a novel permission model — it is the same "Claude sees what the user sees" connector principle already documented in `blog-anthropic-cowork-deploy-guide.md` Claim 3 ("connectors respect your existing permissions"). What's new is a concrete named instance: a specific enterprise SaaS system (Salesforce) with row/field-level permission structures now has an officially supported connector that inherits those exact permissions rather than requiring a separate access-grant model. This is a positive proof point for the "connectors under existing permissions" pattern scaling to a major third-party enterprise system.

### Claim 3: Sellers spend hours per day manually assembling meeting prep and follow-up information scattered across Salesforce, email, call recordings, and Slack

- **Evidence**: Stated problem framing that motivates the product.
- **Confidence**: anecdotal (vendor's framing of the problem, not an independent survey)
- **Quote**: "Sellers often spend hours of their day on meeting prep or follow-up work from customer meetings by manually assembling information scattered across Salesforce, email, call recordings, and Slack."
- **Our assessment**: This is the standard "surrounding work first" framing seen throughout the corpus's GTM/sales sources — the pain point is context assembly across fragmented systems, not deal strategy itself. It corroborates the same problem statement independently described by both Sires (`blog-anthropic-sires-gtm-claude-code.md`, "It was almost impossible to manage my inbox") and Bryant (`blog-anthropic-bryant-cowork-sales.md` Claim 10, "data assembly, report formatting... used to fill my week"), now generalized as the industry-wide justification for a vendor-shipped product rather than a single practitioner's anecdote.

### Claim 4: A personalized morning brief synthesizes the day's meetings, deals closing soon, at-risk opportunities, and unread threads needing a reply

- **Evidence**: Direct feature description.
- **Confidence**: settled (product feature description)
- **Quote**: "Each morning Claude delivers a personalized brief that includes the day's meetings, deals closing soon, at-risk opportunities, and unread threads that need a reply."
- **Our assessment**: This four-part brief composition (calendar + at-risk pipeline + comms backlog) is functionally identical in shape to the "daily brief" skill in `blog-anthropic-sires-gtm-claude-code.md` (Concrete Artifacts → Daily Workflow Skills Stack) and the scheduled call-prep/conference-room skills in `blog-anthropic-bryant-cowork-sales.md` Claim 1, but this version is a packaged, vendor-shipped default rather than a practitioner-authored skill. It confirms the "scheduled multi-source morning synthesis" pattern is now common enough to standardize as an out-of-box feature.

### Claim 5: Call prep assembles open opportunity status, this week's account-team discussion, unanswered threads, and open questions from prior calls by pulling from Salesforce, Slack, and email in one request

- **Evidence**: Direct feature description of the call-prep workflow.
- **Confidence**: settled (product feature description)
- **Quote**: "A seller can ask Claude to prep for their next meeting and it pulls the brief from Salesforce, Slack, and email: open opportunities and where each stands, what the account team discussed this week, unanswered threads, and questions still open from previous calls."
- **Our assessment**: This is a narrower, three-system version of the seven-system `/customer-context` skill in `blog-anthropic-sires-gtm-claude-code.md` Claim 9 (Salesforce, Intercom, Gong, Calendar, Gmail, Drive, BigQuery in ~90 seconds). The vendor product covers fewer systems (Salesforce, Slack, email vs. seven) but ships as a zero-configuration default, illustrating a tradeoff practitioners should note: officially packaged plugins trade integration breadth for install-in-minutes simplicity, while custom-built skills can integrate more systems at the cost of requiring an internal builder.

### Claim 6: Pointed at a specific opportunity, Claude scores the deal against the team's sales methodology, surfacing qualification gaps, unmet stakeholders, and close-date risk factors

- **Evidence**: Direct feature description of deal review/close-plan scoring.
- **Confidence**: settled (product feature description)
- **Quote**: "Pointed at an opportunity, Claude scores the deal against the team's methodology, considering qualification gaps, stakeholders they haven't met, and factors putting the close date at risk."
- **Our assessment**: This is a deal-level analogue to the account-level propensity scoring in `blog-anthropic-bryant-cowork-sales.md` Claim 4 (a five-dimension rubric per account). Both instances demonstrate the same pattern — encode a team's qualitative sales judgment into a scoring rubric Claude applies consistently — but this source applies it live, per-opportunity, on demand, whereas Bryant's is a batch overnight run across 4,000 accounts. Together they show the scoring-rubric pattern working at two different scales/cadences (on-demand single-deal vs. batch full-territory).

### Claim 7: After each call, Claude converts the transcript or the seller's notes into a follow-up email, a Slack deal-channel summary, and draft Salesforce opportunity field updates (next steps, stage, close date) for the seller to review before anything is written

- **Evidence**: Direct feature description of the post-call workflow, including the explicit human-review step.
- **Confidence**: settled (product feature description)
- **Quote**: "After each call, Claude turns the transcript or the seller's notes into a follow-up email, a summary for the deal channel in Slack, and drafts opportunity updates like next steps, stage, and close date, for the seller to review."
- **Quote**: "Claude asks the seller to approve each proposed change before it's written."
- **Our assessment**: The explicit "review before it's written" gate is the same human-in-the-loop-before-anything-ships posture documented in `blog-anthropic-bryant-cowork-sales.md` Claim 9 ("the human-in-the-loop pattern is built in so Claude proposes and I approve before anything ships"). Its presence in a vendor-shipped default (not a practitioner's personal choice) suggests Anthropic/Salesforce are treating approval-before-write as the required default posture for CRM-writing agents, not an optional configuration — worth flagging in any guide chapter on agent write-permissions to production systems of record.

### Claim 8: A seller can request an interactive pipeline dashboard showing stage coverage, deals likely to slip and why, with account-level drill-down

- **Evidence**: Direct feature description of the pipeline-review workflow.
- **Confidence**: settled (product feature description)
- **Quote**: "A seller can ask for a pipeline view and Claude builds an interactive dashboard showing coverage by stage, deals most likely to slip and why, and drill-down by account."
- **Our assessment**: This is the same "build a dashboard from analytical results" skill-chaining pattern documented in `blog-anthropic-bryant-cowork-sales.md` Claim 7 (propensity-scoring output → interactive per-AE territory dashboard). Here the dashboard is generated on demand from live pipeline data rather than from a completed batch scoring run, but the underlying pattern — turn structured Claude output into an interactive, drillable visualization — is identical.

### Claim 9: David Eckstein, CFO of Legora, reports sellers turning live data into meeting briefings "in seconds instead of hours," with new reps starting with a full account picture

- **Evidence**: Named customer quote, attributed with title.
- **Confidence**: anecdotal (single customer executive quote, vendor-supplied, no independent metrics)
- **Quote**: "With Salesforce in Claude, our sellers turn live data into meeting briefings in seconds instead of hours. As our sales team grows, every new rep starts with a full picture of the law firms we serve."
- **Our assessment**: "Seconds instead of hours" is a qualitative, non-quantified claim — consistent in direction with the quantified estimates elsewhere in the corpus (Sires' 2–3 hours/day on email, Bryant's ~90 min/day and ~3 hrs/week on prep/reporting) but weaker evidentially since no number accompanies it. The second sentence (new-rep onboarding benefit) is a distinct claim worth separating: pre-built context-assembly tooling may lower the account-history ramp-up cost for new hires, not just save time for existing reps — this onboarding angle is not present in the Sires or Bryant sources.

### Claim 10: Alexa Vignone, President and Chief Revenue Officer at Salesforce, frames the plugin's value as returning reclaimed prep time directly to customer conversations

- **Evidence**: Named executive quote from the partner company (Salesforce), not Anthropic.
- **Confidence**: anecdotal (partner-company executive endorsement, vendor-supplied)
- **Quote**: "With Salesforce in Claude, sellers can start the day with the pipeline review already done and the account history already there. That time goes straight back into customer conversations."
- **Our assessment**: This is the identical "give back the hours for customer conversations" framing as `blog-anthropic-bryant-cowork-sales.md` Claim 10 ("Sales is full of people who got into the job for the customer conversations. Claude Cowork can give them back the hours to do just that.") — now voiced by Salesforce's own CRO rather than an Anthropic GTM employee. Two independent organizations converging on the same "time reclaimed → customer conversations" narrative strengthens it as the dominant framing for AI-driven sales tooling, though both instances remain promotional rather than measured.

### Claim 11: The plugin has been deployed by three named customers — GitLab, Siemens, and Legora — with roughly 7,000 Salesforce sellers using it

- **Evidence**: Named customer list plus a specific adoption figure.
- **Confidence**: anecdotal (self-reported adoption figure; no independent verification; customer names given without individual GitLab/Siemens quotes or usage detail — only Legora is quoted)
- **Quote**: "7,000 Salesforce sellers use it in their work." (as characterized by extraction; see Extraction Notes on verbatim confidence)
- **Our assessment**: 7,000 sellers across three named enterprise customers (GitLab, Siemens — both engineering-heavy orgs with dedicated sales motions; Legora, a legal-tech company) is a meaningfully larger deployment figure than any single-practitioner or single-team case study elsewhere in the corpus (contrast with Sires' single sales org's ~80% adoption or Bryant's single 4,000-account book). This is the first corpus source documenting CRM-integrated Claude usage at multi-customer, multi-thousand-seat scale rather than within Anthropic's own sales org.

### Claim 12: Admins provision the plugin organization-wide by connecting Salesforce once and requesting access through AgentExchange; sellers then sign in with their own Salesforce credentials

- **Evidence**: Direct description of the getting-started/admin provisioning flow.
- **Confidence**: settled (first-party product/process description)
- **Quote**: "The Salesforce MCP is available to install directly through the marketplace today. To install the plugin, admins can request access through AgentExchange" and connect Salesforce for their organization. (compound: first clause verbatim, second clause paraphrased by extraction — see Extraction Notes)
- **Our assessment**: This is a concrete instance of the "bottom-up discovery, top-down scale" deployment pattern in `blog-anthropic-cowork-deploy-guide.md` Claim 8 — an admin connects the system once organizationally, then individual sellers get scoped access under their own credentials/permissions rather than a shared service account. Notably, distribution runs through AgentExchange (Salesforce's own platform marketplace) as well as the Claude/MCP marketplace — a dual-marketplace distribution model not previously documented in the corpus, where the integration is discoverable from either vendor's ecosystem.

### Claim 13: On Team and Enterprise plans, Anthropic does not train its models on customer data by default

- **Evidence**: Direct data-usage policy statement included in the announcement.
- **Confidence**: settled (first-party policy statement)
- **Quote**: "On Team and Enterprise plans, we don't train our models on your data by default."
- **Our assessment**: A standard enterprise-trust reassurance, included here because Salesforce data is especially sensitive (customer PII, deal terms, pricing). Not novel to the corpus as a policy statement, but its explicit inclusion in a CRM-specific product announcement signals that data-training concerns are treated as a first-order adoption blocker for connecting Claude to systems of record — worth citing in any guide chapter addressing enterprise data-governance objections to agentic CRM access.

## Concrete Artifacts

### Salesforce in Claude — Product Summary (from article)

```
Salesforce in Claude (beta) — Anthropic + Salesforce joint plugin
Published: September 15, 2026
Availability: All paid Claude plans

COMPONENTS:
  Salesforce connector — reads/writes Salesforce data under seller's existing permissions
  Slack connector      — deal-channel summaries, account-team threads
  Setup skill          — identifies a seller's tools, creates a tailored Claude Artifact
  Salesforce MCP       — installable directly via the marketplace

SKILL COUNT: 37 skills for daily account-executive work

CORE WORKFLOWS:
  1. Morning brief    — meetings, deals closing soon, at-risk opportunities, unread threads
  2. Call prep        — pulls Salesforce + Slack + email: open opps, account-team discussion,
                         unanswered threads, open questions from prior calls
  3. Deal review / close plan — scores deal against team methodology: qualification gaps,
                         unmet stakeholders, close-date risk factors
  4. Post-call update  — transcript/notes -> follow-up email + Slack deal-channel summary +
                         draft opportunity field updates (next steps, stage, close date);
                         seller approves before anything is written
  5. Pipeline review   — interactive dashboard: coverage by stage, slip-risk deals, drill-down
                         by account

PERMISSION MODEL:
  - Operates under seller's existing Salesforce permissions (reads only what's authorized)
  - Default approval workflow: Claude proposes, seller approves before any write
  - No default model training on Team/Enterprise plan data

DEPLOYMENT:
  - Admin connects Salesforce once, organization-wide; access controlled per user group
  - Distribution: AgentExchange (Salesforce marketplace) + Salesforce MCP via Claude/MCP
    marketplace
  - Setup guide: support.claude.com

ADOPTION (named customers):
  GitLab, Siemens, Legora — ~7,000 Salesforce sellers using it
```

### Named Quotes (from article)

```
David Eckstein, CFO, Legora:
"With Salesforce in Claude, our sellers turn live data into meeting briefings in seconds
instead of hours. As our sales team grows, every new rep starts with a full picture of
the law firms we serve."

Alexa Vignone, President and Chief Revenue Officer, Salesforce:
"With Salesforce in Claude, sellers can start the day with the pipeline review already
done and the account history already there. That time goes straight back into customer
conversations."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-bryant-cowork-sales.md` Claim 9 (human-in-the-loop approval before
    anything ships) and Claim 10 (reclaimed time redirected to customer conversations) —
    both patterns appear here verbatim in a vendor-shipped default rather than a single
    practitioner's chosen configuration, strengthening them from "one GTM leader's practice"
    to "the standard Anthropic/Salesforce-endorsed posture for CRM-writing agents."
  - `blog-anthropic-cowork-deploy-guide.md` Claim 3 (connectors respect existing permissions;
    "Claude sees what the user sees") — corroborated with a concrete, named enterprise system
    (Salesforce) rather than a generic connector description.
  - `blog-anthropic-cowork-deploy-guide.md` Claim 8 (bottom-up discovery, top-down scale via
    admin-managed plugin marketplaces) — corroborated by the admin-connects-once /
    per-user-group-access provisioning flow described here.
  - `blog-anthropic-sires-gtm-claude-code.md` Claim 3 (web search keeps AI-generated
    communications current without manual synchronization) and the general "surrounding work
    first" problem framing shared with `blog-anthropic-bryant-cowork-sales.md` Claim 10 —
    this source's opening problem statement (hours lost to manually assembling scattered
    Salesforce/email/call/Slack information) restates the same pain point independently.

- **Contradicts**: None identified. No existing source note makes a claim that materially
  opposes anything in this source. No contradiction issue filed.

- **Extends**:
  - `blog-anthropic-sires-gtm-claude-code.md` Claim 9 (`/customer-context`, a practitioner-
    built 7-system, 90-second account-context skill) — this source extends the corpus with
    the vendor-productized counterpart: the same category of capability (multi-system sales
    context assembly), now shipped as an official 37-skill plugin rather than built by one
    non-technical GTM PM with Claude Code and custom MCP servers. Narrower system coverage
    (Salesforce + Slack + email vs. seven systems) but zero-build-effort adoption.
  - `blog-anthropic-bryant-cowork-sales.md` Claim 4 (two-tier account propensity scoring
    rubric) and Claim 7 (dashboard-from-results skill chaining) — this source extends both
    patterns to on-demand, per-deal/live-pipeline application (vs. Bryant's overnight
    batch/quarterly cadence), showing the scoring-rubric and dashboard-chaining patterns
    generalize across cadences.
  - `blog-anthropic-cowork-deploy-guide.md` Concrete Artifacts → "Anthropic Internal Team Case
    Studies Summary" → SALES section — extends the previously Anthropic-internal sales
    archetype (morning briefing, call prep, follow-up, competitive intel, asset creation) to
    an externally-shipped, multi-customer product with the same workflow shape.

- **Novel**:
  - **Vendor co-branded, officially packaged CRM plugin as a distinct maturity stage**: no
    prior corpus source documents a joint Anthropic + third-party-SaaS-vendor plugin shipped
    as a paid-plan default feature (vs. an internally-built Anthropic tool or an individual
    practitioner's custom MCP integration). This is the first "productized by both vendors"
    instance in the corpus.
  - **Dual-marketplace distribution** (AgentExchange + Claude/MCP marketplace): distributing
    the same integration through both the AI vendor's marketplace and the SaaS vendor's own
    platform marketplace is a new distribution pattern not seen in prior sources.
  - **Multi-customer, multi-thousand-seat adoption figure outside Anthropic's own org**:
    7,000 sellers across three named external customers (GitLab, Siemens, Legora) is the
    first corpus data point on CRM-integrated Claude usage at this scale outside Anthropic's
    internal sales team (contrast with Sires' ~80% of one company's sales org, or Bryant's
    single 4,000-account book).
  - **New-hire onboarding benefit from pre-built account context** (Claim 9, Eckstein quote's
    second sentence): the framing that new reps "start with a full picture" of served
    accounts from day one is a distinct onboarding-acceleration benefit not articulated in
    the Sires or Bryant sources, which focus on existing-rep time savings.

## Guide Impact

- **Chapter on Context Assembly / MCP Integration (Ch04)**: Add "Salesforce in Claude" as the
  vendor-productized endpoint of the CRM-context-assembly pattern already documented via
  practitioner builds (`blog-anthropic-sires-gtm-claude-code.md`, `blog-anthropic-bryant-cowork-sales.md`).
  Frame the guide's advice as a build-vs-buy tradeoff: officially packaged plugins trade
  integration breadth (3 systems here vs. 7 in the custom `/customer-context` skill) for
  zero build effort and org-wide admin provisioning; teams needing broader system coverage
  should still expect to build custom MCP integrations.

- **Chapter on Enterprise & Team Adoption (Ch05/Ch06)**: Add the dual-marketplace distribution
  model (AgentExchange + Claude/MCP marketplace) as a new example of how AI-vendor and
  SaaS-vendor ecosystems can co-distribute an integration, alongside the existing
  admin-provisioning pattern in `blog-anthropic-cowork-deploy-guide.md` Claim 8.

- **Chapter on Agent Write-Access to Systems of Record (Ch02/harness-engineering)**: Cite the
  explicit "Claude asks the seller to approve each proposed change before it's written" gate
  as a vendor-default (not optional) posture for any agent capable of writing to a CRM or
  other system of record. Pair with `blog-anthropic-bryant-cowork-sales.md` Claim 9 to show
  this posture is now both a practitioner's personal choice and a shipped-product default.

- **Chapter on Enterprise Data Governance objections (Ch05/Ch06)**: Add the explicit
  "we don't train our models on your data by default" statement (Claim 13) as the standard
  reassurance pattern accompanying agentic access to sensitive systems of record —
  practitioners pitching similar CRM integrations internally should expect this objection
  and have the same answer ready.

## Extraction Notes

- The source was read via three targeted WebFetch passes (the raw page could not be rendered
  to plain text in one pass by the fetch tool, so extraction was triangulated across
  multiple prompts targeting specific sections and exact wording).
- Most feature-description quotes (Claims 1, 3-8, 13) were returned by WebFetch as clean,
  directly-quoted sentences and are treated as verbatim.
- Two items are flagged as lower-confidence on verbatim wording: Claim 2 (the "reads only
  what their permissions allow" phrasing was returned by the fetch tool as its own
  characterization in one pass, not consistently reproduced as a standalone quoted sentence
  in the follow-up verification pass) and Claim 12's second clause (admins "connect
  Salesforce for their organization" was paraphrased by the fetch tool rather than returned
  as an exact quoted sentence). Both are marked in their Quote fields rather than presented
  as clean verbatim quotes, per the no-fabrication rule.
  Claim 11's "7,000 Salesforce sellers" figure was consistently returned across both fetch
  passes with matching phrasing ("7,000 Salesforce sellers use it in their work" /
  "7,000 Salesforce sellers currently using the plugin") and is treated as reliable, though
  the exact original sentence structure in the source could not be independently confirmed
  beyond the fetch tool's renderings.
  A third pass specifically asked for verbatim sentences naming GitLab or Siemens; none was
  returned — the fetch tool reported only that Legora was directly quoted, with GitLab and
  Siemens appearing to be named as customers without individual attributed quotes in the
  source. Do not attribute customer-specific outcomes to GitLab or Siemens beyond "named
  customer."
- No sub-pages were linked from the article requiring follow-up (the "Getting started"
  section references support.claude.com and AgentExchange as external platforms, not
  in-guide sub-pages worth extracting separately).
- Checked all overlapping notes named by the Prospector triage comments
  (`blog-anthropic-sires-gtm-claude-code.md`, `blog-anthropic-cowork-deploy-guide.md`,
  `blog-anthropic-bryant-cowork-sales.md`, `blog-anthropic-claude-code-skills-lessons.md`,
  `blog-anthropic-building-enterprise-agents.md`, `blog-anthropic-claude-tag-employee-workflows.md`).
  No material contradiction found; the relationship throughout is extension/corroboration
  (custom practitioner build -> vendor productization of the same pattern). No contradiction
  issue filed.
- Confidence set to `anecdotal` overall: while several claims (product feature descriptions,
  policy statements) are `settled` first-party facts about what shipped, the source's
  headline value claims (time savings, adoption impact) rest on two vendor-supplied
  executive quotes with no independent measurement, consistent with how the corpus treats
  other first-party GTM/sales announcements.
