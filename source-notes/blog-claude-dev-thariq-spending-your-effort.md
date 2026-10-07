---
source_url: https://claude.dev/blog/spending-your-effort/
source_type: blog-post
title: "Using Claude Code: Spending your effort"
author: Thariq Shihipar
date_published: 2026-09-25
date_extracted: 2026-10-07
last_checked: 2026-10-07
status: current
confidence_overall: emerging
issue: "#3950"
---

# Using Claude Code: Spending your effort

> First-party guidance on what the `effort` setting actually changes (verification, edge-case testing, and how much independent judgement the model uses), backed by Terminal-Bench 3.0 failure-mode data and a "low-effort build, high-effort verify" workflow.

## Source Context

- **Type**: blog-post (Engineering category, claude.dev blog; ~8 min read)
- **Author credibility**: Thariq Shihipar works on Claude Code at Anthropic. This is a first-party account, so it describes Anthropic's own models and internal runs. The post is not independent. The numbers are internal and the author discloses caveats in a footnote.
- **Scope**: Covers Opus 5.5 and Fable 5.1 effort levels (low/medium/high/xhigh/max) in Claude Code. It includes three toy build experiments, Terminal-Bench 3.0 curves and per-category gains, three traced tasks, and a rule of thumb per level. It does not give dollar costs (a separate post, "What a task costs on Opus 5.5", is linked) and does not cover non-Claude models.
- **Note on triage**: The triage comments on the issue disagree about authorship (one names Steve Ash). The page itself lists Thariq Shihipar.

## Extracted Claims

### Claim 1: Effort modulates how much verification and edge-case testing Claude does and how much of its own judgement it uses
- **Evidence**: The author's own tests across normal work plus a Terminal-Bench 3.0 deep dive.
- **Confidence**: emerging
- **Quote**: "effort was a great way of modulating how much verification and edgecase testing Claude did and how much of its own judgement it used."
- **Our assessment**: A useful mental model. Effort is more than "thinking longer": it changes behaviour (adversarial review, fuzzing, autonomous decisions). It is supported by the traced runs but comes from one first-party author.

### Claim 2: Effort is a signal of how much compute you want spent, analogous to a deadline given to a human
- **Evidence**: Analogy of a task due in 1 hour versus 12 hours, no data.
- **Confidence**: anecdotal
- **Quote**: "higher effort will involve Claude taking more independent action for judgement and verification."
- **Our assessment**: Good framing for teaching. It is an analogy, not a mechanism claim.

### Claim 3: Each effort level on Fable 5.1 and Opus 5.5 gives an uptick in benchmark score and tokens consumed, and the curves are better than previous models
- **Evidence**: Fig A, Terminal-Bench 3.0 pass rate against median tokens per attempt, 70 tasks (4 GPU tasks excluded), annotated "same score, half the tokens". Opus 5.5 was run about three weeks after the others, with responses capped at 128k tokens and no GitHub/PyPI access.
- **Confidence**: emerging
- **Quote**: "at each level, there is an uptick in benchmark scores and tokens consumed."
- **Our assessment**: Plausible, but the chart values are not in the text and the runs are not identical across models, so cross-model comparison is weak.

### Claim 4: With an underspecified prompt, higher effort yields a more fleshed-out app but also more choices made on the user's behalf, at steeply rising time cost
- **Evidence**: Fitness tracker build on Opus 5.5: low 1.5 min (log plus simple graph), medium 4 min, high 11 min, max 67 min (adds a heat chart).
- **Confidence**: anecdotal
- **Quote**: "effort changes dramatically how fleshed out the app is, but also results in Claude making more choices along the way."
- **Our assessment**: Single run per level, so anecdotal. The timing ratio (about 45x from low to max) is still a useful cost signal.

### Claim 5: For exploratory design work, low effort is preferable for understanding Claude's direction fast, while max gives polish
- **Evidence**: Redesign of the Claude Code `/config` menu. Low took 1 min and gave a rough interactive sketch. Max took 28 min and gave a Claude Code-like mockup with walkthroughs.
- **Confidence**: anecdotal
- **Quote**: "For this particular task, I think I prefer using low effort to understand Claude's vision."
- **Our assessment**: Supports using fast iteration when the human is in the loop and expects to give feedback.

### Claim 6: A detailed spec makes outputs converge across effort levels
- **Evidence**: Fitness app after an in-depth interview spec. Low 16 min, medium 22 min, high 33 min, max 79 min. Designs and implementations were similar.
- **Confidence**: anecdotal
- **Quote**: "given this spec, the models behaved much more similarly."
- **Our assessment**: Notable: specification quality substitutes for effort, and max effort mostly just simplified some details. It is consistent with the spec-first emphasis elsewhere in the corpus, but it comes from one toy example.

