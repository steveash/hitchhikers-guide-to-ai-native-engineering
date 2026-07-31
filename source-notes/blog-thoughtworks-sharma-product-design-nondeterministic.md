---
source_url: https://www.thoughtworks.com/insights/blog/experience-design/Product-design-in-the-age-of-AI-Designing-non-deterministic-systems
source_type: blog-post
title: "Product design in the age of AI: Designing non-deterministic systems"
author: Abhishek Sharma (Thoughtworks)
date_published: 2026-07-21
date_extracted: 2026-07-31
last_checked: 2026-07-31
status: current
confidence_overall: emerging
issue: "#2362"
---

# Product design in the age of AI: Designing non-deterministic systems

> A Thoughtworks experience designer argues that AI compresses design's
> execution layer (wireframes, screens, prototypes) but not its judgment
> layer, and that the resulting shift moves product designers from
> "designing fixed interfaces" to defining how AI agents make decisions,
> communicate uncertainty, escalate to humans, and build trust — with a
> concrete AI-automation-vs-human-ownership division of labor.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, "Experience design" / "AI and
  ML" categories, published July 21, 2026)
- **Author credibility**: Abhishek Sharma, whose Thoughtworks profile lists
  his title as "Experience Designer" and self-describes as "a design and
  product strategist specializing in architecting scalable, intuitive
  digital experiences across SaaS, enterprise software, supply chain and
  financial domains," working "at the intersection of business viability
  and technical feasibility" with cross-functional product and engineering
  teams. His profile also states he is "deeply focused on the intersection
  of human design and algorithmic collaboration, leveraging designer-centric
  AI to accelerate product discovery, optimize systemic workflows, and
  de-risk complex design decisions." This is a practitioner's synthesis and
  argument piece, not a reported case study — no named client engagement,
  no usage metrics, and no controlled comparison of designer output
  before/after AI adoption are given. The piece carries a standard
  Thoughtworks disclaimer that its opinions are the author's own and don't
  necessarily reflect Thoughtworks' position.
- **Scope**: Covers why screen-count-based design estimation breaks down as
  AI compresses execution time; what does and doesn't compress in the
  design process; a shift in the shape of design briefs toward
  non-deterministic, agentic systems; four new "architectural" design
  question categories (context engineering, managing uncertainty, human
  oversight, trust mechanisms); a table dividing AI-automated work from
  human/designer-owned work; new proposed measurement focus (user
  confidence, intervention rates, override frequency); and four skill
  pillars for human-AI design collaboration. Does NOT cover: any named
  product, tool, or vendor other than passing references to Claude AI and
  v0.dev in the opening anecdote; metrics from a real deployed product; how
  to actually implement the four architectural design categories in a
  design tool or process; or organizational/team-structure change
  management.

## Extracted Claims

### Claim 1: AI compresses design's execution layer, but enterprise-grade design requirements (accessibility, responsive behavior, design systems, usability validation) still require human expertise — the practice shifts toward systems thinking, algorithmic collaboration, and managing non-determinism
- **Evidence**: Author's opening thesis statement, answering the article's
  framing question ("Is my role still relevant?").
- **Confidence**: emerging (a reasoned practitioner thesis, not measured
  against a controlled before/after study)
- **Quote**: "While AI dramatically compresses the execution layer of
  design, enterprise requirements such as accessibility, responsive
  behavior, design systems and usability validation still require human
  expertise. AI accelerates these tasks, but it does not replace the
  necessity for them. What remains is a shift toward deep systems thinking,
  algorithmic collaboration and managing non-deterministic systems."
- **Our assessment**: This is the article's thesis sentence and everything
  else in the piece elaborates on it. The claim is plausible and consistent
  with the broader corpus pattern of "AI compresses execution, judgment
  moves upstream" (see Cross-References), but it is asserted rather than
  demonstrated — no example is given of an AI-generated interface that
  actually failed an accessibility or usability validation check, which
  would have made the "still require human expertise" claim concrete rather
  than assumed.

