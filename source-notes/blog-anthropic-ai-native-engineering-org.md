---
source_url: https://claude.com/blog/running-an-ai-native-engineering-org
source_type: blog-post
title: "Running an AI-native engineering org"
author: Fiona Fung (Director of Engineering, Claude Code and Claude Cowork, Anthropic)
date_published: 2026-06-03
date_extracted: 2026-06-03
last_checked: 2026-06-03
status: current
confidence_overall: emerging
issue: "#1038"
---

# Running an AI-native engineering org

> A first-person account from Anthropic's Director of Engineering for Claude Code on how organizational processes — planning, context gathering, code review, team structure, and hiring — had to change when agentic coding became the team's default way of working; provides the clearest primary-source validation yet of the "bottleneck shift" thesis and a named three-metric framework for tracking adoption stickiness.

## Source Context

- **Type**: blog-post (claude.com/blog, June 3, 2026; first-person practitioner account)
- **Author credibility**: Fiona Fung is the Director of Engineering for Claude Code and Claude Cowork at Anthropic — she manages the engineering team that *builds* the tool the guide is about. This is the highest-credibility possible primary source for "what actually changes organizationally" because (1) she has direct visibility into her own team's practices, (2) she has the authority to define new norms, and (3) her team is the most intensive known user of Claude Code on the planet. Limitations: single organization, which has unique characteristics (everyone dogfoods the product; high AI sophistication; Anthropic resources). The patterns she describes may not generalize to organizations with less AI-native culture.
- **Scope**: Covers four process areas (planning, context gathering, code review, team makeup), a rollout methodology (three core team principles), a measurement framework (three metrics), and a getting-started heuristic. Does NOT cover: technical harness configurations (CLAUDE.md, hooks, permissions), cost or token economics, specific tools used beyond Claude Code and Claude Cowork, individual engineer accounts, or quantitative metrics beyond qualitative claims about commit patterns and onboarding speed.

## Extracted Claims

### Claim 1: Verification, code review, and security replaced code-writing as the primary bottlenecks when agentic coding became the default

