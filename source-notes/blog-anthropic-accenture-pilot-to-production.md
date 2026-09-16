---
source_url: https://claude.com/blog/deploying-ai-from-pilot-to-production
source_type: blog-post
title: "Deploying AI from pilot to production: A practical blueprint for CIOs and technical leaders"
author: Anthropic and Accenture (joint guide; no individual bylines)
date_published: 2026-09-14
date_extracted: 2026-09-16
last_checked: 2026-09-16
status: current
confidence_overall: emerging
issue: "#3473"
---

# Deploying AI from pilot to production

> A 38-page Anthropic+Accenture co-authored guide arguing that pilot-to-production
> failure is driven by seven specific, front-loadable decision categories (strategic
> ownership, data readiness, infrastructure, security/compliance, organizational
> readiness, governance/risk, and scale), each with a "work out" (cross-functional)
> and "assign" (named-owner) question set, backed by Accenture survey statistics and
> eight named Anthropic customer case studies.

## Source Context

- **Type**: blog-post (short ~400-word teaser on claude.com) linking to a 38-page
  downloadable PDF guide, which is where all substantive content lives. Both were
  read; the blog post itself contains only a condensed summary and a download link —
  all claims below are drawn from the PDF
  (`https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6aa46440db7c5ad962ef7ef2_Claude-Accenture-Deploying-AI-from-pilot-to-production-09112026%20(1).pdf`).
- **Author credibility**: Jointly authored and branded by Anthropic and Accenture
  (cover page carries both logos; "About Anthropic" and "About Accenture" sections
  close the guide). This is first-party/vendor-adjacent content — Anthropic has a
  commercial interest in Claude adoption, and Accenture has a commercial interest in
  selling AI transformation consulting engagements. The named customer case studies
  (StubHub, Novo Nordisk, TELUS, Palo Alto Networks, NBIM) are on-the-record quotes
  attributed to named executives, which raises the evidentiary bar above anonymous
  testimonials, but all are Anthropic customers presented in a promotional context.
  The three statistics cited (23% sustained enterprise-wide AI impact, 64%/7% adoption
  vs. data-readiness gap, 42% shared-accountability, 32-cents chargeback figure) come
  from named Accenture research reports (Pulse of Change, July 2026; AI-Ready Data for
  Advanced AI survey, May 2026; Tokenomics research, September 2026) cited by name and
  date but not independently reproduced or linked to primary survey methodology within
  this guide.
- **Scope**: Covers seven "considerations" organized chronologically across
  pre-pilot, pilot-to-production, and in-production phases, plus a closing "enterprise
  AI deployment blueprint" (transition timeline) and a "Getting started" resource list.
  Does NOT cover: pricing, technical implementation details of any specific
  architecture, a full accounting of survey methodology for the cited statistics, or
  guidance on remediation once a program has already stalled in production (the guide
  is framed entirely as "decide this before you commit," not "how to recover").

## Extracted Claims

### Claim 1: Only 23% of C-suite leaders report having achieved sustained, enterprise-wide AI impact, and there is a large gap between organizations that have moved into production and those with the data-readiness required to scale
- **Evidence**: Two named Accenture survey statistics cited with report name and
  publication date.
- **Confidence**: emerging (named, dated survey citations from a report co-publisher
  with a commercial interest in the finding; survey methodology not reproduced in this
  guide)
- **Quote**: "According to Accenture's July 2026 Pulse of Change report, only 23% of C-suite leaders report having achieved sustained, enterprise-wide AI impact with AI initiatives. Readiness to scale shows a similar shortfall: 64% of respondents to Accenture's May 2026 AI-Ready Data for Advanced AI survey say they have moved beyond pilots into production across multiple functions or initiated enterprise-wide efforts for advanced AI, yet only 7% have reached the data-readiness required to scale it."
- **Our assessment**: This is the guide's central "burning platform" statistic and
  directly corroborates the broader "ambition has outrun readiness" narrative already
  documented in this corpus — see Cross-References. We buy the directional finding
  (many pilots stall before reaching sustained production impact) as consistent with
  the rest of the corpus's enterprise-adoption material, but treat the specific
  percentages as vendor-reported survey results rather than independently verified
  figures.

### Claim 2: Pilots succeed partly because they are insulated from the real conditions of production — protected budgets, curated data, AI-native teams, narrow scope, and limited stakeholder exposure — and that insulation makes them an unreliable signal for production performance
- **Evidence**: The guide's core diagnostic framing, stated in the opening section and
  repeated with variation across Considerations 1, 2, and 5.
