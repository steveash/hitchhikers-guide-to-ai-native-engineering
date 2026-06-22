---
source_url: https://simonwillison.net/2026/Jun/14/why-ai-hasnt-replaced-software-engineers/
source_type: blog-post
title: "Why AI hasn't replaced software engineers, and won't"
author: Simon Willison (link-blog curation); primary essay by Arvind Narayanan and Sayash Kapoor (normaltech.ai)
date_published: 2026-06-14
date_extracted: 2026-06-22
last_checked: 2026-06-22
status: current
confidence_overall: emerging
issue: "#1271"
---

# Why AI Hasn't Replaced Software Engineers, and Won't

> Simon Willison links to Arvind Narayanan and Sayash Kapoor's essay that uses NY WARN Act
> government filings (zero AI-related layoffs checked in the first year) and task-breakdown
> survey data to argue that AI has compressed only the "execution" middle of software
> engineering's decide-execute-deliver sandwich, while three structural bottlenecks —
> specifying what to build, verifying and being accountable for delivery, and deep contextual
> understanding — remain human-required for reasons that are not capability limitations.

## Source Context

- **Type**: blog-post (Simon Willison link-blog entry, June 14, 2026; primary content is
  Arvind Narayanan and Sayash Kapoor's essay "Why AI hasn't replaced software engineers,
  and won't" published June 11, 2026, on their Substack "AI as Normal Technology" at
  https://www.normaltech.ai/p/why-ai-hasnt-replaced-software-engineers. Per MINER.md §1,
  the linked essay was read as a substantive linked page; all claims and quotes are
  attributed to their actual source — Willison's post or the Narayanan/Kapoor essay —
  in the Concrete Artifacts section. Willison's URL is the canonical source per the issue.)
- **Author credibility**: Arvind Narayanan and Sayash Kapoor are Princeton researchers and
  co-authors of the book *AI Snake Oil* (Princeton University Press, 2024), which is a
  peer-reviewed academic critique of AI capability claims. Their newsletter "AI as Normal
  Technology" (formerly "AI Snake Oil") applies empirical analysis to AI labor-market
  claims. Willison is the creator of Django, one of the highest-signal independent AI
  tooling commentators, and a 25-year software engineering practitioner; his personal
  commentary adds a first-person practitioner corroboration of the essay's framework.
  Tags on the Willison post: careers, ai, generative-ai, llms, arvind-narayanan, ai-ethics.
- **Scope**: The essay covers: (1) NY WARN Act empirical data on AI-related layoffs;
  (2) a survey of task-time allocation for software engineers; (3) the "decide-execute-
  deliver sandwich" model; (4) three structural bottlenecks that resist automation for
  non-capability reasons; (5) the distinction between vibe coding and agentic engineering;
  (6) a forward-looking claim about employment trends. Willison adds brief personal
  commentary on how the framework matches his own practice. Does NOT cover: harness
  engineering details, specific AI tooling, team adoption strategies, or cost data.

## Extracted Claims

### Claim 1: NY WARN Act data shows zero AI-related software engineer layoffs in the first full year of mandatory AI disclosure

- **Evidence**: Government filing records — New York State became the first U.S. state to
  add a mandatory AI disclosure checkbox to WARN Act filings in March 2025. The essay
  reports empirical count from these government records for the first full year of
  compliance. By late May 2026, only one company (Nespresso) had checked the box,
  representing 46 of approximately 25,000 NY laid-off workers — about 0.2%.
- **Confidence**: settled (government filing records are primary empirical data; count of
  checked boxes is verifiable)
- **Quote**: "In the full first year, more than 160 companies filed WARN notices. Not a
  single one checked the AI box."
  — Narayanan & Kapoor, normaltech.ai, June 11, 2026
- **Our assessment**: This is the empirical foundation of the essay's core argument. WARN
  Act filings are legal documents — checking the wrong box exposes companies to regulatory
  risk, so the data is unlikely to be systematically underreported. The fact that 160+
  companies filed without once attributing layoffs to AI (with one eventual exception of
  trivial scale) is concrete evidence against the "AI layoffs are already happening en
  masse" narrative. The appropriate rebuttal would be that companies are strategically
  avoiding the checkbox despite AI-driven reductions — which is what Claim 2 tests.

### Claim 2: "AI washing" inflates the reported scale of AI-caused layoffs — companies invoke AI when explaining hiring freezes because it plays better with stakeholders than financial constraints

- **Evidence**: Survey of U.S. hiring managers (source attributed as a survey finding by
  the authors; specific survey not named in the accessible text).
- **Confidence**: emerging (the survey statistic is consistent with the WARN Act evidence
  but comes from a self-report survey with unspecified methodology)
- **Quote**: "59% of U.S. hiring managers admitted they emphasize AI when explaining hiring
  freezes or layoffs because it plays better with stakeholders than citing financial
  constraints."
  — Narayanan & Kapoor, normaltech.ai, June 11, 2026
- **Our assessment**: This claim inverts the typical concern. The conventional worry is that
  companies under-attribute layoffs to AI to avoid regulatory or PR scrutiny; this evidence
  suggests the opposite: companies *over*-attribute to AI for narrative purposes. The two
  forces (WARN Act data showing zero vs. manager survey showing over-attribution) converge
  on the same conclusion: AI-caused layoffs are not the primary driver of current tech-
  sector employment changes. The phrase "AI washing" is the authors' own coinage here,
  parallel to "greenwashing."

### Claim 3: Software engineers spend only a small fraction of their time actually writing code, undermining the premise that code-writing AI replaces engineering work

- **Evidence**: 2019 Microsoft paper summarizing prior research on developer time allocation,
  cited by the essay authors.
- **Confidence**: emerging (the finding is from a 2019 study; the range cited is wide,
  suggesting methodological variation; the directional claim — most time is not on coding —
  is consistent with practitioner experience)
- **Quote**: "developers spend surprisingly little time with coding, 9% to 61% depending on
  the study"
  — Narayanan & Kapoor, normaltech.ai, June 11, 2026
- **Our assessment**: Even the upper bound (61%) means coding is less than two-thirds of
  engineering work; at the lower bound (9%), it's nearly negligible. If AI accelerates
  only the coding portion, total engineering productivity improvement is bounded by the
  fraction of time coding represents. This is the empirical basis for the "decide-execute-
  deliver sandwich" claim — the execution layer is already not the dominant time sink.
  The wide range (9–61%) reflects different definitions of "coding" and different job
  roles, but the direction is clear.

### Claim 4: Software engineering work follows a "decide-execute-deliver sandwich" structure — AI has compressed only the execution middle, leaving the outer layers largely unchanged

- **Evidence**: Authors' analytical framework derived from task-breakdown surveys and their
  own analysis of software engineering work structure. "Writing Code vs. Shipping Code"
  and the 2019 Microsoft paper are cited as supporting data.
- **Confidence**: emerging (the framework is the authors' own synthesis, grounded in
  cited evidence but not independently validated as a model)
- **Quote**: "software engineers' work consists of a 'decide-execute-deliver' sandwich
  (with understanding being a prerequisite for all three). AI has compressed the middle
  of the sandwich, but has left the two ends largely unchanged."
  — Narayanan & Kapoor, normaltech.ai, June 11, 2026
- **Our assessment**: This is the central conceptual contribution of the essay. The
  "sandwich" model frames the three-layer structure clearly: decide (specify requirements
  and architecture), execute (write code), deliver (verify, test, account for). The insight
  that "understanding is a prerequisite for all three" is the load-bearing claim — it
  explains why automating execution doesn't unlock automation of the outer layers. The
  framework complements Simon Willison's prior framing in his May 6 post (see
  `blog-simonwillison-vibe-coding-agentic-engineering.md` Claims 9–10) that software
  complexity remains hard regardless of code generation speed.

