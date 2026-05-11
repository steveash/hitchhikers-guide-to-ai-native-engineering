---
source_url: https://cursor.com/blog/third-era
source_type: blog-post
title: "The third era of AI software development"
author: Michael Truell (Cursor / Anysphere)
date_published: 2026-02-26
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#141"
---

# The third era of AI software development (Michael Truell, Cursor)

> A first-party strategic synthesis from Cursor's CEO framing the evolution of AI-assisted development as three eras — Tab autocomplete, synchronous agents, cloud agents — anchored by internal deployment metrics (15× agent growth, 35% of merged PRs from cloud agents) and a forward claim that the majority of development work will be done by autonomous cloud agents within a year.

## Source Context

- **Type**: blog-post (Cursor / Anysphere official blog, ~700 words, published February 26, 2026; written by Michael Truell, Cursor CEO and co-founder)
- **Author credibility**: Michael Truell co-founded Cursor and is its CEO; this is first-person strategic commentary from someone with direct access to Cursor's internal usage data. The metrics cited (15× agent growth, 35% of PRs from agents) are first-party production numbers — Truell has no reason to under-report and every incentive to be accurate, but they are not independently audited. Treat metric claims as emerging. The "eras" framework is the author's own narrative synthesis; treat it as the most credible possible insider interpretation of Cursor's trajectory.
- **Scope**: Covers the macro evolution of AI-assisted coding as three eras, internal Cursor adoption metrics, the constraints of synchronous agents vs. cloud agents, the artifact/preview model for evaluating agent output, and the emergent developer workflow in the third era. Does NOT cover: model internals, training methodology, pricing, API details, or how to configure the product. This is a 700-word strategic post, not a technical deep-dive.

## Extracted Claims

### Claim 1: The evolution of AI-assisted development follows three eras: Tab autocomplete (era 1), synchronous agents (era 2), and cloud agents that operate independently over longer timescales (era 3)

- **Evidence**: Truell's first-person narrative of Cursor's product history, grounded in the adoption metrics described in Claims 2–4. The "three eras" framing synthesizes the internal trajectory Cursor has observed across its user base.
- **Confidence**: emerging (the framework is analytically useful and grounded in real metrics; the boundaries between eras are necessarily blurry in practice)
- **Quote**: "Then agents arrived, and developers shifted to directing agents through synchronous prompt-and-response loops. That was the second era. Now a third era is arriving. It is defined by agents that can tackle larger tasks independently, over longer timescales, with less human direction."
- **Our assessment**: The three-eras framework is the most durable contribution of this post for the guide. It provides a shared vocabulary for discussing where AI-assisted development has been, where it is, and where it's going. The specific trigger for the transition from era 2 to era 3 is named precisely — "the releases of Opus 4.6, Codex 5.3, and Composer 1.5" — which means this is not a gradual drift but a step-change tied to identifiable model releases. For the guide: the eras framework is a pedagogical anchor for contextualizing practitioner patterns across chapters.

### Claim 2: Most Cursor users no longer touch the tab key; the user ratio flipped from 2.5× more Tab users than agent users (March 2025) to 2× more agent users than Tab users now

- **Evidence**: First-party behavioral measurement of Cursor's active user base. The ratio inversion is a clean signal: Tab and agent usage are substitutes, and the substitution is now complete in the opposite direction from where it started.
- **Confidence**: emerging (first-party behavioral data; the specific numbers are precise and falsifiable; no external validation)
- **Quote**: "In March 2025, we had roughly 2.5x as many Tab users as agent users. Now, that is flipped: we now have 2x as many agent users as Tab users."
- **Our assessment**: The flip from 2.5×-Tab to 2×-agent in under one year is a strong directional signal of adoption velocity. The precision (2.5× vs. 2×) and the time anchor (March 2025) are both details that add credibility — this reads as a real number pulled from an analytics dashboard, not a rounded narrative figure. For the guide: this metric quantifies what "the paradigm shift has happened" means in practice. It is not anecdote; it is a ratio that flipped.

### Claim 3: Agent usage in Cursor has grown over 15× in the last year

