---
source_url: https://cursor.com/blog/cursorbench
source_type: blog-post
title: "How we compare model quality in Cursor"
author: Naman Jain (Cursor / Anysphere)
date_published: 2026-03-11
date_extracted: 2026-04-19
last_checked: 2026-04-19
status: current
confidence_overall: emerging
issue: "#160"
---

# How we compare model quality in Cursor (Naman Jain, Cursor)

> Cursor's first-party account of CursorBench: a production-derived offline eval suite
> combined with live-traffic online evals that catches regressions public benchmarks miss,
> built around a novel "Cursor Blame" sourcing technique that generates ground-truth
> (query, solution) pairs directly from committed Cursor sessions.

## Source Context

- **Type**: blog-post (first-party research from Cursor / Anysphere)
- **Author credibility**: Naman Jain is writing from inside Cursor's engineering team.
  This is a vendor post describing their own internal tooling, published on Cursor's
  official blog. As a first-party account of production methodology, it is authoritative
  for the "how Cursor actually evaluates models" question. The claims about SWE-bench
  contamination and saturation are independently corroborated (OpenAI stopped reporting
  SWE-bench Verified for the same reason). No external peer-review. Treat as emerging.
- **Scope**: CursorBench-3 design, data sourcing via Cursor Blame, the online-offline
  hybrid eval loop, critique of public benchmarks, and the correctness-vs-token-efficiency
  tradeoff plot. Published March 11, 2026. Does NOT cover: model training, Cursor product
  features, agent architecture, or how other orgs should build evals (no explicit
  prescription for readers — this is descriptive of their own system).

## Extracted Claims

### Claim 1: Public agent benchmarks suffer three compounding failures: misalignment, grading problems, and training data contamination

- **Evidence**: Three distinct named failure modes. The contamination claim is independently
  corroborated: "OpenAI recently stopped reporting SWE-bench Verified results entirely
  after finding that frontier models could reproduce gold patches from memory, and that
  nearly 60% of unsolved problems had flawed tests."
- **Confidence**: emerging (the contamination sub-claim is effectively settled given
  OpenAI's public behavior; the others rest on Cursor's internal assessment)
- **Quote**: "Most SWE benchmarks focus on bug-fixing tasks; Terminal-Bench emphasizes
  puzzle-style problems (e.g., finding the best chess move from a board position). These
  misalign with actual developer agent usage patterns."
- **Our assessment**: This is the strongest case in our corpus for why public benchmarks
  cannot be trusted to differentiate models at the frontier. The three-part taxonomy
  (alignment, grading, contamination) is analytically clean and actionable. The
  contamination sub-claim is the most important: it means SWE-bench Verified scores are
  no longer interpretable for frontier models. Any guide section citing SWE-bench numbers
  should now carry a contamination caveat.

### Claim 2: Public benchmarks no longer differentiate models that developers experience as meaningfully different

- **Evidence**: CursorBench scatter plots show public benchmarks saturating at frontier
  levels — "models like Haiku can match or exceed GPT-5" on them. CursorBench continues
  to stratify these same models.
- **Confidence**: emerging (internal data, no published numbers, but the direction is
  credible given contamination evidence)
- **Quote**: "public benchmarks no longer tell apart models that have very different
  utility for developers" at frontier levels
- **Our assessment**: This is a strong and credible claim even without published numbers.
  If Haiku scores comparably to GPT-5 on SWE-bench, but developers clearly experience
  them as different quality, then the benchmark has lost discriminative validity. This
  should anchor the guide's treatment of model selection: "evaluate on tasks that look
  like your work, not on SWE-bench."

### Claim 3: "Cursor Blame" traces committed code back to the originating agent request, producing natural (query, ground-truth) pairs from real sessions

- **Evidence**: Described as a concrete internal tool that sources CursorBench tasks.
  The design is mechanically sound: if you know the commit and can trace the agent
  session that produced it, the developer's original request is the query and the
  committed code is the ground truth.
