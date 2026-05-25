---
source_url: https://cursor.com/blog/third-era
source_type: blog-post
title: "The third era of AI software development"
author: Michael Truell (Cursor CEO)
date_published: 2026-02-26
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: emerging
issue: "#141"
---

# The third era of AI software development (Michael Truell, Cursor)

> Cursor's CEO frames AI-assisted development as three named eras — Tab autocomplete,
> synchronous agents, and cloud agents — with concrete Cursor-internal adoption metrics
> (15× agent usage growth, 35% of internal PRs from cloud agents, 2× more agent users
> than Tab users) and a "factory" metaphor for the developer role in the third era.

## Source Context

- **Type**: blog-post (Cursor official blog, CEO authorship, ~4-minute read, published
  February 26, 2026; categorised as "ideas"; strategic/meta-narrative piece)
- **Author credibility**: Michael Truell is Cursor's co-founder and CEO. This is an
  executive-voice strategic framing piece, not an engineering report. Truell writes from
  direct access to Cursor's internal usage data and product roadmap. The quoted metrics
  (15× growth, 35% PR ratio) are first-party with no external audit, but come from an
  executive with authoritative access to the numbers. The motivational framing ("vast
  majority of development work" within a year) is a forward-looking assertion, not a
  measurement. Treat the metrics as emerging; treat the predictions and framing as
  anecdotal.
- **Scope**: Covers the conceptual three-era taxonomy, Cursor-internal usage metrics
  through February 2026, a qualitative description of how third-era developers work, and
  a brief acknowledgement of remaining challenges. Does NOT cover: harness engineering
  specifics, model architecture, training methodology, pricing, or deployment
  infrastructure. The cloud agent launch referenced ("yesterday's launch") refers to
  Cursor cloud agents going live on or around February 25–26, 2026.

## Extracted Claims

### Claim 1: AI-assisted software development has progressed through three named eras — Tab autocomplete, synchronous agents, and cloud agents

- **Evidence**: Explicit three-era taxonomy stated by Cursor's CEO. The eras are defined
  by the interaction mode and the degree of developer involvement in each code-generation
  step.
- **Confidence**: emerging (first-party narrative framing; the era boundaries align with
  observable product releases and Cursor's own usage data; the framework is authored by a
  primary actor in the space rather than an independent analyst)
- **Quote**: "When we started building Cursor a few years ago, most code was written one
  keystroke at a time. Tab autocomplete changed that and opened the first era of
  AI-assisted coding." ... "Then agents arrived, and developers shifted to directing
  agents through synchronous prompt-and-response loops. That was the second era." ...
  "Now a third era is arriving. It is defined by agents that can tackle larger tasks
  independently, over longer timescales, with less human direction."
- **Our assessment**: The three-era taxonomy is a useful narrative scaffold for the guide.
  The era boundaries are not arbitrary — they correspond to distinct interaction paradigms
  (keystroke-level → conversation-level → task-level), which map to distinct harness
  designs, evaluation needs, and developer skill sets. The framework originates from a
  vendor and reflects Cursor's product strategy, so it should be used descriptively rather
  than prescriptively. The claim that the second era "may not last one [year]" (see Claim
  6) is the most forward-leaning element and the least settled.

### Claim 2: Tab completion's first era lasted nearly two years; the synchronous-agent era may not last one year

- **Evidence**: Specific duration claim with an explicit comparison. The Tab era is
  described as running "nearly two years" (roughly 2023–2025); the synchronous-agent era
  is predicted to be shorter.
- **Confidence**: anecdotal (backward-looking characterisation of the Tab era is
  observable; forward-looking claim about the synchronous-agent era is a prediction)
- **Quote**: "The Tab era lasted nearly two years. The second era, in which most work is
  done with synchronous agents, may not last one."
- **Our assessment**: If accurate, the prediction implies a compressed adoption timeline
  for cloud agents compared to Tab. The compression is plausible given the compounding
  factor: Tab adoption was slowed by user habit inertia (typing is deeply ingrained);
  agent usage growth benefits from Tab having already changed developer habits. The
  specific timing depends heavily on model capability improvements remaining on the
  observed trajectory through 2026.

### Claim 3: Agent usage in Cursor grew 15× in one year and has flipped from 2.5× more Tab users to 2× more agent users

- **Evidence**: Two specific internal metrics with an explicit timeframe.
  - March 2025: "roughly 2.5x as many Tab users as agent users"
  - February 2026: "we now have 2x as many agent users as Tab users"
  - Aggregate: "Agent usage in Cursor has grown over 15x in the last year"
- **Confidence**: emerging (first-party internal metrics from the CEO; no external audit;
  specific quantitative values strengthen the claim relative to qualitative-only
  reporting)
- **Quote**: "Agent usage in Cursor has grown over 15x in the last year"
- **Our assessment**: The 15× growth metric is the single most concrete quantitative
  claim in the source and the most useful for the guide. The ratio flip (2.5× Tab
  advantage → 2× agent advantage) demonstrates that this is not incremental growth —
  it is a category inversion within 12 months. The caveat: "usage" may be measured as
  actions, sessions, users, or some other proxy; the denominator is not defined. The
  directional claim (enormous growth, category flip) is reliable even if the precise
  multiplier has measurement uncertainty.

### Claim 4: Most Cursor users no longer use Tab completion at all; the transformation was catalysed by specific model releases

- **Evidence**: Categorical usage claim ("most Cursor users never touch the tab key")
  plus a named set of model releases as causal drivers.
- **Confidence**: anecdotal (the "most users never touch the tab key" claim is not
  supported by a published percentage; the causal attribution to specific models is the
  CEO's interpretation)
- **Quote**: "Developer habits began to shift, slowly through the summer, then rapidly
  over the last few months with the releases of Opus 4.6, Codex 5.3, and Composer 1.5."
  And: "The transformation has been so complete that today, most Cursor users never touch
  the tab key."
- **Our assessment**: The named model releases (Opus 4.6, Codex 5.3, Composer 1.5)
  provide a specific and verifiable timeline anchor for the adoption inflection. These
  releases are independently observable, and the claim that capability thresholds rather
  than marketing or pricing drove adoption is consistent with the pattern seen in other
  technology adoption inflections. The "most users never touch the tab key" assertion is
  the most dramatic quantitative claim in the source and the most in need of supporting
  data — it could reflect a vocal subset of heavy users or a genuine majority behavior
  shift.

### Claim 5: Synchronous agents are limited to a handful of concurrent sessions because they compete for local machine resources

- **Evidence**: Structural argument about the resource-sharing limitation of local agent
  execution.
- **Confidence**: settled (logically necessary — local machines have fixed CPU, memory,
  and disk; concurrent agent sessions share these; the constraint is architectural, not
  empirical)
- **Quote**: "this form of real-time interaction, combined with the fact that synchronous
  agents compete for resources on the local machine, means it is only practical to work
  with a few at a time"
- **Our assessment**: This claim defines the transition rationale from era 2 to era 3.
  The argument is sound: synchronous agents doing non-trivial work (running tests,
  building code) saturate local resources quickly. The cloud agent design directly
  addresses this by giving each session its own VM. For the guide: this is the clearest
  statement of WHY cloud agents are architecturally necessary, not just preferable —
  parallel execution at scale is physically impossible in the local resource model.

### Claim 6: Cloud agents run on dedicated virtual machines, work over hours, and return reviewable artifacts rather than diffs

- **Evidence**: Explicit product description of how cloud agents differ from synchronous
  agents in their execution model and output format.
- **Confidence**: emerging (vendor-described product behavior; consistent with the
  self-hosted cloud agent architecture described in `blog-cursor-self-hosted-cloud-agents.md`)
- **Quote**: "Cloud agents remove both constraints. Each runs on its own virtual machine,
  allowing a developer to hand off a task and move on to something else." And: "The agent
  works through it over hours, iterating and testing until it is confident in the output,
  and returns with something quickly reviewable: logs, video recordings, and live previews
  rather than diffs."
- **Our assessment**: The shift from "diffs" to "logs, video recordings, and live
  previews" is a key observation about the third-era review workflow. In era 2, the
  developer sees what the agent wrote and approves the change. In era 3, the developer
  sees what the agent did and reviews the outcome — a fundamentally different review
  model that requires different tooling. The "hours" timescale is also important: it
  implies that the developer workflow is asynchronous, matching how teams work with
  human contractors rather than how they pair-program.

### Claim 7: The developer role in the third era shifts to "defining the problem and setting review criteria" — interacting with agents as teammates

- **Evidence**: Explicit characterisation of the developer role change, with three
  specific traits observed in early adopters.
- **Confidence**: anecdotal (qualitative observation from internal Cursor users; the
  "three traits" are described by Truell without citing survey data)
- **Quote**: "The human role shifts from guiding each line of code to defining the problem
  and setting review criteria." And from the three traits section: (1) "Agents write
  almost 100% of their code." (2) "They spend their time breaking down problems,
  reviewing artifacts, and giving feedback." (3) "They spin up multiple agents
  simultaneously instead of handholding one to completion."
- **Our assessment**: The three-trait description is the most practically actionable
  element of the source for the guide. It specifies what the new developer skill set
  looks like: problem decomposition, parallel agent management, and artifact review. The
  framing of agents as "teammates" (from the factory metaphor in Claim 8) rather than
  "tools" has implications for how developers communicate tasks — more like writing a
  brief than writing a prompt.

### Claim 8: Cursor's product reframes from "write code" to "build the factory that creates software" — fleets of agents interacted with as teammates

- **Evidence**: Direct strategic reframing from the CEO. The "factory" metaphor is the
  organising concept for the third-era product vision.
- **Confidence**: anecdotal (CEO's strategic framing; the "factory" metaphor is a
  perspective, not a measurement)
- **Quote**: "As a result, Cursor is no longer primarily about writing code. It is about
  helping developers build the factory that creates their software." And: "This factory is
  made up of fleets of agents that they interact with as teammates: providing initial
  direction, equipping them with the tools to work independently, and reviewing their
  work."
- **Our assessment**: The "factory" metaphor is distinct from the "co-pilot" metaphor
  that dominated era 1 framing. A co-pilot is alongside you at every step; a factory
  produces output autonomously to a specification. The shift in metaphor encodes a shift
  in relationship: developers are not guiding the work step-by-step, they are specifying
  requirements and reviewing output. This has direct implications for how the guide frames
  the engineer's job in chapter discussions of the third-era workflow.

### Claim 9: 35% of Cursor's internal PRs are created by cloud agents operating autonomously in cloud VMs

- **Evidence**: Specific first-party metric cited by the CEO for Cursor's own engineering
  organisation.
- **Confidence**: emerging (first-party metric; specific percentage strengthens the claim;
  no external audit; denominator not defined)
- **Quote**: "Thirty-five percent of the PRs we merge internally at Cursor are now created
  by agents operating autonomously in cloud VMs."
- **Our assessment**: This metric (35% in February 2026) is a key data point for the
  guide's adoption trajectory section. It has a direct successor: `blog-cursor-cloud-agent-lessons.md`
  (May 2026) reports "more than 40% of our PRs come from cloud agents, and growing." The
  progression from 35% → 40%+ over three months is consistent with the "and growing"
  qualifier in the later post and provides a concrete adoption trajectory within one
  organisation. For the guide: cloud agents have crossed the "minority → plurality
  contributor" threshold at Cursor by February 2026, with continued growth through May.

### Claim 10: At industrial scale, environment and test flakiness that a single developer can work around interrupts every agent run — this is the primary remaining challenge

- **Evidence**: Explicit acknowledgement of a structural challenge in third-era adoption,
  stated by the CEO as "a lot of work left."
- **Confidence**: settled (the claim is logically necessary — deterministic environment
  expectations are a known challenge in any parallel test execution environment; this
  claim is independently corroborated by `blog-cursor-continual-harness-improvement.md`
  and `blog-cursor-cloud-agent-dev-environments.md`)
- **Quote**: "There is a lot of work left before this approach becomes standard in
  software development. At industrial scale, a flaky test or broken environment that a
  single developer can work around turns into a failure that interrupts every agent run."
- **Our assessment**: This is the most important practical constraint admitted in the
  source. The amplification effect is real and quantifiable: if a flaky test fails 5% of
  the time and you run 20 agents in parallel, the probability that at least one agent is
  interrupted approaches 65%. Human developers tolerate flakiness through ad-hoc
  workarounds; agents cannot. The implication for teams adopting cloud agent workflows:
  improving test reliability and environment reproducibility is a prerequisite for
  productive parallel agent fleets, not a nice-to-have.

### Claim 11: Within a year of this writing, Truell predicts "the vast majority of development work" will be done by cloud agents

- **Evidence**: CEO's explicit forward-looking prediction.
- **Confidence**: anecdotal (prediction; no supporting methodology; reflects the author's
  strategic belief and product roadmap)
- **Quote**: "A year from now, we think the vast majority of development work will be done
  by these kinds of agents."
- **Our assessment**: The prediction should be treated as the author's belief, not as a
  settled claim. If correct, it implies cloud agents would be generating >50% of code
  contributions across most engineering teams by early 2027. The 35% → 40%+ progression
  within Cursor in three months is consistent with this trajectory within Cursor's
  organisation, but extrapolation to "most development work" across all teams requires
  assumptions about industry-wide adoption that the source does not support. For the
  guide: cite this as the vendor's stated belief, not as a forecast.

## Concrete Artifacts

### Three-Era Taxonomy

```
Three eras of AI-assisted software development
Source: "The third era of AI software development," Michael Truell, Cursor (Feb 26, 2026)

ERA 1: Tab autocomplete
  Interaction: keystroke-by-keystroke
  Developer role: typing, accepting suggestions
  Duration: ~2 years (approx. 2023–2025)
  Key characteristic: "identifying where low-entropy, repetitive work could be automated"

ERA 2: Synchronous agents
  Interaction: prompt-and-response loops; developer in loop at every step
  Developer role: directing, reviewing each output
  Duration: "may not last one [year]"
  Constraint: "compete for resources on the local machine"; practical to run "a few at a time"

ERA 3: Cloud agents (arriving Feb 2026)
  Interaction: task hand-off; developer reviews artifacts asynchronously
  Developer role: "defining the problem and setting review criteria"
  Execution: dedicated VM per agent; "iterating and testing until it is confident"
  Output: "logs, video recordings, and live previews rather than diffs"
  Scale: "running agents in parallel practical"
```

### Cursor Internal Adoption Metrics (February 2026)

```
Cursor adoption metrics — "The third era of AI software development" (Feb 26, 2026)

Agent usage growth:
  March 2025:    2.5× more Tab users than agent users
  Feb 2026:      2× more agent users than Tab users
  Net change:    ~15× agent usage growth in 12 months
  Tab usage:     "most Cursor users never touch the tab key"

PR origin (Cursor internal):
  Feb 26, 2026:  35% of merged PRs created by cloud agents autonomously
  May 21, 2026:  40%+ of PRs from cloud agents (blog-cursor-cloud-agent-lessons.md)
  Trend:         "and growing"

Model releases cited as adoption catalysts:
  - Opus 4.6
  - Codex 5.3
  - Composer 1.5
```

### Third-Era Developer Traits (Cursor Internal Observation)

```
Traits of developers adopting cloud agent workflows
Source: "The third era of AI software development," Michael Truell, Cursor (Feb 26, 2026)

1. "Agents write almost 100% of their code."
2. "They spend their time breaking down problems, reviewing artifacts, and giving feedback."
3. "They spin up multiple agents simultaneously instead of handholding one to completion."

Role shift summary:
  Was: "guiding each line of code"
  Now: "defining the problem and setting review criteria"

Agent-as-teammate model:
  - "providing initial direction"
  - "equipping them with the tools to work independently"
  - "reviewing their work"
```

### Cloud Agent vs. Synchronous Agent Comparison

```
Comparison: synchronous agents (era 2) vs. cloud agents (era 3)
Source: "The third era of AI software development," Michael Truell, Cursor (Feb 26, 2026)

                     Synchronous Agents         Cloud Agents
---------------------------------------------------------------------------
Execution location   Local machine              Dedicated cloud VM
Concurrency          "a few at a time"          Many in parallel (practical)
Developer mode       Real-time interaction      Hand off and move on
Session length       Prompt-response loops      "hours" of autonomous work
Output format        Diffs                      "logs, video recordings,
                                                 and live previews"
Review approach      Inspect the change         Inspect the outcome
Resource contention  "compete for resources     Isolated per session
                      on the local machine"
```

## Cross-References

- **Corroborates**: `blog-cursor-cloud-agent-lessons.md` — That post (May 2026) reports
  "more than 40% of our PRs come from cloud agents, and growing." This source (February
  2026) reports 35%. The two figures together establish a concrete adoption trajectory
  within Cursor: 35% (Feb) → 40%+ (May), consistent with the "and growing" qualifier.
  Both posts also corroborate on the Claim 6 architecture (agents on VMs, working
  autonomously). The cloud-agent-lessons post provides the deeper infrastructure
  explanation (Temporal, three-component decoupling) that this strategic piece does not
  cover.

- **Corroborates**: `blog-cursor-self-hosted-cloud-agents.md` — That post confirms the
  cloud VM per-agent execution architecture described here in Claim 6. Specifically, it
  documents per-session VM isolation and the outbound-only HTTPS worker architecture.
  The self-hosted post is the technical companion to this strategic framing piece for
  understanding HOW the cloud agent architecture works.

- **Corroborates**: `blog-cursor-continual-harness-improvement.md` — Claim 12 in that
  note documents the harness evolution from static context toward dynamic, and notes the
  ongoing need for environment reliability improvements. This source's Claim 10 (flaky
  tests interrupt every agent run at industrial scale) is the CEO-level statement of the
  same challenge that the harness engineering post identifies at the implementation level.
  Both converge on environment reliability as the primary scaling barrier.

- **Corroborates**: `blog-cursor-cloud-agent-dev-environments.md` Claim 1 ("An agent
  that can write code but can't run tests, query services, or reach APIs cannot close the
  loop on its work") — That post provides the detailed environment configuration framework
  that addresses the scaling challenge admitted in Claim 10 here. The third-era post
  raises the problem (flaky environments interrupt every run); the dev-environments post
  provides the tooling solution.

- **Extends**: `blog-cursor-composer2-technical-report.md` — That technical report covers
  the training and architecture of Composer 1.5 and Composer 2. This source names
  Composer 1.5 as one of three model releases that catalysed the second-to-third-era
  transition (Claim 4). The third-era article is the product/adoption narrative that
  explains what Composer 1.5's capabilities unlocked; the technical report explains how
  Composer 1.5 and Composer 2 were built.

- **Extends**: `blog-cursor-multi-agent-kernels.md` — That post documents a 3-week
  autonomous multi-agent GPU kernel optimisation run (the "spin up multiple agents in
  parallel" pattern described in Claim 7's developer traits). The kernel optimisation
  system is a concrete existence proof of the third-era workflow described abstractly
  here. It corroborates the feasibility of extended autonomous agent operation (weeks)
  that Claim 6 ("over hours") describes as characteristic of the third era.

- **Novel**: The following are new to the corpus:
  - **The three-era taxonomy as a named framework**: No other source provides a named
    three-tier schema (Tab → synchronous agents → cloud agents) with this level of
    editorial authority from a primary vendor. This is the first corpus source to position
    the eras as a specific historical sequence rather than describing current state.
  - **15× agent usage growth metric**: No other source documents Cursor's agent usage
    growth rate over the 12-month period ending February 2026. The ratio flip from
    2.5× Tab advantage to 2× agent advantage is unique to this source.
  - **Tab completion declared functionally obsolete for most users**: The claim that
    "most Cursor users never touch the tab key" is the strongest statement in the corpus
    that era 1 tooling is effectively deprecated in practice, not just supplemented.
  - **Specific model release catalysts named**: Opus 4.6, Codex 5.3, and Composer 1.5
    as the named inflection drivers for third-era adoption are cited in no other corpus
    source in this specific context.
  - **"Factory" metaphor for developer role**: The "factory" framing (developer builds
    the system that produces software, rather than writing software directly) is a new
    conceptual frame not used in any other source note. It is distinct from "co-pilot"
    (era 1–2 framing) and "orchestrator" (common in multi-agent literature).
  - **Flaky test amplification at agent fleet scale**: The explicit quantification of
    the environment flakiness problem ("single developer can work around" → "interrupts
    every agent run") as the primary scaling challenge is framed more starkly here than
    in any other corpus source.

## Guide Impact

- **Chapter 01 or 00 (Introduction / Historical Context)**: The three-era framework
  (Claim 1) is the clearest narrative scaffold in the corpus for explaining why AI-native
  engineering is different from prior AI coding assistance. It should appear early in the
  guide as a framing device — not as vendor marketing, but as a practical taxonomy with
  concrete era boundaries (named model releases, specific duration, observable interaction
  mode). The "factory" metaphor (Claim 8) is the companion conceptual frame for the
  guide's "what is AI-native engineering?" introduction.

- **Chapter 03 or 05 (Agent Orchestration / Autonomous Systems)**: The 15× growth metric
  (Claim 3) and the 35% PR ratio (Claim 9), together with the `blog-cursor-cloud-agent-lessons.md`
  40%+ figure, form a progression that quantifies the adoption trajectory. Add a data-
  point timeline: Feb 2026 (35%) → May 2026 (40%+). This gives the guide a concrete
  grounding for the claim that cloud agents are already operating at majority-contribution
  scale within leading engineering teams, not just in prototype form.

- **Chapter 03 or 05 (Autonomous Systems — developer role)**: The three-trait description
  of third-era developers (Claim 7: agents write ~100% of code; developer decomposes
  problems, reviews artifacts, runs parallel agents) is the most concrete statement in
  the corpus of what the developer skill set looks like in the third era. This should
  anchor any section on how developer workflows change. The shift from "guiding each line
  of code" to "defining the problem and setting review criteria" is the guide's core thesis
  stated in a single sentence by the vendor who has the most usage data to back it up.

- **Chapter 02 (Harness Engineering — environment reliability prerequisite)**: Claim 10
  (flaky test amplification at fleet scale) should be cited as the motivation for the
  environment quality sections. The causal chain is: cloud agent fleet adoption → flakiness
  that a single human works around becomes a fleet-wide failure → environment reliability
  becomes a first-class engineering concern. Currently `blog-cursor-continual-harness-improvement.md`
  and `blog-cursor-cloud-agent-dev-environments.md` document the solution; this source
  provides the motivating problem statement from the CEO.

- **Chapter 04 (Context Engineering — cloud agent review workflow)**: Claim 6 (artifacts
  and previews as review medium) introduces a review workflow that differs from both
  code review (reading diffs) and test review (reading pass/fail). "Logs, video
  recordings, and live previews" represent a new review artifact class. If the guide
  covers review workflows for agent output, this source provides the canonical description
  of what third-era artifacts look like and why they are the right format for parallel
  agent output (Claim 6: "give you enough context to evaluate output without
  reconstructing each session from scratch").

## Extraction Notes

- Source is a CEO blog post — authoritative on strategy and internal metrics, but not
  on implementation details. All implementation specifics (VM architecture, execution
  infrastructure) are better sourced from companion technical posts
  (`blog-cursor-self-hosted-cloud-agents.md`, `blog-cursor-cloud-agent-lessons.md`).
- The article is short (~700 words in the main body). Each paragraph was read in full.
  There are no sub-pages or linked technical companions within this post itself.
- The "yesterday's launch" reference pins the article date to February 26, 2026 and
  confirms the cloud agent product launched on or around February 25, 2026.
- The 35% PR metric in the body matches "more than one-third" in the opening — these
  are consistent statements of the same figure (35% > 1/3 ≈ 33.3%).
- No contradictions to file: the 35% figure (February) and 40%+ figure (May, in
  `blog-cursor-cloud-agent-lessons.md`) are consistent growth rather than contradictory
  claims. The "factory" framing is complementary to, not in conflict with, multi-agent
  coordination patterns described in other corpus sources.
- The three named model releases (Opus 4.6, Codex 5.3, Composer 1.5) appear in this
  source as causal drivers. Opus 4.6 and Composer 1.5 are discussed technically in
  `blog-cursor-composer2-technical-report.md` and `blog-anthropic-opus47-best-practices.md`;
  their capabilities provide a basis for evaluating the causal attribution, though the
  attribution itself remains the CEO's interpretation.