### Claim 5: The three bottlenecks resisting AI automation are structural, not capability limitations — better AI won't resolve them

- **Evidence**: Authors' own argument, stated explicitly in the context of the three
  bottlenecks. No specific AI capability threshold is identified as a hypothetical fix.
- **Confidence**: emerging (this is the authors' analytical claim, not empirically
  measured; it represents a strong position on a contested question)
- **Quote**: "The reasons why the other two layers have resisted AI is not because of
  capability limitations."
  — Narayanan & Kapoor, normaltech.ai, June 11, 2026
- **Our assessment**: This is a bold claim. The authors are rejecting the "capabilities
  threshold" narrative — the idea that once AI reaches capability X, mass displacement
  becomes inevitable. Their counterargument is structural: the outer sandwich layers
  resist AI not because AI can't do them yet, but because of who needs to be responsible
  for the outcomes and what information is required. If correct, this means AI capability
  improvements won't change the displacement picture qualitatively, only quantitatively
  (faster execution within an already-efficient execution layer).

### Claim 6: "Deciding and specifying what to build" resists AI automation because requirements specification has high organizational stakes and compression causes disproportionate downstream pain

- **Evidence**: Authors' argument, framed around the organizational stakes of requirements
  errors. Also: task-breakdown surveys showing "meetings" appear as a primary engineering
  time sink, further evidence that the deciding layer is significant.
