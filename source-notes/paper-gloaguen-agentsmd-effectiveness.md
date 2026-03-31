---
source_url: https://arxiv.org/abs/2602.11988
source_type: paper
title: "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"
author: Thibaud Gloaguen, Niels Mündler, Mark Niklas Müller, Veselin Raychev, Martin Vechev
date_published: 2026-02-12
date_extracted: 2026-03-30
last_checked: 2026-03-30
status: current
confidence_overall: emerging
issue: "N/A — enqueued from blog-addyosmani-code-agent-orchestra extraction"
---

# Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?

> The first rigorous empirical study of whether AGENTS.md / context files actually help AI coding agents. Finds that LLM-generated context files reduce success rates and increase cost, while developer-written files provide marginal improvement. Introduces AGENTbench (138 tasks, 12 repos) as a complementary benchmark to SWE-bench.

## Source Context

- **Type**: paper (arXiv preprint, not yet peer-reviewed at a top venue)
- **Author credibility**: All five authors are at ETH Zurich's SRI Lab (Secure, Reliable, and Intelligent Systems Lab), led by Martin Vechev, a well-known figure in program analysis and ML for code. The lab has a strong publication record at ICML, NeurIPS, PLDI, etc. This is a credible research group, not a vendor marketing study.
- **Scope**: Evaluates four coding agents across two benchmarks (SWE-bench Lite and AGENTbench) under three conditions (no context, LLM-generated context, developer-written context). Measures success rate, inference cost, tool usage patterns, and instruction compliance. Does NOT evaluate non-Python languages, does NOT measure code quality beyond pass/fail, does NOT test context files in long-term iterative workflows (only single-shot task resolution). Code and benchmark available at https://github.com/eth-sri/agentbench.

## Methodology

### Agents evaluated (4)
1. Claude Code with Sonnet 4.5
2. Codex with GPT-5.2
3. Codex with GPT-5.1 Mini
4. Qwen Code with Qwen3-30B-Coder

### Benchmarks (2)
- **SWE-bench Lite**: 300 tasks from 11 popular Python repos (established benchmark)
- **AGENTbench** (new, constructed by authors): 138 instances from 5,694 PRs across 12 repositories with developer-committed context files

### Conditions (3)
1. **None**: No context file provided
2. **LLM-generated**: Using recommended initialization commands (e.g., `/init`)
3. **Developer-written**: Pre-existing human-authored context files (AGENTbench only)

### AGENTbench construction
- Source: 5,694 pull requests across 12 repositories
- Filtered to 138 final instances
- Minimum requirement: 400+ PRs per repository for candidate selection
- Average PR patch: 118.9 lines edited (range: 12-1,973)
- Average files edited: 2.5 (range: 1-23)
- Average context file length: 641 words (range: 24-2,003)
- Average context file sections: 9.7 (range: 1-29)
- Test coverage: 75% of modified code on average (range: 2.5%-100%)
- 87% of filtered instances had at least one passing test
- Manual inspection of 10% of generated instances: none leaked the solution

## Extracted Claims

### Claim 1: LLM-generated AGENTS.md files reduce task success rates by 0.5% on SWE-bench Lite and 2% on AGENTbench
- **Evidence**: Controlled experiment across 4 agents, 2 benchmarks. Decreases observed in 5 out of 8 settings across both benchmarks. The effect is small but consistent in direction.
- **Confidence**: emerging
- **Quote**: "average resolution rate is reduced by 0.5%" (SWE-bench Lite); "2% average" reduction (AGENTbench)
- **Our assessment**: The numbers are smaller than Osmani's "~3%" summary suggests. The 0.5% SWE-bench Lite figure is within noise for a 300-task benchmark. The 2% AGENTbench figure on 138 tasks is also small. No confidence intervals or statistical significance tests are reported for these headline numbers. The consistent direction across agents is more meaningful than the magnitude. We should cite the directional finding (LLM-generated files do not help and may hurt) at higher confidence than the specific percentages.

### Claim 2: Developer-written context files improve success by ~4% on AGENTbench
- **Evidence**: Same controlled experiment. Developer-written files tested only on AGENTbench (SWE-bench repos lack developer-written context files).
- **Confidence**: emerging
- **Quote**: "4% on average" improvement
- **Our assessment**: This is the more actionable finding. However, it is measured on only 138 tasks from 12 repos, all Python. Per-repository analysis shows "no single repository where the presence of context files has a significant impact" (Figure 12), meaning the 4% is an average that masks high variance. The finding supports our guide's recommendation to write context files by hand, but it should not be presented as a large or reliable effect.