- **Confidence**: emerging (first-party description; mechanism is plausible and specific)
- **Quote**: "Cursor Blame, a tool that traces committed code back to the agent request
  that produced it"
- **Our assessment**: This is the most novel concrete technique in the post. It solves
  the benchmark-contamination problem structurally: the tasks come from internal codebases
  and real sessions, not from public GitHub repositories in training data. The
  "ground truth is what was committed" framing is elegant — it uses developer decisions
  as implicit quality signals without requiring manual annotation. This technique is
  replicable at any org that has AI coding tool usage logs correlated with their git
  history.

### Claim 4: CursorBench tasks use intentionally short, underspecified descriptions that mirror how developers actually communicate with agents

- **Evidence**: Contrasted explicitly with detailed GitHub issues used in SWE-bench.
  The intentional underspecification is a design choice, not a defect.
- **Confidence**: emerging
- **Quote**: "Task descriptions are intentionally short, mirroring how developers
  actually communicate with agents"
- **Our assessment**: This is a meaningful methodological point. A benchmark whose task
  descriptions look like detailed engineering tickets will reward agents that are good at
  parsing structured requirements — not agents that are good at inferring intent from
  terse real-world prompts. The Cursor design choice aligns with what practitioners
  report: real developer requests are short and ambiguous, not structured. Any
  harness-engineering guide section on evaluation should note this distribution mismatch.

### Claim 5: CursorBench-3 tasks roughly double the scope of SWE-bench tasks, measured by LOC and file count

- **Evidence**: Direct comparison to SWE-bench Verified, Pro, and Multilingual variants.
  CursorBench-3 "involves substantially more lines than SWE-bench Verified, Pro, or
  Multilingual" with the scope "roughly doubled from initial version."
- **Confidence**: emerging (internal data; specific numbers not published)
- **Quote**: "Problem scope roughly doubled from initial version, measured by lines of
  code and mean number of files"
- **Our assessment**: Scope growth matters because real engineering tasks span multiple
  files and subsystems; single-file bug-fix benchmarks don't test multi-file reasoning.
  The roughly-2x figure is directionally important even without exact numbers. The
  specific task categories (multi-workspace environments, monorepos, production log
  investigation) are the most guide-relevant detail: they are closer to what senior
  engineers actually do with AI coding tools than the bug-fix-in-one-file archetype.

### Claim 6: CursorBench evaluates agents across four dimensions: solution correctness, code quality, efficiency, and interaction behavior

- **Evidence**: Explicitly stated; the blog post focuses on correctness results but
  notes "in practice we evaluate agents across all of these axes."
- **Confidence**: emerging
- **Quote**: "in practice we evaluate agents across all of these axes"
- **Our assessment**: The four-axis framework is worth naming in the guide. Most public
  benchmarks and most practitioners default to correctness only. The inclusion of
  "interaction behavior" as a first-class eval axis is notable — it covers things like
  whether the agent asks clarifying questions appropriately, how it handles ambiguity,
  and whether it over-engineers solutions. No other source in the corpus names
  interaction behavior as a discrete eval dimension.

### Claim 7: Agentic graders are used for open-ended tasks that admit many valid solutions

- **Evidence**: Described as part of the grading methodology for tasks where narrow
  correctness criteria don't apply.
- **Confidence**: emerging (first-party description of internal tooling)
- **Quote**: N/A (described in the methodology section without a direct quotable sentence)
- **Our assessment**: The "agentic grader" approach — using an LLM to evaluate LLM
  output — is increasingly common but not well-documented in our corpus. The key design
  tension is auto-grader alignment: does the grader agree with developers about what
  "correct" means? The online eval loop (Claim 8) addresses this by cross-checking
  offline grader verdicts against live developer satisfaction signals.

### Claim 8: The online-offline hybrid loop catches regressions where offline grading looks correct but the output feels worse to developers

- **Evidence**: Direct description of failure mode caught by the online eval component.
  The online component tracks "high-level proxies of agent outcomes, including both
  interaction and output quality signals."
