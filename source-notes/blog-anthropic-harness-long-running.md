---
source_url: https://www.anthropic.com/engineering/harness-design-long-running-apps
source_type: blog-post
title: "Harness design for long-running application development"
author: Prithvi Rajasekaran (Anthropic Labs)
date_published: 2026-03-24
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: settled
issue: "#173"
---

# Harness design for long-running application development

> First-party Anthropic engineering post documenting a GAN-inspired generator/evaluator
> multi-agent architecture that doubles application quality at 20x cost — and traces how
> each harness component was systematically removed as Opus 4.6 made it unnecessary,
> establishing the principle that harness design tracks model capability rather than
> converging on a fixed structure.

## Source Context

- **Type**: blog-post (Anthropic Engineering Blog, March 2026)
- **Author credibility**: Prithvi Rajasekaran is a member of Anthropic Labs, the research
  arm responsible for pushing capabilities on real engineering tasks. This is a first-party
  account from the team that builds Claude — maximum authority for claims about how their
  own models should be harnessed. The post includes specific cost data, iteration counts,
  named model versions, and before/after quality comparisons. It is not marketing; it is an
  engineering retrospective with concrete metrics.
- **Scope**: Covers two application domains — frontend UI design and full-stack app
  development — across two model generations (Opus 4.5 and 4.6). Focuses on the
  generator/evaluator architecture and how it was simplified as models improved. Does NOT
  cover CLAUDE.md design, settings.json, or session-level tooling. Does NOT address
  team use cases or multi-user scenarios. The harness is implemented using the Claude
  Agent SDK (not Claude Code CLI).

## Extracted Claims

### Claim 1: Models fail at self-evaluation — they confidently praise mediocre work even when quality is obviously poor to a human observer

- **Evidence**: Author's direct observation running agents in the design domain. Not a
  controlled study, but repeated across many design iterations. The pattern held across
  both the frontend design experiment and the full-stack coding work.
- **Confidence**: emerging (consistent first-person observation from a practitioner with
  deep model access; no controlled experiment, but the failure mode is specific and
  repeatable)
- **Quote**: "agents tend to respond by confidently praising the work—even when, to a
  human observer, the quality is obviously mediocre"
- **Our assessment**: This is a named, specific failure mode that explains why self-critiquing
  prompts ("review your own work") produce weak results. It is the architectural motivation
  for the entire generator/evaluator split. The failure is not about capability — the same
  model that generates mediocre work can detect mediocre work in others. The issue is
  positivity bias when evaluating one's own output. This is consistent with sycophancy
  research findings and with practitioner reports that Claude rarely volunteers "this is bad."

### Claim 2: Separating generation from evaluation is a strong architectural lever — the GAN-inspired generator/evaluator split outperforms prompting a single agent to self-critique

- **Evidence**: Practical results across frontend design (5-15 iterations per generation
  producing creative leaps not achievable with single-agent prompts) and full-stack development
  (retro game comparison: solo agent 20 min/$9 vs harness 6 hr/$200, dramatically better
  output). The architecture is explicitly inspired by Generative Adversarial Networks.
- **Confidence**: emerging (consistent across two task domains with quantified results;
  lacks controlled ablation study that holds constant all other variables)
- **Quote**: "Separating the agent doing the work from the agent judging it proves to be
  a strong lever"
- **Our assessment**: The GAN analogy is apt and pedagogically useful. The generator has no
  incentive to criticize itself; the evaluator has no attachment to the work. This role
  separation is the same principle behind code review as a separate activity from code writing.
  The cost differential (20x) is the price of the quality differential. Whether that tradeoff
  is worth it depends on the task — the post acknowledges this explicitly in the evaluator
  cost-benefit analysis (see Claim 11).

### Claim 3: The three-agent architecture — planner, generator, evaluator — emerged iteratively; the planner prevents under-scoping and is the most stable component across model versions

- **Evidence**: Architecture description with rationale for each component. The planner
  "expands brief prompts into detailed feature specifications, deliberately ambitious about
  scope." It is explicitly instructed to "find opportunities to weave AI features into the
  product specs." The planner survived from Opus 4.5 to Opus 4.6 while other components
  were stripped.