### Claim 2: Screen-count-based design estimation is broken because AI can generate a full screen set for a typical redesign (e.g., 12 screens) in under 20 minutes, compressing what used to take weeks into hours — but this speed increases the risk of inconsistent code and mounting cognitive debt absent clear guidance
- **Evidence**: Concrete illustrative example (a "typical SaaS onboarding
  redesign" of 12 screens, 3 user journeys, 4 sprints) contrasted with
  AI-tool generation speed.
- **Confidence**: anecdotal (the "12 screens," "20 minutes," and "weeks to
  hours" figures are illustrative round numbers, not measured from a
  specific project or tool benchmark)
- **Quote**: "AI tools can generate those 12 screens in under 20 minutes. A
  developer using modern generative platforms can technically produce a
  working React prototype before the discovery workshop is scheduled,
  though these typically require substantial refinement before being
  production-ready. The execution layer — the part that used to take weeks
  — is compressing into hours. While this accelerates delivery, it also
  increases the risk of inconsistent code and mounting cognitive debt if
  teams don't provide clear guidance."
- **Our assessment**: The "substantial refinement before being
  production-ready" and "risk of inconsistent code and mounting cognitive
  debt" qualifiers are the most useful part of this claim for the guide —
  they push back against a naive "AI ships the screens, so design work is
  done" reading, which corroborates the corpus's existing comprehension/
  intent-debt material (see Cross-References). No source is cited for the
  20-minute figure; treat it as illustrative, not measured.

### Claim 3: What doesn't compress under AI acceleration is the contextual understanding of why a given set of screens needs to exist — e.g., recognizing that a "simple onboarding flow" is failing because the product's mental model doesn't match how the user (an operations manager juggling legacy spreadsheets) actually thinks about their job
- **Evidence**: Concrete illustrative example contrasting UI-level failure
  diagnosis with mental-model-level failure diagnosis.
- **Confidence**: anecdotal (illustrative, non-sourced example; not drawn
  from a named client engagement)
- **Quote**: "But here is what does not compress: understanding why those 12
  screens need to exist in the first place. Understanding that your B2B
  SaaS users are operations managers who switch between your product and
  three legacy Excel sheets simultaneously. Understanding that the \"simple
  onboarding flow\" is failing not because of poor UI, but because the
  mental model in the product does not match how the user thinks about
  their job."
- **Our assessment**: This is a specific, reusable diagnostic frame — "is
  this a UI failure or a mental-model failure?" — for distinguishing tasks
  AI execution speed can help with from tasks it can't. It's stated as
  general design wisdom rather than derived from AI specifically, but the
  article's point is that AI's execution speed makes it easy to skip this
  diagnostic step entirely (ship fast, skip the "why"), which raises its
  stakes rather than eliminating its need.

### Claim 4: Design briefs for AI-driven products are qualitatively different from traditional interface-redesign briefs — e.g., "design the experience" for an autonomous Slack procurement-approval agent, instead of "redesign the dashboard"
- **Evidence**: Direct before/after contrast of brief phrasing.
- **Confidence**: anecdotal (a single illustrative example brief, not a
  survey of actual client briefs)
- **Quote**: "The projects landing on product designers' desks today look
  fundamentally different from those of the past. Instead of \"Redesign the
  dashboard,\" the cross-functional brief now reads: \"We are building an
  autonomous AI agent that handles procurement approvals via Slack. Design
  the experience.\""
- **Our assessment**: This is the concrete, memorable example the rest of
  the article's argument hangs on (the Prospector's triage comments flagged
  this "Slack procurement agent" example specifically). It's a plausible
  and illustrative brief, but it is presented as a representative example
  rather than an actual client project the author worked on, so we treat it
  as an illustrative device, not evidence of a documented trend.

### Claim 5: Traditional UX assumptions fail for probabilistic (LLM-based) systems because designers can no longer map fixed paths — they must instead account for variable outputs and ensure the application stays coherent regardless of the specific machine-generated response
- **Evidence**: Author's structural argument, stated as the reason the
  brief in Claim 4 requires a different design approach.
- **Confidence**: emerging (a widely-echoed structural premise in
  discussions of non-deterministic system design, not a novel claim by this
  author, but not independently measured here either)
- **Quote**: "Traditional UX assumptions often fail in these environments
  because LLMs are probabilistic rather than deterministic. Designers can
  no longer map fixed paths; they must account for variable outputs and
  ensure the application remains coherent regardless of the specific
  machine-generated response."
