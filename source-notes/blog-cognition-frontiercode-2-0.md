---
source_url: https://cognition.com/blog/frontier-code-2.0
source_type: blog-post
title: "FrontierCode 2.0"
author: The Cognition Team
date_published: 2026-10-27
date_extracted: 2026-10-28
last_checked: 2026-10-28
status: current
confidence_overall: emerging
issue: "#4391"
---

# FrontierCode 2.0

> Cognition's third-generation "mergeability" benchmark roughly triples its "thoroughness" blocking criteria, loosens scope criteria, drops top scores to ~45%, and publishes per-category blocker failure rates by reasoning effort, showing that higher effort mostly reduces failures except on scope.

## Source Context

- **Type**: blog-post (vendor first-party benchmark release, cognition.com, dated 2026.10.27, byline "The Cognition Team"; links to the live FrontierCode leaderboard).
- **Author credibility**: Cognition (makers of Devin / SWE-series models) builds and runs the benchmark itself and also sells agents that are evaluated on it. Methodology is built with 20+ open-source maintainers, but no task text, grader code, or independent audit is published on this page. All numbers are vendor-reported.
- **Scope**: Covers what changed vs FrontierCode 1.0/1.1 (coverage, blocking criteria, task size), 1.1 vs 2.0 score table, a blocker-category breakdown, thoroughness criteria, reasoning-effort effects (including the scope-blocker discussion), and two task walk-throughs (Mock Service Worker, PostHog Android SDK). Does not give per-model cost numbers in text (the cost chart is interactive), nor the full set of 2.0 scores beyond the eight models in the 1.1-vs-2.0 table. Grading internals are deferred to the FrontierCode 1.0 post.

## Extracted Claims

### Claim 1: FrontierCode 2.0 is positioned as measuring the gap in inferring intent, unstated constraints and long-term consequences, which saturating benchmarks miss
- **Evidence**: Vendor framing based on "experience building and deploying Devin"; contrasted with Terminal-Bench 4.0's `vf2-speedup-networkx` task, whose prompt fully specifies approach and style.
- **Confidence**: emerging
- **Quote**: "Models struggle to infer user intent, respect unstated constraints, and anticipate long-term consequences of their changes, forcing human intervention."
- **Our assessment**: Plausible and consistent with practitioner experience, but it is a motivation statement from a vendor selling agents; the supporting data is their own benchmark.

### Claim 2: 2.0 differs from 1.1 on three axes: broader coverage (incl. security and performance tasks), higher mergeability standards, and larger task scope
- **Evidence**: Stated numbers: tasks from 55% more repositories, 43% more blocking criteria, reference solutions touch 67% more files and 89% more lines, in codebases 25% larger.
- **Confidence**: emerging
- **Quote**: "compared to FrontierCode 1.1, reference solutions modify 67% more files and 89% more lines of code on average, in codebases that are 25% larger."
- **Our assessment**: Specific, checkable-in-principle numbers, but not independently verifiable. Note that harder tasks plus stricter criteria confound any comparison of 1.1 and 2.0 scores as "model regression".

### Claim 3: Headline scores drop sharply from 1.1 to 2.0 and the best model (Opus 5.5) is at only 45.5%; open-weight models trail the most
- **Evidence**: Table at each model's best reasoning effort: Claude Opus 5.5 54.6%→45.5%; GPT-6 Astra 53.3%→42.8%; Grok 4.7 47.6%→28.6%; Gemini 4 Argon 47.5%→26.3%; Muse Wonder 1.0 47.0%→24.3%; SWE-2 50.0%→23.9%; DeepSeek V4.1 Flash 43.9%→19.3%; Kimi K3 44.2%→17.7%.
- **Confidence**: emerging
- **Quote**: "The benchmark is far from saturated: the top-performing model, Opus 5.5, scores only 45%."
- **Our assessment**: The spread widened (1.1 range ~44-55%, 2.0 range ~18-46%), supporting the claim that 2.0 discriminates better. Vendor-reported; "Score" zeroes any solution failing a blocking criterion, so scores are sensitive to rubric strictness. Cognition's own SWE-2 lands near the bottom of the shown list, which is mildly reassuring about self-serving bias.