### Claim 7: A recommended feature loop is interview, implement at low effort, review, then verify at high effort
- **Evidence**: The author's personal practice, not measured.
- **Confidence**: anecdotal
- **Quote**: "Verify and test on high effort"
- **Our assessment**: Actionable and cheap to adopt. It puts expensive effort where Claim 8 says it pays off (verification) rather than in the generative step. It is untested against a single-level baseline.

### Claim 8: Higher effort is best for tasks with many hidden edge cases
- **Evidence**: `html-js-filter` (HTML sanitizer): Fable 5.1 went from 1/5 at low to 5/5 at xhigh. A low attempt took about 2 min, wrote a filter in one pass and tested one hand-written page. A traced high run took about 33 min: adversarial review of its draft, reading the parser source, a standard XSS suite, and a random-document fuzzer.
- **Confidence**: emerging
- **Quote**: "higher effort is best for tasks with lots of hidden edge cases."
- **Our assessment**: Convincing for this class of task, with 5 attempts per task and one traced run. The mechanism (more self-verification) is directly observable in the trace.

### Claim 9: Increasing effort reduces failures from missed edge cases but does not fix a wrong approach
- **Evidence**: Fig B, 370 attempts on Fable 5.1, failures classified by a model judge (approximate). Passed 140 to 214 (low to max), median tokens 73k to 222k. "Missed a case" 59 to 24, "a bug its tests missed" 40 to 14, "wrong or incomplete fix" 31 to 10, "misread a requirement" 45 to 26. "Picked the wrong reading" rose 25 to 47.
- **Confidence**: emerging
- **Quote**: "increasing effort tends to reduce failures due to missing edgecases (purple blocks), but does not fix when the model has the wrong approach (blue blocks)."
- **Our assessment**: Most valuable quantitative piece. The rise in "picked the wrong reading" (25 to 47) suggests that without a human, more effort can mean more confident commitment to a wrong interpretation. Failure categories come from an LLM judge, so treat them as approximate (the post says so).

### Claim 10: Effort gains vary strongly by domain; rulebook-style work gains little
- **Evidence**: Fig C, Fable 5.1 pass rate, low to top effort: Security 64% to 87% (7 tasks), Hardware 34% to 75% (5), ML 54% to 73% (13), Science 41% to 61% (15), Software 43% to 56% (20), Media 18% to 30% (4), Operations 12% to 22% (10). Categories are small, so low pools the two lowest settings and top pools the three highest.
- **Confidence**: emerging
- **Quote**: "Security 64% → 87%, Hardware 34% → 75%, ML 54% → 73%, Science 41% → 61%, Software 43% → 56%, Media 18% → 30%, Operations 12% → 22%"
- **Our assessment**: Tiny per-category task counts (4 to 20) make per-category numbers noisy. Software, the category most readers care about, gains the least among the technical ones except media and operations.

### Claim 11: Without a human in the loop, high effort compensates for not asking clarifying questions
- **Evidence**: `gsea-proteomics`: Opus 5.5 0/5 at low, 4/5 at high. Low picked one data-prep method. High tried two, noticed the significant treatments changed, and investigated.
- **Confidence**: anecdotal
- **Quote**: "If a user were in the loop, Claude may have asked the user about the way to set up the problem, but without a user in the loop, high effort does better."
- **Our assessment**: Links effort to autonomy: effort is a substitute for human clarification in unattended runs. Single traced example.

### Claim 12: Low-effort failures share a pattern of editing or shipping before reproducing, and of unverified warnings
- **Evidence**: `mvcc-lsm-compaction` (Opus 5.5 0/5 low to 4/5 xhigh; about 1 min versus about 11 min per attempt). Low edited code before building or reproducing and did not check that its test would catch the bug. Xhigh reproduced first, wrote a randomized test against a never-compacting reference, and checked the tests failed on half-finished fixes. `cli-2ph-simplex` (0/5 low to 5/5 high). Low stopped around 10k tokens and warned it might be slow without checking. High tested against a brute-force solver and timed larger inputs.
- **Confidence**: emerging
- **Quote**: "and did not check that its new test would have caught the original bug."
- **Our assessment**: Not an exact quote of a single sentence. See extraction notes. The pattern (test the test, differential testing against a reference) is a reusable verification recipe that can be prompted for explicitly at any effort level.

### Claim 13: Rule of thumb for effort levels
- **Evidence**: Author's own usage.
- **Confidence**: anecdotal
- **Quote**: "Max: When I want Claude to operate fully autonomously to solve difficult problems"
- **Our assessment**: Low = in-the-loop brainstorming and sketches. Medium = most regular software work. High = verification-critical or edge-case work such as brownfield bug fixes. Max = fully autonomous hard problems. Reasonable defaults, to be validated by readers. The post invites feedback on whether this matches users' intuition.