- **Evidence**: First-party internal growth metric called out explicitly in the article (formatted as a "Metric" callout). Corroborated directionally by the user ratio inversion described in Claim 2.
- **Confidence**: emerging (first-party production metric; consistent with the ratio inversion evidence; not independently audited)
- **Quote**: "Agent usage in Cursor has grown over 15x in the last year."
- **Our assessment**: 15× over one year is extraordinary growth — it implies this is not incremental adoption but a behavioral category switch. When combined with Claim 2 (user ratio inversion), the picture is: (a) the total number of agent users grew massively, and (b) they now outnumber Tab users by 2:1. For practitioners evaluating when to invest in agentic tooling: the adoption velocity at Cursor is the canary — their data comes first.

### Claim 4: More than one-third of the PRs Cursor merges internally are now created by cloud agents operating autonomously

- **Evidence**: First-party production metric from Cursor's own engineering organization. Reported twice in the article at slightly different precision levels ("more than one-third" in the intro; "thirty-five percent" in the "Shift is Underway" section).
- **Confidence**: emerging (first-party data; no external audit; the consistency of the two figures adds credibility — both map to ~35%)
- **Quote**: "Thirty-five percent of the PRs we merge internally at Cursor are now created by agents operating autonomously in cloud VMs."
- **Our assessment**: 35% is the clearest internal productivity benchmark in the entire Cursor corpus. It answers "what does the third era actually look like in numbers?" Cursor itself — a company with strong incentive to show AI works — has 35% of its code shipped via cloud agents. For practitioners: this is the current frontier for an engineering organization that is deliberately pushing the boundary. It is not "someday"; it is "right now, at the team that builds the product."

### Claim 5: The Tab era lasted nearly two years; the synchronous agent era may not last one year

