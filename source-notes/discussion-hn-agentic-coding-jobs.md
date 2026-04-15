---
source_url: https://news.ycombinator.com/item?id=47303745
source_type: discussion
title: "Ask HN: Are we going to see more job postings asking for only agentic coding?"
author: ronbenton (OP); substantive comments by jackyli02, hackermailman, mattmanser, raw_anon_1111, bediger4000, daringrain32781, codingdave
date_published: 2026-03-09
date_extracted: 2026-04-14
last_checked: 2026-04-14
status: current
confidence_overall: anecdotal
issue: "#43"
---

# Ask HN: Are we going to see more job postings asking for only agentic coding?

> A 11-comment HN discussion thread (March 2026, score: 6) anchored by a
> verbatim Zapier job posting that explicitly frames "directing and reviewing
> agent-written code" as the core workflow — notable not for its engagement
> but for three specific signals: (1) the first documented job-market language
> explicitly deprioritizing hand-written code, (2) a practitioner's concrete
> pre-generation formal-methods workflow that enables "never look at the code"
> generation, and (3) a clarifying exchange showing that LLM reliability in
> API-heavy domains correlates with training-data coverage, not with domain
> type.

## Source Context

- **Type**: discussion (Ask HN, 6 points, 11 comments, 2026-03-09; some
  comments deleted or dead at time of extraction, 8 live comment IDs retrieved)
- **Author credibility**: ronbenton is anonymous on HN. The thread draws
  several named practitioners: hackermailman (describes a detailed formal-
  methods workflow, verifiable named tools — Forge, Alloy, essenceofsoftware.com,
  61040-fa25.github.io); jackyli02 (product-domain observations, no stated
  affiliation); mattmanser (API-domain practitioner, consistent across two
  sub-threads); raw_anon_1111 (AWS SDK practitioner, links to public Boto3
  docs). Low score (6) and small comment count mean the thread has not been
  crowd-validated. Treat all claims as anecdotal from individual practitioners.
- **Scope**: The thread is a reaction to a single job posting (Zapier,
  March 2026). It covers: the cultural shift in employer framing of agentic
  workflows; practitioner skepticism about reliability and token cost; domain-
  dependency of agentic coding success; one practitioner's detailed pre-
  generation design methodology. It does NOT cover: team-level adoption
  strategies, quantitative productivity data, harness configuration, or cost
  metrics. The signal-to-noise ratio is modest — approximately 4 of the 8 live
  comments are substantive; the others are one-liners.

## Concrete Artifacts

### The Zapier Job Posting (verbatim from OP's post)

```
"You work through AI agents, not alongside them. Your daily development
workflow is built around directing and reviewing agent-written code, not
writing it by hand. You have opinions about which models to use for which
tasks, you've hit real failure modes and built mitigations, and your workflow
is actively evolving. Bonus: you use multi-agent patterns, enable others on
your team to build faster with AI, or have scaled AI impact beyond yourself."
```

*Source: ronbenton (OP), https://news.ycombinator.com/item?id=47303745,
2026-03-09*

### hackermailman's Pre-Generation Workflow

```
Pre-generation design pipeline (hackermailman, comment #47323082):

1. User-facing parts:
   - Apply conceptual design (https://essenceofsoftware.com/) to plan modularity
   - Model "concepts" vs. "features" before generating (MIT 6.1040 framing)
   - Example: HN has an "upvoting concept" (purpose: rank) and a separate
     "karma concept" (purpose: downvote access) — conflating them breaks
     modularity; conceptual design makes this visible before coding

2. Hidden/backend parts:
   - Model using lightweight formal methods: Forge or Alloy
     (https://forge-fm.github.io/book/2026/)
   - Uses: security role models (multi-login permission systems), network
     protocols, game rules (no "winner" state unless actually won),
     CSS layout states (prevent broken rendering)
   - Purpose: test for illicit/unexpected states BEFORE generating code

3. Generation:
   - "Now generate the whole system as modules and never look at the code"
   - The property tests from the Forge model become an Oracle
   - Blast agent-generated code with random inputs against the Oracle

Reported output: "I built several gigantic prototypes this way mostly of
papers I read in database designs and screwing around with graphical
interfaces for them."
```

