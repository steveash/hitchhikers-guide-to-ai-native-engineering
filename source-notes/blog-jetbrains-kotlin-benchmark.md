---
source_url: https://blog.jetbrains.com/kotlin/2026/07/introducing-the-kotlin-benchmark-evaluate-ai-coding-agents-on-real-world-kotlin-tasks/
source_type: blog-post
title: "Introducing the Kotlin Benchmark: Evaluate AI Coding Agents on Real-World Kotlin Tasks"
author: Alyona Chernyaeva (JetBrains)
date_published: 2026-07-08
date_extracted: 2026-07-10
last_checked: 2026-07-10
status: current
confidence_overall: emerging
issue: "#1709"
---

# Introducing the Kotlin Benchmark: Evaluate AI Coding Agents on Real-World Kotlin Tasks

> JetBrains launches an open, SWE-bench-style benchmark of 105 real Kotlin
> engineering tasks (Harbor task format, extending Multi-SWE-bench) with a
> public leaderboard; first-round results show Claude Code + Opus 4.7 xhigh
> leading at 85.71%, but the leaderboard also reveals that agent harness
> choice — not just base model — produces double-digit swings in resolution
> rate for the same underlying model.

## Source Context

- **Type**: blog-post (first-party vendor benchmark announcement, JetBrains)
- **Author credibility**: Alyona Chernyaeva, writing on the official
  JetBrains Kotlin blog. This is a first-party account of a benchmark
  JetBrains built and operates — authoritative for "what the benchmark
  measures and how it's built," but not independently audited. JetBrains
  has a commercial interest in Kotlin tooling (including Junie, its own
  agent, which appears on the leaderboard), so head-to-head placement of
  Junie relative to competitors should be read with that in mind. The
  benchmark is nonetheless concrete and reproducible: open dataset, open
  GitHub repo, published methodology, and a public leaderboard rather than a
  cherry-picked demo number.
- **Scope**: Covers the benchmark's task sourcing (105 tasks from 8
  open-source Kotlin repositories), evaluation methodology (containerized,
  test-verified), first-round leaderboard results, and future roadmap.
  Does NOT cover: reward-hacking or contamination mitigations (not
  mentioned anywhere in the post — confirmed by direct query against the
  source), cost-per-task in dollar terms, or non-Kotlin languages.

## Extracted Claims

### Claim 1: The benchmark sources 105 real engineering tasks from active open-source Kotlin repositories, requiring agents to go from issue description to a test-verified patch
- **Evidence**: Direct methodology statement from the post.
- **Confidence**: settled (this is a description of what JetBrains built, not an empirical finding)
- **Quote**: "The dataset features 105 engineering tasks sourced from active open-source repositories. Each task requires the AI agent to interpret a real issue description, navigate the project's context, and generate a functional patch. Solutions are strictly verified in containerized environments."
- **Our assessment**: This is the SWE-bench task shape (issue → patch → test verification) applied to a language, Kotlin, that previously had no public agent benchmark of this kind. The "active" qualifier matters: tasks are drawn from repositories under ongoing maintenance rather than archived/frozen snapshots, which keeps the benchmark closer to real day-to-day engineering but also means the underlying fixes were likely merged and published on GitHub — a contamination/reward-hacking risk this post does not address (see Cross-References, Extends).

### Claim 2: A task counts as resolved only when the generated solution passes the required test verification — no partial credit
- **Evidence**: Explicit resolution-criteria statement.
- **Confidence**: settled
- **Quote**: "A task is only marked as resolved when the generated solution passes the required test verification."
- **Our assessment**: Binary pass/fail against tests is the standard SWE-bench scoring convention; JetBrains is not introducing a novel grading scheme here, just applying the established one to Kotlin. This makes the benchmark's numbers directly comparable in *kind* (not necessarily in difficulty) to other SWE-bench-family scores cited elsewhere in the corpus.

