---
source_url: https://www.thoughtworks.com/insights/articles/how-enterprises-can-reclaim-customer-interactions
source_type: blog-post
title: "How enterprises can reclaim customer interactions from third-party AI platforms"
author: Ahmet Sakar
date_published: 2026-08-06
date_extracted: 2026-08-19
last_checked: 2026-08-19
status: current
confidence_overall: anecdotal
issue: "#2783"
---

# How Enterprises Can Reclaim Customer Interactions From Third-Party AI Platforms

> Thoughtworks Insights essay arguing that customers now route product
> questions to ChatGPT, Claude and Gemini instead of a company's own
> channels, and that most attempts to "reclaim" that interaction with an
> in-house conversational AI channel fail because they don't solve three
> hard problems together (sub-second speed, a trust boundary around
> actions, and hallucination-proof answers) — proposing a named "3/3/3"
> delivery motion (3 days concept → 3 weeks prototype → 3 months build and
> launch) to validate feasibility, business value and customer fit before
> committing to a multiyear program.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, published August 6, 2026;
  auto-discovered from the trusted feed `thoughtworks`). Structured as: a
  framing intro, a "TL;DR" callout, a three-part "why pilots fail" section
  (numbered 01-03), a prescriptive "how to build a conversational channel
  that works" section introducing the 3/3/3 motion, and a closing
  "question for your board" section. Includes a "Sources and further
  reading" citation block naming three external reports.
- **Author credibility**: Ahmet Sakar is credited as the article's sole
  byline ("By Ahmet Sakar"); no title, role, or bio is given anywhere in
  the fetched article text — this matches a pattern already documented in
  this corpus for several other Thoughtworks Insights bylines (e.g.
  `blog-thoughtworks-karle-discovery-dilemma.md`,
  `blog-thoughtworks-puthanveedu-choudhary-overenthusiasm-financial-services.md`).
  Thoughtworks is an already-established vendor-neutral consultancy source
  in this corpus. The article names and attributes three external sources
  (OpenAI/TechCrunch and OpenAI/The Verge usage statistics; a Gartner press
  release quoting a named analyst) in a dedicated "Sources and further
  reading" block — stronger external sourcing discipline than several
  comparable single-author Thoughtworks opinion essays in this corpus that
  cite no named source for their statistics (contrast
  `blog-thoughtworks-kamelman-ai-governance-category-error.md`).
- **Scope**: Covers the strategic case for building an in-house
  conversational customer channel, the three specific technical/business
  problems (speed, trust/action boundary, certifiability of answers) that
  make this hard, and a named delivery methodology (3/3/3) for validating
  and shipping one. Mentions "AI/works™, Thoughtworks' agentic development
  platform" as the delivery substrate underneath the cadence, but gives no
  technical detail, architecture diagram, or named client outcome for that
  platform. Does NOT cover: a named client case study or before/after
  outcome metric for any organization that has run the 3/3/3 motion;
  technical implementation detail for how "structurally impossible"
  hallucination is achieved; or a defined governance/accountability model
  for agent-initiated actions (e.g., who signs off, what audit trail is
  required) beyond naming CISO/regulator/general-counsel sign-off as a
  blocker.

## Extracted Claims

### Claim 1: Customers increasingly route product and service questions to third-party conversational AI assistants (ChatGPT, Claude, Gemini) instead of a company's own website, app, or call center, receiving a complete answer in a conversation the company is not part of but is still accountable for
- **Evidence**: Author's opening framing observation, illustrated with three
  example customer questions, presented as the article's motivating premise.
- **Confidence**: anecdotal (a framing assertion about a behavioral shift,
  not backed by first-party usage data specific to any named company or
  industry — the article's only supporting data point is the general
  ChatGPT scale statistic in Claim 2, not evidence that customers
  specifically ask *product* questions there instead of company channels)
- **Quote**: "Increasingly, they go to ChatGPT, Claude and Gemini instead,
  where customers get a complete, personalized answer in seconds in a
  conversation you're not part of, with an outcome you'll still be held to."
