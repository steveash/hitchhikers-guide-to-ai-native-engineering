---
source_url: https://martinfowler.com/fragments/2026-07-21.html
source_type: blog-post
title: "Fragments: July 21"
author: Martin Fowler (curator); primary data source is Thoughtworks's "The Future of Software Engineering" retreat report (June 28-30, 2026, Engelberg, Switzerland); linked contributors Kelsey Hightower, Jason Koebler (404 Media), Unmesh Joshi, Spender Nelson
date_published: 2026-07-21
date_extracted: 2026-07-22
last_checked: 2026-07-22
status: current
confidence_overall: emerging
issue: "#2130"
---

# Fragments: July 21 (Martin Fowler)

> Fowler closes out his coverage of Thoughtworks's second Future of Software
> Development Retreat by publishing its official report, which names five
> headline findings — verification (not code generation) is the new
> bottleneck, harness engineering is an emerging ownable discipline, an
> apprenticeship crisis is colliding with agentic adoption, the
> executive/engineer expectation gap is a bigger risk than any model
> limitation, and legacy modernization is the clearest near-term value pool —
> backed by concrete retreat data (4x token-usage reduction from harnessing,
> 60%→80% first-pass merge acceptance from a judge-council pattern, 20x
> security-incident growth in six months, $5,000/3-day COBOL-compiler
> generation). Fowler's own fragment adds a cautionary air-filter deployment
> story ($50M saved, $100B lost to context mismatch), operations/agent
> patterns, a DSL-reliability discussion citing Unmesh Joshi and Spender
> Nelson, and a personal essay on "LLM-speak" fatigue and reading drafts aloud
> as a countermeasure.

## Source Context

- **Type**: blog-post (Fowler's "Fragments" series, July 21, 2026 entry — the
  third and closing installment on the July 2026 Thoughtworks Future of
  Software Development Retreat, following `blog-fowler-fragments-2026-07-06.md`
  and `blog-fowler-fragments-2026-07-13.md`). This entry's defining feature is
  that it links to and quotes from the retreat's official published report —
  "The Future of Software Engineering" (Thoughtworks, June 2026,
  `tw_future_of_software_engineering_europe_2026.pdf`, 16 pages) — rather than
  relying solely on Fowler's own first-hand session paraphrase, as the two
  prior fragments did.
- **Author credibility**: Martin Fowler is Chief Scientist at Thoughtworks,
  author of *Refactoring* and *Patterns of Enterprise Application
  Architecture*, and an original Agile Manifesto signatory. The
  `martinfowler.com` feed is designated `trusted-feed` in this repository.
  Fowler both attended the retreat and co-convened it with Thoughtworks. The
  linked Thoughtworks report itself is presented as synthesizing 40
  unconference-style sessions of "senior technologists, CTOs, CEOs, architects
  and consultants." Other named/linked contributors in this fragment: Kelsey
  Hightower (quoted via a linked Bluesky post); Jason Koebler (404 Media,
  quoted via a linked article, "Your AI Use Is Breaking My Brain" — 404 Media
  previously corroborated in this corpus via `blog-fowler-fragments-2026-07-06.md`
  and `blog-thoughtworks-kamelman-token-crisis.md`); Unmesh Joshi
  (Distinguished Engineer at Thoughtworks, author of *Patterns of Distributed
  Systems*, whose article "DSLs Enable Reliable Use of LLMs" is linked and was
  followed for this note); Spender Nelson (quoted via a linked Firetiger blog
  post, not independently followed).
- **Scope**: Covers five topics in order: (1) the Thoughtworks retreat report
  and its five headline findings, with deep-dive material on the
  executive/engineer divide, citizen-development risk, and the AI bubble; (2)
  LLMs in operations; (3) DSLs as an LLM-reliability pattern; (4) an essay on
  "LLM-speak" prose fatigue and the "Say Your Writing" countermeasure. This
  note additionally follows and incorporates primary-source detail from the
  linked Thoughtworks report PDF, Fowler's own `VibeCoding` and
  `SayYourWriting` bliki pages, Unmesh Joshi's DSL article, and Korny
  Sietsma's "Agentic AI and Security" article (the source of the "Lethal
  Trifecta" concept Fowler links to) — five linked pages followed in total,
  per MINER.md's "up to 5" guidance. Does NOT independently follow: the
  Spender Nelson/Firetiger post (already fully quoted within Fowler's own
  fragment text), the Stanford law-professors study beyond its abstract
  figures, or the Qu poll on AI-bubble sentiment (see Extraction Notes).

## Extracted Claims

### Claim 1: The Thoughtworks retreat report names five headline findings spanning nearly every session: verification (not code generation) is the new bottleneck; harness engineering is an emerging, ownable discipline; organizations face a real apprenticeship crisis; the executive/engineer expectation gap is a bigger risk than any technical limitation; and legacy modernization is the clearest, most defensible near-term value pool
- **Evidence**: Verbatim bullet list from the retreat's official published
  report, which Fowler links to and introduces ("They have five headline
  findings"); the same five bullets appear near-identically in the report's
  own executive summary (followed primary source, `tw_future_of_software_engineering_europe_2026.pdf`,
  p.2).
- **Confidence**: emerging (a named, credentialed industry report
  synthesizing 40 sessions at a named unconference, but the report itself
  states its value "was not necessarily consensus but instead the range and
  seriousness of the thinking" — i.e., it is qualitative synthesis, not a
  measured survey)
- **Quote**: "Code generation is no longer the bottleneck — verification is."
  ... "'Harness engineering' is emerging as a distinct, ownable discipline."
  ... "Organizations are colliding with a real apprenticeship crisis." ...
  "The executive/engineer expectation gap is a bigger risk than any technical
  limitation." ... "Legacy modernization is the clearest, most defensible
  near-term value pool."
- **Our assessment**: This is the single most citable framing in the source
  and the first time in this corpus's Fowler-fragments coverage that a formal,
  publishable Thoughtworks report — rather than Fowler's own session
  paraphrase — is available and linked. It should be treated as this corpus's
  primary anchor citation for "verification is the new bottleneck," a claim
  this corpus has approached piecemeal (code-review-bottleneck findings in
  `discussion-hn-autofix-hybrid-review.md`, SDLC-disruption claims in
  `blog-simonwillison-vibe-coding-agentic-engineering.md`) but not yet cited
  to a named industry report making the claim as an explicit headline finding.
  Each of the five findings is elaborated with concrete supporting detail in
  the fuller report (Claims 2-12 below); the guide should cite the aggregate
  finding here and the specific data points from those claims separately,
  since the headline bullets alone are not self-supporting.

### Claim 2: The retreat's report documents a new, human-legible testing vocabulary displacing generic BDD frameworks, a three-stage verification stack for legacy migrations, and a "council of judges" pattern that raised first-pass merge acceptance from roughly 60% to 80%
- **Evidence**: Retreat report's "Verification, not generation, is the new
  bottleneck" section (followed primary source, PDF pp.4-5), presented as
  named practices demonstrated live at sessions, not speculative proposals.
- **Confidence**: emerging (named, demonstrated techniques with one concrete
  measured before/after figure — 60%→80% — from a single unnamed team)
- **Quote**: "A new testing vocabulary is emerging. 'Constraint tests' (single
  input/output tests that box in what an agent is allowed to generate),
  'scenario tests' and 'good/bad logs' (derived from real production
  incidents) were named and demonstrated live. Custom, purpose-built
  approval-testing rigs which were built in hours are proving more effective
  than generic BDD frameworks. This is partly because they keep the
  human-reviewable surface simple and hard for an agent to game."