### Claim 3: Context files increase inference cost by 20-23% on average
- **Evidence**: Table 2 provides per-model, per-benchmark cost comparisons. SWE-bench Lite: +20% average. AGENTbench: +23% average.
- **Confidence**: emerging
- **Quote**: "20% increase on average" (SWE-bench Lite); "23% increase on average" (AGENTbench)
- **Our assessment**: This is the most robust finding in the paper. Cost increase is mechanistic -- more context means more tokens processed, and the behavioral changes (more exploration, more testing) compound the effect. The specific per-model costs are useful:

| Model | Dataset | No context | LLM context | Human context |
|-------|---------|-----------|-------------|---------------|
| Sonnet-4.5 | SWE-Bench | $1.30 | $1.51 | - |
| GPT-5.2 | SWE-Bench | $0.32 | $0.43 | - |
| GPT-5.1 Mini | SWE-Bench | $0.18 | $0.22 | - |
| Qwen3-30B | SWE-Bench | $0.12 | $0.13 | - |
| Sonnet-4.5 | AGENTbench | $1.15 | $1.33 | $1.30 |
| GPT-5.2 | AGENTbench | $0.38 | $0.57 | $0.54 |
| GPT-5.1 Mini | AGENTbench | $0.18 | $0.20 | $0.19 |
| Qwen3-30B | AGENTbench | $0.13 | $0.15 | $0.15 |

Note: developer-written files also increase cost (compare "No context" vs "Human context" columns), just slightly less than LLM-generated ones.

### Claim 4: Agents faithfully follow instructions in context files, including tool-specific directives
- **Evidence**: Behavioral analysis of agent traces. When `uv` is mentioned in context files, it is used 1.6 times per instance on average vs. fewer than 0.01 times without mention. Repository-specific tools: 2.5 times per instance when mentioned vs. fewer than 0.05 when not.
- **Confidence**: settled
- **Quote**: "uv is used 1.6 times per instance on average when mentioned in the context files, compared to fewer than 0.01 times when it is not mentioned"
- **Our assessment**: This is the anchoring effect in quantitative form, and it is the paper's most practically important finding. It means context files function as behavioral nudges with high compliance rates. The implication is two-directional: (a) you can reliably steer agents by mentioning tools/approaches, and (b) mentioning the WRONG tools/approaches will reliably steer agents the wrong way. This validates the "anchoring effect" concern from Osmani's blog -- mentioning deprecated technologies will bias agents toward them.

### Claim 5: Context files encourage broader exploration and more testing, which increases cost without proportional benefit
- **Evidence**: Figure 6 shows tool call increases across all categories (testing, grep, file reading, file writing) when context files are present. Steps increase by +2.45 on SWE-bench Lite and +3.92 on AGENTbench when LLM-generated context is used.
- **Confidence**: emerging
- **Quote**: "context files encourage broader exploration (e.g., more thorough testing and file traversal)"
- **Our assessment**: This is the mechanism behind the cost increase. Context files that say things like "always run the full test suite" or "review related modules" cause agents to do exactly that -- even when the task does not require it. The extra exploration is not discriminate; it applies equally to easy and hard tasks. This supports our guide's principle that context is a budget, not a feature.

### Claim 6: LLM-generated context files are largely redundant with existing repository documentation
- **Evidence**: When .md files, example code, and docs/ folders were removed from repositories, LLM-generated context files improved performance by +2.7% on average, outperforming developer-written documentation.
- **Confidence**: emerging
- **Quote**: "LLM-generated context files not only consistently improve performance by 2.7% on average, but also outperform developer-written documentation" (in documentation-stripped scenarios)
- **Our assessment**: This is the smoking gun for why auto-generated context hurts in normal repos. The LLM-generated content is a lossy summary of what the documentation already says. In a normal repo with intact docs, it is noise. When docs are removed, the summary becomes the only source of that information and is better than nothing. This directly validates the "filter test" recommendation in our guide: if the agent can discover it from the repo, delete it from AGENTS.md.

### Claim 7: Context file overviews do not help agents find relevant files faster
- **Evidence**: Figure 4 measures the average number of steps before the agent interacts with any file modified in the original PR patch. Context files "did not meaningfully reduce" this metric.
- **Confidence**: emerging
- **Quote**: Context files "did not meaningfully reduce" discovery speed
- **Our assessment**: This undercuts a common justification for codebase overviews in AGENTS.md ("it helps the agent navigate"). The agents find the right files at roughly the same speed with or without the overview. 100% of Sonnet-4.5-generated context files and 95-99% of other models' files were flagged as containing codebase overviews -- yet this content provides no measurable benefit for file discovery.