- **Our assessment**: This is the article's load-bearing thesis and the
  reason the Prospector flagged it as high-novelty — it names a specific
  competitive-disintermediation risk (traffic numbers look normal while the
  pre-arrival decision-making conversation has moved elsewhere) that isn't
  addressed by traditional channel-performance metrics. The claim is
  plausible and consistent with general-purpose-AI-assistant adoption
  trends elsewhere in the corpus, but this article supplies no
  company-specific or industry-specific data confirming customers use
  third-party AI for *this company's* product questions specifically,
  as opposed to general information-seeking.

### Claim 2: ChatGPT alone handles over 2.5 billion messages a day from 900 million weekly active users, illustrating the scale of conversational-AI usage customers have already normalized
- **Evidence**: Two externally attributed statistics, cited in the article's
  "Sources and further reading" block to named reports (OpenAI figures as
  reported in The Verge, July 2025, and TechCrunch, February 2026).
- **Confidence**: emerging (both figures are attributed to named,
  checkable third-party reporting rather than left as unsourced assertions
  — stronger sourcing than most individual claims in comparable
  single-author Thoughtworks essays in this corpus — but neither figure was
  independently re-verified against the original TechCrunch/Verge articles
  by this Miner)
- **Quote**: "With ChatGPT alone handling over 2.5 billion messages a day
  from 900 million weekly active users, customers have already imported the
  expectation of conversational immediacy into every interaction they
  have."