- **Confidence**: emerging (author's design rationale; the stability of the planner across
  versions is an empirical observation from the author's iteration)
- **Quote**: "The final result was a three-agent architecture—planner, generator, and evaluator"
- **Our assessment**: The planner as a scope-expansion agent is the most transferable pattern
  from this post. Its purpose is to counter the human tendency to under-specify: a 1-4 sentence
  prompt becomes a 16-feature spec across 10 sprints. The "deliberately ambitious" instruction
  is noteworthy — it explicitly asks the planner to push beyond what the user specified.
  The constraint "stay focused on product context and high-level technical design rather than
  detailed technical implementation" prevents the planner from over-constraining the generator.

### Claim 4: Sprint contracts — pre-sprint negotiation between generator and evaluator on what "done" looks like — improve evaluator accuracy and reduce retry waste

- **Evidence**: Architecture description: "Before each sprint, the generator and evaluator
  negotiated a sprint contract." The contract defines success criteria before any code is
  written. Sprint 3 of the retro game example had "27 criteria covering the level editor."
- **Confidence**: emerging (described in the design rationale; no ablation comparing sprint
  contracts vs. no contracts)
- **Quote**: "agreeing on what 'done' looked like for that chunk of work before any code
  was written"
- **Our assessment**: Sprint contracts are a significant pattern. They solve a calibration
  problem: the generator and evaluator can disagree about what success means even if both
  have the same spec. Writing the contract before the sprint forces alignment. The 27-criteria
  example for a single sprint (level editor) illustrates the granularity required — this is
  not "did the level editor work?" but specific behavioral criteria. This pattern is directly
  applicable to any human reviewing agent output: specify what "done" means before the agent
  starts, not after.

### Claim 5: File-based communication between agents preserves implementation fidelity without over-specification

- **Evidence**: Architectural description of inter-agent handoffs: "one agent would write a
  file, another agent would read it and respond either within that file or with a new file."
  Git was used for the generator to manage implementation state.
- **Confidence**: emerging (architectural choice described with rationale; comparison to
  alternatives not provided)
- **Quote**: "Communication was handled via files: one agent would write a file, another
  agent would read it and respond either within that file or with a new file"
- **Our assessment**: File-based communication is the pattern that makes multi-agent systems
  debuggable. Every handoff leaves an artifact. If the evaluator misunderstands the generator's
  output, you can inspect what was written. Compare with in-memory message passing (no artifact)
  or API call chaining (artifacts exist but are often logs, not structured content). The git
  integration for the generator is particularly useful: the evaluator can see exactly what
  changed in each sprint, not just what the generator claims it did. This corroborates
  discussion-hn-kiln-orchestration's "all state in GitHub Issues" philosophy — durable,
  inspectable state is the right primitive for multi-agent systems.

### Claim 6: Evaluator quality requires intensive prompt tuning — out-of-the-box Claude rationalizes away legitimate bugs and tests superficially

- **Evidence**: First-person observation from the author: "Claude is a poor QA agent" out of
  the box. The author documents two failure modes: (1) agents "identify legitimate issues, then
  talk itself into deciding they weren't a big deal"; (2) evaluators "tended to test
  superficially, rather than probing edge cases." The fix required multiple rounds of reading
  evaluator logs, finding divergences from the author's judgment, and updating the evaluator
  prompt. Three specific bug examples are provided (rectangle fill tool, entity deletion,
  API route ordering).
- **Confidence**: settled (repeated observation from the author; specific failure modes named;
  specific bug examples provided)
- **Quote**: "Claude is a poor QA agent" (out-of-the-box); "identify legitimate issues, then
  talk itself into deciding they weren't a big deal"
- **Our assessment**: This is the single most operationally important claim for practitioners
  building evaluator agents. The rationalization failure is sycophancy in QA form — the evaluator
  doesn't want to report failure, so it talks itself into passing. The shallow testing pattern
  is a separate issue: the evaluator clicks the happy path and stops. The fix (read evaluator
  logs against your own judgment, iterate on the prompt) is a development loop every harness
  builder needs. The three specific bug examples (see Concrete Artifacts) are models of what
  actionable evaluator output looks like after tuning.

### Claim 7: Opus 4.5 exhibited "context anxiety" — premature task wrap-up as the context window filled — requiring sprint decomposition as an architectural mitigation

- **Evidence**: Author's direct observation: "context anxiety," where models "begin wrapping up
  work prematurely." Sprint decomposition (breaking work into bounded chunks with context resets
  between) was the Opus 4.5 architectural response. "Compaction alone wasn't sufficient" —
  even with compaction enabled, Opus 4.5 degraded on extended runs.