### Claim 4: Cost-performance: Opus 5.5 anchors the high end of the Pareto frontier, with Luna, Haiku and Sol at the low-cost end, and GPT-6.1 Sol is particularly cost-efficient
- **Evidence**: Interactive score-vs-cost chart; cost is "mean USD spend per rollout at list API pricing, including public discounts". Underlying values are not in the page text.
- **Confidence**: anecdotal
- **Quote**: "The Pareto frontier includes Opus 5.5 on the high end along with Luna, Haiku, and Sol on the low-cost end, with GPT-6.1 Sol offering particularly strong performance relative to its cost."
- **Our assessment**: Useful directional model-selection signal but we cannot extract numbers; list-price cost ignores caching/discount differences in real use.

### Claim 5: "Thoroughness" criteria (implicit requirements inferable from the prompt and codebase) grew 3x to become the largest blocker category, and have the highest failure rate
- **Evidence**: Blocker counts 1.1→2.0: Thoroughness 168→501, Core behavior 399→353, Avoiding regressions 174→259, Effective test writing 202→213, Lint/format/typecheck 112→183, Scope 56→123. Failure rate (mean of Opus 5.5, Fable 5.1, GPT 6.1 Sol, GPT 6 Astra at high effort): Thoroughness 11.7%→19.2%, Core behavior 9.5%→14.9%.
- **Confidence**: emerging
- **Quote**: "Thoroughness criteria enforce correctness conditions that an agent can be expected to infer from the instructions and the existing codebase, even when they aren’t stated explicitly."
- **Our assessment**: The most guide-relevant finding: even frontier models fail ~1 in 5 implicit-requirement checks. Caveat: the thoroughness criteria are authored by Cognition's maintainers and the increase in count partly explains the higher failure rate (more, stricter checks), so "models got less thorough" should not be inferred.

### Claim 6: Two canonical thoroughness failures are fixing only one instance of a bug and not matching existing support for sibling input types
- **Evidence**: Two worked examples listed in the post (sibling code path with same bug; similar code handling other input types).
- **Confidence**: emerging
- **Quote**: "The prompt identifies a bug in one code path, but the same bug exists in a sibling path. A thorough agent finds and fixes both."
- **Our assessment**: These map directly onto instructions practitioners can put in AGENTS.md / prompts ("search for sibling occurrences", "check what similar code supports"). The post does not test whether such instructions close the gap.

