---
source_url: https://simonwillison.net/2026/Aug/5/muse-code-and-muse-spark-12/
source_type: blog-post
title: "Introducing Muse Code and Muse Spark 1.2"
author: Simon Willison
date_published: 2026-08-05
date_extracted: 2026-08-15
last_checked: 2026-08-15
status: current
confidence_overall: emerging
issue: "#2709"
---

# Introducing Muse Code and Muse Spark 1.2

> Simon Willison's link-blog coverage of Meta's Muse Spark 1.2 model and its
> co-trained terminal coding agent, Muse Code. This note also directly fetches
> the two Meta pages Willison links to — the research announcement and the
> developer model page — which supply concrete architecture detail (async
> background agents, a replay-exact local event log, three bundled skills),
> a 1M-token context window figure, three named benchmarks, a GPU-kernel-
> optimization case study, and the full two-tier pricing table, none of which
> appear in Willison's own post. The single most harness-relevant finding is
> that Meta reports training Muse Spark 1.2 against harness-level trajectories
> — compaction, subagents, and "goals" — not just against code-generation
> quality, blurring the line between harness engineering (a practitioner
> discipline in this corpus) and foundation-model training (a vendor
> discipline).

## Source Context

- **Type**: blog-post (Simon Willison's weblog, "Link Blog" format — a short
  first-person post with direct quotes from Meta's announcement, plus two
  directly-fetched Meta pages: the research announcement at
  `research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2` and the
  developer model page at `developer.meta.com/ai/models/muse-spark/`).
- **Author credibility**: Simon Willison is the creator of Django and the
  `llm` CLI, and the most consistently cross-referenced practitioner source in
  this corpus (see `blog-simonwillison-muse-spark.md`,
  `blog-simonwillison-gpt56-luna-price-drop.md`). He documents what vendors
  publish and adds his own price/benchmark comparisons; he has no affiliation
  with Meta. His own commentary (framing, pelican-test judgment) is
  first-person opinion; the quotes he embeds from Meta are vendor-authored
  and should be read as vendor marketing/self-report, not independent
  verification.
- **Scope**: Covers the August 5, 2026 announcement of Muse Spark 1.2 (a
  coding-focused update to Muse Spark 1.1) and Muse Code (a new terminal
  coding agent, beta). Covers pricing, training methodology as described by
  Meta, and Willison's informal pelican-SVG visual comparison. Does NOT
  include independent benchmark verification, hands-on testing of Muse Code
  by Willison (unlike his April hands-on exploration of meta.ai chat tools),
  or numeric benchmark scores — Meta's own benchmark charts are referenced
  but no numbers are given in the fetched text.

## Extracted Claims

### Claim 1: Meta co-trained Muse Spark 1.2 with Muse Code, a dedicated terminal coding agent, rather than releasing the model and a separate tool independently

- **Evidence**: Meta's own stated training methodology, quoted by Willison and
  corroborated by the research-announcement page's product description.