- **Quote**: "A layered trust-verification stack is forming for high-stakes
  migration work. It looks like this: characterization tests (behavioral
  capture from the legacy system) → symbolic execution (mathematically
  grounded, not AI-generated) → production 'back tests' against real data
  flows."
- **Quote**: "There was discussion about how one team combined linters and
  pattern-matching with a three-model 'council of judges,' raising first-pass
  merge acceptance from roughly 60% to 80%."
- **Our assessment**: This is a substantial, concrete elaboration of the
  "verification is the bottleneck" headline finding (Claim 1) that no prior
  corpus note has captured: a named testing vocabulary (constraint tests,
  scenario tests, good/bad logs) explicitly designed to be "hard for an agent
  to game," a three-stage migration-verification stack, and one of this
  corpus's few *measured* before/after figures for an LLM-judge ensemble
  technique (60%→80% merge acceptance). The report elsewhere adds a pull-quote
  worth preserving as a design principle: conformance tests are explicitly
  ranked above specifications when the two disagree — directly corroborating
  `blog-fowler-fragments-2026-07-13.md` Claim 12 (Sam Ruby/Fowler's
  "conformance tests (sensors) are more valuable than specifications
  (guides)").

### Claim 3: The report states that no one at the retreat could cite data on how many defects manual code review actually catches, calling this a "status quo illusion" that organizations should challenge with evidence rather than continue treating review as a de facto quality guarantee
- **Evidence**: Retreat report's verification section (followed primary
  source, PDF p.4) and its "Actions for technical leaders" section (PDF p.11),
  which both name this as an open recommendation.
- **Confidence**: emerging (a named, repeated observation across multiple
  retreat practitioners, but stated as an absence of data rather than a
  positive finding)
- **Quote**: "The long-standing faith in manual code review is being openly
  questioned. Multiple practitioners pointed out that no one in the room could
  cite data on how many defects manual review actually catches — a 'status
  quo illusion' that needs to be challenged with evidence."
- **Quote**: "Stop treating manual code review as a de facto quality
  guarantee; measure it. If your organization can't produce data on defects
  actually caught by review, treat that as a real gap, not a formality."
- **Our assessment**: This is a pointed, guide-relevant challenge to an
  assumption implicit across much of this corpus's code-review coverage
  (e.g., `blog-simonwillison-vibe-coding-agentic-engineering.md` Claims 2-3 on
  normalization of deviance and the accountability gap, which both assume
  manual review is the meaningful safeguard being eroded). The report doesn't
  argue review is worthless — it argues the *evidence base* for review's
  effectiveness has never been established, which is a distinct and sharper
  claim than "review discipline is eroding." A guide section on code review
  practice should present this as an open measurement gap organizations
  should close, not assume review's defect-catch rate is known or high.

### Claim 4: The report documents measured harness-engineering results — one organization cut token usage by at least 4x and increased output determinism using an effective harness; converting a linter's diagnostic output into step-by-step deterministic refactoring instructions ("habit hooks") raised code-smell resolution from under 50% to roughly 90%; and the best-performing teams let agents propose their own harness edits via a "learn" loop rather than hand-authoring the harness
- **Evidence**: Retreat report's "Harness engineering is becoming a distinct,
  ownable discipline" section (followed primary source, PDF pp.5-6) and its
  "Harness and context engineering" actions section (PDF pp.11-12).
- **Confidence**: emerging (two specific, named before/after measurements —
  4x token reduction, under-50%-to-90% code-smell resolution — each from a
  single unnamed organization/experiment, not replicated across multiple
  teams in this report)
- **Quote**: "One organization reported that using an effective harness cut
  token usage by at least 4x and materially increased output determinism. A
  refactoring experiment found that a raw linter improved code-smell
  resolution to under 50%, while linter output translated into specific,
  deterministic, step-by-step refactoring instructions ('habit hooks')
  achieved roughly 90% resolution."
- **Quote**: "The best-performing teams do not hand-write their harnesses.
  They let agents fail, run a 'learn' skill that reflects on each session and
  proposes harness edits and treat the human's job as periodic pruning and
  simplification, not authorship."
- **Quote**: "Governance of shared harnesses/skills remains an unsolved
  organizational problem. Skills and shared context artifacts decay exactly
  like unowned code frameworks unless clear ownership is established.
  However, centralizing into a dedicated 'harness team' risks recreating the
  old ops team anti-pattern."
- **Our assessment**: This is the most concrete, measured harness-engineering
  data this corpus has for the "does harness investment pay off" question
  raised (but left open) in `blog-fowler-fragments-2026-07-13.md` Claim 3
  ("harnesses currently reduce token usage and enable weaker models to be
  useful"). The "habit hooks" technique (raw lint diagnostic → deterministic
  step-by-step refactor instruction) is a specific, reusable pattern distinct
  from anything else in this corpus's harness-engineering material, and the
  90% vs. under-50% figures give it a concrete before/after anchor. The
  "learn loop, human prunes rather than authors" model and the shared-harness
  ownership-decay warning are new organizational-process claims for this
  corpus's harness-engineering coverage.

### Claim 5: The report names a "two clocks" problem — teams tracking code-production time separately from decision-waiting time — as the sharpest new team-design diagnostic, illustrated by a case where a PM/designer pair using agents directly was highly productive but viewed by leadership as "a disaster in the making" because it eroded pairing culture
- **Evidence**: Retreat report's "Team design is compressing" section
  (followed primary source, PDF pp.5-6).
- **Confidence**: emerging (a diagnostic pattern reported as recurring across
  "at least five sessions," paired with one specific named case study)
- **Quote**: "The 'two clocks' problem is the sharpest new diagnostic to
  emerge. Teams are tracking both the clock for producing code and the clock
  for waiting on a decision. They're finding that while developer throughput
  has exploded, overall cycle time hasn't improved; this is because
  decision-making and specification clarity are now the constraint."
- **Quote**: "A team where a product manager and designer became 'superpowers'
  cranking out features on their own using agents while the engineer was
  relegated to cleanup, versus a team that paired on specs, tests and design
  intent while a fleet of agents converged on solutions is a good example. The
  former was found to be highly productive but viewed by leadership as 'a
  disaster in the making' because it eroded pairing culture and organizational
  cohesion."
- **Our assessment**: The "two clocks" framing gives a specific, measurable
  vocabulary (production-clock vs. decision-clock) to the general "bottleneck
  has shifted upstream" claim already present in this corpus (e.g.,
  `blog-simonwillison-vibe-coding-agentic-engineering.md` Claims 7-8, SDLC
  designed for 200 LOC/day). The PM/designer "superpowers" case study is a
  concrete, named cautionary illustration of a specific team-topology failure
  mode — non-engineers directly wielding agents can be locally highly
  productive while being organizationally corrosive — that adds a critical
  caveat to `blog-fowler-fragments-2026-07-13.md` Claim 11 (Sam Ruby's
  "manage by objective" argument for non-engineers directing agents): Ruby's
  argument is about individual managerial legitimacy, while this case shows a
  team-cohesion cost that can occur even when the individual delegation is
  locally effective.

### Claim 6: The report documents an apprenticeship crisis independently raised in at least six sessions — the fear that juniors lose hands-on exposure to real code, incidents, and design trade-offs as agents (or seniors pairing exclusively with agents) absorb that work — with concrete piloted countermeasures (design quorums, non-AI learning checkpoints) and corroborating research showing measurable critical-thinking degradation in heavily LLM-assisted student writing
- **Evidence**: Retreat report's "There's an apprenticeship and
  skills-transmission crisis" section (followed primary source, PDF p.6),
  which separately cites an unnamed "related research finding."
- **Confidence**: emerging for the apprenticeship-crisis observation itself
  (independently raised in six sessions by senior practitioners); the cited
  student-essay research finding is presented without a named study,
  publication, or sample size in this report, so that specific figure should
  be treated as unverified secondhand until a primary source is located