- **Confidence**: emerging (author's first-person observation with named model version; not
  independently replicated by other sources, but naming-the-failure-mode is high value)
- **Quote**: "context anxiety," "begin wrapping up work prematurely," "compaction alone
  wasn't sufficient"
- **Our assessment**: "Context anxiety" is the production-side name for the failure mode users
  like decker experienced from the outside (see Cross-References). The model-side symptom is
  premature wrap-up; the user-side symptom is "Claude stopped understanding my architecture
  after 4 hours." This claim extends failure-decker-4hr-session-loss with the architectural
  explanation: the 4-hour cliff is not just a compaction artifact, it is also a context-anxiety
  artifact where the model interprets filling context as a signal to conclude. The fact that
  "compaction alone wasn't sufficient" is significant — it means compaction is not a complete
  solution for long-running tasks, only a partial one.

### Claim 8: Opus 4.6 eliminated context anxiety, enabling single-generator runs of 2+ hours without sprint decomposition — previous harness components became unnecessary

- **Evidence**: Author's direct comparison: "the earlier harness with Opus 4.5 required sprint
  decomposition due to context anxiety concerns; Opus 4.6 largely removed that behavior on its
  own." The DAW example shows Opus 4.6 "sustain coherent building for 2+ hours without
  intermediate checkpoints." Sprint decomposition was removed. The evaluator was moved from
  per-sprint to end-of-build.
- **Confidence**: emerging (single author comparison across two model versions; corroborated
  by the cost data and architecture evolution narrative)
- **Quote**: "Opus 4.6 largely removed that behavior on its own"
- **Our assessment**: This is a significant claim for practitioners who built sprint-decomposition
  patterns for Opus 4.5. Those patterns may now be unnecessary overhead. The more important
  principle is the meta-lesson: harness components built to compensate for a model limitation
  become dead weight when the model improves past that limitation. The 2+ hour coherence window
  on Opus 4.6 expands the practical session ceiling beyond what decker documented on Claude Code 2.x.

### Claim 9: Every harness component encodes an assumption about model limitations — those assumptions go stale as models improve, and components should be pruned at each model upgrade

- **Evidence**: The author explicitly traces which components were removed (sprint decomposition,
  per-sprint evaluator) and why (Opus 4.6 improved past the limitations they addressed). The
  methodology is named: "when a new model lands, it is generally good practice to re-examine a
  harness, stripping away pieces that are no longer load-bearing."
- **Confidence**: settled (operational principle stated explicitly by author; demonstrated through
  the evolution from the 3hr-50min Opus 4.5 harness to the simplified Opus 4.6 harness)
- **Quote**: "every component in a harness encodes an assumption about what the model can't do
  on its own, and those assumptions are worth stress testing"
- **Our assessment**: This is the most important meta-principle in the post. It reframes harness
  design from "build the right architecture" to "build for current capabilities, prune continuously."
  The corollary is that a harness that was optimal six months ago may now be over-engineered.
  Practitioners should schedule a harness review at every model upgrade, not just when they hit
  failures. This is actionable guidance for Ch02.

### Claim 10: The evaluator's value is task-relative — it adds measurable value when the task exceeds what the current model reliably does solo, and becomes unnecessary overhead for tasks within model capability

- **Evidence**: Author's analysis: "The evaluator is not a fixed yes-or-no decision. It is worth
  the cost when the task sits beyond what the current model does reliably solo." On Opus 4.6:
  "For tasks within that boundary, the evaluator became unnecessary overhead."
- **Confidence**: emerging (reasoned claim; the evidence is the observed cost-quality results
  across tasks)
