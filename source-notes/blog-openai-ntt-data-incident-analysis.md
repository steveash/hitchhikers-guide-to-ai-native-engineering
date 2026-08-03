---
source_url: https://openai.com/index/ntt-data
source_type: blog-post
title: "NTT DATA Group cuts incident analysis to 30 minutes with Codex"
author: OpenAI (customer-story vertical; quoted subjects Hiroaki Sato — AI Technology Department, and Yuji Shono — Head of Global AI Office, both NTT DATA Group)
date_published: 2026-07-22
date_extracted: 2026-08-03
last_checked: 2026-08-03
status: current
confidence_overall: emerging
issue: "#2447"
---

# NTT DATA Group cuts incident analysis to 30 minutes with Codex

> An OpenAI customer-story case study documenting NTT DATA Group's expansion of Codex to
> approximately 9,000 employees (technical and nontechnical) atop an existing companywide
> ChatGPT Enterprise rollout — headlined by a single named incident-analysis use case (a
> complex incident that previously took five engineers three days, completed by Codex in 30
> minutes) that became the internal proof point driving broader adoption, a named "Client
> Zero" internal-dogfooding strategy, a Center of Excellence (CoE) governance model, and a
> five-item "Leadership lessons" list.

## Source Context

- **Type**: blog-post (OpenAI customer-story page, `openai.com/index/`, ~900 words;
  auto-discovered via the `openai-news` trusted feed, published July 22, 2026). Structured
  with the same house template already documented in the corpus for OpenAI enterprise case
  studies — a company-metadata block (Company size, Region, Industry, Products), a headline
  metrics box, section-by-section named-executive quotes, a "Results at a glance" bullet
  list, and a closing "Leadership lessons" list (see Cross-References for template
  comparison against `blog-openai-bbva-banking-transformation.md` and
  `blog-openai-australian-payments-plus.md`).