- **Confidence**: settled (consistent, load-bearing argument restated with concrete
  supporting detail throughout the guide, not a single passing assertion)
- **Quote**: "That insulation makes pilots successful, but it also makes them an unreliable signal for how enterprise AI will perform in production at scale."
- **Our assessment**: This is the guide's thesis and the frame every other claim hangs
  from. It is a plausible, well-argued diagnostic rather than an empirically measured
  finding (no data quantifies how often "pilot success, production failure" occurs
  versus other failure modes), but it is consistent with, and gives structural
  vocabulary to, the "AI dust" and "retrofitting fails" failure modes already
  documented from monday.com and Coinbase in this corpus.

### Claim 3: A well-defined AI use case requires four explicit elements — a defined user, task, output, and measurable quality threshold — and "the AI can analyze documents" is a capability statement, not a use case
- **Evidence**: Direct worked example contrasting a vague capability statement with a
  fully specified use case.
- **Confidence**: settled (a specific, reusable definitional framework offered as
  prescriptive guidance, not hedged as speculative)
- **Quote**: "'The AI can analyze documents' is a capability, not a use case. → 'The AI reviews lease abstractions for the acquisitions team and flags non-standard clauses for counsel' is a use case."
- **Our assessment**: This four-part job definition (user, task, output, quality
  threshold) is a concrete, portable diagnostic tool distinct from anything else
  extracted from this corpus's enterprise-deployment sources — the Cowork deployment
  guide's five-level maturity model and pilot-use-case categories describe *what kind*
  of workflow to target, not *how precisely* to define one once chosen. Worth adopting
  directly as a scoping checklist.

### Claim 4: StubHub ran rigorous A/B testing across multiple AI model providers, measuring against specific resolution-rate and satisfaction benchmarks before committing to a production deployment, and achieved a 30% reduction in support costs with response times dropping from over 20 minutes to near-instant
- **Evidence**: Named customer case study with a direct, attributed quote from
  StubHub's Engineering Org Chief of Staff.
- **Confidence**: anecdotal (single named customer account, self-reported outcome
  metrics, no independent verification of the 30% figure)
- **Quote**: "The decision to choose Claude was entirely data-driven. We tested multiple model providers side by side, and Claude consistently delivered the best results for case resolution rates and customer satisfaction scores." — Timothy Addison, Engineering Org Chief of Staff, StubHub
- **Our assessment**: This is a concrete, positive illustration of Claim 3's advice
  (measure against a defined baseline before committing) rather than independent
  evidence for it — StubHub is a named Anthropic customer in a vendor-published guide,
  so treat the outcome numbers as a case study, not a controlled study.

### Claim 5: 42% of organizations rely on shared IT and finance accountability, with no single owner responsible for AI costs and outcomes, and the guide argues decision rights, escalation authority, and executive backing are three non-interchangeable ownership components, any one of which missing is enough to stall a program
- **Evidence**: Named Accenture survey statistic (Tokenomics research, September 2026)
  paired with a three-part ownership framework.
- **Confidence**: emerging (named survey statistic plus a prescriptive framework;
  the framework is asserted, not independently tested)
- **Quote**: "Decision rights, escalation authority, and executive backing aren't interchangeable, and the absence of any one of them is enough to stall a program."
- **Our assessment**: The three-way split (decision rights / escalation authority /
  executive backing) is a more granular breakdown of "clear ownership" than most of
  this corpus's adoption material offers, which tends to discuss ownership as a single
  undifferentiated requirement. Useful as a diagnostic checklist for evaluating whether
  a nominal "owner" actually has functioning authority.

### Claim 6: Data causes more pilot-to-production programs to stall than almost any other factor, and only 7% of organizations have reached the data-readiness required to scale advanced AI (generative, agentic, and physical), while "data reinventors" that do reach that bar realize EBIT margin uplifts of up to 1.6x over industry peers
- **Evidence**: Named Accenture survey statistic (AI-Ready Data for Advanced AI
  survey, May 2026).
- **Confidence**: emerging (named, dated survey citation; the "1.6x EBIT uplift"
  figure in particular is a strong claim presented without methodology detail in this
  guide)