### Claim 7: Mock Service Worker task: Opus 5.5 at max effort fixes the reported bug but fails an implicit-correctness expectation (closing the discarded generator so `finally` cleanup runs); 0/5 runs passed at every effort level
- **Evidence**: Task `msw-fix-reset-generator-state` (resetHandlers() doesn't restart generator resolvers); per-effort pass counts 0/5 at low, medium, high, xhigh, max; code excerpt of a generator with a `finally { cleanup() }` block.
- **Confidence**: anecdotal
- **Quote**: "Skipping the user’s cleanup code can cause resource leaks or leave the application in an inconsistent state."
- **Our assessment**: A good, concrete illustration of "fixes as reported, violates unstated invariant". Single task, single model; the claim that experienced JS developers expect the generator be closed is the vendor's judgment.

### Claim 8: PostHog Android task: GPT-6 Astra passes at low effort (5/5) but at higher effort often rewrites/deletes a public-API class and fails a deterministic scope blocker (2/5 medium, 1/5 high, 2/5 xhigh, 1/5 max)
- **Evidence**: Diff-size table: low-effort "Trim" changes PostHogQueue.kt (+21/−9) and PostHogSendCachedEventsIntegration.kt (+1/−109), tests +121/−89; high-effort "Rewrite" deletes the integration (+0/−252), adds PostHogLegacyQueue.kt (+77), touches `posthog.api` and 7 test files (+369/−343).
- **Confidence**: anecdotal
- **Quote**: "Scope blockers, which deterministically check that the model hasn’t modified certain files, catch this change, and the agent fails the task."
- **Our assessment**: Strong illustration that more reasoning effort can produce larger, riskier diffs (public API breakage). Note the fix itself was functionally valid ("passes most of the hidden behavior tests"), so the failure is a scope/compat judgment encoded by the task author, not a bug.

### Claim 9: Score can legitimately fall with higher reasoning effort on this benchmark; on 1.1 this produced "zig-zaggy" curves attributed mainly to scope blockers, with smaller contributions from cheating and overthinking
- **Evidence**: 1.1 criterion pass rates, low→max effort: implementation criteria rise (Opus 5: 79.3%→83.0%; Opus 4.8: 75.5%→79.2%; Fable 5: 79.2%→81.8%; GPT-5.6 Sol: 68.6%→73.0%) while scope criteria fall (Opus 5: 69.2%→51.1%; Opus 4.8: 81.9%→70.9%; Fable 5: 79.1%→63.4%; GPT-5.6 Sol: 79.7%→68.3%).
- **Confidence**: emerging
- **Quote**: "In other words, models tend to write more code and touch more files with increased effort, even when the changes may not be preferable."
- **Our assessment**: Cross-model, consistent direction in four models is stronger evidence than a single anecdote. The "cheating at higher effort" aside (models "accidentally" pulling the solution commit) is an interesting secondary claim given only as a one-line assertion with no data.

### Claim 10: Cognition loosened scope criteria in 2.0 (scope failure 9.0%→3.8%), after finding some scope-violating solutions were "surprisingly reasonable"; it now asserts the effort curves reflect real regressions
- **Evidence**: Average scope blocker failure rate across effort levels 9.0% (1.1) vs 3.8% (2.0); "improved auditing" cited but not described.
- **Confidence**: emerging
- **Quote**: "In FrontierCode 2.0, we loosened our scope criteria to accommodate surprising but acceptable behavior."
- **Our assessment**: An admission that scope enforcement in 1.0 produced false failures, which is relevant to how far to trust "scope" as a quality signal. The self-reported confidence ("we are confident that our effort-performance curves measure real regressions") is unverified; the loosening also conveniently removes the earlier controversy.

### Claim 11: In 2.0, blocker failure rates mostly fall as effort rises (low→max), except scope which rises slightly (3.8%→4.9%)
- **Evidence**: Pooled over Opus 5.5, Fable 5.1, GPT-6.1 Sol, GPT-6 Astra. Low→max: Thoroughness 26.0%→15.3%; Core behavior 20.9%→12.3%; Backwards compatibility 9.7%→5.2%; Avoiding regressions 4.4%→2.2%; Test integrity 3.0%→1.9%; Effective test writing 3.9%→1.3%; Compilation 2.3%→0.7%; Lint/format/typecheck 1.3%→0.5%; Scope 3.8%→4.9%.
- **Confidence**: emerging
- **Quote**: "Thoroughness has the highest failure rate at every effort level, above core behavior."
- **Our assessment**: Supports "spend effort on verification/thoroughness" advice, while confirming a scope/over-reach cost. Pooled across four models, so model-specific behavior is hidden; and the figure says nothing about cost/latency trade-offs.

### Claim 12: Quality control found the reference solution differs from the upstream PR in 80% of tasks (60% in 1.0), and an audit agent found a security vulnerability in an upstream implementation that was reported to maintainers
- **Evidence**: Stated percentages; human + automated review of prompts, reference solutions and grading criteria. No details of the vulnerability or repository.
- **Confidence**: anecdotal
- **Quote**: "In 80% of FrontierCode 2.0 tasks, the reference solution differs from the upstream PR, up from 60% in FrontierCode 1.0."
- **Our assessment**: Two readings: rigorous QC, or evidence that "upstream merged" is a weak ground-truth standard (consistent with the benchmark's mergeability thesis). The vulnerability claim is unsubstantiated here (no CVE/repo named).

### Claim 13: Methodology retained from 1.0: 20+ open-source developers each spending 40+ hours per task
- **Evidence**: Stated; pod leads/contributors named in Acknowledgments (e.g., Claudio Costa, Martin McKeaveney, Tomer Nosrati, Merlijn Vos marked as pod leads).
- **Confidence**: emerging
- **Quote**: "More than 20 world-class open-source developers each spent over 40 hours per task building realistic coding evals from the repositories they maintain."
- **Our assessment**: Note the count differs from the 1.0 post as captured in the existing note (36 maintainers); likely different cohorts or counting (e.g., "20+" for 2.0 authors). Treat as not a contradiction but a discrepancy worth watching.

## Concrete Artifacts

```
Blocking criteria counts by category (FrontierCode 1.1 -> 2.0), Cognition:
Thoroughness 168 -> 501 | Core behavior 399 -> 353 | Avoiding regressions 174 -> 259
Effective test writing 202 -> 213 | Lint/format/typecheck 112 -> 183 | Scope 56 -> 123
Backwards compatibility 85 -> 76 | Compilation 86 -> 69 | Test integrity 48 -> 48
Docs/metadata 6 -> 17 | Implementation detail 9 -> 11
```

```
Blocker failure rate by category (1.1 -> 2.0), mean of Opus 5.5, Fable 5.1,
GPT 6.1 Sol, GPT 6 Astra at high effort (Cognition):
Thoroughness 11.7% -> 19.2% | Core behavior 9.5% -> 14.9% | Backwards compat 2.9% -> 5.9%
Scope 9.0% -> 3.8% | Avoiding regressions 1.3% -> 3.3% | Test integrity 3.4% -> 2.5%
Effective test writing 2.8% -> 1.6% | Compilation 0.7% -> 1.2% | Lint/format/typecheck 1.7% -> 1.0%
```

```
Blocker failure rate by effort, FrontierCode 2.0, low -> max (Cognition):
Thoroughness 26.0 -> 15.3 | Core 20.9 -> 12.3 | Backcompat 9.7 -> 5.2 | Scope 3.8 -> 4.9
Regressions 4.4 -> 2.2 | Test integrity 3.0 -> 1.9 | Test writing 3.9 -> 1.3
Compilation 2.3 -> 0.7 | Lint/format/typecheck 1.3 -> 0.5
```

```
Sample task: msw-fix-reset-generator-state (Mock Service Worker), from the post:
function* () {
  try {
    yield 'first'
    return 'rest'
  } finally {
    cleanup() // never runs after a reset
  }
}
Opus 5.5: 0/5 passes at low, medium, high, xhigh, max.
```

```
Sample task: PostHog Android SDK startup race (Cognition):
GPT-6 Astra pass counts by effort: low 5/5, medium 2/5, high 1/5, xhigh 2/5, max 1/5
Low-effort "Trim" (passes): PostHogQueue.kt +21/-9; PostHogSendCachedEventsIntegration.kt +1/-109; PostHog.kt +2/-2
High-effort "Rewrite" (fails scope blocker): PostHogQueue.kt +56/-24; SendCachedEventsIntegration.kt deleted (+0/-252);
  PostHog.kt +0/-17; PostHogLegacyQueue.kt +77/-0 (outside allowed paths); posthog.api +1/-1 (outside allowed paths)
```

## Cross-References

- **Corroborates**:
  - `blog-claude-dev-thariq-spending-your-effort.md` Claim 4 (with an underspecified prompt, higher effort means more choices made on the user's behalf) and Claim 9 (increasing effort reduces failures from missed edge cases): this note's Claims 9 and 11 give independent third-party-style (Cognition) quantitative support for both halves: higher effort lowers thoroughness/core-behavior failures but increases over-reach (scope).
  - `blog-cognition-frontiercode.md` Claim 3 (scope enforcement as a grading technique): this note's Claim 8 shows the scope blocker in action on a real task.
  - `blog-cognition-frontiercode.md` Claim 1 (mergeability framing) and Claim 12 (METR finding that many benchmark-passing PRs would not be merged): this note's Claims 5-8 offer more granular failure categories that pass tests but fail a maintainer-style bar.
- **Contradicts**: None filed. Candidate evaluated: this note's Claim 13 ("More than 20 world-class open-source developers") vs `blog-cognition-frontiercode.md` Claim 4 (36 maintainers of flagship repos). Judged a counting/cohort discrepancy, not a substantive opposing position on guide advice, so no issue was filed under MINER.md §4a.
- **Extends**: `blog-cognition-frontiercode.md` (FrontierCode 1.0/1.1 methodology and the 1.1 Main leaderboard, Claim 10): adds 2.0 methodology changes, a per-category blocker analysis, and the revised scope criteria. Its 1.1 Main leaderboard (Fable 5 at 53.5%) used different model versions than this post's 1.1 column (Opus 5.5 at 54.6%), so the numbers are not directly comparable across the two notes.
- **Novel**: Per-category blocker failure rates broken out by reasoning effort; the explicit "thoroughness" criterion cluster; Cognition's admission that 1.0 scope blockers over-penalized "surprising but acceptable" changes; the public-API-deletion-at-high-effort example; the claim of 80% reference-solution divergence from upstream PRs.

## Guide Impact

- **Chapter 03 (verification)**: Add the thoroughness finding as evidence that agents miss implicit requirements (sibling code paths, existing-support parity), with the 19.2% pooled blocker failure rate as vendor-reported evidence; recommend reviewer checklists/prompts that explicitly ask for "all instances" and "match existing support". Also add the scope-blocker revision (9.0%→3.8%) as a caution on over-strict scope rules and a caution that benchmark rubrics encode author judgments.
- **Chapter 04 (reasoning effort / cost)**: Complement `blog-claude-dev-thariq-spending-your-effort.md` with the finding that higher effort reduces most blocker failures but not scope failures (3.8%→4.9%), and the PostHog example of a larger, API-breaking rewrite at higher effort. Suggest guidance: for tasks with strict compatibility constraints, state them explicitly or restrict editable paths rather than relying on higher effort.
- **Chapter 02 (harness/eval design)**: Cite as an example of deterministic scope enforcement (allowed-path checks) as a harness guardrail, with the caveat that over-strict scope checks produced false failures in 1.0.
- **Benchmark trust section**: Note that top scores fell ~9 points and low-tier scores ~20-30 points from 1.1 to 2.0 owing to stricter rubrics, so cross-version leaderboards should not be compared.

## Extraction Notes

- Fetched the page's raw HTML with curl and stripped tags; read all text including the table/alt-text data and acknowledgments. The page's interactive charts and diff viewers are client-rendered, so cost values (the score-vs-cost chart) and the per-run agent traces are not available in text. Leaderboard values come from the page's own static data tables.
- Followed no sub-pages: the grading methodology is in the FrontierCode 1.0 post already covered by `blog-cognition-frontiercode.md`.
- The post uses model names (Opus 5.5, Fable 5.1, GPT-6.1 Sol, GPT-6 Astra, Grok 4.7, etc.) exactly as published; the 1.1 effort figures use older model names (Claude Opus 5, Opus 4.8, Fable 5, GPT-5.6 Sol) and come from FrontierCode 1.1, not 2.0.
- Everything is vendor-reported; no independent replication.
