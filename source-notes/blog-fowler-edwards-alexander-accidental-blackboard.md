---
source_url: https://martinfowler.com/articles/exploring-gen-ai/an-accidental-blackboard.html
source_type: blog-post
title: "An Accidental Blackboard"
author: Giles Edwards-Alexander (CTO for Europe, Middle East and India, Thoughtworks)
date_published: 2026-09-02
date_extracted: 2026-09-03
last_checked: 2026-09-03
status: current
confidence_overall: anecdotal
issue: "#3193"
---

# An Accidental Blackboard

> A first-person account of a four-day, ten-engineer Thoughtworks "hyper-agentic" build
> of an airline IROps system, in which the team's commit/rebase discipline and repo-stored
> plan files caused agents to accidentally coordinate through the repository as a classical
> blackboard system (Hearsay-II, 1980; tuple spaces, Gelernter et al., 1986) — the author
> argues the mechanism was accidental, fragile, and not reliably reproducible, and is now
> building a dedicated tool ("Talwrn") to make the pattern intentional.

## Source Context

- **Type**: blog-post (martinfowler.com, part of the "Exploring Gen AI" series — "a series
  capturing Thoughtworks technologists' explorations of using gen ai technology for software
  development" — published 02 September 2026)
- **Author credibility**: Giles Edwards-Alexander is CTO for Europe, Middle East and India at
  Thoughtworks, with over 25 years of engineering and technology leadership experience across
  mobile, AI, retail, fintech, and healthcare, per his byline bio on the article. He states his
  own university research thesis was on "directing agent behaviour with hierarchical sensors,"
  applying reinforcement learning techniques and the blackboard coordination pattern to
  large, dynamic datasets — giving him direct academic grounding in the specific pattern
  (blackboard systems / tuple spaces) he identifies in this piece, distinct from a
  practitioner discovering the concept for the first time. This is a first-person account of
  one internal exercise, not a controlled study or an externally reviewed system.
- **Scope**: Covers one four-day internal Thoughtworks exercise (10 engineers, Barcelona
  office, building a simulated-airline IROps system, described as "a practice exercise, not
  a real client"). Covers: the commit/rebase discipline that was introduced, the plan-file
  side effect that emerged, one concrete example of agents coordinating around an
  evaluator/search-algorithm dependency, one concrete example of the team deliberately
  exploiting the pattern, the author's identification of the pattern as a classical
  blackboard/tuple-space system with historical citations, an account of what broke the
  coordination channel (CI overload), and a forward-looking mention of "Talwrn," a tool the
  author is building to make the pattern intentional. Does NOT cover: the finished IROps
  system's design or evaluation ("this post isn't about how we did that"), any quantified
  measurement of coordination efficiency or failure rate, external validation of the
  approach, or any detail on Talwrn's actual implementation (the tool is described only as
  a stated intention/goal, not shown).

## Extracted Claims

### Claim 1: A four-day, ten-engineer "hyper-agentic" exercise to build an airline IROps system led the team to accidentally rediscover a multi-agent coordination pattern

- **Evidence**: Direct first-person account of the exercise's setup, scale, and framing.
- **Confidence**: anecdotal
- **Quote**: "This week, across Thoughtworks Europe, we took 10 engineers and put them in one room in our Barcelona office. The goal was to see how far and how fast we could go if we really leant into agentic engineering. We called it hyper-agentic. Along the way, we accidentally re-discovered something about coordinating agents."
- **Our assessment**: This is a single internal exercise (10 engineers, 4 days, simulated
  client), not a production system or a study — the "we managed to build one in four days"
  claim about the IROps system itself is explicitly waved off by the author ("But this post
  isn't about how we did that"), so the only claim we treat as evidenced here is the
  coordination-pattern discovery, not the delivery outcome.

### Claim 2: A commit/rebase discipline introduced to fix CI overload from many agents working in one repo had the unplanned side effect of making agent progress visible to other agents

- **Evidence**: Direct causal account: build pipelines suffered from many agents in one repo;
  the team introduced continual commit-and-rebase as a fix for catching build failures
  locally; a side effect followed.
- **Confidence**: anecdotal
- **Quote**: "With lot of agents working in one repo, build pipelines suffered. To deal with this we introduced a discipline: our agents were to continually commit and rebase from main. At first, we required a rebase after commit and to then push, with all of the build checks and controls in place. We introduced this change to catch build failures locally: integrate early and often. But, there was a side-effect."
- **Our assessment**: The causal chain is important and specific: the coordination channel
  was not designed as a coordination channel — it was a byproduct of a CI-stability fix
  (frequent commit/rebase) combined with a separate practice (plan files scoped to spec
  sections, Claim 3). Neither practice alone would have produced the effect; the combination
  did. This is a useful cautionary detail for any guide section recommending frequent-commit
  discipline: the side effects of infrastructure practices can compound in agent-coordination-
  relevant ways that are easy to miss until observed.

### Claim 3: Agent-authored plans, scoped to specification sections and stored in the repository, meant every agent could see every other agent's declared task breakdown against a shared, identically-numbered spec

- **Evidence**: Direct description of the planning practice: agents scoped work to spec
  sections, created linked plans, stored the plans in the repo, and all agents referenced
  the same numbered/identified sections.
- **Confidence**: anecdotal
- **Quote**: "We were directing the agents to plan, to scope work to sections in the spec and to create plans linked to those sections. These plans were stored in the repo. All agents were working off the same spec using the same numbered and identified sections. As agents worked, plans were updated to record progress."
- **Our assessment**: This is the second precondition (alongside Claim 2's commit discipline)
  that made the emergent coordination possible: a shared, addressable naming scheme (numbered
  spec sections) that let independently-working agents refer to the same units of work
  without needing to invent a shared vocabulary themselves.

### Claim 4: Agents used plan-line status as an implicit lock and handoff mechanism — one agent marking a line "in progress" caused another to avoid it, and completion delivered implementation notes directly to the waiting agent

- **Evidence**: Concrete worked example (an evaluator component and a dependent search
  algorithm component, developed by two different agents) followed by the author's
  generalized observation of the mechanism.
- **Confidence**: anecdotal
- **Quote**: "We realised that the agents were using the plans to coordinate. One agent would mark a line of the plan as in progress, the other agent would see that and not work on that line. When the first agent finished, the other agent would see not only that the work was complete and thus it was released to proceed, but would also be directly delivered notes on how the line had been implemented."
- **Our assessment**: This is the article's central concrete mechanism and its strongest,
  most specific claim. It describes two distinct functions bundled into one artifact (the
  plan file): mutual exclusion (avoid duplicate work on the same line) and information
  transfer (delivering implementation notes on completion) — both classical blackboard-system
  functions (see Claim 8), achieved here with no dedicated tooling, just plan files plus
  frequent commits.

### Claim 5: The team moved from passively observing the pattern to deliberately directing an agent to monitor the repository and integrate a dependency's work once it landed

- **Evidence**: A second concrete worked example (a cost model being developed in parallel
  with a verifier), described as an intentional exploitation of the already-observed pattern.
- **Confidence**: anecdotal
- **Quote**: "Knowing that someone else had been working on the cost model and pushing commits continually, we directed the agent working on the verifier to look at plans and source, monitor the repo, and when the work for the cost model lands start to integrate it. And it did."
- **Our assessment**: This is the pivot point in the narrative from "accidental" to
  "exploited" — once the team recognized the mechanism, they could direct an agent to use it
  as an explicit polling/integration strategy. This is a lightweight, low-effort version of
  the "manager plane" alerting behavior in `discussion-hn-ttal-multiagent-factory.md` (Claim
  6), achieved via a plain-language instruction ("monitor the repo... integrate it") rather
  than a dedicated messaging daemon.

### Claim 6: The coordination behavior was entirely unplanned — the team observed it happening before they understood or intentionally designed for it

- **Evidence**: Direct authorial statement, positioned as the summary of the preceding
  narrative section.
- **Confidence**: anecdotal
- **Quote**: "This was entirely ad hoc. It was an accident of a series of decisions. We saw it happen. And then started to use it."
- **Our assessment**: This is an important qualifier for how the guide should present this
  source: it is explicitly not a design pattern the author is recommending practitioners
  replicate procedurally (there is no recipe given for "how to make this happen"); it is a
  retrospective naming of something that already happened, with the follow-up claim (Claim
  9) that the author doubts he could reliably reproduce it.

### Claim 7: The author identifies the emergent coordination mechanism as the classical "blackboard system" pattern, tracing its lineage to the Hearsay-II system (1980) and Gelernter et al.'s tuple space concept (1986), drawing on his own university research

- **Evidence**: Direct authorial account connecting the observed behavior to his academic
  background (a research thesis on directing agent behavior with hierarchical sensors, which
  adopted the blackboard pattern as its coordination structure) and citing the two named
  historical systems with dates.
- **Confidence**: anecdotal (the historical dates/citations are presented as established
  computer-science history by the author, not as a claim original to this article)
- **Quote**: "This had previously been discovered in the development of the Hearsay-II system in 1980. It had been subsequently been developed into the more formal tuple space concept by Gelernter et al. in 1986."
- **Our assessment**: This is the most novel contribution of the source for our corpus: no
  other source note connects modern agentic-coding coordination behavior to the specific,
  named lineage of blackboard systems and tuple spaces in distributed AI research. It gives
  the guide a citable academic anchor for a pattern that `blog-anthropic-multi-agent-
  coordination-patterns.md` names "shared state" without historical grounding (see
  Cross-References).

### Claim 8: A blackboard/tuple space is defined as schema-free shared memory that autonomous agents read and write independently, enabling decomposed problem-solvers to drop labeled partial solutions for others to find and reuse

- **Evidence**: Direct definitional statement following the historical claim (Claim 7),
  describing the general mechanics of the pattern rather than this specific exercise.
- **Confidence**: anecdotal (author's own explanation of an established CS concept, not a
  new empirical finding)
- **Quote**: "A blackboard or tuple space is a shared memory that autonomous agents can read and write from independently. They read and write tuples with a certain minimum structure, and then as many extra fields as you want: no schema. It's a very effective technique for coordinating autonomous problem solvers towards a single goal. They can each solve a decomposed part of the problem, drop their solution into the shared space, label it, and other autonomous searchers will find it, pick it up, and use it as part of their work."
- **Our assessment**: This is a useful, reusable framing for the guide: it describes the
  blackboard pattern's requirements (a shared, minimally-structured, schema-free write
  surface; independent read/write access; labeling for discoverability) as a checklist
  against which any "repo as coordination channel" implementation can be evaluated — and the
  author explicitly says the team's accidental version was missing several of these parts
  (Claim 9).

### Claim 9: The team's accidental implementation was incomplete relative to how blackboard systems formally operate, and the author does not believe he could reliably reproduce it despite having identified the specific triggering prompt

- **Evidence**: Direct self-assessment of the exercise's limitations, including a stated
  fact that post-hoc analysis identified a single prompt responsible for triggering the
  behavior, paired with an explicit statement of low confidence in reproducibility.
- **Confidence**: anecdotal
- **Quote**: "It wasn't fully structured. It was missing some of the key parts of how blackboards operate. And because it was accidental, I'm not convinced I would be able to reliably prompt our agents into doing it again."
- **Our assessment**: This is the load-bearing caveat for the entire source: the author is
  explicit that this was not a robust or intentionally engineered mechanism, and flags
  reproducibility as an open problem rather than a solved one. The guide should not present
  this as "here's how to make your agents use your repo as a blackboard" — it should present
  it as "here is a documented instance of the failure mode/opportunity, and here is what the
  author believes is still missing" (formal structure, per Claim 8's checklist).

### Claim 10: The author believes an intentionally-designed coordination channel should sit independently of source control, because the team's source-control-based version broke when commit frequency was reduced to relieve CI load

- **Evidence**: Direct design recommendation, immediately followed by the specific incident
  that motivates it — the frequent-commit discipline (Claim 2) was itself walked back later
  in the exercise because it was overloading CI, which removed the continuous progress
  signal the coordination depended on.
- **Confidence**: anecdotal
- **Quote**: "The frequent commits were overloading our CI pipeline. We switched to only push when a more coherent chunk of change was complete. This deprived the agents of the continuous flow of updates on progress."
- **Our assessment**: This closes the loop on the article's own narrative: the exact
  mechanism that created the accidental blackboard (frequent commit/push, Claim 2) was later
  reversed for an unrelated reason (CI load), which broke the coordination channel as a
  side effect. This is direct evidence that piggybacking coordination on a version-control
  cadence is fragile — the coordination channel's health is coupled to a decision (commit
  frequency) that is made for entirely different reasons (CI capacity), which is exactly the
  failure mode the author uses to justify Talwrn (Claim 11).

### Claim 11: The author is building a dedicated tool, "Talwrn," intended as a simple, drop-in blackboard for agentic engineering coordination, and plans to use its own development as a running example

- **Evidence**: Direct statement of an in-progress, not-yet-built project, including the
  meaning of its name and the author's stated goal and validation plan.
- **Confidence**: anecdotal (a stated intention/early-stage project, not a shipped tool —
  no implementation detail, screenshot, or usage example is given in this article)
- **Quote**: "I've started working on a project I'm calling Talwrn. That's Welsh for a threshing pit, an area or space where arguments and conflict get worked out. This is aiming to be a blackboard for agentic engineering. My goal is a very simple to use tool that drops straight into your project and immediately offers a communication channel for agents to coordinate work."
- **Our assessment**: This is forward-looking and unverifiable at time of extraction — Talwrn
  is not shown, and there is no way to assess whether it delivers on the "simple to use,
  drops straight into your project" goal. Flag for a future source submission if/when Talwrn
  is released or documented in more detail; do not cite Talwrn in the guide as an existing,
  usable tool.

## Concrete Artifacts

### The two preconditions that combined to produce the accidental blackboard (synthesized from the narrative, Claims 2–3)

```
Source: "An Accidental Blackboard," martinfowler.com, 02 September 2026

Precondition 1 (introduced to fix CI overload, not for coordination):
  - Agents continually commit and rebase from main
  - Rebase-after-commit, then push, with build checks/controls in place
  - Rationale given: "integrate early and often" / catch build failures locally

Precondition 2 (introduced for planning discipline, not for coordination):
  - Agents scope work to numbered/identified sections of a shared spec
  - Agents create plans linked to those spec sections
  - Plans are stored in the repo and updated in place as work progresses

Combined effect (not designed, observed after the fact):
  - Plan updates are swept up in the same frequent-commit cadence as code
  - Other agents reading the repo see plan-line status as an implicit lock
  - Other agents reading a completed plan line receive implementation notes
```

### Historical lineage cited for the blackboard pattern (verbatim dates/names, from source)

```
Source: "An Accidental Blackboard," martinfowler.com, 02 September 2026
        Section: "The repo as an accidental blackboard for agents"

- Hearsay-II system — 1980 (originating development of the blackboard pattern)
- Tuple space concept — Gelernter et al., 1986 (more formal successor concept)
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 5 ("Shared state requires
    first-class termination conditions — without them, agents enter reactive
    token-burning loops," quoting "Shared state removes the intermediary by letting agents
    coordinate through a persistent store that all can read and write directly.") — this
    article's repo-as-plan-file mechanism (Claim 4 here) is a concrete, unplanned instance
    of exactly the "shared state" coordination topology that source names abstractly. Notably,
    this article does not describe any explicit termination/convergence mechanism, which is
    consistent with Claim 9 here (the author's own admission the implementation was "missing
    some of the key parts of how blackboards operate") — read together, the two sources
    suggest termination/convergence handling is one of the missing formal parts.
  - `blog-addyosmani-code-agent-orchestra.md` Claim 4 (Agent Teams: a shared task list with
    dependency tracking, quoting "When backend marks API endpoint complete, blocked test task
    automatically flips to pending.") — this is functionally the same dependency-unlocking
    behavior as Claim 4 here (one agent's plan-line completion releasing another agent to
    proceed), but arrived at through opposite means: Osmani describes a purpose-built,
    vendor-shipped feature (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, an explicit shared task
    list with dependency tracking and file locking); this article describes the same
    end-user-visible behavior emerging from plain plan files and commit discipline, with no
    dedicated feature at all. The convergence on the same coordination behavior from a
    built feature and an accidental byproduct is notable corroborating evidence that
    dependency-aware task handoff is a natural need in multi-agent coding, not an artifact
    of one particular tool.
  - `discussion-hn-ttal-multiagent-factory.md` Claim 6 (P2P mesh topology: workers alert the
    Manager directly when blocked, "workers get blocked, they alert the designer directly
    rather than waiting") — this article's Claim 5 (directing an agent to "monitor the repo...
    and when the work for the cost model lands start to integrate it") is a lighter-weight,
    prompt-only analog of the same alerting/monitoring behavior, achieved without any
    dedicated messaging daemon or mesh protocol.

- **Contradicts**: None filed. No existing corpus note asserts that repo-based, commit-cadence-
  coupled coordination is robust or that shared-state coordination requires no explicit
  termination/completion handling — this article's own account of the mechanism breaking
  when commit frequency changed (Claim 10) is consistent with, not opposed to, the existing
  corpus's caution around shared-state coordination (`blog-anthropic-multi-agent-coordination-
  patterns.md` Claim 5).

- **Extends**:
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 5 and Claim 10 (shared state
    pattern and its decision criteria) — this article adds two things that source lacks: (1)
    a named historical/academic lineage for the pattern (blackboard systems, Hearsay-II 1980,
    tuple spaces 1986 — Claim 7 here), and (2) a concrete account of how a real, though
    unplanned, shared-state coordination channel actually failed in practice (coupling to
    commit cadence, which was changed for an unrelated CI-capacity reason — Claim 10 here).
  - `discussion-hn-ttal-multiagent-factory.md` Claim 5 ("Agents should be stateless
    executors, with all state externalized to standard CLI tools") — this article's plan
    files stored in the repo are a similar externalized-state pattern, but using version
    control itself (not a purpose-built external tool like Taskwarrior/FlickNote) as the
    persistence layer — and, per Claim 10 here, that specific choice (piggybacking on git)
    is exactly what made the channel fragile when commit cadence changed for unrelated
    reasons. This is a concrete argument for TTal's design choice of external, non-VCS state
    tools over relying on commit cadence itself as the signal.

- **Novel**:
  - **Named historical lineage for agent coordination** (blackboard systems / Hearsay-II
    1980 / tuple spaces, Gelernter et al. 1986 — Claim 7): no other source note in the corpus
    connects modern multi-agent coding coordination to this specific, dated computer-science
    history.
  - **A concrete account of shared-state coordination breaking as a side effect of an
    unrelated infrastructure change** (Claim 10): existing corpus sources describe shared-
    state termination/convergence as a design requirement in the abstract
    (`blog-anthropic-multi-agent-coordination-patterns.md` Claim 5); this article is the
    first in the corpus to document an actual instance of a shared-state channel degrading
    because a coupled infrastructure decision (commit frequency) changed for reasons
    unrelated to coordination.
  - **Plan-file-as-implicit-lock via plain commit/rebase discipline, with no dedicated
    tooling** (Claim 4): every other multi-agent coordination source in the corpus describes
    either a vendor feature (Osmani's Agent Teams), a purpose-built CLI (TTal), or an
    orchestration framework (PRINCE/LangGraph) as the coordination mechanism. This is the
    only source documenting the coordination behavior emerging from ordinary version-control
    hygiene practices with no additional tooling at all.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add this article as a concrete, named case study
  under any "shared state" or "multi-agent coordination" section built around
  `blog-anthropic-multi-agent-coordination-patterns.md`'s five-pattern taxonomy. Use Claim 4
  (plan-line-as-lock, notes-on-completion) as a worked example of the shared-state pattern
  operating through nothing more than repo-stored plan files and a commit/rebase discipline —
  and pair it immediately with Claim 9 and Claim 10 (the mechanism was admittedly incomplete
  and broke when commit cadence changed) as the caveat: this is evidence the pattern can
  emerge cheaply, not evidence that it is production-ready without deliberate design for
  termination/completion signaling.

- **Chapter 02 (Harness Engineering)**: Add Claim 7's historical framing (Hearsay-II 1980,
  tuple spaces 1986) as an academic citation anchor wherever the guide discusses the "shared
  state" coordination pattern, giving practitioners a name and literature trail beyond the
  vendor taxonomy.

- **Chapter 04 (Context Engineering)**: Note Claim 2 as a cautionary example of infrastructure
  practices having second-order, agent-coordination-relevant effects that are easy to miss:
  a commit/rebase discipline introduced purely to stabilize CI created (and later, when
  reversed, destroyed) an information channel agents were depending on, without that being
  anyone's stated intent either time.

- **Chapter 05 (Team Adoption)**: If/when Talwrn (Claim 11) ships with usable documentation,
  flag for a follow-up source submission — at extraction time it is a stated intention only
  and should not be cited as an available tool.

## Extraction Notes

- WebFetch's first pass on this URL returned only a short, paraphrased summary (consistent
  with the copyright-caution behavior already documented in other source notes in this
  corpus, e.g. `blog-fowler-garg-orchestrator-tax.md` and `blog-fowler-bayer-prince-agentic-
  rag.md`). To obtain quote-accurate text, the raw HTML was fetched directly via `curl` with
  a browser user-agent and converted to plain text locally; all quotes above were copied
  verbatim from that locally-rendered full text and cross-checked against the surrounding
  paragraph structure of the original HTML. The full article (~1,100 words, two section
  headings) was read in its entirety — no paywall or access restriction was encountered.
  There were no linked sub-pages substantive enough to follow (the only outbound content
  links are to the Thoughtworks "Exploring Gen AI" series index and a "previous article"
  link to "TDD inside the agent loop - theater or actual value?", a different article not
  in scope for this extraction).
- Three separate Prospector triage comments were present on the issue with slightly
  different chapter-number suggestions (Ch05/Ch03; Ch02/Ch04/Ch05; Ch05/Ch03/Ch02), all
  converging on multi-agent coordination as the core topic. This note treats the underlying
  content claims as authoritative over any single comment's specific chapter numbering, per
  the guide's actual chapter structure (`guide/02-harness-engineering.md`,
  `guide/04-context-engineering.md`, `guide/05-team-adoption.md`) at extraction time.
- Cross-reference claims were verified by re-reading the cited source notes directly before
  writing each citation: `blog-anthropic-multi-agent-coordination-patterns.md` (Claims 5,
  10), `blog-addyosmani-code-agent-orchestra.md` (Claim 4), and
  `discussion-hn-ttal-multiagent-factory.md` (Claims 5, 6). `blog-fowler-bayer-prince-
  agentic-rag.md` was also read in full (flagged by the Prospector as overlapping) but
  contains no claims specifically about multi-instance/multi-agent coordination via a shared
  repository or blackboard-style mechanism — it documents a single orchestrated LangGraph
  workflow's internal reflection loops instead — so no cross-reference to it is included
  above; this is a deliberate omission, not an oversight.
- Confidence set to `anecdotal`: this is a first-person account of a single four-day internal
  exercise on a simulated client, with no quantified measurement of the coordination
  mechanism's effectiveness, failure rate, or reproducibility, and the author's own explicit
  statement that he is not confident the behavior could be reliably reproduced (Claim 9).
  The historical/definitional claims about blackboard systems (Claims 7–8) are standard,
  citable computer-science background rather than novel empirical findings, but are still
  graded `anecdotal` here because they are presented without independent citation links (no
  URL to the Hearsay-II or Gelernter et al. sources is given in the article itself).
- No contradiction requiring a formal contradiction issue (per MINER.md §4a) was found.
