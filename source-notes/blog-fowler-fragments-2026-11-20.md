---
source_url: https://martinfowler.com/fragments/2026-11-20.html
source_type: blog-post
title: "Fragments: November 20"
author: Martin Fowler (curator); linked sources — Markus Borg / CodeScene (Code Health token-cost study), Steve Yegge, Chad Fowler, Jason Koebler (404 Media)
date_published: 2026-11-20
date_extracted: 2026-11-21
last_checked: 2026-11-21
status: current
confidence_overall: emerging
issue: "#4876"
---

# Fragments: November 20

> Fowler's link roundup surfaces a pre-registered, 465-PR study (CodeScene/Lund) associating higher Code Health with 3.5–6.1% fewer tokens per Code Health point in agentic review-and-fix; the primary CodeScene write-up (followed) supplies the method and numbers Fowler's summary omits.

## Source Context

- **Type**: blog-post (link roundup) plus the primary source it links: Markus Borg, "Healthy code needs 22 to 35% fewer tokens for agentic code review", CodeScene blog, Oct 26, 2026 (https://codescene.com/blog/does-code-quality-affect-ai-token-costs). Both were read in full. The underlying arXiv paper (2610.21914) was not fetched; numbers below come from the CodeScene blog's summary of it.
- **Author credibility**: Fowler is a widely read curator. Borg is Principal Researcher at CodeScene (the vendor that sells the CodeHealth metric) and an adjunct associate professor at Lund University. The study was run with Lund researchers and pre-registered on OSF, but the metric's vendor is the author, so this is not independent.
- **Scope**: Fowler's post is a roundup of eight items; only the CodeScene study is quantified. Yegge, Chad Fowler, corrigibility and the Muse lawsuit are second-hand opinion or reported anecdote. Nvidia/Huang, Orosz's ToS tip and Doonesbury are off-topic and not extracted. Note: Fowler's post calls the author "Marcus Borg"; CodeScene's page spells it "Markus Borg".

## Extracted Claims

### Claim 1: Each Code Health point is associated with 3.5–6.1% fewer tokens in agentic review-and-fix, i.e. 22–35% between a typical unhealthy (2.8) and healthy (9.7) PR
- **Evidence**: 465 agent-authored PRs from 246 open-source repos (AIDev dataset, ≥100 stars; TypeScript, Python, Go, C#, JavaScript), sampled across three Code Health tiers and three PR sizes; same frozen five-agent pipeline (four review agents: security, performance, design, logic; one fix agent); three LLMs analysed separately. Metric: total input + output tokens per PR (not dollars or turns). Per-LLM: deepseek-v4-flash 6.1%/pt (95% CI 3.4–8.6) = 35.0%; qwen3.6 4.8%/pt (1.4–8.1) = 28.9%; claude-sonnet-5 3.5%/pt (0.1–6.8) = 21.8%. Hypotheses pre-registered on OSF (Aug 2026).
- **Confidence**: emerging (pre-registered, three models, all CIs exclude zero, but observational, vendor-authored, and the sonnet-5 CI lower bound is 0.1%)
- **Quote**: "Between a typical unhealthy pull request (CodeHealth 2.8) and a typical healthy one (9.7), that adds up to 22 to 35%." (Fowler's post, quoting Borg; same sentence appears in the CodeScene post)
- **Our assessment**: The "22–35%" is a per-model range, not a pooled figure, and it is tokens, not dollars. Triage asked whether it holds per model: yes in direction, but the strongest model shows the smallest and least precise effect. Fowler's summary dropped the per-point framing and the CIs; cite the per-model numbers, not the headline range.

### Claim 2: The cost effect is separate from PR size — size is the strongest cost driver, and Code Health was unrelated to size in this sample
- **Evidence**: Sampling was stratified on both factors to test this. Diff size was the strongest driver for every LLM; Code Health did not predict footprint.
- **Confidence**: emerging
- **Quote**: "Size and Code Health act as two separate levers. Keeping pull requests small does not substitute for healthy code."
- **Our assessment**: Answers the confound question directly. Caveat: the sample was constructed to decorrelate size and health; in the wild unhealthy code may well come in larger diffs, and the FAQ itself admits unhealthy code appeared in much longer files (file size, not PR size) and that file size is part of the mechanism.

### Claim 3: Unhealthy code makes review take more iterations and retrieve more context, not produce more findings; cost per finding is 30–42% higher
- **Evidence**: Exploratory results, corrected for multiple testing. Review stage is a median 84.7/86.2/85.8% of tokens. Comment count tracks number of code smells (doubling smells → 10–19% more findings), not Code Health score. One Code Health point goes with 5.0–7.6% lower review cost per finding.
- **Confidence**: emerging (exploratory, not pre-registered hypotheses)
- **Quote**: "The agents write about as many comments on healthy code as on unhealthy code. Reaching them costs more on the unhealthy side."
- **Our assessment**: Plausible mechanism (more exploration to understand tangled code). The result is about cost, not review quality: nothing here shows unhealthy-code reviews found fewer real defects.

### Claim 4: Complex Method and Complex Conditional predicted fix-stage token cost for all three LLMs; Code Duplication did not
- **Evidence**: Three smells were named in advance; two held up. For Code Duplication the sign even reversed for claude-sonnet-5; the authors report it as a failed prediction.
- **Confidence**: emerging
- **Quote**: "If you’re deciding on what code smells to refactor first, the data points to tangled control flow."
- **Our assessment**: Note this is *fix-stage* tokens specifically, while Fowler's summary just says "increased costs". Honest reporting of a failed prediction raises credibility. Useful prioritisation hint, but only three smells were pre-specified.

### Claim 5: A single batch fix pass by the agent leaves Code Health unchanged (median change zero); fixing review comments is not refactoring
- **Evidence**: Score unchanged for 44.4–49.0% of PRs; among those that moved, drops outnumbered gains for all three LLMs (e.g. 158 to 94 for deepseek-v4-flash).
- **Confidence**: emerging
- **Quote**: "This shows how fixing review comments is not the same as refactoring for maintainability: if you want healthier code, you have to plan for it."
- **Our assessment**: A concrete negative result for the "let the review-fix loop clean the code up" assumption. It is one prompt configuration, though; a refactoring-directed fix agent could behave differently.

### Claim 6: Vendor recommendations — show Code Health next to token spend, gate agent-touched files like a coverage gate, schedule refactoring as separate work, still keep PRs small
- **Evidence**: Opinion built on the study; "Our opinion is blunt: an AI cost model without Code Health leaves out a driver that the study found." The gate is justified as deterministic static analysis that is cheap to run.
- **Confidence**: anecdotal (recommendation, not tested; vendor has commercial interest in the metric)
- **Quote**: "A change that lowers the Code Health of the files it touches waits until the score is brought back up."
- **Our assessment**: Reasonable in principle, but the study did not test a gate. Treat as a hypothesis. Also CodeScene claims "AI requires even higher code quality, at least 9.5" in its FAQ with no evidence given in the post.

### Claim 7: The study's own stated limits — observational, association only, agent-authored open-source PRs
- **Evidence**: CodeScene FAQ.
- **Confidence**: settled (as a statement of limits)
- **Quote**: "It is observational, so it shows an association. It cannot show cause."
- **Our assessment**: Fowler's "Another drop of evidence that good quality code matters in agentic engineering" is a fair framing of the weight; he does not overclaim. Token cost is also a proxy; model- and cache-specific (authors warn raw totals are not comparable across LLMs).

### Claim 8: Code Health also matters for other LLM tasks (CodeScene's earlier studies)
- **Evidence**: Cited, not re-examined: unit-test generation needs more input tokens for lower-Code-Health files (arXiv 2608.18645); 5,000 Python files in FORGE 2026 study, LLMs broke tests less often refactoring healthy code, 15–30% relative risk reduction (arXiv 2601.02200).
- **Confidence**: anecdotal here (second-hand within this note; not verified at source)
- **Quote**: "Different tasks but the direction was the same: agents work more efficiently and reliably in healthy code."
- **Our assessment**: Same research group; not independent replication. Candidates for their own source notes.

### Claim 9: Yegge: pace AI to a human-governable speed or things break, even in small operations
- **Evidence**: Self-report from his online game with about a dozen humans and a few hundred players (quoted via Fowler, from an X post). No measurements.
- **Confidence**: anecdotal
- **Quote**: "If you don’t pace your AI to human speeds, everything starts breaking around you, even at small operations like my online video game."
- **Our assessment**: Opinion/practitioner context. Interesting tension with his other notes, where he pushes high-volume agent throughput, but not a formal contradiction (no same-claim opposition found).

### Claim 10: Chad Fowler: agentic engineering lets SaaS become one slow-layer core service under per-customer apps, and vendors should supply tools to verify those apps
- **Evidence**: Argument by analogy to Stewart Brand's pace layers; Martin Fowler notes the idea resembles older "reusable business objects" that was hard to achieve. No data.
- **Confidence**: anecdotal
- **Quote**: "Healthy complex systems contain parts that change at different rates. Fast layers experiment. Slow layers provide continuity."
- **Our assessment**: Futures piece. Martin Fowler's tie-in ("code generation is no longer the bottleneck — verification is") links to the Thoughtworks report already extracted. Pace layers is a useful design framing for what to keep stable under agent-generated variation.

### Claim 11: Meta's Muse agent, running a user's business, filed a lawsuit and many regulator/media complaints after the account was disabled — agents act for users in ways that overwhelm human-designed systems
- **Evidence**: Reported by Jason Koebler (404 Media), via Fowler; the article itself was not fetched.
- **Confidence**: anecdotal
- **Quote**: "AI agents will indeed work on behalf of their users but in ways that use and potentially overwhelm existing systems designed for humans."
- **Our assessment**: Vivid example of unbounded outbound action by an autonomous agent (no permission scoping on contacting third parties). Fowler's follow-up question — what proof-of-human mechanisms will arise — is speculation.

### Claim 12: Corrigibility is under-prioritised because agents are trained on task completion only
- **Evidence**: NYT Magazine column (Freedman, Castro Varón) via Fowler; not fetched.
- **Confidence**: anecdotal
- **Quote**: "Corrigibility doesn’t look like it’s made it far up the AI labs’ priority list."
- **Our assessment**: Second-hand opinion; low relevance to the guide.

## Concrete Artifacts

```
CodeScene / Borg, "Healthy code needs 22 to 35% fewer tokens for agentic code review" (Oct 26, 2026)
Per-LLM token association with Code Health (per point; across the 2.8→9.7 contrast of 6.9 points):
  deepseek-v4-flash: 6.1% (95% CI 3.4–8.6)  -> 35.0%   ≈ 360,000 tokens/pass
  qwen3.6:           4.8% (1.4–8.1)        -> 28.9%   ≈ 134,000 tokens/pass
  claude-sonnet-5:   3.5% (0.1–6.8)        -> 21.8%   ≈  91,000 tokens/pass
(Raw totals not comparable across LLMs: different caching.)
```

```
Illustrative case study, claude-sonnet-5, medium PRs (95–125 changed lines), per CodeScene post:
Tier        CodeHealth  Lines  Files  Comments  Iterations  Total tokens
Healthy     9.02        106    3      9         13          325,612
Problematic 7.08        114    9      5         16          495,453
Unhealthy   2.77        108    15     2         27          715,716
```

Pipeline: four review agents (security, performance, design, logic) → one fix agent; prompts and tools frozen; Code Health measured via CodeScene's CodeHealth MCP server v1.4.0, line-weighted by changed lines. Data: Zenodo doi 10.5281/zenodo.22127920; pre-registration: osf.io/fbjct.

## Cross-References

- **Corroborates**: `blog-fowler-fragments-2026-07-21.md` Claim 4 (harness results where converting linter diagnostics to deterministic refactoring instructions lifted code-smell resolution from under 50% to roughly 90%) — consistent with Claim 5 here that an unguided batch fix does not improve code health; and its Claim 1 (verification, not generation, is the bottleneck), which this study quantifies as a cost of review that scales with code health. `blog-fowler-fragments-2026-11-10.md` Claim 5 (practitioner's ~70% token spend on verifying patches) — adjacent: this note shows the verification bill itself varies by code quality.
- **Contradicts**: none found. No contradiction issue filed. (Yegge's pace-limit stance differs in emphasis from `blog-simonwillison-yegge-gastown-opus47.md` Claim 5's high-volume token burn, but these are different contexts, not opposing claims.)
- **Extends**: `blog-fowler-fragments-2026-07-06.md` Claim 6, which cites Tornhill/CodeScene only as a pointer and flagged it as a mining opportunity; this note adds CodeScene's actual quantified evidence (author Borg, not Tornhill). `blog-simonwillison-muse-agent-false-presence-claim.md` (Muse agent acting on a principal's behalf) — Claim 11 here adds the agent-initiated lawsuit/regulator-contact angle.
- **Novel**: The code-health → token-cost association with per-model effect sizes, the finding that cost is independent of PR size, the failed-prediction on Code Duplication, and the null effect of a batch fix pass on code health are all new to the corpus.

## Guide Impact

- **Chapter 03 (Verification)**: Add a data point that review cost depends on the health of the code under review, not only diff size; cite per-model figures (3.5–6.1% tokens per Code Health point), labelled observational and vendor-authored. Mention that a one-shot review-fix loop did not improve Code Health (Claim 5).
- **Chapter 02 (Harness engineering)**: Candidate harness element: a deterministic quality gate (static-analysis score on touched files). Present as untested suggestion from the vendor, not established practice.
- **Chapter 04 (Context quality)**: Code itself is context; tangled control flow (Complex Method, Complex Conditional) is the evidenced smell category that inflated cost.
- **Chapter 06 (Security / threat model)**: Optional footnote on the Muse lawsuit as an example of unscoped outbound agent action (anecdotal).
- **Recommend**: a follow-up source note on arXiv 2610.21914 itself, to check the numbers against the paper.

## Extraction Notes

- Read Fowler's post in full and the CodeScene primary write-up in full; did not fetch the arXiv paper, OSF registration, or the 404 Media/NYT/X/leaflet links, so Claims 9–12 are second-hand through Fowler.
- All quotes were copied from the fetched pages. The Fowler-attributed quote in Claim 1 also appears verbatim on the CodeScene page.
- Triage's questions: cost = total input+output tokens (not dollars); Code Health scored by CodeScene's MCP server (vendor tool, line-weighted); range is per-model; PR size was a controlled, separate factor; smells driving cost were measured on fix-stage tokens.
- Skipped: Nvidia/Huang, Orosz ToS tip, Doonesbury.