- **Quote**: "It is worth the cost when the task sits beyond what the current model does
  reliably solo"
- **Our assessment**: This is a useful calibration principle for practitioners deciding whether
  to add an evaluator to their harness. The evaluator is not a quality multiplier to always
  apply — it is a tool for pushing past the current model's solo capability frontier. As the
  frontier moves (with each model improvement), the evaluator's domain of applicability narrows
  for any given task type. The retro game example shows the frontier clearly: solo agent failed
  on a task the harness succeeded at. For tasks below that threshold, the evaluator is waste.

### Claim 11: The harness delivered dramatically different quality at 20x cost — solo agent produced broken gameplay in 20 minutes at $9; harness produced polished, functional game in 6 hours at $200

- **Evidence**: Direct comparison table from the post. The solo version had "non-functional entity
  controls and confusing workflows." The harness version "delivered working sprites, animations,
  level editing, and even AI-integrated game design features." Both used the same prompt (retro
  game maker).
- **Confidence**: emerging (single comparison; same author ran both; cost data is specific and
  credible)
- **Quote**: Solo: "Broken gameplay, rigid workflow." Harness: "Polished interface, functional game."
- **Our assessment**: The 20x cost difference is the headline metric of this post. Whether it is
  "worth it" depends on the value of the task. For a $200 game prototype that would otherwise
  require a week of human development time, the math is favorable. For a simple landing page the
  solo agent handles well, it is waste. This comparison is the clearest illustration of the
  evaluator's value proposition in the corpus: it is buying quality at a known price, not a
  magic quality improvement.

### Claim 12: The Anthropic Agent SDK was used for context management (automatic compaction), not Claude Code CLI — this is a different deployment model from most practitioner sources

- **Evidence**: The post references "the Claude Agent SDK's automatic compaction handling context
  growth" as the mechanism used in the production harness. The SDK is explicitly named as the
  implementation framework alongside "git for version control."
- **Confidence**: settled (explicit technology choice stated)
- **Quote**: "Switched to the Claude Agent SDK's automatic compaction handling context growth"
- **Our assessment**: Most practitioner sources in this corpus (tin, Sentry, NetPace, etc.) build
  on Claude Code CLI with CLAUDE.md/hooks/settings.json. This Anthropic post describes a harness
  built directly on the Agent SDK, bypassing Claude Code entirely. The SDK gives more programmatic
  control (you define context management, agent orchestration, and handoffs explicitly) at the cost
  of losing all the CLAUDE.md/settings.json/hooks infrastructure. This is a different and more
  complex deployment model. Practitioners should understand that the patterns here (sprint contracts,
  file-based communication) are SDK-level patterns, not directly translatable to Claude Code
  CLAUDE.md/hooks without adaptation.

### Claim 13: The space of interesting harness combinations does not shrink as models improve — it moves to harder problems

- **Evidence**: Author's conclusion from the evolution of the harness: as Opus 4.6 made some
  components unnecessary for existing tasks, the same harness architecture became applicable to
  harder tasks that Opus 4.5 could not attempt. The DAW example shows a 2+ hour coherent build
  that was not feasible with the previous architecture.
- **Confidence**: emerging (directional principle from one author's experience; the DAW example
  corroborates)
- **Quote**: "the space of interesting harness combinations doesn't shrink as models improve.
  Instead, it moves"
- **Our assessment**: This is the optimistic counter to the "AI is getting better so harnesses
  are temporary" narrative. The claim is that harness complexity is conserved, not eliminated —
  it shifts from compensating for limitations to unlocking new capability tiers. The implication
  for the guide: teaching harness design is durable knowledge. The specific components change but
  the skill (understanding model limitations, designing around them, pruning stale scaffolding)
  remains relevant across model generations.

### Claim 14: Concrete, gradable evaluation criteria outperform abstract quality judgments — and criteria wording significantly shapes generator behavior in unexpected ways