### Claim 14: Effort can be changed mid-conversation without breaking the prompt cache in Claude Code
- **Evidence**: Assertion by the author, no data.
- **Confidence**: anecdotal
- **Quote**: "how they respond to effort without breaking the prompt cache in Claude Code"
- **Our assessment**: Practically important, since it means effort can be raised for the verification phase of the same session. It is stated as a product property of the newest models and is not demonstrated.

## Concrete Artifacts

```
Feature-development loop (Thariq Shihipar, claude.dev, "Spending your effort"):
1. Give Claude a spec and ask it to interview me about any details I'm missing
2. Implement it on low effort
3. Review to make sure it got the gist of it correct, iterate on low effort as needed
4. Verify and test on high effort
```

```
Effort timings, Opus 5.5 (same source)
Fitness app, underspecified:  low 1.5 min | medium 4 min | high 11 min | max 67 min
Fitness app, highly specified: low 16 min | medium 22 min | high 33 min | max 79 min
/config redesign:              low 1 min  | max 28 min
```

```
Fable 5.1, Terminal-Bench 3.0, 370 attempts (Fig B)
                      low (73k median tokens)  max (222k)
passed                140                      214
missed a case          59                       24
a bug its tests missed 40                       14
misread a requirement  45                       26
wrong/incomplete fix   31                       10
picked the wrong reading 25                     47
```

```
Effort-sensitive tasks (5 attempts each)
html-js-filter      Fable 5.1  1/5 low -> 5/5 xhigh
mvcc-lsm-compaction Opus 5.5   0/5 low -> 4/5 xhigh
cli-2ph-simplex     Opus 5.5   0/5 low -> 5/5 high
gsea-proteomics     Opus 5.5   0/5 low -> 4/5 high
```

Footnote 1 caveats (verbatim): "these come from our own internal runs, 5 attempts per task, with our production safety interventions off for Fable 5.1"; "The security tasks also ran without internet access".

## Cross-References

- **Corroborates**: `blog-cursor-bugbot-effort-billing` (Claims 4 and 6): a different vendor also finds that a higher effort setting surfaces more bugs (35% more) in review. `docs-github-copilot-code-review-effort-levels-ga` (Claims 1 and 8): Copilot offers Lite versus Balanced review depth to match complexity and risk, which parallels the "high effort for verification" advice.
- **Contradicts**: None filed. `blog-anthropic-claudecode-quality-postmortem` (Claim 1) reports that medium effort gave only "slightly lower intelligence" yet users perceived significant degradation. This is in tension with the rule of thumb that medium suits most work, but the claims differ in context (default setting versus per-task choice), so not filed under MINER.md §4a.
- **Extends**: `blog-anthropic-claude-code-verification-loops-skills` (Claims 1 and 11): adds an effort-level lever to verification loops (verify at high effort) and empirical evidence that verification behaviour scales with effort.
- **Novel**: First note in the corpus with per-level effort curves, a failure-mode breakdown by effort, per-domain effort gains, and effort-versus-spec-quality observations.

## Guide Impact

- **Chapter 02 (Patterns of Work with AI)**: Add the "interview, low-effort build, review, high-effort verify" loop as a named pattern, citing Claim 7. Note that spec quality narrows the effort difference (Claim 6).
- **Chapter 03 (Agent Orchestration)**: When agents run unattended, effort substitutes for clarifying questions (Claim 11), but also raises the risk of committing to a wrong interpretation (Claim 9). Recommend pairing high-effort autonomous runs with explicit requirement checks.
- **Chapter 06 (Scaling / cost-quality)**: Cite the 73k versus 222k median token cost for 140 versus 214 passes (Claim 9) as an effort cost-quality data point, and the domain table (Claim 10) to guide where to spend. Treat it as first-party and internal.
- **Quality-regression discussion**: Cross-link with the reasoning-effort postmortem note for why defaults matter.

## Extraction Notes

- Read the full page (fetched HTML, text-extracted). Charts are interactive, so only values present in captions and replay text were captured. Fig A has no numeric values in text.
- The Claim 12 quote is a contiguous fragment of: "At low (about a minute per attempt), Claude would edit the code before building it or running the reproducer, and did not check that its new test would have caught the original bug."
- Claim 2 quote is the second sentence of the paragraph beginning "You should think of effort in the same way." It is verbatim.
- Linked related posts (cost on Opus 5.5, etc.) were not followed; they are separate issues. The Terminal-Bench release page was not followed.
