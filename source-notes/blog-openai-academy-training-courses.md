---
source_url: https://openai.com/index/academy-courses-applying-ai-at-work
source_type: blog-post
title: "New OpenAI Academy courses for the next era of work"
author: OpenAI
date_published: 2026-06-12
date_extracted: 2026-07-11
last_checked: 2026-07-11
status: current
confidence_overall: emerging
issue: "#1756"
---

# New OpenAI Academy courses for the next era of work

> OpenAI's announcement of three new OpenAI Academy training courses (AI Foundations,
> Applied AI Foundations, Agents and Workflows) forming a self-selected learning path from
> everyday prompting to directing agent-assisted workflows, plus a companion "Champion
> Deployment Guide" — the corpus's first vendor-published, formal internal-training
> curriculum and organizational rollout playbook for AI courses (as distinct from tool/plugin
> deployment guides already in the corpus).

## Source Context

- **Type**: blog-post (OpenAI customer/product-announcement page, `openai.com/index/`,
  ~700 words; auto-discovered via the `openai-news` trusted feed, published June 12, 2026,
  tagged "AI Adoption"). Two linked pages were also read as substantive sub-pages: the
  OpenAI Academy course catalog (`academy.openai.com`) and a public Academy resource titled
  "OpenAI Academy courses: Champion deployment guide" (published the same day, June 12,
  2026, under `academy.openai.com/.../champions-ecqup/resources/...`).
- **Author credibility**: First-party, house-authored OpenAI announcement copy (byline
  "OpenAI"). Maximum authority on what the courses are named, what they claim to cover, and
  how OpenAI recommends organizations deploy them — this is vendor self-description, not an
  independent evaluation of course quality or learning outcomes. Two named executives are
  quoted: Elena Alfaro (Head of Global AI Adoption, BBVA) and Dr. Lan Guan (Chief AI and
  Data Officer, Accenture) — both are partner-organization endorsements selected by OpenAI
  for the announcement, not independent reviews.
- **Scope**: Covers the naming and stated learning objectives of three courses, named
  delivery partners (BCG, Accenture, BBVA), the certificate-of-completion mechanism, and a
  forward-looking roadmap statement. The linked catalog page adds audience-tier framing per
  course and a wider calendar of live, role/sector-specific webinars. The linked Champion
  Deployment Guide adds a five-step organizational rollout framework, a course-to-audience
  routing table, and an adoption-measurement signal framework. Does NOT cover: actual lesson
  content, module-by-module curriculum, assessment design, or completion-rate data — the
  individual course pages (e.g. `academy.openai.com/public/courses/ai-foundations-juzjs`)
  are gated behind Academy sign-in and returned only navigation chrome with no course body
  content when fetched (see Extraction Notes).

## Extracted Claims

### Claim 1: OpenAI frames training/education as an integral part of its product deployment strategy, not a separate marketing function
- **Evidence**: Direct framing statement opening the announcement's substantive section,
  explicitly linking OpenAI's product-building and enterprise-deployment work to the
  Academy's curriculum design.
- **Confidence**: anecdotal (vendor self-framing; no independent evidence of how curriculum
  design actually draws on deployment work)
- **Quote**: "At OpenAI, we view learning as part of deployment. We build the models and
  products and work closely with organizations applying them across their businesses.
  OpenAI Academy turns those insights into practical learning that helps organizations
  build AI fluency across their workforce and shorten the distance between deployment and
  value."
- **Our assessment**: This is a strategic positioning statement, not a falsifiable
  operational claim — no example is given of a specific deployment insight that flowed into
  a specific course module. Still, it establishes OpenAI's own view of why the Academy
  exists: enterprise deployment and workforce training are treated as one continuous
  motion rather than two separate workstreams, which is a framing the guide can note when
  discussing vendor-provided training as an adoption lever.

### Claim 2: The three courses form a single graduated path — from improving one everyday task, to building a repeatable workflow plan, to practicing an agent-assisted workflow
- **Evidence**: Direct statement of course sequencing and intended learning progression.
- **Confidence**: settled (first-party statement of how OpenAI designed the course
  sequence; authoritative on intended structure, not on whether learners actually progress
  this way)
- **Quote**: "Together, the courses take learners from improving one everyday task, to
  building a repeatable workflow plan, to practicing an agent-assisted workflow they can
  apply to future work."
- **Our assessment**: This progression (single-task improvement → workflow plan → agent
  direction) is structurally similar in shape to Anthropic's five-level Cowork maturity
  model in `blog-anthropic-cowork-deploy-guide.md` Claim 2 (Level 0 chat Q&A → Level 1
  building → Level 2 skill → Level 3 bundled/scheduled skills → Level 4 department
  plugins), but compressed into three named courses rather than five named levels, and
  framed as formal training content rather than a self-assessed maturity ladder for tool
  usage. See Cross-References for the audience-tier distinction (Claim 11), which is a
  more direct point of comparison.

