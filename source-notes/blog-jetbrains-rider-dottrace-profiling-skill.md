---
source_url: https://blog.jetbrains.com/dotnet/2026/06/25/performance-profiling-agent-skill-in-rider/
source_type: blog-post
title: "Your AI Agent Keeps Missing The Real Bottleneck. JetBrains Rider Can Fix It Now."
author: Sasha Ivanova (JetBrains)
date_published: 2026-06-25
date_extracted: 2026-07-03
last_checked: 2026-07-03
status: current
confidence_overall: emerging
issue: "#1455"
---

# Your AI Agent Keeps Missing The Real Bottleneck. JetBrains Rider Can Fix It Now.

> JetBrains introduces `dottrace-analyze`, a dotTrace-backed profiling skill for AI
> Assistant agents in Rider that lets an agent read an actual `.dtp` profiler snapshot
> instead of guessing from source code alone. JetBrains' own 80-run, eight-scenario
> evaluation shows average diagnostic accuracy rising from 4.71/10 to 8.15/10 with the
> skill, perfect root-cause matches more than doubling (20/80 → 48/80), and one case
> study (an Avalonia UI freeze) going from 1.6/10 to a perfect 10/10 on all ten runs —
> at a higher per-run cost in the aggregate batch, but a lower cost in the case where
> the skill prevented a long unproductive search.

## Source Context

- **Type**: blog-post (JetBrains .NET Tools blog, published June 25, 2026; auto-discovered
  via the trusted `jetbrains-ai` RSS feed). Technical/product blog combining a product
  announcement (the `dottrace-analyze` skill) with a first-party evaluation report.
- **Author credibility**: Sasha Ivanova, writing on the official JetBrains .NET blog for a
  feature JetBrains itself built and ships in Rider. First-party vendor source: authoritative
  for what the skill does, how it is invoked, and the exact numbers from JetBrains' own
  evaluation harness. Not an independent or third-party benchmark — JetBrains designed the
  evaluation scenarios, the LLM-as-judge rubric, and chose which case study to highlight, so
  the numbers should be read as evaluation-under-vendor-control rather than a neutral
  audit. No named external customers, no independent replication.
- **Scope**: Covers a single new IDE agent-skill feature (`dottrace-analyze`) for Rider's
  AI Assistant, the mechanics of invoking it against `.dtp` profiler snapshots, and one
  internal evaluation (eight .NET performance scenarios, 80 total runs, plus a
  separately-run Avalonia case study). Does NOT cover: the skill's behavior on non-.NET
  workloads, how it composes with other Rider AI Assistant skills, longitudinal/production
  usage data beyond the evaluation, or how the LLM-as-judge rubric itself was validated
  against human graders. Article is a "Release" / feature-announcement post rather than a
  research paper — no methodology appendix, no raw per-run data published.

## Extracted Claims

### Claim 1: Without runtime profiling access, an agent investigating a performance problem defaults to scanning source code for plausible-looking inefficiencies and presenting them confidently as the bottleneck, whether or not they are the actual cause

- **Evidence**: Framing argument opening the article's problem statement, contrasting what
  a profiler snapshot reveals against what a source-code-only agent can infer.
- **Confidence**: anecdotal (JetBrains' characterization of source-only-agent failure mode;
  consistent with the article's own before/after evaluation data, but stated as narrative
  framing rather than as a separately cited study)
- **Quote**: "But an agent with no access to profiling can't read it. So it does the only
  thing it can: scans the project, finds some plausible-looking inefficiencies, and
  confidently presents them as the bottleneck."
- **Our assessment**: This names a specific failure mode of source-only code-review agents
  applied to performance problems: not "the agent fails to find an answer" but "the agent
  produces a plausible, confidently-stated, and potentially wrong answer." That distinction
  matters for guide purposes — a wrong-but-confident diagnosis is more dangerous to
  downstream trust than a agent that says "I don't know," because a practitioner may act on
  the misdiagnosis (e.g., "optimize this rendering code") without checking it against
  ground truth. The article's own evaluation (Claims 4-6) is offered as the empirical
  backing for this framing.

### Claim 2: JetBrains built `dottrace-analyze`, a dotTrace-backed profiling skill for AI Assistant agents in Rider, so agents can ground performance diagnosis in actual runtime profiler snapshots rather than source-code inspection alone

- **Evidence**: Direct product announcement naming the skill and its integration point
  (AI Assistant agents in Rider, backed by the dotTrace profiler).
