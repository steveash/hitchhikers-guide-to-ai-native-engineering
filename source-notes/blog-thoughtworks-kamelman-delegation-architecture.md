---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/importance-agent-delegation-architecture
source_type: blog-post
title: "The importance of agent delegation architecture"
author: Matt Kamelman
date_published: 2026-08-06
date_extracted: 2026-08-20
last_checked: 2026-08-20
status: current
confidence_overall: anecdotal
issue: "#2815"
---

# The Importance of Agent Delegation Architecture

> Thoughtworks essay arguing that designing agentic systems is converging with
> the practice of management — bounded autonomy (what an agent may decide,
> under what conditions, with what observability and accountability) is the
> right analytic frame, guardrails alone cannot catch judgment failures, and
> "delegation architecture" is an emerging discipline bridging technical
> infrastructure and organizational governance.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, "Generative AI" blog category;
  published August 6, 2026; from the trusted feed `thoughtworks`. A ~short,
  unheaded-intro-plus-six-section think piece: "The job description has been
  changing for years," "An agent cannot be designed in isolation," "Guardrails
  are only one part of the problem," "Software is moving from execution to
  delegation," "The organizational consequence," "When delegation becomes
  architecture." No named framework, numbered model, or step-by-step
  methodology is presented — unlike the same author's co-authored pieces
  (see Cross-References), this is a conceptual/argumentative essay, not a
  framework document.)