- **Confidence**: emerging
- **Quote**: "the agent's output looks correct to a grader but feels worse to a developer"
- **Our assessment**: This is the most important architectural claim in the post. It
  names the fundamental problem with offline evals: grader-developer alignment is not
  guaranteed. A model can satisfy the eval rubric while degrading user experience.
  The only way to catch this class of regression is with live-traffic signals. This is
  the production-grade lesson: offline evals are necessary but not sufficient; you need
  online signals as a sanity check. Highly relevant to Ch03 (verification patterns).

### Claim 9: Correctness is plotted against median completion tokens to capture the compute/latency tradeoff

- **Evidence**: Described as the axis choice for the scatter plot visualization.
  "The top right corner represents ideal agent quality, with highest performance at
  the lowest cost."
- **Confidence**: settled (this is a measurement choice, not an empirical finding)
- **Quote**: "The top right corner represents ideal agent quality, with highest
  performance at the lowest cost"
- **Our assessment**: The choice to make token efficiency a primary eval axis (not an
  afterthought) reflects production engineering values: a model that is marginally more
  correct but 3x more expensive is not the right production choice. This axis-choice
  framing is the clearest articulation we have in the corpus of why "best benchmark
  score" and "best model for production" are different optimization targets.

### Claim 10: Removing semantic search tool via ablation revealed it mattered most for repository-grounded Q&A on larger codebases

- **Evidence**: Concrete ablation experiment: "ran an ablation removing the semantic
  search tool entirely." Result: "scenarios where semantic search mattered most:
  repository-grounded question-answering on larger codebases."
- **Confidence**: emerging (first-party result; specific numbers not published)
- **Quote**: "ran an ablation removing the semantic search tool entirely" / "repository-
  grounded question-answering on larger codebases"
- **Our assessment**: This is a model for how to evaluate individual agent tool
  contributions: ablate the tool and measure the delta. The specific finding
  (semantic search matters most for large-codebase Q&A) is actionable for context
  engineering: if your use case is not large-codebase Q&A, investing in semantic
  search over other retrieval approaches is lower priority. The ablation methodology
  itself is the reusable lesson.

### Claim 11: Near-term, the majority of development work will shift to long-running agents working on their own computers

- **Evidence**: Forward-looking claim from Cursor's engineering perspective, framed as
  the motivation for evolving CursorBench beyond single-session tasks.