- **Author credibility**: House-authored OpenAI customer-story copy built around quotes from
  two named NTT DATA Group individuals: Hiroaki Sato (AI Technology Department) and Yuji
  Shono (Head of Global AI Office). NTT DATA Group is a Japan-based global IT services
  company (consulting, systems development, operations). This is a vendor case study —
  OpenAI selected the customer, chose which quotes and metrics to publish, and frames the
  narrative promotionally (a metrics box, a "Leadership lessons" list, a closing "Contact
  sales" call to action) — not an independent report with disclosed methodology. Neither
  named individual holds a C-suite title comparable to BBVA's Chair-level quote or AP+'s
  three C-level quotes; Sato and Shono are both AI-function specialists (AI Technology
  Department; Head of Global AI Office), not business-unit or company leadership.
- **Scope**: Covers the sequencing from companywide ChatGPT Enterprise adoption to Codex
  expansion, one named incident-analysis use case with a specific before/after metric, an
  internal-dogfooding strategy ("Client Zero"), nontechnical-employee use cases (expense
  extraction, file organization, Excel data analysis, document summarization, ad hoc
  reporting), a governance/security framework built by an internal Center of Excellence
  (CoE), a "Results at a glance" summary (three bullets), and a five-item "Leadership
  lessons" list. Does NOT cover: any headcount figure for the underlying ChatGPT Enterprise
  deployment beyond the 9,000-employee Codex figure, technical implementation detail for the
  incident-analysis workflow (what kind of incident, what systems Codex accessed, what
  "the full process" consisted of), a rollout timeline with dates, cost or licensing terms,
  or any account from an individual contributor engineer — both quoted voices are from the
  internal AI/CoE function, not from the engineering team that ran the incident analysis.

## Extracted Claims

### Claim 1: Codex completed a complex incident analysis for a critical system in 30 minutes that had previously required five experienced engineers and taken three days — a reduction OpenAI's own metrics box expresses as "-99.3%"
- **Evidence**: Named single-incident narrative in the "An early use case builds momentum for Codex" section, plus a headline metrics-box statistic expressing the same reduction as a percentage.
- **Confidence**: anecdotal (a single named incident type with no incident count, no description of what the "complex incident analysis" or "critical system" were, and no detail on what "the full process" (investigation, root-cause identification, remediation, documentation?) actually consisted of)
- **Quote**: "One of the first successes to demonstrate the potential of Codex was the automation of a complex incident analysis for a critical system. The work had previously required five experienced engineers and taken three days to complete. With Codex, the full process was completed in 30 minutes."
- **Quote**: "-99.3% Codex completed an incident analysis in 30 minutes that had previously taken five engineers 3 days"
- **Our assessment**: Unlike `blog-openai-australian-payments-plus.md` Claims 3–4 (which document an unreconciled discrepancy between AP+'s metrics-box figure and body-text figure for the same reconciliation-investigation use case), this article's metrics-box figure ("-99.3%") and body-text description ("five engineers, three days" → "30 minutes") are internally consistent — three days of five-engineer effort is 120 person-hours, and a reduction to 30 minutes of (presumably single-session) Codex-assisted work is indeed a ~99%+ time reduction, whichever way the arithmetic is framed. This is the single most extreme before/after reduction figure in the corpus's set of OpenAI enterprise case studies — larger in percentage terms than AP+'s reconciliation metric (4 hours → 30 minutes, ~87.5%) or the Peru assistant's query-handling reduction documented in `blog-openai-bbva-banking-transformation.md` Claim 10 (~87%). The guide should note that, as with every other vendor case study in this corpus, no measurement methodology (was "three days" a measured historical average or a single prior incident's actual duration?) is disclosed.

### Claim 2: NTT DATA Group expanded Codex to approximately 9,000 employees across both technical and nontechnical roles, building on a prior companywide ChatGPT Enterprise rollout
- **Evidence**: Direct statement of deployment scope, presented as the article's headline eligibility/scale figure and repeated in the "Results at a glance" section.
- **Confidence**: emerging (a specific named headcount figure — 9,000 active Codex users — though the article gives no total-workforce denominator, so the fraction of NTT DATA Group's full headcount this represents is unstated)
- **Quote**: "Building on companywide adoption of ChatGPT Enterprise, NTT DATA Group expanded Codex to approximately 9,000 employees across technical and nontechnical roles."
- **Quote**: "9,000 Active Codex users"
- **Our assessment**: This is a smaller absolute figure than BBVA's ~100,000 ChatGPT Enterprise employees (`blog-openai-bbva-banking-transformation.md` Claim 2) but is specifically a Codex-adoption figure — the article does not disclose how many employees have ChatGPT Enterprise access company-wide, only that Codex (the narrower, more autonomous product) now covers ~9,000 people spanning technical and nontechnical roles. This "technical and nontechnical" framing is the same broad-eligibility pattern documented in `blog-openai-samsung-chatgpt-codex-deployment.md` Claim 2 (Samsung: "technical and non-technical work, across a broad range of functions"), but NTT DATA's version is stronger evidence of actual usage breadth because it reports a specific active-user count rather than an eligibility rule with no usage figure attached.

### Claim 3: Prior to Codex, NTT DATA Group's companywide ChatGPT Enterprise rollout produced self-reported satisfaction above 96% and productivity gains above 95% in an internal survey
- **Evidence**: Direct statement citing an internal survey, presented as the foundation that prepared the organization for Codex adoption.
- **Confidence**: emerging (specific named percentages from a self-reported internal survey; no disclosed sample size, survey population, or methodology — comparable in evidentiary kind to the self-reported single-company metrics graded emerging in `blog-openai-bbva-banking-transformation.md` Claims 6 and 10)
- **Quote**: "In an internal survey, more than 96% of respondents said they were satisfied with ChatGPT Enterprise, and more than 95% reported productivity gains."
- **Our assessment**: These figures describe the earlier ChatGPT Enterprise (chat-only) rollout, not Codex specifically — the article positions them as the adoption foundation that "prepared the organization for the next step: delegating clearly defined tasks to Codex." As with every percentage in this article, no survey methodology is given. The >95%/>96% figures are notably higher than any comparable self-reported adoption metric elsewhere in the corpus (e.g., AP+'s 80% creativity/quality figure or 77% time-savings figure in `blog-openai-australian-payments-plus.md` Claims 8–9), which should be read with appropriate skepticism about survey-response bias (employees satisfied enough to respond to an internal AI-adoption survey are a self-selected population).

### Claim 4: NTT DATA Group runs an internal "Client Zero" strategy — treating its own organization as the first customer and actively encouraging employees to test AI in their daily work — as the mechanism for expanding Codex beyond engineering into nontechnical functions
- **Evidence**: Direct statement naming the strategy, paired with a supporting quote from Hiroaki Sato.
- **Confidence**: anecdotal (a named internal strategy with no detail on how "Client Zero" is operationalized — no named program structure, headcount, or governance process beyond the CoE described in Claim 6)
- **Quote**: "Under their 'Client Zero' approach, NTT DATA Group treats their own organization as the first customer and encourages employees to test AI in their daily work."
- **Quote**: "Through our Client Zero approach, we actively promote the use of AI within our own organization. Codex has significant potential, and employees across many departments are finding ways to apply it to their own work." — Hiroaki Sato, AI Technology Department, NTT DATA Group
- **Our assessment**: "Client Zero" is a distinct branded internal-dogfooding concept not previously documented in the corpus (a grep of existing source notes for "Client Zero" returned zero matches). It is conceptually related to, but distinct from, the champion-network adoption mechanism documented in `blog-openai-bbva-banking-transformation.md` Claim 4 (a two-tier "champions"/"wizards" structure) and `blog-anthropic-legal-industry-deploy.md`'s champion pattern — those describe designated advocate employees driving peer adoption, whereas "Client Zero" describes a company-level organizational posture (the whole company as first customer/test bed for a systems-integrator's own AI offerings) rather than a designated-individual enablement tier. Given that NTT DATA Group is itself an IT-services/systems-integration company that presumably sells AI-transformation services to its own clients, "Client Zero" also functions as a credibility-building narrative (we use what we sell) that a pure end-user enterprise like BBVA or AP+ would not have the same incentive to frame this way — the guide should note this structural difference when citing NTT DATA alongside non-vendor enterprise adopters.

### Claim 5: Hiroaki Sato frames Codex's organizational impact as comparable to the initial arrival of ChatGPT, because it changed how people across the company think about AI's ability to independently lead work
- **Evidence**: Direct pull-quote from Hiroaki Sato, AI Technology Department, presented immediately after the incident-analysis use case.
- **Confidence**: anecdotal (single individual's characterization of organizational sentiment shift; not a measured outcome)
- **Quote**: "Codex has changed how people across the company think about AI. The idea that AI can take the lead in carrying out work has had an impact similar to the arrival of ChatGPT."
- **Our assessment**: This quote explicitly frames the shift as being about agentic autonomy specifically ("AI can take the lead in carrying out work"), not about AI capability generally — the article draws a deliberate distinction between ChatGPT's conversational/assistive framing and Codex's agentic/autonomous framing, and attributes the internal excitement to the latter. This is a company-internal-perception claim, not a productivity claim, and should be cited as evidence of how agentic tooling is perceived to change organizational AI narratives, not as evidence of a measured outcome.

### Claim 6: An internal OpenAI Center of Excellence (CoE) at NTT DATA Group developed and rolled out security guidelines defining what data can be used, which systems Codex can connect to, how network traffic is managed, which sandbox mode to apply, what level of automation is appropriate, and where human review is required
- **Evidence**: Direct statement describing the CoE's role and the specific named categories of guidance it produced.
- **Confidence**: settled (a specific, itemized description of governance-guideline scope — the most operationally concrete governance detail in the article, though the article does not disclose the guidelines' actual content or thresholds, only their categories)
- **Quote**: "To prepare Codex for enterprise use, the OpenAI CoE has developed and rolled out security guidelines alongside practical guidance for adoption. These guidelines clarify what data can be used, which systems Codex can connect to, how network traffic is managed, which sandbox mode to apply, what level of automation is appropriate, and where human review is required."
- **Our assessment**: This six-category governance checklist (data eligibility, system connections, network traffic, sandbox mode, automation level, human-review boundary) is more granular than BBVA's three-pillar "trust, governance, structured learning" framing (`blog-openai-bbva-banking-transformation.md` Claim 3) or AP+'s generic "keeping human experts accountable" qualifier (`blog-openai-australian-payments-plus.md` Claim 5) — it names specific technical/operational control points (sandbox mode, network traffic, automation level) rather than only organizational principles. Note the CoE is named as "the OpenAI CoE" in this sentence — ambiguous whether this is an NTT DATA-internal center of excellence for OpenAI products (consistent with the issue-body auto-discovery framing and the earlier sentence "It established an internal OpenAI Center of Excellence") or a joint/OpenAI-operated body; the article's own earlier sentence ("NTT DATA Group... established an internal OpenAI Center of Excellence, or CoE, to support adoption") indicates it is NTT DATA's own internal body, named after OpenAI, not an OpenAI-staffed function — cite it as an NTT DATA-internal governance function.

### Claim 7: Nontechnical employees at NTT DATA Group use Codex to build lightweight tools, organize large volumes of files, analyze data in Excel, summarize documents, and script repetitive processes — tasks described as things people wanted to automate but that were too time-consuming to handle manually
- **Evidence**: Direct statement describing the category of nontechnical Codex use, followed by a specific named example (Claim 8).
- **Confidence**: anecdotal (a described category of use cases with no adoption count, frequency, or time-savings figure for the category as a whole)
- **Quote**: "Nontechnical employees are already using Codex to build lightweight tools, organize large volumes of files, analyze data in Excel, summarize documents, and script repetitive processes. These are often tasks that people want to automate but that would be too time consuming to handle manually."
- **Our assessment**: This directly corroborates the "role-boundary dissolution" pattern already documented in `blog-openai-codex-knowledge-work.md` Claim 5 (72% of knowledge-worker Codex users produce artifacts weekly; 47% do engineering operations; 46% do code implementation) and `blog-openai-agents-transforming-work.md` Claim 8 (over one-fourth of Codex work done by business-function workers is engineering or coding) — NTT DATA's article is a named enterprise instance of exactly that aggregate telemetry pattern, giving concrete task categories (file organization, Excel analysis, document summarization, process scripting) where the aggregate reports gave only percentage breakdowns.

### Claim 8: A specific nontechnical Codex use case at NTT DATA Group is extracting transportation expenses from credit card statements and transferring them into travel expense forms, with Codex working across multiple files and helping verify the completed transfer
- **Evidence**: Named, specific example given as an illustration of the broader nontechnical-use-case category (Claim 7).
- **Confidence**: anecdotal (a single named workflow example with no volume, frequency, error-rate, or time-savings figure)
- **Quote**: "For example, employees use Codex to extract transportation expenses from credit card statements and transfer them into travel expense forms. Codex can work across multiple files, understand the structure and entry rules of each sheet, and help verify the completed transfer, streamlining work that was previously manual and cumbersome."
- **Our assessment**: This is a concrete, narrow, low-stakes automation example — multi-file structured-data extraction and transcription against known entry rules, with an explicit verification step ("help verify the completed transfer") built into the description. It is structurally similar to the Canvas-LMS-scripting vignette in `blog-openai-codex-knowledge-work.md` Claim 10 (Prof. Taiyo Inoue generating scripts against a documented admin system rather than building new software) — both are examples of an agent automating a bounded, rules-based clerical task against an existing system's structure, a more corroborated and lower-risk pattern than open-ended "build me an app" use cases. No quantified time savings is given for this specific example, unlike Inoue's self-estimated 4-5 hours/week.

### Claim 9: Nontechnical employees at NTT DATA Group can now create analytical reports by analyzing raw data directly with Codex, a task that previously required preparing data in a business intelligence tool and building a dashboard — reducing dependence on specialized tools and skills
- **Evidence**: Direct statement describing a before/after shift in how analytical reports are produced.
- **Confidence**: anecdotal (a described workflow shift with no adoption count, no time-savings figure, and no data-quality or accuracy comparison between BI-tool output and Codex-generated analysis)
- **Quote**: "Another important shift is that nontechnical employees can now complete work that once required support from engineers. Creating an analytical report, for example, previously required preparing data in a business intelligence tool and building a dashboard. With Codex, employees can analyze raw data directly and create the reports they need, improving efficiency while reducing dependence on specialized tools and skills."
- **Our assessment**: This claim describes Codex disintermediating not just manual effort but an entire tooling layer (BI platform + dashboard-building skill), which is a stronger claim than most "AI speeds up an existing workflow" claims in the corpus — here the claim is that the workflow's tooling requirement itself is eliminated. The article gives no detail on data governance, accuracy validation, or whether these Codex-generated reports go through any review before being used for decisions, which is a notable gap given that BI-tool-and-dashboard workflows typically exist partly for governance/consistency reasons (shared definitions, access controls, audit trail) that a one-off Codex analysis may not replicate. The guide should not cite this as evidence that ad hoc AI-generated analysis is a governance-equivalent substitute for BI tooling — only as evidence that employees perceive it as a faster substitute for one-off reporting tasks.

### Claim 10: Weekly active Codex users at NTT DATA Group increased 1.4 times after the company published a usage guide and conducted hands-on training
- **Evidence**: Metrics-box statistic in the "Results at a glance" section, not further elaborated in the article body.
- **Confidence**: emerging (a specific named multiplier tied to a specific stated intervention — publishing a usage guide plus hands-on training — though no baseline user count, time window, or measurement method is disclosed)
- **Quote**: "Increased weekly active Codex users by 1.4 times after publishing a usage guide and conducting hands on training"
- **Our assessment**: This is the article's clearest causally-attributed adoption-intervention claim — unlike the 9,000-user headcount figure (Claim 2), which gives no adoption trajectory, this figure explicitly ties a specific enablement action (usage guide + training) to a measured usage increase. It is directionally consistent with the general "documented onboarding materials accelerate adoption" pattern in `blog-anthropic-legal-industry-deploy.md` Claim 9 (pilot success signals) and `blog-openai-bbva-banking-transformation.md` Claim 5 (leadership training as an adoption accelerator), though NTT DATA's version measures general-employee usage-guide effectiveness rather than leadership training specifically.

### Claim 11: NTT DATA Group automated internal system operations using Playwright, reducing time spent on routine daily tasks, and enabled organization-wide adoption of that automation by packaging it as Skills
- **Evidence**: Metrics-box statistic in the "Results at a glance" section, not elaborated further in the article body.
- **Confidence**: anecdotal (a named mechanism — Playwright-based automation packaged as Skills — with no time-savings figure, task-volume figure, or adoption-count figure, and no description of what "internal system operations" specifically means)
- **Quote**: "Automated internal system operations using Playwright, reducing time spent on routine daily tasks, and enabled organization-wide adoption by packaging the automation as Skills"
- **Our assessment**: This is the article's most technically specific claim (naming a concrete tool, Playwright — a browser-automation framework — rather than describing Codex use only in generic terms) but also its thinnest in outcome evidence: no metric of any kind is attached, only the mechanism description. The "packaging the automation as Skills" detail is the more guide-relevant part — it names a concrete pattern of converting a one-off automation into a reusable, organization-wide-distributable unit, structurally similar to the "skills as encoded institutional knowledge" pattern documented at length in `blog-anthropic-legal-industry-deploy.md` (Claims 6-8, 12, 15), though from OpenAI's Codex/Skills terminology rather than Anthropic's Claude/Skills terminology — this is a notable point of vendor-independent convergence on "skill packaging" as the mechanism for scaling a single automation into org-wide reuse, worth flagging even though this article gives no further operational detail (no governance, versioning, or maintenance process, unlike the Anthropic legal guide's explicit skills-governance section).

### Claim 12: NTT DATA Group names five "Leadership lessons" for embedding Codex across an organization: make ChatGPT Enterprise part of daily work first, deploy broadly to create peer-learning network effects, build a safe/governed usage environment, treat deployment as a continuously-improved beginning (not an endpoint), and have the CoE generalize high-impact use cases into reusable best practices
- **Evidence**: Verbatim bulleted list under the "Leadership lessons" heading.
- **Confidence**: anecdotal (vendor-authored/vendor-curated lessons list; no detail on how these five were selected or whether other lessons were considered and excluded)
- **Quote**: "Make ChatGPT Enterprise part of daily work and help employees build the habits needed to collaborate with AI"
- **Quote**: "Deploy ChatGPT Enterprise broadly to create network effects through peer learning and word of mouth"
- **Quote**: "Create an environment where employees can use AI safely with appropriate security and privacy protections"
- **Quote**: "Treat deployment as the beginning, then continuously improve adoption programs using usage data, surveys, and employee interviews"
- **Quote**: "Have the CoE identify and generalize high impact use cases, then share them as reusable best practices with appropriate safeguards"
- **Our assessment**: This five-item "Leadership lessons" list is structurally identical to the bulleted lessons-learned format already documented in `blog-openai-bbva-banking-transformation.md` (six items) and `blog-openai-australian-payments-plus.md` (four items) — a third and fourth instance respectively of OpenAI's consistent house editorial framing for customer-story closers (per the assessment already established in the BBVA note's Claim 11 and corroborated again in the AP+ note's Claim 11). The first lesson here ("make ChatGPT Enterprise part of daily work... before Codex") explicitly names the sequencing logic the rest of the article demonstrates (chat-first adoption as the prerequisite for agentic-tool adoption), making it the most substantively load-bearing of the five, unlike some of the more generic lessons in BBVA's and AP+'s lists.

## Concrete Artifacts

```
Source: OpenAI, "NTT DATA Group cuts incident analysis to 30 minutes with Codex,"
https://openai.com/index/ntt-data (published July 22, 2026)

Company metadata block (verbatim):
  Company size: Enterprise
  Region:       Asia-Pacific & Oceania
  Industry:     Technology
  Products:     Codex

Headline metrics box (verbatim, two stats):
  9,000     Active Codex users
  -99.3%    Codex completed an incident analysis in 30 minutes that had
            previously taken five engineers 3 days

Section headings (in order):
  Companywide ChatGPT Enterprise adoption creates the foundation for Codex
  An early use case builds momentum for Codex
  Expanding the potential of Codex beyond engineering
  Creating a secure environment for everyone to use Codex
  Results at a glance
  Leadership lessons
  Turning organizational knowledge into customer value

"Results at a glance" (verbatim bulleted list):
  - Completed in 30 minutes a complex incident analysis that previously
    took five experienced engineers three days
  - Increased weekly active Codex users by 1.4 times after publishing a
    usage guide and conducting hands on training
  - Automated internal system operations using Playwright, reducing time
    spent on routine daily tasks, and enabled organization-wide adoption
    by packaging the automation as Skills

"Leadership lessons" (verbatim bulleted list, five items, no elaboration
text beyond the bullet itself):
  - Make ChatGPT Enterprise part of daily work and help employees build
    the habits needed to collaborate with AI
  - Deploy ChatGPT Enterprise broadly to create network effects through
    peer learning and word of mouth
  - Create an environment where employees can use AI safely with
    appropriate security and privacy protections
  - Treat deployment as the beginning, then continuously improve adoption
    programs using usage data, surveys, and employee interviews
  - Have the CoE identify and generalize high impact use cases, then
    share them as reusable best practices with appropriate safeguards

Named individual quotes (verbatim, in order of appearance):
  Hiroaki Sato, AI Technology Department:
    "Codex has changed how people across the company think about AI. The
    idea that AI can take the lead in carrying out work has had an impact
    similar to the arrival of ChatGPT."
  Hiroaki Sato, AI Technology Department:
    "Through our Client Zero approach, we actively promote the use of AI
    within our own organization. Codex has significant potential, and
    employees across many departments are finding ways to apply it to
    their own work."
  Yuji Shono, Head of Global AI Office:
    "Codex is about more than helping developers write code faster. As
    ChatGPT Enterprise has become part of how our employees think,
    explore ideas, and solve problems, Codex opens the door to a new way
    of working. By enabling AI to research, organize, execute, and
    validate work, it empowers every employee to transform how they
    approach their role."
  Yuji Shono, Head of Global AI Office:
    "Creating a secure and well governed environment is essential for
    employees to use Codex with confidence. Our vision is for Codex to
    become more than a tool for engineers. We want it to be a natural
    part of everyday work for every employee, including those in
    nontechnical roles, helping people turn their expertise and ideas
    into greater impact."

Closing framing, "Turning organizational knowledge into customer value"
section (verbatim, final paragraph):
  "Through its 'AI Driven Company' vision, NTT DATA Group aims to amplify
  the knowledge and expertise of every employee, create new services and
  business processes, and help customers transform their operations and
  grow. By demonstrating the value of AI within its own organization, the
  company plans to extend that impact to customers and society more
  broadly."
```

## Cross-References

### Cross-reference verification notes
`blog-openai-australian-payments-plus.md`, `blog-openai-bbva-banking-transformation.md`,
`blog-openai-samsung-chatgpt-codex-deployment.md`, `blog-openai-codex-knowledge-work.md`,
`blog-openai-agents-transforming-work.md`, and `blog-anthropic-legal-industry-deploy.md`
were each re-read in full and the claim numbers cited below were confirmed against those
notes' actual numbered `### Claim N:` headings before writing this note; none were guessed.

- **Corroborates**:
  - `blog-openai-australian-payments-plus.md` Claim 4 (AP+'s reconciliation-investigation
    metric, 4 hours → 30 minutes, ~87.5%) and `blog-openai-bbva-banking-transformation.md`
    Claim 10 (Peru's query-handling time, ~7.5 minutes → ~1 minute, ~87%): NTT DATA's
    incident-analysis metric (Claim 1 here — 3 days of 5-engineer effort → 30 minutes,
    -99.3%) is a third named OpenAI enterprise case study reporting a large, specific
    before/after time-reduction figure for a technical-investigation task, and the most
    extreme of the three in percentage terms. Unlike AP+'s case, NTT DATA's metrics-box
    figure and body-text description are internally consistent (see Claim 1's assessment)
    rather than exhibiting the AP+ note's unreconciled discrepancy.
  - `blog-openai-codex-knowledge-work.md` Claim 5 (72% of knowledge-worker Codex users
    produce artifacts weekly; 47% engineering operations; 46% code implementation) and
    `blog-openai-agents-transforming-work.md` Claim 8 (over one-fourth of business-function
    Codex work is engineering or coding): NTT DATA's nontechnical-employee use cases (Claims
    7-9 here — lightweight tool building, Excel analysis, direct raw-data analysis
    replacing BI-tool workflows) are a named enterprise instance of exactly the
    role-boundary-dissolution pattern those two aggregate-telemetry reports describe
    statistically. This is the first named single-company case study in the corpus giving
    concrete task-level examples (expense-form transcription, ad hoc analytical reporting)
    for that aggregate pattern, rather than only percentage breakdowns.
  - `blog-openai-agents-transforming-work.md` Claim 5 (non-engineering departments at
    OpenAI itself crossed over to majority-agent usage faster than Engineering did once
    they started) and Claim 7 (non-developer Codex growth vastly outpacing developer
    growth): NTT DATA's expansion of Codex to ~9,000 employees "across technical and
    nontechnical roles" (Claim 2 here), explicitly sequenced after a companywide
    ChatGPT-Enterprise foundation (Claim 3), is a named customer-side instance of the same
    "non-technical adoption follows and can accelerate past technical adoption" pattern
    OpenAI's internal telemetry describes.
  - `blog-anthropic-legal-industry-deploy.md` Claims 6-8, 12, and 15 ("skills as encoded
    institutional knowledge," compounding across teams, and skills governance): NTT DATA's
    "packaging the automation as Skills" for organization-wide adoption of its
    Playwright-based automation (Claim 11 here) is a vendor-independent (OpenAI/Codex, not
    Anthropic/Claude) convergence on the same "package a working automation as a
    reusable, distributable skill unit to scale adoption" mechanism — though NTT DATA's
    article gives none of the governance/versioning/maintenance detail the Anthropic legal
    guide provides.
  - `blog-openai-bbva-banking-transformation.md` Claim 5 (BBVA trained 250 leaders including
    the CEO and chairman; leadership participation as an adoption accelerator) and Claim 4
    (champions/wizards enablement network): NTT DATA's "Deploy ChatGPT Enterprise broadly to
    create network effects through peer learning and word of mouth" leadership lesson
    (Claim 12 here) and its usage-guide/training-driven 1.4x weekly-active-user increase
    (Claim 10 here) are a vendor-consistent restatement of the same
    enablement-drives-adoption mechanism, though NTT DATA's version centers on a
    centralized CoE and general training materials rather than a named champion/wizard
    tier structure.

- **Contradicts**: None filed. No existing corpus source makes a claim that materially
  opposes anything in this article, and the article does not disagree with itself on any
  guidance or claim direction — its two internal metrics (Claim 1's incident-analysis
  reduction and metrics-box percentage) are consistent with each other, unlike the
  same-source inconsistency documented in `blog-openai-australian-payments-plus.md` Claims
  3-4.

- **Extends**:
  - `blog-openai-samsung-chatgpt-codex-deployment.md`: both are OpenAI-authored
    Asia-Pacific enterprise deployment announcements for ChatGPT Enterprise + Codex, but
    NTT DATA's article is materially richer in outcome evidence — Samsung's note documents
    zero Samsung-specific productivity metrics and zero named Samsung-executive quotes
    (`blog-openai-samsung-chatgpt-codex-deployment.md` Claim 7's "vendor-only quoted
    perspective" finding), whereas NTT DATA's article provides one specific quantified
    use-case metric (Claim 1), two named NTT DATA-internal quoted individuals, and a
    five-item leadership-lessons list. The guide should not treat these two
    Asia-Pacific-region OpenAI case studies as evidentiarily equivalent.
  - `blog-openai-codex-knowledge-work.md`: extends that report's aggregate,
    self-reported "Codex is for everyone" usage-segmentation claims with a second named
    enterprise deployment instance (after `blog-openai-australian-payments-plus.md`'s
    security-operations and product-prototyping use cases) in which Codex is applied to
    IT-operations incident analysis specifically — a use case not named among that report's
    own customer vignettes (GroundVue, Proaction, a university professor, a personal
    accessibility-tool builder) or in AP+'s case study.
  - `blog-openai-agents-transforming-work.md`: extends that post's OpenAI-internal
    department-crossover telemetry (Engineering first, then Legal/Finance/Recruiting) with
    a named external-customer instance of the identical sequencing pattern — chat tool
    first, broad nontechnical usage following, agentic/Codex adoption expanding from an
    initial engineering-adjacent proof point (the incident-analysis use case) outward to
    nontechnical functions.

- **Novel**:
  - **"Client Zero" branded internal-dogfooding strategy** (Claim 4): No prior corpus
    source names this specific internal-dogfooding framing (a systems-integrator/IT-services
    company treating its own organization as its "first customer" for the AI transformation
    services it also sells externally). A search of existing source notes for "Client Zero"
    returned zero matches.
  - **IT-operations incident analysis as a named Codex use case** (Claim 1): No prior
    corpus source documents a coding agent applied specifically to incident analysis/root-
    cause investigation for a production system, distinct from the security-operations use
    cases (threat modeling, vulnerability analysis, alert triage) named in
    `blog-openai-australian-payments-plus.md` Claim 5 or the reconciliation-investigation
    use case in the same article's Claims 3-4.
  - **A six-category technical governance checklist for enterprise Codex rollout** (Claim
    6 — data eligibility, system connections, network traffic, sandbox mode, automation
    level, human-review boundary): more granular and more technically specific than the
    governance framings named in prior corpus OpenAI case studies (BBVA's three pillars,
    AP+'s single accountability qualifier, Samsung's generic capability-category language).
  - **Weekly-active-user growth figure causally tied to a named enablement intervention**
    (Claim 10 — 1.4x increase after publishing a usage guide and conducting hands-on
    training): unlike most adoption multipliers in the corpus (which report growth without
    naming a specific triggering intervention), this figure is explicitly attributed to a
    stated cause.

## Guide Impact

- **Chapter 08 or Chapter 10 (Agentic Systems for Incident Response / Observability), if
  either exists or is planned**: Cite NTT DATA's incident-analysis use case (Claim 1) as a
  concrete, named example of a coding agent applied to production-incident investigation,
  but flag prominently that the article discloses no detail on what kind of incident, what
  systems Codex accessed, or what "the full process" (investigation only, or investigation
  plus remediation and documentation) actually consisted of — this is adoption/outcome
  evidence, not an incident-response workflow specification a reader could reproduce.
- **Chapter 05 (Team Adoption)**: Add NTT DATA's "Client Zero" framing (Claim 4) as a named
  instance of the "use internal dogfooding to build both product confidence and external
  sales credibility" adoption strategy — distinct from, but complementary to, the
  champion-network mechanisms already documented from BBVA and the Anthropic legal guide.
  Flag the structural caveat that NTT DATA is an IT-services company with an incentive to
  narrate its own AI adoption as proof of what it sells to clients, which is not true of
  BBVA (a bank) or AP+ (a payments operator).
- **Chapter 05 (Team Adoption)**: Add the CoE's six-category governance checklist (Claim 6
  — data eligibility, system connections, network traffic, sandbox mode, automation level,
  human-review boundary) as a more granular, technically-specific governance-scoping
  template than the three-pillar or single-qualifier framings already documented from BBVA
  and AP+, useful if the guide wants a checklist-style governance artifact for enterprise
  agentic-tool rollout.
- **Chapter 02 (Harness Engineering) or Chapter 05, if discussing skill packaging/reuse**:
  Add NTT DATA's Playwright-automation-packaged-as-Skills pattern (Claim 11) as a second,
  vendor-independent (OpenAI/Codex) example of the "package a working automation as a
  reusable skill unit to scale organization-wide adoption" mechanism already documented in
  depth from Anthropic's legal-industry deployment guide — note NTT DATA's version gives no
  governance, versioning, or maintenance detail, so it should be cited only as
  corroborating evidence that the pattern generalizes across vendors, not as an additional
  operational how-to.
- **Any chapter citing before/after time-reduction metrics from vendor case studies**:
  NTT DATA's incident-analysis figure (-99.3%, three days of five-engineer effort to 30
  minutes) is the most extreme single before/after reduction figure in the corpus's set of
  OpenAI enterprise case studies as of this extraction — cite it alongside AP+'s and BBVA's
  comparable figures (Cross-References → Corroborates) as part of a pattern of
  vendor-reported, single-incident, unaudited before/after metrics, not as a
  representative or typical outcome.

## Extraction Notes

- The live URL (`https://openai.com/index/ntt-data`) returned HTTP 403 to both the WebFetch
  tool and a direct `curl` with a browser user-agent (a client-side JS-app loading-shell
  response with a meta-refresh tag), consistent with the Cloudflare-style bot-protection
  behavior already documented for the `openai.com` domain in every other OpenAI
  customer-story source note in this corpus (BBVA, AP+, Samsung, Notion, Codex-for-knowledge
  -work, agents-transforming-work). This confirms the Prospector's third triage comment,
  which flagged the article as unreadable during triage for the same reason.
  Retrieved instead via a Wayback Machine snapshot
  (`web.archive.org/web/20260727135538/https://openai.com/index/ntt-data/`, crawled July 27,
  2026, five days after the article's July 22, 2026 publication date), fetched directly with
  `curl` (WebFetch is blocked from fetching `web.archive.org` URLs directly in this
  environment — the same workaround documented across the corpus's other OpenAI-domain
  extractions). The archived HTML was parsed with a local Python script that stripped
  `script`/`style` tags and converted block-level tags to newlines before stripping
  remaining markup; all quotes in this note were copied character-for-character from that
  extracted text.
- The article's "Keep reading" footer links to three unrelated OpenAI posts (a "Launching
  Health in ChatGPT" product post, an Effingham County AI-infrastructure/Global-Affairs
  post, and a "how news organizations use AI" company post) — none are substantively linked
  follow-on material for this case study, so none were followed as sub-pages, consistent
  with MINER.md §1's "up to 5 linked pages that seem substantive" guidance (zero of the
  linked pages met that bar).
- The article is short (~900 words including the metrics box and lessons list) and every
  substantive sentence in its body is reflected in one of the twelve claims above; this is
  not a case of shallow reading, but the source itself is thin on operational detail for
  its headline use case — no description of what the "complex incident analysis" or
  "critical system" actually were, no rollout timeline with dates, and no
  individual-contributor-engineer account of the incident-analysis work itself (both quoted
  individuals are AI-function/CoE staff, not the engineers involved in the incident).
- No contradiction issue was filed. Reviewed CONTRADICTIONS.md and the corpus's existing
  OpenAI enterprise-case-study notes; no existing source note makes a claim that materially
  opposes anything in this article, and — unlike `blog-openai-australian-payments-plus.md`
  — this article's own metrics-box and body-text figures for its headline use case are
  mutually consistent, so there was no same-source inconsistency to flag either (see
  Claim 1's assessment).