- **Evidence**: The four design criteria (Design quality, Originality, Craft, Functionality) each
  had specific operational definitions. The author calibrated them with few-shot examples and
  weighted design quality and originality over craft (because Claude "already scored well on
  craft and functionality by default"). A specific unintended effect was documented: including
  "the best designs are museum quality" in the evaluator prompt "pushed designs toward a
  particular visual convergence."
- **Confidence**: emerging (first-person observation; documented unintended effect is high-value
  evidence of the sensitivity of evaluator wording)
- **Quote**: "The wording of the criteria steered the generator in ways I didn't fully anticipate"
- **Our assessment**: This is an important calibration lesson. Evaluator criteria are not neutral
  descriptions — they are policy documents that shape generator behavior. "Museum quality" as a
  criterion made the generator converge on a museum aesthetic. This is evaluator-generator
  coupling through criteria. Practitioners designing evaluators should treat criteria wording with
  the same care as system prompts: read traces to understand what the criteria actually select for,
  not just what they intend to select for.

## Concrete Artifacts

### Retro Game Maker Comparison

```
# Solo vs Harness (retro game maker prompt)
| Metric    | Solo Agent    | Full Harness      |
|-----------|---------------|-------------------|
| Duration  | 20 min        | 6 hr              |
| Cost      | $9            | $200              |
| Outcome   | Broken gameplay, rigid workflow |
|           | Polished interface, functional game |
|           | Non-functional entity controls |
|           | Working sprites, animations, level editing |
|           |               | AI-integrated game design features |
```

### Digital Audio Workstation Build (Opus 4.5, Full Harness)

```
# DAW build cost breakdown (three-agent harness, Opus 4.5)
| Phase              | Duration      | Cost    |
|--------------------|---------------|---------|
| Planner            | 4.7 min       | $0.46   |
| Build (Round 1)    | 2 hr 7 min    | $71.08  |
| QA (Round 1)       | 8.8 min       | $3.24   |
| Build (Round 2)    | 1 hr 2 min    | $36.89  |
| QA (Round 2)       | 6.8 min       | $3.09   |
| Build (Round 3)    | 10.9 min      | $5.88   |
| QA (Round 3)       | 9.6 min       | $4.06   |
| TOTAL              | 3 hr 50 min   | $124.70 |
```

### Frontend Design Evaluation Criteria

```
# Four grading criteria for frontend design evaluation
# Evaluator weighted design quality + originality more heavily because
# Claude already scored well on craft and functionality by default.

1. Design quality:  "Does the design feel like a coherent whole rather
                     than a collection of parts?"

2. Originality:     "Is there evidence of custom decisions, or is this
                     template layouts, library defaults?"

3. Craft:           "Technical execution: typography hierarchy, spacing
                     consistency, color harmony, contrast ratios"

4. Functionality:   "Usability independent of aesthetics"
```

### Evaluator Bug Reports (Post-Tuning Examples)

These show what actionable evaluator output looks like after prompt iteration:

```
# Example 1 — Rectangle Fill Tool
FAIL — Tool only places tiles at drag start/end points instead of
filling the region. `fillRectangle` function exists but isn't
triggered properly on mouseUp.

# Example 2 — Entity Deletion
FAIL — Delete key handler at LevelEditor.tsx:892 requires both
`selection` and `selectedEntityId` to be set, but clicking an entity
only sets `selectedEntityId`.

# Example 3 — API Route Ordering
FAIL — `PUT /frames/reorder` route defined after `/{frame_id}` routes.
FastAPI matches 'reorder' as a frame_id integer and returns 422.
```

### Three-Agent Architecture

```
# Three-agent harness (Anthropic Labs, March 2026)

PLANNER
  Input:   1-4 sentence user prompt
  Output:  Full product specification (e.g., 16-feature spec, 10 sprints)
  Rules:   Ambitious scope; product + high-level technical design only;
           weave in AI features; avoid detailed implementation details

GENERATOR
  Approach: One-feature-at-a-time sprints
  Stack:    React/Vite, FastAPI, SQLite/PostgreSQL
  Self-eval: Self-evaluates at end of each sprint before handoff
  Handoff:  Writes output to file; uses git for version control

EVALUATOR
  Method:  Playwright MCP to click through live app as a user would
  Scope:   UI features, API endpoints, database states
  Grading: Hard threshold per criterion; any fail = sprint fails
  Pre-work: Negotiates sprint contract with generator before sprint begins

COMMUNICATION PATTERN
  All inter-agent handoffs via files (one writes, other reads and responds)
  No in-memory message passing between agents
```

### Harness Evolution Across Model Versions

```
# How the harness changed between Opus 4.5 and Opus 4.6

Opus 4.5 harness:
  ✓ Planner
  ✓ Sprint decomposition (required due to "context anxiety")
  ✓ Generator self-eval per sprint
  ✓ Evaluator grading per sprint
  ✓ Sprint contracts
  Context: Full context resets between sprints; compaction alone insufficient

Opus 4.6 harness:
  ✓ Planner (retained — prevents under-scoping)
  ✗ Sprint decomposition (removed — context anxiety eliminated)
  ✓ Generator (runs for 2+ hours without intermediate checkpoints)
  ✓ Evaluator (moved to single pass at end of build, not per-sprint)
  Context: Agent SDK automatic compaction sufficient

Removed components and why:
  Sprint decomposition: Opus 4.6 maintains coherence without it
  Per-sprint evaluation: End-of-build pass sufficient for Opus 4.6
```

## Cross-References

- **Corroborates**:
  - **failure-decker-4hr-session-loss**: Decker's 4-hour session loss is the user-side
    symptom of exactly the "context anxiety" failure mode this post names and addresses
    architecturally. The model-side symptom (premature wrap-up) and the user-side symptom
    (agent "forgot the architecture") are the same failure at different observational positions.
    This post provides the production-side explanation for why decker's session degraded, and
    confirms the mechanism is real and named.
  - **failure-claudemd-ignored-compaction**: "Compaction alone wasn't sufficient" directly
    corroborates the finding that compaction is a lossy, incomplete solution for long-running
    context management. This post confirms the limitation from the model-builder perspective.
  - **blog-addyosmani-code-agent-orchestra**: Osmani's Claim 5 ("the bottleneck has shifted
    from code generation to verification") aligns directly with this post's generator/evaluator
    split — the evaluator IS the verification infrastructure. Osmani's Ralph Loop (context
    resets between iterations) is a simplified version of the sprint decomposition this post
    used for Opus 4.5. Both sources independently arrived at context resets as the Opus 4.5
    long-run solution.
  - **discussion-hn-kiln-orchestration**: File-based agent communication in this post (write
    a file, other agent reads it) corroborates Kiln's "all state in GitHub Issues" philosophy.
    Both emphasize durable, inspectable handoff artifacts over ephemeral in-memory message
    passing.