- **Confidence**: anecdotal (one vendor's forward-looking statement)
- **Quote**: "Over the next year, the vast majority of development work will shift to
  long-running agents working on their own computers"
- **Our assessment**: Treat as a directional signal, not a prediction. The specific
  implication for CursorBench evolution is more concrete: tasks that resolve in a
  single session are already being designed, but the next generation needs cheaper
  grading mechanisms and reproducibility solutions for external service interactions.
  This is the benchmark engineering version of the "long-running agents" thesis.

### Claim 12: CursorBench rankings more closely track actual developer experience than public benchmarks

- **Evidence**: Stated as a design goal and validated (without published correlation
  numbers) through Cursor's use of the online eval loop as ground truth.
- **Confidence**: anecdotal (vendor claim; the online signals are proprietary)
- **Quote**: "CursorBench distinguishes reliably between models that developers
  experience as meaningfully different"
- **Our assessment**: This is the core claim of the paper and the hardest to verify
  externally. Cursor has access to actual developer behavior data (through their product)
  that no external researcher can replicate. The claim is credible given the structural
  design (Cursor Blame sourcing, real-session tasks, online cross-validation) but cannot
  be independently confirmed. Treat as strong signal, not settled fact.

## Concrete Artifacts

### CursorBench Design Summary

```
# CursorBench-3 Architecture (Cursor / Anysphere, March 2026)

DATA SOURCING
  Tool: Cursor Blame
  Method: Trace committed code → originating agent request
  Output: (developer query, committed code) pairs from real Cursor sessions
  Advantage: No training-data contamination (internal codebase, real sessions)
  Refresh cadence: Every few months

TASK CHARACTERISTICS
  Description length: Intentionally short / underspecified
  Scope: Multi-file, monorepos, production log investigation (CursorBench-3)
  LOC vs. SWE-bench Verified: ~2x (roughly, by lines of code and file count)
  Session length: Single-session (current); long-running sessions (future roadmap)

EVALUATION DIMENSIONS
  1. Solution correctness (primary — this blog post)
  2. Code quality
  3. Efficiency
  4. Interaction behavior

GRADING
  Method: Agentic graders for open-ended tasks (multiple valid solutions)
  Limitation: Grader-developer alignment not guaranteed → requires online validation

SCATTER PLOT AXES
  X-axis: Median completion tokens (cost / latency proxy)
  Y-axis: Correctness score
  Ideal region: Top-right (high correctness, low tokens)

ONLINE-OFFLINE HYBRID LOOP
  Offline: CursorBench (as above)
  Online: Live-traffic signals tracking interaction + output quality proxies
  Purpose: Catch regressions where offline grade = pass but developer experience = worse
  Cross-check: If online signals degrade while offline scores hold, the grader is wrong
```

### Public Benchmark Failure Taxonomy

```
# Why public benchmarks fail at the frontier (Cursor's analysis, March 2026)

FAILURE 1 — MISALIGNMENT
  Problem: SWE-bench focuses on bug fixes; Terminal-Bench on puzzles
  Reality: Real dev work is feature development, refactoring, Q&A, exploration
  Impact: Benchmarks reward agents trained on different task distributions

FAILURE 2 — GRADING PROBLEMS
  Problem: Real developer requests admit many valid solutions
  Public benchmark response: Either penalize alternative correct solutions OR
    append synthetic constraints to reduce underspecification
  Impact: Both options introduce grader-vs-reality divergence

FAILURE 3 — TRAINING DATA CONTAMINATION
  Problem: SWE-bench tasks drawn from public GitHub repos → in training data
  Evidence: OpenAI stopped reporting SWE-bench Verified results after finding
    that frontier models could reproduce gold patches from memory
  Evidence: ~60% of unsolved SWE-bench problems have flawed tests
  Impact: Scores reflect memorization, not generalization
```

### Ablation Design Example

```
# Tool ablation methodology (Cursor example)
# Testing: does semantic search improve agent quality?

Procedure:
  1. Run full agent suite on CursorBench tasks WITH semantic search tool
  2. Run same suite WITHOUT semantic search tool (ablation)
  3. Measure delta in correctness scores across task categories

Finding:
  Semantic search mattered most for: repository-grounded Q&A on larger codebases
  Implication: Semantic search investment is high-priority for large-codebase Q&A tasks;
               lower priority for single-file edits or small codebase work
```

## Cross-References

- **Corroborates**: `paper-miller-speed-cost-quality.md` — Miller et al. find that
  Cursor adoption produces measurable quality degradation (41.6% complexity increase)
  when measured externally. The CursorBench post is Cursor's internal view of the same
  quality measurement question. These are complementary: Miller measures from the outside
  (committed code quality over time), Cursor measures from the inside (task correctness
  at model selection time). Neither contradicts the other — internal eval quality and
  external adoption quality outcomes are different dimensions.

- **Corroborates**: `docs-github-copilot-pr-review-metrics.md` — GitHub's cycle-time
  metrics and Cursor's online eval loop share the same structural insight: offline
  metrics (benchmark scores / merge counts) must be validated against live-traffic
  outcome signals. Both sources identify "benchmark passes but reality is worse" as the
  key failure mode to instrument against.

- **Extends**: `blog-french-owen-coding-agents-feb-2026.md` — French-Owen observes that
  Opus vs. Codex quality differences are real and experiential but gives no framework
  for measurement. CursorBench provides the measurement framework: correctness-vs-token
  scatter plots sourced from real sessions. The Cursor Blame technique is the
  production-grade version of the informal practitioner comparisons French-Owen describes.

- **Extends**: `survey-pragmaticengineer-ai-tooling-2026.md` — The Pragmatic Engineer
  survey documents that teams struggle to measure AI tool ROI. CursorBench describes
  a concrete evaluation methodology that teams could adapt for their own model selection
  decisions. The Cursor Blame sourcing approach is replicable at any org with AI coding
  session logs correlated to git history.

- **Novel**: No existing source note covers agent eval methodology or benchmark design.
  This source introduces to the corpus:
  - The online-offline hybrid eval loop as an evaluation architecture pattern
  - The Cursor Blame sourcing technique (session-to-commit correlation for ground truth)
  - The three-part public benchmark failure taxonomy (misalignment, grading, contamination)
  - "Interaction behavior" as a named, first-class eval dimension alongside correctness
  - The correctness-vs-token scatter plot as a model selection visualization
  - Agentic graders for underspecified tasks

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add a section on evaluation methodology for
  agent quality. The Cursor Blame technique is the canonical example of production-
  grounded eval sourcing: use your own git history + session logs, not public benchmarks.
  The ablation design (remove one tool, measure delta per task category) is the
  recommended approach for evaluating individual tool contributions.

- **Chapter 03 (Safety and Verification)**: The online-offline hybrid loop is a
  verification architecture. The core claim — "offline evals are necessary but not
  sufficient; grader-developer alignment is not guaranteed" — should anchor the
  verification section. Any automated quality gate (CI checks, LLM-graded evals)
  needs a live-signal cross-check to detect grader drift. This is the production-grade
  lesson for teams building eval pipelines.

- **Chapter 03 (Benchmark Selection)**: The three-part benchmark failure taxonomy
  (misalignment, grading, contamination) should be the standard checklist before citing
  any public benchmark score. The contamination sub-claim is now effectively settled
  (OpenAI's behavior is public); include it as a caveat in any section that references
  SWE-bench numbers. Recommendation: "do not cite SWE-bench Verified scores for frontier
  models without a contamination caveat."

- **Chapter 04 (Context Engineering)**: The token-efficiency axis (correctness vs.
  median completion tokens) is the evaluation-side complement to the context budget
  heuristics from French-Owen and Sankalp. The scatter plot framing — "top right is
  ideal, high correctness at low token cost" — is the production-engineering version of
  context budget optimization. Add as a model selection criterion alongside raw
  correctness scores.

- **Chapter 05 (Team Adoption / Measuring Impact)**: The CursorBench methodology is
  the strongest available example of how a production team builds their own eval suite
  when public benchmarks fail. Teams evaluating which AI coding model to use should
  build task suites from their own commit history rather than relying on SWE-bench
  leaderboards. The four eval dimensions (correctness, code quality, efficiency,
  interaction behavior) are a starting framework for org-specific eval rubrics.

## Extraction Notes

- Blog post is 7 minutes / ~1,800 words. Full content read; no paywalled sections.
  No linked sub-pages were substantive enough to follow (two recruitment links, one
  chart image without alt text).
- The scatter plot figure referenced in the post (correctness vs. median completion
  tokens) was not rendered in the fetched content — only described in text. The
  description is sufficient to extract the axis design and the "top right is ideal"
  framing; the specific model placements on the plot are not available from the fetch.
- No published numbers beyond the ~2x LOC comparison to SWE-bench. All Cursor-specific
  performance data stays internal. This is expected for a first-party eval paper —
  publishing exact scores would expose competitive model selection strategy.
- The contamination finding (OpenAI stopped reporting SWE-bench Verified results) is
  stated as fact with a specific quantitative claim (~60% of unsolved problems have
  flawed tests). This is corroborated by OpenAI's public behavior but the 60% figure
  is Cursor's representation of OpenAI's internal finding, not a citation to a published
  OpenAI document. Treat the 60% figure as directional, not exact.
- No contradictions to file: no existing source note makes claims about agent eval
  methodology that this source opposes.
