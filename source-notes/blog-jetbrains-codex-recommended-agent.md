---
source_url: https://blog.jetbrains.com/ai/2026/06/codex-is-now-the-recommended-agent-in-jetbrains-ai/
source_type: blog-post
title: "Introducing a Recommended Agent in AI Chat, With Codex as the Current Default"
author: Anna Maltseva
date_published: 2026-06-25
date_extracted: 2026-07-03
last_checked: 2026-07-03
status: current
confidence_overall: emerging
issue: "#1456"
---

# Introducing a Recommended Agent in AI Chat, With Codex as the Current Default

> JetBrains publishes the benchmarking methodology behind picking a default
> "recommended agent" for JetBrains AI's Chat surface — 353 real-world tasks
> across Java/C#/Python, ranked by solve rate → cost → latency with a hard
> $20/month cost gate, validated by an online A/B test — and names Codex
> (GPT-5.4-mini, medium reasoning) the current winner over Junie, while
> explicitly scoping Junie as still-superior for IDE-deep, Java-heavy, BYOK,
> and cost-sensitive use cases.

## Source Context

- **Type**: blog-post (JetBrains AI blog, published June 25, 2026; author Anna
  Maltseva; practitioner/product post describing an internal agent-selection
  decision and the benchmarking process behind it)
- **Author credibility**: JetBrains AI team, writing about JetBrains' own
  product decision (which agent AI Chat recommends by default) and the
  internal benchmark JetBrains ran to make that decision. Authoritative for:
  what JetBrains measured, how it weighted the criteria, and what it decided.
  Not independently verified: the benchmark dataset itself is not published
  (no link to the actual task set or grading harness), so the specific solve
  rate numbers cannot be externally reproduced or audited. This is a vendor
  self-report of its own evaluation, not a third-party benchmark.
- **Scope**: Covers the "recommended agent" feature in JetBrains AI Chat (the
  native JetBrains AI Assistant product, not the GitHub Copilot plugin),
  the benchmark methodology and dataset composition, the ranking criteria and
  cost gate, head-to-head solve-rate/cost numbers for Codex vs. Junie, the
  online A/B test that validated the offline result, and the stated
  use-case-dependent carve-outs for Junie. Does NOT cover: benchmark
  methodology for agents other than Codex and Junie (Claude Agent and other
  ACP-compatible agents are mentioned as switchable options but not benchmarked
  in this post), the actual task dataset or grading harness code, or a
  timeline for when the recommendation might change.

## Extracted Claims

### Claim 1: JetBrains introduced a "recommended agent" feature in AI Chat that automatically selects an agent for the user, replacing the prior requirement to manually choose an agent at the start of every chat
- **Evidence**: Product change described as the article's framing premise, contrasted against the prior UX.
- **Confidence**: settled (shipped product feature, directly described)
- **Quote**: "Previously, AI users in JetBrains IDEs started in Chat mode and had to choose an agent themselves."
- **Our assessment**: This reframes agent selection from a per-session user decision into a vendor-curated default, with manual override still available (Claim 9). This is a UX pattern worth tracking: as the number of viable agents grows, vendors are starting to pick defaults on users' behalf rather than presenting an undifferentiated picker.