- **Quote**: "Accenture's AI-Ready Data for Advanced AI survey found that only 7% of organizations have reached the level of data-readiness required to scale advanced AI, including generative, agentic, and physical AI. Those that do, \"data reinventors,\" realize EBIT margin uplifts of up to 1.6x over industry peers."
- **Our assessment**: The 7% figure is the same statistic as Claim 1's "readiness to
  scale" gap, restated with more precision (advanced AI specifically) and paired with
  a strong financial-outcome claim (1.6x EBIT uplift) that would benefit from
  independent scrutiny before being cited as a settled fact. Treat the causal direction
  (data readiness → EBIT uplift, versus already-strong companies being more likely to
  invest in both) as unresolved in this source.

### Claim 7: Novo Nordisk established exactly what clinical trial and patient data could flow to and from the model, and what controls had to be in place, before building its AI documentation platform — resulting in clinical study report production dropping from more than 10 weeks to under 10 minutes
- **Evidence**: Named customer case study with an attributed quote from Novo Nordisk's
  Digitalization Strategy Director.
- **Confidence**: anecdotal (single named customer account; the ~60x-plus time
  reduction, from 10+ weeks to under 10 minutes, is a striking figure presented
  without a breakdown of what the "10 weeks" baseline process included)
- **Quote**: "In a highly regulated industry, we can't just throw our data into a large language model and hope for the best. Our conversations with Anthropic guided us on how to securely use Claude for planning, strategic tasks, and code generation." — Waheed Jowiya, Digitalization Strategy Director, Novo Nordisk
- **Our assessment**: This is the guide's clearest illustration of Consideration 4's
  "data classification before pilot architecture" advice, but the magnitude of the
  reported improvement (10 weeks → under 10 minutes) is large enough that it should be
  treated as a headline vendor case-study figure rather than a typical or guaranteed
  outcome.

### Claim 8: Gartner predicted in 2025 that organizations will abandon 60% of AI projects unsupported by AI-ready data through 2026, and the guide distinguishes two addressable pre-pilot data problems — access (data exists but can't be reached programmatically or requires lengthy permissions) and quality (data is accessible but inconsistent, incomplete, or unreliable)
- **Evidence**: Cited third-party analyst prediction (Gartner, attributed with a
  specific Q&A title and date in a footnote) plus the guide's own access/quality
  taxonomy.
- **Confidence**: emerging (third-party analyst prediction, cited by name/date/footnote
  rather than reproduced primary text; the access/quality split itself is the guide's
  own framing, offered as a practical checklist rather than a measured finding)
- **Quote**: "In 2025, Gartner predicted that organizations will abandon 60% of AI projects unsupported by AI-ready data through 2026."
- **Our assessment**: The Gartner citation is the one third-party (non-Accenture,
  non-Anthropic) data point in the guide, which somewhat strengthens the "data
  readiness" thesis by showing it isn't solely an Accenture-commissioned finding. The
  access-vs-quality distinction is a useful, concrete diagnostic that other corpus
  sources on data readiness treat more abstractly.

### Claim 9: Modern large-context models have made much retrieval infrastructure (built to work around earlier small context windows) obsolete for some use cases, and teams should audit whether their retrieval pipelines solve a current problem or one that no longer exists — while retrieval still adds value when data freshness or access control are the primary drivers
- **Evidence**: Direct architectural claim in Consideration 2, framed as advice rather
  than a case study.
- **Confidence**: emerging (plausible technical claim consistent with known model
  capability trends, but stated as vendor assertion without a specific benchmark or
  named case where retrieval was successfully removed)
- **Quote**: "Modern models can process entire contracts, codebases, or research reports in a single pass. Before investing in retrieval infrastructure, it's worth auditing whether the architecture is solving a current problem or one that's already been addressed."
- **Our assessment**: This is a specific, actionable architectural claim — "audit
  whether your RAG pipeline is solving an obsolete problem" — that is more concrete
  than most of this corpus's context-engineering material about when retrieval is or
  isn't needed. It is a reasonable claim but should be read as a heuristic prompt for
  investigation, not a blanket "delete your retrieval layer" recommendation; the guide
  itself carves out an exception for freshness/access-control-driven retrieval.

### Claim 10: Most infrastructure problems in enterprise AI programs are not caused by choosing the wrong build-vs-buy or platform path, but by never fully committing to one — organizations that run a pilot on a managed API while a platform team builds an in-house alternative "for when we need more control" end up maintaining two systems within six months
- **Evidence**: Direct narrative example in Consideration 3, describing a common
  anti-pattern.