### Claim 8: Reasoning token usage increases with context files
- **Evidence**: Figure 7 shows GPT-5.2 with LLM context uses +22% reasoning tokens on SWE-Bench, +14% on AGENTbench. GPT-5.1 Mini: +14% and +10% respectively. Developer-written context increases reasoning by +20% (GPT-5.2), +2% (GPT-5.1 Mini).
- **Confidence**: emerging
- **Quote**: N/A (extracted from figures)
- **Our assessment**: Reasoning tokens are "thinking" overhead that does not appear in output but consumes cost and latency. A 22% increase in reasoning without a success rate improvement means the model is "thinking harder" about irrelevant instructions. This is additional evidence for the context-as-budget principle.

### Claim 9: Using a stronger model to generate context files does not consistently help
- **Evidence**: Ablation using GPT-5.2 + Codex-generated files for all agents. SWE-bench: +2% average improvement. AGENTbench: -3% average degradation.
- **Confidence**: emerging
- **Quote**: "Neither the prompt matching the underlying model and agent, nor a specific prompt performs consistently best"
- **Our assessment**: This closes a potential objection ("the auto-generated files were bad because the generating model was weak"). Even with a stronger generator, the results are inconsistent. The problem is not generation quality -- it is the fundamental redundancy of auto-generated content.

### Claim 10: No single repository shows statistically significant context file impact
- **Evidence**: Figure 12 shows per-repository variance in success rate changes.
- **Confidence**: emerging
- **Quote**: "no single repository where the presence of context files has a significant impact"
- **Our assessment**: This is the most important limitation. The headline ~3% hurt / ~4% help numbers are averages across repos with high variance. For any given repository, context files might help substantially, hurt substantially, or make no difference. The implication: the value of AGENTS.md is highly context-dependent. Blanket recommendations for or against are overfit to averages.

## Concrete Artifacts

### Per-model cost data (Table 2)

```
SWE-bench Lite average cost per instance:
  Sonnet-4.5:    $1.30 (none) -> $1.51 (LLM) [+16%]
  GPT-5.2:       $0.32 (none) -> $0.43 (LLM) [+34%]
  GPT-5.1 Mini:  $0.18 (none) -> $0.22 (LLM) [+22%]
  Qwen3-30B:     $0.12 (none) -> $0.13 (LLM) [+8%]

AGENTbench average cost per instance:
  Sonnet-4.5:    $1.15 (none) -> $1.33 (LLM) -> $1.30 (human) [+16% / +13%]
  GPT-5.2:       $0.38 (none) -> $0.57 (LLM) -> $0.54 (human) [+50% / +42%]
  GPT-5.1 Mini:  $0.18 (none) -> $0.20 (LLM) -> $0.19 (human) [+11% / +6%]
  Qwen3-30B:     $0.13 (none) -> $0.15 (LLM) -> $0.15 (human) [+15% / +15%]
```

### Tool anchoring data

```
Tool usage when mentioned vs. not mentioned in context file:
  uv:                   1.6x/instance (mentioned) vs. <0.01x (not mentioned)
  Repo-specific tools:  2.5x/instance (mentioned) vs. <0.05x (not mentioned)
```

### AGENTbench dataset characteristics (Table 1)

```
138 instances from 12 repositories
Average PR description:     415.3 words (range: 5-4,961)
Average issue description:  211.6 words (range: 96-500)
Average codebase size:      3,337 files (range: 151-26,602)
Average PR patch:           118.9 lines edited (range: 12-1,973)
Average files edited:       2.5 (range: 1-23)
Average context file:       641 words (range: 24-2,003)
Average sections:           9.7 (range: 1-29)
Test coverage:              75% average (range: 2.5%-100%)
```

## Companion Study: Lulla et al. (ICSE JAWs 2026)

This source note also covers the related study by Lulla et al. as it addresses the same question from an efficiency (not correctness) angle.