### Claim 2: JetBrains benchmarked candidate agents against 353 real software engineering tasks spanning three ecosystems: Java (225 tasks), C# (38 tasks), and Python (90 tasks)
- **Evidence**: Stated benchmark composition in the "Evaluation using real-world development tasks" section.
- **Confidence**: settled (specific, falsifiable numeric claim about JetBrains' own benchmark, though the underlying dataset is not published for external audit)
- **Quote**: "We evaluated candidate agents using a benchmark dataset built from real software engineering tasks across three ecosystems: Java (225 tasks), C# (38 tasks), and Python (90 tasks)."
- **Our assessment**: A 353-task, three-ecosystem benchmark is a meaningfully larger evaluation than many vendor-reported agent comparisons in the corpus, which often cite a single benchmark suite (e.g., SWE-bench Pro/Multilingual in `blog-cursor-reward-hacking-benchmarks.md`). The Java-heavy composition (225 of 353 tasks, ~64%) matches JetBrains' own IDE user base, which is a reasonable but non-generalizable sampling choice — practitioners on other stacks should not assume the same ranking holds for their ecosystem.

### Claim 3: Each benchmark task is grounded in a real codebase with a natural-language prompt and automated tests that verify the result, covering bug fixes, feature development, and enhancements
- **Evidence**: Direct methodology description of task construction and grading.
- **Confidence**: settled (concrete methodology statement)
- **Quote**: "Each task is grounded in a real codebase, with a prompt describing what needs to be done and automated tests that verify the result. Together, these tasks cover bug fixes, feature development, enhancements, and other common development tasks across real applications, libraries, frameworks, and developer tools."
- **Our assessment**: Automated pass/fail grading against real codebases (rather than synthetic or toy tasks) is a defensible design choice, but it inherits the same class of risk documented in `blog-cursor-reward-hacking-benchmarks.md` — an agent can pass automated tests via shortcuts (e.g., retrieving a known fix) rather than genuinely solving the task, and this post gives no indication that JetBrains audited for that failure mode. See Cross-References.

### Claim 4: JetBrains ranked candidate agents using three criteria in a fixed priority order — solve rate first, then cost, then latency
- **Evidence**: Explicit enumeration in the "Our methodology" section.
- **Confidence**: settled (explicit, ordered methodology statement)
- **Quote**: "In choosing which agent to recommend, we focused on three questions: 1. Can it handle the task?... 2. Is the cost reasonable?... 3. Is it fast enough?... These three metrics (solve rate, cost, and latency) formed the basis of our ranking."
- **Our assessment**: Solve rate is explicitly defined: "Here, we measured by solve rate – the percentage of benchmark tasks where all tests passed." This gives a reusable evaluation framework — solve rate → cost → latency, in that priority order — that other teams designing their own agent-selection process could adopt directly, rather than treating "which agent is best" as a single undifferentiated judgment call.

### Claim 5: Cost was applied as a hard exclusionary gate before ranking on quality: any agent configuration that would push more than 2% of users over $20/month in spend was ruled out entirely, not merely penalized
- **Evidence**: Explicit statement of the cost-gating rule in the methodology.
- **Confidence**: settled (explicit numeric threshold and gating logic)
- **Quote**: "Setups that would push more than 2% of users over $20/month were ruled out before we ranked candidates on quality and latency."
- **Our assessment**: This is a hard-gate-then-rank design, not a weighted-score design — cost is a pass/fail filter applied before solve rate and latency are even compared for the surviving candidates. This is a concrete, reusable pattern for teams setting agent/model defaults under a budget constraint: define a cost ceiling and an acceptable-user-percentage threshold, exclude anything that breaches it, and only then compare quality among survivors.

### Claim 6: In JetBrains' benchmark, Codex (GPT-5.4-mini) and Junie (Gemini 3 Flash) posted nearly identical overall solve rates (39.9% vs. 39.1%), with Codex ahead in Java and C# and Junie faster in Python
- **Evidence**: Head-to-head solve rate, cost, and cost-per-successful-solve figures reported for the two finalist agents.
- **Confidence**: settled (specific reported numbers, though not independently reproducible since the dataset is unpublished)
- **Quote**: (no direct quote; see paraphrase in Our assessment — the specific per-ecosystem breakdown and headline solve-rate numbers were returned to us as a structured comparison table rather than a single verbatim sentence, and MINER.md §2a prohibits presenting a reconstructed table as a quoted passage)
- **Our assessment**: A ~0.8 percentage-point gap in overall solve rate (39.9% vs. 39.1%) is close enough that offline benchmark solve rate alone would not obviously separate the two agents — which is precisely why JetBrains treated the A/B test (Claim 7) as the deciding signal rather than relying on the benchmark number alone. This is a notable methodological point: when offline benchmarks are this close, the vendor did not simply pick the higher number, they escalated to a second, independent validation signal before deciding.

### Claim 7: JetBrains validated the offline benchmark result with an online A/B test on real users, tracking activation, churn, and failure rate, and Codex "came out ahead" in that real-world test as well
- **Evidence**: Explicit description of the A/B test methodology and outcome in the "Final showdown: Junie vs Codex" section.
- **Confidence**: settled (explicit methodology and stated outcome, though exact magnitude of the A/B result is not quantified in the post)
- **Quote**: "We tracked activation, churn, and failure rate."
- **Our assessment**: Combining an offline task-based benchmark with an online behavioral A/B test is a stronger validation pattern than offline benchmarking alone — it checks whether the agent that wins on constructed tasks also produces better real-world engagement and lower churn, which is not guaranteed to correlate. No prior source note in this corpus documents a vendor pairing offline agent benchmarks with an online A/B test specifically for agent-selection decisions; this is a reusable due-diligence pattern for any team choosing a default agent/model, not just JetBrains' internal decision.

### Claim 8: Codex was named the recommended default because it delivered the strongest combination of solve rate and cost across the tested tasks
- **Evidence**: Explicit decision statement in the "What's next for the recommended agent" section.
- **Confidence**: settled (stated decision rationale)
- **Quote**: "Codex is now the recommended agent, having delivered the strongest combination of solve rate and cost across the tasks we tested."
- **Our assessment**: Notably, this rationale cites solve rate and cost, not latency — even though latency was the third stated ranking criterion (Claim 4). The post does not explain whether latency was a tiebreaker that didn't end up mattering, or whether it was simply omitted from this summary sentence. This is a minor gap in an otherwise transparent methodology writeup.

### Claim 9: Despite Codex being the new default, JetBrains explicitly states Junie remains the best choice for IDE-deep workflows, Java-heavy projects, BYOK setups, and cost-sensitive teams, and users can switch to Junie, Claude Agent, or other ACP-compatible agents at any time
- **Evidence**: Explicit use-case carve-out in the "Final showdown: Junie vs Codex" section, plus a statement that the agent picker remains user-overridable.
- **Confidence**: settled (explicit, direct statement of use-case-conditioned recommendation)
- **Quote**: "Junie still remains the best JetBrains-native agent for IDE-deep workflows, Java-heavy projects, BYOK setups and cost-sensitive teams."
- **Our assessment**: This is the single most practically important claim in the post for practitioners: "best agent" is explicitly framed as use-case-dependent, not a universal ranking. JetBrains is naming a default for the median/undifferentiated user while explicitly telling Java-heavy, BYOK, or cost-sensitive teams to override it. For the guide, this is a concrete example of a vendor publishing its own carve-outs to its own default recommendation — a rare level of transparency worth citing directly rather than treating "Codex is now recommended" as a blanket endorsement.

### Claim 10: JetBrains frames the recommendation as provisional and expects to re-evaluate and update it as models evolve, new agents join, and benchmark coverage expands
- **Evidence**: Explicit forward-looking statement in the "What's next for the recommended agent" section.
- **Confidence**: settled (explicit statement of intent; the claim is about JetBrains' stated process, not a prediction requiring outside verification)
- **Quote**: "This isn't a permanent decision, however. As models evolve, new agents join, and our benchmark coverage grows, we'll re-evaluate the decision and update our recommendation based on what the data tells us."
- **Our assessment**: This confirms the "recommended agent" is a living default tied to a repeatable evaluation process, not a one-time marketing claim. Practitioners relying on this guide should treat "Codex is JetBrains' recommended agent" as a June 2026 snapshot, not a durable fact — `last_checked` on this note should be revisited if the guide cites this claim after mid-2026.

## Concrete Artifacts

### Benchmark composition and ranking methodology (JetBrains AI, June 25, 2026)

```
Benchmark dataset: 353 real software engineering tasks
  Java:   225 tasks (across 17 repositories)
  C#:      38 tasks (internal dataset)
  Python:  90 tasks

Task construction: real codebase + natural-language prompt + automated
  tests verifying the result. Covers bug fixes, feature development,
  enhancements, and other common development tasks.

Ranking criteria, in priority order:
  1. Solve rate — % of benchmark tasks where all tests passed
  2. Cost — median cost per task; configurations pushing >2% of users
             over $20/month were excluded before ranking on quality/latency
  3. Latency — median end-to-end latency

Validation: online A/B test with real users, tracking activation, churn,
  and failure rate — used to confirm the offline benchmark result before
  finalizing the default.

Source: "Introducing a Recommended Agent in AI Chat, With Codex as the
Current Default," JetBrains AI blog, June 25, 2026 (Anna Maltseva).
```

### Codex vs. Junie head-to-head results (as reported)

```
Metric                          Codex (GPT-5.4-mini)   Junie (Gemini 3 Flash)
Solve rate (overall)            39.9%                   39.1%
Solve rate (Java)               43.9%                   45.2%
Solve rate (C#)                 62.6%                   58.7%
Median cost per task            $0.1387                 $0.1132
Cost per successful solve       $0.4941                 $0.4337

Junie reported as faster on Python tasks; exact latency figures not
extracted verbatim from the source.

Decision: Codex named default recommended agent based on combined
solve rate + cost; Junie explicitly retained as the better choice for
IDE-deep workflows, Java-heavy projects, BYOK setups, and cost-sensitive
teams.
```

## Cross-References

### Cross-reference verification notes
Claims cited from other source notes below were re-read directly in those
notes before citing (per MINER.md §4b); claim numbers are counted
top-to-bottom in document order as they appear in each cited note.

- **Corroborates**:
  - `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md` Claim 1:
    that note documents GitHub Copilot becoming a selectable, ACP-compatible
    agent inside JetBrains AI Assistant's own agent picker ("GitHub Copilot
    is a first-class option in the AI Assistant agent picker"). This post's
    Claim 9 mentions "other ACP-compatible options" as switchable
    alternatives to the recommended agent in the same AI Chat surface,
    corroborating that the AI Assistant agent picker now hosts multiple
    ACP-connected third-party agents (at minimum Copilot, per that note) in
    addition to JetBrains' own Junie and OpenAI's Codex.
  - `blog-cursor-cursorbench.md` and `blog-cursor-reward-hacking-benchmarks.md`
    (general pattern): both establish that real, automated-test-graded
    software engineering task suites are the emerging standard for agent
    evaluation, rather than synthetic benchmarks or subjective review. This
    post's 353-task, three-ecosystem benchmark (Claim 2) follows the same
    general pattern independently at a different vendor.

- **Contradicts**: None identified directly, but this source raises an
  unaddressed methodological question relative to
  `blog-cursor-reward-hacking-benchmarks.md`. That note's central claim is
  that automated-test-graded coding benchmarks are vulnerable to "runtime
  contamination" — agents retrieving a known fix (e.g., from git history or
  upstream sources) rather than deriving it, inflating solve rate without
  reflecting genuine problem-solving (see that note's summary and Source
  Context). This JetBrains post's benchmark (Claim 3) uses the same
  automated-test-pass/fail grading design, on real codebases, without
  mentioning any contamination audit, isolation of git history, or egress
  proxying (the two mitigations documented in the Cursor note). This is not
  a contradiction between two stated claims — JetBrains makes no claim about
  contamination one way or the other — so per MINER.md §4a ("one side is so
  weakly supported it doesn't rise to a real claim" / claims differing only
  by omission rather than by asserting opposing positions) this does not
  meet the bar for filing a contradiction issue. It is flagged here as an
  open methodological gap instead: the Assayer/Smith should treat JetBrains'
  reported solve-rate gap between Codex and Junie (39.9% vs. 39.1%, Claim 6)
  as potentially inflated by the same contamination risk Cursor documents,
  until JetBrains discloses whether its harness guards against it.

- **Extends**:
  - `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md`: that
    note documents the AI Assistant/AI Chat agent-picker surface and one of
    its selectable agents (Copilot via ACP) but does not discuss any
    default/recommended agent behavior — it describes Copilot as one
    manually-selectable option among others. This post extends that picture
    by describing the same picker's new default-selection behavior (Claim 1)
    and naming the vendor's own benchmarking process for choosing that
    default (Claims 2–8), filling a gap that note explicitly left open.
  - `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md`: that
    note documents Claude becoming a selectable agent provider inside the
    separate GitHub Copilot *plugin's* own agent picker (a different surface
    from AI Assistant/AI Chat). This post's mention of "Claude Agent" as one
    of the switchable alternatives to the recommended agent (Claim 9) is
    adjacent but not confirmed to be the identical integration — this note
    does not assert they are the same underlying Claude integration, since
    the JetBrains post does not specify which product surface hosts its
    "Claude Agent" option. Flagged as an open question rather than assumed.