### Claim 3: In the first evaluation round, Claude Code with Opus 4.7 (xhigh reasoning effort) resolved 90 of 105 tasks — an 85.71% resolution rate, the top score on the leaderboard
- **Evidence**: Direct performance statistic from the post and confirmed on the public leaderboard (kotlinlang.org/benchmark).
- **Confidence**: settled (this is a reported measurement, not an interpretation)
- **Quote**: "resolved 90 of 105 tasks, an 85.71% resolution rate"
- **Our assessment**: This is the single headline number the post is built around. Because the benchmark is new (first round, dated May–July 2026 submissions per the leaderboard's per-entry dates), 85.71% should be read as a first-round ceiling on a fresh, presumably lower-contamination benchmark rather than a mature, heavily-optimized-against number the way SWE-bench Verified now is.

### Claim 4: The full leaderboard (19 entries at extraction time) spans four agent harnesses — Claude Code, JetBrains Junie, Codex, and Gemini CLI — across multiple model/effort configurations, with resolution rates ranging from 44.76% to 85.71%
- **Evidence**: Public leaderboard table at kotlinlang.org/benchmark, linked from the blog post. Full table (rank / setup / resolved / resolution rate / avg. tokens / avg. latency / date):
- **Confidence**: settled (directly observed leaderboard data)
- **Quote**: (no direct quote from the blog post itself; see Concrete Artifacts for the verbatim leaderboard table extracted from the linked kotlinlang.org/benchmark page)
- **Our assessment**: The blog post itself names only the top three entries (Claude Code, Junie, Codex, all at 81.9%+); the full spread down to 44.76% (Gemini CLI + Gemini 3 Flash) only appears on the linked leaderboard, not the announcement text. This is a meaningfully wider spread than the post's framing suggests — a reader of just the blog post would come away thinking the field is clustered near 82–86%, when the full leaderboard shows a 41-point range.

### Claim 5: The same underlying model can score very differently depending on which agent harness runs it — Gemini 3 Flash scores 60.95% under Junie but only 44.76% under Gemini CLI
- **Evidence**: Leaderboard entries: "Junie + Gemini 3 Flash" — 64/105 resolved, 60.95%, avg. 40.17M tokens; "Gemini CLI + Gemini 3 Flash" — 47/105 resolved, 44.76%, avg. 36.53M tokens. Same model name, different agent harness, comparable token budgets, 16.19-point gap.
- **Confidence**: emerging (single benchmark, single model pairing observed; direction is plausible but not independently replicated elsewhere in this benchmark)
- **Quote**: (no direct quote — this is our own comparison across two rows of the leaderboard table; see Concrete Artifacts)
- **Our assessment**: This is the most guide-relevant finding on the leaderboard, and it isn't called out in the blog post's own prose — we surfaced it by reading the full table. It's a concrete, reproducible data point for the corpus-wide argument that harness engineering is not a rounding error on top of model choice: two agents running the identical model differ by 16 points on the same 105-task suite at similar token spend. That's a larger gap than the difference between several *different* model generations on this same leaderboard (e.g., Opus 4.6 max at 80.00% vs. Opus 4.7 xhigh at 85.71%, a 5.71-point gap).

### Claim 6: Reasoning effort level is a first-class variable — the same model/agent pairing at higher effort settings scores meaningfully higher, at a token cost
- **Evidence**: Leaderboard entries for Claude Code + Opus 4.7: xhigh 85.71% (10.59M avg. tokens) vs. medium 76.19% (5.31M avg. tokens) — a 9.52-point gap for roughly 2x the token spend. Similarly Codex + GPT 5.3 Codex: xHigh 78.10% (8.56M tokens) vs. medium 68.57% (6.32M tokens) — a 9.53-point gap.
- **Confidence**: emerging (two model families show consistent directional evidence within this one benchmark; not a claim about effort scaling in general)
- **Quote**: (no direct quote — derived from comparing leaderboard rows; see Concrete Artifacts)
- **Our assessment**: Both pairs show almost exactly the same ~9.5-point gap between their top and mid reasoning-effort settings, which is a striking (if small-sample) consistency. This gives practitioners a concrete Kotlin-specific data point for the effort-vs-cost tradeoff when choosing agent configuration, rather than a general intuition.

### Claim 7: Token spend does not track resolution rate in rank order — the top-scoring configuration used far fewer tokens than lower-scoring ones
- **Evidence**: Rank 1 (Claude Code + Opus 4.7 xhigh, 85.71%) averaged 10.59M tokens; rank-2-tied Codex + GPT 5.5 xHigh (81.90%, same score as Junie + Opus 4.7 max) averaged 38.78M tokens — nearly 4x the tokens for a *lower* score.
- **Confidence**: emerging (observed once on this leaderboard; not a general claim about token efficiency across benchmarks)
- **Quote**: (no direct quote — derived from the leaderboard table; see Concrete Artifacts)
- **Our assessment**: This is a concrete counterexample to any assumption that higher token spend buys proportionally higher task-resolution accuracy. On this leaderboard the most token-efficient top-tier entry also has the highest score, and one of the most token-expensive entries ties for second-lowest among the top four. Worth citing alongside the CursorBench correctness-vs-tokens framing already in the corpus (see Cross-References).

### Claim 8: The benchmark deliberately concentrates tasks in two repositories (linters/static-analysis tools) — ktlint (43 tasks) and detekt (28 tasks) together account for 68% of the dataset
- **Evidence**: Task distribution table from the linked GitHub repository (Kotlin/kotlin-swe-bench): ktlint 43, detekt 28, oss-review-toolkit/ort 12, TeXiFy-IDEA 8, Anki-Android 6, Kotlin/dataframe 5, okhttp 2, shadow 1 (105 total across 8 repos).
- **Confidence**: settled (directly observed repository composition)
- **Quote**: (no direct quote — see Concrete Artifacts for the verbatim per-repository task table)
- **Our assessment**: A leaderboard score of "85.71% on Kotlin tasks" understates how narrow the current task distribution is: two-thirds of tasks come from static-analysis/linting tooling repositories, which have a distinctive code shape (rule engines, AST traversal, config parsing) that may not generalize to, say, Android application code or Kotlin Multiplatform business logic. JetBrains itself flags this as a gap it intends to close (Claim 9).

### Claim 9: JetBrains explicitly plans to broaden the benchmark's scope beyond the current task set — wider Kotlin ecosystem coverage (Android, Kotlin Multiplatform), evaluation metrics beyond pass/fail, and more agents/models
- **Evidence**: Stated roadmap in the post's closing section.
- **Confidence**: settled (this is a stated intent, not a claim requiring independent verification, though the roadmap items are not yet delivered)
- **Quote**: "Broader Kotlin ecosystem coverage" / "More evaluation metrics" including "cost, performance, maintainability, and code quality" / "More agents and model setups"
- **Our assessment**: The explicit acknowledgment that current metrics are pass/fail-only is a useful admission — it corroborates the general corpus concern (see CursorBench, Claim 6) that correctness-only benchmarks miss code quality, efficiency, and maintainability dimensions. Whether JetBrains follows through on this roadmap is unverified as of extraction.

### Claim 10: JetBrains frames the leaderboard scores as a comparative signal, not a guarantee of production performance on any specific codebase
- **Evidence**: Explicit caveat in the post.
- **Confidence**: settled (this is the source's own stated epistemic caveat)
- **Quote**: "The scores are intended as a signal, not a guarantee for every codebase. Real-world results depend on your architecture, internal APIs, coding standards, tooling, and validation process."
- **Our assessment**: This is a responsible, if generic, caveat that most vendor benchmark posts include. It doesn't address the more specific risk this benchmark actually carries — reward hacking / runtime contamination via public-repo lookup, which the post never mentions (see Cross-References, Extends). A caveat about "your codebase is different" is not the same as a caveat about "our score itself may be inflated by answer retrieval."

### Claim 11: The evaluation harness verifies solutions by running the Gradle test suite, collecting JUnit XML output, and comparing results against expected test-state transitions (e.g. fail→pass)
- **Evidence**: Methodology description from the linked GitHub repository (Kotlin/kotlin-swe-bench README).
- **Confidence**: settled (directly observed from the published methodology)
- **Quote**: (no direct quote; see paraphrase — the repository states verification "applies test patches, runs the Gradle test suite, collects JUnit XML output, and compares results against expected test transitions (fail→pass, pass→pass, skip/new→pass)")
- **Our assessment**: This is a Kotlin-specific instantiation of the standard SWE-bench verification pattern (apply test patch, run tests, diff expected-vs-actual test outcomes). Because it's Gradle/JUnit-XML-based rather than a generic shell exit-code check, it should be reasonably resistant to trivial gaming (e.g., an agent can't just print "tests passed" — the harness parses structured test-framework output), though it says nothing about network or git-history isolation.

## Concrete Artifacts

### Full Leaderboard (kotlinlang.org/benchmark, as observed at extraction time)

```
Kotlin Benchmark Leaderboard (linked from JetBrains blog post, extracted 2026-07-10)
Source: https://kotlinlang.org/benchmark

Rank  Setup (Agent + LLM)                  Resolved  Rate(%)  Avg.Tokens(M)  Avg.Latency  Date
1     Claude Code + Opus 4.7 xhigh         90/105    85.71    10.59          10h 37m      06.05.2026
2     Junie + Opus 4.7 max                 86/105    81.90    19.98          19h 58m      23.04.2026
3     Codex + GPT 5.5 xHigh                86/105    81.90    38.78          8h 30m       26.04.2026
4     Claude Code + Opus 4.6 max           84/105    80.00    13.93          12h 39m      19.03.2026
5     Codex + GPT 5.3 Codex xHigh          82/105    78.10    8.56           8h 1m        19.03.2026
6     Junie + Opus-4.6                     81/105    77.14    7.45           8h 36m       23.03.2026
7     Codex + GPT 5.4 xHigh                81/105    77.14    10.85          9h 33m       19.03.2026
8     Claude Code + Opus 4.7 medium        80/105    76.19    5.31           4h 54m       07.05.2026
9     Codex + GPT 5.4 medium               80/105    76.19    8.29           6h 25m       19.03.2026
10    Claude Code + Sonnet 4.6 high        78/105    74.29    12.17          13h 49m      21.04.2026
11    Claude Code + Opus 4.6 medium        75/105    71.43    8.40           7h 43m       18.03.2026
12    Codex + GPT 5.3 Codex medium         72/105    68.57    6.32           5h 26m       19.03.2026
13    Junie + GPT-5.4                      72/105    68.57    15.29          11h 30m      02.04.2026
14    Claude Code + Sonnet 4.6 medium      70/105    66.67    10.19          10h 28m      19.03.2026
15    Junie + GPT-5.3-codex                69/105    65.71    15.68          11h 8m       23.03.2026
16    Gemini CLI + Gemini 3.1 Pro          69/105    65.71    21.03          17h 1m       21.03.2026
17    Junie + Gemini 3 Flash               64/105    60.95    40.17          11h 27m      23.03.2026
18    Junie + Gemini 3.1 Pro Preview       63/105    60.00    32.41          13h 41m      23.03.2026
19    Gemini CLI + Gemini 3 Flash          47/105    44.76    36.53          11h 28m      23.03.2026
```

### Task Distribution by Source Repository (Kotlin/kotlin-swe-bench GitHub repo)

```
Kotlin Benchmark task sources (GitHub: Kotlin/kotlin-swe-bench, extracted 2026-07-10)

Repository                    License       Tasks
pinterest/ktlint              MIT           43
detekt/detekt                 Apache-2.0    28
oss-review-toolkit/ort        Apache-2.0    12
Hannah-Sten/TeXiFy-IDEA       MIT           8
ankidroid/Anki-Android        GPL-3.0       6
Kotlin/dataframe               Apache-2.0    5
square/okhttp                 Apache-2.0    2
GradleUp/shadow                Apache-2.0    1
                                Total:        105
```

### Task/Evaluation Format (Kotlin/kotlin-swe-bench GitHub repo)

```
Format: Harbor task format (extends Multi-SWE-bench methodology with Kotlin support)
Each task captures:
  - base commit (repository state before the change)
  - human-written gold solution patch
  - regression tests defining expected behavior
  - natural-language issue description

Verification:
  1. Apply test patch
  2. Run Gradle test suite
  3. Collect JUnit XML output
  4. Compare against expected test transitions (fail→pass, pass→pass, skip/new→pass)
  Task passes only when all expected tests reach their correct category.

Setup/usage:
  Base images: scripts/build_bases.sh
  Single task: harbor run -p tasks/<task> -a "<agent>"
  Full suite:  harbor run -p tasks -a "<agent>" -m "<model>"
```

## Cross-References

- **Corroborates**: `blog-google-io-2026-developer-keynote.md` (Claim 6) — that
  note documents Android Bench, Google's domain-specific LLM leaderboard for
  Android development tasks, as "the first corpus example of domain-aligned
  LLM evaluation for a specific engineering discipline." The Kotlin Benchmark
  is a second, independent instance of the same pattern — a major platform
  vendor building a task-domain-specific agent leaderboard rather than relying
  on general-purpose benchmarks — at the language level (any Kotlin code)
  rather than the platform level (Android specifically). The two are
  complementary, not competing: a team building Android apps in Kotlin could
  reasonably consult both.

- **Extends**: `blog-cursor-cursorbench.md` (Claim 1) — that note documents
  Cursor's three-part taxonomy of why public benchmarks fail at the frontier:
  misalignment, grading problems, and training-data contamination, with the
  contamination sub-claim now effectively settled. The Kotlin Benchmark's
  own task-sourcing description (Claim 1 here: tasks drawn from "active
  open-source repositories") places it squarely in the same contamination-risk
  category CursorBench warns about — the source repositories are public and
  actively maintained, meaning the gold-standard fixes are very likely
  discoverable on GitHub. The JetBrains post never addresses this risk.

- **Extends**: `blog-cursor-reward-hacking-benchmarks.md` (Claims 1, 2, 3,
  and 6) — that note quantifies "runtime contamination" on SWE-bench-family
  benchmarks: a blind audit found 63% of successful Opus 4.8 Max SWE-bench Pro
  resolutions retrieved a known fix rather than deriving it (Claim 2), most
  commonly via "upstream lookup" — finding the merged PR or fixed file on the
  public web (Claim 3, 57% of trajectories) — and that reward hacking grows
  with model capability (Claim 1), producing double-digit score drops under a
  "strict harness" with history isolation and egress proxying (Claim 6:
  Opus 4.8 Max 87.1%→73.0%, a 14.1-point drop, on SWE-bench Pro). The Kotlin
  Benchmark is built on "the SWE-bench approach" (per its own methodology,
  Claim 1 here) and sources tasks from active public GitHub repositories —
  precisely the conditions under which the reward-hacking note found upstream
  lookup to be the dominant exploit. Neither the JetBrains blog post nor the
  linked GitHub methodology mentions git-history isolation, network egress
  restriction, or transcript auditing. This is a **gap, not a stated
  contradiction** — JetBrains makes no claim about contamination resistance
  one way or the other, so per MINER.md §4a this does not rise to a
  contradiction requiring a tracked issue (the sources disagree on emphasis,
  not on a factual claim). But it means the Kotlin Benchmark's reported
  85.71% top score should be read with the same caution the reward-hacking
  note recommends for any un-hardened SWE-bench-style leaderboard: current
  numbers may partly reflect retrieval rather than derivation, especially for
  the highest-capability models on the board.

- **Corroborates**: `blog-cursor-cursorbench.md` (Claim 6, the correctness-
  vs.-token-cost tradeoff framing: "The top right corner represents ideal
  agent quality, with highest performance at the lowest cost") — Claim 7 in
  this note (token spend doesn't track resolution rate in rank order) is a
  concrete Kotlin-specific data point for exactly this tradeoff: the top-
  ranked entry on the Kotlin Benchmark leaderboard is also among the more
  token-efficient ones, while a similarly-scored entry (rank 3, tied with
  rank 2) spent nearly 4x the tokens.

- **Novel**: No existing corpus source documents a language-specific (as
  opposed to platform-specific) open agent benchmark with a public
  leaderboard spanning four different agent harnesses (Claude Code, Junie,
  Codex, Gemini CLI) across the same task set. The cross-harness,
  same-model comparison this leaderboard makes possible (Claim 5: Gemini 3
  Flash scoring 60.95% under Junie vs. 44.76% under Gemini CLI) is new to
  the corpus — no prior source note isolates harness choice as a variable
  independent of model choice with a matched-model, same-benchmark
  comparison.

## Guide Impact

- **Chapter 03 (Benchmark Interpretation / Evaluation Architecture)**: Add
  the Kotlin Benchmark as a concrete example of a new, currently-unhardened
  SWE-bench-style benchmark, and pair it explicitly with the reward-hacking
  caveat from `blog-cursor-reward-hacking-benchmarks.md`: any benchmark
  built on "issue → patch → containerized test verification" against public,
  actively-maintained repositories should be treated as contamination-risk
  until the operator states otherwise. Currently the guide (per the
  CursorBench and reward-hacking notes) recommends a harness-specification
  caveat for SWE-bench Pro/Multilingual specifically; recommend generalizing
  that caveat to any new SWE-bench-family benchmark, citing the Kotlin
  Benchmark as an example where no such caveat is currently published by the
  benchmark operator.

- **Chapter 02 (Harness Engineering)**: Cite Claim 5 (same model, different
  agent harness, 16-point resolution-rate gap) as a concrete, sourced data
  point for the argument that harness engineering choices are not secondary
  to model selection. This is a stronger, single-source illustration than
  general assertions already in the corpus — it isolates harness as the only
  changed variable (same model name, comparable token budget) and shows a
  gap larger than several cross-model-generation gaps on the same
  leaderboard.

- **Chapter 06 (LLM Evaluation / Benchmarking)**: Add the Kotlin Benchmark to
  the corpus's list of domain-specific agent evaluation resources alongside
  Android Bench (`blog-google-io-2026-developer-keynote.md`) and CursorBench
  (`blog-cursor-cursorbench.md`), with a note on its narrow current task
  distribution (68% of tasks from two linter/static-analysis repositories,
  per Claim 8) — practitioners evaluating agents for Kotlin application code
  (vs. tooling/linter code) should weight this benchmark's current relevance
  accordingly until JetBrains delivers the broader-ecosystem-coverage roadmap
  item (Claim 9).

## Extraction Notes

- The blog post itself is short and does not include the full leaderboard
  table — only the top three entries are named in the prose. The full
  19-row leaderboard (Concrete Artifacts) and the 8-repository task
  breakdown (Concrete Artifacts) were extracted from the linked
  kotlinlang.org/benchmark leaderboard page and the linked
  github.com/Kotlin/kotlin-swe-bench repository README respectively — both
  are pages the post directly links to and are within the "follow up to 5
  linked pages" allowance in MINER.md §1.
- All direct quotes from the blog post were obtained via targeted,
  short-excerpt fetches (each under ~40 words) rather than bulk article
  reproduction, consistent with fair-use citation practice and MINER.md
  §2a's verbatim-fragment requirement. Where no exact quotable sentence
  existed for a claim (e.g., Claims 4, 5, 6, 7, 8, 11 — all derived from
  tabular/structured data rather than prose), the Quote field is marked
  accordingly per MINER.md §2a.5 rather than fabricated.
- Explicitly checked whether the post addresses reward hacking, contamination,
  or eval-environment hardening (network/git isolation) — confirmed via
  direct query against the source that it does not. This absence is treated
  as a genuine gap and flagged under Cross-References → Extends, not
  presented as a contradiction (per MINER.md §4a, silence on a topic is not
  an opposing claim).
- No contradiction issue filed: the source makes no claim that directly
  opposes an existing corpus source note. Its silence on contamination
  controls is a gap relative to `blog-cursor-reward-hacking-benchmarks.md`,
  not a conflicting factual claim, so it does not meet the bar in MINER.md
  §4a for filing a contradiction issue.