- **Our assessment**: This directly corroborates the corpus's existing
  engineering-side treatment of non-determinism (see Cross-References) but
  applies it specifically to UX/interaction design rather than to backend
  evaluation or performance architecture — a genuinely different angle on
  the same underlying system property.

### Claim 6: The designer's role shifts from designing fixed interfaces to defining how AI agents make decisions, communicate uncertainty, and collaborate with people — a "much harder, architectural set of questions" than traditional interface design
- **Evidence**: Author's structural framing, followed by four named
  question categories (context engineering, managing uncertainty, human
  oversight, trust mechanisms — see Concrete Artifacts for the verbatim
  definitions).
- **Confidence**: emerging (a structural/normative claim about how the role
  should evolve, not a report of an already-completed shift)
- **Quote**: "That changes the designer's role fundamentally. Instead of
  designing fixed interfaces, they increasingly define how AI agents make
  decisions, communicate uncertainty and collaborate with people."
- **Our assessment**: This is the article's central role-redefinition claim.
  It's a reasonable synthesis but reads as aspirational/normative ("the
  designer must answer...") rather than descriptive of a widely observed
  practice — no data is given on what fraction of design teams have
  actually adopted this framing versus still operating on the traditional
  interface-design model.

### Claim 7: A worked example — an AI customer-support agent handling refund requests — shows the practical effect of the role shift: less time on chat-screen visuals, more time defining handoff criteria, confidence thresholds, fallback messaging, and feedback mechanisms, because experience quality is determined by AI behavior in success, failure, and uncertainty, not by the interface alone
- **Evidence**: Concrete illustrative example applying Claim 6's abstract
  argument to a specific product scenario.
- **Confidence**: anecdotal (illustrative example, not a documented project)
- **Quote**: "Consider an AI customer support agent handling refund
  requests. A designer spends less time creating chat screens and more time
  defining handoff criteria, confidence thresholds, fallback messaging and
  feedback mechanisms. The interface matters, but the quality of the
  experience is determined by how the AI behaves when it succeeds, fails or
  encounters uncertainty."
- **Our assessment**: This is the article's most concrete "before/after
  time allocation" example and is useful precisely because it names
  specific design artifacts (handoff criteria, confidence thresholds,
  fallback messaging, feedback mechanisms) rather than staying at the level
  of abstract principle. Still illustrative rather than measured — no time-
  allocation study backs the "spends less time / more time" framing.

### Claim 8: The design surface now extends beyond interfaces to include an AI's responses, language, trust posture, and decision-making — designers increasingly define an AI's goals, escalation paths, and guardrails alongside its interface
- **Evidence**: Author's summary statement generalizing Claim 6/7's
  examples into a broader definition of what "design surface" now means.
- **Confidence**: emerging (definitional/normative framing, not measured)
- **Quote**: "The design surface now extends beyond interfaces to include
  responses, language, trust and decision-making. Designers increasingly
  define an AI's goals, escalation paths and guardrails alongside its
  interface."
- **Our assessment**: This is a compact, quotable expansion of "what is a
  design surface" that generalizes well beyond product design specifically
  — it argues that goals, escalation paths, and guardrails (traditionally
  engineering or product-management concerns) are now also design
  concerns. Useful as a boundary-redrawing claim, but the article gives no
  account of how this responsibility gets negotiated against engineering or
  PM ownership of the same artifacts in practice.