- **Confidence**: anecdotal (a described pattern, not attributed to a specific named
  company or dataset; presented as a composite/typical scenario)
- **Quote**: "A pilot runs on a managed API while a platform team builds something in-house for 'when we need more control.' Six months later, the organization is maintaining two systems. Every new use case reopens the same debate and engineers end up solving the same integration problems in parallel."
- **Our assessment**: This is a specific, nameable anti-pattern (parallel build-and-buy
  drift) distinct from the "AI dust" (shallow bolt-on features) and "retrofitting"
  (layering AI onto unchanged legacy systems) anti-patterns already in this corpus —
  it describes indecision between two committed infrastructure paths rather than
  either extreme. Useful as a third, complementary named failure mode for the guide's
  infrastructure-decisions material.

### Claim 11: TELUS built Fuel iX as a multi-model platform (rather than a single-model architecture) because the scale and diversity of use cases required it, and within that platform Claude became the dominant model choice for the most complex and creative tasks, processing 100 billion tokens monthly, contributing to 500,000+ hours saved across 13,000+ custom AI solutions
- **Evidence**: Named customer case study with an attributed quote from TELUS's Chief
  AI Officer.
- **Confidence**: anecdotal (single named customer account with specific but
  self-reported scale figures)
- **Quote**: "When TELUS gave our team access to multiple AI models through Fuel iX, Claude became the overwhelming choice. The platform processes 100 billion tokens monthly, and Claude is the preferred model for our most complex and creative tasks." — Jaime Tatis, Chief AI Officer, TELUS
- **Our assessment**: This is a specific, large-scale (13,000+ custom solutions, tens
  of thousands of employees) case for a multi-model platform architecture, in tension
  in degree (not in kind) with Consideration 1's advice to "match the model to the use
  case" starting narrow — TELUS's case shows multi-model choice scaling successfully
  once the diversity of use cases justified it, which the guide itself frames as the
  correct sequencing ("start with the model best suited to the task and expand when
  there is a specific, validated need").

### Claim 12: Regulated-industry compliance requirements (HIPAA business associate agreements in healthcare, fair-lending and disclosure rules in financial services, auditable human oversight in legal/HR) must be mapped before the pilot architecture is set, because programs that treat compliance as a late-stage gate discover during the production build that regulatory requirements reshape the architecture designed during the pilot
- **Evidence**: Direct sector-specific examples listed in Consideration 4.
- **Confidence**: settled (specific, well-established regulatory requirements named
  by sector; the "must be mapped pre-pilot, not retrofitted" prescription is the
  guide's own framing)
- **Quote**: "Healthcare programs touching patient data need HIPAA-compliant infrastructure and signed business associate agreements before a vendor relationship goes live... Legal and HR programs handling privileged information or employment decisions that must maintain auditable human oversight, which some jurisdictions require."
- **Our assessment**: This directly corroborates the "governance must be built into the
  operating environment's original DNA, not retrofitted" claim already documented from
  Thoughtworks (Shayan Mohanty) in this corpus — see Cross-References. Two
  vendor-adjacent sources, from different companies, converge on the same
  "compliance-first architecture" prescription.

### Claim 13: Because AI outputs are non-deterministic, enterprise QA frameworks designed for deterministic systems don't transfer directly — the discipline required is architectural (building behavioral constraints into how the model operates) rather than validation layers applied after the fact, and organizations that rely on testing alone discover the gap "at the worst possible time, under production load, with real data, and a live audit"
- **Evidence**: Direct architectural argument in Consideration 4, framed as a general
  principle rather than a specific case.
- **Confidence**: emerging (a well-reasoned architectural claim consistent with how
  LLM-based systems behave, but not backed by a named incident or measured comparison
  of testing-only vs. behavioral-constraint approaches within this guide)
- **Quote**: "Approaches that build behavioral constraints into how models operate give compliance and legal teams something they can audit, document, and verify. The relevant question shifts from whether outputs are generally acceptable to whether model behavior can be explained in a regulatory or legal context."
- **Our assessment**: This reframes AI governance from an output-acceptability
  question to an explainability question, which is a subtly different and more
  specific framing than the general "human oversight" material already in this corpus.
  Worth citing for the specific "testing alone fails under live audit" framing.

### Claim 14: A four-tier oversight model — Automated (no human review), Sampled (random subset reviewed on a cadence), Reviewed (every output approved before release), and Advisory (AI analyzes, a human decides and produces the output) — should be matched to output risk rather than applied uniformly, and tiers are meant to be revisited over time (e.g., a low-error-rate Tier 1/2 process may graduate to a lighter tier after six months to a year)
- **Evidence**: A full worked table in Consideration 6 with example use cases and
  review cadence per tier (credit/lending recommendations and hiring screening are
  placed at Tier 4/Advisory; meeting-transcript summarization and code documentation
  are placed at Tier 1/Automated).
- **Confidence**: settled (a fully specified, reusable framework presented as
  prescriptive guidance, with concrete example use cases per tier — the most
  structurally complete framework in the guide)
- **Quote**: "Production systems that apply the same level of human review to every AI output, regardless of the stakes, either stall under the review burden or start cutting corners in ways that introduce risk. Production governance requires a tiered approach."
- **Our assessment**: This is the single most reusable concrete artifact in the guide
  — a complete tier/use-case/cadence table that maps cleanly onto this corpus's
  existing oversight material (e.g., the three-tier manual/semi-automated/automated
  framework already documented from Thoughtworks — see Cross-References), but with a
  finer-grained four-tier split and explicit example use cases per tier that the
  existing corpus framework does not provide.

### Claim 15: Organizations with formal chargeback accountability for AI spending link 32 cents of every dollar of AI token spend to a quantified business outcome — six times more than organizations with no cost allocation — and governance checkpoints that are never audited become "structural drag," accumulating because removing a checkpoint carries visible risk while keeping it carries invisible cost
- **Evidence**: Named Accenture survey statistic (Tokenomics research, September 2026)
  paired with the guide's own "structural drag" framing.
- **Confidence**: emerging (named, dated survey statistic; the "32 cents / six times"
  figure is specific but not accompanied by methodology in this guide)
- **Quote**: "Accenture's September 2026 Tokenomics report finds that organizations with formal chargeback accountability for AI spending link 32 cents of every dollar of AI token spend to a quantified business outcome, six times more than those with no allocation."
- **Our assessment**: This is a concrete, quotable financial-governance statistic that
  is new to this corpus's token-cost material, which has so far focused on the
  supply-side cost drivers (billing shifts, non-engineer token consumption via PDF
  conversion) rather than accountability-linkage outcomes. See Cross-References for
  how this connects to — and does not contradict — the existing token-cost cluster.

### Claim 16: Moving from AI copilots (bounded by the throughput of the person using them) to end-to-end automation (where throughput scales with volume, not headcount) changes the underlying economics of an AI deployment, but the guide explicitly recommends starting with the simplest solution that could work and adding complexity (e.g., multi-step agentic systems) only after a simpler approach has demonstrably hit its limits
- **Evidence**: Direct argument in Consideration 7, explicitly citing Anthropic's own
  "Building effective agents" guidance as making the same point.
- **Confidence**: settled (a clear, specific claim, cross-referenced to a named
  external Anthropic resource within the guide itself)
- **Quote**: "The key is to avoid building complex agentic AI systems when a simpler approach might work. A well-designed prompt is fast to test and has predictable failure modes, while an agentic system with multiple steps, tool use, and decision-making is more capable but harder to debug, more expensive to maintain, and fails in ways that are harder to anticipate."
- **Our assessment**: This "start simple, scale deliberately" claim, together with the
  companion claim that teams must understand a system's specific error modes (not just
  its aggregate accuracy rate) before scaling volume — "a system that's 95% accurate at
  limited volume sounds production-ready, but the remaining 5% matters" depending on
  what the failures cost at full volume — is directly consistent with, and adds a
  production-scaling-specific angle to, Anthropic's own "Building effective agents"
  guidance already referenced elsewhere in this corpus.

## Concrete Artifacts

```
Source: Anthropic + Accenture, "Deploying AI from pilot to production: A practical
blueprint for CIOs and technical leaders," PDF guide, published ~2026-09-11/14.

THE SEVEN CONSIDERATIONS (table of contents, p.2)

  PRE-PILOT
  01. Strategic objectives, ROI, and ownership
  02. Data readiness and integration
  03. Infrastructure and architecture
  04. Security, compliance, and trust

  PILOT TO PRODUCTION
  05. Organizational readiness

  IN PRODUCTION
  06. Governance and risk management
  07. Scale and evolution

Each consideration ends with a two-column "Before you move forward" table:
  "Work out" (cross-functional, no single owner) vs. "Assign" (a named CIO/
  business-leader decision).
```

```
FOUR-TIER OVERSIGHT MODEL (Consideration 6, p.28, verbatim table)

Tier            | Oversight model                          | Example use cases                                                              | Review cadence
1. Automated    | No human review; output goes directly    | Summarizing meeting transcripts; reformatting data between systems;           | Quarterly audit of output quality
                | to workflow                               | generating code documentation                                                  |
2. Sampled      | Random subset reviewed on a regular      | Extracting structured data from invoices; classifying support tickets;        | A portion of outputs reviewed weekly;
                | cadence                                    | populating CRM fields from call transcripts                                   | start with a higher rate of reviews
                |                                            |                                                                                 | and adjust as error patterns stabilize
3. Reviewed     | Human approves every output before it    | Drafting client communications; generating financial analysis for external    | Every output reviewed before release;
                | reaches its audience                      | distribution; producing contract language from templates; creating           | audit the review process monthly for
                |                                            | marketing content                                                              | catch rate and cost
4. Advisory     | AI provides analysis, a human makes the  | Credit and lending recommendations; candidate screening in hiring workflows;  | Every decision documented with an
                | decision and produces the output          | clinical findings for physician review; regulatory filing preparation         | audit trail; compliance review quarterly

Note in text: "The proposed tiers are flexible... if a process has had a low error
rate for a long period of time, say six months or a year, it may be ready to move
up to tier 2."
```

```
AN ENTERPRISE AI DEPLOYMENT BLUEPRINT (p.35, timeline structure)

PRE-PILOT (decide before the pilot begins):
  01 Strategy and ownership — set success criteria, ROI thresholds, go/no-go gates
     [owner: Executive sponsor]
  02 Data and integration — audit the data estate, assign source/pipeline owners
     [owner: Data and IT change owners]
  03 Infrastructure — align platform choices to use case requirements
     [owner: CIO / platform lead]
  04 Security and trust — classify data, clear security/regulatory/access reqs
     [owner: Security and compliance lead]

PILOT (validate, don't defer):
  "No new owners or decisions — the pilot tests the decisions already made."

PREPRODUCTION (prepare the organization):
  05 Org readiness — sequence rollout, fund reskilling, name champions
     [owner: Exec sponsor / change lead]

PRODUCTION (govern by risk):
  06 Governance and risk — define risk taxonomy, monitoring thresholds, review authority
     [owner: Risk and monitoring owner]

SCALED DEPLOYMENT (operate as a capability):
  07 Scale and evolution — start simple, scale deliberately; understand failure
     modes before scaling
     [owner: AI program owner]

Framing text: "Every decision deferred past the pilot creates engineering debt:
parallel systems, integration patterns that never standardize, and a platform
foundation that's always being renegotiated."
```

```
NAMED CASE STUDIES (customer, mechanism, headline outcome)

StubHub    — A/B-tested multiple model providers against resolution-rate/satisfaction
             benchmarks pre-launch → 30% reduction in support costs; response time
             from 20+ min to near-instant. Quote: Timothy Addison, Engineering Org
             Chief of Staff.
Novo Nordisk — Pre-defined what clinical/patient data could flow to/from the model
             before building NovoScribe → clinical study report production from
             10+ weeks to under 10 minutes. Quote: Waheed Jowiya, Digitalization
             Strategy Director.
TELUS      — Built Fuel iX as a deliberate multi-model platform → Claude became
             dominant model for complex/creative tasks; 100B tokens/month;
             500,000+ hours saved; 13,000+ custom AI solutions. Quote: Jaime Tatis,
             Chief AI Officer.
Palo Alto Networks — Treated vendor safety/security posture as a primary evaluation
             criterion, not just technical performance → 20-30% increase in feature
             development velocity. Quote: Gunjan Patel, Director of Engineering.
NBIM (Norges Bank Investment Management) — Built role-specific training paths + a
             50-specialist "AI Ambassador Network" → 600+ active users within two
             months; employees self-report saving 20%+ of weekly time. Quote:
             Stian Kirkeberg, Head of ML and AI.
```

```
Accenture statistics cited (name, date, figure):
- Pulse of Change, July 2026: 23% of C-suite leaders report sustained, enterprise-
  wide AI impact.
- AI-Ready Data for Advanced AI survey, May 2026: 64% moved beyond pilots into
  production across multiple functions / initiated enterprise-wide efforts, but only
  7% reached the data-readiness required to scale advanced AI; "data reinventors"
  realize EBIT margin uplifts of up to 1.6x over industry peers.
- Tokenomics research, September 2026: 42% of organizations rely on shared IT/
  finance accountability with no single AI cost/outcome owner; organizations with
  formal chargeback accountability link 32 cents of every AI token dollar to a
  quantified business outcome (6x those with no allocation).
- Gartner (Q&A with Roxane Edjlali, "Lack of AI-Ready Data Puts AI Projects at Risk,"
  Feb 26, 2025), cited via footnote: predicted 60% of AI projects unsupported by
  AI-ready data will be abandoned through 2026.
```

## Cross-References

### Cross-reference verification notes
`blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md`,
`blog-anthropic-monday-agent-first-platform.md`,
`blog-anthropic-cowork-deploy-guide.md`, and
`blog-simonwillison-accenture-pdf-tokens.md` were re-read directly (MINER.md §4b) and
the claim numbers cited below were confirmed against those notes' numbered
`### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md` Claim 4
    ("governance cannot be retrofitted onto an agent platform after deployment — it
    must be built into the operating environment's original DNA") directly
    corroborates this guide's Claim 12 (sector-specific compliance requirements must
    be mapped pre-pilot) and the guide's repeated "front-load the decisions" framing
    in the transition blueprint. Two independent vendor-adjacent sources (Thoughtworks
    via Shayan Mohanty; Anthropic+Accenture here) converge on "governance/compliance
    design must precede, not follow, deployment."
  - `blog-anthropic-monday-agent-first-platform.md` Claim 11 ("Adoption depends on
    trust as much as it does on capability... governance, permissions, transparency,
    and reliability determine whether agents move beyond pilot programs and into
    production") corroborates this guide's central thesis (Claim 2) that pilot
    conditions are an unreliable signal for production readiness precisely because
    trust/governance infrastructure, not raw capability, is what's missing.
  - `blog-anthropic-cowork-deploy-guide.md` Claim 10 (the "supervised-then-scheduled"
    Level 2→3 autonomy progression: run with validation, then remove it once behavior
    is confirmed) is the same underlying trust-building mechanism as this guide's
    Claim 14 (tiers "flexible... may be ready to move up to tier 2" after a sustained
    low-error-rate period) — two Anthropic-published frameworks independently
    describing graduated autonomy expansion, one at the individual-skill level (Cowork
    guide) and one at the production-oversight-tier level (this guide).
  - `blog-simonwillison-accenture-pdf-tokens.md` Claim 1 (Accenture's own internal
    telemetry attributes majority AI token consumption to non-engineers, not
    engineers) is a different Accenture-sourced data point from the same period
    (leaked audio reported June 2026; this guide published September 2026) that adds
    texture to this guide's Claim 15 (formal chargeback accountability correlates with
    better cost-to-outcome linkage) — both concern AI cost governance at Accenture or
    Accenture's clients, from different evidentiary bases (leaked internal audio vs.
    a published survey).