- **Confidence**: settled (vendor's own technical description, consistent
  across Willison's post and both directly-fetched Meta pages)
- **Quote**: "We co-trained Muse Spark 1.2 with Muse Code to ensure the model
  exhibits its best performance"
- **Our assessment**: This is a stronger form of tool-harness integration than
  Meta's April meta.ai release, where `subagents.spawn_agent` was just one of
  16 generic chat tools (`blog-simonwillison-muse-spark.md`, Claim 4). Here
  Meta treats the model and its dedicated coding harness as a single
  co-trained artifact from the start, rather than a general chat model bolted
  onto tools after the fact. For practitioners, this reinforces that the
  model/harness boundary is increasingly a vendor design decision, not a
  fixed architectural layer.

### Claim 2: Willison frames "long-sequence agentic tool calling" as the single most important characteristic of current frontier models

- **Evidence**: Willison's own editorial framing, the opening sentence of the
  post.
- **Confidence**: anecdotal (one practitioner's opinion, not a measured claim)
- **Quote**: "the most important characteristic of any model these days is
  long-sequence agentic tool calling"
- **Our assessment**: This is Willison's judgment, not a vendor claim, but
  given his consistent cross-model commentary across dozens of notes in this
  corpus, it's a meaningful signal about where he sees the frontier moving.
  It matches the direction already documented in
  `blog-lilianweng-harness-engineering-rsi.md`'s "stabilized" coding-agent
  tool taxonomy — vendors converging on agentic tool-calling as the
  differentiator rather than raw chat quality.

### Claim 3: Muse Spark 1.2 was trained specifically on long-horizon coding tasks: whole-repository generation, large end-to-end projects, and auto-research

- **Evidence**: Vendor-sourced training description, corroborated verbatim
  across Willison's post and the research-announcement page.
- **Confidence**: emerging (vendor claim about training focus; no benchmark
  evidence of how well the model performs at these tasks is given)
- **Quote**: "Muse Spark 1.2 was extensively trained on long-horizon coding
  tasks, including whole-repository generation, large end-to-end projects,
  and auto-research."
- **Our assessment**: "Auto-research" as a named training target is worth
  flagging against `blog-lilianweng-harness-engineering-rsi.md`, which
  documents Trehan & Chopra's (2026) six recurring auto-research failure
  modes (training-data-default bias, implementation drift, memory/context
  degradation on long-horizon projects, over-optimism, weak domain
  intelligence, weak scientific taste) from a controlled study where only 1
  of 45-50 seed ideas per domain made it to a fully executed paper. Meta's
  claim that it trained for auto-research says nothing about whether Muse
  Spark 1.2 avoids those failure modes — this is a training-target claim, not
  a capability-verification claim, and should not be read as evidence the
  failure modes are solved.

### Claim 4: Training explicitly optimized for harness-level behaviors — compaction, subagents, and "goals" — via rejection-sampled harness trajectories, not just code-generation quality

- **Evidence**: Vendor-sourced training description, corroborated verbatim
  across Willison's post and the research-announcement page.
- **Confidence**: emerging (vendor-stated training methodology; "recipe
  optimizations" is not defined further, and there is no independent way to
  verify what was actually optimized or by how much)
- **Quote**: "The training included rejection sampled harness trajectories and
  recipe optimizations for goals, compaction, and subagents, alongside the
  integration of the Muse Code toolset to maximize harness compatibility."
- **Our assessment**: This is the single most harness-engineering-relevant
  claim in the source. Meta names "compaction" and "subagents" as explicit
  RL/rejection-sampling training targets — the same two concepts documented
  empirically at the harness-implementation level in
  `research-wasnotwas-context-compaction.md` (compaction trigger thresholds
  and cost across seven open-source harnesses) and
  `blog-addyosmani-code-agent-orchestra.md` (subagent delegation as a core
  orchestration pattern). This is the first source in the corpus where a
  foundation-model vendor describes training the model itself against
  harness-shaped trajectories, rather than practitioners building harness
  logic around a fixed model. If accurate, it means compaction-awareness and
  subagent-awareness are becoming baked into model weights, not just
  scaffolding — a meaningful shift for anyone designing custom harnesses
  against Meta's models.

### Claim 5: Muse Code uses async background agents that persist for the full session rather than being spawned per task, to avoid redundant information gathering

- **Evidence**: Direct architecture description on the research-announcement
  page (a page Willison links to but does not quote from directly).
- **Confidence**: settled (first-party architecture disclosure, though
  unverified by independent testing)
- **Quote**: "These specialized background agents remain active throughout
  each session, rather than being spawned for individual tasks, helping avoid
  redundant information gathering."
- **Our assessment**: This is a distinct pattern from the "spawn per task"
  sub-agent model documented elsewhere in the corpus (e.g.
  `subagents.spawn_agent` in `blog-simonwillison-muse-spark.md`, or Claude
  Code's Task tool in `blog-addyosmani-code-agent-orchestra.md`). Persisting
  background agents across a session trades isolation for continuity —
  avoiding the cost of re-establishing context each time a sub-task is
  delegated. No source in the corpus previously documented this session-scoped
  persistent-background-agent pattern as an alternative to per-task spawning.

### Claim 6: Muse Code uses a local, append-only event log recording every model call, tool run, approval, and edit, making the runtime "replay-exact and restart-safe"

- **Evidence**: Direct architecture description on the research-announcement
  page.
- **Confidence**: settled (first-party architecture disclosure, though
  unverified by independent testing)
- **Quote**: "Muse Code uses a local event log in which every model call,
  tool run, approval, and edit is appended. This single source of truth makes
  the runtime replay-exact and restart-safe."
- **Our assessment**: This is a concrete crash-recovery architecture pattern
  not previously documented in the corpus — an append-only event log as the
  single source of truth for a coding agent's state, enabling exact replay
  and safe restart after a crash. It's directly relevant to failure reports
  in this corpus about lost agent state (e.g. `failure-decker-4hr-session-loss.md`,
  `failure-beads-background-daemon.md`): an event-sourced runtime is one
  concrete design pattern for avoiding that class of failure, though we have
  no independent evidence yet of how well Muse Code's implementation holds up
  in practice.

### Claim 7: Muse Code ships three built-in skills — `/plan` (produces an approval-gated plan), `/grill` (stress-tests that plan), and `/goal` (works toward completing a specified objective)

- **Evidence**: Direct product description on the research-announcement page.
- **Confidence**: settled (first-party product disclosure)
- **Quote**: `/plan` "turns a task into an approval-gated plan"; `/grill`
  "stress-tests that plan until it holds up"; `/goal` "works toward successful
  completion of the specified objective"
- **Our assessment**: The plan → stress-test → execute sequence is a
  concrete, named implementation of the "plan before you code" pattern
  recommended widely elsewhere in the corpus, but the `/grill` step —
  explicitly adversarially stress-testing the plan before execution — is a
  specific named primitive we have not seen elsewhere. It's a plausible
  template for practitioners building their own planning workflows: separate
  the "produce a plan" step from an explicit "attack this plan" step before
  committing to execution.

### Claim 8: Meta offers Muse Spark 1.2 in two pricing tiers — a standard tier and a heavily discounted "contributor" tier conditioned on granting Meta permission to use submitted data to improve its products

- **Evidence**: Willison's pricing paragraph, corroborated by the exact same
  figures (plus cached-input rates) on the developer.meta.com model page.
- **Confidence**: settled (a specific, dated, checkable pricing table,
  corroborated across two independently-fetched sources)
- **Quote**: "An interesting twist on pricing is that the model is offered as
  two different model IDs. `muse-spark-1.2` is priced at $1.25/million input
  and $4.25/million output - close to Gemini 3.6 Flash ($1.50/$7.50) - but if
  you agree to let Meta use your data "to improve our products" you can use
  `muse-spark-1.2-contributor` which is $0.10/$0.20 - a huge discount, closer
  to GPT-5.6 Luna ($0.20/$1.20) and Gemini 3.1 Flash-Lite ($0.25/$1.50)."
- **Our assessment**: This is a distinct commercial pattern from the
  efficiency-driven price cut documented in
  `blog-simonwillison-gpt56-luna-price-drop.md` (OpenAI cut Luna's price 80%
  by making inference itself cheaper via self-optimized kernels). Here the
  ~92% discount ($1.25→$0.10 input, $4.25→$0.20 output) is conditioned
  entirely on a data-sharing consent choice, not on any underlying efficiency
  gain — the same model, same compute cost, priced differently based on data
  rights. Worth tracking as a second, orthogonal lever (alongside efficiency)
  vendors can pull to move price. The developer.meta.com page adds cached-input
  rates not in Willison's post: $0.15/M cached for the standard tier vs.
  $0.002/M cached for the contributor tier — a roughly 75x cache-price gap
  between the two tiers.

### Claim 9: Muse Spark 1.2 has a 1M-token context window

- **Evidence**: Direct statement on the developer.meta.com model page. Not
  mentioned in Willison's post or the research-announcement page.
- **Confidence**: settled (first-party spec disclosure)
- **Quote**: "The model features a substantial 1M context window, enabling
  extended development sessions without requiring restarts."
- **Our assessment**: This matches the industry direction already documented
  in `blog-anthropic-session-management-1m-context.md` and
  `docs-github-copilot-1m-context-reasoning-levels.md` — 1M-token context is
  becoming table stakes for coding-agent-class models rather than a
  differentiator. Combined with Claim 4 (training against compaction
  trajectories), Meta appears to be hedging both ends: a large context window
  to reduce how often compaction is needed, plus explicit training for
  graceful behavior when compaction does happen.

### Claim 10: Meta demonstrated Muse Code sustaining an autonomous run of 1,000+ tool calls over up to 24 hours to iteratively optimize GPU kernels (KDA and MLA) for NVIDIA Hopper hardware

- **Evidence**: Case study described on the research-announcement page,
  referenced only via chart images — no numeric speedup or success-rate
  results are given in the fetched text.
- **Confidence**: anecdotal (vendor's own marketing case study; no outcome
  metrics, failure rate, or independent reproduction)
- **Quote**: "iteratively optimize GPU kernels over 1,000+ tool calls (up to
  24 hours)" on "KDA and MLA kernels for NVIDIA Hopper GPUs"
- **Our assessment**: Notable primarily for the parallel to
  `blog-simonwillison-gpt56-luna-price-drop.md` (Claim 7), where OpenAI
  credited GPT-5.6 Sol with autonomously rewriting its own production
  inference kernels in Triton/Gluon for a 20% cost reduction — a claim with a
  quantified outcome. Meta's kernel-optimization case study has no comparable
  outcome number in the material we could fetch, only the duration/tool-call
  count. Two vendors independently choosing "long-horizon autonomous GPU
  kernel optimization" as a flagship demonstration of long-sequence agentic
  capability in the same year is a real pattern, but Meta's version reads
  as sustained-execution demonstration ("it ran that long without falling
  over") rather than a demonstrated performance win.

### Claim 11: Willison judges the Muse Spark 1.2 pelican-SVG benchmark as "a small but material improvement" over the 1.1 version

- **Evidence**: Willison's own recurring informal visual benchmark, applied
  consistently across many models in this corpus.
- **Confidence**: anecdotal (single practitioner's subjective visual
  judgment of one SVG image, no quantitative scoring)
- **Quote**: "You can see the Spark 1.1 pelican from 9th July here. I think
  the 1.2 pelican is a small but material improvement."
- **Our assessment**: Consistent with Willison's established methodology
  (`blog-simonwillison-muse-spark.md`, `blog-simonwillison-kimi-k3-pelican-benchmark.md`,
  `blog-simonwillison-pelicanmaxxing.md`) — informal but comparable across
  posts. Low evidentiary weight on its own, but useful as a directional,
  consistently-applied cross-model signal. Note that the intervening "Muse
  Spark 1.1" release (implied by the July 9 reference) does not have its own
  source note in this corpus — see Extraction Notes.

## Concrete Artifacts

### Muse Code bundled skills (Meta research-announcement page)

```
/plan  — turns a task into an approval-gated plan
/grill — stress-tests that plan until it holds up
/goal  — works toward successful completion of the specified objective
```
*Source: research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2*

### Muse Spark 1.2 pricing table (Willison's post + developer.meta.com)

```
Model ID                     Input        Cached Input   Output
muse-spark-1.2               $1.25/M      $0.15/M        $4.25/M
muse-spark-1.2-contributor   $0.10/M      $0.002/M       $0.20/M
                              (requires consent to Meta using submitted
                               data "to improve our products")

Comparison points (Willison):
  Gemini 3.6 Flash      $1.50/$7.50
  GPT-5.6 Luna          $0.20/$1.20
  Gemini 3.1 Flash-Lite $0.25/$1.50
```
*Source: simonwillison.net/2026/Aug/5/muse-code-and-muse-spark-12/ (pricing
paragraph and comparison figures); developer.meta.com/ai/models/muse-spark/
(cached-input rates, not present in Willison's post)*

### Benchmark names cited (no numeric scores in fetched text)

```
Terminal-Bench 2.1
DeepSWE 1.1
Meta Internal Coding Bench
```
*Source: research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2 —
displayed as bar-chart images; no numbers appear in the page's text.*

### Post tags (Willison's blog)

```
ai, generative-ai, llms, meta, llm-pricing, pelican-riding-a-bicycle,
llm-release, coding-agents
```
*Source: simonwillison.net/2026/Aug/5/muse-code-and-muse-spark-12/*

## Cross-References

- **Corroborates**:
  - **research-wasnotwas-context-compaction.md**: That note documents
    compaction as a real, measurable engineering concern across seven
    open-source harnesses (trigger thresholds, cost). Meta naming compaction
    as an explicit training target (Claim 4) corroborates that compaction has
    become a cross-vendor, cross-layer concern — both something practitioners
    engineer around and something foundation-model vendors now train against.
  - **blog-addyosmani-code-agent-orchestra.md**: Subagent delegation as a
    core orchestration pattern (Osmani) is echoed by Meta naming "subagents"
    as a training target (Claim 4) and shipping an async persistent
    background-agent architecture (Claim 5) — a second data point that
    sub-agent patterns are moving from practitioner convention toward vendor
    infrastructure.
  - **blog-simonwillison-gpt56-luna-price-drop.md**: Both this source (Claim
    10) and that note (its Claim 7) show a major vendor demonstrating
    long-horizon autonomous GPU kernel optimization as a flagship agentic
    capability in the same period (July-August 2026) — OpenAI with a
    quantified 20% cost-reduction outcome, Meta with an unquantified
    sustained-execution case study. This strengthens the case that
    kernel-level self-optimization is becoming a standard "look what
    long-horizon agentic tool calling can do" demonstration across vendors.
  - **blog-anthropic-session-management-1m-context.md** and
    **docs-github-copilot-1m-context-reasoning-levels.md**: Muse Spark 1.2's
    1M-token context window (Claim 9) is a third data point that 1M context
    is becoming a baseline expectation for coding-agent-class models, not a
    differentiator.

- **Contradicts**: None identified. No existing source note makes a claim
  that directly opposes anything reported here.

- **Extends**:
  - **blog-simonwillison-muse-spark.md**: Direct predecessor — the April
    2026 first-impression post on the original hosted Muse Spark and meta.ai's
    16-tool chat harness. This source is the August update: a dedicated
    coding agent (Muse Code) co-trained with the model, replacing the
    general-purpose-chat-plus-tools framing of the April post with a
    purpose-built coding-harness framing.
  - **blog-lilianweng-harness-engineering-rsi.md**: That note's "stabilized"
    coding-agent tool taxonomy (file system, shell, IO, external context,
    web search, artifacts, backend processes, agent delegation) is close to
    what Muse Code's own architecture description implies (background agents,
    event-log-backed tool runs, approval gates). It also supplies the
    auto-research failure-mode research (Trehan & Chopra 2026) that directly
    bears on how skeptically to read Claim 3's "trained for auto-research"
    claim.

- **Novel**:
  - **Training explicitly targeting harness-level trajectories** (compaction,
    subagents, goals) via rejection sampling (Claim 4) — no existing note
    documents a foundation-model vendor training the model itself against
    harness-shaped behavior rather than leaving that entirely to prompting/
    scaffolding.
  - **Session-persistent async background agents** as an alternative to
    per-task agent spawning (Claim 5) — not documented elsewhere in the
    corpus.
  - **Append-only local event log for replay-exact, restart-safe runtime**
    (Claim 6) — a concrete crash-recovery architecture pattern not previously
    documented.
  - **Data-sharing-conditioned two-tier pricing** (Claim 8) — a distinct
    monetization lever (data rights, not efficiency) from every other pricing
    change in the corpus.
  - **Gap identified, not a claim**: no source note in this corpus covers the
    intervening "Muse Spark 1.1" release referenced via the July 9 pelican
    link in Claim 11. If that post is ever submitted as its own source, it
    would fill a gap between the April (`blog-simonwillison-muse-spark.md`)
    and August (this note) data points.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Claim 4 (training against
  compaction/subagents/goals trajectories) and Claims 5-7 (async persistent
  background agents, replay-exact event-log runtime, `/plan`→`/grill`→`/goal`
  skill sequence) as concrete evidence that harness-shaped behavior is
  increasingly a vendor training-and-product concern, not solely something
  practitioners bolt on. The `/grill` adversarial-plan-stress-test primitive
  is a specific, nameable pattern worth citing alongside existing
  plan-before-code guidance.
- **Chapter 03 (Context Engineering)**: Cite Claim 9 (1M context window) and
  Claim 4 (compaction as an explicit training target) together as evidence
  that vendors are addressing context lifecycle from both ends — bigger
  windows to delay compaction, and training so the model degrades gracefully
  when compaction does happen — reinforcing the existing
  `research-wasnotwas-context-compaction.md` material.
- **Chapter 05 (Models & Costs, or wherever pricing patterns are discussed)**:
  Add Claim 8 (data-sharing-conditioned contributor pricing) as a second,
  distinct pricing lever alongside the efficiency-driven cuts already
  documented in `blog-simonwillison-gpt56-luna-price-drop.md`. Worth an
  explicit callout that a steep price difference between two otherwise
  identical model IDs does not always signal an efficiency gain — it can
  signal a data-rights trade instead, which has different implications for
  teams with data-sensitivity constraints.

## Extraction Notes

- **Followed 2 linked pages beyond Willison's post**: `research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2`
  (Meta's own announcement — architecture, training methodology, benchmark
  names, kernel case study) and `developer.meta.com/ai/models/muse-spark/`
  (pricing table with cached-input rates, 1M context window spec, access
  platforms). Both supplied substantive, verifiable detail not present in
  Willison's own post, consistent with how `blog-simonwillison-gpt56-luna-price-drop.md`
  incorporated OpenAI's own linked pages. A third link (a Hacker News
  discussion thread referenced by the fetch tool) was not followed — HN
  discussion threads are secondary commentary, not primary source material,
  and the two Meta pages already supplied the substantive technical content.
- **No numeric benchmark scores available**: The research-announcement page
  displays Terminal-Bench 2.1, DeepSWE 1.1, and Meta Internal Coding Bench
  results only as chart images; the fetched text could not extract numeric
  values from these charts. Flagged in Claim 10's Concrete Artifacts rather
  than fabricated.
- **Content retrieved via automated fetch/summarization, not direct
  rendering**: All three URLs (Willison's post and the two Meta pages) were
  retrieved through an automated fetch-and-extract tool rather than viewing
  rendered HTML directly. Quotes were requested and cross-checked across
  multiple targeted fetch passes per page to reduce the risk of paraphrase
  drift, but this note's quotes should be treated as high-confidence rather
  than manually eyeballed against raw HTML.
- **No contradiction filed**: Extraction did not surface a genuine
  contradiction with any existing source note — the auto-research tension
  with `blog-lilianweng-harness-engineering-rsi.md` (Claim 3) is a caution/
  context point, not two sources making opposing claims about the same
  specific fact, so no contradiction issue was filed per MINER.md §4a.