**Paper**: "On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents"
**Authors**: Jai Lal Lulla (Singapore Management University), Seyedmoein Mohsenimofidi (Heidelberg University), Matthias Galster (University of Bamberg), Jie M. Zhang (King's College London), Sebastian Baltes (Heidelberg University), Christoph Treude (Singapore Management University)
**URL**: https://arxiv.org/abs/2601.20404
**Date**: January 28, 2026 (revised March 30, 2026)
**Venue**: ICSE JAWs 2026 (Journal Ahead Workshop), Rio de Janeiro, April 12-18, 2026

### Lulla et al. methodology
- **Agent**: OpenAI Codex (gpt-5.2-codex model) -- single agent only
- **Repos**: 10 repositories (from 132 candidates, filtered to those with root-level AGENTS.md)
- **Tasks**: 124 pull requests, each <= 100 LoC, <= 5 modified files
- **Design**: Paired within-task (same task run with and without AGENTS.md)
- **Context files**: Pre-existing developer-written AGENTS.md files (not auto-generated)
- **Isolation**: Docker environments, no state reuse

### Lulla et al. key results

```
Wall-clock time-to-completion:
  Mean:   162.94s (without) -> 129.91s (with) = -20.27%
  Median:  98.57s (without) ->  70.34s (with) = -28.64%
  Statistical significance: p < 0.05 (Wilcoxon signed-rank test)

Output tokens:
  Mean:   5,744.81 (without) -> 4,591.46 (with) = -20.08%
  Median: 2,925.00 (without) -> 2,440.00 (with) = -16.58%
  Statistical significance: p < 0.05

Input tokens:
  Mean:   353,010.01 (without) -> 318,651.51 (with) = -9.73%
  Median: 116,609.00 (without) -> 120,587.00 (with) = +3.41% (not significant)
```

### Lulla et al. critical limitations
- **Correctness NOT measured**: Only a manual sanity check of 50 random samples confirmed "non-empty, non-trivial code changes." The paper explicitly states: "A comprehensive evaluation of the output quality...is beyond the scope of this paper."
- **Single agent**: Only Codex tested. Generalization to other agents is unknown.
- **Small scope only**: PRs limited to <= 100 LoC. Effect on larger tasks is unknown.
- **Only developer-written files**: Does not test LLM-generated context files.

### Reconciling the two studies

The Gloaguen and Lulla studies appear to contradict each other but actually measure different things:

| Dimension | Gloaguen et al. | Lulla et al. |
|-----------|----------------|-------------|
| Measures | Task success rate (correctness) | Runtime and tokens (efficiency) |
| Context files | Both LLM-generated and developer-written | Developer-written only |
| Agents | 4 agents | 1 agent (Codex) |
| Task scope | Variable (SWE-bench range) | Small only (<= 100 LoC) |
| Benchmark | SWE-bench Lite + AGENTbench | 124 real PRs |
| Key finding | Context files hurt success, increase cost | Context files reduce runtime and tokens |

The reconciliation: developer-written AGENTS.md files may help agents work faster (fewer steps, less exploration) even though they do not reliably improve correctness on benchmarks. Gloaguen's cost increase finding measures total inference cost (more exploration, more testing), while Lulla's token reduction measures output tokens specifically. The agent generates fewer output tokens but may process more input tokens due to the context file itself.

## Cross-References

- **Corroborates**:
  - **blog-addyosmani-code-agent-orchestra (Claim 7)**: Osmani's secondhand summary is directionally correct. His "~3%" success reduction aligns with Gloaguen's 0.5-2% range (Osmani rounded up). His "~4% improvement" for developer-written files matches exactly. His "+20% cost" matches.
  - **guide/00-principles.md ("Deterministic Tools" section)**: The filter test and context-as-budget principles are directly supported by this paper's finding that auto-generated content is redundant with existing documentation.
  - **guide/02-harness-engineering.md ("Do not auto-generate your AGENTS.md" section)**: Directly supported with primary data.
  - **guide/03-safety-and-verification.md ("Gate 3: AGENTS.md as Living Guardrail")**: Supported.

- **Contradicts**:
  - **Partial contradiction with Lulla et al.**: Gloaguen finds context files increase cost; Lulla finds they reduce runtime and output tokens. Not a full contradiction (different metrics), but the surface-level narrative conflict requires careful framing in the guide.

- **Extends**:
  - **blog-addyosmani-code-agent-orchestra (Linked Source 1)**: Osmani's AGENTS.md post cited this study secondhand. We now have the primary data with per-model breakdowns, cost tables, and the documentation-removal experiment that Osmani did not highlight.

- **Novel**:
  - **The tool anchoring quantification** (uv: 1.6x vs 0.01x when mentioned/not). No other source quantifies the behavioral compliance rate of context file instructions.
  - **The documentation-removal experiment**: Showing that auto-generated content helps (+2.7%) only when docs are stripped proves redundancy definitively. This experiment is not cited in Osmani's coverage.
  - **The "no single repository shows significant impact" finding** (Figure 12). This caveat is absent from all secondhand coverage.
  - **Reasoning token overhead** (+22% for GPT-5.2): thinking overhead from context files, invisible in output token counts.
  - **AGENTbench as a benchmark**: 138 tasks from 12 niche repos with developer-written context files. Available for replication.
  - **Lulla et al. efficiency data**: The 28.64% median runtime reduction and 16.58% output token reduction with developer-written files. This provides a different angle than Gloaguen's correctness focus.

## Guide Impact

### Can we upgrade confidence grades?

**Short answer: No.** The existing [settled] tags on Claim 7 in blog-addyosmani-code-agent-orchestra and the guide chapters should be **downgraded to [emerging]**. Here is why:

1. **The Gloaguen paper is an arXiv preprint**, not peer-reviewed at a top venue. The SRI Lab has credibility, but the paper has not survived formal peer review.
2. **No confidence intervals or statistical significance tests** are reported for the headline success rate numbers (0.5%, 2%, 4%). The cost findings are more robust (mechanistic), but the success rate claims are thin.
3. **Per-repository variance is high**: "no single repository where the presence of context files has a significant impact." The averages mask heterogeneity.
4. **Python only**. No evidence for TypeScript, Rust, Go, etc.
5. **Single-shot task resolution only**. Real practitioners use AGENTS.md across multi-turn sessions and iterative workflows. The benchmark does not capture the "compound learning" value of maintained context files.
6. **The Lulla study has its own limitations**: single agent (Codex), small tasks only (<= 100 LoC), no correctness measurement, p < 0.05 without exact p-values.

The directional findings are credible and consistent enough to warrant [emerging] confidence:
- Auto-generated context files do not help and may hurt: [emerging]
- Developer-written files may provide marginal improvement: [emerging]
- Context files increase inference cost: [emerging] (close to [settled] -- mechanistically sound)
- Agents follow context file instructions with high compliance: [emerging] (close to [settled])

### Specific guide changes recommended

- **Chapter 00, "Deterministic Tools" section (lines 137-148)**: Change the two [settled] tags to [emerging]. The claim direction is correct but the evidence is a preprint with no significance tests on the headline numbers. Replace the secondhand citation `[source: blog-addyosmani-code-agent-orchestra, Claim 7]` with `[source: paper-gloaguen-agentsmd-effectiveness, Claims 1-2]`.

- **Chapter 02, "Do not auto-generate your AGENTS.md" section (lines 315-340)**: Change [settled] to [emerging] for the same reason. Add the documentation-removal finding as supporting evidence: "When repository documentation was stripped, LLM-generated files improved success by 2.7% -- proving the auto-generated content was redundant with what the agent could already read." Add the Lulla et al. efficiency finding as a counterpoint: "A separate study (Lulla et al.) found developer-written AGENTS.md reduced median runtime by 28.64%, suggesting that even if context files do not improve correctness, they may improve efficiency." Cite this source note directly instead of through Osmani.

- **Chapter 02, "Do not auto-generate your AGENTS.md" section (lines 330-333)**: The anchoring effect claim currently has [emerging] confidence. The quantitative data from this paper (uv: 1.6x vs 0.01x) strengthens it. Keep [emerging] but note this is now supported by primary data, not just Osmani's blog.

- **Chapter 03, "Gate 3: AGENTS.md as Living Guardrail" section (lines 285-298)**: Change [settled] to [emerging] on the success rate numbers. Add the per-repository variance caveat: "The 4% average improvement masks high per-repository variance; no single repository showed a statistically significant effect."

- **Chapter 00, "Context Is a Budget" section**: Add the reasoning token data: "Context files increase reasoning token usage by up to 22%, meaning the model spends more compute 'thinking' about instructions without producing better outcomes."

## Extraction Notes

- The full paper HTML was available at https://arxiv.org/html/2602.11988v1 and was read in detail. The arXiv abstract page and the SRI Lab publication page were also consulted.
- The Lulla et al. paper was available at https://arxiv.org/html/2601.20404v1 and was read for methodology, results, and limitations. It is included in this source note because it addresses the same research question and is cited alongside Gloaguen in Osmani's blog.
- The Gloaguen paper's code and benchmark are publicly available at https://github.com/eth-sri/agentbench. This enables replication and extension.
- I consulted secondary coverage (InfoQ, MarkTechPost, Upsun) for expert reactions and found one useful practitioner observation: writing context files forces articulation of implicit knowledge, benefiting human onboarding as much as AI assistance. This "dual-use" framing is not in the paper itself.
- The ClawSouls blog (which appeared to compare both studies) returned a 403 error and could not be accessed.
- **Key finding Osmani did NOT highlight**: The per-repository variance finding (no single repo shows significant impact) and the reasoning token overhead (+22%) are absent from Osmani's secondhand coverage. Both are important caveats.
- **Confidence grades in the guide should be downgraded**: The four places that cite this study as [settled] should be changed to [emerging]. An arXiv preprint with no significance tests on headline numbers does not meet the bar for [settled], regardless of the lab's reputation.