- **Novel**:
  - **A vendor-published, numeric, multi-criterion agent-selection
    methodology** (Claims 2, 4, 5): no prior source note in this corpus
    documents a vendor's internal process for choosing a *default* agent
    among multiple viable options, including a hard cost gate and priority
    ordering of criteria. Prior corpus benchmarking sources
    (`blog-cursor-cursorbench.md`, `blog-cursor-reward-hacking-benchmarks.md`)
    document benchmark *design* and its failure modes, not a vendor's
    agent-selection decision process built on top of a benchmark.
  - **Offline benchmark + online A/B test as a combined validation pattern
    for agent selection** (Claim 7): this is the first corpus source
    describing a vendor pairing a task-based offline benchmark with a live
    user A/B test specifically to validate an agent-default decision.
  - **Explicit, vendor-published use-case carve-outs to its own default
    recommendation** (Claim 9): no prior corpus source shows a vendor
    naming specific segments (IDE-deep workflows, Java-heavy projects, BYOK,
    cost-sensitive teams) for which its own new default is *not* the best
    choice, in the same post announcing the default.

## Guide Impact

- **Chapter 04 (Evaluation and benchmarking methodologies)**: Add the
  solve-rate → cost → latency priority ordering (Claim 4) and the hard
  cost-gate design (Claim 5: exclude before ranking on quality, not
  weighted-penalize) as a concrete, reusable framework for teams selecting a
  default agent/model under a budget constraint. Add the offline-benchmark +
  online-A/B-test combination (Claim 7) as a recommended two-stage validation
  pattern — offline benchmarks alone did not resolve a near-tie (39.9% vs.
  39.1%) between Codex and Junie, so JetBrains treated live user behavior as
  the deciding signal. Flag the unaddressed contamination-audit gap relative
  to `blog-cursor-reward-hacking-benchmarks.md` (see Cross-References) as a
  question the guide should raise when citing vendor-reported solve rates
  generally: does the benchmark harness guard against agents retrieving
  known fixes rather than deriving them?