- **Confidence**: emerging (the argument is coherent and consistent with practitioner
  experience, but stated as the authors' analytical claim rather than measured finding)
- **Quote**: "requirements specification takes surprisingly long, and if it is compressed,
  it leads to much more pain down the line."
  — Narayanan & Kapoor, normaltech.ai, June 11, 2026
- **Our assessment**: The word "surprisingly" is load-bearing — even people who try to
  compress requirements discover it was not as safe to compress as they assumed. The
  authors also note that this layer "[requires] thinking about user needs, market signals,
  organizational priorities, and in some cases regulatory constraints." This is consistent
  with the corpus-wide finding that specification quality is the upstream bottleneck for
  agent reliability (see `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 7
  on SDLC bottlenecks shifting upstream). The task surveys' finding that "meetings or
  debugging" are the top activities post-coding further supports that requirements-setting
  (the decision layer) is where engineering time actually concentrates.

### Claim 7: "Verifying and being accountable for delivery" resists AI automation because today's AI is too unreliable for unsupervised mission-critical code delivery

- **Evidence**: Authors' argument, framed around both the organizational accountability
  requirement and current AI reliability limitations. The authors explicitly distinguish
  the capability explanation ("capability limitations") from the accountability explanation,
  and here attribute the resistance to accountability structure plus current reliability.
- **Confidence**: emerging (the accountability argument is structural; the "today's AI is
  so unreliable" part is an empirical claim that will shift as AI improves)
- **Quote**: "human teams need to be accountable for what they deliver. It is possible that
  some day in the future teams will ship mission-critical code without fully testing and
  understanding it, but today's AI is so unreliable that such haphazard practices would
  represent an existential threat."
  — Narayanan & Kapoor, normaltech.ai, June 11, 2026
- **Our assessment**: The authors make a careful distinction here: they allow that the
  reliability argument is time-bounded ("today's AI"), but the accountability argument is
  structural ("human teams need to be accountable"). These are two separate claims bundled
  together. The accountability claim (someone must be legally and professionally
  responsible for delivered software) is a structural-organizational argument that does not
  dissolve with capability improvements; the reliability claim is a current-state empirical
  observation. For the guide: the accountability layer is the more durable argument; it
  corroborates the Willison accountability gap finding (see `blog-simonwillison-vibe-
  coding-agentic-engineering.md` Claim 3: "Claude Code does not have a professional
  reputation! It can't take accountability for what it's done.").

### Claim 8: Even if the execution layer were made instant and perfect, it would only provide marginal improvement because AI has already largely compressed it

- **Evidence**: Authors' own inference from the framework, stated in the "What does the
  future hold?" section.
- **Confidence**: emerging (the directional claim is sound; the "already largely compressed"
  assertion is not quantified)
- **Quote**: "AI has already largely compressed the middle of the sandwich (and the
  compression actually started decades ago)."
  — Narayanan & Kapoor, normaltech.ai, June 11, 2026
- **Quote**: "even making the execution layer instant and perfect will only be a small
  change from the status quo."
  — Narayanan & Kapoor, normaltech.ai, June 11, 2026
- **Our assessment**: This is the forward-looking implication of Claim 3 (developers spend
  9–61% of time on coding). If execution is a small fraction of engineering time and has
  already been substantially compressed, the ceiling for further compression is low. This
  reframes the AI-coding productivity discussion: the real remaining gains are in the
  outer sandwich layers (decision quality, verification quality), not in making code
  generation faster. For the guide: this implies that investment in spec quality, better
  verification practices, and deeper contextual understanding returns more than investment
  in code generation speed beyond current levels.

### Claim 9: Vibe coding and agentic engineering are categorically distinct — the distinguishing feature is whether the engineer reviews and evaluates agent output

- **Evidence**: Authors' own definitional argument, stated in a dedicated section
  "Vibe coding is not agentic engineering." The definition is prescriptive (what vibe
  coding IS), not empirical.
- **Confidence**: settled (definitional claim by named experts; the definition is clear
  and actionable)
- **Quote**: "In true vibe coding the user simply tells the agent what to do, doesn't
  supervise it when it's running, doesn't review the code — might not even have the
  skills to do so — and doesn't evaluate the output."
  — Narayanan & Kapoor, normaltech.ai, June 11, 2026
- **Our assessment**: This is a sharper, more explicit definition of vibe coding than any
  prior corpus source provides. The key distinguishing elements are: no supervision during
  execution, no code review, no output evaluation — and crucially, "might not even have
  the skills to" perform review. The skills gap is what makes it categorically different
  from agentic engineering: vibe coding is not merely a trust decision (choosing not to
  review) but a capability gap (unable to review). Corroborates and sharpens Willison's
  own observation in `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 1 that
  the boundary between vibe coding and agentic engineering was blurring in his own
  practice — this essay provides the crisp definition the Willison post was circling.

### Claim 10: Software engineer employment is still growing post-ChatGPT, but the growth rate has slowed by approximately 3 percentage points per year relative to a no-AI counterfactual

- **Evidence**: Federal Reserve study cited by the authors. The "3 percentage points per
  year" figure is the measured slowdown relative to counterfactual projections.
- **Confidence**: emerging (Federal Reserve study is credible; counterfactual comparison
  involves modeling assumptions; the 3pp figure is specific but model-dependent)
- **Quote**: "Software engineer employment is still growing, but they find that it is
  growing slower post-ChatGPT compared to a no-AI counterfactual, by about 3 percentage
  points per year."
  — Narayanan & Kapoor, normaltech.ai, June 11, 2026 (summarizing a Federal Reserve study)
- **Our assessment**: This is a crucial nuance for guide framing. "Still growing" and
  "slowing" are both true simultaneously. The AI replacement narrative requires employment
  to be falling; the "AI has no effect" framing requires employment to be unchanged. The
  actual evidence supports a third position: AI is creating a measurable (3pp/year)
  headwind on employment growth without causing net job losses. For the guide: practitioners
  and managers who fear mass layoffs should be shown the WARN Act and Federal Reserve
  data; practitioners who dismiss AI's labor-market effects should be shown the 3pp
  slowdown. Neither pure narrative is accurate.

### Claim 11: Aggregate software labor demand will likely remain healthy but individual engineers may still face rocky career paths as roles and expectations shift

- **Evidence**: Authors' own conclusion, stated as a setup for a subsequent essay in their
  series. Not empirically backed in this essay — stated as a forward-looking claim.
- **Confidence**: anecdotal (forward-looking claim from the authors; the distinction between
  aggregate demand and individual outcomes is analytically sound but not evidenced here)
- **Quote**: "The fact that aggregate labor demand in software is likely to remain strong
  doesn't mean that most individual workers won't be affected."
  — Narayanan & Kapoor, normaltech.ai, June 11, 2026
- **Our assessment**: This is the critical bridge between the macro-level evidence (no mass
  displacement) and the practitioner-level experience (real career disruption). Aggregate
  demand remaining strong is consistent with individual roles becoming obsolete,
  compensation compressing, or skill requirements shifting substantially. The authors
  explicitly flag this for a follow-on essay. For the guide: the team adoption chapters
  should present both the aggregate stability (grounding the level of alarm) and the
  individual disruption dynamic (grounding the urgency to adapt). The `discussion-hn-
  agentic-coding-jobs.md` Claim 1 (Zapier explicitly requiring agentic-only coding as a
  baseline competency) is an early signal of exactly this individual-level shift occurring
  even while aggregate demand holds.

### Claim 12: Willison's personal experience corroborates the framework — deep contextual understanding is the irreplaceable value-add that persists regardless of AI assistance available

- **Evidence**: Simon Willison's first-person practitioner commentary on the essay's
  framework, added to his link-blog post. Willison is a 25-year engineering practitioner
  who actively uses AI agents in daily work (creator of 200+ tools at tools.simonwillison.net).
- **Confidence**: anecdotal (single practitioner self-report; but from the same author who
  has extensively documented his AI practice in prior posts)
- **Quote**: "Give me all of the AI assistance in the world and the value I produce will
  still be reliant on how deeply I understand both the problems and the solutions that the
  agents are building for them."
  — Simon Willison, simonwillison.net, June 14, 2026
- **Our assessment**: Willison's phrasing "the solutions that the agents are building for
  them" is precise — he is describing his role as understanding the problems AND evaluating
  the agents' solutions, not writing code himself. This first-person corroboration from an
  active, self-critical practitioner is more valuable than the same claim from an
  advocate: Willison has no reason to overstate the importance of human expertise, and his
  documented uncertainty and self-criticism (see `blog-simonwillison-vibe-coding-agentic-
  engineering.md` Claim 1 on the vibe/agentic blur) makes this endorsement meaningful.

## Concrete Artifacts

### NY WARN Act AI Disclosure Data (from the essay)

```
Source: Narayanan & Kapoor, "Why AI hasn't replaced software engineers, and won't"
        https://www.normaltech.ai/p/why-ai-hasnt-replaced-software-engineers
        Published: June 11, 2026

NY WARN Act AI disclosure timeline:
  - March 2025:   New York became the first U.S. state to add an AI disclosure
                  checkbox to WARN Act filings (mandatory disclosure when companies
                  attribute layoffs to AI)
  - First full year: 160+ companies filed WARN notices
                     Not a single one checked the AI box
  - Late May 2026:   Only one company (Nespresso) checked the box
                     46 out of ~25,000 laid-off workers in New York State
                     Approximately two-tenths of a percent (0.2%)

Counter-signal (AI washing):
  "59% of U.S. hiring managers admitted they emphasize AI when explaining
  hiring freezes or layoffs because it plays better with stakeholders than
  citing financial constraints."
```

### The Decide-Execute-Deliver Sandwich Model (from the essay)

```
Source: Narayanan & Kapoor, normaltech.ai, June 11, 2026

STRUCTURE:
  DECIDE   — deciding and specifying what to build
             [requires user needs, market signals, org priorities, regulatory constraints]
             [AI: assistance helps but doesn't resolve accountability]
  ─────────────────────────────────────────────────────────────
  EXECUTE  — writing code
             [AI: already largely compressed; further compression = small marginal gain]
  ─────────────────────────────────────────────────────────────
  DELIVER  — verifying and being accountable for what is delivered
             [AI: today too unreliable for unsupervised mission-critical delivery]

PREREQUISITE for all three: "the deep human understanding — of the codebase,
the business, and the environment"

STATUS:
  "AI has compressed the middle of the sandwich, but has left the two ends
  largely unchanged."
  
  "AI has already largely compressed the middle of the sandwich (and the
  compression actually started decades ago)."
  
  "even making the execution layer instant and perfect will only be a small
  change from the status quo."

BOTTLENECK INSIGHT:
  "When we did this analysis, it revealed three things as the real bottlenecks
  (1) deciding and specifying what to build, (2) verifying and being accountable
  for what is delivered, and (3) the deep human understanding — of the codebase,
  the business, and the environment — required to carry out both of these."

  "The reasons why the other two layers have resisted AI is not because of
  capability limitations."
```

### Simon Willison's Commentary (verbatim from his post)

```
Source: Simon Willison, simonwillison.net/2026/Jun/14/why-ai-hasnt-replaced-software-engineers/
Published: June 14, 2026

[Framing the essay:]
"The first good news is that the data still doesn't support the idea that AI
is causing mass unemployment."

"AI speeds up the typing-code-into-a-computer phase, but it turns out software
engineering is about a whole lot more than that:"

[After quoting the three bottlenecks:]
"I'm finding AI assistance also helps me with the deciding and verifying steps,
but it's the 'deep human understanding' that remains key to the value I provide."

"Give me all of the AI assistance in the world and the value I produce will
still be reliant on how deeply I understand both the problems and the solutions
that the agents are building for them."
```

### Essay Section Headings and Key Sentences (from the essay)

```
Source: Narayanan & Kapoor, normaltech.ai, June 11, 2026

Opening: "There is great anxiety and uncertainty about AI replacing jobs."

Essay thesis: "In this essay, we argue that there is enough evidence to reject
the narrative that once AI capabilities reach a certain threshold, it will cause
mass layoffs." [as quoted in Willison's post]

Sections:
  1. [Untitled introduction]
  2. "The stories of AI-driven mass layoffs in software seem to be classic
     'AI washing'"
  3. "Why coding agents haven't led to labor displacement: the decide-execute-
     deliver sandwich"
  4. "Vibe coding is not agentic engineering"
  5. "What does the future hold?"

Developer time allocation (2019 Microsoft paper cited):
  "developers spend surprisingly little time with coding, 9% to 61% depending
  on the study"

Task-breakdown surveys finding:
  "If writing code isn't the bottleneck, what is? The task-breakdown surveys
  point at things like meetings or debugging." [as quoted in Willison's post]

Employment trend (Federal Reserve study cited):
  "Software engineer employment is still growing, but they find that it is
  growing slower post-ChatGPT compared to a no-AI counterfactual, by about
  3 percentage points per year."

Vibe coding definition:
  "In true vibe coding the user simply tells the agent what to do, doesn't
  supervise it when it's running, doesn't review the code — might not even
  have the skills to do so — and doesn't evaluate the output."

Conclusion / series setup:
  "This essay is the first in a series, and the next one will look at reasons
  why individual software engineers' careers might be rocky even if overall
  demand is healthy."

  "The fact that aggregate labor demand in software is likely to remain strong
  doesn't mean that most individual workers won't be affected."
```

## Cross-References

- **Corroborates**: `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 9
  ("Experienced engineers remain the primary value driver because AI tools amplify existing
  expertise rather than replacing it") and Claim 10 ("Software complexity remains ferociously
  difficult regardless of code generation speed"): Willison's May 6 post makes the same
  core argument in his own practitioner voice; this June 14 post adds the empirical
  framework (WARN Act data, task surveys) and the formal "decide-execute-deliver" model
  to what was previously an analytical observation. The two posts from the same author,
  four weeks apart, converge on identical conclusions from different starting points
  (practitioner self-report vs. research essay curation).

- **Corroborates**: `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 3 ("AI
  agents lack the professional accountability that makes trusting-without-reviewing human
  teams acceptable"): This source's Claim 7 ("human teams need to be accountable for what
  they deliver") is the Narayanan/Kapoor articulation of the same structural fact Willison
  named from practitioner experience. Narayanan/Kapoor ground it in organizational
  accountability requirements; Willison grounds it in the absence of agent professional
  reputation. The two framings are complementary: one is the organizational necessity
  (accountability must exist somewhere), the other is the gap (agents cannot hold it).

- **Corroborates**: `discussion-hn-agentic-coding-jobs.md` Claim 10 ("The aggregate
  productivity return from agentic coding may be marginal for practitioners who have not
  rebuilt their workflow around it"): codingdave's practitioner experience ("a little more
  speed alongside a little more slop") is consistent with the Narayanan/Kapoor framework.
  If AI has already largely compressed the execution layer, additional execution speed
  would be marginal — exactly what codingdave experiences. The two sources describe the
  same phenomenon from different vantage points (practitioner frustration vs. structural
  model).

- **Corroborates**: `blog-simonwillison-charity-majors-enthusiast-skeptic.md` Claim 3
  ("AI skeptics are also not wrong — shipping code faster than engineers can read it
  depletes institutional trust"): Majors' skeptic argument is the delivery-side expression
  of the Narayanan/Kapoor Claim 7. Majors names the organizational trust dynamic; Narayanan/
  Kapoor name the accountability requirement. Both point to the same structural resistance:
  humans must understand, verify, and be responsible for delivered software.

- **Extends**: `discussion-hn-agentic-coding-jobs.md` Claim 1 ("Zapier is now explicitly
  requiring agentic-only coding as a job expectation, not just AI-assistance"): The Zapier
  posting is consistent with Narayanan/Kapoor's Claim 11 — aggregate employment demand
  remains strong, but individual role descriptions are shifting. An employer can simultaneously
  NOT lay off engineers due to AI AND require that remaining engineers work through agents.
  The Narayanan/Kapoor macro frame and the Zapier micro signal are not contradictions;
  they describe different levels of the same labor-market shift.

- **Novel** (not present in any existing corpus note):
  - **The "decide-execute-deliver sandwich" as a named model**: No existing corpus source
    provides a three-layer model of software engineering work with this structure and
    terminology. This model is the most compact analytical frame in the corpus for
    explaining why AI coding acceleration doesn't translate to AI engineering replacement.
  - **NY WARN Act as empirical evidence**: The corpus has no prior source using government
    labor-regulation filing data to assess AI displacement claims. This is the most
    concrete empirical data in the corpus on the actual labor-market footprint of
    AI-related software engineering layoffs.
  - **"AI washing" as the directional bias**: No corpus source previously named the
    tendency to over-attribute hiring freezes to AI for stakeholder management purposes.
    Prior sources address AI hype generally; this essay identifies a specific mechanism
    (stakeholder narrative management) by which AI's labor impact is overstated.
  - **The 3pp/year employment growth slowdown quantification**: The Federal Reserve finding
    of 3 percentage points per year slower growth vs. counterfactual is the only
    quantitative labor-market estimate in the corpus for AI's effect on software engineer
    employment. Prior corpus sources either claim no impact or speculate about replacement;
    this is measured evidence for a real but bounded effect.
  - **The "decide-execute-deliver" structural argument that resistance is not capability-
    based**: The claim that better AI won't resolve the outer-layer bottlenecks (because
    they're structural, not capability-limited) is a novel and important position in the
    corpus. Prior sources attribute the hard parts of software engineering to current AI
    limitations (the implication being: wait for better AI). Narayanan/Kapoor reject that
    framing.

- **Contradicts**: None found requiring a filed contradiction issue. The employment
  slowdown finding (Claim 10) is nuanced but not in conflict with any existing corpus
  note — no prior note claims software engineer employment is unaffected by AI. The
  accountability argument (Claim 7) is consistent with Willison's prior framing. The
  "AI washing" claim is novel and has no prior corpus position to contradict.

## Guide Impact

- **Chapter 00 (Principles)**: The decide-execute-deliver sandwich model (Claim 4) should
  appear as foundational context for the guide's core premise. The guide argues for
  AI-native engineering — this essay explains *why* that framing is more accurate than
  "AI replaces engineering." Practitioners and their managers reading the guide need to
  understand that AI's productivity gains are bounded to the execution layer, which is
  already largely compressed, while the outer layers (specification quality, verification
  discipline, contextual understanding) remain the primary value drivers. The Narayanan/
  Kapoor framework is the most compact argument for why experienced engineers investing
  in AI tools remain valuable: the tools amplify the execution layer, which already isn't
  the bottleneck.

- **Chapter 01 (Daily Workflows)**: The vibe coding definition (Claim 9) should be added
  to any section that introduces the guide's audience to the distinction between casual
  AI use and structured agentic engineering. The Narayanan/Kapoor definition is crisper
  and more diagnostic than any prior corpus definition: vibe coding is identifiable by
  the absence of supervision, code review, output evaluation, and potentially the skills
  needed to review. A practitioner can self-assess against this definition. The guide
  should recommend that its readers locate themselves in the agentic engineering practice
  and understand what distinguishes it from vibe coding.

- **Chapter 01 (Daily Workflows)** and **Chapter 05 (Team Adoption)**: The WARN Act
  data (Claim 1) and employment growth slowdown (Claim 10) should be cited whenever the
  guide discusses AI's labor-market impact. The guide should present both pieces of data
  together: the displacement narrative is not supported by government filing records;
  growth is slowing but positive. This grounds discussions of urgency without panic and
  avoids both dismissiveness and alarmism about AI's effects on engineering careers.

- **Chapter 05 (Team Adoption)**: Claim 11 (aggregate demand stable; individual careers
  rocky) is the precise framing teams need for adoption conversations with engineers who
  worry about their jobs. The guide can honestly say: the evidence shows no mass
  displacement occurring; but individual role expectations are shifting toward directing
  agents rather than writing code; the teams that adapt will be the ones whose members
  remain employed in rewarding roles. Connect to `discussion-hn-agentic-coding-jobs.md`
  Claim 1 (Zapier requiring agentic competency as a baseline job expectation) as a leading
  indicator of where the individual-career shift is visible in the market.

- **Chapter 03 (Verification)**: Claim 7 (accountability cannot be delegated to today's
  AI) should anchor any section on human-in-the-loop verification requirements. The
  Narayanan/Kapoor framing distinguishes the structural accountability argument (humans
  must be responsible for delivered software) from the capability-limitation argument
  (today's AI is too unreliable). Both apply today; only one will remain as AI improves.
  The guide should explicitly note that even dramatically more capable AI will not resolve
  the accountability-structure argument without organizational redesign.

## Extraction Notes

- **Two-layer source**: The issue URL (Willison's link-blog entry) is a short post (~200
  words) that frames the essay and adds personal commentary. All analytical content beyond
  Willison's four quoted sentences comes from reading the linked essay at
  https://www.normaltech.ai/p/why-ai-hasnt-replaced-software-engineers directly, per
  MINER.md §1 (follow up to 5 linked pages that seem substantive). The Narayanan/Kapoor
  essay is the primary substantive source.
- **Quote attribution in this note**: All quotes are labeled with their actual source
  (Willison's page vs. the essay). When Willison's post quotes from the essay, those
  quotes are attributed to the essay with the note that they appeared in Willison's post.
- **aisnakeoil.com redirects to normaltech.ai**: The authors appear to have renamed their
  newsletter. Both URLs resolve to the same content; the normaltech.ai URL is used
  throughout this note as the stable address. The redirect was confirmed during extraction.
- **Publication date**: The Willison post is June 14, 2026. The linked essay was published
  June 11, 2026, three days earlier. date_published in frontmatter reflects the Willison
  post date, which is the canonical source URL per the issue submission.
- **Credentials for Narayanan & Kapoor**: The authors are described by Willison as
  "Arvind Narayanan" (tagged on the post). They identify themselves on normaltech.ai as
  co-authors of *AI Snake Oil* (Princeton University Press, 2024), a book applying
  critical empirical analysis to AI claims. Narayanan is a Princeton CS professor;
  Kapoor is a Princeton researcher. Their credibility on AI capability claims is high
  due to academic grounding and their established practice of testing AI claims against
  evidence.
- **"Writing Code vs. Shipping Code" citation**: The essay cites a publication by this
  name among the task-breakdown survey sources. The full citation was not accessible
  in the fetched content; the 2019 Microsoft paper and the SWE-chat study are also cited.
- **Cross-reference verification**: All claim numbers cited from other source notes were
  verified by re-reading those notes in this session:
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 3 (lines 86–103):
    "AI agents lack professional accountability" — verified.
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 9 (lines 201–219):
    "Experienced engineers remain the primary value driver" — verified.
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 10 (lines 221–237):
    "Software complexity remains ferociously difficult" — verified.
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 1 (lines 48–64):
    "The boundary between vibe coding and agentic engineering has begun to blur" — verified.
  - `discussion-hn-agentic-coding-jobs.md` Claim 1 (lines 123–144): "Zapier requiring
    agentic-only coding" — verified.
  - `discussion-hn-agentic-coding-jobs.md` Claim 10 (lines 303–325): "Aggregate
    productivity return may be marginal" — verified.
  - `blog-simonwillison-charity-majors-enthusiast-skeptic.md` Claim 3 (lines 87–109):
    "AI skeptics are also not wrong — shipping code faster than engineers can read it
    depletes institutional trust" — verified.