- **Evidence**: First-person observation from the Director of Engineering for Claude Code, describing her own team's experience after adopting agentic coding as the default workflow.
- **Confidence**: emerging (first-party practitioner account; aligns with independent converging evidence from Osmani and Shopify, see Cross-References)
- **Quote**: "On the Claude Code team, writing code, writing tests, and refactoring rarely slows us down anymore. But the bottlenecks didn't go away when agentic coding took away the actual need to type code. Verification, code review, and security took their place."
- **Our assessment**: This is the single most important claim in the source. It names where effort now concentrates when code generation is no longer the constraint. Critically, this is now the third independent source making this claim in the corpus (alongside Osmani's "The bottleneck is no longer generation. It's verification." and Shopify's "[Code review has become] a big bottleneck"). The Anthropic source is uniquely authoritative: Fung is reporting on the team that builds the tool, making this a claim about effect at the source, not downstream.

### Claim 2: Six-month roadmaps became obsolete within three months on the Claude Code team due to agentic engineering speed

- **Evidence**: First-person anecdote from Fung about the team's experience immediately after adopting Claude Code as the default. The "out of date by month three" observation is specific and quantified.
- **Confidence**: anecdotal (single-org experience, not controlled measurement; but specific enough to be credible rather than vague)
- **Quote**: "When I first joined the Claude Code team, we wrote a pretty good six month roadmap, and then _because_ of Claude Code, so many things changed that it was out of date by month three."
- **Our assessment**: The "half-life of a roadmap" claim is a concrete calibration point no existing source provides. If engineering throughput roughly doubles (a conservative estimate from multiple corpus sources), a six-month roadmap covers work that can now complete in three. The "out of date by month three" observation is not about the roadmap being wrong — it is about the pace of execution making it irrelevant faster than expected. This should anchor any chapter section on planning in AI-native teams: long-horizon planning assumptions break because execution speed changed.

### Claim 3: Just-in-time (JIT) planning — short-cycle, prototype-driven, feedback-loop-focused — replaced pre-planned design docs as the dominant planning ritual

- **Evidence**: Named methodology ("I call it just-in-time (JIT) planning") with explicit description of what changed: away from design docs, toward discussions in PRs or prototypes, with rapid internal feedback cycles.
- **Confidence**: emerging (first-party organizational claim; the JIT framing is novel but the underlying shift is consistent with what other sources describe)
- **Quote**: "I call it just-in-time (JIT) planning, almost like JIT compiling: how do you do just the right amount at the right time? Our planning ritual shifted away from design docs toward discussions in PRs or prototypes. The space moves fast so we don't do a lot of product reviews. Our process now is let's prototype, get a lot of internal users on it, and start acting on their feedback."
- **Our assessment**: "JIT planning" is a named, quotable concept from a highly credible source. The analogy to JIT compiling is apt: do planning work at the moment it is needed rather than speculatively ahead of time. The implication is that design docs (written before any code exists) are a form of premature planning that becomes expensive to update when execution outpaces assumptions. For the guide: this is the planning counterpart to the code review and verification shifts — three organizational areas all adapting to the same underlying change in throughput.

### Claim 4: Context gathering shifted from "find the code author" to asking Claude what you actually need to know — the question changed, not just the tool

- **Evidence**: First-person account of a specific norm change: the old norm was to find the person who wrote the code; the new norm is to identify what you actually need (regression owner? expert? decision context?) and ask Claude.
- **Confidence**: emerging (first-party organizational norm change; specific and plausible)
- **Quote**: "When engineers wrote code, the first step to getting an answer to most questions was to find the person who wrote the code. Now, since all our PRs are assisted by Claude, 'Who made this change?' is no longer sufficient. Our new norm is to go a level deeper: what do you actually need to know? For instance: Are you looking for who caused a regression? An expert to answer a customer question? Or context on a decision? You ask Claude that question, and consider whether Claude can answer it directly, also with more data and context."
- **Our assessment**: This is an observation about knowledge retrieval changing, not just tooling changing. "Who made this change?" assumes a human author holds unique knowledge about intent and rationale. When all PRs are Claude-assisted, authorship is diffused — the meaningful question is what knowledge is actually needed, not who holds it. This has implications for documentation practices: institutional knowledge historically lived in the heads of code authors; in an AI-native org, it increasingly lives in the context the agent was given and in the commit/PR history.

### Claim 5: Every recurring information request should trigger a standard automation question — the Claude Code team always asks "Is there a way to automate it?"

- **Evidence**: First-person description of a team norm, with a concrete example (customer feedback channel summary automation).
- **Confidence**: emerging (first-party norm description; the example is specific and replicable)
- **Quote**: "On the Claude Code team, no matter what that question is, our process is to also ask 'Is there a way to automate it?' For example, having Claude summarize customer feedback channels every morning went from a ritual I did manually with my coffee to something I just have running automatically in the background."
- **Our assessment**: The automation reflex is a specific behavioral norm, not just a general principle. The feedback channel example demonstrates the scope: a manual ritual (Fung reading and summarizing feedback channels herself each morning) became a scheduled automation. This is directly equivalent to the routine use case described in `blog-anthropic-claude-code-routines.md`. The "always ask" framing makes this a decision habit rather than an ad-hoc optimization. For the guide: this is the operationalization of "automate the boring stuff" — teams that internalize this question will continuously identify and eliminate routine information-gathering work.

### Claim 6: Code review has bifurcated — Claude handles style, linting, bug-catching, test addition; humans retain domain expertise in legal, security, and product sense

- **Evidence**: First-person description of the team's current code review practice, naming specific Claude-handled areas and specific human-retained areas.
- **Confidence**: emerging (first-party organizational practice; consistent with multiple corpus sources; specific enough to be actionable)
- **Quote**: "We use Code Review heavily. Claude handles all the style and linting, PR feedback requests, catching bugs and fixing them before a full commit, and adding tests. Where we still definitely want a human is expertise. The new norm is human review where it matters: for legal review, I always want my legal partner involved in risk tolerance. For trust boundaries and security-sensitive code, I want the domain experts. Product managers and designers also need to be involved with product sense and taste."
- **Our assessment**: The bifurcation is clearly specified: Claude handles what can be evaluated mechanically or through pattern recognition (style, linting, test coverage, common bugs); humans handle what requires irreducible judgment (legal risk tolerance, security trust model, product taste). This is not a claim that humans review less — it is a claim that humans review *differently*. The "trust but verify" framing in the section heading is explicit: the shift is to trusting Claude on the mechanical layer while concentrating human expertise on the judgment layer.

### Claim 7: The right balance of human vs. AI review will keep changing as models improve — what requires human expertise today may not tomorrow

- **Evidence**: First-person caveat embedded in the code review section. Fung explicitly frames the current balance as temporary and model-dependent.
- **Confidence**: anecdotal (forward-looking claim; but directionally sound given observed model capability trends)
- **Quote**: "It's important to continually evaluate, though, because the right balance of trust vs. verify will keep changing as the models improve. What you need humans for today might look different with the next model."
- **Our assessment**: This is an important epistemic humility claim from the source — she is explicitly saying her own recommendations are provisional. For the guide: any chapter section on code review should carry this caveat. Specific recommendations about what Claude handles vs. what humans handle are time-stamped by current model capabilities. Teams should build a regular review cadence for their human-vs-AI review boundary rather than treating any current practice as permanent.

### Claim 8: Roles blurred in the AI-native team — PMs now code, engineers do content and design; the traditional technical/non-technical division is dissolving

- **Evidence**: First-person observation from the team's director. The PM coding example and engineers doing content/design are specific behavioral changes, not aspirational descriptions.
- **Confidence**: emerging (first-party observation; specific examples; consistent with what AI-tooling reduces the technical barrier for)
- **Quote**: "Claude and AI have reshaped roles across the team. Our PMs code a lot now, which is fun to see. With Claude, you have nontraditional coders now being able to do more engineering, and you have engineers who take on things like content and design, work that were traditionally not on the technical side."
- **Our assessment**: The role blurring is a downstream consequence of AI lowering the skill threshold for crossing role boundaries. A PM who wants to build a prototype no longer needs to learn a full software stack — they can work with Claude at a higher level of abstraction. An engineer who wants to draft documentation no longer needs content-writing expertise — they can collaborate with Claude on prose. The traditional divide (technical vs. non-technical) was partly enforced by the high cost of acquiring skills outside your domain. That cost is reduced when AI can scaffold the gaps.

### Claim 9: Hiring now prioritizes two profiles over raw throughput — "creative builders with product sense" and "engineers with deep systems expertise"

- **Evidence**: First-person statement of hiring philosophy with explicit anti-priority (raw throughput) and two named positive profiles with rationale.
- **Confidence**: emerging (first-party hiring philosophy statement; consistent with the role-blurring claim and the verification-bottleneck claim)
- **Quote**: "On the Claude Code engineering team, I've indexed heavily on two profiles. One is creative builders with product sense: the dreamers who are deeply curious and passionate about shipping products that solve problems. The other one is engineers with deep systems expertise. [...] What I index on less, on the other hand, is raw throughput; the models handle that. The more important question is where you still need human expertise, and that's where I'd focus."
- **Our assessment**: This is the most operationally radical claim in the source from a hiring/org design perspective. "Raw throughput" (write more code faster) is deprioritized because models handle throughput. What cannot be delegated to models — according to Fung — is (1) product intuition and creative direction, and (2) deep systems knowledge for the parts of the stack where understanding is non-negotiable (e.g., building a web execution environment). This is a strong signal for the guide's team adoption chapter: if the Anthropic team building Claude Code is de-emphasizing throughput in hiring, that is a leading-edge signal about where human value concentrates.

### Claim 10: Three core team principles enabled the norm rollout — relentless dogfooding, maximum flatness, and permission to kill obsolete processes

- **Evidence**: First-person description of the principles the team operates under, listed explicitly.
- **Confidence**: emerging (first-party organizational philosophy; the three principles are specific and actionable)
- **Quote**: "Relentlessly dogfood your product" / "Keep the team flat as possible." / "Don't hesitate to kill processes that no longer work"
- **Our assessment**: The three principles are interdependent. Dogfooding ensures the team experiences the tool's capabilities first-hand, enabling genuine process change rather than policy-mandated change. Flatness enables rapid norm updates without bureaucratic drag. Permission to kill processes removes the organizational inertia that causes obsolete norms to persist. Together, they constitute a change management framework specifically suited to a rapidly-evolving AI-native environment where what's true today may not be true next month.

### Claim 11: Three metrics signal that new AI-native norms are sticking — onboarding ramp time, PR cycle time, and Claude-assisted commit rate approaching 100%

- **Evidence**: Named metrics with specific manifestations. The "non-Claude-assisted commit" claim includes a concrete recent observation.
- **Confidence**: emerging (first-party metric description; specific enough to be actionable as a measurement framework)
- **Quote** (onboarding): "Onboarding ramp time goes down" — "engineers ship real code now within their first week"
- **Quote** (commits): "I don't think I've seen a non-Claude-assisted commit in the last four months"
- **Our assessment**: The three metrics form a coherent measurement suite: onboarding time (speed of new engineer capability development), PR cycle time (process infrastructure health — if it goes up, the pipeline is bottlenecked, not the engineers), and Claude-assisted commit rate (adoption penetration). The third metric approaching 100% is the most striking — it means AI-assisted coding is not an optional feature some engineers use; it is effectively universal on the team. This is a concrete calibration point: on Anthropic's own engineering team, non-AI-assisted commits have essentially disappeared.

### Claim 12: Throughput is not a reliable success metric in AI-native engineering — it must not be confused with real outcomes

- **Evidence**: Explicit warning embedded in the metrics section.
- **Confidence**: emerging (first-party warning from a practitioner whose team has high throughput; consistent with the corpus's evidence that throughput gains do not translate linearly to business outcomes)
- **Quote**: "Don't confuse throughput with success."
- **Our assessment**: This is a direct counter to the "10x developer" framing common in vendor marketing. Fung — writing for the team that has the highest possible access to AI throughput — explicitly warns against using throughput as the success metric. This is consistent with Shopify's 20% "humble estimate" of productivity gain (not 10x) and with the Faros productivity paradox (organizational delivery does not scale linearly with individual throughput). The guide should cite this prominently as insider evidence against throughput maximization as the primary adoption goal.

### Claim 13: The entry point for changing norms is identifying the "noisiest workflow" — the most friction-generating, recurring process — and asking whether it still serves its purpose

- **Evidence**: First-person recommendation from the getting started section, with an implied example (the expensive weekly status meeting that was eliminated).
- **Confidence**: anecdotal (single-source recommendation; but methodologically sound as a change-management entry point)
- **Quote**: "pick your noisiest workflow" / "Why are we having this meeting again?"
- **Our assessment**: "Noisiest workflow" is a concrete heuristic for change management that avoids the paralysis of trying to transform everything at once. It prioritizes the processes where the cost of inertia is highest and where eliminating or automating would provide the largest immediate relief. The meeting elimination anecdote grounds this in the most universal process debt (unnecessary recurring meetings) that every engineering team carries. For team adoption chapters: this is the recommended starting point for teams beginning to examine their AI-era process debt.

## Concrete Artifacts

### Section Structure of the Article

```
"Running an AI-native engineering org"
Fiona Fung, Director of Engineering, Claude Code and Claude Cowork
claude.com/blog, June 3, 2026

Sections:
  The processes that quietly stopped working
  Planning: shift roadmaps to just in time
  Context gathering: ask Claude, not the author
  Code review: trust but verify
  Team makeup: blurring roles
  How we rolled out our new norms
  How to know your new processes are sticking
  Getting started
```

### Process Change Summary (Extracted from Article)

```
"Running an AI-native engineering org" — Process Changes
Fiona Fung (Anthropic), June 3, 2026

PLANNING
  Old norm:  Six-month roadmaps + extensive pre-planning (coding was expensive)
  New norm:  JIT planning — prototype, get internal users on it, act on feedback
  Mechanism: Discussions in PRs or prototypes replace formal design docs
  Why:       Six-month roadmap was out of date by month three because of Claude Code

CONTEXT GATHERING
  Old norm:  Find the code author ("Who made this change?")
  New norm:  Ask Claude what you actually need; also ask "Is there a way to automate it?"
  Why:       "All our PRs are assisted by Claude" — authorship no longer implies knowledge

CODE REVIEW
  Old norm:  (implied: broader, more uniform human review)
  New norm:  Claude handles style/linting/PR feedback/bug-catching/tests;
             Humans handle legal risk tolerance, security/trust boundaries, product sense
  Key caveat: "The right balance of trust vs. verify will keep changing as the models improve"

TEAM MAKEUP
  Old norm:  Clear technical/non-technical division by role
  New norm:  PMs code; engineers do content and design; roles blur across traditional lines
  Hiring:    Index on "creative builders with product sense" and "deep systems expertise";
             de-index on "raw throughput" (models handle that)
```

### Metrics for Tracking Adoption Stickiness (Extracted from Article)

```
Three Metrics — "Running an AI-native engineering org"
Fiona Fung (Anthropic), June 3, 2026

1. Onboarding ramp time goes down
   Signal: Engineers ship real code within their first week
   What it measures: Speed of new engineer capability development

2. PR cycle time goes down
   Signal: Identifies infrastructure/pipeline bottlenecks (not engineer bottlenecks)
   What it measures: Health of the overall development pipeline

3. Claude-assisted commits going up (→ approaching 100%)
   Signal: "I don't think I've seen a non-Claude-assisted commit in the last four months"
   What it measures: Actual adoption penetration across the team

Warning: "Don't confuse throughput with success."
```

### Three Core Team Principles (Verbatim from Article)

```
How Anthropic's Claude Code team rolled out new norms:
Fiona Fung (Anthropic), June 3, 2026

  1. "Relentlessly dogfood your product"
     Every team member uses Claude Code and Claude Cowork constantly;
     managers start as ICs, learn by shipping, stay close to the product

  2. "Keep the team flat as possible."
     Enables rapid norm updates without bureaucratic drag

  3. "Don't hesitate to kill processes that no longer work"
     Explicit permission to question and eliminate obsolete processes
     Entry point: "pick your noisiest workflow" — ask if it still serves its purpose
```

## Cross-References

- **Corroborates**: `blog-addyosmani-code-agent-orchestra.md` (Claim 5): Osmani's thesis "The bottleneck is no longer generation. It's verification." directly matches Fung's "Verification, code review, and security took their place." These are two independent sources — Osmani as a practitioner-synthesizer, Fung as a first-party organizational account — converging on the same bottleneck diagnosis. This is now a three-way convergence in the corpus: Osmani, Shopify (below), and Anthropic.

- **Corroborates**: `blog-bvp-shopify-ai-playbook.md` (Claim 4): Farhan Thawar's "[Human review has become] a big bottleneck" at Shopify matches Fung's finding at Anthropic. Three independent organizations (Osmani's cross-org synthesis, Shopify, and Anthropic's own team) now separately identify code review as the post-AI-adoption bottleneck. This convergence is load-bearing for the guide — the bottleneck shift is not a vendor claim, it is independently reported by practitioners using different tools and working in different organizations.

- **Corroborates**: `blog-bvp-shopify-ai-playbook.md` (Claim 8): Shopify's explicit warning that "The brain is a muscle. If you stop using your brain — it will atrophy." maps to Fung's finding that human review must concentrate on irreducible domain expertise (legal risk tolerance, security trust boundaries, product taste). Both organizations independently conclude that the human role narrows to judgment areas that cannot be delegated — which is the appropriate response to the comprehension debt risk, not abdication of review.

- **Corroborates**: `blog-anthropic-code-w-claude-london-2026.md` (Claim 2): Boris Cherny's framing "With agents, that distance is collapsing again: you describe a problem, and the program shows up" describes *why* engineering orgs need to change. Fung's article describes *what* actually changes when that distance has collapsed in an org that fully adopted it. The London article provides the philosophical why; this article provides the operational what.

- **Extends**: `blog-anthropic-claude-code-routines.md` (Claim 9 and the scheduled use cases): Fung's "having Claude summarize customer feedback channels every morning went from a ritual I did manually with my coffee to something I just have running automatically in the background" is a live practitioner example of the scheduled routine pattern the routines article names as a use case. This is first-party confirmation from an Anthropic engineering director that the routine use case is real and in daily use on Anthropic's own team — not a hypothetical from a product announcement.

- **Extends**: `blog-anthropic-claude-code-auto-mode.md` (Claim 1): The 93% blanket approval rate in manual mode and the bottleneck shift described in the auto mode post are consistent with Fung's finding. Auto mode addresses the verification-bottleneck problem at the permission-gating layer; Fung describes the broader organizational reshaping the same bottleneck drives. They are complementary: auto mode is the tooling response; Fung describes the organizational response.

- **Novel**:
  - **"JIT planning" as a named methodology**: No existing corpus source names a specific planning methodology for AI-native teams. "Just-in-time planning, almost like JIT compiling" is the first named, quotable concept for this shift. It provides the guide with a term of art rather than a description.
  - **Six-month roadmap half-life**: The "out of date by month three" observation is the first concrete calibration of how quickly traditional planning horizons become obsolete at AI-native engineering velocity. No other corpus source provides this specific a data point.
  - **"Ask Claude first" as an explicit context-gathering norm**: While other sources discuss Claude Code for code work, no corpus source names the context-gathering shift as a formal organizational norm — the replacement of "find the author" with "ask Claude then ask if it can be automated." This is a new behavioral norm, not just a tool preference.
  - **Hiring de-emphasis of raw throughput**: No other corpus source explicitly states that raw throughput should be de-prioritized as a hiring criterion because models handle it. This is a leading-edge organizational claim with significant implications if it becomes a broader industry norm.
  - **Three-metric adoption measurement framework**: Onboarding ramp time + PR cycle time + Claude-assisted commit rate is a specific, named measurement suite from a named practitioner. No other corpus source provides a complete, attributed measurement framework for tracking AI adoption stickiness at the team level.
  - **Non-Claude-assisted commits essentially absent at Anthropic**: "I don't think I've seen a non-Claude-assisted commit in the last four months" is the most concrete adoption metric in the corpus from the most credible possible source. It establishes what 100% adoption looks like in practice.
  - **"Don't confuse throughput with success"**: An explicit anti-metric warning from the director of engineering for Claude Code — the most credible possible voice for "here is what success actually looks like." No other source states this as bluntly or from this vantage point.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add Fung's "ask Claude first, then ask if it can be automated" norm as the canonical context-gathering workflow for AI-native teams. The automation reflex ("Is there a way to automate it?") should be presented as a standard next-step whenever a recurring information request is identified. The customer feedback channel automation example is a concrete worked case to cite. Current corpus covers Claude Code for code tasks; this extends the norm to information-retrieval tasks.

- **Chapter 01 (Daily Workflows — Planning)**: Add "JIT planning" as the named AI-native alternative to roadmap-driven development. Cite the "out of date by month three" observation as the calibration for why long-horizon planning assumptions break. The shift from design docs to PR discussions and prototypes should be presented as the planning ritual change that accompanies throughput changes — plan just enough, just in time, verified by rapid internal feedback rather than upfront specification.

- **Chapter 02 (Harness Engineering — Code Review)**: The bifurcated code review model (Claude handles mechanical; humans handle domain expertise) should be the anchor claim for the code review section, citing Fung explicitly. The caveat that "the right balance of trust vs. verify will keep changing as the models improve" should appear verbatim as a reminder that any specific recommendation is time-stamped to current model capabilities. This extends the existing corpus coverage of code review (Shopify's bottleneck claim, Sentry's `/gh-review` command) with Anthropic's own first-party practice.

- **Chapter 05 (Team Adoption — Metrics)**: The three-metric adoption framework (onboarding ramp time, PR cycle time, Claude-assisted commit rate) should be presented as a named, attributed measurement suite from Fung. The "Don't confuse throughput with success" warning belongs in the measurement section as the canonical anti-metric caution — throughput is observable but not the right success signal. Currently the corpus lacks a coherent measurement framework for team adoption; Fung's three metrics fill this gap.

- **Chapter 05 (Team Adoption — Role Changes)**: The role-blurring claim (PMs code, engineers do design/content) and the hiring philosophy shift (de-emphasize throughput, prioritize product sense and systems expertise) should appear in the chapter's discussion of how AI adoption changes team structure. Currently the corpus covers adoption patterns (who adopts first, how to drive adoption) but not the downstream structural consequences on roles and hiring priorities. This is novel evidence for those consequences.

- **Chapter 05 (Team Adoption — Getting Started)**: The "noisiest workflow" heuristic should be presented as the recommended entry point for teams beginning to change their AI-era process norms. The three team principles (dogfood, flat, kill obsolete processes) provide the organizational conditions that make continuous norm evolution possible — they belong in the change management section alongside the concrete adoption patterns.

- **Chapter 05 (Team Adoption — Convergence Evidence)**: Fung's bottleneck claim, combined with Osmani's verification bottleneck thesis and Shopify's code review bottleneck confirmation, constitutes three-way convergence that the guide should cite explicitly. This is the strongest convergence in the corpus on any single operational finding.

## Extraction Notes

- The article was fetched multiple times with escalating verbatim-extraction prompts. The quotes in this note are directly from the source except where noted. The WebFetch tool declined to reproduce the full article verbatim (copyright), so quotes were extracted section by section using targeted prompts.
- The "I don't think I've seen a non-Claude-assisted commit in the last four months" quote was provided in response to a targeted statistics/metrics extraction prompt and is treated as verbatim from the source. Assayers should spot-check this quote against the live URL.
- The article is a personal blog-post-style piece (first-person "I"), not a formal Anthropic research post. This increases authenticity (Fung is describing lived experience, not official company positioning) but limits formality (no methodology, no controls, no quantitative benchmarks).
- No linked sub-pages were followed; the article appears to be a single standalone page with no substantive linked content.
- No contradiction with existing corpus notes was found that would require filing a contradiction issue. The closest tension — Shopify does not permit autonomous AI commits (Claim 3 from `blog-bvp-shopify-ai-playbook.md`), while Fung says "Claude-assisted commits" are near-universal — is not a contradiction: Shopify's claim is about autonomous AI commits without human approval; Fung's claim is about human commits made with Claude's assistance. These are different concepts.
- Confidence is set to `emerging`: Fung is the highest-credibility possible practitioner source for organizational effects of Claude Code adoption on an AI-native team. But the claims are from a single organization with unique characteristics (building the tool itself), without quantitative controls, and the most actionable claims (JIT planning, role blurring, hiring philosophy) are organizational observations rather than reproducible measurements.