- **Chapter 02 (Agentic patterns and design — agent selection)**: Add
  Claim 9 (Junie retained for IDE-deep workflows, Java-heavy projects, BYOK,
  cost-sensitive teams) as a concrete illustration of the guide's existing
  "best agent is use-case dependent" position — this is a vendor explicitly
  publishing its own exceptions to its own default, which is stronger
  evidence than a generic statement that agent choice varies by context.
  Update any guide language describing JetBrains AI Chat/AI Assistant as
  presenting an undifferentiated agent picker — as of June 25, 2026 it now
  auto-selects a default (Codex) with manual override still available to
  Junie, Claude Agent, or ACP-compatible agents (Claim 1, Claim 9).

## Extraction Notes

1. **WebFetch returned an AI-summarized/paraphrased pass first**: as with
   several prior source notes in this corpus, the first WebFetch call
   returned a summarized version of the article, not usable for direct
   quotes per MINER.md §2a. Two additional targeted WebFetch calls were made
   with narrower prompts asking for short, verbatim, sub-40-word sentence
   fragments with their source section named, to recover quotable text
   without risking a splice of non-adjacent sentences (MINER.md §2a.3). All
   `Quote` fields above were copied from those targeted-fetch outputs.
2. **No direct quote for the head-to-head numeric comparison (Claim 6)**:
   the per-ecosystem solve-rate/cost/cost-per-solve breakdown was returned to
   us as a structured comparison, not a single verbatim source sentence.
   Rather than reconstruct a sentence that reads as the source's own words
   when it isn't, Claim 6's Quote field is left as an explicit non-quote per
   MINER.md §2a.5, and the numbers are presented in the Concrete Artifacts
   table instead with a note that exact latency figures were not extracted
   verbatim.
3. **Underlying benchmark dataset is not published**: the post reports
   solve-rate, cost, and cost-per-solve figures but does not link to the 353
   tasks, the grading harness, or raw per-task results. All numeric claims in
   this note (Claims 2, 6) should be understood as vendor-reported and not
   independently reproducible from the source alone.
4. **No sub-pages followed**: the article is a self-contained blog post with
   no linked sub-pages (e.g., a separate methodology whitepaper or dataset
   repository) that would meet the "substantive linked page" bar in
   MINER.md §1.
5. **Contamination-gap flagged, not filed as a contradiction**: see
   Cross-References → Contradicts. This is an omission on JetBrains' part
   (no statement either way about contamination auditing), not a stated
   claim that opposes `blog-cursor-reward-hacking-benchmarks.md` — per
   MINER.md §4a this does not meet the bar for a contradiction issue, but it
   is flagged prominently for the Assayer/Smith to weigh when citing
   JetBrains' solve-rate numbers in the guide.