### Claim 9: AI automates rapid wireframing, dynamic component generation, usability heuristic checks, session-recording/A-B-test analysis, initial documentation/copy drafts, and code/prototype generation; humans retain problem framing, business strategy, ethical guardrails, cross-functional negotiation, the final ship/no-ship judgment call, and defining user outcomes and success criteria
- **Evidence**: A two-column table ("AI Automation Layer" vs. "Human/
  Designer Ownership Layer") presented as the article's explicit division
  of labor (see Concrete Artifacts for the full table).
- **Confidence**: emerging (a clean, internally consistent taxonomy;
  presented as prescriptive guidance rather than derived from a measured
  study of where AI actually succeeds or fails on each row)
- **Quote**: (no direct quote; see Concrete Artifacts for the extracted
  table — the table itself, not a prose sentence, is the citable artifact)
- **Our assessment**: This table is the single most reusable, checklist-style
  artifact in the article — a practitioner or manager could use it directly
  to scope a designer's role on an AI-product team. The main limitation is
  that several rows blur under scrutiny (e.g., "Initial documentation and
  copy drafts" as AI-owned vs. "Defining user outcomes and success
  criteria" as human-owned — drafting is AI's, but reviewing/editing those
  drafts for correctness plausibly belongs on the human side too, and the
  table doesn't address review/editing as a separate activity).

### Claim 10: Measuring AI-driven product experiences requires new metrics — user confidence, intervention rates, and frequency of manual overrides — to gauge systemic health, rather than (or in addition to) traditional interface-usage metrics
- **Evidence**: Author's statement introducing a new measurement focus,
  positioned alongside the division-of-labor table.
- **Confidence**: anecdotal (three metric names given with no definitions,
  target ranges, or worked measurement example)
- **Quote**: "Measuring these AI experiences also requires new metrics,
  shifting focus toward user confidence, intervention rates and the
  frequency of manual overrides to gauge systemic health."
- **Our assessment**: This is asserted as a single sentence with no
  elaboration — no definition of how "user confidence" would actually be
  measured (survey? behavioral proxy?), what counts as an "intervention,"
  or what an acceptable override rate looks like. It's a useful pointer
  toward a metrics gap (traditional UX metrics like task completion rate or
  time-on-task don't capture AI-specific failure modes) but is thin enough
  that the guide should present it as a direction to investigate, not a
  ready-to-use metrics framework.

### Claim 11: Designing AI systems is a continuous, ongoing collaboration across user experience, model behavior, technical architecture, and governance — not a sequential product-to-design-to-engineering handoff
- **Evidence**: Author's structural claim, illustrated by extending the
  procurement-approval-agent example (Claim 4) to show the designer
  defining what information the agent needs, how it communicates
  uncertainty, when it needs human intervention, and how users can correct
  or override it.
- **Confidence**: emerging (a structural/normative claim about how
  cross-functional collaboration should work, not a report of measured
  team-process change)
- **Quote**: "Designing AI systems is no longer a sequential handoff
  between product, design and engineering. It becomes a continuous
  collaboration where user experience, model behaviour, technical
  architecture and governance evolve together."
- **Our assessment**: This generalizes the earlier examples into a claim
  about team process, not just individual designer skill — it argues the
  waterfall-like product→design→engineering sequence itself breaks down for
  agentic products, requiring continuous cross-functional involvement
  instead. The article doesn't describe what mechanism (rituals, artifacts,
  meeting cadence) makes this "continuous collaboration" actually work in
  practice, so the claim stays at the level of stated principle.

### Claim 12: Effective human-AI design collaboration requires four skill pillars beyond interface design: systems thinking (design ecosystems, not individual screens), strategic influence (align technical possibilities with business outcomes), ethical reasoning (design for fairness, transparency, accountability), and context engineering (define the information and decision criteria that shape AI behavior)
- **Evidence**: A named, numbered four-pillar list under "Skills for
  effective human-AI collaboration" (see Concrete Artifacts).
- **Confidence**: emerging (a clean taxonomy; presented as prescriptive
  skill guidance, not validated against a skills survey or hiring-outcome
  data)
- **Quote**: (no direct quote; see Concrete Artifacts for the verbatim
  four-pillar list)
- **Our assessment**: "Context engineering" appears twice in the article —
  once as one of four architectural design-question categories (Claim 6)
  and again here as one of four human-AI-collaboration skill pillars — the
  author uses the same term for both the design question ("what information
  does the AI need") and the human skill of answering it, which is
  internally consistent but means the article doesn't distinguish a design
  *artifact* (the context spec) from the *capability* to produce it. Worth
  flagging for guide authors citing this term from this source.

### Claim 13: The transition will not be painless — designer demand shifts toward those who understand systems, human behavior, and responsible AI as the number of screens produced shrinks but the complexity of the problems being solved grows; the article frames this as an upgrade to the role rather than a threat to it
- **Evidence**: Author's closing synthesis statement.
- **Confidence**: emerging (thesis-level closing claim, consistent with but
  not independently proven by the rest of the article's content)
- **Quote**: "The transition will not be painless. As AI takes on more
  execution work, demand will increasingly shift toward designers who
  understand systems, human behavior and responsible AI. The number of
  screens may shrink, but the complexity of the problems being solved is
  growing.
  This is not a threat to the product designer. It is the cross-functional
  upgrade the role has always deserved."
- **Our assessment**: This closing claim explicitly names a real risk (the
  transition "will not be painless" — i.e., not every current product
  designer's skill set survives this shift unchanged) before pivoting to
  the optimistic framing. It's worth noting in the guide that the article's
  own acknowledgment of pain is a more honest note than the "cross-functional
  upgrade" framing that follows it — teams should read this as "some
  designers' current skill sets will not transfer," not merely as
  reassurance.

## Concrete Artifacts

### Four architectural design-question categories (verbatim, "Designing non-deterministic systems" section)
```
Source: "Product design in the age of AI: Designing non-deterministic
systems," Abhishek Sharma, Thoughtworks, 2026-07-21

Context engineering: Define the information, constraints and business
  rules an AI needs to make good decisions.
Managing uncertainty: Design how the AI agent explains uncertainty,
  limitations and failures.
Human oversight: Decide when the AI should escalate to people and what
  information accompanies that handoff.
Trust mechanisms: Design confidence indicators, citations, feedback loops
  and recovery paths that help users calibrate confidence in the system.
```

### AI Automation Layer vs. Human/Designer Ownership Layer (verbatim table)
```
Source: same article, "What AI automation handles, what the
cross-functional team owns" section

AI Automation Layer                      | Human/Designer Ownership Layer
------------------------------------------|--------------------------------
Rapid wireframing & layout variations     | Problem framing & root-cause
                                           | discovery
Dynamic component generation              | Business strategy &
                                           | value-stream alignment
Automated usability heuristic checks      | Ethical guardrails & bias
                                           | mitigation
Session recording & A/B test analysis     | Cross-functional negotiation &
                                           | team alignment
Initial documentation & copy drafts       | The final judgment call on
                                           | what ships
Code/prototype generation                 | Defining user outcomes and
                                           | success criteria
```

### Four skill pillars for effective human-AI collaboration (verbatim list)
```
Source: same article, "Skills for effective human-AI collaboration" section

1. Systems thinking: Design ecosystems instead of individual screens.
2. Strategic influence: Align technical possibilities with business
   outcomes.
3. Ethical reasoning: Design for fairness, transparency and
   accountability.
4. Context engineering: Define the information and decision criteria
   that shape AI behavior.
```

## Cross-References

- **Corroborates** `blog-anthropic-carta-healthcare-context-engineering.md`
  Claim 1 (Matthew Mazzanti: "context construction," not prompt wording, is
  the primary production accuracy lever) and Claim 2 (per-data-point runtime
  context scoping as the concrete engineering pattern): this article's
  "context engineering" design-question category (Claim 6 here, and
  Concrete Artifacts) applies the same underlying principle — that the
  information fed into an AI's decision matters more than surface-level
  polish — to the *design* discipline rather than the *engineering*
  discipline. Carta Healthcare shows what context engineering looks like in
  a production extraction pipeline; this article is the first corpus source
  to argue product designers themselves should own defining that context
  for agent-facing product experiences, not just engineers.
- **Corroborates** `blog-thoughtworks-anand-agent-evaluation-framework.md`
  Claim 2 (traditional software testing assumes deterministic behavior,
  which breaks down for LLM-based systems) and Claim 3 (deterministic vs.
  non-deterministic components require different evaluation approaches):
  this article's Claim 5 states the same deterministic/non-deterministic
  premise independently, applied to UX design assumptions ("designers can
  no longer map fixed paths") rather than to test/evaluation architecture.
  Read together, the two sources show the same system property (LLM
  non-determinism) driving parallel rethinks in two different disciplines —
  QA/evaluation and product design — that don't yet reference each other.
- **Corroborates** `blog-thoughtworks-singh-shaik-performance-engineering.md`
  Claim 1 (naive multi-agent designs fail via reliability degradation when
  unstructured outputs break downstream parsers) in spirit: this article's
  "ensure the application remains coherent regardless of the specific
  machine-generated response" (Claim 5 here) is the design-facing statement
  of the same coherence requirement that article addresses at the
  engineering/schema-validation level (its Claim 12, structured outputs as
  a contract). Neither article cites the other; both independently treat
  "the system must stay coherent even though the model's output varies" as
  a cross-cutting requirement that spans design and engineering.
- **Extends** `blog-anthropic-claude-design-product-designer-workflow.md`:
  that note documents a first-person account of a product designer's
  *tool-level* workflow with Claude Design (prompting patterns, brand-guideline
  distillation into prompts, generate-then-remix practices) for producing
  visual artifacts faster. This article does not discuss any specific
  design tool and instead argues at the *role-definition* level — what
  should a product designer be responsible for, once AI has compressed the
  tool-level execution work that the Claude Design note describes in
  detail. The two are complementary at different altitudes: the Claude
  Design note is the "how" of faster execution; this article is the "then
  what" of redefined designer responsibility once that execution is fast.
- **Extends** `blog-addyosmani-software-factories-light-dark.md` Claim 6 (a
  "lit" factory moves human judgment upstream to product, design, and
  architecture decisions before an agent starts a loop, because reviewing a
  200-line plan is cheaper than reviewing 2,000 lines of generated code):
  this article's division-of-labor table (Claim 9) and its "problem framing
  & root-cause discovery" / "the final judgment call on what ships" rows
  are the product-design-specific instantiation of the same "push judgment
  upstream, let automation handle downstream execution" principle Osmani
  states for code-generation pipelines. Different domains (design vs.
  code), same structural argument about where human judgment should sit
  relative to AI-automated execution.
- **Contradicts**: None found. No existing source note stakes out a
  position on product-design methodology, division of labor, or
  designer-role scope that this article's claims materially oppose.
- **Novel**:
  - **Product-design-discipline framing of non-determinism** — no existing
    corpus source addresses how UX/interaction design specifically (as
    opposed to engineering, evaluation, or performance) should change when
    the underlying system is probabilistic rather than deterministic
    (Claim 5, Claim 6).
  - **The four architectural design-question categories** (context
    engineering, managing uncertainty, human oversight, trust mechanisms) as
    a named checklist for designing agentic product experiences — new to
    the corpus (Claim 6, Concrete Artifacts).
  - **The AI-automation-vs-human-ownership division-of-labor table for
    product design specifically** (Claim 9) — the corpus has code-focused
    automation/ownership splits (e.g., the Osmani factory posts) but no
    prior design-discipline-specific version.
  - **Proposed AI-experience metrics** (user confidence, intervention
    rates, manual-override frequency) as a named alternative to traditional
    UX metrics for agentic products (Claim 10) — thin (one sentence, no
    definitions) but a novel pointer for the corpus.

## Guide Impact

- **Chapter 05 (UX and product management)**: The chapter currently lacks
  design-discipline-specific guidance for non-deterministic/agentic
  products. Add the four architectural design-question categories (Claim 6,
  Concrete Artifacts) as a concrete checklist for teams designing
  agent-facing experiences, and the AI-automation-vs-human-ownership table
  (Claim 9) as a starting point for scoping a designer's responsibilities on
  an AI-product team — flagging per Claim 9's assessment that the table's
  "documentation drafts vs. final judgment call" split leaves review/editing
  responsibility unaddressed.
- **Chapter 05**: Add the worked refund-agent example (Claim 7) as a
  concrete illustration of the time-allocation shift the chapter should
  describe: away from interface visuals, toward handoff criteria, confidence
  thresholds, fallback messaging, and feedback mechanisms — this is more
  concrete than the article's abstract role-redefinition claims (Claim 6,
  Claim 8) and easier for practitioners to apply directly.
- **Chapter 04 (Context Engineering)**: Cross-reference this article's
  design-facing "context engineering" question (Claim 6) against the
  chapter's existing engineering-facing treatment (sourced from Carta
  Healthcare and other notes) to show the same discipline applies to two
  different roles — flag the term's double use within this single article
  (design question category vs. designer skill pillar, per Claim 12's
  assessment) so the guide doesn't conflate a design *artifact* with a
  *capability* when citing "context engineering" from this source.
- **Chapter 05 / Chapter 06**: Note the proposed AI-experience metrics (user
  confidence, intervention rates, override frequency — Claim 10) as a
  direction worth investigating for observability/UX-measurement guidance,
  but flag it as unelaborated (one sentence, no definitions or worked
  measurement example) rather than a ready-to-adopt framework — pair with
  any more fully worked-out evaluation-metrics source before making it a
  guide recommendation.

## Extraction Notes

- Full article text was retrieved by fetching the raw page HTML directly
  (`curl` with a browser user-agent) and stripping tags with a Python
  stdlib pass (script/style removal, block-tag-to-newline conversion,
  HTML-unescape), not via a summarizing tool. All quotes above were copied
  verbatim from that locally-parsed plain-text extraction and cross-checked
  against the raw HTML. One correction from an initial WebFetch pass: the
  WebFetch summary rendered two article sentences ("AI can synthesise
  research, but recognizing which insights matter, and why, remains a
  distinctly human capability." and the closing "This is not a threat to
  the product designer...") as if they were pull-quotes in quotation marks;
  the raw HTML shows both are ordinary body-text sentences, not
  third-party quotes or specially marked callouts. They are quoted above
  only where they appear as the author's own contiguous prose (Claim 13),
  and the first sentence was folded into a paraphrase in Claim 1's context
  rather than presented as a special quotation.
- The author's job title and bio were confirmed by separately fetching his
  Thoughtworks profile page (`https://www.thoughtworks.com/profiles/a/Abhishek-Sharma`,
  linked from the article's embedded structured-data `author` field) and
  reading the embedded `jobTitle`/`description` fields — not visible as
  on-page body text on the article itself.
- The article is short (~1,000 words) and self-contained, with no inline
  citations, footnotes, or in-body links to other substantive pages. The
  only outbound links are three unrelated "More insights" related-article
  teasers at the page bottom (on ephemerality/materiality, modularity, and
  non-functional requirements as an AI-code guardrail) — none bear on this
  article's design-methodology claims, and none were followed as sub-pages
  per MINER.md §1's "seems substantive" bar.
- Three Prospector triage comments were filed on the issue, proposing
  overlapping but not identical chapter sets (Ch02/05/06/07; Ch02/03/05/07;
  Ch03/04/02) and overlap candidates (`blog-anthropic-claude-design-product-designer-workflow.md`,
  `blog-addyosmani-software-factories-light-dark.md`,
  `blog-anthropic-carta-healthcare-context-engineering.md`,
  `blog-thoughtworks-anand-agent-evaluation-framework.md`,
  `blog-thoughtworks-singh-shaik-performance-engineering.md`,
  `docs-ghaw-deterministic-agentic-patterns.md`). All named overlap
  candidates except `docs-ghaw-deterministic-agentic-patterns.md` were read
  in full and cross-referenced above; `docs-ghaw-deterministic-agentic-patterns.md`
  was not cross-referenced because on inspection it documents gh-aw
  workflow-file patterns for deterministic vs. agentic *CI/CD* steps, which
  does not substantively overlap with this article's product-design-role
  claims (consistent with the second triage comment's own caveat that this
  gh-aw note "covers CI/CD architecture, not product UX design"). Guide
  Impact above is scoped to Ch04/Ch05/Ch06, the chapters where this
  article's claims concretely apply, rather than the full union of all
  three comments' chapter guesses.
- No contradiction with any existing source note was identified during
  cross-referencing; none filed per MINER.md §4a.
- Confidence set to `emerging` overall: this is a single practitioner's
  argument/synthesis piece with concrete, well-formed taxonomies (the
  four-category design-question list, the automation/ownership table, the
  four skill pillars) but no case study, client-engagement data, usage
  metric, or controlled comparison behind any individual claim — several
  claims are marked `anecdotal` within their own entries where they rest on
  a single illustrative (non-sourced) example rather than a stated
  principle.