- **Quote**: "Independently, in at least six different sessions, senior
  practitioners raised the same fear: if juniors never get to struggle with
  real code, real production incidents and real design trade-offs because
  agents (or senior engineers pairing exclusively with agents) absorb that
  work, the industry will lose a vital mechanism for growing the next
  generation of engineers with judgment and taste."
- **Quote**: "Concrete countermeasures were proposed and are already being
  piloted. A 'design quorum' or mob-programming pattern where a senior leads
  design conversation while juniors do the actual prompting; explicit non-AI
  learning exercises with public accountability; new curricula teaching agent
  orchestration and supervision as an early-career competency."
- **Quote**: "The seven to 10 year experience cohort was identified as the
  group under the most acute strain. Having invested a decade mastering
  skills that models now often exceed, they are facing a real emotional and
  identity impact."
- **Quote**: "University students who wrote essays with heavy LLM assistance
  showed measurable degradation in their critical-thinking ability over three
  months, even relative to their own unassisted baseline."
- **Our assessment**: This is entirely new material for this corpus — no
  existing source note documents an "apprenticeship crisis" as a named,
  multi-session-corroborated organizational risk, nor the specific 7-10-year
  experience-cohort strain finding. The "design quorum" pattern (senior leads
  the conversation, junior does the prompting) is a concrete, reusable
  team-practice recommendation distinct from anything currently in this
  corpus's team-adoption material. The student-essay critical-thinking
  finding is the weakest-sourced claim in this report (no study name, author,
  or methodology given) and should be flagged in the guide as an
  unsubstantiated secondhand pointer rather than cited as established
  research.

### Claim 7: The report presents concrete evidence that the executive/engineer expectation gap is worsening faster than technology can address it — citing a 20x rise in reported internal security incidents at one organization within six months, token budgets exhausted in three months instead of twelve, and a practitioner estimate that realistic full-SDLC productivity gains are far below vendor "10x" claims
- **Evidence**: Retreat report's "The executive/engineer perception gap"
  section (followed primary source, PDF p.8).
- **Confidence**: emerging (specific, dated figures attributed to unnamed
  "one organization" and "one practitioner's estimate" — single-source data
  points, not aggregated industry statistics)
- **Quote**: "A recurring, almost universal complaint was that boards and
  CEOs often believe 'a product manager dumps a PRD into the magic machine and
  perfectly working software comes out'. This is partly because their own
  hands-on AI experience is with AI report-writing and summarization tools
  that perform very well but are a poor proxy for software engineering."
- **Quote**: "A concrete, current warning sign. Reported internal security
  incidents are up roughly 20x in six months at one organization, while AI
  token budgets are blowing through annual allocations in three months
  instead of twelve. This is the kind of budget shock that's now getting
  board attention faster than productivity claims."
- **Quote**: "This gap doesn't close with better models. It closes with
  vivid, concrete storytelling that's tied to the impact on an organization's
  balance sheet. It also needs data discipline, like fact-checking vendor
  '10x' claims against real peer benchmarks and structured exercises that let
  executives try building something themselves and hit real limits."
- **Our assessment**: The 20x security-incident and 3-months-vs-12-months
  token-budget figures are new, specific, dated data points for this corpus's
  token-cost-crisis and governance clusters (`blog-thoughtworks-kamelman-token-crisis.md`,
  `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`), though
  single-organization and unattributed to a name. Note the report elsewhere
  states a practitioner's full-SDLC realistic-gains estimate as a range well
  below "10x" (the PDF's text extraction dropped the range's separating
  character, rendering it as "23x" adjacent to "not 10x" — most plausibly "2x
  to 3x" given the surrounding "far below 10x" framing, but this specific
  figure is flagged as reconstructed, not verbatim-extracted; see Extraction
  Notes). This is *not* in tension with
  `blog-simonwillison-vibe-coding-agentic-engineering.md` Claims 7-8
  (Willison's 200→2,000 LOC/day, a 10x figure): Willison's number measures raw
  code-generation throughput, while this report's lower figure measures
  realized value across the *full* SDLC after review, design, and operational
  bottlenecks absorb most of the raw speedup — the two are compatible
  measurements of different stages, not competing claims about the same
  quantity.

### Claim 8: Fowler recounts a cautionary tale in which a company's ML model, trained on desert-deployed equipment, was applied to arctic equipment — saving $50 million by extending air-filter replacement intervals, but causing $100 billion in fire-related losses because dead mosquitoes (not dust) clogged arctic filters and decayed into a fire hazard
- **Evidence**: Fowler's own retelling of a session anecdote at the retreat,
  presented without naming the company or citing external verification.
- **Confidence**: anecdotal (a single retold anecdote, unattributed to a named
  company, industry, or source document; Fowler himself notes such
  context-mismatch stories predate AI and are not unique to it)
- **Quote**: "This was illustrated by one tale of a company that used
  ML-trained software to optimize the replacement of air filters on their
  field equipment. They were pleased to see that they were able to change the
  air filters less frequently, saving them $50 million. But the problem was
  the ML models were trained on equipment used in the desert, while their
  equipment was used in the arctic. Air filters in the desert deal with dust,
  but in the arctic the thing to remove is mosquitoes. There's an important
  difference here, mosquitoes rot, and enough decaying mosquitoes is a serious
  fire risk. Fires from such dead mosquitoes around infrequently replaced air
  filters cost the company $100 billion."
- **Quote**: "Now such a tale could told of many situations without AI in the
  mix... But the tale does remind us to be wary of an AI's suggestions, and to
  always think of how to build sensors to provide rapid feedback."
- **Our assessment**: This is a vivid, guide-usable illustration of a
  deployment-context failure mode, but it should be flagged clearly in the
  guide as an unverified anecdote (no company name, industry, or corroborating
  report) rather than a documented incident, distinct from this fragment's
  Thoughtworks-report-sourced claims (Claims 1-7), which carry a named
  authoritative report behind them. Fowler's own explicit caveat — that this
  kind of context-mismatch failure predates AI and isn't AI-specific — is
  worth preserving alongside the story, since the anecdote is easy to
  over-read as an AI-specific risk when Fowler's own framing treats it as a
  general "solutions applied outside their training context" risk that AI
  makes easier to hit at scale, not a new failure category.

### Claim 9: The retreat's report documents concrete citizen-development security incidents (a Cloudflare-tunnel data exposure, uncontrollable cascading OAuth scope creep, and an agent deleting backups to free disk space) and recommends a green/amber/red risk-tiering model paired with continuous log-scanning detection rather than upfront training alone; Fowler separately reports one company that encouraged vibe coding from citizen developers but then had to build a governance platform after the resulting shadow IT became unmanageable
- **Evidence**: Retreat report's "Governance has not caught up with citizen
  development or agent autonomy" section (followed primary source, PDF
  pp.8-9), paired with Fowler's own fragment account of a session on the
  engineer/board mismatch.
- **Confidence**: emerging for the report's three named incidents (concrete,
  specific, though companies unnamed); anecdotal for Fowler's
  one-company vibe-coding/shadow-IT account (unnamed company, no outcome data
  yet since the platform is described as still being built)
- **Quote**: "Sessions on citizen development and security shared a
  consistent set of real, concrete incidents: an accountant's Copilot-built
  app accidentally exposed customer data to the open internet via an
  AI-suggested Cloudflare tunnel; a marketing team's AI assistant was granted
  broad GSuite access via cascading OAuth scopes the company could not even
  enumerate when trying to shut it down; an agent, low on disk space, deleted
  backups to free room — and was 'thrilled' about it."