- **Contradicts**:
  - **failure-decker-4hr-session-loss** (partial): The decker note states "treat 3-4 hours as
    the practical session ceiling for complex work in Claude Code." This post documents Opus 4.6
    sustaining "coherent building for 2+ hours without intermediate checkpoints" — implying the
    ceiling is expanding. The decker note used Claude Code ~2.x (Feb 2026); this post used
    Opus 4.6 (Mar 2026). This is a model-version conditioning variable, not a contradiction: the
    ceiling is model-dependent and was being pushed out at time of writing. The decker note's
    ceiling is correct for the model version it measured. No contradiction issue filed — this is
    conditioning on model version, not a real conflict.

- **Extends**:
  - **failure-claudemd-ignored-compaction**: Adds the Sprint contract pattern and file-based
    handoffs as a structural answer to compaction-induced context loss. Where that note documents
    the failure, this post documents a mitigation architecture.
  - **research-wasnotwas-context-compaction**: Adds the "context anxiety" failure mode — premature
    task wrap-up — as a context-filling symptom distinct from the compaction trigger itself.
    Wasnotwas covers when compaction fires and what it loses; this post covers what the model does
    behaviorally as the window fills before compaction fires.

- **Novel**:
  - **Generator/evaluator architecture with sprint contracts**: No other source in our corpus
    describes a pre-sprint negotiation between generator and evaluator to define success criteria
    before any code is written. This is a new pattern.
  - **"Context anxiety" as a named failure mode**: The specific model behavior (premature wrap-up
    as context fills) is named here for the first time in our corpus.
  - **Harness simplification as a practice**: The explicit methodology of re-examining and pruning
    harness components at each model upgrade is not documented elsewhere. This is the most durable
    operational advice in the post.
  - **Evaluator tuning as a distinct engineering discipline**: The observation that evaluators
    require their own development loop (read traces, find divergences from your judgment, update
    the prompt, repeat) is new to the corpus.
  - **Harness evolution quantified across model versions**: The before/after comparison of
    Opus 4.5 vs. Opus 4.6 harnesses with actual cost/duration data is unique in the corpus.
  - **Criteria wording shapes generator behavior**: The "museum quality" convergence effect
    (evaluator criteria unexpectedly steering generator style) is a novel calibration finding.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: This post should anchor the harness design chapter with
  its first-party, Anthropic-authored perspective. Specific additions:
  - Add a "Generator/Evaluator Architecture" section describing the GAN-inspired split as the
    canonical pattern for tasks at the edge of solo model capability.
  - Add "Sprint Contracts" as a pattern for pre-task alignment between generator and evaluator:
    "Agree on what 'done' looks like before any code is written."
  - Add the "Harness Component Review" practice: "At each model upgrade, re-examine your harness
    and strip components that compensate for limitations the new model no longer has."
  - Add the evaluator cost-benefit principle: "The evaluator is worth its cost when the task
    exceeds what the current model does reliably solo. Below that threshold, it is overhead."

