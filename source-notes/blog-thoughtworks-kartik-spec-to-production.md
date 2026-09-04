---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/from-specification-to-production-building-enterprise-software-with-agentic-ai
source_type: blog-post
title: "From specification to production: Building enterprise software with agentic AI"
author: SG Kartik
date_published: 2026-09-03
date_extracted: 2026-09-04
last_checked: 2026-09-04
status: current
confidence_overall: anecdotal
issue: "#3229"
---

# From Specification to Production: Building Enterprise Software with Agentic AI

> Thoughtworks practitioner account of a single, unnamed enterprise platform
> — "tens of thousands of lines of code across hundreds of source files,"
> zero human-written — built end-to-end from conversational natural-language
> specifications by an agentic AI, in an estimated four weeks versus a
> traditional ~96-week estimate, illustrating five recurring agent behaviors
> and arguing the engineer's role shifts from writing code to reviewing,
> directing, and diagnosing it.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, "Generative AI" blog category;
  published September 3, 2026; discovered via the trusted `thoughtworks` RSS
  feed). A first-person practitioner narrative structured around one
  extended case description (no named client, industry, or platform type
  given) followed by a generalized argument about specification quality and
  the engineer's changing role.
- **Author credibility**: SG Kartik, byline-only (no title, role, or "about
  the author" text surfaced on the fetched page beyond the linked Thoughtworks
  profile page). No prior source note in this corpus is authored by Kartik —
  this is a first appearance. The account is presented as the author's own
  first-person experience ("I've watched," implied throughout via the
  framing of what "the agent" did), not as a controlled study, a named client
  engagement, or independently reviewed outcome data.