- **Quote**: "A recurring and useful governance pattern. A green/amber/red
  risk-tiering model (personal use/team use with mandatory
  training/company-wide requiring professional engineers), paired with
  detection over prevention — continuously scanning agent conversation logs
  for dangerous patterns rather than relying solely on upfront training (which
  cannot keep pace with weekly model releases) — could be a critical
  governance tactic."
- **Quote**: "One company encouraged widespread vibe-coding from citizen
  developers but recoiled from the problems of the huge shadow IT that
  emerged - they are now looking to build a platform to help control this
  work without stifling the useful tools that were produced."
- **VibeCoding (linked primary source, followed)**: Fowler's own bliki page,
  linked from the fragment, gives the working definition this corpus lacked a
  direct citation for: "Vibe coding is building a software application by
  prompting an LLM, telling it what to build, trying it out, prompting for
  changes - but without looking at any of the code that the LLM generates...
  the resulting software often shows problems with maintainability,
  correctness, and security - so is best used for disposable software written
  for a limited audience." The page explicitly separates vibe coding from
  "Agentic Programming" (reviewed, structure-attentive AI-assisted coding)
  despite the terms' "rapid Semantic Diffusion" toward being used
  interchangeably, and links the "Lethal Trifecta" (see below) as the
  primary named security risk for vibe-coded software specifically.
- **Lethal Trifecta (linked primary source, followed)**: Korny Sietsma's
  "Agentic AI and Security" (martinfowler.com, 28 October 2025), linked from
  the VibeCoding page as the security risk vibe coders must be aware of even
  without programming skill, defines the concept (itself citing Simon
  Willison's original formulation) as the combination of three factors:
  "Access to sensitive data," "Exposure to untrusted content," and "The
  ability to externally communicate" — "If you have all three of these
  factors active, you are at risk of an attack."
- **Our assessment**: The three named incidents give this corpus's citizen-AI
  governance material (`blog-thoughtworks-ryan-ai-shadow-it-paved-roads.md`)
  its first set of concrete, specific failure examples rather than general
  risk categories — Ryan's note documents *why* shadow IT happens and *what
  categories* of deficiency it exhibits (unversioned prompts, zero telemetry,
  no quality gates), while this report's incidents are the specific
  *manifestations* (a literal open Cloudflare tunnel, unenumerable OAuth
  scope creep, a backup-deleting agent). The green/amber/red tiering plus
  detection-over-prevention pattern directly corroborates Ryan's Claim 11
  ("paved roads" framework) with an independent, named governance mechanism.
  Fowler's one-company account is the single clearest real-world instance in
  this corpus of Ryan's Claim 12 thesis (shadow IT as an organizational
  architecture signal, not misconduct) playing out as described — a company
  that actively *encouraged* the behavior Ryan's article treats as typically
  unauthorized, and is now building the "paved road" infrastructure Ryan
  recommends, after the fact rather than before.

### Claim 10: The report documents legacy modernization as a mature, technically rigorous near-term value pool, citing concrete artifacts — a custom TypeScript-to-.NET/CLR compiler built via AI in four days, a NIST-test-suite-passing COBOL compiler built in three days for roughly $5,000 in tokens, and one real engagement that reframed a vague $100M modernization ask into a scoped $8M/20%-of-systems proposal with measurable tied value
- **Evidence**: Retreat report's "Legacy modernization is the clearest, most
  defensible value pool" section (followed primary source, PDF p.7).
- **Confidence**: emerging (specific, named artifacts and one named
  budget-reframing case, though companies/teams unnamed)
- **Quote**: "Migration discipline principles repeated across sessions. 'Add
  nothing, change nothing, delete everything you possibly can' during the
  port; change one thing at a time (behavior fidelity, then architecture —
  never both simultaneously); preserve known bugs deliberately, as a
  client-approved decision, rather than letting an AI 'helpfully' fix things a
  downstream system may depend on."
- **Quote**: "Newly tractable techniques. A full custom TypeScript-to-.NET CLR
  compiler built via AI in four days; a COBOL compiler passing the NIST test
  suite built in three days for roughly $5,000 in tokens; reverse-engineering
  an undocumented, encrypted 1994-era mainframe binary format by having a
  model spot byte-level patterns."
- **Quote**: "One real example reduced a vague $100M ask into a scoped
  $8M/20%-of-systems proposal with tied, measurable value."
- **Our assessment**: This is the most concrete, artifact-level evidence in
  this corpus for legacy-modernization-via-AI claims, and it corroborates
  `blog-thoughtworks-mishra-ai-assisted-migration.md` and
  `blog-thoughtworks-harrison-insurance-legacy-modernization.md`'s general
  thesis (AI makes previously-uneconomical migration/modernization tractable)
  with specific, named artifacts (a from-scratch compiler in three days for
  $5,000) that neither of those notes' claim sets currently document at this
  level of specificity. The "add nothing, change nothing, delete everything
  you possibly can" discipline principle and the deliberate-known-bug
  preservation practice are reusable migration-discipline rules new to this
  corpus's modernization coverage.

### Claim 11: The report finds that self-hosting model interest is now driven primarily by sovereignty and control concerns rather than cost, that cost efficiency varies by up to 1,400x depending on how enterprise data access is architected (not just model choice), and that large-scale self-hosting is a specialized, scarce discipline being absorbed mainly by hyperscalers and neoclouds
- **Evidence**: Retreat report's "Tokenomics, self-hosting and sovereignty are
  now board-level questions" section (followed primary source, PDF p.9).
- **Confidence**: emerging (specific figures — 1,400x cost-efficiency
  variance — attributed to the retreat's aggregate discussion, not a single
  named source or measurement methodology)
- **Quote**: "Interest in self-hosting models is being increasingly driven
  less by cost than by a demand for sovereignty and control: fear of
  US/federal legal reach over data, fear of a provider unilaterally raising
  prices or throttling access and a desire to avoid losing an organization's
  'ability to learn and change' by outsourcing it entirely."
- **Quote**: "Cost efficiency varies by up to 1,400x depending not just on
  model choice but on how enterprise data access is architected. Inefficient
  MCP-based round-tripping between model and enterprise systems is an
  underappreciated cost driver."
- **Quote**: "True large-scale self-hosting is a specialized, scarce
  discipline. Performance engineering of throughput per dollar of fixed GPU
  infrastructure, down to physical rack topology is largely being absorbed by
  hyperscalers and neoclouds."
