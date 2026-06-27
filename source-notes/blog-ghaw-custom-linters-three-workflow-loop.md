---
source_url: https://github.github.com/gh-aw/blog/2026-06-26-custom-linters-sergo-linter-miner-and-lintmonster/
source_type: blog-post
title: "Custom Linters in Practice: Sergo, Linter Miner, and LintMonster"
author: GitHub Agentic Workflows team (GitHub Next / Copilot)
date_published: 2026-06-26
date_extracted: 2026-06-27
last_checked: 2026-06-27
status: current
confidence_overall: emerging
issue: "#1331"
---

# Custom Linters in Practice: Sergo, Linter Miner, and LintMonster

> Describes how three interconnected agentic workflows—Linter Miner (invent), Sergo (challenge), LintMonster (apply)—form a continuous quality-improvement loop that maintains 35+ custom Go analyzers in production, providing the most concrete public evidence in the corpus for treating static analysis as a living agentic system rather than a CI gate.

## Source Context

- **Type**: blog-post (operational deep-dive from the GitHub Agentic Workflows blog, published 2026-06-26, reporting on the team's own production linter infrastructure)
- **Author credibility**: First-party from the GitHub Agentic Workflows team (GitHub Next / Copilot). The `gh-aw` project is their own production codebase. PR numbers, issue chains, and ADR references throughout the post are links to real shipped work in that repository. High credibility for described patterns: the evidence is a production system's observable artifact trail, not a design proposal or aspirational architecture.
- **Scope**: Covers the three-workflow loop (Linter Miner, Sergo, LintMonster), their respective responsibilities, and concrete examples of each in action (PR chains, issue resolution chains, registry counts). Does NOT cover: the workflow YAML/frontmatter for any of the three workflows, the full enumerated list of 35 analyzers, how analyzers are deployed to CI, or how this pattern scales to teams other than gh-aw.

## Extracted Claims

### Claim 1: Three interconnected workflows—Linter Miner, Sergo, and LintMonster—manage 35+ custom Go analyzers as a continuous feedback loop, partitioning invention, validation, and application into distinct roles

- **Evidence**: Source describes the full workflow topology with concrete PR chains and issue examples for each workflow. Current registry is at `cmd/linters/main.go` with 35+ registered analyzers. PR numbers span from #34498 to #41285, suggesting sustained operation over multiple months.
- **Confidence**: emerging (first-party, self-reported from the team's own production system; the 35+ count is stated but the specific list is not reproduced in the post)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This is the central claim. The three-workflow model provides the organizing principle: Linter Miner discovers and proposes; Sergo stress-tests and corrects; LintMonster drives compliance. The architecture avoids the common failure mode of "write a linter and forget it" by continuously cycling through all three phases. The 35+ analyzer count demonstrates sustained production operation over time—not an experimental prototype.

### Claim 2: Linter Miner systematically mines discussions, issues, and source code patterns to propose new analyzers, producing PRs with ADR documentation across multiple months

- **Evidence**: Six concrete examples with PR numbers: fprintlnsprintf (PR #34498), timeafterleak (PR #39133), errorfwrapv (PR #39263), wgdonenotdeferred (PR #40837), lenstringsplit (PR #41090), stringreplaceminusone (PR #41285). The PR range spans hundreds of intermediate PRs, indicating sustained multi-month operation.
- **Confidence**: emerging (PR numbers are traceable artifacts; the analysis approach is described but not the YAML/prompt specification)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The examples cover diverse Go anti-patterns: resource leaks (timeafterleak: `time.After()` in `for`+`select` loops), error chain integrity (errorfwrapv: `fmt.Errorf(%v)` vs `%w`), concurrency correctness (wgdonenotdeferred: non-deferred `Done()`), and performance micro-optimizations (lenstringsplit, stringreplaceminusone). The ADR co-documentation at each PR number is architecturally significant: every new linter rule ships with a persistent rationale, not just the rule binary.

### Claim 3: Sergo acts as an adversarial testing layer for linters, specifically targeting precision gaps and suppression shortcomings—false positives, false negatives, and missing `//nolint:` support

- **Evidence**: Five concrete issue-to-PR resolution chains: #40244→#40248 (extended `errstringmatch` coverage to `HasPrefix`, `HasSuffix`, `EqualFold`, `Index`, `LastIndex`, `Compare`), #41377→#41382 (added `//nolint:` support across four context-family analyzers), #41376→#41383 (fixed `manualmutexunlock` false negatives when struct instances shared mutex fields), #40947→#41026 (corrected `wgdonenotdeferred` to handle goroutine closures within loops), #41163→#41188 (fixed `lenstringsplit` false positives with empty raw-string separators).
- **Confidence**: emerging (issue/PR numbers are traceable; Sergo's testing methodology is described at the level of outcomes rather than its workflow specification)
- **Quote**: "Sergo functions as an adversarial testing layer, identifying precision gaps and suppression shortcomings."
- **Our assessment**: The five examples reveal the systematic failure modes of static analysis tools: missing coverage of related-but-distinct functions (HasPrefix alongside Contains), missing suppression support (nolint), false negatives from struct-field aliasing, loop/closure interaction failures, and edge-case false positives from unusual inputs. A dedicated workflow that continuously finds and resolves these—rather than waiting for user bug reports—represents a qualitatively different quality assurance model.

### Claim 4: Sergo enforces narrow, reviewable changes by rejecting sprawling fixes in favor of targeted corrections

- **Evidence**: Explicit documented example: Issue #40243 / PR #40247 was rejected for being too sprawling; fixes were redirected to separate targeted PRs. This is documented alongside the successful issue-to-PR chains as a deliberate quality gate.
- **Confidence**: emerging (single documented rejection example; the juxtaposition with accepted chains implies a policy, not a one-off judgment)
- **Quote**: "The workflow demonstrates quality discipline by rejecting sprawling fixes (Issue #40243 / PR #40247) in favor of narrower, reviewable changes."
- **Our assessment**: The adversarial challenger workflow is not only finding linter failures but enforcing fix quality. A PR that fixes multiple issues at once is harder to review, harder to bisect on regression, and harder to attribute if wrong. Sergo's rejection of a sprawling PR enforces the same small-PR discipline the guide recommends for human engineers. This suggests the system includes implicit engineering-standards enforcement as a side effect of its challenger role.

### Claim 5: LintMonster executes `make golint-custom`, groups findings by root cause, creates tracked issues, and assigns Copilot sessions for remediation—converting diagnostic output into measurable work queues

- **Evidence**: Four concrete examples: Issue #40932 (four resource-lifecycle and context-propagation findings consolidated; merged via PR #41589), Issue #40933 (hard-coded path constants; resolved via PR #41611), Issue #39314 (function-length backlog established at 653 findings), Issue #41466 (function-length backlog refreshed to 660 findings).
- **Confidence**: emerging (issue/PR numbers are traceable; the Copilot session assignment mechanism is named but the specific session configuration is not shown)
- **Quote**: "This workflow converts static analysis output into actionable work queues."
- **Our assessment**: The function-length backlog example (Issue #39314 → Issue #41466: 653 → 660 findings) is particularly significant: the count increased slightly over time, indicating ongoing work against a changing codebase. The number functions as a time-series KPI for compliance debt—not a one-shot fix target. The Copilot session assignment for remediation closes the loop: LintMonster doesn't merely file issues but actively drives remediation by spinning up a coding agent to make fixes.

### Claim 6: The three-workflow partition—invent (Linter Miner), challenge (Sergo), apply (LintMonster)—enables durability through separation of concerns that are typically conflated in traditional linting

- **Evidence**: Source explicitly names and defines the three functions: "Rule invention (Linter Miner): Creates analyzers from observed patterns"; "Rule validation (Sergo): Tests correctness, precision, and suppression coverage"; "Rule application (LintMonster): Drives production code toward compliance."
- **Confidence**: emerging (first-party framing of their own architecture; durability is asserted but not measured with longitudinal data)
- **Quote**: "This separation enables durability through continuous rule expansion, ongoing correction cycles, and measurable repository progress."
- **Our assessment**: Traditional static analysis conflates all three functions: a human writes a rule, does limited testing, applies fixes manually. The three-workflow partition creates independent feedback loops that can run without coordinating: Linter Miner proposes continuously, Sergo tests each new rule reactively, LintMonster processes approved rules on schedule. A Sergo rejection doesn't block LintMonster from continuing to apply existing approved rules.

### Claim 7: The gh-aw project treats static analysis as a "living workflow system, not just a binary that runs in CI"

- **Evidence**: Direct quote from the source's closing section, summarizing the system's design philosophy. Presented as the primary takeaway of the post.
- **Confidence**: anecdotal (a framing claim, not a measurable technical claim; credible given the operational evidence throughout the post)
- **Quote**: "a living workflow system, not just a binary that runs in CI"
- **Our assessment**: This captures the essential architectural shift the post demonstrates. Static analysis in traditional CI is a gate—pass or fail. The three-workflow system makes it a continuously evolving system: new rules are invented, existing rules are corrected, and compliance debt is actively reduced. The "living" metaphor is justified by the artifact trail: 35+ analyzers, multi-month PR activity, issue-to-PR resolution chains, and KPI tracking.

### Claim 8: Workflow definitions in `.github/workflows/` and the linter registry in `cmd/linters/main.go` form the operational backbone, with each new analyzer co-documented via ADRs at matching PR numbers

- **Evidence**: Key Resources section: "Workflow definitions available in `.github/workflows/`", "Linter registry in `cmd/linters/main.go`", "Architectural decisions documented via ADRs (34498, 39133, 40837, 41090, 41285)". The ADR numbers match the Linter Miner PR numbers exactly.
- **Confidence**: settled (file paths and ADR references are concrete artifacts from the gh-aw repository)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The ADR-per-PR co-documentation pattern is unusually disciplined for automated systems: every Linter Miner PR that introduces a new analyzer also creates an ADR, so every rule has a documented rationale that survives beyond the PR description. The registry in `cmd/linters/main.go` is the authoritative catalog—structurally similar in purpose to the broader agent factory status page.

## Concrete Artifacts

### Three-Workflow Loop Summary (from source)

```
Three-Workflow Loop: Custom Linter Lifecycle in gh-aw

LINTER MINER (Invention):
  Role: Mine discussions, issues, source patterns → propose new analyzers
  Output: PRs with co-documented ADRs
  Examples:
    PR #34498 — fprintlnsprintf: Flags fmt.Fprintln(w, fmt.Sprintf(...)) redundancy
    PR #39133 — timeafterleak: Detects time.After() calls in for+select loop combinations
    PR #39263 — errorfwrapv: Finds fmt.Errorf(%v) where %w should preserve error chains
    PR #40837 — wgdonenotdeferred: Catches non-deferred sync.WaitGroup.Done() invocations
    PR #41090 — lenstringsplit: Rewrites len(strings.Split(s,sep)) to strings.Count(s,sep)+1
    PR #41285 — stringreplaceminusone: Converts strings.Replace(...,-1) to strings.ReplaceAll()

SERGO (Validation / Adversarial Challenge):
  Role: Find precision gaps, false positives/negatives, missing nolint coverage
  Output: Targeted fix PRs per failure type; rejects sprawling fixes
  Examples (accepted):
    Issue #40244 → PR #40248: Extended errstringmatch to HasPrefix/HasSuffix/EqualFold/Index/LastIndex/Compare
    Issue #41377 → PR #41382: Added //nolint: support across four context-family analyzers
    Issue #41376 → PR #41383: Fixed manualmutexunlock false negatives (shared struct mutex fields)
    Issue #40947 → PR #41026: Fixed wgdonenotdeferred for goroutine closures within loops
    Issue #41163 → PR #41188: Fixed lenstringsplit false positives with empty raw-string separators
  Examples (rejected):
    Issue #40243 / PR #40247: REJECTED — sprawling fix; redirected to narrower targeted changes

LINTMONSTER (Application):
  Role: Execute make golint-custom → group by root cause → create tracked issues → assign Copilot sessions
  Output: Tracked work queues with measurable backlog
  Examples:
    Issue #40932 → PR #41589: Four resource-lifecycle and context-propagation findings consolidated
    Issue #40933 → PR #41611: Hard-coded path constants replaced
    Issue #39314: Function-length backlog established (653 findings)
    Issue #41466: Function-length backlog refreshed (660 findings)

Registry: cmd/linters/main.go (35+ registered analyzers)
ADRs: co-documented at PR numbers matching Linter Miner PRs (34498, 39133, 40837, 41090, 41285)
Workflows: .github/workflows/
```

*Source: blog-ghaw-custom-linters-three-workflow-loop, all sections*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-agent-factory-status.md` Claim 7 (Go language specialization cluster uses Claude exclusively; Sergo listed as "Sergo - Serena Go Expert" in the catalog): This article confirms Sergo's specific function within that cluster—adversarial linter testing—validating that Claude-assigned Go workflows perform reasoning-intensive domain work. The catalog note names Sergo; this article explains what Sergo does.
  - `docs-ghaw-code-quality-monitoring.md` Claim 6 (per-category aggregation with minimum instance threshold prevents issue-tracker flooding): LintMonster's approach of grouping findings by root cause before creating issues (Claim 5 here) addresses the same failure mode—a raw linter run producing per-file noise instead of actionable categories. Both patterns enforce finding aggregation before issue creation; the code quality monitoring note applies this as a configuration rule, while LintMonster applies it as a workflow behavior.

- **Extends**:
  - `docs-ghaw-agent-factory-status.md` Claim 7 (Go language specialization cluster — Sergo listed by name and engine only): That note documents Sergo as one of six Claude-assigned Go workflows but provides only its name and engine assignment. This article provides the operational depth: Sergo's adversarial testing role, its issue-to-PR resolution chains, and its discipline of rejecting sprawling fixes. Together the two notes give the complete picture of Sergo's place and function in the factory.
  - `docs-ghaw-guides-serena.md` (Serena as semantic code analysis tool for Go): The factory catalog names Sergo as "Sergo - Serena Go Expert," indicating it uses Serena's LSP-backed symbol navigation for Go analysis. This article describes Sergo's outcomes without naming Serena explicitly; the Serena guide documents the capability layer Sergo most likely uses.

- **Contradicts**: None identified. The three-workflow loop pattern is novel to the corpus and does not conflict with existing claims about quality automation approaches.

- **Novel**:
  - **The three-workflow loop pattern (invent → challenge → apply) as a named, distinct architecture** (Claims 1, 6): No existing source note describes a dedicated adversarial challenger workflow as a discrete phase in a quality-improvement system. The three-way partition of traditionally conflated functions (write rule, test rule, apply rule) is new to the corpus.
  - **ADR co-documentation per new analyzer** (Claims 2, 8): The practice of creating an ADR at the same PR number as the new linter rule is not documented in any existing corpus note. This is a novel documentation discipline for agentic quality systems.
  - **Sprawling-fix rejection as a workflow-enforced policy** (Claim 4): No existing note documents an agentic workflow that enforces fix quality by rejecting PRs for being too broad. This is new as a workflow-as-quality-gate pattern.
  - **Compliance debt tracked as a time-series KPI** (Claim 5): The function-length backlog (653 → 660 findings across two issues over time) as an ongoing metric is not documented anywhere in the corpus. This is the first evidence of a linting workflow tracking aggregate compliance debt longitudinally.
  - **Copilot session assignment for issue remediation** (Claim 5): LintMonster's pattern of assigning Copilot sessions to drive issue resolution—not just filing issues and waiting—is not documented elsewhere in the corpus as an agentic close-the-loop pattern.

## Guide Impact

- **Chapter 02 (Automation Patterns / Harness Engineering)**: Add the three-workflow loop (invent → challenge → apply) as a named pattern for self-sustaining quality automation. The key design principle—separating invention, validation, and application into independent feedback loops—generalizes beyond Go linting to any domain where AI discovers patterns, tests its own rules, and drives compliance. The ADR co-documentation practice (Claim 2) is a concrete recommendation to add: agentic quality workflows should produce rationale artifacts alongside their automation artifacts.

- **Chapter 04 (Tool Integration and Validation Loops)**: The adversarial challenger role (Sergo's function in Claim 3) is a concrete application of validation loops to AI-generated artifacts. Sergo validates linter rules that Linter Miner created—the system challenges its own prior output. Document the specific failure modes Sergo finds (precision gaps, suppression coverage, edge-case false positives/negatives) as a checklist for teams building similar challenger workflows. The sprawling-fix rejection policy (Claim 4) is an additional recommendation: challenger workflows should enforce fix quality, not merely identify failures.

- **Chapter 03 (Quality & Testing)**: The function-length backlog tracking pattern (Issue #39314 → Issue #41466: 653 → 660 findings as a time-series KPI, Claim 5) is a concrete recommendation for teams asking how to measure progress on AI-driven code quality work. Create a periodic "backlog refresh" issue alongside targeted remediation issues to maintain a longitudinal view of compliance debt rather than treating each linting run as independent.

## Extraction Notes

1. **WebFetch returned structured summary from the blog post**: WebFetch was prompted to extract full text verbatim. The output is structured with headings and paragraphs that match blog post section structure. The sole confirmed verbatim passage (in explicit quotation marks in the WebFetch output) is "a living workflow system, not just a binary that runs in CI." Other phrasings used as quotes (Claims 3, 4, 5, 6) appeared as structured paragraph text in the WebFetch output and are assessed as likely verbatim but not guaranteed to be character-for-character. The Assayer should spot-check against the source URL.

2. **PR and issue numbers are concrete but unverified links**: All PR and issue numbers (e.g., #34498, #40932) are cited from the source as-is. They are traceable artifacts in the gh-aw GitHub repository but were not independently fetched or verified during extraction.

3. **Workflow YAML not provided in the source**: The post does not show frontmatter YAML for any of the three workflows. Operational behavior is described in narrative form only. See `docs-ghaw-how-they-work.md` for the general workflow specification format.

4. **Serena connection is inferential**: "Sergo - Serena Go Expert" in the factory catalog (`docs-ghaw-agent-factory-status.md` Claim 7) suggests Sergo uses Serena for semantic Go analysis, but the source article does not mention Serena by name. The cross-reference to `docs-ghaw-guides-serena.md` is noted as inferential.

5. **No sub-pages followed**: The source is a single blog post page with no linked sub-pages requiring follow-up.

6. **No contradictions filed**: Reviewed existing source notes. No claims in this source materially oppose existing claims at the MINER.md §4a filing threshold. The three-workflow loop pattern is novel; it extends the factory catalog note rather than contradicting it.