### Claim 3: AI Foundations teaches prompting, giving context, output review, and responsible use, aimed at routine tasks like drafting, summarizing, planning, and meeting preparation
- **Evidence**: Direct course-description sentence from the announcement.
- **Confidence**: settled (first-party description of course content as designed)
- **Quote**: "AI Foundations introduces the core concepts and practices for using AI
  effectively in everyday work, including prompting, giving context, output review, and
  responsible use. Learners leave with the foundations they need to apply those habits and
  improve routine tasks such as drafting, summarizing, planning, and meeting preparation."
- **Our assessment**: This is squarely a Chat-tier ("Level 0/1" in Anthropic's taxonomy)
  curriculum — prompting and context-giving for individual, everyday tasks. It corroborates
  the corpus's general pattern that AI adoption training starts with prompting fundamentals
  before workflow or agent content, but is otherwise a generic fundamentals course
  description with no measurable outcome claims.

### Claim 4: Applied AI Foundations teaches turning effective prompts into structured, repeatable workflows by defining inputs, models, tools, checkpoints, and human review while balancing quality, speed, and cost
- **Evidence**: Direct course-description sentence from the announcement.
- **Confidence**: settled (first-party description of course content as designed)
- **Quote**: "Applied AI Foundations teaches how to turn effective prompts into structured,
  repeatable workflows. Learners understand how to develop a workflow plan that defines the
  right inputs, models, tools, checkpoints, and human review, while balancing quality,
  speed, and cost."
- **Our assessment**: The explicit "workflow plan" components named here (inputs, models,
  tools, checkpoints, human review) closely parallel the operational vocabulary in
  Anthropic's deployment guides — e.g. `blog-anthropic-cowork-deploy-guide.md` Claim 10's
  "supervised, then scheduled" validation-checkpoint pattern for moving from Level 2 to
  Level 3. This is the strongest evidence in the announcement that the second course
  targets exactly the same skill (building a checkpointed, reviewable AI workflow) that
  Anthropic's guides describe operationally — independent, cross-vendor convergence on what
  "workflow design" training should include, though OpenAI's version is a training-course
  description with no worked example, unlike Anthropic's guide which pairs the pattern with
  a named case study.

### Claim 5: Agents and Workflows teaches directing agent-assisted work by providing context, defining outputs and boundaries, and reviewing results, with an explicit focus on identifying where human judgment and oversight are required
- **Evidence**: Direct course-description sentence from the announcement.
- **Confidence**: settled (first-party description of course content as designed)
- **Quote**: "Agents and Workflows focuses on how to direct agent-assisted work by providing
  context, defining outputs and boundaries, and reviewing results. Learners leave able to
  run and refine a reusable workflow while identifying where human judgment and oversight
  are required."
- **Our assessment**: "Defining outputs and boundaries" as a named teachable skill
  corroborates the general human-in-the-loop pattern already well-documented in the corpus
  (e.g. the supervised-then-scheduled autonomy progression in
  `blog-anthropic-cowork-deploy-guide.md` Claim 10), but this course description gives no
  worked example of what "boundaries" means operationally (permission scope? task scope?
  approval gates?) — treat as a course-content label, not evidence of a specific technique.

### Claim 6: OpenAI is delivering the Academy courses in partnership with BCG, Accenture, and BBVA to help organizations build practical AI skills
- **Evidence**: Direct statement naming three delivery/enablement partners.
- **Confidence**: anecdotal (named partnership with no detail on what each partner
  specifically contributes — co-delivery, distribution, case-study input, or something else
  is not specified)
- **Quote**: "As part of this effort, we are working with partners including BCG, Accenture,
  and BBVA to help organizations build practical AI skills and apply them in their
  day-to-day work."
- **Our assessment**: BBVA's presence here is notable because BBVA is already documented in
  the corpus (`blog-openai-bbva-banking-transformation.md`) as running its own internal
  two-tier "champions" + "wizards" enablement network (Claim 4) and a 250-leader training
  program (Claim 5). This announcement does not say whether BBVA's internal training
  program is being replaced by, merged with, or run alongside these new Academy courses —
  it only names BBVA as a partner. Treat as evidence that OpenAI is formalizing an
  ecosystem of enterprise training partners, not as evidence that BBVA's own program has
  changed.

### Claim 7: Course completion certificates are positioned as a mechanism for recognizing champions and helping them find peers building similar workflows, not just a credentialing artifact
- **Evidence**: Direct statement describing the intended organizational function of
  certificates beyond individual recognition.
- **Confidence**: anecdotal (vendor-asserted intended use; no evidence given that
  certificates actually produce peer-discovery in practice)
- **Quote**: "Certificates give companies a simple way to recognize participation,
  celebrate early adopters, and connect learning to practical work already underway. They
  can also help champions find peers who are building new workflows and encourage teams to
  share what is working across the organization."
- **Our assessment**: This reframes a credentialing mechanic (a completion certificate) as
  a champion-network bootstrapping tool — the certificate becomes a discoverable signal of
  "this person is engaged with AI enablement," which a manager or peer can use to identify
  candidate champions. This is a novel mechanism in the corpus: existing champion-network
  documentation (BBVA's tiers, Anthropic's champion-authored-skills leading indicator)
  describes champions being identified through workshop leadership or skill authorship, not
  through a certificate-based discovery signal. See Claim 13 for how the Champion
  Deployment Guide operationalizes this ("Share certificates, learner examples, and useful
  workflows").

### Claim 8: BBVA's Head of Global AI Adoption, Elena Alfaro, publicly welcomes OpenAI Academy as a resource for building practical AI skills
- **Evidence**: Direct attributed pull-quote from a named BBVA executive.
- **Confidence**: anecdotal (single executive's endorsement, solicited by OpenAI for a
  product announcement)
- **Quote**: "We welcome initiatives such as OpenAI Academy that help professionals build
  practical AI skills and better understand how to apply these technologies in their
  everyday work,"
- **Our assessment**: Elena Alfaro is the same named executive quoted at length in
  `blog-openai-bbva-banking-transformation.md` (Head of Global AI Adoption at BBVA,
  attributed there as a source for BBVA's three-pillar trust/governance/structured-learning
  adoption strategy). Her presence in both sources is a direct, verifiable link between two
  corpus entries — the same person who led BBVA's internal champions/wizards program (an
  OpenAI ecosystem case study) is now publicly endorsing OpenAI's formal training product.
  This strengthens (without independently validating) the pattern that BBVA's AI-adoption
  leadership is closely and visibly aligned with OpenAI's own enterprise narrative — a
  useful data point for calibrating how much independent weight to give BBVA-sourced claims
  elsewhere in the corpus.

### Claim 9: Accenture's Chief AI and Data Officer argues that scaling AI adoption requires learning systems, confidence, and new ways of working — not just giving people access to the technology
- **Evidence**: Direct attributed pull-quote from a named Accenture executive.
- **Confidence**: anecdotal (single executive's framing, solicited by OpenAI for a product
  announcement; no measurement or study cited)
- **Quote**: "Scaling AI adoption is not just about giving people access to technology. It
  requires the learning systems, confidence, and new ways of working that help people apply
  AI every day,"
- **Our assessment**: This is a direct, named-executive articulation of the "adoption is
  organizational change, not tooling" claim that the corpus has already documented
  repeatedly from Anthropic-ecosystem sources (e.g. `blog-openai-bbva-banking-transformation.md`
  Claim 11's "Leadership lessons" list, itself flagged there as likely OpenAI house framing
  rather than independent convergence). Coming from an Accenture executive in an
  OpenAI-published announcement, this quote should be read the same way: as further evidence
  of a consistent narrative that vendors and their consulting partners jointly promote
  around AI adoption, not as an independent confirmation from a source outside that
  ecosystem.

### Claim 10: OpenAI Academy's curriculum is built cross-functionally (research, product, safety, deployment teams) and is explicitly framed as continuously evolving, with a stated roadmap for expanded reporting and new role-specific learning paths
- **Evidence**: Direct statements describing curriculum authorship and forward-looking
  plans.
- **Confidence**: anecdotal (vendor roadmap statement; no committed timeline or specific
  named future course)
- **Quote**: "OpenAI Academy is shaped by teams across AI research, product, safety, and
  deployment. The curriculum can evolve alongside our models and products, incorporating
  new capabilities, updated safety practices, and lessons from how organizations put AI to
  work." ... "These courses are the beginning of a broader OpenAI Academy learning roadmap.
  We will continue updating them as our products evolve, expand reporting capabilities for
  organizations, and introduce new learning paths for additional roles and use cases."
- **Our assessment**: "Expand reporting capabilities for organizations" is the only
  concrete forward-looking commitment in the announcement, and it directly matches a gap
  the Champion Deployment Guide already flags as a current limitation (Claim 15: enterprise
  reporting today depends on users signing in with a work email or enterprise "Sign in with
  ChatGPT," and completion-signal collection requires contacting an OpenAI account team).
  This is internally consistent — the announcement's roadmap promise addresses a real,
  named gap in the day-one reporting tooling — which is a small but genuine point of
  self-consistency across the two linked pages.

### Claim 11: The OpenAI Academy catalog page maps each of the three courses to a self-assessed experience tier, letting learners choose an entry point rather than requiring everyone to start at the same level
- **Evidence**: Direct audience labels shown next to each course on the public Academy
  catalog page (`academy.openai.com`).
- **Confidence**: settled (first-party UI copy visible on the live catalog page as
  archived; authoritative on how the catalog presents course entry points)
- **Quote**: "Great for people new to AI" [AI Foundations] ... "Great for people who already
  have some experience" [Applied AI Foundations] ... "For people comfortable using AI"
  [Agents and Workflows]
- **Our assessment**: This is a meaningful structural difference from Anthropic's five-level
  Cowork maturity model (`blog-anthropic-cowork-deploy-guide.md` Claim 2), which is
  explicitly a single ladder where "nobody is expected to jump straight to the top" and
  "Chat is everyone's Level 0" — i.e., Anthropic's model assumes a shared starting point
  with staged progression. OpenAI's catalog instead lets a learner who is "comfortable
  using AI" enroll directly in the most advanced course (Agents and Workflows) without
  passing through the two lower-tier courses. Both models describe a graduated skill
  ladder, but Anthropic's is sequential-for-everyone while OpenAI's is
  self-selected-entry-point. The Champion Deployment Guide's own audience-routing table
  (Claim 15) softens this distinction somewhat by recommending organizations "may also
  recommend a common starting course to create a shared baseline" — so OpenAI's guidance
  to Champions leans back toward Anthropic's shared-starting-point model even though the
  catalog UI itself supports self-selected entry.

### Claim 12: Beyond the three core courses, OpenAI Academy runs an ongoing calendar of live, audience-segmented webinars organized by department and sector (e.g. "How sales teams use Codex," "How finance teams use Codex," legal-aid and higher-education-specific sessions)
- **Evidence**: Direct listing of upcoming and on-demand events on the Academy catalog
  page, each tagged with an audience segment ("Work Users," "Higher Education," "Builders").
- **Confidence**: settled (first-party event listing visible on the live catalog page as
  archived on June 18, 2026; describes what events exist, not their attendance or impact)
- **Quote**: "How business operations teams use Codex" ... "How marketing teams use Codex"
  ... "How sales teams use Codex" ... "How data science teams use Codex" ... "How finance
  teams use Codex" ... "AI foundations for legal aid professionals" ... "SME AI Accelerator
  - en français"
- **Our assessment**: This is a distinct, more granular enablement layer than the three
  named courses in the announcement — a recurring, function-specific webinar series (one
  half-hour session per business function: sales, finance, marketing, data science, business
  operations) plus sector-specific sessions (higher education, legal aid, a French-language
  "SME AI Accelerator"). The three formal courses are the structured curriculum; this
  webinar calendar is the higher-frequency, lower-commitment enablement layer around it.
  Neither the announcement blog post nor the catalog page states whether webinar attendance
  counts toward any course or certificate. This is new to the corpus: no existing source
  documents a vendor running a standing, function-segmented live-training calendar alongside
  a formal course curriculum.

### Claim 13: OpenAI publishes a dedicated "Champion Deployment Guide" prescribing a five-step organizational rollout of the Academy courses: Activate, Engage sponsors, Launch, Reinforce and measure, Share
- **Evidence**: Full five-section structure of the linked Champion Deployment Guide
  resource page, each section with named sub-actions.
- **Confidence**: settled (first-party prescriptive framework, structured and internally
  consistent, with explicit named actions for each of the five steps)
- **Quote**: "Use this guide to plan and run a course deployment inside your organization.
  It will help you: Activate: Make courses available to the broadest possible employee
  audience Engage sponsors: Secure visible leadership support and manager reinforcement
  Launch: Drive awareness through a coordinated organization-wide communications campaign
  Reinforce and measure: Maintain momentum ,track enrollment, completion, and changes in
  adoption Share: Make progress, outcomes, and examples visible, exchange lessons with other
  Champions"
- **Our assessment**: This is a formal, named rollout framework for *training content*
  distribution, structurally parallel to (but distinct in subject from) Anthropic's
  three-phase Evaluate→Pilot→Scale roadmap for *tool* deployment
  (`blog-anthropic-cowork-deploy-guide.md` Claim 5) and the Foundation→Pilot→Scale roadmap
  for legal-tool deployment (`blog-anthropic-legal-industry-deploy.md` Claim 9). Both
  vendors converge on the same underlying idea — a named, staged, Champion-driven rollout
  process is the standard model for enterprise AI enablement — but OpenAI's five steps are
  a communications/change-management sequence (sponsor engagement, launch messaging,
  measurement cadence, story-sharing) for rolling out *courses*, whereas Anthropic's
  phases are a product-adoption sequence (security review, connector setup, skill
  authorship, plugin marketplace provisioning) for rolling out a *tool*. See Claim 14 for a
  specific point of tension between the two vendors' guidance on rollout scope.

### Claim 14: The Champion Deployment Guide explicitly recommends deploying courses to the broadest possible employee audience by default, rather than starting with a small pilot cohort
- **Evidence**: Direct statement in the "Activate" step explaining the rationale for
  broad-access-first deployment.
- **Confidence**: emerging (first-party prescriptive recommendation with a stated rationale;
  not empirically validated against a small-pilot-first alternative)
- **Quote**: "Start by making the courses available to everyone who can benefit. The default
  should be broad access rather than limiting participation to a small cohort. A
  company-wide deployment creates a shared starting point, allows employees to choose
  learning relevant to their needs, and gives the organization a stronger foundation for
  future AI enablement."
- **Our assessment**: This is worth flagging explicitly against Anthropic's guidance,
  though we do not believe it rises to a MINER.md §4a contradiction (see Extraction Notes
  for the reasoning). Anthropic's Cowork and legal-industry deployment guides both
  explicitly recommend starting with "2-3 champion teams" in a Foundation/Evaluate phase
  before any broader rollout (`blog-anthropic-cowork-deploy-guide.md` Claim 5;
  `blog-anthropic-legal-industry-deploy.md` Claim 9), with company-wide access arriving only
  in the final Scale phase (months 4-6). OpenAI's guide recommends the opposite default for
  *course access specifically*: skip the small-cohort pilot and make training available
  company-wide from day one. We read this as a conditioning-variable difference rather than
  a true contradiction — the artifact being rolled out differs (self-paced training content
  with no system access or security surface, versus a production tool wired into
  connectors, data sources, and permission systems that specifically benefits from
  incremental, security-reviewed rollout). The guide should present both patterns with that
  distinction made explicit: broad-access-first for low-risk enablement content, phased
  pilot-first for production tooling with data/system access.

### Claim 15: The guide provides a course-to-audience routing table and a five-signal framework for measuring course-deployment progress (completion, awareness, application, adoption, progression), with an explicit caveat that enterprise-level reporting depends on SSO or work-email sign-in
- **Evidence**: Two structured tables in the guide's "Activate" and "Reinforce and measure"
  sections, plus an explicit reporting-dependency caveat.
- **Confidence**: settled (first-party structured guidance; the reporting-dependency caveat
  is a factual product constraint, not an aspiration)
- **Quote**: "Please note: Enterprise reporting is dependent on users using their work email
  domain or using \"Sign in with ChatGPT\" an choosing their enterprise account. Enterprise
  admins must enable Sign in with ChatGPT for that option to be available."
- **Our assessment**: The routing table (AI Foundations → "employees building core AI
  knowledge and confidence"; Applied AI Foundations → "active users ready to develop more
  structured and repeatable ways of working"; Agents & Workflows → "employees ready to
  explore agent-assisted workflows") gives Champions a concrete decision rule for pointing
  different employees at different courses — a more operational version of the
  self-selected-entry-point pattern in Claim 11. The five-signal framework (completion,
  awareness, application, adoption, progression) is notable for naming "application" and
  "progression" as distinct, harder-to-measure signals alongside the easy-to-measure
  "completion" — an implicit acknowledgment that certificate counts alone do not prove
  behavior change. The reporting caveat (including its verbatim "an choosing" typo in the
  source) is the most concrete IT/measurement constraint in either linked page: without
  enterprise SSO or "Sign in with ChatGPT" configured, an organization cannot get
  aggregate completion data from OpenAI at all and must "contact your OpenAI account team"
  even for the most basic signal.

## Concrete Artifacts

```
Source: OpenAI, "New OpenAI Academy courses for the next era of work,"
https://openai.com/index/academy-courses-applying-ai-at-work (published June 12, 2026;
retrieved via Wayback Machine snapshot — see Extraction Notes)

Three courses (verbatim course-description sentences):
  AI Foundations: "introduces the core concepts and practices for using AI effectively in
    everyday work, including prompting, giving context, output review, and responsible use."
  Applied AI Foundations: "teaches how to turn effective prompts into structured, repeatable
    workflows... a workflow plan that defines the right inputs, models, tools, checkpoints,
    and human review, while balancing quality, speed, and cost."
  Agents and Workflows: "focuses on how to direct agent-assisted work by providing context,
    defining outputs and boundaries, and reviewing results."

Named delivery/enablement partners: BCG, Accenture, BBVA.
```

```
Source: OpenAI Academy course catalog, https://academy.openai.com/
(retrieved via Wayback Machine snapshot dated June 18, 2026)

Course-to-audience tier labels (verbatim, catalog homepage):
  AI Foundations                — "Great for people new to AI"
  Applied AI Foundations        — "Great for people who already have some experience"
  Agents and Workflows          — "For people comfortable using AI"

Live event calendar sample (verbatim titles, as listed June 18, 2026):
  - SME AI Accelerator - en français
  - Builder Bootcamp: Agents / Builder Bootcamp: Codex / Builder Bootcamp: Evals
  - How business operations teams use Codex
  - How marketing teams use Codex
  - How sales teams use Codex
  - How data science teams use Codex
  - How finance teams use Codex
  - Codex for Everyday Use / Codex Fundamentals / Codex for Admins and IT
  - Creating Workspace Agents for Higher Ed Faculty and Researchers
  - Creating Workspace Agents for Higher Education Staff/Admin
  - AI foundations for legal aid professionals

Note: individual course detail pages (e.g. academy.openai.com/public/courses/ai-foundations-juzjs)
require Academy sign-in; fetching the archived snapshot returned only site navigation chrome,
no module/lesson content.
```

```
Source: "OpenAI Academy courses: Champion deployment guide," published June 12, 2026,
https://academy.openai.com/public/clubs/champions-ecqup/resources/openai-academy-courses-champion-deployment-guide-2026-06-11
(retrieved via Wayback Machine snapshot dated June 16, 2026)

Five-step deployment framework (verbatim step names):
  1. Activate      — "Make courses available to the broadest possible employee audience"
  2. Engage sponsors — "Secure visible leadership support and manager reinforcement"
  3. Launch         — "Drive awareness through a coordinated organization-wide communications campaign"
  4. Reinforce and measure — "Maintain momentum, track enrollment, completion, and changes in adoption"
  5. Share          — "Make progress, outcomes, and examples visible, exchange lessons with other Champions"

Course-to-audience routing table (verbatim):
  Course                  | Recommended audience                                          | Use when
  AI Foundations          | Employees building core AI knowledge and confidence           | Employees need a practical introduction to using AI effectively in everyday work
  Applied AI Foundations  | Active users ready to develop more structured and repeatable   | Employees understand the basics and want to apply AI to recurring work
                          | ways of working                                                |
  Agents & Workflows      | Employees ready to explore agent-assisted workflows            | Employees are ready to direct more structured workflows while applying appropriate human judgment and oversight

Suggested 4-week reinforcement cadence (verbatim):
  Launch day — Executive sponsor announcement and organization-wide communications
  Week 1     — Manager reinforcement and internal AI community promotion
  Week 2     — Reminder featuring an employee example, certificate, or course takeaway
  Week 3     — Office hour, team discussion, or application session
  Week 4     — Share progress, recognize participation, and highlight what comes next

Five-signal adoption measurement framework (verbatim signal names and "what it tells you"):
  Course completion   — Whether employees are participating in the learning
  Awareness and reach — Whether employees saw and understood the launch
  Application         — Whether employees are applying the learning
  Adoption             — Whether AI usage is changing
  Progression          — Whether employees are moving into more advanced work

Reporting caveat (verbatim, including source typo "an choosing"):
  "Enterprise reporting is dependent on users using their work email domain or using
  \"Sign in with ChatGPT\" an choosing their enterprise account. Enterprise admins must
  enable Sign in with ChatGPT for that option to be available."

"Position the value" talking points for sponsors (verbatim bullet list):
  - Built by OpenAI: Developed by the teams building the technology
  - Designed for real work: Focused on practical workplace application
  - Continuously updated: Evolves alongside OpenAI products and best practices
  - Learn by doing: Connects learning to real tasks and workflows
  - Recognizes progress: Learners can earn course completion certificates and OpenAI
    Academy badges

Deployment summary template (verbatim field list, for post-launch read-outs at 8-12 weeks):
  Organization or audience reached / Executive sponsor / Launch channels / Courses promoted /
  Participation or completion signals / Employee examples / What worked / What was difficult /
  What we will do next
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-cowork-deploy-guide.md` Claim 9 (champion-authored skills as leading
    pilot indicator) and Claim 5 (three-phase roadmap driven by named champions): OpenAI's
    Champion Deployment Guide (Claim 13) independently confirms that a formal, named
    "Champion" role and a staged organizational rollout playbook are now a standard
    enterprise-AI-adoption pattern across both major-lab ecosystems (Anthropic and OpenAI),
    not an Anthropic/Cowork-specific prescription. This corroborates the same conclusion
    already reached from `blog-openai-bbva-banking-transformation.md` Claim 4 (BBVA's
    champions/wizards network), but this time from OpenAI's own product documentation
    rather than a customer case study.
  - `blog-anthropic-cowork-deploy-guide.md` Claim 4 and Claim 13 (tribal-knowledge/skill
    codification as organizational infrastructure): The Applied AI Foundations course
    description (Claim 4) and the Agents and Workflows course description (Claim 5) target
    the same underlying skill — turning ad hoc AI use into a reviewable, checkpointed,
    reusable workflow — that Anthropic's guide describes operationally through its Skills
    and plugin-stacking mechanisms. This is independent, cross-vendor agreement on what
    "workflow design" competency should include, though OpenAI's version is training-course
    marketing copy with no worked example.
  - `blog-openai-bbva-banking-transformation.md` Claim 11 (OpenAI's consistent house framing
    of "adoption is organizational change, not tooling" across customer stories): Dr. Lan
    Guan's Accenture quote (Claim 9 here — "not just about giving people access to
    technology... requires the learning systems, confidence, and new ways of working") is
    the same framing pattern, now voiced by a different named partner executive in a
    different OpenAI-published piece, reinforcing that this is a consistently promoted
    narrative across OpenAI's ecosystem rather than independent convergence.

- **Contradicts**: None filed as a formal contradiction issue. One point of tension is
  flagged and analyzed but treated as a conditioning-variable difference rather than a
  material contradiction — see Claim 14 and Extraction Notes: OpenAI's Champion Deployment
  Guide recommends broad, company-wide access to courses from day one, while Anthropic's
  `blog-anthropic-cowork-deploy-guide.md` Claim 5 and `blog-anthropic-legal-industry-deploy.md`
  Claim 9 both recommend starting with a small (2-3 team) champion pilot before scaling to
  company-wide. We judge the underlying artifacts (self-paced training content vs. a
  production tool with system connectors and security surface) to differ enough that this
  is not a same-topic disagreement requiring a CONTRADICTIONS.md entry, but the Smith should
  be aware both patterns exist in the corpus and apply to different kinds of rollout.

- **Extends**:
  - `blog-openai-bbva-banking-transformation.md`: BBVA is named as an Academy delivery
    partner here (Claim 6) and its Head of Global AI Adoption, Elena Alfaro, is directly
    quoted in both sources (Claim 8) — this is a verified, direct link between two corpus
    entries rather than a general topical similarity.
  - `blog-anthropic-cowork-deploy-guide.md` and `blog-anthropic-legal-industry-deploy.md`:
    extends the corpus's champion-driven deployment-roadmap pattern with OpenAI's own
    formal, named "Champion Deployment Guide" (Claim 13) — the first vendor-published
    rollout playbook in the corpus that is specifically about deploying *training content*
    rather than a *tool*, giving the guide a clean point of contrast between the two
    deployment types.

- **Novel**:
  - **Formal, named multi-course AI training curriculum from a major lab** (Claims 2-5):
    No prior corpus source documents a structured, named, multi-course curriculum (as
    opposed to a deployment guide, a product announcement, or a customer case study) from
    either OpenAI or Anthropic.
  - **Certificate-as-champion-discovery mechanism** (Claim 7): The explicit framing of
    completion certificates as a tool for finding and recognizing champions (rather than
    just individual credentialing) is new to the corpus.
  - **Self-selected course entry point vs. shared-starting-point maturity ladder** (Claim
    11): The contrast between OpenAI's per-course audience tiers and Anthropic's single
    shared-Level-0-for-everyone model is a new structural comparison point for the guide.
  - **Standing, function/sector-segmented live webinar calendar** (Claim 12): No prior
    corpus source documents a vendor running a recurring, granular (department- and
    sector-specific) live-training calendar as a companion to a formal course curriculum.
  - **Formal training-rollout Champion playbook, distinct from tool-rollout playbooks**
    (Claims 13-15): The five-step Activate/Engage sponsors/Launch/Reinforce-and-measure/Share
    framework, the audience-routing table, the reinforcement cadence, and the five-signal
    measurement framework are all new artifacts in the corpus — the first time a rollout
    playbook is specifically about training-content distribution rather than tool/plugin
    deployment.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Add OpenAI Academy's three-course structure (Claims 2-5)
  and its Champion Deployment Guide (Claims 13-15) as a second, vendor-independent example
  of a formal enterprise AI-training rollout, alongside Anthropic's Cowork and legal-industry
  deployment guides. Present the course-audience routing table and five-signal measurement
  framework (Claim 15) as a concrete, reusable checklist for any organization running a
  training-content rollout (distinct from a tool-deployment rollout).
- **Chapter 05 (Team Adoption)**: Add the broad-access-vs-pilot-first distinction (Claim 14)
  as explicit guidance: default to broad access for low-risk training content; default to a
  small champion pilot for production tools with system/data access. Cite both OpenAI's
  Champion Deployment Guide and Anthropic's Cowork/legal-industry guides as the two sides of
  this conditioning variable.
- **Chapter 05 (Team Adoption)**: Add the certificate-as-champion-discovery mechanism
  (Claim 7) as a novel, low-cost complement to the champion-identification methods already
  in the guide (workshop leadership, skill authorship) — a completion certificate can double
  as a discoverable signal for who to recruit as a champion.
- **Chapter 05 (Team Adoption), if discussing role-specific enablement**: Add the
  function/sector-segmented webinar calendar (Claim 12) as an example of a higher-frequency,
  lower-commitment enablement layer that can run alongside a formal course curriculum,
  distinct from the courses themselves.
- **Any chapter citing vendor-partner testimonial quotes**: Flag Elena Alfaro's and Dr. Lan
  Guan's quotes (Claims 8-9) as ecosystem-aligned partner endorsements, not independent
  evaluations — consistent with the existing caution already applied to
  `blog-openai-bbva-banking-transformation.md`'s "Leadership lessons" framing.

## Extraction Notes

- **The live source URL returned a client-side loading shell, not the article**: Both
  WebFetch and direct `curl` with a browser user-agent against
  `https://openai.com/index/academy-courses-applying-ai-at-work` returned HTTP 403 (WebFetch)
  or a JS-loading-spinner shell (curl), consistent with prior OpenAI-domain extraction
  difficulties noted in `blog-openai-bbva-banking-transformation.md`'s and
  `blog-openai-endava-frontiers.md`'s Extraction Notes. The article was retrieved via a
  Wayback Machine snapshot (`web.archive.org/web/20260617030416/https://openai.com/index/academy-courses-applying-ai-at-work/`),
  HTTP 200, full rendered HTML. Text was extracted with a local Python regex-based tag
  strip (removing `script`/`style` blocks, converting block-level closing tags to
  newlines), not WebFetch, since WebFetch in this environment refuses to fetch
  `web.archive.org` directly. All quotes were copied character-for-character from that
  extracted text.
- **Two substantive linked pages were followed, per MINER.md §1's "follow up to 5 linked
  pages" allowance**: (1) the OpenAI Academy course catalog homepage
  (`academy.openai.com`, Wayback snapshot dated June 18, 2026), and (2) the "OpenAI Academy
  courses: Champion deployment guide" resource page, discovered via the Wayback CDX index
  for `academy.openai.com` and retrieved as a Wayback snapshot dated June 16, 2026 — both
  fetched the same way (curl + Wayback Machine + local tag-stripping) since WebFetch cannot
  reach `web.archive.org`.
- **Individual course detail pages were attempted but are gated**: The catalog's "Go to
  course" links resolve to per-course pages (e.g.
  `academy.openai.com/public/courses/ai-foundations-juzjs`) and a corresponding `_next/data`
  JSON API (e.g. `.../public/courses/ai-foundations-juzjs.json`). The archived JSON endpoints
  returned empty `{}` bodies (likely because the archived crawl did not carry the
  authenticated request headers needed to populate them), and the archived course-page HTML
  returned only site navigation chrome with a "SIGN IN" prompt and no course body content.
  This means the note cannot describe actual lesson/module content for any of the three
  courses — only the one-paragraph descriptions published on the announcement and catalog
  pages. This is a genuine scope limit, not a case of skipping available content.
- **Contradiction analysis (MINER.md §4a)**: The tension between OpenAI's broad-access-first
  course rollout recommendation (Claim 14) and Anthropic's small-pilot-first tool rollout
  recommendation was evaluated against the filing criteria. We did not file a contradiction
  issue: the two sources recommend different rollout defaults for different kinds of
  artifact (self-paced training content with no system/data access, vs. a production tool
  wired into connectors and permission systems). This reads as a conditioning variable
  (what is being rolled out) rather than a same-topic disagreement where both sides would
  give different advice for the same situation. CONTRADICTIONS.md and open
  `contradiction`-labeled issues were checked before this note was finalized; nothing
  existing covers this topic.
- **Confidence calibration**: The three course descriptions and the Champion Deployment
  Guide's structural content (steps, tables, cadence) are first-party, settled descriptions
  of what OpenAI publishes and prescribes — authoritative for "this is what OpenAI says,"
  not for "this works." The partner quotes (Elena Alfaro, Dr. Lan Guan) are anecdotal,
  solicited endorsements. No independent, third-party, or outcome-based evidence appears
  anywhere in either linked page — no completion-rate, satisfaction, or behavior-change data
  is cited for the courses themselves. Overall: **emerging**, matching the calibration
  already applied to Anthropic's comparable deployment guides
  (`blog-anthropic-cowork-deploy-guide.md`, `blog-anthropic-legal-industry-deploy.md`) —
  first-party prescriptive material with no independently validated outcome data.
- All cross-reference claim numbers cited above (from `blog-anthropic-cowork-deploy-guide.md`,
  `blog-anthropic-legal-industry-deploy.md`, and `blog-openai-bbva-banking-transformation.md`)
  were verified by re-reading each cited note's actual claim numbering and content before
  writing this note; none were guessed.