- **Scope**: Covers one described build (a "production-grade, cloud-native
  enterprise platform with multiple backend microservices, a web frontend, a
  full test suite and a complete cloud infrastructure deployment pipeline"),
  the nature of the natural-language requirements given to the agent, a
  seven-step operational loop the agent followed, five recurring behavioral
  patterns the author observed, prompting advice (describe intent, not
  implementation), and a closing argument about specification quality and the
  engineer's shifting role. Does NOT cover: the platform's industry, company,
  or name; team size; specific testing frameworks, coverage figures, or code
  review process; security audit or penetration-testing steps before
  production; rollback/incident procedures; post-deployment monitoring
  practice; or any metric beyond the two headline figures (LOC/file count,
  weeks estimate).

## Extracted Claims

### Claim 1: A complete, production-grade enterprise platform — multiple backend microservices, a web frontend, a full test suite, and a cloud infrastructure deployment pipeline — was built entirely from natural-language specifications, with zero lines of code written by a human developer
- **Evidence**: Author's direct first-person account of a single, unnamed build; no client name, industry, or independently verifiable artifact (repo, screenshot, commit log) is given in the article.
- **Confidence**: anecdotal (single, unnamed, self-reported case; the "zero lines written by a human developer" and "tens of thousands of lines... hundreds of source files" figures cannot be independently checked from the article text)
- **Quote**: "Tens of thousands of lines of code across hundreds of source files. Zero lines written by a human developer."
- **Quote** (the build described): "A production-grade, cloud-native enterprise platform with multiple backend microservices, a web frontend, a full test suite and a complete cloud infrastructure deployment pipeline, was built entirely from natural language specifications."
- **Our assessment**: This is the article's headline claim and its evidentiary weight rests entirely on the author's own word — no named organization, no linked repository, no third-party confirmation. Treat as a vivid anecdote illustrating what agentic development *can* look like under favorable conditions, not as a benchmark result. The claim is also silent on pre-production steps (security review, sign-off, testing rigor) that other Thoughtworks sources in this corpus treat as necessary gates — see Cross-References → Contradicts.

### Claim 2: The project was estimated to take around 96 weeks under a traditional delivery approach but was completed in four weeks using agentic AI, though the author explicitly cautions this reflects one specific project rather than a universal productivity benchmark
- **Evidence**: Author's own estimate comparison, with an explicit hedge against generalizing it.
- **Confidence**: anecdotal (a self-reported estimate-vs-actual comparison for one unnamed project; the 96-week baseline is itself an estimate, not a measured traditional-delivery timeline for the same scope)
- **Quote**: "A project of this scope was estimated to take around 96 weeks using a traditional delivery approach. With agentic AI, it was completed in four weeks."
- **Quote** (the caveat): "While that comparison reflects this specific project rather than a universal productivity benchmark, it illustrates how significantly agentic development can compress implementation timelines."
- **Our assessment**: The author's own hedge is worth preserving in any guide citation — this is presented as an illustrative data point, not a claimed universal multiplier. It is the strongest headline number in the piece and will likely be the one most readers remember, so the guide should carry the caveat alongside the number if cited.

### Claim 3: Requirements were delivered as conversational natural language — the way a stakeholder would talk to a colleague — spanning functional, operational, infrastructure, and debugging categories, without formal specification documents or technical jargon
- **Evidence**: Author's description of the specification process, illustrated with two example requirement statements (one functional, one a debugging/symptom report).
- **Confidence**: anecdotal (illustrative examples from the same single, unnamed project; no data on how many requirements were given this way or how often clarification was needed)
- **Quote** (functional example): "A user should be able to complete a key transaction without needing to log in just using their account reference."
- **Quote** (debugging/symptom example): "The transaction is completing on the frontend but the status isn't reflecting the change."
- **Our assessment**: The debugging example is notable for being a *symptom report*, not a diagnosis — the stakeholder describes what they observed, not what they believe is wrong, which sets up the "autonomous debugging" behavior (Claim 5) as the agent's own responsibility to trace, not the human's.

### Claim 4: The agent followed a repeatable seven-step operational loop for each requirement — read the existing codebase for context, design an implementation, write coordinated code across multiple files, execute and observe results, diagnose failures and apply fixes, and deliver working software — with each iteration completing in minutes rather than days
- **Evidence**: Author's description of the agent's repeated workflow across the engagement.
- **Confidence**: anecdotal (a described pattern from one project, not independently measured or timed)
- **Quote**: "in minutes, not days"
- **Our assessment**: This compressed cycle-time framing is the article's clearest quantitative-feeling (if unmeasured) claim about *iteration speed specifically*, distinct from the overall project-timeline claim in Claim 2 — it describes the loop within a single requirement, not the whole project.

### Claim 5: Five behaviors recurred across the engagement: reading existing code before writing (to match naming conventions and architecture), making the smallest targeted fix rather than refactoring, holding cross-file dependencies in context to change every affected file in the correct order, autonomously diagnosing runtime failures by tracing logs and call stacks without asking a human to diagnose first, and applying security controls (e.g., password hashing with industry-standard algorithms and appropriate cost factors) without being explicitly asked
- **Evidence**: Author's five named behavioral observations, each with a one-to-two sentence description.
- **Confidence**: anecdotal (behavioral pattern observed by one author on one unnamed project; no frequency, failure-rate, or comparison-condition data given for any of the five)
- **Quote** (read before write): "Before making any change, the agent read the relevant files to understand the existing patterns, naming conventions and architecture."
- **Quote** (minimal targeted changes): "The agent did not refactor existing code when asked to fix a bug. It identified the precise location of the problem and made the smallest change that would resolve it."
- **Quote** (cross-file coherence): "The agent held all of these in context simultaneously. When implementing a feature, it identified every file that needed to change, made all the changes in the correct order and verified that the system worked end-to-end."
- **Quote** (autonomous debugging): "When code failed at runtime, the agent did not ask the human to diagnose the problem. It read the log output, traced the error back through the call stack, identified the root cause."
- **Quote** (security by default): "Security controls were applied without being requested. Every generated system had: Password hashing using industry-standard algorithms with appropriate cost factors."
- **Our assessment**: The first four behaviors (read-before-write, minimal diffs, cross-file coherence, autonomous debugging) are consistent, unremarkable descriptions of competent agentic coding practice already well-attested elsewhere in this corpus. The fifth — security controls applied "without being requested" — is the claim this Miner flags most strongly: it directly opposes `blog-thoughtworks-harmellaw-nfr-guardrail.md` Claim 1's thesis that LLMs do not infer non-functional requirements (including security posture) unless explicitly prompted. See Cross-References → Contradicts and filed contradiction issue #3240.

### Claim 6: Effective prompting for agentic development means describing intent rather than implementation — stating the desired outcome, not the mechanism to achieve it (e.g., "see status without refreshing" rather than "add a polling mechanism"), and applying the same principle to debugging by describing symptoms rather than assumed fixes
- **Evidence**: Author's direct prescriptive advice, illustrated with one paired example.
- **Confidence**: anecdotal (a prescriptive recommendation drawn from the same single engagement, not tested against a comparison condition)
- **Quote**: "Describe intent, not implementation. State what you want to achieve, not how to achieve it."
- **Quote** (the paired example): "'A user should be able to see their current status without refreshing the page' rather than 'Add a polling mechanism to this component.'"
- **Our assessment**: This is the article's most directly actionable, quotable piece of prompting guidance — a concrete before/after pair a reader could apply immediately. It is consistent with, and gives a specific worked example for, the general "specify what, not how" instinct already present in this corpus's harness-engineering material.

### Claim 7: As implementation speed increases under agentic AI, specification quality becomes the binding bottleneck — vague requirements produce vague software, and precise requirements produce precise software — which places new demands on product managers, business analysts, and domain experts
- **Evidence**: Author's direct generalizing argument, stated as the article's central takeaway for organizations.
- **Confidence**: anecdotal (a generalized thesis drawn from one project's experience, not measured against a comparison of vague- vs. precise-specification outcomes)
- **Quote**: "As implementation gets faster, specification quality becomes an increasingly important bottleneck. The clearer and more precise the intent, the better the output. Vague requirements produce vague software. Precise requirements produce precise software."
- **Our assessment**: This is a compact, quotable framing of a "bottleneck shifts upstream" argument. It corroborates `blog-thoughtworks-aliyeva-werner-lammel-path-to-production.md` Claim 8 (technology is rarely the primary blocker; the harder problem is organizational/process) and `blog-thoughtworks-harmellaw-nfr-guardrail.md`'s overall thesis that what gets specified up front is what the agent will deliver — though notably, this article frames the risk purely in terms of *functional* vagueness (what the feature should do), while Harmel-Law's piece specifically names *non-functional* requirements (security, reliability, compliance) as the category most likely to be silently skipped absent explicit specification — a gap this article's own security-by-default claim (Claim 5) elides.

### Claim 8: Engineers working alongside agentic AI are not replaced but "elevated" — their value shifts to reviewing generated code for correctness and security, identifying architectural problems before they propagate, diagnosing complex failures, and making judgment calls on trade-offs the agent cannot evaluate; an engineer who can direct an agent precisely, review its output critically, and course-correct effectively is far more productive than one writing every line manually
- **Evidence**: Author's direct argument under a "The role of the engineer is shifting" section heading.
- **Confidence**: anecdotal (a normative/predictive claim about the profession, not measured against comparative productivity data)
- **Quote**: "Engineers who work alongside agentic AI are not replaced, they are elevated. Their value now lies in reviewing generated code for correctness and security, identifying architectural problems before they propagate, diagnosing complex failures and making judgment calls on trade-offs the agent cannot evaluate."
- **Quote** (the productivity claim): "The engineer who can direct an agentic AI precisely, review its output critically and course-correct effectively is vastly more productive than one who writes every line manually."
- **Our assessment**: This closely corroborates `blog-thoughtworks-gall-supervisory-engineering.md` Claim 2 ("In the middle loop, the human engineer evaluates whether the agent actually solved the right problem") and Claim 9 ("evaluating" requires deep system context to judge whether plausible-looking code actually handles real-world conditions) — two independent Thoughtworks trusted-feed authors, writing about six months apart, converge on the same "review/direct, not write" reframing of engineering value. Neither source offers productivity data; both are asserted from practitioner experience.

### Claim 9: The human's role in this engagement was limited to providing the specification and validating that the output matched intent — the agent cannot originate business decisions, apply real credentials, or judge whether a feature "genuinely solve[s] the problem," and organizational governance questions remain open, including how quality and governance practices evolve "when the author of most code is an AI"
- **Evidence**: Author's stated boundary on what the agent could and could not do, plus a closing open question about organizational governance.
- **Confidence**: anecdotal (asserted limitation and an unresolved rhetorical question, not elaborated with a governance mechanism or process in this article)
- **Quote** (the human's role): "providing the specification and validating that the output matched the intent"
- **Quote** (the limitation, partial): "genuinely solve the problem"
- **Quote** (the open governance question): "How do quality and governance practices evolve when the author of most code is an AI?"
- **Our assessment**: This article poses the governance question without answering it — no designated-accountable-human requirement, no oversight tiering, no audit-logging or escalation mechanism is described anywhere in the piece, despite the platform reaching what the author calls "production." This is a significant, guide-relevant gap: `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 5 (three-tier oversight, a named "designated principal") and `blog-thoughtworks-aliyeva-werner-lammel-path-to-production.md` Claim 5 (a four-gate model requiring penetration testing, bias/safety validation, and CISO sign-off before production) both describe exactly the kind of governance/security-gating machinery this article's four-week, zero-human-code build does not mention having passed through. This article motivates the same open question those two pieces attempt to answer, but does not itself engage with their proposed answers.

### Claim 10: The article is silent on verification mechanics beyond "run the code and observe the output" and validating output against intent — no testing framework, coverage target, code review process, security audit, or rollback procedure is named for how the described platform was actually cleared for production
- **Evidence**: Absence, noted across the full article — checked specifically for testing, review, and production-readiness process content and found none beyond the general behaviors in Claim 5 and the human-validates-intent framing in Claim 9.
- **Confidence**: anecdotal (a structural gap the Miner identified by close reading against MINER.md §1's "read the entire source" requirement, not a claim the author makes)
- **Quote**: (no direct quote; see Extraction Notes for the extraction passes that specifically searched for and did not find this content)
- **Our assessment**: This is the single largest gap between this article's framing (a full production-grade platform, "not a claim about a prototype or a weekend toy project") and what the article actually documents about how "production-grade" was verified. Readers of the guide should not infer that the described four-week timeline included the kind of gated verification (penetration testing, CISO sign-off, staged rollout, monitoring) that `blog-thoughtworks-aliyeva-werner-lammel-path-to-production.md`'s four-gate model treats as a precondition for calling something production-ready — the article simply does not describe those steps happening, one way or the other.

## Concrete Artifacts

```
Source: SG Kartik, "From specification to production: Building enterprise
software with agentic AI," Thoughtworks Insights, published September 3, 2026.

Headline figures:
  - "Tens of thousands of lines of code across hundreds of source files."
  - "Zero lines written by a human developer."
  - Traditional estimate: ~96 weeks. Agentic-AI actual: 4 weeks.
    (Author's own caveat: "reflects this specific project rather than a
    universal productivity benchmark.")

Seven-step operational loop (per requirement, as described):
  1. Stakeholder provides a natural-language requirement
  2. Agent reads the existing codebase for context
  3. Agent designs an implementation
  4. Agent writes coordinated code across multiple files
  5. Agent executes the code and observes results
  6. Agent diagnoses failures and applies fixes
  7. Agent delivers working software
  (Each iteration described as completing "in minutes, not days.")

Five recurring agent behaviors (named by the author):
  1. Read before write — reads relevant files for patterns/conventions/
     architecture before changing anything
  2. Minimal, targeted changes — smallest fix that resolves the problem,
     no opportunistic refactoring
  3. Cross-file coherence — holds all affected files in context, changes
     them in the correct order, verifies end-to-end
  4. Autonomous debugging — traces log output and call stacks to root
     cause without asking the human to diagnose first
  5. Security by default — e.g., password hashing with industry-standard
     algorithms and appropriate cost factors, applied without being
     requested

Two example requirement statements (verbatim):
  - Functional: "A user should be able to complete a key transaction
    without needing to log in just using their account reference."
  - Debugging/symptom: "The transaction is completing on the frontend but
    the status isn't reflecting the change."

Intent-vs-implementation prompting example (verbatim):
  "A user should be able to see their current status without refreshing
  the page" (intent) rather than "Add a polling mechanism to this
  component" (implementation).
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-thoughtworks-harmellaw-nfr-guardrail.md`,
`blog-thoughtworks-gall-supervisory-engineering.md`,
`blog-thoughtworks-aliyeva-werner-lammel-path-to-production.md`,
`blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`,
`blog-thoughtworks-kamelman-delegation-architecture.md`,
`blog-thoughtworks-xiong-five-controllers-one-graph.md`, and
`blog-thoughtworks-anand-agent-evaluation-framework.md` were re-read directly
(MINER.md §4b) and claim numbers below were confirmed against those notes'
numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-thoughtworks-gall-supervisory-engineering.md` Claim 2 ("In the
    middle loop, the human engineer evaluates whether the agent actually
    solved the right problem") and Claim 9 ("evaluating" requires deep
    system context to judge plausible-looking code against real-world
    conditions): this article's Claim 8 (engineers "elevated," not
    replaced, valued for review/diagnosis/judgment) independently converges
    on the same reframing of engineering value from a different author, a
    few months later, from the same trusted feed.
  - `blog-thoughtworks-aliyeva-werner-lammel-path-to-production.md` Claim 8
    ("technology is rarely the primary blocker... the bigger challenge is
    organizational"): this article's Claim 7 (specification quality, not
    implementation speed, becomes the bottleneck) makes an adjacent
    argument at the individual-requirement level rather than the
    organizational-process level — both agree the constraint has moved
    upstream of code generation.
  - `blog-thoughtworks-kamelman-delegation-architecture.md` Claim 8
    (delegation "requires more than permission; it requires a model of
    competence, risk and consequence") and `blog-thoughtworks-xiong-five-controllers-one-graph.md`
    Claim 1 (an agent is "a delegation of human judgment"): this article's
    Claim 9 (the human's role reduced to "providing the specification and
    validating that the output matched the intent") is a concrete,
    small-scale instance of exactly the delegation relationship both of
    those more theoretical pieces describe — though this article does not
    engage with either piece's emphasis on bounded authority or oversight
    structure (see Contradicts below).

- **Contradicts**:
  - **`blog-thoughtworks-harmellaw-nfr-guardrail.md` Claim 1** — filed as
    **contradiction issue #3240**. Harmel-Law's central thesis is that LLMs
    "don't infer [non-functional requirements] up front" unless explicitly
    prompted ("Our bias is theirs. The blind spot is the same"), citing
    "security postures that were never specified and therefore never
    enforced" as a concrete symptom. This article's Claim 5 states the
    opposite for the specific case of security: "Security controls were
    applied without being requested," including password hashing with
    industry-standard algorithms — described as one of five *default*
    agent behaviors, not something the human had to specify. Both are
    anecdotal, single-source practitioner claims from the same trusted
    Thoughtworks feed, on the same underlying question, reaching opposite
    conclusions. Per MINER.md §4a, no verdict is picked here — see issue
    #3240 and the eventual CONTRADICTIONS.md entry for resolution.
  - **`blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 5**
    (three-tier oversight structure, including a mandatory "designated
    principal" — a specific human executive legally and operationally
    accountable for the agent's outcomes — for every deployed agent) and
    **`blog-thoughtworks-aliyeva-werner-lammel-path-to-production.md` Claim 5**
    (a four-gate model requiring, at Gate 3, penetration testing,
    use-case-specific bias/safety validation, and final CISO sign-off
    before a system is considered production-ready): this article
    describes reaching "production" (its own word, explicitly contrasted
    with "a prototype or a weekend toy project") in four weeks with no
    designated principal, no oversight tier, and no security/compliance
    gate of any kind mentioned (Claim 10). This is not asserted as false by
    the other two articles, and this Miner is not filing it as a formal
    contradiction (the Kartik article does not affirmatively claim these
    steps were skipped — it simply does not describe them either way), but
    it is a notable tension worth flagging for the Smith: three trusted-feed
    Thoughtworks sources disagree, at minimum by omission, on whether the
    kind of build this article describes would satisfy the governance
    machinery the other two prescribe as necessary for "production."

- **Extends**:
  - `blog-thoughtworks-gall-supervisory-engineering.md`: that article
    conceptually frames "directing," "evaluating," and "correcting" as the
    three pillars of supervisory engineering without a worked example. This
    article's seven-step operational loop and five named agent behaviors
    (Concrete Artifacts) supply a concrete, blow-by-blow illustration of
    what an agent does inside that "middle loop" on a single requirement,
    from the agent's side rather than the supervising engineer's side.
  - `blog-thoughtworks-anand-agent-evaluation-framework.md`: that article's
    four-step implementation roadmap (Claim 9, starting at ~20% automated
    test coverage) describes how an evaluation suite should mature over a
    project's lifecycle. This article gives no comparable detail for its
    own described build (Claim 10), which — read alongside Anand's
    roadmap — suggests either the build skipped this maturation process
    entirely or the article simply omits it; the note cannot distinguish
    between these from the text alone.

- **Novel**:
  - **The seven-step operational loop** (read → design → write → execute/
    observe → diagnose/fix → deliver, Claim 4 / Concrete Artifacts): no
    prior corpus source lays out this specific per-requirement sequence at
    this level of granularity for a single agent (as distinct from
    multi-agent orchestration pipelines documented elsewhere in the
    corpus).
  - **The "security by default" behavioral claim itself** (Claim 5): while
    the corpus has extensive security-governance content (NLP "never"
    lists, Data No-Go Zones, kill switches — all from
    `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`), no
    prior source claims an agent spontaneously applies security controls
    (e.g., password hashing) without being asked. This is new — and
    directly contested by an existing corpus claim, see Contradicts above.
  - **The 96-weeks-to-4-weeks estimate comparison** (Claim 2): a specific,
    if unverifiable and self-caveated, headline productivity figure not
    present elsewhere in this corpus's timeline-compression claims.
  - **The debugging-as-symptom-report framing** (Claim 3's second example,
    "the transaction is completing on the frontend but the status isn't
    reflecting the change"): a specific, concrete illustration of what a
    non-technical bug report looks like when the human is expected to
    describe symptoms, not diagnoses — pairs well with `blog-thoughtworks-gall-supervisory-engineering.md`'s
    more abstract "differential and behavioral review" framing (that
    article's Claim 5) by showing what triggers the loop from the human
    side.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the intent-vs-implementation
  prompting example (Claim 6 — "see status without refreshing the page"
  rather than "add a polling mechanism") as a concrete, immediately usable
  worked example for a section on writing effective natural-language
  requirements for agentic coding, alongside the symptom-vs-diagnosis
  framing for debugging requests (Claim 3).
- **Chapter 03 (Verification)**: Do NOT cite this article's "security by
  default" claim (Claim 5) as evidence that agentic coding reliably applies
  security controls unprompted — it directly contradicts
  `blog-thoughtworks-harmellaw-nfr-guardrail.md` Claim 1 (contradiction
  issue #3240, unresolved). If either claim is cited, present both per
  SMITH.md's `**Debated:**` treatment once the contradiction is resolved.
  Separately, flag Claim 10 (this article describes no testing/review/
  security-gating process for a build it calls "production-grade") as a
  reason to pair any citation of this article's headline timeline (Claim 2)
  with the more process-explicit `blog-thoughtworks-aliyeva-werner-lammel-path-to-production.md`
  four-gate model, so readers don't infer that four weeks and zero
  human-written code implies zero verification overhead.
- **Chapter 04 (Agent Implementation)**: Add the five recurring agent
  behaviors (Claim 5, minus the contested security-by-default item) and the
  seven-step operational loop (Claim 4) as a concrete, single-agent
  illustration of what "good" agentic coding behavior looks like at the
  level of an individual requirement — complements the existing
  multi-agent-orchestration material, which documents coordination across
  agents but not this granular a single-agent behavior trace.
- **Chapter 05 (Team Adoption)**: Add Claim 8 (engineers "elevated," valued
  for review/direction/diagnosis) as a third independent Thoughtworks voice
  corroborating `blog-thoughtworks-gall-supervisory-engineering.md`'s
  "middle loop" framing, for a section on how engineering roles change
  under heavy agentic adoption.

## Extraction Notes

1. **WebFetch declined full verbatim reproduction on the first pass, citing
   copyright; targeted quote extraction was used instead.** Consistent with
   this Miner's prior notes on other Thoughtworks pieces, the first WebFetch
   call returned a condensed synthesis with a stated copyright caveat rather
   than full body text. This note was built from seven separate,
   narrowly-scoped WebFetch calls: (1) an overview pass (author, project
   scope, timeline, metrics), (2) specification process and architecture,
   (3) verification/testing/oversight content — specifically probing for
   and confirming the absence of testing-framework, review-process, and
   security-audit detail (Claim 10), (4) lessons/recommendations and the
   engineer's-role argument, (5) exact-wording verification for the
   96-weeks/4-weeks and zero-human-code passages, (6) exact-wording
   verification for the specification-quality and "elevated" passages, and
   (7) exact-wording verification for the five behaviors and the
   governance/authorship question, plus a final targeted call confirming
   the byline (SG Kartik), publish date, and that no industry/company name
   is given anywhere in the article. Quotes used above were returned
   consistently across these passes; the two "no direct quote" fields
   (Claim 9's phrase "genuinely solve the problem" is used as a short
   verbatim fragment rather than a full sentence, since the surrounding
   sentence structure was not confirmed identically across passes) and
   Claim 10 (a structural absence, not a quote) are flagged as such per
   MINER.md §2a. The Assayer should still spot-check quotes against the
   live URL.
2. **No sub-pages followed.** The article is a short (roughly 1,200-1,500
   word), self-contained practitioner narrative; no inline links to further
   Thoughtworks documentation, named client case studies, or external
   sources were surfaced in any extraction pass.
3. **Contradiction filed before this note was finalized.** Per MINER.md
   §4a, contradiction issue **#3240** was filed prior to writing this note,
   documenting the tension between this article's Claim 5 (security
   controls applied "without being requested") and
   `blog-thoughtworks-harmellaw-nfr-guardrail.md` Claim 1 (LLMs do not infer
   non-functional requirements, including security posture, unless
   explicitly prompted). No verdict is asserted in this note; the
   contradiction awaits human/Smith resolution and a CONTRADICTIONS.md
   entry.
4. **Overall confidence rated "anecdotal."** Every claim in this article
   rests on one author's own first-person account of a single, unnamed
   project — no named client, no independently verifiable metric, no
   comparison condition, and (per Claim 10) no described verification or
   governance process for a build the author calls "production-grade." This
   is consistent with this corpus's treatment of comparable single-author,
   no-case-study-named Thoughtworks practitioner pieces (e.g.
   `blog-thoughtworks-kamelman-delegation-architecture.md`, rated
   anecdotal). The ideas and behavioral observations are coherent and
   consistent with other corpus sources on agentic coding practice (see
   Corroborates), but no individual claim in this note should be cited as
   independently verified, and the security-by-default claim specifically
   should not be cited without the contradiction flag.