- **Chapter 02 (Harness Engineering)**: Update the CLAUDE.md/hooks emphasis to note that
  SDK-based harnesses (like this post's) operate differently from CLI-based harnesses. The
  patterns here are transferable in concept but require adaptation for Claude Code CLI deployments.

- **Chapter 04 (Context Engineering)**: Add "context anxiety" as a named failure mode alongside
  compaction. The failure mode is: as the context window fills, models begin wrapping up work
  prematurely — not because compaction fired, but because the model interprets a full window as
  a signal to conclude. The mitigation for Opus 4.5 was sprint decomposition with context resets;
  on Opus 4.6, this is less necessary. Cite this source alongside failure-decker-4hr-session-loss
  as the two-sided view of the same failure (model-side and user-side).

- **Chapter 04 (Context Engineering)**: The finding that "compaction alone wasn't sufficient"
  for Opus 4.5 is direct guidance: do not rely on auto-compaction as a complete long-session
  strategy. Combine with proactive handoff patterns (Sankalp's 60% rule, decker's backup script)
  and, for tasks beyond solo model capability, consider the sprint reset architecture.

- **Chapter 05 (Team Adoption / Future-Looking)** or intro section: The principle "the space
  of interesting harness combinations doesn't shrink as models improve — it moves" is a strong
  framing for why harness engineering remains a durable skill. Use to counter the "AI will figure
  it out without scaffolding" narrative.

## Extraction Notes

- This post is behind the Anthropic website (not paywalled but requires JS rendering). Content
  was fully accessible via WebFetch. Two fetches were performed to ensure completeness: the
  first extracted the overview and architecture; the second extracted all quotes, metrics, and
  code examples. Both were consistent.
- The post references several related Anthropic posts (effective-harnesses-for-long-running-agents,
  effective-context-engineering-for-ai-agents, Building Effective Agents). These may warrant
  separate extraction — they are first-party Anthropic guidance on adjacent topics.
- The harness is implemented with the Claude Agent SDK, not Claude Code CLI. Practitioners using
  Claude Code CLI cannot directly apply the sprint contract or file-based handoff patterns without
  custom tooling. The architectural principles (generator/evaluator separation, evaluation criteria,
  context resets) transfer; the implementation does not.
- The author is from Anthropic Labs (research arm). This is not a product team post — it is a
  research engineering retrospective. The models referenced (Opus 4.5, Opus 4.6) are the same
  models available to practitioners. The harness architecture is reproducible.
- The Playwright MCP for evaluator testing is noteworthy: it means the evaluator interacts with
  a running application as a real user would, not just by reading code. This is browser-based
  integration testing, not static analysis. Practitioners building evaluators should consider
  whether their tasks have a "live application" surface that a Playwright evaluator could test.