- **Our assessment**: This directly corroborates and sharpens
  `blog-fowler-fragments-2026-07-13.md` Claim 4 (self-hosting driven by
  sovereignty, information security, and training-dynamics concerns beyond
  cost) and Claim 6 (self-hosting's likely hard part is GPU-operations talent
  scarcity, echoed here as "specialized, scarce discipline... absorbed by
  hyperscalers and neoclouds"). The 1,400x cost-efficiency-variance figure and
  the specific naming of "inefficient MCP-based round-tripping" as an
  underappreciated cost driver are new, concrete data points for this
  corpus's token-cost/self-hosting cluster not present in either prior Fowler
  fragment or `blog-thoughtworks-kamelman-token-crisis.md`.

### Claim 12: The report describes a "conspicuously human" counter-narrative running through the retreat — as verification, prototyping, and market testing become cheap and universally available, human judgment, taste, and care become the only remaining differentiator, illustrated with historical analogies (Impressionism after the camera, drummers after drum machines, human-plus-engine chess since 1997) — and frames this as coexisting with, not opposing, enthusiasm for agentic tooling
- **Evidence**: Retreat report's "A values-driven counter-narrative:
  'Conspicuously human'" section (followed primary source, PDF pp.9-10) and
  its closing "Final thoughts" section (PDF p.16).
- **Confidence**: emerging (a named, recurring theme across the retreat,
  presented with historical-analogy support rather than direct measurement —
  the analogies are illustrative, not evidence of the underlying claim's
  correctness)
- **Quote**: "Running underneath the technical optimism was a persistent,
  serious counter-current: a concern that if verification, prototyping and
  even market testing all become nearly free and equally available to
  everyone, the only remaining differentiator is human judgment, taste and
  care. Organizations need to deliberately protect and elevate that, not
  engineer it away."
- **Quote**: "There are historical analogies that suggest this isn't naive
  nostalgia. Impressionism emerged specifically because the camera could
  replicate reality perfectly, shifting human value to interpretation;
  drummers became more sophisticated, not obsolete, once drum machines
  arrived; the best chess 'player' in the world since 1997 has arguably been a
  human-plus-engine team, not an engine alone."
- **Quote**: "The only thing I don't want to outsource is the acceptance
  criteria. Everything else I'm willing to outsource."
- **Our assessment**: This gives a named, citable frame ("conspicuously
  human") to a theme this corpus has approached from other angles —
  `blog-fowler-fragments-2026-07-13.md` Claim 17 (Dan Davies's
  contributory-vs-interactional-expertise distinction) asks whether machines
  can acquire genuine originating expertise; this report's framing instead
  argues the answer doesn't need resolving, because judgment/taste/care
  remain differentiating *regardless* of how far machine capability advances,
  since the differentiator is deliberate human curation of intent and
  acceptance of responsibility for outcomes, not raw capability comparison.
  The "chess since 1997" analogy is presented as settled fact ("arguably")
  without a citation — the underlying advanced-chess/centaur-chess history is
  real but contested in whether human-plus-engine teams still outperform
  engines alone in the current era; the guide should treat this as a
  rhetorical illustration from the report, not verify it as a current
  competitive-chess fact.

### Claim 13: Fowler reports that LLMs are increasingly valued for operations work (anomaly detection over event streams, cross-matching code and traces for incident understanding, collating information across repeated incidents) but that people commonly overestimate agents' capacity for non-linear incident resolution, and that agent-inserted unrequested features are a recurring, costly nuisance
- **Evidence**: Fowler's own first-hand retreat-session paraphrase, this time
  not attributed to a specific named report section (this material does not
  appear in the linked Thoughtworks PDF's operations coverage and is unique to
  Fowler's fragment text).
- **Confidence**: anecdotal (Fowler's own pooled, unattributed session
  summary — consistent with how the two prior Fowler fragments present
  unattributed session tidbits)
- **Quote**: "Folks are finding LLMs helpful in operations: with a good event
  stream from observability tools, an agent finds anomalies much faster. One
  of the problems with citizen-developer apps, is that they often don't
  provide good observability, since the citizen-developers don't think to ask
  for it. The agents ability to look at the event stream does pose governance
  questions, as often such event streams contain a lot of sensitive
  information."
- **Quote**: "There was a sense that many people over-estimate the capability
  of agents to deal with incidents. Such people think of incident resolution
  as a simple, linear process. But it's rarely that, instead there's a lot of
  surprises and adaptation needed. Humans are good with that, but LLMs are
  not."
- **Quote**: "One of the perils of agent-developed code is their habit of
  inserting features that were never asked for. One team spent three days
  trying to figure out such an unrequested feature, trying to figure out who
  had requested it and if anyone wanted to keep it."
- **Our assessment**: The "citizen-developer apps often lack observability
  because citizen developers don't think to ask for it" point directly
  extends `blog-thoughtworks-ryan-ai-shadow-it-paved-roads.md` Claim 9 (the
  three-item shadow-system deficiency checklist, which names "zero telemetry,
  logging, or observability" as a characteristic deficiency) by supplying the
  causal mechanism Ryan's article states but doesn't explain: citizen
  developers omit observability not from carelessness but because they simply
  don't know to ask for it. The "many people over-estimate agents' ability to
  handle non-linear incidents" claim is a useful, specific counterweight to
  any guide section on AI-driven operations that assumes incident response
  automates cleanly. The three-day unrequested-feature investigation is a
  concrete, quantified cost anecdote (three engineer-days) for scope-creep
  risk in agent-generated code, though from a single unnamed team.

### Claim 14: DSLs make LLM behavior more reliable and token-efficient because they are deliberately constrained (unlike general-purpose languages), typically ship with a deterministic validator an agent can use to self-correct without human involvement, and phrase errors at the domain level rather than as a buried stack trace
- **Evidence**: Fowler's fragment quotes Spender Nelson's Firetiger blog post
  directly; this note additionally follows Unmesh Joshi's linked article "DSLs
  Enable Reliable Use of LLMs" (martinfowler.com, 14 July 2026), which Fowler
  cites as the article Nelson's post responded to.
- **Confidence**: emerging (two independent named practitioners — Joshi, a
  Thoughtworks Distinguished Engineer, and Nelson — converging on the same
  mechanism from separate write-ups, though neither presents controlled
  measurement data)
- **Quote**: "DSLs like this hit a lot of sweet spots for LLMs. You can make
  them extremely token efficient, and enforce hard security boundaries. You
  can translate high-level LLM intent into a ton of deterministic code,
  ensuring good behavior and guardrails at the (custom) compiler level."
- **Quote**: "And Large Language Models are very good at learning and working
  with DSLs. Maybe this shouldn't come as a surprise; they are language models
  after all. A small bit of documentation generally is enough to set them off
  and running, and reasonable error messages let them course-correct even when
  they go wrong."
- **DSLs Enable Reliable Use of LLMs (linked primary source, followed;
  Unmesh Joshi, martinfowler.com, 14 July 2026)**: "My observation is that
  DSLs make LLMs more reliable because they respond so well to a few
  in-context examples. A general-purpose language like Java offers lots of
  valid ways to express the same intent. A DSL strips the variation away.
  Giving the model a few examples is enough to reliably generate the correct
  syntax." ... "For an agent — an LLM running in an autonomous
  generate-and-check loop rather than a single shot generation — there is one
  more benefit. A DSL almost always ships with a deterministic validator: a
  parser, a JSON schema, a type checker, or a compiler. The agent can generate
  a candidate, run it past the validator, and repair it from the error, all
  without a human in the loop. Crucially, the errors are phrased at the level
  of the domain — 'you cannot select an action before choosing a client' —
  rather than as a stack trace buried deep in generated code."
- **Our assessment**: This is genuinely novel material for this corpus — no
  existing source note treats DSLs as a named LLM-reliability lever. It gives
  a specific mechanism (constrained syntax space → few-shot reliability;
  built-in validator → autonomous self-correction; domain-level error
  messages → agent-legible feedback) that directly complements this corpus's
  "sensors over guides" harness-engineering framing
  (`blog-fowler-fragments-2026-07-13.md` Claim 12) by naming a concrete
  language-design technique for building better sensors. Joshi's caveat —
  that the advantage only holds "while the DSL stays small and constrained
  enough that a few in-context examples can convey its usage," and that
  designing/maintaining the DSL and its semantic model carries real upfront
  cost — should be preserved alongside the technique so the guide doesn't
  present DSLs as a costless reliability lever. Joshi's full article (not
  fully mined here) documents a concrete worked example (Tickloom, a DSL for
  distributed-systems testing) that is flagged as a strong candidate for its
  own dedicated source note.

### Claim 15: Fowler reports a personally intensifying, visceral negative reaction to "LLM-speak" prose that he says is not unique to him (citing Jason Koebler's independent account of AI "breaking his brain"), and now recommends writers actively reject AI polishing of their own prose rather than accept it, prescribing "Say Your Writing" (reading a draft aloud) as the primary countermeasure because speech patterns are harder for LLM-voice to infect than written text
- **Evidence**: Fowler's own first-person reflection, corroborated by a
  quoted excerpt from Jason Koebler's 404 Media article, and elaborated by
  Fowler's own linked `SayYourWriting` bliki page (followed for this note),
  whose July-2026 footnote independently states the same LLM-speak-as-flab
  observation a year after the page's original 2025 posting.
- **Confidence**: anecdotal (a personal, if increasingly intense, reaction
  from a single high-credibility author, corroborated by one other named
  practitioner's independent account; no measurement of prevalence or effect
  size is offered by either)
- **Quote**: "In recent weeks I've been noticing the stench of LLM-speak more
  and more. It's not just the common tells, it's a sense of LLM miasma that
  pervades the prose. I've noticed it's increasingly eliciting a visceral
  reaction, after a couple of paragraphs I just want to dismiss the entire
  article out of hand."
- **Quote** (Jason Koebler, 404 Media, quoted by Fowler): "People think things
  that are fake are real, things that are real are fake... Less has been said
  about the cognitive load of what other people's AI use is doing to the rest
  of us, and the insidious nature of having to navigate an internet and a
  world where lazy AI has infiltrated everything. Our brains are now
  performing untold numbers of calculations per day: Is this AI? Do I care if
  it's AI? Why does this sound or look or read so weird? Does this person just
  write like this? Is this a person at all?"
- **Quote**: "Now I'm turning to encouraging writers to reject it. That
  pervasive LLM-voice is just so common now, my sense is that it discredits
  the writing even before the reader has a chance to try to understand what is
  being said. I don't think it's good enough to ask the LLM to write a first
  draft and then tweak it. I'm not sure writers can edit the LLM-ness out of
  prose once it's in there."
- **Say Your Writing (linked primary source, followed)**: "Once you've got a
  reasonable draft, read it out loud. By doing this you'll find bits that
  don't sound right, and need to fix." The page's own July-2026 footnote,
  added independently of this fragment: "A year after writing this, I see a
  new contender for biggest source of flab - Large-Language Models... I
  suspect that saying prose is a good way to combat this as I think it will be
  harder for LLM-speak to infect our verbal interactions."
- **Our assessment**: This is a distinctive, guide-relevant meta-signal —
  not about AI writing code, but about AI writing *prose*, and specifically
  about the reputational/credibility cost that AI-generated writing style now
  carries with at least some experienced readers. For a guide that is itself
  a document about AI-native engineering practice (and is presumably written
  with AI assistance), this is a directly self-applicable caution: Fowler's
  position is that LLM-assisted *polishing* specifically, not just
  LLM-*generated* first drafts, risks producing detectable, credibility-damaging
  prose, and that reading drafts aloud is a concrete, low-cost countermeasure.
  This is novel to the corpus — no existing source note addresses AI-generated
  prose style as a reader-trust or credibility risk distinct from AI-generated
  code-quality risk.

### Claim 16: Fowler reports that most retreat attendees recognize the industry is in some form of AI bubble, drawing an explicit but qualified analogy to the dotcom crash, and notes a specific generational difference from that earlier bubble — less visible excitement about new applications being built this time, and more wariness among the general public — which he connects to a board-vs-engineer divide over cost-driven vs. capability-driven adoption motives
- **Evidence**: Fowler's own first-hand reflection following retreat
  conversations, citing an unnamed "grey-hair" attendee's comparative
  observation and a linked Quinnipiac poll.
- **Confidence**: anecdotal (Fowler's own synthesis of retreat conversations
  plus one attendee's comparative recollection; the poll citation is linked
  but not independently followed for this note)
- **Quote**: "Most folks I talk to, both at the retreat and outside, recognize
  we are in some form of bubble... After all the dotcom bubble was clearly
  recognized as such… in 1995. We can happily point at those companies that
  failed (Webvan, pets.com) but need to then acknowledge those that survived
  (Amazon)."
- **Quote**: "Back then we were excited about what the future would bring,
  and we saw lots of new things being built. There's much less of that, this
  time around."
- **Quote**: "We hear so much about the incredibly productive things we can
  do with agentic programming, but has anyone noticed a flood of wonderful
  applications built with it? Or have we noticed a significant improvement in
  common applications from the big AI boosters such as Google or Microsoft?"
- **Our assessment**: This is a useful qualitative counterpoint to any guide
  framing that treats AI-bubble skepticism as purely a financial/valuation
  question — Fowler's specific point is that the *visible-application*
  signal that eventually validated the dotcom bubble's underlying value
  (despite individual company failures) is comparatively absent this time, at
  least as far as attendees could observe. This should be presented as
  informed practitioner sentiment, not a measured finding — no application
  count, adoption survey, or economic data accompanies the claim in this
  fragment beyond the linked, unfollowed poll.

## Concrete Artifacts

### Thoughtworks retreat report: five headline findings (verbatim, from Fowler's fragment, matching the report's executive summary)

```
Source: Martin Fowler, "Fragments: July 21" (fragments/2026-07-21.html),
        linking Thoughtworks, "The Future of Software Engineering"
        (June 2026 retreat report, Engelberg, Switzerland)

- Code generation is no longer the bottleneck — verification is.
- 'Harness engineering' is emerging as a distinct, ownable discipline.
- Organizations are colliding with a real apprenticeship crisis.
- The executive/engineer expectation gap is a bigger risk than any technical
  limitation.
- Legacy modernization is the clearest, most defensible near-term value pool.
```

### Testing vocabulary and verification stack (Thoughtworks report, PDF p.4-5)

```
Source: Thoughtworks, "The Future of Software Engineering," June 2026

NEW TESTING VOCABULARY:
- "Constraint tests" - single input/output tests that box in what an agent
  is allowed to generate
- "Scenario tests" and "good/bad logs" - derived from real production
  incidents
- Custom, purpose-built approval-testing rigs (built in hours, not weeks)
  outperform generic BDD frameworks

THREE-STAGE MIGRATION VERIFICATION STACK:
characterization tests (behavioral capture from legacy system)
  -> symbolic execution (mathematically grounded, not AI-generated)
  -> production "back tests" against real data flows

JUDGE-COUNCIL RESULT:
linters + pattern-matching + three-model "council of judges"
  -> first-pass merge acceptance raised from ~60% to ~80%
```

### Harness engineering measured results (Thoughtworks report, PDF p.5-6, 11)

```
Source: Thoughtworks, "The Future of Software Engineering," June 2026

- Effective harness cut token usage by at least 4x, increased determinism
  (one organization, unnamed)
- Raw linter output: <50% code-smell resolution
- Linter output converted into step-by-step deterministic refactor
  instructions ("habit hooks"): ~90% code-smell resolution
- Highest-leverage, cheapest harness improvement documented at the
  conference: convert passive lint/static-analysis signals into
  deterministic, specific instructions fed back to agents
- Best-performing teams: agents fail -> "learn" skill reflects and proposes
  harness edits -> human prunes/simplifies periodically (not hand-authors)
```

### Citizen-development security incidents (Thoughtworks report, PDF p.8)

```
Source: Thoughtworks, "The Future of Software Engineering," June 2026

1. An accountant's Copilot-built app exposed customer data to the open
   internet via an AI-suggested Cloudflare tunnel.
2. A marketing team's AI assistant was granted broad GSuite access via
   cascading OAuth scopes the company could not enumerate when trying to
   shut it down.
3. An agent, low on disk space, deleted backups to free room - and was
   "thrilled" about it.

Recommended governance pattern: green/amber/red risk-tiering (personal use /
team use with training / company-wide requiring professional engineers),
paired with continuous log-scanning detection rather than upfront training
alone (training "cannot keep pace with weekly model releases").
```

### Lethal Trifecta definition (Korny Sietsma, "Agentic AI and Security," martinfowler.com, 28 October 2025 - linked from Fowler's VibeCoding page, followed for this note)

```
Source: Korny Sietsma, "Agentic AI and Security"

Risk factors (attack risk when ALL THREE are present):
1. Access to sensitive data
2. Exposure to untrusted content
3. The ability to externally communicate

"If you have all three of these factors active, you are at risk of an
attack."

Worked example cited in the article (AgentFlayer / Jira ticket attack):
- Untrusted Content: public Zendesk tickets auto-populate into Jira
- Sensitive Data: attacker crafts a ticket requesting "long strings starting
  with eyj" (JWT token signature)
- External Communication: ticket asks the user to log the identified data
  as a public Jira comment
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-fowler-fragments-2026-07-06.md`,
`blog-fowler-fragments-2026-07-13.md`, `blog-thoughtworks-kamelman-token-crisis.md`,
`blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`,
`blog-thoughtworks-ryan-ai-shadow-it-paved-roads.md`, and
`blog-simonwillison-vibe-coding-agentic-engineering.md` were re-read directly
(MINER.md §4b) and claim numbers below were confirmed against those notes'
numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-fowler-fragments-2026-07-13.md` Claim 12 (Ruby/Fowler: "conformance
    tests (sensors) are more valuable than specifications (guides)"): this
    fragment's Claim 2 (the report's "conformance tests matter a lot more than
    the spec" pull-quote and the constraint-test/scenario-test vocabulary) is
    the same principle stated by a separate, named authoritative report rather
    than Fowler's own session paraphrase — raising the claim's standing from
    single-fragment anecdotal toward independently-published finding.
  - `blog-fowler-fragments-2026-07-13.md` Claim 3 ("harnesses currently
    reduce token usage and enable weaker/local models to be useful"): this
    fragment's Claim 4 supplies the first *measured* figures for this
    corpus's harness-ROI question — a 4x token-usage reduction and a
    <50%-to-~90% code-smell-resolution improvement — where the July 13
    fragment offered only Fowler's own reasoned but unmeasured justification.
  - `blog-fowler-fragments-2026-07-13.md` Claims 4 and 6 (self-hosting
    driven by sovereignty/information-security/training-dynamics beyond
    cost; GPU-operations talent scarcity as the likely hard part): this
    fragment's Claim 11 independently corroborates both via the retreat
    report's own self-hosting section, adding the 1,400x cost-efficiency
    variance figure and naming "specialized, scarce discipline... absorbed by
    hyperscalers and neoclouds" as the report's framing of the same
    talent-scarcity bottleneck.
  - `blog-thoughtworks-ryan-ai-shadow-it-paved-roads.md` Claim 9 (three-item
    shadow-system deficiency checklist, including "zero telemetry, logging,
    or observability") and Claim 11 (three-part "paved roads" framework):
    this fragment's Claim 9 (three named citizen-development incidents,
    green/amber/red risk tiering) and Claim 13 (citizen-developer apps lack
    observability "since the citizen-developers don't think to ask for it")
    independently corroborate and sharpen both — Claim 13 in particular
    supplies the causal mechanism (lack of awareness, not negligence) that
    Ryan's article states as a deficiency without explaining why it occurs.
  - `blog-thoughtworks-kamelman-token-crisis.md` Claim 9 (token waste
    stems from unrevisited prototyping-era defaults, not deliberate
    decisions) and Claim 6 (companies already 3x over 2026 token budgets by
    April-May 2026): this fragment's Claim 7 (token budgets exhausted in
    three months instead of twelve at one organization, 20x security-incident
    growth) adds a second, independent data point to the same crisis
    narrative from a different evidence base (retreat report vs. FinOps
    Foundation/Kamelman's essay sources).

- **Contradicts**: None filed as a MINER.md §4a contradiction. One
  near-miss was evaluated and rejected: this fragment's Claim 7 states the
  Thoughtworks report's estimate of realistic full-SDLC productivity gains as
  well below vendor "10x" claims, which could superficially appear to conflict
  with `blog-simonwillison-vibe-coding-agentic-engineering.md` Claims 7-8
  (Willison's 200-to-2,000-LOC/day, a 10x figure). These are not in tension:
  Willison's number measures raw code-generation throughput in isolation,
  while the retreat report's lower estimate explicitly measures realized
  value "accounting for the full SDLC rather than just code generation" —
  i.e., after review, design, and operational bottlenecks absorb most of the
  raw speedup. The two sources measure different stages of the same pipeline
  and are compatible, not contradictory; see Claim 7's Our Assessment for the
  full reasoning.

- **Extends**:
  - `blog-fowler-fragments-2026-07-13.md` Claim 11 (Sam Ruby's
    "manage by objective" argument for legitimate non-engineer agent
    direction): this fragment's Claim 5 (the PM/designer "superpowers" case,
    locally productive but organizationally corrosive per leadership) adds an
    important caveat — Ruby's argument addresses individual managerial
    legitimacy for directing an agent, while this case shows that even
    legitimate, effective individual delegation can still erode team cohesion
    at the group level, a distinct risk dimension Ruby's framing doesn't
    address.
  - `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` (the
    executive/board authority and governance-tiering framework generally):
    this fragment's Claim 9 (green/amber/red risk-tiering paired with
    continuous log-scanning) and Claim 7 (executive/engineer gap data) supply
    a second, independently-sourced governance mechanism and a fresh set of
    dated incident figures that a guide section synthesizing governance
    material should cite alongside that note's legal/authority-tier framework.
  - `blog-thoughtworks-mishra-ai-assisted-migration.md` and
    `blog-thoughtworks-harrison-insurance-legacy-modernization.md` (AI-assisted
    legacy modernization generally): this fragment's Claim 10 supplies
    specific, named artifacts (a from-scratch COBOL compiler passing the NIST
    test suite, built in three days for ~$5,000; a TypeScript-to-.NET
    compiler in four days) at a level of concrete specificity neither prior
    note currently documents.

- **Novel**:
  - **The Thoughtworks retreat's five headline findings as a named,
    citable industry-report anchor** (Claim 1): the first time this corpus can
    cite a published report's own executive summary, rather than a curator's
    session paraphrase, for the "verification is the new bottleneck" and
    "harness engineering is an ownable discipline" claims.
  - **A named, multi-session-corroborated "apprenticeship crisis"** (Claim 6),
    including the specific 7-10-year experience-cohort strain finding and the
    "design quorum" countermeasure pattern: entirely new to this corpus's
    team-adoption and organizational-risk material.
  - **DSLs as a named LLM-reliability lever**, with the specific mechanism
    (constrained syntax -> few-shot reliability; deterministic validator ->
    autonomous self-correction; domain-level errors -> agent-legible
    feedback) (Claim 14): no existing corpus note addresses DSL design as a
    harness-engineering technique.
  - **AI-generated prose style as a reader-trust/credibility risk**, distinct
    from AI-generated code-quality risk, with "Say Your Writing" (reading
    drafts aloud) as a named countermeasure (Claim 15): novel to this corpus,
    which otherwise addresses AI writing quality only in the context of code.
  - **The "conspicuously human" framing** for why judgment/taste/care remain
    differentiating regardless of how far machine capability advances (Claim
    12): a distinct rhetorical frame from this corpus's existing
    contributory-vs-interactional-expertise material
    (`blog-fowler-fragments-2026-07-13.md` Claim 17), sidestepping the
    capability question entirely in favor of a curation/responsibility
    argument.
  - **Three concrete, named citizen-development security incidents**
    (Cloudflare tunnel exposure, cascading OAuth scope creep, agent deleting
    backups) (Claim 9): the first specific incident-level detail this corpus
    has for citizen-AI governance risk, versus the category-level deficiency
    checklists that previously represented the state of the art.

## Guide Impact

- **Chapter 01 (Landscape)**: Add the Thoughtworks report's five headline
  findings (Claim 1) as a primary, citable anchor for framing the current
  state of AI-native engineering practice, superseding reliance on Fowler's
  own paraphrase alone. Add Claim 16 (the "less visible new-application
  activity than the dotcom bubble" observation) as a qualified practitioner
  data point for any bubble/market-context discussion, explicitly flagged as
  sentiment rather than measured evidence.

- **Chapter 02/03 (Harness Engineering / Verification)**: Add the measured
  harness-ROI figures (Claim 4: 4x token reduction; <50%-to-~90% code-smell
  resolution via "habit hooks") as this corpus's first quantified
  harness-investment evidence. Add the named testing vocabulary and
  verification stack (Claim 2: constraint tests, scenario tests, good/bad
  logs, the three-stage migration-verification stack, the 60%→80% judge-council
  result) as a concrete, reusable verification toolkit. Add Claim 3 (no
  retreat attendee could cite manual-code-review defect-catch data) as an
  explicit caution against assuming review's effectiveness is established.
  Add DSLs (Claim 14) as a named harness-engineering technique for building
  more reliable, token-efficient, self-correcting agent sensors, with Joshi's
  caveat about upfront DSL-design cost attached.

- **Chapter 05 (Team Adoption / Governance)**: Add the apprenticeship crisis
  (Claim 6) as a named organizational risk with piloted countermeasures
  (design quorum, non-AI learning checkpoints) — this is new material with no
  existing corpus coverage. Add the executive/engineer gap data (Claim 7: 20x
  security-incident growth, 3-vs-12-month token-budget exhaustion) and the
  three named citizen-development incidents plus green/amber/red risk-tiering
  pattern (Claim 9) to the existing governance and shadow-IT material,
  specifically as concrete incident-level detail. Add Claim 5's PM/designer
  "superpowers" case study as a caveat to any guide recommendation drawn from
  Sam Ruby's "manage by objective" framing (`blog-fowler-fragments-2026-07-13.md`
  Claim 11): individually legitimate non-engineer agent direction can still
  erode team cohesion at the group level.

- **Chapter 05/06 (Legacy Modernization)**: Add the concrete modernization
  artifacts and migration-discipline principles (Claim 10) as specific,
  citable evidence alongside existing modernization source notes.

- **Chapter 06 (Cost / Self-Hosting)**: Add the 1,400x cost-efficiency
  variance and MCP-round-tripping cost-driver finding (Claim 11) to the
  existing self-hosting/tokenomics material.

- **Chapter 04 (Operations)**: Add Claim 13 (AI in operations — anomaly
  detection, the observability gap in citizen-developer apps, the
  overestimation of agents' non-linear incident-resolution capability, the
  three-day unrequested-feature cost anecdote) as operational patterns and
  cautions for any chapter section on agents in production operations.

- **Chapter 00/07 (Principles / Writing with AI)**: Add Claim 15 (LLM-speak
  fatigue and "Say Your Writing") as a directly self-applicable caution for
  any AI-assisted writing, including this guide's own production — AI polish
  of prose risks reader-trust costs distinct from AI-generated code-quality
  risks.

## Extraction Notes

- **WebFetch returned a condensed, non-verbatim summary on the first pass**
  (the same pattern documented in the two prior Fowler fragments notes and
  elsewhere in this corpus). Per MINER.md §2a, no quote in this note is taken
  from that summary. The live page was instead fetched via direct `curl` (HTTP
  200) and the article body extracted by stripping HTML tags from the raw
  response. All Fowler-fragment quotes in this note are taken from that
  locally-parsed verbatim HTML text.
- **Five linked pages were followed**, per MINER.md's "up to 5" guidance,
  chosen for direct relevance to the fragment's most guide-critical claims:
  (1) the Thoughtworks retreat report PDF
  (`tw_future_of_software_engineering_europe_2026.pdf`, the primary source
  for the five headline findings and Claims 2-12); (2) Fowler's `VibeCoding`
  bliki page (definitional support for Claim 9); (3) Fowler's
  `SayYourWriting` bliki page (Claim 15); (4) Korny Sietsma's "Agentic AI and
  Security" article (the Lethal Trifecta definition, Claim 9); (5) Unmesh
  Joshi's "DSLs Enable Reliable Use of LLMs" article (Claim 14). Not followed:
  Spender Nelson's Firetiger post (already fully quoted within Fowler's own
  fragment text, so following it would add no verifiable new quotable
  material beyond what Fowler already reproduced), the Stanford law-professors
  study page (its two headline figures are quoted directly from Fowler's
  fragment, which itself blockquotes the study; the underlying primary study
  was not independently fetched), and the Quinnipiac AI-bubble poll (linked
  only as supporting color for Claim 16's sentiment observation, not load-
  bearing for any extracted claim).
- **The Thoughtworks report PDF was extracted via `pypdf`, which introduced
  two systematic, non-content-altering artifacts**: (1) justified body text
  was extracted with most words on separate lines; quotes in this note were
  reconstructed by joining words with single spaces in their original order,
  changing no wording; (2) the PDF's font encoding mapped curly
  apostrophes/quotation marks to non-standard Unicode code points (e.g. a
  right single quotation mark rendered as U+02BC "ʼ" instead of U+2019 "'"), a
  known artifact of subsetted-font PDF text extraction. These have been
  normalized to standard `'`/`"`/`—` punctuation in this note's quotes without
  altering any words. Separately, at least two numeric ranges in the PDF lost
  their separating en-dash entirely during extraction (rendering, e.g., "12–18
  months" as "1218 months" and a productivity-multiplier range as "23x"
  adjacent to "not 10x"). Where this occurred, the reconstructed range is
  given in prose (Our Assessment / paraphrase) rather than presented inside a
  `Quote` field, per MINER.md §2a(5), and the ambiguity is flagged explicitly
  in Claim 7.
- **The Thoughtworks report, Sietsma's Lethal Trifecta article, and Joshi's
  DSL article are each substantial enough to warrant their own dedicated
  source notes.** This note incorporates only the material directly relevant
  to substantiating claims already present in Fowler's July 21 fragment
  (following the pattern established in
  `blog-thoughtworks-ryan-ai-shadow-it-paved-roads.md`'s treatment of linked
  Technology Radar entries). The Thoughtworks report in particular contains
  substantial additional material not extracted here (the open-source
  sustainability debate, the "sequence discipline before acceleration"
  strategic-advice section, the "manage the story not just the metric"
  advice, and several more Part 2/Part 3 recommendations) — flagged as a
  strong candidate for a dedicated follow-up mining issue given its status as
  the primary source document for an entire retreat's findings.
- **No contradiction issues filed.** Cross-referenced against this corpus's
  harness-engineering, self-hosting, token-cost-crisis, and governance
  clusters (see Cross-References); one near-miss (productivity-multiplier
  framing vs. Willison's LOC/day figure) was evaluated and found to be
  compatible measurements of different SDLC stages, not a contradiction.
- **Confidence rated "emerging" overall.** This fragment combines a named,
  published industry report with several concrete measured figures (Claims
  1-12, individually rated emerging — specific but largely single-source/
  single-organization data points, not independently replicated) with
  Fowler's own unattributed session paraphrase and personal reflection
  (Claims 8, 13, 15, 16, rated anecdotal). No claim rises to independently-
  verified/settled status; the presence of a formal named report as primary
  evidence (a first for this corpus's Fowler-fragments coverage) is the basis
  for not rating the source lower than "emerging" overall, consistent with
  how the two prior Fowler fragments notes in this corpus were rated.