*Source: hackermailman, comment #47323082 (reply to bediger4000),
https://news.ycombinator.com/item?id=47323082, 2026-03-09 (late)*

### LLM Reliability / Training Coverage Exchange

```
mattmanser (comment #47316821, reply to jackyli02):
  "I work in an API heavy domain. Ironically, you need it to be right and
  LLMs don't cut it."

raw_anon_1111 (comment #47318554, reply to mattmanser):
  "My API heavy domain is coding against the AWS SDK. [...] I've been testing
  writing code and shell scripts against the AWS SDK since 3.5. It helped
  then, I can mostly one shot it now as long as the APIs were available when
  it was trained. Now I just have to tell it to 'search for the latest
  documentation' if its a newer API."

mattmanser (comment #47355782, reply to raw_anon_1111):
  "There's a ton of examples of AWS in GitHub isn't there. You couldn't have
  picked a better API for an AI to one shot from the literally millions of
  examples it has. I mean mapping one crazy API with tons of quirks from one
  non-software company to another non-software company that's often behind a
  username/password or some other barrier."
```

*Source: mattmanser (#47316821, #47355782), raw_anon_1111 (#47318554),
March 2026*

## Extracted Claims

### Claim 1: A major employer (Zapier) is now explicitly requiring agentic-only coding as a job expectation, not just AI-assistance

- **Evidence**: Verbatim job posting quoted by OP. Zapier is a well-known
  workflow automation company (API/integration domain). The posting explicitly
  names multi-agent patterns, model selection opinions, and real failure modes
  as expectations — not bonuses. The "bonus" tier describes team impact
  and scaling, implying the agentic workflow is baseline.
- **Confidence**: anecdotal (single data point, single company, single posting)
- **Quote**: "You work through AI agents, not alongside them. Your daily
  development workflow is built around directing and reviewing agent-written
  code, not writing it by hand."
- **Our assessment**: This is the most concise formulation of "agentic-first"
  as a hiring requirement found in our corpus. The distinction drawn is clean:
  not "uses AI," not "uses AI alongside coding," but specifically that hand-
  written code is not the primary output. The Pragmatic Engineer survey
  (survey-pragmaticengineer-ai-tooling-2026) shows 70% of engineers use 2–4
  AI tools simultaneously, but does not show employers *requiring* agentic
  workflows as a baseline competency. This posting is a leading indicator
  that the market is beginning to price in that requirement. Note that Zapier's
  domain (API integration, glue code) is the most favorable for agentic coding
  reliability — a Zapier-style posting from a systems-software company would
  carry different weight.

### Claim 2: The framing of hand-written code as a suboptimal workflow represents a notable industry shift as of early March 2026

- **Evidence**: jackyli02's practitioner observation, noting this is new in a
  ~6-month window.
- **Confidence**: anecdotal (one observer's assessment)
- **Quote**: "This is explicitly framing hand-written code as the wrong
  workflow. That's a significant shift from even six months ago."
- **Our assessment**: The 6-month timeline is plausible. Claude Code launched
  May 2025; this thread is March 2026 — 10 months later. The Pragmatic
  Engineer survey (Jan–Feb 2026) shows adoption surging but frames AI as
  "alongside" developer work, not "instead of." The Zapier posting is one step
  further: it treats the "alongside" mode as insufficient. Whether this
  generalizes beyond Zapier's specific domain is the key open question.

### Claim 3: Agentic coding adoption is domain-dependent — API/integration ("glue") code is a more natural fit than systems-level work

- **Evidence**: jackyli02's practitioner observation + Zapier's specific
  company profile (workflow automation = API-heavy glue code).
- **Confidence**: anecdotal
- **Quote**: "My sense is this will become more common at companies building
  on top of APIs and integrations (Zapier's core domain), where the code is
  more glue than architecture. Whether it scales to systems-level work is a
  different question."
- **Our assessment**: This is a reasonable conditioning variable. Agentic
  code generation is most reliable when the output has clear acceptance
  criteria, many training examples exist, and the state space is bounded
  (CRUD operations, API calls, data transforms). Systems-level work (kernel
  code, networking stacks, concurrent data structures, security-critical paths)
  has fewer training examples and failure modes that are harder to specify as
  tests. The domain-dependency claim is underspecified here — "systems-level"
  is broad — but the underlying logic is sound. Connect to Claim 4 (training
  data coverage) for a more precise formulation.

### Claim 4: LLM reliability in "API-heavy" domains is not a property of the domain category but of training-data coverage for specific APIs

- **Evidence**: The three-comment exchange between mattmanser and raw_anon_1111.
  mattmanser's initial claim ("I work in an API heavy domain... LLMs don't cut
  it") is rebutted by raw_anon_1111's AWS SDK success, which mattmanser then
  acknowledges is explained by the "literally millions of examples" on GitHub.
  The actual failure domain mattmanser points to is "one crazy API with tons
  of quirks from one non-software company to another non-software company
  that's often behind a username/password or some other barrier."
- **Confidence**: anecdotal (two practitioners, one exchange)
- **Quote (mattmanser)**: "There's a ton of examples of AWS in GitHub isn't
  there. You couldn't have picked a better API for an AI to one shot from the
  literally millions of examples it has."
- **Quote (raw_anon_1111)**: "I can mostly one shot it now as long as the
  APIs were available when it was trained. Now I just have to tell it to
  'search for the latest documentation' if its a newer API."
- **Our assessment**: This exchange produces a more precise model than
  "agentic coding struggles with APIs." The correct framing is: agentic coding
  struggles with *obscure APIs* that have limited training examples, especially
  those behind authentication barriers (which prevent crawling) or belonging
  to non-tech companies (fewer GitHub repos documenting their quirks). Well-
  documented, widely-used APIs (AWS, Stripe, OpenAI) are reliable targets.
  Enterprise integration scenarios (SAP, Workday, legacy internal APIs) are
  not. This has direct implications for the guide: when assessing whether a
  domain is "agent-ready," the question is not "is it API-based" but "does
  the API have good training coverage?"

### Claim 5: Pre-generation formal design (conceptual design + lightweight formal methods) enables reliable "never look at the code" agent generation

- **Evidence**: hackermailman's detailed workflow description, naming specific
  tools (Forge, Alloy, essenceofsoftware.com, MIT 6.1040 course). Claims to
  have built "several gigantic prototypes" of database design papers using
  this approach. The tools are real and publicly available (Forge book linked
  as forge-fm.github.io/book/2026/; essenceofsoftware.com is a published book
  by an MIT professor, Daniel Jackson).
- **Confidence**: anecdotal (one practitioner, self-reported, no code shared)
- **Quote**: "Once everything is planned out this way then generating code is
  trivial again in my limited experience as I'm no expert on agentic coding
  but I've had success doing this."
- **Our assessment**: The most substantive and novel technical claim in the
  thread. The workflow has three distinct layers: (1) conceptual design for
  modularity planning before generation; (2) formal model (Forge/Alloy) for
  state-space verification before generation; (3) property tests from the
  formal model as test oracles after generation. This is not a casual
  practitioner tip — it is a pre-generation design methodology with named,
  independently verifiable tools and academic grounding (MIT course). The
  "limited experience" caveat and lack of shared code keep this anecdotal, but
  the underlying logic is sound: the more formally you specify the system
  before generation, the more precisely you can verify the output. Compare
  to blog-osmani-good-spec's recommendation for detailed specs before agent
  invocation — hackermailman's approach is the formal-methods extreme of that
  spectrum.

### Claim 6: Property tests derived from formal models (Forge/Alloy) serve as oracles for validating agent-generated code at scale

- **Evidence**: hackermailman's stated methodology. Formal model property tests
  are expressed in Forge/Alloy's constraint language; the claim is that these
  same properties can be translated into runtime tests against agent-generated
  code, then applied via random input blasting (property-based testing).
- **Confidence**: anecdotal
- **Quote**: "The same property tests I used for the Forge model I make into
  an Oracle and then blast the agent code with random inputs."
- **Our assessment**: This is a concrete implementation of the
  "spec-as-verification" principle. The Forge model defines what the system
  *should* be; the Oracle tests check whether the agent's code *is* that
  system under arbitrary inputs. This is one of the few mechanisms in our
  corpus that provides systematic rather than sample-based validation of
  agent-generated code. The practical challenge is that translating Forge
  properties into runtime tests requires expertise in both the formal tool
  and the runtime environment. This is a high-skill ceiling approach — not
  general-purpose, but potentially valuable for the "complex system" segment
  where jackyli02 says agentic coding "is a different question."

### Claim 7: Formal methods (Forge/Alloy) apply to non-traditional domains — CSS layout, game rules, security role models — not just protocol verification

- **Evidence**: hackermailman's enumerated use cases: "I now use Forge to plan
  css too because I don't want to show broken css states since I have limited
  design experience." Also: game winner conditions, multi-login security
  models, custom network protocols.
- **Confidence**: anecdotal
- **Quote**: "I now use Forge to plan css too because I don't want to show
  broken css states since I have limited design experience."
- **Our assessment**: The CSS example is the most surprising. Forge is
  typically applied to distributed protocols and security models; using it to
  enumerate CSS state combinations is a novel application. The underlying
  logic is the same (prevent illegal state combinations) but the domain is
  unexpected. This suggests the pre-generation formal modeling approach has
  broader applicability than its academic framing implies. Worth one sentence
  in the guide as an illustration of the technique's scope.

### Claim 8: Failure modes of agent-written code are poorly understood as of early 2026, and "built mitigations" is doing significant work in agentic job descriptions

- **Evidence**: jackyli02's practitioner observation about the Zapier posting.
- **Confidence**: anecdotal (one observer's assessment)
- **Quote**: "The failure modes of agent-written code are still poorly
  understood, and 'built mitigations' is doing a lot of heavy lifting in that
  job listing."
- **Our assessment**: This is a sharp observation. The Zapier posting requires
  applicants to have "hit real failure modes and built mitigations," implying
  that the employer recognizes failure modes are real and understands that
  documented mitigation experience is rare. The "heavily loading" critique is
  valid — this phrasing presupposes that the applicant has already failed in
  ways that aren't yet widely documented and has built solutions that aren't
  yet widely known. It selects for a very small population of practitioners.
  This aligns with the paper-miller-speed-cost-quality finding (complexity
  increase, static analysis warning increase) but from the employer demand
  side rather than the research measurement side.

### Claim 9: For some tasks, direct coding is faster than prompting an agent — an implicit "just do it yourself" threshold exists

- **Evidence**: daringrain32781's practitioner complaint, framed as a time
  comparison.
- **Confidence**: anecdotal (one practitioner assertion)
- **Quote**: "sometimes it's just faster to do the damn thing yourself instead
  of writing a whole paragraph to an agent that still might do it wrong."
- **Our assessment**: This is probably true for small, well-defined, repetitive
  tasks where the engineer can execute in seconds (e.g., a one-line
  regex, a simple type annotation, a known variable rename). The threshold is
  real but unquantified here. French-Owen's note (blog-french-owen-coding-
  agents-feb-2026) indirectly addresses this by recommending agents for
  "bigger problems" — the corollary is that small problems may not be worth
  the overhead of prompting. The guide should acknowledge this threshold
  explicitly rather than implying agents are optimal for all task sizes.

### Claim 10: The aggregate productivity return from agentic coding may be marginal for practitioners who have not rebuilt their workflow around it — "a little more speed alongside a little more slop"

- **Evidence**: codingdave's assessment of their own experience, framing the
  returns as modest and the cost as real (token spend).
- **Confidence**: anecdotal (one practitioner)
- **Quote**: "Our output has not changed, except maybe a little more speed
  alongside a little more slop. People who do get it to work do so by throwing
  a lot of money at tokens. Is that all we are doing? Funding the AI platform
  vendors and stressing ourselves over... a minor speed improvement?"
- **Our assessment**: This matches the skeptical reading of the Miller et al.
  speed-cost-quality paper: raw throughput increases alongside quality
  degradation. codingdave's framing ("minor speed improvement") and Miller's
  findings (41% complexity increase, 30% static-analysis-warning increase) can
  coexist — the engineer perceives modest speed improvement and experiences
  increased slop burden (review, rework, debugging). This is the strongest
  skeptical claim in the thread and should be represented in the guide rather
  than dismissed. The Pragmatic Engineer survey shows high adoption and
  enthusiasm among senior engineers; codingdave's experience may reflect the
  reality for practitioners who have not restructured their workflow to match
  the agentic model (write specs first, review systematically, use harness
  patterns). The thesis of the guide is that the "slop" is addressable via
  workflow — but that claim needs to be defended, not assumed.

## Cross-References

- **Corroborates**: `survey-pragmaticengineer-ai-tooling-2026` — the Pragmatic
  Engineer survey captures team-adoption landscape (70% use 2–4 AI tools; 95%
  weekly usage). This thread adds a job-market-requirement angle the survey
  does not cover: companies beginning to *require* agentic workflow competency,
  not just reward it. The Zapier posting is the first documented instance in
  our corpus of hand-written code being framed as the wrong default.

- **Corroborates**: `research-anthropic-ai-transforming-work` — the Anthropic
  report captures company-level AI transformation. The Zapier posting extends
  this to hiring requirements: not just "our engineers use AI" but "we hire
  engineers who already work through agents."

- **Corroborates**: `paper-miller-speed-cost-quality` — codingdave's "a little
  more speed alongside a little more slop" is the practitioner-stated version
  of Miller et al.'s measured finding (41% complexity increase, 30% static-
  analysis-warning increase alongside throughput gains). Two independent data
  points (one measured, one self-reported) pointing to the same pattern.

- **Extends**: `blog-french-owen-coding-agents-feb-2026` — French-Owen
  describes practitioner tactics for Claude Code and Codex (context budget,
  Skills vs. MCP, sub-agent delegation). hackermailman's formal-methods
  approach is a distinct *upstream* design pattern: it runs before any agent
  invocation, not during session management. French-Owen's advice applies
  inside the agentic session; hackermailman's advice applies before the session
  starts. Both are complementary; the guide should stage them accordingly.

- **Extends**: `blog-osmani-good-spec` — Osmani argues for detailed specs
  before agent invocation. hackermailman's Forge/conceptual-design workflow
  is the formal-methods extreme of this principle: the spec is not just a
  written document but a mathematically verifiable model. hackermailman's
  approach provides the property-test Oracle that Osmani's spec approach
  lacks.

- **Novel**:
  - **Formal-methods-as-pre-generation-design**: No other source in our corpus
    describes using Forge/Alloy or conceptual design (essenceofsoftware.com) as
    a pre-agent step. This is a distinct methodology not documented elsewhere.
  - **Property-tests-from-formal-models-as-agent-output-oracle**: The specific
    pattern of using Forge property tests as Oracle tests for random input
    blasting of agent code is not documented in any other source.
  - **Training-coverage as the precise predictor of API-domain LLM reliability**:
    Prior corpus framing was "API-heavy domains may struggle." The mattmanser/
    raw_anon_1111 exchange narrows this to: obscure, under-documented, or
    auth-gated APIs struggle; well-documented, widely-used APIs (AWS, etc.)
    do not. This is a more precise and actionable distinction.
  - **First job-posting-level requirement for agentic coding competency**: The
    Zapier posting is the earliest documented job-market artifact in our corpus
    that explicitly treats hand-written-code-first as insufficient.

- **Contradicts**: None filed. The thread's skeptical claims (Claim 9, 10)
  are not contradictions with existing notes — they are consistent with
  Miller et al.'s quality findings and the Anthropic report's 0–20% full-
  delegation ceiling. They add practitioner voice to existing empirical data.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: The Zapier posting should be the lead
  example in any section on "what agentic-first workflow looks like as a
  baseline expectation." It is the most compact, quotable formulation of the
  "directing agents" model as a professional competency rather than a power-
  user technique. Quote it verbatim; it is more compelling than any paraphrase.

- **Chapter 01 (Daily Workflows)**: Add the "just do it yourself" threshold
  (Claim 9) as a calibration principle: agents are not uniformly faster for
  all task sizes. The guide should explicitly scope when to invoke agents and
  when to execute directly. This prevents the "agentic-for-everything"
  misapplication that Claim 10 reflects.

- **Chapter 02 (Harness Engineering / Specification)**: Add a section on
  pre-generation design methodology, citing hackermailman's workflow as the
  formal-methods instantiation and blog-osmani-good-spec as the lightweight
  instantiation of the same principle (specify before generating). The key
  spectrum: informal written spec → structured written spec → formal model
  (Forge/Alloy). Use case determines placement: prototype/CRUD leans toward
  informal; complex-protocol/security-critical leans toward formal.

- **Chapter 02 or Chapter 03 (Verification)**: Add property-tests-as-oracle
  (Claim 6) as a verification strategy. This is the only mechanism in our
  corpus that provides systematic rather than sample-based coverage of agent-
  generated code for complex state-dependent logic. Frame it as high-skill-
  ceiling but high-value for domains where correctness is load-bearing.

- **Chapter 03 (Safety and Verification / Domain Fitness Assessment)**: Add
  training-coverage as the specific predictor of LLM reliability for API
  integration (Claim 4). Revise any language that frames "API-heavy" as a
  blanket risk: the real risk factor is API obscurity and documentation depth,
  not the API-integration pattern itself. Practical heuristic: search GitHub
  for examples of the specific API you need — low count → higher verification
  burden needed.

- **Chapter 05 (Team Adoption)**: Use the Zapier posting as a forward signal:
  this is the earliest documented job-market artifact requiring agentic
  workflow as a baseline competency. Teams should treat this as a leading
  indicator of how engineering roles will be described within 12–18 months.
  A team-adoption strategy that prepares engineers for the "directing agents"
  competency profile is building toward the market, not running behind it.

- **Chapter 05 (Team Adoption / Honest Assessment of Returns)**: The codingdave
  claim (Claim 10) must appear in any "honest objections" section. The guide's
  thesis (workflow and harness address the slop) should be stated as a claim
  that needs defense, not as a given. The "minor speed improvement + more slop"
  experience is the expected result for engineers who have not adopted the
  spec-first, harness-structured, verification-checkpointed approach. Present
  the two paths clearly: unstructured agentic use → Claim 10 result; structured
  harness-based use → the guide's approach.

## Extraction Notes

- The thread was extracted via the Hacker News Firebase API
  (hacker-news.firebaseio.com/v0/item/), which returns raw JSON for each
  comment ID. All 8 top-level comment IDs and all reachable replies were
  fetched individually. The result: 4 substantive comments, 1 one-liner, 1
  cynical prediction, 2 deleted comments, 1 dead comment. The effective content
  is in 4–5 comments.
- hackermailman's comment (#47323082) is the highest-value artifact. It was
  posted considerably later than the other top-level replies (time: 1773149810
  vs. the thread's 1773019638 open), suggesting it was written more carefully.
  The named tools (Forge, Alloy, essenceofsoftware.com, MIT 6.1040 course) are
  all publicly verifiable and independently substantive. The methodology is
  novel enough to warrant a contradiction check — none found.
- The mattmanser/raw_anon_1111 exchange (#47316821 → #47318554 → #47355782)
  is the second highest-value artifact. The three-turn exchange resolves an
  apparent contradiction (API domains are bad vs. AWS works fine) into a more
  precise claim (training coverage is the predictor). This resolution is more
  analytically useful than either position alone.
- Low engagement (6 points) means the thread has not been crowd-validated.
  The Zapier posting is a real artifact and the technical claims reference real
  tools, but the practitioner claims are from anonymous individuals. Confidence
  is anecdotal throughout.
- The Prospector correctly noted the scanner's `failure-report` label was
  inaccurate; this is a discussion thread. No failure-report extraction was
  performed.