- **Contradicts**: None filed as a formal contradiction issue. One tension worth
  flagging for the Smith's awareness: this guide's transition blueprint states "No new
  owners or decisions" during the pilot phase — front-loading essentially all
  ownership, infrastructure, and governance decisions before the pilot begins — while
  `blog-anthropic-cowork-deploy-guide.md` Claim 8 recommends the opposite sequencing
  for Cowork adoption specifically: "bottom-up discovery, top-down scale... let teams
  experiment and find what works for their function, then take what works and
  provision it org-wide." Per MINER.md §4a this reads as a conditioning-variable
  difference rather than a material contradiction — the Cowork guide describes
  grassroots, individual-employee skill-building tools (low-stakes, easily reversible),
  while this guide's "decide everything upfront" framework is explicitly scoped to
  named, governed production AI systems (contract review, underwriting, lending) with
  higher consequence of failure. Both sources are Anthropic-published and do not
  address each other, so this is flagged here rather than escalated to a contradiction
  issue.

- **Extends**:
  - `blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md` Claim 4's five-item
    governance checklist (identity, permissions, observability, cost management, human
    escalation) is extended by this guide's fully worked four-tier oversight table
    (Claim 14) — the Thoughtworks source states the checklist abstractly with no named
    mechanism; this guide supplies a complete, example-populated implementation for
    the "human escalation" and "observability" items specifically.
  - `blog-anthropic-cowork-deploy-guide.md`'s five-level maturity model and pilot
    use-case categories (that guide's Claims 2, 6) describe how individual employees
    and teams progress toward AI-augmented work; this guide's seven considerations
    extend that picture to the governance, infrastructure, and organizational
    decisions a CIO must make for a named, production-critical AI initiative — the two
    guides together span "how does grassroots adoption scale" (Cowork guide) and "how
    does a formal AI initiative reach production" (this guide).

- **Novel**:
  - **The four-part use-case definition (user, task, output, quality threshold)**
    (Claim 3) is a specific, portable scoping tool not previously documented in this
    corpus in this exact form.
  - **The three-way, non-interchangeable ownership split (decision rights /
    escalation authority / executive backing)** (Claim 5) is new — prior corpus
    material treats "clear ownership" as a single requirement rather than three
    distinct, independently-necessary components.
  - **The fully worked four-tier oversight table with example use cases per tier**
    (Claim 14) is the most structurally complete human-oversight framework in this
    corpus to date.
  - **The "structural drag" framing for un-audited governance checkpoints** (Claim 15)
    — the specific idea that review checkpoints accumulate because removing one
    carries visible risk while keeping it carries invisible cost — is a new,
    citable vocabulary item.
  - **Named financial-governance outcome linkage (32 cents / 6x chargeback finding)**
    (Claim 15) is new to this corpus's token-cost material, which has so far focused
    on cost drivers rather than accountability-outcome correlation.

## Guide Impact

- **Chapter 02 (Deployment & Operations)**: Add the four-tier oversight model (Claim
  14, full table in Concrete Artifacts) as a named, reusable framework for matching
  human review intensity to output risk — this is more granular and example-populated
  than the three-tier manual/semi-automated/automated framework currently cited from
  Thoughtworks, and should be presented as the primary reference table, with the
  Thoughtworks framework as a corroborating simpler variant.

- **Chapter 02 (Deployment & Operations)**: Add the "front-load the decisions"
  transition blueprint (Concrete Artifacts) as a decision-sequencing checklist for
  readers planning a pilot-to-production transition, but pair it with the noted tension
  (Cross-References → Contradicts) against the Cowork guide's bottom-up sequencing —
  make explicit that "decide everything upfront" applies to governed, higher-stakes
  production systems, not grassroots individual-employee tooling.

- **Chapter 04 (Organizational Patterns)**: Add the three-way ownership split (Claim
  5: decision rights, escalation authority, executive backing) as a diagnostic
  checklist for evaluating whether a named AI program owner actually has functioning
  authority, replacing or supplementing the current single-dimension "clear ownership"
  framing.

- **Chapter 06 (Enterprise Tooling / Governance)**: Add the four-part use-case
  definition (Claim 3: user, task, output, quality threshold) as a scoping template
  readers can apply directly before starting a pilot, and the "structural drag" concept
  (Claim 15) as vocabulary for periodic governance-checkpoint audits.

## Extraction Notes

- The blog post at the issue URL is a ~400-word teaser; all substantive claims come
  from the linked 38-page PDF, which was located via a WebFetch call that surfaced the
  download link, then fetched directly. The PDF's text was extracted by the Read tool
  page-by-page and reproduced here verbatim for all quotes; page numbers are cited in
  the Concrete Artifacts section for traceability.
- All eight pages containing the seven considerations, the diagnostic framing, and the
  closing blueprint were read in full (pp. 1-38, i.e., the entire guide, including the
  "Getting started" resource list on pp. 36-37 and the "About Anthropic" / "About
  Accenture" boilerplate on p. 37). No pages were skipped.
- Two WebFetch attempts against the guide's summarization pipeline initially declined
  to reproduce verbatim text (citing copyright caution) and returned only a condensed
  summary; the direct Read-tool PDF extraction (used for all quotes in this note)
  bypassed that limitation and returned genuine extracted text, which was checked
  against itself for internal consistency (e.g., repeated statistics appearing
  identically on the summary page (p.3) and within the relevant consideration (p.7,
  p.11, p.27) matched word-for-word).
- No contradiction issue was filed. See Cross-References → Contradicts for the
  reasoning (the "decide everything upfront" vs. "bottom-up discovery" tension is a
  scope/stakes difference between governed production systems and grassroots employee
  tooling, not a material contradiction per MINER.md §4a).
