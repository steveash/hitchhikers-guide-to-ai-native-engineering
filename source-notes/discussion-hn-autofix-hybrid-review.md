---
source_url: https://news.ycombinator.com/item?id=46237358
source_type: discussion
title: "Show HN: Autofix Bot – Hybrid static analysis and AI code review agent"
author: sanketsaurav (Sanket Saurav, co-founder, DeepSource; YC W20)
date_published: 2025-12-11
date_extracted: 2026-04-15
last_checked: 2026-04-15
status: current
confidence_overall: emerging
issue: "#48"
---

# Show HN: Autofix Bot – Hybrid Static Analysis and AI Code Review Agent

> A Show HN product launch from DeepSource that doubles as the most concrete
> public taxonomy of LLM-only code-review failure modes available, backed by
> vendor-run benchmark data comparing Autofix Bot, Cursor Bugbot, Claude Code,
> CodeRabbit, and Semgrep CE on the OpenSSF CVE benchmark (200+ real JS/TS
> vulnerabilities). The extractable value is the failure-mode taxonomy, the
> precision/recall breakdown that shows Claude Code has *high* precision but
> very *low* recall for security issues, the hybrid architecture pattern, and
> the per-PR cost comparison.

## Source Context

- **Type**: discussion (Show HN product announcement, 37 points, 13 comments,
  2025-12-11). DeepSource is a YC W20 company building static analysis and code
  health tooling; the founders are Jai and Sanket Saurav. This is a vendor-authored
  launch post, not an independent study. All benchmark data is self-reported unless
  cross-verified against the published benchmark repository
  (https://github.com/ossf-cve-benchmark/ossf-cve-benchmark).
- **Author credibility**: Sanket Saurav is a co-founder of DeepSource, a company
  with documented static analysis infrastructure (5,000+ checkers across multiple
  languages). The claims about static analysis anchoring and AST/data-flow tool
  access are architecturally coherent and consistent with the company's known
  product capabilities. The benchmark numbers are self-reported from a vendor
  with a clear interest in favorable results; treat them as first-party evidence
  requiring independent verification, not as authoritative ground truth. The
  benchmark repo is published and open for replication.
- **Scope**: The HN post covers the product motivation, the LLM-only failure-mode
  taxonomy, the hybrid architecture, and the benchmark results. The linked product
  site (https://autofix.bot) expands the architecture detail and adds the full
  benchmark table including precision/recall/time data. The HN comments add cost
  comparison context (165 real PRs). Does NOT cover: false-positive rates in
  practice, non-JS/TS language performance, behavior on large codebases, or
  long-term production adoption data.

## Extracted Claims

### Claim 1: LLM-only code review has four specific, documentable failure modes

- **Evidence**: Author's structured enumeration from the HN post launch text,
  supported by benchmark data (low recall figures for pure-LLM tools vs.
  hybrid approach).
- **Confidence**: emerging (the taxonomy is well-structured; the benchmark
  partially validates it for the recall claim; non-determinism is widely
  corroborated independently)
- **Quote**: "LLM-only review has several limitations: non-deterministic across
  runs, low recall on security issues, expensive at scale, and a tendency to
  get distracted" [from issue body preview of the original post text]
- **Our assessment**: This is the most crisply articulated failure taxonomy in
  our corpus for LLM-only code review. The four modes are analytically distinct:
  (1) non-determinism is a reliability problem, (2) low security recall is a
  coverage problem, (3) cost is an economics problem, (4) distraction is a focus
  problem. The benchmark provides direct evidence for the recall claim (Claude
  Code recall: 48.78%). The non-determinism claim is independently settled by
  practitioner observation. The "distraction" mechanism — LLMs flagging stylistic
  issues while missing security bugs when both types are present — is the least
  independently verified claim but the most architecturally consequential (it
  is the reason static findings are used as anchors).

### Claim 2: Claude Code has the highest precision (88.89%) but the lowest recall (48.78%) among AI code review tools on the OpenSSF CVE benchmark

- **Evidence**: Vendor-run benchmark on the OpenSSF CVE dataset (200+ real
  JS/TS vulnerabilities). Claude Code was run using "official security review
  command with diff simulation." Full results below in Concrete Artifacts.
- **Confidence**: anecdotal (vendor-run, single benchmark, specific methodology
  per tool)
- **Quote**: N/A (table data, not quoted prose)
- **Our assessment**: The precision/recall split is the single most actionable
  data point in this source. 88.89% precision means Claude Code almost never
  generates a false positive — when it flags something, it's real. But 48.78%
  recall means it misses more than half of actual vulnerabilities in the test
  set. For a team relying on Claude Code for security review via the built-in
  `/review` or security skill: the tool is *not* a comprehensive security
  scanner. It is a high-confidence pointer to a subset of issues. Teams that
  interpret "Claude Code found no security issues" as "there are no security
  issues" are operating on a false premise. The recall gap is the empirical
  reason why the sentry-security skill (37 historical patches → 6 vulnerability
  classes → HIGH/MEDIUM threshold) exists at Sentry: it compensates for exactly
  this recall gap. **Critical caveat**: the benchmark was run by DeepSource with
  tool-specific invocation methods that may not represent each tool's optimal
  usage. Claude Code's "diff simulation" may differ from its real-world
  interactive use. Independent replication against the published benchmark repo
  is strongly recommended before citing these figures in production guidance.

### Claim 3: The hybrid architecture solves the LLM distraction/recall problem by using static findings as anchors for AI review

- **Evidence**: Author's architectural description confirmed by benchmark
  improvement (Autofix Bot F1 80.00% vs. Claude Code F1 62.99%). The
  benchmarks page describes the pipeline explicitly.
- **Confidence**: emerging
- **Quote**: "AI reviews code using static findings as anchors, with access to
  AST, data-flow graphs, control-flow, import graphs as tools"
- **Our assessment**: This is a concrete architectural pattern worth extracting
  for the guide, independent of whether Autofix Bot specifically is
  recommended. The insight is that giving an LLM both (a) deterministic
  static findings to anchor on and (b) structured program analysis as tools
  (AST, CFG, data-flow) addresses both failure modes: anchoring prevents
  distraction, structured analysis provides the semantic context the LLM
  needs to reason about vulnerabilities. The Sentry `sentry-backend-bugs`
  skill is the manual practitioner-built version of the same pattern (encode
  known bug patterns → use as AI review anchors). Autofix Bot is attempting
  to automate this at scale.

### Claim 4: OpenSSF CVE benchmark shows the full precision/recall/time tradeoff across tools

- **Evidence**: Vendor benchmark on 200+ real-life security vulnerabilities in
  JavaScript and TypeScript, validated and fixed in open-source projects. Tools
  tested against simulated pull requests (vulnerable version vs. patched version
  per CVE). See Concrete Artifacts for full table.
- **Confidence**: anecdotal (vendor-run; methodology differences between tools
  not normalized; benchmark repo is public but results not independently
  replicated to our knowledge)
- **Quote**: "For each CVE in the benchmark, we created two variants: the
  vulnerable version and the patched version."
- **Our assessment**: Accuracy was selected as the "hero metric" (correct on
  both variants), with F1 capturing the precision/recall balance. The time
  column (43.92s for Claude Code vs. 143.77s for Autofix Bot vs. 189.88s for
  Cursor Bugbot) reveals that Claude Code's speed advantage is substantial —
  it is ~3× faster than Autofix and ~4× faster than Cursor Bugbot. For
  pipelines where review latency matters (e.g., pre-commit hooks), the
  precision/speed combination may favor Claude Code over the hybrid
  approach despite the recall gap.

### Claim 5: Cursor Bugbot has the highest recall (87.80%) among the tested tools but lower precision (69.23%)

- **Evidence**: Vendor benchmark (same dataset as Claim 4).
- **Confidence**: anecdotal
- **Quote**: N/A (table data)
- **Our assessment**: The Cursor Bugbot precision/recall profile is the inverse
  of Claude Code's: it catches more vulnerabilities but generates more false
  positives. For a security-critical codebase, high recall is the right
  optimization — missing a real vulnerability is worse than investigating a
  false positive. The F1 score (77.42%) reflects this tradeoff landing at
  a reasonable balance. The slower speed (189.88s avg) limits use as an
  interactive tool. The $40/month cap at 200 PRs is a hard deployment ceiling
  for high-velocity teams.

### Claim 6: Secrets detection accuracy varies enormously across tools — from 41.22% F1 (TruffleHog) to 92.78% F1 (Autofix Bot)

- **Evidence**: Vendor benchmark on a proprietary labeled secrets corpus
  (imbalanced dataset). Results in Concrete Artifacts.
- **Confidence**: anecdotal (vendor-run, proprietary dataset not independently
  verifiable)
- **Quote**: "Autofix Bot achieves results by combining a static regex sweep
  (maximizing recall) with a custom fine-tuned classifier (maximizing precision)."
- **Our assessment**: The variance across tools is striking and useful regardless
  of which tool wins. TruffleHog at 41.22% F1 is better than random but
  misses most secrets (27.41% recall). Gitleaks (75.62% F1) is substantially
  better but still misses ~38% of secrets. The "regex sweep + classifier"
  approach (Narada-3.2-3B-v1) achieving 87.45% recall with 98.69% precision
  is a clean example of the same hybrid pattern applied to secrets detection:
  the broad net (regex) catches everything suspicious, the narrow filter
  (classifier) removes false positives. **Dataset caveat**: the secrets corpus
  is proprietary to DeepSource; the secrets detection benchmark cannot be
  independently replicated.

### Claim 7: Per-PR cost on 165 real pull requests: Autofix Bot $21.24 vs. Claude Code $48.86

- **Evidence**: Founder's direct comment in the HN thread responding to a
  pricing concern, citing actual run data on 165 PRs.
- **Confidence**: anecdotal (single dataset, vendor-reported, context unknown)
- **Quote**: "On 165 pull requests, actual costs were: Autofix Bot ($21.24),
  Claude Code ($48.86)"
- **Our assessment**: The 2.3× cost difference is meaningful if the quality
  metrics are comparable. The caveats are: (a) we don't know the PR size
  distribution or language mix of those 165 PRs, (b) Claude Code at $48.86
  for 165 PRs is ~$0.30/PR at the token cost, which scales differently from
  Autofix's $8/100k LOC model, (c) Claude Code was likely run in the same
  benchmark configuration used for the accuracy test ("diff simulation"),
  not necessarily optimal for cost. For the guide's cost framing: static
  analysis as an LLM filter (anchor) reduces token consumption by scoping
  the LLM review to flagged areas, which drives the cost difference. This
  is a generalizable principle, not unique to Autofix Bot.

### Claim 8: The hybrid pipeline architecture is a 7-step sequence

- **Evidence**: Author's architectural description on the benchmarks page.
- **Confidence**: anecdotal (self-described; no independent code review)
- **Quote**: "Codebase indexing → Static pass → AI review → Remediation →
  Sanitization → Output → Caching"
- **Our assessment**: The 7-step breakdown is useful as a reference architecture
  for teams designing their own review quality gates. The critical novelty vs.
  pure LLM approaches is steps 2 and 5: the static pass anchors the AI, and the
  sanitization step validates fixes before output. The caching layer (step 7) is
  the cost-efficiency mechanism — repeat diffs on similar patterns don't re-invoke
  the full AI pipeline. Teams building custom review gates in Claude Code
  could implement a simplified version: run static analysis first (Semgrep, ESLint,
  Bandit), pass findings to Claude with "review these specific locations" rather
  than "review this entire diff."

### Claim 9: AI coding agents have shifted the bottleneck from code generation to code review

- **Evidence**: Author's framing statement opening the product announcement.
- **Confidence**: emerging (consistent with Faros 35% longer review times,
  Miller et al. 30.3% static warning increase, and Pragmatic Engineer survey data)
- **Quote**: "AI coding agents have made code generation nearly free, and they've
  shifted the bottleneck to code review."
- **Our assessment**: This framing is consistent with multiple independent sources
  in our corpus. The Faros report found 35% longer review times alongside 47% more
  PRs. Miller et al. found 30.3% more static analysis warnings. The shift from
  generation bottleneck to review bottleneck is corroborated; the specific framing
  ("nearly free") is marketing but captures a real directional change. For the
  guide: this is a good one-sentence summary of why code review automation is
  now load-bearing infrastructure, not optional tooling.

## Concrete Artifacts

### OpenSSF CVE Benchmark Results (vendor-run, JS/TS, 200+ CVEs)

```
Benchmark dataset: OpenSSF CVE Benchmark
https://github.com/ossf-cve-benchmark/ossf-cve-benchmark
200+ real-life security vulnerabilities in JavaScript and TypeScript,
validated and fixed in open-source projects.
Methodology: simulated pull requests (vulnerable version + patched version per CVE).
Run by DeepSource. Results are vendor-reported.

Tool            | Accuracy | Precision | Recall  | F1 Score | Avg. Time
----------------|----------|-----------|---------|----------|----------
Autofix Bot     | 81.21%   | 84.93%    | 75.61%  | 80.00%   | 143.77s
Cursor Bugbot   | 74.55%   | 69.23%    | 87.80%  | 77.42%   | 189.88s
Claude Code     | 71.52%   | 88.89%    | 48.78%  | 62.99%   |  43.92s
CodeRabbit      | 59.39%   | 82.61%    | 23.17%  | 36.19%   | 124.81s
Semgrep CE      | 56.97%   | 66.67%    | 26.83%  | 38.26%   |  90.00s

Note: Claude Code invoked via "official security review command with diff simulation."
Note: Cursor Bugbot tested through GitHub PRs with Bugbot integration.
Note: Semgrep run with default rulesets against codebases.
Different invocation methods were used per tool — results may not reflect
each tool's optimal configuration for security review.
```

### Secrets Detection Benchmark Results (vendor-run, proprietary corpus)

```
Benchmark dataset: DeepSource proprietary labeled secrets corpus (imbalanced).
Results are vendor-reported. Dataset not publicly available for independent replication.

Tool              | F1 Score | Precision | Recall  | Perfect Matches | Missed Secrets
------------------|----------|-----------|---------|-----------------|---------------
Autofix Bot       | 92.78%   | 98.69%    | 87.45%  | 453             | 65
Gitleaks          | 75.62%   | 96.98%    | 61.97%  | 303             | 197
detect-secrets    | 64.09%   | 67.52%    | 61.00%  | 270             | 202
TruffleHog        | 41.22%   | 83.04%    | 27.41%  | 121             | 376

Autofix approach: static regex sweep (maximize recall) +
Narada-3.2-3B-v1 fine-tuned classifier (maximize precision).
Source: https://huggingface.co/deepsource/Narada-3.2-3B-v1
```

### Per-PR Cost Comparison (vendor-reported, 165 PRs)

```
From HN comment by sanketsaurav responding to pricing question:

165 pull requests measured:
  Autofix Bot:   $21.24  (~$0.13/PR)
  Claude Code:   $48.86  (~$0.30/PR)
  Cursor Bugbot: $40/month (200 PR hard limit per month)

Autofix Bot pricing: $8 per 100,000 lines of code reviewed.
Context unknown (PR size distribution, language mix, codebase type not specified).
```

### Hybrid Pipeline Architecture (7-step)

```
Step 1: Codebase Indexing  — AST and project graph creation
Step 2: Static Pass        — 5,000+ deterministic checkers establish baseline findings
Step 3: AI Review          — Agent reviews diff using static findings as anchors;
                             has access to AST, data-flow graphs, control-flow,
                             import graphs as tools
Step 4: Remediation        — Specialized sub-agents generate fix candidates
Step 5: Sanitization       — Language-specific validation of edits before output
Step 6: Output             — Git patch emission
Step 7: Caching            — Multi-layered caching optimization (repeat patterns
                             skip full AI pipeline)

Source: https://autofix.bot/benchmarks (Architecture Overview section)
```

### LLM-Only Code Review Failure Mode Taxonomy

```
Four failure modes of LLM-only code review (from the Show HN post):

1. Non-determinism across runs
   — Same diff, different findings on repeated invocations

2. Low recall on critical issues
   — "LLMs get distracted by stylistic concerns and miss real problems,
     especially when multiple issue types are present."
   — Validated by benchmark: Claude Code recall 48.78%, CodeRabbit 23.17%

3. Expensive at scale
   — Full-diff LLM review per PR compounds with PR volume
   — 2.3× cost gap vs. static-anchored approach on 165 PRs

4. Distraction / focus dilution
   — LLMs flag low-severity style issues; high-severity security issues deprioritized
   — Mechanism for static anchoring: force the LLM to focus on pre-identified
     high-signal locations

Source: HN post body + benchmarks page failure-mode description
```

## Cross-References

- **Corroborates**: `paper-miller-speed-cost-quality.md` — Miller et al. found
  30.3% increase in static analysis warnings post-Cursor adoption (i.e., AI
  adoption increases static analysis noise). This source provides the *inverse
  design*: using static analysis as an anchor to filter AI review, rather than
  AI generating code that then fails static analysis. Together they frame a
  feedback loop: AI-generated code triggers more static warnings, and static
  warnings are most useful when fed back to AI reviewers as structured anchors
  rather than post-hoc reports.

- **Corroborates**: `practitioner-getsentry-sentry.md` — Sentry's
  `sentry-backend-bugs` skill (638 real production issues, 11 bug-pattern checks,
  HIGH/MEDIUM confidence thresholds) is the manually-curated practitioner
  equivalent of the hybrid architecture described here. Both encode known-bad
  patterns as structured AI guidance rather than relying on open-ended LLM
  review. The Sentry `sentry-security` skill (37 historical patches, 6
  vulnerability classes) directly parallels the role of Autofix Bot's static
  pass as an anchor for AI security review. The difference is scale and
  automation: Sentry's approach requires a platform team to curate the patterns;
  Autofix automates pattern discovery via static analysis.

- **Corroborates**: `blog-faros-claude-code-roi.md` — Faros found 35% longer
  review times alongside 47% more PRs post-Claude-Code adoption. This source
  provides a mechanism: if LLM-only review has recall gaps (48.78% for Claude
  Code) and generates non-deterministic findings, teams iterate over multiple
  review rounds, driving review time up. The hybrid approach is one architectural
  response to the Faros review-time bottleneck.

- **Extends**: `paper-miller-speed-cost-quality.md` — Miller et al. found that
  quality assurance is the bottleneck for AI productivity. This source provides
  a specific architectural pattern (hybrid static+LLM) for addressing one
  dimension of that bottleneck (security recall in code review). Miller does not
  cover review tooling; this source fills that gap.

- **Novel**: The precision/recall breakdown per AI code review tool (especially
  Claude Code's 88.89% precision / 48.78% recall split) is new to the corpus
  and directly actionable for teams using Claude Code for security review. The
  "distraction" failure mode (LLMs deprioritize security when stylistic issues
  are also present) is also new; no other source in the corpus has articulated
  this mechanism specifically.

- **Tension with**: The benchmark figures should not be taken as settled without
  independent replication. The OpenSSF CVE benchmark repo is public; any reader
  who re-runs these tests using each tool's native workflow (rather than the
  invocation methods DeepSource used) may get different results. The guide
  should present these numbers as directional evidence with the caveat noted.

## Guide Impact

- **Chapter on Quality Gates / Code Review**: Use Claim 2 (Claude Code precision
  88.89% / recall 48.78%) to establish that "run Claude Code security review" is
  a necessary but not sufficient quality gate for security-critical code. A team
  relying solely on LLM review for security misses ~half of detected vulnerabilities.
  Recommend pairing Claude Code review with deterministic static analysis (Semgrep,
  Bandit, ESLint security plugins) — running the static pass first, then passing
  findings to Claude. This is an implementation of the hybrid pattern described here
  without requiring Autofix Bot specifically.

- **Chapter on Harness Engineering**: Extract the hybrid pipeline as a general
  pattern recommendation (see Concrete Artifacts, 7-step pipeline). Teams can
  implement steps 1-3 using: existing static analysis tools + Claude Code with
  a prompt anchored on the static findings. The specific invocation:
  "Here are the static analysis findings for this diff: [findings]. Focus your
  security review on these locations and report any additional vulnerabilities
  you find in the surrounding context." This addresses both the distraction
  failure mode and the recall gap.

- **Chapter on Tool Selection**: The benchmark table (Concrete Artifacts) is the
  most concrete head-to-head comparison in our corpus for security review tools.
  Present it with the methodology caveats. The key operational decision factors
  are: precision vs. recall preference (Claude Code is precision-optimized;
  Cursor Bugbot is recall-optimized); latency requirements (Claude Code 43.92s
  avg is 3-4× faster than others); and cost structure.

- **Chapter on Cost and Economics**: Use Claim 7 ($21.24 vs. $48.86 per 165 PRs)
  to illustrate that static analysis as a pre-filter reduces LLM token cost by
  constraining scope. The general principle is: any pipeline that narrows the LLM's
  focus to pre-identified high-signal areas will cost less than one that passes the
  full diff. This principle applies regardless of which tools are used.

## Extraction Notes

1. **Source type clarification**: The issue was auto-discovered as a failure report
   by the failure scanner. The Prospector correctly identified that the primary
   artifact is a Show HN product launch with embedded technical claims. The `triaged:text`
   label governs extraction. This note treats the source as a discussion source,
   not a first-person failure narrative.

2. **Vendor benchmark caveat — critical**: All benchmark data in this source is
   run by DeepSource, the company selling the winning tool. The OpenSSF CVE benchmark
   dataset is publicly available at https://github.com/ossf-cve-benchmark/ossf-cve-benchmark,
   but the *execution methodology* for each competing tool was designed and run by
   DeepSource. Specifically: (a) Claude Code was run with "diff simulation" rather
   than its native interactive workflow; (b) CodeRabbit was evaluated in batches of
   5 due to rate limits, potentially disadvantaging it vs. native operation;
   (c) Semgrep was run with default rulesets, not the tuned rulesets a security
   team would configure. The secrets detection benchmark uses a *proprietary* dataset
   that cannot be independently replicated. Treat all benchmark figures as vendor
   self-report that is directionally indicative but unverified.

3. **Multiple sub-sources read**: In addition to the HN post and comments,
   the following linked pages were read for this extraction:
   - https://autofix.bot (product homepage — feature list, pricing model)
   - https://autofix.bot/benchmarks (full benchmark tables with precision/recall/time)
   Both were accessible as of extraction date 2026-04-15.

4. **Narada model**: The Narada-3.2-3B-v1 classifier used for secrets detection
   is open-sourced on HuggingFace (https://huggingface.co/deepsource/Narada-3.2-3B-v1).
   Teams interested in the hybrid regex+classifier pattern for secrets detection
   can inspect the model weights and training approach.

5. **Pricing caveat**: The $8/100k LOC pricing is stated as subject to revision
   in the HN post. The per-PR cost figures were from one HN commenter exchange;
   treat as directional illustration of the cost-difference mechanism, not as
   current pricing guidance.

6. **Language coverage**: The benchmark covers only JavaScript and TypeScript CVEs.
   Language coverage for the product (TypeScript, Rust, SQL stated) does not include
   Python, Go, Java, C++. Teams working primarily in those languages cannot use this
   benchmark to evaluate the tool.