- **Confidence**: settled (product fact — the skill ships and is named in the announcement)
- **Quote**: "We've been building something to fix that in Rider: a dotTrace-backed
  profiling skill for the agents inside AI Assistant, called `dottrace-analyze`."
- **Our assessment**: This is the headline product fact. It is a concrete instance of a
  broader pattern already emerging in the corpus: IDE vendors shipping domain-specific,
  tool-backed "skills" that hand an agent structured access to data it could not obtain by
  reading source files (see Cross-References — `docs-github-copilot-vs-april-2026.md` for
  the analogous `@BuildPerfCpp` build-performance agent, and `blog-ghaw-agent-observability.md`
  for GitHub's own internal audit/metrics agents). `dottrace-analyze` is the first corpus
  source specifically pairing a CPU/UI-freeze *profiler* (as opposed to build logs, git
  history, or CI metrics) with an agent skill.

### Claim 3: JetBrains frames the skill's value proposition as "evidence beats guessing" — a profiler-backed agent can cite a specific, quantified hotspot instead of offering only speculative code-smell suggestions

- **Evidence**: Direct restatement of the product philosophy immediately following the
  problem statement, using a concrete illustrative contrast ("some code smells that might
  be slow" vs. a cited percentage).
- **Confidence**: anecdotal (marketing/product framing, though internally consistent with
  the mechanism described in Claim 8 and the evaluation results in Claims 4-6)
- **Quote**: "Evidence beats guessing. Without the snapshot, the best an agent can offer is
  'here are some code smells that might be slow.' With it, the agent can say 'this
  snapshot says 88% of your time went here, and here's why.'"
- **Our assessment**: The "88% of your time went here" example is illustrative phrasing,
  not a reported number from the actual evaluation scenarios (the evaluation's own numbers
  are the 4.71→8.15 accuracy scores and the Avalonia 1.6→10 case, not an "88%" hotspot
  figure) — worth noting so this quote isn't mistaken for evaluation data. The underlying
  claim — that citing a measured proportion of runtime is categorically stronger evidence
  than an unverified code-smell guess — is a reasonable and fairly uncontroversial claim
  about what profiling data adds; it does not itself require independent verification
  beyond what profilers already provide to human engineers.

### Claim 4: JetBrains evaluated the skill across eight .NET performance-investigation scenarios from different projects, totaling 80 runs, scoring each answer against a reference root cause using a fixed LLM-as-judge rubric

- **Evidence**: Description of the evaluation methodology: scenario count, run count, and
  the four-part judging rubric.
- **Confidence**: emerging (a real evaluation design with a stated rubric and run count,
  but vendor-run, not independently audited, and the rubric's inter-rater reliability
  against human judges is not reported)
- **Quote**: "each answer was evaluated against a reference root cause with a fixed
  LLM-as-judge rubric: did the agent identify the primary hotspot, explain the mechanism,
  avoid misleading detours, and propose a fix that followed from the evidence?"
- **Our assessment**: This is a concrete, four-criterion LLM-as-judge rubric applied to an
  agentic diagnostic task, which is useful methodologically independent of the specific
  product. The four criteria (primary hotspot identified, mechanism explained, no
  misleading detours, fix follows from evidence) are a reasonable rubric for "did the agent
  actually diagnose the problem" as opposed to "did the agent produce plausible-sounding
  text." `blog-cursor-continual-harness-improvement.md` Claim 2 documents Cursor's own
  LLM-as-judge use (classifying user satisfaction from follow-up messages) — a different
  application (online user-satisfaction signal vs. offline reference-answer grading) of the
  same general LLM-as-judge evaluation technique, corroborating that LLM-as-judge is
  becoming a standard tool for grading agent output where ground truth exists but manual
  grading doesn't scale.

### Claim 5: Across the 80-run evaluation, agents with the profiling skill scored substantially higher on average accuracy and produced far more perfect root-cause matches than agents without it

- **Evidence**: Results table comparing "without skill" vs. "with skill" conditions across
  three metrics.
- **Confidence**: emerging (real reported numbers from a vendor-run internal evaluation;
  no independent replication, no confidence intervals or per-scenario breakdown published)
- **Quote**: (no direct quote; see data table below — the source states the headline
  comparison as "the average accuracy score went from 4.71 to 8.15" across all 80 runs)
- **Our assessment**: The magnitude of the jump (accuracy nearly doubling, perfect matches
  more than doubling) is a large effect size for what is, mechanically, "give the agent one
  additional structured data source." It corroborates a pattern already present in the
  corpus — that agents perform substantially better when given direct access to the
  relevant evidence rather than being left to infer it from adjacent artifacts (see
  Cross-References). The obvious caveat: JetBrains designed both the scenarios and the
  judge rubric, so this number reflects performance on JetBrains-selected .NET scenarios
  specifically, not a general claim about profiler-augmented agents on arbitrary workloads.

**Results table (reproduced from the source's evaluation summary; 80 runs across 8 scenarios):**

| Metric | Without skill | With skill |
|---|---|---|
| Average accuracy score (/10) | 4.71 | 8.15 |
| Runs scoring 8+ | 29 / 80 | 59 / 80 |
| Perfect root-cause matches | 20 / 80 | 48 / 80 |

### Claim 6: In a dedicated case study, an agent diagnosing an Avalonia UI-freeze bug improved from an average score of 1.6/10 without the skill to a perfect 10/10 on every one of ten runs with the skill

- **Evidence**: A separate, more detailed case study (not part of the 80-run aggregate)
  isolating one specific bug and running it ten times per condition.
- **Confidence**: emerging (single-scenario case study; ten runs per condition is a small
  sample, though the reported result is not a borderline improvement — it is 0-variance
  perfect performance across all ten "with skill" runs)
- **Quote**: "Without the skill, the agent averaged 1.6 out of 10. It went looking through
  rendering code, listed some general suggestions, and never landed on the real problem.
  With the skill, it scored 10 out of 10 on every single one of the ten runs."
- **Our assessment**: This is the most dramatic single number in the source, and the zero
  variance ("every single one of the ten runs") is notable — it suggests the failure mode
  without the skill was not occasional bad luck but a structural inability to find this
  particular class of bug (a UI freeze) from source inspection alone, while the profiler
  snapshot made the root cause unambiguous enough for perfect and consistent identification.
  For the guide, this is the strongest single illustrative example available in the corpus
  of "runtime diagnostic access as a categorical capability unlock" rather than an
  incremental accuracy improvement — worth citing as the headline number if the guide
  wants one memorable statistic for this pattern, with the caveat that it is one bug, one
  vendor's evaluation.

### Claim 7: Adding the profiling skill increases average per-run cost in the aggregate batch evaluation, but can reduce both cost and time in specific cases where it prevents an extended, unproductive source-code search

- **Evidence**: Two distinct cost comparisons given in the article: an aggregate batch
  cost increase, and a same-bug, per-run cost *and time* decrease in the Avalonia case
  specifically.
- **Confidence**: emerging (real reported cost figures from a vendor's own runs; token
  pricing and model version used for the cost calculation are not specified in what was
  extracted, so absolute dollar figures may not generalize across models/providers)
- **Quote**: "Cost went from about USD 1.91 per run without the skill to about USD 2.61
  with it."
- **Quote**: "USD 2.58 per run instead of USD 3.74, and 206 seconds instead of 373."
- **Our assessment**: These two numbers are easy to conflate but describe different things:
  the first is the aggregate cost increase across the full 80-run batch (paying more,
  on average, for the extra tool call and profiler data ingestion); the second is the
  Avalonia-specific case where the skill made the agent *both cheaper and faster* than the
  no-skill baseline, because the no-skill agent burned tokens and wall-clock time searching
  unproductively through rendering code before giving an answer anyway. The general
  takeaway for the guide: profiling/runtime-diagnostic tool calls have a fixed cost
  overhead that is not always recouped, but for bugs where source-only search would
  otherwise be long and unproductive, the net effect can be a net cost *and* time
  reduction, not just an accuracy improvement.

### Claim 8: The `dottrace-analyze` skill workflow requires the user to first capture a `.dtp` profiler snapshot (via dotTrace Standalone, the command-line tool, or dotTrace integrated in Rider), after which the agent loads the profiler data, walks the call trees, and connects the evidence back to source code before reasoning about the root cause

- **Evidence**: Description of the mechanical workflow: snapshot capture step (three
  named capture methods) followed by the agent's processing sequence.
- **Confidence**: settled (product mechanism, stated directly as how the feature works)
- **Quote**: "The agent loads the profiler data, walks the call trees, and connects the
  evidence back to your source before it starts reasoning."
- **Our assessment**: This sequencing — load evidence, walk the structure, connect to
  source, *then* reason — is a concrete instance of "evidence-gathering before inference"
  as an agent workflow shape, distinct from an agent that reasons first and searches for
  supporting evidence second (or not at all, per Claim 1's failure mode). The requirement
  that a human first capture the `.dtp` snapshot (the skill does not itself trigger
  profiling) means this is a human-initiated evidence-handoff pattern, not autonomous
  runtime instrumentation — the practitioner still decides when and what to profile; the
  agent's job starts once that artifact exists.

### Claim 9: `dottrace-analyze` is available in Rider 2026.2 EAP 8 (free during the EAP), while dotTrace profiling itself requires a dotUltimate or All Products Pack subscription — a Rider-only license does not include it

- **Evidence**: Availability/licensing statement for the feature.
- **Confidence**: settled (stated licensing/availability terms)
- **Quote**: (no direct quote; see paraphrase — the source states the skill ships in Rider
  2026.2 EAP 8 and that dotTrace profiling requires a dotUltimate or All Products Pack
  subscription, not a Rider-only subscription)
- **Our assessment**: This is a meaningful adoption gate for teams evaluating the pattern:
  the profiling-skill capability is not available to Rider-only license holders, which
  means teams must budget for a broader JetBrains subscription tier specifically to unlock
  this agent capability. Worth noting in the guide as a cost-of-adoption detail distinct
  from the per-run LLM cost figures in Claim 7 — there is a licensing cost on top of the
  token cost.

## Concrete Artifacts

### `dottrace-analyze` workflow (JetBrains Rider, per the source)

```
1. User captures a .dtp profiler snapshot via one of:
   - dotTrace Standalone
   - dotTrace command-line tool
   - dotTrace integrated within Rider

2. User asks the Rider AI Assistant agent to investigate, referencing the
   snapshot (directory/location).

3. Agent (dottrace-analyze skill):
   - loads the profiler data
   - walks the call trees
   - connects the evidence back to source code
   - THEN reasons about root cause (evidence-first, not guess-first)

4. Agent output includes:
   - the methods, source locations, and call paths that own the runtime
   - the root cause stated in plain developer language

Availability: Rider 2026.2 EAP 8 (free during EAP)
Licensing: dotTrace profiling requires dotUltimate or All Products Pack
           subscription (not included in a Rider-only subscription)
```

*Source: blog.jetbrains.com, June 25, 2026, retrieved 2026-07-03.*

### Evaluation results (80 runs, 8 .NET performance scenarios)

```
Condition          | Avg accuracy (/10) | Runs scoring 8+ | Perfect root-cause matches
-------------------|---------------------|------------------|---------------------------
Without skill       | 4.71                | 29 / 80          | 20 / 80
With skill          | 8.15                | 59 / 80          | 48 / 80

Judging method: LLM-as-judge against a reference root cause per scenario.
Rubric (4 criteria): primary hotspot identified; mechanism explained;
no misleading detours; proposed fix follows from the evidence.
```

*Source: blog.jetbrains.com, June 25, 2026, retrieved 2026-07-03.*

### Avalonia UI-freeze case study (10 runs per condition, separate from the 80-run batch)

```
Without skill: avg score 1.6/10 — agent searched rendering code, gave
               general suggestions, never identified the real cause.
With skill:    10/10 on every single one of the 10 runs (zero variance).

Cost/time for this specific bug:
  Without skill: ~USD 3.74/run, 373 seconds
  With skill:    ~USD 2.58/run, 206 seconds
  (skill was both cheaper and faster here, because the no-skill agent
  burned time/tokens searching unproductively before answering anyway)

Aggregate batch cost (all 80 runs, not Avalonia-specific):
  Without skill: ~USD 1.91/run
  With skill:    ~USD 2.61/run
  (skill costs more on average across the full scenario set)
```

*Source: blog.jetbrains.com, June 25, 2026, retrieved 2026-07-03.*

## Cross-References

### Cross-reference verification notes
Claims cited from other source notes below were re-read directly from those notes before
citing (per MINER.md §4b); claim numbers are counted top-to-bottom as they appear in each
note's "Extracted Claims" section.

- **Corroborates**:
  - `blog-ghaw-agent-observability.md` Claim 1 ("Observability isn't optional when you're
    running dozens of AI agents — it's the difference between a well-oiled machine and an
    expensive black box.") — that note documents GitHub's own factory building dedicated
    agents to observe *other agents'* runtime behavior (logs, cost, errors). This source
    documents the mirror-image pattern one layer down: an agent observing the runtime
    behavior of the *program it's debugging* (via a profiler snapshot) rather than the
    runtime behavior of agents themselves. Both sources converge on the same underlying
    principle — agents reasoning about a system perform better with structured runtime
    observability data than with static/source-only artifacts — applied to two different
    "systems": the target codebase (this source) vs. the agent fleet itself
    (`blog-ghaw-agent-observability.md`).
  - `docs-github-copilot-vs-may-2026.md` Claim 12 (the `@BuildPerfCpp` agent reruns a
    comparable incremental build when full-rebuild analysis detects a regression) — this is
    a narrower, prior corpus example of a build/performance-domain agent that consumes
    measured build-performance data rather than only source diffs. `dottrace-analyze`
    extends this pattern from build-time performance measurement to CPU/UI-freeze runtime
    profiling, with a much more detailed before/after evaluation than the `@BuildPerfCpp`
    changelog entry provides.
  - `blog-cursor-continual-harness-improvement.md` Claim 2 (Cursor's LLM-as-judge
    classifies user satisfaction from follow-up messages, e.g., "user moving on to next
    feature" as positive, "user pasting a stack trace" as negative) — a different
    application of LLM-as-judge (online, behavior-inferred satisfaction vs. this source's
    offline, reference-answer-graded accuracy), but both sources use "have an LLM grade
    agent output against a target" as their core evaluation mechanism, corroborating
    LLM-as-judge as a general-purpose technique for grading agentic tasks where scalable
    human grading isn't practical.

- **Extends**:
  - `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md`: that note documents
    GitHub Copilot becoming a selectable agent inside JetBrains' own "AI Assistant" product
    (via the Agent Client Protocol), and separately notes (Claim 4) that the changelog is
    silent on any approval/sandboxing model for Copilot's "run commands" capability inside
    that surface. This source is scoped to Rider's *native* AI Assistant agents (not the
    Copilot-as-guest-agent integration that note covers) and adds a concrete, product-native
    skill (`dottrace-analyze`) to that native surface — the two sources together sketch a
    JetBrains AI Assistant surface that is simultaneously host to guest agents (Copilot) and
    a growing set of its own native, tool-backed skills (profiling).
  - `blog-jetbrains-agentic-ai-governance.md`: that note's governance framework (chain of
    command, audit trails, human checkpoints) is written at the organizational/architectural
    level and does not address specific technical capabilities. This source is a concrete
    example of one of that framework's underlying assumptions in practice — the profiling
    skill workflow (Claim 8) requires a human to explicitly capture and hand off the
    snapshot before the agent acts, which is consistent with (though not explicitly framed
    as) the "intentional checkpoints" pattern from that note's Claim 8 — the human decides
    what evidence to gather and when, rather than the agent instrumenting the target system
    autonomously.

- **Contradicts**: None identified. No existing corpus source claims that source-code-only
  agents are sufficient for performance diagnosis, or that profiler-backed tooling does not
  improve diagnostic accuracy. No contradiction issue filed.

- **Novel**:
  - **A CPU/UI-freeze profiler snapshot as a structured, agent-consumable evidence source**:
    No prior corpus source documents an agent skill built specifically around ingesting a
    profiler snapshot (`.dtp` file, call trees, hot-path percentages) as opposed to build
    logs, git history, CI metrics, or static source code. This is a new evidence modality
    for the corpus's "what data can an agent access beyond source code" catalogue.
  - **A quantified before/after LLM-as-judge evaluation of runtime-diagnostic tool access
    specifically for performance-bug diagnosis**: While LLM-as-judge itself is present
    elsewhere in the corpus (Cursor's satisfaction classifier), no prior source runs a
    controlled with/without-tool-access comparison, scored against reference root causes,
    for a debugging/diagnosis task. This is the first source in the corpus with a specific,
    numeric magnitude (4.71→8.15 average; 1.6→10 case study) for "how much does giving an
    agent access to X improve its diagnostic accuracy on task Y."
  - **A case where added tool access is both more accurate and, in a specific instance,
    cheaper and faster**: Claim 7's Avalonia cost/time comparison (cheaper AND faster with
    the skill, for that specific bug) is a novel data point in the corpus for the general
    "does giving agents more tools cost more or less" question — most corpus discussion of
    added-tool-cost assumes tool access is a pure cost adder (e.g., Bswen's MCP token cost
    note, `blog-bswen-mcp-token-cost.md`, on token overhead from loaded MCP tool
    definitions); this source shows a case where the net effect reverses because the
    alternative (unaided search) was itself expensive.

## Guide Impact

- **Chapter 03 (Agent-Native Development Workflows)**: Add `dottrace-analyze` as a concrete
  example of a domain-specific, tool-backed IDE skill that changes what evidence an agent
  can access for a specific class of task (performance/UI-freeze diagnosis), extending the
  existing `@BuildPerfCpp` example (`docs-github-copilot-vs-may-2026.md` Claim 12) with a
  much more detailed, quantified before/after evaluation. Frame this as an instance of a
  general pattern worth naming explicitly: "evidence-gathering skills" that hand an agent
  structured runtime/measurement data (profiler snapshots, build timing, CI metrics) rather
  than leaving it to infer likely causes from source code alone.

- **Chapter 04 (Observability & State Management)**: Add the profiler-snapshot-as-agent-input
  pattern as a sibling to the agent-fleet observability pattern already documented via
  `blog-ghaw-agent-observability.md`. Both sources support the same guide-level claim —
  "agents reasoning about system behavior benefit from structured runtime observability
  data, not just static artifacts" — but this source applies it to the target *codebase*
  under investigation rather than to the agent fleet itself. Cite the 4.71→8.15 aggregate
  result and the 1.6→10 Avalonia case study as the strongest available quantified evidence
  in the corpus for this specific claim, with the caveat (per Claim 5's assessment) that
  this is a single-vendor, self-designed evaluation, not an independently replicated study.

- **Chapter 05 (Safety & Verification)**: Add the LLM-as-judge rubric described in Claim 4
  (primary hotspot identified; mechanism explained; no misleading detours; fix follows from
  evidence) as a concrete, reusable four-criterion template for grading agent diagnostic
  output against a known-correct answer, corroborating and extending the LLM-as-judge
  technique already documented for online satisfaction classification in
  `blog-cursor-continual-harness-improvement.md` Claim 2. Note for the guide: this rubric
  grades an *offline* task with a known reference answer (unlike Cursor's *online*,
  no-ground-truth satisfaction signal), so the two are complementary evaluation patterns for
  different situations (ground truth available vs. not).

- **Chapter 02 (Harness Engineering — cost)**: Add Claim 7's two-sided cost result (higher
  aggregate per-run cost, but lower cost *and* time in the specific case where the tool
  access short-circuits an otherwise-long unproductive search) as a nuance to any guide
  language that treats "more tool access = strictly more cost." Recommend framing added
  diagnostic tool access as an investment that costs more on average but can pay for itself
  specifically on the harder/longer-tail cases — which is exactly where an agent most needs
  the help.

## Extraction Notes

1. **WebFetch returns AI-processed content, not raw HTML**: As with other notes in this
   corpus, the WebFetch tool summarizes/paraphrases by default. Verbatim quotes above were
   obtained via multiple separate, narrowly-scoped fetch calls explicitly asking for exact
   sentences in quotation marks; each quote used in this note appeared consistently and
   character-identically across at least the fetch that surfaced it (several were
   cross-checked with a second independent fetch). The Assayer should spot-check quotes
   against the live source URL per standard practice.
2. **Author byline confidence**: The byline "Sasha Ivanova" was returned consistently
   across two independent fetches with no conflicting name surfaced by any fetch. Treated
   as reliable but flagged here since author bylines are one of the areas most prone to
   small-model fetch error.
3. **No sub-pages followed**: The article did not link to a separate methodology page,
   raw dataset, or the JetBrains dotTrace product docs in a way that seemed substantive
   enough to follow per MINER.md §1 (up to 5 linked pages) — the evaluation methodology,
   scenario list, and per-scenario breakdown are not published anywhere the article links
   to; only the aggregate table and one case study are given.
4. **"88% of your time went here" (Claim 3) is illustrative, not a reported evaluation
   number**: Flagged explicitly in Claim 3's assessment so this figure isn't later confused
   with the article's actual measured results (4.71→8.15, 20/80→48/80, 1.6→10 in Avalonia).
5. **Single-vendor, non-independent evaluation**: JetBrains designed the eight scenarios,
   the LLM-as-judge rubric, and selected the Avalonia case study for detailed writeup. No
   raw per-run data, scenario descriptions, or judge-model identity were found in the
   article. Confidence is rated "emerging" overall for this reason — the underlying pattern
   (runtime evidence beats source-only guessing) is highly plausible and consistent with the
   rest of the corpus, but the specific magnitudes come from one vendor's self-designed,
   unaudited internal evaluation.
6. **No contradictions found**: Cross-referenced against all JetBrains-tagged notes, the
   observability notes, and the LLM-as-judge/evaluation notes in the corpus. No existing
   source note disputes that runtime/profiler access improves agent diagnostic accuracy, so
   no contradiction issue was filed.