- **Author credibility**: Matt Kamelman ("Innovation Choreographer,
  Thoughtworks" per his byline elsewhere in this corpus) is a repeat author —
  see `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`,
  `blog-thoughtworks-kamelman-unbundling-expertise.md`, and
  `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`. Prior
  Miner notes on his solo and co-authored work found claims frequently
  asserted without external citation, evidence resting on the author's own
  synthesis/authority rather than data, studies, or named case studies. That
  pattern recurs here: this piece contains zero named case studies, metrics,
  or external citations — it is pure argumentative/conceptual writing, in
  contrast to the co-authored `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`
  (same broad topic, published one month earlier), which backs a structurally
  similar argument with two named production case studies and quantified
  outcomes.
- **Scope**: Covers a conceptual argument for why designing agent autonomy
  resembles management practice, why guardrails alone are insufficient
  governance, and why "delegation architecture" should be treated as a
  distinct discipline. Does NOT cover: a named framework, a numbered maturity
  model, specific technical controls (RBAC, NLP scanning, kill switches — see
  `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` for those),
  case studies, metrics, or code/config artifacts. It is intentionally
  positioned as the conceptual "why this discipline matters" essay rather than
  a "how to build it" document.

## Extracted Claims

### Claim 1: The right analytic question for an autonomous system is not "what can this agent do" but "bounded autonomy" — what it may decide, what it may do, under which conditions, with what observability, and under whose accountability
- **Evidence**: Author's direct framing claim under "An agent cannot be designed in isolation," presented as the reframing the rest of the article builds on.
- **Confidence**: emerging (a definitional/framing claim, not measured, but structurally consistent with — and possibly an earlier/looser articulation of — the same author's co-authored "bounded autonomy is the unit of governance" claim published a month later; see Cross-References)
- **Quote**: "what the system may decide, what it may do, under which conditions, with what observability, and under whose accountability."
- **Our assessment**: This is close in substance to `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md` Claim 10 ("Bounded autonomy is the unit of governance in the agentic era"), published a month earlier by the same author with a co-author. Read together, this article looks like Kamelman restating and elaborating that same framing concept in a solo, less-technical register aimed at a broader audience. Useful as a definitional anchor, but it is framing vocabulary, not a new mechanism or measured finding.

### Claim 2: Guardrails can prevent known, explicit-policy violations but cannot catch judgment failures — an agent can comply with every rule and still cause harm
- **Evidence**: Direct statement under "Guardrails are only one part of the problem," followed by three illustrative failure scenarios (see Claim 3).
- **Confidence**: emerging (a specific, falsifiable design claim, illustrated with named scenarios but not backed by an incident count or measured guardrail-failure rate)
- **Quote**: "Guardrails can prevent known actions; they can set spending limits, restrict data access, block destructive commands and require approval when thresholds are crossed."
- **Quote** (the limitation): "A customer-service agent, for instance, might comply with every explicit policy and still damage a relationship through poor judgment."
- **Our assessment**: This is the article's central operational claim and directly corroborates the "delegation failure" category named in `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md` Claim 5 ("The model worked. The platform worked. The practitioner controls worked. The agent did what it was allowed to do. The organization still suffered harm.") — both pieces, by the same author a month apart, describe the identical failure pattern (rule-compliant agent, harmed organization), this article in narrative/illustrative form, the co-authored piece as a named taxonomy category. This is a strong within-author convergence, not independent corroboration from a separate voice.

### Claim 3: Three illustrative scenarios show guardrail-compliant agents still causing harm through poor judgment: a customer-service agent damaging a relationship, a procurement agent accepting exposure-creating contract terms within its financial limit, and a coding agent passing every test while degrading architecture
- **Evidence**: Three parallel hypothetical (not documented/named) examples under "Guardrails are only one part of the problem."
- **Confidence**: anecdotal (illustrative, author-constructed scenarios, not reported incidents or case studies — no named company, agent, or outcome data)
- **Quote**: "A procurement agent might stay within its financial limit while accepting terms that create long-term exposure."
- **Quote** (coding example): "A coding agent might pass every automated test while introducing an architecture that becomes progressively harder to change."
- **Our assessment**: These are constructed illustrations, not case studies — treat as plausible narrative gloss on Claim 2, not as evidence of measured incidence. The coding-agent example ("passes every test, architecture gets harder to change") is a specific, guide-relevant scenario: it is a variant of the "tests are necessary but not sufficient for correctness" theme already present in this corpus (see Cross-References → Corroborates, `blog-addyosmani-code-agent-orchestra.md` Claim 5's comprehension-debt material) but framed at the architecture-erosion level rather than the comprehension-gap level.

### Claim 4: A core unresolved accountability question for agent deployment is who owns the consequences when an agent acts correctly within its instructions and the organization still suffers harm
- **Evidence**: Direct rhetorical question posed under "An agent cannot be designed in isolation," left unanswered in the article (no proposed accountability mechanism given here).
- **Confidence**: anecdotal (posed as an open question, not resolved with a mechanism in this piece)
- **Quote**: "Who owns the consequences when it acts correctly within its instructions and the organization still suffers harm?"
- **Our assessment**: This article poses the question without an answer; `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 5 (the "designated principal" — a specific human executive legally and operationally accountable for the agent's outcomes) and `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 1 (the Andon Labs case: "no governance document, no designated principal and no clear liability chain") supply the concrete mechanism this article leaves open. Worth citing together: this piece motivates the question, the Gordon/Kamelman piece answers it.

### Claim 5: Delegation design requires answering, at minimum, which decisions can be delegated, what an agent may do without approval, which actions must remain reversible, and when escalation is required
- **Evidence**: Direct enumeration under "An agent cannot be designed in isolation," presented as the minimum question set a delegation design must answer.
- **Confidence**: emerging (a specific, actionable checklist, though presented without worked examples or a named organization that has applied it)
- **Quote**: "which decisions can be delegated, what an agent may do without approval, which actions must remain reversible, when escalation is required"
- **Our assessment**: This checklist maps closely onto `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 5's three-tier oversight structure (manual/semi-automated/automated) and its Tier 2 "dynamic escalation" example (negotiations above $10,000 auto-paused and routed to a human supervisor) — that article supplies a concrete, numeric worked example of exactly the "when escalation is required" question this article poses abstractly. Useful as a compact checklist for a guide section, but on its own it is a list of questions to answer, not a method for answering them.

### Claim 6: Designing autonomous agent systems and managing a high-performing human team are converging into descriptions of the same underlying problem, because agentic systems are more sophisticated than software that simply executes predefined instructions
- **Evidence**: Direct comparative argument, contrasting what an engineering leader would say about harness design with what an experienced manager would say about running a team.
- **Confidence**: anecdotal (an analogical/rhetorical argument, not measured — no data comparing management practice to agent-harness design outcomes)
- **Quote**: "Ask an experienced engineering leader what a well-designed harness for an autonomous system should contain and the answer will usually include clear objectives, explicit constraints, bounded scope, escalation paths, observable performance and feedback loops that improve behavior over time. Ask an experienced manager how they run a high-performing team and the description is likely to be remarkably similar."
- **Quote** (the causal claim): "The convergence isn't an accident: we're beginning to build software systems that are more sophisticated than simply executing predefined instructions."
- **Our assessment**: This is the article's rhetorical centerpiece and its main contribution to the corpus's vocabulary — using management-practice language (objectives, constraints, scope, escalation, feedback) as the design vocabulary for agent harnesses. It is an analogy, not a demonstrated transfer of management technique to agent design; no organization's management-practice-derived harness design is documented as having been tried. Treat as a framing device for a guide section introducing agent-governance vocabulary to readers who already have management experience, not as a validated design methodology.

### Claim 7: Entry-level and junior job postings increasingly require production experience with cloud infrastructure, containers, and observability — a continuation of a multi-year trend toward "expert generalists" that is now extending to require agentic-systems literacy
- **Evidence**: Author's characterization of hiring-posting trends under "The job description has been changing for years," presented as historical background rather than sourced to a labor-market study or job-posting dataset.
- **Confidence**: anecdotal (a hiring-trend generalization asserted without citation to a labor-market study, survey, or job-posting corpus)
- **Quote**: "Entry-level job postings began asking candidates to understand not only how to write code, but how that code moved through cloud infrastructure and behaved in production. Production experience with AWS or GCP, containers, Kubernetes, observability and deployment pipelines appeared in roles still described as junior."
- **Quote** (the "expert generalist" framing): "Modern distributed software had already begun producing the expert generalist: someone with genuine depth in one area who could also understand how application code, infrastructure, deployment and operations interacted."
- **Our assessment**: This is asserted as observed trend, not measured against any job-posting dataset or labor statistics — should be flagged as an anecdotal generalization if cited in the guide, similar to how this Miner's prior notes on Kamelman's solo essays flag unsourced historical/labor generalizations (e.g., `blog-thoughtworks-kamelman-unbundling-expertise.md` Claim 5's tribal-elder analogy, also unsourced). Useful as color/motivation for a hiring-and-skills section, not as evidence.

### Claim 8: Traditional software required management too, but that management happened during design; agentic systems shift the central design question from "what should the system do" to "what decisions are we allowing the system to make about how that outcome is reached" — which is a delegation question requiring a model of competence, risk, and consequence, not just a permission
- **Evidence**: Direct argument under "Software is moving from execution to delegation," the article's structural pivot from historical background to the delegation-architecture thesis.
- **Confidence**: emerging (a specific, well-articulated reframing of what changed technically; not measured, but logically load-bearing for the rest of the article's argument)
- **Quote**: "Traditional software required management too, but most of that management happened during design."
- **Quote** (the reframed question): "The central question is no longer only, 'What should the system do?' It's also, 'What decisions are we allowing the system to make about how that outcome is reached?'"
- **Quote** (delegation vs. permission): "That's a delegation question — and delegation requires more than permission; it requires a model of competence, risk and consequence."
- **Our assessment**: This is a precise, citable distinction — permission (can it act) vs. delegation (what judgment can it exercise, and on what basis do we trust that judgment) — that sharpens the "capability vs. accountability" reframe already present in this corpus's governance sources. It corroborates and gives conceptual grounding to `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 11's closing thesis ("The question is not whether an AI agent can act on behalf of your organization; it is whether you have effectively defined the agent's authority before it does") — both articulate the same shift from a binary capability question to a delegation/authority question, this article naming the underlying mechanism (competence, risk, consequence modeling) that the Gordon/Kamelman piece asserts as a conclusion without deriving.

### Claim 9: Engineering and management have historically been separable disciplines — an engineer could understand orchestration without understanding organizational authority, and a manager could delegate without understanding production permissions/identity/escalation — but agentic systems collapse that separation because authority is expressed through technical architecture while technical decisions about tools, permissions, memory, and escalation determine the authority an agent can exercise in practice
- **Evidence**: Direct argument under "The organizational consequence," the article's account of why "delegation architecture" must be a single discipline rather than two separate ones (engineering and management).
- **Confidence**: emerging (a structural argument about why two previously separate disciplines must now converge; internally consistent, not independently tested against an organization that failed by keeping the disciplines separate)
- **Quote**: "An engineer can understand orchestration frameworks without understanding how authority moves through an organization; a manager can understand delegation while knowing little about how permissions, identity and escalation are implemented in production systems."
- **Quote** (why this breaks down): "Agentic systems challenge that separation. The authority granted to an agent is expressed through technical architecture, while technical decisions about tools, permissions, memory and escalation determine the authority it can exercise in practice."
- **Our assessment**: This is the article's clearest organizational-stakes claim: it argues that organizations cannot solve agent governance by having Legal/Management define policy and Engineering implement it separately, because the technical architecture *is* the policy in practice. This directly corroborates the "Thoughtworks advantage" positioning in `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 9 (bridging Legal and Platform Engineering, "if your legal constraints cannot be translated into running code, they do not exist") and the "governance travels with the code" principle in `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md` Claim 7 — three Thoughtworks pieces now converge on governance-must-be-technical-architecture, not policy-plus-implementation-as-separate-steps.

### Claim 10: Agentic systems introduce a different design problem than traditional software because they interpret goals, select actions at runtime, and exercise discretion within a defined environment — so the central design challenge is deciding what judgment should be delegated, making that decision executable, and remaining accountable for what happens afterward
- **Evidence**: Direct closing argument under "When delegation becomes architecture," the article's summary statement of its own thesis.
- **Confidence**: emerging (a compressed restatement/synthesis of the article's argument rather than new evidence)
- **Quote**: "Agentic systems introduce a different design problem. They interpret goals, select actions at runtime and exercise discretion within a defined environment."
- **Quote** (the challenge, restated): "The central challenge is therefore not simply building capable agents. It is deciding what judgment should be delegated, making that decision executable and remaining accountable for what happens afterward."
- **Our assessment**: This is the single most citable summary sentence in the piece — "what judgment should be delegated, making that decision executable, remaining accountable" is a compact three-part checklist (decide / execute / stay accountable) that a guide section could use as a section epigraph or organizing structure. It restates Claims 1, 5, and 9 rather than introducing new content.

### Claim 11: The discipline of agent delegation architecture will be mature when organizations stop asking only what an agent can do and start explicitly designing what authority it should hold, how that authority may be exercised, and how it can be withdrawn
- **Evidence**: Author's closing thesis statement.
- **Confidence**: anecdotal (a forward-looking maturity marker, asserted rather than derived from a maturity model or measured criteria)
- **Quote**: "We'll know the discipline has matured when organizations stop asking only what an agent can do and begin designing, explicitly, what authority it should hold, how that authority may be exercised and how it can be withdrawn."
- **Our assessment**: This closing line is a strong, quotable candidate for a chapter epigraph on agent governance maturity. Note the implicit tension with `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md` (same author, published a month earlier): that piece already presents a fully specified four-layer harness framework with two named, quantified production case studies (Parloa, Morgan Stanley) as evidence the discipline is being built today, while this piece frames the discipline as still immature and asks readers to imagine what maturity would look like. This reads as a register difference (a broad-audience conceptual essay vs. a technical framework document) rather than a substantive contradiction — see Cross-References and Extraction Notes.

## Concrete Artifacts

```
Source: Matt Kamelman, "The importance of agent delegation architecture,"
Thoughtworks Insights, published August 6, 2026.

Section structure (verbatim heading order):
  (unheaded intro)
  The job description has been changing for years
  An agent cannot be designed in isolation
  Guardrails are only one part of the problem
  Software is moving from execution to delegation
  The organizational consequence
  When delegation becomes architecture
  (unheaded closing paragraph)

Three illustrative guardrail-compliant-but-harmful scenarios (Claim 3):
  1. Customer-service agent: complies with every explicit policy, still
     damages a customer relationship through poor judgment.
  2. Procurement agent: stays within its financial limit, still accepts
     contract terms that create long-term exposure.
  3. Coding agent: passes every automated test, still introduces an
     architecture that becomes progressively harder to change.

Delegation design question set (Claim 5):
  - Which decisions can be delegated?
  - What may an agent do without approval?
  - Which actions must remain reversible?
  - When is escalation required?
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`,
`blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`,
`blog-thoughtworks-kamelman-unbundling-expertise.md`, and
`blog-addyosmani-code-agent-orchestra.md` were re-read directly (MINER.md
§4b) and claim numbers below were confirmed against those notes' numbered
`### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`
    Claim 5 (the named "delegation failure" category: "The model worked. The
    platform worked. The practitioner controls worked. The agent did what it
    was allowed to do. The organization still suffered harm.") and Claim 10
    ("Bounded autonomy is the unit of governance in the agentic era. The
    harness is what makes bounded autonomy governable."): This article's
    Claim 1 (bounded autonomy framing) and Claim 2/3 (guardrail-compliant
    agents still causing harm) are the same author's less-technical,
    narrative restatement of concepts that article names as a formal
    taxonomy category and a definitional anchor, respectively. Because both
    pieces share an author (Kamelman) and were published roughly a month
    apart, this is within-author convergence/restatement rather than
    independent corroboration from a separate voice — worth noting as such
    if cited together.
  - `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 5
    (three-tier manual/semi-automated/automated oversight, including the
    "designated principal" accountable-executive requirement and the
    $10,000-threshold dynamic-escalation example) and Claim 1 (the Andon Labs
    case: "no governance document, no designated principal and no clear
    liability chain"): This article's Claim 4 (who owns the consequences when
    an agent acts correctly within instructions and harm still occurs) and
    Claim 5 (the delegation question checklist, including "when escalation is
    required") are posed as open questions here; the Gordon/Kamelman piece
    supplies concrete, named mechanisms that answer them.
  - `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 11
    (closing thesis: "The question is not whether an AI agent can act on
    behalf of your organization; it is whether you have effectively defined
    the agent's authority before it does."): This article's Claim 8 (the
    central design question shifts from "what should the system do" to "what
    decisions are we allowing the system to make," which is "a delegation
    question" requiring "a model of competence, risk and consequence") names
    the underlying mechanism behind the same capability-to-authority reframe.
  - `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 9
    (Thoughtworks bridges Legal and Platform Engineering; "if your legal
    constraints cannot be translated into running code, they do not exist")
    and `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`
    Claim 7 ("governance travels with the code" — the Parloa case study's
    repo-resident governance layers): This article's Claim 9 (engineering and
    management were separable disciplines, but agentic systems collapse that
    separation because "the authority granted to an agent is expressed
    through technical architecture") is the conceptual argument underlying
    both of those more concrete/technical claims — three Thoughtworks pieces
    now converge on governance-as-technical-architecture rather than
    governance-as-separate-policy-document.
  - `blog-addyosmani-code-agent-orchestra.md` Claim 5 (the bottleneck has
    shifted from generation to verification, corroborated by comprehension-
    debt research showing AI users scored 17% lower on comprehension
    quizzes): This article's coding-agent example in Claim 3 ("might pass
    every automated test while introducing an architecture that becomes
    progressively harder to change") is a specific instance of the same
    underlying concern — automated checks (tests) are necessary but
    insufficient for catching harm, from a different angle (architectural
    erosion vs. comprehension gap) and a different author/publication.

- **Contradicts**: No contradiction issue filed. One register tension is
  worth flagging rather than escalating: this article's closing line frames
  agent delegation architecture as an *immature* discipline ("We'll know the
  discipline has matured when organizations stop asking only what an agent
  can do and begin designing, explicitly, what authority it should hold...")
  — implying organizations are still mostly asking capability questions —
  while `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`,
  co-authored by the same Kamelman one month earlier, presents a fully
  specified four-layer harness framework already deployed at Parloa and
  Morgan Stanley with quantified outcomes. Read together, one piece implies
  the field is still nascent and the other implies Thoughtworks has already
  operationalized it at scale. Per the reasoning already applied to a
  structurally similar tension in
  `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`'s own
  Cross-References (comparing that piece to
  `blog-thoughtworks-kamelman-ai-governance-category-error.md`), this reads
  as a difference in register and audience (a broad-audience conceptual essay
  making a discipline-framing argument vs. a technical framework document
  citing named production deployments) rather than a material claim
  contradiction that would change guide advice — both pieces agree on what
  a mature practice would contain; they differ only in how far along the
  industry currently is. Per MINER.md §4a's "when NOT to file" guidance, no
  new contradiction issue was opened.

- **Extends**:
  - `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`: That
    article supplies a named legal/operational framework (actual vs. apparent
    authority, three-tier oversight, specific technical controls) motivated
    by a single case study. This article supplies the broader conceptual
    argument for *why* such a framework is necessary in the first place — the
    management-practice analogy (Claim 6) and the guardrails-insufficiency
    argument (Claim 2) are the "why," while Gordon/Kamelman's piece is the
    "what."
  - `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`:
    That article's four-layer harness taxonomy and "delegation failure"
    category are the technical/organizational implementation of the same
    underlying idea this article argues conceptually. This article can serve
    as the accessible framing/motivation piece a guide section could open
    with before introducing the more technical four-layer taxonomy.

- **Novel**:
  - **The engineering-manager convergence argument** (Claim 6): while this
    corpus's governance sources use management-adjacent vocabulary
    (accountability, escalation, oversight), no prior corpus source
    explicitly argues that agent-harness design and team management are
    "becoming different descriptions of the same problem" because agentic
    systems are more sophisticated than instruction-executing software. This
    specific analogical framing is new.
  - **The delegation-vs-permission distinction** (Claim 8: delegation
    "requires more than permission; it requires a model of competence, risk
    and consequence"): a precise, quotable distinction not named elsewhere in
    the corpus's governance sources, which mostly discuss permission/access
    scoping (RBAC, least-agency, Data No-Go Zones) without separately naming
    the competence/trust dimension.
  - **The three parallel guardrail-compliant-but-harmful scenarios**
    (Claim 3): a compact, memorable illustration format (three domains: CS,
    procurement, coding) not present elsewhere in the corpus in this exact
    triptych form, though each domain's underlying concern (poor judgment
    within policy, contract exposure, architectural erosion) echoes prior
    sources individually.

## Guide Impact

- **Chapter 06 (Security/Threat Model)**: Add the "guardrails prevent known
  actions, not judgment failures" distinction (Claim 2) as an explicit
  framing for why rule-based agent controls are necessary but insufficient —
  pair with the three illustrative scenarios (Claim 3) as concrete "guardrail
  passed, harm occurred anyway" examples a threat-modeling exercise could use
  as prompts ("could our agent pass every check we have and still cause this
  kind of harm?"). This complements, rather than duplicates, the specific
  technical controls (RBAC, NLP "never lists," kill switches) already sourced
  from `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`, which
  answers "what controls do we build" where this article answers "why
  controls alone aren't enough."

- **Chapter 05 (Team Adoption — Organizational Governance)**: Add the
  delegation-design question checklist (Claim 5 — which decisions can be
  delegated, what an agent may do without approval, which actions must
  remain reversible, when escalation is required) as a lightweight,
  discussion-starter checklist for teams defining a new agent's scope, to be
  used before reaching for the heavier three-tier oversight framework already
  sourced from `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`.
  Add Claim 9's argument (engineering and management were separable
  disciplines, but agentic systems collapse that separation) as a
  cross-functional-ownership rationale for why agent governance decisions
  cannot be delegated entirely to either an engineering team or a management/
  policy team in isolation.

- **Chapter 02 (Harness Engineering)**: Add the delegation-vs-permission
  distinction (Claim 8 — delegation "requires more than permission; it
  requires a model of competence, risk and consequence") as conceptual
  grounding for why harness design (CLAUDE.md/AGENTS.md scoping, tool
  permissions) should be justified by a stated model of what the agent is
  competent to judge, not simply by what actions are technically blocked or
  allowed.

## Extraction Notes

1. **WebFetch declined full verbatim reproduction; targeted quote extraction
   was used instead.** As with this Miner's prior notes on other Thoughtworks
   Kamelman pieces, a first WebFetch call against the article returned only a
   condensed, paraphrased summary (with copyright caveats from the underlying
   model), not full verbatim body text. Rather than attempting a raw-HTML
   `curl` fetch (not available as a tool in this session), this note was
   built from five separate, narrowly-scoped WebFetch calls, each asking for
   verbatim quotes on a specific sub-topic (bounded autonomy/guardrails/
   accountability; task decomposition/escalation/observability; section
   headings and closing/opening text; the three middle sections' arguments).
   Several quotes (the bounded-autonomy definition, the customer-service
   example, the section-heading list) were independently returned by more
   than one separately-scoped call with identical wording, which is the best
   verification available in this session that the extracted text is
   accurate rather than a paraphrase drifting between calls. The Assayer
   should still spot-check quotes against the live URL.
2. **No sub-pages followed.** No inline links to further Thoughtworks
   framework documentation or external sources were surfaced in any of the
   targeted extraction passes; the article appears self-contained, consistent
   with the "no external citation" pattern already noted in this Miner's
   prior Kamelman-authored source notes.
3. **No contradiction issue filed.** See Cross-References → Contradicts
   above: a register tension with the same author's
   `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md` is
   flagged but assessed as a difference in audience/register (conceptual
   essay vs. technical framework document with case studies), not a material
   contradiction, following the same reasoning precedent already applied to a
   structurally similar tension elsewhere in the Thoughtworks Kamelman
   cluster.
4. **Overall confidence rated "anecdotal."** This piece contains no named
   case studies, no metrics, no external citations, and no independently
   verifiable claims — every claim rests on the author's own argumentative
   synthesis and analogy (management-practice comparison, hypothetical
   illustrative scenarios, asserted hiring-trend generalizations). This rates
   lower than the co-authored `blog-thoughtworks-squeo-kamelman-operating-system-enterprise-ai.md`
   (rated "emerging," on the strength of two named quantified case studies)
   and `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` (rated
   "emerging," on the strength of a named case study and a legal
   practitioner co-author), but the ideas themselves are coherent, consistent
   with this author's other published framing, and useful as conceptual
   scaffolding/motivation for a guide section — hence "anecdotal" rather than
   the lowest-confidence treatment, with the caveat that no individual claim
   in this note should be cited as independently verified.