- **Evidence**: Truell's reading of adoption velocity data: Tab dominated from late 2022 through mid-2024; synchronous agents rose through 2025; cloud agents appeared in late 2025. The accelerating tempo is the claim.
- **Confidence**: anecdotal (directional assessment by an insider; the time estimates are Truell's interpretation of the data, not a formally measured inflection point)
- **Quote**: "The Tab era lasted nearly two years. The second era, in which most work is done with synchronous agents, may not last one."
- **Our assessment**: If accurate, the implication is significant: each era is shorter than the last. Practitioners who are just now adopting synchronous agents may find the window to optimize that workflow is shorter than the Tab window was. For the guide: this framing supports urgency around investing in cloud/background agent patterns now rather than perfecting synchronous workflows that may be transitional.

### Claim 6: Synchronous agents are resource-constrained to a few at a time; cloud agents on dedicated VMs remove both the attention constraint and the local resource constraint

- **Evidence**: Explicit description of the two constraints of synchronous agents: (1) they require the developer to stay "in the loop at every step," and (2) they "compete for resources on the local machine." Cloud agents resolve both.
- **Confidence**: emerging (architectural reasoning; the constraint analysis is Truell's own framing but grounded in product design choices)
- **Quote**: "this form of real-time interaction, combined with the fact that synchronous agents compete for resources on the local machine, means it is only practical to work with a few at a time."
- **Our assessment**: This is the clearest articulation in the corpus of *why* cloud agents are architecturally superior for parallel workloads. The two constraints (attention and resources) map to different product design challenges: the attention constraint drives the need for artifact-based review (Claim 7); the resource constraint drives the need for cloud VMs. Both need to be solved simultaneously. For the guide: this two-constraint framing should anchor the chapter on cloud/background agents — you cannot parallelize synchronous agents beyond a handful.

### Claim 7: Cloud agents return logs, video recordings, and live previews rather than diffs — making parallel operation practical by giving reviewers enough context to evaluate output without reconstructing each session

- **Evidence**: Product design description of what Cursor's cloud agents actually return. The artifact types (logs, video recordings, live previews) are specifically named as the alternatives to diffs.
- **Confidence**: emerging (product description; consistent with the self-hosted cloud agents note which describes dedicated VMs with terminal + browser + desktop environments)
- **Quote**: "The agent works through it over hours, iterating and testing until it is confident in the output, and returns with something quickly reviewable: logs, video recordings, and live previews rather than diffs."
- **Our assessment**: The shift from diff-as-output to artifact-as-output is the key product design innovation of the third era. A diff requires a reviewer to mentally reconstruct "what problem was being solved and why this change solves it." Logs + video + live preview make the agent's reasoning and results self-evident. For the guide: artifact-first agent output design should be treated as a first-class harness engineering pattern — it is what makes review tractable at scale.

### Claim 8: The human role in the third era shifts from guiding each line of code to defining the problem and setting review criteria

- **Evidence**: Truell's characterization of how third-era developers at Cursor now work, supported by the three traits listed in Claim 9.
- **Confidence**: emerging (insider observation; consistent with the 35% PR creation metric — humans are reviewing, not writing)
- **Quote**: "The human role shifts from guiding each line of code to defining the problem and setting review criteria."
- **Our assessment**: This is the single most important sentence in the article for the guide. It defines what human developers actually *do* in the third era. The skills that become primary: problem decomposition, task specification, criteria articulation, artifact review. The skills that become secondary: line-by-line coding, incremental prompting, debugging individual tool calls. For the guide: this should anchor the chapter on team workflow and developer role — not as a future possibility, but as a present reality at Cursor's own engineering org.

### Claim 9: Third-era developers write almost 100% agent code, spend time on problem decomposition and artifact review rather than coding, and spin up multiple agents simultaneously

- **Evidence**: Three concrete behavioral traits observed in the Cursor employees who have adopted third-era workflows. These are first-hand observations by Truell of colleagues in his own organization.
- **Confidence**: anecdotal (small internal sample; Cursor employees pushing the frontier are not representative of typical developers)
- **Quote**: "1. Agents write almost 100% of their code. 2. They spend their time breaking down problems, reviewing artifacts, and giving feedback. 3. They spin up multiple agents simultaneously instead of handholding one to completion."
- **Our assessment**: The three traits together constitute a complete behavioral profile of the third-era developer. Each trait is a non-obvious inversion of current practice: (1) "almost 100%" vs. the ~30–50% AI contribution today; (2) reviewing artifacts vs. writing code; (3) multiple simultaneous vs. one agent at a time. These are aspirational descriptors for Cursor's frontier users, not average developer behavior. For the guide: these three traits can serve as a "maturity model" for teams to assess where they are in the transition.

### Claim 10: At industrial scale, a flaky test or broken environment that a single developer can work around becomes a failure that interrupts every agent run

- **Evidence**: Truell's observation of the operational challenges of scaling cloud agents within Cursor's own engineering organization. Named as one of the key unsolved problems.
- **Confidence**: emerging (first-party operational observation; logical extension of the parallelization claim — any per-run failure multiplies with agent count)
- **Quote**: "At industrial scale, a flaky test or broken environment that a single developer can work around turns into a failure that interrupts every agent run."
- **Our assessment**: This is the most practically important warning in the article. It names an underappreciated second-order cost of scaling cloud agents: the reliability requirements for CI, test infrastructure, and development environments become dramatically stricter. A 5% flaky test rate is tolerable for a human developer (they re-run); it is catastrophic for a 100-agent fleet (5 agents fail per 100 runs). For the guide: environment reliability should be treated as a prerequisite for cloud agent adoption, not an afterthought. This is the "boring infrastructure problem" that blocks the exciting agentic future.

## Concrete Artifacts

### The Three Eras Framework

```
# AI-Assisted Development: Three Eras (Michael Truell, Cursor, February 2026)

ERA 1: Tab Autocomplete
  Duration: ~2 years (roughly 2022–2024)
  Mechanism: Inline completion; one keystroke at a time → model-assisted
  Role of developer: Primary author; AI is a fast typist
  Bottleneck: Low-entropy, repetitive tasks
  Quote: "Tab excelled at identifying where low-entropy, repetitive work
          could be automated."

ERA 2: Synchronous Agents
  Duration: <1 year (2025; still transitioning)
  Mechanism: Prompt-and-response loops; developer in the loop at each step
  Constraints: (1) Developer must attend each step; (2) Agents compete
               for local machine resources → practical limit: a few at a time
  Role of developer: Director; agent executes, developer watches
  Trigger: Rapid capability increase with Opus 4.6, Codex 5.3, Composer 1.5

ERA 3: Cloud Agents (arriving now)
  Duration: Unknown; may supersede era 2 in under a year
  Mechanism: Agents run on dedicated VMs, work over hours, return artifacts
  Output type: Logs, video recordings, live previews — NOT diffs
  Role of developer: Problem definer + review criteria setter
  Enabler: Dedicated VMs per agent; artifact-based output review
  Internal Cursor metrics (February 2026):
    - 35% of merged PRs created by cloud agents
    - Agent usage: 15× growth over last year
    - User ratio: 2× more agent users than Tab users (was 2.5× more Tab users in March 2025)
```

### Developer Behavioral Profile: Third Era

```
# Third-era developer traits (Cursor internal observations, February 2026)

1. AGENT AUTHORSHIP RATE
   "Agents write almost 100% of their code."

2. TIME ALLOCATION
   "They spend their time breaking down problems, reviewing artifacts,
    and giving feedback."
   (NOT: writing code, debugging tool calls, handholding prompts)

3. PARALLELISM
   "They spin up multiple agents simultaneously instead of handholding
    one to completion."
```

### Industrial Scale Reliability Warning

```
# Cloud agent infrastructure requirement (Cursor, February 2026)

PROBLEM
  "At industrial scale, a flaky test or broken environment that a single
   developer can work around turns into a failure that interrupts every
   agent run."

IMPLICATION
  Flaky test rate × agent fleet size = compounded interruption rate
  Example: 5% flaky test rate × 100 agents = 5 interrupted runs per batch
           A human works around this; an agent stops and needs intervention

PREREQUISITE
  Reliable CI, test infrastructure, and development environments are
  non-negotiable before scaling cloud agents — not a nice-to-have.
```

## Cross-References

- **Corroborates**: `blog-cursor-self-hosted-cloud-agents.md` — The self-hosted cloud agents post (March 2026, one month later) is the product announcement of the same cloud agents this article describes. Claim 4 here (35% of Cursor PRs from cloud agents) is independently stated in both sources, providing convergent first-party evidence. The Truell article provides the strategic framing; the Bazzi article provides the enterprise deployment architecture.

- **Corroborates**: `blog-cursor-continual-harness-improvement.md` Claim 13 — The "software factory" framing in both posts is consistent. This article: "Cursor is no longer primarily about writing code. It is about helping developers build the factory that creates their software." The continual-harness post: "This process is part of the way we're instantiating an automated 'software factory' for our agent harness." Both use the factory metaphor for the same abstraction: developers as factory builders, not workers.

- **Corroborates**: `blog-cursor-better-models-ambitious-work.md` Claim 2 — That post found a 4–6 week lag before developers shifted to more complex tasks after a model upgrade. The "slowly through the summer, then rapidly over the last few months" adoption pattern described here is consistent: the slow summer period corresponds to the discovery-and-reorientation lag; the rapid acceleration corresponds to workflows that have been reoriented around third-era patterns.

- **Corroborates**: `blog-cursor-composer2-technical-report.md` — The technical report (March 2026) provides the training details for Composer 2, which is the next-generation model after Composer 1.5. This article names Composer 1.5 as one of the model releases triggering the era-2→era-3 transition. The 37% relative improvement Composer 2 achieved over Composer 1.5 (Claim 4 in the technical report) supports why the capability jump warranted a new "era" designation.

- **Corroborates**: `blog-cursor-multi-agent-kernels.md` Claim 9 — The kernel optimization post's explicit framing that the system was "compute-limited rather than capability-limited" when running 235 problems on 27 GPUs directly corroborates the constraint analysis here: parallel agents are resource-constrained, not capability-constrained. The cloud-VM-per-agent architecture (Claim 6 here) is the product-level solution to the same constraint.

- **Extends**: `blog-cursor-self-hosted-cloud-agents.md` — The self-hosted post addresses enterprise deployment architecture. This article provides the strategic context that motivates enterprise investment in self-hosted cloud agents: the third era is already here inside Cursor's own engineering org (35% of PRs), and the adoption window for synchronous-agent workflows may be less than a year. Enterprise teams that are still evaluating synchronous agents should know the frontier is already past that.

- **Extends**: `blog-cursor-continual-harness-improvement.md` Claim 12 — That post describes Cursor's harness evolving from heavy static context toward dynamic tool-fetched context. The third-era framing here adds the macro context: the harness simplification mirrors the product simplification — as agents become more capable (era 3), both the harness and the developer workflow simplify. Static context components and synchronous handholding are both signs of era-2 workarounds that become unnecessary.

- **Contradicts**: None identified. The 35% PR-from-agent figure is internally consistent across Cursor's corpus (stated here and consistent with `blog-cursor-self-hosted-cloud-agents.md`). The era framing is novel but does not conflict with any existing note's claims.

- **Novel**: Compared to existing corpus:
  - **The three-eras framework** as a named, metrics-grounded narrative for the evolution of AI-assisted development: no other corpus source provides this level of structured periodization with internal data backing each transition.
  - **35% of merged PRs from cloud agents** as a current production metric: the most specific and credible internal adoption metric in the corpus for autonomous coding agents. (The `blog-cursor-self-hosted-cloud-agents.md` note describes the product; this note provides the first-person CEO-level metric.)
  - **15× agent usage growth over one year**: the first corpus data point quantifying the growth velocity of agent-mode adoption at a major AI coding tool.
  - **User ratio inversion** (2.5× Tab-to-agent → 2× agent-to-Tab): the clearest single metric showing that the behavioral center of gravity at Cursor has permanently shifted to agents over Tab.
  - **Artifact-based output as the key UX unlock for parallelism**: the claim that logs + video + previews (not diffs) make parallel agent review tractable is the first corpus articulation of this specific design principle.
  - **Industrial-scale reliability requirement**: the observation that flaky tests/broken environments that humans work around become per-run blockers at scale is a practical consequence of parallelism not described elsewhere in the corpus.

## Guide Impact

- **Chapter 03 (Agent Orchestration — era framing)**: Add the three-eras framework as the opening context for why agent orchestration matters. The Truell periodization grounds the chapter in a concrete, data-backed narrative: Tab was era 1 (~2 years), synchronous agents are era 2 (<1 year), cloud agents are era 3. This prevents the "why does this matter?" problem in technical chapters. Cite the 15× growth and user-ratio inversion as the quantitative evidence that the transition is underway, not hypothetical.

- **Chapter 04 (Autonomous Systems — constraints of synchronous vs. cloud agents)**: Use Claim 6 to structure the chapter's core design rationale. Synchronous agents have two fundamental constraints (attention bottleneck, local resource contention) that cloud agents solve structurally. The two-constraint framing (attention + resources) is crisper than any existing chapter explanation. Add Claim 7 (artifact output model) as the enabling UX design pattern: without artifact-based output, parallel review is not tractable.

- **Chapter 04 (Autonomous Systems — environment reliability as prerequisite)**: Add Claim 10 as a top-level prerequisite for cloud agent adoption. Currently the corpus has no strong statement about CI/environment reliability as a cloud agent *blocker*. This claim should be added before the "how to build cloud agents" content: "Before scaling cloud agents, eliminate flaky tests and broken environments. What a human works around, an agent cannot." Pair with the failure-report corpus entries (`failure-sukit-parallel-session-ceiling.md`, `failure-hooks-enforcement-2k.md`) as additional evidence.

- **Chapter 05 (Workflows & Scaling — developer role evolution)**: Claim 8 (human role shift) and Claim 9 (third-era behavioral traits) should anchor the chapter on developer workflow transformation. These claims define what developers *do* in the third era: define problems, set review criteria, review artifacts, spin up multiple agents simultaneously. This is more concrete than "AI will change developer work" — it names the specific skills that become primary. The three traits in Claim 9 could become a maturity self-assessment for teams.

- **Chapter 05 (Workflows & Scaling — internal metrics as adoption benchmarks)**: Claim 4 (35% of PRs from cloud agents at Cursor) provides the best available benchmark for what "high-adoption third-era development" looks like numerically. Teams assessing their own adoption can compare to this number. Add alongside `research-anthropic-ai-transforming-work.md` data for a multi-source picture of AI contribution rates.

## Extraction Notes

- Article is ~700 words with no sub-pages or linked technical content to follow. Read in full. The source is a strategic opinion piece by the CEO, not a technical post — it is light on implementation details but high on first-party metrics.
- The "15× agent usage" metric is presented as a callout box in the article ("**Metric:**"), distinct from the surrounding prose. It is a production metric, not a directional claim.
- The article was published alongside a product launch ("yesterday's launch of Cursor cloud agents") — it was the CEO's strategic framing post for the cloud agents announcement. The timing adds credibility to the internal metrics (published at launch, not retrospectively) and also means the "35%" figure was current as of February 26, 2026.
- No contradictions to file: all claims are consistent with or extend existing corpus notes.
- The author's prediction ("A year from now, we think the vast majority of development work will be done by these kinds of agents") was not extracted as a primary claim given it is forward-looking and unverified. It is worth noting as a documented forecast for tracking against 2027 evidence.