- **Our assessment**: This is the article's one concrete, externally-sourced
  data point, used to justify the "customers expect conversational
  immediacy everywhere" claim in the same sentence. The scale statistic
  itself (messages/users) is well-attributed; the causal inference drawn
  from it ("customers have already imported the expectation... into every
  interaction") is the author's own interpretation, not something the cited
  statistics directly measure.

### Claim 3: Nearly all attempts by enterprises to "reclaim" the customer conversation with their own AI-powered channel fail to survive contact with real customers, despite every vendor pitch being built on the promise that they will
- **Evidence**: Author's direct assertion, stated as the pivot from the
  "instinct" to build an in-house channel to the article's actual
  prescription (validate before committing).
- **Confidence**: anecdotal (a strong claim — "almost none... survive" — with
  no named failure count, survey, or case study given; the closest the
  article comes to substantiating a failure rate is the separately-cited
  Gartner agentic-AI-project-cancellation statistic in Claim 5, which
  measures a different thing — project cancellation generally, not
  conversational-channel pilots specifically)
- **Quote**: "Every vendor pitch is built on some version of that promise.
  Almost none of the resulting deployments survive contact with real
  customers."
- **Our assessment**: This is the article's key motivating claim for why the
  3/3/3 methodology (validate-before-build) is necessary rather than a
  large upfront program. It corroborates
  `blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md` Claim 7
  ("stop funding isolated demos and instead build the underlying
  operational substrate") — both sources distrust the assumption that a
  working demo or pilot predicts production survival. Neither source
  quantifies the actual failure rate with data specific to conversational
  AI channels.

### Claim 4: A conversational channel must hold sub-second response pace — the threshold at which a human conversation partner assumes something has gone wrong — because ChatGPT, Claude and Gemini already respond in under a second, and customers who experience slower pace don't complain, they silently switch back to whichever channel answered faster
- **Evidence**: Author's direct claim about conversational pacing norms and
  customer churn behavior, presented as the first of three "hard problems."
- **Confidence**: anecdotal (asserted as a behavioral pattern — "customers
  don't complain, they simply stop using it" — without churn data, A/B
  test results, or a cited latency study)
- **Quote**: "That threshold is well under a second. The benchmark in your
  customer's head is now ChatGPT, Claude and Gemini, all of which already
  respond in under a second."
- **Quote**: "If your channel can't hold that pace consistently, customers
  don't complain. They simply stop using it and go back to the channel
  where they got the answer faster, which is no longer yours."
- **Our assessment**: The "silent churn, not complaint" framing is a useful
  operational point for any chapter on latency budgets — it argues that
  latency failures in a conversational channel are invisible in typical
  complaint/ticket-volume monitoring and will only show up as unexplained
  usage decline. No cited data connects response-time thresholds to actual
  churn rates for any named deployment, so treat the specific "well under a
  second" threshold as an asserted heuristic, not a measured cutoff.

### Claim 5: Routing every customer message through the heaviest/largest AI model in the stack is both too slow and too expensive to operate at production scale, and Gartner predicts more than 40% of agentic AI projects will be canceled by the end of 2027 because "many use cases positioned as agentic today don't require agentic implementations"
- **Evidence**: Author's cost/architecture claim, combined with an
  externally attributed statistic and a direct named quote from a Gartner
  press release.
- **Confidence**: emerging (the Gartner prediction is attributed to a named,
  dated press release and a named analyst — the strongest single citation
  in the article — though this Miner did not independently re-verify the
  figure against the original Gartner release; the preceding cost/latency
  claim about routing every message through the "heaviest AI" is the
  author's own architectural assertion, not itself sourced to Gartner or
  any other citation)
- **Quote**: "Run every reply through the heaviest AI in the stack and your
  unit economics collapse before you've even launched."
- **Quote**: "In June 2025, Gartner predicted that more than 40% of agentic
  AI projects will be canceled by the end of 2027."
- **Quote**: "Many use cases positioned as agentic today don't require
  agentic implementations." — Anushree Verma, Senior Director Analyst,
  Gartner (as quoted in the article)
- **Our assessment**: This is the article's most citable external
  data point and directly extends the corpus's existing routing/cost
  literature — it names model-routing cost blowup as one of the *specific*
  reasons conversational-channel pilots never reach production, connecting
  a widely-cited industry cancellation statistic (Gartner) to a concrete
  mechanism (routing every reply through the largest model) rather than
  leaving "40% of agentic projects get canceled" as an unexplained
  statistic. The Verma quote's point — that many agentic use cases don't
  need full agentic implementations — is a useful complement to any guide
  discussion of over-applying agentic architecture where a lighter-weight
  pattern would do.

### Claim 6: A conversational channel that can only talk, without being able to take real actions (moving money, changing an address, filing a claim, booking a service), delivers all the cost of building it and none of the business value — most organizations respond to the risk of allowing actions by keeping pilots read-only rather than solving the risk
- **Evidence**: Author's direct claim, framed as the second of three "hard
  problems" (the trust boundary around a channel that can act).
- **Confidence**: anecdotal (an architectural/organizational generalization
  about how "most organizations" respond to action risk, with no survey or
  named-company data on how many conversational AI pilots are actually
  read-only)
- **Quote**: "Most organizations today respond to that risk by saying no.
  Pilots stay in read-only sandboxes, unable to actually do anything useful
  for the customer."
- **Quote**: "But a read-only conversational channel isn't a customer
  channel. It's a brochure with a microphone. You get all the cost of
  building it, none of the business value."
- **Our assessment**: The "brochure with a microphone" framing is a sharp,
  quotable diagnostic for why chatbot pilots stall at the demo stage — it
  names a specific failure pattern (action-avoidance) distinct from the
  speed problem in Claim 4. It aligns directionally with
  `blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md` Claim 4
  (governance cannot be retrofitted after deployment; it must be built into
  the operating environment's "original DNA") — both sources treat
  avoiding the action-risk problem (via read-only scope or bolted-on
  controls) as a non-solution, though this article frames it from the
  product-value side (a read-only channel has no business value) while
  Marr/Mohanty frame it from the governance-architecture side.

### Claim 7: The moment a conversational AI is allowed to take action on a customer's behalf, it enters the same risk envelope as other serious business channels (call centers, apps, branches) but without the decades-old security, audit and compliance controls those channels already have — making it correctly something a CISO, regulator, or general counsel will not sign off on by default
- **Evidence**: Author's direct architectural/risk claim, presented as the
  explanation for why the trust-boundary problem is "genuinely hard," not
  merely a matter of enterprise caution.
- **Confidence**: anecdotal (a risk-framing assertion; no named regulatory
  citation, incident, or specific control gap is enumerated beyond the
  general claim that decades-old controls don't yet exist for this channel
  type)
- **Quote**: "Giving a generative AI the keys to your systems is not
  something your CISO, your regulator or your general counsel will sign off
  on by default, and they're right not to."
- **Our assessment**: This explicitly validates rather than dismisses
  enterprise caution about agentic action — a notable framing choice
  (the article agrees the gatekeepers are "right"), distinct from sources
  in this corpus that argue primarily for *removing* friction around AI
  adoption (contrast `blog-thoughtworks-ryan-ai-shadow-it-paved-roads.md`,
  which argues for building "paved roads" so sanctioned AI tooling is
  easier to use than shadow-IT workarounds). This article instead treats
  the trust-boundary problem as requiring engineering, risk, and governance
  work to be "solved together" before action-taking is safe, not as
  friction to be removed by enablement alone.

### Claim 8: A customer-facing conversational channel cannot be built on a system that might hallucinate — for the answers that matter (numbers, policies, entitlements, decisions), hallucination has to be made structurally impossible, which requires rethinking the relationship between the AI and the underlying systems of record rather than trusting the model's own confidence
- **Evidence**: Author's direct claim, presented as the third "hard
  problem" (answers the business can stand behind), following a stated
  liability scenario (a misquoted premium, incorrect balance, hallucinated
  policy, or wrong eligibility decision).
- **Confidence**: anecdotal (a strong architectural prescription —
  "structurally impossible" — asserted without naming a specific technical
  mechanism, reference architecture, or worked example of how any
  organization achieved this)
- **Quote**: "You can't build a customer channel on a system that might
  hallucinate. It has to be built so that hallucination is structurally
  impossible for the answers that matter: the numbers, the policies, the
  entitlements and the decisions."
- **Quote**: "Solving it requires rethinking the relationship between the AI
  and your systems of record from the ground up, which is slow, expensive
  and unforgiving of mistakes."
- **Our assessment**: This is the article's clearest connection to
  Ch03/verification-relevant material in this corpus, though it names no
  concrete mechanism (no deterministic execution layer, provenance chain,
  or grounding technique is described — contrast the much more detailed
  worked implementation in `blog-anthropic-kepler-verifiable-ai-financial.md`
  Claim 9, which describes a deterministic execution layer separating
  reasoning from computation for a similar "answers must be certifiably
  correct" requirement in financial services). Treat this claim as naming
  *what* must be true (structural impossibility of hallucination for
  high-stakes answers) without supplying *how*, and pair it with a source
  that supplies a worked mechanism if the guide wants to make this
  actionable.

### Claim 9: The "3/3/3" delivery motion — three days for concept validation, three weeks for a working prototype, three months for build-and-launch of a minimum lovable product (MLP) — progressively de-risks a conversational-AI investment across desirability, feasibility and business viability, replacing a traditional strategy-then-roadmap-then-multiyear-program approach that the article argues is too slow for this shift
- **Evidence**: Author's named prescriptive methodology, given as the
  article's central "how to build a conversational channel that works"
  recommendation, with an explicit reason for rejecting the traditional
  program-based alternative (assumptions go stale before a multiyear
  program lands).
- **Confidence**: anecdotal (a named delivery framework presented by a
  single author with no named client outcome, timeline data, or before/after
  comparison against the traditional multiyear-program approach it's
  contrasted with)
- **Quote**: "The typical response to a shift this size is to commission a
  strategy, build a roadmap and plan a multiyear program. It is the wrong
  response here."
- **Quote**: "Three days | Concept: Is this real for us?"
- **Quote**: "Three weeks | Prototype: Can we actually do this?"
- **Quote**: "Three months | Build and launch: What happens in the market?"
- **Our assessment**: This is the article's single most reusable,
  guide-relevant artifact — a named, time-boxed methodology rather than a
  vague "move fast and validate" platitude. The prototype phase's stated
  goals ("Prove the speed. Prove safe integration. Prove the answers stand
  up. Test with users.") map directly onto the three hard problems named in
  Claims 4, 6, and 8 (speed, trust/action boundary, certifiability) — the
  methodology is explicitly structured to force validation of exactly the
  three failure modes the article opened with. No named organization's
  outcome from running this specific 3/3/3 cadence is given, so it should
  be treated as a proposed practitioner framework, not a demonstrated
  result.

### Claim 10: Thoughtworks' AI/works™ agentic development platform underlies the 3/3/3 cadence by turning business needs into dynamic specifications and working code through coordinated AI agents, using established components and built-in guardrails so teams can accelerate development while maintaining security and compliance
- **Evidence**: Author's direct claim naming the specific commercial
  platform that enables the described delivery speed.
- **Confidence**: anecdotal (a vendor-platform capability claim for
  Thoughtworks' own commercial product, given with no independent
  technical detail, named client deployment, or third-party benchmark)
- **Quote**: "This is possible due to AI/works™, Thoughtworks' agentic
  development platform that sits underneath this cadence. The platform
  turns business needs into dynamic specifications and working code through
  coordinated AI agents."
- **Our assessment**: This is a vendor self-reference (Thoughtworks citing
  its own commercial platform as the enabling substrate for the
  methodology it's recommending) and should be flagged as such — the claim
  that AI/works specifically is what makes the 3/3/3 timeline achievable is
  unverifiable from this article alone, since no comparison is given
  against attempting the same cadence without that specific platform.
  Treat the 3/3/3 *methodology* (Claim 9) as separable from this specific
  platform claim: the delivery cadence could plausibly be attempted with
  other tooling, even though the article frames AI/works as what "makes it
  possible."

## Concrete Artifacts

### The 3/3/3 delivery motion (as stated in the article)

```
Source: Ahmet Sakar, "How enterprises can reclaim customer interactions
from third-party AI platforms," Thoughtworks Insights, August 6, 2026

Three days | Concept: Is this real for us?
  -> Align executive sponsors on where your customers are moving, which
     conversations matter most to your business and what the shape of a
     first move looks like.

Three weeks | Prototype: Can we actually do this?
  -> Build a working prototype of a real customer conversation. Prove the
     speed. Prove safe integration. Prove the answers stand up. Test with
     users. Emerge with a business case grounded in evidence.

Three months | Build and launch: What happens in the market?
  -> Put an MLP (minimum lovable product) into the hands of customers.
     Measure actual impact on the relationship, the economics and the
     competitive position. Iterate from evidence.

Stated purpose: progressively de-risks investment across desirability,
feasibility and business viability.
```

### The three "hard problems" (as headed in the article)

```
Source: Ahmet Sakar, "How enterprises can reclaim customer interactions
from third-party AI platforms," Thoughtworks Insights, August 6, 2026

01. Speed that keeps customers engaged
    - What it costs you: silent churn back to whichever channel answers
      faster.
    - Why it's hard: routing every message through the heaviest model is
      too slow and too expensive to operate at scale.

02. The trust boundary around a channel that can actually act
    - What it costs you: read-only pilots ("a brochure with a microphone")
      deliver all the cost, none of the business value.
    - Why it's hard: action-taking AI enters the same risk envelope as
      other serious channels without their decades-old controls.

03. Answers your business can stand behind
    - What it costs you: one confidently wrong answer (misquoted premium,
      incorrect balance, hallucinated policy, wrong eligibility decision)
      creates liability that lands on the enterprise, not the AI vendor.
    - Why it's hard: hallucination must be made structurally impossible
      for high-stakes answers, requiring the AI-to-systems-of-record
      relationship to be rethought from the ground up.
```

### Cited external statistics (attributed in the article's "Sources and further reading" block)

```
Source: Ahmet Sakar, "How enterprises can reclaim customer interactions
from third-party AI platforms," Thoughtworks Insights, August 6, 2026 —
"Sources and further reading" section

- OpenAI / TechCrunch ("ChatGPT reaches 900M weekly active users",
  Feb. 27, 2026): 900 million weekly active ChatGPT users.
- OpenAI / The Verge ("OpenAI says ChatGPT users send over 2.5 billion
  prompts every day", Jul. 21, 2025): 2.5 billion+ prompts/day.
- Gartner press release ("Gartner Predicts Over 40% of Agentic AI
  Projects Will Be Canceled by 2027", Jun. 25, 2025), commentary by
  Anushree Verma, Senior Director Analyst: >40% of agentic AI projects
  predicted canceled by end of 2027.
```

## Cross-References

### Cross-reference verification notes
Before writing citations below,
`blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md`,
`blog-thoughtworks-karle-discovery-dilemma.md`,
`blog-thoughtworks-puthanveedu-choudhary-overenthusiasm-financial-services.md`,
`blog-thoughtworks-ryan-ai-shadow-it-paved-roads.md`, and
`blog-thoughtworks-lad-platform-business-value.md` were re-read directly
(MINER.md §4b) and the claim numbers cited below were confirmed against
each note's numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md` Claim 7
    ("Organizations that treat AI deployment as an internal experiment are
    already approaching it incorrectly; enterprises should stop funding
    isolated demos and instead build the underlying operational
    substrate"): This article's Claim 3 ("almost none of the resulting
    deployments survive contact with real customers") is an independent
    articulation of the same underlying skepticism toward demo-stage
    validation as sufficient proof of production readiness — two
    independent Thoughtworks-adjacent sources converge on distrusting the
    pilot/demo as a predictor of production survival.
  - `blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md` Claim 4
    ("Governance cannot be retrofitted onto an agent platform after
    deployment — it must be built into the operating environment's
    'original DNA'"): This article's Claim 6 (read-only pilots as a
    non-solution to action risk — "a brochure with a microphone") and
    Claim 7 (action-taking AI needs decades-old-channel-equivalent
    controls, "engineering, risk and governance... solved together") both
    treat avoiding or bolting-on governance as a non-solution, consistent
    with Marr/Mohanty's "original DNA" framing, though this article argues
    from product-value loss (a read-only channel is worthless) rather than
    governance-architecture failure.
  - `blog-thoughtworks-karle-discovery-dilemma.md` Claim 11 ("themes that
    had surfaced during the AI-assisted simulation reappeared in real user
    sessions without the team prompting for them"): This article's
    3-week prototype phase explicitly includes "Test with users" (Claim 9)
    as a required step before committing to the 3-month build-and-launch
    phase — both sources treat direct validation with real users as a
    required, non-skippable step distinct from AI-assisted simulation or
    internal confidence, though Karle's note demonstrates this at the
    concept-validation stage of product discovery and this article
    prescribes it at the working-prototype stage of a conversational
    channel specifically.
  - `blog-thoughtworks-puthanveedu-choudhary-overenthusiasm-financial-services.md`
    Claim 2 (leaders should ask whether they'd "stake your institution's
    reputation on it, not in a demo, but in a downturn"): Both sources
    treat demo-stage or pilot-stage success as an insufficient bar for a
    real deployment decision — Puthanveedu & Choudhary frame this as a
    financial-services capital-allocation question; this article frames it
    as a conversational-channel production-readiness question. Independent
    convergence across two different Thoughtworks-adjacent essays,
    published roughly two and a half weeks apart, strengthens confidence
    that "survives a demo" is being treated across the corpus as
    categorically distinct from "survives production."

- **Contradicts**: None identified against the cross-referenced notes above.
  Worth naming a framing tension rather than a contradiction: this
  article's Claim 7 explicitly agrees that a CISO/regulator/general
  counsel is "right" to withhold default sign-off on action-taking AI,
  which sits in tension in *emphasis* (not in stated fact) with
  `blog-thoughtworks-ryan-ai-shadow-it-paved-roads.md`'s overall argument
  that organizations should shift "from a posture of gatekeeping to one of
  enablement" for AI tooling generally. The two are not a factual
  contradiction — Ryan's article is about internal employee tooling
  (shadow IT), this article is about customer-facing, transaction-capable
  channels — and Ryan's own Claim 7 already carves out an exception for
  irreducible legal/financial/security constraints, which is exactly the
  category this article's trust-boundary problem falls into. No
  contradiction issue filed per MINER.md §4a's "differ only in context"
  exclusion.

- **Extends**:
  - `blog-thoughtworks-lad-platform-business-value.md` Claim 5 (new
    platform teams inherit an OPEX cost model but costs actually increase
    during build/migration, reading as failure without a reframed
    narrative) and Claim 6 (leaders must shift the funding narrative from
    OPEX to CAPEX): This article's 3/3/3 motion (Claim 9) is a concrete,
    time-boxed delivery mechanism for exactly the kind of
    evidence-before-commitment approach Lad's article argues is needed to
    win CFO-legible funding — Lad supplies the *financial narrative* for
    justifying platform/channel investment; this article supplies the
    *staged delivery methodology* that produces the evidence (a business
    case "grounded in evidence" after the 3-week prototype phase) that
    narrative would need to point to.
  - `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 9 ("provenance
    has to shape the entire system, not get added at the end"): This
    article's Claim 8 (hallucination must be made "structurally
    impossible" for high-stakes answers, requiring the AI-to-systems-of-record
    relationship to be rethought) names the same class of requirement at a
    higher level of abstraction, without describing Kepler's specific
    worked mechanism (a deterministic execution layer separating reasoning
    from computation). Read together: this article states the *what*
    (certifiability is required, not optional, for customer-facing
    answers); Kepler's case study is a candidate worked *how* for one
    industry's version of the same requirement.

- **Novel**:
  - **The "customer conversation has moved, not the traffic numbers" framing**
    (Claim 1): No prior corpus source frames the third-party-AI-adoption risk
    specifically as customers pre-empting a company's own channels during
    the decision-making phase of a purchase or service interaction, while
    conventional channel-traffic metrics look unchanged.
  - **The named "3/3/3" delivery motion itself** (Claim 9, Concrete
    Artifacts): No other source note in this corpus documents a specific,
    named, time-boxed (3 days / 3 weeks / 3 months) methodology for taking
    a conversational-AI product from concept to a production minimum
    lovable product. This is a directly reusable, citable framework
    distinct from the general "iterate and validate" advice found
    elsewhere in the corpus.
  - **The three-problem decomposition of conversational-channel readiness
    (speed / trust boundary / certifiability) as a named, paired
    framework** (Claims 4, 6, 8): While each individual concern (latency,
    action-risk governance, hallucination) appears separately elsewhere in
    this corpus, no prior source names all three together as the specific,
    jointly-necessary conditions for a conversational AI channel to
    "carry the weight of a real business interaction."
  - **The Gartner 40%-agentic-project-cancellation statistic, tied
    specifically to model-routing cost economics as the causal mechanism**
    (Claim 5): This corpus has other sources discussing agentic-AI
    cost/routing tradeoffs and other sources discussing AI-project failure
    generally, but this is the first source in the corpus to connect this
    specific Gartner statistic to the specific mechanism of routing every
    reply through the heaviest available model.

## Guide Impact

- **Chapter 05 (Team Adoption — Delivery Methodology / Use-Case
  Validation)**: Add the 3/3/3 delivery motion (Claim 9, Concrete
  Artifacts) as a named, time-boxed staged-validation framework for
  customer-facing conversational AI products specifically, positioned
  alongside the corpus's existing product-discovery methodology
  (`blog-thoughtworks-karle-discovery-dilemma.md`) and platform-funding
  narrative guidance (`blog-thoughtworks-lad-platform-business-value.md`).
  Recommend flagging explicitly that no named client outcome or timeline
  data validates this specific cadence in the source article — it should
  be presented as a proposed framework, not a proven result.

- **Chapter 03 (Verification) or Chapter 05 (Production Readiness)**: Add
  the three-problem decomposition (speed, trust boundary, certifiability —
  Claims 4, 6, 8, Concrete Artifacts) as a named readiness checklist for
  any chapter section on what distinguishes a production-ready customer
  conversational AI channel from a demo. Pair Claim 8's "hallucination must
  be structurally impossible for high-stakes answers" requirement with
  `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 9 for a source
  that supplies a concrete worked mechanism, since this article names the
  requirement without describing how to achieve it.

- **Chapter 01 (Landscape) or Chapter 05 (Team Adoption)**: Add the
  Gartner 40%-agentic-project-cancellation statistic and the "many use
  cases positioned as agentic today don't require agentic implementations"
  quote (Claim 5) as a citable data point for discussions of
  over-applying agentic architecture, tied specifically here to
  routing-cost economics as one concrete cause — a more specific mechanism
  than a bare citation of the cancellation statistic alone would provide.

## Extraction Notes

1. **Full article text obtained via WebFetch on the first pass.** Unlike
   several other Thoughtworks-sourced notes in this corpus that required
   multiple targeted WebFetch passes or a direct `curl` HTML fetch to get
   quote-accurate text (see Extraction Notes in
   `blog-thoughtworks-ryan-ai-shadow-it-paved-roads.md` and
   `blog-thoughtworks-lad-platform-business-value.md`), a single WebFetch
   request explicitly asking for full verbatim text returned the complete
   article body (author byline, publication date, TL;DR callout, all
   section headings, all body paragraphs, the Gartner pull-quote, and the
   full "Sources and further reading" citation block) in one pass. All
   quotes in this note were copied character-for-character from that
   returned text. The Assayer should still spot-check the highest-value
   quotes (Claims 1, 3, 4, 5, 6, 8, 9) against the live URL, since the
   fetched text is not independently preserved outside this session.
2. **No substantive linked sub-pages to follow.** The fetched article text
   contains no inline hyperlinks to other Thoughtworks articles, Technology
   Radar entries, or external pages beyond the three citations named in the
   closing "Sources and further reading" block (a Gartner press release and
   two news-outlet articles reporting OpenAI usage figures). Those three
   citations are cited-but-not-independently-fetched external reports, not
   Thoughtworks sub-pages; per MINER.md §1 guidance to follow "linked
   pages," none were available to follow within the Thoughtworks site
   itself.
3. **No quantitative outcome data for the article's own central
   recommendation.** The 3/3/3 methodology (Claim 9) and the AI/works
   platform claim (Claim 10) are both presented without a named client
   engagement, timeline, or outcome metric — no organization is named as
   having actually run this cadence and achieved a business result. This
   caps the overall confidence rating at "anecdotal": every individual
   claim in the article is either a single-author framing/prescription with
   no cited data, or (Claims 2 and 5) a genuinely externally-attributed
   statistic used to support a broader, unsourced architectural or
   behavioral assertion. The externally-attributed statistics themselves
   are rated "emerging" individually, but they do not carry enough weight
   across the article's overall argument (which rests primarily on the
   author's own framework and prescriptions) to raise the note's overall
   rating above "anecdotal."
4. **No contradictions filed.** Cross-referenced against
   `blog-thoughtworks-marr-autonomous-ai-enterprise-readiness.md`,
   `blog-thoughtworks-karle-discovery-dilemma.md`,
   `blog-thoughtworks-puthanveedu-choudhary-overenthusiasm-financial-services.md`,
   `blog-thoughtworks-ryan-ai-shadow-it-paved-roads.md`, and
   `blog-thoughtworks-lad-platform-business-value.md` — found strong
   corroboration and extension relationships (see Cross-References) and one
   framing-emphasis tension with Ryan's enablement-over-gatekeeping
   argument, which does not rise to a factual contradiction (see
   Cross-References → Contradicts) and was not filed as an issue.
5. **Vendor self-reference flagged.** Claim 10 (the AI/works™ platform
   claim) is Thoughtworks citing its own commercial product as the enabler
   of the methodology the article recommends. This is noted explicitly in
   the claim's "Our assessment" so the guide does not conflate the 3/3/3
   *methodology* (a reusable framework, Claim 9) with an implicit
   endorsement of a specific commercial platform as the only way to achieve
   it.
